#!/usr/bin/env python3
"""H_036 — loop cycle 2 DEEPEN (honest negative): the ICS flux margin from H_034 does NOT
survive the bandwidth-collection derating. Low-gamma ICS emits into a wide ~1/gamma cone,
but off-axis photons are red-shifted, so keeping the ~2% in-band requires collecting only a
narrow half-angle theta_c ~ sqrt(BW)/gamma. The collected solid-angle fraction ~ (gamma*theta_c)^2
= BW -> the usable in-band flux is derated by ~1/BW ~ 50x. That EATS the H_034 ~15x margin
(15/50 = 0.3x, margin LOST). Recovering it needs the demonstrated headroom: cavity finesse
1e4->1e5 (+10x) AND ERL current 1e3->1e4 class (+10x) = +100x -> restored ~30x. Honest: that
pushes BOTH levers to their demonstrated maximum, simultaneously, undemonstrated at EUV.

Deterministic, stdlib-only. $0 local.
"""
from __future__ import annotations
import json, math, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__)); _ROOT=os.path.abspath(os.path.join(_HERE,"..",".."))
sys.path.insert(0, os.path.join(_ROOT,"tool"))
from lumen_optics import Falsifier, evaluate

GAMMA = math.sqrt(1000.0/(4.0*13.5))   # ICS gamma for 13.5 nm @1um (= H_033, ~4.30)
BW = 0.02                              # 2% in-band requirement
H034_MARGIN = 15.0                     # the recirculation margin from H_034
FINESSE_HEADROOM = 10.0                # 1e4 -> 1e5 demonstrated IR finesse
ERL_CURRENT_HEADROOM = 10.0            # 1e3 -> 1e4 (10 mA -> 100 mA class) headroom

def main()->int:
    theta_cone = 1.0/GAMMA                       # full emission half-angle
    theta_collect = math.sqrt(BW)/GAMMA          # half-angle keeping 2% in-band
    solid_frac = (theta_collect/theta_cone)**2   # = BW
    derate = 1.0/solid_frac                       # ~50x
    margin_after_derate = H034_MARGIN/derate      # < 1 -> lost
    recovery = FINESSE_HEADROOM*ERL_CURRENT_HEADROOM
    margin_recovered = margin_after_derate*recovery
    m={"derate":derate,"margin_after_derate":margin_after_derate,"recovery":recovery,
       "margin_recovered":margin_recovered,"both_levers_maxed_demonstrated":False}
    fs=[
     Falsifier("F-DR-1 DERATE-REAL", lambda m: not (m["derate"]>=20.0),
       "the bandwidth-collection derating must be large (>=20x) -- a real effect, not negligible"),
     Falsifier("F-DR-2 MARGIN-LOST", lambda m: not (m["margin_after_derate"]<1.0),
       "the naive H_034 margin must be LOST after derating (honest negative, <1x)"),
     Falsifier("F-DR-3 HEADROOM-EXISTS", lambda m: not (m["recovery"]>=m["derate"]),
       "demonstrated finesse+current headroom must exceed the derating (recovery possible)"),
     Falsifier("F-DR-4 RECOVERED", lambda m: not (m["margin_recovered"]>=1.0),
       "after applying the headroom the margin must be restored (>=1x) -- the wall reopens again"),
     Falsifier("F-DR-5 HONEST-MAXED", lambda m: m["both_levers_maxed_demonstrated"],
       "running BOTH levers at their demonstrated max simultaneously at EUV must be UNdemonstrated"),
     Falsifier("F-DR-6 BOUNDS", lambda m: not (m["derate"]>0 and m["recovery"]>0),
       "positive"),
    ]
    led=evaluate(m,fs); v="SUPPORTED" if led["all_pass"] else "FALSIFIED"; led["verdict"]=v
    print("H_036 DEEPEN(2) — bandwidth-collection derating eats the ICS margin (honest negative)")
    print(f"  gamma {GAMMA:.2f}: emission cone {theta_cone*1e3:.0f} mrad, but 2% in-band needs collect <= {theta_collect*1e3:.0f} mrad")
    print(f"  collected solid fraction {solid_frac:.3f} -> flux DERATE {derate:.0f}x")
    print(f"  H_034 margin {H034_MARGIN:.0f}x -> after derate {margin_after_derate:.2f}x (LOST)")
    print(f"  recovery headroom finesse(x{FINESSE_HEADROOM:.0f}) x ERL-current(x{ERL_CURRENT_HEADROOM:.0f}) = x{recovery:.0f} -> restored {margin_recovered:.0f}x")
    print(f"  honest: both levers at demonstrated max SIMULTANEOUSLY at EUV? {m['both_levers_maxed_demonstrated']} -> the new front")
    for r in led["falsifiers"]: print(f"  {r['name']:<20} {r['status']}")
    print(f"VERDICT: {v}  ({led['n_pass']}/{led['n_total']} falsifiers PASS)")
    json.dump(led, open(os.path.join(_HERE,"result.json"),"w"), indent=2); return 0
if __name__=="__main__": raise SystemExit(main())
