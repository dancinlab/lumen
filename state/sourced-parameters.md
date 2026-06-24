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
