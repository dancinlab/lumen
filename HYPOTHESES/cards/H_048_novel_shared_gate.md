---
id: H_048
slug: novel-shared-gate
title: The two novel architectures converge on ONE shared gate — both rank-2 SSMB (undulator) and rank-3 compact SSMB-Compton are gated on the same single milestone, steady-state micro-bunching at 13.5 nm precision (σ_z~3 nm → b²~0.14, physics-allowed, undemonstrated); the components are individually demonstrated (SSMB mechanism PoP Nature 2021 at longer λ, Compton X-ray/gamma real via Lyncean/HIGS/ELI, IR enhancement cavities finesse 1e4–1e5 routine) and only the EUV-precision joint operating point is undemonstrated; the rank2-vs-rank3 trade is that rank3 (7 MeV tabletop) pays the Compton bandwidth-collection flux tax (~50× derate) that rank2 (511 MeV undulator, bigger ring) avoids — so one experiment de-risks both
domain: system
status: supported
exploration_method: rank2,3 assault fleet — deep-dive both novel paths' binding gate
verification_method: deterministic harness + 6 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
synthesizes: H_043 (SSMB) · H_044-046 (SSMB-Compton) · the rank 2/3 deep-dive
---
# H_048 — the two novel paths share one gate
> A focused fleet assault on the two NOVEL ranks asked: what single thing gates each? Answer: the SAME thing.
## The shared gate
Both rank-2 SSMB (undulator) and rank-3 compact SSMB-Compton are gated on **steady-state micro-bunching at 13.5 nm precision** (σ_z ~ 3 nm → coherent fraction b² ~ 0.14, **physics-allowed** H_046, **undemonstrated**). The 2021 proof-of-principle showed the mechanism at *longer* wavelength; the EUV-precision joint point (strong laser modulation + low energy spread + ring stability together) is the open experiment.
## Components demonstrated, joint point not
- **SSMB mechanism**: PoP Nature 2021 (Deng/Tang/Chao, MLS Berlin) at longer λ.
- **Compton EUV/X-ray**: real at hard X-ray (Lyncean) and gamma (HIGS/ELI), ~1e13 ph/s.
- **IR enhancement cavity**: finesse 1e4–1e5 routine.
- **Missing**: the 13.5 nm-precision micro-bunching + the integrated high-average-power EUV joint operating point.
## The rank2-vs-rank3 trade
- **rank2 (SSMB undulator)**: avoids the Compton angle-bandwidth flux tax, but needs 511 MeV → a *bigger ring*.
- **rank3 (SSMB-Compton)**: tabletop 7 MeV, but pays the Compton bandwidth-collection tax (~50× derate, H_036), recovered only by stacking IR finesse + ERL current at their demonstrated maxima simultaneously.
- **Common gate**: micro-bunching at 13.5 nm. **One experiment de-risks both.**
## Falsifiers
F-CG-1 both share the gate · F-CG-2 physics-allowed (b²≥0.1) · F-CG-3 rank3 carries an extra flux tax rank2 avoids · F-CG-4 ≥3 components demonstrated · F-CG-5 EUV joint point undemonstrated · F-CG-6 bounds.
## Honest Limits
L1 "shared gate" is the *headline* — each path has secondary gates (rank2: undulator extraction + power-scaling cavity finesse; rank3: the joint finesse×current maximum); L2 the ~50× Compton tax is first-order (H_036 L1); L3 Tsinghua/MLS program timeline + funding for the micro-bunching push are unknown (the economic gate); the funded near-term answer stays the conventional ERL FEL (H_030).
## Verdict
```
verdict_class: SUPPORTED  (6/6)
shared gate = 13.5nm micro-bunching (b²=0.14, physics-allowed, undemonstrated); rank3 pays 50x Compton tax rank2 avoids; 3 components demonstrated, EUV joint point not
key_finding: the two novel architectures converge on ONE shared, physics-allowed, undemonstrated gate --
             steady-state micro-bunching at 13.5 nm. One experiment de-risks both. The rank2-vs-rank3 choice
             is a trade (Compton flux tax vs ring size), not a different gate. Components are individually
             demonstrated; only the EUV-precision joint operating point remains.
honest_note: secondary gates per path (L1); first-order Compton tax (L2); program timeline/funding unknown,
             ERL FEL stays the funded near-term answer (L3).
```
**State output**: `state/h048_novel_shared_gate_2026_06_25/result.json`
