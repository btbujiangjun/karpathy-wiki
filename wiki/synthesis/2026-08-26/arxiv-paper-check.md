---
title: "arXiv Paper Check — AI & CTR (August 26, 2026)"
type: synthesis
created: 2026-08-26
updated: 2026-08-26
tags: [arxiv, daily-check, ai, ctr, recommendation, agents, memory, efficiency, safety, finance, daily-digest]
---

# arXiv Paper Check — AI & CTR (2026-08-26)

> Complement to same-day arxiv-daily and arxiv-ai-search digests. Papers below are **not** covered in those reports. All IDs grep-verified absent from sibling digests before inclusion.

---

## 1. AI Agents & Memory

### 1.1 AgentWeave: Routing Before Reasoning for Efficient Function Calling in Tool-Rich Language Models

- **Authors:** Saurav Singla et al.
- **arXiv:** [2608.23078](https://arxiv.org/abs/2608.23078) (cs.AI, submitted 2026-08-24)
- **Key Innovation:** Introduces a deterministic pre-inference routing layer that constructs a bounded model-visible action space *before* LLM inference, using eligibility, requirement, capability, and routing signals. On 48 BFCL V4 multiple-function tasks, AgentWeave achieves 12.5% success (6/48) vs 0% for all-tools/random/semantic baselines, while presenting **70.18% fewer tools**, using **61.70% fewer tokens**, and **50.95% lower latency**. Demonstrates that candidate-space construction materially affects fixed model function-calling behavior.
- **Why it matters:** Routing as a distinct stage before reasoning is underexplored; this is a clean ablation showing that *what you show the model* matters as much as *how you prompt it*.

### 1.2 CONTRAMEM: Learning Self-Evolving Procedural Memory from Contrasting Multi-Model Trajectories

- **Authors:** (Multi-institutional)
- **arXiv:** [2608.22533](https://arxiv.org/abs/2608.22533) (cs.AI, submitted 2026-08-23)
- **Key Innovation:** Uses same-task outcome variation across multiple source models (GPT-5.5, Claude Sonnet 4.6, DeepSeek V4 Pro) as supervision to distill a compact bank of Function Cards and Skill Cards. More than **doubles held-out success** on GAIA2/ARE (26.2% → 55.3%), with consistent per-model gains. The memory bank transfers unchanged to an unseen target model (Qwen3.7 Plus: 18.5% → 35.5%). Heterogeneous multi-model trajectories yield stronger memory than same-model multi-rollout — the margin comes from **contrastive behavioral diversity**, not stronger source agents or more sampling.
- **Why it matters:** Procedural memory for agents without model training; cross-model heterogeneity as a quality signal is a novel insight.

### 1.3 UniMem: Unifying Multimodal Memory and Control for Vision-Language-Action Models

- **Authors:** Lostenberg et al.
- **arXiv:** [2608.22869](https://arxiv.org/abs/2608.22869) (cs.RO, submitted 2026-08-24)
- **Key Innovation:** Unifies high-level multimodal memory and low-level control under a single VLA backbone. Uses an event classifier for memory updates, a keyframe encoder for dense spatial memory, and a keyframe caching technique to minimize overhead. Achieves **93.4% simulation success** (vs 68.2% fixed-window baseline) and **80.0% hardware success** (vs 43.5% hierarchical baseline) across 9 tasks targeting sequential and spatial memory. Avoids the memory bottleneck and high latency of dual-system architectures.
- **Why it matters:** Single-model memory for robotics; eliminates the need for additional VLMs for long-term memory management.

---

## 2. AI Safety & Robustness

### 2.1 Walking on the DARKSIDE: Coherence Auditing for LLM-Generated Knowledge Graphs

- **Authors:** Aldo Gangemi, Emanuele Bottazzi
- **arXiv:** [2608.23370](https://arxiv.org/abs/2608.23370) (cs.AI, submitted 2026-08-24)
- **Key Innovation:** Formalizes a coherence auditing method on top of Logic-Augmented Generation (LAG). Introduces an explicit data structure of accumulated exclusions over discourse time, with a warrant axis classifying each referent as Warranted, Unattested, Misattributed, or Fabricated. The DelegationRiskAssessment escalates to UNSAFE when fabricated rate is positive or unsupported rate exceeds a threshold. Evaluated on BSBench (100-item adversarial corpus of sophisticated-sounding nonsense across 5 domains) using Gemini 3 + Claude Sonnet 4.6 as independent judge. The XKG functions as "missing memory" and the warrant axis as an "epistemic firewall."
- **Why it matters:** Addresses a real vulnerability: sophisticated nonsensical input gets reified into knowledge graphs alongside legitimate triples, undetectable by automated reasoners.

---

## 3. AI Efficiency & Agent Infrastructure

### 3.1 SparseRead: Token-Efficient Sparse Reading for AI Agents

- **Authors:** Zedong Liu et al.
- **arXiv:** [2608.22237](https://arxiv.org/abs/2608.22237) (cs.AI, submitted 2026-08-23)
- **Key Innovation:** Training-free, model-transparent reading layer that controls content admission *before* unnecessary evidence reaches the model context. Combines a regime-aware Read Gate, extensible Reader Backends, and a stateful protocol for bounded, source-anchored evidence acquisition with explicit refinement, verification, stopping, and fallback. Across 6 frontier models (including Claude Opus 5) and 5 workload scenarios, reduces token volume by **up to 92.9%** and wall time by **up to 89.0%**, while preserving or improving task quality. Consistent gains across 3 agent frameworks demonstrate broad portability.
- **Why it matters:** Over-reading is a systemic problem in agents; this is a principled intervention at the admission layer, not post-hoc compression.

---

## 4. Finance & AI

### 4.1 The Axiomatic Trader: Latent Regularity, Information Budgets, and the Canonical Form of a Quantitative Investment System

- **Authors:** Jiayu Li et al.
- **arXiv:** [2608.23416](https://arxiv.org/abs/2608.23416) (cs.LG, submitted 2026-08-24)
- **Key Innovation:** Formalizes systematic trading around one article of faith — that regularities found in the past persist — as a time-invariant mechanism driven by an unobserved latent state. Shows that five constants (recurrence bound, invariance defect, coherence times, signal ceiling, regime-contingent fraction) nearly force the architecture of a correct quantitative investment system. Provides a mathematical foundation for why certain quantitative strategies work and others fail.
- **Why it matters:** Rare rigorous theoretical framework bridging signal processing, information theory, and trading system design.

---

## Summary

| Category | Papers | Key Theme |
|----------|--------|-----------|
| AI Agents & Memory | 3 | Pre-inference routing, contrastive procedural memory, unified VLA memory |
| AI Safety | 1 | Epistemic firewall for knowledge graph coherence |
| AI Efficiency | 1 | Token-efficient sparse reading (up to 92.9% reduction) |
| Finance & AI | 1 | Mathematical foundation for quantitative trading systems |

**Total:** 6 papers, all IDs grep-verified absent from wiki. Zero overlap with same-day arxiv-daily/arxiv-ai-search.

**Cross-cutting observation:** The agent efficiency cluster (AgentWeave + SparseRead + ContraMem) converges on the same principle: *reduce what the model sees before inference* — whether via routing, sparse reading, or distilled procedural memory. This "front-loading intelligence" pattern is becoming a distinct design philosophy separate from model scaling.
