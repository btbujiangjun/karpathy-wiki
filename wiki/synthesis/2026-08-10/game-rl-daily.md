---
title: "Game RL & Game AI Bot — Daily Synthesis (2026-08-10)"
type: synthesis
created: 2026-08-10
updated: 2026-08-10
tags: [game-rl, game-ai, game-foundation-models, pcg, game-benchmarks, self-play, world-models, multi-agent-rl, llm-agents]
sources: []
---

# Game RL & Game AI Bot — Daily Synthesis (2026-08-10)

> Curated papers on Game RL, Game AI Bots, Game Foundation Models, PCG, Benchmarks, Industry Game AI, and related techniques. Fresh window = the Mon Aug 10, 2026 arXiv announcement batch (submitted Aug 7–9, IDs ~2608.06394–2608.07457). Every paper below was **grep-verified absent** from all prior wiki digests (07-01 → 08-08 game-rl-daily, arxiv-daily/arxiv-ai-search/arxiv-paper-check through 08-10) before inclusion. 13 new papers listed in full across 5 of 7 categories; two categories (PCG, Industry) had no new submissions and are cross-referenced to recent coverage.

---

## 1. Game RL — Reinforcement Learning in Games

### Solver-Guided Reasoning for Mixed-Equilibrium Strategies (MDT)
- **Authors**: Han Wang, Philippe Beardsell, Boning Li, Aaron Sasmita, Shuai Li, Hongyuan Zha, Baoxiang Wang
- **Affiliation**: CUHK-Shenzhen / AIRS (tentative, inferred from co-authors)
- **Venue**: arXiv:2608.06741 (Aug 7, 2026)
- **Key Innovation**: Questions the default of grounding LLM reasoning in human data for game play, arguing human demonstrations are biased toward pure strategies in mixed-equilibrium games. Proposes **Mixed-Strategy Decision Tree (MDT)**, which distills solver output — not human annotations — into sparse, interpretable strategic rules for LLMs. Instantiates on No-Limit Texas Hold'em by querying a solver oracle for **>250 million mixed-strategy decisions**; MDT + contrastive shadow techniques reduce the **ℓ₁ distance to equilibrium by 52.6%** across 8 LLM configurations. Route-only ablations isolate the shadow-based contrast contribution; River-endgame and Liar's Dice experiments test strategic fidelity and portability beyond Hold'em. Relevant to LLM-based game agents that need equilibrium play rather than human-style heuristics.
- **Link**: https://arxiv.org/abs/2608.06741

### Aftab: A Comprehensive Benchmark of CNN Encoders and Advanced Value Functions in Parallelized Q-Networks
- **Authors**: Taha Shieenavaz, Shabnam Zareshahraki, Loris Nanni
- **Affiliation**: University of Padova (tentative, inferred from co-author)
- **Venue**: arXiv:2608.07335 (Aug 7, 2026)
- **Key Innovation**: Systematically explores the visual-encoder design space for the **Parallelized Q-Network (PQN)** paradigm (off-policy learning without replay buffers or target networks). Designs and evaluates **8 CNN topologies** under strict parameter constraints, then integrates the **Hadamax encoding** and advanced Q-learning heads (distributional, ensemble, dueling). On **Atari-57** the composite **Aftab** architecture achieves an **IQM Human-Normalized Score of 6.479** with a 0.86 Probability of Improvement over the PQN baseline; on the non-stationary **Procgen Hard** benchmark it shows out-of-distribution generalization (IQM Procgen score 0.418 vs 0.382). Fully open-sourced (GitHub: tahashieenavaz/aftab). A structural benchmark for memory-efficient, unbuffered RL on classic game environments.
- **Link**: https://arxiv.org/abs/2608.07335

### Algorithmic Threshold Optimization: Quantitative Modeling of Multiplier Distributions in Crash Games
- **Authors**: Sourish Sarkar
- **Affiliation**: —
- **Venue**: arXiv:2608.07103 (Aug 7, 2026)
- **Key Innovation**: Applies algorithmic optimization to **Crash**, a multiplayer casino game blending strategic betting, probability, and computational analysis. Derives an algorithm to choose an **optimal stopping multiplier** that simultaneously minimizes the casino's guaranteed positive earnings while maximizing the number of players who win something in a round — explicitly balancing house and player interests. The algorithm is invariant to player count and bet-size distribution; includes complexity analysis and stopping-multiplier statistics. A formal house-vs-players modeling case for adversarial/economic game settings and a cautionary example of game-theoretic reward optimization (relevant for RL reward design and game fairness auditing).
- **Link**: https://arxiv.org/abs/2608.07103

---

## 2. Game AI Bot — LLM-Powered Game Agents & NPC Intelligence

### Deal Me Maybe: The Role of Emotions in Multi-Agent Negotiation
- **Authors**: Massimiliano Luca, Apoorva Singh, Bruno Lepri
- **Affiliation**: Fondazione Bruno Kessler (FBK, tentative)
- **Venue**: arXiv:2608.06922 (Aug 7, 2026)
- **Key Innovation**: A controlled study of how **prompt-conditioned emotions** shape LLM-based price negotiation between buyer and seller agents over **350 real consumer products**, 2 budget conditions, 36 emotion-pair settings, across 5 widely used LLMs. Finds emotions strongly gate outcomes: **angry buyers almost never reach agreement (0.39% deal rate)** while happy buyers agree most often (28.91%) but get worse prices than fearful buyers. Effects are role-dependent — buyer emotion drives acceptance/rejection while seller emotion shapes concession dynamics — and extend beyond language to termination behavior and price trajectories. Directly relevant to emotion-conditioned NPCs, social-deduction/negotiation game agents, and commerce-oriented game AI (complements the Werewolf EDA study in [[2026-08-08/game-rl-daily]]).
- **Link**: https://arxiv.org/abs/2608.06922

### PHASE-Tree: Modeling Character-State Evolution in Long-Horizon Role-Playing Dialogue
- **Authors**: Bo Tang, Jianan Yang, Junyi Zhu, Yiquan Wu, Rui Zhao, Zhengyu Yang, Yang Zhang, Feiyu Xiong, Zhiyu Li, Jiajun Shen
- **Affiliation**: Tsinghua (tentative, inferred from co-authors)
- **Venue**: arXiv:2608.06975 (Aug 7, 2026)
- **Key Innovation**: Targets the gap between static persona profiles and characters that must **evolve recognizably** across long-horizon role-play. **PHASE-Tree** is a multi-timescale character-state tree with an immutable identity root and mutable persona/session/moment layers, making every mutable field an addressable target for localized within- and cross-episode updates; generation is conditioned via explicit textual provision or implicit parametric adaptation. Introduces **LongEvoRoleBench** (4 long-dialogue corpora for cross-episode evolution + 4 short-dialogue corpora for within-scene state tracking) under a unified next-utterance protocol. Textual PHASE-Tree ranks first in 11/12 dataset-metric cells vs internal variants and all 12 vs external baselines, improving character-level/semantic/embedding scores by 19.7%/12.4%/15.1%. A backbone for persistent, evolving NPCs in narrative games.
- **Link**: https://arxiv.org/abs/2608.06975

---

## 3. Game Foundation Models — Generalist Game Agents & World Models

### MemWM: Memory-Augmented Text-Based World Model
- **Authors**: Yujun Wang, Tao Zhang, Jinhe Bi, Aniri, Wenxuan Ye, Boliang Liu, Sikuan Yan, Shuning Wang, Xuebing Zhou, Sören Pirk, Hinrich Schütze, Yunpu Ma
- **Affiliation**: LMU Munich (tentative, inferred from co-authors)
- **Venue**: arXiv:2608.07107 (Aug 7, 2026)
- **Key Innovation**: Diagnoses that fluent next-state predictions from text-based world models still **omit task-critical facts, corrupt attributes, or apply wrong transition rules**. **MemWM** augments the world model with *world memory* — a curated memory bank of transition rules, state caches, and hard-to-predict facts — used to condition next-state imagination. Evaluates factual state preservation with a new **Structured State Fidelity (SSF)** metric: memory-augmented training improves SSF by up to **206.3%** over SFT. In full planning, the policy model stays frozen and receives policy-side *world skill* (retrieved task-level skills + step-wise corrective guidance); across **ALFWorld, WebShop, ScienceWorld** the memory-augmented agent beats an SFT-trained world-model agent by up to **65.4%** relative. Advances world models for interactive/text-based game environments.
- **Link**: https://arxiv.org/abs/2608.07107

### Dueling World Models: Advantage-Style Action Channels for Common-Mode Distractor Rejection
- **Authors**: Jiazhuo Li, Yiming Fei, Zhiruo Zhou, Heikichi Hayashi
- **Affiliation**: —
- **Venue**: arXiv:2608.06706 (Aug 7, 2026)
- **Key Innovation**: Identifies an "action-blindness" failure in latent world models: when scenes contain motion the agent does not control, action-conditioned predictions become indistinguishable even as training loss improves. Proposes a minimal fix borrowed from dueling decomposition — **subtract the prediction's mean effect over actions** to cancel action-independent variation (where distractors live), yielding a clean controllable channel with no reward, no reconstruction, and no distractor-specific loss. The readout-time subtraction applies unchanged to any action-conditioned world model, including frozen pretrained ones; proven exact in finite samples. On gridworld, synthetic generators, distracting continuous control, and **natural-pixel Atari**, the isolated channel recovers the agent's own effect where entangled predictors fail; applied post hoc it surfaces action channels in off-the-shelf models. Directly relevant to robust world-model-based game agents under environmental distractors.
- **Link**: https://arxiv.org/abs/2608.06706

### WorldTrace: Addressable Memory for Video World Models
- **Authors**: Xindi Wu, Sven Elflein, James Lucas, Olga Russakovsky, Laura Leal-Taixé, Despoina Paschalidou, Jonathan Lorraine, Aljoša Ošep
- **Affiliation**: NVIDIA Research (SIL) + Princeton + TU Munich + others
- **Venue**: arXiv:2608.07408 (Aug 7, 2026)
- **Key Innovation**: Studies **visual persistence** in interactive video world models. Finds KV-cache memory becomes unaddressable beyond the training horizon because temporal RoPE offsets fall out-of-distribution, and naive cache compression in RoPE-rotated space corrupts memory by averaging incompatible positional phases. **WorldTrace** is a training-free memory framework: compressed summary slots get distinct in-distribution virtual positions, with two strategies — **WorldTrace-Field** (temporal coherence) and **WorldTrace-Landmark** (verbatim scene traces at detected transitions for episodic recall). Introduces **LoopBench**, a benchmark for reconstructing a previously visited scene after a long detour: Field improves temporal consistency **+15.5%**, Landmark improves episodic recall **+19.5%**. Extends the video/visual world-model line (cf. γ-World in [[2026-08-10/conference-digest]], MASS in [[2026-08-08/game-rl-daily]]) toward long-horizon game-environment persistence.
- **Link**: https://arxiv.org/abs/2608.07408

---

## 4. Procedural Content Generation (PCG)

> **No new PCG papers this cycle.** Recent coverage: Tencent Hunyuan's WorldClaw agentic 3D open-world generation (2608.05248, [[2026-08-08/game-rl-daily]]); the PCG+LLM line (PCGRLLM, IPCGRL, MIPCGRL, WCRL, Multiverse) via [[2026-08-02/game-rl-daily]] and [[2026-07-30/game-rl-daily]].

---

## 5. Game Benchmarks

### Cross-references (fresh window, already covered — not re-listed)
- **LoopBench** (new benchmark for video world-model scene persistence) is introduced by WorldTrace (2608.07408, Section 3 above).
- **Transformers Struggle to Use Their Emergent World Models: Revisiting the Tower of Hanoi** (2608.07077) — small Transformers develop a geometrically faithful Sierpinski-triangle world model yet frontier reasoning models fail above 3 rings; the failure is representation maintenance during planning, not absence — covered in today's [[2026-08-10/arxiv-paper-check]] (game-like reasoning benchmark).
- Earlier benchmark anchors: DungeonBench (2607.29577) and MirrorCraft (2607.29218) are cross-referenced in [[2026-08-03/arxiv-ai-search]] and [[2026-08-04/game-rl-daily]]; OmniGameArena, GameWorld, BALROG, ACT-Eval, AI World Cup 2026 in prior dailies.

---

## 6. Industry Game AI

> **No new industry submissions this cycle** (the Mon Aug 10 batch has no studio-authored game-AI paper). The most relevant industry item in the batch is **NVIDIA's WorldTrace** (Section 3). NVIDIA + Tsinghua + U Toronto + Vector's **γ-World generative multi-agent world model** (Simplex Rotary Agent Encoding, 24 FPS, zero-shot 2→4 player) is already covered in [[2026-08-10/conference-digest]]. Ongoing tracked threads: KRAFTON PUBG ALLIE ([[2026-07-17/game-rl-daily]]), NVIDIA ACE/NVIGI ([[2026-07-13/game-rl-daily]]), EA SPORTS NHL 26 (2607.07498, [[2026-08-01/game-rl-daily]]).

---

## 7. Related Techniques — Self-Play, World Models, Multi-Agent RL

### Trajectory-Relative Hindsight Distillation for Agentic Reinforcement Learning (TRIAL)
- **Authors**: Haoyu Zheng, Yun Zhu, Qing Wang, Wenqiao Zhang
- **Affiliation**: —
- **Venue**: arXiv:2608.07371 (Aug 7, 2026)
- **Key Innovation**: Addresses the open problem of **allocating dense hindsight signals across decision turns** in agentic RL. **TRIAL** introduces a unified turn-aligned scoring protocol: for each turn it extracts the outcome view of that decision's realized consequence, evaluates the same response under ordinary vs hindsight-conditioned contexts, and uses the **signed log-probability gap** to set direction and local strength of token-level supervision, while turn-level magnitudes are normalized jointly over the trajectory (eligible-token-weighted mean of one). On **WebShop and ALFWorld**, TRIAL outperforms GRPO across all 8 backbone/environment/metric combinations and is best/tied-best among 6 methods on 6 of them (e.g., WebShop + Qwen3-1.7B: success 56.4%→75.2%, task score 78.7%→85.7%). Relevant to dense-credit agentic RL for game agents and interactive environments.
- **Link**: https://arxiv.org/abs/2608.07371

### Why Study Emergent Behavior When You Can Regulate It? Aligning Multi-Agent Systems with Reward Prediction (MARP)
- **Authors**: Assaf Caftory, Almog Zemach, Moshe Butman, Doron Friedman
- **Affiliation**: Reichman University (tentative, inferred from co-author)
- **Venue**: arXiv:2608.07280 (Aug 7, 2026)
- **Key Innovation**: Moves beyond analyzing emergent multi-agent dynamics to **actively shaping them via learned social reward models**. **MARP (Multi-Agent Reward Prediction)** extends preference-based reward modeling to MARL: a shared reward model is learned from episode-level evaluations of collective outcomes, letting decentralized agents align with global social objectives without handcrafted rewards. Validated in the **Harvest Game**, a canonical sequential social dilemma: MARP aligns behavior more closely with target social metrics than reward-based baselines, captures subtle environment structure, and supports composite objectives (sustainability, equality, peace) within one training regime by only changing the high-level evaluation metric. Relevant to cooperative-game AI, NPC governance, and reward-design for multi-agent games.
- **Link**: https://arxiv.org/abs/2608.07280

### Learning Suffers More Than the Policy Class Under Partial Observability: A Closed-Form Analysis
- **Authors**: Idil Gözel
- **Affiliation**: University College London
- **Venue**: arXiv:2608.07228 (Aug 7, 2026)
- **Key Innovation**: Theoretical result on why partially observed RL fails even when a good policy exists and the value function can express it. In a closed-form-solvable partially observed linear-quadratic problem with actor-critic learning, the representable best policy costs 10.4% more than the full-observation controller, but learning lands at a policy **35% worse than the best representable one**. The cause is a **critic bias**: unobservable-state variation is misread as sharp value-function curvature, and the actor follows that error away from the optimum. The one fix is how far the learner looks ahead before trusting its value estimates — *not* memory of past observations (which does not help). Deep RL experiments match the closed form. Foundational for imperfect-information and partially observed game RL (chess/Go-style searches, poker, real-time games).
- **Link**: https://arxiv.org/abs/2608.07228

### Analyzing the Interaction of Optimal Strategies in Mean-Payoff Bidding Games
- **Authors**: Shaull Almagor, Guy Avni, Julian Ewaied
- **Affiliation**: Technion / University of Haifa (tentative, inferred from co-authors)
- **Venue**: arXiv:2608.07383 (Aug 7, 2026)
- **Key Innovation**: Studies what actually happens when **all agents in a multi-agent system assume adversarial opponents** and play their optimal-adversary strategies — a common assumption in game-agent design that yields the strongest guarantees but does not describe the realized interaction. Analyzes **bidding games** on graphs with mean-payoff objectives, where each round an auction decides which agent moves a token. Shows that for the two known explicit optimal-strategy constructions, under restrictions, the generated play is **ultimately periodic**, and gives algorithms to compute the players' utilities. Formal footing for understanding equilibrium-on-paper vs equilibrium-in-practice in auction-style game mechanics (poker auctions, bidding-based games).
- **Link**: https://arxiv.org/abs/2608.07383

### Scalable Long-Horizon Planning with Staggered Updates for Lifelong MAPF (PUSH)
- **Authors**: Vaibhav Sanjay, Jiaoyang Li
- **Affiliation**: Carnegie Mellon University (tentative, inferred from co-author)
- **Venue**: arXiv:2608.06702 (Aug 7, 2026)
- **Key Innovation**: **PUSH** unifies the strengths of PIBT/EPIBT (rule-based, scale to thousands of agents, but temporally myopic), RHCR (multi-step horizon but heavy overhead), and TP (subset planning but restricted to structured maps). It plans RHCR-style windowed paths on **general maps** for only a subset of agents per timestep using staggered planning windows, plus EPIBT-inspired priority inheritance, backtracking, and anytime improvements. Scales to **10k agents** under a second while planning over multi-step horizons and achieves higher system throughput than all baselines in congested long-horizon scenarios. Relevant to large-scale NPC/bot pathfinding and real-time multi-agent game logistics.
- **Link**: https://arxiv.org/abs/2608.06702

---

## Summary Statistics

- **Total new papers**: 13 fully listed (verified NEW via grep against all prior wiki digests)
- **Categories with new papers**: 5 of 7 — Game RL (3), Game AI Bot (2), Game Foundation Models / World Models (3), Benchmarks (cross-refs; 1 new benchmark introduced via WorldTrace), Related Techniques (5). PCG and Industry Game AI had no new submissions.
- **Key venues**: arXiv (Aug 7, 2026 submissions, announced Aug 10)
- **Notable trends**:
  - **World models push toward persistence and controllability**: WorldTrace (addressable KV memory, LoopBench), Dueling World Models (action-channel extraction without extra losses), and MemWM (memory-bank-conditioned text world models) attack three distinct failure modes — long-horizon memory, distractor-induced action-blindness, and factual state fidelity
  - **Solver-guided equilibrium reasoning for LLM agents**: MDT shows solver output (250M+ decisions) beats human-annotated reasoning for mixed-equilibrium games, cutting ℓ₁ distance to equilibrium by 52.6% in No-Limit Hold'em
  - **Emotions as first-class agent parameters**: Deal Me Maybe quantifies how prompt-conditioned emotions radically gate negotiation outcomes (angry buyers 0.39% deal rate) — a lever and a risk for emotion-conditioned game agents
  - **Character-state evolution becomes an explicit model**: PHASE-Tree makes RPG/NPC persona state mutable and addressable across long-horizon role-play
  - **MARL alignment via learned social rewards**: MARP treats emergent behavior as a regulation target using episode-level reward prediction in the Harvest Game social dilemma
  - **Theory for game RL**: closed-form analysis shows partial-observability learning failure is a critic bias (fixable by lookahead, not memory); bidding-game analysis characterizes realized play when everyone plays adversarial-optimal

## Cross-References

- [[2026-08-08/game-rl-daily]] — prior digest (IFlowNets, SyncPlan, MASS, WorldClaw, ACT-Eval, AI World Cup, OASE, Hybrid LLM+RL, ADRS, AI Agent Economics)
- [[2026-08-10/conference-digest]] — γ-World (NVIDIA multi-agent world model), Google game-theory-for-FMs
- [[2026-08-10/arxiv-paper-check]] — Transformers' emergent world models (Tower of Hanoi), WebRider, IB-RL
