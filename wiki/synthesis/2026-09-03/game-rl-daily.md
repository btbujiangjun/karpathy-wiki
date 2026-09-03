---
title: "Game RL & Game AI Bot — Daily Paper Digest (September 3, 2026)"
type: synthesis
created: 2026-09-03
updated: 2026-09-03
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, pcg, benchmarks, world-models, self-play, vlm, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-09-03)

> Survey of recent papers across 7 categories: Game RL, Game AI Bot, Game Foundation Models, Procedural Content Generation, Game Benchmarks, Industry Game AI, and Related Techniques. Papers sourced from arXiv, recent proceedings, and web search.

---

## 1. Game RL — Reinforcement Learning in Games

### 1.1 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL

- **Authors**: Bo Liu, Leon Guertler, Simon C.H. Yu, Zichen Liu, Penghui Qi, Daniel Balcells, et al.
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint
- **arXiv**: [2506.24119](https://arxiv.org/abs/2506.24119)
- **Abstract & Key Innovations**: Introduces SPIRAL, a self-play framework where LLMs learn by playing multi-turn zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation) against improving versions of themselves. Proposes **Role-Conditioned Advantage Estimation (RAE)** to stabilize multi-agent training. Multi-game SPIRAL training achieves up to **+10% improvement** across 8 reasoning benchmarks on 4 models (Qwen3-4B/8B-Base, Octothinker-8B-Base, Llama-3.1-8B-Instruct), outperforming supervised fine-tuning on 25K expert trajectories. Different games develop complementary cognitive skills (spatial reasoning, probabilistic thinking, strategic optimization).

### 1.2 MARSHAL: Incentivizing Multi-Agent Reasoning via Self-Play with Strategic LLMs

- **Authors**: Hui Yuan, Zhe Xu, Zheyue Tan, Xianhao Yi, Guang Mo, Kaiwen Long, et al.
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2025-10)
- **arXiv**: [2510.15414](https://arxiv.org/abs/2510.15414)
- **Abstract & Key Innovations**: End-to-end RL framework for multi-agent reasoning through self-play in cooperative AND competitive games (Tic-Tac-Toe, Kuhn Poker, Mini Hanabi). Features **turn-level advantage estimator** and **agent-specific advantage normalization**. MARSHAL agent (from Qwen3-4B) shows up to **28.7% improvement** on held-out games; generalizes beyond games with +10.0% on AIME, +6.6% on GPQA-Diamond. Advances SPIRAL by showing role separation is critical only in games with distinct return distributions.

### 1.3 STRATAGEM: Transferable Reasoning via Trajectory-Modulated Game Self-Play

- **Authors**: Xiachong Feng, Deyi Yin, Xiaocheng Feng, Yi Jiang, Libo Qin, Yangfan Ye, et al.
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-04)
- **arXiv**: [2604.17696](https://arxiv.org/pdf/2604.17696)
- **Abstract & Key Innovations**: Addresses two barriers to reasoning transfer from games: **domain specificity** and **contextual stasis**. Introduces **Reasoning Transferability Coefficient (φ)** measuring abstraction level, and **Reasoning Evolution Reward (ψ)** incentivizing progressive reasoning. Consistent improvements across math reasoning, general reasoning, and code generation benchmarks, with pronounced gains on competition-level mathematics.

### 1.4 MEMO: Memory-Augmented Model Context Optimization for Robust Multi-Turn Multi-Agent LLM Games

- **Authors**: Yunfei Xie, Kevin Wang, Bobby Cheng, Jianzhu Yao, Zhizhou Sha, Alexander Duffy, et al.
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-03)
- **arXiv**: [2603.09022](https://arxiv.org/pdf/2603.09022)
- **Abstract & Key Innovations**: Self-play framework optimizing inference-time context via retention (persistent memory bank) and exploration (tournament-style prompt evolution with TRUEISKILL). Raises mean win rate from 25.1%→49.5% (GPT-4o-mini) and 20.9%→44.3% (Qwen-2.5-7B) using **19× fewer environment interactions** than RL baselines. Largest gains in negotiation and imperfect-information games.

### 1.5 Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills

- **Authors**: *(unverified)*
- **Affiliation**: *(unverified)* — code: github.com/Qwen-Applications/skill-self-play
- **Venue**: arXiv preprint (2026-07)
- **arXiv**: [2607.22529](https://arxiv.org/html/2607.22529v1)
- **Abstract & Key Innovations**: Co-evolutionary framework (Skill-SP) with proposer, solver, and dynamic skill controller orchestrated via RL loop. Reconciles task diversity and verification reliability through skill-based decomposition: each skill ensures deep verifiable execution while dynamic routing maintains open-ended variety. Pushes performance ceiling of capable backbones on tool-use and reasoning benchmarks.

---

## 2. Game AI Bot — LLM-Powered Game Agents

### 2.1 WorldMind: Decoupled Game World Model for State-Aware NPC Behavior

- **Authors**: *(unverified)*
- **Affiliation**: *(unverified)* — project: teawhite.cn/worldmind_projectpage
- **Venue**: arXiv preprint (2026-08)
- **arXiv**: [2608.21439](https://arxiv.org/html/2608.21439)
- **Abstract & Key Innovations**: First decoupled framework for state-aware NPC behavior in game world models. Four-layer architecture: Understanding (compact state reconstruction) → Decision (LLM reasoning over state) → Control (action-to-condition translation) → Generation (video synthesis). Introduces **BOSS-140K dataset** (200+ hours gameplay video with frame-aligned state annotations). Preferred over baselines in ~70% of pairwise comparisons for NPC behavior.

### 2.2 PCSP: One Policy, Infinite NPCs — Persona-Traceable Shared RL Policies

- **Authors**: Yoosung Hong
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-05)
- **arXiv**: [2605.23652](https://arxiv.org/html/2605.23652)
- **Abstract & Key Innovations**: Persona-Conditioned Shared Policy (PCSP) — a single RL policy conditioned on frozen LLM embeddings of free-form persona descriptions. Combines once-per-NPC persona encoding, low-rank persona projection, and PPO + InfoNCE consistency + KL diversity training. On 300-persona benchmark: **compositional zero-shot persona identification up to 17× above chance**, Spearman ρ≈0.73, **22× faster inference** than LLM-as-policy baseline. UE5 deployment at 64 agents with 1.7% failure rate.

### 2.3 Sensi: Learn One Thing at a Time — Curriculum-Based Test-Time Learning for LLM Game Agents

- **Authors**: Mohsen Arjmandi
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-03)
- **arXiv**: [2603.17683](https://arxiv.org/html/2603.17683)
- **Abstract & Key Innovations**: Two-player architecture separating perception from action for ARC-AGI-3 game-playing. Sensi v1 solves 2 levels via hypothesis accumulation; v2 adds curriculum learning + database-as-control-plane + LLM-as-judge, achieving **50-94× greater sample efficiency** (32 vs 1600-3000 attempts). Precisely diagnoses failure mode as self-consistent hallucination cascade in perception layer.

### 2.4 HeRoN: Mediated RL-LLM Framework for Adaptive NPC Behavior

- **Authors**: *(unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: Neural Computing and Applications, Springer (2026-06)
- **Link**: [Springer](https://link.springer.com/article/10.1007/s00521-026-12275-w)
- **Abstract & Key Innovations**: Integrates RL and LLMs through functional separation: RL-controlled NPC policy for action execution, LLM strategy generator for context-aware proposals, lightweight reviewer for constraint consistency. Achieves up to **81% improvement in task success rate** while substantially reducing constraint-violating actions across two custom game environments.

### 2.5 Nemobot Games: Crafting Strategic AI Gaming Agents with LLMs

- **Authors**: *(unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-04)
- **arXiv**: [2604.21896](https://arxiv.org/abs/2604.21896v1)
- **Abstract & Key Innovations**: Extends Shannon's taxonomy of game-playing machines using LLMs. Four game classes: dictionary-based (compressed state-action mappings), solvable (mathematical reasoning), heuristic (minimax + crowd-sourced data), learning (RLHF + self-critique). Interactive platform for creating and deploying LLM-powered game agents.

### 2.6 Controlling LLM Characters in Live Multiplayer Games

- **Authors**: *(unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-04)
- **arXiv**: [2604.04703](https://arxiv.org/html/2604.04703v2)
- **Abstract & Key Innovations**: **Bounded autonomy** control architecture for LLM characters in live multiplayer games. Three interfaces: agent-agent (probabilistic reply-chain decay), agent-world (embedding-based action grounding with fallback), player-agent (**whisper** soft-steering technique). Deployed in live multiplayer social game, demonstrating workable LLM character interaction.

### 2.7 Orchestrated Reality: LLM-Driven World Simulation as Parameterized-Action POMDP

- **Authors**: Yuhang Huang, Chenmiao Li, Chaowei Fang
- **Affiliation**: University of Tokyo / Individual Researcher
- **Venue**: arXiv preprint (2026-06)
- **arXiv**: [2606.16014](https://doi.org/10.48550/arxiv.2606.16014)
- **Abstract & Key Innovations**: Formalizes LLM-driven game worlds as Parameterized-Action POMDP. JSON entity tree as canonical state, Plan-Diff-Validate-Apply (PDVA) pipeline as transition kernel, schema-validated content-hashed JSON deltas. Framework for game master agents with persistent, inspectable, branchable world state.

---

## 3. Game Foundation Models — Generalist Game Agents

### 3.1 NitroGen: An Open Foundation Model for Generalist Gaming Agents

- **Authors**: Loic Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi Fan
- **Affiliation**: NVIDIA / UW / Caltech / UT Austin
- **Venue**: CVPR 2026
- **arXiv**: [2601.02427](https://arxiv.org/html/2601.02427v1)
- **Abstract & Key Innovations**: Vision-action foundation model trained on **40,000 hours of gameplay across 1,000+ games**. Internet-scale dataset from publicly available videos with automatic action extraction. Unified 16-dim binary gamepad + 4-dim continuous joystick action space. Flow-matching DiT architecture. Fine-tuning from pre-trained weights yields **up to 52% relative improvement** in task success rates. Open-source dataset, evaluation suite, and model weights.

### 3.2 Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents

- **Authors**: Zihao Wang, Xujing Li, Yining Ye, et al.
- **Affiliation**: ByteDance Seed / Peking University / M-A-P
- **Venue**: arXiv preprint (2025-10)
- **arXiv**: [2510.23691](https://doi.org/10.48550/arxiv.2510.23691)
- **Abstract & Key Innovations**: Unified action space based on native keyboard-mouse inputs for generalist game agents. >500B tokens continual pre-training across game trajectories, GUI agent trajectories, and multimodal data. Sparse Thinking strategy (interleaving reasoning and action at critical decision points). **~2× performance improvement in Minecraft** over previous SOTA; outperforms GPT-5, Gemini-2.5-Pro, Claude-4-Sonnet on FPS benchmarks.

### 3.3 Pixels2Play (P2P0.1): A Foundation Model for 3D Gameplay

- **Authors**: Yuguang Yue, Chris Green, Samuel Hunt, Irakli Salia, Wenzhe Shi, Jonathan J. Hunt
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2025-08)
- **arXiv**: [2508.14295](https://arxiv.org/html/2508.14295)
- **Abstract & Key Innovations**: Foundation model trained end-to-end to play 3D games from raw pixels. Decoder-only transformer with auto-regressive action output. Training: labeled demonstrations + unlabeled public videos with imputed actions via inverse-dynamics model. Runs real-time on single RTX 5090. Qualitative results across Roblox and MS-DOS titles.

### 3.4 Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL

- **Authors**: *(unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-05)
- **arXiv**: [2605.00347](https://arxiv.org/html/2605.00347v1)
- **Abstract & Key Innovations**: Studies RL-based training of VLMs for **long-horizon (100+ turns)** decision-making in Super Mario Land. Adapted PPO with lightweight **turn-level critic** substantially improves stability over GRPO/Reinforce++. Pretrained VLMs provide strong action priors, significantly improving sample efficiency. Odysseus achieves at least **3× average game progress** than frontier models. Demonstrates in-game and cross-game generalization.

### 3.5 Towards Generalist Game Players: Foundation Models in the Game Multiverse

- **Authors**: Kuan Zhang, Dongchen Liu, Qiyue Zhao, Tianyu Xin, Yue Su, Haisheng Wang, et al.
- **Affiliation**: Tsinghua University
- **Venue**: arXiv preprint (2026-05)
- **arXiv**: [2605.09965](https://doi.org/10.48550/arxiv.2605.09965)
- **Abstract & Key Innovations**: Comprehensive survey tracing the lifecycle of generalist game players across Dataset, Model, Harness, and Benchmark pillars. Defines four eras (Symbolic/RL → Foundation Models → Creator stage). Five-level roadmap from single-game mastery to simultaneous creation and evolution. Covers LFMs (LLMs, VLMs, VLAs, World Models) as generalist players with omni-reality adaptability.

### 3.6 GameVerse: Can Vision-Language Models Learn from Video-based Reflection?

- **Authors**: Kuan Zhang, Dongchen Liu, Qiyue Zhao, et al.
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-03)
- **arXiv**: [2603.06656](https://arxiv.org/html/2603.06656)
- **Abstract & Key Innovations**: Video game benchmark with **reflect-and-retry paradigm** assessing how VLMs internalize visual experience. Cognitive hierarchical taxonomy spanning 15 globally popular games, dual action space (semantic + GUI), milestone evaluation. Best performance by combining failure trajectories and expert tutorials — training-free analogue to RL + SFT.

---

## 4. Procedural Content Generation

### 4.1 IPCGRL: Language-Instructed RL for Procedural Level Generation

- **Authors**: In-Chang Baek, Sunghyun Kim, Seo-Young Lee, Dong-Hyeon Kim, Kyung-Joong Kim
- **Affiliation**: *(unverified)*
- **Venue**: IEEE Conference on Games (CoG) 2025
- **arXiv**: [2503.12358](https://arxiv.org/html/2503.12358)
- **Abstract & Key Innovations**: Instruction-based PCGRL incorporating sentence embedding model for text-to-level generation. Task-specific fine-tuned embeddings compress game-level conditions. Achieves **21.4% improvement in controllability** and **17.2% improvement in generalizability** for unseen instructions compared to general-purpose BERT embeddings.

### 4.2 VIPCGRL: Human-Aligned PCGRL via Text-Level-Sketch Shared Representation

- **Authors**: In-Chang Baek, Seoyoung Lee, Sung-Hyun Kim, Geumhwan Hwang, KyungJoong Kim
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2025-08)
- **arXiv**: [2508.09860](https://arxiv.org/html/2508.09860)
- **Abstract & Key Innovations**: Three-modality (text, level, sketches) DRL framework with **quadruple contrastive learning** shared embedding space. Auxiliary reward from embedding similarity aligns policy with human style. Outperforms baselines in human-likeness validated by both quantitative metrics and human evaluations.

### 4.3 Procedural Content Metageneration via Program Search and Continual Abstraction Discovery

- **Authors**: *(unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: IEEE (2026)
- **arXiv**: [2608.17947](https://arxiv.org/html/2608.17947v1)
- **Abstract & Key Innovations**: LLM-driven evolutionary search over executable Python-level generators in Sokoban, Zelda, Dangerous Dave, Lode Runner. Introduces **Continual Abstraction Discovery (CAD)** extracting reusable primitives from high-fitness programs. CAD raises mean final best fitness in all 8 domain-API comparisons; learned libraries adopted by most later programs.

### 4.4 Multiverse: Language-Conditioned Multi-Game Level Blending

- **Authors**: In-Chang Baek, Jiyun Jung, Geum-Hwan Hwang, Sung-Hyun Kim, Kyung-Joong Kim
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-03)
- **arXiv**: [2603.26782](https://doi.org/10.48550/arxiv.2603.26782)
- **Abstract & Key Innovations**: Language-conditioned multi-game level generator enabling cross-game level blending through textual specifications. Shared latent space with threshold-based multi-positive contrastive supervision. Supports controllable blending via latent interpolation and zero-shot generation from compositional prompts.

### 4.5 Database-Driven Framework for 3D Level Generation with LLMs

- **Authors**: Kaijie Xu, Clark Verbrugge
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2025-08)
- **arXiv**: [2508.18533](https://arxiv.org/html/2508.18533)
- **Abstract & Key Innovations**: Fully offline, database-driven pipeline using LLMs to seed reusable libraries for facilities, rooms, and mechanics. Multi-phase pipeline: room selection → facility optimization → mechanic integration → navigability repair. Eliminates live LLM calls, giving designers finer control and easier upkeep than prompt-driven approaches.

---

## 5. Game Benchmarks

### 5.1 GameWorld: Standardized Evaluation of Multimodal Game Agents

- **Authors**: Mingyu Ouyang, Siyuan Hu, Kevin Qinghong Lin, Hwee Tou Ng, Mike Zheng Shou
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-04)
- **arXiv**: [2604.07429](https://ar5iv.labs.arxiv.org/html/2604.07429)
- **Abstract & Key Innovations**: Benchmark for multimodal game agents in browser environments. **34 games across 5 genres, 170 tasks**. Two agent interfaces: Computer-Use Agents (raw keyboard/mouse) and Generalist Multimodal Agents (semantic action parsing). State-verifiable evaluation from serialized gameAPI (233 state fields). 18 model-interface pairs evaluated. GameWorld-RT for real-time interaction. Even best agent far from human capabilities.

### 5.2 OmniGameArena: Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics

- **Authors**: Mingxian Lin, Shengju Qian, Yuqi Liu, et al.
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-06)
- **arXiv**: [2606.09826](https://doi.org/10.48550/arxiv.2606.09826)
- **Abstract & Key Innovations**: Real-time benchmark of **12 newly built UE5 games** (7 Solo, 3 PvP, 2 Coop) with unified action interfaces. **Improvement Dynamics Curve (IDC)**: agentic-reflection harness where reflector LLM autonomously refines skill prompts across rounds. No single VLM dominates; commercial agents hold wide gap over open-weight VLMs. IDC shows all 4 top agents improve through reflection, with peak typically mid-curve.

### 5.3 lmgame-Bench: How Good are LLMs at Playing Games?

- **Authors**: Lanxiang Hu, Ming Huo, Yuxuan Zhang, Hongwen Yu, Eric P. Xing, Ion Stoica, et al.
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2025-05)
- **arXiv**: [2505.15146](https://doi.org/10.48550/arxiv.2505.15146)
- **Abstract & Key Innovations**: Suite of platformer, puzzle, and narrative games with unified Gym-style API, lightweight perception/memory scaffolds, and contamination-mitigation techniques. 13 models evaluated: o3 and o1 achieve top-2. **RL training on a single game transfers** both to unseen games and external planning tasks (BlocksWorld, WebShop).

### 5.4 VideoGameBench: Can VLMs Complete Popular Video Games?

- **Authors**: Alex L. Zhang, Thomas L. Griffiths, Karthik R. Narasimhan, Ofir Press
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2025-05)
- **arXiv**: [2505.18134](https://doi.org/10.48550/arxiv.2505.18134)
- **Abstract & Key Innovations**: **10 popular 1990s video games** with only raw visual inputs and high-level descriptions. Three games kept secret for generalization testing. Best models (Gemini 2.5 Pro, Claude 3.7 Sonnet) complete only **0.48% of VideoGameBench** and 1.6% of VideoGameBench Lite (paused emulator). Inference latency identified as major limitation.

### 5.5 Orak: Foundational Benchmark for Training and Evaluating LLM Agents on Video Games

- **Authors**: Dongmin Park, Minkyu Kim, Beongjun Choi, Junhyuck Kim, Keon Lee, Jonghyun Lee, et al.
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2025-06)
- **arXiv**: [2506.03610](https://doi.org/10.48550/arxiv.2506.03610)
- **Abstract & Key Innovations**: **12 popular video games across all major genres** with MCP-based plug-and-play interface. Studies agentic modules (reflection, planning, memory, skill management) essential for complex gameplay. Proposes fine-tuning dataset of LLM gameplay trajectories. Leaderboard, LLM battle arenas, and in-depth analyses of visual input, agentic strategies, and finetuning effects.

### 5.6 DiG-bench: Discovery in Games

- **Authors**: *(unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-08)
- **arXiv**: [2608.12593](https://arxiv.org/html/2608.12593)
- **Abstract & Key Innovations**: **70 independent games** at 7 difficulty tiers testing discovery of transformation rules through interaction/experimentation. Win conditions unknown. Lowest tier routinely solvable by Gemini 3.1 Pro; highest tier challenges best models in agentic harnesses. All 70 solved by at least one human on first attempt. Agentic harness (Claude Code, Codex, Prime Agent) did not improve over basic harness for top tiers.

---

## 6. Industry Game AI

### 6.1 Augmenting Game AI with Deep Reinforcement Learning

- **Authors**: *(unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-06)
- **arXiv**: [2606.20210](https://arxiv.org/html/2606.20210v1)
- **Abstract & Key Innovations**: Vision paper proposing framework for training RL models suited for game AI deployment. Key requirements: **runtime inference constraints** (200μs budget), **modularity** (RL augments existing AI, doesn't replace), **fast training** (daily game changes). Demonstrates with goalkeeper RL system: 5-layer MLP, 300K params, 170μs inference. Argues RL research should prioritize small, sample-efficient architectures for real-time deployment.

### 6.2 Matrix-Game 3.0: Real-Time and Streaming Interactive World Model

- **Authors**: *(unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-04)
- **arXiv**: [2604.08995](https://arxiv.org/html/2604.08995v1)
- **Abstract & Key Innovations**: Memory-augmented interactive world model achieving **720p real-time generation at 40 FPS** with 5B model. Error-aware base model for self-correction, camera-aware memory retrieval, multi-segment autoregressive distillation (DMD), INT8 quantization + VAE pruning. Scales to 28B for improved quality. Industrial-scale data engine combining UE synthetic data + AAA game collection + real-world augmentation.

### 6.3 AI-Native Games: A Survey and Roadmap

- **Authors**: *(unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-07)
- **arXiv**: [2607.00527](https://arxiv.org/html/2607.00527v2)
- **Abstract & Key Innovations**: Defines AI-native games by whether runtime generative AI is constitutive of the core loop. Analyzes **53 publicly available AI-native games/prototypes** with dual-axis G/N taxonomy (game type × dominant AI mechanic). Corpus concentrated around language-forward designs (narrative adventure, epistemic interaction). Roadmap covers controllable generation, AI-as-mechanic design, multimodal/multi-agent systems, inference economics, evaluation, safety, and regulation.

### 6.4 WanToFight: Real-Time Generative Game Engine for Multi-Player Combat

- **Authors**: *(unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-07)
- **arXiv**: [2607.12592](https://arxiv.org/html/2607.12592v1)
- **Abstract & Key Innovations**: First generative game engine combining multi-player control + real-time inference + complex physics + adversarial gameplay. Built on Wan-1.3B: streaming autoregressive generation with block-causal attention + rolling KV cache, Player Association module (CLIP-based identity grounding), gated locally-causal keyboard injection. **30 FPS at 512×384 on single RTX 5090** via 4-step DMD distillation + pruned VAE.

### 6.5 Scalable Generative Game Engine: Breaking the Resolution Wall

- **Authors**: *(unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-02)
- **arXiv**: [2602.00608](https://arxiv.org/html/2602.00608v1)
- **Abstract & Key Innovations**: Hardware-algorithm co-design framework for generative gaming at **720×480 resolution** (50× pixel throughput increase over baselines). Heterogeneous architecture decoupling compute-bound world model from memory-bound decoder. Memory-centric operator fusion + manifold-aware latent extrapolation. **26.4 FPS (3D) / 48.3 FPS (2D)** on Ascend 910C cluster.

### 6.6 ABot-World-0: Action-Conditioned World Model for Real-Time Interaction

- **Authors**: *(unverified)*
- **Affiliation**: *(unverified)* — github: amap-cvlab/ABot-World
- **Venue**: arXiv preprint (2026-07)
- **arXiv**: [2607.19191](https://arxiv.org/html/2607.19191v1)
- **Abstract & Key Innovations**: Multi-source data infrastructure (AAA games, sim engines, internet videos) with WorldExplorer agent-driven collection. Progressive distillation: bidirectional teacher → causal student via teacher forcing + ODE distillation + **LongForcing** for long-horizon alignment. Unified keyboard control for scene roaming + character interaction. **16 FPS at 720P on single RTX 5090**, 1.2s action-to-first-frame latency, ~19 GiB VRAM.

---

## 7. Related Techniques

### 7.1 SENSEI: Semantically Sensible Exploration for Model-Based RL

- **Authors**: Cansu Sancaktar, Christian Gumbsch, Andrii Zadaianchuk, Pavel Kolev, Georg Martius
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2025-03)
- **arXiv**: [2503.01584](https://arxiv.org/pdf/2503.01584)
- **Abstract & Key Innovations**: Framework equipping model-based RL agents with intrinsic motivation for semantically meaningful behavior. Distills "interestingness" reward from VLM annotations, learns to predict via world model. Two intrinsic rewards: (1) reach states with high semantic interestingness, (2) branch out to maximize epistemic uncertainty. Demonstrated in MiniHack, Robodesk, and **Pokémon Red** — outperforms Plan2Explore and PPO by ~2 orders of magnitude on KeyRoom task.

### 7.2 JOWA: Jointly-Optimized World-Action Model for Offline RL

- **Authors**: *(unverified)*
- **Affiliation**: *(unverified)* — github: CJReinforce/JOWA
- **Venue**: arXiv preprint (2025-03, updated 2026)
- **arXiv**: [2410.00564](https://arxiv.org/html/2410.00564v3)
- **Abstract & Key Innovations**: Offline model-based RL agent pretrained across multiple Atari games with ~6B tokens. Shared transformer backbone for world modeling and Q-value criticism, stabilizing TD learning. Planning algorithm compensates for Q-value estimation error. Largest agent (150M params) achieves **78.9% human-level performance** using only 10% subsampled data. Scales favorably; sample-efficient transfer to novel games with only 5K transitions.

### 7.3 WorldLLM: Improving LLMs' World Modeling via Curiosity-Driven Theory-Making

- **Authors**: *(unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2025-06)
- **arXiv**: [2506.06725](https://arxiv.org/html/2506.06725v1)
- **Abstract & Key Innovations**: Enhances LLM-based world modeling by combining Bayesian inference and curiosity-driven RL. LLM generates natural language hypotheses given in prompt for predictions. Hypotheses iteratively refined via Bayesian inference (second LLM as proposal distribution). Curiosity-driven RL agent explores to find transitions with low log-likelihood. Demonstrated in textual game environments — improves predictive accuracy while generating human-interpretable theories.

### 7.4 Hierarchical Planning with Latent World Models (HWM)

- **Authors**: Wancong Zhang, Basile Terver, Artem Zholus, Soham Chitnis, Harsh Sutaria, Mido Assran, et al.
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-04)
- **arXiv**: [2604.03208](https://arxiv.org/html/2604.03208)
- **Abstract & Key Innovations**: Zero-shot hierarchical MPC over learned latent world models. Dynamics at multiple temporal resolutions in shared latent space; coarse predictions serve as subgoals for fine-scale MPC. Learned action encoder compresses primitive actions into latent macro-actions. First world-model planner to demonstrate **zero-shot non-greedy real-robot manipulation from pixels** — Franka pick-&-place at 70% (vs VJEPA2-AC 0%).

### 7.5 Offline RL with Hierarchical Action Chunking (HiQC)

- **Authors**: *(unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-07)
- **arXiv**: [2607.20834](https://arxiv.org/html/2607.20834)
- **Abstract & Key Innovations**: Offline goal-conditioned RL combining high-level latent planning with low-level action chunking. Low-level critic conditioned on temporally extended action sequences enables unbiased k-step value backups. Dual decomposition compresses horizon at both planning and execution levels. **Best aggregate performance on OGBench suite**, largest gains on long-horizon navigation (humanoid-giant: 33% vs HIQL 10%).

### 7.6 CARL: Reusable Skills in Offline Hierarchical RL via Local Dynamics Regularity

- **Authors**: *(unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv preprint (2026-05)
- **arXiv**: [2605.26371](https://arxiv.deeppaper.ai/papers/2605.26371v1)
- **Abstract & Key Innovations**: Learns reusable skills by aligning local contexts with required action sequences (exploiting intuition that local transitions in different global contexts require similar action sequences). CARL shows qualitative clustering of meaningful skills in complex humanoid environments and improved downstream performance on OGBench when integrated with HIQL.

---

## Cross-Cutting Trends

1. **Self-Play as Reasoning Curriculum**: SPIRAL → MARSHAL → STRATAGEM → Skill-SP show rapid progression from single-game zero-sum to multi-game cooperative+competitive self-play for LLM reasoning, with each paper addressing limitations of the previous (domain specificity, role heterogeneity, transferability).

2. **Game Foundation Models Scale to Internet Data**: NitroGen (40K hours/1000+ games, CVPR 2026), Game-TARS (500B+ tokens, ByteDance), and Pixels2Play demonstrate that internet-scale noisy data enables generalist game-playing policies with positive transfer to unseen games.

3. **NPC Intelligence Goes Multi-Layer**: WorldMind (4-layer decoupled architecture), PCSP (shared RL policy + LLM embeddings for persona), and HeRoN (RL + LLM mediated) represent three complementary approaches to scaling NPC intelligence beyond hand-authored behavior trees.

4. **Generative Game Engines Hit Real-Time**: Matrix-Game 3.0 (40 FPS/720p), WanToFight (30 FPS multiplayer), ABot-World-0 (16 FPS/720p), and the co-design framework (26-48 FPS) show the field converging on real-time neural rendering for interactive gameplay, with distillation + quantization as key enablers.

5. **Benchmarks Maturing**: GameWorld (34 games, 170 tasks, state-verifiable), OmniGameArena (UE5, PvP/Coop, IDC reflection), and DiG-bench (70 discovery games, 7 tiers) push beyond single-attempt leaderboards toward robust, multi-dimensional, and reflective evaluation.

6. **PCG Converges on Language Interfaces**: IPCGRL → VIPCGRL → Multiverse show progression from scalar to text to multi-modal (text + level + sketch) conditioning for level generation, with LLM-driven metageneration (CAD) emerging as a complementary paradigm.

7. **World Models as Game Infrastructure**: From video generation (Matrix-Game, WanToFight) to state-aware decision-making (WorldMind) to hierarchical planning (HWM), world models are becoming foundational infrastructure rather than standalone research artifacts.
