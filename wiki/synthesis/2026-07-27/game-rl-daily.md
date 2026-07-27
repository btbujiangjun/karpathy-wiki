---
title: Game RL & Game AI Bot — Daily Paper Digest (July 27, 2026)
type: synthesis
created: 2026-07-27
updated: 2026-07-27
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, pcg, benchmarks, world-models, self-play, vlm, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (July 27, 2026)

## 1. Game RL — Reinforcement Learning in Games

### 1.1 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors**: Bo Liu, Leon Guertler, Simon C.H. Yu, Zichen Liu, Penghui Qi, Daniel Balcells, et al.
- **Affiliation**: Meta FAIR
- **Venue**: ICLR 2026 (Conference Paper)
- **Abstract**: Introduces SPIRAL, a self-play framework where LLMs learn by playing multi-turn zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation) against evolving versions of themselves. Proposes Role-Conditioned Advantage Estimation (RAE) to stabilize multi-agent training. Multi-game training achieves up to 10.5% improvement across 8 reasoning benchmarks on Qwen3-4B-Base (34.0% → 44.5%), outperforming SFT on 25K expert trajectories. Different games develop complementary cognitive skills: spatial reasoning, probabilistic thinking, and strategic optimization.
- **Key Innovation**: Fully online multi-turn multi-agent RL for LLMs with RAE preventing thinking collapse; self-play generates unlimited training data without human supervision.
- **Link**: https://arxiv.org/abs/2506.24119v3

### 1.2 STRATAGEM: Learning Transferable Reasoning via Trajectory-Modulated Game Self-Play
- **Authors**: Xiachong Feng, Deyi Yin, Xiaocheng Feng, Yi Jiang, Libo Qin, Yangfan Ye, et al.
- **Affiliation**: - (arXiv preprint)
- **Venue**: arXiv preprint (April 2026)
- **Abstract**: Addresses two fundamental barriers to reasoning transfer from games: domain specificity and contextual stasis. Introduces Reasoning Transferability Coefficient (φ) measuring abstraction level of reasoning patterns, and Reasoning Evolution Reward (ψ) incentivizing progressive reasoning across turns. Experiments on mathematical reasoning, general reasoning, and code generation show consistent improvements over SPIRAL, with pronounced gains on competition-level mathematics.
- **Key Innovation**: Trajectory-level advantage modulation via transferability and evolution signals; selective reinforcement of abstract, domain-agnostic reasoning patterns.
- **Link**: https://arxiv.org/pdf/2604.17696

### 1.3 Augmenting Game AI with Deep Reinforcement Learning
- **Authors**: Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslén
- **Affiliation**: - (Industry/academic collaboration)
- **Venue**: arXiv preprint (June 2026)
- **Abstract**: Proposes a framework for training RL models with requirements suited towards game AI and game development. Presents examples of games with RL-augmented game AI and describes practicalities of deploying player-facing ML agents in modern games. Identifies bottlenecks in usability, stability, controllability, and integration workflows.
- **Key Innovation**: Practical deployment framework for RL-based game AI in AAA production environments; identifies key bottlenecks for industry adoption.
- **Link**: https://arxiv.org/abs/2606.20210

### 1.4 Concept-Guided Spatial Regularization for World Models in Atari Pong
- **Authors**: Ye Lu, Zaishuo Xia, Weyl Lu, Yubei Chen
- **Affiliation**: - (arXiv preprint)
- **Venue**: arXiv preprint (July 2026)
- **Abstract**: Evaluates five visual world-model agents (DreamerV3, DIAMOND, TWISTER, Simulus, STORM) in Atari Pong with frozen world models.发现闭环rollouts包含明显失败（球消失、错误反弹）。提出Concept-Guided Spatial Regularization (CGSReg) — an auxiliary pixel reconstruction loss on segmented concept regions. CGSReg improves DreamerV3 mean return from -21.00 to -11.90, DIAMOND from -13.90 to -5.80, TWISTER from -21.00 to -1.90.
- **Key Innovation**: Isolating and directly evaluating frozen world models; concept-region reconstruction for task-critical objects.
- **Link**: https://arxiv.org/abs/2607.15142

### 1.5 Multiplayer Interactive World Models with Representation Autoencoders
- **Authors**: - (NVIDIA/academic)
- **Venue**: arXiv preprint (July 2026)
- **Abstract**: First multiplayer world model for highly dynamic environments. 5B-parameter latent diffusion model trained on 10K hours of Rocket League gameplay, generating 4-player matches in real-time (20 FPS on single Nvidia B200). Rollouts stable out to 5 minutes with no collapse observed.
- **Key Innovation**: Multi-agent conditioning via action streams; real-time multiplayer world model generation.
- **Link**: https://arxiv.org/abs/2607.05352v1

### 1.6 Γ-World: Generative Multi-Agent World Modeling Beyond Two Players
- **Authors**: Fangfu Liu, Kai He, Tianchang Shen, Tianshi Cao, Sanja Fidler, Yueqi Duan, et al.
- **Affiliation**: - (arXiv preprint)
- **Venue**: arXiv preprint (May 2026)
- **Abstract**: Introduces Simplex Rotary Agent Encoding (parameter-free 3D RoPE extension) and Sparse Hub Attention for multi-agent world models. Scales from 2 to 4 players without additional training. Generates action-responsive rollouts at 24 FPS with distilled causal student model.
- **Key Innovation**: Permutation-symmetric agent identity encoding; hub-mediated cross-agent communication at linear cost.
- **Link**: https://arxiv.org/pdf/2605.28816

### 1.7 WorldCompass: RL for Long-Horizon World Models
- **Authors**: Zehan Wang, Tengfei Wang, Haiyu Zhang, Xuhui Zuo, Junta Wu, Haoyuan Wang, et al.
- **Affiliation**: - (Open MIND)
- **Venue**: arXiv preprint (February 2026)
- **Abstract**: RL post-training framework for interactive video-based world models. Clip-level rollout strategy, complementary reward functions (interaction-following accuracy + visual quality), negative-aware fine-tuning. Improves composite action accuracy from ~20% to 55% on WorldPlay.
- **Key Innovation**: RL framework tailored for autoregressive interactive world models; clip-level rollout for fine-grained rewards.
- **Link**: https://arxiv.org/pdf/2602.09022

### 1.8 When Actions Disappear: Adversarial Action Removal in Self-Play RL
- **Authors**: Arahan Kujur (and others)
- **Venue**: arXiv preprint (May 2026)
- **Abstract**: Studies adversarial action masking in self-play RL across poker games (6 to 5,531 information states) and two non-poker domains. Learned masking causes substantially more damage than random masking. Attack persists across Q-learning, PPO, NFSP, DQN victims; transfers across agents; amplified by self-play.
- **Key Innovation**: Identifies action availability as a distinct robustness surface; introduces CAC_w and CAC_v metrics.
- **Link**: https://arxiv.deeppaper.ai/papers/2605.16312v1

---

## 2. Game AI Bot — LLM-Powered Game Agents

### 2.1 Think in Games: Learning to Reason in Games via RL with LLMs
- **Authors**: - (arXiv preprint)
- **Venue**: arXiv preprint (August 2025)
- **Abstract**: Proposes Think-In Games (TiG), reformulating RL decision-making as a language modeling task. LLMs generate language-guided policies refined via online RL (GRPO) based on environmental feedback. Validated in Honor of Kings (HoK), bridging declarative knowledge ("knowing about") and procedural knowledge ("knowing how"). Produces step-by-step explanations for decisions.
- **Key Innovation**: RL as language modeling task; interpretable policies with natural language explanations.
- **Link**: https://arxiv.org/html/2508.21365v1

### 2.2 Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with LLMs
- **Authors**: - (NTU)
- **Venue**: arXiv preprint (April 2026)
- **Abstract**: Extends Shannon's taxonomy of game-playing machines using LLMs. Nemobot enables users to create, customize, and deploy LLM-powered game agents across four game classes: dictionary-based, solvable, heuristic-based, and learning-based. Demonstrates self-programming via crowdsourced learning and human creativity.
- **Key Innovation**: Programmable framework bridging classical AI theory with modern LLM capabilities for game agents.
- **Link**: https://arxiv.org/abs/2604.21896v1

### 2.3 Sensi: Curriculum-Based Test-Time Learning for LLM Game Agents
- **Authors**: Mohsen Arjmandi
- **Venue**: arXiv preprint (March 2026)
- **Abstract**: LLM agent architecture for ARC-AGI-3 game-playing. Two-player architecture (Observer + Actor), curriculum-based learning via state machine, database-as-control-plane. Sensi v2 achieves 50-94× greater sample efficiency than comparable systems (32 interactions vs 1,600-3,000). Diagnoses failure mode as self-consistent hallucination cascade in perception layer.
- **Key Innovation**: Structured test-time learning with curriculum + programmable context; diagnosis of perceptual grounding as bottleneck.
- **Link**: https://arxiv.org/html/2603.17683

### 2.4 MEMO: Memory-Augmented Model Context Optimization for Robust Multi-Turn Multi-Agent LLM Games
- **Authors**: Yunfei Xie, Kevin Wang, Bobby Cheng, Jianzhu Yao, et al.
- **Venue**: arXiv preprint (March 2026)
- **Abstract**: Self-play framework optimizing inference-time context. Retention (persistent memory bank) + exploration (tournament-style prompt evolution). Raises mean win rate from 25.1% to 49.5% for GPT-4o-mini across 5 text-based games, using 19× fewer games than RL baselines. Largest gains in negotiation and imperfect-information games.
- **Key Innovation**: Weight-free self-play via context optimization; persistent memory distilling reusable strategic insights.
- **Link**: https://arxiv.org/pdf/2603.09022

### 2.5 Hierarchical Control in Multi-Agent Games: LLM-based Planning and RL Execution
- **Authors**: - (OpenReview)
- **Venue**: RLVG Workshop 2026 (AAMAS)
- **Abstract**: Two-layer hierarchical architecture where LLM (Gemma 3 27B) acts as centralized strategic controller selecting among 4 pretrained RL skill policies for 2v2 King of the Hill. Win rate statistically equivalent to hand-crafted behavior trees (46.4% vs 51.5%). User study: 60% perceive LLM+RL as most human-like (p=0.027).
- **Key Innovation**: LLM orchestration of pretrained RL skills without manual rule engineering; behavioral adaptability as key human-likeness driver.
- **Link**: https://arxiv.org/html/2606.20014v3

### 2.6 HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for LLM Agents
- **Authors**: - (arXiv preprint)
- **Venue**: arXiv preprint (February 2026)
- **Abstract**: Hierarchical Plan-Execute RL framework explicitly separating high-level planning from low-level execution. Hierarchical Advantage Estimation (HAE) provides unbiased gradient estimator with provable variance reduction. Achieves 97.4% success on ALFWorld and 83.3% on WebShop with Qwen2.5-7B-Instruct (+6.6% and +8.3% over best prior method).
- **Key Innovation**: Explicit hierarchical decomposition with HAE; critic-free hierarchical policy optimization.
- **Link**: https://arxiv.org/html/2602.16165v1

### 2.7 The Latent Bridge: A Continuous Slow-Fast Channel for Real-Time Game Agents
- **Authors**: Bojie Li, Noah Shi
- **Venue**: arXiv preprint (June 2026)
- **Abstract**: Couples a frozen reasoning VLM (Qwen3-VL-8B, ~1.5s/response) with a frozen reactive VLM (MiniCPM-o 4.5, milliseconds) via learned continuous Latent Bridge projecting slow model's residuals into fast model's embedding space. Matches or beats Text Bridge in every domain; significantly improves MsPacman (+57%) and RoadRunner (+28%).
- **Key Innovation**: Continuous latent channel for fast/slow model coupling without text round-trip; safe drop-in improvement for real-time agents.
- **Link**: https://arxiv.org/pdf/2606.24470

### 2.8 Pareto-guided Pipeline for Distilling Featherweight AI Agents in Mobile MOBA Games
- **Authors**: Xionghui Yang, Bozhou Chen, Yunlong Lu, Yongyi Wang, Lingfeng Li, Lanxiao Huang, et al.
- **Venue**: arXiv preprint (February 2026)
- **Abstract**: Addresses deploying powerful Honor of Kings agents on mobile devices. Pareto optimality guided distillation pipeline with high-efficiency student architecture search. Achieves 12.4× faster inference and 15.6× energy efficiency improvement while maintaining competitive win rate (40.32% vs teacher's 49.98%).
- **Key Innovation**: Multi-objective optimization for mobile game AI deployment; end-to-end pipeline from complex teacher to featherweight student.
- **Link**: https://arxiv.org/pdf/2602.07521

---

## 3. Game Foundation Models

### 3.1 NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, et al.
- **Affiliation**: NVIDIA / MineDojo
- **Venue**: CVPR 2026 (Oral)
- **Abstract**: Vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games. Internet-scale video-action dataset from automatic action extraction. Flow-matching architecture adapted from GR00T N1. Fine-tuning achieves up to 52% relative improvement over scratch. Releases dataset, evaluation suite, and model weights.
- **Key Innovation**: Internet-scale behavior cloning for multi-game agents; automatic action extraction from public gameplay videos.
- **Link**: https://arxiv.org/pdf/2601.02427

### 3.2 Scaling Behavior Cloning Improves Causal Reasoning: An Open Model for Real-Time Video Game Playing
- **Authors**: Yuguang Yue, Irakli Salia, Samuel Hunt, Chris Green, Wenzhe Shi, Jonathan J. Hunt
- **Affiliation**: - (Open MIND)
- **Venue**: arXiv preprint (January 2026)
- **Abstract**: Open recipe for real-time video game playing foundation model. 8,300+ hours of human gameplay, models up to 1.2B parameters. Lightweight decoder-only transformer for 20Hz inference on consumer GPU. Scaling laws show larger models achieve lower test loss and higher causality scores. Data augmentation significantly reduces training-inference gap.
- **Key Innovation**: Open-source scaling laws for behavior cloning in games; real-time inference on consumer hardware.
- **Link**: https://arxiv.org/pdf/2601.04575

### 3.3 Towards Generalist Game Players: An Investigation of Foundation Models in the Game Multiverse
- **Authors**: Kuan Zhang, Dongchen Liu, Qiyue Zhao, Tianyu Xin, Yue Su, Haisheng Wang, et al.
- **Affiliation**: Tsinghua University
- **Venue**: arXiv preprint (May 2026)
- **Abstract**: Comprehensive survey tracing lifecycle of generalist game players across four eras (symbolic → RL → foundation models → creator). Four pillars: Dataset, Model, Harness, Benchmark. Five-level roadmap from single-game mastery to ultimate creator stage. 228 references.
- **Key Innovation**: First systematic investigation of LFMs as generalist game players through end-to-end lifecycle perspective.
- **Link**: https://arxiv.org/html/2605.09965

### 3.4 GameVerse: Can Vision-Language Models Learn from Video-based Reflection?
- **Authors**: - (arXiv preprint)
- **Venue**: arXiv preprint (March 2026)
- **Abstract**: Comprehensive VLM benchmark with 15 games, dual action space (semantic + GUI control), and reflect-and-retry paradigm. VLMs benefit from video-based reflection; best by combining failure trajectories and expert tutorials (training-free analogue to RL + SFT). Gemini-2.5-Pro achieves highest average ranking.
- **Key Innovation**: Reflect-and-retry evaluation paradigm; failure-as-RL + tutorial-as-SFT synergy.
- **Link**: https://arxiv.org/abs/2603.06656v2

### 3.5 OpenGame: Open Agentic Coding for Games
- **Authors**: Yilei Jiang, Jinyuan Hu, Qianyin Xiao, Yaozhi Zheng, Ruize Ma, Kaituo Feng, et al.
- **Venue**: arXiv preprint (April 2026)
- **Abstract**: First open-source agentic framework for end-to-end web game creation. GameCoder-27B trained via continual pre-training + SFT + execution-grounded RL. Template Skill (evolving project skeletons) + Debug Skill (cumulative error repair). OpenGame-Bench evaluates build health, visual usability, and intent alignment across 150 game prompts.
- **Key Innovation**: Domain-specialized code model for game engines; persistent structural priors + reusable debugging knowledge.
- **Link**: https://arxiv.org/abs/2604.18394

---

## 4. Procedural Content Generation

### 4.1 Multi-task Procedural Content Generation with Reinforcement Learning
- **Authors**: Nekahdari, Kouzehkonani, Saeedi, et al.
- **Affiliation**: - (Scientific Reports)
- **Venue**: Scientific Reports (April 2026)
- **Abstract**: DeBERTa-based LPCGRL with multi-objective training (regression + contrastive alignment + hybrid learning). Dataset of 14,000+ command-level pairs in Super Mario. Outperforms BERT-based methods in command following, semantic stability, and structural diversity. Generalizes to paraphrase and extra-domain instructions.
- **Key Innovation**: Disentangled instruction encoder with multi-objective training for human-aligned PCGRL.
- **Link**: https://www.nature.com/articles/s41598-026-48234-7

### 4.2 Learning Local Constraints for Reinforcement-Learned Content Generators (WCRL)
- **Authors**: - (arXiv preprint)
- **Venue**: arXiv preprint (May 2026)
- **Abstract**: Combines Wave Function Collapse (WFC) with PCGRL by constraining the action space of a PCGRL generator with WFC-learned local rules. Generates visually satisfying and playable Lode Runner levels. Starting from partially collapsed state produces more robust policies.
- **Key Innovation**: Hybrid WFC+PCGRL approach combining local visual patterns with global playability guarantees.
- **Link**: https://arxiv.org/html/2605.13570v1

### 4.3 Procedural Game Level Design with Deep Reinforcement Learning
- **Authors**: Miraç Buğra Özkan
- **Venue**: arXiv preprint (October 2025)
- **Abstract**: Two-agent system in Unity: hummingbird (PPO solver) + island (PPO level generator). Co-adaptive procedural content generation with real-time feedback loop. Hummingbird achieves 90.2% success rate; island agent converges to low-penalty, high-engagement configurations.
- **Key Innovation**: Closed feedback loop between environment generation and task-solving agents; emergent behavior from co-adaptation.
- **Link**: https://arxiv.org/abs/2510.15120

---

## 5. Game Benchmarks

### 5.1 OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics
- **Authors**: Mingxian Lin, Shengju Qian, Yuqi Liu, Yi-Hua Huang, Yiyu Wang, Wei Huang, et al.
- **Venue**: arXiv preprint (June 2026)
- **Abstract**: 12 newly built Unreal Engine 5 games (Solo 7, PvP 3, Coop 2) with unified action interfaces. Improvement Dynamics Curve (IDC): agentic-reflection harness with autonomous tool-use reflector refining skill prompts across rounds. Evaluates 12 VLM agents. Leadership rotates across games; origin-task gain doesn't predict held-out transfer.
- **Key Innovation**: IDC exposes multi-round self-improvement trajectories + held-out transfer as additional observables beyond cold-start scores.
- **Link**: https://arxiv.org/abs/2606.09826

### 5.2 CausalGame: Benchmarking Causal Thinking of LLM Agents in Games
- **Authors**: - (arXiv preprint)
- **Venue**: arXiv preprint (July 2026)
- **Abstract**: 14 game scenarios incorporating selection bias, measurement error, and hidden confounders. Evaluates 30 frontier LLMs. Best model reaches only 68.0% survival vs 78-85% analytical optima; merely 5-7% of sessions receive credits on causal-reasoning rubrics. None demonstrates reliable causal thinking.
- **Key Innovation**: Interactive game-based benchmark for causal reasoning with observational pitfalls; scalable and controlled testbed.
- **Link**: https://arxiv.org/html/2607.04293v1

### 5.3 GVGAI-LLM: Evaluating Large Language Model Agents with Infinite Games
- **Authors**: Yuchen Li, C.C. Lin, Muhammad Umair Nasir, Philip Bontrager, Jialin Liu, Julian Togelius
- **Venue**: arXiv preprint (August 2025)
- **Abstract**: Benchmark built on General Video Game AI framework with diverse arcade-style games. Game description language enables rapid creation of new games/levels. ASCII representation for efficient LLM processing. Reveals persistent LLM limitations in spatial reasoning and basic planning. Deepseek-r1 achieves 50.0% in Sokoban and 54.5% in Escape.
- **Key Innovation**: Infinite game generation via VGDL; interpretable metrics (meaningful step ratio, step efficiency).
- **Link**: https://arxiv.org/pdf/2508.08501

### 5.4 lmgame-Bench: How Good are LLMs at Playing Games?
- **Authors**: Lanxiang Hu, Ming Huo, Yuxuan Zhang, Hongwen Yu, Eric P. Xing, Ion Stoica, et al.
- **Venue**: arXiv preprint (May 2025)
- **Abstract**: Suite of platformer, puzzle, and narrative games with perception/memory scaffolds. Addresses brittle vision, prompt sensitivity, and data contamination. RL training on Sokoban and Tetris transfers to unseen games and external planning tasks (Blocksworld, WebShop). o3 and o1 achieve top performance.
- **Key Innovation**: Gaming environments as training environments improving core LLM capabilities; cross-game and cross-domain transfer.
- **Link**: https://arxiv.org/abs/2505.15146

### 5.5 VideoGameBench: Can Vision-Language Models Complete Popular Video Games?
- **Authors**: Alex L. Zhang, Thomas L. Griffiths, Karthik R. Narasimhan, Ofir Press
- **Venue**: arXiv preprint (May 2025)
- **Abstract**: Benchmark for evaluating VLMs on popular video games. Tests whether VLMs can complete commercial games end-to-end.
- **Key Innovation**: Real commercial game evaluation for VLMs.
- **Link**: https://arxiv.org/abs/2505.18134

---

## 6. Industry Game AI

### 6.1 OPINE-World: Programmatic World Modeling with Ontology-error-Prioritized Interactive Exploration
- **Authors**: David Courtis, Wenhao Li, Scott Sanner
- **Venue**: arXiv preprint (July 2026)
- **Abstract**: LLM agent learning object-centric programmatic world models online from interaction. Two cooperating LLM agents (action agent + synthesizer) with counterexample-guided synthesis. Solves 20 of 25 ARC-AGI-3 games without per-game training, reaching action-efficiency score of 78.4 vs human baseline.
- **Key Innovation**: Programmatic world model synthesis from interaction; ontology error steers exploration toward unexplained objects.
- **Link**: https://arxiv.org/html/2607.01531

### 6.2 WorldLLM: Improving LLMs' World Modeling Using Curiosity-Driven Theory-Making
- **Authors**: - (arXiv preprint)
- **Venue**: arXiv preprint (June 2025)
- **Abstract**: Combines Bayesian inference and curiosity-driven RL for autonomous world model improvement. LLM generates natural language hypotheses given as prompts. Curiosity-driven RL collects transitions with low log-likelihood. Alternating hypothesis refinement and evidence collection drives continual improvement.
- **Key Innovation**: Natural language theories grounding LLM's broad knowledge into precise predictive power; curiosity-driven evidence collection.
- **Link**: https://arxiv.org/abs/2506.06725v1

### 6.3 Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory
- **Authors**: Zile Wang, Zexiang Liu, Jaixing Li, Kaichen Huang, Baixin Xu, Fei Kang, et al.
- **Venue**: arXiv preprint (April 2026)
- **Abstract**: Memory-augmented interactive world model for 720p real-time long-form video generation. 5B model achieves up to 40 FPS at 720p. Camera-aware memory retrieval + error-aware base model for self-correction. Scales to 2×14B for improved quality.
- **Key Innovation**: Industrial-scale deployable world model; training-inference aligned few-step distillation for real-time.
- **Link**: https://arxiv.org/html/2604.08995

### 6.4 Reinforcement World Model Learning for LLM-based Agents
- **Authors**: Xiao Yu, Baolin Peng, Ruize Xu, Yelong Shen, Pengcheng He, Suman Nath, et al.
- **Venue**: arXiv preprint (February 2026)
- **Abstract**: Self-supervised method learning action-conditioned world models for LLM agents using sim-to-real gap rewards in embedding space. Improves base model by 19.6 points on ALFWorld without expert data. Combined with task-success rewards, outperforms direct RL by 6.9 points.
- **Key Innovation**: RL-based world model learning avoiding next-token prediction pitfalls; sim-to-real alignment in embedding space.
- **Link**: https://arxiv.org/pdf/2602.05842

---

## 7. Related Techniques

### 7.1 HiMAC: Hierarchical Macro-Micro Learning for Long-Horizon LLM Agents
- **Authors**: - (arXiv preprint)
- **Venue**: arXiv preprint (March 2026)
- **Abstract**: Decomposes long-horizon decision-making into macro-level blueprint generation and micro-level goal-conditioned execution. Critic-free hierarchical group-based optimization + iterative co-evolution training. Achieves SOTA on ALFWorld, WebShop, and Sokoban. 16% gain over strongest RL baseline on WebShop (83.4% vs 67.4%).
- **Key Innovation**: Structured hierarchy (macro-micro separation) as decisive factor for long-horizon agentic intelligence; critic-free hierarchical optimization.
- **Link**: https://arxiv.org/html/2603.00977v1

### 7.2 Foundation Model Self-Play: Open-Ended Strategy Innovation
- **Authors**: Aaron Dharna, Cong Lu, Jeff Clune
- **Venue**: Reinforcement Learning Journal 2025
- **Abstract**: Foundation-Model Self-Play (FMSP) family: vFMSP (exploitation), NSSP (novelty search), QDSP (quality-diversity). FM generates code-based policies in multi-agent self-play. In Car Tag, surpasses strong human-designed strategies. In Gandalf, automatically red-teams LLMs through 6 defense levels.
- **Key Innovation**: First MAP-Elites algorithm where practitioner need not define dimensions of interest; FM-powered open-ended strategy discovery.
- **Link**: https://arxiv.org/pdf/2507.06466

### 7.3 Active Zero: Self-Evolving VLMs through Active Environment Exploration
- **Authors**: Jinghan He, Junfeng Fang, Feng Xiong, Zijun Yao, Fei Shen, Haiyun Guo, et al.
- **Venue**: arXiv preprint (February 2026)
- **Abstract**: Three co-evolving agents (Searcher, Questioner, Solver) for active exploration of visual environments. Searcher retrieves images at capability frontier; Questioner synthesizes calibrated tasks. Achieves 53.97 average accuracy on reasoning tasks (+5.7%) and 59.77 on general understanding (+3.9%).
- **Key Innovation**: Shift from passive interaction with static images to active exploration; self-scaffolding auto-curriculum.
- **Link**: https://arxiv.org/html/2602.11241

### 7.4 Seirênes: Adversarial Self-Play with Evolving Distractions for LLM Reasoning
- **Authors**: - (arXiv preprint)
- **Venue**: arXiv preprint (May 2026)
- **Abstract**: Shared-parameter self-play RL where single model co-evolves as Adversary (generating misleading contexts) and Reasoner (recovering core logic). Achieves +10.2, +9.1, +7.2 points across 7 math benchmarks on 4B-30B models. 4B model's distractors reduce GPT and Gemini accuracy by 4-5 points.
- **Key Innovation**: Contextual interference as internal training signal; adversarial co-evolution for robust reasoning.
- **Link**: https://arxiv.org/html/2605.11636v1

### 7.5 Curiosity-Driven Exploration in RL: Adaptive Self-Supervised Learning for Action Games
- **Authors**: - (MDPI Computers)
- **Venue**: Computers 2025, 14(10), 434
- **Abstract**: Integration of Intrinsic Curiosity Module (ICM) with A3C algorithm using PPO for policy updates. Applied to action games (Mortal Kombat, Jackie Chan, Street Fighter). Agents learn exploration behaviors without relying solely on external rewards; improved efficiency and learning speed vs baselines.
- **Key Innovation**: ICM+A3C hybrid for curiosity-driven exploration in combat/action games.
- **Link**: https://www.mdpi.com/2073-431X/14/10/434

### 7.6 StarBench: Turn-Based RPG Benchmark for Agentic Multimodal Decision-Making
- **Authors**: - (AAMAS 2026)
- **Venue**: AAMAS 2026
- **Abstract**: Benchmark derived from Honkai: Star Rail evaluating VLMs across 8 combat tasks in direct control (screenshot → keyboard-mouse) and tool-assisted control regimes. Ask-or-act diagnostic measures information seeking. VLMs fail almost entirely in direct control; tool assistance markedly improves success.
- **Key Innovation**: Separating perception-to-control grounding from higher-level decision making; ask-or-act diagnostic.
- **Link**: https://arxiv.org/html/2510.18483v1

---

## Key Themes & Trends

1. **Self-play generates transferable reasoning** (SPIRAL → STRATAGEM → MARS): Zero-sum games develop distinct cognitive patterns (spatial, probabilistic, strategic) that transfer to academic benchmarks. Multi-game training synergistically combines complementary skills.

2. **Foundation models reach internet scale** (NitroGen CVPR 2026, Pixels2Play 1.2B): 40K+ hours of gameplay across 1000+ games enables generalist gaming agents with 52% relative improvement on unseen games. Open-source scaling laws for behavior cloning in games.

3. **World models achieve real-time multiplayer** (5B Rocket League 4-player 20fps, Γ-World 24fps, Matrix-Game 3.0 40fps 720p): Interactive world models transitioning from single-agent to multi-agent settings with hour-long stable rollouts.

4. **Hierarchical RL+LLM architectures dominate complex games** (HiPER 97.4% ALFWorld, HiMAC macro-micro, LLM+RL hierarchical 2v2): Explicit decomposition of planning from execution enables credit assignment in sparse-reward long-horizon settings.

5. **Benchmarks mature rapidly** (OmniGameArena UE5 12 games, CausalGame 14 scenarios 30 LLMs, GVGAI-LLM infinite games, lmgame-Bench 13 models): Evaluation shifting from fire-and-forget to improvement dynamics, causal reasoning, and cross-game transfer.

6. **Industry deployment advances** (Pareto mobile distillation 12.4× speedup, Featherweight AI agents, real-time inference at 40 FPS): Bridging the gap from research prototypes to production-ready game AI with strict latency/energy constraints.

7. **Curiosity and exploration remain critical** (WorldLLM theory-making, Active Zero environment exploration, ICM+A3C action games): Intrinsic motivation continues enabling discovery in sparse-reward and open-ended game environments.
