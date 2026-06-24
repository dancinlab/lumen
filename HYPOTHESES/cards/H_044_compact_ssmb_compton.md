---
id: H_044
slug: compact-ssmb-compton
title: Break the SSMB footprint residual (H_043 L1) via the low-energy SSMB + laser-Compton variant — a 7 MeV micro-bunched beam Compton-scattered off a CO₂ laser reaches 13-14 nm, and at 7 MeV the bending radius is ~2.3 cm (1 T) → a metre-scale (tabletop) ring, ~73× lower energy than the 511 MeV undulator path; this synthesizes SSMB coherent-CW power (H_043) + Compton slice-spread-immunity at MeV (H_033), giving compact + coherent + slice-immune — the tabletop dream resurrected through a different mechanism than the terminal-thin FEL path; honest residual: the Compton flux tax (enhancement cavity, H_034/036) and 13.5 nm kW from a 7-MeV SSMB-Compton ring undemonstrated
domain: light-source
status: supported
exploration_method: break-walls continuation — break the H_043 footprint residual (reference-matched compact SSMB-EUV concept)
verification_method: deterministic harness + 6 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
breaks: H_043 L1 (SSMB footprint) · synthesizes H_033 (ICS) + H_043 (SSMB)
---
# H_044 — compact 7-MeV SSMB-Compton breaks the footprint wall
> H_043 broke the accelerator *power* wall but left a *footprint* residual (still a ~50-100 m ring at undulator energies). Break that residual.
## The compact variant (sourced, as-of 2026-06)
- The Tsinghua SSMB-EUV compact concept uses a **7 MeV micro-bunched beam + CO₂-laser Compton scattering** to reach **13-14 nm** (no undulator).
- At 7 MeV the magnetic **bending radius is ~2.3 cm** (1 T) → a **~1 m-circumference (tabletop) ring**, **~73× lower energy** than the 511 MeV undulator path → the footprint wall is broken.
## The synthesis (why this is the missing piece)
It combines three verified results into one device: **SSMB** coherent-CW micro-bunching (H_043, power) + **laser-Compton** up-conversion that hits 13.5 nm at only MeV and is **slice-spread-immune** (H_033, beam-quality) + **low energy** → small ring (footprint). So it is **compact + coherent + CW + slice-immune** — the tabletop dream the campaign first chased (H_022) and found terminal-thin via the *FEL* path (H_038), resurrected through a *different* mechanism.
## Falsifiers
F-FP-1 ≤10 MeV reaches 13.5 nm · F-FP-2 bend radius ≤5 cm (tabletop ring) · F-FP-3 ≥50× lower energy · F-FP-4 synthesizes SSMB+Compton · F-FP-5 honest residual (Compton flux tax + 13.5 nm kW undemonstrated) · F-FP-6 bounds.
## Honest Limits
L1 it breaks footprint+power+beam-quality but the **Compton flux tax remains** (small cross-section + bandwidth-collection, H_034/036) — needs a high-finesse enhancement cavity, which at 7 MeV + CO₂ is the laser-Compton standard but still the binding engineering front; L2 **13.5 nm kW from a 7-MeV SSMB-Compton ring is undemonstrated** — micro-bunching + Compton + cavity together at litho power is concept-stage; L3 bend radius uses p≈E and a representative 1 T; real rings add straights + insertion devices.
## Verdict
```
verdict_class: SUPPORTED  (6/6)
7 MeV -> bend radius 2.3 cm -> ~1.1 m ring (73x lower energy than 511 MeV); synthesizes SSMB(H_043)+Compton(H_033) -> compact+coherent+CW+slice-immune; residual = Compton flux tax + 13.5nm kW undemonstrated
key_finding: the SSMB footprint residual is broken by the low-energy (7 MeV) SSMB-Compton variant -- a
             metre-scale ring that is compact + coherent + CW + slice-spread-immune. The tabletop dream
             returns through a mechanism (SSMB micro-bunching + laser-Compton) different from the FEL path
             that was terminal-thin. Residual: the Compton flux tax (enhancement cavity) + undemonstrated.
honest_note: Compton flux tax remains, needs enhancement cavity (L1); 13.5nm kW SSMB-Compton undemonstrated (L2);
             representative bend field, straights unmodeled (L3).
```
**State output**: `state/h044_compact_ssmb_compton_2026_06_25/result.json`
