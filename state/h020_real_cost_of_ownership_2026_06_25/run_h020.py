#!/usr/bin/env python3
"""H_020 — real-units cost-of-ownership settles the M8-vs-LPP question (H_019 left
it open in normalized units). With public-order figures, the energy + waste-heat
(M8) term is ~0.5% of LPP cost-of-ownership — the binding economic wall is
CAPEX + maintenance (M7/M9), NOT the M8 thermodynamic floor.

Public-order figures (representative, see card limits):
- 2nd-gen EUV tool CAPEX ~$350M; annual maintenance ~1/4 tool/yr (transcript
  state/euv-yt-2KDLZMG8FAs-transcript.md); wall-plug ~1 MW class; $0.10/kWh;
  utilization ~0.7; capital amortized over 5 yr.

Deterministic, stdlib-only. $0 local.
    python3 state/h020_real_cost_of_ownership_2026_06_25/run_h020.py
"""

from __future__ import annotations

import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "tool"))

from lumen_optics import Falsifier, evaluate

# --- pre-registered parameters (FROZEN 2026-06-25, public-order representative) ---
CAPEX_USD = 350.0e6        # 2nd-gen EUV tool (transcript)
AMORT_YEARS = 5.0          # straight-line capital amortization
MAINT_FRACTION = 0.25      # ~1/4 tool price / yr maintenance (transcript, conservative)
WALLPLUG_W = 1.0e6         # ~1 MW class scanner+source wall-plug
UTILIZATION = 0.70         # fraction of the year producing
USD_PER_KWH = 0.10         # industrial electricity
COOLING_COP = 4.0          # heat removed per electrical W of cooling


def main() -> int:
    hours_yr = 8760.0 * UTILIZATION
    capex_annual = CAPEX_USD / AMORT_YEARS
    maint_annual = MAINT_FRACTION * CAPEX_USD
    # energy bill: generation wall-plug + cooling of (nearly all) waste heat
    energy_gen = WALLPLUG_W / 1e3 * hours_yr * USD_PER_KWH
    energy_cool = (WALLPLUG_W / COOLING_COP) / 1e3 * hours_yr * USD_PER_KWH  # M8 waste-heat removal
    energy_total = energy_gen + energy_cool

    coo_annual = capex_annual + maint_annual + energy_total
    m8_fraction = energy_total / coo_annual
    capex_maint_fraction = (capex_annual + maint_annual) / coo_annual

    metrics = {
        "capex_annual_musd": capex_annual / 1e6,
        "maint_annual_musd": maint_annual / 1e6,
        "energy_total_musd": energy_total / 1e6,
        "coo_annual_musd": coo_annual / 1e6,
        "m8_energy_fraction": m8_fraction,
        "capex_maint_fraction": capex_maint_fraction,
    }

    falsifiers = [
        Falsifier("F-M8-1 NEGLIGIBLE", lambda m: not (m["m8_energy_fraction"] < 0.05),
                  "energy+waste-heat (M8) must be < 5% of cost-of-ownership"),
        Falsifier("F-M8-2 CAPEX-DOMINANT", lambda m: not (m["capex_maint_fraction"] > 0.80),
                  "CAPEX + maintenance must dominate (> 80% of CoO) — the binding economic wall"),
        Falsifier("F-M8-3 ORDERING", lambda m: not (m["energy_total_musd"] < m["maint_annual_musd"]
                  and m["energy_total_musd"] < m["capex_annual_musd"]),
                  "energy term must be far below both maintenance and CAPEX"),
        Falsifier("F-M8-4 BOUNDS", lambda m: not (0.0 < m["m8_energy_fraction"] < 1.0
                  and m["coo_annual_musd"] > 0),
                  "fractions in (0,1), CoO positive"),
        Falsifier("F-M8-5 M8-REAL", lambda m: not (m["energy_total_musd"] > 0),
                  "the M8 waste-heat floor is real and non-zero (just small)"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_020 real-units cost-of-ownership — M8 vs LPP (settles H_019 open question)")
    print(f"  CAPEX/yr   = ${capex_annual/1e6:6.1f}M   maintenance/yr = ${maint_annual/1e6:6.1f}M")
    print(f"  energy/yr  = ${energy_total/1e6:6.2f}M   (gen ${energy_gen/1e6:.2f}M + cooling/M8 ${energy_cool/1e6:.2f}M)")
    print(f"  CoO/yr     = ${coo_annual/1e6:6.1f}M")
    print(f"  M8 (energy+heat) = {m8_fraction*100:.2f}% of CoO  ·  CAPEX+maint = {capex_maint_fraction*100:.1f}%")
    print(f"  -> M8 thermodynamic floor is REAL but economically negligible; CAPEX/maint (M7/M9) is the wall")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<18} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
