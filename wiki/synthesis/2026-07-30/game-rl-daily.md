---
title: "Game RL & Game AI Bot — Daily Synthesis (2026-07-30)"
type: synthesis
created: 2026-07-30
updated: 2026-07-30
tags: [game-rl, game-ai, game-foundation-models, pcg, game-benchmarks, self-play, world-models, multi-agent-rl, llm-agents]
sources: []
---

# Game RL & Game AI Bot — Daily Synthesis (2026-07-30)

> Curated papers on Game RL, Game AI Bots, Game Foundation Models, PCG, Benchmarks, Industry Game AI, and related techniques. Searched arXiv and recent proceedings.

---

## 1. Game RL — Reinforcement Learning in Games

### CAST: Credit Assignment from Solver Teachers for LLM Agents
- **Authors**: Wloner et al.
- **Affiliation**: —
- **Venue**: arXiv:2607.25308 (Jul 2026)
- **Key Innovation**: Converts game solver state-value changes into turn-level training signals for LLM RLVR. Under soft-optimal solver assumption, maximizing solver advantage = on-policy distillation from solver (logit-free). Outperforms all baselines on Sokoban, Minesweeper, Rush Hour, ALFWorld, WebShop.
- **Link**: https://arxiv.org/abs/2607.25308

### Superhuman AI for Stratego Using Self-Play RL and Test-Time Search
- **Authors**: Samuel Sokota, Eugene Vinitsky, Hengyuan Hu, J. Zico Kolter, Gabriele Farina
- **Affiliation**: —
- **Venue**: arXiv:2511.07312 (Nov 2025)
- **Key Innovation**: First superhuman Stratego AI. Achieves vastly superhuman level with only a few thousand dollars of compute via self-play RL and test-time search under imperfect information. Prior multi-million-dollar efforts failed to reach top human level.
- **Link**: https://arxiv.org/abs/2511.07312

### Solly: Outbidding and Outbluffing Elite Humans — Mastering Liar's Poker via Self-Play and RL
- **Authors**: Richard Dewey, Janos Botyanszki, Ciamac C. Moallemi, Andrew T. Zheng
- **Affiliation**: —
- **Venue**: arXiv:2511.03724 (Nov 2025 / May 2026 update)
- **Key Innovation**: First AI to achieve elite human play in reduced-format Liar's Poker. Model-free actor-critic self-play. Develops novel bidding strategies, randomized play; outperforms LLMs including reasoning models.
- **Link**: https://arxiv.org/abs/2511.03724

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors**: Bo Liu, Leon Guertler, Simon Yu, Zichen Liu, Penghui Qi, Daniel Balcells, Mickel Liu, Cheston Tan, Weiyan Shi, Min Lin, Wee Sun Lee, Natasha Jaques
- **Affiliation**: —
- **Venue**: ICLR 2026 / arXiv:2506.24119
- **Key Innovation**: Self-play framework where LLMs learn by playing multi-turn zero-sum games against continuously improving selves. Fully online multi-agent RL with role-conditioned advantage estimation (RAE). Up to 10% improvement on 8 reasoning benchmarks. Multi-game training yields strongest results. DeepSeek-R1-Distill-Qwen-7B still benefits.
- **Link**: https://arxiv.org/abs/2506.24119

### Artificial Generals Intelligence: Mastering Generals.io with RL
- **Authors**: Matej Straka, Martin Schmid
- **Affiliation**: —
- **Venue**: arXiv:2507.06825 (Jul 2025)
- **Key Innovation**: RTS environment compatible with Gymnasium/PettingZoo. RL agent with supervised pre-training + self-play reaches top 0.003% of human 1v1 leaderboard after 36 hours on single H100 GPU. Potential-based reward shaping and memory features.
- **Link**: https://arxiv.org/abs/2507.06825

### CRUISE: Curriculum-Based Iterative Self-Play for Scalable Multi-Drone Racing
- **Authors**: Onur Akgün
- **Affiliation**: —
- **Venue**: arXiv:2510.22570 (Oct 2025, under review)
- **Key Innovation**: RL framework combining progressive difficulty curriculum with self-play for multi-drone racing. Nearly double the planner's mean racing speed, high success rates, robust scalability.
- **Link**: https://arxiv.org/abs/2510.22570

### VGC-Bench: Towards Mastering Diverse Team Strategies in Competitive Pokémon
- **Authors**: Cameron Angliss, Jiaxun Cui, Jiaheng Hu, Arrasy Rahman, Peter Stone
- **Affiliation**: UT Austin / Sony AI?
- **Venue**: arXiv:2506.10326
- **Key Innovation**: Benchmark and framework for competitive Pokémon battling with diverse team strategies.
- **Link**: https://arxiv.org/abs/2506.10326

### IPPO Learns the Game, Not the Team: Generalization in Heterogeneous Agent Teams
- **Authors**: Ryan LeRoy, Jack Kolb
- **Affiliation**: —
- **Venue**: arXiv:2512.08877 (Dec 2025)
- **Key Innovation**: Shows that IPPO baseline generalizes to novel teammate algorithms despite lacking teammate diversity during training, suggesting self-play PPO may learn game-grounded coordination strategies.
- **Link**: https://arxiv.org/abs/2512.08877

### Learning Game-Playing Agents with Generative Code Optimization
- **Authors**: Zhiyi Kuang, Ryan Rong, YuCheng Yuan, Allen Nie
- **Affiliation**: —
- **Venue**: ICML 2025 Workshop / arXiv:2508.19506
- **Key Innovation**: Game-playing policies as Python programs refined by LLMs. Atari performance competitive with deep RL baselines using significantly fewer environment interactions.
- **Link**: https://arxiv.org/abs/2508.19506

### Deep Reinforcement Learning Xiangqi Player with MCTS
- **Authors**: Berk Yilmaz, Junyu Hu, Jinsong Liu
- **Affiliation**: —
- **Venue**: arXiv:2506.15880 (Jun 2025)
- **Key Innovation**: Policy-value networks + MCTS for Xiangqi (Chinese Chess) enabling strategic self-play.
- **Link**: https://arxiv.org/abs/2506.15880

---

## 2. Game AI Bot — LLM-Powered Game Agents & NPC Intelligence

### PCSP: One Policy, Infinite NPCs — Persona-Traceable Shared RL Policies for Scalable Game Agents
- **Authors**: Yoosung Hong et al.
- **Affiliation**: —
- **Venue**: arXiv:2605.23652 (May 2026)
- **Key Innovation**: Single RL policy conditioned on frozen LLM persona embeddings (FiLM fusion + PPO + InfoNCE + KL diversity). 22× faster inference than LLM-as-policy. Zero-shot persona identification 17× above chance. Validated on Melting Pot social dilemmas and deployed in UE5 with 64 agents at 1.7% failure rate.
- **Link**: https://arxiv.org/abs/2605.23652

### Bounded Autonomy: Controlling LLM Characters in Live Multiplayer Games
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2604.04703 (Jul 2026)
- **Key Innovation**: Control architecture for LLM characters in live multiplayer games: probabilistic reply-chain decay, embedding-based action grounding with fallback, and "whisper" soft-steering technique. Deployed in live multiplayer social game.
- **Link**: https://arxiv.org/abs/2604.04703

### COS-PLAY: Co-Evolving LLM Decision and Skill Bank Agents for Long-Horizon Tasks
- **Authors**: Xiyang Wu, Zongxia Li, Guangyao Shi, Alexander Duffy, Tyler Marques, Matthew Olson et al.
- **Affiliation**: —
- **Venue**: arXiv:2604.20987 (Apr 2026)
- **Key Innovation**: Co-evolution framework where LLM decision agent retrieves skills from learnable skill bank while skill-bank agent extracts skills from unlabeled rollouts. 25.1% average improvement over frontier LLMs on single-player games (2048, Candy Crush, Tetris, Super Mario). Competitive on Avalon and Diplomacy.
- **Link**: https://arxiv.org/abs/2604.20987

### Sensi: Learn One Thing at a Time — Curriculum-Based Test-Time Learning for LLM Game Agents
- **Authors**: Mohsen Arjmandi
- **Affiliation**: —
- **Venue**: arXiv:2603.17683 (Mar 2026)
- **Key Innovation**: Two-player (Observer + Actor) architecture with curriculum-based learning managed by external state machine. Database-as-control-plane for steerable context. 50-94× sample efficiency vs. comparable systems on ARC-AGI-3. Honest negative result: v2 solves 0 levels due to perception hallucination cascade, shifting bottleneck from learning efficiency to perceptual grounding.
- **Link**: https://arxiv.org/abs/2603.17683

### Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with LLMs
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2604.21896 (Apr 2026)
- **Key Innovation**: Framework operationalizing Shannon's taxonomy of game-playing machines via LLMs. Covers dictionary-based, solvable, heuristic, and learning-based games. Programmable prompt engineering with crowdsourced strategy refinement.
- **Link**: https://arxiv.org/abs/2604.21896

### Vox Deorum: Hybrid LLM Architecture for 4X/Grand Strategy Game AI (Civilization V)
- **Authors**: John Chen, Sihan Cheng, Can Gurkan, Ryan Lay, Moez Salahuddin
- **Affiliation**: —
- **Venue**: arXiv:2512.18564 (Dec 2025)
- **Key Innovation**: Hybrid LLM+X architecture for Civ V. LLM handles macro-strategic reasoning while algorithmic AI handles tactical execution. Validated over 2,327 games; LLMs achieve competitive gameplay with distinct play styles.
- **Link**: https://arxiv.org/abs/2512.18564

### Orchestrated Reality: From Role-Play to Living, Playable Game Worlds
- **Authors**: Y Huang, Chenmiao Li, Chaowei Fang
- **Affiliation**: —
- **Venue**: arXiv:2606.16014 (Jun 2026)
- **Key Innovation**: Framework for generating living, playable game worlds from role-play interactions. Focus on dynamic world simulation.
- **Link**: https://arxiv.org/abs/2606.16014

### PolicyEvolve: Evolving Programmatic Policies by LLMs for Multi-Player Games via Population-Based Training
- **Authors**: Mingrui Lv, Hangzhi Liu, Zhi Luo, Hongjie Zhang, Jie Ou
- **Affiliation**: —
- **Venue**: arXiv:2509.06053 (Sep 2025)
- **Key Innovation**: Generates interpretable programmatic (rule-based code) policies for multi-player games using LLMs. Global/Local Pool architecture with Policy Planner and Trajectory Critic. Minimal environment interactions needed.
- **Link**: https://arxiv.org/abs/2509.06053

---

## 3. Game Foundation Models — Generalist Game Agents

### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, et al.
- **Affiliation**: NVIDIA / MineDojo
- **Venue**: CVPR 2026 / arXiv:2601.02427 (Jan 2026)
- **Key Innovation**: Vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games. Flow matching (DiT) for action generation conditioned on SigLIP 2 visual encoder. Up to 52% relative improvement on unseen games. Open-source dataset, simulator, and weights.
- **Link**: https://arxiv.org/abs/2601.02427

### Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents
- **Authors**: Zihao Wang, Xujing Li, Yining Ye, Junjie Fang, Haoming Wang, Longxiang Liu, et al.
- **Affiliation**: ByteDance
- **Venue**: arXiv:2510.23691 (Oct 2025)
- **Key Innovation**: Unified action space (keyboard+mouse) for cross-domain pre-training. Sparse Thinking (ReAct at critical decision points). 20,000+ hours of game trajectories. 2× improvement over previous SOTA in Minecraft. Outperforms Gemini-2.5-Pro, GPT-5, Claude-4-Sonnet on various tasks.
- **Link**: https://arxiv.org/abs/2510.23691

### Optimus-3: Towards Generalist Multimodal Minecraft Agents with Scalable Task Experts
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2506.10357
- **Key Innovation**: Knowledge-enhanced data generation + task-level routing MoE (avoids interference among heterogeneous tasks) + Multimodal Reasoning-Augmented RL (GRPO + IoU-Density Reward). Outperforms generalist MLLMs and previous SOTA in Minecraft across Planning (+20%), Grounding (3.4×), Embodied QA (+76%), Reflection (+18%).
- **Link**: https://arxiv.org/abs/2506.10357

### JARVIS-VLA: Post-Training Large-Scale Vision Language Models to Play Visual Games with Keyboards and Mouse
- **Authors**: —
- **Affiliation**: CraftJARVIS
- **Venue**: arXiv:2503.16365
- **Key Innovation**: ActVLP paradigm — post-train VLM on non-trajectory vision-language tasks (knowledge QA, visual alignment, spatial grounding) before action post-training. 40% improvement over best agent baseline on 1k+ atomic Minecraft tasks. State-of-the-art VLA in Minecraft.
- **Link**: https://arxiv.org/abs/2503.16365

### MAIN-VLA: Modeling Abstraction of Intention and Environment for Vision-Language-Action Models
- **Authors**: Zheyuan Zhou, Liang Du, Zixun Sun, X. Y. Zhou, Ruimin Ye, Qihao Chen, et al.
- **Affiliation**: —
- **Venue**: arXiv:2602.02212 (Feb 2026)
- **Key Innovation**: Intention Abstraction (IA) + Environment Semantic Abstraction (ESA) for VLA models. Compact keyword+latent representations. Tested on Minecraft (MCU benchmark) and Game for Peace (battle royale). 67.9% SR on Game for Peace vs. 53.4% vanilla IL. Emergent token pruning for efficiency.
- **Link**: https://arxiv.org/abs/2602.02212

### Pixels2Play (P2P): A Foundation Model for 3D Gameplay
- **Authors**: Yuguang Yue, Chris Green, Samuel Hunt, Irakli Salia, Wenzhe Shi, Jonathan J. Hunt
- **Affiliation**: —
- **Venue**: arXiv:2508.14295 (Aug 2025)
- **Key Innovation**: Foundation model for 3D games from raw pixels. Decoder-only transformer with autoregressive action output. Trained via behavior cloning on instrumented human gameplay + unlabeled videos with inverse-dynamics imputation. Competent play across Roblox and MS-DOS titles. Consumer GPU friendly.
- **Link**: https://arxiv.org/abs/2508.14295

### Scaling Behavior Cloning for 3D Gameplay
- **Authors**: Yuguang Yue, Irakli Salia, Samuel Hunt, Chris Green, Wenzhe Shi, Jonathan J. Hunt
- **Affiliation**: —
- **Venue**: arXiv:2601.04575 (Jan 2026)
- **Key Innovation**: Open recipe for training game-playing foundation model on consumer GPU. 8,300+ hours of human gameplay released. Systematic scaling law study: increasing data and depth leads to more causal policy. Models up to 1.2B parameters.
- **Link**: https://arxiv.org/abs/2601.04575

---

## 4. Procedural Content Generation (PCG)

### VIPCGRL: Human-Aligned PCGRL via Text-Level-Sketch Shared Representation
- **Authors**: In-Chang Baek, Seoyoung Lee, Sung-Hyun Kim, Geumhwan Hwang, KyungJoong Kim
- **Affiliation**: —
- **Venue**: arXiv:2508.09860 (Aug 2025)
- **Key Innovation**: Tri-modal (text, level, sketch) DRL framework for PCG. Quadruple contrastive learning across modalities + human-AI styles. Auxiliary reward from embedding similarity aligns policy with human intent. Outperforms baselines in human-likeness.
- **Link**: https://arxiv.org/abs/2508.09860

### PCGRLLM: LLM-Driven Reward Design for Procedural Content Generation RL
- **Authors**: In-Chang Baek et al.
- **Affiliation**: —
- **Venue**: arXiv:2502.10906 (Feb 2025 / May 2026 update)
- **Key Innovation**: LLM generates reward functions from brief story instructions for PCGRL. Feedback mechanism + reasoning-based prompt engineering lets LLM refine rewards based on trained agent outcomes. Performance comparable to human-designed rewards.
- **Link**: https://arxiv.org/abs/2502.10906

### IPCGRL: Language-Instructed RL for Procedural Level Generation
- **Authors**: In-Chang Baek, Sunghyun Kim, Seo-Young Lee, Dong-Hyeon Kim, Kyung-Joong Kim
- **Affiliation**: —
- **Venue**: IEEE CoG 2025 / arXiv:2503.12358
- **Key Innovation**: Text-controlled PCGRL with task-specific sentence embeddings. 21.4% controllability improvement over BERT-based conditioning. 17.2% improvement in generalization to unseen instructions.
- **Link**: https://arxiv.org/abs/2503.12358

### MIPCGRL: Multi-Objective Instruction-Aware Representation Learning in PCGRL
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2508.09193
- **Key Innovation**: Extends IPCGRL to multi-objective instructions via multi-label classification + multi-head regression networks. 13.8% improvement over IPCGRL on multi-objective level generation tasks.
- **Link**: https://arxiv.org/abs/2508.09193

### WCRL: Learning Local Constraints for Reinforcement-Learned Content Generators
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2605.13570 (May 2026)
- **Key Innovation**: Combines Wave Function Collapse (local pattern learning) with PCGRL (global property guarantees). WFC constrains RL action space. Generates visually satisfying and playable Lode Runner levels.
- **Link**: https://arxiv.org/abs/2605.13570

### Multiverse: Language-Conditioned Multi-Game Level Blending via Shared Representation
- **Authors**: In-Chang Baek, Jiyun Jung, Geum-Hwan Hwang, Sung-Hyun Kim, Kyung-Joong Kim
- **Affiliation**: —
- **Venue**: arXiv:2603.26782 (Mar 2026)
- **Key Innovation**: Language-conditioned multi-game level generator enabling cross-game level blending. Multi-positive contrastive supervision links semantically related levels across games. Latent interpolation enables controllable blending from compositional text prompts.
- **Link**: https://arxiv.org/abs/2603.26782

---

## 5. Game Benchmarks

### Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games
- **Authors**: Dongmin Park, Minkyu Kim, Beongjun Choi, Junhyuck Kim, Keon Lee, Jonghyun Lee, et al.
- **Affiliation**: KRAFTON
- **Venue**: arXiv:2506.03610 (Jun 2025)
- **Key Innovation**: 12 popular games spanning all major genres. MCP-based plug-and-play interface. Fine-tuning dataset of LLM gameplay trajectories. Leaderboard + battle arena. Evaluates 12 LLMs with agentic strategies (reflection-planning, skill-management, etc.).
- **Link**: https://arxiv.org/abs/2506.03610

### lmgame-Bench: How Good are LLMs at Playing Games?
- **Authors**: Lanxiang Hu, Ming Huo, Yuxuan Zhang, Hongwen Yu, Eric P. Xing, Ion Stoica, et al.
- **Affiliation**: —
- **Venue**: arXiv:2505.15146 / ICLR 2026
- **Key Innovation**: Gaming harness (perception + memory scaffolds) to overcome LLM vision limitations. 13 models across 6 games (platformer, puzzle, narrative). RL training on games transfers to unseen games and external planning tasks (Blocksworld, WebShop). Contamination mitigation.
- **Link**: https://arxiv.org/abs/2505.15146

### OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics
- **Authors**: Mingxian Lin, Shengju Qian, Yuqi Liu, Yi-Hua Huang, Yiyu Wang, Wei Huang, et al.
- **Affiliation**: —
- **Venue**: arXiv:2606.09826 (Jun 2026)
- **Key Innovation**: 12 newly built UE5 games (Solo/PvP/Coop), no pre-training leakage risk. Improvement Dynamics Curve (IDC): agentic-reflection harness where LLM autonomously refines skill prompt across rounds. Evaluates commercial VLMs, open-weight VLMs, and specialized game policies (NitroGen, Open-P2P). GPT-5.5 leads; IDC reveals GPT-5.5 skills transfer best.
- **Link**: https://arxiv.org/abs/2606.09826

### GVGAI-LLM: Evaluating LLM Agents with Infinite Games
- **Authors**: Yuchen Li, C. C. Lin, Muhammad Umair Nasir, Philip Bontrager, Jialin Liu, Julian Togelius
- **Affiliation**: NYU / —
- **Venue**: arXiv:2508.08501 (Aug 2025)
- **Key Innovation**: Adapts General Video Game AI (GVGAI) framework for LLM evaluation. ASCII-based game representations. New metrics: meaningful step ratio, step efficiency. Reveals persistent spatial reasoning and planning limitations in current LLMs.
- **Link**: https://arxiv.org/abs/2508.08501

### IPR-1: Interactive Physical Reasoner — Game-to-Unseen Benchmark
- **Authors**: Mingyu Zhang, Lifeng Zhuo, Tianxi Tan, et al.
- **Affiliation**: —
- **Venue**: CVPR 2026 / arXiv:2511.15407
- **Key Innovation**: 1,000+ heterogeneous games benchmark (Game-to-Unseen G2U). World-model rollouts to score and reinforce VLM policy. PhysCode (physics-centric action code). Surpasses GPT-5 overall. Performance improves with more games and interaction steps.
- **Link**: https://arxiv.org/abs/2511.15407

---

## 6. Industry Game AI

### Automated Reward Design for Gran Turismo
- **Authors**: Michel Ma, Takuma Seno, Kaushik Subramanian, Peter R. Wurman, Peter Stone, Craig Sherstan
- **Affiliation**: Sony AI
- **Venue**: arXiv:2511.02094 (Nov 2025)
- **Key Innovation**: Foundation models (LLM reward gen + VLM preference eval + human feedback) to search reward space for GT7 racing agents. Competitive with GT Sophy (champion-level RL agent). Novel behaviors generated.
- **Link**: https://arxiv.org/abs/2511.02094

### Beyond Playtesting: Generative Multi-Agent Simulation System for MMOs
- **Authors**: Ran Zhang, Kun Ouyang, Tiancheng Ma, Yida Yang, Dong Fang
- **Affiliation**: —
- **Venue**: arXiv:2512.02358 (Dec 2025)
- **Key Innovation**: LLM-powered agent simulation for MMO game design optimization. SFT + RL on large-scale real player behavioral data. Data-driven environment model from gameplay logs. Strong consistency with real player behaviors.
- **Link**: https://arxiv.org/abs/2512.02358

---

## 7. Related Techniques — Self-Play, World Models, Multi-Agent RL

### MARSHAL: Incentivizing Multi-Agent Reasoning via Self-Play with Strategic LLMs
- **Authors**: Huining Yuan, Zelai Xu, Zheyue Tan, Xiangmin Yi, Mo Guang, Kaiwen Long, et al.
- **Affiliation**: —
- **Venue**: arXiv:2510.15414 (Oct 2025 / Feb 2026 update)
- **Key Innovation**: End-to-end RL framework for multi-agent LLM reasoning. Turn-level advantage estimator + agent-specific advantage normalization. Self-play across cooperative/competitive games gives up to 28.7% improvements. Transfers to reasoning benchmarks: +10% AIME, +7.6% GPQA-Diamond.
- **Link**: https://arxiv.org/abs/2510.15414

### Vision-Zero: Scalable VLM Self-Improvement via Strategic Gamified Self-Play
- **Authors**: Qinsi Wang, Bo Liu, Tianyi Zhou, Jing Shi, Yueqian Lin, Yiran Chen, Hai Helen Li, Kun Wan, Wentian Zhao
- **Affiliation**: —
- **Venue**: ICLR 2026 / arXiv:2509.25541
- **Key Innovation**: Label-free multi-agent self-play for VLMs via "Who Is the Spy" games from arbitrary images. Iterative Self-Play Policy Optimization (Iterative-SPO). State-of-the-art on reasoning, chart QA, vision-centric tasks.
- **Link**: https://arxiv.org/abs/2509.25541

### Search Self-Play (SSP): Pushing the Frontier of Agent Capability without Supervision
- **Authors**: Hongliang Lu, Yuhang Wen, Pengyu Cheng, et al.
- **Affiliation**: Qwen team (Alibaba)
- **Venue**: ICLR 2026 / arXiv:2510.18821
- **Key Innovation**: Self-play training for LLM search agents. LLM acts simultaneously as task proposer + problem solver. RAG-based ground-truth verification for proposed searches. Co-evolution through competition and cooperation. Significant improvements on search benchmarks without supervision.
- **Link**: https://arxiv.org/abs/2510.18821

### SGA-ACR: Subgoal Graph-Augmented Planning for LLM-Guided Open-World RL
- **Authors**: Shanwei Fan, Bin Zhang, Zhiwei Xu, Yingxuan Teng, Siqi Dai, Lin Cheng, Guoliang Fan
- **Affiliation**: —
- **Venue**: arXiv:2511.20993 (Nov 2025)
- **Key Innovation**: Environment-specific subgoal graph + structured entity knowledge + multi-LLM planning (separate generation, critique, refinement). Subgoal tracker provides auxiliary rewards. Validated on 22 tasks in Crafter open-world game.
- **Link**: https://arxiv.org/abs/2511.20993

### LED-WM: Language-Conditioned World Model for Improved Policy Generalization
- **Authors**: Anh Nguyen, Stefan Lee
- **Affiliation**: —
- **Venue**: NeurIPS 2025 Workshop (LAW) / arXiv:2511.22904
- **Key Innovation**: Language-aware Encoder for Dreamer World Model (LED-WM). Attention-based observation encoder explicitly grounds language descriptions to entities. Policies trained with LED-WM generalize to unseen games described by novel dynamics/language.
- **Link**: https://arxiv.org/abs/2511.22904

### ProPS: Prompted Policy Search — RL through Linguistic and Numerical Reasoning in LLMs
- **Authors**: Yifan Zhou, Sachin Grover, Mohamed El Mistiri, et al.
- **Affiliation**: —
- **Venue**: NeurIPS 2025 / arXiv:2511.21928
- **Key Innovation**: Places LLM at center of policy optimization loop, directly proposing policy updates from reward feedback + natural language input. Outperforms PPO, SAC, TRPO on 8/15 tasks (Atari, MuJoCo, classic control).
- **Link**: https://arxiv.org/abs/2511.21928

### DiffFP: Learning Behaviors from Scratch via Diffusion-based Fictitious Play
- **Authors**: Akash Karthikeyan, Yash Vardhan Pant
- **Affiliation**: —
- **Venue**: IJCAI 2025 Workshop / arXiv:2511.13186
- **Key Innovation**: Diffusion policy for best-response estimation in fictitious play. Converges to ε-Nash in continuous-space zero-sum games. Up to 3× faster convergence and 30× higher success rates against RL baselines.
- **Link**: https://arxiv.org/abs/2511.13186

### Language Self-Play (LSP) for Data-Free Training
- **Authors**: Jakub Grudzien Kuba, Mengting Gu, Qi Ma, Yuandong Tian, Vijai Mohan, Jason Chen
- **Affiliation**: Meta?
- **Venue**: arXiv:2509.07414 (Sep 2025)
- **Key Innovation**: Game-theoretic self-play framework where LLM improves without additional data by playing against itself. Validated on instruction-following, math, and coding with Llama-3.2-3B.
- **Link**: https://arxiv.org/abs/2509.07414

### Multi-Agent Evolve (MAE): LLM Self-Improve through Co-evolution
- **Authors**: Yixing Chen, Yiding Wang, Siqi Zhu, et al.
- **Affiliation**: —
- **Venue**: arXiv:2510.23595 (Oct 2025)
- **Key Innovation**: Triplet of agents (Proposer, Solver, Judge) from single LLM, co-evolved via RL. 4.54% average improvement on multiple benchmarks with Qwen2.5-3B.
- **Link**: https://arxiv.org/abs/2510.23595

### A Comprehensive Review of Multi-Agent Reinforcement Learning in Video Games
- **Authors**: Zhengyang Li, Qijin Ji, Xinghong Ling, Quan Liu
- **Affiliation**: —
- **Venue**: IEEE Trans. Games 2025 / arXiv:2509.03682
- **Key Innovation**: Thorough survey of MARL from turn-based to real-time multi-agent games (Rocket League, Minecraft, Quake III, StarCraft II, Dota 2, Honor of Kings). Novel game complexity estimation method.
- **Link**: https://arxiv.org/abs/2509.03682

### Mastering Da Vinci Code: Transformer, LLM, and PPO-based Agents
- **Authors**: LeCheng Zhang, Yuanshi Wang, Haotian Shen, Xujie Wang
- **Affiliation**: —
- **Venue**: arXiv:2506.12801 (Jun 2025)
- **Key Innovation**: Comparative study of Transformer, LLM (Gemini, DeepSeek, GPT), and PPO agents for logical deduction game. PPO with Transformer encoder achieves 58.5% win rate, significantly outperforming LLM counterparts.
- **Link**: https://arxiv.org/abs/2506.12801

### Equilibrium Policy Generalization: Cross-Graph Zero-Shot in Pursuit-Evasion Games
- **Authors**: Runyu Lu, Peng Zhang, et al.
- **Affiliation**: —
- **Venue**: arXiv:2511.00811 (Nov 2025)
- **Key Innovation**: EPG framework for zero-shot generalization across different graph structures in pursuit-evasion games. DP algorithm for pure-strategy Nash equilibrium. Distance feature enables desirable zero-shot performance on unseen real-world graphs.
- **Link**: https://arxiv.org/abs/2511.00811

---

## Summary Statistics

- **Total papers**: ~40
- **Categories covered**: 7
- **Key venues**: ICLR 2026, CVPR 2026, NeurIPS 2025, IEEE CoG 2025, IEEE Trans. Games
- **Notable trends**:
  - Self-play RL for LLM reasoning (SPIRAL, MARSHAL, Vision-Zero) is a major theme at ICLR 2026
  - Game foundation models scaling to 1000+ games (NitroGen, Game-TARS)
  - LLM-powered NPC control with persona conditioning and bounded autonomy
  - PCGRL advancing to multi-modal (text+sketch+level) conditioning
  - New UE5-based benchmarks (OmniGameArena) avoiding pre-training contamination
  - World models + VLM integration for physical reasoning (IPR-1 CVPR 2026)
  - Game solvers as teachers for LLM agents (CAST)
