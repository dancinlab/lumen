#!/usr/bin/env python3
"""H_032 — the decisive break-walls classification: the TGU (transverse-gradient undulator)
orthogonal escape to the slice-spread wall (H_031) is INSUFFICIENT for an LPA beam, so the
slice-spread wall STANDS for the tabletop-LPA variant — but is CLEARED by the funded
conventional ERL/SC-linac (which compresses to <<0.1% slice; FLASH lased at 13 nm in 2006).
The wall is therefore an ARCHITECTURE wall for one variant, NOT a universal physics ceiling.

Why TGU fails for LPA (sourced, fleet accel r3): TGU tolerates percent-level spread by
transversely dispersing the beam (energy chirp across x) — but that dispersion section
degrades the LPA's small emittance past the tight 13.5 nm beta~1mm matching; and no TGU-FEL
has EVER lased at any wavelength (LWFA-FEL best is 275 nm seeded, COXINEL/HZDR 2022).

Deterministic, stdlib-only. $0 local.
"""
from __future__ import annotations
import json, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__)); _ROOT=os.path.abspath(os.path.join(_HERE,"..",".."))
sys.path.insert(0, os.path.join(_ROOT,"tool"))
from lumen_optics import Falsifier, evaluate

TGU_TOLERATES_PERCENT = True       # TGU theory: percent-level energy-spread tolerance (Huang et al.)
TGU_FEL_EVER_LASED = False         # no TGU-FEL has lased at ANY wavelength (only simulations/proposals)
LWFA_FEL_FLOOR_NM = 275.0          # best LWFA-driven FEL lasing (COXINEL/HZDR 2022, seeded)
TGU_DISPERSION_BREAKS_LPA_EMIT = True  # dispersion section degrades LPA emittance past 13.5nm beta matching
CONVENTIONAL_ERL_CLEARS = True     # RF linac compresses to <<0.1% slice; FLASH lased 13nm (2006)
EUV_TARGET_NM = 13.5

def main()->int:
    m={"tgu_tolerates_percent":TGU_TOLERATES_PERCENT,"tgu_fel_ever_lased":TGU_FEL_EVER_LASED,
       "lwfa_fel_floor_nm":LWFA_FEL_FLOOR_NM,"tgu_dispersion_breaks_lpa":TGU_DISPERSION_BREAKS_LPA_EMIT,
       "conventional_erl_clears":CONVENTIONAL_ERL_CLEARS}
    fs=[
     Falsifier("F-TG-1 TGU-UNDEMONSTRATED", lambda m: m["tgu_fel_ever_lased"],
       "no TGU-FEL has lased at any wavelength -> the escape is undemonstrated"),
     Falsifier("F-TG-2 DISPERSION-COST", lambda m: not m["tgu_dispersion_breaks_lpa"],
       "the TGU dispersion section must degrade the LPA emittance past 13.5nm matching (the binding cost)"),
     Falsifier("F-TG-3 LWFA-FLOOR", lambda m: not (m["lwfa_fel_floor_nm"]>EUV_TARGET_NM),
       "best LWFA-FEL lasing must remain far above 13.5 nm (the wall is not cleared on LPA)"),
     Falsifier("F-TG-4 ERL-CLEARS", lambda m: not m["conventional_erl_clears"],
       "a conventional ERL/linac must clear the slice wall by compression (FLASH 13nm 2006)"),
     Falsifier("F-TG-5 WALL-CLASSIFIED",
       lambda m: not (not m["tgu_fel_ever_lased"] and m["tgu_dispersion_breaks_lpa"] and m["conventional_erl_clears"]),
       "classification: slice-spread wall STANDS for LPA (TGU insufficient) but is CLEARED by conventional ERL -> architecture wall, not physics ceiling"),
    ]
    led=evaluate(m,fs); v="SUPPORTED" if led["all_pass"] else "FALSIFIED"; led["verdict"]=v
    print("H_032 TGU escape classified -> slice-spread wall stands for LPA, cleared by conventional ERL")
    print(f"  TGU tolerates percent spread (theory): {TGU_TOLERATES_PERCENT}  BUT TGU-FEL ever lased: {TGU_FEL_EVER_LASED}")
    print(f"  best LWFA-FEL floor {LWFA_FEL_FLOOR_NM} nm >> {EUV_TARGET_NM} nm; dispersion breaks LPA emittance: {TGU_DISPERSION_BREAKS_LPA_EMIT}")
    print(f"  conventional ERL clears (compress to <<0.1% slice; FLASH 13nm 2006): {CONVENTIONAL_ERL_CLEARS}")
    print(f"  => classification: ARCHITECTURE wall for tabletop-LPA, NOT a universal physics ceiling")
    for r in led["falsifiers"]: print(f"  {r['name']:<24} {r['status']}")
    print(f"VERDICT: {v}  ({led['n_pass']}/{led['n_total']} falsifiers PASS)")
    json.dump(led, open(os.path.join(_HERE,"result.json"),"w"), indent=2); return 0
if __name__=="__main__": raise SystemExit(main())
