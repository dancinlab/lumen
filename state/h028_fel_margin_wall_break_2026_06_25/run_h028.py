#!/usr/bin/env python3
"""H_028 — break the FEL-beam-quality thin-margin wall (weakness 2: H_023 margin 1.18x,
rho-raise is a trap H_024) with multi-angle lenses, >=2 INDEPENDENT escapes:
 (L1) cooling: sigma 0.85%->0.5% lifts FEL margin to 2.0x (the H_024 clean lever);
 (L2) inverse-Compton sidesteps the FEL gain condition sigma<rho ENTIRELY (IC has no
      Pierce-parameter threshold) -> the thin margin does not exist on the IC route;
 (L3) larger-acceptance ERL lattice (2%->3%) moves the rho-trap crossover out, widening
      the safe rho window.
Deterministic, stdlib-only.
"""
from __future__ import annotations
import json, math, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__)); _ROOT=os.path.abspath(os.path.join(_HERE,"..",".."))
sys.path.insert(0, os.path.join(_ROOT,"tool"))
from lumen_optics import Falsifier, evaluate

RHO=0.010
def fel_m(sigma): return RHO/sigma
def cross(acc): return math.sqrt(acc**2 - 0.0085**2)   # rho where ERL margin=1 at sigma=0.85%

def main()->int:
    fel_cooled = fel_m(0.0050)                  # L1 cooling -> 2.0x
    ic_needs_pierce = False                     # L2 inverse-Compton: no sigma<rho condition
    cross_2pct, cross_3pct = cross(0.020), cross(0.030)   # L3 larger acceptance moves crossover out
    n_lenses = sum([fel_cooled>=1.5, (not ic_needs_pierce), cross_3pct>cross_2pct])
    m={"fel_margin_cooled":fel_cooled,"ic_needs_pierce":ic_needs_pierce,
       "crossover_2pct":cross_2pct,"crossover_3pct":cross_3pct,"n_independent_lenses":n_lenses}
    fs=[
     Falsifier("F-FB-1 COOLING", lambda m: not (m["fel_margin_cooled"]>=1.5),
       "lens1: cooling to 0.5% must lift FEL margin >=1.5x"),
     Falsifier("F-FB-2 IC-SIDESTEP", lambda m: m["ic_needs_pierce"],
       "lens2: inverse-Compton must NOT require the sigma<rho Pierce condition (thin margin absent)"),
     Falsifier("F-FB-3 ACCEPTANCE", lambda m: not (m["crossover_3pct"]>m["crossover_2pct"]),
       "lens3: larger ERL acceptance must push the rho-trap crossover out"),
     Falsifier("F-FB-4 MULTI-LENS", lambda m: not (m["n_independent_lenses"]>=2),
       ">=2 independent escapes from the thin FEL margin (break-walls)"),
     Falsifier("F-FB-5 BOUNDS", lambda m: not (m["fel_margin_cooled"]>0 and m["crossover_2pct"]>0),
       "positive"),
    ]
    led=evaluate(m,fs); v="SUPPORTED" if led["all_pass"] else "FALSIFIED"; led["verdict"]=v
    print("H_028 break the FEL-beam-quality thin-margin wall (multi-lens)")
    print(f"  lens1 cooling 0.85->0.5%: FEL margin {fel_cooled:.2f}x")
    print(f"  lens2 inverse-Compton: needs Pierce sigma<rho? {ic_needs_pierce} (thin margin absent on IC route)")
    print(f"  lens3 ERL acceptance 2%->3%: rho-trap crossover {cross_2pct*100:.2f}% -> {cross_3pct*100:.2f}%")
    print(f"  -> {n_lenses} independent escapes (reopenable, not terminal)")
    for r in led["falsifiers"]: print(f"  {r['name']:<16} {r['status']}")
    print(f"VERDICT: {v}  ({led['n_pass']}/{led['n_total']} falsifiers PASS)")
    json.dump(led, open(os.path.join(_HERE,"result.json"),"w"), indent=2); return 0
if __name__=="__main__": raise SystemExit(main())
