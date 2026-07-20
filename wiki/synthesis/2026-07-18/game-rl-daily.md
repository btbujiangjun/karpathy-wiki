---
title: "Game RL & Game AI Bot — Daily Paper Digest (July 18, 2026)"
type: synthesis
created: 2026-07-18
updated: 2026-07-18
sources: [arxiv, acl-anthology, openreview, nature]
tags: [game-rl, self-play, marl, game-ai, llm-agent, pcg, foundation-model, benchmark, game-world-model]
---

# Game RL & Game AI Bot — Daily Paper Digest (July 18, 2026)

> Curated papers across 7 categories: Game RL, Game AI Bot, Foundation Models, PCG, Benchmarks, World Models, and Related Techniques.

---

## 1. Game RL — Reinforcement Learning in Games

### MARL-GPT: Foundation Model for Multi-Agent Reinforcement Learning
- **Affiliation**: Cognitive AI Systems
- **Venue**: arXiv preprint (2026-04)
- **Key Innovations**: Unified GPT-based transformer for MARL across SMACv2, Google Research Football, and POGEMA. Offline RL with expert trajectories (400M SMACv2, 100M GRF, 1B POGEMA) + single observation encoder requiring no task-specific tuning. Competitive with specialized baselines in all tested environments.
- **Link**: https://arxiv.org/pdf/2604.05943

### Stratagem: Learning Transferable Reasoning via Trajectory-Modulated Game Self-Play
- **Authors**: Xiachong Feng, Deyi Yin, Xiaocheng Feng, Yi Jiang, Libo Qin, Yangfan Ye, et al.
- **Venue**: arXiv preprint (2026-04-20)
- **Key Innovations**: Addresses domain specificity and contextual stasis barriers to reasoning transfer. Reasoning Transferability Coefficient + Reasoning Evolution Reward selectively reinforce abstract, domain-agnostic reasoning. Strong gains on competition-level mathematics.
- **Link**: https://arxiv.org/pdf/2604.17696

### Reproducing AlphaZero on Tablut: Self-Play RL for an Asymmetric Board Game
- **Venue**: arXiv preprint (2026-04)
- **Key Innovations**: Adapts AlphaZero to asymmetric board game with separate policy/value heads per role + shared residual trunk. Addresses catastrophic forgetting via C4 augmentation and replay buffer scaling. BayesElo 1235 after 100 iterations.
- **Link**: https://arxiv.org/abs/2604.05476v1

### Mastering Go with Self-play Experience Replay (QZero)
- **Authors**: Jingbin Liu, Xuechun Wang
- **Venue**: arXiv preprint (2026-01)
- **Key Innovations**: Model-free RL for Go that forgoes MCTS. Entropy-regularized Q-learning with single Q-value network. Tabula rasa, 5 months on 7 GPUs achieves AlphaGo-comparable performance — first model-free RL mastering Go.
- **Link**: https://arxiv.org/html/2601.03306

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors**: Bo Liu, Leon Guertler, Simon C.H. Yu, Zichen Liu, Penghui Qi, Daniel Balcells, et al.
- **Venue**: arXiv preprint (2025-06, updated 2026)
- **Key Innovations**: Self-play on TicTacToe/Kuhn Poker/Simple Negotiation. Role-Conditioned Advantage Estimation (RAE) stabilizes multi-agent training. Up to 10.5% improvement across Qwen and Llama. Different games develop complementary cognitive patterns.
- **Link**: https://arxiv.org/pdf/2506.24119 | **Code**: https://github.com/spiral-rl/spiral

### PolicyEvolve: Evolving Programmatic Policies by LLMs for Multi-Player Games via Population-Based Training
- **Authors**: Mingrui Lv, Hangzhi Liu, Zhi Luo, Hongjie Zhang, Xinyan Liu
- **Venue**: arXiv preprint (2025-09)
- **Key Innovations**: First programmatic RL framework for multi-agent tasks. LLMs generate interpretable rule-based code. Global Pool + Local Pool with PBT. Policy Planner + Trajectory Critic iterate until 60% win rate. Outperforms prompt-based baselines.
- **Link**: https://arxiv.org/html/2509.06053v1

### PopuLoRA: Co-Evolving LLM Populations for Reasoning Self-Play
- **Authors**: Roger Creus Castanyer, Geoffrey Bradway, Lorenz Wolf, et al.
- **Venue**: arXiv preprint (2026-05)
- **Key Innovations**: Population-based asymmetric self-play for RLVR. Teachers/students as specialized LoRA adapters. Cross-evaluation replaces single-agent self-calibration. LoRA weight-space evolution at 7B scale. Outperforms single-agent baseline on HumanEval+, MBPP+, AIME, MATH-500.
- **Link**: https://arxiv.org/html/2605.16727

### GEMS: Scalable Surrogate-Free Multi-Agent Reinforcement Learning
- **Authors**: Sharma, Alakh, Trivedi, et al.
- **Venue**: arXiv preprint (2025-09)
- **Key Innovations**: Compact latent anchors + amortized generator replace explicit populations. Monte Carlo rollouts, multiplicative-weights meta-dynamics, empirical-Bernstein UCB oracle. 6x faster, 1.3x less memory than PSRO.
- **Link**: https://arxiv.org/pdf/2509.23462

### FAMOU: Co-Evolutionary Mechanisms for LLM-Driven Strategy Evolution in Adversarial Games
- **Venue**: arXiv preprint (2026-06)
- **Key Innovations**: Evaluator co-evolution + hierarchical deep evaluation + weakness pressure for adversarial LLM evolution. Won 1st hardware round-robin at AAMAS 2026 MCTF. Generated lookahead search and adaptive interception absent from seeds.
- **Link**: https://arxiv.org/html/2606.10389v1 | **Code**: https://github.com/1xiangliu1/FAMOU-CoEvo

---

## 2. Game AI Bot — LLM-Powered Game Agents

### AVA: Attentive VLM Agent for Mastering StarCraft II (AVACraft)
- **Authors**: Weiyu Ma, Yuqian Fu, Zecheng Zhang, Bernard Ghanem, Guohao Li
- **Venue**: Findings of ACL 2026, pp. 4270-4290
- **Key Innovations**: First multimodal benchmark for StarCraft II decision-making. RGB + language + state. 21 scenarios. MARL 27.1% win rate (1M steps); VLMs 75-81% zero-shot. Baselines: IQL/QMIX/QTRAN/VDN + GPT-4o/Qwen-VL.
- **Link**: https://aclanthology.org/2026.findings-acl.208/

### ROE: Learning to Play StarCraft II from Expert and Self-Experiences
- **Affiliation**: Chinese Academy of Sciences
- **Venue**: arXiv preprint (2502.13388v3)
- **Key Innovations**: Keyframe selection by game phase + expert/self-experience reflection. Strategy iteration via post-game reflection. Beats Very Hard robot in TextStarCraft II.
- **Link**: https://arxiv.org/html/2502.13388v3

### Orchestrated Reality: LLM-Driven World Simulation as Parameterized-Action POMDP
- **Authors**: Y Huang, Chenmiao Li, Chaowei Fang
- **Venue**: arXiv preprint (2026-06)
- **Key Innovations**: World as JSON entity tree, actions as (intent, parameters). Plan-Diff-Validate-Apply pipeline with schema-validated deltas. 15 incidents from real deployment. Towards autonomous game engine.
- **Link**: https://arxiv.org/html/2606.16014

### Bounded Autonomy: Controlling LLM Characters in Live Multiplayer Games
- **Authors**: Yunjia Guo, Jinghan Zhu, Siyu Wang, Haixin Qiao
- **Venue**: arXiv preprint (2026-04)
- **Key Innovations**: Three interfaces: agent-agent, agent-world, player-agent. Probabilistic reply-chain decay + embedding-based action grounding + whisper soft-steering. Deployed in live multiplayer social game.
- **Link**: https://arxiv.org/abs/2604.04703

### COSPLAY: Co-Evolving LLM Decision and Skill Bank Agents
- **Authors**: Xiyang Wu, Zongxia Li, Guangyao Shi, et al.
- **Venue**: arXiv preprint (2026-04)
- **Key Innovations**: LLM decision agent + learnable skill bank co-evolution. 8B model achieves 25.1% reward improvement over frontier LLM baselines on game benchmarks.
- **Link**: https://arxiv.org/pdf/2604.20987

### Nemobot Games: LLM-Powered Game Agents via Shannon's Taxonomy
- **Affiliation**: NUS
- **Venue**: arXiv preprint (2026-04)
- **Key Innovations**: Extends Shannon's taxonomy with LLMs. Dictionary/solvable/heuristic/learning-based game classes. Demonstrated across tic-tac-toe, Nim, Mancala.
- **Link**: https://arxiv.org/abs/2604.21896v1

### Sensi: Curriculum-Based Test-Time Learning for LLM Game Agents
- **Authors**: Mohsen Arjmandi
- **Venue**: arXiv preprint (2026-03)
- **Key Innovations**: Observer+Actor two-player architecture. Curriculum + database-as-control-plane + LLM-as-judge. 50-94x sample efficiency (32 vs 1,600-3,000 attempts). Failure diagnosed as hallucination cascade in perception.
- **Link**: https://arxiv.org/pdf/2603.17683

### HeRoN: Mediated RL-LLM Framework for Adaptive NPC Behavior
- **Authors**: Gaetano Cimino, Vincenzo Deufemia, Andrea Selice
- **Venue**: Neural Computing and Applications, 2026
- **Key Innovations**: RL policy + LLM strategy generator + lightweight reviewer. 81% improvement in task success rate over standard RL. Reduces constraint-violating actions.
- **Link**: https://doi.org/10.1007/s00521-026-12275-w

### CASCADE: Low-Cost Social Coordination for Game Worlds
- **Authors**: Yizhi Xu
- **Venue**: arXiv preprint (2026-04)
- **Key Innovations**: 3-layer: Macro State Director + Coordination Hub + Tag-Driven NPCs. LLMs only for player-facing dialogue. Action-Dialogue Decoupling prevents prompt injection. Dramatic cost reduction vs full-generative NPCs.
- **Link**: https://arxiv.org/pdf/2604.03091

### Psy-CoT: Psychology-Grounded Reasoning for Role-Playing Agents
- **Venue**: arXiv preprint (2026-06)
- **Key Innovations**: Three-step CoT: Interaction Perception, Psychological Empathy, Logical Construction. RAPO uses profile-token mutual info for asymmetric gradient weighting. 40.1% improvement over untrained baseline on CoSER.
- **Link**: https://arxiv.org/html/2606.27025v1

---

## 3. Game Foundation Models

### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loic Magne, Anas Awadalla, Guanzhi Wang, et al.
- **Affiliation**: NVIDIA / MineDojo
- **Venue**: CVPR 2026, pp. 21511-21521
- **Key Innovations**: Vision-action model trained on 40K hours across 1,000+ games. Flow matching + SigLIP 2 + DiT action head. 52% relative improvement when fine-tuning on unseen games. Dataset, benchmark, weights released.
- **Link**: https://arxiv.org/pdf/2601.02427 | **Project**: https://nitrogen.minedojo.org/

### Pixels2Play (P2P): Scaling Behavior Cloning for Real-Time Game Playing
- **Authors**: Yuguang Yue, Irakli Salia, Samuel Hunt, Chris Green, Wenzhe Shi, Jonathan J. Hunt
- **Affiliation**: Open MIND
- **Venue**: arXiv preprint (2026-01)
- **Key Innovations**: 8,300+ hours of gameplay, up to 1.2B params. Scaling laws: more data + deeper models yield more causal policies. Causality score measuring frame-sequence reliance. Real-time inference on consumer GPU.
- **Link**: https://arxiv.org/pdf/2601.04575

### Odysseus: Scaling VLMs to 100+ Turn Decision-Making via RL
- **Venue**: arXiv preprint (2026-05)
- **Key Innovations**: PPO with turn-level critic for long-horizon Super Mario Land. Pretrained VLM priors >> from-scratch RL. 3x progress vs frontier models. In-game + cross-game generalization.
- **Link**: https://arxiv.org/html/2605.00347v1

### Towards Generalist Game Players: Foundation Models in the Game Multiverse
- **Authors**: Kuan Zhang, Dongchen Liu, Qiyue Zhao, et al.
- **Affiliation**: Tsinghua University
- **Venue**: arXiv preprint (2026-05)
- **Key Innovations**: Survey of 4 eras: symbolic/RL → foundation models → creator stage. 4 pillars (Dataset, Model, Harness, Benchmark). 5-level roadmap. 5 fundamental trade-offs.
- **Link**: https://arxiv.org/html/2605.09965

### See, Symbolize, Act: Grounding VLMs with Spatial Representations
- **Authors**: Ashish Baghel, Paras Chopra
- **Venue**: arXiv preprint (2026-03)
- **Key Innovations**: Frame-only vs frame+symbols vs GT-symbols vs symbol-only across Atari/VizDoom/AI2-THOR. GT symbols always best. Self-extracted symbols help only when accurate. Perception is bottleneck.
- **Link**: https://arxiv.org/pdf/2603.11601

### GameVerse: VLMs Learning from Video-based Reflection
- **Authors**: Kuan Zhang, Dongchen Liu, Qiyue Zhao, et al.
- **Affiliation**: THUSI Lab
- **Venue**: arXiv preprint (2026-03)
- **Key Innovations**: 15-game benchmark with reflect-and-retry paradigm. Failure trajectories + expert tutorials best (analogue to RL + SFT). Dual action space (semantic + GUI).
- **Link**: https://arxiv.org/html/2603.06656 | **Code**: https://github.com/THUSI-Lab/GameVerse

---

## 4. Procedural Content Generation

### WFC + PCGRL: Learning Local Constraints for RL Content Generators
- **Venue**: arXiv preprint (2026-05)
- **Key Innovations**: WFC constrains PPO-based PCGRL action space for Lode Runner. Random partial collapse improves robustness. Visually satisfying + playable levels.
- **Link**: https://arxiv.org/html/2605.13570v1

### Multiverse: Language-Conditioned Multi-Game Level Blending
- **Authors**: In-Chang Baek, et al.
- **Venue**: arXiv preprint (2026-03)
- **Key Innovations**: Shared latent space aligning text + levels across games. Multi-positive contrastive supervision. Zero-shot cross-game generation from compositional text.
- **Link**: https://arxiv.org/pdf/2603.26782

### HDPCG: High Dimensional Procedural Content Generation
- **Venue**: arXiv preprint (2026-02)
- **Key Innovations**: Non-geometric gameplay dimensions as first-class coordinates. Direction-Space (layers) + Direction-Time (temporal dynamics). Unity case studies with VVVVVV-style mechanics.
- **Link**: https://arxiv.org/html/2602.18943v1

### PRP: Playtrace Reconstructive Partitioning with Cake Representation
- **Venue**: arXiv preprint (2026-07)
- **Key Innovations**: "Cake" representation encoding levels over time. BSP across time matches temporal entities. 100% playability in Sokoban without hand-authored constraints.
- **Link**: https://arxiv.org/html/2607.12097

### Multi-task PCG with RL (DeBERTa + Super Mario)
- **Authors**: A. Nekahdari, et al.
- **Venue**: Scientific Reports, 2026-04
- **Key Innovations**: DeBERTa encoder + multi-objective training. 14K+ command-level pairs. Outperforms BERT in command following and semantic stability.
- **Link**: https://www.nature.com/articles/s41598-026-48234-7

### Co-adaptive DRL Level Design (Unity)
- **Venue**: arXiv preprint (2025-10)
- **Key Innovations**: Two PPO agents: hummingbird solver + island generator. Dynamic feedback loop. PPO > SAC/DDPG for partially observable procedural tasks.
- **Link**: https://arxiv.org/html/2510.15120v1

---

## 5. Game Benchmarks

| Benchmark | Games | Paradigm | Key Feature |
|-----------|-------|----------|-------------|
| AVACraft (ACL 2026) | StarCraft II (21 scenarios) | MARL + VLM | RGB + language + state; VLMs 75-81% zero-shot |
| GameVerse | 15 games | Reflect-retry | Video-based reflection, dual action space |
| Generalist GP survey | 100+ games | Survey | 5-level roadmap, 4 pillars |
| ARC-AGI-3 (Sensi) | Pixel-art puzzles | Test-time learning | 50-94x sample efficiency target |
| MCTF 2026 (FAMOU) | Maritime CTF 3v3 | Adversarial evolution | AAMAS competition benchmark |

---

## 6. Industry Game AI

| System | Company/Institution | Key Innovation |
|--------|-------------------|----------------|
| CASCADE | Academic | 3-layer social coordination, Action-Dialogue Decoupling |
| HeRoN | Academic | RL-LLM mediated NPC, 81% task success improvement |
| Bounded Autonomy | Academic | Live multiplayer LLM characters with whisper steering |
| Orchestrated Reality | Academic | Parameterized-Action POMDP, 15 deployed incidents |
| AVACraft | Academic | StarCraft II VLM+MARL benchmark |

---

## 7. Related Techniques

### Population-Based Training & Evolution
- **PolicyEvolve**: LLM-generated programmatic policies with Global/Local pools
- **PopuLoRA**: LoRA weight-space evolution at 7B scale
- **FAMOU**: Evaluator co-evolution + weakness pressure (AAMAS 2026 winner)
- **GEMS**: Latent anchor PSRO replacement (6x faster)

### Self-Play Reasoning Transfer
- **SPIRAL**: 10.5% reasoning improvement via game self-play
- **Stratagem**: Trajectory-modulated transferable reasoning
- **QZero**: Model-free Go mastery (AlphaGo-comparable)

### RL + LLM for Game Agents
- **ROE**: Episode reflection for StarCraft II strategy iteration
- **COSPLAY**: Co-evolving skill bank + decision agent (+25.1%)
- **Sensi**: Curriculum-based test-time learning (50-94x efficiency)
- **HeRoN**: Mediated RL-LLM for NPC adaptiveness (+81%)

### Procedural Content Generation
- **WFC+PCGRL**: Hybrid constraint + RL for visual + functional levels
- **Multiverse**: Cross-game level blending via shared representations
- **PRP**: Time-aware cake representation + BSP generation
- **HDPCG**: Non-geometric gameplay dimensions

---

## Cross-Cutting Themes

1. **Self-play generates transferable reasoning**: SPIRAL, Stratagem, PopuLoRA, MARL-GPT all show game self-play develops cognitive patterns transferring to math/code/reasoning.

2. **Foundation models at internet scale**: NitroGen (CVPR 2026, 40K hrs/1000+ games) and Pixels2Play (8300+ hrs) demonstrate viability of internet-scale pre-training for game agents. Generalist GP survey provides 5-level roadmap.

3. **VLM agents show promise but perception is bottleneck**: See, Symbolize, Act finds self-extracted symbols help only when accurate. AVACraft shows VLMs achieve 75-81% zero-shot vs MARL 27.1% — but long-horizon tasks remain challenging (Odysseus tackles 100+ turns).

4. **LLM agents entering live games**: Bounded Autonomy, Orchestrated Reality, and CASCADE demonstrate real deployment of LLM characters in multiplayer and open-world settings. Action-Dialogue Decoupling is key safety mechanism.

5. **PCG + RL complementary workflows**: WFC+PCGRL combines visual style with functional guarantees. Multiverse enables cross-game level blending. PRP achieves 100% playability without reward signals.

6. **Population-based evolution scales**: From PSRO (quadratic) → GEMS (6x faster) → PolicyEvolve (LLM-generated code) → PopuLoRA (7B LoRA evolution) → FAMOU (co-evolutionary competition winner).

7. **Game benchmarks expanding**: AVACraft (ACL 2026), GameVerse, Generalist GP survey, ARC-AGI-3, MCTF 2026 — covering MARL, VLM, test-time learning, adversarial evolution.

> Total: **30+ curated papers** across 7 categories.
