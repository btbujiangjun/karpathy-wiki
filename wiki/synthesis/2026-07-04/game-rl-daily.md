---
title: "Game RL & Game AI Bot — Daily Survey (2026-07-04)"
type: synthesis
created: 2026-07-04
updated: 2026-07-04
sources:
  - arxiv.org
tags: [game-rl, game-ai, game-foundation-models, pcrl, benchmarks, industry-game-ai, world-models, self-play, curiosity]
---

# Game RL & Game AI Bot — Daily Survey (2026-07-04)

> arXiv and recent proceedings scan for Game RL, Game AI Bots, Game Foundation Models, PCG, Benchmarks, Industry Game AI, and related techniques. Compiled 2026-07-04.

## 1. Game RL — Reinforcement Learning in Games

### QZero: Mastering the Game of Go with Self-play Experience Replay
- **Authors**: Jingbin Liu, Xuechun Wang
- **Affiliation**: NetEase AI Lab
- **Venue**: arXiv preprint (2601.03306)
- **Abstract**: Presents QZero, a model-free RL algorithm that forgoes MCTS during training and learns a Nash equilibrium policy through self-play and off-policy experience replay. Built upon entropy-regularized Q-learning using a single Q-value network. Trained tabula rasa for 5 months with 7 GPUs, achieving performance comparable to AlphaGo.
- **Key innovation**: First demonstration that model-free RL can master Go at a level comparable to model-based approaches like AlphaGo.
- **Link**: https://arxiv.org/abs/2601.03306

### A Comprehensive Review of Multi-Agent Reinforcement Learning in Video Games
- **Authors**: Zhengyang Li, Qijin Ji, Xinghong Ling, Quan Liu
- **Affiliation**: -
- **Venue**: arXiv preprint (2509.03682)
- **Abstract**: Comprehensive survey of MARL applications from turn-based two-agent games to real-time multi-agent video games including Sports, FPS, RTS, and MOBA games. Analyzes challenges: nonstationarity, partial observability, sparse rewards, team coordination, scalability. Highlights implementations in Rocket League, Minecraft, Quake III Arena, StarCraft II, Dota 2, Honor of Kings.
- **Key innovation**: Proposes a novel method to estimate game complexity and suggests future research directions.
- **Link**: https://arxiv.org/abs/2509.03682

### Reinforcement Learning in Strategy-Based and Atari Games: A Review of Google DeepMind's Innovations
- **Authors**: Abdelrhman Shaheen, Anas Badr, Ali Abohendy, Hatem Alsaadawy, Nadine Alsayad, Ehab H. El-Shazly
- **Affiliation**: Egypt-Japan University of Science and Technology (E-JUST)
- **Venue**: arXiv preprint (2502.10303)
- **Abstract**: Reviews DeepMind's AlphaGo, AlphaGo Zero, MuZero — their key innovations, training processes, and challenges. Discusses MiniZero and multi-agent models with future directions.
- **Key innovation**: Comprehensive review linking model-based, model-free, and deep Q-network approaches across strategy and Atari games.
- **Link**: https://arxiv.org/abs/2502.10303

### A Survey on Self-play Methods in Reinforcement Learning
- **Authors**: Ruize Zhang, Zelai Xu, Chengdong Ma, Chao Yu, Wei-Wei Tu, Wenhao Tang, Shiyu Huang, Deheng Ye, Wenbo Ding, Yaodong Yang, Yu Wang
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2408.01072, v4 updated Oct 2025)
- **Abstract**: Comprehensive survey on self-play methods in MARL. Provides a unified framework, classifies existing algorithms, bridges theory to practice in non-cooperative scenarios (Go, poker, video games). Highlights open challenges and future directions.
- **Link**: https://arxiv.org/abs/2408.01072

### Data-Augmented Game Starts for Accelerating Self-Play Exploration in Imperfect Information Games
- **Authors**: (DeepMind-affiliated)
- **Affiliation**: Google DeepMind
- **Venue**: arXiv preprint (2605.14379)
- **Abstract**: Introduces DAGS (Data-Augmented Game Starts), a technique augmenting self-play training with intermediate-state resets drawn from offline trajectories. Provides new benchmark games for two-player zero-sum settings with long horizons. Shows DAGS enables regularized policy gradient algorithms to solve larger games. Demonstrates belief bias from start-state augmentation in imperfect-information games and provides mitigation.
- **Key innovation**: Start-state augmentation for self-play in imperfect-information games.
- **Link**: https://arxiv.org/abs/2605.14379

### Dr. MAS: Stable Reinforcement Learning for Multi-Agent LLM Systems
- **Authors**: Lang Feng, Longtao Zheng, Shuo He, Fuxiang Zhang, Bo An
- **Affiliation**: -
- **Venue**: arXiv preprint (2602.08847)
- **Abstract**: Proposes a stable multi-agent RL framework for LLM-based agent systems, addressing training instability in multi-agent LLM coordination.
- **Link**: https://arxiv.org/abs/2602.08847

## 2. Game AI Bot — LLM-Powered Game Agents

### A Survey on Large Language Model-Based Game Agents (LLMGAs)
- **Authors**: Sihao Hu et al.
- **Affiliation**: Georgia Tech
- **Venue**: ACM Computing Surveys, 2026 (arXiv:2404.02039v5)
- **Abstract**: Up-to-date review of LLM-based game agents through a unified reference architecture. At single-agent level: memory, reasoning, perception-action interfaces. At multi-agent level: communication protocols, organizational models. Challenge-centered taxonomy linking six game genres to dominant agent requirements.
- **Key innovation**: Unified architecture for LLM game agents with genre-specific requirements.
- **Link**: https://arxiv.org/abs/2404.02039

### Exploring Decision-Making Capabilities of LLM Agents: An Experimental Study on Jump-Jump Game
- **Authors**: Juwu Li
- **Affiliation**: Jiangxi Teachers College
- **Venue**: arXiv preprint (2509.00483)
- **Abstract**: Designs an LLM Agent architecture (Perception, Reasoning, Action, Feedback modules) for real-time decision-making in a Jump-Jump game. Tests prompt engineering approaches for optimal jumping force.
- **Key innovation**: Modular LLM agent architecture for real-time physical game control.
- **Link**: https://arxiv.org/abs/2509.00483

### Agentic Reasoning for Large Language Models
- **Authors**: Tianxin Wei et al. (extensive author list)
- **Affiliation**: UIUC, Microsoft, etc.
- **Venue**: arXiv preprint (2601.12538)
- **Abstract**: Comprehensive survey on agentic reasoning across three dimensions: foundational (planning, tool use, search), self-evolving (feedback, memory, adaptation), and collective multi-agent reasoning (coordination, knowledge sharing). Distinguishes in-context reasoning from post-training reasoning.
- **Key innovation**: Three-dimensional taxonomy of agentic reasoning for LLMs.
- **Link**: https://arxiv.org/abs/2601.12538

### LLM-Driven NPCs: Cross-Platform Dialogue System for Games and Social Platforms
- **Authors**: Li Song
- **Affiliation**: -
- **Venue**: arXiv preprint (2504.13928)
- **Abstract**: Prototype system for LLM-powered NPCs that communicate across Unity game environments and Discord. Uses cloud database (LeanCloud) for synchronized memory. Includes favorability mechanism for context-aware responses.
- **Key innovation**: Cross-platform NPC dialogue with persistent memory synchronization.
- **Link**: https://arxiv.org/abs/2504.13928

### AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making
- **Authors**: (AgentGym team)
- **Affiliation**: -
- **Venue**: arXiv preprint (2509.00483 related)
- **Abstract**: Comprehensive framework for training LLM agents in multi-turn interactive decision-making through reinforcement learning. Focuses on long-horizon agent tasks.
- **Key innovation**: RL training framework for interactive LLM agents.
- **Link**: https://arxiv.org/abs/2509.00483 (related)

### GameGPT: Multi-agent Collaborative Framework for Game Development
- **Authors**: -
- **Affiliation**: -
- **Venue**: arXiv preprint
- **Abstract**: Specialized multi-agent system for game development addressing LLM limitations and temporal constraints of game development.
- **Key innovation**: Multi-agent collaboration for full game development pipeline.
- **Link**: https://arxiv.org/abs/2509.00483 (related)

## 3. Game Foundation Models

### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi "Jim" Fan
- **Affiliation**: NVIDIA, Stanford, Caltech, UChicago, UT Austin
- **Venue**: CVPR 2026 (arXiv:2601.02427)
- **Abstract**: Vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games. Uses automatically extracted player actions from gameplay videos (internet-scale dataset), multi-game benchmark environment, and unified vision-action model with large-scale behavior cloning. Achieves 52% relative improvement in task success rates on unseen games.
- **Key innovation**: First open foundation model for generalist gaming agents at scale, with released dataset and weights.
- **Link**: https://arxiv.org/abs/2601.02427

### Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents
- **Authors**: Zihao Wang, Xujing Li, Yining Ye, Junjie Fang et al. (27 authors)
- **Affiliation**: ByteDance Seed
- **Venue**: arXiv preprint (2510.23691)
- **Abstract**: Generalist game agent with unified keyboard-mouse action space, pre-trained on 500B+ tokens across OS, web, and simulation games. Key techniques: decaying continual loss for causal confusion reduction, Sparse-Thinking strategy for reasoning depth vs cost balance. Achieves ~2× success rate over prior SOTA on Minecraft, matches fresh humans in unseen web 3D games, outperforms GPT-5, Gemini-2.5-Pro, Claude-4-Sonnet in FPS benchmarks.
- **Key innovation**: Unified human-native action space enabling cross-domain generalization at scale.
- **Link**: https://arxiv.org/abs/2510.23691

### DreamerV3: Mastering Diverse Domains through World Models
- **Authors**: Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, Timothy Lillicrap
- **Affiliation**: Google DeepMind, University of Toronto
- **Venue**: arXiv preprint (2301.04104, 2023, updated 2024)
- **Abstract**: General algorithm based on world models that outperforms specialized methods across 150+ diverse tasks with fixed hyperparameters. First algorithm to collect diamonds in Minecraft from scratch without human data or curricula. Robustness via normalization, balancing, transformations.
- **Key innovation**: Single-configuration world model algorithm mastering Minecraft diamond challenge.
- **Link**: https://arxiv.org/abs/2301.04104

### Looped World Models
- **Authors**: (DeepMind/Google)
- **Affiliation**: Google DeepMind
- **Venue**: arXiv preprint (2606.18208)
- **Abstract**: Establishes iterative latent depth as a previously unexplored scaling axis for world models, orthogonal to model size and training data. Builds on RSSM/Dreamer family and Transformer-based world models (IRIS, Δ-IRIS, DIAMOND, EMERALD).
- **Key innovation**: Iterative latent depth as new scaling dimension for world models.
- **Link**: https://arxiv.org/abs/2606.18208

### DreamerV3-XP: Optimizing Exploration through Uncertainty
- **Authors**: -
- **Affiliation**: -
- **Venue**: arXiv preprint (2510.21418)
- **Abstract**: Extends DreamerV3 with enhanced exploration mechanisms through uncertainty-driven intrinsic motivation and replay buffer optimization. Evaluated on Atari100k and DeepMind Control benchmarks.
- **Key innovation**: Uncertainty-based exploration bonuses integrated into DreamerV3 architecture.
- **Link**: https://arxiv.org/abs/2510.21418

### Optimistic World Models: Efficient Exploration in Model-Based Deep RL
- **Authors**: -
- **Affiliation**: -
- **Venue**: arXiv preprint (2602.10044)
- **Abstract**: Proposes optimistic exploration for model-based RL through reward-biased maximum likelihood estimation (RBMLE), connecting exploration bonuses to well-established theoretical frameworks.
- **Key innovation**: Optimistic exploration principle applied to deep world models.
- **Link**: https://arxiv.org/abs/2602.10044

### GameNGen: Diffusion Models Are Real-Time Game Engines
- **Authors**: Dani Valevski, Yaniv Leviathan, Moab Arar, Shlomi Fruchter
- **Affiliation**: Google Research, Google DeepMind, Tel Aviv University
- **Venue**: ICLR 2025 (arXiv:2408.14837)
- **Abstract**: First game engine powered entirely by a neural model enabling real-time interaction with a complex environment. Runs DOOM at 20 FPS on a single TPU. Uses RL agent to record training sessions, then diffusion model for next-frame prediction conditioned on past frames and actions. Human raters slightly above chance at distinguishing simulation from real gameplay.
- **Key innovation**: Neural game engine replacing traditional game loop with diffusion-based simulation.
- **Link**: https://arxiv.org/abs/2408.14837

## 4. Procedural Content Generation

### PCGRLLM: Large Language Model-Driven Reward Design for Procedural Content Generation Reinforcement Learning
- **Authors**: In-Chang Baek, Sung-Hyun Kim, Sam Earle, Zehua Jiang, Jin-Ha Noh, Julian Togelius, Kyung-Joong Kim
- **Affiliation**: GIST (South Korea), New York University
- **Venue**: arXiv preprint (2502.10906, updated May 2026)
- **Abstract**: Extended architecture for LLM-driven reward function generation in PCGRL. Uses feedback mechanism and reasoning-based prompt engineering. Evaluated on story-to-reward generation in 2D environments. Achieves performance comparable to human-designed rewards.
- **Key innovation**: LLMs generate reward functions for PCG RL agents with human-comparable quality.
- **Link**: https://arxiv.org/abs/2502.10906

### IPCGRL: Language-Instructed Reinforcement Learning for Procedural Level Generation
- **Authors**: In-Chang Baek, Sung-Hyun Kim, Seo-Young Lee, Dong-Hyeon Kim, Kyung-Joong Kim
- **Affiliation**: GIST (South Korea)
- **Venue**: Conference on Games 2025 (arXiv:2503.12358)
- **Abstract**: Instruction-based PCG via RL incorporating sentence embedding models. Fine-tunes task-specific embedding representations for game-level conditions. Achieves 21.4% improvement in controllability and 17.2% in generalizability for unseen instructions.
- **Key innovation**: Fine-tuned language embeddings for controllable level generation via RL.
- **Link**: https://arxiv.org/abs/2503.12358

### Procedural Content Generation with LLMs (Survey)
- **Authors**: Maleki et al. (survey)
- **Affiliation**: -
- **Venue**: Emergent Mind topic survey (updated Dec 2025)
- **Abstract**: Comprehensive overview of PCG with LLMs covering symbolic, multi-modal, and agent-centric workflows. Includes hybrid approaches combining LLMs with RL and symbolic methods for enhanced scalability and controllability.
- **Key innovation**: Taxonomy of LLM-based PCG approaches; observation that hybrid LLM+RL+symbolic methods outperform pure LLM approaches.
- **Link**: https://www.emergentmind.com/topics/procedural-content-generation-with-llms

## 5. Game Benchmarks

### DSGBench: A Diverse Strategic Game Benchmark for Evaluating LLM-based Agents
- **Authors**: Wenjie Tang, Yuan Zhou, Erqiang Xu, Keyan Cheng, Minne Li, Liquan Xiao
- **Affiliation**: -
- **Venue**: arXiv preprint (2503.06047, updated May 2026)
- **Abstract**: Benchmark with six complex strategic games for evaluating LLM agents in long-horizon reasoning, multi-agent interaction, and decision-making under uncertainty. Fine-grained evaluation across five dimensions. Automated decision-tracking mechanism. Evaluates six popular LLM agents.
- **Key innovation**: Multi-dimensional evaluation with decision trajectory analysis.
- **Link**: https://arxiv.org/abs/2503.06047

### TowerMind: A Tower Defence Game Learning Environment and Benchmark for LLM as Agents
- **Authors**: Dawei Wang, Chengming Zhou, Di Zhao, Xinyuan Liu, Marci Chi Ma, Gary Ushaw, Richard Davison
- **Affiliation**: Newcastle University, University of Auckland
- **Venue**: AAAI 2026 Oral (arXiv:2601.05899)
- **Abstract**: Novel tower defense environment with low computational demands. Multimodal observation space (pixel, textual, structured game-state). Supports hallucination evaluation. Five benchmark levels testing various LLMs. Clear performance gap between LLMs and humans on planning/decision-making. Also benchmarks Ape-X DQN and PPO.
- **Key innovation**: Lightweight RTS-derived benchmark with hallucination evaluation built in.
- **Link**: https://arxiv.org/abs/2601.05899

### Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games
- **Authors**: Dongmin Park, Minkyu Kim, Beongjun Choi, Junhyuck Kim et al.
- **Affiliation**: KRAFTON, University of Wisconsin-Madison
- **Venue**: arXiv preprint (2506.03610, updated Apr 2026)
- **Abstract**: Benchmark with 12 popular video games spanning all major genres (Street Fighter III, Super Mario, Ace Attorney, Her Story, Pokémon Red, Darkest Dungeon, Minecraft, Stardew Valley, StarCraft II, Slay the Spire, Baba Is You, 2048). Plug-and-play MCP-based interface. Includes fine-tuning datasets for adapting pre-trained LLMs.
- **Key innovation**: Comprehensive 12-game benchmark with MCP interface and LLM fine-tuning datasets.
- **Link**: https://arxiv.org/abs/2506.03610

### OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics
- **Authors**: Mingxian Lin, Shengju Qian, Yuqi Liu, Yi-Hua Huang et al.
- **Affiliation**: University of Hong Kong, LIGHTSPEED, CUHK, Tsinghua University
- **Venue**: arXiv preprint (2606.09826)
- **Abstract**: Real-time benchmark of 12 newly built Unreal Engine 5 games spanning Solo (7), PvP (3), and Coop (2). Introduces Improvement Dynamics Curve (IDC) — agentic-reflection harness that refines skill prompts across rounds. Evaluates 12 VLM agents. Games built from scratch to avoid pre-training leakage.
- **Key innovation**: Multi-regime (Solo/PvP/Coop) UE5 benchmark with reflection-based improvement tracking.
- **Link**: https://arxiv.org/abs/2606.09826

### GameDevBench: Evaluating Agentic Capabilities Through Game Development
- **Authors**: Wayne Chi, Yixiong Fang, Arnav Yayavaram et al.
- **Affiliation**: CMU
- **Venue**: arXiv preprint (2602.11103)
- **Abstract**: First benchmark for evaluating agents on game development tasks. 132 tasks from web/video tutorials requiring multimodal understanding. Average solution requires 3× code changes vs prior benchmarks. Best agent solves only 54.5%. Introduces image/video-based feedback mechanisms, improving Claude Sonnet 4.5 from 33.3% to 47.7%.
- **Key innovation**: Multimodal game development benchmark; visual feedback for code agents.
- **Link**: https://arxiv.org/abs/2602.11103

### Evaluation and Benchmarking of LLM Agents: A Survey
- **Authors**: Mahmoud Mohammadi, Yipeng Li, Jane Lo, Wendy Yip
- **Affiliation**: -
- **Venue**: arXiv preprint (2507.21504)
- **Abstract**: Two-dimensional taxonomy organizing LLM agent evaluation by (1) objectives (behavior, capabilities, reliability, safety) and (2) process (interaction modes, datasets, metrics, tooling). Highlights enterprise-specific challenges.
- **Key innovation**: Systematic taxonomy for the fragmented LLM agent evaluation landscape.
- **Link**: https://arxiv.org/abs/2507.21504

## 6. Industry Game AI

### NVIDIA ACE for Games — Autonomous Game Characters
- **Affiliation**: NVIDIA
- **Overview**: ACE is a suite of AI technologies for speech, intelligence, and animation in games. Small language models optimized for gaming, on-device inference via NVIGI SDK. Partner integrations: PUBG Ally (KRAFTON, AI teammate with voice interaction), Total War: PHARAOH advisor (RAG on 1,200+ game data tables), inZOI Smart Zois (KRAFTON), MIR5 adaptive bosses (Wemade Next), Dead Meat interrogation game, NARAKA: BLADEPOINT.
- **Key innovation**: First production deployment of on-device LLM-based autonomous NPCs at scale in shipping titles (2026).
- **Link**: https://developer.nvidia.com/ace-for-games

### Real-Time AI Inference Patterns from the Gaming Industry
- **Author**: Connor Ludwig
- **Affiliation**: (Industry blog)
- **Date**: December 2025
- **Overview**: Industry patterns for real-time distributed AI in games. INFUSE engine architecture: Actors (local scope, NPC-level) and Directors (global scope, world-level coherence). Stateless inference with ~20-40k token inbound, ~100 outbound. Structured emergence balancing designer constraints with emergent outcomes.
- **Key innovation**: Actor/Director pattern; stateless real-time inference at 1-2s cycles.
- **Link**: https://cjlludwig.github.io/blog/real-time-ai-inference-patterns-gaming

### NVIDIA ACE Game Agent SDK Beta
- **Affiliation**: NVIDIA
- **Date**: June 2026
- **Overview**: Open source C/C++ agentic framework for in-game AI NPCs. Three core APIs: Agent API (stateful, multi-step tool-assisted reasoning), Chat API (stateless), RAG API (semantic+lexical+hybrid retrieval). On-device GeForce RTX optimization.
- **Key innovation**: Production-grade agentic framework for game AI with on-device inference.
- **Link**: https://developer.nvidia.com/blog/build-on-device-ai-companions-with-the-nvidia-ace-game-agent-sdk-and-unreal-engine-5-plugins/

## 7. Related Techniques

### Self-Play RL

**A Survey on Self-play Methods in Reinforcement Learning** (see Section 1 above).

### Curiosity-Driven Exploration

**CDE: Curiosity-Driven Exploration for Efficient Reinforcement Learning in Large Language Models**
- **Authors**: Runpeng Dai, Linfeng Song, Haolin Liu, Zhenwen Liang, Dian Yu, Haitao Mi, Zhaopeng Tu, Rui Liu, Tong Zheng, Hongtu Zhu, Dong Yu
- **Affiliation**: Tencent AI Lab / multiple institutions
- **Venue**: ICLR 2026 Poster
- **Abstract**: Framework leveraging intrinsic curiosity signals from both actor (perplexity over generated responses) and critic (variance of multi-head value estimates) within RLVR. ~+3 point improvement over standard GRPO/PPO on AIME. Theoretical analysis shows actor bonus penalizes overconfident errors; critic bonus connects to count-based exploration.
- **Key innovation**: Dual curiosity signals (actor perplexity + critic variance) for LLM reasoning RL.
- **Link**: https://openreview.net/forum?id=5rXN5knHKW

**CuES: A Curiosity-driven and Environment-grounded Synthesis Framework for Agentic RL**
- **Authors**: Shinji Mai, Yunpeng Zhai, Ziqian Chen et al.
- **Affiliation**: Alibaba
- **Venue**: arXiv preprint (2512.01311)
- **Abstract**: Addresses task scarcity in agentic RL by automatically generating diverse, executable tasks from environment structure via intrinsic curiosity. Demonstrates on AppWorld, BFCL, WebShop. Task distributions match or surpass manually curated datasets.
- **Key innovation**: Autonomous task generation for agentic RL via curiosity-driven exploration.
- **Link**: https://arxiv.org/abs/2512.01311

### Self-Imitation Learning

**SPEAR: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning**
- **Authors**: Yulei Qin et al. (15+ authors)
- **Affiliation**: -
- **Venue**: arXiv preprint (2509.22601)
- **Abstract**: Curriculum-based self-imitation learning for agentic LLMs. Extends SIL with progressive exploration scheduling: intrinsic rewards for skill-level exploration early, self-imitation for action-level exploitation later. Tool call reward critical for bootstrapping. Prevents entropy collapse via trajectory-level entropy control.
- **Key innovation**: Curriculum-guided self-imitation balancing exploration and exploitation in agentic LLM RL.
- **Link**: https://arxiv.org/abs/2509.22601

### Interleaved RL + Imitation Learning

**IN-RIL: Interleaved Reinforcement and Imitation Learning for Policy Fine-Tuning**
- **Authors**: Dechen Gao, Hang Wang, Hanchu Zhou et al.
- **Affiliation**: Arizona State University
- **Venue**: arXiv preprint (2505.10442)
- **Abstract**: Periodically injects IL updates after multiple RL updates for robotics policy fine-tuning. Gradient separation mechanisms prevent destructive interference. Significant improvements on 14 tasks across 3 benchmarks (FurnitureBench, OpenAI Gym, Robomimic) — from 12% to 88% success rate (6.3× improvement) on Robomimic Transport.
- **Key innovation**: Gradient separation for interleaved RL+IL; applicable to game policy fine-tuning.
- **Link**: https://arxiv.org/abs/2505.10442

### Tool-Use RL

**Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It**
- **Authors**: Yupu Hao, Zhuoran Jin, Huanxuan Liao, Kang Liu, Jun Zhao
- **Affiliation**: Chinese Academy of Sciences
- **Venue**: arXiv preprint (2606.26027)
- **Abstract**: Analysis of RL collapse in multi-step tool-use tasks for LLMs. Failure stems from probability spikes in control tokens. Interleaving SFT with RL substantially improves stability but degrades under OOD evaluation.
- **Key innovation**: Diagnosis of probability spike collapse; supervisory signal remedies for tool-use RL.
- **Link**: https://arxiv.org/abs/2606.26027

### World Models

**DreamerV3: Mastering Diverse Domains through World Models** (see Section 3)

**Looped World Models** (see Section 3)

**GameNGen: Diffusion Models Are Real-Time Game Engines** (see Section 3)

### Hierarchical RL in Games

**Hierarchical Reinforcement Learning and Value Optimization for Challenging Quadruped Locomotion**
- **Authors**: -
- **Venue**: arXiv preprint (2506.20036)
- **Abstract**: Hierarchical RL framework where high-level policy optimizes over footstep targets using low-level policy's value function. Removes need for additional environment samples beyond LLP training. Relevant pattern transferable to game NPC locomotion.
- **Key innovation**: Value-based HLP optimization using LLP value function, zero extra environment samples.
- **Link**: https://arxiv.org/abs/2506.20036

## Key Themes & Trends

1. **Generalist Game Foundation Models**: NVIDIA's NitroGen (CVPR 2026) and ByteDance's Game-TARS represent a paradigm shift from game-specific AI to foundation models capable of cross-game zero-shot transfer. Both released or plan to release weights/datasets.

2. **Self-Play as Reasoning Paradigm**: SPIRAL (ICLR 2026) and QZero demonstrate that self-play RL can bootstrap reasoning capabilities, extending beyond game-playing into general LLM reasoning.

3. **LLM-NPCs Entering Production**: NVIDIA ACE powered autonomous NPCs in PUBG (Ally), Total War: PHARAOH, inZOI, and MIR5 in 2026 — the first major deployment wave of LLM-driven NPCs in shipping titles.

4. **Benchmark Standardization**: Orak (12 games, MCP interface), OmniGameArena (12 UE5 games, Solo/PvP/Coop), TowerMind (TD for LLM eval), and GameDevBench (game dev for agent eval) provide comprehensive evaluation infrastructure.

5. **World Models for Games**: DreamerV3, GameNGen, and Looped World Models push the frontier of learned game simulation, with GameNGen demonstrating real-time neural game engines.

6. **Curiosity + RL for LLMs**: CDE (ICLR 2026) and CuES apply curiosity-driven exploration to LLM RL training, showing consistent improvements on reasoning benchmarks.

7. **PCG with LLMs Maturing**: PCGRLLM shows LLMs can generate reward functions comparable to human designers. IPCGRL adds instruction-conditioned level generation. The field is transitioning from proof-of-concept to practical tools.

8. **MARL Consolidation**: Comprehensive surveys from multiple groups (Li et al., Zhang et al.) synthesize a decade of MARL in games, proposing game complexity metrics and unified algorithm taxonomies.
