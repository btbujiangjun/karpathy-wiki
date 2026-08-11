---
title: arXiv Paper Check — AI & CTR (August 11, 2026)
type: synthesis
created: 2026-08-11
updated: 2026-08-11
sources: [arxiv-cs.AI, arxiv-cs.IR]
tags: [arxiv, daily-check, ai, ctr, recommendation, ads, ir, retrieval, moe, efficiency, world-models, agent-safety, llm, finance]
---

# arXiv Paper Check — AI & CTR (August 11, 2026)

> ⚠️ **No new arXiv batch in the last 24 hours.** The most recent announcement is still **Mon, Aug 10, 2026** (cs.AI 88 new / cs.IR 9 new; arXiv has no weekend announcements). That batch was already fully curated in the [arXiv Paper Check — August 10](../2026-08-10/arxiv-paper-check.md) (36 papers). The **Tue, Aug 11 batch lands tonight ~20:00 ET** (= 08:00 +08 on Aug 12).
>
> This report is therefore a **second-pass deep scan of the Mon Aug 10 batch**: it curates the ~60 cs.AI papers plus the cs.IR cross-lists / replacements that the Aug 10 report did **not** cover. **Every arXiv ID below is grep-verified absent from the wiki** before inclusion. No new sub-24h CTR/ads paper beyond the batch.

## 🔥 Highlights

### CTR, Recommendation, Advertising & IR

| Paper | Authors | Key Contribution |
|-------|---------|------------------|
| **SAGEO Arena** (2602.12187; *replacement*, **KDD 2026**) | Sunghwan Kim, Wooseok Jeong, Serin Kim, Sangam Lee, Dongha Lee | First **realistic end-to-end evaluation environment for Search-Augmented Generative Engine Optimization (SAGEO)**: a full generative-search pipeline over structurally rich web documents jointly targets SEO + GEO. Finds existing optimization approaches are **largely impractical under realistic conditions and can degrade retrieval/reranking**; structural information (schema markup) mitigates this, and effective SAGEO must be tailored per pipeline stage. |
| **Pre-Inference Routing** (2608.06607; cross-list cs.CL→cs.IR) | Sreerekha Rajendran | **Difficulty-predictive model routing for document field extraction**: predicts a document's extraction difficulty from cheap features (image quality, layout) and routes between a cheaper and a stronger extractor. Calibrated router **cuts cost 31–33% on receipts and 77% on degraded ad-buy forms** while staying within 0.02 F1 of always-large. Routing only helps when the cheap model fails predictably — main limit is the genre, not the router. |
| **DocMemo** (2608.07067; cross-list cs.AI→cs.IR) | Hanshu Yao, Janfeng Zhong, Niu Lian, Jinpeng Wang | **Memory-guided long-document evidence discovery**: tri-level retrieval state (Document Schema Memory, Page Belief Memory, Question Episodic Memory) refined through dynamic Bayesian page-belief updating with Thompson sampling + spatial proximity propagation + adaptive-granularity evidence access. **SOTA on 3 benchmarks**; fixes the static top-k commitment failure of single-round RAG. |
| **FinRank** (2608.07400) | Sasan Mansouri, Daniel Saad, Mark Wahrenburg, Manu Weissel, Fabian Woebbeking | **Evidence-first financial QA/retrieval benchmark over SEC 10-K/10-Q filings**: 1,185 manually-authored records over 22 companies with gold passages and **hand-curated provenance-sensitive hard negatives** (confusable passages within a filing, across periods, across firms). Even a 7B instruction-tuned embedder reaches only **44.8% Recall@10**; a finance-adapted embedder trails BM25 — evidence grounding, not answer accuracy, is the bottleneck. |
| **Accounting Graph Transformer** (2608.07037) | Shrutendra Harsola, Vignesh Subrahmaniam | **Multi-KPI financial forecasting for small businesses** (13 income/balance/cash-flow KPIs from 71 monthly ledger series, 12–24 month history): masked ledger tokens exchange info via typed attention over a fixed **accounting-relation graph**, fused with a gated 3-month recency path. 5.3M-param model beats LightGBM/TimeMixer/SOFTS on all 13 KPIs (MAE 0.6990 vs 0.7378) across 11,993 forecast origins — relevant to SME-lending / accounting-vertical ranking features. |

### LLM Architectures, MoE & Efficiency

| Paper | Authors | Key Contribution |
|-------|---------|------------------|
| **TEXAS** (2608.06396) | Guanzhi Deng, Haibo Wang, Kuan Wu, Xiangru Jian, Shing Yin Wong, Sichun Luo, Zhuoran Wang, Linqi Song | **Task-Expert-Aware Supervision for downstream MoE adaptation**: discovers task experts by comparing activations on base-model successes vs failures (correctness-conditioned, not just routing usage), then **upweights answer tokens in failed instances that activate these experts**. Best/tied-best in 17 of 18 settings across 3 MoE models, +1.3–1.5 pts over the strongest baseline — a cheap supervision lever for fine-tuning ad/rec MoE rankers. |
| **Policy-Masked Private Experts** (2608.06690) | Zhuoheng Huang, Mukesh Singh | **Auditable & reversible capability access control in sparse MoE**: freeze the pretrained MoE, train a *disjoint private expert branch*, and select public/private pools before top-k routing so an unauthorized request **executes no private expert**. Zero unauthorized executions across 64 adversarial scenarios / 96 deny events on Qwen3-30B-A3B & DeepSeek-V2-Lite; exact allow-deny-allow recovery; private branch improves tool use 5.0–21.3 pp while the public fingerprint stays unchanged. |
| **ReQuant** (2608.07019) | Yongge Ma, Guoan Wang, Feiyu Wang, Yaoming Li, Qian Zhang, Zihan Yan, Yinjun Han, Tong Yang | **Backprop-free fixed-grid discrete refinement for PTQ**: post-processing stage that iteratively revisits weight assignments on the original quantization grid, strictly reducing MSE. Plug-and-play atop any PTQ initializer — simple round-to-nearest can be refined to approach/surpass GPTAQ under the same format, with largest gains at low bit-widths. |

### World Models & Agentic Science

| Paper | Authors | Key Contribution |
|-------|---------|------------------|
| **TaskSense** (2608.06544) | SM Mazharul Islam, Manfred Huber | **Task-centric world models for visual control**: differentiable stochastic spatial attention (conditioned on the previous latent) enforces task relevance *before* latent encoding, with an inverse-dynamics auxiliary objective; the decoder reconstructs only attended regions. **Competitive on DeepMind Control Suite, consistently beats DreamerV3 on Distracting Control Suite** — targets the background-clutter failure mode world models face in real deployment. |
| **Surg-UniWorld** (2608.06770) | Rulin Zhou, Wanhao Liu, Guoheng Ma, Liangjin Shao, Qiujie Song, et al. | **Unified surgical world model with multimodal control experts**: a Hierarchical Surgical Anchor preserves scene identity/anatomy/interaction boundaries from first-frame appearance + masks; Anchor-Relative experts interpret edge/depth/optical-flow; a Multimodal Control Expert composes increments for a Wan2.2 video-diffusion backbone. Ships **Cholec80-SurgWAM** benchmark for controllable surgical video generation. |
| **CGMas** (2608.06694) | Joohee Choi, Junhyeong Lee, Seunghwa Ryu | **Multi-agent LLM framework automating coarse-grained (CG) molecular dynamics**: agents chain topology construction → equilibration → mapping → potential derivation (Boltzmann inversion) → validation from a natural-language polymer spec, with layered self-correction for unsaturated/heteroatom/polar polymers. Completed all 27 homopolymer/copolymer tasks, density within 5% in 22, **simulation time 38–88 min → 1 min**. |
| **MolBioKG** (2608.06713) | Yiming Zhang, Hikaru Shindo, Shuan Chen, Kaushalya Madhawa, Jun Jin Choong, Yuna Oikawa, Takashi Fujiwara, Keisuke Ozawa | **Grounding out-of-graph molecules in a biomedical KG** via multi-resolution structural anchoring: a 2.74M-molecule structural index bridges to a 9.6M-edge KG, so an unseen SMILES retrieves related entities and traverses biomedical neighborhoods without task-specific training. **Multi-hop Hits@10 0.585→0.876, out-of-graph target recall 0.145→0.269**, with traceable structural anchors + source-attributed evidence. |

### Agent Safety, Evaluation & Benchmarks

| Paper | Authors | Key Contribution |
|-------|---------|------------------|
| **StepJack** (2608.06477) | Zhuoxin Zhan, Akbar Rafiey, Avery Ma, Leila Pishdad, Layla El Asri (BorealisAI) | **Multi-step indirect prompt injection benchmark for computer-use agents**: decomposes an adversarial goal into innocuous-looking sub-steps distributed across a chain of pages along the agent's navigation path. On 480 examples, multi-step attacks raise ASR on 3 of 6 CUAs by up to **31.2 pts (GPT-5.4-mini: 41.7% single-step → 72.9% three-step)**; averaged ASR 31.3%→36.9%. New attack surface for agentic web automation. |
| **Do AI Personas Grow? / BFI-Adapt** (2608.06485) | Ming Wang, Peidong Wang, Xiaocui Yang, Daling Wang, Shi Feng, Fiona Fui-Hoon Nah, Ee-Peng Lim | **First benchmark for event-induced personality evolution in LLM agents** (11 major life events, Big Five anchored). PC-Agents shift at similar rates for event-trait pairs with/without documented human directions, magnitudes fall below human effect sizes, and **persona dispersion is compressed 3–4× vs human samples — agents simulate the *mean* of human personality dynamics but not its *shape***. |
| **CyberForge** (2608.06471) | Amine Lbath, Manan Suri, Aurelien Delaitre, Vadim Okun, Massih-Reza Amini, Ram D. Sriram, Dinesh Manocha | **Verified repository-level vulnerability injection for security-agent training**: injects validated bugs into real C/C++ projects (build must pass unit tests; PoV triggers only on injected build), producing **1,034 validated vulns across 80 projects / 63 weakness categories** with CVE-like edit locality. Fine-tuning on the corpus improves SEC-bench patch repair **+3.3 to +14.7 pts** in all 6 configs; a 31B student reaches its GPT-5.4-mini teacher (72.7% vs 74.0%). |
| **NxN E-valuation** (2608.06621) | Bin Wang, Yan Zhong | **E-value hypothesis certification without case-specific nulls**: samples serve as null hypotheses for one another, directly realizing a conditional randomization test (CRT) for hypotheses generated by LLM exploration systems — a universal improvement over LLM circular verification and held-out testing for sample-wise hypotheses. |
| **Automated item evaluation** (2608.06609) | Hotaka Maeda, Yikai Lu | **Predicting standardized-test item acceptance/rejection from item text + LLM critiques** (52,759 ELA/math items, 34% rejected): DeBERTa fusion model hits Accuracy .75 / AUC .80; math (F1 .73) ≫ ELA (F1 .51); struggles on bias/sensitivity flags — a practical triage tool with a fairness caveat. |

## 📦 Version & Cross-List Updates (same batch)

- **Netflix generative recommender** (2605.23312 **v2**) — now *RecSys '26* (20th ACM RecSys). Update to existing page: [netflix-generative-recommender-scaling](../../papers/recommendation/netflix-generative-recommender-scaling.md). v2 details 2M→1B-backbone scaling as a *production-transfer* problem (offset scaling-law fits as diagnostic, multi-token prediction for serving-latency alignment, semantic item towers for cold start).
- **SAGEO Arena** (2602.12187) — see table above; first appearance in the wiki (KDD 2026).
- **READ / Beyond Top-K** (2608.06305 v2) — replacement of the agentic document-retrieval paper already covered in [arXiv Daily Digest 08-07](../2026-08-07/arxiv-daily.md).
- **Two Tower theory** (2403.00802 v2) — theoretical treatment of two-tower recommenders (faster convergence via intrinsic input dimension).

## 📊 Summary

- **New batches in last 24h**: **none** (latest = Mon Aug 10, fully curated in the Aug 10 report).
- **This report**: 18 additional papers from the Mon Aug 10 batch, all grep-verified absent from the wiki: IR/Rec/Ads/Finance 5, MoE & Efficiency 3, World Models & Agentic Science 4, Agent Safety/Eval/Benchmarks 6; plus 4 version/cross-list updates.
- **Batch context**: cs.AI 88 new / cs.IR 9 new, IDs ~2608.06394–2608.07460.

## 🔑 Key Trends (this pass)

1. **CTR/ads surfaces keep moving toward grounded, auditable evidence.** FinRank shows financial retrieval's real bottleneck is evidence grounding (44.8% R@10 ceiling), Pre-Inference Routing makes per-document cost routing practical (77% cost cut on ad-buy forms), and SAGEO Arena exposes that search-engine-optimization methods fail under realistic generative-search pipelines.
2. **MoE becomes a control surface, not just an efficiency trick.** Policy-Masked Private Experts turns top-k routing into auditable capability access control; TEXAS repurposes routing behavior as a supervision signal for downstream adaptation — both directly transferable to ad/rec MoE rankers.
3. **World models + agentic science keep industrializing.** TaskSense attacks visual-distraction robustness, Surg-UniWorld brings multimodal world models to surgery (with a benchmark), and CGMas/MolBioKG push LLM agents into automated simulation and KG grounding.
4. **Agent security matures from guidance to benchmarks.** StepJack (multi-step prompt injection), CyberForge (verified vulnerability-injection training data), and BFI-Adapt (personality-evolution eval) each contribute a reusable benchmark for agent-safety research.

## Related Pages
- [arXiv Paper Check — AI & CTR (August 10, 2026)](../2026-08-10/arxiv-paper-check.md) — primary curation of this same batch (36 papers)
- [arXiv Daily Digest (August 10, 2026)](../2026-08-10/arxiv-daily.md) — breadth pass over cs.CL/cs.LG/cs.GT + cs.AI/cs.IR remainder
- [Conference Digest (August 10, 2026)](../2026-08-10/conference-digest.md) — KDD 2026 + big-company arXiv picks
- [netflix-generative-recommender-scaling](../../papers/recommendation/netflix-generative-recommender-scaling.md) — updated to RecSys '26 v2
