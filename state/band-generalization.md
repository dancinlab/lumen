# Band generalization — EUV is the first instance, not the boundary (H_039 · M10)

> lumen's scope is the **source problem**, not one wavelength. The verified EUV machinery
> (accelerator → undulator/ICS → wavelength dial λ ∝ 1/γ²) generalizes across the spectrum.

## The energy ladder (one undulator, K=1, 18 mm period; dial the electron energy)
```
band                         electron energy   stable natural emitter?
─────────────────────────    ──────────────    ──────────────────────
THz gap (1 THz · 300 µm)     3.4  MeV          NO  ← engine's market
far-IR (30 µm)               10.8 MeV          yes (thermal/QCL)
EUV (13.5 nm)                511  MeV          NO  ← the campaign
water window (3 nm)          1.08 GeV          NO  ← bio imaging
hard X-ray (0.1 nm)          5.94 GeV          NO  (synchrotron-only)
```
One machine spans **6.5 orders of magnitude** in wavelength; EUV is one rung.

## What generalizes — and what doesn't (honest)
- **The dial generalizes freely** (H_039): λ ∝ 1/γ², so any band is a choice of electron energy + extraction (undulator for long λ at low energy; ICS for short λ by laser up-shift).
- **The walls generalize too** (so this is not a free lunch): at every band the campaign's wall
  structure recurs — wavelength is free, the binding wall is **flux** + the extraction tax. For an
  FEL it is the **slice-spread** wall (→ needs a conventional ERL, H_031/032); for ICS it is the
  **bandwidth-collection tax** (fundamental, H_037). So the EUV conclusion transfers: the robust
  high-average-power form in any no-emitter band is the **conventional accelerator-driven source**,
  with the compact-coherent variant terminal-thin (H_038).
- **The incumbent matters**: where a stable natural/compact emitter already exists (far-IR: thermal
  sources, QCLs; visible/near-IR: lasers) the engine has no opening. Its market is exactly the
  **no-stable-emitter bands** (THz gap, EUV, water window, hard X-ray, nuclear γ via ICS) — **M10**.

## Meta-law M10 (frozen prediction)
**The wavelength-agnostic accelerator engine wins precisely the bands that lack a stable natural
emitter.** Falsifiable: name a band with NO stable compact emitter that the accelerator+undulator/ICS
dial cannot reach below ~10 GeV — none is known across THz→hard-X-ray. The EUV campaign is M10 evaluated
at the 13.5 nm rung; the same verdict structure (dial free · flux wall · conventional form robust)
recurs at every other rung.
