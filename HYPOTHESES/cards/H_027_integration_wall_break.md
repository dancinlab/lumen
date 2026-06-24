---
id: H_027
slug: integration-wall-break
title: Break the integration wall (weakness 1) — 3 independent lenses reduce it from "unknown invention" to "bounded engineering": every subsystem is standalone-demonstrated (min TRL 4>1), an integrated undulator+ring+beamline precedent exists (synchrotron/FEL), and start-to-end simulation de-risks the joint constraints
domain: system
status: supported
exploration_method: break-walls multi-lens (≥2 principled lenses)
verification_method: deterministic harness + 5 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
breaks: H_022 L1 (integration unproven)
---
# H_027 — break the integration wall (multi-lens)
> Weakness 1 (H_022 L1): components exist but never on one machine. break-walls: attack with ≥2 lenses, then classify.
## Lenses
- **L1 integration-not-invention**: subsystem standalone TRL — LPA 1 GeV (5), LPA-FEL lasing (4), ERL recovery (6), undulator/IC (9); min 4 > 1 → no new physics, only integration.
- **L2 precedent**: synchrotron/FEL light sources integrate undulator+storage-ring+beamlines at facilities today → the integration *physics* is known; only the compact form factor is new.
- **L3 start-to-end sim**: Genesis/Ocelot/elegant-class codes model the joint LPA→FEL→ERL constraints before metal.
→ 3 independent lenses → the wall is a **bounded-engineering / TRL-gap** wall (reopenable), not a terminal/invention wall.
## Falsifiers
F-IN-1 every subsystem TRL>1 · F-IN-2 integrated precedent exists · F-IN-3 S2E sim available · F-IN-4 ≥2 lenses · F-IN-5 bounds.
## Honest Limits
L1 TRLs are representative estimates (the *combination* TRL is ~2–3, lower than any part); L2 "bounded engineering" ≠ built — the 15–30 yr integration program is the real cost; L3 joint-constraint sim ≠ hardware demo.
## Verdict
```
verdict_class: SUPPORTED  (5/5)
subsystem min TRL 4>1 · precedent True · s2e True · 3 lenses -> bounded-engineering wall (reopenable)
key_finding: the integration wall is reopenable — every subsystem is independently demonstrated, an
             integrated light-source precedent exists, and start-to-end sim de-risks the join; the gap
             is engineering/TRL, not invention. (Combination TRL still ~2-3, L1.)
```
**State output**: `state/h027_integration_wall_break_2026_06_25/result.json`
