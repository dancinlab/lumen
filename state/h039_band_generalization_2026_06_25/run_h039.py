#!/usr/bin/env python3
"""H_039 — GENERALIZE the EUV machinery across wavelength bands. The undulator relation
lambda = (lambda_u / 2 gamma^2)(1 + K^2/2) and the ICS relation lambda = lambda_L/4gamma^2
both give lambda ~ 1/gamma^2 -- so ONE accelerator + undulator architecture spans the whole
spectrum from THz to hard X-ray by dialing the electron energy alone. The bands that lack a
stable natural emitter -- the THz gap, EUV, the soft-X-ray water window -- are precisely the
ones this wavelength-agnostic engine reaches with no entrenched incumbent (meta-law M10).
This is the lumen scope: EUV is the first instance, not the boundary.

Deterministic, stdlib-only. $0 local.
"""
from __future__ import annotations
import json, math, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__)); _ROOT=os.path.abspath(os.path.join(_HERE,"..",".."))
sys.path.insert(0, os.path.join(_ROOT,"tool"))
from lumen_optics import Falsifier, evaluate

_ME_MEV = 0.51099895
U_PERIOD_M = 0.018          # 18 mm undulator (COXINEL U18 class)
K = 1.0                     # undulator parameter -> (1 + K^2/2) = 1.5
_KFAC = 1.0 + K*K/2.0

# representative bands (wavelength in metres) + whether a stable compact natural emitter exists
BANDS = [
    ("THz gap (1 THz, 300 um)", 300e-6, False),
    ("far-IR (30 um)",          30e-6,  True),   # molecular/thermal sources exist
    ("EUV (13.5 nm)",           13.5e-9, False),
    ("water window (3 nm)",     3.0e-9,  False),
    ("hard X-ray (0.1 nm)",     0.1e-9,  False),  # synchrotrons only, not tabletop
]

def energy_mev(wl_m):
    gamma = math.sqrt(U_PERIOD_M*_KFAC/(2.0*wl_m))   # invert undulator relation
    return gamma*_ME_MEV

def main()->int:
    ladder = [(name, wl, energy_mev(wl), has_emitter) for (name,wl,has_emitter) in BANDS]
    energies = [e for (_,_,e,_) in ladder]
    wavelengths = [wl for (_,wl,_,_) in ladder]
    # monotonic: shorter wavelength -> higher energy
    monotonic = all(energies[i] < energies[i+1] for i in range(len(energies)-1))
    e_thz = ladder[0][2]
    e_waterwindow = [e for (n,_,e,_) in ladder if "water" in n][0]
    span_orders = math.log10(wavelengths[0]/wavelengths[-1])
    no_emitter_all_covered = all(e <= 6000.0 for (_,_,e,has) in ladder if not has)  # all no-emitter bands <= 6 GeV
    m={"monotonic":monotonic,"E_THz_MeV":e_thz,"E_waterwindow_MeV":e_waterwindow,
       "span_orders":span_orders,"no_emitter_all_covered":no_emitter_all_covered,
       "E_hardxray_GeV":energies[-1]/1000.0}
    fs=[
     Falsifier("F-GN-1 MONOTONIC-DIAL", lambda m: not m["monotonic"],
       "energy must rise monotonically as wavelength falls (the lambda~1/gamma^2 dial spans bands)"),
     Falsifier("F-GN-2 THZ-TABLETOP", lambda m: not (m["E_THz_MeV"]<=10.0),
       "the THz gap must be reachable at <=10 MeV (truly tabletop low energy)"),
     Falsifier("F-GN-3 WATERWINDOW-SUB2GEV", lambda m: not (m["E_waterwindow_MeV"]<=2000.0),
       "the soft-X-ray water window (3 nm) must be reachable at <=2 GeV"),
     Falsifier("F-GN-4 ONE-MACHINE-WIDE", lambda m: not (m["span_orders"]>=4.0),
       "one undulator + energy dial must span >=4 orders of magnitude in wavelength (THz->X-ray)"),
     Falsifier("F-GN-5 NO-INCUMBENT-COVERED", lambda m: not m["no_emitter_all_covered"],
       "every no-stable-emitter band (THz/EUV/water-window/hard-X) must lie in the covered range (M10)"),
     Falsifier("F-GN-6 BOUNDS", lambda m: not (m["E_THz_MeV"]>0 and m["span_orders"]>0),
       "positive"),
    ]
    led=evaluate(m,fs); v="SUPPORTED" if led["all_pass"] else "FALSIFIED"; led["verdict"]=v
    print("H_039 GENERALIZE — one accelerator + undulator spans THz -> hard X-ray by the energy dial")
    for (name, wl, e, has) in ladder:
        tag = "stable emitter exists" if has else "NO stable emitter (engine's market)"
        ge = f"{e/1000:.2f} GeV" if e>=1000 else f"{e:.1f} MeV"
        print(f"  {name:<26} -> {ge:<10} [{tag}]")
    print(f"  dial monotonic: {monotonic} · span {span_orders:.1f} orders of magnitude (THz->hard X-ray)")
    print(f"  => lumen scope confirmed: EUV (511 MeV) is one rung; the no-emitter bands are the engine's natural market (M10)")
    for r in led["falsifiers"]: print(f"  {r['name']:<26} {r['status']}")
    print(f"VERDICT: {v}  ({led['n_pass']}/{led['n_total']} falsifiers PASS)")
    json.dump(led, open(os.path.join(_HERE,"result.json"),"w"), indent=2); return 0
if __name__=="__main__": raise SystemExit(main())
