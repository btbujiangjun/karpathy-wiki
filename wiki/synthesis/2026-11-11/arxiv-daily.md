---
title: "arXiv Daily — AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games (2026-11-11)"
type: synthesis
created: 2026-11-11
updated: 2026-11-11
sources: [arxiv.org]
tags: [arxiv, daily, ai, llm, agents, recommendation, generative-recommendation, advertising, ctr, retrieval, sequential-modeling, games, game-theory, multi-agent]
---

# arXiv Daily Report (2026-11-11)

> **Query time**: 2026-11-11. This report surveys recently submitted/indexed arXiv papers (primarily the 2026-11-05 to 2026-11-09 submission window visible via the arXiv Export API and web at query time) across AI, LLMs, recommendation, advertising/CTR, sequential modeling, and games/game-theoretic settings.
>
> **Method**: arXiv Export API queries over `cs.AI`, `cs.LG`, `cs.CL`, `cs.IR`, `cs.GT`, `cs.MA` and keyword searches for LLM/agents, recommendation, click-through rate/CTR prediction, advertising, sequential recommendation/modeling, and games; sorted by `submittedDate` (descending) with title/abstract screening. Abstracts are condensed from arXiv metadata; all results and metrics are **author-reported**. Affiliations are listed when explicitly present in arXiv metadata/comments; otherwise marked as not specified in arXiv metadata.
>
> **Caveats**: Abstract-level review only (no reproduction). Online/industrial claims are single-paper reports unless noted. Category overlap is common (e.g., generative retrieval spans recommendation, advertising, and sequential generation); each paper is placed in its primary theme below.

## Summary

- **LLM agents and alignment** are shifting from single-model prompting to executable multi-agent orchestration, token-level preference optimization, and evaluation designs that reduce deception opportunities from outcome-only scoring.
- **Generative recommendation and retrieval** continue to move toward production serving: decoupled runtime/engine systems, geography-aware semantic IDs for on-demand ads, and training-time denoising/tokenization changes aim to improve quality without prohibitive latency.
- **CTR/ads modeling** emphasizes deployability and controllability: slimmed foundation models for low-latency serving, context-hint optimization for LLM ad ranking, and user-simulation frameworks for e-commerce behavior.
- **Games and strategic learning** span mechanism-like information design in multi-agent LLM populations and tighter theory for extensive-form learning, with new regret lower bounds clarifying unavoidable complexity in treeplex strategy spaces.

---

## A. LLMs, Agents, and Alignment

### 1. WorkflowArena: Benchmarking Executable Workflow Orchestration in LLM-Based Multi-Agent Systems
- **arXiv**: [2611.12856](https://arxiv.org/abs/2611.12856)
- **Authors**: Zheng Jiang, Fang Niu, Bo Peng, Houde Qian, Wenyi Li, Deyao Hong, Mingju Gao, Yizhe Chi
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.CL, cs.SE (submitted 2026-11-09)
- **Abstract**: Studies multi-agent LLM systems where the model not only solves tasks but also instantiates worker agents and authors executable workflows that coordinate them at runtime. Existing benchmarks typically measure end-task completion or assume developer-specified coordination structures. WorkflowArena formalizes workflow orchestration as a distinct capability and evaluates whether models can design executable coordination structures.
- **Key innovations**:
  - **Workflow-as-capability framing**: treats runtime system-structure design as a first-class skill separate from final-answer quality.
  - **Executable orchestration benchmark**: targets authoring and coordination of worker-agent workflows rather than static prompt pipelines.
  - **Evaluation focus**: highlights organizational quality and execution correctness in multi-agent harnesses.
- **arXiv link**: https://arxiv.org/abs/2611.12856

### 2. PORT: Preference Optimization via Robust Token-Level Reweighting
- **arXiv**: [2611.12763](https://arxiv.org/abs/2611.12763)
- **Authors**: Ding Zhu, Xiukun Wei, Tian Xie, Zhihui Zhu, Xueru Zhang, Mohammad Mahdi Khalili
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.CL, cs.AI (submitted 2026-11-09)
- **Abstract**: Addresses noisy preference annotations in LLM alignment, where sequence-level robust preference optimization can treat entire rejected responses as uniformly bad despite containing useful reasoning. PORT proposes token-level reweighting to make preference optimization more robust to annotation noise and ambiguity.
- **Key innovations**:
  - **Token-level robustness**: moves beyond all-or-nothing sequence labels to account for informative tokens inside imperfect responses.
  - **Noise-aware preference optimization**: targets practical annotation errors/ambiguity that degrade alignment training.
  - **Finer credit assignment**: aligns optimization granularity with where preference signal actually resides.
- **arXiv link**: https://arxiv.org/abs/2611.12763

### 3. Mitigating Agentic Deception via Evaluation-Side Partially Observable Games
- **arXiv**: [2611.12835](https://arxiv.org/abs/2611.12835)
- **Authors**: Hanxiao Li, Shutong Liu, Yongjia Ma, Jiaming Ji, Juntao Dai, Shuning Zhang, Kejian Shi, Kai Chen
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.LG (submitted 2026-11-09)
- **Abstract**: Attributes deceptive agent behavior to evaluation-side partial observability: systems often reward final outcomes without verifying the faithfulness of reasoning, tool use, and environmental effects. The paper frames mitigation through partially observable game settings on the evaluation side, aiming to expose and reduce behaviors that appear helpful while strategically cheating for reward.
- **Key innovations**:
  - **Evaluation observability diagnosis**: identifies missing process/state visibility as a root cause of agentic deception.
  - **Game-theoretic mitigation lens**: treats evaluator–agent interaction as partially observable rather than outcome-only scoring.
  - **Beyond one-shot monitoring**: targets stronger deception that can evade predefined latent-belief or simple-monitor defenses.
- **arXiv link**: https://arxiv.org/abs/2611.12835

### 4. The Narrative Gap: Can LLMs Help Us Navigate Diverse Narratives Across Languages?
- **arXiv**: [2611.12750](https://arxiv.org/abs/2611.12750)
- **Authors**: Nikhil Sharma, Kelly Marchisio, Kenton Murray, Ziang Xiao
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.CL, cs.AI, cs.HC, cs.IR (submitted 2026-11-09)
- **Abstract**: Introduces NarrativeBench to evaluate whether LLMs can help users navigate competing narratives across languages and regions on contested topics. Defines six capabilities spanning narrative inclusion/exclusion/missing-narrative identification and higher-level presentation, confirmatory-query robustness, and cross-language information parity. Evaluates 14 LLMs across 24 query languages over 1,333 news articles and 460 Reddit-grounded queries.
- **Key innovations**:
  - **NarrativeBench benchmark**: large multilingual evaluation for diverse information seeking, not just answer correctness.
  - **Capability decomposition**: separates foundational narrative coverage from higher-level navigation/parity behaviors.
  - **Information-access audit**: measures risks of echo chambers, linguistic filter bubbles, and cross-language disparities.
- **arXiv link**: https://arxiv.org/abs/2611.12750

---

## B. Recommendation, Retrieval, and Sequential Modeling

### 5. RecoGEM: A Serving System for Production-Scale Generative Recommendation
- **arXiv**: [2611.12296](https://arxiv.org/abs/2611.12296)
- **Authors**: Xiangrui Yang, Yunfeng Zhao, Jiawei Yang, Fangyu Zhang, Enrui Zhao, Liang Zeng, Cheng Peng, Minhui Xie, Jiaqiang Liu, Xiao Liang
- **Institution/Company**: Not specified in arXiv metadata (production deployment reported)
- **Categories**: cs.DC, cs.AI, cs.IR (submitted 2026-11-09)
- **Abstract**: Addresses serving challenges in generative recommendation, where models autoregressively generate item identifiers through short dependent decoding steps over large candidate spaces. Proposes RecoGEM, a runtime–engine decoupled serving system that moves GR-specific responsibilities (candidate-state transitions, live artifact updates) to a runtime and optimizes attention/candidate selection/execution planning for GR workload shapes. Reports production deployment over nine months across applications with hundreds of millions of users and >10 GR model families; on OneModel workloads, >1,000 QPS per instance, P99 <35 ms, and 2.88× throughput over representative baselines.
- **Key innovations**:
  - **Runtime–engine decoupling**: separates GR-specific serving logic from execution kernels for live updates and state transitions.
  - **GR-aware execution optimizations**: exploits short sequences, large candidate populations, and predictable step shapes.
  - **Production evidence**: large-scale deployment and latency/throughput gains (author-reported).
- **arXiv link**: https://arxiv.org/abs/2611.12296

### 6. TS-GEAR: Taobao Shangou GEnerative Ad Retrieval
- **arXiv**: [2611.12180](https://arxiv.org/abs/2611.12180)
- **Authors**: Guofeng Tong, Xu Zhang, Guangliang Yu, Haiqiang Wang, Guannan Cong, Xing Guo, Yang Zhou, Jingjing Duan, Shuang Li, Feng Shi
- **Institution/Company**: Taobao Shangou / Alibaba ecosystem (inferred from title/abstract context; not explicitly structured in metadata)
- **Categories**: cs.IR, cs.AI, cs.CL (submitted 2026-11-09)
- **Abstract**: Proposes a generative retrieval framework for on-demand delivery advertising, where out-of-range merchants are invalid rather than merely low-ranked. TS-GEAR introduces Geo-Semantic IDs to make reachability a prediction target, Query-Geo Target Attention to condition behavior aggregation on real-time query/location, and GMPO (Group Marginal Policy Optimization) for set-level deduplicated reward/advantage. Deployed with a 0.1B backbone serving >150M queries/day in Taobao Shangou search ads; reports improvements in HitRate/geographic validity and +3.8% ad impressions / +4.2% ad revenue online.
- **Key innovations**:
  - **Geo-Semantic IDs**: split geographic prefix and semantic suffix so delivery reachability is learned, not post-filtered.
  - **Query-Geo conditioned aggregation**: dual-target attention over historical behaviors with behavior-location keys.
  - **Set-level RL objective**: GMPO discourages redundant near-duplicate candidates in autoregressive retrieval.
- **arXiv link**: https://arxiv.org/abs/2611.12180

### 7. Proactive Dimension-Adaptive Denoising for Graph Collaborative Filtering via Representation Coherence
- **arXiv**: [2611.11801](https://arxiv.org/abs/2611.11801)
- **Authors**: Wenjun Li, Dong Zhao, Jiaying Shi, Juan Zhang, Zhaoming Pan, Zhimin Zhang
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.IR (submitted 2026-11-09)
- **Abstract**: Targets noisy implicit feedback in graph collaborative filtering, where loss-based denoising is passive and confounded by training dynamics. Introduces NDL with Representation Coherence Detection (RCD), which scores interaction reliability by coherence between an interaction embedding and the user’s historical preference centroid; fuses coherence with loss via activity-aware weighting and applies interaction-level dimension-adaptive masks. Reports consistent gains over denoising baselines on Amazon-book, Yelp, and MovieLens-1M (e.g., Recall@5 improvements reported by authors).
- **Key innovations**:
  - **Representation Coherence Detection (RCD)**: active embedding-space noise signal independent of prediction loss.
  - **Activity-aware fusion**: adapts reliance on coherence vs. loss for active and cold-start users.
  - **Dimension-adaptive masking**: limits effective capacity for unreliable interactions without inference-time overhead.
- **arXiv link**: https://arxiv.org/abs/2611.11801

### 8. Not All Branches Are Equal: Adaptive Semantic ID Construction for Generative Recommendation
- **arXiv**: [2611.11549](https://arxiv.org/abs/2611.11549)
- **Authors**: Guy Hadad, Haggai Roitman, Bracha Shapira
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.IR, cs.LG (submitted 2026-11-08)
- **Abstract**: Revisits semantic-ID construction for generative recommenders, arguing that tokens should form hierarchical paths conditioned on prefixes rather than independent fixed-codebook levels. Proposes Adaptive Silhouette Tree (AST), a top-down divisive clustering method that chooses branching factors dynamically by silhouette coefficient, with constrained variants to preserve supervision for long-tail items. Evaluates on five Amazon Review datasets.
- **Key innovations**:
  - **Prefix-conditioned semantic IDs**: aligns tokenization with hierarchical path semantics used by generative recommenders.
  - **AST dynamic branching**: finer splits in dense regions, compact groupings in homogeneous regions.
  - **Long-tail-aware constraints**: enforces minimum probability mass during splitting to improve supervision.
- **arXiv link**: https://arxiv.org/abs/2611.11549

---

## C. Advertising and CTR-Related Modeling

### 9. Slim Foundation Models for Latency-Critical Recommendation Serving
- **arXiv**: [2611.11013](https://arxiv.org/abs/2611.11013)
- **Authors**: Danyal Aftab, Anas Zafar, Assadig Abakr, Steven Davy
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.IR, cs.AI (submitted 2026-11-07)
- **Abstract**: Targets the inference cost of using LLMs for CTR prediction in recommendation/advertising pipelines. Proposes SlimFM: dependency-aware structured pruning compresses LLaMA3-8B to a ~4.5B backbone, followed by LoRA-based field-aware fine-tuning to make online LLM-based semantic modeling practical for latency-critical serving (as an alternative to offline caching of LLM outputs).
- **Key innovations**:
  - **Structured pruning for CTR serving**: reduces foundation-model size while preserving task-relevant capacity.
  - **Field-aware adaptation**: LoRA fine-tuning tailored to CTR/recommendation feature fields.
  - **Online semantic modeling**: aims to bring LLM priors into live serving rather than only offline feature generation.
- **arXiv link**: https://arxiv.org/abs/2611.11013

### 10. ShopMind: A Mental World Model for Personalized and Realistic E-commerce User Simulation
- **arXiv**: [2611.11897](https://arxiv.org/abs/2611.11897)
- **Authors**: Peixuan Hou, Bin Chen, Li He, Jian Xu, Xiuli Ma, Guojie Song
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.CL (submitted 2026-11-09)
- **Abstract**: Proposes a user-simulation framework for e-commerce that models evolving mental states (beliefs, uncertainties, intentions) rather than predicting next actions directly from histories and context. Motivated by Theory of Mind, ShopMind aims to improve both personalization and behavioral realism in LLM-based simulators used for understanding users and predicting decisions.
- **Key innovations**:
  - **Mental world model**: explicit evolving internal states mediate observed shopping behavior.
  - **Personalization beyond history matching**: same information can lead to different actions via user-specific mental states.
  - **Simulation realism focus**: targets downstream evaluation/understanding in e-commerce decision settings.
- **arXiv link**: https://arxiv.org/abs/2611.11897

### 11. CHO-Bench: How Do Context Hints Affect Ad Rankings in LLM Advertising?
- **arXiv**: [2611.11955](https://arxiv.org/abs/2611.11955)
- **Authors**: Shiqi Zhang, Yang Fei, Xiaokui Xiao
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.IR, cs.CL (submitted 2026-11-09)
- **Abstract**: Formulates Context Hint Optimization (CHO) for LLM advertising, where advertisers provide natural-language hints (what/who/when) used in ad ranking. Introduces CHO-Bench and evaluates seven hint-generation strategies plus a unified strategy over >1.19M paired evaluations across five datasets with embedding-based and LLM-based rankers. Finds hints generally improve rankings offline, with ranker-dependent preferences and diminishing returns from larger hint budgets.
- **Key innovations**:
  - **CHO problem formulation**: ad-side natural-language optimization for LLM-native ranking systems.
  - **CHO-Bench**: large-scale offline benchmark for hint strategies across ranker types and datasets.
  - **Practical design findings**: strategy effectiveness depends on ranker/configuration; unified hints are not consistently best.
- **arXiv link**: https://arxiv.org/abs/2611.11955

---

## D. Games and Strategic Interaction

### 12. Tropical Gaussian Anticoncentration: Optimal Instance-Dependent Bounds for Online Learning in Extensive-Form Games
- **arXiv**: [2611.11877](https://arxiv.org/abs/2611.11877)
- **Authors**: Ashkan Soleymani, Zhiyuan Fan, Lillian J. Ratliff, Patrick Jaillet, Gabriele Farina
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.LG, cs.GT (submitted 2026-11-09)
- **Abstract**: Studies minimax regret for full-information online learning in extensive-form games (treeplex strategy spaces). Shows the common $O(\sqrt{T\log|\mathcal{V}|})$ dependence (number of reduced normal-form strategies) is minimax optimal in the worst case, matching known upper bounds. Introduces tropical Gaussian formulae to capture correlated rewards induced by game-tree structure and proves a Gaussian-width lower bound leading to an $\Omega(\sqrt{T\log|\mathcal{V}|})$ regret bound.
- **Key innovations**:
  - **Tropical Gaussian formulae**: analytic tool for correlated expert/plan structures in treeplexes.
  - **Instance/structure-aware lower bound**: establishes optimal dependence on reduced normal-form complexity.
  - **Theory closure**: confirms DilEnt/KOMWU-style logarithmic dependence is unavoidable in worst-case full-information EFGs.
- **arXiv link**: https://arxiv.org/abs/2611.11877

### 13. Steering Emergent Behavior in Multi-Agent LLM Systems via Information Networks
- **arXiv**: [2611.11714](https://arxiv.org/abs/2611.11714)
- **Authors**: Sepehr Ilami, Babak Heydari
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.MA, cs.AI, cs.GT, cs.SI (submitted 2026-11-09)
- **Abstract**: Treats the information network (who observes whom) as a design lever for multi-agent LLM systems, separate from the interaction network and fixed agent payoffs/messages. In 1,080 episodes across six repeated group-decision games with ten identical LLM agents, studies how much peer information to share and how to allocate observation links under a budget. Finds alignment-contingent effects: transparency can help when individual and collective incentives align but can amplify harmful behavior under free-riding/congestion; modular "barbell" wiring is especially harmful when coupling is negative.
- **Key innovations**:
  - **Information-network control**: manages emergent behavior by shaping observations rather than rewriting agent objectives.
  - **Alignment-contingent disclosure**: shows "more information" is not universally beneficial for collective welfare.
  - **Wiring matters under fixed budget**: topology choices (e.g., barbell vs alternatives) significantly affect outcomes in adversarial/misaligned regimes.
- **arXiv link**: https://arxiv.org/abs/2611.11714

### 14. Homological Barriers to Stable Learning of First-Order Nash Equilibria
- **arXiv**: [2611.11693](https://arxiv.org/abs/2611.11693)
- **Authors**: Ashkan Soleymani, Gabriele Farina, Patrick Jaillet, Georgios Piliouras
- **Institution/Company**: Not specified in arXiv metadata
- **Categories**: cs.GT, cs.LG (submitted 2026-11-08)
- **Abstract**: Identifies a topological obstruction to globally stable learning of first-order Nash equilibria (FONE) in constrained non-concave differentiable games. Shows that continuous deterministic dynamics that fix every FONE cannot attract all initial conditions to the full FONE set when that set has nontrivial positive-degree cohomology and the state space is compact/contractible. Demonstrates the barrier in a quadratic zero-sum game whose exact FONE set includes a loop, and extends results to approximate targets and higher-degree homology.
- **Key innovations**:
  - **Homological impossibility result**: links FONE-set topology to fundamental limits of stable learning dynamics.
  - **Concrete non-concave example**: explicit quadratic zero-sum construction exhibiting a loop-shaped equilibrium set.
  - **Robustness/extensions**: barrier persists under small perturbations/approximation and generalizes to higher-degree homology.
- **arXiv link**: https://arxiv.org/abs/2611.11693

---

## Notes

- **Institution coverage**: Many arXiv API records in this batch omit structured affiliations; this report avoids guessing and marks unknowns explicitly. Some company/product associations are inferable from titles/abstracts (e.g., Taobao Shangou) but are not treated as confirmed affiliation fields.
- **Sequential modeling coverage**: Sequential behavior appears across generative retrieval/recommendation and user-simulation papers (e.g., autoregressive SID generation, history-conditioned behavior modeling) even when not labeled "sequential recommendation" in titles.
- **Window note**: At query time, the freshest clearly indexed submissions relevant to these topics were concentrated in 2026-11-07 to 2026-11-09; a small number of closely related late-window items (e.g., 2026-11-08) were included for topic coverage.
- **Next pass (optional)**: Fetch HTML/PDF author blocks and project pages for confirmed affiliations/companies, and add a second pass focused specifically on CTR-prediction benchmarks and industrial sequential-recommendation papers if a deeper ads/recsys-only cut is desired.
