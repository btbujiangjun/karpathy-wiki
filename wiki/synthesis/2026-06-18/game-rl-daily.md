---
title: Game RL & Game AI Bot Research Daily (2026-06-18)
type: synthesis
created: 2026-06-18
updated: 2026-06-18
sources: []
tags: [game-rl, game-ai, reinforcement-learning, llm-agents, procedural-content-generation, benchmarks, survey]
---

# Game RL & Game AI Bot Research Daily — 2026-06-18

A comprehensive survey of recent papers on Game RL, Game AI Bots, Game Foundation Models, Procedural Content Generation, Game Benchmarks, Industry Game AI, and related techniques. Sources span arXiv (2025–2026) and peer-reviewed proceedings.

---

## 1. Game RL — Reinforcement Learning in Games

### K-Level Policy Gradients (KPG)
- **Authors**: T. Lees et al.
- **Affiliation**: University of Tartu / Various
- **Venue**: arXiv:2509.12117 (Sep 2025)
- **Abstract**: Proposes K-Level Policy Gradients, a game-theoretic MARL algorithm that reaches ε-Nash equilibrium with finite iterates. Applied to MAPPO, FACMAC, and MADDPG.
- **Key innovation**: Recursive reasoning framework for N-player general-sum games; SOTA on SMAC, SMAX, and MAMuJoCo.
- **Link**: [arXiv:2509.12117](https://arxiv.org/abs/2509.12117)

### Optimistic Policy Reconstruction (OPR)
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2603.06793 (Mar 2026)
- **Abstract**: Improves PPO with optimistic trajectory anchoring. Across 49 Atari games at 10M interactions, OPR achieves highest score in 22 environments.
- **Key innovation**: Trajectory-level optimism bias; generalizes to CAGE Challenge 2 cyber-defense, surpassing the winning Cardiff agent.
- **Link**: [arXiv:2603.06793](https://arxiv.org/abs/2603.06793)

### Reproducing AlphaZero on Tablut: Self-Play RL for an Asymmetric Board Game
- **Authors**: T. Lees et al.
- **Affiliation**: University of Tartu
- **Venue**: arXiv:2604.05476 (Apr 2026)
- **Abstract**: Adapts AlphaZero to Tablut, an asymmetric board game. Uses separate policy/value heads per player role with shared residual trunk.
- **Key innovation**: Catastrophic forgetting mitigation via C4 augmentation, larger replay buffer, and past-checkpoint sampling. Achieves BayesElo 1235.
- **Link**: [arXiv:2604.05476](https://arxiv.org/abs/2604.05476)

### STRATAGEM: Learning Transferable Reasoning via Trajectory-Modulated Game Self-Play
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2604.17696 (Apr 2026)
- **Abstract**: Self-play framework for LLM reasoning via game-based training. Compares against Qwen3-4B-Base and SPIRAL across reasoning benchmarks.
- **Key innovation**: Trajectory-modulation mechanism for cross-task reasoning transfer.
- **Link**: [arXiv:2604.17696](https://arxiv.org/abs/2604.17696)

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors**: B. Liu, L. Guertler, S. Yu et al.
- **Affiliation**: MIT / Various
- **Venue**: arXiv:2506.24119 (Jun 2025, updated 2026)
- **Abstract**: Self-play framework where LLMs learn by playing multi-turn zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation). Role-conditioned Advantage Estimation (RAE) stabilizes multi-agent training.
- **Key innovation**: Up to 10% improvement across 8 reasoning benchmarks; works on Qwen, Llama, DeepSeek-R1-Distill. Multi-game training yields strongest results.
- **Link**: [arXiv:2506.24119](https://arxiv.org/abs/2506.24119)

### Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2605.00347 (May 2026)
- **Abstract**: RL-based training of VLMs for long-horizon decision-making in Super Mario Land (100+ turns). Adapted PPO with lightweight turn-level critic.
- **Key innovation**: 3× average game progress over frontier models; cross-game generalization; pretrained VLMs provide strong action priors.
- **Link**: [arXiv:2605.00347](https://arxiv.org/abs/2605.00347)

### Reinforcement Learning in Strategy-Based and Atari Games: A Review of Google DeepMind's Innovations
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2502.10303 (Feb 2025)
- **Abstract**: Comprehensive review of AlphaGo, AlphaGo Zero, MuZero from DeepMind.
- **Key innovation**: Survey covering model-based, model-free, DQN; future directions including MiniZero and multi-agent models.
- **Link**: [arXiv:2502.10303](https://arxiv.org/abs/2502.10303)

---

## 2. Game AI Bot — LLM-Powered Game Agents

### Nemobot Games: Crafting Strategic AI Gaming Agents with LLMs
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2604.21896 (Apr 2026)
- **Abstract**: LLM-based game programming framework extending Shannon's taxonomy. Four game classes: dictionary-based, solvable, heuristic, learning-based games.
- **Key innovation**: Self-programming AI agents with RLHF and self-critique; integrated LLM chatbot for strategy refinement.
- **Link**: [arXiv:2604.21896](https://arxiv.org/abs/2604.21896)

### Sensi: Curriculum-Based Test-Time Learning for LLM Game Agents
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2603.17683 (Mar 2026)
- **Abstract**: Two-player LLM agent architecture for ARC-AGI-3. Separates perception from action; uses database-as-control-plane and LLM-as-judge.
- **Key innovation**: 50–94× greater sample efficiency than comparable systems (32 vs 1,600–3,000 interactions). Diagnoses self-consistent hallucination cascade.
- **Link**: [arXiv:2603.17683](https://arxiv.org/abs/2603.17683)

### LLM Reasoner and Automated Planner: A New NPC Approach
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2501.10106 (Jan 2025)
- **Abstract**: Integrates LLM decision-making with classical automated planning for NPCs in serious games.
- **Key innovation**: LLM selects goals, AP generates sound plans; handles unforeseen scenarios without exhaustive specification.
- **Link**: [arXiv:2501.10106](https://arxiv.org/abs/2501.10106)

### The PokeAgent Challenge
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2603.15563 (Mar 2026)
- **Abstract**: Large-scale benchmark for decision-making on Pokémon with 20M+ battle trajectories. Battling and Speedrunning tracks. NeurIPS 2025 competition.
- **Key innovation**: Reveals gaps between generalist LLMs, specialist RL, and elite humans. Pokémon battling is nearly orthogonal to standard LLM benchmarks.
- **Link**: [arXiv:2603.15563](https://arxiv.org/abs/2603.15563)

### PokéChamp: An Expert-Level Minimax Language Agent
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2503.04094 (Mar 2025)
- **Abstract**: LLM-powered minimax agent for Pokémon battles. LLM replaces action sampling, opponent modeling, and value function estimation.
- **Key innovation**: 76% win rate vs best LLM bot; 84% vs rule-based bot; GPT-4o powered. Largest real-player Pokémon dataset (3M+ games).
- **Link**: [arXiv:2503.04094](https://arxiv.org/abs/2503.04094)

### PORTAL: Agents Play Thousands of 3D Video Games
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2503.13356 (Mar 2025)
- **Abstract**: LLM generates behavior trees (BTs) in DSL for game AI agents. Decouples planning from execution.
- **Key innovation**: First unified approach for thousands of distinct 3D games; real-time performance without LLM latency constraints.
- **Link**: [arXiv:2503.13356](https://arxiv.org/abs/2503.13356)

### LLM-Driven NPCs: Cross-Platform Dialogue System
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2504.13928 (Apr 2025)
- **Abstract**: LLM-powered NPCs communicating across Unity (in-game) and Discord (social) via cloud database (LeanCloud).
- **Key innovation**: Cross-platform memory synchronization; DeepSeek-R1 model; location-aware responses.
- **Link**: [arXiv:2504.13928](https://arxiv.org/abs/2504.13928)

### OpenGame: Open Agentic Coding for Games
- **Authors**: Y. Jiang et al.
- **Affiliation**: Academic
- **Venue**: arXiv:2604.18394 (Apr 2026)
- **Abstract**: First open-source agentic framework for end-to-end web game creation. GameCoder-27B LLM with continual pre-training, SFT, and execution-grounded RL.
- **Key innovation**: Game Skill (Template + Debug) for reusable development; OpenGame-Bench evaluation pipeline with headless browser + VLM judging. SOTA on 150 diverse game prompts.
- **Link**: [arXiv:2604.18394](https://arxiv.org/abs/2604.18394)

### Cutscene Agent: LLM Agent-Driven Cutscene Generation in Unreal Engine
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2604.25318 (Apr 2026)
- **Abstract**: MCP-based framework for generating game cutscenes as native UE assets. Bidirectional agent-engine integration.
- **Key innovation**: Cutscene Toolkit implementing MCP in Unreal Engine; real-time scene state awareness; 8 LLMs evaluated across 5 complexity tiers.
- **Link**: [arXiv:2604.25318](https://arxiv.org/abs/2604.25318)

### Large Language Models in Game Development: Implications for Gameplay, Playability, and Player Experience
- **Authors**: R. de Souza Santos et al.
- **Affiliation**: Academic
- **Venue**: arXiv:2603.27896 (Mar 2026)
- **Abstract**: Collaborative autoethnographic study of two game projects embedding LLMs as architectural components.
- **Key innovation**: Empirical insight into LLM integration challenges: correctness, difficulty calibration, structural coherence.
- **Link**: [arXiv:2603.27896](https://arxiv.org/abs/2603.27896)

---

## 3. Game Foundation Models — Generalist Game Agents

### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: L. Magne, A. Awadalla, G. Wang et al.
- **Affiliation**: NVIDIA / MineDojo
- **Venue**: arXiv:2601.02427 (Jan 2026)
- **Abstract**: Vision-action foundation model trained on 40,000 hours of gameplay videos across 1,000+ games. Unified vision-action transformer via large-scale behavior cloning.
- **Key innovation**: 52% relative improvement in task success on unseen games; internet-scale action-labeled dataset extracted from public gameplay videos; universal Gymnasium API for any commercial game.
- **Link**: [arXiv:2601.02427](https://arxiv.org/abs/2601.02427)

### Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents
- **Authors**: Z. Wang et al.
- **Affiliation**: Academic / SEED
- **Venue**: arXiv:2510.23691 (Oct 2025)
- **Abstract**: Generalist game agent with unified keyboard-mouse action space. Pre-trained on 500B+ tokens across OS, web, and games.
- **Key innovation**: 2× SOTA in Minecraft; near-human generalization in unseen web 3D games; outperforms GPT-5, Gemini-2.5-Pro, Claude-4-Sonnet in FPS benchmarks.
- **Link**: [arXiv:2510.23691](https://arxiv.org/abs/2510.23691)

### Towards Generalist Game Players: Foundation Models in the Game Multiverse
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2605.09965 (May 2026)
- **Abstract**: First systematic investigation of Large Foundation Models (LFMs) as generalist game players. Four-pillar lifecycle: Dataset, Model, Harness, Benchmark.
- **Key innovation**: Five-level roadmap from single-game mastery to creator stage; five fundamental trade-offs bounding the system.
- **Link**: [arXiv:2605.09965](https://arxiv.org/abs/2605.09965)

### GameVerse: Can Vision-Language Models Learn from Video-based Reflection?
- **Authors**: K. Zhang, D. Liu et al.
- **Affiliation**: Tsinghua University
- **Venue**: arXiv:2603.06656 (Mar 2026)
- **Abstract**: Benchmarks VLM game agents across 15 games with reflect-and-retry loop. Failure + tutorial integration mirrors SFT+RL post-training.
- **Key innovation**: Joint failure-as-RL and tutorial-as-SFT outperforms either alone; systematic cognitive hierarchy taxonomy.
- **Link**: [arXiv:2603.06656](https://arxiv.org/abs/2603.06656)

### Pixels2Play (P2P): Scaling Behavior Cloning for Real-Time Video Game Playing
- **Authors**: Various
- **Affiliation**: Elefant AI
- **Venue**: arXiv:2601.04575 (Jan 2026)
- **Abstract**: Open recipe for game-playing foundation model running at 20 Hz on consumer GPU. 8,300+ hours of human gameplay data.
- **Key innovation**: Scaling laws of behavior cloning improve causal reasoning; models up to 1.2B parameters; real-time inference on RTX 5090.
- **Link**: [arXiv:2601.04575](https://arxiv.org/abs/2601.04575)

### MARL-GPT: Foundation Model for Multi-Agent Reinforcement Learning
- **Authors**: Various
- **Affiliation**: Cognitive AI Systems
- **Venue**: arXiv:2604.05943 (Apr 2026)
- **Abstract**: Single GPT-based model trained via offline RL on expert trajectories (400M+ steps) across SMACv2, GRF, POGEMA.
- **Key innovation**: Task-agnostic observation encoder; competitive with specialized baselines across diverse MARL environments.
- **Link**: [arXiv:2604.05943](https://arxiv.org/abs/2604.05943)

### VLMs Play StarCraft II: A Benchmark and Multimodal Decision Method
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2503.05383 (Mar 2025, updated May 2025)
- **Abstract**: VLM-Attention framework with RGB visual inputs and natural language for StarCraft II. RAG for domain knowledge; dynamic role-based task distribution.
- **Key innovation**: Zero-shot complex tactical maneuvers matching trained MARL methods; human-aligned perception.
- **Link**: [arXiv:2503.05383](https://arxiv.org/abs/2503.05383)

### MAIN-VLA: Multimodal Action-Intent Vision-Language-Action Model
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2602.02212 (Feb 2026)
- **Abstract**: VLA model with intention awareness and environmental state awareness for Game for Peace and Valorant.
- **Key innovation**: Zero-shot generalization across games (Game for Peace → Valorant, 42.9% SR); automated intention annotation using foundation models.
- **Link**: [arXiv:2602.02212](https://arxiv.org/abs/2602.02212)

---

## 4. Procedural Content Generation

### PCGRLLM: LLM-Driven Reward Design for PCG RL
- **Authors**: I. Baek, S. Kim, S. Earle, Z. Jiang et al.
- **Affiliation**: Various
- **Venue**: arXiv:2502.10906 (Feb 2025)
- **Abstract**: LLM generates reward functions for PCGRL agents with feedback mechanism and reasoning-based prompting.
- **Key innovation**: Self-alignment and feedback loops achieve human-comparable performance; reduces human dependency in game AI development.
- **Link**: [arXiv:2502.10906](https://arxiv.org/abs/2502.10906)

### IPCGRL: Language-Instructed RL for Procedural Level Generation
- **Authors**: I. Baek, S. Kim et al.
- **Affiliation**: Various
- **Venue**: IEEE CoG 2025 / arXiv:2503.12358
- **Abstract**: Sentence embedding model fine-tuned for text-to-level generation via PCGRL.
- **Key innovation**: 21.4% improvement in controllability; 17.2% better generalization for unseen instructions.
- **Link**: [arXiv:2503.12358](https://arxiv.org/abs/2503.12358)

### VIPCGRL: Human-Aligned PCGRL via Text-Level-Sketch Shared Representation
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2508.09860 (Aug 2025)
- **Abstract**: Three-modality PCGRL (text, level, sketches) with quadruple contrastive learning.
- **Key innovation**: Shared embedding space for human-AI alignment; auxiliary reward from embedding similarity. Outperforms baselines in human-likeness.
- **Link**: [arXiv:2508.09860](https://arxiv.org/abs/2508.09860)

### Learning Local Constraints for Reinforcement-Learned Content Generators
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2605.13570 (May 2026)
- **Abstract**: Combines Wave Function Collapse (WFC) with PCGRL for Lode Runner level generation.
- **Key innovation**: WFC-constrained action space ensures local visual quality while PCGRL guarantees global playability.
- **Link**: [arXiv:2605.13570](https://arxiv.org/abs/2605.13570)

### Procedural Game Level Design with Deep Reinforcement Learning
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2510.15120 (Oct 2025)
- **Abstract**: Dual-agent DRL system in Unity 3D: hummingbird (solver) and island (generator) trained with PPO.
- **Key innovation**: Co-adaptive PCG; emergent behavior from agent interaction; autonomous flower layout generation.
- **Link**: [arXiv:2510.15120](https://arxiv.org/abs/2510.15120)

### Word2World: Generating Stories and Worlds through LLMs
- **Authors**: U. Nasir et al.
- **Affiliation**: New York University / Various
- **Venue**: arXiv:2405.06686 (May 2024)
- **Abstract**: LLM-based system for generating playable 2D game worlds and narratives without task-specific fine-tuning.
- **Key innovation**: Two-step generation pipeline (story → world); supports diverse environments for open-ended RL.
- **Link**: [arXiv:2405.06686](https://arxiv.org/abs/2405.06686)

### Customizable PCG with LLMs
- **Authors**: Various
- **Affiliation**: Various
- **Venue**: SBGames 2025
- **Abstract**: Fine-tunes DeepSeek-R1-Distill-Llama-8B to generate customizable Zelda-like game levels.
- **Key innovation**: High novelty, diversity, and playability; strong adherence to input specifications.
- **Link**: [SBGames 2025](https://sol.sbc.org.br/index.php/sbgames/article/view/37377)

### Matrix-Game: Interactive World Foundation Model
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2506.18701 (Jun 2025)
- **Abstract**: Diffusion-based image-to-world generation model for Minecraft. Matrix-Game-MC dataset with action-labeled video data.
- **Key innovation**: GameWorld Score benchmark for world models; interactive video generation conditioned on keyboard/mouse inputs.
- **Link**: [arXiv:2506.18701](https://arxiv.org/abs/2506.18701)

### Matrix-Game 2.0: Real-Time Streaming Interactive World Model
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2508.13009 (Aug 2025)
- **Abstract**: Few-step auto-regressive diffusion for real-time world model. 25 FPS generation on single H100.
- **Key innovation**: Self-Forcing based distillation; 1,200 hours of UE/GTA5 data; KV caching for minute-long temporal consistency.
- **Link**: [arXiv:2508.13009](https://arxiv.org/abs/2508.13009)

### Matrix-Game 3.0: Real-Time Streaming Interactive World Model with Long-Horizon Memory
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2604.08995 (Apr 2026)
- **Abstract**: Memory-augmented interactive world model for 720p real-time (40 FPS) long-form video generation with 5B model.
- **Key innovation**: Infinite data engine combining UE synthetic + AAA games + real-world data; DMD distillation; camera-aware memory retrieval; 40 FPS at 720p.
- **Link**: [arXiv:2604.08995](https://arxiv.org/abs/2604.08995)

### High-Quality Dynamic Game Content Generation via Small Language Models
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2601.23206 (Jan 2026, updated May 2026)
- **Abstract**: Aggressive fine-tuning of SLMs on scoped tasks for real-time game content. DAG-based synthetic training data.
- **Key innovation**: Retry-until-success strategy with predictable latency; addresses offline/local deployment constraints vs cloud LLMs.
- **Link**: [arXiv:2601.23206](https://arxiv.org/abs/2601.23206)

### CreativeGame: Multi-Agent Iterative Game Generation
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2604.19926 (Apr 2026)
- **Abstract**: 7-agent system for iterative HTML5 game generation with lineage-scoped memory and proxy reward.
- **Key innovation**: MemRL-inspired runtime RL over episodic memory; mechanic-guided planning loop; interpretable version-to-version evolution.
- **Link**: [arXiv:2604.19926](https://arxiv.org/abs/2604.19926)

---

## 5. Game Benchmarks

### VideoGameBench: Can VLMs Complete Popular Video Games?
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2505.18134 (May 2025)
- **Abstract**: 23 curated video games benchmark for VLM agents. VG-Agent ReAct scaffold with memory.
- **Key innovation**: VideoGameBench Lite (turn-based variant) isolates reasoning from reaction speed; dev/test set separation to prevent contamination.
- **Link**: [arXiv:2505.18134](https://arxiv.org/abs/2505.18134)

### GameWorld: Standardized and Verifiable Evaluation of Multimodal Game Agents
- **Authors**: M. Ouyang, S. Hu, K. Q. Lin et al.
- **Affiliation**: NUS / Various
- **Venue**: arXiv:2604.07429 (Apr 2026)
- **Abstract**: 34 browser games (5 genres, 170 tasks) with outcome-based state-verifiable evaluation. Sandbox pauses during inference.
- **Key innovation**: Two interfaces: Computer-Use Agents (raw keyboard/mouse) and Semantic Action Parsing. 18 model–interface pairs evaluated.
- **Link**: [arXiv:2604.07429](https://arxiv.org/abs/2604.07429)
- **Code**: [github.com/gameworld-project/gameworld](https://github.com/gameworld-project/gameworld)

### OmniGameArena: Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics
- **Authors**: M. Lin, S. Qian, Y. Liu et al.
- **Affiliation**: Various
- **Venue**: arXiv:2606.09826 (Jun 2026)
- **Abstract**: 12 custom Unreal Engine 5 games (Solo, PvP, Coop). Introduces Improvement Dynamics Curve (IDC).
- **Key innovation**: Agentic-reflection harness measuring cross-round improvement; PDQ (quality) and LCRT (real-time) tracks; evaluates 12 agents across 3 classes.
- **Link**: [arXiv:2606.09826](https://arxiv.org/abs/2606.09826)
- **Code**: [github.com/mxlin043/OmniGameArena](https://github.com/mxlin043/OmniGameArena)

### lmgame-Bench: How Good are LLMs at Playing Games?
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2505.15146 (May 2025)
- **Abstract**: Gym-style game benchmark for LLMs with perception and memory scaffolds. Platformer, puzzle, narrative games.
- **Key innovation**: RL on a single game transfers to unseen games and external planning tasks; harness boosts 86.7% of runs above random baseline.
- **Link**: [arXiv:2505.15146](https://arxiv.org/abs/2505.15146)

### DSGBench: Diverse Strategic Game Benchmark for LLM Agents
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2503.06047 (Mar 2025, updated May 2026)
- **Abstract**: Suite of strategy games (StarCraft II, Civilization, Street Fighter III, Werewolf, Diplomacy) with fine-grained metrics.
- **Key innovation**: Unified Gym-based interface; automated scoring; covers 5 core agent capabilities.
- **Link**: [arXiv:2503.06047](https://arxiv.org/abs/2503.06047)

### Orak: Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games
- **Authors**: Various
- **Affiliation**: KRAFTON AI
- **Venue**: arXiv:2506.03610 (Jun 2025)
- **Abstract**: 12 popular video games across major genres. MCP-based plug-and-play interface. Fine-tuning dataset of expert LLM gameplay trajectories.
- **Key innovation**: Agentic module studies; LLM battle arenas; turns general LLMs into effective game agents.
- **Link**: [arXiv:2506.03610](https://arxiv.org/abs/2506.03610)

### TowerMind: Tower Defence Game Learning Environment for LLM Agents
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2601.05899 (Jan 2026)
- **Abstract**: Lightweight tower defense environment with multimodal observations (pixel, text, structured). Supports hallucination evaluation.
- **Key innovation**: Reveals performance gap between LLMs and human experts; evaluates Ape-X DQN and PPO alongside GPT-4.1, Gemini-2.5-Pro, Claude 3.7 Sonnet.
- **Link**: [arXiv:2601.05899](https://arxiv.org/abs/2601.05899)

### MineExplorer: Evaluating Open-World Exploration of MLLM Agents in Minecraft
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2605.30931 (May 2026)
- **Abstract**: Controlled benchmark for open-world exploration capabilities of MLLMs in Minecraft. Removes Minecraft-specific knowledge confound.
- **Key innovation**: Multi-agent synthesis for task graph generation; implicit multi-hop tasks; capability load analysis.
- **Link**: [arXiv:2605.30931](https://arxiv.org/abs/2605.30931)

### MineNPC-Task: Task Suite for Memory-Aware Minecraft Agents
- **Authors**: T. Sudaravan Mohan Doss et al.
- **Affiliation**: Academic
- **Venue**: arXiv:2601.05215 (Jan 2026)
- **Abstract**: User-authored benchmark with machine-checkable validators under bounded-knowledge policy. 216 subtasks evaluated with GPT-4o.
- **Key innovation**: Mixed-initiative co-play task elicitation; captures plan/action/memory events; recurring breakdown patterns documented.
- **Link**: [arXiv:2601.05215](https://arxiv.org/abs/2601.05215)

---

## 6. Industry Game AI

### AstraGame: VLM Agent Serving for Large-Scale Game Testing
- **Authors**: Y. Guo, H. Lu, M. Wu, T. Xiong, Y. Deng, D. Ran, W. Yang, T. Xie
- **Affiliation**: Peking University / Tencent / UT Dallas
- **Venue**: FSE 2026 Industry Papers
- **Abstract**: VLM-based game testing framework deployed at WeChat. Decoupled architecture: UIBrain parallelization, UIBase semantic caching, UIFormer token efficiency.
- **Key innovation**: 37.78% improvement in exploration coverage; 58% latency reduction; deployed on 24,000+ mini-games; 180,000+ issues identified.
- **Link**: [FSE 2026](https://conf.researchr.org/details/fse-2026/fse-2026-industry-papers/50/)

### NVIDIA ACE Game Agent SDK
- **Authors**: NVIDIA
- **Affiliation**: NVIDIA
- **Venue**: NVIDIA Technical Blog (Jun 2026)
- **Abstract**: Open source C/C++ framework for on-device AI NPCs with Agent, Chat, and RAG APIs. UE5 plugins for ASR, SLM, TTS.
- **Key innovation**: Used in Total War: PHARAOH (1,200+ game data tables RAG); PUBG: BATTLEGROUNDS. Local, low-latency inference on RTX GPUs.
- **Link**: [NVIDIA Developer Blog](https://developer.nvidia.com/blog/build-on-device-ai-companions-with-the-nvidia-ace-game-agent-sdk-and-unreal-engine-5-plugins/)

---

## 7. Related Techniques

### Foundation Model Self-Play (FMSP): Open-Ended Strategy Innovation
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2507.06466 (Jul 2025)
- **Abstract**: Combines multi-agent self-play with FM code generation. Three variants: vFMSP, NSSP, QDSP.
- **Key innovation**: Discovers diverse strategies in Car Tag (continuous control) and Gandalf (AI safety puzzle); first MAP-Elites algorithm without predefined dimensions.
- **Link**: [arXiv:2507.06466](https://arxiv.org/abs/2507.06466)

### π-Play: Multi-Agent Self-Play via Privileged Self-Distillation
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2604.14054 (Apr 2026)
- **Abstract**: Self-play framework where QCP (question construction path) serves as privileged context for teacher-student distillation.
- **Key innovation**: 2–3× evolutionary efficiency over conventional self-play; data-free surpassing of fully supervised search agents.
- **Link**: [arXiv:2604.14054](https://arxiv.org/abs/2604.14054)

### SeRL: Self-Play RL for LLMs with Limited Data
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2505.20347 (May 2025)
- **Abstract**: Bootstraps LLM training from limited data via self-instruction and self-rewarding (majority-voting).
- **Key innovation**: Matches performance of high-quality labeled data methods; robust online filtering for instruction quality.
- **Link**: [arXiv:2505.20347](https://arxiv.org/abs/2505.20347)

### Internalizing World Models via Self-Play Finetuning for Agentic RL
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2510.15047 (Oct 2025)
- **Abstract**: Self-play fine-tuning (SPA) for exploration of state and action spaces before policy learning.
- **Key innovation**: Exploration before exploitation yields robust internal world models; improves Pass@k without dense external rewards.
- **Link**: [arXiv:2510.15047](https://arxiv.org/abs/2510.15047)

### WorldLLM: Improving LLMs World Modeling via Curiosity-Driven Theory-Making
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2506.06725 (Jun 2025)
- **Abstract**: Combines probabilistic theory induction with curiosity-driven RL exploration for world model improvement.
- **Key innovation**: Natural language theories as hypotheses; Bayesian updating; human-interpretable world models learned through active experimentation.
- **Link**: [arXiv:2506.06725](https://arxiv.org/abs/2506.06725)

### From Curiosity to Competence: World Models and Exploration Dynamics
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2507.08210 (Jul 2025)
- **Abstract**: Studies how curiosity (novelty/information gain) and competence (empowerment) mediate exploration. Compares Tabular vs Dreamer agents.
- **Key innovation**: Formalizes adaptive exploration as balance between pursuing the unknown and the controllable; two-way interaction between exploration and representation learning.
- **Link**: [arXiv:2507.08210](https://arxiv.org/abs/2507.08210)

### HiPER: Hierarchical RL with Explicit Credit Assignment for LLM Agents
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2602.16165 (Feb 2026)
- **Abstract**: Separates high-level planning from low-level execution in LLM agents. Hierarchical Advantage Estimation (HAE).
- **Key innovation**: Boundary-aware bootstrapping across time scales; more stable learning on long-horizon sparse-reward tasks.
- **Link**: [arXiv:2602.16165](https://arxiv.org/abs/2602.16165)

### ProPlay: Procedural World Models for Self-Evolving LLM Agents
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2606.12780 (Jun 2026)
- **Abstract**: Procedure graph world model supporting preplay (rehearsal of future procedural paths). Reliability record embeddings.
- **Key innovation**: Closed-loop between memory and planning; soft guidance via procedural trajectories; improves environment understanding and self-evolution.
- **Link**: [arXiv:2606.12780](https://arxiv.org/abs/2606.12780)

### WISE: Long-Horizon Agent in Minecraft with Why-Which Reasoning
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2606.12852 (Jun 2026)
- **Abstract**: Causal Event Graph augmented with VLM-extracted causal relationships. Opportunistic Task Scheduler.
- **Key innovation**: 30% increase in sequential sparse task success with 26.4% less time; 44% improvement in adaptive non-sequential tasks with 42.5% less time. Significant synergy among components.
- **Link**: [arXiv:2606.12852](https://arxiv.org/abs/2606.12852)

### OpenHA: Open-Source Hierarchical Agentic Models in Minecraft
- **Authors**: Various
- **Affiliation**: CraftJarvis
- **Venue**: arXiv:2509.13347 (Sep 2025)
- **Abstract**: Systematic comparison of action abstractions for VLA/hierarchical agents. Chain of Action (CoA) framework unifying planning and control.
- **Key innovation**: All-in-One agent trained on diverse action spaces achieves SOTA; benchmark of 800+ tasks; fully open-sourced.
- **Link**: [arXiv:2509.13347](https://arxiv.org/abs/2509.13347)

### CrossHA: Training One Model to Master Cross-Level Agentic Actions via RL
- **Authors**: Various
- **Affiliation**: CraftJarvis
- **Venue**: arXiv:2512.09706 (Dec 2025)
- **Abstract**: Unified agent mastering heterogeneous action spaces (APIs, GUI, robotic). Multi-Turn GRPO algorithm.
- **Key innovation**: Trained on 30 tasks generalizes to 800+ Minecraft tasks; emergent trajectory efficiency optimization.
- **Link**: [arXiv:2512.09706](https://arxiv.org/abs/2512.09706)

### MineEvolve: Self-Evolution with Accumulated Knowledge for Long-Horizon Embodied Minecraft Agents
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2603.13131 (Mar 2026)
- **Abstract**: Knowledge-driven self-evolution framework converting past execution into actionable knowledge.
- **Key innovation**: Long-dependency planning and failure recovery in Minecraft; cross-task experience transformation.
- **Link**: [arXiv:2603.13131](https://arxiv.org/abs/2603.13131)

### Optimus-3: Generalist Multimodal Minecraft Agent
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2506.10357 (Jun 2025)
- **Abstract**: MoE architecture with task-level routing for Minecraft. Multimodal Reasoning-Augmented RL.
- **Key innovation**: 42% gain on Embodied QA, 36% on Grounding via IoU-Density Reward + GRPO; knowledge-enhanced data generation pipeline.
- **Link**: [arXiv:2506.10357](https://arxiv.org/abs/2506.10357)

### CODE-SHARP: Continuous Open-Ended Discovery of Skills as Hierarchical Reward Programs
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2602.10085 (Feb 2026)
- **Abstract**: FM-driven open-ended skill discovery. Skills as Python reward programs (SHARPs) in Craftax-Extended (NetHack dynamics).
- **Key innovation**: Sustains open-ended discovery at scale without hand-crafted APIs or massive human trajectories.
- **Link**: [arXiv:2602.10085](https://arxiv.org/abs/2602.10085)

### SCALAR: Learning and Composing Skills via LLM Planning and Deep RL Grounding
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: arXiv:2603.09036 (Mar 2026)
- **Abstract**: Couples symbolic LLM planning with low-level RL through a learned skill library. Crafts skills with preconditions, effects, and reward functions.
- **Key innovation**: 1.9× higher diamond collection in Craftax-Classic; 9% success reaching Gnomish Mines vs 0% for prior methods.
- **Link**: [arXiv:2603.09036](https://arxiv.org/abs/2603.09036)

### Efficient DRL for NetHack Strategies
- **Authors**: Various
- **Affiliation**: Academic
- **Venue**: ICAART 2025
- **Abstract**: DRL agent with VAE and additional rewards for NetHack Learning Environment (NLE). Compares with DreamerV3.
- **Key innovation**: Additional rewards effective for efficient learning; VAE integration challenges documented.
- **Link**: [ICAART 2025 Proceedings](https://www.scitepress.org/Papers/2025/132531/132531.pdf)

---

## Cross-Cutting Themes

1. **Convergence of LLMs and RL**: Multiple papers combine LLM reasoning with RL training (SPIRAL, STRATAGEM, Odysseus, HiPER). Self-play on games is emerging as a scalable method for developing transferable reasoning.
2. **Generalist game agents**: NitroGen, Game-TARS, MARL-GPT, and Pixels2Play demonstrate that large-scale behavior cloning + RL produces agents capable of cross-game generalization.
3. **Foundation models as game testbeds**: Benchmarks like OmniGameArena, GameWorld, VideoGameBench, and Orak provide standardized evaluation for VLMs and LLMs as game agents.
4. **PCG meets LLM**: PCGRLLM, IPCGRL, and VIPCGRL use LLMs for reward design and instruction following in procedural content generation. Matrix-Game series pushes interactive world models toward real-time deployment.
5. **Self-play evolution**: From AlphaZero reproductions (Tablut) to code-based FMSP, self-play continues to be the dominant paradigm for strategy emergence and open-ended learning.
6. **Industrial deployment**: AstraGame (Tencent/WeChat) and NVIDIA ACE demonstrate that VLM-based game testing and NPC systems are moving into production at scale.
7. **Open-source ecosystem**: Many papers release code, datasets, and model weights (NitroGen, OpenGame, Pixels2Play, MARL-GPT, OpenHA, Matrix-Game), accelerating reproducibility.
