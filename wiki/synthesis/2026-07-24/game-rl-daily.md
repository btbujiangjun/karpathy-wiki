---
title: "Game RL & Game AI Bot — Daily Paper Digest (July 24, 2026)"
type: synthesis
created: 2026-07-24
updated: 2026-07-24
sources: [arxiv, proceedings]
tags: [game-rl, game-ai, self-play, llm-agents, game-foundation-models, pcg, benchmarks, world-models, hierarchical-rl, procedural-generation]
---

# Game RL & Game AI Bot — Daily Paper Digest (July 24, 2026)

**Generated:** 2026-07-24

---

## 1. Game RL / Multi-Agent / Self-Play

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning
- **Authors:** Bo Liu, Leon Guertler, Simon Yu, Zichen Liu, Penghui Qi, Daniel Balcells, Mickel Liu, Cheston Tan, Weiyan Shi, Min Lin, Wee Sun Lee, Natasha Jaques
- **Affiliation:** NUS / SingVerse Research / University of Sydney
- **Venue:** ICLR 2026 (Published as conference paper)
- **arXiv:** [2506.24119](https://arxiv.org/abs/2506.24119)
- **Key Innovation:** Self-play framework where LLMs learn by playing multi-turn zero-sum games against continuously improving versions of themselves, generating automatic curriculum of stronger opponents without human supervision. Proposes role-conditioned advantage estimation (RAE) to stabilize multi-agent training under sparse zero-sum rewards. Multi-game training (TicTacToe, Kuhn Poker, Simple Negotiation) yields strongest results. Up to 10% improvement across 8 reasoning benchmarks on 4 models (Qwen, Llama), outperforming SFT on 25,000 expert game trajectories.
- **Link:** [arXiv 2506.24119](https://arxiv.org/abs/2506.24119)

### Self-Play Meta-Reinforcement Learning in Multi-Agent Games
- **Authors:** Imre Gergely Mali
- **Affiliation:** (Published February 2026)
- **Venue:** Acta Universitatis Sapientiae, Informatica 18, 5 (2026)
- **Key Innovation:** Extends meta-RL to multi-agent game settings, enabling fast adaptation in multi-agent environments through self-play meta-learning. Demonstrates that meta-RL facilitates rapid strategy adaptation in competitive and cooperative game settings.
- **Link:** [Springer](https://link.springer.com/article/10.1007/s44427-026-00021-y)

### A Survey on Self-play Methods in Reinforcement Learning
- **Authors:** (Multiple authors)
- **Affiliation:** (Survey paper)
- **arXiv:** [2408.01072](https://arxiv.org/abs/2408.01072) (Updated v3)
- **Key Innovation:** Systematic survey categorizing self-play algorithms into four families: traditional self-play, PSRO series, ongoing-training-based, and regret-minimization-based. Unified framework for MARL + self-play. Covers multi-drone volleyball, robotics sim2real, and LLM reasoning via self-play. Identifies open directions in population diversity, transfer, and scalability.
- **Link:** [arXiv 2408.01072](https://arxiv.org/abs/2408.01072)

### PopuLoRA: Co-Evolving LLM Populations for Reasoning Self-Play
- **Authors:** Roger Creus Castanyer, Geoffrey Bradway, Lorenz Wolf, Max Lin, Augustine N. Mavor-Parker, M. J. Sargent
- **arXiv:** [2607.xxxxx](https://arxiv.org/abs/) (2026)
- **Key Innovation:** Population-based asymmetric self-play framework for RLVR post-training of LLMs. Co-evolves populations of LLMs with LoRA adapters, where different population members explore different reasoning strategies. Outperforms baseline on 3 code benchmarks and 7 math benchmarks. Even the weakest population member beats the baseline on aggregate.
- **Link:** [Semantic Scholar](https://www.semanticscholar.org/paper/) (2026)

---

## 2. LLM / VLM Game Agents & NPC AI

### Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with Large Language Models
- **Authors:** (NTU, Singapore)
- **Affiliation:** Nanyang Technological University
- **arXiv:** [2604.21896](https://arxiv.org/abs/2604.21896) (April 2026)
- **Key Innovation:** AI game programming framework integrating LLMs with Shannon's foundational concepts of game-playing machines. Uses LLM-based programming for AI game bots that interact with humans and adapt strategies through neuralized memoization (storing/refining strategies), trial-and-error learning with human feedback, and programmable prompt engineering via crowdsourcing. Demonstrates on tic-tac-toe, Nim, and Mancala. Bridges Shannon's vision of self-programming machines with LLMs for educational and creative game AI.
- **Link:** [arXiv 2604.21896](https://arxiv.org/abs/2604.21896)

### Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games
- **Authors:** Dongmin Park, Minkyu Kim, Beongjun Choi, Junhyuck Kim, et al.
- **Affiliation:** KRAFTON AI
- **Venue:** ICLR 2026
- **arXiv:** [2506.03610](https://arxiv.org/abs/2506.03610) (v3, updated)
- **Key Innovation:** Foundational benchmark spanning 12 video games across all major genres (Action, Adventure, RPG, Simulation, Strategy, Puzzle) with plug-and-play Model Context Protocol (MCP) interface. Releases fine-tuning dataset of expert LLM gameplay trajectories covering multiple genres, turning general LLMs into effective game agents. Provides game leaderboards, LLM battle arenas, and ablation studies on input modality, agentic strategies, and fine-tuning effects. First benchmark with both training data and multi-genre evaluation.
- **Link:** [arXiv 2506.03610](https://arxiv.org/abs/2506.03610) | [GitHub](https://github.com/krafton-ai/Orak)

### Combining Code Generating LLMs and Self-Play for Game Strategy Generation
- **Authors:** (IJCAI 2025)
- **Venue:** IJCAI 2025
- **Key Innovation:** Self-play approach for generating game-playing strategies represented as computer code. Uses LLMs to generate pieces of code ("generated bots") that play in multi-player games. Strategies evolve through self-play competition between code-generated agents.
- **Link:** [IJCAI 2025 PDF](https://www.ijcai.org/proceedings/2025/1249.pdf)

---

## 3. Game Foundation Models

### Towards Generalist Game Players: An Investigation of Foundation Models in the Game Multiverse
- **Authors:** Kuan Zhang, Dongchen Liu, Qiyue Zhao, Tianyu Xin, Yue Su, Haisheng Wang, Han Yin, Hongbo Ma, Peize Li, Tianjun Gu, Xiangnan Wu, Xinran Zhang, Yongxuan Li, Zirong Chen, Yiming Li
- **Affiliation:** Tsinghua University / MMLab HKU / UCAS
- **arXiv:** [2605.09965](https://arxiv.org/abs/2605.09965) (May 2026)
- **Key Innovation:** First systematic investigation of Large Foundation Models as generalist game players through end-to-end lifecycle. Proposes four-era evolution framework (Symbolic → Deep RL → Foundation Models → Demiurge), unifying Dataset, Model, Harness, and Benchmark as coupled closed loop under Goal-Conditioned POMDP formulation. Identifies five fundamental trade-offs and five-level roadmap toward generalist game player. Comprehensive analysis of 200+ papers covering datasets, models, harnesses, and benchmarks. Companion GitHub repo: Awesome-LFMs-Play-Games.
- **Link:** [arXiv 2605.09965](https://arxiv.org/abs/2605.09965) | [GitHub](https://github.com/THUSI-Lab/Awesome-LFMs-Play-Games)

### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors:** Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, et al.
- **Affiliation:** NVIDIA / MineDojo
- **Venue:** CVPR 2026
- **arXiv:** [2601.02427](https://arxiv.org/abs/2601.02427)
- **Key Innovation:** Open vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games. Internet-scale video-action dataset with auto-extracted input overlays. Gymnasium API wrapper for multi-game evaluation. Fine-tuning yields up to 52% relative improvement; single round of self-iteration boosts 2D metroidvania boss success from 18.7%→53.9%; three rounds →90.5%. Releases dataset, evaluation suite, and model weights.
- **Link:** [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Magne_NitroGen_An_Open_Foundation_Model_for_Generalist_Gaming_Agents_CVPR_2026_paper.html) | [GitHub](https://github.com/MineDojo/NitroGen)

### Scaling Behavior Cloning Improves Causal Reasoning: An Open Model for Real-Time Video Game Playing
- **Authors:** (January 2026)
- **arXiv:** [2601.04575](https://arxiv.org/abs/2601.04575)
- **Key Innovation:** Open recipe for training video game playing foundation model with 8,300+ hours of human gameplay data, 1.2B parameter decoder-only transformer. Systematic study of behavior cloning scaling laws: larger/deeper models achieve higher causality scores in data-abundant regimes, suggesting scaling is one approach to causality in behavior cloning. Real-time inference (20 Hz) on consumer GPU.
- **Link:** [arXiv 2601.04575](https://arxiv.org/abs/2601.04575) | [GitHub](https://github.com/elefant-ai/open-p2p)

---

## 4. World Models for Games

### Dreamer 4: Training Agents Inside of Scalable World Models
- **Authors:** Danijar Hafner et al.
- **Affiliation:** Google DeepMind
- **arXiv:** [2509.24527](https://arxiv.org/abs/2509.24527) (September 2025)
- **Key Innovation:** Scalable agent learning control tasks by RL inside a fast and accurate world model. World model accurately predicts object interactions and game mechanics in Minecraft, outperforming previous world models by large margin. Achieves real-time interactive inference on a single GPU through shortcut forcing objective and efficient transformer architecture. Learns general action conditioning from small amount of data, extracting majority of knowledge from diverse unlabeled videos. First agent to obtain diamonds in Minecraft purely from offline data (no environment interaction), requiring sequences of 20,000+ mouse and keyboard actions from raw pixels.
- **Link:** [arXiv 2509.24527](https://arxiv.org/abs/2509.24527) | [Project](https://danijar.com/dreamer4/)

### MineWorld: A Real-Time and Open-Source Interactive World Model on Minecraft
- **Authors:** Junliang Guo, Yang Ye, Tianyu He, Haoyu Wu, Yushu Jiang, Tim Pearce, Jiang Bian
- **Affiliation:** Microsoft Research Asia
- **arXiv:** [2504.08388](https://arxiv.org/abs/2504.08388) (April 2025)
- **Key Innovation:** Real-time interactive world model for Minecraft driven by visual-action autoregressive Transformer. Takes paired game scenes and actions as input, generates new scenes following actions. Visual game scenes and actions tokenized into discrete token ids (separate image and action tokenizers), concatenated as interleaved input. Open-source and reproducible.
- **Link:** [arXiv 2504.08388](https://arxiv.org/abs/2504.08388)

### JOWA: Scaling Offline Model-Based RL via Jointly-Optimized World-Action Model Pretraining
- **Authors:** Jie Cheng, Ruixi Qiao, ma yingwei, Binhua Li, Gang Xiong, Qinghai Miao, Yongbin Li, Yisheng Lv
- **Venue:** ICLR 2025 (Poster)
- **Key Innovation:** Jointly-Optimized World-Action model pretrained on multiple Atari games with 6 billion tokens of offline data. Joint optimization through shared transformer backbone stabilizes TD learning during pretraining. Proposes provably efficient parallelizable planning algorithm to compensate for Q-value estimation error. Largest agent (150M params) achieves 78.9% human-level performance on pretrained games using only 10% subsampled offline data, outperforming existing large-scale offline RL baselines by 31.6% on average.
- **Link:** [ICLR 2025](https://openreview.net/forum?id=T1OvCSFaum)

### Improving Transformer World Models for Data-Efficient RL
- **Authors:** (February 2025)
- **arXiv:** [2502.01591](https://arxiv.org/abs/2502.01591)
- **Key Innovation:** New MBRL algorithm achieving state-of-the-art on Craftax-classic benchmark (open-world 2D survival game). Policy architecture combining CNNs and RNNs with Dyna with Warmup, nearest neighbor tokenization, and block teacher forcing. Achieves reward of 69 (67.42% after 1M steps), outperforming previous methods and human performance on this challenging benchmark requiring generalization, exploration, and long-term reasoning.
- **Link:** [arXiv 2502.01591](https://arxiv.org/abs/2502.01591)

---

## 5. Procedural Content Generation (PCG)

### PCGRLLM: Large Language Model-Driven Reward Design for Procedural Content Generation Reinforcement Learning
- **Authors:** (February 2025)
- **arXiv:** [2502.10906](https://arxiv.org/abs/2502.10906)
- **Key Innovation:** Feedback-based reward generation framework using LLMs for PCGRL. Reasoning-based prompt engineering (ToT, GoT) for reward space exploration. Self-alignment and feedback loop: LLM generates reward function → PCGRL trains agent → LLM evaluates content and refines reward. 415.5% improvement over zero-shot generation. Tested with two LLMs across four scenarios including two-dimensional level generation tasks.
- **Link:** [arXiv 2502.10906](https://arxiv.org/abs/2502.10906)

### IPCGRL: Language-Instructed Reinforcement Learning for Procedural Level Generation
- **Authors:** I.-C. Baek, S.-H. Kim, S.-Y. Lee, D.-H. Kim, K.-J. Kim
- **Venue:** IEEE Conference on Games (CoG) 2025
- **arXiv:** [2503.12358](https://arxiv.org/abs/2503.12358) (v4, updated)
- **Key Innovation:** Instruction-based PCG via RL incorporating sentence embedding model. Fine-tunes task-specific embedding representations to effectively compress game-level conditions. Achieves up to 21.4% improvement in controllability and 17.2% improvement in generalizability for unseen instructions compared to general-purpose embedding methods.
- **Link:** [arXiv 2503.12358](https://arxiv.org/abs/2503.12358)

### Procedural Content Generation in Games: A Survey with Insights on Emerging LLM Integration
- **Authors:** Mahdi Farrokhi Maleki, Richard Zhao
- **Affiliation:** University of Calgary
- **arXiv:** [2410.15644](https://arxiv.org/abs/2410.15644) (Updated October 2024)
- **Key Innovation:** Comprehensive survey categorizing PCG algorithms and content types while highlighting LLMs as disruptive force since 2023. Covers combined algorithmic methods and identifies key gaps. Emphasizes growing use of LLMs for game content generation across levels, textures, quests, and dialogue.
- **Link:** [arXiv 2410.15644](https://arxiv.org/abs/2410.15644)

---

## 6. Game Benchmarks & Evaluation

### CausalGame: Benchmarking Causal Thinking of LLM Agents in Games
- **Authors:** (July 2026)
- **arXiv:** [2607.04293](https://arxiv.org/abs/2607.04293)
- **Key Innovation:** Novel benchmark with 14 interactive scenarios testing LLM agents' causal thinking through active experimental protocol design, data collection, and explanation reports. Incorporates selection bias, measurement error, and hidden confounders from real-world scientific discovery. Across 30 LLM agents, none demonstrates reliable causal thinking: best model reaches only 68.0% survival against analytical optima of 78-85%, and merely 5-7% of sessions receive credits on causal-reasoning rubrics. Provides scalable testbed for evaluating AI Scientist agents.
- **Link:** [arXiv 2607.04293](https://arxiv.org/abs/2607.04293)

### OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics
- **Authors:** Mingxian Lin, Shengju Qian, Yuqi Liu, Yi-Hua Huang, Yiyu Wang, Wei Huang, Yitang Li, Fan Zhang, Zeyu Hu, Lingting Zhu
- **arXiv:** [2606.09826](https://arxiv.org/abs/2606.09826) (June 2026)
- **Key Innovation:** First unified benchmark built on Unreal Engine 5 with standardized action interface (joystick-like inputs for all agents) across 12 games (7 solo, 3 PvP, 2 coop). Introduces Improvement Dynamics Curve (IDC)—multi-round reflection harness measuring initial score, slope (learning rate), and asymptotic plateau. Bounded skill prompts (≤500 tokens) encode strategy per episode. Held-out variants test generalization vs memorization. Evaluates 12 agents across commercial VLMs (GPT-4V, Gemini) and open-weight VLMs (LLaVA, Qwen-VL).
- **Link:** [arXiv 2606.09826](https://arxiv.org/abs/2606.09826)

### GameDevBench: Evaluating Agentic Capabilities Through Game Development
- **Authors:** Wayne Chi, Yixiong Fang, Arnav Yayavaram, Siddharth Yayavaram, Seth Karten, Qiuhong Anna Wei, Runkun Chen, Alexander Wang, Valerie Chen, Ameet Talwalkar, Chris Donahue
- **arXiv:** [2602.11103](https://arxiv.org/abs/2602.11103) (February 2026, v2 updated June 2026)
- **Key Innovation:** First benchmark for evaluating agents on game development tasks (333 tasks from web/video tutorials). Tasks require deep multimodal understanding—manipulating shaders, sprites, animations within visual game scenes. Average solution requires 3× more lines of code and file changes than prior software development benchmarks. Best agent solves only 53.8% of tasks. Strong correlation between perceived difficulty and multimodal complexity (51.4% gameplay vs 33.0% 2D graphics). Two simple image/video-based feedback mechanisms consistently improve performance.
- **Link:** [arXiv 2602.11103](https://arxiv.org/abs/2602.11103)

### GAMEBoT: Transparent Assessment of LLM Reasoning in Games
- **Authors:** (2025-2026)
- **Key Innovation:** Benchmark evaluating LLM reasoning in competitive gaming environments. Decomposes complex game reasoning into modular subproblems targeting rule understanding, strategy instruction following, and decision-making abilities. Provides transparent assessment beyond single aggregate scores.
- **Link:** [Project Page](https://visual-ai.github.io/gamebot/)

### A Survey on Large Language Model-Based Game Agents
- **Authors:** Sihao Hu et al.
- **Affiliation:** (Multiple institutions)
- **arXiv:** [2404.02039](https://arxiv.org/abs/2404.02039) (v5, updated June 2026)
- **Key Innovation:** Comprehensive survey on LLM-based game agents covering architectures, benchmarks, and applications. Updated through 2026 with latest developments including multimodal game agents, tool-augmented reasoning, and production deployment patterns.
- **Link:** [arXiv 2404.02039](https://arxiv.org/abs/2404.02039)

---

## 7. Industry Game AI

### NVIDIA ACE Game Agent SDK: On-Device AI for Autonomous Game Characters
- **Affiliation:** NVIDIA
- **Venue:** Unreal Fest 2026 (June 16, 2026 release)
- **Key Innovation:** Beta C/C++ framework enabling on-device AI-driven NPCs running on player's RTX GPU (no cloud dependency). Three core APIs: Agent API (manages chat history, drives multi-step reasoning), Chat API (direct inference control), RAG API (retrieval-augmented generation from game data tables). Successfully tested in Total War: PHARAOH (advisors accessing 1,200+ game data tables). Real-time inference using Small Language Models (SLMs) optimized for games—responding in tens of milliseconds. In-Game Inferencing (NVIGI) SDK provides GPU-optimized plugin-based inference manager with compute-in-graphics (CIG) technology.
- **Link:** [NVIDIA Developer](https://developer.nvidia.com/ace/get-started/)

### KRAFTON: NVIDIA ACE Autonomous Characters in Live Games (PUBG Ally, inZOI Smart Zoi)
- **Affiliation:** KRAFTON (PUBG developer)
- **Venue:** GDC 2026 / CES 2026 (demonstrated)
- **Key Innovation:** First large-scale deployment of ACE-powered Co-Playable Characters (CPCs) in live games. PUBG Ally uses Mistral-Nemo-Minitron-8B-128k-instruct for real-time strategic recommendations, loot sharing, vehicle driving, and combat. inZOI Smart Zoi enables NPC social behavior—extended conversations, memory of previous interactions, opinion formation based on observed behavior. NARAKA: BLADEPOINT AI teammates also powered by ACE. Open beta for PUBG Ally imminent.
- **Link:** [NVIDIA News](https://www.nvidia.com/en-us/geforce/news/nvidia-ace-autonomous-ai-companions-pubg-naraka-bladepoint/)

### Real-Time AI Inference Patterns from the Gaming Industry (INFUSE Engine)
- **Affiliation:** Jam and Tea Studio
- **Key Innovation:** Production inference engine (INFUSE) sitting alongside Unreal Engine for adaptive narrative and behavioral logic in real time. Architecture centered on Actors (local NPC-level reasoning) and Directors (global world-level coherence/pacing). Stateless inference calls—entire world state slice included per call (20-40K tokens inbound, ~100 tokens outbound). 1-2 second inference cycles with async queuing, dedicated cloud GPUs. Post-processing guardrails sanitize LLM outputs and apply deterministic correction when NPCs attempt impossible actions. Moved to self-hosted open-weight models for cost efficiency.
- **Link:** [Blog Post](https://cjlludwig.github.io/blog/real-time-ai-inference-patterns-gaming)

---

## 8. Related Techniques

### CDE: Curiosity-Driven Exploration for Efficient Reinforcement Learning in Large Language Models
- **Authors:** (September 2025)
- **arXiv:** [2509.09675](https://arxiv.org/abs/2509.09675)
- **Key Innovation:** Framework leveraging model's own intrinsic sense of curiosity to guide exploration during RLVR, addressing premature convergence and entropy collapse. Shows counting-based exploration using response embeddings is ineffective for LLM RL; proposes curiosity-driven exploration as alternative that outperforms baselines on reasoning tasks.
- **Link:** [arXiv 2509.09675](https://arxiv.org/abs/2509.09675)

### Curiosity-Driven Exploration in RL: An Adaptive Self-Supervised Learning Approach for Playing Action Games
- **Authors:** Seher Shahzad Farooq, Hameedur Rahman, Samiya Abdul Wahid, Muhammad Alyan Ansari, Saira Abdul Wahid, Hosu Lee
- **Venue:** Computers (MDPI), 14(10):434 (October 2025)
- **Key Innovation:** Integration of Intrinsic Curiosity Module (ICM) with Asynchronous Advantage Actor-Critic (A3C) for action games. Self-supervised curiosity signal drives exploration in sparse-reward environments. State-of-the-art results in complex scenarios like Deathmatch. Demonstrates significant advancement in agents' adaptability and performance within action gaming environments.
- **Link:** [MDPI](https://www.mdpi.com/2073-431X/14/10/434)

### Procedural Content Generation via Generative AI: A 2026 Overview
- **Affiliation:** (Multiple institutions, Japan)
- **Key Innovation:** Survey covering PCG via generative AI including GANs, VAEs, diffusion models, and LLMs for game content. Categorizes approaches by content type (levels, textures, music, dialogue) and generation method. Identifies emerging trends in combining multiple generative models for coherent multi-modal game content.
- **Link:** [J-STAGE](https://www.jstage.jst.go.jp/article/iis/advpub/0/advpub_2026.R.01/_pdf)

---

## Key Themes & Trends

1. **Self-Play for LLM Reasoning Matures:** SPIRAL (ICLR 2026) demonstrates self-play on zero-sum games produces transferable reasoning gains (+10% across 8 benchmarks). PopuLoRA extends this to population-based LoRA evolution. The survey on self-play methods (updated v3) provides comprehensive taxonomy of 4 algorithm families.

2. **Foundation Models as Generalist Game Players:** Tsinghua's comprehensive survey (arXiv:2605.09965) proposes four-era evolution framework and five-level roadmap. NitroGen (CVPR 2026) achieves 90.5% boss success on 1000+ games. Scaling BC (1.2B params, 8300+ hrs) shows scaling improves causal reasoning in behavior cloning.

3. **World Models Hit Real-Time:** Dreamer 4 (DeepMind) achieves first offline diamond collection in Minecraft from 20,000+ action sequences. MineWorld (Microsoft) enables real-time interactive Minecraft at scale. JOWA (ICLR 2025) demonstrates 150M jointly-optimized world-action models at 78.9% human-level on Atari with 10% offline data.

4. **Game Benchmarks Explode:** CausalGame introduces causal thinking benchmarks for AI Scientists; OmniGameArena provides UE5-based improvement dynamics curves; GameDevBench tests multimodal game development agents; GAMEBoT decomposes game reasoning into modular subproblems.

5. **On-Device Game AI Reaches Production:** NVIDIA ACE Game Agent SDK (June 2026) enables on-device SLM inference for NPCs. KRAFTON deploys ACE in PUBG Ally and inZOI Smart Zoi—first large-scale live deployment. INFUSE engine demonstrates 1-2s inference cycles with stateless calls.

6. **PCG + LLM Integration Deepens:** PCGRLLM achieves 415% improvement via LLM-driven reward design. IPCGRL enables language-instructed level generation with 21.4% controllability improvement. Survey confirms LLMs as disruptive force in PCG since 2023.

7. **Curiosity-Driven Exploration for LLMs:** CDE applies intrinsic curiosity to RLVR, addressing premature convergence. Traditional curiosity (ICM+A3C) continues advancing in action games with state-of-the-art Deathmatch results.

---

*Next digest: Continue monitoring arXiv cs.AI, cs.GT, cs.LG, cs.CV for new Game RL and Game AI papers.*
