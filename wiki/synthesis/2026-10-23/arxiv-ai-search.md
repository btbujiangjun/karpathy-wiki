---
title: arXiv AI Search - AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games (2026-10-23)
type: synthesis
created: 2026-10-23
updated: 2026-10-23
sources: []
tags: [arxiv, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, generative-recommendation, agent-memory, offline-rl, mechanism-design]
---
# arXiv AI Search - AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games (2026-10-23)

> Curated from recent arXiv submissions (window ~2026-10-19 to 2026-10-22). Focus: recommendation, advertising/auctions, CTR, sequential user modeling, LLM agents/memory, and games. Abstracts are condensed from arXiv; affiliations are parsed from the papers' rendered author blocks, never inferred.

## Summary

- **Recommendation is being re-engineered around semantic IDs and long behavior sequences.** FineSID (Alibaba) stages content tokenization → query-item pretraining → click personalization over one shared Semantic ID space; SPAR (USTC/UESTC/SWJTU/HUJING) adds prefix-conditioned personalization and branch balancing for generative recommendation at Youku; ECHO (Kuaishou) makes 100K-length user histories affordable with a distilled selector plus target-aware retriever (~160× fewer sequence-branch FLOPs).
- **The long tail and the baseline are the new battlegrounds.** CAPE shows generative recommenders forget tail items twice — once in beam search, once in likelihood ranking — and restores memorization without training; Instagram Feed argues rankers should keep the raw baseline prediction and add a separately weighted incremental term.
- **Advertising is moving toward LLM-native and causally grounded mechanisms.** Click Thinning designs a truthful-in-expectation auction for ads embedded in generative answers; Next Best Action formulates business action targeting as a constrained MDP with causal off-policy correction and LP shadow prices.
- **LLM agents are shifting from bigger context to learned memory and self-generated training data.** LongZero learns long-context reasoning from zero external data; Uni-Mem jointly learns memory construction and retrieval with online RL; MemoryTax reports that designed memory mainly patches weak models, while strong coding agents win on cost-accuracy by searching raw history.
- **Games/agentic evaluation:** Environment Duels turns environment authoring and solving into a co-evolution benchmark; Flood-It provides a clean solver comparison where A* wins on typical instances but SAT overtakes at higher complexity.

## Papers

### Recommendation, CTR, Advertising & Commerce

#### 1) SOAR: Social and Opinion-Aware Recommendations
- **arXiv**: [2610.29556](https://arxiv.org/abs/2610.29556)
- **Submitted**: 2026-10-21
- **Authors**: Giannis Christoforidis, Apostolos N. Papadopoulos
- **Institution/Company**: Aristotle University of Thessaloniki
- **Categories**: cs.LG, cs.IR

**Abstract**: Point-of-interest recommendation must capture habits, evolving preferences, and the social context behind user behavior. SOAR jointly incorporates the user's friendship network and textual reviews, with particular emphasis on review sentiment, to assess whether a location is suitable for a specific user. Experiments on real-world datasets show that injecting review evidence into the recommendation process improves precision.

**Key innovations**: social-graph + opinion/sentiment fusion for POI recommendation; explicit modeling of whether a venue fits a user rather than only modeling co-visitation; empirical validation that review text adds precision beyond social signals.

#### 2) Generative Recommenders Forget the Long Tail: Restoring Memorization in Retrieval and Ranking
- **arXiv**: [2610.29298](https://arxiv.org/abs/2610.29298)
- **Submitted**: 2026-10-21
- **Authors**: Xu Huang, Jiancan Wu, Hongzheng Qin, Jiawei Feng, et al.
- **Institution/Company**: University of Science and Technology of China; Independent Researcher
- **Categories**: cs.IR

**Abstract**: Generative recommenders replace retrieve-then-rank with beam search over semantic item identifiers and use the same likelihood for ranking. The authors show this shared score forgets long-tail items twice: beam search prunes tail prefixes by subtree probability mass, and the likelihood still ranks admitted tail items below head items. Both failures reflect missing item-level memorization that collaborative filtering provides. CAPE is a training-free plug-in that adds a co-occurrence memorization channel outside the beam and a memorization-calibrated ranking that fuses generator likelihood with co-occurrence evidence while preserving the generator's first item.

**Key innovations**: a two-stage diagnosis of long-tail failure in generative recommendation; training-free co-occurrence channel + calibrated ranking; improvements on product and music domains with a frozen generator and small latency overhead.

#### 3) Progressive Learning from Content to Relevance to Personalization for CTR Prediction
- **arXiv**: [2610.29138](https://arxiv.org/abs/2610.29138)
- **Submitted**: 2026-10-21
- **Authors**: Zhiguang Yang, Yulin Yang, Fuyu Lv, Dan Ou
- **Institution/Company**: Alibaba Group
- **Categories**: cs.IR, cs.MM

**Abstract**: Multimodal CTR prediction in search depends on item content, query relevance, and user preference. FineSID is a progressive framework that unifies content tokenization, query-item semantic pretraining, and personalized post-training through a shared fine-grained discrete representation. A multi-scale visual tokenizer and text tokenizers produce fine-grained Semantic IDs aligned with ID features; full-parameter pretraining under relevance supervision builds a matching prior; click-supervised fine-tuning then captures personal preference. Offline and online evaluations show gains in CTR and business metrics, plus better within-product creative discrimination.

**Key innovations**: three-stage curriculum over one shared Semantic ID space; explicit relevance stage between content and click supervision; evidence of semantic generalization beyond ID memorization in industrial search.

#### 4) SPAR: Stepwise Personalized Autoregressive Recommendation with Prefix-Balanced Semantic IDs
- **arXiv**: [2610.27898](https://arxiv.org/abs/2610.27898)
- **Submitted**: 2026-10-20
- **Authors**: Chunrui Zhang, Gaoyun Lin, Chang Zhou, Zheng Hu, et al.
- **Institution/Company**: USTC; UESTC; Southwest Jiaotong University; HUJING Digital Media & Entertainment Group
- **Categories**: cs.IR

**Abstract**: Semantic-ID generative recommendation retrieves items through successive token decisions, so personalization must happen at every decoding step. SPAR's PATH Decoder retrieves prefix-relevant evidence from compressed long-term user memory and combines it with recent behavior, profiles, and context; its RQ-PIB module balances historical interaction loads among sibling branches while preserving semantic structure. On Youku production data, SPAR improves HitRate by 2.66% on average, raises target-prefix retention by 5.79 points, and cuts the largest child-branch share by 32.84%. A 7-day A/B test on 10% of traffic improves watch time per user by 3.95% and play conversion by 3.38%.

**Key innovations**: prefix-conditioned evidence retrieval at each decoding step; branch-load balancing to avoid popular-path collapse; large-scale online validation at Youku.

#### 5) Baseline and Incremental: User, Item, and Request Debiasing in Instagram Feed Ranking
- **arXiv**: [2610.27423](https://arxiv.org/abs/2610.27423)
- **Submitted**: 2026-10-20
- **Authors**: Hsin-Chiang Chen, Hao Wang, Gedi Zhou, Mingze Gao, et al.
- **Institution/Company**: Meta
- **Categories**: cs.IR, cs.LG

**Abstract**: A feed ranker scores candidates with a value model that sums engagement predictions, but each prediction conflates a baseline (what this viewer/item/request would produce anyway) with the incremental effect of the candidate. The paper argues that a multi-signal value model should keep the raw prediction and add the incremental part as a separately weighted term. On Instagram Feed, three debiasing families (viewer habit, item popularity, request context) are unified as one parameterized operator, while media-type bias is handled through a debiased label. A four-arm production ablation shows the two-term arm beats either single-term arm in 11 of 13 judged (term, metric) pairs; the operator has since been adopted across Meta surfaces.

**Key innovations**: baseline/incremental decomposition instead of removing the baseline; one operator spanning multiple debiasing families; large-scale production ablation and cross-surface deployment.

#### 6) Next Best Action: Causal Constrained Offline RL for Business Action Targeting
- **arXiv**: [2610.26817](https://arxiv.org/abs/2610.26817)
- **Submitted**: 2026-10-19
- **Authors**: Surya Ramachandiran, Yiming Li, Juan Mancilla-Caceres, Tao Ye, Jun Liu
- **Institution/Company**: Lyft, Inc.
- **Categories**: cs.LG, cs.AI, cs.IR, math.OC

**Abstract**: Next Best Action systems must choose interventions that maximize long-term economic value while satisfying operational constraints and remaining causally grounded. The paper formulates NBA as a Constrained Markov Decision Process and integrates off-policy causal correction of estimated customer dynamics directly into the LP formulation. The resulting policy enforces business guardrails and yields shadow prices that quantify the economic trade-offs of constraints. In a rideshare coupon-targeting case study, the policy improves customer lifetime value by 19% over the behavior policy and 8% over a myopic baseline under the observed budget and RFM state representation.

**Key innovations**: causal correction inside the LP form of a CMDP; interpretable shadow prices for operational constraints; action-agnostic targeting module validated on a real rideshare setting.

#### 7) Truthful by Omission: Click Thinning for LLM-Native Advertising
- **arXiv**: [2610.30999](https://arxiv.org/abs/2610.30999)
- **Submitted**: 2026-10-22
- **Authors**: Junhua Liu, Zhicheng Liang, Zejun Zhang, Langzhou He, Feng Qian
- **Institution/Company**: University of Southern California; The Chinese University of Hong Kong, Shenzhen; University of Illinois Chicago
- **Categories**: cs.GT, cs.AI, cs.DS

**Abstract**: Generative assistants are becoming an advertising medium, embedding sponsored content in answers. This differs from position auctions because an ad's CTR depends on its hosting passage and earlier ads take clicks from later ones, so a higher bid can reshape allocation and reduce the bidder's own clicks. Existing mechanisms either approximate welfare without known truthfulness or are truthful with welfare guarantees that degrade with passage count. The paper proposes click thinning: randomly omit ads so that each ad's overall click probability no longer depends on order, reducing welfare maximization to a tractable matching problem solved with VCG-style payments. The mechanism is truthful in expectation and attains at least half the optimal welfare; the bound sharpens to `2 - (1-δ)^(K-1)` when at most K ads are shown and CTRs are bounded by δ.

**Key innovations**: random omission as an order-decorrelation device; truthful-in-expectation mechanism with a constant welfare guarantee; matching-based allocation with VCG payments for LLM-native ad slots.

#### 8) Doubly Robust Distributionally Robust Offline Contextual Pricing
- **arXiv**: [2610.30957](https://arxiv.org/abs/2610.30957)
- **Submitted**: 2026-10-22
- **Authors**: Min Xu, Xinyi Yin, Yunfan Zhang, Yuxuan Han, Houcai Shen, Caihua Chen
- **Institution/Company**: Nanjing University; New York University (Stern)
- **Categories**: cs.LG

**Abstract**: Offline contextual pricing faces distribution shift between logged training data and deployment. Distributionally robust optimization offers a principled remedy, but existing methods mostly handle discrete actions; continuous-treatment DRO using inverse propensity weighting is sensitive to propensity estimation error. The paper develops a doubly robust framework for distributionally robust off-policy evaluation and learning in continuous pricing. A localized DR estimator handles worst-case expectations with only a few regressions, while a smoothness-aware learning method yields a finite-sample regret bound of `Õ_p(T^{-s/(2s+1)})` for smoothness orders s = 1, 2, improving existing DRO regret rates for continuous treatments.

**Key innovations**: doubly robust DRO for continuous prices; localized estimator that avoids expensive worst-case optimization; improved regret guarantees under distribution shift.

#### 9) Preference Is Not Permission: Personalizing the Auto-Purchase Line in Agentic Commerce
- **arXiv**: [2610.29216](https://arxiv.org/abs/2610.29216)
- **Submitted**: 2026-10-21
- **Authors**: Ryotaro Shimizu, Sai HtaungKham, Mo Fan
- **Institution/Company**: ZOZO Research
- **Categories**: cs.IR, cs.CL, cs.HC, cs.LG

**Abstract**: Personalized shopping benchmarks ask which item fits the user; this paper asks how far an agent may commit on that item. The auto-purchase boundary is evidence-conditioned and three-valued: don't buy, confirm first, or buy automatically, depending on product-information warrant, reversibility, price relative to the user's norm, and urgency. Across sixteen instruction-tuned models, autonomous commitment is misaligned with a human authorization reference: models commit even when fit is low and when their own evidence flag reports missing warrant. The boundary is individual but partly predictable; a shallow learner trained on a few dozen of a person's own labels predicts held-out decisions at a median of 0.79 and beats every evaluated prompt × model configuration, though it does not transfer across domains.

**Key innovations**: reframes personalization as authorization rather than fit; three-valued auto-purchase task with human reference; evidence that lightweight personal labels outperform prompting for safety-critical delegation.

#### 10) ECHO: Efficient Cascade with Homogeneous Operators for Distillation-Guided 100K-Sequence Modeling
- **arXiv**: [2610.28569](https://arxiv.org/abs/2610.28569)
- **Submitted**: 2026-10-20
- **Authors**: Wenhao Li, Qinglin Jia, Chenghou Jin, Zihong Xian, et al.
- **Institution/Company**: Kuaishou Technology
- **Categories**: cs.IR

**Abstract**: Modeling lifetime user behavior is essential for long-range preference capture, but 100K-length sequences make target-aware ranking prohibitively expensive. Search-based methods pay candidate-dependent costs that grow with sequence length, while latent compression loses item-level addressability. ECHO keeps a subset of original event records per user via a Distilled Selector supervised by a candidate-aware full-history teacher, then retrieves a smaller target-relevant set per candidate with a Target-aware Fine-grained Retriever. Retriever and target-attention scorer share the teacher's relevance parameters. At L = 100K, ECHO cuts online sequence-branch FLOPs by ~160× versus an end-to-end model, improves GAUC by 0.113%-1.520% on KuaiRand-1K and an industrial short-video platform, and raises app usage time by 0.613% in online A/B.

**Key innovations**: per-target distillation into a user-level selector; target-aware fine-grained retrieval over retained raw events; homogeneous relevance parameters across the cascade plus deployment-oriented memory/data-movement optimizations.

### LLM Agents, Memory & Evaluation

#### 11) LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data
- **arXiv**: [2610.30132](https://arxiv.org/abs/2610.30132)
- **Submitted**: 2026-10-21
- **Authors**: Zhennan Wan, Jianfei Chen
- **Institution/Company**: Tsinghua University (Institute for AI, BNRist, THBI Lab; Tsinghua-Bosch Joint ML Center)
- **Categories**: cs.CL, cs.LG

**Abstract**: RL can strengthen long-context reasoning, but it needs long, diverse, challenging, and verifiable training data; human annotation is expensive, natural data are scarce, and synthesis methods depend on external corpora or stronger teachers. LongZero lets an LLM improve long-context reasoning without external data: the model first writes a question, answer, and supporting evidence in compact structured form, then expands the evidence into a long multi-document context. These self-written multi-hop tasks are combined with self-written multi-round retrieval tasks and used for GRPO training. Across two LLMs and five benchmarks, LongZero generalizes to real tasks and outperforms RL on externally synthesized data.

**Key innovations**: evidence-first synthesis followed by context expansion; self-generated multi-hop + multi-round retrieval curriculum; long-context RL with zero external data or teacher model.

#### 12) Uni-Mem: Learning a Long-Horizon Agentic Memory Manager with Unified Online Policy Optimization
- **arXiv**: [2610.29671](https://arxiv.org/abs/2610.29671)
- **Submitted**: 2026-10-21
- **Authors**: Zhiqian Xia, Jielong Tang, Ling-An Zeng, Shixiong Kai, et al.
- **Institution/Company**: Southeast University; Huawei Noah's Ark Lab; Sun Yat-sen University; Shandong Normal University
- **Categories**: cs.CL

**Abstract**: Long-term agent memory is moving from predefined workflows toward learnable policies for memory construction and retrieval. Existing methods optimize construction alone or combine retrieval-side online RL with offline construction supervision, limiting co-adaptation. Uni-Mem explores end-to-end online RL for a unified manager, but joint GRPO suffers from confounded group comparisons and sparse feedback over long memory-management trajectories. The paper proposes Stage-Decoupled GRPO, which alternates construction and retrieval optimization while controlling variation from the other stage, plus Event-Wise Credit Assignment, which localizes feedback to responsible events and propagates event-level advantages to constituent operations. Uni-Mem outperforms the strongest RL-based memory on LoCoMo and LongMemEval.

**Key innovations**: jointly learned construction + retrieval under one policy; stage-decoupled GRPO for confounded long-horizon credit; event-level credit assignment for memory operations.

#### 13) MemoryTax: The Bitter Lesson of Agent Memory
- **arXiv**: [2610.29823](https://arxiv.org/abs/2610.29823)
- **Submitted**: 2026-10-21
- **Authors**: Zedong Peng
- **Institution/Company**: Shanghai Jiao Tong University
- **Categories**: cs.CL, cs.AI

**Abstract**: Agent memory systems such as Mem0 and Zep decide what to keep before a question arrives, whereas coding agents keep raw history and let the model search it with tools. This short empirical study asks whether designed memory still helps once the model is strong enough to search for itself. On one LoCoMo conversation (419 turns, 152 questions), it compares full context, BM25, Mem0, and Zep across three coding agents and three models, recording rollout cost. Designed memory is a costly patch for a weak model: Mem0 beats full context only with GPT-4o-mini, and its build alone costs more than a full-context rollout. Memory also has a ceiling set by the writer model. With Claude Opus 5.5, Pi tops the cost-accuracy frontier at 99% for less than half the cost of full context.

**Key innovations**: cost-accuracy framing of agent memory; controlled comparison of designed memory vs tool-based raw-history search; evidence that stronger models shift the optimal memory strategy toward search.

#### 14) Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research
- **arXiv**: [2610.30113](https://arxiv.org/abs/2610.30113)
- **Submitted**: 2026-10-21
- **Authors**: Houde Qian, Zheng Jiang, Wenyi Li, Chenxi Xu, et al.
- **Institution/Company**: Navers Lab, Einsia.AI
- **Categories**: cs.CL, cs.AI, cs.CE

**Abstract**: Quantitative research is an iterative loop: propose a market hypothesis, implement it as an executable signal, test it historically, and decide what to keep. Existing benchmarks score formulas, code, or individual trading decisions, leaving open whether LLMs can complete the loop and produce strategies that generalize beyond the research period. Quant-Arena is a benchmark and public leaderboard for end-to-end quantitative research on real A-share data. A model constructs features and stock-scoring code, receives feedback only on 2022-2023, and freezes one strategy for assessment on sealed 2024 data; a cash-account evaluator applies trading constraints and costs including simulated market impact. Nine frontier models are evaluated: GPT-6 Astra scores highest, yet no model beats the equal-weight market in 2024.

**Key innovations**: sealed-year, end-to-end quantitative research benchmark; cash-account evaluation with costs and market impact; a sobering negative result on frontier-model strategy generalization.

#### 15) Where Do LLMs Learn to Recommend AI?
- **arXiv**: [2610.29785](https://arxiv.org/abs/2610.29785)
- **Submitted**: 2026-10-21
- **Authors**: Benaya Trabelsi, Jonathan Shaki, Sarit Kraus
- **Institution/Company**: Bar-Ilan University
- **Categories**: cs.CL, cs.AI, cs.CY, cs.LG

**Abstract**: Asked what to study, which career to pursue, or what product to build, LLMs often recommend AI-related options. The paper traces this tendency by comparing models before and after fine-tuning and by varying question phrasing. Pretrained models already include explicit AI/ML terms in 27% of recommendations, rising to 59% in released instruction-tuned versions. The rise is not inevitable: general instruction tuning leaves the rate unchanged, but removing the 7% of instruction examples concerning AI cuts it by 14 points below the pretrained starting point; helpfulness-rewarding data raise it by 9 points, while preference data from diverse simulated users lower it by 9. Asking for the "best" option or what to do "right now" raises the rate by 8 and 18 points, and telling the model it is an AI advisor adds 4.

**Key innovations**: separates pretraining bias from post-training amplification; identifies specific instruction/reward data responsible for AI-recommendation bias; quantifies prompt sensitivity of the effect.

### Games & Strategic Reasoning

#### 16) Environment Duels: A Microcosm of LLM Co-Evolution
- **arXiv**: [2610.30116](https://arxiv.org/abs/2610.30116)
- **Submitted**: 2026-10-21
- **Authors**: Shibo Jin, Zhiqiu Xu, Yiling Zou, Shangyu Gong, Mayur Naik
- **Institution/Company**: University of Pennsylvania
- **Categories**: cs.CL, cs.AI

**Abstract**: Frontier LLMs absorb what their predecessors and competitors create, through synthetic training pipelines and data shared on the open web. Environment Duels is a dynamic agentic benchmark that evaluates models both as creators and as solvers of interactive environments: each model writes environments with a privileged hint, aiming for tasks that capable solvers fail without the hint and pass with it. Across nine frontier LLMs, solving and authoring are distinct skills: the strongest solvers are not the strongest authors, while smaller models learn more from how others played and write the hardest environments and most useful hints. Head-to-head outcomes are transitive and yield a stable ranking; independent authors converge on similar designs; and in an RL study with Qwen3.8-27B, a learner's hint lift on an author's environments tracks how much training on those environments improves held-out reasoning and agentic benchmarks.

**Key innovations**: joint authoring/solving benchmark for co-evolution; privileged-hint design that operationalizes teaching quality; evidence linking in-duel hint lift to out-of-distribution capability gains.

#### 17) Solving Flood-It Puzzles: A Comparison of Tailored A* Search with Declarative Solver Approaches
- **arXiv**: [2610.31100](https://arxiv.org/abs/2610.31100)
- **Submitted**: 2026-10-22
- **Authors**: Philipp von Manteuffel, Benjamin Blankertz
- **Institution/Company**: Technische Universität Berlin
- **Categories**: cs.AI

**Abstract**: The paper presents an optimized A* approach for finding minimal move sequences in Flood-It, compared against SAT, Integer Programming, and Constraint Programming solvers. A* performance is substantially improved with an appropriate heuristic and sophisticated equivalences of game states that limit the search space. Comparing the best variant of each approach, A* is fastest at finding a minimal solution in about 75% of tested instances. The SAT-based approach is designed for the decision problem of whether a solution of a given length exists and requires iterative search for the minimum; however, as complexity (minimum solution length) increases, SAT outperforms A*, albeit with a lower crossing point for the decision problem.

**Key innovations**: domain-specific heuristic + state-equivalence pruning for Flood-It; head-to-head comparison of A*, SAT, IP, and CP; characterization of the complexity crossover between search and declarative solving.

## Method & Scope

- Queried the arXiv Export API for the most recent submissions in `cs.IR`, `cs.CL`, `cs.AI`, and `cs.LG` (40 results per category), plus topical sweeps; selected 17 papers across recommendation, CTR, advertising/auctions, pricing, sequential modeling, LLM agents/memory, and games.
- Authors and abstracts come from arXiv metadata; institution/company strings were parsed from `arxiv.org/html/{id}` author blocks (no inference). Where a paper lists multiple affiliations, all are shown.
- **Caveats**: abstract-only review — no PDF full text was read, and all reported numbers are author-reported, not independently reproduced. The window is recent but not exhaustive; several papers were announced in the 2026-10-21/10-22 blocks and may also appear in sibling daily digests.
- **Contradictions with existing wiki pages**: none identified.
