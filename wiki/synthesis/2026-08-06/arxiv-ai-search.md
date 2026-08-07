---
title: "arXiv AI Research Scan — August 6, 2026"
type: synthesis
created: 2026-08-06
updated: 2026-08-06
tags: [arxiv, games, game-theory, mechanism-design, multi-agent, cooperative, prosocial, sequential-modeling, attention-free, llm, agents, memory, vlm, sports-analytics, interpretability]
---

# arXiv AI Research Scan — August 6, 2026

Curated papers from the Thu Aug 6, 2026 arXiv listing (Wed Aug 5 submissions, IDs ~2608.04144–2608.05148) with a focus on the clusters the same-day jobs did **not** cover: **games, game theory & mechanism design, multi-agent cooperation & prosocial learning, attention-free sequence modeling, and sports/match forecasting**. The [daily digest](./arxiv-daily.md) (24 papers: agent memory/skills, RL credit assignment, evaluation hygiene, KV/efficiency, industrial rec/ads) and the [paper check](./arxiv-paper-check.md) (27 papers: CTR/rec/ads, reasoning RL, agents, serving, safety) handled the LLM-agent, rec/ads, and safety streams — this scan is **no overlap** with either, nor with the [Aug 5 scan](../2026-08-05/arxiv-ai-search.md) / [Aug 5 digest](../2026-08-05/arxiv-daily.md). All papers verified against arXiv abs pages (the export API was rate-limited at run time). Note: 2608.04020 (*Artificial Institutions*, cross-listed to cs.GT) was excluded because its v1 predates the Aug 5 window (24 Jun 2026).

---

## Games, Game Theory & Mechanism Design

### 1. Sublogarithmic Swap Regret in Multiplayer General-Sum Games via Hybrid Regularization
- **Authors**: Taira Tsuchiya
- **Institution**: N/A (single author)
- **Date**: submitted 2026-08-04
- **Abstract**: Swap regret governs how fast uncoupled learning dynamics converge to correlated equilibria in multiplayer general-sum games. Under full-information feedback, the best prior guarantee for all players following the same dynamics grows logarithmically in the horizon T. This work constructs uncoupled dynamics in which every player incurs only O(nm²√(log m · log T)) swap regret (n players, m actions per player) — the **first sublogarithmic individual guarantee** in this setting — implying the time-averaged product distribution of play is an O(nm²√(log m · log T)/T)-approximate correlated equilibrium. The key choice is combining the Blum–Mansour reduction with optimistic FTRL under a *hybrid regularizer* that separately weights negative Shannon entropy and the log-barrier: entropy controls the optimistic prediction error, while the log-barrier controls transition-matrix movement through its Bregman divergence. A new sensitivity theorem for stationary distributions of Markov chains (involving neither mixing parameters nor the smallest transition probability) transfers this control to the played strategies, yielding a simpler analysis without local-norm or self-concordance arguments. The guarantee survives an adversarially robust variant and a horizon-free variant.
- **Key Innovations**: Hybrid regularization that partitions control duties (entropy ↔ prediction error, log-barrier ↔ transition dynamics); the first sublogarithmic swap-regret guarantee for multiplayer general-sum games.
- **Link**: https://arxiv.org/abs/2608.04149

### 2. From Compensation Design to Budget-Feasible Mechanisms: A Constant Approximation for Subadditive Valuations
- **Authors**: Ioannis Anagnostides, Kshipra Bhawalkar, Christopher Liaw, Aranyak Mehta, Grigoris Velegkas, Weiqiang Zheng
- **Institution**: N/A (tentative; multi-affiliation incl. Google Research)
- **Date**: submitted 2026-08-05
- **Abstract**: Budget-feasible mechanism design (Singer) governs procurement where a buyer with a budget buys services from strategic agents. The paper significantly advances upper bounds: approximation ratios of **3 for monotone submodular** (from 3.798), **e+1 for nonmonotone submodular** (from 9.742), **e+1 for XOS** (from 28, improving to e in large markets), and **2e+1 for subadditive** (from 33, improving to 2e in large markets) — all via universally truthful mechanisms. For subadditive valuations they obtain a **constant-approximation mechanism running in polynomial time using demand queries**, resolving a long-standing open problem of Dobzinski, Papadimitriou, and Singer (who conjectured a constant approximation requires exponentially many demand queries). The results come from a unifying framework of non-truthful indirect *compensation design*: a potential argument yields constant price-of-stability bounds for marginal-contribution payment rules, which are then translated into truthful direct mechanisms. The core subadditive step is a new smoothing lemma: every subadditive function can be approximated within a factor of 2 by a self-bounding function — which also settles an open question in multiwinner elections (existence of a 2e-approximate core under subadditive valuations).
- **Key Innovations**: Constant-approximation, polynomial-time budget-feasible mechanism for subadditive valuations (refuting the DPS conjecture); compensation design as a unifying bridge between indirect mechanisms and truthfulness; the self-bounding smoothing lemma with independent applications.
- **Link**: https://arxiv.org/abs/2608.04337

### 3. Dimensions of Power: A Systematic Guide to Power Indices for Explainable AI
- **Authors**: Filip Naudot, Arunavo Ganguly, Timotheus Kampik, Vicenç Torra, Christopher Blöcker
- **Institution**: N/A (tentative; Umeå University lineage among co-authors)
- **Date**: submitted 2026-08-05
- **Abstract**: Power indices, born in cooperative game theory to allocate profits/costs and analyze voting fairness, have been repurposed as attribution methods for explaining AI outputs — yet selecting the right index for a given explanation task is understudied. This paper organizes power indices along three attribution dimensions — **single-player, set-based, and cardinality-based** — reviewing the indices in each, generalizing existing ones where applicable, and analyzing which formal principles they satisfy (with proofs for properties missing from the literature). It shows that moving to the cardinality-based setting removes player-identity information while preserving some index-level distinctions, and uses concrete examples to illustrate how the dimension and index choice change the resulting attributions in practice.
- **Key Innovations**: A taxonomy of power indices for XAI plus property proofs; guidance for selecting an attribution index by explanation context; characterization of what cardinality-based indices lose (player identity) and keep (index-level distinctions).
- **Link**: https://arxiv.org/abs/2608.05031

---

## Multi-Agent Cooperation & Prosocial Learning

### 4. Emergence of Reputation-Based Cooperation in LLM Agents
- **Authors**: Kazuya Horibe, Kenji Itao, Wataru Toyokawa
- **Institution**: N/A (tentative; University of Hyogo / RIKEN lineage, Japan)
- **Date**: submitted 2026-08-05
- **Abstract**: Can cooperation among LLM agents be evolutionarily stable against free-rider invasion? The authors study an indirect-reciprocity donation game in which LLM agents observe behavioral traces and donate on a continuous scale, with strategies (natural-language prompts) evolving via cultural transmission across generations. Across four LLM backends, robustness to free-rider invasion varies by **more than an order of magnitude**. The strongest predictor of robustness is *opponent endowment sensitivity* — the degree to which agents discriminate cooperative from uncooperative opponents — operationalizing the classical **Image Scoring** mechanism. Notably, adherence to the Leading-Eight (L1) norm does *not* predict robustness; only the stringency of *defector exclusion* does. The authors conclude LLM agents are confined to Image Scoring-like discrimination and fail to develop the more robust Leading-Eight norms — a fundamental vulnerability in culturally evolved LLM cooperation.
- **Key Innovations**: Evolutionary game theory meets culturally evolving LLM strategies; identifies an "Image Scoring ceiling" for LLM cooperation and defector-exclusion as the operative robustness lever — motivating bottom-up norm construction.
- **Link**: https://arxiv.org/abs/2608.04507

### 5. Calibrating Artificial Guilt: Neurally Grounded Reward Shaping for Prosocial Multi-Agent Reinforcement Learning
- **Authors**: Aaditya Mehta, Arya Shah
- **Institution**: N/A (tentative; academic)
- **Date**: submitted 2026-08-05
- **Abstract**: Cooperative multi-agent RL often adds social terms to individual rewards, but the scale of those terms is usually hand-picked. This work asks whether a *guilt* signal can be calibrated from human neural and behavioral data and transferred to artificial agents. Using the public SoDec responsibility fMRI dataset (40 participants), the authors fit a subject-fixed-effects regression of momentary-happiness changes on outcome-type counts and recover a guilt weight as the Partner-negative minus Social-negative contrast (ŵ = 1.118, Cohen's d = 0.214). Embedding this weight in a two-agent Social Lottery environment and training independent PPO actor-critics under four shaping regimes (neurally calibrated, uniform constant, zero/selfish, unit-coefficient oracle), the calibrated agents track the human social safe-choice rate most closely across 1,000 evaluation episodes (0.459 vs human 0.484; KL = 0.0012), while the other three conditions deviate by one to three orders of magnitude in KL.
- **Key Innovations**: Using an fMRI-derived "guilt" coefficient as a quantitative constraint on prosocial reward shaping — neural priors as a calibration signal rather than a hand-tuned hyperparameter.
- **Link**: https://arxiv.org/abs/2608.04663

### 6. Responsibility in Multi-Agent Sequential Decision-Making: Comparing Human Judgments to Formal Models of Causal Attribution
- **Authors**: Nripsuta Ani Saxena, Stelios Triantafyllou, Goran Radanović
- **Institution**: N/A (tentative; academia)
- **Date**: submitted 2026-08-05
- **Abstract**: As AI enters high-stakes decision-making, attributing responsibility for failures becomes critical, yet it is unclear whether formal *actual-causality* responsibility frameworks align with human judgment. Using a modified version of the card game Goofspiel, the authors run a large-scale survey eliciting human responsibility judgments in multi-agent sequential scenarios and evaluate multiple responsibility-attribution methods against them. **No single formal method consistently aligns with human responses**; instead, agent-specific biases and the amount of information available to agents during decision-making significantly shape responsibility judgments.
- **Key Innovations**: A head-to-head evaluation of formal responsibility attribution (actual causality) against human judgments in sequential multi-agent games, with factor analysis of what actually drives human blame assignment.
- **Link**: https://arxiv.org/abs/2608.04318

---

## LLM Architecture, Sequence Modeling & Information Seeking

### 7. Kathleen Writes: Autoregressive Generation and Data Scaling Without Attention
- **Authors**: George Fountzoulas
- **Institution**: N/A (independent; everything reproducible on a free Kaggle T4)
- **Date**: submitted 2026-08-05
- **Abstract**: Paper 3 of the Kathleen series. Earlier papers showed a byte-level, attention-free architecture (wavetable encoder + multi-scale reverberant state) matching strong classification baselines at ~450–700K parameters without pretraining; this work tests whether the same ingredients generate. (1) **Scaling**: on byte-level language modeling (WikiText-103, raw UTF-8, no tokenizer) the reverberant model beats a parameter-matched transformer at every dataset scale measured (2–512 MB), e.g. **1.84 vs 2.04 bits/byte at 512 MB with ~0.5M parameters**; the transformer needs >512 MB to match what the attention-free model learns from 32 MB. (2) **Measurement**: FORM DISTANCE, a non-parametric, gaming-resistant "reads like text" instrument — nine statistical axes of human text define a reference cloud and five constructed fakes are all rejected. (3) **Generation**: decoding policy dominates architecture — widening the sampler halves the same model's distance (3.17 → 1.52), and a retrieval-augmented decoding scheme pushes a frozen model from 1.52 → 1.14 with no training, with the gain attributable to the sparse phrase dose itself, not the selection gate. The gain has a sharp boundary: phrases must come from the model's own training corpus — a 40× larger foreign library helps not at all, an effect the attention twin shares, consistent with in-context integration being a capability of scale. Also reports four architectural additions that did not help and a computed lexicon reaching 94% of a learned table's top-1 accuracy at one fifth of the parameters.
- **Key Innovations**: An attention-free byte-level architecture that scales better than a parameter-matched transformer at small scale; FORM DISTANCE as a gaming-resistant text-quality instrument; decoding-policy > architecture result with a training-corpus-boundary condition on retrieval-augmented decoding.
- **Link**: https://arxiv.org/abs/2608.04678

### 8. Characterizing the Evolving Landscape of Modern Information Seeking
- **Authors**: Shuoqi Sun
- **Institution**: N/A (PhD research statement; **Best Paper Award at FDIA 2026**, 2 pages excl. references)
- **Date**: submitted 2026-08-05
- **Abstract**: Information seeking (IS) evolves along with human IS processes; since the rise of Generative AI, modern IS has shifted toward more interfaces, more complex interactions, and expanded system capabilities. This PhD research systematically characterizes the changes in modern IS using online crowdsourcing survey experiments, theoretical IS frameworks, and in-lab experiments with neurophysiological signals — offering insights into the current landscape of search-interface preferences and the cognitive effort involved in seeking information, to inform future designs of personalized, cognition-aware IS systems.
- **Key Innovations**: (single-source, work-in-progress) A research agenda pairing classical IS frameworks with neurophysiological measurement to characterize GenAI-era search behavior; flagged as a 2-page abstract rather than a full study.
- **Link**: https://arxiv.org/abs/2608.04609

---

## Agents: Spatial Memory & Grounding

### 9. When Memory Lies: An Empirical Study of Spatial Memory Staleness in VLM Agents
- **Authors**: Yushi Sun, Yanjie Zhang
- **Institution**: N/A (tentative; NTU Singapore lineage — same team as *The Personalization Mirage*, 2608.04570)
- **Date**: submitted 2026-08-05
- **Abstract**: Memory-augmented VLM agents act on persistent spatial knowledge that silently goes stale as the environment changes. Using a dynamic FrozenLake testbed, the authors pair a staleness-detection task with a downstream navigation task across three closed-source and three open-weight VLMs under text and image inputs (1,800 detection runs; 12,000 text-mode navigation episodes over four LLM navigators). Three findings: (1) **text solvability does not imply visual grounding** — models that flag stale entries reliably from text still span vision F1 from 0.887 down to 0.067 on identical grids, with the weakest making fluent, confident decisions that ignore the image; (2) consuming stale memory without audit is a safety liability — in the primary GPT-4o setting, an agent trusting raw memory **dies more than twice as often** as the same agent given no memory; (3) auditing helps but does not close the gap — a transparent read-time filter removes much of the safety cost in text mode, yet even oracle stale labels bring no further significant gain at current grid sizes, and unreliable visual auditing yields no consistent benefit from filtering.
- **Key Innovations**: Frames spatial-memory staleness as a safety failure mode for memory-augmented agents; isolates reliable visual grounding and action selection under memory–observation conflict as the central open challenges.
- **Link**: https://arxiv.org/abs/2608.04574

---

## Sports Analytics & Match Forecasting

### 10. From Score Matrices to Football-Aware Match-State Simulation: An Auditable LLM Harness for Exact-Score Reranking
- **Authors**: Shaopeng Liang
- **Institution**: N/A (single author)
- **Date**: submitted 2026-08-05
- **Abstract**: Football score forecasting combines a strong statistical core (Dynamic Poisson-family models estimate team strength, expected goals, coherent score probabilities) with a difficult contextual edge (roles, tactical matchups, motivation, how a first goal changes behavior) that LLMs can reason about but are not calibrated probability engines. The paper documents an auditable information harness built over four iterations: V1 a dynamic score-driven Dixon-Coles baseline; V2 mapping LLM contextual ratings back into expected-goal parameters; V3 replacing scalar correction with goal-by-goal simulation over a frozen score-candidate set; V4 adding shared first-breakthrough and post-goal cascade judgments, time-aware stopping, and deterministic tail candidates. On a chronological replay of the first 150 matches of the 2025-26 English Premier League: V1 10.0% Top-1 / 26.7% Top-3 exact-score accuracy; V3 12.0% / 30.0%; V4 14.7% / 30.7%, raising candidate coverage 77.3% → 84.7% (though no added tail candidate became a Top-3 hit). V1's native 1X2 distribution achieved 53.3% argmax accuracy, 0.9878 log loss, 0.5870 Brier, 0.2095 ranked probability score. Results are explicitly exploratory — the development slice is not an untouched benchmark, and temporal input isolation cannot exclude outcome memory in a closed LLM.
- **Key Innovations**: An auditable hybrid (statistical base + LLM context) exact-score reranking harness with a clear design evolution; negative findings on where football-aware simulation does and does not help.
- **Link**: https://arxiv.org/abs/2608.05030

---

## Cross-Cutting Observations

| Theme | Description | Representative Papers |
|-------|-------------|----------------------|
| **Formal guarantees for adversarial interaction** | Uncoupled dynamics achieving the first sublogarithmic swap regret (2608.04149); polynomial-time constant approximation resolving the DPS conjecture on budget-feasible mechanisms (2608.04337) — theory advancing on both the learning-dynamics and mechanism-design frontiers | Swap Regret, Budget-Feasible Mechanisms |
| **Prosocial and normative behavior as an empirical object** | LLM cooperation is evolutionary fragile and stuck at Image Scoring (2608.04507); human fMRI "guilt" calibrates reward shaping better than hand-tuning (2608.04663); formal responsibility attribution diverges from human blame (2608.04318) | Reputation-Based Cooperation, Artificial Guilt, Responsibility Attribution |
| **Attention-free sequence models keep improving** | A byte-level attention-free architecture beating a parameter-matched transformer at every scale 2–512 MB, plus a gaming-resistant text-quality metric (2608.04678) — complements the KV/efficiency cluster in the daily digest from a "no attention at all" angle | Kathleen Writes |
| **Memory as a liability, not just an asset** | VLM agents die >2× more often trusting stale spatial memory than with no memory (2608.04574); complements the digest's MirageBench/ScrubJay-MEM from the *perception-grounding* side | When Memory Lies |
| **AI for forecasting gets an audit discipline** | The football harness documents negative findings and explicit scope limits (2608.05030); the FDIA best-paper agenda studies GenAI-era information seeking with neurophysiology (2608.04609) | Football Reranking, Modern Information Seeking |

## Key Takeaways

1. **Game-theoretic theory is pushing worst-case bounds down.** Sublogarithmic swap regret for multiplayer general-sum games and a polynomial-time constant approximation for budget-feasible subadditive mechanisms both land in one batch — the first is a learning-dynamics result, the second a mechanism-design result, and both close or sharply narrow long-open gaps.
2. **Cooperation and blame are being measured, not assumed.** LLM-agent cooperation is shown evolutionarily fragile (Image Scoring ceiling); a neural guilt weight derived from fMRI outperforms hand-tuned prosocial reward shaping by orders of magnitude in KL; and formal actual-causality responsibility attribution fails to match human judgment — three empirical lenses on norms.
3. **Attention-free modeling is a live research thread, not a curiosity.** Kathleen Writes demonstrates better scaling than a parameter-matched transformer at small scale and surfaces a training-corpus boundary on retrieval-augmented decoding — worth tracking alongside the KV-cache/efficiency work covered in the daily digest.
4. **Memory needs audit channels tied to perception.** The VLM spatial-memory result (death rate >2× with stale memory vs none) complements the digest's memory engineering with a grounding/conflict-detection requirement: memory value is conditional on the agent catching contradictions with the environment.
5. **Forecasting papers are getting more honest about evaluation.** The football harness explicitly flags its development-slice and outcome-memory caveats — a welcome contrast to benchmark-engineering, and consistent with the day's evaluation-hygiene theme in the daily digest.

> ⚠️ Note on sourcing: All 10 papers verified against arXiv abs pages (Thu Aug 6, 2026 listing; Wed Aug 5 submissions, IDs 2608.04144–2608.05148). The arXiv export API returned HTTP 429 throughout, so metadata was verified via abs pages; institutions marked `(tentative)` where not stated on the abs page. 2608.04020 (Artificial Institutions) was excluded as a pre-window cross-list (v1 24 Jun 2026). This scan is explicitly disjoint from the same-day [daily digest](./arxiv-daily.md), [paper check](./arxiv-paper-check.md), [conference digest](./conference-digest.md), and the [Aug 5 scan](../2026-08-05/arxiv-ai-search.md) / [Aug 5 digest](../2026-08-05/arxiv-daily.md).

## Related Pages
- [arXiv Daily Digest — 2026-08-06](./arxiv-daily.md) — agent memory/skills, RL credit, evaluation hygiene, KV/efficiency, industrial rec/ads (24 papers)
- [arXiv Paper Check — AI & CTR (August 6, 2026)](./arxiv-paper-check.md) — CTR/rec/ads, reasoning RL, agents, serving, safety (27 papers)
- [arXiv AI Research Scan (August 5, 2026)](../2026-08-05/arxiv-ai-search.md) — prior scan (rec/search/ads, RAG, agents, games/simulation)
