---
title: "arXiv Paper Check — AI & CTR (2026-11-17)"
type: synthesis
created: 2026-11-17
updated: 2026-11-17
sources:
  - https://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL&sortBy=submittedDate&sortOrder=descending&max_results=40
  - https://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=submittedDate&sortOrder=descending&max_results=25
  - https://export.arxiv.org/api/query?search_query=cat:cs.IR+OR+all:%22click-through+rate%22+OR+all:CTR&sortBy=submittedDate&sortOrder=descending&max_results=40
  - https://export.arxiv.org/api/query?search_query=all:%22click-through%22+OR+all:%22CTR+prediction%22+OR+all:%22advertising%22&sortBy=submittedDate&sortOrder=descending&max_results=25
  - https://rss.arxiv.org/rss/cs.IR
tags:
  - arxiv
  - daily-check
  - ai
  - ctr
  - recommendation
  - advertising
  - retrieval
  - agents
  - llm
  - generative-recommendation
  - daily-digest
---

# arXiv Paper Check — AI & CTR (2026-11-17)

> **Window note:** Checked on **2026-11-17** (Tue). The most recent arXiv announcement list (cs.IR RSS, `lastBuildDate` Mon 2026-11-16 05:00 UTC) falls inside the 24-hour window and contains submissions dated **2026-11-13** — those were already summarized by the sibling `arxiv-daily.md` / `arxiv-ai-search.md` reports for today. The **freshest submissions available via the API are dated 2026-11-14** (IDs ~2611.19xxx), which are not yet in the RSS announcement block. This brief therefore curates the **newest 2026-11-14 batch**, plus a small number of highly relevant 2026-11-13/11-12 items that are new to this wiki. All papers below were checked against `wiki/synthesis/**` and are absent from prior reports except where explicitly cross-referenced. All results and metrics are **author-reported**.

## Highlights

| Area | Pick | Why it matters |
|------|------|----------------|
| CTR / Ads | **TokenFormer V2** (2611.19074) | Tencent industrial unified recommender: 5.1× fewer FLOPs and **+2.33% GMV** in a live WeChat Channels advertising A/B test. |
| Rec / Interpretability | **CLEAR** (2611.19110) | Meta-deployed recommender with an editable natural-language interest layer users can inspect and steer (also covered in today's `arxiv-ai-search`). |
| Rec / Fairness Audit | **Verbosity bias in LLM recommenders** (2611.18878) | Label-free randomized-paraphrasing audit finds description length raises selection odds by up to 38% per SD across 9 LLMs. |
| Ads / Systems | **MXFP6 for R&R models** (2611.17501) | First reported native 6-bit GEMM speedups for production ads ranking while holding the strict 0.01% Normalized Entropy launch bar. |
| AI / LLM Safety | **On-policy distillation as a backdoor channel** (2611.19207) | Shows OPD transfers a teacher backdoor far more efficiently than standard distillation — a supply-chain risk for post-training. |
| AI / Tool Use | **Beyond Plain MCP** (2611.19123) | Controlled MCP study: code mode cuts tokens 70–90%, but a decision layer in front adds little; return-shape hints dominate. |
| AI / Eval | **What Moves a LoCoMo Score?** (2611.19199) | Changing only the judge moves a long-term-memory score by 7.2 points and the answer prompt by 9.3 — a benchmark-validity warning. |

## 1) AI — LLMs, Agents, Reasoning, Safety

### On-policy distillation as a Backdoor Propagation Channel
- **arXiv:** [2611.19207](https://arxiv.org/abs/2611.19207) (cs.LG, cs.AI; submitted 2026-11-14)
- **Authors:** Zane Fu, Yanzhao Zheng, Ziting Qin, Qianshan Wei, Yi Yu, Gongli Xi, Jihuai Zhu, Baohua Dong, Hangcheng Zhu, Ruohui Huang, Gang Yu
- **Key contributions:**
  - Reveals a supply-chain risk in **on-policy distillation (OPD)**: an attacker implants a conditional backdoor in a teacher via SFT, and OPD transfers it to the student with only an extremely small fraction of trigger-prompt exposure.
  - Finds backdoor transfer is **substantially stronger under OPD than under conventional distillation**, suggesting OPD is an efficient propagation channel across models.
  - Mechanistic analysis: the signal travels through anomalous conditional-probability differences between triggered and clean inputs, then becomes internalized in student representations; proposes an OPD training method that suppresses these signals at the supervision source.
- **Why interesting:** OPD is increasingly central to LLM post-training; this reframes an efficiency technique as a security surface.

### Beyond Plain MCP: Do Decision Models and Code Mode Make Tool Use Cheaper and Faster?
- **arXiv:** [2611.19123](https://arxiv.org/abs/2611.19123) (cs.SE, cs.AI, cs.CL; submitted 2026-11-14)
- **Authors:** Abhishek Rai
- **Key contributions:**
  - Preregistered evaluation across 12 MCP servers, up to 1,958 distractor tools, and three open-weight agents (Qwen, Gemma, Nemotron) on a sealed test split.
  - **Code mode cuts token usage by 70–90%** and significantly boosts utility versus plain MCP.
  - Declaring **return-shape hints** in code-mode stubs swings success by up to 39.5 points for weaker agents — a larger effect than adding a router. The hypothesis that a decision layer in front of code mode beats code mode alone is **not confirmed**.
- **Why interesting:** Directly tests two popular MCP gateway designs and shows the cheaper architectural choice often wins; releases harness, a 4B tool-selection model, and traces.

### What Moves a LoCoMo Score? Memory Context, Answer Prompts and Judges
- **arXiv:** [2611.19199](https://arxiv.org/abs/2611.19199) (cs.AI; submitted 2026-11-14)
- **Authors:** Nikhil Kumar Jha, Amitoj Cheema
- **Key contributions:**
  - Decomposes a widely reported long-term-memory benchmark: 10 conversations / 1,540 questions, two answer models, two answer prompts, three LLM judges, run against a whole-conversation baseline under identical conditions.
  - **Changing only the judge moves a score by up to 7.2 points; changing only the answer prompt by up to 9.3.**
  - Evaluates Becos (a team memory system for coding agents): 90% fewer context characters, clearly higher than whole-conversation with gpt-4o-mini answers (79.7 vs 73.0 short prompt; 88.8 vs 77.5 step-by-step), roughly tied with gpt-4.1-mini; a blind human check finds primary-judge errors work against Becos.
- **Why interesting:** Concrete evidence that memory-system leaderboards can be dominated by evaluation choices rather than memory quality.

### When the Mythical Man-Month Meets Agentic Web Systems: Structured Coordination for Scalable Development
- **arXiv:** [2611.19140](https://arxiv.org/abs/2611.19140) (cs.SE, cs.AI; submitted 2026-11-14)
- **Authors:** Zhiyao Wu, Zi Liang, Haibo Hu
- **Key contributions:**
  - Studies agent population size vs per-agent token consumption and coordination overhead on complex Web-development tasks; finds a **non-linear scaling pattern** — per-agent tokens fall at first, then show diminishing returns.
  - Proposes the **Surgical Team Model (STM)**: role specialization, constrained inter-agent communication, and coordinator-mediated task aggregation.
  - STM matches representative baselines on completion quality and token use while incurring **higher execution latency**.
- **Why interesting:** Quantifies the coordination tax that offsets naive multi-agent parallelism.

### Isolating Perception for Multi-View Planning under Occlusion-Induced Partial Observability
- **arXiv:** [2611.19179](https://arxiv.org/abs/2611.19179) (cs.CL, cs.AI, cs.CV; submitted 2026-11-14; EACL 2027)
- **Authors:** Kevin Nguyen, Ceyhun Efe Kayan, Feng Liu, Li Zhang
- **Key contributions:**
  - Introduces **BW-PO** (Blocksworld under partial observability), a controlled benchmark that reduces existing VLM planners and formalizers to near-zero performance.
  - Proposes **VLM-as-perceiver**: restrict the VLM to local perception and delegate cross-view evidence reconciliation and planning to external solvers.
  - Raises plan success from 1%→97% (Gemma-4-31B), 0%→95% (Qwen3.5-122B-A10B), and 3%→84% (Gemini-3.1-Pro) on model-specific challenging subsets.
- **Why interesting:** Separates two entangled bottlenecks — depth-ambiguity reconciliation and visual-extraction completeness — and shows delegation beats end-to-end VLM planning.

### LABEL: Literature Asymmetry between Efficacy and Limits in Drug Knowledge and Language Models
- **arXiv:** [2611.19166](https://arxiv.org/abs/2611.19166) (cs.AI, cs.IR; submitted 2026-11-14)
- **Authors:** S M Rayeed, Charles V. Stewart, Yao Ma
- **Key contributions:**
  - Measures a documentation gap across 574 drugs: reference prose names a drug's benefits about **twice as often** as its safety limits (within-drug odds ratio 2.19).
  - Qwen2.5 scaling from 0.5B→14B raises indication accuracy by 18.3 points while contraindication accuracy stays near random — but retrieved passages let models use safety facts as effectively as benefits.
  - **Routing safety questions to official FDA labels boosts accuracy by 15.8 points** when the label states the fact; recommends clinical AI route to regulatory labels/structured databases instead of general corpora.
- **Why interesting:** A clean IR/RAG result — retrieval source choice, not reasoning ability, drives a safety-critical capability gap.

## 2) CTR, Recommendation, Advertising & Retrieval

### TokenFormer V2: Breaking the Resolution-Complexity Dilemma in Unified Recommendation
- **arXiv:** [2611.19074](https://arxiv.org/abs/2611.19074) (cs.IR, cs.LG; submitted 2026-11-14)
- **Authors:** Kaihui Wu, Guoming Li, Liang Guo, Yifeng Zhou, Yuehong Hu, Junwei Pan, Zhixiang Feng, Chengguo Yin, Wenqi Fan, Haijie Gu, Jie Jiang
- **Affiliation:** Not stated in arXiv metadata; evaluated on the Tencent Advertising Algorithm Competition 2026 (TAAC 2026) benchmark and WeChat Channels advertising.
- **Key contributions:**
  - Decouples **representation resolution** from **interaction density** via a group-wise token layout, hierarchical group merging, and NS Fusion / Global Sync modules (a "local–global decomposition"), keeping every encoded event accessible to a Full-Resolution Readout module.
  - On TAAC 2026, top-ranking accuracy with **5.1× fewer FLOPs** than leading unified baselines; up to **+0.07 pp AUC** in billion-parameter WeChat Channels advertising evaluations.
  - Live online A/B against the production model: statistically significant **+2.33% GMV**.
- **Why interesting:** A battle-tested industrial recipe for full-resolution behavior modeling under tight serving budgets.

### CLEAR: Legible and Steerable Recommendation via Grounded Natural-Language Interests
- **arXiv:** [2611.19110](https://arxiv.org/abs/2611.19110) (cs.AI, cs.IR; submitted 2026-11-14)
- **Authors:** Qi Guo, Reza Mirghaderi, Iordanis Fostiropoulos, David Fan, Yuchen Liu, Shiliang Tang, Lukasz Korycki, Golnaz Ghasemiesfeh, et al. (large Meta author list)
- **Affiliation:** Meta (deployed on Instagram and Facebook; per abstract).
- **Key contributions:**
  - End-to-end recommender built around an **editable natural-language interest layer**: users can read interests, add/suppress them, and those states become authoritative preference state grounded in the user's own behavioral events.
  - The interest object doubles as a **serving address** — label and rewrites drive lexical retrieval, supporting events seed behavioral retrieval, and its projection queries an embedding index; a delivery controller replenishes underexposed interests.
  - ~88.5% of displayed interests rated accurate; a specialized 3B generator reaches 0.3967 mean-user F1@10 vs 0.3633 for Gemini 2.5 Pro; components have run in production for over a year.
- **Why interesting:** A rare deployed example of interpreter-able and user-controllable ranking, not just an offline fairness study. *Cross-referenced: also curated in today's `arxiv-ai-search.md`.*

### Label-Free Detection of Structural Bias in LLM-Based Recommender Systems via Randomized Paraphrasing: The Case of Verbosity
- **arXiv:** [2611.18878](https://arxiv.org/abs/2611.18878) (cs.IR, cs.AI; submitted 2026-11-13)
- **Authors:** Carlos Peláez-González, David Herrera-Poyatos, Francisco Herrera, Andrés Herrera-Poyatos
- **Key contributions:**
  - **Label-free audit framework**: rewrite candidate descriptions with randomly assigned paraphrasers in random order; prove that an invariant recommender selects each paraphraser with equal probability, yielding a statistical test that needs no relevance labels.
  - Apply to verbosity bias on 20,000 product queries and 9 LLMs from 5 families: after controlling for relevance signals, description length raises selection odds by **up to 38% per standard deviation** in all nine models.
  - Relevance remains the primary driver; verbosity is a consistent secondary signal. Provides an auditing protocol with cost/sample-size guidance for black-box shopping assistants.
- **Why interesting:** Gives practitioners a practical, annotation-free way to audit deployed LLM recommenders for surface-form bias.

### Advancing Quantization for R&R Models with Microscaling Formats
- **arXiv:** [2611.17501](https://arxiv.org/abs/2611.17501) (cs.AI; submitted 2026-11-12)
- **Authors:** Yavuz Yetim, Bor-Yiing Su, Zhe Wang, Arthur Liu, Pranav Sharma, Ying Wang, Randy Shuai, Luke Pfister, Ruichao Xiao, Bill Zhao, et al. (AMD author list)
- **Key contributions:**
  - Addresses the strict production launch bar for recommendation & ranking (R&R) models: quality must stay within **0.01% Normalized Entropy** of an FP16/FP32 baseline — far tighter than typical LLM quantization tolerance.
  - Reports the **first native MXFP6 GEMM speedups** (both weights and activations at 6-bit) without quality loss, with selective application to stay under the NE threshold; MXFP8 is a viable alternative to row-wise FP8.
  - On two production ads ranking models (AMD MI350X): **1.33–1.55×** GEMM speedup for MXFP8 and **1.73–1.99×** for MXFP6 (up to 2.90× on individual layers); end-to-end throughput gains of 1.5–5.3% (Model A) and 7.6–14.3% (Model B) over FP8 configurations.
- **Why interesting:** Concrete low-precision wins in the ads-ranking regime where accuracy budgets are an order of magnitude tighter than LLM serving.

### LMEG-Doc: Layout-Grounded Multi-View Evidence Graphs for Multimodal Long-Document Retrieval
- **arXiv:** [2611.18901](https://arxiv.org/abs/2611.18901) (cs.IR; submitted 2026-11-13)
- **Authors:** Changcheng Fu, Xiao Liu, Qi Yu, Yage Wang, Derek Young, Giri Iyengar
- **Key contributions:**
  - Builds an **evidence graph** over document elements capturing structural/contextual relations, with Cross-Page Relation Refinement (CRR) using VLM verification to connect evidence across distant pages.
  - Combines multimodal retrieval signals with graph-guided relevance propagation at layout and page levels, recovering complementary figures/tables that individual-similarity ranking misses.
  - Improves retrieval on MMDocIR, DocScope, and FinRAGBench-V; augmenting QA pipelines with retrieved evidence raises answer accuracy by **7.6% (DocScope)** and **15.8% (FinRAGBench-V)**.
- **Why interesting:** Shows relationship-aware retrieval beats similarity-only ranking when evidence is distributed across a long multimodal document.

## Notes and limitations

- **Freshness:** Strict "last 24 hours" (2026-11-16 02:20 → 2026-11-17 02:20 UTC) yielded only the cs.IR RSS batch of 2026-11-13 submissions, all already summarized in sibling reports. This brief prioritizes the **newest 2026-11-14 submissions** surfaced by the API plus two highly relevant 11-13/11-12 items new to the wiki. IDs ~2611.19xxx are the latest visible at query time; no 2026-11-15/16/17 announcement block was yet visible.
- **Dedup:** Every ID was checked against all `wiki/synthesis/**` reports; all are new except CLEAR (2611.19110), which is explicitly cross-referenced to today's `arxiv-ai-search.md`.
- **Method:** arXiv Export API category and keyword queries (cs.AI/cs.LG/cs.CL/cs.IR + CTR/advertising keywords), sorted by submission date, plus the cs.IR RSS feed; title/abstract screening only, no full-text quality review.
- **Attribution:** Affiliations are included only where stated in arXiv metadata or the abstract (Meta for CLEAR; TAAC/WeChat Channels context for TokenFormer V2; AMD author list for the quantization paper); otherwise marked unspecified.
- **Metrics:** All reported numbers (GMV, AUC, FLOPs, token savings, speedups, etc.) are author-reported and not independently reproduced. Benchmarks with known evaluation sensitivity (e.g., LoCoMo) are flagged inline.
