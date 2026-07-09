---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-07-09)"
type: synthesis
created: 2026-07-09
updated: 2026-07-09
sources: [web-search]
tags: [game-rl, game-ai, reinforcement-learning, llm-agents, foundation-models, procedural-content-generation, benchmarks, world-models, self-play]
---

# Game RL & Game AI Bot — Daily Paper Digest

> Curated from arXiv, proceedings, and recent conferences. 50+ papers across 7 categories.
> Date: 2026-07-09

---

## 1. Game RL — Reinforcement Learning in Games

### 1.1 QZero: Mastering the Game of Go with Self-play Experience Replay
- **Authors:** Jingbin Liu, Xuechun Wang
- **Affiliation:** NetEase
- **Venue:** arXiv:2601.03306, 2026
- **Key innovation:** First model-free RL algorithm to master Go without MCTS. Uses entropy-regularized Q-learning with a single Q-value network. Trained tabula rasa on 7 GPUs for 5 months, achieving AlphaGo-comparable performance. Demonstrates off-policy RL feasibility for large-scale environments.
- **Link:** https://arxiv.org/abs/2601.03306

### 1.2 Learning Game-Playing Agents with Generative Code Optimization
- **Authors:** Zhiyi Kuang, Ryan Rong, YuCheng Yuan, Allen Nie
- **Affiliation:** Stanford University
- **Venue:** arXiv:2508.19506, 2025
- **Key innovation:** Represents policies as Python programs refined by LLMs. Self-evolving code agents improve through execution traces and natural language feedback. Competitive with deep RL baselines on Atari (Pong, Breakout, Space Invaders) while using significantly less training time and fewer environment interactions.
- **Link:** https://arxiv.org/abs/2508.19506

### 1.3 Data-Augmented Game Starts for Accelerating Self-Play Exploration (DAGS)
- **Authors:** J.B. Lanier
- **Affiliation:** DeepMind
- **Venue:** arXiv:2605.14379, 2026
- **Key innovation:** Multi-agent starting-state sampling strategy using offline demonstrations to bootstrap self-play exploration in imperfect-information games. Tested on Kuhn Poker, Goofspiel with lower exploitability under fixed compute budgets. New benchmark environments for OpenSpiel.
- **Link:** https://arxiv.org/abs/2605.14379

### 1.4 Think in Games (TiG): Learning to Reason in Games via RL with LLMs
- **Authors:** Yi Liao et al.
- **Affiliation:** -
- **Venue:** arXiv:2508.21365, 2025
- **Key innovation:** Framework that reformulates RL-based decision-making as language modeling. LLMs generate language-guided policies refined through online RL. Provides step-by-step natural language explanations, bridging declarative and procedural knowledge with competitive performance and reduced data demands.
- **Link:** https://arxiv.org/abs/2508.21365

### 1.5 Reinforcement Learning in Strategy-Based and Atari Games: A Review
- **Authors:** Multiple
- **Affiliation:** Google DeepMind
- **Venue:** arXiv:2502.10303, 2025
- **Key innovation:** Comprehensive review of DeepMind's innovations (AlphaGo, AlphaGo Zero, MuZero) covering key innovations, training process, challenges, and improvements. Covers MiniZero and multi-agent model extensions.
- **Link:** https://arxiv.org/abs/2502.10303

---

## 2. Game AI Bot — LLM-Powered Game Agents

### 2.1 AVA: Attentive VLM Agent for Mastering StarCraft II
- **Authors:** Weiyu Ma, Yuqian Fu, Zecheng Zhang, Bernard Ghanem, Guohao Li
- **Affiliation:** ACL 2026 Findings
- **Venue:** ACL 2026 Findings
- **Key innovation:** First multimodal benchmark (AVACraft) for StarCraft II supporting both MARL and VLM paradigms. Provides RGB visual inputs, natural language observations, and structured state. MARL achieves 27.1% win rate after 1M steps; VLMs deliver 75-81% zero-shot win rates without training.
- **Link:** https://aclanthology.org/2026.findings-acl.208/

### 2.2 Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL
- **Authors:** Multiple (Princeton)
- **Affiliation:** Princeton University
- **Venue:** arXiv:2605.00347, 2026
- **Key innovation:** Adapted PPO with lightweight turn-level critic for training VLMs on long-horizon (100+ turn) game tasks in Super Mario Land. Shows pretrained VLMs provide strong action priors, significantly improving sample efficiency. Odysseus achieves 3x average game progress over frontier models.
- **Link:** https://arxiv.org/abs/2605.00347

### 2.3 COSPLAY: Co-Evolving LLM Decision and Skill Bank Agents
- **Authors:** Xiyang Wu, Zongxia Li, Guangyao Shi, et al.
- **Affiliation:** Multiple
- **Venue:** arXiv:2604.20987, 2026
- **Key innovation:** Co-evolution framework with learnable skill bank for LLM agents. Decision agent retrieves skills from bank; skill pipeline discovers reusable skills from unlabeled rollouts. 8B base model achieves 25.1% average reward improvement over frontier LLMs across 6 game environments.
- **Link:** https://arxiv.org/abs/2604.20987

### 2.4 Sensi: Curriculum-Based Test-Time Learning for LLM Game Agents
- **Authors:** Multiple
- **Affiliation:** -
- **Venue:** arXiv:2603.17683, 2026
- **Key innovation:** Structured test-time learning through two-player architecture (Observer + Actor), curriculum-based learning, and database-as-control-plane. Sensi v2 achieves 50-94x greater sample efficiency (~32 attempts vs 1600-3000) on ARC-AGI-3. Diagnoses perception hallucination as bottleneck.
- **Link:** https://arxiv.org/abs/2603.17683

### 2.5 PokéChamp: Expert-level Minimax Language Agent
- **Authors:** Multiple
- **Affiliation:** -
- **Venue:** arXiv:2503.04094, 2025
- **Key innovation:** LLM-powered minimax tree search agent for Pokémon battles. LLMs replace action sampling, opponent modeling, and value function estimation. GPT-4o achieves 76% win rate vs best LLM bot, 84% vs strongest rule-based bot. Projected Elo 1300-1500 on online ladder (top 30%-10%). Compiles 3M+ battle dataset.
- **Link:** https://arxiv.org/abs/2503.04094

### 2.6 PORTAL: Agents Play Thousands of 3D Video Games
- **Authors:** Multiple
- **Affiliation:** -
- **Venue:** arXiv:2503.13356, 2025
- **Key innovation:** Language-guided policy generation using LLMs to produce behavior trees in DSL. Decouples tactical planning from execution for real-time performance. Hybrid rule-based + neural architecture. Demonstrated across thousands of FPS games. No inference latency during gameplay.
- **Link:** https://arxiv.org/abs/2503.13356

### 2.7 MEMO: Memory-Augmented Model Context Optimization for Multi-Agent LLM Games
- **Authors:** Multiple
- **Affiliation:** -
- **Venue:** arXiv:2603.09022, 2026
- **Key innovation:** Self-play framework optimizing inference-time context via persistent memory bank and tournament-style prompt evolution. Raises win rate from 25.1% to 49.5% for GPT-4o-mini (from 20.9% to 44.3% for Qwen-2.5-7B), using 19x fewer games than RL baselines.
- **Link:** https://arxiv.org/abs/2603.09022

### 2.8 Nemobot Games: Crafting Strategic AI Gaming Agents with LLMs
- **Authors:** Y. Wang et al.
- **Affiliation:** -
- **Venue:** arXiv:2604.21896, 2026
- **Key innovation:** Interactive agentic engineering environment extending Shannon's taxonomy with LLMs. Covers dictionary-based, solvable, heuristic, and learning-based games. Integrates reinforcement learning with human feedback, self-critique, and crowdsourced strategy refinement.
- **Link:** https://arxiv.org/abs/2604.21896

### 2.9 OpenGame: Open Agentic Coding for Games
- **Authors:** Yilei Jiang, Jinyuan Hu, Qianyin Xiao, et al.
- **Affiliation:** Multiple
- **Venue:** arXiv:2604.18394, 2026
- **Key innovation:** First open-source agentic framework for end-to-end web game creation. Game Skill: Template + Debug skill components. GameCoder-27B specialized code LLM trained via continual pre-training, SFT, and execution-grounded RL. OpenGame-Bench for evaluating agentic game generation.
- **Link:** https://arxiv.org/abs/2604.18394

### 2.10 MineDreamer: Learning to Follow Instructions via Chain-of-Imagination
- **Authors:** Enshen Zhou, Yiran Qin, Zhenfei Yin, et al.
- **Affiliation:** Multiple
- **Venue:** IROS 2025 Oral; NeurIPS 2024 OWA Workshop
- **Key innovation:** Chain-of-Imagination (CoI) mechanism for instruction following. Uses MLLM + diffusion to envision step-by-step execution. Translates imaginations into visual prompts for VPT controller. Collects 64x more seeds, 7x more wood than VPT baseline in Minecraft.
- **Link:** https://arxiv.org/abs/2403.12037

---

## 3. Game Foundation Models

### 3.1 NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors:** Loïc Magne, Anas Awadalla, Guanzhi Wang, et al. (NVIDIA, Stanford, Caltech, UChicago, UT Austin)
- **Affiliation:** NVIDIA
- **Venue:** CVPR 2026
- **Key innovation:** Vision-action foundation model trained on 40,000 hours of gameplay across 1000+ games. Flow-matching DiT architecture adapted from GR00T N1. Constructs internet-scale video-action dataset from input overlay software. Up to 52% relative improvement in task success on unseen games. Open-source: dataset, evaluation suite, weights.
- **Link:** https://arxiv.org/abs/2601.02427

### 3.2 Game-TARS: Pretrained Foundation Models for Generalist Multimodal Game Agents
- **Authors:** Zihao Wang, Xujing Li, Yining Ye, et al.
- **Affiliation:** ByteDance
- **Venue:** arXiv:2510.23691, 2025
- **Key innovation:** Unified scalable action space anchored to keyboard-mouse inputs. Pre-trained on 500B+ tokens. Decaying continual loss for causal confusion; Sparse-Thinking for reasoning-efficiency tradeoff. 2x success rate over previous SOTA on Minecraft, outperforms GPT-5 and Gemini-2.5-Pro on FPS benchmarks.
- **Link:** https://arxiv.org/abs/2510.23691

### 3.3 Scaling Behavior Cloning Improves Causal Reasoning: Pixels2Play
- **Authors:** Yuguang Yue, Irakli Salia, Samuel Hunt, Chris Green, Wenzhe Shi, Jonathan J. Hunt
- **Affiliation:** Elefant / Multiple
- **Venue:** arXiv:2601.04575, 2026
- **Key innovation:** Open recipe for real-time game-playing foundation model (Pixels2Play). 8300+ hours of human gameplay data. Systematic study of BC scaling laws: larger models and datasets learn more causal policies. Models up to 1.2B parameters. Competitive with human play on 3D games. Fully open-source.
- **Link:** https://arxiv.org/abs/2601.04575

### 3.4 Pixels to Play (P2P0.1): A Foundation Model for 3D Gameplay
- **Authors:** Yuguang Yue, Chris Green, Samuel Hunt, Irakli Salia, Wenzhe Shi, Jonathan J. Hunt
- **Affiliation:** Elefant
- **Venue:** arXiv:2508.14295, 2025
- **Key innovation:** Decoder-only transformer trained via BC on instrumented human gameplay + unlabeled public videos (inverse-dynamics imputed actions). Competent play across Roblox and MS-DOS titles on a single consumer GPU. Text-conditioned policy for controllable AI agents.
- **Link:** https://arxiv.org/abs/2508.14295

### 3.5 Towards Generalist Game Players: A Survey of Foundation Models in the Game Multiverse
- **Authors:** Kuan Zhang, Dongchen Liu, Qiyue Zhao, et al.
- **Affiliation:** Tsinghua University
- **Venue:** arXiv:2605.09965, 2026
- **Key innovation:** Comprehensive survey tracing generalist game players across four eras: symbolic/RL agents → foundation model generalists → future creator stage. Analyzes four pillars: Dataset, Model, Harness, Benchmark. Proposes five-level roadmap from single-game mastery to creator stage.
- **Link:** https://arxiv.org/abs/2605.09965

### 3.6 MARL-GPT: Foundation Model for Multi-Agent Reinforcement Learning
- **Authors:** Multiple
- **Affiliation:** Cognitive AI Systems
- **Venue:** arXiv:2604.05943, 2026
- **Key innovation:** Single GPT-based model trained via offline RL on expert trajectories across SMACv2 (400M), GRF (100M), and POGEMA (1B). Unified transformer encoder requiring no task-specific tuning. Competitive with specialized MARL baselines across all environments.
- **Link:** https://arxiv.org/abs/2604.05943

---

## 4. Procedural Content Generation

### 4.1 PCGRLLM: LLM-Driven Reward Design for PCG RL
- **Authors:** In-Chang Baek, Sunghyun Kim, Sam Earle, Zehua Jiang, Noh Jin-Ha, Julian Togelius, Kyung-Joong Kim
- **Affiliation:** GIST, NYU
- **Venue:** arXiv:2502.10906, 2025
- **Key innovation:** Extended architecture using LLMs for reward function generation in PCG RL. Feedback mechanism with reasoning-based prompt engineering. 415% and 40% performance improvements depending on LLM zero-shot capabilities; reduces human dependency in game AI development.
- **Link:** https://arxiv.org/abs/2502.10906

### 4.2 IPCGRL: Language-Instructed RL for Procedural Level Generation
- **Authors:** In-Chang Baek, Sunghyun Kim, Seo-Young Lee, Dong-Hyeon Kim, Kyung-Joong Kim
- **Affiliation:** GIST
- **Venue:** IEEE CoG 2025
- **Key innovation:** Instruction-based PCG via RL using sentence embedding model. Fine-tunes task-specific embeddings to compress level conditions. Up to 21.4% better controllability and 17.2% better generalizability for unseen instructions.
- **Link:** https://arxiv.org/abs/2503.12358

### 4.3 VIPCGRL: Human-Aligned PCG RL via Text-Level-Sketch Shared Representation
- **Authors:** In-Chang Baek, Seoyoung Lee, Sung-Hyun Kim, Geumhwan Hwang, KyungJoong Kim
- **Affiliation:** GIST
- **Venue:** arXiv:2508.09860, 2025
- **Key innovation:** Three-modality framework (text, level, sketches) for PCG RL. Shared embedding space via quadruple contrastive learning across modalities and human-AI styles. Outperforms baselines in human-likeness validated by metrics and human evaluation.
- **Link:** https://arxiv.org/abs/2508.09860

### 4.4 Multi-task PCG with RL (Scientific Reports)
- **Authors:** Aylin Nekahdari, Elaheh Daei Kouzehkonani, Nima Saeedi, Kimia Shirini, Sina Samadi Gharehveran
- **Affiliation:** -
- **Venue:** Scientific Reports, 2026
- **Key innovation:** Multi-task language-based framework for PCG RL using DeBERTa encoder and multi-objective training (regression, contrastive alignment, hybrid learning). 14,000+ command-level pairs in Super Mario environment. Outperforms BERT-based methods in command following and structural diversity.
- **Link:** https://doi.org/10.1038/s41598-026-48234-7

### 4.5 MOPCGRL: Multi-Objective PCG via RL
- **Authors:** Yubo Yuan, Qingquan Zhang, Bo Yuan, et al.
- **Affiliation:** Multiple
- **Venue:** Complex System Modeling and Simulation, 2026
- **Key innovation:** Trains a set of generators balancing multiple diversity metrics with playability constraints. Increases generator distribution diversity while accelerating early-stage convergence on Mario-AI benchmark.
- **Link:** https://doi.org/10.23919/csms.2025.0034

### 4.6 Agentic PCG: Procedural Content Generation via Tool-using LLMs
- **Authors:** Zehua Jiang, Sam Earle, Ahmed Khalifa, Julian Togelius
- **Affiliation:** NYU
- **Venue:** SSRN 6499021, 2026
- **Key innovation:** LLM agent system using structured tool calling for game level optimization. Supports Binary Maze, Zelda, Sokoban, LodeRunner, Super Mario Bros. Iterative evaluation and editing with configurable metrics targets.
- **Link:** https://github.com/JiangZehua/AgenticPCG

---

## 5. Game Benchmarks

### 5.1 OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents
- **Authors:** Mingxian Lin, Shengju Qian, Yuqi Liu, et al.
- **Affiliation:** HKU / LIGHTSPEED Studios
- **Venue:** arXiv:2606.09826, 2026
- **Key innovation:** 12 newly built Unreal Engine 5 games (7 Solo, 3 PvP, 2 Coop). Improvement Dynamics Curve (IDC) for agentic-reflection harness. Captures cold-start scores + improvement dynamics across reflection rounds. Evaluates 12 VLM agents.
- **Link:** https://arxiv.org/abs/2606.09826

### 5.2 lmgame-Bench: How Good are LLMs at Playing Games?
- **Authors:** Lanxiang Hu, Ming Huo, Yuxuan Zhang, et al.
- **Affiliation:** UC Berkeley
- **Venue:** arXiv:2505.15146, 2025
- **Key innovation:** Benchmarks 13 leading LLMs across 6 games (Sokoban, Super Mario, Tetris, 2048, Candy Crush, Ace Attorney). Features perception/memory scaffolds, contamination detection, and prompt optimization. RL on a single game transfers to unseen games and external planning tasks.
- **Link:** https://arxiv.org/abs/2505.15146

### 5.3 GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents
- **Authors:** Mingyu Ouyang, Siyuan Hu, Kevin Qinghong Lin, Hwee Tou Ng, Mike Zheng Shou
- **Affiliation:** National University of Singapore (NUS)
- **Venue:** arXiv:2604.07429, 2026
- **Key innovation:** 34 games and 170 tasks in browser-based environment. Outcome-based, state-verifiable evaluation across puzzle, platformer, simulation, arcade, runner genres. Fully automated evaluation pipeline.
- **Link:** https://arxiv.org/abs/2604.07429

### 5.4 Orak: Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games
- **Authors:** Dongmin Park, Minkyu Kim, Beongjun Choi, et al.
- **Affiliation:** KRAFTON
- **Venue:** arXiv:2506.03610, 2025
- **Key innovation:** 12 popular games spanning all major genres. MCP-based plug-and-play interface. 10K+ gameplay trajectory fine-tuning dataset. Multi-dimensional evaluation: score leaderboard, LLM battle arenas, visual input analysis, agentic strategy analysis, and finetuning effects.
- **Link:** https://arxiv.org/abs/2506.03610

### 5.5 AI Gamestore: Scalable, Open-Ended Evaluation with Human Games
- **Authors:** Lance Ying, Ryan Truong, Prafull Sharma, et al.
- **Affiliation:** MIT / Harvard
- **Venue:** arXiv:2602.17594, 2026
- **Key innovation:** LLM-synthesized game evaluation platform. 100 games derived from Apple App Store and Steam. Evaluates 7 frontier VLMs; best models achieve <10% of human average score on most games. Diagnostic tool for identifying missing capabilities (world-model learning, memory, planning).
- **Link:** https://arxiv.org/abs/2602.17594

### 5.6 CivBench: Progress-Based Evaluation for LLMs' Strategic Decision-Making
- **Authors:** John Chen, Sihan Cheng, Can Gurkan, Mingyi Lin
- **Affiliation:** -
- **Venue:** arXiv:2604.07733, 2026
- **Key innovation:** Benchmark for LLM strategists in Civilization V. Trains models on turn-level game state to estimate victory probabilities. 307 games across 7 LLMs. Reveals model-specific effects of agentic setup not visible through outcome-only evaluation.
- **Link:** https://arxiv.org/abs/2604.07733

### 5.7 PokéAgent Challenge: Competitive and Long-Context Learning at Scale
- **Authors:** Multiple
- **Affiliation:** NeurIPS 2025 Competition
- **Venue:** arXiv:2603.15563, 2026
- **Key innovation:** Two-track benchmark: Competitive Battling (20M+ trajectories) + RPG Speedrunning (Pokémon Emerald). Orthogonality analysis shows Pokémon battling measures capabilities nearly orthogonal to standard benchmarks (rank-2 SVD explains only 27% of GXE variance). 100+ teams in NeurIPS 2025 competition.
- **Link:** https://arxiv.org/abs/2603.15563

### 5.8 RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
- **Authors:** Multiple
- **Affiliation:** -
- **Venue:** OpenReview, 2026
- **Key innovation:** 75 LLM-generated Elo-calibrated policies across 5 game environments. Agents infer hidden policies as executable code from behavioral traces. Frontier models close 34-72% of gap. Recovered code provides competitive advantage for counter-play.
- **Link:** https://openreview.net/forum?id=KTnZYPgaQz

---

## 6. Industry Game AI

### 6.1 Gran Turismo Sophy: Five Years On — From Nature Cover to Open Frontier
- **Authors:** Sony AI / Polyphony Digital / SIE
- **Affiliation:** Sony AI
- **Venue:** Sony AI Blog, July 2026
- **Key innovation:** First deep RL agent as permanent feature in a console game. Sophy 2.0 (340+ cars, 9 tracks), Sophy 2.1 (Custom Race, 500+ cars), Sophy 3.0 Power Pack (50 races, 24h endurance, full race weekends). Split-second control, multi-objective racing, human-like racing line learning. Influenced Sony's table tennis robot (Nature 2026).
- **Link:** https://ai.sony/blog/gran-turismo-sophy-five-years-on-from-nature-cover-to-open-frontier

### 6.2 NVIDIA ACE: In-Game Inferencing and NPC AI
- **Authors:** NVIDIA
- **Affiliation:** NVIDIA
- **Venue:** NVIDIA Technical Blog, March-June 2026
- **Key innovation:** ACE Game Agent SDK (open source C/C++). Agent, Chat, and RAG APIs for autonomous NPCs. Code agents with Lua for low-latency on-device inference. Production deployments: PUBG Ally (KRAFTON), Total War: PHARAOH advisor, inZOI, NARAKA. UE5 plugins for ASR, SLM (Qwen 3.5 4B), TTS.
- **Link:** https://developer.nvidia.com/blog/build-on-device-ai-companions-with-the-nvidia-ace-game-agent-sdk-and-unreal-engine-5-plugins/

### 6.3 Ubisoft Teammates: Experimental Interactive Characters
- **Authors:** Ubisoft
- **Affiliation:** Ubisoft
- **Venue:** GTC San Jose 2026
- **Key innovation:** Real-time GenAI NPCs with voice interaction. Hybrid cloud/on-device inference. Cascaded pipeline (ASR → LLM → TTS) with end-to-end 1.5s latency. Fine-tuned 0.34B SLM on-device (RTX 4090/5090) using SFT + DPO + GRPO with INT4 quantization. Demo at GTC 2026.
- **Link:** https://www.nvidia.com/en-us/on-demand/session/gtc26-s81739/

### 6.4 Generative AI for Dynamic NPC Behavior and PCG: Production Deployment Survey
- **Authors:** Multiple
- **Affiliation:** Industry
- **Venue:** IJETCSIT, 2026
- **Key innovation:** Comprehensive survey of production GenAI for NPCs/PCG. Covers Epic Games (Fortnite), Rockstar (GTA VI dialogue decay), Ubisoft (NEO NPC), NVIDIA ACE, Inworld AI. Reports 25-40% dev time reduction, >20% cost savings in asset production, up to 40% player satisfaction improvement. $1.79B market in 2026.
- **Link:** https://www.ijetcsit.org/index.php/ijetcsit/article/view/743

---

## 7. Related Techniques

### 7.1 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning
- **Authors:** Multiple
- **Affiliation:** -
- **Venue:** ICLR 2026; arXiv:2506.24119, 2025
- **Key innovation:** Fully online multi-agent RL for LLMs playing zero-sum language games. Role-conditioned advantage estimation (RAE) stabilizes training. Up to 10% improvement across 8 reasoning benchmarks. Multi-game training (TicTacToe, Kuhn Poker, Simple Negotiation) yields strongest results. Benefits even DeepSeek-R1-Distill-Qwen-7B.
- **Link:** https://arxiv.org/abs/2506.24119

### 7.2 MARSHAL: Multi-Agent Reasoning via Self-Play with Strategic LLMs
- **Authors:** Hui Yuan, Zhe Xu, Zhen Tan, et al.
- **Affiliation:** Multiple
- **Venue:** arXiv:2510.15414, 2025
- **Key innovation:** End-to-end RL framework for multi-turn multi-agent self-play. Turn-level advantage estimator and agent-specific advantage normalization. Up to 28.7% performance improvement in held-out games. Zero-shot gains: up to 10.0% on AIME, 7.6% on GPQA-Diamond.
- **Link:** https://arxiv.org/abs/2510.15414

### 7.3 Multi-Agent Transformer World Model (MATWM)
- **Authors:** Azad Deihim, Eduardo Alonso, Dimitra Apostolopoulou
- **Affiliation:** City, University of London
- **Venue:** arXiv:2506.18537, 2025
- **Key innovation:** Decentralized imagination framework with semi-centralized critic and teammate prediction. Prioritized replay handles non-stationarity. SOTA on SMAC, PettingZoo, MeltingPot. Near-optimal performance in as few as 50K environment interactions.
- **Link:** https://arxiv.org/abs/2506.18537

### 7.4 Multiplayer Interactive World Models (Rocket League)
- **Authors:** Multiple
- **Affiliation:** -
- **Venue:** arXiv:2607.05352, 2026
- **Key innovation:** First multiplayer world model conditioning on action streams of multiple agents. 5B-parameter latent diffusion model on 10,000 hours of Rocket League gameplay. Generates 4-player matches at 20fps on single B200 GPU. Rollouts stable for hours. Open-source dataset and code.
- **Link:** https://arxiv.org/abs/2607.05352

### 7.5 MultiWorld: Scalable Multi-Agent Multi-View Video World Models
- **Authors:** Haoyu Wu, Jiwen Yu, Yingtian Zou, Xihui Liu
- **Affiliation:** -
- **Venue:** arXiv:2604.18564, 2026
- **Key innovation:** Multi-Agent Condition Module + Global State Encoder for accurate multi-agent controllability with multi-view consistency. Tested on multiplayer games and multi-robot manipulation. Outperforms baselines in fidelity, action following, and view consistency.
- **Link:** https://arxiv.org/abs/2604.18564

### 7.6 Internalizing World Models via Self-Play Finetuning (SPA)
- **Authors:** Shiqi Chen, Tiejun Zhu, Zian Wang, et al.
- **Affiliation:** -
- **Venue:** arXiv:2510.15047, 2025
- **Key innovation:** Decomposes world model into state representation and transition modeling. Cold-starts policy via self-play SFT stage, then simulates future states prior to policy optimization. Sokoban success rate from 25.6% to 59.8%; FrozenLake from 22.1% to 70.9% for Qwen2.5-1.5B.
- **Link:** https://arxiv.org/abs/2510.15047

### 7.7 ProPlay: Procedural World Models for Self-Evolving LLM Agents
- **Authors:** Yijun Ma, Zehong Wang, Yiyang Li, et al.
- **Affiliation:** -
- **Venue:** arXiv:2606.12780, 2026
- **Key innovation:** Procedure-level preplay via procedure graph. Agent rehearses future procedural paths before each episode; refines using environment feedback. Reliability record embedding for task-specific contribution estimation. Consistently improves self-evolution over strong baselines.
- **Link:** https://arxiv.org/abs/2606.12780

### 7.8 Dreamer 4: Training Agents Inside of Scalable World Models
- **Authors:** Danijar Hafner, Wilson Yan, Timothy Lillicrap
- **Affiliation:** DeepMind / Google
- **Venue:** arXiv:2509.24527, 2025
- **Key innovation:** Flow-matching dynamics with shortcut consistency training. First agent to obtain diamonds in Minecraft purely from offline data. Real-time interactive inference on single GPU. Significantly outperforms VPT offline agent using 100x less data.
- **Link:** https://arxiv.org/abs/2509.24527

### 7.9 GRACE: Language Model Framework for Explainable IRL
- **Authors:** Silvia Sapora, Devon Hjelm, Alexander Toshev, Omar Attia, Bogdan Mazoure
- **Affiliation:** -
- **Venue:** arXiv:2510.02180, 2025
- **Key innovation:** Uses LLMs within evolutionary search to reverse-engineer interpretable code-based reward functions from expert trajectories. Validated on BabyAI and AndroidWorld. Produces rewards that are transparent, verifiable, and effective in downstream RL.
- **Link:** https://arxiv.org/abs/2510.02180

### 7.10 iLLM: Language-Driven Exploration in RL
- **Authors:** Nicolas Bougie, Narimasa Watanabe
- **Affiliation:** -
- **Venue:** ACML 2025 (PMLR 260:127-142)
- **Key innovation:** Curiosity-driven approach leveraging LLM inductive bias for exploration. Two tasks: action generation and history compression. Maps state-action pairs to pretrained token embeddings. Evaluated on BabyAI-Text, MiniHack, Atari, Crafter — higher sample efficiency than prior curiosity methods.
- **Link:** https://proceedings.mlr.press/v260/bougie25a.html

### 7.11 SENSEI: Semantic Exploration Guided by Foundation Models
- **Authors:** Cansu Sancaktar, Christian G., et al.
- **Affiliation:** -
- **Venue:** ICML 2025 (PMLR 267:52745-52777)
- **Key innovation:** Distills reward signal of "interestingness" from VLM annotations into world model. Trains exploration policy maximizing semantic rewards + uncertainty via model-based RL. Discovers meaningful behaviors from images and low-level actions in robotic and video game simulations.
- **Link:** https://proceedings.mlr.press/v267/sancaktar25a.html

### 7.12 GLANCE: Driving Exploration in VLM Agents via Visual-Linguistic Curiosity
- **Authors:** Haoxi Li, Qinglin Hou, Jianfei Ma, et al.
- **Affiliation:** -
- **Venue:** arXiv:2605.03782, 2026
- **Key innovation:** Bridges reasoning and exploration by grounding linguistic world model into visual representations. Discrepancy between linguistic prediction and visual reality as intrinsic curiosity signal for RL. Aligns "what the agent thinks" with "what the agent sees."
- **Link:** https://arxiv.org/abs/2605.03782

### 7.13 Decoding Rewards in Competitive Games: Inverse Game Theory
- **Authors:** Junyi Liao, Zihan Zhu, Ethan Fang, Zhuoran Yang, Vahid Tarokh
- **Affiliation:** Duke / Princeton
- **Venue:** arXiv:2601.12707, 2026
- **Key innovation:** Unified framework for reward recovery in two-player zero-sum matrix/Markov games with entropy regularization. Establishes identifiability via quantal response equilibrium (QRE). Algorithm works in static and dynamic settings with MLE integration and theoretical guarantees.
- **Link:** https://arxiv.org/abs/2601.12707

### 7.14 From Curiosity to Competence: How World Models Interact with Exploration Dynamics
- **Authors:** Multiple
- **Affiliation:** -
- **Venue:** arXiv:2507.08210, 2025
- **Key innovation:** Studies trade-off between curiosity (novelty/information gain) and competence (empowerment). Tabular and Dreamer agents compared. Hybrid strategies combining information gain + empowerment achieve better exploration-safety balances. Dreamer agent reveals two-way interaction between exploration and representation learning.
- **Link:** https://arxiv.org/abs/2507.08210

### 7.15 Recursive Deep Inverse Reinforcement Learning (RDIRL)
- **Authors:** Multiple
- **Affiliation:** -
- **Venue:** ICLR 2026 Submission
- **Key innovation:** Online IRL using sequential second-order Newton updates (EKF-like). Fast convergence for real-time adversarial scenarios. Outperforms leading IRL algorithms on benchmark tasks including strategy game environments.
- **Link:** https://openreview.net/forum?id=JaPcjtJB1C

---

## Cross-Cutting Themes

| Theme | Papers | Key Insight |
|-------|--------|-------------|
| Foundation Models for Games | NitroGen, Game-TARS, Pixels2Play, MARL-GPT | Vision-action foundation models scaling to 1000+ games; unified action spaces enabling cross-game generalization |
| VLM + RL for Long-Horizon | Odysseus, AVA, SPIRAL, GLANCE | PPO with critic stabilization enables 100+ turn tasks; VLM priors drastically improve sample efficiency |
| Self-Play as Reasoning | SPIRAL, MARSHAL, MEMO, DAGS | Zero-sum games develop transferable reasoning patterns; role-conditioned advantage critical for stability |
| World Models for Games | Dreamer 4, MATWM, MultiWorld, ProPlay, Rocket League WM | Multiplayer world models debut; offline policy training inside learned simulators; procedure-level preplay |
| PCG with LLMs | PCGRLLM, IPCGRL, VIPCGRL, Agentic PCG | LLMs as reward designers for PCG RL; multi-modal control (text/level/sketch); tool-using LLM agents for level generation |
| Game Benchmarks | OmniGameArena, GameWorld, Orak, AI Gamestore, PokéAgent | UE5 native benchmarks; verifiable evaluation; orthogonal capability measurement |
| Industry Deployment | GT Sophy, NVIDIA ACE, Ubisoft Teammates | RL agents as permanent game features; on-device SLM NPCs at 1.5s latency; hybrid cloud/edge inference |
| Curiosity & Exploration | SENSEI, iLLM, GLANCE, From Curiosity to Competence | VLM-grounded semantic curiosity; LLM priors for directed exploration; hybrid curiosity-competence strategies |

---

## Newly Created Pages

The following pages were created during this ingest:
- (none — synthesis only)

## Updated Pages

- wiki/index.md (synthesis entry)
- wiki/log.md
