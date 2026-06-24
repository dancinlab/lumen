#!/usr/bin/env python3
"""H_004 — compact (plasma-wakefield) accelerator as a light-source enabler.

A laser-plasma accelerator sustains a GV/m-scale gradient (Dawson wave-breaking
field E_0), thousands of times the ~30 MV/m of conventional RF, so it reaches a
lithography-relevant electron energy in cm rather than tens of metres — the
enabling step toward a compact synchrotron / inverse-Compton EUV source.

Reference-matched to dancinlab/demiurge cern-accelerator
(hexa-lang stdlib/cern/plasma_wakefield.hexa): E_0(1e18 cm^-3) = 96.159 GV/m.

Deterministic, stdlib-only. $0 local.
    python3 state/h004_compact_accelerator_2026_06_24/run_h004.py
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
    accelerator_length,
    evaluate,
    plasma_omega,
    wavebreak_field,
)

# --- pre-registered parameters (FROZEN 2026-06-24) ---------------------------
N_E_CM3 = 1.0e18          # operating plasma density [cm^-3]
RF_GRADIENT = 30.0e6      # conventional RF gradient [V/m] (SCRF class, representative)
TARGET_ENERGY_EV = 1.0e9  # 1 GeV electrons (undulator/IC-relevant energy)
DEMIURGE_E0_GVM = 96.15919872735485  # reference anchor (PR #1176, |Δ|<=5e-13)


def main() -> int:
    omega_p = plasma_omega(N_E_CM3)
    e0 = wavebreak_field(omega_p)          # V/m
    e0_gvm = e0 / 1.0e9

    grad_ratio = e0 / RF_GRADIENT
    len_lpa = accelerator_length(TARGET_ENERGY_EV, e0)
    len_rf = accelerator_length(TARGET_ENERGY_EV, RF_GRADIENT)
    len_ratio = len_rf / len_lpa

    # density monotonicity check (higher density -> higher E_0)
    e0_lo = wavebreak_field(plasma_omega(N_E_CM3 / 4.0))

    metrics = {
        "omega_p_rad_s": omega_p,
        "e0_gvm": e0_gvm,
        "demiurge_e0_gvm": DEMIURGE_E0_GVM,
        "parity_abs_gvm": abs(e0_gvm - DEMIURGE_E0_GVM),
        "rf_gradient_mvm": RF_GRADIENT / 1.0e6,
        "gradient_ratio": grad_ratio,
        "len_lpa_m": len_lpa,
        "len_rf_m": len_rf,
        "len_ratio": len_ratio,
        "e0_lo_gvm": e0_lo / 1.0e9,
    }

    falsifiers = [
        Falsifier("F-CA-1 PARITY", lambda m: m["parity_abs_gvm"] > 1e-6,
                  "E_0 must match demiurge reference (reference-match)"),
        Falsifier("F-CA-2 GRADIENT", lambda m: not (m["gradient_ratio"] >= 100.0),
                  "wakefield gradient must be >=100x conventional RF"),
        Falsifier("F-CA-3 COMPACT", lambda m: not (m["len_ratio"] >= 100.0),
                  "LPA length must be <=1% of an RF linac for same energy"),
        Falsifier("F-CA-4 MONOTONE", lambda m: not (m["e0_gvm"] > m["e0_lo_gvm"]),
                  "higher density must give higher E_0"),
        Falsifier("F-CA-5 BOUNDS", lambda m: not all(v > 0 for v in
                  (m["e0_gvm"], m["len_lpa_m"], m["len_rf_m"], m["gradient_ratio"])),
                  "all quantities positive/finite"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_004 compact plasma-wakefield accelerator as light-source enabler")
    print(f"  n_e={N_E_CM3:.0e} cm^-3  omega_p={omega_p:.4e} rad/s")
    print(f"  E_0 = {e0_gvm:.5f} GV/m  (demiurge ref {DEMIURGE_E0_GVM:.5f}, |Δ|={metrics['parity_abs_gvm']:.2e})")
    print(f"  gradient ratio vs RF({RF_GRADIENT/1e6:.0f} MV/m) = {grad_ratio:.0f}x")
    print(f"  length to {TARGET_ENERGY_EV/1e9:.0f} GeV:  LPA={len_lpa*100:.2f} cm  vs  RF={len_rf:.1f} m  ({len_ratio:.0f}x shorter)")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<16} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
