---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-10-30)"
type: synthesis
created: 2026-10-30
updated: 2026-10-30
sources: []
tags: [game-rl, game-ai, llm-agents, reinforcement-learning, self-play, foundation-models, procedural-content-generation, benchmarks, world-models, vlm, multi-agent-rl, game-theory, daily-digest]
---
# Game RL & Game AI Bot — Daily Paper Digest (2026-10-30)

*Window: arXiv submissions and announcement batches from roughly 2026-10-19 to 2026-10-27. 25 new papers across Game RL, LLM game agents, game world/foundation models, procedural content generation, benchmarks, industry deployment, and related techniques. Papers already covered by the sibling `2026-10-20` through `2026-10-30` digests are excluded; cross-references are noted inline.*

> ⚠️ All performance numbers below are **author-reported** and have not been independently reproduced. Affiliations are taken from arXiv HTML/PDF author blocks; where the paper lists none, this is stated explicitly rather than inferred.

---

## 1. Game RL — Reinforcement Learning in Games

### 1.1 Game-Theoretic Learning, Self-Play, and Equilibrium Selection

#### Conservative Policy Iteration for Zero-Sum POSGs
- **Title:** Conservative Policy Iteration For Zero-Sum POSGs
- **Authors:** Erwan C. Escudie, Matthia Sabatelli, Jilles Steeve Dibangoye
- **Affiliation:** University of Groningen
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.36847](https://arxiv.org/abs/2610.36847)
- **Abstract:** Occupancy-state reductions make dynamic programming possible for zero-sum partially observable stochastic games (zs-POSGs). Existing point-based solvers usually optimise a central value function, which restores Bellman recursion but requires point-based updates over high-dimensional occupancy spaces. The paper introduces an approximate policy-iteration algorithm for finite-horizon zs-POSGs that maintains one policy per player and updates both jointly along occupancy trajectories induced by conservative policy updates.
- **Key Innovations:**
  - Joint per-player policy iteration instead of a single central value function.
  - Each update uses a single supporting hyperplane induced by the current joint policy, concentrating computation on exploitable occupancy regions.
  - Alternates local policy improvement, conservative updates, and persistent exploration.
  - Competitive at small horizons and often better runtime–exploitability trade-offs at larger horizons versus PBVI, HSVI, and CFR+.
- **Relevance:** Directly targets imperfect-information two-player games (poker-like / pursuit-evasion abstractions) where occupancy-state methods are the main scalable alternative to tabular game solving.

#### Noise Shapes the Surplus: Strategic Play Against No-Regret Learners
- **Title:** Noise Shapes the Surplus: Strategic Play Against No-Regret Learners
- **Authors:** Yiheng Su, Emmanouil-Vasileios Vlatakis-Gkaragkounis
- **Affiliation:** University of Wisconsin–Madison
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.36621](https://arxiv.org/abs/2610.36621)
- **Abstract:** Prior work showed that in zero-sum games an optimizer can extract Ω(√T) strategic surplus against noiseless no-regret learners with a constant step size. In practice learners act on perturbed payoff scores and use decaying learning rates η_t. This paper asks whether noise shields the learner from exploitation, for the widely used Follow-the-Regularized-Leader (FTRL) family.
- **Key Innovations:**
  - Three results that do **not** assume independence of the noise.
  - Passive play against a fixed strategy earns at most constant surplus under summability conditions.
  - A clairvoyant mechanism exploits the learner's noise-dependent response to secure Ω(1/η_T) surplus when the limiting mean response is profitable.
  - Active alternating play extracts Ω(Σ_t η_t) surplus even when the mean is not profitable, by exploiting learner movement rather than location.
  - At η_t ∝ t^(−1/2), recovers the noiseless Ω(√T) rate for mean-zero finite-variance perturbations.
- **Relevance:** Sharpens the theory of exploiting learning opponents in repeated games — relevant to opponent modeling, poker/bargaining bots, and algorithmic-market games.

#### The Complexity of Strategizing Against No-Regret Learners: Pure When It Is Easy, Hard Even When Mixed
- **Title:** The Complexity of Strategizing Against No-Regret Learners: Pure When It Is Easy, Hard Even When Mixed
- **Authors:** Yiheng Su, Emmanouil-Vasileios Vlatakis-Gkaragkounis
- **Affiliation:** University of Wisconsin–Madison
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.36261](https://arxiv.org/abs/2610.36261)
- **Abstract:** Studies the computational complexity of clairvoyant strategy optimization against a known online learner in finite-horizon repeated games. In general-sum games with bounded payoffs, unless P = NP, no polynomial-time optimizer can achieve a reward within cT of the optimal pure-action sequence for an absolute constant c > 0, even when allowed to output explicitly represented mixed strategies every round.
- **Key Innovations:**
  - Hardness extends to a broader class of learning dynamics including mean-based algorithms, answering an open question of Assos, Dagan, and Rajaraman (2025).
  - Mixed outputs do not remove the computational obstruction in general-sum games.
  - Striking mirror image: in zero-sum games deterministic pure actions suffice to recover the leading surplus guarantees previously obtained via mixed play against FTRL.
- **Relevance:** Delimits when "exploit the learner" is computationally feasible, with direct implications for opponent-aware game bots and multi-agent training curricula.

#### TANDEM: Balancing Centralized and Decentralized Critics to Address the Information Gap in Complex Multi-Agent Environments
- **Title:** TANDEM: Balancing Centralized and Decentralized Critics to Address the Information Gap in Complex Multi-Agent Environments
- **Authors:** Alireza Saleh Abadi, Leen-Kiat Soh, Adam Eck, Prashant Doshi
- **Affiliation:** University of Nebraska–Lincoln; Oberlin College
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.37592](https://arxiv.org/abs/2610.37592)
- **Abstract:** CTDE shapes decentralized policies with a centralized critic that observes global state, then removes the critic at execution — leaving an information gap. The gap widens under partial observability, observation noise, and openness (agents/tasks changing within an episode). TANDEM keeps one centralized critic but reads it two ways at each step: a centralized read from global state and a decentralized read restricted to what each agent will actually observe at execution.
- **Key Innovations:**
  - Parameter-free gate compares the two critic reads per agent; trains on the decentralized read where they agree and reinstates centralized guidance only where the local view is misleading.
  - Shared target pulls the decentralized read toward the centralized one, so policies rehearse acting without the critic while still correctable.
  - Formalizes task- and agent-open Dec-POMDP (TAO-Dec-POMDP).
  - Evaluated on discovery (partial observability), sampling (observation noise), and wildfire suppression (openness) against six CTDE baselines.
- **Relevance:** Addresses a core failure mode of centralized-training game agents in open, noisy multi-agent games.

#### Centralized Critics for N-Agent Ad Hoc Teamwork
- **Title:** Centralized Critics for N-Agent Ad Hoc Teamwork
- **Authors:** Andrew McAlinden, Caroline Wang, Steven Shi, Arrasy Rahman, Elad Liebman, Peter Stone
- **Affiliation:** Not listed on arXiv (author block omits affiliations)
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.34799](https://arxiv.org/abs/2610.34799)
- **Abstract:** CTDE has become the dominant MARL paradigm, but centralized-critic design for N-agent ad hoc teamwork (NAHT) — where a varying set of learning agents must coordinate with arbitrary uncontrolled teammates from an unknown distribution — remains poorly understood. The paper compares two advantage estimators: controlled-history estimators (only the learner's own agents) and joint-history estimators (also conditioning on uncontrolled teammates' histories).
- **Key Innovations:**
  - Proves both estimators are unbiased.
  - Characterizes conditions under which joint-history estimates have strictly lower variance.
  - Empirically, joint-history critics match or outperform controlled-history critics across NAHT tasks, improving sample efficiency and final return.
- **Relevance:** Provides theory and a practical recommendation for game agents that must cooperate with unknown human or scripted teammates.

#### Preference-Guided Cooperation in Multi-Objective Multi-Agent Reinforcement Learning
- **Title:** Preference-Guided Cooperation in Multi-Objective Multi-Agent Reinforcement Learning
- **Authors:** Qiyue Xia, J. Michael Herrmann
- **Affiliation:** University of Edinburgh
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.35736](https://arxiv.org/abs/2610.35736)
- **Abstract:** MOMARL must handle agent coordination and objective trade-offs simultaneously. Existing work treats cooperation and multi-objective optimization as largely independent, which is exorbitantly complex except in trivial cases. This paper asks whether the structure provided by multiple objectives can itself facilitate cooperation.
- **Key Innovations:**
  - Formulates MOMARL at team and individual levels.
  - Objective-wise counterfactual credit assignment to evaluate each agent's contribution across team objectives.
  - Meta-Gradient Informed MOMARL (MIRL), with static (MIRL-S) and dynamic (MIRL-D) variants; agents learn how to prioritize objectives individually while collectively optimizing the system objective.
  - On a multi-objective multi-particle environment, improves Pareto-front quality; dynamic variant strongest.
- **Relevance:** Multi-objective reward structures are common in strategy games (economy vs. military vs. territory); objective-wise credit is a transferable mechanism.

#### Program-Level Adversarial Co-Adaptive Self-Play for Robotic Security
- **Title:** Program-Level Adversarial Co-Adaptive Self-Play for Robotic Security
- **Authors:** Leo Benaharon, Chi Zhang, Wei Zheng, Weifan Zhang, Yifan Wei
- **Affiliation:** Isuzu Technical Center of America; Purdue University
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.36143](https://arxiv.org/abs/2610.36143)
- **Abstract:** Coding agents can adapt robotic software by revising executable programs, but successful responses to an evolving opponent may not remain effective. The paper presents program-level adversarial co-adaptive self-play in which coding agents generate attacks and defenses from tested opponent code and mission feedback, without model fine-tuning.
- **Key Innovations:**
  - Environment-specific interfaces for autonomous driving and SDK-level humanoid locomotion defenses.
  - Two eight-generation case studies: a driving defender introduces direct-actuation recovery; a humanoid defender revises incoming-state validation.
  - Responses provide local task recovery but do **not** establish sustained robustness.
  - Makes adaptation and its limits observable via executable artifacts and task-level evidence.
- **Relevance:** Self-play over *programs* rather than policies; a useful template for game bot co-evolution and adversarial content generation.

#### SpecMAGIC: Specification-Guided Multi-Task Generalization in Multi-Agent Reinforcement Learning
- **Title:** SpecMAGIC: Specification-Guided Multi-Task Generalization in Multi-Agent Reinforcement Learning
- **Authors:** Zijian Guo, İlker Işık, H. M. Sabbir Ahmad, Wenchao Li
- **Affiliation:** Boston University
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.30443](https://arxiv.org/abs/2610.30443)
- **Abstract:** Multi-task generalization is underexplored in MARL. Many applications require multi-agent systems to generalize across temporally extended tasks with diverse inter-agent coordination requirements. The paper introduces a specification language combining temporal-logic task specifications with operators for expressing coordination requirements.
- **Key Innovations:**
  - Hierarchical framework using the automaton structure of specifications for subtask decomposition.
  - Centralized high-level planner allocates compatible subtask sequences across agents; decentralized low-level policies execute subtasks.
  - Zero-shot generalization to new tasks by recomposing reusable subtask policies according to new specifications, without retraining.
  - Soundness and probabilistic completeness of the high-level planner; strong results on multi-agent navigation as agent count grows.
- **Relevance:** Specification-driven composition is a promising route to generalist multi-agent game players.

#### Vulnerability Analysis for Safe Multi-Agent Reinforcement Learning
- **Title:** Vulnerability Analysis for Safe Multi-Agent Reinforcement Learning
- **Authors:** Taozheng Zhu, Shixiong Jiang, Fanxin Kong
- **Affiliation:** University of Notre Dame
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.27293](https://arxiv.org/abs/2610.27293)
- **Abstract:** Safe MARL (SMARL) enforces safety constraints during policy optimization, but its vulnerability is largely unexplored. This paper studies inference-time observation attacks where an adversary perturbs a subset of agents' observations and thereby changes their actions.
- **Key Innovations:**
  - MinMax Attack jointly selects adversarial target actions for compromised agents while accounting for the Cooperative Resistance of benign agents.
  - Derives a bound on induced safety cost and relates it to Compromised-Agent Budget and Perturbation Budget.
  - Across safety-critical multi-agent benchmarks and SOTA SMARL algorithms, induces substantially higher safety cost than attack baselines while preserving task reward (stealthiness).
- **Relevance:** Red-teaming for game agents and safety-critical multi-agent sims; shows safety constraints alone do not confer robustness.

#### One Act, Many Masks: Effect-Marginal Policy Optimization for Long-Horizon Agents
- **Title:** One Act, Many Masks: Effect-Marginal Policy Optimization for Long-Horizon Agents
- **Authors:** Shaojin Ma, Ruitao Wang, Pengyi Li, Jie Yang, Liangyu Chen, Gangyi Zhao, Hongyao Tang, Yan Zheng, Jianye Hao
- **Affiliation:** Tianjin University; Fudan University; Renmin University of China
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.29427](https://arxiv.org/abs/2610.29427)
- **Abstract:** Multi-turn RL has improved LLM agents on long-horizon interactive tasks, but policy optimization still applies credit through response-specific probability ratios. Different textual responses can induce the same executable effect, yet credit differences from subsequent outcomes remain tied to individual textual realizations — a mismatch the authors call *credit-update misalignment*.
- **Key Innovations:**
  - Shows credit–text pairing directly shapes policy-update directions even when policy context and executable effect are fixed.
  - Effect-Marginal Policy Optimization (EMPO) aligns updates with execution-level equivalence via an effect-level surrogate that couples updates across alternative textual realizations.
  - Preserves original credit signals; integrates with trajectory- and step-level credit estimators; no extra critics or rollouts.
  - Outperforms strong baselines on ALFWorld, WebShop, and Sokoban.
- **Relevance:** Directly applicable to LLM game agents where many text actions map to the same game command; Sokoban is the explicit game testbed.

#### Short-to-Long: Detached Features for Long-Horizon Value Learning
- **Title:** Short-to-Long: Detached Features for Long-Horizon Value Learning
- **Authors:** Tong Che, Boris Ivanovic, Marco Pavone
- **Affiliation:** NVIDIA Research
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.30461](https://arxiv.org/abs/2610.30461)
- **Abstract:** Learning representations from continually changing value targets is hard in deep RL. Smaller discounts make targets less sensitive to distant bootstrap changes, but using them for behavior changes the control objective. Short-to-Long (S2L) supplies a long-horizon behavior learner with features trained by smaller-discount source networks.
- **Key Innovations:**
  - Detached connections prevent the behavior value loss from updating the sources, so each source follows its own value objective while the behavior discount remains unchanged.
  - Gains across Atari, online continuous control, and offline continuous control.
  - Improves paired terminal median on 40 of 57 Atari games.
  - Matched ablations isolate feature transfer, smaller source discounts, and gradient isolation; fixed-trajectory measurements show reduced drift in source value targets.
- **Relevance:** A simple, general value-learning recipe for long-horizon game control.

---

## 2. Game AI Bots — LLM-Powered Game Agents

#### Gym-Anything-RT: Scaling Real-Time Environments for Vision-Language Agents
- **Title:** Gym-Anything-RT: Scaling Real-Time Environments for Vision-Language Agents
- **Authors:** Pranjal Aggarwal, Sean Welleck
- **Affiliation:** Carnegie Mellon University
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.37567](https://arxiv.org/abs/2610.37567)
- **Abstract:** AI agents have progressed in domains with time to deliberate (math, software engineering, desktop apps), but it is unclear how they fare when the environment evolves during reasoning or even during a forward pass. Gym-Anything-RT constructs visual minigames that demand six capabilities required for real-time interaction, using an agentic pipeline to generate environments automatically.
- **Key Innovations:**
  - Controlled comparison: the same minigame can run in real time, paused, or slowed down.
  - 100 generated real-time minigames evaluated across frontier agents.
  - Large real-time gap: GPT-6 Astra (xHigh) passes only 9.0% in real time, rising to 75.0% when paused.
  - Frontier agents with code access write code that bypasses the need to perceive and act in real time.
  - Environments and minigames released.
- **Relevance:** The clearest 2026 measurement of the "real-time tax" on LLM game agents; also a warning that code-execution harnesses can shortcut embodied game benchmarks.

#### A Unified Arena for LLM Agents across Diverse Eurogames (DECE)
- **Title:** A Unified Arena for LLM Agents across Diverse Eurogame
- **Authors:** Fengrui Zhang, Xiang Li, Ruomeng Ding, Jiayi Yuan, Yuchen Huang, Zhaoyang Han, Xiaoliang Wang, Daoyuan Chen, Yaliang Li
- **Affiliation:** Alibaba Group; Nanjing University; National University of Singapore; UNC Chapel Hill; HKUST
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.35773](https://arxiv.org/abs/2610.35773)
- **Abstract:** Competitive games extend agent evaluation to decisions shaped by competing goals and other agents' choices, but existing evaluations are confined to individual games or frameworks. DECE is a unified arena spanning ten Eurogames with shared interfaces and evaluation protocols, combining lasting strategic commitments, shared-resource competition, and multiple victory routes.
- **Key Innovations:**
  - Primary study: 12 model–harness configurations (9 models, 4 harnesses) in 480 three-player matches across ten games; 1,032 completed matches total with supplementary studies.
  - Broad cross-game ranking agreement alongside game-specific strengths.
  - The same model can perform differently across execution harnesses, adding a major source of variance.
  - Competitive advantage does not consistently translate into token or cost efficiency; recommends evaluating complete configurations on both performance and resources.
- **Relevance:** Directly addresses benchmark validity for LLM game agents: harness choice is a first-class variable, not a detail.

#### AI Teaches Humans to Handle Complexity in the Game of Go
- **Title:** AI Teaches Humans to Handle Complexity in the Game of Go
- **Authors:** Adamo Cerioli, Vito D. P. Servedio, Gabriele Cerioli, Antonio Villani, Carlo Metta
- **Affiliation:** University of Parma; Complexity Science Hub Vienna; University of Trieste; NEST-IIT
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.33323](https://arxiv.org/abs/2610.33323)
- **Abstract:** Uses Go as a bounded testbed to study how biological and artificial agents balance local stability against global coordination. Introduces a network-derived metric of strategic tension defined via the spectral radius of spatial dependency matrices.
- **Key Innovations:**
  - Across human skill progression, tension decays from novices to masters as tactical skirmishes give way to territorial stabilization.
  - Longitudinal analysis of professional play 1980–2026 finds a historical paradox: after AlphaGo (2016), elite human matches show a marked surge in sustained tension.
  - A 2-D projection based on move distance and captures places modern professionals close to neural engines.
  - Argues strategic tension is a macroscopic order parameter for decision paradigms, not raw computational strength.
- **Relevance:** Human–AI co-evolution in games; evidence that superhuman game AI changes human strategic style, not just human tooling.

#### Feedback That Backfires in Games: Do LLM Players Repeat the Move They Just Watched Fail?
- **Title:** Feedback That Backfires in Games: Do LLM Players Repeat the Move They Just Watched Fail?
- **Authors:** Esmail Gumaan
- **Affiliation:** University of Passau
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.30205](https://arxiv.org/abs/2610.30205)
- **Abstract:** When an LLM agent's move fails, the harness writes the move and failure message into the transcript and asks again. In tool calling this record makes small models more likely to repeat the failed action. The paper tests whether the same holds in games (Sokoban, Connect Four, Othello), where failure is exactly verifiable as illegal or legal-but-losing.
- **Key Innovations:**
  - On fixed probe items, the failure record backfires: pooled over 8 instruction-tuned models (135M–1.7B), corrective gain G = −1.38 nats per token.
  - Effect operates through the move's surface form, for illegal moves but not losing ones, and not for every model.
  - After the record, the failed move's log-probability barely depends on its prior likelihood (slope 0.18).
  - A failure description that omits the move string preserves model preference; "do not repeat" instructions do nothing; a clean retry is the worst harness; decoder bans stop exact repeats but not illegal play.
  - Along the OLMo 2 1B post-training ladder, inversion is present in the base model and largely removed at DPO.
- **Relevance:** A concrete, reproducible failure mode for LLM game-agent harnesses — and a caution for agent loops that naively append errors.

#### AgentMonopoly: Behavioral Patterns and Persona Control in LLM Agents
- **Title:** AgentMonopoly: Behavioral Patterns and Persona Control in LLM Agents
- **Authors:** Changshun Wu, Mengyu Li, Mathis Marsault, Xiaowei Huang, Chih-Hong Cheng
- **Affiliation:** University of Liverpool; Carl von Ossietzky University of Oldenburg; Chalmers University of Technology
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.29330](https://arxiv.org/abs/2610.29330)
- **Abstract:** Studies how LLM agents' strategies differ and how much persona instructions change behavior over a game. AgentMonopoly is an environment where agents communicate, buy and trade properties, and make decisions affecting later turns.
- **Key Innovations:**
  - Compares four model families at two sizes, in same-model, same-family-different-size, and cross-family games.
  - Models differ in trade frequency, rent waiving, and cash/property management; larger models do **not** consistently win more games.
  - Persona instructions change language and some actions, but changes do not always match the role across all decisions.
  - Argues persona following should be assessed through actions and outcomes as well as language.
- **Relevance:** NPC/persona design for LLM-driven game characters; open-source environment for controlled behavioral studies.

---

## 3. Game Foundation Models & Interactive World Models

#### BoxWorld: Let World Engines Control and Video Generators Render
- **Title:** BoxWorld: Let World Engines Control and Video Generators Render
- **Authors:** Zike Wu, Ahmed Hatem, Chintan Trivedi, Wallace Michel Pinto Lira, Xuebin Qin, Lele Wang, Renjie Liao
- **Affiliation:** University of British Columbia; Vector Institute for AI; Huawei Canada
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.36371](https://arxiv.org/abs/2610.36371)
- **Abstract:** Real-time interactive video worlds with user-defined behaviors must track object states, apply interaction rules, and render consequences as users act. End-to-end video world models usually learn interaction dynamics inside the generator, making object-level rules hard to specify and reason about. BoxWorld separates interaction reasoning from generative rendering.
- **Key Innovations:**
  - A coding agent creates a **Box World Engine** from user-specified rules; it exposes layout boxes, persistent object attributes, and dynamic status variables.
  - A Box-State Generative Renderer autoregressively renders the evolving state stream into video, enabling online control over motion, state switches, and conditional events.
  - Three-stage training: object grounding from open-domain video, state transitions from gameplay video (both auto-annotated), then rollout distillation on self-generated histories.
  - Introduces **PairedStateBench**, a paired benchmark for fine-grained state fidelity.
- **Relevance:** A modular alternative to monolithic game world models; separates symbolic game logic from neural rendering, which is attractive for controllable game generation.

#### World-in-Context: Interactive Video World Modeling with In-Context Conditioning
- **Title:** World-in-Context: Interactive Video World Modeling with In-Context Conditioning
- **Authors:** Harold Haodong Chen, Rui Peng, Rongjin Guo, Lingteng Qiu, Kejie Qiu, Chao Xu, Zilong Dong
- **Affiliation:** Alibaba Token Hub, Alibaba Group
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.33169](https://arxiv.org/abs/2610.33169)
- **Abstract:** Interactive video world models require coordinated control over viewing perspectives, character actions, and camera motion. Existing methods leave view modes implicit in captions, conflate action with camera motion, and inject controls through fragmented pathways. World-in-Context unifies view, action, and camera controls into explicit tokens contextualized in a shared self-attention space (In-Context Conditioning, ICC).
- **Key Innovations:**
  - Explicit view tokens disentangle conflicting dynamics and unlock emergent view switching from single-view data.
  - Action and camera inputs play complementary roles in local responsiveness and global stability.
  - Interaction-Transport RoPE (IT-RoPE) parameterizes temporal attention with accumulated control transitions to preserve continuity across execution intervals.
  - World-in-Context-5B matches 22B EchoWM on WBench navigation (81.5 vs. 81.6) and reaches 93.8% perspective-switching success vs. 18.8% for existing 5B baselines.
- **Relevance:** Directly targets playable, multi-view game world models at a fraction of prior parameter cost.

#### Tempo-Zero: Recursive Self-Play in Executable Worlds for Video Reasoning
- **Title:** Tempo-Zero: Recursive Self-Play in Executable Worlds for Video Reasoning
- **Authors:** Jingmin Zhu, Yanyan Zou, Xiuyu Li, James Bailey, Dinh Phung, Tao Yu, Yunyun Hou, Jun Liu, Jun Zhou, Sirui Wang, Nan Duan, Jiachen Liu, Qiuhong Ke
- **Affiliation:** JD.com; Monash University; Institute of Automation, Chinese Academy of Sciences; Communication University of China; Lancaster University; Griffith University
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.32433](https://arxiv.org/abs/2610.32433)
- **Abstract:** Video reasoning requires understanding temporal event structure, but accurate temporal annotations are expensive. Existing video self-play methods train on fixed recorded videos, cannot alter event dynamics, and rely on noisy pseudo-labels. Tempo-Zero closes a loop of executable environments, execution-verified self-play, and environment evolution: executing a program renders a video with ground-truth option and interval for every question.
- **Key Innovations:**
  - A single policy plays both Questioner and Solver, proposing questions and answering with timestamped evidence lines.
  - Trained on execution-grounded rewards instead of model consensus.
  - Solver performance steers a curriculum over tasks and difficulty; the policy selects rule changes that enrich later event dynamics.
  - Trained only on simple programs, without SFT or external video data, yet outperforms base models and recent self-play baselines across twelve real-world video benchmarks at multiple model scales.
- **Relevance:** Self-play with verifiable, executable environments; a clean example of moving beyond recorded-video curricula toward generated game-like dynamics.

#### WorldStream: Streaming Interactive 3D Worlds with Hierarchical Planning and Persistent State
- **Title:** WorldStream: Streaming Interactive 3D Worlds with Hierarchical Planning and Persistent State
- **Authors:** Xiaoxiao Ma, Weiyang Jin, Yanwen Ma, Haoran Li, Zhixiang Wei, Songchun Zhang, Yaowei Li, Junhao Zhuang, Zeyue Xue, Yuming Li, Zheming Fu, Haoyang Huang, Nan Duan, Feng Zhao
- **Affiliation:** University of Science and Technology of China; Joy Future Academy, JD
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.28827](https://arxiv.org/abs/2610.28827)
- **Abstract:** Presents an open-ended 3D world model with three simultaneous capabilities: extending playable terrain beyond any pre-specified map, acting on open-ended language in the running world, and restoring visited places with their edits.
- **Key Innovations:**
  - Hierarchical planner over a typed decision model: **Macro** fixes settlement, ecology, transport, and hydrology across tiles; **Micro** specializes the contract into tile semantics under measured terrain and accepted neighbor commitments.
  - Deterministic local code compiles accepted plans into terrain, roads, settlements, vegetation, and entities.
  - Streaming separates plan reach from compilation radius and releases geometry behind the user.
  - A single world record retains plans, seeds, object identities, mutable state, boundary commitments, and attribute edits; returning tiles recompile from it.
  - Stateful NPCs update as they act; the model can attach intent to unplanned regions.
- **Relevance:** Persistent, editable world state is the missing ingredient for long-horizon game agents and generated open worlds.

---

## 4. Procedural Content Generation

#### VibeGame: Prompt-to-Game Development with AI-Native Engine and Self-Evolving Adversarial Agent Team
- **Title:** VibeGame: Prompt-to-Game Development with AI-Native Engine and Self-Evolving Adversarial Agent Team
- **Authors:** Wenbo Hu, Ken Li, Jiazhe Wei, Yukang Cao, Weiyi Hong, Jiayi Dai, Chenjun Bai, Jiajun Liang, Yucheng Liao, Ruichuan An, Zeyu Lou, Haofan Wang, Yueming Lyu, Jingkang Yang, Ziwei Liu, Chenyang Si
- **Affiliation:** PRLab, Nanjing University; S-Lab, Nanyang Technological University; Liblib.ai
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.33106](https://arxiv.org/abs/2610.33106)
- **Abstract:** LLM agents enable software development through natural language, but end-to-end game development remains hard: it requires coordinating code, scenes, assets, animations, physics, and configurations, plus interactive validation. VibeGame creates complete 2D game projects from prompts and optional reference images.
- **Key Innovations:**
  - AI-native game engine represents project state as schema-validated structured text with frame-synchronous runtime control, so agents can inspect state, execute actions, and verify behavior at their own pace.
  - Adversarial Agent Team of eight specialized agents separates implementation from review, finding and fixing problems through multi-round loops.
  - Training-free self-evolution distills accepted projects into reusable skeletons, modules, and collaboration contracts.
  - Evaluates prompt-assets-to-game (PA2G) and prompt-to-game (P2G); on a GameCraft-Bench subset, P2G consistently beats several agent harnesses with the same underlying model, including GPT-6.1-Sol.
- **Relevance:** A full-stack PCG/game-creation agent; structured project state is the key enabler for reliable agentic game development.

#### AnyGameRenderer: Entity-Consistent Generative Rendering Across Games and an Entity-Level Benchmark
- **Title:** AnyGameRenderer: Entity-Consistent Generative Rendering Across Games and an Entity-Level Benchmark
- **Authors:** Ruicong Liu, Liangyang Ouyang, Fengbo Lan, Zhixiang Wang, Kaipeng Zhang
- **Affiliation:** Alaya Lab; Shanghai Innovation Institute
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.31466](https://arxiv.org/abs/2610.31466)
- **Abstract:** AI coding agents can build small playable games in minutes, but results usually look like programmer art. AnyGameRenderer is a video-to-video generative renderer that turns blockouts into high-quality visuals while keeping layout, camera, and every entity's position and timing intact.
- **Key Innovations:**
  - Generalizes across tower defense, auto-battlers, top-down survivors, turn-based battles, kart racing, and crowd runners.
  - Takes plain video as game-state input — no G-buffers, per-object labels, or low-poly proxies; gray blockouts, colored primitives, semantic maps, and wireframes all work.
  - Preserves entity correspondence: group counts stay correct and entities appear/disappear on the right frame.
  - Implemented by LoRA fine-tuning MiniMax-H3 ref2va (33B reference-video-conditioned generator) on ~10k paired clips from 38 agent-made games, Unreal Engine multi-stream data, and reconstructed real gameplay.
  - Proposes an entity-level benchmark for correspondence.
- **Relevance:** Closes the visual-quality gap in AI-generated games without changing game logic; a PCG post-processing primitive.

---

## 5. Game Benchmarks & Evaluation

#### WMEval: Evaluating Interactive World Models Grounded on Physical Simulations
- **Title:** WMEval: Evaluating Interactive World Models Grounded on Physical Simulations
- **Authors:** Lanxiang Hu, Yixin Huang, Abhilash Shankarampeta, Zilin Dai, Yuyuan Wu, Kun Qian, Junze Liu, Arvind Srinivasan, Mingjia Huo, Will Lin, Kai Zhong, Weiqi Zhang, Tian Wang, Qingjun Cui, Tajana Rosing, Hao Zhang
- **Affiliation:** UC San Diego; Unity
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.33894](https://arxiv.org/abs/2610.33894)
- **Abstract:** Interactive world models matter for robotics, game engines, and digital twins, but existing benchmarks focus on perceptual similarity rather than physical-causal coherence. WMEval evaluates interactive world models against Unity-based physical simulations as a high-fidelity ground-truth oracle.
- **Key Innovations:**
  - Nine diverse scenes; state-based verification instead of purely perceptual assessment.
  - Evaluates action controllability, scene and character consistency, prompt adherence, kinematics, fluid mechanics, physical causality, and lighting.
  - Executes matched action sequences in simulator and world model, enabling perceptual and physical-causal comparison against simulator-derived states.
  - SOTA models show large gaps on dimensions hidden by standard perceptual metrics.
- **Relevance:** A much-needed physically grounded benchmark for game world models; exposes failures that FVD/PSNR-style metrics miss.

**Cross-references:** [Gym-Anything-RT](#gym-anything-rt-scaling-real-time-environments-for-vision-language-agents) provides a real-time *agent* benchmark; [DECE](#a-unified-arena-for-llm-agents-across-diverse-eurogames-dece) provides a multi-game *strategic* benchmark; [AnyGameRenderer](#anygamerenderer-entity-consistent-generative-rendering-across-games-and-an-entity-level-benchmark) contributes an entity-level rendering benchmark.

---

## 6. Industry Game AI & Real-Time Inference

#### WorldPager: Zero-Stall Tiered Memory for Long-Horizon World Models on a Single Consumer GPU
- **Title:** WorldPager: Zero-Stall Tiered Memory for Long-Horizon World Models on a Single Consumer GPU
- **Authors:** Bingnan Liu, Ruini Xue
- **Affiliation:** University of Electronic Science and Technology of China
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.35529](https://arxiv.org/abs/2610.35529)
- **Abstract:** Interactive world models keep the KV cache of past chunks as retrieval memory so revisited places stay consistent. On a single consumer machine (one RTX 4090, 32 GiB host memory, one NVMe SSD), long sessions hit a capacity wall: Matrix-Game 2.0 exhausts host memory after 45 seconds in bf16 and 2.8 minutes in int4; the positional horizon is 4.3 minutes.
- **Key Innovations:**
  - Shows the memory is capacity-bound rather than bandwidth-bound and that its access set is known before compute because camera pose is an input.
  - Analytical model predicts spill points to within one chunk and classifies zero vs. non-zero stalls on held-out configurations.
  - Stores int4 KV in a GPU/DRAM/NVMe hierarchy, prefetches each chunk's memory from extrapolated pose, never waits on a miss, and writes back in the background.
  - To the authors' knowledge, first to place interactive world-model KV memory on an NVMe tier with zero-stall prefetching.
  - With training-free position handling, generates 37.5 minutes continuously with zero stalls and constant host memory at ~9.5 FPS; int4 shows no measurable quality loss on a sealed test set.
- **Relevance:** Makes long-session, consumer-GPU game world models practical — a real-time inference systems contribution rather than a model contribution.

**Industry note:** This window's industrial signal is mostly *infrastructure and content tooling* rather than studio-authored game AI papers: Alibaba's World-in-Context, JD's WorldStream/Tempo-Zero, Alaya Lab's AnyGameRenderer, and Unity's WMEval all target deployable game/world generation. Roblox's production pre-ranking work appeared in the sibling `2026-10-30` arXiv AI Search digest and is not duplicated here.

---

## 7. Related Techniques — Coordination, Exploration, Credit Assignment

#### PACT: Plan-Augmented Coordination via Trace-Graphs for Dynamic Multi-Agent Combinatorial Optimization
- **Title:** PACT: Plan-Augmented Coordination via Trace-Graphs for Dynamic Multi-Agent Combinatorial Optimization
- **Authors:** Xiao Zhou, Alex Schutz, Victor-Alexandru Darvariu, Nick Hawes
- **Affiliation:** Oxford Robotics Institute, University of Oxford
- **Venue:** arXiv preprint (2026-10)
- **arXiv:** [https://arxiv.org/abs/2610.26671](https://arxiv.org/abs/2610.26671)
- **Abstract:** Multi-agent RL for neural combinatorial optimization usually assumes all problem information is known upfront, but real problems are dynamic: information is revealed as agents act (e.g., arriving at an edge only to discover it is untraversable). Existing methods fail to coordinate exploration and exploitation of progressively revealed information.
- **Key Innovations:**
  - Augments the environment graph with auxiliary nodes representing agents' plans, connected to resource nodes to encode future dependencies.
  - Message passing over the augmented graph grounds inter-agent coordination in the environment.
  - Enables proactive rather than reactive conflict resolution.
  - Improves solution quality in dynamic problems and transfers best to larger instances, outperforming centralized oracles with privileged access to instance uncertainty.
- **Relevance:** Plan-aware coordination for dynamic multi-agent environments; directly analogous to route/territory planning in strategy games and cooperative game AI.

#### Cross-cutting related work in this window
- **Effect-marginal credit assignment** ([EMPO](#one-act-many-masks-effect-marginal-policy-optimization-for-long-horizon-agents)) generalizes step-level credit to execution-equivalent actions.
- **Detached multi-horizon value features** ([S2L](#short-to-long-detached-features-for-long-horizon-value-learning)) is a lightweight long-horizon RL recipe.
- **Execution-verified self-play** ([Tempo-Zero](#tempo-zero-recursive-self-play-in-executable-worlds-for-video-reasoning)) replaces model-consensus pseudo-labels with program execution.
- **Program-level co-adaptive self-play** ([Robotic Security](#program-level-adversarial-co-adaptive-self-play-for-robotic-security)) extends self-play from policies to code.

---

## Summary

**Key trends (late October 2026):**

1. **Real-time interaction is the new frontier — and the gap is huge.** Gym-Anything-RT quantifies a 9.0% → 75.0% pass-rate swing between real-time and paused play for a frontier model, and shows code-capable agents can bypass real-time perception entirely. This is the strongest evidence yet that game agents need latency-aware evaluation, not just turn-based benchmarks.
2. **Benchmarks are moving from outcomes to state and process.** WMEval uses Unity as a physical oracle; DECE shows harness choice can matter as much as model choice; AnyGameRenderer adds entity-level correspondence. The field is converging on deterministic, diagnostic, in-engine evaluation.
3. **World models are being factored into logic + rendering.** BoxWorld separates a symbolic Box World Engine from a generative renderer; WorldStream keeps a persistent world record; World-in-Context unifies view/action/camera tokens. The monolithic end-to-end video world model is giving way to controllable hybrids.
4. **Self-play is broadening beyond policy-space.** Tempo-Zero self-plays over executable programs with execution-grounded rewards; program-level co-adaptive self-play evolves attacker/defender code. This is a natural bridge between game RL and agentic software.
5. **LLM game-agent harnesses are a first-class failure surface.** Feedback That Backfires shows naive error transcripts make small models repeat illegal moves; AgentMonopoly shows personas change language more reliably than actions. Harness design and transcript hygiene deserve as much attention as the model.
6. **Consumer-grade real-time inference is becoming feasible.** WorldPager sustains 37.5 minutes of interactive world video at ~9.5 FPS on one RTX 4090 via int4 KV tiering and pose-predicted prefetching.
7. **Theory is catching up to opponent-aware play.** New results delimit when exploiting no-regret learners is computationally hard (general-sum) versus easy (zero-sum), and how payoff noise shapes extractable surplus.

**Open questions:**
- Can real-time game agents be trained (not just evaluated) under evolving-state constraints?
- Do symbolic-engine + neural-renderer hybrids scale to open-world games, or only short minigames?
- How should game benchmarks account for harness-induced variance and cost, not just win rate?
- Will program-level self-play produce sustained robustness, or only local recovery as the robotics study suggests?

*Method: arXiv advanced-search sweeps over `cs.LG`, `cs.AI`, `cs.GT`, `cs.MA`, `cs.CL`, `cs.CV`, `cs.RO` for gameplay/self-play/MARL/world-model/PCG terms; 369 unique candidates screened, filtered against all existing wiki digests; abstracts, author blocks, and comments taken from arXiv `abs`/`html`/PDF. 25 papers retained. Sibling digests already cover 13 additional candidates (e.g., `2610.36306`, `2610.33845`, `2610.37397`, `2610.34791`, `2610.35980`, `2610.26789`).*
