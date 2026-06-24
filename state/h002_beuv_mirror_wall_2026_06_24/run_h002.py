#!/usr/bin/env python3
"""H_002 — BEUV (6.5 nm) multilayer-mirror throughput wall.

Pre-registered run. Computes the source-power multiplier that a 6.5 nm column
demands relative to a 13.5 nm column with the SAME mirror count, from public
per-mirror reflectivities, then evaluates the pre-registered falsifiers.

Deterministic, stdlib-only. $0 local.
    python3 state/h002_beuv_mirror_wall_2026_06_24/run_h002.py
"""

from __future__ import annotations

import json
import os
import sys

# import the shared harness from repo-root tool/
_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "tool"))

from lumen_optics import (
    Falsifier,
    evaluate,
    mirror_chain_throughput,
    source_power_multiplier,
)

# --- pre-registered parameters (FROZEN 2026-06-24) ---------------------------
R_EUV = 0.70   # Mo/Si per-mirror reflectivity @ 13.5 nm (representative)
R_BEUV = 0.55  # La/B-based per-mirror reflectivity @ 6.5 nm (representative)
N_MIRRORS = 11  # representative all-reflective column (collector+illum+POB)


def main() -> int:
    t_euv = mirror_chain_throughput(R_EUV, N_MIRRORS)
    t_beuv = mirror_chain_throughput(R_BEUV, N_MIRRORS)
    mult = source_power_multiplier(R_EUV, R_BEUV, N_MIRRORS)

    # negative control: identical reflectivity must give multiplier == 1
    mult_ctrl = source_power_multiplier(R_EUV, R_EUV, N_MIRRORS)

    # mirror-count sensitivity: multiplier must grow with N
    mult_n7 = source_power_multiplier(R_EUV, R_BEUV, 7)

    metrics = {
        "R_euv": R_EUV,
        "R_beuv": R_BEUV,
        "n_mirrors": N_MIRRORS,
        "throughput_euv": t_euv,
        "throughput_beuv": t_beuv,
        "power_multiplier": mult,
        "power_multiplier_control": mult_ctrl,
        "power_multiplier_n7": mult_n7,
    }

    falsifiers = [
        Falsifier(
            "F-MW-1 WALL",
            lambda m: m["power_multiplier"] < 2.0,
            "multiplier < 2x -> not a meaningful source wall",
        ),
        Falsifier(
            "F-MW-2 MONOTONE",
            lambda m: not (m["throughput_beuv"] < m["throughput_euv"]),
            "lower reflectivity must give lower throughput",
        ),
        Falsifier(
            "F-MW-3 NEG-CONTROL",
            lambda m: abs(m["power_multiplier_control"] - 1.0) > 1e-9,
            "identical R must give multiplier == 1",
        ),
        Falsifier(
            "F-MW-4 N-SENSITIVITY",
            lambda m: not (m["power_multiplier_n7"] < m["power_multiplier"]),
            "multiplier must grow with mirror count N",
        ),
        Falsifier(
            "F-MW-5 BOUNDS",
            lambda m: not (0.0 < m["throughput_beuv"] <= 1.0 and 0.0 < m["throughput_euv"] <= 1.0),
            "all throughputs in (0,1]",
        ),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_002 BEUV mirror-throughput wall — source-power multiplier")
    print(f"  R_euv={R_EUV} R_beuv={R_BEUV} N={N_MIRRORS}")
    print(f"  throughput_euv  = {t_euv:.6g}")
    print(f"  throughput_beuv = {t_beuv:.6g}")
    print(f"  power_multiplier = {mult:.4f}x  (N=7 -> {mult_n7:.4f}x)")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<18} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    out = os.path.join(_HERE, "result.json")
    with open(out, "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
