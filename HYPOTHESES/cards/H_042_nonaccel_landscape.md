---
id: H_042
slug: nonaccel-landscape
title: Non-accelerator landscape / first-peak check (gap top-3 #2) — surveying the NON-accelerator EUV families against the ~100 W HVM flux floor (HHG 0.30×, DPP 0.0004×, all-optical 0.001×, recombination 0.02×) shows NONE reaches HVM, while the accelerator FEL clears it 40×; so 'accelerator is the answer' is NOT a first-peak artifact — it survives the head-to-head — with the honest nuance that the COMPACT accelerator wins on WAVELENGTH (the dial), not power, the flux wall (H_008) staying binding and the FEL/conventional form clearing power
domain: system
status: supported
exploration_method: gap-fleet lane 2 — non-accelerator family census vs the HVM floor
verification_method: deterministic harness + 6 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
closes: gap landscape / first-peak
---
# H_042 — non-accelerator landscape (the first-peak check)
> The verified spine committed to the accelerator family early (CERN seed). Was that a first-peak bias, or does it survive a real comparison with the non-accelerator families?
## The census (demonstrated in-band power / ~100 W HVM floor)
HHG (gas) 30 W = **0.30×** · DPP (discharge Xe) 0.04 W = **0.0004×** · all-optical cascade ~0.1 W = **0.001×** · recombination laser ~2 W = **0.02×**. **Zero non-accelerator families reach HVM.** The accelerator FEL (1–10 kW) clears it **~40×** — the only survivor.
## Verdict — survives, with an honest nuance
'Accelerator is the answer' is **not a first-peak artifact**: no non-accelerator family clears the flux floor. But the honest nuance the comparison surfaces: the **compact** accelerator wins on **wavelength** (the dial 13.5/6.5/3 nm in one machine), NOT on power — the **flux wall (H_008) stays binding**, and it is the FEL/conventional form that clears power (consistent with H_030/H_040). So the campaign is reconfirmed, not refuted; the first-peak worry resolves to "justified on wavelength, and the power wall was always the real one."
## Falsifiers
F-LS-1 HHG <floor · F-LS-2 DPP <floor · F-LS-3 no non-accelerator clears (not first-peak) · F-LS-4 FEL clears (survivor) · F-LS-5 compact wins wavelength not power (H_008 reconfirmed) · F-LS-6 bounds.
## Honest Limits
L1 demonstrated-power figures are public-order, 2025–2026 snapshot (China LDP ~100–150 W is the closest non-accelerator riser — track WPH not raw W); L2 "HVM floor ~100 W" is the conservative throughput floor (H_005); L3 this compares SUPPLY families, not full per-tool economics (that is H_021/H_040).
## Verdict
```
verdict_class: SUPPORTED  (6/6)
0 non-accelerator families reach the ~100W HVM floor (HHG 0.30x, DPP 4e-4x); FEL clears 40x (only survivor); compact wins wavelength not power
key_finding: the accelerator answer survives the first-peak check — no non-accelerator EUV family reaches
             HVM power. Honest nuance: the compact accelerator wins WAVELENGTH not power; the flux wall
             (H_008) is the real one, cleared by the FEL/conventional form. Reconfirms, not refutes.
honest_note: public-order 2025-26 snapshot, China LDP the closest riser (L1); conservative floor (L2);
             supply-family compare not full economics (L3).
```
**State output**: `state/h042_nonaccel_landscape_2026_06_25/result.json`
