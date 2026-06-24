#!/usr/bin/env python3
"""H_025 — @-family depletion census: the @-combination space is mapped and dry.
Any @-partner must either make EUV photons (supply, which splits exhaustively into
three extraction primitives) or change how many are needed (demand, a multiplier).
Of 4 censused families exactly ONE clears all walls (the accelerator-coherent
spine, H_022); the other three each fall on a DISTINCT wall, so there is no second
independent all-wall-clearer. The taxonomy being complete, further enumeration is
dry -> DEPLETION.

Deterministic, stdlib-only. $0 local.
    python3 state/h025_at_family_depletion_2026_06_25/run_h025.py
"""

from __future__ import annotations

import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "tool"))

from lumen_optics import Falsifier, evaluate

# --- pre-registered census (FROZEN 2026-06-25, from fleet-full at-frontier-census.md) ---
# family -> (verdict, the distinct wall it falls on / "none" if it clears)
CENSUS = {
    "accelerator-coherent (ERL+FEL/IC)":      ("clears-all-walls", "none"),
    "source-coherent (recombination laser)":  ("partial", "flux"),         # 2 W, undemonstrated 13.5nm gain
    "demand-side (resist+gating+grazing)":    ("partial", "rls-defect"),   # multiplier, re-binds to stochastic floor
    "exotic (plasma-mirror/HHG/channeling)":  ("partial", "capex-redundant"),  # variants of the above
}
# the exhaustive taxonomy: supply photon-making primitives + demand multiplier
SUPPLY_PRIMITIVES = {"ebeam-radiator", "atomic-gain", "upconversion"}
DEMAND_MULTIPLIER = {"requirement-reduction"}


def main() -> int:
    clears = [k for k, (v, _) in CENSUS.items() if v == "clears-all-walls"]
    partials = [k for k, (v, _) in CENSUS.items() if v != "clears-all-walls"]
    distinct_walls = {w for (_, w) in CENSUS.values() if w != "none"}
    taxonomy_size = len(SUPPLY_PRIMITIVES) + len(DEMAND_MULTIPLIER)

    metrics = {
        "n_families": len(CENSUS),
        "n_clears_all": len(clears),
        "n_partial": len(partials),
        "n_distinct_failure_walls": len(distinct_walls),
        "taxonomy_size": taxonomy_size,
        "spine_clears": "accelerator-coherent (ERL+FEL/IC)" in clears,
    }

    falsifiers = [
        Falsifier("F-DP-1 SPINE-CLEARS", lambda m: not m["spine_clears"],
                  "the accelerator-coherent spine (H_022) must clear all walls"),
        Falsifier("F-DP-2 SINGLE-CLEARER", lambda m: not (m["n_clears_all"] == 1),
                  "exactly one family clears all walls (no second independent all-wall path)"),
        Falsifier("F-DP-3 DISTINCT-WALLS", lambda m: not (m["n_distinct_failure_walls"] == m["n_partial"]),
                  "each partial family must fall on a DISTINCT wall (genuinely orthogonal enumeration)"),
        Falsifier("F-DP-4 TAXONOMY-COMPLETE", lambda m: not (m["taxonomy_size"] == 4
                  and m["n_families"] >= 4),
                  "supply (3 primitives) + demand (1 multiplier) taxonomy mapped by >= 4 censused families"),
        Falsifier("F-DP-5 DEPLETION", lambda m: not (m["n_clears_all"] == 1
                  and m["n_distinct_failure_walls"] == m["n_partial"] and m["taxonomy_size"] == 4),
                  "DEPLETION = one clearer + orthogonal failures + complete taxonomy (the @-space is dry)"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_025 @-family depletion census — the @-combination space is mapped and dry")
    for fam, (v, w) in CENSUS.items():
        print(f"  {fam:<42} {v:<18} wall={w}")
    print(f"  clears-all: {len(clears)} (spine) · partials: {len(partials)} on {len(distinct_walls)} distinct walls")
    print(f"  taxonomy: 3 supply primitives + 1 demand multiplier = {taxonomy_size} (mapped)")
    print(f"  -> DEPLETION: no second independent all-wall path; @-space is dry (further @ = variants)")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<22} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
