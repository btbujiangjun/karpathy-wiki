---
title: Game RL & Game AI Bot — Daily Survey (2026-06-16)
type: synthesis
created: 2026-06-16
updated: 2026-06-16
tags: [game-rl, game-ai, survey, self-play, marl, foundation-models, pcg, benchmarks, llm-agents]
sources: []
---

# Game RL & Game AI Bot — Daily Survey (2026-06-16)

> Survey of recent arXiv & proceedings papers on Game RL, Game AI Bots, Foundation Models, PCG, Benchmarks, Industry Game AI, and related techniques. Coverage: Jan 2025 – Jun 2026 submissions. This edition focuses on 2025–2026 papers not covered in the previous survey.

## 1. Game Reinforcement Learning — Self-Play, Multi-Agent & Population-Based Training

### SEMA: Self-Evolving Multi-Agent Framework for Efficient Decision Making in Real-Time Strategy Scenarios
- **Authors**: Li Ma, Hao Peng, Yiming Wang, Hongbin Luo, Jie Liu, Kongjing Gu, Guanlin Wu, Hui Lin, Lei Ren
- **Affiliation**: Beihang University
- **Venue**: arXiv (Mar 2026), submitted to Science China Information Science
- **Abstract**: SEMA is a self-evolving multi-agent framework for RTS games that addresses the LLM speed-quality trade-off. It adaptively calibrates model bias through in-episode assessment and cross-episode analysis, incorporates dynamic observation pruning based on structural entropy, and develops a hybrid knowledge-memory mechanism integrating micro-trajectories, macro-experience, and hierarchical domain knowledge.
- **Innovation**: Combination of structural-entropy-based observation pruning with self-evolving multi-agent coordination; 50% latency reduction on StarCraft II maps while improving win rates.
- **Link**: [arXiv:2603.23875](https://arxiv.org/abs/2603.23875)

### RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback
- **Authors**: Xiaoying Zhang, Zichen Liu, Yipeng Zhang, Xia Hu, Wenqi Shao
- **Affiliation**: —
- **Venue**: arXiv (Mar 2026)
- **Abstract**: Online RL framework for LLM agents that generates dual intrinsic feedback via hindsight self-reflection: (1) intrinsic numerical feedback rewarding incremental subtask progress, and (2) intrinsic language feedback distilling reusable lessons into a memory buffer retrieved via SimUtil-UCB strategy. Surpasses GRPO baselines by +18.3% on ALFWorld, +15.4% on WebShop, +27.1% on Sokoban, +8.9% on MineSweeper.
- **Innovation**: Jointly optimizes exploration (numerical intrinsic reward) and experience reuse (language-based memory) in a single RL loop.
- **Link**: [arXiv:2603.08561](https://arxiv.org/abs/2603.08561)

### SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning
- **Authors**: Peng Xia, Jianwen Chen, Hanyang Wang, Jiaqi Liu, Kaide Zeng, Yu Wang, Siwei Han, Yiyang Zhou, Xujiang Zhao, Haifeng Chen, Zeyu Zheng, Cihang Xie, Huaxiu Yao
- **Affiliation**: —
- **Venue**: ICLR 2026 Workshop RSI
- **Abstract**: SkillRL bridges raw experience and policy improvement through automatic skill discovery and recursive evolution. Builds a hierarchical SkillBank via experience-based distillation, uses adaptive retrieval for general and task-specific heuristics, and introduces a recursive evolution mechanism where skill library co-evolves with policy during RL. Achieves SOTA on ALFWorld and WebShop with over 14% improvement and 10–20× token compression.
- **Innovation**: Hierarchical skill library that co-evolves recursively with the RL policy; teacher model distills failures into reusable skills.
- **Link**: [arXiv:2602.08234](https://arxiv.org/abs/2602.08234)

### Internalizing World Models via Self-Play Finetuning for Agentic RL
- **Authors**: Shiqi Chen, et al.
- **Affiliation**: —
- **Venue**: ICLR 2026
- **Abstract**: Proposes SPA (Self-Play Agent), a framework that cold-starts policy via self-play supervised finetuning to learn world models by interacting with environments, then uses them to simulate future states before policy optimization. Boosts Sokoban success rate from 25.6% to 59.8% and FrozenLake from 22.1% to 70.9% for Qwen2.5-1.5B-Instruct.
- **Innovation**: Decomposes world model into state representation + transition modeling; self-play as world model acquisition for downstream RL.
- **Link**: [arXiv:2510.15047](https://arxiv.org/abs/2510.15047)

### GROW: Aligning GRPO with State-Action Modeling for Open-World VLM Agents
- **Authors**: Xiongbin Wu, et al.
- **Affiliation**: —
- **Venue**: arXiv (May 2026)
- **Abstract**: Adapts Group Relative Policy Optimization (GRPO) to VLM agents by decomposing long trajectories into fine-grained state-action samples rather than treating complete rollouts as single training units. Provides surrogate analysis showing the objective preserves core relative policy optimization signal under simplifying assumptions. Achieves SOTA on 800+ Minecraft tasks.
- **Innovation**: State-action-level GRPO for VLM agents; solves long-context noise issue in open-world RL.
- **Link**: [arXiv:2605.20246](https://arxiv.org/abs/2605.20246)

### Offline Fictitious Self-Play for Competitive Games
- **Authors**: Jingxiao Chen, Weiji Xie, Weinan Zhang, Yong Yu, Ying Wen
- **Affiliation**: —
- **Venue**: ICLR 2026 (spotlight)
- **Abstract**: First practical model-free offline RL algorithm for competitive games (Off-FSP). Simulates opponent interactions by adjusting dataset weights with importance sampling, then employs offline self-play to approximate Nash equilibrium. Validated on matrix games, poker, board games, and a real-world human-robot competitive task.
- **Innovation**: Offline self-play without environment interaction; importance sampling for opponent modeling from static datasets.
- **Link**: [arXiv:2403.00841](https://arxiv.org/abs/2403.00841)

## 2. Game AI Bots — LLM-Powered Agents & NPC Intelligence

### Gated Coordination for Efficient Multi-Agent Collaboration in Minecraft Game
- **Authors**: Huadong Jian, et al.
- **Affiliation**: —
- **Venue**: arXiv (Apr 2026)
- **Abstract**: Proposes a partitioned information architecture for MLLM agents that explicitly separates private execution states from public coordination states. Introduces gated coordination with multi-tiered escalation to reduce unnecessary communication. Evaluated on MindCraft and VillagerBench/VillagerAgent platforms across 200+ episodes with 2-3 agent tasks.
- **Innovation**: Partitioned info architecture distinguishing private vs. public agent state; gated escalation prevents coordination noise from local anomalies.
- **Link**: [arXiv:2604.18975](https://arxiv.org/abs/2604.18975)

### Ratchet: A Minimal Hygiene Recipe for Self-Evolving LLM Agents
- **Authors**: Xing Zhang, Yanwei Cui, Guanghui Wang, Ziyuan Li, Wei Qiu, Bing Zhu, Peiyang He
- **Affiliation**: —
- **Venue**: arXiv (May 2026)
- **Abstract**: Ratchet is a single-agent loop where a frozen LLM writes, retrieves, curates, and retires its own natural-language skills. Integrates four candidate hygiene mechanisms: outcome-driven retirement, bounded active-cap, meta-skill authoring guidance, and pattern canonicalisation. On MBPP+ hard-100 with Claude Opus 4.7, lifts pass@1 from 0.258 to 0.584 rolling mean (+0.328pp). Transfers to SWE-bench Verified with +0.22 peak lift.
- **Innovation**: Identifies that the bottleneck in self-evolving agents is lifecycle management, not skill authoring; minimal hygiene recipe closes the gap between LLM-authored and human-curated skills.
- **Link**: [arXiv:2605.22148](https://arxiv.org/abs/2605.22148)

### Experience Transfer for Multimodal LLM Agents in Minecraft Game
- **Authors**: Chenghao Li, Jun Liu, Songbo Zhang, Huadong Jian, Hao Ni, Lik-Hang Lee, Sung-Ho Bae, Guoqing Wang, Yang Yang, Chaoning Zhang
- **Affiliation**: UESTC, KAIST, Hong Kong PolyU, Kyung Hee University
- **Venue**: arXiv (Apr 2026)
- **Abstract**: Proposes Echo, a transfer-oriented memory framework that decomposes reusable knowledge into five dimensions (structure, attribute, process, function, interaction). Uses In-Context Analogy Learning (ICAL) to retrieve and adapt relevant experiences. Achieves 1.3×–1.7× speed-up on object-unlocking tasks in Minecraft with from-scratch learning.
- **Innovation**: Five-dimension knowledge decomposition for explicit transfer; burst-like chain-unlocking phenomenon from accumulated experience.
- **Link**: [arXiv:2604.05533](https://arxiv.org/abs/2604.05533)

## 3. Game Foundation Models — Generalist Game Agents

### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi "Jim" Fan
- **Affiliation**: NVIDIA, Stanford, Caltech, UChicago, UT Austin
- **Venue**: CVPR 2026
- **Abstract**: Vision-action foundation model trained on 40,000 hours of gameplay videos across 1,000+ games. Three key ingredients: (1) internet-scale video-action dataset from publicly available gameplay, (2) multi-game benchmark environment, (3) unified vision-action model with large-scale behavior cloning. Exhibits competence across 3D action, 2D platformer, and procedurally generated worlds. Fine-tuning achieves up to 52% relative improvement on unseen games.
- **Innovation**: First open-source generalist gaming agent at scale; automatic action extraction from streamer overlay videos; dataset/benchmark/model open release.
- **Link**: [arXiv:2601.02427](https://arxiv.org/abs/2601.02427)

### Towards Generalist Game Players: An Investigation of Foundation Models in the Game Multiverse
- **Authors**: Kuan Zhang, et al. (15 authors)
- **Affiliation**: THUSI Lab
- **Venue**: arXiv (May 2026)
- **Abstract**: Comprehensive 51-page survey tracing the full lifecycle of generalist game players across four pillars: Dataset, Model, Harness, and Benchmark. Identifies five fundamental trade-offs bounding the system. Charts a five-level roadmap from single-game mastery to the ultimate creator stage where the agent simultaneously creates and evolves within a theoretical game multiverse.
- **Innovation**: Unified lens on generalist game AI across four pillars with a 5-level maturity roadmap; identifies core trade-offs (generality vs. specialization, etc.).
- **Link**: [arXiv:2605.09965](https://arxiv.org/abs/2605.09965)

## 4. Procedural Content Generation — RL & LLM for Game Content

### PCGRLLM: Large Language Model-Driven Reward Design for Procedural Content Generation Reinforcement Learning
- **Authors**: —
- **Affiliation**: NYU Game Innovation Lab
- **Venue**: arXiv (Feb 2025)
- **Abstract**: PCGRLLM system uses LLMs to design reward functions for PCG RL, converting story descriptions into functional reward systems. Achieves 415% performance increase with one LLM type and 40% with another in 2D environments.
- **Innovation**: LLM-as-reward-designer for PCGRL; reduces need for human reward engineering in content generation.
- **Link**: [arXiv:2502.10906](https://arxiv.org/abs/2502.10906)

### PCGRL+: Scaling, Control and Generalization in Reinforcement Learning Level Generators
- **Authors**: —
- **Affiliation**: NYU Game Innovation Lab
- **Venue**: arXiv (2024)
- **Abstract**: Advances PCGRL with scaling techniques, controllable generation, and improved generalization for level generation across multiple game domains.
- **Innovation**: Scaling laws and control mechanisms for RL-based level generators.
- **Link**: [arXiv:2408.12525](https://arxiv.org/abs/2408.12525)

### Agentic PCG: Procedural Content Generation via Tool-using LLMs
- **Authors**: Zehua Jiang, Sam Earle, Ahmed Khalifa, Julian Togelius
- **Affiliation**: NYU Game Innovation Lab, University of Malta
- **Venue**: SSRN (2026)
- **Abstract**: Tool-using LLM framework for PCG where an agent iteratively edits, evaluates, and optimizes game levels with environment feedback. Supports both static design and dynamic gameplay evaluation, primitive edits and classic PCG algorithms as tools. Works across Binary Maze, Lode Runner, Zelda, Sokoban, and Super Mario Bros.
- **Innovation**: LLM agent with tool-use loop for level generation; combines LLM reasoning with structured environment feedback.
- **Link**: [SSRN](https://ssrn.com/abstract=6499021)

### The Procedural Content Generation Benchmark: An Open-source Testbed for Generative Challenges in Games
- **Authors**: Ahmed Khalifa, Roberto Gallotta, Matthew Barthet, Antonios Liapis, Julian Togelius, Georgios N. Yannakakis
- **Affiliation**: University of Malta, NYU, University of Malta
- **Venue**: FDG 2025
- **Abstract**: Introduces 12 game-related problems with multiple variants for evaluating generative algorithms. Includes level creation, rule set generation, and simple arcade games. Each problem has its own content representation, control parameters, and metrics for quality, diversity, and controllability. Baseline results from random, evolution strategy, and genetic algorithm.
- **Innovation**: Standardized benchmark for PCG algorithms with multi-dimensional evaluation (quality, diversity, controllability).
- **Link**: [arXiv:2503.21474](https://arxiv.org/abs/2503.21474)

### CrawLLM: An LLM-Based Pipeline for Game Asset Generation
- **Authors**: Marvin Zammit, Antonios Liapis, Georgios N. Yannakakis
- **Affiliation**: University of Malta
- **Venue**: IEEE Transactions on Games, 2026 (Early Access)
- **Abstract**: LLM-driven pipeline generating narrative, visual, and gameplay content coherently. Uses Mixtral 8x7B for theme generation, Stable Diffusion XL with ControlNet for visuals. User study shows semantic themes remain discernible across generated game assets.
- **Innovation**: End-to-end LLM+diffusion pipeline for multiplayer game asset generation with theme coherence.
- **Link**: [IEEE ToG](https://antoniosliapis.com/papers/crawllm_an_llm-based_pipeline_for_game_asset_generation.pdf)

## 5. Game Benchmarks — Evaluation Suites & Agent Benchmarks

### ProxyWar: Dynamic Assessment of LLM Code Generation in Game Arenas
- **Authors**: Wenjun Peng, Xinyu Wang, Qi Wu
- **Affiliation**: —
- **Venue**: ICSE 2026
- **Abstract**: Framework that assesses LLM code generation quality by embedding LLM-generated agents in competitive game environments. Combines automated testing, iterative code repair, and multi-agent tournaments. Uncovers discrepancies between benchmark scores and actual dynamic performance across multiple state-of-the-art coders and games.
- **Innovation**: Game-based competitive evaluation for code generation; multi-agent tournament format reveals operational characteristics beyond functional correctness.
- **Link**: [arXiv:2602.04296](https://arxiv.org/abs/2602.04296)

### GameArena: Evaluating LLM Reasoning through Live Computer Games
- **Authors**: Lanxiang Hu, Qiyu Li, Anze Xie, Nan Jiang, Ion Stoica, Haojian Jin, Hao Zhang
- **Affiliation**: UC Berkeley, UC San Diego
- **Venue**: ICLR 2025 (Poster)
- **Abstract**: Dynamic benchmark for evaluating LLM reasoning via interactive gameplay with humans. Three games testing deductive and inductive reasoning. Collects 2000+ game sessions with fine-grained step-by-step reasoning traces for five SOTA LLMs. 100-participant study shows improved user engagement over Chatbot Arena.
- **Innovation**: First benchmark enabling step-by-step LLM reasoning data collection in the wild via gameplay; dynamic, contamination-resistant evaluation.
- **Link**: [OpenReview](https://openreview.net/forum?id=SeQ8l8xo1r)

### MineNPC-Task: Task Suite for Memory-Aware Minecraft Agents
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv (Jan 2026)
- **Abstract**: Task suite designed for evaluating memory-aware agents in Minecraft, with tasks requiring agents to leverage episodic memory for long-horizon planning and adaptation.
- **Innovation**: Standardized evaluation for memory-augmented game agents.
- **Link**: [arXiv:2601.05215](https://arxiv.org/abs/2601.05215)

### Reasoning Capabilities of LLMs in Dynamic Games of Imperfect Information: A Case Study on Dou Dizhu
- **Authors**: Rui He
- **Affiliation**: —
- **Venue**: ICLR 2026
- **Abstract**: Investigates LLM reasoning in the card game Dou Dizhu (imperfect-information game). Establishes a duplicate round-robin tournament benchmark, proposes a data construction framework with globally optimal decision alignment and real-time in-game feedback augmentation. Fine-tuned small LLM shows significantly reduced decision error rate.
- **Innovation**: Rigorous evaluation protocol for imperfect-information games; data construction bridging the information gap for LLM training.
- **Link**: [OpenReview](https://openreview.net/forum?id=lAd8vjQhQG)

## 6. Industry Game AI — Game Engines & Deployment

### GameNGen: Diffusion Models Are Real-Time Game Engines
- **Authors**: Dani Valevski, Yaniv Leviathan, Moab Arar, Shlomi Fruchter
- **Affiliation**: Google
- **Venue**: ICLR 2025 (Poster)
- **Abstract**: First game engine powered entirely by a neural model enabling real-time interaction. Trained on DOOM: uses RL agent to record gameplay, then trains a diffusion model for next-frame prediction conditioned on past frames/actions. Runs at 20 FPS on a single TPU with PSNR 29.4. Human raters slightly above chance at distinguishing simulation from real game clips after 5 minutes.
- **Innovation**: Neural game engine replacing traditional game loops; demonstrates diffusion models can sustain stable long-horizon interactive simulation.
- **Link**: [OpenReview](https://openreview.net/forum?id=P8pqeEkn1H)

### Game Generation via Large Language Models
- **Authors**: Chengpeng Hu, Yunlong Zhao, Jialin Liu
- **Affiliation**: —
- **Venue**: IEEE Conference on Games 2024
- **Abstract**: LLM-based framework to generate game rules and levels simultaneously using video game description language (VGDL). Demonstrates how different prompt contexts affect game generation quality.
- **Innovation**: Simultaneous rule + level generation via LLMs; extends PCG from level generation to full game generation.
- **Link**: [arXiv:2404.08706](https://arxiv.org/abs/2404.08706)

### Genie 2: A Large-Scale Foundation World Model
- **Authors**: Google DeepMind
- **Affiliation**: Google DeepMind
- **Venue**: Blog/Technical Report (Dec 2024)
- **Abstract**: Foundation world model capable of generating an endless variety of action-controllable, playable 3D environments from a single prompt image. Can be played by humans or AI agents using keyboard and mouse inputs.
- **Innovation**: Large-scale generative world model for 3D environments; opens new paradigm for training embodied agents in infinite procedurally generated worlds.
- **Link**: [DeepMind Blog](https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/)

## 7. Related Techniques — World Models, Game Theory, Multi-Agent Systems

### Multi-Agent Strategic Games with LLMs
- **Authors**: Maxim Chupilkin
- **Affiliation**: —
- **Venue**: arXiv (May 2026)
- **Abstract**: Introduces LLMs as experimental subjects in a repeated security dilemma game. Tests multipolarity, finite time horizons, and communication. Results show systematic patterns: multipolarity increases conflict, finite horizons induce backward-induction unraveling, communication reduces conflict via signaling and reciprocity. Provides access to agents' private reasoning and public messages.
- **Innovation**: LLMs as scalable, transparent subjects for studying strategic foundations of conflict and cooperation; bridges game theory and LLM research.
- **Link**: [arXiv:2605.03604](https://arxiv.org/abs/2605.03604)

### Game-Theoretic Lens on LLM-based Multi-Agent Systems
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv (Jan 2026)
- **Abstract**: Survey adopting a game-theoretic framework to categorize LLM-based MAS through four core elements: players, strategies, payoffs, and information. Provides systematic review, identifies research gaps in equilibrium coordination, incentive-compatible communication, and information structure modeling under partial observability.
- **Innovation**: Unified game-theoretic perspective on LLM multi-agent systems connecting classical game theory with modern LLM research.
- **Link**: [arXiv:2601.15047](https://arxiv.org/abs/2601.15047)

### Multi-Agent Collaboration via Evolving Orchestration
- **Authors**: —
- **Affiliation**: Tsinghua / OpenBMB
- **Venue**: NeurIPS 2025 (Poster)
- **Abstract**: Puppeteer-style paradigm for LLM-based MAS where a centralized orchestrator trained via RL dynamically sequences and prioritizes agents. Achieves superior performance with reduced computational costs. Analysis reveals compact, cyclic reasoning structures emerge under evolving orchestration.
- **Innovation**: RL-trained orchestrator for dynamic agent collaboration; emergent cyclic reasoning patterns.
- **Link**: [OpenReview](https://openreview.net/forum?id=L0xZPXT3le)

### What Do World Models Learn in RL? Probing Latent Representations
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv (Mar 2026)
- **Abstract**: Probing study investigating what world models learn in RL settings. Finds that learned world models develop structured, approximately linear internal representations of environment state across two games and two architectures.
- **Innovation**: First interpretability-focused analysis of world model latent representations in game RL.
- **Link**: [arXiv:2603.21546](https://arxiv.org/abs/2603.21546)

### A Comprehensive Review of Multi-Agent Reinforcement Learning in Video Game AI
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv (2025)
- **Abstract**: Survey of MARL in video game AI systems. Proposes a novel method to estimate game complexity and suggests future research directions.
- **Innovation**: Game complexity estimation metric; comprehensive overview of MARL game applications.
- **Link**: [arXiv:2509.03682](https://arxiv.org/abs/2509.03682)

### Reinforcement Learning in Strategy-Based and Atari Games: A Review of Google DeepMind's Innovations
- **Authors**: Abdelrhman Shaheen, et al.
- **Affiliation**: —
- **Venue**: arXiv (Feb 2025, updated Feb 2026)
- **Abstract**: Reviews RL applications in Atari and strategy games, analyzing AlphaGo, AlphaGo Zero, MuZero, MiniZero, and multi-agent models. Discusses key innovations, training processes, challenges, and future directions.
- **Innovation**: Comprehensive review of DeepMind's game RL lineage from AlphaGo to multi-agent systems.
- **Link**: [arXiv:2502.10303](https://arxiv.org/abs/2502.10303)

## Key Themes & Trends

1. **Self-play for LLM reasoning**: Multiple papers (SPIRAL, MARSHAL, GROW, RetroAgent) use game-based self-play RL to improve LLM reasoning — a rapidly growing intersection of game RL and LLM training.
2. **Generalist game agents**: NitroGen and the Generalist Game Players survey represent a shift from single-game superhuman agents to broad multi-game foundation models.
3. **LLM-driven PCG**: PCGRLLM, Agentic PCG, and CrawLLM show LLMs acting as reward designers, level editors, and full asset generation pipelines.
4. **Game-based evaluation**: ProxyWar and GameArena use games as dynamic, contamination-resistant benchmarks for LLM capabilities.
5. **Self-evolving agents**: Ratchet, RetroAgent, and SkillRL explore how frozen LLMs can autonomously build skill libraries — a key direction for agentic AI.
6. **Neural game engines**: GameNGen and Genie 2 point toward a future where game engines are entirely neural.
7. **Game-theoretic LLM analysis**: Increasing use of formal game theory (security dilemmas, Nash equilibria, imperfect-information games) to understand and improve LLM agent behavior.
