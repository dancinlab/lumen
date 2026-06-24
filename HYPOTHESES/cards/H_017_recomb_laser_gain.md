---
id: H_017
slug: recomb-laser-gain
title: Recombination EUV laser saturation requirement — reference-matched to the demonstrated 46.9 nm Ar capillary laser (gL~14), a plasma waveguide makes the saturation length reachable at a modest required gain (~1 cm⁻¹), so the binding open frontier is the 13.5 nm gain, not the geometry — promotes abstract H_B4
domain: light-source
status: supported
exploration_method: gain-length product reference-match (46.9 nm Ar anchor)
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
promoted_from: H_B4
---

# H_017 — recombination EUV laser saturation requirement

> **Promotion of 🜂 H_B4** runnable core. Verifies the geometry/requirement; the 13.5 nm gain itself stays an honest open frontier (not claimed).

## Hypothesis

A saturated soft-X-ray/EUV laser needs gain-length product gL ≳ 14. The demonstrated 46.9 nm
Ne-like Ar capillary-discharge laser reaches gL ~14 (gain ~1 cm⁻¹ over ~14 cm). A plasma waveguide
extends the usable length far past the unguided Rayleigh range (~140×), so at 13.5 nm the *required*
gain to saturate over a guided 14 cm is a modest ~1 cm⁻¹ — meaning the geometry is reachable and the
binding open question is whether a 13.5 nm plasma can deliver that gain, not the optics.

## Variables (pre-registered)
- gL saturation 14 · 46.9 nm anchor (g=1 cm⁻¹, L=14 cm) · Rayleigh 0.1 cm · guided length 14 cm.

## Run Protocol
- harness: `tool/lumen_optics.gain_length_product` · run: `state/h017_recomb_laser_gain_2026_06_25/run_h017.py`
- `python3 .../run_h017.py` · artifacts `.../result.json`.

## Falsifiers
- **F-XRL-1 REFERENCE**: 46.9 nm anchor gL < 14 → reference-match broken.
- **F-XRL-2 WAVEGUIDE**: waveguide length gain ≤ 10× → guiding doesn't help.
- **F-XRL-3 REQUIREMENT**: required 13.5 nm gain ∉ (0, 5] cm⁻¹ → geometry IS the wall.
- **F-XRL-4 UNGUIDED-FAIL**: unguided gL ≥ 14 → no need for a waveguide.
- **F-XRL-5 BOUNDS**: any non-positive → ledger bug.

## Honest Limits
- **L1 (13.5 nm gain unverified — the frontier)**: this proves the geometry + required gain; whether
  a 13.5 nm recombination/Ni-like plasma actually delivers g ≥ 1 cm⁻¹ is the open experimental
  question — shorter λ generally has lower gain (higher Z, harder inversion). NOT claimed here.
- **L2 (gL~14 rule-of-thumb)**: the saturation threshold is approximate (scheme-dependent).
- **L3 (single-pass ASE)**: ignores cavity/seeding that could lower the gL bar (e.g. HHG-seeded amplifier, H_B4 variant).
- **L4 (rep-rate not addressed)**: H_B4's HVM claim also needs ≥10 kHz re-inversion + thermal recovery — a separate wall (cf. H_016/H_018 thermal).

## Cross-Links
- promotes: H_B4. reference-match: 46.9 nm Ar capillary laser. source-side escape vs H_008 flux wall (meta-law M2/E2).

## Verdict
```
verdict_class: SUPPORTED
evidence_summary: gL reference-match + waveguide requirement, 5/5 falsifiers PASS.
  reference 46.9 nm Ar gL = 14.0 (saturated)
  waveguide extends length 140x over Rayleigh
  13.5 nm required gain for saturation over 14 cm = 1.00 cm^-1
key_finding: the recombination-EUV-laser GEOMETRY is reachable — a plasma waveguide makes
             gL>=14 attainable at a modest ~1 cm^-1 gain (reference-matched to the 46.9 nm Ar
             laser). The binding open frontier is the 13.5 nm gain itself, not the optics.
honest_note: 13.5 nm gain unverified, the real frontier (L1); gL~14 approximate (L2); seeding
             could lower the bar (L3); rep-rate/thermal is a separate wall (L4).
```

### Run verdict (VERBATIM — 2026-06-25)
```
H_017 recombination EUV laser saturation requirement (promotes H_B4)
  reference 46.9 nm Ar: gL = 14.0 (>= 14 saturated)
  waveguide extends length 140x over Rayleigh (0.1 cm)
  13.5 nm: required gain for saturation over 14 cm = 1.00 cm^-1
  -> geometry is reachable; the 13.5 nm GAIN itself is the open frontier (honest limit)
  F-XRL-1 REFERENCE  PASS
  F-XRL-2 WAVEGUIDE  PASS
  F-XRL-3 REQUIREMENT PASS
  F-XRL-4 UNGUIDED-FAIL PASS
  F-XRL-5 BOUNDS     PASS
VERDICT: SUPPORTED  (5/5 falsifiers PASS)
```
**State output**: `state/h017_recomb_laser_gain_2026_06_25/result.json`
