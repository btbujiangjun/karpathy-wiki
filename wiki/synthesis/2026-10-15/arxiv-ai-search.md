---
title: "arXiv AI Research Paper Search Report"
type: synthesis
created: 2026-10-15
updated: 2026-10-15
sources: [arxiv.org]
tags: [arxiv, AI, LLM, recommendation, advertising, sequential-modeling, CTR, e-commerce-search, reranking, cold-start, GNN-recommendation, GRPO, hybrid-linear-attention, KV-cache, memory-modules, MoE, speculative-decoding, diffusion-LM, agent-memory, model-routing, auctions, mechanism-design, multi-agent, poker, daily-digest]
---

# arXiv AI Research Paper Search Report — 2026-10-15

Generated: 2026-10-15 (Thursday). **Fresh Mon–Tue submission block (2026-10-13 → 2026-10-14)**, swept via the arXiv export API across 8 target categories: **cs.AI, cs.LG, cs.CL, cs.CV, cs.IR, cs.GT, cs.MA, cs.NE**. **1,234 unique new-submission IDs** extracted (ID window **2610.17503–2610.20610**); **26 papers featured in full + 9 runner-ups**, every ID **grep-verified 0 hits in `wiki/`** at selection time.

**Methodology**: `export.arxiv.org/api/query` with `submittedDate:[202610130000 TO 202610160000]` per category, sorted `submittedDate` descending and paginated (`start`/`max_results`) so the large categories (cs.LG 309, cs.CV 241, cs.CL 218, cs.AI 206 primary) were captured in full. Titles/abstracts/authors parsed from the Atom feed; candidates then screened on target topics (AI / LLM / recommendation / advertising / sequential modeling / CTR / games / auctions & mechanism design / attention & memory architecture / MoE & KV-cache / agent memory). XML cached under the pre-approved temp dir `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/arxiv-search-1015/` and cleaned up after. **Institutions are not printed in the arXiv API** — the affiliation field is author-inferred and marked *tentative* throughout; treat it as a lead, not a citation.

> **Dedup / sibling note**: the sibling `game-rl-daily` job (2026-10-15) covered game IDs in the **2026-10-11 → 2026-10-13** announced block. This report's window (**2026-10-13 → 2026-10-14**) overlaps that block only on 10-13, and every game/MARL/opponent-modeling ID the sibling already claimed (2610.17391, 2610.18229, 2610.18354, 2610.18808, 2610.18560, 2610.17201, 2610.16450, 2610.16848, …) was **excluded from this report**. The only pure-game paper featured here (**SafeAdapt-Poker 2610.20473**) is a 10-14 submission *not* in the sibling's set.

## Summary Statistics

| Scope | Value |
|---|---|
| Window covered | Submissions 2026-10-13 → 2026-10-14; ID range 2610.17503–2610.20610 |
| Categories swept | cs.AI, cs.LG, cs.CL, cs.CV, cs.IR, cs.GT, cs.MA, cs.NE |
| Unique IDs parsed | 1,234 (cs.LG 309, cs.CV 241, cs.CL 218, cs.AI 206, stat.ML 38, cs.IR 15, cs.GT 16, cs.MA 11, cs.NE 2, + cross-listings/other) |
| Featured in full in this report | 26 papers (5 sections) + 9 shortlisted runner-ups |
| Direct advertising / CTR / pCTR papers | **1** advertisement-delivery agentic system (**AdCoEvo 2610.19454**) + **1** sponsored-search credit-assignment paper (**CASI 2610.20293**); no classical pCTR model paper |
| Rec / search / e-commerce relevance | 11 citable papers (seq-rec debiasing, LLM-recommender GRPO, cold-start GNN, explainable rec, basket-choice, conversational rec sim, LLM sparse-retrieval fusion, generative-vs-dense retrieval, subject indexing, slate presentation) |
| Mailing status | API `submittedDate` window; blocks announce for 10-13 and 10-14; terminus at **2610.20610** |

**Theme of the window**: a **sequential-memory / long-context architecture wave** (hybrid-linear-attention speculative drafting, test-time-trained KV compaction, external neural memory modules, depth-as-memory, joint-subspace sparse attention, elastic transformers) co-existing with a **recommendation-methodology-and-agent thread** (popularity-bias sparse objectives, responder-noise-free GRPO for LLM recommenders, cold-start graph distillation, explainable LightGCN, advertising-delivery multi-agent co-evolution) and a **strong mechanism-design cluster** (price-of-anarchy of agentic first-price auctions, truthful topology-aware model routing, improved combinatorial auctions, geographic block-proposing games).

---

## 1 Recommendation, Search, Advertising & E-Commerce

### 1.1 AdCoEvo — Co-Evolving Multi-Agent Advertising Delivery (2610.19454)
- **Title**: AdCoEvo: A Co-Evolving Multi-Agent Advertising Delivery System
- **Authors**: Tianzhu Hu, Hang Yu, Zeyuan Zhao, Zeyu Pan, Huan Luo, Chun Gan, Mingzhe Cao, Liubin Wang, Mingming Li, Jiao Dai, Jizhong Han, Songlin Hu
- **Institution**: CAS Institute of Information Engineering-aligned (*tentative* — Han/Hu)
- **Date**: Wed 14 Oct 2026 (cs.AI, cs.IR, cs.MA)
- **arXiv**: https://arxiv.org/abs/2610.19454
- **Abstract**: Digital-advertising **delivery** is the link between marketing objectives and returns; existing automation covers individual tasks (bidding, budget allocation) but overall coordination stays manual and personal experience does not become reusable operational capability, and systems must update strategies as markets shift. **AdCoEvo** is a **co-evolving multi-agent advertising-delivery system** that connects delivery decisions across timescales and operational granularities through **role specialization**: diagnostic results guide account planning and strategy adjustment for the next period, and the multi-agent system updates its model parameters from actual delivery outcomes, continually improving via mutual feedback among **planning, adjustment, and diagnosis** (co-evolution). vs a rule-based operational baseline (Rule), AdCoEvo raises **advertiser value by 14.02%** while cutting **cost per acquisition by 7.07%**; vs a fixed-parameter multi-agent system it raises value by **3.96%** and lowers CPA by **1.24%**.
- **Key Innovations**: (1) end-to-end advertising-operations automation via a role-specialized multi-agent loop; (2) planning↔adjustment↔diagnosis **mutual-feedback co-evolution** that turns operator experience into reusable models; (3) advertiser-value / CPA evidence against both rule-based and fixed-parameter agent baselines.
- **Venue**: Preprint.

### 1.2 PR-entmax — Popularity-Aware Sparse Objective for Sequential Recommendation (2610.17823)
- **Title**: Mitigating Popularity Bias in Sequential Recommendations with Sparse Prior-Regularized Objective
- **Authors**: Anton Pembek, Anton Klenitskiy, Alexander Savchenko, Alexey Vasilev
- **Institution**: industrial/recsys-aligned (*tentative*)
- **Date**: Tue 13 Oct 2026 (cs.IR)
- **arXiv**: https://arxiv.org/abs/2610.17823
- **Abstract**: Popularity bias over-exposes popular items and shrinks catalog coverage. Proposes **PR-entmax**, a **sparse prior-regularized objective** making popularity correction **context-dependent**. Derived from a generalized variational principle in which an item-popularity prior is folded directly into a **sparse probability mapping**, yielding a *popularity-aware active support*: the set of items receiving non-zero probability (and thus non-zero gradients) is determined jointly by **contextual relevance and item popularity**. The prior therefore affects not only item probabilities but **which items participate in gradient updates**. No architecture change — only the loss function changes; at inference the prior is removed and items are ranked by learned contextual relevance alone. Across multiple benchmarks and sequential-rec architectures it consistently reduces popularity bias while preserving or improving relevance.
- **Key Innovations**: (1) popularity prior embedded in a sparse probability map (active-support geometry); (2) prior reshapes the **gradient support**, not just the output distribution; (3) loss-only, architecture-agnostic debiasing that advances the relevance–debiasing trade-off.
- **Venue**: Preprint.

### 1.3 ReMaRk — Removing Responder Noise from GRPO for LLM Recommenders (2610.17771)
- **Title**: Many Right Answers, One Training Example: Removing Responder Noise from GRPO for LLM Recommenders
- **Authors**: Xin Li, Hao Jiang, Jinghao Guo, Weisi Lin, Chau Yuen
- **Institution**: academic/industrial (*tentative* — Yuen)
- **Date**: Tue 13 Oct 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2610.17771
- **Abstract**: A recommendation request on Reddit draws several replies, each naming different titles — so which replies should a generated list be rewarded against under RL? The SOTA recipe, **Rank-GRPO**, picks one reply per training example, so the advantage mostly records **which reply was drawn (85% of its variance)** rather than how good the list is. **ReMaRk** argues RL should train on the **request, not each answer**: it scores every list once against the **union of all replies' titles** and samples each request equally, making RL cheaper. On seven backbones and three datasets, ReMaRk reaches the validation recall of **2,000 per-reply RL steps in 25–53% of the steps**; trained to convergence it is never significantly behind Rank-GRPO and in four of seven pairs matches Rank-GRPO's best with fewer GPU-hours. The reward also helps on ProtoQA (≈100 answers per question), pointing to a simple rule: **reward multiple valid human answers jointly**.
- **Key Innovations**: (1) diagnoses responder-noise as 85% of Rank-GRPO's advantage variance; (2) union-of-answers reward + per-request sampling; (3) broad (7-backbone / 3-dataset) compute-efficiency win for RL-trained LLM recommenders.
- **Venue**: Preprint.

### 1.4 DualGCN — Dual-Branch Graph Distillation for Cold-Start Recommendation (2610.19578)
- **Title**: Bridging the Topological Divide: Dual-Branch Graph Distillation with Semantic Priors for Robust Cold-Start Recommendation
- **Authors**: Yuanfeng Qiu
- **Institution**: single author (*tentative*)
- **Date**: Wed 14 Oct 2026 (cs.IR, cs.LG)
- **arXiv**: https://arxiv.org/abs/2610.19578
- **Abstract**: Graph Collaborative Filtering suffers **catastrophic representation collapse in strict cold-start** scenarios from the topological isolation of unobserved items; directly mapping isolated semantic attributes into a globally topology-driven collaborative space causes degradation and optimization conflict. **DualGCN** is a **dual-branch graph knowledge-distillation** framework with a decoupled two-stage training paradigm: it first builds a robust collaborative **teacher** whose item representations are anchored by a **topology-smoothed semantic prior** (reshaping the latent manifold), then a **semantic student** branch uses **residual mapping + magnitude-agnostic cosine distillation** for high-fidelity cross-modal alignment without disrupting collaborative signals. A **dynamic norm-reconstruction** mechanism calibrates novel/warm item scales at global retrieval. Across three real-world benchmarks it significantly beats SOTA in strict cold-start while preserving accuracy for active items.
- **Key Innovations**: (1) names the cold-start topological-divide / representation-collapse failure; (2) topology-smoothed semantic-prior teacher + magnitude-agnostic student distillation; (3) dynamic norm reconstruction for retrieval scale calibration.
- **Venue**: Preprint.

### 1.5 xLightGCN — Explainable GNN Recommendation with Most-Influential Peers (2610.19446)
- **Title**: xLightGCN: Explainable Graph Neural Network Based Recommendation Systems with Most Influential Peers
- **Authors**: Calder Johnson, Robin Cohen
- **Institution**: University of Waterloo-aligned (*tentative* — Cohen)
- **Date**: Wed 14 Oct 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2610.19446
- **Abstract**: Recommendation systems are ubiquitous in online social networks but many modern approaches are **opaque black boxes** that are hard to audit or trust. Presents an **exact, graph-based approach** for generating explanations of recommendation decisions, arguing that in the risk-sensitive sociotechnical context of user-facing AI, **explainability is a key pillar of trustworthiness**. The technique is built on **LightGCN-like architectures** and provides an assurance mechanism with specific advantages including **interpretable explanations via "most influential peers"** and a **theoretically guaranteed measure of explanation fidelity**; limitations and future directions discussed.
- **Key Innovations**: (1) exact graph-based explanation generation for LightGCN-class models; (2) theoretically guaranteed explanation-fidelity measure; (3) positions explainability as an assurance mechanism for risk-sensitive recommenders.
- **Venue**: Preprint.

### 1.6 Revisited Negative Sampling for Retail Basket-Choice Modeling (2610.17963)
- **Title**: Better Capturing Interactions Between Products in Retail: Revisited Negative Sampling for Basket Choice Modeling
- **Authors**: Jules Désir, Vincent Auriau, Martin Možina, Emmanuel Malherbe
- **Institution**: Criteo-aligned (*tentative* — Malherbe/Auriau)
- **Date**: Tue 13 Oct 2026 (cs.LG, cs.AI)
- **arXiv**: https://arxiv.org/abs/2610.17963
- **Abstract**: Brick-and-mortar retailers need to capture **interactions between products** (cannibalization vs complementarity) for **assortment optimization** and promotion planning. Proposes a **shopping-basket model** that learns embeddings representing interactions between **products, prices, and stores**, built to mine sales patterns from very large transaction datasets; the optimization loss uses **random negative samples** to overcome the computational bottleneck of large item counts. Experiments on synthetic data show the efficiency of drawing negatives based on the **actual assortment of available products**, beating literature approaches; validated on **millions of transactions from Fortenova Group** (a leading SE-Europe retailer), with interfaces to support category managers.
- **Key Innovations**: (1) product–price–store interaction embeddings for basket choice; (2) assortment-aware negative sampling that outperforms generic sampling; (3) million-scale industrial retail validation.
- **Venue**: ECML PKDD 2025 (LNCS 16021, pp. 125–142).

### 1.7 SimInter — Evidence-Grounded User Simulation for Conversational RecSys (2610.18308)
- **Title**: SimInter: Evidence-Grounded User Simulation with Interview-Based Profile Enrichment for Conversational Recommender Systems
- **Authors**: Erfan Shahabi, Amirhossein Roshandel, Mohammad Sadegh Sadeghi, Azadeh Shakery
- **Institution**: University of Tehran-aligned (*tentative* — Shakery)
- **Date**: Tue 13 Oct 2026 (cs.CL, cs.AI, cs.IR)
- **arXiv**: https://arxiv.org/abs/2610.18308
- **Abstract**: Conversational Recommender Systems need reliable **user simulators** for cost-effective evaluation, but LLM simulators typically condition on profiles from explicit ratings/demographics/static sources — capturing **surface preferences** while omitting implicit behavioral traits (decision-making style, aspect-level preferences, domain expertise). **SimInter** elicits these attributes via **synthetic interviews between two LLM agents**, grounded in the user's statistical profile and historical conversational evidence; an **audit agent** flags fabrication/stereotyping at the turn level before enrichment. On movie recommendation, simulating 300 ReDial users (matched subset of 100), SimInter significantly raises the diversity of expressed preference aspects (**filtered aspect entropy 1.619 vs 0.859**, paired d=0.96, Holm-p<0.001), persisting against two trained recommenders (KBRD, UniCRS) under two independent judges (+0.28 to +0.56 nats, all p<0.001). Human eval finds **94.3%** of enriched-attribute claims supported/partially supported and **95.2%** agreement with the auditor's binary filtering.
- **Key Innovations**: (1) interview-based profile enrichment for grounded user simulation; (2) turn-level fabrication/stereotyping auditor; (3) multi-judge + human validation of a conversational-rec evaluation pipeline.
- **Venue**: Preprint.

### 1.8 XViewRank — Overlap-Conditioned Fusion for LLM-Augmented Sparse Retrieval (2610.20122)
- **Title**: XViewRank: Overlap-Conditioned Score Fusion for LLM-Augmented Sparse Retrieval
- **Authors**: Xinxuan Lv, Minghan Li, Guodong Zhou
- **Institution**: Soochow University-aligned (*tentative* — Zhou)
- **Date**: Wed 14 Oct 2026 (cs.IR)
- **arXiv**: https://arxiv.org/abs/2610.20122
- **Abstract**: LLMs can reduce vocabulary mismatch in sparse retrieval by generating **alternative views of a query** (hypothesis view, step-back view), but once these views are searched independently their ranked lists may be complementary, redundant, or drift — making **fixed fusion suboptimal**. **XViewRank** is a lightweight **retrieval-side** method that *conditionally* fuses BM25 results from the original query plus the two views: for each pooled candidate it retains **three normalized BM25 scores + three query-level overlaps** between the retrieved result sets, and a **small nonlinear scorer** uses the overlaps as context that changes how view-specific scores are interpreted (without jointly encoding query/passage text). Under a matched-input protocol it improves nDCG@10 and MAP over **reciprocal rank fusion** on TREC DL 2019 & 2020 (statistically significant MAP gain on DL19); the clearest benefit occurs when view rankings have **low agreement**, while DL20 evidence is weaker.
- **Key Innovations**: (1) overlap-conditioned (context-varying) score fusion vs fixed RRF; (2) no joint query–passage encoding — compact retrieval-side scorer; (3) honest, statistically-scoped reporting of where the advantage holds.
- **Venue**: Preprint.

### 1.9 Revisiting Generative vs. Dense Retrieval — A Static Value Prior Reverses the Gap (2610.19065)
- **Title**: Revisiting Generative vs. Dense Retrieval: A Static Value Prior Reverses the Gap
- **Authors**: Renbo Tu, Yang Liu, Shuying Sun
- **Institution**: academic/industrial (*tentative*)
- **Date**: Tue 13 Oct 2026 (cs.IR, cs.AI, cs.LG)
- **arXiv**: https://arxiv.org/abs/2610.19065
- **Abstract**: **Generative retrieval (GR)** has emerged as a strong candidate generator for **sequential recommendation** as LMs and semantic item IDs improve, but it is **not a uniformly stronger replacement** of dense retrieval (DR) in online retail candidate generation. On two Amazon Toys datasets, GR leads on **best relevant item value** among users both methods cover, while DR leads on **exact-target recall** and relevant value across the ranked list. Deep analysis finds **popularity contributes most to GR's measured value lead**; adding the same **static item value prior** to DR in one reranking step **reverses this lead** while keeping recall above GR. On an industrial-scale internal e-commerce dataset with LLM-judged relevance, a **14B SID-LLM still underperforms a 47× smaller dense encoder**.
- **Key Innovations**: (1) controlled GR-vs-DR candidate-generation comparison for sequential rec; (2) identifies popularity as the driver of GR's apparent advantage; (3) a one-step static value prior flips the comparison — cautioning against generative-retrieval hype at industrial scale.
- **Venue**: Preprint.

### 1.10 TAGHN — Text-Attentive Graph Reranking for Subject Indexing (2610.20048)
- **Title**: Reading the Neighborhood: Text-Attentive Graph Reranking for Automated Subject Indexing
- **Authors**: Lakshmi Rajendram Bashyam, Ralf Krestel
- **Institution**: Hasso Plattner Institute / Univ. of Potsdam-aligned (*tentative* — Krestel)
- **Date**: Wed 14 Oct 2026 (cs.IR, cs.DL)
- **arXiv**: https://arxiv.org/abs/2610.20048
- **Abstract**: Subject indexing assigns controlled-vocabulary descriptors to bibliographic records — thousands of labels, few positives per label, a long tail. Existing extreme multi-label classifiers treat the vocabulary as a **flat list**, ignoring thesaurus relations. **TAGHN** is a **heterogeneous graph reranker** over a per-document subgraph of retrieved candidates augmented with the **thesaurus neighborhood**: candidate relevance is estimated jointly from document similarity *and* the degree to which the candidate's thesaurus neighborhood matches document content, with a **decomposed scoring head** combining interpretable graph features and retrieval signals. On **STW** (6,198 descriptors), TAGHN reaches **0.380 macro F1** vs 0.346 (fine-tuned cross-encoder) and 0.278 (fixed-vocabulary XMLC); qualitatively it resolves errors per-label scoring cannot (picking a narrower gold descriptor over a broader parent).
- **Key Innovations**: (1) thesaurus-neighborhood-aware graph reranking for XMLC-style indexing; (2) decomposed interpretable scoring head; (3) macro-F1 gain over cross-encoder and XMLC baselines.
- **Venue**: JCDL 2026.

### 1.11 Prompt or Policy? Physician Slate Presentation with LLM User Simulators (2610.18309)
- **Title**: Prompt or Policy? Optimizing Physician Slate Presentations with LLM User Simulators
- **Authors**: Andrei Niculae, Adrian Cosma, Emilian Radoi
- **Institution**: University Politehnica of Bucharest-aligned (*tentative* — Radoi/Cosma)
- **Date**: Tue 13 Oct 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2610.18309
- **Abstract**: Physician recommendation systems identify relevant doctors, but patients struggle to **compare profiles** to decide. Formulates **slate presentation optimization**: given a patient's case and a fixed ranked list of physicians, generate short case-specific summaries that make doctors easier to compare while staying grounded in their profiles. To optimize without real patient interactions, an **offline framework** uses **persona-conditioned LLMs** to simulate patient choices; personas are generated from case-extracted attributes, and presentations are evaluated for accuracy, relevance, naturalness, and simulated choice, with a **second unseen LLM judge** to detect simulator-specific overfitting. Compares prompt-level optimization (**GEPA**), parameter-level (**GRPO**), and their combination across two model sizes: GRPO substantially beats GEPA on satisfying constraints and its simulated-conversion gains persist under the unseen judge; **GEPA-initialized GRPO** trains faster and reaches the highest simulated conversion.
- **Key Innovations**: (1) slate-presentation optimization as a ranking-consumption layer; (2) persona-conditioned LLM user simulator with unseen-judge overfitting check; (3) prompt-level and parameter-level optimization shown complementary.
- **Venue**: Preprint.

---

## 2 Sequential Modeling, Attention & Memory Architecture

### 2.1 ReaDy — HLA Recurrent States for Speculative Drafting (2610.20503)
- **Title**: ReaDy: Recurrent States as Dynamic Context for Speculative Drafting in Hybrid Linear Attention Large Language Models
- **Authors**: Bohan Sun, Zunhai Su, Xialie Zhuang, Jianjin Li, Ngai Wong, Chuan-Wei Kuo
- **Institution**: HKU-aligned (*tentative* — Wong); StartLuxLabs (code repo)
- **Date**: Wed 14 Oct 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2610.20503
- **Abstract**: Speculative decoding drafts multiple tokens per step, but **feature-based drafters rely on target hidden features** whose contextual emphasis may not align with later draft positions. **Hybrid linear attention (HLA)** models maintain compact **recurrent states** accumulating historical associations — an efficient complementary context source. **ReaDy** is (to the authors' knowledge) the **first speculative decoder to leverage HLA recurrent states for position-specific context retrieval** during drafting: each draft position gets a learned query retrieving supplementary context directly from the target's committed recurrent states; a lightweight **state reader** integrates it via residual updates, with low-rank state reads and fused operators bounding overhead. Builds on DSpark's parallel backbone + sequential prediction head with a two-stage adaptation. Across seven benchmarks (math, code, dialogue), **3.16× average decoding speedup** over autoregressive with Qwen3.8-27B on a single B200; beats DSpark on every benchmark (**+7.97% throughput, +8.50% acceptance length** on average).
- **Key Innovations**: (1) recurrent-state-conditioned speculative drafting (first of its kind for HLA); (2) learned per-position state-reader with low-rank reads; (3) consistent gains over DSpark across seven benchmarks.
- **Venue**: Preprint.

### 2.2 Latent Compaction with Test-Time Training (2610.20582)
- **Title**: Latent Compaction with Test-Time Training
- **Authors**: Yingfa Chen, Xingyu Shen, Chaojun Xiao, Xu Han
- **Institution**: Tsinghua THUNLP-aligned (*tentative* — Han/Xiao)
- **Date**: Wed 14 Oct 2026 (cs.CL, cs.LG)
- **arXiv**: https://arxiv.org/abs/2610.20582
- **Abstract**: Long contexts enlarge KV caches; compressing them must preserve information for **unseen** questions. **Latent Compaction** learns a **compact document-specific cache through test-time training**: cache entries are initialized using **reconstruction importance, teacher attention, and key-space diversity**; training first fits attention outputs and log-normalizers to the full cache (reconstruction-selected entries held fixed), then jointly optimizes the whole cache via **end-to-end distillation** from the full-cache model. Model weights stay frozen and training uses only **generic document prompts — no downstream Q/A**. On RULER/LongBench/Phonebook Lookup it substantially beats budget-matched baselines: **96.7% accuracy at 32× compression** (vs 40.0% for KVZip+), transferring across model scales/families (Qwen3, MiniCPM5).
- **Key Innovations**: (1) treating the KV cache as a **trainable network** optimized by test-time training; (2) question-agnostic, weight-frozen compaction; (3) 32× compression with near-full accuracy on RULER.
- **Venue**: Preprint.

### 2.3 Titan-Llama — Retrofitting LLMs with External Neural Memory (2610.19210)
- **Title**: Titan-Llama: Retrofitting Pre-trained LLMs with External Neural Memory Modules
- **Authors**: Sarah Pan, Ali Behrouz
- **Institution**: Google-aligned (*tentative* — Behrouz)
- **Date**: Tue 13 Oct 2026 (cs.CL, cs.AI)
- **arXiv**: https://arxiv.org/abs/2610.19210
- **Abstract**: Transformers pre-train efficiently (parallel attention) but long-context inference needs growing KV caches; efficient recurrent alternatives limit token-wise parallelism during training. **Titan-Llama** is a **post-training method** that retrofits attention-based LMs with a **hierarchical memory architecture updated at test time**: a blockwise attention mask preserves full-fidelity attention over recent tokens while compressing history into recurrent **fixed-size neural memory modules (NMMs)**; pre-trained attention layers are replaced **without training a new LM from scratch**. On Llama-3.2-1B-Instruct it raises accuracy over segmented attention windows from **23.87%→40.51%** (QuALITY) and **14.50%→40.75%** (LongHealth); inference shows **>20% faster prefill**, **37% faster decode** at medium context, and **24% lower steady-state decode memory**.
- **Key Innovations**: (1) retrofit path (no from-scratch retraining) to add test-time-trained memory to existing transformers; (2) blockwise mask + fixed-size NMM compression of history; (3) prefill/decode speed and memory gains at medium context.
- **Venue**: Preprint.

### 2.4 Depth Memory — Unifying Depth Aggregation as Store/Retrieve (2610.18809)
- **Title**: Depth Memory
- **Authors**: David González-Martínez, Philipp Nazari, T. Konstantin Rusch, Shiwei Liu
- **Institution**: academic (*tentative* — Liu/Rusch)
- **Date**: Tue 13 Oct 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2610.18809
- **Abstract**: Residual connections propagate information by additively accumulating layer outputs; recent alternatives (Manifold-Constrained Hyper-Connections **mHC**, **AttnRes**) use more expressive depth aggregation. This work frames **mixing representations over depth as storing/retrieving information across layers** and introduces **Depth Memory (DM)**, a unified framework describing **PreLN transformer, mHC, and AttnRes** as streams carrying representations through the network (e.g., an explicit memory stream queried to enrich each layer's input and written back). Building on this view, **Linear Depth Memory (LDM)** formulates cross-depth retrieval as a regression solved by **recursive least squares**, propagating three streams: the residual stream, a **linear associative memory stream**, and an **inverse covariance stream**; a hardware-aware implementation reduces peak activation memory and traffic. LDM achieves the **lowest perplexity** among PreLN/mHC/AttnRes at 400M and 1.5B scales, with competitive zero-shot accuracy.
- **Key Innovations**: (1) a store/retrieve framing unifying PreLN/mHC/AttnRes; (2) recursive-least-squares depth retrieval (LDM) with three streams; (3) hardware-aware implementation + perplexity wins at two scales.
- **Venue**: Preprint.

### 2.5 Joint Subspace Sparse Attention (JSSA) for Long-Context Decoding (2610.19026)
- **Title**: Joint Subspace Sparse Attention for Efficient Long-Context Decoding
- **Authors**: Jiwon Song, Yoongon Kim, Jae-Joon Kim
- **Institution**: Seoul National University-aligned (*tentative* — Kim)
- **Date**: Tue 13 Oct 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2610.19026
- **Abstract**: Sparse attention cuts the KV-cache traffic dominating long-context decoding, but practical methods operate at coarse granularity. Token-level selection is finer yet faces two challenges: **low-dimensional scoring can lose query–key structure** for accurate ranking, and **gathering scattered selected tokens can offset latency gains**. **JSSA** learns a shared low-dimensional query–key subspace by minimizing **token-score preservation error**; it upper-bounds the non-convex objective with a **tractable marginal objective admitting a closed-form spectral solution** (direct refinement gives no measurable improvement). A **gather-free token-level indexed-attention kernel** supports distinct per-KV-head selections under standard GQA layout. Across GQA, hybrid sliding-window/global, and MLA models, JSSA stays close to full-KV accuracy while avoiding generation-length inflation; on a B200 it reaches up to **6.43× decoding throughput** of full-KV at 128K context and 96–99% of native DSA throughput at 700B scale.
- **Key Innovations**: (1) shared query–key subspace learned via a closed-form spectral bound; (2) gather-free per-KV-head indexed-attention kernel; (3) throughput parity with model-native sparse attention without training.
- **Venue**: Preprint.

---

## 3 LLM Efficiency, MoE & Inference

### 3.1 Spectral-MoE — Heterogeneous Per-Layer Expert Utilization (2610.19232)
- **Title**: Spectral-MoE: Heterogeneous Per-Layer Expert Utilization in Dense-to-MoE Conversion
- **Authors**: Zachary Broveak, Christian Kubicka, Thierry Tambe
- **Institution**: Stanford-aligned (*tentative* — Tambe)
- **Date**: Tue 13 Oct 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2610.19232
- **Abstract**: Dense-to-MoE conversion reduces inference arithmetic by partitioning pretrained FFN neurons into experts and selecting a subset per token. Leading **analytic** (fast, heuristic) and **learning** (slow, gradient-optimized) methods both **fix the same active expert count at every layer**. **Spectral-MoE** learns to allocate a **utilization budget heterogeneously across layers**: a **static** per-layer scalar (shared across tokens) and a **dynamic** per-token schedule. Both allocators beat uniform utilization on both analytic- and learning-based SOTA conversion. At 25% FFN utilization, dynamic allocation reduces WikiText-2 perplexity vs uniform by **1.04 / 2.96 / 2.71 points** on the learned base for Llama-2-7B / Llama-3-8B / Qwen2.5-7B (analytic base: **2.45 / 6.26 / 2.17**), and improves six-task mean accuracy by **1.5 / 4.2 / 3.6 pts** at 12.5 / 25 / 50% utilization on the learned base.
- **Key Innovations**: (1) per-layer (and per-token) expert-utilization allocation as a new optimization axis; (2) works on top of both analytic and learned conversion SOTA; (3) consistent perplexity/accuracy gains across three model families.
- **Venue**: Preprint.

### 3.2 PN-Mix — Pair-Norm Guided Key-Cache Quantization (2610.19605)
- **Title**: PN-Mix: Pair-Norm Guided Mixed-Precision Key Cache Quantization for Efficient Long-Output LLM Inference
- **Authors**: Gil Jae Song, Sungjoo Yoo
- **Institution**: Seoul National University-aligned (*tentative* — Yoo)
- **Date**: Wed 14 Oct 2026 (cs.LG, cs.CL)
- **arXiv**: https://arxiv.org/abs/2610.19605
- **Abstract**: Long-output inference is bottlenecked by KV-cache memory/bandwidth; low-bit (e.g. 2-bit) KV quantization severely degrades accuracy, and prior mixed-precision key-cache methods estimate channel saliency from **key statistics alone**. Through attention-logit perturbation analysis at the **RoPE channel-pair** level, this work shows quantization errors in channel pairs with **large query–key pair-norm products** dominate logit variation. **PN-Mix** assigns higher precision to those **salient channel pairs, identified once at prefill and reused throughout decoding**, for RoPE-based decoder-only LLMs. On reasoning, code-generation, and AIME benchmarks, PN-Mix at **2.26-bit average precision** matches or beats prior mixed-precision methods at 2.32–2.39 bits, and **degrades gracefully down to 1.5 bits** where baselines drop sharply below 2.25 bits.
- **Key Innovations**: (1) RoPE channel-pair query–key pair-norm as the saliency signal; (2) prefill-once, decode-reuse precision schedule; (3) better accuracy-per-bit and graceful low-bit degradation.
- **Venue**: EMNLP 2026.

### 3.3 NatScale — Contrast Calibration for Mixed-Precision MoE Quantization (2610.20353)
- **Title**: Beyond Expert Rankings: Contrast Calibration for Mixed-Precision MoE Quantization
- **Authors**: Renjie Xie, Juncheng Yang, Aoting Hu, Yan Liang, Mingxi Zhang, Zheheng Hong, Wei Xu, Yanzhi Chen
- **Institution**: industrial/academic (*tentative*)
- **Date**: Wed 14 Oct 2026 (cs.LG, stat.ML)
- **arXiv**: https://arxiv.org/abs/2610.20353
- **Abstract**: MoE models activate few experts per token but must store all weights; mixed-precision quantization stores sensitive experts at higher bit-widths, yet **expert rankings alone do not determine how strongly to weight their errors**. **NatScale** is a **contrast-calibrated allocation framework**: a model-specific **power transformation** calibrates gradient-based expert weights to an **information-theoretic contrast target** while preserving rankings; it jointly evaluates each expert's **gate/up/down** configs to estimate output error, then combines errors and calibrated weights with a weight-spectra/variance/precision-decay prior to select configs under a storage budget. Across three models it achieves the **lowest native-to-quantized KL divergence and highest top-token agreement in all nine settings** against five allocation baselines (lowest perplexity in seven).
- **Key Innovations**: (1) moves from expert *ranking* to magnitude-calibrated error weighting; (2) contrast-target power calibration preserving rankings; (3) objective-aware precision allocation with gate/up/down joint error.
- **Venue**: Preprint.

### 3.4 Energy Consumption of Discrete Diffusion vs Autoregressive LMs (2610.19855)
- **Title**: Energy Consumption Analysis of Discrete Diffusion and Autoregressive Language Models
- **Authors**: Boris Ruf, Marcin Detyniecki
- **Institution**: Sopra Steria / academic (*tentative*)
- **Date**: Wed 14 Oct 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2610.19855
- **Abstract**: As LLMs scale, **inference energy** becomes critical. Autoregressive (AR) models are the industry standard; **diffusion LMs (DLLMs)** parallelize token generation. This comparative energy benchmark pits diffusion models (**LLaDA-8B, Dream-7B**) against AR counterparts (**Llama-3.1-8B, Qwen-2.5-7B**), analyzing architecture, KV-cache optimization, and **Joules-per-token** efficiency. At longer sequences (200–600 tokens) diffusion models reach **2.5–2.7 J/token**, roughly **2× more efficient** than AR with KV-cache (**5.3–5.7 J/token**); KV-cache gives AR large (50–70%) energy reductions at longer sequences.
- **Key Innovations**: (1) head-to-head J/token energy benchmark of DLLMs vs AR; (2) quantifies the diffusion efficiency crossover at longer sequences; (3) couples architecture and KV-cache effects.
- **Venue**: GreenSys '26 (workshop proceedings, pp. 7–12).

---

## 4 Agents, Memory & Multi-Agent Systems

### 4.1 MemCode — Discrete Semantic Memory for Long-Term Agents (2610.19472)
- **Title**: MemCode: Discrete Semantic Representations for Long-Term Agent Memory
- **Authors**: Xin Li, Liang Hu, Duoqian Miao, Ming Peng, Qi Zhang
- **Institution**: Tongji University-aligned (*tentative* — Hu/Miao)
- **Date**: Wed 14 Oct 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2610.19472
- **Abstract**: Long-term memory is a bottleneck for LLM agents across sessions. Existing **write-then-retrieve** systems store context-dependent dialogue fragments and retrieve by **nearest-neighbor search in continuous embedding space**, yielding unstable access units and missing **logically related but lexically distant** evidence. **MemCode** couples **retrieval-oriented writing** with **discrete associative retrieval**: it rewrites dialogue into self-contained **atomic memory units (AMUs)**, maps AMUs into a learnable codebook via **isomorphic semantic quantization (ISQ)**, and uses **codebook co-occurrence topology** as a retrieval path complementary to vector search; it separates online atomic writes from **asynchronous offline consolidation**. On LongMemEval-S and LoCoMo (GPT-4o-mini, Qwen3-30B-A3B), MemCode achieves best overall accuracy while keeping per-dialogue memory construction within ~40–130 s — **3–21× faster than LightMem**, and an order of magnitude faster than A-MEM/MemoryOS.
- **Key Innovations**: (1) discrete codebook + ISQ for stable memory units; (2) codebook co-occurrence topology as associative retrieval beyond vector search; (3) large speed lead alongside accuracy gains.
- **Venue**: NeurIPS 2026 (accepted).

### 4.2 STRATA — Self-Maintaining Structured Experience Graphs (2610.19386)
- **Title**: STRATA: Self-Maintaining Structured Experience Graphs for Self-Evolving Language Agents
- **Authors**: Guanhua Zhu, Hanwen Li, Zhi Wei, Mengnan Du, Chenxi Yuan
- **Institution**: NJIT-aligned (*tentative* — Du)
- **Date**: Wed 14 Oct 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2610.19386
- **Abstract**: Self-evolving LLM agents accumulate experience (retrieve memories before acting, write lessons after), but most are **single-level**: trajectories, workflows, and reasoning items land in one **undifferentiated pool indexed by embedding similarity**, with no typed abstraction hierarchy; they never forget/deduplicate and are prone to **negative transfer** (a superficially similar but directionally opposite experience is recalled and copied verbatim, harming the agent). **STRATA** organizes experience into a **three-layer graph** of atomic skills/code snippets, task workflows, and generalized meta-frameworks connected by **typed edges**, maintained via five mechanisms sharing one similarity geometry: multi-dimensional similarity (by operation and target); a **typed reflector** crystallizing procedures from successes and pitfalls from failures; **community detection** inducing meta-frameworks; **pressure-triggered garbage collection with articulation-point protection**; and **contrast edges** flagging confusable, direction-opposite experiences. Across four interactive benchmarks (AppWorld, WebArena, ALFWorld, ScienceWorld), two frozen backbones, seven baselines, STRATA attains the **best average score** with the **lowest latency and fewest environment steps**, and 44% fewer injected memory lines; **contrast edges lift ScienceWorld from 78.7 to 96.7**, isolating negative transfer as a key prior failure mode.
- **Key Innovations**: (1) typed three-layer experience graph with contrast edges; (2) self-maintenance (reflector, community detection, protected GC); (3) names and repairs single-level negative transfer (78.7→96.7).
- **Venue**: Preprint.

### 4.3 MemDuet — Dual-Process Memory for Long-Context Reasoning (2610.19928)
- **Title**: MemDuet: Learning Dual-Process Memory for Long-Context Reasoning
- **Authors**: Jiangcheng Song, Haodong Jing, Yulin Mu, Lesong Tao, Jixin Wang, Jin Cui, Tianjing Ren, Runxuan Xie, Yongqiang Ma, Nanning Zheng
- **Institution**: Xi'an Jiaotong University-aligned (*tentative* — Zheng/Ma)
- **Date**: Wed 14 Oct 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2610.19928
- **Abstract**: Reasoning over very long documents via recurrent memory agents exacerbates the **performance–efficiency trade-off**. Inspired by Kahneman's fast/slow thinking, **MemDuet** coordinates a **small LM for fast, parallel evidence selection** from raw context chunks (**System 1**) with a **large LM for memory-update verification and memory updates in document order** (**System 2**). Trained in three stages: SFT of System 1 for selection, **GRPO** of System 2 for verification/rewriting, and **joint optimization** of both for long-context reasoning. On RULER-HQA, LongBench v2, and 2WikiMultiHopQA it gives a favorable accuracy–efficiency trade-off as context grows: averaged over settings, an end-to-end **9.74× speedup** and **73.91% output-token reduction** relative to RL-MemAgent.
- **Key Innovations**: (1) explicit System-1/System-2 dual-process memory for long context; (2) three-stage SFT→GRPO→joint training; (3) large efficiency gain at matched reasoning.
- **Venue**: Preprint.

### 4.4 Narrowing the Collaboration Gap — Calibrated Belief Communication (2610.19215)
- **Title**: Narrowing the Collaboration Gap, Probably
- **Authors**: Mirah Shi, Marcel Hussing, Ira Globus-Harris, Natalie Collina, Aaron Roth, Surbhi Goel
- **Institution**: University of Pennsylvania-aligned (*tentative* — Roth/Collina/Goel)
- **Date**: Tue 13 Oct 2026 (cs.LG, cs.AI, cs.MA)
- **arXiv**: https://arxiv.org/abs/2610.19215
- **Abstract**: LLMs are increasingly deployed as **teams holding different private information** about a shared task; how should they communicate to aggregate decision-relevant information? Communicating only **actions** can discard uncertainty (two agents may prefer the same action for different reasons). This work studies an alternative interface — agents communicate **calibrated beliefs over actions**. In a synthetic setting capturing multi-round reasoning under partial information, it shows **theoretically and empirically** that communicating **unbiased probabilities can be strictly more powerful** than communicating actions. In a collaborative maze-solving task with trained transformers and pretrained LLM agents, **probability communication outperforms action communication when the exchanged predictions preserve calibrated uncertainty**; when probabilities are **biased the benefit can disappear**. A **post-hoc conversational calibration intervention** consistently improves decision-making by correcting biases (toy transformers and pretrained LLMs in context).
- **Key Innovations**: (1) calibrated-belief communication as a superior multi-agent interface; (2) identifies calibration (not raw information volume) as the mechanism; (3) post-hoc conversational calibration intervention.
- **Venue**: Preprint.

---

## 5 Games, Auctions & Mechanism Design

### 5.1 Price of Anarchy of First-Price Auctions in Agentic Markets (2610.20587)
- **Title**: Price of Anarchy of First-Price Auctions in Agentic Markets
- **Authors**: Shubhendu Trivedi, Jacob Eisenstein, Alekh Agarwal, Ian Gemp, Michael Kaisers, Adam Fisch
- **Institution**: Google DeepMind-aligned (*tentative* — Eisenstein/Gemp/Fisch)
- **Date**: Wed 14 Oct 2026 (cs.GT, cs.AI, cs.LG)
- **arXiv**: https://arxiv.org/abs/2610.20587
- **Abstract**: An **agentic market** is a decentralized serving-time market where AI agents **bid to claim each user prompt**; an agent's bid is based on its expected value (reward for its response minus inference costs). **First-price auctions (FPAs)** are natural (simple, transparent, no central knowledge of private capabilities/costs) but **not truthful**, so the prompt may go to a bidder who does not value it most — welfare loss quantified by the **price-of-anarchy (PoA)**. The paper argues agentic markets likely have features **reducing PoA**: (1) a **competitive floor** (multiple bidders usually value a prompt above some baseline share of optimal welfare — e.g., because strong models are distilled into cheap equivalents), which can drive welfare loss **to zero** as the floor rises; (2) **near-independence** of values after conditioning on the prompt (most predictable variation determined by prompt difficulty), giving an efficiency guarantee approaching **1 − 1/e²** of optimal welfare — both much better than the general **1 − 1/e**. Validated empirically with strategic bidders on the **EmbedLLM** prompt-routing dataset.
- **Key Innovations**: (1) formalizes serving-time agentic prompt markets as FPAs; (2) competitive-floor and conditional near-independence both tighten the welfare bound beyond 1−1/e; (3) empirical validation via LLM-prompt-routing auctions.
- **Venue**: Preprint.

### 5.2 STAR — Strategy-Proof Topology-Aware Agent Routing (2610.19316)
- **Title**: Truthful and Expected-Payment-Optimal Model Routing in Graph-Based Agentic Workflows
- **Authors**: Jiayuan Liu, Mingyu Guo, Jiarui Gan, Vincent Conitzer
- **Institution**: CMU / Oxford-aligned (*tentative* — Conitzer, Gan)
- **Date**: Tue 13 Oct 2026 (cs.GT, cs.CL, cs.MA)
- **arXiv**: https://arxiv.org/abs/2610.19316
- **Abstract**: Assigning routine tasks to cheaper **LLM providers** cuts generation cost, but switching providers may require reprocessing accumulated context — keeping dependent tasks with the same provider can **reuse eligible context**, coupling routing decisions across tasks in a **graph workflow**. Providers may also privately know their real-time unit costs and **strategically misreport**. Formulates this routing as a **single-parameter procurement auction** and proposes **STAR** (Strategy-proof Topology-aware Agent Routing), which minimizes **virtual-cost-weighted graph workloads**; its allocation and payments (computed by integrating workload over possible cost reports) make **truthful reporting utility-maximizing** regardless of others' reports and cover each truthful provider's execution cost. With independent cost distributions and non-decreasing virtual costs, STAR also **minimizes the user's expected total payment**. Synthetic experiments separate the execution-cost benefit of **topology awareness** (grows with fan-out/payload) from the payment benefit of **virtual-cost optimization**, and quantify sensitivity to prior misspecification while strategy-proofness holds.
- **Key Innovations**: (1) graph-workflow model routing as a truthful procurement auction; (2) topology-aware + virtual-cost-weighted allocation; (3) strategy-proofness preserved under prior misspecification.
- **Venue**: Preprint.

### 5.3 Improved Combinatorial Auctions with and without Samples (2610.17517)
- **Title**: Improved Combinatorial Auctions with and without Samples
- **Authors**: Aviad Rubinstein, Sahil Singla
- **Institution**: Stanford / Georgia Tech-aligned (*tentative*)
- **Date**: Tue 13 Oct 2026 (cs.GT, cs.DS)
- **arXiv**: https://arxiv.org/abs/2610.17517
- **Abstract**: New mechanisms for combinatorial auctions in the **offline, secretary, and prophet-with-samples** models, maximizing social welfare with *m* items and *n* XOS buyers. In **prophet-with-samples** (adversarial arrival order, independent value distributions) it gives a universally truthful, polynomial-time **(2+ε)-approximation using O(log log m) samples** per distribution — **tight** even for a single item without incentive constraints (classic prophet inequality). vs the previous SOTA (Dütting–Kesselheim–Lucier–Reiffenhäuser–Singla, FOCS 2024) the running time is **exponentially faster** and sample complexity **doubly-exponentially lower**, resolving two explicit open problems. Using the same techniques it also improves **secretary and offline** versions (worst-case values, random/no order) from the long-standing O((log log m)²)-approximation to **O(log log m)**, answering Assadi–Kesselheim–Singla (SODA 2021).
- **Key Innovations**: (1) tight (2+ε) prophet-with-samples mechanism with O(log log m) samples and poly time; (2) exponential/doubly-exponential improvements over FOCS'24; (3) O(log log m) universally truthful mechanisms for secretary & offline.
- **Venue**: Preprint (theory).

### 5.4 SafeAdapt-Poker — Budgeted Adaptation under Opponent Shift (2610.20473)
- **Title**: SafeAdapt-Poker: Counterfactual Risk Calibration for Budgeted Adaptation under Opponent Shift
- **Authors**: Miaobo Hu, Shuhao Hu, Xiaobo Guo, Xin Wang, Bokun Wang, Rui Chen, Daren Zha, Jun Xiao
- **Institution**: CAS Institute of Information Engineering-aligned (*tentative* — Zha)
- **Date**: Wed 14 Oct 2026 (cs.AI, cs.GT, cs.LG)
- **arXiv**: https://arxiv.org/abs/2610.20473
- **Abstract**: Opponent histories can mislead after behavioral shifts. **SafeAdapt-Poker** formulates **budgeted adaptation under opponent shift** as a **dual-counterfactual sequential-control** problem using only pre-decision information: at each decision the controller asks (i) what **local downside** a deviation from the frozen anchor induces under matched legal continuations, and (ii) what **future adaptation value** is lost by consuming remaining deviation budget now. These are answered by a **monotone strategic-risk model** over deviation intensity and a **paired budget-state continuation model** pricing budget consumption; a **pathwise cumulative-KL ledger** bounds total anchor-relative deviation, and a finite family of frozen controllers is screened on **paired calibration sessions** before held-out interaction (with a finite-candidate perturbation bound on continuation-value error). On exact Leduc it attains **+0.0718 weak-pool gain** (worst-opponent delta −0.0126), raises delayed-opportunity capture from **0.6318 → 0.7841**, and reaches **+42.7 mbb/hand** in abstract-HUNL cross-play; retained public-history screen reports **0.5820 action accuracy / 0.9277 log loss** vs a public prior's 0.5039 / 0.9778.
- **Key Innovations**: (1) dual-counterfactual (local-risk + budget-value) decision control; (2) cumulative-KL deviation ledger bounding anchor drift; (3) strong Leduc/HUNL results under four opponent shifts.
- **Venue**: Preprint.

### 5.5 Degrees of Freedom in Multi-Agent Coordination (2610.17751)
- **Title**: Degrees of Freedom in Multi-Agent Coordination: Between Centralized and Decentralized Regimes
- **Authors**: Yiqing Peng, Hehai Lin, Zixuan Wang, Dongyi Zhang, Zhengjie Zhu, Yi Han, Yangyang Zheng, Hao Wang, Qian Li, Chengwei Qin
- **Institution**: HKUST(GZ)-aligned (*tentative* — Qin)
- **Date**: Tue 13 Oct 2026 (cs.MA, cs.AI, cs.LG)
- **arXiv**: https://arxiv.org/abs/2610.17751
- **Abstract**: LLM-based multi-agent systems are usually organized either **centralized** (explicit control, single-locus bottleneck) or **decentralized** (local autonomy, distributed decisions). **Degrees of Freedom (DoF)** is a **continuous configuration framework** quantifying the size of the decision space delegated downstream — controlling **delegated work granularity** and the **target probability that each task unit is assigned to branches**; its endpoints recover the two regimes. Across domains, DoF reveals a hierarchy of organizational effects: delegated granularity and within-regime routing give **structured but bounded** profile reallocations, while task domain and retained experience drive stronger centralized-vs-decentralized differences. The performance landscape is **task-dependent**; **in five of six evaluated settings an intermediate DoF configuration achieves higher mean accuracy than both endpoints**, arguing for exploring the coordination space between the regimes.
- **Key Innovations**: (1) a continuous DoF knob interpolating centralized↔decentralized MAS; (2) systematic sweep showing intermediate regimes often dominate; (3) task-dependent coordination-landscape characterization.
- **Venue**: Preprint.

---

## Key Trends Across This Window

1. **The "memory architecture" thread is the window's spine** — hybrid-linear-attention recurrent state as drafting context (ReaDy 2610.20503), test-time-trained latent KV compaction (2610.20582), external neural memory retrofits (Titan-Llama 2610.19210), depth-as-memory (Depth Memory 2610.18809), closed-form joint-subspace sparse attention (JSSA 2610.19026): the field is converging on **explicit, trainable, reusable state** over pure scaling of attention/cache.
2. **Recommendation methodology sharpens around evaluation and reward design** — popularity-bias sparse objectives that reshape *gradient support* (PR-entmax 2610.17823), responder-noise removal for LLM-recommender RL (ReMaRk 2610.17771), and a **negative result** showing generative retrieval's lead is popularity-driven and reversible (2610.19065): the day's rec layer is about *what is actually being measured/rewarded*.
3. **Mechanism design is the strongest theory cluster** — PoA of agentic **first-price** prompt auctions (2610.20587), truthful topology-aware **model routing** (2610.19316), tight **combinatorial auctions** with O(log log m) samples (2610.17517), geographic **concurrent block-proposing** games (2610.18812): auctions + routing + decentralization, directly adjacent to the wiki's ads/auction thread.
4. **Agent memory forks into discrete-structure vs dual-process** — MemCode's codebook topology (2610.19472), STRATA's typed experience graph with contrast edges (2610.19386), MemDuet's System-1/System-2 split (2610.19928): three distinct answers to the "single-level embedding pool" critique of write-then-retrieve memory.
5. **Efficiency work splits into quantization and energy accounting** — per-layer MoE utilization (Spectral-MoE 2610.19232), RoPE pair-norm key-cache precision (PN-Mix 2610.19605), contrast-calibrated MoE quantization (NatScale 2610.20353), and a rare **energy benchmark** showing diffusion LMs ~2× more efficient than AR at long sequences (2610.19855).
6. **Games layer thin but real** — the only fresh pure-game paper here is a **poker opponent-shift adaptation** system (SafeAdapt-Poker 2610.20473); the broader game/MARL/PCG marquees of this window were claimed by the sibling `game-rl-daily` (see dedup note).

## ADS / CTR Coherence Check

**One direct advertising-system paper** (AdCoEvo 2610.19454) and **one sponsored-search RL paper** (CASI 2610.20293, featured as a runner-up) — both **agentic/reinforcement** in flavor rather than classical pCTR feature-interaction modeling. The continuing absence of end-to-end CTR/pCTR architecture papers on the daily arXiv side (consistent with the September and October `conference-digest`/`arxiv-paper-check` lanes) is again the window's clearest structural gap; the ads-relevant *theory* layer lives in the mechanism-design cluster (§5.1–§5.2), and the ads-relevant *application* layer in AdCoEvo + CASI.

## Runner-Ups (shortlist, all grep-verified 0 hits in `wiki/`)

- **2610.20293** CASI — Credit Assignment via Set Intervention for Agentic Retrieval: Shapley-based within-set credit for LLM multi-retrieval, with a randomized **7-day production A/B test on 10% of traffic** yielding a **3.51% advertiser-value lift** in a five-action sponsored-search setting (cs.AI/cs.IR) — the day's strongest *industrial ads* result.
- **2610.17959** Virtual Head Attention — NeurIPS 2026 main; near-identity Q Premix + low-rank Postmix give a **GQA-2 architecture** with 2 KV heads, beating GQA/MLA in quality while cutting KV cache 2–4× and training/prefill FLOPs ~7.9% (cs.CL).
- **2610.19552** Test-Time Forecasting — links linear attention to (extended) dynamic mode decomposition; **recurrent depth as gradient-descent iterations** enables in-context forecasting of unseen ODEs/PDEs after one-step training (cs.LG).
- **2610.20588** Your Transformer Is Secretly Elastic — retraining-free elastification via a **differentiable functional-unit ranking relaxation**; smooth degradation to 60% sparsity across 27 vision/text encoders (0.8% accuracy drop pruning DINOv3 ViT-H+/16 to 50%) (cs.LG).
- **2610.19408** ForkGRPO — RL for **diffusion LMs**: samples continuations from high-entropy intermediate states, gives **segment-level credit**; best on 3/4 benchmarks, up to 27.8% fewer generated tokens, 2.49× training speedup (cs.CL).
- **2610.17948** HaloBlock — difficulty-aware **adaptive halo** mechanism (bidirectional cumulative entropy) for diffusion-LM block decoding; better quality + efficiency on LLaDA/Dream (cs.LG).
- **2610.18812** The Geography of (Concurrent) Block Proposing — proposer **location games** with first-price information auctions; concurrent proposers create an economic force toward **geographic decentralization** (cs.GT/econ.TH).
- **2610.18309** covered above in §1.11; **2610.19065**, **2610.20048** covered in §1.9–§1.10 (**listed here for index completeness only**).

## Cross-Reference Index (Sibling Coordination)

- **Same-window game sibling**: `game-rl-daily` (2026-10-15) claimed the **2026-10-11 → 2026-10-13** game block — IDs 2610.17391, 2610.18229, 2610.15932, 2610.18808, 2610.18560, 2610.16776, 2610.17310, 2610.18354, 2610.18424, 2610.17327, 2610.17456, 2610.17201, 2610.16166, 2610.18826, 2610.18637, 2610.16450, 2610.18834, 2610.16423, 2610.17409, 2610.16848. This report's 26 featured + 9 runner-up IDs were selected **after** diffing against that set (per-ID `rg` verified 0 hits); the two windows share only the 10-13 calendar day and **no ID**.
- **Prior-day digest lanes** (`conference-digest` 2026-10-14, `arxiv-paper-check` 2026-10-14) indexed through the **2026-10-10** announcement block, so the 10-13/10-14 block swept here is fresh ground for the arXiv-search lane.

(End of file)
