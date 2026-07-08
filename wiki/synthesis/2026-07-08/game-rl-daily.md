---
title: "Game RL & Game AI Bot — Daily Paper Digest (July 2026)"
type: synthesis
created: 2026-07-08
updated: 2026-07-08
sources: []
tags: [game-rl, self-play, game-foundation-model, game-benchmark, pcg, multi-agent-rl, world-models, llm-agent]
---

# Game RL & Game AI Bot — Daily Paper Digest

> Sweep of arXiv and recent proceedings (ICLR 2026, ACL 2026, AAAI 2026, AAMAS 2026, ICML 2025, NeurIPS 2025, JMLR 2025) for papers published 2025–2026 on Game RL, Game AI Bots, Foundation Models, PCG, Benchmarks, Industry Game AI, and related techniques.

## 1. Game Reinforcement Learning

### QZero: Model-Free RL Masters Go
- **Authors**: Jingbin Liu, Xuechun Wang
- **Affiliation**: —
- **Venue**: arXiv preprint, Jan 2026
- **Abstract**: Presents QZero, a model-free RL algorithm that forgoes MCTS during training. Uses entropy-regularized Q-learning with a single Q-value network. Trained tabula rasa on 7 GPUs for 5 months, achieving AlphaGo-comparable performance.
- **Key innovation**: First demonstration that model-free RL can master Go at AlphaGo level.
- **Link**: [arXiv:2601.03306](https://arxiv.org/abs/2601.03306)

### Superhuman AI for Generals.io
- **Authors**: Matěj Straka, Viliam Lisý, Martin Schmid
- **Affiliation**: —
- **Venue**: arXiv preprint, Jun 2026
- **Abstract**: Superhuman agent for the imperfect-information RTS game Generals.io using self-play with a JAX-native simulator achieving 10M fps on a single GPU (~10,000× speedup). Vision Transformer policy trained with policy-gradient loop.
- **Key innovation**: JAX-native simulator as data bottleneck solution; top-advantage sample filtering.
- **Link**: [arXiv:2606.23348](https://arxiv.org/abs/2606.23348)

### Regret-Guided Search Control (RGSC) for AlphaZero
- **Authors**: (ICLR 2026 paper)
- **Affiliation**: —
- **Venue**: ICLR 2026
- **Abstract**: Extends AlphaZero with a regret network that identifies high-regret states for replay as starting positions. Outperforms AlphaZero and Go-Exploit by 77 and 89 Elo on 9×9 Go, 10×10 Othello, and 11×11 Hex.
- **Key innovation**: Prioritized regret buffer for search control; improves sample efficiency without extra compute.
- **Link**: [arXiv:2602.20809](https://arxiv.org/abs/2602.20809)

### AlphaZero on Tablut: Self-Play RL for Asymmetric Board Games
- **Authors**: Tõnis (et al.)
- **Affiliation**: —
- **Venue**: arXiv preprint, Apr 2026
- **Abstract**: Adapts AlphaZero to Tablut, an asymmetric game. Uses separate policy/value heads per player role with shared residual trunk and C4 augmentation + larger replay buffer to mitigate catastrophic forgetting.
- **Key innovation**: Demonstrates AlphaZero transfer to asymmetric games with architectural modifications.
- **Link**: [arXiv:2604.05476](https://arxiv.org/abs/2604.05476)

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning
- **Authors**: Lei Zhu, Lutz Güertler, Simon C.H. Yu, Zichen Liu, Penghui Qi, Daniel Balcells, et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Jun 2025
- **Abstract**: Self-play framework for LLMs playing multi-turn zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation). Proposes Role-Conditioned Advantage Estimation (RAE) for multi-agent stability. Up to 10% improvement on 8 reasoning benchmarks.
- **Key innovation**: Zero-sum self-play as autonomous reasoning curriculum for LLMs.
- **Link**: [arXiv:2506.24119](https://arxiv.org/abs/2506.24119)

### Stratagem: Learning Transferable Reasoning via Game Self-Play
- **Authors**: Xiachong Feng, Deyi Yin, Xiaocheng Feng, Yi Jiang, Libo Qin, Yangfan Ye, et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Apr 2026
- **Abstract**: Self-play framework using Reasoning Transferability Coefficient and Reasoning Evolution Reward to distinguish transferable reasoning from game-specific heuristics. Gains on math, general reasoning, and code benchmarks.
- **Key innovation**: Separates transferable reasoning patterns from game-specific heuristics in self-play.
- **Link**: [arXiv:2604.17696](https://arxiv.org/abs/2604.17696)

### Generative Code Optimization for Atari
- **Authors**: Zhiyi Kuang, Ryan Rong, YuCheng Yuan, Allen Nie
- **Affiliation**: —
- **Venue**: arXiv preprint, Aug 2025
- **Abstract**: Policies represented as Python programs refined by LLMs via execution traces and natural language feedback. Competitive with deep RL on Atari with far fewer environment interactions.
- **Key innovation**: Programmatic policy representation enabling LLM-based self-improvement.
- **Link**: [arXiv:2508.19506](https://arxiv.org/abs/2508.19506)

### GAE Falls Short in Imperfect-Information Self-Play
- **Authors**: Zhiyuan Fan, Gabriele Farina
- **Affiliation**: MIT
- **Venue**: arXiv preprint, May 2026
- **Abstract**: Identifies GAE variance issues in self-play RL for imperfect-information games. Proposes Q-boosting and Variance-Reduced Policy Optimization (VRPO) using multi-step Expected SARSA(λ). Strong results on Dou Dizhu and HUNL Texas Hold'em.
- **Key innovation**: Variance-reduced advantage estimator for equilibrium self-play.
- **Link**: [arXiv:2605.19235](https://arxiv.org/abs/2605.19235)

### GFXP: Learning Global Nash Equilibrium in Team Competitive Games
- **Authors**: (JMLR 2025)
- **Affiliation**: —
- **Venue**: JMLR 2025 (Volume 26)
- **Abstract**: Generalized Fictitious Cross-Play (GFXP) combines self-play main policy with counter population training. Achieves lowest exploitabilities in matrix games and gridworlds; >94% win rate against SOTA in football game.
- **Key innovation**: Hybrid of self-play and Policy-Space Response Oracles for team competitive games.
- **Link**: [JMLR 26(44)](https://jmlr.org/beta/papers/v26/24-1503.html)

## 2. Multi-Agent RL in Games

### MARL-GPT: Foundation Model for Multi-Agent RL
- **Authors**: Maria Nesterova, Mikhail Kolosov, Anton Andreychuk, Egor Cherepanov, Oleg Bulichev, Alexey Kovalev, Konstantin Yakovlev, Aleksandr Panov, Alexey Skrynnik
- **Affiliation**: AXXX, MIRAI, Innopolis University, SPbU
- **Venue**: AAAI 2026 / AAMAS 2026
- **Abstract**: Single GPT-based model trained on expert trajectories (400M SMACv2, 100M GRF, 1B POGEMA) via offline RL. Single transformer-based observation encoder with no task-specific tuning. Competitive with specialized baselines across all three environments.
- **Key innovation**: First multi-task, multi-environment MARL foundation model.
- **Link**: [arXiv:2604.05943](https://arxiv.org/abs/2604.05943)

### SHPPO: Heterogeneous MARL for Zero-Shot Scalable Collaboration
- **Authors**: (Multiple)
- **Affiliation**: —
- **Venue**: Neurocomputing, Oct 2025
- **Abstract**: Latent network learns strategy patterns per agent; heterogeneous layer generates parameters for decision networks. Achieves zero-shot scalability to unseen agent counts in SMAC and GRF.
- **Key innovation**: Inter-individual + temporal heterogeneity via latent variables in parameter-shared MARL.
- **Link**: [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0925231225013888)

### HLSMAC: High-Level Strategic StarCraft Multi-Agent Challenge
- **Authors**: Xiaoyu Hong, Yungong Wang, D. P. Jin, Ye Yuan, Ximin Huang, Zijian Wu, et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Sep 2025
- **Abstract**: 12 StarCraft II scenarios based on classical stratagems (Thirty-Six Stratagems). Tests tactical maneuvering, timing coordination, and deception. Integrates MARL algorithms and LLM-based agents.
- **Key innovation**: New benchmark for high-level strategic decision-making beyond micromanagement.
- **Link**: [arXiv:2509.12927](https://arxiv.org/abs/2509.12927)

### MARSHAL: Multi-Agent Reasoning via Self-Play with Strategic LLMs
- **Authors**: Hui Yuan, Zhe Xu, Zhen Tan, Xianhao Yi, Guang Mo, Kaiwen Long, et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Oct 2025
- **Abstract**: Turn-level advantage estimator + agent-specific advantage normalization for multi-agent RL in cooperative/competitive games. Up to 28.7% improvement in held-out games; zero-shot gains on AIME, GPQA-Diamond.
- **Key innovation**: Self-play in strategic games generalizes to multi-agent reasoning benchmarks.
- **Link**: [arXiv:2510.15414](https://arxiv.org/abs/2510.15414)

## 3. Game AI Bot — LLM-Powered Game Agents

### Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games
- **Authors**: (Multiple)
- **Affiliation**: —
- **Venue**: arXiv preprint, May 2026
- **Abstract**: PPO with lightweight turn-level critic for VLM fine-tuning on Super Mario Land (>100 turns per episode). At least 3× game progress improvement over frontier models. Open training framework.
- **Key innovation**: Stable long-horizon RL for VLM game agents; critic design matters more than complex RL.
- **Link**: [arXiv:2605.00347](https://arxiv.org/abs/2605.00347)

### AVA: Attentive VLM Agent for Mastering StarCraft II
- **Authors**: Weiyu Ma, Yuqian Fu, Zecheng Zhang, Bernard Ghanem, Guohao Li
- **Affiliation**: —
- **Venue**: ACL 2026 Findings
- **Abstract**: AVACraft — multimodal benchmark for StarCraft II supporting both MARL and VLM paradigms. VLMs achieve 75–81% zero-shot win rate vs 27.1% for MARL after 1M steps. Key trade-offs between training efficiency and interpretability.
- **Key innovation**: First multimodal SC2 benchmark comparing MARL and VLM approaches.
- **Link**: [ACL 2026](https://aclanthology.org/2026.findings-acl.208/)

### Nemobot: LLM-Powered Game Agents Framework
- **Authors**: (Multiple)
- **Affiliation**: —
- **Venue**: arXiv preprint, Apr 2026
- **Abstract**: Extends Shannon's taxonomy of game-playing machines with LLMs. Interactive agentic engineering environment for creating, customizing, and deploying LLM game agents across four game classes.
- **Key innovation**: Programmable prompt engineering + crowdsourced strategy refinement for game AI education.
- **Link**: [arXiv:2604.21896](https://arxiv.org/abs/2604.21896)

### Sensi: Curriculum-Based Test-Time Learning for LLM Game Agents
- **Authors**: Mohsen Arjmandi
- **Affiliation**: —
- **Venue**: arXiv preprint, Mar 2026
- **Abstract**: Two-player architecture (Observer + Actor) with curriculum learning, database-as-control-plane, and LLM-as-judge. Achieves 50–94× sample efficiency on ARC-AGI-3 (32 vs 1,600–3,000 attempts).
- **Key innovation**: Structured test-time learning with curriculum state machine for LLM agents.
- **Link**: [arXiv:2603.17683](https://arxiv.org/abs/2603.17683)

### AdaMARP: Adaptive Multi-Agent Role-Playing Framework
- **Authors**: Zhenhua Xu, Dongsheng Chen, Shuo Wang, Jian Li, Chengjie Wang, Meng Han, et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Jan 2026
- **Abstract**: Immersive message format interleaving [Thought], (Action), and Speech with explicit Scene Manager. 8B actor outperforms several commercial LLMs; 14B surpasses Claude Sonnet 4.5 with AdaSMSet.
- **Key innovation**: Adaptive scene orchestration for LLM role-playing in games.
- **Link**: [arXiv:2601.11007](https://arxiv.org/abs/2601.11007)

### Psy-CoT & RAPO: Improving General Role-Playing Agents
- **Authors**: (Multiple)
- **Affiliation**: —
- **Venue**: arXiv preprint, Jun 2026
- **Abstract**: Psychology-grounded chain-of-thought (Interaction Perception, Psychological Empathy, Logical Construction) + Role-Aware Policy Optimization using profile-token mutual information. Outperforms GRPO on CoSER, CharacterBench, CharacterEval.
- **Key innovation**: Psychology-grounded reasoning + asymmetric gradient weighting for role fidelity.
- **Link**: [arXiv:2606.27025](https://arxiv.org/abs/2606.27025)

### Bounded Autonomy: LLM Characters in Live Multiplayer Games
- **Authors**: (Multiple)
- **Affiliation**: —
- **Venue**: arXiv preprint, Apr 2026
- **Abstract**: Control architecture for LLM characters with agent-agent interaction (reply-chain decay), agent-world action grounding, and player-agent steering (whisper). Deployed in a live multiplayer social game.
- **Key innovation**: Bounded autonomy framework balancing open-ended behavior with executability and steerability.
- **Link**: [arXiv:2604.04703](https://arxiv.org/abs/2604.04703)

### Leveraging LLM Agents for Automated Video Game Testing
- **Authors**: (Multiple)
- **Affiliation**: —
- **Venue**: arXiv preprint, Sep 2025
- **Abstract**: LLM agents for automated game testing, achieving high state coverage in rich open-ended environments.
- **Key innovation**: LLM-driven exploration for game QA automation.
- **Link**: [arXiv:2509.22170](https://arxiv.org/abs/2509.22170)

## 4. Game Foundation Models

### NitroGen: Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi "Jim" Fan
- **Affiliation**: NVIDIA, MineDojo
- **Venue**: arXiv preprint, Jan 2026
- **Abstract**: Vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games. Automatic action extraction from public videos. Up to 52% relative improvement on unseen games.
- **Key innovation**: Internet-scale video-action dataset + multi-game benchmark for generalist game agents.
- **Link**: [arXiv:2601.02427](https://arxiv.org/abs/2601.02427)

### Game-TARS: Pretrained Foundation Model for Generalist Game Agents
- **Authors**: Zihao Wang, Xujing Li, Yining Ye, Junjie Fang, Haoming Wang, Longxiang Liu, et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Oct 2025
- **Abstract**: Unified keyboard-mouse action space pre-trained on 500B+ tokens across OS, web, and games. 2× SOTA success rate on Minecraft. Outperforms GPT-5, Gemini-2.5-Pro, Claude-4-Sonnet on FPS benchmarks.
- **Key innovation**: Decaying continual loss + Sparse-Thinking for scalable generalist game agents.
- **Link**: [arXiv:2510.23691](https://arxiv.org/abs/2510.23691)

### Pixels2Play (P2P): Open Model for Real-Time 3D Gameplay
- **Authors**: Yuguang Yue, Irakli Salia, Samuel Hunt, Chris Green, Wenzhe Shi, Jonathan J. Hunt
- **Affiliation**: —
- **Venue**: arXiv preprint, Aug 2025
- **Abstract**: Decoder-only transformer trained via behavior cloning on 8,300+ hours of human gameplay. Real-time inference on consumer GPU (RTX 5090). Studies scaling laws of BC and causality.
- **Key innovation**: Open recipe for real-time game-playing foundation model; scaling improves causal reasoning.
- **Link**: [arXiv:2508.14295](https://arxiv.org/abs/2508.14295)

### Scaling Behavior Cloning Improves Causal Reasoning
- **Authors**: Yuguang Yue, Irakli Salia, Samuel Hunt, Chris Green, Wenzhe Shi, Jonathan J. Hunt
- **Affiliation**: —
- **Venue**: arXiv preprint, Jan 2026
- **Abstract**: Extends P2P with text-conditioned policy; releases 8,300+ hours of annotated gameplay. Shows scaling model/data improves causal policy learning in games.
- **Key innovation**: Systematic scaling law analysis for behavior cloning in games; open dataset release.
- **Link**: [arXiv:2601.04575](https://arxiv.org/abs/2601.04575)

### Lumine: Open Recipe for Generalist Agents in 3D Open Worlds
- **Authors**: Weihao Tan, Xiangyang Li, Yunhao Fang, Heyuan Yao, Shi Yan, Hao Luo, et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Nov 2025
- **Abstract**: VLM-based agent processing raw pixels at 5 Hz producing 30 Hz keyboard-mouse actions. Completes 5-hour Genshin Impact storyline at human level. Zero-shot generalization to Wuthering Waves and Honkai: Star Rail.
- **Key innovation**: Human-like interaction paradigm with adaptive reasoning frequency.
- **Link**: [arXiv:2511.08892](https://arxiv.org/abs/2511.08892)

### GameVerse: Can VLMs Learn from Video-Based Reflection?
- **Authors**: Kuan Zhang, Dongchen Liu, Qiyue Zhao, Jinkun Hou, Xinran Zhang, Qinlei Xie, et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Mar 2026
- **Abstract**: Reflect-and-retry paradigm for VLMs to internalize visual experience from gameplay. Taxonomy spanning 15 games; training-free analogue to RL+SFT using failure trajectories + expert tutorials.
- **Key innovation**: Video-based reflection as training-free policy improvement for VLMs.
- **Link**: [arXiv:2603.06656](https://arxiv.org/abs/2603.06656)

### Towards Generalist Game Players: A Survey
- **Authors**: Kuan Zhang, Dongchen Liu, Qiyue Zhao, Tianyu Xin, Yue Su, Haisheng Wang, et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, May 2026
- **Abstract**: Comprehensive survey tracing four eras of game AI: symbolic, RL, foundation model, and creator. Analyzes five fundamental trade-offs across Dataset, Model, Harness, and Benchmark pillars.
- **Key innovation**: Unified lens and five-level roadmap toward omnipotent generalist game agents.
- **Link**: [arXiv:2605.09965](https://arxiv.org/abs/2605.09965)

### OpenGame: Open Agentic Coding for Games
- **Authors**: Yilei Jiang, Jinyuan Hu, Qianyin Xiao, Yaozhi Zheng, Ruize Ma, Kaituo Feng, et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Apr 2026
- **Abstract**: GameCoder-27B code LLM for end-to-end web game generation. Template Skill + Debug Skill for cross-file consistency. OpenGame-Bench for evaluating generated games via headless browser + VLM judging.
- **Key innovation**: First open-source agentic framework for end-to-end game creation with execution-grounded RL.
- **Link**: [arXiv:2604.18394](https://arxiv.org/abs/2604.18394)

## 5. World Models for Games

### Dreamer 4: Training Agents Inside Scalable World Models
- **Authors**: Danijar Hafner, Wilson Yan, Timothy Lillicrap
- **Affiliation**: —
- **Venue**: arXiv preprint, Sep 2025 (Nature 2025)
- **Abstract**: Scalable agent that learns to solve control tasks via RL inside a fast, accurate world model. 88+ citations.
- **Key innovation**: Continues the Dreamer lineage; practical world model-based RL at scale.
- **Link**: [arXiv:2509.24527](https://arxiv.org/abs/2509.24527)

### NE-Dreamer: Next Embedding Prediction for World Models
- **Authors**: George Bredis, Nikita Balagansky, Daniil Gavrilov, Ruslan Rakhimov
- **Affiliation**: —
- **Venue**: arXiv preprint, Mar 2026
- **Abstract**: Decoder-free MBRL agent using temporal transformer to predict next encoder embeddings. Matches DreamerV3 on DMControl; substantial gains on DMLab memory/navigation tasks.
- **Key innovation**: Next-embedding prediction replaces pixel reconstruction for world model learning.
- **Link**: [arXiv:2603.02765](https://arxiv.org/abs/2603.02765)

### R2-Dreamer: Redundancy-Reduced World Models (ICLR 2026)
- **Authors**: Naoki Morihira, Amal Nahar, Kartik Bharadwaj, Yasuhiro Kato, Akinobu Hayashi, Tatsuya Harada
- **Affiliation**: Honda R&D, University of Tokyo, RIKEN AIP
- **Venue**: ICLR 2026
- **Abstract**: Decoder-free MBRL with redundancy-reduction objective (Barlow Twins-style). 1.59× faster than DreamerV3. Strong on DMC-Subtle with tiny task-relevant objects.
- **Key innovation**: Internal regularizer replaces data augmentation for decoder-free world models.
- **Link**: [arXiv:2603.18202](https://arxiv.org/abs/2603.18202)

### World-Action Model (WAM)
- **Authors**: (Multiple)
- **Affiliation**: —
- **Venue**: arXiv preprint, Mar 2026
- **Abstract**: Action-regularized world model with inverse dynamics objective in DreamerV2. Improves BC success from 59.4% to 71.2% and PPO fine-tuning to 92.8% on CALVIN.
- **Key innovation**: Jointly reasoning over future observations and actions with inverse dynamics.
- **Link**: [arXiv:2603.28955](https://arxiv.org/abs/2603.28955)

### Dreamer-CDP: Reconstruction-Free World Models
- **Authors**: Michael Hauri, Friedemann Zenke
- **Affiliation**: —
- **Venue**: arXiv preprint, Mar 2026
- **Abstract**: JEPA-style predictor on continuous deterministic representations. Matches DreamerV3 on Crafter without reconstruction. Identifies CDP as essential for reconstruction-free world models.
- **Key innovation**: Continuous Deterministic Representation Prediction closes gap between Dreamer and reconstruction-free methods.
- **Link**: [arXiv:2603.07083](https://arxiv.org/abs/2603.07083)

### ARROW: Augmented Replay for Robust World Models
- **Authors**: Abdulaziz Alyahya, Abdallah Al Siyabi, Markus Ernst, Luke Yang, Levin Kuhlmann, Gideon Kowadlo
- **Affiliation**: —
- **Venue**: arXiv preprint, Mar 2026
- **Abstract**: Model-based continual RL extending DreamerV3 with short-term + long-term distribution-matching replay. Less forgetting on Atari; maintained forward transfer on Procgen.
- **Key innovation**: Bio-inspired dual-buffer replay for continual RL in world models.
- **Link**: [arXiv:2603.11395](https://arxiv.org/abs/2603.11395)

### Optimistic World Models (OWMs)
- **Authors**: Akshay Mete, Shahid Aamir Sheikh, Tzu-Hsiang Lin, Dileep Kalathil, P. R. Kumar
- **Affiliation**: Texas A&M University
- **Venue**: arXiv preprint, Feb 2026
- **Abstract**: Reward-biased maximum likelihood estimation (RBMLE) for optimistic exploration in world models. O-DreamerV3 and O-STORM show significant gains on sparse-reward Atari (Montezuma's Revenge, Private Eye).
- **Key innovation**: Fully gradient-based optimistic dynamics loss for exploration without uncertainty estimates.
- **Link**: [arXiv:2602.10044](https://arxiv.org/abs/2602.10044)

### ResDreamer: Hierarchical Visual Reasoning World Model
- **Authors**: Yuanfei Xu, Lin Liu, Wengang Zhou, Mingxiao Feng, Houqiang Li
- **Affiliation**: —
- **Venue**: arXiv preprint, May 2026
- **Abstract**: Hierarchical world model where each layer reconstructs residuals of the layer below. SOTA sample/parameter efficiency in 3D open-world environments.
- **Key innovation**: Self-supervised hierarchical residual learning for world model reasoning.
- **Link**: [arXiv:2605.17537](https://arxiv.org/abs/2605.17537)

### RAW-Dream: Reinforcing VLAs in Task-Agnostic World Models
- **Authors**: Yucen Wang, Rui Yu, Fengming Zhang, Junjie Lu, Xinyao Qin, Tianxiang Zhang, et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, May 2026
- **Abstract**: Task-agnostic world model pre-trained on diverse behaviors + off-the-shelf VLM for reward generation. Dual-noise verification for hallucination filtering. Zero-shot VLA fine-tuning.
- **Key innovation**: Completely disentangles world model learning from downstream tasks.
- **Link**: [arXiv:2605.12334](https://arxiv.org/abs/2605.12334)

### Matrix-Game 3.0: Real-Time Streaming Interactive World Model
- **Authors**: Zile Wang, Zexiang Liu, Jaixing Li, Kaichen Huang, Baixin Xu, Fei Kang, et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Apr 2026
- **Abstract**: Memory-augmented interactive world model for 720p real-time (40 FPS) long-form video generation. Multi-segment autoregressive DMD distillation with camera-aware memory retrieval.
- **Key innovation**: Industrial-scale world model with minute-long memory consistency at 720p 40 FPS.
- **Link**: [arXiv:2604.08995](https://arxiv.org/abs/2604.08995)

### Matrix-Game 2.0
- **Authors**: Y. Zhang, C. Peng, B. Wang, P. Wang, Q. Zhu, F. Kang, B. Jiang, Z. Gao, E. Li, Y. Liu, Y. Zhou
- **Affiliation**: —
- **Venue**: arXiv preprint, Aug 2025
- **Abstract**: Open-source real-time interactive world model achieving 25 FPS generation via auto-regressive diffusion. Unreal Engine + GTA5 data pipeline produces 1,200 hours of action-annotated video.
- **Key innovation**: Self-Forcing distillation for real-time interactive video generation.
- **Link**: [arXiv:2508.13009](https://arxiv.org/abs/2508.13009)

## 6. Procedural Content Generation

### IPCGRL: Language-Instructed RL for Procedural Level Generation
- **Authors**: In-Chang Baek, Sunghyun Kim, Seo-Young Lee, Dong-Hyeon Kim, Kyung-Joong Kim
- **Affiliation**: —
- **Venue**: arXiv preprint, Mar 2025
- **Abstract**: Sentence embedding fine-tuning for instruction-based PCGRL. Up to 21.4% improvement in controllability and 17.2% in generalizability for unseen instructions.
- **Key innovation**: Text-based instruction fusion with RL for PCG.
- **Link**: [arXiv:2503.12358](https://arxiv.org/abs/2503.12358)

### VIPCGRL: Human-Aligned PCGRL via Text-Level-Sketch Shared Representation
- **Authors**: In-Chang Baek, Seoyoung Lee, Sung-Hyun Kim, Geumhwan Hwang, Kyung-Joong Kim
- **Affiliation**: —
- **Venue**: arXiv preprint, Aug 2025
- **Abstract**: Three-modality (text, level, sketch) shared embedding via quadruple contrastive learning. Human-likeness validated by both metrics and human evaluation.
- **Key innovation**: Multi-modal human-aligned PCGRL with contrastive cross-modality learning.
- **Link**: [arXiv:2508.09860](https://arxiv.org/abs/2508.09860)

### Multiverse: Language-Conditioned Multi-Game Level Blending
- **Authors**: In-Chang Baek, Jiyun Jung, Geum-Hwan Hwang, Sung-Hyun Kim, Kyung-Joong Kim
- **Affiliation**: —
- **Venue**: arXiv preprint, Mar 2026
- **Abstract**: Shared latent space aligning text instructions and level structures across games. Threshold-based multi-positive contrastive supervision for cross-game level blending.
- **Key innovation**: First language-conditioned multi-game level blending framework.
- **Link**: [arXiv:2603.26782](https://arxiv.org/abs/2603.26782)

### PCGRLLM: LLM-Driven Reward Design for PCGRL
- **Authors**: In-Chang Baek, Sunghyun Kim, Sam Earle, Zehua Jiang, Noh Jin-Ha, Julian Togelius, et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Feb 2025
- **Abstract**: LLM generates reward functions for PCGRL agents. Feedback mechanism + reasoning-based prompt engineering. 415% and 40% performance improvements depending on LLM.
- **Key innovation**: Automated reward design for PCG via LLM reasoning.
- **Link**: [arXiv:2502.10906](https://arxiv.org/abs/2502.10906)

### CreativeGame: Mechanic-Aware Creative Game Generation
- **Authors**: Hongnan Ma, Han Wang, Shenglin Wang, Tieyue Yin, Yiwei Shi, Yucong Huang, et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Apr 2026
- **Abstract**: Multi-agent system for iterative HTML5 game generation with proxy reward, lineage-scoped memory, runtime validation, and mechanic-guided planning. 71 stored lineages, 774-entry global mechanic archive.
- **Key innovation**: Mechanic-as-explicit-object paradigm for interpretable game evolution.
- **Link**: [arXiv:2604.19926](https://arxiv.org/abs/2604.19926)

### Learning Local Constraints for RL Content Generators
- **Authors**: (Multiple)
- **Affiliation**: —
- **Venue**: arXiv preprint, May 2026
- **Abstract**: Combines Wave Function Collapse (WFC) with PCGRL by constraining RL action space with WFC-learned local patterns. Generates playable, visually satisfying Lode Runner levels.
- **Key innovation**: Hybrid WFC-RL method combining local constraint learning with global property optimization.
- **Link**: [arXiv:2605.13570](https://arxiv.org/abs/2605.13570)

### Word2Minecraft: LLM 3D Game Level Generation
- **Authors**: Shuo Huang, Muhammad Umair Nasir, Steven James, Julian Togelius
- **Affiliation**: —
- **Venue**: arXiv preprint, Mar 2025
- **Abstract**: Transforms narrative elements into playable Minecraft levels. Scaling algorithm for spatial consistency. GPT-4-Turbo excels at story coherence.
- **Key innovation**: Structured story-to-3D-level pipeline using LLMs.
- **Link**: [arXiv:2503.16536](https://arxiv.org/abs/2503.16536)

### HDPCG: High-Dimensional Procedural Content Generation
- **Authors**: (Multiple)
- **Affiliation**: —
- **Venue**: arXiv preprint, Feb 2026
- **Abstract**: Elevates non-geometric gameplay dimensions (time, layers) to first-class coordinates. Direction-Space and Direction-Time with validation on gravity-flip and parallel-timeline puzzles in Unity.
- **Key innovation**: Formal framework for PCG beyond geometry into mechanism-aware generation.
- **Link**: [arXiv:2602.18943](https://arxiv.org/abs/2602.18943)

### Word2World: Generating Stories and Worlds through LLMs
- **Authors**: Muhammad Umair Nasir, Steven James, Julian Togelius
- **Affiliation**: —
- **Venue**: arXiv preprint, May 2024
- **Abstract**: Zero-shot LLM-based generation of playable 2D games from stories via two-step tile placement and A*-based evaluation.
- **Key innovation**: Zero-shot story-to-playable-game pipeline; LLM as both generator and evaluator.
- **Link**: [arXiv:2405.06686](https://arxiv.org/abs/2405.06686)

### SLMs for Dynamic Game Content Generation
- **Authors**: (Multiple)
- **Affiliation**: —
- **Venue**: arXiv preprint, Jan 2026
- **Abstract**: Aggressive fine-tuning of SLMs on scoped tasks with synthetic DAG-based data. Retry-until-success achieves adequate quality for real-time generation. Practical alternative to cloud-dependent LLMs.
- **Key innovation**: Practical SLM-based agentic networks for local game content generation.
- **Link**: [arXiv:2601.23206](https://arxiv.org/abs/2601.23206)

### DRL for Procedural Level Design
- **Authors**: Murat Özkan
- **Affiliation**: —
- **Venue**: arXiv preprint, Oct 2025
- **Abstract**: Dual-agent system in Unity: hummingbird (solver) + floating island (generator). Both trained with PPO. Emergent co-adaptive behavior.
- **Key innovation**: Co-evolution of level generator and player agent in 3D.
- **Link**: [arXiv:2510.15120](https://arxiv.org/abs/2510.15120)

## 7. Game Benchmarks

### OmniGameArena: Unified UE5 Benchmark for VLM Game Agents
- **Authors**: Mingxian Lin, Shengju Qian, Yuqi Liu, Yi-Hua Huang, Yiyu Wang, Wei Huang, et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Jun 2026
- **Abstract**: 12 Unreal Engine 5 games (Solo, PvP, Coop) with Improvement Dynamics Curve (IDC). Evaluates 12 VLM agents on cold-start + reflection-based improvement.
- **Key innovation**: Improvement Dynamics measures how agents learn from self-reflection across rounds.
- **Link**: [arXiv:2606.09826](https://arxiv.org/abs/2606.09826)

### GameWorld: Standardized Evaluation of Multimodal Game Agents
- **Authors**: Mingyu Ouyang, Siyuan Hu, Kevin Qinghong Lin, Hwee Tou Ng, Mike Zheng Shou
- **Affiliation**: —
- **Venue**: arXiv preprint, Apr 2026
- **Abstract**: 34 browser games, 170 tasks, state-verifiable evaluation. Supports Computer-Use Agents and Generalist Agents. 18 model-interface pairs evaluated. Sandbox decouples inference latency from gameplay.
- **Key innovation**: State-verifiable outcome-based evaluation; repeated full-benchmark robustness studies.
- **Link**: [arXiv:2604.07429](https://arxiv.org/abs/2604.07429)

### Orak: Foundational Benchmark for LLM Agents on Video Games
- **Authors**: Dongmin Park, Minkyu Kim, Beongjun Choi, Junhyuck Kim, Keon Lee, Jonghyun Lee, et al.
- **Affiliation**: KRAFTON
- **Venue**: arXiv preprint, Jun 2025
- **Abstract**: 12 popular video games across all major genres. MCP-based plug-and-play interface. Fine-tuning dataset with 10k gameplay trajectories. Battle arena for LLM vs LLM evaluation.
- **Key innovation**: Comprehensive LLM game benchmark with MCP integration and fine-tuning dataset.
- **Link**: [arXiv:2506.03610](https://arxiv.org/abs/2506.03610)

### lmgame-Bench: How Good are LLMs at Playing Games?
- **Authors**: Lanxiang Hu, Ming Huo, Yuxuan Zhang, Hongwen Yu, Eric P. Xing, Ion Stoica, et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, May 2025
- **Abstract**: 6 games with Gym-style API + perception/memory scaffolds. Addresses brittle vision, prompt sensitivity, data contamination. RL on a single game transfers to unseen games and planning tasks.
- **Key innovation**: Principled mitigation of contamination and prompt variance in game-based LLM evaluation.
- **Link**: [arXiv:2505.15146](https://arxiv.org/abs/2505.15146)

### AI Gamestore: Open-Ended Evaluation of Machine General Intelligence
- **Authors**: Lance Ying, Ryan Truong, Prafull Sharma, Kun Zhao, Nathan Cloos, Kelsey R. Allen, et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Feb 2026
- **Abstract**: LLM-based procedural generation of games from App Store/Steam top charts. 100 games; best VLMs achieve <10% human average score. World-model learning, memory, and planning gaps identified.
- **Key innovation**: Living benchmark of human games sourced from real digital marketplaces.
- **Link**: [arXiv:2602.17594](https://arxiv.org/abs/2602.17594)

### V-MAGE: Vision-Centric Game Evaluation for MLLMs
- **Authors**: (Multiple)
- **Affiliation**: —
- **Venue**: ACL 2026 Findings
- **Abstract**: Five games with 30+ scenarios; dynamic ELO ranking. Models approach human on simple tasks but drop on complex reasoning scenarios.
- **Key innovation**: Frame-by-frame interactive evaluation focusing on vision-centric capabilities.
- **Link**: [ACL 2026 Findings](https://aclanthology.org/2026.findings-acl.878.pdf)

### HLSMAC: High-Level Strategic StarCraft Multi-Agent Challenge
- **(See Section 2 above)**

## 8. Self-Play & Related Techniques

### PopuLoRA: Co-Evolving LLM Populations for Reasoning Self-Play
- **Authors**: Roger Creus Castanyer, Geoffrey Bradway, Lorenz Wolf, Maxwill Lin, Augustine N. Mavor-Parker, Matthew James Sargent
- **Affiliation**: —
- **Venue**: arXiv preprint, May 2026
- **Abstract**: Teacher-student LoRA populations on shared frozen base. Weight-space evolution operators (mutations, crossovers) create population members in seconds. Teachers and students co-evolve in asymmetric arms race.
- **Key innovation**: Population-based asymmetric self-play with LoRA evolution operators at 7B scale.
- **Link**: [arXiv:2605.16727](https://arxiv.org/abs/2605.16727)

### Foundation Model Self-Play (FMSP)
- **Authors**: Aaron Dharna, Cong Lu, Jeff Clune
- **Affiliation**: —
- **Venue**: arXiv preprint, Jul 2025
- **Abstract**: Uses FM code generation to leap across local optima in policy space. Quality-Diversity Self-Play (QDSP) produces diverse high-quality policies. Validated in Car Tag and Gandalf (LLM safety).
- **Key innovation**: Foundation model code generation for creative strategy discovery in self-play.
- **Link**: [arXiv:2507.06466](https://arxiv.org/abs/2507.06466)

### SeRL: Self-Play RL for LLMs with Limited Data
- **Authors**: Wenkai Fang, Shunyu Liu, Zhou Yang, Kongcheng Zhang, Tongya Zheng, Kaixuan Chen, et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, May 2025
- **Abstract**: Self-instruction + self-rewarding modules bootstrap LLM training with minimal initial data. Majority-voting reward estimation. On par with high-quality data + verifiable rewards.
- **Key innovation**: Closed-loop self-play without external data or reward annotations.
- **Link**: [arXiv:2505.20347](https://arxiv.org/abs/2505.20347)

### Reasonably Reasoning AI Agents Avoid Game-Theoretic Failures
- **Authors**: Enoch Hyunwook Kang
- **Affiliation**: —
- **Venue**: arXiv preprint, Mar 2026
- **Abstract**: Proves that off-the-shelf reasoning AI agents can achieve Nash-like play zero-shot. Relaxes common-knowledge payoff assumption. Validated in repeated prisoner's dilemma and marketing games.
- **Key innovation**: Theoretical guarantee that reasoning agents converge to equilibrium without explicit post-training.
- **Link**: [arXiv:2603.18563](https://arxiv.org/abs/2603.18563)

### DEDA-FP: Solving Continuous Mean Field Games (NeurIPS 2025)
- **Authors**: (Multiple)
- **Affiliation**: —
- **Venue**: NeurIPS 2025
- **Abstract**: First DRL method to simultaneously learn Nash equilibrium policies and population distributions in non-stationary MFGs with continuous spaces. 10× sampling efficiency.
- **Key innovation**: Conditional Normalizing Flow for population distribution + deep RL + fictitious play.
- **Link**: [arXiv:2510.22158](https://arxiv.org/abs/2510.22158)

### Model-Free Learning in Dynamic Population Games
- **Authors**: (Multiple)
- **Affiliation**: —
- **Venue**: arXiv preprint, May 2026
- **Abstract**: DQN with fictitious play for Karma economies. Suboptimality bound of O(1/√Ns) + O(1/N). From-scratch equilibrium learning via smoothed policy iteration.
- **Key innovation**: First model-free equilibrium learning for dynamic population games.
- **Link**: [arXiv:2605.11042](https://arxiv.org/abs/2605.11042)

## 9. Industry Game AI

### KRAFTON AI at ICML 2026: Three Fronts for Game AI
- **Authors**: KRAFTON CAIO Lee Kang-wook (presentation)
- **Affiliation**: KRAFTON
- **Venue**: ICML 2026 AI for Games Social Event
- **Abstract**: Three fronts: (1) in-game AI agents (PUBG ALLIE — LLM teammate with 3-layer memory), (2) interactive world models as potential game engine alternatives, (3) production AI for pipeline transformation. ~150-person AI research org.
- **Key innovation**: Commercial deployment of LLM game agent (ALLIE) with low-latency teamplay. Coachable agents for QA (Horizon Forbidden West).
- **Link**: [Inven Global Article](https://www.invenglobal.com/articles/23482/ai-for-games-krafton-highlights-three-fronts)

### GT Sophy: Sony AI's Commercial RL Agent
- **Authors**: Peter Stone (presentation)
- **Affiliation**: Sony AI
- **Venue**: ICML 2026 AI for Games
- **Abstract**: GT Sophy integrated into Gran Turismo 7 for PS5 (Fall 2023) — world's largest commercial deployment of end-to-end RL agent. New: coachable agent for Horizon Forbidden West with style-adjustable slider.
- **Key innovation**: Commercial RL agent deployed to millions; single policy handles diverse playstyles.
- **Link**: ICML 2026 presentation

### Microsoft Research Game Intelligence: WHAM and Data-Efficient Agents
- **Authors**: Lukas Schäfer (presentation)
- **Affiliation**: Microsoft Research
- **Venue**: ICML 2026 AI for Games
- **Abstract**: WHAM (World and Human Action Model) published in Nature 2025. Agent learns from 10–15 human demos; 30ms action prediction for real-time 30 FPS play overcoming network latency.
- **Key innovation**: Extreme data efficiency (10–15 demos) + real-time remote inference.
- **Link**: ICML 2026 presentation

### NC AI: Generative AI for Game Production
- **Authors**: Kim Min-jae (presentation)
- **Affiliation**: NC AI (NCSoft)
- **Venue**: ICML 2026 AI for Games
- **Abstract**: Deep integration of text/image gen AI in planning and concept art. Proprietary tools for 3D mesh, texture, sound generation. Localization tool for multilingual voice + lip-sync. Monkey Test agents for QA automation.
- **Key innovation**: Practical deployment of generative AI across full game production pipeline.
- **Link**: ICML 2026 presentation

### AI Native Games: A Survey and Roadmap
- **Authors**: (Multiple)
- **Affiliation**: —
- **Venue**: arXiv preprint, Jul 2026
- **Abstract**: Defines AI-native games by counterfactual criterion (core loop collapses without generative AI). Analyzes 53 artifacts. G/N taxonomy. Roadmap for controllable generation, AI-as-mechanic, inference economics.
- **Key innovation**: Rigorous definition and comprehensive corpus of AI-native games.
- **Link**: [arXiv:2607.00527](https://arxiv.org/abs/2607.00527)

### MultiGen: Level-Design for Editable Multiplayer Worlds in Diffusion Game Engines
- **Authors**: (Multiple)
- **Affiliation**: —
- **Venue**: arXiv preprint, Mar 2026
- **Abstract**: External persistent memory for diffusion game engines enabling user-editable environments and real-time multiplayer rollouts with coherent viewpoints.
- **Key innovation**: Editable memory representation for generative game engines.
- **Link**: [arXiv:2603.06679](https://arxiv.org/abs/2603.06679)

## 10. Orchestrated Game Worlds

### Orchestrated Reality: LLM-Driven World Simulation as POMDP
- **Authors**: Y Huang, Chenmiao Li, Chaowei Fang
- **Affiliation**: —
- **Venue**: arXiv preprint, Jun 2026
- **Abstract**: Formalizes LLM-driven game worlds as Parameterized-Action POMDP with Plan-Diff-Validate-Apply pipeline. Singleton orchestration agent (Game Master). JSON state tree with schema-validated deltas.
- **Key innovation**: Formal model for LLM-driven world simulation with verifiable state transitions.
- **Link**: [arXiv:2606.16014](https://arxiv.org/abs/2606.16014)

---

*Collected 2026-07-08. Papers span 2024–2026 with emphasis on 2025–2026.*
