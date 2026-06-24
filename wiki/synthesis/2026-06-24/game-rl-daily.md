---
title: "Game RL & Game AI Bot — Daily Survey (2026-06-24)"
type: synthesis
created: 2026-06-24
updated: 2026-06-24
sources: []
tags: [game-rl, game-ai, daily, arxiv, self-play, foundation-models, benchmarks, PCG, world-models, MARL]
---

# Game RL & Game AI Bot — Daily Survey (2026-06-24)

> Curated recent papers from arXiv, ICML 2026, ICLR 2026, CVPR 2026, and other venues on game reinforcement learning, game AI bots, game foundation models, procedural content generation, benchmarks, industry game AI, and related techniques. Compiled 2026-06-24.

---

## 1. Game RL — Reinforcement Learning in Games

### Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games
- **Authors**: Yidong He, Yutao Lai, Pengxu Yang, Jiarui Gan, Jiexin Wang, Yi Cai, Mengchen Zhao
- **Affiliation**: South China University of Technology, University of Oxford
- **Venue**: ICML 2026
- **Abstract**: Proposes Strat-Reasoner, an RL-based framework to improve LLMs' strategic reasoning in multi-agent games. Introduces recursive reasoning where an agent integrates opponents' reasoning processes. Uses centralized CoT comparison module for intermediate reward and group-relative RL for policy optimization. Achieves 22.1% average improvement across various multi-agent games.
- **Key Innovation**: Recursive reasoning paradigm + CoT comparison for fine-grained RL signals in game settings.
- **arXiv**: [2605.04906](https://arxiv.org/abs/2605.04906)

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning
- **Authors**: Bo Liu, Leon Guertler, Simon Yu, Zichen Liu, Penghui Qi, Daniel Balcells, Mickel Liu, Cheston Tan, Weiyan Shi, Min Lin, Wee Sun Lee, Natasha Jaques
- **Affiliation**: Multiple institutions (NTU, etc.)
- **Venue**: ICLR 2026
- **Abstract**: Self-play framework where LLMs learn by playing multi-turn zero-sum games against improving versions of themselves. Role-conditioned advantage estimation (RAE) stabilizes multi-agent training. Improves reasoning by up to 10% across 8 benchmarks. Multi-game training (TicTacToe, Kuhn Poker, Simple Negotiation) yields strongest results.
- **Key Innovation**: Zero-sum game self-play as RLVR alternative without human supervision; transferable reasoning patterns.
- **arXiv**: [2506.24119](https://arxiv.org/abs/2506.24119)

### Multi-Agent Deep Reinforcement Learning Under Constrained Communications (DG-MAPPO)
- **Authors**: Shahil Shaik, Jonathon M. Smereka, Yue Wang
- **Affiliation**: Cornell University
- **Venue**: arXiv 2026
- **Abstract**: Distributed MARL framework removing need for centralized critics. Novel Distributed Graph Attention Network (D-GAT) performs global state inference through multi-hop communication. DG-MAPPO evaluates on StarCraft II Multi-Agent Challenge, Google Research Football, and Multi-Agent MuJoCo, outperforming strong CTDE baselines.
- **Key Innovation**: Fully distributed graph attention for MARL with multi-hop peer-to-peer communication.
- **arXiv**: [2601.17069](https://arxiv.org/abs/2601.17069)

### Multi-Agent Model-Based RL with Joint State-Action Learned Embeddings (MMSA)
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Model-based MARL method fusing value factorization framework with joint state-action representation learning, amortized variational inference, and imagination module. Faithful latent rollouts enable learning decentralized policies from real and imagined experience. Evaluated on SMACv2 challenges.
- **Key Innovation**: Joint state-action embeddings + world model rollouts for cooperative MARL.
- **arXiv**: [2602.12520](https://arxiv.org/abs/2602.12520)

### Learning to Coordinate via Quantum Entanglement in Multi-Agent Reinforcement Learning
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Explores representation of agent coordination through quantum entanglement-inspired mechanisms in MARL. Novel approach to addressing non-stationarity in multi-agent settings.
- **Key Innovation**: Quantum entanglement as coordination mechanism in MARL.
- **arXiv**: [2602.08965](https://arxiv.org/abs/2602.08965)

### A Comprehensive Review of Multi-Agent Reinforcement Learning in Video Games
- **Authors**: Zhengyang Li, Qijin Ji, Xinghong Ling, Quan Liu
- **Affiliation**: (multiple)
- **Venue**: arXiv 2025 (Survey)
- **Abstract**: Comprehensive survey covering MARL from turn-based two-agent games to real-time multi-agent video games. Analyzes challenges: nonstationarity, partial observability, sparse rewards, team coordination, scalability. Covers Rocket League, Minecraft, Quake III, StarCraft II, Dota 2, Honor of Kings.
- **Key Innovation**: Novel method to estimate game complexity; comprehensive taxonomy of MARL in games.
- **arXiv**: [2509.03682](https://arxiv.org/abs/2509.03682)

### Reinforcement Learning in Strategy-Based and Atari Games: A Review of Google DeepMind's Innovations
- **Authors**: Abdelrhman Shaheen, Anas Badr, Ali Abohendy, Hatem Alsaadawy, Nadine Alsayad, Ehab H. El-Shazly
- **Affiliation**: (multiple)
- **Venue**: arXiv 2025/2026 (v2)
- **Abstract**: Reviews DeepMind's RL innovations in gaming: AlphaGo, AlphaGo Zero, MuZero. Analyzes supervised learning + RL integration, self-play efficiency, and model-based dynamics learning. Discusses MiniZero and multi-agent models.
- **arXiv**: [2502.10303](https://arxiv.org/abs/2502.10303)

### Craftax: A Lightning-Fast Benchmark for Open-Ended Reinforcement Learning
- **Authors**: Michael Matthews, Michael Beukman, Benjamin Ellis, Mikayel Samvelyan, Matthew Jackson, Samuel Coward, Jakob Foerster
- **Affiliation**: (FLAIR? Oxford)
- **Venue**: Preprint
- **Abstract**: Craftax is a JAX-based rewrite of Crafter running up to 250x faster. Extended with NetHack-inspired mechanics requiring deep exploration, long-term planning, memory, and continual adaptation. A run of PPO with 1B env interactions finishes in under an hour on a single GPU.
- **Key Innovation**: JAX-accelerated open-ended RL benchmark combining Crafter + NetHack elements.
- **arXiv**: [2402.16801](https://arxiv.org/abs/2402.16801)

---

## 2. Game AI Bot — LLM-Powered Agents, NPC Intelligence

### A Survey on Large Language Model-Based Game Agents (v5)
- **Authors**: Sihao Hu, Tiansheng Huang, Fatih Ilhan, Selim Furkan Tekin, Gaowen Liu, Ramana Rao Kompella, Ling Liu
- **Affiliation**: Georgia Institute of Technology, Cisco Research
- **Venue**: ACM Computing Surveys 2026
- **Abstract**: Up-to-date review of LLM-based game agents through unified reference architecture. Three core components: memory, reasoning, and perception-action interfaces. Multi-agent level covers communication protocols and organizational models. Challenge-centered taxonomy for 6 game genres.
- **Key Innovation**: Unified architecture for LLM game agents; genre-linked taxonomy.
- **arXiv**: [2404.02039](https://arxiv.org/abs/2404.02039) (v5, Jun 2026)

### Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games
- **Authors**: (multiple — KRAFTON AI)
- **Affiliation**: KRAFTON (PUBG)
- **Venue**: arXiv 2025/2026
- **Abstract**: Benchmark for training and evaluating LLM agents across 12 popular video games spanning all major genres. Plug-and-play MCP interface. Releases fine-tuning dataset of expert LLM gameplay trajectories. Includes game leaderboards, LLM battle arenas, and ablation studies.
- **Key Innovation**: First game benchmark with fine-tuning dataset; MCP-based interface; industry-grade from major game studio.
- **arXiv**: [2506.03610](https://arxiv.org/abs/2506.03610)

### ProxyWar: Dynamic Assessment of LLM Code Generation in Game Arenas
- **Authors**: Qi Wu, Wenjun Peng, Xinyu Wang
- **Affiliation**: (multiple)
- **Venue**: ICSE 2026
- **Abstract**: Framework that systematically assesses code generation quality by embedding LLM-generated agents within competitive game environments. Evaluates functional correctness and operational characteristics via automated testing, iterative code repair, and multi-agent tournaments.
- **Key Innovation**: Game-based competitive evaluation of LLM code generation; tournament-based assessment.
- **arXiv**: [2602.04296](https://arxiv.org/abs/2602.04296)

### LLM-Driven NPCs: Cross-Platform Dialogue System for Games and Social Platforms
- **Authors**: Li Song
- **Affiliation**: Independent
- **Venue**: arXiv 2025
- **Abstract**: Prototype system enabling LLM-powered NPCs to communicate with players both in Unity game environment and on Discord. Dialogue logs stored in cloud (LeanCloud) synchronize memory between platforms. Includes basic favorability mechanism for response shaping.
- **Key Innovation**: Cross-platform NPC memory synchronization between game and social platform.
- **arXiv**: [2504.13928](https://arxiv.org/abs/2504.13928)

### AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2025
- **Abstract**: Comprehensive framework for training LLM agents in multi-turn interactive decision-making through RL. Covers exploration, reward design, and trajectory optimization for game-like environments.
- **Key Innovation**: RL training framework for LLM agents in interactive environments.
- **arXiv**: [2509.23863](https://arxiv.org/abs/2509.23863)

---

## 3. Game Foundation Models — Generalist Game Agents

### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loic Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi (Jim) Fan
- **Affiliation**: NVIDIA, UT Austin, Stanford, Caltech
- **Venue**: CVPR 2026
- **Abstract**: Vision-action foundation model trained on 40,000 hours of gameplay videos across 1,000+ games. Three key ingredients: (1) internet-scale action-labeled video dataset with automated action extraction, (2) multi-game benchmark for cross-game generalization, (3) unified vision-action model via large-scale behavior cloning. Up to 52% relative improvement on unseen games.
- **Key Innovation**: First open generalist gaming foundation model; internet-scale gameplay data extraction.
- **arXiv**: [2601.02427](https://arxiv.org/abs/2601.02427)

### Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents
- **Authors**: Zihao Wang, Xujing Li, Yining Ye, Junjie Fang, et al. (27 authors)
- **Affiliation**: ByteDance / Seed
- **Venue**: arXiv 2025 (Oct)
- **Abstract**: Generalist game agent trained on 500B+ tokens with diverse trajectories. Unified scalable action space anchored to native keyboard-mouse inputs. Pre-trained across OS, web, and simulation games. Key techniques: decaying continual loss, Sparse-Thinking strategy. ~2x success rate over SOTA on Minecraft; outperforms GPT-5, Gemini 2.5 Pro, Claude 4 Sonnet on FPS benchmarks.
- **Key Innovation**: Unified action space across OS/web/game domains; large-scale cross-domain pre-training.
- **arXiv**: [2510.23691](https://arxiv.org/abs/2510.23691)

### Scaling Behavior Cloning Improves Causal Reasoning: An Open Model for Real-Time Video Game Playing
- **Authors**: Yuguang Yue, Irakli Salia, Samuel Hunt, Chris Green, Wenzhe Shi, Jonathan J. Hunt
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Open recipe for training a video game playing foundation model designed for inference in real-time on consumer GPU. Observes that causal reasoning improvements from behavior cloning scale with model size and training steps.
- **Key Innovation**: Real-time capable game model; causal reasoning emergence through scaling.
- **arXiv**: (referenced in NitroGen citations)

### Towards Generalist Game Players: An Investigation of Foundation Models
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Investigates multimodal foundation world models for generalist game players. Integrates vision, language, and action for generalist embodied agents across diverse game environments.
- **Key Innovation**: Multimodal foundation world models adapted for interactive game tasks.
- **arXiv**: [2605.04326](https://arxiv.org/abs/2605.04326)

---

## 4. Procedural Content Generation — RL & LLM for Game Content

### Procedural Content Generation in Games: A Survey with Insights on Emerging LLM Integration
- **Authors**: Mahdi Farrokhi Maleki, Richard Zhao
- **Affiliation**: University of Calgary
- **Venue**: AAAI AIIDE 2024
- **Abstract**: Comprehensive survey exploring PCG algorithms: search-based, ML-based, noise functions, and LLMs. Compares methods by content type and publication date. Identifies gaps and suggests future research directions including combined methods.
- **Key Innovation**: First survey integrating LLM-based PCG alongside traditional approaches.
- **arXiv**: [2410.15644](https://arxiv.org/abs/2410.15644)

### PCGRL+: Scaling, Control and Generalization in Reinforcement Learning Level Generators
- **Authors**: (NYU Game Innovation Lab)
- **Affiliation**: New York University
- **Venue**: arXiv 2024
- **Abstract**: Advances in PCG via RL (PCGRL) focusing on scaling to larger levels, control over generation, and generalization across game content types.
- **Key Innovation**: Scaling RL-based level generators with controllability.
- **arXiv**: [2408.12525](https://arxiv.org/abs/2408.12525)

### PCGRLLM: Large Language Model-Driven Reward Design for Procedural Content Generation Reinforcement Learning
- **Authors**: (NYU Game Innovation Lab)
- **Affiliation**: New York University
- **Venue**: arXiv 2025
- **Abstract**: Uses LLMs to design reward functions for PCG RL agents. Combines zero-shot LLM reasoning with RL-based level generation to create high-quality game content.
- **Key Innovation**: LLM as reward designer for PCG RL agents.
- **arXiv**: [2502.10906](https://arxiv.org/abs/2502.10906)

### CrawLLM: An LLM-Based Pipeline for Game Asset Generation
- **Authors**: Marvin Zammit, Antonios Liapis, Georgios N. Yannakakis
- **Affiliation**: University of Malta, Institute of Digital Games
- **Venue**: IEEE Transactions on Games 2026
- **Abstract**: LLM-driven pipeline for generating complete game assets including descriptions, rules, cards, and complete game designs. Demonstrates that semantic themes remain discernible across generated artifacts.
- **Key Innovation**: End-to-end LLM pipeline for game asset generation from theme to implementation.
- **Link**: antoniosliapis.com (IEEE ToG 2026 Early Access)

### Diverse Level Generation via Machine Learning of Quality Diversity (MLQD)
- **Authors**: Konstantinos Sfikas, Antonios Liapis, Georgios N. Yannakakis
- **Affiliation**: Institute of Digital Games
- **Venue**: FDG Workshop on PCG 2025
- **Abstract**: Combines quality-diversity (QD) evolutionary algorithms with ML (Transformers) to replicate QD discovery via efficient generative models. Tested on strategy game map sketches. Transformer captures both diversity and quality traits of training sets.
- **Key Innovation**: Transformer learns to emulate quality-diversity evolution for game content generation.

### The Procedural Content Generation Benchmark
- **Authors**: Ahmed Khalifa, Roberto Gallotta, Matthew Barthet, Antonios Liapis, Julian Togelius, Georgios N. Yannakakis
- **Affiliation**: Institute of Digital Games / NYU
- **Venue**: FDG 2025
- **Abstract**: Open-source benchmark with 12 game-related problems for evaluating generative algorithms. Problems range from levels to simple arcade game rule sets. Each problem has representation, parameters, and metrics for quality, diversity, and controllability.
- **Key Innovation**: Standardized benchmark for PCG algorithm comparison.

---

## 5. Game Benchmarks — Evaluation Suites

### BALROG: Benchmarking Agentic LLM and VLM Reasoning on Games
- **Authors**: Davide Paglieri, Bartłomiej Cupiał, Samuel Coward, Ulyana Piterbarg, Maciej Wołczyk, Akbir Khan, Eduardo Pignatelli, Łukasz Kuciński, Lerrel Pinto, Rob Fergus, Jakob Foerster, Jack Parker-Holder, Tim Rocktäschel
- **Affiliation**: UCL, Oxford, NYU, Anthropic, IDEAS NCBR
- **Venue**: ICLR 2025
- **Abstract**: Benchmark assessing LLM/VLM agentic capabilities via diverse RL game environments from easy (seconds) to extremely challenging (NetHack, years to master). Fine-grained metrics. Key finding: VLMs often perform worse with visual representations than text-only inputs.
- **Key Innovation**: Multi-difficulty game benchmark; counterintuitive VLM finding.
- **arXiv**: [2411.13543](https://arxiv.org/abs/2411.13543)

### LMGame Bench: How Good are LLMs at Playing Games?
- **Authors**: (lmgame-org)
- **Affiliation**: (multiple)
- **Venue**: ICLR 2026
- **Abstract**: Benchmark built on well-established video games (platformer, puzzle, narrative detective). Introduces scaffolds (perception, memory modules) to overcome VLM limitations. Tests 13 models across 6 games. o3 and o1 top-2; significant gap between model and human performance.
- **Key Innovation**: Gaming harness for VLMs; standardized prompt optimization; contamination detection.
- **arXiv**: [2505.15146](https://arxiv.org/abs/2505.15146)

### DSGBench: A Diverse Strategic Game Benchmark for Evaluating LLM-based Agents
- **Authors**: Wenjie Tang, Yuan Zhou, Keyan Cheng, Erqiang Xu, Liquan Xiao, Minne Li
- **Affiliation**: National University of Defense Technology, Intelligent Game and Decision Lab (IGDL)
- **Venue**: arXiv 2025/2026
- **Abstract**: Benchmark with 6 classic strategic games (StarCraft II, Civilization, Street Fighter III, Diplomacy, Werewolf, Stratego). Five capability dimensions: strategic planning, real-time decision-making, social reasoning, team collaboration, adaptive learning. Fine-grained trajectory tracking.
- **Key Innovation**: Multi-dimensional capability evaluation through diverse strategic games.
- **arXiv**: [2503.06047](https://arxiv.org/abs/2503.06047)

### AI GameStore: Scalable, Open-Ended Evaluation of Machine General Intelligence with Human Games
- **Authors**: Lance Ying, Ryan Truong, Prafull Sharma, Kaiya Ivy Zhao, Nathan Cloos, Kelsey R. Allen, Thomas L. Griffiths, Katherine M. Collins, José Hernández-Orallo, Phillip Isola, Samuel J. Gershman, Joshua B. Tenenbaum
- **Affiliation**: MIT, Harvard, UBC, Princeton, Cambridge, UPV
- **Venue**: arXiv 2026
- **Abstract**: Platform using LLMs with humans-in-the-loop to synthesize representative human games from Apple App Store and Steam. Generated 100 games. Evaluated 7 frontier VLMs — best models achieved <10% of human average score on most games. Struggled with world-model learning, memory, and planning.
- **Key Innovation**: Human-game-derived benchmark; scalable open-ended evaluation; reveals large human-AI gap.
- **arXiv**: [2602.17594](https://arxiv.org/abs/2602.17594)

### MCU: An Evaluation Framework for Open-Ended Game Agents (Minecraft Universe)
- **Authors**: Xinyue Zheng, Haowei Lin, Kaichen He, Zihao Wang, Zilong Zheng, Yitao Liang
- **Affiliation**: (multiple)
- **Venue**: ICML 2026
- **Abstract**: Comprehensive evaluation framework in Minecraft with 3,452 composable atomic tasks across 11 major categories. Task composition mechanism generating infinite diverse tasks. AutoEval system achieves 91.5% alignment with human ratings.
- **Key Innovation**: 3,452 atomic tasks + VLM-based automated evaluation with high human alignment.
- **arXiv**: [2310.08367](https://arxiv.org/abs/2310.08367)

### Game Reasoning Arena: A Framework and Benchmark for Assessing Reasoning Capabilities via Game Play
- **Authors**: Lucia Cipolina-Kun, Marianna Nezhurina, Jenia Jitsev
- **Affiliation**: (multiple)
- **Venue**: arXiv 2025
- **Abstract**: Framework for evaluating LLM decision-making through strategic board games in Google OpenSpiel. Enables comparisons between LLM agents, heuristic agents, and RL agents. Integrates API access via liteLLM and local deployment via vLLM.
- **Key Innovation**: OpenSpiel-based standardized LLM game reasoning evaluation with distributed execution.
- **arXiv**: [2508.03368](https://arxiv.org/abs/2508.03368)

---

## 6. Industry Game AI — Studio Papers & Deployment

### GameNGen: Diffusion Models Are Real-Time Game Engines
- **Authors**: Dani Valevski, Yaniv Leviathan, Moab Arar, Shlomi Fruchter
- **Affiliation**: Google Research, Google DeepMind, Tel Aviv University
- **Venue**: ICLR 2025
- **Abstract**: First game engine powered entirely by a neural model enabling real-time interaction. Trained on DOOM gameplay, runs at 20 FPS on a single TPU. Next-frame prediction PSNR of 29.4 (comparable to lossy JPEG). Human raters barely distinguish short clips from real game.
- **Key Innovation**: Neural game engine replacing traditional game loop; diffusion model as real-time interactive simulator.
- **arXiv**: [2408.14837](https://arxiv.org/abs/2408.14837)

### Genie 3: A New Frontier for World Models
- **Authors**: Jack Parker-Holder, Shlomi Fruchter (Google DeepMind)
- **Affiliation**: Google DeepMind
- **Venue**: Blog/Technical Report (2026)
- **Abstract**: General purpose world model generating diverse interactive environments from text prompts. Navigable in real time at 24 FPS, 720p resolution, retaining consistency for minutes. Built on decade of DeepMind environment simulation research.
- **Key Innovation**: Text-to-interactive-world generation at real-time resolution.
- **Link**: [deepmind.google](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/)

### Dreamer 4: Training Agents Inside of Scalable World Models
- **Authors**: Danijar Hafner, Wilson Yan, Timothy Lillicrap
- **Affiliation**: Google DeepMind
- **Venue**: arXiv 2025
- **Abstract**: Scalable agent that solves control tasks by RL inside a fast and accurate world model. First agent to obtain diamonds in Minecraft purely from offline data (no environment interaction). Shortcut forcing objective + efficient transformer. 100× less data than VPT offline agent. Real-time interactive inference on single GPU.
- **Key Innovation**: Offline-to-diamonds in Minecraft; scalable world model for imagination training.
- **arXiv**: [2509.24527](https://arxiv.org/abs/2509.24527)

### Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory
- **Authors**: Zile Wang, Zexiang Liu, Jaixing Li, et al. (23 authors)
- **Affiliation**: Skywork AI
- **Venue**: arXiv 2026
- **Abstract**: Memory-augmented interactive world model for 720p real-time long-form video generation. Up to 40 FPS at 720p with 5B model. Industrial-scale data engine using Unreal Engine + AAA games + real video. Camera-aware memory retrieval for minute-long consistency.
- **Key Innovation**: 40 FPS 720p interactive world model; long-horizon memory via camera-aware retrieval.
- **arXiv**: [2604.08995](https://arxiv.org/abs/2604.08995)

### Real-Time AI Inference Patterns from the Gaming Industry (INFUSE)
- **Authors**: Jam & Tea Studio
- **Affiliation**: Jam & Tea Studio
- **Venue**: Blog/Technical (2025)
- **Abstract**: Detailed architecture description of INFUSE inference engine alongside Unreal Engine for adaptive narrative/behavioral logic. Actors (NPC-level) and Directors (world-level) pattern. Stateless inference with 20-40K token input, ~100 token output. Self-hosted open-weight models, strict structured generation.
- **Key Innovation**: Production-grade real-time AI inference architecture for games; Actor/Director pattern.

### A Minecraft Agent Based on Hierarchical Deep Reinforcement Learning
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: IJITEE 2025
- **Abstract**: Hierarchical agent with high-level planner (options framework), mid-level controllers (resource gathering, crafting), low-level visuomotor policy. Integrates MineRL + VPT pretraining. Evaluated on Obtain Diamond and BASALT benchmarks.
- **Key Innovation**: Three-level hierarchical RL for Minecraft with demonstration pretraining.
- **DOI**: [10.35940/ijitee.K1154.14111025](https://doi.org/10.35940/ijitee.K1154.14111025)

---

## 7. Related Techniques — Self-Play, Curiosity, HRL, World Models, Imitation, Reward Shaping

### SPEAR: Self-Imitation with Progressive Exploration for Agentic Reinforcement Learning
- **Authors**: Yulei Qin et al. (Youtu-Agent Team, 16 authors)
- **Affiliation**: Tencent
- **Venue**: arXiv 2025
- **Abstract**: Curriculum-based self-imitation learning (SIL) recipe for training agentic LLMs. Balances exploration-exploitation via intrinsic reward shaping + self-imitation across stages. Tested on ALFWorld and WebShop — increases success rates of GRPO/GiGPO/Dr.BoT by up to 20.7%.
- **Key Innovation**: Progressive curriculum for SIL; tool-call rewards for skill-level exploration.
- **arXiv**: [2509.22601](https://arxiv.org/abs/2509.22601)

### SeRL: Self-Play Reinforcement Learning for LLMs with Limited Data
- **Authors**: Wenkai Fang, Shunyu Liu, Yang Zhou, Kongcheng Zhang, Tongya Zheng, Kaixuan Chen, Mingli Song, Dacheng Tao
- **Affiliation**: Zhejiang University, Nanyang Technological University
- **Venue**: arXiv 2025/2026
- **Abstract**: Self-play RL framework bootstrapping LLM training with limited initial data. Two modules: self-instruction (generates additional instructions with online filtering) and self-rewarding (majority-voting mechanism for reward estimation without external annotations).
- **Key Innovation**: Self-instruction + self-rewarding eliminates need for human annotation in RL training.
- **arXiv**: [2505.20347](https://arxiv.org/abs/2505.20347)

### Learn the Ropes, Then Trust the Wins: SPEAR (Agentic RL)
- **Authors**: Youtu-Agent Team (Tencent)
- **Affiliation**: Tencent
- **Venue**: arXiv 2025
- **Abstract**: Extends vanilla SIL with entropy steering across stages for multi-turn LLM agents. Intrinsic rewards for tool-use skill accumulation; self-imitation strengthening over time. Clipping of high-covariance tokens for stability.
- **Key Innovation**: Entropy-based progressive curriculum for LLM agent RL.
- **arXiv**: [2509.22601](https://arxiv.org/abs/2509.22601)

### Temporal Self-Imitation Learning (TSIL)
- **Authors**: Yinsen Jia, Boyuan Chen
- **Affiliation**: Duke University
- **Venue**: arXiv 2026 (Jun)
- **Abstract**: RL framework mining temporally efficient successful trajectories as reusable supervision. Progressive refinement using adaptive temporal targets. Across 15 long-horizon manipulation tasks, consistently improves learning efficiency and robustness.
- **Key Innovation**: Temporal efficiency as self-supervisory signal beyond engineered rewards.
- **arXiv**: [2606.19752](https://arxiv.org/abs/2606.19752)

### Reward Design Agent for Reinforcement Learning (RDA)
- **Authors**: (multiple)
- **Affiliation**: (multiple)
- **Venue**: arXiv 2026
- **Abstract**: Uses VLM-based visual trajectory analysis to design and refine reward functions for RL. Compares against Eureka (LLM-based reward design). RDA achieves 0.95 alignment on ManiSkill and significantly outperforms in long-horizon tasks where visual analysis detects misaligned behaviors.
- **Key Innovation**: Visual trajectory analysis for reward design; detects reward mis-specification.
- **arXiv**: [2606.01672](https://arxiv.org/abs/2606.01672)

### Structured Imitation Learning of Interactive Policies through Inverse Games
- **Authors**: Max M. Sun, Todd Murphey
- **Affiliation**: Northwestern University
- **Venue**: RSS 2025 Workshop
- **Abstract**: Combines generative single-agent policy learning with game-theoretic structure for interactive policies. Two-step process: learn individual behavioral patterns from demonstrations, then learn inter-agent dependencies via inverse game problem. Tested on 5-agent social navigation.
- **Key Innovation**: Inverse game formulation for multi-agent imitation learning.
- **arXiv**: [2511.12848](https://arxiv.org/abs/2511.12848)

### Multi-Agent Strategic Games with LLMs: Security Dilemma
- **Authors**: Maxim Chupilkin
- **Affiliation**: (independent)
- **Venue**: arXiv 2026
- **Abstract**: Uses LLMs as experimental subjects in repeated security dilemma games. Reproduces canonical IR theory mechanisms: multipolarity increases conflict, finite horizons induce unraveling, communication reduces conflict. Provides access to agents' private reasoning.
- **Key Innovation**: LLMs as subjects for strategic game theory experimentation.
- **arXiv**: [2605.03604](https://arxiv.org/abs/2605.03604)

### Interpretability in Action: Exploratory Analysis of VPT, a Minecraft Agent
- **Authors**: Karolis Jucys, George Adamopoulos, Mehrab Hamidi, Stephanie Milani, et al.
- **Affiliation**: Mila, UdeM, etc.
- **Venue**: arXiv 2024
- **Abstract**: Mechanistic interpretability of VPT Minecraft agent. Attention analysis reveals agent pays attention to last 4 frames and key-frames in 6-second memory. Uncovers goal misgeneralization: VPT mistakes villager in brown clothes for tree trunk and punches it to death.
- **Key Innovation**: First mechanistic analysis of large open-source game agent; goal misgeneralization discovery.
- **arXiv**: [2407.12161](https://arxiv.org/abs/2407.12161)

---

## Summary

| Category | Papers | Key Trends |
|----------|--------|------------|
| Game RL | 8 | Self-play for reasoning, distributed MARL, quantum coordination, model-based MARL |
| Game AI Bot | 5 | LLM-agent surveys, MCP-based benchmarks, cross-platform NPCs, competitive code-gen eval |
| Game Foundation Models | 4 | Open generalist agents (NitroGen), unified action spaces (Game-TARS), real-time capable models |
| Procedural Content Generation | 5 | LLM-driven reward design for PCG-RL, LLM asset pipelines, standardized PCG benchmarks |
| Game Benchmarks | 6 | Multi-game strategic eval, human-game derived suites, open-ended MCU eval, OpenSpiel LLM eval |
| Industry Game AI | 5 | Neural game engines (GameNGen), world models (Genie 3, Dreamer 4), real-time inference patterns |
| Related Techniques | 7 | Self-imitation, self-play bootstrapping, reward design via VLM, inverse games for imitation |
