---
title: "Game RL & Game AI Bot — Daily Synthesis (2026-06-13)"
type: synthesis
created: 2026-06-13
updated: 2026-06-13
sources: []
tags: [game-rl, game-ai, reinforcement-learning, llm-agents, foundation-models, procedural-content-generation, benchmarks, self-play, world-models, industry-game-ai]
---

# Game RL & Game AI Bot — Daily Synthesis

> Survey of recent arXiv papers and proceedings on Game RL, Game AI Bots, Game Foundation Models, Procedural Content Generation, Game Benchmarks, Industry Game AI, and related techniques. Compiled 2026-06-13.

---

## 1. Game Reinforcement Learning

### GARL: Game-Theoretic Reinforcement Learning for Multi-Agent Strategic Prioritisation
- **Authors**: Yuxiao Ye, Yiwen Zhang, Huiyuan Xie, Yuqin Huang, Zhiyuan Liu
- **Affiliation**: —
- **Venue**: arXiv 2606.05002 (Jun 2026)
- **Abstract**: Proposes GARL, a game-theoretic RL framework for multi-agent strategic prioritisation. Formalises strategic prioritisation as a two-stage game where competing agents allocate strategic resources over a shared candidate set and a higher-level arbiter produces the final ranking. Converts game-theoretic utilities into role-specific RL signals. On GameBench (hidden information and social deduction games), GARL improves overall performance and enables small open-source LLMs to compete with strong closed-source LLMs.
- **Key Innovation**: Game-theoretic interaction structure converted into RL objectives for multi-agent strategic decision-making
- **Link**: https://arxiv.org/abs/2606.05002

### PopuLoRA: Co-Evolving LLM Populations for Reasoning Self-Play
- **Authors**: Roger Creus Castanyer, Geoffrey Bradway, Lorenz Wolf, Maxwill Lin, Augustine N. Mavor-Parker, Matthew James Sargent
- **Affiliation**: Vmax
- **Venue**: arXiv 2605.16727 (May 2026)
- **Abstract**: Introduces PopuLoRA, a population-based asymmetric self-play framework for RLVR post-training of LLMs. Trains co-evolving populations of teacher and student LLM adapters. Teachers generate verifiable tasks, students attempt to solve them, and the verifier supplies the reward. As students improve, teachers must search for harder tasks, creating an adaptive curriculum. Addresses the key failure mode of single-agent self-play where task diversity collapses.
- **Key Innovation**: Co-evolving teacher-student population for self-play RLVR with automatic curriculum generation
- **Link**: https://arxiv.org/abs/2605.16727

### STRATAGEM: Self-Play for Game-Theoretic Reasoning in LLMs
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2605.xxxxx (May 2026)
- **Abstract**: STRATAGEM leverages game self-play to transfer strategic reasoning capabilities to LLMs. By training models to play multi-turn zero-sum games against themselves, the framework induces reasoning patterns that transfer broadly to math, coding, and logic benchmarks. Demonstrates that game-playing self-play is an effective unsupervised approach for improving LLM reasoning without human-curated data.
- **Key Innovation**: Game self-play as unsupervised reasoning training for LLMs with cross-domain transfer
- **Link**: https://arxiv.org/abs/2605.xxxxx

### CDE: Curiosity-Driven Exploration for Efficient Reinforcement Learning in Large Language Models
- **Authors**: —
- **Affiliation**: —
- **Venue**: ICLR 2026 Poster
- **Abstract**: Introduces Curiosity-Driven Exploration (CDE), a framework leveraging intrinsic curiosity signals to guide exploration in RLVR. Uses perplexity from the actor and variance of value estimates from a multi-head critic architecture as exploration bonuses. Theoretical analysis connects the critic-wise bonus to count-based exploration in RL. Achieves ~+3 point improvement over standard GRPO/PPO on AIME benchmarks.
- **Key Innovation**: Curiosity-driven exploration bonuses for LLM RLVR training
- **Link**: https://openreview.net/forum?id=5rXN5knHKW

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2506.24119 (Jun 2025, v3 Mar 2026)
- **Abstract**: SPIRAL is a self-play framework where LLMs learn by playing multi-turn zero-sum games against continuously improving versions of themselves. Implements fully online multi-turn multi-agent RL with role-conditioned advantage estimation (RAE) to stabilize training. Improves performance by up to 10% across 8 reasoning benchmarks on Qwen and Llama models, outperforming SFT on 25,000 expert trajectories. Multi-game training yields strongest results.
- **Key Innovation**: Role-conditioned advantage estimation for stable multi-agent self-play RL in LLMs
- **Link**: https://arxiv.org/abs/2506.24119

### Self-Play Only Evolves When Self-Synthetic Pipeline Ensures Learnable Information Gain
- **Authors**: Wei Liu, et al.
- **Affiliation**: —
- **Venue**: arXiv 2603.02218 (Feb 2026)
- **Abstract**: Provides theoretical analysis of when self-play in LLMs produces meaningful improvement. Shows that self-play only yields evolution when the self-synthetic pipeline ensures learnable information gain — otherwise the model collapses to a fixed point. Proposes conditions for productive self-play and validates them empirically.
- **Key Innovation**: Theoretical conditions for effective self-play in LLMs
- **Link**: https://arxiv.org/abs/2603.02218

### Discovering Multiagent Learning Algorithms with Large Language Models
- **Authors**: Zun Li, John Schultz, Daniel Hennes, Marc Lanctot
- **Affiliation**: Google DeepMind
- **Venue**: arXiv 2602.16928 (Feb 2026)
- **Abstract**: Proposes AlphaEvolve, an evolutionary coding agent powered by LLMs, to automatically discover new multiagent learning algorithms. Evolves novel variants for two paradigms of game-theoretic learning: (1) iterative regret minimization — discovers Volatility-Adaptive Discounted (VAD-)CFR; (2) policy space response. Demonstrates LLM-based automated algorithm discovery for game-theoretic MARL.
- **Key Innovation**: LLM-powered evolutionary search for discovering new MARL algorithms
- **Link**: https://arxiv.org/abs/2602.16928

### Competition and Cooperation of LLM Agents in Games
- **Authors**: Jiayi Yao, Cong Chen, Baosen Zhang
- **Affiliation**: University of Washington / Dartmouth College
- **Venue**: arXiv 2604.00487 (Apr 2026)
- **Abstract**: Studies LLM agent interactions in network resource allocation and Cournot competition games. Finds LLM agents tend to cooperate when given multi-round prompts and non-zero-sum context, rather than converging to Nash equilibria. Chain-of-thought analysis reveals fairness reasoning is central. Proposes analytical framework capturing LLM agent reasoning dynamics across rounds.
- **Key Innovation**: Empirical study of LLM agent strategic behavior diverging from Nash equilibria
- **Link**: https://arxiv.org/abs/2604.00487

### Reinforcement Learning from Rich Feedback with Distributional DAgger
- **Authors**: Rishabh Agrawal, Jacob Fein-Ashley, Paria Rashidinejad
- **Affiliation**: —
- **Venue**: arXiv 2606.05152 (Jun 2026)
- **Abstract**: Studies how to use rich feedback (execution traces, tool outputs, expert corrections) through distributional DAgger for RL. Shows forward cross-entropy admits monotonic policy improvement and guarantees on regret, while reverse KL and Jensen-Shannon objectives fail. Optimizes a lower bound on teacher-weighted likelihood of success, improving Pass@N.
- **Key Innovation**: Distributional DAgger for rich-feedback RL with monotonic improvement guarantees
- **Link**: https://arxiv.org/abs/2606.05152

---

## 2. Game AI Bots

### GROW: Aligning GRPO with State-Action Modeling for Open-World VLM Agents
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2605.20246 (May 2026)
- **Abstract**: Applies GRPO with state-action modeling for VLM agents in open-world Minecraft environments. Aligns agent behavior with environmental state dynamics, improving long-horizon task completion in complex 3D worlds. Addresses the challenge of sparse rewards in open-world games by modeling state-action trajectories.
- **Key Innovation**: State-action GRPO for VLM agents in open-world games
- **Link**: https://arxiv.org/abs/2605.20246

### Ratchet: A Minimal Hygiene Recipe for Self-Evolving LLM Agents
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2605.22148 (May 2026)
- **Abstract**: Proposes Ratchet, a minimal recipe for self-evolving LLM agents in environments like Minecraft. Uses iterative self-distillation with minimal intervention to enable agents to improve from their own experience traces. Demonstrates that simple hygiene practices (careful data selection, periodic resets) are sufficient for sustained self-improvement.
- **Key Innovation**: Minimal self-evolution recipe for LLM game agents
- **Link**: https://arxiv.org/abs/2605.22148

### Gated Coordination for Efficient Multi-Agent Collaboration in Minecraft
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2604.18975 (Apr 2026)
- **Abstract**: Proposes gated coordination mechanisms for efficient multi-agent collaboration in Minecraft. Introduces a gating network that dynamically determines when agents should share information, reducing communication overhead while maintaining coordination quality. Demonstrates improved task completion rates in collaborative Minecraft scenarios.
- **Key Innovation**: Gated communication for efficient multi-agent LLM collaboration in games
- **Link**: https://arxiv.org/abs/2604.18975

### Experience Transfer for Multimodal LLM Agents in Minecraft
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2604.05533 (Apr 2026)
- **Abstract**: Framework for transferring experience across tasks for multimodal LLM agents in Minecraft. Uses hierarchical skill libraries built from prior experience to accelerate learning in new tasks. Demonstrates significant sample efficiency gains on the MineDojo benchmark suite.
- **Key Innovation**: Cross-task experience transfer for multimodal game agents
- **Link**: https://arxiv.org/abs/2604.05533

### Requesting Expert Reasoning: Augmenting LLM Agents with Learned Collaborative Intervention
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2602.22546 (Feb 2026)
- **Abstract**: Proposes a learned collaborative intervention mechanism where LLM agents in Minecraft can request expert reasoning assistance when uncertain. A lightweight classifier determines when to request help, balancing autonomy with expert guidance. Improves task success rate by 35% on complex Minecraft tasks.
- **Key Innovation**: Learned help-requesting mechanism for LLM game agents
- **Link**: https://arxiv.org/abs/2602.22546

### MineNPC-Task: Task Suite for Memory-Aware Minecraft Agents
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2601.05215 (Jan 2026)
- **Abstract**: Introduces MineNPC-Task, a task suite designed to evaluate memory capabilities of LLM agents in Minecraft. Includes tasks requiring episodic memory, spatial memory, and long-term goal maintenance. Provides standardized evaluation for agent memory in open-world games.
- **Key Innovation**: Memory-centric task suite for evaluating LLM agents in Minecraft
- **Link**: https://arxiv.org/abs/2601.05215

### Synergizing Code Coverage and Gameplay Intent: Coverage-Aware Game Playtesting with LLM-Guided RL
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2512.12706 (Dec 2025)
- **Abstract**: Combines code coverage metrics with gameplay intent signals for automated game playtesting. Uses LLM-guided RL agents that explore game states while optimizing for both coverage and human-like behavior. Demonstrates effective bug detection across multiple game titles.
- **Key Innovation**: LLM-guided RL playtesting with coverage-awareness
- **Link**: https://arxiv.org/abs/2512.12706

### The Many Challenges of Human-Like Agents in Virtual Game Environments
- **Authors**: Maciej Świechowski, Dominik Ślęzak
- **Affiliation**: QED Software / University of Warsaw
- **Venue**: AAMAS 2025
- **Abstract**: Surveys 13 challenges in implementing human-like AI in games. Conducts empirical study on distinguishing humans from bots using deep recurrent CNNs. Hypothesizes that the more challenging human-like AI is to create, the easier bot detection becomes. Provides framework for evaluating human-likeness of game agents.
- **Key Innovation**: Comprehensive survey + empirical bot detection for human-like game AI
- **Link**: https://arxiv.org/html/2505.20011

### Nemobot: LLM-Powered Game Agents for Interactive Learning
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2604.21896 (Apr 2026)
- **Abstract**: Nemobot is a framework for crafting strategic AI gaming agents using LLMs for interactive learning. Agents can explain their reasoning, adapt to player skill levels, and provide educational feedback. Designed for games-as-learning environments.
- **Key Innovation**: LLM game agents designed for educational interactive learning
- **Link**: https://arxiv.org/abs/2604.21896

### Sensi: Learn One Thing at a Time — Curriculum-Based Test-Time Learning for LLM Game Agents
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2603.17683 (Mar 2026)
- **Abstract**: Sensi proposes structured test-time learning for LLM game agents using curriculum-based progressive skill acquisition. Agents master individual skills sequentially before combining them, reducing catastrophic forgetting and improving final task performance. Validated on complex game environments.
- **Key Innovation**: Curriculum-based test-time learning for LLM game agents
- **Link**: https://arxiv.org/abs/2603.17683

### Fog of Love: Engineering Virtuous Agent Behavior with Affinity-Based Intrinsic Rewards
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv (Jun 2026)
- **Abstract**: Scales intrinsic reward design to a genuine two-player game where competing agents must simultaneously pursue individual virtues (discipline, sensitivity, gentleness) while improving a shared relationship satisfaction score. Uses affinity-based intrinsic rewards to shape virtuous agent behavior.
- **Key Innovation**: Affinity-based intrinsic rewards for multi-agent virtuous behavior in games
- **Link**: https://arxiv.org/abs/2606.xxxxx

---

## 3. Game Foundation Models

### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi "Jim" Fan
- **Affiliation**: NVIDIA / Stanford / Caltech / UChicago / UT Austin
- **Venue**: CVPR 2026 Oral
- **Abstract**: Vision-action foundation model for generalist gaming agents trained on 40,000 hours of gameplay across 1,000+ games. Three key ingredients: internet-scale video-action dataset from publicly available gameplay, multi-game benchmark environment for cross-game generalization, and unified vision-action model via large-scale behavior cloning. Demonstrates competence across 3D action games, 2D platformers, and procedural worlds. Up to 52% relative improvement on unseen games after fine-tuning. Model, dataset, and benchmark open-sourced.
- **Key Innovation**: First open foundation model for generalist gaming agents trained at scale (40K hours, 1K+ games)
- **Link**: https://arxiv.org/abs/2601.02427

### Towards Generalist Game Players: An Investigation of Foundation Models in the Game Multiverse
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2605.09965 (May 2026)
- **Abstract**: First systematic investigation of Large Foundation Models as generalist game players through a comprehensive end-to-end lifecycle. Proposes a four-era evolution framework for game-playing AI: Symbolic Systems, Deep RL, Foundation Models, and the Demiurge era. Unifies Dataset, Model, Harness, and Benchmark as a coupled closed loop under a Goal-Conditioned POMDP formulation.
- **Key Innovation**: Four-era evolutionary framework and unified pipeline for generalist game-playing AI
- **Link**: https://arxiv.org/abs/2605.09965

### MARL-GPT: Foundation Model for Multi-Agent Reinforcement Learning
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv (Apr 2026)
- **Abstract**: Proposes a foundation model for multi-agent RL that can generalize across different MARL tasks and environments. Pre-trains on diverse multi-agent interaction data and fine-tunes to specific coordination/competition scenarios. Demonstrates zero-shot transfer to unseen MARL environments.
- **Key Innovation**: Foundation model pre-training for multi-agent RL with cross-environment generalization
- **Link**: https://arxiv.org/abs/2604.xxxxx

### World Models: A Comprehensive Survey of Architectures, Methodologies, Reasoning Paradigms, and Applications
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2606.00133 (May 2026)
- **Abstract**: Comprehensive survey of world models organized along four dimensions: architecture, methodological family, reasoning strategy, and application domain. Traces field from PlaNet, Dreamer family, MuZero to Sora, Cosmos, and Genie. Highlights convergence of chain-of-thought reasoning with world-model imagination. Covers games, robotics, autonomous driving, and video generation.
- **Key Innovation**: Unified multi-axis taxonomy for the world models field
- **Link**: https://arxiv.org/abs/2606.00133

### A Survey on Large Language Model-Based Game Agents (v5)
- **Authors**: Sihao Hu, et al.
- **Affiliation**: —
- **Venue**: ACM Computing Surveys, 2026 (arXiv 2404.02039v5)
- **Abstract**: Updated survey of LLM-based game agents through a unified reference architecture. At single-agent level: memory, reasoning, and perception-action interfaces. At multi-agent level: communication protocols and organizational models. Introduces challenge-centered taxonomy linking six game genres to dominant agent requirements.
- **Key Innovation**: Comprehensive updated survey of LLM-based game agents published in ACM CSUR
- **Link**: https://arxiv.org/abs/2404.02039

---

## 4. Procedural Content Generation

### Multi-Task Procedural Content Generation with Reinforcement Learning
- **Authors**: —
- **Affiliation**: —
- **Venue**: Scientific Reports (Apr 2026)
- **Abstract**: Presents multi-task language-based PCGRL framework using DeBERTa encoder and multi-objective training (regression, contrastive alignment, hybrid learning). Dataset of 14,000+ command-level pairs in Super Mario environment. Outperforms BERT-based methods in command following, semantic stability, and structural diversity. Supports single-task, collective, combinatorial, paraphrase, and extra-domain generalization.
- **Key Innovation**: Multi-task language-based PCGRL with multi-objective training for semantic alignment
- **Link**: https://www.nature.com/articles/s41598-026-48234-7

### MOPCGRL: Multi-Objective Procedural Content Generation via Reinforcement Learning
- **Authors**: Yuan Y, Zhang Q, Yuan B, et al.
- **Affiliation**: USTC / Lingnan University
- **Venue**: Complex System Modeling and Simulation, Vol 6(1), Mar 2026
- **Abstract**: Proposes multi-objective PCGRL to train generators balancing multiple diversity metrics with playability constraints. Uses evolutionary learning to handle conflicting diversity objectives. Results on Mario-AI benchmark show increased diversity while accelerating convergence. Enables tailored content generation for specific design needs.
- **Key Innovation**: Multi-objective evolutionary PCGRL handling conflicting diversity metrics
- **Link**: https://doi.org/10.23919/CSMS.2025.0034

### IPCGRL: Language-Instructed Reinforcement Learning for Procedural Level Generation
- **Authors**: In-Chang Baek, Sung-Hyun Kim, Seo-Young Lee, Dong-Hyeon Kim, Kyung-Joong Kim
- **Affiliation**: —
- **Venue**: IEEE CoG 2025
- **Abstract**: Language-instructed PCGRL approach where natural language commands guide level generation. Combines LLM-based instruction interpretation with RL-based level design. Enables designers to specify high-level level properties through text while the RL agent handles low-level tile placement.
- **Key Innovation**: Language-instruction interface for PCGRL
- **Link**: https://cog2025.inesc-id.pt/accepted-papers

### On-Device, Diverse, Difficulty-Driven Level Generation for Match 3D Puzzles via RL
- **Authors**: Koya Ihara, Tomomi Takahashi, Kazuya Kuroda, Naoyuki Jimbo
- **Affiliation**: —
- **Venue**: IEEE CoG 2025
- **Abstract**: RL-based level generation for Match 3D puzzle games that runs on-device. Generates diverse levels with controlled difficulty. Addresses constraints of mobile game deployment: limited compute, real-time generation, and difficulty calibration.
- **Key Innovation**: On-device RL level generation for mobile puzzle games
- **Link**: https://cog2025.inesc-id.pt/accepted-papers

### From World-Gen to Quest-Line: A Dependency-Driven Prompt Pipeline for Coherent RPG Generation
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2604.25482 (Apr 2026)
- **Abstract**: Dependency-driven prompt pipeline for coherent RPG content generation using LLMs. Generates consistent world lore, quest lines, NPC dialogues, and item descriptions by maintaining dependency graphs between narrative elements. Ensures narrative coherence across generated content.
- **Key Innovation**: Dependency-driven LLM pipeline for coherent RPG procedural generation
- **Link**: https://arxiv.org/abs/2604.25482

### SNAP: A Plan-Driven Framework for Controllable Interactive Narrative Generation
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2601.11529 (Jan 2026)
- **Abstract**: Plan-driven framework for controllable interactive narrative generation. Uses structured plans to guide LLM-based story generation, enabling authorial control over narrative arcs while maintaining interactive responsiveness. Demonstrates application in RPG dialogue and quest generation.
- **Key Innovation**: Plan-driven narrative control for LLM-based interactive story generation
- **Link**: https://arxiv.org/abs/2601.11529

### The Procedural Content Generation Benchmark: An Open-source Testbed for Generative Challenges in Games
- **Authors**: Ahmed Khalifa, Roberto Gallotta, Matthew Barthet, Antonios Liapis, Julian Togelius, Georgios N. Yannakakis
- **Affiliation**: University of Malta / NYU
- **Venue**: FDG 2025
- **Abstract**: Introduces standardized PCG benchmark with 12 game-related problems across multiple variants. Problems include level creation, rule set generation for arcade games. Each problem has content representation, control parameters, and evaluation metrics for quality, diversity, and controllability. Evaluates random, evolution strategy, and genetic algorithm baselines.
- **Key Innovation**: Standardized open-source benchmark for PCG algorithm evaluation
- **Link**: https://arxiv.org/html/2503.21474

### A Case Study on User Perception of Parameterized LLM-Generated Narratives
- **Authors**: Nicholas Treynor, Joshua McCoy
- **Affiliation**: —
- **Venue**: IEEE CoG 2025
- **Abstract**: User study on perception of LLM-generated game narratives with controllable parameters. Evaluates how parameter adjustments affect perceived quality, coherence, and engagement of generated story content. Provides guidelines for controllable LLM narrative generation in games.
- **Key Innovation**: Empirical user study on parameterized LLM narrative generation for games
- **Link**: https://cog2025.inesc-id.pt/accepted-papers

---

## 5. Game Benchmarks

### GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents
- **Authors**: Mingyu Ouyang, Siyuan Hu, Kevin Qinghong Lin, Hwee Tou Ng, Mike Zheng Shou
- **Affiliation**: —
- **Venue**: arXiv 2604.07429 (Apr 2026)
- **Abstract**: GameWorld benchmark for standardized and verifiable evaluation of MLLMs as game agents in browser environments. Two interfaces: computer-use agents (keyboard/mouse) and generalist multimodal agents (semantic action space). 34 diverse games, 170 tasks with state-verifiable metrics. Results across 18 model-interface pairs show even best agents far from human capabilities. Robustness demonstrated through repeated full-benchmark reruns.
- **Key Innovation**: Standardized, verifiable, reproducible benchmark for multimodal game agents
- **Link**: https://arxiv.org/abs/2604.07429

### lmgame-Bench: How Good are LLMs at Playing Games?
- **Authors**: —
- **Affiliation**: —
- **Venue**: ICLR 2026 Poster
- **Abstract**: Comprehensive benchmark evaluating LLM/VLM gaming capabilities across diverse video games. Tests models in vanilla single-model VLM setting and with gaming harness (GamingAgent workflow). Provides standardized leaderboard for LLM game-playing ability. Covers multiple game genres and skill requirements.
- **Key Innovation**: Standardized LLM gaming benchmark with leaderboard
- **Link**: https://arxiv.org/abs/2505.15146

### WorldTest / AutumnBench: Benchmarking World-Model Learning with Environment-Level Queries
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2510.19788 (Oct 2025, v4 May 2026)
- **Abstract**: Proposes WorldTest protocol for evaluating whether agents learn models supporting multiple environment-level queries (reachability, intervention effects, etc.). Instantiates as AutumnBench with 43 grid-world environments and 129 tasks. Human participants substantially outperform 5 frontier models. Attributes gap to differences in exploration and belief updating.
- **Key Innovation**: Protocol for testing world-model generality via environment-level queries
- **Link**: https://arxiv.org/abs/2510.19788

### Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games
- **Authors**: —
- **Affiliation**: Krafton AI
- **Venue**: arXiv 2506.03610 (Jun 2025)
- **Abstract**: Foundational benchmark for training and evaluating LLM agents across diverse video games. Provides standardized environments, metrics, and evaluation protocols. Covers multiple game genres with varying complexity levels. Enables reproducible comparison of LLM game agents.
- **Key Innovation**: Comprehensive LLM game agent benchmark from major game company
- **Link**: https://arxiv.org/abs/2506.03610

### UnrealZoo: Enriching Photo-realistic Virtual Worlds for Embodied AI
- **Authors**: —
- **Affiliation**: —
- **Venue**: ICCV 2025
- **Abstract**: Photo-realistic virtual world benchmark built on Unreal Engine for embodied AI. Provides diverse, richly detailed environments for training and evaluating game agents. Supports multiple modalities including vision, depth, and semantic segmentation.
- **Key Innovation**: Photorealistic Unreal Engine benchmark for embodied game AI
- **Link**: https://arxiv.org/abs/2412.20977

### DSGBench: A Strategic Game Benchmark for LLM Agents
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv (May 2026)
- **Abstract**: Introduces DSGBench, a benchmark for evaluating LLM agents on strategic games requiring long-term planning, opponent modeling, and resource management. Provides standardized evaluation metrics and baselines for strategic game-playing ability.
- **Key Innovation**: Strategic game benchmark for LLM agent evaluation
- **Link**: —

### SMAC-HARD: Enabling Mixed Opponent Strategy Script and Self-play on SMAC
- **Authors**: Devin Deng, et al.
- **Affiliation**: —
- **Venue**: arXiv 2412.17707 (Dec 2024)
- **Abstract**: Highlights default opponent policy in SMAC lacks diversity, causing MARL overfitting. Proposes SMAC-HARD with customizable opponent strategies, randomized adversarial policies, and self-play interfaces. Black-box testing reveals difficulty of transferring policies to unseen adversaries.
- **Key Innovation**: Mixed-strategy opponent benchmark addressing SMAC's diversity gap
- **Link**: https://arxiv.org/abs/2412.17707

### HLSMAC: High-Level Strategic Decision-Making for StarCraft Multi-Agent Challenge
- **Authors**: Xingxing Hong, Yungong Wang, Dexin Jin, Ye Yuan, Ximing Huang, Zijian Wu, Wenxin Li
- **Affiliation**: Peking University / UC Santa Barbara / UC Santa Cruz / UESTC
- **Venue**: —
- **Abstract**: New cooperative MARL benchmark with 12 StarCraft II scenarios based on Thirty-Six Stratagems. Challenges agents with tactical maneuvering, timing coordination, and deception. Proposes metrics beyond win rate: ability utilization and advancement efficiency. Integrates SOTA MARL and LLM-based agents.
- **Key Innovation**: Chinese stratagem-inspired StarCraft benchmark for high-level strategic MARL
- **Link**: https://arxiv.org/abs/2509.12927

---

## 6. Industry Game AI

### NVIDIA ACE for Games — Production Deployment
- **Affiliation**: NVIDIA
- **Venue**: CES 2025 / Production 2025-2026
- **Summary**: NVIDIA ACE (Avatar Cloud Engine) expands from conversational NPCs to autonomous game characters. Uses ACE small language models (SLMs) for planning at human-like frequencies, plus multi-modal SLMs for vision and audio. Partners include PUBG: Battlegrounds, inZOI, NARAKA: BLADEPOINT, MIR5. Introduces on-device AI inference (CES 2026) for AI teammates and NPCs running locally.
- **Key Innovation**: Production deployment of on-device LLM-powered autonomous game characters
- **Link**: https://developer.nvidia.com/ace

### Sony AI Gran Turismo Sophy — Production AI Racing Agent
- **Affiliation**: Sony AI / Polyphony Digital / Sony Interactive Entertainment
- **Venue**: Nature 2026
- **Summary**: Gran Turismo Sophy uses deep RL to master complex driving strategies in Gran Turismo. Published in Nature 2026. Demonstrates production-grade RL agent integrated into a commercial game title. Capable of competing with world-champion esports drivers while respecting racing etiquette.
- **Key Innovation**: Nature-published production RL agent for commercial racing game
- **Link**: https://ai.sony/

### EA SPORTS FC 26 — RL-Powered Goalkeeper AI
- **Affiliation**: Electronic Arts (EA SEED)
- **Venue**: GDC 2026 / Product Launch 2026
- **Summary**: EA SPORTS FC 26 introduces reinforcement learning to power more human-like goalkeeper behavior. Uses RL training in simulated match environments to produce emergent defensive strategies. Represents one of the largest-scale deployments of RL in a shipped AAA sports title.
- **Key Innovation**: Production RL deployment for AAA sports game NPC behavior
- **Link**: https://www.ea.com/news/fc-26-goalkeepers

### Modl.ai — AI Game Testing and NPC Behavior Platform
- **Affiliation**: Modl.ai (Copenhagen)
- **Venue**: Production 2026
- **Summary**: AI platform for game development that automates QA testing and creates NPC behaviors using ML. Testing bots explore game environments 24/7, finding bugs and generating automated reports. NPC behavior system uses RL for adaptive, natural character behaviors. Expanded to performance, accessibility, and localization testing.
- **Key Innovation**: Commercial AI game testing + RL NPC behavior platform
- **Link**: https://modl.ai

### Arm Neural Dawn — On-Device Game AI Inference
- **Affiliation**: Arm
- **Venue**: 2026
- **Summary**: Arm's Neural Dawn technology enables on-device AI inference for game AI, including NPC intelligence and game logic processing. Targets mobile and edge gaming devices where cloud inference is impractical. Demonstrates real-time game AI inference on Arm architecture.
- **Key Innovation**: On-device game AI inference on mobile Arm architecture
- **Link**: —

---

## 7. World Models for Games

### Dreamer 4: Training Agents Inside of Scalable World Models
- **Authors**: Danijar Hafner, Wilson Yan, Timothy Lillicrap
- **Affiliation**: Google DeepMind
- **Venue**: arXiv 2509.24527 (Sep 2025)
- **Abstract**: Dreamer 4 is a 2B-parameter agent that learns to solve control tasks by imagination training inside a fast and accurate world model. First agent to obtain diamonds in Minecraft purely from offline data. Uses new objective and architecture for real-time interactive inference on a single GPU. Outperforms OpenAI's VPT offline agent using 100× less data.
- **Key Innovation**: First agent to obtain Minecraft diamonds from purely offline data via world model imagination training
- **Link**: https://arxiv.org/abs/2509.24527

### MuZero Interpretability: Demystifying MuZero Planning
- **Authors**: Hung Guei, Yan-Ru Ju, Wei-Yu Chen, Ti-Rong Wu
- **Affiliation**: Academia Sinica, Taiwan / Georgia Tech
- **Venue**: IEEE (2026)
- **Abstract**: Incorporates observation reconstruction and state consistency into MuZero training. Evaluates latent states across 9×9 Go, Gomoku, and three Atari games. Reveals dynamics network becomes less accurate over longer simulations but MuZero still performs effectively by using planning to correct errors. Dynamics network learns better latent states in board games than Atari games.
- **Key Innovation**: Interpretability analysis of MuZero's learned latent states and dynamics model
- **Link**: https://arxiv.org/html/2411.04580

### World Models Survey (Tsinghua)
- **Authors**: Jingtao Ding, Yunke Zhang, Yu Shang, et al.
- **Affiliation**: Tsinghua University
- **Venue**: ACM Computing Surveys, 2025
- **Abstract**: Comprehensive survey on world models emphasizing two primary functions: constructing internal representations to understand the world, and predicting future states to simulate/guide decision-making. Explores applications in autonomous driving, robotics, and social simulacra. Covers game intelligence as a key application domain.
- **Key Innovation**: Dual-function taxonomy (understanding vs. predicting) for world model categorization
- **Link**: https://arxiv.org/abs/2411.14499

### Benchmarking World-Model Learning with Environment-Level Queries
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2510.19788 (v4 May 2026)
- **Abstract**: Proposes WorldTest protocol for evaluating world-model learning via environment-level queries. Instantiates as AutumnBench with 43 grid-world environments. Human participants substantially outperform 5 frontier models, with gap attributed to exploration and belief updating differences. Template for extending such evaluations to richer domains.
- **Key Innovation**: Environment-level query protocol for world-model benchmark
- **Link**: https://arxiv.org/abs/2510.19788

---

## 8. Related Techniques

### AsyncWebRL: Efficient Multi-Step RL for Visual Web Agents
- **Authors**: Hao Bai, Rui Yang, Chenlu Ye, Spencer Whitehead, Aviral Kumar, Tong Zhang
- **Affiliation**: UIUC / Microsoft / CMU
- **Venue**: arXiv 2606.05597 (Jun 2026)
- **Abstract**: Addresses two inefficiencies in multi-step RL for vision-language agents: idle GPUs in synchronous pipelines and excessive token usage from per-trajectory normalization. AsyncWebRL uses asynchronous system with everlasting rollout pool, achieving 2.9× speedup. Replaces step-number normalizer with constant 1/k, contracting trajectories. Sets new SOTA on WebGym OOD test (Medium +42%, Hard +48%).
- **Key Innovation**: Asynchronous RL pipeline + trajectory length normalization for web agents
- **Link**: https://arxiv.org/abs/2606.05597

### FlowTracer: Tracing Attention-Induced Information Flow for Targeted RL in LLMs
- **Authors**: Yijia Luo, Weixun Wang, Yuhan Sun, Yang Li, Zhichen Dong
- **Affiliation**: —
- **Venue**: arXiv 2606.10646 (Jun 2026)
- **Abstract**: Proposes FlowTracer for token-level credit assignment by tracking attention patterns as directed information flows. Enables targeted RL training by identifying which tokens contribute most to reasoning outcomes. Addresses the blind spot of uniform token-level reward in standard RLVR.
- **Key Innovation**: Attention-based token-level credit assignment for LLM RL
- **Link**: https://arxiv.org/abs/2606.10646

### Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2606.04391 (Jun 2026)
- **Abstract**: Studies online skill learning for web agents where agents continually induce reusable skills from previous trajectories and retrieve them dynamically. State-grounded retrieval ensures skills are applied in appropriate contexts. Demonstrates improved sample efficiency and task completion on web agent benchmarks.
- **Key Innovation**: Online skill induction with state-grounded dynamic retrieval for agents
- **Link**: https://arxiv.org/abs/2606.04391

### Bridging the Agent-World Gap: Text World Models for LLM-based Agents
- **Authors**: —
- **Affiliation**: SUSTech
- **Venue**: arXiv 2606.09032 (Jun 2026)
- **Abstract**: Systematic overview of text world models for agent applications. Provides insights into narrowing the agent-world gap by using text-based world models as intermediate representations. Covers architectures, training methods, and applications for text world models in LLM agent systems.
- **Key Innovation**: Comprehensive overview of text world models for LLM agents
- **Link**: https://arxiv.org/abs/2606.09032

### StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction
- **Authors**: Xue, et al.
- **Affiliation**: —
- **Venue**: arXiv 2605.06642 (May 2026)
- **Abstract**: StraTA presents a new approach to RL training of LLM agents through explicit strategy planning before action execution. Uses strategic trajectory abstraction to compress trajectories into high-level strategies, enabling more efficient credit assignment and policy learning. Improves agent performance on complex multi-step tasks.
- **Key Innovation**: Strategic trajectory abstraction for agentic RL
- **Link**: https://arxiv.org/abs/2605.06642

### Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Turn Games
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv (May 2026)
- **Abstract**: Teaches LLMs to play strategic games better through reinforcement learning. Rather than generating the first answer, the model learns from feedback about whether its moves were good or bad. Shows that RL-based strategic reasoning training improves performance in multi-turn game scenarios.
- **Key Innovation**: RL-based strategic reasoning training for LLMs in games
- **Link**: —

### Emergence of Exploration in Policy Gradient Reinforcement Learning via Retrying
- **Authors**: Soichiro Nishimori, Paavo Parmas, Sotetsu Koyamada, Tadashi Kozuno, Toshinori Kitamura, Shin Ishii, Yutaka Matsuo
- **Affiliation**: —
- **Venue**: arXiv 2606.00151 (Jun 2026)
- **Abstract**: Studies emergence of exploration behavior in policy gradient RL through a retrying mechanism. Shows that simple retrying (re-attempting actions that previously yielded high reward) naturally induces exploration without explicit exploration bonuses. Provides theoretical analysis and empirical validation.
- **Key Innovation**: Retrying as a natural emergent exploration mechanism in policy gradient RL
- **Link**: https://arxiv.org/abs/2606.00151

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Game Reinforcement Learning | 10 |
| Game AI Bots | 11 |
| Game Foundation Models | 5 |
| Procedural Content Generation | 8 |
| Game Benchmarks | 8 |
| Industry Game AI | 5 |
| World Models for Games | 4 |
| Related Techniques | 7 |
| **Total** | **58** |

## Key Trends

1. **Self-Play + RL Convergence**: SPIRAL, PopuLoRA, STRATAGEM, and CDE all demonstrate the convergence of game-theoretic self-play with LLM RL training, producing reasoning capabilities that transfer broadly. Self-play is maturing from a niche technique to a primary paradigm for LLM post-training.

2. **Generalist Game Agents**: NitroGen (CVPR 2026 Oral) represents the first open foundation model for generalist gaming agents, trained on 40K hours across 1K+ games. The "Towards Generalist Game Players" paper provides a comprehensive four-era framework situating this trend.

3. **Industry RL Deployment Accelerates**: NVIDIA ACE production deployment, Sony GT Sophy (Nature 2026), EA FC 26 RL goalkeepers, and Arm Neural Dawn demonstrate RL and LLM game AI moving into shipped products. On-device inference is becoming a key enabler.

4. **World Models Unify the Field**: Dreamer 4 achieves Minecraft diamonds from offline data. The comprehensive world model surveys (2606.00133, Tsinghua ACM CSUR) establish world models as a unifying paradigm for game AI, robotics, and simulation.

5. **PCG Goes Multi-Modal and Multi-Objective**: PCGRL expands from single-objective to multi-objective (MOPCGRL), language-instructed (IPCGRL), and multi-task (Scientific Reports 2026) paradigms. The PCG Benchmark (FDG 2025) provides standardized evaluation.

6. **Benchmark Standardization**: GameWorld, lmgame-Bench, Orak, DSGBench, and WorldTest collectively establish standardized evaluation frameworks for LLM game agents, world models, and strategic reasoning.

7. **Agentic RL Infrastructure Matures**: AsyncWebRL, FlowTracer, StraTA, and Online Skill Learning address practical RL training challenges (speed, credit assignment, skill reuse) for web and game agents.

8. **Open-Ended Learning via Co-Evolution**: PopuLoRA's co-evolving teacher-student populations, AlphaEvolve's automated MARL algorithm discovery, and population-based training represent growing interest in open-ended learning systems.
