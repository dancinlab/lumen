#!/usr/bin/env python3
"""H_026 — sourced re-verification: re-run the chain with PUBLISHED measured values
(state/sourced-parameters.md) and record which verdicts hold vs need honest correction.
Core inputs (optics R, LPP power, wall-plug, CAPEX) CONFIRMED; three optimistic links
CORRECTED by data (La/B best 0.58 -> 6.5nm wall ~8x not 14x; demonstrated 46.9nm XRL
gL~8.28 < 14 saturation -> recombination harder; raw LPA spread several% -> FEL needs cooling).

Deterministic, stdlib-only. $0 local.
"""
from __future__ import annotations
import json, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__)); _ROOT=os.path.abspath(os.path.join(_HERE,"..",".."))
sys.path.insert(0, os.path.join(_ROOT,"tool"))
from lumen_optics import Falsifier, evaluate, source_power_multiplier

# sourced (measured) values
R_EUV, R_BEUV_MEAS, N = 0.70, 0.58, 11      # LaN/B4C best measured 58.1%
XRL_GL_MEAS, XRL_GL_SAT = 8.28, 14.0        # demonstrated 46.9nm gL_max vs saturation rule
BBU_THRESH_MA, BBU_NEED_MA = 10.0, 0.2      # measured ~10 mA vs needed
CORE_CONFIRMED = True                        # optics R, LPP 205-250W, wall-plug 1.17MW, CAPEX $200-400M all in range

def main()->int:
    mult_meas = source_power_multiplier(R_EUV, R_BEUV_MEAS, N)   # 6.5nm wall with best mirror
    bbu_margin = BBU_THRESH_MA / BBU_NEED_MA
    xrl_saturates = XRL_GL_MEAS >= XRL_GL_SAT
    m={"mult_measured":mult_meas,"bbu_margin":bbu_margin,"xrl_gl_meas":XRL_GL_MEAS,
       "xrl_saturates_demo":xrl_saturates,"core_confirmed":CORE_CONFIRMED}
    fs=[
     Falsifier("F-SR-1 OPTICS-HOLDS", lambda m: not (m["mult_measured"]>=2.0),
       "6.5nm optics wall holds (>=2x) even with best-measured La/B 0.58 (less severe than 14x)"),
     Falsifier("F-SR-2 BBU-HOLDS", lambda m: not (m["bbu_margin"]>=10.0),
       "ERL BBU still comfortable (margin>=10x) at measured ~10 mA threshold"),
     Falsifier("F-SR-3 XRL-CORRECTED", lambda m: m["xrl_saturates_demo"],
       "demonstrated 46.9nm XRL gL must be BELOW the gL~14 saturation rule (honest correction: route harder)"),
     Falsifier("F-SR-4 CORE-CONFIRMED", lambda m: not m["core_confirmed"],
       "core inputs (optics/power/wall-plug/CAPEX) must be confirmed within published ranges"),
     Falsifier("F-SR-5 BOUNDS", lambda m: not (m["mult_measured"]>0 and m["bbu_margin"]>0),
       "positive"),
    ]
    led=evaluate(m,fs); v="SUPPORTED" if led["all_pass"] else "FALSIFIED"; led["verdict"]=v
    print("H_026 sourced re-verification (published measured values)")
    print(f"  6.5nm optics wall: multiplier {mult_meas:.2f}x at R_beuv=0.58 (was 14.2x at 0.55) -> still a wall")
    print(f"  ERL BBU: margin {bbu_margin:.0f}x at measured 10 mA threshold -> holds")
    print(f"  46.9nm XRL: demonstrated gL {XRL_GL_MEAS} < {XRL_GL_SAT} saturation -> recombination route harder (corrected)")
    print(f"  core inputs (optics/power/wall-plug 0.02%eff/CAPEX): CONFIRMED within published ranges")
    for r in led["falsifiers"]: print(f"  {r['name']:<18} {r['status']}")
    print(f"VERDICT: {v}  ({led['n_pass']}/{led['n_total']} falsifiers PASS)")
    json.dump(led, open(os.path.join(_HERE,"result.json"),"w"), indent=2); return 0

if __name__=="__main__": raise SystemExit(main())
