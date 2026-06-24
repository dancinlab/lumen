---
id: H_030
slug: funded-reality-refmatch
title: Funded-reality reference-match — the accelerator-driven FEL EUV direction is real and FUNDED (xLight, KEK), validating lumen's direction, but three honest corrections land — the funded driver is a conventional ERL not the tabletop LPA, the funded economic lever is M9-amortization not the M7 module-array, and 13.5 nm-on-LPA + single-pass cooling are undemonstrated; the concept predates lumen (Nakajima 2014) so the synthesis is not novel
domain: system
status: supported
exploration_method: fleet prior-art + accel lanes (reference-match to published/funded reality)
verification_method: deterministic harness + 6 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
corrects: H_021 (M7 emphasis), H_028 (cooling lens), H_022 (LPA-driver emphasis)
---
# H_030 — funded-reality reference-match (the campaign's strongest honesty check)
> commons reference-match: the thesis's reference (the real funded EUV-accelerator landscape) is OPEN — so look at the answer key. The fleet did, and it both validates and corrects the campaign.
## Findings (all sourced, fleet prior-art/accel/econ)
- **Direction validated:** accelerator-driven FEL EUV is a real funded program — xLight ($40M Series-B + ≤$150M CHIPS LOI, 2028 prototype, one source→~20 scanners) and KEK (10 kW ERL EUV-FEL). The campaign was not chasing a fantasy.
- **Correction 1 (driver):** both funded programs use a **conventional ERL/SC-linac**, not a tabletop LPA — lumen's LPA-driver emphasis is the less-mature, less-funded variant.
- **Correction 2 (economics):** the funded lever is **M9-amortization** (one big source spread across ~20 scanners), NOT the **M7 module-array learning curve** H_021 leaned on.
- **Correction 3 (wavelength + cooling):** LPA-FEL has lased only to ~25–27 nm (Wang, Nature 2021), **never 13.5 nm**; single-pass LPA cooling to <0.5% is undemonstrated (OSC is storage-ring only) → **H_028's cooling lens is aspirational**.
- **Novelty:** the LPA-EUV-FEL concept was fully designed by Nakajima (HPLSE 2014) → lumen's synthesis is **not novel**, a >10-yr published direction.
## Falsifiers
F-PA-1 ≥2 funded programs (direction real) · F-PA-2 funded driver is conventional ERL not LPA · F-PA-3 funded leg is M9-amortization not M7 · F-PA-4 LPA-FEL floor >13.5 nm · F-PA-5 concept predates lumen · F-PA-6 single-pass cooling undemonstrated.
## Honest Limits
L1 a funded program ≠ a working tool — xLight's 2028 prototype may slip or fail (the direction's validation is of *intent+capital*, not success); L2 "less-mature variant" is not "wrong" — the LPA driver may still win long-horizon on footprint; the correction is about *revealed industry preference today*; L3 magnitudes (~20 scanners/source, $40M) are public-press order.
## Verdict
```
verdict_class: SUPPORTED  (6/6)
funded programs 2 (xLight,KEK) · driver=conventional-ERL · econ-leg=M9-amortization · LPA floor 25>13.5nm · concept 2014<2026 · single-pass cooling=undemonstrated
key_finding: lumen's DIRECTION (accelerator-driven FEL beats LPP) is validated by real industry money,
             but its specific tabletop-LPA + M7-module-array + cooling form is the less-mature variant of
             an already-funded idea — the industry's revealed bet is a conventional ERL amortized across
             many scanners (M9). The robust restatement of the answer is xLight-shaped, not tabletop-shaped.
honest_note: funded != working (L1); less-mature != wrong, LPA may still win long-horizon on footprint
             (L2); public-press magnitudes (L3). This is the campaign's most important honest correction.
```
**State output**: `state/h030_funded_reality_refmatch_2026_06_25/result.json`
