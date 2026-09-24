---
title: "arXiv AI Research Paper Search Report"
type: synthesis
created: 2026-09-24
updated: 2026-09-24
sources: [arxiv.org]
tags: [arxiv, AI, LLM, recommendation, advertising, sequential-modeling, CTR, games, e-commerce-search, reranking, evaluation-audit, extreme-multi-label, watch-time, linear-RNN, scaling-law, KV-cache, memory-attention, MoE, loading-balance, diffusion-LM, agent-harness, multi-LLM-inference, fraud-detection, mechanism-design, auctions, fair-division, two-sided-markets, MARL, video-generation, world-models, daily-digest]
---

# arXiv AI Research Paper Search Report — 2026-09-24

Generated: 2026-09-24 (Thursday). **Fresh Thu 24 Sep 2026 mailing**, parsed from 8 category listing pages (`/list/{cat}/new`): **cs.AI, cs.LG, cs.IR, cs.CL, cs.GT, cs.MA, cs.NE, cs.CV**. **388 unique new-submission IDs** extracted (window **2609.26809–2609.28473**); **21 papers featured in full + 6 runner-ups**, every ID **grep-verified 0 hits in `wiki/`** at selection time.

**Methodology**: Direct page fetches of `/list/{cat}/new` (all announce **Thursday, 24 September 2026**); title/abstract screen of all 388 candidates on target topics (AI / LLM / recommendation / advertising / sequential modeling / CTR / games / auctions & mechanism design / MoE / KV-cache / agentic engineering), full abstracts extracted from the listing pages' abstract paragraphs. Listing HTML cached under the pre-approved temp dir `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/arxiv-search-0924/` and cleaned up after. Institutions are author-affiliation inferred where arXiv does not print them (marked *tentative*).

> **Dedup / race note**: The sibling `arxiv-daily` job wrote `wiki/synthesis/2026-09-24/arxiv-daily.md` **while this report was being built** (it claimed 52 IDs of the same Thunder-24 window via an API sweep of 287 IDs). All overlap between the two reports was resolved by cross-grepping: this report's 27 curated IDs are **disjoint from the 52 arxiv-daily-claimed IDs** (e.g., DSI watch-time 2609.28383, LLM user profiling 2609.27183, XAI seq-rec 2609.27201, agentic shopping 2609.28372, TimeEvo 2609.27277, JEV-Star 2609.27331, LeWAM 2609.27455, DART 2609.28414, AEWM 2609.28416, Hunyuan-A13B 2609.27284, Risk-Controlled KV 2609.27981 are covered there, not here). Sibling jobs that run after us should treat this report's 27 IDs as claimed.

## Summary Statistics

| Scope | Value |
|---|---|
| Window covered | Thu 24 Sep 2026 mailing; /list-parsed IDs 2609.26809–2609.28473 (fresh, 8 categories) |
| Categories parsed | cs.AI, cs.LG, cs.IR, cs.CL, cs.GT, cs.MA, cs.NE, cs.CV |
| Unique IDs parsed | 388 (cs.LG 115, cs.CV 106, cs.CL 73, cs.AI 59, cs.IR 13, cs.GT 10, cs.MA 7, cs.NE 5) |
| Featured in full in this report | 21 papers (5 sections) + 6 shortlisted runner-ups |
| Direct advertising / CTR / pCTR papers | **0** (no commercial CTR/ad-bidding ML; the "auction" hits are mechanism-design theory — Credible Auctions, Pacing Equilibria — plus fraud detection) |
| Rec/interaction relevance | 6 citable papers incl. e-commerce XMC search, LLM-rec reranking ceiling audit, tie-handling eval audit, live-stream assistance, claim calibration |
| Mailing status | `/new` pages announce Thu-24 at fetch time; window terminus at **2609.28473** (cs.CV max) |

**Theme of the window**: concentrated **recommendation/search evaluation science** (LLM-reranking recall ceiling, tie-handling audit, claim calibration, XMC e-commerce search) plus a **strong auction/mechanism-design cluster** (credible auctions via MPC, online fair division vs oblivious adversary, Bulow–Klemperer-style recruitment, pacing equilibria), a **sequential-memory architecture thread** (Linear RNN scaling laws, sequential-computation distillation, shared-global-KV, Memory Attention), and a **diffusion/agent-memory line** (causal shortcuts for DLMs, harness-as-language, selective multi-LLM collaboration, reflective fraud-detection agents).

---

## 1 Recommendation, Search & E-Commerce

### 1.1 The Recall Ceiling of LLM Recommendation Reranking (2609.27953)
- **Title**: The Recall Ceiling of LLM Recommendation Reranking
- **Authors**: Zhaohui Wang
- **Institution**: single author (*tentative*)
- **Date**: Thu 24 Sep 2026 (cs.IR)
- **arXiv**: https://arxiv.org/abs/2609.27953
- **Abstract**: Many LLM-based recommendation rerankers are evaluated under an **oracle protocol** that guarantees the ground truth is in the scored set (injecting it or scoring against sampled negatives). Across three primary Amazon datasets this protocol **overestimates realistic NDCG@10 by 92–95%**. Cause: a **recall ceiling** — realistic retrieval covers only **2–19%** of relevant items at K=100 across 8 datasets in 3 domains, imposing a deterministic upper bound on any closed-candidate reranker's top-k NDCG (`E[NDCG@k] ≤ Recall@|W_π|` under leave-one-out). Under realistic retrieval, none of nine competing optimization strategies (prompt engineering, 168× model scaling, sequential models, supervised rerankers, LoRA, hybrid retrieval, score-aware prompting, LLM+CF fusion) significantly beats the CF baseline. Proposes **RAEP (Recall-Aware Evaluation Protocol)**: classify the retrieval-recall regime first, then evaluate where the ceiling permits differentiation.
- **Key Innovations**: (1) names the oracle-protocol overestimate (92–95%) and proves the recall-ceiling bound; (2) a nine-strategy negative result — reranker sophistication is downstream of retrieval recall; (3) RAEP as a regime-aware evaluation protocol for future LLM-rec work.
- **Venue**: Preprint.

### 1.2 Tie Handling Is Part of the Evaluation Protocol — Order-Invariance Audit (2609.26977)
- **Title**: Tie Handling Is Part of the Evaluation Protocol: An Order-Invariance Audit for Tie-Heavy Recommender Scores
- **Authors**: Chengkun Guo, Han Chen, Yilin Zhu, Yingrui Li
- **Institution**: academic/industrial (*tentative*)
- **Date**: Thu 24 Sep 2026 (cs.IR)
- **arXiv**: https://arxiv.org/abs/2609.26977
- **Abstract**: Offline top-k evaluation ranks a held-out relevant item against sampled negatives; when several candidates score exactly the same, the **tie-breaking rule becomes part of the ranking**. Storage-order-first + stable-sort means the relevant item wins every tie. Defines **row-order invariance** (permuting input candidates leaves ranking unchanged) and audits it by holding candidates/scores fixed and changing only the tie-break. On 30k Amazon Beauty rows, NDCG@10 for a rating-weighted attribute-overlap score is **0.85 under input-order tie-breaking but 0.17 under a deterministic hash tie-break**; independent-hash expectation ≈ uniform-random tie-break mean. Derives expected Hit Rate/NDCG at cutoff k under random tie ordering and provides a reporting checklist.
- **Key Innovations**: (1) formalizes tie-breaking as part of the evaluation protocol; (2) a 0.85→0.17 NDCG demonstration of evaluator fragility; (3) analytic expectation + practical reporting checklist for tie-heavy benchmarks.
- **Venue**: Preprint.

### 1.3 Extreme Multi-Label E-Commerce Search via Lexical Distillation (2609.26921)
- **Title**: Distilling Lexical Product Associations into Deep Transformers: An Extreme Multi-Label Approach for Natural Language E-Commerce Search
- **Authors**: Sunnidhya Roy, Samarpita Bhaumik
- **Institution**: academic/industrial (*tentative*)
- **Date**: Thu 24 Sep 2026 (cs.IR)
- **arXiv**: https://arxiv.org/abs/2609.26921
- **Abstract**: Traditional e-commerce search depends on inverted-index lexical matching (BM25/TF-IDF), which fails on conversational/intent-driven queries (vocabulary mismatch). Formulates conversational product recommendation as **Extreme Multi-Label Classification (XMLC)** over a catalog of N=54k products / C=53,923 classes (27 retail categories, Amazon Reviews '23). A **pseudo-label knowledge distillation** pipeline transfers TF-IDF-cosine item-to-item similarity topologies (K=50 NN) from a corrected lexical teacher into a pretrained **DistilBERT** encoder. Student hits **P@1 = 93.15%, NDCG@10 = 0.8845, MRR@10 = 0.9545** (vs teacher ceiling 98.10 / 0.9419 / 0.9882), and generalizes to situational/cross-category/paraphrased/negative-constraint queries where lexical models fail entirely.
- **Key Innovations**: (1) XMLC framing of e-commerce search with 54k-class catalog scale; (2) lexical-topology distillation into a transformer student (~classic dense-retrieval upgrade path); (3) scalability analysis of extreme-classification projection layers toward two-tower vector search at industrial (>10^6 item) scale.
- **Venue**: Preprint.

### 1.4 Calibrating Reproduced Claims in Recommender Systems (2609.26975)
- **Title**: Calibrating Reproduced Claims in Recommender Systems
- **Authors**: Alan Said
- **Institution**: (Said; Univ. of Gothenburg lineage *tentative*)
- **Date**: Thu 24 Sep 2026 (cs.IR)
- **arXiv**: https://arxiv.org/abs/2609.26975
- **Abstract**: Reproduction studies produce only partially supported claims: values can differ while method ordering holds; results may hold only in some conditions; a released implementation can fail to reproduce something the model can still reach. Terminologies repeatability/reproducibility/replicability describe how a follow-up relates to an original but **not which parts of the original claim the new results support**. Introduces **claim calibration** — state the strongest claim supported by a follow-up plus the conditions under which it holds and what remains untested — applied to five original–follow-up rec-systems paper pairs, showing numerical/method-order/statistical/conclusion agreement do not always coincide. Proposes a **Claim Evidence Profile** for reporting.
- **Key Innovations**: (1) claim calibration as a reporting norm for reproduction studies; (2) five rec-paper case studies disaggregating what does/doesn't transfer; (3) a structured Claim Evidence Profile template.
- **Venue**: Preprint.

### 1.5 Live Assistant — Whether, When, and Whom to Assist in Live Social Streams (2609.27303)
- **Title**: Live Assistant: Learning Whether, When, and Whom to Assist in Real-World Live Social Streams
- **Authors**: Shujian Gao, Jiamei Yan, Yuchen Yang, Penghao Zhou, Qinglei Wang, Tiehan Fan, Yuan Wang, Zuxuan Wu, Yu-gang Jiang
- **Institution**: Fudan-aligned (*tentative* — Wu/Jiang)
- **Date**: Thu 24 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.27303
- **Abstract**: Livestreams are long immersive interaction environments where assistance needs emerge from the stream itself. **LiveAssistant** formulates livestream assistance as four coupled decisions — **whether to act, when, whom to address, and what to communicate** — a 10-second-interval autoregressive policy consuming native audio/video with synchronized comments, gifts, viewer dynamics, and room metadata, selecting `OBS` (silent) / `MEM` (private semantic update) / `ANS` (recipient + task + grounded message). Builds a **trajectory engine** recovering 320+ hours of optimization trajectories and a human-reviewed benchmark (275 clips, 13,812 decision intervals); trains with **Marker-Aware Multiturn SFT** + **Streaming Multiturn GSPO**. Held-out: 71.14 state / 72.67 recipient / 58.41 task accuracy, beating streaming and general multimodal baselines.
- **Key Innovations**: (1) a four-decision formulation of live-stream assistance (selective participation, not always-answer); (2) 320h reconstructed trajectory corpus + human-reviewed decision benchmark; (3) MA-MSFT + SM-GSPO as the training stack for sparse structured stream decisions.
- **Venue**: Preprint.

### 1.6 When Learned Context Planning Fails to Beat Strong Retrieval (2609.26976)
- **Title**: When Learned Context Planning Fails to Beat Strong Retrieval: A Controlled Study of Planning, Routing, and Reranking for Long-Context QA
- **Authors**: Yingrui Li, Han Chen
- **Institution**: academic/industrial (*tentative*)
- **Date**: Thu 24 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.26976
- **Abstract**: Tests whether **learned context planning** (selecting evidence atoms before reasoning) improves long-context MCQ QA after strong retrieval, routing, budgeted-selection, and reranking controls, on all 503 LongBench-v2 MCQ questions (Qwen2.5-7B-Instruct). At an 18k-character budget, anchored hybrid retrieval = **36.18%** and BM25 = 35.98%, while the best planner-guided method reaches 34.19% (41.4% transductive); on the untouched 152-question test split, anchored hybrid stays ahead (42.11% vs 36.84%). Leakage-safe routers cannot convert a large oracle gap; planner gains shrink/turn negative under tight budgets (only +0.40 pts at 6k, loses at 9k). **Verdict: learned planning is a weak relevance signal, not a replacement for strong retrieval.**
- **Key Innovations**: (1) a heavily controlled negative result isolating planning's marginal value; (2) budgeted-selection analysis showing planner gains do not persist under tight budgets; (3) a strong-retrieval baseline for the planning-on-hold literature (plan-vs-retrieve).
- **Venue**: Preprint.

---

## 2 Sequential Modeling & Attention Architecture

### 2.1 Linear RNN Scaling Laws — When Longer Sequences Beat More Sequences (2609.27964)
- **Title**: Linear RNN Scaling Laws: When Longer Sequences Beat More Sequences
- **Authors**: Ziyan Chen, Zhongzhu Zhou, Peilin Liu, Ding-Xuan Zhou
- **Institution**: City University of Hong Kong-aligned (*tentative* — Zhou)
- **Date**: Thu 24 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.27964
- **Abstract**: Derives **scaling laws for autoregressive sequential pretraining in a tractable teacher–student model**: a stable latent linear RNN generates trajectories; a sketched linear recurrent student (sketch dim M = model size) trains via safeguarded full-batch WSD on next-token prediction, with N independent trajectories of length P as tokens. Innovation/initialization covariances carry power-law exponents α and θ; the induced design spectrum yields explicit approximation, optimization, and statistical rates separated by spectral crossovers. When θ ≥ α, single-scale rates recover; when α−2r ≤ θ < α, a heavier initialization tail changes rates beyond P-dependent crossovers.
- **Key Innovations**: (1) first principled scaling-theory treatment of *sequential* pretraining (N×P factorization of data); (2) shows the variance keeps the $(NP)^{-1}$ factor but sequence length also suppresses the initialization transient — **N and P are not fully interchangeable in the two-scale regime**; (3) spectral-crossover structure linking model size M↔sequence length P.
- **Venue**: Preprint (theory).

### 2.2 Distilling Sequential Computation in Transformer Language Models (2609.27233)
- **Title**: Distilling Sequential Computation in Transformer Language Models
- **Authors**: Zixuan Lan, Jessica Yang, Yanhong Li, Karen Livescu, Jiawei Zhou
- **Institution**: TTIC/Northwestern-aligned (*tentative* — Livescu)
- **Date**: Thu 24 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.27233
- **Abstract**: Adjacent token spans are highly predictable, suggesting representations may be compressible. Introduces a **merge module** that collapses spans of tokens into a single surrogate embedding computed on the fly from static token embeddings, capturing the multi-token functional role — pretrained models run on compressed inputs **without architecture changes or retraining**. Applied at inference to compress prompts and intermediate decoding steps, with a **rollback mechanism** substituting stored multi-token KV-cache entries with single-step surrogates. Reduces effective sequence length **up to 40%** with minimal accuracy loss across LM-eval plus QA, summarization, commonsense, and long-form math; light adaptation improves the accuracy–compression trade-off further.
- **Key Innovations**: (1) distillation of *sequential computation* (collapsed surrogates) as a training-free inference lever; (2) KV-cache surrogate rollback inside decoding; (3) 40% sequence-length compression across diverse models/tasks.
- **Venue**: Preprint.

### 2.3 Shared Global KV with Layer-Specific Local History (2609.28006)
- **Title**: Shared Global KV with Layer-Specific Local History
- **Authors**: Xinglang Xian
- **Institution**: single author (*tentative*)
- **Date**: Thu 24 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.28006
- **Abstract**: Sharing KV across layers saves storage but reduces representational diversity across depth. Studies what **local memory** should retain alongside shared global KV, separating historical content from the input source that formed it. At 126M params / 2K context, an eight-seed study finds **~1.4% lower held-out perplexity** with local history vs a current-token local branch; capacity/entry-count/compute controls support the value of historical content. Equal-learning-rate comparisons against GQA and adjacent-layer KV sharing show better same-source likelihood with larger caches and higher long-request latency; ordering persists after adaptation to 8K (with a short-context cost). Derives a sufficient suffix schedule reducing upper-layer construction work while preserving the cache in exact arithmetic.
- **Key Innovations**: (1) separates *content* from *source* in local-memory design for shared-KV architectures; (2) eight-seed empirical protocol for cache-sharing comparison; (3) suffix-schedule result for cache-construction efficiency.
- **Venue**: Preprint.

### 2.4 Memory Attention — Token-Indexed Value Memory (2609.28399)
- **Title**: Memory Attention
- **Authors**: Jiale Kang
- **Institution**: single author (*tentative*)
- **Date**: Thu 24 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.28399
- **Abstract**: Language models build attention values from contextual hidden states even when part of that content is reusable across contexts. **Memory Attention (MA)** forms values by combining **layer-specific token memory** with contextual keys — memory supplies token-specific representations, keys preserve context dependence. At inference, normalization folds into memory tables, reducing value construction to **lookup and addition**; token-indexed retrieval enables **CPU offloading with prefetching**, cutting GPU parameter storage. With matched training-token budgets and additional memory parameters, MA improves language modeling and average downstream performance across attention configurations.
- **Key Innovations**: (1) token-indexed memory replaces the dedicated value projection (value = context-key + memory lookup); (2) CPU-offload + prefetch serving path; (3) favorable LM/downstream results under matched compute budgets.
- **Venue**: Preprint.

---

## 3 LLM Efficiency, MoE & Reasoning

### 3.1 Scaling of Capability and Efficiency at Inference Time in Large Reasoning Models (2609.27166)
- **Title**: Scaling of Capability and Efficiency at Inference Time in Large Reasoning Models
- **Authors**: Moritz Laber, Zohair Shafi, Germans Savcisens, Brennan Klein, Matteo Chinazzi, Samuel V. Scarpino, Albert-László Barabási, Tina Eliassi-Rad
- **Institution**: Northeastern / ISI / network-science cluster (*tentative* — Barabási/Eliassi-Rad)
- **Date**: Thu 24 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.27166
- **Abstract**: Uses **hierarchical Bayesian models** to separate capability (probability of solving a problem) from **efficiency** (tokens-to-correct) across the DeepSeek-R1-Distill family on four arithmetic/algorithmic classes. At fixed size, correct-solve probability **decays ~exponentially with instance size** (hardness proxy); the decay scale grows **sublinearly** with model size (capability gains diminish). Output length grows as a power law with instance size, but its parameters do **not** vary systematically with model size — **larger models are no more efficient**. Position paper-grade implication: naive scaling buys capability with diminishing returns and near-zero efficiency gains.
- **Key Innovations**: (1) joint hierarchical-Bayesian model of capability × efficiency (vs loss-only scaling law); (2) "efficiency plateau" finding across model scales; (3) clean problem-hardness control for reasoning scaling analysis.
- **Venue**: Preprint.

### 3.2 Exact Quantile Balancing + Load-Error Injection for MoE (2609.28053)
- **Title**: Exact Quantile Balancing and Load-Error Injection for Mixture-of-Experts
- **Authors**: Pit Neitemeier, Jiaze Li, Alessio Serra, Philipp Scholl, Sohir Maskey
- **Institution**: academic/industrial (*tentative*)
- **Date**: Thu 24 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.28053
- **Abstract**: MoE training needs **global** load balance (avoid expert under-utilization) and **local** balance (efficient expert-parallel execution). Existing distributed Quantile Balancing uses shard-dependent/approximate global quantiles; token-independent biases can't guarantee microbatch-level balance. Introduces **EQB** (Exact Quantile Balancing — exact global-batch BF16 quantiles with negligible communication cost) and **LEI** (Load-Error Injection — injects local load errors directly into router-score gradients). On 7.5B-parameter MoEs trained up to **500B tokens**: EQB beats naive QB on global balance and downstream performance; LEI improves local balance and outperforms the GShard loss at comparable quality.
- **Key Innovations**: (1) exact (not approximate) global quantiles at negligible comm cost; (2) gradient-level local-load-error injection for microbatch balance; (3) 500B-token MoE evidence vs quantile-balancing and GShard baselines.
- **Venue**: Preprint.

### 3.3 Causal Shortcuts for Efficient Diffusion-LM Reasoning (2609.28272)
- **Title**: Towards Efficient Reasoning: Learning Causal Shortcuts for Diffusion Language Models
- **Authors**: Dian Jin, Kairong Han, Baohong Li, Xinpeng Dong, Zijing Hu, Nuanqiao Shan, Fei Wu, Kun Kuang
- **Institution**: Zhejiang University-aligned (*tentative* — Wu/Kuang)
- **Date**: Thu 24 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.28272
- **Abstract**: Diffusion LMs, with bidirectional attention, explore an exponentially larger space than autoregressive models and struggle to focus on reasoning-guiding tokens under random masking. Defines **causal shortcuts** — token chains covering the full sequence that give explicit guidance toward correct reasoning trajectories — and shows they improve answer convergence efficiency and generation accuracy. The **CSL (Causal Shortcut Learning)** framework extracts shortcuts step-by-step from data and applies **parallel prioritized masking** during training. Beats SFT-variant baselines across reasoning benchmarks (+1.92% avg over SFT-only, up to **+4.20% on MATH-500**).
- **Key Innovations**: (1) causal-shortcut token chains as a masking-prior for DLM reasoning; (2) parallel prioritized masking — no model-architecture change; (3) consistent gains across two base models / multiple reasoning benchmarks.
- **Venue**: Preprint.

---

## 4 Agentic Systems & Agent Training

### 4.1 Harness as a Language — JAZ (2609.26891)
- **Title**: Harness as a Language: A Minimalist Agent Framework With Maximal Expressivity
- **Authors**: Zhening Li, Joshua Liu, Mateja Vukelic, Nicole Shen, Supriya Lall, Amitayush Thakur, Alex Zhang, Omar Khattab, Jonathan Light, Armando Solar-Lezama
- **Institution**: MIT-aligned (*tentative* — Solar-Lezama/Khattab)
- **Date**: Thu 24 Sep 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.26891
- **Abstract**: Asks how much engineering beyond the **agent loop** is actually needed. **JAZ** is a minimal harness exposing one primitive, `invoke` — the simplest LLM loop satisfying: (1) the LLM can write arbitrary executable code including *recursive* `invoke`; (2) everything visible to the LLM (all inputs and interaction history) are variables in the code environment. Built-in hooks allow constraints/monitoring. With **only prompting** (no bespoke tools, memory, or file systems), JAZ `invoke` outperforms **Letta (MemGPT) by 8% at half its cost** on the recall-heavy portion of StuLife, and matches specialized continual-self-improvement workflows.
- **Key Innovations**: (1) `invoke` as a language primitive — harness = runtime-provided function implementation; (2) maximal expressivity from minimal structure (recursive invoke + code-environment variables); (3) strong externals vs memory-specialized harnesses at half cost.
- **Venue**: Preprint.

### 4.2 COMED — The Missing Middle Between Routing and Collaboration (2609.26913)
- **Title**: COMED: The Missing Middle Between Routing and Collaboration in Multi-LLM Inference
- **Authors**: Norah Alballa, Wenxuan Zhang, Salma Kharrat, Fares Fourati, Zafar Ayyub Qazi, Mohamed Elhoseiny, Marco Canini
- **Institution**: KAUST-aligned (*tentative* — Canini/Elhoseiny)
- **Date**: Thu 24 Sep 2026 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2609.26913
- **Abstract**: Routing stops after selecting an initial model; dense collaboration invokes peers on every query. Shows collaboration is **non-monotonic** — peers recover failures no single model solves alone but can also corrupt initially-correct answers. **COMED** is a **post-anchor controller** for selective cross-model escalation: anchor self-consistency + router margin + a cheap peer probe accept confident answers, verify ambiguous cases, and escalate only when collaboration likely pays. Formalizes a **rescue–harm decomposition**; improves fixed and routed anchors in **all 16 open-weight settings** (+up to 10.7pp on MedQA) with fewer invoked models and tokens than dense collaboration; on HLE improves GPT-5.5 23.1%→28.1% (best overall).
- **Key Innovations**: (1) names collaboration non-monotonicity (rescue vs harm) and decomposes it; (2) controlled escalation as the missing "middle" between routing and dense collaboration; (3) 16-setting open-weight + frontier-HLE evidence of Pareto-superior cost/quality.
- **Venue**: Preprint.

### 4.3 SR-Fraud — Outcome-Supervised Reflective Agent for Non-Stationary Payment Fraud (2609.27287)
- **Title**: SR-Fraud: An Outcome-Supervised Reflective LLM Agent Framework for Non-Stationary Payment Fraud Detection
- **Authors**: Xuwei Tan, Yao Ma, Xueru Zhang
- **Institution**: industrial/academic (*tentative*)
- **Date**: Thu 24 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.27287
- **Abstract**: Real-time payment fraud is a **non-stationary streaming problem** — adversaries adapt before labels mature; burst attacks cause losses before retraining. **SR-Fraud** decouples request-time decisions from offline adaptation: a **frozen, stateless scoring agent** reads a Hybrid Episodic Window to track behavioral shifts per transaction; an offline **reflection agent** proposes boundary hypotheses from matured errors; a **deterministic verifier** admits only supported hypotheses into an executable knowledge state. On a production payment-fraud benchmark improves all detection metrics over the frozen agent, beats static/periodically-retrained CatBoost on point estimates, and detects an emerging fraud burst.
- **Key Innovations**: (1) frozen decision path + verified offline adaptation (no request-time drift); (2) Hypothesis-verifier gate controlling knowledge-state mutation; (3) burst-detection evidence on a production benchmark.
- **Venue**: Preprint.

---

## 5 Games, Auctions & Mechanism Design

### 5.1 Credible Auctions via MPC Gadgets (2609.27402)
- **Title**: Credible AUctions via MPC Gadgets: Bounding Information Leakage Under Abort
- **Authors**: Matheus Venturyne Xavier Ferreira
- **Institution**: (single author; crypto-mechanism design)
- **Date**: Thu 24 Sep 2026 (cs.GT)
- **arXiv**: https://arxiv.org/abs/2609.27402
- **Abstract**: Credible auctions face a **cryptographic barrier** when the auctioneer controls shill bidders: monolithic MPC gives the auctioneer a "free option" (learn outcome, abort if revenue unsatisfactory) by Cleve's coin-flip impossibility; commitments + ex-ante penalties cannot suffice for heavy-tailed distributions. Introduces the **MPC Decomposition Principle** — use MPC strictly as an *information-restriction* gadget, isolating winner determination (reveals winner's identity, **no payment**) — then **Sequential Revelation Auction (SRA)**: leakage bounded ⇒ value of the free option bounded; a penalty of `k ≥ Σ Rev(F_i)` is sufficient for credibility and **tight** for equal-revenue distributions. **Constant-round, incentive-compatible, revenue-optimal credible auction** for all product distributions with vanishing revenue tails — resolves the Akbarpour–Li / Ferreira–Weinberg open question.
- **Key Innovations**: (1) MPC-decomposition: cryptographically minimal winner-determination gadget, not full-mechanism MPC; (2) information-leakage-bounded credibility with a tight penalty; (3) constant-round revenue-optimal credible auction for general product distributions.
- **Venue**: Preprint.

### 5.2 Online Fair Division Against an Oblivious Adversary (2609.28333)
- **Title**: Online Fair Division Against an Oblivious Adversary
- **Authors**: Saar Cohen, Nicholas Teh, Michael Wooldridge
- **Institution**: Oxford-aligned (*tentative* — Wooldridge)
- **Date**: Thu 24 Sep 2026 (cs.GT)
- **arXiv**: https://arxiv.org/abs/2609.28333
- **Abstract**: Online allocation of indivisible goods (allocate immediately & irrevocably). Under an **adaptive** adversary, no algorithm guarantees a good-independent positive PROP1/PROPk approximation; here the **oblivious** adversary fixes input in advance. Improves the Choo et al. uniformly-random baseline from `Θ(1/log(n/δ))`-PROP1 to **`Ω(1/loglog(n/δ))`** with a δ-free algorithm (same algorithm works for every δ), giving each agent almost her bundle with high probability. Contrast: for **EF1**, every randomized algorithm has an input where `α`-EF1 probability ≤ `e^{−Ω(n)}`; EFX probability ≤ 1/n! (near-optimal); MMS ≤ 5/6. Allowing more removals gives positive envy-freeness guarantees (EF up to logarithmically many goods, factor →1).
- **Key Innovations**: (1) tightening randomness-based online fair division to `1/loglog` under an oblivious adversary; (2) a sharp adaptive-vs-oblivious adversary separation (PROP attainable vs not); (3) near-optimal impossibility bounds for EF1/EFX/MMS in the online setting.
- **Venue**: Preprint.

### 5.3 Two Additional Traders Suffice in Two-Sided Markets (2609.27304)
- **Title**: The Power of Recruiting the Smaller Side: Two Additional Traders Suffice in Two-Sided Markets
- **Authors**: Yang Cai, Vineet Gupta, Yanchen Jiang, Christopher Liaw, Aranyak Mehta, Grigoris Velegkas, Di Wang, Mingfei Zhao
- **Institution**: McGill / Google / Yale / Apple-aligned (Cai, Gupta, Mehta, Zhao; multi-institution)
- **Date**: Thu 24 Sep 2026 (cs.GT)
- **arXiv**: https://arxiv.org/abs/2609.27304
- **Abstract**: Bulow–Kemperer-style **competition complexity** in two-sided double auctions with m unit-demand buyers vs n unit-supply sellers. When m ≥ n and buyer values FSD-dominate seller costs, **recruiting just two additional sellers** lets **Seller Trade Reduction (STR)** — a prior-independent mechanism — achieve expected GFT ≥ the first-best GFT of the original market; symmetrically for the buyer side. Resolves open questions of Babaioff–Goldner–Gonczarowski (SODA 2020) and Cai–Liaw–Mehta–Zhao (STOC 2024). Uniform bound is **optimal**: for m=n=1 no prior-free DSIC+IR+budget-balanced mechanism matches first-best GFT with only one extra seller.
- **Key Innovations**: (1) two-traders-suffice prior-independent trade-reduction result; (2) optimality tightness even in the minimal 1×1 market; (3) resolves two venue-level open problems with a non-welfare-preserving mechanism class.
- **Venue**: Preprint (after SODA'20/STOC'24 line).

### 5.4 Pacing Equilibria in Abstract Mechanisms (2609.27285)
- **Title**: Pacing Equilibria in Abstract Mechanisms
- **Authors**: Salam Afiouni, Christian Kroer
- **Institution**: Columbia-aligned (*tentative* — Kroer)
- **Date**: Thu 24 Sep 2026 (cs.GT)
- **arXiv**: https://arxiv.org/abs/2609.27285
- **Abstract**: Multiplicative pacing (scaling buyer bids to spread budgets) is operationally simple but its aggregate behavior is mechanism-dependent — first-price single-item markets have strong structure that fails in second price markets. Develops a **unified theory of pacing equilibria** across a hierarchy of mechanisms: even in first-price **position** auctions the single-item market-equilibrium interpretation can fail; identifies **bid-maximizing pay-your-bid** mechanisms as the broad class where pacing equilibria exist, are unique, and have an Eisenberg–Gale convex-program characterization (efficient computation, Pareto-efficiency, liquid-welfare guarantees). For abstract mechanisms with payment monotonicity, proves existence by smoothing discontinuities and, under extra conditions, uniqueness, revenue-maximality among budget-feasible pacing vectors, shill-proof implementability, and convergent budget-adjustment dynamics.
- **Key Innovations**: (1) elevates pacing-equilibrium theory from single-item first-price to position auctions and general mechanisms; (2) Eisenberg-Gale characterization of a practically-core mechanism class; (3) existence/optimality/shill-proofness transferable conditions for large-scale budget-based allocation.
- **Venue**: Preprint.

### 5.5 Evolutionary Stability Does Not Guarantee Learning Accessibility (2609.27664)
- **Title**: Evolutionary Stability Does Not Guarantee Learning Accessibility: A Multi-Agent Reinforcement Learning Perspective on Cooperation Emergence
- **Authors**: Yijie Wang
- **Institution**: single author (*tentative*)
- **Date**: Thu 24 Sep 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.27664
- **Abstract**: Cooperation emergence needs decentralized agents coordinating while adapting. Evolutionary stability under a population dynamic need not imply **finite-sample learning agents** can reach the outcome through local reward feedback. Studied in a three-agent governance-motivated game (government/platform/users) using replicator dynamics vs three decentralized value-based learners (ε-IQL, scaled Boltzmann, SA–EA BQL). The cooperative evolutionary basin has volume **V_E = 1.00** on the sampled grid, yet empirical learning basins are 0.88 (ε-IQL) and **0.00** (both exploration variants). Broader action diversity + nonzero value separation can coexist with failure to sustain the cooperative joint action.
- **Key Innovations**: (1) distinguishes evolutionary stability from learning accessibility for coupled game–learning systems; (2) a stark V_E=1.00 / learning-basin=0.00 separation result; (3) transferable methodology (population-stability vs finite-sample accessibility grids) for multi-agent governance/games.
- **Venue**: Preprint (theory/empirical).

---

## Key Trends Across This Window

1. **Rec/search evaluation science is the day's rec spine** (27953 recall-ceiling of LLM reranking with a 92–95% oracle overestimate; 26977 tie-handling audit with a 0.85→0.17 NDCG flip; 26975 reproduction claim calibration; 26921 XMC e-commerce lexical distillation): after the sibling daily's serving-engineering rec picks, this report's layer is *how rec results are measured* — a healthy complement to the same window.
2. **Sequential memory architecture returns as theory + mechanism** (27964 Linear-RNN scaling with N/P non-interchangeability; 27233 40% sequential-computation distillation; 28006 shared-global-KV local history; 28399 token-indexed Memory Attention): the "recurrent vs attention memory" debate is now being settled at the scale-law and cache-design level.
3. **Mechanism design is the window's strongest theory cluster** (27402 credible auctions with MPC-decomposition + tight penalties; 28333 oblivious-adversary online fair division at 1/loglog; 27304 two-traders-suffice trade reduction; 27285 pacing equilibria beyond single-item first-price): four papers across auctions/allocations — coheres with the wiki's ads/mechanism-design thread and prefigures ads-market theory content.
4. **Inference-time scaling gets its negative/scrutiny results** (27166: capability gains diminish while efficiency plateaus across scales; 26976: learned context planning loses to strong retrieval under budgets): "more test-time compute" is increasingly evaluated as a trade, not an axiom.
5. **Selective vs brute multi-model/agent structures** (26913 COMED controlled escalation with rescue–harm decomposition; 26891 JAZ harness-as-language at half Letta cost; 27287 SR-Fraud frozen-decide + verified-adapt): the window's agent thread favors *minimal, gated, verified* architectures over maximal orchestration.
6. **Games layer thin but principled** (27664 MARL evolutionary-vs-learning accessibility; SD-related AR video memory in runner-ups): no fresh pure game-bot/PCG marquee unclaimed (JEV-Star was taken by the sibling daily in its §7.5).

## ADS / CTR Coherence Check

**0 direct CTR/advertising-ML papers** in this report's partition (11th–12th consecutive daily window; consistent with sibling reads). The window's closest value-layer lines live here in the *mechanism-design* replica: **Credible Auctions** (27402) and **Pacing Equilibria** (27285) both speak to ad-auction credibility/budget-management theory, and **SR-Fraud** (27287) covers the payments side. The watch-time/theory-driven rec items (DSI 2609.28383) and agentic shopping (2609.28372) were claimed by the sibling `arxiv-daily` and are cross-referenced there. As noted across September, end-to-end CTR/pCTR content continues to arrive via conference batches and the `arxiv-paper-check`/`conference-digest` layers rather than the raw daily arXiv side.

## Runner-Ups (shortlist, all grep-verified 0 hits in `wiki/`)

- **2609.27213** BoundaryMORPH — budgeted reranking via active-set selection for "diffuse" RAG retrieval; allocates a strict cross-encoder budget beyond the context-window capacity instead of re-scoring obvious top candidates (cs.IR).
- **2609.27845** Query Implied Generative Engine Optimization — GEO for black-box generative search engines grounded in query-implicit signals, vs explicit-query-derived alignment (cs.IR) (*abstract truncated in listing*).
- **2609.27867** Evaluation Choices Decide the Forecasting Leaderboard — 24 forecasting methods on a production marketplace panel (1,887 customers × 67 months); changing the unit of analysis moves the production baseline from 2nd-of-19 to 23rd-of-25 — an evaluation-design-reversal result for TSFM benchmarking (cs.LG).
- **2609.27038** Are Stated Reasoning Steps Causally Load-Bearing? — activation-level CoT faithfulness via counterfactual-tagged patching on synthetic multi-hop lookups (predicts the switched answer, unlike degradation-only audits) (cs.AI).
- **2609.26929** Which Objectives Need a Dial? — pre-training measurements predict objective conflict/alignment for human-annotated data (but not AI-annotated) in steerable pluralistic alignment (MODPO) (cs.AI).
- **2609.28466** The Past Frames the Future — bounded-memory autoregressive video generation with explicit memory (entity identity, dynamic state, intervention-driven causal change) for long-horizon consistency (cs.CV).

## Cross-Reference Index (Sibling & Runner-Up Coordinates)

- **Same-window coordination**: `arxiv-daily` (09-24) wrote first and claimed 52 IDs — including the window's rec/ads marquees **DSI 2609.28383**, **LLM user profiling 2609.27183**, **XAI seq-rec 2609.27201**, **agentic shopping 2609.28372**, plus KV/agents/games-content (**TimeEvo 2609.27277**, **JEV-Star 2609.27331**, **LeWAM 2609.27455**, **DART 2609.28414**, **AEWM 2609.28416**, **Hunyuan-A13B 2609.27284**, **Risk-Controlled KV 2609.27981**, **KVSET 2609.27746**, **DeltaS 2609.27470**, **WISE 2609.27373**, **DPara 2609.27396**, **ProCredit 2609.27532**, **JitMem 2609.27334**, **PASTABench 2609.28197**, **Shutdown Sabotage 2609.28274**, **CAVEAT 2609.27273**, **MVCAP 2609.27461**, **RecCAR 2609.27901**, **InternW0 2609.27656**, **RefineICL 2609.27679**, **LoReST 2609.27637**, **ROOSTER 2609.27473**, **Step Law <59M 2609.27581**, **PTTS 2609.27374**, **GUI-SD-v2 2609.27307**, **VHD-Play 2609.27321**, etc.). This report's 21 + 6 runner-up IDs were selected **after** full-diff against that set (per-ID `rg` verified 0 hits; the two initially-shortlisted IDs 2609.28095 / 2609.27588 were dropped as daily-claimed).
- **Unclaimed-remainder map** (for later sibling sweeps): beyond this report's 27 IDs and the daily's 52, the strongest remaining unclaimed candidates we noticed were 2609.27252 (Platonic convergence: structure over geometry), 2609.27306 (discrete diffusion via evolving variational AR networks), 2609.27411 (oscillatory SSM for vibration diagnosis), 2609.28145 (policy distillation for RL), 2609.28064 (SlackDrive adaptive driving inference), 2609.28342 (zero-shot object removal), and 2609.27675 (Track2Art 3D models from 2D point tracks) — a starter map only, not claim-verified.

(End of file)