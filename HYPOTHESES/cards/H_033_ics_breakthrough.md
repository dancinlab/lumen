---
id: H_033
slug: ics-breakthrough
title: Breakthrough — the slice-spread wall is FEL-gain-specific; inverse-Compton scattering (ICS) is the orthogonal radiation mechanism immune to it, reaching 13.5 nm with only ~2.2 MeV (≈455× less beam energy than an undulator FEL) and no Pierce/Ming-Xie gain condition, so slice spread only broadens the ICS linewidth to ~1% (within the ~2% mirror passband) instead of killing output — the compact-source-at-13.5 nm question reopens, the wall relocating to average power (flux), which is reopenable (H_016) not a physics ceiling
domain: light-source
status: supported
exploration_method: break-walls — change the radiation mechanism (enumerate orthogonal gain-free families)
verification_method: deterministic harness + 6 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
breaks: H_031/H_032 (the slice-spread wall, for the compact-source question)
---
# H_033 — breakthrough: ICS sidesteps the slice-spread wall
> Goal "돌파". break-walls forbids calling a wall terminal after one escape (TGU, H_032). The slice-spread wall is **FEL-gain-specific** — it binds only schemes that need exponential FEL gain (gain length ~1/ρ diverges once σ_slice ≫ ρ). Enumerate orthogonal **gain-free** radiation mechanisms.
## The orthogonal mechanism — inverse-Compton scattering (ICS)
- ICS bounces a drive laser off the e-beam, Doppler-upshifting it to EUV: λ_x = λ_L/(4γ²). There is **no Pierce ρ and no Ming-Xie criterion** — slice spread only *broadens the linewidth* (~2σ), it cannot collapse a gain length that doesn't exist.
- **It reaches 13.5 nm with only ~2.2 MeV** (1 µm laser) — vs ~GeV for an undulator FEL, **≈455× less beam energy**. The whole EUV/soft-X band (13.5 → 6.5 → 3 nm) is under ~5 MeV. That is a genuinely tabletop electron source.
- At 0.5% slice spread the ICS linewidth is ~1%, **within the ~2% mirror passband** — usable for litho.
## The wall relocates (honest)
ICS does not make the problem vanish; it **relocates the wall from beam-quality to average power (flux)**: the Thomson cross-section is tiny, so litho-grade flux needs high charge × recirculated laser × high rep rate. But the campaign already showed **flux is reopenable** (H_016: ERL/optical-recirculation, no Liouville ceiling) — a *different, non-terminal* wall. **Residual honesty:** ICS-EUV at lithography in-band power is **undemonstrated** (RadiaBeam X-ray pilot; TU Eindhoven coherent-ICS research; output power "very small").
## Falsifiers
F-BK-1 ICS 13.5 nm ≤5 MeV · F-BK-2 whole band ≤5 MeV · F-BK-3 slice only broadens within passband · F-BK-4 ≥100× less energy than FEL · F-BK-5 ICS-EUV power undemonstrated (honest) · F-BK-6 bounds.
## Honest Limits
L1 ICS is quasi-monochromatic, not laser-coherent — partial (source-size) coherence only; litho tolerance is plausible but unproven at 13.5 nm; L2 the flux wall is real and currently unmet — this breaks the *slice-spread* wall, not the *whole problem*; L3 λ_x=λ_L/4γ² is the ideal head-on formula (recoil, angle, laser bandwidth add corrections).
## Verdict
```
verdict_class: SUPPORTED  (6/6)
ICS 13.5nm=2.20 MeV (455x < FEL) · 3nm=4.66 MeV · slice 0.5% -> linewidth 1.0% (< 2% passband) · ICS-EUV power undemonstrated
key_finding: the slice-spread wall is FEL-specific and is BROKEN for the compact-source question by an
             orthogonal mechanism — inverse-Compton needs no gain condition, reaches 13.5 nm at only ~2 MeV
             (~455x less energy, truly tabletop), and slice spread merely broadens its line. The wall
             relocates to average power (flux), which the campaign already classified as reopenable (H_016).
honest_note: ICS-EUV at litho power is undemonstrated (L2); quasi-mono not coherent (L1); ideal formula (L3).
             This breaks the slice-spread wall, NOT the whole problem — the flux wall is the new front.
```
**State output**: `state/h033_ics_breakthrough_2026_06_25/result.json`
