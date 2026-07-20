---
title: "Game RL & Game AI Bot — Daily Paper Digest (July 20, 2026)"
type: synthesis
created: 2026-07-20
updated: 2026-07-20
tags: [game-rl, game-ai, self-play, foundation-model, pcg, benchmark, world-model, llm-agent]
---

# Game RL & Game AI Bot — Daily Paper Digest (July 20, 2026)

> Curated papers across 7 categories: Game RL, Game AI Bot, Foundation Models, PCG, Benchmarks, World Models, Related Techniques.

---

## 1. Game RL — Reinforcement Learning in Games

| # | Title | Authors | Affiliation | Venue | arXiv |
|---|-------|---------|-------------|-------|-------|
| 1 | **SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL** | Bo Liu, Leon Guertler, Simon C.H. Yu, Zichen Liu, Penghui Qi, Daniel Balcells, et al. | - | ICLR 2026 | [2506.24119](https://arxiv.org/abs/2506.24119) |
| 2 | **Stratagem: Learning Transferable Reasoning via Trajectory-Modulated Game Self-Play** | Xiachong Feng, Deyi Yin, Xiaocheng Feng, Yi Jiang, Libo Qin, Yangfan Ye, et al. | - | arXiv 2026 | [2604.17696](https://arxiv.org/abs/2604.17696) |
| 3 | **MARS: Reinforcing Multi-Agent Reasoning of LLMs through Self-Play in Strategic Games** | Hui Yuan, Zhe Xu, Zheyue Tan, Xianhao Yi, Guang Mo, Kaiwen Long, et al. | Tsinghua (THU-NICS) | arXiv 2025 | [2510.15414](https://arxiv.org/abs/2510.15414) |
| 4 | **MEMO: Memory-augmented MOdel Context Optimization for Multi-Turn LLM Games** | - | - | arXiv 2026 | [2603.09022](https://arxiv.org/abs/2603.09022) |
| 5 | **π-Play: Multi-Agent Self-Play via Privileged Self-Distillation without External Data** | - | - | arXiv 2026 | [2604.14054](https://arxiv.org/abs/2604.14054) |
| 6 | **Multi-Agent Evolve (MAE): LLM Self-Improve through Co-evolution** | - | - | arXiv 2025 | [2510.23595](https://arxiv.org/abs/2510.23595) |
| 7 | **Foundation Model Self-Play (FMSP): Open-Ended Strategy Innovation** | Aaron Dharna, Cong Lu, Jeff Clune | - | arXiv 2025 | [2507.06466](https://arxiv.org/abs/2507.06466) |

### Key Innovations

**SPIRAL** (ICLR 2026): Self-play on zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation) generates automatic curriculum of stronger opponents. Introduces role-conditioned advantage estimation (RAE) for multi-agent training. Multi-game training yields strongest results — up to 10% improvement across 8 reasoning benchmarks on Qwen/Llama families. Even DeepSeek-R1-Distill-Qwen-7B benefits.

**Stratagem**: Addresses two barriers to reasoning transfer — domain specificity and contextual stasis. Introduces Reasoning Transferability Coefficient (φ) that measures abstraction level, and Reasoning Evolution Reward (ψ) that incentivizes progressive reasoning. Experiments show strong gains on competition-level mathematics. Trained on TextArena games with Qwen3-4B.

**MARS**: End-to-end RL for multi-agent reasoning in cooperative AND competitive games. Turn-level advantage estimator for fine-grained credit assignment, agent-specific advantage normalization. Trained on Qwen3-4B, achieves up to 28.7% improvement in held-out games. When integrated into multi-agent systems: 10.0% on AIME, 12.5% on GPQA-Diamond.

**MEMO**: Weight-free self-play framework using persistent memory + tournament-style prompt evolution + prioritized replay. Raises mean win rate from 25.1%→49.5% (GPT-4o-mini) and 20.9%→44.3% (Qwen-2.5-7B) using 2,000 self-play games per task — 19× fewer than RL baselines. Memory is the dominant mechanism.

**π-Play**: Multi-agent self-evolution framework where examiner generates tasks with question construction paths (QCPs), teacher uses QCP as privileged context for dense self-distillation. Transforms sparse-reward self-play into dense-feedback self-evolution. Outperforms supervised baselines by 6.2–14.5% across model scales.

**MAE**: Proposer–Solver–Judge triad from single LLM, jointly trained via RL. Self-rewarding loop without external verifiers. Average 4.54% improvement on Qwen2.5-3B-Instruct across math, coding, reasoning, general knowledge.

**FMSP**: Foundation models generate code-based policies in multi-agent settings. Three variants: Vanilla FMSP (exploitation), Novelty-Search Self-Play (NSSP, exploration), Quality-Diversity Self-Play (QDSP, hybrid). In Car Tag, surpasses human-designed strategies. In Gandalf, auto-red-teams LLM through 6 defense levels.

---

## 2. Game AI Bot — LLM-Powered Game Agents

| # | Title | Authors | Affiliation | Venue | arXiv |
|---|-------|---------|-------------|-------|-------|
| 1 | **Sensi: Learn One Thing at a Time — Curriculum-Based Test-Time Learning for LLM Game Agents** | Mohsen Arjmandi | - | arXiv 2026 | [2603.17683](https://arxiv.org/abs/2603.17683) |
| 2 | **Orchestrated Reality: LLM-Driven World Simulation as a Parameterized-Action POMDP** | Y Huang, Chenmiao Li, Chaowei Fang | - | arXiv 2026 | [2606.16014](https://arxiv.org/abs/2606.16014) |
| 3 | **Bounded Autonomy: Controlling LLM Characters in Live Multiplayer Games** | - | - | arXiv 2026 | [2604.04703](https://arxiv.org/abs/2604.04703) |
| 4 | **COSPLAY: Co-Evolving LLM Decision and Skill Bank Agents for Long-Horizon Tasks** | Xiyang Wu, Zongxia Li, Guangyao Shi, Alexander Duffy, Tyler Marques, Matthew Olson, et al. | - | arXiv 2026 | [2604.20987](https://arxiv.org/abs/2604.20987) |
| 5 | **LLM Reasoner and Automated Planner: A New NPC Approach** | - | - | arXiv 2025 | [2501.10106](https://arxiv.org/abs/2501.10106) |
| 6 | **Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with LLMs** | - | NUS | arXiv 2026 | [2604.21896](https://arxiv.org/abs/2604.21896) |
| 7 | **HexMachina: Self-Evolving LLM Agent Framework for Strategic Planning** | - | - | arXiv 2025 | [2506.04651](https://arxiv.org/abs/2506.04651) |
| 8 | **Psy-CoT: Psychology-Grounded Reasoning and Role-Aware Policy Optimization** | - | - | arXiv 2026 | [2606.27025](https://arxiv.org/abs/2606.27025) |

### Key Innovations

**Sensi** (ARC-AGI-3): Two-player architecture (Observer + Actor) separates perception from action. Curriculum-based learning with state machine + SQLite database-as-control-plane. Sensi v1 solves 2 ARC-AGI-3 levels; v2 achieves 50–94× sample efficiency over baselines (32 vs 1,600–3,000 actions). Failure mode diagnosed as self-consistent hallucination cascade in perception layer.

**Orchestrated Reality**: Formalizes LLM-driven game world as Parameterized-Action POMDP. State = tree of canonical JSON entities; actions = (intent_kind, structured_params). Agent observes narrative projection of state. Plan-Diff-Validate-Apply (PDVA) pipeline commits schema-validated JSON deltas. Catalogue of 15 incidents from real deployment.

**Bounded Autonomy**: Control architecture for LLM characters in live multiplayer with three interfaces: agent-agent (reply-chain decay), agent-world (embedding-based action grounding with fallback), player-agent (whisper soft-steering). Deployed in live multiplayer social game with 40-second behavior heartbeat per character.

**COSPLAY**: LLM decision agent retrieves skills from learnable skill bank; skill pipeline discovers reusable skills from unlabeled rollouts. 8B model achieves 25.1% average reward improvement over 4 frontier LLMs on single-player games. Skills include contracts for reusability.

**Nemobot**: Extends Shannon's taxonomy of game-playing machines with LLMs. Dictionary-based (compressed state-action), rigorously solvable (mathematical reasoning), heuristic-based (minimax + crowd-sourced), learning-based (RLHF + self-critique). Programmable web-based platform for game agent development.

**HexMachina**: Separates environment discovery (API induction) from strategy improvement (player code evolution). Learns Catan from scratch, achieves 54% win rate vs strongest human-crafted AlphaBeta baseline. Artifact-centric continual learning — LLM designs strategy, compiled code executes it consistently.

**Psy-CoT**: Chain-of-thought decomposes into Interaction Perception, Psychological Empathy, Logical Construction. Role-Aware Policy Optimization (RAPO) uses profile–token mutual information for asymmetric gradient weighting. Improvements of 13.7–40.1% over untrained baseline on CoSER across 3 model families.

---

## 3. Game Foundation Models — Generalist Gaming Agents

| # | Title | Authors | Affiliation | Venue | arXiv |
|---|-------|---------|-------------|-------|-------|
| 1 | **NitroGen: An Open Foundation Model for Generalist Gaming Agents** | Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, et al. | NVIDIA / MineDojo | CVPR 2026 | [2601.02427](https://arxiv.org/abs/2601.02427) |
| 2 | **Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents** | Zihao Wang, Xujing Li, Yining Ye, Junjie Fang, et al. | ByteDance | arXiv 2025 | [2510.23691](https://arxiv.org/abs/2510.23691) |
| 3 | **Pixels to Play (P2P): A Foundation Model for 3D Gameplay** | Yuguang Yue, Chris Green, Samuel Hunt, Irakli Salia, Wenzhe Shi, Jonathan J. Hunt | Google DeepMind? | arXiv 2025 | [2508.14295](https://arxiv.org/abs/2508.14295) |
| 4 | **Open MIND: Scaling Behavior Cloning for Real-Time Video Game Playing** | Yuguang Yue, Irakli Salia, Samuel Hunt, Chris Green, Wenzhe Shi, Jonathan J. Hunt | - | arXiv 2026 | [2601.04575](https://arxiv.org/abs/2601.04575) |
| 5 | **Towards Generalist Game Players: An Investigation of Foundation Models in the Game Multiverse** | Kuan Zhang, Dongchen Liu, Qiyue Zhao, Tianyu Xin, Yue Su, Haisheng Wang, et al. | Tsinghua | arXiv 2026 | [2605.09965](https://arxiv.org/abs/2605.09965) |

### Key Innovations

**NitroGen** (CVPR 2026): Vision-action foundation model trained on 40,000 hours of gameplay videos across 1,000+ games. Internet-scale dataset extracted from publicly available gameplay videos with overlay input commands. 500M parameter flow-matching GR00T architecture. 52% relative improvement in task success rate when fine-tuned vs from-scratch. Universal Gymnasium API for any commercial game. Open-source dataset, evaluation suite, and model weights.

**Game-TARS** (ByteDance): Unified keyboard-mouse action space enables large-scale continual pre-training across OS, web, and simulation games. Pre-trained on 500B+ tokens. Decaying continual loss to reduce causal confusion. Sparse-Thinking for reasoning depth/cost balance. ~2× success rate over previous SOTA on Minecraft; close to fresh humans on unseen web 3D games; outperforms GPT-5, Gemini-2.5-Pro, Claude-4-Sonnet in FPS benchmarks.

**Pixels2Play-0.1**: Foundation model for 3D gameplay via behavior cloning. Labeled demonstrations from instrumented gameplay + unlabeled public videos with imputed actions via inverse-dynamics model. Decoder-only transformer with auto-regressive action output. Latency-friendly on single consumer GPU. Competent play across Roblox and MS-DOS titles.

**Open MIND (P2P)**: 8,300+ hours of high-quality human gameplay dataset. Open-source recipe for real-time game playing foundation model on consumer GPU. Systematic study of behavior cloning scaling laws — increasing data and depth yields more causal policy. Up to 1.2B parameters studied.

**Generalist GP Survey** (Tsinghua): Four-era taxonomy — symbolic/RL → foundation model players → creator stage. Five interdependent pillars: Dataset, Model, Harness, Benchmark. Five fundamental trade-offs identified. Five-level roadmap from single-game mastery to ultimate creator stage.

---

## 4. Procedural Content Generation (PCG)

| # | Title | Authors | Affiliation | Venue | arXiv |
|---|-------|---------|-------------|-------|-------|
| 1 | **CreativeGame: Mechanic-Aware Creative Game Generation** | Hongnan Ma, Han Wang, Shenglin Wang, et al. | - | arXiv 2026 | [2604.19926](https://arxiv.org/abs/2604.19926) |
| 2 | **VIPCGRL: Human-Aligned Procedural Level Generation RL via Text-Level-Sketch Shared Representation** | In-Chang Baek, Seoyoung Lee, Sung-Hyun Kim, et al. | - | arXiv 2025 | [2508.09860](https://arxiv.org/abs/2508.09860) |
| 3 | **Multiverse: Language-Conditioned Multi-Game Level Blending via Shared Representation** | In-Chang Baek, Jiyun Jung, Geum-Hwan Hwang, et al. | - | arXiv 2026 | [2603.26782](https://arxiv.org/abs/2603.26782) |
| 4 | **AutoUE: Automated Generation of 3D Games in Unreal Engine via Multi-Agent Systems** | - | - | arXiv 2026 | [2603.07106](https://arxiv.org/abs/2603.07106) |
| 5 | **OpenGame: Open Agentic Coding for Games** | Yilei Jiang, Jinyuan Hu, Qianyin Xiao, et al. | - | arXiv 2026 | [2604.18394](https://arxiv.org/abs/2604.18394) |
| 6 | **High Dimensional PCG (HDPCG)** | - | - | arXiv 2026 | [2602.18943](https://arxiv.org/abs/2602.18943) |
| 7 | **Learning Local Constraints for RL Content Generators** | - | - | arXiv 2026 | [2605.13570](https://arxiv.org/abs/2605.13570) |
| 8 | **A Database-Driven Framework for 3D Level Generation with LLMs** | Kaijie Xu, Clark Verbrugge | - | arXiv 2025 | [2508.18533](https://arxiv.org/abs/2508.18533) |

### Key Innovations

**CreativeGame**: Multi-agent system for iterative HTML5 game generation. 7 agents (10 roles), lineage-scoped memory for cross-version experience, mechanic-guided planning loop, runtime validation. 71 stored lineages, 88 nodes, 774-entry mechanic archive. CreativeProxyReward uses programmatic signals rather than pure LLM judgment.

**VIPCGRL**: Three modalities (text, level, sketches) via quadruple contrastive learning across modalities and human-AI styles. Auxiliary reward based on embedding similarity aligns policy to human-likeness. Outperforms baselines in both quantitative metrics and human evaluations.

**Multiverse**: Language-conditioned multi-game level generator. Threshold-based multi-positive contrastive supervision links semantically related levels across games. Controllable cross-game blending through latent interpolation and zero-shot generation from compositional text.

**AutoUE**: Multi-agent system for end-to-end 3D game generation in Unreal Engine. Model retrieval (858K 3D models), scene generation via PCG graphs, gameplay C++ code, interactive objects, automated play-testing. RAG grounds agents with UE tool documentation.

**OpenGame**: First open-source agentic framework for end-to-end web game creation. GameCoder-27B specialized via continual pre-training + SFT + execution-grounded RL. Game Skill = Template Skill (project skeletons) + Debug Skill (verified fixes). OpenGame-Bench evaluation via headless browser + VLM judging.

**HDPCG**: Elevates non-geometric gameplay dimensions to first-class coordinates. Direction-Space: 4D (x,y,z,ℓ) with gravity inversion and parallel-world switching. Direction-Time: time-expanded graphs for action semantics. Unity case studies with VVVVVV-like and Dishonored 2-like mechanics.

---

## 5. Game Benchmarks

| # | Title | Authors | Affiliation | Venue | arXiv |
|---|-------|---------|-------------|-------|-------|
| 1 | **SciCrafter: Can Current Agents Close the Discovery-to-Application Gap? (Minecraft)** | Zhou Ziheng, Huacong Tang, Jinyuan Zhang, et al. | - | arXiv 2026 | [2604.24697](https://arxiv.org/abs/2604.24697) |
| 2 | **Agentick: A Unified Benchmark for General Sequential Decision-Making Agents** | - | - | arXiv 2026 | [2605.06869](https://arxiv.org/abs/2605.06869) |
| 3 | **OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics** | Mingxian Lin, Shengju Qian, Yuqi Liu, et al. | - | arXiv 2026 | [2606.09826](https://arxiv.org/abs/2606.09826) |
| 4 | **lmgame-Bench: How Good are LLMs at Playing Games?** | Lanxiang Hu, Ming Huo, Yuxuan Zhang, et al. | - | arXiv 2025 | [2505.15146](https://arxiv.org/abs/2505.15146) |
| 5 | **TextAtari: 100K Frames Game Playing with Language Agents** | Wenhao Li, Wenwu Li, Chuyun Shen, et al. | - | arXiv 2025 | [2506.04098](https://arxiv.org/abs/2506.04098) |
| 6 | **VideoGameBench: Can VLMs Complete Popular Video Games?** | Alex L. Zhang, Thomas L. Griffiths, Karthik R. Narasimhan, Ofir Press | - | arXiv 2025 | [2505.18134](https://arxiv.org/abs/2505.18134) |
| 7 | **GameWorld: Standardized and Verifiable Evaluation of Multimodal Game Agents** | - | NUS | arXiv 2026 | [2604.07429](https://arxiv.org/abs/2604.07429) |
| 8 | **TeamCraft: Multi-Modal Multi-Agent Benchmark in Minecraft** | - | - | arXiv 2024 | [2412.05255](https://arxiv.org/abs/2412.05255) |

### Key Innovations

**SciCrafter**: Parameterized redstone circuit tasks in Minecraft. Four capacities: knowledge gap identification, experimental discovery, knowledge consolidation, application. GPT-5.2/Gemini-3-Pro/Claude-Opus-4.5 all plateau at ~26% success rate. Bottleneck shifting from solving problems right to raising the right problems.

**Agentick**: 37 procedurally generated gridworld tasks, 6 capability categories, 5 observation modalities, 4 difficulty levels. No single paradigm dominates: PPO leads planning (0.402) and multi-agent (0.432); GPT-5 mini leads navigation (0.456) and generalization (0.437). Hybrid FM+RL architectures needed.

**OmniGameArena**: 12 UE5 games (Solo 7, PvP 3, Coop 2) with unified action interfaces. Improvement Dynamics Curve (IDC) — agentic reflector LLM autonomously refines skill prompt across rounds. Beyond cold-start leaderboard, exposes score evolution and cross-variant generalization.

**lmgame-Bench**: 6 classical video games with perception/memory scaffolds. Across 13 models, o3/o1 top-2. Gaming performance correlates with unique blends of capabilities. RL on single game transfers to unseen games and external planning tasks (BlocksWorld, WebShop).

**TextAtari**: 23 classic Atari games translated to rich text descriptions, up to 100K steps. Bridges sequential decision-making with NLP. Tests reasoning, planning over extended horizons with raw primitive actions.

**VideoGameBench**: 10 popular 1990s games + 3 secret games. VLMs interact with raw visual inputs only. Best models (Gemini 2.5 Pro, Claude 3.7 Sonnet) complete only 0.48% of VideoGameBench and 1.6% of Lite (paused emulator).

**GameWorld**: 34 browser games, 170 tasks, state-verifiable evaluation via structured JavaScript bridge. Two interfaces: Computer-Use Agents vs Generalist Multimodal Agents via Semantic Action Parsing. Best agents far from human capabilities.

**TeamCraft**: 55K task variants specified by multi-modal prompts in Minecraft. Procedurally-generated expert demonstrations. Evaluates generalization to novel goals, scenes, and unseen numbers of agents.

---

## 6. World Models for Games

| # | Title | Authors | Affiliation | Venue | arXiv |
|---|-------|---------|-------------|-------|-------|
| 1 | **Mind-Studio: Executable World Models with Lookahead Evaluation for Partially Observable Games** | - | - | arXiv 2026 | [2606.16070](https://arxiv.org/abs/2606.16070) |
| 2 | **Distilling Game Code World Model Generation into Lightweight LLMs** | - | - | arXiv 2026 | [2605.24375](https://arxiv.org/abs/2605.24375) |
| 3 | **Code World Models for General Game Playing** | Wolfgang Lehrach, Daniel Hennes, Miguel Lázaro-Gredilla, et al. | DeepMind | arXiv 2025 | [2510.04542](https://arxiv.org/abs/2510.04542) |
| 4 | **Offline RL with Universal Horizon Models (UHM)** | - | - | arXiv 2026 | [2605.15603](https://arxiv.org/abs/2605.15603) |
| 5 | **JOWA: Jointly-Optimized World-Action Model Pretraining for Offline MBRL** | Jie Cheng, Ruixi Qiao, Yingwei Ma, et al. | - | arXiv 2024 | [2410.00564](https://arxiv.org/abs/2410.00564) |

### Key Innovations

**Mind-Studio**: Synthesizes executable pygame-style world models from state-action-next-state trajectories using LLMs. Entropy-selected traces + game skill file. K-step lookahead fidelity protocol. On Montezuma's Revenge: chosen-action NSP from 0.3% (PoE-World) → 48.7%.

**GameCWM Distillation**: SFT + RLVR pipeline to distill GameCWM generation into Qwen2.5-3B-Instruct. 30-game dataset covering perfect and imperfect information. Hierarchical verification framework based on game-theoretic properties. Reduces dependency on frontier models and iterative refinement.

**Code World Models (DeepMind)**: LLM translates natural language rules + trajectories into executable Python world model (state transitions, legal moves, termination, inference functions for hidden states). Combined with MCTS/ISMCTS for planning. Outperforms or matches Gemini 2.5 Pro in 9/10 games. Novel "regularized autoencoder" approach for imperfect information games.

**UHM**: Generalizes geometric horizon models — samples n-step future states with arbitrary horizon distributions. Winsorized horizon distribution stabilizes training. Outperforms baselines on 100 OGBench tasks, especially on highly suboptimal datasets and long-horizon reasoning.

**JOWA**: 150M parameter jointly-optimized world-action model pretrained on 20 Atari games (6B tokens). Parallelizable planning algorithm. 78.9% human-level on pretrained games with 10% data. Sample-efficient transfer to novel games with only 5K offline fine-tuning transitions (~4 trajectories).

---

## 7. Related Techniques

### Curiosity-Driven Exploration
- Curiosity-driven exploration remains a key technique for sparse-reward game environments, with recent work on curiosity-based task generation (CuES) and intrinsic curiosity modules (ICM) for action games

### Hierarchical RL
- Hierarchical planning with latent world models achieves 70% success on real robot tasks
- HiPER (hierarchical plan-execute) achieves 97.4% on ALFWorld (ICML 2026)

### Imitation Learning in Games
- Behavior cloning at scale: 8,300+ hours (Open MIND/Pixels2Play), 40,000 hours (NitroGen)
- Scaling laws for BC in game domains — deeper networks + more data → more causal policies

### World Models
- World models maturing rapidly: executable code world models, multiplayer 5B-parameter models (Rocket League 20fps), self-supervised sim-to-real transfer (RWML)
- Code-as-world-model paradigm: LLM generates game implementations compatible with MCTS solvers

### Offline RL
- JOWA: jointly-optimized world-action models for multi-game offline RL (150M params, 6B tokens)
- UHM: universal horizon models for scalable offline MBRL
- Policy-Driven World Model Adaptation with Stackelberg dynamics for robust offline RL

### Reward Shaping
- Proxy rewards for game content generation (CreativeProxyReward)
- Verifiable rewards via execution-based verification for code world models
- Profile–token mutual information for asymmetric gradient weighting (RAPO)

---

## Key Themes & Trends

1. **Self-Play Generates Transferable Reasoning**: SPIRAL, Stratagem, MARSHAL/MARS demonstrate that game self-play develops cognitive patterns that transfer to mathematical reasoning, general reasoning, and code generation. Multi-game training yields strongest cross-domain transfer.

2. **Foundation Models at Internet Scale**: NitroGen (CVPR 2026, 40K hrs), Game-TARS (ByteDance, 500B tokens), Open MIND (8,300+ hrs open-source) — video game foundation models trained via behavior cloning on internet-scale gameplay data.

3. **Executable World Models via LLMs**: Mind-Studio (48.7% NSP on Montezuma), Code World Models (DeepMind, 9/10 games), GameCWM distillation — LLMs synthesize executable game simulations that enable classical planning (MCTS).

4. **Memory and Self-Evolution Critical**: MEMO (19× fewer games), COSPLAY (skill bank), MineEvolve, WISE — persistent memory and skill discovery are key to efficient adaptation in game environments.

5. **LLM Agents Still Far from Human**: SciCrafter (26% ceiling), VideoGameBench (0.48% completion), GameWorld (far from human), Agentick (no single paradigm dominates) — current frontier models struggle with long-horizon interactive reasoning.

6. **PCG + LLM Complementary**: CreativeGame (mechanic-aware iterative generation), AutoUE (end-to-end 3D in UE), OpenGame (GameCoder-27B), HDPCG (high-dimensional) — LLMs handle design intent, RL handles constraint satisfaction.

7. **Benchmark Explosion**: 8+ new game benchmarks this cycle — OmniGameArena (UE5 IDC), Agentick (37 tasks, 5 modalities), SciCrafter (discovery-to-application), lmgame-Bench (13 models, 6 games), TextAtari (100K frames), VideoGameBench (10 games), GameWorld (34 browser games), TeamCraft (55K Minecraft variants).

---

*Generated: 2026-07-20 | Sources: arXiv, CVPR 2026, ICLR 2026, ICML 2026*
