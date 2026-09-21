---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-09-21)"
type: synthesis
created: 2026-09-21
updated: 2026-09-21
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, world-models, self-play, marl, game-theory, benchmarks, industry-game-ai, imitation-learning, reward-shaping, model-based-rl, risk-sensitive-rl, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-09-21)

> **Methodology note**: **Mon 21 Sep 2026 is the first fresh arXiv mailing since Fri 18 Sep** (weekends silent; the 09-19/09-20 editions were weekend re-mining runs). Fresh window = **Sun 20 Sep submissions announced Mon 21 Sep, IDs 2609.20823–2609.22086**, sitting entirely above the Fri-18 sibling max (2609.20822). Live parses of `/list/{cat}/new` for **cs.AI / cs.GT / cs.LG / cs.MA / cs.CV / cs.CL / cs.RO / cs.NE / cs.HC / cs.LO** → **475 unique in-window IDs** → title + abstract keyword sweep → targeted screening → **18 curated + 3 runner-ups**. Every featured ID was **grep-verified 0 hits in `wiki/`** and sits outside every 09-21 sibling-claimed set.
>
> **Continuity / already-covered by the 09-21 siblings (not re-featured):** the window's pure-game marquee items were taken hours ago by the same-day digests — GameLogicBench 2609.21562, MORM 2609.21976, MEFPIA quantum games 2609.21944, Colonel Blotto Deterrence 2609.21064 → [arxiv-ai-search 09-21](../2026-09-21/arxiv-ai-search.md); TaxiGPT "World Modeling in Transformers" 2609.21748, GameASG-Bench 2609.21293, world-model continual-learning benchmark 2609.22055, OpenMAS-GCom 2609.21527, ArenaFlow 2609.21378 → [arxiv-daily 09-21](../2026-09-21/arxiv-daily.md). This edition therefore mines the **unclaimed game-relevant remainder** — which this window shapes as a **physics/body-first Game RL + world-model-science + LLM-agent-simulation** digest.

---

## 1. Game RL, Multi-Agent Learning & Game Theory

### 1.1 Dynamics-Induced Commitment in Learning-Based Robotic Penalty Kicks
- **Authors**: Ruize Geng, Hao E. Zhang, Yisen Li, Yikai Wang, H. Eric Tseng, Ding Zhao
- **Affiliation**: not stated (inferred — CMU Robotics Institute + Ford autos; Zhao/Tseng name-line match, hierarchical humanoid-quadruped soccer hardware)
- **Venue**: arXiv preprint (2609.21100, cs.RO), fresh Mon 21 Sep window
- **Key Innovations**: Treats the physical *body* as a first-class constraint in strategic game learning. In a **humanoid-shooter vs quadruped-keeper penalty system**, a game-level self-play policy commands fixed soccer whole-body controllers (S-WBCs). **DIC-Map (dynamics-induced commitment mapping)** estimates continuation capability from the kinematics, identifies the *first persistent loss of a terminal alternative* (the moment one action path becomes physically irreversible), and tests whether the remaining interaction still admits a reduced zero-sum game. For symmetric terminal alternatives it yields a closed-form bound on optimal strategy concentration, driven by the responder's value of deferring.
- **Results**: In the two-leg penalty lab, commitment localises **≈0.29 s before contact**; merely increasing ball speed shifts deferral coverage. Across four responder policies, replacing the read-out estimator raises save rate from **0.240 → 0.472**, whereas an equal gain in read accuracy obtained by waiting only reaches 0.246 — indicating the estimator channel (not read accuracy) dominates the improvement.
- **Significance**: One of the cleanest demonstrations that **game-level optimality is body-dependent**: the strategic solution set of a physical game changes as the executor's capabilities change — directly relevant to game AI that must sit on top of physics models, animation controllers, or FPGA-limited actuators.
- **Link**: https://arxiv.org/abs/2609.21100

### 1.2 CounterPlay: Counterfactual Post-Training for Self-Play Driving Policies
- **Authors**: Jiarong Wei, Yin Wu, Runkai He, Abhinav Valada
- **Affiliation**: not stated (inferred — University of Freiburg; Valada autonomous-interactive-systems lineage)
- **Venue**: arXiv preprint (2609.21617, cs.RO), fresh Mon 21 Sep window
- **Key Innovations**: Self-play in high-throughput simulators plateaus because failed episodes revisit — existing post-training evaluates alternative actions *at* the failure state, when recovery may require changing driving style *earlier*. **CounterPlay backtracks**: (i) **failure-driven backtracking** uses the policy's own value estimates to select an earlier stored state for a retry; (ii) **reward conditioning** lets one policy retry that state under styles from cautious to aggressive; (iii) retries are kept only if no other vehicle incurs a new/earlier collision-or-off-road event relative to the factual branch, then distilled under the deployment condition.
- **Results**: On **BehaviorBench**, CounterPlay reaches state-of-the-art on both **Interactive and Random splits across all eight traffic regimes using 1B post-training transitions — just 1% of the anchor's 100B self-play budget**. Improvements hold across all three evaluated driving styles, and a large fraction of the anchor's timeout cases are resolved with a balance of completion vs safety that neither continued self-play nor simply adopting a more aggressive style attains.
- **Significance**: A concrete answer to "what do you do with a converged self-play policy" — targeted counterfactual retraining instead of more simulation, the video-game-esports-analogous 'scrimmage review' pattern for agentic sim training.
- **Link**: https://arxiv.org/abs/2609.21617

### 1.3 MAAP: Multi-Agent Active Perception for Collaborative Manipulation
- **Authors**: Bruno N.Y. Chen, Li Kang, Heng Zhou, Xiufeng Song, Zhemeng Zhang, Jiahua Ma, Yiran Qin
- **Affiliation**: not stated (inferred — academic embodied-manipulation/MARL cluster)
- **Venue**: arXiv preprint (2609.21929, cs.RO / cs.MA), fresh Mon 21 Sep window
- **Key Innovations**: In multi-arm manipulation every wrist camera is a *movable viewpoint* — observations teams currently waste. **MAAP** makes each arm dual-purpose (execute + perceive for the team), removing the dedicated sensing-agent assumption. Paired **RAIL (Role-Aware Imitation Learning)** predicts each arm's current role jointly with its action chunk and conditions action generation on that role, packing role-dependent behaviours into one network.
- **Results**: Widening the perception regime lifts average success on four simulated tasks from **56.5% (fixed camera) → 62.5% (one active wrist) → 70.0% (all active)**, and **MAAP+RAIL → 79.2%**; on the three-arm Microwave task RAIL alone raises success from **47% → 82%** on identical multi-wrist inputs. On a dual-arm platform MAAP+RAIL succeeds in **14/20** placement trials vs **0/20** for fixed-view ACT.
- **Significance**: Collaborative manipulation as *its own active-perception mechanism* — the multi-robot analogue of "players are also cameras", a lightweight restructuring of MARL/IL teams that needs no new hardware.
- **Link**: https://arxiv.org/abs/2609.21929

### 1.4 People Escalate Against a "Human" Competitor and Hold Back Against an "Optimising Machine"
- **Authors**: Vinicius Ferraz, Leon Houf
- **Affiliation**: not stated (inferred — experimental/behavioral economics; dynamic all-pay auction design)
- **Venue**: arXiv preprint (2609.21439, cs.HC / econ), fresh Mon 21 Sep window
- **Key Innovations**: In repeated human-vs-AI contests, escalation is driven by two separable channels — an **opponent effect** (what the system actually is) and an **information effect** (what players are *told*) — and the two are controlled by different actors. A preregistered experiment (N = 1,395) uses a **dynamic all-pay auction**, a repeated contest whose incentives natively produce escalation of commitment, crossed with truthfully-labelled opponent types in a deception-free design.
- **Results**: The *label alone* moves behaviour: median price rises **+6.7 points** when a human may be the opponent, falls **−8.8 points** when an optimising machine may be — a spread of ≈15% of the prize value produced purely by information. Actually facing the AI lowers prices but also reduces the chance both sides end with positive earnings (opponent channel). The information effect survives controlling for articulated strategy and individual differences — "describing an AI competitor is not behaviourally neutral."
- **Significance**: Hard evidence that **game-AI deployment changes human play even before the AI acts** — the information-layer design problem for matchmaking, bot-styled opponents, and live-service game economies that label their competitors.
- **Link**: https://arxiv.org/abs/2609.21439

### 1.5 From Switching to Dynamic Regret: A Simple Reduction via Unbiased Random Sequences
- **Authors**: Yibo Wang, Wenhao Yang, Sifan Yang, Yuanyu Wan, Lijun Zhang
- **Affiliation**: not stated (inferred — Nanjing University; Lijun Zhang online-learning lineage)
- **Venue**: arXiv preprint (2609.20968, cs.LG), fresh Mon 21 Sep window
- **Key Innovations**: Dynamic regret against a time-varying comparator is the right quantity for non-stationary games but its optimal bounds "always require intricate analysis." The paper reduces **dynamic regret → switching regret**: for *any* comparator sequence, construct an auxiliary random sequence that is unbiased per-round with controlled variance and few switches, then decompose dynamic regret into expected switching regret plus the controlled variance.
- **Results**: Out-of-the-box switching-regret algorithms now yield **Õ(T^{1/3}·P_T^{2/3})** dynamic regret for strongly convex and exp-concave losses and recover **O(√(T(1+P_T)))** for general convex — all **matching minimax-optimal** results for the three loss families.
- **Significance**: A general "regret reduction" toolkit for adaptive opponents in games whose optimal strategies drift — one step closer to making no-regret game learning first-class in non-static environments.
- **Link**: https://arxiv.org/abs/2609.20968

---

## 2. Game AI Bots, LLM Agents & NPC Simulation

### 2.1 Bayesian Chronicle Agents: A Controllable Belief Layer for LLM Social Simulation
- **Authors**: Hafsa Akbar, Daniel Platnick, Marjan Alirezaie, Hossein Rahnama
- **Affiliation**: not stated (inferred — Toronto Metropolitan University-aligned agent-simulation group; Rahnama)
- **Venue**: Accepted at the 2nd Workshop for Research on Agent Language Models (REALM), **EMNLP 2026** (arXiv 2609.21997, cs.MA / cs.AI), fresh Mon 21 Sep window
- **Key Innovations**: LLM NPCs in social simulations revise opinions implicitly, in-context — how open an agent is to persuasion can neither be specified nor verified. **Bayesian Chronicle Agents (BCA)** separates *what an agent believes* from *how it speaks*: every stance is an explicit probability, updated by one Bayesian step per utterance heard, with a single prior-strength parameter **κ (stubbornness)** modelled on Friedkin–Johnsen opinion dynamics.
- **Results**: Sweeping κ yields **three canonical opinion regimes on demand** — consensus, persistent disagreement, committed-minority influence — with persistent disagreement matching FJ closed-form fixed points at **R² = 0.93–0.99**. Prescribed κ remains recoverable after the language round-trip (perfect rank-order recovery across all four models), and explicit belief *audits* the simulation: it surfaces systematic per-model stance biases that end-to-end simulation would silently absorb.
- **Significance**: For narrative/social NPCs and market sims, BCA is the "belief as state, language as policy" pattern — controllable, verifiable opinion dynamics instead of prompt-shaped vibes.
- **Link**: https://arxiv.org/abs/2609.21997

### 2.2 BirdsongChat: A Hybrid Multi-Agent Framework for Multimodal Embodied Behavior Simulation
- **Authors**: Callie C. Liao, Duoduo Liao, Ellie L. Zhang
- **Affiliation**: not stated (inferred — multimodal embodied-simulation group)
- **Venue**: Accepted at the 2nd Workshop for Research on Agent Language Models (REALM), **EMNLP 2026** (arXiv 2609.20887, cs.MA), fresh Mon 21 Sep window
- **Key Innovations**: Bridging LLM semantic reasoning and physical simulation agents through an explicit **Unified Parameter Representation (UPR)** — LLM reasoning agents translate multimodal inputs into interpretable control parameters consumed by simulation agents that produce synchronized 3D motion, spatialized soundscapes, and environmental behaviour. The testbed is interactive **avian behaviour simulation** (species, affective state, multi-bird interaction) — a prototype of the "LLM brain + sim body" NPC architecture.
- **Results**: Normalized scores of **94.4% cross-modal coherence, 100% affective consistency, 92.6% generation consistency** on text- and image-guided scenarios.
- **Significance**: The "explicit intermediate representation between reasoning and physics" pattern generalises to virtual NPCs, ecoacoustics, and creative multimedia — the architecture-level answer to controllable embodied NPC behaviour across modalities.
- **Link**: https://arxiv.org/abs/2609.20887

---

## 3. Game Foundation Models, World Models & Game Agents

### 3.1 Skel-WAM: A Hand-Skeleton-Conditioned World Action Model for Human-to-Robot Transfer
- **Authors**: Zetao Cai, Yaping Li, Yiqun Wang, Xinyu Zhan, Yuyin Yang, Haoxiang Ma, Kailin Li, Tao Lu, Jiangmiao Pang, Linning Xu, Dahua Lin
- **Affiliation**: not stated (inferred — CUHK + Shanghai AI Laboratory; Lin/Pang/Xu lineages)
- **Venue**: arXiv preprint (2609.21514, cs.RO), fresh Mon 21 Sep window
- **Key Innovations**: WAM-family entry that closes the **human→robot embodiment gap in the *action* space**: both human and robot motion are aligned to a **common hand-skeleton topology** (skeleton overlays grounding the scene + structured 2.5-D keypoints encoding hand kinematics). Video and Keypoint Experts jointly learn visual+skeletal dynamics in a Mixture-of-Transformers, while a separately robot-trained Action Expert maps predictions to executable controls — allowing human videos to supervise world dynamics **without any robot action labels**.
- **Results**: **79.86% (real bimanual) / 63.29% (sim)** average success, beating strongest baselines by **+22.22 / +8.28 pp**; human-robot cotraining more than doubles real-world success on task variations absent from robot data (**38.89% → 86.11%**).
- **Significance**: "Human gameplay/videos as free world-model supervision" — the cross-embodiment learning surface that lets game and robotics world models be pretrained on the abundant video/stream data instead of scarce robot telemetry.
- **Link**: https://arxiv.org/abs/2609.21514

### 3.2 Sandwich-Residuals: Parameter-Efficient Test-Time Adaptation of World Models
- **Authors**: Krishnam Soni, Aditya Sehgal, Vedant Dave, Elmar Rueckert
- **Affiliation**: not stated (inferred — University of Münster; Rueckert ML-robotics lineage)
- **Venue**: arXiv preprint (2609.21740, cs.RO), fresh Mon 21 Sep window
- **Key Innovations**: Test-time adaptation of latent world models normally rewrites millions of internal weights and needs a choice *which* block to adapt. **Sandwich-Residuals keeps the world model frozen** and learns only small residual corrections *around* the predictor, optimised online from the model's own self-supervised prediction error — no rewards, labels, or source-domain data.
- **Results**: On **21 AdaJEPA conditions**: **1.3× the frozen model's success rate** while retaining **95% of the strongest AdaJEPA variant** with **97–99% fewer adapted parameters**; under compound shifts the advantage widens to 1.9×. The same principle transfers to a DINO-WM model for 3-D manipulation.
- **Significance**: The "surgery on the predictor, not the model" result: effective world-model adaptation does not require touching pretrained internals — a deployment-economics lever for on-device and live-game world models.
- **Link**: https://arxiv.org/abs/2609.21740

### 3.3 Compact but Moving: Intervention-Relevant Geometry in Recurrent World Models
- **Authors**: Yuming Chen, Yang Liu
- **Affiliation**: not stated (inferred — interpretable-dynamics / mechanistic world-model cluster)
- **Venue**: arXiv preprint (2609.21787, cs.RO / cs.LG), fresh Mon 21 Sep window
- **Key Innovations**: Previous work found a checkpoint-specific **rank-4 interface** for one-shot counterfactual velocity interventions in a controlled recurrent world model. This paper asks what happens *after* the correction enters the model: the correction rapidly leaves the fixed entry subspace during autonomous rollout, **yet** a low-rank image obtained by transporting the entry directions along the *factual recurrent Jacobian chain* still captures most of the nonlinear correction.
- **Results**: Tangent-predicted restarts preserve substantial counterfactual-future function; the transport/function pattern recurs across independently trained structured-GRU models and a parameter-matched privileged LSTM. A finite-horizon future-response operator over the recurrent carrier is characterised, with patching shifting its leading sensitive directions toward the native-counterfactual organisation.
- **Significance**: Mechanistic proof that **compact intervention structure can persist as a moving, state-dependent local geometry inside high-dimensional recurrent dynamics** — crucial for anyone patching world models (sim steerability, game NPC trajectory edits) rather than retraining them.
- **Link**: https://arxiv.org/abs/2609.21787

### 3.4 Adaptive Rollout Truncation Based on Epistemic Uncertainty for Efficient Offline World Model Training
- **Authors**: Nikodem Sebastian Zymla, Laurin Thiele, Johannes Pitz
- **Affiliation**: not stated (inferred — RWTH Aachen-aligned; IROS 2026 Workshop paper)
- **Venue**: IEEE/RSJ IROS 2026 Workshop "Rethinking Uncertainty for Modern Robotics Paradigms" (arXiv 2609.21482, cs.RO / cs.LG), fresh Mon 21 Sep window
- **Key Innovations**: Fixed rollout horizons in multi-step autoregressive world-model training (a) waste compute and (b) amplify early training errors while the model is still bad. This paper introduces **epistemic-uncertainty-driven adaptive rollout**: rollouts terminate as soon as uncertainty (five-head ensemble with shared recurrent backbone, or MC Dropout) exceeds a threshold calibrated in a two-stage warm-up — an auto-curriculum on rollout length.
- **Results**: On **ANYmal-D / ANT**, ensemble-based adaptive truncation matches or beats fixed-horizon and RWM-U baselines while needing **≈72% less rollout computation** to reach comparable final prediction performance.
- **Significance**: "Training-time compute follows model reliability" — a cheap curriculum lever every model-based game/sim world model can adopt, complementing the inference-side adaptation work (3.2).
- **Link**: https://arxiv.org/abs/2609.21482

---

## 4. Procedural Content Generation & Automated Game Design

> **No fresh unclaimed PCG content this window.** The window's two game-generation items both shipped hours ago via the same-day siblings — **GameASG-Bench** (2609.21293, 47 browser-native game-generation tasks / 12 genres with L1 static + L2 browser-executed behavioral checks, best strict task success 55.3%) — [arxiv-daily 09-21](../2026-09-21/arxiv-daily.md); **GameLogicBench** (2609.21562, 72 Godot gameplay-logic tasks with tick-level state assertions over 1,451 seeded test cases, best solve 52.78%) — [arxiv-ai-search 09-21](../2026-09-21/arxiv-ai-search.md). Cross-referenced rather than duplicated.

---

## 5. Game & Agent Benchmarks / Evaluation Suites

> **Agent-evaluation-cousin note**: the window's pure-game benchmark slots are sibling-covered (above); the two featured items below are the remaining rigorously-constructed evaluation suites a game-agent context can reuse (human-vs-model cognition, embodied proactive-intelligence).

### 5.1 CogGym: Towards Large-Scale Comparative Evaluation of Human and Machine Cognition
- **Authors**: Lance Ying, Jinzhou Wu, Yingshan Susan Wang, ..., W. Andrew McRae (48-author cognitive-science consortium: Kelsey Allen, Brian Christian, Evelina Fedorenko, Michael C. Frank, Tao Gao, Samuel J. Gershman, Jennifer Hu, Tal Linzen, Hongjing Lu, Timothy O'Donnell, Desmond Ong, Steven T. Piantadosi, Rebecca Saxe, Eric Schulz, Tianmin Shu, Tomer Ullman, Fei Xu, Ilker Yildirim, Thomas L. Griffiths, Tobias Gerstenberg, Kevin Smith, Joshua B. Tenenbaum, et al.)
- **Affiliation**: not stated (inferred — multi-institution cognitive-science consortium, Stanford/MIT/UCLA/Princeton/DeepMind lineage)
- **Venue**: arXiv preprint (2609.21259, cs.AI), fresh Mon 21 Sep window
- **Key Innovations**: Scales human-vs-model comparison to thousands of *matched experimental trials*: a semi-automated human-in-the-loop pipeline standardises diverse paradigms into a task-agnostic **Experiment Markup Language (EML)**. First release: **258 cognitive experiments from 100 papers** on human commonsense reasoning, evaluated across **50 LLMs** against human responses.
- **Results**: Clear scaling trend — larger/newer models better reproduce human judgments — but the gain on commonsense tasks is **considerably slower than the gains on math/coding formal benchmarks**: human split-half reliability is R² ≈ 0.92–0.95, best models reach only **R² = 0.59 (text) / 0.58 (image) / 0.43 (video)**.
- **Significance**: The formal-reasoning-vs-common-reasoning gap quantified at benchmark scale — the measurement tool for judging whether an agent is actually *human-aligned in playable/common worlds*, not just on verifiable puzzles.
- **Link**: https://arxiv.org/abs/2609.21259

### 5.2 RobotEQ-Video: A Video-Centric Benchmark for Social Proactive Intelligence with World-State Taxonomy
- **Authors**: Xinyi Che, Zheng Lian, Kuofei Fang, Xuehao Wang, Xinghai Gao, Junqing Wu, ..., Bin He
- **Affiliation**: not stated (inferred — multi-institution embodied-AI/HCI benchmark cluster)
- **Venue**: arXiv preprint (2609.21371, cs.CV / cs.HC), fresh Mon 21 Sep window
- **Key Innovations**: Shifts Social Proactive Intelligence (SPI) evaluation from static images to **dynamic video** and replaces free-form data collection with a **four-level hierarchical world-state taxonomy** (6 domains → 20 dimensions → 142 level-1 → 816 level-2 attributes) guaranteeing comprehensive scenario coverage.
- **Results**: 2K+ videos, 100K+ human annotations, 16K+ behavior-properness labels. Current systems remain **unreliable and fall short of human performance**, and the paper explores world models as a partial remedy.
- **Significance**: A structured, exhaustive world-state taxonomy for judging *socially appropriate* agent behaviour — the evaluation scaffold for NPCs and sim agents whose correctness is behavioural appropriateness, not just task completion.
- **Link**: https://arxiv.org/abs/2609.21371

---

## 6. Industry Game AI, Sim-to-Real & On-Device Inference

### 6.1 ZYT-World: A Real-Time Controllable World Model for Closed-Loop Autonomous-Driving Simulation
- **Authors**: Boni Hu, Xiong Wei, Haoming Huang, Yong Huang, ..., Wei Bi, Kaixuan Wang, Zichao Guo, Xiaozhi Chen (26-author team)
- **Affiliation**: not stated (inferred — industry autonomous-driving lab; Xiaozhi Chen PointPillars-lineage, production closed-loop sim)
- **Venue**: arXiv preprint / Technical Report (2609.21712, cs.CV), fresh Mon 21 Sep window
- **Key Innovations**: Production closed-loop driving simulation as *game-engine-style world generation*: a single architecture natively producing **four fisheye views (>180° FOV) + three pinhole views**. Projection-specific Plücker adapters encode camera geometry, ego-motion-adaptive layer norm gives global motion control, and a pixel-aligned layout conditions on instance-level boxes/headings/colors. Teacher-forcing + causal-consistency + self-rollout-distribution distillations plus a joint seven-view **RigCritic** compress a 40-step bidirectional teacher into a **one-step per-latent streaming generator**; a 19M-param TinyVAE decoder, W8A8 quantization, and a scene-identity implicit-memory module handle the deployment levers.
- **Results**: One-step model retains **>90% of teacher PSNR/SSIM** with FID/FVD/LPIPS within 11%, and is **107.7× faster** than the 40-step teacher under generator-only timing; TinyVAE decodes **59.8× faster** than the Wan baseline; 30s rollouts and cross-trajectory revisits show the intended long-horizon and location-memory behaviour.
- **Significance**: "Real-time, controllable, place-faithful world models in production sim" — the automotive-motion sim equivalent of game-engine replays, and the industrial cousin of the research video/world-model line featured in prior digests (WorldEngine-2, MoWAM, MM-Future).
- **Link**: https://arxiv.org/abs/2609.21712

---

## 7. Related RL Techniques (Model-Based, Risk-Sensitive, Reward Shaping, Imitation)

### 7.1 Efficient Bayes-Adaptive Reinforcement Learning with Temporal Logic Specifications
- **Authors**: Jonathan Hau, Alessandro Abate
- **Affiliation**: not stated (inferred — University of Oxford; Abate formal-methods/verification lineage)
- **Venue**: IEEE venue (©2026 IEEE notice on arXiv; conference *to appear*), arXiv 2609.20954, cs.LG — fresh Mon 21 Sep window
- **Key Innovations**: End-to-end model-based RL for policy synthesis under **LTL specifications** (safety/reachability): a Limit-Deterministic Büchi Automaton (LDBA) of the task is synchronised with a **Bayes-Adaptive MDP (BAMDP)** of the unknown environment, and a novel **Bayes-Adaptive Monte-Carlo Planning (BAMCP)** algorithm performs approximate Bayes-optimal strategy synthesis in the synchronised construct.
- **Results**: Beats non-Bayesian model-free baselines on property satisfaction and sample efficiency across finite- and infinite-horizon tasks; ablations isolate the new BAMCP's gain over classical BAMCP; a *cautious* RL use case cuts task violations during training.
- **Significance**: Formal-spec-constrained exploration in unknown games — "explore safely toward the objective's automaton" — combining verification-grade task encoding with Bayes-optimal exploration, relevant to game QA and safety-gated RLHF training loops.
- **Link**: https://arxiv.org/abs/2609.20954

### 7.2 Deep RL with Buffered Quantile Objectives (Deep-BQRL)
- **Authors**: Mohammad Alipour-vaezi, Sajad Khodadadian
- **Affiliation**: not stated (inferred — Georgia State University-aligned optimization/risk-sensitive RL group)
- **Venue**: arXiv preprint (2609.21327, cs.AI / cs.LG), fresh Mon 21 Sep window
- **Key Innovations**: Risk-sensitive decision-making by optimizing a *lower-buffered quantile* of the return distribution (averaging nearby quantiles below the target — smooth, stable surrogate of the point quantile). **Deep-BQRL** makes buffered-quantile learning work **model-free with neural function approximation**: learns conditional return quantiles from transitions, constructs buffered action scores from the relevant quantile region, uses **ensemble disagreement for exploration**, and augments the input representation so the policy responds to trajectory information without the exact quantile-state recursion.
- **Results**: On asset-selling optimal stopping and **slippery FrozenLake**, Deep-BQRL attains smaller mean cumulative point-quantile policy gaps than tabular PPO/TRPO at the reported target levels (UCB-BQRL retains the smallest); learned stopping decisions vary interpretably with the target quantile.
- **Significance**: A deployable risk-averse RL that doesn't need an explicit world model — the toolkit for game/agent policies whose downside matters (bankroll management, no-tilt mode, "play safe when behind").
- **Link**: https://arxiv.org/abs/2609.21327

### 7.3 IncentRL: The Trade-Off Between Preference Guidance and Task Performance
- **Authors**: Xuening Wu, Yanlan Kang, Shenqin Yin
- **Affiliation**: not stated (inferred — Chinese academic reinforcement-learning group)
- **Venue**: arXiv preprint (2609.21525, cs.LG), fresh Mon 21 Sep window
- **Key Innovations**: Preference guidance (reward shaping) "may unintentionally change the task being optimized." **IncentRL** adds a **KL penalty between the specified outcome distribution and a preferred distribution**, and *characterizes* the distortion: an external-value perturbation bound, a **strict-action-gap condition** guaranteeing the original optimal policy survives, and the large-weight regime via discounted cumulative preference cost.
- **Results**: Theory illustrated on tied-optima and support-mismatch counter-examples; on **MiniGrid DoorKey-8x8**, a distance-proxy implementation with score-weighted coefficient search reaches **98% mean success after 2M training steps** (coefficient 0.01) vs **90.5%** for the zero-coefficient baseline, with search drifting to smaller coefficients.
- **Significance**: Reward shaping with *guard rails* — the formal statement of "nudge the agent, don't retask it," directly applicable to shaping rewards in game-RL loops where the external score (win the level) must not be distorted by auxiliary signals.
- **Link**: https://arxiv.org/abs/2609.21525

### 7.4 SynthDemo-RL: Breaking the Zero-Reward Barrier in VLA Adaptation with LLM-Guided Synthetic Demonstrations
- **Authors**: Hiroaki Kingetsu, Hiroaki Kurihara, Kaoru Yokoo, Kenji Fukumizu, Manohar Kaul
- **Affiliation**: not stated (inferred — Japan/IST-aligned (Fukumizu, Institute of Statistical Mathematics) + Kaul ML group)
- **Venue**: arXiv preprint (under review; 2609.21650, cs.RO / cs.AI), fresh Mon 21 Sep window
- **Key Innovations**: Fine-tuning VLAs on tasks with **zero successful trajectories** is the classic sparse-reward wall. **SynthDemo-RL** = automated teacher (simulator-privileged state → successful trajectories) → SFT-distill a VLA student → **PPO with binary task-success rewards** refines it. Introduces **reward coverage** (fraction of tasks with ≥1 observed success) as a complement to average success.
- **Results**: On **LIBERO-PRO** (perturbed tasks, no demonstrations): 27/57 tasks at 0% for the fine-tuned base; direct PPO rescues 10, **SynthDemo-RL rescues all 27 → 97.8%/97.1% average success** (Position/Task axes). On standard LIBERO: **96.0%** with no human demos, within 1.7 points of the 50-human-demo baseline; further validated on RoboTwin 2.0 and open-loop-executed on a physical robot.
- **Significance**: The "imitation-to-fill-the-buffer, RL-to-refine" pipeline that converts synthetic demos into robust play — the same pattern transfers to game-bot tasks where no expert plays exist and only a sparse win/lose signal is available.
- **Link**: https://arxiv.org/abs/2609.21650

---

## Runner-ups Worth a Look (grep-verified unclaimed)

- **2609.22086** Designer-RSI — evolving a *procedural memory* (natural-language skill bank) from 1,406 real design briefs with a frozen frontier model across 230+ design tools; 76→139 skills with no weight updates, GenEval2 execution success 72.7→99.3% for Claude-Sonnet-4 — the "externally-grown memory beats SFT" pattern for long-horizon creative agents. https://arxiv.org/abs/2609.22086
- **2609.21838** PopNavShift — matched simulation framework stress-testing social navigation under *pedestrian behavioral population shift* (persona-prompted motion profiles), 7,488 matched robot runs across 8 population conditions; time-pressure only reverses 8.6% of rankings by robot time but **22.4%/23.9% by pedestrian delay metrics** — evaluation-rank fragility under population shift, a caution for sim-based agent benchmarks. https://arxiv.org/abs/2609.21838
- **2609.21637** Chinese Competitive Debating Dataset & Benchmark — 148 matches / 2,698 stages / 20,542 exchange units with 3-judge professional adjudication under a shared rubric; winner-tendency, stage-score and best-debater tasks — a structured competitive-arena benchmark for LLM judgment of interaction-level gamesmanship. https://arxiv.org/abs/2609.21637

## Summary Statistics

| Category | Papers Count |
|----------|-------------|
| Game RL, Multi-Agent Learning & Game Theory | 5 |
| Game AI Bots, LLM Agents & NPC Simulation | 2 |
| Game Foundation Models, World Models & Game Agents | 4 |
| PCG & Automated Game Design | 0 new (sibling-covered: 2) |
| Game & Agent Benchmarks / Evaluation Suites | 2 |
| Industry Game AI, Sim-to-Real & On-Device Inference | 1 |
| Related RL Techniques | 4 |
| **Total featured papers** | **18** |

## Cross-references (covered by 09-21 sibling digests, not re-featured)

- 2609.21562 — GameLogicBench: Godot tick-level game-logic coding-agent benchmark (72 tasks / 1,451 cases, best 52.78%) — [arxiv-ai-search 09-21](../2026-09-21/arxiv-ai-search.md)
- 2609.21976 — MORM: multiplicative optimism for constant regret in general-sum games — [arxiv-ai-search 09-21](../2026-09-21/arxiv-ai-search.md)
- 2609.21944 — MEFPIA: matrix-exponential fixed-point iteration for quantum-game equilibria — [arxiv-ai-search 09-21](../2026-09-21/arxiv-ai-search.md)
- 2609.21064 — Colonel Blotto model of deterrence: information structure of defection — [arxiv-ai-search 09-21](../2026-09-21/arxiv-ai-search.md)
- 2609.21748 — "World Modeling in Transformers" (TaxiGPT): reasoning failures ≠ absent world model — [arxiv-daily 09-21](../2026-09-21/arxiv-daily.md)
- 2609.21293 — GameASG-Bench: autonomous software generation for game development (47 tasks / 12 genres) — [arxiv-daily 09-21](../2026-09-21/arxiv-daily.md)
- 2609.22055 — compositional continual-learning benchmark for world models — [arxiv-daily 09-21](../2026-09-21/arxiv-daily.md)
- 2609.21527 — OpenMAS-GCom: diagnostic benchmark for graph-enhanced multi-agent systems — [arxiv-daily 09-21](../2026-09-21/arxiv-daily.md)
- 2609.21378 — ArenaFlow: tournament-ranking hierarchical credit propagation for open-ended agent RL — [arxiv-daily 09-21](../2026-09-21/arxiv-daily.md)

## Key Themes

1. **The body is a game resource, and the game is learned through it.** DIC-Map (2609.21100) shows optimal strategy concentration is bounded by the responder's *physical* value of deferring; MAAP (2609.21929) shows teammates' bodies are also cameras. Game-level self-play is increasingly solving *executor-constrained* games, not abstract action spaces.

2. **Self-play's frontier moved from "more bootstrap" to "targeted post-training."** CounterPlay (2609.21617) reaches BehaviorBench SOTA over all eight traffic regimes with 1% of the anchor's transitions by counterfactually retrying failed episodes at earlier states — an efficiency result with direct analogue to esports scrimmage review and game-balance retraining cycles.

3. **World-model science matures into interventions and economics.** Skel-WAM (2609.21514) unlocks human videos/footage as world-model supervision; Sandwich-Residuals (2609.21740) adapts frozen WMs with 97–99% fewer parameters; 2609.21787 proves compact interventions survive as *moving* local geometry; 2609.21482 cuts offline WM training compute ~72% via uncertainty-adaptive rollouts; ZYT-World (2609.21712) makes it 107.7× real-time in an industry AD sim. From "can we learn it" to "how do we patch, serve, and deploy it."

4. **Belief as state, language as policy (again).** BCA (2609.21997) gives NPCs an explicit Bayesian belief layer with a stubbornness knob and auditable stance biases; BirdsongChat (2609.20887) separates reasoning agents from sim bodies via a Unified Parameter Representation. Social-simulation agents converge on the same "persistent, checkable inner state" design that the 09-20 digest flagged for game NPCs.

5. **Human-vs-AI measurement is now a first-class experimental design.** The escalation study (2609.21439) proves labels alter human play before the AI acts; CogGym (2609.21259) quantifies a real commonsense-vs-formal reasoning gap (best model R² 0.59 vs human 0.93); PopNavShift (runner-up) shows eval rankings are population-fragile. Evaluation of game AI against humans is becoming its own science.

6. **Dedup discipline note:** every featured ID (2609.21100–2609.21650) was grep-verified 0 hits in `wiki/` and sits outside all 09-21 sibling-claimed sets (full claimed-ID lists confirmed from arxiv-ai-search & arxiv-daily); the window's pure-game benchmark/GT marquee items are cross-referenced rather than duplicated.