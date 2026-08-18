---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-08-18)"
type: synthesis
created: 2026-08-18
updated: 2026-08-18
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, world-models, pcg, benchmarks, self-play, multi-agent-rl, hierarchical-rl, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-08-18)

> Comprehensive scan of arXiv and recent proceedings for Game RL, Game AI Bot, Game Foundation Models, PCG, Benchmarks, Industry Game AI, and related techniques.

---

## 1. Game RL — Reinforcement Learning in Games

### 1.1 Superhuman AI for Generals.io Using Self-Play Reinforcement Learning

- **Authors:** Matěj Straka, Viliam Lisý, Martin Schmid
- **Affiliation:** (Czech Technical University / CTU AI Center)
- **Venue:** arXiv preprint (2026-06-22)
- **arXiv:** https://arxiv.org/abs/2606.23348
- **Abstract:** Presents a superhuman AI agent for Generals.io, a real-time strategy game requiring long-horizon planning and short-term tactics under imperfect information. Trained for four days on 4× NVIDIA H200 GPUs, the agent reaches #1 on the public 1v1 leaderboard of 5,000+ players and beats the two top-ranked humans head-to-head (199–70 record across 269 matches). A JAX-native simulator achieves tens of millions of FPS on a single GPU (~10,000× speedup over prior). The agent is a vision transformer trained end-to-end via self-play PPO with sparse win/loss reward only.
- **Key innovations:** (1) ~10,000× faster JAX-native simulator removing the data bottleneck; (2) pure policy-gradient self-play with sparse reward achieves superhuman play in RTS — no behavior cloning, no reward shaping, no population-based training required; (3) top-advantage sample filtering and exponential moving average (EMA) of policy parameters as key practical ingredients; (4) releases 1v1, 2v2, and free-for-all environments.

### 1.2 EMAgnet: Parameter-Space EMA Regularization for Policy Gradient Self-Play

- **Authors:** (Multiple authors from CMU / DeepMind ecosystem)
- **Affiliation:** (Carnegie Mellon University / related)
- **Venue:** arXiv preprint (2026)
- **arXiv:** https://arxiv.org/abs/2606.23995
- **Abstract:** Introduces EMAgnet, which replaces uniform entropy regularization in self-play with an EMA of the policy's own parameters as the regularization target. This adaptive target evolves with the agent's strategy — forgetting bad strategies while remembering good ones. PPO-EMAg matches or outperforms uniform-magnet baselines on standard benchmarks and outperforms them in games containing strictly dominated strategies.
- **Key innovations:** (1) Parameter-space EMA regularization extending tabular "moving magnet" to deep RL; (2) adaptive regularization that avoids wasting budget on dominated strategies; (3) consistent gains across games with large numbers of strictly dominated actions.

### 1.3 GARIP: A Running-Average Moving Reference for Last-Iterate Self-Play

- **Authors:** (Multiple authors)
- **Venue:** arXiv preprint (2026)
- **arXiv:** https://arxiv.org/abs/2606.22688
- **Abstract:** Studies GARIP, which anchors self-play to the policy's running average rather than periodic snapshots (R-NaD) or fixed magnets (MMD). The running average has a flat lag profile that uniquely minimizes peak lag among causal convex averages at fixed mean lag, making it the collapse-optimal reference shape. GARIP matches R-NaD's peak performance but is a better hyperparameter default — at conventional parameterizations, 0/40 seeds collapse vs 10/40 for snapshots.
- **Key innovations:** (1) Flat lag profile analysis proving running average is peak-minimizing; (2) local last-iterate convergence theorem at constant anchor strength; (3) robust self-play across matrix games, Coin Game, Connect Four, and Othello.

### 1.4 Reproducing AlphaZero on Tablut: Self-Play RL for Asymmetric Board Games

- **Authors:** (Multiple authors)
- **Venue:** arXiv preprint (2026-04-07)
- **arXiv:** https://arxiv.org/abs/2604.05476
- **Abstract:** Investigates adapting AlphaZero to Tablut, an asymmetric historical board game with unequal piece counts and distinct objectives. Modifies the architecture with separate policy/value heads per player role while sharing a residual trunk. Addresses catastrophic forgetting between attacker/defender roles via C4 data augmentation, enlarged replay buffer, and 25% random checkpoint opponents. Achieves BayesElo 1235 over 100 iterations.
- **Key innovations:** (1) Separate heads for asymmetric roles with shared trunk; (2) mitigation of role-interference catastrophic forgetting; (3) demonstration that AlphaZero transfers to highly asymmetric games.

### 1.5 Self-Play RL under Imperfect Information in Big 2

- **Authors:** Aalok Patwa
- **Venue:** arXiv preprint (2026-05-21)
- **arXiv:** https://arxiv.org/abs/2605.28863
- **Abstract:** Develops a self-play RL framework for Big 2, a four-player imperfect-information card game. Under a common environment and training budget, PPO outperforms Monte Carlo Q approximation, SARSA, and Q-learning. Finds that moderate entropy regularization improves PPO and current-policy self-play provides stronger curriculum than checkpoint self-play or fixed-opponent training.
- **Key innovations:** (1) First controlled study of RL objectives for Big 2; (2) demonstrates PPO superiority over value-based methods in multiplayer imperfect-info card games; (3) characterizes entropy regularization sweet spot.

### 1.6 Data-Augmented Game Starts (DAGS) for Accelerating Self-Play Exploration

- **Authors:** JB Lanier, Nathan Monette, Pierre Baldi, Roy Fox
- **Affiliation:** UC Irvine
- **Venue:** arXiv preprint (2026-05-14)
- **arXiv:** https://arxiv.org/abs/2605.14379
- **Abstract:** Proposes DAGS — a starting-state sampling strategy that initializes self-play episodes at intermediate states from offline gameplay data. Enables regularized policy gradient methods to solve games with significantly more challenging exploration under fixed budgets. Introduces new benchmark games wrapping standard OpenSpiel games with gridworld control tasks. Identifies equilibrium bias from modified starting-state distributions and provides multi-task observation flag mitigation.
- **Key innovations:** (1) Starting-state sampling from offline data for exploration acceleration; (2) analytically reducible gridworld-extended benchmarks; (3) multi-task observation flag for equilibrium bias mitigation.

### 1.7 Stratagem: Learning Transferable Reasoning via Trajectory-Modulated Game Self-Play

- **Authors:** Xiachong Feng, Deyi Yin, Xiaocheng Feng, Yi Jiang, Libo Qin, Yangfan Ye, et al.
- **Venue:** arXiv preprint (2026-04-20)
- **arXiv:** https://arxiv.org/abs/2604.17696
- **Abstract:** Proposes STRATAGEM, which trains LLMs through self-play on text-based zero-sum games with two complementary signals: a Reasoning Transferability Coefficient measuring abstraction level, and a Reasoning Evolution Reward incentivizing progressive adaptation. Addresses domain specificity and contextual stasis barriers to reasoning transfer from games to math/code.
- **Key innovations:** (1) Trajectory advantage modulation for transferable reasoning; (2) game-to-domain transfer on math, general reasoning, and code generation benchmarks.

---

## 2. Game AI Bot — LLM-Powered Game Agents

### 2.1 CAST: Game Solvers as Turn-Level Teachers for LLM Agents

- **Authors:** (Multiple authors)
- **Venue:** arXiv preprint (2026)
- **arXiv:** https://arxiv.org/abs/2607.25308
- **Abstract:** Addresses the sparse-reward credit assignment problem in training LLM game agents via RLVR. Proposes CAST — converts game solver state-value changes into per-turn solver advantages injected into RLVR as dense process signals. Under soft-optimal solver assumption, this is equivalent to on-policy distillation requiring only scalar values (not teacher logits). Outperforms all baselines on Sokoban, Minesweeper, Rush Hour and achieves best zero-shot on ALFWorld/WebShop.
- **Key innovations:** (1) Solver-as-teacher turn-level credit assignment; (2) logit-free on-policy distillation equivalence theorem; (3) scalable fine-grained learning signals for LLM game agents.

### 2.2 Hierarchical Control in Multi-Agent Games: LLM Planning + RL Execution

- **Authors:** (Multiple authors)
- **Venue:** arXiv preprint (2026)
- **arXiv:** https://arxiv.org/abs/2606.20014
- **Abstract:** Proposes a hierarchical architecture where a pretrained Gemma 3 27B LLM acts as centralized strategic controller selecting among specialized PPO skill policies for a team of agents. Evaluated in competitive 2v2 King of the Hill. Achieves performance statistically equivalent to hand-crafted behavior trees (46.4% vs 51.5%, p=0.103) and significantly outperforms flat RL. User study: 60% perceive LLM+RL agents as most human-like (p=0.027).
- **Key innovations:** (1) LLM as strategic meta-controller over pretrained RL skills; (2) competitive multi-agent coordination without manual rule engineering; (3) human perception evaluation showing superior believability.

### 2.3 Spatial Reasoning in LLM Game Agents: Causal Context and Multi-Step Planning

- **Authors:** (Multiple authors, IEEE publication)
- **Venue:** IEEE (2026)
- **arXiv:** https://arxiv.org/abs/2607.22732
- **Abstract:** Examines LLM game agent failures in spatial reasoning using a GVGAI benchmark with 3 custom games × 5 difficulty levels. Using Qwen3 models, finds that causal prompt augmentation improves win rates by ~5.35% for 8B models, thinking mode improves by ~36%, and multi-step planning improves up to 45% while reducing per-step response time.
- **Key innovations:** (1) Controlled GVGAI spatial reasoning benchmark for LLMs; (2) demonstrates planning horizon as best practical intervention balancing performance and latency.

### 2.4 Environment-Grounded Automated Prompt Optimization for LLM Game Agents (RAPOA)

- **Authors:** Rean Clive Fernandes, Lukas Fehring, Theresa Eimer, Marius Lindauer, Matthias Feurer
- **Venue:** arXiv preprint (2026-06-16)
- **arXiv:** https://arxiv.org/abs/2606.17838
- **Abstract:** Introduces RAPOA — automated prompt optimization framework that decomposes observation-to-action into a descriptor agent and action selection agent, iteratively refined via LLM-driven evolutionary loop guided by environment returns. On PutNext (where RobustCoTAgent achieves 0%), RAPOA reaches 72.5% success rate using the same underlying LLM.
- **Key innovations:** (1) Multi-agent prompt decomposition for game playing; (2) behavior analyzer for outcome attribution; (3) massive gains from prompt optimization alone (no weight updates).

### 2.5 Bounded Autonomy: Controlling LLM Characters in Live Multiplayer Games

- **Authors:** (Multiple authors)
- **Venue:** arXiv preprint (2026)
- **arXiv:** https://arxiv.org/abs/2604.04703
- **Abstract:** Frames the problem of LLM character control in live multiplayer games as bounded autonomy. Presents a three-interface architecture: agent-agent interaction (reply-chain decay), agent-world action execution (embedding-based grounding with fallback), and player-agent steering (whisper soft-steering). Deployed in a live multiplayer social game.
- **Key innovations:** (1) Probabilistic reply-chain decay for interaction stability; (2) embedding-based action grounding with fallback; (3) whisper — lightweight soft-steering technique for player influence during autonomous play.

### 2.6 Continual Harness: Online Adaptation for Self-Improving Foundation Agents

- **Authors:** (Princeton / DeepMind ecosystem)
- **Venue:** arXiv preprint (2026-08-11)
- **arXiv:** https://arxiv.org/abs/2605.09998
- **Abstract:** Introduces Continual Harness — a reset-free self-improving framework for embodied agents (tested on Pokémon). Gemini Plays Pokémon (GPP) became the first AI system to complete Pokémon Blue, Yellow Legacy (hard mode), and Crystal without lost battles. The agent alternates between acting and refining its own prompt, sub-agents, skills, and memory. Online co-learning loop with frontier teacher model relabeling drives sustained progress.
- **Key innovations:** (1) First AI to complete multiple Pokémon RPGs; (2) reset-free online self-improvement without episode boundaries; (3) joint model-harness co-learning through online process-reward loop.

---

## 3. Game Foundation Models

### 3.1 NitroGen: An Open Foundation Model for Generalist Gaming Agents

- **Authors:** Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi Fan
- **Affiliation:** NVIDIA, UW, Caltech, UT Austin, MIT
- **Venue:** CVPR 2026 (pp. 21511-21521)
- **arXiv:** https://arxiv.org/abs/2601.02427
- **Abstract:** Vision-action foundation model trained on 40,000 hours of gameplay videos across 1,000+ games. Uses flow matching (adapted from GR00T N1) with SigLIP 2 vision encoder + diffusion transformer. Internet-scale dataset extracted from public gameplay videos with overlay input commands. Multi-game benchmark with 30 tasks across 10 commercial games. Pre-training transfers to unseen games with up to 52% relative improvement.
- **Key innovations:** (1) Internet-scale action-labeled gameplay dataset (40K hours, 1000+ games); (2) universal Gymnasium API wrapper for commercial games; (3) pure vision-action model (no language conditioning) achieving cross-game generalization; (4) released dataset, simulator, and weights.

### 3.2 Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents

- **Authors:** (ByteDance Seed team)
- **Affiliation:** ByteDance
- **Venue:** arXiv preprint (2025/2026)
- **arXiv:** https://arxiv.org/abs/2510.23691
- **Abstract:** Generalist game agent trained with unified action space anchored to human-aligned keyboard-mouse inputs (not API/GUI). Pre-trained on 500B+ tokens spanning game trajectories, AI agent trajectories, and multimodal data. Achieves ~2× SOTA success rate in Minecraft, near-human generalization in unseen web 3D games, outperforms GPT-5, Gemini-2.5-Pro, Claude-4-Sonnet on FPS benchmarks. Uses Sparse-Thinking strategy balancing reasoning depth and inference cost.
- **Key innovations:** (1) Human-native interaction paradigm via native keyboard-mouse action space; (2) 500B token scale cross-domain pre-training; (3) decaying continual loss to reduce causal confusion; (4) Sparse-Thinking for reasoning-cost balance.

### 3.3 Towards Generalist Game Players: Foundation Models in the Game Multiverse (Survey)

- **Authors:** Kuan Zhang, Dongchen Liu, Qiyue Zhao, Tianyu Xin, Yue Su, Haisheng Wang, et al.
- **Affiliation:** Tsinghua University (THUSI-Lab)
- **Venue:** arXiv preprint (2026-05-11)
- **arXiv:** https://arxiv.org/abs/2605.09965
- **Abstract:** Comprehensive survey tracing game-playing AI through four eras (Symbolic → Deep RL → Foundation Models → Creator/Demiurge). Organizes around four pillars (Dataset, Model, Harness, Benchmark) and five fundamental trade-offs. Charts a five-level roadmap from single-game mastery to the Demiurge stage where agents become the game simulator itself.
- **Key innovations:** (1) Four-era evolution framework with Goal-Conditioned POMDP formulation; (2) five trade-offs identified (Scale vs Fidelity vs Diversity, Breadth vs Depth, Reasoning vs Reactivity, Modular vs Model-as-Whole, Code Engine vs World Model); (3) comprehensive VLM/VLA model comparison table for game agents.

---

## 4. Procedural Content Generation

### 4.1 VIPCGRL: Human-Aligned PCGRL via Text-Level-Sketch Shared Representation

- **Authors:** In-Chang Baek, Seoyoung Lee, Sung-Hyun Kim, Geumhwan Hwang, KyungJoong Kim
- **Venue:** arXiv preprint (2025-08-13)
- **arXiv:** https://arxiv.org/abs/2508.09860
- **Abstract:** Proposes VIPCGRL — a DRL framework incorporating three modalities (text, level, sketches) for human-aligned procedural level generation. Uses quadruple contrastive learning to train a shared embedding space across modalities and human-AI styles, with auxiliary reward from embedding similarity for policy alignment.
- **Key innovations:** (1) Multi-modal (text + level + sketch) control for PCGRL; (2) quadruple contrastive learning for cross-modal-human alignment; (3) improved human-likeness validated by quantitative metrics and human evaluation.

### 4.2 PCGRLLM: LLM-Driven Reward Design for PCGRL

- **Authors:** In-Chang Baek, Sunghyun Kim, Sam Earle, Zehua Jiang, Noh Jin-Ha, Julian Togelius, et al.
- **Venue:** IEEE Transactions on Games (2026)
- **arXiv:** https://arxiv.org/abs/2502.10906
- **Abstract:** Extends ChatPCG with a feedback mechanism and reasoning-based prompt engineering for LLM-driven reward function generation for PCGRL. Three-step approach: self-alignment, environment alignment + training, feedback-based refinement. Achieves 415% and 40% improvement over prior work using GPT-4o and Llama 3.2-90B respectively.
- **Key innovations:** (1) Feedback-based reward generation loop for PCGRL; (2) self-alignment + feedback two-stage refinement; (3) validated across two frontier LLMs.

### 4.3 Multiverse: Language-Conditioned Multi-Game Level Blending

- **Authors:** (Multiple authors)
- **Venue:** arXiv preprint (2026-03-25)
- **arXiv:** https://arxiv.org/abs/2603.26782
- **Abstract:** Language-conditioned multi-game level generator enabling cross-game level blending through textual specifications. Learns shared latent space with threshold-based multi-positive contrastive supervision linking semantically related levels across games. Enables controllable blending via latent interpolation and zero-shot generation from compositional prompts.
- **Key innovations:** (1) Cross-game level blending through shared latent representation; (2) zero-shot compositional text-to-level generation.

### 4.4 Multi-Agent RL for Video Game Level Design

- **Authors:** Sam Earle, Zehua Jiang, Eugene Vinitsky, Julian Togelius
- **Venue:** arXiv preprint (2025-10-06)
- **arXiv:** https://arxiv.org/abs/2510.04862
- **Abstract:** Frames game level design as multi-agent RL where multiple agents cooperatively edit noisy initial levels. Multi-agent generators are more efficient (fewer reward calculations per action), perform better, and generalize better to out-of-distribution map shapes due to more local, modular design policies.
- **Key innovations:** (1) Multi-agent PCGRL reducing reward computation cost; (2) emergent modularity and better generalization from distributed agents; (3) GPU-parallelized training.

### 4.5 Learning Local Constraints for RL Content Generators (WCRL)

- **Authors:** Debosmita Bhaumik, Julian Togelius, Georgios N. Yannakakis, Ahmed Khalifa
- **Venue:** arXiv preprint (2026)
- **arXiv:** https://arxiv.org/abs/2605.13570
- **Abstract:** Combines Wave Function Collapse (WFC) local constraint solving with PCGRL global property optimization. WFC constrains the PCGRL agent's action space, ensuring visual coherence while RL handles playability via reward functions. Produces visually satisfying and playable Lode Runner levels.
- **Key innovations:** (1) Hybrid WFC + PCGRL combining local aesthetics with global functionality; (2) constraint-RL action space reduction.

---

## 5. Game Benchmarks

### 5.1 GVGAI-LLM: Evaluating Large Language Model Agents with Infinite Games

- **Authors:** Yuchen Li, C. C. Lin, Muhammad Umair Nasir, Philip Bontrager, Jialin Liu, Julian Togelius
- **Venue:** arXiv preprint (2025-08-11)
- **arXiv:** https://arxiv.org/abs/2508.08501
- **Abstract:** Video game benchmark for evaluating LLM reasoning built on GVGAI. Features ASCII-represented arcade-style games with interpretable metrics (meaningful step ratio, step efficiency, win rate). Zero-shot evaluation of GPT-4o-mini, o3-mini, Gemini, DeepSeek across games reveals persistent failures in spatial reasoning and basic planning.
- **Key innovations:** (1) Infinitely extensible via VGDL game description language; (2) interpretable behavior metrics; (3) systematic LLM weakness identification.

### 5.2 OmniGameArena: Unified UE5 Benchmark for VLM Game Agents

- **Authors:** (Multiple authors)
- **Venue:** arXiv preprint (2026)
- **arXiv:** https://arxiv.org/abs/2606.09826
- **Abstract:** 12 custom Unreal Engine 5 games (Solo/PvP/Coop) with unified action interfaces. Introduces Improvement Dynamics Curve (IDC) — an agentic-reflection harness where a reflector LLM autonomously refines skill prompts across rounds. Evaluates 12 VLM agents including commercial (Claude Opus 4.7, GPT-5.5, Gemini 3.1 Pro), open-weight (Qwen3.5), and specialized policies (NitroGen, Open-P2P). Reports cold-start scores, multi-round improvement, and transfer to held-out variants.
- **Key innovations:** (1) Custom UE5 games avoiding pre-training contamination; (2) IDC protocol for measuring self-improvement dynamics; (3) cross-class evaluation (commercial VLMs vs specialized policies); (4) transfer evaluation on held-out variants.

### 5.3 GamingAgent / LMGame-Bench

- **Authors:** Lanxiang Hu, Mingjia Huo, Yuxuan Zhang, Haoyang Yu, Eric P Xing, Ion Stoica, Tajana Rosing, Haojian Jin, Hao Zhang
- **Venue:** ICLR 2026
- **arXiv:** https://arxiv.org/abs/2505.15146
- **GitHub:** https://github.com/lmgame-org/GamingAgent
- **Abstract:** LLM/VLM gaming agent framework and evaluation benchmark. Standardizes gaming environments via Gymnasium and Retro interfaces. Tests both vanilla single-model VLM setting and agentic GamingAgent workflow (gaming harness). Supports computer-use agents running on PC/laptops. Covers Sokoban, Tetris, 2048, Candy Crush, Pokémon Red, Super Mario Bros, Ace Attorney.
- **Key innovations:** (1) Standardized multi-game LLM evaluation framework; (2) gaming harness for agentic performance improvement; (3) ICLR 2026 publication establishing game-based LLM evaluation as a research area.

### 5.4 CUBE: A Standard for Unifying Agent Benchmarks

- **Authors:** Alexandre Lacoste, Nicolas Gontier, Oleh Shliazhko, et al.
- **Venue:** arXiv preprint (2026)
- **arXiv:** https://arxiv.org/abs/2603.15798
- **Abstract:** Proposes CUBE (Common Unified Benchmark Environments) — a universal protocol standard built on MCP and Gym for wrapping benchmarks once and accessing them everywhere. Separates task, benchmark, package, and registry concerns into distinct API layers. Supports async-Gym interaction patterns. Covers 250+ benchmarks across 17 platforms.
- **Key innovations:** (1) MCP + Gym fusion for universal benchmark access; (2) async step function supporting long-running operations; (3) tool configuration for benchmark-specific tools with research flexibility.

---

## 6. Industry Game AI

### 6.1 GAME-RL-INDUSTRY: Practical Deployment Notes

> No standalone industry-specific paper was identified this cycle. However, the following industry-adjacent work is relevant:

- **NitroGen** (NVIDIA, CVPR 2026): Open-source foundation model with universal Gymnasium API for commercial games — directly applicable to industry game AI pipelines.
- **Game-TARS** (ByteDance): 500B+ token scale pre-training on game data — demonstrates industrial-scale investment in game AI foundation models.
- **OmniGameArena**: Custom UE5 games — Unreal Engine 5 integration relevant for game studio deployment.

---

## 7. Related Techniques

### 7.1 World Models for Games

#### 7.1.1 Mind-Studio: Executable World Models with Lookahead Evaluation

- **Authors:** (Multiple authors)
- **Venue:** arXiv preprint (2026)
- **arXiv:** https://arxiv.org/abs/2606.16070
- **Abstract:** Synthesizes executable pygame-style world models from state-action-next-state trajectories using LLMs. Combines entropy-selected traces with compact game skill files. On Montezuma's Revenge, improves chosen-action NSP from 0.3% (PoE-World) to 48.7% while verifying 5/8 subgoals.
- **Key innovations:** (1) LLM-synthesized executable world models; (2) entropy-based informative transition selection; (3) 48.7% NSP improvement over prior art on Montezuma's Revenge.

#### 7.1.2 Distilling Game Code World Models into Lightweight LLMs

- **Authors:** Tyrone Serapio, Arjun Prakash, Haoyang Xu, Kevin Wang, Amy Greenwald
- **Venue:** arXiv preprint (2026-05-23)
- **arXiv:** https://arxiv.org/abs/2605.24375
- **Abstract:** Investigates distilling Game Code World Model (GameCWM) generation into small LLMs via SFT + RLVR. Curated dataset of 30 games, verification framework for structural and semantic game properties, post-training pipeline for Qwen2.5-3B-Instruct.
- **Key innovations:** (1) SFT+RLVR pipeline for GameCWM distillation; (2) execution-based verification as RL reward signal; (3) 3B model capable of generating valid game world models.

#### 7.1.3 ITC: Identifiable Token Correspondence for World Models

- **Authors:** (SNU MLLab)
- **Venue:** arXiv preprint (2026)
- **arXiv:** https://arxiv.org/abs/2605.16457
- **Abstract:** Transformer world model using optimal transport for token correspondence between frames. Each next-frame token is explained by copying from the previous frame or generating new. Achieves 72.5% return on Craftax-classic (vs previous 67.4%), SOTA on MinAtar (all 4 games), and SOTA on Atari 100K (IQM and optimality gap).
- **Key innovations:** (1) Optimal transport-based token correspondence solving object duplication/disappearance; (2) selective token reuse reducing hallucinations; (3) SOTA across Craftax, MinAtar, and Atari 100K.

#### 7.1.4 OPINE-World: Programmatic World Modeling with Ontology-Error-Prioritized Exploration

- **Authors:** David Courtis, Wenhao Li, Scott Sanner
- **Venue:** arXiv preprint (2026-07-01)
- **arXiv:** https://arxiv.org/abs/2607.01531
- **Abstract:** LLM agent learning object-centric programmatic world models online from interaction. Two cooperating agents run hypothesis-and-test loop. Bayesian ontology error steers exploration. Solves 20/25 ARC-AGI-3 games without per-game training (neural/program-synthesis baselines solve 0).
- **Key innovations:** (1) Online programmatic world model learning from pixel observations; (2) ontology error for exploration steering; (3) 20/25 games on ARC-AGI-3 without per-game training.

### 7.2 Hierarchical RL in Games

#### 7.2.1 AgentOWL: Joint Learning of Hierarchical Neural Options and Abstract World Model

- **Authors:** Wasu Top Piriyakulkij, Wolfgang Lehrach, Kevin Ellis, Kevin Murphy
- **Venue:** arXiv preprint (2026)
- **arXiv:** https://arxiv.org/abs/2602.02799
- **Abstract:** Jointly learns abstract world model (symbolic code + non-parametric distributions) and hierarchical neural options. RL in abstract world model yields exploration policy for real-world training. Demonstrates zero-shot generalization to novel starting states in Montezuma's Revenge, Pitfall, and Private Eye.
- **Key innovations:** (1) Sample-efficient joint option-world-model learning; (2) abstract plans enabling exploration of hard-exploration games; (3) zero-shot composition for novel states.

#### 7.2.2 CODE-SHARP: Open-ended Discovery of Skills as Hierarchical Reward Programs

- **Authors:** (Multiple authors)
- **Venue:** arXiv preprint (2026)
- **arXiv:** https://arxiv.org/abs/2602.10085
- **Abstract:** Leverages FMs to autonomously grow an archive of Skills as Hierarchical Reward Programs (SHARPs) — Python programs encoding success conditions with prerequisite chains. On Craftax-Classic and XLand, outperforms prior works by 6× and 2.6× in median performance. Only agents capable of crafting iron tools and mining diamonds. Scales to 90+ discovered SHARPs.
- **Key innovations:** (1) Fully autonomous open-ended skill discovery from environment source code; (2) hierarchical prerequisite chains reducing learning to marginal new behavior; (3) 6× performance improvement on Craftax-Classic.

### 7.3 Imitation Learning / Inverse RL in Games

- **DAGS** (§1.6) uses offline demonstrations for starting-state sampling.
- **CAST** (§2.1) performs logit-free on-policy distillation from game solvers.
- **CRISP** (AAAI 2026) combines PIP + IRL regularizer for hierarchical curriculum learning in robotic/game settings.

### 7.4 Curiosity-Driven / Open-Ended Learning

- **CODE-SHARP** (§7.2.2) demonstrates open-ended skill discovery — closely related to curiosity-driven exploration but structured through hierarchical reward programs rather than intrinsic motivation.
- **AgentOWL** (§7.2.1) achieves focused exploration through abstract planning rather than explicit curiosity bonuses.

### 7.5 Model-Based RL for Games

- **Mind-Studio** (§7.1.1), **ITC** (§7.1.3), **OPINE-World** (§7.1.4), **GameCWM distillation** (§7.1.2) — all represent different approaches to building world models for game environments.
- **RWML** (arXiv:2602.05842) — Reinforcement World Model Learning for LLM-based agents, aligning simulated and real next states in embedding space.

---

## Cross-Cutting Themes

### Trend 1: Sparse Reward Self-Play Scales Further
The Generals.io result (§1.1) extends pure PPO self-play with sparse win/loss reward to real-time strategy games — confirming that the "outer loop" (population/league) may not be essential at scale. EMAgnet (§1.2) and GARIP (§1.3) provide principled regularization improvements.

### Trend 2: Foundation Models Reach Game Scale
NitroGen (CVPR 2026) and Game-TARS demonstrate that internet-scale pre-training on game data produces generalist policies. NitroGen's 40K-hour dataset and universal Gymnasium API could become a standard resource.

### Trend 3: LLMs as Game Controllers — From Planning to Execution
The field is moving beyond simple prompting to sophisticated architectures: hierarchical LLM+RL (§2.2), automated prompt optimization (§2.4), bounded autonomy for live games (§2.5), and self-improving harnesses (§2.6). CAST (§2.1) provides the missing credit assignment for turn-level RL training.

### Trend 4: Programmatic World Models
Mind-Studio, OPINE-World, and GameCWM distillation all show LLMs can generate executable world models from interaction — a promising direction for model-based game AI that enables planning without environment access.

### Trend 5: Benchmarks Get Real-Time and Multi-Modal
OmniGameArena's UE5 games, NitroGen's universal simulator, and LMGame-Bench's multi-interface support are pushing game AI benchmarks beyond static observation-action loops to real-time, visually rich, multi-agent settings.
