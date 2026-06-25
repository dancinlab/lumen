# lumen — 검증지식 전수수집 census (2026-06-25)

`lumen` 리포의 검증된 지식 레지스트리를 전수수집(全數)한 인구조사 산출물.
read-mostly harvest — 본 artifact + CHANGELOG 한 줄만 추가, 카드/atom 미수정.

## 1. 레지스트리 인벤토리 (self-discovered)

| 레지스트리 | 경로 | 성격 |
|---|---|---|
| 가설 레지스트리 (flat) | `HYPOTHESES/REGISTRY.jsonl` | SSOT · JSON 1줄/가설 (60줄) |
| 가설 카드 | `HYPOTHESES/cards/H_*.md` | 카드 1개/가설 (frontmatter + 본문) |
| 실행 산출물 | `state/h0*_*_2026_06_*/result.json` | 결정적 run 결과 (verdict 출처, 50개) |
| 공유 물리엔진 | `tool/lumen_optics.py` · `tool/qa.py` | 모든 카드가 import |
| 사람용 원장 | `CHANGELOG.md` (append-only) · `ARCHITECTURE.json` | 이력 + 설계 SSOT |

- embedded atlas(@P/@C/@L … atom) **없음** — lumen 은 가설-검증 시스템(anima `HYPOTHESES/` 모델)이지 atlas atom 리포가 아님.
- `*.verdict*` / 별도 ATLAS/UNIVERSE README **없음**. 단일 레지스트리 = `HYPOTHESES/REGISTRY.jsonl`.

## 2. 전수 census — 측정된 집계 (grep/parse)

총 레지스트리 엔트리: **60** (`wc -l HYPOTHESES/REGISTRY.jsonl` = 60)

| 분류 | 개수 | 비고 |
|---|---:|---|
| 🟢 SUPPORTED (run+verdict, result.json) | **49** | 검증됨 (numbered H_0xx 체인) |
| 🜂 ABSTRACT → 🟢 promoted (검증으로 흡수) | 3 | H_A4→H_012 · H_B1→H_014 · H_B4→H_017 |
| 🔴 FALSIFIED (정직한 음성) | 1 | H_037 |
| 🜂 ABSTRACT still-open (미검증 conjecture) | 7 | H_A1·A2·A3·A5 · H_B2·B3·B5 |
| **합계** | **60** | |

- **검증됨(VERIFIED) = 49** (🟢 SUPPORTED, falsifier 5/5 또는 6/6 PASS · result.json 산출).
- **미검증/추측(ABSTRACT-open) = 7** (run·verdict 없음, falsifiable prediction만).
- **closed-negative(FALSIFIED) = 1** (H_037).
- result.json 산출 파일: **50개** (`find state -name result.json | wc -l`).
- 검증 카드 verdict 의 PASS 매칭: 49줄 (`grep -c PASS`).
- archived: 0.

tier 배지 규약(`HYPOTHESES/CLAUDE.md:31-35`): 🟢 SUPPORTED · 🟡 PARTIAL · 🔴 FALSIFIED · ⚪ PRE-REGISTERED · 🜂 ABSTRACT.
현재 PARTIAL(🟡)·PRE-REGISTERED(⚪) 엔트리는 0개.

## 3. 헤드라인 검증 발견 (VERIFIED 중)

| id | 분류 | 발견 | cite |
|---|---|---|---|
| H_043 | 🟢 NOVEL·reference-matched | SSMB(Steady-State MicroBunching)가 "잃어버린 중간" — 링 빔 재사용 coherent CW가 가속기 파워벽을 깸. 6/6 PASS | `state/h043_ssmb_novel_breakthrough_2026_06_25/result.json` |
| H_033 | 🟢 BREAKTHROUGH | slice-spread 벽을 compact-source 질문에 대해 ICS(역콤프턴, no gain조건·~2MeV·tabletop)로 돌파. 잔여=재배치된 flux벽. 6/6 PASS | `state/h033_ics_breakthrough_2026_06_25/result.json` |
| H_049 | 🟢 in-silico completion | 닫힌형 프론티어 완결 — 8 abstract 흡수·2 experiment-gated·검증 47/47. 남은건 물리실험. 6/6 PASS | `state/h049_insilico_completion_2026_06_25/result.json` |
| H_022 | 🟢 capstone | compact-accelerator 조합(가속기+ERL+FEL+cooling+모듈어레이)이 flux·CAPEX·wavelength 캠페인 벽 동시 돌파. 6/6 PASS | `state/h022_combination_breakthrough_2026_06_25/result.json` |
| H_002 | 🟢 numerical | BEUV(6.5nm) 거울-투과벽: 동일 11-거울 컬럼이 6.5nm서 ~14.19× 적은 광자 통과 → ~14× 소스파워 강제. 5/5 PASS | `state/h002_beuv_mirror_wall_2026_06_24/result.json` |
| H_038 | 🟢 loop convergence | break→verify→deepen 루프 수렴 — compact coherent EUV terminal-thin, ERL이 견고한 litho-power 답. 5/5 PASS | `state/h038_loop_convergence_2026_06_25/result.json` |
| H_050 | 🟢 literature ref-match | 2025-26 arXiv가 캠페인 프론티어 확증 — 닫힌형으로 도출한 cooling lever가 최신 SSMB 프론티어의 OSC와 정확히 일치. 6/6 PASS | `state/h050_literature_refmatch_2026_06_25/result.json` |
| H_037 | 🔴 FALSIFIED(정직음성) | 고휘도 빔이 ICS bandwidth-collection derating을 못 이김 — brightness escape 부재, derating은 근본적. H_038 수렴에 기여 | `state/h037_brightness_lever_falsified_2026_06_25/result.json` |

## 4. 전체 엔트리 목록 (전수 · 60)

검증 체인 H_001–H_050 (H_037만 🔴, 나머지 49개 🟢 SUPPORTED):
H_001 LPP 소스파워 천장 · H_002 BEUV 거울 throughput 벽 · H_003 NA↔DoF 트레이드 · H_004 compact PWFA 가속기 · H_005 HVM throughput floor · H_006 가속기→EUV 광자 · H_007 sub-13.5nm 튜너빌리티 · H_008 가속기-소스 flux 벽 · H_009 빔 에너지스프레드→선폭 · H_010 싱크로트론 vs LPA · H_011 가속기 파장 reach · H_012 spectral gating+grazing 회복 · H_013 에너지스프레드 cooling이 M4 휘도벽 분할 · H_014 no-SPF in-band 회복 · H_015 wall census · H_016 ERL flux floor 재오픈 · H_017 재결합 EUV 레이저 포화 · H_018 ERL BBU 비-구속벽 · H_019 cost-of-ownership 결합 · H_020 real-units COO · H_021 tabletop 학습곡선 CAPEX · H_022 조합 돌파(capstone) · H_023 ERL↔FEL cross-coupling · H_024 cooling vs ρ · H_025 @-family depletion census · H_026 sourced 재검증 · H_027 integration 벽 돌파 · H_028 FEL thin-margin 벽 돌파 · H_029 replicable-module 벽 돌파 · H_030 funded-reality ref-match · H_031 fleet-r2 slice spread · H_032 TGU escape 분류 · H_033 ICS BREAKTHROUGH · H_034 ICS flux deepen · H_035 IR cavity 재분류 · H_036 ICS bandwidth derate(정직음성) · **H_037 brightness lever FALSIFIED 🔴** · H_038 loop convergence · H_039 band generalization · H_040 band verdict census · H_041 cross-tool parity · H_042 non-accelerator landscape · H_043 SSMB NOVEL · H_044 compact SSMB-Compton footprint · H_045 risk localization · H_046 micro-bunching feasibility · H_047 band-SSMB census · H_048 두 novel 경로 공유게이트 수렴 · H_049 in-silico 완결 audit · H_050 fresh-literature ref-match.

미검증 abstract conjecture (🜂 · run/verdict 없음 · 7개):
H_A1 cavity-enhanced 역콤프턴+attosec 타이밍락 · H_A2 compact LPA micro-SASE FEL · H_A3 recirculating micro-storage+cryo undulator · H_A5 all-optical EUV(HHG→plasma-mirror→metasurface) · H_B2 high-cross-section ultrathin resist · H_B3 two-color narrow-arm litho · H_B5 digital photon-counting litho.

promoted abstract (검증으로 승격, 위 49에 포함): H_A4→H_012 · H_B1→H_014 · H_B4→H_017.

## 5. 정직한 gap

- 단일 레지스트리만 존재 — embedded atlas atom·별도 verdict 원장 없음(lumen 은 가설-검증 시스템). 누락 추정 아님, 실측 부재.
- 60개 엔트리 전수 파싱(JSON) — 샘플링 아님. tier 문자열은 자유서술(예: "· BREAKTHROUGH" suffix)이라 정규화 시 SUPPORTED/ABSTRACT/FALSIFIED 3축으로 묶음.
- "검증됨" 정의 = result.json + falsifier all-PASS verdict. ABSTRACT 7개는 falsifiable prediction이나 미실행 — 정직히 미검증으로 분리(승격은 실제 run 통과로만, `HYPOTHESES/CLAUDE.md:33-35`).
- 카드 본문(`cards/H_*.md`)의 falsifier 디테일·honest-limits는 레지스트리 verdict 요약으로 갈음(전수 본문 미전개).
