---
title: "Game RL & Game AI Bot — Daily Synthesis (2026-06-11)"
type: synthesis
created: 2026-06-11
updated: 2026-06-11
sources: []
tags: [game-rl, game-ai, reinforcement-learning, llm-agents, foundation-models, procedural-content-generation, benchmarks, self-play, world-models]
---

# Game RL & Game AI Bot — Daily Synthesis

> Survey of recent arXiv papers and proceedings on Game RL, Game AI Bots, Game Foundation Models, Procedural Content Generation, Game Benchmarks, Industry Game AI, and related techniques. Compiled 2026-06-11.

---

## 1. Game Reinforcement Learning

### MARL-GPT: Foundation Model for Multi-Agent Reinforcement Learning
- **Authors**: Cognitive AI Systems
- **Affiliation**: —
- **Venue**: arXiv 2604.05943
- **Abstract**: Proposes a single GPT-based model that learns across diverse MARL environments (StarCraft Multi-Agent Challenge, Google Research Football, POGEMA) using offline RL on expert trajectories (1.5B total). Uses a single transformer-based observation encoder requiring no task-specific tuning.
- **Link**: https://arxiv.org/abs/2604.05943

### Mastering Generals.io with Reinforcement Learning
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2507.06825
- **Abstract**: Presents a lightweight RTS benchmark based on the browser game Generals.io, capable of thousands of frames/sec on commodity hardware. Trains a reference agent with supervised pre-training and self-play PPO, reaching top 0.003% of the human 1v1 leaderboard. Uses hierarchical agent with self-play (HASP) and potential-based reward shaping.
- **Link**: https://arxiv.org/abs/2507.06825

### K-Level Policy Gradients for Multi-Agent Reinforcement Learning
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2509.12117
- **Abstract**: Introduces KPG, harnessing k-level game-theoretic thinking to improve convergence of MARL policy gradient algorithms (MAPPO, FACMAC, MADDPG). Shows superior performance in StarCraft II (SMAC/SMAX) and multi-agent MuJoCo. Reaches ε-Nash equilibrium with finite iterates under certain conditions.
- **Link**: https://arxiv.org/abs/2509.12117

### MAT-NAHT: Transformer-Based N-Agent Ad Hoc Teamwork
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2506.05527
- **Abstract**: Centralized transformer method for N-agent ad hoc teamwork (NAHT) in partially observable environments. Outperforms POAM on StarCraft II tasks with superior sample efficiency and generalization, without auxiliary agent-modeling objectives.
- **Link**: https://arxiv.org/abs/2506.05527

### NePPO: Near-Potential Policy Optimization for General-Sum MARL
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2603.06977
- **Abstract**: Algorithm for approximating Nash equilibria in mixed cooperative–competitive games. Learns a shared potential function capturing utility changes under unilateral best-response deviations. Demonstrates low-regret approximate Nash equilibria in zero-sum and general-sum settings.
- **Link**: https://arxiv.org/abs/2603.06977

### PokeRL: Reinforcement Learning for Pokémon Red
- **Authors**: Dheeraj Reddy et al.
- **Affiliation**: —
- **Venue**: arXiv 2604.10812
- **Abstract**: Modular system training DRL agents for early-game Pokémon Red tasks. Contributions include a loop-aware environment wrapper with map masking, multi-layer anti-loop/anti-spam mechanism, and dense hierarchical reward design. Built on PyBoy emulator.
- **Link**: https://arxiv.org/abs/2604.10812

### Playing Pokémon Red via Deep Reinforcement Learning
- **Authors**: Marco Pleines, Daniel Addis, David Rubinstein, Frank Zimmer, Mike Preuss, Peter Whidden
- **Affiliation**: —
- **Venue**: arXiv 2502.19920
- **Abstract**: Baseline DRL agent completing Pokémon Red up to Cerulean City. Ablations reveal vulnerabilities in reward shaping — agents exploit specific reward signals. Argues Pokémon holds strong potential for LLM agents, hierarchical training, and advanced exploration methods.
- **Link**: https://arxiv.org/abs/2502.19920

### Efficient DRL for NetHack Strategies
- **Authors**: —
- **Affiliation**: —
- **Venue**: SciTePress 2025
- **Abstract**: Trains DRL agents for NetHack Learning Environment (NLE) using additional rewards and VAE-based architectures. Demonstrates that additional rewards improve performance over sparse reward baselines, while VAE integration has mixed results.
- **Link**: https://www.scitepress.org/Papers/2025/132531/132531.pdf

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2506.24119
- **Abstract**: Applies self-play to two-player zero-sum language games for developing reasoning capabilities in LLMs. Introduces role-conditioned advantage estimation (RAE) for stable multi-agent training. Uses distributed actor-learner architecture and TextArena for language game simulation.
- **Link**: https://arxiv.org/abs/2506.24119

### π-Play: Multi-Agent Self-Play via Privileged Self-Distillation
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2604.14054
- **Abstract**: Multi-agent self-evolution framework where an examiner generates tasks with construction paths, and a teacher uses these as privileged context for dense supervision. Transforms sparse-reward self-play into dense-feedback self-evolution. Surpasses supervised search agents 2–3× more efficiently than conventional self-play.
- **Link**: https://arxiv.org/abs/2604.14054

### PopuLoRA: Co-Evolving LLM Populations for Reasoning Self-Play
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2605.16727
- **Abstract**: Population-based asymmetric self-play with LoRA adapters on a shared frozen base. Teachers propose problems, matched students solve them, with LoRA weight-space evolution operators (mutations/crossovers). Outperforms single-agent baselines on code and math benchmarks via co-evolutionary arms race.
- **Link**: https://arxiv.org/abs/2605.16727

### OpenSIR: Open-Ended Self-Improving Reasoner
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2511.00602
- **Abstract**: Self-play framework for open-ended learning where teacher-student roles co-evolve. Optimizes for difficulty and diversity rewards, enabling autonomous progression from basic to advanced mathematics without human supervision.
- **Link**: https://arxiv.org/abs/2511.00602

### ArenaRL: Scaling RL for Open-Ended Agents via Tournament-Based Ranking
- **Authors**: Qiang Zhang et al.
- **Affiliation**: —
- **Venue**: arXiv 2601.06487
- **Abstract**: Shifts from pointwise scalar scoring to intra-group relative ranking using tournament-based pairwise evaluation. Seeded single-elimination scheme achieves O(N) complexity with near-equivalent accuracy to full O(N²) comparisons. Builds Open-Travel and Open-DeepResearch benchmarks.
- **Link**: https://arxiv.org/abs/2601.06487

### SCOPE: Self-Play via Co-Evolving Policies for Open-Ended Tasks
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2605.31433
- **Abstract**: Extends data-free self-play to open-ended tasks. A Challenger generates document-grounded tasks near the Solver's frontier; a frozen Judge writes evaluation rubrics. Improves open-ended performance by +5.4 to +10.4 points across 7–8B model families without curated data.
- **Link**: https://arxiv.org/abs/2605.31433

### XPM-WM: Diverse Agent Generation via World Models for Zero-Shot Coordination
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2506.07450
- **Abstract**: Efficient method for generating diverse cooperative agents using world models and cross-play minimization (XPM) with simulated trajectories. More sample-efficient and scalable than prior XPM methods on Overcooked AI. Evaluates on zero-shot coordination with novel partners and real humans.
- **Link**: https://arxiv.org/abs/2506.07450

### Your Self-Play Algorithm is Secretly an Adversarial Imitator
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2602.01357
- **Abstract**: Connects self-play finetuning (SPIN, SPPO, INPO) with adversarial imitation learning (AIL). Provides unified game-theoretic analysis and derives a more stable self-play algorithm based on χ² divergence and IQ-Learn / LS-IQ.
- **Link**: https://arxiv.org/abs/2602.01357

---

## 2. Game AI Bots (LLM-Powered)

### PORTAL: Agents Play Thousands of 3D Video Games
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2503.13356
- **Abstract**: Uses LLMs to generate specialized behavior trees (BTs) expressed in DSL for game-playing AI. Decouples tactical planning from execution. First approach demonstrating agents capable of playing thousands of distinct 3D video games through a unified method. VLM analyzes minimap representations.
- **Link**: https://arxiv.org/abs/2503.13356

### Orak: Foundational Benchmark for LLM Game Agents
- **Authors**: KRAFTON AI
- **Affiliation**: KRAFTON
- **Venue**: arXiv 2506.03610
- **Abstract**: Benchmark for training and evaluating LLM agents across 12 popular video games spanning all major genres. Uses plug-and-play MCP interface. Releases fine-tuning dataset of expert LLM gameplay trajectories. Includes game leaderboards, LLM battle arenas, and analyses of input modality and agentic strategies.
- **Link**: https://arxiv.org/abs/2506.03610

### Bounded Autonomy: Controlling LLM Characters in Live Multiplayer Games
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2604.04703
- **Abstract**: Control architecture for LLM characters in live multiplayer games. Organizes control around three interfaces: agent-agent interaction, agent-world action execution, and player-agent steering. Introduces probabilistic reply-chain decay, embedding-based action grounding, and "whisper" soft-steering.
- **Link**: https://arxiv.org/abs/2604.04703

### Sensi: Curriculum-Based Test-Time Learning for LLM Game Agents
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2603.17683
- **Abstract**: LLM agent architecture for ARC-AGI-3 introducing two-player architecture (perception vs action), curriculum-based learning via state machine, and database-as-control-plane. Completes learning curriculum in ~32 attempts — 50–94× greater sample efficiency than comparable systems.
- **Link**: https://arxiv.org/abs/2603.17683

### The PokeAgent Challenge
- **Authors**: —
- **Affiliation**: NeurIPS 2025 Competition
- **Venue**: arXiv 2603.15563
- **Abstract**: Large-scale Pokémon benchmark with Battling Track (20M+ battle trajectories) and Speedrunning Track (first standardized RPG speedrunning evaluation). 100+ teams in NeurIPS 2025 competition. Reveals gaps between LLM generalists, RL specialists, and elite humans.
- **Link**: https://arxiv.org/abs/2603.15563

### PokeAI: Goal-Generating, Battle-Optimizing Multi-agent System for Pokémon Red
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2506.23689
- **Abstract**: First fully text-based multi-agent LLM framework for Pokémon Red. Three specialized agents: Planning, Execution, and Critique. Closed-loop decision-making with per-agent memory. Demonstrates progression through the game using only text interface.
- **Link**: https://arxiv.org/abs/2506.23689

### Continual Harness: Online Adaptation for Self-Improving Foundation Agents
- **Authors**: Seth Karten et al. (Princeton)
- **Affiliation**: Princeton University
- **Venue**: arXiv 2605.09998
- **Abstract**: Extends Gemini Plays Pokémon (GPP) — first AI system to complete multiple Pokémon RPGs. Formalizes Continual Harness, a reset-free framework automating harness refinement through online in-context learning. Agent alternates between acting and refining its own system prompt, sub-agents, and skill library mid-episode.
- **Link**: https://arxiv.org/abs/2605.09998

### Learning Game-Playing Agents with Generative Code Optimization
- **Authors**: Zhiyi Kuang, Ryan Rong, YuCheng Yuan, Allen Nie
- **Affiliation**: —
- **Venue**: OpenReview
- **Abstract**: Uses LLM-based generative optimizer (OptoPrime) to iteratively refine game-playing code agents in Atari environments (Pong, Breakout, Space Invaders). Agents match DQN/PPO baselines with significantly fewer environment interactions. Code is human-readable by design.
- **Link**: https://openreview.net/pdf?id=ZM65X3NoTd

### SCALAR: Learning and Composing Skills via LLM Planning and RL Grounding
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2603.09036
- **Abstract**: Couples symbolic LLM planning with low-level RL through a learned skill library. LLM proposes skills with preconditions/effects/rewards; RL trains each skill; execution results refine specifications. On Craftax, achieves 1.9× higher diamond collection and 9% success reaching Gnomish Mines (vs 0% for prior methods).
- **Link**: https://arxiv.org/abs/2603.09036

### CrossHA: Training One Model to Master Cross-Level Agentic Actions via RL
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2512.09706
- **Abstract**: Unified agentic model mastering heterogeneous action spaces (APIs, GUI, code). Uses Multi-Turn GRPO for adaptive action switching. SOTA on 800+ Minecraft tasks, demonstrating emergent optimization for trajectory efficiency and long-horizon reasoning.
- **Link**: https://arxiv.org/abs/2512.09706

### CausalMACE: Causality Empowered Multi-Agents in Minecraft
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2508.18797
- **Abstract**: Holistic causality planning framework for multi-agent Minecraft. Introduces overarching task graph for global planning and causality-based dependency management. Achieves 12% improvement in multi-agent cooperative tasks and 7% in single-agent tasks.
- **Link**: https://arxiv.org/abs/2508.18797

### XENON: Experience-based Knowledge Correction for Robust Planning in Minecraft
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2505.24157
- **Abstract**: Algorithmic knowledge correction from experience for LLM planning in Minecraft. Adaptive Dependency Graph corrects item dependencies from successes; Failure-aware Action Memory corrects action knowledge from failures. With only 7B LLM, surpasses GPT-4-based agents.
- **Link**: https://arxiv.org/abs/2505.24157

### Knowledge Retrieval in LLM Gaming: Goal-Oriented Graphs
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2505.18607
- **Abstract**: Proposes directed Goal-Oriented Graph (GoG) where nodes represent goals with attributes and edges encode logical relationships. Retrieval forms complete reasoning chains. Outperforms GraphRAG variants on Minecraft tasks, especially for complex goals (iron, gold, diamond).
- **Link**: https://arxiv.org/abs/2505.18607

### Experience Transfer for Multimodal LLM Agents in Minecraft
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2604.05533
- **Abstract**: Memory-transfer-augmented MLLM agent (Echo) decomposing knowledge into five transfer dimensions. Uses Contextual State Descriptor and structured in-context analogical learning for skill transfer across Minecraft worlds. Superior learning efficiency and task generalization.
- **Link**: https://arxiv.org/abs/2604.05533

### OmniActor: A Generalist GUI and Embodied Agent
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2509.02322
- **Abstract**: Layer-heterogeneity Mixture-of-Experts for unifying GUI and embodied tasks. Shares parameters in shallow layers (understanding) and separates in deep layers (action). Trained on large-scale GUI and embodied data from OS-Atlas, LIBERO, and others.
- **Link**: https://arxiv.org/abs/2509.02322

### MAIN-VLA: Modeling Abstraction of Intention and Environment for VLA
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2602.02212
- **Abstract**: End-to-end VLA combining pixel-based control with high-level semantic abstraction for 3D open worlds and PvP games. Uses automated annotation pipeline with foundation models for latent intention extraction, plus RAG for domain-specific knowledge.
- **Link**: https://arxiv.org/abs/2602.02212

---

## 3. Game Foundation Models

### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi Fan
- **Affiliation**: NVIDIA, MineDojo
- **Venue**: CVPR 2026
- **Abstract**: Vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games. Combines internet-scale video-action dataset, multi-game benchmark environment, and unified vision-action model with large-scale behavior cloning. Fine-tuning achieves 52% relative improvement on unseen games. Dataset, evaluation suite, and model weights released.
- **Link**: https://arxiv.org/abs/2601.02427

### Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents
- **Authors**: SEED-TARS Team
- **Affiliation**: —
- **Venue**: arXiv 2510.23691
- **Abstract**: Generalist game agent with unified scalable action space (keyboard-mouse). Pre-trained on 500B+ tokens across OS, web, and games. Uses decaying continual loss and Sparse-Thinking strategy. 2× SOTA on Minecraft; near human-level on unseen web 3D games; outperforms GPT-5, Gemini-2.5-Pro, Claude-4-Sonnet on FPS benchmarks.
- **Link**: https://arxiv.org/abs/2510.23691

### Pixels2Play (P2P0.1): A Foundation Model for 3D Gameplay
- **Authors**: —
- **Affiliation**: —
- **Venue**: IEEE CoG 2025
- **Abstract**: Foundation model playing 3D video games from raw pixels with recognizable human-like behavior. Trained with behavior cloning on instrumented human data and unlabeled public videos (action imputed via inverse-dynamics model). Decoder-only transformer with auto-regressive action output on a single consumer GPU. Competent on Roblox and MS-DOS titles.
- **Link**: https://arxiv.org/abs/2508.14295

### Scaling Behavior Cloning Improves Causal Reasoning (Open-P2P / Pixels2Play)
- **Authors**: Yue et al.
- **Affiliation**: —
- **Venue**: arXiv 2601.04575
- **Abstract**: Open recipe for training a game-playing foundation model for real-time consumer GPU inference. Releases 8,300+ hours of high-quality human gameplay, code, and checkpoints. Investigates scaling laws of behavior cloning with focus on causal reasoning — larger models and more data yield more causal policies. Models up to 1.2B parameters.
- **Link**: https://arxiv.org/abs/2601.04575

### Towards Generalist Game Players: Investigation of Foundation Models in the Game Multiverse
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2605.09965
- **Abstract**: First systematic investigation of Large Foundation Models as generalist game players through a comprehensive end-to-end lifecycle (Dataset, Model, Harness, Benchmark). Analyzes LLM, VLM, VLA, and World Models across the full pipeline. Proposes evolutionary formulation of generalist game players.
- **Link**: https://arxiv.org/abs/2605.09965

### GameVerse: Can VLMs Learn from Video-based Reflection?
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2603.06656
- **Abstract**: Benchmarks VLM agents through reflect-and-retry loop across 15 games. Reveals VLMs succeed on simple tasks but struggle with generalization. Jointly leveraging failures (RL-like) and tutorials (SFT-like) outperforms either alone — a training-free paradigm mirroring SFT+RL post-training.
- **Link**: https://arxiv.org/abs/2603.06656

### Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2605.00347
- **Abstract**: Studies RL-based training of VLMs for long-horizon decision-making in Super Mario Land (100+ turns). Proposes PPO with lightweight turn-level critic, outperforming GRPO and Reinforce++. Achieves 3× average game progress over frontier models. Generalizes to unseen levels and maintains general-domain capabilities.
- **Link**: https://arxiv.org/abs/2605.00347

---

## 4. Procedural Content Generation

### IPCGRL: Language-Instructed Reinforcement Learning for Procedural Level Generation
- **Authors**: Baek et al.
- **Affiliation**: —
- **Venue**: IEEE CoG 2025
- **Abstract**: Instruction-based PCG via RL with sentence embedding model. Achieves 21.4% improvement in controllability and 17.2% in generalizability for unseen instructions in 2D level generation.
- **Link**: https://arxiv.org/abs/2503.12358

### PCGRLLM: LLM-Driven Reward Design for Procedural Content Generation RL
- **Authors**: Baek et al.
- **Affiliation**: —
- **Venue**: arXiv 2502.10906
- **Abstract**: Feedback-based reward generation framework for PCGRL. Uses self-alignment and feedback loops where LLM generates reward functions from story instructions and refines based on trained agent outcomes. Comparable to human-designed rewards.
- **Link**: https://arxiv.org/abs/2502.10906

### Procedural Game Level Design with Deep RL
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2510.15120
- **Abstract**: Co-adaptive PCG framework with two PPO agents in Unity: a hummingbird (solver) and an island (generator). The generator places collectibles based on solver performance feedback, leading to emergent behavior and robust generalization.
- **Link**: https://arxiv.org/abs/2510.15120

### Learning Local Constraints for RL Content Generators
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2605.13570
- **Abstract**: Combines Wave Function Collapse (local constraints) with PCGRL (global properties) for Lode Runner level generation. Constrains action space with WFC patterns. Produces visually satisfying and playable levels with desired global properties.
- **Link**: https://arxiv.org/abs/2605.13570

### VIPCGRL: Human-Aligned PCGRL via Text-Level-Sketch Shared Representation
- **Authors**: Baek et al.
- **Affiliation**: —
- **Venue**: arXiv 2508.09860
- **Abstract**: Extends PCGRL with three modalities (text, level, sketches) via quadruple contrastive learning in a shared embedding space. Aligns policy with human intent using embedding similarity auxiliary rewards.
- **Link**: https://arxiv.org/abs/2508.09860

### CreativeGame: Multi-Agent System for Iterative Game Generation
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2604.19926
- **Abstract**: Multi-agent system for iterative HTML5 game generation with CreativeProxyReward (programmatic signals), lineage-scoped memory, runtime validation, and mechanic-guided planning. Supports interpretable version-to-version evolution.
- **Link**: https://arxiv.org/abs/2604.19926

### AutoUE: Automated Generation of 3D Games in Unreal Engine via Multi-Agent Systems
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2603.07106
- **Abstract**: Multi-agent system for complete 3D game generation in UE. Agents include: model retrieval (858K 3D models), scene generation (PCG layout), gameplay code generation, interactive object logic, and automated play-testing.
- **Link**: https://arxiv.org/abs/2603.07106

### OpenGame: Open Agentic Coding for Games
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2604.18394
- **Abstract**: Agentic coding framework for web game creation. Includes GameCoder-27B (fine-tuned via CPT + SFT + RL on Phaser engine code). Uses execution-based RL reward from component-level unit tests. Supports multi-file game project generation.
- **Link**: https://arxiv.org/abs/2604.18394

---

## 5. Game Benchmarks

### GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents
- **Authors**: Mingyu Ouyang, Siyuan Hu, Kevin Qinghong Lin, Hwee Tou Ng, Mike Zheng Shou
- **Affiliation**: —
- **Venue**: arXiv 2604.07429
- **Abstract**: Standardized benchmark of 34 browser games across 5 genres (Runner, Arcade, Platformer, Puzzle, Simulation) with 170 tasks. Sandbox pauses game during inference, decoupling latency from decision quality. Evaluates 18 model–interface pairs with Computer-Use Agents and Semantic Action Parsing.
- **Link**: https://arxiv.org/abs/2604.07429

### VideoGameBench: Can Vision-Language Models Complete Popular Video Games?
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2505.18134
- **Abstract**: Benchmark of 23 curated video games evaluating VLM-based agents on core objectives (boss fights, campaigns). Introduces VideoGameBench Lite (turn-based variant pausing emulator during inference). VG-Agent scaffolding uses ReAct with scratchpad memory and multi-frame input.
- **Link**: https://arxiv.org/abs/2505.18134

### DSGBench: Diverse Strategic Game Benchmark for LLM Agents
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2503.06047
- **Abstract**: Evaluates strategic decision-making of LLM agents across strategy games covering 5 capabilities: strategic planning, real-time decision-making, social reasoning, team collaboration, adaptive learning. Includes StarCraft II, Civilization, Street Fighter III, Werewolf, Diplomacy.
- **Link**: https://arxiv.org/abs/2503.06047

### Evaluating Interactive Reasoning in LLMs: Hierarchical Benchmark with Executable Games
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2606.00103
- **Abstract**: Benchmark of 474 executable games across 4 data structures and 3 inference modes, with 5 difficulty levels (2370 instances). Tests contextual robustness and metacognitive adaptation. Games are templated for consistent evaluation.
- **Link**: https://arxiv.org/abs/2606.00103

### lmgame-Bench: How Good are LLMs at Playing Games?
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2505.15146
- **Abstract**: Turns popular video games into reliable LLM evaluations with perception and memory scaffolds. Across 13 leading models, each game probes a unique blend of capabilities. RL training on a single game transfers to unseen games and external planning tasks.
- **Link**: https://arxiv.org/abs/2505.15146

### OmniGameArena: Unified UE5 Benchmark for VLM Game Agents
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2606.09826
- **Abstract**: 12 custom UE5 games (Solo, PvP, Coop) with Improvement Dynamics Curve (IDC) — an agentic-reflection harness. Evaluates commercial VLMs (Claude, GPT-5.5, Gemini, Kimi), open-weight VLMs, and specialized game policies (NitroGen, Open-P2P). Proactive data avoidance strategies prevent contamination.
- **Link**: https://arxiv.org/abs/2606.09826

### MineNPC-Task: Task Suite for Memory-Aware Minecraft Agents
- **Authors**: Tamil Sudaravan Mohan Doss et al.
- **Affiliation**: —
- **Venue**: arXiv 2601.05215
- **Abstract**: User-authored benchmark for memory-aware, mixed-initiative LLM agents in Minecraft. Tasks elicited from expert co-play, normalized into parametric templates with explicit preconditions and machine-checkable validators. 216 subtasks evaluated across 8 players with GPT-4o.
- **Link**: https://arxiv.org/abs/2601.05215

### Optimus-3: Towards Generalist Multimodal Minecraft Agents
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2506.10357
- **Abstract**: General-purpose Minecraft agent with knowledge-enhanced data generation, Mixture-of-Experts for heterogeneous tasks, and Multimodal Reasoning-Augmented RL using IoU-Density Reward with GRPO. Surpasses existing generalist MLLMs and SOTA agents on Minecraft tasks. 42% improvement on Embodied QA, 36% on Grounding.
- **Link**: https://arxiv.org/abs/2506.10357

---

## 6. Industry Game AI

### NVIDIA ACE & In-Game Inferencing (NVIGI) SDK
- **Affiliation**: NVIDIA
- **Venue**: NVIDIA Developer Blog / Technical Blog (2025–2026)
- **Summary**: NVIDIA ACE is a suite of digital human technologies for game characters (speech, intelligence, animation). The NVIGI SDK enables in-process C++ inference alongside rendering via CUDA-in-Graphics. Supports ACE SLMs (including Qwen3-8B), Audio2Face, and RAG plugins. Key features: Multi-LoRA adapters, Vulkan CiG support, Lua-based code agent sample for runtime NPC behavior. Latest updates: DLSS 4.5 UE plugin, multilingual AI characters, synthetic data distillation for lightweight LoRA NPCs.
- **Links**:
  - https://developer.nvidia.com/blog/bring-nvidia-ace-ai-characters-to-games-with-the-new-in-game-inferencing-sdk/
  - https://developer.nvidia.com/blog/how-to-minimize-game-runtime-inference-costs-with-coding-agents/
  - https://developer.nvidia.com/blog/nvidia-ace-adds-open-source-qwen3-slm-for-on-device-deployment-in-pc-games/

---

## 7. Related Techniques

### Curiosity-Critic: Cumulative Prediction Error Improvement as Intrinsic Reward
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2604.18701
- **Abstract**: Curiosity reward grounded in world model's cumulative prediction error improvement. Learns asymptotic error baseline via neural critic co-trained with world model. Outperforms prediction-error, RND, and count-based baselines in stochastic grid worlds.
- **Link**: https://arxiv.org/abs/2604.18701

### JOWA: Jointly-Optimized World-Action Model (Offline MBRL)
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2410.00564 (updated 2025)
- **Abstract**: Offline model-based RL agent pretrained on multiple Atari games (6B tokens). Jointly optimizes world model and Q-value critic through shared transformer backbone. 150M param model achieves 78.9% human-level performance using only 10% data. Sample-efficient transfer to novel games with only 5k offline fine-tuning data.
- **Link**: https://arxiv.org/abs/2410.00564

### Code World Models (CWM) for Game Playing
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2510.04542
- **Abstract**: Uses LLMs to translate game rules and trajectories into executable Python world models. Introduces code-based inference functions for partial observability and heuristic value functions. Outperforms "thinking" LLMs across two-player games including novel OOD games.
- **Link**: https://arxiv.org/abs/2510.04542

### Optimistic World Models (OWMs)
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2602.10044
- **Abstract**: Principled framework for optimistic exploration bringing reward-biased MLE into deep RL. Incorporates optimism via dynamics loss biasing imagined transitions toward higher-reward outcomes. Instantiates Optimistic DreamerV3 and Optimistic STORM, improving sample efficiency and returns.
- **Link**: https://arxiv.org/abs/2602.10044

### PriorZero: Bridging Language Priors and World Models
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2605.12289
- **Abstract**: Integrates LLM-derived conceptual priors into world-model-based planning via MCTS. Root-prior injection focuses search on semantically promising actions while preserving lookahead. Decoupled rollout-training design with alternating optimization. Evaluated on Jericho text games and BabyAI.
- **Link**: https://arxiv.org/abs/2605.12289

### Distilling Game Code World Model Generation
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2605.24375
- **Abstract**: Distills GameCWM generation into lightweight LLMs via SFT + RLVR. Curated 30-game dataset with hierarchical verification framework. Qwen2.5-3B becomes capable of generating valid code world models for perfect and imperfect information games.
- **Link**: https://arxiv.org/abs/2605.24375

### WOMBET: World Model-based Experience Transfer
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2604.08958
- **Abstract**: Generates offline data via uncertainty-penalized planning in source task, transfers to target task via adaptive online fine-tuning. Dual-criterion (high return + low epistemic uncertainty) filtering. Unifies offline MBRL and online adaptation.
- **Link**: https://arxiv.org/abs/2604.08958

### Self-correcting Reward Shaping via Language Models
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2506.23626
- **Abstract**: Automates RL reward weight tuning using LM-based iterative refinement based on behavioral goals and performance statistics. In a racing task, improves success rate from 9% to 74% in one iteration, reaching 80% vs human expert's 94%.
- **Link**: https://arxiv.org/abs/2506.23626

### SPLASH: Sample-efficient Preference-based IRL
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2507.08707
- **Abstract**: Learns reward functions from suboptimal hierarchical demonstrations for long-horizon adversarial tasks (Montezuma's Revenge). Uses trajectory downsampling, alignment checking, adversarial reward selection, and temporal consistency regularization.
- **Link**: https://arxiv.org/abs/2507.08707

### HiPER: Hierarchical RL with Explicit Credit Assignment for LLM Agents
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2602.16165
- **Abstract**: Hierarchical RL framework separating slow planning from fast execution. Introduces Hierarchical Advantage Estimation (HAE) with boundary-aware bootstrapping at two time scales. Improves credit assignment in long-horizon sparse-reward tasks.
- **Link**: https://arxiv.org/abs/2602.16165

### SeRL: Self-Play RL for LLMs with Limited Data
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2505.20347
- **Abstract**: Self-instruction + self-rewarding modules bootstrap LLM training with limited initial data. Majority-voting reward estimation eliminates need for external annotations. Achieves performance comparable to training with high-quality verifiable rewards.
- **Link**: https://arxiv.org/abs/2505.20347

### Reward Design Agent (RDA) for RL
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2606.01672
- **Abstract**: Uses VLM to generate subtask-level diagnostics for targeted reward edits. Evolutionary loop with VLM-based trajectory judging and failure diagnosis. Closes loop between detecting and correcting reward misalignment.
- **Link**: https://arxiv.org/abs/2606.01672

### STRATAGEM: Learning Transferable Reasoning via Game Self-Play
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2604.17696
- **Abstract**: Selectively reinforces trajectories exhibiting abstract and adaptive reasoning via Reasoning Transferability Coefficient (φ) and Reasoning Evolution Reward (ψ). Qwen3-4B trained on 3 text games achieves strong gains on competition-level math (AIME24 +6.70%, AMC23 +7.50%).
- **Link**: https://arxiv.org/abs/2604.17696

### PBT-NCA: Open-Ended Discovery via Population-Based Training
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2604.11248
- **Abstract**: Meta-evolutionary algorithm evolving populations of Neural Cellular Automata under composite novelty+diversity objectives. Spontaneously generates diverse emergent patterns. PBT-based exploit-and-explore cycles with DINOv2 visual diversity scoring.
- **Link**: https://arxiv.org/abs/2604.11248

---

## Key Trends

1. **Convergence of RL and Foundation Models**: The boundary between traditional game RL (PPO, self-play) and LLM/VLM-based agents is dissolving. Frameworks like SPIRAL, STRATAGEM, and Odysseus apply RL directly to LLMs for game-based reasoning training.
2. **Generalist Game Agents at Scale**: Game-TARS (500B+ tokens), NitroGen (40K hours, 1000+ games), and Pixels2Play demonstrate that behavior cloning at internet scale produces capable multi-game agents without per-game engineering.
3. **World Models as a Unifying Framework**: Code World Models, PriorZero, JOWA, and Optimistic World Models all leverage learned environment models for planning, exploration, and transfer — bridging the gap between model-based RL and LLM reasoning.
4. **Open-Ended Learning and Co-Evolution**: PopuLoRA, SCOPE, OpenSIR, and PBT-NCA use population-based co-evolution to sustain continuous improvement without human-curated curricula.
5. **Procedural Content Generation Goes Multi-Modal**: PCGRL methods increasingly incorporate language, sketches, and vision (IPCGRL, VIPCGRL, PCGRLLM) to give designers intuitive control over generated game content.
6. **Benchmark Standardization**: GameWorld, VideoGameBench, OmniGameArena, and Orak provide systematic evaluation frameworks with decoupled inference latency, contamination prevention, and standardized agent interfaces.
7. **Industry Deployment Matures**: NVIDIA ACE + NVIGI SDK brings on-device SLM inference (Qwen3-8B) to commercial game engines, with Multi-LoRA support and CUDA-in-Graphics for real-time NPC intelligence.
