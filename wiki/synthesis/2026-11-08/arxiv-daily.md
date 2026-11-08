---
title: "arXiv Daily — AI, LLMs, Recommendation, Advertising, CTR, Sequential Modeling, Games (2026-11-08)"
type: synthesis
created: 2026-11-08
updated: 2026-11-08
sources: [arxiv.org]
tags: [arxiv, daily, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, generative-recommendation, collaborative-filtering, retrieval, rag, recommender-agents, agents, reinforcement-learning, on-policy-distillation, sparse-autoencoders, linear-attention, sparse-attention, kv-cache, scaling-laws, game-theory, equilibrium-computation, evaluation-audit]
---

# arXiv Daily Report (2026-11-08)

> **Query time**: 2026-11-08. The latest indexed arXiv mailing batch still shows newest submissions dated **2026-11-05** (with a small 2026-11-04/11-02 tail); no 2026-11-06/07 announcement block is visible at query time. This report covers that batch.
>
> **Method**: arXiv Export API queries over `cs.IR`, `cs.AI`, `cs.LG`, `cs.CL`, `cs.GT`, and `cs.MA` sorted by `submittedDate`, plus title/abstract screening for recommendation, advertising/CTR, sequential modeling, LLM training/agents, retrieval, efficiency, and games. Abstracts are condensed from the API; affiliations come from the rendered paper HTML/PDF author blocks. All numbers are **author-reported** and not independently reproduced.
>
> **Companion report**: today's [arxiv-ai-search](arxiv-ai-search.md) covers a separate 26-paper sweep from the same window. Two Meta advertising papers below (`2611.01280`, `2611.01287`) also appear there; they are retained here because advertising/CTR is a required category for this report, and are marked as cross-referenced rather than presented as new discoveries.

## Summary

- **Advertising/CTR work is focused on label scarcity and post-click outcomes.** Meta describes auxiliary supervision for sparse CVR labels and a production system that personalizes the destination of an offsite ad click instead of routing every click to the same landing surface.
- **Recommendation research is auditing its own measurement stack.** Two Alibaba AMap papers show that category dashboards and multi-proxy preference explanations can move substantially under support/logging artifacts; a separate benchmark finds a "personalization imbalance" in multimodal recommendation agents.
- **Generative and LLM-based recommendation keeps diversifying.** E-GenRM builds a reward model for open-ended Taobao shopping agents; RecRSI automates recommender-algorithm discovery with mechanism hypotheses; PACERec adapts static LLM item embeddings with collaborative flow matching; LMStaR ranks explanations as dense retrieval.
- **LLM training has a strong compute-accounting theme.** A controlled study finds on-policy distillation only beats GRPO on accuracy per FLOP when the teacher is the student's own GRPO checkpoint; AttnSR derives step rewards from attention; SAE training-data scaling laws cut activation storage 8–64×.
- **Architecture work targets long-context cost and compression brittleness.** RecSA gives O(log L) sparse selection to 2M tokens; Muir makes linear-attention gates sensitivity-allocated; HST transfers KV, recurrent, and convolution state across hybrid models; a compression study finds larger models retain more of the damage.
- **Games and sequential decision papers are theory-heavy.** Exact proper equilibrium in two-player zero-sum extensive-form games becomes polynomial-time computable; Optimistic Hedge has horizon-independent regret only with two players; SHORE adds learned stability to online 3D bin packing.

## Methodology and scope

- **Sweep**: 80 newest entries from each of `cs.IR`, `cs.AI`, `cs.LG`, `cs.CL`, `cs.GT`, `cs.MA`, plus an `id_list` lookup for two advertising papers just outside the newest-80 window. HTTP 429 rate limits required serial retries with backoff.
- **Selection**: 23 papers balanced across advertising/CTR (2), recommendation/retrieval/sequential modeling (11), LLM training/agents/efficiency (7), and games/game theory/sequential decision (3). Title/abstract screening only.
- **Dedup**: featured IDs were checked against the 2026-11-07 and 2026-11-08 wiki reports. `2611.01280` and `2611.01287` intentionally overlap with today's companion `arxiv-ai-search`; all other featured IDs are absent from both 2026-11-07 and 2026-11-08 sibling reports at write time.
- **Caveats**: abstract-level review. Offline gains are not normalized across papers; online A/B results are single-company reports. Where arXiv HTML/PDF does not state an affiliation, that is stated explicitly.

---

## A. Advertising, CTR and Ranking

### 1. Improving Ads Ranking Models with Auxiliary Supervision: Techniques and Insights
- **arXiv**: [2611.01280](https://arxiv.org/abs/2611.01280)
- **Date**: 2026-10-31
- **Authors**: Nikhil Bhale, Apurva Pathak, SaiSujithKumarReddy MarapaReddy, Xiao Yin, Prateek Bhansali
- **Institution/Company**: Meta Platforms, Menlo Park, California, USA
- **Categories**: cs.IR
- **Abstract**: Post-click conversion rate (CVR) prediction is central to personalized ad delivery, but conversion labels are sparse or missing, which limits supervised learning. This industrial case study asks how to use auxiliary supervision from a diverse set of user events and metadata signals beyond conversion events, and how to model those signals well. It introduces linearized labels for better auxiliary-signal precision, a split architecture that decomposes the training task, and Label Combination (LaCo) for robust handling of noisy auxiliary data. The authors report measurable ranking-model improvements and argue the techniques transfer to related recommendation settings.
- **Key innovations**:
  - A production case study of **auxiliary supervision beyond conversion events** for sparse CVR.
  - **Linearized labels** to improve the precision of auxiliary targets.
  - A **split architecture** that decomposes the training task.
  - **LaCo** for robust combination of noisy auxiliary labels.
- **Cross-reference**: also summarized in today's companion [arxiv-ai-search](arxiv-ai-search.md).

### 2. Dynamic Click Destinations: Personalizing Post Ad-Click Landing Experiences
- **arXiv**: [2611.01287](https://arxiv.org/abs/2611.01287)
- **Date**: 2026-10-31
- **Authors**: Apurva Pathak, Yuya Shiraki, Iman Jenabzadeh, Nikhil Bhale, Yuwen Tan, Shashank Rangarajan, Amirmehdi Sharifzad
- **Institution/Company**: Meta Platforms, Menlo Park, California, USA
- **Categories**: cs.IR
- **Abstract**: Apps that monetize outbound ad clicks have several post-click levers: which landing page to show, whether the click opens a webpage or an app, and whether it resolves to a native in-product surface or the external web. The paper calls personalization over these levers **post ad-click destination automation**. Because the optimal destination varies across users, advertisers, placements, devices, and inferred intent, static routing is suboptimal. Dynamic Click Destinations (DCD) selects a destination per eligible offsite click to maximize Advertiser Value (AV), a value-weighted conversion outcome. The learning objective evolves from post-conversion destination inference, to two-task destination-conditioned conversion prediction, to a single-task policy that predicts which of two destinations is better, trained with A2C-inspired soft labels from a higher-capacity destination-conditioned critic. A web-vs-app case study on a major advertising platform reports online A/B gains over static routing, with the single-task objective performing best.
- **Key innovations**:
  - Formulates **post ad-click destination automation** as a per-click personalization problem.
  - Optimizes **Advertiser Value** rather than a generic click/conversion proxy.
  - Progressive objective design ending in a **pairwise destination policy** with critic-derived soft labels.
  - Large-scale online A/B evidence for web-vs-app destination selection.
- **Cross-reference**: also summarized in today's companion [arxiv-ai-search](arxiv-ai-search.md).

---

## B. Recommendation, Sequential Modeling and Retrieval

### 3. E-GenRM: Generative Reward Modeling for Open-Ended E-Commerce Shopping Agents
- **arXiv**: [2611.03008](https://arxiv.org/abs/2611.03008)
- **Date**: 2026-11-02
- **Authors**: Ying Sun, Qiuyu Zhao, Xiao Wang, Xiyu Zhao, Gege Shi, Zenghui Sun, Jinsong Lan, Haihong Tang, Bo Zheng
- **Institution/Company**: Taobao & Tmall Group of Alibaba; Technische Universität Wien
- **Categories**: cs.IR
- **Abstract**: E-GenRM is a generative reward model for e-commerce shopping agents, motivated by a shift from simple product queries to open-ended shopping tasks. Existing trajectories and reward designs are bounded by current usage patterns and known failures. On the data side, E-GenRM uses naturally occurring user behavior across the shopping app to construct diverse, long-horizon conversational trajectories beyond established patterns. On the modeling side, it first learns from behavior-grounded evaluation chains via supervised fine-tuning, then applies criterion-guided reinforcement learning that rewards correct preference judgments and evidence-supported factual claims. Personalized hard-negative training improves sensitivity to user preferences reflected in behavior, and an active evidence-retrieval extension acquires missing e-commerce information. On E-GenRM-Bench, E-GenRM-27B reaches **87.40% preference accuracy**, 6.97 points above the strongest baseline. A 14-day Taobao online A/B test reports **+1.39 pp effective shopping-assistance rate** and **+2.33 pp user satisfaction**.
- **Key innovations**:
  - Builds long-horizon shopping-agent trajectories from **real user behavior**, not only known agent usage patterns.
  - **Behavior-grounded evaluation chains** for reward-model SFT.
  - **Criterion-guided RL** rewarding preference correctness plus evidence-supported claims.
  - Personalized hard negatives and **active evidence retrieval**; large-scale Taobao validation.

### 4. Alternatives to Shallow Autoencoders for Collaborative Filtering
- **arXiv**: [2611.06610](https://arxiv.org/abs/2611.06610)
- **Date**: 2026-11-04
- **Authors**: Mario Mallea, Angela Nebot, Francisco Mugica
- **Institution/Company**: Universitat Politècnica de Catalunya (Soft Computing Research Group, IDEAI), Barcelona, Spain
- **Categories**: cs.LG, cs.IR
- **Abstract**: Collaborative filtering (CF) is a cornerstone of recommender systems. Embarrassingly Shallow Autoencoders for Sparse Data (EASE) is notable for its ranking accuracy and closed-form solution, but it relies primarily on item-item relationships to fit a full-rank high-dimensional linear mapping. The authors hypothesize that this design limits its ability to capture similar-but-not-equivalent fine-grained user relationships. They introduce an EASE-style alternative that uses **user-user** information, plus a hybrid model combining user-user and item-item adjacency distributions. Experiments on well-known recommendation benchmarks show the proposed models outperform EASE, supporting the user-side signal as a useful complement in shallow-autoencoder CF.
- **Key innovations**:
  - Replaces EASE's purely item-item view with a **user-user** shallow CF formulation.
  - Proposes a **hybrid user-user + item-item** adjacency model.
  - Provides benchmark evidence that the user alternative improves ranking accuracy over EASE.
  - Keeps the interpretable, computationally convenient shallow-linear-CF setting.

### 5. PMRecBench: A Benchmark for Personalization in Recommendation Agents under Multimodal Queries
- **arXiv**: [2611.06349](https://arxiv.org/abs/2611.06349)
- **Date**: 2026-11-04
- **Authors**: Xiaoyu Zhang, Yougang Lyu, Bin Wu, Sahan Bulathwela, Emine Yilmaz
- **Institution/Company**: University College London; University of Amsterdam
- **Categories**: cs.IR
- **Abstract**: Recommendation agents under multimodal queries must satisfy visually specified requirements while reflecting preferences inferred from user histories. Existing personalized recommendation benchmarks use text-only queries, while multimodal benchmarks assess query matching without evaluating personalization against real user histories. PMRecBench pairs **510 quality-controlled image-text queries** across clothing and movies with the corresponding users' real histories. Queries are derived from consistent behavioral patterns in real records, with reference images and targets linked to actual interactions. Diagnostic pools contain items rated highly by the user but violating the stated requirements, and items satisfying requirements but never rated highly. Experiments reveal a **personalization imbalance**: adding multimodal queries improves overall ranking but weakens preference following relative to personalization signals alone, and stronger commercial backbones do not resolve it. The authors link the decline to image interpretation, where agents prioritize resemblance to reference images over user-history evidence.
- **Key innovations**:
  - First benchmark (per authors) for **personalization under multimodal recommendation queries** tied to real histories.
  - **Diagnostic pools** separate requirement understanding from preference following.
  - Quantifies a **personalization imbalance** induced by adding visual query information.
  - Shows model scale alone does not fix the imbalance.

### 6. When Category Means Move: A Paired-Support Audit of Recommendation Logs with Random Insertions
- **arXiv**: [2611.05006](https://arxiv.org/abs/2611.05006)
- **Date**: 2026-11-03
- **Authors**: Yu Zhang, Zhihan Wang, Yuhang Lu, Shuai Li
- **Institution/Company**: AMap, Alibaba Group, Beijing, China
- **Categories**: cs.IR
- **Abstract**: Content-category dashboards summarize production recommendation logs, but the serving policy selects the users, items, and contexts behind each mean. Using KuaiRand random-insertion impressions, the authors audit these summaries on the **same 12,472 users and 5,486 videos** in both logs. Standard means have absolute/centered MAE 0.1935/0.0491 and rank correlation 0.7833. User demeaning plus a random grand-mean anchor reduces absolute MAE by 80.0% but centered MAE by only 21.0%, without reliably improving rank. A complete-support ledger attributes weighted squared error mainly to within-video residual (72.41%) and video mix (23.90%), with 3.65% from random support. In a frozen later test, early category calibration reaches MAE 0.0251 versus 0.0531 for scalar calibration. Decision evidence is cutoff-specific: the nominal top-10 regret change for row-weighted demeaning is −0.0062 [−0.0084, −0.0003], while top-5 and top-20 intervals include zero. All decompositions are descriptive and conditional on their overlap cohort; the authors claim neither intrinsic category effects nor a universally valid correction.
- **Key innovations**:
  - **Paired-support audit** of category dashboards on identical users/items under random-insertion logging.
  - **Complete-support error ledger** separating within-video residual, video mix, and random support.
  - Demonstrates that calibration gains are **cutoff-specific**, with top-5/top-20 intervals crossing zero.
  - Explicitly scopes conclusions to overlap cohorts rather than claiming universal category effects.

### 7. Auditing Multi-Proxy Explanations of Web User Preferences: Identification Boundaries and Abstention
- **arXiv**: [2611.04997](https://arxiv.org/abs/2611.04997)
- **Date**: 2026-11-03
- **Authors**: Yu Zhang, Zhihan Wang, Yuhang Lu, Shuai Li
- **Institution/Company**: AMap, Alibaba Group, Beijing, China
- **Categories**: cs.LG, cs.IR
- **Abstract**: Web systems infer preferences from behavior, ratings, text, and LLM-generated profiles, but explaining a proxy may reveal its measurement process rather than the preference of interest. The paper develops an audit framework that distinguishes **point identification**, **partial identification**, and **abstention** relative to an explicit reference distribution. Under feature-dependent, arbitrarily signed proxy bias, a strict majority of uncontaminated proxy attributions lets the coordinatewise median recover latent-attribution support and direction; with externally justified positive scales it also recovers magnitude. The authors prove the threshold sharp using response-valid indistinguishable worlds, characterize sharp minimax error and exact compatible-target sets under approximate cleanliness and scale uncertainty, and propagate clean-proxy attribution error. A frozen known-truth benchmark and a temporally separated Amazon study evaluate the framework; in the Amazon study, median aggregation reduces comparator-relative conditional sign error for all four targets, and six of eight prespecified target-metric contrasts have Bonferroni intervals excluding zero. The authors caution that weak comparator calibration limits the evidence to fitted-surface alignment rather than latent-preference recovery.
- **Key innovations**:
  - Audit framework separating **identification, partial identification, and abstention** for preference proxies.
  - Sharp majority-clean threshold for median aggregation under signed proxy bias.
  - **Compatible-target sets** quantify what the current proxy configuration can and cannot license.
  - Known-truth benchmark plus temporal Amazon study with prespecified contrasts.

### 8. SciToT: Multimodal Tip-of-the-Tongue Retrieval for Scientific Papers
- **arXiv**: [2611.05829](https://arxiv.org/abs/2611.05829)
- **Date**: 2026-11-04
- **Authors**: Stan Fris, Sijie Tao, Makoto P. Kato, Maarten de Rijke
- **Institution/Company**: University of Amsterdam; National Institute of Informatics, Tokyo; University of Tsukuba
- **Categories**: cs.IR
- **Abstract**: Researchers often struggle to re-find a paper when they remember content but not a reliable identifier such as title or author. This **tip-of-the-tongue (ToT)** retrieval problem is especially hard for scientific documents, where recollections may mix text with figures, diagrams, and plots. Existing ToT benchmarks do not address scientific search. SciToT introduces a multimodal scientific ToT benchmark with **108,512 open-access documents** across five domains and **11,499 synthetically generated queries**. A scalable elicitation pipeline independently extracts textual and visual memory cues and uses LLMs to generate queries resembling incomplete human recollections. The authors analyze public re-finding requests to characterize information needs, validate generated queries with human annotations and automated quality control, and provide lexical, dense, late-interaction, and visually grounded retrieval baselines. Dataset, representations, cues, splits, and pipelines are released under an MIT license.
- **Key innovations**:
  - First multimodal **scientific ToT retrieval benchmark** (per authors).
  - Query generation from **independent textual and visual memory cues**.
  - Grounds query design in real public re-finding requests plus human/automated validation.
  - Four retrieval baseline families and an MIT-licensed release.

### 9. ArcRAG: Agentic Compositional Retrieval over Knowledge Graphs
- **arXiv**: [2611.06481](https://arxiv.org/abs/2611.06481)
- **Date**: 2026-11-04
- **Authors**: Jyotin Goel, Abhinav Arun, Tejas Prakash Agarwal, Bhaskarjit Sarmah, Stefano Pasquali
- **Institution/Company**: Domyn
- **Categories**: cs.CL, cs.AI, cs.IR
- **Abstract**: GraphRAG answers questions by retrieving over a knowledge graph built from a corpus, but retrieval strategies are usually designed around the structure their own construction pipeline produces; whether they survive a change of construction is rarely tested. The paper studies **cross-construction portability**: whether one retrieval procedure, with no construction-specific schema, relation names, or retuning, remains effective when the graph is built differently. ArcRAG induces a **query-local graph interface** at inference time (node labels, relation descriptors, and property keys reachable from the entities named in the question), plans multi-hop traversals against it, and executes and repairs them as Cypher. The authors build MuSiQue, HotpotQA, and TriviaQA as both a schema-guided graph and an open-information-extraction graph, with the retriever configuration fixed across them. Results show retrieval need not be co-designed with graph construction, although construction still shapes absolute accuracy.
- **Key innovations**:
  - Tests **cross-construction portability** of GraphRAG retrieval.
  - **Query-time interface induction** instead of construction-specific schemas.
  - Agentic **plan–execute–repair** of multi-hop Cypher traversals.
  - Controlled comparison across schema-guided vs open-IE graphs with a fixed retriever.

### 10. Signed but Steerable: Measuring and Closing the Text-Vector Integrity Gap in Offline Retrieval-Augmented Generation
- **arXiv**: [2611.06498](https://arxiv.org/abs/2611.06498)
- **Date**: 2026-11-04
- **Authors**: Georgios Feretzakis, Alexandros Papaspyridis
- **Institution/Company**: securagen.ai, Athens, Greece
- **Categories**: cs.CR, cs.IR, cs.LG
- **Abstract**: Offline RAG on edge devices is updated through signed knowledge packs carrying text and precomputed embedding vectors. A signature proves who published a pack, not that its vectors encode its text. The paper studies this **text–vector integrity gap**. A verifier that recomputes vectors and accepts them within a cosine tolerance concedes a predictable share of queries to an attacker who controls the vectors: the hijack rate equals the distribution of angular retrieval margins at the tolerance (the **margin law**). Margins are small in five corpora and two embedding models, so an idealised floating-point-noise tolerance leaves up to **5.5% of queries exposed** (at most 1.2% per corpus after removing exact duplicates), while a threshold calibrated from a CPU INT8–FP32 comparison leaves **98–100% exposed**. On a Raspberry Pi 5 running a local language model, such an attack lowers correct answers from 0.75 to 0.39. On a FAISS product-quantisation index over 57,638 documents, tampered vectors that all pass the audit put the attacker's document first for 25% of targets. Verifying quantisation codes instead, with verifier-decided ambiguity, a calibrated guard band, and canonicalisation, accepted every honest vector on three platforms. The paper also shows common floating-point and dynamic-INT8 pipelines are not bit-reproducible across batch sizes or architectures, and reports pre-registered negative results on abstention, context pruning, and semantic screening.
- **Key innovations**:
  - Identifies and formalizes the **text-vector integrity gap** in signed offline RAG packs.
  - Derives the **margin law** linking angular retrieval margins to hijack rate.
  - Demonstrates practical attacks on CPU/edge and quantized vector stores.
  - Proposes quantisation-code verification with guard bands; documents non-bit-reproducibility and negative results.

### 11. RecRSI: Mechanism-Guided Discovery of Recommendation Algorithms
- **arXiv**: [2611.02487](https://arxiv.org/abs/2611.02487)
- **Date**: 2026-11-02
- **Authors**: Tingran Gan, Zhouziyue Lu, Dian Jin, Tao Li, Yang Gao, Ming Liu, Weiwen Liu, Jianghao Lin, Weinan Zhang, Yong Yu
- **Institution/Company**: Shanghai Jiao Tong University; Fudan University; Meituan
- **Categories**: cs.IR, cs.AI
- **Abstract**: Improving recommendation algorithms requires coordinating interacting design choices and learning from experiments. RecRSI is an LLM-based research framework that organizes algorithm discovery around **mechanism hypotheses**. Each hypothesis links a proposed mechanism change to a reference design, a rationale, and an expected observation. **MechSpace** derives implementable primitives and composition rules from the task source; **Research Line** uses this space and prior evidence to develop and test hypotheses; **Mechanism Feedback** carries outcomes and design context into subsequent research. Across four initial recommenders and four datasets, RecRSI yields average relative improvements of **8.48% NDCG@5** and **6.88% HR@5** over the initial algorithms, and 2.60%/2.20% over the strongest competing result for each setting and metric. Component and process studies link the gains to coordinated mechanism choices and evidence-guided follow-up.
- **Key innovations**:
  - Mechanism hypotheses as the unit of automated recommender research.
  - **MechSpace** primitives and composition rules derived from the task source.
  - **Research Line + Mechanism Feedback** turn each experiment into the next design decision.
  - Consistent gains across four recommenders and four datasets.

### 12. PACERec: Progressive Adaptation of LLM Item Embeddings with Collaborative Evidence for Recommendation
- **arXiv**: [2611.03068](https://arxiv.org/abs/2611.03068)
- **Date**: 2026-11-02
- **Authors**: Junzhao Huang, Xi Wu, Zihan Wang, Zijing Wang, Ming Wang, Kang Liu, Xiaocui Yang, Shi Feng, Daling Wang, Yifei Zhang, Ting Yang, Xurui Li
- **Institution/Company**: Northeastern University, Shenyang; Ant Group
- **Categories**: cs.IR, cs.AI
- **Abstract**: LLM embeddings are increasingly used in sequential recommendation to encode item attributes and alleviate sparse item-ID embeddings, but they typically capture static content similarity and miss sequential transitions. Existing adaptation methods rely on sparse per-item updates or global geometric calibration, so they struggle to transfer preceding interaction context from frequent to long-tail items. PACERec is an **ID-free progressive adaptation** framework that learns a shared velocity field from items with sufficient interactions via **frequency-weighted flow matching**, progressively guiding static LLM embeddings toward collaborative behavioral targets while preserving original item semantics. This avoids sparse per-item updates and generalizes sequential transition patterns to long-tail items for both user modeling and candidate scoring. Experiments on three real-world datasets across three sequential backbones show gains over competitive baselines in overall and long-tail recommendation.
- **Key innovations**:
  - **ID-free** adaptation of LLM item embeddings for sequential recommendation.
  - Shared velocity field learned by **frequency-weighted flow matching**.
  - Transfers behavioral evidence from frequent to **long-tail** items without per-item updates.
  - Preserves semantic content while adding collaborative transition structure.

### 13. Learning to Rank Explanations for Recommendation with Language Models
- **arXiv**: [2611.04775](https://arxiv.org/abs/2611.04775)
- **Date**: 2026-11-03
- **Authors**: Ben Kabongo, Vincent Guigue
- **Institution/Company**: Sorbonne University, CNRS, ISIR; AgroParisTech, UMR MIA Paris-Saclay
- **Categories**: cs.IR
- **Abstract**: Recommender systems need understandable explanations, and LLM-generated justifications are hard to evaluate for factual grounding and personalized relevance. Statement-level ranking offers a reproducible alternative by selecting concise, review-derived explanations and evaluating them with ranking metrics. Existing statement-ranking methods rely largely on collaborative representations, while semantic enhancements often fail to beat simple user-history popularity baselines; adapting language models to personalized statement ranking remains largely unexplored. **LMStaR** is a fully text-based framework that formulates personalized explanation ranking as dense retrieval: a query encoder represents the user's interaction history and target-item metadata, a statement encoder maps candidate explanations into a shared space, and both are jointly adapted with multi-positive contrastive learning. On Amazon Beauty, Amazon Toys, and Yelp, LMStaR achieves the highest NDCG@1 in all three domains, beating CLER by 1.06–8.25 points (+11.8–65.9%). It also leads top-five ranking on both Amazon datasets, though CLER remains stronger on Yelp. Task-specific adaptation improves all five evaluated backbones and transfers across domains without target-domain fine-tuning; counterfactual analyses show the importance of user-specific histories.
- **Key innovations**:
  - Casts **personalized explanation ranking** as text-only dense retrieval.
  - Jointly adapts history-aware query and statement encoders with **multi-positive contrastive learning**.
  - Strong NDCG@1 gains across three domains and five backbones.
  - Cross-domain transfer without target-domain fine-tuning; counterfactual evidence for history use.

---

## C. LLM Training, Agents, Efficiency and Interpretability

### 14. Unpacking the Compute Efficiency of Strong-to-Weak OPD against GRPO
- **arXiv**: [2611.08453](https://arxiv.org/abs/2611.08453)
- **Date**: 2026-11-05
- **Authors**: Zeyu Leo Liu, Yang Li, Bo Pang, Emre Can Acikgoz, Xuan-Phi Nguyen, Anurag Koul, Srijan Bansal, Erik Nijkamp, Shafiq Joty, Semih Yavuz
- **Institution/Company**: Salesforce AI Research; University of Illinois Urbana-Champaign
- **Categories**: cs.LG, cs.CL
- **Abstract**: On-policy distillation (OPD) trains a student on its own rollouts under frozen per-token teacher supervision. The paper asks whether this dense signal reduces the training FLOPs needed to reach a target accuracy compared with reinforcement learning. It systematically compares vanilla reverse-KL OPD with Group Relative Policy Optimization (GRPO) across task difficulty, student and teacher size, domain, and optimization choices, measuring held-out accuracy against training FLOPs. With an **external post-trained teacher**, OPD generally loses to GRPO in accuracy per training FLOP at matched settings, even when the teacher is further trained with GRPO, and often suffers response-length inflation. When the teacher is the **student's own GRPO checkpoint**, OPD recovers that checkpoint's accuracy on math with **50× fewer distillation FLOPs** than GRPO needs to reach the same accuracy; the pattern holds with a larger student, on code, and in a second model family. On a single domain, however, the GRPO checkpoint is already the desired model, so distilling it adds total compute. Multi-teacher OPD consolidates per-domain GRPO experts into one student at only **5.2% (2 domains)** and **8.0% (4 domains)** of specialist training FLOPs; counting specialist training plus distillation, the 2-domain mix reaches joint GRPO performance with **42.0% fewer total FLOPs**.
- **Key innovations**:
  - FLOP-controlled comparison of **OPD vs GRPO** across difficulty, model size, domain, and optimizer.
  - Shows external-teacher OPD is generally less FLOP-efficient than GRPO.
  - Identifies **strong-to-weak distillation from the student's own GRPO checkpoint** as the efficient regime (50× fewer distillation FLOPs).
  - Quantifies multi-teacher consolidation of domain specialists (5.2–8.0% of specialist FLOPs; 42.0% fewer total FLOPs on a 2-domain mix).

### 15. AttnSR: Attention Step Reward for Long-Horizon Agentic RL
- **arXiv**: [2611.07932](https://arxiv.org/abs/2611.07932)
- **Date**: 2026-11-05
- **Authors**: Mengsong Wu, Tianchen Zhou, Zhaochen Su, Zhenhua Liu, Zhe Cui, Aimin Zhou
- **Institution/Company**: East China Normal University (Shanghai Institute of AI for Education); Shanghai Innovation Institute; Hithink Research; Hong Kong University of Science and Technology
- **Categories**: cs.LG, cs.AI
- **Abstract**: Long-horizon LLM agents make multi-step decisions, but outcome-reward-only reinforcement learning gives little direct supervision for individual steps. AttnSR is a step-level reward augmentation method that derives reward allocation from **policy attention extracted during training replay**, without a separately trained reward model or extra rollouts. It traces backward through the policy model's attention graph to estimate the relevance of earlier steps to the final response; the terminal step, measured against a running baseline, determines whether the selected step rewards reinforce or penalize. In a controlled Qwen2.5-7B-Instruct study, AttnSR beats the PPO baseline at every evaluated checkpoint on ALFWorld, raising final held-out success from **91.2% to 97.1%**. It also improves ScienceWorld at every checkpoint while cutting environment interactions by **29.9%**. The ablation shows the benefit depends on how intermediate rewards are assigned rather than simply accumulating step rewards over time.
- **Key innovations**:
  - Extracts **step-level rewards from policy attention** during replay, with no reward model or extra rollouts.
  - Backward attention trace estimates earlier-step relevance to the final response.
  - Running-baseline terminal reward decides reinforcement vs penalty.
  - Strong ALFWorld/ScienceWorld gains and 29.9% fewer interactions; assignment-quality ablation.

### 16. Scaling Laws for SAE Training Data
- **arXiv**: [2611.07756](https://arxiv.org/abs/2611.07756)
- **Date**: 2026-11-05
- **Authors**: Nikita Koriagin, Nikita Balagansky, Daniil Gavrilov
- **Institution/Company**: Yandex; T-Tech
- **Categories**: cs.LG, cs.AI, cs.CL
- **Abstract**: Activation storage is often a bottleneck in sparse-autoencoder (SAE) training. The paper studies how many **unique activations** an SAE needs when its total training budget is fixed. Quality improves rapidly as the buffer grows, then plateaus, where replaying the buffer is nearly as effective as using fresh activations throughout training. Beyond the plateau, additional unique activations bring little benefit for reconstruction or interpretability, so the buffer need not grow with the training budget. The authors describe this diversity-repetition tradeoff with a scaling law for limited data and validate it across dictionary sizes, token budgets, early/middle/late layers of Llama-3.1 and Qwen3, and BatchTopK, TopK, and JumpReLU SAEs. Sweeps over mathematical text and Python code test activation-source effects. Evaluation covers explained variance, reconstruction MSE, feature absorption, automated interpretability, and sparse probing. The practical rule — choose the smallest buffer that reaches the plateau and replay it — reduces activation storage by **8–64×** with negligible quality loss.
- **Key innovations**:
  - A **scaling law for limited SAE training data** over unique activations vs replay.
  - Identifies a quality plateau after which more unique activations are not worth storing.
  - Broad validation across model families, layers, dictionary sizes, and SAE variants.
  - Practical **8–64× activation-storage reduction** with negligible measured quality loss.

### 17. When Bigger Becomes Brittle: Why Compression Hurts More as Language Models Scale
- **arXiv**: [2611.07891](https://arxiv.org/abs/2611.07891)
- **Date**: 2026-11-05
- **Authors**: Gautam Gupta, Dikshant Kukreja, Unique Kumar, Avni Mittal, Deepanshu Dabas, Kshitij Sah, Erik Cambria, Rajiv Ratn Shah, Zhengkui Wang, Avinash Anand
- **Institution/Company**: Indraprastha Institute of Information Technology Delhi; TurboML; Microsoft; Nanyang Technological University; Indian Institute of Technology Kanpur; Singapore Institute of Technology
- **Categories**: cs.AI
- **Abstract**: Quantization and pruning reduce deployment cost, but their effects are usually reported as benchmark scores, which record only the loss remaining at the output. Inside the model, compression damages some components more than others and the rest of the network can partly compensate; output scores cannot separate damage from compensation. The paper studies this compensation for **in-context retrieval**, a capability carried by a small, identifiable set of attention heads. It exactly decomposes the expected loss from ablating these heads into (i) the part restored by the rest of the network, attributed to responsible components, and (ii) the part reaching the output, then compares the decomposition across model sizes. For damage of comparable size, **smaller models restore most of the loss, whereas larger models retain most of it**, because compensating responses offset less as models grow. Compressing the heads produces the same pattern. Compression that is nearly harmless in small models can therefore be costly in large ones.
- **Key innovations**:
  - Separates **compression damage** from **network compensation** for in-context retrieval heads.
  - Exact, attributable loss decomposition rather than output-only benchmark scores.
  - Shows compensation weakens with model scale: larger models retain more of the damage.
  - Implies that compression harmlessness does not transfer upward across model sizes.

### 18. Beyond K/V Caches: Cross-Model State Handoff in Hybrid Linear-Attention LLMs
- **arXiv**: [2611.08133](https://arxiv.org/abs/2611.08133)
- **Date**: 2026-11-05
- **Authors**: Jiacheng Cai, Tao Zhang, Siqi Liang, Yun Dai, Ziqian Zeng
- **Institution/Company**: South China University of Technology
- **Categories**: cs.CL
- **Abstract**: Production deployments often switch between models to balance cost and quality, but context accumulates across turns and each switch forces the target model to re-prefill the conversation. Existing methods transfer full-attention K/V caches across models. Hybrid linear-attention models additionally retain **recurrent states (REC)** and **convolution histories (Conv)**, and the interaction between Conv and REC complicates transfer: Conv perturbations can change keys and values in recurrent layers and alter REC updates; Conv histories are overwritten, but REC changes can still affect later outputs, and more accurate REC reconstruction need not improve continuation. The paper proposes **Hybrid State Transfer (HST)** for all three state types, using structured REC maps and preserving history order during Conv alignment. Adapters are calibrated with the frozen target's outputs during continuation, and full-attention cache map updates are merged offline. Across five benchmarks, Qwen3.5 4B→27B and 9B→27B achieve mean task retentions of **89.88%** and **94.11%**; with source caches available, synthetic 16K inputs show handoff body speedups of **21.66×** and **21.91×**.
- **Key innovations**:
  - Extends cross-model state transfer beyond K/V to **recurrent and convolution state**.
  - Structured REC maps plus order-preserving Conv alignment.
  - Calibrates adapters against the frozen target model's continuation outputs.
  - High task retention and >21× handoff speedup for hybrid linear-attention models.

### 19. Muir: Linear Attention with Sensitivity-Allocated Gating and Matched-Filter Readout
- **arXiv**: [2611.08376](https://arxiv.org/abs/2611.08376)
- **Date**: 2026-11-05
- **Authors**: Tushaar Gangavarapu, Gil Tabak, Clemens JS Schaefer
- **Institution/Company**: University of Texas at Austin; Google (corresponding author domain; arXiv affiliation macro not rendered)
- **Categories**: cs.LG
- **Abstract**: Linear attention compresses context into a fixed-size key-value state for linear-time training and constant-memory inference. Gated delta-rule models decay this state and erase its prediction before writing a new value; Gated DeltaNet-2 (GDN-2) adds channel-wise decay and decoupled full-rank erase/write gates. The paper shows state updates are far less sensitive to **erasure** than to **writes**: key activation and unit normalization concentrate key energy on a sparse subset of channels, whereas value writes scale all channels, so the erase gate can be lower-rank. Slow-decaying state rows also accumulate much larger norms than fast rows, dominating unweighted readout and forcing stronger write-time erasure. **Muir** fuses all gates into a sensitivity-allocated low-rank projection, re-weights state rows with a matched-filter readout gate, and reinvests the saved parameters in a wider feed-forward network. A parallel update keeps training stable at the large chunk sizes needed for wide matrix units. Across 166M–1.34B parameters, Muir lowers perplexity by **1.8–2.0% vs GDN-2** and **2.5–3.6% vs Transformer**, raises commonsense accuracy by up to 1.9 points, extrapolates 2,560× from 4K training to 10M-token streams without perplexity drift, maintains near-100% passkey retrieval to 1M tokens, and trains 2.7× faster than Transformer at 32K while matching GDN-2 throughput.
- **Key innovations**:
  - Sensitivity analysis showing **erase gates need less rank than write gates**.
  - **Matched-filter readout** re-weights slow-decaying state rows.
  - Fuses gates into a low-rank projection and reinvests parameters in a wider FFN.
  - Stable parallel chunk update; strong perplexity, long-context, and throughput results.

### 20. Recursive Sparse Attention: Million-Token Length Extrapolation at Logarithmic Cost
- **arXiv**: [2611.07232](https://arxiv.org/abs/2611.07232)
- **Date**: 2026-11-04
- **Authors**: Ruitian Wang, Xinyu Yang, Minshen Zhang, Hao Zhang
- **Institution/Company**: University of California, San Diego; Carnegie Mellon University
- **Categories**: cs.CL, cs.LG
- **Abstract**: At ~1M-token contexts, dense attention is costly in prefill and decoding, and long training documents become scarce as target length grows. Most sparse attention methods score all preceding blocks or tokens, so per-query selection is **O(L)**; hierarchical selection can reach **O(log L)**, but prior trainable hierarchical methods report accuracy only within their training length. **RecSA** builds a tree over the KV cache in which each node summarizes its subtree with one key and one mean-pooled value. Keys come from one pooler per layer, shared across levels and distilled from dense attention. Each level above the tokens selects at most **k** candidates, so each query has O(log L) selection/read cost; summaries of unselected candidates share one softmax with exact tokens. Each entry's RoPE position is its index among candidates at its level, keeping every relative distance within the training range at any length. Initialized from Qwen3-4B and trained on 0.62B tokens at the original 32K length, RecSA beats all baselines on RULER at every length from 131K to 2M; at 1M it scores **60.5 vs 40.0** for the best baseline. Optimized kernels make it faster than dense attention from 64K to 2M; at 524K on one H200, prefill is **3.2×** and decoding **3.8×** faster.
- **Key innovations**:
  - **Recursive tree over the KV cache** with one key and mean-pooled value per node.
  - O(log L) selection and read per query via ≤k candidates per level.
  - **Level-local RoPE indexing** keeps relative positions inside the training range at any length.
  - Strong 2M-token extrapolation plus 3.2×/3.8× prefill/decode speedups at 524K.

---

## D. Games, Game Theory and Sequential Decision

### 21. Polynomial-Time Computation of Extensive-Form Proper Equilibria in Two-Player Zero-Sum Games
- **arXiv**: [2611.07089](https://arxiv.org/abs/2611.07089)
- **Date**: 2026-11-04
- **Authors**: Sam Ganzfried
- **Institution/Company**: Ganzfried Research; Cornell University
- **Categories**: cs.GT, cs.AI, cs.MA, econ.TH
- **Abstract**: The paper gives a deterministic polynomial-time algorithm for computing an **exact extensive-form proper equilibrium** in a finite two-player zero-sum extensive-form game with perfect recall and rational data. Properness is in the agent normal form: an action at an information set is penalized relative to a better action while all other local behavioral choices, including the player's own future actions, remain fixed. The algorithm assigns each information set a geometric **permutahedron** of allowable action probabilities. A scaled doubly stochastic representation embeds these restrictions in a polynomial-size sequence-form polytope; a saddle point then satisfies the local ε-properness inequalities. To obtain an exact equilibrium rather than an arbitrarily small numerical perturbation, the paper establishes **sign stability** of a parametric linear system, constructs a persistent feasible basis, and extracts limits of behavioral ratios. The resulting probabilities are rational with polynomial encoding length, including at information sets whose realization probabilities vanish.
- **Key innovations**:
  - **Polynomial-time exact** extensive-form proper equilibrium for two-player zero-sum games.
  - Geometric permutahedron restrictions embedded in a sequence-form polytope.
  - Sign-stability and persistent-basis machinery for exact rational probabilities.
  - Handles information sets with zero realization probability.

### 22. Optimistic Hedge in General-Sum Games: Fundamental Limits and Regret Bounds via Temporal Approximation
- **arXiv**: [2611.07078](https://arxiv.org/abs/2611.07078)
- **Date**: 2026-11-04
- **Authors**: Yuval Dagan, Nadav Eisen, Liad Erez, Tomer Koren
- **Institution/Company**: Tel Aviv University; Google Research, Tel Aviv
- **Categories**: cs.LG, cs.GT
- **Abstract**: Optimistic Hedge is a multiplicative-weights update with one step of extrapolation and one of the most natural regret-minimizing dynamics for games, but characterizing its regret has been a longstanding open question. Prior work showed polylogarithmic regret with a fixed learning rate, then a non-constructive horizon-independent bound with unclear dependence on the number of actions. The paper shows the answer **hinges on the number of players**. In two-player games, there is a learning rate for which Optimistic Hedge guarantees **O(n log n) regret independent of the horizon**. In three-player games no such bound is possible: for any learning rate up to an absolute constant and sufficiently large horizon, there is a game with n actions per player where some player's regret is **2^Ω(n)**; more generally, for every m≥3 there are m-player games with some player's regret **2^Ω(mn)**, and for learning rates above 2^−Ω(mn) that regret even grows linearly in T. The upper bound uses a **temporal approximation** framework that approximates losses over time-localized windows by well-behaved functions whose total variation is a small fraction of cumulative variance; the same framework simplifies the proof of a recent O(√m log n log T) bound.
- **Key innovations**:
  - Resolves the player-count dependence of Optimistic Hedge regret.
  - Horizon-independent **O(n log n)** regret in two-player games.
  - Exponential **2^Ω(n)** / **2^Ω(mn)** lower bounds for three or more players.
  - **Temporal approximation** framework yielding a simplified m-player upper-bound proof.

### 23. SHORE: Stability-Hybrid On-Policy Reinforcement Learning for Online Bin Packing
- **arXiv**: [2611.08364](https://arxiv.org/abs/2611.08364)
- **Date**: 2026-11-05
- **Authors**: Chang Shi, Ann Majewicz Fey
- **Institution/Company**: University of Texas at Austin
- **Categories**: cs.RO, cs.LG
- **Abstract**: Online 3D bin packing with a processing buffer requires choosing which box to pack, its orientation, and its placement while keeping the stack stable under unknown future arrivals; a collapse ends the episode and forfeits remaining volume. Existing methods use geometric rules or hard stability masks, limiting how risk can influence the joint choice of box, orientation, and placement. **SHORE** combines a learned **stability probability** of a placement with an on-policy estimate of its return conditional on stability. A 3D U-Net learns stability from executed outcomes and simulated alternatives, revealing outcomes of actions underrepresented in early rollouts. A discrete on-policy actor-critic uses stability predictions in both action values and the policy prior, with gates that limit the effect of an untrained or changing model. Deployment requires no additional search or simulation overhead. In Isaac Gym, SHORE reaches 73% space utilization by **0.4M environment steps**, versus about 1M for the same learner without stability modeling. On the expanded 60-box set, it achieves **0.734** utilization versus **0.588** for the GOPT state of the art, with a higher placement-failure frequency (1.03% vs 0.63%), trading more risk for more packed volume. The authors also demonstrate it on a real robot.
- **Key innovations**:
  - Hybridizes learned **stability probability** with on-policy return conditioning.
  - 3D U-Net stability model trained from executed outcomes plus simulated alternatives.
  - Stability-aware actor-critic values and policy prior with safety gates.
  - Faster learning and higher utilization than GOPT on realistic 60-box arrivals, with explicit risk trade-off.
