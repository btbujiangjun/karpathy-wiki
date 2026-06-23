---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-06-23)"
type: synthesis
created: 2026-06-23
updated: 2026-06-23
sources: []
tags: [game-rl, game-ai, reinforcement-learning, llm-agents, foundation-models, pcg, benchmarks, self-play, world-models, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest

> Coverage: arXiv, ICLR 2026, ICML 2026, CVPR 2026 proceedings. Searched 2026-06-23.

## 1. Game RL — Reinforcement Learning in Games

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning
- **Authors**: Bo Liu et al.
- **Affiliation**: Multiple institutions
- **Venue**: ICLR 2026 (Poster)
- **Abstract**: Introduces SPIRAL, a self-play framework where LLMs learn by playing multi-turn, zero-sum games against continuously improving versions of themselves. Proposes role-conditioned advantage estimation (RAE) to stabilize multi-agent training. Improves reasoning benchmarks by up to 10% across Qwen and Llama families, outperforming SFT on 25,000 expert trajectories. Multi-game training (TicTacToe, Kuhn Poker, Simple Negotiation) yields strongest results. Even DeepSeek-R1-Distill-Qwen-7B benefits.
- **Key innovation**: Self-play + RAEs for LLM reasoning; automatic curriculum via stronger opponents; no human supervision needed.
- **Links**: [arXiv:2506.24119](https://arxiv.org/abs/2506.24119) | [GitHub](https://github.com/spiral-rl/spiral)

### Game-RL: Synthesizing Multimodal Verifiable Game Data to Boost VLMs' General Reasoning
- **Authors**: Jingqi Tong, Jixin Tang, Hangcheng Li, Yurong Mou, Ming Zhang, Jun Zhao, Yanbo Wen, Fan Song et al.
- **Affiliation**: Fudan University, Shanghai Innovation Institute, Shanghai AI Lab, SUSTech
- **Venue**: ICLR 2026 (Poster)
- **Abstract**: Proposes Game-RL, constructing diverse game tasks for RL training to boost VLMs' general reasoning. Introduces Code2Logic, a novel approach adapting game code to synthesize reasoning data with unlimited examples and controllable difficulty. Obtains GameQA dataset (30 games, 158 verifiable tasks). RL training solely on GameQA improves multiple VLMs across 7 out-of-domain vision-language benchmarks. Scaling game diversity/data volume consistently improves generalization.
- **Key innovation**: Code2Logic pipeline; game code → RL training data; verifiable multimodal rewards; out-of-domain transfer.
- **Links**: [arXiv:2505.13886](https://arxiv.org/abs/2505.13886) | [GitHub](https://github.com/tongjingqi/Game-RL)

### Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games
- **Authors**: Yidong He, Yutao Lai, Pengxu Yang, Jiarui Gan, Jiexin Wang, Yi Cai, Mengchen Zhao
- **Affiliation**: South China University of Technology, University of Oxford
- **Venue**: ICML 2026
- **Abstract**: Novel RL-based framework improving LLMs' strategic reasoning in multi-agent games. Introduces recursive reasoning paradigm where agent's reasoning integrates other agents' reasoning processes. Uses centralized CoT comparison module for intermediate reward signals. Computes hybrid advantage with group-relative RL. Achieves 22.1% average improvement across various multi-agent games.
- **Key innovation**: Recursive opponent modeling in reasoning; CoT comparison for intermediate rewards; group-relative RL for multi-agent LLMs.
- **Links**: [arXiv:2605.04906](https://arxiv.org/abs/2605.04906) | [GitHub](https://github.com/ydhe1012/Strat-Reasoner)

### GROW: Aligning GRPO with State-Action Modeling for Open-World VLM Agents
- **Authors**: Multiple
- **Affiliation**: Multiple institutions
- **Venue**: arXiv 2026/05
- **Abstract**: Aligns GRPO with state-action modeling for open-world VLM agents in Minecraft. Bridges the gap between RL training and embodied gameplay.
- **Key innovation**: State-action modeling for GRPO in open-world environments.
- **Links**: [arXiv:2605.20246](https://arxiv.org/abs/2605.20246)

### SkillGraph: Skill-Augmented Reinforcement Learning for Agents via Evolving Skill Graphs
- **Authors**: Multiple
- **Affiliation**: Multiple institutions
- **Venue**: arXiv 2026/05
- **Abstract**: Proposes SkillGraph, a method that augments RL with evolving skill graphs for hierarchical task decomposition in game-like environments.
- **Key innovation**: Dynamic skill graph construction for hierarchical RL.
- **Links**: [arXiv:2605.27899v1](https://arxiv.org/abs/2605.27899)

### Reinforcement Learning in Strategy-Based and Atari Games: A Review of Google DeepMind's Innovations
- **Authors**: Abdelrhman Shaheen, Anas Badr, Ali Abohendy, Hatem Alsaadawy, Nadine Alsayad, Ehab H. El-Shazly
- **Affiliation**: Multiple institutions
- **Venue**: arXiv (updated Feb 2026)
- **Abstract**: Comprehensive review of DeepMind's RL innovations in gaming: AlphaGo, AlphaGo Zero, MuZero, MiniZero. Covers model-based, model-free, and DQN approaches across Atari and strategy games.
- **Key innovation**: Survey covering AlphaGo → MuZero → MiniZero trajectory; multi-agent models.
- **Links**: [arXiv:2502.10303](https://arxiv.org/abs/2502.10303)

## 2. Game AI Bot — LLM-Powered Game Agents

### lmgame-Bench: How Good are LLMs at Playing Games?
- **Authors**: Lanxiang Hu, Mingjia Huo, Yuxuan Zhang, Haoyang Yu, Eric P. Xing, Ion Stoica, Tajana Rosing, Haojian Jin, Hao Zhang
- **Affiliation**: UC Berkeley, CMU, etc.
- **Venue**: ICLR 2026
- **Abstract**: First agentic benchmark for evaluating LLMs on games with gaming harness support. Studies three major challenges: brittle vision perception, prompt sensitivity, and data contamination. Gaming harness composed of agentic modules better distinguishes SOTA models. Evaluates on diverse video games including Sokoban, 2048, Tetris, Candy Crush.
- **Key innovation**: Gaming harness architecture; standardized LLM gaming evaluation; computer-use gaming agents.
- **Links**: [arXiv:2505.15146](https://arxiv.org/abs/2505.15146) | [GitHub](https://github.com/lmgame-org/GamingAgent)

### Ratchet: A Minimal Hygiene Recipe for Self-Evolving LLM Agents
- **Authors**: Multiple
- **Affiliation**: Multiple institutions
- **Venue**: arXiv 2026/05
- **Abstract**: Proposes Ratchet, a minimal recipe for self-evolving LLM agents that iteratively improve through experience replay and self-correction, evaluated in Minecraft.
- **Key innovation**: Minimal self-evolution loop with hygiene practices.
- **Links**: [arXiv:2605.22148](https://arxiv.org/abs/2605.22148)

### Experience Transfer for Multimodal LLM Agents in Minecraft Game
- **Authors**: Multiple
- **Affiliation**: Multiple institutions
- **Venue**: arXiv 2026/04
- **Abstract**: Studies cross-task experience transfer for multimodal LLM agents in Minecraft, enabling agents to leverage knowledge from prior tasks.
- **Links**: [arXiv:2604.05533](https://arxiv.org/abs/2604.05533)

### Gated Coordination for Efficient Multi-Agent Collaboration in Minecraft Game
- **Authors**: Multiple
- **Affiliation**: Multiple institutions
- **Venue**: arXiv 2026/04
- **Abstract**: Proposes gated coordination mechanism for efficient multi-agent collaboration in Minecraft, where agents dynamically decide when to coordinate.
- **Links**: [arXiv:2604.18975](https://arxiv.org/abs/2604.18975)

### MineNPC-Task: Task Suite for Memory-Aware Minecraft Agents
- **Authors**: Multiple
- **Affiliation**: Multiple institutions
- **Venue**: arXiv 2026/01
- **Abstract**: Suite of tasks designed to evaluate memory capabilities of LLM agents in Minecraft, requiring agents to remember past events across sessions.
- **Links**: [arXiv:2601.05215](https://arxiv.org/abs/2601.05215)

## 3. Game Foundation Models

### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi Fan
- **Affiliation**: NVIDIA, Stanford, Caltech, UChicago, UT Austin
- **Venue**: CVPR 2026
- **Abstract**: Vision-action foundation model trained on 40,000 hours of gameplay videos across 1,000+ games. Three key ingredients: (1) internet-scale video-action dataset from public gameplay videos with automatic action extraction, (2) multi-game benchmark environment for cross-game generalization, (3) unified vision-action model via large-scale behavior cloning. Achieves 52% relative improvement in task success on unseen games after fine-tuning. Released as open-source.
- **Key innovation**: Automatic gamepad overlay extraction (R²=0.84 joystick, 96% button accuracy); Gymnasium API wrapper for commercial games; largest open game-playing dataset.
- **Links**: [arXiv:2601.02427](https://arxiv.org/abs/2601.02427) | [Project](https://nitrogen.minedojo.org) | [HF Model](https://huggingface.co/nvidia/NitroGen)

### Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents
- **Authors**: ByteDance Seed Team
- **Affiliation**: ByteDance
- **Venue**: Technical report 2025/10
- **Abstract**: Next-generation generalist game agent integrating visual perception, strategic reasoning, action grounding, and long-term memory within a single VLM. Uses universal human-aligned action space (keyboard + mouse). Focuses on building foundation model for generalist game-playing and broader computer use.
- **Key innovation**: Unified VLM for end-to-end autonomous gameplay; no game-specific code or scripted behaviors; human-like perception-reasoning-action loop.
- **Links**: [Project Page](https://seed-tars.com/game-tars)

### Towards Generalist Game Players: An Investigation of Foundation Models in the Game Multiverse
- **Authors**: Kuan Zhang, Dongchen Liu, Qiyue Zhao, Tianyu Xin, Yue Su et al.
- **Affiliation**: THUSI Lab
- **Venue**: arXiv 2026/05
- **Abstract**: Comprehensive survey of foundation models as generalist game players across datasets, models, harnesses, and benchmarks. Systematic taxonomy of game-playing foundation models.
- **Key innovation**: Unified survey of game foundation model landscape.
- **Links**: [arXiv:2605.09965](https://arxiv.org/abs/2605.09965) | [GitHub](https://github.com/THUSI-Lab/Awesome-LFMs-Play-Games)

### GameGen-Verifier: Parallel Keypoint-Based Verification for LLM-Generated Games via Runtime State Injection
- **Authors**: Chaobo Jia, Ruipeng Wan, Ting Sun, Weihao Tan, Borui Wan, Yuxuan Tong, Guangming Sheng, Hong Xu
- **Venue**: arXiv 2026/05
- **Abstract**: Verification framework for LLM-generated games using parallel keypoint-based verification with runtime state injection.
- **Links**: [arXiv:2605.07442](https://arxiv.org/abs/2605.07442)

## 4. Procedural Content Generation

### PCGRLLM: Large Language Model-Driven Reward Design for Procedural Content Generation Reinforcement Learning
- **Authors**: In-Chang Baek, Sung-Hyun Kim, Sam Earle, Zehua Jiang, Noh Jin-Ha, Julian Togelius, Kyung-Joong Kim
- **Affiliation**: NYU, Multiple Korean institutions
- **Venue**: arXiv 2025/02
- **Abstract**: Addresses reward design bottleneck in PCGRL. Uses LLM with feedback loop and reasoning-based prompt engineering (ToT/GoT) to autonomously generate and refine reward functions. Achieves up to 415% improvement in reward-generation accuracy. Demonstrates generalization across LLMs from zero-shot to few-shot.
- **Key innovation**: LLM-driven reward design for RL-based level generators; self-alignment with environment feedback.
- **Links**: [arXiv:2502.10906](https://arxiv.org/abs/2502.10906)

### Procedural Content Generation in Games: A Survey with Insights on Emerging LLM Integration
- **Authors**: Mahdi Farrokhi Maleki, Richard Zhao
- **Affiliation**: University of Calgary / NYU
- **Venue**: arXiv 2024/10 (updated)
- **Abstract**: Comprehensive survey of PCG methods including search-based, ML-based, noise functions, and LLM-based approaches. Compares methods by content type and publication date. Identifies gaps in LLM integration for PCG.
- **Key innovation**: Taxonomy of LLM-integrated PCG methods; combined methods analysis.
- **Links**: [arXiv:2410.15644](https://arxiv.org/abs/2410.15644)

## 5. Game Benchmarks

### Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games
- **Authors**: Dongmin Park et al.
- **Affiliation**: KRAFTON AI
- **Venue**: arXiv 2026 (updated Apr 2026)
- **Abstract**: Benchmark for LLM agents across 12 popular video games spanning 6 major genres (action, adventure, RPG, simulation, strategy, puzzle). Uses plug-and-play MCP interface. Releases fine-tuning dataset of expert LLM gameplay trajectories. Evaluates input modality, agentic strategies, and fine-tuning effects. Games include Street Fighter III, Super Mario, Ace Attorney, Pokémon Red, StarCraft II, Minecraft, etc.
- **Key innovation**: Full genre coverage; MCP-based plug-and-play interface; expert trajectory fine-tuning dataset.
- **Links**: [arXiv:2506.03610](https://arxiv.org/abs/2506.03610) | [GitHub](https://github.com/krafton-ai/Orak) | [HF Dataset](https://huggingface.co/datasets/KRAFTON/Orak)

### BALROG: Benchmarking Agentic LLM and VLM Reasoning On Games
- **Authors**: Paglieri et al.
- **Venue**: NeurIPS 2024 / ongoing
- **Abstract**: Evaluates agentic LLM/VLM capabilities through six diverse game environments. Tests reasoning, planning, and interaction abilities in game-based settings.
- **Links**: [Paper](https://arxiv.org/abs/2411.13535)

### TowerMind: A Tower Defence Game Learning Environment and Benchmark for LLM as Agents
- **Authors**: Multiple
- **Venue**: arXiv 2026/01
- **Abstract**: Introduces tower defense game environment for evaluating LLM agent planning and decision-making with low computational demands, multimodal observation, and hallucination assessment support.
- **Links**: [arXiv:2601.05899](https://arxiv.org/abs/2601.05899)

### DSGBench: A Strategic Game Benchmark for LLM Agents
- **Authors**: Tang et al.
- **Venue**: arXiv 2025/12
- **Abstract**: Validates LLMs on 6 strategic games including Avalon, Resistance, and Werewolf, testing deception, negotiation, and coalition formation.
- **Links**: Search arXiv for DSGBench

## 6. Industry Game AI

### Game-TARS (ByteDance)
See Section 3. ByteDance's production-ready generalist game agent using unified VLM architecture.

### Orak (KRAFTON)
See Section 5. KRAFTON's 12-game benchmark with fine-tuning dataset.

### Synergizing Code Coverage and Gameplay Intent: Coverage-Aware Game Playtesting with LLM-Guided Reinforcement Learning
- **Authors**: Multiple
- **Affiliation**: Multiple
- **Venue**: arXiv 2025/12
- **Abstract**: Combines LLM guidance with RL for automated game playtesting, using code coverage and gameplay intent signals.
- **Links**: [arXiv:2512.12706](https://arxiv.org/abs/2512.12706)

## 7. Related Techniques

### Reinforcement World Model Learning for LLM-based Agents
- **Authors**: Xiao Yu, Baolin Peng, Ruize Xu, Yelong Shen, Pengcheng He, Suman Nath, Nikhil Singh, Jiangfeng Gao, Zhou Yu
- **Affiliation**: Microsoft Research, Columbia University
- **Venue**: arXiv 2026/02
- **Abstract**: Proposes RWML, a self-supervised method for learning action-conditioned world models for LLM agents using sim-to-real gap rewards. Aligns simulated next states with realized next states in pre-trained embedding space. Outperforms direct task-success RL by 6.9 and 5.7 points on ALFWorld and τ² Bench respectively.
- **Key innovation**: Sim-to-real gap reward for world model learning; more robust than next-token prediction; matches expert-data training performance.
- **Links**: [arXiv:2602.05842](https://arxiv.org/abs/2602.05842)

### Dreamer 4: Training Agents Purely Inside World Models
- **Authors**: Danijar Hafner et al.
- **Affiliation**: Google DeepMind
- **Venue**: arXiv 2025/10
- **Abstract**: First agent to obtain diamonds in Minecraft without practicing in the actual game at all. Learns world model from offline data, then improves behavior via RL in diverse imagined scenarios. Achieves over 20,000 consecutive mouse/keyboard actions for long-horizon tasks.
- **Key innovation**: Pure imagination-based training; world model generalization to complex 3D environments.
- **Links**: [arXiv:2509.24527](https://arxiv.org/abs/2509.24527)

### WoG (World Guidance): World Modeling in Condition Space for Action Generation
- **Authors**: Yue Su et al.
- **Affiliation**: ByteDance Seed, HKU, SJTU
- **Venue**: ICML 2026
- **Abstract**: Proposes world modeling paradigm in condition space for action generation. "Less is more" approach to world models.
- **Links**: [arXiv:2602.22010](https://arxiv.org/abs/2602.22010) | [GitHub](https://github.com/Selen-Suyue/WoG)

### SKILLC: Learning Autonomous Skill Internalization in LLM Agents via Contrastive Credit Assignment
- **Authors**: Multiple
- **Venue**: arXiv 2026/05
- **Abstract**: Contrastive credit assignment for skill internalization in LLM agents, enabling autonomous skill acquisition through interaction.
- **Links**: [arXiv:2605.27899](https://arxiv.org/abs/2605.27899)

### See, Symbolize, Act: Grounding VLMs with Spatial Representations for Better Gameplay
- **Authors**: Multiple
- **Venue**: arXiv 2026/03
- **Abstract**: Grounds VLMs with explicit spatial representations for improved gameplay performance.
- **Links**: [arXiv:2603.11601](https://arxiv.org/abs/2603.11601)

### Implicit Strategic Optimization: Rethinking Long-Horizon Decision-Making in Adversarial Poker Environments
- **Authors**: Multiple
- **Venue**: arXiv 2026/02
- **Abstract**: Rethinks long-horizon decision-making in adversarial poker environments using implicit strategic optimization.
- **Links**: [arXiv:2602.08041](https://arxiv.org/abs/2602.08041)

### Brain Alignment of Reasoning and Action Representations from Vision-Language and Action Models During Naturalistic Gameplay
- **Authors**: Multiple
- **Venue**: arXiv 2026/05
- **Abstract**: Studies brain alignment of VLM and action model representations during gameplay, connecting AI to neuroscience.
- **Links**: [arXiv:2605.19352](https://arxiv.org/abs/2605.19352)

### What and When to Distill: Selective Hindsight Distillation for Multi-Turn Agents
- **Authors**: Multiple
- **Venue**: arXiv 2026/05
- **Abstract**: Selective hindsight distillation method determining what and when to distill from past experiences for multi-turn game agents.
- **Links**: [arXiv:2605.19447](https://arxiv.org/abs/2605.19447)

## Key Themes & Takeaways

1. **Game → Reasoning Transfer**: Multiple papers (Game-RL, SPIRAL, Strat-Reasoner) demonstrate that RL training on games transfers to general reasoning benchmarks — games are emerging as a primary RLVR data source.
2. **Foundation Models for Games**: NitroGen (NVIDIA, CVPR 2026) and Game-TARS (ByteDance) represent a shift toward generalist game agents trained at scale, moving beyond single-game specialists.
3. **Self-Play for LLMs**: SPIRAL and Strat-Reasoner show self-play and multi-agent RL directly improve LLM reasoning, reducing dependence on human-curated data.
4. **Unified Benchmarks**: Orak (KRAFTON) and lmgame-Bench provide standardized evaluation across genres, with fine-tuning datasets to adapt LLMs into game agents.
5. **World Models in Games**: Dreamer 4 and RWML show training agents purely in imagination is becoming viable, even for complex games like Minecraft.
6. **PCG + LLMs**: PCGRLLM demonstrates LLMs can automate reward design for RL-based content generation, reducing human effort.
7. **Open Science**: NitroGen, Game-RL, Orak, and SPIRAL all release code, data, and weights — the game AI field is increasingly open.
