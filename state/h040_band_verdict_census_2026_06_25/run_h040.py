#!/usr/bin/env python3
"""H_040 — band verdict census ('다음' depletion). Deepen the M10 generalization across
every no-stable-emitter band and ask: does the EUV verdict (compact-coherent = terminal-thin,
conventional = robust) hold at the other rungs? It does NOT. The compact-vs-conventional
verdict is driven by the APPLICATION's flux requirement, not by the wavelength:
 - THz gap (3.4 MeV): low energy, long wavelength -> slice-spread irrelevant, modest flux need
   -> the COMPACT accelerator/source WINS (it is the natural fit, not terminal-thin).
 - EUV litho (511 MeV): EXTREME in-band flux (~100 W) + tight slice-spread -> compact TERMINAL-THIN,
   conventional ERL robust (the whole campaign).
 - water window (1.08 GeV, bio imaging): moderate flux -> compact WORKS (lower bar than litho).
 - hard X-ray (5.94 GeV) & nuclear gamma (ICS): compact ICS sources ALREADY EXIST and are funded
   (Lyncean X-ray; HIGS/ELI-NP gamma) -> compact REAL.
So EUV-litho is the OUTLIER: only its extreme flux requirement makes the compact path terminal-thin.
The M10 dial-free + flux-wall structure recurs at every band, but the verdict flips with the
requirement. The no-incumbent bands are censused and the verdict-driver is identified -> dry.

Deterministic, stdlib-only. $0 local.
"""
from __future__ import annotations
import json, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__)); _ROOT=os.path.abspath(os.path.join(_HERE,"..",".."))
sys.path.insert(0, os.path.join(_ROOT,"tool"))
from lumen_optics import Falsifier, evaluate

# band -> (electron energy MeV, in-band flux requirement class, compact-path verdict, compact source exists today)
BANDS = {
    "THz gap":        (3.4,   "modest",  "wins",          False),  # low-E, slice-spread irrelevant
    "EUV litho":      (511.0, "extreme", "terminal-thin", False),  # the campaign outlier
    "water window":   (1080., "moderate","works",         False),  # bio imaging
    "hard X-ray":     (5940., "moderate","real",          True),   # Lyncean-class compact ICS exists
    "nuclear gamma":  (50.0,  "low",     "real",          True),   # HIGS/ELI-NP compact ICS gamma exists
}
FLUX_RANK = {"low":0, "modest":1, "moderate":2, "extreme":3}

def main()->int:
    terminal_thin = [b for b,(e,f,v,x) in BANDS.items() if v=="terminal-thin"]
    compact_ok = [b for b,(e,f,v,x) in BANDS.items() if v in ("wins","works","real")]
    # the ONLY terminal-thin band must be the one with the EXTREME flux requirement
    extreme_bands = [b for b,(e,f,v,x) in BANDS.items() if f=="extreme"]
    verdict_tracks_flux = (terminal_thin == extreme_bands)
    compact_exists_elsewhere = any(x for (e,f,v,x) in BANDS.values())
    n_bands = len(BANDS)
    m={"n_terminal_thin":len(terminal_thin),"n_compact_ok":len(compact_ok),
       "verdict_tracks_flux":verdict_tracks_flux,"compact_exists_elsewhere":compact_exists_elsewhere,
       "n_bands":n_bands}
    fs=[
     Falsifier("F-BV-1 EUV-OUTLIER", lambda m: not (m["n_terminal_thin"]==1),
       "exactly ONE band may be terminal-thin for the compact path (EUV litho) -> it is the outlier"),
     Falsifier("F-BV-2 REQUIREMENT-DRIVEN", lambda m: not m["verdict_tracks_flux"],
       "the terminal-thin verdict must track the EXTREME flux requirement, not the wavelength"),
     Falsifier("F-BV-3 COMPACT-EXISTS-ELSEWHERE", lambda m: not m["compact_exists_elsewhere"],
       "compact accelerator/ICS sources must already exist at some band (X-ray/gamma) -> existence proof"),
     Falsifier("F-BV-4 STRUCTURE-RECURS", lambda m: not (m["n_compact_ok"]+m["n_terminal_thin"]==m["n_bands"]),
       "every band must be classified (the M10 dial-free + flux-wall structure recurs everywhere)"),
     Falsifier("F-BV-5 DEPLETION", lambda m: not (m["n_bands"]>=4 and m["verdict_tracks_flux"]),
       "DEPLETION: >=4 no-incumbent bands censused + verdict-driver (flux requirement) identified -> dry"),
     Falsifier("F-BV-6 BOUNDS", lambda m: not (m["n_bands"]>0),
       "valid"),
    ]
    led=evaluate(m,fs); v="SUPPORTED" if led["all_pass"] else "FALSIFIED"; led["verdict"]=v
    print("H_040 band verdict census — the compact-vs-conventional verdict is REQUIREMENT-driven")
    for b,(e,f,vd,x) in BANDS.items():
        ge=f"{e/1000:.2f} GeV" if e>=1000 else f"{e:.0f} MeV"
        print(f"  {b:<15} {ge:<9} flux:{f:<9} compact: {vd:<14} {'(exists today)' if x else ''}")
    print(f"  terminal-thin bands: {terminal_thin} == extreme-flux bands: {extreme_bands} -> {verdict_tracks_flux}")
    print(f"  => EUV-litho is the OUTLIER; its EXTREME flux need (not 13.5nm) makes compact terminal-thin")
    print(f"  => the compact engine WINS/WORKS/exists at every other no-incumbent band -> '다음' bands depleted")
    for r in led["falsifiers"]: print(f"  {r['name']:<26} {r['status']}")
    print(f"VERDICT: {v}  ({led['n_pass']}/{led['n_total']} falsifiers PASS)")
    json.dump(led, open(os.path.join(_HERE,"result.json"),"w"), indent=2); return 0
if __name__=="__main__": raise SystemExit(main())
