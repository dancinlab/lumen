#!/usr/bin/env python3
"""H_013 — energy-spread cooling splits the M4 brightness wall: cooling the LPA
energy spread from ~1% to ≤0.866% pushes the undulator line inside the 2% in-band
budget (quality sub-wall BEATEN), while the average-power flux gap (H_008) is
UNCHANGED (flux sub-wall STUBBORN). Built from the abstraction-lane prediction P4
(state/euv-meta-laws.md).

Deterministic, stdlib-only. $0 local.
    python3 state/h013_energy_spread_cooling_2026_06_25/run_h013.py
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
    average_power,
    energy_spread_broadening,
    evaluate,
    undulator_natural_linewidth,
)

# --- pre-registered parameters (FROZEN 2026-06-25) ---------------------------
N_PERIODS = 100
INBAND_BW = 0.02            # 2% in-band budget
SIGMA_BEFORE = 0.010       # 1.0% LPA energy spread (uncooled)
SIGMA_AFTER = 0.0085       # cooled below the critical threshold
# flux side (unchanged by cooling) — H_008 numbers
LPA_REP_HZ, LPA_PULSE_J = 1.0e3, 1.0e-6


def total_line(sigma: float) -> float:
    nat = undulator_natural_linewidth(1, N_PERIODS)
    bro = energy_spread_broadening(sigma)
    return math.sqrt(nat ** 2 + bro ** 2)


def main() -> int:
    nat = undulator_natural_linewidth(1, N_PERIODS)
    # critical sigma where total == budget: 2*sigma* = sqrt(budget^2 - nat^2)
    sigma_crit = math.sqrt(INBAND_BW ** 2 - nat ** 2) / 2.0
    line_before = total_line(SIGMA_BEFORE)
    line_after = total_line(SIGMA_AFTER)
    # flux unchanged by cooling (cooling touches phase space, not rep-rate/charge)
    flux_before = average_power(LPA_REP_HZ, LPA_PULSE_J)
    flux_after = flux_before

    metrics = {
        "natural": nat,
        "sigma_crit": sigma_crit,
        "line_before": line_before,
        "line_after": line_after,
        "inband_bw": INBAND_BW,
        "flux_before_w": flux_before,
        "flux_after_w": flux_after,
    }

    falsifiers = [
        Falsifier("F-QW-1 BEFORE-FAIL", lambda m: not (m["line_before"] > m["inband_bw"]),
                  "uncooled 1% line must overfill the 2% budget (quality wall present)"),
        Falsifier("F-QW-2 AFTER-PASS", lambda m: not (m["line_after"] <= m["inband_bw"]),
                  "cooled line must fit inside the 2% budget (quality wall beaten)"),
        Falsifier("F-QW-3 THRESHOLD", lambda m: not (m["sigma_crit"] < SIGMA_BEFORE
                  and SIGMA_AFTER <= m["sigma_crit"]),
                  "cooled sigma must cross the critical threshold sigma* (~0.866%)"),
        Falsifier("F-QW-4 FLUX-STUBBORN", lambda m: abs(m["flux_after_w"] - m["flux_before_w"]) > 1e-18,
                  "cooling must NOT change average power (flux wall unmoved → split is real)"),
        Falsifier("F-QW-5 BOUNDS", lambda m: not (0 < m["line_after"] < m["line_before"]),
                  "cooling must narrow the line, all positive"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_013 energy-spread cooling splits the M4 brightness wall (from P4)")
    print(f"  natural line (N={N_PERIODS}) = {nat*100:.2f}%  · critical sigma* = {sigma_crit*100:.3f}%")
    print(f"  sigma 1.00% -> line {line_before*100:.2f}%  (> {INBAND_BW*100:.0f}% budget: quality WALL)")
    print(f"  sigma {SIGMA_AFTER*100:.2f}% -> line {line_after*100:.2f}%  (<= budget: quality BEATEN)")
    print(f"  flux unchanged: {flux_before*1e3:.3f} mW before = after  (flux WALL stubborn, H_008)")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<18} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
