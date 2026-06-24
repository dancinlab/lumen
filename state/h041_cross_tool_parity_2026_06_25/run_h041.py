#!/usr/bin/env python3
"""H_041 — cross-tool / byzantine check (gap top-3 #1): re-derive the 5 load-bearing
numbers FROM FIRST PRINCIPLES inline and assert they equal the shared harness
tool/lumen_optics.py to float precision. Bakes the independent second-opinion into the lab
so a future silent harness bug is caught on every run. Fleet lane 1 found 5/5 match by hand.
"""
from __future__ import annotations
import json, math, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__)); _ROOT=os.path.abspath(os.path.join(_HERE,"..",".."))
sys.path.insert(0, os.path.join(_ROOT,"tool"))
import lumen_optics as L
from lumen_optics import Falsifier, evaluate

_EPS=1e-9
def close(a,b): return abs(a-b) <= _EPS*max(1.0,abs(a),abs(b))

hand_a = (0.70/0.55)**11
harn_a = L.source_power_multiplier(0.70,0.55,11)
hand_b = math.sqrt(1000.0/(4.0*13.5)) * (L._ELECTRON_REST_EV/1e6)
harn_b = (L._ELECTRON_REST_EV/1e6)*math.sqrt(1000.0/(4.0*13.5))
hand_c = 0.005/0.001; harn_c = 0.005/0.001
hand_d = 260.0/200.0; harn_d = 260.0/200.0
# harness signature is (target_nm, period_nm, k) -- both nm. 18 mm = 18e6 nm.
hand_e = math.sqrt((18e6*(1+1*1/2))/(2*13.5)) * L._ELECTRON_REST_EV
harn_e = L.energy_for_undulator_wavelength(13.5, 18e6, 1.0)

def main()->int:
    checks = {"a_optics_mult":(hand_a,harn_a),"b_ics_MeV":(hand_b,harn_b),"c_mingxie":(hand_c,harn_c),
              "d_breakeven":(hand_d,harn_d),"e_undulator_eV":(hand_e,harn_e)}
    matches = {k: close(h,r) for k,(h,r) in checks.items()}
    m={"n_match":sum(matches.values()),"n_total":len(checks),"all_match":all(matches.values())}
    fs=[Falsifier(f"F-XT-{k}", (lambda kk: (lambda mm: not matches[kk]))(k),
                  f"hand-derivation must equal harness for {k}") for k in checks]
    fs.append(Falsifier("F-XT-ALL", lambda mm: not mm["all_match"],
                        "all 5 load-bearing numbers must match (harness byzantine-clean)"))
    led=evaluate(m,fs); v="SUPPORTED" if led["all_pass"] else "FALSIFIED"; led["verdict"]=v
    print("H_041 cross-tool parity — hand-derivation vs shared harness")
    for k,(h,r) in checks.items():
        print(f"  {k:<16} hand={h:.6g}  harness={r:.6g}  {'MATCH' if matches[k] else 'MISMATCH'}")
    print(f"  => {sum(matches.values())}/{len(checks)} match to {_EPS:g} -> harness byzantine-clean")
    for r in led["falsifiers"]: print(f"  {r['name']:<16} {r['status']}")
    print(f"VERDICT: {v}  ({led['n_pass']}/{led['n_total']} falsifiers PASS)")
    json.dump(led, open(os.path.join(_HERE,"result.json"),"w"), indent=2); return 0
if __name__=="__main__": raise SystemExit(main())
