---
id: H_040
slug: band-verdict-census
title: Band verdict census — the EUV 'compact terminal-thin / conventional robust' verdict does NOT generalize; it is driven by the application's flux requirement, not the wavelength — EUV litho (extreme ~100 W in-band) is the outlier, while the compact accelerator/ICS engine WINS at the THz gap (low energy, slice-spread irrelevant), WORKS at the water window, and ALREADY EXISTS at hard X-ray (Lyncean) and nuclear gamma (HIGS/ELI-NP); the M10 dial-free + flux-wall structure recurs at every rung but the verdict flips with the requirement, so the no-incumbent bands are censused and the 'next' is depleted
domain: system
status: supported
exploration_method: deepen M10 across every no-incumbent band ('다음' depletion)
verification_method: deterministic harness + 6 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
refines: H_038 (terminal-thin was EUV-litho-specific) · H_039/M10
---
# H_040 — band verdict census: the verdict is requirement-driven
> Deepen the M10 generalization across the rest of the engine's market and test whether the EUV verdict transfers. It does not.
## The census
THz gap (3.4 MeV, modest flux) → compact **WINS** · EUV litho (511 MeV, **extreme** flux) → compact **terminal-thin** · water window (1.08 GeV, moderate) → compact **WORKS** · hard X-ray (5.94 GeV) → compact ICS **REAL today** (Lyncean) · nuclear gamma (ICS) → **REAL today** (HIGS/ELI-NP).
## The honest insight
The terminal-thin verdict **tracks the extreme flux requirement, not the wavelength**. EUV litho is the *outlier* — its ~100 W in-band demand + tight slice-spread are what make the compact path terminal-thin (H_031–038). At every other no-incumbent band the wavelength-agnostic engine **wins, works, or already exists**. So lumen's earlier "compact = terminal-thin" was EUV-litho-specific, not a property of the engine.
## Falsifiers
F-BV-1 exactly one terminal-thin band (EUV outlier) · F-BV-2 verdict tracks flux not wavelength · F-BV-3 compact exists at some band (existence proof) · F-BV-4 every band classified (structure recurs) · F-BV-5 ≥4 bands + driver → depletion · F-BV-6 bounds.
## Honest Limits
L1 "flux requirement class" is coarse (modest/moderate/extreme) — a real per-application dose/throughput model would refine the boundary, but EUV-litho's extreme bar is uncontested; L2 "exists today" for X-ray/gamma ICS means demonstrated sources at *their* (lower) average-power needs, not at litho power — the existence proof is of the compact *architecture*, not of litho-grade flux; L3 the census is the no-incumbent supply bands (M10/H_025 taxonomy), not every conceivable application.
## Verdict
```
verdict_class: SUPPORTED  (6/6)
1 terminal-thin band (EUV) == the 1 extreme-flux band · compact WINS/WORKS/exists at THz/water-window/X-ray/gamma · structure recurs
key_finding: the EUV 'compact terminal-thin' verdict does NOT generalize — it is driven by litho's EXTREME
             flux requirement, not by 13.5 nm. The wavelength-agnostic engine wins at the THz gap, works at
             the water window, and already exists at hard X-ray and nuclear gamma. EUV litho is the single
             most-demanding rung; '다음' (other bands) is depleted, the verdict-driver identified.
honest_note: coarse flux classes (L1); 'exists' = compact architecture at lower-flux needs, not litho power
             (L2); no-incumbent supply taxonomy not every application (L3).
```
**State output**: `state/h040_band_verdict_census_2026_06_25/result.json`
