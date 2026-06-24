---
id: H_036
slug: ics-bandwidth-derate
title: Loop cycle-2 deepen (honest negative) — the ICS flux margin does NOT survive the bandwidth-collection derating; low-γ ICS emits into a wide ~1/γ cone but keeping the 2% in-band needs a narrow collection half-angle, derating usable flux by ~50×, which eats the H_034 ~15× margin (→0.3×, LOST); it is recoverable only by pushing the demonstrated headroom (IR finesse 1e4→1e5 ×10 AND ERL current ×10 = ×100 → ~30×), running both levers at their demonstrated max simultaneously at EUV — undemonstrated
domain: light-source
status: supported
exploration_method: break→verify→deepen loop, cycle 2 deepen (surface the honest negative)
verification_method: deterministic harness + 6 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
deepens: H_034 (ICS flux margin) · H_035 (cavity basis)
---
# H_036 — cycle-2 deepen: the bandwidth-collection derating eats the margin
> Honest negative (no tune-to-green). The easy H_034 ~15× flux margin does not survive a real collection effect.
## The derating
- Low-γ ICS (γ≈4.3) emits into a wide cone ~1/γ ≈ 230 mrad, but **off-axis photons red-shift**, so keeping the ~2% in-band requires collecting only θ_c ~ √BW/γ ≈ 33 mrad.
- Collected solid-angle fraction ≈ (γθ_c)² = BW → the in-band flux is **derated ~50×**.
- H_034 margin 15× → after derate **0.3× (LOST)**. The naive recirculation does not reach litho power.
## Recovery (and its honest cost)
- Demonstrated headroom: IR finesse 1e4→1e5 (×10) **and** ERL current 1e3→1e4 class (×10) = ×100 → restored ~30×.
- But that runs **both levers at their demonstrated maximum simultaneously, at EUV — undemonstrated.** The wall reopens, at the cost of a hard joint-maximum that no machine has shown.
## Falsifiers
F-DR-1 derate ≥20× (real) · F-DR-2 naive margin <1× (lost) · F-DR-3 headroom ≥ derate · F-DR-4 recovered ≥1× · F-DR-5 both-maxed-at-EUV undemonstrated (honest) · F-DR-6 bounds.
## Honest Limits
L1 the (γθ)²≈BW collection estimate is first-order (real ICS has recoil + laser-bandwidth terms that worsen it); L2 "recovered 30×" assumes the headroom is free of new losses — it is not (higher current → beam-laser overlap, higher finesse → mirror damage); L3 this is the second consecutive wall that reopens only by stacking demonstrated maxima — a signal the compact-ICS path is *possible but margin-thin*, consistent with the funded-form preferring the conventional ERL (H_030).
## Verdict
```
verdict_class: SUPPORTED  (6/6)
derate 50x · naive margin 15x -> 0.3x (LOST) · headroom x100 -> recovered 30x · both-maxed-at-EUV undemonstrated
key_finding: the ICS flux margin does NOT survive bandwidth-limited collection (~50x derate eats the 15x
             margin). It is recoverable only by stacking the demonstrated finesse + current maxima (x100),
             undemonstrated together at EUV. Honest: the compact-ICS path is possible but margin-thin —
             reinforcing why the funded answer is the conventional ERL (H_030), with ICS the longer shot.
honest_note: first-order collection estimate (L1); headroom not loss-free (L2); reopening-by-stacked-maxima
             is a margin-thin signal (L3).
```
**State output**: `state/h036_ics_bandwidth_derate_2026_06_25/result.json`
