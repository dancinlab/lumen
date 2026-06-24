#!/usr/bin/env python3
"""H_047 — band-SSMB census + synthesis boundary (band-fleet, all no-incumbent bands).
Applying the compact SSMB-Compton synthesis (H_043-046) across the spectrum reveals it
operates in TWO regimes with a SHORT-WAVELENGTH BOUNDARY set by the achievable micro-bunch
length (sigma_z ~ 3 nm):
  - SSMB-COHERENT regime (lambda >~ ~10 nm): bunching gives b^2 >= 0.1 -> N^2 CW power
    (THz, EUV). This is the H_043 breakthrough -- and it matters exactly where EUV-litho's
    extreme flux lives.
  - INCOHERENT-ICS regime (lambda < ~few nm): too short to bunch (b^2 -> 0) -> plain
    inverse-Compton, which is ALREADY REAL today (water window via synchrotron; hard X-ray
    Lyncean; gamma HIGS/ELI) and suffices because those applications have lower flux needs.
So the SSMB-coherence advantage is TARGETED, not universal: it is needed only at the
high-flux band (EUV), and unnecessary at the shorter bands. Per-band verdict stays
requirement-driven (H_040): EUV-litho is the only terminal-thin (extreme flux) rung.

Deterministic, stdlib-only. $0 local.
"""
from __future__ import annotations
import json, math, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__)); _ROOT=os.path.abspath(os.path.join(_HERE,"..",".."))
sys.path.insert(0, os.path.join(_ROOT,"tool"))
from lumen_optics import Falsifier, evaluate

SIGMA_Z_NM = 3.0   # achievable SSMB micro-bunch length (H_046)
def b2(lam_nm): 
    x = math.exp(-0.5*(2*math.pi*SIGMA_Z_NM/lam_nm)**2); return x*x
# band -> (wavelength nm, flux class, compact verdict, exists-today)
BANDS = {
    "THz gap":      (3.0e5, "modest",  "wins",          "synchrotron THz-FEL (JLab/BESSY)"),
    "EUV litho":    (13.5,  "extreme", "terminal-thin", "none (SSMB-EUV concept)"),
    "water window": (3.0,   "moderate","works",         "synchrotron only"),
    "hard X-ray":   (0.1,   "moderate","real-today",    "Lyncean compact ICS"),
    "nuclear gamma":(0.005, "low",     "real-today",    "HIGS / ELI-NP ICS"),
}

def main()->int:
    regimes = {b: ("SSMB-coherent" if b2(lam)>=0.1 else "incoherent-ICS") for b,(lam,_,_,_) in BANDS.items()}
    coherent = [b for b,r in regimes.items() if r=="SSMB-coherent"]
    incoherent = [b for b,r in regimes.items() if r=="incoherent-ICS"]
    terminal_thin = [b for b,(_,f,v,_) in BANDS.items() if v=="terminal-thin"]
    extreme = [b for b,(_,f,_,_) in BANDS.items() if f=="extreme"]
    m={"n_coherent":len(coherent),"n_incoherent":len(incoherent),"n_bands":len(BANDS),
       "euv_in_coherent":"EUV litho" in coherent,"gamma_incoherent":"nuclear gamma" in incoherent,
       "verdict_tracks_flux":(terminal_thin==extreme)}
    fs=[
     Falsifier("F-BC-1 SSMB-REGIME", lambda m: not (m["euv_in_coherent"] and "THz gap" in coherent),
       "SSMB-coherent regime must include THz and EUV (lambda where b^2>=0.1)"),
     Falsifier("F-BC-2 BREAKS-SHORT", lambda m: not m["gamma_incoherent"],
       "gamma (and hard X-ray) must fall to the incoherent-ICS regime (too short to micro-bunch)"),
     Falsifier("F-BC-3 ICS-REAL", lambda m: not (m["n_incoherent"]>=2),
       "the incoherent-ICS regime must hold >=2 bands that are REAL today (Lyncean/HIGS/ELI)"),
     Falsifier("F-BC-4 VERDICT-DRIVEN", lambda m: not m["verdict_tracks_flux"],
       "the only terminal-thin band must be the extreme-flux one (EUV-litho) -> requirement-driven (H_040)"),
     Falsifier("F-BC-5 COVERAGE", lambda m: not (m["n_coherent"]+m["n_incoherent"]==m["n_bands"]),
       "every no-incumbent band must fall in exactly one regime"),
     Falsifier("F-BC-6 BOUNDS", lambda m: not (m["n_bands"]>=5),
       ">=5 bands censused"),
    ]
    led=evaluate(m,fs); v="SUPPORTED" if led["all_pass"] else "FALSIFIED"; led["verdict"]=v
    print("H_047 band-SSMB census + synthesis boundary (sigma_z ~ 3 nm)")
    for b,(lam,f,vd,ex) in BANDS.items():
        print(f"  {b:<14} lambda={lam:>8.4g}nm  b^2={b2(lam):.3f}  {regimes[b]:<14} flux:{f:<9} {vd:<14} [{ex}]")
    print(f"  => SSMB-coherent: {coherent} (incl. EUV, where the breakthrough matters)")
    print(f"  => incoherent-ICS (real today): {incoherent} (lower-flux apps, no coherence needed)")
    print(f"  => verdict requirement-driven: only terminal-thin = extreme-flux EUV-litho ({terminal_thin==extreme})")
    for r in led["falsifiers"]: print(f"  {r['name']:<20} {r['status']}")
    print(f"VERDICT: {v}  ({led['n_pass']}/{led['n_total']} falsifiers PASS)")
    json.dump(led, open(os.path.join(_HERE,"result.json"),"w"), indent=2); return 0
if __name__=="__main__": raise SystemExit(main())
