#!/usr/bin/env python3
"""H_024 — cooling is the clean lever, raising the FEL Pierce rho is a TRAP. The
H_023 cross-coupling has two knobs: energy-spread cooling (sigma) and the FEL
Pierce parameter (rho). Deeper cooling widens BOTH margins (FEL rho/sigma AND ERL
acceptance/sqrt(sigma^2+rho^2)); raising rho widens the FEL margin but CRUSHES the
ERL energy-acceptance margin, and past a crossover rho the recovery fails. So the
combination's FEL beam-quality link is opened by cooling, not by rho.

Deterministic, stdlib-only. $0 local.
    python3 state/h024_cooling_vs_rho_2026_06_25/run_h024.py
"""

from __future__ import annotations

import json
import math
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "tool"))

from lumen_optics import Falsifier, evaluate

# --- pre-registered parameters (FROZEN 2026-06-25) ---------------------------
RHO_BASE = 0.010           # baseline FEL Pierce parameter
SIGMA_BASE = 0.0085        # baseline cooled energy spread (H_013/H_023)
SIGMA_DEEP = 0.0050        # deeper cooling target
RHO_RAISED = 0.020         # the "trap": raise rho instead of cooling
ERL_ACCEPT = 0.020         # ERL energy acceptance


def fel_margin(sigma, rho):
    return rho / sigma


def erl_margin(sigma, rho):
    return ERL_ACCEPT / math.sqrt(sigma ** 2 + rho ** 2)


def main() -> int:
    # baseline (H_023)
    fel0, erl0 = fel_margin(SIGMA_BASE, RHO_BASE), erl_margin(SIGMA_BASE, RHO_BASE)
    # lever A: deeper cooling
    fel_cool, erl_cool = fel_margin(SIGMA_DEEP, RHO_BASE), erl_margin(SIGMA_DEEP, RHO_BASE)
    # lever B (trap): raise rho
    fel_rho, erl_rho = fel_margin(SIGMA_BASE, RHO_RAISED), erl_margin(SIGMA_BASE, RHO_RAISED)
    # crossover rho where ERL margin == 1 at baseline sigma
    rho_crossover = math.sqrt(ERL_ACCEPT ** 2 - SIGMA_BASE ** 2)

    metrics = {
        "fel_base": fel0, "erl_base": erl0,
        "fel_cooled": fel_cool, "erl_cooled": erl_cool,
        "fel_raised_rho": fel_rho, "erl_raised_rho": erl_rho,
        "rho_crossover": rho_crossover,
    }

    falsifiers = [
        Falsifier("F-CR-1 COOLING-WINS", lambda m: not (m["fel_cooled"] >= 1.5 and m["erl_cooled"] >= 1.5),
                  "deeper cooling must lift BOTH margins >= 1.5x (the clean lever)"),
        Falsifier("F-CR-2 RHO-TRAP", lambda m: not (m["erl_raised_rho"] < 1.0),
                  "raising rho must crush the ERL margin below 1 (recovery fails — the trap)"),
        Falsifier("F-CR-3 COOLING-MONOTONE",
                  lambda m: not (m["fel_cooled"] > m["fel_base"] and m["erl_cooled"] > m["erl_base"]),
                  "cooling must improve BOTH margins (same direction)"),
        Falsifier("F-CR-4 RHO-OPPOSED",
                  lambda m: not (m["fel_raised_rho"] > m["fel_base"] and m["erl_raised_rho"] < m["erl_base"]),
                  "raising rho must improve FEL but worsen ERL (opposed directions = trap)"),
        Falsifier("F-CR-5 CROSSOVER", lambda m: not (RHO_BASE < m["rho_crossover"] < RHO_RAISED),
                  "the ERL-fail crossover rho must lie between baseline and the raised value"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_024 cooling is the clean lever; raising rho is a trap")
    print(f"  baseline (sigma {SIGMA_BASE*100:.2f}%, rho {RHO_BASE*100:.1f}%): FEL {fel0:.2f}x · ERL {erl0:.2f}x")
    print(f"  deeper cooling (sigma {SIGMA_DEEP*100:.2f}%):  FEL {fel_cool:.2f}x · ERL {erl_cool:.2f}x   (both UP)")
    print(f"  raise rho ({RHO_RAISED*100:.1f}%) [TRAP]:        FEL {fel_rho:.2f}x · ERL {erl_rho:.2f}x   (ERL FAILS <1)")
    print(f"  ERL-fail crossover at rho = {rho_crossover*100:.2f}%")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<20} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
