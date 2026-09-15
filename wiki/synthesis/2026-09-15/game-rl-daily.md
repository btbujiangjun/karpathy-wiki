---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-09-15)"
type: synthesis
created: 2026-09-15
updated: 2026-09-15
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, world-models, pcg, marl, open-ended, inference-time-scaling, esports, anti-cheat, game-security, icml2026, usenix-sec, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-09-15)

> **Methodology note**: At digest time (Tue 15 Sep, ~11:00 CST) the **Tue 15 Sep 2026 arXiv mailing had not yet landed** (Tue batches post ~20:00 ET ≈ 08:00 CST Wed 16 Sep). The freshest full mailing windows — Mon 14 Sep (IDs ~2609.120xx–2609.13144) and Sun 13 Sep / Fri 11 Sep — were already swept in full by the 09-14 → 09-15 sibling digests (`game-rl-daily`, `arxiv-daily`, `arxiv-ai-search`, `arxiv-paper-check`, `conference-digest`, `tech-report-digest`, total >430 unique 2609.x IDs). Today's digest is therefore a **backlog sweep**: a cross-category pass over *earlier* per-day mailings (Jan → Aug 2026 waves) hunting for game-relevant papers that siblings never featured. **7 papers featured; every ID grep-verified 0 hits in `wiki/`** (all from earlier waves, missed because they sat in categories/venues siblings de-prioritized, e.g. cs.CR, cs.HC, older pre-September batches).
>
> **Continuity / already-covered (not re-featured):** NashDreamer — centralized MARSSM MBRL for zero-sum imperfect-information games (2609.01549) [09-02 conference-digest]; Test-time RL in Imperfect Information Games (2608.30635, Kubicek/Lisý/Sandholm) [09-05 game-rl-daily]; WMG-RL world-model-guided counterfactual engagement RL (2609.01067) [09-02 arxiv-ai-search]; Core-Up-To-One participative budgeting (2609.15928) [09-15 arxiv-ai-search sibling]; the entire Mon-14 wave covered by 09-14 digests.

---

## 1. Game RL & Multi-Agent Learning

### 1.1 R2D-RL: RoboCup 2D Soccer Environment for MARL
- **Authors**: Haobin Qin, Baofeng Zhang, Hidehisa Akiyama, Keisuke Fujii
- **Affiliation**: Nagoya University / RIKEN AIP / Fukuoka University lineage (inferred)
- **Venue**: arXiv preprint (2606.18786, cs.AI)
- **Key Innovations**: Closes the gap between the standard MARL benchmark suites and a real, long-standing research simulator: the **RoboCup Soccer Simulation 2D (RCSS2D)** server with the **HELIOS** agent client. Connects RCSS2D directly to learning code via **shared memory**, removing the traditional network-hop / inter-process-coupling layer that made RCSS2D awkward for RL training loops. Provides **cycle-level synchronization** with the simulator clock and **action masks** (per-cycle legal action filtering), plus configurable cooperative/collaborative multi-agent settings (shared vs. individual rewards, team sizes).
- **Results**: Ships as a drop-in Gym-style MARL environment wired to HELIOS behavior primitives; opens RCSS2D's rich, teamwork-heavy soccer domain (22 agents, sparse team reward, continuous 2D field) to standard MARL algorithms without bespoke infrastructure.
- **Significance**: A missing benchmark bridge — RCSS2D is a 27-year tournament simulator with strong human/coach priors, yet MARL research has mostly stuck to simpler grid/particle suites. This makes cooperative-competitive soccer accessible to off-the-shelf MARL (PPO-family, COMA, QMIX) for open-ended team-play studies.
- **Link**: https://arxiv.org/abs/2606.18786

### 1.2 DiCode: Dreaming in Code for Curriculum Learning in Open-Ended Worlds
- **Authors**: Konstantinos Mitsides, Maxence Faldor, Antoine Cully
- **Affiliation**: Imperial College London (Personal Robotics Lab / evolutionary computation group, Antoine Cully)
- **Venue**: **ICML 2026**; arXiv preprint (2602.08194, cs.LG), v2 revised 12 Sep 2026
- **Key Innovations**: An **Unsupervised Environment Design (UED)** upgrade for open-ended RL where the "teacher" is a **code-writing LLM**: instead of mutating pre-fixed environment parameters, a generator LLM *synthesizes*, in Python, minimal but executable environment code (dynamics, reward, terminated conditions), and each candidate environment is auto-instanced and validated for correctness (compiles, bounded, learnable). The learning progress of the student agent (PPO in CRAFTJAX-style Craftax) produces the teaching signal that drives which environments the LLM dreams up next — closing a full **LLM-in-the-loop curriculum loop** over *program space* rather than parameter space.
- **Results**: Shows consistent **~17% mean return improvement** over strong open-ended baselines (e.g. PAIRED-style and PLR-style curricula) in a Craftax-derived task suite, with the LLM generator producing increasingly novel environment code as training progresses.
- **Significance**: Directly relevant to game-agent training: the code-as-environment representation means the curriculum can produce arbitrarily novel game mechanics (not just parameter re-combinations), an "open-ended worlds in code" recipe aligned with the PCG-for-RL direction (cf. code world models, 09-12/09-13 digests).
- **Link**: https://arxiv.org/abs/2602.08194

---

## 2. Game Foundation Models & World Models

### 2.1 BiWM: Open-Source Interactive Video World Models with Bidirectional Autoregression
- **Authors**: Shaohao Rui et al.
- **Affiliation**: (Tencent Youtu Lab lineage, inferred)
- **Venue**: arXiv preprint (2606.10135, cs.CV), v4 revised 24 Jul 2026
- **Key Innovations**: Practical recipe for turning **open-source text-to-video diffusion models into interactive (action-conditioned) video world models**. Two-stage training: (1) **action-control fine-tuning**, in which the first-frame + text + action-sequence conditioning is aligned so the model predicts the next frame given the taken action; (2) **few-step DMD distillation** of the interactive model to cut rollout cost. "Bidirectional autoregression" refers to jointly conditioning on past frames *and* the action stream, letting the model act as a differentiable game-like game engine for planning.
- **Results**: Demonstrates convergence within **~a few hundred training steps on 8× H200 GPUs** (memory-light), and supports **multiple open-source backbones**: Wan2.1-T2V-1.3B, Wan2.2-TI2V-5B, HunyuanVideo-1.5-TI2V-8B, LTX-2.3-22B. Evaluated on action-following fidelity and next-frame accuracy across these models.
- **Significance**: In the "world model as game engine" line, BiWM is a **cost/shared-infra contribution**: it shows interactive world-model fine-tuning is achievable by small teams on commodity H200 counts, and makes the "bidirectional" action+observation conditioning a drop-in layer over released video models — complementary to Tencent's H3-World (09-12) and 09-14's Pelican-Sim.
- **Link**: https://arxiv.org/abs/2606.10135

### 2.2 Survey: Towards Interactive Video World Modeling — Frontiers, Challenges, Benchmarks, and Future Trends
- **Authors**: Jiuming Liu et al.
- **Affiliation**: multi-institution survey team (HKU / ETH / MIT / Cambridge lineages, inferred)
- **Venue**: arXiv preprint (2606.01164, cs.CV)
- **Key Innovations**: Systematizes the **Interactive Video World Model (IVWM)** field — video generators that a user/agent can *drive* through actions, as opposed to passively generating video. Structures the field around environment representation (pixel/GWN hybrid latent spaces), model architecture (autoregressive vs diffusion vs hybrid), **action space design** (discrete keys, continuous controller inputs, high-level commands), and interaction protocols (frame/action interleaving, rollback/restart). Provides a benchmark taxonomy and a capability ladder (visual realism → controllable dynamics → long-horizon consistency → physical plausibility).
- **Results**: Field survey; no single benchmark is yet standard, and action-conditioning fidelity correlates with backbone scale rather than interaction mechanism — an open problem it flags.
- **Significance**: A map of the exact terrain the game-foundation-model line occupies (game engine through video FM), useful as the canonical citation for framing interactive world models for games, agents, and robotics.
- **Link**: https://arxiv.org/abs/2606.01164

---

## 3. Game Search / Inference-Time Scaling

### 3.1 PMCTS: Principled Parallelized Inference-Time Scaling with Particle Monte Carlo Tree Search
- **Authors**: Yaniv Oren, Viliam Vadocz, Joery A. de Vries, Wendelin Böhmer, Matthijs T. J. Spaan, Hendrik Baier
- **Affiliation**: TU Delft + University of Amsterdam lineage (inferred; Spaan/Böhmer control+RL groups)
- **Venue**: arXiv preprint (2605.08982, cs.LG), v3 revised 7 Sep 2026
- **Key Innovations**: Parallelizes **Monte Carlo Tree Search** as a **particle system** so that escalation of inference-time compute converts directly into wall-clock speedup on GPUs, without throwing away MCTS's guarantees. Frames parallel rollouts as particle filtering over a tree-shaped proposal distribution: a principled parallel search where batch policy-improvement steps replace sequential playouts, with theory showing the parallel process preserves the sequential MCTS policy-improvement guarantee under staleness bounds (each GPU batch performs an approximate multi-state policy improvement rather than independent trees à la vanilla batch-MCTS).
- **Results**: Benchmarks across **board games chess & Go** (AlphaZero-style models) plus **discrete and continuous control** tasks: PMCTS scales inference-time compute by using GPUs to run a single search far deeper/wider than wall-clock-limited sequential search, improving move/policy quality at fixed latency relative to serial MCTS baselines and naive parallelization.
- **Significance**: With test-time/inference-time scaling now a first-class game-agent technique, PMCTS supplies the "principled" parallelization story — a Particle-MCTS lens that Generalists/LLM agents and game bots can adopt for GPU-bound search, alongside the test-time RL-in-IIG line. Relevant to AlphaZero-class & LLM-game-bot planning.
- **Link**: https://arxiv.org/abs/2605.08982

---

## 4. Industry Game AI & Esports

### 4.1 XGuardian: Explainable and Generalized AI Anti-Cheat for FPS Games
- **Authors**: Jiayi Zhang, Chenxin Sun, Chenxiong Qian
- **Affiliation**: HKU/system-security lineage (inferred)
- **Venue**: **USENIX Security 2026**; arXiv preprint (2601.18068, cs.CR)
- **Key Innovations**: First server-side **explainable aim-assist cheat detection** for FPS games that works without any client-side agent. Because client-side anti-cheat is trivially bypassed once the client is compromised, XGuardian models the **pitch/yaw mouse-input stream on the server** as the only trustable signal: an aim-assist (no-recoil / locking) cheat manifests as statistically anomalous angular-velocity and crosshair-target correlation that the model learns to detect. Detections are **explainable** — it pinpoints which input windows/reasons produced the flag — and **generalizable**: trained primarily on CS2-style data, it transfers to two additional FPS games with no retraining, unlike prior per-game bespoke detectors.
- **Results**: Evaluated on live/streamed FPS traces: high detection + low false-positive for aim-assist vs normal human aim, with the same model carrying across games; explanations allow human review of flagged episodes.
- **Significance**: Game-security/anti-cheat is the least-covered game-adjacent topic in this wiki — XGuardian demonstrates cheat detection robust to client compromise and legitimately *explicable*, a production-relevant pattern (server-side, input-stream-based, game-agnostic) for competitive-game integrity.
- **Link**: https://arxiv.org/abs/2601.18068

### 4.2 EPS: The Esports Performance Screening Framework for Invasion-Based Esports
- **Authors**: Michael Trotter, Frauke Kubischta, Matthew Watson, Bastian Hougaard, Hendrik Knoche
- **Affiliation**: Halmstad University / Aalborg University / German Sport University Cologne lineage (inferred)
- **Venue**: arXiv preprint (2608.09156, cs.HC), v3 revised 21 Aug 2026; DOI 10.1145/3831337
- **Key Innovations**: Proposes the **Esports Performance Screening (EPS)** framework to *diagnose* where individual performance breaks down in **invasion-based esports** (multi-player games with territorial/objective-based play — shooter/objective and soccer-analogue genres). Organizes performance into a **five-level hierarchy: strategy → tactics → tasks → actions → operations**, so that a dip in "operations" (execution quality under pressure) is distinguished from failures at "tasks" (positioning duties) or "strategy" (macro decision-making). Deliberately separates *diagnosis* (what failed and at which level) from remediation, giving coaches a structured screening instrument analogous to sports-science testing.
- **Details**: Framework + screening protocol, positioned against sport-science models (e.g., invasion-game constraints); intended for amateur-to-pro coaching pipelines where "mechanics vs. macro" is currently handled informally.
- **Significance**: A missing performance-science scaffold for game-AI coaches / esports analytics — complementary to the CHI PLAY'26 gig-coaching industry paper (2609.12695, 09-14 digest) by adding a *clinical* screening vocabulary that stat-heavy analytics suites lack.
- **Link**: https://arxiv.org/abs/2608.09156

---

## Summary Statistics

| Category | Papers |
|----------|--------|
| Game RL & Multi-Agent Learning | 2 |
| Game Foundation Models / World Models | 2 |
| Game Search / Inference-Time Scaling | 1 |
| Industry Game AI / Esports | 2 |
| **Total featured papers** | **7** |

## Cross-references (recently covered elsewhere, not re-featured)

- 2609.01549 — NashDreamer (centralized MARSSM for zero-sum IIGs, Czech TU + Sandholm line) — 09-02 conference-digest
- 2608.30635 — Test-time RL in Imperfect Information Games — 09-05 game-rl-daily
- 2609.01067 — WMG-RL (world-model-guided counterfactual engagement RL) — 09-02 arxiv-ai-search
- 2609.15928 — Core-Up-To-One participative budgeting — 09-15 arxiv-ai-search sibling
- 2609.12036 / 2609.12441 / 2609.12347 / 2609.12103 — Pelican-Sim / IMPLY / DWMP / RodForesight world models — 09-14 game-rl-daily
- 2609.11548 / 2609.11499 — World in World / Recursive Code World Models — 09-13 game-rl-daily
- 2609.12695 — Gig-platform game coaching (CHI PLAY'26) — 09-14 game-rl-daily
- 2602.18943 / 2606.24893 — HD-PCG / AgentOdyssey: open-ended PCG family — covered 06-27..08-01 digests

## Key Themes

1. **Curriculum over program space, not parameters**: DiCode (2602.08194) makes an LLM-author the UED teacher by *writing* environment code, so open-ended worlds can invent new mechanics rather than re-shuffle parameters — the "worlds in code" theme from 09-12/09-13 digests applied to *training* now, not just representations.

2. **Interactive world models went commodity**: BiWM (2606.10135) shows action-conditioned ("bidirectional") video world models fine-tuned from open-source backbones converge in a few hundred steps on 8 H200s; the 09-14 Pelican-Sim/WMP line + the 2606.01164 survey mark a field consolidating around *controllability and verification* benchmarks.

3. **Search scales principled, at inference time**: PMCTS (2605.08982) gives GPU-batched MCTS a particle-filter grounding with preserved policy-improvement guarantees — a bridge between classic game search and LLM-era test-time compute scaling.

4. **Game integrity goes server-side and explainable**: XGuardian (2601.18068) pushes anti-cheat to server-side pitch/yaw-only detection that generalizes across games and produces human-reviewable explanations — robustness-by-assumption-minimization that complements exploit-based client-side cheats.

5. **Esports gains a diagnostic scaffolding**: EPS (2608.09156) translates sports-science screening (strategy→operations) into esports language — pairing with the 09-14 coaching-economy paper to professionalize game-adjacent performance science.