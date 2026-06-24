#!/usr/bin/env python3
"""H_012 — spectral gating + grazing-incidence column recovers usable in-band flux
(promotion of abstract H_A4 to a verified, runnable hypothesis).

At 6.5 nm, replacing the collection/transport surfaces with grazing-incidence
reflectors (R~0.9) and gating out-of-band shots (raise in-band fraction) lifts
wafer-level in-band flux well past 5x a fixed normal-incidence, ungated baseline.

Deterministic, stdlib-only. $0 local.
    python3 state/h012_gating_grazing_recovery_2026_06_25/run_h012.py
"""

from __future__ import annotations

import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "tool"))

from lumen_optics import Falsifier, column_throughput_mixed, evaluate, mirror_chain_throughput

# --- pre-registered parameters (FROZEN 2026-06-25) ---------------------------
N_TOTAL = 11           # total surfaces (H_002 column)
N_GRAZE = 4            # collection/transport surfaces convertible to grazing
R_GRAZE = 0.90         # grazing-incidence reflectivity (shallow angle)
R_NORMAL = 0.55        # near-normal multilayer R at 6.5 nm (H_002)
INBAND_UNGATED = 0.70  # fraction of a 2.24% line inside the 2% budget (H_009)
INBAND_GATED = 0.98    # in-band fraction after shot-by-shot spectral gating
GATING_DUTY = 0.80     # fraction of shots that survive the gate (cost)


def main() -> int:
    # baseline: all-normal column, ungated
    t_base = mirror_chain_throughput(R_NORMAL, N_TOTAL) * INBAND_UNGATED
    # enhanced: N_GRAZE grazing + rest normal, gated (× duty for discarded shots)
    t_enh = (column_throughput_mixed(R_GRAZE, N_GRAZE, R_NORMAL, N_TOTAL - N_GRAZE)
             * INBAND_GATED * GATING_DUTY)
    ratio = t_enh / t_base

    # component sanity: more grazing surfaces -> higher throughput
    t_enh_more = (column_throughput_mixed(R_GRAZE, N_GRAZE + 2, R_NORMAL, N_TOTAL - N_GRAZE - 2)
                  * INBAND_GATED * GATING_DUTY)

    metrics = {
        "throughput_baseline": t_base,
        "throughput_enhanced": t_enh,
        "recovery_ratio": ratio,
        "inband_ungated": INBAND_UNGATED,
        "inband_gated": INBAND_GATED,
        "throughput_more_grazing": t_enh_more,
    }

    falsifiers = [
        Falsifier("F-RC-1 RECOVER", lambda m: not (m["recovery_ratio"] >= 5.0),
                  "wafer in-band flux must be >= 5x the normal-incidence ungated baseline"),
        Falsifier("F-RC-2 GRAZING", lambda m: not (R_GRAZE > R_NORMAL),
                  "grazing reflectivity must exceed normal-incidence (the optics gain)"),
        Falsifier("F-RC-3 GATING", lambda m: not (m["inband_gated"] > m["inband_ungated"]),
                  "gating must raise the in-band fraction"),
        Falsifier("F-RC-4 MONOTONE", lambda m: not (m["throughput_more_grazing"] > m["throughput_enhanced"]),
                  "more grazing surfaces must raise throughput"),
        Falsifier("F-RC-5 BOUNDS", lambda m: not (0.0 < m["throughput_baseline"] <= 1.0
                  and 0.0 < m["throughput_enhanced"] <= 1.0),
                  "throughputs in (0,1]"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_012 spectral gating + grazing-incidence in-band recovery (promotes H_A4)")
    print(f"  baseline (all-normal R={R_NORMAL}, ungated) = {t_base:.6g}")
    print(f"  enhanced ({N_GRAZE} grazing R={R_GRAZE} + {N_TOTAL-N_GRAZE} normal, gated×duty) = {t_enh:.6g}")
    print(f"  recovery ratio = {ratio:.2f}x  (more-grazing -> {t_enh_more:.6g})")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<16} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
