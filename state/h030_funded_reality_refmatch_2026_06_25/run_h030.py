#!/usr/bin/env python3
"""H_030 — reference-match the campaign conclusion against the FUNDED reality (fleet
prior-art + accel lanes). The accelerator-driven FEL EUV direction is REAL and funded
(xLight, KEK) — validating lumen's direction — BUT three honest corrections land:
 (1) the funded DRIVER is a conventional ERL/SC-linac, NOT the tabletop LPA the campaign
     emphasized -> lumen's LPA leg is the less-mature, less-funded variant;
 (2) the funded ECONOMIC leg is M9-amortization (one big source -> ~20 scanners), NOT the
     M7 module-array learning curve H_021 leaned on;
 (3) LPA-FEL has never lased at 13.5 nm (demonstrated floor ~25 nm) and single-pass cooling
     is undemonstrated -> H_028's cooling lens is aspirational.
 Plus: the LPA-EUV-FEL concept predates lumen (Nakajima 2014) -> not a novel synthesis.

Deterministic, stdlib-only. $0 local.
"""
from __future__ import annotations
import json, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__)); _ROOT=os.path.abspath(os.path.join(_HERE,"..",".."))
sys.path.insert(0, os.path.join(_ROOT,"tool"))
from lumen_optics import Falsifier, evaluate

# funded reality (fleet prior-art lane, public sources)
FUNDED_PROGRAMS = {"xLight":"conventional-ERL/SC-linac", "KEK-EUV-FEL":"conventional-ERL"}
FUNDED_DRIVER_IS_LPA = False              # both funded programs use conventional accelerators
FUNDED_ECON_LEG = "M9-amortization"       # one source -> ~20 scanners (not M7 module-array)
LPA_FEL_FLOOR_NM = 25.0                   # best demonstrated LPA-FEL lasing (Wang 2021: 27nm; 2026: ~25nm)
EUV_TARGET_NM = 13.5
COOLING_SINGLE_PASS_DEMONSTRATED = False  # OSC only on storage rings, not single-pass LPA
CONCEPT_YEAR, LUMEN_YEAR = 2014, 2026     # Nakajima HPLSE 2014 predates lumen

def main()->int:
    m={"funded_programs":len(FUNDED_PROGRAMS),"funded_driver_is_lpa":FUNDED_DRIVER_IS_LPA,
       "funded_econ_leg":FUNDED_ECON_LEG,"lpa_fel_floor_nm":LPA_FEL_FLOOR_NM,
       "cooling_single_pass":COOLING_SINGLE_PASS_DEMONSTRATED,"concept_year":CONCEPT_YEAR}
    fs=[
     Falsifier("F-PA-1 DIRECTION-FUNDED", lambda m: not (m["funded_programs"]>=2),
       ">=2 funded accelerator-EUV-FEL programs must exist (direction validated, not speculation)"),
     Falsifier("F-PA-2 DRIVER-CORRECTION", lambda m: m["funded_driver_is_lpa"],
       "the funded driver must be conventional ERL, NOT LPA (campaign's tabletop-LPA = less-mature variant)"),
     Falsifier("F-PA-3 ECON-LEG-CORRECTION", lambda m: not (m["funded_econ_leg"]=="M9-amortization"),
       "the funded economic leg must be M9-amortization (one source -> many scanners), NOT the M7 module-array"),
     Falsifier("F-PA-4 WAVELENGTH-GAP", lambda m: not (m["lpa_fel_floor_nm"]>EUV_TARGET_NM),
       "demonstrated LPA-FEL floor must exceed 13.5 nm (13.5 nm on LPA is unproven)"),
     Falsifier("F-PA-5 NOT-NOVEL", lambda m: not (m["concept_year"]<LUMEN_YEAR),
       "the LPA-EUV-FEL concept must predate lumen (Nakajima 2014) -> not a novel synthesis"),
     Falsifier("F-PA-6 COOLING-ASPIRATIONAL", lambda m: m["cooling_single_pass"],
       "single-pass LPA cooling must be UNdemonstrated (H_028 cooling lens is aspirational)"),
    ]
    led=evaluate(m,fs); v="SUPPORTED" if led["all_pass"] else "FALSIFIED"; led["verdict"]=v
    print("H_030 funded-reality reference-match (fleet prior-art + accel)")
    print(f"  funded programs: {FUNDED_PROGRAMS} -> direction REAL+funded")
    print(f"  correction 1: funded driver is LPA? {FUNDED_DRIVER_IS_LPA} (conventional ERL funded, not tabletop LPA)")
    print(f"  correction 2: funded econ leg = {FUNDED_ECON_LEG} (one source->~20 scanners; M9 not M7)")
    print(f"  correction 3: LPA-FEL floor {LPA_FEL_FLOOR_NM} nm > {EUV_TARGET_NM} nm target; single-pass cooling demonstrated? {COOLING_SINGLE_PASS_DEMONSTRATED}")
    print(f"  novelty: concept {CONCEPT_YEAR} predates lumen {LUMEN_YEAR} -> not novel")
    for r in led["falsifiers"]: print(f"  {r['name']:<24} {r['status']}")
    print(f"VERDICT: {v}  ({led['n_pass']}/{led['n_total']} falsifiers PASS)")
    json.dump(led, open(os.path.join(_HERE,"result.json"),"w"), indent=2); return 0
if __name__=="__main__": raise SystemExit(main())
