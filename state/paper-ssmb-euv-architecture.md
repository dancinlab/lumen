# Two routes, one gate: steady-state-microbunching architectures for a high-average-power 13.5 nm lithography source

**A closed-form feasibility analysis.** *lumen verified-hypothesis lab — draft, as-of 2026-06.*

> ⚠️ **Scope & honesty.** This is a **closed-form (in-silico) architecture analysis**, not an
> experimental report. Every quantitative claim is a public-physics scaling relation with
> representative parameters, reproduced deterministically by `tool/lumen_optics.py` and the
> per-hypothesis runners in `state/h0*/` (counts/determinism: `tool/qa.py`). It is **reference-match,
> not priority**: where it aligns with published proposals we cite them; we claim convergence on the
> same physics, not precedence. The binding result is an **experimental milestone**, stated as such.

## Abstract

High-volume EUV lithography needs ~100 W of in-band 13.5 nm average power. Laser-produced-plasma
(LPP) sources supply this today but face wavelength (6.5 nm), flux, and CAPEX walls. We analyze two
accelerator architectures that deliver coherent **continuous-wave** EUV by reusing a stored,
micro-bunched electron beam: **(A)** a several-hundred-MeV storage-ring SSMB *undulator* source and
**(B)** a compact ~7 MeV SSMB beam up-converted by *laser-Compton* scattering. We show, in closed
form, that both reduce to a **single shared gate** — steady-state micro-bunching at 13.5 nm precision
(bunch length σ_z ≈ 3 nm → coherent fraction b² ≈ 0.14) — which is physics-allowed but undemonstrated.
The two routes then diverge in exactly one trade: (B) is metre-scale (~1 m ring at 7 MeV) but pays a
~50× Compton bandwidth-collection flux tax that (A) avoids at the cost of a larger ring. A single
experiment — demonstrating EUV-precision steady-state micro-bunching — therefore de-risks both.

## 1. The source problem and the wavelength dial

The framing claim "no clear technical alternative beyond 13.5 nm EUV" conflates *wavelength* with
*flux*. An accelerator + undulator radiates at λ = (λ_u/2γ²)(1+K²/2); inverse-Compton at λ ≈ λ_L/4γ².
Both give **λ ∝ 1/γ²**, so wavelength is an electron-energy dial with **no physical floor** (H_011):
one machine spans THz (3.4 MeV) → EUV (511 MeV) → hard X-ray (5.9 GeV), 6.5 orders of magnitude
(H_039). The 6.5 nm "wall" of LPP — an ~8× mirror-throughput penalty at best-measured La/B reflectivity
0.58 (H_002, H_026) — is a multilayer-optics problem the dial sidesteps.

**The real bound is beam *slice energy spread*.** For an undulator FEL, gain collapses once
σ_δ/ρ ≳ 1 (Ming-Xie); a representative 0.5 % laser-plasma-accelerator beam sits ~5× over the ρ≈10⁻³
budget and will not lase at 13.5 nm (H_031). Single-pass cooling is undemonstrated, and longitudinal
dechirping is not slice cooling (H_031); a transverse-gradient undulator does not rescue it without
breaking the LPA emittance budget (H_032). A conventional RF linac *does* compress to ≪0.1 % slice
(FLASH lased 13 nm in 2006), which is why the funded near-term answer is a shared conventional
energy-recovery-linac FEL amortized across scanners (H_030). The two architectures below instead make
the **flux** wall, not the slice wall, the binding one.

## 2. Configuration A — storage-ring SSMB undulator (rank 2)

In a storage ring, N electrons normally radiate **incoherently** (P ∝ N). Micro-bunch them at the
radiation wavelength (σ_z ≪ λ) and they radiate **coherently** (P ∝ N²) — a ~10⁶× enhancement.
*Steady-state* microbunching (SSMB) sustains the bunching every turn, so the coherent power is
delivered **continuous-wave** from a reused beam, unlike a single-pass FEL whose beam is dumped
(H_043). The mechanism is proof-of-principle demonstrated [1] at longer wavelength; the Tsinghua
SSMB-EUV program targets ~1 kW at 13–14 nm [2,3] (≥10× the ~100 W HVM floor, H_005). Because the
radiation is on-axis undulator emission, configuration A carries **no Compton bandwidth tax**; its
cost is the higher beam energy (~511 MeV at an 18 mm undulator) and hence a larger ring.

## 3. Configuration B — compact 7-MeV SSMB-Compton (rank 3)

Inverse-Compton up-conversion reaches 13.5 nm from a **7 MeV** beam (λ_x = λ_L/4γ², 1 µm drive),
≈455× less energy than the undulator route, and is **slice-spread-immune** (no Pierce gain condition;
slice spread only broadens the line) (H_033). At 7 MeV the bending radius is ~2.3 cm (1 T), giving a
**metre-scale (~1 m) tabletop ring** (H_044). Combining SSMB micro-bunching (coherent CW) with
Compton up-conversion at low energy yields a **compact + coherent + CW + slice-immune** source — the
tabletop ambition reached through a different mechanism than the slice-spread-bound single-pass FEL
(which is terminal-thin, H_038). A 2025 cavity-based compact EUV-litho proposal [4] occupies this
design space.

The residual is a **flux tax**: the Thomson cross-section is small, so the demonstrated Compton flux
(~10¹³ ph/s) is ~7×10⁵ below the ~6.8×10¹⁸ ph/s needed for 100 W (H_034). Recirculation — an optical
enhancement cavity at the **IR drive** wavelength (finesse 10⁴–10⁵, routine; *not* an EUV cavity,
which multilayer R≈0.70 forbids, H_035) × ERL average-current gain (~10³) — gives ~10⁷, exceeding the
gap. But bandwidth-limited collection (keeping a 2 % in-band passband from the wide low-γ cone) derates
the usable flux ~50×, eating that margin; it is recovered only by stacking the demonstrated finesse and
current maxima simultaneously (H_036), and the brightness lever does **not** help — the λ–θ correlation
is radiation kinematics, beam-independent (H_037, a recorded negative).

## 4. The shared gate

Both configurations rest on **one** unproven step: achieving and holding **steady-state micro-bunching
at 13.5 nm precision** (σ_z ≈ 3 nm). This is **physics-allowed** — the bunching factor
b = exp(−½(2πσ_z/λ)²) ≈ 0.38 gives a coherent fraction b² ≈ 0.14 at the design point, a substantial
N² enhancement with no forbidding floor (H_046). The components are individually demonstrated (the
SSMB mechanism [1]; Compton X-ray/γ sources; IR enhancement cavities); only the EUV-precision *joint*
operating point is missing. **One experiment de-risks both routes** (H_048). Strikingly, the cooling
lever this analysis derived closed-form — *open the beam-quality link by cooling, not by raising the
Pierce ρ, which traps the energy-recovery acceptance* (H_024) — is exactly what the latest SSMB
frontier adds: optical stochastic cooling combined with SSMB [5] (H_050).

## 5. The route trade and economics

| | A — SSMB undulator (rank 2) | B — SSMB-Compton (rank 3) |
|---|---|---|
| beam energy | ~511 MeV | **~7 MeV** |
| footprint | larger ring | **~1 m tabletop ring** |
| Compton flux tax | **none** | ~50× derate (cavity-recoverable) |
| shared gate | 13.5 nm micro-bunching (b²≈0.14) | same |

Economics is requirement-driven (H_040): EUV litho is the outlier band whose *extreme* flux makes the
compact-coherent path margin-thin, while THz/water-window/X-ray apps tolerate lower flux and are won by
the same engine at lower cost. The CAPEX win is real only **amortized** (M9): a shared source across
~10 scanner ports reaches ~$26 M/scanner (~8× < LPP) but inverts at fan-out 1 (H_031); the cryomodule
learning curve is shallow (Wright ~0.95), so volume manufacturing (M7) is not the lever. The 2nd-law
waste-heat floor (M8) is ~0.5 % of cost — negligible (H_020).

## 6. Honest limits & the milestone

(i) All scalings are first-order, closed-form, representative-parameter — not start-to-end
simulations; secondary gates remain (undulator extraction and power-scaling cavity finesse for A; the
joint finesse×current maximum for B). (ii) "Physics-allowed" is necessary, not sufficient: collective
effects, ring nonlinearity, and jitter can erode σ_z. (iii) Resist/materials questions are out of
in-silico scope. **The decisive next step is experimental:** demonstrate steady-state micro-bunching
at 13.5 nm with b² ≳ 0.1 held over ≳10³ turns. Falsifier: if σ_z degrades to ≳10 nm (b² ≲ 0.05) under
realistic modulator + spread constraints, the compact-coherent path reverts to longer wavelengths
(where b²→1) and the funded conventional ERL FEL remains the near-term answer.

## References (open, reference-matched)

[1] X. Deng et al., *Experimental demonstration of the mechanism of steady-state microbunching*,
Nature **590**, 576 (2021).
[2] X. Deng et al., *A synchrotron-based kilowatt-level radiation source for EUV lithography*,
Sci. Rep. (2022), s41598-022-07323-z; arXiv:2110.08987.
[3] Tsinghua SSMB-EUV program materials (EUVL Workshop).
[4] C. He, H. Yang, N. Huang, B. Liu, H. Deng, *Cavity-based compact light source for extreme
ultraviolet lithography*, arXiv:2501.14541 (2025).
[5] X. Deng, *Stochastic Cooling Enhanced Steady-State Microbunching*, arXiv:2512.09399 (2025);
*Application of Optical Stochastic Cooling in Future Accelerator Light Sources*, arXiv:2407.16098 (2024).
[6] K. Nakajima et al., conceptual LPA-EUV-FEL, High Power Laser Sci. Eng. (2014).
[7] H. Xiao et al., *Staged Laser Wakefield Acceleration for Saturated Lasing ... EUV to X-ray*,
arXiv:2603.28214 (2026) — LWFA-FEL EUV floor ~24.8 nm.

*Supporting closed-form evidence: lumen `HYPOTHESES/cards/H_{022,024,030–048,050}.md` + deterministic
runners in `state/h0*/`; re-verify with `python3 tool/qa.py`.*
