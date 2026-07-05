---
title: "Game RL & Game AI Bot — Daily Survey (2026-07-05)"
type: synthesis
created: 2026-07-05
updated: 2026-07-05
sources:
  - arxiv.org
tags: [game-rl, game-ai, game-foundation-models, pcg, benchmarks, industry-game-ai, world-models, self-play, curiosity, hierarchical-rl, offline-rl]
---

# Game RL & Game AI Bot — Daily Survey (2026-07-05)

> arXiv and recent proceedings scan for Game RL, Game AI Bots, Game Foundation Models, PCG, Benchmarks, Industry Game AI, and related techniques. Compiled 2026-07-05.

## 1. Game RL — Reinforcement Learning in Games

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors**: Bo Liu, Leon Guertler, Simon Yu, Zichen Liu, Penghui Qi, Daniel Balcells, Mickel Liu, Cheston Tan, Weiyan Shi, Min Lin, Wee Sun Lee, Natasha Jaques
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2506.24119v3, updated Mar 2026)
- **Abstract**: Introduces SPIRAL, a self-play framework where LLMs learn by playing multi-turn zero-sum games against continuously improving versions of themselves, generating an automatic curriculum of stronger opponents. Implements fully online multi-turn multi-agent RL for LLMs with role-conditioned advantage estimation (RAE) to stabilize training. Self-play on Kuhn Poker alone achieves 8.6% improvement on math and 8.4% on general reasoning, outperforming SFT on 25,000 expert game trajectories.
- **Key innovation**: Zero-sum game self-play as a general reasoning training signal for LLMs, eliminating human supervision; transfer identified through three cognitive patterns: systematic decomposition, expected value calculation, case-by-case analysis.
- **Link**: https://arxiv.org/abs/2506.24119

### Think in Games: Learning to Reason in Games via Reinforcement Learning with Large Language Models
- **Authors**: Multiple authors
- **Affiliation**: -
- **Venue**: arXiv preprint (2508.21365)
- **Abstract**: Proposes using digital games as environments where LLMs can safely explore and learn from consequences to bridge the gap between declarative and procedural knowledge. Demonstrates that game-based RL training improves spatial reasoning and cause-effect understanding in LLMs.
- **Key innovation**: Games as training ground for LLM procedural knowledge acquisition.
- **Link**: https://arxiv.org/abs/2508.21365

### Outbidding and Outbluffing Elite Humans: Mastering Liar's Poker via Self-Play and Reinforcement Learning
- **Authors**: Jefferey Rosenbluth, William Wong et al.
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2511.03724)
- **Abstract**: Develops "Solly," an AI agent for Liar's Poker using self-play RL with limited compute (not thousands of GPUs). Shows that small-scale imperfect-information games can achieve human-level performance with much less compute than existing benchmarks and without inference-time search.
- **Key innovation**: Demonstrates that Liar's Poker serves as an ideal small-scale testbed for imperfect-information multi-player game agents; compute-efficient self-play approach.
- **Link**: https://arxiv.org/abs/2511.03724

### SpinGPT: A Large-Language-Model Approach to Playing Poker Correctly
- **Authors**: Narada Maugin, Tristan Cazenave
- **Affiliation**: -
- **Venue**: Advances in Computer Games (ACG) 2025, LNCS (Springer)
- **Abstract**: Presents SpinGPT, the first LLM tailored to Spin & Go, a three-player online poker format. Trained in two stages: (1) Supervised Fine-Tuning on 320k high-stakes expert decisions; (2) RL on 270k solver-generated hands. Matches solver's actions in 78% of decisions. Achieves 13.4 BB/100 versus Slumbot in heads-up over 30,000 hands.
- **Key innovation**: First LLM-based approach to multi-player imperfect-information poker; demonstrates LLMs as a new way to tackle multi-player games where CFR complexity scales exponentially.
- **Link**: https://arxiv.org/abs/2509.22387

### Playing Non-Embedded Card-Based Games with Reinforcement Learning
- **Authors**: Tianyang Wu, Lipeng Wan, Yuhang Wang, Qiang Wan, Xuguang Lan
- **Affiliation**: -
- **Venue**: ICIRA 2024, LNCS vol 15206 (Springer, 2025)
- **Abstract**: Proposes a non-embedded offline RL training strategy using visual inputs for real-time autonomous gameplay in the RTS card game Clash Royale. Uses generative object detection dataset + object detection and OCR models. Enables real-time image acquisition, perception feature fusion, decision-making, and control on mobile devices, defeating built-in AI opponents.
- **Key innovation**: Non-embedded (vision-based) offline RL for card-based RTS games; complete pipeline from pixels to actions on mobile.
- **Link**: https://arxiv.org/abs/2504.04783

### Multi-Agent Training for Pommerman: Curriculum Learning and Population-based Self-Play Approach
- **Authors**: Nhat-Minh Huynh, Hoang-Giang Cao, I-Chen Wu
- **Affiliation**: -
- **Venue**: arXiv preprint (2407.00662v2, updated Jan 2025)
- **Abstract**: Introduces a system for training multi-agent systems to play Pommerman using curriculum learning and population-based self-play. Proposes adaptive annealing factor for dense exploration reward and Elo-based matchmaking mechanism. Trained agent outperforms top learning agents without requiring communication among allied agents.
- **Key innovation**: Adaptive annealing for sparse reward + population self-play with Elo matchmaking for multi-agent competitive games.
- **Link**: https://arxiv.org/abs/2407.00662

## 2. Game AI Bot — LLM-Powered Game Agents

### Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with Large Language Models
- **Authors**: Chee Wei Tan, Yuchen Wang, Shangxin Guo
- **Affiliation**: -
- **Venue**: arXiv preprint (2604.21896, Apr 2026)
- **Abstract**: Introduces Nemobot, an interactive agentic engineering environment for creating LLM-powered game agents across four game classes: dictionary-based, rigorously solvable, heuristic-based, and learning-based games. Uses tool-augmented generation and fine-tuning of strategic game agents. Demonstrates self-programming capability through crowdsourced learning and human creativity.
- **Key innovation**: Shannon's taxonomy operationalized via LLMs; programmable environment for game agent creation with self-programming AI.
- **Link**: https://arxiv.org/abs/2604.21896

### LLM-Driven NPCs: Cross-Platform Dialogue System for Games and Social Platforms
- **Authors**: Multiple authors
- **Affiliation**: -
- **Venue**: arXiv preprint (2504.13928, Apr 2025)
- **Abstract**: Proposes a cross-platform dialogue system for NPCs using LLMs. Combines memory systems with vector search and hybrid memory mechanisms for consistent, evolving interactions. Explores NPCs as persistent social companions beyond game boundaries.
- **Key innovation**: Cross-platform NPC dialogue with persistent memory; NPCs as social companions across games and platforms.
- **Link**: https://arxiv.org/abs/2504.13928

### AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making
- **Authors**: Multiple authors
- **Affiliation**: -
- **Venue**: arXiv preprint
- **Abstract**: Comprehensive framework for training LLM agents in multi-turn interactive decision-making through RL. Covers agent learning across diverse environments including games.
- **Key innovation**: RL training framework for long-horizon LLM agent decision-making.
- **Link**: https://arxiv.org/abs/ (search AgentGym-RL)

### DPEPO: Diverse Parallel Exploration Policy Optimization for LLM-based Agents
- **Authors**: -
- **Affiliation**: -
- **Venue**: arXiv preprint (2604.24320)
- **Abstract**: Proposes diverse parallel exploration policy optimization method for LLM-based agents to improve exploration efficiency in game-like environments.
- **Key innovation**: Parallel exploration strategy for LLM agents.
- **Link**: https://arxiv.org/abs/2604.24320

## 3. Game Foundation Models

### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi "Jim" Fan
- **Affiliation**: NVIDIA, Stanford, Caltech, UChicago, UT Austin
- **Venue**: IEEE CVPR 2026
- **Abstract**: Introduces a vision-action foundation model for generalist gaming agents trained on 40,000 hours of gameplay videos across 1,000+ games. Three key ingredients: (1) internet-scale video-action dataset from public gameplay videos, (2) multi-game benchmark for cross-game generalization, (3) unified vision-action model trained with large-scale behavior cloning. Achieves up to 52% relative improvement in task success rates over models trained from scratch on unseen games.
- **Key innovation**: First open foundation model for generalist gaming agents; internet-scale video-action dataset; cross-game generalization benchmark; open-source release of dataset, evaluation suite, and model weights.
- **Link**: https://arxiv.org/abs/2601.02427

### Towards Generalist Game Players: A Survey
- **Authors**: Kuan Zhang et al.
- **Affiliation**: THUSI Lab
- **Venue**: arXiv preprint (2605.09965, May 2026)
- **Abstract**: Comprehensive survey tracing the full lifecycle of generalist game players across four pillars: Dataset, Model, Harness, and Benchmark. Charts a five-level roadmap from single-game mastery to creator stage where the agent simultaneously creates and evolves within game multiverses. Analyzes five fundamental trade-offs bounding current systems.
- **Key innovation**: Unified lens on generalist game players with roadmap toward AGI through game multiverses.
- **Link**: https://arxiv.org/abs/2605.09965

### Matrix-Game: Interactive World Foundation Model
- **Authors**: Bowen Jiang, Zedong Gao, Eric Li, Yang Liu, Yahui Zhou
- **Affiliation**: -
- **Venue**: arXiv preprint (2506.18701, Jun 2025)
- **Abstract**: Introduces Matrix-Game, an interactive world foundation model for controllable game world generation with 17B+ parameters. Uses two-stage pipeline: large-scale unlabeled pretraining for environment understanding, then action-labeled training for interactive video generation. Curates Matrix-Game-MC, a Minecraft dataset with 2,700+ hours unlabeled and 1,000+ hours labeled gameplay clips. Enables precise control over character actions and camera movements.
- **Key innovation**: Large-scale interactive world foundation model for Minecraft with superior controllability and physical consistency.
- **Link**: https://arxiv.org/abs/2506.18701

### GameVerse: Can Vision-Language Models Learn from Video-based Reflection?
- **Authors**: Multiple authors
- **Affiliation**: -
- **Venue**: arXiv preprint (2603.06656)
- **Abstract**: Introduces a framework where vision-language models learn gameplay by watching and reflecting on video tutorials, mimicking human learning. Combines self-reflection with video-based instruction for game playing.
- **Key innovation**: Video-based reflection learning for VLMs in game environments.
- **Link**: https://arxiv.org/abs/2603.06656

## 4. Procedural Content Generation (PCG)

### PCGRLLM: Large Language Model-Driven Reward Design for Procedural Content Generation Reinforcement Learning
- **Authors**: In-Chang Baek, Sung-Hyun Kim, Sam Earle, Zehua Jiang, Jin-Ha Noh, Julian Togelius, Kyung-Joong Kim
- **Affiliation**: Multiple institutions
- **Venue**: Transactions on Games (accepted), arXiv preprint (2502.10906v2)
- **Abstract**: Introduces PCGRLLM, an LLM-driven reward design architecture for PCG-RL agents. Uses feedback mechanism and reasoning-based prompt engineering techniques. Evaluated on story-to-reward generation in 2D environments. Demonstrates substantial performance improvement (up to 415% depending on zero-shot capability), achieving human-comparable performance. Shows LLMs effective at synthesizing coarse reward functions encoding spatial structure.
- **Key innovation**: LLM as reward function engineer for PCG-RL; complementary human-LLM workflow for reward design.
- **Link**: https://arxiv.org/abs/2502.10906

### IPCGRL: Language-Instructed Reinforcement Learning for Procedural Level Generation
- **Authors**: In-Chang Baek, Sung-Hyun Kim, Seo-Young Lee, Dong-Hyeon Kim, Kyung-Joong Kim
- **Affiliation**: -
- **Venue**: Conference on Games 2025 (accepted)
- **Abstract**: Proposes IPCGRL, an instruction-based PCG method via RL incorporating sentence embedding models. Fine-tunes task-specific embedding representations to compress game-level conditions. Achieves up to 21.4% improvement in controllability and 17.2% improvement in generalizability for unseen instructions.
- **Key innovation**: Natural language instruction control for PCG-RL agents via fine-tuned sentence embeddings.
- **Link**: https://arxiv.org/abs/2503.12358

### Reinforcement Learning-Enhanced Procedural Generation for Dynamic Narrative-Driven AR Experiences
- **Authors**: Aniruddha Srinivas Joshi
- **Affiliation**: Independent Researcher, UC Santa Cruz
- **Venue**: GRAPP 2025
- **Abstract**: Presents an RL-enhanced Wave Function Collapse (WFC) framework for mobile AR environments. Integrates environment-specific rules and dynamic tile weight adjustments informed by RL. Generates contextually coherent and responsive maps for narrative-driven AR games.
- **Key innovation**: RL-dynamic WFC for adaptive AR map generation; first application of RL-enhanced PCG to mobile AR.
- **Link**: https://arxiv.org/abs/2501.08552

### Game Generation via Large Language Models
- **Authors**: Chengpeng Hu, Yunlong Zhao, Jialin Liu
- **Affiliation**: -
- **Venue**: 2024 IEEE Conference on Games
- **Abstract**: Investigates game generation (rules + levels simultaneously) via LLMs using video game description language (VGDL). Demonstrates how LLM-based framework generates new games with different prompt contexts.
- **Key innovation**: LLM-based simultaneous game rule and level generation, extending PCG to full game creation.
- **Link**: https://arxiv.org/abs/2404.08706

## 5. Game Benchmarks

### Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games
- **Authors**: Dongmin Park et al. (Jaehyung Lee, Inkyu Park, Byeong-Uk Lee, Jaeyoung Hwang, Jaewoo Ahn, Ameya S. Mahabaleshwarkar, Bilal Kartal, Pritam Biswas, Yoshi Suhara, Kangwook Lee, Jaewoong Cho)
- **Affiliation**: KRAFTON
- **Venue**: arXiv preprint (2506.03610v3)
- **Abstract**: Presents Orak, a benchmark for training and evaluating LLM agents across 12 popular video games spanning all major genres. Uses plug-and-play MCP-based interface for reproducible studies of agentic modules. Releases fine-tuning dataset of expert LLM gameplay trajectories. Offers united evaluation framework including game leaderboards, LLM battle arenas, and ablation studies of input modality, agentic strategies, and fine-tuning effects.
- **Key innovation**: First comprehensive game benchmark with MCP-based interface; expert trajectory fine-tuning dataset; systematic evaluation across 12 genres.
- **Link**: https://arxiv.org/abs/2506.03610

### DSGBench: A Diverse Strategic Game Benchmark for Evaluating LLM-based Agents
- **Authors**: Wenjie Tang, Yuan Zhou, Erqiang Xu, Keyan Cheng, Minne Li, Liquan Xiao
- **Affiliation**: -
- **Venue**: arXiv preprint (2503.06047v2, updated May 2026)
- **Abstract**: Introduces DSGBench, a rigorous evaluation platform for strategic decision-making with six complex strategic games. Employs fine-grained evaluation scoring across five dimensions with automated decision-tracking. Evaluates six popular LLM agents (open-source and closed-source), identifying distinct strengths and limitations.
- **Key innovation**: Multi-dimensional evaluation (5 dimensions) for strategic LLM agent assessment; decision trajectory analysis.
- **Link**: https://arxiv.org/abs/2503.06047

## 6. Industry Game AI

### Augmenting Game AI with Deep Reinforcement Learning
- **Authors**: Alessandro Sestini et al.
- **Affiliation**: -
- **Venue**: Conference on Games 2026 (vision paper)
- **Abstract**: Vision paper surveying RL applications for game AI deployment. Proposes a framework for training RL models with requirements suited toward game AI and game development. Presents examples of RL-augmented game AI and practicalities of deploying player-facing ML agents in modern games. Identifies bottlenecks: believability vs optimality, sample efficiency, and generalization.
- **Key innovation**: Genre-level readiness framework for RL game AI deployment; practical bottlenecks for production game AI.
- **Link**: https://arxiv.org/abs/2606.20210

### GameNGen: Diffusion Models Are Real-Time Game Engines
- **Authors**: Dani Valevski, Yaniv Leviathan, Moab Arar, Shlomi Fruchter
- **Affiliation**: Google
- **Venue**: ICLR 2025
- **Abstract**: Presents GameNGen, the first game engine powered entirely by a neural model enabling real-time interaction with DOOM. Runs at 20 FPS on a single TPU. Two-phase training: (1) RL agent learns to play the game, (2) diffusion model trained for next-frame prediction conditioned on past frames and actions. Human raters only slightly better than chance at distinguishing simulation from game.
- **Key innovation**: First fully neural game engine; diffusion model for real-time interactive game simulation at 20 FPS.
- **Link**: https://arxiv.org/abs/2408.14837

### MLOps Architectures for Real-Time Game AI Deployment
- **Authors**: Charles James et al.
- **Affiliation**: -
- **Venue**: ResearchGate publication (Feb 2026)
- **Abstract**: Comprehensive examination of MLOps architectures tailored for real-time game AI deployment. Examines cloud-native design, edge-cloud integration, observability-driven optimization, and automation pipelines for low-latency inference, continuous model improvement, and high availability in live game environments.
- **Key innovation**: Structured MLOps framework for game AI covering architecture, operational workflows, and feedback mechanisms.
- **Link**: https://www.researchgate.net/publication/398849408

### NVIDIA ACE & NVIGI: In-Game Inference SDK
- **Affiliation**: NVIDIA
- **Venue**: Production SDK (2025–2026)
- **Abstract**: NVIDIA's ACE (Avatar Cloud Engine) and NVIGI SDK enable on-device AI inference for game characters. Powers NPC dialogue, team coordination (PUBG Ally by KRAFTON), adaptive enemy behavior (MIR5), and social agents (inZOI Smart Zois). Small on-device models optimized for gaming hardware with inference alongside graphics workload.
- **Key innovation**: Production-grade on-device LLM inference for game NPCs; ACE Unreal Engine 5 plugins for end-to-end AI character pipeline.
- **Link**: https://developer.nvidia.com/ace-for-games

## 7. Related Techniques

### Self-Play & Multi-Agent RL

#### A Survey on Self-play Methods in Reinforcement Learning
- **Authors**: Ruize Zhang, Zelai Xu, Chengdong Ma, Chao Yu, Wei-Wei Tu, Wenhao Tang, Shiyu Huang, Deheng Ye, Wenbo Ding, Yaodong Yang, Yu Wang
- **Affiliation**: Tsinghua University, 4Paradigm, Zhipu AI, Tencent, Peking University
- **Venue**: arXiv preprint (2408.01072v3)
- **Abstract**: Comprehensive survey clarifying preliminaries of self-play in RL, providing a unified framework classifying existing self-play algorithms. Bridges gap between algorithms and practical implications across different scenarios.
- **Key innovation**: Unified classification framework for self-play methods in MARL.
- **Link**: https://arxiv.org/abs/2408.01072

### Curiosity-Driven Exploration

#### Curiosity-driven Exploration Based on Hierarchical Vision Transformer for DRL with Sparse Rewards
- **Authors**: Wanting Jiang, Guanwei Liu, Quanyang Leng, Nan Guo
- **Affiliation**: Northeastern University
- **Venue**: Neurocomputing, Vol 639 (Jul 2025)
- **Abstract**: Proposes DiNAT-RCM, a curiosity model based on Dilated Neighborhood Attention Transformer (DiNAT) for efficient state feature learning. Uses hierarchical vision Transformer with AW-A2C (attention-weighted advantage actor-critic). Surpasses RND by 16.25% in reward metrics on Atari 2600.
- **Key innovation**: Hierarchical vision Transformer for curiosity-driven exploration; attention-weighted advantage actor-critic for action space filtering.
- **Link**: https://doi.org/10.1016/j.neucom.2025.130252

#### CERMIC: Curiosity-Driven Exploration through Multi-Agent Contextual Calibration
- **Authors**: Yiyuan Pan et al.
- **Affiliation**: -
- **Venue**: arXiv preprint (2509.20648v3)
- **Abstract**: Proposes CERMIC, a curiosity framework for MARL that filters noisy surprise signals and guides exploration by dynamically calibrating intrinsic curiosity with inferred multi-agent context. Generates theoretically-grounded intrinsic rewards for state transitions with high information gain. Outperforms SoTA on VMAS, Meltingpot, and SMACv2.
- **Key innovation**: Multi-agent contextual calibration for curiosity; distinguishes environmental stochasticity from meaningful novelty.
- **Link**: https://arxiv.org/abs/2509.20648

#### Curiosity Driven Multi-agent Reinforcement Learning for 3D Game Testing
- **Authors**: Raihana Ferdous, Fitsum Kifetew, Davide Prandi, Angelo Susi
- **Affiliation**: -
- **Venue**: A-TEST Workshop @ ICST 2025
- **Abstract**: Presents cMarlTest, a curiosity-driven MARL approach for testing 3D games. Deploys multiple collaborative agents achieving higher coverage than single-agent approaches across three coverage criteria, with better time efficiency.
- **Key innovation**: Curiosity-driven multi-agent testing for 3D games; collaborative coverage optimization.
- **Link**: https://arxiv.org/abs/2502.14606

#### CDE: Curiosity-Driven Exploration for Efficient RL in Large Language Models
- **Authors**: Runpeng Dai et al.
- **Affiliation**: -
- **Venue**: arXiv preprint (2509.09675)
- **Abstract**: Introduces Curiosity-Driven Exploration (CDE) for RLVR in LLMs, using perplexity (actor) and value variance (critic) as exploration bonuses. Achieves ~+3 point improvement over standard GRPO/PPO on AIME benchmarks.
- **Key innovation**: Dual-signal curiosity (actor perplexity + critic variance) for LLM RL exploration.
- **Link**: https://arxiv.org/abs/2509.09675

### Hierarchical RL

#### ARISE: Agent Reasoning with Intrinsic Skill Evolution in Hierarchical Reinforcement Learning
- **Authors**: Yu Li, Rui Miao, Zhengling Qi, Tian Lan
- **Affiliation**: -
- **Venue**: arXiv preprint (2603.16060, Mar 2026)
- **Abstract**: Introduces ARISE, a hierarchical RL framework with Skills Manager (high-level) and Worker (low-level) for mathematical reasoning. Manager maintains tiered skill library through skill generation rollout with structured summarization, using policy-driven selection. Consistently outperforms GRPO-family algorithms across competition math and Omni-MATH benchmarks.
- **Key innovation**: Hierarchical RL architecture with evolving skill library for reasoning; co-evolution of library quality and reasoning performance.
- **Link**: https://arxiv.org/abs/2603.16060

#### Hierarchical Reinforcement Learning with Targeted Causal Interventions
- **Authors**: Sadegh Khorasani, Saber Salehkaleybar, Negar Kiyavash, Matthias Grossglauser
- **Affiliation**: EPFL
- **Venue**: ICML 2025
- **Abstract**: Models subgoal structure as a causal graph in HRL. Proposes causal discovery algorithm to learn subgoal dependencies and prioritize interventions based on importance. Experiments in Minecraft environments. Outperforms existing HRL approaches in training cost with formal theoretical analysis.
- **Key innovation**: Causal discovery for HRL subgoal structure; targeted causal interventions for efficient long-horizon RL.
- **Link**: https://arxiv.org/abs/2507.04373

### Model-Based RL & World Models

#### Improving Transformer World Models for Data-Efficient RL
- **Authors**: Antoine Dedieu, Joseph Ortiz et al. (Google DeepMind)
- **Affiliation**: Google DeepMind
- **Venue**: arXiv preprint (2502.01591)
- **Abstract**: Achieves new SOTA (67.42% reward) on Craftax-classic benchmark, exceeding human performance (65.0%) and DreamerV3 (53.2%) after 1M steps. Three improvements: (a) Dyna with warmup, (b) nearest neighbor tokenizer on image patches, (c) block teacher forcing for joint future token reasoning.
- **Key innovation**: New SOTA on Craftax via improved Transformer world model design; nearest neighbor tokenizer + block teacher forcing.
- **Link**: https://arxiv.org/abs/2502.01591

#### Optimistic World Models: Efficient Exploration in Model-Based Deep RL
- **Authors**: Multiple authors
- **Affiliation**: -
- **Venue**: arXiv preprint (2602.10044)
- **Abstract**: Proposes optimistic exploration strategy for model-based RL by biasing world model predictions toward optimistic outcomes, encouraging exploration of uncertain states.
- **Key innovation**: Optimism bias injection into world model predictions for efficient exploration.
- **Link**: https://arxiv.org/abs/2602.10044

#### Learning Transformer-based World Models with Contrastive Predictive Coding
- **Authors**: Multiple authors
- **Affiliation**: -
- **Venue**: arXiv preprint (2503.04416)
- **Abstract**: Introduces TWISTER, a Transformer model-based RL algorithm using action-conditioned Contrastive Predictive Coding to learn high-level feature representations. World model transforms images into discrete stochastic states and simulates imaginary trajectories for actor-critic training.
- **Key innovation**: Contrastive Predictive Coding for Transformer world model representation learning.
- **Link**: https://arxiv.org/abs/2503.04416

### Offline RL for Games

#### Offline Fictitious Self-Play for Competitive Games
- **Authors**: Jingxiao Chen, Weiji Xie, Weinan Zhang, Yong Yu, Ying Wen
- **Affiliation**: -
- **Venue**: arXiv preprint (2403.00841)
- **Abstract**: Introduces Off-FSP, the first practical model-free offline RL algorithm for competitive games. Uses importance sampling to simulate interactions with various opponents from fixed datasets, enabling offline self-play learning. Combines single-agent offline RL with Fictitious Self-Play to approximate Nash equilibrium. Achieves significantly lower exploitability on matrix games, poker, and board games.
- **Key innovation**: First offline RL algorithm for competitive games combining importance sampling simulation with self-play; validated on real-world human-robot task.
- **Link**: https://arxiv.org/abs/2403.00841

#### Target Return Optimizer for Multi-Game Decision Transformer
- **Authors**: Kensuke Tatematsu, Akifumi Wachi
- **Affiliation**: -
- **Venue**: arXiv preprint (2503.02311, Mar 2025)
- **Abstract**: Proposes MTRO (Multi-Game Target Return Optimizer) to autonomously determine game-specific target returns for Multi-Game Decision Transformer using only offline datasets. No additional training required. Demonstrates enhanced performance on Atari games.
- **Key innovation**: Automated target return optimization for offline decision transformers without additional training.
- **Link**: https://arxiv.org/abs/2503.02311

### Reward Shaping

#### ARMS: Automatic Reward Shaping for Sparse-Reward Multi-Agent Reinforcement Learning
- **Authors**: Elie Abboud, Oren Gal
- **Affiliation**: -
- **Venue**: arXiv preprint (2605.23562, May 2026)
- **Abstract**: Proposes ARMS, a self-supervised reward shaping framework for MARL that learns dense shaping signals from sparse rewards through trajectory ranking. Reformulates policy invariance through conditional best-response reasoning, showing shaping rewards preserve best-response sets and Nash equilibria. Alternates between policy learning and reward learning with shared shaping parameters.
- **Key innovation**: First theoretically-grounded MARL reward shaping with Nash equilibrium preservation guarantee.
- **Link**: https://arxiv.org/abs/2605.23562

### Imitation Learning & Inverse RL

#### RILe: Reinforced Imitation Learning
- **Authors**: Berat Mert Albaba et al.
- **Affiliation**: -
- **Venue**: arXiv preprint (2406.08472v4, updated Apr 2025)
- **Abstract**: Introduces RILe, a trainer-student framework combining imitation learning and inverse RL for dense reward learning in high-dimensional tasks. Trainer learns adaptive reward function; student uses reward to imitate expert behaviors. Achieves near-expert performance in challenging robotic locomotion.
- **Key innovation**: Adaptive trainer-student framework bridging IL and IRL for dense reward acquisition.
- **Link**: https://arxiv.org/abs/2406.08472

#### Structured Imitation Learning of Interactive Policies through Inverse Games
- **Authors**: Max M. Sun, Todd Murphey
- **Affiliation**: -
- **Venue**: RSS 2025 Workshop
- **Abstract**: Introduces a structured IL framework for interactive policies by combining generative single-agent policy learning with game-theoretic structure. Separates learning into individual behavioral patterns via IL then inter-agent dependencies via inverse game problem. Significantly improves non-interactive policies in 5-agent social navigation.
- **Key innovation**: Game-theoretic structure injection into imitation learning for multi-agent interaction.
- **Link**: https://arxiv.org/abs/2511.12848
