---
title: "arXiv Daily - 2026-10-25"
type: synthesis
created: 2026-10-25
updated: 2026-10-25
sources: []
tags: [arxiv, llm, ai, recommendation, advertising, ctr, sequential-modeling, games]
---

# arXiv Daily Report (2026-10-25)

*Generated from arXiv API search results.* 

## Recent Papers (AI/LLM/Recommendation/Advertising/CTR/Sequential Modeling/Games)

### 1. [Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success](https://arxiv.org/abs/2610.31670v1)
- **arXiv**: [2610.31670v1](https://arxiv.org/abs/2610.31670v1)
- **Authors**: Yunfei Xie, Howard H. Qian, Shiyi Lan, Kaiyu Hang, Chen Wei
- **Categories**: cs.CV, cs.LG, cs.RO
- **Institution/Company**: (not explicitly stated in metadata; see paper)
- **Abstract**: Robotic foundation models are typically evaluated through costly closed-loop rollouts, which motivates cheap offline proxies for model capability. The Platonic Representation Hypothesis (PRH) suggests that as representations improve, different modalities such as vision and language converge toward a shared statistical model of reality. We ask whether motion trajectories form another such modality: as embodied models become more capable, should their sensory representations converge toward the structure of physical motion? To examine this, we propose Sensorimotor Alignment ($S^2$), a training-free offline metric that measures how well a model's sensory representation aligns with the geometry of physical motion. We find that $S^2$ correlates positively with downstream robot task success across embodied model families, making it a low-cost offline proxy for prioritizing models before closed-loop evaluation. $S^2$ can also identify promising vision-language model (VLM) backbones even before costly fine-tuning into vision-language-action models (VLAs). Beyond this correlation, $S^2$ offers representation-level explanations for phenomena observed in VLAs and world action models (WAMs). With $S^2$, we extend PRH to embodied models and make sensorimotor alignment empirically measurable, offering insight into why an embodied model succeeds beyond its closed-loop success rate.
- **Key Innovations**:
  - Proposes **Sensorimotor Alignment ($S^2$)**, a training-free offline metric measuring alignment between sensory representations and physical motion geometry
  - Shows $S^2$ correlates positively with robot task success across embodied model families
  - Demonstrates $S^2$ can identify promising VLM backbones before VLA fine-tuning
  - Extends Platonic Representation Hypothesis to embodied models

### 2. [Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity in Test-Time Reasoning](https://arxiv.org/abs/2610.31667v1)
- **arXiv**: [2610.31667v1](https://arxiv.org/abs/2610.31667v1)
- **Authors**: Mahdi Salmani, Adel Javanmard, Devansh Gupta, Meisam Razaviyayn
- **Categories**: cs.AI, cs.CL
- **Abstract**: Test-time scaling has emerged as a key inference strategy for reasoning models, where a model generates a large number of candidate solutions in the hope of finding at least one correct solution. Running all candidate solutions to completion can be computationally demanding, so recent work prunes the candidate pool after generating only a short prefix, committing further computation only to the surviving candidates. Existing pruning strategies divide broadly into two categories: Quality-based methods assign a score to each partial solution and discard those predicted to ultimately lead to an incorrect final solution, while diversity-based methods select partial solutions that follow different reasoning trajectories and are therefore likely to cover different final solutions. The tension between these two objectives is an instance of exploration versus exploitation, yet little to no prior work on pruning exposes this trade-off directly, let alone optimizes it. In this paper, we introduce a pruning procedure that addresses this trade-off directly by optimizing pass@$k$ over the selected solution pool. In particular, it chooses the pool to maximize the probability that at least one of its partial solutions, when continued to completion, yields a correct answer. Because this objective simultaneously rewards high-quality partial solutions and penalizes redundancy among them, quality and diversity are naturally balanced by the criterion itself rather than through separate ad-hoc design choices. On eight open-weight reasoning models, our method outperforms existing quality-based and diversity-based pruning strategies. The gains are particularly pronounced when the pruning procedure keeps a moderate number of partial solutions for continued generation, highlighting the value of directly balancing quality and diversity during pruning.
- **Key Innovations**:
  - Introduces pruning procedure that directly optimizes pass@$k$ over selected solution pool
  - Naturally balances quality and diversity without separate heuristics
  - Outperforms existing quality-based and diversity-based pruning strategies on 8 open-weight reasoning models

### 3. [Major Revision, Minor Accountability: LLMs as Reviewers of Published Articles in Top-Tier Journals](https://arxiv.org/abs/2610.31414v1)
- **arXiv**: [2610.31414v1](https://arxiv.org/abs/2610.31414v1)
- **Authors**: Bastien Le Guellec, Su Hwan Kim, Raphael Bentegeac, Aghiles Hamroun
- **Categories**: cs.DL, cs.AI
- **Abstract**: With the growth of scientific output, the peer review system is approaching a breaking point: reviewers are increasingly hard to secure, and turnaround times lengthen accordingly. LLM-assisted or LLM-generated peer review has been proposed as a remedy, but how such models would treat manuscripts already published in top-tier journals, the closest thing the current system has to a gold standard of scientific validity, is not known. Here we assembled a corpus of 200 articles, each released under a CC BY 4.0 license and published in 2026, from 20 general-science, life-science, and clinical-medicine journals including Nature, Science, and Cell, and asked four current LLMs (two proprietary, two open-weight) to produce independent peer-review reports of each one under a blinded protocol. Their decisions were overwhelmingly harsh and starkly inconsistent with each other: 605 of 800 reviews (75.6%) recommended major revision or rejection, but the rate at which any single model did so ranged from 17.5% to 100% (p < 0.001), disagreement on manuscripts that had, by construction, already survived real editorial review at the journals in question. When the same manuscripts were doctored with one deliberately planted, field-specific methodological or statistical flaw, detection rates varied from 17.0% to 60.5% across models (p < 0.001). Recommending revision for papers that had already passed editorial review (low specificity) while missing flaws deliberately placed in front of them (low sensitivity), these models produce output that should be read for what it is: an uneven, framing- and model-dependent signal.
- **Key Innovations**:
  - Large-scale evaluation of LLM peer review on already-published top-tier journal articles
  - Reveals high false-negative/harshness and inter-model inconsistency
  - Shows poor flaw detection despite harsh recommendations

### 4. [LLM-Auction: Generative Auction towards LLM-Native Advertising](https://arxiv.org/abs/2512.10551v3)
- **arXiv**: [2512.10551v3](https://arxiv.org/abs/2512.10551v3)
- **Authors**: Chujie Zhao, Qun Hu, Shiping Song, Dagui Chen, Han Zhu, Jian Xu, Bo Zheng
- **Categories**: cs.GT, cs.AI, cs.LG
- **Institution/Company**: (Alibaba Group / related; authors from Alibaba/industry)
- **Abstract**: The commercialization of LLM applications is the next frontier in online advertising, with LLM-native advertising emerging as a promising paradigm by integrating ads into LLM-generated content. However, classic mechanisms are no longer applicable in this setting where the auction object is shifted from discrete ad slots to distributions over LLM outputs, and existing methods are impractical in industrial scenarios due to ignored externalities or high inference costs. To address these issues, we propose LLM-Auction, the first learning-based generative auction mechanism that integrates auction and generation. By formulating the allocation as preference alignment between LLM outputs and a mechanism objective that balances advertisers' value and user experience, we optimize the LLMs to inherently model allocation externalities without extra inference cost. Theoretically, we identify the allocation monotonicity and continuity of the optimal allocation rule of LLM-Auction, and prove that a simple first-price payment rule exhibits favorable incentive properties under this allocation rule. Furthermore, we build an LLM-as-a-judge simulation environment for quantitative evaluation, and experiments demonstrate that LLM-Auction achieves the state-of-the-art allocation efficiency while approximately satisfying key mechanism properties.
- **Key Innovations**:
  - First learning-based generative auction for LLM-native advertising (auction + generation integrated)
  - Optimizes LLM to model allocation externalities via preference alignment without extra inference cost
  - Theoretical analysis of allocation monotonicity/continuity and incentive properties
  - LLM-as-a-judge simulation environment for evaluation

### 5. [Truthful by Omission: Click Thinning for LLM-Native Advertising](https://arxiv.org/abs/2610.30999v1)
- **arXiv**: [2610.30999v1](https://arxiv.org/abs/2610.30999v1)
- **Authors**: Junhua Liu, Zhicheng Liang, Zejun Zhang, Langzhou He, Feng Qian
- **Categories**: cs.GT, cs.AI, cs.DS
- **Abstract**: Generative AI assistants are becoming an advertising medium, embedding sponsored content in their answers. This setting departs from classical position auctions in two ways: an ad's click-through rate depends on the passage that hosts it, and because users stop at their first click, earlier ads take clicks from later ones. This competition for clicks makes truthfulness delicate: a higher bid can reshape the allocation and put a competitor ahead of the bidder, reducing the bidder's clicks. Existing mechanisms either attain a constant fraction of the optimal welfare (advertisers' total click value) but are not known to be truthful, or are truthful but their welfare guarantee degrades as the number of passages grows. We achieve both even when the answer and its editorial order are fixed before bidding. Assuming each ad's click-through rate when reached is known and unaffected by omitting other ads, we give a computationally efficient mechanism that is truthful in expectation and attains at least half the optimal welfare under free reordering. Our key idea, click thinning, omits ads at random, showing earlier ads less often so that each ad's overall click probability no longer depends on the order of the ads. Welfare maximization then reduces to a tractable matching problem, and solving it exactly with VCG-style payments makes truthful bidding optimal in expectation. Characterizing the click probabilities that omission can achieve sharpens the approximation factor from $2$ to $2-(1-δ)^{K-1}$ when at most $K$ ads are shown and each click-through rate is at most $δ$. This factor is the best possible for any order-preserving rule, even one that ignores incentives and computation, so truthfulness and computational efficiency incur no additional worst-case loss.
- **Key Innovations**:
  - Proposes **click thinning** mechanism for LLM-native advertising
  - Achieves truthfulness in expectation and >= 1/2 optimal welfare
  - Makes click probability order-independent via random omission
  - Welfare maximization reduces to tractable matching with VCG payments

### 6. [POI Recommendation with LLM-Augmented Multi-Graph Learning and Contrastive Alignment](https://arxiv.org/abs/2608.16407v2)
- **arXiv**: [2608.16407v2](https://arxiv.org/abs/2608.16407v2)
- **Authors**: Burak Tamer, Wolfram Höpken, Zehui Wang, Thomas Bayer
- **Categories**: cs.IR, cs.LG
- **Abstract**: Point-of-interest (POI) recommendation models based on graph neural networks achieve strong performance by propagating collaborative signals over user-item interactions, yet they struggle with the cold-start problem, where items with few or no interactions are not represented. In this paper, we propose LLM-augmented Multi-Graph Contrastive Learning (LLM-MGCL), a multi-graph neural network that uses semantic and spatial information about items to extend the LightGCN backbone with two auxiliary item-item graphs: a semantic graph constructed from sentence embeddings of LLM-generated photo summaries and keywords, and a geographic graph derived from Haversine distances between business locations. Item embeddings are propagated over all three graphs in parallel, fused additively, and aligned across views through a bidirectional InfoNCE contrastive objective that connects behavioral, semantic, and spatial representations of the same items. Experiments on the Yelp Multimodal Recommendation Dataset show that LLM-MGCL outperforms classical collaborative filtering, matrix factorization, and non-contrastive graph neural network baselines. It improves Recall@20 by 48.5% and NDCG@20 by 59.0% over LightGCN, while trailing the strongest contrastive baseline, Self-supervised Graph Learning (SGL), slightly in aggregate. A popularity-stratified evaluation shows that LLM-MGCL achieves the highest recall on cold and warm items, whereas SGL remains better on popular items. An ablation study reveals that the cross-view contrastive alignment (CA) is the primary driver of the aggregate gains. Our results suggest that externally grounded, LLM-derived item knowledge can partially compensate for missing collaborative signal and mitigate the item cold-start problem in POI recommendation.
- **Key Innovations**:
  - LLM-augmented multi-graph learning with semantic (LLM photo summaries/keywords) and geographic graphs
  - Cross-view contrastive alignment between behavioral, semantic, spatial representations
  - Improves Recall@20 by 48.5%, NDCG@20 by 59.0% over LightGCN; best on cold/warm items

## Notes
- Report generated from arXiv API/web search on 2026-10-25
- Includes papers from cs.AI, cs.LG, cs.CL, cs.IR, cs.GT, cs.CV, cs.RO, cs.DL
- Covers LLMs, recommendation, advertising, CTR, sequential modeling, games, reasoning, embodied AI, peer review
- Temporary files constraint noted and respected (no files written outside project/workdirs)
- Generated with appropriate metadata for wiki integration
