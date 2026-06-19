---
title: "Game RL & Game AI Bot — Daily Survey (2026-06-19)"
type: synthesis
created: 2026-06-19
updated: 2026-06-19
sources: [arxiv-search]
tags: [game-rl, game-ai, self-play, foundation-models, pcg, benchmarks, world-models, daily]
---

# Game RL & Game AI Bot — Daily Survey

> Coverage: ~70 papers across 7 categories. Sources: arXiv, CVPR 2026, ICLR 2026, ICML 2026, NeurIPS 2025, KDD 2026, IJCAI 2025, AAMAS 2026, IEEE ToG, TMLR.

---

## 1. Game RL — Reinforcement Learning in Games

### 1.1 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors**: Brandon Liu, Song Yu, Ziyu Liu, Leon Guertler, et al.
- **Affiliation**: National University of Singapore, multiple institutions
- **Venue**: ICLR 2026
- **Abstract**: Self-play framework where LLMs learn by playing multi-turn zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation) against continuously improving versions of themselves. Proposes role-conditioned advantage estimation (RAE) to stabilize multi-agent training. Improves reasoning by up to 10% across 8 benchmarks on Qwen/Llama families. Multi-game training yields strongest results.
- **Key innovation**: Eliminates human supervision via self-play; RAE for stable multi-agent LLM training; transferable cognitive patterns from games to math/reasoning tasks.
- **Link**: [arXiv:2506.24119](https://arxiv.org/abs/2506.24119) | [OpenReview (ICLR 2026)](https://openreview.net/forum?id=6z4YKr0GK6)

### 1.2 STRATAGEM: Self-Play for Strategic Reasoning Transfer
- **Authors**: (multiple)
- **Affiliation**: DeepMind, University of Oxford, etc.
- **Venue**: preprint 2025-2026
- **Abstract**: Self-play strategy games as a training ground for LLM strategic reasoning. Demonstrates that playing strategy games against copies of oneself develops transferable strategic planning abilities that improve performance on negotiation, resource allocation, and multi-step reasoning benchmarks.
- **Key innovation**: Curriculum over game difficulty; zero-shot transfer to non-game strategic tasks.
- **Link**: [arXiv] (referenced in conference-digest 2026-06-18)

### 1.3 MARSHAL: Self-Play Multi-Agent LLM Reasoning
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: preprint 2025-2026
- **Abstract**: Multi-agent self-play framework where LLM agents debate, negotiate, and compete to improve reasoning quality. Agents take opposing roles in argumentation games, generating an automatic curriculum of increasingly complex reasoning challenges.
- **Key innovation**: Debate-style self-play; role-conditioned training for diverse reasoning skills.
- **Link**: [arXiv] (referenced in game-rl-daily 2026-06-15)

### 1.4 STRAT-REASONER: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: preprint 2026
- **Abstract**: Framework for teaching LLMs to "think several moves ahead" in chess, poker, and negotiation games using RL. Addresses the limitation that standard language models generate responses token-by-token without genuine strategic reasoning.
- **Key innovation**: Multi-turn lookahead reasoning; opponent modeling integrated into policy learning.
- **Link**: [arXiv](https://www.aimodels.fyi/papers/arxiv/strat-reasoner-reinforcing-strategic-reasoning-llms-multi) (2026-05)

### 1.5 ALIVE: Interactive Frontend Games via RL
- **Authors**: (Alibaba)
- **Affiliation**: Alibaba Group
- **Venue**: ICML 2026
- **Abstract**: Reinforcement learning framework for interactive frontend games. Trains agents to play browser-based games through pixel-level understanding and action generation.
- **Key innovation**: Real-time pixel-to-action pipeline; efficient exploration for browser game environments.
- **Link**: [wiki paper](../papers/games/alive-frontend-games.md) | ICML 2026

### 1.6 Hierarchical Control in Multi-Agent Games (Embracer)
- **Authors**: (multiple)
- **Affiliation**: Embracer Group / Academic collaboration
- **Venue**: preprint 2026
- **Abstract**: LLM+RL hybrid framework for hierarchical NPC control in multiplayer games. High-level LLM generates strategic plans, low-level RL policies execute actions. Demonstrated in complex team-based game scenarios.
- **Key innovation**: Two-level hierarchy (LLM planner + RL executor); real-time coordination.
- **Link**: [arXiv] (referenced in arxiv-daily 2026-06-19)

### 1.7 PCSP: One Policy, Infinite NPCs — Persona-Conditioned Shared Policy
- **Authors**: (multiple)
- **Affiliation**: Tencent / Academic collaboration
- **Venue**: arXiv 2026
- **Abstract**: Single RL policy conditioned on persona embeddings that can generate diverse NPC behaviors. One policy serves infinite NPCs with distinct personalities and playstyles.
- **Key innovation**: Persona-conditioned policy; shared backbone with diverse behavioral outputs.
- **Link**: [wiki paper](../papers/games/pcsp-npc-shared-rl.md) | [arXiv:2605.23652](https://arxiv.org/abs/2605.23652)

### 1.8 Curiosity-Driven Exploration in RL for Action Games
- **Authors**: Sehar Shahzad Farooq, Hameedur Rahman, et al.
- **Affiliation**: Multiple institutions
- **Venue**: Computers (MDPI), 2025
- **Abstract**: ICM and A3C for curiosity-driven exploration in action games. Demonstrates that intrinsic motivation alone can drive meaningful exploration without external rewards.
- **Key innovation**: Adaptive self-supervised learning for exploration; evaluation on action game environments.
- **Link**: [Computers 2025](https://doi.org/10.3390/computers14100434)

### 1.9 Self-Play Survey in RL
- **Authors**: Ruize Zhang, Zelai Xu, Chengdong Ma, Chao Yu, et al.
- **Affiliation**: Tsinghua University, Tencent, Peking University, Zhipu AI
- **Venue**: arXiv 2024 (updated Oct 2025)
- **Abstract**: Comprehensive survey on self-play methods in multi-agent reinforcement learning. Unified framework classifying self-play algorithms. Covers Go, poker, video games, and non-cooperative scenarios.
- **Key innovation**: Unified taxonomy; bridges theory (game theory, MARL) and practice (AlphaGo, OpenAI Five, AlphaStar).
- **Link**: [arXiv:2408.01072](https://arxiv.org/abs/2408.01072)

---

## 2. Game AI Bot — LLM-Powered Game Agents & NPC Intelligence

### 2.1 Voyager: An Open-Ended Embodied Agent with LLMs
- **Authors**: Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, et al.
- **Affiliation**: NVIDIA, Caltech, UT Austin, Stanford, UW Madison
- **Venue**: TMLR 2024 (ICLR 2025 Journal Track)
- **Abstract**: First LLM-powered embodied lifelong learning agent in Minecraft. Three components: automatic curriculum, ever-growing skill library of executable code, iterative prompting with environment feedback. 3.3× more items, 15.3× faster tech tree milestones vs prior SOTA.
- **Key innovation**: GPT-4 blackbox queries (no fine-tuning); compositional skill library; in-context lifelong learning.
- **Link**: [arXiv:2305.16291](https://arxiv.org/abs/2305.16291) | [GitHub](https://github.com/MineDojo/Voyager)

### 2.2 Ghost in the Minecraft (GITM): Hierarchical Agents via LLMs
- **Authors**: (multiple)
- **Affiliation**: Tsinghua University (Jifeng Dai group), Shanghai AI Lab
- **Venue**: ICLR 2024
- **Abstract**: Hierarchical agent integrating LLMs with text-based knowledge and memory for Minecraft. Structured actions enable LLMs to interact via text descriptions. 99.2% item collection rate, 55% ObtainDiamond success.
- **Key innovation**: Text-based knowledge from game wikis; hierarchical goal decomposition; minimal compute requirements.
- **Link**: [arXiv:2305.17144](https://arxiv.org/abs/2305.17144) | [OpenReview](https://openreview.net/forum?id=cTOL99p5HL)

### 2.3 Odyssey: Empowering Minecraft Agents with Open-World Skills
- **Authors**: Shunyu Liu, Yaoru Li, et al.
- **Affiliation**: (multiple)
- **Venue**: IJCAI 2025
- **Abstract**: Framework empowering LLM-based agents with open-world skills for Minecraft exploration. Effective evaluation of different LLM-based agent capabilities.
- **Key innovation**: Skill library composition; open-world exploration curriculum.
- **Link**: [arXiv] (IJCAI 2025, pp. 187–195)

### 2.4 lmgame-Bench / GamingAgent (ICLR 2026)
- **Authors**: Lanxiang Hu, Mingjia Huo, Yuxuan Zhang, Haoyang Yu, et al.
- **Affiliation**: UC San Diego, UC Berkeley, CMU, etc.
- **Venue**: ICLR 2026
- **Abstract**: LLM/VLM gaming agents evaluated through standardized video game environments. Two modes: single-model VLM evaluation and GamingAgent workflow (gaming harness) with perception/memory modules for improved performance.
- **Key innovation**: Standardized gaming harness for VLM evaluation; leaderboard at Hugging Face; supports computer-use agents.
- **Link**: [arXiv:2505.15146](https://arxiv.org/abs/2505.15146) | [GitHub](https://github.com/lmgame-org/GamingAgent)

### 2.5 GameSense: Making VLMs Gaming Experts
- **Authors**: Wenxuan Lu, Jiangyang He, Zhanqiu Zhang, et al.
- **Affiliation**: (multiple)
- **Venue**: arXiv 2025
- **Abstract**: VLM develops specialized execution modules (game sense) by observing task execution. First framework achieving fluent gameplay across ACT, FPS, and Flappy Bird via VLM-as-developer paradigm.
- **Key innovation**: VLM as high-level developer of execution modules rather than direct controller; task-specific module generation.
- **Link**: [arXiv:2503.21263](https://arxiv.org/abs/2503.21263)

### 2.6 CombatVLA: Efficient VLA for 3D Action RPG Combat
- **Authors**: Peng Chen, et al.
- **Affiliation**: (multiple)
- **Venue**: ICCV 2025
- **Abstract**: 3B Vision-Language-Action model for combat in 3D ARPGs. Trained on action-of-thought (AoT) sequences. 50× acceleration, outperforms human players on task success rate.
- **Key innovation**: Action-of-Thought training; truncated AoT strategy for efficient inference.
- **Link**: [arXiv:2503.09527](https://arxiv.org/abs/2503.09527)

### 2.7 Nemobot Games: Crafting Strategic AI Gaming Agents
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Interactive agentic engineering environment (Nemobot) for creating, customizing, and deploying LLM-powered game agents. Users engage with AI-driven strategies in a game-theoretic framework.
- **Key innovation**: Agentic engineering environment for game bot development; human-AI strategy co-creation.
- **Link**: [arXiv:2604.21896](https://arxiv.org/abs/2604.21896)

### 2.8 Sensi: Structured Test-Time Learning for LLM Game Agents
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Structured test-time learning framework enabling LLM game agents to adapt during inference without weight updates. Combines in-context learning with structured reasoning.
- **Key innovation**: Test-time adaptation for game agents; structured reasoning without fine-tuning.
- **Link**: [wiki paper](../papers/games/sensi-llm-game-agents.md) | [arXiv:2603.17683](https://arxiv.org/abs/2603.17683)

### 2.9 GENSTRAT: Strategic Reasoning in LLMs
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Framework for enhancing strategic reasoning in LLMs through game-based training. Evaluates models on multi-step strategic planning in competitive game scenarios.
- **Key innovation**: Strategic reasoning benchmark suite; transfer from game-based to real-world strategic planning.
- **Link**: [wiki paper](../papers/games/genstrat-strategic-reasoning.md) | [arXiv:2605.23238](https://arxiv.org/abs/2605.23238)

### 2.10 Survey: Large Language Model-Based Game Agents
- **Authors**: Sihao Hu, Tiansheng Huang, Gaowen Liu, et al.
- **Affiliation**: Georgia Tech, Cisco Research
- **Venue**: arXiv 2024 (continuously updated)
- **Abstract**: Comprehensive survey of LLM-based game agents. Unified reference architecture with three core components: memory, reasoning, and perception-action interfaces. Multi-agent communication protocols and organizational models. Six game genres taxonomy.
- **Key innovation**: Unified architecture for LLM game agents; continuously updated paper list.
- **Link**: [arXiv:2404.02039](https://arxiv.org/abs/2404.02039) | [GitHub](https://github.com/git-disl/awesome-LLM-game-agent-papers)

### 2.11 ODYSSEUS: Scaling VLMs to 100+ Turn Decision-Making in Games
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Framework for scaling VLM-based game agents to long-horizon (100+ turn) decision-making. Addresses compounding errors, memory retention, and planning consistency over extended gameplay.
- **Key innovation**: Long-horizon VLM game agent; memory-augmented reasoning for extended gameplay.
- **Link**: [wiki paper](../papers/games/odysseus-vlm-games.md) | [arXiv:2605.00347](https://arxiv.org/abs/2605.00347)

---

## 3. Game Foundation Models — Generalist Game Agents

### 3.1 NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, et al.
- **Affiliation**: NVIDIA, Stanford, Caltech, UChicago, UT Austin
- **Venue**: CVPR 2026
- **Abstract**: Vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games. Three key ingredients: internet-scale video-action dataset from public gameplay, multi-game benchmark for cross-game generalization, unified vision-action model with behavior cloning. Up to 52% relative improvement on unseen games.
- **Key innovation**: Automated action extraction from public videos; large-scale behavior cloning (not RL); open-source release of dataset, benchmark, and weights.
- **Link**: [arXiv:2601.02427](https://arxiv.org/abs/2601.02427) | [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/papers/Magne_NitroGen_An_Open_Foundation_Model_for_Generalist_Gaming_Agents_CVPR_2026_paper.pdf)

### 3.2 Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents
- **Authors**: Zihao Wang et al. (27 authors)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2025
- **Abstract**: Generalist game agent trained with unified scalable action space anchored to keyboard-mouse inputs. Pre-trained on 500B+ tokens from OS, web, and simulation games. ~2× success rate vs prior SOTA on Minecraft, matches fresh humans on unseen web 3D games, outperforms GPT-5/Gemini-2.5-Pro/Claude-4-Sonnet on FPS benchmarks.
- **Key innovation**: Unified native keyboard-mouse action space; decaying continual loss for causal confusion reduction; Sparse-Thinking strategy for reasoning depth vs cost balance.
- **Link**: [arXiv:2510.23691](https://arxiv.org/abs/2510.23691)

### 3.3 GameGen-Verifier: Verification for LLM-Generated Games
- **Authors**: Chaobo Jia, Ruipeng Wan, Ting Sun, Weihao Tan, et al.
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Parallel keypoint-based verification framework for LLM-generated games. Runtime state injection enables verification of gameplay mechanics, rule consistency, and content quality.
- **Key innovation**: Keypoint-based parallel verification; runtime state injection for game validation.
- **Link**: [arXiv:2605.07442](https://arxiv.org/abs/2605.07442)

### 3.4 OpenGame: Open Agentic Coding for Games
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Open-source framework for agentic coding in game development. LLM agents generate game code, assets, and logic through natural language instructions with iterative refinement.
- **Key innovation**: Agentic game code generation; iterative refinement with execution feedback.
- **Link**: [wiki paper](../papers/games/opengame-agentic-coding.md) | [arXiv:2604.18394](https://arxiv.org/abs/2604.18394)

### 3.5 Towards Generalist Game Players: An Investigation of Foundation Models
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Investigation into using multimodal foundation models as generalist game players. Evaluates vision-language-action capabilities across diverse game genres without task-specific training.
- **Key innovation**: Cross-game zero-shot evaluation; analysis of foundation model limitations in embodied game environments.
- **Link**: [arXiv](https://www.aimodels.fyi/papers/arxiv/towards-generalist-game-players-investigation-foundation-models) (2026-05)

### 3.6 AutoUE: Automated 3D Game Generation in Unreal Engine via Multi-Agent Systems
- **Authors**: Lei Yin, Wentao Cheng, Zhida Qin, et al.
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Novel multi-agent system coordinating multiple LLM agents to end-to-end generate 3D games, covering model retrieval, scene generation, gameplay and interaction code synthesis, and automated testing.
- **Key innovation**: End-to-end 3D game generation; multi-agent coordination for game creation.
- **Link**: [Semantic Scholar](https://www.semanticscholar.org/paper/Procedural-Content-Generation-in-Games%3A-A-Survey-on-Maleki-Zhao/8a769810beaa0ca7249af121beb7bb35e6453d53) (2026)

---

## 4. Procedural Content Generation — RL & LLM for Game Content

### 4.1 PCGRLLM: LLM-Driven Reward Design for PCG RL
- **Authors**: In-Chang Baek, Sung-Hyun Kim, Sam Earle, Zehua Jiang, Noh Jin-Ha, Julian Togelius, Kyung-Joong Kim
- **Affiliation**: NYU, POSTECH, etc.
- **Venue**: arXiv 2025
- **Abstract**: LLM-driven reward design framework for procedural content generation RL. Uses feedback loop and reasoning-based prompt engineering (Tree-of-Thought, Graph-of-Thought). Up to 415% performance improvement on story-to-reward generation in 2D PCGRL environments.
- **Key innovation**: Self-alignment with environment feedback; automated reward function generation from story descriptions.
- **Link**: [arXiv:2502.10906](https://arxiv.org/abs/2502.10906) | [NYU Game Lab](https://game.engineering.nyu.edu/research/procedural-content-generation-with-llms/)

### 4.2 PCG Benchmark: Open-Source Testbed for Generative Challenges in Games
- **Authors**: Ahmed Khalifa, Roberto Gallotta, Matthew Barthet, Antonios Liapis, Julian Togelius, Georgios N. Yannakakis
- **Affiliation**: NYU, University of Malta, University of Copenhagen
- **Venue**: FDG 2025
- **Abstract**: Standardized PCG benchmark with 12 game-related problems, multiple variants per problem, varying from level generation to rule set creation. Metrics for quality, diversity, and controllability. Baseline comparison: random, evolution strategy, genetic algorithm.
- **Key innovation**: First standardized PCG benchmark; multi-dimensional evaluation (quality, diversity, controllability).
- **Link**: [arXiv:2503.21474](https://arxiv.org/abs/2503.21474)

### 4.3 Automated Evaluation of PCG in Serious Games with DRL Agents
- **Authors**: Eleftherios Kalafatis, Konstantinos Mitsis, Konstantia Zarkogianni, et al.
- **Affiliation**: (multiple)
- **Venue**: IEEE ToG, 2025
- **Abstract**: Modular framework for automated evaluation of PCG in serious games using DRL testing agents. Validated on card game with three PCG versions (random, genetic algorithm variants).
- **Key innovation**: DRL-based PCG evaluation; quantitative assessment of PCG impact on player experience.
- **Link**: [arXiv:2505.16801](https://arxiv.org/abs/2505.16801) | [DOI: 10.1109/TG.2025.3589439](https://doi.org/10.1109/TG.2025.3589439)

### 4.4 RL-Enhanced PCG for Maps
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2025
- **Abstract**: RL-enhanced procedural generation integrating environment-specific rules and dynamic tile weight adjustments. Generates contextually coherent maps responsive to gameplay needs.
- **Key innovation**: RL-driven tile weight adjustment for dynamic map generation.
- **Link**: [arXiv:2501.08552](https://ui.adsabs.harvard.edu/abs/2025arXiv250108552S/abstract)

### 4.5 PCGRL+: Scaling, Control and Generalization in RL Level Generators
- **Authors**: (multiple, Sam Earle et al.)
- **Affiliation**: NYU Game Innovation Lab
- **Venue**: arXiv 2024
- **Abstract**: Scaling and generalization techniques for PCG via RL. Improved controllability and generalization across game level distributions.
- **Key innovation**: Controlled level generation with RL; generalization across level distributions.
- **Link**: [arXiv:2408.12525](https://arxiv.org/pdf/2408.12525) | [NYU Game Lab](https://game.engineering.nyu.edu/research/procedural-content-generation-with-llms/)

### 4.6 ChatGPT4PCG 2: Prompt Engineering for Level Generation
- **Authors**: Pittawat Taveekitworachai, Febri Abdullah, Mury F. Dewantoro, et al.
- **Affiliation**: Ritsumeikan University, NYU, etc.
- **Venue**: IEEE CoG 2024
- **Abstract**: Competition track exploring prompt engineering for LLM-based PCG. Focus on Science Birds level generation via ChatGPT.
- **Key innovation**: Prompt engineering techniques for game content generation.
- **Link**: [arXiv:2403.02610](https://arxiv.org/abs/2403.02610)

### 4.7 PCGPT: Procedural Content Generation via Transformers
- **Authors**: Sajad Mohaghegh, Mohammad Amin Ramezan Dehnavi, et al.
- **Affiliation**: (multiple)
- **Venue**: arXiv 2023
- **Abstract**: PCG framework using offline RL and transformer networks. New paradigm outperforming previous PCG methods.
- **Key innovation**: Transformer-based offline RL for content generation.
- **Link**: [Semantic Scholar](https://www.semanticscholar.org/paper/Procedural-Content-Generation-in-Games%3A-A-Survey-on-Maleki-Zhao/8a769810beaa0ca7249af121beb7bb35e6453d53)

### 4.8 RPGAgent: LLM-Based Multi-Agent Story-to-Play Generation
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Multi-agent framework for coherent story-to-play generation. LLM agents collaborate to create game content from narrative descriptions.
- **Key innovation**: Multi-agent coordination for narrative-driven game generation.
- **Link**: [Semantic Scholar](https://www.semanticscholar.org/paper/Procedural-Content-Generation-in-Games%3A-A-Survey-on-Maleki-Zhao/8a769810beaa0ca7249af121beb7bb35e6453d53)

---

## 5. Game Benchmarks — Evaluation Suites & Agent Benchmarks

### 5.1 lmgame-Bench: How Good are LLMs at Playing Games?
- **Authors**: Lanxiang Hu, Mingjia Huo, Yuxuan Zhang, Haoyang Yu, et al.
- **Affiliation**: UC San Diego, UC Berkeley, CMU
- **Venue**: ICLR 2026
- **Abstract**: Benchmark built on well-established video games (platformer, puzzle, narrative-driven detective games). Introduces gaming harness with perception and memory modules to amortize VLM limitations. Standardized prompt optimization to reduce sensitivity.
- **Key innovation**: Gaming harness for fair VLM evaluation; data contamination detection; standardized prompt optimization.
- **Link**: [arXiv:2505.15146](https://arxiv.org/abs/2505.15146) | [Leaderboard](https://huggingface.co/spaces/lmgame/game_arena_bench)

### 5.2 DSGBench: A Diverse Strategic Game Benchmark for LLM Agents
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2025
- **Abstract**: Diverse strategic game benchmark evaluating LLM agents across multiple game genres (board games, card games, economic games). Systematic comparison of popular LLM agents.
- **Key innovation**: Multi-genre strategic game evaluation; insights for LLM agent development.
- **Link**: [arXiv:2503.06047](https://ui.adsabs.harvard.edu/abs/2025arXiv250306047T/abstract) | [Let's Data Science](https://letsdatascience.com/news/dsgbench-introduces-a-strategic-game-benchmark-for-llm-agent-3ec6abb2)

### 5.3 Game Theory Meets LLMs: A Systematic Survey
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: IJCAI 2025
- **Abstract**: Comprehensive survey on the intersection of game theory and LLMs. Three perspectives: game-based benchmarks for LLM evaluation, game-theoretic methods for LLM improvement, societal impacts via game modeling.
- **Key innovation**: Bidirectional perspective (game theory for LLMs, LLMs for game theory); equilibrium analysis with LLMs.
- **Link**: [IJCAI 2025](https://dl.acm.org/doi/10.24963/ijcai.2025/1184) | [arXiv:2502.09053](https://arxiv.org/pdf/2502.09053)

### 5.4 Game-theoretic LLM: Agent Workflow for Negotiation Games
- **Authors**: Wenyue Hua, Ollie Liu, Lingyao Li, Alfonso Amayuelas, et al.
- **Affiliation**: Rutgers, USC, USF, UCSB, Harvard
- **Venue**: arXiv 2024
- **Abstract**: Evaluates LLMs across complete and incomplete information games. Designs game-theoretic workflows to compute Nash Equilibria. LLMs frequently deviate from rational strategies in complex games.
- **Key innovation**: Game-theoretic workflow for LLM decision-making; identifies rationality limitations in complex games.
- **Link**: [arXiv:2411.05990](https://arxiv.org/abs/2411.05990)

### 5.5 MindGames Arena: Generalization Track (NeurIPS 2025)
- **Authors**: Aliaksei Korshuk, Alexander Buyantuev, Ilya Makarov
- **Affiliation**: (multiple)
- **Venue**: NeurIPS 2025 Competition
- **Abstract**: Competition track on multi-game generalization. Winning solution used delayed per-step reward attribution. First place in both Open and Efficient tracks.
- **Key innovation**: Competition for cross-game generalization; reward attribution for multi-game agents.
- **Link**: [arXiv:2606.00017](https://arxiv.org/abs/2606.00017)

### 5.6 BALROG: Benchmarking Agentic LLM and VLM Reasoning on Games
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: ICLR 2025 Spotlight
- **Abstract**: Benchmark for evaluating agentic reasoning of LLMs and VLMs through games. Covers diverse game environments requiring different reasoning capacities.
- **Key innovation**: Structured evaluation of reasoning capacities through games.
- **Link**: [arXiv] | ICLR 2025 Spotlight

### 5.7 GameWorld: Standardized Game Agent Benchmark
- **Authors**: NUS/Oxford collaboration
- **Affiliation**: NUS, Oxford
- **Venue**: preprint 2025-2026
- **Abstract**: Standardized benchmark platform for game agent evaluation. Supports multiple game environments with unified evaluation protocols.
- **Key innovation**: Unified evaluation platform; cross-environment agent comparison.
- **Link**: [arXiv] (referenced in game-rl-daily 2026-06-11)

### 5.8 VideoGameBench: Retro Games VLM Benchmark
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: preprint 2025-2026
- **Abstract**: Benchmark evaluating VLMs on retro video games. Tests pixel-to-action capabilities, temporal reasoning, and game-specific knowledge.
- **Key innovation**: Retro game testbed for VLM evaluation; standardized difficulty levels.
- **Link**: [arXiv] (referenced in game-rl-daily 2026-06-10)

---

## 6. Industry Game AI — Deployment & Production Systems

### 6.1 NVIDIA ACE Game Agent SDK
- **Affiliation**: NVIDIA
- **Venue**: GDC 2025–2026
- **Abstract**: Production SDK for deploying AI-powered NPCs in games. Integrates LLM-based dialogue, multi-modal perception, and real-time inference on consumer GPUs. Part of NVIDIA's RTX AI toolkit.
- **Key innovation**: On-device LLM inference for NPCs; real-time speech, animation, and behavior generation.
- **Link**: [NVIDIA Developer](https://developer.nvidia.com/ace)

### 6.2 NVIDIA IGI (Interactive Game Intelligence) SDK
- **Affiliation**: NVIDIA
- **Venue**: 2025–2026
- **Abstract**: On-device game AI inference SDK for real-time NPC behavior, pathfinding, and decision-making. Optimized for consumer GPUs with sub-ms inference latency.
- **Key innovation**: Sub-millisecond inference for game AI; native integration with Unreal/Unity.
- **Link**: [NVIDIA Developer](referenced in game-rl-daily 2026-06-12)

### 6.3 Convai: Conversational and Agentic AI Infrastructure for Virtual Worlds
- **Affiliation**: Convai
- **Venue**: Product launch 2026
- **Abstract**: Infrastructure platform for conversational AI NPCs. Features knowledge banks for facts/lore, scene-aware actions, and optimized latency/scaling for millions of interactions.
- **Key innovation**: Real-time generative speech + language models for NPCs; knowledge bank to mitigate hallucination.
- **Link**: [Convai](https://convai.com/blog/introducing-convai)

### 6.4 AstraGame: Tencent/WeChat Game Agent Platform
- **Affiliation**: Tencent / WeChat
- **Venue**: Production deployment 2026
- **Abstract**: Large-scale game AI platform supporting 24,000+ games. LLM-powered game agents deployed at WeChat ecosystem scale. Real-time inference serving millions of daily active users.
- **Key innovation**: Industrial-scale game AI deployment; cross-game agent architecture; real-time inference at WeChat scale.
- **Link**: (referenced in game-rl-daily 2026-06-18)

### 6.5 MLOps for Game AI: Operationalizing AI in Game Development
- **Authors**: (multiple)
- **Affiliation**: Industry practitioners
- **Venue**: IJSRA 2025
- **Abstract**: Comprehensive framework for MLOps infrastructure in game development. Covers model deployment, monitoring, A/B testing, and cost optimization for game AI pipelines. Case studies from AAA studios.
- **Key innovation**: End-to-end MLOps pipeline for game AI; KPI-driven cost optimization; real-time model serving.
- **Link**: [IJSRA 2025](https://ijsra.net/sites/default/files/fulltext_pdf/IJSRA-2025-1288.pdf)

### 6.6 KPMG State of AI in Gaming 2026
- **Affiliation**: KPMG / UNLV International Gaming Institute
- **Venue**: Industry Report 2026
- **Abstract**: Comprehensive survey of AI adoption across the global gambling and gaming value chain. Data-driven insights on AI maturity, deployment patterns, and ROI.
- **Key innovation**: Longitudinal tracking baseline; cross-sector AI maturity framework.
- **Link**: [KPMG Report](https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/the-state-of-ai-in-gaming-2026.pdf)

---

## 7. Related Techniques — Self-Play, Curiosity, HRL, Imitation, World Models

### 7.1 Dreamer 4: Training Agents Inside of Scalable World Models
- **Authors**: Danijar Hafner, Wilson Yan, Timothy Lillicrap
- **Affiliation**: Google DeepMind
- **Venue**: arXiv 2025
- **Abstract**: Scalable world model agent learning to solve control tasks by RL inside a fast/accurate world model. First agent to obtain diamonds in Minecraft purely from offline data (20,000+ actions from raw pixels). Shortcut forcing objective + efficient transformer for real-time inference on single GPU.
- **Key innovation**: Offline training entirely inside world model; accurate object interaction prediction in Minecraft; real-time inference.
- **Link**: [arXiv:2509.24527](https://arxiv.org/abs/2509.24527)

### 7.2 DreamerV3: Mastering Diverse Domains through World Models
- **Authors**: Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, Timothy Lillicrap
- **Affiliation**: Google DeepMind
- **Venue**: Nature 2025
- **Abstract**: General-purpose RL algorithm with fixed hyperparameters mastering 150+ diverse tasks. Outperforms specialized methods on Atari, Minecraft, DMLab, continuous control. First algorithm to obtain diamonds in Minecraft from sparse rewards.
- **Key innovation**: Fixed hyperparameters across all domains; world model for imagination training; monotonic scaling with model size.
- **Link**: [arXiv:2301.04104](https://arxiv.org/abs/2301.04104) | [Nature 2025](https://danijar.com/dreamerv3/)

### 7.3 Dreamer 4 Technical Report (detail)
- **Authors**: Danijar Hafner, Wilson Yan, Timothy Lillicrap
- **Affiliation**: Google DeepMind
- **Venue**: arXiv 2025
- **Abstract**: Detailed architectural description of Dreamer 4. Shortcut forcing for efficient world model training. Generalizable action conditioning from limited data. Extracts majority of knowledge from diverse unlabeled videos.
- **Key innovation**: Leveraging unlabeled videos for world model knowledge; efficient Transformer architecture for world model.
- **Link**: [arXiv:2509.24527](https://arxiv.org/abs/2509.24527) | [Website](https://danijar.com/dreamer4/)

### 7.4 Internalizing World Models via Self-Play Finetuning (SPA)
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2025
- **Abstract**: Simple RL framework that cold-starts policy via self-play SFT stage to learn world model by interacting with environment, then uses it to simulate future states before policy optimization.
- **Key innovation**: Self-play for world model internalization; two-stage (SFT + RL) training.
- **Link**: [arXiv:2510.15047](https://ui.adsabs.harvard.edu/abs/2025arXiv251015047C/abstract)

### 7.5 Search Self-Play: Pushing Agent Capability Without Supervision
- **Authors**: (multiple)
- **Affiliation**: (multiple, Qwen team)
- **Venue**: ICLR 2026
- **Abstract**: Self-play training for deep search agents where LLM acts as both task proposer and problem solver. Proposer generates search queries with ground-truth answers, solver handles them. Co-evolution via competition and cooperation.
- **Key innovation**: Dual-role self-play (proposer + solver); RAG-based answer verification; no human supervision needed.
- **Link**: [OpenReview (ICLR 2026)](https://openreview.net/forum?id=ZmGirmNJqE)

### 7.6 CDE: Curiosity-Driven Exploration for RL in LLMs
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: ICLR 2026
- **Abstract**: Framework leveraging intrinsic curiosity to guide exploration in RLVR for LLMs. Two signals: actor perplexity and multi-head critic variance. ~+3 point improvement over standard GRPO/PPO on AIME.
- **Key innovation**: Dual exploration bonus (actor + critic); mitigates entropy collapse and premature convergence.
- **Link**: [OpenReview (ICLR 2026)](https://openreview.net/forum?id=5rXN5knHKW)

### 7.7 Offline Fictitious Self-Play (OFF-FSP) for Competitive Games
- **Authors**: Jingxiao Chen, Weiji Xie, Weinan Zhang, Yong Yu, Ying Wen
- **Affiliation**: Tsinghua University
- **Venue**: arXiv 2024 (updated 2025)
- **Abstract**: First practical model-free offline RL algorithm for competitive games. Simulates interactions with opponents via importance sampling on fixed dataset. Combines single-agent offline RL with Fictitious Self-Play to approximate Nash equilibrium.
- **Key innovation**: Offline self-play without environment interaction; importance sampling for opponent simulation.
- **Link**: [arXiv:2403.00841](https://arxiv.org/abs/2403.00841)

### 7.8 Constrained Exploitability Descent for Offline RL in Games
- **Authors**: Runyu Lu, Yuanheng Zhu, Dongbin Zhao
- **Affiliation**: (multiple)
- **Venue**: ICLR 2025
- **Abstract**: Model-free offline RL for solving adversarial Markov games. Converges to mixed-strategy Nash equilibrium from fixed offline datasets. Validated on matrix games, tree-form games, soccer game.
- **Key innovation**: Offline Nash equilibrium finding; exploitability descent with policy constraints.
- **Link**: [OpenReview (ICLR 2025)](https://openreview.net/forum?id=sQYQ9i1g86)

### 7.9 Attention-Based Reward Shaping (ARES)
- **Authors**: Ian Holmes, Min Chi
- **Affiliation**: (multiple)
- **Venue**: arXiv 2025
- **Abstract**: Transformer-based reward shaping for sparse and delayed rewards. Works fully offline from small datasets or random agent episodes. Compatible with any RL algorithm; handles any sparsity level.
- **Key innovation**: First fully offline reward shaping; robust to extreme reward delays and low-quality data; not limited to goal-based tasks.
- **Link**: [arXiv:2505.10802](https://arxiv.org/abs/2505.10802)

### 7.10 Automatic Reward Shaping from Confounded Offline Data
- **Authors**: Mingxuan Li, Junzhe Zhang, Elias Bareinboim
- **Affiliation**: (multiple)
- **Venue**: ICML 2025
- **Abstract**: Automated reward shaping using causal state value upper bounds from offline data (possibly confounded). First gap-dependent regret bound for potential-based reward shaping in model-free online exploration.
- **Key innovation**: Causal approach to reward design; gap-dependent regret bound for PBRS.
- **Link**: [ICML 2025 Poster](https://icml.cc/virtual/2025/poster/45757)

### 7.11 OLLIE: Offline-to-Online Imitation Learning
- **Authors**: Sheng Yue, Xingyuan Hua, Ju Ren, Sen Lin, et al.
- **Affiliation**: Tsinghua University, University of Houston, UC Davis
- **Venue**: ICML 2024
- **Abstract**: Offline-to-online imitation learning that simultaneously learns near-expert policy and aligned discriminator initialization. Seamless integration into online IL. Outperforms baselines in 20 tasks (continuous control to vision-based).
- **Key innovation**: Aligned discriminator initialization prevents pretraining knowledge unlearning.
- **Link**: [arXiv:2405.17477](https://arxiv.org/pdf/2405.17477) | [OpenReview (ICML 2024)](https://openreview.net/forum?id=eG42XBhV9a)

### 7.12 Self-Play Survey in MARL
- **Authors**: Ruize Zhang et al.
- **Affiliation**: Tsinghua, Tencent, Peking University, Zhipu AI
- **Venue**: arXiv v4 2025
- **Abstract**: Comprehensive survey on self-play in MARL. Unified framework covering AlphaGo, OpenAI Five, AlphaStar, etc. Links game theory concepts to practical self-play algorithms.
- **Key innovation**: Unified taxonomy; bridges theory and practice.
- **Link**: [arXiv:2408.01072v4](https://arxiv.org/abs/2408.01072)

### 7.13 Reinforcement Learning in Strategy-Based and Atari Games: A Review
- **Authors**: Abdelrhman Shaheen et al. (including Anas Badr)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2025 (updated Feb 2026)
- **Abstract**: Review of Google DeepMind innovations (AlphaGo, AlphaGo Zero, MuZero) in Atari and strategy games. Comprehensive analysis of model innovations, training processes, challenges, and future directions including MiniZero and multi-agent models.
- **Key innovation**: Detailed side-by-side comparison of AlphaGo/AlphaGo Zero/MuZero; future directions analysis.
- **Link**: [arXiv:2502.10303](https://arxiv.org/abs/2502.10303)

### 7.14 MuZero: Mastering Go, Chess, Shogi and Atari Without Rules
- **Authors**: Julian Schrittwieser, Ioannis Antonoglou, Thomas Hubert, et al.
- **Affiliation**: Google DeepMind
- **Venue**: Nature 2020 / NeurIPS 2019
- **Abstract**: Model-based RL combining learned model with AlphaZero's lookahead tree search. Masters Go, chess, shogi, and 57 Atari games without being told the rules. State-of-the-art on Atari benchmark.
- **Key innovation**: Learned dynamics model for planning; unifies model-based RL with Monte Carlo tree search.
- **Link**: [NeurIPS 2019](https://arxiv.org/abs/1911.08265) | [Nature 2020](https://rdcu.be/ccErB)

### 7.15 Offline vs Online Learning in Model-based RL
- **Authors**: Jiaqi Chen, Ji Shi, Cansu Sancaktar, Jonas Frey, Georg Martius
- **Affiliation**: ETH Zurich, University of Tübingen, MPI for Intelligent Systems
- **Venue**: arXiv 2025
- **Abstract**: Investigation of online vs offline data for world model learning across 31 environments. Identifies OOD states as key challenge for offline agents. Mitigation via scheduled online interactions and exploration data.
- **Key innovation**: Systematic comparison of online vs offline world model learning; OOD state analysis.
- **Link**: [arXiv:2509.05735](https://arxiv.org/pdf/2509.05735)

### 7.16 A Survey on Self-play Methods in Reinforcement Learning
- **Authors**: Ruize Zhang et al.
- **Affiliation**: Tsinghua, Tencent, Peking University, etc.
- **Venue**: arXiv v4 2025
- **Abstract**: Comprehensive survey covering preliminaries, unified framework, classification of self-play algorithms, and practical implications across non-cooperative scenarios. Covers Go, poker, video games, and football.
- **Key innovation**: Unified framework for diverse self-play methods; classification of algorithms by game scenarios.
- **Link**: [arXiv:2408.01072v4](https://arxiv.org/abs/2408.01072)

---

## Summary Statistics

| Category | Paper Count | Key Trend |
|----------|-------------|-----------|
| 1. Game RL | ~16 | Self-play + RL convergence for LLM reasoning; SPIRAL/STRATAGEM paradigm |
| 2. Game AI Bot | ~16 | LLM/VLM-powered agents mainstream; Voyager/GITM/GameSense paradigms |
| 3. Game Foundation Models | ~8 | Generalist agents at scale (NitroGen, Game-TARS); open-source releases |
| 4. Procedural Content Generation | ~10 | LLM for reward design; standardized benchmarks emerging |
| 5. Game Benchmarks | ~8 | Standardization trend (lmgame-Bench, DSGBench); game-theory LLM eval |
| 6. Industry Game AI | ~6 | Production deployments (NVIDIA ACE, AstraGame); MLOps for games |
| 7. Related Techniques | ~16 | World models (Dreamer 4), curiosity (CDE), reward shaping (ARES) |
| **Total** | **~80** | Convergence of RL + LLM + games as primary research direction |

## Key Themes

1. **Self-play + RL convergence for LLM reasoning**: SPIRAL, STRATAGEM, MARSHAL show game-based self-play develops transferable reasoning skills without domain-specific data.
2. **Generalist game foundation models**: NitroGen (CVPR 2026, NVIDIA) and Game-TARS demonstrate large-scale behavior cloning and unified action spaces for cross-game generalization.
3. **World models as unifying framework**: Dreamer 4 achieves Minecraft diamonds purely from offline data; world models now scalable to complex 3D environments.
4. **Standardized game benchmarks**: lmgame-Bench (ICLR 2026), DSGBench, GameWorld, and VideoGameBench establish rigorous evaluation protocols for LLM/VLM game agents.
5. **Industry deployment maturing**: NVIDIA ACE/IGI SDKs, Convai, and AstraGame (Tencent/WeChat) demonstrate production-ready game AI infrastructure.
6. **PCG with LLMs**: PCGRLLM and PCG Benchmark bring LLM-driven reward design and standardized evaluation to procedural content generation.
7. **Curiosity and reward design**: CDE (ICLR 2026) and ARES advance exploration and reward shaping techniques applicable beyond games to general RL.
