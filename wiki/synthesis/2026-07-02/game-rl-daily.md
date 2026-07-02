---
title: Game RL & Game AI Bot — Daily Survey (2026-07-02)
type: synthesis
created: 2026-07-02
updated: 2026-07-02
sources: [arxiv-search, web-search]
tags: [game-rl, game-ai-bot, game-foundation-models, procedural-content-generation, game-benchmarks, industry-game-ai, self-play, world-models]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-07-02)

> Comprehensive survey of recent papers on Game RL, Game AI Bots, Game Foundation Models, PCG, Benchmarks, Industry Game AI, and related techniques. Compiled 2026-07-02.

---

## 1. Game RL — Reinforcement Learning in Games

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning
- **Authors**: Lei Zhu, Lutz Güertler, Simon C.H. Yu, Zichen Liu, Penghui Qi, Daniel Balcells, et al.
- **Affiliation**: —
- **Venue**: ICLR 2026
- **Key Innovations**: A self-play framework where LLMs learn by playing multi-turn zero-sum games (e.g., Connect Four, Tic-Tac-Toe) against continuously improving versions of themselves. Demonstrates that self-play in games transfers to improved reasoning on math and coding benchmarks.
- **Links**: [arXiv:2506.24119](https://arxiv.org/abs/2506.24119) | [GitHub](https://github.com/spiral-rl/spiral)

### MARSHAL: Incentivizing Multi-Agent Reasoning via Self-Play with Strategic LLMs
- **Authors**: Hui Yuan, Zhe Xu, Zhen Tan, Xianhao Yi, Guang Mo, Kaiwen Long, et al.
- **Affiliation**: THU NICS
- **Venue**: ICLR 2026
- **Key Innovations**: End-to-end RL framework for multi-agent reasoning via self-play in both cooperative and competitive games. Features turn-level advantage estimator for credit assignment and agent-specific advantage normalization. Trained agents (Qwen3-4B) achieve up to 28.7% improvement on held-out games and generalize to reasoning benchmarks (+10% on AIME, +7.6% on GPQA-Diamond).
- **Links**: [arXiv:2510.15414](https://arxiv.org/abs/2510.15414) | [GitHub](https://github.com/thu-nics/MARSHAL)

### π-Play: Multi-Agent Self-Play via Privileged Self-Distillation without External Data
- **Authors**: —
- **Affiliation**: —
- **Key Innovations**: Proposes Privileged Information Self-Play, a multi-agent self-evolution framework where an examiner generates tasks with question construction paths (QCPs), and a teacher uses QCP as privileged context to densely supervise a student via self-distillation. Transforms sparse-reward self-play into dense-feedback self-evolution, surpassing supervised search agents with 2-3× efficiency.
- **Links**: [arXiv:2604.14054](https://arxiv.org/abs/2604.14054)

### Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games
- **Authors**: —
- **Affiliation**: —
- **Key Innovations**: Borrows from game theory to apply self-play frameworks where agents share parameters. Focuses on reinforcing strategic reasoning through multi-agent game interactions.
- **Links**: [arXiv:2605.04906](https://arxiv.org/abs/2605.04906)

### Foundation Model Self-Play: Open-Ended Strategy Innovation via Foundation Models
- **Authors**: Aaron Dharna, Cong Lu, Jeff Clune
- **Affiliation**: —
- **Key Innovations**: Leverages FM code-generation capabilities for open-ended strategy innovation. Proposes three variants: Vanilla FMSP, Novelty-Search Self-Play, and Quality-Diversity Self-Play (QDSP). Evaluated in Car Tag (continuous control) and Gandalf (AI safety jailbreak simulation). Discovers diverse RL, tree search, and heuristic strategies.
- **Links**: [arXiv:2507.06466](https://arxiv.org/abs/2507.06466)

### OMAR: One Model, All Roles — Multi-Turn, Multi-Agent Self-Play RL for Conversational Social Intelligence
- **Authors**: Bowen Jiang, Taiwei Shi, Ryo Kamoi, Yuan Yuan, Camillo J. Taylor, Longqi Yang, et al.
- **Affiliation**: —
- **Key Innovations**: Single model role-plays all participants in conversations simultaneously. Hierarchical advantage estimation for long dialogues. In SOTOPIA social environments and Werewolf games, trained models develop empathy, persuasion, and compromise-seeking behaviors.
- **Links**: [arXiv:2602.03109](https://arxiv.org/abs/2602.03109)

### Conservative Equilibrium Discovery in Offline Game-Theoretic Multiagent RL
- **Authors**: Austin A. Nguyen et al.
- **Affiliation**: —
- **Key Innovations**: COffeE-PSRO extends Policy Space Response Oracles with uncertainty quantification and conservatism principles to identify low-regret equilibria from fixed datasets in mixed-motive multiagent settings. First principled offline game-solving approach.
- **Links**: [arXiv:2603.00374](https://arxiv.org/abs/2603.00374)

### ArenaRL: Scaling RL for Open-Ended Agents via Tournament-based Relative Ranking
- **Authors**: —
- **Affiliation**: Alibaba-NLP
- **Key Innovations**: Shifts from pointwise scalar scoring to intra-group relative ranking. Novel process-aware pairwise evaluation mechanism with multi-level rubrics. Tournament-based ranking provides O(N) complexity vs O(N²) for full pairwise comparison. Benchmarks: Open-Travel and Open-DeepResearch for open-ended agent tasks.
- **Links**: [arXiv:2601.06487](https://arxiv.org/abs/2601.06487) | [GitHub](https://github.com/Alibaba-NLP/qqr)

### Learning Game-Playing Agents with Generative Code Optimization
- **Authors**: Zhiyi Kuang, Ryan Rong, YuCheng Yuan, Allen Nie
- **Affiliation**: —
- **Key Innovations**: Represents game-playing policies as Python programs refined using LLMs. Applied to Atari games, achieves competitive performance with deep RL baselines while using significantly less training time and fewer environment interactions.
- **Links**: [arXiv:2508.19506](https://arxiv.org/abs/2508.19506)

### GIFT: Games as Informal Training for Generalizable LLMs
- **Authors**: Nuoyan Lyu, Bingbing Xu, Weihao Meng, Yige Yuan, Yang Zhang, Zhiyong Huang, et al.
- **Affiliation**: —
- **Key Innovations**: Proposes treating games as primary environments for LLM informal learning. Nested Training Framework with "AND" objective (sequential task composition) instead of naive mixing "OR" objective. Uses GRPO across Matrix Games, TicTacToe, and Who's the Spy. Demonstrates game-based informal learning enhances generalization.
- **Links**: [arXiv:2601.05633](https://arxiv.org/abs/2601.05633)

---

## 2. Game AI Bot — LLM-Powered Game Agents

### PokéChamp: An Expert-level Minimax Language Agent
- **Authors**: —
- **Affiliation**: —
- **Key Innovations**: LLM-powered minimax agent for Pokémon battles. LLM replaces three key modules: action sampling, opponent modeling, and value function estimation. GPT-4o achieves 76% win rate vs best LLM bot, 84% vs rule-based bot. Even Llama 3.1 8B beats previous GPT-4o bot. Projected Elo 1300-1500 (top 30%-10% human). Releases 3M+ battle dataset.
- **Links**: [arXiv:2503.04094](https://arxiv.org/abs/2503.04094) | [Project Page](https://sites.google.com/view/pokechamp-llm)

### Sensi: Learn One Thing at a Time — Curriculum-Based Test-Time Learning for LLM Game Agents
- **Authors**: Mohsen Arjmandi et al.
- **Affiliation**: —
- **Key Innovations**: Two-player architecture separating perception from action. Database-as-control-plane where agent's cognitive state resides in SQLite tables. LLM-as-judge with dynamic rubrics. Achieves 50-94× sample efficiency vs comparable systems (~32 vs 1600-3000 interactions). ARC-AGI-3 challenge.
- **Links**: [arXiv:2603.17683](https://arxiv.org/abs/2603.17683)

### Nemobot Games: Crafting Strategic AI Gaming Agents with LLMs
- **Authors**: —
- **Affiliation**: —
- **Key Innovations**: Interactive agentic engineering environment extending Shannon's taxonomy of game-playing machines with LLMs. Supports four game classes: dictionary-based, rigorously solvable, heuristic-based, and learning-based (RLHF + self-critique).
- **Links**: [arXiv:2604.21896](https://arxiv.org/abs/2604.21896)

### Bounded Autonomy: Controlling LLM Characters in Live Multiplayer Games
- **Authors**: —
- **Affiliation**: —
- **Key Innovations**: Control architecture for LLM NPCs in live multiplayer games. Three interfaces: agent-agent interaction, agent-world action execution, player-agent steering. Uses probabilistic reply-chain decay, embedding-based action grounding with fallback, and "whisper" soft-steering. Deployed in live multiplayer social game.
- **Links**: [arXiv:2604.04703](https://arxiv.org/abs/2604.04703)

### HeRoN: A Mediated RL-LLM Framework for Adaptive NPC Behavior
- **Authors**: —
- **Affiliation**: —
- **Venue**: Neural Computing and Applications
- **Key Innovations**: Mediated RL-LLM framework with functional separation and critique-based refinement. RL-controlled NPC policy + LLM strategy generator + lightweight reviewer. Up to 81% improvement in task success rate, substantially reducing constraint-violating actions. ~$0.74/simulated hour cost with GPT-5.2.
- **Links**: [Springer Link](https://link.springer.com/article/10.1007/s00521-026-12275-w)

### PORTAL: Agents Play Thousands of 3D Video Games
- **Authors**: Zhongwen Xu, Xianliang Wang, Siyi Li, Tao Yu, Liang Wang, Qiang Fu, et al.
- **Affiliation**: —
- **Key Innovations**: Language-guided policy generation via behavior trees in DSL. Hybrid policy structure combining rule-based nodes with neural components. Dual-feedback with quantitative metrics + VLM analysis. Instantaneously deployable, human-interpretable policies across thousands of FPS games.
- **Links**: [arXiv:2503.13356](https://arxiv.org/abs/2503.13356) | [Project Page](https://zhongwen.one/projects/portal)

---

## 3. Game Foundation Models — Generalist Game Agents

### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi "Jim" Fan
- **Affiliation**: NVIDIA, Princeton, etc.
- **Venue**: CVPR 2026
- **Key Innovations**: Vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games. 500M-parameter DiT architecture. Behavior cloning on largest video-action gameplay dataset from internet videos. Post-training adaptable to unseen games. Open-source.
- **Links**: [arXiv:2601.02427](https://arxiv.org/abs/2601.02427) | [GitHub](https://github.com/MineDojo/NitroGen) | [Website](https://nitrogen.minedojo.org/)

### Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents
- **Authors**: Zihao Wang, Xujing Li, Yining Ye, Junjie Fang, Haoming Wang, Longxiang Liu, et al.
- **Affiliation**: ByteDance
- **Key Innovations**: Unified scalable action space anchored to human-aligned native keyboard-mouse inputs. Pre-trained on 500B+ tokens across OS, web, and simulation games. Decaying continual loss to reduce causal confusion + Sparse-Thinking inference. ~2× success rate vs SOTA on Minecraft, beats GPT-5, Gemini-2.5-Pro, and Claude-4-Sonnet in FPS benchmarks.
- **Links**: [arXiv:2510.23691](https://arxiv.org/abs/2510.23691)

### P2P (Scaling Behavior Cloning Improves Causal Reasoning): An Open Model for Real-Time Video Game Playing
- **Authors**: Yuguang Yue, Irakli Salia, Samuel Hunt, Chris Green, Wenzhe Shi, Jonathan J. Hunt
- **Affiliation**: Elefant AI
- **Key Innovations**: Open recipe for video game playing foundation model for real-time inference on consumer GPU. Releases 8300+ hours of human gameplay, training/inference code, and pretrained checkpoints. 1.2B parameter model. Systematic scaling laws of BC — larger models and data improve causal reasoning. Playable on consumer GPU in real time.
- **Links**: [arXiv:2601.04575](https://arxiv.org/abs/2601.04575) | [GitHub](https://github.com/elefant-ai/open-p2p) | [Website](https://elefant-ai.github.io/open-p2p/)

### Towards Generalist Game Players: An Investigation of Foundation Models in the Game Multiverse
- **Authors**: —
- **Affiliation**: —
- **Key Innovations**: Comprehensive survey tracing full lifecycle of generalist game players across four pillars: Dataset, Model, Harness, Benchmark. Five fundamental trade-offs restricting the system. Five-level roadmap from single-game mastery to creator stage (simultaneous creation and evolution within game multiverse).
- **Links**: [arXiv:2605.09965](https://arxiv.org/abs/2605.09965)

### Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning
- **Authors**: Chengshuai Shi, Wenzhe Li, et al.
- **Affiliation**: Princeton Language and Intelligence
- **Key Innovations**: Systematic investigation of RL-based training of VLMs for long-horizon (100+ turns) decision-making in Super Mario Land. Adapted PPO with lightweight turn-level critic improves stability over GRPO/Reinforce++. Achieves 3×+ average game progress vs frontier models. Demonstrated cross-game generalization.
- **Links**: [arXiv:2605.00347](https://arxiv.org/abs/2605.00347) | [Website](https://odysseus-project.github.io/)

---

## 4. Procedural Content Generation

### PCGRLLM: Large Language Model-Driven Reward Design for Procedural Content Generation Reinforcement Learning
- **Authors**: In-Chang Baek, Sunghyun Kim, Sam Earle, Zehua Jiang, Noh Jin-Ha, Julian Togelius, et al.
- **Affiliation**: NYU, et al.
- **Key Innovations**: LLM-driven reward function generation for PCGRL. Feedback mechanism and reasoning-based prompt engineering. Story-to-reward generation in 2D environments. 415% and 40% performance improvements depending on LLM zero-shot capability.
- **Links**: [arXiv:2502.10906](https://arxiv.org/abs/2502.10906)

### IPCGRL: Language-Instructed Reinforcement Learning for Procedural Level Generation
- **Authors**: In-Chang Baek, Sunghyun Kim, Seo-Young Lee, Dong-Hyeon Kim, Kyung-Joong Kim
- **Affiliation**: —
- **Key Innovations**: Instruction-based PCG via RL with sentence embedding model. Fine-tunes task-specific embedding for compressing game-level conditions. Up to 21.4% improvement in controllability and 17.2% in generalizability for unseen instructions.
- **Links**: [arXiv:2503.12358](https://arxiv.org/abs/2503.12358)

### VIPCGRL: Human-Aligned PCGRL via Text-Level-Sketch Shared Representation
- **Authors**: In-Chang Baek, Seoyoung Lee, Sung-Hyun Kim, Geumhwan Hwang, Kyung-Joong Kim
- **Affiliation**: —
- **Key Innovations**: Three-modality PCGRL (text, level, sketches) with shared embedding space via quadruple contrastive learning. Auxiliary reward based on embedding similarity. Validated by both quantitative metrics and human evaluations.
- **Links**: [arXiv:2508.09860](https://arxiv.org/abs/2508.09860)

### Learning Local Constraints for Reinforcement-Learned Content Generators
- **Authors**: —
- **Affiliation**: —
- **Key Innovations**: Combines Wave Function Collapse (local patterns) with PCGRL (global playability). Constrains PCGRL action space with WFC-learned constraints. PPO-based RL for Lode Runner level generation. Achieves visually pleasing AND playable levels.
- **Links**: [arXiv:2605.13570](https://arxiv.org/abs/2605.13570)

### OpenGame: Open Agentic Coding for Games
- **Authors**: —
- **Affiliation**: —
- **Key Innovations**: First open-source agentic framework for end-to-end web game creation. Game Skill (Template + Debug skills), GameCoder-27B code LLM (continual pre-training + SFT + execution-grounded RL). OpenGame-Bench for evaluation (Build Health, Visual Usability, Intent Alignment via headless browser + VLM judging). 150 diverse game prompts.
- **Links**: [arXiv:2604.18394](https://arxiv.org/abs/2604.18394)

### GameDevBench: Evaluating Agentic Capabilities Through Game Development
- **Authors**: Wayne Chi, Yixiong Fang, Arnav Yayavaram, Siddharth Yayavaram, Seth Karten, Qiuhong Anna Wei, et al.
- **Affiliation**: —
- **Key Innovations**: First benchmark for game dev agent tasks. 132 tasks from web/video tutorials requiring multimodal understanding (code + shaders, sprites, animations). Best agent solves only 54.5%. Image/video feedback mechanisms improve Claude Sonnet 4.5 from 33.3% to 47.7%.
- **Links**: [arXiv:2602.11103](https://arxiv.org/abs/2602.11103)

---

## 5. Game Benchmarks

### OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics
- **Authors**: —
- **Affiliation**: —
- **Key Innovations**: 12 newly built Unreal Engine 5 games (Solo 7, PvP 3, Coop 2) with unified action interfaces. Improvement Dynamics Curve (IDC) — agentic-reflection harness where tool-using reflector LLM autonomously refines skill prompts across multiple rounds. Cold-start + transfer evaluation. 12 VLM agents evaluated.
- **Links**: [arXiv:2606.09826](https://arxiv.org/abs/2606.09826)

### GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents
- **Authors**: Mingyu Ouyang, Siyuan Hu, Kevin Qinghong Lin, Hwee Tou Ng, Mike Zheng Shou
- **Affiliation**: National University of Singapore
- **Key Innovations**: 34 browser games, 170 tasks, 5 genres. Outcome-based state-verifiable evaluator over serialized gameAPI state. Two interfaces: Computer-Use Agents (keyboard/mouse) and Semantic Action Parsing. 18 model-interface pairs evaluated. Sandbox decouples inference latency from gameplay scores.
- **Links**: [arXiv:2604.07429](https://arxiv.org/abs/2604.07429) | [GitHub](https://github.com/gameworld-project/gameworld) | [Website](https://gameworld-project.github.io/)

### lmgame-Bench: How Good are LLMs at Playing Games?
- **Authors**: Lanxiang Hu, Ming Huo, Yuxuan Zhang, Hongwen Yu, Eric P. Xing, Ion Stoica, et al.
- **Affiliation**: —
- **Key Innovations**: Suite of platformer, puzzle, narrative games with unified Gym-style API + lightweight perception/memory scaffolds. Addresses brittle vision, prompt sensitivity, data contamination. Two-stage DSPy prompt optimization. RL on one game transfers to unseen games and external planning tasks.
- **Links**: [arXiv:2505.15146](https://arxiv.org/abs/2505.15146) | [GitHub](https://github.com/lmgame-org/GamingAgent/lmgame-bench)

### Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games
- **Authors**: Dongmin Park, Minkyu Kim, Beongjun Choi, Junhyuck Kim, Keon Lee, Jonghyun Lee, et al.
- **Affiliation**: KRAFTON AI
- **Venue**: ICLR 2026
- **Key Innovations**: 12 popular video games spanning 6 major genres. MCP-based plug-and-play interface. Fine-tuning dataset of 11,990 expert trajectories (DeepSeek-R1-distilled) for behavioral cloning. Leaderboard, battle arena, and in-depth analysis of agentic strategies.
- **Links**: [arXiv:2506.03610](https://arxiv.org/abs/2506.03610) | [Leaderboard](https://krafton-ai.github.io/orak-leaderboard/) | [GitHub](https://github.com/krafton-ai/Orak)

### OmniPlay: The First Diagnostic Benchmark for Omni-Modal Agentic Reasoning
- **Authors**: Fuqing Bie, Shiyu Huang, Xijia Tao, Zhiqin Fang, Leyi Pan, Junzhe Chen, Min Ren, Liuyu Xiang, Zhaofeng He
- **Affiliation**: —
- **Key Innovations**: First benchmark for omni-modal (video, audio, image, text) AI through interactive games. Unified evaluation framework. Human expert baselines. Tests truly multi-modal reasoning simultaneously.
- **Links**: [arXiv:2508.04361](https://arxiv.org/abs/2508.04361) | [GitHub](https://github.com/fuqingbie/omni-game-benchmark)

### GameCraft-Bench: Can Agents Build Playable Games End-to-End in a Real Game Engine?
- **Authors**: Tongxu Luo, Rongsheng Wang, Jiaxi Bi, Chenming Xu, et al.
- **Affiliation**: —
- **Key Innovations**: 140 tasks across 15 game families in Godot engine. Agents must submit complete Godot projects with replayable demonstration traces. Verifier launches, replays, records, and scores via hidden rubric + multimodal judge. Tests engine grounding, artifact completeness, and interactive verification.
- **Links**: [arXiv:2606.17861](https://arxiv.org/abs/2606.17861)

---

## 6. Industry Game AI

### Augmenting Game AI with Deep Reinforcement Learning
- **Authors**: Alessandro Gisslén et al.
- **Affiliation**: —
- **Key Innovations**: Framework for training DRL models suitable for game AI deployment. Examples of RL-augmented game AI in production. Identifies bottlenecks and hard problems for broad industry adoption. Practicalities of deploying player-facing ML agents in modern games.
- **Links**: [arXiv:2606.20210](https://arxiv.org/abs/2606.20210)

### LEGO: Supporting LLM-enhanced Games with One Gaming GPU
- **Authors**: Han Zhao, Weihao Cui, Zeshen Zhang, Wenhao Zhang, Jiangtong Li, Quan Chen, Youmin Chen, Pu Pang, Zijun Li, Zhenhua Han, Yuqing Yang, Minyi Guo
- **Affiliation**: Shanghai Jiao Tong University, Tongji University, University of Hong Kong, Microsoft Research
- **Venue**: HPCA 2026
- **Key Innovations**: Algorithm-system co-design for co-locating LLM inference and game rendering on one GPU. Resource-oriented layer-skipping adaptor + headroom-maximizing LLM scheduler. On RTX 4090: meets latency targets in all scenarios, +28.8% rendering headroom utilization, +51.4% inference accuracy.
- **Links**: [HPCA 2026](https://2026.hpca-conf.org/details/hpca-2026-main-conference/6/LEGO-Supporting-LLM-enhanced-Games-with-One-Gaming-GPU)

### NVIDIA ACE: Game Agent SDK and In-Game Inferencing
- **Authors**: NVIDIA
- **Affiliation**: NVIDIA
- **Key Innovations**: Production-ready AI suite for in-game characters. Cloud and on-device models for speech, intelligence, animation. NVIGI SDK 1.5 introduces code agents with local SLMs. Lua-based agent code generation minimizes GPU contention. [Posted June 2026](https://developer.nvidia.com/blog/build-on-device-ai-companions-with-the-nvidia-ace-game-agent-sdk-and-unreal-engine-5-plugins/)
- **Links**: [NVIDIA Blog (Jun 2026)](https://developer.nvidia.com/blog/build-on-device-ai-companions-with-the-nvidia-ace-game-agent-sdk-and-unreal-engine-5-plugins/) | [Inference Cost Blog](https://developer.nvidia.com/blog/how-to-minimize-game-runtime-inference-costs-with-coding-agents/)

### HeRoN: RL-LLM Mediated Framework for NPCs
- **Authors**: —
- **Affiliation**: —
- **Venue**: Neural Computing and Applications, 2026
- **Key Innovations**: RL + LLM mediated architecture for adaptive NPCs. Up to 81% task success improvement. Practical cost analysis (~$0.74/hr with GPT-5.2). Designed for production deployment.
- **Links**: [Springer](https://link.springer.com/article/10.1007/s00521-026-12275-w)

---

## 7. Related Techniques

### Self-Play & Population-Based Training
| Paper | Link | Key Idea |
|-------|------|----------|
| SPIRAL — Self-Play for Reasoning | [2506.24119](https://arxiv.org/abs/2506.24119) | Multi-turn zero-sum self-play improves reasoning |
| MARSHAL — Multi-Agent Self-Play | [2510.15414](https://arxiv.org/abs/2510.15414) | Turn-level advantage + agent-specific normalization |
| π-Play — Privileged Self-Distillation | [2604.14054](https://arxiv.org/abs/2604.14054) | Question construction paths as privileged context |
| FMSP — Foundation Model Self-Play | [2507.06466](https://arxiv.org/abs/2507.06466) | FM code-gen for open-ended strategy innovation |
| OMAR — Conversational Self-Play | [2602.03109](https://arxiv.org/abs/2602.03109) | Single model role-plays all participants |

### World Models
| Paper | Link | Key Idea |
|-------|------|----------|
| WorldCam — Interactive 3D Gaming Worlds | [2603.16871](https://arxiv.org/abs/2603.16871) | Camera pose as unifying geometric representation. 3000min human gameplay dataset. Video DiT backbone. |
| GeoWorld — Geometric World Models | [2602.23058](https://arxiv.org/abs/2602.23058) | Hyperbolic JEPA preserves geometric structure. Geometric RL for energy-based optimization. |
| WoVR — World Models as Reliable Simulators | [2602.13977](https://arxiv.org/abs/2602.13977) | Controllable action-conditioned video world model + Keyframe-Initialized Rollouts. LIBERO +29.3pp, real-robot +30.0pp. |
| RWML — Reinforcement World Model Learning | [2602.05842](https://arxiv.org/abs/2602.05842) | Self-supervised world model for LLM agents via sim-to-real gap rewards. +6.9 on ALFWorld, +5.7 on τ²Bench. |
| TC-WM — Task-Centric World Models | [2605.25620](https://arxiv.org/abs/2605.25620) | Task-sufficient latent spaces from visual foundation embeddings. Supports MPC, latent diffusion planner, model-free RL. |

### Hierarchical RL & Curiosity
| Paper | Link | Key Idea |
|-------|------|----------|
| HiPER — Hierarchical RL for LLM Agents | [2602.16165](https://arxiv.org/abs/2602.16165) | Hierarchical Plan–Execute RL with Hierarchical Advantage Estimation. Separates planning from execution. |
| CuES — Curiosity-driven Synthesis for Agentic RL | [2512.01311](https://arxiv.org/abs/2512.01311) | Autonomous task generation from environment structure via intrinsic curiosity. Matches manual datasets in diversity. |
| HRC — Hierarchical RL with Causal Interventions | [2507.04373](https://arxiv.org/abs/2507.04373) | Models subgoal structure as causal graph. Targeted causal interventions for efficient exploration. 2D-Minecraft experiments. |
| Curiosity-Driven Exploration in Action Games | — | ICM-based exploration for improved game-playing performance and adaptability. |

### Inverse RL & Reward Learning
| Paper | Link | Key Idea |
|-------|------|----------|
| IR³ — Inverse RL for Reward Hacking Detection | [2602.19416](https://arxiv.org/abs/2602.19416) | Contrastive IRL (C-IRL) reconstructs implicit reward from RLHF. Sparse Autoencoders identify hacking signatures. 0.89 reward correlation, >90% precision. |
| GRACE — LLM-based Explainable Inverse RL | [2510.02180](https://arxiv.org/abs/2510.02180) | LLM + evolutionary search to generate reward as Python code. BabyAI and AndroidWorld. Interpretable, verifiable reward programs. |

### Imitation Learning & Behavior Cloning
| Paper | Link | Key Idea |
|-------|------|----------|
| P2P — Scaling BC for Video Games | [2601.04575](https://arxiv.org/abs/2601.04575) | 8300h human gameplay, 1.2B parameter BC policy. Scaling laws show larger models learn more causal policies. Consumer GPU real-time. |

---

## Key Themes & Trends

1. **Self-Play + RL as the dominant paradigm for LLM reasoning**: SPIRAL, MARSHAL, π-Play, FMSP, and OMAR all demonstrate that multi-turn game-based self-play provides a scalable, supervision-free training signal that transfers from games to general reasoning (math, coding).

2. **Generalist game foundation models converge**: NitroGen (CVPR 2026), Game-TARS (ByteDance), and P2P (Elefant) all show that large-scale behavior cloning across diverse games with unified action spaces produces generalist agents. Unified keyboard-mouse action spaces (Game-TARS, P2P) are emerging as the standard.

3. **VLM + RL convergence for long-horizon decision-making**: Odysseus (Princeton) demonstrates that PPO with turn-level critics enables 100+ turn gameplay with VLMs, achieving 3× progress vs frontier models.

4. **Game benchmarks standardize**: Orak (ICLR 2026, KRAFTON), GameWorld (NUS), lmgame-Bench, OmniGameArena (UE5), and GameCraft-Bench represent a maturing evaluation ecosystem. Key focus: outcome-based state-verifiable evaluation, multi-agent scenarios, and improvement dynamics.

5. **PCG with LLMs matures**: PCGRLLM, IPCGRL, VIPCGRL form a family of approaches integrating LLMs with PCGRL — from reward design to language-instruction conditioning to multi-modal control. WFC + RL hybrids emerge.

6. **Industry deployment accelerates**: NVIDIA ACE SDK + NVIGI (in-game inference), LEGO (HPCA 2026) for co-locating LLM and rendering on consumer GPUs, HeRoN cost analysis ($0.74/hr), and bounded autonomy architecture for multiplayer NPCs.

7. **World models for games and agents**: WorldCam (interactive 3D gaming), GeoWorld (hyperbolic geometric), WoVR (reliable simulators for VLA), RWML (self-supervised for LLM agents) — world models are unifying games, robotics, and LLM agent communities.

8. **Hierarchical, curiosity-driven, and model-based RL**: HiPER, CuES, and HRC push hierarchical/curiosity-driven methods for long-horizon sparse-reward tasks. These are increasingly applied to LLM agent training pipelines.
