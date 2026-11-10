# Game RL & Game AI Bot — Daily Paper Digest (2026-11-10)

- **Date**: 2026-11-10
- **Window**: ~2026-10-20 → 2026-11-09 (latest available arXiv submissions/revisions and recent proceedings metadata indexed at query time; web search tooling was unavailable in this run, so discovery used arXiv Export API, `/list/cs.AI|cs.LG/recent`, and arXiv abstract pages)
- **Scope**: Game RL, multi-agent/self-play RL, LLM/VLM game agents, game foundation/world models, procedural content generation (PCG), game benchmarks/datasets, industry/academic game-AI systems, and related techniques (world models, reward shaping/credit assignment, hierarchical decomposition, imitation/distillation-adjacent decision learning, exploration/robustness diagnostics)
- **Method note**: Paper metadata below is taken from arXiv abstract pages/API entries fetched on 2026-11-10. Performance numbers, affiliations, and venue claims are **author-reported** unless explicitly stated as proceedings metadata on arXiv. Where arXiv did not expose structured affiliations, entries state that explicitly.

## Executive Summary

Recent game-AI work shows a strong convergence around **playable, controllable world representations** and **decision interfaces that better match game structure**. On the world-model side, Tiresias/LCWM-Bench unifies language-conditioned planning across navigation, robotics, 3D gaming, and driving, while PlayGen2, Fight World Model, Wizard, and WMEval push from plausible video generation toward persistent state, executable rules, physical consistency, and real-time control. On the agent side, papers target diagnosis and reliability rather than raw scores alone: XiangqiBench exposes closed-loop gaps in LLM board-game play, Pac-Man VLM diagnostics separate perception/memory/decision failures, and RLiD moves RL optimization into the executable decision plane for Sokoban/ALFWorld-style agents. In RL/game systems, new results span reward/persona blending (RIDGE), hierarchical policy decomposition for complex roguelikes (Balatro), policy-parameter generation via diffusion (DPPG), and low-cost physical adversarial MARL platforms (KlaskTron). PCG and benchmarks continue to industrialize evaluation: CAD/IEEE CoG 2026 evolves reusable generator programs, while EWM provides multi-view esports data linking observations, actions, and shared state for StarCraft II/Dota 2/CS2.

## Papers

### 1) Game RL

#### Reinforcement Learning for the Game of Balatro: A Fast Simulator and Two-Policy Training Approach
- **Authors**: Ajay Vikram Periasami, Anjaneya Gupta, Ethan Cheng, Ivan Rosales
- **Affiliation**: Not explicitly listed on arXiv abstract page (author affiliations not shown in metadata)
- **Venue / status**: Accepted at EXAG 2026 (AIIDE Workshop on Experimental AI in Games), arXiv 2026-10-28
- **Abstract (summary)**: Addresses Balatro's RL challenges—~3,000 state-dependent actions, long sparse-reward horizons, and stochastic card/shop dynamics—via a Rust simulator diffed against the live client, a masked observation/action interface, and a two-policy PPO decomposition (tactical blind play + strategic shop policy) with cross-agent credit routing.
- **Key innovations**:
  - High-throughput Balatro simulator with automated state-diff validation against the game client.
  - Decomposed multi-policy architecture over disjoint decision phases sharing full state.
  - Per-agent reward routing to improve long-horizon credit assignment.
- **Reported results**: Main joint run reportedly reaches >99% first-blind clear rate and ~10× mean episode return increase, plateauing at mean max ante 3/8; single-agent baselines fail to stably clear first blind.
- **Links**: [arXiv](https://arxiv.org/abs/2610.39049) | [PDF](https://arxiv.org/pdf/2610.39049)

#### Policy Network Diffusion
- **Authors**: Jiate Liu, Deheng Ye
- **Affiliation**: Work done at Tencent in 2024 (as stated on arXiv)
- **Venue / status**: arXiv preprint, v2 2026-11-07
- **Abstract (summary)**: Proposes Diffusion-based Conditional Policy Network Parameter Generation (DPPG), using a Transformer autoencoder to patchify/compress policy parameters and a task-conditioned diffusion model to generate RL policy weights across environments.
- **Key innovations**:
  - Treats policy-network parameters as generative targets for conditional diffusion.
  - Patchified parameter autoencoding enables higher-capacity network generation than prior parameter-generation approaches.
  - Single model synthesizes policies across Classic Control, Atari, and MuJoCo.
- **Reported results**: Generates high-quality policies across domains and can produce faster convergence / competitive performance in previously unseen environments (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.04614) | [PDF](https://arxiv.org/pdf/2611.04614)

#### RIDGE: State-Conditioned Reward Blending for Behavioral Coverage in Deep RL Game Agents
- **Authors**: AL Muqshith Mohammed Shifan, Kevin Christopher Chua, Ali Neshati, Loutfouz Zaman, Cristiano Politowski
- **Affiliation**: Not explicitly listed on arXiv abstract page
- **Venue / status**: Conference of Games (CoG 2026), arXiv 2026-11-03
- **Abstract (summary)**: Introduces a single RL agent that blends multiple persona rewards at runtime for automated playtesting in Crafter, avoiding training N separate persona agents and mitigating reward non-stationarity.
- **Key innovations**:
  - State-conditioned softmax/sigmoid blender over slow-moving state variables.
  - Multi-head critic with one value head per persona trained on stationary signals.
  - Targets switching-stability issues in PPO under changing reward composition.
- **Reported results**: On Crafter with four personas, one RIDGE agent acquires both branches of the wood-tier crafting/combat split that no fixed-persona baseline solves jointly (n=3 seeds per condition, author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.05601) | [PDF](https://arxiv.org/pdf/2611.05601)

### 2) Game AI Bot / LLM & VLM Game Agents

#### RLiD: Reinforcement Learning in the Decision Plane for Language Agents and LLMs
- **Authors**: Ziyi Chen, Yan Zhang, Jianhui Wei, Jianing Yin, Daoan Zhang
- **Affiliation**: Not explicitly listed on arXiv abstract page
- **Venue / status**: arXiv preprint, 2026-11-02
- **Abstract (summary)**: Optimizes executable action-option probabilities directly instead of token-level responses for LLM/language-agent RL, reducing gradient variance from paraphrastic action text and invalid parses.
- **Key innovations**:
  - Decision-plane RL over labeled executable action menus with single forward-pass selection.
  - Optional compact memory and compilation of observations/actions into model input.
  - Distills trained large decision-model policies into generative LLMs.
- **Reported results**: ARC/Countdown/Sokoban improvements or lower cost in several settings; ALFWorld pipeline reaches 99.3% success in 12.7 H100 GPU-hours vs 86.6% in 17.3 GPU-hours for token-level RL; strongest Qwen2.5-1.5B LDM/distilled LLM reaches 100% on 134 unseen + 140 seen ALFWorld games (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.02455) | [PDF](https://arxiv.org/pdf/2611.02455)

#### Finding the Move Is Not Winning the Game: XiangqiBench for Closed-Loop Evaluation of LLM Agents
- **Authors**: Yekun Chai, Qiwei Peng, Haoyi Xiong
- **Affiliation**: Not explicitly listed on arXiv abstract page
- **Venue / status**: arXiv preprint, 2026-10-01
- **Abstract (summary)**: Evaluates LLM agents in closed-loop Chinese chess endgames (119 forced-mate positions) against an engine defender, separating move naming from actually delivering checkmate under opponent response.
- **Key innovations**:
  - Executable REPL interface separating real moves, state queries, and forward simulation.
  - Large trajectory dataset: 8,568 multi-turn trajectories from 12 frontier LLMs.
  - Diagnoses Conversion Gap, Consistency Gap, and Simulation Gap.
- **Reported results**: Reference first-move rate 26.1% in Sighted trials but only 13.9% wins; leading model 38.7% pass@3 vs 5.9% pass^3; 32.3% accepted simulations end in illegal moves and 49.3% comparable cases differ from real defender replies.
- **Links**: [arXiv](https://arxiv.org/abs/2610.02425) | [PDF](https://arxiv.org/pdf/2610.02425)

#### Where It Breaks: Diagnosing Perception, Memory, and Decision Failures of a Vision-Language Agent in Pac-Man
- **Authors**: Xinglu Wang, Edward Wang, Yong Zhang, Zhenan Fan
- **Affiliation**: Not explicitly listed on arXiv abstract page
- **Venue / status**: arXiv preprint, 2026-11-04
- **Abstract (summary)**: Diagnoses why a Qwen3.5-9B-based Pac-Man agent fails by separating perception checks from primitive-policy RL with textual boards, isolating screen-reading errors from sequential decision failures.
- **Key innovations**:
  - Component-wise diagnosis (perception, memory/interaction, decision) rather than single end-score evaluation.
  - Textual-board policy study removes image transcription from decision interface.
  - Post-training evaluation guidance: evaluate perception in use, distinguish training from full-game validation, inspect decisions over time.
- **Reported results**: Held-out maze completion rises from 0% to 80.2% at selected checkpoint (three extra lives) in textual-board policy study; static screenshot accuracy can coexist with interaction-time errors (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.06704) | [PDF](https://arxiv.org/pdf/2611.06704)

#### Catalyzing Interactive HTML Generation Capabilities via High-Fidelity Reinforcement Learning
- **Authors**: Xujia Wang, Yixuan Liu, Shaohan Huang, Furu Wei, Lei Hou, Bin Xu, Juanzi Li
- **Affiliation**: Not explicitly listed on arXiv abstract page (author list includes Shaohan Huang and Furu Wei, commonly associated with Microsoft Research Asia in public literature; affiliation not stated in arXiv metadata and should be verified from PDF)
- **Venue / status**: arXiv preprint, 2026-11-03
- **Abstract (summary)**: Uses mini-games as a demanding testbed for interactive HTML/code generation, training with browser-interaction RL and higher-fidelity reward/credit signals.
- **Key innovations**:
  - WebCatalyst framework with game-level GUI assessor for sustained interaction.
  - Visual Anchor to mitigate VLM reward hacking.
  - Action-Trace Credit for runtime-grounded token-level credit assignment.
- **Reported results**: With <1K training requests (mostly games), Cookie-Bench Mini Games improves 68.8→75.3 and WebGen-Bench accuracy 48.8→56.9 on Qwen3.6-35B-A3B, outperforming Claude Opus 4.7 in average rank across evaluated metrics (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.05151) | [PDF](https://arxiv.org/pdf/2611.05151)

### 3) Game Foundation Models / World Models

#### Tiresias: Towards Language-Conditioned World Models
- **Authors**: Fengyi Wu, Yifei Dong, Yetong Sha, Lingdong Kong, Qiyu Hu, Bohan Xiong, Qi Dai, Alexander G. Hauptmann, Zhi-Qi Cheng
- **Affiliation**: Not fully listed on arXiv abstract page (Alexander G. Hauptmann is publicly associated with CMU; full institutional affiliations should be verified from PDF)
- **Venue / status**: arXiv preprint, 2026-11-07
- **Abstract (summary)**: Introduces LCWM shared task and LCWM-Bench for language-conditioned world modeling across navigation, robotics, 3D gaming, and driving, plus Tiresias for planning via selective imagination.
- **Key innovations**:
  - LCWM-Bench integrates 15 datasets, 142,987 episodes, 428,961 instructions under shared action/evaluation protocol.
  - Tiresias combines diffusion-policy trajectory proposals, trajectory ranking, video-pretrained world-model imagination, and visual ranking.
  - Separates proposal, imagined consequence, and selection for language-guided planning.
- **Reported results**: Competitive planning and imagination performance on LCWM-Bench; ablations show complementary value of trajectory ranking and visual verification (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.10392) | [PDF](https://arxiv.org/pdf/2611.10392) | [Code](https://github.com/UWMILab/Tiresias)

#### PlayGen2: Learning Real-Time Playable Worlds with Explicit 3D State
- **Authors**: Jihai Zhang, Yuhan Zhou, Junyou Li, Deheng Ye, Qi Dou, Yu Cheng
- **Affiliation**: Not explicitly listed on arXiv abstract page (Deheng Ye is publicly associated with Tencent in related work; multi-institution collaboration implied but must be verified from PDF)
- **Venue / status**: arXiv preprint, 2026-11-05
- **Abstract (summary)**: Builds a real-time playable world model for Doom by separating explicit 3D state evolution from neural rendering, maintaining persistent geometry/entity memory instead of recurrent frame-only state.
- **Key innovations**:
  - Persistent world memory with volumetric occupancy geometry and identity-indexed 3D entity states.
  - Joint learning of action-conditioned dynamics, geometry completion, and entity discovery in local regions.
  - Neural renderer consumes depth/semantic projections without feeding generated images back into state prediction.
- **Reported results**: ~160 ms backend latency on MacBook Pro M4 Pro; demonstrates geometry-aware motion, player–NPC interactions, zero-shot unseen-map deployment, multiplayer composition, and programmable rule-based interventions (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.07867) | [PDF](https://arxiv.org/pdf/2611.07867) | [Code](https://github.com/MajorDavidZhang/PlayGen-2)

#### Fight World Model: Customizable Combat through Visual Interaction Proxies
- **Authors**: Jiahua Li, Zixu John, Tom Zhong, Fuping Wu, Tianhao Xu, Ruicheng Zhang, Jun Zhou, Zunnan Xu
- **Affiliation**: Not explicitly listed on arXiv abstract page
- **Venue / status**: arXiv tech report, 2026-10-29
- **Abstract (summary)**: Separates rule-governed combat execution from video rendering for fighting-game world modeling, using an executable engine and deterministic interaction proxy to preserve hits, health, and action semantics.
- **Key innovations**:
  - Executable combat state/rule engine + renderer separation.
  - Spatially/temporally aligned interaction proxy encoding action windows, hit reactions, and persistent health.
  - FightWorld Corpus: 52 skill effects, 187 character-appearance variants, 15 arenas.
- **Reported results**: Without renderer retraining, supports damage scaling, limited-hit immunity, lifesteal, multi-stage skills, character/arena customization; outperforms existing game world models on action fidelity, hit reactions, health-state consistency, and appearance preservation (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2610.40607) | [PDF](https://arxiv.org/pdf/2610.40607) | [Project](https://fight-world-model.github.io)

#### Wizard: Manipulate Any World in Real Time via Agentic Control
- **Authors**: Yuzhe Wu, Zijun Lin, Yeying Jin
- **Affiliation**: Not explicitly listed on arXiv abstract page
- **Venue / status**: arXiv preprint, 2026-10-29
- **Abstract (summary)**: Proposes an agentic game world model for real-time, precise character control with zero-shot generalization across scenes, characters, and actions, using structured skeleton/geometry proxies.
- **Key innovations**:
  - Dataset spanning 750 scenes and 178 characters with skeleton/geometry structure.
  - Proxy-conditioned video generation with adaptive masking for signal-rollout alignment.
  - Agentic framework maintaining/updating explicit game state for configurable gameplay.
- **Reported results**: Claims real-time controllable, generalizable, and mechanically consistent world simulation (quantitative metrics not fully captured in abstract; verify from PDF).
- **Links**: [arXiv](https://arxiv.org/abs/2610.40339) | [PDF](https://arxiv.org/pdf/2610.40339) | [Project](https://wyzardwu.github.io/wizard)

### 4) Procedural Content Generation (PCG)

#### Procedural Content Metageneration via Program Search and Continual Abstraction Discovery
- **Authors**: Matthew Siper, Ahmed Khalifa, Julian Togelius
- **Affiliation**: Not explicitly listed on arXiv abstract page (Julian Togelius is publicly associated with NYU; verify full affiliations from PDF)
- **Venue / status**: Accepted for publication in IEEE Conference on Games 2026, arXiv 2026-08-18
- **Abstract (summary)**: Evolves complete Python procedural content generators (not just levels) for Sokoban, Zelda, Dangerous Dave, and Lode Runner using LLM mutation/crossover and Continual Abstraction Discovery (CAD).
- **Key innovations**:
  - Program-search/metageneration over executable generators.
  - CAD extracts reusable primitives from high-fitness programs into run-specific helper modules.
  - 2×2 study crossing CAD with fixed hand-written domain API across 160 complete runs.
- **Reported results**: CAD raises mean final best fitness in all eight domain/API comparisons; learned libraries are adopted by most later programs and rediscover validation/reachability/structural utilities.
- **Links**: [arXiv](https://arxiv.org/abs/2608.17947) | [PDF](https://arxiv.org/pdf/2608.17947)

### 5) Game Benchmarks, Datasets, and Evaluation

#### WMEval: Evaluating Interactive World Models Grounded on Physical Simulations
- **Authors**: Lanxiang Hu, Yixin Huang, Abhilash Shankarampeta, Zilin Dai, Yuyuan Wu, Kun Qian, Junze Liu, Arvind Srinivasan, Mingjia Huo, Will Lin, Kai Zhong, Weiqi Zhang, Tian Wang, Qingjun Cui, Tajana Rosing, Hao Zhang
- **Affiliation**: Not explicitly listed on arXiv abstract page (Hao Zhang/Tajana Rosing are publicly associated with UCSD in related contexts; verify affiliations from PDF)
- **Venue / status**: arXiv preprint, v2 2026-10-27
- **Abstract (summary)**: Benchmarks interactive world models against Unity-based physical simulation oracles, moving evaluation beyond perceptual similarity to physical-causal coherence.
- **Key innovations**:
  - Matched action execution in simulator and world model for state-based verification.
  - 9 scenes covering action controllability, consistency, prompt adherence, kinematics, fluid mechanics, causality, and lighting.
  - Combines perceptual and physical-causal evaluation using simulator-derived states.
- **Reported results**: Experiments on SOTA models reveal substantial gaps in dimensions hidden by standard perceptual metrics (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2610.33894) | [PDF](https://arxiv.org/pdf/2610.33894) | [Code](https://github.com/hao-ai-lab/WMEval)

#### Esports World Model Dataset
- **Authors**: Weiyu Ma, Zeyuan Gong, Xuhui Liu, Wenxuan Zhang, Jian Ding, Xinyu Cui, Jian Zhao, Mohamed Elhoseiny
- **Affiliation**: Not explicitly listed on arXiv abstract page (Mohamed Elhoseiny is publicly associated with KAUST; verify full affiliations from PDF)
- **Venue / status**: arXiv preprint, 2026-10-12
- **Abstract (summary)**: Large multi-view esports dataset for world-model research linking individual observations/actions to shared state and events in StarCraft II, Dota 2, and Counter-Strike 2.
- **Key innovations**:
  - 3,053 games/maps and ~4,880 player-view hours; 4,628 completed SC2 views, 10 perspectives for 303 Dota 2 matches, up to 10 views/round in CS2.
  - Replay-clock alignment of rendered video with game-native actions, structured state, and events.
  - Exposes fog-of-war, shared team vision, and first-person observation regimes; SC2 entity records distinguish live vs remembered state.
- **Reported results**: Dataset contribution (no model leaderboard reported in abstract).
- **Links**: [arXiv](https://arxiv.org/abs/2610.16166) | [PDF](https://arxiv.org/pdf/2610.16166)

### 6) Industry / Deployment-Relevant Game AI Systems

#### KlaskTron: An Open-Source Platform for Physical Adversarial Multi-Agent RL
- **Authors**: Aswin Ramachandran, Jona Schulz, Maurus Derungs, Carlo Angelini, Tobias Meier, Raffaello D'Andrea
- **Affiliation**: ETH Zurich ecosystem indicated by project URLs (`idscethzurich.github.io`, `github.com/IDSCETHZurich`); formal author affiliations not fully listed on arXiv abstract page
- **Venue / status**: Proceedings of Robotics: Science and Systems (RSS 2026), arXiv 2026-11-02
- **Abstract (summary)**: Open-source, low-cost (<$2500) desktop robotic testbed for adversarial MARL based on KLASK, with CAD/BOM, NVIDIA Isaac Lab digital twin, and sim-to-real baseline.
- **Key innovations**:
  - Complete reproducible hardware/software/simulation stack for physical competitive MARL.
  - Dual CoreXY gantries with high-speed manipulation for dynamic tabletop play.
  - Learned neural actuator model enabling zero-shot policy transfer.
- **Reported results**: Trained agents exhibit emergent adversarial behaviors with validated sim-to-real baseline (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.03138) | [PDF](https://arxiv.org/pdf/2611.03138) | [Hardware](https://idscethzurich.github.io/klask_hardware) | [Software](https://github.com/IDSCETHZurich/klask_software) | [RL](https://github.com/IDSCETHZurich/klask_rl)

### 7) Related Techniques (self-play, world models, reward/credit, hierarchical RL, diagnostics)

#### Cross-cutting techniques highlighted in this window
- **Selective imagination & verification for planning**: Tiresias ranks proposed trajectories and validates imagined rollouts, combining policy proposals with world-model consequences.
- **Explicit/persistent state over recurrent pixels**: PlayGen2 and Fight World Model separate state/rules from rendering to improve consistency and controllability.
- **Decision-plane and runtime-grounded learning**: RLiD optimizes executable actions directly; WebCatalyst uses runtime action traces and anti-hacking visual anchors for interactive game-like RL.
- **Reward/persona and phase decomposition**: RIDGE blends persona rewards with multi-head critics; Balatro RL decomposes tactical/strategic phases for credit assignment.
- **Policy generation as a learned object**: DPPG diffuses policy parameters conditioned on tasks/environments (Classic Control/Atari/MuJoCo).
- **Closed-loop evaluation rigor**: XiangqiBench and Pac-Man diagnosis emphasize reliability, conversion/consistency gaps, and in-use perception checks over static move accuracy.

## Coverage Notes
- **Requested proceedings coverage**: RSS 2026 (KlaskTron), EXAG 2026/AIIDE workshop (Balatro), IEEE CoG 2026 (RIDGE, CAD) are explicitly identified from arXiv metadata/comments. Broader proceedings (NeurIPS/ICLR/ICML/CVPR etc.) were not systematically crawlable in this run due unavailable web search; future runs should cross-check OpenReview/proceedings pages.
- **Industry coverage**: Tencent involvement is stated for Policy Network Diffusion and suggested by coauthors in PlayGen2/Wizard-related ecosystems but not uniformly structured in arXiv metadata; Microsoft Research Asia association is plausible for WebCatalyst authors but unconfirmed on abstract page. These should be verified from PDFs in a follow-up lint/ingest pass.
- **Potential overlap with other 2026-11-10 wiki digests**: Some AI/agent papers in recent lists (e.g., Parallel Agent Teams 2611.09798) are relevant to general agents but excluded here as not game-specific.

## Sources Consulted
- arXiv API: `all:"game" AND all:"reinforcement learning"` (sorted by submittedDate desc)
- arXiv API: `all:"game agent" AND (all:LLM OR all:"large language model")`
- arXiv API: `all:"world model" AND all:game`
- arXiv API: `all:"procedural content generation"`
- arXiv recent listings: https://arxiv.org/list/cs.AI/recent, https://arxiv.org/list/cs.LG/recent
- Individual abstract pages/PDF links for each featured paper above
