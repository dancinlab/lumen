#!/usr/bin/env python3
"""H_001 — LPP source-power ceiling vs the 6.5 nm demand (chains to H_002).

Computes a representative LPP in-band power budget (baseline ~250 W class), a
plausible near-term scaling ceiling, and the 6.5 nm power demand = baseline x
H_002 mirror-throughput multiplier. Tests whether the ceiling can meet the demand.

Deterministic, stdlib-only. $0 local.
    python3 state/h001_lpp_power_ceiling_2026_06_24/run_h001.py
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
    lpp_source_power,
    source_power_multiplier,
)

# --- pre-registered parameters (FROZEN 2026-06-24) ---------------------------
# representative public-order values (see card Honest Limits L1)
BASE_FREP = 50.0e3     # Sn droplet / laser rep rate [Hz]
BASE_EPULSE = 0.5      # drive-laser energy per pulse [J]
BASE_CE = 0.05         # drive -> in-band (2% BW @13.5nm) conversion efficiency
BASE_COLL = 0.20       # collected/usable fraction at intermediate focus

# plausible near-term scaling ceiling (each lever pushed, not a physical limit)
CEIL_FREP = 100.0e3
CEIL_EPULSE = 1.0
CEIL_CE = 0.06
CEIL_COLL = 0.25

# 6.5 nm optics-side demand multiplier — from H_002 frozen params
R_EUV, R_BEUV, N_MIRRORS = 0.70, 0.55, 11


def main() -> int:
    baseline = lpp_source_power(BASE_FREP, BASE_EPULSE, BASE_CE, BASE_COLL)
    ceiling = lpp_source_power(CEIL_FREP, CEIL_EPULSE, CEIL_CE, CEIL_COLL)
    mult = source_power_multiplier(R_EUV, R_BEUV, N_MIRRORS)
    demand = baseline * mult

    metrics = {
        "baseline_w": baseline,
        "ceiling_w": ceiling,
        "h002_multiplier": mult,
        "demand_6p5nm_w": demand,
        "supply_gap_w": demand - ceiling,
        "ce_in_bounds": 0.0 <= BASE_CE <= 1.0 and 0.0 <= CEIL_CE <= 1.0,
        "coll_in_bounds": 0.0 <= BASE_COLL <= 1.0 and 0.0 <= CEIL_COLL <= 1.0,
    }

    falsifiers = [
        Falsifier("F-PC-1 SUPPLY", lambda m: m["ceiling_w"] >= m["demand_6p5nm_w"],
                  "ceiling >= demand -> LPP scaling NOT the wall (hypothesis refuted)"),
        Falsifier("F-PC-2 BASELINE", lambda m: not (150.0 <= m["baseline_w"] <= 400.0),
                  "baseline must reproduce ~250 W class else numbers wrong"),
        Falsifier("F-PC-3 MONOTONE", lambda m: not (m["ceiling_w"] > m["baseline_w"]),
                  "scaling each lever must raise power"),
        Falsifier("F-PC-4 BOUNDS", lambda m: not (m["ce_in_bounds"] and m["coll_in_bounds"]
                  and m["baseline_w"] >= 0 and m["ceiling_w"] >= 0),
                  "CE/collection in [0,1], powers >= 0"),
        Falsifier("F-PC-5 GAP-SIGN", lambda m: not (m["demand_6p5nm_w"] > m["baseline_w"]),
                  "6.5nm demand must exceed today (multiplier > 1)"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_001 LPP source-power ceiling vs 6.5 nm demand")
    print(f"  baseline = {baseline:.1f} W   ceiling = {ceiling:.1f} W")
    print(f"  H_002 multiplier = {mult:.2f}x -> demand = {demand:.1f} W")
    print(f"  supply gap (demand - ceiling) = {demand - ceiling:.1f} W")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<16} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
