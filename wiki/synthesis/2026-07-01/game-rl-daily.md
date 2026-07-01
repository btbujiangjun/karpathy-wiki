---
title: "Game RL & Game AI Bot — Daily Survey (2026-07-01)"
type: synthesis
created: 2026-07-01
updated: 2026-07-01
tags: [game-rl, game-ai, foundation-models, pcg, benchmarks, industry, world-models, self-play, marl, nethack, minecraft, starcraft, poker, atari, survey]
sources: [arxiv]
---

# Game RL & Game AI Bot — Daily Survey (2026-07-01)

Covers 7 categories: Game RL, Game AI Bot, Game Foundation Models, Procedural Content Generation, Game Benchmarks, Industry Game AI, and Related Techniques (world models, self-play, IRL, reward shaping).

---

## 1. Game RL — Reinforcement Learning in Games

### Stratagem: Learning Transferable Reasoning via Trajectory-Modulated Game Self-Play
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Apr 2026
- **Link**: https://arxiv.org/abs/2604.17696
- **Abstract**: Proposes **Stratagem** (Self-Play TRajectory AdvaNtage Activated GamE LearMing), which learns transferable reasoning by selectively reinforcing trajectories that exhibit domain-agnostic and adaptive reasoning patterns during self-play. Introduces a Reasoning Transferability Coefficient and Reasoning Evolution Reward to bias reinforcement toward abstract, progressive reasoning.
- **Key innovations**: Self-play + reasoning transfer; trajectory advantage modulation via abstraction level and reasoning depth metrics; transfers to mathematical reasoning tasks.

### Optimistic Policy Regularization (OPR)
- **Authors**: Mai Pham, Vikrant Vaze, Peter Chin
- **Affiliation**: —
- **Venue**: arXiv preprint, Mar 2026
- **Link**: https://arxiv.org/abs/2603.06793
- **Abstract**: Lightweight mechanism that anchors policy optimization to historically successful behavior via a dynamic buffer of high-performing episodes. Uses directional log-ratio reward shaping and auxiliary behavioral cloning objective. Instantiated on PPO, OPR achieves highest score in 22 of 49 Atari games at 10M-step budget.
- **Key innovations**: Mitigates premature convergence / entropy collapse; strong sample efficiency on ALE; generalizes to CAGE Challenge 2 cyber-defense.

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Jun 2025; updated 2026
- **Link**: https://arxiv.org/abs/2506.24119
- **Abstract**: Self-play framework where LLMs learn by playing multi-turn zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation) against continuously improving versions of themselves. Introduces role-conditioned advantage estimation (RAE) for stable multi-agent training. Improves performance by up to 10% across 8 reasoning benchmarks on Qwen and Llama families.
- **Key innovations**: Fully online multi-turn multi-agent RL for LLMs; automatic curriculum via self-play; complementary cognitive patterns from different games transfer to general reasoning.

### Superhuman AI for Generals.io Using Self-Play Reinforcement Learning
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Jun 2026
- **Link**: https://arxiv.org/abs/2606.23348
- **Abstract**: Demonstrates superhuman performance in Generals.io (an RTS game) using pure PPO self-play with sparse win/loss reward. Releases JAX-native simulator reaching tens of millions of FPS on a single GPU. Covers 1v1, 2v2, and free-for-all modes.
- **Key innovations**: First superhuman AI for Generals.io with sparse reward only; lightweight JAX simulator; multi-mode support (zero-sum, team, general-sum).

### MARL-GPT: Foundation Model for Multi-Agent Reinforcement Learning
- **Authors**: (Anonymous)
- **Affiliation**: Cognitive AI Systems
- **Venue**: arXiv preprint, Apr 2026
- **Link**: https://arxiv.org/abs/2604.05943
- **Abstract**: Single GPT-based model trained via offline RL on expert trajectories across StarCraft Multi-Agent Challenge, Google Research Football, and POGEMA (1.5B total transitions). Uses transformer-based observation encoder requiring no task-specific tuning.
- **Key innovations**: First multi-task transformer foundation model for diverse MARL environments; competitive with specialized baselines on all three benchmarks.

### LLM-Guided Graph Neural Coordination Framework for Cooperative MARL
- **Authors**: Kuang, Z., Xu, Z., Wan, L. et al.
- **Affiliation**: —
- **Venue**: Complex & Intelligent Systems, Jun 2026
- **Link**: https://doi.org/10.1007/s40747-026-02356-7
- **Abstract**: Proposes LLM-GNCF which uses an LLM to dynamically construct a Team-Adaptive Coordination Graph based on real-time strategic semantics. Introduces LLM-empowered latent reward shaping with Chain of Aggregation for sparse rewards. Evaluated on StarCraft II micromanagement.
- **Key innovations**: LLM-guided graph coordination; semantic reward shaping; two-stage training paradigm reducing blind exploration.

### Scalable Option Learning (SOL) in High-Throughput Environments
- **Authors**: (Facebook Research)
- **Affiliation**: Facebook Research
- **Venue**: arXiv preprint, Sep 2025
- **Link**: https://arxiv.org/abs/2509.00338
- **Abstract**: Highly scalable hierarchical RL algorithm achieving 25x higher throughput vs. existing hierarchical methods. Trained on NetHack for 30B frames, significantly surpassing flat agents. Also validated on MiniHack and MuJoCo.
- **Key innovations**: Scalable option learning via GPU parallelization; first large-scale hierarchical RL success on NetHack; open-sourced at github.com/facebookresearch/sol.

### Learning Game-Playing Agents with Generative Code Optimization
- **Authors**: Zhiyi Kuang, Ryan Rong, YuCheng Yuan, Allen Nie
- **Affiliation**: Stanford
- **Venue**: arXiv preprint, Aug 2025
- **Link**: https://arxiv.org/abs/2508.19506
- **Abstract**: Represents policies as Python programs refined using LLMs through execution traces and natural language feedback. Applied to Atari (Pong, Breakout, Space Invaders), achieving performance competitive with deep RL baselines while using significantly less training time.
- **Key innovations**: Programmatic policy representation; self-evolving code policies; LLM-based generative optimization.

### Superhuman AI for Stratego Using Self-Play RL and Test-Time Search
- **Authors**: Samuel Sokota, Eugene Vinitsky, Hengyuan Hu, J. Zico Kolter, Gabriele Farina
- **Affiliation**: CMU / MIT
- **Venue**: arXiv preprint, Nov 2025
- **Link**: https://arxiv.org/abs/2511.07312
- **Abstract**: Achieves vastly superhuman performance in Stratego (massive imperfect-information game) with only a few thousand dollars of compute. Develops general approaches for self-play RL and test-time search under imperfect information.
- **Key innovations**: First superhuman Stratego AI; cost reduction from millions to thousands of dollars; novel search methods for massive hidden information.

### Outbidding and Outbluffing Elite Humans: Mastering Liar's Poker via Self-Play and RL
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Nov 2025
- **Link**: https://arxiv.org/abs/2511.03724
- **Abstract**: First published research on training an AI for multiplayer Liar's Poker using R-NaD (regularized Nash dynamics) from DeepNash. Achieves superhuman performance against elite human players.
- **Key innovations**: First Liar's Poker AI; multi-player imperfect-information game solving; R-NaD adaptation for bluffing games.

### AlphaExploitem: Going Beyond Nash Equilibrium in Poker
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, May 2026
- **Link**: https://arxiv.org/abs/2605.09150
- **Abstract**: Extends AlphaHoldem with hierarchical transformer encoder that processes multi-hand histories for opponent exploitation. Trained via PPO with K-best-league self-play. Exploits weak play without losing to NE opponents.
- **Key innovations**: Transformer-based opponent modeling for exploitation; maintains equilibrium robustness while exploiting suboptimal opponents.

### Implicit Strategic Optimization (ISO) for Long-Horizon Adversarial Games
- **Authors**: Boyang Xia, Weiyou Tian, Qingnan Ren et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Feb 2026
- **Link**: https://arxiv.org/abs/2602.08041
- **Abstract**: Prediction-aware framework for LLM agents in long-horizon adversarial games (6-player No-Limit Texas Hold'em, competitive Pokémon). Combines Strategic Reward Model with iso-grpo optimistic learning rule. Proves sublinear contextual regret.
- **Key innovations**: Online context-conditioned policy updating; strategic reward model for long-run value estimation; theoretical regret guarantees.

### StratFormer: Adaptive Opponent Modeling in Imperfect-Information Games
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Apr 2026
- **Link**: https://arxiv.org/abs/2604.25796
- **Abstract**: Transformer-based meta-agent that learns to model and exploit opponents through dual-turn tokens and two-phase curriculum (GTO phase → exploitation phase). Achieves +0.106 BB/hand over GTO on Leduc Hold'em.
- **Key innovations**: Dual-turn tokenization; phased curriculum from equilibrium to exploitation; interpretable opponent representations.

### Revisiting The NetHack Learning Environment
- **Authors**: (ICLR Blog)
- **Affiliation**: ICLR
- **Venue**: ICLR Blogposts 2026
- **Link**: https://iclr-blogposts.github.io/2026/blog/2026/revisiting-the-nle/
- **Abstract**: Identifies constraints on observation/action spaces in NLE that make much of NetHack's complexity inaccessible. Proposes modifications (scout measure, action parameterization changes) that meaningfully improve RL agent performance.
- **Key innovations**: Critical analysis of NLE interface limitations; actionable modifications for the benchmark.

### Unsupervised Hierarchical Skill Discovery (HiSD)
- **Authors**: Damion Harvey, Geraud Nangue Tasse, Benjamin Rosman, Branden Ingram, Steven James
- **Affiliation**: RAIL Lab
- **Venue**: arXiv preprint, 2026
- **Link**: —
- **Abstract**: Segments unlabelled trajectories into skills and induces hierarchical structure via grammar-based approach. Works on pixel-based observations in Craftax and Minecraft without action labels or rewards.
- **Key innovations**: Fully unsupervised skill hierarchy discovery; grammar induction for skill composition; decouples structure discovery from policy execution.

### Think in Games: Learning to Reason in Games via RL with LLMs
- **Authors**: Yi Liao et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, 2025
- **Link**: https://arxiv.org/abs/2508.21365
- **Abstract**: TiG framework reformulates RL-based decision-making as language modeling: LLMs generate language-guided policies refined through online RL based on environmental feedback. Provides step-by-step natural language explanations.
- **Key innovations**: Bridges declarative-procedural knowledge gap; interpretable game-playing policies; lower data/compute demands vs conventional RL.

### ToolPoker: LLMs + GTO Solvers for Professional Poker Play
- **Authors**: Minhua Lin, Enyan Dai, Hui Liu et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Jan 2026
- **Link**: https://arxiv.org/abs/2602.00528
- **Abstract**: Systematic study of LLMs in poker tasks. Identifies heuristics reliance, factual misunderstandings, and knowing-doing gap. Proposes ToolPoker combining external GTO solvers with LLMs for game-theoretic consistent actions.
- **Key innovations**: Tool-integrated reasoning framework for principled game play; behavior cloning + step-level RL improves reasoning style.

### Safe Test-Time RL for Imperfect Information Games
- **Authors**: —
- **Affiliation**: —
- **Venue**: OpenReview, 2026
- **Link**: https://openreview.net/pdf?id=lcOFmkInX2
- **Abstract**: Shows that naive test-time policy-gradient training in imperfect-information games produces exploitable strategies. Extends safe sub-game solving techniques to RL with gadget games.
- **Key innovations**: Identifies test-time training safety issue in games; extends safe sub-game solving to function approximation setting.

### LAMIR: Look-ahead Reasoning with Learned Model in Imperfect Information Games
- **Authors**: Ondřej Kubíček, Viliam Lisý
- **Affiliation**: CTU Prague
- **Venue**: arXiv preprint, Oct 2025
- **Link**: https://arxiv.org/abs/2510.05048
- **Abstract**: Enables look-ahead reasoning in two-player imperfect-information games using a learned abstract model without explicit game rules. Achieves up to 80% win rate against R-NaD in large games.
- **Key innovations**: Learned model for imperfect-information look-ahead; domain-independent abstraction learning; eliminates need for explicit game rules.

---

## 2. Game AI Bot — LLM-Powered Game Agents

### AVA: Attentive VLM Agent for Mastering StarCraft II
- **Authors**: Weiyu Ma, Yuqian Fu, Zecheng Zhang, Bernard Ghanem, Guohao Li
- **Affiliation**: —
- **Venue**: ACL 2026 Findings
- **Link**: https://aclanthology.org/2026.findings-acl.208/
- **Abstract**: Introduces AVACraft — first multimodal benchmark for StarCraft II supporting both MARL and VLMs. Provides RGB visual inputs, NL observations, and structured state. VLMs achieve 75-81% zero-shot win rate without training, while MARL methods reach 27.1% after 1M steps.
- **Key innovations**: Unified VLM+MARL benchmark for StarCraft II; complementary strengths analysis between training-based and zero-shot approaches.

### Sensi: Curriculum-Based Test-Time Learning for LLM Game Agents
- **Authors**: Mohsen Arjmandi
- **Affiliation**: —
- **Venue**: arXiv preprint, Mar 2026
- **Link**: https://arxiv.org/abs/2603.17683
- **Abstract**: LLM agent for ARC-AGI-3 challenge with two-player architecture (perception vs action), curriculum-based learning managed by external state machine, and database-as-control-plane. Achieves 50-94x sample efficiency over comparable systems.
- **Key innovations**: Structured test-time learning with curriculum; database-as-control-plane for steerable context; diagnostic of self-consistent hallucination cascade.

### Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, May 2026
- **Link**: https://arxiv.org/abs/2605.00347
- **Abstract**: Studies RL-based training of VLMs for long-horizon decision-making in Super Mario Land (100+ turns). Proposes adapted PPO with turn-level critic. Achieves 3x average game progress over frontier models. Maintains general-domain capabilities.
- **Key innovations**: Stable RL for long-horizon VLM agents; lightweight turn-level critic outperforms GRPO/Reinforce++; cross-game generalization; open training framework.

### Bounded Autonomy: LLM Characters in Live Multiplayer Games
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Apr 2026
- **Link**: https://arxiv.org/abs/2604.04703
- **Abstract**: Control architecture for LLM characters in multiplayer games with three interfaces: agent-agent, agent-world, player-agent steering. Implements probabilistic reply-chain decay, embedding-based action grounding, and whisper soft-steering.
- **Key innovations**: Bounded autonomy framework for deployable LLM NPCs; whisper technique for player influence without overriding autonomy; deployed in live multiplayer social game.

### Nemobot Games: Strategic AI Gaming Agents with LLMs
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Apr 2026
- **Link**: https://arxiv.org/abs/2604.21896
- **Abstract**: Programming framework operationalizing Shannon's taxonomy with LLMs across four game classes: dictionary-based, rigorously solvable, heuristic-based, learning-based. Modular, inspectable LLM components for reproducible game AI.
- **Key innovations**: LLM + classical game AI taxonomy integration; programmable prompt engineering; crowdsourced strategy refinement.

### HER: Human-like Reasoning and RL for LLM Role-Playing
- **Authors**: Chengyu Du, Xintao Wang, Aili Chen et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Jan 2026
- **Link**: https://arxiv.org/abs/2601.21459
- **Abstract**: Unified framework for cognitive-level persona simulation. Introduces dual-layer thinking (first-person vs third-person). Trains HER models based on Qwen3-32B via SFT+RL. Achieves 30.26% improvement on CoSER benchmark.
- **Key innovations**: Dual-layer thinking for role-play; principle-aligned reward model; reasoning-augmented role-playing data via reverse engineering.

### Improving General Role-Playing Agents via Psychology-Grounded Reasoning (Psy-CoT, RAPO)
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Jun 2026
- **Link**: https://arxiv.org/abs/2606.27025
- **Abstract**: Psy-CoT structures reasoning into Interaction Perception, Psychological Empathy, Logical Construction. RAPO computes per-token profile-task mutual information with asymmetric advantage-conditioned weighting for RL. Outperforms GRPO on CoSER, CharacterBench, CharacterEval.
- **Key innovations**: Psychology-grounded chain-of-thought for role-play; token-level role-specific gradient amplification; addresses role-agnostic token issue in standard RL.

### AdaMARP: Adaptive Multi-Agent Interaction for Immersive Role-Playing
- **Authors**: Zhenhua Xu, Dongsheng Chen, Shuo Wang et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Jan 2026
- **Link**: https://arxiv.org/abs/2601.11007
- **Abstract**: Multi-agent role-playing framework with immersive message format [Thought], (Action), "Speech" and explicit Scene Manager. 8B actor outperforms several commercial LLMs; 14B surpasses Claude Sonnet 4.5 for orchestration.
- **Key innovations**: Adaptive scene management for role-playing; trajectory-level evaluation (AdaptiveBench); multi-character orchestration with on-the-fly character introduction.

---

## 3. Game Foundation Models

### NitroGen: Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu et al. (NVIDIA)
- **Affiliation**: NVIDIA / MineDojo
- **Venue**: CVPR 2026
- **Link**: https://arxiv.org/abs/2601.02427
- **Abstract**: Vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games. Uses automatically extracted player actions from public videos. Up to 52% relative improvement on unseen games after fine-tuning. Dataset, benchmark, and weights released.
- **Key innovations**: Internet-scale video-action dataset; multi-game benchmark for cross-game generalization; pure vision-action mapping (no language conditioning).

### Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents
- **Authors**: Z. Wang, X. Li, Y. Ye et al. (ByteDance)
- **Affiliation**: ByteDance / Seed
- **Venue**: arXiv preprint, Oct 2025
- **Link**: https://arxiv.org/abs/2510.23691
- **Abstract**: Generalist game agent with unified keyboard-mouse action space. Pre-trained on 500B+ tokens. Decaying continual loss reduces causal confusion; Sparse-Thinking balances reasoning depth and cost. ~2x success rate over SOTA on Minecraft; outperforms GPT-5, Gemini-2.5-Pro, Claude-4-Sonnet on FPS.
- **Key innovations**: Human-aligned native keyboard-mouse action space; sparse thinking for efficient reasoning; cross-domain pre-training (OS, web, simulation games).

### Scaling Behavior Cloning Improves Causal Reasoning: Open Model for Real-Time Game Playing
- **Authors**: Yuguang Yue, Irakli Salia, Samuel Hunt, Chris Green, Wenzhe Shi, Jonathan J. Hunt
- **Affiliation**: —
- **Venue**: arXiv preprint, Jan 2026
- **Link**: https://arxiv.org/abs/2601.04575
- **Abstract**: Open recipe for real-time game-playing foundation model on consumer GPU. Releases 8300+ hours gameplay, training/inference code, checkpoints. Systematically studies scaling laws of BC and causality across model sizes up to 1.2B.
- **Key innovations**: Real-time (20 Hz) on consumer GPU (RTX 5090); custom decoder-only transformer with efficient image tokenization; causal reasoning scales with model depth/data.

### Towards Generalist Game Players: Investigation of Foundation Models in Game Multiverse
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, May 2026
- **Link**: https://arxiv.org/abs/2605.09965
- **Abstract**: First systematic investigation of Large Foundation Models as generalist game players through end-to-end lifecycle (Dataset, Model, Harness, Benchmark). Three-era framing: RL Era, LLM Era, Foundation Model Era.
- **Key innovations**: Unified evolutionary formulation of game AI; comprehensive pipeline perspective; identifies key gap in multimodal observation, open-ended goals, universal action interfaces.

### MAIN-VLA: Modeling Abstraction of Intention and Environment for VLA Models
- **Authors**: Zheyuan Zhou, Liang Du, Zixun Sun et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Feb 2026
- **Link**: https://arxiv.org/abs/2602.02212
- **Abstract**: Proposes intention abstraction and environment state abstraction for VLA models in Minecraft and Game for Peace. Uses Foundation Models for automated intention annotation pipeline. Benchmarked against VPT, STEVE-1, ROCKET-1, JARVIS-VLA, OpenHA.
- **Key innovations**: Abstraction layers for improved generalization in VLA; automated latent intention extraction; Chain of Action (CoA) for unified planning-control.

### OpenHA: Open-Source Hierarchical Agentic Models in Minecraft
- **Authors**: (CraftJarvis)
- **Affiliation**: —
- **Venue**: arXiv preprint, Sep 2025
- **Link**: https://arxiv.org/abs/2509.13347
- **Abstract**: Large-scale comparison of action abstractions for VLA/hierarchical models across 800+ Minecraft tasks. Introduces Chain of Action (CoA) unifying high-level planning and low-level control in a single VLA model. All-in-One agent trained on diverse action mixtures achieves SOTA.
- **Key innovations**: Systematic action space comparison; CoA as intermediate reasoning step; All-in-One training across heterogeneous action spaces.

### CrossAgent: Training One Model to Master Cross-Level Agentic Actions via RL
- **Authors**: Kaichen He, Zihao Wang, Muyao Li, Anji Liu, Yitao Liang
- **Affiliation**: —
- **Venue**: arXiv preprint, Dec 2025
- **Link**: https://arxiv.org/abs/2512.09706
- **Abstract**: Unified agentic model mastering heterogeneous action spaces. Uses Multi-Turn GRPO for adaptive action switching. Trained on 30 Minecraft tasks, generalizes to 800+. Outperforms fixed-action baselines.
- **Key innovations**: Cross-level action space mastery; emergent adaptive action selection; multi-turn GRPO for action switching.

### WISE: Long-Horizon Agent in Minecraft with Why-Which Reasoning
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Jun 2026
- **Link**: https://arxiv.org/abs/2606.12852
- **Abstract**: WISE extends episodic memory with Causal Event Graph built by VLM. Opportunistic Task Scheduler reprioritizes based on causal memories. Achieves 30% increase in sequential sparse task success with 26.4% lower completion time vs SOTA.
- **Key innovations**: Causal Event Graph for semantic memory; causally grounded retrieval; multi-scale progressive exploration.

### Experience Transfer for Multimodal LLM Agents in Minecraft
- **Authors**: Chenghao Li, Jun Liu, Songbo Zhang et al.
- **Affiliation**: —
- **Venue**: CVPR 2026
- **Link**: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Experience_Transfer_for_Multimodal_LLM_Agents_in_Minecraft_Game_CVPR_2026_paper.pdf
- **Abstract**: Proposes five explicit transfer dimensions for multimodal memory in Minecraft agents. Integrates with ICAL for effective organization. Achieves superior learning efficiency and task generalization in learning-from-scratch settings.
- **Key innovations**: Structured multimodal memory transfer; explicit transfer dimensions; ICAL-based organization.

### DeepHA: Deep Hierarchical Agent in Minecraft
- **Authors**: (CraftJarvis)
- **Affiliation**: —
- **Venue**: OpenReview, 2026
- **Link**: https://openreview.net/pdf/3bb9029bd760cc0a36c5d89b046fdc45e45e03fc.pdf
- **Abstract**: Hierarchical VLA agent using chain-of-action paradigm. Consistently surpasses generalist models and strongest specialized baselines across 800+ tasks. Achieves 43.2% ASR on long-horizon items.
- **Key innovations**: Deep hierarchical architecture with VLM high-level + learned low-level; outperforms both generalist and specialized models.

---

## 4. Procedural Content Generation

### OpenGame: Open Agentic Coding for Games + GameCoder-27B
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Apr 2026
- **Link**: https://arxiv.org/abs/2604.18394
- **Abstract**: Open-source agentic framework for end-to-end web game creation. Uses GameCoder-27B (Qwen3.5-27B backbone) trained via CPT + SFT + execution-grounded RL. OpenGame-Bench evaluates build health, visual usability, intent alignment.
- **Key innovations**: Domain-specialized code model for game engines; multi-phase agentic workflow with Template/Debug Skills; execution-grounded RL for code generation.

### High Dimensional Procedural Content Generation (HDPCG)
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Feb 2026
- **Link**: https://arxiv.org/abs/2602.18943
- **Abstract**: Formulates PCG as high-dimensional constraint satisfaction over layers, time, locomotion, and other mechanics simultaneously. Uses TEG-A* search with geometric algebra for multi-axis level generation.
- **Key innovations**: Multi-mechanic joint generation; witness-based level validation; extensible beyond geometry to mechanism-rich worlds.

### Forking Garden: Narrative Arc-Conditioned Gameplay Planning
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, May 2026
- **Link**: https://arxiv.org/abs/2605.01245
- **Abstract**: Generates branching game dungeons conditioned on narrative archetypes (Hero's Journey, Three-act structure). Uses arc-guided constraint algorithms on DAG graphs. Each node instantiated as playable Unity level with multimodal alignment.
- **Key innovations**: LLM + narrative archetype integration for PCG; arc-conditioned graph generation; end-to-end interactive system.

### AgentOdyssey: Open-Ended Text Game Generation for Test-Time Continual Learning Agents
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Jun 2026
- **Link**: https://arxiv.org/abs/2606.24893
- **Abstract**: Procedurally generates open-ended text games with rich entities and world dynamics for evaluating test-time continual learning. Includes diagnostic tests for world knowledge, episodic memory, exploration, and action diversity.
- **Key innovations**: LLM-driven game generation engine with verification; multifaceted evaluation beyond game progress; reveals critical limits in agent learning abilities.

### VIPCGRL: Human-Aligned PCGRL via Text-Level-Sketch Shared Representation
- **Authors**: In-Chang Baek, Seoyoung Lee, Sung-Hyun Kim, Geumhwan Hwang, KyungJoong Kim
- **Affiliation**: —
- **Venue**: arXiv preprint, Aug 2025
- **Link**: https://arxiv.org/abs/2508.09860
- **Abstract**: Proposes Vision-Instruction PCGRL with three modalities (text, level, sketches). Uses quadruple contrastive learning across modalities and human-AI styles. Policy aligned via embedding similarity reward.
- **Key innovations**: Multi-modal control for PCG; human-AI style alignment via contrastive learning; human-likeness validated by human evaluation.

### From World-Gen to Quest-Line: Dependency-Driven Prompt Pipeline for Coherent RPG Generation
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Apr 2026
- **Link**: https://arxiv.org/abs/2604.25482
- **Abstract**: Decomposes RPG generation into sequential stages (world building → NPC → PC → campaign → quest) with structured JSON intermediates. No quality degradation at higher complexity.
- **Key innovations**: Dependency-aware prompt pipeline; structured intermediate representations; scalable narrative consistency.

### Procedural Game Level Design with Deep RL
- **Authors**: Murat Özkan
- **Affiliation**: —
- **Venue**: arXiv preprint, Oct 2025
- **Link**: https://arxiv.org/abs/2510.15120
- **Abstract**: Two-agent DRL system in Unity: hummingbird agent learns to collect objects, island agent generates flower layouts. Both trained with PPO via Unity ML-Agents. Emergent behavior from co-adaptation.
- **Key innovations**: Co-adaptive level generation via dual RL agents; DRL for autonomous game level design.

### ChatPCG: LLM-Driven Reward Design for Procedural Content Generation
- **Authors**: In-Chang Baek, Taehee Park, Jin-Ha Noh, Cheong-Mok Bae, Kyung-Joong Kim
- **Affiliation**: —
- **Venue**: AAAI 2024 (AIIDE)
- **Link**: https://arxiv.org/abs/2406.11875
- **Abstract**: LLM-driven framework for automatic reward design in PCGRL. Generates game-specific reward functions using LLM understanding of game mechanics. Integrated with deep RL for multiplayer game content generation.
- **Key innovations**: Automatic reward function generation via LLM; lowers barrier for PCGRL entry.

### MultiGen: Level-Design for Editable Multiplayer Worlds in Diffusion Game Engines
- **Authors**: Ryan Po et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Mar 2026
- **Link**: https://arxiv.org/abs/2603.06679
- **Abstract**: Introduces explicit external memory for diffusion game engines, enabling editable environments and real-time multiplayer rollouts with coherent cross-player interactions. Decomposes generation into Memory, Observation, Dynamics modules.
- **Key innovations**: Editable persistent state for diffusion world models; shared multiplayer inference; modular generation architecture.

### Procedural Content Generation in Games: Survey with LLM Integration
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Oct 2024
- **Link**: https://arxiv.org/abs/2410.15644
- **Abstract**: Comprehensive survey of PCG methods with focus on emerging LLM integration (17 LLM papers found). Covers search-based, pattern-based, ML-based, and LLM-based PCG.
- **Key innovations**: Taxonomy of PCG methods; identifies LLM+RL combined methods as promising future direction.

---

## 5. Game Benchmarks

### OmniGameArena: Unified UE5 Benchmark for VLM Game Agents
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Jun 2026
- **Link**: https://arxiv.org/abs/2606.09826
- **Abstract**: 12 newly built Unreal Engine 5 games spanning Solo (7), PvP (3), and Coop (2). Introduces Improvement Dynamics Curve (IDC) — agentic-reflection harness that autonomously refines skill prompts across rounds. Evaluates 12 VLM agents.
- **Key innovations**: Custom UE5 games (no pretraining leakage); IDC for measuring improvement over reflection rounds; unified action interfaces for cross-agent comparison.

### GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents
- **Authors**: Mingyu Ouyang, Siyuan Hu, Kevin Qinghong Lin et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Apr 2026
- **Link**: https://arxiv.org/abs/2604.07429
- **Abstract**: 34 browser games, 170 tasks across 5 genres. Browser sandbox pauses during inference to decouple latency from decision quality. State-verifiable evaluator over serialized gameAPI state. Evaluates 18 model-interface pairs.
- **Key innovations**: State-verifiable outcome-based evaluation (no perceptual noise); two agent interfaces (CUA and generalist); repeated-evaluation robustness studies.

### GameDevBench: Evaluating Agentic Capabilities Through Game Development
- **Authors**: Wayne Chi, Yixiong Fang et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Feb 2026
- **Link**: https://arxiv.org/abs/2602.11103
- **Abstract**: First benchmark for evaluating agents on game development tasks (132 tasks from web/video tutorials). Best agent solves only 54.5%. Image/video-based feedback mechanisms improve performance (Claude 33.3% → 47.7%).
- **Key innovations**: Multimodal game development testbed; strong correlation between perceived difficulty and multimodal complexity; vision-based feedback for agent improvement.

### GameCraft-Bench: Can Agents Build Playable Games End-to-End?
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Jun 2026
- **Link**: https://arxiv.org/abs/2606.17861
- **Abstract**: Benchmark of 140 game-building tasks. Strongest agent achieves only 41.4%. Analysis shows agents implement recognizable mechanics but struggle with complete, coherent games.
- **Key innovations**: End-to-end game generation evaluation; rubric-based scoring (Core Mechanics, Content Depth, Functional Visuals, Art & Presentation); headless browser + VLM judging.

### GameVerse: Can VLMs Learn from Video-based Reflection?
- **Authors**: Kuan Zhang, Dongchen Liu, Qiyue Zhao et al.
- **Affiliation**: THUSI Lab
- **Venue**: arXiv preprint, Mar 2026
- **Link**: https://arxiv.org/abs/2603.06656
- **Abstract**: Reflect-and-retry paradigm for VLMs across 15 games. Best results from combining failure trajectories and expert tutorials — training-free analogue to RL + SFT. Cognitive hierarchical taxonomy introduced.
- **Key innovations**: Video-based reflection as training-free RL analogue; cognitive taxonomy for systematic evaluation; dual action space (semantic + GUI).

### AI Gamestore: Scalable, Open-Ended Evaluation of Machine General Intelligence
- **Authors**: Lance Ying, Ryan Truong, Prafull Sharma et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Feb 2026
- **Link**: https://arxiv.org/abs/2602.17594
- **Abstract**: Platform using LLMs + humans-in-the-loop to synthesize games from Apple App Store and Steam top charts. Generated 100 games; best VLMs achieve <10% of human average on most games. Struggles with world-model learning, memory, planning.
- **Key innovations**: "Multiverse of Human Games" evaluation; procedural generation of human-designed game adaptations; reveals large gap between VLMs and human gameplay ability.

### Agentick: Unified Benchmark for General Sequential Decision-Making Agents
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, May 2026
- **Link**: https://arxiv.org/abs/2605.06869
- **Abstract**: 37 procedurally generated tasks across 6 capability categories, 4 task formats, 5 observation modalities. Gymnasium-native, multi-modal observations, per-category diagnostic scoring.
- **Key innovations**: Unified benchmark for both RL and LLM agents; Gymnasium-native interface; supports RL warm-start and RL training for decision-making skills.

### Beyond the Current Observation: Evaluating MLLMs in Controllable Non-Markov Games
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Jun 2026
- **Link**: https://arxiv.org/abs/2606.19338
- **Abstract**: Controllable Non-Markov game benchmark (2D card + 3D maze) requiring memory of past observations. Tests up to 128 context length and 350 images. Isolates memory failures from planning/formatting errors.
- **Key innovations**: Non-Markov game design for memory evaluation; large context/multi-image testing; isolates memory-specific failures.

### PokeGym: Visually-Driven Long-Horizon Benchmark for VLMs
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Apr 2026
- **Link**: https://arxiv.org/abs/2604.08340
- **Abstract**: 30 tasks in Pokémon Legends: Z-A (3D open-world RPG), 30-220 steps. Code-level isolation — agents operate on raw RGB only, evaluator verifies via memory scanning. Reveals physical deadlock recovery as primary bottleneck.
- **Key innovations**: Pure vision-based decision-making in AAA game; automated scalable assessment via memory scanning; identifies Aware vs Unaware Deadlock metacognitive divergence.

---

## 6. Industry Game AI

### AstraGame: VLM Agent Serving for Large-Scale Game Testing (WeChat/Tencent)
- **Authors**: Yuzhe Guo (Peking University), Haochuan Lu (Tencent), Mengzhou Wu et al.
- **Affiliation**: Tencent / Peking University / UT Dallas
- **Venue**: FSE 2026 Industry Papers
- **Link**: https://conf.researchr.org/details/fse-2026/fse-2026-industry-papers/50/
- **Abstract**: Decoupled architecture with UIBrain (parallelized perception/reasoning), UIBase (widget-level semantic caching), UIFormer (token-efficient action protocols). 37.78% improvement in exploration coverage. Deployed on 24,000 mini-games; 58% latency reduction; 180,000+ issues identified.
- **Key innovations**: Large-scale VLM game testing deployment; semantic caching transforms repeated inference into lookup; decoupled small-large model collaboration.

### Augmenting Game AI with Deep RL: Production Deployment
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Jun 2026
- **Link**: https://arxiv.org/abs/2606.20210
- **Abstract**: Practical considerations for RL deployment in AAA games: runtime inference constraints, modularity, efficient networks, fast retraining cycles. Advocates asymmetric actor-critic with small actor for real-time inference.
- **Key innovations**: Production-oriented RL design patterns; analysis of compute budgets shared with non-RL systems; importance of fast training turnaround for game dev cycles.

### Generative AI for Dynamic NPC Behavior and PCG: Industry Survey
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: IJETCSIT, May 2026
- **Link**: https://ijetcsit.org/index.php/ijetcsit/article/view/743
- **Abstract**: Comprehensive technical examination of LLM, diffusion, and RL deployment in commercial games. Analyzes Fortnite AI NPC, GTA VI dialogue decay, Ubisoft NEO NPC, NVIDIA ACE, Inworld AI. Reports 25-40% dev time reduction, 20% cost savings, 40% player satisfaction improvement.
- **Key innovations**: Industry-wide survey; production benchmarks and metrics; ethical implications (SAG-AFTRA, emergent behavior containment).

### How KRAFTON Built PUBG Ally — Co-Playable Character Powered by NVIDIA ACE
- **Authors**: KRAFTON / NVIDIA
- **Affiliation**: KRAFTON / NVIDIA
- **Venue**: GameDev.net, Jun 2026
- **Link**: https://gamedev.net/news/how-krafton-built-pubg-ally-a-co-playable-character-powered-by-nvidia-ace-r4114/
- **Abstract**: PUBG Ally is a co-playable character using on-device ASR, 2B SLM (Mistral-NeMo-Minitron, quantized to 8GB VRAM), and TTS via NVIDIA ACE. Behavior-tree layer handles fast combat reactions. Cloud LLMs deemed too slow; kept everything local.
- **Key innovations**: On-device deployment with strict latency constraints; model is trusted only for intent/coordination/speech, not game facts; aggressive problem constraint (1 map, 1 mode, fixed item taxonomy).

### Orchestrated Reality: LLM-Driven Game Worlds
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Jun 2026
- **Link**: https://arxiv.org/abs/2606.16014
- **Abstract**: Formalizes LLM-driven game worlds as Parameterized-Action POMDP. World is a canonical JSON object owned by a singleton orchestration agent (analogous to tabletop RPG Game Master). PDVA pipeline (Plan-Diff-Validate-Apply) for schema-validated state changes.
- **Key innovations**: Formal model for LLM game engines; auditable JSON state; multi-NPC Markov games and RL environment as future work.

---

## 7. Related Techniques — World Models, Model-Based RL, Curiosity, IRL, Reward Shaping

### Curiosity-Critic: Cumulative Prediction Error Improvement as Intrinsic Reward
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Apr 2026
- **Link**: https://arxiv.org/abs/2604.18701
- **Abstract**: Grounds intrinsic reward in improvement of cumulative prediction error across all visited transitions. Learns asymptotic error baseline via co-trained critic. Higher reward for learnable transitions, collapses for stochastic ones — separates epistemic from aleatoric uncertainty.
- **Key innovations**: Tractable per-step surrogate for cumulative prediction error; online separation of reducible/irreducible error; outperforms prediction-error, RND, and count-based methods.

### Mind-Studio: Executable World Models with Lookahead Evaluation
- **Authors**: Yifei Dong, Mingen Zheng, Linquan Wu, Jeff Z. Pan, Jiaxin Bai
- **Affiliation**: —
- **Venue**: arXiv preprint, Jun 2026
- **Link**: https://arxiv.org/abs/2606.16070
- **Abstract**: Synthesizes executable pygame-style world models from state-action-next-state trajectories using LLMs. K-step lookahead fidelity protocol compares WM rollouts against real environment. On Montezuma's Revenge, improves chosen-action NSP from 0.3% to 48.7%.
- **Key innovations**: Fully executable programmatic world models; object-centric program representation; verifiable via rollback comparison.

### Distilling Game Code World Model Generation into Lightweight LLMs
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, May 2026
- **Link**: https://arxiv.org/abs/2605.24375
- **Abstract**: Investigates distilling GameCWM generation into smaller models. Curated 30-game dataset + verification framework. Pipeline: SFT + RLVR on Qwen2.5-3B-Instruct. RLVR improves execution-level rule adherence.
- **Key innovations**: Distillation of game environment generation; RLVR with execution-based verification; reduces reliance on frontier models.

### ObjectZero: Object-Centric World Models Meet MCTS
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Jan 2026
- **Link**: https://arxiv.org/abs/2601.06604
- **Abstract**: MBRL algorithm using GNNs over object-centric representations with pretrained SLATE/DINOSAUR encoder. Integrated with MCTS planning. Outperforms existing object-centric approaches in interactive object-rich settings.
- **Key innovations**: Object-centric representations for MCTS-based MBRL; structured dynamics models via GNN; object interaction reasoning.

### What Do World Models Learn in RL? Probing Latent Representations
- **Authors**: Xinyu Zhang
- **Affiliation**: —
- **Venue**: arXiv preprint, Mar 2026
- **Link**: https://arxiv.org/abs/2603.21546
- **Abstract**: Applies linear/nonlinear probing, causal interventions, attention analysis to IRIS (discrete token transformer) and DIAMOND (continuous diffusion UNet) world models on Atari. Finds approximately linear game state representations and spatial attention specialization.
- **Key innovations**: Interpretability of world models; approximately linear representations of game state; causal interventions confirm functional use of representations.

### Reinforcement World Model Learning (RWML) for LLM-based Agents
- **Authors**: Xiao Yu, Baolin Peng, Ruize Xu et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Feb 2026
- **Link**: https://arxiv.org/abs/2602.05842
- **Abstract**: Self-supervised method learning action-conditioned world models for LLM-based agents. Aligns simulated next states with realized states in pretrained embedding space. Outperforms direct task-success RL by 6.9 points on ALFWorld and 5.7 on τ2 Bench.
- **Key innovations**: Sim-to-real gap rewards for world model learning; more robust than token prediction or LLM-as-judge; matches expert-data training performance.

### ProPlay: Procedural World Models for Self-Evolving LLM Agents
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Jun 2026
- **Link**: https://arxiv.org/abs/2606.12780
- **Abstract**: Represents environment knowledge as procedure graph with induced procedures and reliability embeddings. Preplay mechanism constructs task-specific procedural trajectories. Graph refined via environment feedback after execution.
- **Key innovations**: Procedure-level world model (not action-level); episodic preplay for soft guidance; self-evolution from environment feedback.

### GLoW: Dual-Scale World Models for LLM Agents in Hard-Exploration Problems
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Sep 2025
- **Link**: https://arxiv.org/abs/2509.24116
- **Abstract**: Dual-scale world models maintaining trajectory frontier at global scale while learning from local trial-and-error via Multi-path Advantage Reflection. SOTA for LLM-based approaches on Jericho benchmark; 100-800x fewer interactions than RL methods.
- **Key innovations**: Global trajectory frontier + local advantage-based exploration; bridges LLM agents and RL sample efficiency.

### ActWorld: Interactive World Model via Action-Aware Memory
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Jun 2026
- **Link**: https://arxiv.org/abs/2606.17730
- **Abstract**: Extends navigation-centric video generators to support mid-rollout object interaction. Identifies navigation-interaction gap as memory-design issue. Achieves real-time keyboard-mouse control with object interaction.
- **Key innovations**: Action-aware memory design for interactive world models; object-level interaction beyond viewpoint control; real-time generation.

### WorldCompass: RL for Long-Horizon World Models
- **Authors**: Zehan Wang, Tengfei Wang, Haiyu Zhang et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Feb 2026
- **Link**: https://arxiv.org/abs/2602.09022
- **Abstract**: RL post-training framework for interactive video-based world models. Introduces clip-level rollout, complementary rewards (interaction accuracy + visual quality), negative-aware fine-tuning. Significantly improves WorldPlay interaction accuracy.
- **Key innovations**: RL-as-post-training for world models; clip-level rollout for autoregressive video generation; complementary reward design suppresses reward hacking.

### Matrix-Game 3.0: Real-Time Streaming Interactive World Model
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Apr 2026
- **Link**: https://arxiv.org/abs/2604.08995
- **Abstract**: Memory-augmented interactive world model for 720p real-time generation. Industrial-scale data engine (UE synthetic + AAA game collection + real video). Multi-segment DMD distillation achieves 40 FPS at 720p with 5B model.
- **Key innovations**: Real-time high-res world model; camera-aware memory retrieval; minute-long temporal consistency; distribution matching distillation for streaming inference.

### Decoding Rewards in Competitive Games: Inverse Game Theory with Entropy Regularization
- **Authors**: Junyi Liao, Zihan Zhu, Ethan Fang, Zhuoran Yang, Vahid Tarokh
- **Affiliation**: —
- **Venue**: arXiv preprint, Jan 2026
- **Link**: https://arxiv.org/abs/2601.12707
- **Abstract**: Unified framework for reward recovery in two-player zero-sum matrix/Markov games with entropy regularization. Establishes identifiability via quantal response equilibrium. MLE-based algorithm with theoretical guarantees.
- **Key innovations**: Reward identifiability in competitive games; QRE-based IRL; sample efficiency guarantees.

### Trust Region IRL (TRIRL)
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, May 2026
- **Link**: https://arxiv.org/abs/2605.11020
- **Abstract**: Non-adversarial IRL with monotonic improvement guarantee. Trust-region-optimal policy for reward update can be globally optimal for smaller update in same direction. Avoids training instabilities of adversarial IRL. 2.4x improvement over SOTA imitation learning.
- **Key innovations**: Monotonic dual improvement without full RL solve per iteration; recovered reward generalizes to dynamics shifts; bridges classical and adversarial IRL.

### Confounding Robust Continuous Control via Automatic Reward Shaping
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Feb 2026
- **Link**: https://arxiv.org/abs/2602.10305
- **Abstract**: Learns reward shaping function from potentially confounded offline datasets using causal Bellman equation. Uses learned upper bound on optimal state values as PBRS potentials. Tested with SAC on continuous control.
- **Key innovations**: Causal approach to automatic reward shaping; robustness to unobserved confounders; principled PBRS potential design.

### LLM Guided Incentive Aware Reward Design for Cooperative MARL
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Mar 2026
- **Link**: https://arxiv.org/abs/2603.24324
- **Abstract**: LLM generates candidate shaping programs from environment instrumentation, constrained by formal validity envelope. MAPPO trains policies; selection based on sparse task return. Improves coordination in Overcooked layouts.
- **Key innovations**: Objective-grounded reward search; LLM + formal validity constraints; automatic coordination incentive discovery.

### DIML: Differentiable Inverse Mechanism Learning
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Jan 2026
- **Link**: https://arxiv.org/abs/2601.17678
- **Abstract**: Recovers unknown incentive-generating mechanisms from observed strategic interaction traces. Differentiates through model of multi-agent learning dynamics. Identifiability under conditional logit response.
- **Key innovations**: Inverse mechanism learning (beyond IRL); differentiable learning dynamics; counterfactual auditing.

### GRACE: LLM Framework for Explainable IRL
- **Authors**: Silvia Sapora, Devon Hjelm, Alexander Toshev, Omar Attia, Bogdan Mazoure
- **Affiliation**: —
- **Venue**: arXiv preprint, Oct 2025
- **Link**: https://arxiv.org/abs/2510.02180
- **Abstract**: LLMs within evolutionary search to reverse-engineer interpretable, code-based reward functions from expert trajectories. Validated on BabyAI and AndroidWorld. LLM's strong priors provide sample efficiency vs GAIL.
- **Key innovations**: Interpretable code-based reward functions; evolutionary search + LLM priors; reward shaping capabilities for long-horizon tasks.

### rePIRL: Learn PRM with Inverse RL for LLM Reasoning
- **Authors**: (Anonymous)
- **Affiliation**: —
- **Venue**: arXiv preprint, Feb 2026
- **Link**: https://arxiv.org/abs/2602.07832
- **Abstract**: IRL-inspired framework learning process reward models for LLM reasoning from expert trajectories only. Models multi-step LLM reasoning as token-level MDP. Unifies online and offline PRM learning.
- **Key innovations**: IRL for process reward model learning; token-level MDP for reasoning; unifies existing PRM methods theoretically.

### Learning Reasoning Reward Models from Expert Demonstration via IRL
- **Authors**: Claudio Fanconi, Nicolás Astorga, Mihaela van der Schaar
- **Affiliation**: —
- **Venue**: arXiv preprint, Oct 2025
- **Link**: https://arxiv.org/abs/2510.01857
- **Abstract**: Adversarial IRL approach learning dense token-wise reward from expert reasoning traces. Used both as training signal and inference-time reranker. Token-level diagnostics expose where traces deviate from good reasoning.
- **Key innovations**: Token-level reasoning reward; dual use (training signal + reranker); interpretable diagnostics.

---

## Summary

This survey covers ~80 papers across 7 categories:

| Category | Count | Key Trends |
|----------|-------|------------|
| Game RL | 19 | Self-play + general reasoning transfer; MARL foundation models; scalable hierarchical RL for NetHack; LLM+game reasoning |
| Game AI Bot | 9 | VLM+RL for long-horizon gameplay; LLM NPCs with bounded autonomy; psychology-grounded role-playing |
| Game Foundation Models | 10 | Internet-scale pretraining (NitroGen, Game-TARS); unified keyboard-mouse action spaces; hierarchical VLA models |
| PCG | 10 | LLM+PCG pipelines; game-generating agents; narrative-arc conditioned generation; diffusion engine levels |
| Game Benchmarks | 9 | Custom UE5 benchmarks; state-verifiable evaluation; non-Markov games for memory testing; game development task benchmarks |
| Industry Game AI | 5 | Production VLM deployment at Tencent; on-device deployment (PUBG Ally/KRAFTON); industry survey with 36% studio adoption |
| Related Techniques | 19 | Curiosity with uncertainty separation; executable world models; IRL for LLM reasoning; RL post-training for world models |

**Cross-cutting themes**: (1) Convergence of VLMs and RL for game agents, (2) Self-play as general reasoning training, (3) Foundation models replacing task-specific policies, (4) Industrial deployment at scale with latency constraints, (5) PCG evolving from heuristic to LLM-driven pipelines.
