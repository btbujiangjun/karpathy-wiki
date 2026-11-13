---
title: arXiv Paper Check — AI & CTR (November 13, 2026)
type: synthesis
created: 2026-11-13
updated: 2026-11-13
sources:
  - http://export.arxiv.org/api/query
  - https://arxiv.org/
tags:
  - arxiv
  - daily-check
  - ai
  - ctr
  - recommendation
  - ads
  - retrieval
  - agents
  - llm
  - daily-digest
---

# arXiv Paper Check — AI & CTR (November 13, 2026)

> **Window note:** Queried on **2026-11-13** via arXiv API (`cs.AI`, `cs.LG`, `cs.IR`, and keyword search for `"click-through rate"` / `CTR`, sorted by submission date). At query time the latest visible submissions in these feeds were primarily dated **2026-11-10–2026-11-11** (e.g. `2611.145xx` in cs.AI/cs.LG, `2611.14938` in CTR/recs results), with no clearly newer 2026-11-12/13 batch returned. This report curates the most interesting **recent** AI and CTR/recommendation papers from that latest available window. All metrics and claims below are **author-reported** from abstracts/metadata unless noted.

## Highlights

| Area | Pick | Why it matters |
|------|------|----------------|
| CTR / recommender systems | **When Does a Recommendation Spark Curiosity? Theory, Measurement, and Field Evidence** (2611.14938) | Formalizes information-gap curiosity into a computable measure, validates it, and reports online A/B gains in CTR, video views, and time spent after deployment. |
| Scientific discovery agents | **Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations** (2611.14514) | Replaces pointwise hypothesis testing with contrast sets over competing explanations, improving resolution from the same evidence/experiment budget (NeurIPS 2026). |
| Agentic RL scaffolding | **AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models** (2611.14515) | Uses a frozen teacher to turn training experience into adaptive strategies/hints; improves RLVR-trained students across ALFWorld, QA, math, and GPU kernel generation. |
| Continual learning evaluation | **Continual-ARC: Measuring Skill Acquisition over a Working Lifetime** (2611.14505) | Proposes a lifelong ARC-based stream to compare memory-based and weight-based continual learning under a unified feedback-budget score. |
| LLM world models / neuro-symbolic | **Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning** (2611.14419) | Finds executability is necessary but insufficient: generated POMDP/stochastic-game world models can be mechanically valid yet structurally diverge from intended decision problems. |
| E-commerce simulation & CTR | **ShopMind: A Mental World Model for Personalized and Realistic E-commerce User Simulation** (2611.11897) | Models evolving beliefs/intents for more realistic user simulation; improves personalization/behavioral realism and downstream CTR prediction. |
| Sponsored search CTR | **Query- and Candidate-Aware Long User Sequence Modeling for Sponsored Product Ranking in Search** (2611.11675) | Combines query- and candidate-aware retrieval over long histories with early fusion; reports online CTR/attributed conversion/orders gains. |
| CTR serving efficiency | **Slim Foundation Models for Latency-Critical Recommendation Serving (SlimFM)** (2611.11013) | Prunes and fine-tunes an LLM to inject field-level semantics into CTR backbones, retaining >99% accuracy with up to 3.4× lower latency. |

## 1) CTR, Recommendation, Advertising & Retrieval

### When Does a Recommendation Spark Curiosity? Theory, Measurement, and Field Evidence
- **Authors:** Pan Li, Alexander Tuzhilin
- **arXiv:** [2611.14938](https://arxiv.org/abs/2611.14938) (submitted 2026-11-11; econ.GN/cs.IR/cs.LG)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Formalizes the information-gap theory of curiosity into five axioms and derives a computational measure of curiosity evoked by a recommended item.
  - Validates the measure via survey study, showing alignment with self-reported curiosity and stronger performance than proxy metrics.
  - Builds a curiosity-aware recommender by incorporating the measure into the utility objective.
- **Reported results:** Offline gains on three real-world datasets over state-of-the-art methods; a large-scale online controlled experiment at a major Asian video-streaming platform significantly increased **click-through rate, video views, and time spent** versus the production system, with subsequent deployment.

### ShopMind: A Mental World Model for Personalized and Realistic E-commerce User Simulation
- **Authors:** Peixuan Hou, Bin Chen, Li He, Jian Xu, Xiuli Ma, Guojie Song
- **arXiv:** [2611.11897](https://arxiv.org/abs/2611.11897) (submitted 2026-11-09; cs.CL)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Introduces a mental world model capturing beliefs, uncertainties, and intentions as they evolve during shopping interactions, rather than predicting next actions directly from history/context alone.
  - Trains a Mental State Reconstruction (MSR) model from behavior–mental-state pairs synthesized by ShopMind.
- **Reported results:** Improves personalization by **18.0%** and behavioral realism by **19.6%** over strongest alternatives; MSR improves consumption value measurement and **CTR prediction**.

### Query- and Candidate-Aware Long User Sequence Modeling for Sponsored Product Ranking in Search
- **Authors:** Dongyue Xie, Sergey Kolbin, Manavender Malgireddy, Iurii Shcherbak, Weixing Tang, Arushi Jain, Wanchen Shao, Kurt Zimmer, Raja Hafiz Affandi, Matt Lindsay
- **arXiv:** [2611.11675](https://arxiv.org/abs/2611.11675) (submitted 2026-11-08; stat.ML/cs.LG)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Addresses sponsored-product search where current query intent and candidate item jointly determine which long-term behaviors are relevant.
  - Uses two long-history retrieval channels (candidate-NN and query-NN), dedicated query/candidate context tokens, and candidate-aware early fusion into history tokens.
- **Reported results:** Offline ablations improve major ranking metrics vs production baseline; online A/B test increased **CTR, attributed conversion rate, and orders per impression** (magnitudes not detailed in abstract).

### Slim Foundation Models for Latency-Critical Recommendation Serving (SlimFM)
- **Authors:** Danyal Aftab, Anas Zafar, Assadig Abakr, Steven Davy
- **arXiv:** [2611.11013](https://arxiv.org/abs/2611.11013) (submitted 2026-11-07; cs.IR/cs.AI)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Makes online LLM semantic modeling practical for CTR pipelines via dependency-aware pruning (LLaMA3-8B → 4.5B), LoRA-based field-aware fine-tuning, and semantic-guided fusion into conventional CTR models.
- **Reported results:** Across 4 datasets and 6 CTR backbones, retains **>99%** of uncompressed-model accuracy while reducing inference latency by **up to 3.4×** relative to LLM-enhanced baselines.

## 2) Core AI, Agents & Evaluation

### Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations
- **Authors:** Ziang Liu, James J. Kim, Yijia Dai, Jennifer J. Sun
- **arXiv:** [2611.14514](https://arxiv.org/abs/2611.14514) (submitted 2026-11-10; cs.AI/cs.CL/cs.LG) — *Accepted at NeurIPS 2026*
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Replaces pointwise hypothesis evaluation (`h` vs `¬h`) with a contrast set of mutually exclusive, collectively exhaustive competing explanations.
  - Scores experiments by belief redistribution across the set and resolves questions when belief concentrates on one explanation; compatible with existing agents for re-evaluation or search guidance.
- **Reported results:** Across six domains, contrast sets resolve **73%** of pointwise candidates with large belief shifts to a specific alternative (vs mostly rejections pointwise); contrast-guided search resolves **67%** more questions than pointwise surprisal under the same budget; blinded expert study chose the same explanation on **78%** of resolved questions.

### AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models
- **Authors:** Zijian Zhang, Rizhen Hu, Jiangweizhi Peng, Shiyang Li, Sujay Bhatt, Sihan Zeng, Mingyi Hong
- **arXiv:** [2611.14515](https://arxiv.org/abs/2611.14515) (submitted 2026-11-10; cs.LG/cs.CL)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Uses a frozen teacher to periodically diagnose student training experience and generate adaptive scaffolds: shared strategies for task classes and hints for hard tasks, removed at evaluation.
  - Applies a unified framework across domains with minimal domain-specific information and no human intervention during training.
- **Reported results:** Outperforms corresponding RL baselines in ALFWorld (+7.2 success points), search-based QA (+4.0 avg EM), math (surpasses reported QuestA accuracy with ~1/3 student training steps), and GPU kernel generation (up to +5.0 points in correct kernels faster than PyTorch reference).

### Continual-ARC: Measuring Skill Acquisition over a Working Lifetime
- **Authors:** Daniel Lenton
- **arXiv:** [2611.14505](https://arxiv.org/abs/2611.14505) (submitted 2026-11-10; cs.LG)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Builds a lifelong stream from ARC-AGI editions where tasks recur with fresh instances after gaps while new tasks arrive; learners pay for demonstrations/answers/actions under a feedback budget.
  - Enables direct comparison of memory-based and weight-based systems on the same scale, with post-stream frozen evaluation for memorization and generalization.
- **Reported findings:** Persistence in tested harnesses generally does not improve memorization without explicit expert guidance; most harness methods learn less than a demo-caching floor; no harness method gains on unseen tasks while weight-based learning shows substantial gains.

### Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning
- **Authors:** Souhaila Djaffal, Amna Jamal, Gagana Madhugiri Devaraja, Anidipta Pal, Jobst Heitzig
- **arXiv:** [2611.14419](https://arxiv.org/abs/2611.14419) (submitted 2026-11-10; cs.AI)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Benchmarks five LLMs generating partially observable stochastic-game world models from 44 scenarios (game, situational, cultural), evaluated on mechanical validity, structural agreement, and semantic criteria.
  - Analyzes 410 first-pass generations across three empirical tracks.
- **Reported results:** In the reference-backed game track, **134/135** models pass strict mechanical audit but mean permutation-invariant structural F1 is only **0.366**, with only **28/134** exactly matching the authored reference; in cultural settings, naming the country often changes structure with small semantic-score changes.

## Notes & Caveats
- **Selection bias:** Curated for relevance to AI/CTR; not exhaustive.
- **Timing:** Strict "last 24 hours" could not be confirmed from API results at query time; entries are drawn from the latest visible arXiv window (mostly 2026-11-10/11 submissions, plus closely related recent CTR/rec items still prominent in recent feeds).
- **Verification:** Affiliations, venues, and production details should be confirmed from PDFs/author pages before formal citation. Several CTR papers (ShopMind, SlimFM, long-sequence sponsored search) were also discussed in recent wiki digests; included here for CTR coverage and cross-reference.