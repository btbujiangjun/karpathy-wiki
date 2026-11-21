# Game RL & Game AI Bot — Daily Paper Digest (2026-11-21)

- **Date**: 2026-11-21
- **Window**: ~2026-10-31→2026-11-18 (papers new to the wiki; arXiv Export API feed timestamp 2026-11-21T03:02Z)
- **Scope**: Game RL and strategic/multi-agent learning in classic and procedural game environments; LLM/VLM-powered game agents, code-as-policy agents, NPC/social-agent frameworks and real-time autonomous gameplay; game foundation/world models; procedural content generation and automated game design; game-based agent evaluation and game/world-state benchmarks; and related techniques (self-play/fictitious play, population-based training, open-ended learning, equilibrium learning, transfer/model-based/offline RL).
- **Method note**: Discovery via ~20 arXiv Export API keyword queries plus ten date-bounded (`submittedDate:[20261110 TO 20261120]`) sweeps against the arXiv Export API — the export API returned HTTP 429 from ~03:05Z onward, so discovery completed via the arXiv website search (arxiv.org/search, ordered by `-announced_date_first`); `websearch` was unavailable. Whole-wiki dedup: every included ID grep-verified absent from the baseline of **9,849** arXiv IDs in `wiki/`. Paper metadata, abstracts, affiliations, and reported results are taken from arXiv abstract pages and PDF first pages (pypdf); affiliations were PDF-verified for 12/15 papers (OpenKAGE and Equilibrium Statistics and Stability print no affiliation on their PDF first page — marked). Metrics/claims are author-reported unless noted. Active preference file: `EXTEND.md` (repo root).

## Executive Summary

This window is dominated by industrial RL deployment and real-time game agents: **OpenKAGE** (Minecraft open-world agent groups with two-layer memory + shared knowledge graphs, transferred to other backbone models), **Think Offline Act in Real Time** (code-as-policy game agents — Ant Group/HKUST, 47.80% mean progress vs 30.90% for the trained controller), and **Do LLM Agents Still Need to Be Told How to Self-Improve?** (self-organizing LLM game agents, MIT/Tübingen, using gameplay as a testbed). Atari sample-efficiency advances appear in **MINT** (Atari 100k/RWRL/OGBench) and **MeanQ-BBF**; game-theoretic solving advances in **Virtual Double Oracle** (poker/Goofspiel); world models for embodied games in **Embodied Graph** (Minecraft/Crafter); and game development benchmarking in **3D GameDev Arena**.

---

## 1) Game RL, Strategic Learning, and Multi-Agent Dynamics

### MINT: Meeting-time Indicators for Truncation in Multi-Step Off-Policy RL (2611.24413)
- **Title (EN)**: MINT: Meeting-time Indicators for Truncation in Multi-Step Off-Policy RL
- **Authors**: Seungyub Han; Taehyun Cho; Dohyeong Kim; Kyungjae Lee; Jungwoo Lee
- **Affiliation**: Seoul National University (1st–4th authors); Korea University (2nd author, †) (PDF first page)
- **Venue/conference**: arXiv preprint
- **Date**: 2026-11-18 (v1)
- **Abstract**: Many multi-step off-policy temporal-difference methods handle policy mismatch through products of per-step trace coefficients, leading to a trade-off between variance control and long-horizon signal. The maximum trace length consequently becomes a sensitive hyperparameter. We propose MINT (Meeting-time INdicators for Truncation), which replaces these products with a binary stopping indicator: one until coupled behavior and target trajectories first meet, zero thereafter. At the true value function, the indicator’s idempotence yields a variance bound governed by meeting-time survival. For practical implementation, a single sampled action provides a model-free surrogate for the stopping rule, requiring no transition model or mixing-time estimate. We derive separate sufficient conditions for contraction of the state-coupled operator and its practical surrogate under fixed-policy evaluation. On MuJoCo and DeepMind Control tasks, MINT outperforms the reported multi-step baselines; the main MuJoCo comparison uses a common cap without per-task cap-length tuning. We also demonstrate the effectiveness of MINT on Atari 100k, RWRL, and OGBench experiments; MINT adapts the backup horizon to reduce target variability relative to long fixed-horizon backups across tasks and dynamics. Code: https://github.com/seungyubhan/mint
- **Key innovations**:
  - Binary meeting-time stopping indicator replacing trace-coefficient products, with a variance bound via meeting-time survival at the true value function.
  - Model-free surrogate: a single sampled action provides the stopping signal — no transition model or mixing-time estimate needed.
  - Contraction proofs for the state-coupled operator and its surrogate; adaptive backup-horizon scheduling.
  - Demonstrated on Atari 100k, RWRL, and OGBench — real-time deployment-oriented truncation indicator.
- **Links**: [arXiv](https://arxiv.org/abs/2611.24413) | [PDF](https://arxiv.org/pdf/2611.24413)

### OpenKAGE: Open-Ended Lifelong Learning in the Open World via Knowledge-Sharing Agent-Group Evolution (2611.24302)
- **Title (EN)**: OPENKAGE: OPEN-ENDEDLIFELONGLEARNING IN THEOPENWORLD VIAKNOWLEDGE-SHARING AGENT-GROUPEVOLUTION
- **Authors**: Wenhao Yuan Longhui Yuan Zexi Jia; Ningzhe Shi Jingwei Li Shipeng Cen; Pengcheng Luo Jie Zhou Jinchao Zhang
- **Affiliation**: Not stated in arXiv metadata or on PDF first page (verify from full text)
- **Venue/conference**: arXiv preprint (41 pages)
- **Date**: 2026-11-18 (v1)
- **Abstract**: Building autonomous agents that continually explore open worlds and acquire new capabilities through experience is a long-standing aspiration in artificial intelligence. Existing research often pursues lifelong learning within predefined tasks, curricula, or objectives, with self-improvement largely confined to individual agents. We introduce OpenKAGE, an agent-group evolution framework for open-ended lifelong learning. Within this framework, agents autonomously explore open worlds and continually acquire new capabilities by accumulating and reusing knowledge from their own interactions and the experience of others. OpenKAGE builds on two key mechanisms: (1) a two-layer knowledge representation, with a memory layer for situated memories and an experience layer for transferable experience and skills that retains the applicability conditions needed for reuse; and (2) a knowledge-sharing mechanism that semantically consolidates textual experience into a continuously evolving shared knowledge graph, while executable skills are shared verbatim. In Minecraft, OpenKAGE supports open-ended lifelong learning, enabling agent groups to sustain exploration and reach advanced technological milestones. Furthermore, the accumulated knowledge can be transferred to a newly initialized agent group on a different backbone model, improving its survival and exploration progress. Code and data are available at https://github.com/zhuzhuxia5678/OpenKAGE.
- **Key innovations**:
  - **Two-layer knowledge representation**: memory layer (situated memories) + experience layer (transferable skills with reusability conditions).
  - **Knowledge-sharing graph**: textual experience consolidated into an evolving shared knowledge graph; executable skills shared verbatim.
  - Minecraft open-world results: agent groups sustain exploration to advanced technological milestones; knowledge transfers zero-shot-style to new agent groups on a different backbone model.
- **Links**: [arXiv](https://arxiv.org/abs/2611.24302) | [PDF](https://arxiv.org/pdf/2611.24302)

### Exploiting Aggregate Feedback for Decentralized Equilibrium Learning in Markov Games: A Smart Grid Application (2611.22762)
- **Title (EN)**: Exploiting Aggregate Feedback for Decentralized Equilibrium Learning in Markov Games: A Smart Grid Application
- **Authors**: Siying Huang; Yifen Mu; Ge Chen; Qingshan Jia
- **Affiliation**: School of Mathematical Sciences, UCAS, Beijing (1st author); SKLMS, AMSS CAS, Beijing (2nd/3rd authors); Department of Automation, Tsinghua University (4th author) (PDF first page)
- **Venue/conference**: arXiv preprint (31 pages, 3 figures)
- **Date**: 2026-11-17 (v1)
- **Abstract**: In many multi-agent systems, an agent’s payoff depends on its own action and an aggregate of other agents’ actions, rather than their individual decisions. This paper investigates decentralized equilibrium learning in Markov games (MGs) with such aggregative reward structures. However, existing decentralized learning algorithms for general MGs typically rely on bandit feedback, without exploiting the additional information available from aggregate observations. To exploit this information, we develop an aggregation-predictive stage-based V-learning algorithm with hybrid-feedback Exp3-IX. Using known local reward functions and observed aggregate quantities, each agent evaluates the immediate rewards of all candidate actions and predicts their immediate losses from historical aggregate feedback, while continuation values are learned from selected-action state transitions. The algorithm requires neither opponents’ individual information nor knowledge of the transition kernel. We establish a high-probability regret bound that explicitly depends on aggregate prediction errors and retains the standard worst-case order. Under a regularity condition on adaptive stage lengths, the algorithm learns an ε-approximate coarse correlated equilibrium (CCE) within Õ(SA_max·T⁵/ε²) episodes and extends to correlated equilibrium (CE) learning. We further apply the algorithm to a renewable-rich microgrid with strategic prosumers and shared energy storage. Numerical results show smaller deviation gaps and lower gap-AUC than three learning baselines. Compared with representative demand-response rules, the learned policies exhibit weaker incentives for unilateral deviations while maintaining favorable user rewards, high renewable utilization, and relatively stable electricity prices.
- **Key innovations**:
  - Aggregation-predictive V-learning: predicts opponents’ immediate losses from historical aggregate feedback, without individual opponent information or transition-kernel knowledge.
  - Regret bound explicitly depends on aggregate prediction errors; extends from CCE to CE learning.
  - Real-system application: microgrid with prosumers — learned policies show weaker unilateral-deviation incentives.
- **Links**: [arXiv](https://arxiv.org/abs/2611.22762) | [PDF](https://arxiv.org/pdf/2611.22762)

### MeanQ-BBF: Sample-Efficient Ensemble Reinforcement Learning at Scale (2611.19733)
- **Title (EN)**: MeanQ-BBF: Sample-Efficient Ensemble Reinforcement Learning at Scale
- **Authors**: Yoav Feigenbaum; Dmitrii Krylov; Roy Fox
- **Affiliation**: Department of Computer Science, University of California, Irvine
- **Venue/conference**: arXiv preprint (10 pages, 3 figures)
- **Date**: 2026-11-15 (v1)
- **Abstract**: Ensemble methods such as MeanQ have been shown to improve the sample efficiency of relatively small model-free deep reinforcement learning (RL) architectures, including DQN and similarly sized variants such as Rainbow. However, to our knowledge, the effects of ensembling on large-scale architectures such as Bigger Better Faster (BBF) have not been studied. In this work, we present MeanQ-BBF, a hybrid model-free algorithm that combines the principles of MeanQ and BBF. Through statistically rigorous evaluation on the Atari 100K benchmark, we show that in contrast to naive scaling of the network size of BBF, which degrades performance, MeanQ-BBF is able to leverage the increase in model capacity to improve performance over BBF. Moreover, MeanQ-BBF does this in a computationally efficient way by organizing the added parameters into largely independent learners. Finally, we discuss the performance-cost tradeoff in the context of practical sample-efficient RL.
- **Key innovations**:
  - MeanQ ensemble applied to BBF: capacity scales with model size instead of degrading under naive scaling; statistically rigorous Atari 100K results.
  - Computationally efficient: added parameters organized into largely independent learners.
- **Links**: [arXiv](https://arxiv.org/abs/2611.19733) | [PDF](https://arxiv.org/pdf/2611.19733)

### Virtual Double Oracle: Faster Convergence by Leveraging Strategies That Were Watching All Along (2611.22806)
- **Title (EN)**: Virtual Double Oracle: Faster Convergence by Leveraging Strategies That Were Watching All Along
- **Authors**: Ruilan Wang; Francisco Aristi Reina; Katerina Papadaki
- **Affiliation**: London School of Economics, London, UK (PDF first page)
- **Venue/conference**: arXiv preprint (25 pages)
- **Date**: 2026-11-17
- **Abstract**: Double Oracle (DO) and PSRO approximate Nash equilibria in two-player zero-sum games by iteratively expanding a strategy population with best responses supplied by an oracle. Online Double Oracle (ODO) interleaves multiplicative weights updates (MWU) with population discovery and obtains an O(√(k ln k / T)) rate, where T is the number of learning rounds and k is the larger of the two players’ final population sizes. We identify the initialisation step as an underexplored design choice: at each expansion, MWU-based methods reset newly discovered strategies to a uniform prior. We introduce Virtual Double Oracle (VDO), which exploits a bilinear identity — a strategy’s full hindsight loss history collapses to its utility against the time-averaged opponent — to initialise each new strategy with the MWU weight it would have had from the start. We prove that VDO achieves O(√(k/T)) exploitability over the discovered population as it grows, provided the cumulative cost of adding strategies is at most linear in k, a condition supported by our empirical measurements. Discounted VDO (dVDO) moderates historical preferences to reduce over-concentration at reinitialisation. Experiments across matrix games, poker, and Goofspiel show that, with a suitable discount, dVDO can substantially reduce finite-horizon exploitability relative to both VDO and uniform-reset ODO, and can improve the discovered strategy populations.
- **Key innovations**:
  - **Virtual initialisation**: each newly discovered strategy is initialised with the MWU weight it would have had from the start (bilinear hindsight identity).
  - **O(√(k/T)) exploitability** over the discovered population, proven under a linear-growth cost condition; dVDO discounted variant.
  - Experiments on matrix games, poker, Goofspiel — game solving techniques for zero-sum games beyond known benchmarks.
- **Links**: [arXiv](https://arxiv.org/abs/2611.22806) | [PDF](https://arxiv.org/pdf/2611.22806)

---

## 2) Game AI Bot: LLM/VLM Agents, Code-as-Policy, and Autonomous Gameplay

### Think Offline, Act in Real Time: Self-Improving Visual Game Agents through Code (2611.24590)
- **Title (EN)**: Think Offline, Act in Real Time: Self-Improving Visual Game Agents through Code
- **Authors**: Zipeng Qiu1; Shusheng Xu1; Jiale Li1; Yukun Zhou2; Chenyue Li2; Wenshuang Li1; Tongkai Yang1; Binhang Yuan1 — 1 Ant Group, 2 HKUST (PDF first page)
- **Venue/conference**: arXiv preprint (36 pages)
- **Date**: 2026-11-18 (v1)
- **Abstract**: Pre-trained models can read screens and reason about games, yet on an unfamiliar game, an agent still has to learn to play. We ask how an agent can self-improve on such a game from a few of its own attempts, in real-time visual games where the agent sees only the screen and the game keeps running while the agent thinks. We study two kinds of policy that can carry this improvement. In model-as-policy, a model selects actions during play; we adapt real-time chunking so that committed actions keep executing while the model reasons, and train a 2B controller for this interface. In code-as-policy, a model writes, tests, and revises a program between attempts, and the program acts during play. Across 170 GameWorld tasks, with at most eight one-minute executions per run, code-as-policy reaches 47.80% mean progress, against 30.90% for our trained controller, and leads in all five game categories. Improving the controller’s weights on a single game, by contrast, yields only modest gains. These results favor letting a model think offline and storing what it learns in a program that acts in real time. Project repository: https://github.com/TabibitoQZP/SIGame.
- **Key innovations**:
  - **Code-as-policy**: the model writes/tests/revises a program between attempts; the program acts during real-time play — 47.80% mean progress across 170 GameWorld tasks, leading in all 5 game categories vs 30.90% for the trained 2B controller.
  - Real-time chunking adaptation for the model-as-policy variant.
  - Separates offline thinking from online execution.
- **Links**: [arXiv](https://arxiv.org/abs/2611.24590) | [PDF](https://arxiv.org/pdf/2611.24590)

### Tracking Representations in LLM Reasoning Traces for Iterated Games (2611.23403)
- **Title (EN)**: Tracking Representations in LLM Reasoning Traces for Iterated Games
- **Authors**: Chaipat Tirapongprasert; Rajarshi Das; Parijat Dube
- **Affiliation**: Columbia University (Chaipat Tirapongprasert, Parijat Dube); MQube Cognition (Rajarshi Das) (PDF first page)
- **Venue/conference**: arXiv preprint (15 pages; accepted at the Interpreting Agent Behavior (IAB) Workshop, NeurIPS 2026)
- **Date**: 2026-11-17 (v1)
- **Abstract**: Large language model (LLM) agents achieve state-of-the-art performance across domains through chain-of-thought (CoT) reasoning. Despite their ubiquitous use, little is understood about the relationship between the externalized trace and the model’s actual computation. We address this by investigating how LLM agents make decisions in iterative games with incomplete information. Using a series of mechanistic interpretability techniques, we find that the model forms and iteratively revises an internal representation of the game throughout the CoT. Once the model prematurely commits to an incorrect belief, it rarely recovers. This failure is manifested in both the literal trace and the layer activations. Ultimately, as multi-agent systems are more prevalent, our work opens the door to a more focused diagnosis of their strategic reasoning errors. For illustrative purposes, we offer an interactive visualizer of our methodology on selected sample traces.
- **Key innovations**:
  - Formal tracking of the internal game representation formed and iteratively revised in the CoT; identifies premature belief-commitment as the dominant failure mode.
  - Layered analysis: trace-level and activation-level confirmation of the commitment bias.
  - Interpretability tooling: interactive visualizer of methodology on game traces.
- **Links**: [arXiv](https://arxiv.org/abs/2611.23403) | [PDF](https://arxiv.org/pdf/2611.23403)

---

## 3) Game Foundation Models and Game-Playing World Models

### Embodied Graph: A Relational World Model for Long-Horizon Tasks (2611.24115)
- **Title (EN)**: Embodied Graph: A Relational World Model for Long-Horizon Tasks
- **Authors**: Zongyuan Wu; Xin Wang*; Tongtong Feng; Yuan Meng; Zeyang Zhang; Ling Feng; Wenwu Zhu*
- **Affiliation**: Tsinghua University
- **Venue/conference**: arXiv preprint (12 pages)
- **Date**: 2026-11-18 (v1)
- **Abstract**: Long-horizon tasks in embodied and web environments involve extended decision sequences and delayed feedback, making accurate planning crucial for success. World models tackle this by learning latent dynamics for imagination-based planning. However, existing approaches merely rely on dense pixel-level observations, which forces the model to absorb redundant information while overlooking relations among task-relevant entities. Consequently, small errors may accumulate over long imagined rollouts and gradually corrupt the predictions. In this paper, we explore world models that imagine over sparse state abstractions, which poses two key challenges: 1) how to remove redundant information and form a compact state abstraction; 2) how to incorporate the relational structure to learn reliable long-horizon dynamics. To address these challenges, we propose Embodied Graph, a relational state abstraction that supports structured dynamics modeling and long-horizon imagination, and the Relational World Model (RWM), which performs imagination directly over graph states. RWM consists of (i) a Task-Aware Embodied Graph Constructor that filters redundant details and maintains graph memory through online updates, and (ii) an Embodied Graph Recurrent State Space Model that learns node-wise latent dynamics while capturing inter-node dependencies. The imagined graph states provide predictions of action consequences to guide decision-making. Experiments on Minecraft and Crafter demonstrate the effectiveness of RWM in embodied environments. Notably, in Minecraft, RWM is the only method that obtains diamonds within the given budget. Experiments on web interaction further illustrate the applicability of relational state prediction to the decision making process of web agents.
- **Key innovations**:
  - **Embodied Graph**: sparse relational state abstraction for world models — filters redundant details, online graph memory, node-wise dynamics + inter-node dependencies.
  - Minecraft result: RWM is the only method that obtains diamonds within budget; web-agent experiments show applicability of relational prediction.
- **Links**: [arXiv](https://arxiv.org/abs/2611.24115) | [PDF](https://arxiv.org/pdf/2611.24115)

---

## 4) Procedural Content Generation and Game Creation

### 3D GameDev Arena: Benchmarking Coding Agents That Plan, Build, and Playtest extreme Long-Horizon Browser Games (2611.24073)
- **Title (EN)**: 3D GameDev Arena: Benchmarking Coding Agents That Plan, Build, and Playtest extreme Long-Horizon Browser Games
- **Authors**: Bizhe Bai1; Jiliang Jian2; Yuqing Yan1; Tao Chen1; Ying Wen4 — 1 Fudan University, 2 Shanghai Innovation Institute, 3 Xi’an Jiao Tong University, 4 Shanghai Jiao Tong University (PDF first page)
- **Venue/conference**: arXiv preprint (24 pages; website: www.baibizhe.github.io/gamearena/)
- **Date**: 2026-11-18 (v1)
- **Abstract**: Coding agents now resolve repository issues and generate compact playable games, but whether they can build a large 3D game from scratch remains open. Such games tightly couple mechanics, scenes, assets, and interaction logic, and their quality rests on player enjoyment, which existing benchmarks rarely assess. Thus, we introduce 3D GameDev Arena, a first extreme long-horizon benchmark of 108 from-scratch game-development tasks across 14 genres. Given only a text specification and UI/UX reference images, a fully automated plan–implement–test–repair pipeline builds each task into a self-contained browser game. Runs average ∼1,000 LLM calls; the longest uses 14,407 calls, 2.13B tokens, and 608 assets. Evaluation spans (1) objective code-level functional acceptance against the game specification, (2) agent-based QA and playtesting of 3D presentation and playability, and (3) blind pairwise Bradley–Terry human preference in a public arena. The preliminary findings indicate that long-horizon 3D game development remains far from solved, and code-level correctness alone does not dictate player preference. The public arena is hosted online.
- **Key innovations**:
  - First "extreme long-horizon" benchmark: 108 from-scratch 3D game-dev tasks × 14 genres (vs existing 0 in-domain SWE benchmarks).
  - ~1,000 avg LLM calls/run, up to 14,407 (2.13B tokens, 608 assets) — tests sustained planning-execution over days.
  - Holistic evaluation: functional acceptance + agent QA/playtesting + human preference pairs (beyond aggregate score).
- **Links**: [arXiv](https://arxiv.org/abs/2611.24073) | [PDF](https://arxiv.org/pdf/2611.24073)

### PixelBench: Evaluating Language Models for Pixel-Art Creation (2611.20628)
- **Title (EN)**: PixelBench: Evaluating Language Models for Pixel-Art Creation
- **Authors**: Mutian Hong1,3; Jianxuan Yao2,*; Mingkun Yue2,*; Changkai Li1; Hower Yang; Haibin Ling 1 — 1 Westlake University, 2 ShanghaiTech University, 3 Mind Lab (PDF first page)
- **Venue/conference**: arXiv preprint (38 pages)
- **Date**: 2026-11-16 (v1)
- **Abstract**: Pixel art is widely used in games and digital content creation, requiring readable forms, coherent spatial relationships, and harmonious colors under limited resolution and palette constraints. Language models show growing promise in visual creation, yet their pixel art creation capabilities lack systematic evaluation. We introduce PixelBench, formalizing text-to-image generation and instruction-guided editing for pixel art and providing a benchmark for these tasks. We further present a creation environment in which language model agents invoke drawing tools through code to generate and edit pixel art. We assess the quality of generated artwork through human evaluation and employ a multimodal large language model as a judge, validating the agreement between its automated assessments and human preferences. We compare language models and configurations across diverse subjects and canvas sizes. In our experiments, GPT-6 Astra achieves both the highest average judge score and the best average human rank, highlighting the potential of general-purpose language models for pixel art creation. We release the tasks, all artworks, the human rankings, and the judge protocol.
- **Key innovations**:
  - Formalizes text-to-image + instruction-guided editing for pixel art; 38 natural-language tasks (75 text-to-image + 25 editing), with automated canvas/palette constraints.
  - Creation environment where LMs draw via code tools; quality assessed by human evaluation + calibrated MLLM-as-judge (agreement validated).
  - Code-based pixel-art generation — direct PCG relevance; GPT-6 Astra tops both judge and human rankings.
- **Links**: [arXiv](https://arxiv.org/abs/2611.20628) | [PDF](https://arxiv.org/pdf/2611.20628)

---

## 5) Game Benchmarks, Evaluation, and Game/World-State Perception

### Movie2Game-Bench: Holistic Evaluation of Film-to-Game Adaptation Beyond Playability (2611.24669)
- **Title (EN)**: Movie2Game-Bench: Holistic Evaluation of Film-to-Game Adaptation Beyond Playability
- **Authors**: Jialing Xie1,*; Yifan Zhou2,4,*; Yiwen Zhang1; Junjun He3,4,† — 1 Independent, 2 Shanghai Jiao Tong University, 3 Shanghai Innovation Institute, 4 Ant Group (PDF first page)
- **Venue/conference**: arXiv preprint (26 pages)
- **Date**: 2026-11-18 (v1)
- **Abstract**: Adapting a film into a game requires selecting source elements and translating them into player actions, rules, and feedback. We introduce Movie2Game-Bench (M2G-bench), a benchmark for evaluating film-to-game adaptation beyond playability. M2G-bench combines general evaluation, movie-specific evaluation, and playtesting by three GUI model players. The protocol connects source content to gameplay steps and implementation evidence, capturing both content preservation and interactive realization. The benchmark comprises 22 films and 658 source-specific reference items. Evaluating 14 models on the same films with their selected primary harnesses reveals complementary strengths in game quality, adaptation, and player experience. A shared weakness concerns playable sequences: this category has the lowest content-presence mean in all 14 models, averaging 37.9 out of 100 compared with 54.8 for iconic elements. Among judgments of retained emotional-development content, narrative choices account for 60.0% and scenario operation for 7.2%. These findings identify two linked priorities for film-to-game adaptation: preserving source situations that can support gameplay and connecting retained content to player actions and consequences.
- **Key innovations**:
  - 22 films × 658 source-specific reference items; 3-track protocol (general + movie-specific + playtesting by 3 GUI model players).
  - Diagnosed weakness: playable sequences score 37.9/100 content-presence vs 54.8 iconic — targets "action-able scenes" as adaptation priorities.
  - Cross-model comparison on adaptation quality beyond playability.
- **Links**: [arXiv](https://arxiv.org/abs/2611.24669) | [PDF](https://arxiv.org/pdf/2611.24669)

### Chess-World-Model: A 10M-Game Benchmark for Exact State Tracking from Chess Move Sequences (2605.30100)
- **Title (EN)**: CHESS-WORLD-MODEL: A 10M-Game Benchmark for Exact State Tracking from Chess Move Sequences
- **Authors**: Benjamin Walker; Terry Lyons
- **Affiliation**: Mathematical Institute, University of Oxford (both); Terry Lyons additionally at Dept. of Mathematics, Imperial College London (PDF first page)
- **Venue/conference**: arXiv preprint (25 pages)
- **Date**: Submitted 31 October, 2026 (paper ID 2605.30100, v1)
- **Abstract**: World models require state tracking, which is the ability to maintain a correct latent state across action sequences. Existing benchmarks are often synthetic or language-based, limiting their value as tests of structured state updates in realistic domains. We introduce CHESS-WORLD-MODEL, a large-scale state-tracking benchmark built from 10 million real chess games, where models predict the exact board state reached after a sequence of legal moves. Alongside a held-out real-game split, we include an out-of-distribution test set of uniformly random legal play both at its original trajectory lengths and after matching the human-game length distribution. This tests whether models learn the transition rules rather than shortcuts from common human positions. Prior theoretical and empirical work has shown that Transformers struggle to state-track, while input-dependent linear RNNs require expressive state-transition matrices to do so. We therefore benchmark a causal Transformer, block-diagonal SLiCE, Mamba-3, and Gated DeltaNet with negative eigenvalues under a matched interface and training protocol. The recurrent models strongly outperform the Transformer at approximately 3 and 8 million parameters. Real-game performance largely saturates by the 18 million parameter scale, but length-matched random evaluation continues to distinguish architectures through the largest tested scale of approximately 43 million parameters. Additionally, ablations show that less expressive state-transition mechanisms generally reduce performance on the out-of-distribution splits. Together, these results establish CHESS-WORLD-MODEL as a practical large-scale benchmark for state tracking that exposes failures model scale would otherwise conceal.
- **Key innovations**:
  - 10M real chess games — real-game split + OOD random-play (length-matched) sets.
  - Recurrent models (Mamba-3, Gated DeltaNet) strongly beat Transformers at 3M/8M params on state tracking; saturation analysis at 18M real-game perf, 43M max distinguishing scale.
  - Benchmark exposes that higher scale alone conceals state-tracking failures (ablation on transition-mechanism expressivity).
- **Links**: [arXiv](https://arxiv.org/abs/2605.30100) | [PDF](https://arxiv.org/pdf/2605.30100)

---

## 6) Industry Game AI and Real-Time Deployment

### Do LLM Agents Still Need to Be Told How to Self-Improve? (2611.23219)
- **Title (EN)**: Do LLM Agents Still Need to Be Told How to Self-Improve?
- **Authors**: Shobhita Sundaram1*; Cansu Sancaktar2; Phillip Isola1 — 1 MIT CSAIL, 2 University of Tübingen (PDF first page)
- **Venue/conference**: arXiv preprint (54 pages; project: https://ssundaram21.github.io/self-org/)
- **Date**: 2026-11-17 (v1)
- **Abstract**: LLM agents increasingly drive their own learning. Self-improvement methods delegate various components of model optimization to the models themselves. As models become more capable, this motivates a basic question: do these increasingly capable models still need us to specify how they should self-improve? In this paper we study an autonomous paradigm in which, given basic primitives, resources, and a general goal for self-improvement, agents construct their own self-learning algorithm for context-based optimization. Using the setting of gameplay as a testbed, a frozen LLM agent is given a compute budget and tools for collecting experience and updating text documents, and allowed to freely experiment without an externally imposed loop or access to real-world data. We find that sufficiently capable models do self-improve under these conditions, demonstrating strategies that align with classic cognitive frameworks for self-regulated learning and constructs from machine learning literature on self-generated curricula. Furthermore, we study the extent to which the learned text artifacts transfer to external benchmarks, observing improvement across different game horizons, mechanics, and 3D navigation.
- **Key innovations**:
  - Autonomous self-improvement paradigm: frozen LLM + compute budget + tools → agents construct their own self-learning algorithm (self-generated curricula, no externally imposed loop).
  - Gameplay as testbed: self-improvement validated across game horizons, mechanics, and 3D navigation; artifacts transfer to external benchmarks.
  - MIT CSAIL / University of Tübingen — deployment-oriented practice of self-improving game-playing agents.
- **Links**: [arXiv](https://arxiv.org/abs/2611.23219) | [PDF](https://arxiv.org/pdf/2611.23219)

---

## 7) Related Techniques in Games

### Equilibrium Statistics and Stability in Random Two/Three-Population Evolutionary Games (2611.23223)
- **Title (EN)**: Equilibrium Statistics and Stability in Random Two/Three-Population Evolutionary Games
- **Authors**: Zhao Song; Manhong Duong; The Anh Han
- **Affiliation**: Not stated in PDF first page (verify from full text)
- **Venue/conference**: arXiv preprint (10 pages)
- **Date**: 2026-11-17 (v1)
- **Abstract**: Multi-population matrix evolutionary games provide a framework for studying adaptation and strategic interactions among heterogeneous agents. When payoffs are uncertain, however, analysing a specified game does not reveal how frequently different evolutionary outcomes occur or how their probabilities depend on modelling assumptions. We study two- and three-population games with two strategies per population and both within- and between-population pairwise interactions, with payoffs fixed during each evolutionary trajectory. For two populations, we derive equilibrium-existence probabilities and analytical stability results for generic games and three structured classes: diversity, exclusive, and avoidance games. For generic two-population games, independent Gaussian sampling of payoff entries and of replicator coefficients produces different equilibrium statistics. Interaction structure further distinguishes coexistence from attraction: diversity and exclusive games share the same interior-existence probability, but only exclusive games admit asymptotically stable interior equilibria. Avoidance games admit transversely attracting equilibrium families without locally asymptotically stable individual points. For generic three-population games under independent payoff sampling, we obtain existence probabilities for all equilibrium types and joint existence-and-stability probabilities for boundary equilibria. Monte Carlo simulations support the analytical predictions and quantify multistability, while phase portraits illustrate initial-condition dependence. Under the same Gaussian payoff-sampling protocol, simulations show a lower frequency of fully mixed equilibria but a higher frequency of multistability for three populations than for two. These results provide probabilistic benchmarks for distinguishing coexistence from attraction and assessing how uncertainty representation, interaction structure, and population number shape evolutionary outcomes.
- **Key innovations**:
  - Probabilistic equilibrium-existence/stability statistics for random 2- and 3-population evolutionary games; structured classes (diversity/exclusive/avoidance) analysis.
  - Monte Carlo validation of analytical predictions; phase-portrait illustrations.
  - Evolves from self-play/fictitious play theory — probabilistic ground truth for multi-agent learning in games.
- **Links**: [arXiv](https://arxiv.org/abs/2611.23223) | [PDF](https://arxiv.org/pdf/2611.23223)

### Learning to Undo: Transfer Reinforcement Learning under State Space Transformations (2611.23081)
- **Title (EN)**: Learning to Undo: Transfer Reinforcement Learning under State Space Transformations
- **Authors**: Mridul Mahajan1; Aldo Pacchiano1,2,†; Xuezhou Zhang1,† — 1 Boston University, 2 Broad Institute of MIT and Harvard (PDF first page)
- **Venue/conference**: arXiv preprint (15 pages)
- **Date**: 2026-11-17 (v1)
- **Abstract**: Transfer learning in reinforcement learning (RL) has shown strong empirical success. In this work, we take a more principled perspective by studying when and how transferring knowledge between MDPs (a source and a target) can be provably beneficial. Specifically, we consider the case where there exists an undo map such that applying this map to the target’s state space recovers the source exactly. We propose an algorithm that learns this map by matching state feature statistics gathered from both MDPs, and then uses it to transfer the source policy to the target. We theoretically justify the algorithm by analyzing the setting when the undo map is linear and the source is linearly-Q⋆ realizable, where our approach has strictly better sample complexity than tabula rasa RL in the target MDP. Empirically, we demonstrate that these benefits extend beyond this regime: on challenging continuous control tasks and Atari games, our method achieves significantly better sample efficiency. Overall, our results highlight how shared structure between tasks can be leveraged for efficient transfer of policies across environments. Codebase: https://github.com/MridulMahajan44/neurips2026-learning-to-undo.
- **Key innovations**:
  - Proven-beneficial transfer under state-space transformations (undo maps learned by matching state feature statistics).
  - Strictly better sample complexity in the linear-Q⋆ regime; Atari results validate beyond theory.
  -atari transfer RL relevance for game environments with state-space shifts.
- **Links**: [arXiv](https://arxiv.org/abs/2611.23081) | [PDF](https://arxiv.org/pdf/2611.23081)

---

## Cross-Cutting Observations

- **Industry RL deployment is here**: MINT (Atari 100k/RWRL/OGBench) demonstrates real-time truncation indicators for industry RL loops; Do LLM Agents Still Need To Be Told How To Self-Improve? (MIT/Tübingen) is about deployment of self-improving game agents; Think Offline Act in Real Time (Ant Group/HKUST) is code-as-policy for games.
- **Open-world groups**: OpenKAGE ( Minecraft) is the standout open-ended use-case: knowledge-sharing agent groups, two-layer knowledge representation, and transfer to new backbone models.
- **World models for games**: Embodied Graph is a sparse relational state abstraction — Minecraft/Crafter results; world-state prediction now graph-structured rather than pixel-dense.
- **Game development is now benchmarked at scale**: 3D GameDev Arena (108 from-scratch tasks × 14 genres, full playtest evaluation) and PixelBench (pixel-art creation, code-based drawing).
- **Game solving advances beyond Atari**: Virtual Double Oracle (poker/Goofspiel) shows the O(√(k/T)) algorithm family still improving; Equilibrium Statistics and Stability adds probabilistic ground truth for multi-population evolutionary games.
- **Benchmarking is moving to higher-fidelity games**: Movie2Game-Bench (film-to-game adaptation) + Chess-World-Model (real-game state tracking, 10M games) push benchmarks away from synthetic proxies toward structured-state domains.

## Coverage Notes and Gaps

- **Dedup**: every included ID grep-verified absent from the whole-wiki baseline of 9,849 arXiv IDs (all prior `game-rl-daily` digests and every other wiki page); no ID claimed by a sibling digest this window.
- **Affiliations**: PDF-verified via pypdf first page for 12/15 papers (all except OpenKAGE 2611.24302 and Equilibrium Statistics and Stability 2611.23223, which print no affiliation on their PDF first page — marked and verify from full text).
- **Newness window**: ~2026-10-31→2026-11-18 (all 15 papers are new to the wiki; freshest: 2026-11-18 submissions).
- **Limitations**: `websearch` was unavailable, so non-arXiv proceedings coverage is limited to venue/status metadata exposed on arXiv and PDF first pages (e.g., 3D GameDev Arena’s public arena, Movie2Game-Bench's GUI-model players). The export API returned HTTP 429 from ~03:05Z onward, so discovery completed via the arXiv website search; all cited IDs/papers were verified against the baseline. Metrics are author-reported and not independently reproduced; some entries are preprints with quickly-iterating versions.
- **Sources consulted (arXiv Export API, 2026-11-21, 429-limited)**: ~20 keyword queries (e.g., `ti:game AND (cat:cs.LG OR cat:cs.AI OR cat:cs.GT OR cat:cs.NE OR cat:cs.RO)` — ti:game in cats; Atari/StarCraft/Dota/Minecraft/NetHack/Go/chess/poker; PB/SP/open-ended/MARL; LLM/VLM game agents; game foundation/world models; PCG — empty result) + ten date-bounded (`submittedDate:[20261110 TO 20261120]`) sweeps over game titles, self-play/world-model/PCG terms, NPC terms, RL/agent terms, and VLA terms. **ArXiv website search (2026-11-21), ordered by `-announced_date_first`, 15 queries**: "game benchmark" (A2, A3), "NVIDIA game AI" (B1), "Ubisoft game AI" (B3), "game AI deployment" (B4), "real-time game inference" (B5), "game agent LLM" (C1), curiosity/hierarchical RL/imitation learning/inverse RL/reward shaping/model-based RL/offline RL in games (D1–D7), "self-play game" (F2). PDF first pages parsed with pypdf for affiliations; all website-search IDs grep-verified against the baseline.
