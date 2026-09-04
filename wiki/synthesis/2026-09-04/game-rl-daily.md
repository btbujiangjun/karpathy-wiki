---
title: "Game RL & Game AI Bot — Daily Synthesis (2026-09-04)"
type: synthesis
created: 2026-09-04
updated: 2026-09-04
tags: [game-rl, game-ai, game-foundation-models, game-benchmark, pcg, industry, agentic-rl, self-play, daily-digest]
---

# Game RL & Game AI Bot — Daily Synthesis (2026-09-04)

Comprehensive survey of recent arXiv papers (2025–2026) across Game RL, Game AI Bot, Game Foundation Models, Procedural Content Generation, Game Benchmarks, Industry Game AI, and related techniques. Prioritized fresh / high-impact work; cross-referenced against existing wiki entries to avoid duplication.

---

## 1. Game RL — Reinforcement Learning in Games

### 1.1 A Comprehensive Review of Multi-Agent Reinforcement Learning in Video Games
- **Authors**: Zhengyang Li, Qijin Ji, Xinghong Ling, Quan Liu
- **Affiliation**: *(unverified)*
- **Venue**: IEEE Transactions on Games, 2025
- **arXiv**: https://arxiv.org/abs/2509.03682
- **Abstract**: Comprehensive survey of MARL applications from turn-based two-agent games to real-time multi-agent video games (Sports, FPS, RTS, MOBA). Covers AlphaStar (StarCraft II), OpenAI Five (Dota 2), and achievements in Rocket League, Minecraft, Quake III Arena, Honor of Kings. Analyzes critical challenges: nonstationarity, partial observability, sparse rewards, team coordination, scalability. Proposes a novel method to estimate game complexity.
- **Key innovations**: Game complexity estimation method; taxonomy from turn-based to real-time MARL; coverage of nonstationary/partially-observable challenges.

### 1.2 SPA: Internalizing World Models via Self-Play Finetuning for Agentic RL
- **Authors**: Shiqi Chen, Tongyao Zhu, Zian Wang, Jinghan Zhang, Teng Xiao, Kangrui Wang, Siyang Gao, Yee Whye Teh et al.
- **Affiliation**: *(multiple institutions, unverified)*
- **Venue**: ICLR 2026 (Poster)
- **arXiv**: https://arxiv.org/abs/2510.15047
- **Abstract**: Proposes SPA — a framework that equips LLM agents with an internal world model via self-play supervised finetuning (SFT) before RL optimization. The world model decomposes into state representation and transition modeling. Self-play SFT cold-starts the policy, then PPO uses the internal world model to simulate future states. Achieves Pass@1 59.8 (vs vanilla RL 25.6) and Pass@8 69.5 (vs 34.0) on Sokoban-like environments.
- **Key innovations**: Self-play as world-model training substrate; "exploration before exploitation" — self-play SFT yields reusable scaffold that diversifies reasoning; ablation shows transition modelling is pivotal (masking state loss → no PPO gain).

### 1.3 Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL
- **Authors**: Chengshuai Shi, Wenzhe Li, Xinran Liang, Yizhou Lu, Wenjia Yang, Ruirong Feng, Seth Karten, Ziran Yang, Zihan Ding, Gabriel Sarch, Danqi Chen, Karthik Narasimhan, Chi Jin
- **Affiliation**: Princeton University (inferred from authors)
- **Venue**: arXiv, May 2026
- **arXiv**: https://arxiv.org/abs/2605.00347
- **Abstract**: Studies RL-based training of VLMs for long-horizon decision-making in Super Mario Land (100+ turns). Proposes adapted PPO variant with lightweight turn-level critic, substantially improving training stability over GRPO/Reinforce++. Shows pretrained VLMs provide strong action priors, improving sample efficiency vs training from scratch. Odysseus framework achieves ≥3× average game progress vs frontier models.
- **Key innovations**: Turn-level critic for VLM RL stability; VLM action priors reduce need for manual action engineering; cross-game generalization while maintaining general capabilities.

### 1.4 Hierarchical Control in Multi-Agent Games: LLM-based Planning and RL Execution
- **Authors**: Jannik Hösch, Alessandro Sestini, Florian Fuchs, Amir Baghi, Joakim Bergdahl, Iolanda Leite, Konrad Tollmar et al.
- **Affiliation**: Electronic Arts (EA), Stockholm (inferred)
- **Venue**: arXiv, June 2026
- **arXiv**: https://arxiv.org/abs/2606.20014
- **Abstract**: Proposes a hierarchical framework for multi-agent games where LLMs handle high-level planning and RL handles low-level execution. Combines the reasoning/language capabilities of LLMs with the precise motor control of RL policies.
- **Key innovations**: LLM planner + RL executor hierarchy for multi-agent game control; bridges language-level strategy with continuous action execution.

### 1.5 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors**: *(multiple, unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: ICLR 2026 (Poster)
- **arXiv**: https://openreview.net/forum?id=7Yayy5fNLg
- **Abstract**: Shows that self-play on zero-sum games incentivizes reasoning capabilities in LLMs through multi-agent, multi-turn reinforcement learning. Self-play creates natural curriculum and increasingly challenging opponents.
- **Key innovations**: Self-play as reasoning catalyst for LLMs; zero-sum game setting as natural RL training ground.

---

## 2. Game AI Bot — LLM-Powered Game Agents

### 2.1 Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with LLMs
- **Authors**: Chee Wei Tan, Yuchen Wang, Shangxin Guo
- **Affiliation**: *(unverified)*
- **Venue**: arXiv, April 2026
- **arXiv**: https://arxiv.org/abs/2604.21896
- **Abstract**: Extends Shannon's taxonomy of game-playing machines using LLMs. Introduces Nemobot — a programmable environment for experimenting with tool-augmented generation and fine-tuning of strategic game agents. Demonstrates how AI agents achieve self-programming by integrating crowdsourced learning and human creativity. Covers strategic games through role-playing games.
- **Key innovations**: LLM-based extension of Shannon's game taxonomy; programmable prompt framework; crowdsourced strategy refinement for self-programming agents.

### 2.2 Augmenting Game AI with Deep Reinforcement Learning
- **Authors**: Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslén
- **Affiliation**: Electronic Arts (EA), Stockholm, Sweden
- **Venue**: Conference on Games (CoG) 2026
- **arXiv**: https://arxiv.org/abs/2606.20210
- **Abstract**: Vision paper proposing a framework for training RL models suited to game AI and game development. Focuses on producing believable characters (not superhuman play) for player-facing bots. Identifies bottlenecks: training-time stability, behavioral drift, plasticity limitations. Describes practical deployment of ML agents in modern AAA games.
- **Key innovations**: Production-oriented RL for believable game AI (vs competitive play); addresses drift/plasticity in live deployment; identifies industry bottlenecks.

### 2.3 GamingAgent: LLM/VLM Gaming Agents and Model Evaluation Through Games
- **Authors**: *(lmgame-org)*
- **Affiliation**: lmgame-org (inferred)
- **Venue**: ICLR 2026
- **GitHub**: https://github.com/lmgame-org/GamingAgent
- **Abstract**: Framework for building and evaluating LLM/VLM gaming agents across diverse game environments. Provides plug-and-play interfaces for connecting game environments with language model agents.
- **Key innovations**: Unified evaluation framework for LLM game agents; environment-agnostic agent interface.

### 2.4 Brain Alignment of Reasoning and Action Representations from VLMs During Gameplay
- **Authors**: *(multiple, unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv, May 2026
- **arXiv**: https://arxiv.org/abs/2605.19352
- **Abstract**: Studies how reasoning and action representations align between VLMs and action models during naturalistic gameplay. Investigates neural correlates of decision-making in game-playing AI systems.
- **Key innovations**: Neuroscience-inspired alignment analysis of game AI representations.

---

## 3. Game Foundation Models — Generalist Game Players

### 3.1 NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi "Jim" Fan
- **Affiliation**: NVIDIA, Stanford, Caltech, UChicago, UT Austin
- **Venue**: CVPR 2026 (Oral)
- **arXiv**: https://arxiv.org/abs/2601.02427
- **Abstract**: Vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games. Three key ingredients: (1) internet-scale video-action dataset from public gameplay videos, (2) multi-game benchmark for cross-game generalization, (3) unified vision-action model via large-scale behavior cloning. Achieves up to 52% relative improvement in task success rates over models trained from scratch on unseen games. Open-source dataset, benchmark, and weights.
- **Key innovations**: 40K-hour gameplay dataset with auto-extracted actions; cross-game generalization benchmark; unified vision-action architecture via BC; open weights.

### 3.2 Towards Generalist Game Players: An Investigation of Foundation Models in the Game Multiverse
- **Authors**: Kuan Zhang, Dongchen Liu, Qiyue Zhao, Tianyu Xin, Yue Su, Haisheng Wang, Han Yin, Hongbo Ma, Peize Li, Tianjun Gu, Xiangnan Wu, Xinran Zhang, Yongxuan Li, Zirong Chen, Yiming Li
- **Affiliation**: Tsinghua University (College of AI), University of Hong Kong (MMLab), UCAS
- **Venue**: arXiv, May 2026
- **arXiv**: https://arxiv.org/abs/2605.09965
- **Abstract**: Comprehensive survey proposing a four-era evolution framework (Symbolic → DRL → Foundation Models → Demiurge/Creator) unified under Goal-Conditioned POMDP. Four-pillar pipeline: Dataset, Model, Harness, Benchmark. Identifies five fundamental trade-offs (Reasoning vs. Reactivity, Scale vs. Fidelity vs. Diversity, Breadth vs. Depth, etc.) and charts a five-level roadmap from single-game mastery to the Creator stage. First systematic investigation of LFMs as generalist game players through end-to-end lifecycle.
- **Key innovations**: Four-era evolutionary framework; five trade-offs taxonomy; five-level AGI roadmap for games; Dataset-Model-Harness-Benchmark coupled loop.

### 3.3 MARL-GPT: Foundation Model for Multi-Agent Reinforcement Learning
- **Authors**: Maria Nesterova, Mikhail Kolosov, Anton Andreychuk, Egor Cherepanov, Oleg Bulichev, Alexey Kovalev, Konstantin Yakovlev, Aleksandr Panov, Alexey Skrynnik
- **Affiliation**: *(unverified)*
- **Venue**: AAMAS 2026 (AAAI Track)
- **arXiv**: https://arxiv.org/abs/2604.05943
- **Abstract**: Single GPT-based model trained to perform across diverse MARL environments (SMACv2, Google Research Football, POGEMA) using offline RL on expert trajectories (400M–1B). Single transformer-based observation encoder with no task-specific tuning achieves competitive performance vs specialized baselines. Paves the way to fundamental MARL model.
- **Key innovations**: Multi-task MARL foundation model; offline RL scaling on expert trajectories; task-agnostic encoder for heterogeneous game environments.

### 3.4 A Survey on Large Language Model-Based Game Agents
- **Authors**: *(multiple, unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: ACM Computing Surveys, 2026
- **arXiv**: https://arxiv.org/abs/2404.02039 (v5)
- **Abstract**: Comprehensive survey on LLM-based game agents. At single-agent level: memory, reasoning, perception-action interfaces. At multi-agent level: communication protocols, organizational models. Challenge-centered taxonomy linking six game genres to dominant agent requirements. Updated 2026 edition.
- **Key innovations**: Memory-Reasoning-Perception taxonomy; six-genre challenge mapping; multi-agent communication framework.

---

## 4. Procedural Content Generation (PCG)

### 4.1 PCGRLLM: LLM-Driven Reward Design for Procedural Content Generation RL
- **Authors**: In-Chang Baek, Sung-Hyun Kim, Sam Earle, Zehua Jiang, Jin-Ha Noh, Julian Togelius, Kyung-Joong Kim
- **Affiliation**: GIST (Gwangju, South Korea), New York University
- **Venue**: arXiv, February 2026
- **arXiv**: https://arxiv.org/abs/2502.10906
- **Abstract**: Uses LLMs to automatically design reward functions for PCGRL. Traditionally, reward design requires domain expertise and is time-consuming. The framework uses LLMs to iteratively generate, evaluate, and refine reward functions based on playtest results. Evaluated on gym-pcgrl environments (binary maps, narrow representation).
- **Key innovations**: LLM-driven reward generation for PCGRL; eliminates manual reward shaping; iterative refinement based on observed generation outcomes.

### 4.2 High Dimensional Procedural Content Generation
- **Authors**: Kaijie Xu et al.
- **Affiliation**: *(unverified)*
- **Venue**: FDG 2026 (Foundations of Digital Games)
- **arXiv**: https://arxiv.org/abs/2602.18943
- **Abstract**: Addresses limitations of geometry-first PCG formulations. Proposes Time Expanded Graph representation with A* search and dynamic programming for mechanics-aware generation. Handles time-dependent traversal, discrete interaction rules, and non-spatial state natively in the generator.
- **Key innovations**: Mechanics-native PCG (not just geometry); Time Expanded Graph for temporal level structure; A* + DP search.

### 4.3 Playing the Imitation Game: How Perceived Generated Content Shapes Player Experience
- **Authors**: Mahsa Bazzaz, Seth Cooper
- **Affiliation**: Northeastern University (inferred from Cooper)
- **Venue**: CHI 2026 (April 2026, Barcelona)
- **arXiv**: https://arxiv.org/abs/2606.14254 (listed as 2602.14254)
- **Abstract**: Studies whether players can distinguish human-created from AI-generated game levels and how perception affects experience. Found that perceived AI-generated levels rated more frustrating/challenging — negative bias appears spontaneously based on unreliable "human-likeness" cues. Players who believed levels were AI-generated rated them as less fun. Explores the gap between PCG and generative AI perceptions.
- **Key innovations**: Perception bias study for generated game content; shows "belief effect" matters more than truth; implications for AI disclosure in games.

---

## 5. Game Benchmarks

### 5.1 GameCraft-Bench: Can Agents Build Playable Games End-to-End in a Real Game Engine?
- **Authors**: Tongxu Luo, Rongsheng Wang, Jiaxi Bi, Chenming Xu, Zhengyang Tang, Jianlong Chen, Juhao Liang, Ke Ji, Zhenyu Zhang, Xinyuan Wang, Tianyi Bai, Ziniu Li, Benyou Wang
- **Affiliation**: *(unverified)*
- **Venue**: arXiv, June 2026
- **arXiv**: https://arxiv.org/abs/2606.17861
- **Abstract**: Benchmark for evaluating agents on end-to-end game generation in Godot engine. 140 tasks across 15 game families. Three desiderata: Engine Grounding, Artifact Completeness, Interactive Verification. Strongest agent achieves only 41.46%; most score below 40%. Agents struggle with complete games, visual feedback, and coherent presentation despite recognizing individual mechanics.
- **Key innovations**: Real game engine (Godot) grounding; interaction-grounded evaluation via replayed demonstrations; reveals completion gap in game generation agents.

### 5.2 GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents
- **Authors**: Mingyu Ouyang, Siyuan Hu, Kevin Qinghong Lin, Hwee Tou Ng, Mike Zheng Shou
- **Affiliation**: National University of Singapore (inferred)
- **Venue**: arXiv, April 2026
- **arXiv**: https://arxiv.org/abs/2604.07429
- **Abstract**: Benchmark for MLLM game agents in browser environments. Two interfaces: (i) computer-use agents (keyboard/mouse), (ii) generalist agents via Semantic Action Parsing. 34 games, 170 tasks, state-verifiable metrics. Best agent far from human capabilities. Studies real-time interaction, context-memory sensitivity, action validity.
- **Key innovations**: Standardized, verifiable evaluation across 34 games; two agent interfaces (raw vs semantic); state-verifiable metrics for reproducibility.

### 5.3 OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics
- **Authors**: Mingxian Lin, Shengju Qian, Yuqi Liu, Yi-Hua Huang, Yiyu Wang, Wei Huang, Yitang Li, Fan Zhang, Zeyu Hu, Lingting Zhu
- **Affiliation**: *(unverified)*
- **Venue**: arXiv, June 2026
- **arXiv**: https://arxiv.org/abs/2606.09826
- **Abstract**: UE5-based benchmark with unified action interface (joystick inputs for all agents). Introduces Improvement Dynamics Curve (IDC) — multi-round reflection harness revealing how agents learn from mistakes. 12 games (7 solo, 3 PvP, 2 coop) + held-out variants to test generalization. Bounded skill prompts (≤500 tokens) force compression of learned strategies.
- **Key innovations**: IDC as evaluation protocol (score vs reflection round + held-out variants); bounded skill prompt for agent memory; unified UE5 action interface; PvP/coop coverage.

### 5.4 GameDevBench: Evaluating Agentic Capabilities Through Game Development
- **Authors**: Wayne Chi, Yixiong Fang, Arnav Yayavaram, Siddharth Yayavaram, Seth Karten, Qiuhong Anna Wei, Runkun Chen, Alexander Wang, Valerie Chen, Ameet Talwalkar, Chris Donahue
- **Affiliation**: Carnegie Mellon University (inferred from Talwalkar)
- **Venue**: arXiv, February 2026 (v2: June 2026)
- **arXiv**: https://arxiv.org/abs/2602.11103
- **Abstract**: 333 game development tasks derived from web/video tutorials. Tasks require multimodal understanding; average solution needs 3× more LOC than prior SE benchmarks. Best agent solves only 53.8%. Strong correlation between perceived difficulty and multimodal complexity. Introduces image/video feedback mechanisms improving GPT-5.4 from 41.1% to 52.0%.
- **Key innovations**: Game development as agent evaluation (not just gameplay); multimodal complexity as difficulty predictor; visual feedback boosts performance.

### 5.5 PokeGym: A Visually-Driven Long-Horizon Benchmark for Vision-Language Models
- **Authors**: *(multiple, unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv, April 2026
- **arXiv**: https://arxiv.org/abs/2604.08340
- **Abstract**: Long-horizon benchmark using Pokémon games for evaluating VLMs. Requires extended visual perception, strategic planning, and multi-step decision-making.
- **Key innovations**: Real-world long-horizon game benchmark; visually rich observation space.

### 5.6 Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games
- **Authors**: Dongmin Park, Minkyu Kim, Beongjun Choi, Junhyuck Kim et al.
- **Affiliation**: *(unverified)*
- **Venue**: arXiv, 2025
- **arXiv**: https://arxiv.org/abs/2506.03610
- **Abstract**: Benchmark for training/evaluating LLM agents across 12 popular video games spanning all major genres. Plug-and-play interface built on Model Context Protocol (MCP). Releases fine-tuning dataset of expert LLM gameplay trajectories.
- **Key innovations**: MCP-based agent interface; expert trajectory dataset for fine-tuning; all-genre coverage.

### 5.7 GBQA: Game Benchmark for Evaluating LLMs as Quality Assurance
- **Authors**: *(multiple, unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv, April 2026
- **arXiv**: https://arxiv.org/abs/2604.08340 (referenced via aimodels.fyi)
- **Abstract**: Quantifies LLM capabilities as game QA testers. Even Claude-4.6-Opus identifies only 48% of verifiable bugs in complex game environments.
- **Key innovations**: Game QA as LLM capability testbed; bug-detection benchmark.

---

## 6. Industry Game AI

### 6.1 Augmenting Game AI with Deep Reinforcement Learning (EA)
- **See Section 2.2 above** (arXiv:2606.20210)
- **Key industry insights**: EA's vision paper on deploying RL agents in AAA games; identifies production bottlenecks including training stability, behavioral drift, and plasticity in live environments.

### 6.2 Hierarchical Control in Multi-Agent Games (EA)
- **See Section 1.4 above** (arXiv:2606.20014)
- **Key industry insights**: EA's hierarchical LLM+RL approach for game character control; production-oriented architecture.

### 6.3 3M Parameters: Specialized Small Models vs Large Language Models for Real-Time Game Control
- **Authors**: *(multiple, unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv, April 2026
- **arXiv**: https://arxiv.org/abs/2604.07385
- **Abstract**: Compares small specialized models (3M parameters) against large LLMs for real-time game control. Demonstrates that specialized small models can achieve competitive performance at a fraction of the cost.
- **Key innovations**: Small model vs LLM trade-off analysis; real-time inference requirements for game AI.

---

## 7. Related Techniques

### 7.1 CDE: Curiosity-Driven Exploration for Efficient RL in LLMs
- **Authors**: *(multiple, unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: ICLR 2026
- **arXiv**: https://openreview.net/forum?id=5rXN5knHKW
- **Abstract**: Curiosity-driven exploration for RL with Verifiable Rewards (RLVR) in LLMs. Addresses exploration efficiency in reasoning tasks.
- **Key innovations**: Curiosity bonus for LLM reasoning exploration; applies classic RL exploration ideas to language model RL.

### 7.2 T²PO: Uncertainty-Guided Exploration Control for Multi-Turn Agentic RL
- **Authors**: *(multiple, unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv, May 2026
- **arXiv**: https://arxiv.org/abs/2605.02178
- **Abstract**: Uncertainty-guided exploration control for stable multi-turn agentic RL. Addresses the challenge of exploration-exploitation in long-horizon agent interactions.
- **Key innovations**: Uncertainty-guided exploration; stability improvements for multi-turn agentic RL.

### 7.3 AEM: Adaptive Entropy Modulation for Multi-Turn Agentic RL
- **Authors**: *(multiple, unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv, May 2026
- **arXiv**: https://arxiv.org/abs/2605.00425
- **Abstract**: Adaptive entropy modulation technique for multi-turn agentic RL training stability.
- **Key innovations**: Dynamic entropy scheduling for agentic RL.

### 7.4 SkillGraph: Skill-Augmented RL for Agents via Evolving Skill Graphs
- **Authors**: *(multiple, unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv, May 2026
- **arXiv**: https://arxiv.org/abs/2605.12039
- **Abstract**: Evolving skill graph representation for RL agents, enabling compositional skill reuse across game-like environments.
- **Key innovations**: Graph-structured skill representation; compositional skill transfer.

### 7.5 Synergizing Code Coverage and Gameplay Intent: Coverage-Aware Game Playtesting with LLM-Guided RL
- **Authors**: *(multiple, unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv, December 2025
- **arXiv**: https://arxiv.org/abs/2512.12706
- **Abstract**: Combines code coverage metrics with gameplay intent using LLM-guided RL for automated game playtesting.
- **Key innovations**: Coverage-intent synergy for test agent guidance; LLM-guided reward shaping for playtesting.

### 7.6 A Survey on Self-play Methods in Reinforcement Learning
- **Authors**: *(multiple, unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv, 2024 (comprehensive survey)
- **arXiv**: https://arxiv.org/abs/2408.01072
- **Abstract**: Comprehensive survey of self-play methods. Categorizes into: traditional self-play, PSRO series, ongoing-training-based, and regret-minimization-based. Covers board games, card games, video games. Analyzes convergence challenges and computational demands. Discusses integration of self-play with LLMs.
- **Key innovations**: Four-category self-play taxonomy; convergence analysis; LLM integration discussion.

### 7.7 Game-Theoretic Lens on LLM-based Multi-Agent Systems
- **Authors**: *(multiple, unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv, January 2026
- **arXiv**: https://arxiv.org/abs/2601.15047
- **Abstract**: Comprehensive survey of LLM-based multi-agent systems through a game-theoretic lens. Covers cooperative, competitive, and mixed objectives. Provides unifying theoretical foundation for studying social dynamics and strategic behaviors.
- **Key innovations**: Game-theoretic framework for LLM multi-agent systems; bridges game theory with modern LLM agent research.

### 7.8 Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games
- **Authors**: *(multiple, unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv, May 2026
- **arXiv**: https://arxiv.org/abs/2605.04906
- **Abstract**: Extends Group Relative Policy Optimization (GRPO) to multi-agent settings. Self-play framework where agents share the same model for strategic reasoning.
- **Key innovations**: GRPO extension to multi-agent game settings; shared-model self-play.

### 7.9 SID-CC SidConArena: Open-Ended Positive-Sum Bargaining Game Environment
- **Authors**: Yeqi Feng et al.
- **Affiliation**: *(unverified)*
- **Venue**: arXiv, June 2026
- **arXiv**: https://arxiv.org/abs/2606.27397
- **Abstract**: Environment for evaluating agents in open-ended, positive-sum bargaining games. Focuses on negotiation and cooperation rather than competitive zero-sum settings.
- **Key innovations**: Positive-sum bargaining benchmark; open-ended negotiation evaluation.

### 7.10 Enhancing Consistency of Werewolf AI through Dialogue Summarization and Persona Information
- **Authors**: *(multiple, unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv, March 2026
- **arXiv**: https://arxiv.org/abs/2603.07111
- **Abstract**: Improves LLM agent consistency in social deduction games (Werewolf/Mafia) through dialogue summarization and persona modeling.
- **Key innovations**: Persona-aware dialogue memory for social deduction games.

### 7.11 Trust, Lies, and Long Memories: Emergent Social Dynamics in Multi-Round Avalon with LLM Agents
- **Authors**: *(multiple, unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv, April 2026
- **arXiv**: https://arxiv.org/abs/2604.20582
- **Abstract**: Studies emergent social dynamics including deception and reputation in multi-round Avalon (social deduction game) with LLM agents.
- **Key innovations**: Emergent deception and reputation tracking in LLM agent social games.

### 7.12 Deception and Communication in Autonomous Multi-Agent Systems: Among Us Study
- **Authors**: *(multiple, unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: AAMAS 2026
- **arXiv**: https://arxiv.org/abs/2603.26635
- **Abstract**: Experimental study of deception and communication strategies in Among Us with autonomous multi-agent systems.
- **Key innovations**: Deception strategy analysis in social deduction game agents.

### 7.13 MINDGAMES: A Live Arena for Evaluating Social and Strategic Reasoning in Multi-Agent LLMs
- **Authors**: *(multiple, unverified)*
- **Affiliation**: *(unverified)*
- **Venue**: arXiv, May 2026
- **arXiv**: https://arxiv.org/abs/2605.29512
- **Abstract**: Live arena platform for evaluating social and strategic reasoning in multi-agent LLM systems.
- **Key innovations**: Live evaluation arena for multi-agent LLM strategic reasoning.

---

## Cross-cutting Themes

1. **LLM + RL convergence in games**: The dominant 2025–2026 trend is combining LLM reasoning/planning with RL execution/control (Odysseus, Hierarchical Control, SPA, MARL-GPT). Pure game RL (DQN/PPO on Atari) is no longer the frontier.

2. **Foundation models entering gaming**: NitroGen (40K hours, 1000+ games), Towards Generalist Game Players survey, MARL-GPT mark the shift from task-specific to generalist game agents.

3. **Benchmark explosion**: GameCraft-Bench (Godot), GameWorld (browser), OmniGameArena (UE5), Orak (MCP), PokeGym, GBQA, GameDevBench — the field is standardizing evaluation with real game engines, verifiable metrics, and multi-round learning curves.

4. **Social/multi-agent games as testbeds**: Avalon, Among Us, Werewolf, MINDGAMES — LLM agents in social deduction games reveal emergent deception, reputation, and strategic communication capabilities.

5. **PCG meets LLMs**: PCGRLLM uses LLMs for reward design in PCGRL; CHI 2026 study reveals player perception biases against AI-generated content.

6. **Industry (EA) active**: EA publishes vision paper on RL-augmented game AI and hierarchical LLM+RL for multi-agent control, signaling industry adoption beyond research demos.

---

## References Index

| # | Paper | arXiv | Category |
|---|-------|-------|----------|
| 1 | Comprehensive Review of MARL in Video Games | 2509.03682 | Game RL |
| 2 | SPA: Internalizing World Models via Self-Play | 2510.15047 | Game RL / Self-Play |
| 3 | Odysseus: VLMs for 100+ Turn Game RL | 2605.00347 | Game RL / VLM |
| 4 | Hierarchical Control in Multi-Agent Games | 2606.20014 | Game RL / Industry |
| 5 | SPIRAL: Self-Play for Reasoning | openreview | Game RL / Self-Play |
| 6 | Nemobot Games | 2604.21896 | Game AI Bot |
| 7 | Augmenting Game AI with RL (EA) | 2606.20210 | Game AI Bot / Industry |
| 8 | GamingAgent | github/lmgame-org | Game AI Bot |
| 9 | Brain Alignment During Gameplay | 2605.19352 | Game AI Bot |
| 10 | NitroGen | 2601.02427 | Foundation Model |
| 11 | Towards Generalist Game Players | 2605.09965 | Foundation Model |
| 12 | MARL-GPT | 2604.05943 | Foundation Model |
| 13 | Survey on LLM-Based Game Agents | 2404.02039 | Foundation Model / Survey |
| 14 | PCGRLLM | 2502.10906 | PCG |
| 15 | High Dimensional PCG | 2602.18943 | PCG |
| 16 | Playing the Imitation Game | 2602.14254 | PCG / Perception |
| 17 | GameCraft-Bench | 2606.17861 | Benchmark |
| 18 | GameWorld | 2604.07429 | Benchmark |
| 19 | OmniGameArena | 2606.09826 | Benchmark |
| 20 | GameDevBench | 2602.11103 | Benchmark |
| 21 | PokeGym | 2604.08340 | Benchmark |
| 22 | Orak | 2506.03610 | Benchmark |
| 23 | GBQA | *(aimodels.fyi)* | Benchmark |
| 24 | 3M Params vs LLMs for Game Control | 2604.07385 | Industry |
| 25 | CDE: Curiosity-Driven Exploration | openreview | Exploration / RL |
| 26 | T²PO | 2605.02178 | Exploration / Agentic RL |
| 27 | AEM: Adaptive Entropy Modulation | 2605.00425 | Agentic RL |
| 28 | SkillGraph | 2605.12039 | Skill RL |
| 29 | Coverage-Aware Playtesting | 2512.12706 | Playtesting / RL |
| 30 | Survey on Self-play Methods | 2408.01072 | Self-Play / Survey |
| 31 | Game-Theoretic Lens on LLM MAS | 2601.15047 | Game Theory / Survey |
| 32 | Strat-Reasoner | 2605.04906 | Multi-Agent RL |
| 33 | SidConArena | 2606.27397 | Bargaining Game |
| 34 | Werewolf AI Consistency | 2603.07111 | Social Deduction |
| 35 | Trust, Lies, and Long Memories | 2604.20582 | Social Deduction |
| 36 | Deception in Among Us | 2603.26635 | Social Deduction / AAMAS |
| 37 | MINDGAMES Arena | 2605.29512 | Strategic Reasoning |
