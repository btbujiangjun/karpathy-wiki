---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-08-23)"
type: synthesis
created: 2026-08-23
updated: 2026-08-23
sources: []
tags: [game-rl, game-ai, llm-agents, world-models, pcg, self-play, benchmarks, reward-shaping, sim-to-real, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest

> Curated arXiv and community papers on Game RL, Game AI Bot, Game Foundation Models, PCG, World Models, Benchmarks, and Related Techniques. Generated 2026-08-23.
>
> **Window**: Weekend edition — Sat Aug 22 → Sun Aug 23, 2026 (no fresh arXiv announcements Fri evening → Sun). This run is therefore a **catch-up sweep of the unclaimed backlog**: the Aug 8–17 wave missed by prior digests, plus two older finds (Feb–Mar 2026). **11 items (10 papers + 1 community tooling release), all NEW** — every ID grep-verified absent from the entire wiki (zero overlap with same-day tech-report-digest and all prior game-rl / arxiv-paper-check / arxiv-ai-search / conference digests). ~45 unique candidate papers screened via ~12 targeted web searches across Game RL, LLM game agents, text-game benchmarks, PCG/world models, offline/imitation RL, and industry news. Note: direct export.arxiv.org API probes in this environment returned only legacy (2019-era) records, so screening relied on web search + per-paper verification against arXiv abs pages. Already-claimed papers excluded on verification: VLM-annotated Trackmania agent [2608.05954], streamed IL augmentations for cloud gaming [2607.14200], Optimistic Policy Regularization [2603.06793], DiG-bench [2608.12593], AgentOdyssey [2606.24893], SciCrafter [2604.24697], CODE-SHARP [2602.10085], SCALAR [2603.09036] (all in earlier digests); CrafterDojo [2508.13530] was unclaimed but excluded as stale (>12 months).

---

## 1. Game RL — Reinforcement Learning in Games

### 1.1 PureTD: Pure Temporal-Difference Learning for Backgammon Money Play
- **Authors**: Alexander Strehl
- **Affiliation**: Independent Researcher
- **Venue**: arXiv preprint, Aug 2026
- **Abstract**: Returns to the TD-Gammon lineage with a deliberately minimal recipe: a pure temporal-difference self-play agent trained for **money-session play** (not just match play), with **no lookahead/search at decision time**. The paper argues that modern compute invites over-engineering of classical board-game agents and shows that a well-tuned TD pipeline remains competitive for backgammon money games, including cube-influenced decisions, while keeping inference trivially cheap.
- **Key Innovations**: Modern replication + ablation of "pure TD, zero search" on money-game evaluation protocol; a strong simplicity baseline for the growing search-augmented game-agent literature.
- **Link**: https://arxiv.org/abs/2608.15146

### 1.2 Watermarked Game Solving via Perturbed Regret Minimization
- **Authors**: Juho Kim, Tuomas Sandholm
- **Affiliation**: Carnegie Mellon University
- **Venue**: arXiv preprint, Aug 2026
- **Abstract**: As game-solving algorithms (CFR-family solvers for poker and other large games) become valuable IP, strategies leak and get reused without attribution. This work embeds **detectable provenance watermarks into solved game strategies** by perturbing the regret-minimization process itself: the solver is steered among near-optimal solutions so the resulting strategy carries a statistical signature recoverable from downstream play, without materially degrading exploitability.
- **Key Innovations**: First watermarking treatment aimed at equilibrium-solving pipelines rather than generative model outputs; ties watermark detectability to perturbation structure inside regret minimization while bounding strategy-quality loss.
- **Link**: https://arxiv.org/abs/2608.14977

### 1.3 AgilePE: Autonomous UAV Pursuit-Evasion via Self-Play Reinforcement Learning
- **Authors**: Wenhao Tang, Tianyang Chen, Zhejun Cui, Boyuan An, Jiayu Chen, Ruize Zhang, Huidong Liu, Tianyue Wu, Qingmin Liao, Fei Gao, Yu Wang, Chao Yu
- **Affiliation**: Tsinghua University / Zhejiang University (tentative — inferred from author roster; abs page lists no affiliations)
- **Venue**: arXiv preprint, Aug 14 2026 (cs.RO), under review
- **Abstract**: A complete sim-to-real system for two-agent UAV pursuit-evasion. The policy maps onboard state observations directly to Collective Thrust and Body Rates (CTBR) commands — no trajectory planner or waypoint controller — trained with competitive **self-play + Prioritized Fictitious Self-Play (PFSP)** over a diversified opponent pool to stabilize optimization and reduce policy oscillation. Deployment uses a hardware-aligned simulator modeling actuator-response dynamics, communication latency, and domain randomization; policies transfer **zero-shot** to real quadrotors, reproducing dodging/flanking tactics and interactive two-agent play.
- **Key Innovations**: End-to-end CTBR control for adversarial aerial pursuit; PFSP-based opponent curriculum shown to suppress oscillation; zero-shot physical transfer of emergent pursuit-evasion tactics.
- **Link**: https://arxiv.org/abs/2608.14135

## 2. Related Techniques — Reward Shaping & Perception-Action Modeling

### 2.1 A Unified Framework for Dynamic Reward Shaping in Reinforcement Learning
- **Authors**: Fouad Bahrpeyma
- **Affiliation**: Independent (single author)
- **Venue**: arXiv preprint, Aug 8 2026 (cs.AI)
- **Abstract**: A theory-led analytical framework comparing **dynamic reward shaping** and neighboring adaptive-reward mechanisms across exploration bonuses, Bayesian guidance, human-in-the-loop learning, automated reward design, and foundation-model reward coding. Distinguishes parametric revision vs state-dependent variation, and additive shaping vs reward replacement / reward-adjacent guidance; comparatively analyzes **twelve method families**, examines when Ng-style policy-invariance guarantees survive deep-RL realities (replay buffers, bootstrapped critics, reward normalization), and flags the unresolved coupling between adaptation rate and learner stability.
- **Key Innovations**: A shared vocabulary/taxonomy for adaptive reward mechanisms; explicit boundary between shaping proper and adjacent mechanisms; relevance to LLM-designed reward pipelines increasingly used in game agents.
- **Link**: https://arxiv.org/abs/2608.08158

### 2.2 CR-Eyes: A Computational Rational Model of Visual Sampling Behavior in Atari Games
- **Authors**: Martin Lorenz, Niko Konzack, Alexander Lingler, Philipp Wintersberger, Patrick Ebel
- **Affiliation**: German HCI group (University of Rostock ecosystem — tentative; abs page lists no affiliations)
- **Venue**: CHI '26 Extended Abstracts (Poster); arXiv Mar 27 2026 (cs.HC)
- **Abstract**: An RL-trained **computational-rationality agent that jointly learns where to look and how to act** under explicit perceptual/cognitive cost constraints in Atari environments. Treating eye movements as goal-directed actions closes the perception-action loop, unlike saliency-prediction user models. Aligns strongly with human task performance and aggregate saliency, while revealing systematic scanpath differences.
- **Key Innovations**: Resource-rational foveated gameplay model on pixel-based dynamic games; human-model comparison at both performance and gaze-trace level. *(Older find — Feb–Mar wave catch-up; previously missed by all digests.)*
- **Link**: https://arxiv.org/abs/2603.26527

## 3. Game AI Bot — LLM/VLM Agents

### 3.1 Hierarchical Self-Improvement (HSI): Task-Specific Evolvable Agent Harnesses
- **Authors**: Tailin Zhou
- **Affiliation**: Single author (abs page lists no affiliation)
- **Venue**: arXiv preprint, Aug 9 2026 (cs.AI)
- **Abstract**: Treats the agent **harness** (executable scaffold around a frozen LLM) as continuously evolvable rather than fixed: each task family owns a harness hot-swapped through a fixed task-injection seam and rewritten from environment feedback. A single frozen backbone operates at three scopes — task harness H, an evolver rewriting H, and a meta-evolver rewriting the evolver's strategy code. On BALROG with DeepSeek-V4-Flash-Preview frozen, HSI gains +39.3 BabyAI / +33.0 Crafter / +25.0 TextWorld / +15.0 MiniHack (% Progress) over the init harness, generalizes held-out on BabaIsAI (0.98 BreakStop, 1.00 GoTo), and beats several frontier models' native configs on TextWorld/Crafter — but yields nothing on NLE, where the feedback signal collapses. Two named bounds: **feedback-fidelity bound** and **backbone capability bound**.
- **Key Innovations**: Meta-level harness evolution with a thinking-on/off ablation isolating evolution's contribution; honest capability-ceiling framing for scaffold engineering on game benchmarks.
- **Link**: https://arxiv.org/abs/2608.08466

### 3.2 NCP-Bench: Can LLM Agents Stick to the Script? Long-Horizon Consistency in Interactive Narratives
- **Authors**: Yingpeng Ma, Jianhao Yan, Bei Shi, Ka Hou Kam, Runnan Wang, Xuebo Liu, Yulong Chen, Yue Zhang, Derek F. Wong
- **Affiliation**: University of Macau / Ocean University of China / Westlake University ecosystem (tentative — inferred from author roster)
- **Venue**: ICML 2026 (accepted); arXiv Aug 8 2026 (cs.CL)
- **Abstract**: Formalizes **Narrative Commitment Preservation (NCP)**: narrator agents must maintain long-horizon logical consistency against unconstrained (adversarial) player interventions. NCP-Bench ships 100 narrative environments derived from movie synopses, each with an auditable specification (trajectory, commitments, initial facts) checked automatically during interaction. Across six SOTA LLMs, fluency does not equal consistency: best model GPT-5.2 survives only 42% of 20-turn interactions, fact-conflict rates run 40–68%, and only isolated runs satisfy all achievement commitments within 100 turns.
- **Key Innovations**: Decouples agent-under-test from a prompt-fixed auditing protocol; first benchmark quantifying commitment drift under adversarial pressure in game-like narrative settings — directly relevant to NPC/story-agent reliability.
- **Link**: https://arxiv.org/abs/2608.08160

## 4. World Models & PCG

### 4.1 Marionette: Predicting World States, Rendering Geometry, Painting Appearance
- **Authors**: Zian Meng, Zhen Li, Chuanhao Li, Qiang Li, Kaipeng Zhang
- **Affiliation**: Shanghai AI Laboratory ecosystem (tentative — inferred from senior author; abs page lists no affiliations)
- **Venue**: arXiv preprint, Aug 14 2026 (cs.CV)
- **Abstract**: Argues interactive game world models should stop autoregressing pixels and instead **explicitly model world state**: a two-stage autoregressive dynamics model predicts an interpretable 276-dimensional 3D state (multi-entity articulated skeletons, metric root trajectories, rotations); a **zero-parameter graphics bridge** computes geometry/occlusion in closed form to emit pose-control videos; a control-conditioned video-diffusion model paints photorealistic RGB. Forcing mismatched action streams shifts root-aligned joint error 31% (state is truly causal); imposing rules *in state space* (terrain collider, separation cap) cuts ground penetration 66% without touching the observation model, at negligible fidelity cost (FVD 831 vs 799 for recorded pose).
- **Key Innovations**: Clean factorization dynamics-state / renderer-geometry / diffusion-appearance for playable world models; shows physics repair belongs in symbolic state space, not in the video prior — a notable counterpoint to fully-latent world-model lines covered in earlier digests (e.g., ForgeWM, PlayWorld).
- **Link**: https://arxiv.org/abs/2608.14530

### 4.2 Beyond Asking: Personalized Game Generation that Reads Players from Behavior
- **Authors**: Yifan Lu, Xiaopeng Yuan, Haohan Wang
- **Affiliation**: University of Illinois Urbana-Champaign (tentative — inferred from senior author)
- **Venue**: arXiv preprint, Aug 17 2026 (cs.AI/HCI)
- **Abstract**: Builds a verified pipeline for behavior-derived player profiling in personalized game generation. Because latent traits are unobservable and questionnaires are noisy/circular, it constructs a synthetic player population whose traits are **ground truth bot parameters** (validated by trait-specific behavioral manipulation), then evaluates policy-agnostic inference from transcripts alone. An **opportunity-aware decision-moment representation** disentangles preference from the chance to express it; few-shot LLM inference beats embedding/rule baselines on most traits though supervised feature regressors remain stronger overall. Inferred profiles then drive difficulty adaptation, validated against ground-truth references and mismatched-profile controls, with an exploratory human study.
- **Key Innovations**: First ground-truth-by-construction benchmark for transcript→trait inference; opportunity-aware representation fixing a subtle confound in behavioral profiling; closed loop from profiling to generated-game adaptation.
- **Link**: https://arxiv.org/abs/2608.16196

## 5. Benchmarks & Evaluation

### 5.1 Two-Bridge: Exclusive Objectives and Extended Horizon StarCraft II Benchmark
- **Authors**: Sourav Panda, Tanmay Ambadkar, Shreyash Kale, Abhinav Verma, Jonathan Dodge
- **Affiliation**: Oregon State University (tentative — inferred from author roster)
- **Venue**: arXiv preprint, v1 Feb 19 2026, v2 Jun 21 2026 (cs.AI)
- **Abstract**: Fills the missing middle between StarCraft II full-game (sparse, noisy rewards, sprawling state-action space) and mini-games (saturable by simple agents). By disabling economy mechanics (resource collection, base building, fog-of-war), Two-Bridge isolates two tactical skills — **long-range navigation and micro-combat** — under exclusive objectives over extended horizons, enabling realistic-budget experiments with modern RL algorithms and steady curricula. Released as a lightweight Gym-compatible wrapper over PySC2 with open-sourced maps/wrappers/reference scripts.
- **Key Innovations**: Purpose-engineered intermediate RTS difficulty tier; clean skill isolation via mechanic ablation rather than map scaling. *(Feb-wave catch-up — previously missed; v2 refresh Jun 21 kept it current.)*
- **Link**: https://arxiv.org/abs/2603.06608

## 6. Industry & Community

### 6.1 bedrock-rl: Deterministic Minecraft RL Framework for VLM Agents (Hugging Face Blog, Aug 19)
- **Source**: Hugging Face community blog post (Aug 19, 2026)
- **What it is**: An open-source framework positioning a **deterministically-seeded Minecraft** stack as a reproducible training substrate for VLM game agents, with **GRPO training via verl** integration for vision-language policies. Emphasis on eliminating simulation nondeterminism so that RL runs on multimodal game agents are comparable across labs.
- **Why it matters**: Complements the wiki's standing observation that Minecraft remains the default proving ground for VLM+RL game agents (cf. MineExplorer, MirrorCraft lines); deterministic replay + mainstream RL infra (verl) lowers the reproduction barrier flagged repeatedly in earlier digests. *(Community release, not peer-reviewed — single-source.)*

---

## Digest Notes

- **Coverage gap acknowledged**: weekend window contained no fresh announcements; all items are backlog catches. The Aug 18–20 wave was already exhaustively mined by the 08-19/08-20/08-21 digests, which is why this edition skews toward Aug 8–17 stragglers.
- **Cross-cutting observations**:
  1. *State-space honesty* — Marionette (explicit 3D state + symbolic physics repair) and Two-Bridge (skill isolation by mechanic ablation) both argue for making hidden structure explicit rather than leaving it implicit in latents or full-game complexity; PureTD makes the mirrored argument that search scaffolds can be dropped when the value function is good enough.
  2. *Provenance & reliability as first-class concerns* — Watermarked Game Solving (solver IP watermarking) and NCP-Bench (narrator commitment auditing) both treat trust/attribution of game-AI outputs as the core problem, a theme absent from earlier digest waves dominated by capability work.
  3. *Harness/scaffold ceiling* — HSI's feedback-fidelity and backbone-capability bounds echo the NLE findings referenced in prior digests: scaffolding cannot rescue tasks beyond the frozen model's reach.
- All entries single-source (arXiv abs pages or one blog post); affiliations marked *tentative* were inferred, not stated.

> ⚠️ No contradictions with existing wiki content detected: none of the retained items overlaps a tracked claim; the two tentative-affiliation inferences follow the convention established in the 08-22 conference-digest log entry.
