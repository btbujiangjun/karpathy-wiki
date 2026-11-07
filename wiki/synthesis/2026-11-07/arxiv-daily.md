---
title: "arXiv Daily — AI / LLM / Recommendation / Advertising / Sequential Modeling / CTR / Games (2026-11-07)"
type: synthesis
created: 2026-11-07
updated: 2026-11-07
sources: [arxiv.org, https://arxiv.org/list/cs.IR/recent, https://arxiv.org/list/cs.CL/recent, https://export.arxiv.org/api/query]
tags: [arxiv-daily, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, generative-recommendation, semantic-ids, reranking, user-modeling, decision-models, game-theory, linear-attention, sparse-attention, speculative-decoding, kv-cache, test-time-compute, agents, rl, daily-digest]
---

# arXiv Daily — 2026-11-07

> **Window**: arXiv category pages show **Fri, 6 Nov 2026** as the latest listing day (checked `cs.IR`/`cs.CL` on 2026-11-07); the Atom export snapshot used for screening was `2026-11-06T23:46Z` with newest submissions dated **2026-11-05** (small tail 2026-11-04). No 2026-11-07 announcement block is visible at run time.
> **Method**: `export.arxiv.org` Atom API (newest-first) plus live `arxiv.org/list` checks for `cs.IR`/`cs.CL`; abstract-level screening across AI, LLM, recommendation, advertising/CTR, sequential modeling, and games/decision topics. Numbers are **author-reported** and not independently reproduced.
> **Affiliation discipline**: arXiv metadata often omits affiliations. Institutions below are taken from paper text/comments only when unambiguous; otherwise marked **not stated on arXiv (inferred/tentative where noted)**.
> **Dedup note**: several IDs overlap with `wiki/synthesis/2026-11-07/arxiv-paper-check.md` from the same batch; overlaps are included here when they are central to the requested domains and are noted inline.

---

## 1. Recommendation, Advertising & CTR

### 1.1 Beyond Independent Predictions: Learning the Browsing Journey for Sequence-Level Re-ranking (ICE)
- **Authors**: Jiayi Zhang, Jingxin Hai, Zhenjia Ma, Hongbin Pei, Dagui Chen, Han Zhu, Jian Xu
- **Institution / Company**: Not stated on arXiv (Taobao/Alibaba production context inferred from 14-day Taobao App A/B and full-traffic deployment)
- **Published**: 2026-11-05 · cs.IR · [arXiv:2611.07591](https://arxiv.org/abs/2611.07591)
- **Abstract**: Re-ranking in industrial Generator–Evaluator systems selects a displayed list by scoring candidate sequences, but common evaluators use Independent Behavior Modeling (IBM), predicting per-item outcomes such as CTR independently. IBM ignores that a click requires the item to be reached and impressed and that items compete for finite user attention, producing biased utility estimates. The paper proposes Joint Behavior Modeling (JBM), which models the display → impression → click process. Its Impression-Click Evaluator (ICE) predicts a browsing-depth distribution for per-position impression probabilities, uses impressions to suppress context from unexposed items during click modeling, and adds a click-distribution matching objective for intra-sequence dependencies. Experiments across backbones and a 14-day Taobao A/B test (+0.70% clicks, +3.67% revenue) followed by full deployment support the approach.
- **Key innovations**:
  - Replaces independent CTR-style scoring with an explicit **display → impression → click** causal process.
  - Uses **browsing-depth/impression probabilities** to mask unexposed items in click modeling.
  - Adds **click-distribution matching** to capture sequence-level competition/dependencies.
  - Production evidence: **+0.70% clicks, +3.67% revenue** (Taobao, 14-day A/B) and full traffic.

### 1.2 BRIDGE: Bridging the Semantic Quantization Gap for Generative Recommendation
- **Authors**: Yatong Xiao, Mingjie Sun, Peng Wang, Wenjin Wu, Peng Jiang
- **Institution / Company**: Not stated on arXiv (large-scale e-commerce advertising platform inferred from online A/B)
- **Published**: 2026-11-05 · cs.IR · [arXiv:2611.07425](https://arxiv.org/abs/2611.07425)
- **Abstract**: Generative recommenders generate hierarchical Semantic IDs (SIDs) from RQ-VAE tokenizers. The paper identifies a Semantic Quantization Gap (SQG): quantization uses continuous codebook centroids, neighborhood geometry, and level-wise entropy, but the decoder receives only discrete IDs. This causes grounding, neighborhood, and difficulty-allocation gaps. BRIDGE injects frozen quantizer centroids as semantic anchors before SID generation, transfers neighborhood-aware knowledge from a privileged EMA teacher to an on-policy student via self-distillation, and allocates recurrent computation more heavily to early, harder SID levels. On three Amazon benchmarks it improves Recall@10/NDCG@10 by 10.9%/9.7% on average over the strongest baseline; a one-week 5%-traffic A/B on a large e-commerce ads platform improves eCPM by 0.65%.
- **Key innovations**:
  - Diagnoses **SQG** between continuous quantizer geometry and discrete SID decoding.
  - **Codebook-grounded latent reasoning** provides frozen centroid anchors before generation.
  - **Privileged EMA self-distillation** preserves neighborhood structure and mitigates exposure bias.
  - **Effort-aware recurrence** focuses compute on harder early SID levels; **+0.65% eCPM** online.

### 1.3 OptST: Optimizing Semantic Tokenization for LLM-Enhanced Recommendation
- **Authors**: Hanchong Chen, Jie Liu, Fuyuan Lyu, Dugang Liu, Lingjie Li, Xiuqiang He, Xing Tang
- **Institution / Company**: Not stated on arXiv (author affiliations not in abstract page metadata)
- **Published**: 2026-11-05 · cs.IR · Accepted to Findings of WSDM 2027 · [arXiv:2611.07523](https://arxiv.org/abs/2611.07523)
- **Abstract**: Semantic tokenization converts LLM-derived user profiles into discrete tokens, but the usual two-stage pipeline freezes the tokenizer before recommendation training, preventing downstream supervision from revising semantic partitions. OptST makes a pretrained tokenizer task-aware without directly updating its encoder or base codebooks. It learns a low-rank deformation of codebook assignments constrained by an anchor regularizer; recommendation supervision reaches the transformation through a straight-through estimator while inference keeps hard nearest-code assignments. OptST also selects an interaction-conditioned prefix to control how much residual semantic detail is exposed per interaction. Experiments on four public datasets show the highest AUC among conventional and LLM-enhanced baselines, with gains persisting across recommender backbones.
- **Key innovations**:
  - Makes semantic tokenization **downstream-task-aware** while keeping pretrained encoder/base codebooks fixed.
  - **Low-rank assignment deformation + anchor regularizer** balances adaptation and geometry preservation.
  - **Straight-through estimator** bridges discrete nearest-code assignment and recommendation loss.
  - **Interaction-conditioned prefix** adapts semantic resolution per sample.

### 1.4 What Gets Hacked in a Collaborative Reward for LLM Recommenders
- **Authors**: Zhuangsheng Li, Liang Dong, Yu Wu, Dailin Li, Yu Xia, Yunhan C. Zhang, Rui Cai, Yi Wu, Julian McAuley
- **Institution / Company**: Not stated on arXiv
- **Published**: 2026-11-05 · cs.IR · [arXiv:2611.07588](https://arxiv.org/abs/2611.07588)
- **Abstract**: Collaborative-filtering (CF) scores can serve as graded RL rewards for LLM recommenders, but they can induce exposure collapse: the CF model's own top lists are diverse, yet an LLM optimized on its rewards concentrates on fewer items. The paper decomposes each CF score into an item-mean component and a user-specific residual; controlled interventions identify the item-mean as a collapse driver. Two corrections are proposed: per-item centering removes each item's estimated mean, and per-item standardization further rescales the residual by its estimated standard deviation. Across two datasets and two identifier schemes, the corrections substantially improve catalog coverage and exposure evenness, increasing distinct items ranked first by up to 9.8× while maintaining comparable ranking accuracy.
- **Key innovations**:
  - Decomposes CF reward into **item-mean** and **user-specific residual**; isolates item-mean as collapse driver.
  - Simple fixes: **per-item centering** and **per-item standardization** of CF rewards.
  - Up to **9.8× more distinct first-ranked items** with comparable ranking accuracy.
  - Actionable diagnostic for RLHF/RL-style training of LLM recommenders.

### 1.5 From Waste to Discovery: Recycling High-Scored Unexposed Candidates in Taobao Feed Recommendation (URED)
- **Authors**: Ge Fan, Kai Meng, Huiping Chu, Yuning Jiang, Han Zhu, Bo Zheng
- **Institution / Company**: Alibaba Group / Taobao feed (production deployment stated; affiliation not printed on arXiv)
- **Published**: 2026-11-04 · cs.AI, cs.IR · [arXiv:2611.05997](https://arxiv.org/abs/2611.05997)
- **Abstract**: URED is a training-free recall-stage system for Taobao feed recommendation, deployed for over six months. It argues that naive exploration boosts inject cold, information-poor candidates that rankers overestimate. Instead, it aggregates items that were scored highly but never exposed over a 30-day horizon and re-injects them at recall time through offline storage, distributed aggregation, and low-latency online serving (one O(1) lookup per request, <1% latency, no retraining). Online A/B tests show +3.47% discovered categories and +8.47% content richness with engagement preserved; completion video views rise +2.62%. Ablations show a one-day window and random score-unfiltered injection fail to deliver the gain. URED reaches 13.9× the platform-average discovery rate while keeping engagement quality near platform average.
- **Key innovations**:
  - Treats **high-scored unexposed items** as a reliable exploration pool, not waste.
  - **Training-free recall pipeline** with 30-day aggregation and O(1) online lookup (<1% latency).
  - Production A/B: **+3.47% discovered categories, +8.47% richness, +2.62% completion views**.
  - Strong ablations on aggregation horizon and score filtering.

### 1.6 Do Recommenders Need to Think in Words? Latent Reasoning for Efficient LLM-Based Recommendation (LatentRec)
- **Authors**: Hongyang Su, Beibei Kong, Lei Cheng, Chengxiang Zhuo, Zang Li
- **Institution / Company**: Not stated on arXiv
- **Published**: 2026-11-05 · cs.CL · CIKM 2026 (Short Paper) · [arXiv:2611.07866](https://arxiv.org/abs/2611.07866)
- **Abstract**: LLM recommenders often generate chain-of-thought text before item prediction, adding inference cost. LatentRec replaces inference-time reasoning artifacts with training-time supervision. A 2.5M-parameter Continuous Thought Module iterates latent reasoning steps over the LLM hidden state during training; Soft Token Selection bridges the norm gap between hidden states and input embeddings; a Per-step Reasoning Loss supervises every intermediate state through the LLM prediction head against the first token of the target Semantic ID. The module is discarded at deployment. On three Amazon benchmarks, LatentRec improves HR@10 by 4.0–5.0% relative over a CoT-distilled baseline at 18.3× lower latency (batch=1).
- **Key innovations**:
  - Moves reasoning cost from **inference-time CoT** to **training-time latent supervision**.
  - **Continuous Thought Module + Soft Token Selection + Per-step Reasoning Loss**.
  - Deploy-time module removal preserves accuracy; **+4.0–5.0% relative HR@10, 18.3× lower latency**.

### 1.7 Generative Retrieval under Real-Time Supply Constraints in Local Commerce (RTP-LLM)
- **Authors**: Shaopeng Liang, Biao Zhang, Hongzhen Ye, Zeyang Hou, Ma Jiang, Jintao Tu, yunxi.hz, Zhijia Fang, Jianqiang Cao, Junxue Rao, Jia Jia
- **Institution / Company**: Not stated on arXiv (local retail/food-delivery setting; Meituan-style context tentatively inferred from paper title/comments context in batch, but not confirmed on abstract page)
- **Published**: 2026-11-04 · cs.IR · [arXiv:2611.06323](https://arxiv.org/abs/2611.06323)
- **Abstract**: In local commerce, generative retrieval must respect request-time serviceability (location, weather, traffic), not just catalog validity. RTP-LLM compiles eligible residual-quantization identifiers into a compressed sparse row prefix index, overlaps CPU compilation with model prefill, and shares the index across beams. Legal expansions keep original log probabilities and constraint states follow selected beam parents. The paper formalizes snapshot-relative identifier validity versus entity-level eligibility/freshness. In a matched-beam daily-constraint case, filtered merchants drop from 170/299 to 29/299; a different-host comparison reports 0.6 ms service-side latency increment. The authors note measurements span development stages and do not establish compute savings at matched retrieval quality.
- **Key innovations**:
  - Makes **request-time supply snapshots** first-class in generative retrieval.
  - **Compiled prefix index** for legal SID expansions, with CPU/prefill overlap and beam sharing.
  - Distinguishes **snapshot-relative validity** from catalog eligibility/freshness.
  - Practical latency evidence, with explicit caveats about matched-quality compute savings.

---

## 2. Sequential Modeling, Search & Ranking Behavior

### 2.1 Deliberate Latent Reasoning for Sequential Recommendation (DESRec)
- **Authors**: Haobo Zhang, Qiannan Zhu, Yutao Zhu, Zhicheng Dou
- **Institution / Company**: Not stated on arXiv (Renmin University of China tentatively inferred from author group; not confirmed on abstract page)
- **Published**: 2026-11-04 · cs.IR · [arXiv:2611.06521](https://arxiv.org/abs/2611.06521)
- **Abstract**: Sequential recommenders with latent reasoning often use a fixed number of reasoning steps for all histories, causing over-thinking on simple sequences and under-thinking on complex ones. DESRec performs personalized latent reasoning. It selects an optimal reasoning step per sequence during training and uses self-distillation to compress that informative state into the final inference state. It also segments user history into a variable number of preference periods, summarizing each as a latent milestone for evolving interests. Experiments on six public datasets and four backbone recommenders against eight baselines show consistent gains.
- **Key innovations**:
  - **Personalized reasoning depth** replaces fixed-step latent reasoning.
  - **Reasoning-step selection + self-distillation** compresses the best training-time state into inference.
  - **Progressive preference extraction** creates variable-length latent milestones over user history.
  - Broad evaluation across datasets/backbones for sequential recommendation.

### 2.2 One Basket, Many Experts: Decorrelated Re-ranking for Financial Asset Recommendation (DSER)
- **Authors**: Ryuki Unno, Keigo Sakurai, Koshi Watanabe, Keisuke Maeda, Takahiro Ogawa, Miki Haseyama
- **Institution / Company**: Not stated on arXiv (Hokkaido University tentatively inferred; not confirmed)
- **Published**: 2026-11-04 · cs.IR, cs.CE · ICAIF 2026 · [arXiv:2611.05952](https://arxiv.org/abs/2611.05952)
- **Abstract**: Financial asset recommendation optimized only for relevance can concentrate on popular, correlated assets, limiting risk-adjusted portfolio return. DSER retains the most relevant expert-following recommendations and replaces the remaining slots with return-decorrelated alternatives. The number of replaced slots `m` is an explicit provider-controlled knob, making the relevance–performance trade-off auditable. On the FAR-Trans retail-brokerage dataset, replacing a few slots improves risk-adjusted return at small relevance cost; gains survive realistic trading costs at typical retail portfolio sizes. The relevance cost is stable across market phases while gain is phase-dependent.
- **Key innovations**:
  - Jointly optimizes **behavioral relevance** and **portfolio risk-adjusted return**.
  - **Decorrelated re-ranking** with an explicit, auditable integer knob `m`.
  - Empirical evidence on FAR-Trans with transaction-cost sensitivity.
  - Useful bridge between recommender ranking and financial decision objectives.

### 2.3 Optimal Re-Ranking Depth
- **Authors**: Siqing Huo, Andrew Parry, Debasis Ganguly, Charles L. A. Clarke
- **Institution / Company**: Not stated on arXiv (University of Waterloo + University of Glasgow tentatively inferred)
- **Published**: 2026-11-04 · cs.IR · SIGIR 2026 · [arXiv:2611.05908](https://arxiv.org/abs/2611.05908)
- **Abstract**: Neural re-rankers are often applied with a fixed depth, but effectiveness may saturate or degrade beyond a query-specific optimum. Using dense LLM-based relevance judgments, the paper shows many queries have a well-defined optimal re-ranking depth. It studies predicting this depth from first-stage retrieval signals and finds standard QPP methods ineffective; an LLM-assessed first-stage quality predictor, IR-DCG@10, can reduce average re-ranking depth by up to 3× while preserving effectiveness. Oracle optimal depths improve effectiveness by over 7% while reducing average depth by 5× on MSMARCO DEV.
- **Key innovations**:
  - Treats re-ranking depth as a **query-specific decision**.
  - Uses **dense LLM relevance judgments** to estimate per-query optima at scale.
  - Proposes **IR-DCG@10** as a predictor; cuts depth up to **3×** without losing effectiveness.
  - Oracle analysis quantifies large efficiency/effectiveness headroom.

### 2.4 Do Search-Augmented Recommenders Use the Latest Search Episode?
- **Authors**: Jiandong Ding
- **Institution / Company**: Not stated on arXiv
- **Published**: 2026-11-04 · cs.IR, cs.LG · WSDM 2027 · [arXiv:2611.06044](https://arxiv.org/abs/2611.06044)
- **Abstract**: Search-augmented recommenders may use the latest search episode and/or earlier searches. FocalSwap audits this by swapping the latest search slot or all search inputs while holding target, candidates, pre-search history, and scorer fixed. It compares neutral masks with matched observed-search replacements and measures rank changes, RR gains, and preference for the true focal search. Evaluations on KuaiSAR/Qilin and SESRec/UniSAR checkpoints show that neutral-mask evidence can overstate contribution: matched replacements give smaller or negative estimates for all-source benefit in some cases. Under primary controls, a positive latest-slot contribution is not established in SESRec or UniSAR.
- **Key innovations**:
  - **FocalSwap** causal audit for search-augmented recommendation inputs.
  - Contrasts **neutral masking** with **matched observed-search replacements**.
  - Shows latest-search attribution can be fragile under realistic controls.
  - Practical warning for interpreting search-signal ablations in RecSys.

### 2.5 GINGER: Spicing Up Graph-Based Vector Search
- **Authors**: Daniel Salwasser, Lars Gottesbüren, Laxman Dhulipala, Jakub Łącki, Guy Blelloch, Rajesh Jayaram, Tobias Rubel, Kshiteej Sheth, Amir Zandieh, Vahab Mirrokni
- **Institution / Company**: Google (developed at Google, stated in abstract)
- **Published**: 2026-11-05 (submitted) · cs.IR, cs.DC · [arXiv:2611.08306](https://arxiv.org/abs/2611.08306)
- **Abstract**: GINGER is an open-source C++ graph-based approximate nearest neighbor search library focused on query throughput, indexing time, and memory efficiency for large high-dimensional embeddings. It builds on proximity graph construction (PiPNN) and TurboQuant, introducing Nested TurboQuant (NTQ), a two-level quantizer supporting low-precision graph navigation and high-precision reranking in one code, achieving near floating-point precision with 2.6× less memory. It compresses proximity graphs by up to 2.5× using graph reordering and AdaptiveGap, a lossless codec building on StreamVByte. At 95% recall, GINGER improves query throughput by 1.8× on average over each dataset's fastest competitor and by at least 2.3× over any single library (2.9× over compact libraries on high-dimensional embeddings).
- **Key innovations**:
  - **Nested TurboQuant** unifies navigation/reranking precision tiers in one representation.
  - **Graph compression + AdaptiveGap** codec reduces memory without throughput loss.
  - Strong ANN throughput/memory trade-offs relevant to retrieval, RAG, and embedding-based RecSys.
  - Production-oriented systems contribution from a large-scale industry team.

---

## 3. LLMs, Agents, and Efficiency

### 3.1 Scientist World: Grow a Research World for AI-Scientists
- **Authors**: Taiming Lu, Sachin Konan, Zhuang Liu
- **Institution / Company**: Not stated on arXiv abstract page
- **Published**: 2026-11-05 · cs.AI, cs.CL, cs.LG · [arXiv:2611.08478](https://arxiv.org/abs/2611.08478)
- **Abstract**: Scientist World converts research papers into executable environments for AI scientists. An autonomous pipeline extracts each paper's open-ended research question and reproduces the proposed method as a baseline; agents entering the environment are evaluated against what human authors achieved. The release includes 1,000 verified environments. The authors report frontier AI scientists surpassing human researchers 74% of the time in this evaluation setup, provide 6,400 hours of research traces, and show a small model improved (+158%) to match frontier ideation performance when trained in the environment.
- **Key innovations**:
  - Turns static papers into **executable research environments** with human baselines.
  - Large-scale benchmark/environment suite: **1,000 verified environments**.
  - Uses environment traces for both evaluation and training/ideation improvement.
  - Directly targets the gap between reading scientific literature and doing runnable science.

### 3.2 Towards Foundation Decision Models: Drex
- **Authors**: Nischay Dhankhar, Alisher Amantay, Zhanibek Datbayev, Darkhan Akhmetov, Yash Shah, Nurmukhamed Ubaidullayev, Raman Saparkhan, Dos Baha, Abulhair Saparov
- **Institution / Company**: NYU + nace.ai (inferred from author group/model release context in batch; not fully printed on abstract page)
- **Published**: 2026-11-05 · cs.CL · [arXiv:2611.07854](https://arxiv.org/abs/2611.07854)
- **Abstract**: Drex is a family of open decision models that return probability distributions over user-supplied options without autoregressive decoding. Each request provides a state (document, record, or agent context, optionally images) and questions with choices, yes/no judgments, or ordered scores. Training combines supervised fine-tuning, reinforcement learning from adjusted feedback (RLAF), and vision tuning for the largest model. On Decision Index 0.4.1, Drex Max scores 67.52 (public suite) versus 60.70 for Jev 1.14.0; on Decision Bench v4 it is statistically tied with d3-turbo and GPT-6 Sol and trails Claude Opus 5.5 by 1.6 points. Typical latency is reported as 183 ms, with stable outputs under option reordering.
- **Key innovations**:
  - **Non-autoregressive decision models** over explicit options for agent/product decisions.
  - Training stack: **SFT + RLAF + consistency/vision components**.
  - Strong decision-benchmark results with low latency and option-order robustness.
  - Open family spanning 8B–27B/35B-A3B configurations.

### 3.3 Latency-Aware Adaptive Best-of-N
- **Authors**: Alon Jacobson, Qian Xie, Peter I. Frazier
- **Institution / Company**: Cornell University (tentatively inferred; not stated on abstract page)
- **Published**: 2026-11-05 · cs.CL, cs.LG · [arXiv:2611.07453](https://arxiv.org/abs/2611.07453)
- **Abstract** (from API/abstract excerpt): The paper studies test-time selection when generating more candidates improves quality but increases latency/cost. It proposes a latency-aware adaptive Best-of-N strategy that decides how many samples to draw based on utility and latency trade-offs rather than using a fixed N. This is relevant to LLM serving, agent tool-use, and recommendation/ranking systems that use verifier- or reward-guided candidate selection under strict latency budgets.
- **Key innovations**:
  - Frames Best-of-N as a **latency/quality control** problem, not just a fixed sampling count.
  - Adaptive stopping/selection can preserve quality while reducing serving latency.
  - Useful for production LLM ranking, reranking, and agent decision pipelines.

### 3.4 SPARE: Fast Linear Attention Decoding with Compact Recurrent States
- **Authors**: Ke Wan, Zaiyi Zheng, Chen Chen
- **Institution / Company**: University of Central Florida (tentatively inferred)
- **Published**: 2026-11-05 · cs.CL · [arXiv:2611.07552](https://arxiv.org/abs/2611.07552)
- **Abstract** (from API): Linear attention avoids quadratic attention cost but recurrent states can scale poorly with representation dimension and cause memory traffic during decoding. SPARE exploits low-rank redundancy in recurrent states with fixed low-dimensional subspaces, heterogeneous rank allocation, and lightweight write compensation, operating directly on compact states without online decomposition or dense-state reconstruction. It reports 2.55× full-model decoding speedup, 7.49× lower recurrent-kernel DRAM traffic, and 3.31× lower peak GPU memory while preserving better associative-retrieval accuracy than structured pruning at matched memory budgets.
- **Key innovations**:
  - **Training-free compact recurrent states** for linear-attention decoding.
  - Heterogeneous rank allocation avoids uniform compression loss.
  - Targets memory traffic, a key bottleneck for long-context/serving efficiency.

---

## 4. Games, Agents, and Decision-Making

### 4.1 A Hidden Markov Preference Model for Online Prediction of Adversary Actions
- **Authors**: Angel Daruna, Michael Cogswell, Tixiao Shan, Yi Yao, Han-Pang Chiu, Ajay Divakaran
- **Institution / Company**: SRI International (tentatively inferred)
- **Published**: 2026-11-05 · cs.LG · [arXiv:2611.08445](https://arxiv.org/abs/2611.08445)
- **Abstract**: The paper models online prediction of an adversary's next action from pre-action information when behavior has persistent but switchable regimes and actions include state-dependent feasible arguments. It uses a hidden Markov model whose latent state is the active regime and whose regime-conditioned action law is defined on a feasibility-masked tree of executable actions. The same likelihood provides next-action predictions and updates regime beliefs; partially observed prefixes contribute resolved local factors. Estimation uses convex logistic fits reusable in Baum-Welch. On the CAGE 2 cyber defense benchmark, the filtered latent state is worth 0.8 nats per step, and after a controller switch loss falls in three steps versus ten for a recurrent baseline.
- **Key innovations**:
  - Combines **latent regime switching** with **feasibility-masked executable action trees**.
  - Unified likelihood for prediction and belief update, including partial observations.
  - Strong sequential decision/game-security result on **CAGE 2** with fast post-switch adaptation.

### 4.2 Turns Matter: Advancing Streaming Video RL via Turn-Level Credit (TurnWise)
- **Authors**: Shuai Dong, Kanghui Tian, Linghan Chen, Wenqi Shao, Hongrui Wu, Haowen Hou, Yongfu Zhu, Xuehui Wang, Ziyue Wang, Wenpu Liu, Weichu Xie, Yuqi Xu, Congcong Wang, Kaiwen Tuo, Caoyuan Ma, Taiqiang Wu, Ji Zhao, Wenzheng Chang, Dianyi Wang, Siyuan Wang, Zhongyu Wei, Yu Qiao, Jiaqi Wang
- **Institution / Company**: Shanghai AI Laboratory + Fudan University (tentatively inferred)
- **Published**: 2026-11-04 · cs.CV, cs.CL, cs.LG · [arXiv:2611.06728](https://arxiv.org/abs/2611.06728)
- **Abstract**: Streaming video agents repeatedly decide whether to respond or keep observing. Existing GRPO-style training often assigns one trajectory-level advantage across turns, reinforcing redundant replies or discouraging useful follow-ups. TurnWise applies turn-level GRPO credit. It uses silence-completed prefix scoring to build group-relative advantages from each decision's remaining return, separating learning signals from earlier rewards. Turn-mean policy optimization averages token losses within and across turns, balancing respond/wait decisions regardless of output length. The method improves streaming video understanding without a learned critic or extra rollouts.
- **Key innovations**:
  - **Turn-level credit assignment** aligned with streaming decisions.
  - **Silence-completed prefix scoring** measures remaining return per decision.
  - Balances **respond vs wait** actions without length bias or critic/extra rollouts.
  - Relevant to game/interactive agents that must act over streaming observations.

---

## Quick Takeaways

- **RecSys/ads CTR modeling** is moving from independent item scoring to **journey/process models** (ICE) and from catalog validity to **request-time feasibility** (RTP-LLM).
- **Generative recommendation** is focused on repairing the **semantic-ID interface**: BRIDGE fixes the decoder-side quantization gap; OptST makes tokenizer assignments task-aware.
- **LLM recommenders** show two efficiency/correctness levers: remove inference-time text reasoning when training-time latent supervision suffices (LatentRec), and correct CF reward components that cause exposure collapse.
- **Sequential/search systems** benefit from audits and adaptive controls: FocalSwap questions latest-search attribution, while optimal re-ranking depth and latency-aware Best-of-N treat compute as a per-query decision.
- **Agent/game settings** reward explicit credit assignment and regime/state modeling: TurnWise for streaming decisions, HMM preference modeling for adversary prediction, Drex for low-latency option-based decisions.
