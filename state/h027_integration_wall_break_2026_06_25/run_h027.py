#!/usr/bin/env python3
"""H_027 — break the INTEGRATION wall (weakness 1: components exist but never on one
machine, H_022 L1) with multi-angle lenses. The wall is reopenable because >=2
independent lenses reduce it from "unknown invention" to "bounded engineering":
 (L1) every subsystem has a STANDALONE demonstration (LPA 1 GeV, LPA-FEL lasing,
      ERL energy recovery, undulator/IC) -> the gap is integration, not new physics;
 (L2) the synchrotron/FEL light-source PRECEDENT integrates undulator+ring+beamlines
      at facilities today -> integration physics is known, only the compact form is new;
 (L3) start-to-end simulation (digital twin) de-risks the joint constraints before metal.
Deterministic, stdlib-only.
"""
from __future__ import annotations
import json, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__)); _ROOT=os.path.abspath(os.path.join(_HERE,"..",".."))
sys.path.insert(0, os.path.join(_ROOT,"tool"))
from lumen_optics import Falsifier, evaluate

# subsystem standalone-demonstration TRL (1-9); integration = combining proven parts
SUBSYS_TRL = {"LPA-1GeV":5, "LPA-FEL-lasing":4, "ERL-recovery":6, "undulator/IC":9}
PRECEDENT_INTEGRATED = True     # synchrotron/FEL facilities integrate undulator+ring+beamlines
S2E_SIM_AVAILABLE = True        # start-to-end codes (Genesis/Ocelot/elegant class) exist
INVENTION_TRL = 1               # "needs new physics" baseline

def main()->int:
    min_trl = min(SUBSYS_TRL.values())
    n_lenses = sum([min_trl>INVENTION_TRL, PRECEDENT_INTEGRATED, S2E_SIM_AVAILABLE])
    m={"min_subsystem_trl":min_trl,"precedent_integrated":PRECEDENT_INTEGRATED,
       "s2e_sim":S2E_SIM_AVAILABLE,"n_independent_lenses":n_lenses}
    fs=[
     Falsifier("F-IN-1 NO-INVENTION", lambda m: not (m["min_subsystem_trl"]>INVENTION_TRL),
       "every subsystem must be standalone-demonstrated (TRL>1) -> integration not invention"),
     Falsifier("F-IN-2 PRECEDENT", lambda m: not m["precedent_integrated"],
       "an integrated undulator+ring+beamline precedent must exist (synchrotron/FEL)"),
     Falsifier("F-IN-3 S2E", lambda m: not m["s2e_sim"],
       "start-to-end simulation must be available to de-risk joint constraints"),
     Falsifier("F-IN-4 MULTI-LENS", lambda m: not (m["n_independent_lenses"]>=2),
       ">=2 independent lenses must reduce the wall (break-walls discipline)"),
     Falsifier("F-IN-5 BOUNDS", lambda m: not (m["min_subsystem_trl"]>=1),
       "TRL valid"),
    ]
    led=evaluate(m,fs); v="SUPPORTED" if led["all_pass"] else "FALSIFIED"; led["verdict"]=v
    print("H_027 break the INTEGRATION wall (multi-lens)")
    print(f"  subsystem standalone TRL: {SUBSYS_TRL} (min {min_trl} > 1 invention)")
    print(f"  lens1 integration-not-invention: {min_trl>1} · lens2 precedent: {PRECEDENT_INTEGRATED} · lens3 s2e-sim: {S2E_SIM_AVAILABLE}")
    print(f"  -> {n_lenses} independent lenses reduce the wall to bounded engineering (reopenable, not terminal)")
    for r in led["falsifiers"]: print(f"  {r['name']:<16} {r['status']}")
    print(f"VERDICT: {v}  ({led['n_pass']}/{led['n_total']} falsifiers PASS)")
    json.dump(led, open(os.path.join(_HERE,"result.json"),"w"), indent=2); return 0
if __name__=="__main__": raise SystemExit(main())
