#!/usr/bin/env python3
"""H_010 — synchrotron vs compact LPA trade: a storage-ring (Pohang-class)
source meets HVM throughput (high average power) but costs a stadium-scale
footprint (~1.5 B$, ~100x area); the compact LPA inverts it (tiny footprint,
flux wall H_008). Neither path is free — the trade is footprint↔throughput.

Deterministic, stdlib-only. $0 local.
    python3 state/h010_synchrotron_vs_lpa_2026_06_24/run_h010.py
"""

from __future__ import annotations

import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "tool"))

from lumen_optics import Falsifier, evaluate

# --- pre-registered parameters (FROZEN 2026-06-24) ---------------------------
# representative public-order figures (transcript + light-source-paths.md)
SYNC_FOOTPRINT_M2 = 1.0e4    # storage ring ~ gymnasium-scale (~100x100 m)
LPA_FOOTPRINT_M2 = 50.0      # laser + cm accel + few-m undulator beamline
SYNC_COST_USD = 1.5e9        # ~1.5 B$ (transcript 1.5-2 jo KRW)
EUV_TOOL_USD = 3.5e8         # one High-NA EUV tool (~350 M$)
HVM_REQUIRED_W = 167.0       # in-band power for 100 WPH (H_008)
SYNC_AVG_POWER_W = 500.0     # storage-ring in-band avg power (quasi-CW, ample)
LPA_AVG_POWER_W = 1.0        # compact LPA pushed (H_008) — flux-limited


def main() -> int:
    footprint_ratio = SYNC_FOOTPRINT_M2 / LPA_FOOTPRINT_M2
    cost_in_tools = SYNC_COST_USD / EUV_TOOL_USD

    metrics = {
        "footprint_ratio": footprint_ratio,
        "sync_cost_in_euv_tools": cost_in_tools,
        "sync_meets_hvm": SYNC_AVG_POWER_W >= HVM_REQUIRED_W,
        "lpa_meets_hvm": LPA_AVG_POWER_W >= HVM_REQUIRED_W,
    }

    falsifiers = [
        Falsifier("F-SYN-1 FOOTPRINT", lambda m: not (m["footprint_ratio"] >= 100.0),
                  "synchrotron must be >= 100x the LPA footprint (the size penalty)"),
        Falsifier("F-SYN-2 COST", lambda m: not (1.0 <= m["sync_cost_in_euv_tools"] <= 10.0),
                  "synchrotron cost ~ a few EUV tools (transcript 'a generation or two')"),
        Falsifier("F-SYN-3 TRADE", lambda m: not (m["sync_meets_hvm"] and not m["lpa_meets_hvm"]),
                  "synchrotron meets HVM power, LPA does not — the footprint<->throughput trade"),
        Falsifier("F-SYN-4 BOUNDS", lambda m: not all(v > 0 for v in
                  (m["footprint_ratio"], m["sync_cost_in_euv_tools"])),
                  "ratios positive"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_010 synchrotron vs compact LPA — footprint <-> throughput trade")
    print(f"  footprint: synchrotron {SYNC_FOOTPRINT_M2:.0f} m^2 vs LPA {LPA_FOOTPRINT_M2:.0f} m^2 = {footprint_ratio:.0f}x")
    print(f"  cost: synchrotron {SYNC_COST_USD/1e9:.1f} B$ = {cost_in_tools:.1f} High-NA EUV tools")
    print(f"  HVM power ({HVM_REQUIRED_W:.0f} W): synchrotron meets={metrics['sync_meets_hvm']}  LPA meets={metrics['lpa_meets_hvm']}")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<16} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
