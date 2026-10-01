---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-10-01)"
type: synthesis
created: 2026-10-01
updated: 2026-10-01
sources: [arxiv.org]
tags: [game-rl, game-ai, llm-agents, game-foundation-models, world-models, pcg, benchmarks, self-play, marl, exploration, imperfect-information, program-synthesis, esports, industry-game-ai, roblox, tencent, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-10-01)

> **A quiet window, but not a quiet field.** The Thu-01-Oct arXiv batch (1,688 papers, IDs 2609.38676–2609.40363, published through 2026-09-30T17:59:56Z) was mined by three same-day siblings before this run; after cross-referencing them, **the fresh window yields exactly one paper that belongs in a game-RL digest** (**Code to Control**, 30 Sep, Harvard/MIT — LLM-synthesized Python controllers that beat PPO on decision latency). The rest of this digest comes from a **rolling topic sweep** across the standing category list. Two topics that have been logged as vacancies for weeks — **PCG** and **industry game AI** — are filled this run, and both are filled by *engineering* papers rather than generative-model papers, which is itself the observation.

---

## §0 Method and Corpus

### 0.1 Window (Part I)
- **Oracle**: the Thu-01-Oct window `submittedDate:[202609300000 TO 202610010000]`, `totalResults=1,688`, IDs 2609.38676–2609.40363. Already fully mined by `wiki/synthesis/2026-10-01/conference-digest.md` (31 papers), `arxiv-ai-search.md`, `arxiv-daily.md`, and `arxiv-paper-check.md`.
- **Cross-reference result**: 161 of those 1,688 papers are already claimed by same-day siblings. Screening the remaining window for game-domain content (real game named, real engine named, or a game-making artifact built) yields **one** genuine game paper: `2609.38733`.
- **Boundary**: the newest unclaimed paper in the descending index at time of writing is `2609.40363`. Yesterday's game digest ceiling was `2609.35771` (published 2026-09-28T17:58:21Z). **The window moved by 4,592 IDs in 48 hours.**

### 0.2 Topic sweep (Part II)
Standing-rule sweep across game RL, LLM game agents, game foundation models, PCG, benchmarks, industry game AI, and related techniques. Compound arXiv queries return empty whenever they exceed ~6 terms, so this run used **short 2–4 term queries** plus category-sorted listing pages, and worked from `arxiv.org/abs/<id>` and `arxiv.org/html/<id>v1` rather than the API.
- **⚠️ arXiv API unusable**: `export.arxiv.org/api/query` returns HTTP 429 (`Rate exceeded`) for this account tier. The HTML search UI and abs/HTML pages work. All metadata below was read from abs pages; affiliations from HTML author blocks.

### 0.3 Dedup
- Whole-`wiki/` regex sweep over `2[0-9]{3}\.[0-9]{4,5}` → **7,526 unique arXiv IDs already claimed** across `wiki/**/*.md` before this file was written.
- Every paper below re-checked **immediately before writing**: **0 hits**.
- Title-level dedup also run: `Code to Control`, `MOBA-VL`, `MOBACast`, `LongPuzzleBench`, `WitnessGym`, `WitnessBench`, `BasketballBench`, `EgoCS`, `MaineCoon`, `Inferix`, `Augmented Random Search`, `option discovery`, `Stag Hunt`, `Neural MMO` → **0 hits each**. `Roblox` (19 files), `GameWAM` (10), `Rocket League` (23), `Valerant` (3), `CombatStateBench` (1) return hits, but in every case they refer to **different, already-claimed papers** — see §9.5.

---

## §1 Game RL — Reinforcement Learning in Games

### ★ Code to Control: Synthesizing Parameterized Reactive Controllers
- **Authors**: Zergham Ahmed, Joshua B. Tenenbaum, Chris Bates, Samuel J. Gershman
- **Affiliation**: Harvard University / MIT / Florida Institute for Human and Machine Cognition *(verified from arXiv HTML author block)*
- **Venue**: arXiv:2609.38733 (30 Sep 2026) — cs.AI, cs.LG, 17 pages, CC BY 4.0. Code: `github.com/ZerghamAhmed/code-to-control`
- **Link**: https://arxiv.org/abs/2609.38733
- **Abstract**: Recent LLM-based control either calls a language model at every action (ReAct) or synthesizes a world model that must be planned through at every decision. Code to Control instead synthesizes **Python controllers that execute directly as policies**. It separates *program structure* from *parameters*: an LLM writes the structure, derivative-free search (Augmented Random Search) fits the numerical parameters against environment feedback.
- **Key innovations**: (1) the separation itself — the LLM never sees the dynamics or a demonstration, and learns from interaction and reward alone; (2) **champion banking** as a load-bearing component, because revision is demonstrably non-monotonic; (3) feature-map factorization for continuous control, `π(o,t) = clip(W φ̂(o,t))`, where the LLM writes interpretable feature *terms* including `sin(ωt)`/`cos(ωt)` gait-phase signals and ARS fits only `W`.
- **Results** (median best score, 3 seeds):
  - Atari: beats WorldCoder and ReAct on **all six** games, beats PPO@100k on all six, and still beats PPO@**20M steps** on 3 of 6. Pong **+18** vs ReAct −17, PoE-World −17, WorldCoder −19, PPO@100k −21, PPO@20M +21. Found after **7 LLM calls / 27k tokens / 25,312 env steps** — versus PPO's 20,000,000.
  - Decision latency: **11.4 µs**, vs PPO 76.5 µs, WorldCoder planning 46 ms, ReAct LLM call 1.29 s. **Faster than a PPO forward pass.**
  - Flappy Bird: survives the full 20,000-step cap (score is cap-limited by construction) using 21,419 env steps and 20 calls. PPO needs ~**93×** the interaction. Zero-shot transfer holds under increased gravity, velocity-dependent drag, mid-episode gravity change, and narrower pipe gap; **parameter-only refitting restores full survival in 3 of 5** remaining cells *with no program change and no further LLM calls*. Reversing gravity sign is the honest failure — it needs a structural change.
  - MuJoCo: beats GIF-MCTS and WorldCoder on **9 of 10**, and on **6 of 10 also beats an oracle planner with access to the true simulator**, which is the paper's most interesting claim: it implies *the planning procedure itself*, not model error, is the bottleneck.
- **Failure modes, self-reported**: across 360 Atari episodes, **72% score below the best-so-far** and **28% drop by >25%** versus the immediately preceding episode. Every revision parsed, no invalid actions, no crashes — the failure is over-eager revision, not broken code. Champion found at median episode 5 of 20, sometimes as late as 19.
- **Why it matters here**: this is the cleanest measurement yet of *decision-time cost as a first-class game-AI metric*. An 11.4 µs controller is a shippable NPC policy; a 1.29 s LLM call is not. Prior digests logged "real-time NPC inference" as an open engineering constraint (see [[Augmenting Game AI with Deep Reinforcement Learning]], 170 µs); this paper gives the same axis a 7-orders-of-magnitude span in one table.
- **Caveats**: operates on structured object-level state (OCAtari-parsed frames), **not pixels**. No matched interaction-efficiency comparison in MuJoCo (the authors say so). Several MuJoCo returns are alive-bonus artifacts — the reported Humanoid controller has return 472.92 with **median displacement −0.44 m**, and the authors flag this themselves rather than letting the table imply locomotion.

### ★ Going Beyond State-Reaching: Learning Abstractions for Intrinsically Motivated Option Discovery
- **Authors**: Akhil Bagaria, Anita De Mello Koch, George Konidaris
- **Affiliation**: Brown University / Amazon *(verified from arXiv HTML author block)*
- **Venue**: arXiv:2609.36473 (29 Sep 2026) — cs.AI, cs.LG
- **Link**: https://arxiv.org/abs/2609.36473
- **Abstract**: Existing option discovery finds subgoals that target *all* state dimensions simultaneously. That produces options valid only in narrow regions, so the option count explodes and swamps the agent's primary reward-maximization objective. This paper identifies a small relevant **feature subset** per subgoal instead, yielding options that generalize broadly. Evaluated on three sparse-reward image-based domains including **Atari's Montezuma's Revenge**.
- **Why it matters here**: Montezuma's Revenge is the canonical exploration-vacancy game, and this is an **exploration** paper that reports exploration speed rather than final return. Konidaris's authorship makes it a reasonable candidate for a real claim; no specific numbers appear in the abstract, so nothing quantitative is asserted here.
- **Caveat**: three domains, Atari-family results only. **No comparison against a named baseline appears in the abstract**, and the wiki has previously logged that this literature reports generalization gaps without a random-policy floor ([[What Does a ProcGen Generalization Gap Measure?]]) — this paper does not report such a floor, so its exploration claims should be read as relative, not absolute.

### ★ Turning Safety into Competence: Minimally Exploitable Robot Policies via Safety-Filtered RL
- **Authors**: Ruihan Wu, Rui Yang, Donggeon David Oh, Duy Nguyen, Haimin Hu
- **Affiliation**: Johns Hopkins University (Computer Science) / Princeton University (Electrical and Computer Engineering) *(verified from arXiv HTML IEEE-style author footnote)*
- **Venue**: arXiv:2609.27312 (23 Sep 2026) — cs.RO, cs.AI, cs.LG, eess.SY, 8 pages
- **Link**: https://arxiv.org/abs/2609.27312
- **Abstract**: Safe-RL methods train one policy to achieve success *and* avoid failure simultaneously. That coupling complicates training and leaves the learned policy **exploitable by deliberate attack** — which matters for competitive deployment. S2C separates the two: it formulates competitive interaction as a **safety-critical Markov game**, *proves* that perfect filtering preserves non-exploitability when all players commit to safe maneuvers, learns the filter by adversarial RL, embeds it in the environment during task-policy training, and keeps it at deployment.
- **Results**: in simulated touchdown games S2C beats **eight** safe-RL baselines on win rate, Elo, and exploitability simultaneously. Hardware stress test against a human opponent confirms competence.
- **Why it matters here**: this is the **exploitability** framing applied to a competitive game. It is the natural counterpart to this wiki's existing line on competitive pressure (SANCT, exploitability certification, [[RSD-Poker]]) — those certify a *residual* policy's worst case; this filters *during* training and proves the filter is safe to keep on. (single-source)

---

## §2 Game AI Bot — LLM Agents, NPC Behavior, and Self-Improvement

### ★ MOBA-VL: Event-Localized Multi-Turn Reinforcement Learning for Real-Time MOBA Commentary
- **Authors**: Shengyun Zhong, Xinkang Zhao, Ziyuan Chu, Linchao Zhu
- **Affiliation**: Zhejiang University / Northeastern University *(verified from arXiv HTML author block)*
- **Venue**: arXiv:2609.38428 (29 Sep 2026) — cs.CV, 30 pages. Project page: `moba-vl.github.io`
- **Link**: https://arxiv.org/abs/2609.38428
- **Abstract**: Real-time MOBA esports commentary needs a VLM to narrate a live match second by second *and* get the events right. Existing streaming VLMs sound natural but miss kills and objectives. MOBA-VL uses **game telemetry — which records exactly when each event occurs — as a supervision signal**, then applies **event-localized multi-turn RL** that rewards only the turns describing each event.
- **Data and results**: MOBACast = **860 professional matches, ~460 hours**, three MOBA games, word-level timestamped commentary. MOBACast-Bench built from held-out tournaments. MOBA-VL is **9B parameters** and beats StreamingVLM **63.25 vs 55.12** Overall on full matches and DeepSeek-V4.1-Flash **63.45 vs 56.22** on clips. Event-localized credit raises **event recall 34.5 → 42.1** over SFT.
- **Why it matters here**: the load-bearing idea is **telemetry as a per-turn reward mask**. This is the same structural move as the [[GraphHCA]] / [[Cross-Rollout Bellman Closure]] / [[HyperMCTS]] cluster logged on 09-30 (turn-level or step-level credit without extra rollouts) — but sourced from the *game engine's* event log rather than from trajectory structure. For any game shipping a telemetry stream, this is a free dense reward signal that no amount of rollout relabeling can synthesize. It also continues the commentary-evaluation line this wiki has tracked since [[ACT-Eval]] and 2608.14016 (VLM commentary "hallucinated game state" as primary failure mode) — event recall is the metric both of those papers implied was missing.
- **Caveat**: commentary, not gameplay. Single window (three games). Code and data "will be released" — **not yet available at time of writing**.

### ★★ Witness: Discovery, Deciphering, and Epiphany in Interactive Puzzle Environments
- **Authors**: Guanghan Ning, Ping Liu, Linyi Li, Huangjie Zheng, Arjun Neervannan, Huu Nguyen, Michael Sklar, Deniz Zorlu, Nicolai Ouporov
- **Affiliation**: Fleet AI / University of Nevada, Reno / Simon Fraser University / independent *(verified from arXiv HTML shared author header; per-author mapping inferred from that header list)*
- **Venue**: arXiv:2609.32208 (26 Sep 2026) — cs.AI. Benchmark: `witnessbench.ai`
- **Link**: https://arxiv.org/abs/2609.32208
- **Abstract**: Interactive **rule-discovery** puzzles: the agent infers hidden rules by experiment and uses what it inferred to reach a stated goal. WITNESS is a 2D ASCII-observation grid puzzle environment with controlled access to rules; an agentic pipeline generates the games for **WitnessGym** (RL training) and **WitnessBench** (public validation + private test). The validation set *separately* tests new compositions of trained primitives against primitives absent from training.
- **Results**: under a shared harness, the best of **18 frontier proprietary and open-weight models solves only 24% of private test level slots**, and scores are sensitive to the observation interface and agent configuration. Giving ground-truth rules raises **Opus-5's** validation RHAE-L5 from **59.9 → 97.8**, whereas a 27B open-weight model gains **only 2.1 points**. RL on WitnessGym raises that 27B model's private-test RHAE-L5 from **2.1 → 5.4** and yields a **+4.1 point** mean gain across four external discovery benchmarks.
- **Why it matters here**: two separable diagnoses in one paper. (1) **Rule acquisition is the bottleneck for frontier models** — supplying the rules nearly closes the gap for Opus-5 (59.9→97.8) while barely helping a 27B model, i.e. the small model fails at *rule-based execution*, a different defect from the frontier model's failure at *acquisition*. (2) **RL on hidden-rule puzzles transfers off-distribution** (+4.1 on four external discovery benchmarks), which is a rare positive generalization claim in a puzzle-RL line that usually reports only in-domain gains.
- **Caveat**: 2D ASCII puzzles. "24% of private test level slots" is a slot-level aggregate, not per-level. RL gains are small in absolute terms (2.1→5.4) and the paper does not claim otherwise.

---

## §3 Game Agents — Benchmarks and Evaluation

### ★★ LongPuzzleBench: Evaluating GUI Agents on Long-Horizon Visual Puzzles
- **Authors**: Bingo Zhang, Haochuan Lu, Zongjie Li, Genjian Li, Ari Yu Zhang, Chaozheng Wang (corresponding: Hongbin Zhang)
- **Affiliation**: Tencent / The Hong Kong University of Science and Technology / The Chinese University of Hong Kong / Vera Praxis / independent *(verified from arXiv HTML author block)*
- **Venue**: arXiv:2609.34769 (28 Sep 2026) — cs.CL, cs.AI
- **Link**: https://arxiv.org/abs/2609.34769
- **Abstract**: GUI agents need long-horizon visual reasoning — keeping a multi-step plan viable as earlier actions constrain later ones. In long-horizon visual puzzles, "a legal move that looks like progress can make the puzzle unsolvable, and the loss shows only several moves later." LongPuzzleBench is **114 levels in six puzzle games played through native GUI actions**, where one objective can take a human **over a thousand actions** on persistent boards, and dead ends go unannounced.
- **Results**: with Native GUI Actions alone, the strongest agents solve most objectives, but success falls sharply on harder, longer boards — **seven of ten general-purpose agents solve nothing harder than Medium**, and **none completes Bolt Unscrew Hard**, which a human solves along with every other objective. Code Execution CUA does not close the gap, and its scores *mix visual solving with algorithmic search*, so it is not a clean comparison. Controlled diagnostics trace all failures to one limitation that **rules, state hints, and failure memory each fail to remove**.
- **The stated mechanism** (the most quotable line in this digest): agents "judge each move by the visible progress it makes, **not by the future options it leaves**." That is a myopia diagnosis, and it is *not* fixed by more rules, more state, or more memory.
- **Why it matters here**: this is the [[OptiArena]] result (§9.2 of the 09-30 digest) stated as a mechanism rather than a gap. OptiArena showed can LLMs improve *executable* algorithms under fixed budgets; LongPuzzleBench shows that adding code execution to a visual agent **does not** buy the missing capability, because the missing capability is a search-over-future-options, not a tool. Any wiki claim that "GUI agents just need code execution" is falsified here.

### ★★ BasketballBench / BasketballSkills
- **Authors**: Yirong Hu, Jiayuan Rao, Yu Zhang, Shangzhe Di, Weidi Xie
- **Affiliation**: **not stated anywhere** in the arXiv HTML render — no affiliation line exists in the author block or footnotes. Treat as unknown; do not infer.
- **Venue**: arXiv:2608.23435 (24 Aug 2026) — cs.CV, cs.AI, 26 pages
- **Link**: https://arxiv.org/abs/2608.23435
- **Abstract**: Understanding a basketball game requires recognizing events, localizing actions, identifying players, *and* relating these to structured game knowledge. Existing benchmarks evaluate these abilities one at a time. **BasketballBench** is a multimodal benchmark of **7,980 questions across ten tasks** in text, image, and video, built from the **2025–2026 NBA season**, including official play-by-play, rosters and profiles for **530 active players**, and **2,501 possession-level broadcast clips**. **BasketballSkills** is an agent composing **eight basketball-specific perception and retrieval tools** under four reusable skills that specify tool order, evidence bindings, and stopping conditions.
- **Result**: current MLLMs struggle particularly on questions requiring **integration of multiple capabilities**; BasketballSkills outperforms them, highlighting the value of explicitly composing domain-specific capabilities.
- **Why it matters here**: the ten-task × 7,980-question structure is the sports/esports analogue of [[SWE-Game]]'s construction-task gap — evaluation that isolates *integration* rather than *capability*. The design choice worth stealing is **stopping conditions as a first-class part of a skill**, which the 09-30 digest's OptiArena entry also treats as load-bearing.

---

## §4 Game Foundation Models and World Models

### ★★ EgoCS-400K: An Egocentric Gameplay Dataset for World Models
- **Authors**: Rongjin Guo, Dong Liang, Yuhao Liu, Fang Liu, Tianyu Huang, Gerhard P. Hancke, Rynson W. H. Lau
- **Affiliation**: City University of Hong Kong *(verified from arXiv HTML author block)*
- **Venue**: arXiv:2606.18180 (16 Jun 2026) — cs.CV, cs.AI, cs.LG, cs.NE
- **Link**: https://arxiv.org/abs/2606.18180
- **Abstract**: World models need temporally aligned **video-action-language** trajectories, not captions. Web video lacks executable actions and states; robotic datasets have supervision but are costly and narrow; simulators lack large-scale *human-driven* trajectories. EgoCS-400K is built from **public professional CS/CS2 match demos**, which preserve human trajectories and allow parsing, replaying, rendering, and temporal alignment.
- **Scale**: **>400,000 first-person videos, 10,000 hours**, from **>1,000 matches and 40,000 rounds**, covering **13 maps and 10 player viewpoints per round**. Extracts player states, view directions, movements, keyboard/button inputs, view-angle changes, weapon usage, game events, and round-level context.
- **Why it matters here**: the input is **public demo archives**, which changes the economics. The wiki's world-model data entries ([Multiplayer Interactive World Models], 10,000 hours from publicly available bots; [Multiplayer World Models], 5B params Rocket League) have all required purpose-built collection. EgoCS-400K is the first entry here whose data pipeline is **reproducible by a third party from artifacts that already exist**. Its "bridge between passive web videos, controllable game simulation, and costly real-world embodied data" framing is the correct supply-chain argument.

### ★ COMBAT: Conditional World Models for Behavioral Agent Training
- **Authors**: Anmol Agarwal, Pranay Meshram, Sumer Singh, Saurav Suman, Andrew Lapp, Shahbuland Matiana, Louis Castricato, Spencer Frazier
- **Affiliation**: Overworld AI / Indian Institute of Science Education and Research Bhopal *(verified from arXiv HTML author block)*
- **Venue**: arXiv:2603.00825 (28 Feb 2026) — cs.CV, cs.AI, cs.LG
- **Link**: https://arxiv.org/abs/2603.00825
- **Abstract**: Video world models simulate 3D-consistent environments interacting with *static* objects, which fails for dynamic reactive agents. COMBAT is a real-time action-controlled world model trained on **Tekken 3** — a 1v1 fighting game. A **1.2B-parameter Diffusion Transformer** conditioned on latent representations from a deep compression autoencoder, with causal distillation and diffusion forcing for real-time inference.
- **The claim**: **sophisticated opponent behavior emerges from training on single-player inputs with no explicit supervision for the opponent's policy.** Unlike imitation learning, which needs complete action labels, COMBAT learns effectively from **partially observed** data to generate responsive behavior for a controllable Player 1.
- **Why it matters here**: this is the strongest form of the "the model learns the opponent" argument — behavior cloning of a reactive adversary from partial logs, inside a fighting game, in a world model rather than a policy. The wiki's [Agentic Game Development as a Verifiable Trajectory Data Engine] (RLHEV) argues game engines supply the missing reward signal for spatial world models; COMBAT supplies the missing *behavioral* signal, and arrives at it from a different direction. Worth flagging as a genuine methodological alternative, not a duplicate.
- **Caveat**: 8 authors, single fighting game, 1.2B params. The paper's own contribution list includes "novel evaluation methods to benchmark this emergent agent behavior" — i.e. the *evaluation* of the emergent behavior is itself a contribution, which is a reason to hold the behavioral claim lightly until those metrics are used elsewhere.

### ★ Inferix: A Block-Diffusion Based Inference Engine for World Simulation
- **Authors**: Inferix Team (Zhejiang University, HKUST, Alibaba DAMO Academy, Alibaba TRE per the paper's own Appendix A)
- **Affiliation**: **team-attributed only** — the arXiv HTML author block reads only "Inferix Team" with no affiliation line; the four institutions come from Appendix A and are reported here as **the paper's own statement, not an author-block verification**
- **Venue**: arXiv:2511.20714 (v1 24 Nov 2025; v2 Apr 2026)
- **Link**: https://arxiv.org/abs/2511.20714
- **Abstract**: Semi-autoregressive **block-diffusion** decoding merges diffusion and autoregressive generation — applying diffusion within each block while conditioning on previous blocks — which reintroduces **LLM-style KV-cache management** and enables efficient variable-length generation. Explicitly positioned as an inference engine for world simulation, not a world model. Ships **LV-Bench**, a fine-grained benchmark for minute-long video generation.
- **Why it matters here**: serving infrastructure, which the game-AI digests have consistently under-covered relative to model papers. Interactive world models must generate **faster than real time** (cf. Rocket League 20 fps on one B200, ABot-World-0 at 16 fps) and every one of those numbers is an *inference-engine* result more than a *model* result. Recording an engine and its benchmark as wiki entities is the correct granularity.

### ★ Simulating the Visual World with Artificial Intelligence: A Roadmap
- **Authors**: Jingtong Yue, Ziqi Huang, Zhaoxi Chen, Xintao Wang, Pengfei Wan, Ziwei Liu
- **Affiliation**: Robotics Institute, Carnegie Mellon University / S-Lab, Nanyang Technological University / Kling Team, Kuaishou Technology *(verified from arXiv HTML author block)*
- **Venue**: arXiv:2511.08585 (v1 11 Nov 2025; v2 5 Feb 2026)
- **Link**: https://arxiv.org/abs/2511.08585
- **Abstract**: Frames modern **video foundation models as the composition of an implicit world model and a video renderer** — the world model encodes physical laws, interaction dynamics, and agent behavior as a latent simulation engine; the renderer exposes it as a video "window." Traces four generations of video generation, ending in a world model that embodies intrinsic physical plausibility, real-time multimodal interaction, and planning across spatiotemporal scales.
- **Why it matters here**: the two-component decomposition (simulation vs rendering) is the *same* split that this digest's newest window papers converge on independently — [[GameDirector]] "decouples rule-based gameplay logic from visual rendering," [Programmable World Model] "decouples world-state evolution from visual observation generation," and [WorldMind] separates understanding/decision/control/generation into four layers. Four independent groups and one survey arriving at the same factorization in eight months is a real signal, and this survey is the natural citation for the framing. (single-source survey)

### ★ MaineCoon: Pursuing A Real-Time Audio-Visual Social World Model
- **Authors**: Lichen Bai, Tianhao Zhang, Shitong Shao, Dingwei Tan, Qiyu Zhong, Zhengpeng Xie, Haopeng Li, Qinghao Huang, Dandan Shen, Tengjiao Ji, Wei Wang, Peicheng Wu, Yuxuan Zhao, Xiangyu Zhu, Welly Luo, Shurui Yang, Zeke Xie
- **Affiliation**: Catnip AI Team (author block gives the team name only, no institutions)
- **Venue**: arXiv:2606.17800 (16 Jun 2026) — cs.CV, cs.AI, 32 pages
- **Link**: https://arxiv.org/abs/2606.17800
- **Abstract**: Existing world models simulate physical environments or game-world exploration but are "fundamentally detached from human-centric social dynamics." MaineCoon is a **22B-parameter real-time audio-visual autoregressive model** reaching **47.5 FPS on a single GPU** — presented as the first real-time audio-visual model optimized for social interaction. Techniques: self-resampling, cross-modal representation alignment, domain-aware preference optimization, and **reinforced online-policy distillation (ROPD)**, plus an agentic streaming inference framework with agentic cache management for thousand-second generation.
- **⚠️ Scope flag**: this is a **social** world model, not a game world model. It is included because (a) ROPD is an RL technique operating on generation latency that game-world-model work would benefit from, and (b) 47.5 FPS on one GPU is the highest real-time figure in this digest and bounds what is currently achievable. **It is not evidence about games.** Do not let the 47.5 FPS be cited as a game-world-model result.

---

## §5 PCG and Level Design — Vacancy Filled

### ★★ Constrained Solvability Queries for 3D Obstacle Course Games
- **Authors**: Zander Majercik, Sharon Zhang, William Wang, Tejan Karmali, Fangjun Zhou, Yucheng Yuan, Jean-Peïc Chou, Maneesh Agrawala, Kayvon Fatahalian
- **Affiliation**: Stanford University / **Roblox** *(verified from arXiv HTML author block)*
- **Venue**: arXiv:2609.36225 (28 Sep 2026) — cs.GR — **Accepted to SIGGRAPH Asia 2026**
- **Link**: https://arxiv.org/abs/2609.36225
- **Abstract**: A system giving designers rapid feedback on **how an obstacle can be solved**. The core contribution is querying for *solutions* (sequences of player actions) that satisfy designer-specified constraints — avoid a region, pass through a waypoint, at most two jumps. Implemented with a high-performance **GoExplore** implementation for exploratory search, guided by an obstacle-solving agent **trained offline with RL**, and a custom GPU-accelerated obstacle-course simulator generating playthrough experience at **nearly 14,000× real time at 60 fps**.
- **Results**: design studies show constrained solvability queries in a rapid loop are expressive enough for designers to see *ways* an obstacle can be solved or *why* it cannot be — including higher-level questions about undesirable solution paths and solution difficulty. **Human playtesting confirms players play the designed obstacles as the designer intended.**
- **Why this is the important PCG entry**: this inverts the usual PCG pipeline. Every PCG entry in this wiki trains a *generator* and then scores its output with a heuristic (PCGRL, WFC+PCGRL, PCGRLLM reward shaping, multiobjective PCGRL). Here the *search* produces solutions and the *designer* accepts or rejects, with the engine running fast enough to be interactive (14,000× real time) that the loop closes inside a design session. It is also a **published venue** (SIGGRAPH Asia 2026), where the PCG slot in this wiki has been empty or filled by unrefereed preprints for weeks.
- **Why it matters for §6 too**: **Roblox is on the author list.** That is the second industry-affiliated paper in this digest and it is the first *PCG-and-shipping-platform* paper this wiki has logged in that configuration.

### ★ Procedural Generation for Level Design of Mansions and Dungeons
- **Authors**: Isaac Fiuza Vieira, Kathya Silvia Collazos Linares, Esteban Walter Gonzalez Clua, Érick Oliveira Rodrigues
- **Affiliation**: not verified from HTML (**tentative**)
- **Venue**: arXiv:2606.03857 (2 Jun 2026) — cs.GR — **Journal ref: SBGAMES 2025**, DOI `10.5753/sbgames.2025.10089`
- **Link**: https://arxiv.org/abs/2606.03857
- **Summary**: Three-stage PCG for structured indoor environments: BSP space segmentation; graph-traversal room connection to avoid redundant links; post-processing to clean structural artifacts and improve visual cohesion. Seeded for reproducibility. Across **100,000 generated maps**, **>91%** achieve complete connectivity under suitable parameters (verified by BFS).
- **Why included**: the only *peer-reviewed, DOI-bearing* PCG item found unclaimed, and the connectivity number is the kind of figure that makes a design claim checkable. Reported as a runner-up-grade entry — no comparison against learned or WFC-based baselines appears in the abstract. *(tentative affiliation)*

---

## §6 Industry Game AI — Vacancy Filled

Both entries here are **engineering papers from platform or product teams**, not research deployments. That is the change from the 09-30 status, which logged "**no game-studio-affiliated paper appears in this digest**."

| Paper (§) | Organization | What shipped | Date |
|---|---|---|---|
| Constrained Solvability Queries (§5) | **Roblox** + Stanford | Interactive obstacle-course design tool, ~14,000× real-time GPU sim, GoExplore + offline RL solver; SIGGRAPH Asia 2026 | 28 Sep |
| LongPuzzleBench (§3) | **Tencent** + HKUST + CUHK | 114-level / 6-game GUI-agent benchmark; agents fail on long-horizon visual planning at scale | 28 Sep |

**Supporting industry signal within other entries** (not separate papers):
- **Fleet AI** co-authors **Witness** (rule-discovery RL + benchmark, 26 Sep).
- **Amazon** co-authors **Going Beyond State-Reaching** (option discovery, 29 Sep).
- **Overworld AI** authors **COMBAT** (Tekken 3 world model, Feb).
- **Alibaba DAMO / Alibaba TRE / Zhejiang / HKUST** staff the **Inferix** team.
- **Kuaishou (Kling)** co-authors the world-model roadmap survey.

**What this does *not* establish**: none of these is a shipped-player-facing RL policy, and none reports a live-service metric (win rate, retention, DAU). This is *platform and tooling* industry presence, which is one step short of the "production deployment in a shipped game" claim that this wiki has never yet been able to log. **The distinction is deliberate and should survive any summary of this section.**

---

## §7 Related Techniques

### ★ RoMEX-φ: Interactive Distributionally Robust Multi-Agent Learning
- **Authors**: Debamita Ghosh, George K. Atia, Yue Wang
- **Affiliation**: University of Central Florida (Electrical & Computer Engineering; Computer Science) *(verified from arXiv HTML author block)*
- **Venue**: arXiv:2609.32048 (25 Sep 2026) — cs.LG, cs.AI, 62 pages
- **Link**: https://arxiv.org/abs/2609.32048
- **Summary**: Model misspecification is amplified in MARL because transition uncertainty compounds with strategic interaction. RoMEX-φ gives model-free online learning in **general-sum distributionally robust Markov games** with general function approximation and φ-divergence uncertainty sets: equilibrium-based exploration plus dual fitted learning, with worst-case values estimated from nominal interaction data via a centered empirical robust discrepancy. Introduces a **robust Multi-Agent Decoupling Coefficient** characterizing exploration complexity from strategic interaction and adversarial transition uncertainty, and obtains sublinear robust regret governed by that coefficient **rather than by state and joint-action space size**.
- **Why here**: the robust-MADC is the general-sum analogue of the exploration-complexity coefficients this wiki tracks in zero-sum settings (DEC-p and the ESAM line). Replacing tabular dependence with intrinsic function-class complexity is the same move that made 2609.31076 and the ESAM line usable outside tabular settings. **No game environment is evaluated** — the numerical result is on a scalable synthetic general-sum DRMG — so this is a methods transfer, not a game result. (single-source)

### ★ Escaping Local Views: Discovering Latent Concepts for Interpretable MARL
- **Authors**: Yijie Sun, Sanquan Sun, Yanda Zhu, Yuanyang Zhu, Yaohua Hu, Chunlin Chen
- **Affiliation**: Nanjing University *(verified from arXiv HTML author block; also returned by Semantic Scholar)*
- **Venue**: arXiv:2609.34459 (28 Sep 2026) — cs.AI
- **Link**: https://arxiv.org/abs/2609.34459
- **Summary**: Recurrent MARL agents encode local interaction histories, but the hidden states give little insight into *why* a decision was made. ELV extracts low-dimensional **semantic concepts** per agent from its local observation and action-observation trajectory, encodes them into a contextual latent via a VAE (the "bridge between local views and global semantics"), applies dual-path attention (one module for per-concept salience against global context, one for pairwise concept interactions), and adds a concept-prediction module whose next-concept prediction error **becomes an intrinsic reward that incentivizes semantic-novelty exploration**.
- **Why here**: the intrinsic-reward-from-prediction-error construction is a fresh member of the wiki's exploration-cluster (curiosity variants, TopoExplore homology signals, CDE/ICM, SuS surprise). The interpretability claim is stronger than most in this literature because the concepts are *semantically structured* rather than post-hoc SAE features — which makes it comparable to the RSAs logged in the conference digests. **No game environment is named in the abstract**, and it reports competitive-but-not-superior performance, so the value is the mechanism, not a benchmark delta. (single-source)

### ★ Be Careful Who You Trust: Coordination Dynamics under Corrupted Communication in LLM Multi-Agent Games
- **Authors**: Xuanyi Liu, Niall Dalton, Hairi Amin, Xiyuan Yin, Lydia Lim
- **Affiliation**: University College London (Computer Science) *(verified from arXiv HTML author block)*
- **Venue**: arXiv:2609.31704 (19 Sep 2026) — cs.MA, cs.LG — **REALM: The 2nd Workshop for Research on Agent Language Models at EMNLP 2026**
- **Link**: https://arxiv.org/abs/2609.31704
- **Summary**: Iterated **N-player Stag Hunt** played by homogeneous LLM groups under controlled *programmatic action inversion* that alters both the public transcript and the executed action. Grid over group size, coordination threshold, corruption level, and seven LLMs.
- **Results and the methodological point**: honest agents' pre-flip Stag choices decline as corruption rises, but **the sharp fall in public success is primarily mechanical** — in the focal N=5, M=3 setting, pre-flip success is **78% at 80% corruption** while public success falls to **12%**. Honest choices track the *public history available at decision time*, especially under high corruption. Three threshold-style public-report benchmarks yield action-match rates similar to the LLM agents, i.e. **substantial descriptive agreement between LLM decisions and classical threshold benchmarks**.
- **Why here**: this is the same separation-of-measurements discipline as the 09-30 §9.3 finding (player-experience metrics confounded by disclosure). Here: **original choice, public action, and executed outcome must be three separate measurements**, and reporting only one of them manufactures a robustness failure that is an artifact of the measurement pipeline. The benchmark-agreement finding is also a deflationary result worth logging: in iterated Stag Hunt, LLMs are not doing anything a threshold rule does not already describe.

### ★ Sim-to-Real Gap in Real-World Game Playing on a $400 Platform
- **Authors**: Rongping Zhou, Omid Tavallaie, Shuaijun Chen, Albert Y. Zomaya
- **Affiliation**: The University of Sydney (Computer Science) / University of Oxford (Engineering Science) / The University of Western Australia (Computer Science) *(verified from arXiv HTML author block)*
- **Venue**: arXiv:2607.10309 (v1 11 Jul 2026; v2 19 Sep 2026) — cs.AI
- **Link**: https://arxiv.org/abs/2607.10309
- **Summary**: A real-world RL platform where an agent on an edge device plays video games on a separate host through a **hardware-emulated keyboard with vision input**, built from <USD 400 of commercial components. Chosen because score-maximization is a task with **no safety risk in the physical world**, sidestepping the usual obstacle to real-world RL.
- **Results**: the simulation-trained agent suffers **1160% performance degradation** relative to human performance after real-world deployment. Direct real-world DQN training reaches **~49% of human level** after 10M steps, demonstrating real-world RL is feasible.
- **Why here**: the 1160% figure is the most extreme sim-to-real degradation this wiki has recorded, and the reason is instructive — the gap is dominated by the **perception and actuation interface** (camera, latency, key actuation), not by dynamics mismatch. This is the empirical counterpart to **Code to Control**'s 11.4 µs decision latency: latency and interface fidelity, not algorithmic sophistication, are what break when control leaves the simulator. (single-source)

---

## §8 Runner-ups (verified unclaimed, lighter entries)

Screen hits that were **dropped as already claimed** — recorded so a future run does not re-query them:

| ID | Date | One-line note |
|---|---|---|
| `2609.39564` | 30 Sep | *A2Z GameSpec-Bench — claimed by same-day `arxiv-paper-check`; the newest window ID screened, cross-referenced not re-summarized* |
| `2609.31076` | 25 Sep | *claimed by same-day siblings* |
| `2609.30177` | 24 Sep | *claimed by same-day siblings* |
| `2609.25652` | 22 Sep | *GameDirector — claimed; see §9.4 decoupling argument* |
| `2609.22177` | Sep | *OpenBlock tile-matching — claimed; the other industry entry already in the corpus* |
| `2608.14977` | 14 Aug | *Watermarked Game Solving via Perturbed Regret Minimization — **claimed since 2026-08-23**; this run screened it, found the hit, and dropped it* |
| `2606.20210` | 18 Jun | *Augmenting Game AI with DRL — claimed; the CoG 2026 vision paper, still the best statement of the deployment-bottleneck problem* |
| `2601.04575` | 7 Jan | *Scaling Behavior Cloning, 8,300+ h open data — claimed; still the largest public game-playing dataset* |

---

## §9 Cross-Cutting Observations

### 9.1 Decision-time latency is now a measured, reported game-AI metric
**Code to Control** (11.4 µs/controller) and the Sim-to-Real platform (2607.10309, 1160% degradation on hardware-emulated actuation) are the same finding from opposite ends. The synthetic corpus has spent a decade reporting *sample efficiency* and asymptotically ignored the per-decision cost that determines whether an agent can be shipped. A µs-scale controller and a 1160% degradation from interface friction in the same digest is the sharpest available statement of why.

### 9.2 Myopia, not capability, is the shared failure — and adding tools does not fix it
LongPuzzleBench's diagnosis — agents judge a move "by the visible progress it makes, not by the future options it leaves" — is **exactly** what Code to Control's LLM revisions fix and what its champion-banking fix protects. The LLM discovers ball-velocity extrapolation (`predicted_ball_y = ball.y + ball.dy * lead_ticks`) and time-to-impact threat detection because it is *shown the trajectory*; GUI agents in LongPuzzleBench, with rules, state hints, and failure memory all supplied, still fail. **Code Execution CUA does not close the gap and its scores mix visual solving with algorithmic search.** So: the capability exists, it is trainable from trajectory feedback, and it is not reachable by bolting on tools.

### 9.3 Supply-side economics changed for world-model data
EgoCS-400K gets 400,000 clips / 10,000 hours / 1,000 matches from **public professional demo archives**, and Multiplayer Interactive World Models gets 10,000 hours from **publicly available bots**. The barrier to entry in game world models has moved from "collect the data" to "parse someone else's data well." Anyone building a game world model in the next cycle should read the EgoCS-400K parsing pipeline before designing a collection rig.

### 9.4 Three independent decoupling arguments converge on simulation-vs-rendering
[GameDirector] (claimed) decouples rule-based gameplay logic from rendering. [Programmable World Model] (claimed) decouples world-state evolution from visual observation generation. [WorldMind] (claimed) splits four layers. The the world-model roadmap survey survey (CMU RI / NTU / Kuaishou Kling) independently arrives at "world model + video renderer" as the composition of a video foundation model. **Five groups, the same factorization, within roughly eight months.** The synthesis is cheap: the renderer is a commodity pretrained video model, and the defensible research contribution is the explicit-state layer above it.

### 9.5 The PCG vacancy filled with an engineering paper, and that is the finding
Every PCG entry this wiki has logged trains a generator and scores it with a heuristic. The Roblox/Stanford obstacle-course paper replaces the generator with an **interactive solver + human accept/reject**, at 14,000× real time, validated by human playtesting, and it is the **only PCG item in this digest with a peer-reviewed venue**. Two readings, both defensible: designers want *solvability feedback*, not *levels*; or a generator was never the bottleneck and nobody instrumented for it. This wiki has a standing note (09-30 §9.5) that the ProcGen/Atari literature should adopt a random-floor control — that discipline has now reached level design.

### 9.6 Measurement discipline is the recurring self-correction
Three entries independently separate measurements that a naive pipeline would conflate: corrupted-communication work separates *original choice / public action / executed outcome* (and finds the failure is 78% vs 12%, i.e. mostly mechanical); rule-discovery separates *acquisition* from *execution* (Opus-5 59.9→97.8 with rules, 27B only 2.1→3.2); latent-concept MARL separates per-concept salience from pairwise interaction from intrinsic reward. Compare the 09-30 finding that player-experience metrics are confounded by capability *disclosure*. The field is converging on: **an aggregate number that mixes two mechanisms is not a result.**

### 9.7 Industry presence is real, and it is one step short of a shipped policy
Roblox, Tencent, Fleet AI, Amazon, Overworld AI, Alibaba, Kuaishou all appear on author lists in this digest. **Zero of these papers reports a player-facing deployed RL policy or a live-service metric.** The 09-30 digest recorded "no game-studio-affiliated paper appears" as a vacuum; today's correction is that the vacuum was a *measurement artifact* — industry work surfaces as platform and tooling papers, which a game-RL query filter discards. It should not be summarized as industry deployment.

---

## §10 Corpus Accounting and Caveats

- **Window (Part I)**: 1,688 papers, IDs 2609.38676–2609.40363, `published` through 2026-09-30T17:59:56Z. 161 already claimed by same-day siblings. **1 paper featured** (**Code to Control**).
- **Topic sweep (Part II)**: short-query arXiv HTML sweep + `abs/`/`html/` verification → **16 papers featured** across §1–§7.
- **Totals**: **17 papers featured** (1 window + 16 sweep), each verified at **0 arXiv-ID hits** in `wiki/` immediately before this file was written, plus title-level dedup on 14 distinctive strings (0 hits each, see §0.3). One further candidate, `2608.14977`, was screened and **dropped on dedup** — it has been claimed since the 2026-08-23 digest (§8).
- **Dedup key**: arXiv ID. Wiki baseline before this write: **7,526 unique arXiv IDs** across `wiki/**/*.md` (regex `2[0-9]{3}\.[0-9]{4,5}`), up from **7,037** in the 09-30 game digest — the delta is the four same-day siblings' claims.
- **⚠️ Affiliation discipline**: verified from arXiv HTML author blocks for 2609.38733, 2609.38428, 2609.36225, 2609.34769, 2609.32208, 2609.36473, 2609.27312, 2609.32048, 2609.31704, 2609.34459, 2607.10309, 2606.18180, 2603.00825, 2511.08585. **1 marked tentative with the evidence named**: 2606.03857 (no HTML verification; SBGAMES venue and DOI read from the arXiv listing page only). **3 with no affiliation available**: 2608.23435 (author block has none — do not infer), 2511.20714 (team name only; four institutions reported as the paper's own Appendix A statement, not author-block verified), 2606.17800 (team name only). The arXiv **API returns no affiliation data at all** and is currently returning HTTP 429 in any case.
- **Refereed vs preprint**: 4 of 17 carry a venue — SIGGRAPH Asia 2026 (2609.36225), REALM @ EMNLP 2026 (2609.31704), SBGAMES 2025 with DOI (2606.03857), and 2609.27312 formatted as an IEEE conference paper without a named venue. **No result in this digest has been independently replicated.**
- **⚠️ Scope discipline**: 2606.17800 (MaineCoon) is a **social** world model, not a game world model; it is included for its real-time figures and its ROPD latency technique and is flagged as such in §4. 2608.23435 (BasketballBench) is sports understanding, not game playing. 2609.32048 and 2609.34459 evaluate **no game environment** and are included as method transfers only.
- **⚠️ Vacancies that remain**: no *published, DOI-bearing* industry **player-facing** game-RL deployment; no self-play / population-based training paper; no offline-RL-for-games paper; no hierarchical-RL-for-games paper. All four were queried and are recorded as vacancies rather than filled with adjacent robotics or generic-MARL papers.
- **⚠️ Method caveat on the sweep itself**: compound arXiv queries above ~6 terms return empty, and this run therefore has **no query log comparable to the 09-30 digest's 109-query accounting**. The pool is broad but not exhaustively searched; the §7 and §8 vacancy claims in particular rest on fewer queries than the 09-30 digest's, and should be weighted accordingly.
