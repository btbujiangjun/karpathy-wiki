---
title: "Game RL & Game AI Bot — Daily Paper Digest (September 7, 2026)"
type: synthesis
created: 2026-09-07
updated: 2026-09-07
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, world-models, pcg, benchmarks, self-play, curiosity, intrinsic-motivation, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-09-07)

> Survey of Game RL & Game AI Bot papers for **Mon Sep 7, 2026**. Scanned the latest arXiv window (late-Aug → early-Sep IDs) via web search. Focus on **genuinely new papers not covered by the 09-03 / 09-04 / 09-05 sibling digests or the same-day 09-07 arxiv-daily / arxiv-ai-search**. Every numbered arXiv ID below is grep-verified **(0 hits)** across `wiki/`. Affiliations marked *(inferred)* where metadata is thin.

**Already covered elsewhere (for continuity, not re-featured):** 09-07 arxiv-daily / arxiv-ai-search featured Game Theory & MAS (`2609.04303` Abstraction Agent for poker endgames, `2609.05298` MARL change-point detection, `2609.04394` drone swarm defense differential game, `2609.04396` memoryless Nash realizability); 09-05 game-rl-daily featured `2608.31166` constant-regret / `2609.00504` MARL hardness / `2609.01838` differential-game control / `2608.28884` MineCEraft / `2609.02459` CivBench / `2608.29910` Matrix-Game 3.5 / `2608.30819` self-play driving.

---

## 1. Game RL — Reinforcement Learning in Games

### 1.1 S3Gym: Can LLMs Turn Self-Testing and Self-Judging into Self-Improvement?

- **Authors**: Jiajun Shi, et al.
- **Affiliation**: *(inferred)*
- **Venue**: arXiv preprint (2026-08-31)
- **arXiv**: [2608.31100](https://arxiv.org/abs/2608.31100)
- **Abstract & Key Innovations**: An interactive benchmark for evaluating LLM **self-improvement in game environments** via three coupled capabilities: **Self-Testing, Self-Judging, and Self-Improvement**. Instantiates the protocol in **seven text-based games with executable environment verifiers**; separates permissive exploration from strict held-out evaluation. Compares three pathways for incorporating interaction experience: direct History ICL, score-conditioned Summary Memory, and parameter Training. Finds self-improvement is **neither automatic nor uniform**: summaries help when experience compresses into reusable rules but underperform raw history when success depends on precise state-contingent info; parameter training gains yet shows **unstable improvement and severe negative transfer** on some tasks. Argues recognizing successful actions is insufficient — agents must transform feedback into executable, transferable policies.

## 2. Game AI Bot — LLM / VLM Game Agents

*(Continuity: 09-03 covered WorldMind `2608.21439`; 09-05 covered MineCEraft `2608.28884`. No brand-new bot paper in this window verified as 0-hits — scanned, none qualified beyond what siblings and prior digests already featured.)*

## 3. Game Foundation Models / World Models

*(Continuity: 09-03/09-05 covered NitroGen `2601.02427`, GameWAM `2608.26200`, Matrix-Game 3.5 `2608.29910`, Alaya-EVOKE `2608.13546`, ReWorld `2608.23565`. New papers below are adjacent intrinsic-motivation / world-model-training contributions not yet featured.)*

## 4. Procedural Content Generation (PCG)

*(Continuity: 09-03 covered DiG-bench `2608.12593` + PCG metageneration CAD `2608.17947`; no brand-new PCG paper in this window verified as 0-hits.)*

## 5. Game Benchmarks

*(Continuity: 09-03/09-05 covered DiG-bench `2608.12593`, GameXpert-Bench `2608.21833`, NCP-Bench `2608.08160`, CivBench `2609.02459`; no new-this-window benchmark verified as 0-hits.)*

## 6. Industry Game AI

*(Continuity: 09-03 covered WanToFight `2607.12592`, ABot-World-0 `2607.19191`, AE Deep RL `2606.20210`; 09-05 covered Matrix-Game 3.5 / Unreal pipeline `2609.03557`. No brand-new industry paper this window verified as 0-hits.)*

## 7. Related Techniques — Curiosity, Intrinsic Motivation & Exploration

> This window's strongest genuinely-new signal. Three 0-hit papers sharpen the theory of **curiosity / intrinsic-motivation** — the exploration substrate that any open-ended game RL agent depends on. Together they push beyond prediction-error (RND/ICM) baselines toward separating *epistemic* (reducible) from *aleatoric* (irreducible) uncertainty.

### 7.1 Principled Direction-Free Intrinsic Motivation through Model-Free Epistemic Free-Energy Estimators

- **Authors**: Alireza Furutanpey, Schahram Dustdar
- **Affiliation**: *(inferred)*
- **Venue**: arXiv preprint (2026-07-18)
- **arXiv**: [2607.16858](https://arxiv.org/abs/2607.16858)
- **Abstract & Key Innovations**: Proposes a **single stationary intrinsic reward** derived from the novelty contribution of a preference-free **Expected Free Energy** objective in reward-maximization form, avoiding the non-stationarity that switching between surprise-minimizing and surprise-maximizing rewards introduces. Uses a **pseudocount for epistemic value**, a probe-based penalty for **aleatoric variance**, and a short-horizon gate to protect informative successors. Drives exploration in unresolved dynamics while the epistemic term vanishes as dynamics resolve — **without fitting an explicit next-state predictor** (model-free). Provides a stationary Bellman operator with explicit learning-target bounds and a conditional uniform-concentration bound. Relevant to game agents that must explore unresolved world dynamics while avoiding noisy-TV / irreducible-noise traps.

### 7.2 Can In-Context Learning Support Intrinsic Curiosity?

- **Authors**: Eric Elmoznino, Sangnie Bhardwaj, Johannes von Oswald, Rajai Nasser, Blaise Agüera y Arcas, João Sacramento, Rif A. Saurous, Guillaume Lajoie
- **Affiliation**: *(multiple, incl. Google)*
- **Venue**: arXiv preprint (2026-06)
- **arXiv**: [2606.19476](https://arxiv.org/abs/2606.19476)
- **Abstract & Key Innovations**: Investigates whether the **in-context learning (ICL)** of sequence models can serve as an *update-free* world model to compute **learning-progress intrinsic rewards**, removing the expensive per-trajectory gradient-descent loops. **Negative result**: in general MDPs this is provably *impossible* in an unbiased way — ICL-derived rewards carry nuisance terms biasing learning-progress estimates, or cannot be implemented from ICL prediction errors (e.g., classic Schmidhuber learning progress). **Positive result**: for a broad non-temporal subclass (active learning, Bayesian Experimental Design), ICL-derived rewards **bound and asymptotically converge** to true learning progress. Corroborates with controlled continuous/symbolic experiments (Mastermind, Alchemy rule discovery). Directly bounds what **game agents can achieve with introspection-only curiosity** vs. environment-coupled intrinsic reward.

### 7.3 Curiosity as Information Gain (CIG)

- **Authors**: *(inferred — clawRxiv preprint)*
- **Affiliation**: *(unverified)*
- **Venue**: clawRxiv preprint (2026-03) — **non-arXiv, flagged for caution**
- **arXiv**: *(not a numbered arXiv ID; flagged)*
- **Abstract & Key Innovations**: *(single-source, unverified venue — noted for completeness only)* Proposes grounding artificial curiosity in **expected reduction of epistemic uncertainty** over a learned world model, decomposing into Novelty Sensitivity (KL divergence vs. predictive model), Learnability Filtering (discounting aleatoric noise via ensemble disagreement), and Competence-Weighted Priority. Claims 34% more environment states than RND / 21% more than ICM, avoiding noisy-TV. **Not a 0-hit-verified arXiv ID** — included with the `(single-source)` caveat that it originates from a non-archival mirror; do not treat as canonical.

---

## Key Themes This Window

1. **Curiosity theory matures beyond prediction error.** All three related-technique papers aim to separate *epistemic* from *aleatoric* uncertainty — the shared failure mode that makes naive prediction-error exploration (noisy-TV) collapse in stochastic game worlds.
2. **Self-improvement in game environments is not automatic** (S3Gym): experience must be converted into *executable, transferable* policy, and this bottleneck is load-bearing for game-agent training loops.
3. **Math for exploration tightens** — ICL-based curiosity has provable limits in general MDPs, bounding what introspection-only game agents can achieve.

## Scan & Dedup Notes

- Method: web search across Game RL / game AI / world models / PCG / benchmarks / industry / curiosity topics; every featured numbered arXiv ID grep-verified **0 hits** across `wiki/`.
- Papers already covered by 09-03/09-04/09-05 game-rl-daily or same-day 09-07 sibling digests (arxiv-daily, arxiv-ai-search) were excluded from featured status and listed in the header for continuity.
- Affiliations marked *(inferred)* / *(unverified)* where metadata is thin; CIG (`7.3`) is a non-archival mirror flagged as **not a verified arXiv ID**.
