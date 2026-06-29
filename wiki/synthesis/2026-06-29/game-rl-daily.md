---
title: Game RL & Game AI Bot — Daily Paper Digest (2026-06-29)
type: synthesis
created: 2026-06-29
updated: 2026-06-29
sources: []
tags: [game-rl, game-ai, self-play, foundation-models, marl, nlg, mcts, world-models, benchmarks, pgrl]
---

# Game RL & Game AI Bot — Daily Paper Digest

> Date: 2026-06-29. Papers gathered from arXiv, CVPR 2026, ACL 2026 Findings, ICML 2025, IJCAI 2025, and Springer.

---

## 1. Game RL — Reinforcement Learning in Games

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning
- **Authors**: Lei Zhu, Lutz Güertler, Simon C.H. Yu, Zichen Liu, Penghui Qi, Daniel Balcells, Mickel Liu, Cheston Tan, Weiyan Shi, Min Lin, Wee Sun Lee, Natasha Jaques
- **Affiliation**: Multiple institutions
- **Venue**: arXiv:2506.24119 (Jun 2025)
- **Abstract**: Self-play framework where LLMs learn by playing multi-turn, zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation) against continuously improving versions of themselves. Proposes role-conditioned advantage estimation (RAE) to stabilize multi-agent training. Improves reasoning by up to 10% across 8 benchmarks on Qwen and Llama families, outperforming SFT on 25,000 expert trajectories.
- **Key Innovation**: Fully online, multi-turn, multi-agent RL system for LLMs; RAE stabilizes multi-agent training; game-derived reasoning transfers broadly.
- **Link**: https://arxiv.org/abs/2506.24119

### Optimistic Policy Regularization (OPR)
- **Authors**: Mai Pham, Vikrant Vaze, Peter Chin
- **Affiliation**: —
- **Venue**: arXiv:2603.06793 (Mar 2026)
- **Abstract**: Lightweight mechanism that anchors policy optimization to historically successful behavior. Uses directional log-ratio reward shaping + auxiliary behavioral cloning objective. Instantiated on PPO, achieves highest score in 22 of 49 Atari games at 10M-step budget. Also generalizes to CAGE Challenge 2 cyber-defense environment.
- **Key Innovation**: Dynamic buffer of high-performing episodes mitigates premature convergence from exploration collapse.
- **Link**: https://arxiv.org/abs/2603.06793

### Stratagem: Learning Transferable Reasoning via Trajectory-Modulated Game Self-Play
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2604.17696 (Apr 2026)
- **Abstract**: Extends self-play paradigm by introducing trajectory-modulated rewards that identify and reinforce reasoning patterns that transfer beyond game-specific contexts. Moves beyond terminal win/loss signals used by SPIRAL.
- **Key Innovation**: Modulates learning signal based on trajectory-level reasoning patterns rather than just game outcomes.
- **Link**: https://arxiv.org/abs/2604.17696

### QZero: Mastering the Game of Go with Self-play Experience Replay
- **Authors**: Jingbin Liu, Xuechun Wang
- **Affiliation**: —
- **Venue**: arXiv:2601.03306 (Jan 2026)
- **Abstract**: Model-free RL algorithm for Go that forgoes search during training. Uses entropy-regularized Q-learning with single Q-value network. Trained tabula rasa for 5 months on 7 GPUs, achieving AlphaGo-comparable performance. First demonstration of model-free RL mastering Go.
- **Key Innovation**: Off-policy experience replay + model-free Q-learning at Go scale; no MCTS needed during training.
- **Link**: https://arxiv.org/abs/2601.03306

### Can Large Language Models Develop Strategic Reasoning? Post-training Insights from Learning Chess (Chess-R1)
- **Authors**: Dongyoon Hwang, Hoonjoon Lee, Jaegul Choo, Dongmin Park, Jongho Park
- **Affiliation**: KRAFTON
- **Venue**: arXiv:2507.00726 (Jul 2025)
- **Abstract**: Investigates whether LLMs can develop strategic reasoning through RL in chess. Uses chess-pretrained action-value network for dense reward (knowledge distillation). Distillation-based dense rewards outperform sparse binary rewards, but all models plateau below expert levels — suggesting pretraining deficits that RL alone cannot overcome.
- **Key Innovation**: Dense reward via chess value network distillation; identifies fundamental limitations of RL-only post-training for strategic tasks.
- **Link**: https://arxiv.org/abs/2507.00726

### Reflection of Episodes: Learning to Play Game from Expert and Self Experiences
- **Authors**: Xiaojie Xu, Zongyuan Li, Chang Lu, Runnan Qi, Yanan Ni, Ling Jiang et al.
- **Affiliation**: Multiple institutions
- **Venue**: arXiv:2502.13388 (Feb 2025)
- **Abstract**: ROE framework for LLM learning in complex environments (StarCraft II) through self-reflection. Uses keyframe selection, expert experience + self-experience for decisions, and post-game reflection to generate new self-experience. Beats Very Hard difficulty in TextStarCraft II.
- **Key Innovation**: Combines expert demonstration with self-play reflection in a structured keyframe-based framework.
- **Link**: https://arxiv.org/abs/2502.13388

### SEMA: Self-Evolving Multi-Agent Framework for Efficient Decision Making in RTS Scenarios
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2603.23875 (Mar 2026)
- **Abstract**: Multi-agent collaborative LLM framework for Real-Time Strategy games. Features dynamic observation pruning via structural entropy, hierarchical experience pool for cross-round strategy evolution, and real-time retrieval-based action correction. Evaluated on 8 StarCraft II maps with Qwen3-next-80b. Reduces latency by 50%.
- **Key Innovation**: Self-organizing collaborative evolution system with decision, evaluation, and policy agents.
- **Link**: https://arxiv.org/abs/2603.23875

### Curriculum Learning with Counterfactual Group Relative Policy Advantage for MARL
- **Authors**: Weiqiang Jin, Hongyang Du, Guizhong Liu, Dong In Kim
- **Affiliation**: Multiple institutions
- **Venue**: arXiv:2506.07548 (Jun 2025)
- **Abstract**: Dynamic curriculum learning framework for MARL that modulates opponent strength based on real-time agent performance. Proposes Counterfactual Group Relative Policy Advantage (CGRPA) for intrinsic credit assignment. Evaluated on SMAC benchmarks.
- **Key Innovation**: Self-adaptive difficulty adjustment + counterfactual credit assignment in non-stationary MARL settings.
- **Link**: https://arxiv.org/abs/2506.07548

### LLM-guided Graph Neural Coordination Framework for Cooperative MARL (LLM-GNCF)
- **Authors**: Kuang, Z., Xu, Z., Wan, L. et al.
- **Affiliation**: Multiple institutions
- **Venue**: Complex & Intelligent Systems (Springer), Jun 2026
- **Abstract**: Integrates LLM semantic reasoning with Graph Neural Coordination for MARL. LLM dynamically constructs Team-Adaptive Coordination Graph (TACG) based on strategic semantics. Introduces LLM-empowered latent reward shaping via Chain of Aggregation. Evaluated on StarCraft II micromanagement.
- **Key Innovation**: LLM-guided coordination graph construction + semantic reward shaping for sparse-reward MARL.
- **Link**: https://link.springer.com/article/10.1007/s40747-026-02356-7

---

## 2. Game AI Bot — LLM-Powered Game Agents

### AVA: Attentive VLM Agent for Mastering StarCraft II
- **Authors**: Weiyu Ma, Yuqian Fu, Zecheng Zhang, Bernard Ghanem, Guohao Li
- **Affiliation**: —
- **Venue**: ACL 2026 Findings (Jul 2026)
- **Abstract**: Introduces AVACraft, first multimodal benchmark for StarCraft II supporting both MARL and VLM paradigms. 21 scenarios covering micromanagement, coordination, and strategic planning. MARL methods achieve 27.1% win rate after 1M steps; VLMs deliver 75–81% zero-shot win rate.
- **Key Innovation**: Unified benchmark for training-based (MARL) vs zero-shot (VLM) methods in StarCraft II.
- **Link**: https://aclanthology.org/2026.findings-acl.208/

### Sensi: Learn One Thing at a Time — Curriculum-Based Test-Time Learning for LLM Game Agents
- **Authors**: Mohsen Arjmandi
- **Affiliation**: —
- **Venue**: arXiv:2603.17683 (Mar 2026)
- **Abstract**: LLM agent architecture for ARC-AGI-3 game challenge with three mechanisms: (1) two-player architecture separating perception from action, (2) curriculum-based learning managed by external state machine, (3) database-as-control-plane. Achieves 50–94× sample efficiency over comparable systems (~32 vs 1,600–3,000 attempts).
- **Key Innovation**: Structured "learn one thing at a time" curriculum with programmatically steerable context window.
- **Link**: https://arxiv.org/abs/2603.17683

### PokerSkill: LLMs Can Play Expert-Level Poker without Training or Solvers
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2605.30094 (May 2026)
- **Abstract**: Framework that elicits latent poker skills from general LLMs through structured prompt guidance — no solver queries or offline learning. Uses deterministic context engine with layered skill library (~60 action-line scenarios, 23 hand classes, 46 bet-size thresholds). Targets full Heads-Up No-Limit Texas Hold'em.
- **Key Innovation**: Pure prompting approach extracts expert-level strategic play; skill library designed by human poker experts.
- **Link**: https://arxiv.org/abs/2605.30094

### ToolPoker: How Far Are LLMs from Professional Poker Players?
- **Authors**: Minhua Lin, Enyan Dai, Hui Liu et al.
- **Affiliation**: —
- **Venue**: arXiv:2602.00528 (Feb 2026)
- **Abstract**: Systematic study of LLMs in poker tasks. Identifies three recurring flaws: reliance on heuristics, factual misunderstandings, and "knowing-doing" gap. Proposes ToolPoker combining external solvers for GTO-consistent actions. Behavior cloning + step-level RL improves reasoning style but remains insufficient.
- **Key Innovation**: Tool-integrated reasoning with external solver; identifies fundamental strategic reasoning gaps in LLMs.
- **Link**: https://arxiv.org/abs/2602.00528

### SpinGPT: LLM Approach to Playing Poker Correctly
- **Authors**: Narada Maugin, Tristan Cazenave
- **Affiliation**: —
- **Venue**: arXiv:2509.22387 (Sep 2025)
- **Abstract**: First LLM tailored to Spin & Go (3-player online poker). Two-stage training: SFT on 320k high-stakes expert decisions + RL on 270k solver-generated hands. Matches solver actions in 78% of decisions. Achieves 13.4 BB/100 vs Slumbot in heads-up.
- **Key Innovation**: First LLM for multi-player tournament poker format; hybrid SFT+RL training pipeline.
- **Link**: https://arxiv.org/abs/2509.22387

### Implicit Strategic Optimization: Long-Horizon Decision-Making in Adversarial Poker Environments
- **Authors**: Boyang Xia, Weiyou Tian, Qingnan Ren et al.
- **Affiliation**: —
- **Venue**: arXiv:2602.08041 (Feb 2026)
- **Abstract**: Introduces ISO framework with Strategic Reward Model (SRM) estimating long-run strategic value of actions + iso-grpo context-conditioned learning. Proves sublinear contextual regret bounds. Evaluated on 6-player No-Limit Texas Hold'em and competitive Pokemon.
- **Key Innovation**: Prediction-aware framework with strategic context forecasting; theoretical regret guarantees.
- **Link**: https://arxiv.org/abs/2602.08041

### CrossAgent: Training One Model to Master Cross-Level Agentic Actions via Reinforcement Learning
- **Authors**: Kaichen He, Zihao Wang, Muyao Li, Anji Liu, Yitao Liang
- **Affiliation**: —
- **Venue**: arXiv:2512.09706 (Dec 2025)
- **Abstract**: Unified agentic model mastering heterogeneous action spaces (APIs, GUI, robotic commands). Uses cold-start SFT + Multi-Turn GRPO. Evaluated on 800+ Minecraft tasks, achieving SOTA by dynamically selecting most effective interface per step.
- **Key Innovation**: Adaptive action switching between levels of abstraction; no human-specified rules.
- **Link**: https://arxiv.org/abs/2512.09706

---

## 3. Game Foundation Models — Generalist Game Agents

### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi Fan
- **Affiliation**: NVIDIA, academia
- **Venue**: **CVPR 2026 Oral** (pp. 21511–21521)
- **Abstract**: Vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games. Three key ingredients: internet-scale video-action dataset from public videos, multi-game benchmark, unified vision-action model with behavior cloning. Transfers to unseen games with up to 52% relative improvement. Dataset, evaluation suite, and weights released open-source.
- **Key Innovation**: Scalable pipeline from internet videos to game-playing agent; first open generalist gaming foundation model at this scale.
- **Link**: https://arxiv.org/abs/2601.02427

### Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents
- **Authors**: Zihao Wang, Xujing Li, Yining Ye et al.
- **Affiliation**: —
- **Venue**: arXiv:2510.23691 (Oct 2025)
- **Abstract**: Generalist game agent with unified keyboard-mouse action space. Pre-trained on 500B+ tokens. Decaying continual loss to reduce causal confusion; Sparse-Thinking strategy balancing reasoning depth and cost. 2× success over previous SOTA on Minecraft, matches fresh humans on unseen web 3D games, outperforms GPT-5/Gemini-2.5-Pro/Claude-4-Sonnet in FPS benchmarks.
- **Key Innovation**: Unified human-aligned action space across OS, web, and games; sparse reasoning for inference efficiency.
- **Link**: https://arxiv.org/abs/2510.23691

### Pixels to Play: A Foundation Model for 3D Gameplay (P2P0.1)
- **Authors**: Yuguang Yue, Chris Green, Samuel Hunt, Irakli Salia, Wenzhe Shi, Jonathan J. Hunt
- **Affiliation**: —
- **Venue**: arXiv:2508.14295 (Aug 2025)
- **Abstract**: Foundation model learning to play 3D video games from pixels. Trained with behavior cloning on instrumented human demonstrations + unlabeled public videos with imputed actions (inverse-dynamics model). Decoder-only transformer with autoregressive action output. Runs on single consumer GPU. Competent play across Roblox and MS-DOS titles.
- **Key Innovation**: End-to-end pixel-to-action on consumer GPU; inverse-dynamics model leverages unlabeled video.
- **Link**: https://arxiv.org/abs/2508.14295

### Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2605.00347 (May 2026)
- **Abstract**: Studies RL-based training of VLMs for long-horizon decision-making in Super Mario Land (100+ turns). Proposes PPO with lightweight turn-level critic, comparing against GRPO and Reinforce++. Pretrained VLMs provide strong action priors. Achieves 3× average game progress over frontier models. Cross-game generalization maintained.
- **Key Innovation**: Turn-level critic PPO stabilizes long-horizon VLM training; identifies key ingredients for multi-modal RL.
- **Link**: https://arxiv.org/abs/2605.00347

### Scaling Behavior Cloning Improves Causal Reasoning: An Open Model for Real-Time Video Game Playing
- **Authors**: Yuguang Yue, Irakli Salia, Samuel Hunt, Chris Green, Wenzhe Shi, Jonathan J. Hunt
- **Affiliation**: —
- **Venue**: arXiv:2601.04575 (Jan 2026)
- **Abstract**: Open recipe for training game-playing foundation model. Releases 8,300+ hours of high-quality human gameplay, training/inference code, pretrained checkpoints. Model plays diverse 3D video games at human-competitive level in real-time on consumer GPU. Examines scaling laws for behavior cloning in games.
- **Key Innovation**: Fully open dataset, code, and model; scaling law analysis for game-playing BC.
- **Link**: https://arxiv.org/abs/2601.04575

### The Latent Bridge: A Continuous Slow–Fast Channel for Real-Time Game Agents
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2606.24470 (Jun 2026)
- **Abstract**: Couples frozen reactive VLM (9B, ~15 Hz) with reasoning VLM (8B, ~1 Hz) via learned continuous Latent Bridge. Projects slow model's residuals into fast model's embedding space (LLaVA-style). Evaluated on 7 Atari games and MetaDrive. Latent Bridge significantly improves two games (MsPacman +57%, RoadRunner +28%).
- **Key Innovation**: Continuous latent channel avoids text round-trip bottleneck between slow reasoning and fast reactive models.
- **Link**: https://arxiv.org/abs/2606.24470

### MARL-GPT: Foundation Model for Multi-Agent Reinforcement Learning
- **Authors**: —
- **Affiliation**: Cognitive AI Systems
- **Venue**: arXiv:2604.05943 (Apr 2026)
- **Abstract**: Single GPT-based model performing well across diverse MARL environments (SMACv2, Google Research Football, POGEMA). Applies offline RL at scale on expert trajectories (400M for SMACv2, 100M for GRF, 1B for POGEMA). Single transformer-based observation encoder with no task-specific tuning.
- **Key Innovation**: First multi-task foundation model for MARL across significantly different domains.
- **Link**: https://arxiv.org/abs/2604.05943

### Towards Generalist Game Players: An Investigation of Foundation Models in the Game Multiverse
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2605.09965 (May 2026)
- **Abstract**: First systematic survey of Large Foundation Models (LLMs, VLMs, VLAs, World Models) as generalist game players. Proposes pipeline-oriented perspective covering Dataset, Model, Harness, and Benchmark as coupled closed loop. Characterizes three eras: hand-crafted → deep RL → foundation models.
- **Key Innovation**: Comprehensive pipeline-oriented taxonomy of generalist game agents.
- **Link**: https://arxiv.org/abs/2605.09965

---

## 4. Procedural Content Generation — RL & LLM for Game Content

### IPCGRL: Language-Instructed Reinforcement Learning for Procedural Level Generation
- **Authors**: In-Chang Baek, Sunghyun Kim, Seo-Young Lee, Dong-Hyeon Kim, Kyung-Joong Kim
- **Affiliation**: —
- **Venue**: arXiv:2503.12358 (Mar 2025)
- **Abstract**: Instruction-based PCG via RL using sentence embedding model. Fine-tunes task-specific embedding representations for game-level conditions. Up to 21.4% improvement in controllability and 17.2% improvement in generalizability for unseen instructions in 2D level generation.
- **Key Innovation**: Text-conditioned RL for level generation; task-specific embedding fine-tuning.
- **Link**: https://arxiv.org/abs/2503.12358

### VIPCGRL: Human-Aligned Procedural Level Generation via Text-Level-Sketch Shared Representation
- **Authors**: In-Chang Baek, Seoyoung Lee, Sung-Hyun Kim, Geumhwan Hwang, Kyung-Joong Kim
- **Affiliation**: —
- **Venue**: arXiv:2508.09860 (Aug 2025)
- **Abstract**: Deep RL framework incorporating three modalities (text, level, sketches) for human-aligned PCG. Introduces shared embedding space via quadruple contrastive learning across modalities and human-AI styles. Auxiliary reward based on embedding similarity. Outperforms baselines in human-likeness.
- **Key Innovation**: Multi-modal contrastive learning for PCG controllability; human-likeness validation via human evaluation.
- **Link**: https://arxiv.org/abs/2508.09860

### Procedural Game Level Design with Deep Reinforcement Learning
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2510.15120 (Oct 2025)
- **Abstract**: Novel DRL method for procedural level design in Unity 3D. Two-agent system: hummingbird (solver) + floating island (generator), both trained with PPO. Generator places collectibles based on solver performance feedback. Emergent co-adaptive behavior.
- **Key Innovation**: Co-adaptive RL agents for simultaneous level generation and solving.
- **Link**: https://arxiv.org/abs/2510.15120

### WorldGen: From Text to Traversable and Interactive 3D Worlds
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2511.16825 (Nov 2025)
- **Abstract**: System for automatic creation of large-scale interactive 3D worlds from text prompts. Combines LLM scene layout reasoning, procedural generation, diffusion-based 3D generation, and object-aware scene decomposition. Produces geometrically consistent, visually rich worlds.
- **Key Innovation**: End-to-end text-to-interactive-3D-world pipeline.
- **Link**: https://arxiv.org/abs/2511.16825

### Narrative-to-Scene Generation: An LLM-Driven Pipeline for 2D Game Environments
- **Authors**: Yi-Chun Chen, Arnav Jhala
- **Affiliation**: —
- **Venue**: arXiv:2509.04481 (Sep 2025)
- **Abstract**: Lightweight pipeline transforming short narrative prompts into 2D tile-based game scenes. Identifies three key time frames from narrative, extracts spatial predicates ("Object-Relation-Object" triples), retrieves visual assets with affordance-aware embeddings. Cellular Automata terrain generation.
- **Key Innovation**: Narrative temporal structure to spatial scene decomposition.
- **Link**: https://arxiv.org/abs/2509.04481

### AI Gamestore: Scalable, Open-Ended Evaluation of Machine General Intelligence with Human Games
- **Authors**: Lance Ying, Ryan Truong, Prafull Sharma et al.
- **Affiliation**: —
- **Venue**: arXiv:2602.17594 (Feb 2026)
- **Abstract**: Platform using LLMs with humans-in-the-loop to synthesize human games from digital gaming platforms. Generated 100 games based on Apple App Store and Steam top charts. Frontier VLMs achieve <10% of human average score on most games. Struggles with world-model learning, memory, and planning.
- **Key Innovation**: Automated game generation from real distribution of human games for evaluation.
- **Link**: https://arxiv.org/abs/2602.17594

### MultiGen: Level-Design for Editable Multiplayer Worlds in Diffusion Game Engines
- **Authors**: Ryan Po et al.
- **Affiliation**: —
- **Venue**: arXiv:2603.06679 (Mar 2026)
- **Abstract**: Introduces explicit external memory into diffusion game engines. Decomposes generation into Memory, Observation, and Dynamics modules. Users get direct editable control over environment structure. Extends to real-time multiplayer rollouts with coherent viewpoints.
- **Key Innovation**: Persistent editable memory for diffusion-based game world generation; multiplayer support.
- **Link**: https://arxiv.org/abs/2603.06679

### A Database-Driven Framework for 3D Level Generation with LLMs
- **Authors**: Kaijie Xu, Clark Verbrugge
- **Affiliation**: —
- **Venue**: arXiv:2508.18533 (Aug 2025)
- **Abstract**: Framework for generating 3D game levels using LLM-assisted construction of reusable databases for architectural components and gameplay mechanics. Multi-phase pipeline: room selection, facility layout optimization, mechanics integration. Two-phase repair system ensures navigability.
- **Key Innovation**: Modular database-driven design with constraint-based optimization for PCG.
- **Link**: https://arxiv.org/abs/2508.18533

### CreativeGame: Multi-Agent System for Iterative HTML5 Game Generation
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2604.19926 (Apr 2026)
- **Abstract**: Multi-agent system with 7 logical agents for iterative game generation. Features CreativeProxyReward (programmatic signals, not LLM judgment), lineage-scoped memory for cross-version experience accumulation, runtime validation, and mechanic-guided planning loop.
- **Key Innovation**: Interpretable version-to-version evolution with mechanic-aware memory.
- **Link**: https://arxiv.org/abs/2604.19926

---

## 5. Game Benchmarks — Evaluation Suites & Environments

### GameVerse: Can Vision-Language Models Learn from Video-based Reflection?
- **Authors**: Kuan Zhang, Dongchen Liu, Qiyue Zhao et al.
- **Affiliation**: THUSI Lab
- **Venue**: arXiv:2603.06656 (Mar 2026)
- **Abstract**: Comprehensive video game benchmark with reflect-and-retry paradigm. Cognitive hierarchical taxonomy spanning 15 globally popular games. Dual action space (semantic + GUI control). VLMs benefit most from combining failure trajectories + expert tutorials — a training-free analogue to RL + SFT.
- **Key Innovation**: Video-based reflection loop as training-free policy improvement for VLMs.
- **Link**: https://arxiv.org/abs/2603.06656

### HLSMAC: A New StarCraft Multi-Agent Challenge for High-Level Strategic Decision-Making
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2509.12927 (Sep 2025)
- **Abstract**: New cooperative MARL benchmark with 12 StarCraft II scenarios based on classical stratagems from Thirty-Six Stratagems. Covers tactical maneuvering, timing coordination, and deception. Introduces multi-dimensional metrics beyond win rate: ability utilization and advancement efficiency.
- **Key Innovation**: Strategically-grounded benchmark scenarios with richer evaluation metrics.
- **Link**: https://arxiv.org/abs/2509.12927

### MineExplorer: Evaluating Open-World Exploration of MLLM Agents in Minecraft
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2605.30931 (May 2026)
- **Abstract**: Benchmark for evaluating open-world exploration in Minecraft. Filters atomic tasks relying on Minecraft-specific knowledge to better reflect general reasoning. Multi-agent synthesis workflow produces reliable instances (30% higher valid rate than single-agent). 1,497 atomic tasks → 813 composite instances.
- **Key Innovation**: Knowledge-controlled task filtering + multi-hop task composition for exploration evaluation.
- **Link**: https://arxiv.org/abs/2605.30931

### MineNPC-Task: Task Suite for Memory-Aware Minecraft Agents
- **Authors**: Tamil Sudaravan Mohan Doss, Michael Xu, Sudha Rao, Andrew D. Wilson, Balasaravanan Thoravi Kumaravel
- **Affiliation**: —
- **Venue**: arXiv:2601.05215 (Jan 2026)
- **Abstract**: Benchmark for memory-aware, mixed-initiative LLM agents in Minecraft. Tasks elicited from expert co-play. Runs inside Mineflayer envelope (no admin commands/global map). 44 user-authored tasks, 216 subtasks. GPT-4o achieves ~33% subtask failure rate.
- **Key Innovation**: User-authored tasks from real co-play; bounded-knowledge policy prevents evaluation shortcuts.
- **Link**: https://arxiv.org/abs/2601.05215

### PillagerBench: Benchmarking LLM-Based Agents in Competitive Minecraft Team Environments
- **Authors**: Olivier Schipper, Yudi Zhang, Yali Du, Mykola Pechenizkiy, Fang Meng
- **Affiliation**: TU Eindhoven, King's College London, U. Liverpool
- **Venue**: arXiv:2509.06235 (Aug 2025)
- **Abstract**: Framework for evaluating multi-agent systems in real-time competitive team-vs-team Minecraft scenarios. Proposes TactiCrafter, an LLM-based multi-agent system with human-readable tactics, causal dependency learning, and opponent adaptation. Self-play enables adaptive learning.
- **Key Innovation**: Competitive multi-agent benchmark + tactics-based agent with causal learning.
- **Link**: https://arxiv.org/abs/2509.06235

### AgentOdyssey: Open-Ended Long-Horizon Text Game Generation for Test-Time Continual Learning Agents
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2606.24893 (Jun 2026)
- **Abstract**: Game generation engine driven by LLM-based entity and rule synthesis grounded in ontology. Generates unlimited diverse game entities (locations, objects, NPCs) and rules with automatic verification. Multi-faceted metrics: world knowledge, episodic memory, exploration, action diversity, model cost.
- **Key Innovation**: Diagnostic test suite beyond game progress metrics; automatic game soundness verification.
- **Link**: https://arxiv.org/abs/2606.24893

### ODYSSEY: Empowering Minecraft Agents with Open-World Skills
- **Authors**: —
- **Affiliation**: —
- **Venue**: IJCAI 2025
- **Abstract**: LLM-based agent framework with open-world skill library (40 primitive + 183 compositional skills). Fine-tuned LLaMA-3 on 390k+ Minecraft Wiki QA entries. Benchmark with long-term planning, dynamic-immediate planning, and autonomous exploration tasks.
- **Key Innovation**: Comprehensive skill library + structured benchmark for open-world agent capabilities.
- **Link**: https://www.ijcai.org/proceedings/2025/0022.pdf

### OpenHA: Large-Scale Benchmark for Minecraft Agents
- **Authors**: —
- **Affiliation**: —
- **Venue**: OpenReview
- **Abstract**: Large-scale benchmark with 800+ human-verified Minecraft tasks across embodied, GUI, and combat categories. Out-of-distribution evaluation with novel world seeds. Trains from Qwen2-VL-7B on expert trajectories.
- **Key Innovation**: Human-verified task suite with comprehensive action space comparison.
- **Link**: https://openreview.net/pdf?id=tRgXKJqMPg

---

## 6. Industry Game AI — Deployed Systems

### PUBG Ally: Co-Playable Character Powered by NVIDIA ACE (KRAFTON)
- **Authors**: KRAFTON / NVIDIA
- **Affiliation**: **KRAFTON, NVIDIA**
- **Venue**: Product launch (Jun 2026)
- **Abstract**: Co-playable character for PUBG: BATTLEGROUNDS. Combines on-device ASR, 2B SLM (Mistral-NeMo-Minitron quantized to 8GB VRAM), and TTS via NVIDIA ACE. Behavior-tree layer handles reflex-level combat. All local inference — no cloud LLM. English, Korean, Chinese support.
- **Key Innovation**: On-device deployment with strict latency constraints; model is not trusted to invent facts — re-observes world each turn.
- **Link**: https://gamedev.net/news/how-krafton-built-pubg-ally-a-co-playable-character-powered-by-nvidia-ace-r4114/

### Augmenting Game AI with Deep Reinforcement Learning
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2606.20210 (Jun 2026)
- **Abstract**: Practical guide for deploying RL-augmented game AI in production. Covers runtime inference constraints (on-device/server), model efficiency, retraining during game development cycles, asymmetric actor-critic architectures, and deployment considerations (GPU/CPU, ONNX/TensorRT).
- **Key Innovation**: Comprehensive deployment framework for RL in commercial games.
- **Link**: https://arxiv.org/abs/2606.20210

### OpenGame: Open Agentic Coding for Games
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2604.18394 (Apr 2026)
- **Abstract**: Open-source agentic framework for end-to-end web game creation. GameCoder-27B (Qwen3.5-27B) trained through CPT + SFT + execution-grounded RL for multi-file game code generation. OpenGame-Bench measures build health, visual usability, intent alignment.
- **Key Innovation**: Domain-specialized code model with RL from execution feedback for game development.
- **Link**: https://arxiv.org/abs/2604.18394

### High-Quality Generation of Dynamic Game Content via Small Language Models
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2601.23206 (May 2026)
- **Abstract**: Argues for SLM over cloud LLM for game content generation. Demonstrates retry-until-success strategy with fine-tuned SLM reaches adequate quality with predictable latency. DAG-based synthetic training data. Minimal RPG loop powered by single specialized SLM as proof of concept.
- **Key Innovation**: Practical local deployment strategy for LLM-based game content; addresses latency/cost barriers.
- **Link**: https://arxiv.org/abs/2601.23206

---

## 7. Related Techniques

### SPA: Internalizing World Models via Self-Play Finetuning for Agentic RL
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2510.15047 (Oct 2025)
- **Abstract**: Self-play finetuning framework that decomposes world modeling into state representation and transition dynamics. Improves exploration before exploitation: self-play explores state and action space instead of overfitting to first successful trajectory. Raises Pass@k metrics.
- **Key Innovation**: World model internalization through self-play as alternative to reward shaping.
- **Link**: https://arxiv.org/abs/2510.15047

### SeRL: Self-Play Reinforcement Learning for LLMs with Limited Data
- **Authors**: Wenkai Fang, Shunyu Liu, Zhou Yang et al.
- **Affiliation**: —
- **Venue**: arXiv:2505.20347 (May 2025)
- **Abstract**: Self-play RL bootstrapping LLM training with limited initial data. Two modules: self-instruction (generates additional instructions with online filtering) and self-rewarding (majority-voting for reward estimation). Matches performance of high-quality data with verifiable rewards.
- **Key Innovation**: Self-contained RL loop without external annotations or verifiable reward functions.
- **Link**: https://arxiv.org/abs/2505.20347

### ProPlay: Procedural World Models for Self-Evolving LLM Agents
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2606.12780 (Jun 2026)
- **Abstract**: Represents environment knowledge as procedure graph with nodes (procedures) and directed edges (transitions with reliability records). Performs procedure-level preplay before each episode — reasons over task, graph, reliabilities, and failure experience. Trajectory injected as soft guidance, not hard constraint.
- **Key Innovation**: Procedural world model with reliability-weighted experience reuse.
- **Link**: https://arxiv.org/abs/2606.12780

### SPEAR: Self-Imitation with Progressive Exploration for Agentic RL
- **Authors**: Yanhui Qin, Xiaoyu Tan, Zhini He et al.
- **Affiliation**: —
- **Venue**: arXiv:2509.22601 (Sep 2025)
- **Abstract**: Self-imitation learning recipe for agentic LLMs. Stages curriculum scheduling harmonizing intrinsic reward shaping and self-imitation: (1) expedite exploration via tool interactions, (2) strengthen exploitation upon convergence. Boosts GRPO/GiGPO/Dr.BoT success rates by up to 16.1%/5.1%/8.6% on ALFWorld and WebShop.
- **Key Innovation**: Progressive exploration-exploitation curriculum for agentic RL.
- **Link**: https://arxiv.org/abs/2509.22601

### π-Play: Multi-Agent Self-Play via Privileged Self-Distillation without External Data
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2604.14054 (Apr 2026)
- **Abstract**: Self-play naturally produces question construction paths (QCP) — intermediate artifacts capturing reverse solution process. Uses QCP as privileged information for teacher model to densely supervise student via self-distillation. Transforms sparse-reward self-play into dense-feedback loop.
- **Key Innovation**: Leverages self-play's intrinsic QCP artifacts for dense supervision without human feedback.
- **Link**: https://arxiv.org/abs/2604.14054

### WorldLLM: Improving LLMs' World Modeling using Curiosity-Driven Theory-Making
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2506.06725 (Jun 2025)
- **Abstract**: Combines probabilistic theory induction (Bayesian hypothesis generation) with curiosity-driven RL exploration. LLM's world model is conditional probability over states given hypotheses. Demonstrated in video game environment with object manipulation.
- **Key Innovation**: Scientific discovery cycle for LLM world models — hypotheses guide exploration, exploration refines hypotheses.
- **Link**: https://arxiv.org/abs/2506.06725

### SIPP: Self-Imitating Proximal Policy Optimization (Match or Replay)
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2603.27515 (Mar 2026)
- **Abstract**: On-policy RL that seamlessly integrates self-imitation into PPO without replay buffers or off-policy corrections. Two strategies: MATCH (state-action pairs for dense reward) and REPLAY (trajectory-level for sparse/binary reward). Handles partial observability (Animal-AI Olympics).
- **Key Innovation**: Preserves PPO's stability guarantees while adding self-imitation exploration.
- **Link**: https://arxiv.org/abs/2603.27515

### CuES: Curiosity-Driven and Environment-Grounded Synthesis for Agentic RL
- **Authors**: Sandra Mai, Yunkai Zhai, Ziqian Chen et al.
- **Affiliation**: —
- **Venue**: arXiv:2512.01311 (Dec 2025)
- **Abstract**: Formalizes task generation for agentic RL. CuES drives exploration via intrinsic curiosity, abstracts interaction patterns into task schemas, refines through memory-based quality control. Evaluated on AppWorld, BFCL, WebShop — matches/surpasses manually curated datasets.
- **Key Innovation**: Autonomous task discovery without handcrafted seeds or external corpora.
- **Link**: https://arxiv.org/abs/2512.01311

### Provable Zero-Shot Generalization in Offline Reinforcement Learning
- **Authors**: —
- **Affiliation**: —
- **Venue**: ICML 2025 (PMLR 267:65122–65143)
- **Abstract**: Studies offline RL with zero-shot generalization (ZSG) across environments. Proposes PERM and PPPO using pessimistic policy evaluation. First theoretical result showing near-optimal ZSG guarantees for offline RL. Sub-optimality bounded by supervised learning error + RL coverage error.
- **Key Innovation**: First provable guarantees for ZSG in offline RL; pessimism principle for generalization.
- **Link**: https://proceedings.mlr.press/v267/wang25dx.html

### Generative Evolutionary Meta-Solver (GEMS): Scalable Surrogate-Free MARL
- **Authors**: Arun Sharma, Gaurav Trivedi, K Bhandari et al.
- **Affiliation**: —
- **Venue**: arXiv:2509.23462 (Sep 2025)
- **Abstract**: Surrogate-free MARL replacing explicit policy populations with compact latent anchors and amortized generator. Empirical-Bernstein UCB oracle for adaptive policy expansion. Up to 6× faster, 1.3× less memory than PSRO. Evaluated on Kuhn Poker, Deceptive Messages, Multi-Particle.
- **Key Innovation**: Eliminates quadratic payoff matrix construction from PSRO-style methods.
- **Link**: https://arxiv.org/abs/2509.23462

### MixExpert: Bringing Human Thoughts Back to the Game of Go
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2601.16447 (Jan 2026)
- **Abstract**: Fine-tunes general LLMs (Qwen2.5-7B/32B, DeepSeek-R1-Distill) on Go via GRPO. Achieves professional-level performance through self-exploration. Maintains general reasoning (math, code) unlike specialized AlphaGo. First general LLM to reach expert Go level.
- **Key Innovation**: Domain-specific GRPO preserves general capabilities; identifies cold-start necessity.
- **Link**: https://arxiv.org/abs/2601.16447

### Look-ahead Reasoning with a Learned Model in Imperfect Information Games (LAMIR)
- **Authors**: Ondřej Kubíček, Viliam Lisý
- **Affiliation**: —
- **Venue**: arXiv:2510.05048 (Oct 2025)
- **Abstract**: Enables look-ahead reasoning in two-player imperfect information games using learned abstract model — no explicit game rules needed. Trains domain-independent abstractions concurrently with model. Up to 80% win rate in large games vs RNaD baseline.
- **Key Innovation**: First algorithm enabling look-ahead reasoning in large-scale imperfect information games without domain-specific knowledge.
- **Link**: https://arxiv.org/abs/2510.05048

### Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2604.08995 (Apr 2026)
- **Abstract**: Memory-augmented interactive world model for 720p real-time long-form video generation. Industrial-scale data engine with Unreal Engine synthetic data + AAA game collection + real-world video. Camera-aware memory retrieval. Multi-segment DMD distillation enables 40 FPS at 720p with 5B model.
- **Key Innovation**: Real-time interactive world model at 720p with minute-long memory consistency.
- **Link**: https://arxiv.org/abs/2604.08995

### Learning Game-Playing Agents with Generative Code Optimization
- **Authors**: Zhiyi Kuang, Ryan Rong, YuCheng Yuan, Allen Nie
- **Affiliation**: —
- **Venue**: arXiv:2508.19506 (Aug 2025)
- **Abstract**: Policies represented as Python programs refined by LLMs. Agents self-improve through execution traces and natural language feedback. Competitive with deep RL baselines on Atari while using significantly less training time and fewer environment interactions.
- **Key Innovation**: Programmatic policy representation with LLM-based self-evolution.
- **Link**: https://arxiv.org/abs/2508.19506

---

## Summary Statistics

| Category | Count | Key Venues |
|----------|-------|-----------|
| Game RL | 9 | CVPR 2026, ACL 2026, NeurIPS/ICML ecosystem |
| Game AI Bot | 7 | ACL 2026 Findings, multiple arXiv |
| Game Foundation Models | 9 | CVPR 2026, multiple arXiv |
| Procedural Content Generation | 9 | Multiple arXiv |
| Game Benchmarks | 8 | IJCAI 2025, multiple arXiv |
| Industry Game AI | 4 | KRAFTON/NVIDIA, multiple arXiv |
| Related Techniques | 14 | ICML 2025, multiple arXiv |
| **Total** | **60** | — |

### Key Themes
1. **Convergence of VLM + RL**: Odysseus, NitroGen, Game-TARS all show VLM+RL for gameplay is now mainstream
2. **Generalist game agents are here**: NitroGen (CVPR 2026), Game-TARS, Pixels2Play demonstrate cross-game generalization from pixel inputs
3. **Industry deployment maturing**: PUBG Ally (KRAFTON/NVIDIA) proves on-device compact SLM viable for real-time game AI
4. **Self-play for reasoning**: SPIRAL and kin show zero-sum games improve LLM reasoning beyond game contexts
5. **World models becoming real-time**: Matrix-Game 3.0 achieves 720p 40 FPS interactive world generation
6. **MARL foundation model**: MARL-GPT suggests transformer-based multi-task MARL is possible
7. **Procedural generation goes multi-modal**: Text, sketch, and language-instructed PCG maturing via RL+contrastive learning
