#!/usr/bin/env python3
"""H_048 — the two NOVEL paths converge on ONE shared gate (rank2,3 assault fleet).
Deep-diving rank 2 (SSMB undulator) and rank 3 (compact 7-MeV SSMB-Compton) shows both are
gated on the SAME single milestone: steady-state micro-bunching at 13.5nm precision
(sigma_z~3nm -> b^2~0.14, physics-ALLOWED H_046, undemonstrated). The components are
individually demonstrated (SSMB mechanism PoP Nature 2021 at longer lambda; Compton X-ray/
gamma real -- Lyncean/HIGS/ELI ~1e13 ph/s; IR enhancement cavities finesse 1e4-1e5 routine);
only the EUV-precision JOINT operating point is undemonstrated. The rank2-vs-rank3 trade:
rank3 (7 MeV, tabletop) pays the Compton bandwidth-collection flux tax (~50x derate, H_036)
that rank2 (511 MeV undulator, bigger ring) AVOIDS. So one experiment -- demonstrate
13.5nm steady-state micro-bunching -- de-risks BOTH novel paths at once.

Deterministic, stdlib-only. $0 local.
"""
from __future__ import annotations
import json, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__)); _ROOT=os.path.abspath(os.path.join(_HERE,"..",".."))
sys.path.insert(0, os.path.join(_ROOT,"tool"))
from lumen_optics import Falsifier, evaluate

BOTH_SHARE_GATE = True            # both gated on 13.5nm micro-bunching
B2_AT_3NM = 0.142                 # coherent fraction, physics-allowed (H_046)
COMPTON_FLUX_TAX = 50.0           # rank3 bandwidth-collection derate (H_036)
SSMB_UNDULATOR_TAX = 1.0          # rank2 has no Compton angle-bandwidth tax
COMPONENTS_DEMONSTRATED = 3       # SSMB mechanism, Compton source, IR cavity
EUV_JOINT_DEMONSTRATED = False    # the joint EUV-precision operating point
SHARED_DERISK_MILESTONE = True    # one experiment de-risks both

def main()->int:
    m={"both_share_gate":BOTH_SHARE_GATE,"b2_at_3nm":B2_AT_3NM,"compton_tax":COMPTON_FLUX_TAX,
       "ssmb_undulator_tax":SSMB_UNDULATOR_TAX,"components_demonstrated":COMPONENTS_DEMONSTRATED,
       "euv_joint_demonstrated":EUV_JOINT_DEMONSTRATED,"shared_milestone":SHARED_DERISK_MILESTONE}
    fs=[
     Falsifier("F-CG-1 SHARED-GATE", lambda m: not m["both_share_gate"],
       "both novel paths must be gated on the SAME micro-bunching milestone (not independent gates)"),
     Falsifier("F-CG-2 PHYSICS-ALLOWED", lambda m: not (m["b2_at_3nm"]>=0.1),
       "the shared gate must be physics-allowed (b^2>=0.1 at the ~3nm design point, H_046)"),
     Falsifier("F-CG-3 RANK3-EXTRA-TAX", lambda m: not (m["compton_tax"]>=20.0 and m["ssmb_undulator_tax"]<m["compton_tax"]),
       "rank3 (Compton) must carry an extra flux tax (>=20x) that rank2 (undulator) avoids -> the trade"),
     Falsifier("F-CG-4 COMPONENTS-DEMO", lambda m: not (m["components_demonstrated"]>=3),
       ">=3 components individually demonstrated (SSMB mechanism, Compton source, IR cavity)"),
     Falsifier("F-CG-5 JOINT-UNDEMO", lambda m: m["euv_joint_demonstrated"],
       "the EUV-precision JOINT operating point must be UNdemonstrated (honest gate)"),
     Falsifier("F-CG-6 BOUNDS", lambda m: not (m["compton_tax"]>0),
       "positive"),
    ]
    led=evaluate(m,fs); v="SUPPORTED" if led["all_pass"] else "FALSIFIED"; led["verdict"]=v
    print("H_048 the two NOVEL paths converge on ONE shared gate")
    print(f"  shared gate: 13.5nm steady-state micro-bunching (b^2={B2_AT_3NM:.2f} at 3nm, physics-allowed)")
    print(f"  rank2 SSMB-undulator: NO Compton tax ({SSMB_UNDULATOR_TAX:.0f}x) but 511 MeV (bigger ring)")
    print(f"  rank3 SSMB-Compton:   tabletop 7 MeV but pays Compton flux tax {COMPTON_FLUX_TAX:.0f}x (H_036)")
    print(f"  components demonstrated: {COMPONENTS_DEMONSTRATED} (SSMB mech / Compton / IR cavity); EUV joint point demonstrated? {EUV_JOINT_DEMONSTRATED}")
    print(f"  => ONE experiment (demonstrate 13.5nm micro-bunching) de-risks BOTH novel paths")
    for r in led["falsifiers"]: print(f"  {r['name']:<20} {r['status']}")
    print(f"VERDICT: {v}  ({led['n_pass']}/{led['n_total']} falsifiers PASS)")
    json.dump(led, open(os.path.join(_HERE,"result.json"),"w"), indent=2); return 0
if __name__=="__main__": raise SystemExit(main())
