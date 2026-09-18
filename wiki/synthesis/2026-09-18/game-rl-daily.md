---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-09-18)"
type: synthesis
created: 2026-09-18
updated: 2026-09-18
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, world-models, mcts, marl, self-play, benchmarks, industry-game-ai, game-theory, offline-rl, model-based-rl, credit-assignment, ope, sim-to-real, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-09-18)

> **Methodology note**: The **Fri 18 Sep 2026 arXiv mailing** (`Showing new listings for Friday, 18 September 2026`, Thu 17 Sep submissions, IDs **2609.19149–2609.20822**) is the fresh window. The same-day sibling digests — `arxiv-ai-search`, `arxiv-paper-check`, `arxiv-daily`, `tech-report-digest` — already ran in full against it and claimed the AI/LLM/IR/CTR/reasoning content (incl. the window's headline game/world-model items: **GAVEL** 2609.19315, **Steering Equilibrium Selection in Regularized Self-Play** 2609.19820, **Astronex-World 1.0** 2609.20034, **Retaliatory Collusion countermeasure** 2609.20548). This digest therefore mines the **unclaimed game-relevant remainder**: live parses of `/list/{cat}/new` for **cs.AI / cs.CL / cs.CV / cs.GT / cs.HC / cs.LG / cs.LO / cs.MA / cs.NE / cs.RO** (924 unique in-window IDs), title + abstract keyword sweep → 36 title-level candidates + targeted abstract screening → **19 curated**. Every featured ID was **grep-verified 0 hits in `wiki/`** and sits outside the sibling-claimed 09-18 ID sets.
>
> **Continuity / already-covered by today's siblings (not re-featured):** **GAVEL** — graph world model harness for verified long-horizon LLM planning, Qwen3-8B 91.8% single-task success (2609.19315) → [arxiv-ai-search 09-18](../../2026-09-18/arxiv-ai-search.md); **Steering Equilibrium Selection in Regularized Self-Play via the Reference Policy** — using the RLHF KL anchor as an equilibrium-selection knob (2609.19820) → [arxiv-ai-search 09-18](../../2026-09-18/arxiv-ai-search.md); **Astronex-World 1.0** — real-time interactive world-model foundation model (2609.20034) → [arxiv-ai-search 09-18](../../2026-09-18/arxiv-ai-search.md); **Retaliatory Algorithmic Collusion countermeasure (CURB)** — TV-distance penalty on Simple Penal Codes' conditional dependence (2609.20548) → [arxiv-ai-search 09-18](../../2026-09-18/arxiv-ai-search.md).

---

## 1. Game RL, Multi-Agent Learning & Game Theory

### 1.1 Graph-Based Stochastic Power-UCT: Monte-Carlo Graph Search with Power Mean Estimation
- **Authors**: Tung Tran, Viet Bao Mai, Hoang Ta, Tuan Dam
- **Affiliation**: Vietnam academic cluster (Mai, Ta) + Caltech lineage (Dam, co-author of the robust-MCTS line 2609.18599) (inferred)
- **Venue**: arXiv preprint (2609.19956, cs.LG)
- **Key Innovations**: Tree-based MCTS **duplicates the same state** when reached via different trajectories, wasting simulations in stochastic MDPs. **GS-Power-UCT** shares states reached at the *same planning depth* while keeping separate value estimates for states reached at different depths — applicable to general stochastic MDPs including those with **cycles**. Two full-state variants follow: **GS-Power-UCT-F** (one node per physical state, maximal sample sharing but mixes values across remaining horizons) and **GS-Power-UCT-F+** (adaptive horizon to bound that mixing bias).
- **Results**: Proves root estimate converges at **O(n^−1/2)** for a fixed planning horizon — matching tree-based Stochastic-Power-UCT while reusing samples across shared states — and that GS-Power-UCT-F+ converges to the optimal infinite-horizon discounted value V*(s0) when the cross-depth gap vanishes. Improved sample efficiency over tree-based and graph-based baselines on stochastic planning benchmarks.
- **Significance**: Directly relevant to game-tree search: cycle-prone stochastic games (gacha/power-ups/random events) waste simulations today; state-sharing MCGS is the same class of technique game-playing engines use to avoid re-planning identical positions.
- **Link**: https://arxiv.org/abs/2609.19956

### 1.2 A Logarithmic Regret Bound for Optimistic Hedge in General-Sum Games
- **Authors**: Junsoo Ha
- **Affiliation**: not stated (inferred — single-author game-theory paper)
- **Venue**: arXiv preprint (2609.19677, cs.GT)
- **Key Innovations**: Can simple **no-regret dynamics** attain smaller regret in self-play than against arbitrary adversaries? Daskalakis et al. (2021) proved O(n·log dᵢ·log⁴T) individual regret for Optimistic Hedge. This work sharpens that analysis via **factorial bounds on high-order differences of probability-weighted pairwise loss gaps** + fixed-norm finite-difference interpolation, achieving **O(√n·log dᵢ·log T)** individual external regret under expected loss-vector feedback with a **larger admissible step size η = Θ(1/(√n·log T))**.
- **Results**: Time-averaged play attains a coarse correlated equilibrium gap **O(√n·log d·log T / T)** where d = max dᵢ — a logarithmic regret bound, improving the O(√T) adversarial floor.
- **Significance**: The cleanest modern statement that "self-play is easier than fighting an adversary" for Optimistic Hedge-style dynamics — the theoretical backbone of why population/self-play training in games converges fast.
- **Link**: https://arxiv.org/abs/2609.19677

### 1.3 Efficient Nash Equilibrium Computation for Cybersecurity Games
- **Authors**: Michael Lanier, David Farmer, Yevgeniy Vorobeychik
- **Affiliation**: Washington University in St. Louis (Vorobeychik) (inferred)
- **Venue**: arXiv preprint (2609.19399, cs.AI / cs.GT)
- **Key Innovations**: PSRO-based equilibrium computation is bottlenecked by **payoff estimation** (every matrix entry = expensive Monte-Carlo simulator rollouts). **Regret-Weighted Payoff Sampling (RWPS)** is a *budgeted* estimator that simulates only the cells an equilibrium is sensitive to and fills the rest with a surrogate trained on earlier simulations. Standard sup-norm bounds fail on such estimators, so the authors prove an **instance-dependent bound weighting error by the opponent's equilibrium mixture** (a certificate computable from simulation data alone) plus a **coverage result**: once the deviation-relevant set is simulated, surrogate error cannot affect either player's regret.
- **Results**: On three 21×21 general-sum games (two synthetic + asymmetric Colonel Blotto), refined bounds are 4–6× tighter; coverage predicts which games are cheap — 18% of the matrix for small-support games vs 82% for Blotto. In growing-pool PSRO, RWPS reaches **lower exploitability than minimum-regret-first search, information-gain search, and progressive sampling at matched budget**, and on the **CyGym and ANSG cyber simulators** it is lowest at the smallest budgets.
- **Significance**: A budget-aware payoff-estimation recipe that directly attacks the cost wall of simulation-based game solving — applicable to any expensive game world (high-fidelity sims, live servers) where equilibrium computation is part of the training loop.
- **Link**: https://arxiv.org/abs/2609.19399

### 1.4 On Periodic and Aperiodic Optimal Strategies in Solvency Games
- **Authors**: Quentin Guilmant, Florian Luca, Richard Mayr, Joël Ouaknine, James Worrell
- **Affiliation**: University of Oxford (Ouaknine, Worrell) + University of Edinburgh (Mayr) + Luca (inferred — international number-theory collaborator)
- **Venue**: arXiv preprint (2609.19438, cs.GT / math.PR)
- **Key Innovations**: **Solvency games** are a gambling problem on infinite-state MDPs (state = investor fortune; each action yields a gain distribution; risk-averse investor minimizes probability of eventual ruin). Prior work showed memoryless deterministic optimal strategies exist but are not eventually constant. This paper **(disproves Kučera's 2012 conjecture)**: optimal strategies need not be ultimately periodic — even with gains in {−3,…,1}, a *unique aperiodic* optimal strategy exists. For gains in {−2,…,1} an ultimately periodic optimal strategy always exists (constant tail or alternating between two actions).
- **Results**: Optimal strategy is computable when unique; some optimal strategy is always computable for gain sets {−ℓ,…,1} for any ℓ; computability of the general case remains open.
- **Significance**: Sharp structural limits on the "eventually periodic keep gambling" intuition that back all cash/capital-management heuristics — a cautionary formal result for risk-averse bot design in gambling-style game economies.
- **Link**: https://arxiv.org/abs/2609.19438

### 1.5 Optimal Strategies in a Sequential Contest with Failures
- **Authors**: Alec Pannunzio, Ashley Shaffer, Gregory Shaver, Shreyas Sundaram
- **Affiliation**: Purdue University cluster (Sundaram, Shaver) (inferred)
- **Venue**: arXiv preprint (2609.19706, math.OC / cs.GT)
- **Key Innovations**: A **Stackelberg model of sequential contests** where the player who invests the most successful effort wins, but each player **fails to invest** their chosen effort with a probability that grows with effort (capturing volatility/credibility), has its own failure cost, and its own effort ceiling (ability). Provides the **follower's optimal response** to an observed leader effort, then the **leader's optimal strategy** anticipating that response.
- **Results**: Full characterization of optimal strategies for both players plus an analysis of how heterogeneous abilities and failure costs bend expected utility for both.
- **Significance**: A clean "who bids when both can fail" formalization — the strategic backbone for auction/pvp/bidding mechanics and for competition models with reliability-constrained players.
- **Link**: https://arxiv.org/abs/2609.19706

---

## 2. Game AI Bots, LLM Agents & Game-Style Benchmarks

### 2.1 DeliveryGym: An RL Environment for Long-Horizon Embodied Agent Planning with Adaptive Curriculum
- **Authors**: Haoqiang Kang, Yiming Zhang, Yiyang Guo, Chuying Li, Jianzhi Shen, Tianruo Rose Xu, Xiaokang Ye, Lianhui Qin
- **Affiliation**: UC San Diego (Qin) (inferred)
- **Venue**: arXiv preprint (2609.19801, cs.LG)
- **Key Innovations**: Argues embodied-agent environments must reward *cross-task dependencies*, not just per-task success (delivering now consumes time/energy/money needed later). **DeliveryGym** is a 3D environment for **continuous courier shifts**: multimodal tool interaction + persistent world dynamics, with **trajectory rewards computed from simulator events** so RL can optimize a whole shift. Crucially, it **adapts future training shifts to the policy's observed weaknesses while keeping evaluation fixed**.
- **Results**: Across 6 models and 13 city maps, evaluation exposes a gap between reliably *executing* assigned deliveries and *choosing/sequencing* work. On the fixed test suite, RL improves **Qwen3-VL-4B net income by 54.3%**; adaptive curriculum training adds **+16.5% test income over uniform sampling** at equal rollout budget.
- **Significance**: An executable, simulator-grounded game-style benchmark for studying long-horizon resource-coupling decisions — and a clean demonstration that *where* an agent practices matters as much as how.
- **Link**: https://arxiv.org/abs/2609.19801

### 2.2 LYRIC: Language-Driven Physics-Based Character Control for Contact-Rich Whole-Body Object Interaction
- **Authors**: Zeyu Han, Zichong Meng, Julian Tanke, Minami Matsumoto, Sergey Bashkirov, Yingruo Fan, Selim Engin, Dongseok Shim, Takashi Shibuya, Yuki Mitsufuji, Huaizu Jiang
- **Affiliation**: Northeastern University (Jiang) + Sony Research cluster (Mitsufuji, Shibuya, Tanke, Shim) (inferred) — industry-academic over RX
- **Venue**: arXiv preprint (2609.19688, cs.RO / cs.GR)
- **Key Innovations**: A **generative flow-matching controller** for **language-driven, contact-rich whole-body object interaction** in physics simulation: one tracking policy trained with *geometry-conditioned interaction rewards* and *relaxed reference tracking near hand-object contact* extracts reliable experts from imperfect MoCap. The full controller is **factorized** into a task-level planner (short-horizon object + humanoid-root trajectories) and a closed-loop action generator; after behavior cloning the planner is frozen and the actor is **post-tuned on-policy** using planner predictions as supervision.
- **Results**: Controlled OMOMO eval: tracker 64.3% vs 53.2% (InterMimic reimplementation); unified policy 76.5% on full OMOMO; held-out split **90.3% task success vs 74.2%** for the strongest kinematic-planner baseline, with better semantic alignment/motion quality; **zero-shot transfer to novel object shapes** and test-time object-waypoint guidance without retraining.
- **Significance**: The physics-sim character-control stack game studios need for "pick up that mug and pour" NPC/intelligent-animation — language-conditioned, whole-body, contact-aware, and hardware-deployable in engine loops.
- **Link**: https://arxiv.org/abs/2609.19688

### 2.3 Contagion on the Trading Floor: How Adversarial Signals Spread in Multi-Agent Trading Systems
- **Authors**: Qi Rong Sua, Junhao Dong, Nguyen Duc Thai, Yuqing Wen, Cheston Tan, Yew-Soon Ong
- **Affiliation**: NTU Singapore / A*STAR CFAR lineage (Ong, Tan) (inferred)
- **Venue**: arXiv preprint (2609.19789, cs.AI)
- **Key Innovations**: First robustness audit of **LLM multi-agent trading stacks** against black-box *input-only* adversarial social-media feeds. Introduces **GMATS** (Generic Multi-Agent Trading System), a framework capturing modern multi-agent trading architectures, plus a **poisoning attacker class** that treats an LLM as a post generator and injects budget-constrained plausible content into the analyst evidence stream. Defines **contagion metrics** tracing belief shifts at analyst/coordinator layers and attack-clean deltas on backtest metrics.
- **Results**: On a safe offline benchmark, simple input-only attackers materially degrade risk-return profiles (Sharpe drops sharply); **suitably designed multi-agent topologies and coordinator prompts dampen adversarial shocks** and improve average robustness under identical poisoning budgets.
- **Significance**: A queueing-model-free audit template for multi-agent decision systems whose "agent economy" connects to games: how adversarial signals propagate through a layered LLM hierarchy — and which agent topologies are robust. Read for the player-coalition/opponent-distrust angle, not the finance part.
- **Link**: https://arxiv.org/abs/2609.19789

---

## 3. Game Foundation Models, World Models & Agents

### 3.1 Conservation Buys Stability and Factoring Buys Counterfactuals in Physical World Models
- **Authors**: Yufeng Wang, Parivesh Priye, Lu Wei, Haibin Ling
- **Affiliation**: Stony Brook University (Ling) (inferred)
- **Venue**: arXiv preprint (2609.19674, cs.LG)
- **Key Innovations**: A learned simulator fails in two *distinct* ways under changed conditions — long-rollout drift, and failure to follow an intervened physical law. This paper shows the two need **different structural remedies**: evolving a learned energy with a **symplectic integrator** preserves conservative geometry (rollouts stay bounded/physical), while **explicit linear factorization** of the physical coupling lets the model follow a *never-seen sign* of that coupling. **Double dissociation** established with matched controls: removing stability structure leaves counterfactual transfer intact; removing factorization destroys counterfactuals without hurting stability.
- **Results**: Symplectic-energized rollouts stay physical up to **100× the training horizon** where equal-capacity predictors, energy-regularized predictors, and tuned neural ODEs diverge; counterfactual law-following works only with factorization; both results persist under pixel-observation state inference and beyond the headline three-body system.
- **Significance**: A concrete design principle for **physical world models in games**: "stable physics rollouts" and "what-if (patched balance/physics) generalization" come from different structural commitments — directly actionable for game-engine neural physics and level-editor what-if sweeps.
- **Link**: https://arxiv.org/abs/2609.19674

### 3.2 WorldContact: A Contact-Centric World Model for Scalable Robot Learning
- **Authors**: Caoliwen Wang, Mengdi Wang, Heng Zhang, Shixun Huang, Siyuan Chen, Chao Liu, Anpei Chen, Zhendong Wang, Peter Yichen Chen, Huamin Wang
- **Affiliation**: Princeton (M. Wang) + graphics/robotics industry-academic cluster (P.Y. Chen, H. Wang) (inferred)
- **Venue**: arXiv preprint (2609.19600, cs.RO)
- **Key Innovations**: A **contact-centric world model for deformable-object manipulation** built from a limited set of high-quality trajectories, generating additional training data by predicting object dynamics at **larger time steps than the source numerical simulator** (which needs small integration steps to avoid interpenetration). Data augmentation made cheaper than sim-rollout replay.
- **Results**: 16 shopping-bag manipulation tasks; state rollout on a single H100 is **10× faster than the source simulator**; a vision-language-action policy fine-tuned on the WorldContact-expanded set goes **65% → 95% single-attempt bag-lift success** on a real robot vs source-sim data alone.
- **Significance**: "Big-step learned physics surrogate as a data furnace" — the exact pattern for scaling game AI training data from expensive real-time physics without fidelity collapse on contact-heavy content.
- **Link**: https://arxiv.org/abs/2609.19600

### 3.3 Feeling Terrain Before Crossing: World Models for Off-Road Navigation
- **Authors**: E-In Son, Dong-Wook Kim, Ji-Hoon Hwang, Kangsun Lee, Jisung Bae, Jung-Taak Kim, Seung-Woo Seo
- **Affiliation**: Seoul National University / KAIST cluster (Seo, Kim) (inferred)
- **Venue**: arXiv preprint (2609.19863, cs.RO / cs.CV)
- **Key Innovations**: Off-road navigation depends on **robot–terrain interaction**, but scene-focused world models only predict pixels. **Feel-WM** — the first off-road navigation world model to **condition on proprioception and predict what the robot will feel** (future proprioceptive state + a learned **failure risk**) alongside what the camera will see, from the robot's own experience with no human labels. The planner rolls out physical future + scene and weighs failure risk vs goal similarity in a separable score.
- **Results**: Beats visual-only world models in open-loop planning and closed-loop rough-terrain navigation across wheeled and legged platforms; deployed onboard a Husky on mountain trails, predicting rough ground ahead and steering around it, completing courses an end-to-end policy fails.
- **Significance**: A template for game/NPC locomotion world models that must predict *consequences the camera can't see* (footing, traction, failure probability) — the "feel plus see" prediction axis game agents need when terrain/traversal matters.
- **Link**: https://arxiv.org/abs/2609.19863

### 3.4 JEPA-WAM: Connecting Generated Visual Instructions to World Action Models through JEPA Latent Representations
- **Authors**: Tianbin Liu, Jian Zhu, Taiyi Su, Jianjun Zhang, Chong Ma, Zitai Huang, Yi Xu
- **Affiliation**: Alibaba DAMO / Shanghai AI Lab lineage (Xu) (inferred, tentative)
- **Venue**: arXiv preprint (2609.20277, cs.AI / cs.RO)
- **Key Innovations**: World Action Models (WAMs) follow instruction poorly when text annotations are sparse/repetitive relative to rich visual-action trajectories — policies latch onto visual context instead of grounding the instruction. **JEPA-WAM** augments each text instruction with **stochastically generated visual instructions** (off-the-shelf text-to-image generator, no training) that are semantically aligned but appearance/layout-divergent, then encodes them with a **frozen V-JEPA 2.1** into compact goal tokens that condition both video and action experts via cross-attention — forcing the policy to ground the *semantics* of the instruction, not the pixels.
- **Results**: Real-robot instruction-following benchmark: **87.3% / 74.5% / 80.9%** success on in-distribution, OOD-scene, and OOD-instruction settings, beating π0 and Fast-WAM by **≥10.0 / 27.3 / 14.5 pp** respectively.
- **Significance**: A cheap, label-frugal way to make text-conditioned world-model agents obey instructions — the semantic-goal-token pattern transfers to any in-game agent asked to "follow the instruction, not the screenshot".
- **Link**: https://arxiv.org/abs/2609.20277

---

## 4. Industry Game AI, Sim-to-Real & Safety Filters

### 4.1 MILER: Semantic Mid-Level Representation for Sim-to-Real Reinforcement Learning in Unstructured Autonomous Driving
- **Authors**: Thomas Steinecker, Denis Trescher, Alexander Bienemann, Thorsten Luettel, Mirko Maehlisch
- **Affiliation**: Fraunhofer FKIE / University of the Bundeswehr Munich lineage (Luettel, Maehlisch) (inferred)
- **Venue**: arXiv preprint (2609.20747, cs.RO / cs.LG)
- **Key Innovations**: RL sim-to-real for **unstructured autonomous driving**: policy trained only in a custom **semantic mid-level representation (MLR) simulator** whose control outputs are applied directly to a bicycle model; at deployment, camera + LiDAR are fused by BEVFusion into a semantic BEV matching the MLR representation, and actions go through a **trajectory-alignment strategy** enabling zero-shot transfer of both perception and control.
- **Results**: 17.3 km driven on a 3.0 km test track with two vehicles, obstacle + hairpin + **33.6 km/h** + off-road sections, no human intervention, entire stack on a **Jetson AGX Orin** (embedded inference).
- **Significance**: The cleanest "train in a mid-level-sim, transfer zero-shot" recipe for game/vehicle-style RL deployment — perception is frozen to the same abstraction used in training, which is exactly what game AI needs when the CE/artist-rendered world must match the training abstraction.
- **Link**: https://arxiv.org/abs/2609.20747

### 4.2 Winning a Won Game: Strict Reach-Avoid-Stay Control Barrier Functions for High-Dimensional Black-Box Systems
- **Authors**: Donggeon David Oh, Duy P. Nguyen, Gongkai Yuan, Qingchen Li, Jaime Fernández Fisac, Haimin Hu
- **Affiliation**: Princeton (Fisac, Hu) (inferred)
- **Venue**: arXiv preprint (2609.19449, cs.RO / eess.SY)
- **Key Innovations**: **sRAS (strict reach-avoid-stay)** formalizes "reach safety, then stay": a Q-value-based CBF safety filter combining a *stay value* (safe permanent residence in a target) with a *reach-avoid value* (safe reachability of the target set) for **high-dimensional black-box systems under bounded uncertainty**. Uses **reachability-based adversarial reinforcement learning** for scalable value approximation — **no known dynamics, affine structure, value derivatives, or hand-designed barriers** at synthesis or deployment.
- **Results**: Under exact values + measure-zero condition, filter preserves sRAS feasibility from almost every winnable initial state; validated on simulation + hardware quadruped gap jumping (cross safely, land, stay safe) and simulated **F1TENTH racing** (safe overtaking and lead retention).
- **Significance**: Safety-filter + adversarial-RL = a deployable recipe for "how a game bot finishes and holds a win state under uncertainty" — identical structure to a racing/maintenance bot that must reach the goal region and stay there without crashing.
- **Link**: https://arxiv.org/abs/2609.19449

---

## 5. Related RL Techniques (Offline RL, Credit Assignment, Evaluation, Prior Guidance)

### 5.1 Improving Online Reinforcement Learning via Bidirectional Behavior Prior Distillation
- **Authors**: Gong Gao, Xiao Lai, Jiaji Shen, Ning Jia, Xianhui Liu, Weidong Zhao
- **Affiliation**: Fudan University lineage (Zhao) (inferred)
- **Venue**: arXiv preprint (2609.20268, cs.LG) — v1 29 Jul 2026 (announced this window)
- **Key Innovations**: Behavior-prior RL normally relies on offline pre-training whose datasets lack expert trajectories → weak priors. **Bidirectional Behavior Prior Distillation (B2PD)** instead uses **action-value priors to guide a CVAE in generating a high-value behavior support set**, then distills those expert behavior priors into the agent — establishing a *bidirectional knowledge flow* (value → generation → distillation → policy) that reduces inefficient exploration and stabilizes optimization.
- **Results**: Substantial sample-efficiency gains with stable policy optimization on state- and pixel-based tasks vs online baselines; shows enforcing a high-value behavioral support set during online learning mitigates critic-induced error amplification.
- **Significance**: "Synthesize your own expert trajectories on the fly" — directly relevant when game agents must bootstrap without a curated expert dataset (common when the game is new and nobody plays it well yet).
- **Link**: https://arxiv.org/abs/2609.20268

### 5.2 Improving Generalization and Robustness in Offline RL via Boundary-Aware Data Augmentation
- **Authors**: Gong Gao, Weidong Zhao, Xianhui Liu
- **Affiliation**: Fudan University lineage (Zhao) (inferred)
- **Venue**: arXiv preprint (2609.20300, cs.LG) — v1 22 Aug 2026 (announced this window)
- **Key Innovations**: Offline RL overfits training data and generalizes poorly to the real environment. Naive interpolation augmentation is fragile because low-level physical signals are hypersensitive to distribution shift; the paper **theoretically shows random episode interpolation's error scales with state distance**, then introduces **Boundary-Aware Data Augmentation (BADA)**: use *neighboring states to construct interpolation boundaries*, producing synthetic data that faithfully preserves the original distribution.
- **Results**: Toy-environment qualitative studies show BADA reconstructs multimodal value distributions while preserving policy smoothness; SOTA across diverse benchmark suites on limited offline datasets.
- **Significance**: The distribution-faithful augmentation answer for offline-trained game agents — keep the learned policy's value shape honest when the real engine/opponent behaves slightly differently from the logged buffer.
- **Link**: https://arxiv.org/abs/2609.20300

### 5.3 Improving Offline Goal-Conditioned RL via Selective Reward Stimulation
- **Authors**: Jing Zhang
- **Affiliation**: not stated (inferred — academic, goal-conditioned RL)
- **Venue**: arXiv preprint (2609.19414, cs.LG)
- **Key Innovations**: In offline goal-conditioned RL with sparse rewards, goal-completion signal is temporally far from the decisions that cause success, and offline value error amplifies this. Analyzed from a **reward-propagation perspective** (goal-directed value separation shrinks relative to local estimation error in a stylized delayed-goal setting), then introduces **Reward Stimulation Implicit Q-Learning (RSIQL)**: inject extra reward at *progress-making intermediate states* flagged by an auxiliary goal-conditioned value function — a flat, non-hierarchical method (no separate subgoal policy).
- **Results**: Beats goal-conditioned IQL on D4RL goal-reaching and OGBench, competitive with hierarchical offline goal-conditioned methods while keeping a simple flat policy.
- **Significance**: "Reward shaping, but principled and from value estimates" — for offline game agents trained on logged play, a cheap way to densify long-horizon success without a hierarchy.
- **Link**: https://arxiv.org/abs/2609.19414

### 5.4 Model-based Bootstrap for Offline Policy Evaluation in Tabular RL
- **Authors**: Weiwei Wang, Yuqiang Li, Xianyi Wu, Bingyi Jing
- **Affiliation**: Hong Kong / Chinese statistics-ML cluster (Jing) (inferred)
- **Venue**: arXiv preprint (2609.20389, stat.ML / cs.LG)
- **Key Innovations**: OPE needs distributional estimates, not just point estimates. Instead of episode-resampling (classical bootstrap), a **model-based bootstrap that regenerates trajectories from an estimated MDP** — accommodating complete trajectories, transition-level observations, and trajectory fragments, and improving finite-sample efficiency. Establishes bootstrap distributional consistency, asymptotically valid confidence intervals, and consistent variance estimation for the target policy value.
- **Results**: Simulations show the method captures the OPE estimator's sampling distribution with tighter and more accurate intervals in most settings.
- **Significance**: When evaluating a new game-AI policy offline before shipping it (patch, matchmaking, economy), you need confidence bounds, not just point estimates — this gives them in a fragment-tolerant, tabular-world way.
- **Link**: https://arxiv.org/abs/2609.20389

### 5.5 EmbodiedMind: Adaptive Data Curation and Prefix-Tree RL for Efficient Embodied Intelligence
- **Authors**: Feifan Wang, Zongbing Zhang, Yu Zhang, Lingfeng Wang, Yurui Zhu, Jin Deng, Mingliang Zhang, Zhengguang Gao, Yongcheng Wang, Jin Xu, Ri Yang
- **Affiliation**: China academic-industry embodied-AI cluster (inferred, tentative)
- **Venue**: arXiv preprint (2609.19659, cs.RO / cs.LG)
- **Key Innovations**: Three-stage training paradigm fixing the embodied-foundation-model problems of **low-informative samples, imbalanced cross-task gradients, and long-horizon credit assignment**: (1) **RSFT** (rejection-sampling fine-tuning) filters low-informative samples for behavioral priors; (2) **IR-GRPO** (iterative rejection GRPO) with **difficulty-stratified per-task queues** and a hybrid reward keeps RL datasets balanced; (3) **Trie-GRPO**, an RL algorithm over **action prefix trees** that gives *step-level advantage estimation* — isolating intermediate correct decisions from downstream errors.
- **Results**: **70.02% average performance across 18 benchmarks**, significantly outperforming other embodied foundation models on long-horizon task-planning accuracy.
- **Significance**: Prefix-tree credit assignment is a practical answer to "which token/step caused success in a long game trajectory" — the game-agent version of decomposing episode rewards into step-level advantages.
- **Link**: https://arxiv.org/abs/2609.19659

---

## Runner-ups Worth a Look (grep-verified unclaimed)

- **2609.20649** DexTouch-WM — action-conditioned tactile world models learned from human touch; human-robot transfer for dexterous manipulation prediction and policy-learning surrogates. https://arxiv.org/abs/2609.20649
- **2609.19452** GLAMDRING — gait+body co-design via RL over Central Pattern Generators; resolves morphology from logged operating envelope so co-design costs only a fixed number of RL runs. https://arxiv.org/abs/2609.19452
- **2609.20450** Sparse One-Step-Ahead Optimal Control of Time-Varying Affine Opinion Networks (DeGroot/Friedkin–Johnsen): sparse intervention in competitive games is an exact potential game; sorting-based exact support selection. https://arxiv.org/abs/2609.20450

## Summary Statistics

| Category | Papers Count |
|----------|-------------|
| Game RL, Multi-Agent Learning & Game Theory | 5 |
| Game AI Bots, LLM Agents & Game-Style Benchmarks | 3 |
| Game Foundation Models & World Models | 4 |
| Industry Game AI, Sim-to-Real & Safety Filters | 2 |
| Related RL Techniques | 5 |
| **Total featured papers** | **19** |

## Cross-references (covered by today's sibling digests, not re-featured)

- 2609.19315 — GAVEL: graph world models for verified long-horizon LLM task planning (Qwen3-8B 91.8% single-task) — [arxiv-ai-search 09-18](../../2026-09-18/arxiv-ai-search.md)
- 2609.19820 — Steering Equilibrium Selection in Regularized Self-Play via the Reference Policy — [arxiv-ai-search 09-18](../../2026-09-18/arxiv-ai-search.md)
- 2609.20548 — Mitigating Retaliatory Algorithmic Collusion in Repeated Games (SPC-conditioning detection + CURB) — [arxiv-ai-search 09-18](../../2026-09-18/arxiv-ai-search.md)
- 2609.20034 — Astronex-World 1.0: real-time interactive world-model foundation model — [arxiv-ai-search 09-18](../../2026-09-18/arxiv-ai-search.md)
- 2609.20807 — Score Centering Stabilizes Off-policy RL (drift cancellation for training-inference mismatch) — [arxiv-ai-search 09-18](../../2026-09-18/arxiv-ai-search.md)
- 2609.20004 — EPIG-Tree: compute-optimal branching for gradient-efficient RL — [arxiv-ai-search 09-18](../../2026-09-18/arxiv-ai-search.md)

## Key Themes

1. **Simulator economics are the through-line of the window**: PSRO paid tribute to slow simulators with budgeted equilibrium-aware payoff sampling (RWPS, 2609.19399); WorldContact (2609.19600) turns a 10×-faster big-step physics surrogate into a training-data furnace; MILER (2609.20747) sidesteps reality gaps entirely by training on a semantic mid-level abstraction and freezing perception to it — three different answers to "the game/sim costs too much to learn from."

2. **World models keep adding a "feel" channel beyond pixels**: Feel-WM (2609.19863) predicts proprioceptive future + failure risk (not just what the camera sees); DexTouch-WM (2609.20649) adds tactile prediction; JEPA-WAM (2609.20277) forces instruction-grounding by presenting only semantic goal tokens. Combined with today's conservation/factoring double-dissociation (2609.19674), world models are maturing from image predictors into *physics- and affordance-aware forecasters*.

3. **Formal game theory is on a robustness-and-clarity streak**: a logarithmic regret bound for self-play no-regret dynamics (2609.19677), a conjecture disproved for solvency-gambling strategies (2609.19438), contest theory with failure probabilities (2609.19706), and the sibling-claimed Nash polytope steering result (2609.19820) — theory is catching up to the empirically-driven game-RL wave.

4. **Dedup discipline note**: every featured ID (2609.19399–2609.20747) is inside this window and was grep-verified 0 hits in `wiki/`; the window's marquee AI/world-model items were deliberately left to sibling digests and cross-referenced rather than duplicated.