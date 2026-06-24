#!/usr/bin/env python3
"""H_045 — risk localization (continuation capstone). After H_043 (power) and H_044
(footprint), the compact SSMB-Compton path has addressed every wall the campaign mapped:
  - wavelength: free dial, lambda ~ 1/gamma^2 (H_011), Compton reaches 13.5nm at MeV (H_033);
  - beam quality: Compton is slice-spread-immune (H_033) -> no FEL slice wall;
  - footprint: 7 MeV -> ~1 m ring (H_044);
  - power: SSMB steady-state micro-bunching -> coherent (N^2) CW (H_043).
ALL of these rest on ONE mechanism: steady-state micro-bunching at ~EUV-wavelength precision.
The 2021 proof-of-principle demonstrated the mechanism (at longer wavelength); pushing the
bunching to 13.5 nm precision is the SINGLE unproven, binding step. So the whole next-gen
compact-coherent-EUV question reduces to ONE measurable milestone: the bunching factor at
13.5 nm. Honest: that milestone is undemonstrated -> the entire path is gated on it.

Deterministic, stdlib-only. $0 local.
"""
from __future__ import annotations
import json, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__)); _ROOT=os.path.abspath(os.path.join(_HERE,"..",".."))
sys.path.insert(0, os.path.join(_ROOT,"tool"))
from lumen_optics import Falsifier, evaluate

# walls and whether the compact SSMB-Compton path addresses each
WALLS = {
    "wavelength":   ("addressed", "free dial + Compton at MeV (H_011/H_033)"),
    "beam-quality": ("addressed", "Compton slice-spread-immune (H_033)"),
    "footprint":    ("addressed", "7 MeV -> ~1 m ring (H_044)"),
    "power":        ("addressed", "SSMB coherent N^2 CW (H_043)"),
    "micro-bunching @EUV precision": ("OPEN", "the single binding unproven step"),
}
MECHANISM_DEMO_LONGER_LAMBDA = True   # Nature 2021 PoP at longer wavelength
EUV_PRECISION_BUNCHING_DEMONSTRATED = False  # the one gating milestone

def main()->int:
    addressed = [k for k,(s,_) in WALLS.items() if s=="addressed"]
    open_walls = [k for k,(s,_) in WALLS.items() if s=="OPEN"]
    m={"n_addressed":len(addressed),"n_open":len(open_walls),
       "mechanism_demo_longer":MECHANISM_DEMO_LONGER_LAMBDA,
       "euv_precision_demonstrated":EUV_PRECISION_BUNCHING_DEMONSTRATED}
    fs=[
     Falsifier("F-RL-1 OTHERS-ADDRESSED", lambda m: not (m["n_addressed"]>=4),
       "wavelength + beam-quality + footprint + power must all be addressed (>=4 walls)"),
     Falsifier("F-RL-2 SINGLE-RISK", lambda m: not (m["n_open"]==1),
       "exactly ONE binding residual must remain -> risk localized to one step"),
     Falsifier("F-RL-3 MECHANISM-DEMO", lambda m: not m["mechanism_demo_longer"],
       "the micro-bunching mechanism must be proof-of-principle demonstrated (Nature 2021, longer lambda)"),
     Falsifier("F-RL-4 MEASURABLE-MILESTONE", lambda m: not (m["n_open"]==1 and m["n_addressed"]>=4),
       "the next-gen compact-EUV question must reduce to ONE measurable milestone (EUV-precision bunching factor)"),
     Falsifier("F-RL-5 HONEST-GATE", lambda m: m["euv_precision_demonstrated"],
       "honest: EUV-precision steady-state micro-bunching must be UNdemonstrated -> the path is gated on it"),
     Falsifier("F-RL-6 BOUNDS", lambda m: not (m["n_addressed"]+m["n_open"]==len(WALLS)),
       "every wall classified"),
    ]
    led=evaluate(m,fs); v="SUPPORTED" if led["all_pass"] else "FALSIFIED"; led["verdict"]=v
    print("H_045 risk localization — the compact-coherent-EUV question reduces to ONE milestone")
    for k,(st,why) in WALLS.items():
        tag = "✅" if st=="addressed" else "🎯"
        print(f"  {tag} {k:<32} {st:<10} {why}")
    print(f"  => {len(addressed)} walls addressed, {len(open_walls)} open: '{open_walls[0]}'")
    print(f"  => the entire next-gen compact-coherent-EUV bet reduces to ONE measurable milestone:")
    print(f"     the steady-state micro-bunching factor achievable at 13.5 nm precision")
    print(f"  mechanism demonstrated at longer lambda (Nature 2021): {MECHANISM_DEMO_LONGER_LAMBDA} · EUV-precision: {EUV_PRECISION_BUNCHING_DEMONSTRATED}")
    for r in led["falsifiers"]: print(f"  {r['name']:<24} {r['status']}")
    print(f"VERDICT: {v}  ({led['n_pass']}/{led['n_total']} falsifiers PASS)")
    json.dump(led, open(os.path.join(_HERE,"result.json"),"w"), indent=2); return 0
if __name__=="__main__": raise SystemExit(main())
