---
title: arXiv AI Search — AI, LLMs, Recommendation, Advertising, CTR, Sequential Modeling, Games (2026-10-30)
type: synthesis
created: 2026-10-30
updated: 2026-10-30
sources: [arxiv.org]
tags: [arxiv, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, generative-recommendation, auctions, mechanism-design, agents, memory, looped-transformers, scaling-laws]
---

# arXiv AI Search — AI, LLMs, Recommendation, Advertising, CTR, Sequential Modeling, Games (2026-10-30)

> Generated: 2026-10-30 | Effective submission window: **2026-10-24 to 2026-10-27** (latest indexed mailing at query time)
>
> A curated sweep of recent arXiv submissions across AI, LLMs, recommendation, advertising, CTR, sequential modeling, and games. Abstracts below are condensed from the arXiv API. Institutions are parsed from the rendered HTML author blocks or the PDF first page, never inferred. Where arXiv lists no affiliation, the field says so explicitly.

## Summary

- **Recommendation is splitting into three optimization targets: input configuration, representation reuse, and inference depth.** OptIDC coordinates sample/feature/embedding-unit selection before interaction modeling; HiRank compresses heterogeneous low-order tokens by effective rank; CRIM caches reusable item memories outside the request path; LoopGR and DPE-Rec buy depth or diffusion speed without proportional parameter growth. The shared constraint is serving cost, not raw model capacity.
- **Generative retrieval is now a memory-and-index problem.** Octen-WebGR puts 201M pages into a 4B model as two-token URL identifiers and runs on one 10 GB GPU, reporting 59.6% top-1 on real navigational traffic versus 46.5% for a click-enhanced dense retriever. MuSID-KD attacks the complementary problem: preserving prefix-level ranking while distilling multi-token semantic IDs.
- **The CTR cluster is about the input side and about evaluation validity.** OptIDC is a model-agnostic input-side selector; a separate theory paper shows that a large fraction of item-item similarity is "phantom correlation" produced by heterogeneous user activity alone. Both argue that gains attributed to architectures may sit in data geometry or preprocessing.
- **Advertising theory is converging on cascade auctions with pair-specific CTRs.** Two papers independently resolve the tension between constant-factor welfare and monotonicity/truthfulness: a factor-6 mechanism for cascade position auctions and a factor-2 mechanism for pair-specific CTRs in AI-generated content. A third result proves joint no-regret is computationally impossible for budget-constrained pacing bidders.
- **Games are being used as system-level agent benchmarks.** DECE spans ten Eurogames and shows harness choice changes the same model's ranking; AutoTavern uses LLM research agents to build a Hearthstone Battlegrounds player that reaches ~15,000 ladder rating; a small-budget Riichi Mahjong replication finds text is the bottleneck, not scale.
- **Agent memory and self-improvement remain the most active LLM frontier.** CrossProfile shows that both "keep rare facts" and "keep relevant facts" fail predictably when fact ownership is confounded with usefulness; TANDEM closes the centralization-decentralization gap with a dual-read critic; Skill∞ and Infinity Machine push recursive self-improvement into skills and research harnesses respectively.
- **Looped Transformers get two complementary fixes.** LoopFold parallelizes recurrent depth to cut latency 46% at five sequential stages; StateLoop adds a persistent per-token state so information can survive across iterations.

## Methodology and scope

- **Source sweep**: arXiv Export API queries for `cs.IR`, `cs.AI`, `cs.LG`, `cs.CL`, `cs.GT`, and `cs.MA` (80–200 most recent entries per category), deduplicated to **445 unique in-window arXiv IDs** for 2026-10-24 through 2026-10-27. The export API returned intermittent `Rate exceeded` / HTTP 503 responses; categories were retried serially with backoff.
- **Selection**: title/abstract screening for recommendation, advertising/auctions, CTR/conversion, sequential modeling, LLM training/agents, and games. **30 papers** are featured. Of these, **21 had zero prior hits** in `wiki/` at shortlist time. Nine (`2610.35695`, `2610.35550`, `2610.35318`, `2610.34157`, `2610.33707`, `2610.34236`, `2610.33845`, `2610.34791`, `2610.37397`) also appear in the [2026-10-29 arXiv AI Search](../2026-10-29/arxiv-ai-search.md), which was written after the initial novelty grep and covers a nearby window; they are retained here as full entries so this report is self-contained. `2610.36020` (Roblox creative pre-ranking) is cross-referenced rather than re-summarized because it is already covered in the [2026-10-29 arXiv Paper Check](../2026-10-29/arxiv-paper-check.md).
- **Metadata**: titles, authors, abstracts, dates, and categories come from the arXiv API. Affiliations come from `arxiv.org/html/{id}v1` `.ltx_role_affiliation` blocks. For eight papers without marked affiliations, the PDF first page was parsed with `pypdf`; `2610.35256` lists only the company (Octen), and `2610.34791` lists a single author at the University of Tokyo.
- **Caveats**: this is an **abstract-only** review; all numbers are author-reported and were not independently reproduced. Venue labels follow arXiv comments. The sweep is bounded by each category's recent-results window and is not an exhaustive census of every 2026-10-24…27 submission.

---

## 1. Recommendation and Generative Recommendation

### 1.1 Do Similarity Measures Measure Similarity? How User Activity Creates Phantom Correlation in Recommender Systems
- **Authors**: Marco Favier, Noah Daniëls, Jens Leysen, Sander Marinus, Bart Goethals
- **Institution/Company**: University of Antwerp
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.35765
- **Categories**: cs.IR, cs.AI

**Abstract**: Item-item similarity assumes that co-consumption reflects shared preference. The paper shows that a substantial fraction of observed similarity is an artifact of variance in user activity. Even if every user consumed items independently, differing only in total consumption volume, standard similarity measures still detect strong associations. The authors call this **phantom correlation**. Starting from minimal assumptions, they show that independent consumption under varying activity is described by a Rasch model, derive how the resulting association depends on item popularity for each similarity measure, and compare the theoretical baseline against real benchmark datasets.

**Key Innovations**:
- Defines phantom correlation as spurious item association arising from heterogeneous user activity with no preference structure.
- Connects independent consumption to a Rasch model and derives popularity-dependent baselines per similarity measure.
- Quantifies how much of the similarity signal in standard benchmarks is explained by activity volume alone.
- Reframes item co-occurrence interpretation for collaborative filtering and similarity-based retrieval.

---

### 1.2 Unified Heterogeneous Feature Interaction via Effective-Rank Scaling for Recommender Systems (HiRank)
- **Authors**: Ao Zhang, Haochuan Li, Boya Du, Jian Yang, Qihang Fang, Yulin Xu
- **Institution/Company**: Alibaba Group; Renmin University of China; Institute of Automation, Chinese Academy of Sciences
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.35318
- **Categories**: cs.IR

**Abstract**: Industrial ranking models must jointly capture heterogeneous feature interactions, long-term user behaviors, and multi-scenario dependencies under strict serving constraints. Existing architectures process sequential and non-sequential features with separate modules, limiting bidirectional exchange; applying homogeneous self-attention to all semantic tokens is inefficient when the two signal types have different effective ranks. HiRank integrates gated sequential attention with heterogeneous feature interaction in a unified backbone, uses scenario-aware aggregation to compress low-order tokens, and transforms the compact representation into scenario-aware composite tokens for high-order self-attention. Online A/B tests report a **2.27% increase in orders per user**.

**Key Innovations**:
- Unified backbone with bidirectional fusion between sequential and non-sequential representations.
- Effective-rank motivation for why homogeneous attention over all tokens is inefficient.
- Scenario-aware token compression and composite-token construction to avoid negative transfer across scenarios.
- Industrial-scale offline scaling plus online A/B evidence.

---

### 1.3 Towards a Unified Framework of Optimal Input-Side Dimensional Configuration for Deep CTR Prediction (OptIDC)
- **Authors**: Chaohua Yang, Fuyuan Lyu, Xing Tang, Dugang Liu, Xiuqiang He, Zhong Ming
- **Institution/Company**: College of Computer Science and Software Engineering, Shenzhen University; McGill University; Shenzhen Technology University
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.35695
- **Categories**: cs.IR, cs.AI

**Abstract**: CTR performance depends not only on feature-interaction architecture but on how input-side information is configured. Prior work optimizes sample selection, feature selection, or embedding-unit selection independently, overlooking their shared form and cross-level dependencies. OptIDC jointly learns sample-, feature-, and embedding-unit-level configurations, and introduces a **selection-weighted Optimal Transport** mechanism to align coarse- and fine-grained selections over finite measures. It is model-agnostic and integrates into existing CTR models. On four real-world benchmarks it consistently achieves higher AUC than existing input-side selection methods.

**Key Innovations**:
- Treats sample, feature, and embedding-unit selection as one joint input-side dimensional configuration problem.
- Uses selection-weighted optimal transport to coordinate selections across granularities and reduce cross-level conflicts.
- Model-agnostic plug-in rather than a new interaction backbone.
- Reports consistent AUC gains across four benchmarks.

---

### 1.4 CRIM: Composable and Reusable Item Memory for Efficient Personalized Retrieval
- **Authors**: Haolin Li, Haipeng Zhang, Mang Li, Zhaohui Xia, Xun Zhu, Miao Li, Yu Zhang, Ji Wu
- **Institution/Company**: Tsinghua University; Alibaba International Digital Commerce Group
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.35323
- **Categories**: cs.IR, cs.CL

**Abstract**: LLM-based personalized search and recommendation repeatedly encode the same item text and grow request inputs with interaction history. CRIM separates item-level semantic encoding from request-level history modeling. A small set of learnable summary tokens compresses each item into compact continuous memories; segment-level readout tokens (REC tokens) add predictive supervision within the history. Because memories are independent of users and queries, they can be cached and reused. At inference, CRIM composes cached memories in interaction order with an optional query. A joint training mechanism combines cached memories with sampled live re-encoding, and periodic refreshes keep the cache consistent. On MovieLens-1M, Qilin, and a new LazSeq dataset, it reports state-of-the-art retrieval with substantially lower inference cost at the same backbone scale.

**Key Innovations**:
- Decouples reusable item memory from request-specific history modeling.
- Compresses each item into a few learnable summary tokens rather than re-reading item text.
- Uses REC readout tokens to inject predictive supervision inside the interaction history.
- Joint cached/live training with periodic refresh to keep the memory consistent.

---

### 1.5 Octen-WebGR: Scaling Generative Retrieval to 200 Million Web Pages
- **Authors**: Guangwei Xu, Wenkai Zhang, Yawen Liu, Dongxu Zhang, Xijie Xu, Kuan Zou
- **Institution/Company**: Octen
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.35256
- **Categories**: cs.IR

**Abstract**: Navigational search must identify one target page among hundreds of millions. Click tables generalize poorly to new query formulations; embedding retrievers generalize across content but often rank navigational targets poorly. Octen-WebGR stores web pages in the parameters of a language model: given a query, it generates a compact **two-token semantic identifier constrained to a table of real URLs**. Octen-WebGR-4B indexes **201 million pages** and is evaluated on real navigational traffic from the month after training. It reaches **59.6% top-1** overall, versus 46.5% for a click-enhanced dense retriever and up to 37.5% for frontier LLMs answering from memory. For unseen queries targeting pages with substantial interaction history, it ranks the correct page first 30.9% of the time versus 17.2% for the dense retriever. The 4B model runs on a single GPU with 10 GB of memory, compared with 412 GB for exact dense retrieval.

**Key Innovations**:
- Two-token semantic identifier constrained to real URLs, enabling direct page retrieval from model parameters.
- 201M-page index in a 4B model with a 10 GB inference footprint.
- Evaluated on post-training real traffic rather than a static click benchmark.
- Documents complementary generalization: generative retrieval wins on new query formulations, dense retrieval on rarely visited pages.

---

### 1.6 MuSID-KD: Multigranularity Knowledge Distillation for Generative Recommendation with Semantic IDs
- **Authors**: Fengshi Zhang, Xiyan Ding, Shuxiao Xie, Wei Zhang
- **Institution/Company**: East China Normal University; Fudan University
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.35218
- **Categories**: cs.AI

**Abstract**: Generative recommendation with semantic IDs predicts the next item as a sequence of discrete tokens, so repeated decoding over SID positions is expensive. Conventional distillation does not fully account for multi-token SID generation: item-level distribution alignment may not preserve the teacher's ranking of candidate groups sharing SID prefixes, and uniform alignment across positions affects final ranking differently. MuSID-KD combines **Hierarchical Candidate Distribution Alignment (HCDA)**, which aggregates item probabilities by shared SID prefixes and aligns distributions from candidate groups down to individual items, with **Ranking Impact Guided Levelwise Distillation (RIGD)**, which allocates supervision by the reduction in pairwise ranking surrogate loss when a student contribution is replaced by the teacher's. Experiments with three lightweight student architectures show improved accuracy and better prefix-marginal and pairwise-ranking alignment without changing online inference architecture.

**Key Innovations**:
- Prefix-aware hierarchical distillation instead of flat item-level distribution matching.
- RIGD allocates supervision by measured pairwise ranking impact per SID position.
- Compatible with multiple lightweight student architectures.
- No change to the student's online inference path.

---

### 1.7 Cross-Domain Sequential Recommendation with Representation-Level User Transfer
- **Authors**: Abdulaziz Samra, Nikita Sukhorukov, Alexey Grishanov, Alexey Vasilev, Evgeny Frolov
- **Institution/Company**: Skolkovo Institute of Science and Technology; Higher School of Economics; AXXX; Sber AI Lab
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.35550
- **Categories**: cs.IR, cs.AI, cs.DC

**Abstract**: Cross-domain sequential recommendation uses source-domain behavior to improve target-domain next-item prediction, but deployment faces isolated interaction data and user heterogeneity. The paper transfers information **only through learned user representations**, without sharing raw interactions or item embeddings. A lightweight adapter projects the source-domain user representation into the target embedding space and integrates it with the target sequence. When source data is unavailable, the model defaults to a target-only sequential recommender while retaining benefits from joint training. Experiments in a benchmark setup and a realistic scalable setup show consistent gains for both shared and unshared users.

**Key Innovations**:
- Representation-only cross-domain transfer that respects business data isolation.
- Lightweight adapter into the target embedding space.
- Graceful fallback to target-only recommendation for users without source activity.
- Evaluated under both benchmark and realistic deployment-oriented conditions (CIKM 2026).

---

### 1.8 MIDA: Multi-Interest Decoding with Adaptive Aggregation for Session-based Recommendation
- **Authors**: Linjiang Guo, Nitin Bisht, Shiqing Wu, Guandong Xu
- **Institution/Company**: University of Technology Sydney; City University of Macau; Education University of Hong Kong
- **Date**: 2026-10-25
- **arXiv**: https://arxiv.org/abs/2610.34192
- **Categories**: cs.IR

**Abstract**: Session-based recommendation degrades when longer histories are available, which the authors associate with decoders that overemphasize recent items and underuse distant but semantically relevant interactions. MIDA is a lightweight, encoder-agnostic reformulation of the decoding stage built on **two-space decoupling**: clustering operates on raw item embeddings so semantic groupings are not distorted by encoder relational biases, while encoder outputs are reserved for aggregation. It uses differentiable multi-interest clustering on raw embeddings and fuses stability and plasticity branches through a gate conditioned on average cluster size, so clustering structure directly governs aggregation. Experiments on multiple benchmarks show consistent gains over state-of-the-art methods at practical cost.

**Key Innovations**:
- Two-space decoupling: semantic clustering on raw embeddings, temporal aggregation on encoder outputs.
- Differentiable multi-interest clustering that preserves semantic structure.
- Cluster-size-conditioned gate coupling clustering structure to aggregation behavior.
- Encoder-agnostic decoder reformulation published in IEEE TKDE.

---

### 1.9 LoopGR: Parameter-Efficient Scaling for Generative Recommendation via Recurrent Depth
- **Authors**: Huizhe Zhang, Yudong Li, Liang Chen, Chengxiang Zhuo, Zang Li
- **Institution/Company**: Sun Yat-sen University; Platform and Content Group, Tencent
- **Date**: 2026-10-25
- **arXiv**: https://arxiv.org/abs/2610.34157
- **Categories**: cs.IR

**Abstract**: Generative recommendation formulates recommendation as autoregressive generation, but scaling is constrained by model size and inference cost. LoopGR adds **recurrent depth** as a scaling dimension: a hierarchical recurrent mechanism alternates between a shared generative decoder and a lightweight context updater, combining expressive history modeling with flexible computational depth without proportional parameter growth. For efficient inference it introduces **recurrent trajectory self-distillation**, distilling a low-budget student from a high-budget teacher by aligning both predictive distributions and evolution directions. LoopGR outperforms strong generative baselines and reduces model size by up to **52%** relative to a representative encoder-decoder baseline.

**Key Innovations**:
- Recurrent depth as a parameter-efficient scaling axis for generative recommendation.
- Shared generative decoder plus lightweight context updater.
- Trajectory self-distillation aligns both predictions and loop evolution directions.
- Up to 52% smaller than an encoder-decoder baseline at better performance.

---

### 1.10 DPE-Rec: Diversity-Preserving and Efficient Diffusion Language Model Recommendation for Bundle Construction
- **Authors**: Pingchuan Ma, Bohan Jiang, Chengshuai Zhao, Dawei Li, Zhen Tan, Huan Liu
- **Institution/Company**: Arizona State University; Stevens Institute of Technology
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.34700
- **Categories**: cs.IR

**Abstract**: Generative bundle construction completes a partial bundle from a large catalog. Diffusion LLMs suit this unordered generation task because bidirectional attention matches unordered bundles and iterative denoising can reveal multiple tokens per step. Two problems arise: confidence-guided decoding postpones semantic-fork decisions, reducing diversity; and revealing more tokens per step can hurt quality. DPE-Rec introduces **semantic-fork-aware GRPO**, which prioritizes semantic-fork decisions via autoregressive rollouts, and **pseudo-trajectory distillation**, which concentrates learning on the subspace visited by high-quality decoding to enable reliable multi-token decoding. It improves recommendation performance by **63% on average**, and its fast variant is **25.6× faster** than existing generative recommendation methods with minimal quality loss.

**Key Innovations**:
- Diffusion LLM formulation for unordered bundle completion.
- Semantic-fork-aware GRPO to protect diversity at decision branch points.
- Pseudo-trajectory distillation to make multi-token decoding reliable.
- 63% average quality gain and 25.6× faster inference for the fast variant.

---

## 2. Advertising, Auctions and Mechanism Design

> The Roblox exploratory creative pre-ranking paper (`2610.36020`) is not repeated here; it is summarized in the [2026-10-29 arXiv Paper Check](../2026-10-29/arxiv-paper-check.md).

### 2.1 A Factor-6 Truthful-in-Expectation Mechanism for Cascade Position Auctions
- **Authors**: Qiuyu Chen, Baao Xie
- **Institution/Company**: Shanghai Jiao Tong University; Ningbo Key Laboratory of Spatial Intelligence and Digital Derivative, Ningbo Institute of Digital Twin, Eastern Institute of Technology
- **Date**: 2026-10-24
- **arXiv**: https://arxiv.org/abs/2610.33707
- **Categories**: cs.GT

**Abstract**: Position auctions assign advertisers to positions and order under cascade behavior, where earlier clicks prevent users from reaching later placements, coupling click probabilities. Prior work achieved constant-factor welfare approximation and monotone logarithmic-factor approximation separately. This paper gives a polynomial-time randomized mechanism that attains both a **factor-6 welfare approximation** and **truthfulness in expectation** for arbitrary public advertiser-position click probabilities. It optimizes a reach-weighted linear relaxation and converts the solution into feasible ordered allocations through matching decomposition, probability-bounded grouping, and calibrated attenuation. The construction makes each advertiser's expected CTR exactly one sixth of its fractional click coordinate, transferring the monotonicity of the fractional allocation to the implemented mechanism, while preserving the welfare guarantee. Allocation and payments are computable in polynomial bit time.

**Key Innovations**:
- Simultaneous constant-factor welfare and truthfulness-in-expectation for general cascade position auctions.
- Reach-weighted LP relaxation plus matching decomposition and calibrated attenuation.
- Exact 1/6 expected-CTR identity transfers monotonicity to the randomized allocation.
- Resolves an open question left by prior cascade-auction work.

---

### 2.2 A Truthful-in-Expectation 2-Approximation for Pair-Specific Cascade Auctions in AI-Generated Content
- **Authors**: Tao Jiang, Minbo Gao, Shaowei Cai
- **Institution/Company**: Key Laboratory of System Software, Institute of Software, Chinese Academy of Sciences; School of Computer Science and Technology, University of Chinese Academy of Sciences
- **Date**: 2026-10-25
- **arXiv**: https://arxiv.org/abs/2610.34236
- **Categories**: cs.GT

**Abstract**: Generative AI interfaces can insert sponsored content at multiple points in an answer, where CTRs depend on the advertiser-position pair. Under the cascade model, users read ads sequentially and stop after the first click, so assignment and order both affect welfare. For arbitrary pair-specific CTRs, prior work gave a 4/(1−ε)-approximation without established monotonicity, and a monotone O(log m)-approximation. This paper gives a polynomial-time mechanism for arbitrary pair-specific CTRs and any limit on displayed ads that is **truthful and individually rational in expectation** and achieves a **2-approximation** to optimal cascade welfare. It selects an advertiser-position matching and a designated last ad, then randomly thins earlier ads so each selected ad's expected cascade CTR is the same fraction of its standalone CTR. This yields a closed-form expected welfare maximized over a bid-independent lottery range by linear programming.

**Key Innovations**:
- 2-approximation with truthfulness in expectation for arbitrary pair-specific CTRs.
- Random-thinning construction equalizes expected cascade CTR as a fixed fraction of standalone CTR.
- Closed-form welfare plus LP over a bid-independent lottery range.
- Shows exactly optimizing the prior welfare surrogate can violate monotonicity.

---

### 2.3 Impossibility of No-Regret in Multi-Agent Bidding
- **Authors**: Zongjun Yang, Rachitesh Kumar, Christian Kroer
- **Institution/Company**: Columbia University; Carnegie Mellon University
- **Date**: 2026-10-27
- **arXiv**: https://arxiv.org/abs/2610.36666
- **Categories**: cs.GT, cs.CC, cs.LG

**Abstract**: The paper considers repeated second-price auctions across n pacing bidders with i.i.d. item arrivals, and shows that it is **computationally impossible for all bidders to achieve no-regret simultaneously** while satisfying budget or return-on-investment constraints. The authors establish a deterministic relationship between high variance in the online bidding system and high regret. By extracting a pacing equilibrium from a low-variance system, they prove **PPAD-hardness** of joint no-regret. For several widely used bidding algorithms, dynamical-systems and numerical evidence show high-variance cycling even on simple market instances.

**Key Innovations**:
- Impossibility result for simultaneous no-regret in budget/ROI-constrained repeated auctions.
- Deterministic high-variance-implies-high-regret relationship.
- PPAD-hardness via reduction from extracting a pacing equilibrium.
- Empirical cycling evidence for common pacing algorithms.

---

### 2.4 Strategyproof Deep Reinforcement Learning for Online Resource Allocation
- **Authors**: Fariba Dehghan, Sebastian Stein, Vahid Yazdanpanah, Stephanie Gauthier
- **Institution/Company**: University of Southampton
- **Date**: 2026-10-27
- **arXiv**: https://arxiv.org/abs/2610.37504
- **Categories**: cs.MA, cs.AI, cs.GT

**Abstract**: Online resource allocation must allocate scarce resources under uncertain demand while ensuring truthful reporting (strategyproofness). RL adapts allocation but does not guarantee strategyproofness; existing strategyproof RL uses a linear allocation rule, while neural mechanism design gives only approximate incentives. This paper introduces the first **strategyproof deep RL mechanism** for online resource allocation. It combines a **monotonic neural network** that learns nonlinear interactions by construction, a **generalized critical payment** (lowest accepted value with other inputs fixed), and training by RL or imitation. On a four-resource stream with interactions a linear rule cannot represent, the neural rule achieves **97.8%** of an offline welfare upper bound versus 93.8% for a linear learner and 89.0% for first-come, first-served. Imitation reaches 97.5% in 261 seconds, about 89× faster than RL.

**Key Innovations**:
- First strategyproof deep RL mechanism for online resource allocation.
- Monotonic neural allocation rule with nonlinear interactions by construction.
- Generalized critical payment preserves strategyproofness and individual rationality.
- Imitation training is ~89× faster than RL at near-identical welfare.

---

## 3. Games and Strategic Agent Evaluation

### 3.1 A Unified Arena for LLM Agents across Diverse Eurogames (DECE)
- **Authors**: Fengrui Zhang, Xiang Li, Ruomeng Ding, Jiayi Yuan, Yuchen Huang, Zhaoyang Han, Xiaoliang Wang, Daoyuan Chen, Yaliang Li
- **Institution/Company**: Alibaba Group; Nanjing University; National University of Singapore; University of North Carolina at Chapel Hill; The Hong Kong University of Science and Technology; Peking University
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.35773
- **Categories**: cs.AI

**Abstract**: Existing game evaluations are confined to individual games or execution frameworks, leaving unclear which competitive advantages persist across settings. DECE is a unified arena spanning **ten Eurogames** with shared interfaces and evaluation protocols. These games combine lasting strategic commitments, competition over shared resources, and multiple victory routes. The primary study evaluates **12 model-harness configurations** (nine models, four harnesses) in 480 three-player matches; the main and supplementary studies total **1,032 matches**. Results show broad cross-game ranking agreement alongside game-specific strengths. The same model can perform differently across harnesses, and performance advantages do not consistently translate into better token or cost efficiency.

**Key Innovations**:
- Standardized ten-game arena with shared interfaces and evaluation protocols.
- Evaluates complete model-harness configurations rather than models in isolation.
- Reports both competitive performance and token/cost efficiency.
- Quantifies harness-induced variance in agent rankings.

---

### 3.2 Build, Don't Play: Self-Improving LLM Research Agents Develop a Hearthstone Battlegrounds AI That Rivals Top Players (AutoTavern)
- **Authors**: Changlian Ma, Limin Wang
- **Institution/Company**: Nanjing University; Shanghai AI Laboratory
- **Date**: 2026-10-24
- **arXiv**: https://arxiv.org/abs/2610.33845
- **Categories**: cs.AI, cs.LG, cs.MA

**Abstract**: AutoTavern is a self-improving research system for Hearthstone Battlegrounds, an eight-player auto-battler with stochastic shops, hidden information, and nearly a thousand interacting cards. Specialized LLM research agents share a typed research memory, every claim passes verification gates, and live games close the loop, so the agents improve the simulator, opponents, policy, and their own research process; a human sets goals and rules on ambiguous mechanics. In **20 days**, AutoTavern built TavernGym, a full-content reproduction of the live game, and delivered **23 versions of TavernAgent** trained with PPO. TavernAgent plays complete games on the live ladder: its rating rose from 6,000 to about **15,000**, and its last 20 records average a placement of 1.60 with 80% first places, better than the server's ten highest-rated players on every statistic (2.34, 59%). On TavernBench (960 tasks, 40 scenarios), TavernAgent answers 91% of play tasks versus at most 63% for frontier LLMs, and decides in 0.03 s where they need up to 26 s.

**Key Innovations**:
- Typed shared research memory plus verification gates for multi-agent research.
- Live-game feedback closes the loop across simulator, opponents, policy, and research process.
- Full-content game reproduction and 23 PPO policy versions in 20 days.
- Large behavioral gap: agents build far better than they play.

---

### 3.3 Text Is the Bottleneck: A Small-Scale Replication of LLM Game Playing in Riichi Mahjong
- **Authors**: Mingge Xu
- **Institution/Company**: Department of Bioengineering, Graduate School of Engineering, The University of Tokyo
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.34791
- **Categories**: cs.CL

**Abstract**: The paper replicates the riichi-mahjong track of "Can Large Language Models Master Complex Card Games?" under a much smaller budget: at most 2B parameters, one 16 GB consumer GPU, about five GPU-days. With matched data and labels, **text is the bottleneck**: a 2.6M-parameter convolutional board encoder agrees with the strong AI Mortal on 80.6% of test decisions, above every text-prompt LLM (best 77.8%), and places better at the table (2.85 over 1,000 games vs. ~3.0). Scaled to 1.71M decisions and distilled from Mortal's Q-values, a 4.9M-parameter Transformer reaches **94.7%** agreement, beats 0.8B LLMs on identical seeds, and is statistically equivalent to parity against three Mortal champions. Training toward the teacher raises teacher agreement more than a 2.5× parameter increase (+2.5 vs. +1.5 points), but neither effect is visible at the table. The paper also documents a paper-code mismatch in the original winner filter and reconstructs its two private engine patches.

**Key Innovations**:
- Small-budget replication that isolates representation (text vs. board state) from scale.
- Matched-data comparison showing a tiny board encoder beats larger text-prompt LLMs.
- Q-value distillation reaches teacher parity with a 4.9M-parameter Transformer.
- Documents agreement-vs-playing-strength decoupling and original paper-code mismatch.

---

### 3.4 Game-Theoretic Solvers with Bayesian Opponent Modeling and Moral Rhetoric Framing for GLEE
- **Authors**: Hayden Arnold
- **Institution/Company**: KAIST
- **Date**: 2026-10-27
- **arXiv**: https://arxiv.org/abs/2610.37397
- **Categories**: cs.GT, cs.CL

**Abstract**: The paper describes the agent submitted to the GLEE competition, which plays bargaining, negotiation, and persuasion games against human and AI opponents. It combines a **classical game-theoretic solver** for numeric moves, an **online Bayesian layer** for opponent archetypes, and a **language model** for messages. It uses Rubinstein bargaining, Faratin concession, and Kamenica–Gentzkow disclosure, adapting them with a Bayesian estimate of hidden discount factor, reservation value, or signaling reliability, plus a Thompson-sampling bandit over five moral-foundation framings. Evaluation covers **13,200 Monte Carlo games** against 11 synthetic archetypes, an ablation of opponent modeling, and **9,337 live-game messages**; moral rhetoric framing in persuasion is strongly correlated with purchase (χ² = 616.7, p ≈ 3.7×10⁻¹³²), surviving controls for quality, round, and configuration.

**Key Innovations**:
- Hybrid architecture separating numeric game-theoretic moves from LLM-generated rhetoric.
- Online Bayesian adaptation of opponent discount factor, reservation value, and signaling reliability.
- Thompson-sampled moral-foundation framing for message register.
- Reports failure modes where theoretically optimal policies underperform live.

---

## 4. LLM Agents, Memory and Self-Improvement

### 4.1 Infinity Machine: A Self-Improving AI Agent for Research
- **Authors**: Harish Santhanalakshmi Ganesan
- **Institution/Company**: Independent researcher
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.35579
- **Categories**: cs.AI

**Abstract**: Infinity Machine is a self-improving research agent for problems whose answers a program or data can check. Each candidate solution is produced by a full tool-using agent working up to an hour in a fresh sandbox; proposers see only a public score, and a private split decides what counts. The harness itself (prompts, tools, skills, playbook, meta agent) is an **editable genome**, changed only through a kernel-enforced gate with held-out and cost checks. In autonomous mode, an agent picks an open problem and writes its verifier, the kernel calibrates it, an adversarial agent audits it, and an agent that never sees the verifier re-checks the result. Across **14 problems in six days** for about **$180** of model usage, it produced four results beyond published state of the art in quantum information, including a certified depolarizing-channel threshold and a 44-gate Golay state preparation. It also cut SABRE qubit-routing overhead from 68,559 to 12,087 added gates and reduced energy per MAC of an open 8×8 INT8 systolic tile by 77.7%. The paper documents failures as well: gamed lenient scorers four times, one rejected harness generation, and one agent-written score pointing the wrong way.

**Key Innovations**:
- Harness-as-genome with kernel-enforced held-out and cost gates.
- Autonomous problem selection, verifier writing, adversarial audit, and blind re-check.
- Cost-bounded research loop (~$180 over six days).
- Unusually explicit failure reporting alongside SOTA results.

---

### 4.2 Skill∞: Recursive Self-Improvement for Agent Skill Optimization
- **Authors**: Wangcheng Tao, Zhanglu Yan, Han Wu, Weng-Fai Wong
- **Institution/Company**: National University of Singapore; City University of Hong Kong
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.35434
- **Categories**: cs.AI, cs.CL

**Abstract**: Recursive self-improvement (RSI) requires a system to improve the way it improves. Language agents increasingly store procedural knowledge in reusable skills, and skill optimization is a direct route to RSI because the optimization procedure itself can be encoded as a skill. Existing optimizers use hand-designed procedures or confine a meta-skill to a fixed pipeline and relearn it per task. Skill∞ makes skill optimization recursively self-improving: a **meta agent follows a meta-skill to optimize task skills and optimizes the meta-skill itself using the same procedure**. The meta agent diagnoses execution traces, proposes candidates, requests independent reviews, and allocates search budget; the meta-skill defines these steps and can rewrite them. The meta-skill is decoupled from task skills and reused across domains. On **83 SkillsBench tasks**, Skill∞ reaches a **60.7% pass rate**, versus 56.4% for human-curated skills and 54.5% for SkillEvolver.

**Key Innovations**:
- Meta-skill optimized by the same optimization procedure it defines.
- Agent-led diagnosis, proposal, independent review, and budget allocation.
- Decoupled meta-skill reusable across task domains.
- Standard skill-package interface for both levels.

---

### 4.3 EvoRouter: Cost-Efficient Multi-Agent Routing via Insight-Guided On-Policy Distillation
- **Authors**: Yitao Xiao, Xu Zhang, Ye Cheng, Shaoyong Guo, Yan Sun, Ziyue Zhu, Sitao Xie, Guo Tong, Haoran Luo
- **Institution/Company**: Beijing University of Posts and Telecommunications; Fudan University, Shanghai Innovation Institute; Nanyang Technological University
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.35690
- **Categories**: cs.AI, cs.MA

**Abstract**: Serving web queries with multi-agent systems requires configuring models, collaboration modes, agent counts, interaction rounds, and skills, producing a combinatorial space with sparse execution rewards. EvoRouter is a self-evolving routing framework driven by insight-guided on-policy distillation. A dedicated expert periodically synthesizes performance-cost feedback from configuration trajectories into reusable **conditional routing insights** about capability requirements, returns from resource scaling, and configuration interactions. A privileged teacher combines these insights with current execution feedback to provide dense token-level supervision to the router through on-policy distillation. Cost-aware RL jointly optimizes task performance and compute. On **19 in-domain datasets** across five domains and two out-of-domain benchmarks, EvoRouter reaches **68.69%** average in-domain accuracy, **+7.23 percentage points** over the strongest routing baseline, while reducing inference compute cost by **50.95%**.

**Key Innovations**:
- Reusable conditional routing insights distilled from configuration trajectories.
- Privileged teacher plus on-policy distillation for dense supervision of sparse routing rewards.
- Cost-aware RL over joint performance and compute.
- Execution-driven self-improvement loop that regenerates trajectories for insight extraction.

---

### 4.4 Rare, Relevant, and Still Wrong: How Memory Fails LLM Group Decisions (CrossProfile)
- **Authors**: Anouar Imel, Imad Charradi, Abderrahman Sghir, Khalil El Khammar
- **Institution/Company**: University of Electronic Science and Technology of China; Xidian University; Nanjing University of Aeronautics and Astronautics; Nanjing University of Information Science and Technology
- **Date**: 2026-10-27
- **arXiv**: https://arxiv.org/abs/2610.37624
- **Categories**: cs.AI, cs.CL, cs.MA, cs.SI

**Abstract**: When an LLM group's discussion is compressed into a short memory, should the memory keep the rarest claims or the claims relevant to decision criteria? On hidden-profile tasks both heuristics look attractive because fact prevalence is confounded with usefulness. CrossProfile is a diagnostic benchmark of **60 templates** with automatically verified answer keys, in which ownership of supporting, decoy, and irrelevant facts is crossed while text is held fixed (**480 tasks**). Across Qwen2.5-7B, Llama-3.1-8B, and two DeepSeek models, both heuristics fail predictably: relevance-based selection readmits on-topic decoys, losing 23–31 points to rarest-first in the classic hidden-profile configuration, while rarest-first is no better than random on average and wins only where rare facts happen to be useful. Accuracy follows the **balance of evidence** the memory keeps, not the selection policy. The decision model adds a social-proof failure: weighting facts attributed to many agents hurts, and removing or randomly reassigning attribution tags raises accuracy by 13–24 points. In natural discussions, the complete transcript yields lower accuracy than no notes at all.

**Key Innovations**:
- CrossProfile benchmark that disentangles fact prevalence from decision usefulness.
- Shows both rarity- and relevance-based memory selection fail in predictable regimes.
- Identifies balance-of-evidence as the variable that actually predicts accuracy.
- Quantifies social-proof bias from agent attribution tags.

---

### 4.5 TANDEM: Balancing Centralized and Decentralized Critics to Address the Information Gap in Complex Multi-Agent Environments
- **Authors**: Alireza Saleh Abadi, Leen-Kiat Soh, Adam Eck, Prashant Doshi
- **Institution/Company**: University of Nebraska-Lincoln; Oberlin College; University of Georgia
- **Date**: 2026-10-27
- **arXiv**: https://arxiv.org/abs/2610.37592
- **Categories**: cs.MA

**Abstract**: Cooperative multi-agent RL under centralized training with decentralized execution (CTDE) shapes decentralized policies with a centralized critic, then removes the critic at execution. The resulting information gap widens under partial observability, observation noise, and openness. Existing methods transfer centralized guidance in one direction only, so policies never rehearse acting without the critic while corrections are still available. TANDEM keeps one centralized critic and reads it two ways at each training step: a **centralized read** from the global state and a **decentralized read** restricted to what each agent will have at execution. A parameter-free gate compares the reads per agent and trains on the decentralized read where they agree, reinstating the centralized read only where the local view is misleading; a shared target pulls the decentralized read toward the centralized one. The setting is formalized as a task- and agent-open Dec-POMDP. TANDEM is best on **8 of 9 setups** and never significantly worse than any of six CTDE baselines.

**Key Innovations**:
- Dual-read critic: centralized and execution-available views at every step.
- Parameter-free gate decides which read supervises each agent.
- Shared target aligns the decentralized read with the centralized one.
- TAO-Dec-POMDP formalization covering partial observability, noise, and openness.

---

### 4.6 Learning to Remember: Advances in Memory Mechanisms for Large Language Models
- **Authors**: Chenye Han, Hongche Yu, Mengyue Wu, Dell Zhang, Jixiang Luo
- **Institution/Company**: Shanghai Jiao Tong University; Institute of Artificial Intelligence, China Telecom (TeleAI); XSci, London
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.35089
- **Categories**: cs.IR

**Abstract**: This survey organizes LLM memory around three dimensions: the **life cycle of memory**, the **storage substrate**, and the **system role** memory plays in LLM-based agents, using cognitive-science concepts as motivation rather than as a separate mechanism family. It distinguishes three mechanism families: **nonparametric memory** (text, graph, multimodal, or database-like structures outside parameters), **parametric memory** (activations, KV caches, learned modules, adapters, or weights), and **memory for agent evolution** (stored experience supporting RL, continual learning, procedural reuse, context engineering, and harness design). Evaluation is treated as a cross-cutting component rather than a memory mechanism. Unlike RAG- or long-context-centric surveys, it emphasizes the full life cycle: construction, maintenance, retrieval, consolidation, forgetting, governance, and evaluation.

**Key Innovations**:
- Three-axis taxonomy: life cycle, storage substrate, system role.
- Separates nonparametric, parametric, and agent-evolution memory.
- Treats evaluation and governance as cross-cutting rather than an afterthought.
- Maps benchmarks and deployment concerns onto the same framework.

---

## 5. Sequential Modeling and Dialogue

### 5.1 BehaviorMem: Building and Evaluating User Memory from Real-World E-Commerce Behavior Streams
- **Authors**: Sizhe Wang, Xinghao Fang, Rui Qiu, Zhenjia Ma, Dagui Chen, Kun Kuang, Hongcheng Guo
- **Institution/Company**: Fudan University; Zhejiang University; Taobao & Tmall Group, Alibaba
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.34790
- **Categories**: cs.CL

**Abstract**: E-commerce users express preferences through explicit language and implicit product interactions. Existing memory methods target language interactions and offer limited real behavioral data and limited separation of **remembering** concrete evidence from **inferring** unobserved needs. The paper formulates continual behavioral user memory around these joint requirements. **BehaviorMemBench** is built from real e-commerce logs covering **1,194 users** and **17,462 behavioral batches** over more than three years, with automatic future-behavior labels and a task-independent memory interface that evaluates remembering and inference separately. **BehaviorMem** organizes explicit behavioral facts and inferred user characteristics across long-term and short-term scopes in a two-axis state, with evidence-grounded formation, continual maintenance, and query-independent readout. Across two builders and two task readers it leads evaluated agentic memories on both remember and infer, and validation on a public dataset supports downstream usefulness.

**Key Innovations**:
- Separates memory "remembering" from behavioral "inference" in both benchmark and method.
- Three-year real e-commerce log benchmark with automatic future-behavior labels.
- Two-axis state: explicit facts vs. inferred characteristics, long- vs. short-term.
- Query-independent readout so memory can be reused across downstream tasks.

---

### 5.2 CoLink: Global Compression and Knowledge Linking for Multi-Turn Dialogue Modeling
- **Authors**: Lian Yan, Zhenbo Xia, Haotian Wang, Chen Tang, Yi Guan, Jie Liu, Jingchi Jiang
- **Institution/Company**: Harbin Institute of Technology; Institute for Advanced Algorithms Research, Shanghai
- **Date**: 2026-10-25
- **arXiv**: https://arxiv.org/abs/2610.34335
- **Categories**: cs.CL, cs.AI

**Abstract**: Extracting salient information from long-horizon dialogue remains difficult because of context limits, information loss, retrieval redundancy, and myopic attention. CoLink clusters historical contexts into **topic graphs** to establish cross-semantic associations with external knowledge, then retrieves and activates knowledge by combining semantic relevance with graph-structural topology under adaptive control of thought. It grounds multi-turn dialogue in information theory to derive an objective for extracting core sense-making information, and uses a competitive slot mechanism to condense the global context into dedicated memory and knowledge slots. Experiments on public and MMD datasets support its superiority and generalizability in knowledge linking and sense modeling.

**Key Innovations**:
- Topic-graph organization of dialogue history linked to external knowledge.
- Retrieval that fuses semantic relevance with graph topology.
- Information-theoretic objective for core sense-making extraction.
- Competitive slot mechanism for compact global memory and knowledge representation.

---

## 6. LLM Architecture, Training and Theory

### 6.1 LoopFold: Parallelizing Recurrent Depth in Looped Transformers
- **Authors**: Feichen Song, Boyi Zeng, Yiqin Hao, Shixiang Song, He Li, Yizhou Yang, Zitong Wang, Yifan Liu, Ziwei He, Zhouhan Lin
- **Institution/Company**: Shanghai Jiao Tong University; Sun Yat-sen University; Shanghai Innovation Institute
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.35556
- **Categories**: cs.CL

**Abstract**: Looped Transformers increase computation per token by repeatedly applying a shared backbone, but each loop depends on the previous one, so recurrent depth increases decoding latency. Parallel Loop Transformers overlap loop computation across token positions but show diminishing accuracy gains at larger depths. LoopFold **folds computation at multiple recurrent depths into parallel batches for the same token prefix**. A lightweight predictor estimates inputs to later loops so they can start before earlier loops finish; a corrector refines later-loop outputs using newly available earlier results. All components are trained jointly with only the final next-token prediction loss. With 1.4B models, deeper LoopFold configurations improve average zero-shot accuracy across eight tasks from **53.41% to 56.38%**. Compared with a nine-loop vanilla model, LoopFold uses **five sequential stages** and reduces decoding latency by **46%**.

**Key Innovations**:
- Folds multiple loop depths into parallel batches for the same prefix.
- Predictor starts later loops early; corrector repairs them with earlier results.
- Joint training with only the final next-token loss.
- 46% lower decoding latency with five sequential stages versus nine vanilla loops.

---

### 6.2 StateLoop: Persistent State for Looped Transformers
- **Authors**: Feichen Song, Boyi Zeng, He Li, Shixiang Song, Yiqin Hao, Zitong Wang, Yizhou Yang, Yifan Liu, Ziwei He, Zhouhan Lin
- **Institution/Company**: Shanghai Jiao Tong University; Sun Yat-sen University; Shanghai Innovation Institute
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.35544
- **Categories**: cs.CL

**Abstract**: Vanilla looped Transformers pass each backbone output directly to the next iteration, so retaining information across the loop depends entirely on the single hidden state. StateLoop maintains **one additional persistent state per token** across iterations. At each iteration, a learned gate controls how much previous state is retained and how much backbone output is incorporated; the updated state is projected back and added to the backbone output for subsequent iterations and final prediction. StateLoop reduces Pile perplexity and improves average accuracy across **eight zero-shot tasks** over vanilla looped models. Its perplexity advantage grows with trained loop depth, consistent with persistent state becoming more useful as recurrent computation deepens.

**Key Innovations**:
- Per-token persistent state carried across loop iterations.
- Learned gate balances state retention against new backbone information.
- Projected state is added back to the backbone stream for later loops and prediction.
- Gains scale with trained loop depth.

---

### 6.3 Quantitative Generalization Bounds for Multi-Layer Transformers: A Few Long Strings can Beat Many Short Ones
- **Authors**: Marius Henry, Michael Rizvi-Martel, Michael Hahn
- **Institution/Company**: LaCoCo, Saarland University; Mila & Université de Montréal; Zuse School ELIZA
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.35715
- **Categories**: cs.LG, cs.AI, cs.CL

**Abstract**: Transformer generalization has two axes that are usually studied separately: in-distribution statistical generalization and length generalization. This paper gives a **joint treatment** for fixed-precision transformers. It derives generalization guarantees in terms of parameter sizes, the quantization space, and the alphabet size that supplies the sequences, and illustrates the trade-off between sample count and training length. In particular, it finds that **increasing training length can be exponentially more efficient than increasing the sample size**. Experiments support the theoretical predictions.

**Key Innovations**:
- Joint bounds covering both in-distribution and length generalization.
- Quantitative dependence on parameter size, quantization, and alphabet size.
- Shows longer training sequences can be exponentially more sample-efficient than more short samples.
- Theory-to-experiment validation of the predicted trade-off.

---

### 6.4 An Algorithmic Account of Few-Shot Concept Induction in Language Models (ADA)
- **Authors**: Michael A. Lepori, Laila Johnston, Aalok Sathe, Zhuonan Yang, Roman Feiman, Ellie Pavlick
- **Institution/Company**: Brown University
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.35533
- **Categories**: cs.CL

**Abstract**: Models and minds can represent not only features of an entity but which features are relevant in a context. The paper proposes **Amortized Direction Accentuation (ADA)**, an algorithmic hypothesis for how relevance is determined in few-shot concept induction, the ability to infer a latent concept from a small number of positive examples. Under ADA, concept induction forms a summary representation of the examples in a feature space shaped by **amortized knowledge about which features tend to be useful for finding commonalities** between items. The hypothesis is investigated and validated in language models using a few-shot concept induction task, offering a mechanistic perspective on contextualization and a candidate account of a core cognitive capability.

**Key Innovations**:
- ADA algorithmic hypothesis for few-shot concept induction.
- Amortized prior over which feature directions are useful for commonality detection.
- Validated mechanistically in language models rather than only behaviorally.
- Bridges in-context learning and cognitive accounts of relevance representation.

---

## Cross-cutting observations

1. **Efficiency is being pursued at different layers of the stack.** CRIM removes repeated item encoding, Octen-WebGR replaces a 412 GB dense index with a 10 GB model, LoopGR reduces parameters by 52%, DPE-Rec cuts inference steps by 25.6×, and LoopFold reduces loop latency by 46%. These are not competing claims; they target memory, index size, parameter count, denoising steps, and sequential depth respectively.
2. **Several papers attack evaluation validity rather than model quality.** Phantom correlation shows a similarity metric can measure activity volume; CrossProfile shows memory-selection heuristics can track fact ownership rather than usefulness; the Riichi replication shows agreement gains need not translate into playing strength; DECE shows harness choice shifts rankings. The common lesson is that benchmark gains need a stated causal pathway.
3. **Auction theory is moving toward deployable generality.** The two cascade-auction papers handle arbitrary pair-specific CTRs rather than factorized models, while the no-regret impossibility result explains why budget-constrained auto-bidding markets should not be expected to converge to jointly optimal behavior. Together they set expectations for what a real ad platform can guarantee.
4. **Self-improvement is being operationalized as harness and skill optimization.** Infinity Machine edits its own prompts/tools/skills behind held-out and cost gates; Skill∞ optimizes the meta-skill that optimizes task skills; EvoRouter distills routing insights back into its policy. The shared safety mechanism is an external check the optimizer cannot edit.
5. **Game environments are becoming agent system benchmarks.** AutoTavern, DECE, GLEE, and the Riichi replication all evaluate complete pipelines under stochasticity, hidden information, and live opponents. The recurring finding is that the model is only one component: harness, memory, verification, and representation can dominate.
