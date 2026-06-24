---
id: H_035
slug: ir-cavity-reclassify
title: Loop cycle-2 breakthrough — the ICS enhancement cavity operates at the IR DRIVE wavelength (finesse 1e4–1e5 routine), NOT at EUV (where multilayer R~0.70 forbids a cavity, finesse ~9); so the H_034 recirculation flux gain rests on demonstrated IR-cavity tech and the margin is robust, not a fragile EUV-cavity problem; honest residual: an integrated high-average-power EUV-ICS source (IR cavity + ERL + MHz sync) is undemonstrated
domain: light-source
status: supported
exploration_method: break→verify→deepen loop, cycle 2 — reclassify the simultaneity wall
verification_method: deterministic harness + 6 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
breaks: H_034 residual (flux-simultaneity / "EUV cavity impossible" worry)
---
# H_035 — cycle-2 breakthrough: the cavity is at IR, not EUV
> The feared wall: "a high-finesse enhancement cavity at EUV is impossible (multilayer R~0.70)." That is a **misclassification**.
## The reclassification
- An EUV cavity at R=0.70 has finesse ~9 — useless (confirms you cannot store EUV).
- But the ICS enhancement cavity stores the **drive laser (1 µm IR)**, where finesse **1e4–1e5 is routine** and demonstrated. The EUV is produced at the collision and extracted once — it never circulates.
- So the H_034 recirculation gain (cavity 1e4 × ERL 1e3) rests on **demonstrated IR-cavity tech** → the flux margin is **robust**, not a fragile EUV-optics problem.
## Honest residual
An *integrated* high-average-power EUV-ICS source — IR enhancement cavity + ERL + MHz bunch/pulse synchronization — is **undemonstrated**; that integration is the real front (deepened in H_036).
## Falsifiers
F-CV-1 cavity at IR drive · F-CV-2 IR finesse ≥1e4 demonstrated · F-CV-3 EUV cavity finesse <100 (forbidden) · F-CV-4 margin rests on demonstrated tech · F-CV-5 integrated EUV-ICS undemonstrated (honest) · F-CV-6 bounds.
## Honest Limits
L1 finesse formula π√R/(1−R) is the ideal two-mirror value; L2 "robust" is about the *basis* (demonstrated IR tech), not that the integrated source exists; L3 IR cavity + high-current ERL beam crossing has its own beam-laser overlap/damage limits not modeled here.
## Verdict
```
verdict_class: SUPPORTED  (6/6)
EUV cavity finesse ~9 (useless) · cavity at 1000nm IR finesse 1e4 (routine) · margin rests on demonstrated tech · integrated EUV-ICS undemonstrated
key_finding: the "EUV enhancement cavity is impossible" objection is a misclassification — the cavity is
             at the IR drive wavelength (high finesse routine), so the H_034 flux-recirculation margin
             stands on demonstrated tech. The real residual is the integrated high-avg-power EUV-ICS source.
honest_note: ideal finesse formula (L1); robust basis != built source (L2); beam-laser overlap limits unmodeled (L3).
```
**State output**: `state/h035_ir_cavity_reclassify_2026_06_25/result.json`
