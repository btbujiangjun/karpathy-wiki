---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-08-29)"
type: synthesis
created: 2026-08-29
updated: 2026-08-29
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, pcg, game-benchmarks, world-models, self-play, vlm, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-08-29)

Curated survey of fresh papers on reinforcement learning in games, game foundation & world models, procedural content generation, game benchmarks, industry game AI, and related techniques, from the **Fri Aug 28 announcement wave (Thu Aug 27 submissions, IDs ~2608.24xxx–27455)** plus recent proceedings.

> Scope & verification: papers below were **grep-verified absent from `wiki/`** (no ID appears in any existing page, including the 08-28 siblings [arxiv-daily](../2026-08-28/arxiv-daily.md) / [arxiv-ai-search](../2026-08-28/arxiv-ai-search.md), which locked their window at ~2608.27455). Later committed same-week digests re-checked: **Magpie** (`2608.27168`, real-time generative world renderer) and **Nash Loci** (`2608.27300`) were initially identified here but are **excluded above the line because they were independently claimed by the 08-31 [game-rl-daily](../2026-08-31/game-rl-daily.md) and 08-30 [arxiv-ai-search](../2026-08-30/arxiv-ai-search.md) digests** — noted to prevent duplicate IDs. Sections 2 (Game AI Bot — LLM agents) and 1.2 (Game-Specific RL) had **no genuinely-new entries** this wave (saturated by prior digests). Direct arXiv API/web is blocked in this environment; metadata was recovered via alphaXiv + targeted `websearch`. Affiliations marked *(stated)* come from paper front matter; *(inferred)* = deduced from author identities / project pages; otherwise "not stated". **15 papers across 6 sections.**

---

## 1. Game RL — Reinforcement Learning in Games

### 1.1 Self-Play & Parallel RL

| # | Title | Authors | Affiliation | Venue | arXiv | Key Innovation |
|---|-------|---------|-------------|-------|-------|----------------|
| 1 | **Shared Actors Need Not Share Critics: Effects of Value Mismatch in Parallel Reinforcement Learning** | Zhenya Liu, Yang Meng, Zhuokai Zhao, Xuefeng Liu, Yuxin Chen | University of Pennsylvania *(inferred: same group as PATH below; Yuxin Chen is UPenn RL-theory faculty)* | arXiv | [2608.26481](https://arxiv.org/abs/2608.26481) | A single policy trained in parallel across environments (procedural levels, randomized dynamics, curricula) usually shares one critic; when environments assign different returns to the same critic-visible input, value mismatch systematically shifts sampled advantages. Theoretical bandit models prove the effect redistributes updates (reinforcing unhelpful actions, attenuating useful ones). Minimal fix: condition the critic on a *logged environment index*. Multihead conditional critic improves aggregate normalized return by **40.8%** across all 16 Procgen games (600 unseen levels each), with more stable learning in BipedalWalker. |

---

## 3. Game & Interactive-World Foundation Models

| # | Title | Authors | Affiliation | Venue | arXiv | Key Innovation |
|---|-------|---------|-------------|-------|-------|----------------|
| 2 | **SpatialCrafter: Single Image World Modeling with Generative 3D Proxies** | Chuan Fang, Lingteng Qiu, Yixun Liang, Rui Chen, Kunming Luo, Zhaohua Zheng, Tongyuan Bai, Feipeng Tian, Zilong Dong, Zihan Zhou, Ping Tan | HKUST; Tongyi Lab, Alibaba; ManyCore Tech Inc.; Jilin University *(stated)* | SIGGRAPH Asia 2026 | [2608.27073](https://arxiv.org/abs/2608.27073) | Explorable image→scene generation for gaming/VR/robotics. Two-stage framework: a Point-anchored Sparse Structure (PaSS) Flow module predicts a globally aligned, geometrically consistent **3D proxy**, then the video-diffusion-model is re-framed as a *Generative Deferred Refiner* synthesizing high-frequency photorealistic detail on the proxy geometry. Parallel Geometry Injection + Proxy-Aware Corruption training keeps the pretrained generative manifold intact. Releases a first-of-its-kind hybrid dataset of ~115K scenes. Fixes the stochastic hallucination / long-term drift / weak 3D consistency of sparse-conditioning baselines. |
| 3 | **Latent Spatial Memory for Video World Models (Mirage)** | Weijie Wang, Haoyu Zhao, Yifan Yang, Feng Chen, Zeyu Zhang, Yefei He, Zicheng Duan, Donny Y. Chen, Yuqing Yang, Bohan Zhuang | Zhejiang University *(inferred: Bohan Zhuang is ZJU faculty)* | arXiv | [2606.09828](https://arxiv.org/abs/2606.09828) | Explicit point-cloud memory in RGB space is expensive (repeated rendering + VAE encoding) and lossy (round trip through pixel space). Mirage introduces **latent spatial memory**: a persistent 3D cache of scene tokens in the diffusion latent space, built by depth-guided back-projection and queried via direct latent-space warping. Up to **10.57× faster** end-to-end video generation and **55× lower** memory footprint vs explicit-3D baselines; SOTA on WorldScore, strong RealEstate10K reconstruction. |

---

## 4. Procedural Content Generation

| # | Title | Authors | Affiliation | Venue | arXiv | Key Innovation |
|---|-------|---------|-------------|-------|-------|----------------|
| 4 | **4DSynth: Controllable Procedural World Synthesis for Dynamic Embodied Simulation** | Zehao Qi, Haochen Luo, Jia-Wang Bian, Zeyu Ma, Shuyang Sun | NTU; University of Oxford; Princeton University; Google DeepMind *(stated)* | arXiv | [2608.26947](https://arxiv.org/abs/2608.26947) | Turns a natural-language description, a blueprint mask, or a single photograph into an **editable 4D environment** (explicit geometry, animated actors, collision-free trajectories, physics-ready state; OpenUSD export). Multiple scene routes share one geometry-grounded representation so the same pipeline handles animation, camera planning, rendering, and task generation. Validates with **4DSynth-Nav** (~333-task interactive navigation benchmark, fully procedurally generated): two vision-language models fail the majority of tasks across three difficulty tiers and stall early. Procedural controllability makes every failure reproducible and each difficulty axis independently tunable. |
| 5 | **Procedura: Agentic 3D Modeling with Procedural Control** | Youtian Lin, Yikang Yang, Zhanpeng Hu, Mengqi Zhou, Feihu Zhang, Xun Cao, Jiaheng Liu, Yao Yao | Nanjing University *(inferred: Xun Cao, Feihu Zhang, Yao Yao are NJU faculty)* | arXiv | [2608.26238](https://arxiv.org/abs/2608.26238) | "3D shape as code": an LLM agent writes an object as a **procedural assembly** — a parametric program whose named parts are joined by typed, machine-checkable mates. From a text prompt it plans an assembly graph and writes the program part by part, solving each placement from mated frames (not guessing), admitting a part only after compile/mate/connectivity checks; a decoupled vision critic refines it one diagnosed fix at a time. Per-part materials + simulator-validated articulation. Outperforms native 3D generators and all prior 3D-code agents on P3D-Bench and its own hard-surface **MechBench-36**; only method whose output is an editable, part-structured program with the sharpest edges. |

---

## 5. Game Benchmarks & Evaluation

| # | Title | Authors | Affiliation | Venue | arXiv | Key Innovation |
|---|-------|---------|-------------|-------|-------|----------------|
| 6 | **R2M-Bench: Evaluating Revisit Memory via Relative Consistency in Interactive Video World Models** | Qiwen Gu, Bingjie Gao, Rui Chen, Geng Li, Jifan Li, Qishuai Wen, Li Niu, Jing Tang, Xiangxiang Chu, Junqiao Zhao | DreamX Team, Alibaba Group; Tongji University; Shanghai Jiao Tong University *(stated)* | arXiv | [2608.27328](https://arxiv.org/abs/2608.27328) | High first-visit/return similarity can just mean the rollout changed little, so absolute revisit scores conflate memory with rendering stability / failed motion. R2M-Bench compares each revisit pair against two same-rollout controls (gap-matched non-revisit = temporal stability; short-range = short-horizon consistency), producing **MemoryGain (MG)** and the **Normalized Memory Ratio (NMR)**. 300 instances (100 scenes × 3 leave-and-return trajectories) across 7 action-conditioned video world models: NMR↔human Spearman ρ=0.547 (95% CI [0.45,0.63]); NMR's correlation with generated motion is 0.072 vs 0.207 for raw revisit similarity (kills the slow-motion shortcut). **DreamX-World-Memo** tops Overall NMR. |

---

## 6. Industry Game AI

| # | Title | Authors | Affiliation | Venue | arXiv | Key Innovation |
|---|-------|---------|-------------|-------|-------|----------------|
| 7 | **Account Consistency from Gameplay Traces: Same-Player Verification in Counter-Strike 2** | Xuchen Zhang | Not stated (single author) | arXiv | [2608.24893](https://arxiv.org/abs/2608.24893) | Frames CS2 account-integrity review (temporary substitution, rank boosting, high-skill players on lower-ranked accounts) as **same-player verification**: a match replay is encoded as a demo-player behavioral fingerprint (crosshair control, movement-stop-fire coordination, economy/buy, combat/engagement, temporal rhythm), and a model judges whether two observations come from the same real player. ROC-AUC **0.926** (Perfect, 3,570 demos) and **0.956** (Professional, 539 demos). Strongest identity signals are low-level mechanical (aim/crosshair), not single-match outcomes; aggregating K=10 historical demos lifts account-history AUC to **0.982**. |
| 8 | **CPGRec+: A Balance-oriented Framework for Personalized Video Game Recommendations** | Xiping Li, Aier Yang, Jianghong Ma, Kangzhe Liu, Shanshan Feng, Haijun Zhang, Yi Zhao | Harbin Institute of Technology; Wuhan University *(stated, via PDF)* | arXiv | [2604.14586](https://arxiv.org/abs/2604.14586) | GNN game recommenders optimize accuracy over diversity and ignore the uneven significance of player-game interactions (which also fuels GNN over-smoothing). Adds two LLM-informed modules on top of CPGRec: **Preference-informed Edge Reweighting (PER)** assigns signed edge weights to separate player interests from disinterests and measures preference strength, mitigating over-smoothing; **Preference-informed Representation Generation (PRG)** has an LLM reason over global-vs-personal interests to write contextualized player/game descriptions. Superior accuracy **and** diversity vs SOTA on two Steam datasets. |

---

## 7. Related Techniques

### 7.1 World Models for Agents (no reconstruction, no labels)

| # | Title | Authors | Affiliation | Venue | arXiv | Key Innovation |
|---|-------|---------|-------------|-------|-------|----------------|
| 9 | **Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization** | Jiaming Zhou, Qihang Zhang, Gangwei Xu, Cunxin Fan, Yujie Zhao, Ruilin Wang, Yiming Luo, Shuai Yang, Xing Zhu, Yujun Shen, Junwei Liang, Yinghao Xu | Robbyant; HKUST (Guangzhou); HKUST *(stated)* | arXiv | [2608.26103](https://arxiv.org/abs/2608.26103) | Transfers LLM-style in-context learning to robot manipulation by making the task specification a **human video**. Zero-WAM is a causal video-action model that executes unseen tasks by following in-context human-video guidance, no parameter update. An automatic pipeline converts task-sampled robot trajectories into semantically matched human videos to build **HumanGen** (74.2K human-robot ICL pairs across 8.6K tasks); the in-context future chunk prediction (IFP) objective suppresses seen-task shortcuts. On 7 unseen RoboTwin 2.0 tasks: **47.0%** avg success, +29.5 pp over the strongest video-conditioned baseline. |
| 10 | **Predicting Consequences and Reinforcing Navigation Policies with Latent World Models** | Zengmao Wang, Wei Gao, Shuhan Shen | Shanghai Jiao Tong University *(inferred: Shuhan Shen is SJTU faculty)* | arXiv | [2608.26190](https://arxiv.org/abs/2608.26190) | World models for decision-making usually reconstruct future observations/features. This **compatibility-prediction latent world model** instead predicts action-conditioned *latent feature compatibility* — spatial proximity correlates with latent similarity, so action consequences are scored directly in latent space. Counterfactual training on cross-trajectory action sequences teaches which choices lead closer to the goal; the WM then supervises policy learning from **unlabeled video** and further improves the policy via RL conducted *entirely inside the world model* (no action annotations, no extra environment interaction). Outperforms prior world-model and imitation methods on multiple real-world robot navigation datasets. |

### 7.2 Curriculum RL & Offline RL

| # | Title | Authors | Affiliation | Venue | arXiv | Key Innovation |
|---|-------|---------|-------------|-------|-------|----------------|
| 11 | **PATH: Active Curriculum Refinement for Reinforcement Learning** | Zhenya Liu, Yuxin Chen | University of Pennsylvania *(inferred)* | ICML 2026 | [2608.26469](https://arxiv.org/abs/2608.26469) | Environments connected by prerequisite relations (difficulty-increasing edits, parameter increments) form a **directed-acyclic curriculum graph** that is usually only exploited implicitly. PATH performs active learning over the graph: first expands coverage by sampling diverse curriculum paths, then reallocates training toward regions that remain unmastered. Explicitly leveraging the structure yields strong robustness and generalization across diverse environments. |
| 12 | **Simple Actors and Deep Critics for Scalable Reinforcement Learning (LAC)** | Guhyeon Kang, Jaehwi Lee, Minhae Kwon | Not stated | arXiv | [2608.26659](https://arxiv.org/abs/2608.26659) | Since the offline critic is trained once but the actor runs at every deployment decision, capacity is better spent on the critic — but deeper offline critics are known to destabilize. Identifies three failure modes: optimization, bootstrap-noise amplification, value-range drift, each fixed by a residual MLP backbone, n-step bootstrap targets, and categorical cross-entropy loss. **LAC** (light actor, deep critic) matches the strongest diffusion/flow-matching baselines on OGBench at up to **4× lower inference latency**, comparable to one-step distilled policies. |

### 7.3 Distributional RL — Theory

| # | Title | Authors | Affiliation | Venue | arXiv | Key Innovation |
|---|-------|---------|-------------|-------|-------|----------------|
| 13 | **A Finite Sample Analysis for Quantile Temporal Difference Learning in Distributional RL** | Zijie Cheng, Xiang Li, Yang Peng, Zhihua Zhang | Peking University *(inferred: Zhihua Zhang is PKU faculty)* | arXiv | [2608.27313](https://arxiv.org/abs/2608.27313) | First **global finite-sample guarantee** for synchronous quantile TD in tabular distributional RL. Splits stability into two mechanisms: a global comparison argument using order monotonicity of reward CDFs + the W∞ contraction of the distributional Bellman operator (brings any initialization into a local neighborhood), then a linearized QTD mean-field whose Jacobian is a nonsingular **M-matrix** with a positive semigroup enabling variance-sensitive martingale analysis. For stepsizes α_t=c(t+1)^(-a), a∈(1/2,1), the last-iterate fluctuation is Õ(T^(-a/2)/√(1-γ)) with **no polynomial dependence on the number of quantiles** — sharply separating local stochastic fluctuation from global sample complexity. |

### 7.4 Game Theory & Combinatorial Games

| # | Title | Authors | Affiliation | Venue | arXiv | Key Innovation |
|---|-------|---------|-------------|-------|-------|----------------|
| 14 | **Blindfolded pursuit with delays of your choice** | Torben Schürenberg, Maximilian J. Stahlberg | Not stated | arXiv | [2608.27347](https://arxiv.org/abs/2608.27347) | Pursuit-evasion on graphs: one pursuer versus an **invisible** evader, where the pursuer assigns integer travel times (delays) to edges and queries one vertex per time step. With unit travel times this is the hunter-and-rabbit game (evader must move) or a firefighting variant (evader can wait). The power to **choose travel times lets a single pursuer succeed in polynomial time on any graph** — in contrast to unweighted graphs where the required hunter/firefighter count can grow linearly with vertices. If the evader may also start before an unknown earlier time, the pursuer still wins given exponential time. |
| 15 | **Algorithms for Robbins' Problem using Markov Decision Processes** | Léonard Brice, F. Thomas Bruss, Anirban Majumdar, Jean-François Raskin | Université libre de Bruxelles *(inferred: Brice, Bruss & Raskin are ULB-based)* | arXiv | [2608.27419](https://arxiv.org/abs/2608.27419) | Treats the full-information secretary variant: minimize the expected **rank** of the selected candidate — decision after each interview, no recall. Models instances as **infinite-state MDPs**, then builds finite-state abstractions with simple memory structures that suffice for near-optimal strategies (full memory of past values is needed for optimality in general). Provides better approximations than previously known for all n, **5 ≤ n ≤ 100** (exact values were only known through n ≤ 4). |

---

## Key Trends

1. **Gameplay logic and visuals are separating again, but into a system boundary.** Magpie (covered by the 08-31 digest) and this wave's 4DSynth / SpatialCrafter all enforce a clean contract between rule/state ownership and generative appearance — 4DSynth exports editable, physics-ready OpenUSD stages, and "every failure reproducible" is treated as a first-class feature of procedural controllability.

2. **World models are moving out of pixel space.** Mirage stores 3D memory directly in diffusion latent space; navigation world models (LWM) predict latent feature compatibility instead of reconstructing frames. 10.6× speedups and label-free policy supervision are the payoffs, and R2M-Bench shows evaluation is co-evolving (relative calibration vs naive revisit similarity) to keep pace.

3. **Task specification by video is maturing as an ICL recipe.** Zero-WAM converts 74.2K robot trajectories into matched human videos and lets a causal video-action model follow an unseen task purely from in-context video (+29.5 pp over video-conditioned baselines), parallel to latent world models that supervise policies from unlabeled video with in-WM RL.

4. **Capacity and credit get re-allocated deliberately.** LAC moves offline-RL capacity to a deep critic (4× cheaper deployment), Shared Actors fixes value mismatch across parallel environments with a small index-conditioned critic (+40.8% Procgen), and PATH explicitly allocates training effort over curriculum DAGs.

5. **The integrity/identity layer of game AI is industrializing.** CS2 same-player verification turns anti-boosting and account review into a supervised behavioral-fingerprint problem (0.956 ROC-AUC professional), while CPGRec+ pushes balanced (accuracy + diversity) LLM-informed game recommendation — both closer to shipping products than research demos.

6. **The mathematical floor under game AI is tightening in the same wave:** a global finite-sample guarantee for quantile TD, an MDP abstraction for optimal-stopping secretary-type problems with near-optimal memory structures, and a single-pursuer polynomial result for graph pursuit with chosen delays.