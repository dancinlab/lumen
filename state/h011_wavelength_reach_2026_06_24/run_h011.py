#!/usr/bin/env python3
"""H_011 — accelerator wavelength reach: there is no theoretical short-wavelength
floor. Undulator wavelength scales as lambda ~ 1/gamma^2 ~ 1/E^2, so raising the
electron energy walks continuously EUV -> water-window -> X-ray. Single-stage LPA
(<=1 GeV) reaches ~3 nm; a few stages (<=2 GeV) reach ~1 nm. The binding wall is
flux/beam-quality (H_008/H_009), NOT wavelength.

Deterministic, stdlib-only. $0 local.
    python3 state/h011_wavelength_reach_2026_06_24/run_h011.py
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
    lorentz_gamma,
    undulator_wavelength,
)

# --- pre-registered parameters (FROZEN 2026-06-24) ---------------------------
PERIOD_NM = 15.0e6   # same undulator as H_006/H_007 (15 mm)
K = 1.0
SINGLE_STAGE_GEV = 1.0   # single-stage LPA reach (H_004)
FEW_STAGE_GEV = 2.0      # a few staged LPA modules


def main() -> int:
    # wavelength vs energy ladder
    ladder = {f"{E}GeV": undulator_wavelength(PERIOD_NM, lorentz_gamma(E * 1e9), K)
              for E in [0.5, 1, 2, 5, 10]}
    # energy needed for short targets
    e_3nm = energy_for_undulator_wavelength(3.0, PERIOD_NM, K) / 1e9
    e_1nm = energy_for_undulator_wavelength(1.0, PERIOD_NM, K) / 1e9
    e_01nm = energy_for_undulator_wavelength(0.1, PERIOD_NM, K) / 1e9

    # inverse-square law: doubling energy quarters wavelength
    inv_sq_ratio = ladder["2GeV"] / ladder["1GeV"]

    metrics = {
        "lambda_at_GeV": ladder,
        "energy_3nm_gev": e_3nm,
        "energy_1nm_gev": e_1nm,
        "energy_0p1nm_gev": e_01nm,
        "inv_square_ratio": inv_sq_ratio,
    }

    falsifiers = [
        Falsifier("F-WR-1 MONOTONE",
                  lambda m: not (m["lambda_at_GeV"]["10GeV"] < m["lambda_at_GeV"]["1GeV"]
                                 < m["lambda_at_GeV"]["0.5GeV"]),
                  "wavelength must keep falling as energy rises (no floor)"),
        Falsifier("F-WR-2 INVERSE-SQUARE", lambda m: abs(m["inv_square_ratio"] - 0.25) > 1e-6,
                  "doubling energy must quarter wavelength (lambda ~ 1/E^2)"),
        Falsifier("F-WR-3 SINGLE-STAGE", lambda m: not (m["energy_3nm_gev"] <= SINGLE_STAGE_GEV),
                  "3 nm must be within single-stage LPA reach (<=1 GeV)"),
        Falsifier("F-WR-4 FEW-STAGE", lambda m: not (m["energy_1nm_gev"] <= FEW_STAGE_GEV),
                  "1 nm (soft X-ray) must be within a few staged LPA modules (<=2 GeV)"),
        Falsifier("F-WR-5 BOUNDS",
                  lambda m: not (all(v > 0 for v in m["lambda_at_GeV"].values())
                                 and m["energy_0p1nm_gev"] > 0),
                  "all wavelengths/energies positive & finite"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_011 accelerator wavelength reach (15 mm undulator, K=1)")
    for E in [0.5, 1, 2, 5, 10]:
        print(f"  {E:>4} GeV -> {ladder[f'{E}GeV']:8.3f} nm")
    print(f"  energy needed: 3 nm={e_3nm:.2f} GeV | 1 nm={e_1nm:.2f} GeV | 0.1 nm={e_01nm:.2f} GeV")
    print(f"  1/E^2 check: lambda(2GeV)/lambda(1GeV) = {inv_sq_ratio:.4f} (expect 0.25)")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<18} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
