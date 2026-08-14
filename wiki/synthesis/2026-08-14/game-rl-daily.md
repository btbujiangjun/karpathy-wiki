---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-08-14)"
type: synthesis
created: 2026-08-14
updated: 2026-08-14
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, world-models, pcg, benchmarks, self-play, multi-agent-rl, ai-native-games, open-ended, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-08-14)

> Curated papers on Game RL, Game AI Bots, Game Foundation Models, PCG, Benchmarks, Industry Game AI, and related techniques.
>
> **Coverage note**: The **Fri Aug 14, 2026 announced window** (Thu Aug 13 submission wave, IDs ~2608.12308–2608.13560), harvested from the arXiv API date-range queries (`submittedDate:[202608130000 TO 202608140000]`) for cs.AI, cs.LG, cs.CL, cs.GT, cs.MA, cs.CV, cs.HC, cs.RO — **339 unique papers** fused and filtered. **16 papers total**, every one **grep-verified absent** from the entire wiki (0 hits in index/log/synthesis/papers/**). Zero overlap with the same-day [[2026-08-14/arxiv-daily]] (29 papers), [[2026-08-14/arxiv-ai-search]] (20 papers), [[2026-08-14/arxiv-paper-check]] (19 papers) and all prior digests — the game/world-model items those digests claimed (AlayaWorld 2608.13492, Do-LLMs-Beat-Nash 2608.12547, TsuGO 2608.13221, Error-Aware Reverse Auction 2608.12719, Objective-Is-The-Bottleneck 2608.12959, Diagnosing JEPA World Models 2608.12939, Entropy-Augmented 2608.12534, DIVE 2608.12486, 2608.12921, 2608.13043, 2608.13096, 2608.13120) are intentionally **not** duplicated here. This window's game-specific yield centers on **world models**: an Alaya-Lab endless-world generator (a sibling of the AlayaWorld tech report claimed by same-day arxiv-daily), a Kuaishou/HKU agent-player world-model benchmark, and a StarCraft II memory-enhanced LLM agent.

---

## 1. Game RL — Reinforcement Learning in Games

### 1.1 Decentralized Multi-Player Q-Learning in Episodic Markov Decision Processes with Information Asymmetry
- **Authors**: Larissa Xu; King Bi; William Chang
- **Affiliation**: not identified
- **Venue**: arXiv:2608.12753 (Aug 13, 2026), cs.LG
- **Abstract**: Decentralized multi-player RL in episodic tabular MDPs under three forms of information asymmetry: (A) unobserved actions with common rewards, (B) observed actions with independent rewards, and (C) unobserved actions with independent rewards. Players cannot communicate during learning but may agree on a protocol a priori. For A and B, `mQ-learning` and `mQ-learning-intervals` achieve $\tilde{O}(\sqrt{H^4 S A_{joint} T})$ regret; for C, `mEXC` and `mEXC-Bellman` two-phase explore-then-commit algorithms achieve $\tilde{O}(H (S A_{joint})^{1/3} T^{2/3})$. Against the centralized joint-action benchmark, decentralized learning under information asymmetry matches single-agent Q-learning rates up to log factors.
- **Key Innovation**: A near-tight regret characterization showing information asymmetry costs little in episodic MDPs — a theoretical foundation for decentralized game agents that must coordinate without a shared observation of each other's actions (e.g. team-game bots, hidden-action RTS coordination).
- **Link**: https://arxiv.org/abs/2608.12753

### 1.2 Revisiting Overestimation Bias Problem of Q-learning: Settling Large Discrete Action Space via Action Intersection
- **Authors**: Pu Li; Tao Tan; Hong Xie; Xiaoyu Shi; Mingsheng Shang
- **Affiliation**: not identified (academic, inferred)
- **Venue**: arXiv:2608.12912 (Aug 13, 2026), cs.LG
- **Abstract**: Studies the overestimation bias of Q-learning under large action spaces. The coupling paradigm (optimal action and its Q-value estimated with the same Q-function) always carries positive bias under randomness; the decoupling paradigm (two independent Q-functions) always carries negative bias. **Action intersection** — two Q-functions share a fraction of trajectory data, updated via coupling on shared samples and decoupling on unshared ones — yields semi-decoupling with a large, finely-adjustable bias range (under-estimate to over-estimate by tuning the sharing fraction).
- **Key Innovation**: A simple, theoretically-grounded dial for the bias of Q-learning with large action spaces — directly applicable to game agents with combinatorially large action heads (card games, build orders, MOBA item/ability spaces).
- **Link**: https://arxiv.org/abs/2608.12912

### 1.3 OGR-MARL: Option-Guided Residual Multi-Agent Reinforcement Learning for Heterogeneous USV Cooperative Pursuit in Constrained Port Waterways
- **Authors**: Mao Jiayang; Wang Lanfeng; Peng Zhao-Han
- **Affiliation**: not identified (academic, inferred)
- **Venue**: arXiv:2608.12995 (Aug 13, 2026), cs.MA / cs.AI
- **Abstract**: OGR-MARL is a MARL-agnostic framework for heterogeneous cooperative pursuit: it integrates shared evader belief, role-conditioned option targets, adaptive rule penalties, and **residual policy learning** — agents learn corrective actions on top of rule-guided behaviors instead of exploring from scratch. Instantiated on MADDPG/MATD3/MAPPO/MASAC; the OGR-MASAC variant reaches a **75.0% capture rate** in a constrained port-waterway scenario, with zero-shot transfer to a QGIS/AIS-informed map.
- **Key Innovation**: Option-guided residual learning lets MARL start from rule priors — a pattern directly portable to game NPC teams learning corrections over scripted/behavior-tree strategies.
- **Link**: https://arxiv.org/abs/2608.12995

---

## 2. Game AI Bot — LLM Agents in Games

### 2.1 LLMs Are Not Good Strategists, Yet Memory-Enhanced Agency Boosts Reasoning
- **Authors**: Yi Wu; Zhimin Hu
- **Affiliation**: not identified (extends the ICLR 2025 workshop paper "LLMs Aren't Good Strategists, Yet Can Accumulate Episodes for Improved Planning")
- **Venue**: arXiv:2608.12626 (Aug 13, 2026), cs.MA / cs.CL
- **Abstract**: Strategic reasoning in LLMs within long-horizon environments is limited by inconsistent subgoals — finite attention resources prevent strategic coherence over thousands of steps, causing **strategic drift**. Introduces **EpicStar**, which lets the agent "learn memory as policy": a bank of successful past episodes acts as a heuristic alongside a working memory tracking short-term environmental changes. A dynamic gating mechanism decides at inference whether to execute a retrieved action directly or perform new reasoning via contextual fusion of retrieved episodes and working memory. Evaluated in **StarCraft II** against diverse opponent styles: significantly higher win rates than baselines while consuming an **order of magnitude fewer tokens**, robust across difficulty levels and opponent strategies.
- **Key Innovation**: Structured cross-episode memory (episodic bank + working memory + dynamic gate) as the decisive factor for long-horizon strategic execution — the first evidence that *what an LLM game agent remembers*, not raw reasoning power, is the binding constraint in RTS play (extends the [[2026-08-10/game-rl-daily]] MEMO memory-augmented self-play thread).
- **Link**: https://arxiv.org/abs/2608.12626

---

## 3. Game Foundation Models / World Models

### 3.1 Alaya-EVOKE: From Linear-Scaling Supervision to Endless World
- **Authors**: Yuanyang Yin; Gongxuan Wang; Yifan Zhan; Chuanhao Li; Kaipeng Zhang; Feng Zhao
- **Affiliation**: **Alaya Lab** (Shanda Games; correspondence kaipeng.zhang@shanda.com) with Feng Zhao (USTC) — the same team as the AlayaWorld technical report (2608.13492, claimed by same-day [[2026-08-14/arxiv-daily]]; earlier [[2026-08-02/game-rl-daily]])
- **Venue**: arXiv:2608.13546 (Aug 13, 2026), cs.CV
- **Abstract**: Interactive world models must support persistent memory, responsive interaction, and long-horizon generation — conflicting demands. **Evoke** externalizes persistent world state into a camera-indexed world state bank (only view-relevant info retrieved, denoiser context stays bounded) and redesigns the teacher for long-horizon supervision via sparse attention (chunk-wise grouping + retrieval of selected distant frames + linear-attention global state → **linear** memory/compute growth). A 30-second distribution-matching objective under self-forced rollouts transfers long-horizon capability and drift resistance to a **three-step student with no classifier-free guidance**. On a single H200 at 384×640, each 1.5 s chunk generates in 2.11 s; SOTA on WBench, competitive on VBench-Long / VBench-2.0.
- **Key Innovation**: The first interactive world model with **externalized world-state memory + linear-scaling long-horizon supervision** — explicitly built for "open-ended, continuously evolving" game-like worlds, and the companion paper to AlayaWorld's playable game-world claim.
- **Link**: https://arxiv.org/abs/2608.13546

### 3.2 A Unifying Perspective on Causal World Models: From Observations to Representations to Structure
- **Authors**: Avinash Kori; Fabrizio Russo
- **Affiliation**: not identified
- **Venue**: arXiv:2608.13456 (Aug 13, 2026), cs.CV / cs.AI
- **Abstract**: Studies world models from a causal perspective across abstraction levels (perceptual observations → conceptual representation of environment dynamics). Argues useful WMs must go beyond generative capability: they should capture entity properties, entity-to-entity interactions, and entity-to-environment interactions. Provides a formal definition of Causal WMs (CWMs) grounded in their supported tasks, connecting to causal representation learning, object-centric learning, causal discovery, structural causal models, and model-based decision-making; relates CWMs to identifiability literature (when components are recoverable from data, up to which equivalence).
- **Key Innovation**: A formal unification of world models with the causal-representation literature — a definitional scaffold for game world models that must support counterfactual reasoning and causal credit assignment (complements the [[2026-08-13/game-rl-daily]] driving-WM counterfactual-gap critique).
- **Link**: https://arxiv.org/abs/2608.13456

### 3.3 S2-HWM: Sparse Event-Structured Hierarchical World Model for Long-Horizon Surgical Robot Manipulation
- **Authors**: Shuzhe Zhang; Xin Zhu; Yinling Qian; Qiong Wang
- **Affiliation**: not identified
- **Venue**: arXiv:2608.13103 (Aug 13, 2026), cs.RO
- **Abstract**: Long-horizon manipulation suffers sparse rewards while meaningful interaction changes occur at irregular intervals. **S2-HWM** learns sparse event evidence from primitive latent trajectories to coordinate an event-level manager and a primitive-step worker. Learned event evidence forms variable-duration segments for an Event Transition Model (ETM) predicting next-boundary state, segment duration, and accumulated reward — chaining these provides a variable-duration continuation beyond the primitive imagination horizon. On SurRoL PegTransfer: **98.7% success**, +22.7 pp over the flat GAS DreamerV3 baseline.
- **Key Innovation**: Sparse, learned event boundaries as the scheduling abstraction for hierarchical world-model imagination — transferable to long-horizon game tasks where milestone events (capture, objective completion) occur at irregular intervals.
- **Link**: https://arxiv.org/abs/2608.13103

### 3.4 DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation
- **Authors**: DreamX Team (Rui Chen; Xiangxiang Chu; Geng Li; Jifan Li; Qingfeng Shi; Datao Tang; Jing Tang; Jun Wang; Pengfei Zhang)
- **Affiliation**: not stated
- **Venue**: arXiv:2608.13489 (Aug 13, 2026), cs.CV / cs.RO
- **Abstract**: An action-conditioned video world model: given an observed frame, language instruction, and prescribed action sequence (end-effector poses + gripper states), predicts future observations. Injects per-arm SE(3) transformations into attention via **PRoPE-style geometric encoding** (preserving arm identity and rigid-motion structure), adds a depth branch for scene geometry, and uses SAM3 masks with a frozen V-JEPA teacher to keep manipulated objects consistent through grasps. Distills the multi-step generator into a few-step student. **First place on Track 1, second on Track 2 of the WorldArena 2.0 Challenge.**
- **Key Innovation**: Geometric action conditioning (per-entity SE(3) pose encoding in attention) as the mechanism for *faithful* action-conditioned rollouts — a design transferable to game world models needing object-consistent responses to precise controller actions.
- **Link**: https://arxiv.org/abs/2608.13489

---

## 4. PCG — Procedural Content Generation

> **No new PCG papers in this window.** Ongoing threads unchanged: WorldClaw agentic 3D open-world generation ([[2026-08-08/game-rl-daily]]), Play2Code/PlaytestArena GUI-agent playtesting ([[2026-08-11/game-rl-daily]]), AutoBG board-game design assistant ([[2026-08-02/game-rl-daily]]).

---

## 5. Game Benchmarks

### 5.1 PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives
- **Authors**: Kaixin Ding; Xi Chen; Minghong Cai; Zhiyuan Xu; Yiyang Wang; Yuxiang Lu; Junyi Li; Shuyang Chen; Yuan Gao; Xin Tao; Pengfei Wan; Hengshuang Zhao
- **Affiliation**: University of Hong Kong (Kaixin Ding — PhD student of Hengshuang Zhao; Zhao) + Kuaishou Kling Team (Xin Tao, Pengfei Wan), inferred from author affiliations
- **Venue**: arXiv:2608.13552 (Aug 13, 2026), cs.CV (distinct from the robot world-model paper "PlayWorld: Learning Robot World Models from Autonomous Play", 2603.09030)
- **Abstract**: Fixed action-conditioned evaluation is unsuitable for comparing interactive world models because the action sequence achieving the same objective varies between models. PlayWorld instead uses **multi-modal Agent Players that interact with world models toward specified long-horizon objectives** — e.g. turn 360° to check environment consistency, or walk into water to check ripple realism. Provides **171 scenarios**, each with a specified objective, evaluating four core dimensions: geometry consistency, interaction fidelity, out-of-sight evolution, and insight evolution, plus basic video quality/controllability metrics. Across nine state-of-the-art world models, current models remain unreliable on long-horizon interactive objectives, especially spatial consistency and persistent state evolution. Code/data: https://github.com/kxding/PlayWorld.
- **Key Innovation**: The first objective-driven, agent-player evaluation paradigm for interactive world models — the benchmark bridge between "looks consistent" and "sustains a player's goal over time", directly targeting game-world-model quality.
- **Link**: https://arxiv.org/abs/2608.13552

### 5.2 H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models
- **Authors**: Dingyi Rong; Yue Shi; Chaofan Ma; Jiezhang Cao; Zongrui Wang; Zeyu Zhang; Yao Mu; Guangtao Zhai; Ning Liu
- **Affiliation**: SJTU (Guangtao Zhai, inferred)
- **Venue**: arXiv:2608.13049 (Aug 13, 2026), cs.CV / cs.RO
- **Abstract**: Evaluates whether video world models can convert egocentric human manipulation demonstrations into robot-centric videos (cross-embodiment transfer for scalable robot data). Each instance contains a human demo, target embodiment constraints, and source-grounded annotations (task goals, action events, functional contacts, object responses). Five evaluation dimensions: goal-state completion, action-event completion, functional-contact transfer, embodiment correctness, general video quality. Benchmarking **11 video generation models** across 6 manipulation families and 2 robot embodiments shows leading models still fail at embodiment consistency, functional interaction, and task execution.
- **Key Innovation**: A systematic diagnostic for cross-embodiment transfer in world models — relevant to game foundation models that must port content/behaviors across character morphologies.
- **Link**: https://arxiv.org/abs/2608.13049

### 5.3 HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments
- **Authors**: Quan-Dung Pham; Anh Dao; The-Anh Nguyen; Minh Nguyen-Dinh; Phuong Nam Dang; Tri Pham; Hung Tran; Bach Dao; Tuyen P. Le; Truong Nguyen; Quan Nguyen
- **Affiliation**: not identified (academic, inferred)
- **Venue**: arXiv:2608.12860 (Aug 13, 2026), cs.RO
- **Abstract**: VLN for humanoids poses challenges wheeled benchmarks miss: bipedal physical constraints, morphology variance, and egocentric camera dynamics. Built on **NVIDIA Isaac Sim**, supporting 4 humanoid robots (Unitree G1/H1, Internal-A/B, 10–12 lower-body DoF, 1.17–1.80 m) via a hierarchical RL locomotion policy + PD/MPC trackers; compatible with NaVILA, DualVLN, StreamVLN, JanusVLN. 933 collision-aware reference episodes with fine-grained + three stylistic instruction variants. JanusVLN leads (43.55% SR, 48.38 nDTW); a 20-episode sim-to-real pilot correlates r=0.935 with real robot error.
- **Key Innovation**: Physics-grounded, multi-embodiment VLN benchmark — a template for embodiment-robust evaluation of humanoid/NPC navigation stacks.
- **Link**: https://arxiv.org/abs/2608.12860

---

## 6. Industry Game AI

> **No standalone studio-authored submissions in this window** — the industry signal is in two papers covered above by their labs: **Alaya Lab / Shanda Games** (Alaya-EVOKE, section 3.1 — endless interactive world model, sibling of the AlayaWorld technical report claimed by same-day [[2026-08-14/arxiv-daily]]) and **Kuaishou Kling Team + HKU** (PlayWorld, section 5.1 — the agent-player benchmark comes out of Kling's world-model program, [[2026-08-14/arxiv-ai-search]]'s world-model-benchmark thread: iWorld-Bench).

---

## 7. Related Techniques — Open-Ended Learning, Multi-Agent RL, Credit Assignment

### 7.1 Beyond Outcome Rewards: Step-Level Self-Distilled Policy Optimization for Deep Search Agents
- **Authors**: Haoze Wu; Chuqiao Kuang; Tianyi Zhuang; Xiaoguang Li
- **Affiliation**: not identified
- **Venue**: arXiv:2608.12764 (Aug 13, 2026), cs.AI / cs.LG
- **Abstract**: Deep search agents span dozens of steps but standard RL gives one outcome reward per trajectory — too sparse for credit assignment. On-policy self-distillation's teacher has privileged information (correct answer) that differs systematically from the student's exploration-based reasoning. **SSPO** resolves the tension with (1) **Evidence Anchors** — concise step-level web-extracted evidence snippets as privileged info that reveals key reasoning steps but not the answer path — and (2) converting teacher–student disagreement into **step-level advantage weights within GRPO, applied only to incorrect trajectories**, decoupling *what* to update (outcome reward direction) from *how much* (teacher-modulated magnitude). On Qwen3-8B, SSPO consistently beats GRPO on BrowseComp/GAIA/FRAMES, matching GRPO trained with 2× gradient steps at ~5% per-step overhead.
- **Key Innovation**: Step-level, evidence-grounded advantage weighting for sparse long-horizon RL — the same credit-assignment pathology (one outcome for a many-step trajectory) that plagues game RL with sparse objective rewards (extends the [[2026-08-12/game-rl-daily]] ADRS-style dense-reward threads).
- **Link**: https://arxiv.org/abs/2608.12764

### 7.2 Temporal GRPO: Beyond Trajectory-Level Credit in Vision-Language-Action Reinforcement Learning
- **Authors**: Yao Zhou; Hang Gao; Fengge Wu; Changwen Zheng; Wenwen Qiang
- **Affiliation**: not identified (academic, inferred)
- **Venue**: arXiv:2608.13026 (Aug 13, 2026), cs.RO
- **Abstract**: Identifies **trajectory-level credit aliasing** in GRPO-based VLA post-training: a rollout that completes several valid stages but fails later penalizes the actions behind earlier progress. Temporal GRPO constructs detectable task stages, aligns each rollout with stage-specific action intervals, and compares only rollouts that entered the same stage, applying stage advantages to their corresponding intervals in a single update. On RoboTwin 2.0 it improves task success and sample efficiency; controlled updates on LIBERO-Long preserve shared prerequisite stages and concentrate improvement at the first diverging stage.
- **Key Innovation**: Stage-aligned advantage computation as a fix for outcome-aliasing in GRPO — directly relevant to game-agent RL where one late failure drowns earlier good segments.
- **Link**: https://arxiv.org/abs/2608.13026

### 7.3 Online Inference for Quantile Temporal Difference Learning in Distributional Reinforcement Learning
- **Authors**: Zijie Cheng; Yang Peng; Zhihua Zhang
- **Affiliation**: Peking University (Zhihua Zhang, inferred)
- **Venue**: arXiv:2608.12973 (Aug 13, 2026), cs.LG
- **Abstract**: Establishes functional central limit theorems for synchronous and asynchronous **QTD** (quantile temporal difference) learning under a generative model — averaged iterates converge weakly to a rescaled Brownian motion — then builds online statistical inference via random scaling: an asymptotically pivotal statistic computed along the QTD path **without storing the trajectory**, cutting memory substantially.
- **Key Innovation**: The first online inference machinery for distributional RL (the family behind distributional game agents' value uncertainty) — enabling statistically-tested QTD value estimates in resource-constrained agents.
- **Link**: https://arxiv.org/abs/2608.12973

### 7.4 ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models
- **Authors**: Gehan Zheng; Matthew Johnson-Roberson; Weiming Zhi
- **Affiliation**: Carnegie Mellon University (Johnson-Roberson, inferred)
- **Venue**: arXiv:2608.13438 (Aug 13, 2026), cs.CV / cs.RO / cs.AI
- **Abstract**: Contact-rich manipulation failures are usually detected only after commitment. **ContactGuard** is a pre-contact execution monitor for chunked visuomotor policies: it predicts a planned action chunk's short-horizon consequence in latent visual space with a latent world model trained from unlabelled trajectories (compact multi-view embeddings, avoiding pixel-level prediction), then a lightweight failure probe (trained on a small labelled pre-contact set) aborts before contact. Transfers to live robot without modifying the underlying policy.
- **Key Innovation**: Latent-space world-model rollouts as a cheap, policy-agnostic execution monitor — the "world model as pre-flight check" pattern usable for game-bot safety gates.
- **Link**: https://arxiv.org/abs/2608.13438

### 7.5 Agent Behavioral Contracts II: Certifying Compositional Reliability Without Assuming Independence
- **Authors**: Varun Pratap Bhardwaj; Garima Singh; Arun Pratap Bhardwaj
- **Affiliation**: not identified
- **Venue**: arXiv:2608.12895 (Aug 13, 2026), cs.MA / cs.AI
- **Abstract**: Compositional reliability bounds for multi-agent systems multiply component reliabilities — a step licensed by a conditional-independence assumption "routinely stated and rarely tested". This paper tests it: **two instances of one model in a two-agent handoff co-fail on 90.0% of missions on which either fails** (log OR 6.66; phi 0.916), in a preregistered 18,000-mission evaluation scored by deterministic code with no LLM judge. Positive dependence inflates joint failure above the independence product, so redundancy is over-credited exactly when components share a model. Proves a bootstrap bound on a fitted dependence model loses coverage as n grows; gives a finite-sample certificate (linear program over a Bonferroni–Clopper–Pearson box) that is sound, sharp, and monotone in the moment family, plus an anytime-valid certificate (type-I error 0.0471 under optional stopping).
- **Key Innovation**: Shows redundancy-with-identical-models is systematically over-rated in multi-agent systems and provides assumption-free reliability certificates — the failure-mode math for shared-model LLM agent teams (NPC swarms, agent societies).
- **Link**: https://arxiv.org/abs/2608.12895

---

## Summary Statistics

- **Total new papers**: 16 fully listed (verified NEW via grep against the entire wiki), across 5 of 7 categories
- **Fresh window (submitted Aug 13, 2026, announced Fri Aug 14)**: 16 papers — decentralized multi-player Q-learning (asymmetric info), action-intersection Q-learning bias, OGR-MARL pursuit, EpicStar StarCraft II LLM agent, Alaya-EVOKE endless world, causal-world-model unification, S2-HWM surgical world model, DreamX-Phi action-conditioned video WM, PlayWorld agent-player benchmark, H2R-Bench cross-embodiment, HumanoidVLN, SSPO step-level credit, Temporal GRPO, online QTD inference, ContactGuard latent monitor, Agent Behavioral Contracts II
- **PCG**: no new submissions this window (threads unchanged)
- **Key venues**: arXiv preprints; WorldArena 2.0 Challenge (DreamX-Phi, competition result)
- **Notable trends**:
  - **World models take the window**: Alaya-EVOKE (externalized world-state memory, linear-scaling long-horizon supervision) and PlayWorld (agent-player evaluation of long-horizon objectives) attack the same two walls — persistence/consistency and fair interactive evaluation — from generation and measurement sides, respectively; both are game-domain adjacent, and PlayWorld's authors span HKU + Kuaishou Kling (industry tie-in)
  - **Game AI Bot memory thesis strengthens**: EpicStar (StarCraft II) shows cross-episode memory, not reasoning power, is the binding constraint for long-horizon strategic coherence — consistent with the [[2026-08-10/game-rl-daily]] MEMO findings that memory-augmented agents win with orders-of-magnitude fewer resources
  - **Sparse credit assignment is the shared bottleneck**: SSPO (Evidence Anchors + step-level GRPO advantages) and Temporal GRPO (stage-aligned advantages) independently fix "one outcome per trajectory" aliasing in search agents and VLA policies — the same pathology in game RL with sparse objectives; the Q-learning bias and online-QTD papers add theory for large-action / distributional game agents
  - **Multi-agent reliability gets statistical teeth**: Agent Behavioral Contracts II quantifies why shared-model redundancy is over-credited (90.0% co-failure), with finite-sample certificates — a governance result for LLM-agent game systems

## Cross-References

- [[2026-08-14/arxiv-daily]] — same-day breadth digest; includes AlayaWorld v1.1 (2608.13492), Objective-Is-The-Bottleneck (2608.12959), Diagnosing JEPA World Models (2608.12939) — zero overlap with this digest
- [[2026-08-14/arxiv-ai-search]] — same-day digest; includes Do-LLMs-Beat-Nash (2608.12547), TsuGO (2608.13221), Error-Aware Reverse Auction (2608.12719), iWorld-Bench (2605.03941, world-model benchmark thread) — zero overlap
- [[2026-08-14/arxiv-paper-check]] — same-day digest; 19 cs.AI/cs.IR papers — zero overlap
- [[2026-08-13/game-rl-daily]] — prior digest (successor-feature MARL safety, similarity-signal cooperation, IF:CARGO, Pharos Night, driving-WM counterfactual gap, Steam GenAI perception; covered up to ~2608.12307)
- [[2026-08-12/game-rl-daily]] — prior digest (Hierarchical Games, Not a Monolith, LeWorldModel reproduction, DSLE Dark Souls)
- [[2026-08-02/game-rl-daily]] — AlayaWorld original technical report coverage (the lab behind today's Alaya-EVOKE)
