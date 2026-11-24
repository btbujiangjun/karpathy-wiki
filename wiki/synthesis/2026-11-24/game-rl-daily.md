---
title: "Game RL & Game AI Bot — Daily Digest (2026-11-24)"
type: synthesis
created: 2026-11-24
updated: 2026-11-24
sources: []
tags: [game-rl, game-ai, reinforcement-learning, multi-agent-rl, self-play, foundation-models, pcg, benchmarks, world-models, npc, industry-game-ai, vlm, daily-digest]
---

# Game RL & Game AI Bot — Daily Digest (2026-11-24)

- **Date**: 2026-11-24
- **Window**: new papers via arXiv Export API (`export.arxiv.org/api/query`, sorted by `submittedDate`), queries covering the 7 topics + related techniques; window ≈ 2026-11-21 → 2026-11-24; abstracts/authors/dates from Atom feed; venue from arXiv comments where present (most are plain arXiv preprints); all metrics/claims author-reported.

## Executive Summary

New submissions cluster on three themes: (1) **LLM/VLM-powered game agents** — Gamer, GameRealm, AutoPILOT/AFK-Bench, PlayScriptBench, AstronautBench, PlayCraft — plus LLM-in-context adaptivity for imperfect-information games (Leduc Hold'em, NLHE); (2) **classic Game RL expansions** — efficient self-play chess (3.2k Elo), Atari sample-efficiency (Learning to Undo), Mario with PCG level sets (Stack more levels); (3) **PCG advances** — physics-aware PCGRL platformer synthesis, LLM program search (LLM-MetaGen, Craftax goal compilers), a Grover-oracle quantum PCG paper. Industry coverage is thin: no named game-studio papers found; closest is UnityBench-Mini3D (Unity). Full details per topic below.

---

## 1) Game RL — Chess, Atari, RTS, Card Games, Minecraft

### Stack more levels: how to get general and human-like Mario playing (2611.16175v1)
- **Authors**: Shinichi Arimura ; Yuchen Li ; Julian Togelius
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-12)
- **Abstract**: Super Mario Bros. is widely used in game AI and PCG, yet it remains unclear whether a model-free agent can reliably win unseen levels. Training PPO agents on increasingly large sets of PCG-generated levels generally improves unseen-level performance; fine-tuning with Diffusion-Reward Adversarial Imitation Learning (DRAIL) on human gameplay demonstrations raises action-level human-likeness while preserving much of the PPO-induced persona.
- **Key innovations**: PPO on increasing PCG Mario sets for generalization to 1000 held-out levels; three gameplay archetypes (runner/killer/collector) shaped by DRAIL for human-like play.
- **Links**: [arXiv](https://arxiv.org/abs/2611.16175v1)

### Learning to Undo: Transfer Reinforcement Learning under State Space Transformations (2611.23081v1)
- **Authors**: Mridul Mahajan ; Aldo Pacchiano ; Xuezhou Zhang
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-17)
- **Abstract**: Transfer learning in RL: when a target MDP admits an "undo map" that recovers the source's state space, policies transfer with strictly better sample complexity; empirically the method improves sample efficiency on Atari games and continuous control tasks.
- **Key innovations**: Undo-map algorithm learned by matching state feature statistics between source and target; near-linear-Q^* source realization yields provable sample-complexity gains; validated on Atari + continuous control.
- **Links**: [arXiv](https://arxiv.org/abs/2611.23081v1)

### Learning In-Context Adaptivity for LLMs through Continual Gameplay (2611.21710v1)
- **Authors**: Jiale Liu ; Zun Li ; John Schultz
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-16)
- **Abstract**: LLM agents in repeated imperfect-information games: in-context adaptivity (learning opponent tendencies from experience in the context) beats static defaults on some models; post-training Qwen3.5-9B via SFT + trajectory-level RL on an exploitable-opponent pool doubles the 9B experience gain vs SFT in Leduc Hold'em and quintuples it in No-Limit Hold'em, matching or surpassing frontier models across 35 opponents.
- **Key innovations**: Paired protocol isolating experience-gain from single-game skill; memory-doing gap analysis (models record tendencies but rarely change play); RL-on-matched-contexts (full-match return) improves summary + action generation together.
- **Links**: [arXiv](https://arxiv.org/abs/2611.21710v1)

### Learning Martial Arts Motion Skills for Animating Opponents in VR Sparring Games (2611.23825v1)
- **Authors**: Jiqing Wen ; Qixuan Shi ; Robert LiKamWa ; Pavan Turaga
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-18)
- **Abstract**: martial arts motion capture dataset + RL with adversarial style rewards to build a repertoire of motion skills for virtual sparring; adapted via target-directed reward shaping for striking and evasion; evaluated via user study (physical plausibility, smoothness, form) and deployed in a Meta Quest VR sparring prototype.
- **Key innovations**: RL pretraining of martial arts skill repertoire from Mocap + adversarial style rewards; task-specific adaptation (striking/evasion); interactive VR opponent prototype combining policy clips with state-based control.
- **Links**: [arXiv](https://arxiv.org/abs/2611.23825v1)

### Single-shot holographic gradients for training wavefronts through disorder (2611.27439v1)
- **Authors**: Kerem Ekec ; Bahadır Utku Kesgin ; Uğur Teğin
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-20)
- **Abstract**: Optical systems in situ: one off-axis hologram measures the training error (holographic gradient); a compact adjoint refreshes a trained program every ~seconds; focuses light through thin diffusers; "the reference beam becomes a computing layer that plays a video game".
- **Key innovations**: Real-time optical training via holographic gradients (camera intensity → gradient); adjoint network refresh during training; demonstrates self-correcting processors and playing a game as a byproduct.
- **Links**: [arXiv](https://arxiv.org/abs/2611.27439v1)

---

## 2) Game AI Bot — LLM/VLM Game Agents, NPC Intelligence, Bot Frameworks

### AutoPILOT: A Visual Agent Harness for Real-Time Gameplay (2611.28202v1)
- **Authors**: Mark Zhao ; Pengcheng Wang ; Rui Yang ; Jiarui Yao ; Xirui Jiang ; Yuxi Chen ; Bingxuan Li ; Hanyang Chen ; Ke Yang ; Manling Li ; Tong Zhang ; Huan Zhang
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-20)
- **Abstract**: Existing harnesses turn each model call into ≤1 action, so the agent acts only as often as the model thinks. AutoPILOT changes this: per model call the model can send a primitive, start an open-loop macro, or write a closed-loop controller that keeps playing from the screen without further calls until it hands control back. Evaluated in AFK-Bench: 120 browser games grouped by how they respond to inaction.
- **Key innovations**: Three-level control interface (primitive / open-loop macro / closed-loop controller with handback); AFK-Bench (120 diverse real-time/clock-paused browser games); gains over VISTA: +30.3 pts real-time, +35.1 pts GameWorld, while cutting API cost to ~1/5 of VISTA.
- **Links**: [arXiv](https://arxiv.org/abs/2611.28202v1)

### PlayScriptBench: Can Vision-Language Models Synthesize Executable Game-Playing Programs? (2611.27741v1)
- **Authors**: Yao Tong ; Jiaxin Qi ; Dingyu Zhang ; Jianqiang Huang
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-20)
- **Abstract**: Instead of step-by-step interaction, evaluate whether VLMs can synthesize an executable game-playing program from game states — jointly grounding visuals, dynamics, strategic planning, and executable control; on 16 games (4 genres) strong VLMs still fail, exposing a gap between passive visual game understanding and executable closed-loop control; 4-stage pipeline: Explore → Perception → API Construction → Strategy Composition.
- **Key innovations**: Script-based VLM game-agent benchmark (PlayScriptBench); decomposition into four stages to ease program synthesis for VLMs.
- **Links**: [arXiv](https://arxiv.org/abs/2611.27741v1)

### AstronautBench: Measuring Agent Self-Improvement Across Episodes Through Knowledge, Evidence, and Progress (2611.26910v1)
- **Authors**: Congyuan Yu ; Runping Tian
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-19)
- **Abstract**: Benchmark on the game Outer Wilds: agents run 22-minute episode loops; only knowledge persists across episodes; measures knowledge correctness, evidence support, and progress (places reached, rumor facts). Found the GPT-6.1 Sol agent's correct answers grow 14.6% → 26.8% but evidence support stays low; no new rumor facts after episode 3.
- **Key innovations**: Three views (knowledge / evidence / progress) on one run; LLM judges; shows self-improvement is not always self-evident; offers a stricter self-improvement yardstick for embodied agents.
- **Links**: [arXiv](https://arxiv.org/abs/2611.26910v1)

### PlayCraft: Designing Engaging Games from Agent Play Experience (2611.26624v1)
- **Authors**: Weihao Cheng
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-19)
- **Abstract**: Coding agents generate playable games but may be unengaging (mastery is a key engagement driver). PlayCraft alternates playing and crafting: a player agent watches and reports its progress, and a crafter agent uses reports to estimate player ability, predict performance per proficiency, and revise the game for mastery. Evaluated on games in fresh runs with player agents across three intelligence settings.
- **Key innovations**: Agent-play experience as input to automatic game-design revisions for mastery; learning-gain and learning-slope metrics per setting.
- **Links**: [arXiv](https://arxiv.org/abs/2611.26624v1)

### When Agents Play Differently: Localizing Human–Agent Behavioral Divergence with Conditional Distributional Testing (2611.26012v1)
- **Authors**: Oleg Smirnov ; John Pertoft ; Sara Karimi
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-19)
- **Abstract**: Commercial match-3 game: measures nonparametric discrepancies between human and agent behavioral distributions within contextual cells and identifies subgroup rules where they diverge; finds process-level move-efficiency divergence invisible to win-rate means.
- **Key innovations**: Stratified distributional divergence framework for human-vs-agent behavior localization; open-source implementation for reproducibility.
- **Links**: [arXiv](https://arxiv.org/abs/2611.26012v1)

---

## 3) Game Foundation Models — Generalist Game Models & VLA Agents

### Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent (2611.18397v3)
- **Authors**: Run Luo ; Kuan Zhang ; Qi Deng ; Yukun Chen ; Zhihao Yang ; Yufei Zhang ; Renrong Hu ; Yi Zhang ; Guiyu Ma ; Tianyu Fan ; Longze Chen ; Hao Sun ; Jiaming Li ; Jiaming Yang ; Xiaohao Liu ; Tao Tan ; Minzheng Wang ; Hangtian Jia ; Shuai Yuan ; Lvdi Wang ; Xiao Liu ; Chao Ma ; Yuting Zou ; Yinhe Zheng ; Xiaobo Xia ; Dawei Jiang ; Shaoqing Ren
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-13)
- **Abstract**: Gamer: end-to-end VLA framework for long-horizon tasks in interactive environments; continues pre-training on tens of thousands of hours of device-level keyboard/mouse trajectories over simulated games and embodied environments; sparse-thinking instruction tuning; stable multi-turn RL for long horizons (finite-context, rollout error, sparse rewards); cloud-edge inference for low-latency serving; solid generalization in 3D open-world games and 2D benchmarks.
- **Key innovations**: Cross-domain (digital + physical) pre-training on interaction trajectories (v2: up to 27B); sparse-thinking instruction tuning; real-time cloud-edge serving engine (unbounded context); scaling data+algorithms into generalist agents.
- **Links**: [arXiv](https://arxiv.org/abs/2611.18397v3)

### GameRealm: Grounding Visual Learning in Interactive Games (2611.23140v1)
- **Authors**: Weiguang Zhao ; Yifan Wang ; Ni Yang ; Yating Wang ; Xingyu Miao ; Yankai Jiang ; Mulin Yu ; Tao Lu ; Haoyu Guo ; Junting Dong ; Weinan Zhang ; Chunhua Shen
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-17)
- **Abstract**: Large-scale dataset grounding visual observations in synchronized game-native supervision: 120M RGB frames / 1,000 h of gameplay across views, with metric depth, camera parameters, synchronized audio, control inputs, and 3D point trajectories; flexible view configurations; built via a unified human+agentic data collection pipeline.
- **Key innovations**: 120M-frame interactive game dataset with depth/camera/audio/action/trajectory supervision; improves visual foundation models in generation + geometric learning (GameRealm-Bench).
- **Links**: [arXiv](https://arxiv.org/abs/2611.23140v1)

### From Game Generation to Game Playing: Fully Automated Ability Training for Vision-Language-Action Models (2611.11136v2)
- **Authors**: Changran Liu ; Qi Wu ; Wenchao Ma ; Sharon X. Huang ; Haomiao Jiang
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-08)
- **Abstract**: Automatic generation of executable environments + expert demos: an LLM-powered agent builds environments/tasks; programmatic experts generate aligned instructions, rendered observations, keyboard/mouse actions; trains Script2Play via behavior cloning on 150.3 h of synthetic gameplay in Minecraft and Roblox; generalizes across game engines on public game benchmarks.
- **Key innovations**: LLM-driven environment + task generation with privileged simulator state for aligned instruction/action supervision; targeted synthetic supervision for VLA ability training.
- **Links**: [arXiv](https://arxiv.org/abs/2611.11136v2)

---

## 4) Procedural Content Generation — RL for Levels, LLM for Content

### PCGRL for Complex Platformers: Synthesizing Playable and Diverse Levels via Inflated Envelopes and Forward Curricula (2611.22250v1)
- **Authors**: Di Wu
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-17)
- **Abstract**: Physics-aware, curriculum-guided PCGRL for platformers: "inflated volume envelope" adds physics-feasible kinematics to the MDP; multi-stage forward extension curriculum with intermediate feedback stabilizes credit assignment over long horizons; high-entropy stochastic inference + post-hoc rejection filtering restores level diversity without sacrificing playability on multi-scale canvases.
- **Key innovations**: InflatedVolumeEnvelope state representation; forward-curriculum PCGRL; diversity via stochastic inference + parallel rejection filtering.
- **Links**: [arXiv](https://arxiv.org/abs/2611.22250v1)

### Procedural Content Metageneration via Program Search and Continual Abstraction Discovery (2610.10593v1)
- **Authors**: Matthew Siper ; Ahmed Khalifa ; Julian Togelius
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-08-18)
- **Abstract**: LLMs generate executable programs; search is done over generators by mutation/crossover; CAD (Continual Abstraction Discovery) extracts reusable primitives into run-specific helper modules; 2×2 experiment crosses CAD with a hand-written domain API in Sokoban, Zelda, Dangerous Dave, Lode Runner; CAD improves mean final best fitness across all 8 comparisons.
- **Key innovations**: Program-search PCG (LLM mutation + crossover); Continual Abstraction Discovery for reusable primitives.
- **Links**: [arXiv](https://arxiv.org/abs/2610.10593v1)

### Continuation-Guided LLM Evolution of Program Policies and Goal Compilers in Craftax (2611.19537v1)
- **Authors**: Víctor Gallego
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-14)
- **Abstract**: Coding-agent-synthesized program policies for the Craftax PCG game: refinement via a feedback cascade (episode → hierarchical goals → belief updates, densely scored by simulator); then factoring the controller into an environment interpreter + rule program; coding agents optimize a reusable goal compiler C_θ mapping structured tasks to rule programs, transferring zero-shot to longer tasks without LLM calls; reaches the final stage ~50% of runs.
- **Key innovations**: Feedback-cascade refinement from sparse episode returns to dense hierarchical-goal signals; reusable goal compilers (LLM-optimized) that turn new tasks into rule programs without inference-time LLMs.
- **Links**: [arXiv](https://arxiv.org/abs/2611.19537v1) | [GitHub](https://github.com/vicgalle/craftax-program-policies)

### The Cost of a Real Grover Oracle: Minecraft Seed Search from Software to Quantum Hardware (2610.33139v1)
- **Authors**: Evan M. Reeves ; Elias Sopkin ; Thomas A. Searles
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-10-23)
- **Abstract**: Resource estimates for Grover oracles for Minecraft 1.13.1 seed recovery (structure-placement predicate + LCG inverse); Fourier-basis constant arithmetic reduces width/gate counts; results verified against Java reference and hardware-executed on IBM and Quantinuum H2-1; alternative construction: 275 qubits/48,896 CX vs 467/2,038,804.
- **Key innovations**: Quantum-search application to MCGPCG; arithmetic specialization quantified; routing sensitivity shown on real hardware.
- **Links**: [arXiv](https://arxiv.org/abs/2610.33139v1)

---

## 5) Game Benchmarks — New Game-Based Evaluation Suites

### AutoPILOT: A Visual Agent Harness for Real-Time Gameplay (2611.28202v1)
- See §2 — includes AFK-Bench: 120 diverse browser games, real-time + paused-clock groups.

### PlayScriptBench (2611.27741v1)
- See §2 — VLM script synthesis benchmark across 16 games / 4 genres.

### AstronautBench (2611.26910v1)
- See §2 — Outer Wilds self-improvement benchmark with 3 views (knowledge/evidence/progress).

### MANGO Arena: Same Seeds, Different Chains Evaluating LLM Agents in a Disrupted Supply Chain (2611.23613v1)
- **Authors**: Sara Amar
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-17)
- **Abstract**: Open testbed: 4 LLM agents each run one company in a serial supply chain (MANGO, a classroom factory-management game); hard rules enforced (truck limit, no-credit cash, capacity); logs blocked attempts; public message board forbids side payments; measures bullwhip effect, rule adherence, and collusion proposals; observed demand amplification ×7–25 (retailer) / ×13–179 (supplier).
- **Key innovations**: Simultaneous economic + rule-adherence + collusion measurements in one game; reporting practices for multi-agent evals (same seeds → up to ×17 variation without failed calls).
- **Links**: [arXiv](https://arxiv.org/abs/2611.23613v1)

---

## 6) Industry Game AI

- No papers from named game studios (EA/Ubisoft/Naughty Dog/Riot/Blizzard/Valve, etc.) were returned by the queried keywords ("game AI", reinforcement, studio names + "game development"). Newer studio-game implementations appear mostly as coding-agent benchmarks:

### UnityBench-Mini3D: Evaluating LLM Agents for 3D Game Development in Unity (2610.35980v1)
- **Authors**: Yijun Zhou ; Minghao Shao ; Ke Zhang ; Renkai Yuan ; Hongbo Yuan ; Bin Hu ; Bo Zhao Qian ; Hongxia Shen ; Yanhong Liu ; Yuting Chen ; Yuntao Shi ; Zhongxuan Xu ; Shuo Mao ; Haijia Zhou ; Zhendong Li ; Tao Zhang ; Chenggang Li ; Yuxuan Wang ; Zinan Zheng ; Calvin Zhang ; Jia Li ; Heng Chang ; Jie Feng
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-10-26)
- **Abstract**: Benchmark of 77 Unity project tasks over 7 skill categories + 3 tiers (Unity Skill Categories + difficulty); paired with 1,178 held-out human-authored milestone tests covering scene structure, component config, runtime behavior; in-engine evaluation, deterministic partial credit.
- **Key innovations**: Unity-specific coding-agent benchmark with executable milestone tests (vs coarser LLM-judge benchmarks); performance: 80.9% easy / 35.2% hard / 57.7% overall across 21 models × 9 harnesses.
- **Links**: [arXiv](https://arxiv.org/abs/2610.35980v1)

---

## 7) Related Techniques — Self-Play, Curiosity, World Models, Imitation/IRL in Games

### Learning to Undo (2611.23081v1) — see §1
### Learning In-Context Adaptivity for LLMs through Continual Gameplay (2611.21710v1) — see §1 (poker self-play + in-context adaptivity)
### When Agents Play Differently: Localizing Human–Agent Behavioral Divergence with Conditional Distributional Testing (2611.26012v1) — see §2 (match-3 human-agent divergence)

### Curiosity-Driven Exploration / World Models for Games
- **NOTE (honest gap)**: No standalone "curiosity-driven exploration" or "world-model for games" arXiv papers were surfaced by the queried searches this window; related world-model work appears as data (GameRealm), benchmarks (WMEval — evaluation of interactive world models on physical simulations; see 2026-11-23 digest), and decision-model systems (Piccolo, 2026-11-18). Recommended follow-up searches: `curiosity` + `game`, `world model` + `game`.

### Other Related (cross-topic)
- **Piccolo: Co-Evolving Decision Models and Data through Recursive Self-Improvement** (2611.24651v1, 2026-11-18) — multimodal decision models (0.8B–27B) trained on games + other tasks via agentic data engineering + RSI.

---

*Method note: discovery via arXiv Export API sorted by submittedDate with ~12 topic queries per run (game RL: Atari/StarCraft/Dota/Go/chess/poker/Minecraft/NetHack; LLM/NPC agents; foundation models; procedural content generation; benchmarks; industry names; self-play/curiosity/hierarchical RL); window ~2026-11-21 → 2026-11-24; deduped vs the whole-wiki ID baseline (grep `wiki/synthesis/**`); abstracts/authors/dates from the Atom feed; affiliations from arXiv metadata (many papers do not state affiliations on arXiv — flagged "Not stated"); all metrics/claims author-reported; journal venues not identifiable for most preprints. Validated with quick spot-checks of paper titles/IDs via arXiv pages.*
