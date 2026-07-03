---
title: "Game RL & Game AI Bot — Daily Survey (2026-07-03)"
type: synthesis
created: 2026-07-03
updated: 2026-07-03
sources: [arxiv.org]
tags: [game-rl, game-ai, reinforcement-learning, game-foundation-models, procedural-content-generation, game-benchmarks, self-play, multi-agent-rl]
---

# Game RL & Game AI Bot — Daily Survey (2026-07-03)

Covering ~40 papers across 7 categories from recent arXiv and proceedings (2025–2026).

---

## 1. Game RL — Reinforcement Learning in Games

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning
- **Authors**: Bo Liu, Leon Guertler, Simon Yu, Zichen Liu, Penghui Qi, Daniel Balcells, Mickel Liu, Cheston Tan, Weiyan Shi, Min Lin, Wee Sun Lee, Natasha Jaques
- **Affiliation**: Sea AI Lab / NUS / Google DeepMind
- **Venue**: ICLR 2026
- **Abstract**: Introduces SPIRAL, a self-play framework where LLMs learn by playing multi-turn zero-sum games (Kuhn Poker, TicTacToe, Simple Negotiation) against continuously improving versions of themselves. Proposes role-conditioned advantage estimation (RAE) to stabilize multi-agent training. Training Qwen3-4B on Kuhn Poker alone achieves 8.6% improvement on math and 8.4% on general reasoning, outperforming SFT on 25,000 expert trajectories.
- **Link**: [arXiv:2506.24119](https://arxiv.org/abs/2506.24119)

### Reinforcement Learning in Strategy-Based and Atari Games: A Review of Google DeepMind's Innovations
- **Authors**: Abdelrhman Shaheen, Anas Badr, Ali Abohendy, Hatem Alsaadawy, Nadine Alsayad, Ehab H. El-Shazly
- **Affiliation**: Egypt-Japan University of Science and Technology (E-JUST)
- **Venue**: arXiv (v2 Feb 2026)
- **Abstract**: Comprehensive review of AlphaGo, AlphaGo Zero, MuZero, MiniZero, and multi-agent models from Google DeepMind. Covers model-based, model-free, and DQN approaches for Atari and strategy games.
- **Link**: [arXiv:2502.10303](https://arxiv.org/abs/2502.10303)

### Augmenting Game AI with Deep Reinforcement Learning
- **Authors**: Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslén
- **Affiliation**: Embark Studios / King / various
- **Venue**: Conference on Games 2026 (Vision paper)
- **Abstract**: Framework for training RL models with requirements suited towards game AI and game development. Presents examples of RL-augmented game AI and identifies bottlenecks for deploying player-facing ML agents in modern games.
- **Link**: [arXiv:2606.20210](https://arxiv.org/abs/2606.20210)

### Yahtzee: Reinforcement Learning Techniques for Stochastic Combinatorial Games
- **Authors**: Nicholas Pape
- **Affiliation**: —
- **Venue**: arXiv (Dec 2025)
- **Abstract**: RL for stochastic combinatorial game Yahtzee. A2C achieves median 241.78 (within 5% of optimal DP 254.59). REINFORCE and PPO prove hyperparameter-sensitive. Highlights persistent long-horizon credit-assignment and exploration challenges.
- **Link**: [arXiv:2601.00007](https://arxiv.org/abs/2601.00007)

### A Comprehensive Review of Multi-Agent Reinforcement Learning in Video Games
- **Authors**: Zhengyang Li, Qijin Ji, Xinghong Ling, Quan Liu
- **Affiliation**: —
- **Venue**: IEEE Transactions on Games, 2025
- **Abstract**: Thorough examination of MARL from turn-based two-agent games to real-time multi-agent video games (FPS, RTS, MOBA). Covers AlphaStar, OpenAI Five, Rocket League, Minecraft, Quake III Arena, Dota 2, Honor of Kings. Proposes novel method to estimate game complexity.
- **Link**: [arXiv:2509.03682](https://arxiv.org/abs/2509.03682)

### Curiosity Driven Multi-agent Reinforcement Learning for 3D Game Testing
- **Authors**: Raihana Ferdous, Fitsum Kifetew, Davide Prandi, Angelo Susi
- **Affiliation**: CNR / FBK (Italy)
- **Venue**: ICSTW 2025
- **Abstract**: cMarlTest — curiosity-driven MARL for 3D game testing. Multiple collaborating agents achieve higher coverage and efficiency than single-agent RL.
- **Link**: [IEEE](https://doi.org/10.1109/ICSTW64639.2025.10962505)

### MARSHAL: Incentivizing Multi-Agent Reasoning via Self-Play
- **Authors**: —
- **Affiliation**: —
- **Venue**: ICLR 2026
- **Abstract**: Multi-agent reasoning benchmark and training framework using self-play dynamics.
- **Link**: [OpenReview](https://openreview.net/forum?id=GCd5v3ehmr)

### Game-RL: Synthesizing Multimodal Verifiable Rewards from Video Games for VLM Reasoning
- **Authors**: Jingqi Tong et al.
- **Affiliation**: —
- **Venue**: ICLR 2026 submitted
- **Abstract**: Proposes Code2Logic to adapt game code for synthesizing game reasoning tasks. GameQA dataset of 30 games and 158 tasks. RL training on GameQA boosts VLMs across 7 diverse vision-language benchmarks, demonstrating video games as valuable training resources for general reasoning.
- **Link**: [arXiv:2505.13886](https://arxiv.org/abs/2505.13886)

---

## 2. Game AI Bot — LLM-Powered Game Agents & NPC Intelligence

### A Survey on Large Language Model-Based Game Agents (LLMGAs)
- **Authors**: Sihao Hu, Tiansheng Huang, Gaowen Liu, Ramana Rao Kompella, Fatih Ilhan, Selim Furkan Tekin, Yichang Xu, Zachary Yahn, Ling Liu
- **Affiliation**: Georgia Tech / Cisco
- **Venue**: ACM Computing Surveys, 2026
- **Abstract**: Up-to-date review of LLM-based game agents through a unified reference architecture. Three core components: memory, reasoning, and perception-action interfaces. Multi-agent level covers communication protocols and organizational models. Challenge-centered taxonomy linking 6 game genres to dominant agent requirements.
- **Link**: [arXiv:2404.02039](https://arxiv.org/abs/2404.02039)

### GAMEBoT: Transparent Assessment of LLM Reasoning in Games
- **Authors**: Wenye Lin, Jonathan Roberts, Yunhan Yang, Samuel Albanie, Zongqing Lu, Kai Han
- **Affiliation**: —
- **Venue**: ACL 2025
- **Abstract**: Gaming arena for transparent assessment of LLM reasoning. Decomposes complex reasoning into modular subproblems with CoT prompts. Rule-based algorithms generate ground truth for intermediate reasoning steps. Benchmarks 17 LLMs across 8 games.
- **Link**: [ACL Anthology](https://aclanthology.org/2025.acl-long.378)

### Playing Repeated Games with Large Language Models
- **Authors**: Elif Akata et al.
- **Affiliation**: Helmholtz Munich / University of Tübingen
- **Venue**: Nature Human Behaviour, 2025
- **Abstract**: Behavioral game theory approach to studying LLMs. LLMs perform well in self-interested games (Prisoner's Dilemma) but struggle in coordination games (Battle of the Sexes). Proposes "social chain-of-thought" prompting for improved coordination.
- **Link**: [Nature](https://www.nature.com/articles/s41562-025-02172-y)

### Game Theory Meets Large Language Models: A Systematic Survey
- **Authors**: —
- **Affiliation**: —
- **Venue**: IJCAI 2025
- **Abstract**: Comprehensive survey on bidirectional relationship between LLMs and game theory — game-based evaluation, game-theoretic algorithmic innovations, LLM influence on traditional game models.
- **Link**: [IJCAI](https://www.ijcai.org/proceedings/2025/1184.pdf)

### Advanced Game-Theoretic Frameworks for Multi-Agent AI Challenges: A 2025 Outlook
- **Authors**: Pavel Malinovskiy
- **Affiliation**: —
- **Venue**: IRJETS, March 2025
- **Abstract**: Robust theoretical tools for aligning strategic interaction in uncertain, partially adversarial contexts.
- **Link**: [arXiv:2506.17348](https://arxiv.org/abs/2506.17348)

---

## 3. Game Foundation Models — Generalist Game Agents

### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi Fan
- **Affiliation**: NVIDIA / Stanford / Caltech / UChicago / UT Austin
- **Venue**: CVPR 2026
- **Abstract**: Vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games. Internet-scale video-action dataset with automatically extracted player actions. Unified vision-action model with large-scale behavior cloning. Up to 52% relative improvement on unseen games. Open-source release of dataset, evaluation suite, and model weights.
- **Link**: [arXiv:2601.02427](https://arxiv.org/abs/2601.02427)

### Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents
- **Authors**: Zihao Wang, Xujing Li, Yining Ye, Junjie Fang, et al. (27 authors)
- **Affiliation**: ByteDance Seed
- **Venue**: arXiv (Oct 2025)
- **Abstract**: Generalist game agent with unified keyboard-mouse action space enabling pre-training across OS, web, and simulation games. Pre-trained on 500B+ tokens. Decaying continual loss reduces causal confusion; Sparse-Thinking balances reasoning depth and cost. 2× success rate on Minecraft vs SOTA. Outperforms GPT-5, Gemini-2.5-Pro, Claude-4-Sonnet in FPS benchmarks.
- **Link**: [arXiv:2510.23691](https://arxiv.org/abs/2510.23691)

### Towards Generalist Game Players: An Investigation of Foundation Models in the Game Multiverse
- **Authors**: Kuan Zhang, Dongchen Liu, Qiyue Zhao, Tianyu Xin, Yue Su, Haisheng Wang, Han Yin, Hongbo Ma, Peize Li, Tianjun Gu, Xiangnan Wu, Xinran Zhang, Yongxuan Li, Zirong Chen, Yiming Li
- **Affiliation**: Tsinghua University
- **Venue**: arXiv (May 2026)
- **Abstract**: Comprehensive review proposing four-era evolutionary framework, four-pillar pipeline (Dataset, Model, Harness, Benchmark), five fundamental trade-offs, and five-level roadmap from single-game mastery to creator stage. Frames game multiverse as key AGI testbed.
- **Link**: [arXiv:2605.09965](https://arxiv.org/abs/2605.09965)

### Scaling Behavior Cloning Improves Causal Reasoning: An Open Model for Real-Time Video Game Playing
- **Authors**: Yuguang Yue, Irakli Salia, Samuel Hunt, Chris Green, Wenzhe Shi, Jonathan J. Hunt
- **Affiliation**: —
- **Venue**: arXiv (2026)
- **Abstract**: Open recipe for training a video game playing foundation model for real-time inference on consumer GPU. Scaling behavior cloning improves causal reasoning.
- **Link**: [arXiv](https://arxiv.org/abs/2606.20210) (related)

---

## 4. Procedural Content Generation (PCG)

### Procedural Content Generation in Games: A Survey with Insights on Emerging LLM Integration
- **Authors**: Mahdi Farrokhi Maleki, Richard Zhao
- **Affiliation**: University of Calgary
- **Venue**: AAAI AIIDE 2024
- **Abstract**: Comprehensive PCG survey covering search-based, ML-based, noise-based methods and the newcomer LLMs. Detailed discussion on combined methods. Identifies gaps and future research directions.
- **Link**: [arXiv:2410.15644](https://arxiv.org/abs/2410.15644) / [AAAI](https://doi.org/10.1609/aiide.v20i1.31877)

### IPCGRL: Language-Instructed Reinforcement Learning for Procedural Level Generation
- **Authors**: In-Chang Baek, Sung-Hyun Kim, Seo-Young Lee, Dong-Hyeon Kim, Kyung-Joong Kim
- **Affiliation**: —
- **Venue**: Conference on Games 2025
- **Abstract**: Instruction-based PCG via RL with sentence embedding model. Fine-tunes task-specific embedding representations. Up to 21.4% improvement in controllability and 17.2% improvement in generalizability for unseen instructions.
- **Link**: [arXiv:2503.12358](https://arxiv.org/abs/2503.12358)

### PCGRLLM: Large Language Model-Driven Reward Design for Procedural Content Generation Reinforcement Learning
- **Authors**: —
- **Affiliation**: NYU Game Innovation Lab
- **Venue**: arXiv (2025)
- **Abstract**: LLMs design reward functions for PCGRL agents. Demonstrates automated reward shaping for level generation tasks.
- **Link**: [arXiv:2502.10906](https://arxiv.org/abs/2502.10906)

---

## 5. Game Benchmarks & Evaluation

### Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games
- **Authors**: Dongmin Park et al.
- **Affiliation**: KRAFTON
- **Venue**: ICLR 2026
- **Abstract**: Benchmark for training and evaluating LLM agents across 12 popular video games spanning all major genres. MCP-based plug-and-play interface. Releases fine-tuning dataset of expert LLM gameplay trajectories. Includes game leaderboards, LLM battle arenas, and ablation studies.
- **Link**: [arXiv:2506.03610](https://arxiv.org/abs/2506.03610)

### AI GameStore: Scalable, Open-Ended Evaluation of Machine General Intelligence with Human Games
- **Authors**: Lance Ying, Ryan Truong, Prafull Sharma, Kaiya Ivy Zhao, Nathan Cloos, Kelsey R. Allen, Thomas L. Griffiths, Katherine M. Collins, José Hernández-Orallo, Phillip Isola, Samuel J. Gershman, Joshua B. Tenenbaum
- **Affiliation**: MIT / Harvard / UBC / Princeton / Cambridge / UPV
- **Venue**: arXiv (Feb 2026)
- **Abstract**: Platform using LLMs with humans-in-the-loop to synthesize new human games for AI evaluation. Generated 100 games based on App Store and Steam top charts. Best VLMs achieved <10% of human average score on most games. Struggles with world-model learning, memory, and planning.
- **Link**: [arXiv:2602.17594](https://arxiv.org/abs/2602.17594)

### LMGame Bench and GamingAgent
- **Authors**: —
- **Affiliation**: LMGame / ICLR 2026
- **Venue**: ICLR 2026
- **Abstract**: Repository enabling LLM/VLM-based agents in standardized interactive gaming environments. Evaluates SOTA models with diverse video games. Includes GamingAgent workflow for improved gaming performance. Supports computer-use agents for gaming.
- **Link**: [GitHub](https://github.com/lmgame-org/GamingAgent) / [arXiv:2505.15146](https://arxiv.org/pdf/2505.15146)

### Decrypto: A Benchmark for Multi-Agent Reasoning and Theory of Mind
- **Authors**: Andrei Lupu, Timon Willi, Jakob Foerster
- **Affiliation**: Facebook Research (Meta) / Oxford
- **Venue**: arXiv (2025)
- **Abstract**: Game-based benchmark for multi-agent reasoning and Theory of Mind in LLMs. Based on the Decrypto board game. Evaluates cooperation, competition, and ToM capabilities. Framework for studying ToM in LLMs with multiple experiments.
- **Link**: [arXiv:2506.20664](https://arxiv.org/abs/2506.20664)

### GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents
- **Authors**: Mingyu Ouyang et al.
- **Affiliation**: NUS
- **Venue**: arXiv (2026)
- **Abstract**: Benchmark designed for standardized and verifiable evaluation of MLLMs as generalist game agents in browser environments.
- **Link**: [arXiv](https://arxiv.org/abs/2606.05449)

### Agent Skill Evaluation and Evolution: Frameworks and Benchmarks
- **Authors**: Kexin Ding, Yang Zhou, Can Jin, Feng Tong, Mu Zhou, Dimitris N. Metaxas
- **Affiliation**: —
- **Venue**: arXiv (Jun 2026)
- **Abstract**: Survey of skill evolution paradigms (execution feedback, trajectory distillation, compression, RL) and six skill-centric benchmark categories.
- **Link**: [arXiv:2606.11435](https://arxiv.org/abs/2606.11435)

---

## 6. Industry Game AI

### PUBG Ally (KRAFTON) — Orak
- **Affiliation**: KRAFTON
- **Venue**: ICLR 2026
- **Abstract**: Production-grade game AI benchmark from KRAFTON (PUBG publisher). Orak benchmark covers 12 games with MCP-based agent evaluation framework.
- **Link**: [arXiv:2506.03610](https://arxiv.org/abs/2506.03610)

### NVIDIA ACE (Avatar Cloud Engine) — NitroGen
- **Affiliation**: NVIDIA
- **Venue**: CVPR 2026
- **Abstract**: NVIDIA's generalist gaming agent model (NitroGen) represents industry push toward foundation models for game AI. Open-source release targets game developers and researchers.
- **Link**: [arXiv:2601.02427](https://arxiv.org/abs/2601.02427)

### ByteDance Seed — Game-TARS
- **Affiliation**: ByteDance
- **Venue**: arXiv (Oct 2025)
- **Abstract**: Production-scale generalist game agent from ByteDance's Seed team. Unified action space for cross-domain gameplay.
- **Link**: [arXiv:2510.23691](https://arxiv.org/abs/2510.23691)

### Game Theory and Agentic AI — Google DeepMind
- **Venue**: 2026
- **Abstract**: DeepMind's research on LLMs rewriting their own game theory algorithms, outperforming expert-designed algorithms.
- **Link**: [MarkTechPost](https://www.marktechpost.com/2026/04/03/google-deepminds-research-lets-an-llm-rewrite-its-own-game-theory-algorithms-and-it-outperformed-the-experts/)

---

## 7. Related Techniques

### Self-Play RL

**A Survey on Self-play Methods in Reinforcement Learning**
- **Authors**: Ruize Zhang, Zelai Xu, Chengdong Ma, Chao Yu, Wei-Wei Tu, Wenhao Tang, Shiyu Huang, Deheng Ye, Wenbo Ding, Yaodong Yang, Yu Wang
- **Affiliation**: Tsinghua / Tencent AI Lab / various
- **Venue**: arXiv (v4 Oct 2025)
- **Abstract**: Comprehensive survey of self-play methods in MARL. Unified framework classifying existing self-play algorithms. Bridges gap between algorithms and practical implications. Covers Go, poker, video games.
- **Link**: [arXiv:2408.01072](https://arxiv.org/abs/2408.01072)

### Multi-Agent RL

**A Multi-Agent Reinforcement Learning Framework for Exploring Dominant Strategies in Iterated and Evolutionary Games**
- **Authors**: —
- **Affiliation**: —
- **Venue**: Nature Communications, 2025
- **Abstract**: MARL approach exploring dominant strategies in iterated and evolutionary games. Uncovers memory-two bilateral reciprocity (MTBR) strategy, consistently achieving higher payoffs.
- **Link**: [Nature](https://www.nature.com/articles/s41467-025-67178-6)

**A Review of Multi-Agent Reinforcement Learning Algorithms**
- **Authors**: —
- **Affiliation**: —
- **Venue**: Electronics (MDPI), 2025
- **Abstract**: Systematic review of MARL algorithms (value-based, policy-based, actor-critic). Classification by reward: fully cooperative, fully competitive, mixed. Discusses dimensionality, non-stationarity, partial observability, scalability.
- **Link**: [MDPI](https://www.mdpi.com/2079-9292/14/4/820)

### World Models & Model-Based RL

**Scaling Offline Model-Based RL via Jointly-Optimized World-Action Model Pretraining (JOWA)**
- **Authors**: Jie Cheng, Ruixi Qiao, Yingwei Ma, Binhua Li, Gang Xiong, Qinghai Miao, Yongbin Li, Yisheng Lv
- **Affiliation**: —
- **Venue**: arXiv (v4 Jan 2026)
- **Abstract**: Offline model-based RL pretrained on multiple Atari games (6B tokens). Jointly-optimized world-action model with shared transformer backbone. 150M param agent achieves 78.9% human-level on pretrained games using only 10% data. Sample-efficiently transfers to novel games with 5k offline fine-tuning data.
- **Link**: [arXiv:2410.00564](https://arxiv.org/abs/2410.00564)

### Theory of Mind in Game Agents

**Evaluating Theory of Mind and Internal Beliefs in LLM-Based Multi-Agent Systems**
- **Authors**: Adam Kostka, Jarosław A. Chudziak
- **Affiliation**: —
- **Venue**: ICCCI 2025
- **Abstract**: Novel multi-agent architecture integrating ToM, BDI-style internal beliefs, and symbolic solvers for logical verification in resource allocation problems.
- **Link**: [arXiv:2603.00142](https://arxiv.org/abs/2603.00142)

### Foundation Model Self-Play

**Foundation Model Self-Play: Open-Ended Strategy Innovation via Foundation Models**
- **Authors**: Aaron Dharna, Cong Lu, Jeff Clune
- **Affiliation**: —
- **Venue**: RLJ 2025
- **Abstract**: Self-play using foundation models for open-ended strategy innovation.
- **Link**: [RLJ](https://rlj.cs.umass.edu/2025/2025issue.html)

---

## Summary of Key Trends

| Trend | Representative Papers |
|-------|----------------------|
| **Self-play + RL as LLM reasoning paradigm** | SPIRAL, MARSHAL, Foundation Model Self-Play |
| **Generalist game foundation models** | NitroGen (NVIDIA), Game-TARS (ByteDance), Towards Generalist Game Players (Tsinghua) |
| **VLM agents for long-horizon gameplay** | Game-RL, Game-TARS, LMGame Bench |
| **Game benchmarks standardizing** | Orak (KRAFTON), AI GameStore (MIT/Harvard), GameWorld, Decrypto (Meta) |
| **PCG with LLMs maturing** | PCGRLLM, IPCGRL, PCG Survey with LLM insights |
| **Game theory + LLMs intersection** | GAMEBoT, Repeated Games with LLMs, Game Theory Meets LLMs |
| **Industry deployment accelerating** | NVIDIA NitroGen, ByteDance Game-TARS, KRAFTON Orak |
| **MARL surveys consolidating field** | Comprehensive MARL in Video Games (IEEE ToG), Self-Play Survey, MARL Algorithms Review |
| **World models for games** | JOWA (offline MBRL), RLC 2026 Workshop on Generative World Models |
