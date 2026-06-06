---
title: arXiv Paper Check — AI & CTR (June 6, 2026)
type: synthesis
created: 2026-06-06
updated: 2026-06-06
sources: []
tags: [arxiv, ai, ctr, recommendation, survey]
---

# arXiv Paper Check — AI & CTR (June 6, 2026)

> Surveyed: cs.AI (108 new + 172 cross, Fri 5 Jun), cs.LG (232 entries, Fri 5 Jun), cs.IR (20 entries, Fri 5 Jun), and RSS/live listings for Sat 6 Jun.

---

## CTR & Recommendation Systems

| Paper | Authors | Key Contribution |
|-------|---------|-----------------|
| **DS-MLP** (2606.04944) | Mao et al. | Dual-Stream MLP for CTR. Knowledge distillation consolidates explicit feature interactions into a main MLP + parallel MLP for implicit interactions. SOTA on Criteo/Avazu/Movielens. Efficient vanilla MLP at inference. |
| **GenLI** (2605.15905) | — | Generative long-term user interest modeling. Target-independent interest generation + O(1) behavior retrieval. Deployed at Meituan. +0.776% CTR, +1.567% RPM online. |
| **LoopCTR** (2604.19550) | — | Loop scaling paradigm: recursive layer reuse via shared parameters. Train-multi-loop, infer-zero-loop. New SOTA across Amazon/KuaiVideo/TaobaoAds. 0.02–0.04 AUC headroom revealed. |
| **EST** (2602.10811) | — | Efficiently Scalable Transformer for CTR. Lightweight Cross-Attention + Content Sparse Attention. Unified sequence modeling. Deployed at Taobao display ads. +3.27% RPM, +1.22% CTR. |
| **HeMix** (2602.09387) | Wang et al. | Query-Mixed Interest Extraction + HeteroMixer block. Deployed at AMAP. +3.61% GMV, +2.78% PV_CTR. Scaling behavior demonstrated. |
| **PRECTR-V2** (2602.20676) | Cao et al. | Unified Relevance–CTR framework. Cross-user preference mining, exposure bias correction, LLM-distilled encoder. |
| **SparseCTR** (2601.17836) | Lai et al. | Three-branch sparse self-attention for long-term user behaviors. Scaling law across 3 OOM FLOPs. +1.72% CTR online. |
| **BAHSD** (2606.03091) | Zhou et al. | Adaptive distillation for black-box sequential recommendation. Addresses long-tail head solidification. |

## AI / LLM Systems

| Paper | Authors | Key Contribution |
|-------|---------|-----------------|
| **Agents' Last Exam (ALE)** (2606.05405) | Sun, Han et al. (250+ coauthors) | Benchmark for economically valuable long-horizon tasks. 55 subfields, 13 industry clusters, 1K+ tasks. Avg pass rate: 2.6%. Living benchmark. |
| **LeanMarathon** (2606.05400) | Zhang et al. | Multi-agent harness for research-level Lean autoformalization. Proved 258 lemmas/theorems across 4 Erdős problems. No sorry. |
| **PACT** (2606.05304) | Huang et al. | Protocolized Action-state Communication for MAS. Treats inter-agent communication as public state update. Lifts OpenHands resolve rate at -10% tokens. |
| **OpenWebRL** (2606.02031) | Yang et al. | Open-source online multi-turn RL for visual web agents. Demystifies RL training for web agents. |
| **Image Generators are Generalist Vision Learners** (2604.20329) | Gabeur et al. (Google/DeepMind) | Image/video generators exhibit zero-shot visual understanding behaviors akin to LLM emergent capabilities. |
| **Toto 2.0** (2605.20119) | Khwaja et al. (Salesforce) | Time series foundation models scale: 4M→2.5B parameters. 5 open models. New SOTA on GIFT-Eval. |
| **Exact Linear Attention (ELA)** (2605.18848) | Ou | Linear complexity Transformer attention via exact kernel decomposition. No approximation error. |
| **SentinelBench** (2606.05342) | Maldaner et al. (Microsoft) | 100-task benchmark for long-running monitoring agents across 10 synthetic web environments. |
| **HypRAG** (2602.07739) | Madhu et al. | Hyperbolic dense retrieval for RAG. Hierarchical structure preservation outperforms Euclidean retrievers. |
| **Escaping the Verifier** (2511.21667) | Cai, Ryabinin, Provilkov | Learning to reason via demonstrations when verifiers are unavailable. Alternative to RL-based reasoning training. |
| **Soft Sequence Policy Optimization** (2602.19327) | Glazyrina et al. | New RL alignment method with sequence-level importance sampling weights. Improves on GRPO. |
| **Rollout-Level Advantage-Prioritized ER for GRPO** (2606.04560) | Yoo et al. | Experience replay for GRPO. Addresses sample inefficiency in reasoning LLM post-training. |
| **Do Transformers Need Three Projections?** (2606.04032) | Kayyam et al. | Systematic study of QKV variants. Analyzes impact of omitting Q/K/V projections. |
| **The Topological Trouble With Transformers** (2604.17121) | Mozer, Siddiqui, Liu | Fundamental limitation: transformers' feedforward architecture limits dynamic state tracking. |
| **GITCO** (2606.05332) | Pandey et al. | Inference-time context optimization for TimesFM. +1.95% MASE via selective patch suppression. |
| **TimeClaw** (2606.05404) | Li et al. | Agentic harness for contextualized time series reasoning. Integrates temporal tools with LLM agents. |
| **A2RAG** (2601.21162) | Liu et al. | Adaptive Agentic Graph RAG. Cost-aware, mixed-difficulty workload handling. |
| **Synthetic Contrastive Reasoning** (2606.05382) | Singh et al. | CPO for multi-table QA. +9.7–16.3% over SFT across Qwen3/Mistral/Llama. |
| **Mutation Without Variation** (2606.05408) | Gurkan et al. | LLM program mutation converges to attractors. 87% chains revisit previous structural forms. |
| **Stability vs. Manipulability** (2606.05384) | Dutta, Moharir | LLM judges are reversible under post-decision challenge. New ERS metric. |

---

## Key Highlights

1. **CTR scaling heats up** — Five notable CTR papers (DS-MLP, LoopCTR, EST, HeMix, SparseCTR) all from major industrial labs (Taobao, AMAP, Meituan). Shift toward unified sequence modeling and scaling laws for CTR.

2. **Agents' Last Exam sets a low bar** — 2.6% pass rate on economically valuable tasks. 250+ experts contributed. Signals massive headroom for agentic systems.

3. **LeanMarathon proves AI co-mathematician is viable** — 258 lemmas, 0 sorries across 4 Erdős problems. Multi-agent orchestration beats single-shot approaches.

4. **Emergent visual understanding from generators** — Google/DeepMind shows image generators have zero-shot visual understanding, mirroring LLM emergence.

5. **Transformers' fundamental limits** — Mozer et al. prove transformers have inherent topological trouble with state tracking. Implies architectural innovations needed beyond attention.

6. **LLM program evolution converges** — 87% of mutation chains revisit previous structures. Suggests fundamental limits on LLM-driven open-ended discovery without diversity mechanisms.
