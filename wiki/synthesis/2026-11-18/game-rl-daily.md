# Game RL & Game AI Bot — Daily Paper Digest (2026-11-18)

- **Date**: 2026-11-18
- **Window**: ~2026-11-12 → 2026-11-17 (freshest arXiv submissions/revisions and arXiv-exposed venue metadata available at query time; arXiv Export API feed timestamp 2026-11-18T02:19Z)
- **Scope**: Game RL and strategic/multi-agent learning in classic and procedural game environments; LLM/VLM-powered game agents, code-as-policy agents, NPC/social-agent frameworks and real-time autonomous gameplay; game foundation/world models and industry game-AI systems; procedural content generation and game-level synthesis; game-based agent evaluation and game/world-state benchmarks; and related techniques (self-play/fictitious play, MCTS exploration, safe/in-context RL, imitation and model-based RL).
- **Method note**: Discovery used 27 keyword queries plus ten date-bounded (`submittedDate:[20261112 TO 20261118]`) topic/category sweeps against the arXiv Export API over HTTPS on 2026-11-18 (~2,000 unique pooled records screened to 333 fresh non-baseline candidates); `websearch` was unavailable in this run, so recent non-arXiv proceedings coverage is limited to venue/status metadata exposed on arXiv and PDF first pages. Every included ID was grep-verified as absent from the whole-wiki baseline of **10,489** arXiv IDs previously recorded anywhere under `wiki/` (including all prior `game-rl-daily.md` digests and today's sibling syntheses). Paper metadata, abstracts, venues, affiliations, and reported results are taken from arXiv abstract pages and PDF first pages (pypdf) and are **author-reported** unless noted. Affiliations were PDF-verified for 12/13 papers; the one exception is marked accordingly.
- **Active preference file**: `EXTEND.md` (repo root).

## Executive Summary

This window's strongest signal is **industry-built, real-time game-world models and gameplay agents**: Microsoft Cambridge's data-efficient real-time world models (2611.22497) reach a **79× inference speedup** trained on just ~28 hours of gameplay; LIGHTSPEED/Tencent's LightAct (2611.21065) turns **1,024 decision roots from a single source game** into +23.6/+29.2/+13.0 pp progress gains at 2B/4B/9B scales across 170 GameWorld tasks (34 games); and a TCG Crest replication (2611.20953) shows Claude repairing Atari/LunarLander policies from weights alone and writing a 9×9 Go network that beats three PPO opponents in 85–94% of games. **Generalization via reusable program artifacts** recurs: Komorebi AI's Craftax goal compiler (2611.19537) reaches 50% final-stage arrival vs <1% for episode-return feedback and transfers zero-shot to longer tasks. **Evaluation is getting more mechanism-aware**: ACM MM 2026 Oral ALIVE-Bench (2611.20956) scores VLM social agents across perception/understanding/influence/outcome with counterpart states aligning ρ≈0.72 with human judgments; EyeHeight (2611.21782, Nanjing U) shows all six open interactive-video world models regress toward human eye level; and FlipTest (2611.19822, Google DeepMind) finds the best of 11 video world models at 18.3% minimal-pair accuracy — **below the 25% random baseline**. **PCG** is represented by a physics-aware PCGRL framework for complex platformers (2611.22250, HIT/HKU). **Related techniques** span certified Nash Q-learning for jump-diffusion games (2611.21272), a geometric analysis of nonlinear fictitious play (2611.17286, UMD), safe in-context RL distillation (2611.21524, UVA), and learned pseudo-counts for MCTS (2611.22301, Fudan/Meituan).

---

## 1) Game RL, Strategic Learning, and Multi-Agent Dynamics

### Continuation-Guided LLM Evolution of Program Policies and Goal Compilers in Craftax
- **Title (EN)**: Continuation-Guided LLM Evolution of Program Policies and Goal Compilers in Craftax
- **Authors**: Víctor Gallego
- **Affiliation**: Komorebi AI Technologies (PDF first page)
- **Venue/conference**: arXiv preprint ("Preprint"; 17 pages); code: github.com/vicgalle/craftax-program-policies
- **Date**: 2026-11-14 (v1)
- **Abstract**: Coding agents can synthesize and optimize code-based policies from simulator feedback, so the deployed program acts with zero inference-model calls. For long-horizon tasks two problems arise: local improvements can hurt final success, and a new objective requires another expensive synthesis run. The paper develops competence through a *feedback cascade* — from episode returns to hierarchical goals and belief updates scored densely from the simulator. In Craftax (a partially observed, procedurally generated survival game), refinement on episode-level feedback stalls below 1% final-level arrival, while the cascade reaches the final stage 50% of the time (28% final-boss defeats). The controller is then factored into an environment interpreter *I* (models, memory, skills) and a rule program *p₀*, and coding agents optimize a reusable goal compiler *Cθ* mapping structured tasks *g* to new rule programs *p_g*. Across five compiler searches trained only on short tasks, the compilers transfer zero-shot to longer tasks with no task-specific tuning and no inference-time LLM calls (author-reported).
- **Key innovations**:
  - **Dense continuation-scored feedback cascade**: episode returns → hierarchical goals → belief updates makes long-horizon code-policy search tractable (<1% → 50% final-stage arrival).
  - **Interpreter/rule-program factorization**: separates reusable environment machinery from an editable rule program, enabling objective switching without re-synthesis.
  - **Learned goal compiler**: five independent compiler searches trained on short tasks transfer zero-shot to long tasks with no LLM calls at inference.
  - **Neuro-symbolic division of labor**: expensive offline search, cheap/auditable program execution at deployment — directly relevant to training-free, interpretable game bots.
- **Links**: [arXiv](https://arxiv.org/abs/2611.19537) | [PDF](https://arxiv.org/pdf/2611.19537)

### Certified Nash Equilibrium Learning for Nonzero-Sum Jump-Diffusion Games: Policy Iteration and Off-Policy Q-Learning
- **Title (EN)**: Certified Nash Equilibrium Learning for Nonzero-Sum Jump-Diffusion Games: Policy Iteration and Off-Policy Q-Learning
- **Authors**: Pengwei Wang; Na Li; Jiacheng Fan; Tielong Shen; Zuo Quan Xu
- **Affiliation**: Shandong University of Finance and Economics; Dalian University of Technology; The Hong Kong Polytechnic University (PDF first page)
- **Venue/conference**: arXiv preprint (31 pages, 3 figures)
- **Date**: 2026-11-16 (v1)
- **Abstract**: The paper establishes two model-free RL methods for infinite-horizon *N*-player linear-quadratic nonzero-sum stochastic differential games whose drift, Brownian diffusion, and Poisson jump amplitudes all depend on players' controls — control dependence in diffusion/jump terms couples simultaneous feedback updates. A verifiable certificate guarantees the partially model-free policy-iteration map is contractive on an invariant closed ball around an admissible initial feedback profile; all iterates are mean-square stabilizing and converge locally geometrically to closed-loop Nash feedback gains and value matrices. To implement updates from data, an off-policy Q-learning algorithm reuses the same behavior-policy data across iterations without knowing system coefficients or jump intensity. Under quantitative persistence of excitation and a common initialization, exact population regression reproduces the policy-iteration sequence, so the same local convergence guarantee applies at the population level; simulations validate both algorithms (author-reported).
- **Key innovations**:
  - **Certified convergence for coupled control-dependent noise**: a checkable contractivity certificate gives mean-square stability of *all* iterates and local geometric Nash convergence.
  - **Fully model-free off-policy Q-learning** for nonzero-sum games with Poisson jumps, requiring neither dynamics coefficients nor jump intensity.
  - **Population-regression equivalence** ties data-driven Q-learning to the certified policy-iteration sequence.
  - **Game-RL theory relevance**: extends model-free Nash-learning guarantees beyond purely drift-coupled games to jump-diffusion settings.
- **Links**: [arXiv](https://arxiv.org/abs/2611.21272) | [PDF](https://arxiv.org/pdf/2611.21272)

### Fictitious Play When Agents Are Not Expected-Utility Maximizers: A Geometric Analysis in 2-Action Games
- **Title (EN)**: Fictitious Play When Agents Are Not Expected-Utility Maximizers: A Geometric Analysis in 2-Action Games
- **Authors**: Hao Liang; Solaleh Mohammadi; Kaiqing Zhang
- **Affiliation**: University of Maryland, College Park (PDF first page)
- **Venue/conference**: arXiv preprint (79 pages; cs.GT)
- **Date**: 2026-11-12 (v1)
- **Abstract**: Fictitious play (FP) is a canonical model of independent learning in repeated games, where each agent best-responds to the empirical distribution of opponents' past actions under *expected* payoff. Learning agents may instead use nonlinear evaluation functionals (e.g., risk measures) to account for opponent-induced uncertainty. This paper studies nonlinear fictitious play (NL-FP), where each pure action is evaluated by a general functional of the payoff distribution induced by the opponent's empirical belief. It identifies a *single-crossing property* (SCP) of evaluation functionals that preserves the classical FP geometry in 2×2 games, and gives a novel geometric convergence analysis even when SCP fails. Beyond 2×2, NL-FP convergence can fail even in continuous time when the two-action player uses CVaR in a 2×3 game; a finite-crossing condition is identified that ensures convergence of both continuous-time dynamics and discrete-time iterates in general 2×*n* games (author-reported).
- **Key innovations**:
  - **Nonlinear-evaluator fictitious play**: generalizes the classic self-play/fictitious-play model to risk-sensitive and other nonlinear agent objectives.
  - **Single-crossing property** preserving classical FP geometry in 2×2 games, with convergence analysis when it fails.
  - **Negative result**: CVaR-based players can break even continuous-time NL-FP convergence in 2×3 games.
  - **Finite-crossing condition** giving a new convergence criterion for general 2×*n* games and insight into classical FP's global landscape.
- **Links**: [arXiv](https://arxiv.org/abs/2611.17286) | [PDF](https://arxiv.org/pdf/2611.17286)

---

## 2) Game AI Bot: LLM/VLM Agents, Code-as-Policy, and Autonomous Gameplay

### What Makes a Good Move? Learning to Act from Experience in Visual Worlds (LightAct)
- **Title (EN)**: What Makes a Good Move? Learning to Act from Experience in Visual Worlds
- **Authors**: Cehao Yang; Ziyi He; Jing Yi; Jian Guo; Hui Xiong
- **Affiliation**: HKUST(GZ); HKU; LIGHTSPEED; IDEA Research (PDF first page; first author's work done during a LIGHTSPEED internship)
- **Venue/conference**: arXiv preprint (15 pages)
- **Date**: 2026-11-16 (v1)
- **Abstract**: Visual policies must turn interaction experience into guidance for individual decisions: trajectory outcomes obscure action quality, and unguided exploration revisits familiar states. LightAct connects skill-guided exploration with policy internalization. Interaction segments are summarized into experience entries and consolidated into a *game-specific skill* that steers root collection toward broader state coverage. At each root, candidate actions are compared by short rollouts under a shared frozen policy; environment-reported score gains are averaged across continuations and normalized into relative action rewards, yielding reusable RL supervision. Training uses only 1,024 decision roots from a single source game. Across 170 GameWorld tasks spanning 34 games, LightAct improves overall progress by 23.6, 29.2, and 13.0 percentage points at 2B, 4B, and 9B scales, with the strongest model competitive with reported proprietary-model results (author-reported).
- **Key innovations**:
  - **Relative action rewards from short rollouts**: converts environment score gains into dense, reusable per-action supervision instead of sparse trajectory outcomes.
  - **Skill-guided root collection**: a game-specific skill consolidated from experience entries broadens visited-state coverage before RL.
  - **Extreme data efficiency**: 1,024 decision roots from one source game generalize to 170 tasks / 34 games.
  - **Scale study + strong proprietary parity**: gains at 2B/4B/9B with the 9B model competitive with much larger proprietary VLMs; ablations confirm gains across three policy optimizers.
- **Links**: [arXiv](https://arxiv.org/abs/2611.21065) | [PDF](https://arxiv.org/pdf/2611.21065)

### Same Fix, Different Weights: Replicating Weight-Space Programming with Claude
- **Title (EN)**: Same Fix, Different Weights: Replicating Weight-Space Programming with Claude
- **Authors**: Subham Kundu
- **Affiliation**: TCG Crest (PDF first page)
- **Venue/conference**: arXiv preprint (61 pages; ten pre-registered experiments)
- **Date**: 2026-11-16 (v1)
- **Abstract**: This paper re-runs the core of a reported weight-space-programming study with Claude Opus 5.5 on networks trained in Gymnasium, the Arcade Learning Environment, and a 9×9 Go engine, using pre-registered grading, untrained-network and hidden-unit-permutation controls, and hand audits of every sandboxed code cell. Reading was mixed: Claude named 3 of 4 Atari games from policy weights (14/20 attempts) but its training-data claims often followed priors. One-shot weight edits took a failing MountainCar policy from 0% to 100% success and a hovering LunarLander policy from 0% to 85.6%; zero-shot networks beat PPO at 100k steps on 4 of 5 environments, each implementing a textbook controller. Given 9×9 Go rules, no training, and no forward passes, Claude wrote a 1.48M-parameter Go network winning 85–94% of 128 games against each of three PPO opponents. Every edit acted at the output layer (final-norm scaling raising effective sampling temperature; logit shifts on "Wait"/`</think>`), unlike the original's internal-loop edit (author-reported).
- **Key innovations**:
  - **Independent pre-registered replication** of training-free, LM-written network weights for game policies, with controls and code audits.
  - **Concrete game results from weights alone**: Atari-game identification, MountainCar 0→100%, LunarLander 0→85.6%, zero-shot policies beating 100k-step PPO on 4/5 envs.
  - **Compiled Go player**: a 1.48M-parameter 9×9 Go network written with no training or forward passes beats three PPO opponents 85–94%.
  - **Mechanistic caution**: the "fix" is output-logit/norm rescaling rather than an internal algorithmic change — successful edits reduce to textbook controllers, delineating the scope of weight-space programming.
- **Links**: [arXiv](https://arxiv.org/abs/2611.20953) | [PDF](https://arxiv.org/pdf/2611.20953)

---

## 3) Game Foundation Models, World Models, and Industry Game AI

### Towards Data-Efficient, Real-Time World Models
- **Title (EN)**: Towards Data-Efficient, Real-Time World Models
- **Authors**: Raluca Stevenson; David Bignell; Jennifer C. White; Tabish Rashid; Emanuele Aiello; Mariya Hendriksen; Junha Hyung; Sadegh Aliakbarian; Abdelhak Lemkhenter; Marko Tot; Katja Hofmann; Sarah Parisot
- **Affiliation**: Microsoft, Cambridge, United Kingdom (PDF first page)
- **Venue/conference**: arXiv preprint (18 pages, 12 figures; includes supplementary material)
- **Date**: 2026-11-17 (v1)
- **Abstract**: World models can generate gameplay sequences consistent with user-input actions, but high-quality consistent generation typically costs inference speed and enormous training data, blocking real-time interactive play and custom training. This work targets both: it replaces next-token prediction with a two-stage discrete-diffusion approach using a lightweight refinement transformer that performs iterative masked predictions. Building on an autoregressive world model capable of consistent multi-minute sequences (Kanervisto et al., 2025), it achieves a **79× model speed-up** with a modest quality trade-off, and reproduces high-quality consistent gameplay from roughly **one day (28 hours)** of gameplay data. The authors frame this as removing barriers to real-time inference and data-efficient customization for creative/game-development uses (author-reported).
- **Key innovations**:
  - **Two-stage discrete diffusion for world models**: iterative masked prediction replaces next-token generation, enabling large inference speedups.
  - **79× speedup** over a strong autoregressive gameplay world model with modest quality loss — a concrete step toward playable, real-time interaction.
  - **28-hour data regime**: high-quality, minute-scale consistent gameplay from ~1 day of data, making custom world-model training practical.
  - **Industry game-AI signal**: a full Microsoft Cambridge system aimed at real-time interactive play and game-development ideation.
- **Links**: [arXiv](https://arxiv.org/abs/2611.22497) | [PDF](https://arxiv.org/pdf/2611.22497)

### Perception into Imagination: Executable Memory for World Models
- **Title (EN)**: Perception into Imagination: Executable Memory for World Models
- **Authors**: Xianyao Li; Ruitong Tian; Rui Min; Fang Xu; Jing Du
- **Affiliation**: Not stated in arXiv metadata or on PDF first page (verify from full text)
- **Venue/conference**: arXiv preprint (18 pages, 6 figures, 15 tables)
- **Date**: 2026-11-17 (v1)
- **Abstract**: Agents must reuse facts they saw or touched after visibility/contact is lost, and their own actions change the implications of those facts. Executable perceptual memory (EPM) advances explicit perceptual state alongside neural latent dynamics during imagination, and its evolving read-out informs reward prediction, value estimation, and policy learning. Reward inputs are aligned with the transitions that produced them, and the reward head is supervised on open-loop rollouts of recorded actions. On Memory Maze 13×13, EPM reaches 30.37 return at 1M interactions vs 23.37 when the same read-out informs only policy/value (+7.00, CI [3.80, 10.21]); it also improves control on 9×9 and MiniWorld, with probes showing stronger reward anticipation for remembered out-of-view arrivals (author-reported).
- **Key innovations**:
  - **Executable perceptual memory**: remembered facts are advanced by candidate actions inside imagined rollouts, not just stored passively.
  - **Reward-grounded memory readout**: memory feeds reward prediction/value learning, with rewards aligned to their generating transitions and supervised on open-loop rollouts.
  - **Quantified gain in memory game environments**: +7.00 return on Memory Maze 13×13 plus gains on 9×9 and MiniWorld.
  - **Model-based RL relevance**: connects persistent perception to predicted consequences and learning signals for world-model planning.
- **Links**: [arXiv](https://arxiv.org/abs/2611.22294) | [PDF](https://arxiv.org/pdf/2611.22294)

---

## 4) Procedural Content Generation and Game Creation

### PCGRL for Complex Platformers: Synthesizing Playable and Diverse Levels via Inflated Envelopes and Forward Curricula
- **Title (EN)**: PCGRL for Complex Platformers: Synthesizing Playable and Diverse Levels via Inflated Envelopes and Forward Curricula
- **Authors**: Di Wu
- **Affiliation**: Harbin Institute of Technology (currently with The University of Hong Kong; PDF first page)
- **Venue/conference**: arXiv preprint (9 pages, 6 figures, 1 table)
- **Date**: 2026-11-17 (v1)
- **Abstract**: PCG via reinforcement learning suffers exploration bottlenecks and scaling limits on long-sequence generation governed by strict rigid-body rules and non-linear kinematic boundaries (platformer constraints), often failing to keep large levels solvable. The paper presents a physics-aware, curriculum-guided PCGRL framework. An "Inflated Volume Envelope" embeds continuous kinematic feasibility into the discrete MDP state space; intermediate state-transition feedback plus a multi-stage forward-extension curriculum eases sparse rewards and stabilizes long-horizon credit assignment; and high-entropy stochastic inference with post-hoc parallel rejection filtering counters the monotonous maps of converged deterministic policies. Across multi-scale canvases the framework improves structural diversity while maintaining physical playability and converges reliably where PCGRL baselines degrade (author-reported).
- **Key innovations**:
  - **Inflated Volume Envelope**: physics-constrained MDP representation that carries continuous kinematic feasibility into discrete level editing.
  - **Forward-extension curriculum + transition feedback**: makes extremely long PCG action sequences learnable under sparse solvability rewards.
  - **Diversity-preserving synthesis**: high-entropy stochastic inference with parallel rejection filtering avoids monotonic "safe" level collapse.
  - **Scalability**: maintains solvability and convergence stability on large canvases where standard PCGRL breaks down.
- **Links**: [arXiv](https://arxiv.org/abs/2611.22250) | [PDF](https://arxiv.org/pdf/2611.22250)

---

## 5) Game Benchmarks, Evaluation, and Game/World-State Perception

### From Vision to Interaction: Evaluating Dynamic Social Intelligence of VLM Agents in ALIVE-World (ALIVE-Bench)
- **Title (EN)**: From Vision to Interaction: Evaluating Dynamic Social Intelligence of VLM Agents in ALIVE-World
- **Authors**: Yue Xu; Xiaoyu Qin; Sihan Zhao; Ze-en Xiong; Jia Jia
- **Affiliation**: Tsinghua University; BNRist; Key Laboratory of Pervasive Computing, Ministry of Education (PDF first page)
- **Venue/conference**: ACM Multimedia 2026 (MM '26) — Oral Presentation, Outstanding Paper Award; DOI 10.1145/3767308.3836378
- **Date**: 2026-11-16 (v1)
- **Abstract**: Existing social-intelligence evaluations fragment the skill into text abstractions, static tasks, or embodied simulators lacking social dynamics. ALIVE-World is an embodied simulation environment with dynamic multimodal interaction — egocentric vision, language, and non-verbal action — populated by counterpart agents driven by a profile-conditioned dual-system (intuitive-affective + logical-cognitive) architecture; their internal states align with human judgments (ρ≈0.72). ALIVE-Bench turns assessment into a trackable quantitative framework grounded in environmental states and agent internals, scoring VLM agents on perception, understanding, influence, and outcome. Experiments show dynamic social intelligence is multi-dimensional and scenario-dependent, and reveal a critical bottleneck between upstream perception and downstream social intervention (author-reported).
- **Key innovations**:
  - **Dynamic embodied social simulation**: concurrent multimodal actions (locomotion, gesture, gaze, speech) with socially reactive, dual-system counterpart agents/NPCs.
  - **Transparent four-dimension benchmark**: perception / understanding / influence / outcome scored from hidden environment and agent state, not just text.
  - **Human-aligned counterpart states**: ρ≈0.72 agreement with human judgments supports use as social feedback.
  - **Diagnosed perception→intervention gap**: identifies a bottleneck separating VLMs' social reading from effective embodied influence.
- **Links**: [arXiv](https://arxiv.org/abs/2611.20956) | [PDF](https://arxiv.org/pdf/2611.20956)

### Every Camera Grows Up: Camera-Height Regression in Interactive Video World Models (EyeHeight)
- **Title (EN)**: Every Camera Grows Up: Camera-Height Regression in Interactive Video World Models
- **Authors**: Sheng Lu; Guangpin Tao; Tong Lu; Ying Tai
- **Affiliation**: State Key Laboratory for Novel Software Technology, Nanjing University (PDF first page)
- **Venue/conference**: arXiv preprint
- **Date**: 2026-11-16 (v1)
- **Abstract**: Interactive video world models act as simulators for embodied agents: from a start image and action trajectory they generate the views an agent would see, and a faithful simulator must preserve the camera's starting height. The paper shows six recent open-weight models fail: as generated content replaces the start view, they drift toward human eye level — "camera-height regression." The EyeHeight benchmark pairs six rendered elevations (0.15–2.2 m) and four calibrated real-rig heights with scale-free multi-view height estimation. All six models lose their initial height during a 180° turn-and-walk (from 0.15 m, only 0–20% of clips end within 1.3× of the start, converging to 1.1–1.5 m), while ground-truth renders stay within a few percent. The pull traces to human-centric video priors; in SANA-WM text height cues and floor-disparity maps do not prevent it, and 360° turns that restore the start view largely reverse it (author-reported).
- **Key innovations**:
  - **New failure mode + benchmark**: EyeHeight quantifies camera-height regression across six elevations, seven rendered scenes, and four real-rig heights.
  - **Six-model audit**: all tested open interactive-video world models drift to human eye level during rotation, with concrete downstream control bias (0.26 m path-endpoint shift for a navigation model).
  - **Cause analysis**: attributes drift to human-centric video priors; shows text/floor cues fail while view restoration reverses it.
  - **Game/world-model evaluation relevance**: exposes a hidden validity problem when using generative world models as game/embodied simulators.
- **Links**: [arXiv](https://arxiv.org/abs/2611.21782) | [PDF](https://arxiv.org/pdf/2611.21782)

### The Flip Test: Video World Models Fail to Learn the World State
- **Title (EN)**: The Flip Test: Video World Models Fail to Learn the World State
- **Authors**: Mi Luo; Lijun Yu; Adams Wei Yu; Ang Cao; Baochen Sun; Ming-Hsuan Yang; Nan Hua; Yuan Hao; Alex Dimakis; Ya Xu; Ed H. Chi; Xuezhi Wang; Yinxiao Liu
- **Affiliation**: UT Austin; Google DeepMind; UC Berkeley (PDF first page)
- **Venue/conference**: arXiv preprint (35 pages); project page: https://flip-test.github.io/
- **Date**: 2026-11-15 (v1)
- **Abstract**: Do video world models actually track world state? The paper probes counterfactually: when a tiny change in the present flips the future (a box millimeters before vs past a table edge), a state-tracking model must flip its prediction. FlipTest is a three-level hierarchy over 1,680 initial frames from 10 simulated and 15 real tasks — visual minimal pairs, matched controls, and dense sweeps. All 11 evaluated video world models fall short: the best averages 18.3% pair accuracy, **below 25% random guessing**; models flip equally on state-preserving and state-changing steps. On the same frames a VLM is selective (near-S-shaped boundary curve) and a coding agent measuring the image nearly locates the true boundary, implying the deciding information is in the frame and video models miss it. The authors urge rethinking world modeling beyond plausible pixels toward causal state (author-reported).
- **Key innovations**:
  - **Counterfactual minimal-pair protocol**: tests state tracking by requiring prediction flips exactly at causal boundaries.
  - **Strong negative result**: best of 11 video world models at 18.3% < random 25% — a clean falsification of "plausible video = world model."
  - **Three-level hierarchy** (minimal pairs / matched controls / dense sweeps) over 1,680 real+simulated frames.
  - **Industry evaluation signal**: VLMs and a measurement coding agent succeed where generative video models fail, redirecting world-model design toward causal state.
- **Links**: [arXiv](https://arxiv.org/abs/2611.19822) | [PDF](https://arxiv.org/pdf/2611.19822)

---

## 6) Related Techniques: Safe/In-Context RL, Imitation, and Search

### Algorithm Distillation for Safe In-Context Reinforcement Learning
- **Title (EN)**: Algorithm Distillation for Safe In-Context Reinforcement Learning
- **Authors**: Minjae Kwon; Amir Moeini; Shangtong Zhang; Lu Feng
- **Affiliation**: University of Virginia (PDF first page)
- **Venue/conference**: arXiv preprint (28 pages)
- **Date**: 2026-11-16 (v1)
- **Abstract**: Safe in-context RL asks a fixed-parameter policy to improve on an unseen constrained task from its interaction history while keeping cost within budget. Prior Safe Algorithm Distillation (Safe AD) shows adaptation failures (e.g., negative return on locomotion, rarely reaching the goal in CarGoal). The paper revisits two parts: first, distilling a *budget-aware teacher* with an explore-then-exploit phase (explore more while budget remains; exploit after first reward/cost), collecting histories under fixed or dynamic budgets — dynamic budgets raise occupancy entropy and improve return/lower cost in DarkRoom and HalfCheetah. Second, A-Lag applies a test-time action reweighting by predicted cost with an adaptive Lagrange multiplier updated from observed costs; A-Lag lowers mean episode cost vs Safe AD in all five environments (with lower final return in four) (author-reported).
- **Key innovations**:
  - **Budget-aware teacher distillation**: two-phase explore/exploit histories give the in-context learner cost-conditioned adaptation signal.
  - **Dynamic-budget training** increases coverage of return/budget inputs and improves goal-reaching in grid-world and locomotion tasks.
  - **A-Lag test-time cost correction**: adaptive Lagrange reweighting reduces cost across all five Safe ICRL benchmarks without retraining.
  - **Grid-world/navigation game relevance**: DarkRoom/PointGoal/CarGoal are hidden-goal/hazard game-like tasks; clarifies when algorithm distillation succeeds under safety constraints.
- **Links**: [arXiv](https://arxiv.org/abs/2611.21524) | [PDF](https://arxiv.org/pdf/2611.21524)

### MCTS Is Counting the Wrong Thing: Learning Exploration Counts for LLM Reasoning
- **Title (EN)**: MCTS Is Counting the Wrong Thing: Learning Exploration Counts for LLM Reasoning
- **Authors**: Xuan Zhang; Zhijian Zhou; Zicheng Hu; Yan Feng; Hongyan Hao; Yuan Qi; Chao Qu
- **Affiliation**: Fudan University; Shanghai Innovation Institute; Meituan; Shanghai Academy of Artificial Intelligence for Science (PDF first page)
- **Venue/conference**: arXiv preprint (38 pages)
- **Date**: 2026-11-17 (v1)
- **Abstract**: MCTS powered landmark RL systems such as AlphaGo, but its LLM-reasoning gains are often modest. The paper identifies *what MCTS counts* as a bottleneck: standard UCT assigns independent visit counts to textual branches, so different phrasings of the same strategy repeatedly earn exploration bonuses; theory links this count fragmentation to increased cumulative regret. Learned Pseudo-Count MCTS (LPC-MCTS) changes only the exploration statistic: a lightweight Coin-Flipping Network head on policy hidden representations estimates representation coverage, letting related branches share exploration evidence. Across five math-reasoning and seven search benchmarks LPC-MCTS beats strong baselines; swapping counts at inference gives +3.79 mean@16 points (Qwen2.5-7B) and +2.71 (Qwen3-4B), and training+inference gains reach +4.96/+4.37 (author-reported).
- **Key innovations**:
  - **Diagnosis of count fragmentation in UCT** with a cumulative-regret argument for why semantically duplicate branches waste exploration.
  - **Learned pseudo-counts via a coin-flipping head**: representation-coverage estimates replace raw visit counts, requiring no other MCTS change.
  - **Consistent gains** across 12 benchmarks and two training/inference regimes.
  - **Game-RL lineage**: directly revisits the AlphaGo-era exploration statistic, relevant to MCTS-based game agents and self-play search.
- **Links**: [arXiv](https://arxiv.org/abs/2611.22301) | [PDF](https://arxiv.org/pdf/2611.22301)

---

## Cross-Cutting Observations

- **Industry game AI is now a first-class research output**: this window features full systems from Microsoft Cambridge (79× real-time gameplay world model), LIGHTSPEED/Tencent + IDEA (LightAct), Google DeepMind (FlipTest), and Meituan (LPC-MCTS) — system-level papers with concrete deployment-oriented metrics rather than isolated benchmarks.
- **Real-time, data-efficient world models are the new game-foundation-model battleground**: Microsoft's 28-hour / 79× result and the wave of evaluation papers (EyeHeight, FlipTest, EPM) both push world models from "plausible video" toward faithful, controllable, low-latency simulators.
- **Generalization is being bought with reusable artifacts, not just more training**: Craftax's goal compiler, WSP's written weights, and PCGRL's diversity-preserving synthesis all separate a reusable, auditable artifact (program / weights / envelope) from expensive search, with zero-shot or held-out transfer.
- **Evaluation is moving from outcome scores to mechanism**: FlipTest's counterfactual minimal pairs, EyeHeight's camera-height drift, ALIVE-Bench's perception→intervention bottleneck, and LightAct's rollout-derived action rewards all diagnose *why* an agent/model succeeds or fails.
- **Classical RL techniques stay active in game-like settings**: fictitious play with nonlinear evaluators, certified Nash Q-learning, safe in-context RL, and MCTS pseudo-counts each provide concrete theory or ablations that clarify when self-play/search/distillation help.

## Coverage Notes and Gaps

- **Deduplication**: whole-wiki baseline of 10,489 arXiv IDs (all prior `game-rl-daily` digests plus every other wiki page and today's sibling syntheses); every included ID was grep-verified as absent from that baseline. No paper featured here was claimed by a sibling digest this window.
- **Topic coverage**: direct coverage for Game RL/strategic learning (Craftax, jump-diffusion Nash Q-learning, nonlinear fictitious play), Game AI bots (LightAct, WSP replication), game foundation/world models and industry game AI (Microsoft real-time world models, EPM), PCG (physics-aware PCGRL platformers), game benchmarks (ALIVE-Bench, EyeHeight, FlipTest), and related techniques (safe ICRL, MCTS exploration). Dedicated new *training* papers for StarCraft/Dota/NetHack/Go/chess/poker were sparse in the deduplicated fresh window; Go and Atari appear via the WSP replication (2611.20953) and MCTS's AlphaGo lineage (2611.22301).
- **Affiliations/venues**: affiliations PDF-verified for 12/13 papers; EPM (2611.22294) prints no affiliation on its first page. One paper carries a peer-reviewed venue (ALIVE-Bench, ACM MM 2026 Oral + Outstanding Paper Award); the rest are arXiv preprints, and venue labels are taken from arXiv comments/PDF footers and may reflect acceptance status rather than final published versions.
- **Limitations**: `websearch` was unavailable, so non-arXiv proceedings coverage is limited to venue/status metadata exposed on arXiv and PDF first pages. All reported metrics are author-reported and were not independently reproduced; several entries involve rapidly iterating preprints whose numbers may change in later versions.
- **Sources consulted (arXiv Export API, 2026-11-18)**: 27 keyword queries — `all:"game agent"`, `all:"reinforcement learning" AND all:game`, `all:"LLM agent" AND all:game`, `all:game AND all:"self-play"`, `all:"world model" AND (all:game OR all:Minecraft OR all:Atari)`, `all:"multi-agent reinforcement learning" AND all:game`, Minecraft/Atari/StarCraft/Dota/NetHack/poker/chess/Go combinations, `all:"procedural content generation"`, `all:"level generation" AND all:game`, `all:"game benchmark"`, `all:"game foundation model"`, `all:NPC`, `all:"game" AND all:"offline reinforcement"`, `all:"vision-language-action" AND all:game`, `all:"game" AND all:"imitation learning"`, `all:"curiosity" AND all:game`, `all:"hierarchical reinforcement" AND all:game`, `all:"reward shaping" AND all:game`, `all:"open-ended" AND all:game AND all:learning`, plus `cat:cs.MA` / `cat:cs.AI AND all:game`; ten date-bounded (`submittedDate:[20261112 TO 20261118]`) term sweeps over game titles, canonical game names, self-play/world-model/PCG terms, game-agent/NPC/benchmark terms, RL/agent terms, and VLA terms; title-only sweeps for `ti:game`, `ti:Minecraft/Atari/...`, `ti:"self-play"/"world model"/"procedural content"`; PDF first pages parsed with pypdf for affiliations and result details. Cache/fetch artifacts were confined to the pre-authorized temp directory and removed after use.
