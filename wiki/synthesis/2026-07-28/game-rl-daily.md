---
title: Game RL & Game AI Bot — Daily Paper Digest (July 28, 2026)
type: synthesis
created: 2026-07-28
updated: 2026-07-28
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, pcg, benchmarks, world-models, self-play, vlm, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (July 28, 2026)

## 1. Game RL — Reinforcement Learning in Games

### 1.1 MARL-GPT: Foundation Model for Multi-Agent Reinforcement Learning
- **Authors**: Multiple authors (Cognitive-AI-Systems)
- **Affiliation**: Cognitive-AI-Systems / Academic
- **Venue**: arXiv preprint (April 2026)
- **Abstract**: Proposes MARL-GPT, a single GPT-based model that learns and performs well across diverse MARL environments including StarCraft Multi-Agent Challenge (SMACv2), Google Research Football (GRF), and POGEMA. Applies offline RL to train at scale on expert trajectories (400M for SMACv2, 100M for GRF, 1B for POGEMA) combined with a single transformer-based observation encoder requiring no task-specific tuning. Achieves competitive performance compared to specialized baselines in all tested environments.
- **Key Innovation**: First unified transformer-based foundation model for multiple multi-agent environments; scales from specialized to generalist MARL.
- **Link**: https://www.arxiv.org/pdf/2604.05943

### 1.2 HRL-IM/CBS: Hierarchical RL in StarCraft Micromanagement
- **Authors**: Multiple authors
- **Affiliation**: Academic
- **Venue**: arXiv preprint (June 2026)
- **Abstract**: Proposes HRL-IM/CBS, a hierarchical RL framework with influence map hashing and cluster-based scripts for StarCraft micromanagement. Influence map hashing encodes global battlefield situations into compact hexadecimal codes, capturing spatial control and relative advantage. Cluster-based scripts enable dynamic local coordination through adaptive unit partitioning. Hierarchical multi-Q-table architecture decomposes decision-making into upper-level clustering strategy selection and lower-level tactical execution. Experiments across six asymmetric scenarios demonstrate competitive performance against deep RL baselines with advantages in sample efficiency and interpretability.
- **Key Innovation**: Influence map hashing for state abstraction; interpretable Q-table representations for transparent decision-making.
- **Link**: https://arxiv.gg/abs/2606.30092

### 1.3 Reproducing AlphaZero on Tablut: Self-Play RL for Asymmetric Board Games
- **Authors**: Multiple authors
- **Affiliation**: Academic
- **Venue**: arXiv preprint (April 2026)
- **Abstract**: Investigates adaptation of AlphaZero to Tablut, an asymmetric historical board game with unequal piece counts and distinct player objectives (king capture vs king escape). Modifies architecture to use separate policy and value heads for each player role while maintaining a shared residual trunk. Mitigates training instabilities via C4 data augmentation, increased replay buffer size, and playing 25% of training games against randomly sampled past checkpoints. Over 100 self-play iterations, achieves BayesElo rating of 1235 relative to randomly initialized baseline.
- **Key Innovation**: Role-specific policy/value heads for asymmetric games; catastrophic forgetting mitigation techniques for self-play.
- **Link**: https://arxiv.org/abs/2604.05476v1

### 1.4 Open-ended Multi-agent Autocurricula via Visual Inspection of Policies
- **Authors**: Lorenzo Pantè, Andrea Fanti, Roberto Capobianco
- **Affiliation**: Academic
- **Venue**: arXiv preprint (July 2026)
- **Abstract**: Introduces Visual Inspection of Policies (VIP), leveraging a Video Language Model to process policy videos and provide curriculum recommendations for open-ended RL. Studies the approach on StarCraft Multi-Agent Challenge (SMAC). Shows that even with a lightweight and openly accessible VLM (VideoLLaMa2-7B), VIP can use policy videos to generate more effective curricula than both text-only ablation and methods relying on scalar task scores.
- **Key Innovation**: Using VLM to inspect policy behavior via recorded episode videos for curriculum design; video-based difficulty assessment.
- **Link**: https://arxiv.org/html/2607.08193

### 1.5 Play Like Champions: Counterfactual Feedback in Latent Space
- **Authors**: Multiple authors
- **Affiliation**: Academic
- **Venue**: arXiv preprint (June 2026)
- **Abstract**: Proposes generating counterfactual feedback in latent space for game playing, enabling agents to learn from hypothetical scenarios without requiring full environment rollouts.
- **Key Innovation**: Latent-space counterfactual generation for sample-efficient game learning.
- **Link**: https://arxiv.gg/abs/2607.00190

---

## 2. Game AI Bot — LLM-Powered Game Agents

### 2.1 AVA: Attentive VLM Agent for Mastering StarCraft II
- **Authors**: Weiyu Ma, Yuqian Fu, Zecheng Zhang, Bernard Ghanem, Guohao Li
- **Affiliation**: Academic (ACL 2026)
- **Venue**: Findings of ACL 2026 (San Diego)
- **Abstract**: Introduces AVACraft, the first multimodal benchmark environment for complex decision-making in StarCraft II, supporting both traditional MARL and modern VLM paradigms. Provides RGB visual inputs, natural language observations, and structured state information. Features 21 carefully designed scenarios covering micromanagement, coordination, and strategic planning. MARL methods achieve up to 27.1% win rate after 1M training steps, while VLMs deliver superior zero-shot performance (75-81% win rate) without any training.
- **Key Innovation**: Unified framework bridging MARL and VLM paradigms; systematic comparison of training-based vs zero-shot decision-making.
- **Link**: https://aclanthology.org/2026.findings-acl.208/

### 2.2 Nemobot Games: Strategic AI Gaming Agents with LLMs
- **Authors**: Multiple authors
- **Affiliation**: Academic
- **Venue**: arXiv preprint (April 2026)
- **Abstract**: Introduces Nemobot, an interactive agentic engineering environment extending Shannon's taxonomy of game-playing machines using LLMs. Demonstrates capabilities across four classes: dictionary-based games (compressed state-action mappings), rigorously solvable games (mathematical reasoning), heuristic-based games (minimax + crowd-sourced data), and learning-based games (RLHF + self-critique). Provides programmable environment for tool-augmented generation and fine-tuning of strategic game agents.
- **Key Innovation**: Operationalizing Shannon's taxonomy with LLMs; programmable prompt engineering for game-playing agents.
- **Link**: https://arxiv.org/abs/2604.21896v1

### 2.3 PCSP: Persona-Traceable Shared RL Policies for Scalable Game Agents
- **Authors**: Yoosung Hong
- **Affiliation**: Academic/Industry
- **Venue**: arXiv preprint (May 2026)
- **Abstract**: Introduces PCSP (Persona-Conditioned Shared Policy), a single RL policy conditioned on frozen LLM embeddings of free-form persona descriptions. Combines once-per-NPC persona encoding, low-rank persona projection, neural persona conditioning, and PPO + InfoNCE consistency + KL diversity training. On 300-persona life-simulation benchmark, achieves compositional zero-shot persona identification up to 17x above chance, Spearman ρ≈0.73 semantic-behavioral alignment, and 22x faster inference than LLM-as-policy baseline. UE5 deployment demonstrates sub-frame inference at 64 agents with 1.7% failure rate.
- **Key Innovation**: Single shared policy supporting hundreds of distinct personas; InfoNCE consistency objective causally responsible for persona recoverability.
- **Link**: https://arxiv.org/html/2605.23652

### 2.4 Bounded Autonomy: Controlling LLM Characters in Live Multiplayer Games
- **Authors**: Multiple authors
- **Affiliation**: Academic/Industry
- **Venue**: arXiv preprint (April 2026, revised July 2026)
- **Abstract**: Frames LLM character control as bounded autonomy with three interfaces: agent-agent interaction (probabilistic reply-chain decay), agent-world action execution (embedding-based grounding with fallback), and player-agent steering (whisper soft-steering technique). Deployed in live multiplayer social game with analysis of interaction stability, grounding quality, and whisper intervention success.
- **Key Innovation**: Bounded autonomy architecture for live multiplayer LLM characters; whisper-based soft steering without full override.
- **Link**: https://arxiv.org/html/2604.04703v2

### 2.5 Orchestrated Reality: LLM-Driven World Simulation as Parameterized-Action POMDP
- **Authors**: Yuhang Huang, Chenmiao Li, Chaowei Fang
- **Affiliation**: The University of Tokyo
- **Venue**: arXiv preprint (June 2026)
- **Abstract**: Formalizes LLM-driven game world as a Parameterized-Action POMDP with canonical JSON state tree. Introduces Plan-Diff-Validate-Apply (PDVA) pipeline for schema-validated JSON deltas. Treats the world as canonical object owned by a singleton orchestration agent analogous to tabletop-RPG Game Master. Provides 15 illustrative incidents from real deployment.
- **Key Innovation**: Canonical JSON world state with validated transitions; GM-agent architecture for persistent LLM game worlds.
- **Link**: https://arxiv.org/html/2606.16014

### 2.6 COS-PLAY: Multi-Agent Co-Evolution Framework for Long-Horizon Game Playing
- **Authors**: Multiple authors
- **Affiliation**: Academic
- **Venue**: arXiv preprint (April 2026)
- **Abstract**: Proposes co-evolution framework comprising LLM-based decision agent and skill bank agent for unsupervised skill discovery. Decision agent maintains intention and active skill, retrieves or switches skills as needed. Skill bank agent performs unsupervised skill discovery by segmenting trajectories, learning compact skill contracts. Optimized with GRPO. Built on 8B base model, achieves over 25.1% average gain against four frontier LLM baselines on single-player games.
- **Key Innovation**: Co-evolutionary loop between decision agent and skill bank; unsupervised skill discovery from unlabeled trajectories.
- **Link**: https://arxiv.org/pdf/2604.20987

### 2.7 Sensi: Curriculum-Based Test-Time Learning for LLM Game Agents
- **Authors**: Mohsen Arjmandi
- **Affiliation**: Academic
- **Venue**: arXiv preprint (March 2026)
- **Abstract**: Introduces Sensi for ARC-AGI-3 game-playing challenge with two-player architecture separating perception from action, curriculum-based learning managed by external state machine, and database-as-control-plane. Sensi v1 solves 2 game levels; v2 achieves 50-94x greater sample efficiency than comparable systems (32 vs 1,600-3,000 attempts). Diagnoses failure mode as self-consistent hallucination cascade in perception layer.
- **Key Innovation**: Structured test-time learning with curriculum; SQLite database as programmable context control plane.
- **Link**: https://arxiv.org/pdf/2603.17683

### 2.8 Orak: Foundational Benchmark for Training and Evaluating LLM Game Agents
- **Authors**: Multiple authors (KRAFTON AI)
- **Affiliation**: KRAFTON AI
- **Venue**: arXiv preprint (2025/2026)
- **Abstract**: Benchmark for training and evaluating LLM agents across 12 popular video games spanning all major genres. Uses plug-and-play interface built on Model Context Protocol (MCP). Releases fine-tuning dataset of expert LLM gameplay trajectories covering multiple genres. Offers game leaderboards, LLM battle arenas, and ablation studies of input modality, agentic strategies, and fine-tuning effects.
- **Key Innovation**: MCP-based reproducible evaluation framework; expert trajectory dataset for fine-tuning general LLMs into game agents.
- **Link**: https://arxiv.org/html/2506.03610v3

---

## 3. Game Foundation Models — Generalist Game-Playing Models

### 3.1 NitroGen: Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi Fan
- **Affiliation**: NVIDIA / MineDojo
- **Venue**: CVPR 2026 (pp. 21511-21521)
- **Abstract**: Vision-action foundation model trained on 40,000 hours of gameplay videos across 1,000+ games. Internet-scale dataset constructed by automatically extracting player actions from publicly available gameplay videos via gamepad overlay detection. Multi-game benchmark environment for cross-game generalization. Unified vision-action model trained with large-scale behavior cloning. Transfers effectively to unseen games, achieving up to 52% relative improvement in task success rates over models trained from scratch.
- **Key Innovation**: Internet-scale action-labeled dataset from gamepad overlays; universal simulator wrapper for commercial games via Gymnasium API.
- **Link**: https://arxiv.org/abs/2601.02427

### 3.2 Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents
- **Authors**: Multiple authors (ByteDance/Seed)
- **Affiliation**: ByteDance Seed
- **Venue**: arXiv preprint (October 2025)
- **Abstract**: Generalist game agent trained with unified, scalable action space anchored to human-aligned native keyboard-mouse inputs. Pre-trained on over 500B tokens with diverse trajectories and multimodal data. Key techniques: decaying continual loss to reduce causal confusion, Sparse-Thinking strategy balancing reasoning depth and inference cost. Achieves ~2x success rate over previous SOTA on Minecraft, outperforms GPT-5, Gemini-2.5-Pro, and Claude-4-Sonnet in FPS benchmarks.
- **Key Innovation**: Unified keyboard-mouse action space enabling cross-domain pre-training; decaying continual loss for causal confusion reduction.
- **Link**: https://arxiv.org/html/2510.23691v1

### 3.3 Towards Generalist Game Players: Foundation Models in the Game Multiverse
- **Authors**: Kuan Zhang, Dongchen Liu, Qiyue Zhao, Tianyu Xin, Yue Su, Haisheng Wang, et al.
- **Affiliation**: Tsinghua University (THUSI Lab)
- **Venue**: arXiv preprint (May 2026)
- **Abstract**: Comprehensive review organizing the field around four pillars: Dataset, Model, Harness, and Benchmark. Traces lifecycle from environment-specific RL agents to foundation models as generalist players toward future creator stage. Charts five-level roadmap from single-game mastery to omnipotent generalist agent. Identifies five fundamental trade-offs bounding the system.
- **Key Innovation**: Four-pillar pipeline framework; five-level evolutionary roadmap for generalist game players.
- **Link**: https://arxiv.org/abs/2605.09965

### 3.4 Scaling Behavior Cloning for Real-Time Video Game Playing (Pixels2Play)
- **Authors**: Yuguang Yue, Irakli Salia, Samuel Hunt, Chris Green, Wenzhe Shi, Jonathan J. Hunt
- **Affiliation**: Academic/Industry
- **Venue**: arXiv preprint (January 2026)
- **Abstract**: Open recipe for training video game playing foundation model for real-time inference on consumer GPU. Releases 8,300+ hours of high-quality human gameplay data. Shows scaling laws of behavior cloning — larger models achieve lower test loss and higher causality scores. Systematic study of how causality varies with parameters (up to 1.2B) and training steps. Model plays variety of 3D video games at human-competitive level.
- **Key Innovation**: Scaling laws for behavior cloning causality; real-time 20Hz inference on consumer GPUs.
- **Link**: https://arxiv.org/pdf/2601.04575

### 3.5 Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL
- **Authors**: Multiple authors
- **Affiliation**: Academic
- **Venue**: arXiv preprint (May 2026)
- **Abstract**: Addresses the challenge of scaling VLMs to long-horizon (100+ turn) decision-making in games through reinforcement learning, enabling sustained game play over extended interaction sequences.
- **Key Innovation**: RL-based scaling of VLMs for extended game interaction horizons.
- **Link**: https://arxiv.org/html/2605.00347v1

---

## 4. Procedural Content Generation

### 4.1 AutoUE: Automated 3D Game Generation in Unreal Engine via Multi-Agent Systems
- **Authors**: Multiple authors
- **Affiliation**: Academic
- **Venue**: arXiv preprint (March 2026)
- **Abstract**: Multi-agent system coordinating model retrieval (858K 3D models), scene generation (PCG), gameplay code synthesis, interactive object creation, and automated game testing. RAG mechanism grounds agents with UE tool documentation. Automated play-testing pipeline generates and executes runtime test commands. Constructs game generation dataset and demonstrates end-to-end 3D game generation.
- **Key Innovation**: End-to-end 3D game generation pipeline with automated play-testing; RAG for tool documentation grounding.
- **Link**: https://arxiv.org/abs/2603.07106v1

### 4.2 CreativeGame: Mechanic-Aware Creative Game Generation
- **Authors**: Hongnan Ma, Han Wang, Shenglin Wang, Tieyue Yin, Yiwei Shi, Yucong Huang, et al.
- **Affiliation**: Academic
- **Venue**: arXiv preprint (April 2026)
- **Abstract**: Multi-agent system for iterative HTML5 game generation with CreativeProxyReward (programmatic signals replacing pure LLM judgment), lineage-scoped memory for cross-version experience, runtime validation, and mechanic-guided planning loop. System contains 71 stored lineages, 88 saved nodes, and 774-entry global mechanic archive. Real 4-generation lineage shows mechanic-level innovation emerging in later versions.
- **Key Innovation**: Mechanic-level explicit planning objects; lineage-scoped memory for cross-version experience accumulation.
- **Link**: https://arxiv.org/pdf/2604.19926

### 4.3 Learning Local Constraints for RL Content Generators (WFC + PCGRL)
- **Authors**: Multiple authors
- **Affiliation**: Academic
- **Venue**: arXiv preprint (May 2026)
- **Abstract**: Combines Wave Function Collapse (WFC) local pattern learning with PCGRL for generating visually satisfying and playable puzzle-platform levels. Constrains action space of PCGRL generator with WFC-learned adjacency rules. Tested on Lode Runner levels with varying input sizes, diversity, and starting states. Best generators produce both visually satisfying and playable levels.
- **Key Innovation**: Hybrid WFC-PCGRL framework; constraint-based action space reduction for visual consistency.
- **Link**: https://arxiv.org/html/2605.13570v1

### 4.4 Multiverse: Language-Conditioned Multi-Game Level Blending
- **Authors**: In-Chang Baek, Jiyun Jung, Geum-Hwan Hwang, Sung-Hyun Kim, Kyung-Joong Kim
- **Affiliation**: Academic
- **Venue**: arXiv preprint (March 2026)
- **Abstract**: Language-conditioned multi-game level generator enabling cross-game level blending through textual specifications. Learns shared latent space aligning text and level structures with threshold-based multi-positive contrastive supervision. Supports zero-shot generation from compositional textual prompts and controllable blending via latent interpolation.
- **Key Innovation**: Cross-game contrastive learning for shared representation; text-driven level blending across game domains.
- **Link**: https://arxiv.org/pdf/2603.26782

### 4.5 MORTAR: Evolving Mechanics for Automatic Game Design
- **Authors**: Muhammad U. Nasir, Yuchen Li, Steven James, Julian Togelius
- **Affiliation**: Academic
- **Venue**: GECCO 2026 (July 2026, San Jose, Costa Rica)
- **Abstract**: System for autonomously evolving game mechanics using MAP-Elites quality-diversity algorithm with LLM-driven code-level variation operators. Evaluates mechanics through MCTS constructing complete games. Introduces Constrained Importance Through Search (CITS) score derived from Shapley values. Produces games with coherent structure, varied interaction patterns, and meaningful skill gradients.
- **Key Innovation**: LLM as evolutionary operator for code-level mechanic mutation; Shapley-value-inspired fitness for mechanic contribution.
- **Link**: https://www.raillab.org/publication/nasir-2026-mortar/nasir-2026-mortar.pdf

### 4.6 High Dimensional Procedural Content Generation (HDPCG)
- **Authors**: Multiple authors
- **Affiliation**: Academic
- **Venue**: arXiv preprint (February 2026)
- **Abstract**: Introduces HDPCG framework elevating non-geometric gameplay dimensions to first-class coordinates. Direction-Space augments geometry with discrete layer dimension (4D reachability). Direction-Time augments with temporal dynamics via time-expanded graphs. Three general algorithms with shared pipeline: abstract skeleton generation, controlled grounding, high-dimensional validation, multi-metric evaluation.
- **Key Innovation**: Joint geometry-mechanics state space; temporal dynamics as first-class PCG dimension.
- **Link**: https://arxiv.org/html/2602.18943v1

### 4.7 Forking Garden: Narrative Arc-Conditioned Gameplay Planning
- **Authors**: Multiple authors
- **Affiliation**: Academic
- **Venue**: arXiv preprint (May 2026)
- **Abstract**: Framework for generating branching games from user-provided storylines conditioned on narrative archetypes. Generate-first-constrain-later paradigm: generates diverse node pool then assembles into dungeon graph via arc-guided constraint algorithms. Multimodal alignment of gameplay elements (NPC behavior, difficulty, items, combat). End-to-end interactive system with Unity deployment.
- **Key Innovation**: Narrative arc conditioning for gameplay; generate-first-constrain-later graph assembly.
- **Link**: https://arxiv.org/html/2605.01245v1

---

## 5. Game Benchmarks — Evaluation Suites

### 5.1 BALROG: Benchmarking Agentic LLM and VLM Reasoning On Games
- **Authors**: Davide Paglieri, Bartłomiej Cupiał, Samuel Coward, Ulyana Piterbarg, Maciej Wołczyk, Akbir Khan, et al.
- **Affiliation**: Academic (Multiple institutions)
- **Venue**: ICLR 2025
- **Abstract**: Benchmark aggregating six RL game environments (BabyAI, Crafter, TextWorld, Baba Is AI, MiniHack, NetHack) for testing long-context LLM agentic capabilities. Fine-grained metrics capture task progression. Novel data-informed progression system for NetHack. Finding: multimodal LLMs perform worse with visual input than text-only, suggesting vision-based decision-making is far from solved.
- **Key Innovation**: Unified multi-game benchmark spanning easy to extremely hard; NetHack progression metric.
- **Link**: https://doi.org/10.48550/arxiv.2411.13543

### 5.2 VideoGameBench: Can VLMs Complete Popular Video Games?
- **Authors**: Alex L. Zhang, Thomas L. Griffiths, Karthik R. Narasimhan, Ofir Press
- **Affiliation**: Academic
- **Venue**: arXiv preprint (May 2025)
- **Abstract**: Benchmark of 10 popular 1990s video games requiring real-time VLM interaction with only raw visual inputs. Three games held secret for generalization testing. Best models (Gemini 2.5 Pro, Claude 3.7 Sonnet) complete only 0.48% of VideoGameBench and 1.6% of VideoGameBench Lite (paused inference). Introduces VideoGameBench Lite decoupling reasoning from reaction time.
- **Key Innovation**: Real-time game evaluation without scaffolding; latency-free evaluation variant (Lite).
- **Link**: https://doi.org/10.48550/arxiv.2505.18134

### 5.3 GameVerse: VLM Learning from Video-Based Reflection
- **Authors**: Multiple authors
- **Affiliation**: Academic
- **Venue**: arXiv preprint (March 2026)
- **Abstract**: Comprehensive benchmark spanning 15 globally popular games with reflect-and-retry paradigm. Dual action space for semantic and GUI control. Cognitive hierarchical taxonomy. Experiments show VLMs benefit from video-based reflection, with best results from combining failure trajectories and expert tutorials — a training-free analogue to RL + SFT. Gap between easy games (100% for Gemini-2.5-Pro) and hard games (0%) reveals severe generalization deficit.
- **Key Innovation**: Reflect-and-retry paradigm as training-free proxy for RL + SFT; failure + tutorial combination for policy refinement.
- **Link**: https://arxiv.org/abs/2603.06656v2

### 5.4 MineExplorer: Evaluating Open-World Exploration of MLLM Agents in Minecraft
- **Authors**: Multiple authors
- **Affiliation**: Academic
- **Venue**: arXiv preprint (May 2026)
- **Abstract**: Benchmark for open-world exploration capabilities of MLLM agents in Minecraft, filtering out tasks relying on Minecraft-specific knowledge to reflect general reasoning. Multi-agent synthesis workflow for task graphs, sandbox scenes, and rule-based milestone evaluators. Strong models handle single-hop tasks but degrade sharply on multi-hop tasks requiring hidden prerequisite coordination.
- **Key Innovation**: Filtering domain-specific tasks for general exploration evaluation; multi-agent synthesis for reliable benchmark instances.
- **Link**: https://arxiv.org/html/2605.30931v1

### 5.5 MineNPC-Task: Task Suite for Memory-Aware Minecraft Agents
- **Authors**: Multiple authors
- **Affiliation**: Academic
- **Venue**: arXiv preprint (January 2026)
- **Abstract**: User-authored benchmark with tasks elicited through formative and summative co-play with expert players, normalized into parametric templates with explicit preconditions. Bounded-knowledge policy forbids out-of-world shortcuts. Captures plan, action, and memory events. Initial snapshot: GPT-4o evaluation on 216 subtasks across 8 experienced players.
- **Key Innovation**: Expert co-play task elicitation; bounded-knowledge evaluation policy.
- **Link**: https://arxiv.org/abs/2601.05215v2

---

## 6. Industry Game AI — Real-World Deployment

### 6.1 Controlling LLM Characters in Live Multiplayer Games (Bounded Autonomy)
- **Authors**: Multiple authors
- **Affiliation**: Academic/Industry
- **Venue**: arXiv preprint (April 2026, revised July 2026)
- **Abstract**: Deployed architecture for player-owned LLM characters in live multiplayer game. Every character belongs to online human player; no background NPCs. 40-second behavior heartbeat. Three-tier architecture: game client, game server, stateless AI service. Whisper technique lets players nudge character behavior without full override.
- **Key Innovation**: Production deployment of LLM characters in live multiplayer; whisper-based player steering.
- **Link**: https://arxiv.org/html/2604.04703v2

### 6.2 PCSP UE5 Deployment: Real-Time Persona-Conditioned NPC Control
- **Authors**: Yoosung Hong
- **Affiliation**: Academic/Industry
- **Venue**: arXiv preprint (May 2026)
- **Abstract**: UE5.5 deployment of PCSP as hybrid intent stack: PCSP selects semantic intents, Behavior Tree/Blackboard/EQS/AIController/NavMesh execute them. Exported to ONNX (20-action head, 33-d obs, 64-d persona projection). Scaling sweep {8-128 agents x 3 seeds x 630s} demonstrates sub-frame inference. Hybrid PCSP: 2,077 episodes, 0% failure, 708.9 avg reward. BTOnly: 87.6% failure.
- **Key Innovation**: Commercial game engine integration; ONNX runtime for production deployment at 64+ concurrent agents.
- **Link**: https://arxiv.org/html/2605.23652

### 6.3 MoEC: Memory-Routed Mixture-of-Experts Controller for Minecraft
- **Authors**: Hui Wu, Chao Xu, Jianghui Wang, Ziqiong Liu, Dong Li, Yiwei Dai, Emad Barsoum
- **Affiliation**: Industry/Academic
- **Venue**: ACL 2026 (Long Paper, pp. 22444-22459)
- **Abstract**: Memory-Routed Mixture-of-Experts Controller for adaptive Minecraft control. Routes via subgoal-indexed non-parametric expert memory; regulates capacity through failure-triggered expert growth and redundancy-aware consolidation. Enables continual adaptation without full retraining with bounded inference cost.
- **Key Innovation**: Expert memory routing with failure-triggered growth; redundancy-aware consolidation for continual learning.
- **Link**: https://aclanthology.org/2026.acl-long.1027/

---

## 7. Related Techniques

### 7.1 GLANCE: Curiosity-Driven Exploration for VLM Agents
- **Authors**: Haoxi Li, Qinglin Hou, Jianfei Ma, Jinxiang Lai, Tao Han, Sikai Bai, et al.
- **Affiliation**: Academic
- **Venue**: arXiv preprint (May 2026)
- **Abstract**: Unifies reasoning and exploration by grounding agent's linguistic world model into stable visual representations of evolving target network. Leverages discrepancy between linguistic prediction and visual reality as intrinsic curiosity signal within RL. Curriculum Exploration mechanism periodically re-initializes projector weights to prevent curiosity drain. Achieves overall score 0.86 in sparse-reward settings, outperforming VAGEN-Full.
- **Key Innovation**: Cross-modal curiosity (linguistic prediction vs visual reality); curriculum exploration preventing curiosity drain.
- **Link**: https://arxiv.org/html/2605.03782

### 7.2 HiPER: Hierarchical RL with Explicit Credit Assignment for LLM Agents
- **Authors**: Multiple authors
- **Affiliation**: Academic
- **Venue**: arXiv preprint (February 2026)
- **Abstract**: Hierarchical Plan-Execute RL framework separating high-level planning from low-level execution. Hierarchical Advantage Estimation (HAE) provides coupled learning signals for subgoal selection, switching, and action execution. Proved unbiased estimator with provably reduced variance compared to flat GAE. Explicitly models multi-timescale structure of agent behavior.
- **Key Innovation**: Boundary-aware bootstrapping coupling planning and execution levels; two-time-scale advantage estimation.
- **Link**: https://arxiv.org/html/2602.16165v1

### 7.3 CDE: Curiosity-Driven Exploration for Efficient RL in LLMs
- **Authors**: Multiple authors
- **Affiliation**: Academic
- **Venue**: arXiv preprint (September 2025)
- **Abstract**: Framework leveraging model's intrinsic curiosity via actor perplexity and critic value variance. Multi-head bootstrapped critic provides posterior approximation. Actor curiosity penalizes overconfident errors and promotes diversity. Critic curiosity connects to count-based exploration bonus in linear MDPs. Achieves +3 point improvement on AIME benchmarks over standard GRPO/PPO.
- **Key Innovation**: Dual curiosity signals (actor perplexity + critic variance); theoretical connection to count-based exploration.
- **Link**: https://arxiv.org/html/2509.09675v1

### 7.4 SPEAR: Self-Imitation with Progressive Exploration for Agentic RL
- **Authors**: Multiple authors
- **Affiliation**: Academic
- **Venue**: arXiv preprint (September 2025)
- **Abstract**: Curriculum-based self-imitation learning for agentic LLMs. Skill-level exploration via intrinsic tool-call reward, action-level exploration via progressive SIL amplification. Advantage recalibration for off-policy updates. Covariance-based clipping to curb over-confidence. Dr.BoT strong baseline combines industrial bag-of-tricks. Increases success rates by up to 16.1% on ALFWorld and 20.7% on WebShop.
- **Key Innovation**: Curriculum balancing exploration/exploitation via SIL; covariance-based trajectory-level clipping.
- **Link**: https://arxiv.org/html/2509.22601v2

### 7.5 CIG: Curiosity as Information Gain for Open-Ended Environments
- **Authors**: Multiple authors
- **Affiliation**: Academic
- **Venue**: arXiv preprint (March 2026)
- **Abstract**: Principled formulation grounding artificial curiosity in expected reduction of epistemic uncertainty. Decomposes into Novelty Sensitivity (KL divergence), Learnability Filtering (ensemble disagreement), and Competence-Weighted Priority. Discovers 34% more states than RND and 21% more than ICM within identical compute budgets while avoiding noisy-TV problem.
- **Key Innovation**: Information-theoretic curiosity decomposition; competence-weighted exploration priority.
- **Link**: https://clawrxiv.io/abs/2603.00009

### 7.6 ExToken: Structured Exploration for VLA-RL Fine-tuning
- **Authors**: Multiple authors
- **Affiliation**: Academic
- **Venue**: arXiv preprint (July 2026)
- **Abstract**: Conditions VLA policies on discrete behavioral priors from offline demonstrations for structured exploration. Token-conditioned rollout collection improves trajectory diversity. State-conditioned token selector bridges exploration during training with deterministic inference at deployment. Consistently accelerates convergence and improves performance under constrained interaction budgets.
- **Key Innovation**: Discrete behavioral tokens for structured exploration; state-conditioned selector for deployment alignment.
- **Link**: https://arxiv.org/abs/2607.12931v1

### 7.7 MineEvolve: Self-Evolution with Accumulated Knowledge for Minecraft
- **Authors**: Multiple authors
- **Affiliation**: Academic (USTC)
- **Venue**: arXiv preprint (March 2026, revised)
- **Abstract**: Knowledge-driven self-evolution framework converting execution feedback into actionable behavioral knowledge. Monitor converts subgoal execution into typed feedback; Inducer derives reusable skills and remedies; Curator validates and retrieves; Adaptor repairs unfinished plans. Consistently improves across multiple LM planners on Minecraft MCU long-horizon tasks, with larger gains on high-dependency groups.
- **Key Innovation**: Typed feedback → skill/remedy induction → knowledge-conditioned plan repair pipeline.
- **Link**: https://arxiv.org/html/2603.13131v3

### 7.8 Echo: Experience Transfer for Multimodal LLM Agents in Minecraft
- **Authors**: Chenghao Li, Jun Liu, Songbo Zhang, et al.
- **Affiliation**: Academic (CVPR 2026)
- **Venue**: CVPR 2026
- **Abstract**: Transfer-oriented memory framework decomposing reusable knowledge into five dimensions (structure, attribute, process, function, interaction). Contextual State Descriptor encodes visual, textual, and interactive signals. ICAL module retrieves and adapts past experiences. Achieves 1.3x-1.7x speed-up on object-unlocking tasks. Exhibits burst-like chain-unlocking phenomenon after acquiring transferable experience.
- **Key Innovation**: Five-dimensional knowledge decomposition for transfer; burst-like chain-unlocking phenomenon.
- **Link**: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Experience_Transfer_for_Multimodal_LLM_Agents_in_Minecraft_Game_CVPR_2026_paper.pdf

### 7.9 WISE: Long-Horizon Agent in Minecraft with Why-Which Reasoning
- **Authors**: Changhao Chen
- **Affiliation**: HKUST (Guangzhou)
- **Venue**: arXiv preprint (June 2026)
- **Abstract**: Long-horizon agent framework with Causal Event Graph augmenting episodic memory with explicit causal structure. Opportunistic Task Scheduler dynamically re-prioritizes subtasks when causally relevant opportunities detected. Multi-scale progressive exploration strategy for spatially comprehensive observations. Large improvements on long-horizon sparse tasks requiring adaptive decision-making.
- **Key Innovation**: Causal Event Graph linking observations to task relevance; opportunistic task reordering.
- **Link**: https://www.alphaxiv.org/abs/2606.12852

### 7.10 Psy-CoT + RAPO: Psychology-Grounded Reasoning for Role-Playing Agents
- **Authors**: Multiple authors
- **Affiliation**: Academic
- **Venue**: arXiv preprint (June 2026)
- **Abstract**: Psy-CoT decomposes pre-response reasoning into Interaction Perception, Psychological Empathy, and Logical Construction. RAPO uses profile-token mutual information to weight gradients asymmetrically — amplifying role-specific tokens under positive advantage, attenuating under negative. Outperforms GRPO on CoSER, CharacterBench, and CharacterEval.
- **Key Innovation**: Psychology-grounded CoT for subjective character reasoning; MI-weighted asymmetric gradient signals.
- **Link**: https://arxiv.org/html/2606.27025v1

---

## Key Themes & Trends

1. **Foundation Models for Games**: Major push toward generalist game agents — NitroGen (NVIDIA, CVPR 2026), Game-TARS (ByteDance), Pixels2Play demonstrate internet-scale pre-training enables cross-game transfer. MARL-GPT extends this to multi-agent settings.

2. **Self-Play for Reasoning Transfer**: SPIRAL and STRATAGEM show game self-play develops transferable reasoning in LLMs, not just game-specific heuristics. The field is moving from "win at games" to "learn reasoning from games."

3. **Persona-Scalable NPCs**: PCSP demonstrates a single shared RL policy can support 300+ distinct personas with zero-shot generalization, deployed in UE5 at 64 concurrent agents with sub-frame inference.

4. **Benchmark Arms Race**: BALROG (ICLR 2025), VideoGameBench, GameVerse, MineExplorer, and Orak form a rapidly expanding evaluation ecosystem. VideoGameBench Lite decouples reasoning from reaction time.

5. **LLM Game World Engineering**: Bounded Autonomy (live multiplayer deployment), Orchestrated Reality (GM-agent architecture), and PCSP (UE5 integration) show the field moving from research prototypes to production systems.

6. **Exploration Innovations**: GLANCE (cross-modal curiosity), CDE (actor+critic curiosity), CIG (information-theoretic curiosity), and SPEAR (progressive self-imitation) provide complementary approaches to the exploration-exploitation challenge in game RL.

7. **Hierarchical Approaches Winning**: HiPER, WISE, MineEvolve, and MoEC all demonstrate that explicit hierarchical decomposition (planner/executor, causal reasoning, knowledge induction) outperforms flat policies on long-horizon game tasks.

8. **PCG Maturity**: AutoUE (end-to-end 3D), MORTAR (mechanic evolution), CreativeGame (iterative refinement), HDPCG (dimension expansion), and Multiverse (cross-game blending) show PCG moving beyond level generation to mechanics, narratives, and multi-game domains.
