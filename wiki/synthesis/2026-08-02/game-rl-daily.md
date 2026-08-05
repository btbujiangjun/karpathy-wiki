---
title: "Game RL & Game AI Bot — Daily Synthesis (2026-08-02)"
type: synthesis
created: 2026-08-02
updated: 2026-08-02
tags: [game-rl, game-ai, game-foundation-models, pcg, game-benchmarks, self-play, world-models, multi-agent-rl, llm-agents, industry-game-ai]
sources: []
---

# Game RL & Game AI Bot — Daily Synthesis (2026-08-02)

> Curated papers on Game RL, Game AI Bots, Game Foundation Models, PCG, Benchmarks, Industry Game AI, and related techniques. Verified against the arXiv API (submitted Apr–Jul 2026, fresh window Jul 2026). Complements the 2026-08-01 digest (no overlap).

---

## 1. Game RL — Reinforcement Learning in Games

### Superhuman AI for Generals.io Using Self-Play Reinforcement Learning
- **Authors**: Matej Straka, Viliam Lisý, Martin Schmid
- **Affiliation**: Charles University / Google DeepMind
- **Venue**: arXiv:2606.23348 (Jun 2026)
- **Key Innovation**: Self-play agent for Generals.io (real-time strategy with long-horizon planning + imperfect information) reaches **#1 on the public 1v1 leaderboard of 5,000+ humans**, beating the two top-ranked players 199–70 in 269 ladder matches. Trained 4 days on 4× NVIDIA H200; a JAX-native simulator runs tens of millions of frames/second on a single GPU.
- **Link**: https://arxiv.org/abs/2606.23348

### CAST: Game Solvers as Turn-Level Teachers for LLM Agents
- **Authors**: Yu Wang, Yi-Kai Zhang, Wentao Shi, Ziang Ye, Yuchun Miao, Yueqing Sun, Qi Gu, Xunliang Cai, Lan-Zhe Guo, Han-Jia Ye, Fuli Feng
- **Affiliation**: USTC / Meituan
- **Venue**: arXiv:2607.25308 (Jul 2026)
- **Key Innovation**: Credit Assignment from Solver Teachers — uses the change in a game solver's state value as a dense turn-level reward for RLVR-style training of LLM agents in long-horizon games, addressing the sparse final-reward credit assignment problem that standard RLVR suffers from.
- **Link**: https://arxiv.org/abs/2607.25308

### WallZero: Mastering the Game of WallGo with Strategic Analysis
- **Authors**: Hsing-Yu Chen, Jérôme Arjonilla, I-Chen Wu, Ti-Rong Wu
- **Affiliation**: National Yang Ming Chiao Tung University
- **Venue**: arXiv:2606.17847 (Jun 2026)
- **Key Innovation**: AlphaZero-style engine for WallGo (a territory-invasion game related to Go) with a focus on strategic analysis of openings/endgames, extending the MCTS+neural self-play recipe to a new combinatorial game.
- **Link**: https://arxiv.org/abs/2606.17847

### AlphaZero in Sparsely Rewarded Games: Limits and Auxiliary Supervision
- **Authors**: Brent Kong, Tejas Ram, Tony Yue Yu
- **Affiliation**: —
- **Venue**: arXiv:2607.08984 (Jul 2026)
- **Key Innovation**: Probes the gap between "superhuman" and "perfect" play in AlphaZero using oracle-evaluable domains: Connect Four (solved partisan) and Chomp (Grundy-number structure). Proposes AlphaZero Auxiliary Loss (AZAL) that adds oracle-derived policy supervision, and quantifies where vanilla self-play+MCTS saturates.
- **Link**: https://arxiv.org/abs/2607.08984

### Self-Play Reinforcement Learning under Imperfect Information in Big 2
- **Authors**: Aalok Patwa
- **Affiliation**: —
- **Venue**: arXiv:2605.28863 (May 2026)
- **Key Innovation**: Studies self-play RL for Big 2 (a popular imperfect-information shedding card game with hidden hands and complex legal-action structure), benchmarking policy-gradient self-play in a game more combinatorial than poker micro-variants.
- **Link**: https://arxiv.org/abs/2605.28863

### Real-Time Parallel Counterfactual Regret Minimization
- **Authors**: Boning Li, Longbo Huang
- **Affiliation**: Tsinghua University
- **Venue**: arXiv:2605.19928 (May 2026)
- **Key Innovation**: First parallelization framework for real-time depth-limited CFR (the algorithmic family behind Libratus/Pluribus). Seamlessly integrates pruning and other accelerations to run near-equilibrium solving within strict per-decision seconds-level time budgets.
- **Link**: https://arxiv.org/abs/2605.19928

### AlphaExploitem: Going Beyond the Nash Equilibrium in Poker by Learning to Exploit Suboptimal Play
- **Authors**: Vlad Murgoci, Matthijs Spaan, Yaniv Oren
- **Affiliation**: TU Delft
- **Venue**: arXiv:2605.09150 (May 2026)
- **Key Innovation**: Extends the competitive-RL agent AlphaHoldem with a hierarchical transformer encoder that reasons over previously played hands, and trains against a diverse pool of exploitable opponents to deliberately deviate from Nash play and maximize utility against suboptimal humans.
- **Link**: https://arxiv.org/abs/2605.09150

### World Models for Policy Refinement in StarCraft II (StarWM)
- **Authors**: Yixin Zhang, Ziyi Wang, Yiming Rong, Haoxi Wang, Jinling Jiang, Shuang Xu, Haoran Wu, Shiyu Zhou, Bo Xu
- **Affiliation**: CAS Institute of Automation
- **Venue**: arXiv:2602.14857 (Feb 2026)
- **Key Innovation**: First action-conditioned world model for StarCraft II that predicts future observations under partial observability and integrates into the LLM-based decision loop for policy refinement — bridging the gap between model-free LLM agents and model-based planning in massive RTS state spaces.
- **Link**: https://arxiv.org/abs/2602.14857

### Endpoint Replay: Compressing the Recency Buffer in Deep Reinforcement Learning
- **Authors**: Parham Mohammad Panahi, Armin Ashrafi, Haoyu Du, Andrew Patterson, Martha White, Adam White
- **Affiliation**: University of Alberta
- **Venue**: arXiv:2607.25123 (Jul 2026)
- **Key Innovation**: Atari/control-oriented replay-buffer method that compresses the recency buffer by storing trajectory endpoints, cutting memory while preserving near-on-policy learning — a systems-level efficiency win for deep RL training.
- **Link**: https://arxiv.org/abs/2607.25123

---

## 2. Game AI Bot — LLM-Powered Game Agents & NPC Intelligence

### Environment-Grounded Automated Prompt Optimization for LLM Game Agents
- **Authors**: Rean Clive Fernandes, Lukas Fehring, Theresa Eimer, Marius Lindauer, Matthias Feurer
- **Affiliation**: Leibniz University Hannover
- **Venue**: arXiv:2606.17838 (Jun 2026)
- **Key Innovation**: Decomposes the observation-to-action pipeline into a goal-conditioned descriptor agent + action selection agent, and auto-optimizes each module's prompt via an LLM-driven evolutionary loop grounded in environment returns, with a behavior analyzer attributing episode outcomes to specific prompt components.
- **Link**: https://arxiv.org/abs/2606.17838

### The Latent Bridge: A Continuous Slow-Fast Channel for Real-Time Game Agents
- **Authors**: Bojie Li, Noah Shi
- **Affiliation**: —
- **Venue**: arXiv:2606.24470 (Jun 2026)
- **Key Innovation**: Pairs a 9B reactive VLM (millisecond actions) with an 8B reasoning VLM (~1.5s deliberation) and trains only the communication channel between them, hitting 15 Hz control loops while retaining planning-level quality — a concrete recipe for the real-time game-agent latency/quality tradeoff.
- **Link**: https://arxiv.org/abs/2606.24470

### SPIKE: An Adaptive Dual Controller Framework for Cost-Efficient Long-Horizon Game Agents
- **Authors**: Wencan Jiang, Jiangning Zhang, Jianbiao Mei, Jinzhuo Liu, Yu Yang, Xiaobin Hu, Zhucun Xue, Yong Liu, Dacheng Tao
- **Affiliation**: —
- **Venue**: arXiv:2605.18636 (May 2026)
- **Key Innovation**: Reuses strategic reasoning across locally stable trajectory segments and re-invokes it at event boundaries — a low-frequency Strategic Controller + reactive low-level executor that cuts token/latency cost for long-horizon open-world game control without drifting.
- **Link**: https://arxiv.org/abs/2605.18636

### How Clued Up are LLMs? Evaluating Multi-Step Deductive Reasoning in a Text-Based Game Environment
- **Authors**: Rebecca Ansell, Autumn Toney-Wails
- **Affiliation**: —
- **Venue**: arXiv:2603.17169 (Mar 2026)
- **Key Innovation**: Rule-based text-adventure Clue testbed with 6 LLM agents (GPT-4o-mini, Gemini-2.5-Flash): across 18 games agents win only 4 times, and fine-tuning on structured logic puzzles does NOT transfer to sustained in-game deductive reasoning — a sobering result on LLM long-horizon inference.
- **Link**: https://arxiv.org/abs/2603.17169

### CA2: Code-Aware Agent for Automated Game Testing
- **Authors**: Valliappan Chidambaram Adaikkappan, Vincent Martineau, Joshua Romoff, David Meger
- **Affiliation**: McGill / Ubisoft
- **Venue**: arXiv:2605.13918 (May 2026)
- **Key Innovation**: Game-testing LLM agent that reasons about game code (not just observations) to target untested branches and generate more relevant test actions — code-aware exploration for automated playtesting.
- **Link**: https://arxiv.org/abs/2605.13918

### MIMIC-Py: An Extensible Tool for Personality-Driven Automated Game Testing with LLMs
- **Authors**: Yifei Chen, Sarra Habchi, Lili Wei
- **Affiliation**: Concordia University
- **Venue**: arXiv:2604.07752 (Apr 2026)
- **Key Innovation**: Turns personality-driven LLM playtesting agents into a reusable Python framework with personality traits as configurable inputs and a modular architecture decoupling agent behavior from game-specific logic — cross-game, extensible automated QA.
- **Link**: https://arxiv.org/abs/2604.07752

### Fixed-Persona SLMs with Modular Memory: Scalable NPC Dialogue on Consumer Hardware
- **Authors**: Martin Braas, Lukas Esterle
- **Affiliation**: —
- **Venue**: arXiv:2511.10277 (Nov 2025)
- **Key Innovation**: Small language models with fixed personas + modular (external) memory for NPC dialogue, designed to run on consumer hardware — a practical path to shipping LLM-driven NPCs without cloud inference.
- **Link**: https://arxiv.org/abs/2511.10277

---

## 3. Game Foundation Models — Generalist Game Agents & World Models

### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi "Jim" Fan
- **Affiliation**: NVIDIA / UIUC
- **Venue**: arXiv:2601.02427 (Jan 2026)
- **Key Innovation**: Vision-action foundation model for generalist game agents trained on **40,000 hours of gameplay video across 1,000+ games**, using automatically-extracted player actions, a multi-game benchmark for cross-game generalization, and large-scale behavior cloning — competence across 3D action combat, platformers, and more.
- **Link**: https://arxiv.org/abs/2601.02427

### Multiplayer Interactive World Models with Representation Autoencoders
- **Authors**: Anthony Hu, Václav Volhejn, Adrien Ramanana Rahary, Chris Mulder, Aditya Makkar, Alyx Liao, Amélie Royer, Manu Orsini, Adam Jelley, Eloi Alonso, Florian Laurent, Fredrik Norén, James Swingos, Jan Hünermann, Kent Rollins, Lucas Hosseini, Matthieu Le Cauchois, Maxim Peter, Pim de Witte, Tim Brown, Vincent Micheli, Moritz Böhle, Gabriel de Marmiesse, Viktoriia Sharmanska, Lucia Specia, Michael Black, Patrick Pérez
- **Affiliation**: Google DeepMind
- **Venue**: arXiv:2607.05352 (Jul 2026)
- **Key Innovation**: First **multiplayer** world model, studied in Rocket League: conditions on the action streams of multiple agents, learns to attribute scene changes to the correct player, and stays coherent under arbitrary action combinations. Trained on 10,000 hours of bot gameplay.
- **Link**: https://arxiv.org/abs/2607.05352

### AlayaWorld: Interactive Long-Horizon World Modeling — Full Technical Report
- **Authors**: AlayaWorld Team (Kaipeng Zhang, Chuanhao Li, et al.)
- **Affiliation**: Alibaba
- **Venue**: arXiv:2607.18367 (Jul 2026)
- **Key Innovation**: Interactive long-horizon video world model generating explorable, evolving virtual worlds from text/image/video input, targeting four coupled capabilities: interaction, persistent spatiotemporal consistency, stable long-horizon generation, and efficient response.
- **Link**: https://arxiv.org/abs/2607.18367

### ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU
- **Authors**: Fan Jiang, Zhaoxu Sun, Mengchao Wang, et al. (large team)
- **Affiliation**: —
- **Venue**: arXiv:2607.19191 (Jul 2026)
- **Key Innovation**: Action-conditioned world model for real-time long-horizon closed-loop interaction, distilled from a bidirectional teacher to a causal student; multi-source data (AAA games, simulators, internet video) with 14 deterministic quality checks + VLM assessment + synchronized action/text annotation — runs on a single desktop GPU.
- **Link**: https://arxiv.org/abs/2607.19191

### Lumine: An Open Recipe for Building Generalist Agents in 3D Open Worlds
- **Authors**: Weihao Tan, Xiangyang Li, Yunhao Fang, Heyuan Yao, Shi Yan, Hao Luo, Tenglong Ao, Huihui Li, Hongbin Ren, Bairen Yi, Yujia Qin, Bo An, Libin Liu, Guang Shi
- **Affiliation**: Tsinghua University / Peking University
- **Venue**: arXiv:2511.08892 (Nov 2025)
- **Key Innovation**: Open recipe for generalist embodied agents in 3D open worlds: a 3D navigation stack, perception module, and LLM planner trained on large-scale trajectory data — lays out a reproducible pipeline for open-world game/embodied agents.
- **Link**: https://arxiv.org/abs/2511.08892

### MARL-GPT: Foundation Model for Multi-Agent Reinforcement Learning
- **Authors**: Maria Nesterova, Mikhail Kolosov, Anton Andreychuk, Egor Cherepanov, Oleg Bulichev, Alexey Kovalev, Konstantin Yakovlev, Aleksandr Panov, Alexey Skrynnik
- **Affiliation**: AIRI / HSE University (Moscow)
- **Venue**: arXiv:2604.05943 (Apr 2026)
- **Key Innovation**: Single GPT-style model trained with offline RL on expert trajectories (400M SMACv2, 100M GRF, 1B POGEMA) that performs well across diverse MARL environments/tasks — a generalist foundation model for multi-agent RL rather than per-task models.
- **Link**: https://arxiv.org/abs/2604.05943

### Mind-Studio: Executable World Models with Lookahead Evaluation for Partially Observable Games
- **Authors**: Yifei Dong, Mingen Zheng, Linquan Wu, Jeff Z. Pan, Jiaxin Bai
- **Affiliation**: University of Edinburgh / HKUST
- **Venue**: arXiv:2606.16070 (Jun 2026)
- **Key Innovation**: Synthesizes complete executable pygame-style world models from state-action-next-state trajectories using LLMs (entropy-selected traces + game skill file), enabling independent planning via lookahead evaluation in partially observable games.
- **Link**: https://arxiv.org/abs/2606.16070

### Nano World Models: A Minimalist Implementation of Future Video Prediction
- **Authors**: Siqiao Huang, Partha Kaushik, Michael Chen, Hengkai Pan, Kaiwen Geng, Omar Chehab, Fernando Moreno-Pino, Max Simchowitz
- **Affiliation**: MIT
- **Venue**: arXiv:2605.23993 (May 2026)
- **Key Innovation**: Compact, reproducible codebase for diffusion-forcing-based world models — a unified interface for generative objectives, model scales, and action-conditioning that lets the research community ablate modern world-model design choices on modest compute.
- **Link**: https://arxiv.org/abs/2605.23993

---

## 4. Procedural Content Generation (PCG)

### The Garden of Forking Paths: Narrative Arc-Conditioned Gameplay Planning
- **Authors**: Yunge Wen, Chenliang Huang, Hangyu Zhou, Zhuo Zeng, Chun Ming Louis Po, Julian Togelius, Timothy Merino, Sam Earle
- **Affiliation**: NYU
- **Venue**: arXiv:2605.01245 (May 2026)
- **Key Innovation**: Generates branching games from user storylines conditioned on narrative archetypes (Hero's Journey, three-act structure): a diverse pool of independent nodes is assembled into a dungeon graph via arc-guided constraint algorithms, explicitly grounding PCG in narrative structure.
- **Link**: https://arxiv.org/abs/2605.01245

### From World-Gen to Quest-Line: A Dependency-Driven Prompt Pipeline for Coherent RPG Generation
- **Authors**: Dominik Borawski, Marta Szulc, Robert Chudy, Małgorzata Giedrowicz, Piotr Mironowicz
- **Affiliation**: —
- **Venue**: arXiv:2604.25482 (Apr 2026)
- **Key Innovation**: Multi-stage LLM prompt pipeline (world → NPCs → player character → campaign quests → quest-lines) modeling narrative dependencies through structured intermediate representations to keep large RPG content generation coherent and controllable.
- **Link**: https://arxiv.org/abs/2604.25482

### Multiverse: Language-Conditioned Multi-Game Level Blending via Shared Representation
- **Authors**: In-Chang Baek, Jiyun Jung, Geum-Hwan Hwang, Sung-Hyun Kim, Kyung-Joong Kim
- **Affiliation**: Hanyang University
- **Venue**: arXiv:2603.26782 (Mar 2026)
- **Key Innovation**: First language-conditioned generator that spans multiple games via a shared latent space aligning textual instructions with structural level representations, enabling cross-game level blending (e.g., taking a platformer layout and realizing it in another game's grammar).
- **Link**: https://arxiv.org/abs/2603.26782

### High-Dimensional Procedural Content Generation
- **Authors**: Kaijie Xu, Clark Verbrugge
- **Affiliation**: McGill University
- **Venue**: arXiv:2602.18943 (Feb 2026)
- **Key Innovation**: Elevates non-geometric gameplay dimensions (layers, state) to first-class coordinates of a joint generation space — Direction-Space augments geometry with a discrete layer dimension (validated in 4D reachability); a framework for expressing gameplay mechanics directly in PCG.
- **Link**: https://arxiv.org/abs/2602.18943

### Zero-Shot 3D Map Generation with LLM Agents: A Dual-Agent Architecture for PCG
- **Authors**: Lim Chien Her, Ming Yan, Yunshu Bai, Ruihao Li, Hao Zhang
- **Affiliation**: —
- **Venue**: arXiv:2512.10501 (Dec 2025)
- **Key Innovation**: Training-free Actor+Critic LLM architecture that bridges the semantic gap between abstract user instructions and strict PCG parameter specifications — zero-shot configuration of 3D map generation pipelines without fine-tuning.
- **Link**: https://arxiv.org/abs/2512.10501

### AutoBG: A Board Game Design Assistant with Interactive Ideation, Iterative Rulebook Generation, and Individualized Feedback
- **Authors**: Zizhen Li, Chuanhao Li, Yibin Wang, Jianwen Sun, Yukang Feng, Fanrui Zhang, Mingzhu Sun, Yifei Huang, Kaipeng Zhang
- **Affiliation**: —
- **Venue**: arXiv:2606.01976 (Jun 2026)
- **Key Innovation**: End-to-end board-game design assistant: interactive ideation, iterative rulebook generation, and individualized design feedback — an AI-native tool for the game-design loop itself (content generation beyond levels).
- **Link**: https://arxiv.org/abs/2606.01976

---

## 5. Game Benchmarks

### MINDGAMES: A Live Arena for Evaluating Social and Strategic Reasoning in Multi-Agent LLMs
- **Authors**: Kevin Wang, Anna Thöni, Benjamin Kempinski, et al. (large multi-institution consortium incl. Mathieu Laurière, Yoram Bachrach, Maria Polukarov, Cheston Tan, Tal Kachman, Pramod Viswanath, Atlas Wang)
- **Affiliation**: Multi-institution (NYU, DeepMind, NTU, UIUC, etc.)
- **Venue**: arXiv:2605.29512 (May 2026)
- **Key Innovation**: Multi-game live arena operationalizing theory-of-mind reasoning — belief attribution under hidden information, opponent modeling, strategic reasoning over extended interactions — as a persistent evaluation platform rather than static single-game benchmarks.
- **Link**: https://arxiv.org/abs/2605.29512

### OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics
- **Authors**: Mingxian Lin, Shengju Qian, Yuqi Liu, Yi-Hua Huang, Yiyu Wang, Wei Huang, Yitang Li, Fan Zhang, Zeyu Hu, Lingting Zhu, Xin Wang, Xiaojuan Qi
- **Affiliation**: HKU
- **Venue**: arXiv:2606.09826 (Jun 2026)
- **Key Innovation**: Real-time benchmark of twelve new Unreal Engine 5 games spanning Solo (7), PvP (3), and Coop (2) with unified action interfaces; introduces **Improvement Dynamics** — measuring how heterogeneous agent classes (commercial VLMs, open-weight VLMs, specialized game policies) improve across attempts rather than a single first-attempt score.
- **Link**: https://arxiv.org/abs/2606.09826

### GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents
- **Authors**: Mingyu Ouyang, Siyuan Hu, Kevin Qinghong Lin, Hwee Tou Ng, Mike Zheng Shou
- **Affiliation**: National University of Singapore
- **Venue**: arXiv:2604.07429 (Apr 2026)
- **Key Innovation**: Benchmark designed for standardized, verifiable evaluation of multimodal LLM agents in games, tackling heterogeneous action interfaces and heuristic verification — fine-grained perception, long-horizon planning, and precise control probes.
- **Link**: https://arxiv.org/abs/2604.07429

### SciCrafter: Can Current Agents Close the Discovery-to-Application Gap? A Minecraft Case Study
- **Authors**: Zhou Ziheng, Huacong Tang, Jinyuan Zhang, Haowei Lin, Bangcheng Yang, Qian Long, Fang Sun, Yizhou Sun, Yitao Liang, Ying Nian Wu, Demetri Terzopoulos, Xiaofeng Gao
- **Affiliation**: UCLA
- **Venue**: arXiv:2604.24697 (Apr 2026)
- **Key Innovation**: Minecraft benchmark operationalizing the discovery-to-application loop through parameterized redstone circuit tasks — agents must ignite lamps in specified patterns, and scaling target parameters sharply increases construction complexity, testing whether agents can both discover causal regularities and build working systems.
- **Link**: https://arxiv.org/abs/2604.24697

### OpenGuanDan: A Large-Scale Imperfect Information Game Benchmark
- **Authors**: Chao Li, Shangdong Yang, Chiheng Zhan, Zhenxing Ge, Yujing Hu, Bingkun Bao, Xingguo Chen, Yang Gao
- **Affiliation**: —
- **Venue**: arXiv:2602.00676 (Jan 2026)
- **Key Innovation**: New benchmark for GuanDan, a popular four-player multi-round Chinese card game — efficient simulation, large-scale evaluation for imperfect-information game AI research beyond poker-family games.
- **Link**: https://arxiv.org/abs/2602.00676

### FootsiesGym: A Fighting Game Benchmark for Two-Player Zero-Sum Imperfect-Information Games
- **Authors**: Chase McDonald, Nathan Tsang, Wesley N. Kerr
- **Affiliation**: —
- **Venue**: arXiv:2607.06514 (Jul 2026)
- **Key Innovation**: Open-source environment built on the minimalist 2D fighting game Footsies, isolating the cyclic, non-transitive strategic interactions of fighting-game neutral play; includes a vectorized high-throughput simulator and RL algorithm baselines — a compact proxy for cyclic meta-game learning.
- **Link**: https://arxiv.org/abs/2607.06514

### Causal Reinforcement Learning for Complex Card Games: A Magic: The Gathering Benchmark
- **Authors**: Cristiano da Costa Cunha, Ajmal Mian, Tim French, Wei Liu
- **Affiliation**: University of Western Australia
- **Venue**: arXiv:2605.06066 (May 2026)
- **Key Innovation**: MTG-Causal-RL: a Gymnasium benchmark on Magic: The Gathering combining sequential decision-making, hidden information, a 3,077-dim partial observation, 478-action masked space, and a hand-specified Structural Causal Model over strategic variables with per-factor credit tracking — first causal-RL benchmark for a complex commercial card game.
- **Link**: https://arxiv.org/abs/2605.06066

---

## 6. Industry Game AI

### TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale
- **Authors**: Zhouchonghao Wu, Akshay Rangesh, Weixin Li, Wei-Jer Chang, Zachary Lee, Tim Wang, Wei Zhan
- **Affiliation**: —
- **Venue**: arXiv:2607.13028 (Jul 2026)
- **Key Innovation**: Procedural driving simulator + self-play training stack: configurable C engine sustains **1.3M agent-steps/second on a single server GPU** (zero-copy CPU simulation / GPU inference), targeting safety-critical long-tail driving behavior with zero human demonstrations — a game-engine-style approach to autonomous-driving RL.
- **Link**: https://arxiv.org/abs/2607.13028

### ActionParty: Multi-Subject Action Binding in Generative Video Games
- **Authors**: Alexander Pondaven, Ziyi Wu, Igor Gilitschenski, Philip Torr, Sergey Tulyakov, Fabio Pizzati, Aliaksandr Siarohin
- **Affiliation**: Snap / University of Toronto / Oxford
- **Venue**: arXiv:2604.02330 (Apr 2026)
- **Key Innovation**: Makes generative video-game engines support **multiple simultaneously-controlled characters** by binding independent action sequences to distinct subjects in one scene — a step from single-character (GameNGen-style) playable worlds toward true multi-agent generative games.
- **Link**: https://arxiv.org/abs/2604.02330

### LPM 1.0: Video-based Character Performance Model
- **Authors**: Ailing Zeng, Casper Yang, Chauncey Ge, et al. (large team)
- **Affiliation**: Tencent AI Lab
- **Venue**: arXiv:2604.07823 (Apr 2026)
- **Key Innovation**: Production-grade video-based character performance model for games — converts real/designed video performances into controllable in-game character motion, a foundation model layer for game character animation pipelines.
- **Link**: https://arxiv.org/abs/2604.07823

### Play Like Champions: Counterfactual Feedback Generation in Latent Space
- **Authors**: Andrzej Białecki, Adam Mastalerz, Han Zhou
- **Affiliation**: —
- **Venue**: arXiv:2607.00190 (Jun 2026)
- **Key Innovation**: Inverts the "beat humans" agenda for real-time strategy: learns the latent geometry of expert play and generates **counterfactual feedback** to coach human players toward champion behavior — the chess/Go-style trainer role extended to RTS.
- **Link**: https://arxiv.org/abs/2607.00190

### Scouting by Reward: VLM-TO-IRL-Driven Player Selection for Esports
- **Authors**: Qing Yan, Wenyu Yang, Yufei Wang, Wenhao Ma, Linchong Hu, Yifei Jin, Anton Dahbura
- **Affiliation**: Johns Hopkins University
- **Venue**: arXiv:2604.14474 (Apr 2026)
- **Key Innovation**: Reframes esports player scouting as inverse RL: learns professional-specific reward functions from logged gameplay (guided by VLM-derived labels), then ranks prospects by stylistic alignment with a target tactical archetype rather than aggregate stats.
- **Link**: https://arxiv.org/abs/2604.14474

### GameVerse: Can Vision-Language Models Learn from Video-Based Reflection?
- **Authors**: Kuan Zhang, Dongchen Liu, Qiyue Zhao, Jinkun Hou, Xinran Zhang, Qinlei Xie, Miao Liu, Yiming Li
- **Affiliation**: —
- **Venue**: arXiv:2603.06656 (Mar 2026)
- **Key Innovation**: Reflect-and-retry evaluation paradigm: VLMs watch tutorials and replay failures to improve game policies, assessed via a cognitive hierarchical taxonomy — a mirror of how human players learn by watching and reflecting.
- **Link**: https://arxiv.org/abs/2603.06656

---

## 7. Related Techniques — Self-Play, Open-Ended Learning, MARL, Imitation/Inverse RL

### An Information-Theoretic Definition for Open-Ended Learning
- **Authors**: Wanqiao Xu, Yifan Zhu, Benjamin Van Roy
- **Affiliation**: Stanford University
- **Venue**: arXiv:2606.08369 (Jun 2026)
- **Key Innovation**: Defines open-endedness via the **bit-equivalent** — the information required to attain each level of expected reward. An environment is open-ended if an agent can achieve linear growth in bit-equivalent; establishes theoretical conditions for open-ended exploration.
- **Link**: https://arxiv.org/abs/2606.08369

### A Compositional Framework for Open-Ended Intelligence
- **Authors**: Ida Momennejad, Roberta Raileanu
- **Affiliation**: Microsoft Research / Meta FAIR
- **Venue**: arXiv:2606.15386 (Jun 2026)
- **Key Innovation**: Formalizes open-ended intelligence as compositional closure: a finite set of representational + algorithmic primitives (selection, recursion, branching) that generates novel problems/behaviors — a mathematics of generalization to out-of-distribution environments.
- **Link**: https://arxiv.org/abs/2606.15386

### PopuLoRA: Co-Evolving LLM Populations for Reasoning Self-Play
- **Authors**: Roger Creus Castanyer, Geoffrey Bradway, Lorenz Wolf, Maxwill Lin, Augustine N. Mavor-Parker, Matthew James Sargent
- **Affiliation**: —
- **Venue**: arXiv:2605.16727 (May 2026)
- **Key Innovation**: Population-based asymmetric self-play for RLVR post-training: teacher/student LoRA adapters on a shared frozen base, teachers propose problems, matched students solve under a programmatic verifier; LoRA weight-space evolution (mutation/crossover) replaces the self-calibration bottleneck of single-agent self-play.
- **Link**: https://arxiv.org/abs/2605.16727

### A Structural Threshold in Decision Capacity Governs Collapse in Self-Play RL
- **Authors**: Arahan Kujur
- **Affiliation**: —
- **Venue**: arXiv:2605.16315 (May 2026)
- **Key Innovation**: Across poker variants, matrix games, and a dice game, eliminating all positive-reach contingent decisions drives self-play agents to a deterministic exploitation attractor near-maximal loss; preserving a single contingent decision point prevents collapse — a threshold theory of self-play co-adaptation failure.
- **Link**: https://arxiv.org/abs/2605.16315

### When Actions Disappear: Adversarial Action Removal in Self-Play RL
- **Authors**: Arahan Kujur
- **Affiliation**: —
- **Venue**: arXiv:2605.16312 (May 2026)
- **Key Innovation**: Shows adversarial action masking (removing legal actions before the agent acts) damages self-play agents far more than perturbations, transfers across Q-learning/PPO/NFSP/DQN, is amplified by self-play, and shows no recovery — a robustness red flag for deployed game RL.
- **Link**: https://arxiv.org/abs/2605.16312

### ARMS: Automatic Reward Shaping for Sparse-Reward Multi-Agent RL
- **Authors**: Elie Abboud, Oren Gal
- **Affiliation**: —
- **Venue**: arXiv:2605.23562 (May 2026)
- **Key Innovation**: Self-supervised reward shaping for MARL that learns dense shaping signals from sparse environmental rewards via trajectory ranking — designed to preserve the strategic structure of the underlying game rather than merely speeding short-term optimization.
- **Link**: https://arxiv.org/abs/2605.23562

### Beyond Bayesian Nash: Learning Minimax-Regret Equilibria for Adversarial Team Games under Asymmetric Information
- **Authors**: Naman Aggarwal, Jonathan P. How
- **Affiliation**: MIT
- **Venue**: arXiv:2607.09993 (Jul 2026)
- **Key Innovation**: Shows Bayesian Nash equilibria are fragile to distribution shift in adversarial team games (e.g., hidden-goal path-finding), and learns **minimax-regret equilibria** robust to hidden opponent types and deception — a solution concept for adversarial game settings with asymmetric info.
- **Link**: https://arxiv.org/abs/2607.09993

### SuS: Strategy-Aware Surprise for Intrinsic Exploration
- **Authors**: Mark Kashirskiy, Ilya Makarov
- **Affiliation**: HSE University
- **Venue**: arXiv:2601.10349 (Jan 2026)
- **Key Innovation**: Curiosity-driven exploration combining Strategy Stability (behavioral consistency across timesteps) with Strategy Surprise (unexpected outcomes relative to the agent's strategy representation) — addressing prediction-error-based intrinsic rewards that can be gamed or forgotten.
- **Link**: https://arxiv.org/abs/2601.10349

### Inverse RL Helps Align AI by Imitating Humans (PARED)
- **Authors**: Michał Wiliński, Liu Leqi, Chirag Nagpal
- **Affiliation**: Apple
- **Venue**: arXiv:2607.24900 (Jul 2026)
- **Key Innovation**: Projected Alignment Reward Estimated from Demonstrations — shows demonstrations alone can yield an inspectable, reusable implicit reward that is then optimized on-policy, bridging inverse RL and alignment as an alternative to reward-model/RLHF pipelines.
- **Link**: https://arxiv.org/abs/2607.24900

---

## Summary Statistics

- **Total papers**: 53 (verified via arXiv API)
- **Categories covered**: 7
- **Key venues**: arXiv 2026 (fresh window mostly Jun–Jul 2026); complements 2026-07-27 and 2026-08-01 game digests with zero overlap
- **Notable trends**:
  - **Game RL going "human-flavored"**: superhuman-but-exploitable thresholds (Generals.io leaderboard win, AlphaZero sparsely-rewarded limits), solver-as-teacher credit assignment (CAST), and poker agents that deliberately exploit suboptimal play (AlphaExploitem)
  - **Multiplayer/real-time world models are the frontier**: DeepMind's multi-agent Rocket League world model, Alibaba's AlayaWorld, single-GPU ABot-World-0, and slow-fast dual-VLM agents (Latent Bridge, SPIKE) for real-time control
  - **Foundation models for games industrialize**: NitroGen (40k hours / 1k games), MARL-GPT (offline-RL MARL foundation model), Lumine 3D open worlds
  - **LLM agents as game QA/testers**: code-aware (CA2), personality-driven (MIMIC-Py), and LLM-vs-LLM deductive tests (Clue) — plus sobering results on sustained reasoning
  - **PCG moving up the abstraction ladder**: narrative-arc-conditioned generation, world→quest pipelines, cross-game level blending, and LLM-configurable 3D map pipelines
  - **Benchmarks diversify beyond Atari/poker**: fighting-game neutral play (FootsiesGym), causal card games (MTG), Chinese card games (GuanDan), live social-reasoning arenas (MINDGAMES), and discovery-to-application Minecraft (SciCrafter)
  - **Self-play fragility and open-endedness become first-class theory**: structural collapse thresholds, adversarial action removal, and information-theoretic open-endedness definitions
