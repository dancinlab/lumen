# Changelog

All notable changes to lumen are recorded here (append-only).

## Unreleased

- Run **H_011 accelerator wavelength reach** (🟢 SUPPORTED, 5/5, deterministic):
  no theoretical short-wavelength floor — λ ~ 1/E² walks EUV→water-window→X-ray
  (0.5/1/2/5/10 GeV → 11.75/2.94/0.73/0.12/0.03 nm; 3 nm@0.99 GeV, 1 nm@1.71 GeV,
  0.1 nm@5.42 GeV). Single-stage LPA (≤1 GeV) reaches ~3 nm, a few stages (≤2 GeV)
  ~1 nm; the binding wall is flux (H_008) / beam quality (H_009), not wavelength.
  Answers "이론상 몇 nm까지?". Note line added to `state/light-source-paths.md`.

- Run three more hypotheses (all 🟢 SUPPORTED, deterministic) — the honest walls
  that balance the accelerator chain: **H_008 flux/average-power wall** (at present
  LPA rep rates in-band EUV power is ~10³–10⁵× below the ~167 W for 100 WPH → the
  compact path is flux-limited, not wavelength-limited), **H_009 beam-quality
  linewidth** (~1% energy spread → ~2.24% line > 2% in-band budget, swamps
  harmonics), **H_010 synchrotron vs LPA** (storage ring meets HVM power but ~4
  EUV-tools cost + ~200× footprint; landscape is a footprint↔throughput trade).
  Added `power_for_throughput`, `average_power`, `undulator_natural_linewidth`,
  `energy_spread_broadening` to `tool/lumen_optics.py`; "compact-accelerator open
  walls" map + H_006/H_007 lines in `state/light-source-paths.md`.

- Extract YouTube transcript (`sidecar research yt`, EUV source-problem talk) to
  `state/euv-yt-2KDLZMG8FAs-transcript.md`; fold new facts into the pillar notes —
  `light-source-paths.md` (HVM ≈100 WPH throughput floor + LDP <60 WPH gap, 6.5 nm
  Gd/Lu/La candidates, LPP mechanism detail), `optics.md` (NA generation timeline:
  Gen1 0.33/2017 → Gen2 0.55/2024–25/8 nm → Gen3 ~2035–39 → beyond = no alternative).

- Run three more hypotheses to verdict (all 🟢 SUPPORTED, 5/5 falsifiers, deterministic),
  extending the accelerator path and the sub-13.5 nm question:
  **H_005 HVM throughput floor** — at the same source 6.5 nm prints only ~11 WPH vs the
  ~100 WPH floor (1/14 photons → 1/14 throughput); restoring it needs ~2.4 kW (beyond
  H_001) → throughput/economics wall. **H_006 accelerator→EUV photons** — undulator makes
  13.5 nm at ~0.47 GeV (single-stage LPA reach), inverse-Compton at ~2 MeV; closes H_004's
  electron→photon gap. **H_007 sub-13.5 nm tunability** — the same undulator spans
  13.5/6.5/5/3 nm at 466/672/766/990 MeV (~2.1× energy dial, all ≤1 GeV); shorter
  wavelength is an electron-energy knob, not the LPP emitter(Sn→Gd/Lu/La)+multilayer
  (Mo/Si→La/B) double-swap. Added `hvm_throughput_wph`, `lorentz_gamma`,
  `undulator_wavelength`, `energy_for_undulator_wavelength`, `inverse_compton_wavelength`
  to `tool/lumen_optics.py`; updated ARCHITECTURE harness + compact-accelerator nodes.

- Rename `UNIVERSE/` → **`HYPOTHESES/`** (folder) and its registry `HYPOTHESES.jsonl`
  → `REGISTRY.jsonl` (avoid `HYPOTHESES/HYPOTHESES.jsonl` redundancy); all references
  updated (cards · CLAUDE.md · ARCHITECTURE.json · harness docstrings · `source` field).

- Run three more hypotheses to verdict (all 🟢 SUPPORTED, 5/5 falsifiers each):
  **H_001 LPP source-power ceiling** — representative LPP budget (~250 W → ~1.5 kW
  pushed) falls ~2 kW short of the ~3.5 kW the 6.5 nm optics demand (H_002 ×14)
  requires → LPP power-scaling alone insufficient for 6.5 nm (engineering-horizon,
  reopenable). **H_003 NA↔DoF trade** — NA 0.33→0.55 prints 1.67× finer but loses
  2.78× focus depth (= (NA_hi/NA_lo)²); DoF penalty strictly steeper than resolution
  gain (geometric root of the thin-resist wall). **H_004 compact accelerator** —
  Dawson wave-breaking field E₀=96.159 GV/m **reference-matched to dancinlab/demiurge
  cern-accelerator** (`hexa-lang/stdlib/cern/plasma_wakefield.hexa`, |Δ|=0); ~3200×
  conventional RF → reaches 1 GeV in ~1 cm vs ~33 m, the compactness enabler for a
  tabletop accelerator-driven EUV source ("no CERN required"; photon-generation
  downstream). Added accelerator primitives (`plasma_omega`, `wavebreak_field`,
  `accelerator_length`) to `tool/lumen_optics.py`; `light-source.compact-accelerator`
  node to ARCHITECTURE.json; compact-LPA path row + verified-findings block to
  `state/light-source-paths.md`.

- Add **HYPOTHESES hypothesis-verification system** (modeled on anima's `HYPOTHESES/`):
  `HYPOTHESES/REGISTRY.jsonl` registry + `HYPOTHESES/cards/H_*.md` (frozen pre-registration
  + ≥5 measurable falsifiers + honest limits + verbatim verdict) + `cards/_TEMPLATE.md`.
  Shared runnable harness lives in repo-root **`tool/lumen_optics.py`** (deterministic,
  stdlib-only physics: mirror-chain throughput, source-power multiplier, NA↔DoF, LPP power
  budget, falsifier ledger) per anima-parity. First card **H_002 BEUV mirror-throughput
  wall** run to verdict: a 6.5 nm La/B column (R=0.55) passes ~14× fewer photons than a
  13.5 nm Mo/Si column (R=0.70) at the same 11 mirrors → ~14× source-power demand;
  **SUPPORTED, 5/5 falsifiers PASS** (`state/h002_beuv_mirror_wall_2026_06_24/`).
  **H_001 LPP source-power ceiling** pre-registered/frozen (still-to-run, no verdict).
  Added `verification` node + `dataflow.verify` to ARCHITECTURE.json; folder guides for
  `HYPOTHESES/` and `tool/`.

- Choose form = **research hub**. Tree = table of contents, `state/` = per-pillar
  research. Added `state/light-source-paths.md` (LPP/DPP/LDP/synchrotron/FEL comparison
  table + sub-13.5 nm prospects), `state/photochemistry.md` (resist / stochastics /
  thin-film), `state/optics.md` (NA↔DoF, multilayer mirrors). Filled ARCHITECTURE.json
  `dataflow` node (input → curate-by-pillar → output).


- Define direction: lumen targets the next-generation semiconductor-lithography
  light-source problem (EUV 13.5 nm first; the sub-13.5 nm / 6.5 nm stable-source gap
  is the central target). Filled ARCHITECTURE.json overview (scope + core dilemma:
  roadmap gap, NA-vs-DoF, shorter-wavelength source) and components (three reference
  fields: light-source, photochemistry, optics). Added first state artifact
  `state/euv-source-problem.md` (sourced reference note).


- Scaffold the `lumen` project: standard `src/` + `state/` layout, with the architecture SSOT as
  `ARCHITECTURE.json` (JSON `children` tree) + `architecture.html` viewer + `serve.py`, plus
  CHANGELOG/CLAUDE docs. Scope framed as the general "engineer a light source nature does not
  stably provide" problem, with EUV (13.5 nm) as the first instance.
