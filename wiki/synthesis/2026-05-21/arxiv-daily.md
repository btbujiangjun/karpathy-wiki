---
title: arXiv Daily — May 21, 2026 (AI & CTR)
type: synthesis
created: 2026-05-21
updated: 2026-05-21
sources: []
tags: [arxiv, ai, ctr, recommendation, daily-report]
---

# arXiv Daily — May 21, 2026 (AI & CTR)

New submissions from cs.AI (31 entries) and cs.IR (5 new + 11 replacements). Highlights below.

## AI

### CPO: DPO and RLHF Are Not Equivalent
**arXiv:2605.20834** | Zhiqin Yang et al.

Proves the DPO-RLHF equivalence is *conditional* on an implicit assumption that is frequently violated. When the RLHF-optimal policy does not prefer human-preferred responses, DPO optimizes relative advantage over the reference policy rather than absolute alignment. Introduces **Constrained Preference Optimization (CPO)** with provable alignment guarantees. SOTA on standard benchmarks.

### SOLAR: Self-Optimizing Lifelong Autonomous Agent
**arXiv:2605.20189** | Nitin Vetcha, Dianbo Liu

Parameter-level meta-learning agent that treats model weights as an RL environment. Outperforms baselines on common-sense, math, medical, coding, social, and logical reasoning. Accepted at AAAI 2026.

### PlanningBench: Scalable Planning Data for LLMs
**arXiv:2605.20873** | Ziliang Zhao et al.

Framework for generating diverse, verifiable planning data across 30+ task types. RL on PlanningBench data improves performance on unseen planning benchmarks. Reveals frontier LLMs still struggle with coupled constraints.

### AgentCo-op: Retrieval-Based Multi-Agent Workflows
**arXiv:2605.20425** | Shuaike Shen et al.

Composes reusable skills, tools, and agents into executable workflows via typed artifact handoffs. Applies local repair on failure. SOTA on 4/6 coding/math/QA benchmarks with lower per-task cost.

### Conflict-Aware Guidance for Flow Models
**arXiv:2605.20758** | Xuehui Yu et al. | ICML 2026

Identifies root cause of off-manifold drift in compositional guided diffusion/flow sampling — gradient misalignment. Proposes **Conflict-Aware Additive Guidance** that dynamically detects and resolves gradient conflicts. Beats baselines in generation fidelity.

### AutoRPA: LLM-Driven GUI Automation
**arXiv:2605.21082** | Minghao Chen et al. | ICML 2026

Distills ReAct-style agent decision logic into robust RPA functions via translator-builder pipeline and hybrid repair. Reduces token usage by 82–96% on similar tasks.

### ScenePilot: Boundary-Driven Scenario Generation
**arXiv:2605.21168** | Qiyu Ruan et al.

Generates physically-valid yet autonomy-stressing driving scenarios via constrained multi-objective RL. +6.2 pp collision rate while preserving physical validity.

## CTR / Recommendation

### UG-Sep: Compute Only Once (ByteDance)
**arXiv:2602.10455** (replaced) | Hui Lu et al.

User-Group Separation framework for TokenMixer-based dense interaction models. Disentangles user/item information flows so user-side computation is reusable across samples. **Reduces inference latency by up to 20%** across Douyin Feed, Ads, and Qianchuan at ByteDance. Combines with W8A16 quantization for additional acceleration.

### Generative Long-term User Interest Modeling for CTR
**arXiv:2605.15905** (May 15) | Jiangli Shao et al.

Generative approach to long-term user interest modeling. Uses diffusion to generate behavior representations rather than matching directly. Addresses incomplete/biased interest from target-centered retrieval.

### TriRec: Tri-party LLM-agent Recommendation
**arXiv:2603.10673** (replaced) | Yaxin Gong et al.

First tri-party (user, item, platform) LLM-agent recommendation framework. Item agents self-promote to improve matching and cold-start. Consistent gains in accuracy, fairness, and item-level utility.

### Layer-wise Token Compression (LTC) for Reranking
**arXiv:2605.20683** | Shengyao Zhuang et al. | SIGIR 2026

Adaptive token pooling at intermediate transformer layers for cross-encoder rerankers. Up to 25% QPS gain for passage ranking, **116% for document ranking**. Compression acts as a beneficial regularizer on long documents.

### MemConflict: Long-Term Memory Under Conflicts
**arXiv:2605.20926** | Zhen Tao et al.

Diagnostic framework for LLM memory systems under temporal, factual, and contextual conflicts. Evaluates 6 systems — uneven strengths across conflict types; answer correctness diverges from retrieval quality.

### CALMem: Application-Layer Dual Memory
**arXiv:2605.20724** | Rajendra Narayan Jena et al.

Episodic + semantic memory for LLM conversational assistants. Pure application-layer — no model modification needed. Intra-session retrieval of compacted-away turns is a key contribution.

## Notable Trends

- **Alignment theory tightening**: CPO shows DPO's equivalence to RLHF is fragile — expect more work on provable alignment.
- **Recommendation systems going generative**: CTR prediction is shifting from discriminative feature-interaction to generative paradigms (UG-Sep, Generative Long-term Interest).
- **LLM agents for everything**: 50%+ of cs.AI new submissions involve multi-agent frameworks or tool-use agents.
- **Memory as a first-class IR problem**: MemConflict and CALMem signal growing maturity in long-term memory evaluation for conversational AI.
