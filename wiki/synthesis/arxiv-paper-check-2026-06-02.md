---
title: arXiv Paper Check — 2026-06-02
type: synthesis
created: 2026-06-02
updated: 2026-06-02
sources: []
tags: [arxiv, paper-review, ctr, recommendation, ai, llm, rag, agents]
---

# arXiv Paper Check — 2026-06-02

Scan of cs.AI, cs.IR, and cs.LG new listings from Mon 1 Jun 2026. 36 entries in cs.AI, 12 in cs.IR, 171 in cs.LG.

---

## CTR / Recommendation / Ranking

| Paper | Authors | Venue | Key Contribution |
|-------|---------|-------|-----------------|
| **Graph-GRPO** (2605.31003) | Che et al. | CIKM 2026 | Extends GRPO with dependency-aware credit assignment for generative e-commerce search relevance. Models CoT reasoning steps as a dependency graph; propagates outcome rewards over edges for fine-grained step-level credit. Online A/B verified. |
| **SaFeAU / Semantic Factor Learning** (2605.31414) | Yu et al. | KDD 2026 | Beyond instance-level alignment: disentangles item representations into independent semantic factors via routing. Mitigates false negatives in CF by matching uninteracted items that share semantic factors with interacted ones. Outperforms GCN-based SOTA on sparse datasets at MF-level efficiency. |
| **Climber-Pilot** (2605.06235, replaced) | Guo et al. (14 authors) | — | Non-myopic generative recommendation from NetEase Cloud Music. Time-Aware Multi-Item Prediction (TAMIP) distills long-horizon foresight; Condition-Guided Sparse Attention (CGSA) enforces business constraints during generation. +4.24% core business metric in online A/B. |
| **HERec** (2411.13865, replaced) | Ma et al. | KDD 2026 | Hyperbolic framework balancing exploration/exploitation in recommenders. Semantic-enhanced hyperbolic alignment + automatic hierarchical clustering via Dasgupta's cost. +5.49% utility, +11.39% diversity. Addresses information cocoons. |
| **FOSTER** (2605.30772) | Tran et al. | — | First-order dataset distillation for text-based sequential recommendation. Stochastic item subset sampling + trajectory-anchored parameter reset bypasses bi-level optimization cost. Approximates full-dataset performance with as few as 20 synthetic sequences. |
| **Aligning Dense Retrievers with LLM Utility** (2604.22722, replaced) | Sandhu et al. | — | Utility-Aligned Embeddings (UAE): trains bi-encoder to imitate LLM-perplexity-derived utility distribution via Utility-Modulated InfoNCE. 180× faster than LLM re-ranking, +30.6% Recall@1 on QASPER. |

## AI / LLM Systems

| Paper | Authors | Venue | Key Contribution |
|-------|---------|-------|-----------------|
| **UniScale** (2605.30898) | Huang et al. | ICML 2026 | Unifies model routing and test-time scaling as a multi-armed bandit problem. LinUCB-based online policy learns when to route to larger models vs. allocate more inference compute. Fine-grained quality-cost trade-off across dynamic scenarios. |
| **SLAT** (2605.30832) | Yao et al. | — | Segment-Level Adaptive Trimming for efficient CoT. Identifies high-probability segments with low marginal utility as "overthinking." RL framework selectively suppresses redundant segments, reducing reasoning length by 50% while maintaining accuracy. |
| **VeriGate** (2605.30451) | Agrawal, Liu, Huang | — | Verifier-gated step-level GRPO. Keeps verifier in charge when rewards are informative; falls back to process supervision (PRM) when verifier rewards degenerate. Converts PRM scores into future-cumulated rewards. +20% accuracy on 1.5B, +12% on 7B models across 6 reasoning benchmarks. |
| **COMPASS** (2605.30838) | Shen et al. | — | Cognitive MCTS-Guided Process Alignment for safe search agents. Uses MCTS to synthesize stealthy attack trajectories; introspective step-wise alignment isolates risky intermediate actions. Safety-utility trade-off with less training data. |

## Agentic Systems

| Paper | Authors | Venue | Key Contribution |
|-------|---------|-------|-----------------|
| **Harness Updating ≠ Harness Benefit** (2605.30621) | Lin et al. (16 authors) | — | Disentangles two capabilities in self-evolving LLM agents: harness-updating is flat in base capability (even small models produce useful updates), harness-benefit is non-monotonic (mid-tier models benefit most). Key finding: invest capability budget in the task-solving agent, not the evolver. |
| **MAVEN** (2605.30738) | Ghugarkar et al. | — | Lightweight symbolic reasoning scaffold for agentic tool calling. Improves GPT-OSS-120b from 48% → 71% on MAVEN-Bench without additional training. Competitive with frontier proprietary models at ~1/10 cost. |
| **AdaCoM** (2605.30785) | Yi et al. | — | Adaptive Context Management for long-horizon agents. External LLM manages frozen agent's context via RL. Reveals Fidelity-Reliability Trade-off: high-performing agents need fidelity, low-performing need aggressive compression. |
| **DecomposeR** (2605.30824) | Hussain, Wu, Yao | — | Planner-centric RL for deep research. Represents research plans as typed DAGs; separate RL stages for planning and answer synthesis. +5.1–8.0 points on long-form benchmarks over comparable open baselines. |

## IR / RAG / Retrieval

| Paper | Authors | Venue | Key Contribution |
|-------|---------|-------|-----------------|
| **DynaTree** (2605.31377) | Qi et al. | — | Two-stage agentic retrieval for time-sensitive news. Offline: coordinated agents build reusable retrieval tree. Online: lightweight daily subtree selection without agentic reasoning. Deployed at Syft; improves survival rate from 0.32–0.53 → 0.59–0.73. |
| **V-SPLADE** (2605.30917) | Cho et al. (7 authors) | — | First inference-free multimodal learned sparse retriever for visual documents. Caption-gated token supervision activates retrieval-relevant vocabulary dimensions. +13.8pp NDCG@5 over dense baseline; 2× R@5 on 18.7M corpus. |
| **On the impact of retrieved content representations in RAG** (2605.30790) | Ross et al. | ACL 2026 ARR | Controlled study of 14 document representations (selection, summarisation, reformulation). Key finding: **answer retention** is the primary determinant of generator accuracy — when retention is high, wording/length/query-dependence have limited effect. |
| **MIMO** (2605.31171) | Jang, Hong, Lim | — | Multilingual IR via monolingual objectives. Two-stage: English teacher model anchors cross-lingual alignment via distillation, then joint optimization of distillation + cross-lingual contrastive learning. Resolves trade-off between alignment and uniformity. |

## Data & Benchmarks

| Paper | Authors | Venue | Key Contribution |
|-------|---------|-------|-----------------|
| **EHRBench** (2605.30637) | Xie et al. | KDD 2026 Oral | 1M QA items from EHR trajectories for clinical decision-making. Automated EHR-LLM-KB pipeline for scalable construction. Benchmarks 30+ LLMs on diagnosis, treatment, and prognosis. |
| **SPECTRA** (2605.31575) | Liang | — | Synthetic IR test collection framework with relevance oracles and controlled distractor diagnostics. 60K docs / 9.6M tokens generated at ~12-14K docs/sec. Exposes scaling and failure modes before costly collection construction. |
| **PhyDrawGen** (2605.30512) | Haque et al. | EMNLP 2026 | Neuro-symbolic pipeline for physics diagram generation. LLM → scene graph → deterministic PSLG solver → VLM propose-verify loop. Outperforms GPT-5-image, Gemini 2.5 Flash, Gemini 3 Pro on 1,449 physics problems. |
| **BilliardPhys-Bench** (2605.30900) | Wang et al. | — | Benchmark for physical reasoning in MLLMs. Tests collision prediction, wall bounces, final positions. Reveals "stasis bias": when correct outcome is hard to infer, models predict no interaction. |

## Notable Mentions

- **Vector Linking** (2605.31100, ICML 2026): cross-model embedding correspondence via local isometric consistency. Applications to vector DB integration.
- **LLM-FACETS** (2605.31167): privacy-preserving LLM evaluation framework aligned with EU AI Act stakeholder roles.
- **LongDS-Bench** (2605.30434): benchmark exposing long-horizon state tracking failures in agentic data analysis — best model reaches only 48.45%.
- **Feedback Distillation** (2605.30861): distills LLM privileged feedback for Lean theorem proving; maintains higher trajectory diversity than GRPO.

---

## Summary

Today's arXiv was heavy on **agentic systems** — the most striking finding is the Harness Updating vs. Harness Benefit paper showing that mid-tier models benefit most from evolved harnesses, and that update quality is surprisingly flat across model scales. On the **CTR/rec** side, Graph-GRPO and SaFeAU (both at KDD/CIKM 2026) represent continued progress in RL-based generative retrieval and semantic disentanglement for CF. The **SLAT** and **VeriGate** papers both tackle the efficiency-of-reasoning problem from different angles — segment-level trimming and verifier-gated process rewards. **UniScale** (ICML 2026) is a clever unification of model routing + test-time compute scaling that deserves attention from anyone running LLM inference at scale.
