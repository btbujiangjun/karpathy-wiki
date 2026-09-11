---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-09-11)"
type: synthesis
created: 2026-09-11
updated: 2026-09-11
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, pcg, benchmarks, world-models, self-play, vlm, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-09-11)

> Comprehensive survey of recent papers (2025–2026) across Game RL, Game AI Bot, Game Foundation Models, PCG, Benchmarks, Industry Game AI, and related techniques.

---

## 1. Game RL — Reinforcement Learning in Games

### 1.1 CAST: Game Solvers as Turn-Level Teachers for LLM Agents
- **Authors**: Yu Wang, Yi-Kai Zhang, Wentao Shi, Ziang Ye, Yuchun Miao, Yueqing Sun, Qi Gu, Xunliang Cai, Lan-Zhe Guo, Han-Jia Ye, Fuli Feng
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint
- **Key Innovations**: Addresses sparse reward problem in RLVR for LLM game agents by using game solver state values as turn-level credit assignment signals. Converts solver advantage into process supervision at negligible overhead. Under soft-optimal solver assumption, maximizing solver advantage is equivalent to on-policy distillation without teacher logits. Asinh transformation + RMS normalization stabilize training.
- **Results**: Outperforms all baselines on Sokoban, Minesweeper, Rush Hour (in-domain & unseen difficulty). Highest zero-shot performance on ALFWorld and WebShop. Reaches DAPO peak in 1.7–2.0× fewer steps.
- **Link**: https://arxiv.org/pdf/2607.25308

### 1.2 Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL
- **Authors**: Chengshuai Shi, Wenzhe Li, Xinran Liang, Yizhou Lu, Wenjia Yang, Ruirong Feng, et al.
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-05)
- **Key Innovations**: First to scale RL training of VLMs to 100+ turn long-horizon game decision-making (Super Mario Land). Adapted PPO with lightweight turn-level critic for stability. Shows pretrained VLMs provide strong action priors that improve sample efficiency vs. training from scratch. Open framework combining SFT initialization + multi-task RL with auto-curriculum.
- **Results**: 3× average game progress over frontier models. Cross-game generalization to unseen levels while maintaining general-domain capabilities.
- **Link**: https://arxiv.org/abs/2605.00347

### 1.3 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint
- **Key Innovations**: Fully online multi-turn, multi-agent RL system for LLMs with distributed actor-learner architecture. Role-conditioned advantage estimation (RAE) stabilizes multi-agent training. Trains on TicTacToe, Kuhn Poker, Simple Negotiation — games naturally develop transferable reasoning patterns.
- **Results**: Up to 10% improvement across 8 reasoning benchmarks on 4 model families. Multi-game training yields strongest results. Transfers even to models already trained with RLVR (DeepSeek-R1-Distill-Qwen-7B).
- **Link**: https://arxiv.org/abs/2506.24119

### 1.4 Think in Games: Learning to Reason in Games via RL with LLMs
- **Authors**: Liao Yi, Yu Gu, Yuan Sui, Zining Zhu, Yifan Lu, Guohua Tang, et al.
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2025-08)
- **Key Innovations**: Framework for training LLMs to develop reasoning through game environments. Demonstrates that game-based RL can transfer to general reasoning tasks.
- **Link**: https://arxiv.org/abs/2508.21365

### 1.5 Agents of Change: Self-Evolving LLM Agents for Strategic Planning
- **Authors**: Belle Nikolas, Barnes Dakota, Alfonso Amayuelas, Ivan Bercovich, Xin Eric Wang, William Yang Wang
- **Affiliation**: UC Santa Cruz
- **Venue**: arXiv preprint (2025-06)
- **Key Innovations**: Multi-agent architecture (Analyzer, Researcher, Coder, Player) for autonomous prompt and code evolution in Settlers of Catan. Agents iteratively self-improve without human intervention. Demonstrates LLMs as designers of themselves.
- **Results**: Self-evolving agents with Claude 3.7 and GPT-4o outperform static baselines by autonomously adopting strategies.
- **Link**: https://arxiv.org/abs/2506.04651

---

## 2. Game AI Bot — LLM-Powered Game Agents

### 2.1 Lumine: An Open Recipe for Building Generalist Agents in 3D Open Worlds
- **Authors**: Weihao Tan, Xiangyang Li, Yunhao Fang, Heyuan Yao, Shi Yan, Hao Luo, et al.
- **Affiliation**: Nanyang Technological University / ByteDance
- **Venue**: arXiv preprint (2025-11)
- **Key Innovations**: First agent completing hours-long missions in real time in 3D open-world games (Genshin Impact). Unified perception-reasoning-action at 5Hz raw pixel input → 30Hz keyboard-mouse output. Hybrid thinking strategy for adaptive reasoning. Three-stage training: 1731h human gameplay pretraining, 200h instruction following, 15h reasoning data.
- **Results**: Completes entire 5-hour Mondstadt storyline at human-level efficiency. Zero-shot transfer to Wuthering Waves (100min) and Honkai: Star Rail (5h first chapter).
- **Link**: https://arxiv.org/abs/2511.08892

### 2.2 Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with LLMs
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-04)
- **Key Innovations**: Extends Shannon's taxonomy of game-playing machines with LLMs. Interactive agentic environment for creating LLM-powered game agents across 4 game classes: dictionary-based, solvable, heuristic-based, and learning-based. Programmable prompts as modular components.
- **Link**: https://arxiv.org/abs/2604.21896

### 2.3 Sensi: Learn One Thing at a Time — Curriculum-Based Test-Time Learning for LLM Game Agents
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-03)
- **Key Innovations**: Two-player architecture (Observer + Actor) separating perception from action for ARC-AGI-3 game-playing. Curriculum-based learning with state machine management. Database-as-control-plane using SQLite for programmable context. LLM-as-judge with dynamic rubrics.
- **Results**: Sensi v2 achieves 50–94× greater sample efficiency than comparable systems (32 vs 1,600–3,000 attempts). Diagnoses failure as hallucination cascade in perception layer.
- **Link**: https://arxiv.org/abs/2603.17683

### 2.4 LLM-Guided Reinforcement Learning for Adaptive NPC Behavior in Multi-Agent Combat Games
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-09)
- **Key Innovations**: Runtime strategy-selection framework where a local Mistral 7B LLM guides a trained PPO policy without modifying underlying behavior. Reads live game state every 5 seconds and assigns tactical tags (Surround, Flank, etc.).
- **Results**: Against Balanced opponent, win rate doubled from 11% to 24%. Shows both potential and limitations of LLM-guided strategy selection — model tends to over-select "Surround" (83.8%) regardless of opponent type.
- **Link**: https://arxiv.org/abs/2609.02931

### 2.5 Towards Generalist Game Players: An Investigation of Foundation Models in the Game Multiverse
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-05)
- **Key Innovations**: Comprehensive four-pillar pipeline (Dataset, Model, Harness, Benchmark) for generalist game players. Traces four eras from symbolic agents → RL agents → foundation models → creator stage. Five-level roadmap toward omnipotent generalist agent. Covers LLM, VLM, VLA, and World Model architectures.
- **Link**: https://arxiv.org/abs/2605.09965

---

## 3. Game Foundation Models

### 3.1 NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loic Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi Fan
- **Affiliation**: NVIDIA / UC Irvine / UW / Caltech / Georgia Tech
- **Venue**: **CVPR 2026 (Honorable Mention)**
- **Key Innovations**: Video-action foundation model trained on 40,000 hours of gameplay across 1,000+ games. Internet-scale dataset extracted from public gameplay videos with automatic action annotation. Multi-game benchmark with universal Gymnasium API. Flow matching architecture (SigLIP 2 + DiT) for visual-to-action generation.
- **Results**: Up to 52% relative improvement in task success rates via fine-tuning vs. training from scratch. Strong cross-game generalization. Open-source dataset, benchmark, and model weights.
- **Link**: https://arxiv.org/abs/2601.02427

### 3.2 Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents
- **Authors**: Z. Wang, X. Li, Y. Ye, J. Fang, H. Wang, et al.
- **Affiliation**: ByteDance Seed
- **Venue**: arXiv preprint (2025-10)
- **Key Innovations**: Unified action space anchored to native keyboard-mouse inputs (no API/GUI). Pre-trained on 500B+ tokens across game trajectories, GUI agent trajectories, and multimodal data. Decaying continual loss to reduce causal confusion. Sparse Thinking strategy balancing reasoning depth and inference cost.
- **Results**: 2× success rate over previous SOTA on Minecraft tasks. Outperforms GPT-5, Gemini-2.5-Pro, and Claude-4-Sonnet on FPS benchmarks.
- **Link**: https://arxiv.org/abs/2510.23691

### 3.3 Pixels2Play-0.1 (P2P): A Foundation Model for 3D Gameplay
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint
- **Key Innovations**: End-to-end behavior cloning from raw pixels across diverse 3D games. Uses labeled demonstrations + unlabeled public videos with inverse-dynamics model for action imputation. Decoder-only transformer with autoregressive action output. Text-conditioned for goal-directed behavior.
- **Results**: Competent play across Roblox and MS-DOS titles. Runs real-time on single RTX 5090 GPU.
- **Link**: https://arxiv.org/abs/2508.14295

### 3.4 GameVerse: Can Vision-Language Models Learn from Video-based Reflection?
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-03)
- **Key Innovations**: Reflect-and-retry paradigm for evaluating VLM agents. 15 globally popular games with cognitive hierarchical taxonomy. Dual action space (semantic + GUI). Combining failure trajectories + expert tutorials mirrors RL + SFT synergy.
- **Results**: VLMs benefit from video-based reflection. Integration of failures + tutorials outperforms either alone by 4.7–16.4%. Gemini-2.5-Pro achieves perfect scores on easy games but collapses to 0 on complex ones.
- **Link**: https://arxiv.org/abs/2603.06656

---

## 4. Procedural Content Generation (PCG)

### 4.1 Video Game Level Design as a Multi-Agent Reinforcement Learning Problem
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2025-10)
- **Key Innovations**: First to frame PCGRL as multi-agent problem. Multiple agents with local observations self-organize over noisy initial levels. Better generalization to out-of-distribution map shapes due to learning more local, modular design policies. JAX implementation with full GPU parallelization.
- **Results**: Multi-agent outperforms single-agent across all evaluation settings including OOD map shapes. Maintains advantages even when controlling for total actions and reward sparsity.
- **Link**: https://arxiv.org/abs/2510.04862

### 4.2 Multiverse: Language-Conditioned Multi-Game Level Generator
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-03)
- **Key Innovations**: Shared latent space aligning text and level structures across game domains. Threshold-based multi-positive contrastive supervision for cross-game alignment. Enables controllable blending through latent interpolation and zero-shot generation from compositional text prompts.
- **Link**: https://arxiv.org/abs/2603.26782

### 4.3 Procedural Content Metageneration via Program Search and Continual Abstraction Discovery (CAD)
- **Authors**: Matthew Siper, Ahmed Khalifa, Julian Togelius
- **Affiliation**: NYU Game Innovation Lab / University of Malta
- **Venue**: AIIDE 2026
- **Key Innovations**: LLM-driven evolutionary search over complete Python generators (not individual levels). Continual Abstraction Discovery (CAD) extracts reusable primitives from high-fitness programs into a run-specific helper module. Evaluated across Sokoban, Zelda, Dangerous Dave, Lode Runner.
- **Results**: CAD raises mean final best fitness in all 8 domain×API conditions. Learned libraries adopted by most later programs and repeatedly rediscover validation, reachability, and structural utilities.
- **Link**: https://arxiv.org/abs/2608.17947

### 4.4 VIPCGRL: Human-Aligned PCGRL via Text-Level-Sketch Shared Representation
- **Authors**: In-Chang Baek, Seoyoung Lee, Sung-Hyun Kim, Geumhwan Hwang, KyungJoong Kim
- **Affiliation**: Yonsei University / DAUM
- **Venue**: arXiv preprint (2025-08)
- **Key Innovations**: Multi-modal DRL framework incorporating text, level, and sketch modalities. Quadruple contrastive learning aligns representations across modalities and human-AI styles. Auxiliary similarity reward for human-aligned policy.
- **Results**: Outperforms baselines in human-likeness validated by both metrics and human evaluation.
- **Link**: https://arxiv.org/abs/2508.09860

### 4.5 PlayTrain: An Efficient RL Framework for LLM-Generated Adaptable JavaScript Games
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-09)
- **Key Innovations**: Combines LLM ability to generate JS games from minimal prompts with efficient RL training pipeline. Any JS game runs in standard gym environment. 1M+ agent-decisions per second on single GPU. Can clone Atari/ProcGen games in JS and create modified versions.
- **Link**: https://arxiv.org/abs/2609.09059

### 4.6 Learning Local Constraints for RL-earned Content Generators
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-05)
- **Key Innovations**: Combines Wave Function Collapse (WFC) local constraint learning with PCGRL global property optimization. WFC constrains action space of PPO-based PCGRL agent. Produces visually satisfying AND playable Lode Runner levels.
- **Link**: https://arxiv.org/abs/2605.13570

### 4.7 Distilling Game Code World Model Generation into Lightweight LLMs
- **Authors**: Tyrone Serapio, Arjun Prakash, Haoyang Xu, Kevin Wang, Amy Greenwald
- **Affiliation**: Brown University
- **Venue**: arXiv preprint (2026-05)
- **Key Innovations**: Distills Game Code World Model (GameCWM) generation from frontier models into Qwen2.5-3B via SFT + RLVR. Curated dataset of 30 games. Verification framework evaluating structural and semantic game properties. Execution-based verifier for reward signals.
- **Link**: https://arxiv.org/abs/2605.24375

---

## 5. Game Benchmarks

### 5.1 StarBench: A Turn-Based RPG Benchmark for Agentic Multimodal Decision-Making
- **Authors**: Haoran Zhang, Chenhao Zhu, Sicong Guo, Hanzhe Guo, Haiming Li, Dahai Yu
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2025-10)
- **Key Innovations**: Real-client benchmark from Honkai: Star Rail. Two regimes: direct control (pixels → actions) and tool-assisted control. Ask-or-act diagnostic measuring when agents seek guidance. Tests both perception-to-control grounding and strategic decision-making.
- **Results**: VLMs fail almost entirely in direct control. Tool assistance with textualized UI markedly improves success. Calibrated information seeking yields measurable uplifts.
- **Link**: https://arxiv.org/abs/2510.18483

### 5.2 Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games
- **Authors**: Not fully listed
- **Affiliation**: KRAFTON AI
- **Venue**: arXiv preprint (2025-06)
- **Key Innovations**: 12 video games spanning all major genres (action, adventure, RPG, simulation, strategy, puzzle). Plug-and-play interface via MCP. Includes fine-tuning dataset of expert LLM gameplay trajectories. Leaderboards, LLM battle arenas, ablation studies.
- **Results**: Gemini-2.5-pro ranks first in 5/12 games. Most small open-source LLMs (<8B) show near-zero on complex games.
- **Link**: https://arxiv.org/abs/2506.03610

### 5.3 BALROG: Benchmarking Agentic LLM and VLM Reasoning On Games
- **Authors**: Tim Rocktäschel et al.
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2025-04)
- **Key Innovations**: Six challenging RL environments (BabyAI, Crafter, TextWorld, MiniHack, etc.) spanning easy to extremely hard. Standardized 0-100 scoring. Exposes "knowing-doing gap" — models possess knowledge but fail to apply it.
- **Results**: Even best model (o1-preview) achieves only 1.57% progression on NetHack. Several models perform worse with visual representations.
- **Link**: https://arxiv.org/abs/2411.13543

### 5.4 TextAtari: 100K Frames Game Playing with Language Agents
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2025-06)
- **Key Innovations**: Translates Atari visual states to rich text descriptions. ~100 distinct tasks up to 100,000 steps. Four scenarios (Basic, Obscured, Manual Augmentation, Reference-based). Evaluates how prior knowledge affects long-horizon performance.
- **Results**: 90%+ of scenarios fall below 10% human capability. Only 2 tasks approach human performance. Game manuals and expert demos yield >100% average improvement.
- **Link**: https://arxiv.org/abs/2506.04098

### 5.5 lmgame-Bench: How Good are LLMs at Playing Games?
- **Authors**: Lanxiang Hu, Ming Huo, Yuxuan Zhang, Hongwen Yu, Eric P. Xing, Ion Stoica, et al.
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2025-05)
- **Key Innovations**: Platformer, puzzle, narrative games via unified Gym-style API. Lightweight perception and memory scaffolds. Standardized prompt optimization. Anti-contamination measures.
- **Results**: o3 and o1 achieve top-2 across all games. RL on a single game from lmgame-Bench transfers to unseen games and external planning tasks.
- **Link**: https://arxiv.org/abs/2505.15146

### 5.6 OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics
- **Authors**: Mingxian Lin, Shengju Qian, Yuqi Liu, et al.
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-06)
- **Key Innovations**: 12 newly built UE5 games (7 Solo, 3 PvP, 2 Coop). Improvement Dynamics Curve (IDC) — agentic self-reflection harness across rounds. Evaluated 12 VLM agents including commercial, open-weight, and specialized game policies.
- **Results**: GPT-5.5 leads Solo and Coop. Open-weight models score 0 on Coop games. Multi-round reflection consistently improves performance across all models.
- **Link**: https://arxiv.org/abs/2606.09826

### 5.7 AVA: Attentive VLM Agent for Mastering StarCraft II (AVACraft)
- **Authors**: Not fully listed
- **Affiliation**: CAMEL-AI
- **Venue**: ACL 2026 Findings
- **Key Innovations**: Multimodal StarCraft II benchmark supporting both MARL and VLM paradigms. RGB visuals + natural language observations. 21 scenarios spanning micromanagement, coordination, and strategic planning.
- **Results**: MARL peaks at 19.3% win rate after 5M steps. VLMs achieve 75–90% zero-shot, exposing complementary strengths between paradigms.
- **Link**: https://aclanthology.org/2026.findings-acl.208.pdf

---

## 6. Industry Game AI

### 6.1 Magpie: Real-Time World Renderer for Interactive Games
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-08)
- **Key Innovations**: Separates gameplay execution from visual generation. Game Engine resolves actions and maintains world state; independent Render Server generates visuals from white-box frames. Text + first-frame image for style initialization. 300 hours of interactive video collected in Unreal Engine.
- **Link**: https://arxiv.org/abs/2608.27168

### 6.2 Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory
- **Authors**: Yahui Zhou et al.
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-04)
- **Key Innovations**: Memory-augmented interactive world model for 720p real-time generation. Industrial-scale data engine integrating Unreal Engine + AAA game recording. Camera-aware memory retrieval for long-horizon consistency. Multi-segment autoregressive distillation (DMD) + INT8 quantization + VAE pruning.
- **Results**: 5B model achieves 40 FPS at 720p. 2×14B MoE model improves quality. Stable memory consistency over minute-long sequences.
- **Link**: https://arxiv.org/abs/2604.08995

### 6.3 Multiplayer Interactive World Models with Representation Autoencoders
- **Authors**: Anthony Hu, Václav Volhejn, Adrien Ramanana Rahary, et al.
- **Affiliation**: Kyutai / Epic Games
- **Venue**: arXiv preprint (2026-07)
- **Key Innovations**: First interactive multiplayer world model for highly dynamic environments. Conditions on action streams of multiple agents. 5B parameter latent diffusion model trained on 10,000 hours of Rocket League. Generates 4-player matches at 20 fps on single Nvidia B200. Rollouts stable far beyond training horizon.
- **Link**: https://arxiv.org/abs/2607.05352

### 6.4 Scalable Generative Game Engine: Breaking the Resolution Wall via Hardware-Algorithm Co-Design
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-01)
- **Key Innovations**: Heterogeneous computing framework decoupling world model (compute-bound) and decoder (memory-bound). Memory-centric operator fusion using on-chip SRAM. Manifold-aware latent extrapolation exploiting temporal redundancy. Validated on Ascend 910C cluster.
- **Results**: Real-time generation at 720×480 (50× increase over prior 64×64 baselines). 26.4 FPS continuous 3D racing, 48.3 FPS discrete 2D platformer. 2.7ms amortized effective latency.
- **Link**: https://arxiv.org/abs/2602.00608

### 6.5 AI Level of Detail: Distance-Aware ML Model Precision Selection for Real-Time Human Motion Prediction in Games
- **Authors**: Mathew Varghese
- **Affiliation**: SIGGRAPH 2026 Workshops
- **Venue**: SIGGRAPH Technical Workshops 2026
- **Key Innovations**: Extends classical geometry LOD to ML model inference precision. Distance-based routing to FP32/FP16/INT8 ONNX variants. INT8 achieves 9.79× latency improvement with manageable accuracy loss.
- **Link**: https://doi.org/10.1145/3799828.3816004

### 6.6 Agentic Game Development as a Verifiable Trajectory Data Engine for Scaling World Models
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-08)
- **Key Innovations**: Proposes Reinforcement Learning with Human-Engine Verification (RLHEV). Game engines provide verifiable rewards (collision, physics, navigability) analogous to compilers in code. Combines dense engine signals with implicit human acceptance feedback for RL post-training of world models.
- **Link**: https://arxiv.org/abs/2608.25518

---

## 7. Related Techniques

### 7.1 Self-Play & Population-based training

#### PopuLoRA: Co-Evolving LLM Populations for Reasoning Self-Play
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-05)
- **Key Innovations**: Population-based asymmetric self-play for RLVR. Teachers and students are specialized LoRA adapters. LoRA weight-space evolution operators (SVD mutations, DARE/TIES crossovers) for PBT replacement step at 7B scale. TrueSkill-weighted cross-evaluation.
- **Results**: Population outperforms single-agent baseline on all code (HumanEval+, MBPP+, LiveCodeBench) and math benchmarks (AIME 24/25, AMC 23, MATH-500). Even weakest population member beats baseline.
- **Link**: https://arxiv.org/abs/2605.16727

#### SCOPE: Self-Play via Co-Evolving Policies for Open-Ended Tasks
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-05)
- **Key Innovations**: First data-free self-play for open-ended tasks. Challenger generates document-grounded tasks, Solver answers via multi-turn retrieval, frozen model serves as self-judge with task-specific rubrics. Information asymmetry for sustained self-play.
- **Results**: Up to +10.4 points on open-ended benchmarks. Transfers to short-form QA (+13.8 points). Matches/exceeds GRPO trained on ~9K curated prompts.
- **Link**: https://arxiv.org/abs/2605.31433

#### OpenSIR: Open-Ended Self-Improving Reasoner
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2025-11)
- **Key Innovations**: Single LLM alternates teacher/student roles. Diversity rewards push toward unfamiliar concepts. Difficulty calibration keeps problems learnable. Starting from a single trivial seed.
- **Results**: Average +3.6 points on instruction models, +3.1 on reasoning models across 7 math benchmarks. Only self-play method that transfers to general reasoning (+4.4 points).
- **Link**: https://arxiv.org/abs/2511.00602

#### G-Zero: Self-Play for Open-Ended Generation from Zero Data
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-05)
- **Key Innovations**: Verifier-free co-evolutionary framework. Hint-δ intrinsic reward quantifies predictive shift between unassisted and hint-conditioned responses. Proposer trained via GRPO, Generator optimized via DPO. Bypasses external judges entirely.
- **Results**: +3.74 on AlpacaEval, +5.21 on AIME 25. Reasoning improvements transfer from open-ended to verifiable domains.
- **Link**: https://arxiv.org/abs/2605.09959

#### Skill Self-Play (Skill-SP): Pushing the Frontier of LLM Capability with Co-Evolving Skills
- **Authors**: Not fully listed
- **Affiliation**: Alibaba/Qwen
- **Venue**: arXiv preprint (2026-07)
- **Key Innovations**: Co-evolutionary framework with proposer, solver, and dynamic skill controller. Skills as modular packages ensuring deep verifiable execution while maintaining open-ended variety. Skill library auto-refines, prunes, and induces new skills.
- **Results**: Up to +42.9 points on tool use, +12.0 on logical reasoning.
- **Link**: https://arxiv.org/abs/2607.22529

### 7.2 World Models for Games

#### GameWAM: A World Action Model for Video Games
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-08)
- **Key Innovations**: First WAM for native closed-loop gameplay and GUI control. Jointly generates future visual observations and executable keyboard-mouse trajectories via parallel generative processes with block-causal conditioning and flow matching. Block-cycle control for long-horizon interaction.
- **Results**: Competitive task success with fewer executed native actions than compared agents. Discovers Low-Frequency Action Source Imprinting (LASI) failure mode.
- **Link**: https://arxiv.org/abs/2608.26200

#### WorldMind: Decoupled Game World Model for State-Aware NPC Behavior
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-08)
- **Key Innovations**: Four-layer decoupled framework: Understanding → Decision → Control → Generation. Explicit interface for state-grounded NPC behavior. BOSS-140K dataset of gameplay videos paired with rich internal game states.
- **Results**: Preferred over baselines in ~70% of pairwise comparisons for tactically appropriate and coherent NPC behavior.
- **Link**: https://arxiv.org/abs/2608.21439

#### ActSWM: Action-Sensitive World Models for Long-Horizon Planning in Open-World Games
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-07)
- **Key Innovations**: Identifies Context Collapse failure mode where latent predictors maintain high similarity but produce indistinguishable futures under different actions. Transition-separation principle enforces action sensitivity as constraint on latent rollouts. Enables world-model-based action recovery from offline gameplay videos.
- **Link**: https://arxiv.org/abs/2607.26712

#### Mind-Studio: Executable World Models with Lookahead Evaluation for Partially Observable Games
- **Authors**: Yifei Dong, Mingen Zheng, Linquan Wu, Jeff Z. Pan, Jiaxin Bai
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-06)
- **Key Innovations**: Synthesizes executable pygame-style world models from state-action-next-state trajectories using LLMs. Entropy-selected traces + game skill file. K-step lookahead fidelity protocol. On Montezuma's Revenge: chosen-action NSP from 0.3% (PoE-World) to 48.7%.
- **Link**: https://arxiv.org/abs/2606.16070

#### Concept-Guided Spatial Regularization for World Models in Atari Pong
- **Authors**: Ye Lu, Zaishuo Xia, Weyl Lu, Yubei Chen
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-07)
- **Key Innovations**: Evaluates 5 frozen visual world models (DreamerV3, DIAMOND, TWISTER, Simulus, STORM) in isolation. Introduces pixel-space zero-shot MBRL. Proposes CGSReg — spatial regularizer on task-critical concept regions.
- **Results**: CGSReg improves DreamerV3 (-21.00 → -11.90), DIAMOND (-13.90 → -5.80), TWISTER (-21.00 → -1.90) in zero-shot MBRL. But policies still don't solve Pong — world models remain unreliable.
- **Link**: https://arxiv.org/abs/2607.15142

#### Programmable World Model
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-09)
- **Key Innovations**: Decouples world-state evolution from visual observation generation. Agent translates NL instructions into executable programs specifying entity states and transition rules. State-augmented 3D OBBs as intermediate representation for pixel-aligned conditioning. CombatStateBench for evaluation.
- **Results**: 94% Count Accuracy, 98% State Accuracy — substantially outperforming existing interactive video world models.
- **Link**: https://arxiv.org/abs/2609.10540

### 7.3 Offline RL & Model-Based RL for Games

#### JOWA: Jointly-Optimized World-Action Model for Offline Model-Based RL
- **Authors**: Not fully listed
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint (2026-01)
- **Key Innovations**: Single offline model-based RL agent playing multiple Atari games. Shared transformer backbone for world modeling and Q-value criticism. 6B token pretraining across multiple games. Provable planning algorithm compensating Q-value estimation error.
- **Results**: 150M parameter model achieves 78.9% human-level on pretrained games with 10% subsampled data. 5K offline fine-tuning samples (≈4 trajectories) for novel game transfer. Steepest scaling curve among all algorithms.
- **Link**: https://arxiv.org/abs/2410.00564

---

## Summary Statistics

| Category | Papers Count |
|----------|-------------|
| Game RL | 5 |
| Game AI Bot | 5 |
| Game Foundation Models | 4 |
| PCG | 7 |
| Benchmarks | 7 |
| Industry Game AI | 6 |
| Related Techniques (Self-Play) | 5 |
| Related Techniques (World Models) | 5 |
| Related Techniques (Offline/Model-Based RL) | 1 |
| **Total** | **45** |

## Key Themes

1. **Foundation Models Go Multi-Game**: NitroGen (CVPR'26), Game-TARS, Pixels2Play, and Lumine all push toward generalist game agents from internet-scale data, moving beyond single-game specialization.

2. **Self-Play for LLM Post-Training**: PopuLoRA, SPIRAL, SCOPE, OpenSIR, G-Zero, and Skill-SP demonstrate that self-play — once proven for Go/Poker/Dota — is now a core paradigm for LLM reasoning improvement without human data.

3. **World Models Reach Real-Time**: Matrix-Game 3.0 (40 FPS@720p), Magpie, and the Kyutai multiplayer world model show that interactive world models are transitioning from research demos to deployable systems.

4. **PCG Goes Multi-Agent & Multi-Modal**: Multi-agent PCGRL, text-level-sketch VIPCGRL, and LLM-driven program search with CAD show PCG moving beyond single-agent RL toward richer, more controllable generation.

5. **The "Knowing-Doing Gap" Persists**: BALROG and TextAtari reveal that LLMs possess game knowledge but fail to apply it in interactive settings. The gap between knowledge and execution remains the central challenge.

6. **Benchmarks Get Harder & More Diverse**: From StarBench (real client, RPG) to OmniGameArena (UE5, PvP/Coop) to AVACraft (StarCraft II, MARL+VLM), benchmarks are evolving to test real gameplay rather than toy environments.
