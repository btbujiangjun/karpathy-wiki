---
title: Game RL & Game AI Bot — Daily Paper Digest (July 14, 2026)
type: synthesis
created: 2026-07-14
updated: 2026-07-14
tags: [game-rl, game-ai, self-play, marl, vlm-agents, foundation-models, pcg, benchmarks, world-models]
---

# Game RL & Game AI Bot — Daily Paper Digest (July 14, 2026)

A curated digest of recent arXiv papers and published proceedings covering reinforcement learning in games, LLM/VLM game agents, game foundation models, procedural content generation, game benchmarks, industry game AI, and related techniques.

---

## 1. Game RL — Reinforcement Learning in Games

### 1.1 MARL-GPT: A Foundation Model for Multi-Agent Reinforcement Learning
- **Authors**: Multiple authors (Cognitive AI Systems group)
- **Affiliation**: Cognitive AI Systems
- **Venue**: arXiv preprint
- **Link**: https://arxiv.org/pdf/2604.05943
- **Abstract & Key Innovations**: Proposes MARL-GPT, a single GPT-based transformer model trained to perform well across diverse multi-agent RL environments (SMACv2, Google Research Football, POGEMA). Uses offline RL on 400M–1B expert trajectories with a unified observation encoder requiring no task-specific tuning. Achieves competitive performance vs. specialized baselines. Supports online fine-tuning for unseen tasks, demonstrating fast adaptation (e.g., Terran 5v5 from 0.4→0.8 success rate). Represents a path toward a "ChatGPT for MARL."

### 1.2 Superhuman AI for Generals.io Using Self-Play RL
- **Authors**: Matěj Straka, Viliam Lisý, Martin Schmid
- **Affiliation**: - (arXiv preprint)
- **Venue**: arXiv preprint (2026-06-22)
- **Link**: https://arxiv.org/html/2606.23348
- **Abstract & Key Innovations**: Presents a superhuman AI agent for Generals.io (real-time strategy game with imperfect information). Trained for 4 days on 4× NVIDIA H200 GPUs, reaches #1 on public 1v1 leaderboard (5000+ human players), beating 2nd place by the margin separating 2nd from 25th. Key enabler: a JAX-native simulator reaching tens of millions of FPS on a single GPU (~10,000× speedup over prior simulator). Uses ViT policy trained end-to-end by self-play with policy-gradient and sparse win/loss reward. Demonstrates that removing the data bottleneck via fast simulator is what matters most.

### 1.3 Stratagem: Learning Transferable Reasoning via Trajectory-Modulated Game Self-Play
- **Authors**: Xiachong Feng, Deyi Yin, Xiaocheng Feng, Yi Jiang, Libo Qin, Yangfan Ye, et al.
- **Affiliation**: - (arXiv preprint)
- **Venue**: arXiv preprint (2026-04-20)
- **Link**: https://arxiv.org/pdf/2604.17696
- **Abstract & Key Innovations**: Addresses two barriers to reasoning transfer from games: domain specificity and contextual stasis. STRATAGEM selectively reinforces trajectories exhibiting abstract, domain-agnostic reasoning via a Reasoning Transferability Coefficient, and incentivizes adaptive reasoning via a Reasoning Evolution Reward. Demonstrates substantial improvements across mathematical reasoning, general reasoning, and code generation benchmarks, with strong gains on competition-level mathematics.

### 1.4 Reproducing AlphaZero on Tablut: Self-Play RL for Asymmetric Board Games
- **Authors**: -
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-04-07)
- **Link**: https://arxiv.org/abs/2604.05476v1
- **Abstract & Key Innovations**: Investigates adapting AlphaZero to Tablut, an asymmetric board game (king capture vs. king escape). Modifies architecture with separate policy/value heads per player role while maintaining shared residual trunk. Addresses catastrophic forgetting between roles via C4 augmentation, larger replay buffer, and 25% games against random past checkpoints. Achieves BayesElo 1235 over 100 self-play iterations, confirming AlphaZero can transfer to asymmetric games with proper stabilization.

### 1.5 Generative Gamer: Learning Equilibrium Strategy by LLM-driven Dynamic Deduction
- **Authors**: Yadong Zhang, Xinshu Shen, Yupei Ren, Shangqing Zhao, Man Lan
- **Affiliation**: - (ACL 2026)
- **Venue**: ACL 2026 Long Papers (pages 12604–12617)
- **Link**: https://aclanthology.org/2026.acl-long.574/
- **Abstract & Key Innovations**: Introduces Generative Gamer (GenGamer), training LLMs to reason like expert players by generating compact, pruned reasoning trajectories (Dynamic Deduction). Integrates action pruning (policy confidence), state pruning (value estimation), and branch pruning (alpha-beta principles). Proposes Deduction Tree Reward (DTR) for process-oriented step-by-step feedback. Achieves SOTA on Tic-Tac-Toe and Leduc Poker.

---

## 2. Game AI Bot — LLM/VLM-Powered Game Agents

### 2.1 Bounded Autonomy: Controlling LLM Characters in Live Multiplayer Games
- **Authors**: -
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-04-07, updated 2026-07-07)
- **Link**: https://arxiv.org/abs/2604.04703v1
- **Abstract & Key Innovations**: Frames a control architecture for LLM characters in live multiplayer games organized around three interfaces: agent-agent interaction (reply-focus arbitration + reply-chain decay), agent-world action execution (embedding-based grounding with fallback), and player-agent steering (whisper — a lightweight soft-steering technique). Deployed in a live multiplayer social game. Provides a concrete exemplar for controllable LLM character play as a distinct runtime control problem.

### 2.2 Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with LLMs
- **Authors**: -
- **Affiliation**: NUS (National University of Singapore)
- **Venue**: arXiv preprint (2026-04-23)
- **Link**: https://arxiv.org/abs/2604.21896v1
- **Abstract & Key Innovations**: Presents Nemobot, an interactive agentic engineering environment enabling users to create, customize, and deploy LLM-powered game agents. Focuses on strategic AI gaming agents for interactive learning scenarios.

### 2.3 PTCG-Bench: Can LLM Agents Master Pokémon Trading Card Game?
- **Authors**: Dongdong Hua, Yifei Sun, R.L. Huang, Feng Gao, Chunping Wang, Yang Yang
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-05-28)
- **Link**: https://doi.org/10.48550/arxiv.2605.29653
- **Abstract & Key Innovations**: Benchmark built on Pokémon Trading Card Game evaluating LLM agents at two levels: decision-making within a complex environment and self-evolution through accumulated experience. Includes modular harness ablation for interpretability. Shows LLM agents achieve non-trivial gameplay but sustained stable self-evolution remains challenging and sensitive to harness design.

### 2.4 Orchestrated Reality: LLM-Driven World Simulation as Parameterized-Action POMDP
- **Authors**: Y Huang, Chenmiao Li, Chaowei Fang
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-06-14)
- **Link**: https://arxiv.org/html/2606.16014
- **Abstract & Key Innovations**: Formalizes an LLM-driven game world for human players as a Parameterized-Action POMDP with JSON entity state, plan-diff-validate-apply pipeline for transitions, and narrative projection observations. Provides a singleton orchestration agent analogous to a tabletop-RPG Game Master. Includes 15 illustrative incidents from a real deployment.

### 2.5 OpenGame: Open Agentic Coding for Games
- **Authors**: Yilei Jiang, Jinyuan Hu, Qianyin Xiao, Yaozhi Zheng, Ruize Ma, Kaituo Feng, et al.
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-04-20)
- **Link**: https://arxiv.org/abs/2604.18394
- **Abstract & Key Innovations**: Framework for open agentic coding of games, enabling automated game development through agent-driven code generation.

---

## 3. Game Foundation Models — Generalist Game-Playing Models

### 3.1 NitroGen: An Open Foundation Model for Generalist Gaming Agents (CVPR 2026)
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi "Jim" Fan
- **Affiliation**: NVIDIA / MineDojo / academic collaborators
- **Venue**: CVPR 2026 (pages 21511–21521)
- **Link**: https://arxiv.org/abs/2601.02427
- **Abstract & Key Innovations**: Vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games. Internet-scale video-action dataset from publicly available gameplay videos via automatic gamepad overlay extraction. Multi-game benchmark environment for cross-game generalization. Unified 500M-parameter DiT model trained via behavior cloning. Achieves up to 52% relative improvement in task success on unseen games via fine-tuning. Releases dataset, evaluation suite, and model weights.

### 3.2 Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents
- **Authors**: -
- **Affiliation**: ByteDance (Seed team)
- **Venue**: arXiv preprint
- **Link**: https://arxiv.org/html/2510.23691v1
- **Abstract & Key Innovations**: Generalist game agent with unified keyboard-mouse action space (human-native interaction paradigm). Pre-trained on 500B+ tokens across game trajectories, GUI agent trajectories, and multimodal data. Key techniques: decaying continual loss to reduce causal confusion, Sparse-Thinking strategy balancing reasoning depth and inference cost. Achieves ~2× success rate over prior SOTA on Minecraft, near-human generalization in unseen web 3D games, outperforms GPT-5/Gemini-2.5-Pro/Claude-4-Sonnet on FPS benchmarks. Scaling results confirm unified action space sustains improvements across cross-game multimodal data.

### 3.3 Scaling Behavior Cloning Improves Causal Reasoning: Pixels2Play
- **Authors**: Yuguang Yue, Irakli Salia, Samuel Hunt, Chris Green, Wenzhe Shi, Jonathan J. Hunt
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-01-08)
- **Link**: https://arxiv.org/pdf/2601.04575
- **Abstract & Key Innovations**: Open recipe for training a video game playing foundation model (Pixels2Play / P2P). 8,300+ hours of high-quality human gameplay data released. Text-conditioned policy producing keyboard/mouse actions from pixels in real-time on consumer GPU. Lightweight decoder-only transformer with custom image tokenization. Systematic study of behavior cloning scaling laws up to 1.2B parameters, showing increasing model depth/data improves causal reasoning.

### 3.4 Towards Generalist Game Players: An Investigation of Foundation Models in the Game Multiverse
- **Authors**: Kuan Zhang, Dongchen Liu, Qiyue Zhao, Tianyu Xin, Yue Su, Haisheng Wang, et al.
- **Affiliation**: Tsinghua University (THUSI Lab)
- **Venue**: arXiv preprint (2026-05-11)
- **Link**: https://arxiv.org/abs/2605.09965
- **Abstract & Key Innovations**: Comprehensive survey tracing the full lifecycle of a generalist game player across four pillars: Dataset, Model, Harness, and Benchmark. Identifies five fundamental trade-offs. Charts a five-level roadmap from single-game mastery to a "creator" stage where agents create and evolve within game multiverses. Covers four eras: symbolic/RL agents → foundation model generalist players → creator stage.

### 3.5 GameVerse: Can Vision-Language Models Learn from Video-based Reflection?
- **Authors**: Kuan Zhang, Dongchen Liu, Qiyue Zhao, Jinkun Hou, Xinran Zhang, Qinlei Xie, et al.
- **Affiliation**: THUSI Lab (Tsinghua)
- **Venue**: arXiv preprint (2026-03-01)
- **Link**: https://arxiv.org/html/2603.06656
- **Abstract & Key Innovations**: Benchmark enabling a reflective visual interaction loop using a reflect-and-retry paradigm across 15 globally popular games. Dual action space (semantic + GUI control). Shows VLMs benefit from video-based reflection, performing best by combining failure trajectories and expert tutorials — a training-free analogue to RL + SFT.

### 3.6 Lumine: An Open Recipe for Building Generalist Agents in 3D Open Worlds
- **Authors**: Weihao Tan, Xiangyang Li, Yunhao Fang, Heyuan Yao, Shi Yan, Hao Luo, et al.
- **Affiliation**: -
- **Venue**: arXiv preprint (2025-11-12)
- **Link**: https://arxiv.org/html/2511.08892
- **Abstract & Key Innovations**: First open recipe for generalist agents completing hours-long complex missions in real-time within 3D open worlds. Trained in Genshin Impact, completes the entire 5-hour Mondstadt main storyline. Processes raw pixels at 5 Hz producing 30 Hz keyboard-mouse actions with adaptive reasoning invocation. Demonstrates strong zero-shot cross-game generalization (100-minute missions in Wuthering Waves, full 5-hour chapter of Honkai: Star Rail).

---

## 4. Procedural Content Generation

### 4.1 IPCGRL: Language-Instructed Reinforcement Learning for Procedural Level Generation
- **Authors**: In-Chang Baek, Sunghyun Kim, Seo-Young Lee, Dong-Hyeon Kim, Kyung-Joong Kim
- **Affiliation**: -
- **Venue**: arXiv preprint (2025-03-16)
- **Link**: https://arxiv.org/html/2503.12358
- **Abstract & Key Innovations**: Instruction-based PCG via RL incorporating a sentence embedding model. Fine-tunes task-specific embedding representations to compress game-level conditions. Achieves 21.4% improvement in controllability and 17.2% in generalizability for unseen instructions. Extends modality of conditional input for more flexible PCG interaction.

### 4.2 PCGRLLM: Large Language Model-Driven Reward Design for Procedural Content Generation via RL
- **Authors**: -
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-05-25)
- **Link**: https://arxiv.org/html/2502.10906v2
- **Abstract & Key Innovations**: Extended architecture using LLMs to design reward functions for DRL-based procedural content generation. Automates the typically manual reward engineering process.

### 4.3 Multiverse: Language-Conditioned Multi-Game Level Blending via Shared Representation
- **Authors**: In-Chang Baek, Jiyun Jung, Geum-Hwan Hwang, Sung-Hyun Kim, Kyung-Joong Kim
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-03-25)
- **Link**: https://arxiv.org/pdf/2603.26782
- **Abstract & Key Innovations**: Language-conditioned multi-game level generator enabling cross-game level blending. Learns shared latent space aligning text instructions and level structures via threshold-based multi-positive contrastive supervision. Supports controllable blending through latent interpolation and zero-shot generation from compositional prompts.

### 4.4 Agentic PCG: Procedural Content Generation via Tool-using LLMs
- **Authors**: Zehua Jiang, Sam Earle, Ahmed Khalifa, Julian Togelius
- **Affiliation**: -
- **Venue**: SSRN (2026)
- **Link**: https://github.com/JiangZehua/AgenticPCG
- **Abstract & Key Innovations**: LLM agent system using structured tool calling to optimize game levels through iterative evaluation and editing. Supports Binary Maze, BinaryDoor, Zelda, Sokoban, LodeRunner, and Super Mario Bros.

### 4.5 Designing Fun: LLM-based Game Level Generation via Agent Gameplay Feedback
- **Authors**: Yu-Hsuan (GitHub)
- **Affiliation**: -
- **Venue**: GitHub project (2026)
- **Link**: https://github.com/Yu-Hsuan-1220/RL_Final_Project
- **Abstract & Key Innovations**: Two-stage pipeline: SFT teaches LLM to output valid MiniGrid levels, then GRPO with fun-aligned reward optimizes for skill-discriminative challenges, meaningful object interactions, and diverse layouts. Reward decomposed into format correctness (95%), solvability (79.4%), regret (0.173), interactions (0.864), and diversity (0.324).

### 4.6 The Garden of Forking Paths: Narrative Arc-Conditioned Gameplay Planning
- **Authors**: -
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-05-01)
- **Link**: https://arxiv.org/html/2605.01245v1
- **Abstract & Key Innovations**: Framework for narrative arc-conditioned gameplay planning generating branching games from user-provided storylines. Generate-first-constrain-later paradigm: generates diverse independent nodes, then assembles into dungeon graph via arc-guided constraint algorithms. Multimodal alignment of gameplay elements (NPC behavior, difficulty, items) with narrative arc states. Integrated with Unity for end-to-end interactive system.

### 4.7 MultiGen: Level-Design for Editable Multiplayer Worlds in Diffusion Game Engines
- **Authors**: -
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-03-03)
- **Link**: https://arxiv.org/abs/2603.06679v1
- **Abstract & Key Innovations**: Introduces explicit external memory into diffusion game engines for user control over environment structure and shared multiplayer inference. Decomposes generation into Memory, Observation, and Dynamics modules. Gives users direct, editable control via persistent state representation independent of model context window.

---

## 5. Game Benchmarks

### 5.1 OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics
- **Authors**: Mingxian Lin, Shengju Qian, Yuqi Liu, Yi-Hua Huang, Yiyu Wang, Wei Huang, et al.
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-06-08)
- **Link**: https://arxiv.org/html/2606.09826
- **Abstract & Key Innovations**: 12 newly built Unreal Engine 5 games spanning Solo (7), PvP (3), and Coop (2) with unified action interfaces. Improvement Dynamics Curve (IDC): agentic-reflection harness where a reflector LLM autonomously refines skill prompts across rounds. Beyond cold-start leaderboard, tracks score evolution across reflection rounds and skill transfer to held-out variants. Reports observables for 12 VLM agents and 4 top agents under IDC.

### 5.2 GameWorld: Standardized Benchmark for Multimodal Game Agents
- **Authors**: Mingyu Ouyang et al.
- **Affiliation**: NUS
- **Venue**: arXiv preprint (2026-04-07)
- **Link**: https://huggingface.co/papers/2604.07429
- **Abstract & Key Innovations**: Standardized, verifiable benchmark for evaluating multimodal game agents across 34 browser games and 170 tasks.

### 5.3 AgentOdyssey: Open-Ended Long-Horizon Text Game Generation for Test-Time Continual Learning
- **Authors**: -
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-06-24)
- **Link**: https://arxiv.org/html/2606.24893v1
- **Abstract & Key Innovations**: Procedurally generates open-ended text games with rich entities, world dynamics, and long-horizon tasks for evaluating test-time continual learning. Multifaceted evaluation: world knowledge QA, episodic memory QA, object/action exploration, action diversity, and model cost. Reveals critical limits — even top agents far below human performance. Identifies short-term memory as key component.

### 5.4 Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games
- **Authors**: Dongmin Park, Minkyu Kim, Beongjun Choi, Junhyuck Kim, Keon Lee, Jonghyun Lee, et al.
- **Affiliation**: KRAFTON
- **Venue**: arXiv preprint (2025-06-04)
- **Link**: https://arxiv.org/html/2506.03610
- **Abstract & Key Innovations**: 12 popular video games spanning all major genres. Plug-and-play MCP interface for seamless LLM-game connection. Fine-tuning dataset of LLM gameplay trajectories. General game score leaderboards, LLM battle arenas, and in-depth analyses of visual inputs, agentic strategies, and finetuning effects.

### 5.5 PTCG-Bench: LLM Agents Master Pokémon Trading Card Game
- **Authors**: Dongdong Hua, Yifei Sun, R.L. Huang, Feng Gao, Chunping Wang, Yang Yang
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-05-28)
- **Link**: https://doi.org/10.48550/arxiv.2605.29653
- **Abstract & Key Innovations**: Benchmark on Pokémon Trading Card Game evaluating LLM agents' decision-making and self-evolution capabilities. Includes modular harness ablation. Shows non-trivial gameplay performance but sustained self-evolution remains challenging.

### 5.6 CivBench: Progress-Based Evaluation for LLMs' Strategic Decision-Making in Civilization V
- **Authors**: John Chen, Sihan Cheng, Can Gurkan, Mingyi Lin
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-04-09)
- **Link**: https://doi.org/10.48550/arxiv.2604.07733
- **Abstract & Key Innovations**: Benchmark for LLM strategists in multiplayer Civilization V. Trains models on turn-level game state to estimate victory probabilities throughout play (not just terminal outcomes). Validated through predictive, construct, and convergent validity. 307 games with 7 LLMs reveal distinct strategic profiles invisible through outcome-only evaluation.

### 5.7 StarBench: Turn-Based RPG Benchmark for Agentic Multimodal Decision-Making
- **Authors**: -
- **Affiliation**: -
- **Venue**: arXiv preprint (2025-10-18)
- **Link**: https://arxiv.org/html/2510.18483v1
- **Abstract & Key Innovations**: Benchmark from Honkai: Star Rail evaluating VLMs on (i) multimodal decision-making from pixels to actions and (ii) agentic information seeking (ask-or-act diagnostic). Direct control vs. tool-assisted control under identical tasks. Current VLMs fail almost entirely in direct control; tool assistance markedly improves success.

### 5.8 MineExplorer: Evaluating Open-World Exploration of MLLM Agents in Minecraft
- **Authors**: Tianjie Ju et al.
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-06-01)
- **Link**: https://huggingface.co/papers/2605.30931
- **Abstract & Key Innovations**: Benchmark filtering Minecraft-specific tasks to evaluate general open-world exploration. Multi-agent synthesis workflow for reliable instances (30% higher validity vs. single-agent). Composes atomic tasks into implicit multi-hop tasks. Even best models (Claude-Opus-4.6, Gemini-3.1-Pro) degrade sharply on multi-hop tasks.

### 5.9 CausalGame: Benchmarking Causal Thinking of LLM Agents in Games
- **Authors**: -
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-07-04)
- **Link**: https://arxiv.org/html/2607.04293v1
- **Abstract & Key Innovations**: Benchmark specifically targeting causal reasoning capabilities of LLM agents in game settings.

---

## 6. Industry Game AI

### 6.1 Augmenting Game AI with Deep Reinforcement Learning
- **Authors**: Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslén
- **Affiliation**: - (industry/authors)
- **Venue**: arXiv preprint (2026-06-18)
- **Link**: https://arxiv.org/abs/2606.20210
- **Abstract & Key Innovations**: Envisions applications of reinforcement learning for game AI in the future, discussing practical deployment considerations and industry perspectives on RL-based game AI.

### 6.2 Experience Transfer for Multimodal LLM Agents in Minecraft Game
- **Authors**: Chenghao Li, Jun Liu, Songbo Zhang, Huadong Jian, Hao Ni, Lik-Hang Lee, Sung-Ho Bae, Guoqing Wang, Yang Yang, Chaoning Zhang
- **Affiliation**: -
- **Venue**: CVPR 2026
- **Link**: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Experience_Transfer_for_Multimodal_LLM_Agents_in_Minecraft_Game_CVPR_2026_paper.pdf
- **Abstract & Key Innovations**: Published at CVPR 2026. Focuses on transferring experience knowledge to multimodal LLM agents in Minecraft, addressing the challenge of cross-domain skill transfer in game environments.

---

## 7. Related Techniques

### 7.1 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors**: Lei Zhu, Lutz Güertler, Simon C.H. Yu, Zichen Liu, Penghui Qi, Daniel Balcells, et al.
- **Affiliation**: -
- **Venue**: arXiv preprint (2025-06-30, cited at ICLR 2026)
- **Link**: https://arxiv.org/abs/2506.24119
- **Abstract & Key Innovations**: Self-play framework where models learn by playing multi-turn zero-sum games against improving versions of themselves. Generates automatic curriculum of stronger opponents. Role-conditioned advantage estimation (RAE) stabilizes multi-agent training. Improves up to 10% across 8 reasoning benchmarks on 4 models (Qwen and Llama families). Multi-game training (TicTacToe, Kuhn Poker, Simple Negotiation) yields strongest results. Different games develop complementary reasoning strengths that transfer.

### 7.2 MARS: Reinforcing Multi-Agent Reasoning of LLMs through Self-Play in Strategic Games
- **Authors**: - (Tsinghua NICS group)
- **Affiliation**: Tsinghua University
- **Venue**: arXiv preprint (2025-10-17)
- **Link**: https://arxiv.org/html/2510.15414v1
- **Abstract & Key Innovations**: End-to-end RL framework incentivizing multi-agent reasoning through self-play in both cooperative and competitive games. Turn-level advantage estimator for fine-grained credit assignment. Agent-specific advantage normalization for stable multi-agent training. Trained from Qwen3-4B, achieves up to 28.7% improvement on held-out games. Generalizes beyond games: +10.0% on AIME and +12.5% on GPQA-Diamond when integrated into multi-agent systems.

### 7.3 MEMO: Memory-Augmented Model Context Optimization for LLM Game Agents
- **Authors**: -
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-03-09)
- **Link**: https://www.arxiv.org/pdf/2603.09022
- **Abstract & Key Innovations**: Weight-free self-play framework coupling retention (persistent memory bank distilling trajectories into reusable insights) with exploration (tournament-style prompt evolution + prioritized replay). Raises mean win rate from 25.1%→49.5% (GPT-4o-mini) and 20.9%→44.3% (Qwen-2.5-7B) using 2,000 self-play games per task (19× fewer than RL baselines). Reduces run-to-run variance by 7×. Demonstrates persistent memory is what transforms context optimization.

### 7.4 CuES: A Curiosity-Driven and Environment-Grounded Synthesis Framework for Agentic RL
- **Authors**: Sandra Mai, Yunkai Zhai, Ziqian Chen, Cheng Chen, Anni Zou, Shuailin Tao, et al.
- **Affiliation**: -
- **Venue**: arXiv preprint (2025-12-01)
- **Link**: https://arxiv.org/pdf/2512.01311
- **Abstract & Key Innovations**: Addresses task scarcity for agentic RL. Autonomously generates diverse, executable tasks from environment structure via intrinsic curiosity without handcrafted seeds. Abstracts interaction patterns into reusable task schemas with memory-based quality control. Produces task distributions matching or surpassing manually curated datasets in diversity and executability across AppWorld, BFCL, and WebShop.

### 7.5 SuS: Strategy-aware Surprise for Intrinsic Exploration
- **Authors**: Mark Kashirskiy, Ilya Makarov
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-01-15)
- **Link**: https://arxiv.org/pdf/2601.10349
- **Abstract & Key Innovations**: Intrinsic motivation using pre-post prediction mismatch in strategy space. Strategy Stability measures behavioral consistency; Strategy Surprise captures unexpected strategic outcomes. Achieves 17.4% improvement in Pass@1 and 26.4% in Pass@5 on mathematical reasoning tasks. Ablation confirms both components necessary (removal causes ≥10% degradation).

### 7.6 Mind-Studio: Executable World Models with Lookahead Evaluation for Partially Observable Games
- **Authors**: -
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-06-16)
- **Link**: https://arxiv.org/html/2606.16070v2
- **Abstract & Key Innovations**: Synthesizes executable pygame-style world models from state-action-next-state trajectories using LLMs. Entropy-selected traces + game skill file guide single-pass LLM synthesis. On Montezuma's Revenge, improves chosen-action NSP from 0.3% (PoE-World) to 48.7% while verifying 5/8 subgoals. Demonstrates a single unrefined LLM pass can produce meaningful executable world models.

### 7.7 Distilling Game Code World Model Generation into Lightweight LLMs
- **Authors**: -
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-05-24)
- **Link**: https://arxiv.org/html/2605.24375v1
- **Abstract & Key Innovations**: Investigates whether GameCWM generation can be distilled into smaller models via post-training. Curated dataset of 30 games (perfect + imperfect information). Hierarchical verification framework evaluating structural and semantic game properties. Two-stage pipeline: SFT + RLVR (GRPO). Shows SFT+RLVR pipeline strongest, enabling Qwen2.5-3B-Instruct to generate valid GameCWMs without frontier model dependency.

### 7.8 WISE: A Long-Horizon Agent in Minecraft with Why-Which Reasoning
- **Authors**: -
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-06-12)
- **Link**: https://arxiv.org/html/2606.12852v1
- **Abstract & Key Innovations**: Long-horizon agent with Causal Event Graph augmenting episodic memory with explicit causal structure (cow → CAN_OBTAIN → beef). Opportunistic Task Scheduler dynamically re-prioritizes subtasks when causally relevant opportunities detected. Multi-scale progressive exploration. Achieves 14% improvement in exploration coverage, 30% increase in sequential sparse task success (26.4% less time), and 44% increase in adaptive non-sequential task success (42.5% less time).

### 7.9 MineEvolve: Self-Evolution with Accumulated Knowledge for Long-Horizon Embodied Minecraft Agents
- **Authors**: -
- **Affiliation**: USTC
- **Venue**: arXiv preprint (2026-03-13)
- **Link**: https://arxiv.org/html/2603.13131v2
- **Abstract & Key Innovations**: Knowledge-driven self-evolution framework converting execution feedback into actionable behavioral knowledge. Monitor → Inducer → Curator → Adaptor pipeline. Successful executions distilled into reusable skills; failures transformed into remedies for plan repair. Consistently improves across multiple LM planners, with larger gains on high-dependency task groups.

### 7.10 Sensi: Learn One Thing at a Time — Curriculum-Based Test-Time Learning for LLM Game Agents
- **Authors**: Mohsen Arjmandi
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-03-18)
- **Link**: https://arxiv.org/pdf/2603.17683
- **Abstract & Key Innovations**: Two-player architecture separating perception from action. Curriculum-based learning via external state machine. Database-as-control-plane making context window programmatically steerable. LLM-as-judge with dynamic rubrics. Sensi v2 completes entire learning curriculum in ~32 actions (50–94× more sample-efficient than comparable systems). Precisely diagnoses failure as self-consistent hallucination cascade in perception layer.

### 7.11 AlayaWorld: Long-Horizon and Playable Video World Generation
- **Authors**: -
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-07-07)
- **Link**: https://arxiv.org/html/2607.06291v1
- **Abstract & Key Innovations**: Full-stack open-source framework for interactive generative worlds. Autoregressive DiT with prompt-switching mechanism, AdaLN-style camera control, 3D cache, history compression, error bank, and few-step distillation. Supports open-ended real-time interaction (navigation, combat, spell casting, monster summoning). Trained on both gameplay and real-world videos.

### 7.12 WorldCam: Interactive Autoregressive 3D Gaming Worlds with Camera Pose
- **Authors**: -
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-03-17)
- **Link**: https://arxiv.org/abs/2603.16871v1
- **Abstract & Key Innovations**: Establishes camera pose as unifying geometric representation for interactive gaming worlds. Physics-based continuous action space in Lie algebra for precise 6-DoF camera poses. Global camera poses as spatial indices for geometrically consistent revisiting. 3,000 minutes of authentic human gameplay (Counter-Strike, Xonotic, Unvanquished). Outperforms Yume, Matrix-Game 2.0, and GameCraft in action controllability, visual quality, and 3D consistency.

### 7.13 Reinforcement World Model Learning for LLM-based Agents (RWML)
- **Authors**: Xiao Yu, Baolin Peng, Ruize Xu, Yelong Shen, Pengcheng He, Suman Nath, et al.
- **Affiliation**: -
- **Venue**: arXiv preprint (2026-02-05)
- **Link**: https://arxiv.org/pdf/2602.05842
- **Abstract & Key Innovations**: Self-supervised method learning action-conditioned world models for LLM agents using sim-to-real gap rewards. Aligns simulated vs. realized next states in pre-trained embedding space. Improves base model by 19.6 on ALFWorld and 7.9 on τ²Bench without any expert data or task-success rewards. When combined with task-success RL, outperforms direct RL by 6.9 and 5.7 points respectively.

### 7.14 Scalable Multi-Task RL for Generalizable Spatial Intelligence in Visuomotor Agents
- **Authors**: -
- **Affiliation**: -
- **Venue**: arXiv preprint (2025-07-23)
- **Link**: https://arxiv.org/html/2507.23698v1
- **Abstract & Key Innovations**: RL-finetuned visuomotor agents in Minecraft achieve zero-shot generalization to unseen worlds. Cross-view goal specification as unified multi-task goal space. Automated task synthesis within Minecraft generates 100,000+ training tasks. Achieves 4× improvement in interaction success rates. Demonstrates zero-shot transfer to DMLab, Unreal Engine, and real-world Mecanum-wheeled robot.

---

## Summary Statistics

| Category | Papers |
|----------|--------|
| Game RL | 5 |
| Game AI Bot | 5 |
| Foundation Models | 6 |
| Procedural Content Generation | 7 |
| Game Benchmarks | 9 |
| Industry Game AI | 2 |
| Related Techniques | 14 |
| **Total** | **48** |

## Key Trends

1. **Foundation models at internet scale** maturing: NitroGen (40K hrs, 1000+ games, CVPR 2026), Game-TARS (500B+ tokens), Pixels2Play (8300+ hrs open), Lumine (5-hour open-world completion)
2. **Self-play as LLM reasoning paradigm**: SPIRAL transfers game reasoning to math/code, MARS extends to cooperative games, STRATAGEM adds trajectory-level transferability
3. **VLM agents entering real game clients**: AVA (StarCraft II, ACL 2026), Odysseus (100+ turn RL), StarBench (real-client benchmark), Bounded Autonomy (live multiplayer deployment)
4. **Executable world models via LLMs**: Mind-Studio (48.7% NSP on Montezuma), GameCWM distillation into 3B models, RWML self-supervised world learning
5. **PCG + LLM complementary workflows**: IPCGRL (language-instructed PCGRL), Agentic PCG (tool-using LLMs), Multiverse (cross-game blending), narrative arc conditioning
6. **Game benchmarks proliferating**: 8 new benchmarks (OmniGameArena, GameWorld, AgentOdyssey, Orak, PTCG-Bench, CivBench, StarBench, MineExplorer)
7. **Memory and self-evolution critical**: WISE causal event graph (+44% adaptive tasks), MineEvolve knowledge accumulation, MEMO persistent memory (19× fewer games)
8. **Curiosity and intrinsic motivation evolving**: CuES (environment-grounded task generation), SuS (strategy-aware surprise), CIG (information gain framework)
