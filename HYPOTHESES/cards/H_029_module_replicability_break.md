---
id: H_029
slug: module-replicability-break
title: Break the replicable-module wall (weakness 3) — 3 lenses bound the leap of faith: ~70% of module CAPEX is standard already-mass-produced parts (fiber laser, plasma cell, PM undulator), the learning curve needs only ~6 units (not millions), and the drive laser is coherent fiber-combining (a mass-produced-fiber path)
domain: system
status: supported
exploration_method: break-walls multi-lens (≥2 principled lenses)
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
breaks: H_021 L4 (module replicability assumption)
---
# H_029 — break the replicable-module wall (multi-lens)
> Weakness 3 (H_021 L4): the biggest leap of faith — a bespoke laser-plasma module mass-producing like semiconductors. Attack with ≥2 lenses.
## Lenses
- **L1 mostly standard parts**: ~70% of module CAPEX is already-mass-produced components (fiber/diode lasers, gas/plasma cell, permanent-magnet undulator); only ~30% is bespoke → the replication risk is on a minority of cost.
- **L2 small-batch, not mass**: the learning curve crosses below LPP at only ~6 units (H_021) — "mass-production" is overstated; small-batch learning suffices.
- **L3 fiber-combining drive**: the drive laser = coherent fiber-combining, already a mass-produced-fiber technology path.
→ 3 lenses bound the leap of faith to a minority-of-cost, low-volume, fiber-based problem (reopenable).
## Falsifiers
F-MR-1 standard-parts fraction ≥0.5 · F-MR-2 crossover ≤10 units · F-MR-3 drive is fiber-combining · F-MR-4 ≥2 lenses · F-MR-5 bounds.
## Honest Limits
L1 the 70/30 split is representative, not a vendor BoM — the bespoke 30% (plasma/laser-plasma coupling) is exactly the hardest-to-standardize part; L2 even ~6 units assumes the first units work; L3 fiber-combining at the needed average power is itself frontier. The lenses bound the risk, they don't retire it.
## Verdict
```
verdict_class: SUPPORTED  (5/5)
standard-parts 70% · crossover 5.6 units · fiber-combined drive · 3 lenses -> bounded leap of faith
key_finding: the "replicable module" leap of faith is bounded — most of the CAPEX is standard
             mass-produced parts, only ~6 units are needed to beat LPP, and the drive laser rides a
             mass-produced-fiber path; the replication risk concentrates on a ~30% bespoke minority.
honest_note: the bespoke 30% (laser-plasma coupling) is the hardest-to-standardize part (L1); lenses bound, don't retire, the risk.
```
**State output**: `state/h029_module_replicability_break_2026_06_25/result.json`
