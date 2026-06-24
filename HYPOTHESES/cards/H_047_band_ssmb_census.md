---
id: H_047
slug: band-ssmb-census
title: Band-SSMB census + synthesis boundary — applying the compact SSMB-Compton synthesis across every no-incumbent band reveals two regimes split by the achievable micro-bunch length (σ_z ~ 3 nm); the SSMB-coherent (N² CW) regime covers λ ≳ ~10 nm (THz b²=1.0, EUV b²=0.14) — exactly where EUV-litho's extreme flux lives — while the shorter bands (water window, hard X-ray, gamma; b²→0, too short to micro-bunch) fall to plain incoherent inverse-Compton, which is ALREADY REAL today (synchrotron / Lyncean / HIGS / ELI-NP) and suffices because those applications have lower flux needs; the per-band verdict stays requirement-driven (H_040) with EUV-litho the only terminal-thin (extreme-flux) rung
domain: system
status: supported
exploration_method: band-fleet — apply the SSMB-Compton synthesis to all no-incumbent bands
verification_method: deterministic harness + 6 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
generalizes: H_043-046 (SSMB-Compton) across H_040/M10 bands
---
# H_047 — the SSMB-coherence advantage is targeted, not universal
> Apply the compact SSMB-Compton synthesis (H_043-046) to every no-incumbent band. Where does the coherence help, and where does it break?
## Two regimes (σ_z ~ 3 nm achievable bunch length)
| band | λ | b² | regime | verdict | exists today |
|---|---|---|---|---|---|
| THz gap | 300 µm | 1.00 | **SSMB-coherent** | wins | synchrotron THz-FEL |
| EUV litho | 13.5 nm | 0.14 | **SSMB-coherent** | terminal-thin | none (SSMB-EUV concept) |
| water window | 3 nm | ~0 | incoherent-ICS | works | synchrotron only |
| hard X-ray | 0.1 nm | ~0 | incoherent-ICS | real-today | Lyncean compact ICS |
| nuclear gamma | ~5 pm | ~0 | incoherent-ICS | real-today | HIGS / ELI-NP |
## The synthesis boundary (the honest finding)
The SSMB coherent-N²-CW advantage (the H_043 breakthrough) applies only where the wavelength is long enough to micro-bunch (**λ ≳ ~10 nm** at σ_z ~ 3 nm) — **THz and EUV**. Below that, the bunching factor collapses (b²→0) and the engine falls back to **plain incoherent inverse-Compton**, which is **already real** (Lyncean, HIGS, ELI-NP). And that is fine, because the shorter bands' applications need far less flux than EUV-litho. So the breakthrough is **targeted**: it matters exactly at the one high-flux band (EUV) and is **unnecessary elsewhere**.
## Falsifiers
F-BC-1 SSMB-coherent regime includes THz+EUV · F-BC-2 gamma breaks to incoherent (too short to bunch) · F-BC-3 ≥2 incoherent-ICS bands real today · F-BC-4 only extreme-flux EUV is terminal-thin (requirement-driven) · F-BC-5 every band in one regime · F-BC-6 ≥5 bands.
## Honest Limits
L1 the b² boundary uses a representative σ_z ~ 3 nm; sub-nm bunching (if achieved) would extend the SSMB-coherent regime toward the water window; L2 "real today" for X-ray/gamma is at *their* lower-flux needs, not litho power; L3 verdicts are supply-side per-band, not full per-application economics.
## Verdict
```
verdict_class: SUPPORTED  (6/6)
SSMB-coherent: THz(b²=1.0)+EUV(b²=0.14); incoherent-ICS (real today): water-window/hard-X/gamma; only EUV terminal-thin (extreme flux)
key_finding: the SSMB coherent-CW breakthrough is TARGETED -- it applies at λ≳~10nm (THz, EUV), exactly where
             EUV-litho's extreme flux lives, and is unnecessary at the shorter bands, which fall to incoherent
             inverse-Compton that is already real (Lyncean/HIGS/ELI). The band-space splits cleanly into two
             regimes by the micro-bunch length, and the verdict stays requirement-driven.
honest_note: representative σ_z~3nm sets the boundary (L1); 'real today' at lower-flux apps not litho (L2);
             supply-side per-band not full economics (L3).
```
**State output**: `state/h047_band_ssmb_census_2026_06_25/result.json`
