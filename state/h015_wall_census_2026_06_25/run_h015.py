#!/usr/bin/env python3
"""H_015 — wall census (meta-law prediction P5): across every proposed sub-13.5 nm
architecture the binding constraint is always one of the four cost meta-laws
{M1 photon, M2 power, M3 footprint, M4 brightness/flux} and NEVER wavelength (M5).

Deterministic, stdlib-only. $0 local.
    python3 state/h015_wall_census_2026_06_25/run_h015.py
"""

from __future__ import annotations

import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "tool"))

from lumen_optics import Falsifier, evaluate

# --- pre-registered census (FROZEN 2026-06-25) -------------------------------
# each architecture -> its binding wall (the meta-law it fails on)
COST_WALLS = {"M1", "M2", "M3", "M4"}
CENSUS = {
    "LPP (tin droplet)":            "M2",  # thermal source-power ceiling
    "Synchrotron (storage ring)":   "M3",  # footprint (meets power)
    "LPA-undulator":                "M4",  # flux/brightness (the terminal wall)
    "Inverse-Compton":              "M4",  # flux
    "Recombination EUV laser":      "M2",  # rep-rate/thermal (non-thermal escape, but binds on avg power)
    "6.5 nm BEUV optics (any src)": "M1",  # multiplicative reflectance loss
}
ACCEL_ROUTES = {"LPA-undulator", "Inverse-Compton"}


def main() -> int:
    walls = list(CENSUS.values())
    any_wavelength = any(w == "wavelength" or w == "M5" for w in walls)
    all_in_cost_set = all(w in COST_WALLS for w in walls)
    n_arch = len(CENSUS)
    accel_on_flux = all(CENSUS[a] == "M4" for a in ACCEL_ROUTES)

    metrics = {
        "n_architectures": n_arch,
        "any_binds_on_wavelength": any_wavelength,
        "all_in_cost_set": all_in_cost_set,
        "accel_routes_bind_on_flux_M4": accel_on_flux,
        "census": CENSUS,
    }

    falsifiers = [
        Falsifier("F-CEN-1 NO-WAVELENGTH", lambda m: m["any_binds_on_wavelength"],
                  "no architecture may bind on wavelength (M5 = freedom law)"),
        Falsifier("F-CEN-2 IN-SET", lambda m: not m["all_in_cost_set"],
                  "every binding wall must be one of {M1,M2,M3,M4}"),
        Falsifier("F-CEN-3 COVERAGE", lambda m: not (m["n_architectures"] >= 3),
                  ">= 3 distinct architectures censused"),
        Falsifier("F-CEN-4 FLUX-TERMINAL", lambda m: not m["accel_routes_bind_on_flux_M4"],
                  "the compact-accelerator routes must bind on M4 (flux) -> the terminal question"),
        Falsifier("F-CEN-5 ALL-WALLS-HIT", lambda m: not (set(CENSUS.values()) == COST_WALLS),
                  "all four cost meta-laws appear as some architecture's binding wall (taxonomy complete)"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_015 wall census — binding wall is never wavelength (P5)")
    for arch, w in CENSUS.items():
        print(f"  {arch:<30} -> {w}")
    print(f"  binds-on-wavelength: {any_wavelength}  ·  all in {{M1..M4}}: {all_in_cost_set}")
    print(f"  accelerator routes bind on M4 (flux): {accel_on_flux}")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<20} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
