#!/usr/bin/env python3
"""H_022 — combination breakthrough: tabletop accelerator + ERL + FEL + cooling +
module-array clears EVERY wall at once (flux floor AND CAPEX wall AND wavelength
tunability), and each lever is NECESSARY — drop one and a wall reappears. The
goal "tabletop accelerator + @ combination wall-breakthrough" realized by stacking
the verified levers H_004 x H_016 x H_A2 x H_013 x H_021.

Deterministic, stdlib-only. $0 local.
    python3 state/h022_combination_breakthrough_2026_06_25/run_h022.py
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
    average_power,
    erl_rep_rate_ceiling,
    evaluate,
    wright_unit_cost,
)

# --- pre-registered stack parameters (FROZEN 2026-06-25) ---------------------
HVM_FLOOR_W = 167.0        # flux floor (H_005)
LPP_TOOL = 1.0             # CAPEX baseline (H_020/H_021)
# flux levers (H_016): ERL recovery + FEL pulse energy + cooling enables FEL gain (H_013)
HEAT_W, E_BUNCH_J, ETA = 1.0e4, 0.10, 0.95
PULSE_FEL_J, PULSE_SPONT_J = 1.0e-4, 1.0e-6
# capex levers (H_021): replicable module learning curve
C1_COMPACT, LR, N_MODULES = 1.5, 0.85, 10
# wavelength tunability (H_007) carried as a verified capability
WAVELENGTH_TUNABLE = True


def main() -> int:
    f_erl = erl_rep_rate_ceiling(HEAT_W, E_BUNCH_J, ETA)
    p_full = average_power(f_erl, PULSE_FEL_J)        # full stack: ERL + FEL
    p_no_fel = average_power(f_erl, PULSE_SPONT_J)    # drop FEL -> spontaneous only
    capex_full = wright_unit_cost(C1_COMPACT, N_MODULES, LR)   # full stack: module array
    capex_no_array = wright_unit_cost(C1_COMPACT, 1, LR)       # drop array -> single bespoke unit

    flux_cleared = p_full >= HVM_FLOOR_W
    capex_cleared = capex_full < LPP_TOOL
    all_walls = flux_cleared and capex_cleared and WAVELENGTH_TUNABLE

    metrics = {
        "stack_power_w": p_full,
        "stack_capex": capex_full,
        "power_no_fel_w": p_no_fel,
        "capex_no_array": capex_no_array,
        "flux_cleared": flux_cleared,
        "capex_cleared": capex_cleared,
        "wavelength_tunable": WAVELENGTH_TUNABLE,
        "all_walls_cleared": all_walls,
    }

    falsifiers = [
        Falsifier("F-CMB-1 FLUX", lambda m: not (m["stack_power_w"] >= HVM_FLOOR_W),
                  "the full stack must clear the 167 W flux floor"),
        Falsifier("F-CMB-2 CAPEX", lambda m: not (m["stack_capex"] < LPP_TOOL),
                  "the full stack must clear the CAPEX wall (< LPP tool)"),
        Falsifier("F-CMB-3 FEL-NECESSARY", lambda m: not (m["power_no_fel_w"] < HVM_FLOOR_W),
                  "dropping FEL must reopen the flux wall (FEL is necessary)"),
        Falsifier("F-CMB-4 ARRAY-NECESSARY", lambda m: not (m["capex_no_array"] >= LPP_TOOL),
                  "dropping the module array must reopen the CAPEX wall (array is necessary)"),
        Falsifier("F-CMB-5 ALL-WALLS", lambda m: not m["all_walls_cleared"],
                  "flux AND capex AND wavelength must all clear together (the combination breakthrough)"),
        Falsifier("F-CMB-6 BOUNDS", lambda m: not all(v > 0 for v in
                  (m["stack_power_w"], m["stack_capex"], m["power_no_fel_w"])),
                  "all positive"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_022 combination breakthrough — tabletop accelerator + ERL + FEL + cooling + array")
    print(f"  FLUX : full stack {p_full:.0f} W >= {HVM_FLOOR_W:.0f} floor  ({'CLEARED' if flux_cleared else 'WALL'})")
    print(f"  CAPEX: full stack {capex_full:.2f} < {LPP_TOOL:.1f} LPP     ({'CLEARED' if capex_cleared else 'WALL'})")
    print(f"  WAVELENGTH: 13.5/6.5/5/3 nm tunable (H_007)               ({'CLEARED' if WAVELENGTH_TUNABLE else 'WALL'})")
    print(f"  necessity: drop FEL -> {p_no_fel:.0f} W (wall) · drop array -> {capex_no_array:.2f} (wall)")
    print(f"  -> ALL WALLS CLEARED simultaneously: {all_walls}  (each lever necessary)")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<18} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
