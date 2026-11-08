---
title: arXiv AI Search — Recent Papers (AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games)
type: synthesis
created: 2026-11-08
updated: 2026-11-08
sources:
  - https://arxiv.org/
  - http://export.arxiv.org/api/query
tags:
  - arxiv
  - ai
  - llm
  - agents
  - recommendation
  - generative-recommendation
  - semantic-ids
  - sequential-modeling
  - linear-attention
  - ctr
  - advertising
  - whole-page-ranking
  - auctions
  - game-ai
  - game-theory
  - mechanism-design
  - retrieval
  - daily-digest
---

# arXiv AI Search — Recent Papers (AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games)

**Date:** 2026-11-08
**Scope:** Recent arXiv submissions, primarily the **2026-11-05** announcement block (latest available at fetch time) and the preceding week (2026-10-27 → 2026-11-05), across AI, LLMs/agents, recommendation, generative retrieval, advertising, CTR/ranking, sequential modeling, games, and auction/mechanism design.
**Method:** 11 paced arXiv Export-API queries — categories `cs.AI`, `cs.IR`, `cs.LG`, `cs.CL`, `cs.GT`, `cs.MA` sorted by `submittedDate` descending, plus keyword sweeps for recommendation, CTR, advertising, sequential modeling, and games. **539 unique IDs** pooled after de-duplication; titles/abstracts screened; all 26 featured IDs were grep-checked against `wiki/` to flag overlap with same-day sibling digests.
**Affiliation note:** arXiv metadata for fresh submissions usually omits structured institution fields. Affiliations below are stated only where the abstract/comment makes them explicit; otherwise they are inferred from author lineage and marked *(tentative)*.

## Summary Statistics

| Scope | Value |
|---|---|
| Queries run | 11 (6 category + 5 topical sweeps) |
| Unique papers pooled | 539 |
| Latest submission block | 2026-11-05 (announced 2026-11-06) |
| Featured in full | 26 papers across 5 sections |
| Short runner-ups | 8 |
| Direct advertising / CTR / ranking papers | 6 featured (AdSteer, ads auxiliary supervision, dynamic click destinations, whole-page MIS, optimal re-ranking depth, autobidding complexity) |
| Recommendation / generative retrieval papers | 8 featured |
| Sequential-modeling / architecture papers | 3 featured |
| Games / game-theory / mechanism-design papers | 5 featured |

**Theme of the window:** a strong **recommendation-representation** cluster (semantic IDs vs soft prototypes, flow-based CF, data-efficient scaling laws, intent-aware GEO), a **production advertising/ranking** cluster (decoding-time native ads, auxiliary supervision for sparse CVR, post-click destination personalization, one-pass whole-page ranking), and a **sequence-architecture measurement** cluster that emphasizes honest efficiency accounting (backend-relative memory claims, second-moment routing, sparse linear-attention prefill).

---

## 1. LLMs, Agents & Reasoning

### 1.1 More Agents, More Reliable? System-Level Reliability of Multi-Agent LLMs (2611.07140)
- **Title**: More Agents, More Reliable? System-Level Reliability of Multi-Agent LLMs under Operational-Profile Uncertainty
- **Authors**: Burkay Tunçtürk, Koorosh Aslansefat, Yiannis Papadopoulos, Bao Nguyen
- **Institution/Company**: UK academic (Hull/York lineage) *(tentative)*
- **Date**: 2026-11-04 (cs.MA); submitted to IEEE Software Magazine
- **arXiv**: https://arxiv.org/abs/2611.07140
- **Abstract**: Teams increasingly compose software from cooperating LLM agents under the assumption that more agents buy more reliability, but average benchmark accuracy ignores both the deployed input mix and the rule that merges agent answers. The authors extend HIP-LLM (hierarchical imprecise-probability assessment of single LLMs) with a Bayesian network of the multi-agent system's failure logic. Agent failure-probability intervals propagate through the network — where the combining rule can itself fail — into a reliability envelope that shows which evidence is the binding constraint. In a regulated chemical-hazard statement-extraction pipeline, majority voting over three models protected against the weakest model but did not clearly beat the best one, and a voter failing on 5% of demands largely erased its advantage over the middle model.
- **Key Innovations**: (1) system-level reliability envelope for multi-agent LLM pipelines rather than single-model accuracy; (2) explicitly models failure of the answer-combining rule; (3) a negative/qualified result: more agents produce a more defensible reliability claim, not automatically a more reliable system.
- **Venue**: Preprint (IEEE Software submission).

### 1.2 Scaling Laws for Data-Constrained Dense Retrieval (2611.04979)
- **Title**: Scaling Laws For Data-Constrained Dense Retrieval
- **Authors**: Bowen Fu, Jingtao Zhan
- **Institution/Company**: Tsinghua University *(tentative)*
- **Date**: 2026-11-03 (cs.IR)
- **arXiv**: https://arxiv.org/abs/2611.04979
- **Abstract**: Dense retrievers are fine-tuned on limited supervised retrieval data and reused across many epochs, a regime that standard abundant-data scaling laws do not describe. The paper studies the **minimum achievable evaluation loss (MAEL)** under fixed model size and unique-data budget. Learning-rate choices change optimization trajectories but barely change MAEL; after rescaling the step axis, learning curves collapse across learning rates, and CKA shows MAEL checkpoints learn highly similar representations. Across 35 BERT-family retrievers fine-tuned on MS MARCO subsets, MAEL follows a simple **multiplicative power law** over non-embedding parameters and unique samples, beating additive formulations. The authors also derive a scaling law for the step at which MAEL is reached and show optimal weight decay tracks an approximately invariant EMA timescale. In the observed regime, scaling pretrained model size is ~**1.46×** as fine-tuning-compute-efficient as adding unique in-domain data.
- **Key Innovations**: (1) MAEL as the right target for data-constrained retrieval scaling; (2) multiplicative (not additive) scaling law over parameters × unique samples; (3) an explicit model-size vs data trade-off ratio for retrieval fine-tuning.
- **Venue**: Preprint.

### 1.3 Near-Zero Token Embeddings Silently Stall Training in Gated Sequence Models (2611.04449)
- **Title**: Near-Zero Token Embeddings Silently Stall Training in Gated Sequence Models
- **Authors**: Xin Liu, Boyuan Sun, Yuxin Wang, Haoran Song, Mingjian Zhao, Mengyu Liu
- **Institution/Company**: Not stated in arXiv metadata
- **Date**: 2026-11-03 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2611.04449
- **Abstract**: A survey of 291 open-weight repositories (280 distinct embedding tables) finds that **52.6% of untied gated/hybrid checkpoints** (20/38) contain reachable input embeddings with norms below 10⁻⁶, versus 0% of weight-tied models. Such rows arise when unseen rare/template tokens receive zero input gradients while AdamW weight decay shrinks untied embeddings. In gated sequence models (Mamba, Gated DeltaNet, xLSTM), a near-zero token can amplify input-embedding gradients by up to **35 orders of magnitude**; current-token readout factors (SiLU gates / linear queries) vanish, historical-state readout is suppressed, and Pre-RMSNorm can amplify backward gradients by up to 10³ per layer. Once a gradient entry exceeds 1.84×10¹⁹, FP32 global-norm clipping in PyTorch/HF Trainer/FSDP2 overflows to infinity and zeros the batch's gradients; in Telugu continual pretraining of Nemotron-3-Nano-4B this discards updates on ~20% of steps. Remedies: **GroupClip** (64-bit/rescaled input-embedding clipping) for released checkpoints, and **GateFloor** (SiLU(z)+δ) during pretraining.
- **Key Innovations**: (1) identifies a silent, widespread failure mode specific to untied gated/hybrid models; (2) traces it to gradient overflow in standard clipping; (3) two low-overhead fixes for checkpoints and pretraining.
- **Venue**: Preprint.

### 1.4 WISE: Agentic Whole-page Multimodal Search Experience Attribution (2611.06777)
- **Title**: WISE: An Agentic Framework for Whole-page Multimodal Search Experience Attribution
- **Authors**: Wenyi Xu, Renzhe Zhou, Songyang Li, Feiran Zhu, Ruoqi Zhao, Chenglei Dai, Xuanping Li, Kaiqiao Zhan, Jingwei Zhuo
- **Institution/Company**: Alibaba *(tentative — Jingwei Zhuo)*
- **Date**: 2026-11-04 (cs.IR)
- **arXiv**: https://arxiv.org/abs/2611.06777
- **Abstract**: Algorithm-driven services (search, recommendation, advertising) are multi-stage pipelines; post-deployment monitoring focuses on operational reliability, yet operationally healthy systems can still return poor-quality results. The paper formulates **System Quality Diagnosis (SQD)** — beyond detecting bad outcomes, attribute their causes across system components — and proposes **WISE**, an agentic framework that discovers user-facing issues and traces them to algorithmic components. **ReTrace** constructs evidence-consistent trajectory supervision; **Adaptive Harness-Policy Optimization (AHPO)** performs failure-guided optimization of both agent harness and model policy. **WISE-BENCH** combines user-facing evidence, internal pipeline traces, and expert diagnosis annotations. WISE reaches **75.20% end-to-end accuracy** on Qwen3.5-35B-A3B, with consistent gains across model scales, and supports production auditing, online QA, and relevance-model optimization.
- **Key Innovations**: (1) SQD task formulation for attributing quality failures to pipeline stages; (2) ReTrace + AHPO for reliable diagnostic trajectories; (3) a real-world multimodal search diagnosis benchmark and production deployment evidence.
- **Venue**: Preprint.

---

## 2. Recommendation & Generative Retrieval

### 2.1 SourceFlow: Collaborative Source Coupling for Flow-Based Recommendation (2611.04455)
- **Title**: SourceFlow: Collaborative Source Coupling for Flow-Based Recommendation
- **Authors**: Chenghao Wu, Yongqi Zhou, Jin Chen, Yifeng Zhou, Jinchang Zhu, Junwei Pan, Chao Zhou, Zhixiang Feng, Chengguo Yin, Menglin Yang
- **Institution/Company**: HKUST / industry collaboration *(tentative — Menglin Yang)*
- **Date**: 2026-11-03 (cs.IR)
- **arXiv**: https://arxiv.org/abs/2611.04455
- **Abstract**: Flow-based collaborative filtering learns a discrete path from a sampled source to the user's observed interaction history, enabling few-step inference, but existing methods sample each source independently from global item frequencies, giving the predictor no user-specific source cue. **SourceFlow** moves collaborative structure into the source distribution itself: **Neighborhood Coupling** constructs displaced binary sources by replacing historical items with unobserved collaborative alternatives; **Collaborative Consensus** refines replacement probabilities using evidence from other users who share observed items; **Stretched Restoration** retains replacements at late flow times so the model gets more chances to recover the originals. On five datasets it improves over competitive baselines, with a mean **+15.7% Recall@10** over the strongest flow-based baseline. Controlled experiments show gains vanish if sources are reassigned across users, confirming the coupling matters.
- **Key Innovations**: (1) source-distribution design rather than extra predictor conditioning for flow-based CF; (2) neighborhood + consensus collaborative replacement; (3) stretched restoration as a training-time recovery curriculum.
- **Venue**: Preprint (under review).

### 2.2 IDs That Mean Something: A Hands-On Tutorial on Semantic IDs (2611.04140)
- **Title**: IDs That Mean Something: A Hands-On Tutorial on Semantic IDs for Recommender Systems
- **Authors**: Roger Zhe Li, Aghiles Salah, Mete Sertkan, Changhong Jin, Yingjie Niu, Ruihai Dong, Barry Smyth
- **Institution/Company**: University College Dublin *(tentative — Smyth/Dong)*
- **Date**: 2026-11-03 (cs.IR); accepted to CIKM '26
- **arXiv**: https://arxiv.org/abs/2611.04140
- **Abstract**: Traditional recommenders use arbitrary integer IDs carrying no semantics, forcing models to learn representations purely from interactions, with exploding embedding tables and scenario-specific architectures as side effects. **Semantic IDs** encode content, hierarchy, and relationships directly into item identity, offering a principled way to compress large-scale semantic information into the ID and enabling native unification across modalities, domains, and tasks for both generative and discriminative recommenders. This tutorial traces the evolution from raw IDs to semantic IDs, reviews applications in multi-modality, cold-start, and cross-domain recommendation, and provides hands-on exercises for building/evaluating semantic IDs, training models, and exploring cross-domain transfer. It closes with open challenges including dynamic semantic IDs and multi-stakeholder utility.
- **Key Innovations**: (1) a consolidated framework/narrative for the semantic-ID shift; (2) practical build-and-evaluate exercises; (3) explicit open-problem list (dynamic SIDs, multi-stakeholder utility).
- **Venue**: CIKM 2026 tutorial.

### 2.3 Data-Efficient Scaling-Law Discovery for Recommendation Systems (2611.05643)
- **Title**: Data-Efficient Scaling-Law Discovery for Recommendation Systems via Coupled Hyperparameter Scaling
- **Authors**: John Martabano Landy, Louis C. Tiao, Yao Xuan, Luc Kien Hang, Rupinder P. Khandpur, Arvind M. Vepa, Srinidhi Raghavendran, Anirudh Agrawal, Xiaoyi Leo Liu, Jiang Liu, Peggy Yao, Alireza Vahdatpour, Djordje Gligorijevic
- **Institution/Company**: Meta (evaluated on Meta's ads ranking and retrieval system)
- **Date**: 2026-11-03 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2611.05643
- **Abstract**: Large ranking/recommendation models benefit from compute like LLMs and show broadly power-law scaling, but heterogeneous ranking architectures make scaling laws harder to derive. The paper introduces a **scaling layer** that groups primitive architecture parameters into semantically coherent groups and defines how they co-vary, inducing a low-dimensional hyper-hyperparameter space. **Axia** fits scaling-informed surrogates, selects configurations with a posterior-based acquisition criterion, and returns a Pareto frontier for per-model operating points, replacing exhaustive sweeps with a few informative runs. A fleet-level evaluation protocol makes refinements measurable. Across **34 model iterations in two development cycles on Meta's ads ranking and retrieval system**, the workflow yields a mean **0.66% offline normalized-entropy improvement** and **0.36% cumulative online lift**.
- **Key Innovations**: (1) scaling layer for heterogeneous ranking architectures; (2) data-efficient Bayesian acquisition over scaling surrogates; (3) fleet-level protocol + production evidence on Meta ads.
- **Venue**: Preprint.

### 2.4 Item Representations Matter: Hard Semantic IDs vs Soft Prototype Mixtures (2611.05799)
- **Title**: Item Representations Matter: Bridging Hard Semantic IDs and Soft Prototype Mixtures for Generative Retrieval
- **Authors**: Vicente Balmaseda, Dongqi Fu, Jiarui Feng, Ren Chen, Hanqing Zeng, Tianxin Wei, Yinglong Xia, Tianbao Yang, Hong Li
- **Institution/Company**: Amazon / UIUC *(tentative — Yinglong Xia, Dongqi Fu)*
- **Date**: 2026-11-04 (cs.IR)
- **arXiv**: https://arxiv.org/abs/2611.05799
- **Abstract**: Generative retrieval predicts the next item either as discrete semantic-ID codes or as a continuous vector. Hard SIDs share parameters and pretrained semantic structure but discard information during quantization; continuous models avoid quantization but use flat lookup tables without parameter tying. **CAP-Mix** represents each item as a **soft mixture of shared prototypes plus an item-specific vector**, trained jointly and kept soft at inference. Pretrained information is optional: SID responsibilities can initialize the assignment prior, and a content embedding can initialize the item vector without changing the initial flat table. On three datasets, CAP-Mix improves over a flat table on two sparse Amazon datasets and slightly on Steam without pretrained information; given only an offline SID it beats a hard table from the same tokenizer by **4.45–14.90% HR@5**, and averaged over six benchmarks it improves HR@5/NDCG@5 by **6.9%/13.6%** relative to the best baseline while delivering **1.4–161×** the inference throughput of discrete baselines.
- **Key Innovations**: (1) soft prototype mixtures as a middle ground between hard SIDs and flat embeddings; (2) optional SID/content initialization; (3) large throughput advantage over discrete generative retrieval.
- **Venue**: Preprint.

### 2.5 Generative Learning on Dynamic Text-Attributed Graphs (2611.06458)
- **Title**: Generative Learning on Dynamic Text-Attributed Graphs
- **Authors**: Zhenyu Yang, Yuhong Chen, Binli Luo, Xiaodong Li, Xiaolin Hu, Hui Li, Jintang Li
- **Institution/Company**: Sun Yat-sen University *(tentative — Jintang Li)*
- **Date**: 2026-11-04 (cs.SI)
- **arXiv**: https://arxiv.org/abs/2611.06458
- **Abstract**: Dynamic text-attributed graphs model evolving interactions with rich text, but future-link prediction is difficult for nodes with little history or entirely new targets. The paper proposes a generative framework that represents nodes with compact **semantic identifiers (SIDs) learned from text** and autoregressively predicts a target SID conditioned on the source SID, recent interaction events, and relative time gaps. A lightweight structural calibration adds repetition, co-occurrence, and popularity signals. At inference, the query context is encoded once and SID likelihoods are reused to rank prescribed candidates, giving a candidate-efficient interface. On nine datasets it is broadly competitive across domains/graph densities; source-side inductive tests show text-derived SIDs help when the test source has no observed history, and two recommendation case studies evaluate new-user adaptation and first-arrival item ranking.
- **Key Innovations**: (1) text-derived SIDs for dynamic text-attributed link prediction; (2) candidate-efficient one-encode/reuse-likelihood inference; (3) inductive evaluations for cold sources and new items.
- **Venue**: Preprint.

### 2.6 Generative Retrieval under Real-Time Supply Constraints in Local Commerce (2611.06323)
- **Title**: Generative Retrieval under Real-Time Supply Constraints in Local Commerce
- **Authors**: Shaopeng Liang, Biao Zhang, Hongzhen Ye, Zeyang Hou, Ma Jiang, Jintao Tu, Yunxi Huang, Zhijia Fang, Jianqiang Cao, Junxue Rao, Jia Jia
- **Institution/Company**: Local-commerce platform (Meituan lineage) *(tentative)*
- **Date**: 2026-11-04 (cs.IR)
- **arXiv**: https://arxiv.org/abs/2611.06323
- **Abstract**: Generative retrieval predicts semantic identifiers for candidate entities, but in local retail/food delivery a catalog-valid identifier may be **infeasible for a specific user at a specific time** because location, weather, and traffic reshape supply. Post-generation filtering wastes beam capacity and inference. The paper studies retrieval over an explicitly materialized request-time supply snapshot and proposes **RTP-LLM**: eligible residual-quantization identifiers are compiled into a compressed sparse-row prefix index, CPU compilation overlaps model prefill, and the uploaded index is shared across beams; legal expansions retain original-model log probabilities and constraint states follow selected beam parents. It formalizes **snapshot-relative identifier validity** versus entity eligibility and freshness. A matched-beam daily-constraint case reduces filtered merchants from **170/299 to 29/299**; a different-host comparison reports a **0.6 ms** service-side latency increment.
- **Key Innovations**: (1) request-time supply snapshot as a first-class retrieval constraint; (2) prefix-index compilation overlapped with prefill and shared across beams; (3) formal distinction between snapshot validity, entity eligibility, and freshness.
- **Venue**: Preprint.

### 2.7 τ-Rec-Books: Disclosure-Controlled Benchmark for Requirement Elicitation (2611.04459)
- **Title**: τ-Rec-Books: A Disclosure-Controlled Benchmark for Requirement Elicitation in Agentic Recommender Systems
- **Authors**: Bharath Sivaram Narasimhan, Karthik R. Narasimhan
- **Institution/Company**: Independent/academic *(tentative)*
- **Date**: 2026-11-03 (cs.IR); submitted to ECIR 2027 (Resource Track)
- **arXiv**: https://arxiv.org/abs/2611.04459
- **Abstract**: Conversational recommenders must progressively discover a user's needs before recommending. τ-Rec-Books holds each request fixed and varies only **when** the user reveals requirements: all at the start (volunteer), one at the start and the rest when asked (mixed), or some never (hidden). A hidden requirement can only be found by proposing books and inferring it from accept/reject verdicts. The benchmark generates **450 tasks over 20,000 Wikidata books**, uses a rule-based simulated user, and scores against catalog metadata without an LLM judge. Across four agents and two interfaces, success falls from **0.975 (volunteer) to 0.756 (mixed) and 0.283 (hidden)**. Mixed tasks fail mainly because agents do not ask; when told to ask, every agent reaches ≥0.931. On hidden tasks most failures come from recommending a book never proposed; when told to propose first, agents only match a popularity baseline and stay below a rejection-based requirement-elimination baseline.
- **Key Innovations**: (1) disclosure-controlled elicitation benchmark; (2) LLM-judge-free scoring against catalog metadata; (3) clean diagnosis of "did not ask" vs "did not propose" failures.
- **Venue**: ECIR 2027 resource submission (preprint).

### 2.8 IntentGEO: Intent-aware Generative Engine Optimization for Recommendation (2611.04225)
- **Title**: IntentGEO: Intent-aware Generative Engine Optimization for Recommendation
- **Authors**: Runlin Lei, Shiqi Zhang, Xiaokui Xiao, Zhewei Wei
- **Institution/Company**: Renmin University of China / Peking University *(tentative — Zhewei Wei, Xiaokui Xiao)*
- **Date**: 2026-11-03 (cs.IR)
- **arXiv**: https://arxiv.org/abs/2611.04225
- **Abstract**: LLMs increasingly shape recommendations, creating demand for **Generative Engine Optimization (GEO)** to improve item visibility in generated responses. Existing GEO is content-centric and optimizes for general queries, but a shared item description serves users with different needs, so visibility gains depend on request intent. **IntentGEO** evaluates shared rewrites across need specificity and decision progression. Revisiting existing GEO methods, the authors find visibility gains vary by intent and that learning-based prompt optimization can underperform its handwritten seed: updates drift from explicit recommendation instructions toward generic promotional tactics. **AMO (Anchored Meta-Optimization)** keeps recommendation instructions in a fixed core while learning appended strategies from citation feedback. Across four domains and ten intent states, AMO improves average citation-rank gain by **35%** over the strongest prior learning-based baseline and leads on nine states; it also transfers to an agentic recommendation pipeline and, after adaptation, to the closed-source **Doubao** assistant.
- **Key Innovations**: (1) intent as a first-class dimension of GEO evaluation; (2) diagnoses and fixes prompt drift via anchored optimization; (3) cross-domain + deployed-assistant transfer.
- **Venue**: Preprint.

---

## 3. Advertising, CTR & Ranking

### 3.1 AdSteer: Native Advertising in LLM Generation (2611.04147)
- **Title**: AdSteer: Native Advertising in Large Language Model Generation
- **Authors**: Shuhang Lin, Chuhao Zhou, Zhenyu Wang, Xiao Lin, Changsheng Wang, Saibo Geng, Dimitris N. Metaxas
- **Institution/Company**: Rutgers University *(tentative — Metaxas)*
- **Date**: 2026-11-03 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2611.04147
- **Abstract**: Rising LLM serving costs motivate alternative monetization, and native advertising can create value by aligning user intent with merchant offerings. Existing integrations rely on prompt-level injection, multi-pass rewriting, or fine-tuning, which can hurt response quality or add compute. **AdSteer** is a **lightweight decoding-time** advertising framework that adaptively adjusts token probabilities to integrate contextually appropriate ads, calibrating both the strength and duration of advertising influence so sponsored content remains a natural part of the response. On GEM-Bench across three scenarios, AdSteer improves overall score by **14.1%** over the strongest baselines while using **22.5% fewer total tokens** than rewrite-based methods.
- **Key Innovations**: (1) decoding-time ad steering instead of prompting/rewriting/fine-tuning; (2) calibrated influence strength and duration; (3) quality gain plus token savings.
- **Venue**: Preprint.

### 3.2 Improving Ads Ranking Models with Auxiliary Supervision (2611.01280)
- **Title**: Improving Ads Ranking Models with Auxiliary Supervision: Techniques and Insights
- **Authors**: Nikhil Bhale, Apurva Pathak, SaiSujithKumarReddy MarapaReddy, Xiao Yin, Prateek Bhansali
- **Institution/Company**: Large advertising platform (Yahoo lineage) *(tentative)*
- **Date**: 2026-10-31 (cs.IR); accepted to IEEE ICDM WAIP 2026
- **arXiv**: https://arxiv.org/abs/2611.01280
- **Abstract**: Post-click conversion rate (CVR) prediction is central to personalized ad delivery, but conversion labels are sparse or missing. This industry case study uses **auxiliary supervision from diverse user events and metadata signals** beyond conversions, plus modeling techniques to exploit them: **linearized labels** for improved auxiliary-signal precision, a **split architecture** for training-task decomposition, and **Label Combination (LaCo)** for robustly managing noisy auxiliary data. Empirical results show measurable ranking-model improvements, and the techniques are presented as reusable across recommendation systems and related domains.
- **Key Innovations**: (1) auxiliary-supervision taxonomy for sparse CVR; (2) linearized labels + split-task architecture; (3) LaCo noise-robust label combination, with production-style evidence.
- **Venue**: ICDM 2026 WAIP workshop.

### 3.3 Dynamic Click Destinations: Personalizing Post Ad-Click Landing (2611.01287)
- **Title**: Dynamic Click Destinations: Personalizing Post Ad-Click Landing Experiences
- **Authors**: Apurva Pathak, Yuya Shiraki, Iman Jenabzadeh, Nikhil Bhale, Yuwen Tan, Shashank Rangarajan, Amirmehdi Sharifzad
- **Institution/Company**: Large advertising platform (Yahoo lineage) *(tentative)*
- **Date**: 2026-10-31 (cs.IR); accepted to IEEE ICDM WAIP 2026
- **arXiv**: https://arxiv.org/abs/2611.01287
- **Abstract**: Apps monetizing outbound ad clicks have multiple post-click levers — which landing page, web vs app, native in-product surface vs external site. The optimal destination is heterogeneous across users, advertisers, placements, devices, and inferred intent, so static policies are suboptimal. **Dynamic Click Destinations (DCD)** selects a destination per eligible offsite click to maximize **Advertiser Value (AV)**, a value-weighted conversion outcome. The paper traces an evolution from post-conversion destination inference, to two-task destination-conditioned conversion prediction, to a **single-task policy** predicting which of two destinations is better, trained with A2C-inspired soft labels from a higher-capacity destination-conditioned critic. In a web-vs-app A/B case study at scale, per-click personalization beats static routing, with the single-task objective giving the largest gains.
- **Key Innovations**: (1) names post-ad-click destination as an under-explored conversion lever; (2) critic-derived soft-label single-task policy; (3) large-scale online A/B validation.
- **Venue**: ICDM 2026 WAIP workshop.

### 3.4 Towards Efficient Whole Page Ranking with One-Pass Inference (2611.05542)
- **Title**: Towards Efficient Whole Page Ranking with One-Pass Inference
- **Authors**: Qi Xu, Zhigang Hua, Zijie Lei, Yan Xie, Jizhe Zhang, Lynn Lu, Delun Du, Sha Hua, Ren Mao, Ke Pan, Haomin Yu, Sandeep Pandey, Luke Simon
- **Institution/Company**: Meta *(tentative — Sandeep Pandey, Luke Simon)*
- **Date**: 2026-11-03 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2611.05542
- **Abstract**: Whole-page ranking jointly optimizes ads and organic content under layout and business constraints. Non-autoregressive (NAR) approaches are efficient but score candidates independently of previously selected items, missing order-dependent interactions; autoregressive (AR) methods capture those dependencies but incur large inference overhead. **Multi-Item Scoring (MIS)** is a prefix-aware NAR-style framework that integrates global candidate interactions, localized prefix conditioning, and position-aware scoring in a shared representation. It computes reusable representations once per request and performs lightweight prefix-conditioned scoring during constrained beam search. On KuaiRand-1K and RL4RS, MIS approaches the generation quality of an AR CGA baseline with **4.07× / 3.54×** faster CPU decoding; in a randomized large-scale social-video platform evaluation it improves realization by **0.104%** and watch time by **0.058%** while cutting ranking-service CPU by **9.73%**.
- **Key Innovations**: (1) prefix-aware NAR that recovers AR order-dependence with one-pass representations; (2) constrained-beam scoring without repeated full-model inference; (3) production-level quality/efficiency trade-off evidence.
- **Venue**: Preprint.

### 3.5 Optimal Re-Ranking Depth (2611.05908)
- **Title**: Optimal Re-Ranking Depth
- **Authors**: Siqing Huo, Andrew Parry, Debasis Ganguly, Charles L. A. Clarke
- **Institution/Company**: University of Waterloo / University of Glasgow *(tentative — Clarke, Ganguly)*
- **Date**: 2026-11-04 (cs.IR)
- **arXiv**: https://arxiv.org/abs/2611.05908
- **Abstract**: Second-stage neural rankers typically use a fixed re-ranking depth, assuming effectiveness saturates with depth, though prior work suggests the optimum varies by query. Using **dense LLM-based relevance judgments**, the authors show many queries have a well-defined **per-query optimal re-ranking depth**, beyond which effectiveness stagnates or degrades. They formulate depth as a query-specific property and test whether it can be predicted from first-stage retrieval characteristics. Most standard query-performance-prediction (QPP) methods fail, but a predictor derived from **LLM-assessed first-stage ranking quality (IR-DCG@10)** can reduce average depth by up to **3×** while preserving effectiveness. Under oracle depth selection, effectiveness improves by more than **7%** while reducing depth by **5×** on MSMARCO DEV. Judgments, code, and artifacts are released.
- **Key Innovations**: (1) reframes re-ranking depth as a predictable query property; (2) IR-DCG@10 as a lightweight depth predictor; (3) LLM-judgment methodology that makes large-scale per-query analysis feasible.
- **Venue**: Preprint.

### 3.6 On the Complexity of Exact Autobidding Equilibria (2611.04475)
- **Title**: On the Complexity of Exact Autobidding Equilibria
- **Authors**: Yiyang Huang, Zhengyang Liu, Yonglei Yan
- **Institution/Company**: Academic *(tentative)*
- **Date**: 2026-11-03 (cs.GT)
- **arXiv**: https://arxiv.org/abs/2611.04475
- **Abstract**: Autobidding equilibria link advertisers' value multipliers or participation probabilities through aggregate budget and return-on-investment (ROI) constraints. The paper establishes the exact computational complexity of finding these equilibria across canonical settings: exact equilibrium computation is **FIXP-complete** for second-price ROI pacing, budget- or ROI-constrained generalized second-price (GSP) sponsored shopping, and second-price throttling. Approximating the equilibrium control vector in distance to a true equilibrium is **FIXPₐ-complete** when the target accuracy is part of the input.
- **Key Innovations**: (1) exact complexity classification for autobidding equilibria; (2) covers ROI pacing, GSP sponsored shopping, and throttling; (3) hardness of approximation as a function of target accuracy.
- **Venue**: Preprint (full version with appendices).

---

## 4. Sequential Modeling & Architecture

### 4.1 Attention, Dynamic Wave and Hybrid Sequence Mixers (2610.39854)
- **Title**: Attention, Dynamic Wave and Hybrid Sequence Mixers in Language Models
- **Authors**: Dmytro Babarytskyi, Oleksandr Babarytskyi
- **Institution/Company**: Independent *(tentative)*
- **Date**: 2026-10-29 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2610.39854
- **Abstract**: The paper formalizes a **Dynamic Wave** recurrent layer based on input-dependent exponential damping and cosine phase modulation, then evaluates three 10.94M-parameter configurations (Pure Transformer, Pure Wave, Hybrid Wave-Attention) on TinyStories up to 4096 tokens. The hybrid reaches the best perplexity (**5.95** vs 6.93 Transformer, 7.26 Pure Wave). The efficiency picture is governed by implementation more than architecture: against an **unfused** attention baseline, Pure Wave uses **78.7% less peak VRAM** at 4096 tokens (1404.3 MB vs 6601.6 MB), but against a **fused SDPA kernel** it has **no advantage** (1404.3 MB vs 1403.6 MB) and in training is **8.3% more expensive** than the Transformer. Hoisting elementwise terms out of the recurrence loop speeds the layer up **2.53×** without a custom kernel, cutting the latency gap from 2.48× to 1.12×. A hybrid stack inherits the cost of its more expensive mixer, matching Transformer peak VRAM within 0.1%.
- **Key Innovations**: (1) Dynamic Wave mixer with input-dependent damping/phase; (2) a careful backend-relative efficiency audit; (3) closed-form memory model predicting when attention overtakes vocabulary projection.
- **Venue**: Preprint.

### 4.2 MERLIN: Multi-State Linear Attention with Second-Order Routing (2610.37645)
- **Title**: Multi-State Linear Attention with Generalized Second-Order Routing
- **Authors**: Hee Seung Hwang, Sanghyuk Chun, Xindi Wu, Olga Russakovsky, Zhiwei Deng
- **Institution/Company**: Princeton / NAVER-KAIST *(tentative — Russakovsky, Chun)*
- **Date**: 2026-10-27 (cs.CL)
- **arXiv**: https://arxiv.org/abs/2610.37645
- **Abstract**: Multi-State Linear Attention (MSLA) splits context into segments and compresses each into its own memory state, but aggregates states using only the **mean alignment** between a query and each segment's keys, ignoring within-segment variance. **MERLIN (MomEnt Routing for multi-state LINear attention)** tracks the **first and second moments** of each segment's keys, letting a query recover both mean and variance of its alignment for content-aware per-state aggregation. On multi-state variants of **Gated DeltaNet-1.3B** and **Mamba-2-780M**, MERLIN consistently beats existing aggregation methods on long-context tasks: **+8.3% / +7.0%** on RULER needle-in-a-haystack and long-context QA, and **+13.5% / +12.0%** on LongBench subtasks — even outperforming baselines that consume **4× more memory**.
- **Key Innovations**: (1) second-moment (variance-aware) routing for MSLA; (2) simple, general augmentation of existing linear-attention models; (3) strong long-context gains at lower memory.
- **Venue**: Preprint.

### 4.3 SparseGDN: Chunk Sparse Linear Attention (2610.41420)
- **Title**: SparseGDN: Chunk Sparse in Linear Attention
- **Authors**: Jiedong Zhuang, Peng Zhao, Jialin Tang, Haoji Hu
- **Institution/Company**: Zhejiang University *(tentative)*
- **Date**: 2026-10-30 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2610.41420
- **Abstract**: Gated Delta Networks (GDNs) offer linear-time sequence modeling, but long-context prefill is expensive due to dense intra-chunk computation, recurrent-state updates, and intermediate-state storage. **SparseGDN** combines a structured intra-chunk approximation with input-dependent recurrent-event selection while still producing outputs for every token. A **block-adjacent solver** reduces local Delta-solve computation; a **dynamic selector** allocates recurrent-update budgets across head pairs. The GPU implementation materializes updates only for selected events and reconstructs token outputs from compact state snapshots and group-local interactions, reducing compute and memory traffic. On **Qwen3.5-4B / Qwen3.5-9B** over RULER tasks from 4K to 128K, retaining ~**29%** of recurrent events on average yields **1.50–1.94× GDN-core prefill speedups** over native FLA kernels, including online selection overhead.
- **Key Innovations**: (1) input-dependent sparse recurrent-event selection for GDNs; (2) block-adjacent solver + compact state snapshots; (3) hardware-aware prefill speedups at 128K context.
- **Venue**: Preprint.

---

## 5. Games, Game AI & Mechanism Design

### 5.1 LLM-based NPCs in Video Games: A Systematic Mapping Study (2611.05427)
- **Title**: LLM-based NPCs in Video Games: A Systematic Mapping Study
- **Authors**: Dilan Mian, Jeremy Bradbury, Yann-Gaël Guéhéneuc, Fabio Petrillo, Cristiano Politowski
- **Institution/Company**: Concordia University / UQAM *(tentative)*
- **Date**: 2026-11-02 (cs.SE); IEEE Transactions on Games (Early Access)
- **arXiv**: https://arxiv.org/abs/2611.05427
- **Abstract**: NPCs have long been driven by rule-based, pre-scripted systems; LLMs promise open conversation, adaptation, and emergent behavior, prompting academic and commercial experimentation without a unified picture of what has been built and at what cost. This systematic mapping study screens **377 papers** and analyzes **42** against one main and ten sub-questions across four thematic axes, giving the first quantitative characterization of component adoption, latency, safety coverage, and reproducibility. Short-term memory (**60%**) and world-state grounding (**69%**) are near-universal, while long-term memory (**31%**), reflection (**38%**), and retrieval-augmented generation (**14%**) remain rare; response times span **2.6–15 seconds**. The paper identifies six structural barriers to commercial adoption and offers evidence-based recommendations.
- **Key Innovations**: (1) first quantitative map of LLM-NPC research; (2) adoption/latency/safety/reproducibility statistics; (3) six concrete commercialization barriers + recommendations.
- **Venue**: IEEE Transactions on Games (Early Access).

### 5.2 Efficient Equilibrium Computation in Colonel Blotto Games (2611.05221)
- **Title**: Efficient Equilibrium Computation in Colonel Blotto Games
- **Authors**: Martin Bichler, Abheek Ghosh
- **Institution/Company**: Technical University of Munich *(tentative — Bichler)*
- **Date**: 2026-11-03 (cs.GT)
- **arXiv**: https://arxiv.org/abs/2611.05221
- **Abstract**: Colonel Blotto is a fundamental resource-allocation game: two players divide budgets across battlefields and the higher allocation wins each battlefield's value. Efficient equilibrium computation for the classical continuous version with arbitrary budgets and battlefield values (same for both players) had remained unresolved. The paper gives a **fully polynomial-time approximation scheme (FPTAS)** computing an ε-Nash equilibrium in time polynomial in input length and 1/ε, and nearly linear in input length for fixed ε. For sufficiently balanced budgets and battlefield values, it computes exact equilibria in **linear time**.
- **Key Innovations**: (1) resolves the long-open complexity of continuous Colonel Blotto equilibrium; (2) FPTAS with near-linear scaling for fixed accuracy; (3) exact linear-time special case for balanced instances.
- **Venue**: Preprint (75 pages).

### 5.3 KlaskTron: Open-Source Physical Adversarial Multi-Agent RL (2611.03138)
- **Title**: KlaskTron: An Open-Source Platform for Physical Adversarial Multi-Agent RL
- **Authors**: Aswin Ramachandran, Jona Schulz, Maurus Derungs, Carlo Angelini, Tobias Meier, Raffaello D'Andrea
- **Institution/Company**: ETH Zurich *(tentative — D'Andrea; IDSC ETH repository)*
- **Date**: 2026-11-02 (cs.RO)
- **arXiv**: https://arxiv.org/abs/2611.03138
- **Abstract**: Physical multi-agent RL progress is limited by accessible, standardized benchmarks: physical platforms are often expensive, facility-bound, or lack open designs. **KlaskTron** is an open-source, low-cost (**< $2,500**), desktop-scale robotic testbed for adversarial MARL based on the tabletop game KLASK. It uses dual CoreXY gantries with high-torque brushless motors for fast, precise manipulation and ships a complete ecosystem: CAD/BOM hardware, a GPU-native digital twin in **NVIDIA Isaac Lab**, and a validated sim-to-real baseline with a learned neural actuator model. The baseline enables **zero-shot policy transfer**, with trained agents exhibiting emergent adversarial behavior; all hardware, software, and RL assets are public.
- **Key Innovations**: (1) sub-$2,500 reproducible physical MARL testbed; (2) Isaac Lab digital twin + learned actuator model; (3) zero-shot sim-to-real adversarial policies.
- **Venue**: Preprint.

### 5.4 Regret Bounds for Profit Maximization in Bilateral Trade (2611.08173)
- **Title**: Regret Bounds for Profit Maximization in Bilateral Trade: Learning the Best Posted-Price Mechanism
- **Authors**: Johannes Brüstle, Simone Di Gregorio, Federico Fusco, Stefano Leonardi
- **Institution/Company**: Sapienza University of Rome / LUISS *(tentative)*
- **Date**: 2026-11-05 (cs.GT)
- **arXiv**: https://arxiv.org/abs/2611.08173
- **Abstract**: A profit-maximizing broker intermediates between a strategic seller and buyer with private valuations, proposing a price to each; trade occurs if both accept and profit is the buyer-price minus seller-price. Each round the learner observes only whether trade occurred and competes with the best fixed price pair in hindsight. For adversarial valuations, the paper gives a polynomial-time algorithm with **Õ(T^{2/3})** regret, nearly tight even for i.i.d. independent distributions and matching the one-sided pricing rate. Under i.i.d. valuations with the **monotone-hazard-rate (MHR)** property, it gives **Õ(√T)** regret via localized estimation plus a stochastic convex-bandit routine on the negative log expected profit. It also proves a separation: the minimax rate for regular distributions is **Õ(T^{3/5})**, unlike one-sided pricing's Õ(√T).
- **Key Innovations**: (1) near-tight two-sided pricing regret under bandit feedback; (2) MHR vs regular distribution separation; (3) localized estimation + convex bandits technique.
- **Venue**: Preprint.

### 5.5 Offline Learning of Reserve Prices from Censored Bids (2611.06067)
- **Title**: Offline Learning of Reserve Prices from Censored Bids
- **Authors**: Lavanya Marla, Yunzong Xu, Boxuan Zhou
- **Institution/Company**: University of Maryland / UIUC *(tentative — Marla)*
- **Date**: 2026-11-04 (cs.GT)
- **arXiv**: https://arxiv.org/abs/2611.06067
- **Abstract**: A seller wants to learn a reserve price for a second-price auction from censored historical bids: values below past reserves are unobserved, so even unlimited data may not reveal the revenue-maximizing reserve. Under a **monotone hazard rate (MHR)** assumption, the paper characterizes exactly when an optimal reserve is identified even if the value distribution is not — either revenue has not begun to fall at the lowest historical reserve, or the censored fraction is as large as MHR allows (pinning down the distribution). When identification fails, it derives the reserve minimizing worst-case revenue regret and shows this unique **minimax reserve** depends on only two observables: the censored fraction and the hazard just above the lowest historical reserve. Regret scales as **O(N^{-1/2})** when the optimum lies among observed bids, **O(N^{-1})** from the censored count alone in the pinned case, and **O(N^{-2/5})** in the nonidentifiable regime. Experiments use synthetic data and eBay bids.
- **Key Innovations**: (1) identifies when censored auction data suffices to learn an optimal reserve; (2) minimax reserve with a two-observable characterization; (3) regret bounds spanning identifiable and nonidentifiable regimes.
- **Venue**: Preprint (87 pages).

---

## Runner-Ups (brief)

| Paper | Authors | Institution | arXiv | Why relevant |
|---|---|---|---|---|
| Cold-Start Pricing of LLM Services under Two-Sided Learning | Zhicheng Du, Pinyan Lu, Keyu Wang, Zihe Wang, Xiang Yan, Chunxue Yang | Academic *(tentative)* | [2611.03199](https://arxiv.org/abs/2611.03199) | Pricing/mechanism design for LLM inference markets |
| On inverse aggregate network assignment games | Joseph Y. J. Chow | NYU *(tentative)* | [2611.03409](https://arxiv.org/abs/2611.03409) | Two-sided mobility-market estimation with rationing prices |
| QueryFlow: Multi-Hop Graph Retrieval with Adaptive Query Evolution | Manzong Huang, Chenyang Bu, Yi He, Jiapu Wang, Xindong Wu | Academic *(tentative)* | [2611.04625](https://arxiv.org/abs/2611.04625) | Adaptive multi-hop graph retrieval |
| Do Retrieval Ranking Models Capture Event Order? | Alon Eirew, Lidan Avisar, Kfir Bar, Ido Dagan | Academic *(tentative)* | [2611.04343](https://arxiv.org/abs/2611.04343) | Timeline-constrained retrieval / temporal ranking |
| Turbocharging PiPNN for Proximity and k-NN Graph Building | Tobias Rubel, Richard Wen, Guy Blelloch, Laxman Dhulipala, Lars Gottesbüren, Jakub Łącki | CMU / Google *(tentative)* | [2611.05690](https://arxiv.org/abs/2611.05690) | Scalable k-NN graph construction for retrieval |
| Trilemma: How Agents choose between Honesty, Confidentiality, and Task Completion | Johannes Taraz, Abhinav Kumar, Sahar Abdelnabi | Academic *(tentative)* | [2611.08312](https://arxiv.org/abs/2611.08312) | Agent safety / competing objectives |
| Take It From Here: Evaluating Coding Agents On Project Takeover | Dingxian Wang et al. | Industry *(tentative)* | [2611.07307](https://arxiv.org/abs/2611.07307) | Coding-agent takeover evaluation |
| Signed, Sealed, Leaked: Trust Beyond Signature for MCP Toolchains | Yichiet Aun et al. | Academic *(tentative)* | [2611.06585](https://arxiv.org/abs/2611.06585) | Agent toolchain security |

---

## Cross-cutting Observations

1. **Irreversible quantization is being softened, not abandoned.** CAP-Mix (2.4) keeps hard-SID semantics but replaces the hard bottleneck with soft prototype mixtures and recovers 4.45–14.90% HR@5 over a hard table at the same tokenizer. Semantic-ID tutorials (2.2) and text-derived SIDs (2.5) point the same way: identity tokens are becoming a shared interface rather than a lossy lookup key.
2. **Scaling-law tooling is moving into ranking systems.** Meta's Axia (2.3) treats architecture choices as a low-dimensional scaling manifold and reports a 0.36% cumulative online lift from only 34 model iterations — evidence that compute-allocation methodology, not just model architecture, is now an online-leverage lever.
3. **Serving constraints are entering the model.** RTP-LLM (2.6) makes request-time supply a decoding-time constraint; AdSteer (3.1) steers ads at the token level; MIS (3.4) recovers autoregressive order-dependence in a non-autoregressive one-pass ranker. The common pattern is moving business constraints earlier in the stack to avoid wasted beam capacity / inference / rewriting.
4. **Efficiency claims are being audited against named backends.** The Dynamic Wave study (4.1) shows a 78.7% VRAM win against unfused attention collapses to ~0% against fused SDPA; MERLIN (4.2) and SparseGDN (4.3) therefore report both quality and concrete kernel-level speedups. This is a healthier reporting norm for the linear-attention literature.
5. **Evaluation science keeps surfacing hidden protocol choices.** τ-Rec-Books (2.7) isolates disclosure timing; Optimal Re-Ranking Depth (3.5) shows a fixed depth is often wrong and that IR-DCG@10 can cut depth 3× without losing effectiveness. In both cases the measured "ability" depends heavily on a protocol knob that is usually left implicit.
6. **Sparse-attention and gated models have a silent numerical failure mode.** Near-zero token embeddings (1.3) affect 52.6% of untied gated/hybrid checkpoints surveyed, and the failure is invisible in loss curves until clipping overflow discards ~20% of steps. This is a practical checkpoint-audit item for anyone shipping Mamba/Gated DeltaNet/xLSTM variants.

---

## Source / Reproducibility Notes

- **Data source**: arXiv Export API (`https://export.arxiv.org/api/query`), queried 2026-11-08. The API returned intermittent HTTP 429 responses; queries were paced and retried serially. Pooled results were cached under the pre-approved temp dir `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/arxiv-search-1107/` and cleaned up after the report was written.
- **Coverage caveat**: `cs.LG`, `cs.CL`, `cs.IR`, `cs.GT`, `cs.MA`, and `cs.AI` were sampled at the 60–70 most-recent records per query, so the pool is a recent-window snapshot rather than an exhaustive category census. The latest submission timestamp observed was **2026-11-05T18:59:29Z**; the 2026-11-06 block had not yet posted at fetch time.
- **Abstract-only**: summaries are based on arXiv titles/abstracts and comments, not full PDFs. All quantitative claims are author-reported.
- **Sibling overlap**: same-day sibling digests (`arxiv-daily`, `arxiv-paper-check`, `game-rl-daily`, `conference-digest`) may cover some of the same IDs. This report intentionally favors IDs with **zero prior `wiki/` hits**; overlaps are limited to well-known items and are not re-derived from sibling text.
- **Affiliation caveat**: where arXiv did not state an institution, the affiliation is inferred from author lineage and marked *(tentative)*. Treat these as leads, not verified facts.
