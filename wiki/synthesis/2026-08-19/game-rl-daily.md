---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-08-19)"
type: synthesis
created: 2026-08-19
updated: 2026-08-19
sources: []
tags: [game-rl, game-ai, self-play, llm-agent, foundation-model, pcg, benchmark, world-model]
---

# Game RL & Game AI Bot — Daily Paper Digest

> Curated arXiv and proceedings papers on Game RL, Game AI Bot, Game Foundation Models, PCG, Benchmarks, Industry Game AI, and Related Techniques. Generated 2026-08-19.

---

## 1. Game RL — Reinforcement Learning in Games

### 1.1 Superhuman AI for Generals.io Using Self-Play Reinforcement Learning
- **Authors**: Matěj Straka, Viliam Lisý, Martin Schmid
- **Affiliation**: Czech Technical University in Prague / Free League
- **Venue**: arXiv preprint, Jun 2026
- **Abstract**: Presents a superhuman AI agent for Generals.io, a real-time strategy game requiring long-horizon planning under imperfect information. Trained for 4 days on 4× NVIDIA H200 GPUs, the agent reaches #1 on the public 1v1 leaderboard of 5,000+ players and beats top-ranked humans 199–70 across 269 ladder matches. A key enabler is a JAX-native simulator achieving tens of millions of frames per second (~10,000× speedup). The agent uses a Vision Transformer policy trained end-to-end via policy-gradient self-play with sparse win/loss reward, top-advantage sample filtering, and EMA of policy parameters. Ablations show that behavior cloning, reward shaping, and population-based self-play are not required at this scale.
- **Key Innovations**: 10,000× faster JAX simulator; pure policy-gradient self-play from sparse reward alone in large RTS; EMA stabilizer; open-source 1v1/2v2/FFA simulator.
- **Link**: https://arxiv.org/abs/2606.23348

### 1.2 QZero: Mastering the Game of Go with Self-play Experience Replay
- **Authors**: Jingbin Liu, Xuechun Wang
- **Affiliation**: Independent / Tsinghua-affiliated
- **Venue**: arXiv preprint, Jan 2026
- **Abstract**: Proposes QZero, a model-free RL algorithm that forgoes MCTS and learns a Nash equilibrium policy through self-play and off-policy experience replay. Built on entropy-regularized Q-learning with a single Q-value network, trained tabula rasa (no human data) for 5 months on 7 GPUs, QZero achieves performance comparable to AlphaGo. Identifies three key components: an Ignition Mechanism (episode returns to initiate Q-learning), entropy regularization, and off-policy replay. Demonstrates the first efficient model-free RL approach to master Go.
- **Key Innovations**: First model-free off-policy RL to reach AlphaGo-level in Go; 7 GPUs vs. massive compute of AlphaGo; ignition mechanism for cold-start Q-learning.
- **Link**: https://arxiv.org/abs/2601.03306

### 1.3 Reproducing AlphaZero on Tablut: Self-Play RL for an Asymmetric Board Game
- **Authors**: Tõnis Lees, Tambet Matiisen
- **Affiliation**: University of Tartu
- **Venue**: arXiv preprint, Apr 2026
- **Abstract**: Investigates adapting AlphaZero to Tablut, an asymmetric board game with unequal piece counts and distinct objectives. Modifies the architecture to use separate policy/value heads per player role while sharing a residual trunk. Addresses catastrophic forgetting between attacker/defender roles via C4 data augmentation, larger replay buffers, and playing 25% of training games against randomly sampled past checkpoints. Over 100 self-play iterations, the model achieves BayesElo 1235 relative to random baseline.
- **Key Innovations**: Asymmetric AlphaZero architecture; anti-forgetting techniques for multi-role self-play; C4 augmentation for board games.
- **Link**: https://arxiv.org/abs/2604.05476

### 1.4 Data-Augmented Game Starts for Accelerating Self-Play Exploration in Imperfect Information Games
- **Authors**: JB Lanier, Nathan Monette, Pierre Baldi, Roy Fox
- **Affiliation**: UC Irvine
- **Venue**: arXiv preprint, May 2026
- **Abstract**: Proposes DAGS (Data-Augmented Game Starts), a starting-state sampling strategy for two-player zero-sum games that initializes RL episodes at intermediate states from offline gameplay data. Evaluates on synthetic datasets and control variants of Kuhn Poker, Goofspiel, and counterexample games. Under fixed compute budgets, DAGS enables regularized policy gradient methods to solve games with significantly more challenging exploration. Also proposes multi-task observation flags to mitigate biased equilibria from augmented starting states.
- **Key Innovations**: Off-policy starting-state sampling for self-play; multi-task observation flags to prevent equilibrium bias; new benchmark environments for exploration-heavy imperfect-information games.
- **Link**: https://arxiv.org/abs/2605.14379

### 1.5 Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning
- **Authors**: Chengshuai Shi, Wenzhe Li, Xinran Liang, Yizhou Lu, Wenjia Yang, Ruirong Feng, et al.
- **Affiliation**: Shanghai Jiao Tong University / Shanghai AI Lab
- **Venue**: arXiv preprint, May 2026
- **Abstract**: Studies RL-based training of VLMs for long-horizon decision-making in Super Mario Land (100+ turns). Proposes an adapted PPO variant with a lightweight turn-level critic, substantially improving training stability and sample efficiency over GRPO and Reinforce++. Introduces Odysseus, an open training framework that achieves 3× average game progress over frontier models. Trained models exhibit consistent improvements under both in-game and cross-game generalization while maintaining general-domain capabilities.
- **Key Innovations**: Turn-level critic for long-horizon VLM RL; PPO variant for multi-turn decision-making; cross-game generalization from game-trained VLMs; open-source framework.
- **Link**: https://arxiv.org/abs/2605.00347

### 1.6 From Player to Master: Enhancing Test-Time Learning of LLM Agents via Reinforcement Learning over Memory
- **Authors**: Yishuo Cai, Xingyu Guo, Xuancheng Huang, et al.
- **Affiliation**: Peking University / Tencent
- **Venue**: arXiv preprint, Jun 2026
- **Abstract**: Proposes MEMOPILOT, a plug-in memory copilot that explicitly trains the memory update process to improve a frozen LLM's performance across sequential interactions. Formulates memory updating as a multi-turn decision problem optimized end-to-end with multi-turn GRPO. Introduces turn-wise reward signals and context-independent, turn-level advantage estimation. Evaluated on multi-round Rock-Paper-Scissors and Limit Texas Hold'em, ranking first in Elo ratings on both games and outperforming DeepSeek V3.2.
- **Key Innovations**: RL-trained memory update for LLM agents; multi-turn GRPO with turn-level advantage; test-time learning in adversarial games.
- **Link**: https://arxiv.org/abs/2606.08656

### 1.7 STRATAGEM: Learning Transferable Reasoning via Trajectory-Modulated Game Self-Play
- **Authors**: (ACL 2026 proceedings)
- **Affiliation**: NUS / Alibaba
- **Venue**: ACL 2026
- **Abstract**: Addresses the problem that game-based RL training often learns game-specific heuristics rather than transferable reasoning. STRATAGEM introduces trajectory-modulated self-play that identifies and reinforces reasoning patterns that transfer across games, spanning mathematical reasoning, general reasoning, and code generation. Trained on three zero-sum games using Qwen models, demonstrating improved cross-domain reasoning.
- **Key Innovations**: Trajectory modulation for transferable reasoning from game self-play; cross-domain transfer from games to math/code.
- **Link**: https://aclanthology.org/2026.acl-long.897

---

## 2. Game AI Bot — LLM-Powered Game Agents

### 2.1 CAST: Game Solvers as Turn-Level Teachers for LLM Agents
- **Authors**: (Multiple authors)
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint, Jul 2026
- **Abstract**: Addresses the credit-assignment bottleneck in training LLM game agents with sparse terminal rewards. CAST converts game solver state-value changes into solver advantages and injects them into RLVR as turn-level signals. Under a soft-optimal solver assumption, maximizing solver advantage is equivalent to on-policy distillation from the solver using only scalar values (no teacher logits). Outperforms all trained baselines on Sokoban, Minesweeper, and Rush Hour; achieves highest zero-shot performance on ALFWorld and WebShop.
- **Key Innovations**: Solver-as-teacher turn-level credit assignment; logit-free on-policy distillation; generalizes across puzzle games and real-world tasks.
- **Link**: https://arxiv.org/abs/2607.25308

### 2.2 Environment-Grounded Automated Prompt Optimization for LLM Game Agents
- **Authors**: Rean Clive Fernandes, Lukas Fehring, Theresa Eimer, Marius Lindauer, Matthias Feurer
- **Affiliation**: University of Freiburg / Snorkel AI
- **Venue**: arXiv preprint, Jun 2026
- **Abstract**: Introduces RAPOA, an automated prompt optimization framework for LLM agents that decomposes observation-to-action into a goal-conditioned descriptor agent and an action selection agent. Uses an LLM-driven evolutionary loop guided by environment returns. On PutNext (a multi-step coordination task where RobustCoTAgent achieves 0% success), RAPOA reaches 72.5% success rate using the same underlying LLM.
- **Key Innovations**: Multi-agent prompt decomposition; behavior analyzer for outcome attribution; evolutionary prompt optimization without weight updates.
- **Link**: https://arxiv.org/abs/2606.17838

### 2.3 MEMO: Memory-Augmented Model Context Optimization for Robust Multi-Turn Multi-Agent LLM Games
- **Authors**: (Multiple authors)
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint, Mar 2026 (updated 2026)
- **Abstract**: Proposes MEMO, a self-play framework optimizing inference-time context without weight updates. Couples retention (persistent memory bank with CRUD operations) with exploration (tournament-style prompt evolution with TrueSkill and prioritized replay). Across five text-based games, raises GPT-4o-mini mean win rate from 25.1% to 49.5% and Qwen-2.5-7B from 20.9% to 44.3%, using 19× fewer games than RL baselines while reducing run-to-run variance by 7×.
- **Key Innovations**: Persistent memory bank for multi-agent LLM games; TrueSkill-guided prompt evolution; prioritized replay of rare states; weight-free optimization.
- **Link**: https://arxiv.org/abs/2603.09022

### 2.4 Hierarchical Control in Multi-Agent Games: LLM-based Planning and RL Execution
- **Authors**: (Multiple authors)
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint, Jun 2026
- **Abstract**: Proposes a two-layer hierarchical architecture where a Gemma 3 27B LLM acts as a centralized meta-controller selecting among 4 pretrained RL skill policies for a 2v2 King of the Hill game. Achieves task performance statistically equivalent to hand-crafted behavior trees (46.4% vs 51.5% win rate, p=0.103) while significantly outperforming Flat RL. User study (n=15) shows 60% perceive LLM+RL agents as most human-like.
- **Key Innovations**: LLM-orchestrated RL skill selection; hierarchical LLM+RL for competitive multi-agent games; human-likeness evaluation via user study.
- **Link**: https://arxiv.org/abs/2606.20014

### 2.5 Beyond Static Evaluation: Co-Evolutionary Mechanisms for LLM-Driven Strategy Evolution in Adversarial Games
- **Authors**: (Multiple authors)
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint / AAMAS 2026 MCTF Competition
- **Abstract**: Proposes FAMOU, extending LLM code-level evolution to adversarial multi-agent games with three mechanisms: evaluator co-evolution (incorporating champions into opponent pool), hierarchical deep evaluation (statistically reliable assessments), and weakness pressure (dynamically up-weighting hardest opponents). Achieves highest combined score (0.526) and 61.7% win rate on MCTF 2026 3v3 maritime capture-the-flag. LLM mutation generates tactical structures absent from seed strategies (lookahead search, adaptive interception). Won 1st in hardware round-robin at AAMAS 2026 competition.
- **Key Innovations**: Evaluator co-evolution for adversarial LLM code evolution; hierarchical deep evaluation; weakness pressure; LLM-generated novel tactical structures.
- **Link**: https://arxiv.org/abs/2606.10389

### 2.6 AutoHarness: Improving LLM Agents by Automatically Synthesizing a Code Harness
- **Authors**: (Google DeepMind affiliated)
- **Affiliation**: Google DeepMind
- **Venue**: arXiv preprint, Mar 2026
- **Abstract**: Demonstrates that Gemini-2.5-Flash can automatically synthesize code harnesses to prevent illegal moves. In Kaggle GameArena chess competition, 78% of Gemini-2.5-Flash losses were from illegal moves. The resulting harness prevents all illegal moves in 145 TextArena games, enabling the smaller model to outperform Gemini-2.5-Pro. Pushing further, Gemini-2.5-Flash generates entire policies in code, eliminating LLM at decision time, achieving higher average reward than GPT-5.2-High on 16 TextArena 1-player games.
- **Key Innovations**: Auto-synthesized code harness to prevent illegal moves; full policy-as-code eliminating runtime LLM inference; smaller model outperforming larger via harness.
- **Link**: https://arxiv.org/abs/2603.03329

### 2.7 Generative Gamer: Learning Equilibrium Strategy by LLM-driven Dynamic Deduction
- **Authors**: Yadong Zhang, Xinshu Shen, Yupei Ren, Shangqing Zhao, Man Lan
- **Affiliation**: East China Normal University
- **Venue**: ACL 2026
- **Abstract**: Introduces GenGamer, a framework training LLMs to reason like expert players by generating compact, pruned reasoning trajectories (Dynamic Deduction). Integrates action pruning (policy confidence), state pruning (value estimation), and branch pruning (alpha-beta principles). Proposes Deduction Tree Reward (DTR) for step-by-step process feedback. Experiments on Tic-Tac-Toe and Leduc Poker show performance surpassing current state-of-the-art LLMs.
- **Key Innovations**: Dynamic deduction for LLM game reasoning; process-oriented DTR reward; action/state/branch pruning for game tree search.
- **Link**: https://aclanthology.org/2026.acl-long.574

### 2.8 Training a Conditioned Video Game Agent on a VLM Annotated Dataset
- **Authors**: K. Schmid, I. Frosio
- **Affiliation**: NVIDIA
- **Venue**: arXiv preprint, Aug 2026
- **Abstract**: Proposes annotating video game datasets with VLMs (Qwen-3.5) to extract human-defined rewards, then training conditioned offline RL agents that respond to desired returns. Evaluated on Trackmania racing game with 25K frames annotated at 0.3s intervals. Discusses difficulties including sparse rewards in annotation and distribution shift in conditioned inference.
- **Key Innovations**: VLM-based dataset annotation for game rewards; conditioned offline RL for return-controllable game agents; no game engine access required.
- **Link**: https://arxiv.org/abs/2608.05954

### 2.9 GIFT: Games as Informal Training for Generalizable LLMs
- **Authors**: Nuoyan Lyu, Bingbing Xu, Tian, Xueyun, Weihao Meng, Yige Yuan, Yang Zhang, et al.
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint, Jan 2026
- **Abstract**: Proposes treating games as environments for LLM informal learning via GRPO-based RL across Matrix Games, TicTacToe, and Who's the Spy. Introduces Nested Training Framework enforcing explicit "AND" objective (master all abilities simultaneously) vs naive task-mixing's implicit "OR" objective. Game-augmented formal learning improves general ability from 38.34% to 42.43% (1.5B) and from 42.00% to 55.84% (7B models) on broad ability benchmarks.
- **Key Innovations**: Games as informal learning for LLM generalization; nested training framework; game-based training improves broad reasoning capabilities.
- **Link**: https://arxiv.org/abs/2601.05633

---

## 3. Game Foundation Models

### 3.1 NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, et al.
- **Affiliation**: NVIDIA / Caltech / UT Austin / UW / UC Berkeley
- **Venue**: CVPR 2026
- **Abstract**: Introduces NitroGen, a vision-action foundation model trained on 40,000 hours of gameplay videos across 1,000+ games. Three key ingredients: (1) internet-scale video-action dataset from overlay input commands in gameplay videos, (2) multi-game benchmark (30 tasks across 10 commercial games), (3) unified vision-action model via large-scale behavior cloning. Achieves up to 52% relative improvement in task success rates over scratch-trained models via fine-tuning. Released dataset, evaluation suite, and model weights.
- **Key Innovations**: Largest open gaming dataset (40K hours, 1K+ games); universal Gymnasium API harness; cross-game generalization from internet-scale BC pre-training.
- **Link**: https://arxiv.org/abs/2601.02427

### 3.2 Towards Generalist Game Players: An Investigation of Foundation Models in the Game Multiverse
- **Authors**: Kuan Zhang, Dongchen Liu, Qiyue Zhao, Tianyu Xin, Yue Su, Haisheng Wang, et al.
- **Affiliation**: Tsinghua University / THUSI Lab
- **Venue**: arXiv preprint, May 2026
- **Abstract**: Comprehensive survey tracing the lifecycle of generalist game players across four pillars: Dataset, Model, Harness, and Benchmark. Identifies five fundamental trade-offs bounding the system. Proposes a five-level roadmap from single-game mastery to a "creator" stage where the agent creates new game worlds and evolves within them. Covers LLM, VLM, VA, and VLA models across dozens of games including Minecraft, StarCraft II, Go, chess, poker, and more.
- **Key Innovations**: First systematic lifecycle investigation of foundation models as game players; five-level roadmap to AGI through games; comprehensive taxonomy of 50+ game-playing models.
- **Link**: https://arxiv.org/abs/2605.09965

---

## 4. Procedural Content Generation

### 4.1 PCGRLLM: LLM-Driven Reward Design for Procedural Content Generation RL
- **Authors**: (Korean research group)
- **Affiliation**: Korean institutions
- **Venue**: arXiv preprint, Feb 2026 (updated May 2026)
- **Abstract**: Introduces PCGRLLM, an improved architecture for LLM-driven reward generation for PCGRL. Employs feedback mechanism and reasoning-based prompt engineering for story-to-reward generation in 2D environments. Two state-of-the-art LLMs evaluated across various reasoning prompts. Achieves performance comparable to human-designed rewards, demonstrating potential to reduce human dependency in game AI development.
- **Key Innovations**: Feedback-based LLM reward refinement for PCG; self-alignment + feedback loop; reasoning-based prompt engineering for reward code generation.
- **Link**: https://arxiv.org/abs/2502.10906

### 4.2 MIPCGRL: Multi-Objective Instruction-Aware Representation Learning in PCG RL
- **Authors**: S. Kim, G. Hwang, I. Baek, S. Lee, K. Kim
- **Affiliation**: Korean institutions
- **Venue**: arXiv preprint, Aug 2026
- **Abstract**: Proposes MIPCGRL for multi-objective natural language conditioned level generation. Incorporates sentence embeddings with multi-label classification and multi-head regression for disentangled task-specific representations. Achieves 13.8% improvement in controllability over IPCGRL for multi-objective instructions. Enables complex instructions like "Long path and many bats" for level generation.
- **Key Innovations**: Multi-objective instruction representation for PCGRL; disentangled task-specific embedding; multi-label classification + multi-head regression.
- **Link**: https://arxiv.org/abs/2508.09193

### 4.3 Learning Local Constraints for Reinforcement-Learned Content Generators
- **Authors**: Debosmita Bhaumik, Julian Togelius, Georgios N. Yannakakis, Ahmed Khalifa
- **Affiliation**: ITU Copenhagen / NYU
- **Venue**: arXiv preprint, May 2026
- **Abstract**: Combines Wave Function Collapse (WFC) constraints with PCGRL to generate visually satisfying and playable game levels. Constrains the PCGRL generator's action space with WFC-learned local constraints, achieving both visual quality and global properties (playability). Evaluated on Lode Runner levels, demonstrating that the hybrid approach outperforms either method alone.
- **Key Innovations**: WFC+PCGRL hybrid for visual quality + playability; Lode Runner as a harder PCG testbed; analysis of input diversity and pattern filtering effects.
- **Link**: https://arxiv.org/abs/2605.13570

### 4.4 MAGIC: Transition-Aware Generation of Navigable Multi-Scene Game Worlds with LLMs
- **Authors**: Tsz Hei Fan, Choi Wing Fung, Yuxuan Wan, Shuqing Li, Michael R. Lyu
- **Affiliation**: CUHK
- **Venue**: arXiv preprint, Jul 2026
- **Abstract**: Presents MAGIC, a prompt-to-project system generating runnable multi-scene game projects. Addresses three obstacles: cross-scene consistency (via transition-aware IR), in-scene navigability (flood-fill validator), and transition evaluation (agent that runs each transition in play). Achieves 0.99 precision, 0.95 recall, 0.96 F1 on 100 multi-scene cases. Produces executable Unity projects for every case.
- **Key Innovations**: Multi-scene coherent generation; transition-aware intermediate representation; flood-fill navigability validation; transition-focused evaluation agent.
- **Link**: https://arxiv.org/abs/2607.11594

### 4.5 OpenGame: Open Agentic Coding for Games
- **Authors**: Yilei Jiang, Jinyuan Hu, Qianyin Xiao, Yaozhi Zheng, et al.
- **Affiliation**: Shanghai Jiao Tong University / Shanghai AI Lab
- **Venue**: arXiv preprint, Apr 2026
- **Abstract**: Presents OpenGame, an open-source agentic framework for end-to-end web game creation from natural language. Core model GameCoder-27B trained via continual pre-training, SFT, and execution-grounded RL. Introduces Game Skill (Template Skill + Debug Skill) and OpenGame-Bench evaluating Build Health, Visual Usability, and Intent Alignment. Establishes new SOTA across 150 diverse game prompts.
- **Key Innovations**: GameCoder-27B domain-specialized code model; Template Skill (emerging template families) + Debug Skill (cumulative error repair); execution-grounded RL for game code.
- **Link**: https://arxiv.org/abs/2604.18394

### 4.6 IPCGRL: Language-Instructed Reinforcement Learning for Procedural Level Generation
- **Authors**: (Multiple authors)
- **Affiliation**: Korean institutions
- **Venue**: arXiv preprint, Mar 2026 (updated)
- **Abstract**: Proposes IPCGRL, an instruction-based PCGRL method incorporating sentence embedding models. Fine-tunes task-specific embeddings to compress game-level conditions. Achieves 21.4% improvement in controllability and 17.2% in generalizability for unseen instructions over general-purpose embeddings. Extends conditional input modality for more flexible procedural content generation.
- **Key Innovations**: Language-conditioned PCGRL; fine-tuned task-specific sentence embeddings; improved generalization to unseen natural language instructions.
- **Link**: https://arxiv.org/abs/2503.12358

---

## 5. Game Benchmarks

### 5.1 OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics
- **Authors**: (Multiple authors)
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint, Jun 2026
- **Abstract**: Introduces OmniGameArena, a real-time benchmark of 12 newly built Unreal Engine 5 games spanning Solo (7), PvP (3), and Coop (2) with unified action interfaces. Proposes IDC (Improvement Dynamics Curve), an agentic-reflection harness where a reflector LLM autonomously refines skill prompts across rounds. Evaluates 12 VLM agents including Claude Opus 4.7, GPT-5.5, Gemini 3.1 Pro, NitroGen, and Open-P2P. Key finding: leadership rotates across games and origin-task gain doesn't predict held-out transfer.
- **Key Innovations**: 12 UE5 games (Solo/PvP/Coop) with unified interfaces; IDC self-improvement protocol; cross-game transfer evaluation; evaluation of specialized vs generalist game policies.
- **Link**: https://arxiv.org/abs/2606.09826

### 5.2 RNG-Bench: Reconstructive Non-Markov Games Benchmark
- **Authors**: Shengyuan Ding, Xilin Wei, Xinyu Fang, et al.
- **Affiliation**: Shanghai Jiao Tong University / Shanghai AI Lab
- **Venue**: arXiv preprint, Jun 2026
- **Abstract**: Introduces RNG-Bench, two games (Matching Pairs and 3D Maze) under a unified closed-loop harness testing hidden-state reconstruction during multi-step interaction. Three controlled difficulty axes: grid size, visual pattern, observation modality. Hardest configs require ~128K tokens and 350 image inputs per episode. Introduces Memory Gap metric disentangling forgetting from poor action selection. Fine-tuning Qwen3.5-9B on optimal-policy rollouts improves performance and transfers to existing benchmarks.
- **Key Innovations**: Non-Markov game benchmark isolating belief-state tracking; Memory Gap metric; head-to-head duel protocol; training data from simulator rollouts.
- **Link**: https://arxiv.org/abs/2606.19338

### 5.3 GameCraft-Bench: Can Agents Build Playable Games End-to-End in a Real Game Engine?
- **Authors**: (Multiple authors)
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint, Jun 2026
- **Abstract**: Introduces GameCraft-Bench, 140 Godot tasks across 15 game families evaluating end-to-end game generation. Requires Engine Grounding, Artifact Completeness, and Interactive Verification. Strongest agent (Claude Code + Opus 4.7) achieves only 41.46%. Most agents score below 40%. Analysis reveals agents implement recognizable mechanics but struggle with complete games, content depth, visual feedback, and coherent presentation.
- **Key Innovations**: Real Godot engine benchmark; interaction-grounded evaluation via replayed demonstrations; 140 tasks across 15 game families; current agents far from reliable game generation.
- **Link**: https://arxiv.org/abs/2606.17861

### 5.4 GameDevBench: Evaluating Agentic Capabilities Through Game Development
- **Authors**: Wayne Chi, Yixiong Fang, et al.
- **Affiliation**: CMU / Stanford
- **Venue**: arXiv preprint, Feb 2026
- **Abstract**: First benchmark for evaluating agents on game development tasks (132 tasks from Godot tutorials). Tasks require 3× more LOC changes than SWE-Bench. Best agent solves only 54.5%. Success rates drop from 46.9% on gameplay tasks to 31.6% on 2D graphics tasks. Introduces image and video-based feedback mechanisms; Claude Sonnet 4.5 improves from 33.3% to 47.7% with visual feedback.
- **Key Innovations**: First game development benchmark; tutorial-derived diverse tasks; multimodal feedback mechanisms; strong correlation between multimodal complexity and task difficulty.
- **Link**: https://arxiv.org/abs/2602.11103

### 5.5 AutoWorldModel-Bench: A State-Centric Benchmark for Automated World-Model Research
- **Authors**: (EA Research / affiliated)
- **Affiliation**: Electronic Arts
- **Venue**: arXiv preprint, Aug 2026
- **Abstract**: Closed-loop benchmark where coding agents autonomously improve world models across 8 game environments under unified structured-state representation. Codex-5.4 and Claude Opus 4.6 improve base models in 63/64 sessions, with mean test-score lift of +0.196. In 91% of sessions, winning edits are substantive model/training changes. 33/64 sessions show substantial gains (Δ≥0.10). Improvement concentrated at long-horizon rollout rather than one-step fit.
- **Key Innovations**: Autonomous world-model research benchmark; unified structured-state representation across 8 games; agent-as-researcher paradigm; long-horizon rollout improvement.
- **Link**: https://arxiv.org/abs/2608.11216

### 5.6 Agent Island: A Saturation- and Contamination-Resistant Benchmark from Multiagent Games
- **Authors**: Connacher Murphy
- **Affiliation**: Independent
- **Venue**: arXiv preprint, May 2026
- **Abstract**: Introduces Agent Island, a multiplayer simulation environment where LM agents compete in cooperation, conflict, and persuasion. Dynamic benchmark mitigating saturation and contamination: new models can always outperform leaders; agents compete against adaptive opponents. 999 games with 49 unique models; GPT-5.5 dominates with posterior mean skill 5.64 vs. 3.10 for second. Discovers 8.3pp same-provider preference in final-round votes.
- **Key Innovations**: Dynamic benchmark resistant to saturation/contamination; Bayesian Plackett-Luce ranking; cross-model behavioral analysis; same-provider voting bias discovery.
- **Link**: https://arxiv.org/abs/2605.04312

---

## 6. World Models for Games

### 6.1 WorldCompass: RL for Long-Horizon World Models
- **Authors**: (Tencent Hunyuan team)
- **Affiliation**: Tencent
- **Venue**: arXiv preprint, Feb 2026
- **Abstract**: Proposes WorldCompass, an RL post-training framework for long-horizon interactive video-based world models. Introduces clip-level rollout strategy (reducing complexity from O(N·G) to O(N+G)), complementary reward functions (interaction-following accuracy + visual quality), and negative-aware fine-tuning. Applied to WorldPlay, improves complex composite action accuracy from ~20% to 55%.
- **Key Innovations**: Clip-level rollout for autoregressive video world models; complementary reward to suppress reward hacking; RL post-training for world models.
- **Link**: https://arxiv.org/abs/2602.09022

### 6.2 OPINE-World: Programmatic World Modeling with Ontology-error-Prioritized Interactive Exploration
- **Authors**: David Courtis, Wenhao Li, Scott Sanner
- **Affiliation**: University of Toronto
- **Venue**: arXiv preprint, Jul 2026
- **Abstract**: Introduces OPINE-World, an LLM agent learning object-centric programmatic world models online from interaction. Two cooperating LLM agents run hypothesis-and-test loops with CEGIS verification and model-based planning. Uses Bayesian "ontology error" to steer exploration toward unexplained objects. Solves 20/25 ARC-AGI-3 games without per-game training (action-efficiency score 78.4 vs. human baseline).
- **Key Innovations**: Programmatic world model from interaction (no pre-training); ontology error for exploration steering; two-agent hypothesis-test loop; ARC-AGI-3 solver.
- **Link**: https://arxiv.org/abs/2607.01531

---

## 7. Related Techniques

### 7.1 Curiosity-Critic: Cumulative Prediction Error as Intrinsic Reward for World Model Training
- **Authors**: Vin Bhaskara, Haicheng Wang
- **Affiliation**: (University-affiliated)
- **Venue**: arXiv preprint, Apr 2026
- **Abstract**: Introduces Curiosity-Critic, grounding intrinsic reward in cumulative prediction error improvement across all visited transitions. Reduces to tractable per-step form: difference between current prediction error and learned asymptotic baseline. A learned critic co-trained with the world model separates epistemic from aleatoric prediction error online. Outperforms prediction-error and visitation-count baselines on stochastic grid world.
- **Key Innovations**: Cumulative prediction error improvement as reward; learned critic for asymptotic baseline; online separation of epistemic vs aleatoric error.
- **Link**: https://arxiv.org/abs/2604.18701

### 7.2 Remember to be Curious: Episodic Context and Persistent Worlds for 3D Exploration
- **Authors**: Lily Goli, Justin Kerr, Daniele Reda, et al.
- **Affiliation**: UC Berkeley / Google
- **Venue**: arXiv preprint, May 2026
- **Abstract**: Demonstrates that effective curiosity in 3D environments requires spatial persistence and episodic context. Uses online 3D Gaussian Splatting as persistent world model and a sequence agent over RGB observations for episodic context. Trained purely via curiosity on HM3D, outperforms active mapping baselines and generalizes zero-shot to Gibson and AI-generated worlds. Enables downstream task adaptation (apple picking, image-goal navigation).
- **Key Innovations**: Persistent 3D reconstruction as curiosity world model; episodic sequence architecture for exploration; pure curiosity training for 3D navigation.
- **Link**: https://arxiv.org/abs/2605.22814

### 7.3 GLANCE: Driving Exploration in VLM Agents via Visual-Linguistic Curiosity
- **Authors**: Haoxi Li, Qinglin Hou, Jianfei Ma, et al.
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint, May 2026
- **Abstract**: Proposes GLANCE, bridging VLM reasoning and exploration by grounding linguistic predictions into visual representations via a momentum-updated target network. Uses discrepancy between linguistic prediction and visual reality as intrinsic curiosity reward. Introduces Curriculum Exploration (periodic projector re-initialization) to prevent curiosity drain. Evaluated on grid puzzles, 3D navigation, object manipulation, and geometric reconstruction.
- **Key Innovations**: Cross-modal curiosity (linguistic-visual discrepancy); curriculum exploration via projector rejuvenation; VLM as both world model and policy.
- **Link**: https://arxiv.org/abs/2605.03782

### 7.4 From Curiosity to Competence: How World Models Interact with the Dynamics of Exploration
- **Authors**: (Multiple authors)
- **Affiliation**: Multiple institutions
- **Venue**: arXiv preprint, Jul 2025
- **Abstract**: Bridges cognitive theories of intrinsic motivation with RL, studying how evolving internal representations mediate the curiosity-competence trade-off. Compares Tabular (handcrafted) and Dreamer (learned) agents. Dreamer agent reveals two-way interaction between exploration and representation learning, mirroring developmental co-evolution of curiosity and competence.
- **Key Innovations**: Formalizes adaptive exploration as curiosity-competence balance; empirical comparison of tabular vs learned world models for exploration; cognitive-RL bridge.
- **Link**: https://arxiv.org/abs/2507.08210

---

## Summary of Trends

1. **Self-play RL remains powerful**: Pure policy-gradient self-play from sparse reward reaches superhuman in Generals.io; model-free off-policy RL matches AlphaGo in Go.
2. **LLM agents are rapidly advancing in games**: Solver-as-teacher (CAST), memory optimization (MEMO/MEMOPILOT), hierarchical LLM+RL, and automated prompt optimization all show strong results.
3. **Game foundation models maturing**: NitroGen (CVPR 2026) demonstrates internet-scale pre-training for generalist gaming agents; comprehensive surveys map the field.
4. **PCG increasingly LLM-driven**: LLM reward design, instruction-conditioned level generation, and multi-scene world generation show LLMs transforming content creation.
5. **New benchmarks proliferate**: OmniGameArena (UE5), RNG-Bench (non-Markov), GameCraft-Bench (Godot), GameDevBench, AutoWorldModel-Bench, and Agent Island address different evaluation gaps.
6. **Curiosity and world models**: Persistent 3D reconstruction, cross-modal curiosity, and programmatic world models are advancing exploration in complex environments.
7. **Code evolution over policy learning**: LLM code-level evolution (FAMOU) generates novel tactical structures, suggesting a shift from learning policies to evolving strategy code.
