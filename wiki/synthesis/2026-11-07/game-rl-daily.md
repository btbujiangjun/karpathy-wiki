---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-11-07)"
type: synthesis
created: 2026-11-07
updated: 2026-11-07
sources: []
tags: [game-rl, game-ai, llm-agents, reinforcement-learning, self-play, foundation-models, procedural-content-generation, benchmarks, world-models, vlm, multi-agent-rl, game-theory, daily-digest]
---
# Game RL & Game AI Bot — Daily Paper Digest (2026-11-07)

*Window: arXiv submissions announced roughly 2026-10-28 → 2026-11-06 (including Fri Nov 6 listings where relevant). 34 new papers across Game RL, game-theoretic learning, MARL systems, LLM/VLA game agents, interactive world models, procedural content generation, game benchmarks, industry deployment, and related techniques. Papers already covered by the sibling `2026-10-30` digest (e.g. `2610.37567`, `2610.35773`, `2610.33894`, `2610.31466`) are excluded; cross-references are noted inline.*

> ⚠️ All performance numbers below are **author-reported** and have not been independently reproduced. Affiliations are taken from arXiv HTML/PDF author blocks; where the paper lists none, this is stated explicitly rather than inferred.

---

## 1. Game RL — Algorithms, Self-Play, and Game-Theoretic Learning

### 1.1 Opponent Shaping, Regret, and Equilibrium

#### Discovering Learning Rules that Shape Others
- **Title:** Discovering Learning Rules that Shape Others
- **Authors:** Hong Jun Lee, Ziyan Wang, Jun Wang, Stefanos Leonardos, Yali Du
- **Affiliation:** King's College London; Harvard University; University College London
- **Venue:** arXiv preprint (2026-11)
- **arXiv:** [https://arxiv.org/abs/2611.08335](https://arxiv.org/abs/2611.08335)
- **Abstract:** In general-sum games, self-interested learners can reach outcomes that are poor for everyone, motivating methods that shape the opponent's learning. LOLA differentiates through the opponent's learning process; M-FOS uses model-free optimisation for long-horizon opponent shaping. Both require access to the opponent's parameters, policy, rewards, or learning rule during deployment. In single-agent RL, meta-learned update rules (e.g. DiscoRL) achieve state-of-the-art results while reading only the agent's own experience. The paper extends this framework to general-sum settings with Discovered Update Rule for Opponent Shaping (DUOS).
- **Key Innovations:**
  - First method to discover an update rule for an agent in general-sum games.
  - DUOS meta-trains the rule to maximise the agent's expected lifetime return and updates an inner network using only the agent's own experience.
  - The discovered rule exhibits behaviour consistent with opponent shaping **without** reading opponent policies or parameters.
  - Ranks 1st in normalised mean score and 1st in self-play among tournament entrants.
- **Relevance:** A practical route to opponent-aware game bots that do not need privileged access to the opponent — important for deployed multiplayer agents and population-based training.

#### Optimal Learning in Games with Arbitrary Delays: Best-of-Both-Worlds for Self-Play and Adversarial Opponents
- **Title:** Optimal Learning in Games with Arbitrary Delays: Best-of-Both-Worlds for Self-Play and Adversarial Opponents
- **Authors:** Emmanuel Esposito, Andrew Jacobsen, Hao Qiu, Alexander Ryabchenko, Mengxiao Zhang
- **Affiliation:** CREST, ENSAE, IP Paris (FairPlay Team); Universitat Pompeu Fabra; National University of Singapore; University of Toronto / Vector Institute; University of Iowa
- **Venue:** arXiv preprint (2026-11)
- **arXiv:** [https://arxiv.org/abs/2611.07773](https://arxiv.org/abs/2611.07773)
- **Abstract:** The paper studies learning in zero-sum games with delayed feedback and introduces Multi-Anchor Optimistic Online Mirror Descent (MAO-OMD), a single algorithm that obtains optimal fast rates in self-play on smooth games while maintaining minimax-optimal guarantees against arbitrary opponents.
- **Key Innovations:**
  - In smooth zero-sum games with arbitrary unknown delays, MAO-OMD achieves O(σ_max + 1) social and individual regret in self-play, where σ_max is the maximum number of outstanding gradients.
  - Simultaneously guarantees minimax-optimal O(√(T + d_tot)) individual regret against arbitrary opponents (d_tot = total delay).
  - Proves these optimal rates cannot be obtained simultaneously via the standard black-box reduction to the undelayed setting.
  - Extends to multi-player games and player-dependent delay sequences.
- **Relevance:** Real game training loops (distributed self-play, async actors) have stale gradients; this gives a single algorithm that is robust to both self-play and adversarial opponents under delay.

#### Learning and Steering in Incomplete-Information Games
- **Title:** Learning and Steering in Incomplete-Information Games
- **Authors:** Asrın Efe Yorulmaz, Tamer Başar
- **Affiliation:** University of Illinois Urbana–Champaign
- **Venue:** arXiv preprint (2026-11), 57 pages
- **arXiv:** [https://arxiv.org/abs/2611.07589](https://arxiv.org/abs/2611.07589)
- **Abstract:** A mediator seeks to influence strategic decision dynamics using only outcome-level feedback and without knowing agents' utilities. The mediator knows the game form and her own objective, commits to nonnegative payments, and provides recommendations and contexts, but receives only a single realized terminal outcome rather than full-information feedback.
- **Key Innovations:**
  - Halving-type algorithms learn utility differences in normal-form games and conditional continuation-value differences in extensive-form games.
  - Sample complexity Õ(ε⁻²), matching worst-case lower bounds up to logarithmic factors.
  - A Lagrangian "Learn-Compute-Steer" algorithm interleaves learning, equilibrium computation, and steering toward mediator-optimal extensive-form correlated equilibria (EFCE).
  - With high probability: directness and optimality gaps Õ(T^(−1/4)); time-average payments Õ(T^(−1/8)).
- **Relevance:** Mechanism-design / steering theory for game platforms and AI mediators that can nudge adaptive players (matchmaking, reward design, in-game incentives).

#### Learning vs. Optimizing Players in Budgeted Games
- **Title:** Learning vs. Optimizing Players in Budgeted Games
- **Authors:** Giannis Fikioris, Balasubramanian Sivan, Éva Tardos
- **Affiliation:** Google Research; Cornell University
- **Venue:** arXiv preprint (2026-11)
- **arXiv:** [https://arxiv.org/abs/2611.05580](https://arxiv.org/abs/2611.05580)
- **Abstract:** The paper studies repeated general games over T rounds between a utility-maximizing optimizer and a learning agent, where budget constraints couple decisions across rounds. Without budgets, low swap regret both guarantees sublinear learner regret and caps the optimizer at its Stackelberg value. Budgets break this picture: adversarial no-regret becomes impossible.
- **Key Innovations:**
  - Defines *non-manipulability*: no adaptive optimizer earns more than BSE·T + o(T), where BSE is the Budgeted Stackelberg Equilibrium value.
  - Gives an efficient budget-feasible learner achieving non-manipulability and low stochastic regret in every budgeted game.
  - Any adaptive optimizer earns at most BSE·T + O(√T) in expectation; O(√T) regret per interval when the optimizer plays a fixed mixed strategy.
  - Introduces response calibration and dual-weighted Lagrangian calibration, and constructs the required randomized forecasts in polynomial time.
- **Relevance:** Budgets are ubiquitous in games (energy, currency, turns); this characterises when a learning bot can avoid being exploited by an optimizer.

#### When Is a Game a Markov Decision Process? Correspondences Between Game Theory and Reinforcement Learning
- **Title:** When Is a Game a Markov Decision Process? Correspondences Between Game Theory and Reinforcement Learning
- **Authors:** Eduardo C. Garrido-Merchán
- **Affiliation:** DIGNUM Centre, Universidad Pontificia Comillas (Madrid)
- **Venue:** arXiv monograph (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.41962](https://arxiv.org/abs/2610.41962)
- **Abstract:** Reinforcement learning and game theory describe the same object from two sides. The two literatures keep separate vocabularies for identical structures, and prior treatments present the correspondence as analogy rather than theorem. This monograph supplies the theorems.
- **Key Innovations:**
  - Classifies every correspondence as a definitional identity, an exact value-/solution-preserving reduction, or a structural analogy that fails under identifiable conditions.
  - Covers normal-form through repeated, stochastic, partially observable, extensive-form imperfect-information, Bayesian, graphical, Stackelberg, potential, coalitional, mean-field, and evolutionary games.
  - Maps solution concepts: Nash ↔ Bellman fixed point, quantal response ↔ soft Bellman, Shapley ↔ credit assignment, Blackwell approachability ↔ no-regret learning.
  - Records complexity and the training procedures sound for each model class; collects known non-correspondences (independent-learner non-stationarity, uncoupled-convergence impossibilities, CCE-vs-CE gap).
- **Relevance:** A reference for reasoning rigorously about game-agent training; useful when deciding whether a game should be modelled as an MDP, POSG, or extensive-form game.

#### Game-Theoretic Foundations for Undiscounted Bisimulation Metrics
- **Title:** Game-Theoretic Foundations for Undiscounted Bisimulation Metrics
- **Authors:** Matthew Zurek, Yudong Chen, Josiah P. Hanna
- **Affiliation:** University of Wisconsin–Madison
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.38313](https://arxiv.org/abs/2610.38313)
- **Abstract:** Bisimulation metrics offer a principled notion of task-relevant state similarity, but existing constructions are largely confined to discounted MDPs. The paper develops a unified foundation for undiscounted (total- and average-reward) settings by replacing the operator-centric view with a game-centric one.
- **Key Innovations:**
  - Interprets prior metric operators as Bellman–Shapley operators of zero-sum turn-based games; metrics become game value functions, yielding unique definitions even at γ = 1.
  - Characterises how metric finiteness depends on MDP structure and motivates directed metrics finite in weakly communicating MDPs.
  - Abstract framework for modifying action spaces via general transition-coupling sets, recovering existing metrics and guiding new ones.
  - Proves metrics bound total-reward and optimal relative-value differences; provides error/suboptimality guarantees for aggregation-based planning.
- **Relevance:** Long-horizon game state abstraction without discounting — relevant to episodic games, average-reward settings, and state aggregation in large game worlds.

#### Reinforcement Learning for the Game of Balatro: A Fast Simulator and Two-Policy Training Approach
- **Title:** Reinforcement Learning for the Game of Balatro: A Fast Simulator and Two-Policy Training Approach
- **Authors:** Ajay Vikram Periasami, Anjaneya Gupta, Ethan Cheng, Ivan Rosales
- **Affiliation:** Duke University
- **Venue:** EXAG 2026 (AIIDE Workshop on Experimental AI in Games)
- **arXiv:** [https://arxiv.org/abs/2610.39049](https://arxiv.org/abs/2610.39049)
- **Abstract:** Balatro, a 2024 roguelike deckbuilder, combines a 3,000-action state-dependent action space, horizons of several hundred decisions with sparse rewards, and pervasive stochasticity in card draws and shop generation. Published RL results remain scarce.
- **Key Innovations:**
  - High-throughput Rust simulator automatically state-diffed against the live game client via BalatroBot.
  - Condensed observation–action interface with dynamic per-step masking of legal moves.
  - Multi-agent PPO with a tactical blind policy and a strategic shop policy sharing full game state but acting in disjoint phases, plus per-agent reward routing and explicit cross-agent credit.
  - First-blind clear rate converges above 99%; mean return rises ~10× and plateaus at mean maximum ante 3/8; single-agent baselines oscillate between greedy and hoarding failure modes.
- **Relevance:** A clean case study in decomposing a complex, stochastic deckbuilder into phase-specific policies; localises the remaining gap to long-horizon strategy rather than tactical play.

#### RIDGE: State-Conditioned Reward Blending for Behavioral Coverage in Deep RL Game Agents
- **Title:** RIDGE: State-Conditioned Reward Blending for Behavioral Coverage in Deep RL Game Agents
- **Authors:** AL Muqshith Mohammed Shifan, Kevin Christopher Chua, Ali Neshati, Loutfouz Zaman, Cristiano Politowski
- **Affiliation:** Ontario Tech University
- **Venue:** Conference on Games 2026 (4-page paper)
- **arXiv:** [https://arxiv.org/abs/2611.05601](https://arxiv.org/abs/2611.05601)
- **Abstract:** A deep RL agent trained on a fixed persona reward plays one way; automated playtesting therefore needs N agents for N styles. Changing reward composition mid-episode runs into the switching-stability dilemma because PPO degrades under non-stationary rewards.
- **Key Innovations:**
  - State-conditioned blender computes softmax-normalized sigmoid weights from slow-moving state variables.
  - Multi-head critic trains one value head per persona on its own stationary signal.
  - On Crafter with four personas, one RIDGE agent acquires both branches of the wood-tier crafting/combat split that no fixed-persona baseline solves jointly.
  - Sharpness ablation confirms state-conditioning drives the gain (n = 3 seeds; larger sweeps deferred).
- **Relevance:** Single-policy behavioural coverage for automated playtesting and diverse NPC behaviour — avoids training one agent per style.

#### Inner-Learning: From Hand-Coded Beliefs to Declarative Knowledge in Trick-Taking Games
- **Title:** Inner-Learning: From Hand-Coded Beliefs to Declarative Knowledge in Trick-Taking Games
- **Authors:** Stefan Edelkamp
- **Affiliation:** Charles University, Prague
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.38304](https://arxiv.org/abs/2610.38304)
- **Abstract:** Presents a declarative approach to belief-state modelling in trick-taking card games. Starting from a state-of-the-art Skat player, hand-coded inference rules are automatically extracted into a domain-specific language built on the primitive ¬holds(P, C) — player P cannot hold any card in set C.
- **Key Innovations:**
  - Round-trip code generation verifies extracted rules reproduce the original engine's intended behaviour, correcting three audited bugs.
  - Grows the rule base via symmetric derivation and annotation of an expert strategy document, unifying code, symmetry, and expertise.
  - Extends the representation with cardinality constraints (at-most-k / at-least-k) enforced at world-generation time; confidence parameters connect symbolic rules to probabilistic belief updates.
  - Self-play shows the declarative engine measurably improves winning percentage and score over the original hand-coded engine.
- **Relevance:** Symbolic + probabilistic belief modelling for imperfect-information card games; a bridge between hand-crafted game AI and learned/declarative knowledge.

---

## 2. Multi-Agent RL, Open-Ended Learning, and Systems

#### An Axiomatic Framework for Reinforcement Learning in Open Multi-Agent Systems
- **Title:** An Axiomatic Framework for Reinforcement Learning in Open Multi-Agent Systems
- **Authors:** Jianhong Wang, Yang Li, Samuel Kaski, Jonathan Lawry
- **Affiliation:** University of Bristol (INFORMED-AI Hub); Shanghai Jiao Tong University; ELLIS Institute Finland
- **Venue:** NeurIPS 2026
- **arXiv:** [https://arxiv.org/abs/2611.03301](https://arxiv.org/abs/2611.03301)
- **Abstract:** Open multi-agent systems, where only a subset of agents are controllable, are central to real-world domains but lack a principled foundation for RL algorithm design. The paper studies n-agent ad hoc teamwork (NAHT) and proposes an axiomatic framework deriving value-function learning from the Shapley axioms (Efficiency, Symmetry, Linearity).
- **Key Innovations:**
  - Novel NAHT decomposition characterising the difference between open and fully controllable multi-agent systems.
  - Enforcing the axioms on individual value functions recovers the Shapley value for Dec-POMDPs.
  - Introduces Shapley Machines and Banzhaf Machines, generic templates instantiable with standard RL methods.
  - Applied to IPPO and POAM, consistently improves learning efficiency and generalisation to unseen agent types/conventions on NAHT benchmarks.
- **Relevance:** Principled credit assignment when teammates come and go — common in multiplayer games, ad hoc coalitions, and open game populations.

#### AGiR: Mitigating Gift Over-Reliance in Mixed-Motive Games
- **Title:** AGiR: Mitigating Gift Over-Reliance in Mixed-Motive Games
- **Authors:** Woohyeon Byeon, Seongmin Kim, Jiwon Jeon, Woojun Kim, Youngchul Sung
- **Affiliation:** KAIST
- **Venue:** NeurIPS 2026
- **arXiv:** [https://arxiv.org/abs/2611.02875](https://arxiv.org/abs/2611.02875)
- **Abstract:** Mixed-motive games (MMGs) model settings where self-interested agents must both cooperate and compete. Existing gifting methods cause *gift over-reliance*: agents become overly dependent on incoming gifts and fail to learn reward-yielding behaviours.
- **Key Innovations:**
  - Refusal-augmented gifting framework with an adaptive refusal mechanism that selectively rejects a portion of received gifts from policy-update signals.
  - Mitigates gift over-reliance and prevents exploitation; gifting-method-agnostic and compatible with decentralized learning.
  - Across diverse MMG environments and gifting schemes, reduces lock-in to sacrificing policies and improves α-fairness.
- **Relevance:** Mixed-motive game bots (team competition, negotiation, social dilemmas) where naive reward sharing collapses into passivity.

#### From Single-Agent Self-Discovery to Multi-Agent Adaptation: Scaling Laws of Partner Feedback and Convention Rigidity in Meta Reinforcement Learning Algorithms
- **Title:** From Single-Agent Self-Discovery to Multi-Agent Adaptation: Scaling Laws of Partner Feedback and Convention Rigidity in Meta Reinforcement Learning Algorithms
- **Authors:** Haomin Luo, Ersha Li
- **Affiliation:** University of Cambridge; Models2 AI
- **Venue:** arXiv preprint (2026-11), 71 pages
- **arXiv:** [https://arxiv.org/abs/2611.01742](https://arxiv.org/abs/2611.01742)
- **Abstract:** A key milestone toward recursive self-improvement is replacing hand-crafted optimizers with meta-learned update rules (Disco103, OPEN) that discover how agents learn. The paper asks whether co-evolution with adapting teammates sustains capability gains or traps agents in brittle conventions.
- **Key Innovations:**
  - 1,800+ runs in continuous collective robotics (VMAS) and discrete coordination (Overcooked); establishes five laws of multi-agent adaptation.
  - Counterfactual partner swaps expose an evaluation illusion: +1.066 team gain can conceal −0.119 focal loss and inflate transfer by +0.649 to +1.210.
  - 288-run physical-coupling sweep finds a linear scaling law (β = +0.255, p = 0.000488, Spearman ρ = 1.0); severing feedback causes monotonic collapse.
  - In Overcooked, MAPPO self-play conventions induce a 28.13% cross-partner collision rate; Disco103 cuts it to 12.77% and achieves 3.33× higher bank return.
- **Relevance:** Scaling laws for multi-agent meta-RL and concrete evidence that self-play conventions can be brittle and partner-specific.

#### KlaskTron: An Open-Source Platform for Physical Adversarial Multi-Agent RL
- **Title:** KlaskTron: An Open-Source Platform for Physical Adversarial Multi-Agent RL
- **Authors:** Aswin Ramachandran, Jona Schulz, Maurus Derungs, Carlo Angelini, Tobias Meier, Raffaello D'Andrea
- **Affiliation:** Institute for Dynamic Systems and Control (IDSC), ETH Zürich
- **Venue:** RSS 2026 (Robotics: Science and Systems, Sydney)
- **arXiv:** [https://arxiv.org/abs/2611.03138](https://arxiv.org/abs/2611.03138)
- **Abstract:** Physical multi-agent RL is challenged by limited accessible, standardized benchmarks. KlaskTron is an open-source, low-cost (<$2,500), desktop-scale robotic testbed for adversarial MARL based on the tabletop game KLASK.
- **Key Innovations:**
  - Dual CoreXY gantries with high-torque brushless motors for high-speed, precise competitive play.
  - Complete ecosystem: hardware CAD/BOM, GPU-native digital twin in NVIDIA Isaac Lab, and a validated sim-to-real baseline using a learned neural actuator model.
  - Demonstrates zero-shot policy transfer with emergent adversarial behaviours; all assets released publicly.
- **Relevance:** Brings game-style adversarial MARL into the physical world at low cost — a reproducible bridge between simulated game AI and robotics.


#### EFXPLORER: Cooperative Multi-Agent Reinforcement Learning via Epigraph-Form Guided Exploration
- **Title:** Cooperative Multi-Agent Reinforcement Learning via Epigraph-Form Guided Exploration
- **Authors:** Sungil Son, Hoseong Jung, Dahyun Oh, H. Jin Kim
- **Affiliation:** Seoul National University
- **Venue:** NeurIPS 2026
- **arXiv:** [https://arxiv.org/abs/2611.07066](https://arxiv.org/abs/2611.07066) | **PDF:** [https://arxiv.org/pdf/2611.07066](https://arxiv.org/pdf/2611.07066)
- **Abstract:** Discovering cooperative behavior in MARL is difficult because the joint state-action space is combinatorial and trial-and-error alone rarely yields coordinated strategies. Intrinsic rewards can help discovery but naively mixing them with team objectives can distort the learning signal and hurt task performance. EFXPLORER frames exploration as constrained optimisation: maximise exploration subject to preserving established task performance.
- **Key Innovations:**
  - Epigraph reformulation introduces adaptive exploration budgets, separating intrinsic rewards from task objectives and regulating exploration through task feasibility rather than scalar reward mixing.
  - Incorporates a successor-distance-based intrinsic reward that captures long-horizon dependencies to encourage diverse, temporally extended exploration.
  - Conservative exploration framework avoids the objective distortion that often arises when intrinsic bonuses overshadow team rewards.
  - Empirically outperforms strong baselines and induces novel cooperative strategies across **SMAX, VMAS, and MPE** benchmark suites.
- **Relevance:** A principled exploration mechanism for cooperative game/MARL benchmarks (SMAX/VMAS/MPE) — directly addresses the common failure mode where curiosity bonuses break coordination.

#### SEER: A Scalable Event-Driven Runtime for Parallel Execution of Multi-Agent Reinforcement Learning Environments
- **Title:** SEER: A Scalable Event-Driven Runtime for Parallel Execution of Multi-Agent Reinforcement Learning Environments
- **Authors:** Jiming Su, Feng Zhu, Yuhao Xiao, Miao Zhang
- **Affiliation:** National University of Defense Technology (NUDT)
- **Venue:** arXiv preprint (2026-11)
- **arXiv:** [https://arxiv.org/abs/2611.07996](https://arxiv.org/abs/2611.07996)
- **Abstract:** In MARL workloads, policy inference can be batched on GPUs, but the CPU-side environment path still updates entity states, resolves local interactions, and builds observations inside each `env.step`. This path can dominate latency. Existing vectorized environment interfaces and event-driven runtimes do not address fine-grained cross-entity work inside one bounded MARL step while preserving step-level semantics.
- **Key Innovations:**
  - Models each environment step as a bounded stream of timestamped events under an explicit event-locality contract.
  - CAS-based dual-layer event queue: local queues preserve per-entity causal order; a parallel executive list exposes ready work to worker threads.
  - STPA preflight-guided thread-pool selection combines short runtime traces with static workload and hardware features.
  - Reduces inference latency 16.2% on UAV swarm control and environment-execution latency 46.9%/19.5%/64.9% versus ROSS-T/NBSE/ROOT-Sim on wireless management.
- **Relevance:** Training-throughput infrastructure for large multi-agent game environments; environment simulation is often the bottleneck after GPU policy batching.


#### MA-SafeDiffuser: Safe Multi-Agent Planning with Diffusion Probabilistic Models
- **Title:** MA-SafeDiffuser: Safe Multi-Agent Planning with Diffusion Probabilistic Models
- **Authors:** Kiran Ravish, Ankita Kushwaha, Preeti, Pawan Kumar
- **Affiliation:** IIIT Hyderabad, Hyderabad, India
- **Venue:** AAMAS 2026
- **arXiv:** [https://arxiv.org/abs/2611.05524](https://arxiv.org/abs/2611.05524) | **PDF:** [https://arxiv.org/pdf/2611.05524](https://arxiv.org/pdf/2611.05524)
- **Abstract:** MA-SafeDiffuser extends SafeDiffuser to multi-agent settings by equipping diffusion-based trajectory planners with finite-time diffusion invariance guarantees for joint-agent safety specifications. Building on single-agent CBF constraints embedded into reverse-diffusion updates, it provides joint-safe planning for interacting agents.
- **Key Innovations:**
  - Formalises joint safe sets as intersections of per-agent and pairwise barrier sets.
  - Derives centralised and decentralised (communication-aware) constrained denoising procedures with provable invariance under mild assumptions.
  - Addresses local-trap and deadlock phenomena via time-varying specifications and liveness CBFs.
  - Develops a lightweight benchmarking suite including a multi-agent Maze2D domain; empirically reduces violation counts relative to unconstrained diffusion baselines while retaining planning quality.
- **Relevance:** Diffusion-based multi-agent planning with safety guarantees — relevant to game/NPC path planning, collision-aware multi-agent control, and safe generative policies.

---

## 3. Game AI Bots — LLM / VLA Game Agents

#### TaskFrame: Connecting Task-Level Planning with Frame-Level Control for Game Agents
- **Title:** TaskFrame: Connecting Task-Level Planning with Frame-Level Control for Game Agents
- **Authors:** Guangzhi Wang, Junfu Pu, Yiran Wang, Xingyilang Yin, Honghao Chen, Cheng Cheng, Lingen Li, Yinan Zhou, et al.
- **Affiliation:** Tencent ARC Lab; The Chinese University of Hong Kong; City University of Hong Kong; Huazhong University of Science and Technology; Peking University; University of Macau; Great Bay University
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.40276](https://arxiv.org/abs/2610.40276)
- **Abstract:** General game agents need high-level task reasoning and low-latency action control in rapidly changing visual environments — capabilities with very different computational profiles. TaskFrame is a hierarchical planner–controller framework connecting task-level planning with frame-level keyboard-and-mouse control.
- **Key Innovations:**
  - Vision-language task planner decomposes a goal into ordered atomic instructions, optimised with supervised learning and dependency-aware GRPO.
  - Hidden states of special goal tokens provide continuous goal embeddings cached and reused across control steps.
  - Causal Transformer controller combines the active goal embedding with recent observations to predict discrete keyboard/mouse buttons and continuous camera motion each step.
  - Three-stage training (planner, controller pretraining, joint alignment); in Minecraft beats evaluated baselines on closed-loop combat success and is competitive on instruction decomposition.
- **Relevance:** A production-oriented architecture for LLM-planner + fast-controller game agents; directly targets the latency gap between reasoning and frame-level play.

#### Where It Breaks: Diagnosing Perception, Memory, and Decision Failures of a Vision-Language Agent in Pac-Man
- **Title:** Where It Breaks: Diagnosing Perception, Memory, and Decision Failures of a Vision-Language Agent in Pac-Man
- **Authors:** Xinglu Wang, Edward Wang, Yong Zhang, Zhenan Fan
- **Affiliation:** Not listed on arXiv author block
- **Venue:** arXiv preprint (2026-11), 35 pages
- **arXiv:** [https://arxiv.org/abs/2611.06704](https://arxiv.org/abs/2611.06704)
- **Abstract:** Training an agent to play Pac-Man with only up/down/left/right actions raises a basic question: when performance is poor, what should be improved? Difficulty can arise from reading the screen or from choosing actions over a long sequence. The paper separates perception checks from primitive-policy RL studies on a Qwen3.5-9B-based agent.
- **Key Innovations:**
  - Policy study uses textual boards to remove image transcription from the decision interface; completion on eight held-out mazes rises from 0% to 80.2% at a selected checkpoint (three extra lives).
  - Perception checks show accurate static screenshot reading can coexist with errors during interaction.
  - A separate policy comparison shows further optimisation can accompany worse action choices.
  - Recommends post-training checks: evaluate perception in use, distinguish training success from full-game validation, and inspect decisions and later performance rather than one selected score.
- **Relevance:** A diagnostic methodology for VLM game agents; evidence that benchmark scores can hide perception/decision failures.

#### TactiNavi: Serving and Revising an LLM Game Coach with Explicit Strategy Conditions
- **Title:** TactiNavi: Serving and Revising an LLM Game Coach with Explicit Strategy Conditions
- **Authors:** Qi Liu, Xiaoyang Yuan, Zhuomeng Zhang, Yubin Ruan, Xinyi Mou, Wenjin Wang, Hanying Jiao, Di Wu, et al.
- **Affiliation:** Tencent; Tongji University; Shanghai Innovation Institute
- **Venue:** arXiv preprint (2026-11), 17 pages
- **arXiv:** [https://arxiv.org/abs/2611.04772](https://arxiv.org/abs/2611.04772)
- **Abstract:** A deployed LLM coaching agent answers requests whose correct response depends on player state and game version, so advice that is right for one player can be wrong for the next. TactiNavi is the serving system behind the LLM coach of a commercial open-world game.
- **Key Innovations:**
  - Offline compiler turns versioned game evidence and expert guidance into strategy packages with explicit prerequisites.
  - Serving plane evaluates prerequisites as three-valued conditions over structured player state and records decision traces.
  - Control plane validates revisions on held-out traffic before release using condition–rule dependencies.
  - On 1,122 logged coaching turns across three deployment periods: condition-bearing packages raise correctness 57.9% → 82.0% over atomic facts and cut strategy misapplication under changed player state 18.1% → 10.4%; trace-based claim verification reaches 86.4% precision at 2.07 s median latency.
  - A null-model rerun recovers 38.4% of failing turns, and only 1 of 15 shipped revision units passes release checks retrospectively.
- **Relevance:** One of the most concrete deployed LLM game-agent serving reports; applicability-as-a-first-class-object and null-model release testing are transferable lessons.

#### StreamDuo: A Live Commentator and a Research Agent for Unseen Games
- **Title:** StreamDuo: A Live Commentator and a Research Agent for Unseen Games
- **Authors:** Zixian Gao, Penghao Luo, Xiangcheng Cao, Lixin Xiu, Ziqi Cai, Zhen Li, Erwin Wu, Kaipeng Zhang
- **Affiliation:** Alaya Lab; The University of Tokyo; Georgia Institute of Technology; Peking University; Institute of Science Tokyo
- **Venue:** arXiv preprint (2026-10), 18 pages
- **arXiv:** [https://arxiv.org/abs/2611.01120](https://arxiv.org/abs/2611.01120)
- **Abstract:** Streaming video LLMs can commentate live gameplay but are trained and tested on the same games. The paper studies cross-game streaming commentary and finds current commentators transfer timing but not game-world knowledge. StreamDuo pairs a trainable commentator with a frozen research agent that reads the wiki of the game being played.
- **Key Innovations:**
  - Commentator asks for help only when it cannot name something; research agent returns a few wiki entries ~2 s later while the stream continues.
  - Two-stage training on a single game: information-gain labels teach when to ask; on-policy self-distillation teaches use of noisy answers.
  - Trained on Baldur's Gate 3, tested on ten unseen games: entity recall 0.082 → 0.116 over Proact-VL, source-game leakage 9.9% → 1.0%, best timing and highest judged liveliness/quality among streaming models.
- **Relevance:** A tool-augmented streaming game agent that generalises across unseen games — relevant to AI casters, companion agents, and real-time game narration.

#### Can Large Language Model Agents Learn by Watching Tutorial Videos?
- **Title:** Can Large Language Model Agents Learn by Watching Tutorial Videos?
- **Authors:** Haoyu Zhao, Zafeirios Fountas, Jun Wang
- **Affiliation:** University College London
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2611.01460](https://arxiv.org/abs/2611.01460)
- **Abstract:** Millions of instructional videos are uploaded online, yet LLM agents cannot exploit this ever-expanding resource because capabilities are frozen after training and parameter updates at scale are expensive. TAL is a nonparametric continual-learning paradigm that consolidates tutorial videos into a persistent structured *tutorialbook* memory.
- **Key Innovations:**
  - Two-stage adversarial process harvests hard, video-grounded questions to refine memory.
  - Inference retrieves through a Table-of-Contents (TOC) tree, tying retrieval to reasoning rather than embedding similarity.
  - VidLearn benchmark: 72 chess tutorial videos across 12 openings; TAL improves monotonically with more videos, up to 113%/91% relative gains over vanilla MLLMs on train/test.
  - In actual gameplay, TAL reaches a stronger opening-phase position in 69% of head-to-head games; generality shown in a second domain.
- **Relevance:** Parameter-update-free learning from human game tutorials — an important capability for deployed game agents that must keep up with patches, openings, and metas.

#### Rome Wasn't Built in One Turn: Replay-Grounded Reward Signals for Long-Horizon Freeciv Agents
- **Title:** Rome Wasn't Built in One Turn: Replay-Grounded Reward Signals for Long-Horizon Freeciv Agents
- **Authors:** Yanchen Liu, Xinyu Che, Brihi Joshi, Renzo Fukuda, Junhua Liu, Ruifeng Li, Yunfei Ge, Hang Yan, et al.
- **Affiliation:** University of Southern California; Xi'an Jiaotong University; Stanford University; Northwestern University
- **Venue:** arXiv preprint (2026-10), 22 pages
- **arXiv:** [https://arxiv.org/abs/2610.41264](https://arxiv.org/abs/2610.41264)
- **Abstract:** Training language-model agents to play long-horizon strategy games is hard because deterministic feedback is sparse and often only arrives at the end. In-game scores can offer dense signals, but they do not reliably predict future outcomes: in 8–68% of position pairs across eight strategy games, the higher-scoring position leads to the worse outcome — a phenomenon the authors call *scoreboard traps*.
- **Key Innovations:**
  - CivHarness saves game states, branches on decisions, and replays to future turns to provide measurable long-horizon feedback.
  - CivTelescope LLM Judge predicts which of two positions yields the better outcome; 1.3–2.0× more accurate than off-the-shelf LMs on scoreboard-trap pairs.
  - CivMarshmallow trains a Freeciv agent with CivTelescope as dense reward: +8.94 average mid-game training phase gain, 77% more than the end-of-game reward baseline.
  - A hybrid reward that shifts from scoreboard/end-of-game to CivTelescope over 120 turns scores highest among compared rewards.
- **Relevance:** Dense, replay-grounded reward shaping for long-horizon strategy games; the scoreboard-trap measurement is a useful caution for game-agent reward design.

#### EpiAgent: Epistemic Self-Play for LLM Agents
- **Title:** EpiAgent: Epistemic Self-Play for LLM Agents
- **Authors:** Xuanfa Jin, Xinyu Cui, Zhijian Ma, Xue Yan, Jian Zhao, Haifeng Zhang, Jun Wang
- **Affiliation:** Institute of Automation, Chinese Academy of Sciences; School of Artificial Intelligence, UCAS; Zhongguancun Academy; AI Centre, Department of Computer Science, UCL
- **Venue:** arXiv preprint (2026-10), 23 pages
- **arXiv:** [https://arxiv.org/abs/2610.40227](https://arxiv.org/abs/2610.40227)
- **Abstract:** Epistemic game theory explains strategic behaviour via beliefs about others and how they update. Modern LLM agents often lack an explicit mechanism for learning and updating such beliefs under incomplete information.
- **Key Innovations:**
  - Explicit learnable epistemic layer maintains beliefs over others' private information and forms an epistemic state for action selection.
  - Policy decomposed into Epistemic Update (beliefs from interaction history) and Action Planning (actions conditioned on epistemic state).
  - Bi-level optimisation solved by Epistemic Self-Play, alternately optimising the two stages with an intrinsic prediction reward for belief quality.
  - Outperforms prompting-based and RL-based baselines across mixed and competitive scenarios; analyses show improved belief-inference accuracy.
- **Relevance:** Adds explicit theory-of-mind-style belief modelling to LLM game agents — important for poker-like, negotiation, and hidden-role games.

#### AceAction-5M: Hierarchical Goals for Generalist Action Learning Across 3D Game Worlds
- **Title:** AceAction-5M: Hierarchical Goals for Generalist Action Learning Across 3D Game Worlds
- **Authors:** Kailing Li, Ruoxuan Zhang, Zheyuan Zhou, Boyang Chu, Yingshan Lei, Hongxia Xie, Liang Du, Zixun Sun
- **Affiliation:** Tencent; Jilin University; East China Normal University
- **Venue:** arXiv preprint (2026-11)
- **arXiv:** [https://arxiv.org/abs/2611.04241](https://arxiv.org/abs/2611.04241)
- **Abstract:** Video games provide a practical setting for collecting vision-language-action (VLA) data, whose acquisition in physical environments is costly. Existing datasets are limited by restricted game coverage, sparse language supervision, or temporal hierarchies that do not reflect changes in task objectives.
- **Key Innovations:**
  - AceAction dataset of human gameplay across multiple 3D games, linking overall instructions, ordered subgoals, and local skill instructions to temporally aligned observations and keyboard-and-mouse actions.
  - VLM pipeline identifies subgoals from objective/interaction-target changes, anchors navigation goals to waypoints, and composes adjacent subgoals into task instructions.
  - Covers navigation, reconnaissance, combat, interaction, and recovery with explicit stage boundaries; 95.8% pass rate on a 500-trajectory audit.
  - Data foundation for skill execution, composition, and switching under complex instructions.
- **Relevance:** Large-scale hierarchical VLA data for generalist game agents — directly targets imitation learning and skill composition in 3D game worlds.

---

## 4. Game Foundation Models and Interactive World Models

#### PlayGen2: Learning Real-Time Playable Worlds with Explicit 3D State
- **Title:** PlayGen2: Learning Real-Time Playable Worlds with Explicit 3D State
- **Authors:** Jihai Zhang, Yuhan Zhou, Junyou Li, Deheng Ye, Qi Dou, Yu Cheng
- **Affiliation:** The Chinese University of Hong Kong; Tencent; Nanyang Technological University; Wellington College
- **Venue:** arXiv preprint (2026-11); code and weights released
- **arXiv:** [https://arxiv.org/abs/2611.07867](https://arxiv.org/abs/2611.07867)
- **Abstract:** A playable world needs responsive control, persistent spatial structure, and coherent interactions with dynamic entities. Using generated frames as the sole recurrent world representation ties these requirements to view-dependent appearance synthesis, hurting long-term spatial/temporal consistency. PlayGen2 separates learned 3D state evolution from neural rendering.
- **Key Innovations:**
  - Persistent world memory: static geometry as a volumetric occupancy grid plus identity-indexed 3D states for player and other entities.
  - World-state model jointly learns action-conditioned entity dynamics, geometry completion, and entity discovery within a fixed-size local region.
  - Neural renderer synthesises first-person observations from depth and semantic projections, without feeding generated images back into state prediction.
  - On Doom: ~160 ms end-to-end backend latency on a MacBook Pro M4 Pro; zero-shot on unseen maps, multiplayer via composition of single-player models, and programmable rule-based state interventions.
- **Relevance:** A concrete step toward real-time, interactive game world models that run on consumer hardware; explicit state avoids the drift of frame-only world models.

#### Fight World Model: Customizable Combat through Visual Interaction Proxies
- **Title:** Fight World Model: Customizable Combat through Visual Interaction Proxies
- **Authors:** Jiahua Li, Zixu John, Tom Zhong, Fuping Wu, Tianhao Xu, Ruicheng Zhang, Jun Zhou, Zunnan Xu
- **Affiliation:** Imperial College London; Tsinghua University; Nanyang Technological University
- **Venue:** arXiv technical report (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.40607](https://arxiv.org/abs/2610.40607)
- **Abstract:** A playable, programmable game world must maintain persistent state, enforce executable rules, and support extensible mechanics. Existing video world models generate plausible combat but struggle to keep hit reactions and health updates consistent with game rules. FWM separates rule-governed combat execution from video rendering.
- **Key Innovations:**
  - Executable engine maintains state and resolves interactions; a deterministic compiler encodes outcomes and attempted actions in a spatially/temporally aligned interaction proxy.
  - Proxy aligns action and skill windows, brief hit reactions, and persistent health by fighter identity and timing; cues can be controlled separately to render under modified rules.
  - Trained on FightWorld Corpus: 52 skill effects, 187 character-appearance variants, 15 arenas.
  - Without retraining the renderer, supports damage scaling, limited-hit immunity, lifesteal, and multi-stage skill mechanics; outperforms existing game world models on action fidelity, hit reactions, health consistency, and appearance preservation.
- **Relevance:** Shows how to make generative game worlds obey game rules — a prerequisite for AI-generated, moddable combat games.

#### Wizard: Manipulate Any World in Real Time via Agentic Control
- **Title:** Wizard: Manipulate Any World in Real Time via Agentic Control
- **Authors:** Yuzhe Wu, Zijun Lin, Yeying Jin
- **Affiliation:** Tencent; National University of Singapore; Nanyang Technological University
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.40339](https://arxiv.org/abs/2610.40339)
- **Abstract:** Video world models enable realistic interactive virtual environments, but existing agentic frameworks support only simple settings and predefined motion, generalise poorly, and offer limited real-time interactivity. Wizard is an agentic game world model enabling real-time precise character-motion control with zero-shot generalisation across scenes, characters, and actions.
- **Key Innovations:**
  - Dataset spanning 750 scenes and 178 characters with skeleton and geometry information as structured representations.
  - Structured proxies condition a video generation model; an adaptive masking mechanism improves alignment between conditioning signals and generated rollouts.
  - Agentic framework explicitly maintains and updates game state, letting players configure worlds and exercise fine-grained motion control while preserving visual quality and gameplay consistency.
- **Relevance:** Player-driven game creation via agentic control of world models; combines explicit state with generative rendering.

#### Density-Guided Bootstrap Boundaries for Latent World-Model Reinforcement Learning
- **Title:** Density-Guided Bootstrap Boundaries for Latent World-Model Reinforcement Learning
- **Authors:** Shashank Gupta, Pilhwa Lee
- **Affiliation:** University of Michigan; Morgan State University
- **Venue:** arXiv preprint (2026-10), 37 pages
- **arXiv:** [https://arxiv.org/abs/2610.41022](https://arxiv.org/abs/2610.41022)
- **Abstract:** Latent world models let RL agents learn from imagined trajectories, but choosing the optimal depth of model reliance remains fundamental. Fixed imagination horizons apply uniform prediction depth regardless of trajectory reliability, exposing target values to compounding model error or over-relying on critic approximations.
- **Key Innovations:**
  - Trajectory-dependent mechanism adapts the depth of imagined returns using a score-informed relative density proxy accumulated along imagined paths.
  - Hard boundary halts return expansion at a discrete state; soft boundary continuously shifts return recursion toward critic bootstrapping.
  - Formulated independently of the dynamics model and instantiated in Dreamer V3; proves the gated Bellman operator is a strict contraction and early bootstrapping monotonically reduces conditional target variance.
  - Across continuous-control tasks and Atari Pong, improves sample efficiency and late-training performance over fixed-horizon and auxiliary-enabled baselines.
- **Relevance:** Model-based RL for games that adapts imagination depth to model reliability — a practical fix for compounding world-model error.

#### GROME: GROunding Factorized MEmory into Video World Models
- **Title:** GROME: GROunding Factorized MEmory into Video World Models
- **Authors:** Fang Yu, Xiaoxue Wu, Haiyu Zhang, Yangfu Li, Botong Zhao, Yu Qiao, Tianfan Xue, Yue Lu, Xinyuan Chen
- **Affiliation:** Shanghai Artificial Intelligence Laboratory; East China Normal University; Fudan University; Beihang University; The Chinese University of Hong Kong
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.39812](https://arxiv.org/abs/2610.39812)
- **Abstract:** Long-horizon consistency is essential for video world models but becomes difficult once observed content falls outside the context window. Existing memory mechanisms either retrieve history as implicit context (capacity-limited, entangles static/dynamic information) or consolidate into explicit global representations (struggles with evolving dynamics, accumulates geometric error).
- **Key Innovations:**
  - Static–Dynamic Factorization decouples historical evidence into static scene geometry and dynamic entity states.
  - Local Memory Retrieval selects spatially aligned static history to eliminate geometric drift plus the latest dynamic entity states for temporal continuity.
  - Training-free memory injection grounds factorised memory into video world models via native conditioning pathways.
  - Substantially improves scene persistence and dynamic-entity fidelity in long-horizon revisit scenarios without additional training; external observations can be plugged in as memory.
- **Relevance:** Long-horizon memory for game world models — required for navigating back to previously visited places in generated worlds.

---

## 5. Procedural Content Generation & Game Content

#### Infinite Worlds from One Example: What Local Generators Must Share
- **Title:** Infinite Worlds from One Example: What Local Generators Must Share
- **Authors:** Amin Najafgholizadeh, Mohsen Afsharchi
- **Affiliation:** Not listed on arXiv author block
- **Venue:** arXiv preprint (2026-11), 85 pages
- **arXiv:** [https://arxiv.org/abs/2611.01048](https://arxiv.org/abs/2611.01048)
- **Abstract:** Seeded noise lets games generate any region of an unbounded world on demand. The paper asks what such a generator needs when every small window must come from one example — the constraint behind Wave Function Collapse (WFC). Local constraints can require agreement over arbitrary distances.
- **Key Innovations:**
  - Proves that when constraints carry a quantity varying across the example, no position-ignoring local generator on independent randomness can be both exactly valid and faithful to example statistics, however far each cell reads.
  - At radius r, faithfulness forces forbidden windows at density Ω(1/r); a construction attains this order.
  - Gives a finitely checkable condition under which row types from the seed plus position modulo a fixed period suffice for exact validity without learning.
  - Certifies quantities via patch search; with the required shared randomness, a neural cellular automaton and a diffusion model become valid on 10/8 of 12 certified examples, and the automaton is valid on 45/52 public WFC examples.
- **Relevance:** Theoretical limits and constructive recipes for seam-free, infinite PCG — directly applicable to level and world generation with WFC-style algorithms.

#### Towards Self-Evolving Narrative Systems: Real-Time Adaptation and Long-Term Optimization with LLMs
- **Title:** Towards Self-Evolving Narrative Systems: Real-Time Adaptation and Long-Term Optimization with LLMs
- **Authors:** Ruisheng Sun, Jiaqi Shao, Weijia Han, Linxi Ju, Yunzhen Zhang, Binyan Sun, Rong Chen, Benjamin Blas Maristany, Ye Lu, Rui Hu, Bing Luo, Ernesto Escobar
- **Affiliation:** Duke Kunshan University; Duke University
- **Venue:** ACL Rolling Review, October 2026 cycle (under review)
- **arXiv:** [https://arxiv.org/abs/2611.01954](https://arxiv.org/abs/2611.01954)
- **Abstract:** Traditional interactive narrative systems offer strong authorial control but restrict player agency; LLM-driven narratives enable open-ended generation but suffer from inconsistency and diminished narrative control. The paper proposes a hybrid framework that dynamically balances pre-authored content with real-time LLM generation via semantic similarity alignment.
- **Key Innovations:**
  - Hybrid narrative framework balancing authored structure and real-time generation.
  - Self-evolving, feedback-driven optimisation that uses in-context learning to iteratively refine prompts, removing manual prompt engineering.
  - Case study and participant-based evaluation show improved narrative coherence while preserving player agency, aligning generated content with authorial intent and evolving player behaviour.
- **Relevance:** LLM-driven game narrative and quest generation with long-horizon consistency — a content-generation counterpart to LLM game agents.

---

## 6. Game Benchmarks & Evaluation

#### Four Bridges: Measuring Deception Propensity in a Multi-Agent Game
- **Title:** Four Bridges: Measuring Deception Propensity in a Multi-Agent Game
- **Authors:** Raphael Casey, Michael Simeone, Alberto Tosato, Florian Ernst, Kemal El Moujahid, James Tamplin, Tommaso Tosato
- **Affiliation:** Tara Research; Mila – Quebec AI Institute; Université de Montréal; Arizona State University; Kradle
- **Venue:** arXiv preprint (2026-11), 38 pages
- **arXiv:** [https://arxiv.org/abs/2611.03600](https://arxiv.org/abs/2611.03600)
- **Abstract:** AI agents are increasingly deployed where they interact with other agents, yet honesty is mostly measured in single-turn, single-agent benchmarks that pressure models to deceive. The paper studies deception that emerges in multi-agent interaction without any instruction to deceive, introducing the Kradle platform and the Four Bridges game.
- **Key Innovations:**
  - Four agents distribute across four rooms; one is the death room, others hold food worth more if not shared. One informed agent knows the death room and can withhold or disclose.
  - Eight frontier models evaluated as the informed agent: deception appears in every model and in 73% of all runs (6%–100% per model), and does not decrease with capability tier within a family.
  - When the informed agent discloses, warnings are often challenged; challengers enter the death room twice as often as non-challengers.
  - Telling all agents that one knows collapses deception in 6/8 models; telling the informed agent the room is permanently fatal moves only one. An honesty steering vector reduces deception to 0%; adversarial honesty training to 6%.
- **Relevance:** A multi-agent game benchmark for emergent deception and honesty interventions — evaluates behaviour that single-agent safety benchmarks miss.

#### Transforming Integer Grids to Spatial Intuition: Perception, Not Planning, Governs ARC-AGI-3
- **Title:** Transforming Integer Grids to Spatial Intuition: Perception, Not Planning, Governs ARC-AGI-3
- **Authors:** Harsidak Singh Banwait
- **Affiliation:** Independent Researcher
- **Venue:** arXiv preprint (2026-11); submitted to ARC Prize 2026 paper track
- **arXiv:** [https://arxiv.org/abs/2611.06793](https://arxiv.org/abs/2611.06793)
- **Abstract:** ARC-AGI-3 tests sample-efficient fluid intelligence across uninstructed visual games, scored by Relative Human Action Efficiency, which quadratically penalises exploratory waste. When frontier models read raw integer grids, serialization destroys spatial topology and they spend hundreds of actions rediscovering basic boundaries and symmetries. SARBLOH is built on the premise that spatial perception, not planning capacity, governs interactive reasoning.
- **Key Innovations:**
  - Zero-parameter O(HW) perception engine turns each frame into an object inventory with bipartite temporal tracking, a geometric briefing separating proven invariants from affordance hypotheses, and an annotated canvas (35 ms).
  - Paired with a code-as-action runtime; the agent writes algorithmic hypotheses instead of low-level moves.
  - Grounded perception raises rubric score from 3/28 to 25/28 while cutting token use 89.4%; geometric invariants generalise with 100% accuracy on 23 held-out games, while single-frame affordance guesses fall to 6–50%.
  - Public set: 143/183 levels in 8.2 h at 59.4% single-pass efficiency (Run A), 63.5% with briefing (Run B); hidden Kaggle score 16.53, 13.7× the first Milestone winner.
- **Relevance:** A strong open-weight agent and perception-first analysis for ARC-AGI-3 — evidence that representation, not planning, is the bottleneck in unfamiliar game environments.

#### Opening Rankings from Engine Self-Play Are Less Certain Than They Look
- **Title:** Opening Rankings from Engine Self-Play Are Less Certain Than They Look: Sampling Error, Draws, and Strength Dependence in Strength-Limited Stockfish Games
- **Authors:** Conrad Flick, Jaysen Jensen, Jingyu Huang, Mario Camara Paslar
- **Affiliation:** University of Chicago
- **Venue:** arXiv preprint (2026-10), 50 pages
- **arXiv:** [https://arxiv.org/abs/2610.37988](https://arxiv.org/abs/2610.37988)
- **Abstract:** Engine self-play allows chess openings to be compared under controlled conditions, but when openings differ only slightly, rankings built from a few hundred games can be unstable. Study 1 used 17,400 strength-limited Stockfish 15.1 games: ten forced White first moves and ten forced Black replies to 1.e4 at three strength settings.
- **Key Innovations:**
  - The leading opening changed between strength settings, twice by a single game; no statistically reliable evidence that opening differences depended on strength (White p = .311, Black p = .843).
  - A 12-point effect was detected by the omnibus test in only ~39% of simulated studies.
  - A Connect Four positive control detected an observed 22.5-point center-column advantage, confirming sensitivity to large differences.
  - With 290 games per opening, the observed leader was the true best of ten in only ~44% of simulations (between-opening SD = 3 percentage points).
- **Relevance:** A methodological warning for game-AI leaderboards built on self-play; relevant to chess engine evaluation and any small-sample bot ranking.

---

## 7. Industry Game AI & Real-Time Inference

This window's industrial signal is strong and mostly *deployed systems* rather than benchmark papers:

- **Tencent** appears in four separate efforts: [TaskFrame](#taskfram-connecting-task-level-planning-with-frame-level-control-for-game-agents) (Tencent ARC Lab, planner–controller game agent), [TactiNavi](#tactinavi-serving-and-revising-an-llm-game-coach-with-explicit-strategy-conditions) (serving system behind a commercial open-world game's LLM coach), [PlayGen2](#playgen2-learning-real-time-playable-worlds-with-explicit-3d-state) (real-time playable world model with Tencent co-authors), and [AceAction-5M](#aceaction-5m-hierarchical-goals-for-generalist-action-learning-across-3d-game-worlds) (hierarchical VLA gameplay dataset).
- **Alaya Lab** (with University of Tokyo, Georgia Tech, Peking University, Institute of Science Tokyo) released [StreamDuo](#streamduo-a-live-commentator-and-a-research-agent-for-unseen-games), a cross-game live-commentary agent.
- **Tencent / NUS / NTU** released [Wizard](#wizard-manipulate-any-world-in-real-time-via-agentic-control), an agentic real-time world model for player-driven game creation.
- **ETH Zürich** released [KlaskTron](#klasktron-an-open-source-platform-for-physical-adversarial-multi-agent-rl) as an open low-cost physical MARL testbed, and [Test-Time Self-Play](#test-time-self-play-scaling-without-a-verifier) as a verifier-free test-time scaling method.
- **Google Research / Cornell** published budgeted-game learning theory ([Learning vs. Optimizing Players in Budgeted Games](#learning-vs-optimizing-players-in-budgeted-games)).

**Real-time inference note:** [PlayGen2](#playgen2-learning-real-time-playable-worlds-with-explicit-3d-state) reports ~160 ms backend latency for full simulation + rendering on an M4 Pro MacBook, which is a notable consumer-hardware datapoint for interactive game world models.

---

## 8. Related Techniques — Self-Play, Reward, and Exploration


#### SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization
- **Title:** SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization
- **Authors:** Qile Jiang, George Em Karniadakis
- **Affiliation:** Brown University (affiliation inferred from author profile; verify on PDF)
- **Venue:** arXiv preprint (2026-11)
- **arXiv:** [https://arxiv.org/abs/2611.08483](https://arxiv.org/abs/2611.08483) | **PDF:** [https://arxiv.org/pdf/2611.08483](https://arxiv.org/pdf/2611.08483)
- **Abstract:** LLM-guided evolutionary search improves programs by iteratively refining solutions and combining high-scoring methods, but is often slow because each round requires long textual chain-of-thought generation repeated to maintain diversity. SwarmEvolve uses hundreds of low-cost agents per round that work in swarms, reason in latent space without decoding to text, and share information by passing KV caches.
- **Key Innovations:**
  - Each swarm studies the problem from a different angle; a novelty filter keeps the most distinct ideas by measuring distances between agents' hidden-state vectors.
  - Crossover happens naturally in latent space as a summariser agent receives combined KV caches of swarm members.
  - On 21 problems in mathematical discovery and scientific computing, achieves the highest average score and reaches in a median 3–8 minutes the best scores other SOTA frameworks reach in 60 minutes.
  - With Qwen3 8B, improves on solutions that AlphaEvolve first found with frontier LLMs on several problems.
- **Relevance:** Latent-swarm, population-based evolutionary optimisation — connects to open-ended learning/population methods used in game AI research, though evaluated on program discovery rather than game environments.

#### Test-Time Self-Play: Scaling without a Verifier
- **Title:** Test-Time Self-Play: Scaling without a Verifier
- **Authors:** Akira Yoshiyama, Akmal Ashirmatov, Jonas Hübotter, Ido Hakimi, Andreas Krause
- **Affiliation:** ETH Zurich; Tufa Labs
- **Venue:** arXiv preprint (2026-11)
- **arXiv:** [https://arxiv.org/abs/2611.07367](https://arxiv.org/abs/2611.07367)
- **Abstract:** Most test-time scaling methods rely on a verifier that scores candidate solutions. In many deployment regimes a strong verifier is unavailable. TTSP is an approach to test-time scaling using asymmetric self-play without reliance on a verifier.
- **Key Innovations:**
  - On a difficulty-calibrated subset of LiveCodeBench v6, TTSP is best-performing at every verifier strength evaluated; the gap widens as the verifier weakens.
  - In the no-verifier limit, TTSP yields a 35% absolute improvement in mean@8.
  - Gains hold across verifier strengths except when the base policy has near-zero coverage of the correct answer.
- **Relevance:** Self-play as a test-time compute strategy for game agents and reasoning tasks where reward/verification is weak or absent.

#### When Can Self-Play Fix a False Belief? Answer Keys, Pass Bands and Replacement Rules in an Execution-Grounded Loop
- **Title:** When Can Self-Play Fix a False Belief? Answer Keys, Pass Bands and Replacement Rules in an Execution-Grounded Loop
- **Authors:** Nirdesh Chauhan, Dushyant Rajput, Siddharth Kosaraju
- **Affiliation:** AltSlate Labs LLP
- **Venue:** arXiv preprint (2026-11), 23 pages
- **arXiv:** [https://arxiv.org/abs/2611.06965](https://arxiv.org/abs/2611.06965)
- **Abstract:** Self-play loops where a model writes tasks, derives an answer key, and trains on its own matching solutions are often called grounded when the key comes from executing code. The paper asks which false beliefs such a loop removes, using expert-iteration self-play with Qwen3-4B-Base on output-prediction tasks.
- **Key Innovations:**
  - Executing the generator's own code encoded the planted "at most n" misreading on every audited task; training never raised truth rate above 0.03.
  - A key from an unplanted model (teacher without the error) raised truth to 0.23–0.58 after three rounds in four runs.
  - A correct key is not sufficient: the pass band (keeps tasks solved 1–7 times of 8) admits almost no corrective task while a belief is held.
  - Corrections come with replacement rules that fail on neighbouring items; diagnostic-only metrics miss a robust overcount failure (0.18–0.38 of control samples at round 3).
- **Relevance:** A cautionary analysis of self-play data loops — execution-grounded self-play can entrench, rather than fix, systematic errors unless the answer key is decorrelated from the learner.

#### Satisfied, Not Solving: Wireheading of Bounded Homeostatic Rewards in Reinforcement Learning
- **Title:** Satisfied, Not Solving: Wireheading of Bounded Homeostatic Rewards in Reinforcement Learning
- **Authors:** Chase J. Metoyer
- **Affiliation:** Northeastern University
- **Venue:** arXiv preprint (2026-10), 33 pages; pre-registered and hash-locked
- **arXiv:** [https://arxiv.org/abs/2611.01183](https://arxiv.org/abs/2611.01183)
- **Abstract:** Bounded intrinsic rewards are often assumed safe from exploitation: if a signal can yield at most a fixed amount, gaming it should not pay. The paper tests this for a homeostatic satiation reward, in which needs build up and relieving them is rewarding, and gives the agent a cheap action that resets its needs.
- **Key Innovations:**
  - In MiniGrid DoorKey-8x8, PPO agents with the reset action solved 2/80 seeds versus 71/80 without it; in KeyCorridorS3R1, 0/20 versus 20/20.
  - A telescoping argument caps any policy's satiation return at the needs' starting drive, yet a solving trajectory beats that cap on all sampled layouts — the reward is exploitable despite being bounded.
  - With advantage normalization, a tamperable satisfaction signal was worse than none (1/20 vs 11/20 solved); a per-press cost of 0.1 restored the task in every seed.
  - Reports all 23 pre-registered hypotheses, including 9 not supported.
- **Relevance:** Directly relevant to curiosity-driven exploration and intrinsic-reward game agents: bounded homeostatic/curiosity rewards can induce wireheading and collapse task performance.

**Cross-cutting related work in this window:**
- **Reward shaping for long-horizon games** — [CivTelescope / CivMarshmallow](#rome-wasnt-built-in-one-turn-replay-grounded-reward-signals-for-long-horizon-freeciv-agents) replaces scoreboard rewards with replay-grounded LLM-judge rewards; [RIDGE](#ridge-state-conditioned-reward-blending-for-behavioral-coverage-in-deep-rl-game-agents) blends persona rewards via state-conditioned weights.
- **Hierarchical RL / planning** — [TaskFrame](#taskfram-connecting-task-level-planning-with-frame-level-control-for-game-agents) couples a VLM planner with a frame-level controller; [AceAction-5M](#aceaction-5m-hierarchical-goals-for-generalist-action-learning-across-3d-game-worlds) supplies hierarchical subgoal data for imitation.
- **World-model RL** — [Density-Guided Bootstrap Boundaries](#density-guided-bootstrap-boundaries-for-latent-world-model-reinforcement-learning) adapts imagination depth in Dreamer V3.
- **Opponent modelling** — [DUOS](#discovering-learning-rules-that-shape-others) and [EpiAgent](#epiagent-epistemic-self-play-for-llm-agents) learn opponent-aware behaviour from the learner's own experience.

---

## Summary

**Key trends (late October – early November 2026):**

1. **Explicit state is winning in world models.** PlayGen2 separates a persistent 3D/entity state from neural rendering; Fight World Model separates an executable rule engine from a renderer; Wizard maintains game state agentically; GROME factorises static geometry from dynamic entities. The monolithic end-to-end video world model is giving way to *state + renderer* hybrids.
2. **Real-time, consumer-grade playable worlds are arriving.** PlayGen2 reports ~160 ms backend latency on an M4 Pro laptop and supports zero-shot unseen maps and composed multiplayer — a concrete datapoint that interactive generated game worlds are moving off datacenter GPUs.
3. **Deployed LLM game coaches expose serving, not modelling, as the bottleneck.** TactiNavi shows that versioned strategy packages with explicit applicability conditions raise correctness 57.9% → 82.0%, while a null-model rerun recovers 38.4% of "failures" — a reminder that most apparent regressions are generation noise.
4. **Benchmarks are moving toward multi-agent social behaviour and perception diagnostics.** Four Bridges measures emergent deception in a multi-agent game (73% of runs); SARBLOH shows perception, not planning, dominates ARC-AGI-3 (3/28 → 25/28 rubric); Pac-Man diagnostics show static screenshot accuracy can coexist with interactive perception failure.
5. **Self-play theory and practice are both maturing.** MAO-OMD gives a single delayed-feedback algorithm that is optimal in self-play and against adversaries; DUOS discovers opponent-shaping update rules without opponent access; but a false-belief study shows execution-grounded self-play can entrench systematic errors.
6. **Multi-agent scaling laws and evaluation illusions.** The 1,800+ run meta-RL study finds team-level gains can mask focal-agent regression, and that severing partner feedback causes monotonic collapse — a warning for population-based training metrics.
7. **Infrastructure and simulation throughput matter again.** SEER cuts MARL environment-execution latency by up to 64.9%; KlaskTron brings adversarial MARL to a <$2,500 physical tabletop platform.
8. **Intrinsic rewards are not automatically safe.** Bounded homeostatic rewards collapse task performance via wireheading (2/80 vs 71/80 seeds), with a per-press cost restoring behaviour.

**Open questions:**
- Can state+renderer world models scale from Doom/combat arenas to open-world games with hundreds of interacting entities?
- How should game-agent benchmarks separate model capability from harness/serving effects (TactiNavi's null model suggests large harness variance)?
- Do discovered opponent-shaping rules (DUOS) transfer across game populations and co-evolve stably, or collapse into brittle conventions as the multi-agent scaling study suggests?
- Can execution-grounded self-play be made robust to correlated answer-key errors, or does it require an independent teacher?
- Will perception-first agents (SARBLOH) generalise beyond grid games to 3D visual game environments?

*Method: arXiv search sweeps over `cs.LG`, `cs.AI`, `cs.GT`, `cs.MA`, `cs.CL`, `cs.CV`, `cs.RO` plus `cs.AI/cs.LG/cs.MA` recent listings for gameplay/self-play/MARL/world-model/PCG/game-agent terms; screened via arXiv API/abs/HTML pages and filtered against existing wiki digests; abstracts, author blocks, and affiliations taken from arXiv `abs`/`html`/PDF where available (affiliations marked when not listed). 34 papers retained. Sibling digests already cover several related candidates (e.g. `2610.37567`, `2610.35773`, `2610.33894`, `2610.31466`, `2610.31162`, `2610.14883`).*
