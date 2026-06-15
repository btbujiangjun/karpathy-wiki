---
title: Game RL & Game AI Bot — Daily Survey (2026-06-15)
type: synthesis
created: 2026-06-15
updated: 2026-06-15
tags: [game-rl, game-ai, survey, self-play, marl, world-models, pcg, benchmarks]
---

# Game RL & Game AI Bot — Daily Survey (2026-06-15)

> Survey of recent arXiv & proceedings papers on Game RL, Game AI Bots, Foundation Models, PCG, Benchmarks, and related techniques. Coverage: June 2025 – June 2026 submissions.

## 1. Game Reinforcement Learning — Self-Play & Multi-Agent

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors**: Bo Liu, Leon Guertler, Simon Yu, Zichen Liu, Penghui Qi, Daniel Balcells, Mickel Liu, Cheston Tan, Weiyan Shi, Min Lin, Wee Sun Lee, Natasha Jaques
- **Affiliation**: Sea AI Lab, NUS
- **Venue**: ICLR 2026
- **Abstract**: Self-play framework where LLMs learn by playing multi-turn zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation) against continuously improving versions of themselves. Proposes role-conditioned advantage estimation (RAE) for stable multi-agent training. Improves reasoning benchmarks by up to 10% across Qwen and Llama families; transfers to unseen games and reasoning tasks.
- **Innovation**: Fully online multi-turn multi-agent RL for LLMs; zero-sum games as automatic curriculum for reasoning development.
- **Link**: [arXiv:2506.24119](https://arxiv.org/abs/2506.24119)

### MARSHAL: Incentivizing Multi-Agent Reasoning via Self-Play with Strategic LLMs
- **Authors**: Huining Yuan, Zelai Xu, Zheyue Tan, Xiangmin Yi, Mo Guang, Kaiwen Long, Haojia Hui, Boxun Li, Xinlei Chen, Bo Zhao, Xiao-Ping Zhang, Chao Yu, Yu Wang
- **Affiliation**: Tsinghua University
- **Venue**: arXiv (Oct 2025, v3 Feb 2026)
- **Abstract**: End-to-end RL framework for multi-agent reasoning through self-play in cooperative and competitive games. Features turn-level advantage estimator for long-horizon credit assignment and agent-specific advantage normalization. Qwen3-4B agents achieve 28.7% improvement on held-out games; transfers to AIME (+10%), GPQA-Diamond (+7.6%) in zero-shot.
- **Innovation**: First end-to-end RL for multi-turn multi-agent LLM reasoning; game-trained strategic abilities generalize to non-game reasoning benchmarks.
- **Link**: [arXiv:2510.15414](https://arxiv.org/abs/2510.15414)

### Beyond Static Evaluation: Co-Evolutionary Mechanisms for LLM-Driven Strategy Evolution in Adversarial Games
- **Authors**: Haoran Li, Zengle Ge, Ziyang Zhang, et al.
- **Affiliation**: Baidu
- **Venue**: arXiv (Jun 2026)
- **Abstract**: Proposes FAMOU framework with evaluator co-evolution, hierarchical deep evaluation, and weakness pressure for LLM-driven code evolution in adversarial games. On MCTF 2026 3v3 maritime capture-the-flag, achieves highest combined score (0.526) and 61.7% win rate against unseen opponents. Evolved strategies discover lookahead search and adaptive interception. 1st place AAMAS 2026 MCTF Competition.
- **Innovation**: Co-evolution of evaluator alongside strategy population; LLM mutation generates tactical structures absent from seed strategies.
- **Link**: [arXiv:2606.10389](https://arxiv.org/abs/2606.10389)

### Φ-Actor-Critic: Steering General-Sum Games to Pareto-Efficient Correlated Equilibria
- **Authors**: Wongyu Lee, Francesco Lelli, Omran Ayoub, Massimo Tornatore
- **Affiliation**: — (accepted IJCAI 2026)
- **Venue**: IJCAI 2026
- **Abstract**: Framework leveraging swap regret minimization to steer MARL toward high-welfare correlated equilibria. Uses centralized attention critic for vector-valued regret prediction. Experiments on matrix games, MPE, and Melting Pot Harvest.
- **Innovation**: Lagrangian-based equilibrium selection for social welfare optimization in general-sum games.
- **Link**: [arXiv:2606.11284](https://arxiv.org/abs/2606.11284)

### α-fair Heterogeneous Agent Reinforcement Learning
- **Authors**: Yao-hua Franck Xu, Tayeb Lemlouma, Jean-Marie Bonnin, Arnaud Braud
- **Affiliation**: — (Jun 2026)
- **Venue**: arXiv (Jun 2026)
- **Abstract**: Bridges α-fairness with Heterogeneous-Agent Trust Region Learning (HATRL). Introduces α-fair HATRPO and α-fair HAPPO for sequential social dilemmas (CleanUp, CommonHarvest). Achieves fairer outcomes without sacrificing utilitarian efficiency.
- **Innovation**: Fairness-aware MARL with monotonic improvement guarantees and Nash convergence.
- **Link**: [arXiv:2606.13076](https://arxiv.org/abs/2606.13076)

### Learning to Contest: Decentralized Robust Fairness in Cooperative MARL via Cross-Attention
- **Authors**: Can Savcı
- **Affiliation**: — (Jun 2026)
- **Venue**: arXiv (Jun 2026)
- **Abstract**: CAN, a permutation-equivariant cross-attention policy for detecting and responding to free-riders in fair MARL. Keeps exploitability near centralized oracle levels at no efficiency cost.
- **Innovation**: Decentralized defense against free-riding in egalitarian welfare MARL teams.
- **Link**: [arXiv:2606.06162](https://arxiv.org/abs/2606.06162)

### Episodic Memory Temporal Consistency for Cooperative Multi-Agent Reinforcement Learning
- **Authors**: Zicheng Zhao, Yu Lan, Chengzhengxu Li, Zhaohan Zhang, Xiaoming Liu
- **Affiliation**: — (Jun 2026)
- **Venue**: arXiv (Jun 2026)
- **Abstract**: EMTC framework leveraging episodic memory for temporal consistency in cooperative MARL.
- **Link**: [arXiv:2606.04492](https://arxiv.org/abs/2606.04492)

### Learning Coordinated Preference for Multi-Objective Multi-Agent Reinforcement Learning
- **Authors**: Pengxin Wang, Lihao Guo, Yi Xie, Bo Liu, Siyang Cao, Jingdi Chen
- **Affiliation**: — (Jun 2026)
- **Venue**: arXiv (Jun 2026)
- **Abstract**: PCMA learns coordinated agent-specific preferences for complementary trade-offs in multi-objective MARL. Experiments on cooperative MOMA environments and traffic control.
- **Link**: [arXiv:2606.14693](https://arxiv.org/abs/2606.14693)

## 2. Game AI Bots — LLM-Powered Agents & NPC Intelligence

### GamingAgent / lmgame-Bench: How Good are LLMs at Playing Games?
- **Authors**: Lanxiang Hu, Mingjia Huo, Yuxuan Zhang, Haoyang Yu, Eric P. Xing, Ion Stoica, Tajana Rosing, Haojian Jin, Hao Zhang
- **Affiliation**: UC San Diego, UC Berkeley, CMU
- **Venue**: arXiv (May 2025)
- **Abstract**: Suite of platformer, puzzle, and narrative games via Gym-style API. Tests 13 leading models; finds RL on a single game transfers to unseen games and external planning tasks. Addresses brittle vision perception, prompt sensitivity, data contamination.
- **Innovation**: GamingAgent workflow (gaming harness) improves VLM gaming performance; standardized benchmark for LLM game-playing.
- **Link**: [arXiv:2505.15146](https://arxiv.org/abs/2505.15146) | [GitHub](https://github.com/lmgame-org/GamingAgent)

### Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games
- **Authors**: Dongmin Park, Minkyu Kim, Beongjun Choi, et al.
- **Affiliation**: KRAFTON
- **Venue**: arXiv (Jun 2025, v3 Apr 2026)
- **Abstract**: 12 popular video games covering all major genres with MCP-based plug-and-play interface. Releases fine-tuning dataset of expert LLM gameplay trajectories. Includes leaderboards, battle arenas, ablation studies.
- **Innovation**: First benchmark combining evaluation, agentic module study, and fine-tuning dataset for game LLM agents.
- **Link**: [arXiv:2506.03610](https://arxiv.org/abs/2506.03610) | [GitHub](https://github.com/krafton-ai/Orak)

### Fog of Love: Affinity-based Reinforcement Learning in a Game Environment
- **Authors**: Ajay Vishwanath, Christian Omlin
- **Affiliation**: — (Jun 2026)
- **Venue**: arXiv (Jun 2026)
- **Abstract**: Two-player multi-agent environment based on the role-playing board game Fog of Love. Uses affinity-based RL with policy regularization for virtuous agent behavior. Agents compete for individual virtues while cooperating on relationship satisfaction.
- **Innovation**: Complex multi-agent game environment for studying virtuous AI behavior; MADDPG agents with localized affinities.
- **Link**: [arXiv:2606.04750](https://arxiv.org/abs/2606.04750)

### Brain Alignment of Vision-Language and Action Models During Naturalistic Gameplay
- **Authors**: Subba Reddy Oota, Anant Khandelwal, Khushbu Pahwa, et al.
- **Affiliation**: IIT Hyderabad, JHU, IIT Delhi, IIIT Hyderabad, Microsoft
- **Venue**: arXiv (May 2026)
- **Abstract**: fMRI study of VLM and LAM brain alignment during Atari gameplay. Both foundation model families outperform RL baselines in voxel-wise encoding. Action-specialized fine-tuning reorganizes representations toward action-relevant neural computations.
- **Innovation**: First brain alignment comparison of VLMs and large action models during interactive gameplay.
- **Link**: [arXiv:2605.19352](https://arxiv.org/abs/2605.19352)

### Predicting Decisions of AI Agents from Limited Interaction
- **Authors**: Eilam Shapira, Moshe Tennenholtz, Roi Reichart
- **Affiliation**: Technion
- **Venue**: arXiv (May 2026)
- **Abstract**: Target-adaptive text-tabular prediction for modeling LLM agents in bargaining and negotiation games. Uses tabular foundation model with LLM-as-Observer for decision prediction. Trained on 13 frontier-LLM agents, tested on 91 held-out agents.
- **Innovation**: Formulating counterpart prediction as target-adaptive text-tabular task; LLM hidden states as decision-oriented features.
- **Link**: [arXiv:2605.12411](https://arxiv.org/abs/2605.12411)

## 3. Game Foundation Models & World Models

### Agent World Model: Infinity Synthetic Environments for Agentic RL
- **Authors**: Zhaoyang Wang, Canwen Xu, Boyi Liu, Yite Wang, Siwei Han, Zhewei Yao, Huaxiu Yao, Yuxiong He
- **Affiliation**: Snowflake, UNC Chapel Hill
- **Venue**: ICML 2026
- **Abstract**: Fully synthetic environment generation pipeline scaling to 1,000 environments for multi-turn tool-use agents. Code-driven with databases for reliable state transitions. Large-scale RL training yields strong out-of-distribution generalization on three benchmarks.
- **Innovation**: Synthetic environment generation for agentic RL training at scale; database-backed environments more reliable than LLM-simulated.
- **Link**: [arXiv:2602.10090](https://arxiv.org/abs/2602.10090) | [GitHub](https://github.com/Snowflake-Labs/agent-world-model)

### Optimistic World Models: Efficient Exploration in Model-Based Deep RL
- **Authors**: Akshay Mete, Shahid Aamir Sheikh, Tzu-Hsiang Lin, Dileep Kalathil, P. R. Kumar
- **Affiliation**: Texas A&M University
- **Venue**: arXiv (Feb 2026)
- **Abstract**: Brings reward-biased MLE (RBMLE) from adaptive control into deep RL. Optimism incorporated directly into model learning via optimistic dynamics loss. Plug-and-play with DreamerV3 and STORM architectures. Significant improvements in sample efficiency and cumulative return.
- **Innovation**: Fully gradient-based optimism without uncertainty estimates or constrained optimization; applicable to world model frameworks.
- **Link**: [arXiv:2602.10044](https://arxiv.org/abs/2602.10044)

### RePAIR: Self-Supervised Representation Learning in Chess
- **Authors**: Christoph Koller, Johannes Fürnkranz, Timo Bertram
- **Affiliation**: Johannes Kepler University Linz
- **Venue**: IEEE Conference on Games 2026 (oral)
- **Abstract**: Synthesizes MAE, JEPA, and BERT for self-supervised representation learning on chess positions. Encoder refines board representations with meaningful chess concepts emerging in latent space. Reconstructs masked board states without costly RL.
- **Innovation**: Self-supervised alternative to RL-based chess representation; lightweight Predictor repairs sequence gaps in embedding space.
- **Link**: [arXiv:2606.11860](https://arxiv.org/abs/2606.11860)

## 4. Procedural Content Generation

### Multi-task Procedural Content Generation with Reinforcement Learning
- **Authors**: — (multiple)
- **Affiliation**: —
- **Venue**: Scientific Reports (Apr 2026)
- **Abstract**: Language-based PCGRL framework using DeBERTa encoder and multi-objective training. Dataset of 14,000+ command-level pairs in Super Mario environment. Evaluates single-task, collective, combinatorial, paraphrase, and extra-domain generalization.
- **Innovation**: Semantic alignment between linguistic commands and quantitative game surface features for PCG.
- **Link**: [Nature Scientific Reports](https://www.nature.com/articles/s41598-026-48234-7)

### IPCGRL: Language-Instructed RL for Procedural Level Generation
- **Authors**: In-Chang Baek, Sung-Hyun Kim, Seo-Young Lee, Dong-Hyeon Kim, Kyung-Joong Kim
- **Affiliation**: —
- **Venue**: IEEE CoG 2025
- **Abstract**: Instruction-based PCG via RL using sentence embedding model. Fine-tunes task-specific embedding representations. Up to 21.4% improvement in controllability and 17.2% in generalizability for unseen instructions.
- **Link**: [arXiv:2503.12358](https://arxiv.org/abs/2503.12358)

### PCGRLLM: LLM-Driven Reward Design for PCG RL
- **Authors**: In-Chang Baek et al.
- **Affiliation**: —
- **Venue**: arXiv (Feb 2025)
- **Abstract**: Uses LLMs to design reward functions for PCGRL agents. LLM generates and iteratively refines reward functions based on agent performance feedback.
- **Link**: [arXiv:2502.10906](https://arxiv.org/abs/2502.10906)

### Procedural Content Generation in Games: A Survey with Insights on Emerging LLM Integration
- **Authors**: — (multiple)
- **Affiliation**: —
- **Venue**: ResearchGate (Aug 2025)
- **Abstract**: Comprehensive survey comparing PCG algorithms: search-based, ML-based, noise functions, and LLMs. Provides timeline analysis and future research directions.
- **Link**: [ResearchGate](https://www.researchgate.net/publication/385888613)

## 5. Game Benchmarks & Evaluation

### lmgame-Bench (see Section 2)
- Benchmark for LLM/VLM game-playing agents with platformer, puzzle, and narrative games.

### Orak (see Section 2)
- 12-game benchmark across all major genres with MCP interface and fine-tuning dataset.

### GAMEBoT: Transparent Assessment of LLM Reasoning in Games
- **Authors**: Visual AI Lab
- **Affiliation**: —
- **Venue**: ACL 2025
- **Abstract**: Benchmark evaluating LLM reasoning through direct competition in 8 diverse games. Goes beyond win/loss to analyze intermediate reasoning steps. Features game logs and visualizations.
- **Link**: [arXiv:2412.13602](https://arxiv.org/abs/2412.13602) | [GitHub](https://github.com/Visual-AI/GAMEBoT)

### OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents
- **Note**: Mentioned in search results (aimodels.fyi, Jun 2026). A unified Unreal Engine 5 benchmark for evaluating VLM game agents.
- **Link**: Search "OmniGameArena" on arXiv.

## 6. Industry Game AI & Related Techniques

### Cooperative Long Rope Skipping via Multi-Agent RL (Marope)
- **Authors**: Zihao Wang, Shijie Peng, Kerui Wu, et al.
- **Affiliation**: Nanjing University
- **Venue**: arXiv (Jun 2026)
- **Abstract**: Hierarchical MARL framework for cooperative long rope skipping with Unitree G1 humanoids. Lower-level decentralized rope manipulation policies; upper-level centralized scheduling. Deployed on real robots.
- **Innovation**: First MARL for multi-humanoid cooperative athletic locomotion; sim-to-real transfer for rope skipping.
- **Link**: [arXiv:2606.08064](https://arxiv.org/abs/2606.08064)

### Modelling Opinion Dynamics at Scale with Deep MARL
- **Authors**: Lukas Seier, Brandon Kaplowitz, Sebastian Towers, Richard Bailey, Jakob Foerster
- **Affiliation**: University of Oxford
- **Venue**: arXiv (Jun 2026)
- **Abstract**: GPU-accelerated consensus game scaling to 1000 agents. Extends other-play to general-sum social interactions. Validated on Bluesky network data.
- **Link**: [arXiv:2606.07487](https://arxiv.org/abs/2606.07487)

## 7. Related Techniques — Exploration, World Models, Imitation

### Optimistic World Models (see Section 3)
- Model-based RL exploration via optimistic dynamics loss.

### From Zero to Hero: Training-Free Custom Concept Spawning in World Models (SPAWN)
- **Authors**: Kiymet Akdemir, Pinar Yanardag
- **Affiliation**: — (Jun 2026)
- **Venue**: arXiv (Jun 2026)
- **Abstract**: Training-free method for introducing user-specified visual concepts into autoregressive world models. Exploits pinned anchor in image-to-video backbone memory. Applications in gaming, interactive storytelling.
- **Link**: [arXiv:2606.02575](https://arxiv.org/abs/2606.02575)

### GARL: Game-Theoretic Reinforcement Learning for Multi-Agent Strategic Prioritisation
- **Authors**: Yuxiao Ye, Yiwen Zhang, Huiyuan Xie, Yuqin Huang, Zhiyuan Liu
- **Affiliation**: — (Jun 2026)
- **Venue**: arXiv (Jun 2026)
- **Abstract**: Formalises strategic prioritisation as a two-stage game where competing agents allocate resources over candidates. Game-theoretic utilities converted into role-specific RL signals.
- **Link**: [arXiv:2606.05002](https://arxiv.org/abs/2606.05002)

---

## Summary Statistics

| Category | Papers |
|----------|--------|
| Self-Play & Multi-Agent RL | 8 |
| LLM Game AI Bots / NPCs | 5 |
| Foundation Models & World Models | 3 |
| Procedural Content Generation | 4 |
| Game Benchmarks | 4 |
| Industry Game AI | 2 |
| Related Techniques | 3 |
| **Total** | **29** |

## Key Trends

1. **Self-play for reasoning**: SPIRAL and MARSHAL establish self-play on zero-sum games as a powerful method for developing transferable reasoning in LLMs, with game-trained agents outperforming SFT and RLVR baselines on math/QA benchmarks.
2. **LLM game benchmarks mature**: lmgame-Bench, Orak, and GAMEBoT provide standardized evaluation suites, addressing contamination and prompt sensitivity issues.
3. **World models for agents**: Agent World Model and Optimistic World Models push synthetic environment generation and exploration for agentic RL.
4. **PCG with LLM integration**: Language-instructed PCGRL (IPCGRL) and LLM-driven reward design (PCGRLLM) bridge NLP and game content generation.
5. **Co-evolution in adversarial games**: FAMOU demonstrates LLM-driven code evolution discovering emergent tactical structures in competitive multi-agent settings.
