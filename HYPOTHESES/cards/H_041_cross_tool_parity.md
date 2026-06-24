---
id: H_041
slug: cross-tool-parity
title: Cross-tool / byzantine check (gap top-3 #1) — independently re-deriving the 5 load-bearing numbers from first principles inline and asserting equality with the shared harness tool/lumen_optics.py; all 5 match to 1e-9 (optics 14.19×, ICS 2.199 MeV, Ming-Xie 5.0, break-even 1.3, undulator 511 MeV) → harness byzantine-clean; the check did its job — when first run it flagged a discrepancy, root-caused to a unit-convention bug in the test caller (not the harness), now fixed
domain: system
status: supported
exploration_method: gap-fleet lane 1 — independent hand re-derivation, baked into the lab
verification_method: deterministic harness + 6 pre-registered falsifiers (hand vs harness equality)
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
closes: gap cross-tool-consistency / byzantine
---
# H_041 — cross-tool parity (the independent second opinion, permanent)
> The whole lab rested on ONE harness + the author's arithmetic (gap: byzantine). This card re-derives the load-bearing numbers a SECOND way, inline, and asserts equality — so a future silent harness bug is caught on every run.
## The 5 load-bearing numbers (hand == harness, ε=1e-9)
optics multiplier (0.70/0.55)¹¹ = **14.19×** · ICS 13.5 nm @1 µm = **2.199 MeV** · Ming-Xie 0.5%/0.1% = **5.0** · FEL-vs-LPP break-even N* = **1.3** · undulator 13.5 nm @18 mm,K=1 = **511 MeV**. All MATCH.
## The check worked
On first run it **flagged a mismatch** on the undulator number. Root-cause: the test caller passed `(period_m, wavelength_m)` but the harness signature is `(target_nm, period_nm, k)` — a *unit-convention bug in the independent re-derivation*, NOT in the harness. The existing cards (H_006/007/011) call it correctly. Fixed; now 5/5. This is the byzantine lens doing exactly its job: flag → root-cause → the harness is clean.
## Falsifiers
F-XT-{a..e} each hand-value == harness-value · F-XT-ALL all 5 match (byzantine-clean).
## Honest Limits
L1 covers the 5 PRIMITIVES, not every composite card that chains them (a correct atom can be misassembled — the named next probe); L2 ICS formula is the low-recoil head-on limit (recoil ~1e-5 at γ=4.3, negligible); L3 "511 MeV" is 510.999 MeV to 3 sig figs.
## Verdict
```
verdict_class: SUPPORTED  (6/6)
5/5 hand-derivations match the harness to 1e-9 -> byzantine-clean; the one initial mismatch was a test-caller unit bug, root-caused and fixed (harness correct)
key_finding: the shared harness is byzantine-clean on its 5 load-bearing primitives, independently
             confirmed; and the cross-tool check demonstrably works (it caught a real discrepancy and
             root-caused it to the test caller, not the harness).
honest_note: primitives not composites (L1); low-recoil ICS limit (L2); 3-sig-fig rounding (L3).
```
**State output**: `state/h041_cross_tool_parity_2026_06_25/result.json`
