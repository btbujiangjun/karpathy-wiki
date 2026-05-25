---
title: Affiliation Landscape — AI Research by Institution (2025-2026)
type: synthesis
created: 2026-05-25
updated: 2026-05-25
sources: [arxiv-broad-2026-05-25.md]
tags: [affiliation, landscape, google, meta, microsoft, bytedance, alibaba, tencent, kuaishou, nvidia]
---

# Affiliation Landscape — AI Research by Institution (2025-2026)

> Analysis of technical directions and evolutionary trends across major companies and research institutions, based on ~121 recent arXiv papers.

---

## 1. Google DeepMind

**Papers**: 4+ (Decoupled DiLoCo, SML, SPINAL co-author, Efficient Exploration)

| Direction | Key Work | Technical Route |
|-----------|----------|-----------------|
| Distributed Training | Decoupled DiLoCo (2604.21428) | Fully asynchronous learners with chaos engineering; 88% goodput under failures |
| Social Meta-Learning | SML (2602.16488) | Online RL for learning from language feedback; cross-domain transfer (math→code) |
| Alignment Diagnostics | SPINAL (2601.06238, co-author) | Layerwise geometric diagnostic for DPO alignment |
| RLHF Scaling | Efficient Exploration (2603.17378) | Online uncertainty-guided exploration; RLHF scaling laws |

**Evolution**: Google DeepMind is focused on infrastructure scaling (Decoupled DiLoCo for geo-distributed training) and post-training methodologies (SML for interactive learning). The "bitter lesson" framing in Decoupled DiLoCo suggests a strategic bet on algorithms that exploit massive compute. Post-training work (SML, Efficient Exploration) emphasizes sample efficiency and generalization rather than raw scale.

---

## 2. NVIDIA

**Papers**: 4+ (Megatron Core MoE, Swimba, TMPC, DiLaDiff)

| Direction | Key Work | Technical Route |
|-----------|----------|-----------------|
| MoE Systems | Megatron Core (2603.07685) | Production MoE training; 1,233 TFLOPS/GPU for DeepSeek-V3-685B |
| MoE + SSM | Swimba (2603.06938) | MoE-parameterized SSM; single-pass recurrence; 14B model |
| Test-time Alignment | TMPC (ICLR 2026) | MPC-inspired inference-time alignment; hierarchical RL principles |
| Diffusion LM | DiLaDiff (2605.23605) | Distilled latent-augmented diffusion for language |

**Evolution**: NVIDIA's research spans the full stack from systems (Megatron Core) to architecture (Swimba) to inference-time methods (TMPC). The Swimba work represents a novel convergence of MoE and state-space models, while Megatron Core positions NVIDIA as the infrastructure provider for the MoE era. TMPC shows movement into alignment methodology.

---

## 3. Microsoft (Bing Ads / Research Asia)

**Papers**: 3+ (AdNanny, SkillOpt, Inductive Deductive Synthesis co-author)

| Direction | Key Work | Technical Route |
|-----------|----------|-----------------|
| Unified Ads LLM | AdNanny (2602.01563) | Single 671B reasoning LLM for all offline ads tasks; SFT + RL alignment |
| Agent Skills | SkillOpt (2605.23904) | Self-evolving agent skills via structured optimization |
| Verified Synthesis | Inductive Deductive Synthesis (2605.23109, co-author) | Combines inductive and deductive reasoning for verified systems |

**Evolution**: Microsoft is applying LLM reasoning capabilities to ads infrastructure (AdNanny replaces task-specific models with a unified reasoning backbone). Research Asia contributes to agent skill learning (SkillOpt). The verified synthesis work (with UC Berkeley) targets formal methods integration.

---

## 4. ByteDance

**Papers**: 5+ (LONGER, OneTrans, HAP, Precise, CST)

| Direction | Key Work | Technical Route |
|-----------|----------|-----------------|
| Long Sequence Rec | LONGER (2505.04421) | Long-sequence transformer for Douyin; global tokens + hybrid causal attention |
| Unified Rec Backbone | OneTrans (2510.26104) | Unified feature interaction + sequence modeling; 5.68% GMV lift |
| Pre-ranking | HAP (2603.03770) | Heterogeneity-aware pre-ranking; deployed on Toutiao for 9 months |
| Flow-Matching RL | Precise (2605.23522) | SDE-consistent sampling for flow-matching RL |
| Scaling CTR | EST (2602.10811) | Power-law scaling in CTR; Lightweight Cross-Attention |

**Evolution**: ByteDance leads in industrial recommendation scaling, with a clear trajectory from separate sequence/feature models (LONGER, OneTrans) toward unified architectures. The EST work establishes power-law scaling in CTR. Precise represents a novel direction combining flow-matching with RL for controllable generation.

---

## 5. Alibaba Group

**Papers**: 7+ (EST, GFlowGR, RARE, LBM, DAIAN, HeMix, DyDiT++)

| Direction | Key Work | Technical Route |
|-----------|----------|-----------------|
| Ad Retrieval | RARE (2504.01304) | LLM-generated Commercial Intentions for real-time retrieval; 5.04% consumption lift |
| CTR Scaling | EST (2602.10811) | Power-law CTR scaling; deployed on Taobao display ads |
| Generative Rec Fine-tuning | GFlowGR (2506.16114) | GFlowNet-based fine-tuning; 1% annual revenue lift since May 2025 |
| Auto-bidding | LBM (2603.05134) | Hierarchical LLM auto-bidding; LBM-Think + LBM-Act + GQPO |
| Intent-Aware CTR | DAIAN (2602.13971) | Intent myopia mitigation for trigger-induced recommendation |
| Scalable CTR | HeMix (2602.09387) | Query-mixed interest extraction; deployed on AMAP |
| Efficient Diffusion | DyDiT++ (2504.06803) | Dynamic computation for DiT; 51% FLOPs reduction |

**Evolution**: Alibaba's research spans the full recommendation pipeline (retrieval → pre-ranking → ranking → auto-bidding). The GFlowGR deployment on Taobao represents a novel training paradigm for generative recommenders. DyDiT++ shows their investment in efficient generative models.

---

## 6. Tencent

**Papers**: 3+ (RankUp, OneRanker, Foundation Protocol co-author)

| Direction | Key Work | Technical Route |
|-----------|----------|-----------------|
| High-Rank CTR | RankUp (2604.17878) | Embedding collapse mitigation; +3.41% GMV on Weixin |
| Generative Ranking | OneRanker (2603.02999) | Unified generation + ranking; K/V pass-through; +1.34% GMV |
| Agent Protocol | Foundation Protocol (2605.23218, co-author) | Agentic society coordination protocol |

**Evolution**: Tencent is transitioning from traditional ranking (RankUp's representation improvement) to generative approaches (OneRanker's unified generation-ranking). The agent protocol work (with HKUST/UIUC) represents a longer-term bet on multi-agent systems.

---

## 7. Kuaishou

**Papers**: 5+ (OneMall, OneRec-V2, GR4AD, DualGR, MaRI)

| Direction | Key Work | Technical Route |
|-----------|----------|-----------------|
| Generative E-commerce Rec | OneMall (2601.21770) | End-to-end generative; +14.7% GMV; 400M DAU |
| Generative Rec Pipeline | OneRec-V2 (2508.20900) | Lazy decoder-only; preference alignment; 0.467-0.741% stay time |
| Ad Generative Rec | GR4AD (2602.22732) | UA-SID + LazyAR + RSPO; 4.2% ad revenue improvement |
| Generative Retrieval | DualGR (2511.12518) | Dual-branch long/short-term; exposure-aware loss |
| Inference Acceleration | MaRI (2602.23105) | Structural re-parameterization; 1.3× speedup |

**Evolution**: Kuaishou is arguably the most aggressive adopter of generative recommendation at scale. From OneRec to OneRec-V2 to OneMall to GR4AD, the trajectory shows rapid iteration. DualGR adds generative retrieval to complement generative ranking. MaRI addresses the efficiency bottleneck of generative models.

---

## 8. Other Industry

| Company | Key Paper | Direction |
|---------|-----------|-----------|
| Netflix | Generative Recommender Scaling (2605.23312) | Scaling generative recommenders to 1B params |
| LinkedIn | CADET (2602.11410), LLM Ad Retrieval (2605.21969) | Decoder-only CTR + semantic ad retrieval |
| LinkedIn | LLM Retrieval for Stable Ads (2605.21969) | Semantic candidate generation for ad stability |
| Walmart | Unified Supervision for Sponsored Search (2604.07930) | Bi-encoder training with unified supervision |
| Meituan | PRECTR-V2 (2602.20676), KP-Agent (2601.05257) | Unified relevance-CTR + agentic keyword pruning |
| Xiaohongshu | IDProxy (2603.01590) | MLLM cold-start CTR proxy embeddings |
| Baidu | GRAB (2602.01865) | Generative CTR with CamA attention |
| Salesforce | AutoResearch AI (2605.23204) | Research automation agents |
| Arcee AI | Trinity Large (2602.17004) | Open-weight 685B MoE with Muon optimizer |
| PORTULAN | CLARIN-PT-LDB (2603.12872) | Portuguese LLM leaderboard |

---

## 9. Academia

| Institution | Key Paper | Direction |
|-------------|-----------|-----------|
| CMU | ImProver 2 (2605.22885) | Neurosymbolic proof optimization |
| MIT | Dimensionality Barrier (2605.23556) | Retrieval theory |
| UC Berkeley | Inductive Deductive Synthesis (2605.23109) | Verified program synthesis |
| CityU HK | GFlowGR (2506.16114, co-author) | Generative Rec fine-tuning |
| NTU Singapore | OneTrans (2510.26104, co-author) | Unified recommendation backbone |
| NYCU | TMPC (ICLR 2026, co-author) | Test-time alignment |
| IIIT Ranchi | SPINAL (2601.06238, co-author) | Alignment diagnostics |

---

## 10. Cross-Institution Collaboration Patterns

| Collaboration | Papers | Domain |
|--------------|--------|--------|
| Tencent + HKUST + UIUC | Foundation Protocol (2605.23218) | Multi-agent systems |
| UC Berkeley + Microsoft | Inductive Deductive Synthesis (2605.23109) | Verified program synthesis |
| Alibaba + CityU HK | GFlowGR (2506.16114) | Generative recommendation |
| ByteDance + NTU | OneTrans (2510.26104) | Recommendation systems |
| NVIDIA + NYCU | TMPC (ICLR 2026) | Test-time alignment |
| Google DeepMind + Google Research | Decoupled DiLoCo (2604.21428) | Distributed training |

**Pattern**: Industry-academia collaboration is most active in recommendation systems and agent systems. Chinese tech companies (Alibaba, ByteDance, Kuaishou, Tencent) disproportionately dominate recommendation/CTR research. US-based research focuses more on LLM training theory, alignment, and fundamental sequence modeling.

---

## Key Insights

1. **Generative Recommendation is industry-standard**: Kuaishou (OneRec/OneMall/GR4AD), ByteDance (OneTrans), Netflix, and Alibaba (GFlowGR) have all deployed generative recommenders in production.

2. **CTR scaling laws emerge**: EST (Alibaba) and LoopCTR establish power-law scaling in CTR prediction, mirroring the LLM community.

3. **MoE goes mainstream**: Megatron Core (NVIDIA), Trinity Large (Arcee AI), and FineRMoE show MoE becoming the default architecture for scaling.

4. **Agent research is academic-heavy**: Most multi-agent papers come from unaffiliated academic groups, with notable exceptions from Microsoft, Salesforce, and Tencent.

5. **Chinese tech dominates applied RecSys**: 80%+ of recommendation/CTR/ad papers come from Chinese companies (Alibaba, ByteDance, Kuaishou, Tencent, Meituan).

6. **Google DeepMind leads training infrastructure**: Decoupled DiLoCo, SML, and scaling law research position Google at the frontier of training methodology.

7. **Video generation race intensifies**: ViBe, LatSearch, Causal Forcing, and Adaptive Distillation show rapid progress in video diffusion, with no single dominant player.

8. **SSM-Tranformer hybrid convergence**: Mamba-3, InfoMamba, TransMamba, and Swimba all explore hybrid architectures, suggesting the field is converging on blended designs.
