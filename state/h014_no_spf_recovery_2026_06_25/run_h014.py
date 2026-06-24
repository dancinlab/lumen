#!/usr/bin/env python3
"""H_014 — no-SPF in-band recovery (promotes abstract H_B1): an intrinsically
narrow source drops the spectral-purity filter a broadband LPP needs, recovering
the ~25-30% in-band power the SPF throws away. Narrow is REQUIRED (broadband
without an SPF exceeds the out-of-band contamination tolerance).

Deterministic, stdlib-only. $0 local.
    python3 state/h014_no_spf_recovery_2026_06_25/run_h014.py
"""

from __future__ import annotations

import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "tool"))

from lumen_optics import Falsifier, evaluate, spf_recovery

# --- pre-registered parameters (FROZEN 2026-06-25) ---------------------------
SPF_TRANSMISSION = 0.70    # broadband path keeps a spectral-purity filter (~30% loss)
OOB_BROADBAND = 0.15       # out-of-band fraction of a broadband LPP (needs filtering)
OOB_NARROW = 0.001         # out-of-band fraction of an intrinsically narrow source
OOB_TOLERANCE = 0.02       # max OOB the wafer/optics tolerate without an SPF


def main() -> int:
    recovery = spf_recovery(SPF_TRANSMISSION)
    narrow_can_skip = OOB_NARROW <= OOB_TOLERANCE
    broadband_must_keep = OOB_BROADBAND > OOB_TOLERANCE
    recovery_tighter = spf_recovery(0.60)   # worse SPF loss -> more to recover

    metrics = {
        "spf_transmission": SPF_TRANSMISSION,
        "recovery": recovery,
        "narrow_can_skip_spf": narrow_can_skip,
        "broadband_must_keep_spf": broadband_must_keep,
        "recovery_at_0p60": recovery_tighter,
    }

    falsifiers = [
        Falsifier("F-SPF-1 RECOVER", lambda m: not (m["recovery"] >= 1.25),
                  "dropping the SPF must recover >= 25% in-band power"),
        Falsifier("F-SPF-2 NARROW-REQ", lambda m: not (m["narrow_can_skip_spf"]
                  and m["broadband_must_keep_spf"]),
                  "narrow source may skip the SPF; broadband may not (the recovery needs a narrow line)"),
        Falsifier("F-SPF-3 MONOTONE", lambda m: not (m["recovery_at_0p60"] > m["recovery"]),
                  "more SPF loss -> more recovery available"),
        Falsifier("F-SPF-4 NO-FREE-LUNCH", lambda m: not (m["recovery"] <= 1.0 / m["spf_transmission"] + 1e-9),
                  "recovery is bounded by 1/transmission (no over-claim)"),
        Falsifier("F-SPF-5 BOUNDS", lambda m: not (m["recovery"] > 1.0 and 0 < m["spf_transmission"] <= 1.0),
                  "recovery > 1, transmission in (0,1]"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_014 no-SPF in-band recovery (promotes H_B1)")
    print(f"  broadband SPF transmission {SPF_TRANSMISSION} -> narrow recovers {recovery:.3f}x ({(recovery-1)*100:.0f}%)")
    print(f"  narrow OOB {OOB_NARROW} <= tol {OOB_TOLERANCE}: skip SPF = {narrow_can_skip}")
    print(f"  broadband OOB {OOB_BROADBAND} > tol: must keep SPF = {broadband_must_keep}")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<18} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
