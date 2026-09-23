---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-09-23)"
type: synthesis
created: 2026-09-23
updated: 2026-09-23
sources: [arxiv.org]
tags: [game-rl, game-ai, llm-agents, foundation-models, world-models, pcg, benchmarks, industry-game-ai, self-play, marl, game-theory, model-based-rl, world-action-models, kv-quantization, simulation-reliability, human-behavior-simulation, social-sim, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-09-23)

> **Methodology note**: **Wed 23 Sep 2026** mailing (processes Tue 22 Sep submissions). Fresh window = **IDs 2609.25006–2609.26796**, sitting entirely above the 09-22 sibling max (2609.24554). Live `/list/{cat}/new` parses for **cs.AI / cs.LG / cs.GT / cs.MA / cs.NE / cs.RO / cs.HC / cs.CV / cs.CL** → **965 unique listed IDs** → subtracted the full wiki-coverage set (6,331-ID known set, which already includes today's sibling digests) → **857 unclaimed** → title + abstract keyword sweep → **23 targets fetched at arXiv abs-page depth** → **20 curated + 3 runner-ups**. Every featured/runner-up ID was **grep-verified 0 hits in `wiki/` and 0 hits in today's sibling-claimed sets** (60 IDs claimed by 09-23 arxiv-daily / arxiv-paper-check / arxiv-ai-search / conference-digest, all excluded by construction).
>
> **Continuity / already-covered by the 09-23 siblings (cross-referenced, not re-featured):** the fresh window's *pure-game marquee* was taken hours ago by the same-day digests — **GameDirector** 2609.25652 (decoupling rule-based gameplay logic from generative video rendering, player-configurable game world models) → both [arxiv-daily 09-23](../2026-09-23/arxiv-daily.md) §7.1 and [arxiv-ai-search 09-23](../2026-09-23/arxiv-ai-search.md) §6.2; **CoDeR** 2609.26458 (code-plans + diffusion-renders open-ended world modeling) → [arxiv-ai-search 09-23](../2026-09-23/arxiv-ai-search.md) §6.1; **TriWorldBench** 2609.25220 (tri-view consistency benchmark for embodied world models) and **Dual-Frontier** 2609.26107 (when to trust a world-model-guided decision) and **PersonaWeaver** 2609.25485 (controllable diversity in procedural character generation) → [arxiv-daily 09-23](../2026-09-23/arxiv-daily.md) §7; **Auction Bridge CFR** 2609.26265 and **prophet inequalities under p-mean welfare** 2609.25424 → [arxiv-ai-search 09-23](../2026-09-23/arxiv-ai-search.md) §6. This edition therefore mines the **unclaimed game-relevant remainder** — which this window shapes as a **MARL-adaptation + game-theory-robustness + world-action-model + human-behavior/social-simulation + deployment-economics** digest.
>
> **Window character**: this Wed-23 window is game-light at the level of *titles* (the classic game marquees were all claimed by siblings); the unclaimed remainder generalizes the game-AI levers instead — observation-level MARL adaptation, Byzantine robustness in cooperative learning, bandit/game-theory guarantees, world-action unification, and the "simulation reliability" wave that governs LLM-agent and NPC societies.

---

## 1. Game RL, Multi-Agent Learning & Game Theory

### 1.1 MATES: Learning Multi-Agent Interactions by Transforming Observations for Frozen Single-Agent Policies
- **Authors**: Elie Abboud, Oren Gal
- **Affiliation**: not stated (inferred — Oren Gal is at Technion, robotics/MARL group) (tentative)
- **Venue**: arXiv preprint (2609.26010, cs.MA / cs.LG), announced in the Wed 23 Sep window
- **Key Innovations**: MARL normally trains decentralized policies from scratch, forcing agents to learn individual competence and coordination *simultaneously*. **MATES (Multi-Agent Observation Transformation for Existing Single-Agent Policies)** flips this: for tasks whose multi-agent observations preserve the solo-task information while exposing separately identifiable neighbor information, a **small input-side adapter** is learned to map the multi-agent observation into the format expected by a **frozen single-agent policy** — the pretrained policy's internals, objectives and update procedure stay untouched.
- **Results**: Evaluated on lifelong pathfinding, navigation and cooperative discovery in discrete and continuous settings, MATES optimizes only **3.5–7.3% as many parameters as full-policy training** while consistently beating MARL-from-scratch, approaching full-fine-tuning performance, staying competitive with demonstration-based baselines, and retaining strong performance at **team sizes never seen in training**.
- **Significance**: "Learn coordination without losing competence" — a transfer recipe for game squads (add a teammate to a trained AI, don't retrain the whole agent) and for live-service NPC casts built on frozen base policies.
- **Link**: https://arxiv.org/abs/2609.26010

### 1.2 Fully Byzantine-Resilient Multi-Agent Reinforcement Learning (FRAC-MARL)
- **Authors**: Haejoon Lee, Dimitra Panagou
- **Affiliation**: not stated (inferred — Panagou is at University of Michigan, distributed robotics/control) (tentative)
- **Venue**: arXiv preprint (2609.25701, cs.LG / cs.MA / eess.SY), announced in the Wed 23 Sep window
- **Key Innovations**: Distributed actor-critic MARL is vulnerable to Byzantine agents on the communication layer — existing methods only guarantee convergence to a *neighborhood* of the attack-free limit point. **FRAC-MARL** makes every agent leverage **redundancy in two-hop messages** to identify and drop unreliable messages, achieving *fully* resilient convergence: under linear-parameterized value/team-reward functions and Byzantine edge attacks, agent parameters converge **almost surely to the same limit points as the attack-free case** over time-varying communication graphs. Introduces a novel, polynomial-time-verifiable topological condition for convergence plus a systematic network-construction method.
- **Results**: Proven convergence and demonstrated on cooperative multi-robot formation control; the two-hop-redundancy scheme removes the residual performance degradation of prior resilient-MARL methods.
- **Significance**: Cooperative game/robot teams need trust guarantees, not just attack tolerance — a strong robustness result for large-scale opponent/teammate training pipelines where communication (e.g., between distributed training workers) can be adversarial.
- **Link**: https://arxiv.org/abs/2609.25701

### 1.3 Improved Multiplayer Bandit Algorithms for Bernoulli Rewards
- **Authors**: Khang Nguyen, Ricardo Parada, William Chang
- **Affiliation**: not stated (inferred — academic bandits/learning-theory group) (tentative)
- **Venue**: arXiv preprint (2609.26213, cs.AI / cs.LG), announced in the Wed 23 Sep window
- **Key Innovations**: Multiplayer multi-armed bandits with **information asymmetry** (players differ in which arms they see or which rewards they observe) model competitive/cooperative exploration in games. The paper replaces the Hoeffding-style confidence intervals of prior work with **KL-divergence-based bounds**, producing strictly tighter regret guarantees across three asymmetric information structures (action-asymmetry, reward-asymmetry, both). Proposes **mKL-UCB**, **mKL-UCB-Intervals** and **mKL-DSEE**.
- **Results**: The improvement factor over Hoeffding variants is **at least 2 by Pinsker's inequality** and far larger when reward means are near 0 or 1; for reward-asymmetry, the paper proves two arms' KL-intervals separate after a *deterministic* number of samples, and that **M independent players accelerate elimination** further.
- **Significance**: Tight bandit guarantees for multiplayer exploration — the exploration-economics backbone for matchmaking, item/level A/B testing across player pools, and opponent-model-free exploration in game environments.
- **Link**: https://arxiv.org/abs/2609.26213

### 1.4 Achieving Robust Performance Using Minimal Communication in Resource Allocation Games
- **Authors**: Brandon Collins, Colton Hill, Philip N. Brown
- **Affiliation**: Colorado (Philip N. Brown is at University of Colorado Colorado Springs, network/game theory) (tentative)
- **Venue**: arXiv preprint (2609.26670, cs.GT / cs.MA / math.OC), announced in the Wed 23 Sep window
- **Key Innovations**: Resource-allocation games model team coordination in **denied-communication environments**; the open question is how much communication loss degrades emergent coordination. Quantifying with the **Price of Anarchy**, the paper's main result is a computationally efficient algorithm that finds a **minimal communication network preserving the full-information performance guarantee**. It also supplies algorithms computing Nash and strict-Nash equilibria in the full-information setting, sufficient conditions for strict-Nash existence, characterizes strict Nash equilibria across all networks, and shows each full-information strict-Nash equilibrium has a necessary-and-sufficient inducing link set.
- **Results**: Provably minimal communication for equal performance guarantee; execution-time experiments and several example games (incl. congestion-style allocation games) accompany the theory.
- **Significance**: "Which comms links actually matter for team performance?" — a formal handle for bandwidth-constrained game-AI teams (esports comms, radio-limited multi-robot teams, fleet coordination) where full broadcast is impossible.
- **Link**: https://arxiv.org/abs/2609.26670

### 1.5 Strategic Disclosure of Action Space in Principal-Agent Contracts (WINE 2026)
- **Authors**: Xiaotie Deng, Ningyuan Li
- **Affiliation**: not stated (inferred — Deng is at Peking University, game theory/mechanism design) (tentative)
- **Venue**: WINE 2026 (accepted; full version on arXiv), announced in the Wed 23 Sep window
- **Key Innovations**: In principal-agent contracting, the agent may **strategically disclose only part of her action space** to shape the principal's perception before a revenue-optimal contract is designed — a game-theoretic information-design twist with direct analogs in game balance and agent capability disclosure. Two variants by cost verifiability: with unverifiable costs the agent extracts the entire first-best surplus (principal gets zero); with verifiable costs the agent's optimal disclosure is characterized for binary-outcome and linear-contract settings, reducing to a two-variable convex program.
- **Results**: The agent secures at least a **1/e fraction of first-best surplus**, a 1/e welfare guarantee under optimal disclosure; the principal's revenue can be arbitrarily small vs first-best, but if the max/min expected-reward ratio among non-null base actions is ≤ L, revenue is Θ(1/log L) of first-best. The 1/e agent guarantee extends to general outcome spaces.
- **Significance**: Formalizes "capability hiding" as a strategic move — relevant to agent-marketplaces, skill-gated game AI, and any system where an agent's disclosed capabilities set the contract/reward others write for it.
- **Link**: https://arxiv.org/abs/2609.25410

---

## 2. Game AI Bots, LLM Agents & Human-Behavior / NPC Simulation

### 2.1 ReliMap: Understanding Reliability in LLM-Based Human Behavior Simulation
- **Authors**: Pei Wang, Lei Wang, Yuanzi Li, Xu Chen
- **Affiliation**: not stated (inferred — Xu Chen is at Renmin University of China, LLM-agent simulation) (tentative)
- **Venue**: arXiv preprint (2609.25066, cs.CL / cs.AI), announced in the Wed 23 Sep window
- **Key Innovations**: LLMs are increasingly used to simulate human survey responses and behavioral reactions (player panels, NPC populations), yet end-to-end scores hide *where* reliability fails. **ReliMap** decomposes simulation into three structured layers and evaluates reliability at **individual level (R1) and population level (R2)** across three config dimensions (model capacity, profile completeness, population coverage) — 4 simulation tasks × 11 LLMs.
- **Results**: All models show substantial **distributional bias without profile conditioning**; profile conditioning helps but with diminishing returns; larger models benefit more and attribute **informativeness beats attribute quantity**; critically, **R1 gains do not reliably transfer to R2** (individual and population reliability can move in opposite directions); more coverage reduces variance but not systematic bias, with R2 plateauing at ~50–100 individuals.
- **Significance**: The reliability map every game studio needs before seeding towns with LLM NPCs or simulating player-population reactions — "simulate the population, don't simulate the average."
- **Link**: https://arxiv.org/abs/2609.25066

### 2.2 Do Synthetic Personas Predict Real Audience Response? A Sim-to-Real Study Where a No-Persona Baseline Beats Personality Engineered Personas
- **Authors**: Alexandre Cristovão Maiorano
- **Affiliation**: independent researcher (author-stated context) (tentative)
- **Venue**: arXiv preprint (2609.25010, cs.AI / cs.CL / econ), announced in the Wed 23 Sep window
- **Key Innovations**: Marketers (and game-market researchers) use profile-conditioned LLM "synthetic personas" to predict audience reactions to copy before shipping. This is the sim-to-real validity study such workflows rarely run: it uses the **Upworthy Research Archive** (thousands of headline A/B tests on shared real traffic with measured click-through) as held-out ground truth, comparing a demographically grounded 10-persona panel against a **no-persona zero-shot baseline** that simply asks how likely a typical reader is to click.
- **Results**: The **no-persona baseline beats the persona panel** on the real click-through-validated prediction task — personality engineering machinery did not improve out-of-sample prediction and in some settings hurt it; the paper analyzes when persona conditioning helps vs hurts (task granularity, base rate, persona-homogeneity artifacts).
- **Significance**: A controlled dose of skepticism for the "LLM-as-user-panel" paradigm in game telemetry/design research — cheap no-persona baselines should be the null hypothesis before persona pipelines get funded.
- **Link**: https://arxiv.org/abs/2609.25010

### 2.3 The Limits of Simulated Societies: How Post-Training and Survey Fine-Tuning Erase Cross-Cultural Variance
- **Authors**: Rojin Ziaei
- **Affiliation**: not stated (inferred — computational-social-science / LLM-simulation group) (tentative)
- **Venue**: arXiv preprint (2609.25760, cs.AI / cs.CL), announced in the Wed 23 Sep window
- **Key Innovations**: Simulating diverse human populations requires reproducing the *spread* of opinion, not just the mean — most evaluations score point accuracy and miss this. Introduces a diagnostic measuring **point accuracy alongside dispersion retention** (predicted-vs-human standard deviation ratio) on **10,000 respondent–question pairs from the World Values Survey** (12 countries / 6 continents), evaluating 11 zero-shot models and 5 post-trained variants (SFT / DPO / GRPO on WVS data).
- **Results**: Identifies a failure mode — **consensus staleness / variance collapse**: post-training and survey fine-tuning improve point accuracy while *erasing cross-cultural and within-group variance*; models converge toward a single flattened "global survey respondent" and under-predict the tails of real opinion distributions that matter most in player/NPC population design.
- **Significance**: Directly relevant to LLM-NPC sociology and behavioral-simulation: post-trained models look more accurate per respondent while becoming *less* usable as heterogeneous populations — population-level variance is a first-class objective, not a byproduct.
- **Link**: https://arxiv.org/abs/2609.25760

---

## 3. Game Foundation Models, World Models & Game Agents

### 3.1 PatchWAM: An Action Is Worth One Patch — Unified World-Action Modeling
- **Authors**: Tianheng Wang, Zhou Xie, Heng Jia, Jianhua Xu, Tong Zhang, Kaicheng Yu
- **Affiliation**: not stated (inferred — world-action-model / VLA group; Kaicheng Yu is NTU-affiliated, historical) (tentative)
- **Venue**: arXiv preprint (2609.25961, cs.RO / cs.LG / cs.AI), announced in the Wed 23 Sep window
- **Key Innovations**: Do visual prediction and action generation require separate computational pathways in generative visual models? **PatchWAM** answers "no": it expresses continuous actions through a fixed **Action-as-Patch** mapping so actions become just another patch in the visual sequence — a single model predicts both the robot's next action and the scene's appearance **in the same generative process**, with no dedicated action head and no separate action expert.
- **Results**: With subsampled training windows, PatchWAM beats a matched dual-expert control baseline; full-data with augmented demonstrations reaches **91.8% success on LIBERO-Plus and 96.12% on RoboTwin 2.0**. The core thesis: "capability need not be added where it can be inherited — the constraint on extending a generative backbone is the interface a new signal is written in."
- **Significance**: A clean unification argument for game world models and agents — one generative backbone consumes observation + action together, the architecture behind "game foundation models that both imagine and play."
- **Link**: https://arxiv.org/abs/2609.25961

### 3.2 Skytopia: Monocular Drone Navigation with Action-Conditioned Latent World Models
- **Authors**: Yuhang Zhang, Rangya Zhang, Yujing Shang, Zhuoyuan Yu, Weiying Wang, Steven Yang, Qingsong Yan, Chao Yan, Mir Feroskhan
- **Affiliation**: not stated (inferred — Mir Feroskhan is at NTU Singapore, aerial robotics) (tentative)
- **Venue**: arXiv preprint (2609.26007, cs.RO / cs.AI), announced in the Wed 23 Sep window
- **Key Innovations**: A strong representation-first argument for world models in control: **what a policy needs from a world model is not the prediction but the representation required to produce it.** In flight, the executed action explains almost all change between monocular observations — prediction collapses into reprojecting a static scene under a known displacement. Skytopia therefore trains **action-conditioned latent world models** used purely as representation extractors, decoupling "world-model as generative predictor" from "world-model as encoder for policy decisions."
- **Results**: Monocular drone navigation to a goal in unseen environments; the latent-representation world model yields effective goal-reaching where pixel-reconstruction world models (executed predictively) squander capacity on low-information recency.
- **Significance**: Supports the game-AI trend of **latent/planning-relevant world models** (cf. ForeDrive 3.3 below, Dual-Frontier cross-referenced) — the representation, not the render, is the leverage for control agents.
- **Link**: https://arxiv.org/abs/2609.26007

### 3.3 ForeDrive: Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model
- **Authors**: Sinuo Wang, Zichong Gu, Yuhan Huang, Wenxin Wen, Xun Yang, Yiqing Zhang, Xingyu Zhang, Ningyu Che, Jie Ling, Qiankun Yu, Wei Liu, Jing Xu, Xin Gao, et al.
- **Affiliation**: not stated (inferred — academy+industry AD cluster; Wei Liu historically Tencent/WeChat AI) (tentative)
- **Venue**: arXiv preprint (2609.26299, cs.CV / cs.RO), announced in the Wed 23 Sep window
- **Key Innovations**: Latent world models are usually optimized for *predictability*, but predictability ≠ useful-for-planning. ForeDrive learns a **planning-relevant latent representation** and couples it *asymmetrically* to a Diffusion-Transformer planner: the planner consumes multi-horizon latent futures from a JEPA-style world model, planning gradients update the shared online encoder, while stop-gradient routing keeps the future-latent predictor training on forecast objective only.
- **Results**: On driving benchmarks, planning-relevant latents beat both pixel-reconstruction world models and off-the-shelf latent predictors as planner conditioning; the asymmetric routing prevents the JEPA-predictor from being corrupted by control gradients.
- **Significance**: "Represent for the task, not for the renderer" — the same planning-vs-reconstruction split game agents and world-model companies are converging on (matching this window's CoDeR/GameDirector separation of dynamics from rendering competence).
- **Link**: https://arxiv.org/abs/2609.26299

---

## 4. Procedural Content Generation, 3D-World Generation & Automated Game Design

### 4.1 Fysiverse-3D-Vision: Generating Executable 3D Worlds from Images through Unified Spatial Reasoning
- **Authors**: Dingkang Yang, Yizhou Liu, Wendong Cheng, Zizhi Chen, Shunli Wang, Yang Liu, Hongsheng Li, Lihua Zhang
- **Affiliation**: Fysics AI Technical Report (stated); authors span Fudan/CUHK-linked groups (tentative)
- **Venue**: arXiv preprint / industry technical report (2609.25741, cs.CV / cs.AI), announced in the Wed 23 Sep window
- **Key Innovations**: 3D generative models synthesize visually plausible scenes but couple spatial layout to specific asset generators, so scene-level **metric geometry, object semantics and executable physics** stay disconnected. **Fysiverse-3D-Vision** is a unified vision-language-geometry framework for generative 3D scene reconstruction and *executable* asset construction from a single image — jointly modeling semantics, metric geometry and scene-level spatial relations so the generated world is usable for interactive editing, physical simulation and embodied applications.
- **Results**: Technical-report-level evidence on single-image → executable 3D scene generation, unlocking layout-correct, physics-ready worlds (the same assets that then drive agents/robots).
- **Significance**: "Worlds you can run, not just render" — the image-to-executable-world pipeline is exactly the content-generation substrate procedural / generative game design needs; sits alongside this window's ϕ-RIE (4.2) on the physicals-first generation axis.
- **Link**: https://arxiv.org/abs/2609.25741

### 4.2 ϕ-RIE: From Photorealistic Reconstruction to Interactive Environments
- **Authors**: Runyi Yang, Deheng Zhang, Xiaoye Wang, Kanzhi Wu, Lei Sun, Ajad Chhatkuli, Kunyu Peng, Luc Van Gool, Danda Pani Paudel
- **Affiliation**: ETH Zürich + IIT-affiliated cluster (L. Van Gool, D. P. Paudel, K. Peng, A. Chhatkuli) (tentative)
- **Venue**: arXiv preprint (2609.26795, cs.RO / cs.CV), announced in the Wed 23 Sep window
- **Key Innovations**: 3D Gaussian Splatting reconstructions are photoreal but not interactive — objects can't move independently, make contact or reveal occluded surroundings. **ϕ-RIE** (Photorealistic Reconstruction → Interactive Environments) is a Gaussian-native pipeline converting *selected objects* into **movable simulator assets while preserving the background reconstruction**, using key observations on object/background appearance entanglement, hidden geometry and occluded content.
- **Results**: Reconstructed scenes become interactive sim environments where objects separate, move, and occlude/reveal correctly — without full re-meshing or bullet-style downgrade of the reconstruction.
- **Significance**: The missing glue between "movie-like capture" and "physics-ready game environment" — studios can turn real-world scans into playable/simulatable spaces, and game world models get pre-meshed interactive assets from monocular/3DGS capture.
- **Link**: https://arxiv.org/abs/2609.26795

---

## 5. Game Benchmarks & Evaluation Suites

### 5.1 Behavior Is Not Enough: A Mechanism-Based Evaluation of Social Norm Emergence in LLM Societies
- **Authors**: Rasika Muralidharan, Haewoon Kwak, Jisun An
- **Affiliation**: Singapore Management University (SMU, Solv[AI] Lab) (inferred from authors) (tentative)
- **Venue**: arXiv preprint (2609.26481, cs.GT / cs.AI / cs.CE), under review for AAAI 2027 Special Track: AI Alignment; announced in the Wed 23 Sep window
- **Key Innovations**: **Social norms cannot be identified from behavior alone** — the same cooperative equilibrium can reflect shared expectations, strategic incentives, or mere imitation. This is a direct critique of game-AI benchmark practice that reads "behavioral convergence" as "norm emergence." The framework measures agents' **reported empirical + normative expectations *in addition to* behavior**, and isolates two collective mechanisms from norm-formation theory: **social learning through interaction** and **social selection through network-based group formation**, via controlled ablations.
- **Results**: Eliciting expectations changes the measured "norms"; interaction-based learning and network-based selection produce distinct signatures that pure behavior conflates — benchmark conclusions about norm emergence depend on which mechanism the test actually exercises.
- **Significance**: An evaluation-validity milestone for LLM-agent societies (NPC societies, multiplayer social sims): measurement must separate the *mechanism* (expectations, incentives, imitation) from the *outcome* (behavioral convergence).
- **Link**: https://arxiv.org/abs/2609.26481

### 5.2 COA-Bench: Adversarial Course-of-Action Generation via Game-Theoretic Self-Play
- **Authors**: Natan Vidra, Alina Kapanova, Arun Kanhai, Spurthi Setty
- **Affiliation**: not stated (inferred — defense/planning AI group; DAI 2026 Industry Track submission, synthetic offline scenarios only) (tentative)
- **Venue**: arXiv preprint (2609.26059, cs.AI / cs.GT / cs.SE), DAI 2026 Industry Track submission; announced in the Wed 23 Sep window
- **Key Innovations**: Course-of-action (COA) generation framed as a **distributed game**: propose structured candidate actions, evaluate against an **adversarial response**, and surface options coherent under changing conditions. COA-Bench is a small offline benchmark + reproducibility artifact comparing COA-generation policies **through self-play**, representing COAs as typed action chains with conditional branches scored by a synthetic adversary — no classified data.
- **Results**: Reproducible self-play evaluation of COA matching vs COA generation (distinct DecisionFunction sub-problems); provides the scoring scaffold for comparing planning policies under adversarial counter-action.
- **Significance**: A public, synthetic benchmark for "plan against an adversary and re-plan" — the benchmark pattern for military-adjacent game AI, strategy bots and automated wargaming research; self-play as the evaluation surface.
- **Link**: https://arxiv.org/abs/2609.26059

### 5.3 DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving (CoRL 2026)
- **Authors**: Ziyang Leng, Sicheng Mo, Seth Z. Zhao, Haoyuan Cai, Yu Zeng, Rowan McAllister, Bolei Zhou
- **Affiliation**: UCLA / NADLab cluster + Waymo-adjacent (Rowan McAllister) (tentative)
- **Venue**: CoRL 2026 (accepted); arXiv abstract page notes project page
- **Key Innovations**: Simulation for closed-loop evaluation must preserve **policy-relevant features**, not merely photo-realism. DreamStream is a generative closed-loop simulator using a **simulator-grounded autoregressive video model** distilled (via traffic-layout guidance) from a large pretrained video model: appearance can vary while the scene features the driving policy relies on are preserved, closing the sim-to-real gap that corrupts otherwise faithful end-to-end evaluation.
- **Results**: Policy-oriented fidelity evaluation of end-to-end policies in closed-loop, avoiding the classic "photo-real but policy-blind" failure of generative simulators.
- **Significance**: "Evaluate the policy, not the pixels" — the same principle as game-bot evaluation benches where render-fidelity falsely substitutes for decision-relevant fidelity (parallel to 5.1's mechanism-vs-outcome critique).
- **Link**: https://arxiv.org/abs/2609.26792

---

## 6. Industry Game AI, Real-Time Inference & Deployment Economics

### 6.1 QuantWM: Temporally Consistent 2-Bit KV-Cache Quantization for World Models and Video Generation
- **Authors**: Jiaqi Zhao, Xiaobin Hu, Bo Yin, Junpeng Jiang, Miao Zhang, Shuicheng Yan
- **Affiliation**: not stated (inferred — SKLOIS/CAS + Immerge-Affiliated cluster, Shuicheng Yan) (tentative)
- **Venue**: arXiv preprint (2609.26425, cs.AI / cs.CV / cs.LG), announced in the Wed 23 Sep window
- **Key Innovations**: KV-cache memory is *the* deployment bottleneck for video generation and world models; existing 2-bit KV quantization is near-lossless on VBench yet produces **severe temporal flickering**. The paper traces the cause: Key quantization has smaller reconstruction error than Value but much larger output degradation because small Key perturbations shift attention logits (QK^T) and change which temporal-spatial tokens Queries select. **QuantWM**: a training-free, strictly-causal 2-bit KV-quantization framework with (a) **quantization-sensitivity-aware clustering (QSAC)** — Hassan historical Query sensitivity + residual ranges to pick INT2-friendly Key centroids — and (b) **principal-subspace attention compensation (PSAC)** — low-rank correction of remaining Key error along the dominant Query subspace.
- **Results**: On Causal-Forcing, LingBot-World-v2, HY-World 1.5, Matrix-Game-2 and Longcat-Video: significantly improved visual quality and temporal consistency, beating existing methods on image+video metrics with up to **6.20× KV-cache memory compression** and limited overhead.
- **Significance**: Deployment economics for game world models/trailers on consumer GPUs — 2-bit KV with temporal consistency is what actually ships interactive world-model inference on-device, directly extending the wiki's RimJobs/RimJobs-style on-device-inference line (09-20 digest).
- **Link**: https://arxiv.org/abs/2609.26425

---

## 7. Related RL Techniques (Offline RL, Curiosity, Credit Assignment, Model-Based)

### 7.1 PACT: From Credit Assignment to Critic Alignment
- **Authors**: Jiayan Fu, Hang Xu, Yong Zhang, Zhaokai Luo, Yao Hu, Dongyan Zhao, Mu Chuan
- **Affiliation**: not stated (inferred — Huawei Noah's Ark/PDL-linked authors + Peking University, Dongyan Zhao) (tentative)
- **Venue**: arXiv preprint (2609.26355, cs.LG / cs.CL), announced in the Wed 23 Sep window
- **Key Innovations**: Token-level credit in LLM post-training RL lacked a mathematical definition. The paper proves three regularity conditions (**Completeness, Prefix Consistency, Neutrality**) **uniquely determine** token-level credit, and uses the characterization to unify existing algorithms: an ideal OPD teacher acts as an *implicit critic* (expected gradient proportional to token-credit gradient); response-level **RLOO** matches the expected contribution of token-level credit despite coarser granularity; approximate credit sparsity holds under bounded outcome rewards; intermediate critic errors in GAE can rival the credit itself. This motivates **Policy-Aligned Critic Training (PACT)**: Actor-then-Critic update order with importance-sampling correction aligning the critic with the *updated* policy.
- **Results**: **72.87% average accuracy across four agentic-math benchmarks** (+8.80 over GRPO, +13.16 over PPO) and **67.4% pass@1 on SWE-bench Verified** (+2.4/+2.0/+3.8 over PPO/GRPO/SAO).
- **Significance**: The credit-assignment math underneath game-policy training in LLM agents — a principled critic-consistency fix that transfers to any token-level RL loop, including self-play and reward-shaping pipelines.
- **Link**: https://arxiv.org/abs/2609.26355

### 7.2 A Decentralized Partially-Observable Team Decision Methodology with Delayed Information Sharing
- **Authors**: Xiaoxing Ren, Thomas Parisini, Andreas A. Malikopoulos
- **Affiliation**: University of Delaware (Malikopoulos) + Imperial College (Parisini) (tentative)
- **Venue**: arXiv preprint (2609.26783, cs.LG / cs.MA / math.OC), announced in the Wed 23 Sep window
- **Key Innovations**: Team decision-making under **partial observability + unknown dynamics + delayed common information** is the realistic setting of cooperative game teams. Combining **team-theoretic equivalence** with **low-rank latent-dynamics models**, each member learns an approximate low-rank MDP from local private information + delayed shared info and runs least-squares value iteration — **fully decentralized** (no coordinator, no centralized training).
- **Results**: Each member recovers the corresponding component of an approximate team-optimal policy; the paper establishes **finite-sample performance guarantees and a sample-complexity bound** under sparse/delayed communication.
- **Significance**: "Delayed-common-information team play" — a formal plug for cooperative game/robot teams where players can't see everything and comms lag, complementing the minimal-communication result in 1.4.
- **Link**: https://arxiv.org/abs/2609.26783

### 7.3 Deep RL on Item-Compatibility Graphs for One-Dimensional Bin Packing
- **Authors**: M. Aslı Aydın
- **Affiliation**: not stated (inferred — operations-research/RL single-authored) (tentative)
- **Venue**: arXiv preprint (2609.25397, cs.LG / cs.AI), announced in the Wed 23 Sep window
- **Key Innovations**: A size-agnostic end-to-end **graph RL** solver for 1D bin packing: the packing process is an MDP over an **item-compatibility graph** where each action merges two partial bins that fit together; a GNN actor-critic extracts relational features, trained via RL and decoded by stochastic beam search, **generalizing zero-shot to instances of any size**.
- **Results**: Zero-shot on the full **BPPLIB** benchmark: lowers the constructive-heuristic mean optimality gap 2.66% → 2.31% (largest gains on structured instances); beats recent learned methods on most of the nine families, is far more stable across distributions, and outperforms a solver-based SOTA learned method on the hardest family *using no solver at all* (a grouping genetic algorithm stays ahead overall).
- **Significance**: Relational RL for NP-hard packing/matching — the same compatibility-graph abstraction applies to inventory/bag/queue optimization in games and to item-trism in content systems.
- **Link**: https://arxiv.org/abs/2609.25397

---

## Runner-ups Worth a Look (grep-verified unclaimed)

- **2609.25432** Tipping Points in LLM-Based Multi-Agent Systems: Stance on Climate Change Action — endows agent-based models with LLM-communicating agents to study social tipping points under small perturbations (LLM agent societies as climate-opinion simulators). https://arxiv.org/abs/2609.25432
- **2609.26056** CricRAG — retrieval-augmented VLMs aligned to skill-appropriate benchmarks for personalized cricket coaching (VLM-game application; AAAI-25 knowledgeable-foundational-models workshop). https://arxiv.org/abs/2609.26056
- **2609.25738** OmniFysics-Nano-V2 Technical Report — compact omni-modal model for physical-world perception across vision/audio/speech/language (physical-world understanding for embodied/agentic systems; Fysics AI line). https://arxiv.org/abs/2609.25738

## Summary Statistics

| Category | Papers Count |
|----------|-------------|
| Game RL, Multi-Agent Learning & Game Theory | 5 |
| Game AI Bots, LLM Agents & Human-Behavior / NPC Simulation | 3 |
| Game Foundation Models, World Models & Game Agents | 3 |
| PCG, 3D-World Generation & Automated Game Design | 2 |
| Game Benchmarks & Evaluation Suites | 3 |
| Industry Game AI, Real-Time Inference & Deployment Economics | 1 |
| Related RL Techniques | 3 |
| **Total featured papers** | **20** |

## Cross-references (covered by sibling digests 09-23, not re-featured)

- 2609.25652 — GameDirector: decoupling rule-based gameplay logic from generative rendering, player-configurable game world models — [arxiv-daily 09-23 §7.1](../2026-09-23/arxiv-daily.md) / [arxiv-ai-search 09-23 §6.2](../2026-09-23/arxiv-ai-search.md)
- 2609.26458 — CoDeR: code-plans + diffusion-renders open-ended generative world modeling — [arxiv-ai-search 09-23 §6.1](../2026-09-23/arxiv-ai-search.md)
- 2609.25220 — TriWorldBench: tri-view consistency benchmark for embodied world models — [arxiv-daily 09-23 §7.2](../2026-09-23/arxiv-daily.md)
- 2609.26107 — Dual-Frontier: when can an agent trust its world model (failure attribution) — [arxiv-daily 09-23 §7.3](../2026-09-23/arxiv-daily.md)
- 2609.25485 — PersonaWeaver: controllable diversity beyond archetypes in procedural character generation — [arxiv-daily 09-23 §7.4](../2026-09-23/arxiv-daily.md)
- 2609.26265 — Auction Bridge CFR analysis and 2609.25424 — prophet inequalities under p-mean welfare — [arxiv-ai-search 09-23 §6](../2026-09-23/arxiv-ai-search.md)

## Key Themes

1. **MARL converges on "don't retrain what already works."** MATES (2609.26010) adapts frozen single-agent policies through observation transformation (3.5–7.3% of full-training parameters and still beats from-scratch MARL); FRAC-MARL (2609.25701) guarantees *full* Byzantine resilience by 2-hop-message redundancy. Cooperative game AI increasingly treats competence as an asset to preserve and coordination as a thin adaptor layer on top.

2. **Game theory returns to *guarantees under degraded information.*** Minimal-communication resource-allocation games (2609.26670) compute the smallest network that keeps the full-information Price-of-Anarchy bound; mKL-UCB multiplayer bandits (2609.26213) tighten regret via KL bounds; decentralized team-MDP with delayed info sharing (2609.26783) provides finite-sample convergence. Together: "what's the cheapest information structure that keeps my team near-optimal" is the recurring question.

3. **World-action unification + planning-relevant representations.** PatchWAM (2609.25961) treats actions as patches inside the visual generative process (no action head); Skytopia (2609.26007) and ForeDrive (2609.26299) argue policies need the *representation*, not the *render*, of a world model. This dovetails with the siblings' GameDirector/CoDeR — across the whole 09-23 window the field is decoupling dynamics competence from visualization competence.

4. **The simulation-reliability wave hits NPC/agent societies.** ReliMap (2609.25066), No-Persona-Baseline (2609.25010) and Limits-of-Simulated-Societies (2609.25760) all stress-test whether LLMs can stand in for human populations; Behavior-Is-Not-Enough (2609.26481) shows *why* behavioral benchmarks can't certify norm emergence. For game studios this is the memory of calibration: profile-conditioned NPC populations can look better per-respondent while diverging from the population *distribution* they're meant to model.

5. **Deployment economics for world models keeps closing the loop.** QuantWM (2609.26425) recovers temporal consistency at 2-bit KV (6.20× compression) — interactive world-model inference on consumer hardware moves from "demo" to "ship-able," continuing the industry-AI economics thread of this digest series.

6. **Dedup discipline note:** every featured ID (2609.26010–2609.25410) was grep-verified 0 hits in `wiki/` and 0 hits in the 09-23 sibling-claimed sets; the window's game marquees (GameDirector, CoDeR, PersonaWeaver, Dual-Frontier, TriWorldBench, Auction Bridge CFR, prophet inequalities) are cross-referenced, not duplicated.