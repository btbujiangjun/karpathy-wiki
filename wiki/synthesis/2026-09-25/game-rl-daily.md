---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-09-25)"
type: synthesis
created: 2026-09-25
updated: 2026-09-25
sources: [arxiv.org]
tags: [game-rl, game-ai, llm-agents, foundation-models, world-models, pcg, benchmarks, industry-game-ai, self-play, marl, world-action-models, role-playing-agents, agent-simulation, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-09-25)

> **Methodology note**: **Fri 25 Sep 2026** mailing (processes Thu 24 Sep submissions). Fresh window = **IDs 2609.28475–2609.30264**. My pipeline page-parsed `/list/{cat}/new` (New-submissions sections only) over **10 categories — cs.AI / cs.LG / cs.GT / cs.MA / cs.NE / cs.CV / cs.CL / cs.RO / cs.HC / cs.LO** via `https://arxiv.org` (export.arxiv.org returned empty bodies — workaround documented) → **551 unique fresh IDs parsed** (cs.AI 107 / cs.LG 119 / cs.CV 111 / cs.RO 87 / cs.CL 86 / cs.HC 24 / cs.GT 8 / cs.NE 4 / cs.MA 3 / cs.LO 2) → in-window filter [2609.28475–2609.30264] → **483 unclaimed** after subtracting sibling-claimed IDs → title + abstract keyword sweep (game / RL / self-play / world model / NPC / benchmark / agent …) → **~29 concise targets deepened at full-abstract depth** → **26 curated featured + 3 runner-ups, all 29 IDs grep-verified 0 hits in `wiki/` at write time** (the 09-25 siblings that raced ahead of me — arxiv-daily, arxiv-ai-search, arxiv-paper-check — are all covered by the whole-wiki `rg` diff).
>
> **Continuity / already-covered by the 09-25 siblings (cross-referenced, not re-featured):** the window's *pure-game and world-model marquees* were claimed hours before my write by the same-day digests — **PUBG Ally** 2609.29837 (KRAFTON live-service conversational teammate, +25.1pp net recommend) → [arxiv-ai-search 09-25 §5.4](../2026-09-25/arxiv-ai-search.md); **Multiplayer Colonel Blotto PPAD-hardness** 2609.30019 → §5.1; **Three-Player Auction Bridge iterative dominance** 2609.29615 → §5.2; **Search-Aware RL for Roblox query understanding** 2609.30177 → §1.5; **Anchored Planning** 2609.30036 (frozen world models plan better than goal-image scoring) → §6.2; **RLVR spin-glass theory** 2609.28625 → §6.1; **RWM** (planning in representation geometry) 2609.29171 and **GRAFT** (trajectory-graph step-level advantages) 2609.28963 → [arxiv-daily 09-25](../2026-09-25/arxiv-daily.md); **PixelJev** visual-choice model 2609.29283 → daily §8.1; **ExplorationBench** (verifiable Alien-Worlds sandboxes) 2609.30199 → [arxiv-paper-check 09-25](../2026-09-25/arxiv-paper-check.md) §Runner-ups. Notably, the ai-search report **explicitly parked** three game-relevant IDs in its unclaimed-remainder map — **Self-Play Pretraining with Zero Data** 2609.30063, **AD-WM action-discriminative world models** 2609.30264, **PAWS policy-driven agentic world simulation** 2609.28547 — which I now claim (grep-verified unfeatured).
>
> **Window character**: with the pure-game marquees taken, the unclaimed remainder is dominated by **world models at the representation level** (object permanence, delta/latent dynamics, action-discriminability, graph topologies, navigation) and **agent-capability engineering** (role-playing RL curricula, delay-of-gratification survival, skill composition/retirement, privileged-information practice). A strong cognitive-science undercurrent: object permanence, bounded rationality via reaction time, and delayed gratification as formal evaluation instruments.

---

## 1. Game RL, Multi-Agent Learning & Game Theory

### 1.1 Self-Play Pretraining with Zero Data
- **Authors**: (not parsed in full; arXiv 2609.30063)
- **Affiliation**: not stated (tentative — self-referential pretraining / Solomonoff-inspired line)
- **Venue**: arXiv preprint (2609.30063), announced in the Fri 25 Sep window — placed in the ai-search remainder map, unclaimed until now
- **Key Innovations**: Pushes self-play past the data-curation bottleneck: instead of scaling on human-curated corpora, the model itself generates the data most useful for its own improvement. Two models trained in tandem from random init — a **generator proposes programs interpreted by a universal Turing machine** (byte-sequence synthesis; the search space = all computable structure, a Solomonoff-induction echo), a **learner autoregressively predicts those byte sequences** with plain next-token CE. The generator is trained with **RL to produce sequences at the frontier of the learner's capabilities** — an adaptive curriculum with effectively unbounded data, limited by compute rather than human knowledge.
- **Results**: Zero-shot loss on several natural datasets scales predictably in self-play compute (clean transfer test — neither model ever saw natural data); models exhibit in-context learning and discover recognizable mathematical sequences during training.
- **Significance**: The most direct "self-play as a learning algorithm, not just a game tactic" statement this window — the generator-vs-learner frontier equilibrium is the same dynamical structure as game self-play, relocated to pretraining data synthesis.
- **Link**: https://arxiv.org/abs/2609.30063

### 1.2 AdvRole: Adversarial Closed-Loop Curriculum for Evolving Role-Playing Agents
- **Authors**: Zheng Zhang, Liu Liu, Qi Chai, Deheng Ye, Peilin Zhao, Mao Zheng, Hao Wang
- **Affiliation**: not stated (inferred — Deheng Ye and Peilin Zhao are Tencent AI Lab role-play/RL researchers) (tentative)
- **Venue**: arXiv preprint (2609.28609, cs.AI), announced in the Fri 25 Sep window
- **Key Innovations**: RL for LLM role-playing agents is normally trained on a **fixed scenario pool collected up-front** — a distributional bottleneck: as the agent improves, the scenarios where it performs poorly change, while the training distribution stays static. **AdvRole** turns role-playing RL into a **closed-loop adversarial curriculum**: an **Actor** learns to role-play while a **Rewriter** edits character profiles and dialogue contexts into actor-specific hard scenarios, trained with a **performance-gap reward** that favors rewrites reducing the Actor's score relative to the original scenario. The scenario pool therefore co-evolves with the Actor and tracks under-mastered regions of the character-context space.
- **Results**: Outperforms baselines on three role-playing benchmarks (English + Chinese) plus a new multilingual benchmark released with the paper.
- **Significance**: The "adversary-as-curriculum-designer" pattern applied to NPC/role-play RL — the direct map from agent training to content generation that game studios need for evolving character difficulty.
- **Link**: https://arxiv.org/abs/2609.28609

### 1.3 Multi-Agent Debate for Explainable Trading: Reasoning, Consensus, and Performance in Simulated Markets
- **Authors**: Juli Huang, Alanood Alrassan, Deveen Harischandra, Theodore Wu, Veljko Skarich, Matthew Hayes
- **Affiliation**: not stated (tentative)
- **Venue**: arXiv preprint (2609.29701, cs.AI), announced in the Fri 25 Sep window
- **Key Innovations**: Does better *reasoning quality* in multi-agent debate translate into better *economic outcomes*? Specialized agents propose, critique, and revise portfolio allocations in historical market simulations; reasoning quality is scored on **logical validity / evidential support / alternative consideration / causal alignment** and compared against financial performance.
- **Results**: Across 210 controlled runs, aggregate reasoning quality shows **no meaningful relationship with Sharpe ratio (r = 0.07, p = 0.29) or total return (r = 0.03, p = 0.70)**; structured prompting lifts measured reasoning +17.7% (d ≈ 2.0) but the gains don't reach returns. Root cause is **sycophantic convergence** — agents abandon independent positions during critique-revision cycles. A **Jensen-Shannon divergence intervention that preserves disagreement** improves Sharpe +0.14 (p = 0.028) and Sortino +0.25 (p = 0.026), while stronger-causal-reasoning interventions do not.
- **Significance**: A decisive answer for game/NPC debate-based decision loops: diversity preservation, not reasoning polish, is what pays — the same tradeoff applies to trading bots, debate-based game AIs, and deliberating agent squads.
- **Link**: https://arxiv.org/abs/2609.29701

### 1.4 Epistemic-Probabilistic Model for Guarded Multi-Agent LLM Coordination (EPLA)
- **Authors**: Mehdi Nasiri, Mohammad Saeed Arvenaghi, Sadegh Vaezi, Ebrahim Ardeshir-Larijani
- **Affiliation**: not stated (tentative)
- **Venue**: arXiv preprint (2609.29366, cs.AI), announced in the Fri 25 Sep window
- **Key Innovations**: Attacks two gaps in multi-agent LLM systems under the lens of multi-agent-systems theory — the absence of **social behavior** and the lack of **coordination mechanisms**. **EPLA (Epistemic Probabilistic Language Agents)** is a neuro-symbolic architecture where a **Symbolic Guard** provides structured diagnostic feedback; the LLM emits *typed actions* and the Guard controls their execution against an authoritative symbolic state. The epistemic layer is formalized on a gossip testbed through **epistemic lottery gossip models** — view-based call histories combined with agent-indexed probability weights.
- **Results**: Formalization + architecture proposal for *guarded* coordination under uncertainty; motivates how such a formalism addresses agentic-LLM shortcomings (unknown emergent behavior, natural-language-bounded interaction).
- **Significance**: "Actions pass through a symbolic guard" is a concrete mechanism design for multi-agent game bots and NPC squads where the LLM proposes and the simulator/ruleset disposes.
- **Link**: https://arxiv.org/abs/2609.29366

### 1.5 Graph-Based Inference and Topology-Aware MARL for Large-Scale Railway Network Management
- **Authors**: Giacomo Arcieri, Gregory Duthé, Christophe Muller, Konstantinos G. Papakonstantinou, Daniel Straub, Eleni Chatzi
- **Affiliation**: not stated (inferred — Straub, Chatzi, Papakonstantinou are at ETH Zürich; Duthé alumnus ETH/EPFL; data partner Swiss Federal Railways) (tentative)
- **Venue**: arXiv preprint (2609.30150, cs.LG), announced in the Fri 25 Sep window
- **Key Innovations**: Scaling RL to large infrastructure networks: a **hierarchical Bayesian model with a Gaussian Process on Graph kernel** infers a realistic spatially-correlated networked maintenance environment from Swiss Federal Railways data; a **topology-aware MARL framework** (graph neural networks + graph Transformers) optimizes network-level policies. Central contribution is **zero-shot transfer**: graph-based agents trained on small network portions deploy directly on large-scale unseen networks with no retraining.
- **Results**: Significantly outperforms optimized heuristics and standard MARL baselines on large networks, with reduced training time.
- **Significance**: Ports the graph-MARL + zero-shot-transfer recipe into a real-world large-scale sequential decision system — a template for networked game-world management (economies of scale, spatial correlations) beyond the usual grid worlds.
- **Link**: https://arxiv.org/abs/2609.30150

### 1.6 Policy Complexity, Reaction Time, and Bounded Rationality in Reinforcement Learning (MI-SARSA)
- **Authors**: James Wu, Chris R. Sims
- **Affiliation**: not stated (inferred — Chris R. Sims is at Rensselaer Polytechnic Institute, computational cognitive science) (tentative)
- **Venue**: arXiv preprint (2609.28737, cs.LG), announced in the Fri 25 Sep window
- **Key Innovations**: Biological agents don't learn under unlimited computation — perception, attention, and working-memory constraints bound policy complexity, which standard RL ignores. **MI-SARSA** is an on-policy TD algorithm with **mutual-information regularization** through a learned marginal action prior and a penalty on state-specific deviations: state information is used only when its expected return benefit justifies the informational cost. The same state-specific cost that compresses the policy also produces **trial-level reaction-time predictions** — unusual for RL, which predicts choices/returns but rarely latency.
- **Results**: Produces a reward-complexity tradeoff; stronger information penalties yield simpler policies, lower control costs, faster reaction times; under environment shift, more regularization reduces post-switch degradation but lowers asymptotic return (robustness-capacity tradeoff).
- **Significance**: A principled "thinking time" cost for decision-making agents — directly relevant to game bots that must balance reaction speed against policy sophistication, and to opponent modeling with bounded rationality.
- **Link**: https://arxiv.org/abs/2609.28737

---

## 2. Game AI Bots, LLM Agents & Human-Behavior / NPC Simulation

### 2.1 Delay-of-Gratification as a Multi-Agent Survival Micro-benchmark for Long-Horizon LLMs
- **Authors**: Olga Manakina, Igor Bogdanov, Chung-Horng Lung
- **Affiliation**: not stated (inferred — Chung-Horng Lung is at Carleton University; consistent with the paired 2609.29508 paper) (tentative)
- **Venue**: arXiv preprint (2609.29509, cs.CL), announced in the Fri 25 Sep window
- **Key Innovations**: The **Stanford marshmallow experiment** as a machine test: ReAct agents operate minute-by-minute with a "raise a question" tool under a per-step budget, choosing each step between continuing to delay a reward vs claiming it immediately (terminating). Full-factorial over **social context (broadcast vs isolated), personas (age, hedonic drive), and metacognitive policy (mandatory vs optional tool use)**; outcomes via **Kaplan-Meier survival curves and discrete-time hazard models** over a long risk horizon — 19,200 agent trajectories across 64 cells.
- **Results**: Sharp early "eat" impulse; only **75.9% persist to the end**. Isolation reduces per-minute risk vs broadcast; a must-use self-questioning policy *increases* risk. Agents ask ≈7.12 questions on average, hitting the per-step budget in ≈6% of minutes; questioning declines faster under broadcast than isolation. Ablations: removing hedonic drive/persona age raises survival and completion (near 1.0) while preserving the must-vs-may ordering.
- **Significance**: A compact, auditable, time-resolved benchmark for **social contagion + tool-use dynamics** in long-horizon LLM agents — survival statistics as the evaluation regime for NPC persistence and temptation resistance in agent-dense games.
- **Link**: https://arxiv.org/abs/2609.29509

### 2.2 Evaluation of Multi-Turn Consistency in LLM Agents: Survival Analysis and Failure-Rationale Taxonomy
- **Authors**: Igor Bogdanov, Olga Manakina, Chung-Horng Lung
- **Affiliation**: not stated (inferred — Carleton University, companion to 2609.29509) (tentative)
- **Venue**: arXiv preprint (2609.29508, cs.CL), announced in the Fri 25 Sep window
- **Key Innovations**: Companion to §2.1: evaluates **temporal consistency** directly, treating the first reward-claim as a **time-to-event** outcome across a full-factorial manipulation of social visibility / persona stressors / deliberation policy — **84,540 trajectories across 8 model families**. Then builds a **seven-category failure-rationale taxonomy** from 13,780 terminating deliberation traces via LLM-assisted labeling + human audit (κ = 0.83).
- **Results**: Early failures are more impulse-driven, later failures more fatigue- and cost-benefit-framed; public settings increase norm-oriented justifications. Finds a **deliberation-inconsistency association**: among failures, longer deliberation correlates with *higher* intra-rationale contradiction (simultaneous pro-delay and pro-claim statements) — challenging "more reasoning text ⇒ more consistency". Produces model-specific **"failure fingerprints"** and distinct temporal reliability regimes.
- **Significance**: The diagnostics layer for agent persistence — rationale taxonomy + hazard modeling = an evaluation lens for diagnosing *when and why* multi-turn NPC/agent behavior drifts, not just whether it drifts.
- **Link**: https://arxiv.org/abs/2609.29508

### 2.3 SkillPivot: Deviation-Guided Skill Self-Evolution for LLM Agents
- **Authors**: Yichun Feng, Jiawei Wang, Haozhe Sun
- **Affiliation**: not stated (tentative)
- **Venue**: arXiv preprint (2609.29154, cs.AI), announced in the Fri 25 Sep window
- **Key Innovations**: Failed trajectories are rarely *entirely* wrong — an agent often collects useful evidence and makes progress before deviating into an erroneous suffix. Improving skills by forcing failures to match a fixed successful roll-out is therefore inappropriate, and coarse whole-trajectory reflection wastes signal. **SkillPivot** detects the **deviation point** (transition from a useful prefix to an erroneous suffix) using execution validity, goal progress, and action diversity; a stronger teacher continues from the same prefix under the same interaction history to produce a successful alternative, and the student's failed suffix is contrasted against it for **localized skill updates** that preserve already-effective guidance.
- **Results**: Consistently outperforms competing skill-evolution methods on ToolQA, LogicBench, and WildClawBench; improves multiple agent models and yields compact, transferable skill updates.
- **Significance**: "Skill by surgical credit — not wholesale rewriting" — the game-agent equivalent of fixing a losing strategy's late-game blunders instead of invalidating the whole approach.
- **Link**: https://arxiv.org/abs/2609.29154

### 2.4 Safe Skill Retirement for Physical Agents
- **Authors**: Zhonghao Zhan, Xiao Ma, Hamed Haddadi
- **Affiliation**: not stated (inferred — Hamed Haddadi is at Imperial College London) (tentative)
- **Venue**: arXiv preprint (2609.29543, cs.AI), announced in the Fri 25 Sep window
- **Key Innovations**: Agent skills bundle procedural guidance with execution conditions governing **authority, user consent, and live environment state**; when model capabilities advance, maintainers prune instructions that look redundant on authorized benchmark tasks — but authorized tests can leave **dormant safety conditions untested**. Introduces **matched authority counterfactuals** (hold requested action / tool parameters / intended effect fixed while varying one governing predicate) and a **two-gate retirement certificate**: preserve authorized utility within a declared margin AND produce zero unauthorized protected effects.
- **Results**: Across four frontier/local models × 12 skill bundles (2,592 cells), task-certified reductions remove **over 94% of skill clauses** and preserve authorized completion yet produce **unauthorized protected effects in every bundle**. Boundary enforcement passes the protected-effects gate but fails utility for one configuration; one bounded combined protocol passes both gates across all four configs at zero utility headroom. End-to-end check on a real Home Assistant camera chain.
- **Significance**: A formal "safety audit before you delete a skill" discipline — transferable to pruning NPC/agent capability sets where bench-passing removals can silently break consent/authority behavior in live play.
- **Link**: https://arxiv.org/abs/2609.29543

---

## 3. Game Foundation Models, World Models & Game Agents

### 3.1 Training Object Permanence in World Models (WROP / PWM-WROP)
- **Authors**: Haotian Zhang, Fengyuan Yu, Dezhi Luo, Haoran Sun, Zehong Zhao, Qingying Gao, Yihan Li, Siyuan An, Huayi Qin, Yilan Zhang, Zhengze Jiang, Pinyuan Feng, Renrui Zhang, et al. (+ more)
- **Affiliation**: not stated (inferred — large multi-lab consortium around video/world-model training; Renrui Zhang historically OpenAI-lab / video-model foundations) (tentative)
- **Venue**: arXiv preprint (2609.28654, cs.CV), announced in the Fri 25 Sep window
- **Key Innovations**: Asks whether video-generation world models have emerged **object permanence** — a hallmark human cognitive prior — and whether it can be *trained in* with a core-cognition-inspired dataset. **WROP (World Reasoning with Object Permanence)** = 150 hand-designed cognitive-science tasks in **six cognitive categories**; Blender generators randomize speed / lighting / camera / nuisance parameters while preserving cognitive structure → 10,000+ samples per task. Releases a **1.5M-sample training corpus** and a **300-question exam**; evaluates 14 video models (3 reference-to-video, 7 edit, 4 continuation).
- **Results**: **PWM-WROP**, their 16B world model, ranks **first among continuation models and third overall** in a blind pairwise Elo study (behind only a statistical tie of two reference-to-video models). Full open release: data, exam, model answers, scores, weights, and PWM (native-PyTorch training stack on AWS Trainium2).
- **Significance**: The cognitive-core training recipe for world models — permanence/solidity as a *trainable* axis rather than an emergent accident — with an open benchmark to detect it in game world models.
- **Link**: https://arxiv.org/abs/2609.28654

### 3.2 DeltaWAM: Delta World Action Models for Bimanual Manipulation
- **Authors**: Han Yan, Zishang Xiang, Haokai Jiang, Zeyu Zhang, Qilin Wang, Weiyu Guo, Yandong Guo, Boxin Shi, Hao Tang
- **Affiliation**: not stated (inferred — Boxin Shi and Hao Tang are historically Peking University, video/3D vision) (tentative)
- **Venue**: arXiv preprint (2609.28811, cs.CV/cs.RO), announced in the Fri 25 Sep window
- **Key Innovations**: World-action models (WAMs) transfer video-generator priors to control, but existing WAMs predict **dense future frames**, repeatedly modeling largely unchanged content and coupling action-conditioned dynamics to nuisance appearance. **DeltaWAM** instead jointly predicts **visual deltas and actions** using dense-anchor / sparse-delta / action streams in three sharing architectures, plus **Streaming Delta Memory (SDM)** — cached anchor context updated with compact observed deltas so the heavy video expert isn't reprocessed per step.
- **Results**: On RoboTwin, DeltaWAM + SDM lifts average success to **85.4% clean / 83.9% under visual randomization** (from Fast-WAM 81.3% / 75.8%); the three architectures cut training FLOPs 17.8–23.8%, SDM cuts one-step inference latency **−36.6%** and FLOPs **−31.6%**; real-world evaluations show the highest overall success and normalized progress.
- **Significance**: "Predict only what changed" is the efficiency thesis for action-driven world models — the same delta principle keeps real-time game/embodied simulators cheap under repeated interaction.
- **Link**: https://arxiv.org/abs/2609.28811

### 3.3 Beyond Static Graph World Models: Learning Stochastic Latent Dynamics over Evolving Topologies (GDM)
- **Authors**: Alex Schutz, Nick Hawes, Victor-Alexandru Darvariu
- **Affiliation**: not stated (inferred — Hawes and Darvariu are at University of Oxford, Oxford Robotics Institute) (tentative)
- **Venue**: arXiv preprint (2609.28670, cs.AI/cs.LG), announced in the Fri 25 Sep window
- **Key Innovations**: Existing graph world models assume **fixed topologies** in deterministic, fully observable environments. **GDM (Graph Dynamics Model)** handles the general case of **evolving topologies in stochastic, partially-observable settings**: a **sparse recurrent adjacency matrix** models topology updates and drives message-passing, while a recurrent state-space architecture models stochastic transitions. Also identifies an evaluation gap — existing methods can't compare predicted vs true *distributions* over the joint graph state (interdependent topology + node features + graph features) — and introduces the **Graph Distribution Distance (GDD)**: maximum mean discrepancy with a graph kernel.
- **Results**: Outperforms baselines across several stochastic / partially-observable environments and shows **zero-shot generalisation on large graphs**.
- **Significance**: Relational world models for worlds whose *structure itself changes* — quest/world-state graphs, evolving faction topologies, and networked game economies, not just fixed boxes-and-arrows simulators.
- **Link**: https://arxiv.org/abs/2609.28670

### 3.4 Visual Representation and History Modeling for Navigation World Models
- **Authors**: Guangfu Guo, Xiaoqian Lu, Rui Liu, Yutong Chen, Kunpeng Liu, Long Cheng
- **Affiliation**: not stated (tentative)
- **Venue**: arXiv preprint (2609.29555, cs.CV), announced in the Fri 25 Sep window
- **Key Innovations**: Two design questions for **Navigation World Models** (action-conditioned visual-future predictors for planning): which visual representation, and how to model observation history under repeated candidate queries. Standard Global-Softmax re-processes history each time, scaling badly with context/multi-query planning. Under a unified conditional flow-transformer: compares five frozen visual representations, then builds **Cached-Linear** (local/shifted-window attention for target mixing + linear attention for reusable history) and **Balanced Gated Delta Network (GDN)** adding frame-wise recurrent memory.
- **Results**: Representation choice is objective-dependent — **PAE-L** best for reconstruction, **RAE-B** for direct prediction, **V-JEPA** for long-horizon rollout. Cached-Linear substantially cuts compute/memory on shared-history workloads vs Global-Softmax; Balanced GDN improves selected direct-prediction endpoints with efficient context reuse.
- **Significance**: "Which optic, which memory policy" evidence for the representation layer of navigation/game world models — direct guidance for picking visual encoders and history caches in long-horizon simulators.
- **Link**: https://arxiv.org/abs/2609.29555

### 3.5 HelloWorld: Towards Practical Applications of Generative Driving World Models
- **Authors**: Fan Lu, Hanshi Wang, Zijing Wang, Quan Feng, Zhi Wang, Shijie Chen, Xianming Zeng, Yujian Zhang, Jiazhe Wang, Xin Zha, Kai Wang, Zhijie Zhao, Lin Zhu, Tianyi Ya(n) et al. (auth-list truncated)
- **Affiliation**: not stated (inferred — Chinese academic/industry driving-AI cluster) (tentative)
- **Venue**: arXiv preprint (2609.28931, cs.CV), announced in the Fri 25 Sep window
- **Key Innovations**: A **2B driving world model system** aimed at production demands: generalization across diverse scenes, faithful response to prescribed controls, coherent multi-sensor observation generation, and efficiency under repeated inference. Progressively specializes broad video priors into controllable driving generation using **ego pose, HD maps, and 3D boxes**; a **block-causal generation interface** + adaptation to self-generated context aligns with sequential simulation; supports **synchronized seven-camera RGB** and **conditional LiDAR synthesis**; distilled toward few-step inference.
- **Results**: Evaluates visual quality, control fidelity, cross-view consistency, robustness under repeated generation, inference efficiency, and LiDAR synthesis — a unified framework for scalable driving data generation and interactive simulation.
- **Significance**: An industrial-grade "interactive world-model as a service" stack — the production engineering pattern (multi-sensor, few-step inference, control fidelity) game world models need to become playable products.
- **Link**: https://arxiv.org/abs/2609.28931

### 3.6 Underwater C³-JEPA: Object-Centric Cross-View World Model for ROV Salvage
- **Authors**: Yuncong Yang, Jinlong Li, Yulong Xue, Feng Wu, Chunwen Zhang, Lei Qiao, Xuyang Wang
- **Affiliation**: not stated (inferred — Chinese underwater-robotics / USTC-adjacent cluster) (tentative)
- **Venue**: arXiv preprint (2609.30214, cs.AI/cs.RO), announced in the Fri 25 Sep window
- **Key Innovations**: C³-JEPA (cross-view, control-conditioned, context-extended): an object-centric multi-view predictive world model for **near-field heavy-load underwater ROV salvage** — no contact sensors. Predicts in latent space how the task-object evolves under contact interaction and vehicle hydrodynamic lag, from synchronized multi-view RGB + control signals. Encodes multi-camera obs into task-object/context tokens, fuses cross-camera evidence via held-out-view attention, predicts future states conditioned on control; weak binding anchors target/gripper at low label cost; **SIGReg** sharpens geometry.
- **Results**: Transfers substantially more task-relevant info to downstream probes than a reconstruction-free latent baseline; supports **MPC candidate evaluation and imagined-rollout behavior-agent training**; on real underwater video, the same architecture recovers a withheld camera's object state and stays ahead of persistence.
- **Significance**: Object-centric JEPA world modeling in a hard, contactless, partially-observable domain — evidence that latent prediction + MPC rollout works where contact sensing is impossible, a regime that simulated game-physics worlds share.
- **Link**: https://arxiv.org/abs/2609.30214

### 3.7 AD-WM: Action-Discriminative World Models for Counterfactual Model Predictive Control
- **Authors**: (not parsed in full; arXiv 2609.30264 — placed in the ai-search remainder map, unclaimed until now)
- **Affiliation**: not stated (inferred — world-model MPC / LeWM-adjacent control lab) (tentative)
- **Venue**: arXiv preprint (2609.30264, cs.RO/cs.LG), announced in the Fri 25 Sep window
- **Key Innovations**: Latent world models trained on **factual transitions** can achieve low factual error yet **poorly distinguish candidate actions** — a disease for MPC, which must compare alternatives from the same state. **AD-WM** is an action-discriminative joint-embedding world model: residual latent dynamics + **predictor-level action-recovery regularization** (inverse dynamics, normalized recovery objective motivated by conditional mutual information), so planning transitions preserve action information; auxiliary heads are discarded at test time, leaving MPC unchanged.
- **Results**: On OGBench-Cube, AD-WM lifts hard-start success **3.7% → 52.0%** over a matched LeWM baseline and improves mean success in 4/5 simulation environments. Diagnostics: factual prediction error and whole-bank action ranking **do not** follow closed-loop success ordering; CEM-aligned elite regret does. With frozen V-JEPA 2 + matched DROID post-training, zero-shot transfer to Franka pick-and-place rises **42.2% → 71.1%** without lab-specific adaptation.
- **Significance**: "Train for counterfactual discriminability, not factual fidelity" — arguably *the* most direct insight this window for what a planning world model should optimize, directly transferable to game-planning simulators.
- **Link**: https://arxiv.org/abs/2609.30264

---

## 4. Procedural Content Generation, 3D-World Generation & Automated Game Design

**This window's unclaimed remainder contains 0 standalone PCG/game-design papers** — the second consecutive day I've emptied this section's unclaimed pool. Closest overlaps live in adjacent sections: **AdvRole** (2609.28609, §1.2) treats scenario *con*tent as a co-evolved curriculum output (content generation as training infrastructure), and **Self-Play Pretraining** (2609.30063, §1.1) is data generation by self-play, but neither is a level/content-generation paper. Level-generation and game-design marquees from today's wider mailing were cross-referenced rather than re-featured (see final section).

---

## 5. Game Benchmarks & Evaluation Suites

### 5.1 PAWS: Policy-driven Agentic World Simulation
- **Authors**: (not parsed in full; arXiv 2609.28547 — placed in the ai-search remainder map, unclaimed until now)
- **Affiliation**: not stated (inferred — financial multi-agent simulation / event-extraction group) (tentative)
- **Venue**: arXiv preprint (2609.28547, cs.AI/cs.CL), announced in the Fri 25 Sep window
- **Key Innovations**: Policies propagate through public communication, institutional decisions, and stakeholder responses — yet financial multi-agent simulation datasets rarely tie these to temporally-aligned historical evidence. **PAWS** covers **36 verified U.S. financial/economic policy episodes, 12,727 policy-linked news records, 65,291 source-grounded stakeholder actions**, each action linked to supporting news and represented by a **multi-layer event frame** (interaction mode, financial-action family/subtype, semantic attributes, conditional mappings to external taxonomies); entities normalized to organizations; actions aligned with daily market-return context for **policy-agent simulation replay**.
- **Results**: On 2,522 stratified action samples, independent AI + human reviewers reach **89.4% initial agreement** (adjudicated after); 2008 short-selling-ban and 2001 decimalization case studies recover documented policy timelines and market patterns. A **replay study shows high accuracy can mask failure to detect rare stakeholder actions** — action timing and calibration are the central challenges.
- **Significance**: An auditable, source-grounded substrate for **agent influence, policy-response cascades, and action-outcome alignment** in historically grounded simulations — the data discipline for economic/mini-game NPC worlds that must not hallucinate their own history.
- **Link**: https://arxiv.org/abs/2609.28547

### 5.2 Beyond Spatial Benchmarks: From Spatial Reasoning to Navigation (Spatial-Nav)
- **Authors**: Xun Huang, Shijia Zhao, Rongsheng Qu, Jiayuan Li, Xin Lu, Weixin Li, Chenglu Wen, Cheng Wang
- **Affiliation**: not stated (inferred — Cheng Wang and Chenglu Wen are at Xiamen University, spatial-computing cluster) (tentative)
- **Venue**: arXiv preprint (2609.29934, cs.CV), announced in the Fri 25 Sep window
- **Key Innovations**: Finds a **gap between benchmark-oriented spatial specialization and navigation performance**: existing spatial benchmarks test isolated inferences from images/video with little connection to downstream navigation. Builds **Spatial-Nav-100K**, fine-tunes in two stages (a shared **spatial-navigation foundation**, then phase-specialization), and introduces **Spatial-NPD** where a teacher conditioned on spatial priors produces grounded action preferences that are **distilled into a student policy** — so no explicit spatial reasoning is needed at inference.
- **Results**: With **45 A100 GPU-hours** of policy training, an 8B model reaches **SR/SPL 77.4/35.4 on HM3D-v0.2, 60.2/30.5 on v0.1, 47.9/20.6** on train-unseen MP3D — outperforming systems relying on closed-source models or thousands of GPU-hours, at **148 ms per action step**. All code/datasets public.
- **Significance**: "Calibrate the benchmark to the goal" — spatial reasoning only pays off in navigation when supervision aligns with navigation goals/phases/decision-learning; the same lesson applies to game agents evaluated on orthogonal reasoning suites.
- **Link**: https://arxiv.org/abs/2609.29934

---

## 6. Industry Game AI, Real-Time Inference & Deployment Economics

**This window's unclaimed remainder contains 0 standalone industry-game-AI papers** — the marquees were claimed earlier today by the siblings. Cross-referenced rather than re-featured:
- **PUBG Ally** 2609.29837 — *live-service conversational teammate*: KRAFTON voice-enabled embodied teammate (LLM agent + fast control layer), trained on ~39k real sessions, deployed on-device with safety guardrails; net recommend **+25.1pp** across 141 countries — [arxiv-ai-search 09-25 §5.4](../2026-09-25/arxiv-ai-search.md).
- **Search-Aware RL for Roblox query understanding** 2609.30177 — *production search RL*: distill-then-RL with per-component live-search rewards, **NDCG@20 +8.9** over SFT — [arxiv-ai-search 09-25 §1.5](../2026-09-25/arxiv-ai-search.md).
- **HelloWorld** 2609.28931 (my §3.5) is the window's closest *industrial world-model system* paper and is featured here rather than in this section.

---

## 7. Related RL Techniques (RLVR, Credit Assignment, Exploration, Learning from Experience)

### 7.1 RLVR for Small Search Agents
- **Authors**: Gaurisankar Jayadas, Aske Plaat, Álvaro Serra-Gómez, Sandheep P
- **Affiliation**: not stated (inferred — Aske Plaat is at Leiden Institute of Advanced Computer Science) (tentative)
- **Venue**: arXiv preprint (2609.28765, cs.AI), announced in the Fri 25 Sep window
- **Key Innovations**: Tests whether the reason-over-search RLVR recipe works at small scale without teacher distillation. Trains **Qwen3.5-0.8B with GRPO + an interleaved Wikipedia-search tool** on MuSiQue, varying only the reward across three shapes × three seeds; evaluates every checkpoint on a seven-benchmark QA suite.
- **Results**: Works — best run **0.352 average exact match vs 0.092 untrained floor (3.8×)** with no distillation in the loop. But the **Search-R1-faithful exact-match-only reward is the worst of the three** at every seed and horizon — even on exact match itself. Verdict: sparse exact-match RLVR (the math/code default) is the wrong starting point at this size; small-model RLVR needs its own reward-design study.
- **Significance**: A seed-level-evidenced guardrail for anyone applying RLVR to small game/simulation agents — reward shape, not model size, is the lever below 1B.
- **Link**: https://arxiv.org/abs/2609.28765

### 7.2 Privileged Self-Practice (PSP): From Self-Distillation to Privileged Information for Multi-Turn Agents
- **Authors**: Xingyu Su, Abhishek Kumar, Qing Ping, Youzhi Luo, Jonathan Buck, Zach Zhang, Subramanian Chidambaram, Vinayak Arannil
- **Affiliation**: not stated (inferred — Kumar, Zhang, Arannil, Buck, Chidambaram are AWS/NVIDIA-adjacent; LLM-post-training line) (tentative)
- **Venue**: arXiv preprint (2609.29051, cs.AI), announced in the Fri 25 Sep window
- **Key Innovations**: On-policy self-distillation (OPSD) injects privileged information (PI) into the **loss** — and this paper shows that in multi-turn agents it teaches the student "to act with confidence but without the information behind it" (behaves as if it had PI it never observed; can fall *below* the untrained base). **PSP keeps the PI and moves it from loss to sampler**: when a student's rollouts mostly fail, an analyzer injects a short per-task instruction, the task is re-sampled with it in context, and training proceeds with an unchanged GRPO objective — PI stays in the prompt, never in the loss.
- **Results**: Across AppWorld and SWE-bench Verified × 3 student models, PSP gets the best average score in every setting and is the only method consistently beating plain GRPO — task-goal completion **up to +65% on AppWorld**, resolved rate **up to +61% on SWE-bench Verified**.
- **Significance**: "Use privileged hints at rollout time, not supervisor time" — the credit/loss-design lesson for teaching game agents from hidden game state without baking oracle signals into the objective.
- **Link**: https://arxiv.org/abs/2609.29051

### 7.3 Certified Predictive Value-of-Advice Gating for Cost-Aware LLM Guidance in RL
- **Authors**: Ibne Farabi Shihab, Md Najmus Swaqeeb, Abu Sa-Adat Mohamed Moon-Im Al Ahsan
- **Affiliation**: not stated (tentative)
- **Venue**: arXiv preprint (2609.29548, cs.LG), announced in the Fri 25 Sep window
- **Key Innovations**: LLM advice accelerates RL but calls are costly and responses may be stale/wrong. Formulates advice acquisition as **response-contingent metareasoning**: before querying, the controller predicts possible parsed responses, evaluates the decision + declared continuation each would produce, and queries **only when a lower confidence bound on predictive value exceeds the priced cost**; execution is separately gated by an action-specific certificate.
- **Results**: On BabyAI, a proxy-calibrated controller with Qwen2.5-1.5B/7B advisors improves GoToObj return over no-query by +0.029–0.030 across 20 seeds while **reducing calls >97% vs always-query**; GoToLocal is a null result. Exactly-matched-call tests show an advantage over random placement only for the 1.5B advisor; Mondrian calibration lifts decision-relevant coverage 0.47→0.85 (still below the 0.90 target). Verdict: robust sparse advice volume on a useful task, not a proven per-state placement advantage.
- **Significance**: Honest metareasoning for "when to ask the big model" — the cost certificate framing game-NPC/reasoning loops need before wiring an advisor into every decision.
- **Link**: https://arxiv.org/abs/2609.29548

### 7.4 Streaming Deep RL for Adaptive Continual Learning in Robotics
- **Authors**: Teeratham Vitchutripop, Alyssa Quarles, Wenhe Zhang, Richard Xue, Daniel Rakita
- **Affiliation**: not stated (inferred — Daniel Rakita is at University of Wisconsin–Madison, robot learning) (tentative)
- **Venue**: arXiv preprint (2609.28807, cs.RO), announced in the Fri 25 Sep window
- **Key Innovations**: First analysis of **streaming deep RL as a continual learning framework** for robot adaptation: after pretraining, updates use only the latest experience stream (mimicking moment-to-moment biological learning) to adapt to unforeseen changes in the agent, environment, or goals — instead of forever growing an offline dataset.
- **Results**: In quadruped locomotion, stream learning with certain optimizers + plasticity-loss mitigation leverages pretraining-domain knowledge to adapt online, **outperforming batch on-policy methods and improving task success up to 90% over the pretrained policy**; manipulation extrapolates the observation **partially**, with stability/performance limits.
- **Significance**: Evidence that game/robot agents can keep learning from their live experience stream — with an honest account of where streaming adaptation breaks (different morphologies/task regimes).
- **Link**: https://arxiv.org/abs/2609.28807

### 7.5 Uncertainty-Gated Exploration Noise Suppresses Task Collapse in Online RL Fine-Tuning of a Flow-Matching VLA Policy
- **Authors**: Mehmet Turan Yardımcı, Yunus Emre Çoğurcu
- **Affiliation**: not stated (tentative)
- **Venue**: arXiv preprint (2609.28838, cs.LG/cs.RO), announced in the Fri 25 Sep window
- **Key Innovations**: Online RL fine-tuning of pretrained flow-matching VLA policies risks **task collapse** — continued updates destroy per-task competence while aggregate metrics look healthy. Under a matched small-compute budget on LIBERO-10 with a 450M SmolVLA trained by PPO with stochastic (SDE) sampling, compares three exploration-noise policies differing in one live variable: fixed noise, a ReinFlow-style learned noise network, and an **uncertainty-gated controller** redistributing exploration across task streams from task-agnostic novelty + competence signals (no task labels, no episode boundaries).
- **Results**: Under the pooled definition, fixed noise collapses 2/3 seeds and learned noise every seed to iteration 200, while the **controller collapses none in any of its 3 seeds**; measured parameter displacement shows the controller's action expert keeps changing with mean applied noise near the fixed scale. No arm beats behavior-cloning within budget. Ships tools measuring per-task collapse under four definitions, noise rescoring, and instrument tares.
- **Significance**: "Where you explore across tasks matters more than how much" — a reproducibility-quality exploration finding for continued game-agent training without task supervision.
- **Link**: https://arxiv.org/abs/2609.28838

### 7.6 PoEM: Predicting RL Outcomes from Existing Policies
- **Authors**: Kimia Hamidieh, Giannis Daras, Antonio Torralba
- **Affiliation**: not stated (inferred — Hamidieh, Daras, Torralba are at MIT CSAIL) (tentative)
- **Venue**: arXiv preprint (2609.30226, cs.LG), announced in the Fri 25 Sep window
- **Key Innovations**: Foundation-model post-training RL must be re-run from scratch whenever the reward changes or rewards are combined. **PoEM** predicts the RL outcome for a **new reward function from policies already post-trained on other rewards**, without running RL: if the new reward is a linear combination of existing ones, the new log-policy is shown to be a linear combination of the existing log-policies — and even when rewards aren't linearly connected, RL log-policies often span an approximately low-rank subspace across rewards. Weighting coefficients are estimated from reward/policy outputs on samples only.
- **Results**: Validated across synthetic and real rewards in both text and image modalities — approximates target RL policies without additional RL training.
- **Significance**: "Dry-run reward design before paying for training" — a planning-ahead primitive for iterating reward functions (alignment, correctness, game objectives) without burning retraining budget.
- **Link**: https://arxiv.org/abs/2609.30226

### 7.7 Auditability Is Not One Property: Rule Overlap, Behavioural Agreement, and Composition in RL
- **Authors**: Liu Hung Ming
- **Affiliation**: not stated (tentative)
- **Venue**: arXiv preprint (2609.28581, cs.AI/cs.LG), announced in the Fri 25 Sep window
- **Key Innovations**: Can independently trained opaque RL policies be represented *and composed* through **auditable discrete behavioral rules**? Defines auditability as six separately testable predicates — **trace integrity, lossless coding, rule coverage, behavioral agreement, composition quality, value-model reliability** — using a shared frozen symbolizer, passive rule extraction, append-only hash-bound ledger, exact environment replay, and offline confidence-ranked arbitration with blind-spot fallback.
- **Results**: Puts strict limits on the description layer: **rule-set overlap does not imply behavioral agreement** (policies sharing symbolic rules can act near-chance on fresh states); a conflict-domain apparent fusion failure traces to an **induction/deployment argmax mismatch** fixable by deployment-consistent re-induction; a fitted-Q general-policy-improvement diagnostic fails in both environments. Contributes an **evidence-bounded audit protocol**, not universal interpretability.
- **Significance**: The negative-result honesty game-AI governance needs: auditable rule descriptions of policies don't automatically compose into new skills — with a protocol for *checking* each auditability claim separately.
- **Link**: https://arxiv.org/abs/2609.28581

---

## Runner-ups Worth a Look (grep-verified unclaimed)

- **2609.29000** Learning from Mixed-Quality Deployment Experience for Robot Manipulation (PACL) — post-deployment robot learning from naturally accumulated mixed-quality rollouts (no human correction, no active exploration): predictive chunk-level critic with future-latent prediction converts chunk Q-values into discrete quality conditions guiding a diffusion actor; on simulated + real manipulation consistently improves the pretrained policy over IL/offline-RL baselines — deployment-experience learning for embodied game controllers. https://arxiv.org/abs/2609.29000
- **2609.29020** Outcome-Sensitive Motion Search for Impact-Aware Dexterous Catching — formalizes **interventional outcome sensitivity** and an outcome-sensitive window (OSW) to explain why a privileged RL teacher under-delivers demonstrations (teacher failures limit coverage; tiny pre-contact variation flips impact/grasp); learns a task-conditioned manifold of successful OSW motions with geodesic search to repair failures; the resulting IL policy *outperforms the privileged teacher* in catch success + impact mitigation — demo curation as a first-class RL-adjacent problem. https://arxiv.org/abs/2609.29020
- **2609.30258** Temporal Gradient Inversion for Private Trajectory Reconstruction in Embodied RL (TRACE) — amortized temporal gradient-inversion attack autoregressively reconstructing private observation-action trajectories from per-step policy gradients (exploits cross-time correlation via a conditional mutual-information bound + closed-form action recovery from policy-head structure); 18.8 dB PSNR with near-perfect action recovery, orders of magnitude faster than optimization attacks — the "distributed multi-agent RL leaks your play" result that sequence-aware privacy mechanisms must fix. https://arxiv.org/abs/2609.30258

## Summary Statistics

| Category | Papers Count |
|----------|-------------|
| Game RL, Multi-Agent Learning & Game Theory | 6 |
| Game AI Bots, LLM Agents & Human-Behavior / NPC Simulation | 4 |
| Game Foundation Models, World Models & Game Agents | 7 |
| PCG, 3D-World Generation & Automated Game Design | 0 (vacancy — second consecutive window) |
| Game Benchmarks & Evaluation Suites | 2 |
| Industry Game AI, Real-Time Inference & Deployment Economics | 0 (vacancy — industry story cross-referenced to siblings) |
| Related RL Techniques | 7 |
| **Total featured papers** | **26** (+3 runner-ups) |

## Cross-references (covered by sibling digests 09-25, not re-featured)

- 2609.29837 — PUBG Ally: KRAFTON live-service conversational embodied teammate (+25.1pp net recommend) — [arxiv-ai-search 09-25 §5.4](../2026-09-25/arxiv-ai-search.md)
- 2609.30019 — Multiplayer Colonel Blotto PPAD-hardness with player-specific values — [arxiv-ai-search 09-25 §5.1](../2026-09-25/arxiv-ai-search.md)
- 2609.29615 — Three-player Auction Bridge pre-game iterative dominance — [arxiv-ai-search 09-25 §5.2](../2026-09-25/arxiv-ai-search.md)
- 2609.30177 — Search-Aware RL for Roblox query understanding (NDCG@20 +8.9) — [arxiv-ai-search 09-25 §1.5](../2026-09-25/arxiv-ai-search.md)
- 2609.30036 — Anchored Planning: frozen world models plan better than goal-image scoring — [arxiv-ai-search 09-25 §6.2](../2026-09-25/arxiv-ai-search.md)
- 2609.28625 — RLVR landscapes benign under spin-glass theory — [arxiv-ai-search 09-25 §6.1](../2026-09-25/arxiv-ai-search.md)
- 2609.29171 — RWM: planning in representation geometry (no rollouts/search) — [arxiv-daily 09-25](../2026-09-25/arxiv-daily.md)
- 2609.28963 — GRAFT: trajectory-graph step-level advantages for agentic RL — [arxiv-daily 09-25 §2.2](../2026-09-25/arxiv-daily.md)
- 2609.29283 — PixelJev: Jev-style visual choice model — [arxiv-daily 09-25 §8.1](../2026-09-25/arxiv-daily.md)
- 2609.30199 — ExplorationBench: verifiable Alien-Worlds exploration sandboxes — [arxiv-paper-check 09-25](../2026-09-25/arxiv-paper-check.md)

## Key Themes

1. **World-model design targets the *planning interface*, not factual fidelity.** AD-WM (2609.30264) is the sharpest statement — factual prediction error and whole-bank action ranking don't follow closed-loop success; what matters is **action discriminability** under counterfactual selection (3.7%→52% hard-start OGBench-Cube). WROP (2609.28654) adds the cognitive axis: object permanence can be *trained in* as a first-class property, not hoped for. DeltaWAM (2609.28811) and Navigation-WM history caching (2609.29555) attack the efficiency floor — delta-only prediction and reusable-history attention — that interactive deployment demands.

2. **Agent-capability engineering turns into adversarial/self-referential loops.** AdvRole (2609.28609) makes the scenario pool a co-evolved adversary (performance-gap reward); Self-Play Pretraining (2609.30063) makes data generation itself a generator-vs-learner RL game; SkillPivot (2609.29154) localizes skill fixes to deviation points instead of rewriting whole strategies. The through-line: the *training curriculum* is becoming a learned artifact.

3. **Rationality and temptation become measurable agent properties.** The marshmallow pair (2609.29509/29508) delivers survival curves, hazard models, and a κ=0.83 failure-rationale taxonomy over 84–200k trajectories; MI-SARSA (2609.28737) derives reaction-time predictions from information-cost policy compression. Multi-agent behavior is being studied with the time-resolved statistics of demography, not pass/fail accuracy.

4. **Debate/deliberation value = disagreement preservation.** Multi-Agent Debate trading (2609.29701) shows reasoning-quality gains (d≈2.0) with zero economic-transfer, while a divergence-preservation intervention pays (Sharpe +0.14) — sycophantic convergence is the central failure. EPLA (2609.29366) supplies the formal coordination glue (guarded typed actions + epistemic lottery gossip) for multi-agent LLM systems.

5. **Efficiency & honesty in RL post-training.** PSP (2609.29051) moves privileged info from loss to sampler (+61% SWE-bench resolved); RLVR-for-small-search-agents (2609.28765) proves reward *shape* is the lever below 1B; uncertainty-gated exploration (2609.28838) redistributes exploration to prevent task collapse; PoEM (2609.30226) predicts RL outcomes to avoid re-training. Each is a "stop paying for what you don't need" result for game-agent training pipelines.

6. **Dedup discipline note:** all 29 curated IDs (featured 2609.28609–2609.30264 range) were grep-verified 0 hits in `wiki/` at write time and sit inside the Fri-25 window (≥ 2609.28475); the game marquees claimed by today's siblings (PUBG Ally, Blotto, Auction Bridge, Roblox search RL, Anchored Planning, RWM, GRAFT, PixelJev, ExplorationBench) are cross-referenced, and the three IDs the ai-search remainder map explicitly parked — 2609.30063, 2609.30264, 2609.28547 — are **claimed here** as features, not duplicated.