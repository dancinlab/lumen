# Resist-demand + recombination-laser brainstorm (divergence to depletion)

> ⚠️ **Unverified ideation** (d6 / 🜂). The two least-explored frontiers of the EUV source problem,
> divergence lane (fleet). NOT findings. Top-5 frozen as 🜂 abstract hypotheses `H_B1`–`H_B5`.
> Frontier **A** = resist-side photon-demand reduction (make the wafer need fewer photons).
> Frontier **B** = recombination / inner-shell EUV lasing (narrow line without an undulator).
> 8 rounds to depletion, ~90 ideas → 8 themes → top-5. Each idea: (a) frontier/wall · (b) principle · (c) prediction.

## Selected highlights per round (full set condensed; see git for the raw divergence)

**R1–R2 (resist):** chemically-amplified gain runaway (turnover ≥10³ → dose <5 mJ/cm²) · high-Z sensitizer two-step (Sn/Sb, ≥3× fewer photons) · metal-oxide cluster resists (4–6× absorption → ≤15 mJ/cm²) · dry/ALD ultrathin resist (≤40% photon budget) · resonant-cavity resist stack (absorption 30%→70%) · sparse-EUV (cuts only) + DSA/DUV bulk (≤10% full-field dose) · single-photon-counting (Geiger-mode) resist (⟨5 photons/pixel⟩) · two-color resist (EUV arms, cheap visible fires, ≤30% EUV dose) · thermal-latent phase-change resist · multi-pass dose averaging (EPE ∝ 1/√K) · standing-wave dose concentration (≥80% dose into <20% area) · source-resist co-design (≥20% effective in-band recovered).

**R3–R4 (recombination/inner-shell laser):** Ni-like/Ne-like collisional XRL at 13.5 nm (gL≥14) · inner-shell photo-pumped (pump <Auger lifetime) · 3-body recombination in rapidly-cooled plasma (gain >5 cm⁻¹) · capillary-discharge Z-pinch pushed to higher Z (gL≥5) · OFI all-optical recombination laser (<1 J/pulse) · dielectronic-recombination selective feed (FWHM <0.5%) · HHG-seeded plasma amplifier (>100× single-pass, seed-locked line) · quasi-CW high-rep Ni-like (≥10 kHz, ≥1 µJ) · 6.5 nm Gd/Tb lanthanide lasing line (leapfrog) · plasma-waveguide gain extension (saturation in <1 cm) · transfer pumping (donor→acceptor plasma) · waste-energy harvest from spent LPP tin plasma (≥1% recovered coherent) · magnetic confinement re-invertible column · DFB plasma density grating (single-mode, Δλ/λ<10⁻³) · EBIT-pumped HCI trap laser.

**R5 (A×B + metrology/comp-litho):** narrow line + resonant ultrathin resist (≥90% absorption ≤10 nm) · coherent source + ptychography/holographic exposure (≥3× fewer photons) · inverse-litho stochastic budget transfer (≥25% dose cut) · source-flicker-aware dosing (CD σ<0.5 nm at ±20% jitter) · **no-SPF narrow-line recovery** (drop spectral-purity filters → +25% in-band) · interference/Talbot litho from coherent XRL (≥80% photon utilization) · XRL doubles as actinic inspection source · counted-dose feedback (10× fewer defects) · coherent recirculation cavity (≥3× fluence) · ML latent-image denoise (60% photon count).

**R6 (SF/heterogeneous):** biological photoprotein resist (QY>0.9) · metamaterial perfect-absorber resist (≥95% in <15 nm) · Purcell-enhanced lasing transition (≥5×) · squeezed/sub-shot-noise EUV dosing (≥3 dB) · reaction-diffusion self-organizing litho (<10% photon budget) · wafer-integrated EUV nanolaser array (≥167 W aggregate, distributed) · Floquet/time-crystal steady inversion · DNA-origami single-molecule resist (<2 photons/feature).

**R7 (combinations):** "starved-source HVM stack" (seeded XRL + no-SPF + MOx resist + recycle cavity → 167 W-equiv from <40 W raw) · "two-color narrow-arm" (OFI laser arms + visible develops, ≤15% EUV dose) · "coherent ptycho-litho" (≥4× photon cut) · "digital photon-counting litho" (<1 ppm defect at ⟨5/pixel⟩) · "sparse-EUV hybrid node" (≤10% full-field dose) · "re-invertible high-rep XRL engine" (mag-confine + kHz + waste-harvest) · "all-optical compact line source" (OFI + DFB + waveguide → single-mode saturated, no accelerator).

**R8 depletion:** mostly dups (entanglement dosing ~ squeezed light; CTTS ~ sensitizer; autoionizing ~ DR resonance). Depletion declared.

## Clusters (8 themes)
C1 chemical/catalytic gain · C2 high-cross-section absorbers · C3 photon-economy/sparse-EUV ·
C4 stochastics engineering · C5 collisional/recombination plasma lasers · C6 coherence & cavity
exploitation · C7 spectral-purity/system-level relief · C8 SF/exotic.

## Shortlist → frozen as 🜂 abstract hypotheses
- **H_B1** No-SPF narrow-line recovery (C7) — narrow XRL deletes spectral-purity-filter losses (~25–30%) + doubles as inspection. Cheapest near-term, testable on existing optics.
- **H_B2** High-cross-section ultrathin resist (C2) — 4–6× absorption in ≤12 nm film multiplies effective dose (MOx real, metamaterial-absorber the stretch).
- **H_B3** Two-color narrow-arm litho (C3) — EUV only "arms," cheap photons clear → EUV demand ≤15–20%.
- **H_B4** Re-invertible high-rep recombination laser (C5) — the only intrinsically-narrow, undulator-free source-side escape from the flux wall (gL≥14 + ≥10 kHz).
- **H_B5** Digital photon-counting litho (C4) — convert dose-to-clear into a counting problem; prints at ⟨5 photons/pixel⟩ if per-photon gain >10³.

## Structural takeaways
- Cheapest near-term win = **system-level in-band recovery** (kill SPF losses with a narrow line, H_B1).
- The only genuine **source-side** escape from the accelerator flux wall = a **re-invertible high-rep recombination/collisional EUV laser** (H_B4) — sidesteps the accelerator entirely (cf. meta-law M2/E2).
- Resist absorption (H_B2) + sparse-EUV (H_B3) attack the *dose* wall multiplicatively and are the most fundable mid-term.
