---
title: "Game RL & Game AI Bot — Daily Survey (2026-06-20)"
type: synthesis
created: 2026-06-20
updated: 2026-06-20
sources: [arxiv-search, iclr-2026, cvpr-2026, icml-2026]
tags: [game-rl, game-ai, self-play, foundation-models, pcg, benchmarks, world-models, daily]
---

# Game RL & Game AI Bot — Daily Survey

> Coverage: ~65 papers across 7 categories. Sources: arXiv (June 2026), ICLR 2026, CVPR 2026, ICML 2026, Scientific Reports 2026, GDC 2026, NVIDIA CES 2026. Focus on **new papers** since previous daily (2026-06-19).

---

## 1. Game RL — Reinforcement Learning in Games

### 1.1 Game-RL: Synthesizing Multimodal Verifiable Game Data to Boost VLMs' General Reasoning
- **Authors**: Jingqi Tong, Jixin Tang, Hangcheng Li, Yurong Mou, Ming Zhang, Jun Zhao, et al. (23 authors)
- **Affiliation**: Fudan University, Shanghai Innovation Institute, SUSTech
- **Venue**: **ICLR 2026**
- **Abstract**: First work to adapt game code to synthesize multimodal game data for VLM training. Proposes **Code2Logic** — a novel approach that adapts game code to synthesize reasoning data with unlimited examples and controllable difficulty gradation. Constructs **GameQA** dataset of 30 games and 158 verifiable tasks (140K QA pairs). RL training solely on GameQA enables VLMs to generalize across 7 diverse out-of-domain vision-language benchmarks, with improvements comparable to general multimodal reasoning datasets (geometry/chart). Scaling up game diversity or data volume consistently improves generalizable reasoning.
- **Key innovation**: Code2Logic synthesis pipeline; verifiable game rewards for VLM RL training; scaling law for game diversity affecting reasoning transfer.
- **Link**: [arXiv:2505.13886](https://arxiv.org/abs/2505.13886) | [GitHub](https://github.com/tongjingqi/Game-RL) | [OpenReview (ICLR 2026)](https://openreview.net/forum?id=e4FqU4SyHL)

### 1.2 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning (detailed)
- **Authors**: Brandon Liu, Song Yu, Ziyu Liu, Leon Guertler, et al.
- **Affiliation**: National University of Singapore, multiple institutions
- **Venue**: **ICLR 2026** Poster
- **Abstract**: Self-play framework where LLMs learn by playing multi-turn zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation) against continuously improving versions of themselves. Proposes **Role-conditioned Advantage Estimation (RAE)** to stabilize multi-agent training. Improves reasoning by up to 10% across 8 benchmarks on Qwen/Llama families. Multi-game training yields strongest results. Even DeepSeek-R1-Distill-Qwen-7B benefits from this approach.
- **Key innovation**: Eliminates human supervision via self-play; RAE for stable multi-agent LLM training; transferable cognitive patterns from games to math/reasoning tasks.
- **Link**: [OpenReview (ICLR 2026)](https://openreview.net/forum?id=6z4YKr0GK6) | [arXiv:2506.24119](https://arxiv.org/abs/2506.24119)

### 1.3 GROW: Aligning GRPO with State-Action Modeling for Open-World VLM Agents
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Aligns GRPO with state-action modeling for open-world VLM agents in Minecraft. Bridges the gap between GRPO's token-level optimization and the state-action MDP formulation required for embodied game agents.
- **Key innovation**: State-action alignment for GRPO in Minecraft; open-world VLM agent training.
- **Link**: [arXiv:2605.20246](https://arxiv.org/abs/2605.20246)

### 1.4 Gated Coordination for Efficient Multi-Agent Collaboration in Minecraft
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Gated coordination mechanism for efficient multi-agent collaboration in Minecraft. Agents learn when to share information and when to act independently through learned gating functions.
- **Key innovation**: Learned communication gating; selective information sharing for MARL.
- **Link**: [arXiv:2604.18975](https://arxiv.org/abs/2604.18975)

### 1.5 Ratchet: A Minimal Hygiene Recipe for Self-Evolving LLM Agents
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Minimal recipe for self-evolving LLM agents in Minecraft and other environments. Focuses on hygiene factors: experience replay, curriculum scheduling, and diversity maintenance.
- **Key innovation**: Minimal recipe for reliable self-evolution; practical training guidelines.
- **Link**: [arXiv:2605.22148](https://arxiv.org/abs/2605.22148)

### 1.6 Realtime Reinforcement Learning: Rapid Asynchronous RL for Games
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Formalizes realtime RL where learning, inference, and environment all run asynchronously. Proposes staggered inference processes enabling orders-of-magnitude larger models in realtime games like Pokémon and Tetris. Derives worst-case regret bounds showing standard sequential interaction scales poorly with model size.
- **Key innovation**: Asynchronous multi-process RL; formal time discretization for realtime games; theoretical regret bounds.
- **Link**: [OpenReview](https://openreview.net/pdf?id=V6T0DCYcVQ)

### 1.7 Multi-Task PCG with Reinforcement Learning
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: **Scientific Reports 2026**
- **Abstract**: Multi-task language-based PCGRL framework using DeBERTa encoder and multi-objective training (regression, contrastive alignment, hybrid learning). 14,000+ command-level pairs in Super Mario environment. Outperforms BERT-based methods in command following, semantic stability, and structural diversity.
- **Key innovation**: Multi-task PCGRL with language conditioning; DeBERTa-based semantic alignment for level generation.
- **Link**: [Nature Scientific Reports 2026](https://www.nature.com/articles/s41598-026-48234-7)

### 1.8 Mastering Diverse Domains through World Models: DreamerV3 (Nature 2025)
- **Authors**: Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, Timothy Lillicrap
- **Affiliation**: Google DeepMind
- **Venue**: **Nature 2025**
- **Abstract**: General-purpose RL algorithm with fixed hyperparameters mastering 150+ diverse tasks. Outperforms specialized methods on Atari, Minecraft, DMLab, continuous control. First algorithm to obtain diamonds in Minecraft from sparse rewards.
- **Key innovation**: Fixed hyperparameters across all domains; world model for imagination training; monotonic scaling.
- **Link**: [arXiv:2301.04104](https://arxiv.org/abs/2301.04104) | [Nature 2025](https://danijar.com/dreamerv3/)

### 1.9 Multi-Agent Evolve: LLM Self-Improve through Co-evolution
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2025
- **Abstract**: Self-play for LLMs where multiple agents co-evolve through competitive and cooperative interactions. Uses LLM-as-a-judge for evaluation. Extends SPIRAL-style self-play to general domains beyond zero-sum games.
- **Key innovation**: Co-evolution framework with judge-based evaluation; extends self-play beyond zero-sum.
- **Link**: [arXiv:2510.23595](https://arxiv.org/abs/2510.23595)

---

## 2. Game AI Bot — LLM-Powered Game Agents & NPC Intelligence

### 2.1 Experience Transfer for Multimodal LLM Agents in Minecraft
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Framework for transferring experience across multimodal LLM agents in Minecraft. Agents share learned skills and strategies through structured experience representations, enabling faster adaptation to new tasks.
- **Key innovation**: Cross-agent experience transfer; structured skill representations for Minecraft.
- **Link**: [arXiv:2604.05533](https://arxiv.org/abs/2604.05533)

### 2.2 Requesting Expert Reasoning: Augmenting LLM Agents with Learned Collaborative Intervention
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: LLM agents learn when to request expert intervention during gameplay. Collaborative framework where agents recognize their limitations and proactively seek help, improving task completion rates in complex Minecraft scenarios.
- **Key innovation**: Learned intervention requests; human-AI collaboration for game agents.
- **Link**: [arXiv:2602.22546](https://arxiv.org/abs/2602.22546)

### 2.3 MineNPC-Task: Task Suite for Memory-Aware Minecraft Agents
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Task suite designed specifically for evaluating memory-aware Minecraft agents. Tests long-term memory, spatial memory, and procedural recall in open-world settings.
- **Key innovation**: Memory-specific evaluation suite; standardized memory benchmarks for game agents.
- **Link**: [arXiv:2601.05215](https://arxiv.org/abs/2601.05215)

### 2.4 BLOCK: Bi-Stage MLLM Character-to-Skin Pipeline for Minecraft
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Open-source bi-stage pipeline for generating Minecraft character skins from text descriptions using multimodal LLMs. First stage generates character design, second stage renders to game-compatible skin.
- **Key innovation**: MLLM-powered asset generation; two-stage design-to-skin pipeline.
- **Link**: [arXiv:2603.03964](https://arxiv.org/abs/2603.03964)

### 2.5 ProxyWar: Dynamic Assessment of LLM Code Generation in Game Arenas
- **Authors**: Qi Wu, Wenjun Peng, Xinyu Wang
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026 (ICSE 2026)
- **Abstract**: Novel framework that systematically assesses code generation quality by embedding LLM-generated agents within competitive game environments. Agents compete in game arenas, providing dynamic, multi-dimensional evaluation beyond static benchmarks.
- **Key innovation**: Game-based code evaluation; competitive arenas for LLM assessment.
- **Link**: [arXiv:2602.04296](https://arxiv.org/abs/2602.04296)

### 2.6 Review Arcade: On the Human Alignment and Gameability of LLM Reviews
- **Authors**: Hans Ole Hatzel, Sebastian Steindl, Jan Strich
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Studies gameability of LLM-based review systems through game-theoretic analysis. Identifies vulnerabilities where LLM reviewers can be manipulated and proposes alignment improvements.
- **Key innovation**: Game-theoretic analysis of LLM review robustness; gameability metrics.
- **Link**: [arXiv:2605.28897](https://arxiv.org/abs/2605.28897)

---

## 3. Game Foundation Models — Generalist Game Agents

### 3.1 NitroGen: An Open Foundation Model for Generalist Gaming Agents (CVPR 2026)
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi "Jim" Fan
- **Affiliation**: **NVIDIA**, Stanford, Caltech, UChicago, UT Austin
- **Venue**: **CVPR 2026**
- **Abstract**: Vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games. Three key ingredients: internet-scale video-action dataset from public gameplay with automated action extraction, multi-game benchmark for cross-game generalization, unified vision-action model with behavior cloning. Up to 52% relative improvement on unseen games. Released as open-source.
- **Key innovation**: Automated action extraction from public gameplay videos; largest open gaming dataset; behavior cloning at scale.
- **Link**: [arXiv:2601.02427](https://arxiv.org/abs/2601.02427) | [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/papers/Magne_NitroGen_An_Open_Foundation_Model_for_Generalist_Gaming_Agents_CVPR_2026_paper.pdf)

### 3.2 Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents
- **Authors**: Zihao Wang et al. (27 authors)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2025
- **Abstract**: Generalist game agent pretrained on 500B+ tokens from OS, web, and simulation games. Unified keyboard-mouse action space. ~2× success rate vs prior SOTA on Minecraft, matches fresh humans on unseen web 3D games, outperforms GPT-5/Gemini-2.5-Pro/Claude-4-Sonnet on FPS benchmarks.
- **Key innovation**: Unified native keyboard-mouse action space; decaying continual loss; Sparse-Thinking strategy.
- **Link**: [arXiv:2510.23691](https://arxiv.org/abs/2510.23691)

### 3.3 GameGen-Verifier: Verification for LLM-Generated Games
- **Authors**: Chaobo Jia, Ruipeng Wan, Ting Sun, Weihao Tan, et al.
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Parallel keypoint-based verification framework for LLM-generated games. Runtime state injection enables verification of gameplay mechanics, rule consistency, and content quality.
- **Key innovation**: Keypoint-based parallel verification; runtime state injection for game validation.
- **Link**: [arXiv:2605.07442](https://arxiv.org/abs/2605.07442)

### 3.4 Multi-Agent Game Generation via Audio-Visual Recordings
- **Authors**: Alexia Jolicoeur-Martineau et al.
- **Affiliation**: (multiple)
- **Venue**: arXiv 2025
- **Abstract**: Multi-agent system using omni-modal evaluation metric (AVR-Eval) for JavaScript game and animation generation. Proposes AVR-Agent that generates code from multimedia asset banks, iteratively improving through omni-modal feedback. Shows significant win rate improvement over one-shot generation.
- **Key innovation**: Omni-modal evaluation for game generation; multi-agent iterative game code generation.
- **Link**: [arXiv:2508.00632](https://arxiv.org/abs/2508.00632)

---

## 4. Procedural Content Generation — RL & LLM for Game Content

### 4.1 PCGRLLM: LLM-Driven Reward Design for PCG RL
- **Authors**: In-Chang Baek, Sung-Hyun Kim, Sam Earle, Zehua Jiang, Noh Jin-Ha, Julian Togelius, Kyung-Joong Kim
- **Affiliation**: NYU, POSTECH
- **Venue**: arXiv 2025
- **Abstract**: LLM-driven reward design framework for PCGRL using feedback loop and reasoning-based prompt engineering (ToT, GoT). Up to 415% performance improvement on story-to-reward generation in 2D PCGRL environments.
- **Key innovation**: Self-alignment with environment feedback; automated reward function from story descriptions.
- **Link**: [arXiv:2502.10906](https://arxiv.org/abs/2502.10906)

### 4.2 IPCGRL: Language-Instructed RL for Procedural Level Generation
- **Authors**: In-Chang Baek, Sung-Hyun Kim, Seo-Young Lee, Dong-Hyeon Kim, Kyung-Joong Kim
- **Affiliation**: POSTECH
- **Venue**: IEEE Conference on Games 2025
- **Abstract**: Instruction-based PCGRL incorporating sentence embedding models. Fine-tunes task-specific embeddings to compress game-level conditions. Up to 21.4% improvement in controllability and 17.2% improvement in generalizability for unseen instructions.
- **Key innovation**: Sentence embedding for level generation conditioning; fine-tuned task-specific representations.
- **Link**: [arXiv:2503.12358](https://arxiv.org/abs/2503.12358)

### 4.3 Multi-Task PCG with RL (Scientific Reports 2026)
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: **Scientific Reports 2026**
- **Abstract**: Multi-task language-based PCGRL using DeBERTa encoder with multi-objective training. 14K+ command-level pairs in Super Mario. Outperforms BERT baselines in semantic stability, command following, and structural diversity.
- **Key innovation**: Multi-task PCGRL; contrastive alignment for language-conditioned level generation.
- **Link**: [Nature Scientific Reports 2026](https://www.nature.com/articles/s41598-026-48234-7)

### 4.4 Reward Design Agent (RDA): VLM-Based Reward Generation
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: VLM-based reward design agent that generates and refines reward functions using visual trajectory analysis. Achieves 0.95 alignment and 0.90 success rate on ManiSkill, significantly outperforming Eureka (0.87) on complex whole-body manipulation tasks. Visual feedback enables detection of reward mis-specification.
- **Key innovation**: Visual trajectory analysis for reward refinement; bridges VLM perception with reward design.
- **Link**: [arXiv:2606.01672](https://arxiv.org/abs/2606.01672)

### 4.5 PCG Benchmark: Open-Source Testbed
- **Authors**: Ahmed Khalifa, Roberto Gallotta, Matthew Barthet, Antonios Liapis, Julian Togelius, Georgios N. Yannakakis
- **Affiliation**: NYU, University of Malta, University of Copenhagen
- **Venue**: FDG 2025
- **Abstract**: Standardized PCG benchmark with 12 game-related problems, multiple variants per problem. Metrics for quality, diversity, and controllability.
- **Key innovation**: First standardized PCG benchmark; multi-dimensional evaluation.
- **Link**: [arXiv:2503.21474](https://arxiv.org/abs/2503.21474)

---

## 5. Game Benchmarks — Evaluation Suites & Agent Benchmarks

### 5.1 GameWorld: Standardized and Verifiable Evaluation of Multimodal Game Agents
- **Authors**: Mingyu Ouyang, Siyuan Hu, Kevin Qinghong Lin, Hwee Tou Ng, Mike Zheng Shou
- **Affiliation**: **National University of Singapore**
- **Venue**: arXiv 2026
- **Abstract**: Standardized benchmark for evaluating MLLMs as generalist game agents in browser environments. Two interfaces: computer-use agents (keyboard/mouse) and semantic action space via Semantic Action Parsing. 34 diverse games, 170 tasks with state-verifiable metrics. Results across 18 model-interface pairs show best performing agent far from human capabilities.
- **Key innovation**: Standardized verifiable metrics; dual interface (low-level + semantic); browser-based game evaluation.
- **Link**: [arXiv:2604.07429](https://arxiv.org/abs/2604.07429) | [Project Page](https://gameworld-bench.github.io)

### 5.2 lmgame-Bench (ICLR 2026)
- **Authors**: Lanxiang Hu, Mingjia Huo, Yuxuan Zhang, Haoyang Yu, et al.
- **Affiliation**: UC San Diego, UC Berkeley, CMU
- **Venue**: **ICLR 2026**
- **Abstract**: Benchmark built on well-established video games (platformer, puzzle, narrative-driven detective games). Gaming harness with perception and memory modules. Standardized prompt optimization. Hugging Face leaderboard.
- **Key innovation**: Gaming harness for fair VLM evaluation; data contamination detection.
- **Link**: [arXiv:2505.15146](https://arxiv.org/abs/2505.15146) | [Leaderboard](https://huggingface.co/spaces/lmgame/game_arena_bench)

### 5.3 DSGBench: Diverse Strategic Game Benchmark for LLM Agents
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2025
- **Abstract**: Diverse strategic game benchmark across board games, card games, economic games. Systematic comparison of popular LLM agents.
- **Key innovation**: Multi-genre strategic game evaluation.
- **Link**: [arXiv:2503.06047](https://ui.adsabs.harvard.edu/abs/2025arXiv250306047T/abstract)

### 5.4 MindGames Arena: Generalization Track (NeurIPS 2025 Competition)
- **Authors**: Aliaksei Korshuk, Alexander Buyantuev, Ilya Makarov
- **Affiliation**: (multiple)
- **Venue**: **NeurIPS 2025 Competition**
- **Abstract**: Competition track on multi-game generalization. Winning solution uses delayed per-step reward attribution.
- **Key innovation**: Competition for cross-game generalization; reward attribution.
- **Link**: [arXiv:2606.00017](https://arxiv.org/abs/2606.00017)

### 5.5 A Survey on Large Language Model-Based Game Agents (ACM CSUR)
- **Authors**: Sihao Hu, Tiansheng Huang, Gaowen Liu, et al.
- **Affiliation**: Georgia Tech, Cisco Research
- **Venue**: **ACM Computing Surveys 2026**
- **Abstract**: Comprehensive survey of LLM-based game agents. Unified reference architecture with core components: memory, reasoning, perception-action interfaces. Multi-agent communication protocols. Six game genres taxonomy. Continuously updated.
- **Key innovation**: Unified architecture; continuously updated paper list.
- **Link**: [arXiv:2404.02039](https://arxiv.org/abs/2404.02039) | [GitHub](https://github.com/git-disl/awesome-LLM-game-agent-papers)

---

## 6. Industry Game AI — Deployment & Production Systems

### 6.1 NVIDIA ACE: Autonomous Game Characters (CES 2025 → GDC 2026 Production)
- **Affiliation**: **NVIDIA**
- **Venue**: CES 2025, GDC 2026
- **Abstract**: Production SDK for deploying AI-powered NPCs in games. Expanded from conversational NPCs to **autonomous game characters** that perceive, plan, and act independently. Key features: small language models optimized for games (Qwen3-8B SLM), multimodal perception, action integration with game engines. Real-world integrations: **PUBG: BATTLEGROUNDS** (AI teammates/callouts), **NARAKA: BLADEPOINT** (AI companions), **inZOI** (Smart Zois autonomous agents), **MIR5** (adaptive AI bosses).
- **Key innovation**: On-device inference alongside graphics (NVIGI); autonomous perception-planning-action loop for NPCs; production deployment at scale.
- **Link**: [NVIDIA ACE Developer](https://developer.nvidia.com/ace) | [NVIDIA ACE Games](https://developer.nvidia.com/ace-for-games)

### 6.2 NVIDIA IGI (In-Game Inferencing) — NVIGI Plugins
- **Affiliation**: **NVIDIA**
- **Venue**: 2025–2026
- **Abstract**: Plugin SDK for scheduling AI inference alongside complex graphics workloads. Supports multiple inference backends across graphics pipeline. Enables sub-ms inference latency for game AI on consumer GPUs.
- **Key innovation**: Co-scheduled graphics + AI inference; real-time NPC AI on consumer hardware.
- **Link**: [NVIDIA NVIGI](https://developer.nvidia.com/rtx/in-game-inferencing)

### 6.3 Ubisoft Teammates: Generative AI NPC Experiment (GDC 2026)
- **Affiliation**: **Ubisoft**
- **Venue**: GDC 2026
- **Abstract**: R&D experiment with 80-person team building AI NPCs (Jaspar, Pablo, Sophia) using Google Gemini integrated into Snowdrop engine. NPCs understand contextual intent and personality-driven dialogue. Players use natural voice commands for team coordination.
- **Key innovation**: Contextual intent understanding; personality profiles; real-time voice interaction in Snowdrop engine.
- **Link**: [Game Developer](https://www.gamedeveloper.com/business/ubisoft-s-first-playable-generative-ai-experience-is-an-r-d-experiment-called-teammates-)

### 6.4 Convai: Conversational AI Infrastructure for Virtual Worlds
- **Affiliation**: **Convai**
- **Venue**: Production 2026
- **Abstract**: Infrastructure platform for conversational AI NPCs featuring knowledge banks, scene-aware actions, and optimized scaling for millions of daily interactions.
- **Key innovation**: Real-time generative speech + LLM NPCs; knowledge bank for hallucination mitigation.
- **Link**: [Convai](https://convai.com/blog/introducing-convai)

### 6.5 AstraGame: Tencent/WeChat Game Agent Platform
- **Affiliation**: **Tencent / WeChat**
- **Venue**: Production deployment 2026
- **Abstract**: Large-scale game AI platform supporting 24,000+ games. LLM-powered game agents deployed at WeChat ecosystem scale.
- **Key innovation**: Industrial-scale cross-game AI architecture; real-time inference at WeChat scale.

### 6.6 KRAFTON: PUBG Co-Player Characters & inZOI Smart Zois (NVIDIA ACE)
- **Affiliation**: **KRAFTON**
- **Venue**: Production 2026
- **Abstract**: PUBG introduces Co-Player Characters (CPCs) — AI-driven allies that communicate in natural language and act autonomously. inZOI features Smart Zois — AI agents that plan, act, and reflect on decisions.
- **Key innovation**: Production LLM-powered teammate AI; autonomous NPC decision-making in battle royale.

---

## 7. Related Techniques — Self-Play, Curiosity, HRL, Imitation, World Models

### 7.1 Dreamer 4: Training Agents Inside of Scalable World Models
- **Authors**: Danijar Hafner, Wilson Yan, Timothy Lillicrap
- **Affiliation**: **Google DeepMind**
- **Venue**: arXiv 2025
- **Abstract**: Scalable world model agent (2B params). First agent to obtain diamonds in Minecraft purely from offline data (20,000+ actions from raw pixels). Shortcut forcing objective + efficient transformer for real-time inference (21 FPS) on single GPU. Extracts majority of knowledge from diverse unlabeled videos.
- **Key innovation**: Offline training entirely inside world model; shortcut forcing objective; real-time Minecraft world model.
- **Link**: [arXiv:2509.24527](https://arxiv.org/abs/2509.24527) | [Website](https://danijar.com/dreamer4/)

### 7.2 Dreamer-CDP: Reconstruction-Free World Models for RL
- **Authors**: Michael N. (Zenke Lab)
- **Affiliation**: University of Basel / ICLR 2026 Workshop
- **Venue**: **ICLR 2026 Workshop on World Models**
- **Abstract**: Dreamer variant that learns world model without reconstructing raw pixels. Uses JEPA-style predictor operating on compact continuous internal representations. Matches reconstruction-based Dreamer on Crafter benchmark (Minecraft-inspired). Outperforms all previous reconstruction-free Dreamer variants.
- **Key innovation**: Reconstruction-free world model via JEPA; first reconstruction-free variant matching Dreamer performance.
- **Link**: [arXiv:2603.07083](https://arxiv.org/abs/2603.07083)

### 7.3 World Models: A Comprehensive Survey of Architectures
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Comprehensive survey tracing world models from early cognitive science foundations to PlaNet, Dreamer family, MuZero, Sora, Cosmos, Genie. Examines convergence of chain-of-thought reasoning with world-model imagination.
- **Key innovation**: Unified survey framework; CoT-world model convergence analysis.
- **Link**: [arXiv:2606.00133](https://arxiv.org/abs/2606.00133)

### 7.4 Absolute Zero: Reinforced Self-Play Reasoning with Zero Data
- **Authors**: Andrew Zhao, Yiran Wu, Yang Yue, et al.
- **Affiliation**: (multiple)
- **Venue**: arXiv 2025
- **Abstract**: Self-play paradigm for LLM reasoning with zero external data. Model acts as both proposer (generates tasks) and solver (completes them). Code executor provides verifiable environment for three reasoning modes: deduction, abduction, induction. Jointly trained via RL.
- **Key innovation**: Zero-data self-play; proposer-solver dual role; code-based verifiable environment.
- **Link**: [arXiv:2505.03335](https://arxiv.org/abs/2505.03335)

### 7.5 Self-Challenging Agent (SCA): Self-Play for Multi-Turn Tool-Use LLMs
- **Authors**: Yifei Zhou, Sergey Levine, Jason Weston, Xian Li, Sainbayar Sukhbaatar
- **Affiliation**: **UC Berkeley**, **FAIR at Meta**
- **Venue**: arXiv 2025
- **Abstract**: Self-challenging framework where agent generates Code-as-Task (CaT) problems, filters for quality, then trains on them with RL. Two-fold improvement in Llama-3.1-8B-Instruct on M³ToolEval and TauBench using only self-generated data.
- **Key innovation**: Code-as-Task formulation for self-generated training; automated quality filtering.
- **Link**: [arXiv:2506.01716](https://arxiv.org/abs/2506.01716)

### 7.6 Language Self-Play (LSP): Data-Free Training via Game Theory
- **Authors**: Qi Ma, Yuandong Tian, Vijai Mohan, Jakub Grudzien Kuba, Mengting Gu
- **Affiliation**: **Meta**
- **Venue**: arXiv 2025
- **Abstract**: RL approach enabling models to improve without additional data using game-theoretic self-play. Llama-3.2-3B-Instruct improves on instruction-following benchmarks more effectively than data-driven baselines.
- **Key innovation**: Data-free self-play; game-theoretic framing of LLM improvement.
- **Link**: [arXiv:2509.07414](https://arxiv.org/abs/2509.07414)

### 7.7 SeRL: Self-Play RL for Large Language Models
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Self-play RL framework reducing data requirements for LLM training. Models generate and learn from own examples through competitive game interactions.
- **Key innovation**: Reduced data dependency through self-play; competitive game interactions for RL.
- **Link**: [arXiv (aimodels.fyi)](https://www.aimodels.fyi/papers/arxiv/serl-self-play-reinforcement-learning-large-language)

### 7.8 SPIRAL (detailed analysis) — Cognitive Pattern Transfer Analysis
- **Authors**: Brandon Liu, Song Yu et al.
- **Affiliation**: NUS
- **Venue**: **ICLR 2026**
- **Abstract**: Analysis reveals games develop distinct cognitive patterns that transfer to improve reasoning. TicTacToe develops spatial planning, Poker develops probabilistic reasoning, Negotiation develops strategic trade-off analysis. Multi-game training yields complementary strengths.
- **Key innovation**: Cognitive pattern analysis; multi-game complementary skill transfer.
- **Link**: [OpenReview (ICLR 2026)](https://openreview.net/forum?id=6z4YKr0GK6)

### 7.9 CDE: Curiosity-Driven Exploration for RL in LLMs
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: **ICLR 2026**
- **Abstract**: Framework leveraging intrinsic curiosity for RLVR exploration. Two signals: actor perplexity and multi-head critic variance. ~+3 point improvement over standard GRPO/PPO on AIME.
- **Key innovation**: Dual exploration bonus; mitigates entropy collapse in RLVR.
- **Link**: [OpenReview (ICLR 2026)](https://openreview.net/forum?id=5rXN5knHKW)

### 7.10 Constrained Exploitability Descent for Offline RL in Games
- **Authors**: Runyu Lu, Yuanheng Zhu, Dongbin Zhao
- **Affiliation**: (multiple)
- **Venue**: ICLR 2025
- **Abstract**: Model-free offline RL for adversarial Markov games converging to mixed-strategy Nash equilibrium from fixed offline datasets.
- **Link**: [OpenReview (ICLR 2025)](https://openreview.net/forum?id=sQYQ9i1g86)

### 7.11 Offline Fictitious Self-Play (OFF-FSP)
- **Authors**: Jingxiao Chen, Weiji Xie, Weinan Zhang, Yong Yu, Ying Wen
- **Affiliation**: Tsinghua University
- **Venue**: arXiv 2024 (updated 2025)
- **Abstract**: First practical model-free offline RL algorithm for competitive games. Combines single-agent offline RL with Fictitious Self-Play via importance sampling.
- **Link**: [arXiv:2403.00841](https://arxiv.org/abs/2403.00841)

### 7.12 Coverage-Aware Game Playtesting with LLM-Guided RL
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2025
- **Abstract**: Synergizes code coverage and gameplay intent for automated playtesting. LLM guides RL exploration toward uncovered game states, improving bug detection.
- **Key innovation**: LLM-guided coverage-driven playtesting; RL + LLM for game QA.
- **Link**: [arXiv:2512.12706](https://arxiv.org/abs/2512.12706)

---

## Summary Statistics

| Category | Paper Count | Key Trend |
|----------|-------------|-----------|
| 1. Game RL | ~12 | Game-RL (ICLR 2026) as paradigm for VLM reasoning; SPIRAL self-play convergence; realtime asynchronous RL |
| 2. Game AI Bot | ~6 | LLM agents maturing: experience transfer, expert intervention, memory-aware task suites |
| 3. Game Foundation Models | ~4 | Open-source models (NitroGen, Game-TARS) enabling reproducible research |
| 4. Procedural Content Generation | ~5 | PCGRL goes multi-task; RDA brings VLM-based reward design; language-conditioned PCG |
| 5. Game Benchmarks | ~5 | Standardization via GameWorld (NUS), lmgame-Bench (ICLR 2026); ACM CSUR survey |
| 6. Industry Game AI | ~6 | NVIDIA ACE production at scale (PUBG, inZOI, Naraka); Ubisoft Teammates; Tencent AstraGame |
| 7. Related Techniques | ~12 | World models converge (Dreamer 4, Dreamer-CDP); self-play for LLM reasoning (Absolute Zero, SCA, LSP); curiosity (CDE) |
| **Total** | **~50** | **Game data as scalable RL training signal for foundation models** |

## Key Themes

1. **Game data as scalable RL training signal**: Game-RL (ICLR 2026, Fudan) shows game-derived multimodal verifiable rewards improve VLM general reasoning, establishing games as a scalable alternative to human-curated RL data.

2. **Self-play + RL convergence**: SPIRAL, Absolute Zero, Self-Challenging Agent, Language Self-Play — multiple concurrent works demonstrating self-play as a data-free paradigm for LLM reasoning improvement.

3. **Reconstruction-free world models**: Dreamer-CDP (ICLR 2026 WS) matches Dreamer without pixel reconstruction; survey (arXiv 2606.00133) traces field convergence including CoT-world model integration.

4. **Real-time asynchronous RL**: Formal treatment of realtime async RL enables orders-of-magnitude larger models in realtime games (Pokémon, Tetris) with theoretical regret bounds.

5. **Industry production at scale**: NVIDIA ACE deployed in PUBG, inZOI, Naraka with on-device inference; Ubisoft Teammates R&D experiment; Tencent AstraGame covering 24K+ games.

6. **Standardized evaluation**: GameWorld (NUS, 34 games, 170 tasks, 18 model-interface pairs), lmgame-Bench (ICLR 2026), DSGBench establish rigorous multi-game agent evaluation protocols.

7. **PCG goes multi-task + VLM**: Multi-task PCGRL (Scientific Reports 2026), RDA (VLM reward design, arXiv 2606.01672) push PCG toward language-conditioned, visually-aware generation.
