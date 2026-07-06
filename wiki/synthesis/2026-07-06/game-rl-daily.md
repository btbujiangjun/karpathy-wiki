---
title: "Game RL & Game AI Bot — arXiv & Proceedings Daily (2026-07-06)"
type: synthesis
created: 2026-07-06
updated: 2026-07-06
sources: [arxiv.org, openreview.net, proceedings.mlr.press, openaccess.thecvf.com, dl.acm.org]
tags: [game-rl, game-ai, foundation-models, self-play, world-models, marl, pcg, benchmarks, llm-agents, industry]
---

# Game RL & Game AI Bot — arXiv & Proceedings Daily

> **2026-07-06** | Covers 25+ papers across 7 topics: Game RL, Game AI Bots, Game Foundation Models, PCG, Benchmarks, Industry Game AI, and Related Techniques.
> Searched: arXiv cs.AI/cs.LG/cs.CV/cs.MA, CVPR 2026, ICLR 2026, AAMAS 2025, IEEE TG, NeurIPS 2024-25.

---

## Table of Contents

1. [Game Foundation Models](#1-game-foundation-models)
2. [Self-Play & Multi-Agent Reasoning](#2-self-play--multi-agent-reasoning)
3. [World Models for Games](#3-world-models-for-games)
4. [Multi-Agent RL in Games](#4-multi-agent-rl-in-games)
5. [Game AI Bots & LLM-Powered NPCs](#5-game-ai-bots--llm-powered-npcs)
6. [Procedural Content Generation](#6-procedural-content-generation)
7. [Game Benchmarks & Evaluation](#7-game-benchmarks--evaluation)
8. [Industry Game AI](#8-industry-game-ai)
9. [Related Techniques](#9-related-techniques)
10. [Survey & Review Papers](#10-survey--review-papers)

---

## 1. Game Foundation Models

### 1.1 NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi "Jim" Fan
- **Affiliation**: NVIDIA, Stanford, Caltech, UChicago, UT Austin
- **Venue**: CVPR 2026
- **Abstract**: Introduces a vision-action foundation model for generalist gaming agents trained on 40,000 hours of gameplay videos across 1,000+ games. Three key ingredients: (1) internet-scale video-action dataset via automated action extraction from public gameplay videos, (2) multi-game benchmark for cross-game generalization, (3) unified vision-action model via large-scale behavior cloning. Shows competence in 3D combat, 2D platformers, and procedurally generated worlds. Up to 52% relative improvement on unseen games.
- **Key Innovation**: First open foundation model for generalist game playing; demonstrates that behavior cloning at scale produces cross-game transfer.
- **Links**: [arXiv:2601.02427](https://arxiv.org/abs/2601.02427) | [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/papers/Magne_NitroGen_An_Open_Foundation_Model_for_Generalist_Gaming_Agents_CVPR_2026_paper.pdf) | [Project](https://nitrogen.minedojo.org)

### 1.2 Scaling Behavior Climbing Improves Causal Reasoning: An Open Model for Real-Time Video Game Playing
- **Authors**: Yuguang Yue, Irakli Salia, Samuel Hunt, Chris Green, Wenzhe Shi, Jonathan J Hunt
- **Affiliation**: (independent / corporate)
- **Venue**: arXiv 2026-01
- **Abstract**: Introduces an open recipe for training a video game playing foundation model designed for inference in realtime on a consumer GPU. Releases 8,300+ hours of high-quality human gameplay data, training/inference code, and checkpoints. Best model achieves performance competitive with human players across 3D games. Investigates scaling laws of behavior cloning with focus on causal reasoning — increasing training data and network depth leads to more causal policies. Validates findings at scale with models up to 1.2B parameters.
- **Key Innovation**: Open-source game playing foundation model with causal reasoning analysis; real-time inference on consumer GPU.
- **Links**: [arXiv:2601.04575](https://arxiv.org/abs/2601.04575)

### 1.3 Towards Generalist Game Players: An Investigation of Foundation Models in the Game Multiverse
- **Authors**: Kuan Zhang et al. (THUSI-Lab)
- **Affiliation**: Tsinghua University
- **Venue**: arXiv 2026-05
- **Abstract**: Comprehensive survey/review proposing a four-era evolutionary framework, a four-pillar pipeline (Dataset, Model, Harness, Benchmark), five fundamental trade-offs, and a five-level roadmap for generalist game-playing AI. Traces evolution from symbolic systems → DRL specialists → large foundation models as generalist players → future "creator" stage where agent creates new game worlds. Provides unified lens onto the rapidly shifting field.
- **Key Innovation**: End-to-end framework for understanding and building generalist game players; roadmap from single-game mastery to AGI-level game intelligence.
- **Links**: [arXiv:2605.09965](https://arxiv.org/abs/2605.09965) | [GitHub](https://github.com/THUSI-Lab/Awesome-LFMs-Play-Games)

---

## 2. Self-Play & Multi-Agent Reasoning

### 2.1 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning
- **Authors**: Bo Liu, Leon Guertler, Simon Yu, Zichen Liu, Penghui Qi, Daniel Balcells, Mickel Liu, Cheston Tan, Weiyan Shi, Min Lin, Wee Sun Lee, Natasha Jaques
- **Affiliation**: (multiple; includes Google DeepMind alum)
- **Venue**: ICLR 2026
- **Abstract**: Self-play framework where LLMs learn by playing multi-turn zero-sum games against continuously improving versions of themselves. Generates infinite curriculum of progressively challenging problems. Introduces role-conditioned advantage estimation (RAE) to stabilize multi-agent training. Training Qwen3-4B-Base on Kuhn Poker alone achieves 8.6% improvement on math and 8.4% on general reasoning. Multi-game training (TicTacToe, Kuhn Poker, Simple Negotiation) further enhances performance. Applied to DeepSeek-R1-Distill-Qwen-7B yields 2.0% average improvement.
- **Key Innovation**: Self-play on games transfers to general reasoning; RAE for stable multi-agent RL training of LLMs.
- **Links**: [arXiv:2506.24119](https://arxiv.org/abs/2506.24119)

### 2.2 MARSHAL: Incentivizing Multi-Agent Reasoning via Self-Play with Strategic LLMs
- **Authors**: (multiple authors; Tsinghua University)
- **Affiliation**: Tsinghua University
- **Venue**: arXiv 2025-10
- **Abstract**: End-to-end RL framework for multi-turn, multi-agent scenarios. Features turn-level advantage estimator for credit assignment and agent-specific advantage normalization. Agents trained from Qwen3-4B develop strong strategic abilities in cooperative and competitive games, with up to 28.7% performance improvements on held-out games.
- **Key Innovation**: End-to-end multi-agent RL for LLMs; turn-level credit assignment.
- **Links**: [arXiv:2510.15414](https://arxiv.org/abs/2510.15414)

### 2.3 Data-Augmented Game Starts (DAGS) for Accelerating Self-Play Exploration in Imperfect Information Games
- **Authors**: JB Lanier, Nathan Monette, Pierre Baldi, Roy Fox
- **Affiliation**: UC Irvine
- **Venue**: arXiv 2026-05
- **Abstract**: Multi-agent starting-state sampling strategy to accelerate online exploration in regularized policy-gradient methods for 2p0s games. Uses offline demonstrations from skilled humans to initialize RL data collection at intermediate states. Evaluated on synthetic datasets, Kuhn Poker, Goofspiel. Under fixed computational budgets, DAGS achieves lower exploitability. Releases new benchmark environments that increase exploration challenges in OpenSpiel.
- **Key Innovation**: Demonstration-guided state initialization for self-play; addresses exploration challenges in large imperfect-information games (StarCraft, Dota scale).
- **Links**: [arXiv:2605.14379](https://arxiv.org/abs/2605.14379)

### 2.4 PolicyEvolve: Evolving Programmatic Policies by LLMs for Multi-Player Games via Population-Based Training
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2025-09
- **Abstract**: Framework for multi-agent tasks that enables policy generation and improvement without human intervention. Maintains global policy pool (elite policies) and local policy pool. Policy Planner generates candidate policies; Trajectory Critic analyzes interaction data. Policies evolve through population-based self-play against the global pool. Validated on multi-player zero-sum games across diverse LLMs. Produces high-quality white-box programmatic policies through minimal environmental exploration.
- **Key Innovation**: LLM-driven programmatic policy evolution with population-based training for multi-agent games.
- **Links**: [arXiv:2509.06053](https://arxiv.org/abs/2509.06053)

---

## 3. World Models for Games

### 3.1 Dreamer 4: Training Agents Inside of Scalable World Models
- **Authors**: Danijar Hafner, Wilson Yan, Timothy Lillicrap
- **Affiliation**: Google DeepMind
- **Venue**: arXiv 2025-09
- **Abstract**: Dreamer 4 is a scalable agent that learns to solve control tasks via RL inside a fast and accurate world model. In Minecraft, it accurately predicts object interactions and game mechanics, outperforming previous world models by a large margin. Real-time interactive inference on a single GPU via shortcut forcing objective and efficient transformer architecture. First agent to obtain diamonds in Minecraft purely from offline data (0.7% success rate, 21 FPS on single GPU). Requires sequences of over 20,000 mouse/keyboard actions from raw pixels.
- **Key Innovation**: Shortcut forcing for efficient world model training; first offline diamond acquisition in Minecraft; learns from unlabeled videos + small action-labeled data.
- **Links**: [arXiv:2509.24527](https://arxiv.org/abs/2509.24527) | [Project](https://danijar.com/dreamer4/)

### 3.2 Matrix-Game: Interactive World Foundation Model
- **Authors**: Yifan Zhang et al.
- **Affiliation**: SkyworkAI
- **Venue**: arXiv 2025-06
- **Abstract**: Interactive world foundation model for controllable game world generation. Two-stage pipeline: large-scale unlabeled pretraining for environment understanding, then action-labeled training for interactive video generation. Curates Matrix-Game-MC dataset (2,700+ hours unlabeled, 1,000+ hours labeled with keyboard/mouse annotations). Adopts controllable image-to-world generation paradigm conditioned on reference image, motion context, and user actions. 17B parameters. Introduces GameWorld Score benchmark. Outperforms Oasis and MineWorld on all metrics.
- **Key Innovation**: Largest Minecraft world model (17B params); fine-grained action controllability; comprehensive benchmark.
- **Links**: [arXiv:2506.18701](https://arxiv.org/abs/2506.18701) | [GitHub](https://github.com/SkyworkAI/Matrix-Game)

### 3.3 MineWorld: A Real-Time and Open-Source Interactive World Model on Minecraft
- **Authors**: Junliang Guo, Yang Ye, Tianyu He, Haoyu Wu, Yushu Jiang, Tim Pearce, Jiang Bian
- **Affiliation**: Microsoft Research
- **Venue**: arXiv 2025-04
- **Abstract**: Real-time interactive world model on Minecraft driven by a visual-action autoregressive Transformer. Transforms visual scenes and actions into discrete token IDs (image tokenizer + action tokenizer), trains with next token prediction. Novel parallel decoding algorithm predicts spatial redundant tokens simultaneously, enabling 4-7 FPS for real-time interaction. New metrics for evaluating both visual quality and action following. Outperforms SOTA open-source diffusion-based world models.
- **Key Innovation**: First open-source real-time interactive world model for Minecraft; parallel decoding for spatial tokens.
- **Links**: [arXiv:2504.08388](https://arxiv.org/abs/2504.08388) | [Project](https://aka.ms/mineworld)

### 3.4 Agent World Model (AWM): Infinity Synthetic Environments for Agentic RL
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026-02
- **Abstract**: Open-source pipeline that synthesizes executable tool-use environments at scale. Analogous to learned world models in model-based RL but realized via code-driven environments rather than neural dynamics. Generates thousands of executable environments for training agentic LLMs via RL. Addresses scalability limitations of environment synthesis.
- **Key Innovation**: Code-driven environment synthesis for agentic RL training at scale.
- **Links**: [arXiv:2602.10090](https://arxiv.org/abs/2602.10090)

---

## 4. Multi-Agent RL in Games

### 4.1 GAWM: Global-Aware World Model for Multi-Agent Reinforcement Learning
- **Authors**: Meiqin Liu et al.
- **Affiliation**: (multiple)
- **Venue**: arXiv 2025-01
- **Abstract**: Model-based MARL method that enhances centralized world model's ability to achieve globally unified state representation. Uses additional Transformer architecture to fuse local observations from different agents under CTDE paradigm. Addresses distribution mismatch between pseudo data samples and real samples. Outperforms model-free and model-based approaches in SMAC.
- **Key Innovation**: Transformer-based global state fusion for model-based MARL; significant improvements in SMAC.
- **Links**: [arXiv:2501.10116](https://arxiv.org/abs/2501.10116)

### 4.2 Offline-to-Online Multi-Agent RL with Offline Value Function Memory and Sequential Exploration
- **Authors**: Hai Zhong, Xun Wang, Zhuoran Li, Longbo Huang
- **Affiliation**: Tsinghua University
- **Venue**: AAMAS 2025
- **Abstract**: Extends offline-to-online RL paradigm to multi-agent settings. Leverages offline data for initialization and online fine-tuning. Introduces offline value function memory to prevent catastrophic forgetting during online fine-tuning, and sequential exploration strategy for coordinated multi-agent exploration. Addresses non-stationarity and credit assignment in O2O MARL.
- **Key Innovation**: First principled approach to offline-to-online transfer in MARL.
- **Links**: [arXiv:2410.19450](https://arxiv.org/abs/2410.19450)

---

## 5. Game AI Bots & LLM-Powered NPCs

### 5.1 A Survey on Large Language Model-Based Game Agents
- **Authors**: Sihao Hu et al.
- **Affiliation**: Georgia Tech (DISL)
- **Venue**: ACM Computing Surveys, 2026
- **Abstract**: Up-to-date review of LLM-based game agents (LLMGAs) through a unified reference architecture. Single-agent level: memory, reasoning, perception-action interfaces. Multi-agent level: communication protocols, organizational models, coordination, role differentiation, large-scale social behaviors. Challenge-centered taxonomy linking six major game genres to dominant agent requirements (from low-latency control in action games to open-ended goal formation in sandbox worlds).
- **Key Innovation**: Unified reference architecture for LLM-based game agents; genre-requirement taxonomy.
- **Links**: [arXiv:2404.02039](https://arxiv.org/abs/2404.02039) | [GitHub](https://github.com/git-disl/awesome-LLM-game-agent-papers)

### 5.2 Interactive AI NPCs Powered by LLMs: Technical Report for the CPDC Challenge 2025
- **Authors**: Yitian Huang, Yuxuan Lei, Jianxun Lian, Hao Liao
- **Affiliation**: Shenzhen University, USTC, Microsoft Research Asia
- **Venue**: CPDC Challenge 2025 (1st place)
- **Abstract**: Winning solution for the Commonsense Persona-Grounded Dialogue Challenge (CPDC 2025). Context Engineering: dynamic tool pruning and persona clipping for input compression, post-processing for parameter normalization. GPU Track: adopted GRPO training (RL directly optimized by reward signals) instead of SFT, mitigating small-sample overfitting. Ranked 1st in Task 2 API, 2nd in Task 1 API, 3rd in Task 3 and GPU track.
- **Key Innovation**: GRPO for NPC dialogue; context engineering for LLM game agents.
- **Links**: [arXiv:2511.20200](https://arxiv.org/abs/2511.20200)

### 5.3 LLM-Driven NPCs: Cross-Platform Dialogue System for Games and Social Platforms
- **Authors**: Li Song
- **Affiliation**: (independent)
- **Venue**: arXiv 2025-04
- **Abstract**: Prototype system enabling LLM-powered NPCs to communicate with players both in-game (Unity) and on social platforms (Discord). Dialogue logs stored in cloud database (LeanCloud) for cross-platform memory synchronization. Includes favorability mechanism shaping NPC responses based on interaction history.
- **Key Innovation**: Cross-platform NPC dialogue with persistent memory across game and social platforms.
- **Links**: [arXiv:2504.13928](https://arxiv.org/abs/2504.13928)

### 5.4 Playing DOOM with 1.3M Parameters: Specialized Small Models vs Large Language Models for Real-Time Game Control
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026-04
- **Abstract**: Compares specialized small models (1.3M params) against large language models for real-time DOOM gameplay. Small model uses hash embeddings, character-level tokenization of ASCII game frames, attention pooling, and 5 transformer layers. Achieves competitive gameplay with dramatically lower compute. Systematic comparison reveals small specialized models can match or exceed LLM performance in real-time game control tasks.
- **Key Innovation**: Demonstrates tiny specialized models can rival LLMs for real-time game control; practical insights for deployment.
- **Links**: [arXiv:2604.07385](https://arxiv.org/abs/2604.07385)

---

## 6. Procedural Content Generation

### 6.1 PCGRLLM: Large Language Model-Driven Reward Design for Procedural Content Generation Reinforcement Learning
- **Authors**: In-Chang Baek, Sung-Hyun Kim, Sam Earle, Zehua Jiang, Jin-Ha Noh, Julian Togelius, Kyung-Joong Kim
- **Affiliation**: NYU / (multiple Korean institutions)
- **Venue**: IEEE Transactions on Games (accepted)
- **Abstract**: Extends earlier PCGRL+ work with LLM-driven reward design. Uses feedback mechanism and reasoning-based prompt engineering (Tree-of-Thought, Graph-of-Thought). Evaluated on story-to-reward generation task in 2D environment. Achieves 415% and 40% improvements over baselines depending on LLM zero-shot capabilities. Demonstrates potential to reduce human dependency in game AI reward design.
- **Key Innovation**: LLM as reward engineer for PCGRL; ToT/GoT reasoning for reward generation; feedback-based refinement.
- **Links**: [arXiv:2502.10906](https://arxiv.org/abs/2502.10906)

### 6.2 IPCGRL: Language-Instructed Reinforcement Learning for Procedural Level Generation
- **Authors**: In-Chang Baek, Sung-Hyun Kim, Seo-Young Lee, Dong-Hyeon Kim, Kyung-Joong Kim
- **Affiliation**: (Korean institutions)
- **Venue**: IEEE Conference on Games 2025
- **Abstract**: Instruction-based PCG via RL incorporating a sentence embedding model. Fine-tunes task-specific embedding representations to compress game-level conditions. Up to 21.4% improvement in controllability and 17.2% in generalizability for unseen instructions. Extends modality of conditional input for PCG.
- **Key Innovation**: Natural language instruction for PCG-level generation; sentence embedding fine-tuning.
- **Links**: [arXiv:2503.12358](https://arxiv.org/abs/2503.12358)

### 6.3 Procedural Content Generation in Games: A Survey with Insights on Emerging LLM Integration
- **Authors**: Mahdi Farrokhi Maleki, Richard Zhao
- **Affiliation**: University of Calgary
- **Venue**: AIIDE-24 (AAAI)
- **Abstract**: Comprehensive survey of PCG algorithms: search-based, ML-based, noise functions, and LLMs. Compares methods by content type and publication date. Identifies gaps and suggests future directions. Key insight: LLMs have disrupted the trajectory of PCG advancement.
- **Key Innovation**: First survey to comprehensively cover LLM integration in PCG.
- **Links**: [arXiv:2410.15644](https://arxiv.org/abs/2410.15644) | [DOI: 10.1609/aiide.v20i1.31877](https://doi.org/10.1609/aiide.v20i1.31877)

---

## 7. Game Benchmarks & Evaluation

### 7.1 DSGBench: A Diverse Strategic Game Benchmark for Evaluating LLM-based Agents in Complex Decision-Making
- **Authors**: Wenjie Tang et al.
- **Affiliation**: (multiple)
- **Venue**: arXiv 2025-03 (updated 2026-05)
- **Abstract**: Rigorous evaluation platform with six complex strategic games for long-term, multi-dimensional decision-making. Fine-grained scoring across five dimensions. Automated decision-tracking mechanism for in-depth behavior analysis. Evaluates six popular LLM agents (open-source and closed-source), revealing distinct strengths and systemic limitations.
- **Key Innovation**: Multi-dimensional strategic game benchmark with decision trajectory analysis for LLM agents.
- **Links**: [arXiv:2503.06047](https://arxiv.org/abs/2503.06047)

### 7.2 TowerMind: A Tower Defence Game Learning Environment and Benchmark for LLM as Agents
- **Authors**: Dawei Wang, Chengming Zhou, Di Zhao, Xinyuan Liu, Marci Chi Ma, Gary Ushaw, Richard Davison
- **Affiliation**: Newcastle University
- **Venue**: arXiv 2026-01
- **Abstract**: Tower Defence game environment as a subclass of RTS for LLM agent evaluation. Provides computationally efficient alternative to SC2LE/SMAC while preserving RTS-style challenges. Supports multimodal observations. Benchmarks LLM agents alongside traditional DRL (DQN, PPO). Demonstrates that TowerMind is a challenging environment broadening RL benchmark diversity.
- **Key Innovation**: Lightweight RTS-style benchmark for LLM agents; bridges TD games and AI research.
- **Links**: [arXiv:2601.05899](https://arxiv.org/abs/2601.05899)

---

## 8. Industry Game AI

### 8.1 NVIDIA ACE: Autonomous Game Characters Platform
- **Affiliation**: NVIDIA
- **Announced**: CES 2025 / GDC 2026
- **Description**: Full-stack platform for AI-powered game characters. Expanded from conversational NPCs to autonomous game characters that perceive, plan, and act like human players. Key components: (1) ACE Small Language Models (SLMs) optimized for planning at human-like frequencies, (2) Multi-modal SLMs for vision/audio perception, (3) In-Game Inferencing (NVIGI) SDK for on-device inference with compute-in-graphics (CIG) technology, (4) Game Agent SDK for native C/C++ integration. Partners include PUBG: BATTLEGROUNDS, inZOI, NARAKA: BLADEPOINT, MIR5.
- **Key Innovation**: First production deployment of LLM-powered autonomous NPCs in major titles; on-device SLM inference for real-time game AI.
- **Links**: [NVIDIA ACE](https://developer.nvidia.com/ace) | [NVIGI SDK](https://developer.nvidia.com/rtx/in-game-inferencing) | [GDC 2026 coverage](https://developer.nvidia.com/blog/bring-nvidia-ace-ai-characters-to-games-with-the-new-in-game-inference-sdk/)

### 8.2 Inworld AI — NPC Intelligence Platform
- **Affiliation**: Inworld AI ($120M raised, $500M valuation)
- **Status**: Production 2025-2026
- **Description**: Provides APIs for voice synthesis, emotional response modeling, and evolving personality systems. Integrates with Unity and Unreal Engine. NPCs develop relationships, hold grudges, adapt personality based on context. Used by major game studios for conversational NPCs.
- **Key Innovation**: Emotional state machines + LLM for persistent NPC personality.

### 8.3 Ubisoft NEO NPC
- **Affiliation**: Ubisoft
- **Status**: Announced 2025-2026
- **Description**: First-party AAA NPC AI system for Ubisoft open-world titles. NPCs answer unprompted questions about game world, generate contextual quests based on local events, maintain faction allegiances that shift dynamically. Integrates narrative grounding to prevent lore-breaking.

---

## 9. Related Techniques

### 9.1 CDE: Curiosity-Driven Exploration for Efficient RL in Large Language Models
- **Authors**: Runpeng Dai, Linfeng Song, Haolin Liu, Zhenwen Liang, Dian Yu, Haitao Mi, Zhaopeng Tu, Rui Liu, Tong Zheng, Hongtu Zhu, Dong Yu
- **Affiliation**: Tencent AI Lab
- **Venue**: arXiv 2025-09
- **Abstract**: Curiosity-Driven Exploration framework using signals from both actor (perplexity over generated response) and critic (variance of value estimates from multi-head architecture). Both signals serve as exploration bonus within RLVR framework. Theoretical analysis shows actor-wise bonus penalizes overconfident errors. Achieves +3 point improvement over standard GRPO/PPO on AIME benchmarks.
- **Key Innovation**: Dual intrinsic motivation (actor + critic) for exploration in LLM RL training.
- **Links**: [arXiv:2509.09675](https://arxiv.org/abs/2509.09675)

### 9.2 Imitating Language via Scalable Inverse Reinforcement Learning
- **Authors**: Markus Wulfmeier, Michael Bloesch, Nino Vieillard, Arun Ahuja, Jorg Bornschein, Sandy Huang, Artem Sokolov, Matt Barnes, Guillaume Desjardins, Alex Bewley, Sarah Bechtle, Jost Tobias Springenberg, Nikola Momchev, Olivier Bachem, Matthieu Geist, Martin Riedmiller
- **Affiliation**: Google DeepMind
- **Venue**: NeurIPS 2024
- **Abstract**: Investigates IRL perspective for language model imitation. Reformulates inverse soft-Q-learning as temporal difference regularized extension of MLE. Creates principled connection between MLE and IRL. Shows clear advantages for IRL-based imitation in retaining diversity while maximizing task performance.
- **Key Innovation**: Scalable IRL for language; bridges supervised fine-tuning and RLHF via principled IRL formulation.
- **Links**: [arXiv:2409.01369](https://arxiv.org/abs/2409.01369)

### 9.3 Policy-Driven World Model Adaptation for Robust Offline Model-based RL
- **Authors**: Jiayu Chen, Le Xu, Aravind Venugopal, Jeff Schneider
- **Affiliation**: CMU
- **Venue**: arXiv 2025-05 (updated 2026-01)
- **Abstract**: Addresses objective mismatch in offline MBRL where world model is not optimized for policy learning. Proposes framework that dynamically adapts world model alongside policy under unified maximin objective. Uses Stackelberg learning dynamics. Theoretical analysis with computationally efficient implementations.
- **Key Innovation**: Maximin optimization for world model adaptation; Stackelberg learning for offline MBRL.
- **Links**: [arXiv:2505.13709](https://arxiv.org/abs/2505.13709)

### 9.4 Is Behavior Cloning All You Need? Understanding Horizon in Imitation Learning
- **Authors**: Dylan J. Foster, Adam Block, Dipendra Misra
- **Affiliation**: Microsoft Research / MIT
- **Venue**: NeurIPS 2024
- **Abstract**: Revisits the gap between offline and online IL. Shows through new analysis of BC with logarithmic loss that horizon-independent sample complexity is achievable in offline IL under controlled payoff range and certain complexity measures. Provides theoretical foundation for BC at scale.
- **Key Innovation**: Theoretical proof that BC can achieve horizon-independent sample complexity under realizable conditions.
- **Links**: [arXiv:2407.15007](https://arxiv.org/abs/2407.15007)

---

## 10. Survey & Review Papers

### 10.1 A Comprehensive Review of Multi-Agent Reinforcement Learning in Video Games
- **Authors**: Zhengyang Li, Qijin Ji, Xinghong Ling, Quan Liu
- **Affiliation**: (multiple)
- **Venue**: IEEE Transactions on Games, 2025
- **Abstract**: Thorough examination of MARL from turn-based two-agent games to real-time multi-agent video games (Sports, FPS, RTS, MOBA). Analyzes challenges: nonstationarity, partial observability, sparse rewards, team coordination, scalability. Highlights implementations in Rocket League, Minecraft, Quake III Arena, StarCraft II, Dota 2, Honor of Kings. Proposes novel method to estimate game complexity.
- **Key Innovation**: Game complexity estimation method; comprehensive genre-by-genre MARL analysis.
- **Links**: [arXiv:2509.03682](https://arxiv.org/abs/2509.03682)

### 10.2 A Survey on Self-play Methods in Reinforcement Learning
- **Authors**: Ruize Zhang, Zelai Xu, Chengdong Ma, Chao Yu, Wei-Wei Tu, Wenhao Tang, Shiyu Huang, Deheng Ye, Wenbo Ding, Yaodong Yang, Yu Wang
- **Affiliation**: Tsinghua University, Peking University, 4Paradigm, Zhipu AI, Tencent
- **Venue**: arXiv 2024-08 (updated 2025-10)
- **Abstract**: Comprehensive roadmap of self-play methods. Unified framework classifying existing self-play algorithms. Bridges algorithms and practical implications across non-cooperative scenarios. Covers applications from Go, poker, and video games to multi-agent RL.
- **Key Innovation**: Unified taxonomy of self-play methods; practical implications across game scenarios.
- **Links**: [arXiv:2408.01072](https://arxiv.org/abs/2408.01072)

### 10.3 A General Review of Large Language Model Agents in Game Applications
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: ICCSIT 2025 (ACM)
- **Abstract**: Review of LLM agents across game paradigms: social reasoning, strategy, action execution, narrative interaction. Finds no single LLM architecture excels in all game dimensions. Recommends modular systems with symbolic reasoning, memory augmentation, emotionally grounded language models, and domain-specific fine-tuning.
- **Key Innovation**: Systematic evaluation of LLM agents across game paradigms; modular architecture recommendations.
- **Links**: [ACM DL](https://dl.acm.org/doi/10.1145/3783862.3783876)

### 10.4 Reinforcement Learning in Strategy-Based and Atari Games: A Review of Google DeepMind's Innovations
- **Authors**: Abdelrhman Shaheen, Anas Badr, Ali Abohendy, Hatem Alsaadawy, Nadine Alsayad, Ehab H. El-Shazly
- **Affiliation**: (multiple)
- **Venue**: arXiv 2025-02
- **Abstract**: Reviews AlphaGo, AlphaGo Zero, and MuZero. Discusses MiniZero, multi-agent models, and future directions. Covers training processes, challenges, and improvements.
- **Links**: [arXiv:2502.10303](https://arxiv.org/abs/2502.10303)

---

## Key Trends

1. **Game Foundation Models Going Open-Source**: NitroGen (NVIDIA) and the scaling BC model represent a shift toward open-source game-playing foundation models, lowering the barrier for game AI research.
2. **Self-Play for LLM Reasoning**: SPIRAL and MARSHAL demonstrate that self-play in zero-sum games transfers to general reasoning abilities — a paradigm shift from game-specific training to general capability building.
3. **World Models Reach Minecraft Diamond**: Dreamer 4 (DeepMind) achieves the first offline diamond acquisition, while Matrix-Game (SkyworkAI) scales to 17B parameters — world models are becoming practical for complex game environments.
4. **LLMs for PCG Reward Design**: PCGRLLM and IPCGRL show LLMs can replace human reward engineering for procedural content generation, with Tree-of-Thought reasoning achieving human-comparable performance.
5. **Industry Deployment Accelerating**: NVIDIA ACE is now deployed in PUBG, inZOI, and NARAKA at production scale, marking the transition of LLM-powered NPCs from demo to real products.
6. **Benchmarks for LLM Agents in Games**: DSGBench and TowerMind fill the gap in systematic evaluation of LLM-based agents in complex game environments, with fine-grained scoring dimensions.
7. **Small Models Compete with LLMs for Game Control**: The DOOM study shows 1.3M parameter specialized models can match LLMs for real-time control, suggesting optimized small models may be the practical path for in-game AI deployment.
8. **Curiosity-Driven Exploration Returns**: CDE adapts classic intrinsic motivation ideas to LLM RL training, showing +3 point improvements on reasoning benchmarks — relevant for exploration in sparse-reward game environments.
