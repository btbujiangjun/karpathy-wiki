---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-09-14)"
type: synthesis
created: 2026-09-14
updated: 2026-09-14
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, pcg, benchmarks, world-models, self-play, multi-agent-rl, offline-rl, robust-rl, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-09-14)

> **Methodology note**: arXiv **Mon 14 Sep 2026** mailing announced today — the first fresh window since Fri 11 Sep (Wed 10 – Thu 11 Sep submission wave, IDs ~2609.120xx–2609.13144). This run parsed the **recent listings of cs.AI / cs.CL / cs.CV / cs.GT / cs.HC / cs.LG / cs.MA / cs.NE / cs.RO** (Mon 14 block only, incl. page-2 skips for >50-entry categories). Every featured ID was **grep-verified 0 hits in `wiki/`**; papers already covered by today's sibling digests (arxiv-daily / arxiv-ai-search / arxiv-paper-check / conference-digest / tech-report-digest) are **excluded `by construction`** and cross-referenced below. **21 new papers featured; every one is fresh to the wiki.**
>
> **Continuity / already-covered by 09-14 siblings (not re-featured):** HORIZON zero-shot opponent adaptation (2609.12422) and Fragility of Worst-Case Nash in congestion games (2609.12220) → [arxiv-ai-search 09-14](../../2026-09-14/arxiv-ai-search.md); Werewolf belief-shift (2609.12446), EvoRS reward self-evolution (2609.12459), LLM pricing collusion (2609.13037), Pure Price of Anarchy (2609.12077) → [arxiv-daily 09-14](../../2026-09-14/arxiv-daily.md).

---

## 1. Game RL & Multi-Agent Reinforcement Learning

### 1.1 Curriculum-Based Adversarial Heterogeneous-Agent RL for Autonomous Quadrotor Capture in Maritime Settings
- **Authors**: Allan Minh-Tam Nguyen, Sree Showrya Kotala, Stefan Banioi-Crijman, Kurt Driessens, Rico Möckel
- **Affiliation**: Maastricht University (inferred)
- **Venue**: submitted to BNAIC 2026; arXiv preprint (2609.12758, cs.LG)
- **Key Innovations**: Studies **simulated mid-air capture of quadrotor UAVs by a ship-mounted robotic arm** — a maritime recovery task where wind turbulence and deck motion make conventional landing unreliable. Trains robust cooperative policies with **Heterogeneous-Agent PPO (HAPPO)** under two regimes: (a) curriculum + **adversarial wind agent (HARL-AC)** that actively fights the recovery policy, vs (b) curriculum-based domain randomization, all in NVIDIA Isaac Lab.
- **Results**: In-distribution (sea states 0/4/5) both reach up to 97.5% success; out-of-distribution (sea states 7/8/10) HARL-AC generalizes better — up to +16% higher median success at sea state 10 and substantially lower crash rates (down ~14%) vs domain randomization; the adversarially trained policy is more cautious (<3% extra timeouts) but safer in unseen severe conditions.
- **Significance**: Adversarial self-play-style curriculum as a generalization lever in heterogeneous MARL — the same recipe used for bot robustness transfers to maritime robotics.
- **Link**: https://arxiv.org/abs/2609.12758

### 1.2 CanvasAnneal: Curriculum Reinforcement Learning for Diffusion Language Models
- **Authors**: Blake Olson, Yuhang Song, Emmett McQuinn, Yuan Shangguan
- **Affiliation**: Apple (inferred)
- **Venue**: arXiv preprint (2609.13060, cs.LG)
- **Key Innovations**: Applies RL to **Diffusion Language Models (DLMs)** and attacks the exploration bottleneck with a curriculum: during the initial RL phase, teacher-generated reasoning traces are injected into the initial diffusion canvas to warm-start exploration; guidance is gradually removed ("annealed") until the model generates reasoning trajectories independently. Built on diffu-GRPO.
- **Results**: Outperforms standard diffu-GRPO on MATH500, Countdown, and Tau2, substantially accelerating reward improvement on harder tasks (gains task-dependent).
- **Significance**: Curriculum-driven RL for generative game-adjacent models (procedural text/world generation as diffusion processes); directly tradeable to LLM-driven game agents.
- **Link**: https://arxiv.org/abs/2609.13060

### 1.3 Groupoid-Based Internal State Representations for Reinforcement Learning with Local Symmetries
- **Authors**: Ben Opperman, Eduardo Alonso, Esther Mondragón
- **Affiliation**: City, University of London (inferred)
- **Venue**: The Eighteenth Workshop on Adaptive and Learning Agents (ALA 2026) @ **AAMAS 2026**; arXiv preprint (2609.13035, cs.LG)
- **Key Innovations**: Most symmetry-aware RL assumes a globally structured MDP with uniformly applicable actions. This work uses **groupoids** to capture *local, state-dependent* symmetries and support dynamic discovery of equivalence structures during interaction — maintaining orbit representatives plus **transporters** that map raw states to canonical forms, so learning happens in a symmetry-reduced space while local distinctions survive.
- **Results**: Improves sample efficiency and convergence in dense, large-scale environments exhibiting strong partial symmetries, with substantial gains over standard Q-learning.
- **Significance**: A principled route to exploiting modular/partial symmetries — directly relevant to board-game and tile-based game state spaces where symmetries are local rather than global.
- **Link**: https://arxiv.org/abs/2609.13035

### 1.4 Decentralized Evolution of Hexapod Gaits with Independent Leg Controllers
- **Authors**: Gary B. Parker et al.
- **Affiliation**: Connecticut College (inferred)
- **Venue**: arXiv preprint (2609.12400, cs.AI / cs.RO)
- **Key Innovations**: Evolves **each hexapod leg's gait independently** via a decentralized evolutionary algorithm (no centralized coordination), in Webots with the Mantis hexapod — allowing emergent behaviors to drive coordinated locomotion. Benchmarked against **cooperative coevolution**.
- **Results**: Shows improved efficacy in generating stable, adaptive gaits plus interesting emergent coordination, reducing the complexity of gait optimization.
- **Significance**: Decentralized/population-based evolution as an alternative to centralized MARL for locomotion-style game/physics agents.
- **Link**: https://arxiv.org/abs/2609.12400

---

## 2. Game AI Bots & LLM Agents in Games

### 2.1 Information Specialization and Constrained Synthesis in Multi-Agent LLM Forecasting: A Prospective Live-Study of the 2026 FIFA World Cup
- **Authors**: Julian Varghese, Lucas Bickmann, Sarah Sandmann
- **Affiliation**: University of Münster lineage (inferred)
- **Venue**: arXiv preprint (2609.12495, cs.AI / cs.CL)
- **Key Innovations**: Live, prospective evaluation over the **final 56 matches of the 2026 FIFA World Cup** with a **four-agent LLM pipeline**: a quantitative specialist (structured performance stats), a news specialist (injuries, tactics, press-conference info), a critic, and a meta-agent that combines forecasts. Betting market as external benchmark.
- **Results**: The news specialist achieved the highest mean probability-weighted Top-3 utility and matched the betting market on Top-3 exact-score hits — evidence that rapidly-changing unstructured info adds forecasting signal beyond structured statistics. But the two specialists agreed on ≥2 of 3 scorelines in 50/56 matches, and the meta-agent never produced a scoreline outside the specialists' forecast set: critic/meta stages added no complementary information.
- **Significance**: A cautionary result for **multi-agent "superbot" pipelines in game prediction** — specialization without forecast diversification, and synthesis without novel synthesis, cap the ceiling.
- **Link**: https://arxiv.org/abs/2609.12495

### 2.2 The House with a Million Windows: Interactive Fiction for Narrative Restorying
- **Authors**: Cody Kommers, Sarah G. Immel, Drew Hemment, Mina Lee
- **Affiliation**: (inferred — independent researcher / MIT / University of Edinburgh / Stanford lineage)
- **Venue**: arXiv preprint (2609.12537, cs.CL / cs.HC)
- **Key Innovations**: An **LLM-based interactive fiction system** that helps users explore multiple meanings of a personal story through a text-based narrative: users tell a story, then encounter LLM-generated "windows" that reframe it in different literary styles (drawn from the *restorying intervention* psychology paradigm).
- **Results**: Empirically increases users' sense of narrative identity; an expert review examines how the effect is achieved. Positions LLMs as meaning-expanding devices rather than story-flattening generators.
- **Significance**: A design pattern for **LLM-driven narrative games and interactive fiction NPCs** — counter-weights the homogenization critique of generative writing in games.
- **Link**: https://arxiv.org/abs/2609.12537

---

## 3. Game Foundation Models & World Models

### 3.1 Pelican-Sim 1.0: A General World Model Simulator for Embodied Intelligence
- **Authors**: Shilong Zou, Shilin Zhang, Yingji Zhang, Yuhang Huang, Yi Zhang, Zeyuan Ding, Han Dong, Junwei Liao, Yong Dai, Jian Tang, Xiaozhu Ju
- **Affiliation**: Jian Tang (Mila / HEC Montréal lineage) + industry co-authors; affiliation not stated in abstract (inferred)
- **Venue**: arXiv technical report (2609.12036, cs.RO / cs.AI)
- **Key Innovations**: A **general world-model simulator** predicting future observations from visual context + robot actions, with four design features: (1) **unified 28-dim action space** covering most mainstream embodiments (one model across heterogeneous devices); (2) **action-visual injection** — URDF- and camera-rendered action videos bridge actions and pixels (PSNR +0.904 over fusion baselines); (3) **sparse MoE** layers to absorb the action modality and reduce inter-modality conflict (FVD −6.530 vs dense); (4) **efficient rollout**: causal adaptation + few-step distillation → 4-step autoregressive simulator at **5.67× speedup** over the 35-step model.
- **Results**: Trained on ~1M real+sim trajectories; PSNR +4.636 (AgiBotWorld Beta), +2.080 (RoboMIND), +10.343 (RoboTwin) over strongest baselines. Downstream on RoboTwin: +500 generated trajectories on 50 demos/task raises policy success 70%→93%; policy evaluation hits Pearson 0.994 across 5 checkpoints; +47.7% action-selection / +20.3% policy-improvement gains.
- **Significance**: One of the strongest "world model as general simulator" results this window — the exact substrate game-foundation-model teams need for simulatable game worlds with cheap, controllable rollouts.
- **Link**: https://arxiv.org/abs/2609.12036

### 3.2 IMPLY: Physically Anchored Consistency for World-Model Rollouts
- **Authors**: Aman Mehta, Riya Baviskar
- **Affiliation**: not specified (inferred)
- **Venue**: arXiv preprint (2609.12441, cs.RO / cs.AI / cs.CV / cs.LG)
- **Key Innovations**: World-model consistency checks ask *"do the model's futures agree"* — but none knows physics. **IMPLY** reads the physics each rollout *implies* by **inverting a simulator**, then scores rollouts by how well **one object explains all of them**, anchored to **two calibration pushes** the model has actually observed. Shows self-consistency gives a *perfect score* to a model that ignores the object and always predicts a typical push; anchoring exposes it (AUROC 0.70 vs 1.00).
- **Results**: On real V-JEPA-2-AC adapted rollouts, object tracking correlates 0.91 with truth given its own calibration pushes but 0.05 given another object's — self-consistency cannot tell these apart (52% preference ≈ chance), anchored disagreement prefers the right evidence 73% of the time and correlates 0.92–0.99 with rollout error; selecting among candidate rollout sets comes within 0.003 of a truth-seeing oracle.
- **Significance**: The sharpest current argument that **world-model evaluation must be anchored to evidence, not closure** — critical for trusting game/embodied world models in planning.
- **Link**: https://arxiv.org/abs/2609.12441

### 3.3 DWMP: Leveraging Dual World Models for Humanoid Obstacle Traversal
- **Authors**: Rongjun Jin, Jianming Ma, Yue Gao
- **Affiliation**: (inferred — Chinese university lineage)
- **Venue**: arXiv preprint (2609.12347, cs.RO)
- **Key Innovations**: Splits the world-model job by modality: a **Koopman-based dynamics world model** lifts low-dim proprioception into a latent space where temporal evolution is *approximately linear* (easy features for the actor), while an **RSSM-based visual world model** compresses egocentric depth into compact stochastic states preserving obstacle geometry. A student policy acts on the fused latent representation.
- **Results**: Improves obstacle-traversal over baselines in simulation and deploys on a **Unitree G1 humanoid** under randomized obstacle layouts.
- **Significance**: Modality-specialized dual WMs — a template for game agents that mix kinematic state + egocentric visuals.
- **Link**: https://arxiv.org/abs/2609.12347

### 3.4 RodForesight: A World Model Enhanced Diffusion Policy for Slender and Material-Agnostic Rod Insertion
- **Authors**: Chuanbo Yu, Mingyu Yue, Yan Lyu, Chuhan Song, Peng Wang
- **Affiliation**: not specified (inferred)
- **Venue**: arXiv preprint (2609.12103, cs.RO)
- **Key Innovations**: For bendable high-aspect-ratio rod insertion (peg-in-hole assumptions break), factorizes into coarse approaching (visual servoing) + predictive insertion. During insertion a **diffusion policy generates candidate action chunks** and an **action-conditioned world model predicts their effects** on rod-hole alignment, so the agent **pre-execution evaluates** chunks by predicted tilt/radial error and picks the best.
- **Results**: Success rate improves from 88.9% to 96.7% vs diffusion-policy baselines, including an end-to-end setting.
- **Significance**: World model as pre-execution action evaluator — an inference-time re-ranking pattern directly usable in game bot controllers.
- **Link**: https://arxiv.org/abs/2609.12103

### 3.5 High-Fidelity Multi-Body Simulator for Autonomous Racing
- **Authors**: Nicola Musiu et al.
- **Affiliation**: MIT (inferred)
- **Venue**: arXiv preprint (2609.12795, cs.RO)
- **Key Innovations**: Custom high-fidelity vehicle-dynamics racing sim: a **Dymola multi-body digital twin** exported as an **FMU**, 3D road surfaces via the **Curved Regular Grid (CRG) standard** (elevation + curbs), integrated software-in-the-loop with a real autonomous-racing stack in C++. Includes a calibration procedure from experimental data.
- **Results**: Runs in real time on a portable computer and provides reliable ground truth for algorithm validation pre-deployment.
- **Significance**: Game-racing / sim-to-real infrastructure — the sim-fidelity backbone for industry racing AI (F1-style agent training).
- **Link**: https://arxiv.org/abs/2609.12795

---

## 4. Procedural Content Generation & Game Content

### 4.1 The Possibility of Solving a 3×3 Rubik's Cube under 2 Seconds — Optimizing Block Building
- **Authors**: Chung To Kong
- **Affiliation**: (independent, Hong Kong, inferred)
- **Venue**: arXiv preprint (2609.12946, cs.GT)
- **Key Innovations**: Speedcubing block-building is essential but has had no systematic training method. The **"AK-cubie method"** constructs **near-optimal block-building move sequences in short computation time**, and ships companion software so cubers can train look-ahead and block-building skills.
- **Results**: Positions the method as a contribution toward breaking the 2-second world record; gameplay re-watching reveals only outcomes, not mechanisms — this surfaces the mechanism.
- **Significance**: Puzzle-solving search/optimization with a human-training feedback loop — game-adjacent to "AI coaching for esports/competitive puzzles" and PCG of solve sequences.
- **Link**: https://arxiv.org/abs/2609.12946

### 4.2 CMA-OT: Hierarchical Expert Supervision for Dance-to-Music Generation
- **Authors**: Jinting Wang, Chenxing Li, Dong Yu, Li Liu
- **Affiliation**: Tencent AI Lab lineage (Dong Yu, inferred)
- **Venue**: accepted at **ACM MM 2026**; arXiv preprint (2609.13118, cs.AI / cs.SD)
- **Key Innovations**: Dance-to-music (D2M) generation has a semantic mismatch between sparse dance cues and dense composition needs. **CMA-OT** adds an external music expert that supervises the generator's *latent features* at multiple scales via a **curriculum-guided multi-scale learning** schedule, plus **scale-aware Optimal Transport** for fine-grained alignment under temporal mismatch.
- **Results**: State-of-the-art rhythmic synchronization, perceptual quality, and overall generation on two datasets.
- **Significance**: Rhythm/dance content generation is the direct cousin of rhythm-game charting and game-music PCG — hierarchical external-supervision is a reuseable recipe.
- **Link**: https://arxiv.org/abs/2609.13118

---

## 5. Benchmarks & Agent Evaluation

### 5.1 VRL-Bench: Benchmarking Agents on Computer Control Tasks under Finite Trial Budgets
- **Authors**: Yu Bai, Yukai Miao, Dawei Wang, Li Chen, Yanyu Ren, Yuqian Shi, Dan Li, Ying Xiong, Chengqiu Tan, Run Zhou, Li Li
- **Affiliation**: Tsinghua lineage (inferred)
- **Venue**: arXiv preprint (2609.12404, cs.AI)
- **Key Innovations**: A harness for **fair evaluation of trial-and-error (verbal RL) learning under finite budgets** on MiniWoB and WebShop. Re-evaluates Reflexion and later verbal-memory methods across three models: each improves success over memory-free retry in some settings and **reduces it in others**; replay experiments show reflection can actively lower success (exploit-vs-explore tradeoff). Proposes **VEX²**, a verbal exploration-exploitation scheduler that uses an LLM to jointly select policies and allocate the remaining trial budget.
- **Results**: VEX² is the only evaluated update with *positive* success-rate gains over retry in all six settings.
- **Significance**: Computer-control benchmarking for game-like GUI bots — and a warning that simplistic verbal self-improvement can backfire under budget constraints.
- **Link**: https://arxiv.org/abs/2609.12404

### 5.2 Embodied-BenchForge: A Closed-Loop Agentic Workflow for Embodied Benchmark Construction
- **Authors**: Baoyang Jiang, Fengchun Zhang, Leyuan Wang, Haotian Li, Yida Wang, Zhe Ji, Jinshan Lai, Xi Ren, Danyang Li, Zheng Yang, Jianwei Hu, Qiang Ma
- **Affiliation**: not specified (inferred — Chinese embodied-AI lab)
- **Venue**: arXiv preprint (2609.13082, cs.AI)
- **Key Innovations**: Benchmarks built by agentic systems suffer from **unverified intermediate artifacts propagating defects downstream**. Embodied-BenchForge formulates construction as **Closed-Loop Benchmark Synthesis**: forward artifact synthesis (typed, reusable "skills" into executable workflows) plus backward **Requirement-Guided Verification and Repair**, with an **artifact dependency graph** and provenance-driven local re-execution / upstream rollback.
- **Results**: Builds six benchmarks in the Offline EQA Track plus one interactive benchmark with 220 executable tasks; representative MLLMs/agents show the suite distinguishes observation-based understanding from closed-loop execution; ablations validate verification-repair and cross-benchmark skill reuse.
- **Significance**: The "verify every intermediate artifact" discipline applies directly to game-benchmark and agentic game-level construction.
- **Link**: https://arxiv.org/abs/2609.13082

---

## 6. Industry Game AI & Game Coaching

### 6.1 Understanding Game Coaching on Gig Platforms
- **Authors**: Hwijoon Lee, Saiph Savage
- **Affiliation**: Northeastern University (inferred)
- **Venue**: accepted at **CHI PLAY 2026**; arXiv preprint (2609.12695, cs.HC / cs.CY)
- **Key Innovations**: Interviews with 20 experienced freelance game coaches across **17 competitive games on Fiverr** — the first systematic study of human game-coaching as a gig economy. Coaches (without shared training) converge on rapport-building, individualized diagnosis, and adaptive feedback; two structural conditions shape the work: **dual precarity** (platform instability × live-service game lifecycle volatility) and **earned authority** (legitimacy via visible competitive achievement in the same spaces as students).
- **Results**: Coaches welcome AI for *administrative and analytic* support but **resist AI in live interactions**, where trust, relational engagement, and situated judgment stay central.
- **Significance**: Design constraints for **compute-assisted coaching / replay-analysis tools** and for bot-difficulty tuning that respects human coaching practice — a grounded Industry Game AI data point.
- **Link**: https://arxiv.org/abs/2609.12695

---

## 7. Related RL Techniques (Offline, Robust, Model-Based, Exploration)

### 7.1 SCQ: Stabilizing Conservative Q-Learning with Sigmoid-Bounded Entropy
- **Authors**: Xiefeng Wu, Shu Zhang, Zhaojie Chu, Mingyu Hu
- **Affiliation**: not specified (inferred)
- **Venue**: arXiv preprint (2609.12749, cs.AI)
- **Key Innovations**: Offline-to-online RL suffers persistent value-estimation instability; an overlooked source is the **standard log-entropy term going negative**, destabilizing policy updates. **SCQ** replaces it with a **sigmoid-bounded, strictly-positive** entropy formulation while keeping conservative Q regularization and return-based lower-bound calibration. A clipping/positive-score ablation shows **positivity itself**, not score shape, drives most gains.
- **Results**: Matches or exceeds baselines on D4RL (Minari), single-demonstration and standard settings, plus simulation and **real-robot** tasks across manipulation, wheeled, quadruped, humanoid.
- **Significance**: The "entropy sign" bug is a clean, transferable fix for CQL-family offline RL used in game agents.
- **Link**: https://arxiv.org/abs/2609.12749

### 7.2 MInTRL: Off-policy Intervention can Boost On-policy RL
- **Authors**: Mingyu Chen, Yefan Tao, Gerald Friedland, Xuezhou Zhang, Chris Kong
- **Affiliation**: multi-institution (inferred)
- **Venue**: arXiv preprint (2609.12419, cs.LG / cs.AI)
- **Key Innovations**: For RL with verifiable rewards, on-policy keeps data near the policy but limits discovery, while off-policy (SFT) expands coverage at the cost of distribution shift. **Minimal Intervention RL** inserts **sparse, local judge interventions** into otherwise on-policy rollouts: a judge-intervention policy periodically reviews the current output, replaces erroneous suffixes with short corrections, then returns control. Training uses **sequence-level advantage regression** (no importance sampling).
- **Results**: Beats on-policy and off-policy baselines on math and code benchmarks; remains effective with self-intervention and across judge policies; performance peaks at moderate intervention intensity ("intervene minimally").
- **Significance**: A principled bridge for exploration in RLVR/agent training — directly reusable in game-bot reward shaping.
- **Link**: https://arxiv.org/abs/2609.12419

### 7.3 Certified Safety Curation: Distribution-Free Guarantees for Safe Offline RL
- **Authors**: Adam Haroon, Cody Fleming
- **Affiliation**: University of Virginia (inferred)
- **Venue**: arXiv preprint (2609.12014, cs.LG)
- **Key Innovations**: When safety can only be judged by comparing short clips / occasional episode-budget checks (no per-transition cost), proposes **filter-then-clone**: a state-only value trained from segment comparisons scores whole trajectories, **Learn-then-Test calibration** certifies a selection threshold under a distribution-free (α, δ) bound on the unsafe fraction, then behavior cloning. Show reweighting individual transitions fails even with an exact value — the value must select whole trajectories.
- **Results**: Meets cost budgets on 11/15 DSRL tasks (one short of cloning the ground-truth safe subset); strongest full-label method becomes safe on a certified selection where no cost-target setting rescues it, and refusal probability has a closed form in pool purity.
- **Significance**: Safety certification for offline RL pipelines — applies to curating safe game-agent training sets.
- **Link**: https://arxiv.org/abs/2609.12014

### 7.4 A Unified and Constrained View of Regularization-Based Robust Reinforcement Learning
- **Authors**: Amine Andam, Jamal Bentahar, Mustapha Hedabou
- **Affiliation**: Concordia University (inferred)
- **Venue**: arXiv preprint (2609.13050, cs.LG)
- **Key Innovations**: Unifies regularization-based robust-DRL methods by deriving **new upper bounds on the nominal-vs-worst-case performance gap**, each expressed as an existing regularization objective plus a **KL-divergence penalty between nominal and worst-case policies** (explains why KL penalties help robustness). Reformulates robust training as **constrained optimization with a jointly-tuned Lagrange multiplier** instead of a fixed weight.
- **Results**: Extensive adversarial evaluations across continuous-control tasks validate the analysis.
- **Significance**: Theory for why robustness regularizers work in games/adversarial settings, with an auto-tuned multiplier recipe.
- **Link**: https://arxiv.org/abs/2609.13050

### 7.5 Robust Policy Optimization via Adversarial Importance Sampling (Advis)
- **Authors**: Amine Andam, Jamal Bentahar, Mustapha Hedabou
- **Affiliation**: Concordia University (inferred)
- **Venue**: arXiv preprint (2609.13044, cs.LG)
- **Key Innovations**: **Advis** estimates and optimizes **verifiable worst-case returns** via importance sampling over trajectories from standard training — jointly satisfying three criteria prior work didn't: no additional environment interactions, no auxiliary networks, and long-term robustness. Also releases **advrl**, a modular PyTorch library of robustness methods/attacks, and shows learned-adversary hyperparameters **do not transfer across agents**, so policies should be evaluated against 6–14× more attacker configurations.
- **Results**: Evaluated on continuous-control environments, outperforming existing robust-DRL baselines.
- **Significance**: Verification-style robust RL for game bots under input perturbation (e.g., observation noise / adversarial inputs).
- **Link**: https://arxiv.org/abs/2609.13044

---

## Summary Statistics

| Category | Papers Count |
|----------|-------------|
| Game RL & Multi-Agent RL | 4 |
| Game AI Bots & LLM Agents in Games | 2 |
| Game Foundation Models & World Models | 5 |
| PCG & Game Content | 2 |
| Benchmarks & Agent Evaluation | 2 |
| Industry Game AI & Game Coaching | 1 |
| Related RL Techniques | 5 |
| **Total featured papers** | **21** |

## Cross-references (covered by today's sibling digests, not re-featured)

- 2609.12422 — HORIZON hierarchical belief / opponent-conditioned zero-shot opponent adaptation (Lux AI S3) — [arxiv-ai-search 09-14](https://arxiv.org/abs/2609.12422)
- 2609.12220 — Fragility of Worst-Case Nash Equilibria in Atomic Congestion Games (UCCS) — [arxiv-ai-search 09-14](https://arxiv.org/abs/2609.12220)
- 2609.12446 — LLM belief shifts in Werewolf (NYCU, EMNLP'26) — [arxiv-daily 09-14](https://arxiv.org/abs/2609.12446)
- 2609.12459 — EvoRS on-policy self-evolution of reward DAGs for open-ended RL (Fudan) — [arxiv-daily 09-14](https://arxiv.org/abs/2609.12459)
- 2609.13037 — Mitigating Emergent Collusion in LLM Pricing Agents — [arxiv-daily 09-14](https://arxiv.org/abs/2609.13037)
- 2609.12077 — Pure Price of Anarchy for Networked Resource Allocation (UCCS) — [arxiv-daily 09-14](https://arxiv.org/abs/2609.12077)
- 2609.12531 — Temporal Recurrence Favors Fewer Layers (Sokoban study) — [arxiv-ai-search 09-14](https://arxiv.org/abs/2609.12531)

## Key Themes

1. **World models shift from generating to evaluating**: Pelican-Sim (2609.12036) makes a *general*, one-embodiment simulator with 5.67× distilled rollouts; IMPLY (2609.12441) argues consistency-only evaluation of WMs is unusable and must be **anchored to observed evidence**; DWMP (2609.12347) and RodForesight (2609.12103) reuse WMs as pre-execution action evaluators. The game-foundation-model story is now "roll out cheap, verify by physics, score actions before executing."

2. **The Mon-14 window is RL-methods heavy, game-domain thin**: The freshest mailing had almost no Atari/StarCraft/Go-style classic game-RL papers; the game-adjacent content arrived as embodied/AI robotics (Isaac Lab adversarial MARL, 2609.12758), diffusion-LM RL curriculum (2609.13060), and evaluation harnesses (2609.12404, 2609.13082). The game-RL frontier continues its migration toward embodied + LLM-agent domains.

3. **Robustness and safety go formal**: Two same-group papers from Concordia (2609.13050, 2609.13044) unify robust-RL regularization and give verification-style adversarial importance sampling; UVA's certified safety curation (2609.12014) gives distribution-free composition guarantees for offline warm-start sets.

4. **Multi-agent LLM pipelines show a negative result worth remembering**: The FIFA live study (2609.12495) found critic + meta-agent stages added no scoreline diversity over the strongest specialist — a direct check on the "more agents = better" assumption in game/storytelling agents.