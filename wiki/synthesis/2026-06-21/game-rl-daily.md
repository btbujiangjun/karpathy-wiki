---
title: "Game RL & Game AI Bot Daily — 2026-06-21"
type: synthesis
created: 2026-06-21
updated: 2026-06-21
sources: []
tags: [game-rl, game-ai, daily, arxiv, self-play, foundation-models, benchmarks]
---

# Game RL & Game AI Bot Daily — 2026-06-21

> Curated recent papers from arXiv, ICLR 2026, CVPR 2026, and other venues on game reinforcement learning, game AI bots, game foundation models, procedural content generation, benchmarks, industry game AI, and related techniques. Compiled 2026-06-21.

---

## 1. Game RL — Reinforcement Learning in Games

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning
- **Authors**: Bo Liu, Simon Yu, Zichen Liu, Leon Guertler, Penghui Qi, Daniel Balcells, Mickel Liu, Cheston Tan, Weiyan Shi, Min Lin, Wee Sun Lee, Natasha Jaques
- **Affiliation**: Multiple institutions
- **Venue**: ICLR 2026 (Poster)
- **Abstract**: Introduces SPIRAL, a self-play framework where models learn by playing multi-turn zero-sum games against continuously improving versions of themselves. Uses role-conditioned advantage estimation (RAE) to stabilize multi-agent training. Improves reasoning by up to 10% across 8 benchmarks on Qwen and Llama model families, outperforming SFT on 25,000 expert game trajectories.
- **arXiv**: [OpenReview (ICLR 2026)](https://openreview.net/forum?id=7Yayy5fNLg)

### Offline Fictitious Self-Play for Competitive Games (Off-FSP)
- **Authors**: Jingxiao Chen, Weiji Xie, Weinan Zhang, Yong Yu, Ying Wen
- **Affiliation**: Shanghai Jiao Tong University
- **Venue**: Preprint 2025/2026
- **Abstract**: First practical model-free offline RL algorithm for competitive games. Simulates interactions with varying opponents using importance sampling on fixed datasets; combines single-agent offline RL with Fictitious Self-Play to approximate Nash equilibrium. Experiments on matrix games, poker, board games, and real-world human-robot tasks.
- **arXiv**: [2403.00841](https://arxiv.org/abs/2403.00841)

### Game-RL: Synthesizing Multimodal Verifiable Game Data to Boost VLMs' General Reasoning
- **Authors**: Jingqi Tong, Jixin Tang, Hangcheng Li, Yurong Mou, Ming Zhang, Jun Zhao, Yanbo Wen, Fan Song, Jiahao
- **Affiliation**: Fudan University
- **Venue**: ICLR 2026
- **Abstract**: Synthesizes multimodal verifiable game data to enhance VLM reasoning. Uses game environments as data generators for training vision-language models on structured reasoning tasks.

### GROW: Aligning GRPO with State-Action Modeling for Open-World VLM Agents
- **Authors**: Xiongbin Wu, Zhihao Luo, Shanzhe Lei, Lechao Zhang, Xuhong Wang, Jie Yang, Zhonglong Zheng, Yuanjie Zheng, Xin Tan, Wei Liu
- **Affiliation**: Shanghai Jiao Tong University, Shanghai AI Lab, East China Normal University, Zhejiang Normal University, Shandong Normal University
- **Venue**: arXiv 2026
- **Abstract**: Proposes GROW, an RL framework for open-world VLM agents (Minecraft) that decomposes trajectories into state-action samples and computes advantages between samples rather than treating full trajectories as entities. Enables effective multi-turn GRPO for vision-language agents.
- **arXiv**: [2605.20246](https://arxiv.org/abs/2605.20246)

### A Comprehensive Review of Multiagent Reinforcement Learning in Video Games
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: IEEE Transactions (2025)
- **Abstract**: Comprehensive survey covering multi-agent RL in video games, including cooperative, competitive, and mixed settings. Covers MARL algorithms, game environments, and open challenges.
- **Link**: [IEEE DOI 10.1109/11079788](https://ieeexplore.ieee.org/document/11079788)

### Large-Scale Study of Curiosity-Driven Learning
- **Authors**: Yuri Burda, Harri Edwards, Deepak Pathak, Amos Storkey, Trevor Darrell, Alexei A. Efros
- **Affiliation**: OpenAI, UC Berkeley, etc.
- **Venue**: ICLR 2019 (classic reference, still actively cited in 2026 game RL work)
- **Abstract**: Landmark large-scale study of purely curiosity-driven learning without extrinsic rewards across 54 Atari and Super Mario benchmarks. Shows alignment between intrinsic curiosity and hand-designed rewards. Random features sufficient for many benchmarks; learned features generalize better.

---

## 2. Game AI Bot — LLM-Powered Agents, NPC Intelligence

### Enhancing Game AI Behaviors with Large Language Models and Agent-Based Systems
- **Authors**: Andrei-Alexandru Gâdoi, Alin Stefanescu
- **Affiliation**: Electronic Arts (EA), Bucharest; University of Bucharest
- **Venue**: FSE Companion '25 (ACM International Conference on the Foundations of Software Engineering, July 2025)
- **Abstract**: Proposes a framework using LLMs and agent-based AI to improve game AI behaviors. Orchestrates interconnected parts to create complex behavior trees (BTs) for NPCs. Industry-applied from EA.
- **Link**: [ACM DOI 10.1145/3696630.3728553](https://dl.acm.org/doi/10.1145/3696630.3728553)

### Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents
- **Authors**: Zihao Wang et al. (27 authors)
- **Affiliation**: ByteDance / Seed
- **Venue**: arXiv 2025 (Oct 2025)
- **Abstract**: Generalist game agent trained on 500B+ tokens with diverse trajectories. Uses unified action space anchored to native keyboard-mouse inputs. Pre-trained across OS, web, and simulation games. Key techniques: decaying continual loss, multimodal data.
- **arXiv**: [2510.23691](https://arxiv.org/abs/2510.23691)

### A Survey on Large Language Model-Based Game Agents
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: ACM Computing Surveys (CSUR) 2026
- **Abstract**: Comprehensive survey covering LLM-based game agents, including architectures, reasoning methods, tool use, and evaluation. Taxonomizes agent designs for NPCs, in-game assistants, and autonomous players.

### CrawLLM: LLM-Based Pipeline for Game Asset Generation
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: IEEE Transactions on Visualization and Computer Graphics (ToG) 2026
- **Abstract**: Uses LLMs to generate game assets procedurally, covering environments, items, and narratives. Pipeline from natural language description to in-game 3D assets.

### Competition and Cooperation of LLM Agents in Games
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: 2026
- **Abstract**: Studies how LLM agents behave in game-theoretic settings with mixed competition and cooperation. Tests on social deduction games, economic games, and negotiation scenarios.

### GameUIAgent: LLM-Powered Framework for Automated Game UI Design
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: 2026
- **Abstract**: Framework using LLMs to automate game UI design through iterative generation and evaluation. Reduces manual design effort for in-game interfaces.

---

## 3. Game Foundation Models — Generalist Game Models

### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi "Jim" Fan
- **Affiliation**: NVIDIA, Stanford, Caltech, UChicago, UT Austin
- **Venue**: CVPR 2026
- **Abstract**: Vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games. Three key ingredients: (1) internet-scale video-action dataset from public gameplay videos, (2) multi-game benchmark environment for cross-game generalization, (3) unified vision-action model via large-scale behavior cloning. Achieves 52% relative improvement on unseen games. Releases dataset, evaluation suite, and model weights.
- **arXiv**: [2601.02427](https://arxiv.org/abs/2601.02427)

### Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents
- **(Same as Section 2 — Cross-category)**
- **Venue**: arXiv 2025
- **Key innovation**: Unified scalable action space across heterogeneous domains (OS, web, simulation games). 500B+ tokens. Decaying continual loss.
- **arXiv**: [2510.23691](https://arxiv.org/abs/2510.23691)

### GameNGen: Diffusion Models Are Real-Time Game Engines
- **Authors**: Dani Valevski, Yaniv Leviathan, Moab Arar, Shlomi Fruchter
- **Affiliation**: Google Research, Google DeepMind, Tel Aviv University
- **Venue**: ICLR 2025 (oral?; widely cited)
- **Abstract**: First game engine powered entirely by a neural model for real-time interaction. Trained on DOOM gameplay, runs at 20 FPS on a single TPU. Next-frame prediction achieves PSNR 29.4 (comparable to lossy JPEG). Two-phase training: (1) RL agent records gameplay, (2) diffusion model conditioned on past frames and actions. Augmented conditioning for long-term stability.
- **arXiv**: [2408.14837](https://arxiv.org/abs/2408.14837)

### Matrix-Game 3.0: Real-Time Streaming Interactive World Model
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: 2026
- **Abstract**: Scalable world model for real-time interactive game simulation. Enables streaming generation of game states conditioned on actions, supporting long-horizon gameplay with learned dynamics.

### JOWA: Jointly-Optimized World-Action Model for Offline Model-Based RL in Atari
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: ICLR 2025
- **Abstract**: Jointly optimizes world model and policy for offline model-based RL in game domains. Achieves strong results on the Atari 100K benchmark with limited environment interactions.

---

## 4. Procedural Content Generation — RL & LLM for Game Content

### PCGRLLM: Large Language Model-Driven Reward Design for Procedural Content Generation Reinforcement Learning
- **Authors**: (NYU Game Innovation Lab)
- **Affiliation**: New York University
- **Venue**: 2025
- **Abstract**: Uses LLMs to design reward functions for PCG RL (PCGRL). Enables non-expert users to specify level design goals in natural language and have the LLM translate them into reward signals for level generators.
- **arXiv**: [2502.10906](https://arxiv.org/abs/2502.10906)

### PCGRL+: Scaling, Control and Generalization in Reinforcement Learning Level Generators
- **Authors**: (NYU Game Innovation Lab)
- **Affiliation**: New York University
- **Venue**: 2024/2025
- **Abstract**: Extends PCGRL with techniques for scaling, better control, and generalization across level distributions. Addresses challenges in training RL agents for game level generation.
- **arXiv**: [2408.12525](https://arxiv.org/abs/2408.12525)

### The Procedural Content Generation Benchmark (PCG-Bench)
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: FDG 2025
- **Abstract**: Introduces benchmark for evaluating PCG methods, including RL-based, LLM-based, and hybrid approaches. Standardized metrics and environments for comparing level generators.

### Procedural Content Generation in Minecraft (NYU Research)
- **Authors**: (NYU Game Innovation Lab)
- **Affiliation**: NYU
- **Venue**: Ongoing project
- **Abstract**: Research on using LLMs and PCG for generating Minecraft structures, quests, and world content through natural language specifications.
- **Link**: [NYU Game Innovation Lab](https://game.engineering.nyu.edu/research/procedural-content-generation-in-minecraft/)

---

## 5. Game Benchmarks — Evaluation Suites for Game Agents

### GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents
- **Authors**: (multiple)
- **Affiliation**: National University of Singapore, University of Oxford (and others)
- **Venue**: arXiv 2026 (Apr 2026)
- **Abstract**: Standardized benchmark for evaluating multimodal game agents. Provides a suite of game environments with fine-grained perception, long-horizon planning, and precise control requirements. Measures systematic performance across vision-language-action capabilities.
- **arXiv**: [2604.07429](https://arxiv.org/abs/2604.07429)

### Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games
- **Authors**: (multiple)
- **Affiliation**: KRAFTON (publisher of PUBG)
- **Venue**: arXiv 2025 (Jun 2025)
- **Abstract**: Benchmark spanning 12 popular video games across all major genres. Uses plug-and-play interface based on Model Context Protocol (MCP) for reproducible studies of agentic modules in varied game scenarios.
- **arXiv**: [2506.03610](https://arxiv.org/abs/2506.03610)

### BALROG: Benchmarking Agentic LLM and VLM Reasoning on Games
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: 2025/2026
- **Abstract**: Evaluates LLM and VLM agents across diverse games requiring multi-step reasoning, planning, and adaptation. Provides standardized evaluation protocol and leaderboard.

### DSGBench: Diverse Strategic Game Benchmark
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: 2025/2026
- **Abstract**: Benchmark suite for strategic reasoning in games, covering combinatorial games, economic games, and social deduction games. Evaluates agent strategic decision-making capabilities.

### OfflineMania: Benchmark Environment for Offline RL in the TrackMania Racing Game
- **Authors**: (EA SEED)
- **Affiliation**: Electronic Arts SEED
- **Venue**: 2025/2026
- **Abstract**: Provides offline RL benchmark using TrackMania racing game. Large pre-collected datasets with rich state-action trajectories for offline RL research in continuous control game domains.

---

## 6. Industry Game AI — Studio Deployments & Real-Time Inference

### Enhancing Game AI Behaviors with LLMs and Agentic AI (EA)
- **Authors**: Andrei-Alexandru Gâdoi, Alin Stefanescu
- **Affiliation**: Electronic Arts
- **Venue**: FSE Companion '25 (2025)
- **Abstract**: EA's framework for integrating LLMs into game AI using behavior trees. Practical deployment considerations for real-time game inference.
- **Link**: [ACM DOI 10.1145/3696630.3728553](https://dl.acm.org/doi/10.1145/3696630.3728553)

### Beyond Copy-and-Paste: How Game Studios Are Reorganizing Around AI
- **Authors**: (multiple)
- **Affiliation**: Wharton School
- **Venue**: Wharton Research 2026
- **Abstract**: Study of organizational changes at major game studios (EA, Ubisoft, etc.) as they adopt AI workflows for game development, NPC behavior, and content generation.

### MLOps Architectures for Real-Time Game AI Deployment
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: 2025/2026
- **Abstract**: Survey and architectural patterns for deploying ML models in real-time game inference pipelines. Covers latency optimization, model quantization, speculative decoding, and KV cache management for LLM-powered game agents.

### Real-Time AI Inference Systems: Speculative Decoding, KV Cache & Streaming Architecture
- **Authors**: Kumar Shivam
- **Affiliation**: (independent)
- **Venue**: Medium (2026) — technical blog referenced in literature
- **Abstract**: Practical production guide for real-time LLM inference including speculative decoding with EAGLE3, KV cache management, tensor parallelism, and FP8 quantization — relevant for game AI deployment.
- **Link**: [Medium](https://kumarshivam-66534.medium.com/real-time-ai-inference-systems-speculative-decoding-kv-cache-streaming-architecture-f8812f7e25dd)

---

## 7. Related Techniques — Self-Play, Curiosity, Hierarchical RL, Imitation, World Models

### SPIRAL: Self-Play on Zero-Sum Games (See Section 1)
- Self-play + multi-agent multi-turn RL for LLM reasoning improvement.
- **ICLR 2026**

### Offline Fictitious Self-Play (See Section 1)
- Offline self-play for competitive games using importance sampling.
- **arXiv 2403.00841**

### Large-Scale Study of Curiosity-Driven Learning (See Section 1)
- Curiosity as intrinsic reward across 54 Atari/Super Mario benchmarks.
- **ICLR 2019** (classic, still foundational)

### Hierarchical RL with Targeted Causal Interventions
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: ICML 2025
- **Abstract**: HRL framework with targeted causal interventions for more efficient exploration in game domains. Demonstrates improved sample efficiency on complex hierarchical game tasks.

### World Models Unlock Optimal Foraging Strategies in Games
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: 2025/2026
- **Abstract**: Applies world models to game foraging scenarios, achieving near-optimal strategies through learned environment dynamics and model-based planning.

### A Survey on Self-Play Methods in Reinforcement Learning
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: TMLR 2025
- **Abstract**: Comprehensive survey covering self-play methods, including fictitious self-play, neural self-play, and population-based training. Applications in game AI and multi-agent systems.

### MARSHAL: Multi-Agent Reasoning via Self-Play with Strategic LLMs
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: ICLR 2026
- **Abstract**: Extends self-play to multi-agent reasoning settings. Strategic LLM agents improve through iterative self-play in game-theoretic scenarios.

---

## Key Trends (2026)

1. **Self-play for LLM reasoning**: SPIRAL shows self-play in zero-sum games improves general reasoning — a new axis beyond SFT/RLHF.
2. **Generalist game foundation models**: NitroGen (NVIDIA) and Game-TARS (ByteDance) train across hundreds/thousands of games for zero-shot transfer.
3. **Game world models**: GameNGen-type neural game engines continue to evolve; Matrix-Game 3.0 pushes real-time streaming interactive world models.
4. **LLM + RL for game content**: PCGRLLM uses LLMs as reward designers for RL-based procedural level generation.
5. **Standardized evaluation**: GameWorld, Orak, and BALROG aim to standardize game agent benchmarking.
6. **Industrial deployment**: EA, Ubisoft, KRAFTON actively publishing game AI infrastructure papers.
7. **Offline RL for competitive games**: Off-FSP opens offline RL to competitive multi-agent settings.
8. **GRPO for open-world VLM agents**: GROW adapts RL-based alignment to multi-turn game agent scenarios.

---

> *Generated 2026-06-21 by automated arXiv/paper search. Links verified at time of compilation.*
