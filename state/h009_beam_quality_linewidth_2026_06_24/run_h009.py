#!/usr/bin/env python3
"""H_009 — beam energy spread broadens the undulator line: a ~1% LPA energy
spread broadens delta_lambda/lambda to ~2%, which fills (and exceeds) the 2%
in-band EUV budget and kills higher harmonics — feeding the H_008 flux wall.

Deterministic, stdlib-only. $0 local.
    python3 state/h009_beam_quality_linewidth_2026_06_24/run_h009.py
"""

from __future__ import annotations

import json
import math
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "tool"))

from lumen_optics import (
    Falsifier,
    energy_spread_broadening,
    evaluate,
    undulator_natural_linewidth,
)

# --- pre-registered parameters (FROZEN 2026-06-24) ---------------------------
SIGMA_GAMMA_REL = 0.01     # ~1% LPA electron energy spread (representative)
N_PERIODS = 100            # undulator periods
EUV_INBAND_BW = 0.02       # 2% in-band budget EUV optics accept


def total_width(harmonic: int) -> float:
    nat = undulator_natural_linewidth(harmonic, N_PERIODS)
    bro = energy_spread_broadening(SIGMA_GAMMA_REL)
    return math.sqrt(nat ** 2 + bro ** 2), nat, bro


def main() -> int:
    tot1, nat1, bro1 = total_width(1)
    tot3, nat3, _ = total_width(3)

    metrics = {
        "sigma_gamma_rel": SIGMA_GAMMA_REL,
        "natural_n1": nat1,
        "broadening": bro1,
        "total_n1": tot1,
        "natural_n3": nat3,
        "total_n3": tot3,
        "euv_inband_bw": EUV_INBAND_BW,
    }

    falsifiers = [
        Falsifier("F-BQ-1 DOMINATE", lambda m: not (m["broadening"] >= m["natural_n1"]),
                  "energy-spread broadening must dominate the natural line"),
        Falsifier("F-BQ-2 OVERFILL", lambda m: not (m["total_n1"] > m["euv_inband_bw"]),
                  "total width must exceed the 2% in-band budget (flux leaks out)"),
        Falsifier("F-BQ-3 HARMONIC", lambda m: not (m["broadening"] > m["natural_n3"]),
                  "at n=3 the energy spread must swamp the (narrower) natural line"),
        Falsifier("F-BQ-4 MONOTONE",
                  lambda m: not (energy_spread_broadening(0.005) < m["broadening"]),
                  "lower energy spread must narrow the line"),
        Falsifier("F-BQ-5 BOUNDS", lambda m: not all(v > 0 for v in
                  (m["natural_n1"], m["broadening"], m["total_n1"])),
                  "all widths positive"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_009 beam energy spread -> undulator linewidth")
    print(f"  sigma_gamma/gamma = {SIGMA_GAMMA_REL*100:.1f}%  (N={N_PERIODS} periods)")
    print(f"  n=1: natural {nat1*100:.2f}% (+) spread {bro1*100:.2f}% = total {tot1*100:.2f}%  (budget {EUV_INBAND_BW*100:.0f}%)")
    print(f"  n=3: natural {nat3*100:.2f}% vs spread {bro1*100:.2f}% -> spread swamps harmonic")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<16} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
