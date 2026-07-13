---
title: Game RL & Game AI Bot — Daily Paper Digest (July 13, 2026)
type: synthesis
created: 2026-07-13
updated: 2026-07-13
tags: [game-rl, game-ai, reinforcement-learning, self-play, foundation-models, pcg, benchmarks, world-models, llm-agents, marl, nvidia, deepmind]
---

# Game RL & Game AI Bot — Daily Paper Digest (July 13, 2026)

> Curated papers from arXiv, recent conference proceedings (ICML 2026, ICLR 2026, CVPR 2026, NeurIPS 2025, AAAI 2026, CoG 2026, AIIDE 2024), and industry sources covering Game RL, Game AI Bots, Foundation Models, PCG, Benchmarks, Industry Deployment, and Related Techniques.

---

## 1. Game RL — Reinforcement Learning in Games

### 1.1 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors:** Bo Liu, Leon Guertler, Simon Yu, Zichen Liu, Penghui Qi, Daniel Balcells, Mickel Liu, Cheston Tan, Weiyan Shi, Min Lin, Wee Sun Lee, Natasha Jaques
- **Affiliation:** University of Sydney, NUS
- **Venue:** ICLR 2026
- **Abstract:** Introduces SPIRAL, a self-play framework where models learn by playing multi-turn zero-sum games against continuously improving versions of themselves. Proposes role-conditioned advantage estimation (RAE) to stabilize multi-agent training. Improves performance by up to 10% across 8 reasoning benchmarks on 4 models (Qwen, Llama families). Multi-game training (TicTacToe, Kuhn Poker, Simple Negotiation) yields strongest results. Chain-of-thought analysis reveals games develop distinct cognitive patterns that transfer to reasoning.
- **Key Innovation:** Self-play as automatic curriculum for LLM reasoning without human supervision
- **Link:** https://arxiv.org/abs/2506.24119

### 1.2 Code World Models for General Game Playing
- **Authors:** Wolfgang Lehrach, Daniel Hennes, Miguel Lázaro-Gredilla, Xinghua Lou, Carter Wendelken, Zun Li, Antoine Dedieu, Jordi Grau-Moya, Marc Lanctot, Atil Iscen, John Schultz, Marcus Chiam, Ian Gemp, Piotr Zielinski, Satinder Singh, Kevin P. Murphy
- **Affiliation:** Google DeepMind
- **Venue:** Preprint 2025
- **Abstract:** Uses LLMs to translate natural language rules and game trajectories into executable Python code world models (CWMs). Generated models serve as verifiable simulation engines for MCTS planning. Handles both perfect and imperfect information games. Outperforms or matches Gemini 2.5 Pro in 9 out of 10 games, including 4 novel games created for the paper.
- **Key Innovation:** LLM-synthesized code as verifiable world models for MCTS planning; handles partial observability via LLM-generated autoencoders
- **Link:** https://arxiv.org/abs/2510.04542

### 1.3 Reinforcement Learning in Strategy-Based and Atari Games: A Review of Google DeepMind's Innovations
- **Authors:** Abdelrhman Shaheen, Anas Badr, Ali Abohendy, Hatem Alsaadawy, Nadine Alsayad, Ehab H. El-Shazly
- **Affiliation:** Egypt-Japan University of Science and Technology (E-JUST)
- **Venue:** Preprint 2026
- **Abstract:** Comprehensive review of DeepMind's RL innovations in games — AlphaGo, AlphaGo Zero, MuZero. Covers model-based, model-free, and deep Q-network approaches. Discusses MiniZero and multi-agent extensions, showing future directions for game RL.
- **Key Innovation:** Unified survey of the Alpha* family and their evolution
- **Link:** https://arxiv.org/abs/2502.10303

### 1.4 A Survey on Self-play Methods in Reinforcement Learning
- **Authors:** Ruize Zhang, Zelai Xu, Chengdong Ma, Chao Yu, Wei-Wei Tu, Wenhao Tang, Shiyu Huang, Deheng Ye, Wenbo Ding, Yaodong Yang, Yu Wang
- **Affiliation:** Tsinghua University, Peking University, Tencent, 4Paradigm, Zhipu AI
- **Venue:** Preprint (v4 Oct 2025)
- **Abstract:** Comprehensive survey of self-play algorithms in RL. Covers MARL framework, game theory concepts, unified classification of self-play methods, and their role in different non-cooperative scenarios including Go, poker, and video games. Highlights open challenges and future directions.
- **Key Innovation:** Unified taxonomy for self-play methods bridging algorithms and practical implications
- **Link:** https://arxiv.org/abs/2408.01072

### 1.5 A Survey on Large Language Model Based Game Agents
- **Authors:** Sihao Hu, Tiansheng Huang, Gaowen Liu, Ramana Rao Kompella, Fatih Ilhan, Selim Furkan Tekin, Yichang Xu, Zachary Yahn, Ling Liu
- **Affiliation:** Georgia Institute of Technology, Cisco Research
- **Venue:** Preprint (v2 2024)
- **Abstract:** Comprehensive overview of LLM-based game agents. Introduces conceptual architecture centered on memory, reasoning, and I/O components. Surveys agents across 6 game genres: adventure, communication, competition, cooperation, simulation, and crafting & exploration. Maintains curated paper list at github.com/git-disl/awesome-LLM-game-agent-papers.
- **Key Innovation:** Unified LLM game agent architecture taxonomy across 6 game genres
- **Link:** https://arxiv.org/abs/2404.02039

---

## 2. Game AI Bot — LLM-Powered Game Agents & NPC Intelligence

### 2.1 Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with LLMs
- **Authors:** Chee Wei Tan, Yuchen Wang, Shangxin Guo
- **Affiliation:** National University of Singapore (NUS)
- **Venue:** Preprint Apr 2026
- **Abstract:** Introduces Nemobot, an interactive agentic engineering environment extending Shannon's taxonomy of game-playing machines with LLMs. Evaluated across 4 game classes: dictionary-based (compressed state-action mappings), solvable (mathematical reasoning for optimal strategies), heuristic-based (classical minimax + crowd-sourced data), and learning-based (RL with human feedback + self-critique). Demonstrates gamified AI education capabilities.
- **Key Innovation:** LLM-powered framework spanning Shannon's 4 game taxonomy classes with collaborative prompt engineering
- **Link:** https://arxiv.org/abs/2604.21896

### 2.2 One Policy, Infinite NPCs: Persona-Traceable Shared RL Policies for Scalable Game Agents (PCSP)
- **Authors:** Yoosung Hong et al.
- **Affiliation:** Not specified
- **Venue:** Preprint May 2026
- **Abstract:** Introduces PCSP — a single RL policy conditioned on frozen LLM embeddings of free-form persona descriptions for NPC control. Combines once-per-NPC persona encoding, low-rank persona projection, neural persona conditioning, and PPO + InfoNCE consistency + KL diversity training. Validated on Melting Pot 2.4.0 substrates and deployed in UE5 with 64 concurrent agents at sub-frame inference times.
- **Key Innovation:** Shared RL policy supporting persona-conditioned NPC behavior at scale with real-time inference in commercial game engines
- **Link:** https://arxiv.org/abs/2605.23652

### 2.3 Interactive AI NPCs Powered by LLMs: Technical Report for the CPDC Challenge 2025
- **Authors:** Yitian Huang, Yuxuan Lei, Jianxun Lian, Hao Liao
- **Affiliation:** Shenzhen University, USTC, Microsoft Research Asia
- **Venue:** CPDC 2025 (1st place Team MSRA_SC)
- **Abstract:** Winning solution for the Commonsense Persona-Grounded Dialogue Challenge. Centers on Context Engineering (dynamic tool pruning, persona clipping) and GRPO training replacing SFT to mitigate small-sample overfitting. Ranks 1st in Task 2 API, 2nd in Task 1 API, 3rd in Task 3 API and GPU track.
- **Key Innovation:** GRPO training for NPC dialogue outperforming SFT; context engineering for tool-call stability
- **Link:** https://arxiv.org/abs/2511.20200

### 2.4 AI Level of Detail: Distance-Aware ML Model Precision Selection for Real-Time Human Motion Prediction in Games
- **Authors:** Mathew Varghese
- **Affiliation:** University of Washington
- **Venue:** SIGGRAPH Technical Workshops 2026
- **Abstract:** Proposes AI Level of Detail (AI LOD) — adapting ML inference precision (FP32/FP16/INT8) based on NPC distance from player camera. Mirrors classical geometry LOD but for AI-driven animation. Evaluated on CMU Mocap dataset using convolutional seq2seq model exported to ONNX Runtime variants.
- **Key Innovation:** Distance-aware quantization as LOD strategy for AI-based character animation in game engines
- **Link:** https://arxiv.org/abs/2606.06565

### 2.5 RuleSmith: Multi-Agent LLMs for Automated Game Balancing
- **Authors:** Not specified in detail
- **Affiliation:** Not specified
- **Venue:** Preprint Feb 2026
- **Abstract:** Uses LLM agents as players while a Bayesian optimizer searches the rule space for configurations that balance asymmetric roles in games. Does not train policies with gradient-based RL — instead leverages LLM agents for non-cooperative multi-agent evaluation of game balance.
- **Key Innovation:** LLM-as-player paradigm with Bayesian optimization for automated game balance tuning
- **Link:** https://arxiv.org/abs/2602.06232

---

## 3. Game Foundation Models — Generalist Game-Playing Models

### 3.1 NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors:** Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi "Jim" Fan
- **Affiliation:** NVIDIA, Stanford, Caltech, UChicago, UT Austin
- **Venue:** CVPR 2026
- **Abstract:** Vision-action foundation model trained on 40,000 hours of gameplay videos across 1,000+ games. Three key ingredients: (1) internet-scale video-action dataset with automatic player action extraction, (2) multi-game benchmark for cross-game generalization, (3) unified vision-action model via large-scale behavior cloning. Achieves up to 52% relative improvement in task success rates on unseen games. Fully open-source (dataset, evaluation suite, model weights).
- **Key Innovation:** First open-source foundation model for generalist gaming at internet scale (40K hrs, 1000+ games)
- **Link:** https://arxiv.org/abs/2601.02427

### 3.2 Towards Generalist Game Players: A Comprehensive Survey
- **Authors:** Haisheng Wang, Han Yin, Hongbo Ma, Peize Li, Tianjun Gu, Xiangnan Wu, Xinran Zhang, Yongxuan Li, Zirong Chen, Yiming Li et al.
- **Affiliation:** Tsinghua University (THUSI Lab)
- **Venue:** Preprint May 2026
- **Abstract:** 51-page survey tracing the full lifecycle of generalist game players across four interdependent pillars: Dataset, Model, Harness, and Benchmark. Identifies five fundamental trade-offs and charts a five-level roadmap from single-game mastery to a "creator stage" where agents simultaneously create and evolve within game multiverses. Maintains github.com/THUSI-Lab/Awesome-LFMs-Play-Games.
- **Key Innovation:** Five-level roadmap for generalist game players; end-to-end analysis across Dataset/Model/Harness/Benchmark
- **Link:** https://arxiv.org/abs/2605.09965

### 3.3 CoMaTrack: Competitive Multi-Agent Game-Theoretic Tracking with Vision-Language-Action Models
- **Authors:** Youzhi Liu, Li Gao, Liu Liu, Mingyang Lv, Yang Cai
- **Affiliation:** Not specified
- **Venue:** Preprint Mar 2026
- **Abstract:** Competitive game-theoretic MARL framework for embodied visual tracking. Trains agents in dynamic adversarial settings with competitive subtasks. Introduces CoMaTrack-Bench, the first Habitat-based benchmark for language-conditioned competitive EVT. A 3B VLM trained with the framework surpasses 7B single-agent imitation learning methods on EVT-Bench.
- **Key Innovation:** Game-theoretic adversarial training for VLM embodied agents; 3B beating 7B via competitive multi-agent RL
- **Link:** https://arxiv.org/abs/2603.22846

---

## 4. Procedural Content Generation — RL & LLM for Game Content

### 4.1 PCGRLLM: Large Language Model-Driven Reward Design for Procedural Content Generation RL
- **Authors:** Not specified in detail
- **Affiliation:** NYU Game Innovation Lab, GIST
- **Venue:** IEEE Transactions on Games
- **Abstract:** Uses LLMs to generate reward functions for PCGRL agents. Finds LLM-generated rewards outperform human-crafted rewards in spatial constraint scenarios, while humans excel at multi-objective tuning. Proposes complementary human-LLM workflow: LLMs for coarse spatial reward formulation, humans for fine-tuning.
- **Key Innovation:** LLM as reward function engineer for PCGRL; complementary human-LLM reward design workflow
- **Link:** https://arxiv.org/abs/2502.10906

### 4.2 Procedural Content Generation in Games: A Survey with Insights on Emerging LLM Integration
- **Authors:** Mahdi Farrokhi Maleki, Richard Zhao
- **Affiliation:** University of Calgary
- **Venue:** AIIDE 2024
- **Abstract:** Comprehensive survey of PCG in video games covering search-based, ML-based, and LLM-based methods. Analyzes 207 papers from FDG, CoG, AIIDE, CHI-PLAY, and ACG (2019-2023). Compares methods by content type and publication date. Identifies gaps and future research directions in LLM-integrated PCG.
- **Key Innovation:** First systematic comparison of LLM vs traditional PCG methods with gap analysis
- **Link:** https://arxiv.org/abs/2410.15644

### 4.3 The Procedural Content Generation Benchmark: An Open-source Testbed for Generative Challenges in Games
- **Authors:** Not specified in detail
- **Affiliation:** Not specified
- **Venue:** Preprint 2025
- **Abstract:** Introduces PCG Benchmark — an open-source testbed standardizing PCG problems in games. Offers 12 problems out of the box including generation of game rules, levels, buildings, word games, and patterns. Unified evaluation criteria: quality, diversity, and controllability. Compared against 3 baseline search-based PCG algorithms.
- **Key Innovation:** First standardized benchmark for PCG analogous to ALE for RL
- **Link:** https://arxiv.org/abs/2503.21474

### 4.4 Procedural Game Level Design with Deep Reinforcement Learning
- **Authors:** Not specified in detail
- **Affiliation:** Not specified
- **Venue:** Preprint Oct 2025
- **Abstract:** Co-adaptive PCG framework with two RL agents: a hummingbird agent learning navigation/collection and an island agent trained via PPO to generate diverse flower placements. Island agent learns to adjust layout parameters based on environmental cues and past episode outcomes. Emergent behaviors include altitude-aware navigation and terrain-sensitive movement.
- **Key Innovation:** Co-adaptive RL-based PCG where both level generator and player agent learn simultaneously
- **Link:** https://arxiv.org/abs/2510.15120

---

## 5. Game Benchmarks — Evaluation Suites for Game AI Agents

### 5.1 BALROG: Benchmarking Agentic LLM and VLM Reasoning On Games
- **Authors:** Not specified in detail
- **Affiliation:** Not specified
- **Venue:** ICLR 2025
- **Abstract:** Suite of 6 RL environments testing agentic capabilities of long-context LLMs: long-term planning, spatial reasoning, and navigation. Provides fine-grained metrics and a novel data-informed progression system for NetHack. Finds multimodal LLMs perform much worse with images vs text-only descriptions. Identifies a "knowing-doing gap" where models possess knowledge but cannot employ it.
- **Key Innovation:** Game-based agentic benchmark revealing VLM decision-making failures; NetHack progression system
- **Link:** https://arxiv.org/abs/2411.13543

### 5.2 StarCraft+: Benchmarking Multi-agent Algorithms in Adversary Paradigm (SC2BA)
- **Authors:** Yadong Li, Tong Zhang, Bo Huang, Zhen Cui
- **Affiliation:** Nanjing University of Science and Technology, Zaozhuang University
- **Venue:** Preprint Dec 2025
- **Abstract:** Establishes StarCraft II Battle Arena (SC2BA) — a multi-agent algorithm-vs-algorithm environment for benchmarking MARL in adversary paradigm. Unlike SMAC's fixed built-in AI opponents, SC2BA enables inter-algorithm adversary with fairness, usability, and customizability. Benchmarks classic MARL algorithms in dual-algorithm paired and multi-algorithm mixed adversary modes. Includes adversarial PyMARL (APyMARL) library.
- **Key Innovation:** Algorithm-vs-algorithm adversary benchmark replacing fixed AI opponents in SMAC
- **Link:** https://arxiv.org/abs/2512.16444

### 5.3 TeamCraft: A Benchmark for Multi-Modal Multi-Agent Systems in Minecraft
- **Authors:** Qian Long, Zhi Li, Ran Gong, Ying Nian Wu, Demetri Terzopoulos, Xiaofeng Gao
- **Affiliation:** UCLA, University of Toronto
- **Venue:** Preprint Dec 2024
- **Abstract:** Multi-modal multi-agent benchmark built on Minecraft. Features 55,000 task variants specified by multi-modal prompts, procedurally-generated expert demonstrations for imitation learning, and protocols evaluating model generalization. Results show existing models struggle to generalize to novel goals, scenes, and unseen numbers of agents.
- **Key Innovation:** Largest multi-modal multi-agent Minecraft benchmark with 55K task variants
- **Link:** https://arxiv.org/abs/2412.05255

### 5.4 OpenGuanDan: A Large-Scale Imperfect Information Game Benchmark
- **Authors:** Not specified in detail
- **Affiliation:** Not specified
- **Venue:** Preprint Feb 2026
- **Abstract:** Benchmark for GuanDan, a complex 4-player Chinese card game with two standard decks. Tests RL-based agents (DanZero, SDMC), game-theoretic agents (GS2), and LLM-based agents. Empirically demonstrates that existing GuanDan AI agents fail to achieve superhuman performance. Integrates multiple agent paradigms into a unified evaluation framework.
- **Key Innovation:** First large-scale benchmark for complex imperfect-information card games in Chinese gaming culture
- **Link:** https://arxiv.org/abs/2602.00676

### 5.5 BuilderBench: A Benchmark for Generalist Agents
- **Authors:** Not specified in detail (DeepMind)
- **Affiliation:** Google DeepMind
- **Venue:** Preprint Oct 2025
- **Abstract:** Open-ended block-building benchmark for evaluating generalist agents. Tasks require logical reasoning (commutativity/associativity), geometrical reasoning (overhangs, packing), and intuitive physics (gravity, friction, balancing). Uses MuJoCo+JAX for 10-100× faster training than CPU-based benchmarks. 40+ tasks; PPO agent stacks 2 blocks in 30 minutes on single GPU.
- **Key Innovation:** Hardware-accelerated generalist agent benchmark with physics-intuitive construction tasks
- **Link:** Referenced in BuilderBench paper (ResearchGate 2025)

---

## 6. Industry Game AI — Real-World Deployment & Studio Research

### 6.1 NVIDIA ACE & NVIGI SDK — In-Game Inferencing for Autonomous Game Characters
- **Authors:** NVIDIA Research
- **Affiliation:** NVIDIA
- **Venue:** GDC 2026, Industry
- **Abstract:** NVIDIA ACE (Avatar Cloud Engine) suite brings generative AI to game characters via RTX PC inference. NVIGI SDK enables real-time LLM inference in game engines with structured generation, guardrails, and stateless architecture (20-40K tokens in, ~100 tokens out per call). Supports Qwen3-0.6B to Qwen3.5-8B models. Deployed in PUBG, inZOI, NARAKA: BLADEPOINT, and Black Myth: Wukong. Key pattern: client owns state, inference is stateless.
- **Key Innovation:** Production-grade on-device LLM inference SDK for NPCs with sub-second latency
- **Link:** https://developer.nvidia.com/rtx/in-game-inferencing

### 6.2 Real-Time AI Inference Patterns from the Gaming Industry (INFUSE Engine)
- **Authors:** Jam and Tea Studio
- **Affiliation:** Jam and Tea Studio
- **Venue:** Industry blog Dec 2025
- **Abstract:** Presents INFUSE — an inference engine alongside Unreal Engine for adaptive narrative/behavioral logic. Pattern: Actors (local NPC reasoning) + Directors (global coherence/pacing). Key design: clients own state, every inference call includes entire world state slice (20-40K tokens), expects ~100 tokens out. Automated "theater tests" validate behavior across simulated worlds.
- **Key Innovation:** Actor-Director pattern for narrative AI; stateless inference architecture for deterministic NPC behavior
- **Link:** https://cjlludwig.github.io/blog/real-time-ai-inference-patterns-gaming

### 6.3 Generative AI for Dynamic NPC Behavior and PCG in Games
- **Authors:** Not specified in detail
- **Affiliation:** Multiple (industry survey)
- **Venue:** IJETCSIT 2025
- **Abstract:** Architecture, implementation, and production deployment study of generative AI for NPC behavior and PCG. Covers hybrid AI architectures (GOAP + LLM), neural behavior trees, hierarchical context summarization for long-horizon NPC memory, and real-time inference in commercial engines (UE5, Unity). References NVIDIA, Epic Games, and Inworld AI production systems.
- **Key Innovation:** Comprehensive production deployment analysis of LLM-powered NPCs across game engines
- **Link:** Referenced in IJETCSIT paper

---

## 7. Related Techniques — Self-Play, Exploration, World Models, Imitation Learning, etc.

### 7.1 From Curiosity to Competence: How World Models Interact with the Dynamics of Exploration
- **Authors:** Not specified in detail
- **Affiliation:** Not specified
- **Venue:** Preprint Jul 2025
- **Abstract:** Investigates intrinsic motivation mechanisms in model-based RL agents (tabular and Dreamer). Compares novelty, information gain, and empowerment in exploration. Shows curiosity and competence play complementary roles: novelty can get stuck in local optima, information gain avoids this but is slowed by stochasticity, empowerment prefers deterministic dynamics but can adaptively abandon comfort zones.
- **Key Innovation:** Empirical analysis of curiosity vs competence complementarity in world model-based exploration
- **Link:** https://arxiv.org/abs/2507.08210

### 7.2 CDE: Curiosity-Driven Exploration for Efficient RL in Large Language Models
- **Authors:** Runpeng Dai, Linfeng Song, Haolin Liu, Zhenwen Liang, Dian Yu, Haitao Mi, Zhaopeng Tu, Rui Liu, Tong Zheng, Hongtu Zhu, Dong Yu
- **Affiliation:** Tencent AI Lab, various
- **Venue:** Preprint Sep 2025
- **Abstract:** Leverages the model's own intrinsic curiosity to guide exploration in RLVR. Actor uses perplexity over generated responses; critic uses variance of multi-head value estimates. Both serve as exploration bonuses. Achieves ~+3 point improvement over standard GRPO/PPO on AIME benchmarks. Identifies calibration collapse mechanism within RLVR.
- **Key Innovation:** Curiosity-driven exploration bonus for LLM RL; connects actor perplexity to diversity and critic variance to count-based exploration
- **Link:** https://arxiv.org/abs/2509.09675

### 7.3 Hierarchical Planning with Latent World Models (HWM)
- **Authors:** Not specified (Meta FAIR — Yann LeCun, Nicolas Ballas et al.)
- **Affiliation:** Meta FAIR
- **Venue:** Preprint Apr 2026
- **Abstract:** Architecture for hierarchical model predictive control on visual world models. Learns world models at multiple temporal scales in shared latent space; long-horizon model predictions serve as subgoals for short-horizon model via latent matching. Learns action encoder compressing primitive action chunks into latent macro-actions. Achieves 70% success on real-world Franka pick-and-place from single goal image.
- **Key Innovation:** Multi-scale latent world models with macro-action compression for hierarchical planning
- **Link:** https://arxiv.org/abs/2604.03208

### 7.4 RLVR-World: Training World Models with Reinforcement Learning
- **Authors:** Jialong Wu, Shaofeng Yin, Ningya Feng, Mingsheng Long
- **Affiliation:** Tsinghua University
- **Venue:** Preprint May 2025
- **Abstract:** Framework leveraging RL with verifiable rewards (RLVR) to directly optimize world models for task-specific metrics. Evaluates decoded predictions as verifiable rewards. Demonstrates gains on language and video-based world models across text games, web navigation, and robot manipulation.
- **Key Innovation:** RLVR paradigm applied to world model training; metric-aligned optimization beyond MLE
- **Link:** https://arxiv.org/abs/2505.13934

### 7.5 π-Play: Multi-Agent Self-Play via Privileged Self-Distillation without External Data
- **Authors:** Yaocheng Zhang, Jialun Chai, Xiaohan Wang, Wei Lin, Guojun Yin, Dongbin Zhao
- **Affiliation:** Not specified
- **Venue:** Preprint Apr 2026
- **Abstract:** Multi-agent self-evolution framework combining self-play and self-distillation. Examiner generates tasks with question construction paths (QCPs); teacher uses QCP as privileged context to densely supervise student via self-distillation. Transforms sparse-reward self-play into dense-feedback co-evolution. Surpasses fully supervised search agents and improves evolutionary efficiency 2-3× over conventional self-play.
- **Key Innovation:** Privileged information from self-play QCPs enables dense supervision without human feedback
- **Link:** https://arxiv.org/abs/2604.14054

### 7.6 Matrix-Game: Interactive World Foundation Model
- **Authors:** Not specified in detail
- **Affiliation:** Not specified
- **Venue:** Preprint Jun 2026
- **Abstract:** Interactive world foundation model based on video diffusion for game environments. Outperforms GameNGen and MineWorld in controllability (keyboard/mouse accuracy) and physical consistency while maintaining high visual and temporal quality. Demonstrates generation of interactive game worlds from action sequences.
- **Key Innovation:** Video diffusion-based interactive world model for game environments with high controllability
- **Link:** https://arxiv.org/abs/2506.18701

### 7.7 Self-Improving AI Agents through Self-Play
- **Authors:** Not specified in detail
- **Affiliation:** Not specified
- **Venue:** Preprint Dec 2025
- **Abstract:** Theoretical framework unifying self-improvement across conventional RL agents, RLHF/RLAIF pipelines, and SFT-trained LLM agents via the Generator-Verifier-Updater (GVU) operator. Equips parameter manifold with Fisher information metric and derives Variance Inequality — a spectral condition under which any GVU loop yields positive capability gain. Applies to self-play, self-correction, and tool use.
- **Key Innovation:** Geometric framework unifying self-play RL, RLHF, and SFT self-improvement via Fisher metric on policy manifolds
- **Link:** https://arxiv.org/abs/2512.02731

### 7.8 Synthesizing World Models for Bilevel Planning (TheoryCoder)
- **Authors:** Zergham Ahmed, Joshua B. Tenenbaum, Christopher J. Bates, Samuel J. Gershman
- **Affiliation:** Harvard University
- **Venue:** Preprint Mar 2025
- **Abstract:** TheoryCoder instantiates Theory-Based RL (TBRL) using hierarchical representations and LLM-synthesized Python programs as world models. Agents learn general-purpose abstractions (e.g., "move to") grounded in environments via synthesized low-level transition models. Bilevel planning exploits hierarchical structure for scalable learning and planning in video game environments.
- **Key Innovation:** LLM-synthesized code as hierarchical world models for sample-efficient RL in games
- **Link:** https://arxiv.org/abs/2503.20124

### 7.9 Learning in Mean Field Games: A Survey
- **Authors:** Mathieu Laurière, Sarah Perrin, Julien Pérolat, Sertan Girgin, Paul Muller, Romuald Élie, Matthieu Geist, Olivier Pietquin
- **Affiliation:** Google DeepMind, various
- **Venue:** Preprint (v4 Jul 2024)
- **Abstract:** Comprehensive survey of RL methods for learning equilibria in Mean Field Games (MFGs). Covers static, stationary, and evolutive MFG settings. Bridges classical iterative methods with MDP-based RL approaches for model-free MFG solutions. Demonstrates on benchmark problems with perspectives for scaling to complex environments.
- **Key Innovation:** Unified RL framework for Mean Field Games enabling scalable multi-agent learning
- **Link:** https://arxiv.org/abs/2205.12944

### 7.10 Integrating Reinforcement Learning with Visual Generative Models: Foundations and Advances
- **Authors:** Not specified in detail
- **Affiliation:** Not specified
- **Venue:** Preprint 2025
- **Abstract:** Survey on integrating RL with visual generative models. Covers DQN and Rainbow for Atari, A3C/TRPO/PPO for continuous control, and the shift toward offline RL, model-based methods, and alignment-driven learning. Discusses sample inefficiency, limited generalization (Procgen benchmark), and unrealistic assumptions as key limitations driving Phase II research.
- **Key Innovation:** Survey connecting visual generative models with RL evolution from DQN to alignment-driven learning
- **Link:** https://arxiv.org/abs/2508.10316

---

## Summary Statistics

| Category | Papers Count | Key Venues |
|----------|-------------|------------|
| Game RL | 5 | ICLR 2026, DeepMind, Tsinghua/Peking/Tencent, Georgia Tech |
| Game AI Bot | 5 | NUS, SIGGRAPH 2026, MSR Asia, CPDC 2025 |
| Game Foundation Models | 3 | CVPR 2026 (NVIDIA), Tsinghua survey |
| Procedural Content Generation | 4 | IEEE ToG, AIIDE 2024, CoG |
| Game Benchmarks | 5 | ICLR 2025, NeurIPS 2023, UCLA |
| Industry Game AI | 3 | NVIDIA GDC 2026, Epic/UE5 |
| Related Techniques | 10 | Meta FAIR, Tsinghua, Harvard, DeepMind |
| **Total** | **35** | |

## Cross-Cutting Themes

1. **Foundation Models for Games at Scale:** NitroGen (40K hrs, 1000+ games) and the Generalist Game Player survey establish that game foundation models are entering the "internet pretraining" era, analogous to LLMs.

2. **Self-Play as Reasoning Paradigm:** SPIRAL (ICLR 2026) and the self-play survey demonstrate that zero-sum game self-play develops transferable reasoning capabilities, bridging game RL and LLM reasoning.

3. **LLM-Generated World Models:** Code World Models (DeepMind) and TheoryCoder (Harvard) show LLMs can synthesize executable world models from game rules, enabling MCTS planning without manual environment engineering.

4. **NPC Intelligence Entering Production:** NVIDIA ACE/NVIGI SDK and INFUSE Engine demonstrate real-time LLM-powered NPCs in commercial games (PUBG, inZOI, NARAKA). Stateless inference architecture (20-40K in / ~100 out) is emerging as the standard pattern.

5. **PCG + LLM Convergence:** PCGRLLM shows LLMs excel at spatial reward design while humans excel at multi-objective tuning — pointing toward complementary human-LLM workflows for game content generation.

6. **Game Benchmarks Maturing:** SC2BA (algorithm-vs-algorithm), BALROG (LLM agentic), TeamCraft (multi-modal multi-agent Minecraft), and OpenGuanDan (imperfect information card games) expand the benchmark landscape beyond traditional SMAC/Atari.

7. **World Models + Hierarchical Planning:** HWM (Meta) and RLVR-World (Tsinghua) advance model-based RL with multi-scale latent representations and RL-optimized world model training.
