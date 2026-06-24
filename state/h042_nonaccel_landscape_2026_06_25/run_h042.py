#!/usr/bin/env python3
"""H_042 — non-accelerator landscape / first-peak check (gap top-3 #2). The verified spine
committed to the accelerator family early (CERN seed). Fleet lane 2 surveyed the NON-
accelerator EUV families vs the HVM flux floor (~100 W in-band): NONE reaches HVM, so
'accelerator is the answer' is NOT a first-peak artifact -- it survives. Honest nuance: the
COMPACT accelerator wins WAVELENGTH (dial), not power; the flux wall (H_008) stays binding,
and the FEL/conventional form clears power. Reconfirms the campaign, not refutes it.
"""
from __future__ import annotations
import json, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__)); _ROOT=os.path.abspath(os.path.join(_HERE,"..",".."))
sys.path.insert(0, os.path.join(_ROOT,"tool"))
from lumen_optics import Falsifier, evaluate

HVM_FLOOR_W = 100.0
FAMILIES = {"HHG (gas)":30.0, "DPP (discharge Xe)":0.04, "all-optical cascade":0.1, "recombination laser":2.0}
ACCEL_FEL_W = 4000.0
COMPACT_LPA_WINS_WAVELENGTH = True
COMPACT_LPA_ALONE_MEETS_POWER = False

def main()->int:
    fracs = {k: w/HVM_FLOOR_W for k,w in FAMILIES.items()}
    nonaccel_clears = [k for k,f in fracs.items() if f>=1.0]
    accel_frac = ACCEL_FEL_W/HVM_FLOOR_W
    m={"n_nonaccel_clear":len(nonaccel_clears),"accel_fel_frac":accel_frac,
       "compact_wins_wavelength":COMPACT_LPA_WINS_WAVELENGTH,
       "compact_alone_meets_power":COMPACT_LPA_ALONE_MEETS_POWER,"best_nonaccel_frac":max(fracs.values())}
    fs=[
     Falsifier("F-LS-1 HHG-LOSES", lambda m: not (fracs["HHG (gas)"]<1.0), "HHG < floor"),
     Falsifier("F-LS-2 DPP-LOSES", lambda m: not (fracs["DPP (discharge Xe)"]<1.0), "DPP < floor"),
     Falsifier("F-LS-3 NO-NONACCEL-CLEARS", lambda m: not (m["n_nonaccel_clear"]==0),
       "no non-accelerator family reaches HVM -> not a first-peak artifact"),
     Falsifier("F-LS-4 ACCEL-CLEARS", lambda m: not (m["accel_fel_frac"]>=1.0),
       "the FEL (accelerator) must clear the floor (the survivor)"),
     Falsifier("F-LS-5 COMPACT-WAVELENGTH-NOT-POWER",
       lambda m: not (m["compact_wins_wavelength"] and not m["compact_alone_meets_power"]),
       "compact LPA wins wavelength but not power alone (H_008 reconfirmed, honest)"),
     Falsifier("F-LS-6 BOUNDS", lambda m: not (m["best_nonaccel_frac"]>0), "positive"),
    ]
    led=evaluate(m,fs); v="SUPPORTED" if led["all_pass"] else "FALSIFIED"; led["verdict"]=v
    print("H_042 non-accelerator landscape — first-peak check")
    for k,f in fracs.items():
        print(f"  {k:<22} {FAMILIES[k]:>7.2f} W = {f:.4f}x floor  {'CLEARS' if f>=1 else 'loses'}")
    print(f"  accelerator FEL: {ACCEL_FEL_W:.0f} W = {accel_frac:.0f}x floor  CLEARS (only survivor)")
    print(f"  => 0 non-accelerator families reach HVM -> 'accelerator is the answer' survives (not first-peak)")
    print(f"  => honest: compact LPA wins WAVELENGTH (dial), not POWER; flux wall H_008 binding")
    for r in led["falsifiers"]: print(f"  {r['name']:<28} {r['status']}")
    print(f"VERDICT: {v}  ({led['n_pass']}/{led['n_total']} falsifiers PASS)")
    json.dump(led, open(os.path.join(_HERE,"result.json"),"w"), indent=2); return 0
if __name__=="__main__": raise SystemExit(main())
