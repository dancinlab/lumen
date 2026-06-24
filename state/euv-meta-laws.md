# EUV source-problem meta-laws (abstraction lane · 🜂 unverified)

> ⚠️ **Abstract / d6 / 🜂 — coordinates, not discovery.** Peels the verified law-set H_001–H_012
> down to the conserved trade-offs underneath (meta-laws), names the assumption each breakthrough
> must break (escape), and casts each escape as a falsifiable prediction. Output of the lumen
> "abstraction lane" (fleet). Nothing here is established.

## Census — what each H-law conserves

| Cluster | Conserved / traded quantity | H-laws |
|---|---|---|
| C1 Photon survival | photons through optics, R^N | H_002 |
| C2 Source-power ceiling | average in-band power of a thermal/plasma emitter | H_001 · H_005 · H_008 |
| C3 Acceleration footprint | gradient × length = energy | H_004 · H_010 |
| C4 Phase-space / brightness | emittance + energy spread → in-band fraction | H_009 · H_008(flux) |
| C5 Wavelength dial | λ vs electron energy, no floor | H_006 · H_007 · H_011 |

C1–C4 are *cost* faces; C5 is the lone *freedom* face — the wall is never wavelength, always one of the four costs.

## Meta-laws (🜂)

- **M1 — Multiplicative reflectance attrition.** Incoherent imaging conserves nothing additively: T = R^N, demand ∝ R^(−N). *Why:* each bounce is an independent Bernoulli survival on a Bragg stack; at short λ layer index-contrast → 1, capping peak R; N is fixed by the imaging NA/aberration budget. *Faces:* H_002.
- **M2 — Power–rep-rate product floor.** P̄ = f_rep·E_pulse·CE·η saturates (~1.5 kW LPP) because the factors are plasma-coupled and trade against each other. *Why:* a thermal radiator's brightness is capped by emission temperature + self-absorption; the factors share one plasma state. *Faces:* H_001 · H_005 · H_008.
- **M3 — Footprint × gradient invariant.** E = ∫eE_z dl; at fixed E, footprint and gradient trade reciprocally (RF: low-field × km; wakefield: 96 GV/m × cm). *Why:* energy is a line integral of force; gradient capped by medium breakdown / cold wave-breaking field. *Faces:* H_004 · H_010 · H_007.
- **M4 — Liouville / brightness bound.** 6-D phase-space density is conserved under conservative forces; Δλ/λ ≈ 2(σγ/γ), so the 2% in-band budget hard-caps σγ/γ ≲ 1% (present LPA violates → 2.24%). *Why:* Liouville's theorem; an undulator only maps the injector's density to photons, never improves it. *Faces:* H_009 · H_008(flux face).
- **M5 — Wavelength has no floor (the freedom law).** λ ∝ 1/E² is unbounded; what is conserved is the *transfer of the wall* — every nm is paid as M2-power, M3-footprint, or M4-brightness, never as λ-impossibility. *Faces:* H_011 · H_006 · H_007.

## Escapes (broken assumption → mechanism · 🜂)

- **E1 (beats M1):** drop "incoherent imaging mirrors" → all-grazing-incidence (total external reflection, R≈0.9 even at 6.5 nm) or coherent maskless projection collapses N. *(Partially realized: H_012, ~8×.)*
- **E2 (beats M2):** drop "thermal radiator" → non-thermal coherent emitter (FEL/undulator/inverse-Compton) decouples the factors; P̄ = rep-rate × beam energy set by wall-plug. Debt then migrates to M3/M4.
- **E3 (beats M3):** drop "single-stage / cold-medium gradient cap" → staging + higher plasma density (E_0 ∝ √n_e) moves the footprint×gradient curve.
- **E4 (beats M4) — HIGHEST LEVERAGE:** drop "conservative single-particle (Liouville)" → dissipative cooling (radiative / laser / optical-stochastic) or chirp+dechirp compression shrinks σγ/γ below the 1% in-band threshold. Liouville forbids only lossless optics.
- **E5:** M5 is not a wall — it is the map. The escape is to attack the cheapest of M1–M4, not the wavelength.

## Falsifiable predictions (🜂)

- **P1 (E1):** a grazing/coherent column drops the 6.5 nm photon penalty below ~5× (vs 14×). Probe: ray-trace + reflectivity sweep. *(H_012 verified the recovery side, ~8×.)*
- **P2 (E2):** a non-thermal source delivers P̄ ≥ 3.5 kW in-band at 6.5 nm with no plasma-coupling rolloff. Probe: power-budget sweep finding the binding factor (will be M4, not M2).
- **P3 (E3):** staged high-density LPA reaches the target γ at ≥10× smaller footprint than a synchrotron at equal power. Probe: E_0 ∝ √n_e staging scaling calc.
- **P4 (E4) — first to attack:** a cooling stage drives σγ/γ from ~1% to ≤0.87%, pushing the undulator line inside 2%, **while the flux wall (H_008) does NOT relax** → M4 splits into a beatable *quality* sub-wall and a stubborn *flux* sub-wall. Probe: single desktop beam-dynamics sim. *(Frozen as verified H_013.)*
- **P5 (E5):** across ≥3 architectures the binding wall is always one of M1–M4, never wavelength. Probe: tabulate LPP / synchrotron / LPA-undulator / inverse-Compton vs the four walls.

## Verdict (🜂)

- **True ceilings:** M4 flux-face (charge × rep-rate, thermodynamic) is the hardest; M3 gradient in its breakdown form is a material ceiling (but footprint-face reopenable); M5 is not a ceiling.
- **Reopenable substrate walls:** M1 (grazing/coherent), M2 (non-thermal emitter — already half-broken, which is why the problem migrates to M3/M4), M4-quality face (dissipative cooling).
- **Attack first → E4/P4:** the quality sub-wall is a 2.24%-vs-2% miss (the smallest hard margin in the whole law-set), breakable by a non-conservative mechanism, cheapest to probe, and it cleanly *separates* the beatable quality-wall from the stubborn flux-wall (H_008) — the single most decision-relevant unknown for HVM viability. → built as **H_013**.
