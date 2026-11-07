---
title: "arXiv Daily — AI / LLM / Recommendation / Advertising / Sequential Modeling / CTR / Games (2026-11-07)"
type: synthesis
created: 2026-11-07
updated: 2026-11-07
sources: [arxiv.org]
tags: [arxiv-daily, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, generative-recommendation, semantic-ids, reranking, user-modeling, decision-models, game-theory, linear-attention, sparse-attention, speculative-decoding, kv-cache, test-time-compute, agents, rl, daily-digest]
---

# arXiv Daily — 2026-11-07

> **Window**: newest indexed submissions are dated **2026-11-05** (with a small tail from **2026-11-04**); the export API snapshot at run time was `2026-11-06T23:46Z`. No 2026-11-06 or 2026-11-07 submission block was indexed yet. Saturday run, so this is the Friday-visible batch.
> **Method**: `export.arxiv.org` Atom API, newest-first, 150 entries each for **cs.IR / cs.AI / cs.LG / cs.CL** → **510 unique entries** after dedup. Queries for cs.GT / cs.MA / stat.ML were rate-limited (`HTTP 429`) and are therefore covered only through cross-listings in the four harvested categories; games/decision coverage below relies on cs.AI/cs.LG/cs.CL/cs.IR cross-lists.
> **Screening**: 510 titles → ~45 abstracts read in depth → **24 featured papers + 6 runner-ups**. Numbers are author-reported and not independently reproduced.
> **Sibling dedup**: today's `arxiv-paper-check.md` already features 28 IDs from this same batch (OPD cluster, RecSA, SAE work, user embeddings, OptST, CF-reward hacking, TTSP, PlayGen2, etc.). This report deliberately covers a different subset; the only intentional overlap is the two **CTR/advertising** anchors (ICE, BRIDGE), included for lane completeness and cross-referenced in §1.
> **Affiliation discipline**: the arXiv Atom API does not print affiliations. Institutions below are read from the paper text/benchmark lineage where unambiguous, otherwise marked **inferred / tentative**.

---

## 1. Recommendation, Advertising & CTR

### 1.1 Beyond Independent Predictions: Learning the Browsing Journey for Sequence-Level Re-ranking (ICE)

- **Authors**: Jiayi Zhang, Jingxin Hai, Zhenjia Ma, Hongbin Pei, Dagui Chen, Han Zhu, Jian Xu
- **Institution / Company**: Alibaba Group (Taobao) — inferred from the 14-day Taobao A/B test and full-traffic deployment; affiliation not printed on arXiv.
- **Published**: 2026-11-05 · cs.IR
- **Abstract**: Re-ranking aims to present users with an ordered list that maximizes sequence-level utility. Industrial deployments widely adopt the Generator–Evaluator framework, where the generator proposes candidate sequences and the evaluator scores them to select the best one for display. The fidelity of the evaluator's utility estimates thus directly governs recommendation quality. However, existing evaluators predominantly follow the Independent Behavior Modeling (IBM) paradigm, which simplifies the continuous user browsing journey into independent per-item predictions (e.g., CTR). This oversimplification ignores two physical realities: (i) a click can occur only after the item has been reached and impressed, and (ii) items compete for finite user attention. As a result, IBM produces systematically biased evaluations and suboptimal sequence selection. To address this, we propose a Joint Behavior Modeling (JBM) perspective that explicitly models the display → impression → click process to capture causal and competitive dependencies within a sequence. Building on JBM, we develop the Impression-Click Evaluator (ICE), a plug-and-play framework that (i) predicts a browsing-depth distribution to estimate per-position impression probabilities, (ii) leverages predicted impressions to suppress spurious context from unexposed items during click modeling, and (iii) introduces a click distribution matching objective to capture intra-sequence dependencies. Extensive offline experiments across diverse backbones, together with a 14-day online A/B test in the Taobao App (+0.70% clicks, +3.67% revenue) and full-traffic deployment, validate the effectiveness and robustness.
- **Key innovations**:
  - Replaces independent per-item CTR estimation with an explicit **display → impression → click** joint process.
  - Predicts a **browsing-depth distribution** to estimate per-position impression probabilities, and masks unexposed items during click modeling.
  - Adds a **click-distribution matching** objective to capture intra-sequence competition and dependencies.
  - Plug-and-play across backbones; Taobao A/B lift of **+0.70% clicks / +3.67% revenue**, then full traffic.
- **Link**: [arXiv:2611.07591](https://arxiv.org/abs/2611.07591)
- **Note**: also covered in `wiki/synthesis/2026-11-07/arxiv-paper-check.md`.

### 1.2 BRIDGE: Bridging the Semantic Quantization Gap for Generative Recommendation

- **Authors**: Yatong Xiao, Mingjie Sun, Peng Wang, Wenjin Wu, Peng Jiang
- **Institution / Company**: Large e-commerce advertising platform — inferred from the one-week online A/B on an ads platform; authors' affiliation not printed.
- **Published**: 2026-11-05 · cs.IR
- **Abstract**: Generative recommendation retrieves items by autoregressively generating Semantic IDs (SIDs), where an RQ-VAE quantizes each item into a hierarchical SID sequence that the decoder generates level by level. We identify an overlooked bottleneck in this paradigm: the Semantic Quantization Gap (SQG). Quantization derives SIDs from rich continuous signals, including codebook centroids, local neighborhood geometry, and level-wise entropy. However, the decoder receives only discrete identifiers and loses the semantic structure that shaped them. This mismatch manifests in three ways: a grounding gap, where the decoder lacks semantic anchors when target-side information is limited; a neighborhood gap, where token-level supervision discards inter-item similarity and exacerbates exposure bias; and a difficulty gap, where computation is allocated uniformly despite generation difficulty diminishing with depth. To bridge the SQG, we propose BRIDGE. Codebook-grounded latent reasoning injects frozen quantizer centroids as semantic anchors before SID generation. Privileged EMA self-distillation transfers neighborhood-aware knowledge from a teacher to an on-policy student, preserving inter-item geometry while mitigating exposure bias. Effort-aware recurrence allocates more computation to the challenging early levels and progressively reduces it with depth. Across three Amazon benchmarks, BRIDGE improves Recall@10 and NDCG@10 by 10.9% and 9.7% on average over the strongest baseline (up to 12.6% and 10.7%). In a one-week online A/B experiment on a large-scale e-commerce advertising platform with 5% traffic, BRIDGE improves eCPM by 0.65%.
- **Key innovations**:
  - Names and diagnoses the **Semantic Quantization Gap**: the decoder sees hard SIDs but not the continuous geometry that produced them.
  - **Codebook-grounded latent reasoning** injects frozen quantizer centroids as semantic anchors before SID generation.
  - **Privileged EMA self-distillation** transfers neighborhood-aware geometry to an on-policy student and reduces exposure bias.
  - **Effort-aware recurrence** spends more compute on harder early SID levels.
  - **+10.9% Recall@10 / +9.7% NDCG@10** average on three Amazon benchmarks; **+0.65% eCPM** in a 5%-traffic online ads A/B.
- **Link**: [arXiv:2611.07425](https://arxiv.org/abs/2611.07425)
- **Note**: also covered in `wiki/synthesis/2026-11-07/arxiv-paper-check.md`.

### 1.3 From Waste to Discovery: Recycling High-Scored Unexposed Candidates in Taobao Feed Recommendation (URED)

- **Authors**: Ge Fan, Kai Meng, Huiping Chu, Yuning Jiang, Han Zhu, Bo Zheng
- **Institution / Company**: Alibaba Group (Taobao feed) — production deployment stated in the abstract.
- **Published**: 2026-11-04 · cs.AI, cs.IR
- **Abstract**: Helping users discover new interests is vital to the long-term health of industrial recommender systems, yet the usual remedy, boosting exposure of under-explored (discovery) content, often backfires in production. We report URED (Unexposed Recycling for Efficient Discovery), a training-free recall-stage system serving Taobao feed recommendation at Alibaba for over six months to tens of millions of daily active users. It rests on a production-validated insight: naive boosting fails because it injects cold, information-poor candidates that rankers systematically over-estimate, buying no discovery gain while risking engagement. Items scored highly but never exposed (signals industrial pipelines routinely discard) form a pool that is both relevant and reliably predictable. Over a 30-day horizon URED aggregates them and re-injects them at recall time through a lightweight pipeline spanning offline storage, distributed aggregation, and low-latency online serving, adding under 1% latency via a single O(1) lookup per request with no model retraining. Online A/B tests show +3.47% discovered categories and +8.47% content richness with engagement preserved: completion video views rise significantly (+2.62%) and total views move positive (+0.36%, not significant). Ablations confirm both design pillars are necessary: a one-day window collapses the discovery gain to +0.55% (not significant), and random injection without score filtering yields no gain while trending negative on engagement (-0.17%). Across production recall channels, URED reaches 13.9x the platform-average discovery rate (6.3x the strongest nearline baseline) at engagement quality on par with the platform average. We share deployment details and lessons for practitioners facing the exploration-exploitation dilemma under tight resource constraints.
- **Key innovations**:
  - Reframes exploration as **recycling high-scored but unexposed candidates** rather than boosting cold content.
  - Training-free recall-stage pipeline: offline storage + distributed aggregation + one O(1) online lookup, **<1% latency**, no retraining.
  - One-day vs 30-day window ablation shows the discovery gain depends on a sufficiently long aggregation horizon.
  - Production A/B: **+3.47% discovered categories, +8.47% content richness, +2.62% completion views**, engagement preserved.
- **Link**: [arXiv:2611.05997](https://arxiv.org/abs/2611.05997)

### 1.4 Deliberate Latent Reasoning for Sequential Recommendation (DESRec)

- **Authors**: Haobo Zhang, Qiannan Zhu, Yutao Zhu, Zhicheng Dou
- **Institution / Company**: Renmin University of China — inferred from the author group; not printed on arXiv.
- **Published**: 2026-11-04 · cs.IR
- **Abstract**: Sequential recommenders are widely applied in real-world scenarios to model user preferences and behavior patterns based on user interactions. Recent advances in sequential recommendation enhance transformer-based models with latent reasoning to refine user representations by autoregressively generating intermediate reasoning vectors. However, exploring the optimal reasoning depth for diverse user histories remains challenging: existing methods typically employ a fixed number of reasoning steps for all users. This "one-size-fits-all" strategy often leads to suboptimal representation learning due to over-thinking in simple histories or under-thinking in complex ones. To address this, we propose DESRec, a deliberate latent reasoning framework that performs personalized latent reasoning to learn more informative reasoning states and enhance user modeling for sequential recommendation. Specifically, it designs a reasoning step selection module that identifies the optimal reasoning step for each user sequence during the training phase. Through a self-distillation mechanism, it compresses this most informative state into the final reasoning step, which serves as the final user representation for item ranking during inference. Moreover, it introduces a progressive preference extraction mechanism for personalized reasoning, which dynamically segments a user's history into a variable number of periods and summarizes each into a latent milestone representing the user's preference for that period. It will be used as the input of the subsequent reasoning. The number of milestones varies with the users' history, enabling a personalized reasoning over users' evolving interests. Extensive experimental results on six public datasets and four backbone recommenders demonstrate the superiority of DESRec over eight baseline models.
- **Key innovations**:
  - Personalized **latent reasoning depth** instead of a fixed number of reasoning steps for every user.
  - A **reasoning-step selection module** finds the most informative step per sequence, then self-distillation compresses it into the final inference state.
  - **Progressive preference extraction** segments each history into a variable number of periods, producing latent milestones for evolving interests.
  - Evaluated on six public datasets and four backbones against eight baselines.
- **Link**: [arXiv:2611.06521](https://arxiv.org/abs/2611.06521)

### 1.5 Do Recommenders Need to Think in Words? Latent Reasoning for Efficient LLM-Based Recommendation (LatentRec)

- **Authors**: Hongyang Su, Beibei Kong, Lei Cheng, Chengxiang Zhuo, Zang Li
- **Institution / Company**: Tencent — inferred from the author group; affiliation not printed on arXiv (tentative).
- **Published**: 2026-11-04 · cs.CL · CIKM 2026 short paper
- **Abstract**: LLM-based recommender systems increasingly generate chain-of-thought (CoT) text before each item prediction to activate the LLM's reasoning capacity, costing tens to hundreds of extra tokens per recommendation at inference. We ask whether inference-time reasoning artifacts (textual or latent) can be replaced by training-time supervision alone, without loss of accuracy. We propose LatentRec, a framework for LLM-based generative recommendation that replaces inference-time reasoning artifacts with training-time per-step head supervision. LatentRec has three components. A 2.5M-parameter Continuous Thought Module iterates K latent reasoning steps over the LLM's hidden state during training. Soft Token Selection bridges the ~14x norm gap between hidden states and input embeddings. A Per-step Reasoning Loss (PRL) supervises every intermediate state through the LLM's prediction head against the first token of the target Semantic ID. The trained LLM retains this accuracy without the module at inference, so the module can be discarded at deployment. On three Amazon benchmarks, LatentRec improves HR@10 by 4.0-5.0% (relative) over a CoT-distilled baseline at 18.3x lower latency (batch=1). Per-step training supervision consistently improves accuracy across three datasets, paid once at training rather than at every recommendation.
- **Key innovations**:
  - Moves reasoning from **inference-time CoT text** to **training-time per-step latent supervision**.
  - A small (2.5M-parameter) **Continuous Thought Module** iterates latent steps; **Soft Token Selection** bridges the hidden-state/embedding norm gap.
  - **Per-step Reasoning Loss** supervises every intermediate state via the LLM prediction head against the first Semantic-ID token.
  - Module is discarded at deployment: **+4.0–5.0% relative HR@10** over CoT-distilled baseline at **18.3× lower latency** (batch=1).
- **Link**: [arXiv:2611.07866](https://arxiv.org/abs/2611.07866)

### 1.6 One Basket, Many Experts: Decorrelated Re-ranking for Financial Asset Recommendation (DSER)

- **Authors**: Ryuki Unno, Keigo Sakurai, Koshi Watanabe, Keisuke Maeda, Takahiro Ogawa, Miki Haseyama
- **Institution / Company**: Hokkaido University — inferred from the author group; not printed on arXiv.
- **Published**: 2026-11-04 · cs.IR, cs.CE · ICAIF 2026
- **Abstract**: Financial asset recommendation for retail investors is typically optimized for relevance, that is, how well a recommendation matches what each user will buy. From the service provider's point of view, the value of a recommendation also depends on portfolio performance: the risk-adjusted return the recommended assets (the basket) deliver, which drives user engagement and fee revenue. The two goals are rarely achieved jointly, because the recommendations that best match user behavior concentrate on a few popular assets whose returns are highly correlated, which caps the risk-adjusted return a provider can offer. We propose Decorrelated-Satellite Expert Re-ranking (DSER), which retains the most relevant recommendations from an expert-following list and replaces the rest with return-decorrelated alternatives. The number of replaced slots is a single integer m (a knob) that the provider sets, so the relevance–performance trade-off becomes an explicit, auditable choice rather than a property hidden inside a learned model. In experiments on the public FAR-Trans retail-brokerage dataset, under the primary protocol, replacing a few slots improves risk-adjusted return at a small relevance cost, and the gain survives realistic trading costs at typical retail portfolio sizes. Minimizing correlation would lower basket volatility, but in our data the least-correlated assets are more volatile and higher-return, so their volatility offsets that reduction while their return drives the gain, not lower volatility. The resulting trade-off is asymmetric, with the relevance cost consistent across market phases while the gain is phase-dependent. The provider sets m to read off exactly how much relevance each operating point costs.
- **Key innovations**:
  - Jointly optimizes **behavioral relevance** and **portfolio risk-adjusted return** in re-ranking.
  - **DSER** keeps the most relevant expert-following slots and replaces the rest with return-decorrelated alternatives.
  - A single integer knob **m** makes the relevance–performance trade-off explicit and auditable.
  - FAR-Trans experiments show gains survive realistic trading costs; the relevance cost is stable across market phases while the gain is phase-dependent.
- **Link**: [arXiv:2611.05952](https://arxiv.org/abs/2611.05952)

### 1.7 PMRecBench: A Benchmark for Personalization in Recommendation Agents under Multimodal Queries

- **Authors**: Xiaoyu Zhang, Yougang Lyu, Bin Wu, Sahan Bulathwela, Emine Yilmaz
- **Institution / Company**: University College London — inferred from the author group; not printed on arXiv.
- **Published**: 2026-11-04 · cs.IR
- **Abstract**: On Web platforms for shopping and entertainment, recommendation agents under multimodal queries aim to deliver personalized recommendations that satisfy users' visually specified requirements and reflect preferences inferred from user histories. However, existing personalized recommendation benchmarks use text-only queries, while multimodal ones assess query matching without evaluating personalization based on real user histories. We introduce the Personalized Multimodal Recommendation Benchmark (PMRecBench), the first benchmark to evaluate the personalization of recommendation agents under multimodal queries. It pairs 510 quality-controlled image-text queries across clothing and movies with the corresponding users' real histories. PMRecBench features two key designs: (1) queries derived from consistent behavioral patterns in real user records, with reference images and targets linked to actual interactions; and (2) challenging diagnostic pools with candidate items rated highly by the user but violating requirements, and items satisfying requirements but never rated highly, testing requirement understanding and preference following, respectively. Extensive experiments on diagnostic pools reveal a personalization imbalance in recommendation agents: relative to personalization signals alone, adding multimodal queries weakens preference following, even though the additional information about query requirements improves overall ranking performance. Further analysis links this decline in preference following to image interpretation, where agents can prioritize resemblance to reference images over evidence from user histories, and stronger commercial backbones alone fail to resolve this imbalance. This personalization imbalance highlights a central challenge for recommendation agents: improving ranking performance while preserving preference following when responding to multimodal user queries.
- **Key innovations**:
  - First benchmark for **personalization under multimodal (image-text) queries**, pairing 510 queries with real user histories.
  - Diagnostic pools separate **requirement understanding** (items satisfying the query but never highly rated) from **preference following** (highly rated but requirement-violating items).
  - Reveals a **personalization imbalance**: multimodal query information improves overall ranking but weakens preference following.
  - Traces the failure to image interpretation and shows stronger commercial backbones alone do not fix it.
- **Link**: [arXiv:2611.06349](https://arxiv.org/abs/2611.06349)

### 1.8 Generative Retrieval under Real-Time Supply Constraints in Local Commerce (RTP-LLM)

- **Authors**: Shaopeng Liang, Biao Zhang, Hongzhen Ye, Zeyang Hou, Ma Jiang, Jintao Tu, yunxi. hz, Zhijia Fang, Jianqiang Cao, Junxue Rao, Jia Jia
- **Institution / Company**: Meituan — inferred from the local retail / food-delivery setting; affiliation not printed (tentative).
- **Published**: 2026-11-04 · cs.IR
- **Abstract**: Generative retrieval predicts semantic identifiers for candidate entities. In local retail and food delivery, candidates must also be serviceable for a particular user at a particular time. Location, weather, and traffic reshape merchant and product supply, so a catalog-valid identifier may be infeasible for the current request. Post-generation filtering removes such candidates only after beam capacity and inference computation have been spent. We study retrieval over an explicitly materialized, request-time supply snapshot, where short output sequences leave little opportunity to amortize online constraint preparation. Our RTP-LLM pipeline compiles eligible residual-quantization identifiers into a compressed sparse row prefix index, overlaps CPU compilation with model prefill, and shares the uploaded index across beams. Legal expansions retain original-model log probabilities, and constraint states follow selected beam parents. We formalize snapshot-relative identifier validity and distinguish it from entity-level eligibility and freshness. The implementation generates three-token merchant identifiers. Historical evidence covers T+1 daily-refresh catalog constraints and subsequent request-scoped serving evaluations. In one matched-beam daily-constraint case, filtered merchants decrease from 170 of 299 candidates to 29 of 299; residual distance filtering motivates request-specific constraints. A different-host comparison with 30,000 supplied entries reports a 0.6 ms service-side latency increment, while client measurements expose additional request costs. Captured requests from three geographic settings characterize behavior across supply sizes and output widths. These observations span development stages and measurement boundaries. They establish a practical implementation and identify bottlenecks, but do not establish compute savings at matched retrieval quality.
- **Key innovations**:
  - Makes **request-time supply constraints** first-class in generative retrieval, rather than post-generation filtering.
  - Compiles eligible RQ identifiers into a **compressed sparse row prefix index**, overlaps CPU compilation with model prefill, and shares the index across beams.
  - Formalizes **snapshot-relative identifier validity** vs entity-level eligibility and freshness.
  - Matched-beam case reduces filtered merchants from **170/299 to 29/299**; service-side latency increment **0.6 ms** in a different-host comparison.
- **Link**: [arXiv:2611.06323](https://arxiv.org/abs/2611.06323)

---

## 2. Search, Ranking & Attribution

### 2.1 Optimal Re-Ranking Depth

- **Authors**: Siqing Huo, Andrew Parry, Debasis Ganguly, Charles L. A. Clarke
- **Institution / Company**: University of Waterloo + University of Glasgow — inferred from the author group; not printed on arXiv.
- **Published**: 2026-11-04 · cs.IR
- **Abstract**: Second-stage neural rankers are commonly applied with a fixed re-ranking depth, assuming that retrieval effectiveness saturates as depth increases. Prior research has questioned the assumption that increasing the re-ranking depth yields linear performance gains, further suggesting that optimal re-ranking depth varies considerably from query to query. In the past, studying such phenomena was methodologically difficult given the scale of manual annotation required. With the advent of LLM-based relevance judgments we can now more easily undertake such studies, in this case to pinpoint the optimal re-ranking depth on a per-query basis. Using dense LLM-based relevance judgments over a typical re-ranking pipeline, we show that many queries exhibit a well-defined optimal re-ranking depth, beyond which effectiveness stagnates or degrades. We formulate re-ranking depth as a query-specific property and study whether it can be predicted a priori from first-stage retrieval characteristics. Through a large-scale analysis, we find that most standard query performance prediction (QPP) methods are ineffective for this task. In contrast, a predictor derived from LLM-assessed first-stage ranking quality, which we term IR-DCG@10, can reduce the average re-ranking depth by up to a factor of 3 while preserving overall effectiveness, depending on the specific first- and second-stage rankers used. Under oracle selection of optimal depths, we further show that retrieval effectiveness can improve by more than 7% while reducing the average re-ranking depth by a factor of 5 on the MSMARCO DEV collection. Given our promising preliminary findings, we would encourage the use of automatic judgments to facilitate research otherwise infeasible under manual annotation. Towards this point, we release relevance judgments, our codebase, and experimental artefacts to support reproducibility and further research.
- **Key innovations**:
  - Formulates re-ranking depth as a **query-specific** property rather than a global constant.
  - Uses dense **LLM-based relevance judgments** to locate each query's optimal depth at scale.
  - Shows standard QPP methods fail here, while **IR-DCG@10** (LLM-assessed first-stage quality) cuts average depth up to **3×** with preserved effectiveness.
  - Oracle analysis: **>7% effectiveness gain** with **5× lower** average depth on MSMARCO DEV.
- **Link**: [arXiv:2611.05908](https://arxiv.org/abs/2611.05908)

### 2.2 WISE: An Agentic Framework for Whole-page Multimodal Search Experience Attribution

- **Authors**: Wenyi Xu, Renzhe Zhou, Songyang Li, Feiran Zhu, Ruoqi Zhao, Chenglei Dai, Xuanping Li, Kaiqiao Zhan, Jingwei Zhuo
- **Institution / Company**: Industrial search platform — affiliation not printed on arXiv (tentative).
- **Published**: 2026-11-04 · cs.IR
- **Abstract**: Algorithm-driven services, including search, recommendation, and advertising, rely on multi-stage model pipelines. While research prioritizes model optimization, post-deployment monitoring focuses on operational reliability. Yet operationally healthy systems may still produce poor-quality results, exposing a gap in existing evaluation and monitoring practices. However, a systematic problem formulation and benchmark for this task remain lacking. To bridge this gap, we formulate System Quality Diagnosis (SQD) for algorithm-driven services, a new task that extends quality evaluation beyond identifying poor outcomes to attributing their causes across system components. Focusing on industrial search, we propose WISE, an agentic framework for end-to-end quality diagnosis that discovers user-facing issues and traces their origins to underlying algorithmic components. To improve diagnostic reliability, we introduce ReTrace for constructing evidence-consistent trajectory supervision and Adaptive Harness-Policy Optimization (AHPO) for failure-guided optimization of the agent harness and model policy. To enable systematic evaluation, we construct WISE-BENCH, a real-world multimodal search benchmark that combines user-facing evidence, internal pipeline traces, and expert diagnosis annotations. Extensive experiments show consistent gains across model scales, with WISE achieving 75.20% end-to-end accuracy on Qwen3.5-35B-A3B. In production, WISE supports quality auditing, online quality assurance, and model optimization, reducing diagnosis costs and improving downstream relevance models.
- **Key innovations**:
  - Defines **System Quality Diagnosis (SQD)**: not just detecting bad outcomes, but attributing them to pipeline components.
  - **WISE** agent discovers user-facing issues and traces them across a multi-stage search/recommendation/ads stack.
  - **ReTrace** builds evidence-consistent trajectory supervision; **AHPO** optimizes agent harness + policy from failures.
  - **WISE-BENCH** combines user evidence, internal traces, and expert diagnoses; **75.20%** end-to-end accuracy on Qwen3.5-35B-A3B.
- **Link**: [arXiv:2611.06777](https://arxiv.org/abs/2611.06777)

### 2.3 Do Search-Augmented Recommenders Use the Latest Search Episode?

- **Authors**: Jiandong Ding
- **Institution / Company**: Affiliation not printed on arXiv.
- **Published**: 2026-11-04 · cs.IR, cs.LG · WSDM 2027
- **Abstract**: Search-augmented recommenders can use the latest search episode and earlier searches. We introduce FocalSwap to test how these inputs contribute to the next recommendation. For each recommendation, it changes the latest search slot or all search inputs while holding the target, candidates, pre-search history, and scorer fixed. It compares neutral masks with matched observed-search replacements, recording rank changes, RR gains relative to each control, and preference for the true focal search. A planted signal and GenSAR's current-query task confirm that the audit detects known input dependence. We evaluate behavioral and lexical evidence on KuaiSAR and Qilin, and recommendation checkpoints trained using the released SESRec and UniSAR implementations. Across three independently trained UniSAR checkpoints, the estimated all-source benefit depends on the control. On the same 66,139 rows, replacing all search inputs with a neutral ID yields a positive signed contribution, whereas replacing them with category/profile-matched observed search sequences gives smaller estimates, with an interval below zero for one checkpoint. The paired RR gaps range from +2.770 × 10^-3 to +6.604 × 10^-3, and every adjusted interval is above zero. Neutral masks change 59.7-61.7% of target ranks, while matched replacements change 44.1-44.8%. The control contrast persists across five alternative donor assignments per checkpoint. Under the primary neutral-mask and category-matched controls, positive latest-slot contribution is not established in SESRec or UniSAR. These results show why masking evidence should be compared with observed-search replacements when attributing a benefit to broader search state or the latest episode.
- **Key innovations**:
  - **FocalSwap** causal audit swaps the latest search slot or all search inputs while holding target/candidates/history/scorer fixed.
  - Compares neutral masks against **matched observed-search replacements**, exposing control-dependent attribution.
  - Finds **no established positive latest-slot contribution** in SESRec or UniSAR under primary controls, despite positive RR gaps under neutral masking.
  - A caution for search-augmented recommenders: masking-only evidence overstates the value of the latest search episode.
- **Link**: [arXiv:2611.06044](https://arxiv.org/abs/2611.06044)

### 2.4 Item Representations Matter: Bridging Hard Semantic IDs and Soft Prototype Mixtures for Generative Retrieval (CAP-Mix)

- **Authors**: Vicente Balmaseda, Dongqi Fu, Jiarui Feng, Ren Chen, Hanqing Zeng, Tianxin Wei, Yinglong Xia, Tianbao Yang, Hong Li
- **Institution / Company**: Texas A&M University + collaborators — inferred from the author group; affiliation not printed (tentative).
- **Published**: 2026-11-04 · cs.IR, cs.LG
- **Abstract**: Modern recommender systems rely on generative retrieval techniques to predict the next item either as discrete codes or as a continuous vector. On the one hand, Semantic IDs (SIDs) give discrete models shared parameters and pretrained semantic structure, but discretizing items into hard codes discards some information from the original content embeddings. On the other hand, continuous models avoid quantization, yet typically use flat item lookup tables with no explicit parameter tying across items. We ask whether a continuous recommender can introduce shared structure without making it a discrete bottleneck. We propose CAP-Mix, a flow recommender that represents each item as a soft mixture of shared prototypes plus an item-specific vector. The assignments, prototypes, and item vectors are trained jointly, and the soft representation is retained at inference. Pretrained information is optional: SID responsibilities can serve as a prior over assignments, while a full content embedding can initialize the item-specific vector without changing the initial flat table. In matched comparisons on three datasets, CAP-Mix improves over a flat table on the two sparse Amazon datasets and yields a small gain on Steam when trained without pretrained information. Given only an offline SID, it outperforms a hard table built from the same tokenizer by 4.45-14.90% in HR@5. Given the full content embedding, it matches or improves a strong flat table while hard assignments regress on the sparse Amazon datasets. Overall, averaged across six benchmarks, CAP-Mix improves HR@5 and NDCG@5 by 6.9% and 13.6% relative to the best evaluated baseline for each dataset and metric, while delivering 1.4-161x the inference throughput of the discrete baselines in our experiments.
- **Key innovations**:
  - Represents each item as a **soft mixture of shared prototypes + an item-specific vector**, retaining continuous structure without a hard discrete bottleneck.
  - Jointly trains assignments, prototypes, and item vectors; SID responsibilities can act as an optional prior.
  - Beats a hard table from the same tokenizer by **4.45–14.90% HR@5** given only an offline SID.
  - Averaged over six benchmarks: **+6.9% HR@5 / +13.6% NDCG@5**, with **1.4–161×** inference throughput vs discrete baselines.
- **Link**: [arXiv:2611.05799](https://arxiv.org/abs/2611.05799)

---

## 3. Sequential Modeling, Decision & Games

### 3.1 A Hidden Markov Preference Model for Online Prediction of Adversary Actions

- **Authors**: Angel Daruna, Michael Cogswell, Tixiao Shan, Yi Yao, Han-Pang Chiu, Ajay Divakaran
- **Institution / Company**: SRI International — inferred from the author group; not printed on arXiv.
- **Published**: 2026-11-05 · cs.LG
- **Abstract**: A defender anticipating an attacker needs a probability distribution over the attacker's next action from information available before that action occurs. Two structures complicate this: the attacker's behavioral regime persists and can switch within an episode, and each action combines an operation with state-dependent arguments whose feasible values change over time. We capture both with a hidden Markov model whose latent state is the active regime and whose regime-conditioned action law is defined on a feasibility-masked tree of executable actions. The same likelihood forms the next-action distribution and updates the regime belief once the action is seen, and a partially observed prefix contributes its resolved local factors. Estimation separates into convex logistic fits that Baum-Welch reuses when regimes are unlabeled. We derive a reach-weighted nodewise KL expression for regime information, a sequence-wise log-loss bound for switching regime paths, and a uniform fallback guarantee. On the CAGE 2 cyber defense benchmark the filtered latent state is worth 0.8 nats per step, and after a controller switch the loss begins to fall in three steps against ten for a recurrent baseline.
- **Key innovations**:
  - Latent **behavioral regime** HMM combined with a **feasibility-masked tree** of executable actions, so next-action probabilities respect state-dependent argument validity.
  - Same likelihood drives prediction and regime-belief updates; a partially observed prefix contributes resolved local factors.
  - Estimation reduces to convex logistic fits reusable in Baum-Welch for unlabeled regimes; provides reach-weighted KL, log-loss, and fallback guarantees.
  - CAGE 2 cyber-defense: filtered latent state worth **0.8 nats/step**; post-switch loss recovers in **3 steps vs 10** for a recurrent baseline.
- **Link**: [arXiv:2611.08445](https://arxiv.org/abs/2611.08445)

### 3.2 Learning and Steering in Incomplete-Information Games

- **Authors**: Asrın Efe Yorulmaz, Tamer Başar
- **Institution / Company**: University of Illinois Urbana-Champaign — inferred from the author group; not printed on arXiv.
- **Published**: 2026-11-05 · cs.GT, cs.AI, cs.LG, eess.SY, math.OC
- **Abstract**: In many modern multi-agent systems, a mediator seeks to influence strategic decision dynamics using only outcome-level feedback and without knowing agents' utilities. In this work, we study how a mediator can learn an unknown game and steer adaptive agents toward outcomes that maximize her utility using only trajectory feedback. The mediator knows the game form and her own objective, but not the agents' utilities. Moreover, she commits to nonnegative payments and provides recommendations and contexts, but receives only a single realized terminal outcome rather than full-information feedback. We develop halving-type algorithms that learn utility differences in normal-form games and conditional continuation-value differences in extensive-form games, achieving a sample complexity of Õ(ε^-2) that matches worst-case lower bounds up to logarithmic factors. We then combine these learning procedures with a Lagrangian formulation in an online Learn-Compute-Steer algorithm that interleaves learning, equilibrium computation, and steering toward mediator-optimal extensive-form correlated equilibria (EFCE). With high probability, the Learn-Compute-Steer algorithm achieves a directness gap and an optimality gap of Õ(T^-1/4), while time-average payments are of Õ(T^-1/8).
- **Key innovations**:
  - Mediator learns an unknown game from **outcome-level trajectory feedback only**, without agents' utilities.
  - Halving-type algorithms for utility differences (normal form) and conditional continuation values (extensive form), **Õ(ε^-2)** sample complexity.
  - **Learn-Compute-Steer** interleaves learning, equilibrium computation, and steering toward mediator-optimal EFCE.
  - High-probability **Õ(T^-1/4)** directness/optimality gaps with **Õ(T^-1/8)** time-average payments.
- **Link**: [arXiv:2611.07589](https://arxiv.org/abs/2611.07589)

### 3.3 Optimal Learning in Games with Arbitrary Delays: Best-of-Both-Worlds for Self-Play and Adversarial Opponents

- **Authors**: Emmanuel Esposito, Andrew Jacobsen, Hao Qiu, Alexander Ryabchenko, Mengxiao Zhang
- **Institution / Company**: Affiliation not printed on arXiv.
- **Published**: 2026-11-05 · cs.LG, stat.ML
- **Abstract**: We study learning in zero-sum games with delayed feedback. We introduce Multi-Anchor Optimistic Online Mirror Descent (MAO-OMD), a single algorithm which obtains optimal fast rates in self-play on smooth games, while simultaneously maintaining minimax optimal guarantees against arbitrary opponents. In particular, in smooth zero-sum games with arbitrary and unknown feedback delays, MAO-OMD obtains O(σ_max + 1) social and individual regrets when used by both players, where σ_max denotes the maximum number of outstanding gradients, while also guaranteeing minimax optimal O(√(T + d_tot)) individual regret against arbitrary opponents, where d_tot is the total delay. Moreover, we show that these optimal rates cannot be obtained simultaneously using the standard black-box reduction to the undelayed setting. We also extend our results to multi-player games, and to games with player-dependent delay sequences.
- **Key innovations**:
  - **MAO-OMD** is a single algorithm that is simultaneously fast in self-play and robust against arbitrary opponents under arbitrary unknown delays.
  - Self-play: **O(σ_max + 1)** social and individual regret on smooth zero-sum games.
  - Adversarial: minimax-optimal **O(√(T + d_tot))** individual regret; shows black-box reduction cannot achieve both.
  - Extends to multi-player games and player-dependent delay sequences.
- **Link**: [arXiv:2611.07773](https://arxiv.org/abs/2611.07773)

### 3.4 Towards Foundation Decision Models: Drex

- **Authors**: Nischay Dhankhar, Alisher Amantay, Zhanibek Datbayev, Darkhan Akhmetov, Yash Shah, Nurmukhamed Ubaidullayev, Raman Saparkhan, Dos Baha, Abulhair Saparov
- **Institution / Company**: New York University + nace.ai — inferred from the author group and the `nace-ai` model/code release; affiliation not printed on arXiv.
- **Published**: 2026-11-05 · cs.CL
- **Abstract**: Autoregressive approaches with large language models, such as long chain-of-thought reasoning, have become the default for new AI applications because they reach higher accuracy on a wide range of tasks. In production, however, they give inconsistent answers, require parsing of outputs, and add cost and latency. Decision models address this: given a question and a set of options supplied by the user, they return a probability distribution over the options without autoregressive decoding. We present Drex, a family of four open decision models with 8B (DLM), 9B (v1.5), 35B with 3B active (v2.0), and 27B (Max) parameters. Each request consists of a state (a document, record, or agent context, optionally with images) and questions about it, each asking for a choice among options, a yes/no judgment, or a score on an ordered scale. Training combines supervised fine-tuning with reinforcement learning from adjusted feedback (RLAF), plus vision tuning for Max. Ablations show that RLAF improves accuracy and that consistency losses improve robustness to option order. On Decision Index 0.4.1, Max sets a new state of the art among the decision models we compare (67.52 on the public suite vs. 60.70 for Jev 1.14.0). On Decision Bench v4, it is statistically tied with d3-turbo and GPT-6 Sol and trails Claude Opus 5.5 by 1.6 points, and it has the highest accuracy among decision models on DecideBench. Max answers a typical request in 183 ms, against about 2.0 s for GPT-6 Sol and 3.5 s for Claude Opus 5.5, and its outputs are stable under option reordering. All four models are open source.
- **Key innovations**:
  - A family of four **open decision models** (8B, 9B, 35B-A3B, 27B) that return option distributions without autoregressive decoding.
  - Requests combine a state (document/record/agent context, optionally images) with multiple-choice, yes/no, or ordered-score questions.
  - Training: SFT + **RLAF** (RL from adjusted feedback) + vision tuning; consistency losses improve option-order robustness.
  - **67.52** on Decision Index 0.4.1 vs 60.70 for Jev 1.14.0; **183 ms** typical latency vs ~2.0 s for GPT-6 Sol and ~3.5 s for Claude Opus 5.5.
- **Link**: [arXiv:2611.07854](https://arxiv.org/abs/2611.07854)

### 3.5 Turns Matter: Advancing Streaming Video RL via Turn-Level Credit (TurnWise)

- **Authors**: Shuai Dong, Kanghui Tian, Linghan Chen, Wenqi Shao, Hongrui Wu, Haowen Hou, Yongfu Zhu, Xuehui Wang, Ziyue Wang, Wenpu Liu, Weichu Xie, Yuqi Xu, Congcong Wang, Kaiwen Tuo, Caoyuan Ma, Taiqiang Wu, Ji Zhao, Wenzheng Chang, Dianyi Wang, Siyuan Wang, Zhongyu Wei, Yu Qiao, Jiaqi Wang
- **Institution / Company**: Shanghai AI Laboratory + Fudan University — inferred from the author group; not printed on arXiv.
- **Published**: 2026-11-04 · cs.CV, cs.CL, cs.LG
- **Abstract**: Streaming video understanding requires models to repeatedly decide whether to respond or continue observing. Recently, Group Relative Policy Optimization (GRPO) has been applied to this setting, with existing approaches emphasizing reward design while retaining a single trajectory-level advantage across turns. Such shared credit can reinforce redundant replies after earlier successes and discourage useful follow-ups after earlier failures. We propose TurnWise, a turn-level GRPO framework that aligns learning with individual streaming decisions. TurnWise addresses the mismatch between trajectory-level feedback and turn-level interaction, promoting informative responses and reducing redundancy. Specifically, turn-level credit assignment uses silence-completed prefix scoring to construct group-relative advantages from each decision's remaining return, separating its learning signal from earlier rewards. Turn-mean policy optimization averages token losses within each turn and then across turns, giving response and waiting decisions equal weight regardless of output length. These complementary designs improve streaming policy learning without a learned critic or additional rollouts. Extensive experiments show our method outperforms prior RL approaches for streaming video understanding.
- **Key innovations**:
  - **Turn-level GRPO** for streaming video, replacing trajectory-level credit with per-decision credit.
  - **Silence-completed prefix scoring** constructs group-relative advantages from each decision's remaining return.
  - **Turn-mean policy optimization** averages token losses within and across turns, balancing respond vs wait regardless of output length.
  - No learned critic and no additional rollouts; consistently beats prior streaming-video RL methods.
- **Link**: [arXiv:2611.06728](https://arxiv.org/abs/2611.06728)

---

## 4. LLM Efficiency, Architecture & Inference

### 4.1 First-Token Attraction in Mamba Dynamics

- **Authors**: Trinh T. Nguyen, Minh-Khoi Nguyen-Nhat, Duy-Tung Pham, Hoang-Son Do, Tan Minh Nguyen, Thieu N. Vo
- **Institution / Company**: Vietnam-based collaboration — affiliation not printed on arXiv (tentative).
- **Published**: 2026-11-05 · cs.AI
- **Abstract**: We study token dynamics in deep Mamba models, with a particular focus on the attracting role of the first token. Unlike attention mechanisms, where token interactions are governed by positive scalar coefficients, Mamba dynamics involve full matrix-valued interaction coefficients with no positivity or definiteness guarantees. This structural difference makes Mamba dynamics substantially harder to analyze and prevents the direct application of existing techniques for attention-based models. To overcome this challenge, we introduce a new analytical framework based on a high-dimensional invariant box and a sharp exit-time argument, which together recover an effective form of sign-definiteness. Using this framework, we characterize the possible limit points of token trajectories and prove explicit exponential convergence rates. Our analysis reveals that the first token has privileged dynamics: its limiting direction attracts subsequent tokens, inducing token clustering and attention-sink phenomena in deep Mamba models. We further show that this attraction mechanism extends to broader sequence dynamics, including state-space models, causal attention, and classical time-series models. Experiments on Falcon-Mamba-7B validate our predictions, showing that concentration on the first token increases with depth and dominates in later layers.
- **Key innovations**:
  - New analytical framework for Mamba token dynamics using a **high-dimensional invariant box** and a sharp exit-time argument to recover sign-definiteness.
  - Proves explicit **exponential convergence rates** and characterizes token-trajectory limit points.
  - Shows the **first token has privileged attracting dynamics**, inducing token clustering and attention-sink behavior.
  - Extends to state-space models, causal attention, and classical time-series models; validated on Falcon-Mamba-7B.
- **Link**: [arXiv:2611.08303](https://arxiv.org/abs/2611.08303)

### 4.2 SPARE: Fast Linear Attention Decoding with Compact Recurrent States

- **Authors**: Ke Wan, Zaiyi Zheng, Chen Chen
- **Institution / Company**: University of Central Florida — inferred from the author group; not printed (tentative).
- **Published**: 2026-11-05 · cs.CL
- **Abstract**: Linear attention reduces the quadratic sequence-length complexity of softmax attention by maintaining fixed-size recurrent states. However, these states scale quadratically with the representation dimension and require repeated data transfers during decoding, creating a substantial GPU memory bottleneck. Recent studies have revealed significant low-rank redundancy in recurrent states, suggesting opportunities for more efficient representations. We introduce SPARE (State Projection for Accelerated Recurrent Execution), a training-free method that exploits this redundancy through fixed low-dimensional subspaces, heterogeneous rank allocation, and lightweight write compensation. By performing recurrent reads and updates directly on compact states, SPARE reduces memory traffic without online decomposition or dense-state reconstruction. SPARE achieves 2.55x full-model decoding speedup, 7.49x lower recurrent-kernel DRAM traffic, and 3.31x lower peak GPU memory, while preserving better associative-retrieval accuracy than structured pruning at matched memory budgets.
- **Key innovations**:
  - **Training-free** compression of linear-attention recurrent states via fixed low-dimensional subspaces.
  - **Heterogeneous rank allocation** + lightweight write compensation; reads/updates operate directly on compact states.
  - Avoids online decomposition or dense-state reconstruction.
  - **2.55×** full-model decoding speedup, **7.49×** lower recurrent-kernel DRAM traffic, **3.31×** lower peak GPU memory, better associative retrieval than structured pruning at matched budgets.
- **Link**: [arXiv:2611.07552](https://arxiv.org/abs/2611.07552)

### 4.3 Latency-Aware Adaptive Best-of-N

- **Authors**: Alon Jacobson, Qian Xie, Peter I. Frazier
- **Institution / Company**: Cornell University — inferred from the author group; not printed on arXiv.
- **Published**: 2026-11-05 · cs.CL, cs.LG
- **Abstract**: Test-time compute (TTC) improves language model responses by spending additional computation at inference time, and the right amount of compute depends on the prompt. Adaptive TTC methods allocate compute based on signals of response quality such as observed rewards, often by stopping once the signal exceeds a fixed threshold, and generally measure cost by the number of generations or tokens. But in online serving, latency is also a cost: it grows with server load, so a method using a fixed threshold spends too little compute when generation is fast and too much when it is slow. For Best-of-N sampling, a widely used TTC method, we propose a two-stage adaptive algorithm that draws an initial batch, then uses the observed rewards and the batch's latency to decide whether to draw a second batch and at what size by comparing expected improvement against predicted cost: it draws one when the first batch's best reward is below a threshold that decreases with the first batch's latency, without explicitly measuring server load. We map each reward to its value under the cumulative distribution function (CDF) of the prompt's reward distribution, so the same tradeoff parameters can be reused across tasks; a regression fitted offline on other prompts predicts a distribution for the CDF value of the first batch's best reward, giving the expected improvement in closed form. We evaluate the method by simulation on a preference-based alignment benchmark, measuring generations-equivalent cost: generations plus latency, converted to generations. The method reaches Best-of-N's reward at lower generations-equivalent cost, and conditioning on the measured first-batch latency saves at least as much of that cost as fixed-threshold (latency-unaware) baselines, and more when latency is highly variable, when it grows with batch size, and when the second batch's latency is highly predictable from the first's.
- **Key innovations**:
  - Treats **latency as part of the inference cost** in adaptive Best-of-N, without explicitly measuring server load.
  - Two-stage algorithm: draw an initial batch, then use observed rewards + batch latency to decide whether/how large a second batch should be.
  - Maps rewards through the prompt's **reward CDF** so trade-off parameters transfer across tasks; closed-form expected improvement.
  - Reaches Best-of-N reward at lower generations-equivalent cost; gains grow when latency is variable or scales with batch size.
- **Link**: [arXiv:2611.07453](https://arxiv.org/abs/2611.07453)

### 4.4 SpecCTMC: Exact Speculative Simulation of Diffusion Language Model Continuous-Time Markov Chains

- **Authors**: Siva Rajesh Kasa, Yasong Dai, Sumit Negi, Hongdong Li
- **Institution / Company**: Industrial research lab — affiliation not printed on arXiv (tentative).
- **Published**: 2026-11-05 · cs.CL
- **Abstract**: Masked diffusion language models offer parallel text generation, but independently sampling multiple tokens can disrupt their dependencies and change the output distribution. Exact continuous-time sampling avoids this approximation, yet typically requires one sequential model evaluation per token. We introduce SpecCTMC, a training-free speculative sampler that reduces this sequential bottleneck without a separate draft model. SpecCTMC proposes successive token updates using previously computed model predictions, evaluates their intermediate states in parallel, and applies an exact acceptance-and-correction procedure. We prove that SpecCTMC preserves the joint distribution of event times, generation order, and token values of the underlying continuous-time Markov chain. It therefore introduces neither time-discretization error nor additional factorization error from parallel decoding. Experiments on LLaDA-8B-Instruct and Dream-v0-Instruct-7B across five benchmarks demonstrate 1.73-4.38x fewer sequential model evaluations than direct continuous-time sampling, while preserving the reference sampling distribution.
- **Key innovations**:
  - **Training-free speculative sampler** for masked diffusion LMs, with no separate draft model.
  - Proposes successive token updates from previously computed predictions, evaluates intermediate states in parallel, and applies exact acceptance/correction.
  - Proves preservation of the joint distribution over **event times, generation order, and token values** — no discretization or parallel-factorization error.
  - **1.73–4.38× fewer sequential model evaluations** on LLaDA-8B and Dream-v0-7B across five benchmarks.
- **Link**: [arXiv:2611.08362](https://arxiv.org/abs/2611.08362)

### 4.5 Beyond K/V Caches: Cross-Model State Handoff in Hybrid Linear-Attention LLMs (HST)

- **Authors**: Jiacheng Cai, Tao Zhang, Siqi Liang, Yun Dai, Ziqian Zeng
- **Institution / Company**: Affiliation not printed on arXiv (tentative).
- **Published**: 2026-11-05 · cs.CL
- **Abstract**: Production deployments often use different models to balance cost and quality through cascading, routing, and switching models during long conversations. Context accumulates across turns. Each switch requires the target to repeat prefill over this context. Existing methods transfer full-attention (FA) K/V caches across models. Hybrid linear-attention models also retain recurrent states (REC) and convolution histories (Conv). The interaction between Conv and REC complicates cross-model state transfer. Conv perturbations can change keys and values in recurrent layers and alter REC updates. Conv histories are overwritten, but changes in REC can still affect later outputs. More accurate REC reconstruction need not improve continuation. Building on this, we propose Hybrid State Transfer (HST) for all three state types. It uses structured REC maps and preserves history order during Conv alignment. We calibrate the adapters using the frozen target's outputs during continuation. FA cache map updates are merged offline. Across five benchmarks, Qwen3.5 4B→27B and 9B→27B achieve mean task retentions of 89.88% and 94.11%, respectively. With source caches already available, separate timing on synthetic 16K inputs yields handoff body speedups of 21.66x and 21.91x.
- **Key innovations**:
  - Extends cross-model cache transfer beyond full-attention K/V to **recurrent states (REC)** and **convolution histories (Conv)** in hybrid linear-attention LLMs.
  - **Structured REC maps** + history-order-preserving Conv alignment; adapters calibrated on the frozen target's continuation outputs.
  - Offline-merged FA cache map updates.
  - Qwen3.5 4B→27B / 9B→27B retain **89.88% / 94.11%** mean task performance; **~21.7–21.9×** handoff body speedup at 16K.
- **Link**: [arXiv:2611.08133](https://arxiv.org/abs/2611.08133)

---

## 5. Agents & Post-Training

### 5.1 AttnSR: Attention Step Reward for Long-Horizon Agentic RL

- **Authors**: Mengsong Wu, Tianchen Zhou, Zhaochen Su, Zhenhua Liu, Zhe Cui, Aimin Zhou
- **Institution / Company**: East China Normal University — inferred from the author group; not printed (tentative).
- **Published**: 2026-11-05 · cs.LG, cs.AI
- **Abstract**: Long-horizon LLM agents make multi-step decisions, yet outcome-reward-only reinforcement learning provides little direct supervision for individual steps. We introduce AttnSR, a step-level reward augmentation method that derives reward allocations from policy attention extracted during training replay, without a separately trained reward model or additional rollouts. AttnSR traces backward through the policy model attention graph to estimate the relevance of earlier steps to the final response. The terminal step, measured relative to a running baseline, determines whether these rewards reinforce or penalize the selected steps. In a controlled Qwen2.5-7B-Instruct study, AttnSR consistently outperforms the PPO baseline across all evaluated checkpoints on ALFWorld, raising final held-out success from 91.2% to 97.1%. The ablation experiment shows that the benefit depends on how intermediate rewards are assigned, rather than simple accumulation of step rewards over time. AttnSR also improves ScienceWorld at every checkpoint while cutting environment interactions by 29.9%. These results support policy attention as a practical prior for step-level reward allocation in long-horizon agentic RL.
- **Key innovations**:
  - Derives **step-level rewards from policy attention** during replay — no separate reward model and no extra rollouts.
  - Traces backward through the attention graph to score earlier-step relevance; the terminal step (vs a running baseline) decides reinforcement vs penalty.
  - ALFWorld held-out success **91.2% → 97.1%** with PPO baseline, all checkpoints improved.
  - Also improves ScienceWorld while cutting environment interactions by **29.9%**; benefit depends on credit assignment, not reward accumulation.
- **Link**: [arXiv:2611.07932](https://arxiv.org/abs/2611.07932)

### 5.2 The Last Mile to the Real World: Agent-Native Primitives as Reusable Building Blocks (HEELO)

- **Authors**: Haibo Jin, Peng Kuang, Xiaopeng Yuan, Lucheng Fu, Jerry Wang, Xucheng Yu, Yaoning Yu, Dehao Wu, Runguo Li, Colin Su, Jingxuan Sun, Xuyang Liu, Haojing Luo, Haohan Wang
- **Institution / Company**: University of Illinois Urbana-Champaign + Heelo.dev — inferred from the author group and project page; not printed on arXiv.
- **Published**: 2026-11-05 · cs.CL, cs.AI, cs.LG, cs.MA, cs.SE
- **Abstract**: How can an agent handle a real-world task end to end? Frontier models with their own harnesses still fall short on real-world benchmarks: on Terminal-Bench 4.0, GPT-5.6 Sol with Codex resolves 37.3% of the tasks and Claude Opus 5 with Claude Code 51.8%. These tasks fail at the step from reaching a resource to applying it, which we call the last mile to the real world. Existing approaches put the resource within reach but leave the competence to apply it with the caller, so each harness rebuilds that competence. We introduce agent-native primitives, reusable units that equip a resource with a resident LLM that applies it in context and communicates with other primitives, and HEELO (Harness Engineering around Evolving Agent-Native Primitives for the Last Mile to Real-WOrld Tasks), a harness engineering framework that builds each task's harness from a library of such primitives. HEELO composes the primitives a task needs into a task-specific graph, verifies the result against evidence from the environment, revises the primitives a failure implicates, and admits new or improved primitives after validation. We instantiate HEELO with eight primitive families, each built for one kind of task, and evaluate them on more than twenty benchmarks. Dev-Primitives raise Terminal-Bench 4.0 resolution from 37.3% under Codex to 55.5% on the same backbone, Harness Primitives composed per task raise Terminal-Bench 2.0 Pass@1 from 60.0% for the seed harness to 72.2%, Tool Primitives raise ToolBench pass rate from 55.8% to 75.1%, and Navigation Primitives raise GAIA-Text-103 accuracy from 45.6% to 58.3%. On the 46 real-world tasks of our heelo.dev platform, Claude Opus 5.5 with Claude Code and GPT-6.1 Sol with Codex complete 9 each on their own and 39 and 35 when connected to HEELO through our MCP server, with 1.9× and 2.3× less time and 1.55× lower cost per completed task.
- **Key innovations**:
  - Defines **agent-native primitives**: resources paired with a resident LLM that applies them in context and talks to other primitives.
  - **HEELO** composes primitives into a task-specific graph, verifies against environment evidence, revises implicated primitives, and admits validated improvements.
  - Eight primitive families evaluated on 20+ benchmarks: Terminal-Bench 4.0 **37.3% → 55.5%**, Terminal-Bench 2.0 Pass@1 **60.0% → 72.2%**, ToolBench **55.8% → 75.1%**, GAIA-Text-103 **45.6% → 58.3%**.
  - On 46 real-world tasks, MCP-connected agents complete **39/46** and **35/46** vs 9/46 standalone, with **1.9–2.3× less time** and **1.55× lower cost** per completed task.
- **Link**: [arXiv:2611.07461](https://arxiv.org/abs/2611.07461)

---

## 6. Runner-ups & Same-Batch Sibling Coverage

### 6.1 Runner-ups

| arXiv ID | Title | Why it is worth a look |
|---|---|---|
| [2611.06610](https://arxiv.org/abs/2611.06610) | Alternatives to Shallow Autoencoders for Collaborative Filtering | Adds user-user adjacency to EASE-style CF and a user-user + item-item hybrid; improves ranking on standard benchmarks. |
| [2611.07296](https://arxiv.org/abs/2611.07296) | Robust Ranking of Port Impacts from Impending Tropical Cyclones | Two-stage retrieval + Wide & Deep ranking for port impact under landfall uncertainty; +85.5% / +55.5% ranking agreement vs distance baseline. |
| [2611.07508](https://arxiv.org/abs/2611.07508) | DelegateEval: Evaluating Platforms for Personal External Service Agents | Eight-dimension platform-level evaluation framework for agents that serve external clients on an individual's behalf. |
| [2611.07891](https://arxiv.org/abs/2611.07891) | When Bigger Becomes Brittle: Why Compression Hurts More as Language Models Scale | Decomposes compression damage vs network compensation; larger models retain more of the damage, so "harmless" compression can be costly at scale. |
| [2611.07982](https://arxiv.org/abs/2611.07982) | How Far Can Lightweight LLMs Go in Intent-to-SLO Translation? | Ten sub-10B LLMs on 716 intents: best strict F1 0.943, but rephrasing weakens invalid-intent rejection in 15/16 configurations. |
| [2611.07650](https://arxiv.org/abs/2611.07650) | What the Middleman Delivers: Answer Behavior, Tool Permissions, and Billed Usage in LLM API Relays | Audits commercial LLM API relays for answer behavior, tool permissions, and billing inconsistencies. |

### 6.2 Already covered in today's sibling `arxiv-paper-check.md`

To avoid duplicate full entries, these same-batch papers are cross-referenced rather than repeated:

- **OPD cluster**: learning dynamics (2611.08016), CoRD coupled rollouts (2611.07959), O²PD prefix gating (2611.07731), OPD-vs-GRPO FLOP accounting (2611.08453).
- **Efficiency/architecture**: RecSA million-token sparse attention (2611.07232), Muir linear attention (2611.08376), Loopback Transformer (2611.07226), la-JEPA (2611.08156).
- **Interpretability**: SAE-over-MoE expert specialization (2611.08089), SAE training-data scaling law (2611.07756).
- **Recommendation/user modeling**: User embeddings as behavioral-mode superpositions (2611.08487), CF-reward exposure collapse (2611.07588), OptST semantic tokenization (2611.07523), GINGER graph ANN search (2611.08306), Axis-LoRA personal-memory retrieval (2611.07820).
- **Games/self-play/world models**: Test-Time Self-Play without a verifier (2611.07367), PlayGen2 real-time playable worlds (2611.07867).
- **Agents/RL**: multi-turn agentic RL budget dependence (2611.06483), verifier-RL marginal value (2611.07639).

---

## 7. Observations

1. **The CTR/ads lane is production-heavy, not architecture-heavy.** The two anchors are both online-validated: ICE changes the *evaluation target* from independent CTR to a display→impression→click process (Taobao +0.70% clicks / +3.67% revenue), while BRIDGE changes the *generative-retrieval representation* and reports +0.65% eCPM on an ads platform. No new classical CTR-prediction backbone appears in this window.
2. **Recommendation is converging on sequence-level and personalized-compute objectives.** DESRec learns per-user latent reasoning depth; LatentRec removes inference-time CoT entirely; RTP-LLM treats request-time supply as a first-class retrieval constraint; PMRecBench shows multimodal query understanding can *hurt* preference following.
3. **Semantic IDs remain the main generative-retrieval battleground.** BRIDGE targets the quantization gap; CAP-Mix proposes soft prototype mixtures as a continuous alternative to hard SIDs; RTP-LLM compiles RQ identifiers into a constrained prefix index for local commerce.
4. **LLM efficiency work is increasingly white-box.** Mamba's first-token attraction is analyzed theoretically; SPARE exploits low-rank recurrent-state redundancy; SpecCTMC gives an exact distribution-preserving speculative sampler for diffusion LMs; HST extends cross-model state transfer to recurrent + convolution state.
5. **Games/decision work splits into theory and deployable decision models.** MAO-OMD handles delayed feedback in self-play and against adversaries; mediator steering learns incomplete-information games from outcome feedback; Drex argues for non-autoregressive decision heads with 183 ms latency and stable option ordering.
6. **Agent post-training is moving from outcome rewards to step-level credit.** AttnSR derives step rewards from policy attention (91.2% → 97.1% ALFWorld), and HEELO packages reusable agent-native primitives rather than rebuilding harness competence per task.

---

*Generated from the arXiv export API on 2026-11-07. Abstract text is quoted/condensed from arXiv metadata; key innovations are the report author's summary. Affiliations marked tentative are inferred and should be verified against the paper PDF before citation.*
