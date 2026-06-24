#!/usr/bin/env python3
"""H_023 — ERL<->FEL cross-coupling (deepening H_022's weakest link, L1). H_022
multiplied separately-verified levers; this checks they CO-EXIST on one beam:
(1) the FEL gain condition sigma_gamma/gamma < rho must be met by the COOLED beam
    (H_013, 0.85%) at the high-current LPA Pierce parameter (rho ~ 1%);
(2) the ERL must energy-recover the POST-FEL beam (spread broadened by ~rho) within
    its energy acceptance.
Finding: both hold, but the FEL beam-quality coupling is the TIGHTEST margin — the
binding cross-coupling of the combination (not flux, not CAPEX).

Deterministic, stdlib-only. $0 local.
    python3 state/h023_erl_fel_crosscoupling_2026_06_25/run_h023.py
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
SIGMA_COOLED = 0.0085      # cooled energy spread (H_013 output)
FEL_RHO = 0.010           # FEL Pierce parameter, high-current LPA regime (~1%)
FEL_SAT_SPREAD = 0.010    # FEL-saturation-induced spread on the spent beam (~rho)
ERL_ACCEPTANCE = 0.020    # ERL energy acceptance (~2%, lattice-dependent)


def main() -> int:
    # (1) FEL gain: cooled beam must be inside the Pierce bandwidth
    fel_margin = FEL_RHO / SIGMA_COOLED
    fel_ok = SIGMA_COOLED < FEL_RHO
    # (2) ERL recovery: post-FEL spread must be inside the ERL acceptance
    sigma_post = math.sqrt(SIGMA_COOLED ** 2 + FEL_SAT_SPREAD ** 2)
    erl_margin = ERL_ACCEPTANCE / sigma_post
    erl_ok = sigma_post < ERL_ACCEPTANCE

    metrics = {
        "sigma_cooled": SIGMA_COOLED,
        "fel_rho": FEL_RHO,
        "fel_margin": fel_margin,
        "sigma_post_fel": sigma_post,
        "erl_acceptance": ERL_ACCEPTANCE,
        "erl_margin": erl_margin,
        "fel_is_tightest": fel_margin < erl_margin,
    }

    falsifiers = [
        Falsifier("F-CC-1 FEL-GAIN", lambda m: not m["sigma_cooled"] < m["fel_rho"],
                  "cooled beam (H_013) must sit inside the FEL Pierce bandwidth (gain survives)"),
        Falsifier("F-CC-2 ERL-ACCEPT", lambda m: not (m["sigma_post_fel"] < m["erl_acceptance"]),
                  "post-FEL spread must sit inside the ERL energy acceptance (recovery survives)"),
        Falsifier("F-CC-3 FEL-TIGHTEST", lambda m: not m["fel_is_tightest"],
                  "FEL beam-quality margin must be the tightest (the binding cross-coupling)"),
        Falsifier("F-CC-4 POSITIVE-MARGIN", lambda m: not (m["fel_margin"] > 1.0 and m["erl_margin"] > 1.0),
                  "both couplings must hold with margin > 1 (combination is consistent)"),
        Falsifier("F-CC-5 BOUNDS", lambda m: not all(v > 0 for v in
                  (m["fel_margin"], m["erl_margin"], m["sigma_post_fel"])),
                  "all positive"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_023 ERL<->FEL cross-coupling (deepening H_022 weakest link)")
    print(f"  FEL gain: cooled {SIGMA_COOLED*100:.2f}% < rho {FEL_RHO*100:.1f}%  -> margin {fel_margin:.2f}x  ({'OK' if fel_ok else 'WALL'})")
    print(f"  ERL recovery: post-FEL {sigma_post*100:.2f}% < acceptance {ERL_ACCEPTANCE*100:.1f}%  -> margin {erl_margin:.2f}x  ({'OK' if erl_ok else 'WALL'})")
    print(f"  binding cross-coupling = FEL beam-quality (margin {fel_margin:.2f}x < ERL {erl_margin:.2f}x)")
    print(f"  -> combination is consistent, but FEL beam-quality is the tightest link (deeper cooling buys margin)")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<20} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
