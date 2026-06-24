# Sourced parameters — real public data vs the campaign's representative values

> Goal "실측 + 검증 고갈": ground each key hypothesis parameter in published/measured data, mark
> CONFIRMED (representative value within the real range) or CORRECTED (real data differs materially).
> This is the real-value SSOT; the re-verification ledger is `state/h026_sourced_reverify_*/` (H_026).
> Facts are public-order; cite the sources, not vendor-confidential figures.

## Optics
| Parameter | Card value | Sourced (measured) | Verdict |
|---|---|---|---|
| Mo/Si reflectivity @13.5 nm | R=0.70 (H_002) | ~67–71% peak (70.0% with B₄C interfaces; 68.8% sputtered) | ✅ CONFIRMED |
| La/B-based reflectivity @6.5 nm | R=0.55 (H_002) | La/B₄C 51.1% · **LaN/B₄C 58.1%** · 64% off-normal @6.65 nm | ⚠️ slightly low — best measured 0.58 → wall less severe (re-run H_026) |
| EUV mirror count | N=11 (H_002) | illuminator 4 + projection 6 = **10** (0.33 NA); High-NA projection 8 | ✅ CONFIRMED (~10–11) |

## LPP source + throughput + power
| Parameter | Card value | Sourced | Verdict |
|---|---|---|---|
| LPP in-band source power | 250 W (H_001) | >200 W at IF; 205 W operating, 250 W target | ✅ CONFIRMED |
| droplet / rep rate | 50 kHz (H_001) | ~50 kHz | ✅ CONFIRMED |
| conversion efficiency (2% BW) | 5% (H_001) | ~4–5% | ✅ CONFIRMED |
| HVM throughput floor | 100 WPH (H_005) | NXE ≥135–170 WPH; EXE ≥185 WPH | ✅ CONFIRMED (100 conservative) |
| scanner wall-plug power | 1 MW (H_020) | ~1,170 kW (Low-NA) → up to 1,400 kW (High-NA) | ✅ CONFIRMED (~1.17 MW) |
| **wall-plug efficiency** | ~0.02% implied (H_008/020) | **~0.02% (200 W at IF for 100 WPH ⇐ ~1 MW input)** | ✅ CONFIRMED — direct anchor |
| EUV tool CAPEX | $350 M (H_020) | >$200 M (0.33 NA); $300–400 M (High-NA EXE) | ✅ CONFIRMED |
| energy / year per scanner | (derived) | ~10.2 GWh/yr (cross-check) | ✅ consistent with ~1 MW × ~70% util |

## Accelerator / FEL / recombination laser
| Parameter | Card value | Sourced | Verdict |
|---|---|---|---|
| LPA gradient E₀ @1e18 cm⁻³ | 96.16 GV/m (H_004) | reference-matched to demiurge (Dawson) | ✅ exact |
| LPA-FEL energy spread σγ/γ | 0.85% cooled (H_023/024) | LPA beams **typically several %**; FEL "exists with 1% spread"; sub-% only with modern LWFA | ⚠️ CORRECTED — raw LPA σ often > ρ; cooling is REQUIRED, not routine (strengthens H_024) |
| FEL Pierce ρ | 1.0% (H_023/024) | high-current LPA regime; FEL needs σγ/γ < ρ (gain length ∝ 1/(quadratic in spread)) | ✅ structurally right; margin thinner than implied |
| 46.9 nm Ar XRL gain g | 1.0 cm⁻¹ (H_017) | measured **0.46–1.2 cm⁻¹** (typ. ~0.6) | ⚠️ CORRECTED — ~0.6, not 1.0 |
| 46.9 nm XRL gain-length gL | 14 (saturation, H_017) | **measured gL_max ≈ 8.28**; saturated amplifier to ~16.4 cm (Rocca) | ⚠️ CORRECTED — demonstrated gL ~8 < 14; saturation harder → recombination route harder |
| ERL BBU threshold current | 20 mA (H_018) | ~1→10 mA (MESA); ~10 mA (JLab IR-demo) | ⚠️ CORRECTED — ~10 mA (margin still ~50× → conclusion holds) |

## Economics (generic — not litho-specific, lower-priority)
| Parameter | Card value | Sourced | Verdict |
|---|---|---|---|
| industrial electricity | $0.10/kWh (H_020) | generic industrial $0.07–0.15/kWh (region-dependent) | ◐ generic textbook |
| maintenance fraction | 1/4 tool/yr (H_020) | transcript ~1/4–1/3 | ◐ source = transcript |
| Wright learning rate | 0.85 (H_021) | generic hardware Wright slope 0.80–0.90 | ◐ generic, not accelerator-specific |

## Net (🜂 honest)
- **The campaign's CORE inputs are real**, not fabricated: optics R, mirror count, LPP power/CE/rep-rate,
  scanner wall-plug, the ~0.02% efficiency, EUV-tool CAPEX, throughput floor — all within published ranges.
- **Three optimistic links are corrected by data:** (1) best-measured La/B is 0.58 → the 6.5 nm optics wall
  is ~8× not 14× (still a wall); (2) the demonstrated 46.9 nm XRL reaches gL ~8, *below* the gL~14 saturation
  rule → the recombination-laser route is harder than H_017's anchor implied; (3) raw LPA energy spread is
  often several %, so the FEL coupling needs cooling that is not yet routine (strengthens the H_024 "cooling
  is the binding lever" finding).
- **Net effect on conclusions:** the *physics-wall* findings hold (flux not a ceiling, CAPEX the binding
  wall, M8 ~0.5%); the *engineering margins are thinner* than the representative cards implied — the honest
  direction of every correction is "harder, not easier."

## Fleet round — deeper sourcing (prior-art · accel · econ lanes, 🜂)
| Finding | Sourced | Effect on campaign |
|---|---|---|
| **Concept novelty** | LPA-EUV-FEL fully designed by Nakajima (HPLSE 2014): 5cm gas-cell→660 MeV→1m undulator→1 kW@13.5nm; compact 13.5nm FEL PRSTAB 14:040702 (2011) | ⚠️ lumen's synthesis is **NOT novel** — a >10-yr published direction |
| **Funded driver** | xLight ($40M Series-B Jul-2025; ≤$150M CHIPS LOI Dec-2025; 2028 Albany prototype; ex-LCLS CEO; 1 source→~20 scanners) + KEK 10 kW ERL EUV-FEL — both **conventional ERL/SC-linac** | ⚠️ the **tabletop-LPA driver lumen emphasized is the less-mature, less-funded variant**; industry bet on conventional ERL |
| **Funded econ leg** | xLight model = one big source amortized across ~20 scanners | ⚠️ the funded lever is **M9-amortization, not the M7 module-array learning curve** of H_021 |
| **LPA-FEL wavelength floor** | demonstrated 27 nm SASE (Wang, Nature 595:516, 2021); ~25 nm (2026) — **never 13.5 nm on LPA** | ⚠️ 13.5 nm on an LPA beam is unproven (~2× the target) |
| **Cooling lever** | optical-stochastic cooling demonstrated only on storage-ring circulating beams (IOTA, Nature 2022); **no single-pass GeV-LPA cooling to <0.5%** | ⚠️ H_028's cooling lens is **aspirational** for single-pass LPA |
| **Wright slope** | accelerator/ILC components 85–95% (0.90 typical); 0.85 is the aggressive end | ⚠️ at b=0.90, module@N=10 ≈ 35% (not 20%) → H_021 survives only if first-unit < 2× mature |
| **Energy share** | ~$0.6/wafer-layer of ~$70 tool cost (~1%); FEL ~6× better wall-plug than LPP | ✅ confirms M8 negligible + the efficiency-edge thesis |

**Fleet net (🜂):** the campaign's *direction* is validated by real industry money (xLight/KEK) — but three honest corrections land via H_030: (1) the funded driver is a **conventional ERL, not the tabletop LPA** lumen emphasized; (2) the funded economic lever is **M9-amortization, not M7 module-learning**; (3) **13.5 nm-on-LPA and single-pass cooling are undemonstrated**. The robust restatement: "a shared accelerator-driven FEL amortized across many scanners" (the xLight bet) — lumen's specific *compact-LPA + module-array + cooling* form is the longer-horizon, less-proven variant of an already-pursued idea.

## Fleet round 2 — sharpened corrections (🜂, H_031)
| Finding | Sourced | Effect |
|---|---|---|
| Single-pass cooling | never demonstrated; OSC is multi-turn storage-ring only (IOTA 100 MeV; CESR 1 GeV) | ⚠️ H_028 cooling lens aspirational (confirmed) |
| Dechirp ≠ cooling | DESY LUX (Nature 2025) 2.13%→0.068% single-pass, but a *correlation* rotation — slice spread unchanged | ⚠️ the demonstrated single-pass win does NOT help FEL gain |
| Slice-spread wall | 0.5% slice / ρ~1e-3 ≈ 5× over Ming-Xie → no 13.5 nm lasing; demonstrated LPA-FEL floor ~24.8–27 nm | ⚠️ the wavelength dial (H_007/H_011) is bounded by slice spread; TGU = named unverified escape |
| xLight architecture | definitively an **ERL FEL** (EUVL Workshop 2024 P43, JLab heritage), not cavity, not LPA; $150 M CHIPS finalized 2026-06; zero funded LPA programs | ✅ sharpens H_030 (funded = energy-recovery linac) |
| Cryomodule Wright | HEP SRF slope ~0.95 (E-XFEL 103 CMs, ILC TDR) → ~15% over a fleet | ⚠️ economics = M9 amortization, not M7 learning |
| Amortization break-even | KEK $260 M/10 kW → ~$26 M/scanner at N~10 (~8× < LPP); inverts at N=1 ($260 M > $200 M) | ⚠️ H_021 holds only at fan-out N≥~2 |
| IC-EUV (H_028 L2) | inverse-Compton is genuinely undulator-free (no σ<ρ), but EUV-IC undemonstrated (RadiaBeam X-ray pilot; TU Eindhoven research; "very small" power) | ◐ real physics, undemonstrated at EUV |

**Fleet-r2 net (🜂):** the wavelength "dial" is bounded by **slice energy spread** — dechirping (the only demonstrated single-pass win) is not cooling, so a real 0.5% LPA beam will not lase at 13.5 nm; only a TGU (unverified) could. The CAPEX win is **real but only amortized** across a fan-out (M9), the manufacturing learning curve (M7) being shallow. Every r2 correction again points the same honest direction: **the funded conventional-ERL/M9 form is the robust one; the tabletop-LPA/dial/cooling form is the harder, less-proven variant.**

## Fleet round 3 — the decisive TGU escape (🜂, H_032) · FLEET DEPLETED
| Probe | Sourced | Verdict |
|---|---|---|
| TGU energy-spread tolerance | percent-level (Huang TGU theory; ring-RAFEL sim stable at 0.45% @13.5 nm) | theory OK |
| TGU-FEL ever lased | **none at any wavelength** (only simulations/proposals); best LWFA-FEL = 275 nm seeded (COXINEL/HZDR 2022) | ❌ undemonstrated |
| TGU cost for LPA | dispersion section degrades small LPA emittance past the tight 13.5 nm β~1 mm matching (PRAB 20.020701 transport limits) | ❌ breaks LPA emittance budget |
| Conventional ERL clears? | RF compression to ≪0.1% slice; FLASH lased 13 nm in 2006 (600 MeV linac) | ✅ yes |

**Fleet-r3 net + DEPLETION (🜂):** the last named orthogonal escape (TGU) does NOT rescue the tabletop-LPA at 13.5 nm — undemonstrated, and its dispersion cost breaks the LPA emittance budget. So the slice-spread wall is classified: it **STANDS for the tabletop-LPA variant** but is an **architecture wall, not a physics ceiling** — the funded conventional ERL clears it by compression. All fleet lanes are now depleted: the load-bearing question (is the answer tabletop-LPA or shared-ERL?) is resolved in favor of the **shared conventional-ERL FEL amortized across scanners** (xLight/KEK), the form industry is funding. Remaining threads (GENESIS curves, IC-EUV power, drive-laser ceiling) are refinements that cannot move this conclusion.

## Breakthrough — inverse-Compton sidesteps the slice-spread wall (🜂, H_033)
The slice-spread wall (H_031/032) is **FEL-gain-specific**. The orthogonal gain-free mechanism — **inverse-Compton scattering** — reaches 13.5 nm with **~2.2 MeV** (λ_x = λ_L/4γ², 1 µm laser), ≈455× less beam energy than an undulator FEL, with **no Pierce/Ming-Xie condition**, so a 0.5% slice spread only broadens the line to ~1% (within the ~2% mirror passband). The compact-source-at-13.5 nm question **reopens**; the wall **relocates to average power (flux)**, which the campaign classified as reopenable (H_016, no Liouville ceiling). **Honest residual:** ICS-EUV at lithography in-band power is undemonstrated (RadiaBeam X-ray pilot; TU Eindhoven coherent-ICS research; power "very small"). So this breaks the *slice-spread* wall, not the whole problem — the new front is ICS flux.
