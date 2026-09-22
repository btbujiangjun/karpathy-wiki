---
title: "arXiv Paper Check — AI & CTR (September 22, 2026)"
type: synthesis
created: 2026-09-22
updated: 2026-09-22
sources: []
tags: [arxiv, daily-check, ai, ctr, pre-ranking, feed-recommendation, ab-testing, stratification, imbalanced-classification, tabular-learning, ai-search, retrieval, quantization, llm-as-judge, ranking-calibration, geo, reranking, rag, agent-infrastructure, search-data, alignment, political-bias, preference-alignment, daily-digest]
---

# arXiv Paper Check — AI & CTR (September 22, 2026)

**Tuesday note**: the live arXiv mailing is the **Tue 22 Sep 2026** batch (Mon 21 Sep submissions, IDs **2609.22087–2609.24554**), already extensively claimed by today's [[arxiv-daily]] (38 papers / 7 sections + 12 runner-ups). This issue is therefore a **second-pass sweep of the unclaimed remainder of the Tue-22 window** from the AI & CTR angle — restricted to papers *not* claimed by today's arxiv-daily, today's arxiv-ai-search (Mon-21 remainder), or any earlier sibling. All 13 featured arXiv IDs below were grep-verified absent (0 hits) from the entire `wiki/`.

**CTR status**: no genuinely new *direct-category* CTR/ads papers remain unclaimed — the window's flagship rec/ads entries (UNIQUE flat-quantized unified retrieval+ranking, MuSeR long-seq multi-interest, GradCIR graded-relevance multimodal CIR at Walmart, YouTube Music offline-deferred LLM rationales) were all featured in today's [[arxiv-daily]]. The CTR-relevant remainder here clusters around **pre-ranking / feed at industry scale (LinkedIn), A/B-test power via optimal stratification, rare-class ranking for imbalanced conversion data, tabular feature screening, and the AI-Search retrieval-quality pipeline**.

---

## ① Pre-Ranking, Tabular & Ranking-Side Signal (4)

### Connected Content Retriever: Dense Graph Edge Features Powering Pre-Ranking at LinkedIn
- **Authors**: Akhilesh Gupta, Sudarshan Srinivasa Ramanujam, Chirag Bhanuprasad Mehta, Reshma Asharaf Beena, Dhritiman Das, Birjodh Singh Tiwana, Bhargavkumar Kanubhai Patel, Mack Lee, Renyi Tang
- **arXiv**: [2609.22441](https://arxiv.org/abs/2609.22441) — cs.LG (LinkedIn AI)
- **Key contribution**: Pre-ranking in large-scale feed recommendation must compress hundreds of thousands of candidate items into a shortlist usable by deep rankers, under strict serving budgets on constrained hardware. LinkedIn's **Connected Content Retriever (CCR)** treats pre-ranking as a dense **graph-edge-feature** problem on the graph connecting a member to Candidate class of items, computing sum-pooled dense graph edge features over the recommended content candidates, then serving them through a GPU **sorted-search join** as a fast scan-to-rank primitive. This lets the pre-ranker retire the coarse max-pooled / cross-feature aggregation of prior lines and scale model capacity ~50× (fast dense models) vs the previous generation while keeping production latency in budget.
- **Why it matters**: One of the few concrete industry accounts of the CTR-side *pre-ranking* layer this window, and a checklist item for the modern pre-ranking stack — node/graph-typed pooling of candidate-side features + GPU scan-to-rank join. Companion to the wiki's feed-recommendation / industrial-CTR thread.

### Optimal Multi-way Decision Trees for Stratified Sampling in Online Controlled Experiments (OMST)
- **Authors**: Tomoka Takei, Shunnosuke Ikeda, Yuichi Takano
- **arXiv**: [2609.23308](https://arxiv.org/abs/2609.23308) — cs.LG, stat.CO
- **Key contribution**: Stratified sampling for A/B tests only pays off if the strata are built well. **OMST** casts stratification as a path-selection problem over a feature graph, and optimizes the strata with an exact variance-minimizing binary-optimization formulation under both continuous proportional allocation and Neyman-type optimal allocation; supervised optimal binning generates outcome-relevant candidate splits for numeric features, and reduction procedures prune redundant candidate paths/assignment constraints to keep the optimization tractable. Experiments on a real and a simulated dataset show comparable-or-better variance reduction than existing methods with shallow, interpretable trees.
- **Why it matters**: Adds an optimization-based, interpretable tool to online-experimentation power without extra sample — directly relevant to how CTR/product changes get validated at scale, matching the wiki's [[online-controlled-experiments]] / experimentation-methodology line.

### Density-Ratio Rescoring for Imbalanced Classification (DRR)
- **Authors**: Dongha Kim, Seunghwan Park
- **arXiv**: [2609.23926](https://arxiv.org/abs/2609.23926) — stat.ML, cs.LG
- **Key contribution**: For rare-class (deeply imbalanced) tasks — the statistical regime of CTR/conversion data — DRR augments a classifier trained at the original prior with a **survey-raking dual score**: raking reweights the majority sample to match minority feature moments within tolerance, the dual is standardized and fused at a fixed half weight, and prediction uses the fitted dual directly (no resampling, no refitting). Under exact population matching + log-linear tilt, the dual equals the log density ratio up to a constant; a class-separation analysis gives the signal/correlation conditions under which fusion helps. Across 24 tabular benchmarks, 30 trials × 5 learners, DRR at D=128 random features beats the standardized base on *every* dataset (+0.034 mean AP) and beats a shared-dual raking-and-relabeling resampler on 22/24 (+0.092 mean AP), plus all 8 one-vs-rest gene-expression tasks.
- **Why it matters**: A reusable, well-characterized rescoring primitive for improving rare-positive ranking on top of any prior-trained classifier — cheap applied to conversion/click modeling. Empirical counterpoint to resampling-heavy pipelines.

### PACE: Plug-and-Play Contextual Embedding for Feature Screening with Pretrained Tabular Foundation Models
- **Authors**: Qi Qin, Erbo Li, Ting Wei, Zizhou Huang, Zixuan Qin, Wu Wang, Yifan Sun
- **arXiv**: [2609.23574](https://arxiv.org/abs/2609.23574) — stat.ML, cs.LG (TALENT/Ant — Chinese tech affiliate, *tentative*)
- **Key contribution**: Feature screening on raw values misses nonlinear/distributional structure. **PACE** inserts a *frozen* tabular foundation model (TFM) column encoder in front of an existing feature-scoring rule, expanding each feature into a higher-dimensional contextual representation — a plug-and-play upstream primitive. On TALENT datasets, PACE-DC improves binary AUC by +0.077 and multiclass macro-AUC by +0.064 over raw-space screening, with median normalized RMSE +0.063 across ten learners; matched random-weight/random-feature controls show the gain comes from pretrained structure, not mere dimensional expansion, and PACE wins the performance–time trade-off vs task-fitted selectors and attribution methods.
- **Why it matters**: A reusable way to bring pretrained column geometry into classical tabular pipelines (feature screening, DCN/CTR-style setups) — another data point in the wiki's tabular-classical-vs-LLM thread that does *not* require retraining the FM.

---

## ② Retrieval: Contexts, Reliability & Quantization (4)

### From Ranked Documents to Reliable Contexts: An Answer-Oriented Context Construct Framework for AI Search
- **Authors**: Yunfei Zhong, Yinqiong Cai, Lixin Su, Haosheng Qian, Lixin Zou, Yixing Fan, Sheng Xu, Jiafeng Guo, Daiting Shi, Jingzhou He
- **arXiv**: [2609.23354](https://arxiv.org/abs/2609.23354) — cs.IR (CAS + Huawei — *tentative*)
- **Key contribution**: In AI Search, retrieved documents feed a generator, so the retrieval objective shifts from ranking by search satisfaction to **constructing reliable context for correct answers**. Proposes a three-stage framework: ① *Answer Support* — identify documents contributing information to answer generation; ② *Content Trustworthiness* — assess reliability for correctness from source/temporal/factual perspectives; ③ *Context Organization* — select, consolidate and structure retained info under a finite context budget for consistent generation. Includes an industrial workflow (prior + posterior optimization) and a two-level evaluation protocol (retrieval-side context *and* final answers); consistent improvements at both levels.
- **Why it matters**: A clean formulation of what this wiki's AI-search thread keeps hitting — retrieval success ≠ answer correctness; budgeted, trust-ranked context construction is the actual objective. Industrial instantiation signal.

### The Undetected Damage of Quantization on Retrieval and How to Fix It
- **Authors**: Luca Zhou, Alessandro Zirilli, Daniele Solombrino, Roberto Dessì, Emanuele Rodolà
- **arXiv**: [2609.24322](https://arxiv.org/abs/2609.24322) — cs.LG, cs.AI (Sapienza)
- **Key contribution**: A quantized model that *keeps its classification accuracy* still changes **14–46% of its top-1 retrieval results**, and aggregate ranking metrics (NDCG-10 etc.) reveal only part of that. The cause: the top-1 result only survives if the gap between the two highest scores exceeds twice the largest rounding error — classification losses push the correct class apart and seed that gap, but retrieval scores separate nothing top-1 from top-2. This gap is **label-free, measurable per input**, and predicts both which models break under quantization (pre-deployment) and which individual quantized answers still match full precision (runtime). Fixes: spend extra bit-width on the layers whose quantization moves the gap most (recovers ~¾ of an extra bit's benefit at half its cost), or route low-gap inputs to full precision.
- **Why it matters**: A crisp, actionable account of the retrieval-specific failure mode in [[quantization]] that classic accuracy-walks miss — most classification inputs survive quantization, but most retrieval queries don't. Directly useful for embedded/edge retrieval serving where quantized recommenders are the norm.

### Scoring With the Engine: Retrieval Exposure, Cross-Engine Divergence, and the Limits of Engine-Agnostic GEO Scores
- **Authors**: Benjamin Tannenbaum
- **arXiv**: [2609.22655](https://arxiv.org/abs/2609.22655) — cs.IR
- **Key contribution**: Questions whether generative-engine visibility can be approximated by deterministic, engine-free page scores — and separates the two stages such scores conflate: *exposure* to a live engine, and *citation selection* conditional on exposure. An observational audit on 6 June 2026 (ChatGPT, Copilot, Google, Perplexity; 15 fixed commercial prompts; 589 citations, 528 URLs, 356 domains) finds cross-engine citation overlap is essentially zero — mean pairwise Jaccard 0.0079, median 0, 84.9% of engine pairs share no URL; observed overlap is only **5.7% of a matched-size hypergeometric baseline** (0.1272); 96.4% of URLs appear in only one engine; a 5–6 June same-engine rerun shows 67.0% mean URL-set turnover. Conclusion: engine-free scores do not measure end-to-end visibility but can estimate *page fit* or *query–page quality* — the paper argues for reporting page fit, observed exposure, conditional selection, and final visibility as four distinct quantities.
- **Why it matters**: The sharpest evidence yet for ''engine-agnostic GEO'' limits — deterministic scores conflate fit/exposure/selection, and live-engine overlap is near zero. Complements the AI-search source-exposure audit (2609.24407) in today's [[arxiv-daily]]. Strong candidate for the wiki's AI-search/GEO measurement line.

### Per-Query Gating of LLM Rerankers for Multi-Hop Retrieval
- **Authors**: Andre Bacellar
- **arXiv**: [2609.22880](https://arxiv.org/abs/2609.22880) — cs.IR, cs.AI, cs.CL, cs.LG
- **Key contribution**: LLM rerankers on graph-augmented dense pipelines (HippoRAG2-style) cost ~$0.2–0.3/1k queries plus ~1s tail latency for mixed gains — improving final-hop top-K on 7/9 cells (up to +34.8 pp). Asks whether a learned **per-query gate** can skip the reranker where it won't help, using only pre-call features (27 score + lexical statistics of the two retrieval lists, plus a PCA of a small query embedding) with an executable fallback. Every choice (fallback, threshold) is made inside the training fold and applied once to held-out queries; harmful skips are reported. Across 9 cells on 2WikiMultiHopQA/MuSiQue/HotpotQA the gate skips **51% of calls at ~1.2 pp held-out LastHop@K cost** (four cells meet a pre-registered 1 pp rule, but harmful skips outnumber beneficial ones 190:136 in one counting); a budget-calibrated variant skips 42% while the realized harm (1.45 pp) exceeds the promised 1 pp — a quantified selection optimism. Transparency gold: the paper retracts an earlier "73% lossless" figure that rested on an oracle fallback and a wrong target.
- **Why it matters**: A model exercise in *cost-adaptive retrieval* with rigorous held-out protocol and failure reporting — how the industry will actually budget LLM reranker spend after the unicost/rerank-mania wave. Reinforces the wiki's AI-Search cost-vs-lift measurement theme.

---

## ③ AI-Search Infrastructure, Judges & Data Provenance (4)

### Semantics Delivery Network: Rethinking Web Retrieval Infrastructure for LLM Agents
- **Authors**: Peichun Hua, Yunming Xiao
- **arXiv**: [2609.22486](https://arxiv.org/abs/2609.22486) — cs.NI, cs.IR, cs.LG
- **Key contribution**: Today's web stack is built for human clients — search returns URL-ranked snippets, CDNs cache URL-addressed objects — while LLM agents consume short semantic passages ("chunks") selected for task utility, retrieve statefully across turns, and duplicate each other's search/ingest/processing. Proposes **Semantics Delivery Network (SemDN)**: an origin-authorized, hierarchical edge substrate that indexes, searches and smart-caches content at *chunk granularity*; serves agents on behalf of participating sites; amortizes acquisition/processing across agents; supports tenant-specific retrieval policies. Key open problem: unlike URL caching, semantic retrieval gives no explicit miss signal, so SemDN must estimate corpus incompleteness/staleness and trigger scoped refresh. Preliminary probes show a large gap between page content processed vs chunks consumed, substantial task-local reuse, and higher answer quality per context token from chunk delivery.
- **Why it matters**: Reframes the agentic-RAG performance problem as a *network-delivery abstraction* problem — chunk is the addressable unit, not URL. Reinforces the wiki's agent-infrastructure / web-as-attention-thrift thread; also a genuine new architectural concept (types: network operator entity → new concept page candidate).

### OSCAR: Order-aware Scoring and Calibration for AI Rankings
- **Authors**: You Liu, Yue Liu, Quanchao Lu, Nick Shipilov
- **arXiv**: [2609.24128](https://arxiv.org/abs/2609.24128) — stat.ML, cs.LG
- **Key contribution**: Judge-specific sensitivity is useful for aggregating pairwise LLM evals, but its estimates hinge on which systematic presentation effects are modeled. **OSCAR** is an order-aware framework adding judge-specific position (and length/family) terms to sensitivity-based ranking. In released judgments from 18 evaluators, the all-response A-minus-B score difference spans −63.11 to +98.31 pp; matching question/response/candidate/judge in the released table yields +24.22 (95% CI [22.90, 25.54]). A controlled calculation shows the stakes: with true sensitivity fixed at 1, omitting a position intercept of 4 collapses the population-optimal slope to 0.0771. Across four datasets, position gives the largest stand-alone predictive improvement; in dependent-binary simulations, adjusting both mean AND covariance reaches 94.4–95.4% coverage (either alone is insufficient); at N=10,000, OSCAR cuts mean neutral-target RMSE from 0.1158 (sensitivity-only) to **0.0237**.
- **Why it matters**: The judge-reliability arc (LLJ Cards, "Judging a Review by its Cover", "Agreement Overstates Evidence" in today's [[arxiv-daily]]) gets its most explicit causal handle yet — *position effects on LLM judges are real, large, and correctable with order-aware calibration*. Strong [[llm-as-judge]] evidence.

### You Can Tell Who's Asking: What the Web's Questions Are Made Of, and Where They Come From
- **Authors**: Calvin Zhou, Vincent McCloskey, Krishna Srinivasan
- **arXiv**: [2609.24106](https://arxiv.org/abs/2609.24106) — cs.CL (Google-affiliated, *tentative*)
- **Key contribution**: A 13.4B-question-occurrence diachronic audit (110 FineWeb snapshots, 2013–2025) of the assumption that scraped web questions proxy human intent. Three findings: ① *provenance is legible* — a logistic model separates genuine user questions from templated/manufactured ones at **AUC 0.725** using length + surrounding context (not question type), though only 0.554 vs commerce-FAQ writing; ② *frequency ≠ demand* — over 70% of the top-1,000 most frequent questions are boilerplate/templated, so occurrence counts measure publication, not asking; ③ *the genuine share of occurrences fell 79% over 12 years* (42–56% after controlling for crawl composition), with question length and context shrinking — the crawlable web's questions shifted from asking humans to being *manufactured for machines to read*.
- **Why it matters**: A quantifiable alarm for any QA training set, retrieval benchmark or content-strategy input scraped from the web (including this wiki's own corpus of ingested web sources): demand-side validity is decaying. Directly relevant to search-data / benchmark-data heritage.

---

## ④ Alignment & Preferences (2)

### Auditing Political Alignment in LLM Assistants: Engagement, Stance, and User Identity
- **Authors**: Joan C. Timoneda
- **arXiv**: [2609.23039](https://arxiv.org/abs/2609.23039) — cs.CL, cs.AI, cs.CY (Purdue; preregistered)
- **Key contribution**: Audits presume a static "average user", but assistant political behavior is a **speech regime** — a policy over whom to answer, what to say, and whether to engage at all, conditional on topic and inferred user identity, where engagement/stance/refusal each carry topic-varying costs. Derives a 5-regime typology from engagement × stance and tests six systems (OpenAI, Anthropic, xAI, Google, Mistral, DeepSeek) in a preregistered **7,500 multi-turn conversation** experiment that randomly assigns user political identity across 5 topics (abortion, Catalan independence, climate change, Nazism, pineapple-on-pizza control), with two cross-developer LLM judges validated against humans and refusal treated as an outcome (not missing). Results: every system accommodates the control topic (restraint is a policy); on abortion, GPT engages/mirrors every user while Gemma refuses everyone, Claude answers strongly conservative users ~35% and almost no one else, and Grok accommodates conservatives only; on settled topics (climate, Nazism) five systems hold firm for every user. Systems also infer the user's identity from cues and condition engagement on it.
- **Why it matters**: The most audited political-alignment study this window, with a sharp methodological point — average-user audits hide *conditional* speech regimes; engagement/non-response must be modeled as outcomes, and user identity is inferred by the systems. Human-judge-free two-LLM-judge design is itself relevant to the wiki judge-reliability thread.

### Are Human-Aligned Models Models of Humans? A Turing-Test Gap in Preference Alignment
- **Authors**: Suqin Yuan, Runqi Lin, Muyang Li, Guanzhe Hong, Jindong Gu, Lei Feng, Chris Russell, Tongliang Liu
- **arXiv**: [2609.23640](https://arxiv.org/abs/2609.23640) — cs.AI
- **Key contribution**: Preference alignment is described as "aligning models with humans", but the responses people *prefer* from an AI need not be the responses they themselves would *give*. Distinguishes alignment-with-preferences from alignment-with-behavior: preference alignment preserves the human response distribution only under a restrictive condition, and no real-human-preference dataset consistently satisfies it. Empirically, the loss of human-response likelihood grows with preference-weighting strength (in *either* direction) and the gap also appears under standard DPO — so human-likeness is an explicit, strainable dimension of alignment, not an automatic by-product.
- **Why it matters**: A conceptual decoupling this wiki's alignment thread keeps needing — preferability and humanness are different objectives; RLHF/DPO can actively de-humanize response distributions. Sets up the missing third axis (behavior) in preference-based alignment evals.

---

## Cross-Cutting Themes

1. **Pre-ranking & industrial CTR get concrete again**: LinkedIn's CCR (graph-edge-featured pre-ranker served by GPU sorted-search join) is this week's flagship production-CTR artifact, after three+ windows of drought — and it's a *pipeline/format* contribution (dense graph edge features + scan-to-rank), not a new loss.
2. **Retrieval quality becomes a budgeted, gated resource**: Per-Query Gating (skip 51% of LLM-rerank calls at ~1 pp), gap-based quantized-retrieval trust (spend precision only where needed), and SemDN (chunk-level delivery + estimated miss signals) all treat retrieval quality as something to *allocate* rather than maximize — the industry's cost curve finally hitting the [[ai-search]] pipeline.
3. **AI-Search evaluation splits into fit/exposure/selection**: Scoring-With-the-Engine's four-quantity decomposition (fit, exposure, selection, visibility) is the cleanest measurement proposal this window, echoing the answer-oriented context framework (2609.23354) — retrieval-side metrics alone are declared insufficient at both audit and construction levels.
4. **Classical tabular keeps its seat**: DRR and PACE both add reusable, well-characterized primitives *to* the classical stack (rescoring duals, frozen-TFM column embeddings) rather than replacing it — matching the wiki's tabular-classical-vs-LLM position.
5. **Alignment audits must condition on the user**: The political speech-regime study (7,500 conversations, identity-randomized) shows assistant stance is a *conditional policy over inferred identity*, not a single answer; refusal-as-outcome is the methodological crux. Pairs with the Turing-test gap (preference ≠ behavior) to widen what "alignment eval" should measure.
6. **Web-corpus demand validity decays**: 79% decline in genuine-question share over 12 years — any question-derived training/eval signal from the crawlable web inherits manufactured-for-machines noise. A standing caveat for QA/retrieval benchmark heritage.

---

## Method Note

Tuesday fresh mailing (Mon Sep 21 submissions, Tue Sep 22 2026; IDs **2609.22087–2609.24554**). Pool: arXiv API tail sweep (5 target categories cs.AI / cs.LG / cs.CL / cs.CV / cs.IR with stat.ML cross-listings folded in) → **684 unique in-window entries** (published-date spread, overwhelmingly 09-18–09-21: 68/190/201/209 plus a handful of strays). Sibling dedup: today's [[arxiv-daily]] (Tue-22 window; 55 claimed IDs incl. 12 runner-ups) and [[arxiv-ai-search]] (Mon-21 remainder, deliberately disjoint by construction) removed → **632 unclaimed IDs**, then keyword-screened for CTR/recommendation/tabular/retrieval/AI-search/ranking-signal/relevance → 13 featured + runner-ups below. Every featured ID grep-verified **0 hits in `wiki/`**. Affiliations marked *(tentative)* where inferred from author/affiliation text rather than confirmed metadata. Window's flagship rec/CTR/LLM entries were claimed by today's arxiv-daily — this issue mines the remainder.

**Runner-ups** (0-hit verified, not featured): 2609.22601 Fairly Compensated Distributed IR (purchase-before-reveal partial-info retrieval marketplaces, cryptographic feasibility); 2609.22770 Parameterized Dense-Sparse Fusion for Hybrid Retrieval (rank-score mixing on BEIR SciFact via Qdrant); 2609.22819 Counterfactual Tool Ranking under Utility/Cost/Privilege Constraints; 2609.24441 MUSE dependency-aware adaptation of a frozen vision backbone for multivariate TSF; 2609.24370 Prescriptive SVD-Inspired Attention; 2609.23780 Falling Trees interpretable risk-prioritization model class.

**Next fresh window**: Wed Sep 23 2026 (Tue 22 Sep submissions).