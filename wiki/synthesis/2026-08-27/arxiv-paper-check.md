---
title: "arXiv Paper Check — AI & CTR (August 27, 2026)"
type: synthesis
created: 2026-08-27
updated: 2026-08-27
sources: []
tags: [arxiv, daily-check, ai, ctr, recommendation, agents, memory, multimodal, cold-start, sequential-rec, world-models, safety, daily-digest]
---

# arXiv Paper Check — AI & CTR (August 27, 2026)

Complement to same-day [arxiv-daily](arxiv-daily.md) (which covered DCEO, AMBER, TransRetrieval, CRAMER, TAGR, HSR, SWIM, HiPS, AsymSpec, Tool-Call Steering, Agentic Game Dev, Alignment Auditors — 12 papers). This check adds **6 verified-new papers** from the Aug 26–27 announcement window not found in any existing wiki digest. All IDs grep-verified absent from entire wiki before inclusion.

---

## Recommendation & CTR (3)

### DUMoE: Drift-Aware Multimodal User Representation via Sparse MoE
- **arXiv**: [2608.25773](https://arxiv.org/abs/2608.25773)
- **Authors**: Ziqing Qian, Haohang Chen, Shengqi Dang, Yuhan Xiong, Canyu Shen, Jiaying Lei, Nan Cao
- **Key Contribution**: Unified framework for drift-aware multimodal user representation. Combines (i) temporal dynamics-aware backbone (static profiles + short-term + long-term signals) with (ii) sparse MoE interest adapter where each expert models a distinct interest subspace and a gating network dynamically selects a sparse subset per user. Three-stage training decouples backbone learning, expert specialization, and gating optimization.
- **Significance**: Addresses interest drift in social media — user preferences shift across time with multi-scale temporal patterns. The sparse MoE approach to interest disentanglement is a natural extension of the production MoE trend in CTR models, applied here to user representation rather than feature interaction.

### D3ER: Disentangle and Distill Dynamic Ensemble for Multi-Modal Recommendation
- **arXiv**: [2608.25737](https://arxiv.org/abs/2608.25737)
- **Authors**: Bingnan Wang, Yi Li, Xiongxin Tang, Fanjiang Xu, Jiangmeng Li
- **Venue**: Accepted at ACMMM 2026
- **Key Contribution**: Dynamic ensemble framework that disentangles multi-modal features and distills them for recommendation. Addresses the challenge of effectively combining visual, textual, and behavioral signals in multi-modal recommendation.
- **Significance**: Multi-modal rec is converging with CTR prediction as e-commerce platforms integrate image/video/text. The distillation approach aligns with the train-time enrichment, zero-serving-cost trend seen in HARNESS-LM and GPSD.

### MOTIF: Motivation-guided Topology Inference for Cold-Start Multimodal Rec
- **arXiv**: [2608.25381](https://arxiv.org/abs/2608.25381)
- **Authors**: Yurui Shi, Yuchen Miao, Ximing Hu, Zijun Wang, Chang Han
- **Venue**: Accepted at WISE 2026
- **Key Contribution**: Infers latent topology of user motivation from multi-modal signals to address cold-start recommendation. Uses graph structure discovery to bridge the gap between content features and user preferences when interaction history is sparse.
- **Significance**: Cold-start remains a core challenge — IDProxy (Xiaohongshu) and LLM-HYPER (hypernetwork) address it from different angles; MOTIF adds a topology-inference perspective that could complement these approaches.

---

## Agent Memory & Verification (2)

### Stale Constraints in Inherited Agent Memory
- **arXiv**: [2608.25553](https://arxiv.org/abs/2608.25553)
- **Authors**: Kazuki Nakayashiki
- **Key Contribution**: Models supersession explicitly in agent memory — historical provenance is immutable, but which record is current changes. Under a scarce verification budget (2 records), agents inspected provenance paths in only ~20% of episodes. When constraints had been superseded, native allocation produced stale-consistent decisions in 74.7–77.3% of episodes. Re-assigning one verification slot to the critical path raised correct decisions by +61–74 points across 6 models.
- **Significance**: Directly relevant to Karpathy's "verification gap" concept. Memory systems need freshness/supersession signals separate from relevance — current RAG systems treat all retrieved context as equally valid regardless of temporal status. This is a rigorous negative result on agent memory safety.

### CaSKG: Counterfactual-Causal Skill Graphs for Agent Skill Retrieval
- **arXiv**: [2608.25500](https://arxiv.org/abs/2608.25500)
- **Authors**: Zhiyuan Li, Linyuan Gao, Xuechun Ding, Hongwei Chen, Yuan Wu, Yi Chang
- **Key Contribution**: Constructs counterfactual-causal skill graphs where nodes are skills and edges encode causal dependencies. Enables scalable agent skill retrieval by reasoning about which skills are causally necessary vs. merely correlated with task success.
- **Significance**: Connects to the agent skills/composition literature (SkillOpt, AutoHarness). The counterfactual-causal framing goes beyond semantic similarity for skill retrieval — "what would happen if I didn't use this skill?" rather than "does this skill look similar to my current task?"

---

## Generative Models & Reasoning (1)

### PUMA: Post-Hoc Sparsification of Universal Multimodal Embeddings
- **arXiv**: [2608.25780](https://arxiv.org/abs/2608.25780)
- **Authors**: Matteo Attimonelli, Alessandro De Bellis, Franco Maria Nardini, Claudio Pomo, Cosimo Rulli, Rossano Venturini, Tommaso Di Noia
- **Key Contribution**: Sparse autoencoder recipe that maps universal multimodal embeddings (Qwen3-VL-Embedding-2B) to compact sparse codes without retraining the backbone. Statistically indistinguishable from or improves over dense retrieval on 4/5 benchmarks. Reduces vector storage 8–16x (FP32) and up to 25x faster than exact dense scoring on large candidate pools. Identifies two failure modes of post-hoc sparsification: insufficient pre-TopK support and retrieval-misaligned active support.
- **Significance**: As multimodal embeddings scale to production (WeMM-Embedding 2B/4B/9B), inference efficiency becomes the bottleneck. PUMA's recipe could be applied to any universal embedder. The two failure-mode taxonomy is a useful diagnostic framework.

---

## Key Trends

1. **MoE interest disentanglement** — DUMoE applies sparse MoE to user representation, extending the MoE-for-CTR trend (MTmixAtt, UniMixer) from feature interaction to interest modeling.
2. **Freshness ≠ relevance** — Stale Constraints paper demonstrates that memory retrieval systems fundamentally need temporal/supersession signals, not just semantic relevance. This is an under-explored dimension in current RAG systems.
3. **Cold-start via topology, not just embeddings** — MOTIF's motivation-guided topology inference adds a structural perspective to the cold-start problem alongside embedding-based (IDProxy) and hypernetwork (LLM-HYPER) approaches.
4. **Post-hoc efficiency for multimodal embedders** — PUMA shows that sparsification can be applied after training without quality loss, offering a deployment-time optimization path separate from architecture design.
5. **Causal skill graphs** — CaSKG moves agent skill retrieval from semantic matching to causal reasoning, a direction that could improve composition reliability in multi-step agent workflows.

---

## Coverage & Dedup

- **Source**: arXiv listings for cs.LG, cs.AI, cs.IR (Thu Aug 27, 2026 announcement window = Wed Aug 26 submissions)
- **Scan**: 188 cs.LG + 209 cs.AI + 26 cs.IR = 423 entries screened
- **Overlap with arxiv-daily 08-27**: DCEO, AMBER, TransRetrieval, CRAMER, TAGR, HSR, SWIM, HiPS, AsymSpec, Tool-Call Steering, Agentic Game Dev, Alignment Auditors (12 papers) — all already covered
- **This report**: 6 papers NOT in any existing wiki digest, all IDs grep-verified absent
