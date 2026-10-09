---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-10-09)"
type: synthesis
created: 2026-10-09
updated: 2026-10-09
sources: [arxiv.org]
tags: [game-rl, game-ai, llm-agents, foundation-models, world-models, pcg, benchmarks, self-play, multi-agent, game-theory, hierarchical-rl, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-10-09)

> **A thin, sibling-split window.** Yesterday's stated ceiling was `2610.10539`; today's frontier is `2610.12470`. The fresh band `2610.10540`–`2610.12470` is real (816 in-window records, 764 unclaimed), but the game lane was **almost entirely claimed by same-day siblings**: the strongest game-RL/game-agent papers of the window (`2610.11663` RTS command-conditioned PPO, `2610.11692` Jev-as-RL-component on Atari/MiniGrid, `2610.11842` ad-hoc MARL, `2610.11450` ARC-AGI-3 coding agent, `2610.12341` AAArena, `2610.11129` GameCommBench, `2610.11696` Tower-of-Hanoi characterization, `2610.12321` public-goods MARL) are all recorded in `arxiv-daily.md` and `arxiv-ai-search.md`, so this report **withdraws them to §9.3 rather than re-summarizing**. What remains — and what this digest features — is the window's **world-model / benchmark / programmatic-content + game-theory** slice: a **distributed real-time multiplayer world model (Counter-Strike 2)**, a **Minecraft multiplayer world-model benchmark whose best generated system scores 21/100**, a **Minecraft spatial-agent benchmark (HKUST)**, a **game-engine-coupled interactive world framework (MirroS)**, an **LLM-generated-voxel-world judge**, and four **game-theory/complexity** results. §1 (Game RL) and §6 (Industry) are **declared near-vacant**; PCG is the one lane that is *not* vacant, courtesy of the LLM-world-generation pair.

---

## §0 Method and Corpus

### 0.1 Boundary determination
- **Yesterday's stated ceiling: `2610.10539`** (the 2026-10-08 digest's §0.1 frontier).
- **Today's true frontier: `2610.12470`** (`Dex-One2Many: Learning Dexterous Manipulation from a Single Human Demonstration`, `cs.RO`/`cs.CV` — **recorded as the boundary marker, not a game paper**). The maximum indexed ID across the swept category feeds and keyword queries at run time.
- **Fresh band: `2610.10540`–`2610.12470`.** This is the **2026-10-08 submission block, announced 2026-10-09** — a **single-day announcement block**, not a rolling 24 h (arXiv announcement lag, as documented on 10-07/10-08). The entire band is `2610.*`.
- **Catch-ups**: none admitted this run. Every featured paper is `2610.10540`+ and published 2026-10-08.

### 0.2 Sweep — three channels
1. **arXiv export API, ten category feeds** (Atom XML, `curl`/`urllib` + browser UA, 3 s spacing; `cs.AI`, `cs.LG`, `cs.CL`, `cs.CV`, `cs.MA`, `cs.GT`, `cs.HC`, `cs.RO`, `cs.NE`, `cs.SE`, **plus continuation pages `start=200` for `cs.AI` and `cs.LG`** to cover `2610.09624`/`2610.10091` down below the window floor): **1,972 unique records**, max `2610.12470`.
2. **Twenty-eight keyword queries** (two passes; `all:"…"` and `ti:`/`abs:` forms: `game`, `games`, `gaming`, `gameplay`, `chess`, `poker`, `Atari`, `StarCraft`, `Minecraft`, `NetHack`, `NPC`, `esports`, `multiplayer`, `board games`, `video games`, `self-play`, `multi-agent reinforcement learning`, `game agent`, `game environment`, `game-playing`, `procedural content`, `level generation`, `game theory`, `world model`, etc.): **~3,900 records**, union-deduplicated.
3. **Recent-proceedings check** (`neurips.cc/virtual/2026`): the 2026-10-08 run's proceedings channel was reused by inspection, **not re-harvested** — no new game paper posted since 2026-09-25 that this series had not already logged surfaced in the window. **CoG 2026 IEEE Xplore remains pending** (expected ~2026-10-16).

**Pool accounting**: merged unique pool **5,904 records** → **816 in-window** (`≥2610.10540`) → **764 unclaimed** by the whole-wiki baseline and same-day siblings → **241 broad-lexicon candidates** → **18 window papers featured** (§1–§7) after abstract reading. The remainder were read and excluded as out-of-lane (robot world-action models, driving/navigation world models, GUI-transition world models, diffusion video generation).

### 0.3 Dedup — clean on the featured set, eight game-lane withdrawals
- Baselines: **8,377 claimed IDs** (whole-`wiki/` regex sweep `2[0-9]{3}\.[0-9]{4,5}` at run start) + **80 same-day sibling IDs** (`wiki/synthesis/2026-10-09/arxiv-daily.md` + `arxiv-ai-search.md`, snapshot taken before drafting).
- **All 18 featured IDs re-verified immediately before writing: 0 collisions.**
- **Eight game-lane papers inside this window are sibling-claimed** and are **withdrawn to §9.3 rather than re-summarized** — including four in `arxiv-ai-search.md`'s dedicated Lane D (Games / Multi-Agent) and four in `arxiv-daily.md`'s Games section.
- **Title-level dedup note**: `MultiWorldBench` (this run, §5) is a **new** Minecraft multiplayer world-model benchmark and is **not** the same object as the wiki's earlier world-model benchmark entries (`WBench`/`PlayWorld`, 10-06/10-08 digests); no name collision arose.

### 0.4 Affiliations
- Institutions read **only** from each paper's own arXiv HTML `ltx_authors` / `ltx_role_affiliation` block or explicit author-line text — **never inferred from surnames, email domains, or author homepages**.
- **16 of 18 affiliations recovered.** **1 not recoverable on arXiv** (`2610.12135` Q-Shaped Options — the HTML author render is unavailable and the abs page carries no affiliation block; **not inferred** despite Oxford-FLAIR author names). **1 single-author independent** (`2610.10622` WorldBench — Krish Bakshi, a personal email; reported as printed).
- **2 sibling-claimed game papers carry industry affiliations** (`2610.11450` = **AWS**; `2610.12341` = Tsinghua), recorded only in the §9.3 table, sourced from the siblings.

---

## §1 Game RL — Reinforcement Learning in Games

> **Lane status: near-vacant, and the vacancy is sibling-induced, not a true lull.** The window contained at least four genuine RL-in-games papers — `2610.11663` (constrained command-conditioned PPO + Thompson-sampling bandit strategist for **MicroRTS**), `2610.11692` (a frozen **Jev** decision model used as reference policy / exploration judge / replay rater across **9 MiniGrid + 3 Atari** tasks), `2610.11842` (**ConventionPlay**, ad-hoc-collaboration RL for mixed-adaptability partner populations), and `2610.12321` (tabular Q-learning in **spatial public-goods dilemmas**) — **all four already claimed by same-day siblings** and withdrawn to §9.3. The three featured items below are therefore the RL-*adjacent* residue: two generic long-horizon/hierarchical RL methods with direct game applicability, and one combinatorial-game complexity result.

### ★★ Q-Shaped Options for Hierarchical Reinforcement Learning
- **Authors**: Clarisse Wibault, Antoine Gorceix, Antonio Léon Villares, Alexey Zakharov, Evangelos Chatzaroulas, Michael Matthews, Eduardo Pignatelli, Jakob Foerster
- **Affiliation**: ⚠️ **not recoverable this run** — the arXiv HTML author render is unavailable and the abs page carries no affiliation block; **not inferred** despite the Oxford-FLAIR author names.
- **Venue**: arXiv:2610.12135 (8 Oct 2026) — `cs.AI`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.12135
- **Abstract and key innovations**: HRL should give both benefits of hierarchy — **temporal abstraction** (options shrink the decision horizon) and **spatial abstraction** (per-level state abstractions aggregate data). Current methods fail one of two ways: some **discard option distinctions needed for optimal control** (undermining the hierarchy), others **retain unnecessary distinctions** (keeping horizon reduction but forfeiting coarser state abstraction). The paper characterizes **three desiderata for an action abstraction** and introduces **Q-Shaped Options (QSO)**: distinct state-value functions, Q-functions and policies at each level, with the **action abstraction between consecutive levels learned as a shared encoder shaped jointly by the two levels' Q-functions**; the low-level Q-function uses the option as its goal.
- **Why it matters here**: hierarchical RL is the wiki's standing answer to **long-horizon, goal-conditioned game tasks** (Minecraft diamond, StarCraft tech trees), and the failure taxonomy here — *too coarse vs. too fine an option space* — is exactly the practical tension that makes HRL brittle in games. Tying the learned abstraction to the Q-functions rather than to reconstruction is a clean objective choice.
- **Caveats**: preprint, unreviewed; **affiliation unrecoverable**; abstract excerpt does not list games or benchmark names, so the game relevance is at the *method* level.

### ★★ World-Model Policy Arbiter for Goal-Conditioned Reinforcement Learning (WMPA)
- **Authors**: Junwei Quan, Evgenii Opryshko, Nicholas Rhinehart, Igor Gilitschenski
- **Affiliation**: **University of Toronto** (Quan, Rhinehart, Gilitschenski) and **Vector Institute** (Opryshko, Gilitschenski). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.10932 (8 Oct 2026) — `cs.LG`. Comment: *"22 pages, 3 figures, 14 tables. Project page + code."*
- **Link**: https://arxiv.org/abs/2610.10932
- **Abstract and key innovations**: no single offline goal-conditioned RL algorithm is best across environments, goals, and even **phases of the same task**. Instead of deploying one policy, **WMPA treats a bank of frozen goal-conditioned policies as a portfolio** and arbitrates at test time: it **rolls each frozen policy out inside a learned state-space world model**, scores the imagined futures with a **shared goal-conditioned value function**, and executes the winner for a **short commitment interval** before re-arbitrating. Value functions across policies are not directly comparable (different scales; some policies have none), so comparison happens through *imagined future states*; the commitment interval bounds switching instability.
- **Why it matters here**: it is the wiki's cleanest instance of **"action selection = choosing which policy to run"** — the same meta-control problem as selecting a strategy in a decomposition like `2610.11663`'s strategist/executor split (sibling-claimed, §9.3), but solved with **rollouts in a learned world model** rather than a bandit. Relevant to any game agent that has a repertoire of skills and no single good policy.
- **Caveats**: preprint, unreviewed; requires a pre-existing **bank** of frozen policies (not learned here); evaluated on OGBench-class offline tasks, **not a named game**.

### ★ The Computational Complexity of the Ungar Games on Distributive Lattices
- **Authors**: Kengo Hashimoto
- **Affiliation**: ⚠️ **none printed** on the abs page or HTML author block; **not inferred**.
- **Venue**: arXiv:2610.11017 (8 Oct 2026) — `math.CO`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.11017
- **Abstract and key innovations**: the **Ungar game** (Defant et al.) is a combinatorial game on a finite lattice; on a distributive lattice it reduces via Birkhoff's theorem to **repeatedly choosing and removing a non-empty set of maximal elements from a poset `P`**. The paper **settles an open question** of Defant et al. by proving the outcome problem on `J(P)` is **PSPACE-complete** — even for posets of max chain length ≤ 3 with bipartite Hasse diagram — and shows **NP-completeness for chain length ≤ 2**, while length ≤ 1 is in LOGSPACE.
- **Why it matters here**: one of the window's two hardness results in a *game* (the other being `2610.12378`, §7); it gives a **clean complexity hierarchy** (SPACE/NP/LOG) for a game with a geometric origin. Modest scope for the game-AI lane, recorded for completeness.
- **Caveats**: pure combinatorics/complexity — **no algorithm, no experiments, no game-playing agent**; `math.CO` contribution; single-author, affiliation unprinted.

---

## §2 Game AI Bot — LLM-Powered Game Agents and NPC Intelligence

### ★★★ AgentGarten: Code Worlds for Evolving Agents
- **Authors**: MirroS Technical Report (Jiawei Chi, Shangchen Miao, Zhiyuan Shi, Kailu Wu, Hanyang Wang, Weiliang Chen, Qiyu Dai, Jinshan Ren, Jun Gao, Mingsheng Long, Yueqi Duan, Jiangran Lyu, Jialong Wu, Fangfu Liu)
- **Affiliation**: **MirroS, Tsinghua University, Peking University** (printed on the title block). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.12374 (8 Oct 2026) — `cs.CV`. Comment: *"Project page"*. **No venue acceptance claimed; self-described "Technical Report".**
- **Link**: https://arxiv.org/abs/2610.12374 · Project: https://mirros-lab.github.io/agent-garten
- **Abstract and key innovations**: interactive virtual worlds let agents learn by exploration, but **what they can learn is bounded by the environment**, which must be both **faithful** (consistent state/rules/dynamics) and **realistic** (real-world visual distributions). AgentGarten couples **simulators and game engines with a shared neural renderer**: the simulation backends maintain **persistent world state and execute program-defined interaction rules**, while the renderer generates **visual observations from structured conditions** exported through a common interface. The renderer adapts a **pretrained video model to geometry conditions**, is distilled with a proposed **Adversarial Forcing** (makes history-prefilling differentiable through exact replay, so losses on later predictions update how the renderer encodes prior observations) and is optimized for real-time interaction. Agents perceive, act in real time, and **distill each round of experience into "playbooks" that subsequent agents inherit and refine**.
- **Results**: **agents learn from just 4 rounds**, versus millions for a conventional RL counterpart; new worlds are written as code and rendered through the same interface, so environments **scale in number and difficulty alongside their agents**.
- **Why it matters here**: this is the window's strongest **"environments as the lever"** result and the most concrete instance of the wiki's recurring *the environment is the curriculum* thread — a **game-engine-first**, code-defined, neural-rendered world where the agent's learning signal is *self-distilled playbooks*, not gradients. It is also a direct answer to the measurement/world-model concerns of 10-08: if the environment's state is engine-owned and rule-executing, the "world-model fidelity" problem is replaced by a renderer-fidelity problem.
- **Caveats**: **self-described Technical Report from a small lab** (MirroS) — unreviewed; the "4 rounds vs millions" comparison is to "a conventional RL counterpart" whose budget is not specified in the abstract; the playbook-distillation loop is a bespoke mechanism without independent replication.

### ★★ Constitutional Gating and Deterministic Recovery for Multi-Agent LLM Negotiation
- **Authors**: Masaaki Nakatsu, Reno Wang
- **Affiliation**: **AO, Inc. / OrbLabs AG** (Nakatsu) and **AO, Inc.** (Wang). Printed in the author block.
- **Venue**: arXiv:2610.11542 (8 Oct 2026) — `cs.CL`, `cs.AI`. Comment: *"29 pages, 3 figures. Gatekeeper, agents, constitution, lexicon, 30 run logs and analysis scripts released. Companion paper: arXiv:2610.09772."*
- **Link**: https://arxiv.org/abs/2610.11542
- **Abstract and key innovations**: multi-agent LLM systems negotiating with a **stateful adversarial counterpart** waste model calls in three ways — **polite loops** that never meet a hidden acceptance condition, **malformed outputs** triggering retries, and **compliance deadlocks**. Against a released adversarial **Gatekeeper** (acceptance rules are fixed regexes; its LLM only renders reply text), the paper ablates a three-part stack: a **5-Pillar runtime constitution**, a **4-tier swarm** (Director, three-agent majority vote, Monitor, schema hard gate) and **Cognitive Annealing** (deterministic deadlock detection + **atomic purge** of agent context + canonical recovery message).
- **Results (30 runs, Gemini 2.5 Pro agents / Claude Haiku 4.5 Gatekeeper)**: constitution + Director make an acceptable framing **possible but not reliable** (0/5 baseline unlocks → 1/5 and 2/5); when the swarm unlocks it does so in one turn at **67–73% fewer tokens**, when it does not it costs 17–38% more. Under honeytrap-to-compliance deadlock, **LLM-only steering escapes 0/5 while atomic purge + canonical strike escapes 5/5** (Fisher p=0.008); LLM-written strikes failed the deterministic pre-flight **5/5** even when an LLM Monitor approved 4. **Pre-registered call/token-reduction hypotheses were not supported.**
- **Why it matters here**: it is a **negotiation-game bot** result with an unusually honest ledger — the paper reports the *null* on its own pre-registered efficiency hypotheses and finds the only robust escape is **deterministic**, not LLM-driven. For game bots that must negotiate (auction, diplomacy, trading NPCs) the lesson is concrete: **deterministic recovery beats LLM steering under adversarial pressure**.
- **Caveats**: a **known-solution testbed** (it measures stack execution/recovery, not discovery); single model pair; 5 runs/config; **industry lab, unreviewed**; the negotiation "game" is a market-delegation abstraction, not a game environment.

### §2 coverage note
NPC behaviour modelling, bot-detection, and social-deduction agents produced **no featureable unclaimed arXiv paper**. The lane's strongest game-agent items — **AAArena** (`2610.12341`), **Jev-as-RL-component** (`2610.11692`), **ConventionPlay** (`2610.11842`) and the **ARC-AGI-3** coding agent (`2610.11450`) — are sibling-claimed (§9.3).

---

## §3 Game Foundation Models & World Models for Games

### ★★★ WorldCast: Distributed Multiplayer World Models
- **Authors**: Ziyang Ye, Junchao Huang, Evelyn Zhang, Zhihao Xie, Ruicheng Zhang, Boyao Han, Litao Ban, Ziye Wang, Xinting Hu, Shaoshuai Shi, Zhuotao Tian, Li Jiang
- **Affiliation**: **CUHK-Shenzhen** (Ye, Huang, Xie, Han, Jiang), **SLAI** (Huang, Zhang, Tian, Jiang), **Tsinghua SIGS** (Ruicheng Zhang), **Voyager Research, Didi Chuxing** (Ban, Wang, Shi), **USTC** (Hu). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.12412 (8 Oct 2026) — `cs.CV`. Comment: *"31 pages, 19 figures, 20 tables. Project page."*
- **Link**: https://arxiv.org/abs/2610.12412 · Project: https://ziyang-ye.github.io/WorldCast-Page
- **Abstract and key innovations**: multiplayer world models must generate **independently controlled views** consistent in **both players and shared environment**. Most methods use **joint multi-view generation**, whose cost grows with each player. **WorldCast is distributed**: each player runs a **local client (video generator + state model)**; the state model estimates the player's position from generated video and control inputs; clients **exchange player states** and project them into **camera-aligned player-state fields** guiding *where and how* other players are rendered, while **shared scene state** lets clients reuse one another's generated observations. Experiments on **Counter-Strike 2**: **>10× higher player-rendering rates** than joint generation, stable image quality over **hour-long rollouts**, each client real-time.
- **Why it matters here**: it is the window's headline **game world-model** result and the first in the series that is **architecturally distributed** rather than a bigger joint generator — the scaling answer for multiplayer (each added player adds a client, not a cross-product). The **player-state field** as the inter-client interface is the reusable primitive.
- **Caveats**: preprint, unreviewed; evaluation is **CS2 only**; "consistency" is argued visually + via exchange protocol, and the paper's own benchmark sibling (`2610.11723`, §5) shows world-model consistency metrics are still weak — read WorldCast's claims against MultiWorldBench's floor (best generated system 21/100).

### ★★ Multi-Agent Egocentric World Model with Fine-Grained Embodied Interaction (ME-World)
- **Authors**: Dahyun Chung, Siyoon Jin, Hyunwook Choi, Honggyu An, Junyoung Seo, Hyunsung Kim, Seung Wook Kim, Seungryong Kim
- **Affiliation**: **KAIST AI** (all authors; co-corresponding: Seung Wook Kim, Seungryong Kim). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.12299 (8 Oct 2026) — `cs.CV`, `cs.AI`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.12299 · Project: https://cvlab-kaist.github.io/ME-World
- **Abstract and key innovations**: egocentric world models predict first-person observations conditioned on one agent's actions; real embodied settings have **multiple interacting agents**. Existing multi-agent world models use **coarse actions** (locomotion, camera, discrete commands), leaving **fine-grained embodied interaction** under-explored. ME-World formulates **synchronized ego-stream generation** for multiple agents and **jointly denoises multiple ego streams in a shared token sequence**, conditioning each stream on **all agents' target-view poses** and grounding generation with **shared environment memory**. It introduces **shared-world consistency metrics** (environment, update, identity).
- **Why it matters here**: fine-grained multi-agent interaction (two avatars manipulating the same object) is precisely where single-agent egocentric world models break; conditioning each stream on *all* agents' poses is the cross-view action-consistency device that multiplayer game world models need but joint generators hide.
- **Caveats**: preprint, unreviewed; trained on **real + synthetic multi-agent data** (domain mix unclear in the abstract); no named commercial game; the "consistency metrics" are introduced by the same paper.

### §3 coverage note
- A **generalist game-playing foundation model** did not appear in this window (vacancy, not a claim of absence). The two entries above are **world-model infrastructure for multi-agent gameplay**, not unified game policies.
- **`2610.12417` WOVEN (CMU/UCSD — MLLM visual-transition reasoning; 36,076 examples, 20 scene types; training ~2,000-item subsets improves 22 of 26 external benchmarks by up to 27.3 pp)** is recorded as a **§5 pointer**: it is a **visual-transition-reasoning** training source/benchmark for embodied agents, not a game environment, but its "shared training primitive" framing is the most transferable non-game result in the window.

---

## §4 Procedural Content Generation

> **Lane status: NOT vacant this run** — the first PCG-relevant feature since 2026-10-06, after the 10-07/10-08 two-run vacancy. Both entries are **LLM/program-driven world generation and its grading**, which is where the lane has migrated.

### ★★ WorldBench: Evaluating LLMs on Three.js Voxel World Generation
- **Authors**: Krish Bakshi (single author; personal email in the HTML author block — reported as printed)
- **Affiliation**: ⚠️ **independent / not stated** — no institution printed; **not inferred**.
- **Venue**: arXiv:2610.10622 (8 Oct 2026) — `cs.GR` primary, `cs.AI`, `cs.CL`, `cs.CV`, `cs.SE`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.10622 · Code: https://github.com/KrishBakshi/worldbench
- **Abstract and key innovations**: LLMs can write **complete interactive 3D worlds as code**, but grading them is unreliable. Existing judges take **one view** (a VLM scores rendered snapshots, or an LLM reads source); on worlds from five frontier models the two views **disagree on 32% of required items**, mostly code no frame shows, and fixed views miss close-up content. **WorldBench** is a benchmark + judge for **open-ended, LLM-generated Three.js worlds** from one prompt (a floating voxel island with ten biomes, physics, day/night and seasonal cycles). The judge **explores the running world** (controls its clock, orbits it, sends a **navigator agent to frame each biome**) and **reads the code for what it sees**, trusting neither channel alone: a code quote counts only if the source contains it; visual claims are checked against measured pixels. A **mutation test** (features removed by construction) shows code-only judging gives full credit to **4 of 5 removed features**; the judge cuts kept-points on removed features by a third (5.44 → 3.55 of 7.11).
- **Why it matters here**: a clean, honest **PCG-evaluation** result: **generation quality is now good enough that the bottleneck has moved to grading** — and the fix is **closed-loop exploration + code/visual cross-checking**, the same "trust neither the metric nor the model alone" shape as the 10-08 measurement-critique cluster. Its **mutation test is a reusable falsification protocol** for any LLM-content judge.
- **Caveats**: single-author, **independent, unreviewed**; one prompt / one world family (voxel islands); 5 evaluated models; "navigation agent" framing implies LLM-in-the-loop, whose own reliability is not separately measured.

### ★ OuroWorld: Bringing Any 3D World Alive as Diverse, Endlessly Looping 3D Cinemagraphs
- **Authors**: You-Zhe Xie, Ting-Wei Chou, Yu-Hsuan Li, Kaipeng Zhang, Zhixiang Wang, Yu-Lun Liu
- **Affiliation**: **National Yang Ming Chiao Tung University** (Xie, Chou, Li, Liu) + **Alaya Lab** (Zhang, Wang). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.12461 (8 Oct 2026) — `cs.CV`, `cs.GR`. Comment: *"Project page."*
- **Link**: https://arxiv.org/abs/2610.12461 · Project: https://ouroworld.userwei.com
- **Abstract and key innovations**: 3D world models generate explorable scenes that are **frozen in time**. OuroWorld turns any static **3D Gaussian Splatting** scene into a **3D cinemagraph** — vivid, diverse motion looping seamlessly from any viewpoint — with a **mask-free** pipeline: a VLM infers plausible dynamics, guides a video model to synthesize a reference video, which is lifted/completed into multi-view video. It learns from this imperfect supervision via **Inconsistency-Robust Periodic 4DGS**: a **Fourier-series deformation field guarantees looping by construction**, and a **Grounded Drift Field** anchored at the reference view absorbs cross-view inconsistency; unlike Eulerian methods limited to fluid-like motion, it captures general deformation, object motion, and illumination change.
- **Why it matters here**: adjacent to PCG as **automated dynamic-content generation for static worlds** — the "bring a level to life" primitive for game/simulation content pipelines. The **loop-by-construction** Fourier field is the transferable trick.
- **Caveats**: preprint, unreviewed; **not a game environment** (no interaction, no agents); evaluation is **ground-truth-free** (vividness/naturalness/loop-seam) plus user study (70.8–99.0% wins on 39 scenes) — a soft protocol.

---

## §5 Game Benchmarks

### ★★★ Mine Odyssey: Benchmarking Spatial Agentic Intelligence in the Wild
- **Authors**: Yuxuan Cao, Junlong Li, Hao Li, Junxian He
- **Affiliation**: **The Hong Kong University of Science and Technology (HKUST)** (all authors; email `@connect.ust.hk`; code under `hkust-nlp`). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.11328 (8 Oct 2026) — `cs.AI`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.11328 · Project: https://mine-odyssey.github.io · Code: https://github.com/hkust-nlp/MineOdyssey
- **Abstract and key innovations**: agents need **agentic spatial intelligence** — explore unfamiliar environments, update spatial understanding through interaction, adapt actions to sustain progress toward a sequence of goals. **Mine Odyssey** evaluates this with **Minecraft reconstructions of real-world locations**: **180 tasks / 30 locations across 20 countries and 5 continents** (20 outdoor, 10 indoor), spanning Manhattan, rural Entrup, Santa Lucía Hill, Buckingham Palace. Tasks give a **natural-language waypoint sequence**; success requires finding routes and entrances, **opening doors, and moving between levels via stairs and ladders**, while monitoring progress and recovering from navigation errors.
- **Results**: **GPT-6 Astra 85.6%**, Claude Opus 5.5 **73.9%**, best open-weight **DeepSeek-V4.1-Flash 23.9%** — a **~50-point open/closed gap** and large room on agentic spatial intelligence.
- **Why it matters here**: the window's strongest **game-based agent benchmark**: it converts Minecraft into a **geographically real, waypoint-sequenced navigation** test, which is a harder and more *semantically grounded* spatial task than prior Minecraft agent suites. The **open-vs-closed ~50-point gap** is the replica-ready headline number.
- **Caveats**: Minecraft reconstruction fidelity to real locations is asserted, not audited; single game engine; **sibling-claimed? no — unclaimed**, but note the identical window produced a *different* Minecraft benchmark (MultiWorldBench, below) — real growth, not collision.

### ★★ MultiWorldBench: Do Independently Controlled Views Describe One Shared World?
- **Authors**: Zhangbo Xu, Ruoxi Zhang, Rui Hu, Yisong Wang
- **Affiliation**: **Zhiying Guangnian Technology Co., Ltd.** (recovered from the arXiv HTML authors block).
- **Venue**: arXiv:2610.11723 (8 Oct 2026) — `cs.AI`, `cs.CV`. Comment: *"31 pages, 17 figures, 3 tables."*
- **Link**: https://arxiv.org/abs/2610.11723
- **Abstract and key innovations**: multiplayer world models must keep **independently controlled views consistent with one shared, persistent world**. MultiWorldBench is a **diagnostic Minecraft benchmark**: **495 case configurations / 7 task suites / 10 capabilities** (independent control, cross-view motion, shared-state synchronization, persistence, structural reasoning, concurrent interaction, delayed revisit). It evaluates **Solaris, Gamma-World, MineWorld** against **Engine GT** ground truth.
- **Results**: best generated system **Gamma-World 21.39/100** (Solaris 20.88, MineWorld 1.89) vs **Engine GT 91.69**. **All generated systems score ≤ 8.00 on state persistence and 1.33 on structural consistency**; none succeeds at spatial reasoning or building-identity preservation. Human preferences match the automatic ranking (**mean dimension-level Spearman 0.96**).
- **Why it matters here**: it is the sharpest **world-model reality check** in the window and a direct companion to `WorldCast` (§3): *plausible individual views do not yet constitute a coherent multiplayer world*. The **10-capability decomposition** is the reusable instrument; the **≤8/100 persistence floor** is the number to cite against any multiplayer-world-model claim.
- **Caveats**: preprint, unreviewed; three generated systems only; the "Engine GT = 91.69" reference is the oracle, not a competitor; Minecraft-only.

### §5 coverage note
**GameCommBench** (AI-generated game commentary, board/sports/esports; `2610.11129`) and **AAArena** (12 game ladder, 1,920 human programs; `2610.12341`) and the **Tower-of-Hanoi 3D characterization framework** (`2610.11696`) are the window's other game benchmarks — **all sibling-claimed** (§9.3). Anchors from earlier runs (PlaySuite, Learn2Play, BoardGameArena, BALROG) stand. **CoG 2026 Xplore still pending (~10-16).**

---

## §6 Industry Game AI — Game Development, Deployment, and Real-Time Inference

> **Lane status: declared vacancy for original arXiv output** — but the window is unusually **industry-dense by affection, not by section**: the strongest features carry industry affiliations (**WorldCast** = CUHK-Shenzhen + **Didi Chuxing Voyager Research**; **AgentGarten** = **MirroS** + Tsinghua + PKU; **SP-DocReader** = **OPPO**; **ME-World** = KAIST), and the sibling-claimed game papers include **AWS** (`2610.11450`) and Tsinghua's competition platform (`2610.12341`). No new engine-integration, on-device-inference, or NPC-deployment paper surfaced as an unclaimed primary contribution. The 10-07 reading — *"industry game-AI results in this corpus are systematically unreviewed and should be read as claims, not findings"* — applies to every industry paper above.

---

## §7 Related Techniques — Self-Play, Game Theory, Multi-Agent and Safe RL

### ★ Self-Play
#### SP-DocReader: Difference-Aware Self-Play for Precise Document OCR
- **Authors**: Wenjie Liao, Xiaohui Song, Liangjie Zhao, Haonan Lu
- **Affiliation**: **Guangdong OPPO Mobile Telecommunications Corp., Ltd.** (Liao, Song, Lu) + **Adelaide University** (Zhao). Recovered from the arXiv HTML authors block.
- **Venue**: arXiv:2610.11148 (8 Oct 2026) — `cs.CV`, `cs.AI`. **No venue acceptance claimed.**
- **Link**: https://arxiv.org/abs/2610.11148
- **Abstract and key innovations**: a **self-play** framework for OCR that targets **residual errors after SFT**. **Reading Discrepancy Masking** aligns reference and generated tokens via **longest common subsequence** and scores unmatched positions with their full conditioning prefixes; **Focused Fidelity Loss** adds direct negative-log-likelihood supervision at unmatched ground-truth positions. Only the OCR module trains (backbone frozen); the combined gradient is derived to separate relative-score optimization from direct supervision. **Reduces Vary-600K character error rate ~54% on Qwen3-VL-4B and improves DocVQA ANLS by 3.7 points.**
- **Why it matters here**: relevant to the game-lane only as a **self-play *technique*** — the wiki's self-play interest is normally games/RLVR, but here self-play is used as a **discrepancy-targeted fine-tuning objective**, which is the same "focus the signal on what remains wrong" principle behind the game-agent teacher distillation in `2610.11692` (sibling, §9.3). Included for the transferable mechanism, not the domain.
- **Caveats**: **OCR, not games** — included as a technique transplant; industry preprint, unreviewed.

### ★★ Multi-Agent Decision-Making
#### Mental-Models for Multi-Agent Systems
- **Authors**: Hanan Gani, Lulu Shao, Manmohan Chandraker
- **Affiliation**: **University of California, San Diego** (all three). Recovered from the arXiv HTML authors block.
- **Venue**: **NeurIPS 2026** (accepted, per the arXiv comment) — arXiv:2610.12453 (8 Oct 2026,) `cs.MA`.
- **Link**: https://arxiv.org/abs/2610.12453 · Code: https://github.com/hananshafi/Mental-Models
- **Abstract and key innovations**: robust multi-agent decision-making requires reasoning about **what others know, intend, and will do under partial observability**, but current agentic systems use prompts/memory/behavioral shaping without an **explicit, reusable partner-state representation**. The paper equips an agent with a **latent mental model of its counterpart**, learns an **amortized recursive Theory-of-Mind representation** (first- and second-order mental state) jointly with a **belief-conditioned reward model** that scores candidate actions relative to the inferred partner state, then learns a policy under that belief-aware signal — so the agent acts independently at inference while retaining explicit partner modeling.
- **Why it matters here**: it is the window's cleanest **opponent/partner modeling** result and directly connects to the game lane's ad-hoc-collaboration thread (`2610.11842` ConventionPlay, sibling-claimed) and to human–AI negotiation (`2610.11542`, §2). **Second-order** ToM is what separates "model the opponent's action" from "model the opponent's model of me" — the recursion that poker/diplomacy agents need.
- **Caveats**: evaluated on language-only + multimodal benchmarks (not a named game); "mental state" is latent and not human-validated; **NeurIPS 2026 acceptance is the paper's own comment** (main track not distinguished there).

### ★ Game Theory & Complexity
- **`2610.11711` Antichains for Concurrent Parameterized Games** — Bertrand, Bouyer, Staquet (**Université de Rennes/Inria/CNRS/IRISA; CNRS & ENS Paris-Saclay; Nantes Université**; in GandALF 2026 proceedings). Symbolic **antichain fixed-point algorithms** compute Eve's winning region in the exponential **knowledge game** for concurrent parameterized reachability games (PSPACE-complete); C++ implementation + benchmarks. *Why it matters*: symbolic, not explicit-state, solving of **games with an arbitrary number of players** — the many-agent regime. *Caveat*: formal verification, not gameplay; no learned agents.
- **`2610.11718` A Fast and High-Accuracy Finite-Time Sliding-Mode Algorithm for Computing Local Stackelberg Equilibria in Nonlinear Bilevel Games** — Zenati, Muir, Youcef-Toumi (**City St George's University of London + MIT**). Recasts Stackelberg-equilibrium computation as **manifold stabilization**: first-order optimality conditions define **Stackelberg sliding manifolds**, and sliding-mode dynamics drive iterates to them in finite time, with curvature conditions selecting valid equilibria. **100% success over 500 nonconvex Monte-Carlo trials**, median **26 iterations** vs 456 for the nearest fully successful baseline, residuals ~1e-16. *Why it matters*: leader–follower (Stackelberg) structure underlies adversarial/opponent-aware game AI; a **finite-time, curvature-filtered** equilibrium solver is a reusable primitive. *Caveat*: pure optimization; no game environment.
- **`2610.12378` On the Hardness of 4-to-1 Games with Perfect Completeness** — Fei, Minzer, Wang (**MIT**). Proves the **4-to-1 Games Conjecture** (Khot, CCC 2002): NP-hard to distinguish value 1 from value ≤ ε, with implications for coloring and independent-set hardness. *Why it matters*: a foundational **inapproximability** result in the games/PCP lineage that underpins hardness of constraint games. *Caveat*: complexity theory — no AI, no gameplay.

### ★ Safe & Portfolio RL (game-adjacent)
- **`2610.12420` A Unified Bellman Operator for Safety-Critical Reinforcement Learning** — Rao, Karegoudra Jayanth, Eysenbach, Fisac (**Princeton University**). Unifies performance and safety into a **joint value function** with a **two-timescale TD** convergence proof (fast timescale estimates safety value; slow timescale the joint value), yielding a policy that **maximizes task return subject to safety at all times**; stable convergence with near-zero test-time violations on continuous control. *Why it matters*: safe game/task RL without a hand-built safety filter — relevant to deployment (bots that must not ruin a shared session). *Caveat*: continuous-control (not games); theory + simulation.

---

## Summary Statistics

| Category | Papers Count |
|----------|-------------|
| §1 Game RL (incl. HRL, offline-GCRL, combinatorial game) | 3 |
| §2 Game AI Bot | 2 |
| §3 Game Foundation Models & World Models | 2 |
| §4 Procedural Content Generation | 2 |
| §5 Game Benchmarks | 2 |
| §6 Industry Game AI | 0 (vacancy) |
| §7 Related Techniques (self-play, multi-agent, game theory, safe RL) | 6 |
| **Total featured (unclaimed)** | **18** |
| **Sibling-claimed game papers withdrawn (§9.3)** | **8** (+9 game-theory/econ non-game) |

## Key Themes

1. **The day's strongest game papers were already taken.** Four in `arxiv-ai-search.md`'s Lane D (AAArena, Jev-as-RL, ConventionPlay, ARC-AGI-3) and four in `arxiv-daily.md`'s Games section (RTS command-conditioned PPO, GameCommBench, Tower-of-Hanoi characterization, public-goods MARL) are sibling-claimed. The same-day sibling-coordination protocol (10-07/10-08 recommendation) is now *working* — and the direct cost is that this run's featured set is the world-model/PCG/game-theory residue.
2. **Multiplayer world models are the frontier — and they are not yet coherent.** `WorldCast` (distributed, real-time, CS2, hour-long rollouts) and `ME-World` (fine-grained multi-agent ego streams) push capability; `MultiWorldBench` measures it and finds the best generated system at **21.39/100** with a **≤8/100 state-persistence floor** and **none** passing spatial reasoning. Capability and measurement shipped in the **same window** and disagree by design.
3. **Grading is the new PCG bottleneck.** `WorldBench` shows code-only and vision-only judges **disagree on 32% of items** and that code-only judging credits features that never run; its fix is **closed-loop exploration + code/visual cross-check + mutation testing**. This is the PCG-lane echo of the 10-08 world-model metric crisis.
4. **The environment is the lever, again.** `AgentGarten` couples rule-executing engine state with a distilled neural renderer and reports **4 rounds of agent learning vs millions for RL** — the strongest "build the world, not the gradient" claim in the series, from a paper that also lets worlds be **written as code**.
5. **Minecraft is the default testbed, twice over.** `Mine Odyssey` (180 real-place navigation tasks; GPT-6 85.6% vs open-weight 23.9%) and `MultiWorldBench` (495 multiplayer consistency configs) independently rebuilt Minecraft as a benchmark on the same day — one for **spatial agents**, one for **multiplayer world models**.
6. **Honest negatives keep shipping.** `2610.11542` reports its own **pre-registered efficiency hypotheses unsupported** (and finds deterministic recovery beats LLM steering 5/5 vs 0/5); `WorldBench`'s mutation test falsifies code-only judging; `MultiWorldBench` reports persistence floors near zero. This continues the 10-05/10-08 conclusion that **an instrument-critique outranks a method with a better number**.

---

## §9 Contradictions, Venue Updates, and Sibling Collisions

### 9.1 Contradictions
- **No direct claim-level contradiction of a prior digest was found.** The load-bearing tension is **intra-window**: `WorldCast` (§3) and `ME-World` (§3) advance multiplayer world-model **capability**, while `MultiWorldBench` (§5) independently measures the class and finds **near-zero state persistence and structural consistency**. These are compatible only under the reading that *capability improved on rendering/scale while coherence remains unsolved*; flagged so the pair is not merged into a single "multiplayer world models work now" claim.
- **Standing 10-08 caveat carried forward, not retracted**: the world-model lane's FVD/LPIPS-family comparisons remain under the Kuration SDK falsification; today's `MultiWorldBench` is a partial answer (engine-grounded capabilities instead of visual-similarity metrics) and should be cited alongside it.

### 9.2 Venue updates
- `2610.12453` **Mental-Models for Multi-Agent Systems — accepted at NeurIPS 2026** (per the arXiv comment; main-track status not distinguished).
- `2610.11711` **Antichains for Concurrent Parameterized Games — in GandALF 2026 proceedings** (arXiv:2610.08898); full proofs at arXiv:2505.13460.
- No new NeurIPS-2026 game poster surfaced in the window; the proceedings channel was inspected but **not re-harvested**.
- **CoG 2026 IEEE Xplore proceedings remain pending** (expected ~2026-10-16 per the 10-05/10-06 digests) — not re-fetched.

### 9.3 Sibling-claimed papers (withdrawn from §§1–7, not re-summarized)
Eight game-lane papers inside the fresh window are claimed by same-day siblings. Recorded here; **this report does not restate the siblings' findings as its own.**

| arXiv ID | Title | Claimed by | Why it belonged here |
|---|---|---|---|
| `2610.11663` | Constrained Command-Conditioned RL with Bandit Strategy Selection in Real-Time Strategy Games | `arxiv-daily.md` §Games #42 | Game RL: constrained command-conditioned PPO **executor** + Thompson-sampling bandit **strategist** on **MicroRTS** (Netherlands defence-academia). Would have been a §1 feature. |
| `2610.11692` | Can Jev Be Your Q or Policy in Reinforcement Learning? | `arxiv-ai-search.md` Lane D #20 | Game RL: frozen **Jev** decision model as reference policy / exploration judge / replay rater across **9 MiniGrid + 3 Atari** (Shanxi/NJU/CUHK/Tianjin). Directly extends 10-08's Jev thread. |
| `2610.11842` | ConventionPlay: Capability-Limited Training for Robust Ad-Hoc Collaboration | `arxiv-ai-search.md` Lane D #21 | Multi-agent RL: train against a **mixed-adaptability partner population** (Sheffield + CMU). Would have anchored §1/§7. |
| `2610.11450` | Tracing the Thoughts of a Coding Agent Playing ARC-AGI-3 | `arxiv-ai-search.md` Lane D #22 | Game agent: frozen coding agent on interactive reasoning games; artifact-only white-box trace (**AWS**). Would have been a §2/§6 feature. |
| `2610.12341` | AAArena: Heuristic Learning in a Long-Running Game Agent Competition | `arxiv-ai-search.md` Lane D #19 | Game agent benchmark: 12 adversarial games + **1,920 human programs**; Opus5.5 wins 6 gold medals (Tsinghua). Would have been the §2/§5 anchor. |
| `2610.11129` | GameCommBench: A Unified Benchmark and Type-Aware Evaluation for AI-Generated Game Commentary | `arxiv-daily.md` §Games #43 | Game benchmark: commentary across board games/sports/esports + **TACE** type-aware evaluation. Would have been a §5 feature. |
| `2610.11696` | A 3D Characterization Framework for Intelligent Sequential Decision Making | `arxiv-daily.md` §Games #44 | Game/puzzle benchmark: autonomy × skill × cost characterization of graph/RL/LLM solvers on **Tower of Hanoi**. Would have been a §5 feature. |
| `2610.12321` | Spatial Pattern Formation from Multi-Agent Learning in Public Goods Dilemmas | `arxiv-daily.md` §Games #37 | Multi-agent RL in a **game** (spatial public-goods dilemma; tabular Q-learning). Would have been a §1/§7 feature. |

**Not withdrawn (already-claimed or non-game), recorded for completeness**: `arxiv-daily.md`'s Games section also claimed nine **game-theory / economics / mechanism-design** papers — `2610.09985` (LLM pricing+advertising), `2610.06559` (MIRT auctions), `2610.11051` (multi-item auctions), `2610.11675` (delegate pricing), `2610.11074` (budget pacing), `2610.09371` (confidence-signaling game), `2610.09244` (risk-averse MFGs), `2610.07814` (SGDA min-max games), `2610.07491` (LiRA MARL shared constraints). These are **not game-environment papers** and would have been out-of-lane for this digest independently of the claim.

### 9.4 Coverage gaps declared
- The max indexed timestamp across feeds is the **2026-10-08 submission block announced 2026-10-09**; papers submitted 2026-10-09 are not yet indexed and not covered.
- Keyword queries are `max_results ≤ 200` each with `sortBy=submittedDate`; category feeds are `max_results=200` per query (with `start=200` continuations for `cs.AI`/`cs.LG` only) — **not exhaustive for older bands**; backfill beyond the window is not claimed.
- **`2610.12135` (Q-Shaped Options) has no recoverable affiliation** (no HTML author render); marked inline rather than guessed.
- **No CoG 2026 Xplore check, no OpenReview sweep** this run; both are standing deferred channels.

### 9.5 Name-collision and attribution notes
- **"MultiWorldBench" is new** (this run) and is **not** a rename of any prior wiki benchmark; the wiki's earlier world-model benchmarks (`WBench`, `PlayWorld`, `WBench`-class entries on 10-06/10-08) are distinct objects. Cite by ID.
- **"WorldCast"** (this run, distributed multiplayer world model) is unrelated to any earlier `Cast`/`World` acronym in the wiki; no collision found.
- **"Jev"**: today's sibling `arxiv-ai-search.md` §4.20 explicitly disambiguates its Jev paper (`2610.11692`, the RL-component study) from the 10-08 digest's `2610.09188` (the original Jev probability-only model). **Two papers, one model name** — cite by ID.
- **"WorldBench"** (this run, LLM Three.js world generation) vs. the wiki's earlier `WBench`/world-model benchmark references — **different names, different instruments**; no merge.

### 9.6 Method/process note
- The 10-08 run's recommendation (*snapshot the claimed-ID set after all same-day siblings exist*) was honoured: this run's baseline was taken **after** `arxiv-daily.md` and `arxiv-ai-search.md` were on disk, and the eight §9.3 withdrawals are the direct product of that. **0 collisions on the featured set.** The remaining structural cost is visible: when a sibling takes an entire lane (Games), the lane's digest is reduced to residue — a coordination question (who owns which lane, or whether a shared claimed-ID lock file should enforce lane assignment), proposed for the next run.

### 9.7 Caveat on the sibling's own baseline
- The sibling `arxiv-ai-search.md` reports a whole-wiki baseline of **8,295 IDs**; this run's regex sweep returned **8,377** — a +82 delta consistent with the siblings' own additions landing on disk between the two baseline snapshots. Not a discrepancy in method, but recorded so a future run can reconcile the two numbers.
