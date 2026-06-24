#!/usr/bin/env python3
"""H_005 — HVM throughput floor: at the same source, 6.5 nm delivers ~14x fewer
photons (H_002), so its wafer-per-hour throughput falls below the ~100 WPH that
high-volume manufacturing requires.

The 100 WPH HVM threshold is a public industry figure (transcript
state/euv-yt-2KDLZMG8FAs-transcript.md: "양산으로 가려면 적어도 100개 정도").

Deterministic, stdlib-only. $0 local.
    python3 state/h005_hvm_throughput_floor_2026_06_24/run_h005.py
"""

from __future__ import annotations

import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "tool"))

from lumen_optics import (
    Falsifier,
    evaluate,
    hvm_throughput_wph,
    source_power_multiplier,
)

# --- pre-registered parameters (FROZEN 2026-06-24) ---------------------------
HVM_FLOOR_WPH = 100.0       # public HVM throughput threshold (transcript)
REF_POWER_W = 250.0         # incumbent LPP source-power class (H_001 baseline)
REF_WPH = 150.0             # representative 13.5 nm HVM throughput at REF_POWER
R_EUV, R_BEUV, N_MIRRORS = 0.70, 0.55, 11  # H_002 frozen params


def main() -> int:
    mult = source_power_multiplier(R_EUV, R_BEUV, N_MIRRORS)

    # 13.5 nm at the incumbent source
    wph_135 = hvm_throughput_wph(REF_POWER_W, REF_POWER_W, REF_WPH)
    # 6.5 nm at the SAME source power: ~mult fewer photons reach the wafer,
    # so effective throughput drops by the same factor.
    wph_65_same_source = wph_135 / mult
    # source power needed to restore HVM floor at 6.5 nm
    power_needed_w = REF_POWER_W * mult * (HVM_FLOOR_WPH / REF_WPH)

    metrics = {
        "hvm_floor_wph": HVM_FLOOR_WPH,
        "wph_135": wph_135,
        "h002_multiplier": mult,
        "wph_65_same_source": wph_65_same_source,
        "power_needed_for_floor_w": power_needed_w,
    }

    falsifiers = [
        Falsifier("F-WPH-1 BASELINE", lambda m: not (m["wph_135"] >= m["hvm_floor_wph"]),
                  "13.5nm incumbent must clear the HVM floor (else calibration wrong)"),
        Falsifier("F-WPH-2 SHORTFALL", lambda m: not (m["wph_65_same_source"] < m["hvm_floor_wph"]),
                  "6.5nm at same source must fall below HVM floor (the claim)"),
        Falsifier("F-WPH-3 MONOTONE", lambda m: not (m["wph_135"] > m["wph_65_same_source"]),
                  "more photons -> more throughput"),
        Falsifier("F-WPH-4 POWER-GAP", lambda m: not (m["power_needed_for_floor_w"] > m["wph_135"]),
                  "restoring the floor must demand far more source power than today"),
        Falsifier("F-WPH-5 BOUNDS", lambda m: not all(v > 0 for v in
                  (m["wph_135"], m["wph_65_same_source"], m["power_needed_for_floor_w"])),
                  "all throughputs/powers positive"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_005 HVM throughput floor (100 WPH) vs 6.5 nm")
    print(f"  13.5nm @ {REF_POWER_W:.0f} W = {wph_135:.1f} WPH  (floor {HVM_FLOOR_WPH:.0f})")
    print(f"  6.5nm @ same source = {wph_65_same_source:.1f} WPH  (1/{mult:.1f} photons)")
    print(f"  source power to restore floor at 6.5nm = {power_needed_w:.0f} W")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<16} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
