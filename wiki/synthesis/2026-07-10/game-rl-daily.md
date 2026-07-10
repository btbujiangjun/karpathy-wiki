---
title: "Game RL & Game AI Bot — Daily Digest (2026-07-10)"
type: synthesis
created: 2026-07-10
updated: 2026-07-10
tags: [game-rl, game-ai, self-play, multi-agent, foundation-model, world-model, pcg, benchmark, industry]
sources: []
---

# Game RL & Game AI Bot — Daily Digest

> Compiled 2026-07-10 from arXiv, CVPR 2026, ICLR 2026, SBGames 2025, NVIDIA Technical Blog. Covers Game RL, Game AI Bots, Foundation Models, PCG, Benchmarks, Industry Game AI, World Models, and Related Techniques.

---

## 1. Game RL — Self-Play & Board Games

### QZero: Mastering the Game of Go with Self-play Experience Replay
- **Authors**: Jingbin Liu, Xuechun Wang
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Jan 2026
- **Abstract**: Presents QZero, a model-free RL algorithm that forgoes MCTS during training and learns a Nash equilibrium policy through self-play and off-policy experience replay. Built on entropy-regularized Q-learning with a single Q-value network. Trained tabula rasa on 7 GPUs for 5 months, achieves performance comparable to AlphaGo.
- **Key Innovation**: First demonstration that model-free off-policy RL can master Go at scale.
- **Link**: [arXiv:2601.03306](https://arxiv.org/abs/2601.03306)

### Regret-Guided Search Control (RGSC) for AlphaZero
- **Authors**: N/A
- **Affiliation**: N/A
- **Venue**: ICLR 2026
- **Abstract**: Extends AlphaZero with a regret network that identifies high-regret states where the agent's evaluation diverges most from actual outcomes. Uses a prioritized regret buffer to restart self-play from these states. Outperforms AlphaZero and Go-Exploit by avg 77 and 89 Elo across 9x9 Go, 10x10 Othello, 11x11 Hex. Improves win rate against KataGo from 69.3% to 78.2%.
- **Key Innovation**: Learned regret-guided search control for efficient self-play.
- **Link**: [arXiv:2602.20809](https://arxiv.org/abs/2602.20809)

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning
- **Authors**: Lei Zhu, Lutz Güertler, Simon C.H. Yu, Zichen Liu, Penghui Qi, Daniel Balcells, et al.
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Jun 2025
- **Abstract**: Self-play framework where LLMs learn by playing multi-turn zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation) against continuously improving versions of themselves. Introduces role-conditioned advantage estimation (RAE). Improves performance up to 10% across 8 reasoning benchmarks on Qwen and Llama families.
- **Key Innovation**: Online multi-agent multi-turn RL system for LLMs with automatic curriculum via self-play.
- **Link**: [arXiv:2506.24119](https://arxiv.org/abs/2506.24119)

### Reproducing AlphaZero on Tablut: Self-Play RL for an Asymmetric Board Game
- **Authors**: N/A
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Apr 2026
- **Abstract**: Adapts AlphaZero to Tablut, an asymmetric board game with unequal piece counts and distinct player objectives. Uses separate policy/value heads per player role with shared residual trunk. Mitigates catastrophic forgetting via C4 augmentation, larger replay buffer, and sampling past checkpoints.
- **Key Innovation**: Modified AlphaZero architecture for asymmetric games with stabilization techniques.
- **Link**: [arXiv:2604.05476](https://arxiv.org/abs/2604.05476)

### Superhuman AI for Generals.io Using Self-Play Reinforcement Learning
- **Authors**: Matěj Straka, Viliam Lisý, Martin Schmid
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Jun 2026
- **Abstract**: Superhuman agent for Generals.io (real-time strategy game under imperfect information). Trained on 4x H200 GPUs for 4 days. Uses JAX-native simulator achieving tens of millions of FPS (10,000x speedup). Vision Transformer policy with policy-gradient, top-advantage sample filtering, and EMA policy parameters.
- **Key Innovation**: Extreme simulator speed enabling rapid self-play; reaches #1 on 5,000+ player leaderboard.
- **Link**: [arXiv:2606.23348](https://arxiv.org/abs/2606.23348)

---

## 2. Game RL — Multi-Agent & Foundation Models for MARL

### MARL-GPT: Foundation Model for Multi-Agent Reinforcement Learning
- **Authors**: N/A
- **Affiliation**: Cognitive AI Systems
- **Venue**: arXiv preprint, Apr 2026
- **Abstract**: Single GPT-based model trained via offline RL on expert trajectories (400M SMACv2 + 100M GRF + 1B POGEMA) achieves competitive performance across diverse MARL environments. Uses transformer observation encoder requiring no task-specific tuning.
- **Key Innovation**: First multi-task transformer-based foundation model for diverse multi-agent problems.
- **Link**: [arXiv:2604.05943](https://arxiv.org/abs/2604.05943)

### MARSHAL: Incentivizing Multi-Agent Reasoning via Self-Play with Strategic LLMs
- **Authors**: Hui Yuan, Zhe Xu, Zhen Tan, Xianhao Yi, Guang Mo, Kaiwen Long, et al.
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Oct 2025
- **Abstract**: End-to-end RL framework for multi-turn multi-agent scenarios. Features turn-level advantage estimator and agent-specific advantage normalization. Qwen3-4B agents achieve up to 28.7% improvement in held-out games; generalizes to reasoning benchmarks (AIME +10%, GPQA-Diamond +7.6%).
- **Key Innovation**: Self-play in strategic games as a generalizable approach for multi-agent reasoning.
- **Link**: [arXiv:2510.15414](https://arxiv.org/abs/2510.15414)

### π-Play: Multi-Agent Self-Play via Privileged Self-Distillation
- **Authors**: Yaocheng Zhang, Yuanheng Zhu, Wenyue Chong, Songjun Tu, Qichao Zhang, Jiajun Chai, et al.
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Apr 2026
- **Abstract**: Combines self-play and self-distillation where an examiner generates tasks with question construction paths (QCPs), and a teacher uses QCP as privileged context for dense supervision. Transforms sparse-reward self-play into dense-feedback co-evolution.
- **Key Innovation**: Privileged information from self-play enables data-free training surpassing supervised search agents.
- **Link**: [arXiv:2604.14054](https://arxiv.org/abs/2604.14054)

### SAGE: Multi-Agent Self-Evolution for LLM Reasoning
- **Authors**: Yulin Peng, Xinxin Zhu, Chenxing Wei, Nianbo Zeng, Leilei Wang, Yong He, et al.
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Mar 2026
- **Abstract**: Closed-loop framework with 4 agents (Challenger, Planner, Solver, Critic) co-evolving from a shared LLM backbone. Challenger generates increasingly difficult tasks; Critic prevents curriculum drift. Qwen-2.5-7B improves 8.9% on LiveCodeBench and 10.7% on OlympiadBench.
- **Key Innovation**: Multi-agent self-evolution with explicit planning and quality control for reasoning.
- **Link**: [arXiv:2603.15255](https://arxiv.org/abs/2603.15255)

### OpenSIR: Open-Ended Self-Improving Reasoner
- **Authors**: N/A
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Nov 2025
- **Abstract**: Self-play framework where a single LLM alternates teacher/student roles to generate and solve novel problems without external verifiers. Uses diversity rewards and difficulty calibration. Improves all models avg +3.6 on instruction models and +3.1 on reasoning models across 7 math benchmarks.
- **Key Innovation**: Open-ended discovery via diversity rewards; surpasses GRPO baselines trained on 7K+ examples starting from single trivial seed.
- **Link**: [arXiv:2511.00602](https://arxiv.org/abs/2511.00602)

---

## 3. Game RL — Atari & Video Game RL

### Learning Game-Playing Agents with Generative Code Optimization
- **Authors**: Zhiyi Kuang, Ryan Rong, YuCheng Yuan, Allen Nie
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Aug 2025
- **Abstract**: Policies represented as Python programs and refined using LLMs. Self-evolving code with current observation as input, action as output. Achieves competitive performance with deep RL on Atari while using significantly less training time and environment interactions.
- **Key Innovation**: Programmatic policy representations for efficient, adaptable agents.
- **Link**: [arXiv:2508.19506](https://arxiv.org/abs/2508.19506)

### Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL
- **Authors**: N/A
- **Affiliation**: N/A
- **Venue**: arXiv preprint, May 2026
- **Abstract**: Studies RL-based training of VLMs for long-horizon decision-making in Super Mario Land (100+ turns). Adapts PPO with lightweight turn-level critic, substantially improving over GRPO/Reinforce++. Pretrained VLMs provide strong action priors. Achieves 3x average game progress over frontier models.
- **Key Innovation**: Open training framework for VLM agents with stable RL in long-horizon multi-modal settings.
- **Link**: [arXiv:2605.00347](https://arxiv.org/abs/2605.00347)

### The Latent Bridge: A Continuous Slow-Fast Channel for Real-Time Game Agents
- **Authors**: Bojie Li, Noah Shi
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Jun 2026
- **Abstract**: Couples two frozen VLMs (9B reactive, 8B reasoning) with a learned continuous Latent Bridge projecting slow model residuals into fast model's embedding space. On 7 Atari games + MetaDrive, matches/beats Text Bridge in every domain (MsPacman +57%, RoadRunner +28%).
- **Key Innovation**: Learned latent channel between slow reasoning and fast reactive models for real-time game agents.
- **Link**: [arXiv:2606.24470](https://arxiv.org/abs/2606.24470)

---

## 4. Game AI Bots & NPC Intelligence

### Reflection of Episodes (ROE) — LLM Game Agent for StarCraft II
- **Authors**: N/A
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Feb 2025
- **Abstract**: Framework using keyframe selection and reflection on expert/self-experience for LLM decision-making in TextStarCraft II. After each game, LLM reflects to generate new self-experience. Beats Very Hard difficulty bots with 20% win rate.
- **Key Innovation**: Strategy iteration via reflection of episodes for LLM-based StarCraft II agents.
- **Link**: [arXiv:2502.13388](https://arxiv.org/abs/2502.13388)

### HER: Human-like Reasoning and Reinforcement Learning for LLM Role-playing
- **Authors**: Chengyu Du, Xintao Wang, Aili Chen, Weiyuan Li, Rui Xu, Junteng Liu, et al.
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Jan 2026
- **Abstract**: Unified framework for cognitive-level persona simulation. Introduces dual-layer thinking (first-person vs third-person). Uses reverse-engineered reasoning data and human-aligned reward models. Trained on Qwen3-32B via SFT+RL. +30.26% on CoSER, +14.97% on Minimax Role-Play Bench.
- **Key Innovation**: Distinguishes character's internal thoughts from LLM's planning for realistic role-play.
- **Link**: [arXiv:2601.21459](https://arxiv.org/abs/2601.21459)

### Character-R1: Enhancing Role-Aware Reasoning in RPAs via RLVR
- **Authors**: Yihong Tang, Kehai Chen, Xuefeng Bai, Benyou Wang, Zeming Liu, Haifeng Wang, et al.
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Jan 2026
- **Abstract**: RLVR framework with three reward designs: Cognitive Focus Reward (enforces analysis of 10 character elements), Reference-Guided Reward, and Character-Conditioned Reward Normalization. Significantly outperforms existing methods on CharacterBench.
- **Key Innovation**: Verifiable reward signals for role-playing agents via explicit cognitive modeling.
- **Link**: [arXiv:2601.04611](https://arxiv.org/abs/2601.04611)

### Bounded Autonomy: Controlling LLM Characters in Live Multiplayer Games
- **Authors**: N/A
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Apr 2026
- **Abstract**: Studies control mechanisms for LLM-driven characters in live multiplayer game settings.
- **Key Innovation**: Bounded autonomy framework for LLM NPCs in multiplayer contexts.
- **Link**: [arXiv:2604.04703](https://arxiv.org/abs/2604.04703)

### Nemobot Games: Strategic AI Gaming Agents with LLMs
- **Authors**: N/A
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Apr 2026
- **Abstract**: Extends Shannon's taxonomy of game-playing machines using LLMs. Interactive environment for creating/deploying LLM-powered game agents across dictionary-based, solvable, heuristic-based, and learning-based game classes.
- **Key Innovation**: Programmable framework operationalizing Shannon's taxonomy with modern LLMs.
- **Link**: [arXiv:2604.21896](https://arxiv.org/abs/2604.21896)

### AdaMARP: Adaptive Multi-Agent Interaction Framework for Immersive Role-Playing
- **Authors**: Zhenhua Xu, Dongsheng Chen, Shuo Wang, Jian Li, Chengjie Wang, Meng Han, et al.
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Jan 2026
- **Abstract**: Adaptive multi-agent framework for general immersive role-playing.
- **Link**: [arXiv:2601.11007](https://arxiv.org/abs/2601.11007)

### Sensi: Curriculum-Based Test-Time Learning for LLM Game Agents
- **Authors**: Mohsen Arjmandi
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Mar 2026
- **Abstract**: Curriculum-based approach enabling LLM game agents to learn one thing at a time during test time.
- **Link**: [arXiv:2603.17683](https://arxiv.org/abs/2603.17683)

---

## 5. Game Foundation Models

### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi "Jim" Fan
- **Affiliation**: NVIDIA, MineDojo
- **Venue**: CVPR 2026
- **Abstract**: Vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games. Uses internet-scale video-action dataset with automatically extracted player actions. Unified vision-action model with large-scale behavior cloning. Up to 52% relative improvement on unseen games. Dataset, evaluation suite, and weights released.
- **Key Innovation**: First open foundation model for generalist gaming agents at scale.
- **Link**: [arXiv:2601.02427](https://arxiv.org/abs/2601.02427) | [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Magne_NitroGen_An_Open_Foundation_Model_for_Generalist_Gaming_Agents_CVPR_2026_paper.html)

### Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents
- **Authors**: Zihao Wang, Xujing Li, Yining Ye, Junjie Fang, Haoming Wang, Longxiang Liu, et al.
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Oct 2025
- **Abstract**: Generalist game agent with unified scalable action space anchored to native keyboard-mouse inputs. Pre-trained on 500B+ tokens across OS, web, and simulation games. Decaying continual loss and Sparse-Thinking strategy. ~2x success rate over SOTA on Minecraft, close to fresh humans on unseen 3D web games, outperforms GPT-5 on FPS.
- **Key Innovation**: Unified action space enabling large-scale continual pre-training across heterogeneous domains.
- **Link**: [arXiv:2510.23691](https://arxiv.org/abs/2510.23691)

### Pixels2Play: A Foundation Model for 3D Gameplay
- **Authors**: Yuguang Yue, Chris Green, Samuel Hunt, Irakli Salia, Wenzhe Shi, Jonathan J. Hunt
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Aug 2025
- **Abstract**: Foundation model for 3D video games trained end-to-end via behavior cloning on instrumented human gameplay + unlabeled public videos (actions imputed via inverse dynamics). Decoder-only transformer with autoregressive action output. Real-time on consumer GPU.
- **Key Innovation**: Combines labeled demonstrations with unlabeled public videos via inverse dynamics for scalable game policy learning.
- **Link**: [arXiv:2508.14295](https://arxiv.org/abs/2508.14295)

### Pixels2Play (Scaling Behavior Cloning) — Open Recipe
- **Authors**: Yuguang Yue, Irakli Salia, Samuel Hunt, Chris Green, Wenzhe Shi, Jonathan J. Hunt
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Jan 2026
- **Abstract**: Open recipe for video game playing foundation model for real-time inference on consumer GPU. Releases 8,300+ hours of labeled gameplay, code, and checkpoints. Studies scaling laws of behavior cloning up to 1.2B parameters. Shows larger/deeper models learn more causal policies.
- **Key Innovation**: Systematic study of scaling laws and causal reasoning in behavior-cloned game policies.
- **Link**: [arXiv:2601.04575](https://arxiv.org/abs/2601.04575)

### Lumine: An Open Recipe for Building Generalist Agents in 3D Open Worlds
- **Authors**: Weihao Tan, et al.
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Nov 2025 (Hugging Face papers)
- **Abstract**: VLM-based agent for completing hours-long complex missions in 3D open worlds. Processes raw pixels at 5 Hz to produce 30 Hz actions. Trained in Genshin Impact; completes entire 5-hour Mondstadt storyline at human-level efficiency. Zero-shot cross-game generalization to Wuthering Waves and Honkai: Star Rail.
- **Key Innovation**: First open recipe for generalist agents in 3D open worlds with zero-shot cross-game generalization.
- **Link**: [arXiv:2511.08892](https://arxiv.org/abs/2511.08892)

### GameVerse: Can VLMs Learn from Video-based Reflection?
- **Authors**: Kuan Zhang, Dongchen Liu, Qiyue Zhao, Jinkun Hou, Xinran Zhang, Qinlei Xie, et al.
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Mar 2026
- **Abstract**: Benchmark enabling reflective visual interaction loop for VLMs. Uses "reflect-and-retry" paradigm with cognitive hierarchical taxonomy spanning 15 games. VLMs benefit from combining failure trajectories and expert tutorials — a training-free analogue to RL+SFT.
- **Key Innovation**: Video-based reflection as a training-free improvement mechanism for VLM game agents.
- **Link**: [arXiv:2603.06656](https://arxiv.org/abs/2603.06656)

### Towards Generalist Game Players: Foundation Models in the Game Multiverse
- **Authors**: Kuan Zhang, Dongchen Liu, Qiyue Zhao, Tianyu Xin, Yue Su, Haisheng Wang, et al.
- **Affiliation**: N/A
- **Venue**: arXiv preprint, May 2026
- **Abstract**: Survey tracing four eras of game AI: symbolic/RL agents → foundation models as generalist players → future creator stage. Maps five fundamental trade-offs. Proposes five-level roadmap from single-game mastery to ultimate creator stage.
- **Key Innovation**: Unified lens and roadmap for generalist game agents toward AGI.
- **Link**: [arXiv:2605.09965](https://arxiv.org/abs/2605.09965)

---

## 6. Procedural Content Generation (PCG)

### IPCGRL: Language-Instructed Reinforcement Learning for Procedural Level Generation
- **Authors**: In-Chang Baek, Sunghyun Kim, Seo-Young Lee, Dong-Hyeon Kim, Kyung-Joong Kim
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Mar 2025
- **Abstract**: Instruction-based PCG via RL incorporating sentence embedding model. Fine-tunes task-specific embeddings to compress game-level conditions. Up to 21.4% improvement in controllability and 17.2% in generalizability for unseen instructions on 2D level generation.
- **Key Innovation**: Language instructions for controllable PCG via RL with learned task-specific embeddings.
- **Link**: [arXiv:2503.12358](https://arxiv.org/abs/2503.12358)

### PCGRLLM: Large Language Model-Driven Reward Design for PCGRL
- **Authors**: In-Chang Baek, Sunghyun Kim, Sam Earle, Zehua Jiang, Noh Jin-Ha, Julian Togelius, et al.
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Feb 2025
- **Abstract**: Uses LLMs to generate reward functions for RL-based content generators. Employs feedback mechanism and reasoning-based prompt engineering. 415% and 40% performance improvements depending on LLM zero-shot capabilities.
- **Key Innovation**: LLM-automated reward design for procedural content generation RL.
- **Link**: [arXiv:2502.10906](https://arxiv.org/abs/2502.10906)

### CreativeGame: Toward Mechanic-Aware Creative Game Generation
- **Authors**: Hongnan Ma, Han Wang, Shenglin Wang, Tieyue Yin, Yiwei Shi, Yucong Huang, et al.
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Apr 2026
- **Abstract**: Multi-agent system for iterative HTML5 game generation with proxy rewards, lineage-scoped memory, runtime validation, and mechanic-guided planning. 71 lineages, 88 nodes, 774-entry mechanic archive.
- **Key Innovation**: Mechanic-aware iterative game generation with explicit mechanic planning and evolution tracking.
- **Link**: [arXiv:2604.19926](https://arxiv.org/abs/2604.19926)

### A Database-Driven Framework for 3D Level Generation with LLMs
- **Authors**: Kaijie Xu, Clark Verbrugge
- **Affiliation**: McGill University
- **Venue**: arXiv preprint, Aug 2025
- **Abstract**: Multi-phase pipeline using LLM-assisted construction of reusable databases for architectural components and gameplay mechanics. Two-phase repair system ensures navigability. Validated on diverse 3D environments.
- **Key Innovation**: Database-centric framework combining modular design with constraint-based optimization for 3D level generation.
- **Link**: [arXiv:2508.18533](https://arxiv.org/abs/2508.18533)

### PCGRL+: Scaling, Control and Generalization in RL Level Generators
- **Authors**: Sam Earle, Zehua Jiang, Julian Togelius
- **Affiliation**: New York University
- **Venue**: arXiv preprint, Aug 2024 (updated)
- **Abstract**: PCGRL environments in JAX for GPU-parallel simulation (15x speedup). Randomizes level sizes and uses "pinpoints" to counter overfitting. Partial observations produce better generalization to larger maps. Trained for 1B timesteps.
- **Key Innovation**: JAX-native PCGRL with randomized levels and partial observations for scalable controllable generation.
- **Link**: [arXiv:2408.12525](https://arxiv.org/abs/2408.12525)

### Customizable Procedural Content Generation with LLMs
- **Authors**: Marcelo Júnior, Mario Adaniya, Luiz Nunes
- **Affiliation**: Brazil
- **Venue**: SBGames 2025
- **Abstract**: Fine-tunes DeepSeek-R1-Distill-Llama-8B to generate customizable Zelda-like 2D game levels. Achieves high novelty, diversity, and playability with strong input adherence.
- **Key Innovation**: Instruction-tuned LLM for controllable game level generation with quantifiable metrics.
- **Link**: [SBGames 2025](https://sol.sbc.org.br/index.php/sbgames/article/view/37377) | DOI: 10.5753/sbgames.2025.10297

---

## 7. Game Benchmarks

### OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents
- **Authors**: Mingxian Lin, Shengju Qian, Yuqi Liu, Yi-Hua Huang, Yiyu Wang, Wei Huang, et al.
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Jun 2026
- **Abstract**: Real-time benchmark of 12 Unreal Engine 5 games (Solo, PvP, Coop). Introduces Improvement Dynamics Curve (IDC) — tool-using reflector LLM refines skill prompts across multiple rounds, measuring score evolution. Evaluates 12 VLM agents.
- **Key Innovation**: Multi-game UE5 benchmark with reflection-based improvement measurement.
- **Link**: [arXiv:2606.09826](https://arxiv.org/abs/2606.09826) | [GitHub](https://github.com/mxlin043/OmniGameArena)

### GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents
- **Authors**: Mingyu Ouyang, Siyuan Hu, Kevin Qinghong Lin, Hwee Tou Ng, Mike Zheng Shou
- **Affiliation**: NUS
- **Venue**: arXiv preprint, Apr 2026
- **Abstract**: Benchmarks multimodal game agents across 34 browser-based games and 170 tasks. Uses outcome-based, state-verifiable evaluation.
- **Key Innovation**: Large-scale standardized benchmark with verifiable task completion metrics.
- **Link**: [arXiv:2604.07429](https://arxiv.org/abs/2604.07429) | [GitHub](https://github.com/gameworld-project/gameworld)

### VideoGameBench: Can VLMs Complete Popular Video Games?
- **Authors**: Alex L. Zhang, Thomas L. Griffiths, Karthik R. Narasimhan, Ofir Press
- **Affiliation**: Princeton
- **Venue**: arXiv preprint, May 2025
- **Abstract**: Benchmark of 10 popular 1990s video games (Game Boy + DOS). VLMs interact in real-time with raw visual inputs. Best models (Gemini 2.5 Pro, Claude 3.7) complete only 0.48% of games. Introduces VideoGameBench Lite (turn-based) where best reaches 1.6%.
- **Key Innovation**: Direct VLM evaluation on complete game completion; reveals massive gap between VLMs and human gameplay.
- **Link**: [arXiv:2505.18134](https://arxiv.org/abs/2505.18134)

### Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games
- **Authors**: Dongmin Park, Minkyu Kim, Beongjun Choi, Junhyuck Kim, Keon Lee, Jonghyun Lee, et al.
- **Affiliation**: KRAFTON AI
- **Venue**: arXiv preprint, Jun 2025
- **Abstract**: 12 popular video games spanning all major genres. MCP-based plug-and-play interface for LLM/game connection. Extensive analysis of visual input, agentic strategies, and fine-tuning effects. Includes fine-tuning dataset from expert LLM trajectories.
- **Key Innovation**: Foundational benchmark with MCP integration for plug-and-play LLM agent evaluation across diverse genres.
- **Link**: [arXiv:2506.03610](https://arxiv.org/abs/2506.03610) | [GitHub](https://github.com/krafton-ai/ORAK)

### AI Gamestore: Scalable, Open-Ended Evaluation of Machine General Intelligence
- **Authors**: Lance Ying, Ryan Truong, Prafull Sharma, Kun Zhao, Nathan Cloos, Kelsey R. Allen, et al.
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Feb 2026
- **Abstract**: Platform using LLMs with humans-in-the-loop to synthesize new games from App Store/Steam top charts. Generated 100 games; evaluated 7 frontier VLMs. Best models achieve <10% of human average score. Tests world-model learning, memory, and planning.
- **Key Innovation**: Living benchmark continually generating new human games to prevent saturation.
- **Link**: [arXiv:2602.17594](https://arxiv.org/abs/2602.17594)

### AgentOdyssey: Open-Ended Long-Horizon Text Game Generation for Test-Time Continual Learning Agents
- **Authors**: N/A
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Jun 2026
- **Abstract**: Framework procedurally generating open-ended text games with rich entities, world dynamics, and long-horizon tasks. Multifaceted evaluation: world knowledge acquisition, episodic memory, exploration, action diversity. Even top agents remain far below human.
- **Key Innovation**: Diagnostic benchmark for test-time continual learning in procedurally generated text games.
- **Link**: [arXiv:2606.24893](https://arxiv.org/abs/2606.24893)

---

## 8. Industry Game AI

### NVIDIA ACE Game Agent SDK (Beta)
- **Affiliation**: NVIDIA
- **Venue**: Unreal Fest 2026 (Jun 2026)
- **Summary**: Lightweight open-source C/C++ framework with Agent, Chat, and RAG APIs for building on-device AI NPCs. Used in PUBG: BATTLEGROUNDS (AI teammate "Ally") and Total War: PHARAOH (AI advisor with RAG on 1,200+ game data tables). New UE5 plugins for ASR, SLM (Qwen 3.5 4B), and TTS (Chatterbox Turbo 350M). All optimized for local RTX hardware.
- **Key Innovation**: Production-grade on-device AI NPC framework with full speech-intelligence-animation pipeline.
- **Link**: [NVIDIA Technical Blog](https://developer.nvidia.com/blog/build-on-device-ai-companions-with-the-nvidia-ace-game-agent-sdk-and-unreal-engine-5-plugins/)

### NVIDIA In-Game Inferencing (NVIGI) SDK
- **Affiliation**: NVIDIA
- **Venue**: NVIDIA Technical Blog, Feb 2025
- **Summary**: GPU-optimized plugin-based inference manager for integrating ACE models into C++ games. Supports ASR, SLMs (Llama-3.2-3B, Nemotron-Mini-4B, Mistral-Nemo-Minitron), embedding models. Uses compute-in-graphics (CIG) technology to run AI inference concurrently with rendering.
- **Link**: [NVIDIA Technical Blog](https://developer.nvidia.com/blog/bring-nvidia-ace-ai-characters-to-games-with-the-new-in-game-inference-sdk/)

### Code Agents for Minimizing Game Runtime Inference Costs
- **Affiliation**: NVIDIA
- **Venue**: NVIDIA Technical Blog, Mar 2026
- **Summary**: Code agent approach where SLMs generate and execute complex logic in a single inference call (vs. tool-calling's per-function calls). Uses Lua for safe embedding. Demonstrated in ASCII dungeon crawler where AI agent fights alongside player.
- **Key Innovation**: Code agents reduce GPU contention by generating all function calls in one inference.
- **Link**: [NVIDIA Technical Blog](https://developer.nvidia.com/blog/how-to-minimize-game-runtime-inference-costs-with-coding-agents/)

### AI Native Games: A Survey and Roadmap
- **Authors**: N/A
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Jul 2026
- **Abstract**: Defines AI-native games by whether runtime generative AI is constitutive of the core loop. Screens and analyzes 53 AI-native games. Proposes dual-axis G/N taxonomy and roadmap for controllable generation, AI-as-mechanic, multi-agent systems, and inference economics.
- **Key Innovation**: Formal definition and taxonomy of AI-native games with counterfactual criterion.
- **Link**: [arXiv:2607.00527](https://arxiv.org/abs/2607.00527)

---

## 9. World Models for Games

### Matrix-Game 3.0: Real-Time Interactive World Model with Long-Horizon Memory
- **Authors**: N/A
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Apr 2026
- **Abstract**: Memory-augmented interactive world model for 720p real-time long-form video generation. Industrial-scale data engine (UE5 + AAA games + real-world video). Error-aware training, camera-aware memory retrieval, multi-segment DMD distillation. Achieves 40 FPS at 720p with 5B model.
- **Key Innovation**: Real-time 720p interactive world model with long-horizon memory and 28B scaling.
- **Link**: [arXiv:2604.08995](https://arxiv.org/abs/2604.08995)

### Solaris: Multiplayer Video World Model in Minecraft
- **Authors**: N/A
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Feb 2026
- **Abstract**: First multiplayer video world model for consistent multi-view observations. SolarisEngine collects 12.64M multiplayer frames. Staged pipeline: single-player → multiplayer. Introduces Checkpointed Self Forcing for memory-efficient long-horizon training.
- **Key Innovation**: First multi-agent video world model for Minecraft with consistent multi-view simulation.
- **Link**: [arXiv:2602.22208](https://arxiv.org/abs/2602.22208)

### MineWorld: Real-Time Interactive World Model on Minecraft
- **Authors**: Jinhu Guo, Ye Yang, Tianyu He, H. Wu, Yushu Jiang, Tim Pearce, et al.
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Apr 2025
- **Abstract**: Visual-action autoregressive Transformer for Minecraft. Transforms scenes and actions into discrete tokens with next-token prediction. Novel parallel decoding algorithm predicts spatial-redundant tokens simultaneously. 4-7 FPS generation enabling real-time interaction. Outperforms SOTA diffusion-based world models.
- **Key Innovation**: Autoregressive visual-action model with parallel decoding for real-time Minecraft world modeling.
- **Link**: [arXiv:2504.08388](https://arxiv.org/abs/2504.08388)

### Matrix-Game: Interactive World Foundation Model (17B)
- **Authors**: N/A
- **Affiliation**: Skywork AI
- **Venue**: arXiv preprint, Jun 2025
- **Abstract**: 17B-parameter interactive world foundation model for controllable Minecraft world generation. Two-stage training: unlabeled pretraining + action-labeled fine-tuning. 2,700+ hours unlabeled + 1,000+ hours labeled clips. Introduces GameWorld Score benchmark. Outperforms Oasis and MineWorld on all metrics.
- **Key Innovation**: Large-scale world foundation model with precise action control and physical consistency.
- **Link**: [arXiv:2506.18701](https://arxiv.org/abs/2506.18701)

### WorldCam: Interactive Autoregressive 3D Gaming Worlds
- **Authors**: N/A
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Mar 2026
- **Abstract**: Uses camera pose as unifying geometric representation for both immediate action control and long-horizon 3D consistency. Physics-based continuous action space with Lie algebra for 6-DoF poses. 3,000-minute human gameplay dataset (CS, Xonotic, Unvanquished). Outperforms Matrix-Game 2.0 and GameCraft.
- **Key Innovation**: Camera pose as unified representation for action control and spatial consistency in interactive world models.
- **Link**: [arXiv:2603.16871](https://arxiv.org/abs/2603.16871)

### ActWorld: From Explorable to Interactive World Model
- **Authors**: Zhexiao Xiong, Y Song, Hao Kang, Qing Yan, Liming Jiang, Jie Yang, et al.
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Jun 2026
- **Abstract**: Extends navigation-centric world models to support mid-rollout object interaction. Constructs 100K interaction video dataset with per-chunk captions. Hierarchical action-aware memory routes compression by interaction importance.
- **Key Innovation**: First interactive world model supporting both navigation and object interaction within a single model.
- **Link**: [arXiv:2606.17730](https://arxiv.org/abs/2606.17730)

### Multiplayer Interactive World Models with Representation Autoencoders
- **Authors**: N/A
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Jul 2026
- **Abstract**: First multiplayer world model for highly dynamic environments (Rocket League). 5B-parameter latent diffusion model trained on 10,000 hours of bot gameplay. Generates 4-player matches at 20 FPS on single B200 GPU. Rollouts stable for hours.
- **Key Innovation**: First multiplayer world model for fast physics-based games with hours-long rollout stability.
- **Link**: [arXiv:2607.05352](https://arxiv.org/abs/2607.05352)

### OPINE-World: Programmatic World Modeling with Ontology-Error-Prioritized Exploration
- **Authors**: N/A
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Jul 2026
- **Abstract**: LLM agent learning object-centric programmatic world models online via hypothesis-and-test loop. Two cooperating agents (action + synthesis) with exact-replay verification. Solves 20/25 ARC-AGI-3 games without per-game training (action-efficiency 78.4 vs human baseline).
- **Key Innovation**: Programmatic world models synthesized online by LLM agents with Bayesian ontology-error exploration.
- **Link**: [arXiv:2607.01531](https://arxiv.org/abs/2607.01531)

---

## 10. Related Techniques

### Curiosity-Critic: Cumulative Prediction Error Improvement as Intrinsic Reward
- **Authors**: Vin Bhaskara, Haicheng Wang
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Apr 2026
- **Abstract**: Grounds intrinsic reward in improvement of cumulative prediction error. Learns asymptotic error baseline online via critic. Separates epistemic from aleatoric uncertainty. Outperforms prediction-error, visitation-count, and RND on stochastic grid worlds.
- **Key Innovation**: Tractable intrinsic reward distinguishing reducible from irreducible prediction error for world model training.
- **Link**: [arXiv:2604.18701](https://arxiv.org/abs/2604.18701)

### From Curiosity to Competence: World Models and Exploration Dynamics
- **Authors**: N/A
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Jul 2025
- **Abstract**: Studies how intrinsic motivations (novelty, information gain, empowerment) interact with learned representations in Dreamer agents. Hybrid curiosity-competence strategies yield synergistic exploration benefits.
- **Key Innovation**: Formal analysis of curiosity-competence trade-off in model-based RL with learned world models.
- **Link**: [arXiv:2507.08210](https://arxiv.org/abs/2507.08210)

### TROFI: Trajectory-Ranked Offline Inverse Reinforcement Learning
- **Authors**: N/A
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Jun 2025
- **Abstract**: Learns reward function from human preferences (trajectory rankings) without requiring optimal trajectories. Combines T-REX + TD3+BC. Validated on D4RL benchmarks and 3D game environment. Performs comparably to ground-truth reward.
- **Key Innovation**: Weakly-supervised offline IRL using ranked demonstrations for game development without reward engineering.
- **Link**: [arXiv:2506.22008](https://arxiv.org/abs/2506.22008)

### STO-RL: Offline RL with LLM-Guided Subgoal Temporal Order
- **Authors**: Chengyang Gu, Yuxin Pan, Hui Xiong, Yize Chen
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Jan 2026
- **Abstract**: Uses LLMs to generate temporally ordered subgoal sequences with potential-based reward shaping. Transforms sparse terminal rewards into dense temporally consistent signals. Outperforms SOTA offline goal-conditioned and hierarchical RL baselines.
- **Key Innovation**: LLM-guided temporal order for subgoal-based reward shaping in offline RL.
- **Link**: [arXiv:2601.08107](https://arxiv.org/abs/2601.08107)

### HiPER: Hierarchical RL with Explicit Credit Assignment for LLM Agents
- **Authors**: N/A
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Feb 2026
- **Abstract**: Hierarchical Plan-Execute RL framework separating high-level planning from low-level execution. Introduces Hierarchical Advantage Estimation (HAE) with boundary-aware bootstrapping. Provably reduces variance over flat GAE.
- **Key Innovation**: Hierarchical advantage estimation aligned with two-level plan-execute structure for LLM agents.
- **Link**: [arXiv:2602.16165](https://arxiv.org/abs/2602.16165)

### Efficient Hierarchical Implicit Flow Q-learning for Offline Goal-Conditioned RL
- **Authors**: Zhiqiang Dong, Teng Pang, Rongjian Xu, Guoqiang Wu
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Apr 2026
- **Abstract**: Goal-conditioned mean flow policy capturing complex target distributions via learned average velocity field. Introduces LeJEPA loss for discriminative goal representations. Strong performance on OGBench (state-based and pixel-based).
- **Key Innovation**: Flow-based hierarchical policy for offline goal-conditioned RL with one-step sampling.
- **Link**: [arXiv:2604.08960](https://arxiv.org/abs/2604.08960)

### PROF: LLM-Based Reward Code Preference Optimization for Offline IL
- **Authors**: N/A
- **Affiliation**: N/A
- **Venue**: ICLR 2026
- **Abstract**: LLM generates and improves executable reward functions for offline imitation learning. Introduces Reward Preference Ranking (RPR) using dominance scores without environment interaction. Surpasses strong baselines on D4RL.
- **Key Innovation**: Automatic reward function code generation and optimization for offline IL using LLMs.
- **Link**: OpenReview ICLR 2026

### Cago: Capability-Aware Goal Sampling for Learning from Demonstrations
- **Authors**: Ye Duan, Yuning Wang, Wenjie Qiu, He Zhu
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Jan 2026
- **Abstract**: Treats demonstrations as structured roadmaps. Monitors which parts of a demonstration the agent can reach and samples intermediate goals at the boundary of current capabilities. Builds adaptive curriculum for progressive task learning.
- **Key Innovation**: Capability-aware goal sampling aligning learning process with agent's evolving competence.
- **Link**: [arXiv:2601.08731](https://arxiv.org/abs/2601.08731)

### TRRO/PIRO: Trust Region Reward Optimization & Proximal Inverse Reward Optimization
- **Authors**: Yang Chen, Menglin Zou, Jiaqi Zhang, Yingqian Zhang, Junyi Yang, G. Gendron, et al.
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Sep 2025
- **Abstract**: Unifies non-adversarial IRL methods under likelihood maximization framework. TRRO guarantees monotonic improvement. PIRO provides IRL counterpart to TRPO stability guarantees. Matches/surpasses SOTA on MuJoCo and Gym-Robotics.
- **Key Innovation**: First monotonic improvement guarantee for inverse RL via trust-region optimization.
- **Link**: [arXiv:2509.23135](https://arxiv.org/abs/2509.23135)

### Multi-Agent Imitation Learning with Function Approximation
- **Authors**: Luca Viano, Till Freihaut, Emanuele Nevali, Volkan Cevher, Matthieu Geist, Giorgia Ramponi
- **Affiliation**: N/A
- **Venue**: arXiv preprint, Feb 2026
- **Abstract**: First theoretical analysis of multi-agent imitation learning in linear Markov games. Replaces state-action concentrability with feature-level coefficient. First computationally efficient interactive MAIL algorithm with sample complexity depending only on feature dimension d.
- **Key Innovation**: Theoretical foundations for multi-agent imitation learning with function approximation.
- **Link**: [arXiv:2602.22810](https://arxiv.org/abs/2602.22810)

### Structured Imitation Learning of Interactive Policies through Inverse Games
- **Authors**: Muchen Sun, Todd D. Murphey
- **Affiliation**: Northwestern University
- **Venue**: arXiv preprint, Nov 2025
- **Abstract**: Two-step structured IL: learn individual behavioral patterns from multi-agent demonstrations, then learn inter-agent dependencies via inverse game solving. Significantly improves non-interactive policies on 5-agent social navigation.
- **Key Innovation**: Game-theoretic structure for imitation learning of interactive multi-agent policies.
- **Link**: [arXiv:2511.12848](https://arxiv.org/abs/2511.12848)

---

## Summary Statistics

| Category | Papers |
|----------|--------|
| Game RL — Self-Play & Board Games | 5 |
| Game RL — Multi-Agent & MARL Foundation Models | 5 |
| Game RL — Atari & Video Games | 3 |
| Game AI Bots & NPC Intelligence | 8 |
| Game Foundation Models | 7 |
| Procedural Content Generation | 6 |
| Game Benchmarks | 6 |
| Industry Game AI | 4 |
| World Models for Games | 8 |
| Related Techniques | 11 |
| **Total** | **63** |
