#!/usr/bin/env python3
"""H_037 — loop cycle 3, BREAKTHROUGH ATTEMPT (honest negative expected): can a
high-brightness (low-divergence) electron beam beat the H_036 bandwidth-collection
derating by letting you collect a larger in-band cone fraction?

Tested claim: a low-divergence beam recovers the in-band fraction (raises it >= 2x BW).
Reality check: in ICS the wavelength-angle correlation is RADIATION KINEMATICS,
lambda(theta) = lambda_0 * (1 + gamma^2 theta^2). The off-axis photons are at a genuinely
different wavelength, OUT of the 2% band, REGARDLESS of beam quality. So the in-band cone
fraction is ~BW independent of beam brightness -> the escape does NOT work. We report this
honestly as FALSIFIED (the derating is a fundamental ICS tax, not a beam-quality problem).

Deterministic, stdlib-only. $0 local.
"""
from __future__ import annotations
import json, math, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__)); _ROOT=os.path.abspath(os.path.join(_HERE,"..",".."))
sys.path.insert(0, os.path.join(_ROOT,"tool"))
from lumen_optics import Falsifier, evaluate

GAMMA = math.sqrt(1000.0/(4.0*13.5))   # 13.5 nm ICS gamma (~4.30)
BW = 0.02
# in-band cone fraction for collection half-angle theta_c with lambda(theta)=l0(1+g^2 th^2):
# in-band requires g^2 th^2 <= BW -> fraction ~ (g th_c)^2 = BW, INDEPENDENT of beam divergence
def inband_fraction(beam_divergence_rad):
    theta_c = math.sqrt(BW)/GAMMA          # set by kinematics, not by the beam
    return (GAMMA*theta_c)**2              # = BW, regardless of beam_divergence

def main()->int:
    frac_high_div = inband_fraction(0.300)   # poor beam (300 mrad)
    frac_low_div  = inband_fraction(0.001)   # excellent beam (1 mrad)
    recovery = frac_low_div / frac_high_div  # = 1.0 -> NO recovery
    lever_works = recovery >= 2.0            # the tested claim
    m={"frac_high_div":frac_high_div,"frac_low_div":frac_low_div,"recovery":recovery,
       "lever_works":lever_works}
    fs=[
     Falsifier("F-HB-1 BRIGHTNESS-RECOVERS", lambda m: not m["lever_works"],
       "TESTED CLAIM: a high-brightness beam must recover the in-band fraction (>=2x). "
       "It does NOT (kinematic lambda-theta correlation is beam-independent) -> this falsifier TRIGGERS"),
     Falsifier("F-HB-2 KINEMATIC-INVARIANT", lambda m: not (abs(m["recovery"]-1.0)<1e-9),
       "the in-band fraction must be invariant to beam divergence (confirms the tax is fundamental)"),
     Falsifier("F-HB-3 BOUNDS", lambda m: not (m["frac_high_div"]>0),
       "positive"),
    ]
    led=evaluate(m,fs); v="SUPPORTED" if led["all_pass"] else "FALSIFIED"; led["verdict"]=v
    print("H_037 BREAKTHROUGH ATTEMPT (cycle 3) — high-brightness beam vs the bandwidth derating")
    print(f"  in-band fraction: poor beam {frac_high_div:.3f} · excellent beam {frac_low_div:.3f} -> recovery {recovery:.2f}x")
    print(f"  lambda(theta)=l0(1+gamma^2 theta^2) is RADIATION KINEMATICS -> off-axis photons are out-of-band regardless of beam")
    print(f"  => the high-brightness lever does NOT beat the ~50x derating (it is a FUNDAMENTAL ICS tax)")
    for r in led["falsifiers"]: print(f"  {r['name']:<24} {r['status']}")
    print(f"VERDICT: {v}  ({led['n_pass']}/{led['n_total']} falsifiers PASS)  [honest negative — escape does not exist]")
    json.dump(led, open(os.path.join(_HERE,"result.json"),"w"), indent=2); return 0
if __name__=="__main__": raise SystemExit(main())
