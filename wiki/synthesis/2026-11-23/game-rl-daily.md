# Game RL & Game AI Bot — Daily Digest (2026-11-23)

- **Date**: 2026-11-23
- **Window**: new papers, ID-level dedupe vs whole-wiki baseline (grep `wiki/synthesis/**`, ~10.8k arXiv IDs); arXiv Export API (`export.arxiv.org/api/query`, sorted by `submittedDate`), window 2026-11-09 → 2026-11-23 (today); affiliations from PDF page-1 (pypdf); abstracts/authors/dates from Atom feed; all metrics/claims author-reported.
- **Scope**: Game RL (chess, Atari, RTS, card games like GuanDan, AAA games); multi-agent RL in games, self-play/PB/open-ended learning; LLM/VLM-powered game agents, NPC intelligence, game bot frameworks, autonomous gameplay; game foundation models & game-playing world models; PCG (level generation, enemy morphology, automated game design); game benchmarks (script-based controller synthesis, LLM game arenas, MARL benchmarks); industry game AI (Fayn-class); related techniques (curiosity-driven exploration, world models, imitation/IRL, reward shaping, model-based/offline RL, opponent shaping, game-theory learning).

## Executive Summary

32 papers this window; strongest signals: LLM/VLM-powered game agents and game-native benchmarks — PlayScriptBench (VLM script synthesis), WorldAuditBench (UE5/Three.js world auditing), Gamer, GameRealm, HiSTEVE 1.0 — plus deeper Game RL in chess (Engineering Efficient Self-Play Chess), RTS (MicroRTS command-conditioned RL) and card games (GuanDan self-play gap); PCG expands into LLM-written content (Weight-Space Programming on Unseen Games) and morphological generation. Note: the EA SPORTS FC 25 Goalkeeping paper (arXiv 2610.23216v4, 2026-10-27) was not recovered from result sets this window; it appears covered in earlier digests — excluded as not newly verified this cycle.

---

## 1) Game RL — Chess, Atari, RTS, Card Games

### Engineering Efficient Self-Play Chess: Search, Replay, and Throughput Under Limited Compute (2609.37447v1)
- **Title (EN)**: Engineering Efficient Self-Play Chess: Search, Replay, and Throughput Under Limited Compute
- **Authors**: Bertil Braun
- **Affiliation**: Not stated on arXiv PDF p.1
- **Venue/conference**: arXiv preprint (26 pages, 17 figures, including appendices; code & evidence: github.com/BertilBraun/Advanced-Techniques-in-Chess-Engi…)
- **Date**: 2026-09-27
- **Abstract**: How strong can an AlphaZero-style chess system become under limited training compute when its entire learning loop is engineered for efficiency? We train from random initialization through searched self-play on a single eight-GPU node for 2.5 days; the 6.32M-param model reaches 3,251 benchmark Elo (3,206–3,297) at 100,000 searches/move (estimated <5 s thinking) vs a fixed-node Stockfish 13 ladder. The run ingests 3.25M games (~100B search simulations, 836.6M training presentations). We investigate search allocation, replay & restart-state selection, policy representation, progressive model sizing, quantized inference, and throughput engineering.
- **Key innovations**: AlphaZero-style self-play on one 8-GPU node in 2.5 days → 6.32M-param model at 3,251 Elo with 100k searches/move (<5 s thinking); 3.25M games / ~100B sims / 836.6M presentations; engineering: search allocation, replay/restart-state selection, policy representation, progressive sizing, quantized inference.
- **Links**: [arXiv](https://arxiv.org/abs/2609.37447v1) | [PDF](https://arxiv.org/pdf/2609.37447v1)

### Constrained Command-Conditioned Reinforcement Learning with Bandit Strategy Selection in Real-Time Strategy Games (2610.11663v1)
- **Title (EN)**: Constrained Command-Conditioned Reinforcement Learning with Bandit Strategy Selection in Real-Time Strategy Games
- **Authors**: Nick Leenders ; Roy Lindelauf ; Joost van Oijen ; Boris Cule
- **Affiliation**: Tilburg University — Data Science Center of Excellence / Department of Intelligent Systems (PDF page-1)
- **Venue/conference**: arXiv preprint
- **Date**: 2026-10-08
- **Abstract**: Deep RL agents reach strong performance in real-time strategy games but can be brittle against opponents outside their training distribution. Separating strategic command selection from learned unit control lets different strategies adapt per opponent while reusing the same execution policy. We introduce a constrained command-conditioned Proximal Policy Optimization (PPO) policy, the executor, for MicroRTS: discrete commands specify strategic objectives and behavioral requirements for economy, army composition, military posture and worker policy over multiple env steps; the executor determines unit-level actions. A Thompson-sampling bandit acts as the strategist, selecting command tuples from an opponent-strategy estimate built from in-game observations (not opponent identity). In a controlled comparison with a flat PPO baseline, the strategist-executor system wins significantly more often vs the three strongest opponents on a training map.
- **Key innovations**: Command-conditioned PPO executor on MicroRTS (commands = strategies + economy/army/posture objectives; executor = unit actions); Thompson-sampling bandit strategist estimating opponent strategy from observations; wins vs top opponents vs flat PPO.
- **Links**: [arXiv](https://arxiv.org/abs/2610.11663v1) | [PDF](https://arxiv.org/pdf/2610.11663v1)

### The Predictive–Optimization Gap in GuanDan Self-Play (2610.29411v1)
- **Title (EN)**: The Predictive–Optimization Gap in GuanDan Self-Play
- **Authors**: Qicheng Zou ; Biao Yuan ; Siyu Song ; Wentao Liu ; Xiaokun Wang
- **Affiliation**: University of California, San Diego (Q. Zou et al.) — PDF-verified statement
- **Venue/conference**: arXiv preprint (cs.LG, stat.ML)
- **Date**: 2026-10-21
- **Abstract**: Outcome-predictive signals are often treated as promising optimization targets in RL, but predictive validity and optimization utility are different claims. We expose this distinction in GuanDan, a multi-round imperfect-information game where the implication of a round outcome depends on the public match state. Held-out analysis shows state–gain interactions provide incremental predictive value beyond a constant signed-gain effect. Using changes in a frozen match-win predictor (ΔΦ) as a controlled supervision signal in a matched DanZero-style self-play protocol: a selected progress-augmented checkpoint substantially outperforms its matched baseline on a locked evaluation, but method-level results reverse this across seeds — none of five preregistered replication seeds is positive, and effects change sign without a common late-stage advantage.
- **Key innovations**: Identifies the predictive–optimization gap in GuanDan: ΔΦ describes real match progress but provides unreliable optimization direction under self-play (sign-changing across seeds; positive only by chance in selected lineages).
- **Links**: [arXiv](https://arxiv.org/abs/2610.29411v1) | [PDF](https://arxiv.org/pdf/2610.29411v1)

### GTAGym: AAA Game Tasks Environment for Evaluation and Reinforcement Learning (2611.13028v2)
- **Title (EN)**: GTAGym: AAA Game Tasks Environment for Evaluation and Reinforcement Learning
- **Authors**: Jiajun Chen ; Shicheng Fang ; Jiahao Lu ; Yuxin Wang ; Xipeng Qiu
- **Affiliation**: Shanghai Innovation Institute ; Fudan University (PDF page-1)
- **Venue/conference**: arXiv preprint (cs.CV, cs.AI, cs.CL)
- **Date**: 2026-11-09
- **Abstract**: AAA games offer a rich testbed for evaluating agent perception, reasoning, and control, but task outcomes are hard to verify automatically. We introduce GTAGym, an environment and framework for evaluation and RL on GTA V tasks. Its benchmark, GTAVBench, reconstructed from GTA V main-story missions, has 103 online tasks across nine task families, plus 47 image-based shooting/sniping tasks from GTA V imagery.
- **Key innovations**: GTAVBench — 103 reconstructed main-story mission tasks (9 families) + 47 shooting/sniping image tasks; RL evaluation framework for GTA V.
- **Links**: [arXiv](https://arxiv.org/abs/2611.13028v2) | [PDF](https://arxiv.org/pdf/2611.13028v2)

---

## 2) Game AI Bot — LLM/VLM Agents, NPC Intelligence, Bot Frameworks

### Can Vision-Language Models Synthesize Executable Game-Playing Programs? (2611.27741v1)
- **Title (EN)**: Can Vision-Language Models Synthesize Executable Game-Playing Programs?
- **Authors**: Yao Tong ; Jiaxin Qi ; Dingyu Zhang ; Jianqiang Huang
- **Affiliation**: Hangzhou Institute for Advanced Study, University of Chinese Academy of Sciences (Computer Network Information Center) — PDF page-1
- **Venue/conference**: arXiv preprint (21 pages, 3 figures, 13 tables)
- **Date**: 2026-11-20
- **Abstract**: VLMs have endowed multimodal agents with strong visual perception and long-horizon reasoning, making VLM-based autonomous game playing feasible. Existing game benchmarks evaluate step-by-step interaction; instead we propose PlayScriptBench, a script-based game benchmark that evaluates whether VLMs can synthesize an executable game-playing program from game states. Experiments on 16 games across 4 genres show that strong VLMs struggle on this benchmark, revealing a gap between passive visual game understanding and executable closed-loop game control.
- **Key innovations**: PlayScriptBench — evaluates VLM script synthesis (visual grounding, dynamics understanding, strategic planning, executable control) instead of step-by-step interaction; 4-stage pipeline (Explore → Perception → API Construction → Strategy Composition).
- **Links**: [arXiv](https://arxiv.org/abs/2611.27741v1) | [PDF](https://arxiv.org/pdf/2611.27741v1)

### Efficient Multimodal Agents for Auditing 3D Worlds (2611.25543v1)
- **Title (EN)**: Efficient Multimodal Agents for Auditing 3D Worlds
- **Authors**: Jingbo Yang ; Ziyan Jiang ; Li An ; Jiabao Ji ; Yujian Liu ; Tommi Jaakkola ; Yang Zhang ; Shiyu Chang …
- **Affiliation**: Not stated on PDF p.1
- **Venue/conference**: arXiv preprint
- **Date**: 2026-11-19
- **Abstract**: Multimodal agents can now build interactive 3D worlds and games, yet glitches remain (floating objects, walkable walls, objects changing with no observer). An automatic auditor must navigate to glitch candidates, trigger invisible glitches, and recognize what is wrong. Current auditors are accurate-but-slow or cheap-but-unreliable. WorldAuditBench is built from 213 tasks on Unreal Engine 5 and Three.js worlds; the auditor is a swarm of small explorers (navigate + trigger) reviewed by a frontier model; it succeeds on 55.9% of tasks, 13.6 points above the strongest auditor at ~4× lower cost, and matches frontier exploration at 4.6× lower cost.
- **Key innovations**: WorldAuditBench (213 UE5/Three.js audit tasks); auditor architecture: swarm of small explorers + frontier-model reviewer; 55.9% success, >4× cost reduction vs best auditor.
- **Links**: [arXiv](https://arxiv.org/abs/2611.25543v1) | [PDF](https://arxiv.org/pdf/2611.25543v1)

### Recurrent Vision Language Models Solve the Shell Game (2611.25210v1)
- **Title (EN)**: Recurrent Vision Language Models Solve the Shell Game
- **Authors**: Dingqiang Ye ; Jiacong Xu ; Wen Zhang ; Yiqun Mei ; Vishal M. Patel
- **Affiliation**: Johns Hopkins University
- **Venue/conference**: arXiv preprint
- **Date**: 2026-11-18
- **Abstract**: Tracking a hidden object through a video is effortless for humans but a bottleneck for VLMs. In the shell game (ball under one of several swapped cups), VLMs answering directly stay near chance. RecurrentVLM makes every attention layer of a pretrained VLM recur over finished frame groups by computing layer K/V from its own output; with a single answer token it reaches 100% on VET-Bench and 99.6% on MET-Bench, and 99% on 50-swap games after training on at most 30 swaps.
- **Key innovations**: RecurrentVLM — serial-computation state tracking in VLMs; solves shell-game tracking; length generalization; generalizes to 50-swap games.
- **Links**: [arXiv](https://arxiv.org/abs/2611.25210v1) | [PDF](https://arxiv.org/pdf/2611.25210v1)

### Acting by Intent, Reacting by Sight: Visual Conditioned Reflexes for Real-Time VLM Agents (2611.18723v1)
- **Title (EN)**: Acting by Intent, Reacting by Sight: Visual Conditioned Reflexes for Real-Time VLM Agents
- **Authors**: Qiancheng Zhou ; Wenhua Zhang
- **Affiliation**: Not stated on PDF p.1
- **Venue/conference**: arXiv preprint
- **Date**: 2026-11-09
- **Abstract**: VLMs are generalist agents that perceive, reason and act — but real-time video games demand deliberate control for exploration AND split-second reactions to fast hazards; relying solely on direct VLM actions is too slow, while scripting is blind at action time. We pair normal conscious control with conditioned reflexes (visual-conditioned, reactive), a dedicated reflex architecture for real-time VLM game agents.
- **Key innovations**: Visual-conditioned reflex architecture for real-time VLM agents (conscious control + split-second reflexes).
- **Links**: [arXiv](https://arxiv.org/abs/2611.18723v1) | [PDF](https://arxiv.org/pdf/2611.18723v1)

### Compiling Known Rules into Compact Neural Agents: Weight-Space Programming on Unseen Games (2611.16981v1)
- **Title (EN)**: Compiling Known Rules into Compact Neural Agents: Weight-Space Programming on Unseen Games
- **Authors**: Jens Lehmann
- **Affiliation**: Amazon, TU Dresden (PDF page-1; work done outside Amazon)
- **Venue/conference**: arXiv preprint (32 pages, 4 figures. Code: github.com/JensLehmann/weight-space-programming-games)
- **Date**: 2026-11-12
- **Abstract**: Weight-space programming (WSP) uses language models to construct neural network weights without training. We test whether known game mechanics can be compiled into compact agents that generalize to held-out levels, renderings and start states within a game family. Writers receive simulator source with held-out level data removed for 20 privately authored, unpublished ARC-AGI-3-style game families. With a fixed 57k-parameter recurrent architecture, the strongest writer reaches 56% held-out-level success with feedback; the four main writers' Python players reach 97–100%. An exploratory free-architecture condition reaches even higher.
- **Key innovations**: WSP — LMs write game-family network weights directly; 57k-param recurrent agents; strongest writer 56% held-out vs Python players 97–100%; free-architecture exploratory condition.
- **Links**: [arXiv](https://arxiv.org/abs/2611.16981v1) | [PDF](https://arxiv.org/pdf/2611.16981v1)

---

## 3) Game Foundation Models / Game-Playing World Models

### Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent (2611.18397v3)
- **Title (EN)**: Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent
- **Authors**: Run Luo ; Kuan Zhang ; Qi Deng ; Yukun Chen ; Zhihao Yang ; Yufei Zhang ; Renrong Hu ; Yi Zhang ; Guiyu Ma ; Tianyu Fan ; … (27 authors)
- **Affiliation**: Not stated on arXiv metadata
- **Venue/conference**: arXiv preprint (cs.CL, cs.AI, cs.CV)
- **Date**: 2026-11-13
- **Abstract**: Gamer — generalist agent framework for long-horizon tasks in complex interactive environments. End-to-end architecture: perception, memory management, multi-step reasoning. Shared training & deployment pipeline for conventional 2D interfaces and complex 3D simulated worlds. Pre-training on a dataset from tens of thousands of hours of device-level keyboard/mouse interaction (simulated games + embodied environments; learns environmental dynamics). Sparse-thinking instruction tuning reduces redundant computation while preserving complex-decision reasoning. Stable multi-turn RL method for long-horizon interaction (finite context windows, accumulated rollout errors, sparse rewards). Cloud-edge inference engine serving simulated environments concurrently with low online latency; across multiple challenging 3D open-world games it matches skilled players in generalization & operational efficiency; competitive on conventional 2D game benchmarks.
- **Key innovations**: Generalist VLA foundation model for games — tens of thousands of hours of KBM pre-training on games + embodied trajectories; sparse-thinking instruction tuning; stable multi-turn RL for long horizons; cloud-edge real-time serving engine.
- **Links**: [arXiv](https://arxiv.org/abs/2611.18397v3) | [PDF](https://arxiv.org/pdf/2611.18397v3)

### GameRealm: Grounding Visual Learning in Interactive Games (2611.23140v1)
- **Title (EN)**: GameRealm: Grounding Visual Learning in Interactive Games
- **Authors**: Weiguang Zhao ; Yifan Wang ; Ni Yang ; Yating Wang ; Xingyu Miao ; Yankai Jiang ; Mulin Yu ; Tao Lu ; Haoyu Guo ; Junting Dong ; Weinan Zhang ; Chunhua Shen
- **Affiliation**: Shanghai Artificial Intelligence Laboratory ; Shanghai Jiao Tong University ; Zhejiang University (PDF page-1)
- **Venue/conference**: arXiv preprint (cs.CV)
- **Date**: 2026-11-17
- **Abstract**: GameRealm — large-scale, richly annotated dataset that grounds visual observations in synchronized, game-native supervision. >120 million RGB frames, 1,000 hours of gameplay across all views. Rich multimodal supervision: metric depth, camera parameters, synchronized audio, control inputs, and 3D point trajectories. Flexible view configurations (single-view, stereo, multi-view, panoramic). Unified data-collection pipeline (human-operated interaction + agentic exploration). Extensive experiments: strengthens VFMs in both visual generation and geometric learning.
- **Key innovations**: GameRealm — >120M RGB frames, 1,000h gameplay, game-native supervision (depth, camera, audio, controls, 3D points); unified human + agentic data pipeline; strengthens visual foundation models in generation AND geometric learning.
- **Links**: [arXiv](https://arxiv.org/abs/2611.23140v1) | [PDF](https://arxiv.org/pdf/2611.23140v1)

### HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games (2610.31162v1)
- **Title (EN)**: HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games
- **Authors**: Zecong Tang ; Zian Guan ; Yuncheng Guo ; Zhanqiu Zhang ; Yiwen Guo ; Bo Dai
- **Affiliation**: The University of Hong Kong ; Zhejiang University ; Fudan University ; LIGHTSPEED ; Independent Researcher (PDF page-1)
- **Venue/conference**: arXiv preprint (cs.CV)
- **Date**: 2026-10-22
- **Abstract**: Building virtual embodied agents that operate in open-ended games like human players is a long-standing goal; Minecraft provides a natural testbed (procedurally generated open world). Existing agents offer either native visuomotor control (no long-horizon autonomy) or high-level planning via APIs/skills (no native control). HiSTEVE — hierarchical VLA agent with a capability-aware harness: orchestration uses structured memory for progress tracking + a VLM planner for subtask selection within the VLA's capabilities; a policy-coupled task-completion state detector signals candidate completion. Control: single VLA with vision-only perception and native KBM actions. Trained via world-knowledge injection, imitation learning, and RL with environment feedback; improves reliability and recovery. Achieves 85.0% atomic-task performance on MineStudio Bench and 37.4% average success on OpenHA; completes long-horizon tasks (crafting an iron pickaxe from scratch).
- **Key innovations**: Hierarchical VLA agent for open-world games (orchestration: memory + VLM planner; control: single VLA); VLA+VLM planning + completion detector; RLM + imitation training; 85.0% atomic-task on MineStudio Bench.
- **Links**: [arXiv](https://arxiv.org/abs/2610.31162v1) | [PDF](https://arxiv.org/pdf/2610.31162v1)

---

## 4) Procedural Content Generation

### Stack more levels: how to get general and human-like Mario playing (2611.16175v1)
- **Title (EN)**: Stack more levels: how to get general and human-like Mario playing
- **Authors**: Shinichi Arimura ; Yuchen Li ; Julian Togelius
- **Affiliation**: New York University
- **Venue/conference**: arXiv preprint
- **Date**: 2026-11-12
- **Abstract**: Super Mario Bros. is widely used in game AI and PCG, yet it's unclear whether a model-free agent can reliably win unseen levels. We train Proximal Policy Optimization (PPO) agents on increasingly large sets of PCG-generated Mario levels and evaluate generalization on 1,000 held-out test levels. We then shape competent PPO policies into three gameplay archetypes — runner, killer, and collector — and fine-tune them with Diffusion-Reward Adversarial Imitation Learning (DRAIL) using human gameplay demonstrations. More PCG levels generally improve unseen-level performance; DRAIL increases action-level human-likeness while preserving much of the PPO-induced persona.
- **Key innovations**: PPO generalization on PCG Mario levels (1,000 held-out); 3 gameplay archetypes via reward shaping; DRAIL human-demo fine-tuning → human-like actions.
- **Links**: [arXiv](https://arxiv.org/abs/2611.16175v1) | [PDF](https://arxiv.org/pdf/2611.16175v1)

### InfiniDream: Open-Ended Photorealistic 3D Worlds Through Procedural Generation (2610.26853v2)
- **Title (EN)**: InfiniDream: Open-Ended Photorealistic 3D Worlds Through Procedural Generation
- **Authors**: Yi-Chuan Huang ; Hao-Jen Chien ; Zheng-Hui Huang ; Yu-Lun Liu ; Kaipeng Zhang ; Zhixiang Wang
- **Affiliation**: Alaya Lab ; National Yang Ming Chiao Tung University ; National Taiwan University (PDF page-1)
- **Venue/conference**: arXiv preprint (Project page: yichuanh.github.io/infinidream-page/)
- **Date**: 2026-10-19
- **Abstract**: Procedural generation is key for synthetic data & game development (greater controllability, editability, diversity), but VLM-based code generation produces relatively simple 3D assets while sophisticated photorealistic procedural systems require manual development; VLM-guided procedural methods are constrained by predefined factories/APIs. InfiniDream — a VLM-driven framework for open-ended procedural 3D world generation: (1) Symbolically Constrained Asset Generation — LMs create novel, photorealistic procedural assets preserving editability and seed-based diversity; (2) end-to-end text-to-world pipeline: semantic scene planning + Deterministic Frustum-Guided Grid Placement for precise object placement, procedural population and animation. Evaluated on 100 object + 20 scene tasks (4 perceptual metrics), diversity/human-preference analysis.
- **Key innovations**: Symbolically Constrained Asset Generation (LM-written photorealistic procedural assets); text-to-world with semantic planning + Deterministic Frustum-Guided Grid Placement; 100 object + 20 scene tasks.
- **Links**: [arXiv](https://arxiv.org/abs/2610.26853v2) | [PDF](https://arxiv.org/pdf/2610.26853v2)

### An Exploration of Collision-based Enemy Morphology Generation (2606.02832v1)
- **Title (EN)**: An Exploration of Collision-based Enemy Morphology Generation
- **Authors**: Johor Jara Gonzalez ; Matthew Guzdial
- **Affiliation**: Alberta Machine Intelligence Institute (Amii) ; Department of Computing Science, University of Alberta (PDF page-1)
- **Venue/conference**: arXiv preprint
- **Date**: 2026-06-01
- **Abstract**: Despite extensive PCG research, little work has explored generating enemy morphologies — the basic body plan and collision information for in-game enemies. We explore three novel approaches to generate enemy morphologies based on player collision information. Each approach has different strengths/weaknesses but performs equivalent-or-better than evolutionary baselines.
- **Key innovations**: 3 novel approaches for enemy morphology generation from player-collision information; comparable to evolutionary baselines.
- **Links**: [arXiv](https://arxiv.org/abs/2606.02832v1) | [PDF](https://arxiv.org/pdf/2606.02832v1)

### Procedural Generation of First Person Shooter Maps using Map-Elites (2605.30570v1)
- **Title (EN)**: Procedural Generation of First Person Shooter Maps using Map-Elites
- **Authors**: Simone de Donato ; Pier Luca Lanzi ; Daniele Loiacono
- **Affiliation**: Not stated on arXiv PDF p.1
- **Venue/conference**: arXiv preprint
- **Date**: 2026-05-28
- **Abstract**: We apply MAP-Elites (quality-diversity) to design FPS levels. Considers two map representations (All-Black, Grid-Graph) plus two novel ones (Point-Line, Spatial-Layout). Defines topological metrics (layout-determined) and emergent metrics (evaluated through actual gameplay). In-depth analysis to identify the most suitable features for illumination.
- **Key innovations**: Map-Elites FPS level illumination with 2 new map representations (Point-Line, Spatial-Layout); topological + gameplay-based emergent metrics.
- **Links**: [arXiv](https://arxiv.org/abs/2605.30570v1) | [PDF](https://arxiv.org/pdf/2605.30570v1)

### Runtime Evaluation of Procedural Content Generation in an Endless Runner Game Using Autonomous Agents (2605.01783v1)
- **Title (EN)**: Runtime Evaluation of Procedural Content Generation in an Endless Runner Game Using Autonomous Agents
- **Authors**: Rishabh Kar
- **Affiliation**: Department of Informatics, King's College London
- **Venue/conference**: arXiv preprint (25 pages, 2 figures)
- **Date**: 2026-05-03
- **Abstract**: PCG enables algorithmic content creation without manual design, but generated content may be unbalanced, blocked, repetitive, or technically unsolvable. This paper presents Momentum, an endless-runner game integrating runtime terrain generation, environment-object spawning and autonomous agent-based evaluation in one gameplay loop (constraint-driven placement inspired by Wave Function Collapse).
- **Key innovations**: Momentum endless-runner with runtime PCG + autonomous agent-based runtime evaluation.
- **Links**: [arXiv](https://arxiv.org/abs/2605.01783v1) | [PDF](https://arxiv.org/pdf/2605.01783v1)

### A Novel Procedural Generation for Level Design of Mansions and Dungeons (2606.03857v1)
- **Title (EN)**: A Novel Procedural Generation for Level Design of Mansions and Dungeons
- **Authors**: Isaac Fiuza Vieira ; Kathya Silvia Collazos Linares ; Esteban Walter Gonzalez Clua ; Érick Oliveira Rodrigues
- **Affiliation**: Not stated on PDF p.1
- **Venue/conference**: arXiv preprint (cs.GR)
- **Date**: 2026-06-02
- **Abstract**: PCG is essential for game development (production time/cost, replayability), but unaligned PCG yields incoherent spatial structures and poor gameplay. The work proposes a level-design-principles-guided PCG method for structured indoor environments (houses, mansions, dungeons): 3 stages — spatial-structure segmentation, layout synthesis, refinement — ensuring architectural coherence and navigability.
- **Key innovations**: Level-design-principles-guided PCG for mansions/dungeons (3 stages: segmentation, layout synthesis, refinement).
- **Links**: [arXiv](https://arxiv.org/abs/2606.03857v1) | [PDF](https://arxiv.org/pdf/2606.03857v1)

### From World-Gen to Quest-Line: A Dependency-Driven Prompt Pipeline for Coherent RPG Generation (2604.25482v1)
- **Title (EN)**: From World-Gen to Quest-Line: A Dependency-Driven Prompt Pipeline for Coherent RPG Generation
- **Authors**: Dominik Borawski ; Marta Szulc ; Robert Chudy ; Małgorzata Giedrowicz ; Piotr Mironowicz
- **Affiliation**: Gdańsk University of Technology
- **Venue/conference**: arXiv preprint (13 pages, 1 figure, 5 listings)
- **Date**: 2026-04-28
- **Abstract**: LLMs have strong potential for narrative generation, but complex multi-layered RPG worlds remain limited by coherence/controllability/structural-consistency issues. Dependency-aware, multi-stage prompt pipeline for procedural RPG content generation, modeling narrative dependencies via structured intermediate representations: world building → NPC creation → player character → campaign-level quest planning → quest expansion.
- **Key innovations**: Dependency-aware multi-stage prompt pipeline for coherent RPG generation (world/NPC/player/quest-planning/quest-expansion stages).
- **Links**: [arXiv](https://arxiv.org/abs/2604.25482v1) | [PDF](https://arxiv.org/pdf/2604.25482v1)

---

## 5) Game Benchmarks

### 3D GameDev Arena: Benchmarking Coding Agents That Plan, Build, and Playtest Extreme Long-Horizon Browser Games (2611.24073v1)
- **Title (EN)**: 3D GameDev Arena: Benchmarking Coding Agents That Plan, Build, and Playtest Extreme Long-Horizon Browser Games
- **Authors**: Bizhe Bai ; Jiliang Jian ; Yuqing Yan ; Tao Chen ; Ying Wen
- **Affiliation**: Fudan University ; Shanghai Innovation Institute ; Xi'an Jiaotong University ; Shanghai Jiao Tong University (PDF page-1)
- **Venue/conference**: arXiv preprint (23 Pages)
- **Date**: 2026-11-18
- **Abstract**: Coding agents now generate compact playable games, but whether they can build a large 3D game from scratch remains open; quality rests on player enjoyment (coupling mechanics, scenes, assets, logic). 3D GameDev Arena: a first extreme long-horizon benchmark of 108 from-scratch game-development tasks across 14 genres. Given only a text spec + UI/UX reference images, a plan–implement–test–repair pipeline builds each task into a self-contained browser game (avg ~1,000 LLM calls; longest 14,407 calls, 2.13B tokens, 608 assets). Evaluation: (1) code-level functional acceptance vs spec, (2) agent-based QA/playtesting of 3D presentation & playability, (3) blind pairwise human preference (Bradley–Terry). Findings: 3D game development remains far from solved; code correctness ≠ player preference.
- **Key innovations**: 3D GameDev Arena (108 from-scratch 3D browser-game dev tasks, 14 genres); agent-based QA/playtesting + blind human preference; large-scale plan–implement–test–repair pipeline.
- **Links**: [arXiv](https://arxiv.org/abs/2611.24073v1) | [PDF](https://arxiv.org/pdf/2611.24073v1)

### MANGO Arena: Same Seeds, Different Chains Evaluating LLM Agents in a Disrupted Supply Chain (2611.23613v1)
- **Title (EN)**: MANGO Arena: Same Seeds, Different Chains Evaluating LLM Agents in a Disrupted Supply Chain
- **Authors**: Sara Amar
- **Affiliation**: Department of Engineering, Bowling Green State University
- **Venue/conference**: arXiv preprint (8 pages, 2 figures,)
- **Date**: 2026-11-17
- **Abstract**: MANGO Arena — an open-source testbed in which four LLM agents each run one company in a serial supply chain adapted from MANGO, a classroom factory-management game. Hard rules enforced (truck limit, no-credit cash constraint, production capacity), every blocked rule attempt logged, and a public message board forbidding side payments. Measures at once: economic outcome (bullwhip effect), rule adherence under pressure, and collusion proposals. Pilot: LLM agents amplified demand variability upstream (7–25× Retailer, 13–179× Supplier); real rule violations rare (≤7/288 per model); no collusion proposals. Caveats: API failures enter metrics as silent "no order" decisions; reruns change metrics by up to 17× — methodological gaps acknowledged.
- **Key innovations**: Rule-adherence + collusion-audit game benchmark (MANGO); bullwhip + rule-adherence + collusion-proposal measurement in one env; pilot findings on API-failure metric contamination.
- **Links**: [arXiv](https://arxiv.org/abs/2611.23613v1) | [PDF](https://arxiv.org/pdf/2611.23613v1)

### MARL-BattleGrounds: A Novel JAX-native Benchmark for Heterogeneous and Competitive Multi-agent RL (2610.14883v1)
- **Title (EN)**: MARL-BattleGrounds: A Novel JAX-native Benchmark for Heterogeneous and Competitive Multi-agent RL
- **Authors**: Ulixes Tariq Hawili ; Subramanian Ramamoorthy ; Yoann Altmann ; Ignacio Carlucho
- **Affiliation**: School of Engineering, University of Edinburgh ; School of Informatics, Heriot-Watt University (PDF page-1)
- **Venue/conference**: arXiv preprint (34 pages, 14 figures, 18 tables. Project website: marl-battlegrounds.com)
- **Date**: 2026-10-10
- **Abstract**: MARL-BattleGrounds (MARL-BGs) — JAX-native, researcher-centric MARL benchmark (sample-efficient, computationally efficient). Team Deathmatch: simultaneous 2-team 5v5 of heterogeneous agents with distinct basic/passive/ultimate abilities designed to synergize/counter. 52 hand-designed maps (12-map curriculum, 10 validation, 10 test). Two evaluation modes: 8 endgame scenarios (win an unseen nearly-lost position vs a reactive controller, 5–10 ticks) + monthly round-robin tournament (Elo leaderboard; all entrants open). Simulator speed: 50,000 5v5 steps/sec on one RTX 5090.
- **Key innovations**: JAX-native MARL benchmark (5v5 Team Deathmatch, heterogeneous classes); curricula + tournament leaderboard; 50k 5v5 steps/sec.
- **Links**: [arXiv](https://arxiv.org/abs/2610.14883v1) | [PDF](https://arxiv.org/pdf/2610.14883v1)

### Chess-World-Model: A 10M-Game Benchmark for Exact State Tracking from Chess Move Sequences (2605.30100v2)
- **Title (EN)**: Chess-World-Model: A 10M-Game Benchmark for Exact State Tracking from Chess Move Sequences
- **Authors**: Benjamin Walker ; Terry Lyons
- **Affiliation**: Mathematical Institute, University of Oxford ; Continuous Intelligence Limited ; Department of Mathematics, Imperial College London (PDF page-1)
- **Venue/conference**: NeurIPS 2026 Evaluations & Datasets
- **Date**: 2026-05-28
- **Abstract**: World models require state tracking (maintaining a correct latent state across action sequences). Chess-World-Model — a large-scale state-tracking benchmark from 10 million real chess games; models predict the exact board state reached after a sequence of legal moves. Includes a held-out real-game split and an OOD test set of uniformly random legal play (at original lengths and matched to human-game length distribution). Transformers struggle; recurrent models (SLiCE, Mamba-3, Gated DeltaNet with negative eigenvalues) strongly outperform at 3–8M params; real-game performance saturates by ~18M, with length-matched random eval distinguishing architectures through ~43M.
- **Key innovations**: 10M-game state-tracking benchmark (exact board-state prediction); OOD random-play length-matched eval; recurrent models beat transformers at 3–8M params.
- **Links**: [arXiv](https://arxiv.org/abs/2605.30100v2) | [PDF](https://arxiv.org/pdf/2605.30100v2)

### MINDGAMES: A Live Arena for Evaluating Social and Strategic Reasoning in Multi-Agent LLMs (2605.29512v1)
- **Title (EN)**: MINDGAMES: A Live Arena for Evaluating Social and Strategic Reasoning in Multi-Agent LLMs
- **Authors**: Kevin Wang ; Anna Thöni ; Benjamin Kempinski ; Bobby Cheng ; Jianzhu Yao … (28 authors)
- **Affiliation**: Not stated on PDF p.1
- **Venue/conference**: arXiv preprint
- **Date**: 2026-05-28
- **Abstract**: LLMs deployed as interactive agents but capacity for sustained social/strategic reasoning poorly understood; static vignettes/single-game benchmarks insufficient. MINDGAMES — multi-game arena (TextArena, TrueSkill ratings) operationalizing complementary reasoning demands: belief attribution under hidden information, opponent modeling via repeated strategic interaction, cooperative inference under knowledge asymmetries, sustained deception in social deduction. Games: Colonel Blotto, Iterated Prisoner's Dilemma, Codenames, Secret Mafia. Validated via 2025 conference competition (944 agents, 76 teams); dataset of 29,571 games + MG-Ref offline protocol.
- **Key innovations**: Multi-game LLM arena (ToM + strategic-reasoning demands); built on TextArena + TrueSkill; validated via 2025 conference; MG-Ref deterministic offline tournament.
- **Links**: [arXiv](https://arxiv.org/abs/2605.29512v1) | [PDF](https://arxiv.org/pdf/2605.29512v1)

---

## 6) Industry Game AI

### Faynt: Scaling and Optimizing Policies for Competitive Melee (2610.02144v1)
- **Title (EN)**: Faynt: Scaling and Optimizing Policies for Competitive Melee
- **Authors**: Ali Janati ; Nikita Kuzmin ; Rohit Swamy ; Charles Niu
- **Affiliation**: Not stated on arXiv metadata
- **Venue/conference**: arXiv preprint (54 pages. Preprint, in review)
- **Date**: 2026-10-01
- **Abstract**: Faynt — family of 10M- and 75M-parameter Transformer policies for Super Smash Bros. Melee, each controlling all 26 characters with a single checkpoint. After RL, the 10M wins 240/244 same-character games (98.4%) vs 14 specialist/multi-character releases, with a winning record against every release; Faynt uses no added action delay. Against a zero-delay Slippi-AI baseline, the 10M wins all 68 games across two conditioning settings. Optimized inference on recorded game states: 5.2 ms (10M) / 8.7 ms (75M) per decision on an NVIDIA T4. Open-sourced weights + benchmark suites + automated model-tournament platform.
- **Key innovations**: Faynt — first 10M-param Transformer for Melee; 98.4% win rate on 244 same-character games (zero-delay); open-sourced weights, benchmark suites, automated tournaments.
- **Links**: [arXiv](https://arxiv.org/abs/2610.02144v1) | [PDF](https://arxiv.org/pdf/2610.02144v1)

---

## 7) Related techniques (self-play, curiosity-driven exploration, hierarchical RL, imitation/IRL, reward shaping, world models, model-based/offline RL, opponent shaping, game-theory learning)

### Learning to Undo: Transfer Reinforcement Learning under State Space Transformations (2611.23081v1)
- **Title (EN)**: Learning to Undo: Transfer Reinforcement Learning under State Space Transformations
- **Authors**: Mridul Mahajan ; Aldo Pacchiano ; Xuezhou Zhang
- **Affiliation**: Boston University ; Broad Institute of MIT and Harvard (PDF page-1)
- **Venue/conference**: NeurIPS'26 paper
- **Date**: 2026-11-17
- **Abstract**: Transfer learning in RL has shown strong empirical success. Study case: source and target MDPs related by an "undo map" (target state space recovered by applying the map to the source). Learn the map by matching state-feature statistics from both MDPs, then transfer the source policy. Theoretical analysis: strictly better sample complexity than tabula rasa RL in the target on linearly-Q*-realizable + linear-undo settings. Empirical: challenging continuous-control tasks and Atari games show significantly better sample efficiency (beyond the regime).
- **Key innovations**: Undo-map transfer by state-feature-statistics matching; theory: strictly better sample complexity on linear regimes; Atari + continuous-control empirical wins.
- **Links**: [arXiv](https://arxiv.org/abs/2611.23081v1) | [PDF](https://arxiv.org/pdf/2611.23081v1)

### Optimal Learning in Games with Arbitrary Delays: Best-of-Both-Worlds for Self-Play and Adversarial Opponents (2611.07773v1)
- **Title (EN)**: Optimal Learning in Games with Arbitrary Delays: Best-of-Both-Worlds for Self-Play and Adversarial Opponents
- **Authors**: Emmanuel Esposito ; Andrew Jacobsen ; Hao Qiu ; Alexander Ryabchenko ; Mengxiao Zhang
- **Affiliation**: National University of Singapore ; University of Toronto, Vector Institute
- **Venue/conference**: arXiv preprint (cs.LG, stat.ML)
- **Date**: 2026-11-05
- **Abstract**: Zero-sum games with delayed feedback; Multi-Anchor Optimistic Online Mirror Descent (MAO-OMD): optimal fast rates in self-play on smooth games with arbitrary unknown delays, while maintaining minimax-optimal guarantees against arbitrary opponents (O(√(T + d_tot)) regret). Multi-player + player-dependent delay extensions.
- **Key innovations**: MAO-OMD — best-of-both-worlds self-play (fast rates, arbitrary delays) + adversarial regret (minimax-optimal); extends to multi-player.
- **Links**: [arXiv](https://arxiv.org/abs/2611.07773v1) | [PDF](https://arxiv.org/pdf/2611.07773v1)

### When Is a Game a Markov Decision Process? Correspondences Between Game Theory and Reinforcement Learning (2610.41962v2)
- **Title (EN)**: When Is a Game a Markov Decision Process? Correspondences Between Game Theory and Reinforcement Learning
- **Authors**: Eduardo C. Garrido-Merchán
- **Affiliation**: Not stated on PDF p.1
- **Venue/conference**: arXiv preprint (cs.GT, cs.LG)
- **Date**: 2026-10-30
- **Abstract**: RL and game theory describe the same object from two sides (what's rational vs. how experience gets there). This monograph supplies the theorems: a game is a Markov decision process in three senses — definitional identity, exact reduction (value/solution-preserving), or structural analogy that fails under identifiable conditions. Covers standard game classes (normal-form, repeated, stochastic, partially observable, extensive-form, Bayesian, graphical, Stackelberg, potential, coalitional, mean-field, evolutionary) and solution concepts (Nash ↔ Bellman fixed point; quantal response ↔ soft Bellman; Shapley value ↔ credit assignment; approachability ↔ no-regret). Maps model classes to sound training procedures + complexity of solution problems; catalogs correspondences that do NOT hold (non-stationarity invalidates independent-learner reduction; uncoupled convergence to Nash impossibility; CCE vs CE gap in no-regret self-play).
- **Key innovations**: Theorems characterizing game↔MDP correspondences (identity / reduction / analogy); full taxonomy of game classes ↔ RL decision-theoretic models; solution-concept correspondences; complexity notes.
- **Links**: [arXiv](https://arxiv.org/abs/2610.41962v2) | [PDF](https://arxiv.org/pdf/2610.41962v2)

### Is Anyone Enforcing the Cartel? What Reinforcement Learning Teaches LLM Agents in Markets (2610.28787v1)
- **Title (EN)**: Is Anyone Enforcing the Cartel? What Reinforcement Learning Teaches LLM Agents in Markets
- **Authors**: Hieu Tran ; Hong Yu
- **Affiliation**: University of Massachusetts Amherst ; University of Massachusetts Lowell
- **Venue/conference**: arXiv preprint (45 pages, 13 figures, 20 tables)
- **Date**: 2026-10-20
- **Abstract**: Evaluations report LLM pricing agents collude; but collusion = enforcement (a cartel holds only if cheaters are punished). Audit tests enforcement by forcing members to cheat in counterfactual market copies. Findings: in self-play, small LLMs learn fixed rules ignoring rivals; against a punishing rival → deterred; against a cheating rival → matching cuts but no enforcement (the costly price war is rarely tried); against own copies, deterred/matching can both earn cartel profits but only enforce them (and only thinly, against large cuts); Q-learners enforce collusion only in pricing; prompted LLMs reach cartel-like outcomes via rules ignoring the market.
- **Key innovations**: Enforcement-based cartel definition + audit methodology for LLM agents in pricing/trading (self-play vs counterfactual enforcement); UMass Amherst/UMass Lowell.
- **Links**: [arXiv](https://arxiv.org/abs/2610.28787v1) | [PDF](https://arxiv.org/pdf/2610.28787v1)

### Thompson Sampling for Learning in Zero-Sum Games (2610.18899v1)
- **Title (EN)**: Thompson Sampling for Learning in Zero-Sum Games
- **Authors**: Kenshi Abe ; Kaito Ariu ; Po-An Wang
- **Affiliation**: CyberAgent ; Tohoku University ; National Tsing Hua University
- **Venue/conference**: arXiv preprint (cs.GT, stat.ML)
- **Date**: 2026-10-11
- **Abstract**: Thompson sampling (TS) achieves logarithmic, asymptotically optimal regret in stochastic bandits, but behavior in multi-agent learning less understood. Study: TS in unknown 2-player zero-sum matrix games with Gaussian bandit feedback; plays the posterior-sampled game's equilibrium. Expected cumulative duality gap: O(√T) generally, O(log T) for pure equilibria (with exact instance-dependent coefficient); minimax lower bounds match; also identify the √T coefficient. Experiments confirm predicted rates.
- **Key innovations**: TS regret rates for zero-sum matrix games (O(√T) with identifiable coefficient / O(log T) for pure); duality-gap analysis; CyberAgent/Tohoku/Tsing Hua.
- **Links**: [arXiv](https://arxiv.org/abs/2610.18899v1) | [PDF](https://arxiv.org/pdf/2610.18899v1)

### Inner-Learning: From Hand-Coded Beliefs to Declarative Knowledge in Trick-Taking Games (2610.38304v1)
- **Title (EN)**: Inner-Learning: From Hand-Coded Beliefs to Declarative Knowledge in Trick-Taking Games
- **Authors**: Stefan Edelkamp
- **Affiliation**: Charles University, Prague (Department of Theoretical Computer Science and Mathematical Logic, Faculty of Mathematics and Physics)
- **Venue/conference**: arXiv preprint
- **Date**: 2026-10-28
- **Abstract**: Declarative approach to belief-state modeling in trick-taking games: extract a state-of-the-art Skat player's hand-coded inference rules into a DSL (¬holds(P,C) — player P cannot hold card set C); round-trip code gen verifies the declarative engine reproduces the original (up to 3 audited bugs); grow the rule base via symmetric derivation + expert-annotated strategy docs; add cardinality constraints (at-most-k / at-least-k) at world-gen; self-play eval: the declarative engine measurably improves win rate & score vs the original.
- **Key innovations**: Skat belief rules → declarative DSL; round-trip verification (3 audited original bugs corrected); symmetric derivation + expert annotations; cardinality constraints; self-play improvement.
- **Links**: [arXiv](https://arxiv.org/abs/2610.38304v1) | [PDF](https://arxiv.org/pdf/2610.38304v1)

### On the Convergence of Alternating Regret Matching Algorithms (2611.02521v1)
- **Title (EN)**: On the Convergence of Alternating Regret Matching Algorithms
- **Authors**: Anh Duc Nguyen ; Ioannis Anagnostides ; Brian Hu Zhang ; Tuomas Sandholm
- **Affiliation**: Carnegie Mellon University ; MIT
- **Venue/conference**: arXiv preprint (cs.GT, cs.LG)
- **Date**: 2026-11-02
- **Abstract**: Alternating RM+ performance (better than simultaneous in practice) is a central ingredient of solvers; theory lags behind. Develop a systematic analysis framework: alternating analog of the RVU property → optimal T^{-1} average-iterate convergence within this family (half-prediction = unique prediction multiplier satisfying the alternating RVU property); refinements: T^{-1/2} best-iterate convergence, strategy-profile convergence to a single Nash equilibrium without uniqueness; separations between alternating and simultaneous updates (a game where half-prediction RM+ converges under alternation but not in the last iterate under simultaneous); 15-game benchmarks show practical speedups.
- **Key innovations**: Alternating RM+ convergence theory (alternating RVU property; T^{-1} avg-iterate; T^{-1/2} best-iterate); unique half-prediction multiplier; alternating vs simultaneous separations; 15-benchmark experiments.
- **Links**: [arXiv](https://arxiv.org/abs/2611.02521v1) | [PDF](https://arxiv.org/pdf/2611.02521v1)

---

## Coverage Notes and Gaps

- **Dedup**: all 32 IDs are new to the wiki (grep-verified against whole-wiki baseline; ~10.8k arXiv IDs across `wiki/synthesis/**`).
- **Window/freshness**: papers new to the wiki, ID-level dedupe; arXiv Export API (`export.arxiv.org/api/query`, sorted by `submittedDate`), window 2026-11-09 → 2026-11-23 (today); freshest 2026-11-20.
- **Affiliations**: from PDF page-1 (pypdf) where found; "Not stated on PDF p.1/metadata" marked for Faynt, MINDGAMES, Gamer, PlayScriptBench?, gameplay — author-reported style consistent with prior digests.
- **Limitations**: discovery via ~8 topic queries (~32 unique candidates after dedup, 32 selected); abstracts/authors/dates from Atom feed; all metrics/claims author-reported; no full-text review beyond PDF p.1.
- **Search coverage gap**: EA SPORTS FC 25 Goalkeeping (2610.23216v4, 2026-10-27) not surfaced in result sets this window; excluded (treated as not newly recovered).
- **Trends**: (1) LLM/VLM game agents + game-native benchmarks (PlayScriptBench, WorldAuditBench, Gamer, GameRealm, HiSTEVE); (2) deeper Game RL — chess self-play efficiency (Braun), RTS command-conditioned RL, GuanDan self-play gap, GTAGym; (3) PCG expansion — LLM-written content (WSP on Unseen Games), LLM-driven world/agent generation (InfiniDream, From World-Gen to Quest-Line), morphology generation (Enemy Morphology); (4) benchmark growth — script synthesis, audit, MARL tournaments; (5) industry-scale game AI (Fayn-class measurable deployments).
