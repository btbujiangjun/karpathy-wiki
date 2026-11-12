# Game RL & Game AI Bot — Daily Paper Digest (2026-11-12)

- **Date**: 2026-11-12
- **Window**: ~2026-10-15 → 2026-11-10 (latest available arXiv submissions/revisions and recent proceedings metadata indexed at query time)
- **Scope**: Game RL (Atari, Minecraft, roguelikes, tabletop/physical games, etc.), multi-agent RL and self-play, LLM/VLM-powered game agents and NPC/gameplay control, game foundation/world models, procedural content generation (PCG), game benchmarks/environments/infrastructure, industry game AI systems, and related techniques (world models, model-based RL, object-centric RL, memory, imitation/video-to-action learning, hierarchical control)
- **Method note**: Discovery used arXiv Export API queries and recent arXiv listings via `webfetch` in this run (`websearch` was unavailable). Paper metadata, abstracts, venues, affiliations, and reported results below are taken from arXiv abstract/API pages fetched on 2026-11-12 and are **author-reported** unless otherwise noted. Where affiliations or venues are not explicitly present in arXiv metadata, this is stated. Papers already covered in `wiki/synthesis/2026-11-11/game-rl-daily.md` and `wiki/synthesis/2026-11-10/game-rl-daily.md` were intentionally de-emphasized.

## Executive Summary

Recent progress clusters around **long-horizon game agency, reusable world/action representations, and scalable training/evaluation infrastructure**. In Minecraft and other open worlds, agent work increasingly combines planning, memory, skills, and multi-agent coordination: a Gemini 4 Argon team reports the first end-to-end autonomous Ender Dragon completion using Mineflayer-based coding agents (2610.22319), while TaskFrame (2610.40276), MFM (2610.22686), EvolvingBrain (2610.20786), BCMAAC (2610.35398), and MANA (2611.14431) explore planner-controller hierarchies, multimodal filesystem memory, adaptive skill self-evolution, decentralized belief-conditioned collaboration, and embodied NPC alignment. On the RL and world-model side, Mirror (2610.24177) learns video-to-action mappings through self-improvement across Atari, control, and Minecraft; OverSeer (2610.28554) improves multi-agent visual consistency in Minecraft/Doom via fixed auxiliary views; and model-based RL papers target reliable imagined returns and memory (2610.41022, with Atari Pong evaluation). For PCG and infrastructure, CAD (2608.17947, IEEE CoG 2026) evolves reusable generator programs with continual abstraction discovery, JAXtari (2610.23650) accelerates Atari RL with object-centric/modifiable GPU environments, and KlaskTron (2611.03138, RSS 2026) provides a low-cost physical adversarial MARL testbed. Related techniques emphasize object-relative representations (2610.28197, Atari Foosball/Tag) and the shift from raw scores to diagnosis of control, memory, and generalization.

## 1) Game AI Bots, LLM/VLM Agents, and NPC Intelligence

### A team of Gemini 4 Argon agents beats Minecraft
- **Authors**: Maxence Faldor, Satinder Singh, Roberta Raileanu
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF; authors are associated in public contexts with Google DeepMind/academic collaborations, but arXiv page does not provide structured affiliations)
- **Venue / status**: arXiv preprint, 2026-10-15
- **Abstract (summary)**: Four Gemini 4 Argon agents control Minecraft players via Mineflayer, coordinate through in-game chat and shared memory, and autonomously plan/write/debug programs to defeat the Ender Dragon from a random Easy-difficulty world without pre-scouted seeds or human-written game-specific tools.
- **Key innovations**:
  - Fully autonomous multi-agent coding-and-play loop in a long-horizon survival game.
  - Emergent role division, knowledge sharing, and recovery behaviors without manually assigned roles or game logic.
  - Large-scale long-horizon execution: 2,783 programs, 605 deaths, 27h14m end-to-end run.
- **Reported results**: Claims first end-to-end autonomous Minecraft completion by AI agents under the stated setup (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2610.22319) | [PDF](https://arxiv.org/pdf/2610.22319)
- **Why it matters**: A strong industry-scale demonstration of long-horizon multi-agent game autonomy, tool/program synthesis, and coordination under delayed, dependent objectives.

### TaskFrame: Connecting Task-Level Planning with Frame-Level Control for Game Agents
- **Authors**: Guangzhi Wang, Junfu Pu, Yiran Wang, Xingyilang Yin, Honghao Chen, Cheng Cheng, Lingen Li, Yinan Zhou, Jiarui Wu, Yinuo Jiang, Hongbo Jin, Xiaodong Cun, Ying Shan
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue / status**: arXiv preprint, 2026-10-29
- **Abstract (summary)**: Hierarchical Minecraft agent coupling a VLM task planner with a causal Transformer controller for frame-level keyboard/mouse actions. Planner goal tokens produce cached continuous embeddings reused by the low-latency controller.
- **Key innovations**:
  - Planner-controller split bridging high-level decomposition and fast visuomotor control.
  - Dependency-aware GRPO and supervised learning for instruction decomposition.
  - Special goal-token hidden states as reusable control embeddings.
- **Reported results**: Competitive instruction decomposition vs general-purpose VLMs; higher closed-loop combat success rate than evaluated baselines in Minecraft (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2610.40276) | [PDF](https://arxiv.org/pdf/2610.40276)
- **Topics**: Game AI bot, hierarchical control, VLM planning, embodied gameplay.

### Demonstration of MANA: Multi-perspective Alignment of NPC Agents
- **Authors**: Amir Tahmasbi, Keshav Singh, Shaheer Raza, Owen Mei, Jason Wu
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue / status**: arXiv preprint, 2026-11-10
- **Abstract (summary)**: Interactive Minecraft authoring system where developers align NPC behavior by embodying characters in-game and demonstrating movement/dialogue; demonstrations are distilled into generalized context-to-action policies.
- **Key innovations**:
  - Multi-perspective embodied demonstration for NPC alignment.
  - In-situ policy distillation from few minutes of gameplay demonstrations.
  - Runtime switching between character POVs for rapid behavior authoring.
- **Reported results**: After ~2 minutes of play, aligned Fletcher/Farmer NPCs exhibit consistent aggressive/cowardly behaviors in unseen scenarios (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.14431) | [PDF](https://arxiv.org/pdf/2611.14431)
- **Topics**: NPC intelligence, game bot authoring, imitation/alignment from demonstrations.

### EvolvingBrain: An Adaptive Skill System for Multi-modal Agents Self-Evolution in Open Worlds
- **Authors**: Runxuan Liu, Jingqi Shi, Baoxin Wang, Honghong Zhao, Haoyuan Xu, Yueqing Sun, Jiafeng Liang, Tao He, Dayong Wu, Qi Gu, Shijin Wang, Ming Liu, Bing Qin
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue / status**: arXiv preprint, 2026-10-14
- **Abstract (summary)**: Proposes an adaptive skill system for multimodal open-world agents that extracts procedural/problematic patterns from trajectories, evolves stratified domain/plan/action-trap skills, and uses state-aware skill fusion guided by structured abstractive memory.
- **Key innovations**:
  - Stratified skill self-evolution from agent-specific trajectories.
  - State-aware adaptive execution with long-horizon structured memory.
  - Experience organization beyond imitation or outcome-only RL.
- **Reported results**: Improves success rates and shows generalization on VAB-Minecraft and DiscoveryWorld (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2610.20786) | [PDF](https://arxiv.org/pdf/2610.20786)
- **Topics**: Open-world game agents, skill libraries, self-evolution, memory.

### Belief-Conditioned Multi-Agent Actor Critic for Decentralized LLM Collaboration
- **Authors**: Tianle Chen, Shuo Liu, Christopher Amato
- **Affiliation**: Not explicitly listed in arXiv metadata (Christopher Amato is publicly associated with Northeastern University; verify full affiliations from PDF)
- **Venue / status**: Accepted at NeurIPS 2026 Workshop PTA: From Pretrained Representations to Acting Agents (as stated on arXiv)
- **Abstract (summary)**: BCMAAC maintains beliefs over contextual information to improve decentralized LLM collaboration under limited communication and shared objectives.
- **Key innovations**:
  - Belief-conditioned actor-critic training for decentralized LLM agents.
  - Uses communication traces/context inference instead of predefined workflows.
  - Targets multi-turn collaborative tasks with richer contextual information.
- **Reported results**: Improves task performance and collaborative behavior over naive actor-critic baselines on Minecraft gameplay, web search, and tool-use tasks (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2610.35398) | [PDF](https://arxiv.org/pdf/2610.35398)
- **Topics**: Multi-agent LLM collaboration, MARL, Minecraft, decentralized decision-making.

## 2) Game RL, Model-Based RL, and Related Learning Techniques

### Self-Improving Video-to-Action Models
- **Authors**: Hyunwoo Ryu, Eric Ming Chen, Max Wilcoxson, Vincent Sitzmann
- **Affiliation**: Not explicitly listed in arXiv metadata (Vincent Sitzmann is publicly associated with MIT; verify full affiliations from PDF)
- **Venue / status**: arXiv preprint, 2026-10-16
- **Abstract (summary)**: Mirror learns video-to-action/inverse-dynamics mappings through environment interaction without prior action data or hand-crafted rewards, by attempting to execute visual plans and training on resulting video-action pairs.
- **Key innovations**:
  - Self-supervised video-plan following loop for embodied/game agents.
  - Bridges generative video planning and executable control without expert action datasets.
  - Applies to both online self-improvement and offline action-labeled settings.
- **Reported results**: Outperforms leading learning-from-observation methods across Atari, OGBench, and DeepMind Control; achieves near-expert performance with oracle plans; outperforms methods with expert actions/hand-engineered task knowledge on Minecraft BASALT; reports first self-improvement-only iron pickaxe acquisition in Minecraft survival and SOTA offline diamond acquisition (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2610.24177) | [PDF](https://arxiv.org/pdf/2610.24177) | [Project](https://wilcoxsonm21.github.io/mirror/)
- **Topics**: Imitation/inverse dynamics, video-to-action, self-improvement, Atari, Minecraft.

### Density-Guided Bootstrap Boundaries for Latent World-Model Reinforcement Learning
- **Authors**: Shashank Gupta, Pilhwa Lee
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue / status**: arXiv preprint, 2026-10-29
- **Abstract (summary)**: Adapts imagination depth in latent world-model RL using density-guided bootstrap boundaries, replacing fixed horizons with hard/soft trajectory-dependent stopping criteria based on a score-informed density proxy.
- **Key innovations**:
  - Trajectory-dependent return expansion boundary for model-based RL.
  - Hard and soft gating variants preserving boundary value estimates and weighting losses.
  - Theoretical analysis: gated Bellman operator contraction and reduced conditional target variance from early bootstrapping.
- **Reported results**: Improves sample efficiency and late-training performance over fixed-horizon and auxiliary-enabled baselines on continuous-control tasks and Atari Pong, instantiated within Dreamer V3 (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2610.41022) | [PDF](https://arxiv.org/pdf/2610.41022)
- **Topics**: Model-based RL, world models, imagination horizon, Atari.

### Reframing Object-Centric Reinforcement Learning: From Absolute to Relative Representations
- **Authors**: Cedric Derstroff, Jannis Blüml, Janosch Moos, Michael Girstl, Zihan Ye, Debora Clever, Kristian Kersting
- **Affiliation**: Not explicitly listed in arXiv metadata (Kristian Kersting is publicly associated with TU Darmstadt/hessian.AI; verify full affiliations from PDF)
- **Venue / status**: arXiv preprint, 2026-10-20
- **Abstract (summary)**: Argues for object-relative coordinates anchored to relevant entities (ORCA) and introduces ORBiT, a transformer architecture for anchor-relative inputs in RL, improving generalization over absolute global coordinates.
- **Key innovations**:
  - Object-relative state representation and anchor-based inductive bias.
  - ORBiT transformer for relative entity processing in RL.
  - Controlled generalization studies (shifts, rotations, unseen distractors).
- **Reported results**: Outperforms pixel-based PPO baseline with aggregate HNS IQM > 1.0 over 13 Atari games; learns Foosball from scratch and dominates baselines; shows generalization benefits in Tag environment (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2610.28197) | [PDF](https://arxiv.org/pdf/2610.28197)
- **Topics**: Object-centric RL, representation learning, Atari, generalization.

## 3) Game Foundation Models and World Models

### OverSeer: Multi-Agent World Models Beyond What Agents See
- **Authors**: Runjia Li, Kam Woh Ng, Minghao Chen, Junlin Han, Jianyuan Wang, Zhaochong An, Juan-Manuel Perez-Rua, Andrea Vedaldi, Shikun Liu
- **Affiliation**: Not explicitly listed in arXiv metadata (Andrea Vedaldi and several coauthors are publicly associated with University of Oxford/Meta AI research contexts; verify full affiliations from PDF)
- **Venue / status**: arXiv preprint, 2026-10-20
- **Abstract (summary)**: Extends video world models to multi-agent settings by adding fixed auxiliary camera views as a proxy for world-centric state, and compresses redundant semi-static auxiliary views with a delta-VAE.
- **Key innovations**:
  - Fixed auxiliary views for cross-agent and temporal consistency.
  - Delta-VAE encodes changes relative to a static reference image to reduce token/computation cost.
  - Multi-agent world modeling formulation beyond egocentric-only streams.
- **Reported results**: Improved world/agent consistency in Minecraft and Doom experiments, with qualitative real-world multi-camera results; delta-VAE substantially reduces auxiliary-view computational overhead (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2610.28554) | [PDF](https://arxiv.org/pdf/2610.28554)
- **Topics**: Multi-agent world models, game foundation/world models, Minecraft, Doom.

### Multimodal Filesystem Memory For Long-Horizon Embodied Agents
- **Authors**: Chloe Su, Jiahan Li, Zhenting Qi, Chaoran Cheng, Haoyu Chen, Sejoon Jun, Weirui Ye, Yilun Du
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue / status**: arXiv preprint (v2 2026-10-28), 2026-10-15
- **Abstract (summary)**: MFM organizes long-horizon agent memory as a multimodal filesystem with episodic, spatial, semantic/procedural, and working memory components, using searchable textual records linked to original multimodal episodes.
- **Key innovations**:
  - Complementary memory types with retrieval and consolidation into reusable knowledge/procedures.
  - Preserves access to original observations/actions/outcomes instead of relying only on summaries.
  - Designed for long-horizon embodied/game and computer-use tasks.
- **Reported results**: Improves performance with three base models on Minecraft and computer-use tasks; with GPT-6-Astra completes Mine Diamond from Scratch and reaches 16/24 Ender Dragon milestones vs 12.7 for best baseline, and achieves 0.440 mean reward on CUABench-KiCad vs 0.400 best baseline / 0.267 no persistent memory (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2610.22686) | [PDF](https://arxiv.org/pdf/2610.22686)
- **Topics**: Long-horizon memory, embodied agents, Minecraft, planning/execution support.

## 4) Procedural Content Generation and Game Design

### Procedural Content Metageneration via Program Search and Continual Abstraction Discovery
- **Authors**: Matthew Siper, Ahmed Khalifa, Julian Togelius
- **Affiliation**: Not explicitly listed in arXiv metadata (Julian Togelius is publicly associated with NYU; verify full affiliations from PDF)
- **Venue / status**: Accepted for publication in IEEE Conference on Games (CoG) 2026 (as stated on arXiv), 2026-08-18
- **Abstract (summary)**: Searches directly over procedural content generators (Python programs) rather than individual levels, evolving complete generators with LLM mutation/crossover and introducing Continual Abstraction Discovery (CAD) to extract reusable primitives into run-specific helper modules.
- **Key innovations**:
  - Metageneration: evolutionary search in generator-program space for Sokoban, Zelda, Dangerous Dave, and Lode Runner.
  - CAD discovers and reuses abstractions (validation, reachability, structural utilities) during runs.
  - Controlled 2x2 experiment crossing CAD with fixed hand-written domain API.
- **Reported results**: CAD raises mean final best fitness in all eight domain/API comparisons across 160 complete runs; learned libraries are adopted by most later programs (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2608.17947) | [PDF](https://arxiv.org/pdf/2608.17947)
- **Topics**: PCG, LLM-assisted program search, automated game design, reusable abstractions.

## 5) Game Benchmarks, Environments, and Infrastructure

### JAXtari: High-Throughput and Easy-to-Modify Arcade Learning Environment
- **Authors**: Quentin Delfosse, Raban Emunds, Paul Seitz, Sebastian Wette, Jannis Blüml, Daniel Kirn, Dominik Mandok, Kristian Kersting
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue / status**: Advances in Neural Information Processing Systems (NeurIPS 2026), as stated in arXiv journal reference; posted 2026-10-16
- **Abstract (summary)**: Open-source high-performance JAX reimplementation of Atari 2600 environments providing GPU-parallel training, object-centric observations, and flexible environment modification.
- **Key innovations**:
  - GPU-native ALE alternative for modern RL pipelines.
  - Object extraction and environment modification support for robustness/causal/neuro-symbolic studies.
  - High-throughput benchmarking enabling rapid iteration.
- **Reported results**: PPO agents can finish 100M environment steps on a single A100 GPU in under an hour (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2610.23650) | [PDF](https://arxiv.org/pdf/2610.23650)
- **Topics**: Game RL infrastructure, Atari benchmark, object-centric evaluation, modifiable environments.

### KlaskTron: An Open-Source Platform for Physical Adversarial Multi-Agent RL
- **Authors**: Aswin Ramachandran, Jona Schulz, Maurus Derungs, Carlo Angelini, Tobias Meier, Raffaello D'Andrea
- **Affiliation**: Not explicitly listed in arXiv metadata (Raffaello D'Andrea is publicly associated with ETH Zurich/IDSC; verify full affiliations from PDF)
- **Venue / status**: Proceedings of Robotics: Science and Systems (RSS), Sydney, Australia, July 2026 (as stated on arXiv)
- **Abstract (summary)**: Low-cost (<$2500 USD) open-source desktop robotic testbed for adversarial MARL based on KLASK, with hardware designs, GPU-native Isaac Lab digital twin, and validated sim-to-real baseline.
- **Key innovations**:
  - Physical, reproducible adversarial MARL benchmark bridging sim-to-real gap.
  - Complete ecosystem: CAD/BOM, simulation, inference stack, and learned neural actuator model.
  - Zero-shot transfer baseline for emergent competitive behaviors.
- **Reported results**: Demonstrates zero-shot policy transfer and emergent adversarial behaviors on the physical platform (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.03138) | [PDF](https://arxiv.org/pdf/2611.03138) | [Hardware](https://idscethzurich.github.io/klask_hardware) | [Software](https://github.com/IDSCETHZurich/klask_software) | [RL](https://github.com/IDSCETHZurich/klask_rl)
- **Topics**: Multi-agent RL, self-play/adversarial games, sim-to-real, benchmark platform.

## 6) Cross-Cutting Observations

- **Long-horizon autonomy is moving from single-agent prompting to systems**: planning/control splits, memory filesystems, skill banks, and multi-agent program-writing teams are becoming standard design patterns (2610.22319, 2610.40276, 2610.22686, 2610.20786, 2610.35398).
- **World/action representations are becoming more structured**: fixed auxiliary views for multi-agent consistency (2610.28554), density-aware imagination boundaries (2610.41022), object-relative state frames (2610.28197), and video-to-action self-improvement (2610.24177) all reduce reliance on brittle raw observations.
- **Infrastructure is targeting iteration speed and diagnosis**: JAXtari accelerates Atari experimentation and object-level interventions (2610.23650), while KlaskTron and CAD emphasize reproducible physical/symbolic testbeds for adversarial play and generator design (2611.03138, 2608.17947).
- **NPC/game-bot authoring is becoming more interactive**: embodied demonstration/alignment workflows (2611.14431) complement autonomous training by enabling fast, in-context behavior specification.

## Coverage Notes and Gaps

- **Proceedings coverage**: Explicitly identified venues/status from arXiv metadata in this digest include RSS 2026 (KlaskTron), IEEE CoG 2026 (CAD), and NeurIPS 2026-related listings/workshops (JAXtari, BCMAAC). Broader proceedings pages (ICLR/ICML/NeurIPS main tracks, CVPR/ACL workshops, AAAI/CoRL game-related sessions) were not comprehensively crawlable because web search was unavailable.
- **Industry game AI**: Direct deployment papers from major game studios were limited in accessible metadata this window. The strongest industry-adjacent signal is the Gemini 4 Argon Minecraft team report (2610.22319), though structured company affiliation is not present on the arXiv page and should be verified from the PDF.
- **Affiliation verification**: Many entries list authors but lack structured institution fields in arXiv metadata; PDF verification is recommended before canonicalizing affiliations in entity pages.
- **Overlap management**: Intentionally excluded or de-emphasized papers covered in recent digests (e.g. 2611.13113, 2611.12324, 2611.12088, 2611.09625, 2611.13028, 2611.11136, 2610.31162, 2610.27417, 2611.10392, 2611.07867, 2611.04614, 2611.05601, 2611.02455, 2611.06704, 2611.05151).

## Sources Consulted (arXiv API / pages)

- `all:"game" AND (all:"reinforcement learning" OR all:RL)` (submittedDate desc)
- `(all:"game agent" OR all:"game AI") AND (all:LLM OR all:"large language model" OR all:VLM)` (submittedDate desc)
- `all:"world model" AND (all:game OR all:Atari OR all:Minecraft)` (submittedDate desc)
- `all:"procedural content generation" AND all:game` (submittedDate desc)
- `all:"procedural content generation" AND (all:LLM OR all:"reinforcement learning" OR all:"large language model")` (submittedDate desc)
- `(all:"self-play" OR all:"multi-agent reinforcement learning") AND all:game` (submittedDate desc)
- `all:"game benchmark" AND (all:agent OR all:LLM OR all:RL)` (submittedDate desc)
- `(all:Minecraft OR all:StarCraft OR all:Atari OR all:NetHack OR all:poker) AND (all:RL OR all:agent OR all:LLM)` (submittedDate desc)
- Individual abstract/PDF pages for featured papers above
