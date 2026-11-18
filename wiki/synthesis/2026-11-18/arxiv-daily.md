---
title: "arXiv Daily — AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games (2026-11-18)"
type: synthesis
created: 2026-11-18
updated: 2026-11-18
sources: [arxiv.org]
tags: [arxiv, daily, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, retrieval, generative-recommendation, semantic-ids, agent-memory, weight-space-memory, test-time-adaptation, agentic-rl, llm-judges, cot-theory, kv-cache, speculative-decoding, quantization, moe-serving, game-theory, multi-agent-rl, cross-game-generalization, llm-agents]
---

# arXiv Daily Report (2026-11-18)

> **Query time**: 2026-11-18. The newest arXiv indexing blocks visible are **Mon, 16 Nov** and **Tue, 17 Nov 2026**; the papers below carry `submittedDate` **2026-11-14 → 2026-11-17** (a few 11-14/15 papers are backfilled because they were not in prior editions). This report is strictly newer than the 2026-11-17 edition, which covered the 2026-11-11…11-13 batch.
>
> **Method**: arXiv Export API queries over `cs.IR`, `cs.LG`, `cs.CL`, `cs.AI`, `cs.GT`, `cs.MA` (200 newest entries each, sorted by `submittedDate`) — 1,061 unique papers after dedup — title/abstract screening for recommendation, advertising/CTR, sequential modeling, LLM agents/memory/reasoning, serving efficiency, and games. Abstracts are condensed from API metadata; affiliations were recovered from the rendered paper HTML author blocks. All numbers are **author-reported** and not independently reproduced.
>
> **Freshness / dedup**: all 24 IDs below were checked against every existing `wiki/synthesis/**` report and are absent from prior editions.

## Summary

- **Generative recommendation gets a training-signal makeover.** GainReason scores individual reasoning sentences by their effect on target Semantic-ID likelihood (Predictive Gain); a multiple-choice auxiliary task injects the relative positive/negative signal that generative retrieval otherwise lacks (+4.9%–79% NDCG@10 on TIGER); CARE builds retrieval-*aligned* Semantic IDs instead of document-only ones. The shared theme: the tokenizer/objective, not just the architecture, bounds what generative recsys can recall.
- **Industrial retrieval papers lead with deployment numbers.** UniGraph (Ant Group) reports 27.6%–52.3% higher QPS at Recall@100 ≥ 0.95; IntentFlow (Xiaohongshu) reports +28.17% Top-4 CTR in a user-level A/B test over a ~10-billion-item index at P50 1.07 s; CARE is deployed in an industrial video-search retrieval stage.
- **CTR proper is thin but present.** No pure click-model paper in this window; the closest industrial evidence is IntentFlow's click-through gains, BRAVE's cost-aware reflection budget for recommendation agents, and the look-ahead-free trading-agent benchmarks in Section D, which quantify how little "signal" agent decisions actually add.
- **Agent memory splits into two camps — and they complement each other.** CLAM compiles session activations into a low-rank adapter with a recurrent hypernetwork (zero gradient steps, zero LLM calls) while keeping an episodic buffer; on the hardest cases the parametric channel still adds 4–5 points *with an oracle buffer*. MemDoctor and StaleBench/LEDGER-style work push the other direction: attribute and repair failures across Write/Update/Retrieve/Answer stages.
- **Test-time adaptation has a clear winner: in-context experience.** A controlled 14-mechanism study finds ICL raises mean success 28.8% → 49.4%, and adding GRPO reaches 51.6%, while self-distillation is mixed — ICL reuses environment structure but makes agents skip verification, which RL restores.
- **Efficiency work co-designs algorithms with hardware formats and schedulers.** MiSTiQ pairs trellis-coded KV storage with microscaling (MX) compute at ~1.25 bits/element; a draft-cache study shows key/value bit allocation depends on quantizer layout; Stint makes preemption "productive" (p99 TPOT −50.7%) and CECAR routes MoE experts by predicted reuse distance to hit 12.5 tok/s on a 16 GB consumer GPU.
- **Games/sequential decision span cooperation, markets, and generalization.** LLM agents' apologies and verbal cooperation frequently diverge from later actions; two look-ahead-free trading studies find no significant alpha (median 78% of returns are factor exposure, and the only "edge" is memorized pre-cutoff knowledge); MARL work formalizes exogenous regime shifts (ED-POMDP) and cross-game VLM control via conflict-aware multi-teacher distillation.

## Methodology and scope

- **Sweep**: 200 newest entries from each of `cs.IR`, `cs.LG`, `cs.CL`, `cs.AI`, `cs.GT`, `cs.MA` via `https://export.arxiv.org/api/query`, sorted by submission date; 1,061 unique papers after ID dedup.
- **Selection**: 24 papers balanced across recommendation/retrieval/CTR (6), LLM agents/memory/training/reasoning (7), serving/efficiency (5), and games/game theory/MARL (6). Title/abstract screening only; no full-text quality assessment.
- **Affiliations**: extracted from arXiv HTML author blocks (`ltx_author_notes` / title-page footnotes). Where an author block lists no institution (Nos. 20, 21), this is stated explicitly rather than guessed.
- **Caveats**: offline/online gains are not normalized across papers; single-company A/B results are self-reported. Paper No. 2's arXiv abstract is an ethics/broader-impact statement rather than a method/results summary, so its entry is deliberately conservative.

---

## A. Advertising, CTR, Ranking and Recommendation

### 1. GainReason: Learning to Reason with Predictive Gains for Generative Recommendation
- **arXiv**: [2611.21441](https://arxiv.org/abs/2611.21441)
- **Date**: 2026-11-16
- **Authors**: Zhuoyang Li, Teng Shi, Jiakai Tang, Weijie Yu, Guofu Xie, Xiao Zhang, Lei Kou, Yang Yu, Lei Shen, Xin Chen, Bing Wang, Xiaoyi Zeng, Jun Xu
- **Institution/Company**: Renmin University of China (Gaoling School of AI); University of International Business and Economics; Alibaba International Digital Commercial Group
- **Categories**: cs.AI
- **Abstract**: Reasoning-enhanced generative recommendation uses LLM reasoning for next-item prediction, but typical methods optimize with GRPO and rule-based rewards tied only to final recommendation performance. The authors identify two limits: individual reasoning steps' predictive contributions are not reflected in the optimization signal, and trajectories within a group often receive indistinguishable rewards. **Predictive Gain (PG)** measures the change in target Semantic-ID (SID) log-likelihood induced by each individual reasoning sentence, yielding contribution-aware, discriminative rewards; the paper theoretically aligns expected PG with the recommendation ranking objective. **PGRO** optimizes reasoning with sentence-level rewards, supported by a custom causal-attention mechanism for efficient PG computation, and an auxiliary **PGRU** task adaptively strengthens reasoning-conditioned prediction. Experiments on three public benchmarks report consistent gains over competitive baselines.
- **Key innovations**:
  - **Sentence-level Predictive Gain** reward from target-SID log-likelihood change — contribution-aware reasoning credit.
  - Theoretical alignment of expected PG with the recommendation ranking objective.
  - Custom causal attention for efficient PG computation plus a complementary PGRU task.

### 2. BRAVE: Reflection Is Not Always Worth It — Budgeted Reflection Allocation for Recommendation Agents
- **arXiv**: [2611.19847](https://arxiv.org/abs/2611.19847)
- **Date**: 2026-11-15
- **Authors**: Jinfeng Xu, Zheyu Chen, Ziyue Peng, Jianheng Tang, Zheng Lin, Wenhao Yuan, Jian Chen, Shujie Li, Victor Leung
- **Institution/Company**: University of British Columbia; Hong Kong Polytechnic University; HKUST; Peking University; University of Luxembourg; University of Hong Kong
- **Categories**: cs.IR
- **Abstract**: The work reduces unnecessary LLM reflection in recommendation agents while preserving full-catalog ranking and inference reranking. BRAVE changes only **how training-time reflection is allocated**, so it requires no new user data and no extra LLM exposure beyond the base agent protocol. The arXiv abstract is primarily a broader-impact/ethics statement: the main risk is that a poorly calibrated allocator may give less reflection to users with sparse, niche, or under-represented preferences, weakening personalization or affecting item exposure. Mitigations include deployment-time auditing, conservative allocation, task-side (not sensitive-attribute) ranking evidence, and a small fairness/random coverage budget; privacy is managed by minimizing user text sent to the LLM controller and anonymizing identifiers. (Accepted at WSDM 2027.)
- **Key innovations**:
  - Frames reflection as a **cost-aware budget allocation layer** rather than an always-on capability.
  - Leaves full-catalog ranking and inference reranking intact, limiting behavioral side effects.
  - Explicit subgroup/equity auditing protocol (history length, item popularity, cohorts) for deployment.
- **Note**: The public abstract does not report a method equation or head-line metric; treat the above as scope, not a validated result.

### 3. Keep It Simple! A Multiple-Choice Task Can Benefit Generative Recommendation
- **arXiv**: [2611.19320](https://arxiv.org/abs/2611.19320)
- **Date**: 2026-11-14
- **Authors**: Wei-Hsiang Huang, Jyun-Yu Jiang, Pu-Jen Cheng
- **Institution/Company**: National Taiwan University; Coupang
- **Categories**: cs.IR
- **Abstract**: Generative retrieval for sequential recommendation usually autoregressively generates item Semantic IDs and relies on semantic alignment, architectural complexity, and heavy tuning. The paper argues the standard learning framework has a foundational gap: models directly predict target items without explicitly learning negative compositions or relative ranking, unlike Bayesian Personalized Ranking (BPR). A **simple multiple-choice auxiliary task** addresses this; **Task Identifiers** and **Candidate Constructions** synthesize its training data with minimal adaptation. Theoretical analysis from information theory and compositional generalization explains the benefit. On four public benchmarks the approach improves the conventional generative recommender TIGER by **4.9% to 79% in NDCG@10**.
- **Key innovations**:
  - Adds BPR-style **relative positive/negative discrimination** to generative retrieval via a multiple-choice auxiliary objective.
  - Minimal-adaptation data synthesis (Task Identifiers + Candidate Constructions) — no architecture change.
  - Information-theoretic and compositional-generalization justification for why the auxiliary task helps.

### 4. UniGraph: A Unified Graph-based Index for Dynamic Hybrid Dense-Sparse Vector Retrieval
- **arXiv**: [2611.20758](https://arxiv.org/abs/2611.20758)
- **Date**: 2026-11-16
- **Authors**: Keyu Chen, Xiaoyao Zhong, Jiabao Jin, Peng Cheng, Wangze Ni, Jingkuan Song, Heng Tao Shen
- **Institution/Company**: Tongji University; Zhejiang University (deployed at Ant Group; under ICDE 2027 review)
- **Categories**: cs.IR, cs.DB
- **Abstract**: Hybrid dense-sparse retrieval ranks by a query-dependent weighted sum of dense and sparse distances, but systems typically search separate indexes and rerank the union — two passes, with premature candidate loss for items that only rank well after the signals are combined. A single graph built at one hybrid weight cannot serve varying query weights because the neighborhood structure changes. **UniGraph** merges neighbor sets computed at multiple hybrid weights into one bounded-degree graph, supporting query-specific weights without index rebuilding. An adaptive weight-guided search switches between sparse- and dense-guided entry points, and a dense-first pruning strategy avoids unnecessary exact sparse-distance computations. At Recall@100 ≥ 0.95 it delivers **27.6%–52.3% higher QPS** than the fastest per-dataset baseline in the mixed-weight setting; deployed at scale in Ant Group's production environment.
- **Key innovations**:
  - **Single bounded-degree graph** encoding neighborhoods across multiple hybrid weights — no rebuild per query weight.
  - Adaptive sparse/dense entry-point selection and dense-first hybrid-distance pruning.
  - Production-scale deployment for query-dependent hybrid retrieval.

### 5. IntentFlow: An Intent-Driven Real-Time Multimodal Search System with Image-Text Queries at Xiaohongshu
- **arXiv**: [2611.20448](https://arxiv.org/abs/2611.20448)
- **Date**: 2026-11-16
- **Authors**: Dongjia Zhao, Yuchen Ma, Chunsheng Shi, Ziqiu Gui, Chao Yuan, Jianing Zhu, Zhaoxing Zhang, Yahui Liu, Daoxin Zhang, Yi Wu, Yao Hu, Cheng Chen
- **Institution/Company**: Xiaohongshu
- **Categories**: cs.IR
- **Abstract**: For image-text queries in UGC communities, relevance depends on retrieval intent, not visual/topical similarity — and relevant notes may be absent from the initial candidate set, so reranking alone cannot fix it. IntentFlow uses a **hierarchical intent taxonomy** and intent-specific relevance criteria to align data construction, representation learning, and reranking over an index on the order of **ten billion entries**. An offline agentic data workflow acquires and verifies supervision; the embedding model combines intent-aware contrastive learning, graded ranking, and distribution distillation; a compact reranker scores query-candidate evidence conditioned on predicted intents. In a user-level A/B test it beats the production visual-search-then-rerank system by **+28.17% Top-4 query CTR, +18.96% query CTR, and +12.56% average time spent**, at **P50 end-to-end latency 1.07 s**.
- **Key innovations**:
  - **Explicit hierarchical intent modeling** spanning candidate retrieval *and* reranking under one relevance criterion.
  - Agentic offline verification loop for training-data construction at web scale.
  - Industrial-scale evidence of click-through/time-spent gains with sub-second latency.

### 6. CARE: Contrastive-Anchored Residual Encoding with Listwise Reconstruction for Retrieval-Oriented Semantic IDs
- **arXiv**: [2611.20721](https://arxiv.org/abs/2611.20721)
- **Date**: 2026-11-16
- **Authors**: Yuan Xu, Dawei Chen, Xiaoguang Lin, Xin Chen, Yulong Ou, Haijun Wu
- **Institution/Company**: Tencent
- **Categories**: cs.IR
- **Abstract**: In generative retrieval the Semantic-ID (SID) tokenizer bounds recall, yet common tokenizers (residual k-means, RQ-VAE, finite scalar quantization) optimize document-embedding criteria without checking whether a query can still find relevant documents after quantization. **CARE-SID** quantizes in a retrieval-aligned space: a zero-initialized residual alignment network is trained with a query-document contrastive loss, an anchor loss and a reconstruction target fixed to the original embedding prevent drift/collapse, and reference-vector rating residual quantization assigns codes. **CARE-LR** additionally distills, per training query, the similarity distribution induced by the original embeddings over a candidate list into the SID reconstructions. Both keep a document-only encoding interface. SIDs are judged *without training a generator* via row-budget recall in bucketing and reconstruction views; on industrial video-search data both beat residual k-means, with CARE-LR improving further. Contrastive alignment helps most when the base embedding was not trained on search data, and the embedding affects SID recall far more than the quantizer.
- **Key innovations**:
  - **Retrieval-aligned SID tokenization** via contrastive residual alignment with anti-drift anchors.
  - **Listwise similarity distillation** into reconstructions (CARE-LR) for ranking-faithful codes.
  - Generator-free SID evaluation protocol; deployed in an industrial video-search retrieval stage.

---

## B. LLM Agents, Memory, Training and Reasoning

### 7. GainCtrl: Predicting Remaining Gains for Efficient LLM Agent Execution
- **arXiv**: [2611.20736](https://arxiv.org/abs/2611.20736)
- **Date**: 2026-11-16
- **Authors**: Kangwen Zhao, Jianfeng Cai, Ruopei Sun, Mingxiao Feng, Peng Zhang, Wengang Zhou, Houqiang Li
- **Institution/Company**: University of Science and Technology of China; Ant Digital Technologies (Ant Group)
- **Categories**: cs.AI
- **Abstract**: Repeated attempts improve tool-using agents, but continued execution costs tokens even when the best result is unlikely to improve — raising the question of when to stop while preserving task-level Best-of-N quality. GainCtrl uses a lightweight **CPU predictor** over interaction histories to estimate expected positive gains over retained scores, then makes stopping decisions with calibrated thresholds that limit loss in mean Best-of-N quality. Trajectory replay across three environments and three LLM actors shows that interpolated quality–cost frontiers generally use fewer tokens than baselines at matched target quality; fixed policies also approach full-execution quality with much lower token use. The predictor runs at millisecond latency on one CPU thread and needs no access to LLM internals.
- **Key innovations**:
  - **Gain-based stopping controller** that monitors expected improvement rather than fixed attempt counts.
  - Calibrated thresholds giving an explicit quality–cost trade-off on Best-of-N metrics.
  - Black-box, millisecond-latency CPU predictor usable without model internals.

### 8. CLAM: Instant Weight-Space Consolidation for Long-Term Memory in LLMs
- **arXiv**: [2611.20759](https://arxiv.org/abs/2611.20759)
- **Date**: 2026-11-16
- **Authors**: Manan Suri, Dinesh Manocha
- **Institution/Company**: University of Maryland, College Park
- **Categories**: cs.CL
- **Abstract**: Text-extraction agent memories never change the model's weights; fine-tuning does, but needs serving-time backpropagation and degrades on long histories. **CLAM (Carried Latent Adapter Memory)** combines both: a **recurrent hypernetwork** compiles a stream of session activations into a low-rank adapter in a **single forward pass — no gradient steps and no LM generation calls** — while an episodic buffer supplies verbatim detail at inference. A gated latent state carries knowledge across sessions in fixed size. On LoCoMo and LongMemEval-S across three open 2–7B models, CLAM leads agentic baselines by 1–45 points and gradient-based parametric methods by 10–45 points, with 3–151× less wall-clock time than extraction systems to build memory. The channels are complementary: the adapter adds 12–15 accuracy points when the buffer misses gold evidence, and still 4–5 points with an oracle buffer.
- **Key innovations**:
  - **Gradient-free parametric memory**: recurrent hypernetwork compiles activations into a low-rank adapter in one pass.
  - Fixed-size gated latent state so parametric memory accumulates without growing.
  - Demonstrated complementarity of parametric and episodic memory, including under an oracle buffer.

### 9. Where Should LLM Agents Adapt at Test Time? In Context, in Weights, or Both?
- **arXiv**: [2611.19700](https://arxiv.org/abs/2611.19700)
- **Date**: 2026-11-15
- **Authors**: Parsa Mirtaheri, Mohammadreza Armandpour, Keivan Alizadeh, Iman Mirzadeh, Parshin Shojaee, Aryo Lotfi, David Harrison, Mehrdad Farajtabar
- **Institution/Company**: UC San Diego; Apple (some authors' work done at Apple)
- **Categories**: cs.LG, cs.AI, cs.CL
- **Abstract**: The paper compares test-time adaptation channels — in-context learning (ICL), GRPO with verifiable rewards, and self-distillation (SDPO) — alone and combined, under a shared online protocol so agents learn only from their own attempts and environment feedback. It evaluates **14 adaptation mechanisms plus a stateless baseline** with Qwen3.5-9B on **109 tasks from four environments** (SWE-bench Verified, AppWorld, ScienceWorld, BIRD-Critic-SQLite), five task orders each. ICL gives the largest standalone gain, lifting mean success from **28.8% to 49.4%**; adding GRPO reaches **51.6%**, while SDPO has mixed effects. Traces show ICL reduces lookups and shortens attempts (environment structure reuse) but also makes agents skip inspection/verification; adding GRPO restores those behaviors while preserving fewer lookups.
- **Key innovations**:
  - Controlled like-for-like comparison of **context vs weight adaptation** with a matched online protocol.
  - Large sweep (14 mechanisms × 4 environments × 5 orders) with pre-adaptation evaluation per task.
  - Mechanistic trace explanation: ICL saves lookups but erodes verification; RL repairs it.

### 10. ToolGraph as a Q-Function for Test-Time Scaling of Tool-Use Agents
- **arXiv**: [2611.20569](https://arxiv.org/abs/2611.20569)
- **Date**: 2026-11-16
- **Authors**: Ke Shen, Ankita Bhaumik, Li Dong, Shengjie Liu, Shuzhen Li, Naveed Ahmed Janvekar
- **Institution/Company**: Amazon; Princeton University (NeurIPS 2026 workshop PTA)
- **Categories**: cs.AI
- **Abstract**: Tool-use agents must chain interdependent calls, but which outputs satisfy which later inputs is hard to infer from descriptions alone. ToolGraph compiles this once into a directed, weighted dependency graph: parameter matching and **interventional probes** (execute a candidate chain with/without its proposed predecessor) propose edges whose evidence is fused into edge confidence. Prior work uses such graphs for retrieval/path search/next-call scoring; here graph paths are composed into a **goal-conditioned action value Q(s,a,g)**. Three estimators (dynamic programming over entity sets, a distilled GraphSAGE estimator, and an LLM scorer conditioned on graph evidence) plus a verbalizer are compared on two benchmarks and three backbones. Composition pays off only when the estimator also reads the concrete state: the LLM estimator beats personalized-PageRank retrieval in **every** setting (**+8.3 points on average**), while purely structural estimators fall below it — a value over tool types cannot distinguish a correct tool called with a wrong argument. Graph construction is a one-time cost reported separately (comparable to request-time cost at this scale).
- **Key innovations**:
  - Reuses a tool-dependency graph as a **multi-step Q-function**, not just a retriever.
  - Interventional probes with edge confidence to build the graph from a deployed catalog.
  - Shows state-conditioned, LLM-based value estimation is necessary; structural value alone fails.

### 11. Tight PAC-Bayes Generalisation Guarantees for Large Language Model Judges
- **arXiv**: [2611.20818](https://arxiv.org/abs/2611.20818)
- **Date**: 2026-11-16
- **Authors**: Tom A. Lamb, Philip H. S. Torr, Tim G. J. Rudner
- **Institution/Company**: University of Oxford; University of Toronto; Vector Institute; Vijil
- **Categories**: cs.LG
- **Abstract**: LLM judges monitor agent outputs but rarely come with formal reliability guarantees. The paper certifies a judge's risk over safety classifications of prompt–response pairs from a deployed generator using a refined **PAC-Bayes** compression framework with tighter bounds and more efficient coding. Standard parameter-efficient fine-tuning yields **non-vacuous and even tight certificates** for safety judges under both classification and Brier risk, without holding out validation data. **LoRA-GT** shares one quantization scale across layers, giving the tightest certificates with minimal predictive degradation. Across five guardrail models and four benchmarks, certificate tightness is governed more by **adaptation complexity than base-model scale**; the paper also shows how far quantization can go before added risk outweighs the shorter-description gain.
- **Key innovations**:
  - First practical route to **non-vacuous safety-judge certificates** without a held-out set.
  - LoRA-GT cross-layer scale sharing for tight bounds at low performance cost.
  - Identifies adaptation complexity — not model size — as the driver of certificate tightness.

### 12. Optimal Autoregressive Chain-of-Thought Learning via Bagging
- **arXiv**: [2611.21597](https://arxiv.org/abs/2611.21597)
- **Date**: 2026-11-16
- **Authors**: Awni Altabaa, John Lafferty, Omar Montasser
- **Institution/Company**: Department of Statistics and Data Science, Yale University
- **Categories**: cs.LG, stat.ML
- **Abstract**: The task is learning an autoregressive next-token generator from chain-of-thought demonstrations of length *T*. A **bagging** algorithm outputs a majority vote of generators trained to be CoT-consistent on bootstrap samples. For binary token sets it achieves the **optimal sample complexity O((d_VC + log(1/δ))/ε), independent of the CoT length T**; for finite alphabets the VC dimension is replaced by the multiclass Graph dimension *d_G*, giving optimality up to a log|Σ| factor. The ensemble has O(log(T/δ)) members and can be distilled into a single generator in the class at the cost of n·log(nT) unlabeled prompts.
- **Key innovations**:
  - **Length-independent optimal sample complexity** for learning a CoT generator via bagging.
  - Majority vote of CoT-consistent bootstrap generators with a provable ensemble size bound.
  - Distillation back into a single generator using unlabeled prompts.

### 13. MemDoctor: Stage-wise Error Attribution and Repair for MLLM Agent Memory
- **arXiv**: [2611.21019](https://arxiv.org/abs/2611.21019)
- **Date**: 2026-11-16
- **Authors**: Ruiyang Jiang, Xinyang Liao, Weikai Huang, Yuqi Niu, Junjie Zhou, Yubin Zheng
- **Institution/Company**: Shanghai Jiao Tong University; Xi'an Jiaotong University; Xidian University
- **Categories**: cs.CL
- **Abstract**: Multimodal-agent failures usually begin earlier than the final answer — in how a record was written, updated, or retrieved. The paper formalizes multimodal memory as four stages (**Write, Update, Retrieve, Answer**) with nine error types. Stage-resolved analysis on Mem-Gallery attributes most failures to a source stage, mostly before the answer; error-injection experiments show early errors survive downstream as apparent evidence and hurt most when no other record holds the fact, so diagnosing from quoted evidence blames where the error surfaces, not where it began. **MemDoctor** has the memory-building MLLM trace each needed fact backward through the four stages, accepts a diagnosis only when the cited evidence is actually found in memory, and repairs that stage before re-answering. On a **4B backbone** it improves accuracy on Mem-Gallery and MemLens, outperforming all evaluated 8B baselines, and the same loop also improves MuRAG and A-Mem.
- **Key innovations**:
  - **Four-stage, nine-error taxonomy** with causal error tracing from answer back to source stage.
  - Evidence-grounded diagnosis acceptance criterion (avoids plausible-but-unfounded blame).
  - Self-repair loop where a 4B model beats 8B baselines and generalizes to other memory systems.

---

## C. Systems and Efficiency

### 14. MiSTiQ: MicroScaling Trellis Quantization for Extreme KV Cache Compression
- **arXiv**: [2611.21216](https://arxiv.org/abs/2611.21216)
- **Date**: 2026-11-16
- **Authors**: Ofir Gordon, Lior Dikstein, Paul Balanca, Idan Achituve, Douglas Orr, Hai Victor Habi
- **Institution/Company**: Arm AI Research (Arm Ltd); Graphcore Research
- **Categories**: cs.LG
- **Abstract**: Codebook-based KV-cache vector quantization reaches very low bit widths, but hardware limits codebook size and most methods reconstruct the cache in higher precision for attention, forfeiting compute benefits. MiSTiQ is a drop-in replacement combining **trellis-coded storage** with **microscaling (MX) formats** for low-precision computation: trellis quantization plus beam search encodes over large reconstruction spaces without large codebooks, and derived **MX-Hash functions** emit reconstruction values directly in the target MX element format using the scale-conditioned marginal of block-normalized Gaussian inputs. On Llama3 and Qwen3 it achieves lower WikiText perplexity and higher GSM8K accuracy than evaluated baselines across several block-scale formats at roughly **1.25 effective bits per element**, and the highest LongBench average on both models with NVFP4.
- **Key innovations**:
  - **Trellis-coded + beam-searched KV storage** that avoids hardware-limited large codebooks.
  - MX-Hash functions producing values directly in MX/NVFP4 format so attention stays low-precision.
  - Drop-in replacement compatible with existing codebook quantizers at ~1.25 bits/element.

### 15. Memory-Efficient Speculative Decoding with Quantized Draft KV Cache
- **arXiv**: [2611.20565](https://arxiv.org/abs/2611.20565)
- **Date**: 2026-11-16
- **Authors**: Saksham Gupta, Michael Li
- **Institution/Company**: Carnegie Mellon University (AXIOM Workshop, NeurIPS 2026)
- **Categories**: cs.LG, cs.AI
- **Abstract**: Speculative decoding keeps two KV caches; this work quantizes the draft cache while leaving the target cache and verifier in BF16, so compression cannot change the target's final correction rule. A precision-split study finds that with a naive per-token quantizer keys look far more sensitive (**K8V4 beats K4V8 by 10.87 pp** in acceptance), but with grouped per-channel keys the gap becomes **−0.25 pp** — changing only the key quantizer can erase or reverse the preferred split. Following KIVI, the authors adopt **K4V4 with per-channel keys and per-token values**: across six model pairs it cuts draft-cache memory **66.20%** and combined memory **23.95%**, with mean acceptance dropping only 57.93% → 57.14% (1.36% relative).
- **Key innovations**:
  - Isolates the overlooked **draft KV cache** as a memory target without touching target-model correctness.
  - Shows key/value bit allocation is **layout-dependent**, overturning a naive sensitivity conclusion.
  - KIVI-style K4V4 layout yields large memory savings at ~1.4% relative acceptance loss.

### 16. JointQ: Joint Scale-and-Integer Quantization for Large Language Models
- **arXiv**: [2611.20384](https://arxiv.org/abs/2611.20384)
- **Date**: 2026-11-16
- **Authors**: Keiji Kimura, Yuma Ichikawa
- **Institution/Company**: Fujitsu Limited, Kanagawa, Japan (code: OneCompression)
- **Categories**: cs.LG, cs.CL
- **Abstract**: GPTQ optimizes continuous group scales separately from discrete integer assignment. JointQ extends the closed-form optimal-scale evaluation used in per-channel quantization to **group-wise quantization**, where a row's scales are coupled through the Hessian: each local move changes one integer and recomputes its group's optimal scale in closed form while accounting for other groups through the full Hessian, with scales periodically re-solved jointly. Starting from a row-wise choice among scale-refitted candidates including GPTQ means unregularized JointQ never has higher layer-wise calibration error. It preserves the GPTQ output format (drop-in). Across four models/settings it improves six-task average accuracy over vanilla GPTQ in **14/16** comparisons and perplexity in **12/16**; mean accuracy gain rises from 0.0044 (W4G128) to 0.1559 (W3 per-channel), with diagonal Tikhonov regularization mitigating severe W3 perplexity degradation.
- **Key innovations**:
  - **Joint scale + integer local search** with Hessian-aware closed-form scale refits for group-wise PTQ.
  - Monotone-start guarantee relative to GPTQ calibration error and drop-in format compatibility.
  - Largest gains in hard low-bit / large-group regimes, with a regularization fix for W3.

### 17. Making Preemption Productive in Long-Output LLM Serving (Stint)
- **arXiv**: [2611.20106](https://arxiv.org/abs/2611.20106)
- **Date**: 2026-11-15
- **Authors**: Ziji Shi, Xinyi Wan, Chaoyi Ruan, Guangxing Huang, Min Lin, Jialin Li
- **Institution/Company**: National University of Singapore; Sea AI Lab, Singapore
- **Categories**: cs.DC, cs.AI, cs.OS
- **Abstract**: Long reasoning outputs hold KV cache for minutes; when memory fills, preempted requests can repeatedly lose and recover state while producing little output — **KV thrashing**, which in some cases stalls over a fifth of requests for more than a minute. Stint preserves preempted work, bounds wait time, and gives the request fresh output on return: fixed-length KV snapshots go into a contiguity-first CPU pool with an exact-extent allocator, moved via fused K/V gather/scatter kernels and double buffering; age-based readmission and a "protection" turn of fresh decoding precede any new preemption; remaining-length estimates from decoding hidden states guide victim selection. On olympiad-math replays with Qwen3-32B on H200, no request pauses more than 50 s, **p99 time-per-output-token falls 50.7%** versus recomputation, and the replay finishes 10.7% sooner (12.0% higher throughput).
- **Key innovations**:
  - Names and attacks **KV thrashing** by preserving preempted snapshots instead of recomputing.
  - Contiguity-first CPU pool + fused gather/scatter + double-buffered transfer.
  - Age-based readmission and protected fresh-decoding turns; hidden-state remaining-length victim selection.

### 18. CECAR: Cache & Expert Co-Aware Routing Accelerates On-Device Inference of MoE LLMs
- **arXiv**: [2611.20119](https://arxiv.org/abs/2611.20119)
- **Date**: 2026-11-15
- **Authors**: Byeongju Kim, Hoonki Lee, Byungjun Kim, Inyul Ra, Yongjin Kim, Yongseong Lee, Sangyeob Kim
- **Institution/Company**: KAIST; Agency for Defense Development; Yonsei University (NeurIPS 2026)
- **Categories**: cs.LG, cs.AI
- **Abstract**: Large MoE models remain impractical on devices because all expert weights must be memory-resident. The paper observes that cache hit rates are bounded even under Belady's optimal policy, that these bounds are insufficient for low-latency on-device inference, and that prior binary cache-presence routing induces instability. **CECAR** couples routing and cache management with an ML-based policy predicting each expert's **expected reuse distance**, prioritizing routing and execution toward experts with smaller predicted reuse distance. On Qwen3-30B-A3B with a 16 GB consumer GPU and non-resident experts fetched from SSD, CECAR reaches **12.5 tokens/s — a 4.5× speedup** over conventional MoE inference and higher decode speed than baselines keeping the entire model in DRAM.
- **Key innovations**:
  - Formal observation that **Belady-optimal cache bounds are too low** for on-device MoE — routing must be co-designed.
  - Predicted expert reuse distance replaces binary cache presence as the routing signal.
  - SSD-backed 30B-A3B MoE decoding faster than fully DRAM-resident baselines on 16 GB hardware.

---

## D. Games, Game Theory and Sequential Decision

### 19. From Apology to Action: Apologies, Compensation, and Cooperation in LLM Agents
- **arXiv**: [2611.21984](https://arxiv.org/abs/2611.21984)
- **Date**: 2026-11-16
- **Authors**: Grace Ibukunoluwa Ufeoshi, Alessandro Di Stefano, Ndidi Bianca Ogbo, The Anh Han, Zhao Song
- **Institution/Company**: Teesside University; Ravensbourne University London
- **Categories**: cs.GT
- **Abstract**: The study asks whether an LLM agent's apology predicts later cooperation, using controlled **Prisoner's Dilemma** experiments with Claude Opus 4.8, GPT-5.5, Gemini 3.1 Pro, and Mistral Large 3 across payoff conditions, with/without one round of interaction history, and with/without compensation. Apology behavior varies substantially by model and prior outcome, and verbal cooperation does not reliably track subsequent actions: Claude Opus 4.8 apologized even after mutual cooperation, while Mistral Large 3 apologized after being exploited yet kept defecting even against a cooperating opponent. After unilateral defection, positively compensated apologies from GPT-5.5 and Gemini 3.1 Pro were followed by mutual cooperation, unlike those from Claude and Mistral.
- **Key innovations**:
  - Separates **verbal reconciliation from actual strategic behavior** in commercial LLM agents.
  - Adds costly compensation and interaction history as experimental levers.
  - Cross-model evidence that conciliatory messages can precede continued defection.

### 20. LLM Trading Agents Earn Beta, Not Alpha: A Look-Ahead-Free Benchmark
- **arXiv**: [2611.19530](https://arxiv.org/abs/2611.19530)
- **Date**: 2026-11-14
- **Authors**: Jackson Wang
- **Institution/Company**: Not specified in the paper (single author)
- **Categories**: cs.AI, cs.MA
- **Abstract**: The paper introduces **rta-bench-1**, a look-ahead-free backtest over three US markets (rally, bear, crash) that reveals each headline only at its publication minute, plays periods blind and named, checks every run for look-ahead, splits returns into factor exposure and alpha, and scores decisions against random same-day/same-sector choices. Across **91 runs of six models from four vendors**, no alpha was significant; market/style exposure explained a **median 78%** of returns and decisions did no better than random same-sector stocks. Agents bought the most positive-news stocks yet earned as much without headlines. A single cash rule in the prompt cut a GPT-based agent's stock share by 30.3 points in all six pairs, showing rule-following is reliable even when skill is absent.
- **Key innovations**:
  - **Publication-time news replay** plus explicit look-ahead checking removes a common source of inflated agent returns.
  - Factor/alpha decomposition and random same-sector controls separate skill from exposure.
  - Large repeated-run design (models × markets × seeds) quantifying seed noise (5.2 points average).

### 21. The Only Edge Was Memorized in Training: LLM Trading Agents Around Earnings and Bad News
- **arXiv**: [2611.22177](https://arxiv.org/abs/2611.22177)
- **Date**: 2026-11-17
- **Authors**: Jackson Wang
- **Institution/Company**: Not specified in the paper (single author)
- **Categories**: cs.AI, cs.MA
- **Abstract**: Using the same look-ahead-free benchmark, this study tests five models from four vendors **before 598 earnings announcements** and **after 409 bad-news drops** of large US stocks, comparing staged agents, single calls, simple rules, and logistic regression, with and without the stock name. No agent beat the simple bets: before earnings agents mostly bought and earned what buying before every announcement earned; after bad news a Gemini-based agent labeled almost every fall an overreaction, but no agent picked better dips than buying them all. The only gains came from memorized training data — given only ticker and dates, a GPT-based model called **59.2%** of announcement directions before its training cutoff versus **53.3%** after.
- **Key innovations**:
  - Tests the two surviving "edge" windows (scheduled events, post-shock reversal) under strict no-look-ahead.
  - Ticker on/off ablation isolates **training memorization** from genuine event reasoning.
  - Recommends comparing event agents to simple bets and testing blind after the training cutoff.

### 22. CoopDistill: Equilibrium-Guided Multi-Agent Policy Distillation for Cooperative Driving
- **arXiv**: [2611.21069](https://arxiv.org/abs/2611.21069)
- **Date**: 2026-11-16
- **Authors**: Shiyu Fang, Sheng Zhao, Jiarui Zhang, Chengkai Xu, Xiaocong Zhao, Peng Hang, Jian Sun
- **Institution/Company**: Tongji University; Shanghai Jiao Tong University
- **Categories**: cs.RO, cs.MA
- **Abstract**: Cooperative driving must balance safety-constrained optimization (which fixes paths) with MARL's flexible exploration. CoopDistill uses a **potential-game (PG) formulation** as a fixed-path longitudinal reference, around which a residual MARL policy learns longitudinal acceleration, conflict-approach timing, and lateral path corrections. A **hard-case curriculum** concentrates experience on interactions PG leaves unresolved or delayed, and a comparative rollout selector evaluates joint consequences against PG before choosing the executed action. Across merging, roundabout, and intersection scenarios, six baselines, and four CAV penetration levels, CoopDistill improves success by **2.1–27.1 percentage points** and reduces delay **7.3%–27.3%** relative to PG, with no observed collisions.
- **Key innovations**:
  - **Game-theoretic reference + residual MARL** keeps safety guarantees while restoring spatial flexibility.
  - Hard-case curriculum focused on equilibrium's unresolved interactions.
  - Comparative rollout selector for safe joint action execution; zero observed collisions.

### 23. Addressing Exogenous Variability in Cooperative Multi-Agent Reinforcement Learning (LEICA)
- **arXiv**: [2611.22067](https://arxiv.org/abs/2611.22067)
- **Date**: 2026-11-17
- **Authors**: Seongmin Kim, Woohyeon Byeon, Jiwon Jeon, Seungyul Han, Youngchul Sung
- **Institution/Company**: KAIST; UNIST (NeurIPS 2026)
- **Categories**: cs.MA, cs.LG
- **Abstract**: Cooperative MARL often fails when opponents or environment regimes shift uncontrollably. The paper formalizes this as the **Exogenous Dec-POMDP (ED-POMDP)**: an episode-level exogenous regime indexes transition dynamics, and the global state splits into components directly responsive to the team's current action and components that are not. This exposes **mediated influence** — actions cannot update the latter now but can shape their later evolution through the former. **LEICA** is a CTDE-compatible algorithm learning history-conditioned context representations for both components and shaping policy updates with agent-wise, influence-weighted counterfactual intrinsic rewards. On SMAX benchmarks with opponent strategy shifts it improves both training performance and generalization to unseen strategies over baselines.
- **Key innovations**:
  - New **ED-POMDP** formalization distinguishing action-responsive from non-responsive state components.
  - **Mediated influence** as the mechanism for indirect control over exogenous dynamics.
  - Influence-weighted counterfactual intrinsic rewards with CTDE compatibility; generalization to unseen opponents.

### 24. Conflict-Aware Multi-Teacher On-Policy Distillation in Aligned Action Spaces for Cross-Game Generalization
- **arXiv**: [2611.21094](https://arxiv.org/abs/2611.21094)
- **Date**: 2026-11-16
- **Authors**: Jing Yi, Cehao Yang, Hualei Zhang, Haitao Li
- **Institution/Company**: LIGHTSPEED; HKUST(GZ); HKUST
- **Categories**: cs.AI
- **Abstract**: Zero-shot cross-game generalization consolidates source-game experts into one VLM controlling unseen games from pixels without target-game updates. Multi-teacher on-policy distillation (MOPD) faces two bottlenecks in autoregressive VLMs: token-to-action misalignment from subword length bias distorts action probabilities, and teachers under incompatible dynamics issue contradictory corrections (negative transfer). **CAMOPD** uses **complete-action alignment** to normalize command-completion likelihoods over each game's legal action set, forming a calibrated categorical policy with reliable uncertainty margins for selective on-policy retention and cross-game visual specialist probes. Conflict-aware consolidation cross-evaluates specialists across source games, upweighting compatible teachers and suppressing conflicting corrections — without target-game data. On GameWorld temporal and directional transfer suites with Qwen3.5-4B it reaches **26/30 (86.7%)** and **24/30 (80.0%)** Task-1 zero-shot success on unseen GeoDash and Doodle Jump, beating prompting, weight-merging, and multi-task baselines.
- **Key innovations**:
  - **Complete-action alignment** fixes subword bias and yields calibrated action distributions.
  - Cross-game specialist cross-evaluation resolves **teacher conflict** without target-game data.
  - Strong zero-shot VLM game control on unseen games with a 4B model.

---

## Notes and limitations

- Automated snapshot from arXiv API metadata/abstracts queried 2026-11-18; not a full literature review. Metrics and claims are as reported by authors.
- Affiliations were extracted from arXiv HTML author blocks; two single-author entries (Nos. 20 and 21) state no institution and are marked accordingly. Paper No. 2's public abstract is an impact-statement rather than a method/results summary, so its entry intentionally makes no performance claim.
- Dedicated advertising/CTR modeling papers remained scarce in the 11-14…11-17 window; the angle is covered by IntentFlow's A/B click-through results (No. 5), BRAVE's budgeted reflection (No. 2), and the trading-agent signal audits (Nos. 20–21). Re-check coverage on the next run.
- All 24 IDs were checked against every existing report under `wiki/synthesis/` and are new to this wiki as of write time.
- No files were written outside the repository; temporary fetch/cache files live only under `/private/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/` and are removed after use.
