---
title: Game RL & Game AI Bot — Daily Survey (2026-06-25)
type: synthesis
created: 2026-06-25
updated: 2026-06-25
sources: []
tags: [game-rl, game-ai, game-foundation-models, pcg, game-benchmarks, self-play, world-models, curiosity, marl, llm-agents]
---

# Game RL & Game AI Bot — Daily Survey (2026-06-25)

> Curated from arXiv and recent proceedings. Covers Game RL, LLM-powered game agents, game foundation models, PCG, game benchmarks, industry game AI, and related techniques (self-play, world models, curiosity, hierarchical RL, MARL).

---

## 1. Game Reinforcement Learning

### 1.1 QZero: Mastering the Game of Go with Self-play Experience Replay

| Field | Value |
|-------|-------|
| **Authors** | N/A (anonymous preprint) |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Jan 2026 |
| **Links** | [arXiv:2601.03306](https://arxiv.org/abs/2601.03306) |

**Abstract:** Presents QZero, a model-free RL algorithm that forgoes search during training and learns a Nash equilibrium policy through self-play and off-policy experience replay. Built upon entropy-regularized Q-learning, QZero uses a single Q-value network to unify policy evaluation and improvement. Trained tabula rasa with only 7 GPUs for 5 months, it achieves performance comparable to AlphaGo — demonstrating the efficiency of model-free RL for Go.

**Key innovations:**
- Model-free alternative to AlphaZero's MCTS-based approach
- Entropy-regularized Q-learning with self-play off-policy replay
- Single Q-network architecture for both evaluation and improvement
- Dramatically reduced compute (7 GPUs vs. AlphaGo's TPU cluster)

---

### 1.2 Regret-Guided Search Control (RGSC) for AlphaZero

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | ICLR 2026 |
| **Links** | [arXiv:2602.20809](https://arxiv.org/abs/2602.20809) |

**Abstract:** Proposes Regret-Guided Search Control (RGSC), a framework extending AlphaZero by identifying and prioritizing high-regret states as search control openings for self-play. Integrates a regret network and a prioritized regret buffer. Across 9x9 Go, 10x10 Othello, and 11x11 Hex, RGSC outperforms AlphaZero and Go-Exploit by an average of 77 and 89 Elo respectively. On a well-trained 9x9 Go model, it improves win rate against KataGo from 69.3% to 78.2%.

**Key innovations:**
- Regret-guided state selection for self-play openings
- Prioritized regret buffer for efficient learning
- Generalizes beyond board games to Atari (Pac-Man with MuZero)

---

### 1.3 K-Level Policy Gradients for Multi-Agent RL

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Sep 2025 |
| **Links** | [arXiv:2509.12117](https://arxiv.org/abs/2509.12117) |

**Abstract:** Introduces K-Level Policy Gradient (KPG), a method that recursively updates each agent against the updated policies of other agents, speeding up discovery of effective coordinated policies. Theoretically proves monotonic convergence to a local Nash equilibrium. Applied to MAPPO, MADDPG, and FACMAC, KPG shows superior performance in StarCraft II and multi-agent MuJoCo.

**Key innovations:**
- Recursive k-level thinking for MARL policy updates
- Theoretical convergence guarantees to local Nash equilibrium
- Principled integration with existing deep MARL algorithms

---

### 1.4 Optimistic Policy Regularization (OPR)

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Mar 2026 |
| **Links** | [arXiv:2603.06793](https://arxiv.org/abs/2603.06793) |

**Abstract:** Introduces Optimistic Policy Regularization (OPR) applied to PPO, which substantially improves sample efficiency on the Arcade Learning Environment. Across 49 Atari games at the 10M interaction budget, OPR achieves the highest score in 22 environments. Also generalizes to the CAGE Challenge 2 cyber-defense environment, surpassing the competition-winning agent.

**Key innovations:**
- Optimistic trajectory weighting for actor-critic updates
- State-specific exploration bonuses via trajectory history
- Strong performance on both dense and sparse reward Atari games
- Cross-domain transfer to cyber-defense tasks

---

### 1.5 Dreamer: Mastering Diverse Control Tasks through World Models

| Field | Value |
|-------|-------|
| **Authors** | Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, Timothy Lillicrap |
| **Affiliation** | Google DeepMind |
| **Venue** | Nature 640, 647–653 (2025) |
| **Links** | [Nature](https://www.nature.com/articles/s41586-025-08744-2) |

**Abstract:** Presents Dreamer, a general algorithm that outperforms specialized expert algorithms across 150+ tasks using fixed hyperparameters. Learns a world model that predicts outcomes of potential actions, with a critic network judging values and an actor network choosing actions. Outperforms MuZero on 57 Atari games while using fewer computational resources. Published in Nature.

**Key innovations:**
- Fixed hyperparameters across 150+ diverse control tasks
- Outperforms MuZero, Rainbow, and IQN on Atari
- World model for imagination-based planning
- Predictable scaling: larger models achieve higher scores with less interaction

---

### 1.6 Mastering the Game of No-Press Diplomacy via Deterministic Equilibrium Search

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | ICLR 2026 (noted in search results) |
| **Links** | Referenced in ICLR 2026 proceedings |

**Abstract:** Related to multi-agent equilibrium search in large-scale imperfect-information games (No-Press Diplomacy — 7-player).

---

## 2. LLM-Powered Game AI Bots

### 2.1 Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with LLMs

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Apr 2026 |
| **Links** | [arXiv:2604.21896](https://arxiv.org/abs/2604.21896) |

**Abstract:** Introduces Nemobot, an interactive agentic engineering environment enabling users to create, customize, and deploy LLM-powered game agents. Covers four game classes: dictionary-based (state-action compression), rigorously solvable (mathematical reasoning), heuristic-based (minimax + crowdsourcing), and learning-based (RLHF + self-critique).

**Key innovations:**
- Operates on Shannon's taxonomy of game-playing machines
- LLM-based chatbot with tool-augmented generation
- Programmable environment for self-programming AI agents

---

### 2.2 Sensi: Curriculum-Based Test-Time Learning for LLM Game Agents

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Mar 2026 |
| **Links** | [arXiv:2603.17683](https://arxiv.org/abs/2603.17683) |

**Abstract:** Presents Sensi, an LLM agent architecture for ARC-AGI-3 game challenge introducing (1) two-player architecture separating perception from action, (2) curriculum-based learning with external state machine, (3) database-as-control-plane. Sensi v2 completes its learning curriculum in ~32 action attempts, achieving 50–94× greater sample efficiency than comparable systems (1,600–3,000 attempts).

**Key innovations:**
- Separation of perception and action into two specialized agents
- Database-as-control-plane for programmatic context steering
- LLM-as-judge with dynamically generated evaluation rubrics
- Radical sample efficiency improvement

---

### 2.3 ChatNPC: Towards Immersive Video Game Experience through Naturalistic and Emotive Dialogue

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | ACL ARR 2026 |
| **Links** | [OpenReview](https://openreview.net/forum?id=y08EEyE0q7) |

**Abstract:** Presents ChatNPC, a game companion that dynamically personalizes responses in real time based on players' emotional shifts. Integrates a game sentinel-guided agent (SeGent), memory capability, and chat planning tool for reasoning instantiation. Uses lightweight game-template as information framework.

**Key innovations:**
- Real-time emotional shift tracking for NPC responses
- Sentinel-guided agent architecture
- Lightweight game-template for contextual NPC dialogue
- Naturalistic pauses, sighs, and conversational cues

---

### 2.4 Deflanderization for Game Dialogue: Balancing Character Authenticity with Task Execution

| Field | Value |
|-------|-------|
| **Authors** | Pasin Buakhaw, Kun Kerdthaisong, Phuree Phenhiran, Pitikorn Khlaisamniang, Supasate Vorathammathorn, Piyalitt Ittichaiwong, Nutchanon Yongsatianchot |
| **Affiliation** | TU_Character_lab |
| **Venue** | CPDC 2025 / arXiv |
| **Links** | [arXiv:2510.13586](https://arxiv.org/abs/2510.13586) |

**Abstract:** Reports participation in Commonsense Persona-Grounded Dialogue Challenge (CPDC) 2025. Combines Deflanderization prompting (suppressing excessive role-play) with fine-tuned Qwen3-14B via SFT and LoRA. Ranked 2nd on Task 1, 2nd on Task 3 (API track), and 4th on Task 3 (GPU track).

**Key innovations:**
- Deflanderization prompting method to balance persona vs. task fidelity
- Dual-control approach: lightweight prompting + fine-tuned models
- RAG+Refine and RAG+Memory approaches for stability

---

### 2.5 LLM-Based Behavior Agent with Natural Language Personality Control

| Field | Value |
|-------|-------|
| **Authors** | Tarigan et al. |
| **Affiliation** | N/A |
| **Venue** | Engineering, Technology & Applied Science Research, Oct 2025 |
| **Links** | [ETASR](https://etasr.com/index.php/ETASR/article/view/12631) |

**Abstract:** Explores LLMs for personality-driven NPC behavior using OCEAN personality model. A stateless LLM with automated prompt generator dynamically constructs context-aware prompts based on NPC traits, game states, and environmental factors, implemented in the roguelike Rudantara RPG.

**Key innovations:**
- OCEAN personality model for NPC decision-making
- Automated prompt generation from game state + personality
- Eliminates traditional behavior trees and scripting

---

### 2.6 LLM-Driven NPCs: Cross-Platform Dialogue System for Games and Social Platforms

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Apr 2025 |
| **Links** | [arXiv:2504.13928](https://arxiv.org/abs/2504.13928) |

**Abstract:** Presents a prototype enabling LLM-powered NPCs to communicate across Unity (in-game) and Discord (social platform) using DeepSeek-R1. Dialogue logs stored in cloud database (LeanCloud) for cross-platform memory synchronization.

**Key innovations:**
- Cross-platform NPC dialogue (game + social media)
- Cloud-synchronized memory for persistent conversations
- Location-aware contextual responses

---

### 2.7 LLM NPC Action Planning in VR Games

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | AIMEDIA 2025 |
| **Links** | [Presentation slides](https://www.iaria.org/conferences2025/filesAIMEDIA25/40024_aimedia.pdf) |

**Abstract:** Addresses NPC action planning in VR games using LLMs with few-shot learning. NPCs perceive the 3D world, understand player intentions, and plan/execute physical actions. Uses Llama-3 models with structured JSON output, achieving 86.4% accuracy.

**Key innovations:**
- Few-shot action planning for VR NPCs
- Dynamic world perception + game knowledge injection
- Function chaining for complex action sequences

---

### 2.8 A Survey on Large Language Model-Based Game Agents

| Field | Value |
|-------|-------|
| **Authors** | Hu et al. |
| **Affiliation** | N/A |
| **Venue** | arXiv (continuously updated) |
| **Links** | [arXiv:2404.02039](https://arxiv.org/abs/2404.02039) |

**Abstract:** Comprehensive survey of LLM-based game agents (LLMGAs) through a unified reference architecture. Covers single-agent (memory, reasoning, perception-action) and multi-agent (communication, coordination, social behavior) dimensions. Introduces challenge-centered taxonomy linking six game genres to agent requirements.

**Key innovations:**
- Unified reference architecture for LLM game agents
- Challenge-centered taxonomy across game genres
- Continuously updated paper list at github.com/git-disl/awesome-LLM-game-agent-papers

---

## 3. Game Foundation Models

### 3.1 NitroGen: An Open Foundation Model for Generalist Gaming Agents

| Field | Value |
|-------|-------|
| **Authors** | Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi "Jim" Fan |
| **Affiliation** | NVIDIA, MineDojo |
| **Venue** | CVPR 2026 |
| **Links** | [arXiv:2601.02427](https://arxiv.org/abs/2601.02427) |

**Abstract:** Vision-action foundation model for generalist gaming agents trained on 40,000 hours of gameplay videos across 1,000+ games. Uses (1) internet-scale video-action dataset, (2) multi-game benchmark, (3) unified vision-action model with behavior cloning. Fine-tuned models show up to 52% relative improvement on unseen games over training from scratch. Open-source: dataset, eval suite, model weights.

**Key innovations:**
- Largest open-source gaming dataset (40K hrs, 1,000+ games)
- Automated action extraction from public gameplay videos
- Cross-game zero-shot and fine-tuning generalization
- 500M parameter DiT architecture (System-1 sensory model)

---

### 3.2 Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents

| Field | Value |
|-------|-------|
| **Authors** | Wang et al. |
| **Affiliation** | ByteDance (Seed-TARS) |
| **Venue** | arXiv preprint, Oct 2025 |
| **Links** | [arXiv:2510.23691](https://arxiv.org/abs/2510.23691) |

**Abstract:** Generalist game agent with unified scalable action space anchored to human-aligned keyboard-mouse inputs. Pre-trained on 500B+ tokens with diverse trajectories. Key techniques: decaying continual loss for causal confusion mitigation, efficient Sparse-Thinking strategy. Achieves ~2× success rate vs. prior SOTA on Minecraft, near-human generalization on unseen web 3D games, and outperforms GPT-5, Gemini-2.5-Pro, Claude-4-Sonnet on FPS benchmarks.

**Key innovations:**
- Native keyboard-mouse action space (no API/GUI abstraction)
- Decaying continual loss for causal confusion
- Sparse-Thinking for reasoning depth vs. cost tradeoff
- Massive pre-training (500B+ tokens) across OS, web, and game domains
- Cross-domain transfer: games → general computer use

---

### 3.3 Pixels2Play (P2P 0.1): A Foundation Model for 3D Gameplay

| Field | Value |
|-------|-------|
| **Authors** | Yue, Green, Hunt, et al. |
| **Affiliation** | N/A |
| **Venue** | IEEE CoG 2025 |
| **Links** | [arXiv:2508.14295](https://arxiv.org/abs/2508.14295) |

**Abstract:** Foundation model that learns to play 3D video games from raw pixels. Trained via behavior cloning on instrumented human demonstrations + unlabeled public videos with imputed actions via inverse-dynamics model. Decoder-only transformer with auto-regressive action output. Text-conditioned control planned for future.

**Key innovations:**
- End-to-end from pixels to actions for 3D games
- Inverse-dynamics model for leveraging unlabeled video data
- Consumer GPU latency-friendly architecture
- Early prototypes for AI teammates, controllable NPCs, assistive testers

---

### 3.4 Scaling Behavior Cloning Improves Causal Reasoning: An Open Model for Real-Time Video Game Playing

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Jan 2026 |
| **Links** | [arXiv:2601.04575](https://arxiv.org/abs/2601.04575) |

**Abstract:** Introduces P2Play, an open recipe for training video game playing foundation models for real-time inference on consumer GPUs. Releases all data (8,300+ hrs), code, and checkpoints. Shows that scaling behavior cloning improves causal reasoning — validated across models up to 1.2B parameters.

**Key innovations:**
- Fully open-source: 8,300+ hrs gameplay data, code, weights
- Text-conditioned policy from pixels to keyboard/mouse actions
- Causal reasoning improvements with scale (model size + data)
- Real-time (20 Hz) inference on consumer GPU (RTX 5090)

---

### 3.5 OpenGame: Open Agentic Coding for Games

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Apr 2026 |
| **Links** | [arXiv:2604.18394](https://arxiv.org/abs/2604.18394) |

**Abstract:** Open-source agentic framework for end-to-end web game creation from natural-language specifications. Features multi-phase workflow with Game Skill (Template Skill + Debug Skill) and GameCoder-27B foundation model (trained via continual pre-training + SFT + execution-grounded RL). Introduces OpenGame-Bench for dynamic evaluation.

**Key innovations:**
- End-to-end game generation from natural language
- GameCoder-27B: domain-specialized code model
- Three-stage training: continual pre-training → SFT → execution-grounded RL
- Dynamic evaluation beyond static code correctness

---

### 3.6 Towards Generalist Game Players: Foundation Models in the Game Multiverse

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, May 2026 |
| **Links** | [arXiv:2605.09965](https://arxiv.org/abs/2605.09965) |

**Abstract:** First systematic investigation of Large Foundation Models as generalist game players. Traces four eras: environment-specific agents → current foundation models → future creator stage. Analyzes four pillars (Dataset, Model, Harness, Benchmark) and five fundamental trade-offs. Proposes a five-level roadmap from single-game mastery to creator-stage.

**Key innovations:**
- End-to-end lifecycle perspective on generalist game agents
- Five fundamental trade-offs bounding the system
- Five-level roadmap: mastery → generalization → adaptation → creation → omnipotence
- Unified lens across RL, LLM, VLM, VLA, and world model approaches

---

## 4. Procedural Content Generation

### 4.1 IPCGRL: Language-Instructed RL for Procedural Level Generation

| Field | Value |
|-------|-------|
| **Authors** | Baek, Kim, et al. |
| **Affiliation** | N/A |
| **Venue** | IEEE CoG 2025 |
| **Links** | [arXiv:2503.12358](https://arxiv.org/abs/2503.12358) |

**Abstract:** Instruction-based PCG via RL incorporating sentence embedding model. Fine-tunes task-specific embeddings to compress game-level conditions. Achieves 21.4% improvement in controllability and 17.2% improvement in generalizability for unseen instructions.

**Key innovations:**
- Natural language instruction control for PCGRL
- Sentence embedding fine-tuning for task-specific compression
- Flexible multi-modal conditional input

---

### 4.2 PCGRLLM: LLM-Driven Reward Design for PCGRL

| Field | Value |
|-------|-------|
| **Authors** | Baek, Kim, Earle, Jiang, Jin-Ha, Togelius, Kim |
| **Affiliation** | NYU, et al. |
| **Venue** | arXiv preprint, Feb 2025 |
| **Links** | [arXiv:2502.10906](https://arxiv.org/abs/2502.10906) |

**Abstract:** Feedback-based reward generation framework for PCG. LLM generates reward function from story instruction, PCGRL model trains with it, then LLM provides feedback to update rewards in next iteration. Self-alignment + feedback refinement.

**Key innovations:**
- LLM-in-the-loop reward design for PCG
- Iterative self-alignment and feedback cycle
- Eliminates hand-crafted reward engineering for content generation

---

### 4.3 Multiverse: Language-Conditioned Multi-Game Level Generator

| Field | Value |
|-------|-------|
| **Authors** | Kim, Baek, Lee |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Mar 2026 |
| **Links** | [arXiv:2603.26782](https://arxiv.org/abs/2603.26782) |

**Abstract:** Language-conditioned multi-game level generator enabling cross-game generation and level blending within a shared latent space. Uses cross-game contrastive learning to align game domains. Enables zero-shot cross-game generation from compositional textual instructions.

**Key innovations:**
- Shared latent space across multiple game domains
- Cross-game contrastive learning for domain alignment
- Zero-shot level blending from compositional instructions

---

### 4.4 VIPCGRL: Vision-Instruction PCGRL

| Field | Value |
|-------|-------|
| **Authors** | Baek et al. |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Aug 2025 |
| **Links** | [arXiv:2508.09860](https://arxiv.org/abs/2508.09860) |

**Abstract:** Introduces visual modalities (grid-based level + designer sketches) alongside text for PCGRL control. Uses quadruple contrastive learning for multi-modal capability and auxiliary reward from shared representation for policy alignment.

**Key innovations:**
- Multi-modal PCGRL: text + level grid + designer sketch
- Quadruple contrastive learning for unified control representation
- Human-aligned co-creative level design

---

### 4.5 Word2Minecraft: LLM-Based Minecraft Level Generation from Stories

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Mar 2025 |
| **Links** | [arXiv:2503.16536](https://arxiv.org/abs/2503.16536) |

**Abstract:** System leveraging LLMs to generate playable Minecraft levels from structured stories. Incorporates scaling algorithm for spatial consistency and sub-map generation for diverse objectives. Compares GPT-4-Turbo and GPT-4o-Mini on story coherence, diversity, enjoyment, aesthetics, functionality.

**Key innovations:**
- Story-to-playable-level translation
- Spatial consistency via dynamic tile scaling
- Multi-objective sub-map generation

---

### 4.6 Learning Local Constraints for RL Content Generators (WFC + PCGRL)

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, May 2026 |
| **Links** | [arXiv:2605.13570](https://arxiv.org/abs/2605.13570) |

**Abstract:** Combines Wave Function Collapse (WFC) local constraints with PCGRL global guarantees for Lode Runner level generation. PPO-based RL agent selects tile values under WFC-learned local constraints. Generates visually satisfying and playable puzzle-platform levels.

**Key innovations:**
- Hybrid WFC + PCGRL for local aesthetics + global playability
- Constrained action space via learned local patterns
- Random collapse starting state for robust generalization

---

### 4.7 WorldGen: From Text to Traversable and Interactive 3D Worlds

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Nov 2025 |
| **Links** | [arXiv:2511.16825](https://arxiv.org/abs/2511.16825) |

**Abstract:** System for automatic creation of large-scale interactive 3D worlds from text prompts. Combines LLM-driven scene layout reasoning, procedural generation, diffusion-based 3D generation, and object-aware scene decomposition. Modular and controllable for gaming and simulation.

**Key innovations:**
- End-to-end text-to-3D-world pipeline
- Procedural generation guided by LLM-parsed natural language
- Object-aware scene decomposition for editability

---

### 4.8 Forking Garden: Narrative Arc-Conditioned Gameplay Planning

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, May 2026 |
| **Links** | [arXiv:2605.01245](https://arxiv.org/abs/2605.01245) |

**Abstract:** Framework for narrative arc-conditioned gameplay planning that generates branching games from user-provided storylines. Uses emotional arc framework (Reagan et al.) to guide dungeon graph assembly with multimodal alignment of gameplay elements. End-to-end interactive system in Unity.

**Key innovations:**
- Narrative archetype (Hero's Journey, Three-act) guided generation
- DAG-based branching dungeon graphs
- Multimodal alignment: NPC, enemy, item, combat aligned to narrative state

---

### 4.9 Database-Driven Framework for 3D Level Generation with LLMs

| Field | Value |
|-------|-------|
| **Authors** | Xu, Verbrugge |
| **Affiliation** | N/A |
| **Venue** | FDG 2025 PCG Workshop |
| **Links** | [arXiv:2508.18533](https://arxiv.org/abs/2508.18533) |

**Abstract:** Offline LLM-assisted construction of reusable databases for architectural components and gameplay mechanics. Multi-phase pipeline: Room DB → Facility DB → Mechanics DB → repair system for navigability. Eliminates live LLM calls at generation time for deterministic control.

**Key innovations:**
- Fully offline database-driven PCG (no live LLM calls)
- Multi-floor navigable 3D levels
- Configurable gameplay progression pacing

---

### 4.10 Narrative-to-Scene Generation: LLM Pipeline for 2D Game Environments

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Sep 2025 |
| **Links** | [arXiv:2509.04481](https://arxiv.org/abs/2509.04481) |

**Abstract:** Lightweight pipeline transforming short narrative prompts into 2D tile-based game scenes reflecting temporal story structure. Uses (1) LLM for story segmentation, (2) spatial predicate extraction as "Object-Relation-Object" triples, (3) GameTileNet semantic embeddings for asset retrieval, (4) Cellular Automata terrain generation.

**Key innovations:**
- Temporal story segmentation into game scenes
- Symbolic spatial predicate representation
- Affordance-aware tile embedding retrieval
- Lightweight, model-agnostic pipeline

---

### 4.11 MultiGen: Level-Design for Editable Multiplayer Worlds in Diffusion Game Engines

| Field | Value |
|-------|-------|
| **Authors** | Ryan Po et al. |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Mar 2026 |
| **Links** | [arXiv:2603.06679](https://arxiv.org/abs/2603.06679) |

**Abstract:** Introduces explicit external memory into diffusion game engines for editable, reproducible experiences and multiplayer shared inference. Decomposes generation into Memory, Observation, and Dynamics modules. Users get direct editable control via persistent state representation.

**Key innovations:**
- External persistent memory for diffusion game engines
- Decomposed generation (Memory → Observation → Dynamics)
- Real-time multiplayer rollouts with consistent viewpoints

---

## 5. Game Benchmarks

### 5.1 BALROG: Benchmarking Agentic LLM and VLM Reasoning on Games

| Field | Value |
|-------|-------|
| **Authors** | Paglieri et al. |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Nov 2024 |
| **Links** | [arXiv:2411.13543](https://arxiv.org/abs/2411.13543) |

**Abstract:** Aggregates complex RL game environments (BabyAI, Crafter, TextWorld, Baba Is AI, MiniHack, NetHack) into unified testbed for long-context LLM/VLM evaluation. Games are procedurally generated, preventing memorization. Spans difficulty from fair zero-shot performance (BabyAI) to near-impossible (NetHack).

**Key innovations:**
- Unified multi-game benchmark for LLM/VLM agents
- Procedural generation prevents data contamination
- Wide difficulty spectrum with lightweight simulators
- LLMs know game mechanics but fail to apply them (knowledge-action gap)

---

### 5.2 GameWorld: Standardized and Verifiable Evaluation of Multimodal Game Agents

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Apr 2026 |
| **Links** | [arXiv:2604.07429](https://arxiv.org/abs/2604.07429) |

**Abstract:** Standardized benchmark for MLLM game agents in browser environments. 34 games, 170 tasks, two agent interfaces: Computer-Use Agents (raw keyboard/mouse) and Generalist Multimodal Agents (semantic action space). Features state-verifiable metrics and decoupled inference latency. Evaluates 18 model-interface pairs.

**Key innovations:**
- Standardized browser-based sandbox with paused game execution
- State-verifiable outcome-based evaluation
- Dual interface study: raw controls vs. semantic actions
- Reproducibility through full-benchmark rerun studies

---

### 5.3 OmniGameArena: Unified UE5 Benchmark for VLM Game Agents

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Jun 2026 |
| **Links** | [arXiv:2606.09826](https://arxiv.org/abs/2606.09826) |

**Abstract:** Suite of 12 custom Unreal Engine 5 games spanning Solo, PvP, and Coop regimes. Evaluates distinct capability axes of vision-based game agents. Addresses pre-training contamination by building new games. Studies improvement dynamics across repeated interaction.

**Key innovations:**
- Custom UE5 games (no contamination risk)
- Three interaction regimes: Solo, PvP, Coop
- Continuous progress metrics for capability tracking
- Repeated interaction analysis (beyond single-shot scores)

---

### 5.4 Orak: Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games

| Field | Value |
|-------|-------|
| **Authors** | KRAFTON AI |
| **Affiliation** | KRAFTON |
| **Venue** | arXiv preprint, Jun 2026 |
| **Links** | [arXiv:2506.03610](https://arxiv.org/abs/2506.03610) |

**Abstract:** Benchmark for training/evaluating LLM agents across 12 popular games spanning all major genres. Uses plug-and-play MCP interface for agentic modules (reflection, planning). Releases fine-tuning dataset of expert LLM gameplay trajectories. Supports game leaderboards, LLM battle arenas, and in-depth analysis.

**Key innovations:**
- MCP-based plug-and-play agentic module interface
- 12 games across 6 genres (action, adventure, RPG, simulation, strategy, puzzle)
- Expert LLM gameplay trajectory fine-tuning dataset
- Multi-dimensional evaluation (leaderboards, battle arenas, agentic strategy analysis)

---

### 5.5 Agentick: Unified Benchmark for General Sequential Decision-Making Agents

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, May 2026 |
| **Links** | [arXiv:2605.06869](https://arxiv.org/abs/2605.06869) |

**Abstract:** Provides purpose-built capability categories, five synchronized observation modalities, standardized LLM/VLM/RL harnesses, oracle trajectory datasets, and unified scoring protocol. Designed for cross-paradigm comparison between RL, LLM, and VLM agents.

**Key innovations:**
- Cross-paradigm comparison: RL vs. LLM vs. VLM
- Five synchronized observation modalities
- Capability decomposition across categories
- Unified scoring protocol

---

### 5.6 MineExplorer: Evaluating Open-World Exploration of MLLM Agents in Minecraft

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, May 2026 |
| **Links** | [arXiv:2605.30931](https://arxiv.org/abs/2605.30931) |

**Abstract:** Benchmark for evaluating open-world exploration in Minecraft. Filters Minecraft-specific knowledge reliance, organizes tasks around ReAct-style capability formulation, composes atomic tasks into implicit multi-hop tasks. Uses multi-agent synthesis for reliable instance generation.

**Key innovations:**
- Deconfounds Minecraft-specific knowledge from general exploration
- Implicit multi-hop task composition from atomic tasks
- Multi-agent synthesis workflow for task reliability
- Task difficulty tracking and model capability analysis

---

### 5.7 MCU (Minecraft Universe): Evaluation Framework for Open-Ended Game Agents

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | CraftJarvis |
| **Venue** | ICML 2025 Spotlight |
| **Links** | [OpenReview](https://openreview.net/forum?id=hrdLhNDAzp) |

**Abstract:** Comprehensive evaluation framework in Minecraft with 3,452 composable atomic tasks across 11 categories, task composition mechanism for infinite diverse tasks, and automated evaluation achieving 91.5% human alignment. Even SOTA foundation agents struggle with increasing complexity.

**Key innovations:**
- 3,452 atomic tasks across 11 major categories
- Infinite task composition with diverse difficulty
- 91.5% human rating alignment for open-ended assessment

---

### 5.8 lmgame-Bench: How Good are LLMs at Playing Games?

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | ICLR 2026 (noted in search results) |
| **Links** | [arXiv:2505.15146](https://arxiv.org/abs/2505.15146) |

**Abstract:** Studies challenges in using video games to evaluate LLMs: brittle vision, prompt sensitivity, data contamination. Introduces lmgame-Bench with Gym-style API, perception/memory scaffolds, standardized prompt optimization. RL on a single game transfers to unseen games and external planning tasks.

**Key innovations:**
- Identifies three evaluation failure modes (vision, prompt, contamination)
- Perception and memory scaffolds for principled evaluation
- Transfer learning from games to external planning tasks
- 13 leading models evaluated across platformer, puzzle, narrative games

---

### 5.9 TextAtari: 100K Frames Game Playing with Language Agents

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Jun 2026 |
| **Links** | [arXiv:2506.04098](https://arxiv.org/abs/2506.04098) |

**Abstract:** Converts Atari games into rich textual descriptions for evaluating long-horizon reasoning in language agents. Supports up to 10,000-step horizons. Evaluates three agent architectures across diverse Atari game tasks.

**Key innovations:**
- Textual rendering of Atari for LLM-based agents
- Ultra-long horizon benchmark (10,000 steps)
- Categories: exploration, planning, skill acquisition tasks

---

### 5.10 MineNPC-Task: Task Suite for Memory-Aware Minecraft Agents

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Jan 2026 |
| **Links** | [arXiv:2601.05215](https://arxiv.org/abs/2601.05215) |

**Abstract:** User-authored benchmark for memory-aware, mixed-initiative LLM agents in Minecraft. Tasks elicited from co-play with expert players, normalized into parametric templates with machine-checkable validators. Captures plan/act/memory events.

**Key innovations:**
- User-authored (not synthetic) task generation
- Machine-checkable validators with bounded-knowledge policy
- Mixed-initiative agent-human interaction evaluation
- Plan/act/memory event logging for failure analysis

---

## 6. Industry Game AI

### 6.1 Generative AI for Dynamic NPC Behavior and PCG: Production Deployment

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | Industry survey |
| **Venue** | IJETCSIT, May 2026 |
| **Links** | [IJETCSIT](https://www.ijetcsit.org/index.php/ijetcsit/article/view/743) |

**Abstract:** Comprehensive technical examination of generative AI architectures for NPC behavior and PCG in commercial games. Evaluates production deployments: Epic Games (Fortnite AI NPC), Rockstar (GTA VI dialogue decay), Ubisoft (NEO NPC), NVIDIA ACE, Inworld AI. Reports 25-40% dev time reduction, 20%+ cost savings, 40% player satisfaction improvement.

**Key innovations:**
- Analysis of production game AI deployments
- Multi-layer stack: perception → reasoning → dialogue → memory → action
- Real-world metrics from AAA studios
- Addresses SAG-AFTRA, ethical implications, emergent behavior containment

---

### 6.2 Game Companies Transform into AI Enterprises

| Field | Value |
|-------|-------|
| **Authors** | Industry reporting |
| **Source** | Chosun, Jun 2026 |
| **Links** | [Article](https://www.chosun.com/english/industry-en/2026/06/23/CPA44UMN7NBMXL5RTNHN63HMBQ/) |

**Highlights:**
- KRAFTON invests ₩50B in HyperAccel (AI semiconductor startup developing LPUs for LLM inference)
- Sony acquires Cineverse Labs (ML for 3D environment conversion)
- Roblox acquired Room.ai (3D avatars via deep learning)
- Tencent invests ¥1.8B in Enflame Technology (AI chips)
- VibeCoding emerges as core tool in game development

---

### 6.3 Sony PlayStation AI Strategy

| Field | Value |
|-------|-------|
| **Source** | SEC Filing / Insider Gaming, Jun 2026 |
| **Links** | [Insider Gaming](https://insider-gaming.com/sony-clarifies-playstation-ai-usage/) |

**Highlights:**
- AI for game development productivity
- AI for graphical improvements (upscaling, rendering)
- AI for player transaction routing and recommendations
- "Unleash the creativity of studios" via AI tooling

---

### 6.4 Devcom 2025: Edge-Cloud AI for Game Production

| Field | Value |
|-------|-------|
| **Source** | Devcom 2025 Panel |
| **Links** | [DualMedia](https://www.dualmedia.com/gaming-empowered-ai-devcom/) |

**Highlights:**
- Edge-first inference for low-latency NPC decision loops
- Federated learning for privacy-preserving model training
- Unity/Epic Games middleware integration for runtime AI
- Console certification constraints (Xbox, PlayStation)

---

## 7. Related Techniques

### 7.1 Self-Play & Multi-Agent RL

#### 7.1.1 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning

| Field | Value |
|-------|-------|
| **Authors** | Liu, Guertler, Yu, et al. |
| **Affiliation** | N/A |
| **Venue** | ICLR 2026 |
| **Links** | [arXiv:2506.24119](https://arxiv.org/abs/2506.24119) |

**Abstract:** Applies self-play to two-player zero-sum language games (TicTacToe, Kuhn Poker, Simple Negotiation) for developing reasoning in LLMs. Introduces role-conditioned advantage estimation (RAE) for stable multi-agent training. Multi-game training achieves up to 10% improvement across 8 reasoning benchmarks (MATH500, AIME, GPQA, MMLU-Pro).

**Key innovations:**
- Unlimited training data via game dynamics (no human-curated pairs)
- Role-conditioned advantage estimation for multi-agent stability
- Transferable reasoning from games to general benchmarks
- Distributed actor-learner architecture for multi-turn self-play

---

#### 7.1.2 Stratagem: Learning Transferable Reasoning via Trajectory-Modulated Game Self-Play

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Apr 2026 |
| **Links** | [arXiv:2604.17696](https://arxiv.org/abs/2604.17696) |

**Abstract:** Learns transferable reasoning by selectively reinforcing trajectories that exhibit domain-agnostic and adaptive reasoning patterns. Uses transferability advantage and reasoning evolution reward to go beyond terminal game outcomes. Addresses domain specificity and shallow adaptation.

**Key innovations:**
- Trajectory-level transferability scoring
- Multiplicative transferability × additive reasoning evolution reward
- Domain-agnostic pattern reinforcement over game-specific heuristics

---

#### 7.1.3 MARSHAL: Multi-Agent Reasoning via Self-Play with Strategic LLMs

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Oct 2025 |
| **Links** | [arXiv:2510.15414](https://arxiv.org/abs/2510.15414) |

**Abstract:** End-to-end RL framework for multi-agent reasoning in cooperative and competitive games. Features turn-level advantage estimator and agent-specific advantage normalization. Up to 28.7% improvement in held-out games. Zero-shot gains of 10.0% on AIME, 7.6% on GPQA-Diamond when integrated into leading MAS systems.

**Key innovations:**
- Turn-level advantage estimation for fine-grained credit assignment
- Agent-specific advantage normalization for heterogeneous roles
- Cross-game generalization to reasoning benchmarks
- GRPO-based multi-agent self-play

---

#### 7.1.4 OMAR: One Model, All Roles — Multi-Turn Multi-Agent Self-Play

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Feb 2026 |
| **Links** | [arXiv:2602.03109](https://arxiv.org/abs/2602.03109) |

**Abstract:** Single model role-plays all participants in conversations simultaneously, learning long-term goals and social norms from dynamic interaction. Uses hierarchical advantage estimation (turn-level + token-level). Trained in SOTOPIA social environment and Werewolf games. Emergent empathy, persuasion, and compromise-seeking.

**Key innovations:**
- Single model for all roles in multi-agent conversation
- Hierarchical advantage estimation across turns and tokens
- Emergent social behaviors without human supervision
- Competitive scenarios incentivize collaborative behaviors

---

#### 7.1.5 PopuLoRA: Co-Evolving LLM Populations for Reasoning Self-Play

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, May 2026 |
| **Links** | [arXiv:2605.16727](https://arxiv.org/abs/2605.16727) |

**Abstract:** Population-based asymmetric self-play using LoRA adapters on a shared frozen base. Teachers propose problems, students solve under programmatic verifier. LoRA weight-space evolution operators (mutations, crossovers) serve as PBT replacement. Population arms race: increasingly complex problems, expanding coverage.

**Key innovations:**
- LoRA-based population training (no separate full models)
- Cross-evolution between teacher and student sub-populations
- LoRA weight-space mutations and crossovers (seconds per step)
- Avoids single-agent mode collapse/self-calibration

---

#### 7.1.6 Foundation Model Self-Play (FMSP): Open-Ended Strategy Innovation

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Jul 2025 |
| **Links** | [arXiv:2507.06466](https://arxiv.org/abs/2507.06466) |

**Abstract:** Three variants: (1) vFMSP refines policies via competitive self-play, (2) NSSP builds diverse population ignoring performance, (3) QDSP combines quality + diversity. In Car Tag, discovers RL, tree search, heuristic methods. In Gandalf, jailbreaks LLM defenses and patches vulnerabilities automatically.

**Key innovations:**
- Foundation models as strategy innovation engines
- Quality-Diversity Self-Play for diverse high-quality policies
- Cross-paradigm strategy discovery (RL, search, heuristics)
- Automatic red-teaming and vulnerability patching

---

#### 7.1.7 PolicyEvolve: Evolve Programmatic Policies via LLMs + Population-Based Training

| Field | Value |
|-------|-------|
| **Authors** | Lv, Liu, Luo, Zhang, Ou |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Sep 2025 |
| **Links** | [arXiv:2509.06053](https://arxiv.org/abs/2509.06053) |

**Abstract:** Framework for multi-agent tasks enabling policy generation and improvement without human intervention. Maintains global policy pool (elite policies) + local pool (temporary policies). Policy Planner + Trajectory Critic for iterative refinement. Consistent ELO improvement across multi-player zero-sum games.

**Key innovations:**
- LLM generates programmatic policies for games
- Global/local policy pools with population-based training
- Trajectory Critic identifies vulnerabilities for improvement
- White-box programmatic policy output

---

#### 7.1.8 π-Play: Multi-Agent Self-Play via Privileged Self-Distillation

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Apr 2026 |
| **Links** | [arXiv:2604.14054](https://arxiv.org/abs/2604.14054) |

**Abstract:** Exploits question construction path (QCP) as privileged information naturally produced by self-play. Teacher model uses QCP as privileged context to densely supervise student via self-distillation. Transforms sparse-reward self-play into dense-feedback evolution loop. Surpasses fully supervised search agents.

**Key innovations:**
- Natural privileged information from self-play process
- Dense self-distillation from teacher to student
- 2–3× efficiency improvement over conventional self-play

---

#### 7.1.9 Beyond Static Evaluation: Co-Evolutionary Mechanisms for LLM-Driven Strategy Evolution

| Field | Value |
|-------|-------|
| **Authors** | Sygkounas et al. |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Jun 2026 |
| **Links** | [arXiv:2606.10389](https://arxiv.org/abs/2606.10389) |

**Abstract:** Extends FAMOU framework to adversarial multi-agent games by co-evolving the evaluation process alongside strategies. 3v3 maritime capture-the-flag: 68.0% win rate across ten benchmark opponents. Evolves tactical structures (lookahead search, EWMA interception) absent from seed strategies.

**Key innovations:**
- Co-evolution of evaluation and strategy
- LLM as directed mutation operator producing algorithmic innovations
- Emergent tactical structures from evolution

---

#### 7.1.10 Scalable Population Training for Zero-Shot Coordination

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Nov 2025 |
| **Links** | [arXiv:2511.11083](https://arxiv.org/abs/2511.11083) |

**Abstract:** Addresses Zero-Shot Coordination (ZSC) — agents must collaborate with unseen partners. Uses meta-agent for efficient population training with mutual information term for population divergence. Avoids heavy computational load of training separate neural networks per agent.

**Key innovations:**
- Meta-agent for population training (efficient)
- Mutual information divergence for population diversity
- Value-based method compatible

---

#### 7.1.11 COvolve: Co-Evolution of LLM-Generated Strategies

| Field | Value |
|-------|-------|
| **Authors** | Sygkounas et al. |
| **Affiliation** | N/A |
| **Venue** | 2026 (noted in FMSP paper) |

**Abstract:** Models LLM-generated strategies and environments as a zero-sum game. Improves strategy robustness through adversarial co-evolution.

---

#### 7.1.12 Multi-Agent Training for Pommerman: Curriculum Learning and Population-Based Self-Play

| Field | Value |
|-------|-------|
| **Authors** | Giang Cao et al. |
| **Affiliation** | N/A |
| **Venue** | arXiv, updated Jan 2025 |
| **Links** | [arXiv:2407.00662](https://arxiv.org/abs/2407.00662) |

**Abstract:** Combines curriculum learning and population-based self-play for Pommerman. Addresses sparse rewards with adaptive annealing factor for dense exploration reward, and Elo-based matchmaking.

---

### 7.2 World Models & Model-Based RL

#### 7.2.1 Dreamer-CDP: Improving Reconstruction-free World Models

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Mar 2026 |
| **Links** | [arXiv:2603.07083](https://arxiv.org/abs/2603.07083) |

**Abstract:** Removes reconstruction loss from DreamerV3, adds JEPA-style predictor for Continuous Deterministic Representation Prediction. Achieves Crafter score of 16.2% (on par with DreamerV3 at 14.5%). Shows reconstruction is not necessary for effective world models.

**Key innovations:**
- Decoder-free world model architecture
- JEPA-style next latent prediction
- Competitive performance without pixel reconstruction

---

#### 7.2.2 NE-Dreamer: Next Embedding Prediction for World Models

| Field | Value |
|-------|-------|
| **Authors** | Xu, Ma, Chai, et al. |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Mar 2026 |
| **Links** | [arXiv:2603.02765](https://arxiv.org/abs/2603.02765) |

**Abstract:** Decoder-free MBRL agent using temporal transformer to predict next-step encoder embeddings. On DeepMind Control Suite matches DreamerV3. On DMLab (memory + spatial reasoning tasks), achieves substantial gains. Next-embedding prediction with temporal transformers as effective scalable framework.

**Key innovations:**
- Temporal transformer for next-embedding prediction
- No reconstruction loss or auxiliary supervision
- Strong long-horizon memory and spatial reasoning

---

#### 7.2.3 Optimistic World Models (OWM) for Efficient Exploration

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Feb 2026 |
| **Links** | [arXiv:2602.10044](https://arxiv.org/abs/2602.10044) |

**Abstract:** Framework for optimistic exploration with biased maximum likelihood estimation. Integrates optimistic dynamics loss requiring no hyperparameter tuning. Instantiated as Optimistic DreamerV3 and Optimistic STORM — demonstrate improved sample efficiency on Atari100K and DMC.

**Key innovations:**
- Optimistic dynamics loss for exploration
- Drop-in replacement for any Dreamer-style world model
- Minimal hyperparameter tuning required
- Combines well with actor entropy bonuses

---

#### 7.2.4 ARROW: Augmented Replay for Robust World Models (Continual RL)

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Mar 2026 |
| **Links** | [arXiv:2603.11395](https://arxiv.org/abs/2603.11395) |

**Abstract:** Model-based continual RL extending DreamerV3 with dual-buffer replay mechanism (short-term FIFO + long-term distribution-matching). Demonstrates substantially less forgetting on non-shared-structure tasks (Atari) while maintaining forward transfer on shared-structure tasks (Procgen CoinRun).

**Key innovations:**
- Biologically-inspired dual replay buffer
- Model-based continual learning with fixed memory budget
- No task identifiers required

---

#### 7.2.5 Code World Models (CWM): LLM-Generated Game Models

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Oct 2025 |
| **Links** | [arXiv:2510.04542](https://arxiv.org/abs/2510.04542) |

**Abstract:** LLMs generate game world models as Python code from trajectory data + textual descriptions. Extends CWM framework to two-player games, synthesizes value functions for MCTS, introduces inference-as-code for imperfect information games. Outperforms frontier "thinking" LLMs on multiple perfect and imperfect information games.

**Key innovations:**
- LLM as induction engine for world model code
- Code-based autoencoders for imperfect information state estimation
- Synthesized heuristic value functions for search-based policies
- Generalizes to OOD (novel) games

---

#### 7.2.6 Distilling Game Code World Model Generation into Lightweight LLMs

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, May 2026 |
| **Links** | [arXiv:2605.24375](https://arxiv.org/abs/2605.24375) |

**Abstract:** Distills GameCWM generation into Qwen2.5-3B-Instruct via SFT + RLVR (GRPO). Curated dataset of 30 games spanning perfect and imperfect information games. Verification framework for structural and semantic game properties. SFT improves syntactic correctness; RLVR improves execution-level rule adherence.

**Key innovations:**
- Distillation of world model generation to small models (3B)
- SFT + RLVR post-training pipeline with execution verifier
- Makes automatic environment generation scalable

---

#### 7.2.7 LAMIR: Look-Ahead Reasoning with Learned Model in Imperfect Information Games

| Field | Value |
|-------|-------|
| **Authors** | Ondrej Kubicek, Viliam Lisý |
| **Affiliation** | N/A |
| **Venue** | ICLR 2026 Poster |
| **Links** | [OpenReview](https://openreview.net/forum?id=NnBbr4hI8a) |

**Abstract:** Learns abstracted model of an imperfect information game from agent-environment interaction. At test time, uses trained model for look-ahead reasoning. Learned abstraction limits subgame size, making principled look-ahead tractable in large games where previous methods could not scale.

---

#### 7.2.8 Matrix-Game 3.0: Real-Time Streaming Interactive World Model

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Apr 2026 |
| **Links** | [arXiv:2604.08995](https://arxiv.org/abs/2604.08995) |

**Abstract:** Memory-augmented interactive world model for 720p real-time (40 FPS) long-form video generation. Upgrades: synthetic data from Unreal Engine + AAA game data + real-world video augmentation. Self-correction via residual re-injection, camera-aware memory retrieval. Scaling to 2×14B model.

**Key innovations:**
- Real-time 720p generation at 40 FPS
- Industrial-scale data engine (Unreal + AAA + real)
- Long-horizon memory via residual self-correction
- DMD distillation for efficient inference

---

#### 7.2.9 Heterogeneous Generative Game Engine (Real-Time Neural Rendering)

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Feb 2026 |
| **Links** | [arXiv:2602.00608](https://arxiv.org/abs/2602.00608) |

**Abstract:** Bridges "Memory Wall" for generative game engines. Heterogeneous computing on NPU cluster, decoupling compute-bound DiT from memory-bound decoder. Achieves 720×480 resolution at 48.3 FPS — 50× increase in pixel throughput. Manifold-Aware Latent Extrapolation for ultra-low latency.

**Key innovations:**
- Heterogeneous compute architecture for generative games
- Memory-centric operator fusion with on-chip SRAM
- 50× pixel throughput improvement over prior generative engines
- Manifold-Aware Latent Extrapolation for perceived responsiveness

---

### 7.3 Curiosity-Driven Exploration

#### 7.3.1 GLANCE: Visual-Linguistic Curiosity for VLM Agents

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, May 2026 |
| **Links** | [arXiv:2605.03782](https://arxiv.org/abs/2605.03782) |

**Abstract:** Cross-modal curiosity for VLM agents: "what the VLM agent thinks should predict what it sees." Uses linguistic CoT-future prediction error as intrinsic reward. Outperforms exploitation-based RL methods across Grid Puzzles, 3D Navigation, Object Manipulation, Geometric Reconstruction. Lightweight — VLM serves as both world model and policy.

**Key innovations:**
- Cross-modal curiosity (linguistic hypothesis → visual reality)
- VLM as unified world model + policy
- Works without extrinsic rewards
- Curriculum exploration prevents curiosity collapse

---

#### 7.3.2 CDE: Curiosity-Driven Exploration for LLM Reasoning

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Sep 2025 |
| **Links** | [arXiv:2509.09675](https://arxiv.org/abs/2509.09675) |

**Abstract:** Curiosity signals from both actor (perplexity over generated response) and critic (multi-head value variance). Actor curiosity penalizes overconfident errors; critic curiosity connects to count-based exploration. Approx. +3 points on AIME over standard GRPO/PPO.

**Key innovations:**
- Dual-source curiosity: actor perplexity + critic value variance
- Theoretical connection to count-based exploration
- Identifies calibration collapse mechanism in RLVR

---

#### 7.3.3 CuES: Curiosity-Driven Environment-Grounded Task Synthesis

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | Alibaba (ModelScope) |
| **Venue** | arXiv preprint, Dec 2025 |
| **Links** | [arXiv:2512.01311](https://arxiv.org/abs/2512.01311) |

**Abstract:** Framework for autonomous task generation in agentic RL environments. Drives exploration via intrinsic curiosity, abstracts interaction patterns into reusable task schemas. Produces task distributions matching manual curation across AppWorld, BFCL, WebShop.

**Key innovations:**
- Solves task scarcity for agentic RL
- Curiosity-driven task schema discovery
- Top-down guidance + memory-based quality control

---

#### 7.3.4 CERMIC: Multi-Agent Curiosity Calibration

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Sep 2025 |
| **Links** | [arXiv:2509.20648](https://arxiv.org/abs/2509.20648) |

**Abstract:** Plug-and-play module for MARL exploration. Uses Information Bottleneck to learn multi-agent contextualized exploratory representation. Filters spurious novelty via inferred peer intentions. Grounded in Bayesian Surprise with theoretical guarantees.

**Key innovations:**
- Multi-agent contextualized curiosity calibration
- Information Bottleneck for robust novelty filtering
- Plug-and-play with MAPPO, QMIX
- Theoretical intrinsic reward guarantees

---

### 7.4 Hierarchical RL

#### 7.4.1 H2RL: Hybrid Hierarchical RL with Logical Pretraining

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Mar 2026 |
| **Links** | [arXiv:2603.06565](https://arxiv.org/abs/2603.06565) |

**Abstract:** Neuro-symbolic HRL framework using differentiable symbolic logic and options for pretraining. Embeds logic priors into neural policies via logic-informed pretraining. Mitigates policy misalignment and improves long-horizon decision-making without logical reasoning at inference.

**Key innovations:**
- Differentiable symbolic logic for option-based pretraining
- Mitigates reward over-exploitation and misalignment
- No logical reasoning required at inference time

---

#### 7.4.2 HiPER: Hierarchical RL with Explicit Credit Assignment for LLM Agents

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Feb 2026 |
| **Links** | [arXiv:2602.16165](https://arxiv.org/abs/2602.16165) |

**Abstract:** Separates slow high-level planning from fast low-level action execution in LLM agents. Proposes Hierarchical Advantage Estimation (HAE) with boundary-aware bootstrapping. Addresses long-horizon sparse-reward credit assignment.

**Key innovations:**
- Plan-Execute factorization for LLM agent hierarchy
- Hierarchical Advantage Estimation for cross-level credit assignment
- Boundary-aware bootstrapping coupling high and low levels

---

#### 7.4.3 STEP-HRL: Augmented Step-Level Transitions for LLM Agents

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Apr 2026 |
| **Links** | [arXiv:2604.05808](https://arxiv.org/abs/2604.05808) |

**Abstract:** Enables step-level learning in LLM agents by conditioning on single-step transitions rather than full interaction histories. Uses completed subtasks for global progress + local progress module for iterative summarization. Outperforms baselines on ScienceWorld and ALFWorld while reducing token usage.

**Key innovations:**
- Step-level policy (constant input size, not full history)
- Local progress module for compact subtask summarization
- Reduced computational cost + better generalization

---

### 7.5 Inverse RL & Reward Design

#### 7.5.1 rePIRL: Learn PRM with Inverse RL for LLM Reasoning

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Feb 2026 |
| **Links** | [arXiv:2602.07832](https://arxiv.org/abs/2602.07832) |

**Abstract:** IRL-inspired framework for learning Process Reward Models (PRMs) for LLM reasoning. Models multi-step reasoning as token-level MDP with maximum entropy RL loss. Unifies online and offline PRM learning (DPO, PRIME, Math-Shepherd, MCTS) under a single framework.

**Key innovations:**
- Inverse RL for PRM learning in LLM reasoning
- Token-level MDP formulation
- Unified framework for DPO, PRIME, MCTS methods

---

### 7.6 Imitation Learning & Behavior Cloning

#### 7.6.1 Scaling Behavior Cloning Improves Causal Reasoning (see also 3.4)

Refer to Section 3.4 for the open model for real-time video game playing. Also demonstrates that scaling data and model size in behavior cloning improves causal reasoning capabilities.

#### 7.6.2 Combining Code-Generating LLMs and Self-Play to Iteratively Refine Strategies in Games

| Field | Value |
|-------|-------|
| **Authors** | Yoram Bachrach, Edan Toledo, Karen Hambardzumyan, et al. (incl. Jakob Foerster, Roberta Raileanu, Andrei Lupu) |
| **Affiliation** | N/A |
| **Venue** | IJCAI 2025 |
| **Links** | [IJCAI Proceedings](https://www.ijcai.org/proceedings/2025/1249) |

**Abstract:** Uses LLM to generate game-playing bot code, then uses Policy Space Response Oracle (PSRO) framework for iterative refinement through competition. Mixture Bot adapts strategy per game by selecting from a portfolio. Combines SWE-agent capabilities with game-theoretic self-play.

**Key innovations:**
- LLM generates executable game bot code
- PSRO for iterative strategy refinement
- Mixture Bot selects strategy adaptively
- Combines program synthesis with game theory

---

### 7.7 Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, May 2026 |
| **Links** | [arXiv:2605.00347](https://arxiv.org/abs/2605.00347) |

**Abstract:** Studies RL-based training of VLMs for long-horizon (100+ turns) decision-making in Super Mario Land. Proposes adapted PPO with lightweight turn-level critic — outperforms critic-free methods (GRPO, Reinforce++). Pretrained VLMs provide strong action priors. Achieves 3× average game progress vs. frontier models.

**Key innovations:**
- Lightweight turn-level critic for stable multi-modal RL
- Pretrained VLMs as effective action priors
- Cross-game generalization while maintaining general capabilities
- Open training framework (Odysseus)

---

### 7.8 Matrix-Game: Interactive World Foundation Model

| Field | Value |
|-------|-------|
| **Authors** | N/A |
| **Affiliation** | N/A |
| **Venue** | arXiv preprint, Jun 2026 |
| **Links** | [arXiv:2506.18701](https://arxiv.org/abs/2506.18701) |

**Abstract:** Interactive world foundation model for game world generation. Includes Matrix-Game-MC dataset (Minecraft world modeling) and GameWorld Score benchmark for evaluation. Diffusion-based image-to-world with keyboard/mouse control.

**Key innovations:**
- Diffusion-based interactive world generation
- Large-scale annotated Minecraft dataset
- Multi-dimensional evaluation benchmark (visual, temporal, controllability, physics)

---

## Summary Statistics

| Category | Paper Count |
|----------|-------------|
| Game RL | 6 |
| LLM Game AI Bots | 8 |
| Game Foundation Models | 6 |
| Procedural Content Generation | 11 |
| Game Benchmarks | 10 |
| Industry Game AI | 4 |
| Self-Play & Multi-Agent RL | 12 |
| World Models & Model-Based RL | 9 |
| Curiosity-Driven Exploration | 4 |
| Hierarchical RL | 3 |
| Inverse RL / Imitation Learning | 2 |
| **Total** | **~75 papers** |

## Key Themes

1. **Convergence of RL + LLM**: Self-play in games is becoming the dominant paradigm for training general reasoning capabilities in LLMs (SPIRAL, MARSHAL, Stratagem, OMAR)
2. **Game Foundation Models**: From single-game specialists to multi-game generalists (NitroGen, Game-TARS, Pixels2Play, P2Play) — all using behavior cloning at scale
3. **LLM as World Model Generator**: Code World Models enable LLMs to synthesize game environments from descriptions (CWM, Distilled CWM)
4. **Diffusion Game Engines**: Real-time generative game worlds at 720p/40FPS (Matrix-Game 3.0) — approaching production viability
5. **LLM-Powered NPCs**: From static dialogue trees to dynamic, memory-augmented, emotionally aware characters (ChatNPC, Deflanderization, Nemobot)
6. **Evaluation Infrastructure**: Benchmarks maturing from single-game RL (Atari) to multi-game multi-modal agent evaluation (GameWorld, OmniGameArena, Orak, MineExplorer)
7. **Population-Based Self-Play**: Evolving from simple self-play to sophisticated population training with LLM-based strategy innovation (PopuLoRA, FMSP, PolicyEvolve, COvolve)
8. **Industry Adoption**: Major studios (Epic, Rockstar, Ubisoft, KRAFTON, Sony, Tencent) investing in AI for NPCs, PCG, and inference hardware
