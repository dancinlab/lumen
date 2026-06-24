#!/usr/bin/env python3
"""H_003 — NA vs depth-of-focus trade: resolution gains linearly, DoF loses
quadratically, so the focus penalty is steeper than the resolution gain.

Deterministic, stdlib-only. $0 local.
    python3 state/h003_na_dof_trade_2026_06_24/run_h003.py
"""

from __future__ import annotations

import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "tool"))

from lumen_optics import Falsifier, depth_of_focus, evaluate, resolution_half_pitch

# --- pre-registered parameters (FROZEN 2026-06-24) ---------------------------
LAMBDA = 13.5   # nm (EUV)
NA_LO = 0.33    # ASML NXE
NA_HI = 0.55    # ASML EXE (High-NA)
K1 = 0.3        # representative process k1
K2 = 0.5        # representative process k2


def main() -> int:
    res_lo = resolution_half_pitch(K1, LAMBDA, NA_LO)
    res_hi = resolution_half_pitch(K1, LAMBDA, NA_HI)
    dof_lo = depth_of_focus(K2, LAMBDA, NA_LO)
    dof_hi = depth_of_focus(K2, LAMBDA, NA_HI)

    res_gain = res_lo / res_hi          # >1: high NA prints finer
    dof_loss = dof_lo / dof_hi          # >1: high NA loses focus depth
    na_ratio_sq = (NA_HI / NA_LO) ** 2  # the NA^2 law

    metrics = {
        "res_lo_nm": res_lo, "res_hi_nm": res_hi,
        "dof_lo_nm": dof_lo, "dof_hi_nm": dof_hi,
        "res_gain": res_gain, "dof_loss": dof_loss,
        "na_ratio_sq": na_ratio_sq,
    }

    falsifiers = [
        Falsifier("F-DOF-1 RES-GAIN", lambda m: not (m["res_hi_nm"] < m["res_lo_nm"]),
                  "high NA must print finer"),
        Falsifier("F-DOF-2 DOF-LOSS", lambda m: not (m["dof_hi_nm"] < m["dof_lo_nm"]),
                  "high NA must shrink depth-of-focus"),
        Falsifier("F-DOF-3 QUADRATIC", lambda m: abs(m["dof_loss"] - m["na_ratio_sq"]) > 1e-9,
                  "DoF loss must equal (NA_hi/NA_lo)^2 (the NA^2 law)"),
        Falsifier("F-DOF-4 PENALTY", lambda m: not (m["dof_loss"] > m["res_gain"]),
                  "DoF penalty must be steeper than resolution gain"),
        Falsifier("F-DOF-5 BOUNDS", lambda m: not all(v > 0 for v in
                  (m["res_lo_nm"], m["res_hi_nm"], m["dof_lo_nm"], m["dof_hi_nm"])),
                  "all distances positive"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_003 NA vs depth-of-focus trade")
    print(f"  NA {NA_LO}->{NA_HI} @ {LAMBDA}nm")
    print(f"  resolution {res_lo:.2f} -> {res_hi:.2f} nm  (gain {res_gain:.3f}x finer)")
    print(f"  depth-of-focus {dof_lo:.2f} -> {dof_hi:.2f} nm  (loss {dof_loss:.3f}x)")
    print(f"  NA^2 law check: dof_loss={dof_loss:.4f} vs (NA_hi/NA_lo)^2={na_ratio_sq:.4f}")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<18} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
