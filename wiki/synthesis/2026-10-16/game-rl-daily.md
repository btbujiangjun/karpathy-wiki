---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-10-16)"
type: synthesis
created: 2026-10-16
updated: 2026-10-16
sources: [arxiv.org]
tags: [game-rl, game-ai, llm-agents, reinforcement-learning, self-play, multi-agent, foundation-models, world-models, pcg, benchmarks, npc, game-theory, inverse-rl, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-10-16)

> A **seven-lane sweep** (Game RL, Game AI Bot, Game Foundation Models, PCG, Game Benchmarks, Industry Game AI, Related Techniques) over the **fresh Fri 2026-10-16 arXiv announcement block**, harvested from the `arxiv.org/list/cs.*/new` listing pages (cs.AI, cs.LG, cs.MA, cs.CL, cs.CV, cs.GT, cs.RO, cs.HC, cs.SE) with per-paper metadata from the listing (title/authors/subjects/comments/abstract) and affiliation recovered from the LaTeXML HTML where printed. **Method note up front**: the arXiv **export API remained unavailable** this run — `http://export.arxiv.org/api/query` → HTTP 301, `https://` → HTTP 429 ("Rate exceeded") — so metadata was harvested from the listing HTML pages and individual `arxiv.org/abs` / `arxiv.org/html` pages instead. Every featured ID was **grep-verified against the live `wiki/**/*.md` tree before writing** (§0.3). Featured IDs span `2610.15054`–`2610.22319`; submissions 10–15 Oct 2026.

---

## §0 Method and Corpus

### 0.1 Coverage
- **Source**: `arxiv.org/list/{cs.AI,cs.LG,cs.MA,cs.CL,cs.CV,cs.GT,cs.RO,cs.HC,cs.SE}/new` for the **Fri 16 Oct 2026** announcement block — **1,721 unique entries** parsed across these categories (cs.AI 453, cs.LG 467, cs.CL 267, cs.CV 253, cs.RO 149, cs.MA 34, cs.GT 16, plus cs.HC / cs.SE).
- **Filter**: title + abstract keyword sweep across game lanes (game/gaming/gameplay/Atari/StarCraft/Dota/Minecraft/NetHack/poker/chess/backgammon/RPG/NPC/self-play/open-ended/level-generation/world-model/…), then manual triage; 72 raw candidates reduced to 22 featured.
- **Window vs. siblings**: the same-day siblings already claim the fresh `>2610.20610` block — `arxiv-daily` (2026-10-16), `arxiv-ai-search` (2610.17503–2610.20610 window), `conference-digest` (IDs `>2610.20610`), `tech-report-digest`. Overlap is managed explicitly in §0.3; in particular **SafeAdapt-Poker `2610.20473`** (featured in 10-15 `arxiv-daily`/`arxiv-ai-search`) and **Why Alternation Speeds Up CFR `2610.21970`** (featured in today's `conference-digest`) are **cross-referenced, not re-featured**.

### 0.2 Sweep
1. Listing-page harvest (`/new`) with full `<dd>` abstract blocks for nine categories.
2. Abs-page pulls for submission dates + subjects + venue comments; HTML pulls (`/html/{id}v1`) to recover author affiliations where printed.
3. Targeted arXiv search (`sortBy=announced`) for PCG / game-agent-benchmark terms to size the PCG and benchmark lanes.
4. **Dedup** — each candidate ID `grep`-tested against the whole `wiki/` tree (§0.3).

### 0.3 Dedup accounting (featured + notable cross-references)
| arXiv ID | Venue/subject | In-wiki hits | Status |
|----------|---------------|-------------:|--------|
| 2610.22319 (Gemini 4 / Minecraft) | cs.AI | 0 | **fresh** |
| 2610.20786 (EvolvingBrain) | cs.AI | 0 | **fresh** |
| 2610.21525 (CriticaLLM) | cs.AI | 0 | **fresh** |
| 2610.21040 (RRI meta-prompt) | cs.AI/cs.MA | 0 | **fresh** |
| 2610.21156 (MASP self-play dialogue) | cs.CL | 0 | **fresh** |
| 2610.20811 (RIGen) | cs.CV | 0 | **fresh** |
| 2610.21910 (CoWorld Reasoner) | cs.AI | 0 | **fresh** |
| 2610.22311 (Velox) | cs.CV | 0 | **fresh** |
| 2610.21095 (OneWM) | cs.CV | 0 | **fresh** |
| 2610.21612 (Intrinsic Dynamics WM) | cs.AI | 0 | **fresh** |
| 2610.20665 (RealtimeBench) | cs.AI | 0 | **fresh** |
| 2610.20693 (Orbia) | cs.CV | 0 | **fresh** |
| 2610.21244 (System1-Arena) | cs.CL/cs.AI | 0 | **fresh** |
| 2610.22289 (Env-agnostic coding agents) | cs.AI | 0 | **fresh** |
| 2610.21319 (CA-MAMBA) | cs.AI | 0 | **fresh** |
| 2610.20866 (SHRED) | cs.LG/cs.RO | 0 | **fresh** |
| 2610.19714 (Uncertainty self-play driving) | cs.RO | 0 | **fresh** |
| 2610.21029 (SCARCE) | cs.MA | 0 | **fresh** |
| 2610.21711 (LLM price competition) | cs.GT | 0 | **fresh** |
| 2610.21912 (Learning Rewards in Strategic Games) | cs.GT | 0 | **fresh** |
| 2610.22287 (Temporal-objective MARL) | cs.LG | 0 | **fresh** |
| 2610.15054 (Iterated games) | physics.soc-ph | 0 | **fresh** |
| 2610.20473 (SafeAdapt-Poker) | cs.AI/cs.GT | 4 | cross-ref (in 10-15 siblings) |
| 2610.21970 (CFR alternation) | cs.GT | 1 | cross-ref (in 10-16 conference-digest) |
| 2608.15146 (PureTD backgammon) | cs.LG | 4 | cross-ref (featured 08-23) |
| 2610.14883 (MARL-BattleGrounds) | cs.LG | 3 | cross-ref (featured 10-15) |
| 2610.16776 (Game-Creation-Agents) | cs.AI | 4 | cross-ref (featured 10-15) |

### 0.4 Affiliations and venues
- **Abs/listing pages frequently do not print affiliations.** Where an institution could not be read from the paper's own author block / LaTeXML affiliation spans, it is marked **"not stated"** and **not inferred** from surnames or email domains (standing wiki discipline). Inferred affiliations appear only as **"⚠️ inference from public author records — tentative"**, never asserted as fact.
- Venues are stated **only where explicit** (e.g. `EMNLP 2026 Main Conference`); otherwise `arXiv preprint`. **No result independently replicated.**

---

## §1 Game RL — Reinforcement Learning in Games, Self-Play, Multi-Agent & Game Theory

### ★★★ Learning Rewards in Strategic Games
- **Authors**: Antoine Bergerault, Cyrille Kone, Giorgia Ramponi
- **Affiliation**: ALPI Lab (per author block).
- **Venue**: arXiv:2610.21912 (15 Oct 2026) — `cs.GT`; `cs.AI`, `cs.LG`, `cs.MA`.
- **Link**: https://arxiv.org/abs/2610.21912
- **Abstract and key innovations**: extends **inverse reinforcement learning (IRL)** to **strategic multi-agent** settings, where the core difficulty is that *a reward that explains observed behavior need not induce optimal strategies when used for decision-making*. The paper formalizes this via **strategic identifiability** and proves a **negative result**: learning from a **fixed policy pair can be insufficient to strategically identify rewards, independent of the number of expert samples `K`** (no finite sample budget suffices). Motivated by this, the authors study what additional data/interactions restore identifiability.
- **Why it matters here**: the wiki's cleanest theoretical statement of *why reward inference in games is harder than single-agent IRL* — the reward-shaping / inverse-RL foundation that the competitive-game RL line (§2) and reward-shaping entries rest on.
- **Caveats**: **fully fresh — 0 hits in wiki**; theory paper (Nash-adjacent games), no Atari/board-game leaderboard.

### ★★ Learning Rational Strategies for Temporal Objectives in Multi-Agent Systems
- **Authors**: Omar Adalat, Edwin Hamel-De le Court, Francesco Belardinelli
- **Affiliation**: Imperial College London; University of Manchester.
- **Venue**: arXiv:2610.22287 (15 Oct 2026) — `cs.LG`; `cs.LO`, `cs.MA`.
- **Link**: https://arxiv.org/abs/2610.22287
- **Abstract and key innovations**: studies **rational synthesis** in **stochastic multi-agent systems with unknown dynamics**, where each agent has its own probabilistic temporal objective in **Probabilistic LTL on Finite Traces (`PLTL_f`)**. Solution concepts (**Nash equilibrium, subgame-perfect equilibrium**) are imposed as constraints on the joint strategy profile, with payoffs derived from each agent's probability of satisfying its temporal objective. The paper gives **conditional convergence guarantees for tabular Nash-Q learning** and **finite-sample confidence bounds** certifying constraint satisfaction.
- **Why it matters here**: bridges the wiki's **RL-dynamics** and **formal-specification** lines — "learn equilibrium strategies *subject to* temporal-logic constraints," a policy-side analogue of §7's constrained MARL.
- **Caveats**: **fully fresh — 0 hits in wiki**; tabular/known-state scope; guarantees are conditional.

### ★★ How language model agents reshape price competition
- **Authors**: Martin Bichler, Philip Hierhager, Kassian Köck, Fabian Pieroth
- **Affiliation**: Technical University of Munich (School of Computation, Information and Technology).
- **Venue**: arXiv:2610.21711 (15 Oct 2026) — `cs.GT`.
- **Link**: https://arxiv.org/abs/2610.21711
- **Abstract and key innovations**: uses **repeated Bertrand competition** as a stringent testbed (where standard online learners typically collapse to **stage-game Nash, prices ≈ marginal cost**) and shows **LLM pricing agents can escape it — depending on deployment choices**. LLMs out-adapt standard online learners, but the edge **largely disappears against full-information learners**. A key finding: **agents posting one price per period from raw market histories (including rival prices) can sustain supracompetitive regimes in self-play**, whereas agents that **emit probability distributions from summarized own-profit histories drift toward the competitive region**. An extracted **surrogate algorithm** shows how LLMs in specific deployments profit from regularly undercutting slower learners.
- **Why it matters here**: the sharpest fresh evidence that **LLM-agent "collusion"/supracompetitive outcomes are a deployment artifact, not an intrinsic capability** — a game-theoretic counterpoint to the wiki's LLM-NPC and multi-agent-LLM lines, with an explicit self-play mechanism.
- **Caveats**: **fully fresh — 0 hits in wiki**; homogeneous-goods (stylized) market; "collusion" is emergent, not explicitly coordinated.

### ★ Multi-Agent Learning of Reactive Strategies in Iterated Games
- **Authors**: James P. Wolfe, Joshua B. Plotkin
- **Affiliation**: not stated on arXiv metadata; *not inferred* (public records suggest University of Pennsylvania — tentative).
- **Venue**: arXiv:2610.15054 (10 Oct 2026) — `physics.soc-ph`; `cs.GT`, `q-bio.PE`.
- **Link**: https://arxiv.org/abs/2610.15054
- **Abstract and key innovations**: studies **selfish gradient-ascent learners** (rather than imitation dynamics) on the **2-D space of reactive strategies** — parameterized by **reciprocity** (P(cooperate | co-player cooperates)) and **forgiveness** (P(cooperate | co-player defects)) — in the **iterated prisoner's dilemma**. Because learners adapt to one another rather than to a fixed environment, the paper characterizes when mutual gradient ascent fails to produce good group outcomes and how the reactive-strategy geometry shapes convergence.
- **Why it matters here**: a mathematically clean **social-dilemma self-play** companion to the wiki's IPD/cooperation literature; the continuous-trait lens (reciprocity × forgiveness) is a useful vocabulary for NPC social policies.
- **Caveats**: **fully fresh — 0 hits in wiki**; two-trait policy class; no deep RL.

---

## §2 Game AI Bot — LLM-Powered Game Agents and NPC Intelligence

### ★★★ A team of Gemini 4 Argon agents beats Minecraft
- **Authors**: Maxence Faldor, Satinder Singh, Roberta Raileanu
- **Affiliation**: not stated on arXiv metadata; **⚠️ inference from public author records (Gemini / Google DeepMind authors) — tentative**.
- **Venue**: arXiv:2610.22319 (15 Oct 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2610.22319
- **Abstract and key innovations**: four **Gemini 4 Argon** agents were placed in a sandboxed **Minecraft survival world** with a single goal — **defeat the Ender Dragon**. Each agent controls a player through the open-source **Mineflayer** library and coordinates via **in-game chat + shared memory**. **No roles assigned, no human-written game logic**: the agents "planned, wrote, and debugged every program themselves." From a **randomly generated world on Easy**, the team wrote **2,783 programs** and completed the game in **27 h 14 min**, dying **605 times**. The authors claim this is the **first end-to-end autonomous completion of Minecraft by AI agents** using only standard Mineflayer, without pre-scouted seeds or human-written game-specific tools.
- **Why it matters here**: the strongest fresh **long-horizon, autonomous, code-writing game agent** result in the wiki — the "agents program themselves to win" thesis at Minecraft scale, directly extending the wiki's long-horizon-agent line (cf. 10-11's ASH/Pokemon–Zelda, 10-15's Game-Creation-Agents).
- **Caveats**: **fully fresh — 0 hits in wiki**; single run/world; "first" claim is paper-asserted; evaluation is completion (not win-rate vs. baselines); pauses/interventions permitted by the harness.

### ★★ EvolvingBrain: An Adaptive Skill System for Multi-modal Agents Self-Evolution in Open Worlds
- **Authors**: Runxuan Liu, Jingqi Shi, Baoxin Wang, Honghong Zhao, Haoyuan Xu, Yueqing Sun, Jiafeng Liang, Tao He, Dayong Wu, Qi Gu, Shijin Wang, Ming Liu, Bing Qin
- **Affiliation**: Harbin Institute of Technology; iFLYTEK; Meituan (per author block).
- **Venue**: arXiv:2610.20786 (14 Oct 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2610.20786
- **Abstract and key innovations**: argues multi-modal open-world agents have limited **self-evolution** — SFT enables imitation but not active experience organization, while outcome-based RL **underuses intermediate trajectories**. Proposes **EvolvingBrain**, an **adaptive skill system** with **(i) Stratified Skill Self-Evolution** that mines **Procedural Patterns** and **Problematic Patterns** from model-specific trajectories, summarizes them into skills, and evolves through repeated open-world interaction into a **Stratified Skill Architecture (Domain / Plan / Action-Trap skills)** — a multi-granularity knowledge repository, plus a **novel mechanism** for skill retrieval/reuse.
- **Why it matters here**: a fresh **experience→skill→reuse** memory architecture for open-world (Minecraft-family) agents — complementary to the wiki's memory-as-policy and skill-library entries, and a non-DeepMind industrial (iFLYTEK/Meituan) data point.
- **Caveats**: **fully fresh — 0 hits in wiki**; method-dense with abstract truncated in listing (mechanism details beyond the abstract not verified); single-source.

### ★★ CriticaLLM: Using LLMs as Autonomous Game Master for Tabletop Role-Playing Games
- **Authors**: Gaëtan Berlaimont, Justin Vanwichelen, Benoît Ronval, Hélène Verhaeghe
- **Affiliation**: UCLouvain, Louvain-la-Neuve, Belgium.
- **Venue**: arXiv:2610.21525 (15 Oct 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2610.21525
- **Abstract and key innovations**: identifies key components LLMs should exhibit for **Tabletop RPGs (e.g. Dungeons & Dragons)** and introduces **CriticaLLM**, a **fully automated Game Master** that can run entire TTRPG sessions — from **generating diverse stories** to **managing exploration and combat phases** — while respecting rules and leaving player-action freedom. Evaluated with **actual TTRPG players** and across the **diversity of generated plots and antagonists** for four LLMs.
- **Why it matters here**: the fresh **LLM-as-Game-Master / autonomous-narrative** entry — the "run the game, not just play it" cousin of the wiki's NPC and game-creation lines, with a human-player study (rare in this lane).
- **Caveats**: **fully fresh — 0 hits in wiki**; TTRPG-only; diversity/eval protocol paper-defined; four models.

### ★★ RRI: Recursive Reward Improvement via Adversarial Meta-Prompt Evolution
- **Authors**: Wei Dai, Qianchu Liu, Guanghui Qin, Xing Han, Tristan Naumann, Paul Pu Liang, Sheng Zhang
- **Affiliation**: Massachusetts Institute of Technology; Microsoft Research; Johns Hopkins University (per author block).
- **Venue**: arXiv:2610.21040 (15 Oct 2026) — `cs.AI`; `cs.MA`.
- **Link**: https://arxiv.org/abs/2610.21040
- **Abstract and key innovations**: targets **Recursive Self-Improvement (RSI)** in a **proposer–solver loop** for **open-ended expert tasks with no answer key** (e.g. clinical report generation), where the proposer must also **write a rubric**. The core failure mode is **rubric exploitation**: naively generated rubrics let solvers "name the expected topics without the substance," corrupting learning. **RRI (Recursive Reward Improvement)** evolves the **rubric itself** adversarially rather than the task, closing the exploit channel.
- **Why it matters here**: the wiki's cleanest fresh treatment of **reward/rubric hacking in self-improving game-like loops** — the "who writes the reward" problem adjacent to §1's IRL and to self-play reward design.
- **Caveats**: **fully fresh — 0 hits in wiki**; domain is expert text (not a game per se) — included as the **reward-design / self-improvement** bridge.

### ★ MASP: Stop Training Against Soft Users — Mentalized Adversarial Self-Play for Proactive Dialogue
- **Authors**: Zanwu Liu, Dan Zhang, Xiaodi Wang, Yongbo Mao, Xiaoyang Guo, Yonglin Wu, Peiyue Jiang, Yangyang Wei, Zecheng Lin
- **Affiliation**: School of Artificial Intelligence, Beihang University; Dongchezu Technology Co., Ltd., Beijing.
- **Venue**: **EMNLP 2026 (Main Conference)** — also arXiv:2610.21156 (15 Oct 2026) — `cs.CL`.
- **Link**: https://arxiv.org/abs/2610.21156
- **Abstract and key innovations**: frames proactive dialogue as a **partially observable game between a system and a rationally resisting user**. Notes that training/eval against **fixed or overly compliant simulators** rewards **soft-user bias** rather than robustness. **MASP (Mentalized Adversarial Self-Play)** models the user's evolving mental state with a **BDI-based latent state**, separates **reward-side teacher mentalization** from **policy-side student mentalization**, and **alternates self-play updates** for system and user policies — "turning robustness to rational resistance into a training signal."
- **Why it matters here**: a fresh **opponent-modeling / adversarial-self-play** instance outside board games — the dialogue/NPC analogue of population-based self-play, directly relevant to any NPC that must face adversarial users.
- **Caveats**: **fully fresh — 0 hits in wiki**; dialogue (not a game environment); EMNLP-profile evaluation.

---

## §3 Game Foundation Models & World Models

### ★★★ RIGen: Beyond Action Following with Reciprocal Interaction in Generative Gameplay
- **Authors**: Mengfei Li, Yi Zhang, Xingtong Ge, Lunjie Zhu, Fangyu Lin, Peng Li, Guanglu Song, Yu Liu, Wei Xue, Wenhan Luo, Yike Guo
- **Affiliation**: The Hong Kong University of Science and Technology; Vivix Group Limited (per author block; project lead / corresponding author marked in HTML).
- **Venue**: arXiv:2610.20811 (14 Oct 2026) — `cs.CV`.
- **Link**: https://arxiv.org/abs/2610.20811
- **Abstract and key innovations**: argues generative gameplay needs **persistent consequences** and a world that "acts according to its own state and rules," not just immediate responses to player actions. **RIGen (Reciprocally Interactive Generation)** combines **(1) persistent state + configurable rules, (2) contextual interaction reasoning, and (3) action-conditioned audiovisual generation** — so **interaction consequences and actor behavior jointly determine generated content** while keeping game state and visuals consistent.
- **Why it matters here**: the fresh anchor for the wiki's **generative-playable-world** lane — pushes past "action→frame" video generation toward **rule-grounded reciprocal worlds**, the interface between world models and actual game logic.
- **Caveats**: **fully fresh — 0 hits in wiki**; generative (not benchmarked on classic game RL); industrial co-authorship (Vivix Group).

### ★★ CoWorld Reasoner: Agentic Multimodal Reasoning with the Evolving Video World Model-Driven Harness
- **Authors**: Dongjie Cheng, Ruifeng Yuan, Ran Wei, Ning Song, Yongqi Li, Wenjie Li
- **Affiliation**: not stated on arXiv metadata; *not inferred*.
- **Venue**: arXiv:2610.21910 (15 Oct 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2610.21910
- **Abstract and key innovations**: existing approaches invoke a **Video World Model (VWM)** through **fixed pipelines** (e.g. novel-view synthesis). **CoWorld Reasoner** instead treats the VWM as a **unified visual reasoning engine**, wrapped in a **Video-World-Model-Driven Harness** that exposes visual operations as **tools**; **skills guide the VLM** in deciding *whether to imagine*, *which operation to run*, *how to construct the generation request*, and *how to interpret the result* — flexible visual imagination for diverse spatiotemporal reasoning tasks.
- **Why it matters here**: the **agentic-tool wrapper around world models** — the same "harness" pattern the wiki tracks for LLM agents, now applied to VWMs; a natural counterpart to 10-11's PlayWorld (world-model *benchmark*) on the *use* side.
- **Caveats**: **fully fresh — 0 hits in wiki**; reasoning-centric (not game-specific); affiliation not captured.

### ★★ Velox: Spatial Memory Makes World Models Efficient
- **Authors**: Qiuhong Shen, Shizun Wang, Xinchao Wang
- **Affiliation**: National University of Singapore.
- **Venue**: arXiv:2610.22311 (15 Oct 2026) — `cs.CV`.
- **Link**: https://arxiv.org/abs/2610.22311
- **Abstract and key innovations**: chunked video-diffusion world models keep context in **growing KV caches**, so later chunks get progressively slower. **Velox** is a **training-free attention router** doing **region-level context selection** using **frustum-slab correspondences** from streaming geometry: historical blocks are represented as **camera frustum slabs with depth intervals**, current-block depth comes from **recency-priority multiwarp**, and for well-covered regions **slab overlap softly modulates each layer's model-derived block importance** (uncovered regions fall back to the model's own routing).
- **Why it matters here**: attacks the **inference-cost bottleneck** of interactive world models — the "real-time game inference" concern (lane 6) expressed as a memory-efficiency mechanism; complements the wiki's world-model rollout-quality entries.
- **Caveats**: **fully fresh — 0 hits in wiki**; efficiency-focused (rollout quality traded off/nuanced); single-institution.

### ★★ OneWM: Can World and Action Modeling Benefit Each Other under Unified Causal Training?
- **Authors**: Yue Su, Bokai Lin, Xinkai Wang, Chubin Zhang, Xiangnan Wu, Kuan Zhang, Weiyang Jin, Jiwen Yu, Yiming Li, Cewu Lu, Lixin Yang, Xihui Liu
- **Affiliation**: not stated on arXiv metadata (author set spans Shanghai-Jiao-Tong / HKU / Shanghai AI Lab lines); *not inferred*.
- **Venue**: arXiv:2610.21095 (15 Oct 2026) — `cs.CV`. Project page linked.
- **Link**: https://arxiv.org/abs/2610.21095
- **Abstract and key innovations**: asks whether **world and action modeling reciprocally benefit** under unified causal training. **OneWM** treats **actions as both conditions for world prediction and targets for policy learning** in a shared video–action architecture, tested on **LIBERO, LIBERO-Plus, RoboCasa365** plus real-world policy experiments. Findings: learning the **visual consequences of specified actions improves policy performance and generalization** across scene changes; in turn **action learning improves multi-view world prediction**.
- **Why it matters here**: the fresh **bidirectional world-model↔policy** evidence — a mechanistic answer to "does imagination help control (and vice versa)?"; the embodied-manipulation analogue of game world models.
- **Caveats**: **fully fresh — 0 hits in wiki**; robotics benchmarks (LIBERO/RoboCasa), not game environments.

### ★★ Learning Intrinsic Dynamics in Latent World Models
- **Authors**: Jiamin Shi, Yuanhong Zhang, Zhiyang Liu, Jiawei Sun, Jingwen Fu
- **Affiliation**: Xi'an Jiaotong University; National University of Singapore.
- **Venue**: arXiv:2610.21612 (15 Oct 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2610.21612
- **Abstract and key innovations**: connects **action predictability** (reconstructing an action from consecutive latent states) with preservation of **intrinsic dynamics** (action→consequence relationships). **Central hypothesis**: encouraging action predictability stops the representation from discarding the distinctions between actions and their consequences. Provides **theory** (a positive lower bound on squared inverse-prediction error when an encoder merges distinguishable outcomes of different actions) plus empirical evidence that forward prediction benefits.
- **Why it matters here**: a crisp **representation-learning objective** for world models with a theoretical handle — the "don't let the encoder forget what actions do" principle, directly usable in game world models.
- **Caveats**: **fully fresh — 0 hits in wiki**; short paper (12 pages); theoretical bound is restricted to a stated regime.

---

## §4 Procedural Content Generation (PCG)

> **⚠️ Lane note — no fresh PCG paper in the 2026-10-16 block.** The announced window contains **no new procedural-content-generation / level-generation paper**. This is a genuine thin-lane result, not an omission: a targeted arXiv `sortBy=announced` sweep for "procedural content generation game" (top-50 by announcement date) returned the freshest PCG items at **`2610.11237`** (group-dance generation — *not* game PCG) and older IDs (`2607.12097`, `2606.03857`, `2606.02832`, `2605.01783`, `2604.27972`), all preceding this window. The nearest relevant, already-documented anchors:
> - **Multiverse: Language-Conditioned Multi-Game Level Blending via Shared Representation** — `2603.26782` (19 wiki hits).
> - **High-Dimensional PCG (HDPCG)** — `2602.18943` (17 hits): elevates non-geometric gameplay dimensions (layer, time) to first-class coordinates for controllable level generation.
> - **Playtrace Reconstructive Partitioning** — `2607.12097` (7 hits): domain-independent "cake" level representation over time; Sokoban.
> - **The Procedural Content Generation Benchmark** — `2503.21474` (6 hits): 12 game-content problems with quality/diversity/controllability metrics.

---

## §5 Game Benchmarks & Evaluation Suites

### ★★★ The World Won't Wait: Evaluating and Teaching Agents Under a Live Clock (RealtimeBench + TORSI)
- **Authors**: Ningxin Pan, Hanyu Li, Yeqing Shen, Ning Ding, Yehui Tang, Wentao Zhang
- **Affiliation**: Peking University; Samsung Research, Beijing.
- **Venue**: arXiv:2610.20665 (14 Oct 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2610.20665
- **Abstract and key innovations**: introduces **RealtimeBench**, **180 tasks across six game types**, to evaluate agents **while games keep running during inference** — an otherwise correct action can *arrive too late*. Paired evaluations show a slow/strong model (**GPT-6.1-sol**) **beats a faster model (Jev) when games are paused, but loses when they keep running** — a clean demonstration that reasoning latency is a first-class failure mode. Proposes **TORSI (Two-Timescale Offline Recursive Self-Improvement)**: a **slow teacher** studies failures and tests corrections in **paused** games between attempts and writes reusable instructions for a **fast student** that acts **without teacher calls during gameplay**; two rounds raise Jev's average test score **13.51 → 24.19** (0–100 progress) across all six game types.
- **Why it matters here**: the fresh benchmark that formally prices **wall-clock latency** into game-agent evaluation — a dimension the wiki's static agent benchmarks miss; directly relevant to real-time game inference (lane 6) and to any "think-then-act" NPC.
- **Caveats**: **fully fresh — 0 hits in wiki**; six (paper-defined) game types; model names are as reported in the abstract.

### ★★★ Orbia: Do Generated Videos Form a Consistent 3D World?
- **Authors**: Dongyue Lu, Guian Fang, Hur Lim, Yonggang Wu, Yanrong Wang, Hongshan Chen, Shengju Qian, Yue Liao, Wei Chow, Lingdong Kong, Tianxin Huang, Yu Yang, Hongji Yang, Junchao Huang, Ao Liang, Yihao Wang, Zihan Wang, Rong Li, Hanlin Chen, Xin Wang, Wei Tsang Ooi, Mike Zheng Shou, Shuicheng Yan
- **Affiliation**: not stated on arXiv metadata for the aggregate author block; **⚠️ inference from public author records (NUS Show Lab / Skywork AI lines) — tentative**.
- **Venue**: arXiv:2610.20693 (14 Oct 2026) — `cs.CV`. Technical report, 70 pages; project page, code, dataset linked.
- **Link**: https://arxiv.org/abs/2610.20693
- **Abstract and key innovations**: argues visually appealing frames "do not necessarily depict a consistent 3D world." **Orbia** is presented as the **first benchmark dedicated to systematic, comprehensive evaluation of 3D consistency in interactive world models**. Via **controlled exploration and revisit**, it organizes evaluation into **three dimensions: input preservation, generated-content persistence, and 3D self-consistency**. Input preservation uses **registered RGB-D references + annotated anchors** for appearance/geometry/spatial-stability measurement; persistence compares revisits to regions absent from the input against their first generation.
- **Why it matters here**: the strongest fresh **world-model evaluation** artifact — a rigorous 3D-consistency yardstick complementary to 10-11's PlayWorld (objective/behavioral) and the wiki's GameHorizon thread.
- **Caveats**: **fully fresh — 0 hits in wiki**; "first" is paper-asserted; affiliation not printed on metadata.

### ★★ System1-Arena: Which Decisions Can Be Left to System 1?
- **Authors**: Tianyu Chen, Xinyang Liu, Ruyi An, Zhendong Wang, Mingyuan Zhou
- **Affiliation**: The University of Texas at Austin (per author block).
- **Venue**: arXiv:2610.21244 (15 Oct 2026) — `cs.CL`; `cs.AI`, `cs.LG`. Code, leaderboard, dataset linked.
- **Link**: https://arxiv.org/abs/2610.21244
- **Abstract and key innovations**: contrasts **System-1** models (single forward pass, probabilities over options — e.g. Jev, OpenAI Decisions API) against **System-2** generative reasoning, and asks which decisions can be left to System 1. **System1-Arena** gives all models the same decision requests and scores their probabilities: **92k questions across 105 tasks from 268 public sources** in four groups (text classification/knowledge, applied decisions, evaluation/control, agent/action), plus **138 closed-loop environments** spanning web shopping, SWE-bench coding control, **robotics, games, and driving**; in **real-time mode the world evolves while the model decides**. Evaluates **30 models** (7 closed LLMs, 13 …).
- **Why it matters here**: pairs with RealtimeBench on the **latency–capability frontier**, and adds a **decision-time/closed-loop** evaluation hub with an explicit games slice.
- **Caveats**: **fully fresh — 0 hits in wiki**; games are one slice among many; venue not stated (leaderboard artifact).

### ★★ Improving Environment-Agnostic Coding Agents: The Role of Scaffolding
- **Authors**: Sergey Rodionov
- **Affiliation**: not stated.
- **Venue**: arXiv:2610.22289 (15 Oct 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2610.22289
- **Abstract and key innovations**: tests whether stronger models reduce the value of developer-supplied scaffolding. Evaluates a **Codex-based agent** in two nearly identical prompt variants across **ARC-AGI-3, AGI Maze, and Terminal-Bench**, with unchanged code/prompts/tools (environment-specific info passed as input). **A single instruction change** — encouraging the agent to **report difficulties and return control for automatic continuation** — improves mean scores on **both ARC-AGI-3 and AGI Maze**, while Terminal-Bench shows small mixed changes. Yet the general agent stays **below an ARC-AGI-3-specific reference**, even with **GPT-5.6-sol**.
- **Why it matters here**: a fresh **ARC-AGI-3 / maze** interaction-scaffolding study — the "the harness, not the model" thread, and evidence that **environment-agnostic scaffolding has a ceiling** on game-like interactive reasoning.
- **Caveats**: **fully fresh — 0 hits in wiki**; single-author; ARC-AGI-3/AGI Maze are puzzle/interactive benchmarks (not classic game RL).

---

## §6 Industry Game AI & Deployment

> **Lane note.** The fresh block is **light on dedicated studio papers** (no Tencent/NetEase/miHoYo/EA/Ubisoft PCG title in-window). Industrial involvement this edition is embedded in the featured set: **Google DeepMind** (Gemini 4 Minecraft agents, `2610.22319` — §2), **iFLYTEK + Meituan** (EvolvingBrain `2610.20786` — §2), **Microsoft Research** (RRI `2610.21040` — §2), and **HKUST × Vivix Group** (RIGen `2610.20811` — §3). The strongest *deployment-economics* signal remains the real-time inference pressure documented by **RealtimeBench `2610.20665`** (§5) and the efficiency mechanism in **Velox `2610.22311`** (§3). For continuity on shipped-game/genre AI, see the already-documented **Game-Creation-Agents `2610.16776`** (Tencent; cross-ref below).

---

## §7 Related Techniques — Self-Play, Model-Based MARL, Imagination, Emergent Multi-Agent Behavior

### ★★ Constrained Multi-Agent Reinforcement Learning in Imagination (CA-MAMBA)
- **Authors**: Raz Shmueli, Shahaf S. Shperberg
- **Affiliation**: Ben-Gurion University of the Negev, Beer-Sheva, Israel.
- **Venue**: arXiv:2610.21319 (15 Oct 2026) — `cs.AI`.
- **Link**: https://arxiv.org/abs/2610.21319
- **Abstract and key innovations**: moves most **constrained policy updates into imagination** via a **multi-agent world model** that predicts **cost**. Reports that the stronger model-free baseline needs **10–20×** CA-MAMBA's interactions on the median **SMAC** configuration, and CA-MAMBA earns **2.8–12×** the baselines' **MAMuJoCo** reward at equal budget. In controlled tests on one task per benchmark, pricing the model's cost advantages at parity **more than halves a cost-blind learner's cost** and meets a tight continuous-control limit the learned multiplier misses — suggesting the model's cost estimates are **not the bottleneck**.
- **Why it matters here**: the fresh **model-based-constrained MARL** result — imagination as the sample-efficiency engine for multi-agent game control (SMAC), with an explicit "the model is good enough" diagnostic.
- **Caveats**: **fully fresh — 0 hits in wiki**; SMAC/MAMuJoCo (not Atari/board games); abstract is terse.

### ★★ SHRED: Self-Play for Heterogeneous Road-Users without Expert Demonstrations
- **Authors**: Wei-Jer Chang, Zhouchonghao Wu, Akshay Rangesh, Weixin Li, Masayoshi Tomizuka, Wei Zhan
- **Affiliation**: Applied Intuition, Mountain View, CA; University of California, Berkeley.
- **Venue**: arXiv:2610.20866 (14 Oct 2026) — `cs.LG`; `cs.AI`, `cs.RO`. Comments: *Self-play for Autonomous Driving*.
- **Link**: https://arxiv.org/abs/2610.20866
- **Abstract and key innovations**: asks whether **realistic interaction behavior can emerge purely through self-play** (no human demonstrations, no logged-trajectory replay). **SHRED** jointly trains **vehicles, pedestrians, and cyclists** through **large-scale heterogeneous self-play from random initialization**, combining **type-specific dynamics and objectives** with **procedural scenario generation** and **per-agent randomization**. On the **Waymo Open Sim Agents Challenge (WOSAC)** it jointly controls all three road-user types and outperforms [demonstration-based baselines].
- **Why it matters here**: the wiki's freshest **heterogeneous self-play with zero demonstrations** — the multi-agent-simulation analogue of alpha-zero-style self-play, and an industrial (Applied Intuition) self-play deployment.
- **Caveats**: **fully fresh — 0 hits in wiki**; driving (not a "game"), included under self-play technique; WOSAC is a simulation-realism benchmark.

### ★★ Uncertainty-Driven Self-Play for Robust Multi-Agent Driving Policies
- **Authors**: Sajad Marvi, Julian Schmidt, Alessandro Canevaro, Julian Jordan, Abhinav Valada
- **Affiliation**: not stated on arXiv metadata; **⚠️ inference (University of Freiburg — Valada lab) — tentative**.
- **Venue**: arXiv:2610.19714 (14 Oct 2026) — `cs.RO`; `cs.AI`, `cs.MA`.
- **Link**: https://arxiv.org/abs/2610.19714
- **Abstract and key innovations**: an **uncertainty-driven self-play** scheme in which **half the agents are rewarded for increasing their neighbors' epistemic uncertainty** while the other half learn to drive safely; **epistemic uncertainty** acts as an **automatic proxy for scenario difficulty**, so exploring agents seek out hard cases and **generate a curriculum without manual scenario design**. The resulting policy **outperforms standard self-play**.
- **Why it matters here**: a clean **curriculum-via-uncertainty** self-play mechanism — the population-based-training idea expressed contractively, useful beyond driving.
- **Caveats**: **fully fresh — 0 hits in wiki**; driving domain; abstract truncated in listing.

### ★ SCARCE: Emergent Institutions in Long-Horizon Multi-Agent Coding Systems
- **Authors**: Abhinav Kumar, Rediet Abebe, Eugene Bagdasarian, Sahar Abdelnabi
- **Affiliation**: University of Massachusetts Amherst; ELLIS Institute Tübingen (per author block).
- **Venue**: arXiv:2610.21029 (15 Oct 2026) — `cs.MA`; `cs.AI`.
- **Link**: https://arxiv.org/abs/2610.21029
- **Abstract and key innovations**: argues prior agent-negotiation studies use **stylized games and simulated bargaining**, leaving open how coordination evolves in **sustained long-horizon tasks**. **SCARCE (Shared Compute ARena for Coding agEnts)** has agents solve **sequences of coding tasks under individual deadlines** while **negotiating access to a shared execution resource** (when/how long they may inspect, compile, run tests). Agents **spontaneously develop informal institutions** — persistent rules and commitments grounded in **reputation, reciprocity**, and [norm enforcement].
- **Why it matters here**: the wiki's fresh **emergent-institutions / social-coordination** data point — a "real (non-stylized) game" study of multi-agent resource competition with safety implications.
- **Caveats**: **fully fresh — 0 hits in wiki**; coding-task arena (not a video game); abstract truncated in listing.

---

## Cross-references (established wiki content, not re-summarized)

- **PureTD: RL for Backgammon Money Games with No Evaluation-time Search** `2608.15146` *(self-play TD-Gammon for **cubeful money games**; search-free model beats GNU Backgammon / Open Sage at 1-ply, and beats cubeless→Janowski conversion at equal size)* — 4 hits; **featured in `game-rl-daily` 08-23**, re-referenced 08-31.
- **SafeAdapt-Poker: Counterfactual Risk Calibration for Budgeted Adaptation under Opponent Shift** `2610.20473` *(dual-counterfactual sequential control under **opponent shift**; monotone strategic-risk model + budget-state continuation model)* — 4 hits; featured in the 10-15 `arxiv-daily` / `arxiv-ai-search` (game/mechanism slice), **not yet in a `game-rl-daily`**.
- **Why Alternation Speeds Up Counterfactual Regret Minimization?** `2610.21970` *(tests the "optimism" intuition for alternating RM⁺ self-play; canonical additive form fails an information-matched test on an analytic witness family)* — 1 hit; featured in **today's `conference-digest` (2026-10-16)**.
- **MARL-BattleGrounds: A JAX-native Benchmark for Heterogeneous and Competitive Multi-agent RL** `2610.14883` — 3 hits; scheduled **10-15** `game-rl-daily`.
- **Game-Creation-Agents: Autonomous Game Production** `2610.16776` (Tencent) — 4 hits; scheduled **10-15** `game-rl-daily`.
- **SpireBench** `2610.12596` (Slay the Spire long-horizon strategic play) — 2 hits — and **SpeedrunBench** `2610.08076` (video-game speedrunning) — 6 hits — game-benchmark lane, documented in prior digests.

---

## Contradictions / open questions
- **Latency vs. capability.** RealtimeBench `2610.20665` shows a *slower, stronger* model **loses** once the clock runs; System1-Arena `2610.21244` independently institutionalizes the same "world evolves while deciding" axis. Neither contradicts prior wiki entries, but together they sharpen the open question of **when reasoning beats reflex in games** — the wiki's earlier long-horizon-agent entries mostly evaluate with the game paused.
- **Self-play generality.** SHRED `2610.20866` and Uncertainty-Driven Self-Play `2610.19714` both report self-play **without demonstrations** beating demonstration/standard baselines in *driving*; whether this transfers to heterogeneous **game** agent populations (beyond WOSAC) is untested here — flagged, not resolved.
- **No contradicting claim** within this edition was identified against existing wiki sources; all featured items are new-to-wiki and single-source.
