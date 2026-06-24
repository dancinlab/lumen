#!/usr/bin/env python3
"""H_006 — undulator / inverse-Compton turns an LPA electron beam into EUV
photons at LPA-reachable energies, closing the accelerator->light chain (H_004).

Deterministic, stdlib-only. $0 local.
    python3 state/h006_undulator_photon_2026_06_24/run_h006.py
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
    energy_for_undulator_wavelength,
    evaluate,
    inverse_compton_wavelength,
    lorentz_gamma,
    undulator_wavelength,
)

# --- pre-registered parameters (FROZEN 2026-06-24) ---------------------------
TARGET_NM = 13.5            # EUV fundamental to produce
PERIOD_NM = 15.0e6          # undulator period 15 mm (representative)
K = 1.0                     # undulator deflection parameter
LPA_REACH_EV = 1.0e9        # single-stage LPA reach (H_004) [eV]
IC_LASER_NM = 1000.0        # 1 µm drive laser for inverse-Compton route


def main() -> int:
    e_und = energy_for_undulator_wavelength(TARGET_NM, PERIOD_NM, K)
    g_und = lorentz_gamma(e_und)
    lam_roundtrip = undulator_wavelength(PERIOD_NM, g_und, K)

    # inverse-Compton route: which energy gives 13.5 nm from a 1 µm laser?
    # lambda_x = laser/(4 gamma^2) -> gamma = sqrt(laser/(4*target))
    g_ic = (IC_LASER_NM / (4.0 * TARGET_NM)) ** 0.5
    e_ic = g_ic * 510998.95
    lam_ic = inverse_compton_wavelength(IC_LASER_NM, g_ic)

    metrics = {
        "target_nm": TARGET_NM,
        "undulator_energy_mev": e_und / 1e6,
        "undulator_roundtrip_nm": lam_roundtrip,
        "ic_energy_mev": e_ic / 1e6,
        "ic_roundtrip_nm": lam_ic,
        "lpa_reach_mev": LPA_REACH_EV / 1e6,
    }

    falsifiers = [
        Falsifier("F-UND-1 REACH", lambda m: not (m["undulator_energy_mev"] <= m["lpa_reach_mev"]),
                  "undulator energy for 13.5nm must be within single-stage LPA reach"),
        Falsifier("F-UND-2 ROUNDTRIP", lambda m: abs(m["undulator_roundtrip_nm"] - TARGET_NM) > 1e-6,
                  "undulator wavelength at derived gamma must equal target (consistency)"),
        Falsifier("F-IC-3 LOW-E", lambda m: not (m["ic_energy_mev"] < 100.0),
                  "inverse-Compton must reach EUV at far lower energy (alt route)"),
        Falsifier("F-IC-4 ROUNDTRIP", lambda m: abs(m["ic_roundtrip_nm"] - TARGET_NM) > 1e-6,
                  "IC wavelength at derived gamma must equal target"),
        Falsifier("F-5 BOUNDS", lambda m: not all(v > 0 for v in
                  (m["undulator_energy_mev"], m["ic_energy_mev"], m["undulator_roundtrip_nm"])),
                  "all energies/wavelengths positive"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_006 undulator / inverse-Compton -> EUV photons from an LPA beam")
    print(f"  target {TARGET_NM} nm")
    print(f"  undulator (period {PERIOD_NM/1e6:.0f} mm, K={K}): E = {e_und/1e6:.1f} MeV  (LPA reach {LPA_REACH_EV/1e6:.0f} MeV)")
    print(f"    roundtrip lambda = {lam_roundtrip:.4f} nm")
    print(f"  inverse-Compton (1 µm laser): E = {e_ic/1e6:.2f} MeV  (roundtrip {lam_ic:.4f} nm)")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<16} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
