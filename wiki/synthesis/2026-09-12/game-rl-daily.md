---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-09-12)"
type: synthesis
created: 2026-09-12
updated: 2026-09-12
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, pcg, benchmarks, world-models, self-play, multi-agent-rl, vlm, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-09-12)

> Recent arXiv + proceedings scan (2026-08-27 → 2026-09-11 window). The freshest arXiv mailing is **Fri 11 Sep 2026** (weekend = no new mailing on Sat 12 Sep). All featured IDs grep-verified **0 hits** in `wiki/`, and excluded from 09-09 → 09-12 sibling digests (game-rl-daily, arxiv-daily, arxiv-ai-search, arxiv-paper-check, conference-digest, tech-report-digest). **20 papers featured across 7 sections + 2 event/proceedings pointers.**
>
> **Continuity / already-covered (not re-featured):** GitGPU-CFR (2609.11923, 09-11 arxiv-daily), T1 terminal-agent RL (2609.11042, 09-12 arxiv-daily), TNBR (2609.11863) + ABRA (2609.11889) + Games-over-Observation-Space Capture-the-Flag (2609.06178) + last-iterate policy dynamics (2609.08823) [09-12 arxiv-daily], PlayTrain (2609.09059, 09-10 game-rl-daily), Programmable World Model (2609.10540, 09-11 game-rl-daily), LLM-guided NPC RL (2609.02931, 09-11 game-rl-daily), WorldMind (2608.21439, 09-10 game-rl-daily), ReactiveGWM/StatePlay/etc. (earlier digests).

---

## 1. Game RL — Reinforcement Learning in Games

### 1.1 The Surprising Effectiveness of Approximate Value Iteration in Self-Play
- **Authors**: Raphael Boige, Amine Boumaza, Bruno Scherrer
- **Affiliation**: Université de Lorraine (LORIA) / Inria Nancy (inferred)
- **Venue**: arXiv preprint (2609.09094)
- **Key Innovations**: Challenges the MCTS-dominated self-play paradigm. Trains a minimal self-play Approximate Value Iteration (AVI) agent and evaluates it with ground-truth oracles on non-trivial, moderately sized games (Connect Four, Hex 7×7, synthetic games). AVI learns *more accurate value functions* than AlphaZero, while its one-step-lookahead greedy policies remain competitive with MCTS-based policies at substantially lower training and inference cost. Preliminary experiments on Othello and Go(9×9) show AVI trains stably on larger games.
- **Significance**: Suggests the success of MCTS may have eclipsed simpler approaches that are increasingly practical — a useful counterweight to search-heavy recipes as deep-learning tooling matures.
- **Link**: https://arxiv.org/abs/2609.09094

### 1.2 Near-Optimal Reinforcement Learning with Multi-Step Transition Lookahead
- **Authors**: Corentin Pla, Hugo Richard, Marc Abeille, Vianney Perchet
- **Affiliation**: Université Gustave Eiffel / ENS Paris-Saclay — Criteo AI Lab (inferred)
- **Venue**: arXiv preprint (2609.11807, stat.ML/cs.LG)
- **Key Innovations**: Studies RL with ℓ-step transition lookahead (agent can observe which states any ℓ-action sequence leads to before acting — the abstraction behind game-tree search). Resolves two open questions: (1) exact planning with multi-step lookahead is **NP-hard for every fixed rational discount factor** γ∈(0,1); (2) near-optimal planning can still be done efficiently via a randomized polynomial-time approximation scheme.
- **Significance**: Formalizes the boundary between search-based game agents (lookahead) and RL value learning; gives theory that planning-under-lookahead is tractably *approximable* even where exact optimization is hard.
- **Link**: https://arxiv.org/abs/2609.11807

### 1.3 DRG-MAPPO: Hierarchical Dynamic Role-Graph Multi-Agent Reinforcement Learning for Cooperative Air Combat
- **Authors**: Junlin Liu, Chengwei Li, Yang Gao, Hui Chang, Xinchen Zhang, Zhijun Zhao, Hao Zhao
- **Affiliation**: (not specified)
- **Venue**: arXiv preprint (2609.11155)
- **Key Innovations**: MARL framework for cooperative air combat that combines graph-based relational modeling with dynamic role assignment. Constructs a battlefield interaction graph, extracts relational features among allies/enemies/threats via graph attention; a high-level policy assigns tactical roles (leader/supporter), and a low-level policy executes discrete maneuvers conditioned on roles + graph features. A target-priority auxiliary task fosters emergent focus-fire.
- **Results**: State-of-the-art 87% win rate; balances relational modeling, interpretability, and optimization stability.
- **Significance**: Game-like tactical simulation testbed with structured role reasoning — a concrete instance of hierarchical MARL for adversarial games.
- **Link**: https://arxiv.org/abs/2609.11155

### 1.4 SUN: Reaching for Novelty in Reinforcement Learning
- **Authors**: Wenyan Yang, Arsenii Mustafin, Dominik Baumann, Joni Pajarinen, Simone Parisi
- **Affiliation**: TU Darmstadt / Aalto University / TU Wien (inferred)
- **Venue**: Accepted at EWRL 2026 (19th European Workshop on RL); arXiv preprint (2609.08642)
- **Key Innovations**: First goal-selection scheme that scores goals by **novelty and reachability jointly** (prior work trades them off by hand, applies them in sequence, or drops one). SUN (SUccessor-to-Novelty) derives an indicator from successor value functions that identifies goals that are both novel and reachable; proves it recovers count-based bonuses in the limit, bounds short-horizon hitting probabilities, and provably rejects unreachable goals. Lightweight pseudocount avoids classic overhead.
- **Results**: Consistently outperforms SOTA in standard + novel environments with unreachable/hard-to-reach states, irreversible transitions, obstacles, mazes, unbounded spaces.
- **Significance**: Curiosity/exploration recipe directly applicable to open-ended game environments.
- **Link**: https://arxiv.org/abs/2609.08642

### 1.5 Certifying Lower Bounds for Risk-Sensitive Reinforcement Learning under Adversarial State Perturbations
- **Authors**: Tong Li, Saunak Kumar Panda, Yisha Xiang
- **Affiliation**: (not specified)
- **Venue**: arXiv preprint (2609.10866, cs.LG/math.OC)
- **Key Innovations**: Extends RL robustness certification from risk-neutral objectives to **risk-sensitive (exponential utility) objectives** under ℓ_p-norm-bounded state adversarial perturbations. Introduces a φ-divergence relaxation of the perturbation set, formulating risk-sensitive certification as convex optimization with lower bounds on expected cumulative reward.
- **Significance**: Safety-certification machinery for risk-sensitive agents — relevant to high-stakes game/match environments where reward variance matters.
- **Link**: https://arxiv.org/abs/2609.10866

### 1.6 Rank Without an Oracle: Deviation-Aware Interaction-Rank Selection from Offline Multi-Agent Logs
- **Authors**: Xiangwu Wang, Chengwei Cao, Hongyuan Tang
- **Affiliation**: (not specified)
- **Venue**: arXiv preprint (2609.08358, cs.MA/cs.GT)
- **Key Innovations**: Addresses a selection gap in offline MARL: payoff models are *estimated* under a logging distribution but *deployed* on distributions induced by learned solutions + unilateral deviations. SIRV (Selective Interaction-Rank Validation) evaluates nested interaction-rank candidates on a union of all deployment and unilateral-replacement distributions, returning the smallest rank within tolerance of the best worst-target risk; provides finite-candidate target-risk bounds and candidate-specific **CCE-gap certificates**, plus a two-point off-support non-identifiability result.
- **Results**: Empirical-Bernstein bounds cut median CCE-gap certificate by 42.5% vs Hoeffding on common returns (2,048 games/family factorial study); SIRV-EB fallback lowers mean selection CCE-regret under rank misspecification.
- **Significance**: Offline multi-agent model selection that respects strategic incentives — directly applicable to offline RL for games (SMAX/StarCraft-style datasets).
- **Link**: https://arxiv.org/abs/2609.08358

---

## 2. Game AI Bot — LLM-Powered Game Agents

### 2.1 MARBO: Relational Belief Grounding for LLM Agents in Social Deduction Games
- **Authors**: Hwang Yechan, Bae Sangjun, Kim Jeongmo, Bang Sangwoo, Han Seungyul
- **Affiliation**: (not specified — Korea)
- **Venue**: **EMNLP 2026** (accepted); arXiv preprint (2609.06563)
- **Key Innovations**: Social deduction games (Werewolf-style) require reasoning under partial observability via relational belief about hidden roles/team alignments. MARBO (Multi-Agent Relational Belief Optimization) is a belief-grounded preference optimization framework: it supervises LLM actions and in-game speech **only when behaviors are supported by reliable relational beliefs** and lead to strategically favorable outcomes. Explicitly mitigates strategically inconsistent behavior in compact LLM agents, which prior prompt/preference-optimization approaches fail to ground.
- **Significance**: One of the first belief-grounded RL/DPO pipelines for LLM agents in hidden-role games; addresses the perception-action gap in social-deduction settings.
- **Link**: https://arxiv.org/abs/2609.06563

### 2.2 SocialRL: Refining LLMs' Social Intelligence through Multi-turn Reinforcement Learning and Reward Design
- **Authors**: Jianing Wang, Xintao Wang, Aili Chen, Jie Shi, Hongcheng Guo, Jun Gao, Wenxuan Zhao, Chengkun Lang, Yuanli Guo, Yanghua Xiao
- **Affiliation**: Fudan University group (inferred)
- **Venue**: arXiv preprint (2609.09764, cs.CL)
- **Key Innovations**: Argues single-turn utterance optimization with sparse outcome rewards produces short-sighted dialogue policies. SocialRL applies **multi-turn PPO** that propagates delayed outcome rewards back to each turn for long-horizon planning, plus **six process-reward dimensions** capturing the goal-vs-relationship trade-off in sustained social interaction.
- **Significance**: Multi-turn RL reward design for conversational/NPC game agents — bridges dialogue and game-agent RL.
- **Link**: https://arxiv.org/abs/2609.09764

### 2.3 Fork Where the Model Changes Its Mind: Belief-Shift Branching for Tree-Structured Reinforcement Learning
- **Authors**: Bin Lei, Yu Li, Prafulla Kumar Choubey, Jiaxin Zhang, Becky Xiangyu Peng, Qinyuan Ye, Kartik Narayan, Caiwen Ding, Silvio Savarese, Chien-Sheng Wu
- **Affiliation**: Salesforce AI Research + academia mix (inferred)
- **Venue**: arXiv preprint (2609.11061, cs.AI)
- **Key Innovations**: Formalizes **fork placement** in tree-structured RLVR (sibling-outcome differences = step-level credit). Shows forks placed where the outcome is already settled yield almost no credit signal, so where you fork determines how much step-level RL gains. Proposes belief-shift branching that locates the *pivots* of a chain's value curve — where the expected outcome turns — instead of structure-based heuristics (fixed lengths, midpoints, delimiter tokens, next-token entropy).
- **Significance**: A principled credit-assignment recipe for sparse-reward game/agent RL over long rollout chains — complements CAST-style solver-as-teacher and other RLVR games work.
- **Link**: https://arxiv.org/abs/2609.11061

---

## 3. Game Foundation Models

### 3.1 World-Time Compute with Verified Code World Models
- **Authors**: James Schwoebel, Ingrida Semenec, Jenia Rousseva, Marcos Ortiz, Collin Overbay, Christopher Klaus, Anderson Edmond, Manish Bhatt, Rome Thorstenson, Jessica Tsai, Martin G. Frasch
- **Affiliation**: (not specified)
- **Venue**: arXiv preprint (2609.09163, cs.LG), 36 pages
- **Key Innovations**: When a domain's dynamics can be written as code, one template instantiates into many **verified code world models** — executable programs over symbolic state that yield an inexhaustible supply of exactly-labeled trajectories. Fine-tuning an LLM on trajectories through many such worlds ("world-time compute", a training-time analogue of test-time compute) lifts generalization to held-out worlds never trained on. Labels are trustworthy because worlds are verified code.
- **Results**: +29 points at 0.5B scale; largest model's lift within noise (saturation consistent with capability scarcity).
- **Significance**: A cheap data-manufacturing route for game-like world modeling — directly parallels game-code-world-model generation (GameCWM/Brown) covered in prior digests.
- **Link**: https://arxiv.org/abs/2609.09163

### 3.2 Learning Counterfactual World Models for Embodied Reasoning under Partial Observability
- **Authors**: Todd Y. Zhou, Daniel Zhang
- **Affiliation**: (not specified)
- **Venue**: arXiv preprint (2609.05834, cs.AI)
- **Key Innovations**: Identifies a failure mode — **counterfactual collapse**: a world model predicts visually plausible futures while failing to distinguish interventions with different behavioral consequences, arising from representations optimized for perceptual similarity rather than intervention structure (the objective of most large-scale pretrained video/multimodal encoders). Introduces counterfactual supervision so learned representations stay actionable under partial observability.
- **Significance**: Pins a concrete "knowing-doing" failure of video-pretrained world models and a representational fix — directly relevant to game foundation models (NitroGen/Game-TARS lineage).
- **Link**: https://arxiv.org/abs/2609.05834

### 3.3 H3-World: Turning Language Understanding into World Control
- **Authors**: Danze Chen, Zeqing Wang, Ziyue Lin, Xingyi Yang, Yeying Jin
- **Affiliation**: **Tencent / National University of Singapore / Hong Kong Polytechnic University (HKUST-internships at Tencent)**
- **Venue**: arXiv preprint (2609.01560)
- **Key Innovations**: Turns the 33B MiniMax-H3 video generator into an interactive world model without dedicated action modules: uses the native **language pathway** as the control interface (character + camera commands as compositional textual instructions aligned to temporal video latents), plus **temporal attention routing** to prevent control leakage across action intervals. Reuses the semantic representations from large-scale video pretraining.
- **Results**: Only 8,000 gameplay samples, 10,000 LoRA steps, 0.199% trainable parameters; precise character/camera control, preserved generation quality, and transfer to unseen scenarios.
- **Significance**: Industry-side evidence that "language-as-interface" is emerging in large video models — the same thesis as Programmable World Model (Tencent, 09-11) but via text conditioning instead of OBB compilation.
- **Link**: https://arxiv.org/abs/2609.01560

---

## 4. Procedural Content Generation (PCG)

### 4.1 Valerant: An Automatic Navigable Game Map Generator via Action-Conditioned World Model Exploration
- **Authors**: Yiran Qiao, Feng Wang, Jing Ma
- **Affiliation**: Hong Kong Baptist University group (inferred)
- **Venue**: arXiv preprint (2609.09418, cs.AI)
- **Key Innovations**: Extends World Action Models from 2D visual rollout space to **persistent 3D navigable geometry**. Since games (unlike driving/robotics) have no external physical substrate, Valerant's key insight is to couple a **pretrained action-conditioned world model** (training-free) with **SLAM-based spatial reconstruction** and **exploration-driven action selection**: predictive visual rollouts incrementally build a persistent 3D game map from a single input image.
- **Significance**: A training-free bridge between video world models and 3D map generation — reduces manual effort in game-level construction and opens a new PCG direction at the WM×geometry intersection.
- **Link**: https://arxiv.org/abs/2609.09418

---

## 5. Game Benchmarks

### 5.1 No new game-specific benchmark in the Fri 11 Sep window
- The Fri 11 / Thu 10 Sep windows produced no fresh 0-hit game benchmark papers (the scan flagged only non-game agentic benchmarks such as Mr.LHDR 2609.11318, Q2D-Web 2609.08887, ReactHuman 2609.10895 — embodied-robotics, not games).
- **Recent game benchmarks already covered in this wiki** (cross-refs, no re-feature): GameWorld 2604.07429, OmniGameArena 2606.09826, StarBench 2510.18483, BALROG 2411.13543, AVACraft (ACL'26 Findings), Orak 2506.03610, lmgame-Bench 2505.15146.

### 5.2 Proceedings/Event pointer: IEEE Conference on Games (CoG) 2026 competitions
- **Venue**: IEEE Conference on Games 2026 (site: cog2026.org, hosted by Universidad Complutense de Madrid)
- **Active competitions targeting LLM/game-RL agents**:
  1. **DareFightingICE LLM AI Competition** — real-time fighting-game agents restricted to **LLM prompting / fine-tuning only** (models ≤ 7B); no hand-coded rules or RL — tests pure LLM zero-shot control under 5-ms action deadlines.
  2. **Battlesnake Blackout** — multiplayer grid Battlesnake with fog-of-war (imperfect information): opponent modeling, trap-setting, long-horizon planning under uncertainty.
  3. **Planet Wars (RTS)** — human-designed code agents currently beat deep-RL agents; LLM-coded and evolutionary-coded agents explicitly welcome — a live benchmark of learned vs. static strategy.
- **Significance**: Live evidence of the industry shift the arXiv papers are driving toward (LLM-only game control, imperfect-information self-play, code-evolved strategies).

---

## 6. Industry Game AI

### 6.1 KuaiRP Series Role-playing Models Technical Report
- **Authors**: Kuaishou RP team (tech report)
- **Affiliation**: **Kuaishou (快手)**
- **Venue**: arXiv preprint (2609.11127)
- **Key Innovations**: Full technical solution for a dedicated role-playing model family balancing (1) simplified prompt engineering, (2) stable output quality, (3) built-in domain/world knowledge, (4) small-parameter efficient deployment. Multi-stage pipeline: standardized character templates + SFT data from user-behavior simulation and reverse-profile filtering → **rule-based composite reward RL** that eliminates length-expansion and repetitive-generation degradation → new **Two-stage On-Policy Distillation (OPD) with Cumulative-Divergence Decay (CDD)** self-distillation (domain-adapted model = teacher, original base = student) to recover general agent capabilities lost to domain SFT/RL.
- **Results**: Matches SOTA proprietary models in role-playing fidelity within target domains while recovering general capability at very low deployment cost.
- **Significance**: A production-grade recipe for the NPC/character-dialogue layer of game AI — the same catastrophic-forgetting-vs-domain-depth trade-off that ChatNPC/Nemobot work addresses.
- **Link**: https://arxiv.org/abs/2609.11127

### 6.2 Industry notes
- H3-World (Tencent, featured in §3.3) is the clearest fresh industry instance of game-foundation-model work this week.
- Cross-refs to recent industry coverage: GPU-CFR (2609.11923, 09-11 arxiv-daily), WorldMind (Tencent, 09-10), Matrix-Game 3.0, Kyutai Multiplayer WM, Magpie (09-11 digest).

---

## 7. Related Techniques

### 7.1 Self-Play

#### Building the Harness Automatically: Self-Play in Code Distills a Text Harness for Black-Box Optimization
- **Authors**: Yi Wu, Zheng Ren, Zhiyu Hu, Haochen Wang, Daryl Chang, Li Wei, Ting Wang, Zhen Li, Pooja Gupta, Nitin Jindal, Lukasz Heldt
- **Affiliation**: (not specified; industrial lab, inferred Google-affiliated)
- **Venue**: arXiv preprint (2609.09468, cs.LG)
- **Key Innovations**: Can an agent learn a numerical search strategy by *execution* and then transfer it as *text*? Under low budget, an agent repeatedly writes and evaluates optimizer programs, then distills the program + practice record into a frozen 197-word "Harness A" text prompt. Harness A cuts Gemini Flash regret 48% (independent N=30, p<.001), enters the GP-BO performance range on the practice family, lowers mean regret on all three held-out BBOB landscapes, and transfers to Claude Sonnet (−43%/−49%, p≤.005).
- **Significance**: Self-play-to-prompt distillation — empirical support for "learn by doing, then verbalize" that complements skill-library self-play (CoSkill, Skill-SP) covered in prior digests.
- **Link**: https://arxiv.org/abs/2609.09468

### 7.2 Exploration / Reward Design

#### TRACE: Training Reasoning Agents for Causal Exploration with Synthesized Rewards
- **Authors**: Rui Sun, Zhan Shi, Bing He
- **Affiliation**: (not specified — advertising-diagnostics setting)
- **Venue**: arXiv preprint (2609.10315, cs.AI/cs.LG)
- **Key Innovations**: Asks whether the verifiability asymmetry of RLVR (objective answers cheap to check in math/code but not in diagnostic reasoning) can be *engineered*: sample an intervention, inject it into a controlled simulator, generate the resulting observations, and use the hidden intervention as an oracle label. Instantiated in TRACE, a digital-advertising diagnostic environment where agents must investigate noisy, confounded, distributed evidence toward the synthesized cause.
- **Significance**: A "simulator-verifier" pattern for turning unstructured diagnostic tasks into game-like verifiable-reward RL — relevant to game analytics/bot diagnosis.
- **Link**: https://arxiv.org/abs/2609.10315

### 7.3 Multi-Task / Multi-Domain RL

#### One Step, One Lead: Mitigating Higher-Order Interference in Multi-Domain Reinforcement Learning via Cross-Step Control
- **Authors**: Zihan Lin, Xiaohan Wang, Jie Cao, Jiajun Chai, Guojun Yin, Wei Lin, Ran He
- **Affiliation**: CASIA (inferred)
- **Venue**: arXiv preprint (2609.06469, cs.LG)
- **Key Innovations**: Shows single-step (first-order gradient alignment / curvature) views can miss **sequential interference**: same-point domain gradients may stay near-orthogonal while consecutive realized updates partially reverse each other in output space. Proves consecutive token log-probability footprints recover this interaction as a local second-order term from adjacent checkpoints, without reconstructing same-point gradients. Proposes cross-step control to mitigate it.
- **Significance**: Stabilization recipe for training game agents across many games/domains jointly (Odysseus-style multi-level RL) — interference is what makes multi-game RL fail.
- **Link**: https://arxiv.org/abs/2609.06469

### 7.4 Offline RL / Value Estimation

#### Optimal Value Inference for Reinforcement Learning
- **Authors**: Nan Lu, Ethan Lee, James M. Robins, David Simchi-Levi, Junwei Lu
- **Affiliation**: MIT / Harvard (inferred)
- **Venue**: arXiv preprint (2609.09981, stat.ML/stat.ME)
- **Key Innovations**: Offline inference for the *optimal value*. Derives two nuisance functions as fixed points of a self-induced Bellman equation that approximates the max-Bellman operator with its softmax correspondence; constructs a debiased estimator via Neyman orthogonality with **asymptotic normality under diverging horizons** even under time-varying behavior policies. Applied to real decision problems including bike repositioning.
- **Significance**: Statistical foundation for offline RL model selection/value estimation in games where you only have logged play data (offline MARL/game-agent evaluation).
- **Link**: https://arxiv.org/abs/2609.09981

---

## Summary Statistics

| Category | Papers Count |
|----------|-------------|
| Game RL | 6 |
| Game AI Bot | 3 |
| Game Foundation Models | 3 |
| PCG | 1 |
| Benchmarks | 1 + 1 event pointer |
| Industry Game AI | 1 + cross-refs |
| Related Techniques | 4 |
| **Total featured papers** | **20** |

## Key Themes

1. **Search vs. simplicity in game RL**: AVI-vs-AlphaZero (2609.09094) and the multi-step-lookahead theory (2609.11807) both interrogate the "MCTS is the way" assumption — the field is re-benchmarking whether lighter self-play recipes are competitive.

2. **Belief-grounded LLM agents**: MARBO (EMNLP 2026) grounds preference optimization in relational beliefs for hidden-role games; SocialRL adds multi-turn process reward — the game-agent frontier is moving from text-fluency to world/role grounding.

3. **Language as the world-model control interface (industry)**: H3-World (Tencent) and Programmable World Model (09-11) converge on the same thesis — large video generators are becoming controllable game worlds, now via native text conditioning.

4. **Offline/multi-agent selection is now a certification problem**: SIRV (2609.08358) and Optimal Value Inference (2609.09981) treat offline model selection with strategic/statistical guarantees — offline RL for games maturing into a rigorous selection discipline.

5. **Novelty + reachability jointly (again)**: SUN (2609.08642) unifies the two exploration signals that prior curiosity methods trade off — recurring theme across this wiki's game-RL exploration threads.