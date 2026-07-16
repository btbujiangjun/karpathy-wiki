---
title: "Game RL & Game AI Bot Daily Digest — 2026-07-16"
type: synthesis
created: 2026-07-16
updated: 2026-07-16
sources: []
tags: [game-rl, game-ai, self-play, multi-agent, foundation-models, pcg, benchmark, world-model, hierarchical-rl]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-07-16)

A curated survey of recent arXiv papers and proceedings on reinforcement learning in games, LLM-powered game agents, game foundation models, procedural content generation, game benchmarks, and related techniques.

---

## 1. Game RL — Self-Play & Multi-Agent Reinforcement Learning

### 1.1 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning

- **Authors:** Bo Liu, Leon Guertler, Simon C.H. Yu, Zichen Liu, Penghui Qi, Daniel Balcells, et al.
- **Affiliation:** (Multiple institutions)
- **Venue:** arXiv preprint, Jun 2025
- **Link:** https://arxiv.org/abs/2506.24119
- **Abstract & Key Innovations:**
  Introduces SPIRAL, a self-play framework where LLMs learn by playing multi-turn zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation) against improving versions of themselves. Proposes role-conditioned advantage estimation (RAE) for stabilizing multi-agent training. Produces reasoning capabilities that transfer broadly, improving up to 10% across 8 reasoning benchmarks on Qwen and Llama families. Multi-game training yields strongest results. Even DeepSeek-R1-Distill-Qwen-7B benefits.

### 1.2 Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games

- **Authors:** (Multi-institution team)
- **Venue:** arXiv preprint, May 2026
- **Link:** https://arxiv.org/abs/2605.04906
- **Abstract & Key Innovations:**
  Proposes Strat-Reasoner with a recursive reasoning paradigm where an agent's reasoning integrates other agents' reasoning processes. Uses centralized CoT comparison module for reward signals and hybrid advantage estimation. Achieves 22.1% average performance improvement across multi-agent games. Outperforms SPIRAL and MARSHAL on multiple benchmarks.

### 1.3 MARSHAL: Incentivizing Multi-Agent Reasoning via Self-Play with Strategic LLMs

- **Authors:** Hui Yuan, Zhe Xu, Zheyue Tan, Xianhao Yi, Guang Mo, Kaiwen Long, et al.
- **Venue:** arXiv preprint, Oct 2025
- **Link:** https://arxiv.org/abs/2510.15414
- **Abstract & Key Innovations:**
  End-to-end RL framework for multi-agent reasoning through self-play in cooperative and competitive games. Features turn-level advantage estimator for credit assignment and agent-specific advantage normalization. Up to 28.7% performance improvements in held-out games. Generalizes beyond games with up to 10.0% gains on AIME and 7.6% on GPQA-Diamond.

### 1.4 MEMO: Memory-augmented MOdel context optimization for Multi-Turn Multi-Agent LLM Games

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, Mar 2026
- **Link:** https://arxiv.org/abs/2603.09022
- **Abstract & Key Innovations:**
  Weight-free self-play framework coupling persistent memory bank with tournament-style prompt evolution and prioritized replay. Raises mean win rate from 25.1% to 49.5% for GPT-4o-mini across 5 text-based games. Uses 19× fewer environment interactions than RL baselines while reducing run-to-run variance by 7×.

### 1.5 OMAR: One Model, All Roles — Multi-Turn, Multi-Agent Self-Play RL for Conversational Social Intelligence

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, Feb 2026
- **Link:** https://arxiv.org/abs/2602.03109
- **Abstract & Key Innovations:**
  Single model role-plays all participants in conversation simultaneously through multi-turn self-play. Implements hierarchical advantage estimation for turn-level and token-level advantages. Evaluations in SOTOPIA and Werewolf games show emergent social intelligence (empathy, persuasion, compromise).

### 1.6 STRATAGEM: Learning Transferable Reasoning via Trajectory-Modulated Game Self-Play

- **Authors:** Xiachong Feng, Deyi Yin, Xiaocheng Feng, Yi Jiang, Libo Qin, Yangfan Ye, et al.
- **Venue:** arXiv preprint, Apr 2026
- **Link:** https://arxiv.org/abs/2604.17696
- **Abstract & Key Innovations:**
  Addresses two barriers to reasoning transfer from games: domain specificity and contextual stasis. Uses Reasoning Transferability Coefficient and Reasoning Evolution Reward. Shows substantial improvements in math reasoning, general reasoning, and code generation.

### 1.7 Reproducing AlphaZero on Tablut: Self-Play RL for an Asymmetric Board Game

- **Authors:** (Research team)
- **Venue:** arXiv preprint, Apr 2026
- **Link:** https://arxiv.org/abs/2604.05476
- **Abstract & Key Innovations:**
  Modifies AlphaZero architecture with separate policy/value heads for each player role while maintaining shared residual trunk. Addresses catastrophic forgetting between attacker/defender roles through C4 augmentation, larger replay buffers, and playing 25% of games against random past checkpoints. Achieves BayesElo 1235 over 100 self-play iterations.

### 1.8 QZero: Mastering the Game of Go with Self-play Experience Replay

- **Authors:** Jingbin Liu, Xuechun Wang
- **Venue:** arXiv preprint, Jan 2026
- **Link:** https://arxiv.org/abs/2601.03306
- **Abstract & Key Innovations:**
  Model-free RL algorithm that forgoes MCTS during training, learning Nash equilibrium through self-play and off-policy experience replay. Built on entropy-regularized Q-learning with single Q-value network. Trained tabula rasa for 5 months on 7 GPUs, achieves AlphaGo-comparable performance. First demonstration of model-free RL mastering Go.

### 1.9 π-Play: Multi-Agent Self-Play via Privileged Self-Distillation without External Data

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, Apr 2026
- **Link:** https://arxiv.org/abs/2604.14054
- **Abstract & Key Innovations:**
  Uses question construction paths (QCPs) from self-play as privileged information for self-distillation. Transforms sparse-reward self-play into dense-feedback self-evolution. Surpasses supervised search agents and improves evolutionary efficiency by 2–3× over conventional self-play.

### 1.10 SELF-REDTEAM: Chasing Moving Targets with Online Self-Play RL for Safer Language Models

- **Authors:** Mickel Liu, Liwei Jiang, Yancheng Liang, Simon Shaolei Du, Yejin Choi, Tim Althoff, et al.
- **Venue:** arXiv preprint, Jun 2025
- **Link:** https://arxiv.org/abs/2506.07468
- **Abstract & Key Innovations:**
  First fully online self-play MARL for continuous co-evolution of attacker and defender. Single policy self-plays both roles with hidden chain-of-thought. Theoretical safety guarantee from Nash equilibrium. Improves safety of RLHF-trained models by up to 95% across 14 benchmarks. Discovers 17.8% more diverse attacks.

---

## 2. Game AI Bot — LLM-Powered Game Agents

### 2.1 Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with LLMs

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, Apr 2026
- **Link:** https://arxiv.org/abs/2604.21896
- **Abstract & Key Innovations:**
  Extends Shannon's taxonomy of game-playing machines with LLMs. Implements four categories: dictionary-based, solvable, heuristic, and learning-based games. Nemobot provides programmable environment for tool-augmented generation and fine-tuning of strategic game agents. Demonstrates self-programming AI through crowdsourced learning.

### 2.2 COSPLAY: Co-Evolving LLM Decision and Skill Bank Agents for Long-Horizon Tasks

- **Authors:** Xiyang Wu, Zongxia Li, Guangyao Shi, Alexander Duffy, Tyler Marques, Matthew Olson, et al.
- **Venue:** arXiv preprint, Apr 2026
- **Link:** https://arxiv.org/abs/2604.20987
- **Abstract & Key Innovations:**
  Co-evolution framework where LLM decision agent retrieves skills from learnable skill bank while skill pipeline extracts reusable skills from unlabeled rollouts. 8B model achieves over 25.1% average reward improvement against four frontier LLM baselines on single-player game benchmarks.

### 2.3 Learning Game-Playing Agents with Generative Code Optimization

- **Authors:** Zhiyi Kuang, Ryan Rong, YuCheng Yuan, Allen Nie
- **Venue:** arXiv preprint, Aug 2025
- **Link:** https://arxiv.org/abs/2508.19506
- **Abstract & Key Innovations:**
  Policies represented as Python programs refined using LLMs. Self-evolving code with execution traces and natural language feedback. Competitive with deep RL baselines on Atari games with significantly less training time and fewer environment interactions.

### 2.4 Sensi: Learn One Thing at a Time — Curriculum-Based Test-Time Learning for LLM Game Agents

- **Authors:** Mohsen Arjmandi
- **Venue:** arXiv preprint, Mar 2026
- **Link:** https://arxiv.org/abs/2603.17683
- **Abstract & Key Innovations:**
  Two-player architecture separating perception from action. Curriculum-based learning with state machine and database-as-control-plane. LLM-as-judge with dynamic rubrics. Achieves 50–94× greater sample efficiency than comparable systems (32 vs. 1,600–3,000 action attempts).

### 2.5 AutoHarness: Improving LLM Agents by Automatically Synthesizing a Code Harness

- **Authors:** (Google DeepMind / Multi-institution)
- **Venue:** arXiv preprint, Mar 2026
- **Link:** https://arxiv.org/abs/2603.03329
- **Abstract & Key Innovations:**
  Gemini-2.5-Flash automatically synthesizes code harness using tree search with Thompson sampling. Prevents all illegal moves in 145 TextArena games. Smaller model outperforms Gemini-2.5-Pro. Harness-as-policy eliminates LLM at decision time, achieving highest average reward (0.870) on 16 1P games, beating GPT-5.2-High.

### 2.6 Agents of Change: Self-Evolving LLM Agents for Strategic Planning (HexMachina)

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, Jun 2025 (updated Oct 2025)
- **Link:** https://arxiv.org/abs/2506.04651
- **Abstract & Key Innovations:**
  Continual learning multi-agent system for Settlers of Catan. Separates environment discovery from strategy improvement. Learns from scratch and evolves players outperforming AlphaBeta baseline (54% win rate). Artifact-centric continual learning transforms LLMs from stepwise deciders to stable strategy designers.

### 2.7 FAMOU: Co-Evolutionary Mechanisms for LLM-Driven Strategy Evolution in Adversarial Games

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, Jun 2026
- **Link:** https://arxiv.org/abs/2606.10389
- **Abstract & Key Innovations:**
  Evaluator co-evolution, hierarchical deep evaluation, and weakness pressure for LLM code-level evolution. Outperforms OpenEvolve and ShinkaEvolve on MCTF 2026 3v3 maritime CTF. LLM generates tactical structures (lookahead search, EWMA interception) absent from seed strategies. 1st place hardware round-robin at AAMAS 2026 MCTF Competition.

### 2.8 PORTAL: Agents Play Thousands of 3D Video Games

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, Mar 2025
- **Link:** https://arxiv.org/abs/2503.13356
- **Abstract & Key Innovations:**
  LLM generates behavior trees in domain-specific language for thousands of FPS games. Hybrid policy with rule-based and neural network components. Dual-feedback: quantitative metrics + VLM mini-map analysis. Instantaneously deployable, human-interpretable policies with cross-game generalization.

---

## 3. Game Foundation Models

### 3.1 NitroGen: An Open Foundation Model for Generalist Gaming Agents

- **Authors:** Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, et al.
- **Affiliation:** NVIDIA / MineDojo
- **Venue:** CVPR 2026
- **Link:** https://arxiv.org/abs/2601.02427
- **Abstract & Key Innovations:**
  Vision-action foundation model trained on 40,000 hours of gameplay videos across 1,000+ games. Internet-scale dataset with automatic action extraction from input overlay videos. Multi-game benchmark (30 tasks, 10 games). 500M parameter model with flow-matching GR00T architecture. Fine-tuning achieves up to 52% relative improvement over from-scratch training. Open-source dataset, simulator, and weights.

### 3.2 Pixels2Play: Scaling Behavior Cloning Improves Causal Reasoning

- **Authors:** Yuguang Yue, Irakli Salia, Samuel Hunt, Chris Green, Wenzhe Shi, Jonathan J. Hunt
- **Venue:** arXiv preprint, Jan 2026
- **Link:** https://arxiv.org/abs/2601.04575
- **Abstract & Key Innovations:**
  Open recipe for training video game playing foundation model (1.2B params) on 8,300+ hours of human gameplay. Real-time inference on consumer GPU. Shows scaling laws: increasing model depth and data leads to more causal policies. Releases all data, code, and checkpoints under open license.

### 3.3 Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents

- **Authors:** Zihao Wang, Xujing Li, Yining Ye, Junjie Fang, Haoming Wang, Longxiang Liu, et al.
- **Venue:** arXiv preprint, Oct 2025
- **Link:** https://arxiv.org/abs/2510.23691
- **Abstract & Key Innovations:**
  Unified action space anchored to native keyboard-mouse inputs for large-scale continual pre-training across OS, web, and simulation games. Pre-trained on 500B tokens. Decaying continual loss reduces causal confusion. Sparse-Thinking balances reasoning depth and inference cost. 2× success rate on Minecraft, outperforms GPT-5/Gemini-2.5-Pro/Claude-4-Sonnet in FPS benchmarks.

### 3.4 Pixels to Play: A Foundation Model for 3D Gameplay (P2P-0.1)

- **Authors:** Yuguang Yue, Chris Green, Samuel Hunt, Irakli Salia, Wenzhe Shi, Jonathan J. Hunt
- **Venue:** arXiv preprint, Aug 2025
- **Link:** https://arxiv.org/abs/2508.14295
- **Abstract & Key Innovations:**
  Foundation model trained with behavior cloning: labeled demonstrations + unlabeled videos with imputed actions via inverse-dynamics model. Decoder-only transformer with auto-regressive action output. Competent play across Roblox and MS-DOS titles.

### 3.5 Towards Generalist Game Players: An Investigation of Foundation Models in the Game Multiverse

- **Authors:** Kuan Zhang, Dongchen Liu, Qiyue Zhao, Tianyu Xin, Yue Su, Haisheng Wang, et al.
- **Venue:** arXiv preprint, May 2026
- **Link:** https://arxiv.org/abs/2605.09965
- **Abstract & Key Innovations:**
  Comprehensive survey tracing generalist game player across four eras (symbolic → RL → foundation models → creator stage). Four pillars: Dataset, Model, Harness, Benchmark. Five-level roadmap from single-game mastery to simultaneous creation and evolution. Identifies five fundamental trade-offs bounding the system.

### 3.6 GameVerse: Can Vision-Language Models Learn from Video-based Reflection?

- **Authors:** Kuan Zhang, Dongchen Liu, Qiyue Zhao, Jinkun Hou, Xinran Zhang, Qinlei Xie, et al.
- **Venue:** arXiv preprint, Mar 2026
- **Link:** https://arxiv.org/abs/2603.06656
- **Abstract & Key Innovations:**
  Video game benchmark enabling reflective visual interaction loop with reflect-and-retry paradigm. Cognitive taxonomy spanning 15 games, dual action space, milestone evaluation. VLMs benefit most from combining failure trajectories and expert tutorials.

### 3.7 OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics

- **Authors:** Mingxian Lin, Shengju Qian, Yuqi Liu, Yi-Hua Huang, Yiyu Wang, Wei Huang, et al.
- **Venue:** arXiv preprint, Jun 2026
- **Link:** https://arxiv.org/abs/2606.09826
- **Abstract & Key Innovations:**
  12 Unreal Engine 5 games (Solo/PvP/Coop) with unified action interfaces. Improvement Dynamics Curve (IDC) with agentic-reflection harness. Beyond cold-start scores, exposes how scores evolve across reflection rounds and generalize to held-out variants.

---

## 4. Procedural Content Generation

### 4.1 IPCGRL: Language-Instructed Reinforcement Learning for Procedural Level Generation

- **Authors:** In-Chang Baek, Sunghyun Kim, Seo-Young Lee, Dong-Hyeon Kim, Kyung-Joong Kim
- **Venue:** arXiv preprint, Mar 2025
- **Link:** https://arxiv.org/abs/2503.12358
- **Abstract & Key Innovations:**
  Instruction-based PCG via RL with sentence embedding model. Fine-tunes task-specific embeddings for game-level conditions. 21.4% improvement in controllability and 17.2% in generalizability for unseen instructions.

### 4.2 WCRL: Learning Local Constraints for RL Content Generators

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, May 2026
- **Link:** https://arxiv.org/abs/2605.13570
- **Abstract & Key Innovations:**
  Combines Wave Function Collapse (WFC) with PCGRL. WFC constrains action space of PCGRL generator via local rules. Produces visually satisfying and playable puzzle-platform levels (Lode Runner) with desired global properties. Random collapse during training produces more robust policies.

### 4.3 AutoUE: Automated Generation of 3D Games in Unreal Engine via Multi-Agent Systems

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, Mar 2026
- **Link:** https://arxiv.org/abs/2603.07106
- **Abstract & Key Innovations:**
  Multi-agent system for end-to-end 3D game generation in UE: model retrieval (858K 3D models), scene generation via PCG graphs, gameplay code synthesis, and automated play-testing. RAG grounds agents with UE tool documentation. Game design patterns ensure correct code generation.

### 4.4 PCGRLLM: LLM-Driven Reward Design for PCG Reinforcement Learning

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, Feb 2026 (updated May 2026)
- **Link:** https://arxiv.org/abs/2502.10906
- **Abstract & Key Innovations:**
  Employs feedback mechanism and reasoning-based prompt engineering for story-to-reward generation. Evaluates with two state-of-the-art LLMs. Achieves human-comparable performance, reducing human dependency in game AI development.

### 4.5 AutoBG: A Board Game Design Assistant with Interactive Ideation

- **Authors:** Zizhen Li, Chuanhao Li, Yibin Wang, Jianwen Sun, Yukang Feng, Fanrui Zhang, et al.
- **Venue:** arXiv preprint, Jun 2026
- **Link:** https://arxiv.org/abs/2606.01976
- **Abstract & Key Innovations:**
  Four specialized modules: BG-Ideator (dialogue), BG-Realizer (rulebook generation), BG-Critic (design flaw diagnosis), BG-Persona (150 real player profiles). Built on 2.2K rulebooks and 180K player reviews. Outperforms GPT-5.4 on 207 held-out games.

### 4.6 Orchestrated Reality: LLM-Driven World Simulation as a Parameterized-Action POMDP

- **Authors:** Y Huang, Chenmiao Li, Chaowei Fang
- **Venue:** arXiv preprint, Jun 2026
- **Link:** https://arxiv.org/abs/2606.16014
- **Abstract & Key Innovations:**
  Treats LLM-driven game world as Parameterized-Action POMDP. Singleton orchestration agent (analogous to tabletop GM) owns canonical JSON world state. Plan-Diff-Validate-Apply pipeline with schema-validated JSON deltas. 15 illustrative incidents from real deployment.

---

## 5. Game Benchmarks

### 5.1 TextArena: A Collection of 100+ Competitive Text-Based Games

- **Authors:** Leon Guertler, Bobby Cheng, Su Yu, Bo Liu, Leshem Choshen, Cheston Tan
- **Venue:** arXiv preprint, Apr 2025
- **Link:** https://arxiv.org/abs/2504.11442
- **Abstract & Key Innovations:**
  100+ text-based games (single/two/multi-player) with Gym-compatible API. Online TrueSkill™ leaderboard with model-vs-model and model-vs-human. Soft-skill profiling (Theory of Mind, Bluffing, Persuasion, etc.). Highlighted by Andrej Karpathy. NeurIPS 2025 MindGames competition.

### 5.2 OmniGameArena: Unified UE5 Benchmark for VLM Game Agents

(See §3.7 above)

### 5.3 An Open-source Testbed for Generative Challenges in Games (PCG Benchmark)

- **Authors:** Ahmed Khalifa, Roberto Gallotta, Matthew Barthet, Antonios Liapis, Julian Togelius, Georgios N. Yannakakis
- **Venue:** arXiv preprint, Mar 2025
- **Link:** https://arxiv.org/abs/2503.21474
- **Abstract & Key Innovations:**
  Benchmark for evaluating generative algorithms on different game content creation tasks. Standardized evaluation framework for PCG research.

---

## 6. World Models for Games

### 6.1 RLVR-World: Training World Models with Reinforcement Learning

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, May 2025
- **Link:** https://arxiv.org/abs/2505.13934
- **Abstract & Key Innovations:**
  Unified framework using RLVR to optimize world models for task-specific metrics. +30.7% accuracy on text game state prediction, +15.1% F1 on web page state prediction. Applies to both language and video world models.

### 6.2 PriorZero: Bridging Language Priors and World Models for Decision Making

- **Authors:** Junyu Xiong, Yuan Pu, Jia Tang, Yazhe Niu
- **Venue:** arXiv preprint, May 2026
- **Link:** https://arxiv.org/abs/2605.12289
- **Abstract & Key Innovations:**
  Root-prior injection in MCTS using LLM priors at root node only. Decoupled rollout-training design. World model jointly improves dynamics, policy, and value predictions. Improves exploration efficiency and asymptotic performance on Jericho and BabyAI.

### 6.3 WorldCam: Interactive Autoregressive 3D Gaming Worlds

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, Mar 2026
- **Link:** https://arxiv.org/abs/2603.16871
- **Abstract & Key Innovations:**
  Camera pose as unifying geometric representation for action control and 3D consistency. Physics-based continuous action space in Lie algebra for 6-DoF poses. Pose-anchored long-term memory for consistent revisiting. 3,000 minutes of annotated gameplay dataset.

### 6.4 Reinforcement World Model Learning for LLM-based Agents (RWML)

- **Authors:** Xiao Yu, Baolin Peng, Ruize Xu, Yelong Shen, Pengcheng He, Suman Nath, et al.
- **Venue:** arXiv preprint, Feb 2026
- **Link:** https://arxiv.org/abs/2602.05842
- **Abstract & Key Innovations:**
  Self-supervised method using sim-to-real gap rewards in pre-trained embedding space. Avoids next-token prediction collapse. +19.6 and +6.9 points on ALFWorld and τ² Bench without expert data. Outperforms direct task-success reward RL when combined.

### 6.5 Multiplayer Interactive World Models with Representation Autoencoders

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, Jul 2026
- **Link:** https://arxiv.org/abs/2607.05352
- **Abstract & Key Innovations:**
  First multiplayer world model for highly dynamic environments. Conditions on action streams of multiple agents. 5B-parameter latent diffusion model generating 4-player Rocket League matches at 20 FPS on single B200 GPU. Stable rollouts up to 5 minutes. Releases dataset, code, and live demo.

### 6.6 PaW: Policy and World Modeling Co-Training for Language Agents

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, Jun 2026
- **Link:** https://arxiv.org/abs/2606.02388
- **Abstract & Key Innovations:**
  Reuses on-policy RL rollouts for joint policy optimization and world-modeling supervision. Action-entropy-based WM data selection, clipped MAE loss, reward-adaptive balancing. Consistent improvements across ALFWorld, WebShop, and search-augmented QA with negligible overhead.

### 6.7 Self-Improving World Modelling with Latent Actions (SWIRL)

- **Authors:** Yifu Qiu, Zheng Zhao, W.K. Li, Yftah Ziser, Anna Korhonen, Shay Cohen, et al.
- **Venue:** arXiv preprint, Feb 2026
- **Link:** https://arxiv.org/abs/2602.06130
- **Abstract & Key Innovations:**
  Learns from state-only sequences by treating actions as latent variables. Alternates Forward World Modelling and Inverse Dynamics Modelling with GRPO. +16% on AURORABench, +28% on ByteMorph, +16% on WorldPredictionBench.

### 6.8 Kairos: A Regret-Aware Native World-Action Model Stack for Physical AI

- **Authors:** (NVIDIA / Multi-institution)
- **Venue:** arXiv preprint, Jun 2026
- **Link:** https://arxiv.org/abs/2606.16533
- **Abstract & Key Innovations:**
  Fourth class of world-action models: unified understanding–generation–prediction. Regret-aware design learning control-sufficient state Z_t. Native architecture with Hybrid Linear Temporal Memory. Deployment-Aware System Co-Design for closed-loop readiness.

### 6.9 PAN: A General, Interactable, and Long-Horizon World Model

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, Nov 2025 (updated)
- **Link:** https://arxiv.org/abs/2511.09057
- **Abstract & Key Innovations:**
  Generative Latent Prediction architecture combining LLM-based autoregressive latent dynamics with video diffusion decoder. Trained on diverse video-action pairs. Supports open-domain, action-conditioned simulation with coherent long-term dynamics.

---

## 7. Related Techniques

### 7.1 HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for LLM Agents

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, Feb 2026
- **Link:** https://arxiv.org/abs/2602.16165
- **Abstract & Key Innovations:**
  Separates high-level planning from low-level execution. Hierarchical advantage estimation (HAE) assigns credit at both levels. 97.4% on ALFWorld and 83.3% on WebShop with Qwen2.5-7B (+6.6% and +8.3% over best prior). Provable variance reduction vs. flat GAE.

### 7.2 HiMAC: Hierarchical Macro-Micro Learning for Long-Horizon LLM Agents

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, Mar 2026
- **Link:** https://arxiv.org/abs/2603.00977
- **Abstract & Key Innovations:**
  Blueprint generation followed by goal-conditioned action execution. Critic-free hierarchical policy optimization extending GRPO to bi-level structures. Iterative co-evolution training. 83.4% on WebShop (16% gain over strongest RL baseline). Self-verification behaviors emerge spontaneously.

### 7.3 SPEAR: Self-Imitation with Progressive Exploration for Agentic RL

- **Authors:** Yulei Qin, Xiaoyu Tan, Zhini He, Gang Li, Haojia Lin, Zongyi Li, et al.
- **Venue:** arXiv preprint, Sep 2025
- **Link:** https://arxiv.org/abs/2509.22601
- **Abstract & Key Innovations:**
  Curriculum scheduling harmonizing intrinsic reward shaping and self-imitation. Progressive exploration-exploitation balance without entropy collapse. +16.1% on ALFWorld, +20.7% on WebShop. Plug-and-play with 10–25% extra complexity.

### 7.4 CDE: Curiosity-Driven Exploration for Efficient RL in Large Language Models

- **Authors:** Runpeng Dai, Linfeng Song, Haolin Liu, Zhenwen Liang, Dian Yu, Haitao Mi, et al.
- **Venue:** arXiv preprint, Sep 2025
- **Link:** https://arxiv.org/abs/2509.09675
- **Abstract & Key Innovations:**
  Actor curiosity via perplexity over generated response; critic curiosity via variance of multi-head value estimates. Connects critic bonus to count-based exploration in linear MDPs. +3 points over standard RLVR on AIME. Identifies calibration collapse mechanism in RLVR.

### 7.5 CuES: Curiosity-driven and Environment-grounded Synthesis Framework for Agentic RL

- **Authors:** Shinji Mai, Yunkai Zhai, Ziqian Chen, Cheng Chen, Anni Zou, Shuailin Tao, et al.
- **Venue:** arXiv preprint, Dec 2025
- **Link:** https://arxiv.org/abs/2512.01311
- **Abstract & Key Innovations:**
  Autonomous task generation from environment structure under intrinsic curiosity. Abstracts interaction patterns into reusable task schemas. Outperforms manually curated datasets by 30+ points on avg@8 across AppWorld, BFCL, WebShop.

### 7.6 cMarlTest: Curiosity Driven Multi-agent RL for 3D Game Testing

- **Authors:** (FBK / Multi-institution)
- **Venue:** arXiv preprint, Feb 2025
- **Link:** https://arxiv.org/abs/2502.14606
- **Abstract & Key Innovations:**
  Cooperative MARL for automated 3D game testing. Active agent performs actions; passive agent shares observations. Curiosity-based reward encouraging novelty. Higher coverage across entity, connection, and spatial criteria vs. single-agent RL.

### 7.7 Curiosity-Driven Exploration in RL for Action Games

- **Authors:** (Research team)
- **Venue:** Computers (MDPI), Oct 2025
- **Link:** https://doi.org/10.3390/computers14100434
- **Abstract & Key Innovations:**
  ICM + A3C with PPO optimization for action games (Mortal Kombat, Street Fighter). Curiosity-driven exploration without external rewards. Improved exploration efficiency and generalization to novel scenarios.

---

## Key Trends & Observations

1. **Self-play for reasoning (not just games):** SPIRAL, MARSHAL, and Strat-Reasoner show that game self-play generates transferable reasoning skills for math, code, and general problem-solving.

2. **LLM-as-game-engine:** HexMachina, FAMOU, and AutoHarness demonstrate that LLMs can serve as strategy architects rather than per-turn deciders, producing executable code policies.

3. **Foundation models go multi-game:** NitroGen (CVPR 2026), Game-TARS, and Pixels2Play establish internet-scale pre-training for generalist game agents, with open-source releases.

4. **World models are the new frontier:** 9 papers on world models for games/simulation, with multiplayer world models (Rocket League, 5B params) and camera-pose-anchored 3D consistency as key innovations.

5. **Hierarchical RL for LLM agents:** HiPER and HiMAC show that explicit macro-micro decomposition dramatically improves long-horizon performance (97.4% ALFWorld).

6. **Benchmark explosion:** TextArena (100+ games), OmniGameArena (UE5), and PCG Benchmark create standardized evaluation for the field.

7. **Code-as-policy:** AutoHarness, FAMOU, and generative code optimization show that synthesizing entire policies in code can beat much larger LLMs at near-zero inference cost.
