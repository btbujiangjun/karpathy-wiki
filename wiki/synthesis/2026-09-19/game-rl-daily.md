---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-09-19)"
type: synthesis
created: 2026-09-19
updated: 2026-09-19
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, world-models, wam, flow-matching, jepa, game-theory, fair-division, vlnce, offline-rl, sim-to-real, autonomous-driving, dexterous-manipulation, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-09-19)

> **Methodology note**: **Sat 19 Sep 2026 has no fresh arXiv mailing** (weekend), so this digest re-mines the **Fri 18 Sep 2026 window** (`Showing new listings for Friday, 18 September 2026`, Thu 17 Sep submissions, IDs **2609.19149–2609.20822**). Of 912 unique in-window IDs across the live-parsed `/list/{cat}/new` pages (**cs.AI / cs.CL / cs.CV / cs.GT / cs.HC / cs.LG / cs.LO / cs.MA / cs.NE / cs.RO**), 551 remain unclaimed after the 09-18 siblings. The same-day siblings — `arxiv-paper-check`, `conference-digest`, `investment-daily`, `tech-report-digest` — ran against the same window and claimed the agentic-RL / AI-application content. This digest mines the **unclaimed game-relevant remainder**: title + abstract keyword sweep → candidates → targeted abstract screening → **18 curated**. Every featured ID was **grep-verified 0 hits in `wiki/`** and sits outside the sibling-claimed 09-18 and 09-19 ID sets.
>
> **Continuity / already-covered (not re-featured):** **Reach or Solve? Attributing Agentic RL Gains with Checkpoint Handoffs** (REACH/SOLVE attribution protocol, 2609.19636) → [arxiv-paper-check 09-19](arxiv-paper-check.md); **UnifiedPlayers** (GRPO three-player planning/execution/evaluation self-play, 2609.20089) → [arxiv-paper-check 09-19](arxiv-paper-check.md); **BATON** (dual-axis agent RL, 2609.19830) and **SoL-Pi** (recursively scaling auto-research harnesses, 2609.20519) → [arxiv-paper-check 09-19](arxiv-paper-check.md). Game/world-model headline items from the 09-18 window (GAVEL 2609.19315, Steering Equilibrium Selection 2609.19820, Astronex-World 2609.20034, Retaliatory Collusion 2609.20548, Score Centering 2609.20807, EPIG-Tree 2609.20004) → [arxiv-ai-search 09-18](../../2026-09-18/arxiv-ai-search.md). **GameWAM** (2608.26200) was already covered on 09-05/09-11 — not re-featured.

---

## 1. Game RL, Multi-Agent Learning & Game Theory

### 1.1 Mutual Evaluation and Supervision without Peers
- **Authors**: Zachary Robertson
- **Affiliation**: single author, not stated (inferred — mechanism-design / information-elicitation theory)
- **Venue**: arXiv preprint (2609.20789, cs.GT / cs.IT), submitted 17 Sep 2026
- **Key Innovations**: Introduces a **single-worker + critic mechanism** ("mutual evaluation") where both worker and critic are modeled as strategic agents. The critic chooses a finite-valued rule inducing an evaluation score over joint report laws, and common payoff is analyzed via regret against the unrestricted critic envelope. Unlike peer-prediction and scoring-rule literature, the **replication-loop mechanism needs no peers**, no ground-truth reference, and no likelihood-ratio estimation to elicit truthful reports.
- **Results**: Constructs implementations producing **unbiased Pearson and Shannon information scores** under this peer-free, ground-truth-free setting; type-agreement payoffs are implemented using same-task replications and new-task samples.
- **Significance**: A mechanism-design result relevant to **self-play and no-peer training loops**: how to reward honest reporting when there is no external judge — the same informational structure game-AI reward-shaping faces when only the environment (not other agents) can supervise performance.
- **Link**: https://arxiv.org/abs/2609.20789

### 1.2 Asymptotic Max-Min Fair Allocation with Random Utilities
- **Authors**: Noam Glazner, Amir Leshem
- **Affiliation**: Israel academic cluster — Bar-Ilan University (Leshem) (inferred)
- **Venue**: arXiv preprint (2609.19319, cs.GT / cs.IT), submitted 16 Sep 2026
- **Key Innovations**: Fair division of **indivisible goods** under **i.i.d. random utilities**. Derives **asymptotic characterizations of the max-min (egalitarian) value** via distributional quantiles in the balanced case K=N and the K=L·N extension.
- **Results**: Proves that for sufficiently **light-tailed distributions the relative efficiency loss of max-min fairness converges to zero** as the market grows — fairness is (asymptotically) free. Welfare gap between the max-min allocation and the sum-optimal allocation vanishes in large random instances.
- **Significance**: A theoretical comfort result for **economy/resource-allocation systems in games**: egalitarian fairness can be achieved without sacrificing total welfare at scale, under light-tailed item valuations.
- **Link**: https://arxiv.org/abs/2609.19319

---

## 2. Game AI Bots, LLM Agents & Game-Style Benchmarks

### 2.1 GPT-6-Astra in a Navigation Workflow: Behavioral Analysis in Zero-Shot Vision-and-Language Navigation in Continuous Environments
- **Authors**: Guangzhao Dai, Qi Wu, Bin Zhu
- **Affiliation**: Singapore Management University (Dai, Zhu) + AIML, University of Adelaide (Wu) — confirmed via web
- **Venue**: arXiv preprint (2609.20116, cs.RO), submitted 17 Sep 2026
- **Key Innovations**: A **zero-shot VLN-CE behavioral study** of the frontier model GPT-6-Astra inside a common observation–decision–execution workflow, using direct model API calls — **no agent harness, no navigation-specific fine-tuning**. Context management and action control (retained progress records, selected observations, execution feedback) are part of the evaluated system.
- **Results**: On **50 of 100 R2R-CE val-unseen episodes** used by Open-Nav: **52.0% success, 48.9 SPL, 70.8 nDTW**. Analysis shows recorded responses link landmarks and earlier actions to instructions via observations and supplied history — the model builds a coarse episodic map rather than reactive next-step guessing.
- **Significance**: Direct read on how a frontier LLM behaves as an **in-game navigator bot** with zero adaptation — instructive baseline for game agents that must follow natural-language route instructions in continuous 3D worlds.
- **Link**: https://arxiv.org/abs/2609.20116

### 2.2 Navi-Agent: Unlocalized Monocular Navigation Agent
- **Authors**: Wenyuan Xie, Mengyang Hong, Yongzhong Wang, Yanbiao Ji, Yijin Zhou, Shaokai Wu, Shalayiding Sirejiding, Huayi Zhou, Yi-Chao Chen, Ma Ling, Yue Ding, Hongtao Lu
- **Affiliation**: Shanghai Jiao Tong University cluster (Lu, Chen) (inferred)
- **Venue**: arXiv preprint (2609.20388, cs.RO / cs.CV)
- **Key Innovations**: A **coordinate-free, geometry-unconstrained zero-shot VLN-CE agent**. Instead of depth maps / globally consistent coordinates, Navi-Agent builds a **navigation topology**: nodes = visual places, edges = motion transitions, constructed from visual observations and executed motion histories. This supports observation-based approximate self-localization, **task-progress verification**, and visual-revisitation-based recovery from errors.
- **Results**: Closed-loop navigation by decomposing instructions into sub-goals, executing local visual navigation, and verifying visited places against the topology — **no GPS-like global coordinates at all**.
- **Significance**: The "no map, no GPS, just landmarks" architecture transferable to game NPC navigation and last-metric indoor agents that must recover from wrong turns without global localization.
- **Link**: https://arxiv.org/abs/2609.20388

### 2.3 SIMLIFE: Pattern Understanding for Long-Horizon Human-Agent Partnership
- **Authors**: Run Peng, Zinnia Nie, Jing Ding, Yinpei Dai, Yichi Zhang, Zengqing Wu, Yao Fu, Ziqiao Ma, Jiayuan Mao, Joyce Chai
- **Affiliation**: University of Michigan (Mao, Chai) + industry research cluster (inferred)
- **Venue**: arXiv preprint (2609.19610, cs.AI)
- **Key Innovations**: **SimLife** — a scalable platform simulating long-term household life with rich visual observations, ground-truth action logs, and synthetic dialogues with audio. On top, **SimLife-BP** evaluates long-context pattern understanding: inferring latent behavioral rules from weeks/months of everyday observations, probing **direct, counterfactual, noisy, and inverse reasoning** under varying rule-hint levels.
- **Results**: **106 episodes averaging 15.49 h / 38.57 in-game days**, **1,439 QA pairs**. Frontier models often achieve surface-level prediction without comprehensive rule understanding, rely on **frequency heuristics rather than if-then reasoning**, and fail when behavioral patterns change.
- **Significance**: The benchmark for "how long must an AI companion/game-NPC observe you before it understands your routines?" — a game-style long-horizon partnership benchmark with explicit ground-truth logs, directly relevant to companion-NPC and life-simulation product design.
- **Link**: https://arxiv.org/abs/2609.19610

### 2.4 Semantic Action Graph: A Shared Representation for Agent Grounding and Human Interpretation of Sports Highlights
- **Authors**: Tica Lin, Deepak Chandran, Gauri Jagatap, Chen Chen, Andrea Fanelli, David Gunawan, Josh Kimball
- **Affiliation**: Dolby Laboratories (all authors) — confirmed; IEEE VIS 2026 Workshop on GenAI for Visual Analysis of Sports
- **Venue**: arXiv preprint (2609.20768, cs.HC / cs.AI)
- **Key Innovations**: A lightweight **domain schema for sports broadcasts** representing a match as performer / action / recipient / moment / state nodes connected by role, temporal, and outcome edges — giving agents a **shared, closed vocabulary** and **frame-addressable moments**. Serves two consumers at once: an agentic pipeline composing narrated highlights, and a visual interface letting viewers query/inspect the same structure. Instantiated as **SportSAGE**.
- **Results**: Feedback from **12 soccer fans**: satisfied with highlight/narrative quality; used the graph interface to search, navigate, and inspect moments — verifying a shared representation makes generated content auditable and steerable.
- **Significance**: An answer to "how do viewers verify an AI-curated highlights bot?" — schema-grounded highlight generation with a human-inspectable structure, exportable to any spectator-sports game/live-cast product.
- **Link**: https://arxiv.org/abs/2609.20768

---

## 3. Game Foundation Models, World Models & Agents

### 3.1 MoWAM: Explicit Future Motion Prediction for Efficient World Action Models
- **Authors**: Jiayu Wang, Bin Zhu, Yue Yu, Jingjing Chen
- **Affiliation**: Fudan University (Wang, Yu, Chen) + Singapore Management University (Zhu) — confirmed via web
- **Venue**: arXiv preprint (2609.20709, cs.RO), submitted 17 Sep 2026
- **Key Innovations**: World Action Models (WAMs) that generate future videos at inference pay a large compute tax; removing future generation leaves dynamics only implicitly coded. **MoWAM** replaces future-video generation with **explicit future motion prediction** — modeling structured robot motion as a compact abstraction of the future (how the robot is expected to evolve under the scene + interaction constraints). A **Mixture-of-Transformer** architecture learns future visual dynamics during training while jointly predicting motion and action, so **video generation is removed entirely at inference** while an explicit future representation is retained.
- **Results**: Compact motion representation enables **efficient inference-time scaling by sampling multiple motion/action candidate pairs and selecting among them with a motion-aware** scoring scheme.
- **Significance**: The "drop video-gen at inference, keep a cheap explicit future" pattern — the efficiency direction that makes world models viable in online game/robot loops where per-step video generation is too slow.
- **Link**: https://arxiv.org/abs/2609.20709

### 3.2 Agile-WAM: An Agile Tactile World Action Model for Contact-Rich Robot Control
- **Authors**: Hanchu Zhou, Brendan Lynch, Raman Goyal, Dechen Gao, Begum Kasap, Boqi Zhao, Junshan Zhang
- **Affiliation**: University of California, Davis (Zhou, Gao, Zhao, Zhang) + Analog Devices (Lynch, Goyal, Kasap) — confirmed via web
- **Venue**: arXiv preprint (2609.20761, cs.RO / cs.LG), submitted 17 Sep 2026
- **Key Innovations**: Tactile WAMs usually lean on large pretrained generative backbones for contact-rich dynamics — slow and inflexible. **Agile-WAM** encodes vision + tactile observations into a shared latent that directly feeds a **vision-tactile-to-action flow-matching process** generating action chunks and future visual/tactile latents jointly. Key observation: **vision and touch evolve at different timescales** (adjacent frames are similar; tactile signals change abruptly at contact) → introduces **multi-horizon multimodal prediction**: bigger temporal offset supervision for visual latents, sharper offset for tactile latents.
- **Results**: Flow-matching over shared vision-tactile latents removes the pretrained-generative-backbone bottleneck; multi-horizon prediction respects the modality timescale mismatch.
- **Significance**: Timescale-aware multimodal prediction is the template for any world model fusing **slow visual + fast discrete contact/event channels** — directly applicable to game physics where vision-frequency observations and event-driven contacts coexist.
- **Link**: https://arxiv.org/abs/2609.20761

### 3.3 MM-Future: Multi-Mode Joint World-Action Modeling for Autonomous Driving
- **Authors**: Shuai Liu, Hechangle Gong, Hao Jiang, Runlin He, Junxiang Zhan, Kai Huang, Sheng Yang, Shaoqing Ren
- **Affiliation**: NIO (Liu, Jiang, He, Zhan, Yang) + USTC AGI Institute (Ren, Gong) + Sun Yat-sen University (Huang) + Beihang (Gong) — confirmed via web
- **Venue**: arXiv preprint (2609.20377, cs.CV)
- **Key Innovations**: Autonomous driving couples decision-making with scene evolution under **multi-mode uncertainty**. **MM-Future** generates **multiple paired scene-action hypotheses**, each initialized from a structured action prior + independent future-scene source, then **co-evolved through a modality-aware diffusion Transformer** with bidirectional interaction within each pair. Multi-view video is compressed into planning-oriented **MM-Tokens** for efficient multi-mode rollout, and a future-conditioned proposal scorer ranks trajectory candidates.
- **Results**: **94.0 PDMS / 91.5 EPDMS on NAVSIM navtest** and **32.3 HD-Score in zero-shot closed-loop evaluation on HUGSIM**; ablations confirm joint multi-mode world-action modeling beats single-mode and action-only variants.
- **Significance**: Game-relevant as "predict a *set* of plausible futures with paired actions and pick post-rollout" — the multi-mode proposal-scoring pattern transfers to racing/strategy game agents that must hedge across opponent behaviors.
- **Link**: https://arxiv.org/abs/2609.20377

### 3.4 JEPA-Anything: Learning Predictive Models across Different Worlds
- **Authors**: Taoyong Cui, Zhongyao Wang, Xinyue Xu, Weiyang Liu, Zhaochen Yu, Yuying Zhang, Qiang Gao, Mengyue Yang, Wanli Ouyang, Pheng Ann Heng, Yingcheng Wu, Zhenfei Yin, Ling Yang
- **Affiliation**: CUHK (Cui, Heng, Ouyang; Cui also Stanford visiting) + PhAI Labs / Princeton lineage (Yin, Yang) — confirmed via web
- **Venue**: arXiv preprint (2609.20800, cs.CL), submitted 17 Sep 2026
- **Key Innovations**: World modeling remains domain-specific; can **one learning principle span radically different systems**? **JEPA-Anything** proposes **Orthogonal Predictive Factorization (OPF)**: extend joint-embedding predictive architectures by decomposing latent targets into complementary factors, learning each via dedicated pathways, and recombining them within a shared predictive design.
- **Results**: Evaluated across **seven domains — vision, biology, clinical trajectories, control, molecular dynamics, physical fields, weather** — covering representation learning, intervention prediction, OOD generalization, long-horizon dynamics (10 matched dynamics tasks, 1,000+ clinical events forecasting, **100-step molecular rollouts across four systems**). Beats matched JEPA baselines on **all 10 dynamics tasks** and cuts single-intervention prediction error on Interventional Pong.
- **Significance**: A strong claim that **JEPA-style predictive learning generalizes across "worlds"** — the foundation for unified world models reusable across game, physics, biology, and control simulation.
- **Link**: https://arxiv.org/abs/2609.20800

### 3.5 TacSushi: Tactile-Grounded World-Action Modeling for Dexterous Sushi Manipulation
- **Authors**: Haodi Hu, Kaen Kogashi, Toshiaki Koike-Akino
- **Affiliation**: USC (Hu) + Mitsubishi Electric Research Laboratories (Kogashi, Koike-Akino) — confirmed via web
- **Venue**: arXiv preprint (2609.19613, cs.RO / cs.AI / cs.LG)
- **Key Innovations**: Dexterous food manipulation (deformation, occlusion, uncertain contact). **TacSushi** — a tactile-grounded, **Cosmos3-based world-action policy** that learns from recorded future consequences while acting on current observations. Encodes RGB, language, and hand state with **feature-wise gated fusion** of fingertip tactile features into the action representation; a training-time decoder predicts logged future visual observations, task progress, **relative contact risk**, and tactile summaries (removed at deployment). **Failed trials provide consequence supervision but their actions are excluded from imitation.**
- **Results**: Trained on **340 successful + 50 failed real-robot trials**; **600 rollouts** across 3 in-distribution tasks and 2 OOD ingredient variants vs 6 methods. Terminal outcomes scored with an **anchored visual-quality protocol equal-weighting 5 human ratings + 3 VLM ratings** (beyond a geometric threshold).
- **Significance**: The value of **using failures as consequence labels without imitating them** — plus a VLM+human quality scoring protocol — directly relevant to game-AI learning from player failure traces and to any tactile/contact-heavy dexterous-robot skilling.
- **Link**: https://arxiv.org/abs/2609.19613

---

## 4. Industry Game AI, Sim-to-Real & Safety Filters

### 4.1 PreDE: Predict Before You Deploy — Offline Prediction of Quantization-Induced Task Degradation for World Action Models
- **Authors**: Jiuyi Xu, Jinjia Guo, Meida Chen, Jing Du, Yangming Shi
- **Affiliation**: University of Florida lineage (Du, Shi) (inferred)
- **Venue**: arXiv preprint (2609.19441, cs.RO / cs.AI)
- **Key Innovations**: WAMs run on video-generation backbones needing serious memory/compute; quantization helps but its config space (bit width, grouping, quantizer) is huge, and evaluating every config by closed-loop rollout is costly. **PreDE** predicts **quantization-induced task degradation offline from action deviations**: a small dev-set of closed-loop outcomes calibrates two thresholds, then the framework accepts / rejects / defers each new configuration using a fixed observation log under a within-setting label-ordering hypothesis.
- **Results**: Across **five WAMs and four benchmark settings**: quantization task loss is **configuration-dependent and cannot be explained by bit width alone or a shared deviation threshold** — motivating exactly this per-config prediction.
- **Significance**: "Budgeted model-deployment triage": decide which compressed/small variant of a world-model bot can ship without running the full game — a reusable recipe whenever compute-constrained deployment of heavy world models is the bottleneck.
- **Link**: https://arxiv.org/abs/2609.19441

### 4.2 Learning Reliable Parking Policies via Offline Reinforcement Learning with Quantized Action Representations
- **Authors**: Zewei Yang, Zengqi Peng, Jun Ma
- **Affiliation**: HKUST-GZ (all authors) — confirmed via web; Jun Ma robot-learning group
- **Venue**: arXiv preprint (2609.19894, cs.RO)
- **Key Innovations**: Parking is safety-critical, cluttered, weakly structured, and interactive. A **waypoint-level offline RL** framework for interaction-aware autonomous parking: a dedicated dataset built from **hierarchical expert rollouts with rotational waypoint augmentation** (non-interactive + interactive scenarios); a **LiDAR obstacle representation adapted to the target pose via feature-wise linear modulation**; and a **state-conditioned tokenizer quantizing continuous waypoint sequences into discrete action tokens** over which **conservative Q-learning** suppresses value overestimation on poorly supported actions.
- **Results**: Extensive closed-loop experiments in a parking simulator against prior methods establish reliable interaction-aware maneuver generation.
- **Significance**: Compact representation design (LiDAR → target-pose-conditioned features; continuous actions → tokens + CQL) is a clean blueprint for **offline-RL control of structured maneuvers in tight game/vehicle scenarios**.
- **Link**: https://arxiv.org/abs/2609.19894

### 4.3 Hybrid Residual Reinforcement Learning for Contact-Rich Robotic Book Insertion
- **Authors**: Tianyuan Liu, Rutherford Agbeshi Patamia, Benjamin Champion, Akansel Cosgun, Richard Dazeley
- **Affiliation**: Deakin University lineage (Cosgun, Dazeley; Monash/Deakin ML cluster) (inferred)
- **Venue**: arXiv preprint (2609.19962, cs.RO)
- **Key Innovations**: Book-in-shelf insertion: **millimetre-scale pose error** turns a valid approach into jamming/release failure. The method keeps a **nominal task-space controller for structured insertion/seating** while **residual PPO** supplies bounded local corrections and decides when to release; only the short open-retreat-reclose transition is scripted — a division of authority between known geometry and learned behavior.
- **Results**: Deployment-matched simulation over **512 fixed conditions: 98.50% mean success (SD 0.23 pp) across 3 runs vs 37.89% for nominal control**. Physical xArm7: **60 trials over 30 matched conditions raise success 26.7% → 63.3%**.
- **Significance**: The cleanest recent statement of "trust the controller for what it knows, let RL patch the residual" — the pattern for any game/robot skill where a hand-designed strategy mostly works but needs local corrections in tight tolerances.
- **Link**: https://arxiv.org/abs/2609.19962

---

## 5. Related RL Techniques (Offline RL, Policy Optimization, MPC-Guided Learning, Test-Time Guidance)

### 5.1 GR2PO: Group Relative Return Policy Optimization for Continuous Robot Control
- **Authors**: Pengqin Wang, Qiming Zhang, Shaojie Shen, Jun Ma
- **Affiliation**: HKUST (Guangzhou) (all authors) — confirmed via web; Jun Ma robot-learning group
- **Venue**: arXiv preprint (2609.19850, cs.RO)
- **Key Innovations**: Actor-critic methods pay a value-network overhead and suffer value-approximation error; critic-free group relative policy optimization removes the critic but **fails to learn long-term outcomes under immediate dense rewards**. **GR2PO** estimates **discounted returns from parallelly collected trajectories**, applies **group normalization at each rollout time index**, and uses **relative advantages with clipped targets** to update the policy — a critic-free, return-aware policy optimizer.
- **Results**: Instantiated on robot-control simulation environments, showing improved training efficiency and long-horizon credit assignment vs actor-critic and prior critic-free group-relative baselines.
- **Significance**: Game-agent-relevant as the **GRPO→continuous-control crossover**: group-relative comparing of trajectory returns without a critic, for dense-reward continuous action spaces.
- **Link**: https://arxiv.org/abs/2609.19850

### 5.2 CARE-VI: Conservative Adaptive Reliability Estimation for Value Improvement in Off-Policy Actor-Critic Learning
- **Authors**: Xiang Zou, Shengzhu Shi, Junqi Gao, Zhichang Guo
- **Affiliation**: not stated (inferred — Chinese academic RL cluster)
- **Venue**: arXiv preprint (2609.20098, cs.LG)
- **Key Innovations**: Off-policy actor-critic value improvement depends on how candidate next-action values are **ranked, reviewed, and weighted**. Three mechanisms: **CARS** (Conservative Adaptive Ranking and Screening — retain an ordered candidate prefix within a budget, narrow only when the boundary gap exceeds a disagreement-scaled uncertainty radius), **SEVA** (Selector-Evaluator Value Assessment — order candidates with selector critics, review with a separately parameterized evaluator critic, cap at selector reference), and **DARE** (Dynamic Adaptive Risk-aware Enhancement — regulate each residual correction by candidate reliability and evidence).
- **Results**: Systematically mitigates premature candidate commitment, selection-score bias, and amplification of weak evidence in value improvement targets.
- **Significance**: A "value-improvement with conservative ranking" toolbox for off-policy game-agent training where replay buffers are off-policy by construction and value-target reliability dominates final performance.
- **Link**: https://arxiv.org/abs/2609.20098

### 5.3 SGPS: Accelerating Visual Policy Learning with Sampling-Based Model Predictive Control
- **Authors**: Yilang Liu, Haoxiang You, Qian Wang, Daniel Rakita, Ian Abraham
- **Affiliation**: Yale University (Rakita, Abraham) (inferred)
- **Venue**: arXiv preprint (2609.20575, cs.RO / cs.AI / cs.LG)
- **Key Innovations**: First-order policy gradients (FoPG) via differentiable sim cut training cost but can converge to unintended contact patterns. **SGPS (Sampling-Guided Policy Search)** couples **recurring action-target refinement by sampling-based MPC with first-order policy optimization**: behavior cloning initializes the policy from sampled actions, then training alternates sampling-based refinement with short-horizon FoPG updates under perturbed initial states/randomized dynamics. A **decoupled FoPG formulation excludes rendering from the computation graph**, enabling direct learning from depth observations without a state-policy teacher.
- **Results**: On a **single GPU**, learns policies for locomotion, obstacle traversal, crate pushing, and bimanual carrying.
- **Significance**: "Let a fast but local optimizer (MPC/differentiable sim) generate targets, RL polish them" — an economical training recipe for vision-based game/robot controllers on limited compute.
- **Link**: https://arxiv.org/abs/2609.20575

### 5.4 TraceFlow: Guiding Frozen Flow-Matching Robot Policies with Success and Failure Traces
- **Authors**: Jiaxuan Zhang, Ruizhe Liu, Yu Zhang, Yanchao Yang
- **Affiliation**: HKU cluster (Yu Zhang, Yanchao Yang) (inferred)
- **Venue**: arXiv preprint (2609.20646, cs.RO)
- **Key Innovations**: A frozen flow-matching VLA policy regenerates action chunks each step from a learned velocity field, blind to whether earlier rollouts succeeded. Concurrent test-time methods provide positive guidance (retrieved successes, critics, verifiers) but **none uses the robot's own failed rollouts as negative evidence with only a terminal outcome bit**. **TraceFlow** builds a **progress-aligned guidance field** that turns action densities of retrieved successful *and* failed rollouts into a **bounded correction** to the frozen flow-matching expert, needing **one terminal outcome bit per rollout and no other label**. Its **TraceBank** stores time-ordered state-action traces with terminal labels, seeded from target-task training traces and later admitting the deployed robot's own rollouts.
- **Results**: On an ordered real-robot packing task, the base flow-matching policy completes a fraction of the cases; TraceFlow's negative-trace guidance corrects failed chunks without retraining.
- **Significance**: Test-time corrective feedback for frozen policies using **failures as negative evidence**, merely from a success/fail bit — the cheapest possible "learn from your own dead runs" loop for deployed game/robot agents that cannot retrain online.
- **Link**: https://arxiv.org/abs/2609.20646

---

## Runner-ups Worth a Look (grep-verified unclaimed)

- **2609.20586** CoRef-GS — collaborative-reference-guided embodied manipulation: decompose comp/object relations into sparse references to drive long-horizon joint-generation of high-level behavior; frame-addressable, interaction-complete, improved success rates. https://arxiv.org/abs/2609.20586
- **2609.20396** Imagine-TAMP — language-and-texture-guided Task-and-Motion-Planning: visual sim2real for OPEN-TAMP with imagination-based feasibility checks for leakage-prone constrained manipulation. https://arxiv.org/abs/2609.20396
- **2609.20669** Learning Foresight — forward-dynamics-augmented offline RL for long-horizon decision-making, closing the "world-model hindsight" gap. https://arxiv.org/abs/2609.20669

## Summary Statistics

| Category | Papers Count |
|----------|-------------|
| Game RL, Multi-Agent Learning & Game Theory | 2 |
| Game AI Bots, LLM Agents & Game-Style Benchmarks | 4 |
| Game Foundation Models, World Models & Agents | 5 |
| Industry Game AI, Sim-to-Real & Safety Filters | 3 |
| Related RL Techniques | 4 |
| **Total featured papers** | **18** |

## Cross-references (covered by same-day sibling digests, not re-featured)

- 2609.19636 — Reach or Solve? REACH/SOLVE attribution with checkpoint handoffs (agentic RL measurement) — [arxiv-paper-check 09-19](arxiv-paper-check.md)
- 2609.20089 — UnifiedPlayers: three-player planning/execution/evaluation GRPO self-play — [arxiv-paper-check 09-19](arxiv-paper-check.md)
- 2609.19830 — BATON: dual-axis (intra-trajectory/inter-trajectory) policy optimization for agents — [arxiv-paper-check 09-19](arxiv-paper-check.md)
- 2609.20519 — SoL-Pi: recursively scaling auto-research loops / harness efficiency — [arxiv-paper-check 09-19](arxiv-paper-check.md)
- 2609.19315 — GAVEL: graph world models for verified long-horizon LLM task planning — [09-18 sibling digests](../../2026-09-18/arxiv-ai-search.md)
- 2609.19820 — Steering Equilibrium Selection in Regularized Self-Play — [09-18 sibling digests](../../2026-09-18/arxiv-ai-search.md)
- 2609.20548 — Retaliatory Algorithmic Collusion countermeasure (CURB) — [09-18 sibling digests](../../2026-09-18/arxiv-ai-search.md)
- 2609.20034 — Astronex-World 1.0: real-time interactive world-model foundation model — [09-18 sibling digests](../../2026-09-18/arxiv-ai-search.md)
- 2609.20807 — Score Centering Stabilizes Off-policy RL — [09-18 sibling digests](../../2026-09-18/arxiv-ai-search.md)
- 2609.20004 — EPIG-Tree: compute-optimal branching for gradient-efficient RL — [09-18 sibling digests](../../2026-09-18/arxiv-ai-search.md)

## Key Themes

1. **World models are racing to drop inference-time video generation.** MoWAM (2609.20709) removes video-gen entirely at inference, keeping only explicit motion prediction; Agile-WAM (2609.20761) drops the pretrained generative backbone via shared-latent flow matching; MM-Future (2609.20377) compresses multi-view video into MM-Tokens for efficient multi-mode rollout; PreDE (2609.19441) predicts when a quantized WAM will still work, *before* deployment. The lingering question — "how expensive is a world model at inference?" — now has concrete efficiency recipes on four fronts.

2. **"Use failures as data, but don't imitate them."** TacSushi (2609.19613) uses failed trials for consequence supervision while excluding their actions from imitation; TraceFlow (2609.20646) turns the robot's own failed rollouts into bounded negative evidence using only a terminal success/fail bit. A shared 2026 pattern: closed-loop learning that treats failure as information without imitating failed behavior.

3. **JEPA-style predictive learning claims cross-domain generality.** JEPA-Anything (2609.20800) applies orthogonal predictive factorization across vision, biology, clinical, control, MD, physics fields, and weather — improving all 10 dynamics baselines. Watch for the JEPA-vs-diffusion world-model artifact line (Cosmos3 in TacSushi) rather than the physics specifics.

4. **Frontier-LLM VLN-CE is now a bot-behavioral lab.** GPT-6-Astra (2609.20116) shows a bare-API workflow already reaches 52.0% SR / 70.8 nDTW zero-shot, while Navi-Agent (2609.20388) demonstrates coordinate-free topological navigation without depth or global coordinates — two architectural answers for instruction-guided game NPCs.

5. **Dedup discipline note:** every featured ID (2609.20789–2609.20646) is inside the 09-18 window and was grep-verified 0 hits in `wiki/`; agentic-RL content claimed by same-day `arxiv-paper-check` and window headline world-model items claimed by 09-18 siblings are cross-referenced rather than duplicated.
