---
title: "arXiv Paper Check — AI & CTR (2026-11-18)"
type: synthesis
created: 2026-11-18
updated: 2026-11-18
sources:
  - https://export.arxiv.org/api/query?search_query=cat:cs.IR&sortBy=submittedDate&sortOrder=descending&max_results=70
  - https://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL&sortBy=submittedDate&sortOrder=descending&max_results=80
  - https://export.arxiv.org/api/query?search_query=all:%22click-through+rate%22+OR+all:%22CTR+prediction%22+OR+all:%22click+through%22+OR+all:%22advertising%22&sortBy=submittedDate&sortOrder=descending&max_results=60
  - https://export.arxiv.org/api/query?search_query=all:%22recommendation%22+OR+all:%22recommender%22+OR+all:%22generative+retrieval%22+OR+all:%22ranking%22&sortBy=submittedDate&sortOrder=descending&max_results=60
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
  - agent-memory
  - personalization
  - llm
  - daily-digest
---

# arXiv Paper Check — AI & CTR (2026-11-18)

> **Window note:** Checked **2026-11-18 02:21 UTC**. The strict last-24-hour window (2026-11-17 02:21 → 2026-11-18 02:21 UTC) is satisfiable this run: the newest announcement block (`cs.IR` RSS, items dated Tue 2026-11-17 00:00 -0500 / 05:00 UTC, feed built 08:26 UTC) falls inside it and carries **2026-11-16** submissions. The arXiv API additionally surfaces even fresher **2026-11-17** submissions (IDs ~2611.22xxx) that are not yet in the RSS block. This brief curates the newest **2026-11-16 / 11-17** batch (plus one adjacent 11-15 ads/ROI paper). Every ID below was checked against all `wiki/synthesis/**` reports and is **new to the wiki**; no overlap with today's sibling `arxiv-daily.md`, which covers a different set of 11-14…11-17 papers. All results and metrics are **author-reported**.

## Highlights

| Area | Pick | Why it matters |
|------|------|----------------|
| Rec / Decoding | **CG2R** (2611.22163) | Puts a learned semantic-cluster prior directly into the item scoring rule — defined even for cold-start users — and serves in milliseconds. |
| Retrieval / Ads | **SIMQ** (2611.22079) | One CPU-only graph index for ColBERT-style multi-vector retrieval; integrated into Ant Group's open-source VSAG library. |
| IR / LLM Ranking | **Evidence Diet** (2611.20837) | Shows LLM rankers are sensitive to *which* candidate gets *which* graph evidence: swapping intact count pairs drops NDCG@5 by 4 points. |
| Shopping / CTR | **Product follow-through** (2611.20378) | Links AI-assistant chats to later retailer browsing: shoppers reach the named product, but 89% of visits carry no referral signal. |
| AI / Agents | **RAG in a Trenchcoat** (2611.22179) | A deliberately minimal RAG memory matches SOTA on standard benchmarks — but adversarial probes show no memory design wins universally. |
| AI / Sampling | **Long-context generation** (2611.22148) | At temperature 2, `top-nsigma` resolves 46–62/100 coding issues where `top-p` resolves 0 — a sampler, not a training, fix. |

## 1) CTR, Recommendation, Advertising & Retrieval

### Cluster-Guided Decoding with Trust-Region Constraints for Personalized Recommendation
- **arXiv:** [2611.22163](https://arxiv.org/abs/2611.22163) (cs.IR; submitted 2026-11-17)
- **Authors:** Gezheng Wen, Chao Shen, Raviteja Anantha, Tan Shen Cliff Chung, Layne C. Price
- **Key contributions:**
  - Proposes **CG2R (Cluster-Guided Generative Reconstruction)**: learns a hierarchy of semantic clusters and adds a **cluster-level prior directly to the item scoring rule**, rather than using clusters only for candidate pre-selection.
  - The prior is assembled from cluster centroids rather than per-item statistics, so it remains **defined for cold-start users** with no history; trust-region constraints keep the cluster steer controlled.
  - On three benchmarks it beats classical, neural, and LLM-based baselines on Recall and nDCG, with **larger gains on sparser catalogs**, and serves in milliseconds (low-latency first-stage retrieval).
- **Why interesting:** A rare design where the learned cluster structure shapes ranking itself and degrades gracefully as data thins out.

### SIMQ: A Single Graph-based Index for Multi-Vector Query
- **arXiv:** [2611.22079](https://arxiv.org/abs/2611.22079) (cs.IR, cs.DB; submitted 2026-11-17)
- **Authors:** Yifan Lu, Jiabao Jin, Xiaoyao Zhong, Peng Cheng, Xiangyu Wang, Haotian Li, Hua Chen, Junqing Chen, Wei Xi, Heng Tao Shen
- **Key contributions:**
  - Bridges single-vector graph indices and multi-vector (ColBERT/MaxSim) retrieval via **data-aware sampling-based clustering** and **per-token graph navigation** — no per-query interaction matrix and no GPU-accelerated clustering (the two bottlenecks of prior approaches).
  - Builds one graph over cluster centroids independently of PLAID's residual representation; theory shows data-aware partitioning has smaller expected approximation error than data-oblivious partitioning under a manifold assumption.
  - **SIMQ+** adds count-based scoring and a dynamic candidate set for robustness; evaluated on five benchmarks (recall, throughput, construction time), primarily on CPU. **Integrated into VSAG**, Ant Group's open-source vector search library.
- **Why interesting:** Makes multi-vector retrieval practical on CPU with a single index — directly relevant to large-scale ads/recall stages.

### Evidence Diet: When Graph Evidence Helps LLMs Rank Competing Candidates
- **arXiv:** [2611.20837](https://arxiv.org/abs/2611.20837) (cs.IR, cs.AI; submitted 2026-11-16)
- **Authors:** Yuchong Hu, Zhao Zhang, Ziyao Zhao, Haoyu Wang, Jing Xiao
- **Key contributions:**
  - Studies how LLM rankers use collaborative graph evidence on Amazon Books and MovieTV: **swapping user-level evidence degrades ranking**, while matched item substitutions barely matter — an attribution effect.
  - Adding candidate-level graph records to history improves NDCG@5 by **+2.28 (Books) / +2.54 (MovieTV)**; numerical counts in history score outperform presenting them as text.
  - Exchanging intact count pairs among supported candidates (preserving support and token length) still **lowers NDCG@5 by 4.06 / 3.26 points**; a frozen test on 274 unused users confirms correct evidence→candidate assignment raises pairwise accuracy by **+6.07 pp** (95% CI [4.18, 8.00]).
- **Why interesting:** A controlled warning that "more evidence" is not enough — which candidate receives which evidence changes LLM ranking outcomes.

### Straight to the Product: What Online Retailers Miss When Shoppers Ask AI First
- **arXiv:** [2611.20378](https://arxiv.org/abs/2611.20378) (cs.IR, cs.CY, cs.HC; submitted 2026-11-16)
- **Authors:** Michael Iannelli, Alan Ai
- **Key contributions:**
  - Links the same users' AI-assistant conversations to later browsing at **20 large online retailers**: among recent non-visitors, visits to the assistant-named product within a day rise from 0.02 to **2.07 per 100 answers**; on days with a product-page visit, 44% show a product from the user's own answer vs 1.5% for a matched answer given to someone else.
  - **89% of visits carry no referral signal** and 54% follow a web search (the same share as usual visits); when a search precedes the first visit it names the answer's product 28% of the time (1% in earlier weeks) — "the search box as an address bar."
  - Proposes **product follow-through** (share of answers followed by a visit to the named product) as a referral-free way to evaluate shopping assistants and agents.
- **Why interesting:** Quantifies the real downstream CTR-like behavior AI shopping answers drive and why affiliate/referral logs miss most of it.

### Thinking Harder Doesn't Lead to Better Choices: Reasoning Effort in LLM Shopping Agents
- **arXiv:** [2611.22033](https://arxiv.org/abs/2611.22033) (cs.AI, cs.CL, cs.CY, cs.HC, econ.GN; submitted 2026-11-17)
- **Authors:** Adi Krishnamoorthy, X. Y. Han
- **Key contributions:**
  - Benchmarks **10 frontier models on three product-choice benchmarks** built from WebShop, Amazon SQID, and Wayfair WANDS.
  - Increasing reasoning effort does **not** significantly improve decision quality, but **does** significantly raise stated confidence — "extra thinking buys confidence rather than correctness"; most models are poorly calibrated at some effort levels.
  - Errors are strongly shared across models, and on tasks where many models err, a large number pick the **same wrong product**.
- **Why interesting:** Directly relevant to recommender/shopping agents — more test-time compute is not a substitute for product-selection accuracy or reliable confidence.

### UrbanROI: Causal Modeling for Regional ROI Forecasting under POI Entry
- **arXiv:** [2611.20180](https://arxiv.org/abs/2611.20180) (cs.LG; submitted 2026-11-15)
- **Authors:** Zhaoqi Zhang, Miao Xie, Linyou Cai, Qianlong Xie, Xingxing Wang, Siqiang Luo, Gao Cong
- **Key contributions:**
  - Defines **regional ROI forecasting under POI entry**: predict a commercial region's future ROI trajectory after a new point of interest opens, modeling temporal evolution and competition-driven interactions.
  - UrbanROI uses an **Interaction-aware Regional Graph** (user request context + spatial proximity + request-level commercial signals) and constructs structurally aligned treatment/control graphs for factual vs counterfactual regional states.
  - On large real-world POI and advertising datasets it consistently beats strong baselines in post-entry ROI forecasting.
- **Why interesting:** Brings causal/interventional modeling to ad-budget allocation and merchant onboarding at the region level, beyond single-ad or single-merchant ROI.

## 2) AI — LLMs, Agents, Reasoning & Systems

### RAG in a Trenchcoat: When Minimal Memory Is Enough for Agentic Systems, and When It Isn't
- **arXiv:** [2611.22179](https://arxiv.org/abs/2611.22179) (cs.AI; submitted 2026-11-17)
- **Authors:** Jingyu Liu, Zongze Li, Zach Xu, Zhanhui Zhou, Tahseen Rabbani, Dawn Song, Ce Zhang
- **Key contributions:**
  - **BRIDGE**, a deliberately minimal RAG memory (chained observation notes, hybrid BM25+cosine retrieval, chronological rendering, one LLM call per ingest/query, ~5–7K reader tokens), reaches parity with prior SOTA on LongMemEval-S and BEAM and **beats the best memory baseline by 5.7–6.3 points** on EverMemBench.
  - Argues standard benchmarks score *what memory retrieves*, not what it enables an agent to do; introduces **five adversarial probes** where each query requires applying a remembered rule/pattern it never mentions.
  - Across 5 probes × 20 scenarios **no architecture wins universally**: atomic-fact extractors (LangMem) win rule application, BRIDGE's block summaries win pattern induction; a recall benchmark cannot see this gap.
- **Why interesting:** Reframes agent-memory evaluation around downstream action, with concrete evidence that benchmark parity hides design-specific failures.

### RegimeCouncil: Paired-Evidence Routing for Memory Conflict Governance in LLM Agents
- **arXiv:** [2611.22113](https://arxiv.org/abs/2611.22113) (cs.AI; submitted 2026-11-17)
- **Authors:** Qingcan Kang, Mingyang Liu, Shixiong Kai, Tao Zhong, Mingxuan Yuan
- **Key contributions:**
  - Formulates **memory conflict governance** as an online scope choice under hidden validity and delayed feedback — suppress a stale fact only locally (same fact) or globally (all facts) — and proves neither fixed policy suffices.
  - **RegimeCouncil** keeps both scopes as advisors, uses with-memory vs no-memory comparisons, and a Meta Governor that defaults local and switches to global only on a strictly positive utility margin (finite-time switching guarantee), with no LLM retraining.
  - On LongMemEval update streams plus TempLAMA/TAQA drift with Qwen3-30B-A3B and GPT-4o, it beats the better fixed policy by **+5.2–7.3 points** on disagreement episodes across all 30 held-out settings.
- **Why interesting:** A lightweight, theoretically grounded controller for a personalization failure mode (stale memory) that most agents handle with a hard-coded choice.

### Sample-efficient Personalization of LLM Alignment with Multidimensional User Preference Data
- **arXiv:** [2611.22210](https://arxiv.org/abs/2611.22210) (cs.LG; submitted 2026-11-17)
- **Authors:** Zhen-Yu Zhang, Jerry Huang, Gang Niu, Takashi Ishida, Masashi Sugiyama
- **Key contributions:**
  - **MPG-DPO** builds a **personalized preference cone** from low-cost multidimensional automated-verifier evaluations of a user's historical comparisons, then discards confidently dominated responses and selects the two most contested ones inside the cone.
  - Addresses a gap where active alignment methods quantify uncertainty from the LLM's view, which can differ from the user's (a pair uncertain to the model may already be ordered by the user's history).
  - Theory shows the fraction of queries spent on cone-dominated responses vanishes with high probability; experiments across LLM families beat strong contenders at matched query budgets.
- **Why interesting:** Makes online preference alignment sample-efficient *and* user-specific — a personalization angle usually absent from alignment work.

### When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based AI Agents
- **arXiv:** [2611.21577](https://arxiv.org/abs/2611.21577) (cs.CR, cs.AI; submitted 2026-11-16)
- **Authors:** Zeynab Anbiaee, Sajjad Dadkhah, Ali A. Ghorbani
- **Key contributions:**
  - Defines **tool-provider misbinding**: a request meant for a legitimate provider is resolved to an attacker-controlled tool, with no compromise of the host, LLM, legitimate server, or network — only another MCP server advertising chosen metadata.
  - Five LLM-based clients in a controlled MCP environment: exact-name collision + task-aligned description + compatible schema is the strongest failure combination, but authority-enhanced descriptions with compatible schema also cause wrong-provider execution without name collision.
  - Different models expose the weakness differently (attacker-controlled selection, clarification requests, unstable resolution).
- **Why interesting:** A supply-chain/security risk for any agent stack composing tools from multiple MCP servers — metadata is not identity.

### Long-Context Generation Is a Sampling Problem (When You Turn Up the Heat)
- **arXiv:** [2611.22148](https://arxiv.org/abs/2611.22148) (cs.AI, cs.CL; submitted 2026-11-17)
- **Authors:** Allen G. Roush, Minh Nhat Nguyen, Ravid Shwartz-Ziv, Judah Goldfeder, Sanjay Basu
- **Key contributions:**
  - Tests **29 open-weight models (1B–122B)** on ten benchmarks plus needle retrieval to 1M tokens: samplers that keep a small, steady candidate pool at high temperature preserve accuracy; those admitting low-probability tokens collapse.
  - At temperature 2, coding agents using `top-p`/`top-k`/`Top-H` resolve **0/100** GitHub issues while `top-nsigma` resolves **46–62** and wins every disagreement; across benchmarks `top-nsigma` keeps a median **100%** of its temperature-1 score vs **26%** for `top-p`.
  - Candidate-pool size predicts quality (Spearman −0.77 across 133 settings); freezing the pool at temperature 1 stops `Top-H`, `min-p`, and `p-less` from collapsing. Code and data released.
- **Why interesting:** A cheap inference-time fix to long-generation degradation that does not require retraining.

### What RL on Expert-Built Tasks Teaches Nemotron 3.5 Super
- **arXiv:** [2611.22161](https://arxiv.org/abs/2611.22161) (cs.LG, cs.AI, cs.CL, cs.SE; submitted 2026-11-17)
- **Authors:** Sushant Mehta, Edwin Chen
- **Key contributions:**
  - Post-trains **NVIDIA Nemotron 3.5 Super (120B total / 12B active)** with RL on five expert-built task sets (SWE, complex constraints, long-horizon tool use, charts, enterprise docs), each a fresh rank-32 LoRA with CISPO, no supervised stage.
  - Gains across 12 benchmarks range from **+4.5 (IFBench) to +13.8 points (GDP_pdf: 10.4%→24.2%)**; SWE-bench Pro V2 86.9%→92.1%, Terminal-Bench 2.1 63.9%→70.3%, AutomationBench 14.8%→27.5%, Chartography 39.4%→50.6%.
  - Side-by-side attempt analysis links gains to specific behaviors each adapter acquires (finding data/rules before acting, writing scratch tests, carrying earlier turns, measuring chart marks in code).
- **Why interesting:** An industrial-scale ablation showing single-skill RL adapters transfer and generalize across a broad benchmark suite.

## Notes and limitations

- **Freshness / window:** The strict 24h window was met via the Tue 2026-11-17 05:00 UTC cs.IR announcement block (built 08:26 UTC), which contains 2026-11-16 submissions; API queries surfaced additional 2026-11-17 submissions (IDs ~2611.22xxx) not yet announced. One adjacent 2026-11-15 ads/ROI paper (UrbanROI) is included for CTR coverage.
- **Dedup:** All 12 IDs were checked against every `wiki/synthesis/**` report and are new; no overlap with today's `arxiv-daily.md` (which covers a different 24-paper set). Duplicate check at query time returned 0 prior hits for every ID here.
- **Method:** arXiv Export API category + keyword queries (cs.IR / cs.AI / cs.LG / cs.CL + CTR/advertising/recommendation/ranking keywords, sorted by submission date) plus the cs.IR RSS feed; title/abstract screening only, no full-text quality review.
- **Attribution:** Affiliations were taken only where stated in the abstract/metadata (Ant Group for SIMQ via VSAG; NVIDIA for Nemotron 3.5 Super; deployment context for the Xiaohongshu/Taobao-style studies is not claimed here unless stated). Numbers are as reported by the authors and not independently reproduced.
- **Coverage gap:** Pure click-model / pCTR architecture papers were thin in this window; the CTR angle is covered by CG2R, SIMQ, Evidence Diet, product follow-through, shopping-agent reasoning, and UrbanROI.
