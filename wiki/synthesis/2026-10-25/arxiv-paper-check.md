---
title: "arXiv Paper Check — AI & CTR (October 25, 2026)"
type: synthesis
created: 2026-10-25
updated: 2026-10-25
sources: []
tags: [arxiv, daily-check, ai, ctr, recommendation, ads, llm, agents, retrieval, ir, ranking]
---

# arXiv Paper Check — AI & CTR (October 25, 2026)

*Report generated: 2026-10-25 | Window: Recent submissions (Oct 21–25, 2026)*

## Top Picks

### 1) [Progressive Learning from Content to Relevance to Personalization for CTR Prediction](https://arxiv.org/abs/2610.29138v1)
- **Authors:** Zhiguang Yang, Yulin Yang, Fuyu Lv, Dan Ou (Alibaba)
- **Categories:** cs.IR, cs.MM
- **Published:** 2026-10-21
- **Summary:** FineSID proposes a three-stage progressive framework for multimodal CTR: (1) convert heterogeneous content to fine-grained Semantic IDs via multi-scale visual/text tokenizers, (2) query–item relevance pretraining jointly optimizing multimodal SIDs and conventional fields, (3) personalized fine-tuning on clicks.
- **Key Contributions:**
  - Unified content tokenization into fine-grained Semantic IDs aligned with ID features
  - Shared predictor across relevance pretraining and personalization
  - Demonstrated gains in CTR and business metrics; improved creative discrimination

### 2) [When Agentic Retrieval Fails Silently: Framework and Production Evidence from a Creative AI Assistant](https://arxiv.org/abs/2610.30423v1)
- **Authors:** Fergie Yan, Liang, Anuj Agarwal, Aditya Reddy Cheruku (Adobe)
- **Categories:** cs.IR
- **Published:** 2026-10-21
- **Summary:** Identifies attribution gap in agentic retrieval (agent reads results before user, delayed actions, blended outcomes). Proposes **Layered Agentic Retrieval Assessment (LARA)** with lineage schema measuring retrieval/engagement/outcome layers separately.
- **Key Contributions:**
  - Formalizes "attribution gap" for agentic assistants vs traditional ranking
  - LARA framework applicable without new modeling
  - Production analysis on Adobe Express showing different reformulation patterns (chat 44.4% vs gallery 33.1%)

### 3) [Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success](https://arxiv.org/abs/2610.31670v1)
- **Authors:** Yunfei Xie, Howard H. Qian, Shiyi Lan, Kaiyu Hang, Chen Wei
- **Categories:** cs.CV, cs.LG, cs.RO
- **Published:** 2026-10-22
- **Summary:** Proposes **Sensorimotor Alignment ($S^2$)**, a training-free offline metric measuring how well sensory representations align with physical motion geometry. Correlates with robot task success and can predict VLM backbone potential before VLA fine-tuning.
- **Key Contributions:**
  - Extends Platonic Representation Hypothesis to embodied/sensorimotor domain
  - Cheap proxy for policy evaluation without closed-loop rollouts
  - Explains observed phenomena in VLAs/world-action models

### 4) [Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity in Test-Time Reasoning](https://arxiv.org/abs/2610.31667v1)
- **Authors:** (multiple)
- **Categories:** cs.AI, cs.LG
- **Published:** 2026-10-22
- **Summary:** Addresses computational cost of test-time scaling by pruning candidate reasoning paths early. Optimizes directly for pass@$k$ (probability of finding correct solution within k) while balancing quality and diversity.
- **Key Contributions:**
  - Direct pass@$k$ optimization objective for pruning
  - Better trade-off between compute and success probability vs naive pruning
  - Relevant to efficient reasoning at scale

### 5) [Learn the Task, Not the Schedule: Reducing Spurious Cross-Arm Coupling in Bimanual Imitation Learning](https://arxiv.org/abs/2610.26507v1)
- **Authors:** (multiple)
- **Categories:** cs.RO, cs.LG
- **Published:** 2026-10-19
- **Summary:** Identifies that standard bimanual imitation learns spurious coupling from demonstration timing/schedules. Proposes approach to decouple what to do from when to do it.
- **Key Contributions:**
  - Diagnoses schedule leakage in bimanual policies
  - Improves generalization across timing variations
  - Practical for dexterous manipulation

## Emerging Trends

- **Agentic IR evaluation is maturing**: Move beyond CTR/MRR to attribution-aware metrics (LARA) that account for agent consumption patterns.
- **Content-centric CTR**: Fine-grained semantic representations (Semantic IDs) + progressive training are gaining traction as alternatives to pure ID memorization.
- **Efficient reasoning**: Direct optimization for pass@$k$ and thought pruning reflect shift toward compute-efficient test-time scaling.
- **Embodied representation alignment**: Sensorimotor alignment metrics provide new ways to evaluate foundation models pre-deployment.

## Notes
- Abstracts only; numbers/reproductions not independently verified.
- Focused on cs.AI/cs.IR/cs.LG categories with CTR/recommendation/ads/agentic relevance.
- Many recent papers (Oct 22+) show continued emphasis on evaluation, efficiency, and agentic systems.
