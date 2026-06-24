#!/usr/bin/env python3
"""H_008 — accelerator-source flux/average-power wall: at present LPA repetition
rates the undulator's average in-band EUV power is orders of magnitude below the
~167 W that 100 WPH HVM requires. The compact-accelerator path is flux-limited,
not wavelength-limited (the honest counter to H_004/H_006/H_007).

Deterministic, stdlib-only. $0 local.
    python3 state/h008_accelerator_flux_wall_2026_06_24/run_h008.py
"""

from __future__ import annotations

import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "tool"))

from lumen_optics import Falsifier, average_power, evaluate, power_for_throughput

# --- pre-registered parameters (FROZEN 2026-06-24) ---------------------------
HVM_WPH = 100.0            # HVM throughput floor (H_005)
REF_POWER_W = 250.0        # 13.5nm in-band power class
REF_WPH = 150.0            # 13.5nm WPH at REF_POWER
LPA_REP_HZ = 1.0e3         # present high-rep LPA frontier (~kHz)
LPA_PULSE_EUV_J = 1.0e-6   # representative in-band EUV per shot (~1 µJ, optimistic)
LPA_REP_FUTURE_HZ = 1.0e5  # pushed rep rate (~100 kHz, LPP-class)


def main() -> int:
    required_w = power_for_throughput(HVM_WPH, REF_POWER_W, REF_WPH)
    lpa_now_w = average_power(LPA_REP_HZ, LPA_PULSE_EUV_J)
    lpa_pushed_w = average_power(LPA_REP_FUTURE_HZ, LPA_PULSE_EUV_J)
    gap_now = required_w / lpa_now_w
    gap_pushed = required_w / lpa_pushed_w

    metrics = {
        "required_w": required_w,
        "lpa_now_w": lpa_now_w,
        "lpa_pushed_w": lpa_pushed_w,
        "gap_now": gap_now,
        "gap_pushed": gap_pushed,
    }

    falsifiers = [
        Falsifier("F-FLX-1 WALL", lambda m: not (m["lpa_now_w"] < m["required_w"]),
                  "present LPA avg power must fall below HVM requirement (the wall)"),
        Falsifier("F-FLX-2 SEVERE", lambda m: not (m["gap_now"] >= 100.0),
                  "gap must be >= 100x (order-of-magnitude wall, not a tweak)"),
        Falsifier("F-FLX-3 REP-LEVER", lambda m: not (m["lpa_pushed_w"] < m["required_w"]),
                  "even ~100x rep-rate must stay below requirement (not a trivial fix)"),
        Falsifier("F-FLX-4 MONOTONE", lambda m: not (m["lpa_pushed_w"] > m["lpa_now_w"]),
                  "higher rep rate must raise average power"),
        Falsifier("F-FLX-5 BOUNDS", lambda m: not all(v > 0 for v in
                  (m["required_w"], m["lpa_now_w"], m["lpa_pushed_w"])),
                  "all powers positive"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_008 accelerator-source flux / average-power wall")
    print(f"  HVM requires ~{required_w:.0f} W in-band (for {HVM_WPH:.0f} WPH)")
    print(f"  LPA now ({LPA_REP_HZ:.0e} Hz x {LPA_PULSE_EUV_J*1e6:.0f} µJ) = {lpa_now_w*1e3:.3f} mW  (gap {gap_now:.0f}x)")
    print(f"  LPA pushed ({LPA_REP_FUTURE_HZ:.0e} Hz) = {lpa_pushed_w:.3f} W  (gap {gap_pushed:.0f}x)")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<16} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
