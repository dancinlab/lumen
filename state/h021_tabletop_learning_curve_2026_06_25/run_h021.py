#!/usr/bin/env python3
"""H_021 — the tabletop (compact laser-plasma) accelerator wins the CAPEX terminal
wall via the M7 learning curve. Because it is small and REPLICABLE, mass-produced
modules ride a Wright's-law curve and cross below LPP tool CAPEX at a modest unit
count (~6); a synchrotron (monolithic civil works, not replicable) stays stuck
above. This is the affirmative case that the campaign's CAPEX/M7 conclusion picks
the tabletop accelerator as the front-runner.

Normalized CAPEX units (LPP tool = 1.0). Deterministic, stdlib-only. $0 local.
    python3 state/h021_tabletop_learning_curve_2026_06_25/run_h021.py
"""

from __future__ import annotations

import json
import math
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "tool"))

from lumen_optics import Falsifier, evaluate, wright_unit_cost

# --- pre-registered parameters (FROZEN 2026-06-25, normalized) ---------------
LPP_TOOL = 1.0             # LPP EUV tool CAPEX baseline
C1_COMPACT = 1.5          # first-unit bespoke CAPEX of a compact-accelerator module
LEARNING_RATE = 0.85      # 15% cost cut per cumulative-output doubling (Wright)
SYNCHROTRON_CAPEX = 4.0   # ~4x EUV tool, monolithic (no module replication)


def crossover_n(c1: float, lr: float, target: float) -> float:
    # solve c1 * N**log2(lr) = target  ->  N = (target/c1)**(1/log2(lr))
    return (target / c1) ** (1.0 / math.log2(lr))


def main() -> int:
    c_n1 = wright_unit_cost(C1_COMPACT, 1, LEARNING_RATE)
    c_n10 = wright_unit_cost(C1_COMPACT, 10, LEARNING_RATE)
    c_n100 = wright_unit_cost(C1_COMPACT, 100, LEARNING_RATE)
    n_cross = crossover_n(C1_COMPACT, LEARNING_RATE, LPP_TOOL)
    # synchrotron rides no curve: one-off monolith stays at its bespoke cost
    sync_at_volume = SYNCHROTRON_CAPEX  # replication factor = 1

    metrics = {
        "compact_n1": c_n1,
        "compact_n10": c_n10,
        "compact_n100": c_n100,
        "crossover_units": n_cross,
        "lpp_tool": LPP_TOOL,
        "synchrotron_capex": sync_at_volume,
    }

    falsifiers = [
        Falsifier("F-LC-1 CROSSOVER", lambda m: not (1.0 < m["crossover_units"] < 100.0),
                  "compact CAPEX must cross below LPP at a modest, finite unit count"),
        Falsifier("F-LC-2 DESCENT", lambda m: not (m["compact_n100"] < m["compact_n10"] < m["compact_n1"]),
                  "the learning curve must strictly lower unit cost with volume"),
        Falsifier("F-LC-3 BEATS-LPP", lambda m: not (m["compact_n10"] < m["lpp_tool"]),
                  "at ~10 modules compact CAPEX must beat the LPP tool"),
        Falsifier("F-LC-4 SYNCH-STUCK", lambda m: not (m["synchrotron_capex"] > m["lpp_tool"]
                  and m["synchrotron_capex"] > m["compact_n10"]),
                  "the monolithic synchrotron (no replication) must stay above both LPP and the compact route"),
        Falsifier("F-LC-5 BOUNDS", lambda m: not all(v > 0 for v in
                  (m["compact_n1"], m["compact_n100"], m["crossover_units"])),
                  "all positive"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_021 tabletop accelerator wins the CAPEX wall via the M7 learning curve")
    print(f"  compact module CAPEX (LPP tool = 1.0): N=1 {c_n1:.2f} · N=10 {c_n10:.2f} · N=100 {c_n100:.2f}")
    print(f"  crosses below LPP at ~{n_cross:.1f} modules  (learning rate {LEARNING_RATE})")
    print(f"  synchrotron (monolithic, no replication) = {SYNCHROTRON_CAPEX:.1f} — stuck above, never rides the curve")
    print(f"  -> the small, REPLICABLE tabletop accelerator is the route that wins the CAPEX terminal wall")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<16} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
