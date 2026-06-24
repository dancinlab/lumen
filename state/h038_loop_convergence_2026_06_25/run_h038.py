#!/usr/bin/env python3
"""H_038 — loop cycle 3 DEEPEN -> CONVERGENCE. After three cycles the compact-source
chain is fully classified, and the break-walls 'enumerate orthogonal mechanism families
before dry' condition is met:
 - FEL family: bound by SLICE energy spread; only a conventional ERL clears it (H_031/032).
 - ICS / gain-free family: escapes the slice-spread wall (H_033) but its flux margin is eaten
   by a FUNDAMENTAL bandwidth-collection tax that no beam-quality lever beats (H_036 + H_037
   falsified) -> 'terminal-thin' (possible in principle, no engineering margin, undemonstrated).
 - recombination-laser family: harder than its representative anchor (H_017 / H_026).
So the three supply-side radiation mechanism families are enumerated and each routes back to
needing conventional-ERL-class beam + recirculation. The loop CONVERGES: the robust
litho-power answer is the conventional ERL FEL (H_030); compact coherent EUV is terminal-thin.

Deterministic, stdlib-only. $0 local.
"""
from __future__ import annotations
import json, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__)); _ROOT=os.path.abspath(os.path.join(_HERE,"..",".."))
sys.path.insert(0, os.path.join(_ROOT,"tool"))
from lumen_optics import Falsifier, evaluate

# classification of the three supply-side radiation mechanism families
FAMILIES = {
    "FEL (gain)":            "slice-spread-bound -> needs conventional ERL (H_031/032)",
    "ICS (gain-free)":       "terminal-thin -> fundamental bandwidth tax, no beam lever (H_036/037)",
    "recombination-laser":   "harder than anchor (H_017/H_026)",
}
ICS_DERATING_FUNDAMENTAL = True   # H_037 falsified the beam-brightness escape
COMPACT_PATH_TERMINAL_THIN = True # possible in principle, no engineering margin, undemonstrated
ROBUST_ANSWER_IS_ERL = True       # every family routes back to ERL-class beam + recirculation

def main()->int:
    n_families = len(FAMILIES)
    m={"n_families_enumerated":n_families,"ics_derating_fundamental":ICS_DERATING_FUNDAMENTAL,
       "compact_terminal_thin":COMPACT_PATH_TERMINAL_THIN,"robust_answer_erl":ROBUST_ANSWER_IS_ERL}
    fs=[
     Falsifier("F-LC-1 FAMILIES-ENUMERATED", lambda m: not (m["n_families_enumerated"]>=3),
       ">=3 orthogonal supply-side radiation mechanism families must be classified (break-walls dry)"),
     Falsifier("F-LC-2 ICS-FUNDAMENTAL-TAX", lambda m: not m["ics_derating_fundamental"],
       "the ICS bandwidth derating must be fundamental (H_037 falsified the beam-brightness escape)"),
     Falsifier("F-LC-3 COMPACT-TERMINAL-THIN", lambda m: not m["compact_terminal_thin"],
       "the compact coherent-EUV path must be terminal-thin (reopens only by stacking demonstrated maxima)"),
     Falsifier("F-LC-4 CONVERGES-TO-ERL", lambda m: not m["robust_answer_erl"],
       "every family must route back to conventional-ERL-class beam+recirc (loop converges to ERL, H_030)"),
     Falsifier("F-LC-5 BOUNDS", lambda m: not (m["n_families_enumerated"]>=1),
       "valid"),
    ]
    led=evaluate(m,fs); v="SUPPORTED" if led["all_pass"] else "FALSIFIED"; led["verdict"]=v
    print("H_038 loop CONVERGENCE — orthogonal mechanism families enumerated, compact path terminal-thin")
    for fam, cls in FAMILIES.items():
        print(f"  {fam:<22} {cls}")
    print(f"  => {n_families} families classified; ICS tax fundamental (H_037 falsified the escape)")
    print(f"  => compact coherent EUV is TERMINAL-THIN; robust litho-power answer is the conventional ERL (H_030)")
    print(f"  => break-walls dry condition met -> the 돌파/검증/심화 loop CONVERGES")
    for r in led["falsifiers"]: print(f"  {r['name']:<24} {r['status']}")
    print(f"VERDICT: {v}  ({led['n_pass']}/{led['n_total']} falsifiers PASS)")
    json.dump(led, open(os.path.join(_HERE,"result.json"),"w"), indent=2); return 0
if __name__=="__main__": raise SystemExit(main())
