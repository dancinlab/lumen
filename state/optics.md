# Optics (광학계) — focusing and imaging the source

Pillar 3 of the lumen research hub. The projection optics that shrink and focus the
source onto the wafer. This is where the NA / depth-of-focus trade-off originates,
which then drives the resist (`photochemistry.md`) and source (`light-source-paths.md`)
constraints. Items marked `?` need verification before use.

## The NA ↔ depth-of-focus trade

- **Resolution** (half-pitch) ≈ k₁ · λ / NA — smaller with shorter λ or higher NA.
- **Depth-of-focus** ≈ k₂ · λ / NA² — falls with NA², so raising NA for resolution
  collapses the focus window → ultra-thin resist + tighter focus control.

```
NA ↑   →  해상도 ↑  (좋음)
NA ↑   →  DoF ↓ (NA² 로)  →  레지스트 극박막·초점 제어 난도 ↑  (나쁨)
```

- Current EUV: NA ≈ **0.33** (ASML NXE). High-NA: NA ≈ **0.55** (ASML EXE / "High-NA EUV").
- High-NA uses **anamorphic** optics (different magnification in x/y, 4×/8×) → half-field
  imaging, stitching, throughput implications `?`.

## NA generations (timeline)

NA is the variable that separates EUV generations (source: transcript `euv-yt-2KDLZMG8FAs-transcript.md`):

- **Gen 1** — NA 0.33, first HVM ~**2017**.
- **Gen 2 (High-NA)** — NA 0.55, HVM ramping **2024–2025**; physical resolution ~**8 nm**. Tied to DRAM nodes D1c → D1d → 0a (single-digit-nm features from 0a).
- **Gen 3** — projected **~2035–2039** (~9–10 yr cadence). Source has some information but **almost no surrounding ecosystem** — viability by then is unpredictable, and it is far harder than Gen 1/2.
- **Beyond Gen 3** — "no clear alternative"; this is lumen's central target (the sub-13.5 nm source). See `HYPOTHESES/` H_004/H_006/H_007 (compact-accelerator route).

## Mirror / multilayer challenge

- EUV is absorbed by everything → all-reflective optics with **multilayer mirrors**.
- 13.5 nm: **Mo/Si** multilayers, ~70% reflectivity per mirror; with ~10+ mirrors the
  total throughput budget is already tight.
- ~6.5 nm ("BEUV"): needs **La/B-based** multilayers with **lower** reflectivity →
  more loss per mirror → demands far more source power (ties back to the source wall).

## Open questions

- Throughput math: per-mirror reflectivity × mirror count × source power — where is the
  6.5 nm system-level wall?
- Does High-NA (0.55) buy enough nodes to bridge to whatever comes after EUV, or is it a
  stopgap before the source problem must be solved?
