---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-08-11)"
type: synthesis
created: 2026-08-11
updated: 2026-08-11
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, pcg, benchmarks, world-models, self-play, vlm, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-08-11)

> Curated papers on Game RL, Game AI Bots, Game Foundation Models, PCG, Benchmarks, Industry Game AI, and related techniques.
>
> **Coverage note**: The Tue Aug 11 arXiv announcement batch lands ~20:00 ET; the most recent submissions available now are those submitted Aug 8–10 (IDs ~2608.07500–2608.09926), which have not been covered by any prior digest. This report is therefore a **second-pass deep scan of the newest submissions** (6 fresh world-model/game papers) **plus recall fill-in** of strong game-AI papers from Apr–Jul 2026 that prior dailies missed (11 papers) and 2 ICML 2026 game-RL papers. Every paper below was **grep-verified absent** from the entire wiki (0 hits in index/log/synthesis/**) before inclusion. Fresh-window papers are cross-checked against today's [[2026-08-11/arxiv-paper-check]] and [[2026-08-11/conference-digest]] for zero overlap.

---

## 1. Game RL — Reinforcement Learning in Games

### 1.1 How Reasoning Evolves from Post-Training Data: An Empirical Study Using Chess
- **Authors**: Lucas Dionisopoulos, Nicklas Majamaki, Prithviraj Ammanabrolu
- **Affiliation**: UC San Diego
- **Venue**: ICML 2026 (accepted; earlier version = NeurIPS 2025 FoRLM Workshop, Oral)
- **Abstract**: Studies how reasoning evolves in a language model from SFT to RL, using chess as a clean, verifiable RL testbed. Compares six theoretically-motivated datasets: fine-tuning to directly predict the best move gives the strongest RL performance but the RL stage elicits **unfaithful reasoning** (reasoning inconsistent with the chosen move); training on multi-move trajectories yields comparable performance with faithful reasoning and more stable RL. Several SFT-checkpoint metrics (evaluation performance, hallucination rates, reasoning quality) predict post-RL performance. A 7B model built with this recipe surpasses leading open-source reasoning models in chess.
- **Key Innovation**: Chess as a probe for how SFT data shapes RL reasoning — dense high-quality tokens (best-move prediction) trade reasoning faithfulness for move quality; multi-step trajectories decouple the two. Releases models/data/code (lang-chess).
- **Link**: https://arxiv.org/abs/2604.05134

### 1.2 Reinforcement Learning in Super Mario Bros: Curriculum, Pedagogy, and Optimal Level Design in World 1-1
- **Authors**: Jesse Ponnock, Lucas Ho
- **Affiliation**: —
- **Venue**: arXiv:2606.29511 (June 28, 2026)
- **Abstract**: Reimplements World 1-1 of Super Mario Bros as a fully discrete environment and compares Q-Learning, SARSA, Monte Carlo, and DQN across three progressively complex level versions. Monte Carlo wins (94.9% ± 1.5% win rate vs DQN 76.4% ± 3.4%) by maximizing intermediate rewards along winning paths. A curriculum experiment permuting the six canonical level segments across twelve conditions shows the canonical ordering converges fastest, is most learning-efficient, and is the only condition with zero catastrophic failures — no random permutation matches all three criteria.
- **Key Innovation**: First empirical validation that World 1-1's design encodes genuine pedagogical structure measurable by RL — a real-data argument that curated level ordering accelerates learning beyond chance.
- **Link**: https://arxiv.org/abs/2606.29511

### 1.3 A Differentiable Atari VCS: A Complex, Fully Known Ground Truth for Explainable AI
- **Authors**: Andreas Maier, Siming Bayer, Patrick Krauss
- **Affiliation**: FAU Erlangen-Nürnberg
- **Venue**: arXiv:2606.22447 (June 21, 2026)
- **Abstract**: Reimplements the Atari 2600 VCS — the cradle of deep RL — as two independent end-to-end differentiable emulators in Julia (jutari) and JAX (jaxtari), validated bit-for-bit against xitari on all 64 supported ALE games (64/64 byte-identical RAM, 64/64 pixel-identical screens). Treats the cartridge ROM as a weight tensor, RAM as a soft tape, and control flow as gates, proving differentiable (soft) execution equals original (hard) execution.
- **Key Innovation**: A fully-specified, fully-differentiable game-computation substrate where every internal state is inspectable — closing the "no ground truth where XAI is needed most" gap for game agents and RL explainability.
- **Link**: https://arxiv.org/abs/2606.22447

### 1.4 Towards Scalable Multi-Task Reinforcement Learning with Large Decision Models
- **Authors**: Thibaut Kulak
- **Affiliation**: —
- **Venue**: arXiv:2606.24962 (June 23, 2026)
- **Abstract**: Introduces **LDM-v0**, a Large Decision Model trained offline on trajectories from thousands of heterogeneous RL environments. A multi-task, multi-modal transformer policy conditioned on observation/action/reward/termination histories, trained via supervised next-action prediction. A single pretrained model matches independently-trained task-specific reference policies on ~1,000 environments spanning robotics, autonomous driving, inventory management, cybersecurity, trading, and **video games**.
- **Key Innovation**: Demonstrates feasibility of large-scale offline pretraining of one sequence-model policy across heterogeneous RL domains including games — a decision-model analogue of foundation pretraining.
- **Link**: https://arxiv.org/abs/2606.24962

### 1.5 Revisiting Action Factorization for Complex Action Spaces
- **Authors**: Timothy Flavin, Sandip Sen
- **Affiliation**: University of Tulsa
- **Venue**: arXiv:2606.26574 (June 25, 2026)
- **Abstract**: Cross-sectional study of action-factorization methods (independent networks, shared encoder, VDN, QPLEX, Joint, Auto-Regressive) across PPO/SAC/DQN and discretized/hybrid/continuous action spaces on four lightweight game-like environments (Platform, hybrid-LunarLander, Hybrid-Shoot, CoopPush), ~220 valid configurations. Notes that default benchmark environments (Atari, SMAC, LunarLander) implement uniform action spaces, hiding the hybrid discrete-continuous challenges common in games. Releases two new C++ parallel Gymnasium environments.
- **Key Innovation**: Systematizes hybrid-action RL design choices for game/robotics control — a practical map of which factorization works for which algorithm × action-space combination.
- **Link**: https://arxiv.org/abs/2606.26574

### 1.6 Provably Optimal Learning Algorithms for Assistance Games
- **Authors**: Nivasini Ananthakrishnan, Mark Bedaywi, Michael I. Jordan, Stuart Russell, Nika Haghtalab
- **Affiliation**: UC Berkeley
- **Venue**: arXiv:2607.08012 (July 9, 2026)
- **Abstract**: Studies the online variant of assistance games — an informed agent (human) and an uninformed agent (assistant) repeatedly interact over T timesteps to optimize a common reward, the assistant seeing only the human's actions. Introduces **assistance regret** (gap to the optimal joint hindsight policy) and gives the first provably efficient decentralized algorithms achieving a (1−1/e)-approximate regret rate of Õ(T^3/4) with polynomial runtime. Proves no algorithm can beat the (1−1/e) factor (computationally intractable); a pseudo-decentralized variant with a shared random string reaches Õ(T^1/2), optimal up to log factors.
- **Key Innovation**: First provable guarantees for repeated assistance games (human-AI cooperation) — foundational theory for assistive AI in cooperative game-play and human-in-the-loop game settings.
- **Link**: https://arxiv.org/abs/2607.08012

### 1.7 Frontier Coding Agents Can Now Implement an AlphaZero Self-Play Machine Learning Pipeline for Connect Four That Performs Comparably to an External Solver
- **Authors**: Joshua Sherwood, Ben Aybar, Benjamin Kaplan
- **Affiliation**: —
- **Venue**: arXiv:2604.25067 (April 27, 2026, v2)
- **Abstract**: A proof-of-concept benchmark for **recursive self-improvement forecasting**: frontier coding agents must autonomously implement an end-to-end AlphaZero-style self-play ML pipeline for Connect Four on consumer hardware within a three-hour budget, given a minimal task description (no reference paper). Resulting game AIs are evaluated in a round-robin tournament anchored to the Pascal Pons Connect Four solver. Claude Opus 4.7 won as first-mover against Pons in 7/8 trials — statistically better than other agents tested (none exceeding 2/8). The task was impossible for all frontier agents in January 2026 but is now near-saturation.
- **Key Innovation**: Measures the capability to *autonomously reproduce* self-play RL research pipelines from a bare task description — an early-warning probe for AI-accelerating-AI, using a game AI as the testbed.
- **Link**: https://arxiv.org/abs/2604.25067

---

## 2. Game AI Bot — LLM-Powered Game Agents & NPC Intelligence

### 2.1 Empowering NPC Dialogue with Environmental Context Using LLMs and Panoramic Images
- **Authors**: Grega Radež, Ciril Bohak
- **Affiliation**: University of Ljubljana
- **Venue**: arXiv:2604.19192 (April 21, 2026, v2)
- **Abstract**: Gives NPCs spatial awareness by capturing panoramic images of their surroundings, running semantic segmentation, and encoding object locations + scene-graph data (directional vectors within the NPC's bounding sphere) into a structured JSON fed to the LLM. NPCs can then reference nearby objects, landmarks, and environment features dynamically instead of using pre-scripted dialogue. Evaluated via expert interviews followed by an integrated user study.
- **Key Innovation**: A cheap vision-pipeline wrapper (panorama → segmentation → spatial JSON) that makes LLM NPC dialogue grounded in the game world — directly addresses the spatial-blindness of scripted NPCs.
- **Link**: https://arxiv.org/abs/2604.19192

### 2.2 The Double-Edged Sword of Open-Ended Interaction: How LLM-Driven NPCs Affect Players' Cognitive Load and Gaming Experience
- **Authors**: Ting-Chen Hsu, Wenren Chen, Jiangxu Lin, Fei Qin, Zheyuan Zhang
- **Affiliation**: National Taiwan Normal University (tentative, inferred from co-author)
- **Venue**: arXiv:2604.10107 (April 11, 2026)
- **Abstract**: Randomized between-subject experiment (N=130) in a self-built game prototype comparing LLM-NPCs vs pre-scripted NPCs across multiple modules. LLM-NPCs significantly increased cognitive load (p < .001), mediated by expressive effort and response uncertainty, yet gave no significant overall experience gain (p = .195) — they boosted perceived autonomy but hurt system usability and trust. Effects varied strongly across task scenarios (p < .001), largest in open-ended modules (content creation, relationship building); extraversion (p = .031) and neuroticism modulate outcomes.
- **Key Innovation**: Controlled evidence that open-ended LLM-NPC interaction is a two-sided tradeoff — cognitive-load cost vs autonomy benefit — and that scenario structure, not just model quality, determines the experience outcome.
- **Link**: https://arxiv.org/abs/2604.10107

### 2.3 Game AI Not Fun? A Scoping Review and Meta-Analysis on the Differences in Enjoyment between Human and Computer Opponents
- **Authors**: Ray Ito
- **Affiliation**: —
- **Venue**: arXiv:2607.24749 (May 22, 2026)
- **Abstract**: Scoping review mapping 20 studies of player enjoyment against human vs computer opponents, plus a three-level meta-analysis of nine studies. Finds a statistically significant **medium-to-large pooled effect size: a psychological enjoyment penalty in computer-opponent conditions** — perceiving an opponent as artificial diminishes the experience despite advances in game-character AI.
- **Key Innovation**: Quantifies the "artificial opponent penalty" across the literature — an evidence base for why game AI (including RL/LLM bots) must be designed for perceived humanness, not just strength.
- **Link**: https://arxiv.org/abs/2607.24749

---

## 3. Game Foundation Models — Generalist Game Agents & World Models

### 3.1 Sekai2: From World Exploration to Interactive World Modeling
- **Authors**: Kang He, Wenshuo Peng, Zihui Gao, Jiaming Tan, Kaipeng Zhang, Yongtao Ge
- **Affiliation**: Shanghai AI Laboratory / OpenGVLab (tentative, inferred from co-authors)
- **Venue**: arXiv:2608.09449 (Aug 10, 2026)
- **Abstract**: World-exploration video dataset for interactive world modeling: 128,892 clips / 2,826 hours / 10,428 source videos across 113 countries, deliberately weighted toward sustained observation (43,594 two-minute segments = 51.4% of footage). Every clip carries a released camera trajectory and hierarchical annotations disentangling subject motion, environment dynamics, static content, and camera behavior (649,597 temporally grounded segments). Crucially includes 982 **panoramic sequences with non-linear trajectories, loops, and revisits** — repeated observations of the same locations across time/viewpoint, providing supervision for persistent scene representations and long-term spatial memory.
- **Key Innovation**: A corpus that jointly provides long videos + camera trajectories + time-aligned semantics (which web video and pose-annotated datasets each lack individually), purpose-built for long-horizon, camera-controllable, interactive world-model pre-training.
- **Link**: https://arxiv.org/abs/2608.09449

### 3.2 Learning How the World Evolves: Extrapolative Video World Models via Latent Dynamics Reasoning
- **Authors**: Haodong Li, Shaoteng Liu, Tianyu Wang, Chongjian Ge, Sihui Ji, Jiahan Zhang, Xin Lin, Haolin Lu, Zhe Lin, Manmohan Chandraker
- **Affiliation**: — (inferred: UCSD / Adobe Research / PKU)
- **Venue**: arXiv:2608.09926 (Aug 10, 2026)
- **Abstract**: Argues leading video diffusion models fit pixels without modeling how pixels transit over time, so they render plausible frames that may violate physical laws. **Latent Dynamics Reasoning (LDR)** casts latent transition as explicit kinematic integration: lower-order dynamics are integrated numerically and the model regresses only the third-and-higher-order residual. On a controlled white-box physics benchmark (uniform motion, parabola, collision, bouncing, looming), LDR's in- vs out-of-distribution error gap is >20× smaller than the video-diffusion baseline at 256² resolution, with 26× fewer parameters and 143× faster. It even generalizes under severe shift (trained on red balls left-to-right, predicts a blue square right-to-left).
- **Key Innovation**: First video world model that extrapolates learned dynamics beyond its training distribution — an explicit-dynamics prior for game-style physics rollouts.
- **Link**: https://arxiv.org/abs/2608.09926

### 3.3 Population-Scalable Multi-Agent World Modeling (Khora)
- **Authors**: Renjie Zhao, Yuxiang Wu, Mingyu Zhang, Jiaxin Li, Sisi Li, Yimin Sheng, Tianxi Tan, Zhenkai Zhang, Jianyi Zhu, Yong-Lu Li
- **Affiliation**: SJTU (tentative, inferred from co-author)
- **Venue**: arXiv:2608.08600 (Aug 9, 2026)
- **Abstract**: Existing multi-agent world models assume a fixed number of agents at train and inference time. **Khora** instead derives cross-view consistency from a shared world state whose evolution does not assume a predefined agent count, and generates agent-specific observations by querying this state through a unified rendering interface. Decoupling world-state evolution from visual rendering enables **inference-time expansion to arbitrary numbers of agents without retraining**, with approximately linear practical scaling in the number of queried views. Generalizes to unseen agent counts while maintaining visual quality and multi-agent consistency; ships a real-time interactive system.
- **Key Innovation**: Population-agnostic rendering via shared world state — breaks the fixed-N bottleneck for scalable multi-agent game/world simulation (extends the γ-World / MASS line).
- **Link**: https://arxiv.org/abs/2608.08600

### 3.4 Twin Rollouts: Noise-Coupled Counterfactual Branching in Interactive Video World Models
- **Authors**: Yu Ma, Hongli Shi, Xinran Xu
- **Affiliation**: —
- **Venue**: arXiv:2608.08982 (Aug 10, 2026)
- **Abstract**: Studies counterfactual generation inside interactive-video rollouts: given a model-generated trajectory, what would have happened had actions differed from step t* onward? Formalizes **noise-coupled twin rollouts** — a factual and a counterfactual branch sharing the generated prefix and the future exogenous-noise sequence, diverging only in the action stream. Because the factual branch is self-generated, its exogenous noise is known exactly, making Pearl's abduction step exact by construction (sidestepping the approximate-inversion problem of editing-based pipelines). A spatiotemporal locality metric penalizes divergence outside the intervention's causal descendants; forking the simulator state at t* yields ground-truth re-renders usable as verifiable rewards for post-training.
- **Key Innovation**: Turns counterfactual minimal-change into a per-sample verifiable property — a recipe for RL/post-training signal in interactive game-world models (framework + metrics; experiments forthcoming).
- **Link**: https://arxiv.org/abs/2608.08982

### 3.5 WorldSimProbe: Diagnosing Simulator Faithfulness in Action-Conditioned World Models for Embodied Manipulation
- **Authors**: Peterson Co, Sicheng Hu, Chunxuan Jiao, Hongyang Cheng, Yulin Luo, Yijie Xu, Sixiang Chen, Zhongxia Zhao, Zihao Wang, DaFeng Chi, Peidong Liu, YuTong Chen, Henghua Liu, Zhihao Yuan, Huizhu Jia, Yuzheng Zhuang, Tianle Zhang, Liang Lin, Huajie Tan, Shanghang Zhang
- **Affiliation**: — (inferred: PKU / Sun Yat-sen University)
- **Venue**: arXiv:2608.09298 (Aug 10, 2026)
- **Abstract**: Action-conditioned world models (ACWMs) promise scalable predictive simulators for planning, but prevailing evals measure visual quality or task outcomes rather than simulator fidelity. Formalizes the **Observable Simulator Contract** (supplied actions must induce corresponding agent motion; environment responses must be grounded in that realized motion) and operationalizes it as **WorldSimProbe**: five controlled suites (local control sensitivity, global trajectory variation, source-diverse actions, interaction grounding, dynamics), evaluated on six open-source ACWMs over 18,000+ instances across RoboTwin, ManiSkill, and LIBERO. Reveals systematic action-realization degradation and structured interaction/dynamics failures, with benchmark signals consistent with human judgments and downstream outcomes.
- **Key Innovation**: A capability-based, contract-style diagnostic for whether a world model actually *simulates* — a transferable standard for validating game/embodied world models beyond coarse task success.
- **Link**: https://arxiv.org/abs/2608.09298

### 3.6 verdi: Retrieval Is Not Transfer for Continual World Model Optimization
- **Authors**: Junyu Wu, Shiqin Nie, Youyi Kou, Baohua Yin, Guocai Yao, Qingyu Chen, Jingheng Ma, Shiji Zhou, Hongyong Song, Mingchen Zhuge, Sen Cui, Changshui Zhang
- **Affiliation**: Tsinghua University (tentative, inferred from co-author)
- **Venue**: arXiv:2608.09537 (Aug 10, 2026)
- **Abstract**: Optimizing a pretrained world model toward a user objective usually rediscovers optimization strategies from scratch; existing research agents treat successful strategies as directly reusable recipes without transfer safeguards. **VERDI** argues retrieval ≠ transfer: a strategy validated on one model is at best an optimization hypothesis for another, becoming transferable knowledge only after target-side experimental validation. It builds an **Optimization Fingerprint** per model via shared inference-time probes, retrieves relevant prior experience as ranked hypotheses, validates every candidate under a frozen target-side verifier before admitting it as reusable evidence, and evolves probes on fingerprint contradictions. On Ctrl-World, the Cosmos family, and RoboCoin: search cost −68%, GPU cost −69%, negative transfer 0.34→0.06, transfer-outcome prediction at 83% sign accuracy.
- **Key Innovation**: Evidence-licensed continual optimization for world models — treats cross-model strategy transfer as a validation problem, not a retrieval problem.
- **Link**: https://arxiv.org/abs/2608.09537

---

## 4. Procedural Content Generation (PCG)

### 4.1 GUI Agents for Continual Game Generation (Play2Code / PlaytestArena)
- **Authors**: Yixu Huang, Bo Li, Na Li, Zhe Wang, Kaijie Chen, Haonan Ge, Qingyi Si, Yuanzhe Shen, Ruihan Yang, Guangjing Wang, Hongcheng Guo
- **Affiliation**: — (inferred: Peking University)
- **Venue**: arXiv:2605.28258 (May 27, 2026)
- **Abstract**: Argues generating a game is not the same as making one that can be played — one-shot prompt→artifact translation leaves interaction-level failures undetected. Uses GUI agents in two roles: (1) **objective evaluator** via **PlaytestArena** (200 browser-based game-generation tasks across 8 genres with expected in-play-behavior rubrics, adjudicated by a GUI agent that loads each build in a browser and plays it); and (2) **subjective playtester** via **Play2Code**, where a game agent and a GUI agent operate in a sustained loop with shared memory, turning game generation into a dialogue between coding and playing. Even frontier models struggle to generate playable games directly; Play2Code reaches a 66.8% rubric pass-rate (+37.1 / +14.6 over single-pass and agentic-coding baselines). GUI playtester feedback is more traceable than human reports yet idiosyncratic in human-tester-like ways.
- **Key Innovation**: Agent-in-the-loop playtesting as the missing feedback channel for game code generation — the "a game must be played" evaluation principle for LLM PCG.
- **Link**: https://arxiv.org/abs/2605.28258

---

## 5. Game Benchmarks

### 5.1 Social Gym and SPaRTan: Benchmarking and Improving LLM Social Reasoning via Multi-Agent Game Tournaments
- **Authors**: Keyu He, Xuhui Zhou, Maarten Sap
- **Affiliation**: CMU
- **Venue**: arXiv:2608.09128 (Aug 10, 2026)
- **Abstract**: Social interaction lacks objective ground truth, so evals fall back on costly, noisy LLM judges and models get no reliable learning signal. **Social Gym** is an environment of 21 multi-agent social games (Werewolves, Resistance, Spyfall) whose rule-decided outcomes make agent performance verifiable and objective, with an Elo tournament producing a cross-game leaderboard. GPT-5-mini tops the board, but no model excels at all games or roles — exposing social-reasoning limits. **SPaRTan** (Self-Play and Reflect-Transfer) is a training-free self-improvement loop: a model plays a game, reflects on trajectories/outcomes to produce a transferable playbook, and applies it in subsequent games. Playbooks help GPT-5-mini level up on weaker roles but largely do not improve Qwen3-32B.
- **Key Innovation**: Verifiable, judge-free social-reasoning evaluation (rule-decided outcomes + Elo), plus a training-free self-improvement method for social-deduction game agents.
- **Link**: https://arxiv.org/abs/2608.09128

---

## 6. Industry Game AI

> **No new studio-authored submissions in this window.** Industry-relevant items above: Khora's real-time interactive open-world simulator (3.3) and Sekai2's corpus-scale interactive-world resource (3.1). Ongoing tracked industry threads — EA SPORTS NHL 26 automated game testing (2607.07498, [[2026-08-01/game-rl-daily]]), KRAFTON PUBG ALLIE ([[2026-07-17/game-rl-daily]]), NVIDIA ACE/NVIGI ([[2026-07-13/game-rl-daily]]), NVIDIA NitroGen CVPR 2026 Oral generalist game agent + γ-World multi-agent world model ([[2026-07-27/game-rl-daily]], [[2026-08-10/conference-digest]]), Google DeepMind game theory for foundation models (2608.03958, [[2026-08-10/conference-digest]]).

---

## 7. Related Techniques — Human-in-the-Loop RL, Game-Theoretic Agents, Safe World-Model RL

### 7.1 Learning Safe Agent Behaviour from Human Preferences and Justifications via World Models (DROPJ)
- **Authors**: Ilias Kazantzidis, Timothy J. Norman, Yali Du, Christopher T. Freeman
- **Affiliation**: University of Southampton / King's College London (inferred from co-authors)
- **Venue**: arXiv:2607.13172 (July 14, 2026)
- **Abstract**: Addresses safe training and deployment when environment dynamics are unknown and no suitable reward exists. **DROPJ** first learns a world model (a learned simulator) from a dataset of prior real-world trajectories; a human plays the game *inside this learned simulator* to extract informative simulated trajectories; pairs of trajectory segments elicit human preferences **plus justifications**; a reward model is trained from these justified preferences and used, together with the world model, to deploy the agent via model predictive control. Real-user experiments show simulator-played informative trajectories significantly cut training compute versus other strategies and can improve deployment performance.
- **Key Innovation**: Human-in-the-loop safe RL that adds *justifications* to preference queries and reuses the world model for both reward learning and MPC deployment — practical for safety-critical game-agent/NPC training.
- **Link**: https://arxiv.org/abs/2607.13172

### 7.2 Game of Thought: Robust Information Seeking with Large Language Models Using Game Theory
- **Authors**: Langyuan Cui, Chun Kai Ling, Hwee Tou Ng
- **Affiliation**: National University of Singapore
- **Venue**: arXiv:2602.01708 (Feb 2, 2026); ICML 2026 (accepted per third-party listings)
- **Abstract**: Uses Twenty Questions to evaluate LLM information-seeking and formalizes its adversarial counterpart, **Strategic Language Search (SLS)**, as a two-player zero-sum extensive-form game with imperfect information. **Game of Thought (GoT)** applies depth-limited subgame solving with heuristic leaf payoffs and counterfactual regret minimization to approximate Nash-equilibrium strategies. Consistently improves worst-case performance versus direct prompting and heuristic-guided search across all tested settings.
- **Key Innovation**: Game-theoretic (CFR/subgame-solving) robustness for LLM information-seeking agents — worst-case guarantees from equilibrium play rather than prompt heuristics.
- **Link**: https://arxiv.org/abs/2602.01708

---

## Summary Statistics

- **Total new papers**: 19 fully listed (verified NEW via grep against the entire wiki), across all 7 categories
- **Fresh window (submitted Aug 8–10, 2026)**: 6 papers — Sekai2, LDR extrapolative world models, Khora, Twin Rollouts, WorldSimProbe, VERDI, Social Gym & SPaRTan
- **Recall fill-in (Apr–Jul 2026, previously missed)**: 11 papers — chess reasoning, Super Mario RL, differentiable Atari, LDM-v0, action factorization, assistance games, AlphaZero pipeline, NPC dialogue, LLM-NPC cognitive load, AI-opponent enjoyment, GUI game generation, DROPJ
- **Key venues**: ICML 2026 (chess reasoning, Game of Thought), arXiv preprints
- **Notable trends**:
  - **World models move toward population scalability and simulator fidelity**: Khora (arbitrary agent counts, inference-time), WorldSimProbe (contract-based fidelity diagnosis), Sekai2 (exploration corpus with loop-revisit supervision), LDR (extrapolative dynamics), Twin Rollouts (counterfactual as verifiable reward), VERDI (evidence-licensed continual optimization) — the frontier is no longer just "generate plausible pixels"
  - **Games as verifiable RL testbeds for LLM reasoning**: chess for SFT→RL reasoning evolution (2604.05134); social-deduction games with rule-decided outcomes as judge-free social benchmarks (Social Gym); Twenty Questions as an extensive-form-game eval (Game of Thought)
  - **Player-centric game AI evidence accumulates**: LLM-NPCs raise cognitive load without experience gains (N=130 study); meta-analysis quantifies the "artificial opponent" enjoyment penalty — game AI quality is becoming an empirical player-experience question, not just a win-rate question
  - **Self-play research automation as an AI-progress probe**: coding agents now reproduce AlphaZero pipelines near-saturation (Connect Four benchmark) — game RL as the canary for AI-accelerating-AI
  - **PCG gains a player**: GUI agents that actually play generated games close the loop for game-code generation (Play2Code/PlaytestArena)

## Cross-References

- [[2026-08-10/game-rl-daily]] — prior digest (MDT solver-guided poker, Aftab, MemWM, Dueling World Models, WorldTrace, TRIAL, MARP)
- [[2026-08-11/arxiv-paper-check]] — same-window second-pass scan (18 papers, zero overlap)
- [[2026-08-11/conference-digest]] — Anthropic Riemann zeta, ICLR 2026 RSI workshop, WorldEvolver
- [[2026-08-10/conference-digest]] — γ-World (NVIDIA), Google embedded Bayesian game theory, KDD 2026
- [[2026-07-27/game-rl-daily]] — SPIRAL/STRATAGEM self-play reasoning, NitroGen, OmniGameArena benchmarks
