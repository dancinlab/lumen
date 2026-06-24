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

## Band verdict census — the compact verdict is REQUIREMENT-driven (H_040, '다음' depletion)
The EUV verdict (compact-coherent = terminal-thin, conventional = robust) does NOT generalize —
it is driven by the *application's flux requirement*, not the wavelength:
```
band            energy     flux need   compact-path verdict
─────────────   ────────   ─────────   ──────────────────────
THz gap         3.4 MeV    modest      WINS (slice-spread irrelevant at long λ, low-E cheap)
EUV litho       511 MeV    EXTREME     terminal-thin  ← the outlier (campaign)
water window    1.08 GeV   moderate    WORKS (bio imaging, lower bar than litho)
hard X-ray      5.94 GeV   moderate    REAL — Lyncean-class compact ICS exists today
nuclear gamma   ~50 MeV    low         REAL — HIGS / ELI-NP compact ICS gamma exist today
```
**EUV-litho is the outlier:** only its extreme in-band flux (~100 W) + tight slice-spread make the
compact path terminal-thin. Everywhere else the wavelength-agnostic engine **wins, works, or already
exists**. So M10 sharpens: the engine is the no-incumbent market's natural source; the compact-vs-
conventional choice is set by the application's flux requirement, and EUV litho is simply the most
demanding rung. **'다음' (other bands) depleted** — the census is complete and the verdict-driver is
identified; further bands only re-apply the same requirement-driven rule.

## SSMB synthesis boundary across bands (H_047, band-fleet)
Applying the compact SSMB-Compton synthesis (H_043-046) to every no-incumbent band splits them into
two regimes by the achievable micro-bunch length (σ_z ~ 3 nm):
```
band            λ        b²      regime           verdict        exists today
─────────────   ──────   ─────   ──────────────   ────────────   ──────────────
THz gap         300µm    1.00    SSMB-coherent    wins           synchrotron THz-FEL
EUV litho       13.5nm   0.14    SSMB-coherent    terminal-thin  none (SSMB-EUV concept)
water window    3nm      ~0      incoherent-ICS   works          synchrotron only
hard X-ray      0.1nm    ~0      incoherent-ICS   real-today     Lyncean compact ICS
nuclear gamma   ~5pm     ~0      incoherent-ICS   real-today     HIGS / ELI-NP
```
**The SSMB coherent-CW breakthrough is TARGETED, not universal:** it applies at λ≳~10nm (THz, EUV) — exactly
where EUV-litho's extreme flux lives — and is unnecessary at the shorter bands, which fall to plain incoherent
inverse-Compton that is **already real** (Lyncean/HIGS/ELI) and suffices at their lower flux needs. Band fleet
depleted: the band-space is mapped into two regimes, the verdict stays requirement-driven (H_040), no new physics.

## The two novel paths share one gate (H_048, rank2,3 assault)
Rank-2 SSMB (undulator) and rank-3 compact SSMB-Compton both gate on the SAME milestone — steady-state
micro-bunching at 13.5 nm precision (σ_z~3nm → b²~0.14, physics-allowed, undemonstrated). Components are
individually demonstrated (SSMB mechanism Nature 2021; Compton real via Lyncean/HIGS/ELI ~1e13 ph/s; IR
cavity finesse 1e4-1e5); only the EUV-precision JOINT operating point is missing. Trade: rank3 (7 MeV,
tabletop) pays the Compton bandwidth-collection flux tax (~50× derate, H_036) that rank2 (511 MeV undulator,
bigger ring) avoids. **One experiment — demonstrate 13.5 nm steady-state micro-bunching — de-risks both.**
