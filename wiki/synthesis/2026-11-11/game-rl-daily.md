# Game RL & Game AI Bot — Daily Paper Digest (2026-11-11)

- **Date**: 2026-11-11
- **Window**: ~2026-10-20 → 2026-11-09/10 (latest available arXiv submissions and recent listings indexed at query time)
- **Scope**: Game RL (Atari, Minecraft, roguelikes, strategy/board games, etc.), multi-agent RL and self-play, LLM/VLM-powered game agents and NPC/gameplay control, game foundation/generalist models, procedural content/game generation, game benchmarks and environments, and related techniques (world models, intrinsic motivation, imitation learning/behavior cloning, opponent shaping, hierarchical control, test-time adaptation)
- **Method note**: Discovery used arXiv API queries and recent cs.AI/cs.LG listings via `webfetch` (web search unavailable in this run). Paper metadata, venues, affiliations, and results are taken from arXiv abstracts/pages retrieved on 2026-11-11 and are **author-reported** unless otherwise noted. Where affiliations or venues are not explicitly present in arXiv metadata, this is stated.

## Executive Summary

Recent game-AI work emphasizes **learning reusable world knowledge and control interfaces** rather than task-specific scoring alone. New world-model results probe how intrinsic motivation builds transferable models (2611.13113), how many exposures are needed to learn unseen game mechanics at test time in ARC-AGI-3 (2611.12324), and how test-time gradient updates can encode episodic memory for model-based RL across Memory Maze, Atari, and control benchmarks (2611.09625). On the agent side, VLA/gameplay systems push toward scalable supervision and long-horizon play: Script2Play synthesizes Minecraft/Roblox environments and demonstrations for behavior-cloned gameplay (2611.11136), HiSTEVE combines a hierarchical harness with native keyboard/mouse VLA control in Minecraft (2610.31162), and GTAGym turns GTA V missions into an automatically verifiable evaluation/RL environment (2611.13028). In game RL and multi-agent settings, papers explore zero-search high-difficulty roguelike play with failure-driven restarts in Slay the Spire 2 (2611.12088), opponent-shaping update rules learned without opponent access at deployment (2611.08335), and competitive/heterogeneous MARL evaluation via JAX-native battlegrounds (2610.14883). Broader themes include synthetic data/game generation for training, harness/co-evolution for long-horizon agents, and scaling embodied pretraining across diverse virtual worlds.

## 1) Game RL, World Models, and Related Learning Techniques

### Building World Models from Intrinsic Motivation
- **Authors**: Reece Keller, Declan Kutscher, Xaq Pitkow, Aran Nayebi
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: arXiv preprint
- **arXiv / PDF**: [arXiv:2611.13113](https://arxiv.org/abs/2611.13113) | [PDF](https://arxiv.org/pdf/2611.13113)
- **Abstract**: Studies how intrinsic motivation shapes world-model learning in the absence of extrinsic rewards, integrating 24 intrinsic objectives (curiosity, entropy, competency, etc.) into a common model-based RL framework and evaluating downstream zero-shot, few-shot, and multi-task control.
- **Key innovations**:
  - Large comparative study of intrinsic objectives jointly with world-model representation learning (observation reconstruction, latent prediction, redundancy reduction).
  - Evaluates reusable world models across locomotion, manipulation, and open-ended gaming environments.
  - Shows episodic/lifelong novelty can complement recurrent world-model state for transfer/adaptation.
- **Reported results**: Curiosity-driven exploration with observation reconstruction yields the strongest aggregate family profile; episodic+lifelong novelty achieves best zero-shot transfer and few-shot adaptation in compositional vision-based tasks (author-reported).

### How Many Exposures Does a World Model Need? Learning Unseen Game Mechanics at Test Time
- **Authors**: Ku Onoda, Haruto Kawano, Shota Takashiro, Kohei Hayashi
- **Affiliation**: Not explicitly listed in arXiv metadata; code/weights released under Third Intelligence GitHub (verify institutional affiliations from PDF)
- **Venue/conference**: ARC Prize 2026 Paper Track (as stated in arXiv comments)
- **arXiv / PDF**: [arXiv:2611.12324](https://arxiv.org/abs/2611.12324) | [PDF](https://arxiv.org/pdf/2611.12324) | [Code](https://github.com/third-intelligence/WARC)
- **Abstract**: Introduces MechEval for measuring how many exposures a world model needs to learn unseen game mechanics in ARC-AGI-3, and WARC, a 35M-parameter ViT world model updated after each transition at test time.
- **Key innovations**:
  - **MechEval** labels 69 recurring mechanics across 20 ARC-AGI-3 games and scores predictions on mechanic-affected cells per exposure.
  - **WARC** performs full-parameter test-time updates from interaction transitions for unseen game mechanics.
  - **WARC-Agent** pairs learned world model with fixed graph explorer for closed-loop play.
- **Reported results**: On held-out games, WARC learns to predict 4/5 mechanics with >=80% accuracy on affected cells and retains it; half reach that accuracy within ~80 exposures. WARC-Agent triples official efficiency score from 0.15 to 0.46 on public games and scores 0.20 on hidden Kaggle leaderboard games (author-reported).

### Zero-Search Reinforcement Learning for Slay the Spire 2 with Failure-Driven Restarts
- **Authors**: Xiangqin Chen, Zhengxuan Xie
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: arXiv preprint
- **arXiv / PDF**: [arXiv:2611.12088](https://arxiv.org/abs/2611.12088) | [PDF](https://arxiv.org/pdf/2611.12088) | [Code](https://github.com/HalfVulpes/sts2ai)
- **Abstract**: Trains a 6.6M-parameter entity-transformer policy for Slay the Spire 2 that selects actions in one forward pass (no search), using exact replay/restart from the game assembly and a failure-driven curriculum that allocates restarts to states preceding losses.
- **Key innovations**:
  - Exact replayable training/evaluation in headless host of compiled STS2 assembly (v0.107.1).
  - **Failure-driven restart allocation** targets long-horizon late-fight failures common in roguelike deckbuilders.
  - Search-free reactive policy compared against search-based and LLM baselines.
- **Reported results**: On 12,800 held-out A10 games, released policies average 8.05% wins across five characters (Ironclad 15.6%, Regent 12.5%) vs 0.55% for AlphaSpire networks used without search; A0 80.2% (near Spire Mentor 80.3%); 21–27 ms/decision on one CPU core. Failure-driven allocation outperforms uniform restart in Regent initializations by 3.6 pp average in controlled study (author-reported).

### Encoding Memory in World Models with Test-Time Model-Based Reinforcement Learning
- **Authors**: Maxime Burchi, Fayaz Ali Dharejo, Radu Timofte
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: arXiv preprint
- **arXiv / PDF**: [arXiv:2611.09625](https://arxiv.org/abs/2611.09625) | [PDF](https://arxiv.org/pdf/2611.09625)
- **Abstract**: Proposes TT-MBRL, which performs gradient descent at test time to encode episode observations into world-model parameters, creating episode-specific world models for improved long-term memory in model-based RL.
- **Key innovations**:
  - Moves beyond architecture-only memory solutions by adapting world-model parameters during episodes.
  - Evaluated across Memory Maze 2D/3D and standard non-memory benchmarks.
- **Reported results**: Achieves new state-of-the-art on Memory Maze benchmark and maintains strong performance on DeepMind Control and Atari 100k (author-reported).
- **Relevance**: Model-based RL, memory/world models for games, and Atari evaluation.

## 2) LLM/VLM-Powered Game Agents and NPC/Gameplay Control

### GTAGym: Real AAA Game Tasks Environment for Evaluation and Reinforcement Learning
- **Authors**: Jiajun Chen, Shicheng Fang, Jiahao Lu, Yuxin Wang, Xipeng Qiu
- **Affiliation**: Not explicitly listed in arXiv metadata (authors include researchers commonly associated with Fudan University/NLP groups; verify from PDF)
- **Venue/conference**: arXiv preprint
- **arXiv / PDF**: [arXiv:2611.13028](https://arxiv.org/abs/2611.13028) | [PDF](https://arxiv.org/pdf/2611.13028)
- **Abstract**: Presents GTAGym, an environment/framework for evaluating and training agents on GTA V tasks with automatic engine-state outcome checks. Includes GTAVBench (103 online tasks from main-story missions + 47 image-based shooting/sniping tasks) and RL task generation.
- **Key innovations**:
  - **GTAVBench / GTAVBench-AGI**: realistic AAA task benchmark with screenshot+keyboard/mouse interface and automatic verification.
  - Scalable task generator for 3D/image-based shooting and navigation with automatic rewards/termination.
  - Supports LLM/VLM evaluation and LoRA RL fine-tuning in the same game environment.
- **Reported results**: Best evaluated configuration achieves 70.9% overall accuracy on GTAVBench-AGI; LoRA RL of Qwen3.8-27B improves native GTA V tasks from 15% to 23% and transfers out of domain (author-reported).

### From Game Generation to Game Playing: Fully Automated Ability Training for Vision-Language-Action Models
- **Authors**: Changran Liu, Qi Wu, Wenchao Ma, Sharon X. Huang, Haomiao Jiang
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: arXiv preprint
- **arXiv / PDF**: [arXiv:2611.11136](https://arxiv.org/abs/2611.11136) | [PDF](https://arxiv.org/pdf/2611.11136)
- **Abstract**: Introduces an automated pipeline where an LLM agent builds executable game environments/tasks and programmatic experts generate aligned instructions, observations, and keyboard/mouse actions. Trains Script2Play via behavior cloning on synthetic Minecraft and Roblox gameplay.
- **Key innovations**:
  - **Game generation → gameplay training loop**: LLM-driven environment/task construction plus privileged expert demonstration generation.
  - Large synthetic gameplay dataset (150.3 hours) for VLA post-training without human demonstrations or RL.
  - Cross-engine instruction-following evaluation (Minecraft, Roblox/public benchmarks).
- **Reported results**: Script2Play (4B VLM post-trained with behavior cloning) follows gameplay instructions effectively and generalizes across game engines on multiple public game benchmarks (author-reported).

### HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games
- **Authors**: Zecong Tang, Zian Guan, Yuncheng Guo, Zhanqiu Zhang, Yiwen Guo, Bo Dai
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: arXiv preprint
- **arXiv / PDF**: [arXiv:2610.31162](https://arxiv.org/abs/2610.31162) | [PDF](https://arxiv.org/pdf/2610.31162)
- **Abstract**: Hierarchical Minecraft VLA agent with capability-aware harness, structured memory, VLM planner, policy-coupled completion detection, and native vision-only keyboard/mouse control.
- **Key innovations**:
  - Hierarchical planner–controller split with long-horizon orchestration and low-level native interface control.
  - Regime-specific RMSNorm branches and separate mouse-movement embeddings for heterogeneous GUI/non-GUI interactions.
  - Training pipeline: world knowledge injection, imitation learning, and RL with environment feedback.
- **Reported results**: 85.0% on MineStudio Bench and 37.4% average success on OpenHA; completes long-horizon tasks such as crafting an iron pickaxe from scratch (author-reported).

### KPHarness: Co-Evolving Knowledge and Probing for Long-Horizon Gaming Harnesses
- **Authors**: Zhikang Chen, Yueqing Sun, Sen Cui, Ziang Ye, Yu Wang, Yan Feng, Xierui Song, Yu Zhang, Tingting Zhu
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: arXiv preprint
- **arXiv / PDF**: [arXiv:2610.27417](https://arxiv.org/abs/2610.27417) | [PDF](https://arxiv.org/pdf/2610.27417)
- **Abstract**: Adapts the external execution harness of a frozen VLA model via co-evolution of recovery knowledge and active probing, with bounded harness revisions accepted only after matched sandbox improvement.
- **Key innovations**:
  - Knowledge-probing co-evolution: failures trigger diagnostic probes and refine intervention hypotheses.
  - Separates fast policy execution from slow research/adaptation loop with validated cross-task reuse.
- **Reported results**: Improves Minecraft task coverage over bare policy, fixed harness, and knowledge-only/non-adaptive probing baselines; transfers evolved harness/knowledge/probing to unseen tasks (author-reported).

## 3) Multi-Agent RL, Self-Play, and Game-Theoretic Learning

### A Gamified Framework for Conflict-Driven Design: Discovering Strategies for Collaborative Resilience with Multi-Agent Learning
- **Authors**: Jin Gao
- **Affiliation**: Not explicitly listed in arXiv abstract page (verify from PDF/proceedings)
- **Venue/conference**: ACADIA 2025: Computing for Resilience (proceedings), Miami, USA; arXiv posting 2026-11-07
- **arXiv / PDF**: [arXiv:2611.10841](https://arxiv.org/abs/2611.10841) | [PDF](https://arxiv.org/pdf/2611.10841) | [DOI](https://doi.org/10.52842/conf.acadia.2025.2.724)
- **Abstract**: Models urban design conflict as a non-zero-sum digital board game where stakeholder agents allocate scarce resources; trains MARL policies and studies outcomes including self-play behavior and human-in-the-loop replay/intervention.
- **Key innovations**:
  - Game-theoretic/MARL formulation of multi-stakeholder design trade-offs with shared resilience objectives.
  - Human-in-the-loop interface for participatory strategy exploration.
- **Reported results**: 4x4 policies reach ~84% of simulated annealing benchmark; 8x8 self-play favors resilience-improving projects; 12x12 historical-map simulation mean score 452.1 vs 357.3 random baseline over 10,000 runs (author-reported).

### Discovering Update Rules for Opponent Shaping in General-Sum Games
- **Authors**: Hong Jun Lee, Ziyan Wang, Jun Wang, Stefanos Leonardos, Yali Du
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue/conference**: arXiv preprint (v2)
- **arXiv / PDF**: [arXiv:2611.08335](https://arxiv.org/abs/2611.08335) | [PDF](https://arxiv.org/pdf/2611.08335)
- **Abstract**: Introduces DUOS, which meta-learns an update rule for opponent shaping in general-sum games. The learned rule updates an inner network using only the agent's own experience, without access to opponent parameters/policies/rewards/learning rules at deployment.
- **Key innovations**:
  - Discovery of deployment-time opponent-shaping update rules (meta-learned, experience-only).
  - Bridges opponent-shaping methods (e.g. LOLA/M-FOS motivations) with discovered update-rule/meta-learning paradigms.
- **Reported results**: Exhibits opponent-shaping-consistent behavior without reading opponent internals; ranks 1st in normalized mean score and 1st in self-play among tournament entrants (author-reported).

## 4) Game Benchmarks, Environments, and Generalist/Foundation Directions

### MARL-BattleGrounds: A Novel JAX-native Benchmark for Heterogeneous and Competitive Multi-agent RL
- **Authors**: Ulixes Tariq Hawili, Subramanian Ramamoorthy, Yoann Altmann, Ignacio Carlucho
- **Affiliation**: Not fully listed in arXiv metadata (authors include researchers associated with University of Edinburgh/Heriot-Watt in public contexts; verify from PDF)
- **Venue/conference**: arXiv preprint
- **arXiv / PDF**: [arXiv:2610.14883](https://arxiv.org/abs/2610.14883) | [PDF](https://arxiv.org/pdf/2610.14883) | [Project](https://marl-battlegrounds.com)
- **Abstract**: JAX-native heterogeneous competitive MARL benchmark (Team Deathmatch, 5v5 classes/abilities) with maps/curriculum, evaluation modes, scripted opponents, replay tools, LLM-agent API, and human-AI play support.
- **Key innovations**:
  - Scalable, sample-efficient benchmark bridging simple micromanagement and expensive large-scale game environments.
  - Rich evaluation suite: endgame generalization scenarios, tournament/Elo protocol, 11k+ metrics per game.
  - Supports self-play/cross-play/curriculum/zero-shot coordination and LLM-vs-policy evaluation.
- **Reported results**: Simulator runs ~50,000 5v5 game steps/sec on one RTX 5090 with 1,024 parallel games; benchmarked with multiple deep MARL baselines (author-reported).

### Scaling in Games: Continued Pre-Training For Embodied Agents In Diverse Virtual Worlds
- **Authors**: Kuan Zhang, Yukun Chen, Zhihao Yang, Yue Su, Xiangnan Wu, Zirong Chen, Run Luo, Jinkun Hou, Tao Tan, Yinhe Zheng, Yiming Li
- **Affiliation**: Not explicitly listed in arXiv metadata (project/model links indicate THUSI-Lab; verify from PDF)
- **Venue/conference**: arXiv preprint
- **arXiv / PDF**: [arXiv:2610.28698](https://arxiv.org/abs/2610.28698) | [PDF](https://arxiv.org/pdf/2610.28698) | [Project](https://gamescaling.github.io) | [Model](https://huggingface.co/THUSI-Lab/GameScaling)
- **Abstract**: Controlled study of continued pretraining for embodied agents across data volume, diversity, and model size (120 configs, 0.8B–27B, 50–1,600 hours, Minecraft-only to multi-world mixtures), evaluating transfer from in-corpus to unseen worlds.
- **Key innovations**:
  - Systematic scaling analysis for virtual-world embodied agents (data/diversity/model axes).
  - Distinguishes early broad cross-world interface learning from later world-specific gains; fits empirical scaling relation.
- **Reported results**: More data improves in-corpus performance; diversity helps related-world transfer; larger models improve data efficiency but can generalize worse to distant worlds under single-world training. Models are competitive with Minecraft specialists/frontier models in 3D worlds and strong in real-time settings (author-reported).

## 5) Procedural Content Generation and Game/Environment Synthesis

### Script2Play (cross-cutting: game generation + training data synthesis)
- **Primary entry**: [2611.11136](https://arxiv.org/abs/2611.11136)
- **PCG relevance**: Uses an LLM-powered agent with game-building tools to automatically construct executable environments and tasks targeting specified skills, then generates expert demonstrations for VLA training.
- **Why it matters**: Demonstrates automated environment/task generation as a scalable alternative to costly human-collected demonstrations for gameplay instruction following (Minecraft/Roblox).

## Coverage Notes and Gaps

- **Recent proceedings (last ~1–2 weeks)**: Explicit newly indexed proceedings papers were limited in accessible metadata during this run. ACADIA 2025 publication metadata is present for 2611.10841, and ARC Prize 2026 Paper Track is stated for 2611.12324. Broader conference/proceedings cross-checks (NeurIPS/ICLR/ICML/RSS/CoG/CVPR workshop pages, OpenReview proceedings feeds) were not fully crawlable because web search was unavailable.
- **Industry game AI**: Direct "major studio deployment" papers were sparse in this window; GTAGym/Script2Play/HiSTEVE/KPHarness are relevant to practical game-agent stacks and AAA/open-world environments, but company affiliations are not consistently specified in arXiv metadata and should be verified from PDFs.
- **Affiliation verification**: Several entries have author lists but no structured institution fields on arXiv pages; follow-up lint/ingest should extract affiliations from PDFs for canonical records.
- **Overlap management**: Papers already featured in `wiki/synthesis/2026-11-10/game-rl-daily.md` (e.g. Tiresias 2611.10392, PlayGen2 2611.07867, RIDGE 2611.05601, RLiD 2611.02455, Pac-Man diagnosis 2611.06704, etc.) were intentionally de-emphasized here in favor of newer or differently scoped additions.

## Sources Consulted (arXiv API / listings)

- `all:"game" AND all:"reinforcement learning"` (submittedDate desc)
- `all:"game agent" AND (all:LLM OR all:"large language model" OR all:VLM)` (submittedDate desc)
- `all:"world model" AND (all:game OR all:gameplay OR all:"video game")` (submittedDate desc)
- `all:"procedural content generation" AND (all:RL OR all:LLM OR all:game)` (submittedDate desc)
- `all:"game benchmark" AND (all:agent OR all:LLM OR all:RL)` (submittedDate desc)
- `all:"self-play" AND all:game` (submittedDate desc)
- `all:"multi-agent reinforcement learning" AND all:game` (submittedDate desc)
- `(all:Minecraft OR all:StarCraft OR all:Dota OR all:NetHack OR all:Poker OR all:Atari) AND (all:RL OR all:agent OR all:LLM)` (submittedDate desc)
- `all:"game" AND (all:"foundation model" OR all:"generalist" OR all:"vision-language")` (submittedDate desc)
- Recent listings: [cs.AI recent](https://arxiv.org/list/cs.AI/recent), [cs.LG recent](https://arxiv.org/list/cs.LG/recent)
- Individual abstract pages/PDFs for featured papers above
