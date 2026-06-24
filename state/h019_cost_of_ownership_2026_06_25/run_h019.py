#!/usr/bin/env python3
"""H_019 — cost-of-ownership conjunction (economic prediction Q3, the campaign's
cheapest terminal probe). A compact coherent/ERL source beats LPP $/wafer-layer
ONLY when both levers fire: efficiency η >= ~4x LPP (M6) AND amortization across
M >= ~3 scanners (M9). Neither lever alone suffices.

Deterministic, stdlib-only. $0 local. Normalized cost units (LPP = 1.0).
    python3 state/h019_cost_of_ownership_2026_06_25/run_h019.py
"""

from __future__ import annotations

import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "tool"))

from lumen_optics import Falsifier, cost_of_ownership, evaluate

# --- pre-registered parameters (FROZEN 2026-06-25, normalized) ---------------
COST_LPP = 1.0             # LPP $/wafer-layer baseline (capex 0.4 + opex 0.6)
CAPEX_UNIT = 1.2          # coherent bespoke unit CAPEX share (higher than LPP)
OPEX_BASE = 0.6           # coherent OPEX_energy at eta_ratio=1 (same as LPP energy share)
ETA_WIN, M_WIN = 4.0, 3   # both levers fired
ETA_ONLY, M_ONLY = 4.0, 1  # efficiency only (no amortization)
M_ONLY_ETA = 1.0          # amortization only (no efficiency gain)


def main() -> int:
    c_both = cost_of_ownership(CAPEX_UNIT, OPEX_BASE, ETA_WIN, M_WIN)
    c_eta_only = cost_of_ownership(CAPEX_UNIT, OPEX_BASE, ETA_ONLY, M_ONLY)
    c_amort_only = cost_of_ownership(CAPEX_UNIT, OPEX_BASE, M_ONLY_ETA, M_WIN)
    # M8 floor: as N->inf the OPEX_energy term never vanishes
    c_infinite_scanners = cost_of_ownership(CAPEX_UNIT, OPEX_BASE, ETA_WIN, 10_000_000)
    m8_floor = OPEX_BASE / ETA_WIN

    metrics = {
        "cost_lpp": COST_LPP,
        "cost_both_levers": c_both,
        "cost_eta_only": c_eta_only,
        "cost_amort_only": c_amort_only,
        "cost_infinite_scanners": c_infinite_scanners,
        "m8_opex_floor": m8_floor,
    }

    falsifiers = [
        Falsifier("F-COO-1 WIN", lambda m: not (m["cost_both_levers"] < m["cost_lpp"]),
                  "both levers (eta>=4x AND M>=3) must beat LPP"),
        Falsifier("F-COO-2 ETA-INSUFFICIENT", lambda m: not (m["cost_eta_only"] >= m["cost_lpp"]),
                  "efficiency alone (M=1) must NOT beat LPP"),
        Falsifier("F-COO-3 AMORT-INSUFFICIENT", lambda m: not (m["cost_amort_only"] >= m["cost_lpp"]),
                  "amortization alone (eta=1) must NOT beat LPP"),
        Falsifier("F-COO-4 CONJUNCTION", lambda m: not (m["cost_both_levers"] < m["cost_lpp"]
                  <= min(m["cost_eta_only"], m["cost_amort_only"])),
                  "the win requires BOTH levers (conjunction, not either alone)"),
        Falsifier("F-COO-5 M8-FLOOR", lambda m: abs(m["cost_infinite_scanners"] - m["m8_opex_floor"]) > 1e-6,
                  "as scanners->inf the cost asymptotes to the M8 waste-heat OPEX floor (never 0)"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_019 cost-of-ownership conjunction (economic Q3, normalized LPP=1.0)")
    print(f"  LPP baseline = {COST_LPP:.2f}")
    print(f"  coherent BOTH (eta x{ETA_WIN:.0f}, M={M_WIN}) = {c_both:.2f}  -> {'WIN' if c_both<1 else 'lose'}")
    print(f"  coherent eta-only (M=1)   = {c_eta_only:.2f}  -> {'win' if c_eta_only<1 else 'LOSE'}")
    print(f"  coherent amort-only (eta=1) = {c_amort_only:.2f}  -> {'win' if c_amort_only<1 else 'LOSE'}")
    print(f"  M->inf asymptote = {c_infinite_scanners:.3f} = M8 OPEX floor {m8_floor:.3f} (never 0)")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<22} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
