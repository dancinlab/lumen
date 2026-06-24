---
id: H_028
slug: fel-margin-wall-break
title: Break the FEL beam-quality thin-margin wall (weakness 2) — 3 independent escapes: cooling lifts the margin to 2.0×, inverse-Compton sidesteps the σ<ρ Pierce condition entirely, and a larger ERL acceptance pushes the ρ-trap crossover from 1.81% to 2.88%
domain: light-source
status: supported
exploration_method: break-walls multi-lens (≥2 principled escapes)
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
breaks: H_023/H_024 (thin FEL margin 1.18×)
---
# H_028 — break the FEL beam-quality wall (multi-lens)
> Weakness 2: the FEL coupling margin is thin (1.18×, H_023) and raising ρ is a trap (H_024). Attack with ≥2 independent escapes.
## Lenses
- **L1 cooling**: σ 0.85%→0.5% lifts the FEL margin to 2.0× (the H_024 clean lever).
- **L2 inverse-Compton**: IC has NO Pierce σ<ρ gain condition → the thin-margin wall *does not exist* on the IC photon route (H_006 alt).
- **L3 larger ERL acceptance**: 2%→3% pushes the ρ-trap crossover out (1.81%→2.88%), widening the safe ρ window.
→ 3 independent escapes (one widens, one removes, one relaxes) → reopenable, not terminal.
## Falsifiers
F-FB-1 cooling margin ≥1.5× · F-FB-2 IC needs no Pierce condition · F-FB-3 larger acceptance lifts crossover · F-FB-4 ≥2 lenses · F-FB-5 bounds.
## Honest Limits
L1 cooling stage is itself undesigned (H_013 L1) — the lens names the escape, not the build; L2 IC trades the FEL exponential gain for lower flux/shot (its own wall); L3 larger acceptance costs lattice complexity. Reopenable ≠ solved.
## Verdict
```
verdict_class: SUPPORTED  (5/5)
cooling 2.0x · IC needs Pierce=False · crossover 1.81%->2.88% · 3 escapes -> reopenable
key_finding: the thin FEL margin is reopenable by THREE independent escapes — cooling widens it,
             inverse-Compton removes the σ<ρ condition entirely, and a larger ERL acceptance relaxes
             the ρ-trap; not a single fragile path. (Each escape has its own cost, L1-L3.)
```
**State output**: `state/h028_fel_margin_wall_break_2026_06_25/result.json`
