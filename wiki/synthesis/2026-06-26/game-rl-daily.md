---
title: 'Game RL & Game AI Bot — Daily Paper Digest'
type: synthesis
created: 2026-06-26
updated: 2026-06-26
sources: [arxiv-paper-check.md, conference-digest.md]
tags: [game-rl, game-ai, reinforcement-learning, game-bots, foundation-models, procedural-content-generation, self-play, daily]
---

# Game RL & Game AI Bot — Daily Paper Digest

> Comprehensive roundup of recent papers on Game RL, Game AI Bots, Game Foundation Models, Procedural Content Generation, Game Benchmarks, and related techniques. Searched arXiv, CVPR 2026, CoG 2025, ICLR 2026, ACM CSUR.

---

## 1. Multi-Agent RL in Games

### A Comprehensive Review of Multi-Agent Reinforcement Learning in Video Games
- **Authors:** Zhengyang Li, Qijin Ji, Xinghong Ling, Quan Liu
- **Affiliation:** — (academic)
- **Venue:** arXiv, Sep 2025
- **Abstract & Key Innovations:** Surveys MARL applications from turn-based two-agent games to real-time multi-agent video games including Sports, FPS, RTS, and MOBA genres. Covers landmark systems (AlphaStar, OpenAI Five, Honor of Kings). Analyzes challenges: nonstationarity, partial observability, sparse rewards, team coordination, scalability. Proposes a novel game complexity estimation method.
- **Link:** [arXiv:2509.03682](https://arxiv.org/abs/2509.03682)

### Reinforcement Learning in Strategy-Based and Atari Games: A Review of Google DeepMind's Innovations
- **Authors:** Abdelrhman Shaheen, Anas Badr, Ali Abohendy, Hatem Alsaadawy, Nadine Alsayad, Ehab H. El-Shazly
- **Affiliation:** Egypt-Japan University of Science and Technology (E-JUST)
- **Venue:** arXiv (v2 Feb 2026)
- **Abstract & Key Innovations:** Reviews DeepMind's AlphaGo, AlphaGo Zero, MuZero. Analyzes progression from supervised+RL hybrid to pure self-play to model-based RL without known rules. Discusses MiniZero, multi-agent extensions (AlphaStar). Highlights future directions for real-world RL deployment.
- **Link:** [arXiv:2502.10303](https://arxiv.org/abs/2502.10303)

---

## 2. LLM-Powered Game Agents & NPCs

### A Survey on Large Language Model-Based Game Agents
- **Authors:** (multiple, from Georgia Tech DISL)
- **Affiliation:** Georgia Institute of Technology (DISL Lab)
- **Venue:** ACM Computing Surveys (CSUR), Jun 2026
- **Abstract & Key Innovations:** Comprehensive survey of LLM-based game agents (LLMGAs). Proposes unified reference architecture with memory system, reasoning mechanism, perception & action interface. Introduces multi-LLMGA framework for population-level interaction. Maps 6 game genres to distinct agent design requirements. Covers 2022–2026 literature.
- **Link:** [arXiv:2404.02039](https://arxiv.org/abs/2404.02039)

### LLM-Driven NPCs: Cross-Platform Dialogue System for Games and Social Platforms
- **Authors:** Li Song
- **Affiliation:** — (prototype system)
- **Venue:** arXiv, Apr 2025
- **Abstract & Key Innovations:** Prototype LLM-powered NPCs communicating in both Unity game and Discord. Cloud database (LeanCloud) synchronizes memory across platforms. Initial experiments show cross-platform technical feasibility. Foundation for emotional modeling and persistent memory.
- **Link:** [arXiv:2504.13928](https://arxiv.org/abs/2504.13928)

### Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with Large Language Models
- **Authors:** Chee Wei Tan, Yuchen Wang, Shangxin Guo
- **Affiliation:** — (academic)
- **Venue:** arXiv, Apr 2026
- **Abstract & Key Innovations:** Extends Claude Shannon's game machine taxonomy with LLMs. Nemobot environment for creating LLM-powered game agents across 4 game classes: dictionary-based, rigorously solvable, heuristic-based, learning-based. Combines minimax, crowdsourced data, RLHF, self-critique for iterative strategy refinement.
- **Link:** [arXiv:2604.21896](https://arxiv.org/abs/2604.21896)

---

## 3. Game Foundation Models (Generalist Game Agents)

### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors:** Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi "Jim" Fan
- **Affiliation:** NVIDIA, Stanford, Caltech, UChicago, UT Austin
- **Venue:** CVPR 2026 (**Oral**, Best Paper Honorable Mention)
- **Abstract & Key Innovations:** Vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games. Three key ingredients: (1) internet-scale video-action dataset via automatic action extraction from overlay software, (2) multi-game benchmark environment for cross-game generalization, (3) unified vision-action model via large-scale behavior cloning. Achieves 52% relative improvement on unseen games. Open-source dataset, evaluation suite, weights.
- **Link:** [arXiv:2601.02427](https://arxiv.org/abs/2601.02427)

### Lumine: An Open Recipe for Building Generalist Agents in 3D Open Worlds
- **Authors:** Weihao Tan, Xiangyang Li, Yunhao Fang, Heyuan Yao, Shi Yan, Hao Luo, Tenglong Ao, Huihui Li, Hongbin Ren, Bairen Yi, Yujia Qin, Bo An, Libin Liu, Guang Shi
- **Affiliation:** ByteDance Seed
- **Venue:** arXiv, Nov 2025
- **Abstract & Key Innovations:** First open recipe for generalist agents completing hours-long 3D open-world missions in real time. VLM-powered: processes raw pixels at 5 Hz → 30 Hz keyboard-mouse actions. Trained on Genshin Impact (1,731h pretrain + 200h instruction + 15h reasoning). Completes 5h Mondstadt storyline on par with humans. Zero-shot generalization to Wuthering Waves (100min) and Honkai: Star Rail (5h chapter).
- **Link:** [arXiv:2511.08892](https://arxiv.org/abs/2511.08892)

### Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents
- **Authors:** Zihao Wang, Xujing Li, Yining Ye, Junjie Fang, Haoming Wang, Longxiang Liu, Shihao Liang, Junting Lu, Zhiyong Wu, Jiazhan Feng, Wanjun Zhong, Zili Li, Yu Wang, Yu Miao, Bo Zhou, Yuanfan Li, Hao Wang, Zhongkai Zhao, Faming Wu, Zhengxuan Jiang, Weihao Tan, Heyuan Yao, Shi Yan, Xiangyang Li, Yitao Liang, Yujia Qin, Guang Shi
- **Affiliation:** ByteDance Seed
- **Venue:** arXiv, Oct 2025
- **Abstract & Key Innovations:** Unified keyboard-mouse action space for cross-domain pre-training (OS, web, simulation games). Pre-trained on 500B+ tokens. Key techniques: decaying continual loss to reduce causal confusion, Sparse-Thinking strategy balancing reasoning depth and cost. 2× SOTA on Minecraft, near-fresh-human generality on unseen web 3D games, outperforms GPT-5/Gemini-2.5-Pro/Claude-4-Sonnet on FPS benchmarks.
- **Link:** [arXiv:2510.23691](https://arxiv.org/abs/2510.23691)

### GROW: Aligning GRPO with State-Action Modeling for Open-World VLM Agents
- **Authors:** Xiongbin Wu, Zhihao Luo, Shanzhe Lei, Lechao Zhang, Xuhong Wang, Jie Yang, Zhonglong Zheng, Yuanjie Zheng, Xin Tan, Wei Liu
- **Affiliation:** — (academic)
- **Venue:** arXiv, May 2026
- **Abstract & Key Innovations:** Adapts GRPO for VLM agents in open-world settings by decomposing long trajectories into state-action samples for efficient credit assignment. SOTA on 800+ Minecraft tasks (embodied, GUI, combat). Up to 29.3pp improvement on GUI tasks. Surrogate analysis proves core RL signal preserved under simplifying assumptions.
- **Link:** [arXiv:2605.20246](https://arxiv.org/abs/2605.20246)

### Towards Generalist Game Players: An Investigation of Foundation Models in the Game Multiverse
- **Authors:** (multiple)
- **Affiliation:** — (survey)
- **Venue:** arXiv, May 2026
- **Abstract & Key Innovations:** Comprehensive systematized study of LFMs (LLMs, VLMs, VLAs, WAMs) for generalist game-playing agents. Four pillars: Dataset, Model, Harness, Benchmark. Five fundamental trade-offs (reasoning vs reactivity, breadth vs depth, etc.). Roadmap through 5 developmental levels toward AGI-like generality. Covers NitroGen, OpenP2P and other recent systems.
- **Link:** [arXiv:2605.09965](https://arxiv.org/abs/2605.09965)

---

## 4. Procedural Content Generation

### IPCGRL: Language-Instructed Reinforcement Learning for Procedural Level Generation
- **Authors:** In-Chang Baek, Sung-Hyun Kim, Seo-Young Lee, Dong-Hyeon Kim, Kyung-Joong Kim
- **Affiliation:** — (academic)
- **Venue:** Conference on Games (CoG) 2025
- **Abstract & Key Innovations:** Instruction-based PCG via RL with sentence embedding model. Fine-tunes task-specific embeddings for game level conditions. Up to 21.4% improvement in controllability and 17.2% improvement in generalizability for unseen instructions on 2D level generation. Extends conditional input modality for flexible interaction.
- **Link:** [arXiv:2503.12358](https://arxiv.org/abs/2503.12358)

### PCGRLLM: Large Language Model-Driven Reward Design for Procedural Content Generation Reinforcement Learning
- **Authors:** In-Chang Baek, Sung-Hyun Kim, Sam Earle, Zehua Jiang, Noh Jin-Ha, Julian Togelius, Kyung-Joong Kim
- **Affiliation:** NYU Game Innovation Lab, — (academic)
- **Venue:** arXiv, Feb 2025
- **Abstract & Key Innovations:** Uses LLMs (via ToT/GoT reasoning) to autonomously generate and refine reward functions for PCGRL agents. Up to 415% improvement in reward-generation accuracy. Shows LLMs excel at spatial constraint rewards vs humans better at multi-objective trade-offs. Complementary human–LLM workflow for reward design.
- **Link:** [arXiv:2502.10906](https://arxiv.org/abs/2502.10906)

### MOPCGRL: Multi-Objective Procedural Content Generation via Reinforcement Learning
- **Authors:** (multiple)
- **Affiliation:** — (academic)
- **Venue:** Complex System Modeling and Simulation, IEEE, Mar 2026
- **Abstract & Key Innovations:** Multi-objective RL for training level generators that balance trade-offs between diversity metrics with playability constraints. Evaluated on Mario-AI benchmark. Increases generator distribution diversity while accelerating convergence. Enables researchers to tailor content to specific needs.
- **Link:** IEEE DOI: [10.23919/CSMS.2025.0034](https://doi.org/10.23919/CSMS.2025.0034)

### CrawLLM: An LLM-Based Pipeline for Game Asset Generation
- **Authors:** Marvin Zammit, Antonios Liapis, Georgios N. Yannakakis
- **Affiliation:** University of Malta / Institute of Digital Games
- **Venue:** IEEE Transactions on Games, 2026 (Early Access)
- **Abstract & Key Innovations:** LLM-driven pipeline for generating narrative, visual, and gameplay content coherently. Uses Mixtral 8x7B for themes, Stable Diffusion XL for visual assets. User study shows semantic themes remain clearly discernible. Demonstrates potential of LLM-driven pipelines for PCG.
- **Link:** (PDF available via NYU Game Lab)

---

## 5. Game Benchmarks & Agent Evaluation

### WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation
- **Authors:** Shuangrui Ding, Xuanlang Dai, Long Xing, Shengyuan Ding, Ziyu Liu, Yang JingYi, Penghui Yang, Zhixiong Zhang, Xilin Wei, Xinyu Fang, Yubo Ma, Haodong Duan, Jing Shao, Jiaqi Wang, Dahua Lin, Kai Chen, Yuhang Zang
- **Affiliation:** Shanghai AI Lab; CUHK; Fudan; USTC; SJTU; Tsinghua; NTU
- **Venue:** arXiv, May 2026
- **Abstract & Key Innovations:** 60 bilingual multimodal tasks averaging 8 min wall-clock time, 20+ tool calls. Native Docker runtime with real CLI harness (OpenClaw, Claude Code, Codex, Hermes Agent). Hybrid grading (rule-based + state auditing + LLM/VLM judge). Best model (Claude Opus 4.7) reaches only 62.2%. Not a game-specific benchmark but relevant for game agent tool-use evaluation.
- **Link:** [arXiv:2605.10912](https://arxiv.org/abs/2605.10912)

### GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents
- **Authors:** (multiple)
- **Affiliation:** — (academic)
- **Venue:** arXiv, Apr 2026
- **Abstract & Key Innovations:** Standardized evaluation suite for multimodal game agents. Provides verifiable metrics across diverse game environments. Addresses reproducibility challenges in game agent evaluation.
- **Link:** [arXiv:2604.07429](https://arxiv.org/abs/2604.07429)

### PokeGym: A Visually-Driven Long-Horizon Benchmark for Vision-Language Models
- **Authors:** (multiple)
- **Affiliation:** — (academic)
- **Venue:** arXiv, Apr 2026
- **Abstract & Key Innovations:** Long-horizon benchmark using Pokémon games for VLM evaluation. Visually-driven tasks requiring sustained reasoning and planning. Tests VLMs on game state understanding, strategy, and multi-step decision making.
- **Link:** [arXiv:2604.08340](https://arxiv.org/abs/2604.08340)

---

## 6. Self-Play RL & World Models for Games

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning
- **Authors:** Bo Liu, Leon Guertler, Simon Yu, Zichen Liu, Penghui Qi, Daniel Balcells, Mickel Liu, Cheston Tan, Weiyan Shi, Min Lin, Wee Sun Lee, Natasha Jaques
- **Affiliation:** — (academic/industry)
- **Venue:** arXiv (v3 Mar 2026)
- **Abstract & Key Innovations:** Self-play framework for LLMs using multi-turn zero-sum games (Kuhn Poker, TicTacToe, Simple Negotiation). Role-conditioned advantage estimation (RAE) for stable multi-agent training. Training on Kuhn Poker alone yields 8.6% math improvement, 8.4% general reasoning. Multi-game training yields strongest transfer. Up to 10% improvement across 8 reasoning benchmarks on Qwen/Llama families.
- **Link:** [arXiv:2506.24119](https://arxiv.org/abs/2506.24119)

### A Survey on Self-play Methods in Reinforcement Learning
- **Authors:** Ruize Zhang, Zelai Xu, Chengdong Ma, Chao Yu, Wei-Wei Tu, Wenhao Tang, Shiyu Huang, Deheng Ye, Wenbo Ding, Yaodong Yang, Yu Wang
- **Affiliation:** — (academic survey)
- **Venue:** arXiv (v4 Oct 2025)
- **Abstract & Key Innovations:** Comprehensive roadmap of self-play methods in MARL. Unified framework for classifying self-play algorithms. Covers Go, poker, video games. Bridges algorithms to practical implications in non-cooperative scenarios. Highlights open challenges.
- **Link:** [arXiv:2408.01072](https://arxiv.org/abs/2408.01072)

### Internalizing World Models via Self-Play Finetuning for Agentic RL
- **Authors:** Shiqi Chen, Jinghan Zhang et al.
- **Affiliation:** — (academic)
- **Venue:** ICLR 2026 (submitted)
- **Abstract & Key Innovations:** SPA framework: cold-starts policy via Self-Play SFT to learn world model (state representation + transition modeling), then simulates future states before policy optimization. Sokoban success rate 25.6%→59.8%, FrozenLake 22.1%→70.9% for Qwen2.5-1.5B.
- **Link:** [arXiv:2510.15047](https://arxiv.org/abs/2510.15047)

### SeRL: Self-Play Reinforcement Learning for Large Language Models with Limited Data
- **Authors:** Wenkai Fang, Shunyu Liu, Yang Zhou, Kongcheng Zhang, Tongya Zheng, Kaixuan Chen, Mingli Song, Dacheng Tao
- **Affiliation:** Zhejiang University, NTU Singapore
- **Venue:** arXiv, May 2025
- **Abstract & Key Innovations:** Self-play RL with self-instruction and self-rewarding modules for bootstrapping LLM training with limited initial data. Majority-voting mechanism estimates response rewards without external annotations. Matches performance of high-quality data with verifiable rewards on reasoning benchmarks.
- **Link:** [arXiv:2505.20347](https://arxiv.org/abs/2505.20347)

### SPEAR: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning
- **Authors:** Yulei Qin, Sheng Ye, Ke Li, Xing Sun et al.
- **Affiliation:** — (academic)
- **Venue:** arXiv, Sep 2025
- **Abstract & Key Innovations:** Curriculum-based self-imitation learning (SIL) for agentic LLMs on long-horizon, sparsely-rewarded tasks. Replay buffer stores self-generated promising trajectories. Intrinsic rewards foster skill-level exploration; SIL strengthens action-level exploration. Addresses entropy collapse and runaway divergence in multi-turn RL.
- **Link:** [arXiv:2509.22601](https://arxiv.org/abs/2509.22601)

---

## 7. Related Techniques: Curiosity, Hierarchical RL, Imitation Learning

### Curiosity-driven exploration based on hierarchical vision transformer for deep reinforcement learning with sparse rewards
- **Authors:** (multiple)
- **Affiliation:** — (academic)
- **Venue:** Neurocomputing, Jul 2025
- **Abstract & Key Innovations:** Proposes DiNAT-RCM curiosity model based on Dilated Neighborhood Attention Transformer for useful state features in sparse-reward RL. AW-A2C actor-critic with self-attention for precise action selection. Evaluated on Atari 2600 (Gym). Outperforms RND and LBS baselines.
- **Link:** [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0925231225009245)

### Structured Imitation Learning of Interactive Policies through Inverse Games
- **Authors:** Max M. Sun, Todd Murphey
- **Affiliation:** Northwestern University
- **Venue:** RSS 2025 Workshop on Generative Modeling Meets HRI
- **Abstract & Key Innovations:** Combines generative single-agent policy learning with game-theoretic structure for interactive policies. Two-step: (1) learn individual behavioral patterns via imitation learning, (2) learn inter-agent dependencies via inverse game problem. Comparable to ground truth on 5-agent social navigation with only 50 demos.
- **Link:** [arXiv:2511.12848](https://arxiv.org/abs/2511.12848)

### Hierarchical Frameworks for Scaling-up Multi-agent Coordination (HiSOMA, L2M2)
- **Authors:** Minghong Geng
- **Affiliation:** — (academic)
- **Venue:** AAMAS 2025 (Extended Abstract)
- **Abstract & Key Innovations:** HiSOMA: hierarchical framework integrating self-organizing networks with MARL for long-horizon planning. L2M2: LLMs for high-level planning in hierarchical multi-agent systems. MOSMAC benchmark for multi-objective MARL.
- **Link:** [AAMAS 2025](https://dl.acm.org/doi/10.5555/3709347.3744052)

### Learning to Plan, Planning to Learn: Adaptive Hierarchical RL-MPC for Sample-Efficient Decision Making
- **Authors:** Toshiaki Hori et al.
- **Affiliation:** — (academic)
- **Venue:** arXiv, Dec 2025
- **Abstract & Key Innovations:** Adaptive hierarchical RL-MPC framework combining model predictive control with hierarchical RL for sample-efficient decision making. Relevant for game environments requiring long-horizon planning and real-time control.
- **Link:** [arXiv:2512.17091](https://arxiv.org/abs/2512.17091)

---

## 8. Industry Game AI

> Notable industry contributions from major labs/studios:

| Lab | Paper/System | Focus |
|-----|-------------|-------|
| **NVIDIA** | NitroGen (CVPR 2026 Oral) | Open foundation model, generalist gaming agents, 40K hrs, 1K+ games |
| **ByteDance Seed** | Lumine (arXiv Nov 2025) | 3D open-world generalist agent, Genshin Impact |
| **ByteDance Seed** | Game-TARS (arXiv Oct 2025) | Unified keyboard-mouse agent, 500B tokens, outperforms GPT-5 on FPS |
| **NVIDIA** | GROW (arXiv May 2026) | GRPO for VLM agents, Minecraft SOTA |
| **NYU Game Innovation Lab** | PCGRLLM, IPCGRL (CoG 2025) | LLM reward design + RL for PCG |
| **CMU / OpenAI** | MineRL (IJCAI 2019, ongoing) | Minecraft RL dataset, BASALT competitions |

---

## Key Trends Observed

1. **Convergence of VLM + RL**: Game agents are increasingly VLM-driven with RL fine-tuning (GROW, SPIRAL). GRPO is emerging as a popular RL algorithm for game agents.
2. **Unified Action Spaces**: Game-TARS and NitroGen both advocate for simple, scalable keyboard-mouse action spaces over game-specific APIs.
3. **Self-Play for Reasoning**: Zero-sum games (Kuhn Poker, TicTacToe) are being used to train general reasoning in LLMs (SPIRAL).
4. **Open-World 3D Games as Testbeds**: Commercial games (Genshin Impact, Minecraft, Wuthering Waves) are becoming primary evaluation platforms.
5. **LLMs for PCG**: LLMs automate reward design (PCGRLLM), level generation (IPCGRL), and full game asset pipelines (CrawLLM).
6. **Open-source shifting**: NitroGen, Lumine, and Game-TARS all release weights, datasets, and evaluation suites.
