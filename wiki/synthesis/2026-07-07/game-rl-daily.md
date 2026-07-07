---
title: Game RL & Game AI Bot — arXiv & Proceedings Daily (2026-07-07)
type: synthesis
created: 2026-07-07
updated: 2026-07-07
sources: [arxiv]
tags: [game-rl, game-ai, self-play, game-foundation-models, game-agents, reinforcement-learning]
---

# Game RL & Game AI Bot — arXiv & Proceedings Daily

> 30+ curated papers across 7 topics. Coverage: arXiv / CVPR 2026 / ICLR 2026 / CoG 2026 / IEEE Trans. on Games / L4DC 2026.

---

## 1. Game RL — Self-Play & Multi-Agent RL

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning
- **Authors**: Bo Liu, Leon Guertler, Simon Yu, Zichen Liu, Penghui Qi, Daniel Balcells, Mickel Liu, Cheston Tan, Weiyan Shi, Min Lin, Wee Sun Lee, Natasha Jaques
- **Affiliation**: —
- **Venue**: ICLR 2026
- **Abstract**: Introduces SPIRAL, a self-play framework where LLMs learn by playing multi-turn zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation) against continuously improving versions of themselves. Proposes role-conditioned advantage estimation (RAE) to stabilize multi-agent training. Improves reasoning by up to 10% across 8 benchmarks on Qwen and Llama families. Multi-game training yields strongest results; even DeepSeek-R1-Distill-Qwen-7B benefits (+2%).
- **Link**: [arXiv:2506.24119](https://arxiv.org/abs/2506.24119) | [Code](https://github.com/spiral-rl/spiral)

### A Comprehensive Review of Multi-Agent Reinforcement Learning in Video Games
- **Authors**: Zhengyang Li, Qijin Ji, Xinghong Ling, Quan Liu
- **Affiliation**: —
- **Venue**: IEEE Transactions on Games (Vol. 17, Issue 4, Dec 2025)
- **Abstract**: Thorough examination of MARL from turn-based two-agent games to real-time multiagent games including sports, FPS, RTS, and MOBA genres. Highlights AlphaStar, OpenAI Five, and implementations in Rocket League, Minecraft, Quake III Arena, Dota 2, Honor of Kings. Analyzes nonstationarity, partial observability, sparse rewards, team coordination, scalability. Proposes novel method to estimate game complexity.
- **Link**: [arXiv:2509.03682](https://arxiv.org/abs/2509.03682) | DOI: 10.1109/TG.2025.3588809

### SMAC-Talk: A Natural Language Extension of the StarCraft Multi-Agent Challenge for LLMs
- **Authors**: Joel Sol, Homayoun Najjaran
- **Affiliation**: —
- **Venue**: —
- **Abstract**: Extends SMAC with a natural language communication channel for evaluating LLM-based agents in cooperative multi-agent environments. Includes settings with deceptive communicators that try to disrupt allies through communication alone. Benchmarks Qwen3.5 models, studying reasoning structure, memory, and model scale effects on coordination. Open benchmark release.
- **Link**: [arXiv:2606.04202](https://arxiv.org/abs/2606.04202)

### Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces
- **Authors**: Chenchen Zhang
- **Affiliation**: —
- **Venue**: —
- **Abstract**: Studies RL for LLM-based multi-agent systems through orchestration traces (temporal interaction graphs with spawning, delegation, communication, tool use). Identifies 8 reward families, 8 credit-bearing units, and 5 sub-decisions (spawn, delegate, communicate, aggregate, stop). Connects academic methods to industrial evidence from Kimi Agent Swarm, OpenAI Codex, Anthropic Claude Code. 84-entry tagged paper pool released.
- **Link**: [arXiv:2605.02801](https://arxiv.org/abs/2605.02801) | [Code](https://github.com/xxzcc/awesome-llm-mas-rl)

### OpenGuanDan: A Large-Scale Imperfect Information Game Benchmark
- **Authors**: —
- **Affiliation**: —
- **Venue**: —
- **Abstract**: Introduces GuanDan as a novel poker game benchmark with information sets up to 10^118, legal action space up to 10^4. Compares RL-based agents (DanZero, SDMC), game-theoretic agents (GS2), and LLM-based agents (Suspicion-Agent, PokerGPT, Agent-Pro). Demonstrates that existing GuanDan AI fails to achieve superhuman performance, calling for further advances.
- **Link**: [arXiv:2602.00676](https://arxiv.org/abs/2602.00676)

---

## 2. Game AI Bot — LLM-Powered Game Agents & NPC Intelligence

### Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with LLMs
- **Authors**: Chee Wei Tan, Yuchen Wang, Shangxin Guo
- **Affiliation**: —
- **Venue**: —
- **Abstract**: Introduces Nemobot, an interactive agentic engineering environment for creating LLM-powered game agents. Operates across 4 game classes: dictionary-based (compressed state-action mappings), rigorously solvable (mathematical reasoning), heuristic-based (minimax + crowdsourced), and learning-based (RLHF + self-critique). Tool-augmented generation and fine-tuning of strategic game agents.
- **Link**: [arXiv:2604.21896](https://arxiv.org/abs/2604.21896)

### Augmenting Game AI with Deep Reinforcement Learning
- **Authors**: Alessandro Sestini et al.
- **Affiliation**: —
- **Venue**: Conference on Games 2026 (vision paper)
- **Abstract**: Surveys how RL can create more believable game AI. Describes deployment examples (EA SPORTS FC 25 goalkeeper positioning, Battlefield 6 soldier locomotion). Identifies bottlenecks: sample efficiency, generalization, believability vs optimality tension. Proposes framework for training RL models suited towards game AI and game development.
- **Link**: [arXiv:2606.20210](https://arxiv.org/abs/2606.20210)

### Experience Transfer for Multimodal LLM Agents in Minecraft Game (Echo)
- **Authors**: Chenghao Li, Jun Liu, Songbo Zhang, Huadong Jian, Hao Ni, Lik-Hang Lee, Sung-Ho Bae, Guoqing Wang, Yang Yang, Chaoning Zhang
- **Affiliation**: UESTC, KAIST, HK PolyU, Kyung Hee University
- **Venue**: —
- **Abstract**: Proposes Echo, a transfer-oriented memory framework for Minecraft MLLM agents. Decomposes reusable knowledge into 5 dimensions: structure, attribute, process, function, interaction. Uses In-Context Analogy Learning (ICAL) to retrieve and adapt experiences. Achieves 1.3×–1.7× speed-up on object-unlocking tasks under from-scratch learning; exhibits burst-like chain-unlocking phenomenon.
- **Link**: [arXiv:2604.05533](https://arxiv.org/abs/2604.05533) | [Code](https://github.com/CatworldLee/Echo)

### Voyager: An Open-Ended Embodied Agent with Large Language Models
- **Authors**: Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, Anima Anandkumar
- **Affiliation**: NVIDIA, Caltech, UT Austin, Stanford, UW Madison
- **Venue**: TMLR 2024 (journal-track ICLR 2025)
- **Abstract**: First LLM-powered embodied lifelong learning agent in Minecraft. Three components: automatic curriculum for exploration, ever-growing skill library of executable code, iterative prompting with environment feedback. Interacts with GPT-4 via blackbox queries. Obtains 3.3× more unique items, travels 2.3× longer distances, unlocks tech tree milestones up to 15.3× faster than prior SOTA.
- **Link**: [arXiv:2305.16291](https://arxiv.org/abs/2305.16291)

---

## 3. Game Foundation Models — Generalist Game Agents

### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi Fan
- **Affiliation**: NVIDIA, Stanford, Caltech, UChicago, UT Austin
- **Venue**: CVPR 2026
- **Abstract**: Vision-action foundation model trained on 40,000 hours of gameplay video across 1,000+ games. Three contributions: (1) internet-scale video-action dataset from automatic player action extraction, (2) multi-game benchmark for cross-game generalization, (3) unified vision-action model via large-scale behavior cloning. Up to 52% relative improvement in task success rates on unseen games. Model weights, dataset, and evaluation suite open-sourced.
- **Link**: [arXiv:2601.02427](https://arxiv.org/abs/2601.02427) | [Project](https://nitrogen.minedojo.org/) | [Code](https://github.com/MineDojo/NitroGen)

### Towards Generalist Game Players: An Investigation of Foundation Models in the Game Multiverse
- **Authors**: Kuan Zhang, Dongchen Liu, Qiyue Zhao, Tianyu Xin, Yue Su et al.
- **Affiliation**: Tsinghua University
- **Venue**: —
- **Abstract**: Comprehensive survey tracing the full lifecycle of generalist game players across four eras: symbolic → deep RL → foundation models → future creator stage. Four pillars: Dataset, Model, Harness, Benchmark. Identifies five fundamental trade-offs bounding the system. Charts a five-level roadmap from single-game mastery to omnipotent creator that simultaneously creates and evolves within game multiverse. 51 pages.
- **Link**: [arXiv:2605.09965](https://arxiv.org/abs/2605.09965) | [GitHub](https://github.com/THUSI-Lab/Awesome-LFMs-Play-Games)

### SIMA 2: A Generalist Embodied Agent for 3D Virtual Worlds
- **Authors**: SIMA Team (Google DeepMind)
- **Affiliation**: Google DeepMind
- **Venue**: —
- **Abstract**: Built upon Gemini foundation model. Acts as interactive partner capable of reasoning about high-level goals, conversing with users, handling complex instructions through language and images. Closes gap with human performance across diverse game portfolio, demonstrates robust generalization to unseen environments. Uses Gemini to generate tasks and rewards for autonomous self-improvement.
- **Link**: [arXiv (Dec 2025)](https://arxiv.org/search/?searchtype=author&query=SIMA+team)

---

## 4. Procedural Content Generation — RL & LLM for Game Content

### PCGRLLM: Large Language Model-Driven Reward Design for Procedural Content Generation Reinforcement Learning
- **Authors**: In-Chang Baek, Sung-Hyun Kim, Sam Earle, Zehua Jiang, Jin-Ha Noh, Julian Togelius, Kyung-Joong Kim
- **Affiliation**: GIST, NYU
- **Venue**: IEEE Transactions on Games (accepted May 2026)
- **Abstract**: Extends PCGRL architecture with LLM-driven reward generation. Uses feedback mechanism and reasoning-based prompt engineering for story-to-reward generation in 2D environments. Demonstrates 415% and 40% performance improvements depending on LLM zero-shot capability. Human-competitive performance achieved, reducing human dependency in game AI development.
- **Link**: [arXiv:2502.10906](https://arxiv.org/abs/2502.10906)

### IPCGRL: Language-Instructed Reinforcement Learning for Procedural Level Generation
- **Authors**: In-Chang Baek, Sung-Hyun Kim, Seo-Young Lee, Dong-Hyeon Kim, Kyung-Joong Kim
- **Affiliation**: GIST
- **Venue**: Conference on Games 2025
- **Abstract**: Instruction-based PCG via RL incorporating sentence embedding model. Fine-tunes task-specific embedding representations to compress game-level conditions. Up to 21.4% improvement in controllability and 17.2% improvement in generalizability for unseen instructions. Extends modality of conditional input for PCG.
- **Link**: [arXiv:2503.12358](https://arxiv.org/abs/2503.12358)

### PCG in Games: A Survey with Insights on Emerging LLM Integration
- **Authors**: Mahdi Farrokhi Maleki, Richard Zhao
- **Affiliation**: —
- **Venue**: AIIDE 2024 (AAAI)
- **Abstract**: Comprehensive survey of PCG algorithms including search-based, ML-based, noise functions, and LLMs. Compares methods by content type and publication date. Identifies gaps and future research directions. Covers the disruptive impact of LLMs on PCG advancement.
- **Link**: [arXiv:2410.15644](https://arxiv.org/abs/2410.15644) | DOI: 10.1609/aiide.v20i1.31877

---

## 5. Game Benchmarks — Evaluation Suites & Agent Benchmarks

### GameDevBench: Evaluating Agentic Capabilities Through Game Development
- **Authors**: Wayne Chi, Yixiong Fang, Arnav Yayavaram, Siddharth Yayavaram, Seth Karten, Qiuhong Anna Wei, Runkun Chen, Alexander Wang, Valerie Chen, Ameet Talwalkar, Chris Donahue
- **Affiliation**: —
- **Venue**: —
- **Abstract**: First benchmark for evaluating agents on game development tasks. 333 tasks from web/video tutorials requiring multimodal understanding (shaders, sprites, animations). Average solution requires 3× more code than prior benchmarks. Best agent solves only 53.8%. Introduces image- and video-based feedback mechanisms improving GPT-5.4 from 41.1% to 52.0%.
- **Link**: [arXiv:2602.11103](https://arxiv.org/abs/2602.11103)

### Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games
- **Authors**: Dongmin Park et al.
- **Affiliation**: KRAFTON
- **Venue**: —
- **Abstract**: Benchmark across 12 popular video games spanning all major genres. Uses plug-and-play MCP interface. Releases fine-tuning dataset of expert LLM gameplay trajectories. Includes game leaderboards, LLM battle arenas, ablation studies of input modality, agentic strategies, and fine-tuning effects.
- **Link**: [arXiv:2506.03610](https://arxiv.org/abs/2506.03610) | [Code](https://github.com/krafton-ai/Orak) | [Dataset](https://huggingface.co/datasets/KRAFTON/Orak)

### OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics
- **Authors**: Mingxian Lin, Shengju Qian, Yuqi Liu, Yi-Hua Huang, Yiyu Wang, Wei Huang, Yitang Li, Fan Zhang, Zeyu Hu, Lingting Zhu, Xin Wang, Xiaojuan Qi
- **Affiliation**: HKU, LIGHTSPEED Studios
- **Venue**: —
- **Abstract**: Real-time benchmark of 12 newly built Unreal Engine 5 games spanning Solo (7), PvP (3), and Coop (2) with unified action interfaces. Introduces Improvement Dynamics Curve (IDC) — agentic-reflection harness where a tool-using reflector LLM refines bounded skill prompts across multiple rounds. Evaluates 12 VLM agents on cold-start leaderboard and 4 top agents under IDC.
- **Link**: [arXiv:2606.09826](https://arxiv.org/abs/2606.09826)

### GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents
- **Authors**: Mingyu Ouyang, Siyuan Hu, Kevin Qinghong Lin, Hwee Tou Ng, Mike Zheng Shou
- **Affiliation**: National University of Singapore (NUS)
- **Venue**: —
- **Abstract**: Benchmark with 34 diverse games and 170 tasks, each with state-verifiable metrics. Tests two agent interfaces: computer-use agents (keyboard/mouse) and generalist multimodal agents (semantic action space). Best performing agent far from human capabilities. Extensive rerun experiments demonstrate robustness. Offers standardized, verifiable, reproducible evaluation framework.
- **Link**: [arXiv:2604.07429](https://arxiv.org/abs/2604.07429) | [Project](https://gameworld-bench.github.io)

### BALROG: Benchmarking Agentic LLM and VLM Reasoning On Games
- **Authors**: Davide Paglieri et al.
- **Affiliation**: UCL DARK Lab, IDEAS NCBR, U. Warsaw, Oxford, NYU, Anthropic
- **Venue**: ICLR 2025 (poster)
- **Abstract**: Aggregates 6 RL environments (BabyAI, Crafter, TextWorld, Baba Is AI, MiniHack, NLE) for evaluating LLM/VLM agentic capabilities. Requires natural language actions over hundreds-thousands of steps. Key finding: frontier models complete only a fraction of tasks; VLMs sometimes perform worse with visual input than textual descriptions.
- **Link**: [arXiv:2411.13543](https://arxiv.org/abs/2411.13543) | [Website](https://balrogai.com/) | [Code](https://github.com/balrog-ai/BALROG)

### GameCraft-Bench: Can Agents Build Playable Games End-to-End in a Real Game Engine?
- **Authors**: Tongxu Luo, Rongsheng Wang, Jiaxi Bi et al. (25 authors)
- **Affiliation**: —
- **Venue**: —
- **Abstract**: Formalizes end-to-end game generation as producing complete game artifacts in a target environment. Proposes interaction-grounded evaluation with replayed demonstrations and rubric-guided multimodal judging. 140 Godot tasks across 15 game families. Strongest agent achieves only 41.46%; most agents score below 40%. Agents struggle with complete games with functional visual feedback and coherent presentation.
- **Link**: [arXiv:2606.17861](https://arxiv.org/abs/2606.17861)

---

## 6. Industry Game AI — Production Deployment & Real-Time Inference

### Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory
- **Authors**: Zile Wang, Zexiang Liu, Jiaxing Li, Kaichen Huang, Baixin Xu et al.
- **Affiliation**: Skywork AI
- **Venue**: —
- **Abstract**: Memory-augmented interactive world model for 720p real-time long-form video generation. Achieves 40 FPS at 720p with 5B model. Industrial-scale data engine integrating Unreal Engine synthetic data, AAA game collection, real-world video augmentation. Camera-aware memory retrieval enables minute-long consistency. Scales to 2×14B model for improved quality. Practical pathway toward industrial-scale deployable world models.
- **Link**: [arXiv:2604.08995](https://arxiv.org/abs/2604.08995) | [Project](https://matrix-game-v3.github.io/)

### GameNGen: Diffusion Models Are Real-Time Game Engines
- **Authors**: Dani Valevski, Yaniv Leviathan, Moab Arar, Shlomi Fruchter
- **Affiliation**: Google Research, Google DeepMind, Tel Aviv University
- **Venue**: ICLR 2025
- **Abstract**: First game engine powered entirely by a neural model. Simulates DOOM at 20 FPS on a single TPU. Two-phase training: (1) RL agent plays game and records sessions, (2) diffusion model trained to produce next frame conditioned on past frames and actions. PSNR of 29.4, comparable to lossy JPEG compression. Human raters only slightly better than random at distinguishing simulation from real game.
- **Link**: [arXiv:2408.14837](https://arxiv.org/abs/2408.14837) | [Project](https://gamengen.github.io/)

---

## 7. Related Techniques — Self-Play, Curiosity, World Models, Imitation, IRL

### SPA: Internalizing World Models via Self-Play Finetuning for Agentic RL
- **Authors**: Shiqi Chen, Tongyao Zhu, Zian Wang, Jinghan Zhang, Kangrui Wang, Siyang Gao, Teng Xiao, Yee Whye Teh, Junxian He, Manling Li
- **Affiliation**: —
- **Venue**: —
- **Abstract**: Equips LLM agents with internal world model via self-play supervised finetuning (SFT) stage to learn environment dynamics, then uses it to simulate future states prior to policy optimization. Sokoban success rate from 25.6% to 59.8%; FrozenLake from 22.1% to 70.9% on Qwen2.5-1.5B-Instruct. Outperforms online world-modeling baselines.
- **Link**: [arXiv:2510.15047](https://arxiv.org/abs/2510.15047)

### CDE: Curiosity-Driven Exploration for Efficient Reinforcement Learning in LLMs
- **Authors**: Runpeng Dai, Linfeng Song, Haolin Liu, Zhenwen Liang, Dian Yu, Haitao Mi, Zhaopeng Tu, Rui Liu, Tong Zheng, Hongtu Zhu, Dong Yu
- **Affiliation**: —
- **Venue**: —
- **Abstract**: Introduces curiosity-driven exploration for RLVR in LLMs. Uses actor-side perplexity and critic-side multi-head value variance as exploration bonuses. Theoretical analysis connects critic-wise bonus to count-based exploration. ~+3 point improvement over standard GRPO/PPO on AIME benchmarks. Identifies calibration collapse mechanism within RLVR.
- **Link**: [arXiv:2509.09675](https://arxiv.org/abs/2509.09675)

### Valdi: Value Diffusion World Models
- **Authors**: Christopher Lindenberg, Kashyap Chitta
- **Affiliation**: —
- **Venue**: RLC 2026 WMW
- **Abstract**: Combines end-to-end online training for MPC with latent diffusion dynamics model. In CarRacing environment, single diffusion step at both training and inference matches deterministic MLP baseline. Exposes trade-off between predictive multimodality and control performance.
- **Link**: [arXiv:2607.00917](https://arxiv.org/abs/2607.00917) | [Code](https://github.com/Kit115/ValueDiffusionWorldModels)

### Scaling World-Model RL Through Diffusion Policy Optimization
- **Authors**: Xiaoyuan Cheng, Wenxuan Yuan, Zhancun Mu, Yuanzhao Zhang, Yiming Yang, Hai Wang, Zhuo Sun, Che Liu
- **Affiliation**: —
- **Venue**: —
- **Abstract**: Identifies structural misalignment between search and value learning in existing world model approaches — policy improvement relies on value functions from non-search policy, causing training inconsistency. Proposes diffusion policy optimization to address model bias, error compounding, and this structural misalignment.
- **Link**: [arXiv:2605.26282](https://arxiv.org/abs/2605.26282)

### RILe: Reinforced Imitation Learning
- **Authors**: Berat Mert Albaba et al.
- **Affiliation**: —
- **Venue**: —
- **Abstract**: Combines IL and IRL in a trainer-student framework. Trainer learns adaptive reward function; student uses it to imitate expert behaviors. Dynamic guidance adjusts as student evolves. Near-expert performance across multiple robotic locomotion tasks. Addresses high-dimensional environments where direct imitation fails.
- **Link**: [arXiv:2406.08472](https://arxiv.org/abs/2406.08472)

### Enhancing Inverse Reinforcement Learning through Encoding Dynamic Information in Reward Shaping
- **Authors**: Simon Sinong Zhan, Philip Wang, Qingyuan Wu, Ruochen Jiao, Yixuan Wang, Chao Huang, Qi Zhu
- **Affiliation**: Northwestern University, University of Southampton
- **Venue**: L4DC 2026
- **Abstract**: Maximum causal entropy off-policy IRL with transition-aware reward shaping. Embeds learned transition dynamics into reward for stochastic-invariant rewards. Theoretical bounds on reward error and performance. Superior performance on stochastic MuJoCo locomotion and Atari tasks; competitive on deterministic settings.
- **Link**: [arXiv:2410.03847](https://arxiv.org/abs/2410.03847)

### A Survey on Self-play Methods in Reinforcement Learning
- **Authors**: Ruize Zhang, Zelai Xu, Chengdong Ma, Chao Yu, Wei-Wei Tu, Wenhao Tang, Shiyu Huang, Deheng Ye, Wenbo Ding, Yaodong Yang, Yu Wang
- **Affiliation**: —
- **Venue**: —
- **Abstract**: Comprehensive survey of self-play methods in MARL. Covers Go, poker, video games. Provides unified framework and classification of existing self-play algorithms. Bridges gap between algorithms and practical implications in non-cooperative scenarios. Highlights open challenges and future directions.
- **Link**: [arXiv:2408.01072](https://arxiv.org/abs/2408.01072)

### Vid2World: Crafting Video Diffusion Models to Interactive World Models
- **Authors**: Siqiao Huang, Jialong Wu, Qixing Zhou, Shangchen Miao, Mingsheng Long
- **Affiliation**: —
- **Venue**: —
- **Abstract**: General approach for leveraging pre-trained video diffusion models as interactive world models. Systematically explores video diffusion causalization — reshaping architecture and training objective for autoregressive generation. Bridges gap between large-scale video pre-training and interactive decision-making.
- **Link**: [arXiv:2505.14357](https://arxiv.org/abs/2505.14357)

### Reward Shaping for (Inference-Time) Alignment: A Stackelberg Game Perspective
- **Authors**: Haichuan Wang, Tao Lin, Lingkai Kong, Ce Li, Hezi Jiang, Milind Tambe
- **Affiliation**: —
- **Venue**: ICML 2026
- **Abstract**: Formalizes reward model optimization under KL regularization as a Stackelberg game. Shows simple reward shaping approximates optimal reward model. Seamlessly integrates into existing alignment methods. Consistently improves average reward with >66% win-tie rates against all baselines.
- **Link**: [arXiv:2602.02572](https://arxiv.org/abs/2602.02572)

---

## Cross-Cutting Themes

| Theme | Papers |
|-------|--------|
| **Self-play → reasoning transfer** | SPIRAL, SPA, Self-play Survey |
| **Game foundation models** | NitroGen (CVPR 2026), Towards Generalist Game Players survey, SIMA 2 |
| **Neural game engines / world models** | GameNGen (ICLR 2025), Matrix-Game 3.0, Vid2World, Valdi, Scaling WM-RL |
| **LLM-PCG convergence** | PCGRLLM (IEEE ToG), IPCGRL (CoG 2025), PCG+LLM survey (AIIDE 2024) |
| **Benchmark standardization** | Orak (KRAFTON), OmniGameArena (UE5), GameWorld (NUS), GameDevBench, GameCraft-Bench, BALROG |
| **Industry deployment** | Augmenting Game AI (CoG 2026), Matrix-Game 3.0 (Skywork), GameNGen (Google) |
| **Curiosity & exploration for LLM RL** | CDE, SPA, RILe |
| **MARL surveys consolidating field** | MARL in Video Games (IEEE ToG), Self-play Survey |
| **LLM game agents** | Nemobot, Echo (Minecraft), SMAC-Talk, Voyager |
