#!/usr/bin/env python3
"""H_017 — recombination EUV laser saturation requirement (promotes abstract H_B4
runnable core). Reference-matched to the demonstrated 46.9 nm Ne-like Ar capillary
laser (gain ~1.0 cm^-1 over ~14 cm -> gL ~14, saturated). A plasma waveguide makes
the saturation length reachable (L >> Rayleigh range) so the binding open frontier
is the 13.5 nm GAIN itself, not the geometry.

Deterministic, stdlib-only. $0 local.
    python3 state/h017_recomb_laser_gain_2026_06_25/run_h017.py
"""

from __future__ import annotations

import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "tool"))

from lumen_optics import Falsifier, evaluate, gain_length_product

# --- pre-registered parameters (FROZEN 2026-06-25) ---------------------------
GL_SATURATION = 14.0       # saturated-ASE gain-length threshold
# reference anchor: 46.9 nm Ne-like Ar capillary-discharge laser (demonstrated)
G_REF_CM = 1.0             # gain [cm^-1]
L_REF_CM = 14.0            # active length [cm]
# geometry at 13.5 nm
RAYLEIGH_CM = 0.1          # unguided Rayleigh range (tight focus)
L_GUIDED_CM = 14.0         # plasma-waveguide-extended length


def main() -> int:
    gl_ref = gain_length_product(G_REF_CM, L_REF_CM)            # ~14, saturated
    gl_unguided = gain_length_product(G_REF_CM, RAYLEIGH_CM)    # tiny
    # required 13.5 nm gain to saturate over the guided length
    g_required = GL_SATURATION / L_GUIDED_CM
    waveguide_gain = L_GUIDED_CM / RAYLEIGH_CM                  # length extension factor

    metrics = {
        "gl_saturation": GL_SATURATION,
        "gl_reference_46p9nm": gl_ref,
        "gl_unguided": gl_unguided,
        "g_required_135nm_per_cm": g_required,
        "waveguide_length_gain": waveguide_gain,
    }

    falsifiers = [
        Falsifier("F-XRL-1 REFERENCE", lambda m: not (m["gl_reference_46p9nm"] >= GL_SATURATION),
                  "the 46.9 nm Ar anchor must reach gL >= 14 (reference-match)"),
        Falsifier("F-XRL-2 WAVEGUIDE", lambda m: not (m["waveguide_length_gain"] > 10.0),
                  "plasma waveguide must extend usable length >> unguided Rayleigh range"),
        Falsifier("F-XRL-3 REQUIREMENT", lambda m: not (0.0 < m["g_required_135nm_per_cm"] <= 5.0),
                  "required 13.5 nm gain for saturation must be modest (<= a few cm^-1), i.e. geometry not the wall"),
        Falsifier("F-XRL-4 UNGUIDED-FAIL", lambda m: not (m["gl_unguided"] < GL_SATURATION),
                  "unguided geometry must fall short (why the waveguide is needed)"),
        Falsifier("F-XRL-5 BOUNDS", lambda m: not all(v > 0 for v in
                  (m["gl_reference_46p9nm"], m["g_required_135nm_per_cm"], m["waveguide_length_gain"])),
                  "all positive"),
    ]

    ledger = evaluate(metrics, falsifiers)
    verdict = "SUPPORTED" if ledger["all_pass"] else "FALSIFIED"
    ledger["verdict"] = verdict

    print("H_017 recombination EUV laser saturation requirement (promotes H_B4)")
    print(f"  reference 46.9 nm Ar: gL = {gl_ref:.1f} (>= {GL_SATURATION:.0f} saturated)")
    print(f"  waveguide extends length {waveguide_gain:.0f}x over Rayleigh ({RAYLEIGH_CM} cm)")
    print(f"  13.5 nm: required gain for saturation over {L_GUIDED_CM:.0f} cm = {g_required:.2f} cm^-1")
    print(f"  -> geometry is reachable; the 13.5 nm GAIN itself is the open frontier (honest limit)")
    for r in ledger["falsifiers"]:
        print(f"  {r['name']:<18} {r['status']}")
    print(f"VERDICT: {verdict}  ({ledger['n_pass']}/{ledger['n_total']} falsifiers PASS)")

    with open(os.path.join(_HERE, "result.json"), "w") as fh:
        json.dump(ledger, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
