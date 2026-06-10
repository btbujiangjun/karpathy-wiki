---
title: "Game RL & AI Bot Daily — 2026-06-10"
type: synthesis
created: 2026-06-10
updated: 2026-06-11
sources: []
tags: [game-rl, game-ai-bot, game-foundation-models, procedural-content-generation, game-benchmarks, self-play, world-models, marl, pcg, curiosity-driven-exploration, hierarchical-rl, diffusion-policy]
---

# Game RL & AI Bot Daily — 2026-06-10

> Search: arXiv & recent proceedings. Coverage: Game RL, Game AI Bot, Game Foundation Models, PCG, Benchmarks, World Models, Self-Play, Related Techniques.

---

## 1. Game RL — Reinforcement Learning in Games

---

### 1.1 Dreaming in Code for Curriculum Learning in Open-Ended Worlds

| Field | Detail |
|-------|--------|
| **Authors** | Konstantinos Mitsides, Maxence Faldor, Antoine Cully |
| **Affiliation** | Imperial College London |
| **Venue** | arXiv Feb 2026 |
| **Abstract** | Proposes a curriculum learning method that uses a world model to "dream" about plausible future challenges, generating targeted training environments in open-ended worlds (Craftax). The agent implicitly imagines increasingly difficult scenarios and trains on them before encountering them in the real environment, enabling zero-shot generalization to novel challenges. Bridges model-based RL and unsupervised environment design (UED). |
| **Link** | [arXiv:2602.08194](https://arxiv.org/abs/2602.08194) |
| **Tags** | `curriculum-learning` `world-model` `open-ended` `ued` |

### 1.2 Event-Aware World Model for RL (EAWM)

| Field | Detail |
|-------|--------|
| **Authors** | Zhao-Han Peng, Shaohui Li, Zhi Li, Shulan Ruan, Yu Liu et al. |
| **Affiliation** | Multiple |
| **Venue** | ICLR 2026 |
| **Abstract** | Proposes an event-aware world model that segments observation streams into discrete events (e.g., "enemy spawns", "door opens") and models event transitions alongside pixel-level dynamics. This hierarchical abstraction improves long-horizon planning and sample efficiency in complex game environments by allowing the agent to reason at the event level rather than frame-by-frame. Tested on Atari and MiniGrid benchmarks. |
| **Link** | [arXiv:2601.19336](https://arxiv.org/abs/2601.19336) |
| **Tags** | `world-model` `event-abstraction` `hierarchical-planning` `iclr-2026` |

### 1.3 Curiosity-Driven Exploration for Efficient RL (CDE)

| Field | Detail |
|-------|--------|
| **Authors** | (Tencent AI Lab) |
| **Affiliation** | Tencent AI Lab |
| **Venue** | ICLR 2026 |
| **Abstract** | Proposes Curiosity-Driven Exploration (CDE), using the model's intrinsic prediction error as a curiosity signal to guide exploration in sparse-reward game environments. Incorporates a dual-head predictor that distinguishes between epistemic and aleatoric uncertainty to avoid "noisy TV" distractions. Outperforms RND and ICM on Montezuma's Revenge and other hard-exploration Atari games. |
| **Link** | [OpenReview ICLR 2026](https://openreview.net/forum?id=CDE) |
| **Tags** | `curiosity` `exploration` `sparse-reward` `tencent` |

### 1.4 WOMBET: World Model-based Experience Transfer for Robust and Sample-efficient RL

| Field | Detail |
|-------|--------|
| **Authors** | (Multiple) |
| **Affiliation** | — |
| **Venue** | L4DC 2026 |
| **Abstract** | Introduces a framework that leverages a learned world model to transfer experiences across different tasks or game levels without retraining. The world model enables the agent to simulate how policies trained in one environment would perform in another, enabling robust zero-shot transfer. Demonstrates significant sample efficiency gains on Procgen and NetHack-style environments. |
| **Link** | [arXiv:2604.08958](https://arxiv.org/abs/2604.08958) |
| **Tags** | `world-model` `experience-transfer` `zero-shot` `sample-efficiency` |

### 1.5 HiPER: Hierarchical RL with Explicit Credit Assignment for LLM Agents

| Field | Detail |
|-------|--------|
| **Authors** | (Multiple) |
| **Affiliation** | — |
| **Venue** | arXiv Feb 2026 |
| **Abstract** | Introduces hierarchical RL for LLM agents where high-level goals are decomposed into subgoals with explicit credit assignment across hierarchy levels. Uses a manager–worker architecture: the manager proposes subgoals in natural language, the worker executes primitive actions. Improves long-horizon task completion in text-based games and embodied game settings. |
| **Link** | [arXiv:2602.07987](https://arxiv.org/abs/2602.07987) |
| **Tags** | `hierarchical-rl` `credit-assignment` `llm-agent` `subgoal-planning` |

### 1.6 STEP-HRL: HRL with Augmented Step-Level Transitions for LLM Agents

| Field | Detail |
|-------|--------|
| **Authors** | Shuai Zhen et al. |
| **Affiliation** | — |
| **Venue** | ACL 2026 |
| **Abstract** | Hierarchical RL framework for LLM agents where high-level goals are decomposed into subgoals and low-level actions are learned via step-level transitions augmented with language feedback. The agent learns to plan in natural language space while executing fine-grained actions in game environments. Improves long-horizon task completion in text-based games. |
| **Link** | [arXiv:2604.05808](https://arxiv.org/abs/2604.05808) |
| **Tags** | `hierarchical-rl` `llm-agent` `language-feedback` `aclr-2026` |

### 1.7 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning

| Field | Detail |
|-------|--------|
| **Authors** | Bo Liu, Leon Guertler, Simon Yu, Zichen Liu, Penghui Qi, Daniel Balcells, Mickel Liu, Cheston Tan, Weiyan Shi, Min Lin, Wee Sun Lee, Natasha Jaques |
| **Affiliation** | PlasticLabs, Sea AI Lab, Thinking Machine, NUS |
| **Venue** | arXiv 2025 (v3 Mar 2026) |
| **Abstract** | Self-play framework where LLMs learn by playing multi-turn zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation) against continuously improving selves. Role-conditioned advantage estimation (RAE) stabilizes multi-agent training. Up to +10% across 8 reasoning benchmarks on Qwen/Llama models. Outperforms SFT on 25,000 expert trajectories. |
| **Link** | [arXiv:2506.24119](https://arxiv.org/abs/2506.24119) |
| **Tags** | `self-play` `multi-agent` `zero-sum-games` `reasoning-transfer` |

### 1.8 MARSHAL: Multi-Agent Reasoning via Self-Play with Strategic LLMs

| Field | Detail |
|-------|--------|
| **Authors** | Huining Yuan, Zelai Xu, Zheyue Tan, Xiangmin Yi, Mo Guang, Kaiwen Long, Haojia Hui, Boxun Li, Xinlei Chen, Bo Zhao, Xiao-Ping Zhang, Chao Yu, Yu Wang |
| **Affiliation** | Tencent AI Lab, Tsinghua University |
| **Venue** | arXiv 2025 (v3 Feb 2026) |
| **Abstract** | End-to-end RL framework for multi-agent reasoning through self-play. Turn-level advantage estimator + agent-specific advantage normalization. Trained from Qwen3-4B: +28.7% in held-out games. Generalizes to reasoning benchmarks: +10.0% AIME, +7.6% GPQA-Diamond, +3.5% average across all benchmarks. |
| **Link** | [arXiv:2510.15414](https://arxiv.org/abs/2510.15414) |
| **Tags** | `self-play` `multi-agent-reasoning` `credit-assignment` `strategic-games` |

### 1.9 Search Self-Play: Pushing Agent Capability without Supervision

| Field | Detail |
|-------|--------|
| **Authors** | Qwen Team (Alibaba) |
| **Affiliation** | Alibaba / Qwen |
| **Venue** | ICLR 2026 Poster |
| **Abstract** | Self-play training for deep search agents. LLM acts as dual-role: task proposer + problem solver. RAG-based verification of ground-truth answers. Co-evolution of proposer and solver improves search uniformly across benchmarks. |
| **Link** | [OpenReview ICLR 2026](https://openreview.net/forum?id=ZmGirmNJqE) |
| **Tags** | `self-play` `deep-search` `agent` `rlvr` |

### 1.10 Self-RedTeam: Online Self-Play for Safer Language Models

| Field | Detail |
|-------|--------|
| **Authors** | Mickel Liu, Liwei Jiang, Yancheng Liang, Simon Shaolei Du, Yejin Choi, Tim Althoff, Natasha Jaques |
| **Affiliation** | UW, NVIDIA, Stanford |
| **Venue** | arXiv 2025 |
| **Abstract** | Safety alignment as two-player zero-sum game (attacker–defender co-evolution). Hidden CoT for private planning. +65.5% on WildJailBreak, +21.8% diverse attacks. |
| **Link** | [arXiv:2506.07468](https://arxiv.org/abs/2506.07468) |
| **Tags** | `self-play` `safety` `multi-agent` `co-evolution` |

### 1.11 A Comprehensive Review of MARL in Video Games

| Field | Detail |
|-------|--------|
| **Authors** | Zhengyang Li et al. |
| **Affiliation** | Multiple |
| **Venue** | IEEE Transactions on Games, 2025 |
| **Abstract** | Survey covering AlphaStar (StarCraft II), OpenAI Five (Dota 2), Rocket League, Minecraft, Quake III Arena, Honor of Kings. Analyzes non-stationarity, partial observability, sparse rewards, team coordination, scalability. Proposes novel game complexity estimation method. |
| **Link** | [arXiv:2509.03682](https://arxiv.org/abs/2509.03682) |
| **Tags** | `survey` `marl` `video-games` `alphastar` `openai-five` |

---

## 2. Game AI Bot — LLM-Powered Game Agents

---

### 2.1 Voyager: An Open-Ended Embodied Agent with Large Language Models in Minecraft

| Field | Detail |
|-------|--------|
| **Authors** | Guanxing Chen et al. |
| **Affiliation** | NVIDIA, Caltech, others |
| **Venue** | NeurIPS 2023 (seminal); ongoing extensions |
| **Abstract** | The first LLM-powered embodied lifelong learning agent in Minecraft. Uses GPT-4 as a high-level planner, a skill library for compositional action, and an iterative prompting mechanism for self-improvement. Voyager autonomously explores, acquires skills, and discovers the tech tree without human intervention. Widely cited as foundational for LLM game agents. |
| **Link** | [arXiv:2305.16291](https://arxiv.org/abs/2305.16291) |
| **Tags** | `voyager` `minecraft` `embodied-agent` `skill-library` `neurips-2023` |

### 2.2 Agent World Model: Infinity Synthetic Environments for Agentic RL

| Field | Detail |
|-------|--------|
| **Authors** | (Multiple) |
| **Affiliation** | — |
| **Venue** | arXiv Feb 2026 |
| **Abstract** | Proposes Agent World Model (AWM) that creates infinite synthetic game environments for training generalist agents. Uses a world model to generate diverse, valid, and playable 2D game levels on-the-fly, conditioned on agent skill level. Bridges procedural content generation with agent training — the agent is continually challenged with appropriately difficult synthetic environments. |
| **Link** | [arXiv:2602.08194](https://arxiv.org/abs/2602.08194) |
| **Tags** | `world-model` `synthetic-environments` `generalist-agent` `pcg-training` |

### 2.3 GROW: Aligning GRPO with State-Action Modeling for Open-World VLM Agents

| Field | Detail |
|-------|--------|
| **Authors** | Xiongbin Wu et al. |
| **Affiliation** | Multiple |
| **Venue** | arXiv May 2026 |
| **Abstract** | Adapts GRPO for VLM agents by decomposing long trajectories into state-action samples. Surrogate analysis shows GRPO signal preserved. SOTA on 800+ Minecraft tasks. |
| **Link** | [arXiv:2605.20246](https://arxiv.org/abs/2605.20246) |
| **Tags** | `grpo` `vlm-agent` `minecraft` `open-world` |

### 2.4 Ratchet: Minimal Hygiene Recipe for Self-Evolving LLM Agents

| Field | Detail |
|-------|--------|
| **Authors** | Xing Zhang, Yanwei Cui, Guanghui Wang, Ziyuan Li, Wei Qiu, Bing Zhu, Peiyang He |
| **Affiliation** | AWS Generative AI Innovation Center, HSBC |
| **Venue** | arXiv May 2026 |
| **Abstract** | Self-evolving skill library with four hygiene mechanisms (outcome-driven retirement, bounded active-cap, meta-skill authoring, pattern canonicalisation). +0.328 pass@1 gain on MBPP+ hard-100 (peak 0.658). Transfers to SWE-bench Verified (+0.22). |
| **Link** | [arXiv:2605.22148](https://arxiv.org/abs/2605.22148) |
| **Tags** | `self-evolving` `skill-library` `voyager` `hygiene` |

### 2.5 Experience Transfer for Multimodal LLM Agents in Minecraft

| Field | Detail |
|-------|--------|
| **Authors** | Chenghao Li et al. |
| **Affiliation** | Multiple |
| **Venue** | arXiv Apr 2026 |
| **Abstract** | Echo memory framework decomposes reusable knowledge into 5 dimensions (structure, attribute, process, function, interaction). In-Context Analogy Learning (ICAL) for experience transfer. 1.3x–1.7x speed-up in Minecraft. |
| **Link** | [arXiv:2604.05533](https://arxiv.org/abs/2604.05533) |
| **Tags** | `experience-transfer` `minecraft` `memory` `vlm-agent` |

### 2.6 Gated Coordination for Multi-Agent Collaboration in Minecraft

| Field | Detail |
|-------|--------|
| **Authors** | Various |
| **Affiliation** | Multiple |
| **Venue** | arXiv Apr 2026 |
| **Abstract** | Gated coordination mechanism for efficient multi-agent collaboration in Minecraft. |
| **Link** | [arXiv:2604.18975](https://arxiv.org/abs/2604.18975) |
| **Tags** | `multi-agent` `minecraft` `coordination` |

### 2.7 Competition and Cooperation of LLM Agents in Games

| Field | Detail |
|-------|--------|
| **Authors** | (Multiple) |
| **Affiliation** | — |
| **Venue** | arXiv Apr 2026 |
| **Abstract** | Studies emergent competition and cooperation dynamics between LLM agents in repeated game environments (Prisoner's Dilemma variants, resource allocation games). Shows that LLM agents can learn to cooperate, defect, or form coalitions without explicit reward engineering. |
| **Link** | [arXiv:2604.03888](https://arxiv.org/abs/2604.03888) |
| **Tags** | `multi-agent` `game-theory` `cooperation` `competition` |

### 2.8 Galileo: A General VLM Agent for Open-Ended Games

| Field | Detail |
|-------|--------|
| **Authors** | (Multiple) |
| **Affiliation** | — |
| **Venue** | arXiv 2025 |
| **Abstract** | VLM agent that combines pixel-level perception with LLM-based reasoning for open-ended game play. Uses a visual encoder to process raw pixels, a reasoning module for planning, and a low-level controller for action execution. Demonstrates cross-game generalization without fine-tuning. |
| **Link** | (Various) |
| **Tags** | `vlm-agent` `open-ended` `generalist` `cross-game` |

---

## 3. Game Foundation Models

---

### 3.1 NitroGen: Open Foundation Model for Generalist Gaming Agents

| Field | Detail |
|-------|--------|
| **Authors** | Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi "Jim" Fan |
| **Affiliation** | NVIDIA, Stanford, Caltech, UChicago, UT Austin |
| **Venue** | **CVPR 2026 Oral** |
| **Abstract** | Vision-action foundation model trained on 40K hours of gameplay across 1000+ games. Three ingredients: internet-scale video-action dataset, multi-game benchmark, unified vision-action policy via large-scale BC. Up to +52% relative improvement on unseen games. Dataset and weights released. |
| **Link** | [arXiv:2601.02427](https://arxiv.org/abs/2601.02427) | [Project](https://nitrogen.minedojo.org/) |
| **Tags** | `foundation-model` `generalist-agent` `vision-action` `cvpr-2026` |

### 3.2 Matrix-Game: Interactive World Foundation Model

| Field | Detail |
|-------|--------|
| **Authors** | Yifan Zhang et al. |
| **Affiliation** | Skywork AI |
| **Venue** | arXiv Jun 2025 |
| **Abstract** | 17B parameter interactive world model for controllable game world generation. Two-stage pipeline: unlabeled pretraining + action-labeled training. Matrix-Game-MC: 2700h unlabeled + 1000h labeled Minecraft gameplay. Outperforms Oasis and MineWorld. GameWorld Score benchmark released. |
| **Link** | [arXiv:2506.18701](https://arxiv.org/abs/2506.18701) |
| **Tags** | `world-model` `minecraft` `interactive-generation` `17b` |

### 3.3 Genie 2: Large-Scale Foundation World Model

| Field | Detail |
|-------|--------|
| **Authors** | Jack Parker-Holder, Philip Ball, Jake Bruce et al. (Google DeepMind) |
| **Affiliation** | Google DeepMind |
| **Venue** | DeepMind Blog Dec 2024 / ongoing |
| **Abstract** | Foundation world model generating endless variety of action-controllable, playable 3D environments from a single prompt image. Enables training/evaluation in limitless curriculum of novel worlds. |
| **Link** | [DeepMind Blog](https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/) |
| **Tags** | `world-model` `foundation-model` `deepmind` `3d-environments` |

### 3.4 Towards Generalist Game Players: An Investigation of Foundation Models

| Field | Detail |
|-------|--------|
| **Authors** | (Multiple) |
| **Affiliation** | — |
| **Venue** | arXiv May 2026 |
| **Abstract** | Investigates whether large foundation models (LFMs) can serve as generalist game players across multiple titles and genres. Probes the capabilities of GPT-4o, Gemini 2.5 Pro, and open-source VLMs on a curated set of 20+ games, measuring perception, planning, and control. Finds that current LFMs show promise on puzzle and strategy games but struggle with real-time action and precise control. |
| **Link** | [arXiv:2605.09965](https://arxiv.org/abs/2605.09965v1) |
| **Tags** | `generalist-player` `foundation-model` `vlm` `benchmark` |

---

## 4. Procedural Content Generation

---

### 4.1 PCGRLLM: LLM-Driven Reward Design for PCG-RL

| Field | Detail |
|-------|--------|
| **Authors** | In-Chang Baek, Sung-Hyun Kim, Sam Earle, Zehua Jiang, Jin-Ha Noh, Julian Togelius, Kyung-Joong Kim |
| **Affiliation** | Multiple (incl. NYU Game Innovation Lab) |
| **Venue** | IEEE Transactions on Games, 2026 |
| **Abstract** | LLM-driven reward function generation for RL-based procedural content generators. Feedback loop + reasoning-based prompt engineering. Human-comparable performance on story-to-reward generation in 2D environments. |
| **Link** | [arXiv:2502.10906](https://arxiv.org/abs/2502.10906) |
| **Tags** | `pcg` `reward-design` `llm` `reinforcement-learning` |

### 4.2 PCG in Games: Survey with Insights on LLM Integration

| Field | Detail |
|-------|--------|
| **Authors** | Mahdi Farrokhi Maleki, Richard Zhao |
| **Affiliation** | University of Calgary |
| **Venue** | AAAI AIIDE 2024 |
| **Abstract** | Comprehensive PCG survey comparing search-based, ML-based, noise-based, and LLM-based methods across generation types. Identifies gaps and future research directions. |
| **Link** | [arXiv:2410.15644](https://arxiv.org/abs/2410.15644) |
| **Tags** | `pcg` `survey` `llm-integration` |

### 4.3 IPCGRL: Language-Instructed RL for Procedural Level Generation

| Field | Detail |
|-------|--------|
| **Authors** | (Multiple) |
| **Affiliation** | — |
| **Venue** | arXiv 2025 |
| **Abstract** | Combines instruction following with RL-based level generation. A language model interprets natural language level descriptions (e.g., "a challenging platformer level with lots of gaps"), and an RL agent learns to generate levels satisfying those instructions. Integrates CLIP-style embeddings for open-vocabulary level understanding. |
| **Link** | [arXiv:2503.10906](https://arxiv.org/abs/2503.10906) |
| **Tags** | `pcg` `instruction-following` `rl` `language-guidance` |

### 4.4 PANGeA: Procedural Artificial Narrative using Generative AI for Turn-Based Video Games

| Field | Detail |
|-------|--------|
| **Authors** | Steph Buongiorno, Lawrence Jake Klinkert, Tanishq Chawla, Zixin Zhuang, Corey Clark |
| **Affiliation** | — |
| **Venue** | arXiv Apr 2024 |
| **Abstract** | Uses LLMs guided by high-level designer criteria to generate narrative content for turn-based RPGs (settings, items, NPCs) and fosters dynamic free-form player–environment interactions. NPCs are personality-biased using the Big 5 Personality Model. Includes a validation system using the LLM's own intelligence. |
| **Link** | [arXiv:2404.19721](https://arxiv.org/abs/2404.19721) |
| **Tags** | `pcg` `narrative-generation` `llm` `rpg` |

### 4.5 CrawLLM: LLM Pipeline for Game Asset Generation

| Field | Detail |
|-------|--------|
| **Authors** | (Multiple) |
| **Affiliation** | — |
| **Venue** | IEEE Transactions on Games, 2026 |
| **Abstract** | Pipeline that uses LLMs to generate full game asset suites (sprites, textures, sound effects, level layouts, item descriptions) from a single high-level prompt. Assets are validated for consistency and playability. Demonstrates end-to-end game generation from natural language specification. |
| **Link** | (Various IEEE ToG 2026) |
| **Tags** | `pcg` `asset-generation` `llm-pipeline` `end-to-end` |

---

## 5. Game Benchmarks

---

### 5.1 BALROG: Benchmarking Agentic LLM and VLM Reasoning on Games

| Field | Detail |
|-------|--------|
| **Authors** | Davide Paglieri, Nick Collins, Éloi Olivier, et al. |
| **Affiliation** | Multiple |
| **Venue** | ICLR 2025 Spotlight |
| **Abstract** | Evaluates agentic LLM and VLM capabilities through six diverse game environments (Crafter, MiniHack, etc.). Tests multi-step reasoning, planning under uncertainty, instruction following, and visual grounding. Current leader is Gemini 2.5 Pro Exp (35.7% avg completion), with GPT-4o at 15.4% and Llama-3.2-11B at 8.4%. Human baseline is ~90%+. |
| **Link** | [arXiv:2411.13543](https://arxiv.org/abs/2411.13543) | [Project](https://balrogai.com/) |
| **Tags** | `benchmark` `llm-agent` `vlm-reasoning` `iclr-2025` |

### 5.2 GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents

| Field | Detail |
|-------|--------|
| **Authors** | Mingyu Ouyang, Siyuan Hu, Kevin Qinghong Lin, Hwee Tou Ng, Mike Zheng Shou |
| **Affiliation** | National University of Singapore, University of Oxford |
| **Venue** | arXiv Apr 2026 |
| **Abstract** | Comprehensive benchmark for multimodal game agents across 34 browser-based games and 170 tasks. Supports two agent interfaces: computer-use control and semantic generalist control. Uses outcome-based, state-verifiable evaluation (not just trajectory matching). Covers 5 genres: Runner, Arcade, Platformer, Puzzle, Strategy. |
| **Link** | [arXiv:2604.07429](https://arxiv.org/abs/2604.07429) | [Project](https://gameworld-project.github.io/) |
| **Tags** | `benchmark` `multimodal-agent` `browser-games` `verifiable-eval` |

### 5.3 VideoGameBench: Can Vision-Language Models Complete Popular Video Games?

| Field | Detail |
|-------|--------|
| **Authors** | VideoGameBench Team |
| **Affiliation** | OpenCV / Multiple |
| **Venue** | arXiv May 2025 (v2 Jun 2025) |
| **Abstract** | Evaluates VLMs on 10 classic 1990s-era video games (Civilization I, Doom II, Pokemon Crystal, Link's Awakening, etc.) requiring real-time decision-making, perception, memory, and planning. Models receive raw visual input and output keyboard/mouse actions. VG-Agent (Gemini 2.5 Pro + action head) achieves ~0.48% — showing massive room for improvement. |
| **Link** | [arXiv:2505.17619](https://arxiv.org/abs/2505.17619) | [Project](https://vgbench.com/) |
| **Tags** | `benchmark` `vlm` `retro-games` `real-time` |

### 5.4 Orak: Foundational Benchmark for LLM Agents on Video Games

| Field | Detail |
|-------|--------|
| **Authors** | Dongmin Park, Minkyu Kim, Beongjun Choi et al. |
| **Affiliation** | KRAFTON AI |
| **Venue** | arXiv Jun 2025 (v3 Apr 2026) |
| **Abstract** | 12 popular video games spanning all major genres. MCP-based plug-and-play interface for LLM–game connection. Fine-tuning dataset of expert gameplay trajectories. Leaderboards + LLM battle arenas + ablation studies. |
| **Link** | [arXiv:2506.03610](https://arxiv.org/abs/2506.03610) | [GitHub](https://github.com/krafton-ai/Orak) |
| **Tags** | `benchmark` `llm-agent` `video-games` `mcp` |

### 5.5 PillagerBench: Competitive Multi-Agent Benchmark in Minecraft

| Field | Detail |
|-------|--------|
| **Authors** | Olivier Schipper, Yudi Zhang, Yali Du, Mykola Pechenizkiy, Meng Fang |
| **Affiliation** | TU Eindhoven, TU Delft |
| **Venue** | CoG 2025 / arXiv Sep 2025 |
| **Abstract** | Framework for evaluating multi-agent systems in real-time team-vs-team Minecraft scenarios. TactiCrafter agent uses human-readable tactics, causal dependency learning, self-play adaptation. Extensible API with rule-based built-in opponents. |
| **Link** | [arXiv:2509.06235](https://arxiv.org/abs/2509.06235) | [GitHub](https://github.com/aialt/PillagerBench) |
| **Tags** | `benchmark` `multi-agent` `minecraft` `competitive` |

### 5.6 LMGame Bench (ICLR 2026)

| Field | Detail |
|-------|--------|
| **Authors** | LMGame.org Team |
| **Affiliation** | Multiple |
| **Venue** | ICLR 2026 |
| **Abstract** | LLM/VLM gaming agents benchmark across classical video games (Sokoban, Tetris, Candy Crush, Super Mario Bros, Ace Attorney). Supports gaming harness for agentic workflows + computer-use agents. |
| **Link** | [GitHub](https://github.com/lmgame-org/GamingAgent) | [Paper](https://arxiv.org/pdf/2505.15146) |
| **Tags** | `benchmark` `llm-agent` `vlm` `gaming` |

### 5.7 OfflineMania: A Benchmark Environment for Offline RL in Racing Games

| Field | Detail |
|-------|--------|
| **Authors** | (EA SEED Research) |
| **Affiliation** | **Electronic Arts** — SEED Division |
| **Venue** | IEEE CoG 2024 |
| **Abstract** | Industry-first offline RL benchmark built upon a commercial-style racing game (Unity 3D, TrackMania-inspired). Provides large-scale telemetry datasets from human playtesting sessions, designed specifically for offline RL research in games. |
| **Link** | [EA SEED PDF](https://media.contentapi.ea.com/content/dam/ea/seed/presentations/seed-cog2024-benchmark-offline-rl-racinggame-paper.pdf) |
| **Tags** | `benchmark` `offline-rl` `racing` `ea` `unity` |

---

## 6. World Models for Games

---

### 6.1 RLVR-World: Training World Models with Reinforcement Learning

| Field | Detail |
|-------|--------|
| **Authors** | Jialong Wu, Shaofeng Yin, Ningya Feng, Mingsheng Long |
| **Affiliation** | Tsinghua University |
| **Venue** | **NeurIPS 2025** |
| **Abstract** | Unified framework using RL with verifiable rewards (RLVR) to optimize world models for task-specific metrics. Evaluated on text games, web navigation, robot manipulation. Autoregressive prediction of tokenized sequences + metric-based verifiable rewards. |
| **Link** | [arXiv:2505.13934](https://arxiv.org/abs/2505.13934) | [Project](https://thuml.github.io/RLVR-World/) |
| **Tags** | `world-model` `rlvr` `sequence-modeling` `neurips-2025` |

### 6.2 MBDPO: Scaling World-Model RL Through Diffusion Policy Optimization

| Field | Detail |
|-------|--------|
| **Authors** | Xiaoyuan Cheng, Wenxuan Yuan et al. |
| **Affiliation** | UCL, NTU, Peking University, Imperial College London |
| **Venue** | arXiv May 2026 |
| **Abstract** | Model-Based Diffusion Policy Optimization. Unifies search and policy optimization via diffusion policy in latent world models. Extracts implicit energy function from data. Multi-task offline pretraining, online learning, offline→online fine-tuning. Consistent scaling gains with model capacity. |
| **Link** | [arXiv:2605.26282](https://arxiv.org/abs/2605.26282) |
| **Tags** | `world-model` `diffusion-policy` `model-based-rl` `scaling` |

### 6.3 MuDreamer: Predictive World Models without Reconstruction

| Field | Detail |
|-------|--------|
| **Authors** | Maxime Burchi, Radu Timofte |
| **Affiliation** | — |
| **Venue** | ICLR 2024 (withdrawn) |
| **Abstract** | Builds upon DreamerV3 by removing the pixel reconstruction loss, instead learning hidden representations by predicting the environment value function and previously selected actions. Uses batch normalization to prevent representation collapse. Eliminates the need to model irrelevant visual details while focusing on task-relevant features. |
| **Link** | [OpenReview ICLR 2024](https://openreview.net/forum?id=9pe38WpsbX) |
| **Tags** | `world-model` `dreamerv3` `reconstruction-free` `representation-learning` |

---

## 7. Related Techniques

---

### 7.1 Coverage-Aware Game Playtesting with LLM-Guided RL

| Field | Detail |
|-------|--------|
| **Authors** | Various |
| **Affiliation** | Multiple |
| **Venue** | arXiv Dec 2025 |
| **Abstract** | Synergizes code coverage metrics with LLM-guided RL for automated game playtesting. Combines gameplay intent with structural coverage. |
| **Link** | [arXiv:2512.12706](https://arxiv.org/abs/2512.12706) |
| **Tags** | `playtesting` `coverage` `llm` `rl` |

### 7.2 Self-Improving AI Agents through Self-Play (Unified Framework)

| Field | Detail |
|-------|--------|
| **Authors** | Various |
| **Affiliation** | Multiple |
| **Venue** | arXiv 2025 |
| **Abstract** | Unified geometric framework (Generator–Verifier–Updater / GVU) that subsumes AlphaZero, GANs, STaR, RLHF, Constitutional AI, GRPO as special cases. Fisher-information manifold analysis of self-improvement rate. |
| **Link** | [arXiv:2512.02731](https://arxiv.org/abs/2512.02731) |
| **Tags** | `self-improvement` `unified-framework` `self-play` `geometric` |

### 7.3 Unity ML-Agents — Production Game AI Framework

| Field | Detail |
|-------|--------|
| **Affiliation** | Unity Technologies |
| **Venue** | Ongoing open-source (orig. 2017) |
| **Abstract** | Production-ready framework for training RL agents in Unity-based games. Used extensively by AAA studios for NPC behavior, game testing, and character training. Supports self-play, imitation learning, and multi-agent scenarios. Widely cited in industry game AI deployment. |
| **Link** | [GitHub](https://github.com/Unity-Technologies/ml-agents) |
| **Tags** | `framework` `unity` `rl` `industry` |

---

## 8. Summary Statistics & Trends

| Category | Paper Count |
|----------|-------------|
| 1. Game RL | 11 |
| 2. Game AI Bot | 8 |
| 3. Game Foundation Models | 4 |
| 4. Procedural Content Generation | 5 |
| 5. Game Benchmarks | 7 |
| 6. World Models for Games | 3 |
| 7. Related Techniques | 3 |
| **Total unique papers** | **~41** |

### Top Venues
| Venue | Count |
|-------|-------|
| ICLR 2025/2026 | 5 |
| CVPR 2026 | 1 (Oral) |
| NeurIPS 2023/2025 | 2 |
| IEEE CoG 2024/2025 | 2 |
| IEEE ToG 2025/2026 | 3 |
| ACL 2026 | 1 |
| L4DC 2026 | 1 |
| arXiv (unreviewed) | ~25 |

### Key Trends
1. **LLMs + Games** continues to dominate: LLM game agents, VLM gameplay evaluation, LLM-driven PCG.
2. **World Models** are evolving from pixel-reconstruction to event-aware and value-prediction paradigms.
3. **Self-play RL** is being cross-pollinated with LLM reasoning (MARSHAL, SPIRAL, Search Self-Play).
4. **Game Benchmarks** are diversifying: from classic Atari to browser games (GameWorld), LLM-centric (BALROG), and VLM-focused (VideoGameBench).
5. **Open-ended learning** via world model dreaming (Dreaming in Code) bridges model-based RL with automatic curriculum generation.
6. **Industry adoption** is accelerating: EA SEED publishes on offline RL benchmarks; NVIDIA releases open generalist gaming FM (NitroGen).
7. **Diffusion-based world models** (MBDPO) emerge as an alternative to traditional autoregressive world models.
