---
title: "arXiv AI Search 2026-10-05 — Ads Recommendation Scaling, Generative Advertising, and CTR Architecture (re-visit sweep)"
type: synthesis
created: 2026-10-05
updated: 2026-10-05
sources: [opencode-tool-output-109d45677001]
tags: [arxiv, recommendation, advertising, ctr, sequential-modeling, scaling-laws, generative-recommendation, semantic-id, cold-start, hypernetwork, query-decoding, serving-architecture]
---

# arXiv AI Search 2026-10-05 — CTR / Ads / Sequential Modeling re-visit sweep

> **Headline finding: this report contains ZERO new papers.** All 8 entries returned by the search were already ingested into this wiki months before today. This is a **re-visit / consolidation pass**, not an ingest. Read §2 (dedup ledger) before treating anything here as new.

## 1. Search Metadata

| Field | Value |
|---|---|
| **Date of search** | 2026-10-05 |
| **Search channel** | Web search; result snippets + highlight excerpts, not a direct arXiv API pull |
| **Source artifact** | `/Users/admin/.local/share/opencode/tool-output/tool_109d45677001N4V80BIszuDn14` (53,642 bytes / 186 lines) |
| **Total papers returned** | **8** |
| **New to this wiki** | **0** |
| **Already in `wiki/`** | **8** (dedup ledger in §2) |
| **Submission window covered** | 2026-01-27 → 2026-09-03 (not a single window; a topic-scoped backfill across the whole of 2026 so far) |

⚠️ **The search query string is not recorded in the source artifact.** The file begins mid-result with a `Title:` line and contains no query provenance. The topical scope below is therefore **reconstructed from the returned results**, not read from the search:

`{AI | LLM | recommendation | advertising | sequential modeling | CTR | games}` against `arxiv.org`, restricted to 2026 submissions.

Do not treat that reconstruction as the literal query. Any future run reproducing this sweep should capture the query string at fetch time.

⚠️ **Coverage note on "games":** the brief asked for games-relevant papers. **Zero of the 8 results are game papers.** The only game-adjacent string in the entire source artifact is a single illustrative ad-feature definition in LLM-HYPER (`feature_toys_games`, engagement with toys/games/puzzle categories). The games lane returned nothing here; game RL is covered by the separate [`../2026-10-04/game-rl-daily.md`](../2026-10-04/game-rl-daily.md) track.

## 2. Dedup Ledger — all 8 already claimed

Every ID was regex-checked against the whole of `wiki/` immediately before writing.

| # | arXiv ID | Paper | Files in `wiki/` already citing the ID | Earliest claim |
|---|---|---|---|---|
| 1 | [`2601.20083`](https://arxiv.org/abs/2601.20083) | LLaTTE | 14 | [`wiki/papers/ctr/llatte.md`](../../papers/ctr/llatte.md) (created 2026-05-29) |
| 2 | [`2602.01865`](https://arxiv.org/abs/2602.01865) | GRAB | 71 | [`../2026-05-29/conference-digest.md`](../2026-05-29/conference-digest.md) |
| 3 | [`2604.12096`](https://arxiv.org/abs/2604.12096) | LLM-HYPER | 24 | [`../2026-06-16/arxiv-daily.md`](../2026-06-16/arxiv-daily.md) §5.6 |
| 4 | [`2605.25583`](https://arxiv.org/abs/2605.25583) | LENS | 3 | [`../2026-07-22/arxiv-paper-check.md`](../2026-07-22/arxiv-paper-check.md) §3.9 |
| 5 | [`2602.22732`](https://arxiv.org/abs/2602.22732) | GR4AD | 53 | [`../2026-05-26/conference-digest.md`](../2026-05-26/conference-digest.md) |
| 6 | [`2609.03290`](https://arxiv.org/abs/2609.03290) | UniCon | 11 | [`../2026-09-05/arxiv-ai-search.md`](../2026-09-05/arxiv-ai-search.md) |
| 7 | [`2609.01240`](https://arxiv.org/abs/2609.01240) | ReST | 11 | [`../2026-09-02/arxiv-ai-search.md`](../2026-09-02/arxiv-ai-search.md) |
| 8 | [`2603.02999`](https://arxiv.org/abs/2603.02999) | OneRanker | 43 | [`../2026-05-24/arxiv-daily.md`](../2026-05-24/arxiv-daily.md) |

**GRAB (71 files) and GR4AD (53) and OneRanker (43) are among the most-cited arXiv IDs in this wiki.** They have been swept repeatedly by the daily jobs for five months. A plain keyword search returning them again is the expected outcome of a topic-scoped backfill, not a discovery failure — and it is the signal that this lane is saturated at daily cadence.

**Consequence for the wiki:** no new paper pages are warranted. The useful output of this run is §3 (consolidated architecture map) and §4 (three metadata discrepancies that this re-visit surfaced).

## 3. Consolidated Reference — 8 Papers

### Master comparison table

| # | Paper | arXiv | Date | Institution | Paradigm | Headline online result |
|---|---|---|---|---|---|---|
| 1 | LLaTTE | [2601.20083](https://arxiv.org/abs/2601.20083) | 2026-01-27 | **Meta** | Scaling laws + 2-stage async | **+4.3% conversion** (FB Feed & Reels), ~0.25% NE ↓ |
| 2 | GRAB | [2602.01865](https://arxiv.org/abs/2602.01865) | 2026-02-02 | **Baidu** | Generative CTR (sequence-first) | **+3.49% CTR / +3.05% CPM** |
| 3 | GR4AD | [2602.22732v2](https://arxiv.org/abs/2602.22732) | — | **Kuaishou** | Generative rec + real-time serving | **+4.2% ad revenue** |
| 4 | OneRanker | [2603.02999v1](https://arxiv.org/abs/2603.02999) | — | **Tencent (Weixin)** | Unified generation + ranking | **GMV-Normal +1.34%** |
| 5 | LLM-HYPER | [2604.12096](https://arxiv.org/abs/2604.12096) | 2026-04-13 | *unnamed* US e-commerce | LLM-as-hypernetwork, training-free | cold-start ≈ warm-start, **p = 0.62** |
| 6 | LENS | [2605.25583](https://arxiv.org/abs/2605.25583) | 2026-06-11 | *unstated in source* | Staged interaction granularity | offline only (12/12 positive cells) |
| 7 | ReST | [2609.01240](https://arxiv.org/abs/2609.01240) | 2026-09-01 | *unnamed* prod. ad platform | Rec-native Transformer scaling | **+1.31% AUC / +11.93% revenue** @ 50 ms P99 |
| 8 | UniCon | [2609.03290](https://arxiv.org/abs/2609.03290) | 2026-09-03 | **Meituan** | Unified context-centric | **+3.09% RPM / +2.07% CTR / +2.95% revenue** |

⚠️ **Version-suffix caveat.** Source URLs for GR4AD (`/abs/2602.22732v2`) and OneRanker (`/abs/2603.02999v1`) carry explicit versions, and `index.md` elsewhere cites OneRanker as `2603.02999v3` — i.e. the wiki tracks a **later version than this artifact's v1**. The numbers above are v1/v2 as they appear in the source artifact and may not reflect the current version of record.

---

### 1. LLaTTE: Scaling Laws for Multi-Stage Sequence Modeling in Large-Scale Ads Recommendation

- **arXiv**: [`2601.20083`](https://arxiv.org/abs/2601.20083) — *full text: [PDF](https://arxiv.org/pdf/2601.20083)*
- **Published**: 2026-01-27 · **Authors**: not listed in source artifact · **Institution**: **Meta** (stated in text: "largest user model deployment at Meta")
- **Existing wiki page**: [`wiki/papers/ctr/llatte.md`](../../papers/ctr/llatte.md)

**Abstract (highlight excerpt, verbatim):**
> We present LLaTTE (LLM-Style Latent Transformers for Temporal Events), a scalable transformer architecture for production ads recommendation. Through systematic experiments, we demonstrate that sequence modeling in recommendation systems follows predictable power-law scaling similar to LLMs. Crucially, we find that semantic features bend the scaling curve: they are a prerequisite for scaling, enabling the model to effectively utilize the capacity of deeper and longer architectures. To realize the benefits of continued scaling under strict latency constraints, we introduce a two-stage architecture that offloads the heavy computation of large, long-context models to an asynchronous upstream user model. We demonstrate that upstream improvements transfer predictably to downstream ranking tasks. Deployed as the largest user model at Meta, this multi-stage framework drives a 4.3% conversion uplift on Facebook Feed and Reels with minimal serving overhead, establishing a practical blueprint for harnessing scaling laws in industrial recommender systems.

**Key innovations:**
- **Content-aware scaling law** — the paper's most transferable claim. Semantic content embeddings are a **prerequisite** for steeper scaling, not a marginal add-on: *"with ID-only inputs, depth and sequence-length scaling quickly exhibit diminishing returns, whereas with content-enriched sequences, the same increases in L and T translate into substantially larger NE gains."* The stated corollary is that **analyzing model size and compute in isolation is insufficient to predict performance**.
- **Two-stage offload architecture** — asynchronous upstream user model triggered by high-value events (primarily conversions) writes cached user embeddings to a feature store; the compact online ranker reads them as dense features. Upstream consumes **>45× the sequence FLOPs** of its online counterpart.
- **Measured transfer ratio τ ≈ 50%** through a strict fixed-bandwidth information bottleneck (`d_transfer = 2048`). Concrete data point: a 0.14% upstream improvement → 0.07% downstream.
- **Width-before-depth ordering** — model width acts as a capacity bottleneck; sufficient width must be established before depth scaling becomes effective.
- **Serving constraint as design input** — production ranker caps at ~T ≈ 400 events/token per source under a strict per-request budget at trillion-request scale.

⚠️ **Caveat carried forward**: the existing wiki page `papers/ctr/llatte.md` contains a results table with figures (e.g. "encoder capacity 2× → +0.25% AUC, +0.8% revenue") that **do not appear in this source artifact**. Those numbers are unsourced in the artifact and should be re-verified against the paper before being cited.

---

### 2. GRAB: An LLM-Inspired Sequence-First CTR Prediction Modeling Paradigm

- **arXiv**: [`2602.01865`](https://arxiv.org/abs/2602.01865) — *source artifact URL was the HTML render: [2602.01865v1](https://arxiv.org/html/2602.01865v1)*
- **Published**: 2026-02-02 · **Authors**: not listed in source artifact · **Institution**: **Baidu** (stated: "Baidu's commercial advertising CTR ranking business", "Baidu home feed scenario")

**Abstract (highlight excerpt, verbatim):**
> Traditional Deep Learning Recommendation Models (DLRMs) face increasing bottlenecks in performance and efficiency, often struggling with generalization and long-sequence modeling. Inspired by the scaling success of Large Language Models (LLMs), we propose Generative Ranking for Ads at Baidu (GRAB), an end-to-end generative framework for Click-Through Rate (CTR) prediction. GRAB integrates a novel Causal Action-aware Multi-channel Attention (CamA) mechanism to effectively capture temporal dynamics and specific action signals within user behavior sequences. Full-scale online deployment demonstrates that GRAB significantly outperforms established DLRMs, delivering a 3.05% increase in revenue and a 3.49% rise in CTR. Furthermore, the model demonstrates desirable scaling behavior: its expressive power shows a monotonic and approximately linear improvement as longer interaction sequences are utilized.

**Key innovations:**
- **CamA (Causal Action-aware Multi-channel Attention)** — preserves heterogeneous action semantics that naive homogeneous serialization discards. Names the problem explicitly: existing GR models "typically ignore data heterogeneity."
- **Three-stage pipeline as DLRM/GR bridge** — sparse feature layer → dense tokenizer → sequence modeling layer, "enabling end-to-end training and inference along a single, unified computation path from input to output." The dense tokenizer is the specific mechanism that bridges legacy sparse feature engineering with tokenized sequential modeling.
- **Sequence Then Sparse (STS) training** — sequence packing gives efficiency but induces **distribution skew**: packed mini-batch samples share a user, so high intra-user correlation causes redundant updates on specific sparse IDs and overfitting to specific user-ad interactions. STS decouples long-range sequential modeling from robust sparse feature learning.
- **Three named deployment challenges** solved jointly: (i) bridging large-scale sparse feature engineering with tokenized sequential modeling; (ii) modeling heterogeneous action semantics lost by homogeneous serialization; (iii) training instability from sequence packing under strict optimization constraints.
- **Baselines beaten**: DIN, SIM(Soft), TWIN, HSTU, LONGER. Offline **+0.19% relative** over the best baseline; online A/B **~2 bp AUC**.

⚠️ Note a wording drift between the source's two figures: the highlight says "3.05% increase in revenue" while the body text says "**3.05% increase in CPM**." The same 3.05% figure is labelled both ways. CPM is the more precise term; treat "revenue" in the highlight as loose phrasing.

---

### 3. GR4AD: Generative Recommendation for Large-Scale Advertising

- **arXiv**: [`2602.22732v2`](https://arxiv.org/abs/2602.22732v2)
- **Published**: not present in source artifact · **Authors**: not listed in source artifact · **Institution**: **Kuaishou** (stated: "fully deployed in Kuaishou advertising system serving over 400 million users")

**Abstract (highlight excerpt, verbatim):**
> Generative recommendation has recently attracted widespread attention in industry due to its potential for scaling and stronger model capacity. However, deploying real-time generative recommendation in large-scale advertising requires designs beyond large-language-model (LLM)-style training and serving recipes. We present a production-oriented generative recommender co-designed across architecture, learning, and serving, named GR4AD (Generative Recommendation for ADdvertising). As for tokenization, GR4AD proposes UA-SID (Unified Advertisement Semantic ID) to capture complicated business information. Furthermore, GR4AD introduces LazyAR, a lazy autoregressive decoder that relaxes layer-wise dependencies for short, multi-candidate generation, preserving effectiveness while reducing inference cost, which facilitates scaling under fixed serving budgets. To align optimization with business value, GR4AD employs VSL (Value-Aware Supervised Learning) and proposes RSPO (Ranking-Guided Softmax Preference Optimization), a ranking-aware, list-wise reinforcement learning algorithm that optimizes value-based rewards under list-level metrics for continual online updates. For online inference, we further propose dynamic beam serving, which adapts beam width across generation levels and online load to control compute. Large-scale online A/B tests show up to 4.2% ad revenue improvement over an existing DLRM-based stack, with consistent gains from both model scaling and inference-time scaling. GR4AD has been fully deployed in Kuaishou advertising system with over 400 million users and achieves high-throughput real-time serving.

**Key innovations:**
- **UA-SID (Unified Advertisement Semantic ID)** — a fine-tuned MLLM embedding trained on real ad creatives via instruction tuning + co-occurrence learning. Directly targets a named gap: "**no end-to-end, fine-tuned advertisement LLM embedding exists**" prior to this work.
- **MGMR (Multi-Granularity-Multi-Resolution) RQ-Kmeans** — quantization to model *non*-semantic business information (conversion type, ads account), reduce SID collisions, improve codebook utilization. The distinction between semantic and business-signal channels is the load-bearing idea.
- **LazyAR decoder** — relaxes layer-wise autoregressive dependencies for short multi-candidate generation. **Inference-time scaling** as a distinct lever from model scaling.
- **RSPO (Ranking-Guided Softmax Preference Optimization)** — list-wise RL aligned directly to ranking NDCG, replacing heuristic chosen–rejected pair construction (cf. LambdaRank, SDPO) with a direct list-metric objective.
- **Dynamic Beam Serving (DBS)** — Dynamic Beam Width + Traffic-Aware Adaptive Beam Search, plus short-TTL cache. Adapts decoding compute to live traffic and latency budget.
- **Serving envelope**: **<100 ms latency, 500+ QPS per L20**; deployed model size **0.16B**; closed-loop architecture integrating reward estimation, online learning, and real-time indexing.

---

### 4. OneRanker: Unified Generation and Ranking with One Model in Industrial Advertising Recommendation

- **arXiv**: [`2603.02999v1`](https://arxiv.org/abs/2603.02999v1) — *see version caveat above; `index.md` cites a v3*
- **Published**: not present in source artifact · **Authors**: not listed in source artifact · **Institution**: **Tencent** (stated: "Tencent's WeiXin channels advertising system")

**Abstract (highlight excerpt, verbatim):**
> The end-to-end generative paradigm is revolutionizing advertising recommendation systems, driving a shift from traditional cascaded architectures towards unified modeling. However, practical deployment faces three core challenges: the misalignment between interest objectives and business value, the target-agnostic limitation of generative processes, and the disconnection between generation and ranking stages. Existing solutions often fall into a dilemma where single-stage fusion induces optimization tension, while stage decoupling causes irreversible information loss. To address this, we propose OneRanker, achieving architectural-level deep integration of generation and ranking. First, we design a value-aware multi-task decoupling architecture. By leveraging task token sequences and causal mask, we separate interest coverage and value optimization spaces within shared representations, effectively alleviating target conflicts. Second, we construct a coarse-to-fine collaborative target awareness mechanism, utilizing Fake Item Tokens for implicit awareness during generation and a ranking decoder for explicit value alignment at the candidate level. Finally, we propose input-output dual-side consistency guarantees. Through Key/Value pass-through mechanisms and Distribution Consistency (DC) Constraint Loss, we achieve end-to-end collaborative optimization between generation and ranking. The full deployment on Tencent's WeiXin channels advertising system has shown a significant improvement in key business metrics (GMV - Normal +1.34%), providing a new paradigm with industrial feasibility for generative advertising recommendations.

**Key innovations:**
- **The dilemma it names is the contribution.** Single-stage fusion (injecting eCPM into MTP heads directly) induces **optimization tension** between interest coverage and value optimization in a shared representation space; stage decoupling (generate-then-rank) causes the generator to miss ranking objectives, "leading to systematic filtering of high-value candidates at the generation stage."
- **Value-aware multi-task decoupling** — keeps MTP's multi-interest heads for coverage breadth, adds a dedicated value-aware head; shared user representations but **decoupled output spaces via independent task tokens**. Task ordering priors (**impression → click → conversion → value**) with causal mask let high-level value tasks absorb knowledge from low-level interest tasks.
- **Fake Item Tokens** — K-means over the entire item space for *coarse-grained* implicit target awareness during generation; plus a dual-channel representation (task-semantic + target-aware) fused by inner product at retrieval for explicit target sensitivity.
- **Dual-side consistency** — input side: ranking decoder's Key/Value built from *both* the original multi-interest and the refined representations, so ranking inherits generation information. Output side: DC mechanism propagates business-value signals from ranker back to generator as **soft labels**. Joint loss `L_total = αL_MTP + βL_rank + γL_consistency` gives gradient-level collaboration, letting the generator "anticipate" ranking preferences during training.
- **Architecture**: Step 1 uses GPR's tokenization (user / context / content / item tokens) with an **HSTU Decoder-only** backbone; autoregressive MTP generates multiple semantic-ID paths in parallel in one forward pass.

---

### 5. LLM-HYPER: Generative CTR Modeling for Cold-Start Ad Personalization via LLM-Based Hypernetworks

- **arXiv**: [`2604.12096`](https://arxiv.org/abs/2604.12096) — *source artifact URL was the HTML render: [2604.12096v1](https://arxiv.org/html/2604.12096v1)*
- **Published**: 2026-04-13 · **Authors**: not listed in source artifact · **Institution**: **unnamed** ("one of the top e-commerce platforms in the U.S."); LLM backbones used are Google **Gemini-2.5-Pro / 2.5-Flash**, OpenAI **GPT-4o**, **GPT-5.1**

**Abstract (highlight excerpt, verbatim):**
> LLM-HYPER: Generative CTR Modeling for Cold-Start Ad Personalization via LLM-Based Hypernetworks
>
> On online advertising platforms, newly introduced promotional ads face the cold-start problem, as they lack sufficient user feedback for model training. In this work, we propose LLM-HYPER, a novel framework that treats large language models (LLMs) as hypernetworks to directly generate the parameters of the click-through rate (CTR) estimator in a training-free manner. LLM-HYPER uses few-shot Chain-of-Thought prompting over multimodal ad content (text and images) to infer feature-wise model weights for a linear CTR predictor. By retrieving semantically similar past campaigns via CLIP embeddings and formatting them into prompt-based demonstrations, the LLM learns to reason about customer intent, feature influence, and content relevance. To ensure numerical stability and serviceability, we introduce normalization and calibration techniques that align the generated weights with production-ready CTR distributions. Extensive offline experiments show that LLM-HYPER significantly outperforms cold-start baselines in NDCG@10 by 55.9%. Our real-world online A/B test on one of the top e-commerce platforms in the U.S. demonstrates the strong performance of LLM-HYPER, which drastically reduces the cold-start period and achieves competitive performance. LLM-HYPER has been successfully deployed in production.

**Key innovations:**
- **Training-free hypernetwork** — differs from existing hypernetwork solutions that "have strict dependency of training data." The LLM emits feature-wise weights for a **linear** CTR predictor directly from ad content + user-feature definitions.
- **Multimodal CLIP-retrieved few-shot demonstrations** — semantically similar past campaigns (CLIP embeddings) formatted as prompt demonstrations; **5-shot CoT, temperature 0.5** for all variants.
- **The deployment decoupling is the engineering insight** — weight generation is slow and offline; serving is fast and scalable. Before a cold-start ad's launch date there is ample time to generate weights. A **label-independent normalization and calibration** mechanism then stabilizes them. Serving is a linear model.
- **Ablation findings**: even **zero-shot achieves +33.3% NDCG@10** (strong cross-modal generalization); excluding visual features "drastically reduces performance across all variants"; 5-shot is the best overall balance, 3-shot marginally better on NDCG@10 — a moderate number of high-quality examples suffices.
- **Interpretability as a byproduct** — the framework yields human-readable reasoning + generated weights. Worked example on `feature_toys_games`: construction-set ad → large weight (strong relevance); outdoor-furniture ad → very low weight (conflicting); weakly-relevant ad → neutral.
- **Comparative finding worth carrying**: `EmbT5` (offline ad-relevance embeddings) fails in strict cold start due to a **big context gap between offline ad relevance and online user feedback**, while LLM-HYPER bridges it. The LLM-R / LLM-TR generative recommenders are *worst* on all metrics due to **hallucination and out-of-distribution prediction** (invented ad names, ranking zero-interaction novel ads to the top).
- **Online result**: statistically indistinguishable from the ideal warm-start model in a 30-day A/B (**p = 0.62**).

---

### 6. LENS: A Staged Design for Interaction Granularity in Sequential CTR Prediction

- **arXiv**: [`2605.25583`](https://arxiv.org/abs/2605.25583)
- **Published**: 2026-06-11 · **Authors**: not listed in source artifact (see §4.2) · **Institution**: not stated in source artifact; benchmarks include a **Tencent** dataset (TAAC)
- **Type note**: this is an **offline / benchmark paper** — the only entry in this set with no online A/B result.

**Abstract (highlight excerpt, verbatim):**
> In sequential CTR prediction, a central design question is at what granularity the target should interact with the user behaviour sequence. Existing models mainly follow two routes. Raw-item architectures such as DIN let the target score each item in the sequence directly. This relies on well-trained item embeddings and becomes brittle for sparse items. Latent-query architectures such as HyFormer, MixFormer, and OneTrans build query representations by combining the target with other information. This is more robust across item-density regimes but blunter: target-specific control is diluted. We propose LENS to restore target-specific control within these coarser bottlenecks. LENS has two modules: a Target-Conditioned Query Gate (TCQG) for query activation and a Target-Conditioned Position Bias (TCPB) for history retrieval. We further introduce Query-Specific Position Bias (QueryPos), a simple static position-aware reference for latent-query backbones. Across three representative latent-query backbones and four datasets, the combined QueryPos+LENS design achieves positive total-gain point estimates in all twelve evaluated backbone–dataset cells. We also identify a density-dependent conditioning rule: as item density decreases, the optimal condition source shifts from item-only to item-plus-sequence.

**Key innovations:**
- **Reframes the architecture choice as a two-route trade-off** — raw-item (DIN) = precise target control but brittle on sparse items; latent-query (HyFormer / MixFormer / OneTrans) = robust across density regimes but blunted target control. LENS's thesis: the *interaction bottleneck is fixed once the architecture is chosen*, so target-specific control must be added back explicitly rather than hoped for.
- **Three staged modules, all zero-initialised** so each can be added incrementally and the model starts as the unmodified backbone:
  - **QueryPos** (Stage 2) — per-query learnable position prior, **applied in cross-attention rather than self-attention** (differs from RoPE/ALiBi/T5-bias/Transformer-XL, all self-attention or sequence-level).
  - **TCQG** (Stage 3) — controls *which* latent queries are active for a given candidate.
  - **TCPB** (Stage 3) — controls *where* those active queries retrieve from history.
- **Portability is the primary evidence, not peak score** — the same Stage 2 + Stage 3 additions transfer to MixFormer and OneTrans, which "neither includes a dedicated query-specific position component." All **12/12 backbone–dataset cells** show positive total-gain point estimates, across ~10³ down to ~1.1 samples/item.
- **Density-driven conditioning rule with a located boundary** — condition source switches from item-only to item+sequence **below ~50 samples/item**. Verified per dataset: KuaiRec (~1000 samples/item) item-only wins; TaobaoAd (~59) tied, item-only selected by the pre-specified rule; TAAC (~22) and KuaiRand (~1.1) item+sequence wins. Rationale: reliable item embeddings remove the need for additional sequence context.
- **Benchmark**: TAAC — sparse-vocabulary industrial dataset from the Tencent Advertising Algorithm Competition 2025, ~22 training samples per item, time-split protocol, sequence length 100.
- ⚠️ **Honest reading of the headline**: "positive total-gain *point estimates*" is not a significance claim. The source reports no confidence intervals or p-values for the 12 cells.

---

### 7. ReST: From Language to Behavior — Scaling Sequence Transformers for Industrial Recommendation Ranking with Rec-Native Designs

- **arXiv**: [`2609.01240`](https://arxiv.org/abs/2609.01240)
- **Submitted**: 2026-09-01 · **Authors**: Jie Chen, Xiangqian Yu, Yanchao Lian, Tan Lu, Run Yang, Zhengchun Shang, Xing Wang, Cheng Chen, Ke Hu, Qiang Li, Tianjiu Yin, Xiaobing Liu · **Institution**: *not named in the source artifact* — see §4.1

**Abstract (verbatim):**
> Scaling Transformers has driven large gains in language modeling, but transplanting this to behavior-sequence modeling in production ranking is challenging: recommendation differs in signal quality, where behavior sequences are noisy, temporally irregular, and sparsely supervised, and in computation asymmetry, where each request scores many candidates against one shared user history under tight latency budgets. We propose ReST, a recommendation-native Transformer scaling framework. For signal quality, it introduces a sequence encoder with dual-gated attention, rotary positional and temporal embedding, stabilized residual normalization, and training-only auxiliary objectives. For computation asymmetry, it factorizes ranking into a heavy reusable encoder and a lightweight cross decoder with projection-free KV attention and token-specific parameterization, coupling user-level shared-prefix training with shared-prefix serving for compute-once, decode-many-times ranking. Across industrial and public benchmarks, ReST achieves higher accuracy and scales more consistently along sequence length, depth, and width, where LLM-style Transformer blocks saturate. A one-week online A/B test on a production advertising platform improves online AUC by 1.31% and lifts a core revenue metric by 11.93% within a 50 ms P99 budget; ReST has since been fully deployed in production, showing that behavior-sequence scaling remains a promising, under-exploited axis for production ranking.

**Key innovations:**
- **Names the two structural obstacles explicitly** — (a) **signal quality**: sequences are noisy, temporally irregular, sparsely supervised (vs. clean uniformly-supervised language); (b) **computation asymmetry**: one shared user history scored against *many* candidates per request, under a tight latency budget. The second is the genuinely recommendation-specific one.
- **Signal-quality adaptations**: dual-gated attention, rotary positional **and temporal** embedding, stabilized residual normalization, training-only auxiliary objectives.
- **Computation-asymmetry solution**: heavy reusable encoder + lightweight cross decoder with **projection-free KV attention** and **token-specific parameterization**, coupling shared-prefix *training* with shared-prefix *serving* → **compute-once, decode-many-times** ranking.
- **The central empirical claim is comparative**: LLM-style Transformer blocks **saturate** along sequence length, depth and width where ReST does not. This is a claim about the *baseline failing*, not only about ReST succeeding.
- **Serving envelope**: 50 ms P99, one-week A/B, **fully deployed in production**.

---

### 8. UniCon: A Unified Context-Centric Modeling Paradigm for CTR Prediction

- **arXiv**: [`2609.03290`](https://arxiv.org/abs/2609.03290)
- **Submitted**: 2026-09-03 · **Authors**: Jiajun Cui, Zhengqi Xu, Fan Zhang, Zhangteng, Gu Tang, Honghong Zhu, Mengxi Wu, Yulin Liang, Xingxing Wang · **Institution**: **Meituan** (stated: "On Meituan search advertising")

**Abstract (verbatim):**
> Unified modeling has become a major direction for industrial click-through rate (CTR) prediction. Existing approaches typically unify sequential and non-sequential signals at the token level, model their interactions in a shared backbone, and increase model capacity to improve scaling behavior. However, this division originates from legacy feature-engineering practice and is misaligned with the underlying decision process. User behavior is inherently a sequence of homogeneous context units; at the level of input organization, historical behavior and the current request differ only in whether their outcomes are observed or remain to be predicted. Treating them as heterogeneous signals obscures structural dependencies within the user's decision context, limiting both scaling efficiency and prediction quality. This limitation is particularly pronounced in context-rich scenarios such as e-commerce shelves and waterfall feeds. To address this, we propose UniCon, a unified context-centric modeling architecture that treats the request context as the basic modeling unit and organizes history and prediction targets as homogeneous context units. Intra-context attention captures local coupling among items within a context (Locality), while inter-context attention models the dynamic evolution of decision states across contexts (Dynamics). This organization bridges the structural gap between history and target and supports more effective scaling of unified CTR models. Context-unit-level sequence compression further reduces deployment overhead. On Meituan search advertising, UniCon improves offline AUC by 0.0139 over a strong production baseline and achieves statistically significant online lifts of 3.09% in RPM, 2.07% in CTR, and 2.95% in revenue.

**Key innovations:**
- **The diagnosis is the contribution** — the sequential/non-sequential split "originates from legacy feature-engineering practice and is **misaligned with the underlying decision process**." User behavior is a sequence of **homogeneous context units**; history and the current request differ *only* in whether outcomes are observed or pending. Treating them as heterogeneous obscures structural dependencies.
- **Context as the modeling unit** — intra-context attention for **Locality** (item coupling within a context) + inter-context attention for **Dynamics** (evolution of decision state across contexts).
- **Context-unit-level sequence compression** for deployment overhead, not just accuracy.
- **Result**: offline **AUC +0.0139** over a strong production baseline; online **RPM +3.09% / CTR +2.07% / revenue +2.95%**, all statistically significant.
- **Scope of the argument**: strongest in context-rich surfaces — e-commerce shelves, waterfall feeds.

---

## 4. Metadata Discrepancies Surfaced by This Re-Visit

Three items where this artifact and existing wiki content disagree. None changes a paper's finding; all three are attribution risks.

### 4.1 ⚠️ ReST institution — unnamed here vs. "ByteDance" in the wiki

- **Source artifact**: says only "a production advertising platform." **No institution is stated anywhere in the artifact.** Per this wiki's standing affiliation discipline, institutions are read only from the paper's own author block and **never inferred**.
- [`../2026-10-01/arxiv-ai-search.md`](../2026-10-01/arxiv-ai-search.md) records ReST as **"ByteDance"** — with no `*inferred*` marker, unlike its HELIX entry which *is* marked inferred.
- **Unresolved.** The 2026-10-01 report should either mark ByteDance as inferred or resolve it from the paper's own author block. The 12 author names in the artifact are unresolvable to an employer from the artifact alone.
- **Recommendation**: verify against `arxiv.org/html/2609.01240v1` and correct whichever page is wrong. Do not cite "ByteDance / ReST" unqualified until then.

### 4.2 ⚠️ LENS authors — attributed in the wiki, absent from the source

- [`../2026-07-22/arxiv-paper-check.md`](../2026-07-22/arxiv-paper-check.md) §3.9 lists **"Yuan Wang, Yue Liu, Jun Zhang, Jie Jiang"** for `2605.25583`, and dates it **25 May 2026**.
- **Source artifact**: lists **no authors** and dates it **2026-06-11**.
- **Two problems**: (a) the four-name attribution has no provenance in this artifact; (b) **the dates disagree by 17 days**, which matters because `2605.25583` is a May-ID paper whose v1 would be May and whose listed publication date is June — consistent with a **v2/revision**, but the 2026-07-22 report gives no version suffix.
- **Recommendation**: treat the four-name author list as **unverified**; the institution (unstated here; TAAC is a Tencent-competition dataset) likewise.

### 4.3 ⚠️ LLaTTE wiki page contains figures not present in any source artifact

As flagged inline at entry 1: [`../../papers/ctr/llatte.md`](../../papers/ctr/llatte.md) carries a table of AUC/revenue/compute deltas per scaling operation that appears in **no** available source text. Those numbers are currently unsourced and are the kind of figure that gets quoted downstream. Verify against the paper before reuse, or mark them provisional on the page itself.

## 5. Cross-Cutting Observations

1. **The field has converged on "one model, several stages" over "one stage, fused."** GR4AD (LazyAR + dynamic beam), OneRanker (dual-side consistency with a ranking decoder inside the generative model), LLaTTE (async upstream user encoder + compact online ranker), ReST (heavy encoder + light cross-decoder, compute-once/decode-many), GRAB (dense tokenizer as the DLRM↔GR bridge). Five independent industrial teams, five architectures, one shape: **separate the expensive reusable computation from the cheap per-request computation, and spend the savings on sequence depth.**
2. **Every paper here attacks the *transfer* of LLM machinery, and the point of attack is always the same: positional and semantic assumptions.** LLaTTE finds RoPE-style scale transfer breaks without semantic features (content bends the curve). GR4AD finds no fine-tuned ad-LLM embedding exists. UniCon finds the token-level sequential/non-sequential split is a legacy artifact, not a structural fact. LENS separates per-query cross-attention position bias from self-attention RoPE/ALiBi. ReST finds LLM blocks *saturate* where rec-native blocks do not. **The primitives transfer; the assumptions do not.**
3. **Latency is treated as a first-class modelling constraint, and it is reported.** LLaTTE: >45× FLOP asymmetry between stages. ReST: 50 ms P99 with a compute-once/decode-many structure. GR4AD: <100 ms, 500+ QPS per L20, adaptive beam width. **A CTR paper that reports offline AUC without a serving envelope is now visibly incomplete** — GR4AD's paper says exactly this.
4. **Cold start is being reframed as a weight-generation problem rather than a data problem.** LLM-HYPER generates the predictor's weights from ad content with no training data at all, and closes the gap to an ideal warm-start model at p = 0.62. Combined with the offline-embedding failure it documents (EmbT5's context gap), this is a negative result *for the offline-embedding approach* hiding inside a positive result for the LLM approach.
5. **⚠️ Online A/B disclosure is near-universal — with one exception.** 7 of 8 report live business metrics (conversion, CTR/CPM, revenue, GMV, RPM). **LENS reports none**, and its headline is "positive point estimates" across 12 cells with no significance test. It is also the only paper here without a production deployment. Treat it as an architectural-design paper, not an effectiveness claim.
6. **The keyword-search lane in this wiki is saturated.** GRAB has been returned to this wiki **71 times**, GR4AD **53**, OneRanker **43**. A topic-scoped backfill over the 2026 CTR/ads lane can no longer produce new material — it can only re-surface canonical industrial systems. **This lane should move to a lower cadence or narrower triggers** (new-ID range above the current ceiling `2610.02210`, per the 2026-10-04 game-RL run) rather than a recurring full-keyword sweep.

## 6. Method & Discipline

- **Dedup**: whole-`wiki/` regex per arXiv ID, run immediately before writing. **8/8 IDs already present.** Title-level pass on 8 distinctive strings (`LLaTTE`, `GRAB:`, `LLM-HYPER`, `UniCon`, `ReST, a recommendation`, `GR4AD`, `LENS`, `OneRanker`) → no unclaimed hits.
- **Abstracts**: quoted verbatim from the source artifact. Where the artifact itself was a highlight/highlight-plus-body blend, this is marked *(highlight excerpt)* rather than *(abstract)*.
- **Institutions**: taken only from text inside the artifact. Three are unstated (ReST, LENS, LLM-HYPER's platform) and are recorded as such. **No institution was inferred from author names or email domains** — see §4.1 for the one place this discipline is currently violated elsewhere in the wiki.
- **No new paper pages created.** Only this synthesis file.
- **Not done**: no arXiv API re-fetch of any of the 8 IDs. Abstracts and numbers here are as found in the source artifact; version drift against the current arXiv record of each paper is possible and is flagged for GR4AD/OneRanker in §3.

## 7. Related Pages

- [`../2026-10-04/arxiv-paper-check.md`](../2026-10-04/arxiv-paper-check.md) — separate CTR/AI sweep, older window
- [`../2026-10-04/game-rl-daily.md`](../2026-10-04/game-rl-daily.md) — the games lane (empty in this sweep)
- [`../2026-10-04/arxiv-ai-search.md`](../2026-10-04/arxiv-ai-search.md) — documents the current-window CTR/ads **coverage gap**
- [`../2026-10-01/arxiv-ai-search.md`](../2026-10-01/arxiv-ai-search.md) — §4.1's ByteDance attribution to correct
- [`../ctr-scaling-landscape.md`](../ctr-scaling-landscape.md) — cross-window synthesis of the scaling-law thread LLaTTE/ReST/UniCon extend
- [`../../papers/ctr/llatte.md`](../../papers/ctr/llatte.md) — §4.3's unsourced-figure page
