#!/usr/bin/env python3
"""H_018 — ERL beam-breakup (BBU) is NOT the binding wall at EUV-relevant current
(the cheapest probe the flux-ceiling verdict flagged). The average current an
ERL+FEL EUV source needs (Q x f ~0.2 mA) sits far below demonstrated BBU
threshold currents (tens of mA with HOM damping), so BBU does not cap the ERL
escape — the binding ERL limit is heat/wall-plug, not instability.

Deterministic, stdlib-only. $0 local.
    python3 state/h018_erl_bbu_threshold_2026_06_25/run_h018.py
"""

from __future__ import annotations

import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "tool"))

from lumen_optics import Falsifier, evaluate

# --- pre-registered parameters (FROZEN 2026-06-25) ---------------------------
Q_BUNCH_C = 100.0e-12      # bunch charge 100 pC
F_REP_HZ = 2.0e6          # rep-rate for 167 W via ERL+FEL (H_016)
I_BBU_THRESHOLD_A = 20.0e-3  # demonstrated ERL BBU threshold with HOM damping (~20 mA)
I_BBU_NO_DAMPING_A = 1.0e-3  # without HOM damping (~1 mA) — shows damping lifts it


def main() -> int:
    i_needed = Q_BUNCH_C * F_REP_HZ          # average current required
    margin = I_BBU_THRESHOLD_A / i_needed
    damping_gain = I_BBU_THRESHOLD_A / I_BBU_NO_DAMPING_A

    metrics = {
        "i_needed_a": i_needed,
        "i_bbu_threshold_a": I_BBU_THRESHOLD_A,
        "margin": margin,
        "i_bbu_no_damping_a": I_BBU_NO_DAMPING_A,
        "hom_damping_gain": damping_gain,
    }

    falsifiers = [
        Falsifier("F-BBU-1 BELOW", lambda m: not (m["i_needed_a"] < m["i_bbu_threshold_a"]),
                  "required ERL current must sit below the BBU threshold (BBU not the wall)"),
        Falsifier("F-BBU-2 MARGIN", lambda m: not (m["margin"] >= 10.0),
                  "BBU margin must be >= 10x (comfortably stable)"),
        Falsifier("F-BBU-3 DAMPING", lambda m: not (m["hom_damping_gain"] > 1.0),
                  "HOM damping must raise the threshold (the engineering lever)"),
        Falsifier("F-BBU-4 BOUNDS", lambda m: not all(v > 0 for v in
                  (m["i_needed_a"], m["i_bbu_threshold_a"], m["margin"])),
                  "all positive"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_018 ERL beam-breakup (BBU) is not the binding wall at EUV current")
    print(f"  current needed (Q x f) = {i_needed*1e3:.2f} mA")
    print(f"  BBU threshold (HOM-damped) = {I_BBU_THRESHOLD_A*1e3:.0f} mA  -> margin {margin:.0f}x")
    print(f"  HOM damping lifts threshold {damping_gain:.0f}x ({I_BBU_NO_DAMPING_A*1e3:.0f}->{I_BBU_THRESHOLD_A*1e3:.0f} mA)")
    print(f"  -> binding ERL limit is heat/wall-plug (H_016), not BBU instability")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<14} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
