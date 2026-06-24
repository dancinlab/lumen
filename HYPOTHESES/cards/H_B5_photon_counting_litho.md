---
id: H_B5
slug: photon-counting-litho
title: Digital photon-counting litho — a Geiger-mode resist + photon-counting metrology converts dose-to-clear into a counting problem, printing at ⟨5 photons/pixel⟩ if per-photon gain >10³
domain: photochemistry
tier: 🜂 ABSTRACT (unverified · falsifiable prediction)
status: abstract-conjecture
unverified: true
since: 2026-06-25
scope: ⚠️ Imagination, not a finding — frontier-divergence coordinate. No run, no verdict.
---

# H_B5 — digital photon-counting litho

> **🜂 ABSTRACT.** Brainstorm shortlist (`state/resist-laser-brainstorm.md`, C4). Unverified.

## Which wall
Stochastics/dose — beat the Poisson shot-noise floor that caps a starved source at small pitch.

## Principle
Make each absorption a discrete, amplified, latched "hit" (Geiger-mode resist) and pair it with
photon-counting dose metrology + flicker-aware dosing. The pattern becomes a map of counted hits
and develop is a threshold on count — removing analog dose-to-clear and its shot-noise penalty.

## Falsifiable prediction
With per-photon gain > 10³, reliable printing at ⟨5 photons/pixel⟩ with < 1 ppm pixel error, even
under ±20% source jitter. If gain spreads laterally and blurs the count map below CD spec, falsified.

## How it would be tested
Poisson defect model at ⟨N⟩ photons/pixel with single-photon gain + lateral-blur kernel vs the
1 ppm defect bar; compares analog dose-to-clear vs counted-threshold. Not run here.

## Honest status
Unverified (🜂), most speculative resist bet; single-photon gain >10³ without lateral blur is the
crux (the same blur that helps edges, H_009-analog, hurts pixel isolation).

## Cross-links
- beats: stochastic floor (photochemistry.md RLS). complements: starved source (H_008). source: `state/resist-laser-brainstorm.md`.
