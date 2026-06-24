#!/usr/bin/env python3
"""H_016 — ERL reopens the flux floor (first probe of the abstraction-lane verdict
'flux face is REOPENABLE'). Energy recovery lifts the thermal-limited rep-rate by
1/(1-eta_recover) with no thermodynamic cap; combined with FEL-class pulse energy
(N_ib gain) it reaches the ~167 W HVM floor in a compact footprint — but ERL alone
(spontaneous pulse) does NOT, confirming flux is a *product* engineering wall, not
a 2nd-law ceiling.

Deterministic, stdlib-only. $0 local.
    python3 state/h016_erl_flux_reopen_2026_06_25/run_h016.py
"""

from __future__ import annotations

import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "tool"))

from lumen_optics import Falsifier, average_power, erl_rep_rate_ceiling, evaluate

# --- pre-registered parameters (FROZEN 2026-06-25) ---------------------------
HEAT_BUDGET_W = 1.0e4       # removable beam-dump/cooling heat budget [W]
E_BUNCH_J = 0.10           # energy per bunch (1 GeV x 100 pC) [J]
HVM_FLOOR_W = 167.0        # in-band power for 100 WPH (H_005)
PULSE_SPONT_J = 1.0e-6     # spontaneous-undulator in-band EUV per bunch (~1 µJ)
PULSE_FEL_J = 1.0e-4       # FEL-class in-band per bunch (~100x, H_A2) [J]
ETA_LOW, ETA_HIGH = 0.90, 0.95


def main() -> int:
    # rep-rate ceilings: no ERL (eta=0) vs ERL
    f_noerl = erl_rep_rate_ceiling(HEAT_BUDGET_W, E_BUNCH_J, 0.0)
    f_erl90 = erl_rep_rate_ceiling(HEAT_BUDGET_W, E_BUNCH_J, ETA_LOW)
    f_erl95 = erl_rep_rate_ceiling(HEAT_BUDGET_W, E_BUNCH_J, ETA_HIGH)
    lift_90 = f_erl90 / f_noerl

    # in-band power: ERL f-ceiling x pulse energy
    p_erl_spont = average_power(f_erl95, PULSE_SPONT_J)   # ERL alone, spontaneous
    p_erl_fel = average_power(f_erl95, PULSE_FEL_J)        # ERL + FEL gain

    metrics = {
        "f_noerl_hz": f_noerl,
        "f_erl90_hz": f_erl90,
        "f_erl95_hz": f_erl95,
        "lift_at_0p90": lift_90,
        "p_erl_spontaneous_w": p_erl_spont,
        "p_erl_fel_w": p_erl_fel,
        "hvm_floor_w": HVM_FLOOR_W,
    }

    falsifiers = [
        Falsifier("F-ERL-1 LIFT", lambda m: not (m["lift_at_0p90"] >= 10.0),
                  "ERL recovery at eta=0.9 must lift the rep-rate ceiling >= 10x"),
        Falsifier("F-ERL-2 REACH", lambda m: not (m["p_erl_fel_w"] >= m["hvm_floor_w"]),
                  "ERL + FEL pulse must reach the ~167 W HVM floor (flux reopened)"),
        Falsifier("F-ERL-3 NECESSARY", lambda m: not (m["p_erl_spontaneous_w"] < m["hvm_floor_w"]),
                  "ERL alone (spontaneous) must fall short -> flux is a product wall, ERL necessary not sufficient"),
        Falsifier("F-ERL-4 MONOTONE", lambda m: not (m["f_erl95_hz"] > m["f_erl90_hz"] > m["f_noerl_hz"]),
                  "higher recovery -> higher rep-rate ceiling"),
        Falsifier("F-ERL-5 NO-CEILING", lambda m: not (
                  erl_rep_rate_ceiling(HEAT_BUDGET_W, E_BUNCH_J, 0.999) > m["f_erl95_hz"]),
                  "ceiling keeps rising as eta->1 (no thermodynamic floor: flux is REOPENABLE)"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_016 ERL reopens the flux floor (abstraction-lane first probe)")
    print(f"  rep-rate ceiling: no-ERL {f_noerl:.3g} Hz -> ERL0.90 {f_erl90:.3g} Hz ({lift_90:.0f}x) -> ERL0.95 {f_erl95:.3g} Hz")
    print(f"  in-band power @ERL0.95: spontaneous {p_erl_spont:.1f} W  vs  +FEL {p_erl_fel:.1f} W  (floor {HVM_FLOOR_W:.0f})")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<18} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
