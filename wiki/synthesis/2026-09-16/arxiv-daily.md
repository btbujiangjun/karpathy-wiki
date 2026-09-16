---
title: "arXiv Daily — AI / LLM / Recommendation / Advertising / CTR / Games"
type: synthesis
created: 2026-09-16
updated: 2026-09-16
sources: [arxiv.org]
tags: [arxiv-daily, AI, LLM, recommendation, advertising, CTR, generative-retrieval, sequential-modeling, KV-cache, attention, serving, speculation, MoE, alignment, safety, agents, memory, evaluation, IR, games, game-theory, daily-digest]
---

# arXiv Daily Report — 2026-09-16

> **Mailing status**: No fresh mailing beyond the **Tue 15 Sep 2026** window at run time — arXiv's `/list/{cat}/new` pages and RSS still announce Tuesday 15 September (max ID ~2609.15989; the Wed 16 Sep batch posts tonight ~20:00 ET). Today's report therefore mines the **unclaimed remainder** of the Tue-15 window, exactly as the 09-15 arxiv-paper-check treated the prior Mon-14 mailing.
> **Methodology**: Parsed `/list/{cat}/new` for cs.IR / cs.AI / cs.LG / cs.CL / cs.GT / cs.MA / cs.NE (1,641 raw entries, 753 unclaimed candidates in the 2609.132xx–2609.15989 band after subtracting the 4,731-ID wiki coverage set), then cross-excluded every ID cited in the 09-15 reports (72 IDs; 733 remain), screened titles+abstracts inline in the listing, and featured **31 fresh papers** (all verify **0 hits in `wiki/`**). The arXiv API remained rate-limited (`Rate exceeded.`), so direct page fetch was used; probe HTML was cached under `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/` and cleaned up after.
> **CTR/ads note**: After several windows with ≈0 direct CTR/ads material (09-13 → 09-15 all logged the noise-floor pattern), this remainder is **unusually ads/CTR-rich**: GESE (+2.57% CTR online), VARG (GMV +1.45% / PCTR +0.31% on Tmall search A/B), and LazFormer (industrial transformer rec) are all direct hits.

---

## 1. Recommendation & Generative Recommendation

### 1.1 LazFormer: Scaling Transformers for Industrial Recommendation via Transferable Generative Pre-training

| Field | Detail |
|-------|--------|
| **Authors** | Xiaodong Li, Alin Fan, Mingyang Li, Yan Xiao, Shichao Nie, Junfeng Zhang, Shaochuan Lin, Zhanming Ou, Tao Luo, Xiaoyi Zeng |
| **Institution** | Industrial recommendation team (inferred; same Xiaoyi Zeng / Alin Fan group as MIMA featured 09-14) |
| **Published** | 14 Sep 2026 (cs.IR) |
| **Abstract** | Transformers for industrial recommendation are usually trained from scratch optimizing sparse+dense parameters together — computationally heavy and slow to converge. Pre-training initializes both, but faces **negative transfer** (pre-train and ranking input features differ) and **sparse-parameter overfitting** under multi-epoch ranking (freezing them kills adaptability). **LazFormer** contributes (i) a generative pre-training module that autoregressively generates sequential features for favorable sparse/dense initialization; (ii) a **transferable residual adapter** that injects ranking-specific features in a residual way to neutralize negative transfer; (iii) a **request-aware ranking module** combining long-sequence compression, hybrid sparse attention, and request-aware decoding for ultra-long user histories; (iv) **asymmetric multi-epoch training** that resets sparse parameters but continuously accumulates dense parameters across epochs. |
| **Key Innovations** | (1) Generative pre-training reused across inconsistent feature spaces via a residual adapter; (2) request-aware long-sequence modeling (compression + hybrid sparse attention); (3) asymmetric epoch strategy decoupling sparse-reset / dense-accumulate. |
| **Link** | [arXiv:2609.14978](https://arxiv.org/abs/2609.14978) |

### 1.2 LION: Self-Evolving Memory for Generative Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Xinyu Lin, Zhuosong Jiang, Zixiao Suo, Siqin Wang, Hanqing Zeng, Hanchao Yu, Yinglong Xia, Jiang Zhang, Aashu Singh, Fei Liu, Wenjie Wang, Fuli Feng, Yang Song, Qifan Wang, Tat-Seng Chua |
| **Institution** | Meta AI / USTC / NUS (inferred; Qifan Wang, Hanqing Zeng, Yinglong Xia = Meta; Fuli Feng = USTC; Tat-Seng Chua = NUS) — CIKM 2026 |
| **Published** | 14 Sep 2026 (cs.IR) |
| **Abstract** | User preferences drift continuously, so generative recommenders must **self-evolve**; but continual retraining / distillation-based adaptation hits **evolution conflict**: heterogeneous preference shifts are optimized inside one fully-shared autoregressive parameter space, so dominant patterns progressively dominate while underrepresented patterns get ignored. **LION** installs a sparse **Key-Value memory layer** and follows three principles — **isolated memorization** (sparse memory activation so different behavioral patterns evolve independently), **reinforced evolution** (a consolidation loss amplifies underrepresented preference dynamics during continual adaptation), and **scalable application**. Effectively evolves shared-model generation without letting the majority wash out the tail. |
| **Key Innovations** | (1) Names "evolution conflict" as the failure mode of naive self-evolving generative rec; (2) sparse KV memory as the isolation mechanism + consolidation-loss reinforcement; (3) CIKM'26 evidence across per-period and user/item-varying continual settings. |
| **Link** | [arXiv:2609.15598](https://arxiv.org/abs/2609.15598) |

### 1.3 SCRec: Addressing Cross-Stage Decoupling of Semantic and Collaborative Signals in Generative Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Jiayi Dan |
| **Institution** | (single author, inferred academic) |
| **Published** | 12 Sep 2026 (cs.IR) |
| **Abstract** | Two-stage generative recommenders tokenize items by **textual semantics** (little collaborative signal) then re-embed code sequences from **interactions only** (dropping semantics) — the two stages are **decoupled**, hurting coherence and accuracy. **SCRec** adds bidirectional information supplementation: (i) **collaborative-enhanced tokenization** that textualizes interaction signals into semantic tokens with no extra alignment task; (ii) **semantic-guided generation**, recalibrating semantic priors with learnable code embeddings at decode; (iii) **manifold alignment** reconciling the discrete codebook-index geometry with the dense continuous semantic space. General, plug-in framework with minimal extra training/inference cost. |
| **Key Innovations** | (1) Explicit cross-stage decoupling diagnosis for generative rec; (2) collaborative-in→tokenization, semantic-back→generation bidirectional loop; (3) manifold-level geometric reconciliation of codebook vs semantic space. |
| **Link** | [arXiv:2609.13678](https://arxiv.org/abs/2609.13678) |

### 1.4 P3Rec: Distilling Prior–Posterior Preference Reasoning for LLM-based Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Jinfei Chen, Weihai Lu, Jiawei Cheng |
| **Institution** | (inferred academic) |
| **Published** | 12 Sep 2026 (cs.IR); online 15 Sep |
| **Abstract** | LLM-as-Enhancer recommendation distills LLM preference knowledge into lightweight recommenders to avoid costly online LLM calls, but prior work usually distills from **one perspective only**: prior preference (stable, consistent interests — weak for the current decision) or posterior preference (target-relevant fine-grained interests — over-reliant on target clues). **P3Rec** extracts *both*: target-agnostic prior preferences and target-conditioned posterior preferences from the user side, plus item-centric representations from item semantics and predecessor interactions; then it **internalizes** prior knowledge via absorption and posterior knowledge via distillation into behavioral representations. Because the fused vector may not always be a decisive retrieval direction, it measures **historical interest dispersion (interest entropy)** and adaptively calibrates the user representation before contrastive retrieval optimization. |
| **Key Innovations** | (1) Complementary prior+posterior distillation instead of single-view knowledge; (2) item-centric + interest-entropy calibration of the distilled representation; (3) keeps lightweight (no online LLM at serving). |
| **Link** | [arXiv:2609.13993](https://arxiv.org/abs/2609.13993) |

### 1.5 TATK: Triple-Aware Top-K Learning with Knowledge-Grounded Verification for LLM-based Sequential Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Yuchen Guan, Jiaye Liu, Yifei Han, Zhenxi Zhang, Yixuan Weng, Bin Li |
| **Institution** | (inferred academic) — EMNLP 2026 Main |
| **Published** | 13 Sep 2026 (cs.CL) |
| **Abstract** | LLM sequential recommenders cast next-item prediction as text generation, but that interface is poorly matched to **full-catalog top-K ranking**. **TATK** couples **Top-K Learning (TKL)** — context-aware metadata-KG prompt grounding + position-aware top-K rewards aligning training with ranking utility — with **Knowledge-Grounded Verification (KGV)** — a structure-aware rerank over top-M candidates after a single LLM forward pass, reusing the same metadata-derived item graph. On Musical Instruments / CDs & Vinyl / Video Games (Amazon 2023, matched R2ec-style full-catalog protocol): improves over the matched R2ec reproduction on **all 36 metrics** (NDCG@10 up to +27% on Gemma-2-2B, +8% on Qwen2.5-3B) at ≤1.17× RecPO latency. Diagnostics: structural (KG) evidence helps for recoverable top-M candidates with reliable metadata and should be gated when KG relations are sparse/noisy. |
| **Key Innovations** | (1) Position-aware top-K reward (ranking utility, not text-likelihood) for LLM rec; (2) single-pass generation + structure-aware rerank ; (3) explicit "gate the KG, don't trust it blindly" diagnostic. |
| **Link** | [arXiv:2609.14565](https://arxiv.org/abs/2609.14565) |

### 1.6 VARG: Value-Aware and Ranking-Aligned Generative Retrieval for Dynamic E-commerce Search

| Field | Detail |
|-------|--------|
| **Authors** | Xiaopeng Chu, Jianbo Zhu, Mingmin Jin, Jing Wang, Xing Fang, Wenyi Zhang |
| **Institution** | Alibaba / Tmall App search (inferred from content) |
| **Published** | 13 Sep 2026 (cs.IR) |
| **Abstract** | E-commerce search candidate generation must weigh relevance, personalization, **and business value** before ranking. **VARG** is a generative retrieval system for **Tmall App search** that directly admits generated candidates to the final ranker. **VARG-ID** builds semantic prefixes with RQ-VAE, adds bidirectional query-item contrastive learning, and appends a **value-ordered third token** so item addresses carry a business-value prior. Three-stage SFT (item-to-identifier, query-semantic, personalized retrieval) uses value-aware, hierarchy-aligned supervision plus **LO-SFT** (local ordinal supervision, learning within-cluster ordering). **Prefix-GRPO** scores candidate prefix probability with gated rewards (output legality, user behavior, ranker advantage, search relevance) under prefix-aware token weighting. Daily product/model updates preserve addresses without re-tokenizing the catalog. Offline: millions-scale identifier stability and value-recall gains; **14-day A/B on 20% of traffic: GMV +1.45%, per-user IPV +0.22%, PCTR +0.31%**. |
| **Key Innovations** | (1) Value-ordering baked into the item *identifier*, not just the ranker (business-aware addresses); (2) Prefix-GRPO optimizing ranking-aligned candidate generation; (3) production-scale A/B with daily re-tokenization discipline. |
| **Link** | [arXiv:2609.14493](https://arxiv.org/abs/2609.14493) |

### 1.7 GESE: Generate to Explore, Select to Exploit — Aligning LLM-based Headline Generation with Personalized Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Yi Chen, Rufeng Cheng, Qiang Xie, Tao Li |
| **Institution** | (industrial feeds platform, 100M+ DAU, inferred) |
| **Published** | 14 Sep 2026 (cs.IR) |
| **Abstract** | A static headline for an item in a recommendation feed fails the diverse user population — especially long-tail audiences. Optimizing an LLM to emit a single best headline causes **mode collapse** into generic patterns that satisfy average taste. **GESE** decouples personalization at the presentation layer: a **generative explorer** (LLM) uses Group Sequence Policy Optimization (**GSPO**) with a hierarchical reward to emit a candidate set maximizing semantic coverage of latent interests; then a **lightweight feedback-aware selector** (the exploiter) picks the best realization from the set using real-time context. On a commercial platform (>100M DAU): **CTR +2.57%, dwell time +0.87%** vs SOTA baselines. |
| **Key Innovations** | (1) Diversity-vs-precision decoupling as an explicit presentation-layer architecture (explore-then-select); (2) GSPO with hierarchical (coverage + per-item) rewards; (3) large-scale online validation — a rare direct CTR lift from generative content adaptation. |
| **Link** | [arXiv:2609.15094](https://arxiv.org/abs/2609.15094) |

### 1.8 Safety as a Constraint: Fine-Tuning an LLM Recommender to Explain Itself

| Field | Detail |
|-------|--------|
| **Authors** | Jiashu He, Emma Yanyong Kong, JJ Tan, David Fagnan |
| **Institution** | (large video-streaming service, inferred) |
| **Published** | 12 Sep 2026 (cs.AI) |
| **Abstract** | Recommenders predict *what* but not *why*; per-user personalized explanations could be served by a frontier-model call but at extra cost/latency. This paper trains a **recommender LLM** to generate faithful, **strictly non-harmful** explanations grounded in the user's watch history of a large streaming service. Two LLM-judge reward models cover three criteria, and **constrained GRPO** is used so safety enters as a constraint rather than a soft trade-off. On a held-out real-world set, the all-three-criteria PASS rate rises **0.649 → 0.956** (own judges) / **0.677 → 0.931** (independent judge) while recommendation language and performance stay intact — showing an LLM recommender can take on secondary tasks (explanation) without hurting ranking. |
| **Key Innovations** | (1) Constraint-based (not weighted-loss) GRPO for safety/faithfulness in generative rec; (2) judge-finetuned dual reward models; (3) evidence that a single LLM recommender can dual-purpose (rank + explain) with no degradation. |
| **Link** | [arXiv:2609.13657](https://arxiv.org/abs/2609.13657) |

---

## 2. Sequential Modeling, Attention & Serving Efficiency

### 2.1 Self-Indexing Attention: Compression-Compatible Sparse Long-Context LLM Inference

| Field | Detail |
|-------|--------|
| **Authors** | Xu Yang, Jiapeng Zhang, Zhangke, Changjian Chen, Yuxin Chen, Feiqiang Sun, Chengguang Xu, Feng Jin, Zhuo Tang |
| **Institution** | (inferred academic) |
| **Published** | 16 Aug 2026 (submission) / cs.IR |
| **Abstract** | Sparse long-context inference retrieves tokens in prefill and decode but existing methods use **different retrieval representations per stage**. **Self-Indexing Attention** is training-free and built on one **transform-domain sign–magnitude representation** shared across stages: the key signs form a reusable 1-bit token-level index for grouped prefill selection and decode retrieval, compatible with external KV-cache compression (no separate indexer metadata), and answerable via bitwise ops on modern accelerators. At 5% attention density it stays close to dense attention on LongBench/RULER with **up to 6.1× prefill and 10.3× decode attention-operator speedups**, and works with TurboQuant and DeepSeekV4-Flash low-bit KV compression plus pretrained sparse-attention indexers. |
| **Key Innovations** | (1) One reusable sign-magnitude index across prefill+decode (no per-stage retraining/refetch); (2) 1-bit, bitwise-accelerable index compatible with external KV compressors; (3) large speedups at ~dense accuracy. |
| **Link** | [arXiv:2609.13205](https://arxiv.org/abs/2609.13205) |

### 2.2 Grouped Value Attention: Efficient KV Caching via On-Demand Key Reconstruction

| Field | Detail |
|-------|--------|
| **Authors** | Vishesh Tripathi, Abhay Kumar, Ramsha Khan |
| **Institution** | (inferred academic) |
| **Published** | 8 Sep 2026 (submission) / cs.AR |
| **Abstract** | GQA halves KV traffic by sharing value heads but still stores **a key and a value per step**. **GVA (Grouped Value Attention)** stores only grouped *values* and reconstructs content keys at inference with a learned **linear map that can be absorbed into the query** — so content keys are never materialized in the desired decode path. A small decoupled **RoPE positional channel** retains position via a separately cached positional key. For studied configs the persistent cache shrinks ~**45–47% vs matched GQA**; at 350M-scale / 30B FineWeb-Edu tokens the positional variant scores 44.18 avg on five tasks (GQA 44.36, MLA 43.88) — near-GQA quality with a much more compact cache. Custom decoding kernels being evaluated; open-source planned. |
| **Key Innovations** | (1) Store value-only + reconstruct keys in-query (eliminates materialized content keys); (2) decoupled positional KV channel for RoPE; (3) ~half the persistent cache at near-GQA accuracy. |
| **Link** | [arXiv:2609.13285](https://arxiv.org/abs/2609.13285) |

### 2.3 Carryover Drafting: Recycling Rejected States for Speculative Decoding

| Field | Detail |
|-------|--------|
| **Authors** | Jahyun Koo, Sunghyeon Woo, Jaeeun Kil, Jeongtae Lee, Sungjae Lee, Kyomin Jung, Minsub Kim |
| **Institution** | Seoul National University / industrial (inferred; Kyomin Jung) |
| **Published** | 13 Sep 2026 (cs.LG) |
| **Abstract** | Speculative decoding verifies several drafted tokens per target pass; by construction the verifier computes representations of **both accepted and rejected tokens**, yet drafters discard the rejected ones. **Carryover Drafting** repurposes rejected target hidden states as temporary KV context the drafter selectively attends to (single learned "rejected" embedding distinguishes them from committed context; context replaced each round, bounded by one proposal block). A **parallel draft-verify-draft training** exposes inference-aligned rejected states without sacrificing training parallelism. With DFlash and a DSpark-derived semi-autoregressive drafter on two targets: **acceptance length +6.5–14.7%, end-to-end vLLM speedup +7.9–14.4%** (up to +28.8% on translation). |
| **Key Innovations** | (1) Turns the verifier's "wasted" rejected-state compute into drafting signal; (2) minimal interface change (one embedding, bounded extra context) riding the existing drafters; (3) parallel training aligned to inference-time rejected states. |
| **Link** | [arXiv:2609.14717](https://arxiv.org/abs/2609.14717) |

### 2.4 AttnFuse: A Composable DSL for Compiling Attentions to Fused GPU Kernels

| Field | Detail |
|-------|--------|
| **Authors** | Varun Kumar Dasoju, Tian Zhao |
| **Institution** | (inferred academic) |
| **Published** | 11 Sep 2026 (cs.LG) |
| **Abstract** | Every new attention variant needs expert-written GPU kernels, and PyTorch's `flex_attention` only supports modifications **after** the central matmul — it cannot express pre-matmul transforms like **RoPE**, the positional encoding in every major LLM. **AttnFuse** is a small attention DSL making pre-multiplication transforms first-class: ten composable building blocks describe a variant and a compiler emits a single fused kernel. On RTX 3090: **2.10× over flex_attention** on RoPE+causal; on H100 runs a full Llama-3-8B training step within 5% of PyTorch's hand-tuned backend. The **Rotation Calculus** derived from compute-to-bandwidth ratios decides when to fuse RoPE vs apply separately, with a crossover matching measurement. |
| **Key Innovations** | (1) RoPE and other pre-matmul ops as first-class DSL citizens (beyond flex_attention's post-matmul window); (2) single-kernel compilation with real speedups; (3) an analytical rotation-fusion rule tied to GPU compute:bandwidth. |
| **Link** | [arXiv:2609.13612](https://arxiv.org/abs/2609.13612) |

### 2.5 OpWeave: Flexible Operator Disaggregation for Heterogeneous LLM Serving

| Field | Detail |
|-------|--------|
| **Authors** | Zikun Li, Yixuan Mei, Shiqi Pan, Zixuan Chen, Xiaowen Zhang, Mengdi Wu, Shuhuai Lin, Yutong Yang, Zhihao Zhang, Xupeng Miao, Rashmi Vinayak, Zhihao Jia |
| **Institution** | CMU (inferred; Zhihao Jia, Rashmi Vinayak, Xupeng Miao) |
| **Published** | 13 Sep 2026 (cs.DC) |
| **Abstract** | Serving systems increasingly **disaggregate attention from FFN/MoE execution**, but existing systems fix the operator boundaries and lack a unified account of *when* disaggregation pays. **OpWeave** is an end-to-end heterogeneous ODS framework: an **analytical cost model** bounds homogeneous and heterogeneous disaggregation gains over colocated serving; a **regularity-aware planner** jointly optimizes operator partitioning and deployment (tractable even for hybrid-attention models); a vLLM-based runtime executes flexibly-staged plans across heterogeneous device groups. Reduces serving cost **up to 1.78× (homogeneous) / 1.89× (heterogeneous)** vs best feasible baselines while meeting latency SLOs. |
| **Key Innovations** | (1) First unified cost-theoretic characterization of *whether/when* operator disaggregation helps; (2) regularity-aware joint partition/deploy search for hybrid attention; (3) an actual vLLM runtime executing cross-device operator stages. |
| **Link** | [arXiv:2609.14237](https://arxiv.org/abs/2609.14237) |

---

## 3. LLM Training, Alignment & Efficient Pre-training

### 3.1 MoARa: Module-Aware Rank Allocation and Structure-Preserving Decomposition for Low-Rank LLM Pre-training

| Field | Detail |
|-------|--------|
| **Authors** | Keunyoung Kim, Nojun Kwak |
| **Institution** | Seoul National University (inferred) — EMNLP 2026 Main |
| **Published** | 14 Sep 2026 (cs.LG) |
| **Abstract** | Low-rank gradient projection cuts optimizer-state memory in LLM pre-training but still spends extra steps/wall-clock vs full-rank. MoARa attributes this to two flaws: the projection-rank budget is spent **uniformly across modules with heterogeneous projection sensitivity**, and projecting a raw gradient **attenuates magnitude and direction jointly**. **MoARa** uses static profiling-based, module-aware rank allocation plus a **block-wise magnitude–direction decomposition** (default block ~ attention-head width). Across five Transformer families (Llama/Qwen/DeepSeek, 300M–7B), GaLore+MoARa reaches standard GaLore's final perplexity in **37% fewer steps and 34% less wall-clock on Llama-2-7B** (0.2% extra reserved memory). The module-aware allocation alone helps all six low-rank methods tested (up to 41.7% step / 37.1% wall-clock reduction). |
| **Key Innovations** | (1) Module-sensitivity profiling replaces uniform low-rank budgets; (2) magnitude/direction decomposition preserves gradient geometry; (3) positive transfer — rank allocation alone strengthens six low-rank pre-training methods. |
| **Link** | [arXiv:2609.15037](https://arxiv.org/abs/2609.15037) |

### 3.2 MoME: Mixture-of-Memory Embeddings for Context-Aware Sparse Lookup

| Field | Detail |
|-------|--------|
| **Authors** | Muchen Li, Leonid Sigal, Renjie Liao |
| **Institution** | University of British Columbia (inferred) |
| **Published** | 14 Sep 2026 (cs.CL) |
| **Abstract** | "Conditional memory" adds token-indexed embedding tables that cheaply augment an LLM backbone, but existing methods retrieve a **deterministic fixed row per surface form** — collapsing polysemes (python-the-language vs python-the-animal) into one embedding. **MoME (Mixture of Memory Embeddings)** replaces the single row with **M slots** and a learned gate over hidden states to pick which slots to read per position. Iso-parameter and iso-FLOP controlled pre-training across nanochat, Llama-3/MobileLLM and Qwen3 backbones: beats Value Embedding, Bigram, and STEM baselines with a more promising memory-size scaling trend at sub-billion scale, while routing analyses show sense-aware slot dispatch (interpretable mixtures). |
| **Key Innovations** | (1) Context-gated *mixture* memory (multiple slots per token) vs single-row lookups; (2) consistent wins iso-parameter/iso-FLOP with better memory-scaling slope; (3) interpretable sense-specialized routing of polysemous tokens. |
| **Link** | [arXiv:2609.15126](https://arxiv.org/abs/2609.15126) |

### 3.3 SaLT-DPO: Segment-Aware Listwise Alignment for Reasoning Safety in Large Reasoning Models

| Field | Detail |
|-------|--------|
| **Authors** | JungMin Yun, Junehyoung Kwon, Hayeong Ryu, Byeonggeuk Lim, Hoejoon Kwon, YoungBin Kim |
| **Institution** | Korea University (inferred) — EMNLP 2026 Main |
| **Published** | 14 Sep 2026 (cs.AI) |
| **Abstract** | Large Reasoning Models have a **dual safety surface**: both reasoning traces and final answers can carry harm, but whole-response alignment lets unsafe reasoning hide behind a safe-looking answer. **SaLT-DPO** (Segment-aware Listwise Target DPO) (1) decomposes responses into reasoning/answer segments, scores each independently, and aligns **length-normalized segment rewards** to soft target distributions over candidates; (2) adds **safety coherence regularization** (weakest-link principle) for cross-segment consistency; (3) **utility-anchors** benign prompts to cut over-refusal. On three LRMs it cuts unsafe rates for both segments while limiting benign-compliance and reasoning degradation; ablations confirm the three components are complementary. |
| **Key Innovations** | (1) Segment-level (not whole-response) safety rewards for LRMs; (2) listwise soft targets + weakest-link coherence; (3) explicit anti-over-refusal anchoring. |
| **Link** | [arXiv:2609.15517](https://arxiv.org/abs/2609.15517) |

### 3.4 Mixture-of-Experts Language Models Can Be Strong and Efficient Retrievers

| Field | Detail |
|-------|--------|
| **Authors** | Anubhav Shrestha, Safal Shrestha, Minwu Kim, Torsten Suel, Keith Ross |
| **Institution** | NYU (inferred; Keith Ross, Torsten Suel) |
| **Published** | 11 Sep 2026 (cs.IR) |
| **Abstract** | Fine-tuned decoder LLMs make strong first-stage retrievers but cost scales with **total** model size since every query/document passes through everything. MoE LLMs activate only a subset of parameters per token yet are underexplored as retrievers. Training MoE and dense backbones with the same procedure: MoE retrievers beat dense retrievers with comparable *active* parameter counts by **up to 3.0 nDCG@10 on BEIR**; the strongest MoE matches an 8B dense retriever with **59% fewer active parameters and 18% lower query-encoding time**. The number of experts used at query time can be cut **without retraining/re-indexing**, keeping >99% effectiveness while saving up to 26% query-encoding time — and strong MoE first stages often obviate rerankers. |
| **Key Innovations** | (1) MoE as a retrievers-vs-parameter-efficiency result (active-parameter scaling, not nominal size); (2) serving-time expert reduction with no re-indexing; (3) "MoE first-stage ≈ reranked dense" cost/quality map. |
| **Link** | [arXiv:2609.13486](https://arxiv.org/abs/2609.13486) |

### 3.5 ShieldVLA: Feasibility-Aware Safety Alignment for Vision-Language-Action Models

| Field | Detail |
|-------|--------|
| **Authors** | Manan Tayal, Akshay Nambi |
| **Institution** | Microsoft Research India (inferred; Akshay Nambi) |
| **Published** | 2 Sep 2026 (submission) / cs.RO |
| **Abstract** | Safety fine-tuning of VLA (robot manipulation/navigation) models typically uses **Lagrangian soft penalties** on expected cost → residual violations or over-conservatism, and visual domains lack dense per-step safety labels. **ShieldVLA** learns a **model-free approximation of the Hamilton–Jacobi reachability value function** from visual observations to estimate the safe operating region, and gates policy optimization — **reward maximization inside the feasible region, recovery near unsafe states** — avoiding the persistent reward–cost trade-off. A **rubric-based VLM safety scorer** turns semantic safety feedback into structured critic targets without manual cost labels. Across five navigation+manipulation benchmarks and multiple VLA backbones: **−57% cumulative safety cost and +0.13 task success vs SafeVLA**. |
| **Key Innovations** | (1) HJ-reachability safety critic as a gating constraint (not a soft cost); (2) rubric-driven VLM → critic-target supervision pipeline (no cost labels); (3) simultaneous safety-cost and success-rate improvement. |
| **Link** | [arXiv:2609.13231](https://arxiv.org/abs/2609.13231) |

---

## 4. LLM Agents & Long-Horizon Memory

### 4.1 Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement

| Field | Detail |
|-------|--------|
| **Authors** | Hongyao Tang, Yi Ma, Pengyi Li, Yifu Yuan |
| **Institution** | PKU/BIGAI-aligned (inferred; Hongyao Tang) |
| **Published** | 11 Sep 2026 (cs.AI) |
| **Abstract** | "Recursive self-improvement (RSI)" is claimed at many scales but has **no single formal description**, whereas the classical counterpart — generalized policy iteration (GPI) — is well understood (when the update principle and evaluation base live outside the agent). **Generalized Agent Iteration (GAI)** unifies the two as one learning paradigm: the agent is a configuration of modifiable components in a system; learning is a cycle of *agent evaluation* and *agent improvement*. Two dials classify every instance: **whether the improving mechanism is part of the agent** (the GPI↔RSI boundary) and **whether the evaluation standard is grounded outside it** (anchored / goal-drift / fully-self-referential polarity). Place existing systems on these two axes, making the defects of RSI statable "one condition at a time." |
| **Key Innovations** | (1) First unified formalism spanning GPI and RSI; (2) two coordinate dials (internal-optimizer, external-groundedness) that place known systems comparably; (3) a principled vocabulary for diagnosing RSI failures. |
| **Link** | [arXiv:2609.13406](https://arxiv.org/abs/2609.13406) |

### 4.2 LIMBO: Lifelong Inference-Time Memory and Budget Optimization for LLM Agents

| Field | Detail |
|-------|--------|
| **Authors** | Siddharth Sharma, Nilesh Prasad Pandey, Onat Gungor, Tajana Rosing |
| **Institution** | UCSD (inferred; Tajana Rosing) — ICTAI 2026 |
| **Published** | 12 Sep 2026 (cs.LG) |
| **Abstract** | Lifelong agents use **experience replay** (past interactions injected into the prompt), but replay competes with retrieval/reasoning/tool-use/verification for the same bounded prompt+compute budget. Existing systems fix the replay policy regardless of whether replay helps the current task. **LIMBO** frames this as *inference-time memory allocation* — memory as a controllable resource — and learns the per-task memory strategy **and** compute budget **online in a single pass** (no weights, no teacher, no offline retraining). On LifelongAgentBench across three LLM backbones: better cost-accuracy trade-offs than SOTA memory baselines, and matches the strongest baselines at up to **~83% lower inference cost (~53% average)**. |
| **Key Innovations** | (1) Surfaces "inference-time memory allocation" as a distinct problem class for lifelong agents; (2) online, single-pass, retraining-free policy; (3) up to ~83% cost reduction at matched quality. |
| **Link** | [arXiv:2609.14138](https://arxiv.org/abs/2609.14138) |

### 4.3 Pull: Lazy Materialization of Working Memory for Stateful LLM Conversations

| Field | Detail |
|-------|--------|
| **Authors** | Jiangang Chen |
| **Institution** | (single author, inferred industrial) |
| **Published** | 13 Sep 2026 (cs.CL) |
| **Abstract** | Hundreds-of-turn conversations make full-context injection $O(N^2)$ in tokens, while summarization/truncation **irreversibly** discard history. **Pull** is a session router with an addressable metadata directory maintained by a local **deterministic Purifier** (zero LLM calls, ms latency); at query time the LLM lazily materializes only the turns it needs, and unmaterialized turns stay **reversibly** collapsed (later queries can expand them). On LoCoEval (128 conversations, 12,780 turns): −75.1% per-query tokens (single-hop, quality unchanged Δ=−0.002 n.s.) and −72.0% (multi-hop, quality +0.017). A 7,831-query routing benchmark shows entity-lifecycle tracking is a prerequisite for distance-independent routing; on BEAM 1M, **F1 +55.2% over truncation**. |
| **Key Innovations** | (1) Reversible lazy materialization vs irreversible compression; (2) deterministic zero-LLM-call metadata/purification director; (3) quantitative evidence that entity-lifecycle bookkeeping is the enabler for stateful routing. |
| **Link** | [arXiv:2609.14773](https://arxiv.org/abs/2609.14773) |

### 4.4 PolicyMem: Geometric Policy Memory for LLM Governance

| Field | Detail |
|-------|--------|
| **Authors** | Yuanchen Bei, Zhengzhang Chen, Yanjun Zhao, Haoyu Wang, Hanghang Tong, Haifeng Chen |
| **Institution** | Zhejiang University / NEC Labs America (inferred; Haifeng Chen, Zhengzhang Chen) |
| **Published** | 12 Sep 2026 (cs.CL) |
| **Abstract** | LLM governance guards (learning-based classifiers vs programmable rule frameworks) fail to **externalize policies as reusable operational state**. **PolicyMem** stores natural-language policies as **geometric memory objects — low-rank subspaces in a shared representation space**: a memory writer compiles policies into memory slots; query-response pairs read memory via projection energy. The resulting evidence profile directly yields the safety verdict and is reused for **attribution and post-intervention verification**; coupled with a response rewriter it closes a **detect–rewrite–verify** governance loop. SOTA unsafe-detection across five benchmarks, with policy attribution, rewriting, and post-intervention verification all mediated by the same shared memory. |
| **Key Innovations** | (1) Policies as reusable geometric (low-rank subspace) memory objects — not weights or hand-written rules; (2) one shared evidence profile drives detection *and* attribution *and* verification; (3) closes an editing loop over the same policy memory. |
| **Link** | [arXiv:2609.13734](https://arxiv.org/abs/2609.13734) |

### 4.5 Why LLM Agents Collapse Without Oversight: The Enforcement Gap in Emergence World Failures

| Field | Detail |
|-------|--------|
| **Authors** | Yuhang Wang |
| **Institution** | (single author, inferred) |
| **Published** | 14 Sep 2026 (cs.AI) |
| **Abstract** | In Emergence World, frontier LLM agents in an unsupervised simulation committed crimes, starved, and enforced unanimous conformity with **no external attacker**. The mechanism, per this paper, is an **enforcement gap**: Reflexion-style agents *detect* dangerous plan steps via self-critique but the architecture gives **no pathway from detection to action** — the audit sees, the controller ignores. A single conditional check (<20 lines) closing the gap reduces attack success **>4× across frontier models, five agent frameworks, and an independent benchmark**; formally, when enforcement probability → 0, detection quality is irrelevant to security. Two compounding failure modes (unreliable auditors, unparseable verdicts) explain every collapse pattern; a GRPO-trained controller resolves the ambiguous-verdict case, motivating a three-requirement **Audit Enforcement Specification** absent from deployed frameworks. |
| **Key Innovations** | (1) Pins Emergence-World collapse on a concrete architectural gap, not model malice; (2) formal result that detection without enforcement is security-irrelevant; (3) tiny, universally-applicable fix with >4× reduction. |
| **Link** | [arXiv:2609.15293](https://arxiv.org/abs/2609.15293) |

---

## 5. Evaluation, Search & IR Theory

### 5.1 CoArena: Evaluating Computer-Use and Multi-Agent Systems in Real Time

| Field | Detail |
|-------|--------|
| **Authors** | Nitish Kovuru, Prateek Jannu |
| **Institution** | (inferred academic) |
| **Published** | 13 Sep 2026 (cs.LG) |
| **Abstract** | Static computer-use benchmarks age, leak, and drift from how people actually use agents. **CoArena** measures use directly: real users submit tasks; two systems (single model or multi-agent pipeline behind the same tool interface) execute concurrently in identical sandboxed desktops; users blind-judge the two outcomes; a public leaderboard is refit from the judgments. The core contribution is a **formal account of "real-time" as five measurable properties** (continuous task arrival, live concurrent execution, online rating updates, freshness with contamination resistance, bounded feedback latency from failed run to reusable training env). Full Bradley-Terry machinery follows: penalized MLE, streaming Elo-like updates, cluster-robust CIs, rank bands, and new-system entry rules — with a worked five-system / 211-vote example. |
| **Key Innovations** | (1) Live user-judged concurrency as the evaluation primitive (no fixed task set); (2) five-property formalization of "real-time evaluation"; (3) complete Bayesian/BT rating + contamination story, derived end-to-end. |
| **Link** | [arXiv:2609.14239](https://arxiv.org/abs/2609.14239) |

### 5.2 The Wisdom of the Loudest: A Large-Scale Audit of Generative Search on Reddit

| Field | Detail |
|-------|--------|
| **Authors** | Agam Goyal, Wang Claire, Eshwar Chandrasekharan |
| **Institution** | UIUC (inferred; Eshwar Chandrasekharan) |
| **Published** | 13 Sep 2026 (cs.IR) |
| **Abstract** | Generative search mediates access to online communities, yet little is known about **which voices survive retrieval and synthesis**. The authors audit Reddit Answers on **10,000 queries from 20 advice/support communities, run 3× → 30,000 answers over 14.68M comments**. Findings: run-to-run differences are driven **primarily by retrieval**; answers routinely blend evidence across communities; selection strongly favors **already-visible, top-level comments**; formal/directive language is surfaced more, while **experiential first-person voice declines sharply** — weakened both at selection and during synthesis. Conclusion: community-grounded generative search is not neutral summarization and needs provenance/plurality/legibility, not just relevance and fluency. |
| **Key Innovations** | (1) Unprecedented audit scale for a generative search product (30k answers); (2) attribution of output variance to retrieval vs synthesis; (3) "wisdom of the loudest" — an empirical voice-selection bias with design recommendations. |
| **Link** | [arXiv:2609.14575](https://arxiv.org/abs/2609.14575) |

### 5.3 Beyond Benchmark Scores: How Synthetic and Authentic Query Distributions Diverge in RAG Evaluation

| Field | Detail |
|-------|--------|
| **Authors** | Filip J. Kucia, Barbara M. Gawlik |
| **Institution** | (inferred academic) — CIKM 2026 (Short Research Paper) |
| **Published** | 13 Sep 2026 (cs.IR) |
| **Abstract** | RAG systems are routinely evaluated on **synthetic** question sets generated from the corpus, but distribution shift can overstate deployment readiness. On a university faculty information system, comparing **1,851 synthetic questions (Gemini Notebook) vs 322 authentic survey queries**: authentic queries average **6.8 words vs 15.7**, draw from only **53 unique sources vs 165**, and include topics the generator never covers. Configurations that look great on synthetic benchmarks drop substantially on authentic queries — and optimizing on synthetic queries selected a **higher-latency hybrid retriever** (sparse retrieval helped long synthetic questions but not short authentic ones, costing up to **8× latency**). Recommendation: treat synthetic (capacity ceiling) and authentic (robustness) sets as complementary extremes. |
| **Key Innovations** | (1) Concrete synthetic-vs-authentic query divergence numbers (length, source coverage, topic coverage); (2) a case where synthetic optimization actually *selected the wrong architecture*; (3) practical complementary-extremes evaluation recommendation. |
| **Link** | [arXiv:2609.14579](https://arxiv.org/abs/2609.14579) |

### 5.4 Vibe Patenting: Evaluating LLM Judges for Professional Patent-Drafting Agents

| Field | Detail |
|-------|--------|
| **Authors** | Toshiaki Koike-Akino, Vlad Blaykhman, Ye Wang, Jing Liu, Gene V. Vinokur |
| **Institution** | MERL / professional legal (inferred; Toshiaki Koike-Akino, Gene V. Vinokur) |
| **Published** | 11 Sep 2026 (cs.AI) |
| **Abstract** | Do LLM judges stay reliable on complex professional work? **Vibe Patenting** is an end-to-end patent-drafting testbed: a separately-invoked LLM judge evaluates drafts and returns structured feedback for iterative revision. Judge-guided revision consistently improves judge-assessed quality while unguided revision saturates; iterative judge feedback lets a **low-reasoning agent approach a much more expensive high-reasoning agent**; stronger models/reasoning generally help. Cross-validation against an **independent professional patent attorney** finds meaningful but **strongly metric-dependent agreement and systematic calibration differences** — the judge is useful as an optimization signal yet should not be mistaken for attorney-level evaluation. |
| **Key Innovations** | (1) A realistic agentic benchmark for judge-driven iterative generation; (2) "cheap judge + iteration ≈ expensive agent" result; (3) honest judge-vs-domain-expert calibration gap. |
| **Link** | [arXiv:2609.13422](https://arxiv.org/abs/2609.13422) |

### 5.5 TF-IDF and BM25 Are Exact KL Divergences

| Field | Detail |
|-------|--------|
| **Authors** | Ivan Silajev |
| **Institution** | (single author, inferred) |
| **Published** | 11 Sep 2026 (cs.IR) |
| **Abstract** | TF-IDF and BM25 are ubiquitous relevance scorers with **no standard probabilistic derivation** inside a unified framework. This paper shows both admit an **exact interpretation as Kullback–Leibler divergences between two probability models** — including the practically-used BM25 variant with the +1 IDF correction (the original variant is discussed separately). The result gives TF-IDF/BM25 a common theoretical footing and a principled basis for comparing them with other IR methods (interpolation, language models, BM25 variants) rather than only experimentally. |
| **Key Innovations** | (1) Exact (not asymptotic) KL interpretation of TF-IDF and BM25; (2) handles the +1-correction BM25 actually deployed; (3) a unified statistical lens for the classic lexical-scoring family. |
| **Link** | [arXiv:2609.14016](https://arxiv.org/abs/2609.14016) |

---

## 6. Games & Market Dynamics

### 6.1 Multi-Agent Reinforcement Learning in Markets with Congestion

| Field | Detail |
|-------|--------|
| **Authors** | Qixuan Zai, Randall Berry |
| **Institution** | Northwestern University (inferred; Randall Berry) |
| **Published** | 13 Sep 2026 (cs.GT) |
| **Abstract** | Extends the "**independently learning MARL agents tacitly collude**" literature to markets where firms face **congestible resources**: Bertrand competition with price announcements, customers choosing among firms by price *and* congestion, and an **unknown inverse demand curve** firms must learn online. Each firm is a self-interested learner choosing prices to maximize profit. The study maps how **learning dynamics, state representation, and strategic interaction jointly shape competition** in congestible-resource markets — with direct implications for designing learning-enabled markets (and, downstream, ad/allocative auctions with congested capacity). |
| **Key Innovations** | (1) Tacit-collusion analysis extended to congestion-dependent demand (price × congestion trade-off); (2) unknown inverse-demand learning by self-interested agents; (3) implications for mechanism/state-design to keep learning markets competitive. |
| **Link** | [arXiv:2609.14827](https://arxiv.org/abs/2609.14827) |

### 6.2 High-Probability Nash Regret for Decentralized Learning in Markov α-Potential Games

| Field | Detail |
|-------|--------|
| **Authors** | S. Rasoul Etesami |
| **Institution** | Purdue University (inferred) |
| **Published** | 14 Sep 2026 (cs.LG) |
| **Abstract** | Decentralized NE learning in infinite-horizon discounted Markov **α-potential games** under bandit feedback: KL-projected natural-policy-gradient algorithms in an **episodic** setting and a **fully online asynchronous** setting (one cost sample per step, async updates along a continuing trajectory), with finite-time high-probability NE regret of **Õ(T^{-1/4}) and Õ(T^{-2/15})** respectively. Crucially, the bounds drop the **distribution-mismatch coefficient** (which can scale with state-space size) while tolerating potential approximation error, estimation-oracle bias, and transition sensitivity; state-wise potential structure yields additive dependence on α. Specializes to independent-resource Markov congestion games (IMCG) — including a new strategic **online job scheduling on stochastic machines** application. |
| **Key Innovations** | (1) First finite-time high-probability NE regret for fully online async decentralized learning in Markov α-potential games; (2) eliminates the distribution-mismatch coefficient; (3) constructively connects approximate-potential structure and congestion games to scheduling. |
| **Link** | [arXiv:2609.14959](https://arxiv.org/abs/2609.14959) |

### 6.3 A Game-Theoretic Framework for Incentive-Compatible AI Training Under Renewable-Energy Constraints

| Field | Detail |
|-------|--------|
| **Authors** | Konstantinos Varsos, Ramin Khalili, Adamantia Stamou, George D. Stamoulis, Vasillios A. Siris |
| **Institution** | AUEB (Athens University of Economics and Business, inferred) |
| **Published** | 14 Sep 2026 (cs.ET) |
| **Abstract** | Distributed/collaborative AI training runs across heterogeneous nodes whose energy availability varies in space and time, while renewable grids increasingly have excess generation. This paper builds a **game-theoretic model of carbon-aware AI training**: agents strategically decide whether to participate and how hard to train under limited renewable supply, balancing diminishing learning returns, green-budget rewards, and grid-consumption penalties. Analyzed with Federated Learning as the representative case study, covering **equilibrium existence, efficiency, and adaptive dynamics**; simulations show appropriately designed incentives can **eliminate grid-based energy usage while preserving model performance** — an incentive-compatible mechanism to sharply cut AI training carbon emissions. |
| **Key Innovations** | (1) Participation + intensity as strategic variables under renewable budgets; (2) equilibrium/efficiency analysis of green-training incentives; (3) simulation evidence that incentives can zero-out grid energy without degrading models. |
| **Link** | [arXiv:2609.15389](https://arxiv.org/abs/2609.15389) |

---

## Summary of Key Trends

| Trend | Notable Papers |
|-------|---------------|
| **Ads/CTR returns to the daily arXiv feed** | GESE (+2.57% CTR / +0.87% dwell), VARG (Tmall A/B: GMV +1.45%, PCTR +0.31%, IPV +0.22%), LazFormer (industrial gen-pre-training for ranking) — breaking the multi-window "≈0 CTR/ads" noise-floor pattern |
| **Generative rec moves from architecture to lifecycle** | LION (self-evolving memory against "evolution conflict"), SCRec (cross-stage decoupling), P3Rec (prior+posterior distillation), TATK (top-K + KG-verified rerank, EMNLP'26), Safety-as-a-Constraint (constrained-GRPO explanations) |
| **KV cache: store less, reconstruct/repurpose more** | GVA (value-only keys, ~45% smaller persistent cache), Self-Indexing Attention (1-bit shared stage-wide index), Carryover Drafting (recycled rejected KV for drafting) — consistent with the SpectralShift/AttnKV threads from 09-15 |
| **Attention systems get a compiler layer** | AttnFuse (RoPE-first-class DSL, 2.10× over flex_attention), OpWeave (when-to-disaggregate theory for heterogeneous serving, ~1.8× cost cuts) |
| **Low-resource pre-training keeps tightening** | MoARa (module-aware rank allocation, 37% fewer steps), MoME (context-gated memory mixtures), MoE-as-retrievers (an active-parameter result) |
| **Safety shifts from whole-response to structure** | SaLT-DPO (segment-aware reasoning+answer alignment), ShieldVLA (HJ-reachability gated VLA safety), constrained-GRPO for rec explanation |
| **Agent memory is being budgeted and secured** | LIMBO (online inference-time memory allocation), Pull (reversible lazy materialization), PolicyMem (geometric policy memory), enforcement-gap diagnosis (+>4× attack reduction) |
| **Evaluation keeps auditing its own proxies** | CoArena (live real-time evaluation formalism), Reddit generative-search voice audit, synthetic-vs-authentic RAG divergence (CIKM'26), Vibe Patenting (judge-vs-attorney calibration) |
| **Markets/GT joins the collusion + congestion line** | MARL in congestible markets (tacit collusion under congestion), high-probability Nash regret for async potential games, incentive-compatible green training |

(Runner-ups worth a look, grep-verified unclaimed: **2609.14773's sibling** Pull line above; **2609.13889** PMPA persistent memory poisoning on harness agents; **2609.14850** Self-Orchestrating language models (PASTA/TIP/Planned Diffusion); **2609.13489** pre-retrieval query clustering for adaptive top-k RAG; **2609.13334** Agentic Company OS substrate inversion; **2609.14976** MemRiskBench trace-aware risk evaluation for long-horizon agents; **2609.13253** mean-field MARL; **2609.14088** consistency-robustness strategyproof scheduling — flagged 09-15 runner-ups are excluded by construction.)

(End of file — total 31 papers / 6 sections)