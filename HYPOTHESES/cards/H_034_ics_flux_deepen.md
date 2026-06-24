---
id: H_034
slug: ics-flux-deepen
title: Deepen the ICS breakthrough — the residual flux wall (demonstrated Compton flux falls ~7e5× short of the ~100 W in-band litho target) is reopenable in principle by the same recirculation family the campaign used for flux (H_016) — an optical enhancement cavity (~1e4 circulating-power gain) times an ERL (~1e3 average-current gain) gives ~1e7, exceeding the gap with ~15× margin; honest residual: litho-power ICS-EUV is undemonstrated and needs near-maximal cavity AND ERL together
domain: light-source
status: supported
exploration_method: break→verify→deepen loop (deepen H_033's residual)
verification_method: deterministic harness + 6 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
deepens: H_033 (ICS breakthrough) · H_016 (flux reopenable)
---
# H_034 — deepen: the ICS flux wall is reopenable by recirculation
> Loop step (돌파→검증→심화). H_033 broke the slice-spread wall via ICS but relocated it to **flux** (tiny Thomson cross-section). Deepen that residual.
## The gap (quantified)
- Litho needs ~100 W in-band at 13.5 nm = **6.8e18 photons/s**. The best demonstrated Compton (X-ray) source is ~1e13 ph/s → a **~7e5× flux gap**. The flux wall is real, not trivial.
## The recirculation levers (same family as H_016)
- **L1 optical enhancement cavity**: traps the drive laser → ~**1e4** circulating-power gain (demonstrated in Compton X-ray sources).
- **L2 ERL**: recovers the e-beam energy → high average current, ~**1e3** gain over single-pass.
- Product ~**1e7** > the ~7e5 gap → the ICS flux wall is **reopenable in principle** (~15× margin), the same class as the FEL flux wall (H_016), not a physics ceiling.
## Honest residual
Closing the gap needs **near-maximal cavity AND ERL together**, and **litho-power ICS-EUV is undemonstrated** (X-ray Compton sources sit far below). So the flux wall is *classified reopenable*, not *cleared* — the simultaneity + EUV-cavity engineering is the new front.
## Falsifiers
F-FX-1 gap ≥1e5 (real) · F-FX-2 cavity ≥1e4 · F-FX-3 ERL ≥1e3 · F-FX-4 recirc ≥ gap (reopenable) · F-FX-5 litho-power ICS-EUV undemonstrated (honest) · F-FX-6 bounds.
## Honest Limits
L1 flux estimate uses order-of-magnitude demonstrated/target numbers, not a specific machine design; L2 EUV enhancement cavities are harder than IR (mirror damage, vacuum) — the 1e4 gain is borrowed from IR Compton sources and is itself a frontier at EUV drive; L3 "reopenable in principle" ≠ built — the margin is only ~15×, so any sub-maximal lever closes it.
## Verdict
```
verdict_class: SUPPORTED  (6/6)
litho 6.8e18 ph/s · demonstrated ~1e13 · gap 6.8e5 · recirc cavity(1e4)xERL(1e3)=1e7 >= gap (margin ~15x) · litho-power undemonstrated
key_finding: the ICS flux wall is real (~7e5x gap) but reopenable in principle by the same recirculation
             physics the campaign used for flux (cavity x ERL ~1e7 > gap). It is NOT a new physics ceiling
             -- but the ~15x margin is thin and litho-power ICS-EUV is undemonstrated, so the simultaneity
             of near-maximal cavity AND ERL is the next front.
honest_note: order-of-magnitude flux numbers (L1); EUV enhancement cavities are a frontier (L2); thin ~15x
             margin, reopenable != built (L3).
```
**State output**: `state/h034_ics_flux_deepen_2026_06_25/result.json`
