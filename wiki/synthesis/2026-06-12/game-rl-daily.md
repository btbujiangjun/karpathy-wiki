---
title: "Game RL & Game AI Bot — Daily Synthesis (2026-06-12)"
type: synthesis
created: 2026-06-12
updated: 2026-06-12
sources: []
tags: [game-rl, game-ai, reinforcement-learning, llm-agents, foundation-models, procedural-content-generation, benchmarks, self-play, world-models, industry-game-ai]
---

# Game RL & Game AI Bot — Daily Synthesis

> Survey of recent arXiv papers and proceedings on Game RL, Game AI Bots, Game Foundation Models, Procedural Content Generation, Game Benchmarks, Industry Game AI, and related techniques. Compiled 2026-06-12.

---

## 1. Game Reinforcement Learning

### Resource-Efficient Model-Free Reinforcement Learning for Board Games
- **Authors**: Kazuki Ota, Takayuki Osa, Motoki Omura, Tatsuya Harada
- **Affiliation**: University of Tokyo / RIKEN
- **Venue**: arXiv 2602.10894 (Feb 2026)
- **Abstract**: Proposes a model-free RL algorithm for board games designed to achieve more efficient learning than search-based methods like AlphaZero. Validated on 5 board games: Animal Shogi, Gardner Chess, Go, Hex, and Othello. Ablation study shows importance of core techniques. Demonstrates model-free RL can compete in domains traditionally dominated by search-based methods.
- **Key Innovation**: Model-free RL matching AlphaZero-style performance at lower compute cost
- **Link**: https://arxiv.org/abs/2602.10894

### PokeRL: Reinforcement Learning for Pokémon Red
- **Authors**: Dheeraj Reddy, et al.
- **Affiliation**: —
- **Venue**: arXiv 2604.10812 (Apr 2026)
- **Abstract**: Modular system training deep RL agents for early-game tasks in Pokémon Red (exiting house, exploring Pallet Town, winning first rival battle). Contributions: loop-aware PyBoy wrapper with map masking, multi-layer anti-loop/anti-spam mechanism, dense hierarchical reward design. Positioned as intermediate step between toy benchmarks and full "Pokémon League champion" agents.
- **Key Innovation**: Explicit modeling of failure modes (action loops, menu spam) in long-horizon RPG RL
- **Link**: https://arxiv.org/abs/2604.10812

### Learning to Play Blackjack: A Curriculum Learning Perspective
- **Authors**: Amirreza Alasti, Efe Erdal, Yücel Celik, Theresa Eimer
- **Affiliation**: —
- **Venue**: arXiv 2604.00076 (Mar 2026)
- **Abstract**: Novel framework using LLM to dynamically generate a curriculum over available actions for Tabular Q-Learning and DQN agents in Blackjack. LLM creates multi-stage training path progressively introducing complex actions. Results: DQN win rate 43.97% → 47.41%, bust rate 32.9% → 28.0%, training accelerated by 74%.
- **Key Innovation**: LLM-guided curricula for RL agents in card games
- **Link**: https://arxiv.org/abs/2604.00076

### MAGIC: Multi-Step Advantage-Gated Causal Influence for MARL
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2605.01805 (May 2026)
- **Abstract**: MARL framework estimating multi-step action effects between agents using counterfactual interventions. Uses advantage gate to direct exploration toward beneficial behaviors. Outperforms prior methods on MPE (26.9% improvement) and SMAC/SMACv2 (10.1% improvement).
- **Key Innovation**: Counterfactual interventional causality for multi-agent coordination
- **Link**: https://arxiv.org/abs/2605.01805

### MRVF: Multi-Round Value Factorization for MARL
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2604.05297 (Apr 2026)
- **Abstract**: Introduces theoretical tool for studying convergence of greedy action under value factorization. Proposes MRVF with forward and backward multi-round factorization to ensure training stability. Outperforms QMIX and other value factorization methods on non-monotonic games, predator-prey, and SMAC scenarios.
- **Key Innovation**: Theoretical convergence guarantees for value factorization in MARL
- **Link**: https://arxiv.org/abs/2604.05297

### SMAC-HARD: Enabling Mixed Opponent Strategy Script and Self-play on SMAC
- **Authors**: Devin Deng, et al.
- **Affiliation**: —
- **Venue**: arXiv 2412.17707 (Dec 2024)
- **Abstract**: Highlights that default opponent policy in SMAC lacks diversity, causing MARL algorithms to overfit. Proposes SMAC-HARD benchmark with customizable opponent strategies, randomized adversarial policies, and self-play interfaces. Black-box testing reveals difficulty of transferring learned policies to unseen adversaries.
- **Key Innovation**: Mixed-strategy opponent benchmark addressing SMAC's diversity gap
- **Link**: https://arxiv.org/abs/2412.17707

### StarCraft+ (SC2BA): Benchmarking Multi-agent Algorithms in StarCraft II Battle Arena
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2512.16444 (Dec 2025)
- **Abstract**: Establishes algorithm-vs-algorithm environment (SC2BA) for refreshing MARL benchmarking in adversarial paradigm. Features dual-algorithm paired adversary and multi-algorithm mixed adversary modes. Includes APyMARL library. Benchmarks classic MARL algorithms across two adversarial modes.
- **Key Innovation**: Adversarial algorithm-vs-algorithm benchmark for StarCraft II
- **Link**: https://arxiv.org/abs/2512.16444

### HLSMAC: High-Level Strategic Decision-Making for StarCraft Multi-Agent Challenge
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2509.12927 (Sep 2025)
- **Abstract**: New cooperative MARL benchmark with 12 StarCraft II scenarios based on Thirty-Six Stratagems. Challenges agents with tactical maneuvering, timing coordination, and deception. Proposes metrics beyond win rate: ability utilization and advancement efficiency. Integrates SOTA MARL and LLM-based agents.
- **Key Innovation**: Chinese stratagem-inspired StarCraft benchmark for high-level strategic MARL
- **Link**: https://arxiv.org/abs/2509.12927

### SEMA: Self-Evolving Multi-Agent Framework for RTS Decision Making
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2603.23875 (Mar 2026)
- **Abstract**: LLM-based framework for Real-Time Strategy decision-making addressing speed-quality trade-off. Features dynamic observation pruning via structural entropy, hybrid knowledge-memory mechanism (micro-trajectories, macro-experience, hierarchical domain knowledge). Superior win rates on StarCraft II maps with >50% latency reduction.
- **Key Innovation**: Structural entropy-based pruning + hybrid memory for LLM RTS agents
- **Link**: https://arxiv.org/abs/2603.23875

### π-Play: Multi-Agent Self-Play via Privileged Self-Distillation
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2604.14054 (Apr 2026)
- **Abstract**: Observes self-play naturally produces question construction paths (QCPs) — intermediate artifacts capturing reverse solution process. Proposes π-Play where examiner generates tasks + QCPs, teacher uses QCP as privileged context to densely supervise student. 2-3× efficiency over conventional self-play for search agents.
- **Key Innovation**: Privileged self-distillation from self-play's intermediate artifacts
- **Link**: https://arxiv.org/abs/2604.14054

---

## 2. Game AI Bots

### STRATAGEM: Learning Transferable Reasoning via Trajectory-Modulated Game Self-Play
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2604.17696 (Apr 2026)
- **Abstract**: Self-play framework for LLMs using trajectory-modulated game training that transfers to mathematical reasoning. Against Qwen3-4B-Base + SPIRAL baselines: 8/9 benchmarks improved. AIME24: 2× improvement (10% → 20%), AMC-23: +10pp. General reasoning (HumanEval pass@1): +10pp over baseline.
- **Key Innovation**: Game self-play that transfers to mathematical reasoning tasks
- **Link**: https://arxiv.org/abs/2604.17696

### APEX: Autonomous Policy Exploration for Self-Evolving LLM Agents
- **Authors**: Liu, et al.
- **Affiliation**: —
- **Venue**: arXiv 2605.21240 (May 2026)
- **Abstract**: Addresses exploration collapse in self-evolving agents: as memory grows, behavior concentrates around familiar routines. Proposes strategy map — DAG of milestones with prerequisite edges. Fork Discovery expands map, Policy Selection balances exploration/exploitation. Outperforms baselines on 9 Jericho text-adventure games and WebArena.
- **Key Innovation**: DAG-based strategy maps to prevent exploration collapse in LLM agents
- **Link**: https://arxiv.org/abs/2605.21240

### FAMOU: Beyond Static Evaluation — Co-Evolutionary Mechanisms for LLM-Driven Strategy Evolution
- **Authors**: Li, et al.
- **Affiliation**: —
- **Venue**: arXiv 2606.10389 (Jun 2026)
- **Abstract**: Extends LLM-driven code evolution to adversarial multi-agent games. Three mechanisms: evaluator co-evolution, hierarchical deep evaluation, weakness pressure. On MCTF 2026 3v3 maritime capture-the-flag: highest combined score (0.526), best generalization (61.7% win rate vs unseen). LLM mutation generates novel tactics (lookahead search, adaptive interception). 1st in AAMAS 2026 MCTF hardware round-robin.
- **Key Innovation**: Co-evolving evaluation alongside strategies for LLM code evolution in games
- **Link**: https://arxiv.org/abs/2606.10389

### MEMO: Memory-augmented Model Context Optimization for Self-Play
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2603.09022 (Mar 2026)
- **Abstract**: Weight-free self-play framework for multi-agent LLM games coupling retention (persistent memory bank distilling trajectories) with exploration (tournament-style prompt evolution + prioritized replay). Raises mean win rates across 5 text-based games, uses 19× fewer games than RL baselines, reduces outcome dispersion. Contexts transfer across games and model families.
- **Key Innovation**: Memory-augmented context optimization without weight updates
- **Link**: https://arxiv.org/abs/2603.09022

### Bounded Autonomy: Controlling LLM Characters in Live Multiplayer Games
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2604.04703 (Apr 2026)
- **Abstract**: Frames bounded autonomy as control architecture for LLM characters in live multiplayer games. Three interfaces: agent-agent interaction (probabilistic reply-chain decay), agent-world execution (embedding-based action grounding with fallback), player-agent steering (whisper — soft-steering technique). Deployed in live multiplayer social game with evaluation of interaction stability, grounding quality.
- **Key Innovation**: Practical control architecture balancing LLM autonomy with player steerability
- **Link**: https://arxiv.org/abs/2604.04703

### PTCG-Bench: Can LLM Agents Master Pokémon Trading Card Game?
- **Authors**: —
- **Affiliation**: ZJU (Zhejiang University)
- **Venue**: arXiv 2605.29653 (May 2026)
- **Abstract**: Benchmark evaluating LLM agents in Pokémon TCG along decision-making under imperfect info, self-evolution through cross-game experience, and modular harness ablation. Shows LLMs achieve non-trivial gameplay but sustained self-evolution remains challenging; performance sensitive to harness design.
- **Key Innovation**: Pokémon TCG as benchmark for self-evolving LLM agents with imperfect information
- **Link**: https://arxiv.org/abs/2605.29653

### Competition and Cooperation of LLM Agents in Games
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2604.00487 (Apr 2026)
- **Abstract**: Studies LLM agent interactions in network resource allocation and Cournot competition games. Rather than converging to Nash equilibria, LLM agents tend to cooperate when given multi-round prompts and non-zero-sum context. Chain-of-thought analysis reveals fairness reasoning is central. Proposes analytical framework capturing reasoning dynamics across rounds.
- **Key Innovation**: Empirical finding that LLM agents cooperate (not compete) in strategic games
- **Link**: https://arxiv.org/abs/2604.00487

### AVACraft: Attentive VLM Agent for Mastering StarCraft II
- **Authors**: Camel AI
- **Affiliation**: —
- **Venue**: arXiv 2503.05383 (Mar 2025, updated 2026)
- **Abstract**: Multimodal StarCraft II benchmark supporting both MARL and VLM paradigms. 21 scenarios spanning micromanagement, coordination, strategic planning. MARL peaks at 19.3% win rate after 5M steps; VLMs achieve 75-90% zero-shot with human-aligned decisions. Exposes trade-offs between sample efficiency, performance ceilings, interpretability, deployment cost.
- **Key Innovation**: First unified benchmark comparing MARL vs VLM zero-shot in StarCraft II
- **Link**: https://arxiv.org/abs/2503.05383

### Echo: Experience Transfer for Multimodal LLM Agents in Minecraft
- **Authors**: Chenghao Li, et al.
- **Affiliation**: —
- **Venue**: arXiv 2604.05533 (Apr 2026)
- **Abstract**: Transfer-oriented memory framework decomposing reusable knowledge into 5 dimensions: structure, attribute, process, function, interaction. Uses In-Context Analogy Learning (ICAL) to retrieve and adapt experiences. In Minecraft: 1.3-1.7× speed-up on object-unlocking tasks. Exhibits burst-like chain-unlocking phenomenon.
- **Key Innovation**: Structured 5-dimension experience decomposition for knowledge transfer
- **Link**: https://arxiv.org/abs/2604.05533

### PEAM: Parametric Embodied Agent Memory in Minecraft
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2605.27762 (May 2026)
- **Abstract**: Transforms agent memory from inference-time retrieval into parameter-resident skills via multimodal MoE LoRA with per-category physically isolated adapters. Failure-correction trajectory pairs internalized via joint BC + contrastive objective. Parameterization-worthiness score and scale-free self-triggered consolidation. Improves long-horizon task performance, mitigates forgetting.
- **Key Innovation**: Parameter-level memory consolidation with per-category isolation in MoE LoRA
- **Link**: https://arxiv.org/abs/2605.27762

### MineEvolve: Self-Evolution with Accumulated Knowledge for Long-Horizon Minecraft Agents
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2603.13131 (Mar 2026)
- **Abstract**: Knowledge-driven self-evolution framework transforming past executions into reusable knowledge for future decisions. Uses monitor, inducer, curator components. Addresses long-dependency planning, failure recovery, cross-task experience transformation in Minecraft.
- **Key Innovation**: Knowledge-driven self-evolution for long-horizon embodied agents
- **Link**: https://arxiv.org/abs/2603.13131

### CrossHA: Training One Model to Master Cross-Level Agentic Actions via RL
- **Authors**: Kaichen He, Zihao Wang, Muyao Li, Anji Liu, Yitao Liang
- **Affiliation**: —
- **Venue**: CVPR 2026 / arXiv 2512.09706
- **Abstract**: Unified agentic model mastering heterogeneous action spaces. Three-stage pipeline: cold-start SFT, Single-Turn RL, Multi-Turn GRPO. Trained on 30 Minecraft tasks, generalizes to 800+ tasks. Autonomously selects optimal action spaces (high-level APIs vs low-level controls), significantly outperforming fixed-action baselines.
- **Key Innovation**: Multi-level action space selection via multi-turn GRPO in Minecraft
- **Link**: https://arxiv.org/abs/2512.09706

---

## 3. Game Foundation Models

### Towards Generalist Game Players: An Investigation of Foundation Models in the Game Multiverse
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2605.09965 (May 2026)
- **Abstract**: Comprehensive survey tracing generalist game player evolution across 4 eras (symbolic/RL → foundation models → creator stage). Four interdependent pillars: Dataset, Model, Harness, Benchmark. Five-level roadmap from single-game mastery to creator stage. First systematic investigation of Large Foundation Models (LFMs) as generalist game players through end-to-end lifecycle.
- **Key Innovation**: Unified pipeline-oriented taxonomy for generalist game agent research
- **Link**: https://arxiv.org/abs/2605.09965

### Scaling Behavior Cloning Improves Causal Reasoning: An Open Model for Real-Time Video Game Playing
- **Authors**: Elefant AI
- **Affiliation**: Elefant AI
- **Venue**: arXiv 2601.04575 (Jan 2026)
- **Abstract**: Open recipe for training video game playing foundation model for real-time inference on consumer GPU. Releases 8300+ hours of human gameplay, code, checkpoints. Shows competitive human-level performance across 3D games. Demonstrates scaling BC improves causal reasoning: more data and network depth → more causal policy (validated in toy setting and at scale up to 1.2B params).
- **Key Innovation**: Open-source foundation model for real-time game playing with causal reasoning scaling laws
- **Link**: https://arxiv.org/abs/2601.04575

### Pixels2Play 0.1 (P2P0.1): A Foundation Model for 3D Gameplay
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2508.14295 / CoG 2025 (short paper)
- **Abstract**: Foundation model trained end-to-end to play 3D video games from raw pixels using behavior cloning. Labeled demonstrations + unlabeled public videos with imputed actions via inverse-dynamics model. Decoder-only transformer with autoregressive action output, latency-friendly on single consumer GPU. Competent play across Roblox and classic MS-DOS titles. Text-conditioned control planned.
- **Key Innovation**: Text-conditioned foundation model for 3D games from raw pixels
- **Link**: https://arxiv.org/abs/2508.14295

### Optimus-3: Generalist Multimodal Minecraft Agent with Scalable Task Experts
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2506.10357 (Jun 2025)
- **Abstract**: General-purpose Minecraft agent with three innovations: (1) knowledge-enhanced data generation pipeline, (2) MoE architecture with task-level routing to mitigate heterogeneous task interference, (3) Multimodal Reasoning-Augmented RL using GRPO with IoU-Density Reward. Surpasses both generalist MLLMs and existing SOTA agents across wide range of Minecraft tasks.
- **Key Innovation**: Task-level MoE routing + reasoning-augmented GRPO for Minecraft
- **Link**: https://arxiv.org/abs/2506.10357

### Training One Model to Master Cross-Level Agentic Actions via RL
- **Authors**: Kaichen He, Zihao Wang, Muyao Li, Anji Liu, Yitao Liang
- **Affiliation**: —
- **Venue**: CVPR 2026
- **Abstract**: See [[#CrossHA]] above (same paper).
- **Link**: https://openaccess.thecvf.com/content/CVPR2026/papers/He_Training_One_Model_to_Master_Cross-Level_Agentic_Actions_via_Reinforcement_CVPR_2026_paper.pdf

---

## 4. Procedural Content Generation

### Learning Local Constraints for Reinforcement-Learned Content Generators
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2605.13570 (May 2026)
- **Abstract**: Combines PCGRL (RL-based generation) with Wave Function Collapse (WFC). Constrains PCGRL generator's action space with WFC-learned constraints — RL achieves global properties (playability) while WFC enforces local visual aesthetics. Tested on Lode Runner puzzle-platformer levels. Best generators produce visually satisfying and playable levels.
- **Key Innovation**: Hybrid WFC+RL for simultaneously satisfying local aesthetics and global playability
- **Link**: https://arxiv.org/abs/2605.13570

### IPCGRL: Language-Instructed Reinforcement Learning for Procedural Level Generation
- **Authors**: Baek, et al.
- **Affiliation**: —
- **Venue**: arXiv 2503.12358 (Mar 2025)
- **Abstract**: Instruction-based PCG via RL incorporating sentence embedding model. Fine-tunes task-specific embedding representations for compressing game-level conditions. 21.4% improvement in controllability and 17.2% improvement in generalizability vs pretrained BERT embeddings on 2D level generation. Flexible and expressive interaction framework.
- **Key Innovation**: Sentence embedding fine-tuning for text-conditioned level generation
- **Link**: https://arxiv.org/abs/2503.12358

### VIPCGRL: Human-Aligned PCG via Text-Level-Sketch Shared Representation
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2508.09860 (Aug 2025)
- **Abstract**: Vision-Instruction PCGRL incorporating three modalities (text, level, sketches). Quadruple contrastive learning across modalities and human-AI styles. Auxiliary reward based on embedding similarity. Outperforms baselines in human-likeness validated by quantitative metrics and human evaluations.
- **Key Innovation**: Multi-modal (text+level+sketch) shared embedding for human-aligned PCG
- **Link**: https://arxiv.org/abs/2508.09860

### Multi-task Procedural Content Generation with Reinforcement Learning
- **Authors**: Nekahdari, Kouzehkonani, Saeedi, et al.
- **Affiliation**: —
- **Venue**: Scientific Reports (2026)
- **Abstract**: Multi-task language-based PCGRL framework using DeBERTa encoder and multi-objective training (regression, contrastive alignment, hybrid learning). Evaluated on 14,000+ command-level pairs in Super Mario. Outperforms BERT-based methods in command following, semantic stability, structural diversity.
- **Key Innovation**: Multi-task + contrastive alignment for language-conditioned PCG
- **Link**: https://doi.org/10.1038/s41598-026-48234-7

### MOPCGRL: Multi-Objective Procedural Content Generation via Reinforcement Learning
- **Authors**: Yuan, Zhang, Yuan, et al.
- **Affiliation**: —
- **Venue**: Complex System Modeling and Simulation, 6(1): 57-74 (Mar 2026)
- **Abstract**: Trains set of generators balancing trade-offs between multiple diversity metrics with playability as constraint. Compared on Mario-AI benchmark. Increases generator distribution diversity while accelerating early-stage convergence. Enables understanding of relationships among conflicting diversity metrics.
- **Key Innovation**: Pareto-optimal multi-objective PCGRL with playability constraints
- **Link**: https://doi.org/10.23919/CSMS.2025.0034

### PCGRL-Jax: Scaling, Control and Generalization in RL Level Generators
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2408.12525 (Aug 2024, updated)
- **Abstract**: Reimplements PCGRL in JAX for GPU-parallel simulation (15× speedup). Trains for 1B timesteps (vs previous 200M). Introduces randomized level sizes and frozen pinpoints to counter overfitting. Partial observation windows learn more robust design strategies on out-of-distribution map sizes.
- **Key Innovation**: JAX-accelerated PCGRL enabling billion-step training and robust generalization
- **Link**: https://arxiv.org/abs/2408.12525

### HDPCG: High Dimensional Procedural Content Generation
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2602.18943 (Feb 2026)
- **Abstract**: Extends PCG beyond geometry to include layers, time, locomotion modes. Search-based approach using TEG-A* with event-window unrolling. Plans toward PCGML and RL integration, user studies, and multi-mechanic composition. Instantiated on 2D/3D grids.
- **Key Innovation**: High-dimensional PCG incorporating multiple game mechanics simultaneously
- **Link**: https://arxiv.org/abs/2602.18943

### A Modular Framework for Automated Evaluation of PCG in Serious Games with DRL Agents
- **Authors**: Eleftherios Kalafatis, Konstantinos Mitsis, et al.
- **Affiliation**: —
- **Venue**: arXiv 2505.16801 (May 2025)
- **Abstract**: Automated evaluation framework for PCG in serious games using DRL testing agents. Validated on card game SG with 3 PCG versions (random vs genetic algorithm). DRL agents trained on genetic PCG versions peaked at 97% win rate; statistically significant higher than random PCG (94%).
- **Key Innovation**: DRL agents as automated evaluators of procedurally generated game content
- **Link**: https://arxiv.org/abs/2505.16801

---

## 5. Game Benchmarks

### GameDevBench: Evaluating Agentic Capabilities Through Game Development
- **Authors**: Wayne Chi, et al.
- **Affiliation**: —
- **Venue**: arXiv 2602.11103 (Feb 2026)
- **Abstract**: First benchmark for evaluating agents on game development tasks. 132 tasks from web/video tutorials requiring multimodal understanding — average solution needs 3× more code and file changes than prior SWE benchmarks. Best agent solves only 54.5%. Image/video feedback mechanisms consistently improve performance (Claude Sonnet 4.5: 33.3% → 47.7%).
- **Key Innovation**: Game development as multimodal agentic benchmark with visual feedback
- **Link**: https://arxiv.org/abs/2602.11103

### lmgame-Bench: How Good are LLMs at Playing Games?
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2505.15146 (May 2025)
- **Abstract**: Studies challenges in using video games to evaluate LLMs (brittle perception, prompt sensitivity, data contamination). Introduces lmgame-Bench with platformer/puzzle/narrative games via unified Gym-style API. Shows RL on a single game transfers to unseen games and external planning tasks. 13 models evaluated; o3/o1 achieve top performance.
- **Key Innovation**: Game-based LLM benchmark with RL transfer verification
- **Link**: https://arxiv.org/abs/2505.15146

### GameWorld: Standardized and Verifiable Evaluation of Multimodal Game Agents
- **Authors**: —
- **Affiliation**: NUS / Oxford
- **Venue**: arXiv 2604.07429 (Apr 2026)
- **Abstract**: Benchmark for MLLMs as game agents with 34 browser games and 170 tasks. Two interfaces: (1) Computer-use agents (keyboard/mouse), (2) Generalist multimodal agents (semantic action parsing). State-verifiable metrics for outcome-based evaluation. Best agent far from human. Repeated full-benchmark reruns demonstrate robustness.
- **Key Innovation**: Dual-interface (CUA + semantic) browser game benchmark with state verification
- **Link**: https://arxiv.org/abs/2604.07429

### GameVerse: Can Vision-Language Models Learn from Video-based Reflection?
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2603.06656 (Mar 2026)
- **Abstract**: Benchmark with 15 globally popular games, dual action space (semantic + GUI), reflect-and-retry paradigm. Shows VLMs benefit from reflecting on failures + expert tutorials — training-free analogue to RL + SFT. Combining failures (analogous to RL) and tutorials (analogous to SFT) yields largest gains.
- **Key Innovation**: Video-based reflection benchmark with training-free RL+SFT analogue
- **Link**: https://arxiv.org/abs/2603.06656

### MineExplorer: Evaluating Open-World Exploration of MLLM Agents in Minecraft
- **Authors**: Tianjie Ju, et al.
- **Affiliation**: —
- **Venue**: arXiv 2605.30931 (May 2026)
- **Abstract**: Benchmark for open-world exploration in Minecraft using ReAct-style capability formulation. Multi-agent synthesis workflow for task graph, sandbox scenes, and rule-based evaluators. Strong models handle single-hop tasks but degrade sharply on multi-hop tasks with hidden prerequisites. Larger models or thinking modes don't consistently translate to better performance.
- **Key Innovation**: Multi-agent synthetic workflow for reliable Minecraft exploration benchmark
- **Link**: https://arxiv.org/abs/2605.30931

### MineNPC-Task: Task Suite for Memory-Aware Minecraft Agents
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2601.05215 (Jan 2026)
- **Abstract**: User-authored benchmark for memory-aware, mixed-initiative LLM agents in Minecraft. Tasks elicited from expert co-play, normalized into parametric templates with preconditions and dependency structure. Bounded-knowledge policy forbids out-of-world shortcuts. GPT-4o baseline: 71 subtask failures out of 216 (~33%).
- **Key Innovation**: User-authored Minecraft benchmark with bounded-knowledge evaluation
- **Link**: https://arxiv.org/abs/2601.05215

### Orak: Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games
- **Authors**: KRAFTON AI
- **Affiliation**: KRAFTON
- **Venue**: arXiv 2506.03610 (Jun 2025)
- **Abstract**: Benchmark across 12 popular video games spanning all major genres using Model Context Protocol (MCP) plug-and-play interface. Releases fine-tuning dataset of expert LLM gameplay trajectories. 15 LLMs evaluated: proprietary LLMs lead but gap narrows in battle scenarios; fine-tuning enables cross-game transfer.
- **Key Innovation**: MCP-based plug-and-play game benchmark with LLM fine-tuning dataset
- **Link**: https://arxiv.org/abs/2506.03610

### GameTraversalBenchmark: Evaluating Planning Abilities of LLMs Through 2D Game Maps
- **Authors**: Umair Nasir, et al.
- **Affiliation**: —
- **Venue**: arXiv 2410.07765 (Oct 2024)
- **Abstract**: Benchmark consisting of diverse 2D grid-based game maps evaluating traversal planning. GPT-4-Turbo achieves only 44.97% on composite score. o1 reasoning model scores 67.84%. Benchmark remains challenging for current models.
- **Key Innovation**: 2D game map traversal as planning benchmark for LLMs
- **Link**: https://arxiv.org/abs/2410.07765

---

## 6. Industry Game AI

### NVIDIA In-Game Inferencing (IGI) SDK + Cosmos-Reason1 Optimization
- **Authors**: NVIDIA
- **Affiliation**: NVIDIA
- **Venue**: arXiv 2604.26334 (Apr 2026)
- **Abstract**: Enables game developers to integrate xLM inference at any VRAM budget via IGI SDK. Pipelines sharding achieves: TTFT improvement up to 6.7×, TPS up to 30× for LLMs, VRAM reduction 10× for Cosmos-Reason1 VLM on client systems. Uses CUDA-in-Graphics for concurrent AI + graphics.
- **Key Innovation**: Production-grade on-device LLM/VLM inference for game integration
- **Link**: https://arxiv.org/abs/2604.26334

### Mobile MOBA Game AI Deployment (Honor of Kings)
- **Authors**: —
- **Affiliation**: Tencent / Honor of Kings
- **Venue**: arXiv 2602.07521 (Feb 2026)
- **Abstract**: Pareto optimality guided pipeline for deploying MOBA game AI on mobile devices. Designs efficient student architecture achieving 12.4× faster inference (<0.5ms/frame), 15.6× energy efficiency improvement (<0.5mAh/game), while retaining 40.32% win rate against teacher model. First systematic study bridging large-scale game AI to mobile deployment.
- **Key Innovation**: Pareto-optimal distillation for mobile MOBA AI deployment
- **Link**: https://arxiv.org/abs/2602.07521

### Arm Neural Dawn: Neural Graphics on Mobile
- **Authors**: Arm / Sumo Digital
- **Affiliation**: Arm, Sumo Digital
- **Venue**: Arm News (Jun 2026)
- **Abstract**: Mobile game demonstrating Arm Neural Technology using Unreal Engine MegaLights, ray-traced effects in mobile power envelope. 120 minutes of gameplay across 4 levels. Dedicated neural accelerators in Mali GPUs enable AI-powered graphics on mobile.
- **Key Innovation**: Neural graphics pipeline for real-time cinematic lighting on mobile
- **Link**: https://newsroom.arm.com/news/announcing-neural-dawn

### cMarlTest: Curiosity Driven MARL for 3D Game Testing
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2502.14606 (Feb 2025)
- **Abstract**: Testing approach for 3D games using curiosity-driven MARL. Multiple agents collaborate to explore game worlds maximizing coverage (entity, entity connection, spatial). Effective and efficient compared to single-agent RL baseline.
- **Key Innovation**: Multi-agent curiosity-driven exploration for automated game testing
- **Link**: https://arxiv.org/abs/2502.14606

### NVIDIA + Krafton + NCSoft: Physical AI and On-Device Gaming Cooperation
- **Authors**: NVIDIA, Krafton, NCSoft
- **Affiliation**: NVIDIA, KRAFTON, NCSoft
- **Venue**: Industry news (Jun 2026)
- **Abstract**: Jensen Huang meets Krafton/NCSoft leadership. Krafton: on-device AI characters (PUBG Ally, inZOI Smart Zoi via NVIDIA ACE), physical AI unit Ludo Robotics. NCSoft: world models, industrial simulation, defense physical AI, autonomous welding AI.
- **Key Innovation**: Game studios as partners in physical AI through virtual training grounds
- **Link**: https://en.bloomingbit.io/feed/news/113544

---

## 7. World Models for Games

### WorldCompass: RL for Long-Horizon World Models
- **Authors**: Tencent Hunyuan
- **Affiliation**: Tencent
- **Venue**: arXiv 2602.09022 (Feb 2026)
- **Abstract**: RL post-training framework for interactive video world models. Three innovations: clip-level rollout strategy (fine-grained rewards), complementary reward functions (interaction accuracy + visual quality), negative-aware fine-tuning. Significantly improves interaction accuracy and visual fidelity of WorldPlay across various scenarios.
- **Key Innovation**: RL-based post-training for interactive world model accuracy
- **Link**: https://arxiv.org/abs/2602.09022

### WorldCam: Interactive Autoregressive 3D Gaming Worlds with Camera Pose
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2603.16871 (Mar 2026)
- **Abstract**: Establishes camera pose as unifying geometric representation for action control and 3D consistency. Physics-based continuous action space → precise 6-DoF camera poses via Lie algebra. Global camera poses as spatial indices for long-horizon navigation. 3,000 minutes of human gameplay annotated with camera trajectories. Substantially outperforms prior interactive world models.
- **Key Innovation**: Camera pose as geometric anchor for 3D world model consistency
- **Link**: https://arxiv.org/abs/2603.16871

### Solaris: Multiplayer Video World Model in Minecraft
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2602.22208 (Feb 2026)
- **Abstract**: First multiplayer video world model generating consistent multi-view observations. Multiplayer data collection system producing 12.64M frames. Staged training from single-player to multiplayer combining bidirectional + causal + Self Forcing. Checkpointed Self Forcing for memory-efficient long-horizon training.
- **Key Innovation**: Multi-view consistent world model for multiplayer environments
- **Link**: https://arxiv.org/abs/2602.22208

### EAWM: Event-Aware World Model for Reinforcement Learning
- **Authors**: Zhao-Han Peng, Shaohui Li, Zhi Li, Shulan Ruan, Yu Liu, You He
- **Affiliation**: —
- **Venue**: arXiv 2601.19336 (Jan 2026)
- **Abstract**: Cognitive-inspired framework segmenting continuous sensory streams into discrete events. Automated event generator + Generic Event Segmentor (GES). Event-aware representations improve MBRL by 10-45% on Atari 100K, Craftax 1M, DeepMind Control 500K, DMC-GB2 500K. Unified formulation of seemingly distinct world model architectures.
- **Key Innovation**: Event-based abstraction for world models, inspired by human cognition
- **Link**: https://arxiv.org/abs/2601.19336

### Distilling Game Code World Models into Lightweight LLMs
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2605.24375 (May 2026)
- **Abstract**: Investigates distilling Game Code World Model generation capabilities into smaller models via SFT + RLVR. Curated dataset of 30 games (perfect and imperfect information). Verification framework evaluating structural + semantic game properties. Qwen2.5-3B-Instruct: SFT increases syntactic correctness, RLVR improves execution-level game rule adherence.
- **Key Innovation**: Distilling game logic coding into small LLMs via SFT+RLVR
- **Link**: https://arxiv.org/abs/2605.24375

### RWML: Reinforcement World Model Learning for LLM-based Agents
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2602.05842 (Feb 2026)
- **Abstract**: Self-supervised method learning action-conditioned world models for LLM agents. Aligns simulated next states with realized next states in pretrained embedding space (sim-to-real gap rewards). On ALFWorld and τ² Bench: +19.6 and +6.9 points over base without expert data. Combined with task-success rewards outperforms direct task-success RL by 6.9/5.7 points.
- **Key Innovation**: Sim-to-real world model alignment for LLM agents via embedding space
- **Link**: https://arxiv.org/abs/2602.05842

### What Do World Models Learn in RL? Probing Latent Representations
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2603.21546 (Mar 2026)
- **Abstract**: Applies interpretability techniques to two world models (IRIS — VQ-VAE+transformer, DIAMOND — diffusion UNet on Atari). Linear probing shows approximately linear game state representations (object positions, scores). Causal interventions confirm functional use. Attention heads show spatial specialization. Token ablation identifies object-containing tokens as disproportionately important.
- **Key Innovation**: First mechanistic interpretability study of world model internal representations
- **Link**: https://arxiv.org/abs/2603.21546

### SWIRL: Self-Improving World Modelling with Latent Actions
- **Authors**: Qiu, et al.
- **Affiliation**: —
- **Venue**: arXiv 2602.06130 (Feb 2026)
- **Abstract**: Learns world models from state-only sequences by treating actions as latent variable, alternating Forward World Modelling and Inverse Dynamics Modelling. Trained with GRPO using log-probability as reward. Gains: Aurora-Bench +16%, ByteMorph +28%, WorldPredictionBench +16%, StableToolBench +14%.
- **Key Innovation**: Self-supervised world model learning without action labels via variational EM
- **Link**: https://arxiv.org/abs/2602.06130

### Agent World Model (AWM): Infinite Synthetic Environments for Agentic RL
- **Authors**: Snowflake Labs
- **Affiliation**: Snowflake
- **Venue**: arXiv 2602.10090 (Feb 2026)
- **Abstract**: Fully synthetic environment generation pipeline scaling to 1,000 environments covering everyday scenarios. Agents interact with rich toolsets (35 tools/environment avg) via code-driven DB-backed environments. Large-scale GRPO training in synthetic environments yields strong out-of-distribution generalization on 3 tool-use benchmarks.
- **Key Innovation**: Database-backed synthetic environments enabling scalable agentic RL
- **Link**: https://arxiv.org/abs/2602.10090

---

## 8. Related Techniques

### HiPER: Hierarchical RL with Explicit Credit Assignment for LLM Agents
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2602.16165 (Feb 2026)
- **Abstract**: Hierarchical Plan-Execute RL framework separating high-level planning (subgoal proposals) from low-level execution. Introduces Hierarchical Advantage Estimation (HAE) providing unbiased gradient estimator with provably reduced variance vs flat GAE. Addresses long-horizon, sparse-reward tasks for LLM agents.
- **Key Innovation**: Hierarchical advantage estimation for structured RL credit assignment
- **Link**: https://arxiv.org/abs/2602.16165

### AgentOWL: Joint Learning of Hierarchical Neural Options and Abstract World Model
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2602.02799 (Feb 2026)
- **Abstract**: Jointly learns abstract world model (symbolic code + non-parametric distributions) and hierarchical neural options. Sample-efficient skill acquisition on Object-Centric Atari games (Montezuma's Revenge, Pitfall, Private Eye). Acquires highest number of skills vs baselines.
- **Key Innovation**: Symbolic-nonparametric hybrid world model for hierarchical option learning
- **Link**: https://arxiv.org/abs/2602.02799

### Multi-level Meta-Reinforcement Learning with Skill-based Curriculum
- **Authors**: Sichen Yang, et al.
- **Affiliation**: —
- **Venue**: arXiv 2603.08773 (Mar 2026)
- **Abstract**: Efficient multi-level MDP compression procedure: parametric policy family at one level → single actions in compressed MDPs at higher levels. Decouples sub-tasks, reduces stochasticity and policy search space. Teacher organizes student's learning via curriculum. Demonstrated on MazeBase+.
- **Key Innovation**: Multi-level MDP compression with transferable skills across levels
- **Link**: https://arxiv.org/abs/2603.08773

### Remember to be Curious: Episodic Context and Persistent Worlds for 3D Exploration
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2605.22814 (May 2026)
- **Abstract**: Shows curiosity-driven RL in photorealistic 3D fails due to lack of spatial persistence and episodic context. Uses online 3D reconstruction as persistent world model + sequence model policy over RGB frames. Trained purely on curiosity on HM3D, outperforms active-mapping baselines and zero-shot generalizes to Gibson and AI-generated worlds.
- **Key Innovation**: Persistent 3D reconstruction + episodic memory for curiosity-driven exploration
- **Link**: https://arxiv.org/abs/2605.22814

### GLANCE: Visual-Linguistic Curiosity for VLM Agents
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2605.03782 (May 2026)
- **Abstract**: Projects VLM linguistic predictions into visual representation space; uses discrepancy as curiosity reward. Jointly optimizes world modeling + exploration. Transforms exploration from stochastic search into active falsification. Outperforms exploitation-based RL methods on Grid Puzzles, 3D Navigation, Object Manipulation, Geometric Reconstruction.
- **Key Innovation**: Cross-modal curiosity aligning linguistic reasoning with visual reality
- **Link**: https://arxiv.org/abs/2605.03782

### CurioSFT: Entropy-Preserving SFT for Large Reasoning Models
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv 2602.02244 (Feb 2026)
- **Abstract**: Addresses SFT-induced overconfidence reducing RL exploration diversity. Self-Exploratory Distillation + Entropy-Guided Temperature Selection. Outperforms vanilla SFT by 2.5 points in-distribution, 2.9 points OOD. RL gains: +5.0 average improvement.
- **Key Innovation**: Entropy-preserving SFT maintaining exploration capabilities for subsequent RL
- **Link**: https://arxiv.org/abs/2602.02244

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Game Reinforcement Learning | 10 |
| Game AI Bots | 12 |
| Game Foundation Models | 4 |
| Procedural Content Generation | 8 |
| Game Benchmarks | 8 |
| Industry Game AI | 4 |
| World Models for Games | 9 |
| Related Techniques | 6 |
| **Total** | **61** |

## Key Trends

1. **Self-play + RL for LLM reasoning**: STRATAGEM, SPIRAL, π-Play demonstrate game self-play transfers to mathematical and general reasoning — a major convergence of game RL and LLM post-training.

2. **MARL benchmarks evolving**: SMAC-HARD, HLSMAC, SC2BA, AVACraft address SMAC's diversity and strategic depth limitations.

3. **World models as game engines**: Matrix-Game 3.0 (40 FPS 720p), WorldCam, Solaris (multiplayer) push interactive world models toward production quality.

4. **On-device game AI matures**: NVIDIA IGI SDK, Honor of Kings mobile deployment, Arm Neural Dawn show industry investment in client-side inference.

5. **LLM agents tackle complex games**: PTCG-Bench, APEX (Jericho text adventures), Bounded Autonomy (live multiplayer), AVACraft (StarCraft II) test LLMs in increasingly realistic and complex game scenarios.

6. **PCG goes multi-modal**: VIPCGRL (text+level+sketch), IPCGRL (language-instructed), and MOPCGRL (multi-objective) expand PCG controllability.

7. **Co-evolution for open-ended learning**: FAMOU demonstrates LLMs can serve as mutation operators generating novel tactical structures (lookahead search, adaptive interception) in adversarial games.

8. **Interpretability for world models**: First mechanistic probing studies (What Do World Models Learn in RL?) reveal approximately linear state representations in learned world models.
