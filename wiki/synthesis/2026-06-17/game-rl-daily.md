---
title: Game RL & Game AI Bot — Daily Survey (2026-06-17)
type: synthesis
created: 2026-06-17
updated: 2026-06-17
sources: [arxiv-search]
tags: [game-rl, game-ai, survey, daily]
---

# Game RL & Game AI Bot — Daily Survey

> Date: 2026-06-17
> Papers surveyed: ~60 across 8 categories
> Sources: arXiv cs.AI, cs.LG, cs.MA, cs.GT, cs.HC, conference proceedings (ICML 2026, Nature, IEEE CoG, NeurIPS 2025, RLC 2025)

---

## Table of Contents

1. [Game RL — Self-Play, MARL, Population-Based Training](#1-game-rl)
2. [Game AI Bot — LLM-Powered Agents, NPC Intelligence](#2-game-ai-bot)
3. [Game Foundation Models](#3-game-foundation-models)
4. [Procedural Content Generation](#4-procedural-content-generation)
5. [Game Benchmarks](#5-game-benchmarks)
6. [Industry Game AI](#6-industry-game-ai)
7. [World Models & Model-Based RL](#7-world-models--model-based-rl)
8. [Related Techniques](#8-related-techniques)

---

## 1. Game RL

### 1.1 MARSHAL: Multi-Agent Reasoning through Self-play with Strategic LLMs
- **Authors:** (MARSHAL team)
- **Affiliation:** —
- **Venue:** arXiv 2510.15414
- **Abstract:** End-to-end RL framework for multi-agent reasoning via self-play in cooperative and competitive games. Features turn-level advantage estimator and agent-specific advantage normalization. Agents trained from Qwen3-4B achieve up to 28.7% performance improvements in held-out games, with zero-shot gains transferring to AIME (+10.0%), GPQA-Diamond (+7.6%), and other reasoning benchmarks.
- **Link:** https://arxiv.org/abs/2510.15414

### 1.2 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors:** (SPIRAL team)
- **Affiliation:** —
- **Venue:** arXiv 2506.24119
- **Abstract:** Applies self-play to two-player zero-sum language games for developing reasoning capabilities. Generates unlimited training data through game dynamics alone. Introduces role-conditioned advantage estimation (RAE) to stabilize multi-agent training. Fully online, multi-turn, multi-agent RL with distributed actor-learner architecture.
- **Link:** https://arxiv.org/abs/2506.24119

### 1.3 PolicyEvolve: Evolving Programmatic Policies by LLMs for Multi-Player Games via Population-Based Training
- **Authors:** (PolicyEvolve team)
- **Affiliation:** —
- **Venue:** arXiv 2509.06053
- **Abstract:** Generates interpretable programmatic policies for multi-player games using LLMs combined with population-based training. Features Global Pool (elite policies), Local Pool (temporary), Policy Planner (LLM-based code generation), and Trajectory Critic (vulnerability analysis). Significantly outperforms prompt-based baselines in policy quality with minimal environment interactions.
- **Link:** https://arxiv.org/abs/2509.06053

### 1.4 PopuLoRA: Co-Evolving LLM Populations for Reasoning Self-Play
- **Authors:** (PopuLoRA team)
- **Affiliation:** —
- **Venue:** arXiv 2605.16727
- **Abstract:** Population-based asymmetric self-play framework for RLVR post-training. Teachers propose problems, matched students solve them under programmatic verifier. LoRA weight-space evolution operators (mutations, crossovers) serve as PBT replacement step. Population outperforms single-agent baseline on HumanEval+, MBPP+, LiveCodeBench, and 7 math benchmarks.
- **Link:** https://arxiv.org/abs/2605.16727

### 1.5 OMAR: One Model, All Roles — Multi-Turn, Multi-Agent Self-Play RL for Conversational Social Intelligence
- **Authors:** (OMAR team)
- **Affiliation:** —
- **Venue:** arXiv 2602.03109
- **Abstract:** Enables a single model to role-play all participants in a conversation simultaneously, learning social intelligence through multi-turn self-play. Hierarchical advantage estimation for turn-level and token-level advantages. Evaluated in SOTOPIA social environment and Werewolf strategy games, demonstrating emergent empathy, persuasion, and compromise-seeking.
- **Link:** https://arxiv.org/abs/2602.03109

### 1.6 Foundation Model Self-Play (FMSP): Open-Ended Strategy Innovation via Foundation Models
- **Authors:** Dharna et al.
- **Affiliation:** —
- **Venue:** arXiv 2507.06466
- **Abstract:** Leverages foundation models' code-generation to overcome self-play limitations (local optima, lack of diversity). Proposes Vanilla FMSP, Novelty-Search Self-Play (NSSP), and Quality-Diversity Self-Play (QDSP). Evaluated in Car Tag (continuous-control pursuer-evader) and Gandalf (LLM jailbreak safety simulation). FMSPs explore diverse RL, tree search, and heuristic methods beyond human-designed strategies.
- **Link:** https://arxiv.org/abs/2507.06466

### 1.7 Seirênes: Adversarial Self-Play with Evolving Distractions for LLM Reasoning
- **Authors:** (Seirênes team)
- **Affiliation:** —
- **Venue:** arXiv 2605.11636
- **Abstract:** Transforms contextual interference into training signal via parameter-shared adversarial self-play. A single model both constructs distracting contexts and solves problems by discerning essential task from perturbations. Achieves average gains of +10.2, +9.1, +7.2 points across 7 math reasoning benchmarks at 4B-30B scales. Distractions from 4B model reduce GPT/Gemini accuracy by 4-5 points.
- **Link:** https://arxiv.org/abs/2605.11636

### 1.8 SAGE: Multi-Agent Self-Evolution for LLM Reasoning
- **Authors:** (SAGE team)
- **Affiliation:** —
- **Venue:** arXiv 2603.15255
- **Abstract:** Closed-loop framework with 4 agents (Challenger, Planner, Solver, Critic) co-evolving from shared LLM backbone using small seed set. Challenger generates increasingly difficult tasks; Planner produces structured multi-step plans; Critic prevents curriculum drift. Improves Qwen-2.5-7B by 8.9% on LiveCodeBench and 10.7% on OlympiadBench.
- **Link:** https://arxiv.org/abs/2603.15255

### 1.9 π-Play: Multi-Agent Self-Play via Privileged Self-Distillation
- **Authors:** (π-Play team)
- **Affiliation:** —
- **Venue:** arXiv 2604.14054
- **Abstract:** Observes that self-play naturally produces question construction paths (QCP) — privileged information for self-distillation. An examiner generates tasks with QCPs, a teacher leverages QCP as privileged context to densely supervise a student. Transforms sparse-reward self-play into dense-feedback self-evolution loop, improving efficiency 2-3x over conventional self-play.
- **Link:** https://arxiv.org/abs/2604.14054

### 1.10 GEMS: Generative Evolutionary Meta-Solver for Scalable MARL
- **Authors:** (GEMS team)
- **Affiliation:** —
- **Venue:** arXiv 2509.23462
- **Abstract:** Replaces explicit policy populations in PSRO with compact latent anchors and amortized generator. Uses unbiased Monte Carlo rollouts, multiplicative-weights meta-dynamics, and model-free UCB oracle. Up to 6x faster, 1.3x less memory than PSRO while achieving higher rewards across Kuhn Poker, Deceptive Messages, and Multi-Particle environments.
- **Link:** https://arxiv.org/abs/2509.23462

### 1.11 Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning
- **Authors:** (Odysseus team)
- **Affiliation:** —
- **Venue:** arXiv 2605.00347
- **Abstract:** Studies RL-based training of VLMs for long-horizon decision-making in Super Mario Land (100+ turns). Proposes adapted PPO with lightweight turn-level critic, substantially improving stability over GRPO/Reinforce++. Pretrained VLMs provide strong action priors, reducing need for action engineering. Achieves at least 3x average game progress over frontier models, with cross-game generalization.
- **Link:** https://arxiv.org/abs/2605.00347

---

## 2. Game AI Bot

### 2.1 PORTAL: Agents Play Thousands of 3D Video Games
- **Authors:** (PORTAL team)
- **Affiliation:** —
- **Venue:** arXiv 2503.13356
- **Abstract:** Novel approach using LLMs to generate specialized behavior trees (BTs) expressed in DSL for thousands of 3D games. Decouples tactical planning from execution, eliminating inference latency during gameplay. Hybrid architecture integrating rule-based nodes with neural network components. First demonstration of agents playing thousands of distinct 3D games through unified approach.
- **Link:** https://arxiv.org/abs/2503.13356

### 2.2 Sensi: Curriculum-Based Test-Time Learning for LLM Game Agents
- **Authors:** (Sensi team)
- **Affiliation:** —
- **Venue:** arXiv 2603.17683
- **Abstract:** LLM agent architecture for ARC-AGI-3 with structured test-time learning: (1) two-player architecture separating perception from action, (2) curriculum-based learning via external state machine, (3) database-as-control-plane for steerable context. Sensi v2 achieves 50-94x greater sample efficiency (32 vs 1600-3000 interactions). Diagnosis: self-consistent hallucination cascade in perception layer.
- **Link:** https://arxiv.org/abs/2603.17683

### 2.3 LLM Reasoner and Automated Planner: A New NPC Approach
- **Authors:** (Reasoner-Planner team)
- **Affiliation:** —
- **Venue:** arXiv 2501.10106
- **Abstract:** Novel NPC architecture integrating LLM for decision-making with classical automated planning (AP) for sound plan generation. LLM selects goals based on world state; AP generates executable plans. Enables adaptation to unforeseen situations while maintaining human-like behavior through three modules: Reasoner (LLM), Planner (AP), Interface.
- **Link:** https://arxiv.org/abs/2501.10106

### 2.4 AdaMARP: Adaptive Multi-Agent Interaction Framework for General Immersive Role-Playing
- **Authors:** (AdaMARP team)
- **Affiliation:** —
- **Venue:** arXiv 2601.11007
- **Abstract:** Adaptive multi-agent role-playing framework with immersive message format interleaving Thought, Action, Environment, Speech. Scene Manager controls narrative via discrete actions (init_scene, pick_speaker, switch_scene, add_role, end). 8B Actor outperforms GPT-4o-mini; 14B Scene Manager surpasses Claude Sonnet 4.5.
- **Link:** https://arxiv.org/abs/2601.11007

### 2.5 Nemobot Games: Crafting Strategic AI Gaming Agents with LLMs
- **Authors:** (Nemobot team)
- **Affiliation:** —
- **Venue:** arXiv 2604.21896
- **Abstract:** Extends Shannon's taxonomy of game-playing machines via LLM-powered agents. Interactive environment for creating/deploying LLM game agents across four game classes: dictionary-based, rigorously solvable, heuristic-based, and learning-based. Integrates RL with human feedback and self-critique for iterative strategy refinement.
- **Link:** https://arxiv.org/abs/2604.21896

### 2.6 Bounded Autonomy for LLM Characters in Live Multiplayer Games
- **Authors:** (Bounded Autonomy team)
- **Affiliation:** —
- **Venue:** arXiv 2604.04703
- **Abstract:** Control architecture for LLM characters in live multiplayer games. Three interfaces: agent-agent interaction (probabilistic reply-chain decay), agent-world action execution (embedding-based grounding with fallback), and player-agent steering (whisper soft-steering technique). Deployed and studied in live multiplayer social game.
- **Link:** https://arxiv.org/abs/2604.04703

### 2.7 OpenGame: Open Agentic Coding for Games
- **Authors:** Jiang et al.
- **Affiliation:** —
- **Venue:** arXiv 2604.18394
- **Abstract:** First open-source agentic framework for end-to-end web game creation. Game Skill (Template + Debug Skills) enables scaffold stable architectures. GameCoder-27B code LLM specialized for game engine via continual pre-training, SFT, and execution-grounded RL. OpenGame-Bench evaluates build health, visual usability, intent alignment. SOTA across 150 diverse game prompts.
- **Link:** https://arxiv.org/abs/2604.18394

### 2.8 Forking Garden: Narrative Arc-Conditioned Gameplay Planning
- **Authors:** (Forking Garden team)
- **Affiliation:** —
- **Venue:** arXiv 2605.01245
- **Abstract:** Generates branching game dungeons conditioned on narrative archetypes (Hero's Journey, Three-act structure). Generates diverse node pool, assembles into DAG via arc-guided constraints, instantiates as playable levels with multimodal alignment. Dynamic RAG for personalized dialogue based on player history.
- **Link:** https://arxiv.org/abs/2605.01245

---

## 3. Game Foundation Models

### 3.1 Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents
- **Authors:** Wang et al.
- **Affiliation:** —
- **Venue:** arXiv 2510.23691
- **Abstract:** Generalist game agent with unified scalable action space anchored to native keyboard-mouse inputs. Pre-trained on 500B+ tokens across OS, web, and simulation games. Key techniques: decaying continual loss to reduce causal confusion, Sparse-Thinking for reasoning depth vs cost balance. 2x SOTA in Minecraft, near-human in unseen web 3D games, outperforms GPT-5/Gemini-2.5-Pro/Claude-4-Sonnet in FPS.
- **Link:** https://arxiv.org/abs/2510.23691

### 3.2 NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors:** Magne et al.
- **Affiliation:** NVIDIA
- **Venue:** CVPR 2026 / arXiv 2601.02427
- **Abstract:** Vision-action foundation model trained on 40,000 hours of gameplay across 1000+ games. Internet-scale video-action dataset from public gameplay. Multi-game benchmark for cross-game generalization. Up to 52% relative improvement in task success on unseen games over scratch-trained models. Open-source dataset, evaluation suite, and model weights.
- **Link:** https://arxiv.org/abs/2601.02427

### 3.3 Pixels2Play-0.1 (P2P0.1): Foundation Model for 3D Gameplay
- **Authors:** Yue et al.
- **Affiliation:** —
- **Venue:** IEEE CoG 2025 / arXiv 2508.14295
- **Abstract:** Foundation model learning to play 3D games from pixels with human-like behavior. Trained with behavior cloning on instrumented human gameplay + unlabeled public videos (action imputation via inverse dynamics). Decoder-only transformer with autoregressive action output. Competent play across Roblox and MS-DOS titles on single consumer GPU.
- **Link:** https://arxiv.org/abs/2508.14295

### 3.4 Scaling Behavior Cloning Improves Causal Reasoning: Open Model for Real-Time Video Game Playing
- **Authors:** (Open P2P team)
- **Affiliation:** Elefant AI
- **Venue:** arXiv 2601.04575
- **Abstract:** Open recipe for real-time game-playing foundation model on consumer GPU. Releases 8300+ hours high-quality human gameplay, training/inference code, and checkpoints. Demonstrates scaling laws of BC: increasing data and depth leads to more causal policy. Models up to 1.2B parameters. Competitive with human players across 3D games.
- **Link:** https://arxiv.org/abs/2601.04575

### 3.5 Towards Generalist Game Players: Foundation Models in the Game Multiverse
- **Authors:** (Survey team)
- **Affiliation:** —
- **Venue:** arXiv 2605.09965
- **Abstract:** First systematic investigation of Large Foundation Models (LFMs) as generalist game players through comprehensive end-to-end lifecycle. Covers Dataset, Model, Harness, Benchmark as coupled closed loop. Traces evolution from RL era → LLM era → Foundation Model era. Comprehensive survey of VLM/VLA/world model approaches to game playing.
- **Link:** https://arxiv.org/abs/2605.09965

---

## 4. Procedural Content Generation

### 4.1 PCGRLLM: LLM-Driven Reward Design for Procedural Content Generation RL
- **Authors:** Baek et al.
- **Affiliation:** —
- **Venue:** arXiv 2502.10906
- **Abstract:** Extended architecture for LLM-driven reward generation in PCGRL. Uses feedback mechanism and reasoning-based prompt engineering. Story-to-reward generation task in 2D environment. Self-alignment and feedback-based reward refinement loop. Achieves performance comparable to humans, reducing human dependency in game AI development.
- **Link:** https://arxiv.org/abs/2502.10906

### 4.2 IPCGRL: Language-Instructed RL for Procedural Level Generation
- **Authors:** Baek et al.
- **Affiliation:** —
- **Venue:** IEEE CoG 2025 / arXiv 2503.12358
- **Abstract:** Instruction-based PCG via RL incorporating sentence embedding model. Fine-tunes task-specific embedding representations for compressing game-level conditions. Up to 21.4% improvement in controllability and 17.2% improvement in generalizability for unseen instructions.
- **Link:** https://arxiv.org/abs/2503.12358

### 4.3 VIPCGRL: Human-Aligned PCG RL via Text-Level-Sketch Shared Representation
- **Authors:** Baek et al.
- **Affiliation:** —
- **Venue:** arXiv 2508.09860
- **Abstract:** Multi-modal PCGRL incorporating grid-based level representations, designer sketches, and textual input. Quadruple contrastive learning for unified multi-modal representation. Auxiliary reward from shared representation aligns policy with human intent. Outperforms baselines in human-likeness and multi-modal conditional generation.
- **Link:** https://arxiv.org/abs/2508.09860

### 4.4 Multiverse: Language-Conditioned Multi-Game Level Generator
- **Authors:** (Multiverse team)
- **Affiliation:** —
- **Venue:** arXiv 2603.26782
- **Abstract:** Language-conditioned multi-game level generator enabling cross-game structural correspondences. Cross-game contrastive learning aligns game domains while preserving fine-grained semantics. Demonstrates ratio-consistent blending behavior and zero-shot cross-game level generation from compositional textual instructions.
- **Link:** https://arxiv.org/abs/2603.26782

### 4.5 Database-Driven Framework for 3D Level Generation with LLMs
- **Authors:** Xu, Verbrugge
- **Affiliation:** —
- **Venue:** arXiv 2508.18533
- **Abstract:** Offline LLM-assisted construction of reusable databases for architectural components and gameplay mechanics. Multi-phase pipeline: room database assembly, facility layout optimization, mechanic integration with topological/spatial rules. Two-phase repair system ensures navigability. Scalable database-centric foundation for automated 3D complex level generation.
- **Link:** https://arxiv.org/abs/2508.18533

### 4.6 AutoUE: Automated Generation of 3D Games in Unreal Engine via Multi-Agent Systems
- **Authors:** (AutoUE team)
- **Affiliation:** —
- **Venue:** arXiv 2603.07106
- **Abstract:** Multi-agent system for end-to-end 3D game generation in Unreal Engine. Agents coordinate for model retrieval (858K 3D model embedding DB), scene generation (UE PCG), gameplay code synthesis (C++), and automated play-testing. RAG mechanism grounds agents with UE tool documentation. Generates correct, robust code with engine constraints.
- **Link:** https://arxiv.org/abs/2603.07106

### 4.7 Learning Local Constraints for RL Content Generators
- **Authors:** (Hybrid PCG team)
- **Affiliation:** —
- **Venue:** arXiv 2605.13570
- **Abstract:** Combines Wave Function Collapse (local constraints) with PCGRL (global properties). Constrains PCGRL action space with WFC-learned constraints. Produces visually satisfying and playable Lode Runner levels with desired global properties. Studies hyperparameter sensitivity: input size, diversity, pattern frequency, starting state.
- **Link:** https://arxiv.org/abs/2605.13570

### 4.8 CreativeGame: Multi-Agent System for Iterative HTML5 Game Generation
- **Authors:** (CreativeGame team)
- **Affiliation:** —
- **Venue:** arXiv 2604.19926
- **Abstract:** Multi-agent system for iterative game generation with 7 agents (10 executable roles). Proxy reward from programmatic signals (not pure LLM judgment). Lineage-scoped memory for cross-version experience accumulation. Mechanic-guided planning loop with explicit mechanic plans before code generation. Supports interpretable version-to-version evolution.
- **Link:** https://arxiv.org/abs/2604.19926

### 4.9 GameGrammar: Generative Ontology for Tabletop Game Design
- **Authors:** (GameGrammar team)
- **Affiliation:** —
- **Venue:** arXiv 2602.05636
- **Abstract:** Generative Ontology encodes domain knowledge as executable Pydantic schemas constraining LLM generation via DSPy signatures. Multi-agent pipeline: Mechanics Architect, Theme Weaver, Component Designer, Balance Critic. Retrieval-augmented generation from BoardGameGeek corpus (100,000+ games). Schema validation reduces consistency errors from 5.03 to 0.10.
- **Link:** https://arxiv.org/abs/2602.05636

### 4.10 High Dimensional Procedural Content Generation (HDPCG)
- **Authors:** (HDPCG team)
- **Affiliation:** —
- **Venue:** arXiv 2602.18943
- **Abstract:** Studies PCG beyond geometry into additional gameplay dimensions (layers, time, locomotion modes). Encodes world state as attribute-labeled cells over expanded state space. Multi-tier planners with bounded-suboptimal search. Combines geometric PCG with structured game rules and temporally evolving elements.
- **Link:** https://arxiv.org/abs/2602.18943

### 4.11 Fly, Fail, Fix: Iterative Game Repair with RL and Large Multimodal Models
- **Authors:** (FlyFailFix team)
- **Affiliation:** —
- **Venue:** arXiv 2507.12666
- **Abstract:** LMM takes designer role, uses gameplay behavior from RL player (pretrained DQN) to guide game design iteration. Tested in Flappy Bird — fixes broken level generators to achieve target player score. Textual summaries and visual gameplay recordings both effective for LMM to tune difficulty. Demonstrates viability of automated design iteration.
- **Link:** https://arxiv.org/abs/2507.12666

---

## 5. Game Benchmarks

### 5.1 Orak: Foundational Benchmark for Training and Evaluating LLM Agents
- **Authors:** Park et al. (KRAFTON)
- **Affiliation:** KRAFTON
- **Venue:** arXiv 2506.03610
- **Abstract:** Benchmark across 12 popular video games spanning all major genres. Plug-and-play MCP interface for reproducible agentic module studies. Releases fine-tuning dataset of expert LLM gameplay trajectories. United evaluation framework with game leaderboards, LLM battle arenas, and ablation studies.
- **Link:** https://arxiv.org/abs/2506.03610

### 5.2 OmniGameArena: Unified UE5 Benchmark for VLM Game Agents
- **Authors:** (OmniGameArena team)
- **Affiliation:** —
- **Venue:** arXiv 2606.09826
- **Abstract:** 12 newly built Unreal Engine 5 games spanning Solo (7), PvP (3), and Coop (2). Unified action interfaces. Improvement Dynamics Curve (IDC): tool-using reflector LLM refines skill prompt across multiple rounds. Evaluates 12 VLM agents on cold-start leaderboard and 4 top agents under IDC.
- **Link:** https://arxiv.org/abs/2606.09826

### 5.3 GameWorld: Standardized and Verifiable Evaluation of Multimodal Game Agents
- **Authors:** (GameWorld team)
- **Affiliation:** NUS, Oxford
- **Venue:** arXiv 2604.07429
- **Abstract:** 34 browser games with 170 tasks across 5 genres. Two interfaces: Computer-Use Agents (keyboard/mouse) and Generalist Multimodal Agents (semantic action parsing). State-verifiable metrics for outcome-based evaluation. 18 model-interface pairs evaluated. Most performant agents still far from human capabilities.
- **Link:** https://arxiv.org/abs/2604.07429

### 5.4 VideoGameBench: Can VLMs Complete Popular Video Games?
- **Authors:** Zhang et al.
- **Affiliation:** Princeton
- **Venue:** arXiv 2505.18134
- **Abstract:** 10 popular 1990s video games for real-time VLM interaction. Raw visual inputs only + high-level objective descriptions. 3 secret games to test generalization. Best model (Gemini 2.5 Pro) completes only 0.48% of games. VideoGameBench Lite (pauses during inference): best model achieves 1.6%.
- **Link:** https://arxiv.org/abs/2505.18134

### 5.5 PokeGym: Visually-Driven Long-Horizon Benchmark for VLMs
- **Authors:** (PokeGym team)
- **Affiliation:** —
- **Venue:** arXiv 2604.08340
- **Abstract:** Visually-driven benchmark in Pokémon Legends: Z-A (3D open-world RPG). 30 tasks (30-220 steps) across navigation, interaction, mixed scenarios. Three instruction granularities. Code-level isolation forcing pure vision-based decisions. Key finding: physical deadlock recovery (not high-level planning) is primary bottleneck. Stronger models show "aware deadlocks" vs weaker models' "unaware deadlocks."
- **Link:** https://arxiv.org/abs/2604.08340

### 5.6 lmgame-Bench: How Good are LLMs at Playing Games?
- **Authors:** Hu et al.
- **Affiliation:** —
- **Venue:** arXiv 2505.15146
- **Abstract:** Suite of platformer, puzzle, and narrative games via unified Gym-style API. Lightweight perception and memory scaffolds to address brittle vision, prompt sensitivity, contamination. 13 leading models evaluated. RL on single game transfers to unseen games and external planning tasks. o3 and o1 top the leaderboard.
- **Link:** https://arxiv.org/abs/2505.15146

### 5.7 GameVerse: Can VLMs Learn from Video-based Reflection?
- **Authors:** (GameVerse team)
- **Affiliation:** —
- **Venue:** arXiv 2603.06656
- **Abstract:** 15 globally popular games with reflect-and-retry paradigm. Cognitive hierarchical taxonomy. Dual action space (semantic + GUI). Milestone scoring via advanced VLMs. Key finding: combining failure trajectories (analogous to RL) and expert tutorials (analogous to SFT) yields best improvements — training-free proxy for SFT+RL post-training.
- **Link:** https://arxiv.org/abs/2603.06656

### 5.8 PokeAgent Challenge: Competitive and Long-Context Learning at Scale
- **Authors:** (PokeAgent team)
- **Affiliation:** NeurIPS 2025 Competition
- **Venue:** arXiv 2603.15563
- **Abstract:** Large-scale benchmark on Pokémon's multi-agent battle system and RPG environment. Battling Track (20M+ trajectories, strategic reasoning under partial observability) and Speedrunning Track (long-horizon planning). 100+ teams competed at NeurIPS 2025. Pokémon battling nearly orthogonal to standard LLM benchmarks.
- **Link:** https://arxiv.org/abs/2603.15563

### 5.9 GameDevBench: Evaluating Agentic Capabilities Through Game Development
- **Authors:** (GameDevBench team)
- **Affiliation:** —
- **Venue:** arXiv 2602.11103
- **Abstract:** 132 game development tasks from web and video tutorials. Requires multimodal understanding (shaders, sprites, animations). Best agent solves only 54.5% of tasks. Success drops from 46.9% (gameplay) to 31.6% (2D graphics). Image/video feedback mechanisms improve performance (Claude Sonnet 4.5: 33.3% → 47.7%).
- **Link:** https://arxiv.org/abs/2602.11103

---

## 6. Industry Game AI

### 6.1 Real-Time Diffusion Policies for Games: CPQE (Consistency Policy with Q-Ensembles)
- **Authors:** Zhang, Luo, Sjölund, Mattsson, Gisslén, Sestini
- **Affiliation:** Uppsala University, EA SEED
- **Venue:** RLC 2025 / IEEE CoG 2025
- **Abstract:** Combines consistency models with Q-ensembles for fast inference in game environments. CPQE achieves 60 Hz inference (vs 20 Hz for SOTA diffusion policies) while maintaining comparable performance. Stable training with Q-ensembles providing reliable value function estimates. Practical solution for real-time deployment of diffusion-based game policies.
- **Link:** https://openreview.net/pdf?id=76f59dfea1c9a852ae4b5961901388f5031b37cb

### 6.2 SPEQ: Offline Stabilization Phases for Efficient Q-Learning in High Update-To-Data Ratio RL
- **Authors:** Romeo, Macaluso, Sestini, Bagdanov, Gisslén
- **Affiliation:** University of Florence, EA SEED
- **Venue:** RLC 2025
- **Abstract:** Addresses instability in high update-to-data ratio offline RL. Introduces stabilization phases for efficient Q-learning. Relevant to game AI training pipelines where sample efficiency is critical.
- **Link:** https://www.ea.com/seed/publications

### 6.3 TROFI: Trajectory-Ranked Offline Inverse Reinforcement Learning
- **Authors:** Sestini, Bergdahl, Tollmar, Bagdanov, Gisslén
- **Affiliation:** EA SEED, KTH
- **Venue:** RLC 2025
- **Abstract:** Trajectory-ranked offline IRL for learning reward functions from ranked demonstrations. Applicable to learning human-preferred behaviors in games without hand-crafted rewards.
- **Link:** https://www.ea.com/seed/publications

### 6.4 NVIDIA ACE Game Agent SDK & Unreal Engine 5 Plugins
- **Authors:** NVIDIA
- **Affiliation:** NVIDIA
- **Venue:** Unreal Fest 2026 (Technical Blog)
- **Abstract:** Lightweight C/C++ agentic framework for in-game AI NPCs. Agent, Chat, RAG APIs. On-device, low-latency AI companions. New UE5 plugins: automatic speech recognition, SLM, text-to-speech. Battle-tested in Total War: PHARAOH (RAG over 1200+ game data tables). Open source, optimized for NVIDIA RTX.
- **Link:** https://developer.nvidia.com/blog/build-on-device-ai-companions-with-the-nvidia-ace-game-agent-sdk-and-unreal-engine-5-plugins/

### 6.5 Minimizing Game Runtime Inference Costs with Coding Agents (NVIDIA NVIGI)
- **Authors:** NVIDIA
- **Affiliation:** NVIDIA
- **Venue:** NVIDIA Technical Blog (March 2026)
- **Abstract:** Code agents with SLMs generate and execute complex logic in single inference call, reducing GPU contention. Lua-based execution (200KB runtime, sub-ms startup). Hardened Lua for safe embedding. Demonstrated in 2D dungeon AI companion sample. Enables dynamic, flexible in-game actions with minimal inference overhead.
- **Link:** https://developer.nvidia.com/blog/how-to-minimize-game-runtime-inference-costs-with-coding-agents/

### 6.6 Sony Research Tokyo Multimodal AI Framework
- **Authors:** Sony Research
- **Affiliation:** Sony
- **Venue:** 2026
- **Abstract:** Multimodal AI framework targeting both robotics and PlayStation gaming. 3 configurations (1.2B, 7B, 22B). Sub-50ms inference on edge hardware. Inputs: RGB video, depth, LiDAR, audio, text. Powers NPCs that respond dynamically to player actions, voice commands, and environmental context. Plans integration into first-party PlayStation Studios titles by late 2026.
- **Link:** (News coverage)

---

## 7. World Models & Model-Based RL

### 7.1 DreamerV3: Mastering Diverse Control Tasks Through World Models
- **Authors:** Hafner, Pasukonis, Ba, Lillicrap
- **Affiliation:** Google DeepMind
- **Venue:** Nature 640, 647-653 (2025)
- **Abstract:** Third-generation Dreamer algorithm using fixed hyperparameters across 150+ diverse tasks. Robustness via normalization, balancing, transformations. First algorithm to collect diamonds in Minecraft from scratch without human data or curricula. Larger models achieve higher scores with less interaction.
- **Link:** https://www.nature.com/articles/s41586-025-08744-2

### 7.2 TransDreamerV3: Implanting Transformer in DreamerV3
- **Authors:** (TransDreamerV3 team)
- **Affiliation:** —
- **Venue:** arXiv 2506.17103
- **Abstract:** Enhances DreamerV3 by replacing GRU in RSSM with transformer encoder. Integrates TSSM (Transformer State-Space Model) for long-range memory. Outperforms DreamerV3 on Atari-Freeway and Crafter tasks. Shows promise for complex environments requiring sophisticated temporal understanding.
- **Link:** https://arxiv.org/abs/2506.17103

### 7.3 Matrix-Game: Interactive World Foundation Model
- **Authors:** (Matrix-Game team)
- **Affiliation:** SkyworkAI
- **Venue:** arXiv 2506.18701
- **Abstract:** 17B parameter interactive world model for controllable game world generation. Two-stage pipeline: unlabeled pretraining + action-labeled training. Matrix-Game-MC dataset: 2700h unlabeled + 1000h labeled Minecraft clips. Controllable image-to-world generation paradigm. GameWorld Score benchmark. Outperforms Oasis and MineWorld across all metrics.
- **Link:** https://arxiv.org/abs/2506.18701

### 7.4 Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory
- **Authors:** (Matrix-Game 3.0 team)
- **Affiliation:** SkyworkAI
- **Venue:** arXiv 2604.08995
- **Abstract:** Memory-augmented interactive world model for 720p real-time long-form video generation. 40 FPS at 720p with 5B model. Industrial-scale infinite data engine (Unreal Engine synthetic + AAA game collection + real-world video). Camera-aware memory retrieval for long-horizon spatiotemporal consistency. Multi-segment DMD distillation for efficient real-time inference.
- **Link:** https://arxiv.org/abs/2604.08995

### 7.5 WorldCam: Interactive Autoregressive 3D Gaming Worlds with Camera Pose as Unifying Geometric Representation
- **Authors:** (WorldCam team)
- **Affiliation:** —
- **Venue:** arXiv 2603.16871
- **Abstract:** Establishes camera pose as unifying geometric representation for action control and 3D consistency. Physics-based continuous action space using Lie algebra for 6-DoF camera poses. Global camera poses as spatial indices for geometrically consistent revisiting. 3000-minute human gameplay dataset with camera trajectories and text descriptions.
- **Link:** https://arxiv.org/abs/2603.16871

### 7.6 DreamX-World 1.0: General-Purpose Interactive World Model
- **Authors:** (DreamX-World team)
- **Affiliation:** —
- **Venue:** arXiv 2606.16993
- **Abstract:** General-purpose interactive world model from Wan2.2. Camera conditioning, non-local scene memory, event interaction, autoregressive long-video generation. Data engine combining Unreal Engine trajectories, gameplay recordings, real-world videos. Up to 16 FPS on 8x RTX 5090. Camera-control score 73.75, overall 84.76.
- **Link:** https://arxiv.org/abs/2606.16993

### 7.7 ARROW: Augmented Replay for Robust World Models
- **Authors:** (ARROW team)
- **Affiliation:** —
- **Venue:** arXiv 2603.11395
- **Abstract:** Extends DreamerV3 with memory-efficient, distribution-matching replay buffer for continual RL. Short-term FIFO + strategic long-term replay balancing. Substantial improvements in tasks without shared structure. Supports model-based continual RL without explicit task identifiers.
- **Link:** https://arxiv.org/abs/2603.11395

### 7.8 Code World Models for General Game Playing
- **Authors:** (Code World Models team)
- **Affiliation:** —
- **Venue:** arXiv 2510.04542
- **Abstract:** Uses LLMs to translate natural language game rules and trajectories into executable Python world models. Code World Model (CWM) with state definition, legal moves, transitions, observations, rewards, termination. Generates heuristic value functions for MCTS/IS-MCTS. Outperforms frontier "thinking" LLMs across various two-player games including OOD ones.
- **Link:** https://arxiv.org/abs/2510.04542

### 7.9 Distilling Game Code World Model Generation into Lightweight LLMs
- **Authors:** (GameCWM Distillation team)
- **Affiliation:** —
- **Venue:** arXiv 2605.24375
- **Abstract:** Distills GameCWM generation into small models via SFT+RLVR post-training. Curated dataset of 30 games (perfect + imperfect info). Verification framework for structural and semantic game properties. Makes Qwen2.5-3B-Instruct capable of generating valid GameCWMs without frontier model refinement loops.
- **Link:** https://arxiv.org/abs/2605.24375

### 7.10 Mind Dreamer: Active Latent Intervention on Latent Manifolds
- **Authors:** (Mind Dreamer team)
- **Affiliation:** —
- **Venue:** arXiv 2605.16030
- **Abstract:** Operationalizes Active Latent Intervention (ALI) to transcend Markovian continuity in MBRL. Adversarial state generator synthesizes counterfactual latent jumps to epistemic blind spots. Relay Value Function (RVF) and Relay Uncertainty Function (RUF) with quadratic discount for stable uncertainty propagation. 1.67x average improvement over DreamerV3 on DeepMind Control Suite.
- **Link:** https://arxiv.org/abs/2605.16030

---

## 8. Related Techniques

### 8.1 Generative Evolutionary Meta-Solver (GEMS) — see §1.10

### 8.2 Foundation Model Self-Play (FMSP) — see §1.6

### 8.3 Cross-Entropy Games for General Capabilities
- **Authors:** (Cross-Entropy Games team)
- **Affiliation:** —
- **Venue:** arXiv 2603.22479
- **Abstract:** Uses cross-entropy as game score for training general-purpose agents. Covering strategic reasoning, language understanding, and planning.
- **Link:** https://arxiv.org/abs/2603.22479

### 8.4 GenStrat: Strategic Reasoning in LLMs
- **Authors:** (GenStrat team)
- **Affiliation:** —
- **Venue:** arXiv 2605.23238
- **Abstract:** Framework for evaluating and improving strategic reasoning in LLMs through game-theoretic scenarios.
- **Link:** https://arxiv.org/abs/2605.23238

### 8.5 PCSP: One Policy, Infinite NPCs — Persona-Conditioned Shared Policy RL
- **Authors:** (PCSP team)
- **Affiliation:** —
- **Venue:** arXiv 2605.23652
- **Abstract:** Single shared RL policy conditioned on persona embeddings for diverse NPC behaviors. Enables infinite character variations from one policy.
- **Link:** https://arxiv.org/abs/2605.23652

### 8.6 HGPO: Hierarchy-of-Groups Policy Optimization
- **Authors:** (HGPO team)
- **Affiliation:** —
- **Venue:** arXiv 2602.22817
- **Abstract:** Multi-agent RL optimization method organizing agents into hierarchical groups for more stable and efficient policy learning.
- **Link:** https://arxiv.org/abs/2602.22817

### 8.7 ALIVE: Interactive Frontend Games via RL
- **Authors:** Alibaba
- **Affiliation:** Alibaba
- **Venue:** ICML 2026
- **Abstract:** RL-based approach for generating interactive frontend game experiences. Demonstrates practical game AI deployment in production web environments.

### 8.8 Dark Souls III: Lifelong Learning in Games
- **Authors:** (Dark Souls III team)
- **Affiliation:** —
- **Venue:** ICLR 2026 Workshop / arXiv 2601.17923
- **Abstract:** Studies lifelong/continual RL in the challenging Dark Souls III environment. Addresses catastrophic forgetting and policy adaptation in long-running game agents.
- **Link:** https://arxiv.org/abs/2601.17923

---

## Key Trends & Summary

| Theme | Key Papers | Observation |
|-------|-----------|-------------|
| **Self-play → Reasoning** | SPIRAL, MARSHAL, Seirênes, PopuLoRA, OMAR | Self-play in games is a scalable pathway to general LLM reasoning, transferring to math/code benchmarks |
| **Generalist Game Agents** | Game-TARS, NitroGen, P2P, Open P2P | Foundation models trained on 1000s of games approach human-level generalization; open-source models maturing |
| **World Models at Scale** | Matrix-Game 3.0, WorldCam, DreamX-World, DreamerV3 (Nature) | Interactive world models reaching 40 FPS real-time 720p with minute-long consistency; camera pose as unifying representation |
| **PCG Goes Multimodal** | PCGRLLM, IPCGRL, VIPCGRL, Multiverse, AutoUE | Language, sketches, and vision modalities integrated into PCG pipelines; End-to-end game generation in commercial engines |
| **Benchmark Standardization** | Orak, GameWorld, OmniGameArena, VideoGameBench | Move toward standardized, verifiable, multi-genre game agent evaluation; state-verifiable metrics replacing heuristic judgment |
| **Industry Deployment** | NVIDIA ACE/IGI, EA SEED (CPQE, SPEQ, TROFI), Sony PlayStation AI | On-device inference (60Hz diffusion policies), SLM code agents, LLM NPCs in live multiplayer games reaching production |
| **Open-Ended Learning** | FMSP, PolicyEvolve, SAGE, GEMS | Foundation models enabling co-evolution, population-based training, and quality-diversity search for strategy discovery |
| **Code-Generated Game Worlds** | Code World Models, GameCWM Distillation, OpenGame | LLMs generating executable game environments from natural language; distilling into lightweight models for accessibility |

---

## Statistics

- **Total papers surveyed:** ~60
- **Categories:** 8 (Game RL, Game AI Bot, Game Foundation Models, PCG, Game Benchmarks, Industry Game AI, World Models, Related Techniques)
- **New this session vs 2026-06-16:** Matrix-Game 3.0, DreamX-World 1.0, GameDevBench, OmniGameArena, CPQE (EA), Sony AI Framework, Forking Garden, GameGrammar, HDPCG, FlyFailFix, PopuLoRA, Seirênes, SAGE, CreativeGame, Mind Dreamer, Distilling GameCWMs, ARROW, PokeGym, Code World Models, PokeAgent Challenge, Multiverse, VIPCGRL, AutoUE, Bounded Autonomy
