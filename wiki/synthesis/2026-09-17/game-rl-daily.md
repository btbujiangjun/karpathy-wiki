---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-09-17)"
type: synthesis
created: 2026-09-17
updated: 2026-09-17
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, world-models, pcg, marl, self-play, benchmarks, industry-game-ai, game-theory, imitation-learning, robust-rl, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-09-17)

> **Methodology note**: The **Thu 17 Sep 2026 arXiv mailing** (`Showing new listings for Thursday, 17 September 2026`, Wed 16 Sep submissions, IDs **2609.17532–2609.19145**) is the freshest window; the same-day sibling digests — `arxiv-ai-search`, `conference-digest`, `tech-report-digest` — already ran in full against it and claimed the AI/rec/CTR/agent/venue-tagged content (incl. the window's headline game papers). This digest therefore mines the **unclaimed game-relevant remainder**: live parses of `/list/{cat}/new` for **cs.AI / cs.CL / cs.CV / cs.GT / cs.HC / cs.LG / cs.MA / cs.NE / cs.RO** (509 unique IDs in-window), title + abstract keyword sweep → 21 candidates screened → 15 curated. Every featured ID was **grep-verified 0 hits in `wiki/`** and sits outside the sibling-claimed 09-17 ID sets.
>
> **Continuity / already-covered by today's siblings (not re-featured):** **Gauntlet "Compiled Agency"** — frontier coding agents build their own StarCraft II / Freeciv / Flappy Bird players, zero model calls at play (2609.18996); **Zing-0.5** — 5B playable keyboard+text joint-control world model at 24 FPS / ~$0.009 per stream-minute (2609.17909); **Chess as Strategic-Reasoning Substrate** systematic mapping (2609.18286); **Long-Lived Characters, Local Inference** — incremental memory for local-game NPCs (2609.18935); **Changepoint-Aware World Models** — DreamerV3 + CUSUM dynamics-shift detector + stale-replay forgetting (2609.18950); **MARL price competition in shared spectrum** (2609.17754) → [arxiv-ai-search 09-17](../../2026-09-17/arxiv-ai-search.md); **Recursive Reasoning vs Statistical Extrapolation in Multi-Agent Games** — REE diagnostic, ICL ≈ statistical extrapolation in strategic games (2609.18591) → [conference-digest 09-17](../../2026-09-17/conference-digest.md).

---

## 1. Game RL & Multi-Agent Learning

### 1.1 Decentralized Optimal Equilibrium Learning Over Dynamic Networks
- **Authors**: Seref Taha Kiremitci, Muhammed O. Sayin
- **Affiliation**: Bilkent University lineage (inferred)
- **Venue**: arXiv preprint (2609.17601, cs.GT)
- **Key Innovations**: Decentralized learning of **socially-optimal equilibria in finite normal-form games** over *dynamic* communication networks. Each agent sees only its own realized payoffs, knows no model of the game, and talks only to time-varying neighbors over low-bandwidth channels. The proposal exchanges **randomized semantic content/discontent signals** (from local payoff comparisons) plus **time-stamped, time-stacked tables** instead of raw actions/payoffs/parameters — combining table fusion with **temporal majority reconstruction** to survive link churn while staying fully decentralized.
- **Results**: Finite-time **logarithmic regret** guarantees (with an in-phase exploration perturbation) for optimal-equilibrium selection under both utilitarian and proportional-fair social-welfare objectives; simulations show socially desirable equilibria are selected even under dynamic connectivity.
- **Significance**: A practical recipe for **distributed equilibrium selection** in systems where no node holds the payoff matrix — relevant to decentralized MARL for games and to coalition/pricing games run on sparse communication graphs.
- **Link**: https://arxiv.org/abs/2609.17601

### 1.2 CoRe-MARL: Cooperative Redistribution Under Unknown Dynamics Using Recurrent Multi-Agent Reinforcement Learning
- **Authors**: Naimur Rahman Chowdhury, Shatabdi Sen Prapti, Md. Salehin Seyam, Limon Bin Hossain
- **Affiliation**: not stated (inferred — South-Asia academic cluster)
- **Venue**: arXiv preprint (2609.18639, cs.LG)
- **Key Innovations**: Formulates decentralized **relief-supply redistribution between local centers** as a Dec-POMDP where each center is an agent that must smooth stock imbalances with limited information and disrupted transport. A **recurrent network** captures evolving supply/demand dynamics the actors never observe directly; **MAPPO** provides centralized-training/decentralized-execution (CTDE) with a recurrent critic.
- **Results**: Recurrent MAPPO reduces the service gap across centers and lifts the *worst-served* center's service while keeping network-wide service competitive vs recurrent IPPO and a local-only heuristic, and stays stable across diverse trajectory patterns.
- **Significance**: A clean example of the "egalitarian/welfare objective in decentralized team games" template — reusable for cooperative resource-allocation game environments and for team-game baselines in MARL libraries.
- **Link**: https://arxiv.org/abs/2609.18639

### 1.3 Social Laws for Multi-agent Coordination in Stochastic Environments
- **Authors**: Rolando Fernandez, Caleb Probine, Tyler Lee, Jeffrey Chen, Erez Karpas, Muhammad Arrasy Rahman, Peter Stone, Ufuk Topcu
- **Affiliation**: UT Austin (Stone, Topcu, Fernandez, Probine, Lee, Chen, Rahman) + Technion (Karpas) (inferred)
- **Venue**: arXiv preprint (2609.18929, cs.MA)
- **Key Innovations**: Prior "social laws" (restrictions agents agree to follow to avoid interference) assume **deterministic, goal-based** worlds. This paper extends social laws to **stochastic, reward-based environments**, defining **α-robustness** — the guaranteed utility each agent keeps while pursuing its *own optimal single-agent policy*, assuming everyone obeys the law — and verifies robustness by reducing to solving a series of MDPs.
- **Results**: Formal robustness verification for stochastic settings; empirical validation on toy environments.
- **Significance**: A principled handle on "who gives up what utility for cooperation" — directly applicable to coordinated game teams, traffic-style NP-fighting policies, and safe multi-agent bot design.
- **Link**: https://arxiv.org/abs/2609.18929

### 1.4 Epsilon-Nash Equilibria in History-Dependent SA-MDPs
- **Authors**: Brandon Gary Kaplowitz, Dominik Bohnet Zurcher, Akash Agrawal, Tala Jafari, Christian Schroeder de Witt, Paul W. Goldberg
- **Affiliation**: University of Oxford lineage (Goldberg, de Witt) (inferred)
- **Venue**: arXiv preprint (2609.18829, cs.GT)
- **Key Innovations**: State-adversarial MDPs (SA-MDPs) — where an adversary who knows the true state picks a perturbed observation within a proximity set each step — are treated as an **observation-space attack game**. Previous work assumed Markovian policies; here the solution concept is generalized to **history dependence**, proving there is **no universal (initial-state-distribution-agnostic) history-dependent equilibrium policy**, then giving the first algorithmic route to ε-approximate *initial-state-dependent* equilibria by reducing SA-MDPs to a strategically-equivalent constrained zero-sum **one-sided partially-observable stochastic game**.
- **Results**: Works on small analytically verifiable games and **scales to Atari Freeway rollouts** with a 12-period-ahead horizon.
- **Significance**: History-dependence breaking attacks' folklore assumptions matters for **adversarial robustness of game-playing RL agents** — and the constrained-POSG reduction is a reusable computational bridge.
- **Link**: https://arxiv.org/abs/2609.18829

### 1.5 Core Stability Recognition for Minimum-Cost Spanning Tree Games: A Parameterized Perspective
- **Authors**: Michal Dvořák, Ioannis Kakatelis, Dušan Knop
- **Affiliation**: Czech academic cluster (Dvořák, Knop) (inferred)
- **Venue**: arXiv preprint (2609.18807, cs.GT)
- **Key Innovations**: The minimum-cost spanning tree game (MSTG) — a cooperative network game where players share an edge-weighted tree connecting to a source — asks whether a payoff allocation is *stable* (in the core). Deciding **core non-membership is coNP-hard** in general; this paper maps the boundary: hardness is extended to graphs *very close to planar*, while on the positive side core recognition is **FPT by allocation support size**, and by treewidth / signed neighborhood diversity; kernelization gives a cubic kernel on planar graphs, quadratic on signed-NND, linear by feedback edge number.
- **Results**: Fixed-parameter tractability + kernel complexity results for MSTG core recognition.
- **Significance**: Algorithmic game theory for cooperative/coalitional settings — the kind of stability machinery used to design revenue-sharing and cost-sharing rules in game economies.
- **Link**: https://arxiv.org/abs/2609.18807

---

## 2. Game AI Bots & LLM Agents in Games

### 2.1 Clueing up LLMs with Tool-Augmented Deductive Reasoning
- **Authors**: Rebecca Ansell, Autumn Toney-Wails
- **Affiliation**: not stated (inferred — independent/academic)
- **Venue**: arXiv preprint (2609.18736, cs.AI)
- **Key Innovations**: Implements a **text-based, multi-agent version of the classic board game Clue** as an evaluation environment for multi-step, agentic deductive reasoning: agents must infer hidden information from a sequence of observations, keep consistency across turns, and reason over evolving logical constraints. Six LLM agents (GPT-4o-mini and Gemini-2.5-Flash) play baseline turn-based games, then a **tool-augmented variant converts implicit game state from reasoning logs into an explicit structured possibility matrix** — encoding extended-turn memory and deductive constraints *outside* the agent's context so the LLM only has to reason over the remaining possibilities.
- **Keywords**: Clue as a *strategic-reasoning environment with formal, checkable game state* — the possibility-matrix tool is a concrete answer to the "LLM game agents need external state" problem (see Gauntlet's empty-policy-file contract, 2609.18996, for the same theme at the systems level).
- **Results**: Tool augmentation supports reasoning quality and task success vs the baselines over repeated games.
- **Significance**: Role-playing/board-game LLM agents get a cheap, non-architectural memory+rules substrate; the Clue environment itself is reusable as a multi-agent deductive-reasoning benchmark.
- **Link**: https://arxiv.org/abs/2609.18736

### 2.2 TalkMatrix: Generating Character Dialogue that is Both Consistent and Diverse
- **Authors**: Ayuto Tsutsumi, Yuu Jinnai
- **Affiliation**: Preferred Networks lineage (Jinnai) (inferred)
- **Venue**: arXiv preprint (2609.19022, cs.CL) — v1 20 Jul 2026 (new to wiki)
- **Key Innovations**: Frames game character dialogue not as per-prompt decoding but as **structured multi-prompt, multi-completion selection**: given a candidate pool per (character × situation) cell, pick one completion per cell to optimize a *collection-level* objective — each character stays consistent across situations, each line fits its situation, and characters/situations stay distinguishable. **TalkMatrix** generates candidates for every cell and jointly selects the matrix via **four embedding-based consistency/diversity objectives**, maximized under a **two-level minimax** (worst-dimension) formulation solved by multi-start coordinate ascent.
- **Results**: On 50 synthetic role-playing scenarios + 25 curated board-game scenarios, LLM-as-a-judge ranks matrix-level selection higher than random / independent cell-level decoding baselines.
- **Significance**: A direct fix for the **"consistent yet diverse" NPC dialogue** problem — global selection instead of greedy per-line sampling, with game developer-grade board-game scenarios as the testbed.
- **Link**: https://arxiv.org/abs/2609.19022

---

## 3. Game Foundation Models & World Models

### 3.1 WAVE-Go: World-Model Navigation with Adaptive Execution for Wheel-Legged Robots
- **Authors**: Mingyi Li, Ji Li, Zhihao Ouyang, Yage He, Börje F. Karlsson
- **Affiliation**: Chalmers University of Technology lineage (Karlsson) (inferred)
- **Venue**: arXiv preprint (2609.18193, cs.RO)
- **Key Innovations**: World models predict the *consequences* of navigation actions, but predicted action sequences go stale mid-execution (dynamic obstacles, locomotion-mode changes). **WAVE-Go** decouples **world-action prediction from interruptible command execution**: the executor adaptively picks an *action prefix*, cancels pending commands when updated observations invalidate them, and gates posture/locomotion-mode transitions behind clearance/stability/task-evidence checks; prefix selection is formalized as **conditional risk under an estimated cumulative failure budget**.
- **Results**: 74.1% in-distribution / 63.3% dynamic-OOD image-goal navigation success (vs 4.7 / 7.7pp over the strongest baseline), collisions down from 4.4→2.9 per 100 m; vs fixed-4-command execution, +4.0pp success with **−51.2% replanning frequency** and −6.5% collisions.
- **Significance**: The "world model anticipates, executor interrupts" pattern is exactly the control loop game bots need when acting in live, drifting environments with world-model rollouts.
- **Link**: https://arxiv.org/abs/2609.18193

### 3.2 RiskWorld: Risk-Aware World Modeling with Flow-Guided Occupancy Evolution for Selective Trajectory Planning
- **Authors**: Rongxiang Zeng, Linsen Cai, Jiafu Zhang, Yijie Zhong, Yide Tao, Shuai Wang, Nan Zheng, Hai L. Vu, Alvaro Garcia Hernandez, Yongqi Dong
- **Affiliation**: driving-autonomy cluster (inferred)
- **Venue**: arXiv preprint (2609.18442, cs.AI / cs.ET)
- **Key Innovations**: A **risk-aware shared world model** that both forecasts occupancy and drives *selective* trajectory replacement in automated driving. Spatial risk fields + temporal actor context are fused with BEV features; **flow-guided evolution** transports occupancy/scene features and **signed residuals** correct post-transport error. One forecast per planning step is **reused across candidates** (cheap marginal evaluation), each candidate is scored against a current-state persistence reference, and the planned anchor is replaced only when predicted risk triggers intervention AND an alternative satisfies component-wise risk/trajectory-error constraints.
- **Results**: Lowest collision rate at a 3 s evaluation horizon on nuScenes + second-best average L2 error among SOTA baselines, at **11.5 FPS on one RTX 4090 with 90.81 M params**.
- **Significance**: Real-time, single-card safety-conditioned world modeling with selective re-planning — a deployable blueprint for game-engine NPC behavior under collision/risk budgets.
- **Link**: https://arxiv.org/abs/2609.18442

---

## 4. Industry Game AI, Gamified Data & Simulators

### 4.1 From Gameplay to Policy: Towards Scalable Robot Data Collection via Gamified Robot-Free Interaction
- **Authors**: Zheng Li, Liang Zhu, Junzhe Wang, Huayuan Chen, Ziyun Liu, Jiahang Cao, Xinyu Sheng, Pei Qu, Yufei Jia, Ximeng Zhang, Jiarui Xie, Zizhao Yuan, Haoang Li, Yi Cai, Jinni Zhou, Jun Ma
- **Affiliation**: SJTU / CUHK lineage (Li Haoang, Ma Jun) (inferred)
- **Venue**: arXiv preprint (2609.18650, cs.RO)
- **Key Innovations**: **Project Kitchen** turns robot data collection into a **VR-based gamified, robot-free egocentric gameplay experience** (inspired by how games sustain long-term engagement): players perform goal-directed manipulation in VR without any robot hardware, so collection crowdsources at scale and transfers across embodiments. **Game2Policy** then bridges game-to-real by extracting **embodiment-invariant affordance cues (contact points, sub-goal states)** from gameplay trajectories, pre-training an affordance model on game data, and jointly fine-tuning it with downstream policies on a *handful* of real-robot demos.
- **Results**: +10.0 points average success in simulation and **+18.3 points on real robots in the few-shot setting**; user studies confirm engagement + behavioral diversity.
- **Significance**: Gaming mechanics as a *data-collection engine* for policy learning — the strongest "gameplay-as-infrastructure" paper this window, with direct copyable patterns for industry game-AI data pipelines.
- **Link**: https://arxiv.org/abs/2609.18650

### 4.2 Imitation Learning for Autonomous Driving in CARLA
- **Authors**: Jordy Kieto
- **Affiliation**: not stated (inferred — independent researcher using the CARLA open simulator)
- **Venue**: arXiv preprint (2609.17757, cs.AI / cs.RO)
- **Key Innovations**: A careful **behavioral-cloning competence study** in the game-engine simulator CARLA: a compact **1.36 M-parameter multimodal policy** (five-frame RGB+LiDAR+telemetry+waypoint histories → throttle/brake/steering at 20 Hz) trained only on offline autopilot demonstrations (236,882 windows ≈ 3.3 h driving, 448 captures, systematic route-generation with spawn-point enumeration and route verification).
- **Results**: Drives autonomously for hours on training and held-out routes (no collisions in reported runs), transfers qualitatively to an unseen town with different road geometry, and shows large-deviation recovery; ships code, checkpoint, ONNX model, data sample and an **evidence audit** distinguishing measured vs qualitative claims.
- **Significance**: A rigor exemplar for sim-trained game/vehicle closing-the-loop — how to report offline-vs-closed-loop claims honestly, plus a reusable CARLA behavior-cloning baseline for vehicle-game bots.
- **Link**: https://arxiv.org/abs/2609.17757

---

## 5. Related RL Techniques (Robust RL, Model-Based RL, Imitation Learning)

### 5.1 Online Robust Reinforcement Learning Through Monte-Carlo Planning
- **Authors**: Tuan Dam, Kishan Panaganti, Brahim Driss, Adam Wierman
- **Affiliation**: Caltech lineage (Wierman) (inferred)
- **Venue**: arXiv preprint (2609.18599, cs.LG)
- **Key Innovations**: MCTS achieves its fame in Chess/Go/Shogi by assuming the simulator matches the world — which fails in low-fidelity game/robotics sims. This **robust MCTS** accounts for ambiguity in *transition dynamics and reward distribution* simultaneously: a **robust power-mean backup operator** plus designed exploration bonuses give finite-sample convergence at every tree node.
- **Results**: Root-node value estimation converges at **O(n^−1/2)**, matching standard MCTS order, with strong empirical robustness under significant reward/transition ambiguity.
- **Significance**: Simulation-based planning that stays calibrated when the sim drifts from reality — directly relevant to game agents trained in sims being deployed against real capturable dynamics.
- **Link**: https://arxiv.org/abs/2609.18599

### 5.2 Characterizing Replay Retention Under Dynamics Shift in Model-Based Reinforcement Learning
- **Authors**: Everest Yang, Skye Thompson, George D. Konidaris
- **Affiliation**: Brown University (Konidaris) (inferred)
- **Venue**: arXiv preprint (2609.18167, cs.RO)
- **Key Innovations**: **Continual MBRL**, where physics/mechanics change mid-career (a frequent event in games when patches, maps or character physics change), must decide whether to keep old replay. The paper characterizes the decision with two quantities — **change magnitude** and **age-staleness AUC** (how well transition age separates stale from fresh) — and shows replay-retention policy is not one-size-fits-all: forgetting stale data helps after large permanent shifts but *hurts* when dynamics recur.
- **Results**: Effects tested across two locomotion morphologies, two MBRL algorithms, and Real-World RL benchmark perturbations; an interaction-data estimator can provide the quantities needed to choose a retention strategy after permanent shifts.
- **Significance**: The "how much of the old experience to keep after a rule change" question maps 1:1 onto **game-agent retraining when game balance/mechanics change** — a practical rulebook for skill retention.
- **Link**: https://arxiv.org/abs/2609.18167

### 5.3 Missing Bridges: Composition-Aware Active Imitation Learning
- **Authors**: Maxwell J. Jacobson, Ahmed H. Qureshi, Yexiang Xue
- **Affiliation**: Purdue University (Qureshi, Xue) (inferred)
- **Venue**: arXiv preprint (2609.18004, cs.AI / cs.RO)
- **Key Innovations**: Active IL usually requests demos with highest *information gain about the expert policy*, ignoring composability. **AALT (Adaptive Agents via Latent Topologies)** instead requests demos that maximize **expected gains in start–goal connectivity**, organizes obtained demos into a latent topology of hub states connected by learned behaviors, and identifies **bridge demonstrations** that unlock many tasks at once (formally tied to task-reachability information gain); inference plans through the topology and conditions a diffusion policy on successive hub transitions.
- **Results**: In a simulated UR5e ordered-retrieval domain with 72 tasks, AALT climbs from 42/72 to **72/72 tasks using only 3 demonstrations (5 transitions)** beyond the initial dataset — vs the best baseline needing 98 transitions for 88.6%.
- **Significance**: Order-of-magnitude expert-effort reduction in structured multi-task domains — the composability idea transfers to game-skill libraries where one demonstration teaches many levels/units.
- **Link**: https://arxiv.org/abs/2609.18004

### 5.4 Learning to Stack: Cube-Stacking Imitation Learning from Virtual Reality Demonstrations
- **Authors**: Gryffin Reizian, Jordan Dowdy, Jean Chagas Vaz
- **Affiliation**: Arizona State University lineage (Vaz) (inferred)
- **Venue**: arXiv preprint (2609.19040, cs.RO) — v1 20 Jul 2026 (new to wiki)
- **Key Innovations**: A VR→sim **demonstration re-use pipeline** built on NVIDIA Isaac Sim/Isaac Lab: an operator wearing an HTC Vive Pro 2 + Manus Quantum gloves provides SE(3) end-effector commands; recorded trajectories are **replayed and re-rendered under new sensor/state configurations**, so one teleoperated session yields many demonstrations (task-space→joint-space conversion decoupled from dataset construction).
- **Results**: 200 virtual demos collected in 30 minutes (vs 45 real-world), plus 100 Isaac Mimic samples; a LeRobot-style dual-camera behavior-cloning policy trains from the virtual set and is evaluated in simulation.
- **Significance**: "One human session, many sim demos" — a data-amplification pattern applicable to game-engine training pipelines where real-time rendering makes re-rendering cheap.
- **Link**: https://arxiv.org/abs/2609.19040

---

## Summary Statistics

| Category | Papers Count |
|----------|-------------|
| Game RL, MARL & Game Theory | 5 |
| Game AI Bots & LLM Agents in Games | 2 |
| Game Foundation Models & World Models | 2 |
| Industry Game AI, Gamified Data & Simulators | 2 |
| Related RL Techniques | 4 |
| **Total featured papers** | **15** |

## Cross-references (covered by today's sibling digests, not re-featured)

- 2609.18996 — Gauntlet "Compiled Agency": coding agents self-build winning SC2/Freeciv/Flappy Bird players, zero model calls at play — [arxiv-ai-search 09-17](https://arxiv.org/abs/2609.18996)
- 2609.17909 — Zing-0.5: 5B playable world model, joint keyboard+text control, 24 FPS / $0.009 per stream-minute — [arxiv-ai-search 09-17](https://arxiv.org/abs/2609.17909)
- 2609.18286 — Chess as Strategic-Reasoning Substrate: 84-family systematic mapping (humans/engines/LLMs/hybrids) — [arxiv-ai-search 09-17](https://arxiv.org/abs/2609.18286)
- 2609.18950 — Changepoint-Aware World Models: DreamerV3 + CUSUM + stale-replay forgetting (RSS'26 workshop) — [arxiv-ai-search 09-17](https://arxiv.org/abs/2609.18950)
- 2609.18935 — Long-Lived Characters, Local Inference: incremental memory maintenance for local-game NPCs — [arxiv-ai-search 09-17](https://arxiv.org/abs/2609.18935)
- 2609.17754 — Learning Market Competition in Shared Spectrum (MARL for price/quantity competition) — [arxiv-ai-search 09-17](https://arxiv.org/abs/2609.17754)
- 2609.18591 — Recursive Reasoning or Statistical Extrapolation? ICL in Multi-Agent Interdependent Decision-Making (REE diagnostic) — [conference-digest 09-17](https://arxiv.org/abs/2609.18591)

## Key Themes

1. **The window's game headline belongs to siblings — and it is "agents that build the player"**: Gauntlet's compiled-agency agents (2609.18996), Zing-0.5's 24 FPS playable world model (2609.17909), and the chess mapping (2609.18286) are the flagship results of the Thu-17 batch; this digest supplies the *technical substrate* beneath them — externalized game-state tools for deductive-reasoning agents (Clue 2609.18736), matrix-level dialogue selection for NPCs (2609.19022), and world models that re-plan under risk/failure budgets (WAVE-Go, RiskWorld).

2. **"Gamified data" becomes an infrastructure thesis**: Project Kitchen (2609.18650) turns robot-demo collection into VR gameplay with +18.3 pts real-robot few-shot gains; CARLA behavior cloning (2609.17757) and cube-stacking VR re-rendering (2609.19040) round out a "one session → many sim demos → few-shot real transfer" pipeline family — the industry-game-AI angle of the window.

3. **Equilibrium/game-theory work stays formal and decentralized**: decentralized optimal-equilibrium learning on dynamic networks (2609.17601), social laws for stochastic multi-agent coordination (Stone/Topcu, 2609.18929), history-dependent adversarial equilibrium computation that scales to Atari Freeway (2609.18829), and FPT core-stability recognition for MSTG (2609.18807) — a lean but rigorous game-theory slot.

4. **Dedup discipline note**: every one of the 15 featured IDs (≥ 2609.17601) is ≥ the 09-16 coverage ceiling (2609.17527) and was grep-verified 0 hits in `wiki/`; the window's marquee game papers were deliberately left to the sibling digests and cross-referenced rather than duplicated.