---
title: "Game RL & Game AI Bot — Daily Paper Digest (September 9, 2026)"
type: synthesis
created: 2026-09-09
updated: 2026-09-09
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, pcg, benchmarks, world-models, verbal-rl, hierarchical-rl, offline-marl, self-play, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-09-09)

> Survey of Game RL & Game AI Bot papers for **Wed Sep 9, 2026**. arXiv's `list/*/recent` is still anchored at the **Mon 7 Sep 2026** window (no new mailing), which the 09-07/09-08 game-rl-daily and sibling digests already mined twice. This report is therefore a **third pass / noise-floor sweep** over the Sep 1–8 window, plus targeted web mining of the freshest game-specific submissions NOT yet surfaced anywhere in `wiki/`. Every numbered arXiv ID below is grep-verified **0 hits** in `wiki/` before this report (exceptions noted inline). Affiliations marked *(inferred)* where arXiv metadata is thin.

**Already covered elsewhere (continuity, not re-featured):** 09-08 covered S3Gym + curiosity trio, Abstraction Agent (`2609.04303`), MARL change-point detection (`2609.05298`), drone-swarm differential games (`2609.04394`), memoryless Nash (`2609.04396`), TourPhysics (`2609.04911`), causal-induction VGDL (`2602.00190`), SimSkill (`2609.03753`), LifeSync-Games (`2609.03169`), world-acting-systems review (`2609.04894`); 09-05 covered constant regret (`2608.31166`), MARL hardness (`2609.00504`), differential games (`2609.01838`), MineCEraft (`2608.28884`), CivBench (`2609.02459`), Matrix-Game 3.5 (`2608.29910`), self-play driving (`2608.30819`), OOD seq-model offline MARL (`2609.03667`) under 09-05 [[arxiv-ai-search]]; 09-09 [[arxiv-ai-search]] covered postponed-information equilibrium selection (`2609.05897`), Ask-Before-Act (`2609.05961`), emergent-tool-use causal analysis (`2609.06019`); 09-06 [[arxiv-daily]] covered MasterChess/chess-search (`2608.27757`) and dialogue-game agents. Also deduped out: CHAMP MOBA matchmaking (`2609.04870`, CIKM'26, 09-08), NashDreamer (`2609.01549`, 09-02), SPIRAL (`2506.24119`, ICLR'26), DAGS (`2605.14379`), GameDevBench (ICML'26 AIWILD), OmniGameArena (`2606.09826`), GameWorld (`2604.07429`).

---

## 1. Game RL — Reinforcement Learning in Games

### 1.1 Explore More, Drift Less: Outcome-Only Reinforcement Learning Can Suffice for Long-Horizon Interactive Agents (CANOPY)

- **Authors**: Liming Pu, Xiaoxia Li, Yifu Liu, Teng Cao, Bin Yang
- **Affiliation**: *(inferred — multi-institution, likely academic + industry lineage)*
- **Venue**: arXiv preprint, submitted 2026-09-01 (13 pp.)
- **arXiv**: [2609.01245](https://arxiv.org/abs/2609.01245)
- **Abstract & Key Innovations**: Argues that the widely-believed ceiling of **outcome-only RL** on small open models is "an artifact of two failures of common practice": **(1) signal starvation** — group-relative RL with sparse outcome-only rewards only produces a gradient when a task's rollout group mixes successes and failures, so under-scaled exploration silences the hardest, most instructive tasks; **(2) policy drift** — squeezing many updates out of a small task pool degrades the policy when an unanchored objective lets the sampling distribution collapse exactly at saturation. Proposes **CANOPY (Coverage-ANchored On-PolicY RL)**, a minimalist protocol: scale same-task exploration until the natural signal reappears; keep every update on-policy, KL-anchored, and confined to the agent's own action tokens. A **Qwen3-14B** policy trained with CANOPY through environment interaction alone (no task-specific supervision, auxiliary credit signals, or agent scaffolding) **topped the AppWorld public leaderboard** (Feb 2026; Test-Normal TGC 86.9, Test-Challenge 67.6), and the same principles lift Qwen3.5-9B on SWE-bench Verified by **16.6 points**.
- **Game relevance**: Long-horizon interactive agents with end-of-task verification are the direct analog of game agents trained on sparse goal rewards (diamond-hunt in Minecraft, long strategy games). The "exploration scaling directly attacks signal starvation" message transfers directly to sparse-reward game environments, and the "interaction budget at test time" trick parallels how game bots are deployed.

## 2. Game AI Bot — LLM / VLM Game Agents & Game Understanding

### 2.1 Selective Agent Guidance via Entropy: Learning Autonomous Policies from Imperfect VLM Teachers (SAGE)

- **Authors**: Giovanni Bonetta, Matteo Merler, Davide Zago, Rossella Cancelliere, Bernardo Magnini
- **Affiliation**: *(inferred — Fondazione Bruno Kessler / Trento NLP lineage)*
- **Venue**: **EMNLP 2026 Findings** (journal-ref present)
- **arXiv**: [2609.01567](https://arxiv.org/abs/2609.01567)
- **Abstract & Key Innovations**: Frames the problem of learning a **cheap autonomous policy from an online, expensive, and imperfect but informative VLM teacher**. VLM-as-policy is brittle: it must be queried at every step, never improves from interaction, and repeats systematic errors. **SAGE** queries the VLM **only when the learner is uncertain** (entropy-gated), executes the suggested action during training, and distills guidance into a lightweight **RL policy**. Because VLM advice is not always reliable, SAGE weights teacher-action distillation by **environment-derived advantages** rather than treating all suggestions equally. Across sparse-reward visual reasoning and navigation tasks it learns policies that act **without VLM calls at evaluation time** and beats unguided RL in several environments — in some cases **exceeding the VLM teacher**. Selective guidance pays off exactly when the VLM helps discover high-reward trajectories and under-performs when unguided exploration already succeeds.
- **Game relevance**: A direct recipe for game-bot deployment: use a strong VLM as an *entropy-gated coarse navigator* during training, then ship a small distilled RL policy with zero VLM inference cost at inference — the same economics as running polished game agents on console/handheld budgets without cloud VLMs.

## 3. Game Foundation Models / World Models

*(This window's genuinely-new foundation-model-for-games signal is thin — the frontier position is unchanged from 09-08: NitroGen (CVPR'26), GameWorld (`2604.07429`), OmniGameArena (`2606.09826`), and the 2605.09965 "Generalist Game Players" four-era survey remain the anchors. The closest new material this pass surfaced is CoSkill §4 and the Verbal-RL survey §6, which bear directly on how game foundation models accumulate skills and how their feedback channel is defined.)*

## 4. Game AI Bot — Skill Evolution & Hierarchical Agents

### 4.1 CoSkill: Joint Reinforcement Learning of Reasoning and Meta-Skill Agents for Hierarchical Skill Evolution

- **Authors**: Jinyuan Feng, Dongmin Li, Yiqun Chen, Yang Gao, Xing Chen, Huimu Wang, Zhiqiang Pu
- **Affiliation**: *(inferred — Chinese Academy of Sciences / Institute of Automation lineage)*
- **Venue**: arXiv preprint, submitted 2026-09-04
- **arXiv**: [2609.04865](https://arxiv.org/abs/2609.04865)
- **Abstract & Key Innovations**: Identifies a structural flaw in existing **skill-library agentic RL** paradigms: they either decouple skill evolution from policy optimization, or instantiate meta-skills as **fixed workflows** — treating skills as passive objects to be managed. **CoSkill** recasts the static meta-skill workflow as a **learnable Meta-Skill Agent** and jointly trains it with a **Reasoning Agent** over a hierarchical skill library, modeling the two as a **cooperative team sharing a single backbone**. End-to-end co-adaptation: the Reasoning Agent conditions its actions on a retrieved task skill plus step skills from its child set, and its task performance gradient guides the Meta-Skill Agent in refining those step skills. On **ALFWorld 98.4%** and **WebShop 90.6%** success (+3.5 / +6.2 pp over prior skill-based and RL baselines), with better early-stage sample efficiency, asymptotic performance, and wall-clock efficiency.
- **Game relevance**: Skill libraries are the standard abstraction for game NPCs (Voyager-style code skills, MOBA macro skills, fighting-game combo libraries). CoSkill is the first to demonstrate the *co-adaptation loop* — skills improve toward what the agent actually needs while the agent learns to exploit them — which maps directly to open-ended game progression and NPC personalization.

## 5. Game Benchmarks

*(No brand-new standalone game benchmark verified 0-hit this morning — GameXpert-Bench, DiG-bench, CivBench, OmniGameArena, GameWorld remain the September benchmark anchors from 09-03/09-05 digests. Benchmark-relevant novelty this pass lives in §1.1 (CANOPY's AppWorld-style outcome-only protocol is directly transferable to verifiable game-task suites) and §6 (verbal-RL taxonomy as an evaluation-framework lens).)*

## 6. Related Techniques — Verbal RL, Offline MARL, Hierarchical Learning

### 6.1 The Rise of Verbal Reinforcement Learning

- **Authors**: Kshitij Tayal, Arun Sharma, Genta Indra Winata, Anirban Das, Sambit Sahu
- **Affiliation**: *(inferred — multi-institution, incl. IIITD / MBZUAI / Gramener lineage)*
- **Venue**: arXiv preprint, submitted 2026-09-01
- **arXiv**: [2609.01597](https://arxiv.org/abs/2609.01597)
- **Abstract & Key Innovations**: The **first unified account of Verbal Reinforcement Learning (VRL)** — natural language as a primary feedback channel for improving language agents, conveying intent, preferences, and causal structure interpretable by both humans and models. Organized along a single axis (**when** verbal feedback takes effect × **what** it modifies), yielding three pillars: **(1) Language as Grounding Signal** — language defines the task itself (goals, states, reward structures); **(2) Language as Deliberative Feedback** — NL guides test-time reasoning without parameter updates; **(3) Language as Learning Signal** — language-based feedback shapes parameters through training. For each pillar they synthesize representative work, distinguish key approach subcategories, and delineate the distinct role language plays in shaping agent behavior.
- **Game relevance**: Game AI is a prime VRL testbed — reward designers already write game goals in natural language, LLM NPCs receive verbal instruction/teaching, and text-based game agents (TextArena-style) are exactly the "language-defined POMDPs" pillar 1 formalizes. This taxonomy is the framework for classifying next-wave "prompt-as-reward" game training.

### 6.2 (Cross-ref) Out-of-Distribution Generalisation with Sequence Models in Offline Multi-Agent Reinforcement Learning

- **Authors**: Oussama Hidaoui, Omer Ebead, Ulrich Armel Mbou Sob, Siddarth Singh, et al. (large InstaDeep-led team)
- **Affiliation**: **InstaDeep** (+ collaborators)
- **Venue**: arXiv preprint, submitted 2026-09-03 (10 pp.)
- **arXiv**: [2609.03667](https://arxiv.org/abs/2609.03667)
- **Abstract & Key Innovations** *(featured as game-relevant cross-ref; full treatment in 09-05 [[arxiv-ai-search]])*: A principled analysis of **zero-shot task generalisation in offline MARL**, with an extensive empirical study of the scaling behavior of task diversity, dataset size, and network capacity. Extends offline sequence-modeling architectures to **multi-task observation/action spaces with variable agent counts**. Chief finding: **scaling task diversity — not dataset size — is the dominant factor** for robust zero-shot transfer; on Connector, RWARE, **SMAX (StarCraft)**, and LBF the multi-task approach improves held-out tasks **3.2×** over single-task models and beats strong behavior-cloning baselines.
- **Game relevance**: For game-RL, the headline is that a *diverse curriculum of scenarios* (varying agent counts, map/hero configurations) beats simply piling on more offline data — a design rule for building offline datasets for StarCraft-style and sports game bots.

---

## Key Themes This Window

1. **Outcome-only RL's ceiling is a practice bug, not an algorithm ceiling.** CANOPY (`2609.01245`) attributes sparse-reward RL failure to signal starvation (under-scaled exploration) and policy drift (unanchored updates) and fixes both with a minimalist protocol that tops a public interactive-agent leaderboard on a 14B open model — the strongest September counter-example to "need dense rewards / SFT priors / skill libraries for long-horizon agents."
2. **Skill systems are moving from passive artifacts to co-adapted agents.** CoSkill (`2609.04865`) upgrades the "skill library" from a managed object to a jointly-trained meta-skill agent that co-adapts with the reasoning agent — a structural shift for game NPC skill evolution and open-ended progression.
3. **Verbally-specified feedback is becoming a 1st-class RL channel.** The VRL taxonomy (`2609.01597`) and SAGE's entropy-gated VLM distillation (`2609.01567`) both formalize "language as reward/teaching signal" — directly applicable to game reward design and to shipping lightweight game bots trained under VLM guidance but deployed VLM-free.
4. **Task diversity beats data volume in offline multi-agent transfer** (InstaDeep `2609.03667`) — a concrete data-curation rule for StarCraft-class game bots.

## Scan & Dedup Notes

- Method: arXiv `list/{cs.AI,cs.LG,cs.CV,cs.GT,cs.MA}/recent` parsed (still anchored Mon 7 Sep 2026 window) + targeted web search of game RL / game AI bot / game foundation models / PCG / benchmarks / industry / self-play / world-models over the Sep 1–8 window.
- **No new arXiv mailing since Mon 7 Sep 2026**; this is a third-pass noise-floor sweep + web mining. Every featured numbered arXiv ID is grep-verified **0 hits** in `wiki/` before this report (footnoted where a sibling/daily digest carried a passing mention: `2609.03667`).
- Papers already covered by 09-03/09-05/09-07/09-08 game-rl-daily or sibling digests are excluded from featured status and listed in the header for continuity.
- Affiliations marked *(inferred)* where metadata is thin; `2609.01567` venue = EMNLP 2026 Findings (journal-ref field); `2609.01245`/`2609.01597`/`2609.04865` affiliations inferred from author lineage.