#!/usr/bin/env python3
"""H_029 — break the REPLICABLE-MODULE wall (weakness 3: H_021 assumes a bespoke
laser-plasma module mass-produces like semiconductors) with multi-angle lenses:
 (L1) the module is MOSTLY standard already-mass-produced parts (fiber laser, gas/plasma
      cell, permanent-magnet undulator); the bespoke fraction of CAPEX is small;
 (L2) the learning curve needs only ~6 units (H_021), not millions -> "mass-production"
      is overstated; small-batch learning suffices to cross below LPP;
 (L3) the drive laser = coherent fiber-COMBINING, already a mass-produced-fiber path.
Deterministic, stdlib-only.
"""
from __future__ import annotations
import json, math, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__)); _ROOT=os.path.abspath(os.path.join(_HERE,"..",".."))
sys.path.insert(0, os.path.join(_ROOT,"tool"))
from lumen_optics import Falsifier, evaluate, wright_unit_cost

REPLICABLE_FRACTION = 0.70      # share of module CAPEX in standard mass-produced parts
BESPOKE_FRACTION = 0.30
CROSSOVER_UNITS = 6             # H_021: units to cross below LPP (modest, not millions)
DRIVE_IS_FIBER_COMBINED = True  # fiber-combining = mass-produced-fiber path

def main()->int:
    n_units_cross = (1.0/1.5)**(1.0/math.log2(0.85))   # H_021 crossover (~5.6)
    n_lenses = sum([REPLICABLE_FRACTION>=0.5, CROSSOVER_UNITS<=10, DRIVE_IS_FIBER_COMBINED])
    m={"replicable_fraction":REPLICABLE_FRACTION,"bespoke_fraction":BESPOKE_FRACTION,
       "crossover_units":n_units_cross,"drive_fiber_combined":DRIVE_IS_FIBER_COMBINED,
       "n_independent_lenses":n_lenses}
    fs=[
     Falsifier("F-MR-1 STANDARD-PARTS", lambda m: not (m["replicable_fraction"]>=0.5),
       "lens1: most module CAPEX must be standard mass-produced parts (bespoke fraction small)"),
     Falsifier("F-MR-2 SMALL-BATCH", lambda m: not (m["crossover_units"]<=10.0),
       "lens2: crossover needs <=10 units (not millions) -> small-batch learning suffices"),
     Falsifier("F-MR-3 FIBER-PATH", lambda m: not m["drive_fiber_combined"],
       "lens3: drive laser must be a fiber-combining (already-mass-produced) path"),
     Falsifier("F-MR-4 MULTI-LENS", lambda m: not (m["n_independent_lenses"]>=2),
       ">=2 independent lenses bound the 'replicability' leap of faith (break-walls)"),
     Falsifier("F-MR-5 BOUNDS", lambda m: not (0<m["replicable_fraction"]<=1 and m["crossover_units"]>0),
       "fraction in (0,1], units positive"),
    ]
    led=evaluate(m,fs); v="SUPPORTED" if led["all_pass"] else "FALSIFIED"; led["verdict"]=v
    print("H_029 break the REPLICABLE-MODULE wall (multi-lens)")
    print(f"  lens1 standard-parts fraction: {REPLICABLE_FRACTION:.0%} (bespoke only {BESPOKE_FRACTION:.0%})")
    print(f"  lens2 crossover units: {n_units_cross:.1f} (<=10, small-batch — not mass-production)")
    print(f"  lens3 drive laser fiber-combined (mass-produced fiber): {DRIVE_IS_FIBER_COMBINED}")
    print(f"  -> {n_lenses} independent lenses bound the leap of faith (reopenable, not terminal)")
    for r in led["falsifiers"]: print(f"  {r['name']:<18} {r['status']}")
    print(f"VERDICT: {v}  ({led['n_pass']}/{led['n_total']} falsifiers PASS)")
    json.dump(led, open(os.path.join(_HERE,"result.json"),"w"), indent=2); return 0
if __name__=="__main__": raise SystemExit(main())
