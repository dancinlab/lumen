---
id: H_024
slug: cooling-vs-rho
title: Cooling is the clean lever, raising the FEL Pierce ρ is a trap — deeper cooling lifts BOTH the FEL and ERL margins, while raising ρ widens the FEL margin but crushes the ERL energy-acceptance margin below 1 (recovery fails) past a crossover ρ≈1.8%
domain: light-source
status: supported
exploration_method: two-knob analysis of the H_023 cross-coupling (fleet-full finding)
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
deepens: H_023 (the binding FEL beam-quality coupling)
---

# H_024 — cooling is the clean lever; raising ρ is a trap

> Deepens H_023's binding cross-coupling. The fleet-full @-frontier sweep surfaced that the FEL
> beam-quality margin has two knobs (cooling σ, Pierce ρ) — and they are NOT interchangeable.

## Hypothesis

The FEL coupling has FEL margin = ρ/σ and ERL margin = acceptance/√(σ²+ρ²). **Deeper cooling (lower
σ)** raises BOTH. **Raising ρ** raises the FEL margin (more gain bandwidth) but *lowers* the ERL
margin (the post-FEL beam, spread ~√(σ²+ρ²), grows past the ERL acceptance) — and past a crossover
ρ (~1.8% at the cooled σ) the ERL recovery fails, re-binding the flux wall H_016 had reopened. So
the combination's tightest link is opened by **cooling, not ρ** — ρ is a trap.

## Variables (pre-registered)
- baseline σ 0.85% · ρ 1.0% · deeper-cooling σ 0.5% · raised-ρ 2.0% · ERL acceptance 2.0%.

## Run Protocol
- harness: `tool/lumen_optics.evaluate` · run: `state/h024_cooling_vs_rho_2026_06_25/run_h024.py`
- `python3 .../run_h024.py` · `.../result.json`.

## Falsifiers
- **F-CR-1 COOLING-WINS**: cooled σ=0.5% doesn't lift both margins ≥1.5× → cooling not the clean lever.
- **F-CR-2 RHO-TRAP**: raising ρ doesn't push ERL margin <1 → no trap.
- **F-CR-3 COOLING-MONOTONE**: cooling doesn't improve both → model wrong.
- **F-CR-4 RHO-OPPOSED**: raising ρ doesn't improve FEL while worsening ERL → not opposed.
- **F-CR-5 CROSSOVER**: ERL-fail crossover ρ ∉ (baseline, raised) → crossover mislocated.

## Honest Limits
- **L1 (scalar two-knob model)**: real FEL/ERL physics couple emittance, slippage, lattice dispersion;
  this is the first-order σ/ρ trade, not a start-to-end design (H_023 L2 carried).
- **L2 (acceptance representative)**: 2% ERL acceptance is lattice-dependent; a larger acceptance moves
  the crossover ρ out but does not remove the opposed-direction structure.
- **L3 (cooling has its own cost)**: deeper cooling (H_013 L4) can scrape charge / lengthen the machine,
  a second-order coupling to flux not modeled — cooling is the clean lever *for beam quality*, not free.

## Cross-Links
- deepens: H_023 (FEL coupling) · H_013 (cooling) · H_016 (ERL, the recovery that ρ-trap breaks).
- source: `state/at-frontier-census.md` (fleet-full finding).

## Verdict
```
verdict_class: SUPPORTED
evidence_summary: two-knob σ/ρ margin analysis, 5/5 falsifiers PASS.
  baseline σ0.85%/ρ1.0%: FEL 1.18x · ERL 1.52x
  deeper cooling σ0.50%: FEL 2.00x · ERL 1.79x (both UP)
  raise ρ 2.0% [trap]:   FEL 2.35x · ERL 0.92x (ERL FAILS); crossover ρ=1.81%
key_finding: the combination's tightest link (FEL beam quality, H_023) is opened by deeper COOLING,
             which lifts both the FEL and ERL margins, NOT by raising the Pierce ρ — which widens the
             FEL margin but crushes the ERL energy-acceptance and fails recovery past ρ≈1.8%. Cooling
             is the clean lever; ρ is a trap.
honest_note: scalar two-knob model, not a start-to-end design (L1); acceptance representative (L2);
             cooling has its own second-order flux cost (L3).
```

### Run verdict (VERBATIM — 2026-06-25)
```
H_024 cooling is the clean lever; raising rho is a trap
  baseline (sigma 0.85%, rho 1.0%): FEL 1.18x · ERL 1.52x
  deeper cooling (sigma 0.50%):  FEL 2.00x · ERL 1.79x   (both UP)
  raise rho (2.0%) [TRAP]:        FEL 2.35x · ERL 0.92x   (ERL FAILS <1)
  ERL-fail crossover at rho = 1.81%
  F-CR-1 COOLING-WINS  PASS
  F-CR-2 RHO-TRAP      PASS
  F-CR-3 COOLING-MONOTONE PASS
  F-CR-4 RHO-OPPOSED   PASS
  F-CR-5 CROSSOVER     PASS
VERDICT: SUPPORTED  (5/5 falsifiers PASS)
```
**State output**: `state/h024_cooling_vs_rho_2026_06_25/result.json`
