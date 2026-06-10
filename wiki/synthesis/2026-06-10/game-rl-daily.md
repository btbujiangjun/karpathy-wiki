---
title: "Game RL & Game AI Bot — Daily Survey (2026-06-10)"
type: synthesis
created: 2026-06-10
updated: 2026-06-10
sources: []
tags: [game-rl, game-ai-bot, game-foundation-models, procedural-content-generation, game-benchmarks, self-play, world-models, marl]
---

# Game RL & Game AI Bot — Daily Survey

> All dates are 2025–2026. Links to arXiv / OpenReview / project pages.

---

## 1. Game RL — Reinforcement Learning in Games

### 1.1 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors**: Bo Liu, Leon Guertler, Simon Yu, Zichen Liu, Penghui Qi, Daniel Balcells, Mickel Liu, Cheston Tan, Weiyan Shi, Min Lin, Wee Sun Lee, Natasha Jaques
- **Affiliation**: PlasticLabs, Sea AI Lab, Thinking Machine, NUS
- **Venue**: arXiv 2025 (v3 Mar 2026)
- **Abstract**: Self-play framework where LLMs learn by playing multi-turn zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation) against continuously improving selves. Role-conditioned advantage estimation (RAE) stabilizes multi-agent training. Up to +10% across 8 reasoning benchmarks on Qwen/Llama models. Outperforms SFT on 25,000 expert trajectories.
- **Link**: [arXiv:2506.24119](https://arxiv.org/abs/2506.24119)
- **Tags**: `self-play` `multi-agent` `zero-sum-games` `reasoning-transfer`

### 1.2 MARSHAL: Multi-Agent Reasoning via Self-Play with Strategic LLMs
- **Authors**: Huining Yuan, Zelai Xu, Zheyue Tan, Xiangmin Yi, Mo Guang, Kaiwen Long, Haojia Hui, Boxun Li, Xinlei Chen, Bo Zhao, Xiao-Ping Zhang, Chao Yu, Yu Wang
- **Affiliation**: Tencent AI Lab, Tsinghua University
- **Venue**: arXiv 2025 (v3 Feb 2026)
- **Abstract**: End-to-end RL framework for multi-agent reasoning through self-play. Turn-level advantage estimator + agent-specific advantage normalization. Trained from Qwen3-4B: +28.7% in held-out games. Generalizes to reasoning benchmarks: +10.0% AIME, +7.6% GPQA-Diamond, +3.5% average across all benchmarks.
- **Link**: [arXiv:2510.15414](https://arxiv.org/abs/2510.15414)
- **Tags**: `self-play` `multi-agent-reasoning` `credit-assignment` `strategic-games`

### 1.3 Search Self-Play: Pushing Agent Capability without Supervision
- **Authors**: Qwen Team (Alibaba)
- **Affiliation**: Alibaba / Qwen
- **Venue**: ICLR 2026 Poster
- **Abstract**: Self-play training for deep search agents. LLM acts as dual-role: task proposer + problem solver. RAG-based verification of ground-truth answers. Co-evolution of proposer and solver improves search uniformly across benchmarks.
- **Link**: [OpenReview ICLR 2026](https://openreview.net/forum?id=ZmGirmNJqE)
- **Tags**: `self-play` `deep-search` `agent` `rlvr`

### 1.4 Self-RedTeam: Online Self-Play for Safer Language Models
- **Authors**: Mickel Liu, Liwei Jiang, Yancheng Liang, Simon Shaolei Du, Yejin Choi, Tim Althoff, Natasha Jaques
- **Affiliation**: UW, NVIDIA, Stanford
- **Venue**: arXiv 2025
- **Abstract**: Safety alignment as two-player zero-sum game (attacker–defender co-evolution). Hidden CoT for private planning. +65.5% on WildJailBreak, +21.8% diverse attacks.
- **Link**: [arXiv:2506.07468](https://arxiv.org/abs/2506.07468)
- **Tags**: `self-play` `safety` `multi-agent` `co-evolution`

### 1.5 A Comprehensive Review of MARL in Video Games
- **Authors**: Zhengyang Li et al.
- **Affiliation**: Multiple
- **Venue**: IEEE Transactions on Games, 2025
- **Abstract**: Survey covering AlphaStar (StarCraft II), OpenAI Five (Dota 2), Rocket League, Minecraft, Quake III Arena, Honor of Kings. Analyzes non-stationarity, partial observability, sparse rewards, team coordination, scalability. Proposes novel game complexity estimation method.
- **Link**: [arXiv:2509.03682](https://arxiv.org/abs/2509.03682)
- **Tags**: `survey` `marl` `video-games` `alphastar` `openai-five`

---

## 2. Game AI Bot — LLM-Powered Game Agents

### 2.1 GROW: Aligning GRPO with State-Action Modeling for Open-World VLM Agents
- **Authors**: Xiongbin Wu et al.
- **Affiliation**: Multiple
- **Venue**: arXiv May 2026
- **Abstract**: Adapts GRPO for VLM agents by decomposing long trajectories into state-action samples. Surrogate analysis shows GRPO signal preserved. SOTA on 800+ Minecraft tasks.
- **Link**: [arXiv:2605.20246](https://arxiv.org/abs/2605.20246)
- **Tags**: `grpo` `vlm-agent` `minecraft` `open-world`

### 2.2 Ratchet: Minimal Hygiene Recipe for Self-Evolving LLM Agents
- **Authors**: Xing Zhang, Yanwei Cui, Guanghui Wang, Ziyuan Li, Wei Qiu, Bing Zhu, Peiyang He
- **Affiliation**: AWS Generative AI Innovation Center, HSBC
- **Venue**: arXiv May 2026
- **Abstract**: Self-evolving skill library with four hygiene mechanisms (outcome-driven retirement, bounded active-cap, meta-skill authoring, pattern canonicalisation). +0.328 pass@1 gain on MBPP+ hard-100 (peak 0.658). Transfers to SWE-bench Verified (+0.22).
- **Link**: [arXiv:2605.22148](https://arxiv.org/abs/2605.22148)
- **Tags**: `self-evolving` `skill-library` `voyager` `hygiene`

### 2.3 Experience Transfer for Multimodal LLM Agents in Minecraft
- **Authors**: Chenghao Li et al.
- **Affiliation**: Multiple
- **Venue**: arXiv Apr 2026
- **Abstract**: Echo memory framework decomposes reusable knowledge into 5 dimensions (structure, attribute, process, function, interaction). In-Context Analogy Learning (ICAL) for experience transfer. 1.3x–1.7x speed-up in Minecraft.
- **Link**: [arXiv:2604.05533](https://arxiv.org/abs/2604.05533)
- **Tags**: `experience-transfer` `minecraft` `memory` `vlm-agent`

### 2.4 Gated Coordination for Multi-Agent Collaboration in Minecraft
- **Authors**: Various
- **Affiliation**: Multiple
- **Venue**: arXiv Apr 2026
- **Abstract**: Gated coordination mechanism for efficient multi-agent collaboration in Minecraft.
- **Link**: [arXiv:2604.18975](https://arxiv.org/abs/2604.18975)
- **Tags**: `multi-agent` `minecraft` `coordination`

---

## 3. Game Foundation Models

### 3.1 NitroGen: Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi "Jim" Fan
- **Affiliation**: NVIDIA, Stanford, Caltech, UChicago, UT Austin
- **Venue**: CVPR 2026 **Oral**
- **Abstract**: Vision-action foundation model trained on 40K hours of gameplay across 1000+ games. Three ingredients: internet-scale video-action dataset, multi-game benchmark, unified vision-action policy via large-scale BC. Up to +52% relative improvement on unseen games. Dataset and weights released.
- **Link**: [arXiv:2601.02427](https://arxiv.org/abs/2601.02427) | [Project](https://nitrogen.minedojo.org/)
- **Tags**: `foundation-model` `generalist-agent` `vision-action` `cvpr-2026`

### 3.2 Matrix-Game: Interactive World Foundation Model
- **Authors**: Yifan Zhang et al.
- **Affiliation**: Skywork AI
- **Venue**: arXiv Jun 2025
- **Abstract**: 17B parameter interactive world model for controllable game world generation. Two-stage pipeline: unlabeled pretraining + action-labeled training. Matrix-Game-MC: 2700h unlabeled + 1000h labeled Minecraft gameplay. Outperforms Oasis and MineWorld. GameWorld Score benchmark released.
- **Link**: [arXiv:2506.18701](https://arxiv.org/abs/2506.18701)
- **Tags**: `world-model` `minecraft` `interactive-generation` `17b`

### 3.3 Genie 2: Large-Scale Foundation World Model
- **Authors**: Jack Parker-Holder, Philip Ball, Jake Bruce et al. (Google DeepMind)
- **Affiliation**: Google DeepMind
- **Venue**: DeepMind Blog Dec 2024 / ongoing
- **Abstract**: Foundation world model generating endless variety of action-controllable, playable 3D environments from single prompt image. Enables training/evaluation in limitless curriculum of novel worlds.
- **Link**: [DeepMind Blog](https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/)
- **Tags**: `world-model` `foundation-model` `deepmind` `3d-environments`

---

## 4. Procedural Content Generation

### 4.1 PCGRLLM: LLM-Driven Reward Design for PCG-RL
- **Authors**: In-Chang Baek, Sung-Hyun Kim, Sam Earle, Zehua Jiang, Jin-Ha Noh, Julian Togelius, Kyung-Joong Kim
- **Affiliation**: Multiple (incl. NYU Game Innovation Lab)
- **Venue**: IEEE Transactions on Games, 2026
- **Abstract**: LLM-driven reward function generation for RL-based procedural content generators. Feedback loop + reasoning-based prompt engineering. Human-comparable performance on story-to-reward generation in 2D environments.
- **Link**: [arXiv:2502.10906](https://arxiv.org/abs/2502.10906)
- **Tags**: `pcg` `reward-design` `llm` `reinforcement-learning`

### 4.2 PCG in Games: Survey with Insights on LLM Integration
- **Authors**: Mahdi Farrokhi Maleki, Richard Zhao
- **Affiliation**: University of Calgary
- **Venue**: AAAI AIIDE 2024
- **Abstract**: Comprehensive PCG survey comparing search-based, ML-based, noise-based, and LLM-based methods across generation types. Identifies gaps and future research directions.
- **Link**: [arXiv:2410.15644](https://arxiv.org/abs/2410.15644)
- **Tags**: `pcg` `survey` `llm-integration`

---

## 5. Game Benchmarks

### 5.1 Orak: Foundational Benchmark for LLM Agents on Video Games
- **Authors**: Dongmin Park, Minkyu Kim, Beongjun Choi et al.
- **Affiliation**: KRAFTON AI
- **Venue**: arXiv Jun 2025 (v3 Apr 2026)
- **Abstract**: 12 popular video games spanning all major genres. MCP-based plug-and-play interface for LLM–game connection. Fine-tuning dataset of expert gameplay trajectories. Leaderboards + LLM battle arenas + ablation studies.
- **Link**: [arXiv:2506.03610](https://arxiv.org/abs/2506.03610) | [GitHub](https://github.com/krafton-ai/Orak)
- **Tags**: `benchmark` `llm-agent` `video-games` `mcp`

### 5.2 PillagerBench: Competitive Multi-Agent Benchmark in Minecraft
- **Authors**: Olivier Schipper, Yudi Zhang, Yali Du, Mykola Pechenizkiy, Meng Fang
- **Affiliation**: TU Eindhoven, TU Delft
- **Venue**: CoG 2025 / arXiv Sep 2025
- **Abstract**: Framework for evaluating multi-agent systems in real-time team-vs-team Minecraft scenarios. TactiCrafter agent uses human-readable tactics, causal dependency learning, self-play adaptation. Extensible API with rule-based built-in opponents.
- **Link**: [arXiv:2509.06235](https://arxiv.org/abs/2509.06235) | [GitHub](https://github.com/aialt/PillagerBench)
- **Tags**: `benchmark` `multi-agent` `minecraft` `competitive`

### 5.3 LMGame Bench (ICLR 2026)
- **Authors**: LMGame.org Team
- **Affiliation**: Multiple
- **Venue**: ICLR 2026
- **Abstract**: LLM/VLM gaming agents benchmark across classical video games (Sokoban, Tetris, Candy Crush, Super Mario Bros, Ace Attorney). Supports gaming harness for agentic workflows + computer-use agents.
- **Link**: [GitHub](https://github.com/lmgame-org/GamingAgent) | [Paper](https://arxiv.org/pdf/2505.15146)
- **Tags**: `benchmark` `llm-agent` `vlm` `gaming`

---

## 6. World Models for Games

### 6.1 RLVR-World: Training World Models with Reinforcement Learning
- **Authors**: Jialong Wu, Shaofeng Yin, Ningya Feng, Mingsheng Long
- **Affiliation**: Tsinghua University
- **Venue**: NeurIPS 2025
- **Abstract**: Unified framework using RL with verifiable rewards (RLVR) to optimize world models for task-specific metrics. Evaluated on text games, web navigation, robot manipulation. Autoregressive prediction of tokenized sequences + metric-based verifiable rewards.
- **Link**: [arXiv:2505.13934](https://arxiv.org/abs/2505.13934) | [Project](https://thuml.github.io/RLVR-World/)
- **Tags**: `world-model` `rlvr` `sequence-modeling` `neurips-2025`

### 6.2 MBDPO: Scaling World-Model RL Through Diffusion Policy Optimization
- **Authors**: Xiaoyuan Cheng, Wenxuan Yuan et al.
- **Affiliation**: UCL, NTU, Peking University, Imperial College London
- **Venue**: arXiv May 2026
- **Abstract**: Model-Based Diffusion Policy Optimization. Unifies search and policy optimization via diffusion policy in latent world models. Extracts implicit energy function from data. Multi-task offline pretraining, online learning, offline→online fine-tuning. Consistent scaling gains with model capacity.
- **Link**: [arXiv:2605.26282](https://arxiv.org/abs/2605.26282)
- **Tags**: `world-model` `diffusion-policy` `model-based-rl` `scaling`

---

## 7. Related Techniques

### 7.1 Coverage-Aware Game Playtesting with LLM-Guided RL
- **Authors**: Various
- **Affiliation**: Multiple
- **Venue**: arXiv Dec 2025
- **Abstract**: Synergizes code coverage metrics with LLM-guided RL for automated game playtesting. Combines gameplay intent with structural coverage.
- **Link**: [arXiv:2512.12706](https://arxiv.org/abs/2512.12706)
- **Tags**: `playtesting` `coverage` `llm` `rl`

### 7.2 Self-Improving AI Agents through Self-Play (Unified Framework)
- **Authors**: Various
- **Affiliation**: Multiple
- **Venue**: arXiv 2025
- **Abstract**: Unified geometric framework (Generator–Verifier–Updater / GVU) that subsumes AlphaZero, GANs, STaR, RLHF, Constitutional AI, GRPO as special cases. Fisher-information manifold analysis of self-improvement rate.
- **Link**: [arXiv:2512.02731](https://arxiv.org/abs/2512.02731)
- **Tags**: `self-improvement` `unified-framework` `self-play` `geometric`

---

## Summary Table

| # | Paper | Category | Venue | Key Innovation |
|---|-------|----------|-------|----------------|
| 1 | SPIRAL | Game RL / Self-Play | arXiv 2025 | Zero-sum games → reasoning transfer, RAE |
| 2 | MARSHAL | Game RL / Self-Play | arXiv 2025 | Turn-level advantage for multi-agent reasoning |
| 3 | Search Self-Play | Game RL / Self-Play | ICLR 2026 | Proposer–solver co-evolution for search |
| 4 | Self-RedTeam | Game RL / Self-Play | arXiv 2025 | Attacker–defender self-play for safety |
| 5 | MARL Survey | Game RL / MARL | IEEE ToG 2025 | Comprehensive MARL + game complexity metric |
| 6 | GROW | Game AI Bot | arXiv 2026 | GRPO state-action decomposition for VLM agents |
| 7 | Ratchet | Game AI Bot | arXiv 2026 | Skill library hygiene for self-evolving agents |
| 8 | Experience Transfer | Game AI Bot | arXiv 2026 | 5-dim memory + ICAL for Minecraft agents |
| 9 | NitroGen | Game Foundation Model | CVPR 2026 Oral | 40K hours, 1000+ games vision-action FM |
| 10 | Matrix-Game | Game Foundation Model | arXiv 2025 | 17B interactive world model for Minecraft |
| 11 | Genie 2 | Game Foundation Model | DeepMind 2024 | Foundation world model for 3D environments |
| 12 | PCGRLLM | Procedural Content Generation | IEEE ToG 2026 | LLM reward design for PCG-RL |
| 13 | PCG Survey | Procedural Content Generation | AAAI AIIDE 2024 | PCG + emerging LLM integration survey |
| 14 | Orak | Game Benchmark | arXiv 2025 | 12-game benchmark with MCP interface |
| 15 | PillagerBench | Game Benchmark | CoG 2025 | Competitive multi-agent Minecraft benchmark |
| 16 | LMGame Bench | Game Benchmark | ICLR 2026 | LLM/VLM gaming agent evaluation suite |
| 17 | RLVR-World | World Model | NeurIPS 2025 | RLVR for world model optimization |
| 18 | MBDPO | World Model | arXiv 2026 | Diffusion policy optimization in world models |
| 19 | Coverage Playtesting | Related | arXiv 2025 | LLM + code coverage for game testing |
| 20 | Self-Improving Framework | Related | arXiv 2025 | Unified GVU geometry for self-play methods |
