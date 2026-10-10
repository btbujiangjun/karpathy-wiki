---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-10-10)"
type: synthesis
created: 2026-10-10
updated: 2026-10-10
sources: [arxiv.org]
tags: [game-rl, game-ai, llm-agents, foundation-models, world-models, pcg, benchmarks, self-play, multi-agent, game-theory, hierarchical-rl, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-10-10)

> A **spot-check digest across all seven lanes** (Game RL, Game AI Bot, Game Foundation Models, PCG, Benchmarks, Industry Game AI, Related Techniques), compiled from targeted arXiv abstraction sweeps + web searches run for this digest. **Method note up front**: this edition is *not* a full export-API window enumeration (the 2026-10-08 announcement block was already claimed by today's sibling digests `arxiv-daily.md`, `arxiv-paper-check.md`, `arxiv-ai-search.md`, whose own Games sections report **zero fresh in-window game-playing RL papers and zero CTR papers**). Instead it surfaces the **strongest recent game-RL/game-AI papers across the 2602→2609 ID range** not re-featured since the September digests, plus five **fully-fresh** items (0 hits anywhere in the wiki). Every featured ID was grep-verified: **0 hits in `wiki/synthesis/2026-10-10/`**; 5 of 18 are **0 hits repo-wide**; the remaining 13 are already documented in earlier digests and are detailed here for continuity with an explicit note.

---

## §0 Method and Corpus

### 0.1 Coverage
- **No fresh in-window game papers to claim.** The 2026-10-08 announcement block (`2610.10537+`) was harvested today by sibling digests and contains **no unclaimed game-playing-RL paper** (declared in-both `arxiv-daily.md` §6 and `arxiv-paper-check.md`). PCG/industry-game-AI found nothing new in-window either. This digest therefore **re-mines the recent back-catalog** (`2602.*`–`2609.*`) across the seven requested lanes.
- **Boundary**: all featured IDs ≤ `2609.25001` (latest submission date ~2026-09-21). Deliberately **no catch-up of `2610.*`** — that space is sibling-claimed for 10-09/10-10.

### 0.2 Sweep
1. **Web/targeted searches** across: Game RL (self-play, PPO, imperfect information), Game AI Bot / LLM+RL NPC, Game Foundation Models / generalist agents, PCG (level gen, LLM, PCGRL), Game Benchmarks (Minecraft, NetHack, ARC), Industry Game AI (real-time inference, pipelines), Related (world models, curiosity, HRL, offline RL).
2. **arXiv abs-page pulls** for every refined candidate to lock authors + submission dates.
3. **Dedup** — each candidate ID `rg`-grep'd against the whole `wiki/` (**18 featured: 5 fresh / 13 documented-and-refeatured**) and against `wiki/synthesis/2026-10-10/` (**0 hits for all 18**).

### 0.3 Dedup accounting (featured set)
| arXiv ID | In wiki total | In today's dir |
|----------|--------------:|---------------:|
| 2604.20381 (QDHUAC) | 0 | 0 |
| 2607.04409 (Task-Sufficient WMs) | 0 | 0 |
| 2609.05650 (Endogenous Curiosity) | 0 | 0 |
| 2602.00460 (SIERL) | 0 | 0 |
| 2506.21039 (SSE) | 0 | 0 |
| 2606.23348 (Generals.io) | 14 | 0 |
| 2604.05476 (Tablut) | 10 | 0 |
| 2605.30931 (MineExplorer) | 8 | 0 |
| 2603.07106 (AutoUE) | 6 | 0 |
| 2605.28863 (Big Two) | 5 | 0 |
| 2510.04862 (Multi-agent PCGRL) | 5 | 0 |
| 2607.29218 (MirrorCraft) | 4 | 0 |
| 2604.20209 (SGS) | 3 | 0 |
| 2609.25001 (GameHorizon) | 3 | 0 |
| 2605.16315 (Structural Threshold) | 3 | 0 |
| 2605.19235 (VRPO) | 2 | 0 |
| 2604.25318 (Cutscene Agent) | 1 | 0 |
| 2606.06565 (AI LOD) | 1 | 0 |

### 0.4 Affiliations and venues
- **Abs-page pulls do not print affiliations.** Where an institution could not be read from the paper's own author block/thanks, it is marked **"not stated"** and **not inferred** from surnames or email domains (standing wiki discipline). Inferred affiliations appear only as **"⚠️ inference from public author records — tentative"**, never asserted as fact.
- Venues are stated **only where the venue is explicit** in the source (e.g., `SIGGRAPH Technical Workshops 2026`); otherwise `arXiv preprint`. **No result independently replicated.**

---

## §1 Game RL — Reinforcement Learning in Games

### ★★★ Superhuman AI for Generals.io Using Self-Play Reinforcement Learning
- **Authors**: Matej Straka, Viliam Lisý, Martin Schmid
- **Affiliation**: ⚠️ not stated on abs page; *not inferred* (Czech research-team authorship per public records — tentative).
- **Venue**: arXiv:2606.23348 (22 Jun 2026) — `cs.AI`/`cs.LG`.
- **Link**: https://arxiv.org/abs/2606.23348
- **Abstract and key innovations**: a JAX-simulated **Generals.io** 1v1 agent trained purely by self-play PPO reaches **superhuman** play (RTS-style fog-of-war strategy game). The custom simulator runs at **tens of millions of environment steps/second (~10,000× faster)** than prior implementations, letting a ViT policy train in ~4 days on 4×H200. Training uses self-play policy-gradient with **top-advantage sample filtering** and an **EMA of policy parameters** (stabilizing the changing adversary). The final agent reached **#1 on Generals.io's public 1v1 leaderboard (5,000+ human players)** and beat the top human players **199–70**.
- **Why it matters here**: the strongest recent result in the wiki's *self-play-at-game-scale* line and the clearest demonstration that **RL, not LLM/agent scaffolding, still owns board/video-game mastery at the top end** — and that cheap JAX simulators multiply compute-constrained research.
- **Caveats**: already in wiki (14 hits) from an earlier digest — re-featured for the lane overview; single-game scope; human-result sample sizes not independently verified.

### ★★ Self-Play Reinforcement Learning under Imperfect Information in Big Two
- **Authors**: Aalok Patwa
- **Affiliation**: ⚠️ not stated (single-author; no institution printed).
- **Venue**: arXiv:2605.28863 (v2 28 Jun 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2605.28863
- **Abstract and key innovations**: systematic comparison of self-play RL algorithms in **Big Two** (4-player, imperfect-information trick-taking card game with large branching): **PPO outperforms Monte-Carlo Q, SARSA and Q-learning** under self-play; **entropy regularization** materially helps; **current-policy self-play** is the best opponent curriculum (outperforming playing against older/random selves). Practical ablations on reward shaping and exploration for a realistic imperfect-information card game.
- **Why it matters here**: fills the wiki's *classical imperfect-information card games* lane with a clean algorithm-vs-algorithm result that mirrors **Tablut**'s (below) themes of self-play stability.
- **Caveats**: already in wiki (5 hits) from an earlier digest; single-card-game scope, no human baseline.

### ★★ Reproducing AlphaZero on Tablut: Asymmetry-Breaking and Training Stability in Zero-Shot Self-Play
- **Authors**: Tõnis Lees, Tambet Matiisen
- **Affiliation**: ⚠️ not stated on abs page; *not inferred* (Estonian authorship per public records — tentative).
- **Venue**: arXiv:2604.05476 (7 Apr 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2604.05476
- **Abstract and key innovations**: reproduces an **AlphaZero-style** training pipeline on **Tablut** (asymmetric, two-role "Tafl" game) and attacks its self-play training collapse. Key fixes: **separate policy/value heads per player role sharing a single residual trunk**, **C4 rotation augmentation**, a **larger replay buffer**, and **~25% of self-play games against past checkpoints** — together addressing catastrophic forgetting in the asymmetric setting.
- **Why it matters here**: the *asymmetric-role self-play stability* lesson transfers directly to any asymmetric game/NPC setting (attacker vs defender). Complements the imperfect-information lines (§1 above) on the same stability axis.
- **Caveats**: already in wiki (10 hits) from an earlier digest; no frontier-model baseline (classical AlphaZero nets).

### ★★ GAE Falls Short in Imperfect-Information Self-Play RL (VRPO)
- **Authors**: Zhiyuan Fan, Gabriele Farina
- **Affiliation**: ⚠️ not stated on abs page; *not inferred* (MIT-aligned authors per public records — tentative).
- **Venue**: arXiv:2605.19235 (19 May 2026) — `cs.LG`.
- **Link**: https://arxiv.org/abs/2605.19235
- **Abstract and key innovations**: shows **Generalized Advantage Estimation (GAE) adds harmful variance in imperfect-information games at equilibrium**, destabilizing policy-gradient self-play. Proposes **Q-boosting** — a variance-reduced advantage estimator built from the **Expected SARSA(λ) trace** — as a drop-in replacement (VRPO). Reports more stable training and better final policies on imperfect-information benchmarks.
- **Why it matters here**: gives the wiki's stop-the-bleeding list for *self-play instability* a concrete, method-shaped fix (advantage estimator choice) — relevant to every poker/negotiation/curriculum self-play feature in this wiki.
- **Caveats**: already in wiki (2 hits); games evaluated are strategy-adjacent; paper preprint-level.

### ★★ A Structural Threshold in Decision Capacity Governs Collapse in Self-Play RL
- **Authors**: Arahan Kujur
- **Affiliation**: ⚠️ not stated; *not inferred*.
- **Venue**: arXiv:2605.16315 (4 May 2026) — `cs.LG`.
- **Link**: https://arxiv.org/abs/2605.16315
- **Abstract and key innovations**: theory + experiments on **self-play collapse**: under asymmetric rule perturbations to a base game, a **structural threshold at zero reach-weighted contingent action capacity** separates "healthy self-play" from collapse. Collapse is **reversible** with the right intervention but **intensifies under function approximation**; demonstrated on poker-, matrix- and dice-style games that isolate the mechanism.
- **Why it matters here**: the sharpest *mechanistic* account of why self-play diverges in the wiki (fits beside GAE-Falls-Short and Tablut's checkpoint play as the same underlying failure).
- **Caveats**: already in wiki (3 hits); simplified games, structural criterion not yet tested on full-scale self-play RL.

### ★★ QDHUAC: Distributional Value Estimation Without Target Networks for Robust Quality-Diversity RL
- **Authors**: Behrad Koohy, Jamie Bayne
- **Affiliation**: ⚠️ not stated on abs page; *not inferred*.
- **Venue**: arXiv:2604.20381 (22 Apr 2026) — `cs.LG`/`cs.AI`. (Originally submitted in the QD-RL series, device = **Brax**.)
- **Link**: https://arxiv.org/abs/2604.20381
- **Abstract and key innovations**: combines **Quality-Diversity RL** with a **target-free distributional critic** at **high update-to-data ratio** for **Dominated Novelty Search**. Removing target networks + using distributional value estimation makes critic training robust under the batch-staleness QD-RL imposes, yielding **order-of-magnitude fewer environment steps** to the same behavioural diversity on the Brax benchmark suite.
- **Why it matters here**: quality-diversity / novel examples is an under-covered lane in this wiki's game-RL corpus — this is the first featured QD-RL method, directly applicable to open-ended game-content policies and skill archives.
- **Caveats**: **fully fresh — 0 hits in wiki**; Brax locomotion tasks, not a named game.

---

## §2 Game AI Bot — LLM-Powered Game Agents and NPC Intelligence

### ★★★ Cutscene Agent: An LLM-Game-Engine Agent for 3D Cutscene Generation
- **Authors**: Lanshan He, Haozhou Pang, Qi Gan, Xin Shen, Ziwei Zhang, Yibo Liu, Gang Fang, Bo Liu, Kai Sheng, Shengfeng Zeng, Chaofan Li, Zhen Hui, Keer Zhou, Lan Zhou, Shujun Dai
- **Affiliation**: ⚠️ not stated on abs page; *not inferred* (large industrial author block per public records — tentative).
- **Venue**: arXiv:2604.25318 (28 Apr 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2604.25318
- **Abstract and key innovations**: an **LLM-driven agent framework that generates 3D cutscenes inside a commercial game engine**. Uses a **Model Context Protocol (MCP)-style bidirectional interface** so the LLM sends engine commands *and* receives live scene/state feedback for closed-loop editing. A declarative instruction is decomposed into engine-level action sequences; comes with **CutsceneBench** to score output against human-authored ground truth.
- **Why it matters here**: the wiki's cleanest **industry LLM↔engine integration** result (engine-as-tool via MCP), sitting directly on the [[model-context-protocol]] entity's game-application thread.
- **Caveats**: 1 hit in wiki (already documented — re-featured for the lane); evaluation is generative-quality-driven rather than gameplay win-rate.

### Cross-references (established, not re-summarized)
- **Bounded Autonomy** `2604.04703` *(A Theory of Bounded Autonomy, game-NPC autonomy bounds)* — 19 hits in wiki, covered since the April digests.
- **LLM-Guided Reinforcement Learning for Adaptive NPC Behavior in Multi-Agent Combat Games** `2609.02931` *(runtime strategy tags from a local Mistral-7B steering a trained PPO policy; win rate 11%→24%)* — 11 hits, last featured in the **10-04** digest.

---

## §3 Game Foundation Models

### Lane status
**No fresh unclaimed generalist/foundation-model paper surfaced in-window**; the GFMs that dominated recent digests remain canonical and are cross-referenced rather than re-summarized:
- **NitroGen** `2601.02427` — open generalist game agent (40k h / 1,000+ games), **CVPR 2026 (Honorable Mention)**; 52 hits in wiki.
- **Game-TARS** `2510.23691` — ByteDance Seed generalist multimodal game agent, native keyboard-mouse action space (500B+ tokens); 32 hits in wiki.
- **Pixels2Play** `2508.14295`, **GameVerse** `2603.06656`, **Lumine** `2511.08892` — 3D-open-world + VLM-reflection generalist agents; all documented in the 09-11 digest.

### ⭐ Note on dataset-adjacent GFM work
The window's actual GFM-*adjacent* increment is data/benchmark infrastructure, not a new model — **GameHorizon Suite** (§5) ships the first AAA-scale gameplay video-action-instruction dataset built for training/evaluating such foundation models, and **MirrorCraft** (§5) stress-tests them under hidden rule changes. Both are detailed in §5 and flagged here as the GFM lane's real 2026-09/10 storyline.

---

## §4 Procedural Content Generation (PCG)

### ★★ AutoUE: An Automated Multi-Agent System for Generating 3D Games in Unreal Engine
- **Authors**: Lei Yin, Wentao Cheng, Zhida Qin, Tianyu Huang, Yidong Li, Gangyi Ding
- **Affiliation**: ⚠️ not stated on abs page; *not inferred* (Beijing-based authorship per public records — tentative).
- **Venue**: arXiv:2603.07106 (v2 8 Apr 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2603.07106
- **Abstract and key innovations**: a **multi-agent LLM system that generates playable 3D games in Unreal Engine** from natural-language descriptions. Grounds generation with **RAG over UE tool documentation**, applies **design-pattern templates + engine constraints**, and closes the loop with an **automated play-testing pipeline** that reports runtime errors back to the generation agents for revision.
- **Why it matters here**: PCG's "content = runnable code in a real engine" direction (llm-c/software-3.0 adjacent) with an actual verification loop — complements the wiki's [[software-3-0]] and game-world-model lines.
- **Caveats**: 6 hits in wiki (documented earlier, re-featured); playability at AAA-scope not demonstrated; generated-games complexity ceiling is modest.

### ★★ Video Game Level Design as a Multi-Agent Reinforcement Learning Problem
- **Authors**: not fully listed on the abridged sources
- **Affiliation**: ⚠️ not restated here — see 09-11 digest for the full author list (multi-institution, *not inferred*).
- **Venue**: arXiv:2510.04862 (Oct 2025) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2510.04862
- **Abstract and key innovations**: first **PCGRL reframed as multi-agent RL**: several generator agents operate over **local neighbourhood observations** on noisy initial levels, self-organizing globally. A **JAX/GPU-parallelized** implementation makes training cheap; the multi-agent formulation **generalizes better to out-of-distribution map shapes** than a single global generator because it learns *local, modular design skills*.
- **Why it matters here**: the structural PCG insight (local-vs-global content control) that later multiverse/multimodal PCG work builds on; still the reference for multi-agent PCGRL in this wiki.
- **Caveats**: 5 hits in wiki (documented in 09-11); pre-recent surge preprint.

### Cross-references (established, not re-summarized)
- **PCGRLLM** `2502.10906` (Prompts-in-context generator; 37 hits), **VIPCGRL** `2508.09860` (text-level-sketch shared representation, Yonsei; 20 hits), **Multiverse** `2603.26782` (language-conditioned multi-game level generator; 17 hits), **Programmatic Content Metageneration + CAD** `2608.17947` (AIIDE 2026; NYU+Malta; last featured **10-04**).

---

## §5 Game Benchmarks & Datasets

### ★★★ MineExplorer: An Exploration Benchmark for MLLM Agents in Minecraft
- **Authors**: Tianjie Ju, Yueqing Sun, Zheng Wu, Wei Zhang, Yaqi Huo, Xi Su, Qi Gu, Xunliang Cai, Gongshen Liu, Zhuosheng Zhang
- **Affiliation**: ⚠️ not stated on abs page; *not inferred* (SJTU/Meituan-aligned authors per public records — tentative).
- **Venue**: arXiv:2605.30931 (v4 4 Sep 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2605.30931
- **Abstract and key innovations**: an **open-world exploration benchmark for multimodal-LLM (MLLM) agents in Minecraft** that deliberately **filters out atomic tasks that leak Minecraft-specific knowledge**, isolating true exploration ability (perception + planning in unfamiliar space). ReArSt-style **capability formulation** decomposes exploration into perception/planning/acting skills, and a **multi-agent synthesis workflow** generates the task suite at scale.
- **Why it matters here**: addresses a known benchmark confound in the wiki's Minecraft lane (knowledge-leak via domain priors) and pairs naturally with **MirrorCraft** (hidden-rule generalization) below.
- **Caveats**: 8 hits in wiki (documented; re-featured); MLLM-only scope; results vs frontier models modest.

### ★★★ GameHorizon Suite: Toward Multi-Horizon Game AI via Automated Annotation and a Large-Scale AAA Gameplay Dataset
- **Authors**: Yiran Wang, Xingyilang Yin, Junfu Pu, Guangzhi Wang, Kaifeng Li, Mingyu Ouyang, Huiqiang Sun, Lingen Li, Cheng Cheng, Wangbo Yu, Honghao Chen, Xiaodong Cun, Chi-Man Pun, Zhiguo Cao, Ying Shan
- **Affiliation**: ⚠️ not stated on abs page; *not inferred* (Tencent-ARC-aligned author block per public records, incl. Ying Shan — tentative).
- **Venue**: arXiv:2609.25001 (21 Sep 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2609.25001
- **Abstract and key innovations**: the **GameHorizon-Annotator** automated annotation pipeline + **GameHorizon-Data**, billed as the **first large-scale AAA gameplay dataset with temporally-aligned gameplay videos, player actions, and multi-horizon instructions**. Enables **multi-horizon evaluation** of game agents (short-term action, mid-term tactic, long-term objective) — differentiating "can act" from "can plan."
- **Why it matters here**: the GFM-adjacent infrastructure result flagged in §3 — datasets with *instruction-horizon hierarchy* are exactly what generalist game-agent training is missing.
- **Caveats**: 3 hits in wiki (documented; re-featured); data/benchmark paper — no model trained on it yet; dataset not independently inspected.

### ★★★ MirrorCraft: A Paired Benchmark for Evaluating Generalization under Hidden World Changes
- **Authors**: Jianxin Gao, Beini Hu, Runze Li, Wanli Peng, Ruohan Lei, Jinyuan Zhang, Linna Deng, Tianyi Yu, Zining Wang
- **Affiliation**: ⚠️ not stated; *not inferred* (Tencent/industry-aligned author block per public records — tentative).
- **Venue**: arXiv:2607.29218 (31 Jul 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2607.29218
- **Abstract and key innovations**: a **paired (Vanilla–Mirror) Minecraft benchmark** where the "Mirror" worlds change **server-side rules via datapacks** without announcing the change. An agent must detect + adapt: **5 biomes, 6 rule suites, 3 progression objectives, 2 model families, 6 agent configurations**, exposed through the **Mineflayer** interface. Clean ablations on rule-change detectability.
- **Why it matters here**: the wiki's only *rule-change generalization* benchmark — the empirical instrument behind "what happens when the world model is secretly wrong," linking to world-model and NPC-adaptation themes.
- **Caveats**: 4 hits in wiki (documented; re-featured); paper describes benchmark + initial agent scores, not a strong adaptive method.

### Cross-references (established, not re-summarized)
- **Orak** `2506.03610` (KRAFTON, 12-genre foundational game-agent benchmark; 33 hits), **PlaySuite** `2610.07127` (Anthropic; featured **10-07**), **MineNPC-Task** `2601.05215` (13 hits), **lmgame-Bench** `2505.15146`, **BALROG** `2411.13543`, **StarBench** `2510.18483`, **OmniGameArena** `2606.09826` — all documented in prior digests.

---

## §6 Industry Game AI

### ★★ AI Level of Detail: Distance-Aware ML Model Precision Selection for Real-Time Human Motion Prediction in Games
- **Authors**: Mathew Varghese
- **Affiliation**: ⚠️ not stated (single-author).
- **Venue**: **SIGGRAPH Technical Workshops 2026** (DOI 10.1145/3799828.3816004) — also arXiv:2606.06565.
- **Link**: https://doi.org/10.1145/3799828.3816004 · https://arxiv.org/abs/2606.06565
- **Abstract and key innovations**: extends classical geometry **LOD to the ML model itself**: route inference to **ONNX FP32/FP16/INT8 variants of the same motion-prediction model based on on-screen distance**. Near-camera NPCs get full-precision inference; distant NPCs get quantized variants with **manageable accuracy loss** (INT8 ≈ **9.79× latency improvement**), enabling many more concurrent NPC policies on a fixed GPU budget.
- **Why it matters here**: the wiki's sharpest *deployment-economics* result for **real-time NPC inference** — a concrete engineering lever industrial teams can ship immediately (pairs with the 09-20 "deployment economics" theme).
- **Caveats**: 1 hit in wiki (documented 09-11; re-featured); single-model/domain evaluation (motion prediction).

### Cross-references (established, not re-summarized)
- **Augmenting Game AI with Deep RL** `2606.20210` (survey; 64 hits — the lane's backbone), **AI for Games in the Foundation Model Era** `2609.16679` (featured **09-16**), **Reinforcement Learning with Human-Engine Verification** `2608.25518` (RLHEV; featured **09-11**), **WorldMind** `2608.21439` (decoupled state-aware NPC world model; featured **09-11**).

---

## §7 Related Techniques

### 7.1 Self-Play / Scaling

#### ★★★ Scaling Self-Play with Self-Guidance (SGS)
- **Authors**: Luke Bailey, Kaiyue Wen, Kefan Dong, Tatsunori Hashimoto, Tengyu Ma
- **Affiliation**: ⚠️ not stated on abs page; *not inferred* (Stanford-aligned authors per public records — tentative).
- **Venue**: arXiv:2604.20209 (v2 11 Aug 2026) — `cs.LG`.
- **Link**: https://arxiv.org/abs/2604.20209
- **Abstract and key innovations**: a **Conjecturer–Solver–Guide** self-play framework. The Guide **scores and filters the Conjecturer's synthesized problems by relevance and answer-cleanliness** before they reach the Solver, directly attacking **reward-hacking collapse** (Conjecturer learns to spam easy/ambiguous tasks that fool the solver judge). Cleaner synergy problems → sustained self-improvement across math/code-style tasks.
- **Why it matters here**: the most robust countermeasure in the wiki to self-play's "the verifier gets gamed" failure — a direct sibling of this digest's Game RL collapse papers, from a canonical research team.
- **Caveats**: 3 hits in wiki (documented; re-featured); evaluated on benchmark-style tasks, not full games.

#### Cross-references
- **PopuLoRA** `2605.16727` (LoRA population self-play PBT-like evolution; 13 hits), **G-Zero** `2605.09959`, **SCOPE** `2605.31433`, **OpenSIR** `2511.00602`, **Skill-SP** `2607.22529` — all documented in the 09-11 §7.1.

### 7.2 World Models for Games

#### ★★★ Learning Task-Sufficient World Models (agentic exploration + structured modeling)
- **Authors**: Fan Feng, Yujia Zheng, Minghao Fu, Yongqiang Chen, Guangyi Chen, Kevin Murphy, Biwei Huang, Kun Zhang
- **Affiliation**: ⚠️ not stated on abs page; *not inferred* (Google/CUHK/CMU-aligned authors per public records — tentative).
- **Venue**: arXiv:2607.04409 (5 Jul 2026) — `cs.LG`.
- **Link**: https://arxiv.org/abs/2607.04409
- **Abstract and key innovations**: closes the loop between **agentic exploration and structured world-model learning**: the model actively picks which data to collect (world-model-guided exploration) while using an **adaptive curriculum** to grow task complexity; learns **structured/task-sufficient latent states** rather than full scene reconstruction, improving generalization across skills and object-skill compositions in continuous-control and robotic-manipulation benchmarks.
- **Why it matters here**: **fully fresh (0 hits)** — the wiki's first entry on *exploration-driving-model-construction* (vs. the passive E2E world models elsewhere in §7.2); directly relevant to game NPCs that must rebuild their model of a changing level.
- **Caveats**: benchmark scope is manipulation/control, not a named game; abstraction level well above pixel-level game rendering.

#### ★★ OPINE-World: Programmatic World Modeling for ARC-AGI-3
- **Authors**: David Courtis, Wenhao Li, Scott Sanner
- **Affiliation**: ⚠️ not stated on abs page; *not inferred* (Univ. of Toronto-aligned authors per public records — tentative).
- **Venue**: arXiv:2607.01531 (v3 26 Sep 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2607.01531
- **Abstract and key innovations**: extends the **WorldCoder** line to **programmatic world modeling under fully unknown state representation, transitions and goals**: maintains a **Bayesian exploration-centric hypothesis space** over symbolic world-model programs and scores them by data fit + reachability. Reports improved sample-efficient task solving on **ARC-AGI-3**-style abstract reasoning tasks.
- **Why it matters here**: bridges game-world-modeling and abstract-reasoning benchmarks; one of the few programmatic (non-neural-renderer) world models in the wiki.
- **Caveats**: 8 hits in wiki (documented; re-featured); ARC-AGI-3 scope, not interactive game-window control.

#### Cross-references
- **ActSWM** `2607.26712` (action-sensitive world models, Context Collapse; featured **09-11**), **GameWAM** `2608.26200`, **Mind-Studio** `2606.16070`, **Concept-Guided Spatial Regularization** `2607.15142`, **Programmable World Model** `2609.10540` — all documented in prior digests.

### 7.3 Exploration, Curiosity & Hierarchical RL

#### ★★ Endogenous Exploration in Reinforcement Learning with Intrinsic Curiosity
- **Authors**: Armando Vieira
- **Affiliation**: ⚠️ not stated (single-author).
- **Venue**: arXiv:2609.05650 (4 Sep 2026) — `cs.LG`.
- **Link**: https://arxiv.org/abs/2609.05650
- **Abstract and key innovations**: **Liquid State Machine (LSM)** reservoir as the policy substrate with a **curiosity intrinsic-reward** bonus whose strength is tuned to an **intermediate coherence window** ("incoherence" of the reservoir dynamics). On **LunarLanderv2** and **BipedalWalkerv3**, curiosity improves learning *only inside that window* — too much or too little signal hurts — giving a concrete schedule insight for intrinsic-reward game agents.
- **Why it matters here**: **fully fresh (0 hits)** — the wiki's only *reservoir/LSM-substrate RL* entry; its "curiosity has a sweet spot" finding extends the standing curiosity/exploration line.
- **Caveats**: toy-continuous-control scope; single-author preprint; LSM substrate not yet at deep-policy scale.

#### ★★★ SIERL: Subgoal-Induced Exploration Reinforcement Learning
- **Authors**: Georgios Sotirchos, Zlatan Ajanović, Jens Kober
- **Affiliation**: ⚠️ not stated on abs page; *not inferred* (TU-Delft-aligned authors per public records, Kober — tentative).
- **Venue**: arXiv:2602.00460 (31 Jan 2026) — `cs.LG`.
- **Link**: https://arxiv.org/abs/2602.00460
- **Abstract and key innovations**: **frontier-based sub-goal selection** for exploration: the agent maintains cost-to-come/cost-to-go estimates and **picks sub-goals at the frontier boundary of the already-known state space**, learning the frontier–sub-goal mapping as a policy component. Improves sparse-reward exploration efficiency in challenging benchmark environments.
- **Why it matters here**: **fully fresh (0 hits)** — a concrete, game-relevant mechanism (frontier exploration) for open-world games with sparse rewards (Minecraft-style), where exploring the unknown *is* the objective.
- **Caveats**: benchmark scope is navigation/franka-style continuous domains, not a named game.

#### ★★★ Strict Subgoal Execution: Graph-Based Hierarchical Reinforcement Learning
- **Authors**: Jaebak Hwang, Sanghyeon Lee, Jeongmo Kim, Seungyul Han
- **Affiliation**: ⚠️ not stated on abs page; *not inferred* (Korea-aligned authors per public records — tentative).
- **Venue**: arXiv:2506.21039 (v3 20 May 2026) — `cs.LG`.
- **Link**: https://arxiv.org/abs/2506.21039
- **Abstract and key innovations**: **SSE** — graph-based hierarchical RL that **strictly enforces subgoal execution** instead of treating subgoals as soft targets. **Frontier Experience Replay (FER)** cleanly discards transitions from *unreachable* subgoals (the classic HRL stale-sample failure), and a **decoupled exploration policy** resolves the exploration-exploitation conflict between hierarchy levels.
- **Why it matters here**: **fully fresh (0 hits)** — directly answers the HRL-brittleness problem flagged across this wiki's long-horizon game lanes (Tablut-style stability, Minecraft-diamond horizons), on the same family-line as SIERL above.
- **Caveats**: benchmark/dataset breadth moderate; preprint-level evaluation.

---

## Summary Statistics

| Category | Papers Count |
|----------|-------------|
| Game RL | 6 |
| Game AI Bot | 1 (+2 cross-ref) |
| Game Foundation Models | 0 (+5 cross-ref) |
| PCG | 2 (+4 cross-ref) |
| Benchmarks & Datasets | 3 (+6 cross-ref) |
| Industry Game AI | 1 (+4 cross-ref) |
| Related Techniques | 5 |
| **Featured total** | **18** (5 fully fresh, 13 documented-and-refeatured) |

## Key Themes

1. **Self-play stability is still the binding constraint.** Generals.io (GS:6 winning with checkpoint-EMA), Tablut (per-role heads + checkpoint play), GAE-Falls-Short (advantage-estimator variance), Structural Threshold (decision-capacity collapse), and SGS (guide-filtered problem synthesis) are *five* papers converging on the same axis: **self-play diverges unless you stabilise the changing opponent + the credit signal**, whether at board-game, card-game, or LLM-post-training scale.

2. **World models are now built to be wrong, tested, and rebuilt.** Task-Sufficient WMs (exploration drives model construction), OPINE-World (Bayesian hypothesis space over programs), MirrorCraft (hidden rule changes), and MineExplorer (knowledge-leak-filtered exploration) mark a shift from "render the world" to "**detect and repair a wrong model of the world**."

3. **Benchmarks are the real 2026-09/10 GFM storyline.** No new generalist game foundation model in this window; the increment is **data/eval infrastructure** — GameHorizon's AAA multi-horizon dataset, MirrorCraft's paired rule-change tests, MineExplorer's leak-free exploration suite.

4. **Exploration returns as a first-class technique lane.** Three fresh entries (SIERL frontier sub-goals, SSE strict-subgoal HRL + Frontier Replay, LSM-curiosity-with-a-sweet-spot) fill the sparse-reward open-world niche that Atari-era bonuses never covered.

5. **PCG converges on local/multi-agent control + engine-grounded verification.** Multi-agent PCGRL's local-modular-design thesis and AutoUE's RAG+play-testing loop both say the same thing: **generative content must be controllable at the component level and verifiable by execution.**

> **Dedup/venue disclosures**: all 18 featured IDs `rg`-verified 0 hits in `wiki/synthesis/2026-10-10/`; 5 are 0 hits repo-wide. Selected venues stated only where explicit (SIGGRAPH Technical Workshops 2026). Affiliations printed as **not stated** or **tentative inference**; none asserted as fact. No result independently replicated. Today's siblings (`arxiv-daily`, `arxiv-paper-check`, `arxiv-ai-search`) independently reported **zero fresh in-window game-RL/CTR papers**, consistent with this digest's back-catalog basis.