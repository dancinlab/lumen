#!/usr/bin/env python3
"""H_007 — sub-13.5 nm tunability by electron energy: the SAME undulator reaches
13.5 / 6.5 / 5 / 3 nm by raising electron energy (gamma ~ 1/sqrt(lambda)), all
within a ~2x energy dial and single-stage LPA reach — no emitter-element swap,
no new mirror multilayer.

Deterministic, stdlib-only. $0 local.
    python3 state/h007_sub13_tunability_2026_06_24/run_h007.py
"""

from __future__ import annotations

import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "tool"))

from lumen_optics import Falsifier, energy_for_undulator_wavelength, evaluate

# --- pre-registered parameters (FROZEN 2026-06-24) ---------------------------
TARGETS_NM = [13.5, 6.5, 5.0, 3.0]   # EUV -> BEUV ladder (transcript)
PERIOD_NM = 15.0e6                   # same undulator as H_006
K = 1.0
LPA_REACH_EV = 1.0e9                 # single-stage LPA reach (H_004)


def main() -> int:
    energies = {f"{t}nm": energy_for_undulator_wavelength(t, PERIOD_NM, K) for t in TARGETS_NM}
    e_ref = energies["13.5nm"]
    e_min = energies["3.0nm"]

    # sqrt-law check: E(lambda)/E(13.5) should equal sqrt(13.5/lambda)
    sqrt_ok = all(
        abs(energies[f"{t}nm"] / e_ref - (13.5 / t) ** 0.5) < 1e-9 for t in TARGETS_NM
    )
    dial_ratio = e_min / e_ref  # 3 nm vs 13.5 nm energy span

    metrics = {
        "energy_mev": {k: v / 1e6 for k, v in energies.items()},
        "max_energy_mev": e_min / 1e6,
        "lpa_reach_mev": LPA_REACH_EV / 1e6,
        "sqrt_law_holds": sqrt_ok,
        "dial_ratio_3_over_135": dial_ratio,
    }

    falsifiers = [
        Falsifier("F-TUN-1 SPAN", lambda m: not (m["max_energy_mev"] <= m["lpa_reach_mev"]),
                  "all targets incl. 3nm must be within single-stage LPA reach"),
        Falsifier("F-TUN-2 SQRT-LAW", lambda m: not m["sqrt_law_holds"],
                  "E(lambda) must follow gamma ~ 1/sqrt(lambda)"),
        Falsifier("F-TUN-3 MONOTONE",
                  lambda m: not (m["energy_mev"]["3.0nm"] > m["energy_mev"]["13.5nm"]),
                  "shorter wavelength must need higher energy"),
        Falsifier("F-TUN-4 DIAL", lambda m: not (m["dial_ratio_3_over_135"] <= 3.0),
                  "13.5->3nm must be a modest energy dial (<=3x), not a regime change"),
        Falsifier("F-TUN-5 BOUNDS", lambda m: not all(v > 0 for v in m["energy_mev"].values()),
                  "all energies positive"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_007 sub-13.5 nm tunability by electron energy (same undulator)")
    for t in TARGETS_NM:
        print(f"  {t:>5} nm -> {energies[f'{t}nm']/1e6:7.1f} MeV")
    print(f"  dial 13.5->3 nm = {dial_ratio:.2f}x energy  (LPA reach {LPA_REACH_EV/1e6:.0f} MeV)")
    print(f"  sqrt-law (gamma ~ 1/sqrt(lambda)) holds: {sqrt_ok}")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<16} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
