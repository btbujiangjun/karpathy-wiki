---
title: "Game RL & Game AI Bot — Daily Paper Digest (September 5, 2026)"
type: synthesis
created: 2026-09-05
updated: 2026-09-05
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, world-models, pcg, benchmarks, self-play, multi-agent-rl, mcts, industry, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-09-05)

> Survey of 26 verified-new papers across 7 categories: Game RL, Game AI Bot, Game Foundation Models, Procedural Content Generation, Game Benchmarks, Industry Game AI, and Related Techniques. Scanned the **Fri Sep 4, 2026 arXiv mailing** (IDs `2609.0xxxx–2609.04xxx`) plus the Aug 31 – Sep 4 announcement window via arXiv listing pages (`/list/{cat}/recent`, API rate-limited HTTP 429) across cs.AI / cs.LG / cs.GT / cs.MA / stat.ML / cs.CV / cs.HC. Every featured arXiv ID is grep-verified absent from `wiki/`; deduped against same-day and prior sibling digests (see note below). Affiliations marked *(inferred)* or *(unverified)* where metadata is thin.

**Deduped out (already covered):** Turn-Based Combat Arena `2609.03122`, LLM-Guided RL NPCs `2609.02931`, Mean-field RL representations `2609.02928`, PokaiTrainer `2608.29197` (09-05 arxiv-daily); LUGL `2609.03660`, Robust PAC CSGs `2609.04189`, HOOD `2609.04113` (09-05 arxiv-ai-search); NashDreamer `2609.01549`, HyperWorld `2609.00002`, IMPACT `2609.00161`, Streaming4D `2609.00610` (09-02 digests); Test-time RL in imperfect-information games `2608.30635`, Motus2 `2608.30237` (09-01 arxiv-daily); Beyond Search-Imitation chess `2608.27757`, Refundable Deposits `2608.27536`, dialogue-game agents `2608.27672` / `2608.28458` (08-31 digests).

---

## 1. Game RL — Reinforcement Learning in Games

### 1.1 Constant Individual Regret in General Games

- **Authors**: Mingyang Liu, Gabriele Farina, Asuman Ozdaglar
- **Affiliation**: MIT
- **Venue**: arXiv preprint (2026-08)
- **arXiv**: [2608.31166](https://arxiv.org/abs/2608.31166)
- **Abstract & Key Innovations**: Proves the first **horizon-independent (constant) individual regret** guarantee for every finite N-player normal-form game under full-information feedback, removing the prior polylog(H) dependence. Introduces **ECHO-OFTRL** — optimistic follow-the-regularized-leader (OFTRL) plus an **EMA cascade for high-order optimism**, deterministic and fully uncoupled. Simultaneous guarantees: each player's cumulative regret bounded by a function of the largest action-set size only, plus a fast (polylogarithmic-rate) early phase to constant regret. Directly relevant to self-play / no-regret learning in game AIs.

### 1.2 Independent Reinforcement Learning in Discounted Markov Games

- **Authors**: Asrin Efe Yorulmaz, Uğur Aydın, Tamer Başar
- **Affiliation**: UIUC (Coordinated Science Laboratory)
- **Venue**: arXiv preprint (2026-09)
- **arXiv**: [2609.00504](https://arxiv.org/abs/2609.00504)
- **Abstract & Key Innovations**: Studies **radically uncoupled** (each agent sees only its own action/state) learning in discounted general-sum Markov games. Assuming ETH for PPAD, proves there is **no polynomial-time algorithm** computing inverse-polynomially accurate coarse correlated equilibria for every fixed discount factor. Complementarily gives what appears to be the **first radically uncoupled algorithm with sub-exponential convergence** to coarse correlated equilibria in discounted general-sum Markov games — a concrete boundary for decentralized RL play.

### 1.3 Differential Games for Compositional Handling of Competing Control Tasks

- **Authors**: Joshua Shay Kricheli
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-09)
- **arXiv**: [2609.01838](https://arxiv.org/abs/2609.01838)
- **Abstract & Key Innovations**: Divide-and-conquer control design for **single-agent, multi-objective dynamical systems** recast as a **non-cooperative differential game**. Each control objective gets a virtual input and a virtual player optimizing its own cost against the others' optimal policies; a **Nash equilibrium** of the auxiliary game yields a compositional controller. Offers a principled way to handle competing objectives (e.g., game agents trading attack vs. defense vs. movement) without manual reward shaping.

### 1.4 Horizon-Independent Contraction for Continuous-Time Discounted Regularized Mean-Field Games

- **Authors**: Junji Yan, Uğur Aydın, Tamer Başar
- **Affiliation**: UIUC
- **Venue**: arXiv preprint (2026-08)
- **arXiv**: [2608.27723](https://arxiv.org/abs/2608.27723)
- **Abstract & Key Innovations**: Contraction analysis of non-stationary continuous-time mean-field games (MFGs) under discounting + entropy regularization, over finite controlled CTMCs. Shows that under a **sufficiently large discount rate, finite-horizon MFGs admit a horizon-independent contraction condition** coinciding with the infinite-horizon non-stationary case; derives explicit convergence-rate constants. Relevant to population-based / open-ended RL where many agents share an aggregate environment.

### 1.5 Is Monte Carlo Tree Search Just Every-Visit Monte Carlo Control?

- **Authors**: Xianyi Wu
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-08)
- **arXiv**: [2608.27985](https://arxiv.org/abs/2608.27985)
- **Abstract & Key Innovations**: Position-style note arguing that at the level of **trajectory generation and action-value updating, MCTS and every-visit Monte Carlo control are "largely terminological"** rather than methodologically distinct: the tree policy is the learned part of a policy and the rollout policy the not-yet-learned part, unified in an on-policy/an-off-policy view. Provides a clarification useful for reasoning about why game-tree search and RL value-learning converge in practice.

### 1.6 The Role of Network Topology and Opponent Information in Shaping Cooperation in MARL Systems

- **Authors**: Seongho Son, Stephen Hailes, Mirco Musolesi
- **Affiliation**: University College London (UCL)
- **Venue**: arXiv preprint (2026-08)
- **arXiv**: [2608.28977](https://arxiv.org/abs/2608.28977)
- **Abstract & Key Innovations**: Empirically studies how **graph topology** and the information available about opponents shape emergent cooperation when agents **learn Iterated Prisoner's Dilemma (IPD) via deep RL** (as opposed to the classic strategy-imitation literature). Each agent is a graph node playing neighbours; the paper measures how cooperation depends on the topology (e.g., density, mixing) and how much an agent observes of its opponents. A practical survey for designing cooperative multi-agent game bots.

---

## 2. Game AI Bot — LLM-Powered Game Agents

### 2.1 MineCEraft: Evaluating Language Models as Construction Engineers in the World of Minecraft

- **Authors**: Sewoong Lee, Risham Sidhu, Julia Hockenmaier, Yoonhwa Jung
- **Affiliation**: University of Illinois Urbana-Champaign (UIUC)
- **Venue**: **EMNLP 2026 Findings**
- **arXiv**: [2608.28884](https://arxiv.org/abs/2608.28884)
- **Abstract & Key Innovations**: Open-source **Minecraft Construction Engineering Benchmark** with **723 domain-expert hand-crafted natural-language instructions** over **17 task categories**, all **programmatically verifiable** — a safe, controllable testbed for LLM construction engineering. Uses programmatic verification rather than LLM-judges to objectively measure task success; positioned for studying spatial reasoning, instruction following, and long-horizon block manipulation in an open world.

### 2.2 HoopMind: A Real-Time Neural Game-Tree System for Opponent-Aware Possession Planning

- **Authors**: Yibo Gong, Cong Guo, Jiacheng Ding
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-08)
- **arXiv**: [2608.29563](https://arxiv.org/abs/2608.29563)
- **Abstract & Key Innovations**: Sports-analytics/NPC-style **real-time game-tree system for basketball possession planning** built on publicly available data: fuses **five public sources** into a **4.23M-shot / 21-season** dataset (shot locations, two play-by-play feeds, matchup tracking, player biometrics) with 99.5–100% alignment, and flags two easy-to-miss data pitfalls. Models a half-court possession as a tree search with **opponent-aware planning**, aiming to democratize analytics that pro teams keep private (school-coach use case).

### 2.3 ChessQueries: Toward Better Chess Board Recognition

- **Authors**: Joël Seytre
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-08)
- **arXiv**: [2608.30762](https://arxiv.org/abs/2608.30762)
- **Abstract & Key Innovations**: Chess board recognition (mapping a board image to piece-on-square) improved via a **ViT encoder + DETR-style decoder** architecture. On the established **ChessReD** benchmark, improves SOTA from **15.3% to 99.2%** accuracy and shows strong out-of-distribution robustness, saturating the two existing benchmarks. An enabling perception module for chess-playing bots / LLM chess agents operating on images instead of FEN.

### 2.4 JSON-Bag VF: Game-Agnostic Value Functions through Automatic JSON Feature Extraction

- **Authors**: Dien Nguyen, Diego Perez-Liebana
- **Affiliation**: Queen Mary University of London (QMUL)
- **Venue**: arXiv preprint (2026-08)
- **arXiv**: [2608.30056](https://arxiv.org/abs/2608.30056)
- **Abstract & Key Innovations**: Trains **game-agnostic value functions** on game trajectories tokenized as **JSON Bag-of-Tokens (JSON-Bag)** prototypes, extended with **Random-Forest-based feature selection** plus a game-stage-specific feature selector. Combined with **One-Step-Look-Ahead (JSON-Bag OSLA)**, evaluated on **six tabletop games**; the generic JSON pipeline transfers across games without hand-designed state features — a step toward reusable value/policy components for game bots.

---

## 3. Game Foundation Models & World Models

### 3.1 The Intervention Gap in Latent World Models

- **Authors**: Donna Vakalis
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-08)
- **arXiv**: [2608.29998](https://arxiv.org/abs/2608.29998)
- **Abstract & Key Innovations**: Identifies **planning-time intervention fidelity** as a distinct, measurable property of world models: whether the model's *own* open-loop transitions move task variables the way **matched environment interventions** do. Across released TD-MPC2 checkpoints, episode return drops as an operator-error diagnostic on task observables grows while reward-prediction error stays small ~ flat — i.e., **reward fit does not reveal intervention fidelity**. Argues for diagnostics beyond generative/task-loss success.

### 3.2 Semantic Bayesian World Models

- **Authors**: Tommaso Soru
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-09)
- **arXiv**: [2609.03834](https://arxiv.org/abs/2609.03834)
- **Abstract & Key Innovations**: Vision for **Semantic Bayesian World Models (SBWMs)**: Web knowledge represented as a *shared evolving fabric of beliefs over knowledge graphs* rather than crisp facts, where ontological axioms constrain priors and observations update beliefs via **Bayesian inference**. Positions KG + foundation-model integration as a unified reasoning architecture (world model with uncertainty), which is directly relevant to game-world and NPC knowledge grounding. *(tentative)*

### 3.3 How do World Models and Policies Compose in LLM Agents? A Joint Spectral and Behavioral Account

- **Authors**: Ruize Xu, Xiao Yu, Yujin Tang, Chenming Shang, Nikhil Singh
- **Affiliation**: *(inferred — MIT-affiliated)*
- **Venue**: arXiv preprint (2026-08)
- **arXiv**: [2608.30067](https://arxiv.org/abs/2608.30067)
- **Abstract & Key Innovations**: Controlled experiments combining **world-model training (next-state prediction)** and **policy training (reward maximization)** in LLM agents, dissected via **additive parameter updates**. Finds effective world-model updates are **low-rank and share an input-feature subspace with policy updates** while writing to nearly orthogonal output directions (train separately or sequentially); however in projection, composition can interfere. Informs how game agents should jointly learn simulator and policy.

### 3.4 CAER: Causal Action Effect Reweighting for World Model Training

- **Authors**: Jianjie Fang, Xvyuan Liu, Ziyou Wang, Rongze Tang, Zhaolu Wang, Zhuohang Li, Xin Zhang, Haisheng Su, Chen Gao, Wei Wu, Xinlei Chen, Yong Li
- **Affiliation**: *(inferred — Tsinghua et al.)*
- **Venue**: arXiv preprint (2026-08)
- **arXiv**: [2608.30897](https://arxiv.org/abs/2608.30897)
- **Abstract & Key Innovations**: World models trained with space-time-uniform MSE let **abundant background tokens dominate the gradient** while sparse interaction dynamics stay under-optimized — the model learns appearance, not how *actions* change the world. **Causal Action Effect Reweighting (CAER)** downweights causal-null tokens and upweights action-affected regions, a general and cheap training paradigm for action-conditioned video world models (game/embodied simulators).

### 3.5 Rethinking World Models for Safety-Critical Embodied Systems

- **Authors**: Kailang Ma, Heye Huang, Inhi Kim, Kitae Jang
- **Affiliation**: *(inferred — University of Melbourne / KAIST)*
- **Venue**: arXiv preprint (2026-09)
- **arXiv**: [2609.03774](https://arxiv.org/abs/2609.03774)
- **Abstract & Key Innovations**: Perspective identifying **three structural mismatches** in current world modeling for safety-critical (embodied) systems: **likelihood vs risk**, **prediction vs intervention**, and **finite-horizon prediction vs accumulated consequences**. Proposes a **Risk-Informed World Model (RIWM)** as a decision-centric research direction — highly relevant as game and autopilot world models move toward deployment where visual fidelity ≠ decision evidence.

---

## 4. Procedural Content Generation

### 4.1 Learning Feasibility-Aware Latent Spaces for Preference-Based Exploration of Procedural Automotive Wheel Designs

- **Authors**: Takashi Owaki, Yuki Koyama, Tomoyasu Nakano, Takahiro Yamaguchi, Masataka Goto, Hiroyuki Sakai
- **Affiliation**: *(inferred — AIST Japan et al.)*
- **Venue**: arXiv preprint (2026-09)
- **arXiv**: [2609.00527](https://arxiv.org/abs/2609.00527)
- **Abstract & Key Innovations**: Interaction-oriented representation learning for **procedural content generation**: screens procedurally generated samples by **geometric rule checks**, learns a **feasibility-aware latent space**, and interacts via human preference-based optimization so suggestions are meaningful *and* valid. Evaluated on automotive wheel design — a nice industrial PCG + human-in-the-loop (preference RL-adjacent) case study which transfers to game-asset generation.

---

## 5. Game & World-Model Benchmarks

### 5.1 CivBench: A Long-Horizon Benchmark for Tool-Mediated Agents in Civilization VI

- **Authors**: Austin Tudor David Andrews, Liam Wilkinson, Jamie Heagerty, Harry Coppock, Jakob Nicolaus Foerster, Rui Ponte Costa
- **Affiliation**: University of Oxford / Newcastle University / University of Bristol
- **Venue**: arXiv preprint (2026-09)
- **arXiv**: [2609.02459](https://arxiv.org/abs/2609.02459)
- **Abstract & Key Innovations**: Open-source benchmark evaluating **language-model agents in long-horizon, tool-mediated game environments via the Model Context Protocol (MCP)**. A single episode spans **300+ turns and thousands of tool calls** over a large action space — sustained planning, state monitoring, and execution under partial observability. Exposes **76 MCP tools** plus a narration layer converting visual game state to structured text. Pilot-characterizes agent behaviour across **4 model families / 23 admissible runs** — the first Civ-class benchmark for LLM game agents.

### 5.2 Can Video World Models Track Unobserved World States?

- **Authors**: Joonghyuk Shin, Yicong Hong, Jaesik Park, Xun Huang
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-08)
- **arXiv**: [2608.30692](https://arxiv.org/abs/2608.30692)
- **Abstract & Key Innovations**: Benchmark probing whether video world models actually maintain **hidden world state** beyond visual fidelity: an action-conditioned **video "Shell Game"** — a visual analog of S₅ state tracking that decouples rendering from compositing hidden state. Bidirectional/autoregressive Transformers, Mamba, and nonnegative-eigenvalue linear attention fit the training horizon (5 swaps) but **fall toward chance on longer swap chains (extrapolation) while still rendering plausibly** — a clean diagnostic for "visually fluent but state-blind" simulators.

### 5.3 Do Video Generators Track the World Across Segments? A Benchmark and Method for World-State Reasoning in Video Continuation

- **Authors**: Yingmao Miao, Pengfei Zhang, Chaoran Xu, Meng Yu, Jing Tang, Xiangxiang Chu, Chao Shen, Chenhao Lin
- **Affiliation**: *(inferred — Xi'an Jiaotong University et al.)*
- **Venue**: arXiv preprint (2026-09)
- **arXiv**: [2609.03673](https://arxiv.org/abs/2609.03673)
- **Abstract & Key Innovations**: Long videos are built by composing segments, and generators rely on memory (recent frames, key frames, memory banks, cached features), but current generators **do not reliably convert past evidence into a world-state interface**: a past frame remains valid history yet may no longer hold in the current world state. Provides a **benchmark for world-state reasoning in video continuation** plus a method to enforce cross-segment state consistency.

### 5.4 SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models

- **Authors**: Junchao Huang, Guian Fang, Shengju Qian, Xianghao Kong, Zhuoran Zhao, Wei Huang, Yihua Du, Zixin Zhang, Justin Cui, Yuchao Gu, Yukang Chen, Xinting Hu, Tianyu He, Shaoshuai Shi, Zhuotao Tian, Xin Wang, Mike Zheng Shou, Li Jiang
- **Affiliation**: *(inferred — NUS / HKU et al.)*
- **Venue**: arXiv preprint (2026-09)
- **arXiv**: [2609.02886](https://arxiv.org/abs/2609.02886)
- **Abstract & Key Innovations**: Fully open foundation for building **interactive video world models** from data preparation through long-horizon inference, solving the **naive data-mixing trap**: heterogeneous sources (temporal scale, camera geometry, visual quality, motion, captioning style) and model-specific backbones yield inconsistent supervision. SolarWM provides a reconfigurable pipeline (open data recipe + scalable training + inference), a reproducibility-first answer to the fragmentation of long-horizon interactive world-model research.

### 5.5 VeriPhy: Agentic Physical Reasoning for World Model Evaluation and Refinement

- **Authors**: Wenzhuo Xu, Yuchen Zhu, Chongjian Ge, Xuan Shen, Jing Shi, Jason Kuen, Yongxin Chen, Molei Tao, Christopher McComb, Noelia Grande Gutiérrez, Jiuxiang Gu
- **Affiliation**: *(inferred — Apple et al.)*
- **Venue**: arXiv preprint (2026-09)
- **arXiv**: [2609.03153](https://arxiv.org/abs/2609.03153)
- **Abstract & Key Innovations**: Visual fluency ≠ physical reliability, and a scalar quality score cannot say *which* obligation a video violates or *when*. **VeriPhy** is an auditable physical-verification system: a **text-only planner compiles the prompt into typed physical obligations and a statically validated execution plan before any frame**, then observations gate/scope calls to frozen low-level experts (segmentation, tracking, counting, eleven typed physical measurements). Provides auditable world-model evaluation + a signal for refinement.

---

## 6. Industry Game AI

### 6.1 Matrix-Game 3.5: Enhancing Real-Time Streaming Interactive World Models with Patch Memory

- **Authors**: Runjia Qian, Zile Wang, Jihai Zhang, Kai Zou, Wei Yu, Jiaxing Li, Zexiang Liu, Yaokun Li, Fei Kang, Kaichen Huang, Mengyin An, Haobo Zhang, Biao Jiang, Jiahua Wang, Haofeng Sun, Yang Liu, Yangguang Li
- **Affiliation**: *(inferred — Alibaba Tongyi et al., same team as Matrix-Game 3.0)*
- **Venue**: arXiv preprint (2026-08)
- **arXiv**: [2608.29910](https://arxiv.org/abs/2608.29910)
- **Abstract & Key Innovations**: Successor to Matrix-Game 3.0 targeted at real-time interactive world generation for games/robotics/XR. The persistent interactive-simulation challenge is to simultaneously keep **scene geometry, dynamic consistency, and camera control** stable while generating autoregressively in real time. **Patch Memory** extends the streaming world model to better preserve geometry and dynamic consistency across long-horizon interaction — building toward persistent, playable generative worlds.

### 6.2 Building Pretraining Data for World Models: An Unreal Engine-Based Pipeline for Action-Conditioned Video Generation

- **Authors**: Haoyu Wang, Songchun Zhang, Haoran Li, Haoyang Huang, Zeyue Xue, Nan Duan
- **Affiliation**: *(inferred — Tsinghua / Visual Agent et al.)*
- **Venue**: arXiv preprint (2026-09)
- **arXiv**: [2609.03557](https://arxiv.org/abs/2609.03557)
- **Abstract & Key Innovations**: Action-conditioned video models need visual data **temporally aligned with control signals** — which ordinary real-world video cannot provide. Describes a **large-scale synthetic data production pipeline built on Unreal Engine** that generates action-conditioned, multi-view video, reconciling real-time physics with high-quality offline rendering via separated trajectory-generation and rendering stages. A practical industrial-scale answer to the "where do you get aligned action→video pairs?" bottleneck for game world models.

---

## 7. Related Techniques

### 7.1 What Emerges and What Breaks in Self-Play Driving

- **Authors**: Laur Sisask, Ardi Tampuu, Tambet Matiisen
- **Affiliation**: University of Tartu
- **Venue**: arXiv preprint (2026-08)
- **arXiv**: [2608.30819](https://arxiv.org/abs/2608.30819)
- **Abstract & Key Innovations**: Follow-up to Gigaflow / Puffer-Drive: trains driving policies via **pure self-play**, scaling from MLPs to **Transformers**, on the HD map of a real city targeted for deployment. On CARLA and Waymax the policies fall short of Gigaflow, traced to concrete failure modes — **reward hacking at traffic lights and a missing incentive to stop at stop signs** — plus an analysis of which traffic rules *emerge* vs *break* under self-play. An honest, diagnostic take on self-play RL in a complex game-like simulation.

### 7.2 Uncertainty-Driven Replay Memory for Reinforcement Learning

- **Authors**: Sheeraja Rajakrishnan, Alexander G. Ororbia, Travis Desell, Daniel E. Krutz
- **Affiliation**: Rochester Institute of Technology (RIT)
- **Venue**: arXiv preprint (2026-08)
- **arXiv**: [2608.29860](https://arxiv.org/abs/2608.29860)
- **Abstract & Key Innovations**: Reformulates the **experience replay buffer** around uncertainty: **UDRM (Uncertainty-Driven Replay Memory)** upweights/channels experiences according to whether actions explore **unknown vs well-known** regions, reducing training time and improving total reward. Buffer-level uncertainty as a cheap intrinsic signal is directly applicable to game RL (Atari-style) training pipelines.

### 7.3 AI Alignment through a Game-theoretic Lens: A Survey

- **Authors**: Yanan Cai, Zhongrui Zhao, Zhigang Lu, Ickjai Lee, Wei Emma Zhang, Minhui Xue, Yihong Zhang, Shuchao Pang, Wei Xiang
- **Affiliation**: *(inferred — Australian universities: JCU / UniSA et al.)*
- **Venue**: arXiv preprint (2026-08)
- **arXiv**: [2608.27910](https://arxiv.org/abs/2608.27910)
- **Abstract & Key Innovations**: Surveys **AI alignment via game theory**, organizing recent progress around game-theoretic elements (players, strategies, equilibria, mechanism) and synthesizing the literature on context-dependent, non-transitive, multi-party preferences that standard alignment (helpfulness/harmlessness/controllability) struggles to capture. Connects the game-RL/multi-agent literature to alignment, complementing wiki coverage of game-theoretic LLM research. *(tentative)*

---

## Cross-Cutting Trends

1. **Game RL theory advances on regret & decentralization**: New constant-regret guarantees in general games (ECHO-OFTRL, MIT), PPAD-hardness boundaries + first sub-exponential radically-uncoupled rates in discounted Markov games (UIUC), and horizon-independent contraction for regularized MFGs together sharpen what decentralized self-play can provably achieve.

2. **World-model honesty becomes a first-class evaluation axis**: `The Intervention Gap`, the `video Shell Game`, `VeriPhy`, and the cross-segment world-state benchmark all converge on the same finding — **visual fidelity carries no guarantee of intervention/state fidelity** — echoing the "Context Collapse" thread from prior digests (ActSWM `2607.26712`).

3. **Game benchmarks for LLM agents graduate to tool-mediated long-horizon play**: CivBench (300+ turns / 76 MCP tools via MCP) and MineCEraft (723 verifiable construction instructions, EMNLP 2026 Findings) push beyond single-frame/task evaluation toward sustained planning under partial observability.

4. **Real-time interactive world models & synthetic data pipelines mature**: Matrix-Game 3.5 (patch memory) and the Unreal Engine action-conditioned data pipeline address the two production bottlenecks — long-horizon stability and aligned action→video supervision — for generative game engines.

5. **Self-play & multi-agent empirical study matures beyond toy domains**: from IPD cooperation under network topology (UCL) to self-play driving with documented rule-hacking failure modes (U Tartu), the community is now studying *why* self-play produces good/bad emergent behaviour, not just win rates.