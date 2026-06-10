---
title: Game RL & Game AI Bot Daily — 2026-06-10
type: synthesis
created: 2026-06-10
updated: 2026-06-10
sources: []
tags: [game-rl, game-ai, self-play, marl, foundation-models, pcg, benchmarks, world-models, curiosity, hierarchical-rl, survey]
---

# Game RL & Game AI Bot Daily — 2026-06-10

> arXiv and recent proceedings survey. Covers Game RL, Game AI Bots, Game Foundation Models, PCG, Benchmarks, Industry Game AI, and related techniques.

---

## 1. Game Reinforcement Learning (MARL, Self-Play)

### 1.1 K-Level Policy Gradients (KPG)
- **Title:** K-Level Policy Gradients: Game-Theoretic Multi-Agent RL
- **Authors:** (anonymous, under review)
- **Affiliation:** —
- **Venue:** arXiv:2509.12117, Sep 2025
- **Abstract & Innovation:** Harnesses Stackelberg game theory for N-player general-sum games. KPG generalises actor-critic MARL by recursing K levels of strategic reasoning. Reaches ε-Nash equilibrium with finite iterates. Applied to MAPPO, FACMAC, MADDPG — shows superior performance on SMAC, SMAX, and MAMuJoCo.
- **Link:** https://arxiv.org/abs/2509.12117

### 1.2 HLSMAC
- **Title:** HLSMAC: A New StarCraft Multi-Agent Challenge for High-Level Strategic Decision-Making
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2509.12927, Sep 2025
- **Abstract & Innovation:** Extends SMAC with 12 scenarios based on the Thirty-Six Stratagems, challenging agents with tactical maneuvering, timing coordination, and deception. Integrates both SOTA MARL algorithms and LLM-based agents. New metrics beyond win rate (ability utilization, advancement efficiency).
- **Link:** https://arxiv.org/abs/2509.12927

### 1.3 MARSHAL
- **Title:** MARSHAL: Incentivizing Multi-Agent Reasoning via Self-Play with Strategic LLMs
- **Authors:** (multiple, from Qwen team / academic)
- **Affiliation:** Qwen / Academic
- **Venue:** arXiv:2510.15414
- **Abstract & Innovation:** End-to-end RL framework for multi-turn, multi-agent self-play with LLMs in cooperative and competitive games. Introduces turn-level advantage estimator + agent-specific advantage normalization atop GRPO. Qwen3-4B agents improve 28.7% on held-out games. Zero-shot transfer to AIME (+10%), GPQA-Diamond (+7.6%).
- **Link:** https://arxiv.org/abs/2510.15414

### 1.4 SPIRAL
- **Title:** SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2506.24119
- **Abstract & Innovation:** Self-play framework where models learn by playing multi-turn zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation) against continuously improving versions of themselves. Proposes Role-conditioned Advantage Estimation (RAE) to stabilize multi-agent RL. Up to 10% improvement across 8 reasoning benchmarks on Qwen and Llama families. Outperforms SFT on 25K expert trajectories.
- **Link:** https://arxiv.org/abs/2506.24119

### 1.5 Foundation Model Self-Play (FMSP)
- **Title:** Foundation Model Self-Play: Open-Ended Strategy Innovation via Foundation Models
- **Authors:** (multiple)
- **Affiliation:** —
- **Venue:** arXiv:2507.06466
- **Abstract & Innovation:** Family of approaches (vFMSP, NSSP, QDSP) that use FM code-generation for open-ended strategy discovery in multi-agent games. Evaluated on Car Tag (continuous control) and Gandalf (LLM jailbreaking). QDSP discovers diverse high-quality policies; FMSPs can automatically red-team and patch LLM vulnerabilities.
- **Link:** https://arxiv.org/abs/2507.06466

### 1.6 SPIRAL (Odysseus)
- *See Section 3.2 for Odysseus (VLM + RL for long-horizon game play).*

### 1.7 SCOPE
- **Title:** SCOPE: Self-Play via Co-Evolving Policies for Open-Ended Tasks
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2605.31433
- **Abstract & Innovation:** First framework extending data-free self-play to open-ended tasks (no verifiable answers). Co-evolves Challenger (task generation) and Solver (task solving) with a fixed frozen-base Judge writing rubrics. Uses rubric-based rewards instead of rule-based verifiers. Works on document-grounded tasks.
- **Link:** https://arxiv.org/abs/2605.31433

### 1.8 G-Zero
- **Title:** G-Zero: Self-Play for Open-Ended Generation from Zero Data
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2605.09959
- **Abstract & Innovation:** Verifier-free co-evolutionary framework using Hint-δ intrinsic reward — measures predictive shift between a Generator's unassisted response vs. hint-conditioned response. Proposer trained via GRPO to target Generator blind spots; Generator optimized via DPO. Bypasses external judge capability ceilings.
- **Link:** https://arxiv.org/abs/2605.09959

### 1.9 Scaling Self-Play with Self-Guidance (SGS)
- **Title:** Scaling Self-Play with Self-Guidance
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2604.20209
- **Abstract & Innovation:** Asymmetric self-play with three roles (Solver, Conjecturer, Guide). Guide scores synthetic problems by relevance and clarity, preventing Conjecturer degradation over long training runs.
- **Link:** https://arxiv.org/abs/2604.20209

### 1.10 OpenSIR
- **Title:** Open-Ended Self-Improving Reasoner (OpenSIR)
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2511.00602
- **Abstract & Innovation:** Self-play where LLM alternates teacher/student roles to generate and solve novel problems without external supervision. Optimizes for difficulty + diversity rewards. Achieves open-ended learning from basic to advanced mathematics.
- **Link:** https://arxiv.org/abs/2511.00602

### 1.11 PopuLoRA
- **Title:** PopuLoRA: Co-Evolving LLM Populations for Reasoning Self-Play
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2605.16727
- **Abstract & Innovation:** Population-based asymmetric self-play for RLVR. LoRA adapters on shared frozen base. Teachers propose problems, students solve. LoRA weight-space evolution operators (mutations/crossovers in seconds). Co-evolutionary arms race avoids self-calibration collapse.
- **Link:** https://arxiv.org/abs/2605.16727

### 1.12 π-Play
- **Title:** π-Play: Multi-Agent Self-Play via Privileged Self-Distillation without External Data
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2604.14054
- **Abstract & Innovation:** Self-play produces question construction paths (QCPs) — used as privileged context for teacher-student self-distillation. Transforms sparse-reward self-play into dense-feedback self-evolution. Outperforms fully supervised search agents.
- **Link:** https://arxiv.org/abs/2604.14054

### 1.13 MARL-GPT
- **Title:** MARL-GPT: Foundation Model for Multi-Agent Reinforcement Learning
- **Authors:** (CogAI Systems / academic)
- **Affiliation:** Cognitive AI Systems
- **Venue:** arXiv:2604.05943
- **Abstract & Innovation:** Single GPT-based model trained via offline RL on expert trajectories (400M SMACv2, 100M GRF, 1B POGEMA) with transformer observation encoder. Competitive across diverse MARL environments without task-specific tuning.
- **Link:** https://arxiv.org/abs/2604.05943

### 1.14 LaMer
- **Title:** Meta-RL Induces Exploration in Language Agents
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2512.16848
- **Abstract & Innovation:** Meta-RL framework for LLM agents with cross-episode training + in-context policy adaptation via reflection. +11%/14%/19% on Sokoban/MineSweeper/Webshop.
- **Link:** https://arxiv.org/abs/2512.16848

### 1.15 PokeRL
- **Title:** PokeRL: A Modular RL System for Early-Game Pokemon Red
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2604.10812, Apr 2026
- **Abstract & Innovation:** PPO agents for Pokemon Red early-game tasks with loop masking, anti-spam mechanisms, dense hierarchical reward design, and curriculum over 3 sequences.
- **Link:** https://arxiv.org/abs/2604.10812

### 1.16 SeRL
- **Title:** SeRL: Self-Play Reinforcement Learning for Large Language Models with Limited Data
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2505.20347
- **Abstract & Innovation:** Self-instruction + self-rewarding modules bootstrap LLM RL training with minimal initial data. Majority-voting reward estimation. On par with verifiable-reward methods.
- **Link:** https://arxiv.org/abs/2505.20347

---

## 2. Game AI Bots (LLM-Powered)

### 2.1 Continual Harness
- **Title:** Continual Harness: Online Adaptation for Self-Improving Foundation Agents
- **Authors:** (Gemini team)
- **Affiliation:** Google DeepMind
- **Venue:** arXiv:2605.09998
- **Abstract & Innovation:** Automates manual harness refinement for LLM game agents. Extends Gemini Plays Pokémon (GPP) — first AI to complete multiple Pokémon RPGs (Blue, Yellow Legacy, Crystal). Uses online in-context learning: agent alternates between acting and refining system prompt/sub-agents/skills/memory mid-episode via Refiner.
- **Link:** https://arxiv.org/abs/2605.09998

### 2.2 Sensi
- **Title:** Sensi: Learn One Thing at a Time — Curriculum-Based Test-Time Learning for LLM Game Agents
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2603.17683
- **Abstract & Innovation:** Two-player architecture (perception vs. action) + curriculum-based learning + database-as-control-plane for ARC-AGI-3. Achieves 50–94× sample efficiency over baselines (completes curriculum in ~32 interactions vs 1600–3000).
- **Link:** https://arxiv.org/abs/2603.17683

### 2.3 Bounded Autonomy
- **Title:** Bounded Autonomy: Controlling LLM Characters in Live Multiplayer Games
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2604.04703
- **Abstract & Innovation:** Control architecture for LLM NPCs in live multiplayer games. Three interfaces: agent-agent, agent-world, player-agent. Probabilistic reply-chain decay, embedding-based action grounding, and "whisper" soft-steering.
- **Link:** https://arxiv.org/abs/2604.04703

### 2.4 MineNPC-Task
- **Title:** MineNPC-Task: Task Suite for Memory-Aware Minecraft Agents
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2601.05215
- **Abstract & Innovation:** User-authored benchmark for memory-aware LLM agents in Minecraft. 216 subtasks from expert co-play with parametric templates, precondition checks, and bounded-knowledge policy. GPT-4o evaluated.
- **Link:** https://arxiv.org/abs/2601.05215

### 2.5 HER
- **Title:** HER: Human-like Reasoning and Reinforcement Learning for LLM Role-playing
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2601.21459
- **Abstract & Innovation:** Dual-layer thinking (first-person character thinking vs third-person LLM thinking) for LLM role-playing. Reverse-engineered reasoning-augmented data. RL with self-principled generative reward model. 30.26% improvement on CoSER benchmark.
- **Link:** https://arxiv.org/abs/2601.21459

### 2.6 Codified Finite-State Machines for Role-playing
- **Title:** Codified Finite-State Machines for Role-playing
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2602.05905
- **Abstract & Innovation:** CFSM/CPFSM framework using LLM-based coding to extract character state machines from textual profiles. Probabilistic transitions. Outperforms prompting-based baselines in role-playing consistency.
- **Link:** https://arxiv.org/abs/2602.05905

### 2.7 LLM-Driven NPCs: Cross-Platform Dialogue
- **Title:** LLM-Driven NPCs: Cross-Platform Dialogue System for Games and Social Platforms
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2504.13928, Apr 2025
- **Abstract & Innovation:** Prototype integrating DeepSeek-R1 with Unity + Discord for cross-platform NPC dialogue. Cloud database for synchronized memory.
- **Link:** https://arxiv.org/abs/2504.13928

### 2.8 PORTAL
- **Title:** PORTAL: Agents Play Thousands of 3D Video Games
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2503.13356, Mar 2025
- **Abstract & Innovation:** LLM generates specialized Behavior Trees (BTs) in DSL for game-playing across thousands of 3D games. Decouples tactical planning from execution — real-time performance without RL training costs.
- **Link:** https://arxiv.org/abs/2503.13356

### 2.9 OpenGame
- **Title:** OpenGame: Open Agentic Coding for Games
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2604.18394
- **Abstract & Innovation:** First open-source agentic framework for end-to-end web game creation. GameCoder-27B (CPT + SFT + RL). Three-stage pipeline. OpenGame-Bench for dynamic evaluation across 150 game prompts. Also trains game-playing LLM.
- **Link:** https://arxiv.org/abs/2604.18394

---

## 3. Game Foundation Models

### 3.1 NitroGen
- **Title:** NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors:** Magne et al.
- **Affiliation:** NVIDIA / MineDojo
- **Venue:** CVPR 2026
- **Abstract & Innovation:** Vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games. Automatically extracts actions from public videos. Universal Gymnasium API for any game. Up to 52% relative improvement on unseen games via fine-tuning. Open-source weights, data, and eval suite.
- **Link:** https://arxiv.org/abs/2601.02427

### 3.2 Odysseus
- **Title:** Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2605.00347
- **Abstract & Innovation:** PPO with lightweight turn-level critic for VLM long-horizon game play (Super Mario Land, 100+ turns). Shows critic-based PPO > GRPO/Reinforce++ for long-horizon. Pretrained VLMs provide strong action priors. 3× game progress over frontier models. Cross-game generalization.
- **Link:** https://arxiv.org/abs/2605.00347

### 3.3 Game-TARS
- **Title:** Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents
- **Authors:** Wang et al.
- **Affiliation:** SEED / Tencent
- **Venue:** arXiv:2510.23691
- **Abstract & Innovation:** Unified action space (keyboard-mouse). Pre-trained on 500B+ tokens across OS, web, and games. Decaying continual loss + Sparse-Thinking strategy. 2× SOTA in Minecraft; nears human-level in unseen web 3D games; outperforms GPT-5, Gemini 2.5 Pro, Claude 4 Sonnet on FPS benchmarks.
- **Link:** https://arxiv.org/abs/2510.23691

### 3.4 Scaling Behavior Cloning — Pixels2Play (P2P)
- **Title:** Scaling Behavior Cloning Improves Causal Reasoning: An Open Model for Real-Time Video Game Playing
- **Authors:** (anonymous, Elefant AI)
- **Affiliation:** Elefant AI
- **Venue:** arXiv:2601.04575
- **Abstract & Innovation:** Open recipe for real-time game-playing foundation model on consumer GPU. 8,300+ hours of high-quality human gameplay. Models up to 1.2B params. Scaling laws show BC improves causal reasoning. Real-time 20 Hz inference on RTX 5090.
- **Link:** https://arxiv.org/abs/2601.04575

### 3.5 Towards Generalist Game Players (Survey)
- **Title:** Towards Generalist Game Players: An Investigation of Foundation Models in the Game Multiverse
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2605.09965, May 2026
- **Abstract & Innovation:** Comprehensive survey of LFMs as generalist game players across four pillars (Dataset, Model, Harness, Benchmark). Four evolutionary eras: symbolic → DRL → foundation models → future creator stage. Five fundamental trade-offs. Five-level roadmap to AGI via games.
- **Link:** https://arxiv.org/abs/2605.09965

### 3.6 GameVerse
- **Title:** GameVerse: Can Vision-Language Models Learn from Video-based Reflection?
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2603.06656
- **Abstract & Innovation:** Benchmark with reflect-and-retry paradigm. 15 games, dual action space. Combining failure reflection + expert tutorials mirrors SFT+RL. Training-free paradigm for VLM game agents.
- **Link:** https://arxiv.org/abs/2603.06656

### 3.7 G1 (mentioned in Towards Generalist survey)
- Referenced as training VLMs via RL self-evolution in multi-game environments, where perception and reasoning mutually bootstrap.

---

## 4. Procedural Content Generation (RL + LLM + PCG)

### 4.1 IPCGRL
- **Title:** IPCGRL: Language-Instructed Reinforcement Learning for Procedural Level Generation
- **Authors:** Baek et al.
- **Affiliation:** —
- **Venue:** IEEE CoG 2025
- **Abstract & Innovation:** Instruction-based PCG via RL with sentence embedding model. Fine-tunes task-specific embeddings to compress game-level conditions. 21.4% controllability improvement, 17.2% generalization improvement on 2D level generation.
- **Link:** https://arxiv.org/abs/2503.12358

### 4.2 Multi-Agent PCGRL
- **Title:** Video Game Level Design as a Multi-Agent Reinforcement Learning Problem
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2510.04862, Oct 2025
- **Abstract & Innovation:** Frames level generation as multi-agent problem — multiple embodied generators with local observations. Reduces reward calc bottleneck, improves generalization to out-of-distribution map shapes. Open-sourced on GPU-parallelized PCGRL.
- **Link:** https://arxiv.org/abs/2510.04862

### 4.3 VIPCGRL
- **Title:** Human-Aligned Procedural Level Generation via Text-Level-Sketch Shared Representation
- **Authors:** Baek, Kim et al.
- **Affiliation:** —
- **Venue:** arXiv:2508.09860
- **Abstract & Innovation:** Three-modality PCGRL (text, level grid, sketches). Quadruple contrastive learning for shared embedding. Auxiliary reward for human-likeness alignment.
- **Link:** https://arxiv.org/abs/2508.09860

### 4.4 Procedural Game Level Design with DRL
- **Title:** Procedural Game Level Design with Deep Reinforcement Learning
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2510.15120, Oct 2025
- **Abstract & Innovation:** Two-agent system in Unity 3D: Hummingbird (solver) + Island (flower generator). Both trained with PPO. Co-adaptive emergent behavior for automated level design.
- **Link:** https://arxiv.org/abs/2510.15120

### 4.5 Database-Driven 3D Level Generation with LLMs
- **Title:** A Database-Driven Framework for 3D Level Generation with LLMs
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2508.18533
- **Abstract & Innovation:** Offline LLM-assisted construction of reusable databases (Room, Facility, Mechanics DBs). Multi-phase pipeline + two-phase repair system. No live LLM calls during generation.
- **Link:** https://arxiv.org/abs/2508.18533

### 4.6 WFC + PCGRL Hybrid
- **Title:** Learning Local Constraints for Reinforcement-Learned Content Generators
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2605.13570
- **Abstract & Innovation:** Combines Wave Function Collapse (local constraints) with PCGRL (global playability) for Lode Runner levels. PPO agent selects tile patterns within WFC constraints.
- **Link:** https://arxiv.org/abs/2605.13570

### 4.7 PCGRLLM
- **Title:** PCGRLLM: Large Language Model-Driven Reward Design for Procedural Content Generation Reinforcement Learning
- **Authors:** Baek et al.
- **Affiliation:** —
- **Venue:** arXiv:2502.10906, Feb 2025
- **Abstract & Innovation:** LLM designs reward functions for PCGRL agents autonomously. Automates the reward engineering bottleneck in RL-based PCG.
- **Link:** https://arxiv.org/abs/2502.10906

### 4.8 CreativeGame
- **Title:** CreativeGame: Multi-Agent Iterative Game Generation with Proxy Rewards
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2604.19926
- **Abstract & Innovation:** Multi-agent system for iterative HTML5 game generation. Proxy reward (programmatic signals), lineage-scoped memory, mechanic-guided planning loop. 7 agents, 10 roles.
- **Link:** https://arxiv.org/abs/2604.19926

### 4.9 High Dimensional PCG
- **Title:** High Dimensional Procedural Content Generation (HDPCG)
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2602.18943
- **Abstract & Innovation:** Extends PCG with additional gameplay dimensions (layers, time, locomotion modes). Encodes world state as attribute-labeled cells over expanded state space. Multi-tier planners with bounded-suboptimal search.
- **Link:** https://arxiv.org/abs/2602.18943

### 4.10 Multiverse
- **Title:** Multiverse: Language-Conditioned Multi-Game Level Generator
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2603.26782, Mar 2026
- **Abstract & Innovation:** Cross-game contrastive learning for language-conditioned level generation across game domains. Conditional VQ-VAE. Enables level blending — combining structural attributes from multiple source games.
- **Link:** https://arxiv.org/abs/2603.26782

### 4.11 DreamGarden
- **Title:** DreamGarden: A Designer Assistant for Growing Games from a Single Prompt
- **Authors:** Earle, Parajuli, Banburski-Fahey
- **Affiliation:** —
- **Venue:** CHI 2025
- **Abstract & Innovation:** Designer assistant that grows complete games from a single natural language prompt.
- **Link:** (CHI 2025 proceedings)

### 4.12 AutoUE
- **Title:** AutoUE: Automated Generation of 3D Games in Unreal Engine via Multi-Agent Systems
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2603.07106
- **Abstract & Innovation:** Multi-agent system for end-to-end 3D game generation in UE5. RAG for tool docs, C++ gameplay code generation, automated play-testing.
- **Link:** https://arxiv.org/abs/2603.07106

---

## 5. Game Benchmarks

### 5.1 Orak
- **Title:** Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games
- **Authors:** Park et al.
- **Affiliation:** KRAFTON AI
- **Venue:** arXiv:2506.03610
- **Abstract & Innovation:** 12 popular video games across all major genres. MCP-based plug-and-play interface. Fine-tuning dataset of expert LLM gameplay trajectories. Game leaderboards + LLM battle arenas.
- **Link:** https://arxiv.org/abs/2506.03610

### 5.2 GameWorld
- **Title:** GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2604.07429
- **Abstract & Innovation:** 34 browser games across 5 genres, 170 tasks. Sandbox decouples inference latency. State-verifiable evaluator. Studies 18 model–interface pairs. Real-time variant GameWorld-RT. Capability-aligned curriculum analysis.
- **Link:** https://arxiv.org/abs/2604.07429

### 5.3 VideoGameBench
- **Title:** VideoGameBench: Can Vision-Language Models Complete Popular Video Games?
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2505.18134
- **Abstract & Innovation:** 10 popular 1990s games (3 secret). Raw visual input only. Frontier VLMs complete only 0.48% (real-time) / 1.6% (paused). Gemini 2.5 Pro and Claude 3.7 Sonnet best among tested.
- **Link:** https://arxiv.org/abs/2505.18134

### 5.4 BALROG
- **Title:** BALROG: Benchmarking Agentic LLM and VLM Reasoning On Games
- **Authors:** Paglieri et al.
- **Affiliation:** —
- **Venue:** arXiv:2411.13543
- **Abstract & Innovation:** Aggregates 6 RL game environments (BabyAI, Crafter, TextWorld, Baba Is AI, MiniHack, NetHack). Procedurally generated — no memorization. Fine-grained 0–100 metric; data-informed NetHack progression system.
- **Link:** https://arxiv.org/abs/2411.13543

### 5.5 GameDevBench
- **Title:** GameDevBench: Evaluating Agentic Capabilities Through Game Development
- **Authors:** Chi et al.
- **Affiliation:** —
- **Venue:** arXiv:2602.11103
- **Abstract & Innovation:** First benchmark for agents on game development tasks. 132 tasks from Godot tutorials. 3× more complex than SWE-Bench. Best agent solves only 54.5%. Image/video feedback improves performance.
- **Link:** https://arxiv.org/abs/2602.11103

### 5.6 CUBE
- **Title:** CUBE: A Standard for Unifying Agent Benchmarks
- **Authors:** Lacoste et al.
- **Affiliation:** The Alliance
- **Venue:** arXiv:2603.15798
- **Abstract & Innovation:** Universal protocol standard unifying benchmark interfaces. Any CUBE-compliant benchmark works with any CUBE-compliant eval framework.
- **Link:** https://arxiv.org/abs/2603.15798

### 5.7 Survey on Evaluation of LLM-based Agents
- **Title:** A Survey on Evaluation of LLM-based Agents
- **Authors:** Yehudai et al.
- **Affiliation:** —
- **Venue:** arXiv:2503.16416
- **Abstract & Innovation:** First comprehensive survey of evaluation methods for LLM-based agents across 5 perspectives. Covers game agent evaluation. Trends toward realistic, challenging, continuously updated benchmarks.
- **Link:** https://arxiv.org/abs/2503.16416

---

## 6. Industry Game AI

### 6.1 Pareto-Guided Distillation for Mobile MOBA
- **Title:** Pareto-guided Pipeline for Distilling Featherweight AI Agents in Mobile MOBA Games
- **Authors:** (anonymous)
- **Affiliation:** Tencent (Honor of Kings team)
- **Venue:** arXiv:2602.07521
- **Abstract & Innovation:** Distills Honnor of Kings AI into mobile-deployable agents. 12.4× faster inference (<0.5ms/frame), 15.6× energy efficiency improvement. Retains 40.32% win rate against teacher. Deployed on iQOO 12 phone (Snapdragon 8 Gen 3).
- **Link:** https://arxiv.org/abs/2602.07521

### 6.2 NVIDIA NVIGI SDK
- **Title:** NVIGI — In-Game Inferencing SDK
- **Affiliation:** NVIDIA
- **Venue:** SDK documentation (v1.6.0)
- **Abstract & Innovation:** Production SDK for GPU-accelerated AI inference in 3D games. Integrates LLMs (GGML, CUDA, D3D12), TensorRT. Non-blocking polling for game engine ticks.
- **Link:** https://docs.nvidia.com/nvigi-sdk/

### 6.3 Unreal Engine NNE + TensorRT for RTX
- **Title:** Speed Up Unreal Engine NNE Inference with NVIDIA TensorRT for RTX Runtime
- **Author:** Homam Bahnassi
- **Affiliation:** NVIDIA
- **Venue:** NVIDIA Developer Blog, Apr 2026
- **Abstract & Innovation:** TensorRT for RTX plugin as NNE runtime in UE5. JIT optimizer generates GPU-specific inference engines. 1.5× faster than DirectML (3.8ms vs 5.7ms on RTX 5090).
- **Link:** https://developer.nvidia.com/blog/speed-up-unreal-engine-nne-inference-with-nvidia-tensorrt-for-rtx-runtime/

### 6.4 Game-TARS (also in §3.3)
- SEED / Tencent's generalist game agent. See §3.3.

### 6.5 NitroGen (also in §3.1)
- NVIDIA's generalist game playing foundation model. See §3.1.

### 6.6 UniGen
- **Title:** 90% Faster, 100% Code-Free: MLLM-Driven Zero-Code 3D Game Development
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2509.26161
- **Abstract & Innovation:** End-to-end zero-coding 3D game generation from natural language. Unity C# generation. 91.4% development time reduction.
- **Link:** https://arxiv.org/abs/2509.26161

---

## 7. World Models & Model-Based RL for Games

### 7.1 Matrix-Game
- **Title:** Matrix-Game: Interactive World Foundation Model
- **Authors:** (Skywork AI)
- **Affiliation:** Skywork AI
- **Venue:** arXiv:2506.18701
- **Abstract & Innovation:** Interactive world foundation model for controllable game world generation. 17B params. 2,700h unlabeled + 1,000h labeled Minecraft video. GameWorld Score benchmark. Outperforms Oasis and MineWorld in controllability and physical consistency.
- **Link:** https://arxiv.org/abs/2506.18701

### 7.2 Matrix-Game 3.0
- **Title:** Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory
- **Authors:** (Skywork AI)
- **Affiliation:** Skywork AI
- **Venue:** arXiv:2604.08995
- **Abstract & Innovation:** Real-time streaming interactive generation with long-horizon memory consistency. Causal autoregressive few-step diffusion + memory mechanism for minute-long consistency.
- **Link:** https://arxiv.org/abs/2604.08995

### 7.3 WorldCam
- **Title:** WorldCam: Interactive Autoregressive 3D Gaming Worlds with Camera Pose as a Unifying Geometric Representation
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2603.16871
- **Abstract & Innovation:** Uses camera pose as unifying geometric representation for action control and 3D consistency. Video DiT backbone. 3,000 minutes of human gameplay annotated with camera trajectories. Physics-based continuous action space (Lie algebra).
- **Link:** https://arxiv.org/abs/2603.16871

### 7.4 LingBot-World
- **Title:** Advancing Open-source World Models
- **Authors:** (LingBot team)
- **Affiliation:** LingBot
- **Venue:** arXiv:2601.20540
- **Abstract & Innovation:** Open-source world simulator. High fidelity across realism, science, cartoon. Minute-level horizon consistency. Real-time interactivity (<1s latency at 16fps).
- **Link:** https://arxiv.org/abs/2601.20540

### 7.5 RLVR-World
- **Title:** RLVR-World: Training World Models with Reinforcement Learning
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2505.13934
- **Abstract & Innovation:** Unified RLVR framework for training world models. Autoregressive token prediction + verifiable rewards on decoded predictions. +30.7% accuracy on text game state prediction; +15.1% F1 on web page prediction.
- **Link:** https://arxiv.org/abs/2505.13934

### 7.6 Code World Models (CWM)
- **Title:** Code World Models: LLM-Generated Game Models via Python Code
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2510.04542, Oct 2025
- **Abstract & Innovation:** LLMs translate game rules + trajectories into executable Python world models. Search-based policies (MCTS, ISMCTS) with CWM. Outperforms "thinking" LLMs in two-player games.
- **Link:** https://arxiv.org/abs/2510.04542

### 7.7 Distilling Game Code World Models
- **Title:** Distilling Game Code World Model Generation into Lightweight Large Language Models
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2605.24375
- **Abstract & Innovation:** Distills GameCWM generation into Qwen2.5-3B via SFT + RLVR. Dataset of 30 games. GRPO with execution-based verifier.
- **Link:** https://arxiv.org/abs/2605.24375

### 7.8 Agent World Model (AWM)
- **Title:** Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning
- **Authors:** (Snowflake Labs)
- **Affiliation:** Snowflake Labs
- **Venue:** arXiv:2602.10090, Feb 2026
- **Abstract & Innovation:** Fully synthetic environment generation pipeline via code + databases. 1,000 environments with 35 tools each. Reliable state transitions. Large-scale RL for tool-use agents shows strong OOD generalization.
- **Link:** https://arxiv.org/abs/2602.10090

### 7.9 Reinforcement World Model Learning (RWML)
- **Title:** Reinforcement World Model Learning for LLM-based Agents
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2602.05842
- **Abstract & Innovation:** Self-supervised RL method learning action-conditioned world models for LLM agents. Sim-to-real gap rewards in embedding space. +19.6 on ALFWorld without expert data.
- **Link:** https://arxiv.org/abs/2602.05842

### 7.10 Remember to be Curious
- **Title:** Remember to be Curious: Episodic Context and Persistent Worlds for 3D Exploration
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2605.22814
- **Abstract & Innovation:** Curiosity-driven exploration using persistent online 3D reconstruction as forward model. Episodic memory for planning. Outperforms active-mapping baselines on HM3D, zero-shot to Gibson and AI-generated worlds.
- **Link:** https://arxiv.org/abs/2605.22814

---

## 8. Curiosity, Exploration, Hierarchical RL, Imitation & Inverse RL

### 8.1 CDE (Curiosity-Driven Exploration)
- **Title:** CDE: Curiosity-Driven Exploration for Efficient Reinforcement Learning in Large Language Models
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2509.09675, Sep 2025
- **Abstract & Innovation:** Curiosity signals from both actor (perplexity) and critic (multi-head value variance). Actor-wise bonus penalizes overconfident errors. Critic-wise bonus ≈ count-based exploration. +3 points on AIME with GRPO/PPO.
- **Link:** https://arxiv.org/abs/2509.09675

### 8.2 CuES
- **Title:** CuES: A Curiosity-driven and Environment-grounded Synthesis Framework for Agentic RL
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2512.01311
- **Abstract & Innovation:** Autonomous task generation via intrinsic curiosity. Abstracts interaction patterns into reusable task schemas. Tested on AppWorld, BFCL, WebShop.
- **Link:** https://arxiv.org/abs/2512.01311

### 8.3 OGER
- **Title:** OGER: A Robust Offline-Guided Exploration Reward for Hybrid Reinforcement Learning
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2604.18530
- **Abstract & Innovation:** Unifies offline teacher guidance + online RL. Multi-teacher collaborative training + divergence-based exploration reward + entropy-aware modulation. For LLM reasoning.
- **Link:** https://arxiv.org/abs/2604.18530

### 8.4 RAPO
- **Title:** RAPO: Expanding Exploration for LLM Agents via Retrieval-Augmented Policy Optimization
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2603.03078
- **Abstract & Innovation:** Retrieval-augmented exploration for agentic RL. Hybrid-policy rollout + retrieval reward + importance shaping. Retrieval broadens step-level exploration.
- **Link:** https://arxiv.org/abs/2603.03078

### 8.5 SPEAR (Self-Imitation Learning)
- **Title:** Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2509.22601
- **Abstract & Innovation:** Self-imitation learning with curriculum scheduling for exploration-exploitation balance. Scheduled entropy + intrinsic rewards. +16.1% on ALFWorld, +20.7% on WebShop.
- **Link:** https://arxiv.org/abs/2509.22601

### 8.6 Cago
- **Title:** Cago: Capability-Aware Goal Sampling for Learning from Demonstrations
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2601.08731
- **Abstract & Innovation:** Novel learning-from-demonstrations method using demonstrations as structured roadmaps. Tracks agent competence along demonstration trajectories; samples goals just beyond current capability. Bridges imitation + RL.
- **Link:** https://arxiv.org/abs/2601.08731

### 8.7 IRL for Reasoning (Process-Level)
- **Title:** Inverse Reinforcement Learning for Process-Level Reasoning from Expert Demonstrations
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2510.01857
- **Abstract & Innovation:** Formulates process-level reasoning as IRL to learn dense token-level reward models from expert traces. Token-wise feedback for training + inference reranking + error localization.
- **Link:** https://arxiv.org/abs/2510.01857

### 8.8 QD-IRL + EBC
- **Title:** Diversifying Policy Behaviors with Extrinsic Behavioral Curiosity
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2410.06151
- **Abstract & Innovation:** Quality-Diversity Inverse RL (QD-IRL) + Extrinsic Behavioral Curiosity (EBC). Diverse policy archive with curiosity rewards from external critic. Up to 185% improvement on locomotion tasks.
- **Link:** https://arxiv.org/abs/2410.06151

### 8.9 STEP-HRL (Hierarchical RL for LLM Agents)
- **Title:** Hierarchical Reinforcement Learning with Augmented Step-Level Transitions for LLM Agents
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2604.05808, Apr 2026
- **Abstract & Innovation:** HRL for LLM agents using completed subtasks as global progress + local progress module for compact summaries. Step-level transitions (not full histories). Outperforms baselines on ScienceWorld, ALFWorld with reduced token usage.
- **Link:** https://arxiv.org/abs/2604.05808

### 8.10 HGPO
- **Title:** Hierarchy-of-Groups Policy Optimization for Long-Horizon Agentic Tasks
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2602.22817
- **Abstract & Innovation:** Context-aware hierarchical grouping + adaptive weighting advantage estimation for long-horizon agentic RL. Outperforms baselines on ALFWorld and WebShop.
- **Link:** https://arxiv.org/abs/2602.22817

### 8.11 HiPER
- **Title:** HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2602.16165
- **Abstract & Innovation:** Plan–Execute hierarchical RL with Hierarchical Advantage Estimation (HAE). Separates high-level planner from low-level executor. Unbiased gradient with provably reduced variance.
- **Link:** https://arxiv.org/abs/2602.16165

### 8.12 STO-RL
- **Title:** STO-RL: Offline RL using LLM-Guided Subgoal Temporal Order
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2601.08107
- **Abstract & Innovation:** LLM generates temporally ordered subgoals + potential-based reward shaping for offline RL. Transforms sparse rewards into dense signals. Tested on FourRoom, CliffWalking, PointMaze.
- **Link:** https://arxiv.org/abs/2601.08107

### 8.13 SPAARS
- **Title:** SPAARS: Safer RL Policy Alignment through Abstract Exploration and Refined Exploitation of Action Space
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2603.09378, Mar 2026
- **Abstract & Innovation:** Curriculum framework for safe offline-to-online RL. Starts with latent-space exploration (CVAE), then transfers to raw action space. Provable exploitation gap bound. 5× sample efficiency.
- **Link:** https://arxiv.org/abs/2603.09378

### 8.14 NF-HIQL
- **Title:** Data-Efficient Hierarchical Goal-Conditioned RL via Normalizing Flows
- **Authors:** (anonymous)
- **Affiliation:** —
- **Venue:** arXiv:2602.11142
- **Abstract & Innovation:** Normalizing flow policies for both high- and low-level in H-GCRL. KL-divergence bounds + PAC-style guarantees. Outperforms diffusion-based methods (BESO). Matches full-dataset baselines with 50% data.
- **Link:** https://arxiv.org/abs/2602.11142

---

## 9. Key Themes & Trends

1. **Self-play goes open-ended**: SPIRAL, SCOPE, G-Zero, OpenSIR, PopuLoRA — self-play is moving beyond verifiable tasks toward rubric-based and intrinsic-reward-driven open-ended learning.
2. **Foundation models as game agents**: NitroGen (CVPR 2026), Game-TARS, Odysseus — massive BC/RL pre-training yields generalist game-playing agents that approach/beat humans and frontier models.
3. **RL for VLM game agents**: Odysseus shows PPO + turn-level critic works for 100+ turn game play, out-performing GRPO/Reinforce++ in long-horizon settings.
4. **MARL + LLMs**: MARSHAL, MARL-GPT, HLSMAC — LLMs are being integrated into MARL pipelines as both policies and strategic reasoners.
5. **Industry deployment maturing**: Tencent's HoK distillation for mobile, NVIDIA's NVIGI SDK, UE5 NNE + TensorRT — game AI deployment is becoming practical.
6. **PCG meets LLMs**: IPCGRL, PCGRLLM, VIPCGRL, AutoUE — language-conditioned and LLM-driven PCG for levels, rewards, and entire games.
7. **World models are real**: Matrix-Game (17B), LingBot-World, WorldCam — interactive world models with real-time generation, long-horizon consistency, and action control.
8. **Benchmarks proliferate**: Orak, GameWorld, VideoGameBench, BALROG — each testing different aspects of game agent capability (LLM vs VLM, real-time vs paused, etc.).

---

## Paper Count Summary

| Category | Count |
|----------|-------|
| Game RL (MARL, Self-Play) | 16 |
| Game AI Bots (LLM-Powered) | 9 |
| Game Foundation Models | 7 |
| Procedural Content Generation | 12 |
| Game Benchmarks | 7 |
| Industry Game AI | 6 |
| World Models & Model-Based RL | 10 |
| Curiosity, Exploration, HRL, Imitation, IRL | 14 |
| **Total** | **81** |
