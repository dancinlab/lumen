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

## Flux-face ceiling verdict (🜂 — the decisive peel)

Is the **flux sub-wall** (M4 flux face) a true thermodynamic ceiling or reopenable? Decomposing
P_ib = Q·f·N_ib·E_γ (charge × rep-rate × in-band photons/bunch × 13.5 nm quantum):

- **Q** REOPENABLE — bounded by injector space-charge (a non-conserved collective force, suppressed ∝1/γ² by high-energy injection); not a conservation law.
- **f** REOPENABLE (engineering/economic) — bounded by removable heat-flux + wall-plug €, not principle. **ERL** (energy-recovery linac) recovers beam energy → lifts the ceiling by 1/(1−η_rec) (verified **H_016**).
- **N_ib** MIXED — spectral-capture floor = the *quality sub-wall* (beatable by cooling, H_013); FEL extraction efficiency has a soft, regime-reopenable ceiling.

**Brightness theorem:** the radiance/étendue 2nd-law floor (Planck B_ν(T)) binds only *thermal/
incoherent* radiators (= M2) — and is **evaded by non-thermal coherent sources** (FEL, inverse-
Compton, recombination laser), whose photon mode-occupancy ≫1. Liouville for the photon beam binds
only passive optics, not the electron→photon *generation* step. There is **no conservation
inequality that floors average in-band EUV power for a coherent source** at given wall-plug + volume.

**Verdict: the flux face is REOPENABLE, not a true ceiling.** The only surviving hard laws are
energy conservation (P_ib ≤ η·P_wallplug) and the 2nd-law waste-heat minimum — both *efficiency/
economic* bounds, not power floors. The terminal question therefore mutates from "is flux a ceiling?"
(no) to **"can a coherent or energy-recovered source deliver 167 W in a non-stadium volume at
affordable wall-plug?"** — engineering/economic, not thermodynamic.

- **Highest-leverage escape: ERL** (attacks f *and* wall-plug/heat together) → **H_016** (SUPPORTED:
  1/(1−η) lift, no cap; ERL+FEL reaches 200 W compact; ERL alone insufficient = product wall).
- **The load-bearing 🜂 claim** ("no brightness/Liouville floor for a coherent source") is the one
  most worth an adversarial check — predicted falsifier: coherent B_ν exceeds the thermal Planck
  bound at equal drive by ≥10³× (next probe).

## Economic tier — M6–M9 (🜂, the mutated terminal question)

Once flux is reopenable, the terminal question is economic: **compact 167 W at affordable wall-plug.**
Figure of merit = **$/wafer-layer** = (CAPEX·CRF + OPEX) / (wafer-layers/yr), OPEX_energy ∝ (€/kWh)·P_ib/η.

- **M6 — η–coherence coupling (transducer law).** OPEX_energy·η = const at fixed P_ib; the energy bill
  falls *only* by raising η (electrical→in-band), and η rises *only* by coherent generation (occupancy ≫1,
  no out-of-band/2%-capture loss) or beam-energy recovery (ERL). Economic image of physics escape E2.
  Faces: LPP (low-η floor) vs FEL/IC/recombination+ERL (high-η).
- **M7 — CAPEX–footprint gradient trade vs learning curve (size law).** For one bespoke machine,
  $·(gradient)⁻¹ per unit beam energy is conserved (RF: cheap/m, huge; wakefield: compact, bespoke-$).
  Escape = **volume amortization** (mass-produced module arrays descend a Wright's-law curve, b≈0.85–0.9).
- **M8 — Landauer/2nd-law waste-heat OPEX floor (the TRUE ceiling).** P_waste ≥ (1−η)P_wall must be
  cooled at €; cannot be escaped, only minimized by η→1. Bites hardest in small high-heat-flux (compact)
  volume — the price of non-stadium. The asymptote the learning curve never crosses.
- **M9 — single-source amortization/utilization law.** $/wafer-layer × (scanners served) = CAPEX·CRF/throughput;
  a high-CAPEX central coherent source (ERL/FEL beam-split to N scanners) gets cheap *per wafer* only at high utilization.

**Per-route (🜂 order-of-magnitude):** LPP = small footprint but pinned on the low-η OPEX floor (M6/M8);
synchrotron = efficient but ~200× footprint (M7, M9-escapable); **ERL+FEL = de-risked front-runner**
(compact ~200 W, recovery-boosted η; needs M7 learning-curve + M9 amortization to beat LPP);
**recombination laser = high-variance dark horse** (fewest components, no undulator-capture loss = best
intrinsic M6, but unverified at 167 W).

**Predictions Q1–Q3 (🜂, all spreadsheet-grade — cheaper than any physics card):**
- **Q1 (M6):** coherent/ERL reaches η ≥ ~3–5× LPP → OPEX_energy < LPP at €0.1–0.3/kWh.
- **Q2 (M7/M9):** at N≥~10 modules, learning-curve CAPEX/W drops below synchrotron, within ~2× LPP.
- **Q3 (terminal):** compact coherent beats LPP $/wafer-layer only when η ≥ Q1 **AND** amortized across
  M≥~3 scanners — a *conjunction*, neither lever alone. → built as **H_019**.

**Economic verdict (🜂):** reopenable down to the **M8 waste-heat asymptote** (M6 efficiency + M7/M9
amortization are reopenable engineering/volume levers; M8 is the one true ceiling). Whether the M8
asymptote sits above or below LPP's all-in $/wafer-layer is the single decision-relevant unknown —
settled by the Q3 cost-of-ownership spreadsheet (H_019), not by more physics.
