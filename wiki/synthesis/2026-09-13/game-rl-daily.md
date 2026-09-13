---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-09-13)"
type: synthesis
created: 2026-09-13
updated: 2026-09-13
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, pcg, benchmarks, world-models, self-play, multi-agent-rl, game-theory, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-09-13)

> **Weekend note on methodology**: arXiv announced no new mailing on Sun 13 Sep 2026, so the freshest window is the **Fri 11 Sep 2026** mailing (Wed 9 – Thu 10 Sep submission wave, IDs ~2609.069xx–2609.119xx). This run did a **cross-category sweep** of cs.AI / cs.GT / cs.MA / cs.LG / cs.CV / cs.CL / cs.RO / cs.NE / cs.HC recent listings (433 entries parsed), grep-verified every featured ID **0 hits** in `wiki/`, and excluded papers already covered by the 09-12 → 09-13 sibling digests (game-rl-daily, arxiv-daily, arxiv-ai-search, arxiv-paper-check, conference-digest, tech-report-digest). **8 new papers featured; every one is fresh to the wiki.**
>
> **Continuity / already-covered (not re-featured):** The Fine-Grained Complexity of ε-Approximate Nash Equilibrium / Free Games (2609.07136, Golowich — featured in today's sibling [arxiv-daily](https://arxiv.org/abs/2609.07136)); DRG-MAPPO air-combat (2609.11155), SIRV offline MARL selection (2609.08358), AVI-vs-AlphaZero (2609.09094), multi-step-lookahead theory (2609.11807), SUN novelty+reachability (2609.08642), risk-sensitive RL certification (2609.10866), GPU-CFR (2609.11923) [09-12 digest]; CAST (2607.25308), Odysseus (2605.00347) [09-11 digest]; mean-field RL scaling (2609.02928), robust PAC learning of stochastic games (2609.04189) [earlier digests].

---

## 1. Game RL & Cooperative Multi-Agent Learning

### 1.1 Certifying cooperation: a novel approach to cooperative multi-agent task generation
- **Authors**: Yannick Molinghen, Hugo Charels, Tom Lenaerts
- **Affiliation**: Université libre de Bruxelles (MLG research lab, inferred)
- **Venue**: arXiv preprint (2609.06586, cs.MA / cs.AI / cs.LG)
- **Key Innovations**: In the **Laser Learning Environment** multi-agent path-finding domain, asks *when does a shared reward actually require cooperation*. Represents helper→beneficiary interactions as **temporal cooperation graphs** and defines six cooperation profiles as overlapping graph predicates; proves every cooperative trajectory satisfies ≥1 profile. By encoding env dynamics + profile predicates as propositional formulae, distinguishes tasks that admit a profile in *some* winning trajectory from those requiring it in *every* winning trajectory within a horizon. Used as filters, turns a random layout sampler into a **task generator with certified cooperation requirements**.
- **Results**: Five MARL algorithms trained on the certified pools — diversity improves joint success when cooperation-free solutions exist, but when cooperation is required, joint success stays near zero even as individual exits rise (policies chase rewarded partial completion, rarely exhibiting the certified profile).
- **Significance**: A formal machinery for *task-level* cooperation certification — directly relevant to open-ended cooperative game training and to explaining why shared-reward agents under-cooperate.
- **Link**: https://arxiv.org/abs/2609.06586

### 1.2 Reachability-Certified Subteam Decomposition for Locally Interacting Multi-Agent MDPs
- **Authors**: Xiangwu Wang, Chengwei Cao, Hongyuan Tang
- **Affiliation**: (not specified — same group as SIRV 2609.08358)
- **Venue**: arXiv preprint (2609.08366, cs.MA)
- **Key Innovations**: Under persistent communication limits a multi-agent system must decide *which agents may coordinate* through a rollout. Prior work keys off current proximity, but separated agents may interact later and a large pair reward may stay unreachable until too discounted. **RCSD** combines a speed-limit lower bound on pairwise contact time with a reward envelope to form a current-state affinity. For any capacity-valid persistent partition, the cut-affinity sum bounds the reward-deletion error of every unchanged stationary policy; a product of team-optimal policies on the resulting cut MDP has regret ≤ 2× the certificate vs the centralized optimum (both worst-case tight).
- **Results**: On a controlled 5-agent family, RCSD-Exact cuts aggregated normalized regret 56.0% / 28.8% / 25.3% vs uniform / distance-only / envelope-only partitions; no bound violations over 384 + 1,440 evaluations.
- **Significance**: Certificate-grounded partitioning for MARL in structured (game-like) MDPs — the same "model selection = certification" theme as SIRV, extended to pairwise-coordination structure.
- **Link**: https://arxiv.org/abs/2609.08366

### 1.3 Deception in Reach-Avoid Game with Unknown Heterogeneous Attackers Speed Information
- **Authors**: Xiangkai Wu, Shaolin Tan, Wei Wang, Zhen Han
- **Affiliation**: (Chinese university, inferred)
- **Venue**: arXiv preprint (2609.06953, cs.GT / cs.RO)
- **Key Innovations**: Reach-avoid game with two Attackers (maximize arrivals to target) vs one Defender, under **information asymmetry**: attackers' heterogeneous max speeds are private but disclosed only as continuous ranges. Heterogeneity pushes uncertainty from a common capability level to the *relative capability configuration*, creating capture-order ambiguity over infinitely many speed combinations. Introduces a **critical speed pair** framework characterizing when different capability configurations induce different optimal capture orders (lifting the Defender's guessing behavior) and enabling **information-limiting strategies** for the attackers.
- **Results**: Under certain initial conditions attackers can mislead the Defender via a slow-speed deception strategy, achieving better payoffs than in the complete-information game; numerics show dilemmas are widespread.
- **Significance**: Bluffing/deception as a first-class mechanism in adversarial game RL — relevant to imperfect-information bot design and meta-strategy in pursuit games.
- **Link**: https://arxiv.org/abs/2609.06953

---

## 2. Game Foundation Models & World Models

### 2.1 World in World: Explore the World with World Models
- **Authors**: Chenxi Song, Yanming Yang, Chi Zhang
- **Affiliation**: BAAI / Peking University lineage (inferred)
- **Venue**: arXiv preprint (2609.11548, cs.CV)
- **Key Innovations**: Attack on flexible control of autoregressive video world models: exploring a source video from new viewpoints requires the rollout to stay synchronized with the recorded event, place observed content in the requested view, plausibly complete newly exposed regions, and *recover previously generated appearance* on revisits. **World in World** is a **training-free inference-time interface** that converts heterogeneous control evidence (source-video observations, target-view projections, geometry renderings guiding completion, retrieved generated states beyond the rolling cache) into camera- and time-labelled clean visual states read through the native self-attention of a frozen causal video model. A correspondence router fuses persistent point identities + geometry for token correspondences; **Evidence-wise Attention CFG (EWA)** independently regulates each auxiliary channel's contribution.
- **Significance**: One frozen backbone supports camera-controlled re-rendering, long-horizon revisiting, and human-motion transfer — the "game-world-as-video-model" control stack, complementary to Tencent's H3-World (09-12) but inference-time and training-free.
- **Link**: https://arxiv.org/abs/2609.11548

### 2.2 Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs
- **Authors**: Zhiqi Li, Yuxuan Liao, Bo Zhu
- **Affiliation**: Dartmouth College lineage (Bo Zhu, inferred)
- **Venue**: arXiv preprint (2609.11499, cs.CV)
- **Key Innovations**: Code world models represent worlds as executable programs, but the *construction process* for a complex world is under-specified. **RCWM** reconstructs complex 3D worlds in code from a **single reference image**: a **Recursive Scene Program (RSP)** representation + a construction solver that recursively calls itself following a global-locate → recursively-reconstruct-parts → revisit-compose cycle. Reference-aligned views propagate a shared camera projection across levels; parent revisitation fixes boundary / spatial-relation / shared errors that emerge after local refinement; a vision-language coding agent compares reference images with rendered scenes to guide refinement and descent.
- **Results**: Outperforms prior code-based image-to-scene reconstruction methods across complex scenes; ablations support recursive construction (deeper calls improve finer-scale reconstruction).
- **Significance**: Bridges game-worthy *executable* 3D world building with PCG — a construction principle directly relevant to programmatic game-world generation and interactive world engines.
- **Link**: https://arxiv.org/abs/2609.11499

---

## 3. Game Theory, Self-Play & Equilibrium Learning

### 3.1 Entropic Risk-Sensitive Evolutionary Learning and Equilibrium Selection in Coordination Games
- **Authors**: Solaleh Mohammadi, Xiang Gao, Kaiqing Zhang
- **Affiliation**: University of Maryland (Kaiqing Zhang) + co-authors (inferred)
- **Venue**: Accepted at **IEEE CDC 2026**; arXiv preprint (2609.08677, eess.SY / cs.GT / cs.MA)
- **Key Innovations**: Studies risk-sensitive evolutionary learning dynamics in coordination games. Agents' risk attitudes enter through the entropic risk measure, evaluating opponent-induced payoff uncertainty in noisy best responses under two protocols (best-response-with-mutations and logit choice). In the single-population 2×2 setting — where risk-neutral dynamics favor the risk-dominant equilibrium — risk sensitivity changes the stochastically stable outcome: **risk-seeking selects the payoff-dominant equilibrium; risk-averse selects the maximin equilibrium**.
- **Results**: Also identifies a robust regime where any super-dominant equilibrium is stochastically stable for all risk attitudes, and extends to symmetric k-action games: sufficiently risk-seeking populations uniquely select the strongly payoff-dominant equilibrium when it exists.
- **Significance**: Risk attitude as a "control knob" for equilibrium selection — a self-play/learning-dynamics result transferable to population-based training for game agents.
- **Link**: https://arxiv.org/abs/2609.08677

### 3.2 Exact-Form Regret for Gradient Descent, Mirror Descent and Follow-the-Regularized-Leader
- **Authors**: Ashkan Soleymani, Gabriele Farina, Patrick Jaillet
- **Affiliation**: MIT (Farina / Jaillet, inferred)
- **Venue**: arXiv preprint (2609.09466, cs.LG / cs.GT / math.OC)
- **Key Innovations**: Derives **exact-form** (non-asymptotic, equal-sign) regret expressions for Gradient Descent (GD), Mirror Descent (MD) and FTRL on **reduced-form cycles**, matching known upper bounds without the usual constant slack. The exact characterization makes sharp comparisons across algorithms and highlights where tuned hyper-parameters are actually tight.
- **Significance**: Foundational for no-regret learning in games (self-play convergence rates): exact regret formulas sharpen the theory used to analyze game-solving dynamics.
- **Link**: https://arxiv.org/abs/2609.09466

### 3.3 Towards Actionable Strategy Certificates in Stochastic Parity Games
- **Authors**: Christel Baier, Diane Cauquil, Calvin Chau, Sascha Klüppelholz, Anne-Kathrin Schmuck
- **Affiliation**: TU Dresden (Baier group) + TU Berlin lineage (inferred)
- **Venue**: arXiv preprint (2609.08529, cs.GT)
- **Key Innovations**: Introduces **Actionable Strategy Certificates (ASCerts)**: a local, permissive representation of a large class of winning strategies in stochastic parity games (2.5-player) with quantitative objectives. Extends stochastic-invariant certificates to games, proving synthesized strategies stay in a safe region with probability ≥ λ; reinterprets the certificates as concise local representations of (possibly infinitely many) strategies, combined with strategy templates for almost-sure winning. Enables efficient synthesis, adaptation, and runtime strategy extraction.
- **Significance**: Verifiable, adaptively-reconfigurable strategy synthesis for adversarial/environment games — applicable to safety-certified game-adjacent control and formal game AI.
- **Link**: https://arxiv.org/abs/2609.08529

---

## Summary Statistics

| Category | Papers Count |
|----------|-------------|
| Game RL & Cooperative MARL | 3 |
| Game Foundation Models / World Models | 2 |
| Game Theory / Self-Play / Equilibrium Learning | 3 |
| **Total featured papers** | **8** |

## Cross-references (recently covered elsewhere, not re-featured)

- 2609.07136 — Fine-grained complexity of approximate Nash / free games (Golowich) — [sibling arxiv-daily 09-13](https://arxiv.org/abs/2609.07136)
- 2609.08358 — SIRV offline MARL selection (same authors as 1.2) — 09-12 game-rl-daily
- 2609.09094 / 2609.11807 — AVI-vs-AlphaZero / multi-step-lookahead planning — 09-12 game-rl-daily
- 2609.01560 — H3-World (Tencent) video world model — 09-12 game-rl-daily
- 2609.10464 — Semigroup-JEPA zero-shot physics — 09-10 arxiv-paper-check

## Key Themes

1. **Cooperation is now a certified quantity, not an emergent hope**: Molinghen et al. (2609.06586) turn "does this task require cooperation?" into decidable predicates over temporal cooperation graphs; RCSD (2609.08366) certifies subteam partitions and bounds the delegation regret. MARL-in-games edges from "train more" toward "prove what the task demands".

2. **World models get a code/geometry construction path**: Both CV finds (World in World 2609.11548 — training-free control of frozen video WMs — and RCWM 2609.11499 — recursive scene programs for 3D world building) move the game-foundation-model frontier from *generating* worlds toward *constructing, re-visiting and completing* them structurally.

3. **Risk sensitivity becomes a designed dial**: Entropic risk-sensitive evolutionary dynamics (2609.08677) shows risk attitude *steers* which equilibrium a population lands on — a lever for population-based self-play tuning rather than a nuisance parameter.

4. **Theory refresh for no-regret / safe game play**: Exact-form regret (2609.09466) and actionable strategy certificates (2609.08529) sharpen the formal toolkit underneath self-play convergence and safety-certified game agents.