---
title: "arXiv Daily — AI, LLMs, Recommendation, Advertising, CTR, Sequential Modeling, Games (2026-11-20)"
type: synthesis
created: 2026-11-20
updated: 2026-11-20
sources: [arxiv.org]
tags: [arxiv, daily, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, generative-recommendation, collaborative-filtering, retrieval, rag, recommender-agents, agents, reinforcement-learning, on-policy-distillation, sparse-autoencoders, linear-attention, sparse-attention, kv-cache, scaling-laws, game-theory, equilibrium-computation, evaluation-audit, voice-agents, multimodal, security, quantum-computing, survival-analysis, digital-twins]
---

# arXiv Daily Report (2026-11-20)

> **Query time**: 2026-11-20. This report covers the newest arXiv batch across AI, LLMs, recommendation, advertising/CTR, sequential modeling, games, and related areas.
>
> **Method**: arXiv Export API sweeps over `cat:cs.AI OR cat:cs.LG OR cat:cs.CL OR cat:cs.IR OR cat:cs.NE OR cat:stat.ML OR cat:cs.GT OR cat:cs.MA` sorted by `submittedDate` descending (newest 20 entries); plus a dedicated `cat:cs.IR` sweep (newest 15) for recommendation/advertising topics, and a `cat:cs.GT OR cat:cs.MA` sweep (newest 10) for games and multi-agent topics. The export API was rate-limited (HTTP 429/500); retries with backoff were used throughout.
>
> **Scope**: 30 papers — A(1) + B(4) + C(5) + D(6) + E(3) + F(1) + G(3) + H(1) + I(6). Papers whose rendered paper HTML (arXiv `/html/<id>`) does not state an affiliation are marked "not stated on arXiv". All numbers are **author-reported** and not independently reproduced.

## Summary

- **Advertising/CTR**: X-split Argus proposes offline-computed, reusable history-token sets (produced by an end-to-end history compressor) consumed by an online ranker via cross-attention, with teacher distillation from uncompressed histories; offline NE down 0.81%; A/B +4.65% business metric / +2.96% clicks.
- **Recommendation/sequential**: LQ-Rec (Late Quantization) — non-autoregressive generative retrieval with additive error bounds and anytime compression; CONCORD-Rec — reliability-conditioned diffusion recommendation with counterfactual catalog-partition utility (+4% NDCG; +14.63% under 30% conflict); ReflectRec — verifier-guided LLM recommendation for MovieLens (+16.25/+4.46 pp Hit@10); MARS — agentic multi-stage pipeline orchestration with three-stage post-training.
- **Games**: feature-attribution stability bands via the core/nucleolus/bargaining sets of explained-variance games; exact complexity thresholds for network Cournot (cubic always tractable; quartic ≤ 3 firms/market; quintic ≤ 2); competitive ratio < 1/2 for subadditive auctions; GridAnchor cyber-physical hallucination detection (0.846 AP); Kaer security-aware replanning (benchmark: Cintra).
- **LLM training/inference**: WeightCode (weight-space programming; up to 99.8% command composition match); RoCoKV (uncertainty-aware pruning + redundancy-aware selection, vLLM CUDA plugin; 1.27X/1.43X speedups); dimension-free error-feedback buffer bounds; curvature-guided composable fine-tuning dynamics; LoongForge-Embodied (1.47x–4.38x training speedups).
- **LLM safety/integrity**: SciIntBench compliance study (models identify misuse in 91% of covert cases but refuse in 34%; rephrasing + system prompts raise refusal to 86–88%); DRJanus HDR-gain-map camouflage (evades 6 moderation services + 9 VLMs).
- **Agents**: SkillPlumber — instruction-level coverage-driven skill self-evolution (+25.6–30.4 pp vs initial skill).
- **Voice**: Turkish end-of-turn detection with a fine-tuned TurnGPT (best-calibrated; minimal response delay).
- **VLM/robotics**: Raptor — training-free tree adaptation for VLM speculative decoding (up to 2.39x); ActMem — in-context memory with a Latent Memory CoT (71.1% on RoboMemArena); demonstration-free skill composition for navigation/manipulation.
- **Planning**: planning-width approximation hardness (NP-hard to distinguish width 1 from Θ(N) even with a unique optimal plan).
- **Medical/scientific**: BraTS-GoAT consensus pseudo-labeling (DSC 0.834); TSGSurv — two-stage survival generative modeling with variance correction; quantum ECG reconstruction via preconditioned VQLS; FamilySpace — emergent chemical semantics in crystal VAEs; PAIR-MED — multilingual medical reasoning across 12 languages.

---

## A. Advertising, CTR and Ranking

### 1. X-split Argus: Learning Reusable History Tokens for Efficient CTR Prediction
- **arXiv**: [2611.24283](https://arxiv.org/abs/2611.24283)
- **Date**: 2026-11-18
- **Authors**: Alexander Ploshkin, Nikita Stepanov, Alexey Pismenny, Viacheslav Ovchinnikov, Nikolay Savushkin
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.IR
- **Abstract**: Accurate click-through rate (CTR) prediction depends on user representations that capture both persistent preferences and recent intent, yet processing extensive behavioral histories for every ranking request is costly under production compute and latency constraints. We present X-split ARGUS, a framework for ad ranking whose history compressor and online ranker are trained end to end. The compressor encodes past interactions into a compact set of tokens that are computed offline and reused across candidates, while the online ranker scores ads through cross-attention to these tokens and representations of recent events. Training combines an autoregressive loss for click feedback with distillation of candidate-specific click logits from a larger teacher that scores each candidate using the uncompressed history. The number of compressed history tokens and the length of recent history can be adjusted to fit serving compute and latency budgets. Offline evaluation shows a 0.81% relative reduction in normalized entropy (NE) compared with the production baseline. Deployment in a large-scale real-time bidding system increases online inference cost by 15% relative to the production baseline. An online A/B test against this baseline yields relative gains of 4.65% in a business metric reflecting the monetary value of conversions generated for advertisers and 2.96% in clicks.
- **Key innovations**:
  - End-to-end trained history compressor producing offline, reusable token sets consumed by all candidates.
  - Online ranker combining cross-attention to compressed history with recent-event representations.
  - Distillation of candidate-specific click logits from an uncompressed-history teacher.
  - Tunable token-count / recent-history-length budget knobs for serving cost.
  - Offline 0.81% NE improvement; online A/B: +4.65% business metric, +2.96% clicks.

---

## B. Recommendation, Sequential Modeling and Retrieval

### 2. LQ-Rec: Late Quantization for Sequential Recommendation
- **arXiv**: [2611.25256](https://arxiv.org/abs/2611.25256)
- **Date**: 2026-11-18
- **Authors**: Satoshi Koide, Yueqi Wang, Julian McAuley
- **Institution/Company**: Toyota Motor North America; UC San Diego
- **Categories**: cs.IR
- **Abstract**: Generative retrieval (GR) for sequential recommendation compresses each item into a short semantic ID and trains an autoregressive decoder to generate next-item codes from a user history. While appealing for cold-start handling and storage, autoregressive GR suffers a structural scaling limit: typically, longer semantic IDs reduce quantization error in principle but degrade ranking quality and quadratic memory usage against semantic ID length. We propose Late Quantization (LQ), a non-autoregressive paradigm that confines discretization to the output (item) side of the pipeline. The encoder and scoring rule operate in continuous space, while items are stored and matched as semantic IDs produced by an end-to-end-trained residual quantizer. This architectural shift permits an additive error decomposition and a pairwise ordering theorem that jointly bound the quantization-induced ranking drop, a structural guarantee absent in prior semantic-ID recommenders. Across four public benchmarks, the resulting recommender, LQ-Rec, delivers three capabilities simultaneously: ranking quality improves monotonically with the semantic-ID length and outperforms existing baselines; a single trained model supports anytime compression, tuning ranking quality against inference cost without retraining; and LQ-Rec shows superior generalization on a memorization/generalization partition.
- **Key innovations**:
  - Non-autoregressive generative recommendation; discretization moved entirely to the output side.
  - Additive error decomposition + pairwise ordering theorem bounding the quantization-induced ranking drop.
  - Quality-vs-ID-length monotonicity; anytime compression without retraining.
  - Stronger generalization on the memorization/generalization split.

### 3. ReflectRec: Cycle-Consistency Preference Verification for LLM-based Recommendation
- **arXiv**: [2611.23969](https://arxiv.org/abs/2611.23969)
- **Date**: 2026-11-18
- **Authors**: Dae Kyoo Kim, Heejung Cho, Sungmoo Hong, Eunil Park
- **Institution/Company**: Sungkyunkwan University; NAVER Corp; KIAT; KT Corp; Jaume I University
- **Categories**: cs.CL, cs.IR
- **Abstract**: CoT-style LLM recommenders generate a natural-language preference note as a chain-of-thought prefix to ranking, but the note is trusted without verification, and the ranker never consults behaviorally similar users. We propose ReflectRec, organized around a preference-to-history round-trip verifier whose recall score serves as an operational signal of preference-to-history recoverability, enabling conditional regeneration for low-recoverability preferences and selection among regeneration attempts. Around this verifier, we wire a semantic Stage-1 prompt, conditional regeneration, and Forward-Look retrieval that injects future watches of behaviorally similar users as a collaborative hint. On MovieLens-100K and MovieLens-1M, the full pipeline outperforms CoT4Rec-ICL by +16.25 / +4.46 pp Hit@10, with positive gains across all ValScore buckets and three LLM backbones (Qwen3-30B, Qwen2.5-72B, and Llama-3.3-70B). We also observe a similar verifier-guided regeneration pattern on Amazon Electronics.
- **Key innovations**:
  - Preference-to-history round-trip verifier; recall score as operational recoverability signal; conditional regeneration of low-recoverability notes.
  - Forward-Look retrieval injecting future watches of behaviorally similar users as collaborative hints.
  - +16.25 / +4.46 pp Hit@10 over CoT4Rec-ICL on MovieLens-100K/1M across three backbones.

### 4. CONCORD-Rec: Catalog-Conditioned Modality Utility for Semantic-ID Diffusion Recommendation
- **arXiv**: [2611.23710](https://arxiv.org/abs/2611.23710)
- **Date**: 2026-11-18
- **Authors**: Haopeng Jin, Bingkang Shi, Tao Yu, Yifei Ma, Hao Liu, Hongzhu Yi, Jinwen Luo
- **Institution/Company**: Tencent; University of Chinese Academy of Sciences; Beijing University of Posts and Telecommunications († = corresponding authors)
- **Categories**: cs.IR
- **Abstract**: Multimodal generative recommendation with discrete semantic identifiers (SIDs) requires distinguishing historical modalities that merely alter token predictions from those that genuinely reduce catalog-level ambiguity. When audiovisual, visual, or textual streams are missing, degraded, or semantically conflicting, uniform fusion and unconstrained token gates can propagate misleading content across iterative denoising steps. We propose CONCORD-Rec, a reliability-conditioned discrete diffusion recommender supervised by counterfactual catalog-partition utility. Given a fixed tokenizer and a partially masked SID state, CONCORD-Rec evaluates out-of-fold teacher coalitions over the exact feasible catalog support and aggregates item posteriors across the target code partition at each unresolved position. Rather than distilling raw token probabilities directly, the resulting counterfactual loss differences supervise an availability-masked tokenwise gate that allocates bounded modality residuals around a behavioral denoiser while retaining an exact behavioral fallback slot. We establish theoretical fixed-support ranking stability bounds under gate perturbations and evaluate position-level and code-conditional allocation across audiovisual and image-text recommendation benchmarks under controlled missingness, signal degradation, and semantic conflict. Across 20 source-compatible protocol–dataset rows, CONCORD-Rec improves NDCG by 4%; under matched 30% conflict it improves NDCG by 14.63%. The full-vs-uniform-T=16 sweep improves quality by 2.00-3.58% while reducing p95 latency by up to 86.89%.
- **Key innovations**:
  - Reliability-conditioned discrete diffusion recommender supervised by counterfactual catalog-partition utility.
  - Availability-masked tokenwise gates allocate bounded modality residuals around a behavioral denoiser; exact behavioral fallback retained.
  - Theoretical fixed-support ranking stability bounds under gate perturbations; position-level + code-conditional allocation.
  - +4% NDCG overall; +14.63% under 30% conflict; 2.00–3.58% quality at T=16 with p95 latency cut up to 86.89%.

### 5. MARS Technical Report
- **arXiv**: [2611.24006](https://arxiv.org/abs/2611.24006)
- **Date**: 2026-11-18
- **Authors**: Tong Liu, Chaoqun Hou, Longxiang Xiong, Junhong Lou, Jiaqi Zheng, Qixin Li, Zixin Zhao, Yong Duan, Xiannian Hu, Fengze Jiang, Yu Zhu, Cheng Guo, Xinyuan Qi, Zi Zhuang, Ping Liu, Lv Shao, Zongwei Wang
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.IR
- **Abstract**: Modern industrial recommender systems use multi-stage cascades--retrieval, pre-ranking, ranking, and re-ranking--to narrow millions of candidates to a personalized list. While each stage deploys sophisticated models, pipeline-level decisions on channel activation, quotas, model selection, and score fusion remain engineer-tuned and user-agnostic within each scenario. This report presents MARS (Multi-stage Agentic Recommendation System), extending personalization from individual-stage predictions to full pipeline orchestration. A near-line agent built on fine-tuned Qwen3-0.6B generates per-user configurations--a seven-dimensional action covering pipeline mode, retrieval quotas, model selection, fusion weights, and reranker settings--from a constrained action space. Configurations are validated, cached, and consumed asynchronously; the cascade never waits for LLM inference. Schema checks, fallbacks, and a kill switch ensure serving safety. The policy is trained in three stages: Confidence-aware SFT distills schema-valid generation from a teacher model; Format-Anchored Preference Optimization (FAPO) learns action preferences via ActionMask with posterior weighting; Group Relative Policy Optimization (GRPO) refines the policy through Sandbox replay with a frozen reward model, without exposing exploratory actions to live traffic. Two-week A/B tests across five Taobao scenarios with over ten million daily users show positive gains on all key metrics. The largest reach +5.22% V2P and +7.34% GMV, with positive CTR lifts on both click surfaces. About 20% of requests use a lightweight Minimal mode, and deployment shows 12 ms lower mean serving latency versus production.
- **Key innovations**:
  - Agentic multi-stage pipeline orchestration: a near-line Qwen3-0.6B agent generates per-user seven-dimensional actions (mode, quotas, model selection, fusion, reranker).
  - Three-stage post-training: Confidence-aware SFT → Format-Anchored Preference Optimization (FAPO) → Group Relative Policy Optimization (GRPO) via Sandbox replay.
  - Serving safety: schema checks, incumbent fallbacks, master kill switch; async caching means the cascade never waits for LLM inference.
  - A/B evidence: +5.22% V2P, +7.34% GMV; ~20% of requests in Minimal mode; 12 ms lower serving latency vs production.

---

## C. Games, Game Theory and Sequential Decision

### 6. Stability Bands for Feature Attribution: The Core, the Nucleolus and the Bargaining Set of Explained-Variance Games
- **arXiv**: [2611.25238](https://arxiv.org/abs/2611.25238)
- **Date**: 2026-11-18
- **Authors**: Fernando Delbianco, Fernando Tohmé
- **Institution/Company**: Department of Economics, Universidad Nacional del Sur (UNS), Bahía Blanca, Argentina; Institute of Mathematics – CONICET, Bahía Blanca, Argentina
- **Categories**: cs.GT, cs.LG, econ.EM (primary: cs.GT)
- **Abstract**: Shapley-value attributions are the default way of explaining machine-learning predictions in economics, but they report a single number per feature and say nothing about whether a coalition of features that jointly accounts for more than it receives could contest that allocation. We study feature attribution through the core, the nucleolus and the bargaining set of an explained-variance game, in which the worth of a set of features is the variance of the model's predictions that those features generate. For every feature we report a stability band (its range of shares over the core, or over the least core when the core is empty), with the nucleolus as distinguished point and a certificate that the allocation admits no justified objection. Three results organise the approach. First, for linear models the game is exactly 2-additive, with pairwise Harsanyi dividends 2β_iβ_jσ_{ij}, so multicollinearity is what creates coalitional structure. Second, in every 2-additive game the prenucleolus coincides with the Shapley value, the (least) core is point-symmetric around it, and the core is non-empty if and only if every cut of the interaction graph has non-negative weight. The Shapley value thus always lies in the prebargaining set, and stability adds information only through band widths and interactions of order three or more. Third, for convex games the bands have a closed form and any allocation can be certified with one minimum cut. In a hedonic price model, the usual mean-SHAP explanation admits a justified objection by the coalition {Ratings, ROM, Battery}. In a gradient-boosting forecaster of retail orders the exact game has an empty core and strong higher-order interactions; the nucleolus departs from the Shapley value by up to 0.19 variance shares, and sparse third-order surrogates recover it where pairwise ones cannot.
- **Key innovations**:
  - Feature attribution via the core, nucleolus and bargaining set of explained-variance games; stability bands with the nucleolus as distinguished point and justification certificates.
  - Linear models: game is exactly 2-additive (pairwise Harsanyi dividends); multicollinearity creates coalitional structure.
  - General result: prenucleolus = Shapley in 2-additive games; core non-empty iff interaction-graph cuts are non-negative.
  - Closed-form bands for convex games; certifiable via one min-cut.

### 7. GridAnchor: Specialized Multi-Agent AI for Safeguarding Autonomous Energy Systems Against Cyber-Physical Hallucinations
- **arXiv**: [2611.25158](https://arxiv.org/abs/2611.25158)
- **Date**: 2026-11-18
- **Authors**: Abderaouf Bahi, Hasan Masrur
- **Institution/Company**: Computer Science and Applied Mathematics Laboratory (LIMA), Faculty of Science and Technology, Chadli Bendjedid University, P.O. Box 73, El Tarf, 36000, Algeria; Center for Smart Mobility and Logistics (IRC-SML), King Fahd University of Petroleum & Minerals, Dhahran, 31261, Saudi Arabia; Department of Industrial and Systems Engineering, King Fahd University of Petroleum & Minerals, Dhahran, 31261, Saudi Arabia
- **Categories**: cs.MA
- **Abstract**: Autonomous energy systems increasingly chain specialized learned agents, such as a forecaster, a state estimator and a dispatcher that may be a language model. These agents can emit confident outputs that contradict physics, and downstream agents may act on them. We define such cyber-physical hallucinations and their cascades, organize them in eight types, and build CPH-Bench, a generator of labeled episodes on SimBench feeders. We propose GridAnchor, a verification layer whose Physics-Residual Graph Transformer scores every claim from residuals between the claims, the measurements and a linearized grid model. Mondrian conformal p-values with the Benjamini-Hochberg procedure turn the scores into decisions, a root head attributes cascades, and a quadratic program repairs unsafe actions with a voltage margin calibrated at repaired steps. On a simulated rural medium-voltage feeder, GridAnchor reaches a message-level area under the precision-recall curve of 0.846, against 0.837 for the strongest of six baselines, a difference within the confidence interval. It leads on estimates and actions, whereas a self-consistency check that knows the label tolerances reaches 0.874 by leading on forecasts. The false-alarm rate stays within 0.17 percentage points of the nominal level on steps without injected hallucinations. In closed loop, GridAnchor leaves no bus outside the voltage band on the test days, against 0.0700% of the bus-steps without protection, and simpler detectors with the same mitigation come close. Stale but coherent messages and single-bus forecast errors remain mostly undetected.
- **Key innovations**:
  - Cyber-physical hallucination detection and cascade attribution for chained learned energy-system agents.
  - Physics-Residual Graph Transformer + Mondrian conformal + Benjamini-Hochberg + root-cause attribution + calibrated voltage-margin quadratic repair.
  - Closed-loop coverage: no bus outside the voltage band on test days (0.0700% without protection).

### 8. Sharp Complexity Thresholds for Network Cournot Competition
- **arXiv**: [2611.24931](https://arxiv.org/abs/2611.24931)
- **Date**: 2026-11-18
- **Authors**: Mohammad Hajiaghayi, Mohammad Mahdavi
- **Institution/Company**: University of Maryland, College Park
- **Categories**: cs.GT, cs.CC (primary: cs.GT)
- **Abstract**: We determine the approximation complexity of network Cournot equilibrium as a function of demand degree and the number of firms sharing a market. For common, nonincreasing concave polynomial inverse demands, convex quadratic costs of firms' allocation vectors, and rational total capacities, high-precision approximation is polynomial-time solvable for cubic demands, regardless of market size. Quartic demands remain tractable when each market has at most three firms, and quintic demands remain tractable with at most two. These thresholds are exact: approximation at a fixed positive profit-regret tolerance is PPAD-hard for quartic demands with four firms per market, quintic demands with three, and sextic demands with two. Each hardness result uses one fixed demand curve in every market, a constant number of markets per firm, and globally nondecreasing strongly convex quadratic costs. We also give a polynomial-time algorithm for arbitrary-degree nonincreasing concave polynomial demands when each firm's convex polynomial cost depends only on its total production. The algorithm applies to arbitrary access graphs and permits firm-specific inverse demands. Its running time is polynomial in the input size and the logarithm of the inverse accuracy. The algorithm assigns one marginal charge to each firm and adjusts the charges until each firm's total sales approximate the quantity it would produce at that charge.
- **Key innovations**:
  - Exact complexity thresholds for network Cournot approximation: cubic always tractable; quartic tractable ≤ 3 firms/market; quintic tractable ≤ 2.
  - PPAD-hardness for quartic (4 firms), quintic (3), sextic (2) with positive profit-regret tolerance.
  - Polynomial-time algorithm for arbitrary-degree nonincreasing concave demands with firm-specific costs; marginal-charge adjustment.

### 9. The Optimal Competitive Ratio for Subadditive Online Combinatorial Auctions Is Less Than 1/2
- **arXiv**: [2611.24920](https://arxiv.org/abs/2611.24920)
- **Date**: 2026-11-18
- **Authors**: Andrés Cristi, Jiechen Zhang
- **Institution/Company**: EPFL
- **Categories**: cs.GT
- **Abstract**: We construct a four-buyer online combinatorial auction with independent subadditive valuations and a fixed, known arrival order in which every online rule earns strictly less than 1/2 of the expected offline optimum. A common partition, revealed at the third arrival, gives the first three buyers one unit of welfare per item. If the rule uses three distinct partitions, either an item allocated early contributes zero or the fourth buyer's expected value for the remaining bundle is one less than its size. We compute the optimal online and offline welfare exactly and show that a 1/2 guarantee always holds with at most three buyers.
- **Key innovations**:
  - First example where the optimal competitive ratio for subadditive online combinatorial auctions is strictly below 1/2; every online rule earns < 1/2 of the expected offline optimum.
  - Exact optimal online/offline welfare computation used to derive the competitive guarantee.

### 10. Kaer: Security-Aware Replanning for Multi-Agent Systems
- **arXiv**: [2611.24839](https://arxiv.org/abs/2611.24839)
- **Date**: 2026-11-18
- **Authors**: Tushin Mallick, Evan Rose, Matthew Laws, Alina Oprea, Cristina Nita-Rotaru
- **Institution/Company**: Northeastern University
- **Categories**: cs.MA, cs.LG (primary: cs.MA)
- **Abstract**: One popular architecture for multi-agent systems (MAS) relies on an orchestrator that generates an initial plan, coordinates its execution, and dynamically revises the plan based on agent feedback when tasks cannot be fully specified in advance. This dynamic replanning introduces a critical vulnerability: malicious agents can embed instructions within their feedback to hijack the replanning process. Existing defenses focus exclusively on per-tool access control or static, pre-execution policy enforcement, leaving the replanning phase unsecured. We introduce Kaer, a multi-agent framework featuring security-aware replanning. Kaer shields the planner from untrusted agent feedback by conveying diagnostics to the replanning procedure strictly through abstract templates. Plan revisions are restricted to a set of deterministic repair operators, and all modified plans must satisfy preset policies. We create Cintra, a benchmark of simulated user tasks requiring replanning paired with adversarial objectives targeting the replanning phase. Using Cintra, we evaluate both task completion rates and system vulnerability to replanning exploits by malicious agents. Evaluating Kaer on Cintra against Magentic-One (an undefended MAS) and ControlValve (the state-of-the-art defense) demonstrates that Kaer achieves higher robustness than both systems while maintaining comparable utility to ControlValve. Although abstract failure templates slightly constrain utility on select tasks, Kaer enables MAS to perform secure, dynamic plan revisions without exposing the orchestrator to untrusted agent feedback.
- **Key innovations**:
  - Security-aware replanning: diagnostics conveyed through abstract templates; revisions restricted to deterministic repair operators with preset policies.
  - Cintra benchmark of simulated user tasks with adversarial replanning objectives; evaluation against Magentic-One and ControlValve.

---

## D. LLM Training, Serving, Inference and Architecture

### 11. WeightCode: Installing New Capabilities into Neural Networks via Weight-Space Programming
- **arXiv**: [2611.25476](https://arxiv.org/abs/2611.25476)
- **Date**: 2026-11-19
- **Authors**: Bo Li, Taoyong Cui, Bob Zhang, Mengran Li, Chengyang Zhang, Yang Zhang, Pheng Ann Heng, Wanli Ouyang, Zhenfei Yin, Yingcheng Wu, Ling Yang
- **Institution/Company**: University of Macau; National University of Singapore; The Chinese University of Hong Kong; Sun Yat-sen University; Sichuan University; University of Oxford; Stanford University; Peking University
- **Categories**: cs.LG, cs.AI (primary: cs.LG)
- **Abstract**: Neural networks encode learned capabilities in their weights, yet extending those capabilities with explicit task knowledge remains a fundamental challenge. Here we show that Weight-Space Programming (WSP), in which executable programs read, construct or modify a network's weights directly, can install new capabilities within trained neural networks. WeightCode, a WSP framework, uses a frozen language model to write executable weight programs that install new computations into trained neural networks using task knowledge and their existing weights, without gradient-based training. Once installed, the new capabilities run independently of the language model. Given a grammar or eight demonstrations, weight programs enable previously unseen command compositions (0% to 99.8% exact match) and a new pickup action (0% to 98.4% success), while preserving the original command and navigation capabilities. On ImageNet, four weight programs achieve net gains of 8.84-17.62 points while preserving clean accuracy, outperforming the best of eight fine-tuning methods under matched examples, checks, and retention constraints. In a Vision Transformer, causal interventions show that installed noise-correction gates drive robustness gains, while their selective activation preserves clean accuracy. Rerun on five independently trained Vision Transformers without further language model calls, ten weight programs retain 83-110% of their source-network gains on average, whereas copying their fixed weight edits yields negligible gains. Six programs written for an already edited network add 5.23-14.50 points of contrast robustness while retaining the previously installed noise gain. Together, these results establish WSP as a new route to acquiring and accumulating capabilities in trained neural networks through reusable weight programs.
- **Key innovations**:
  - Weight-Space Programming (WSP): executable weight programs written by a frozen LM that install new capabilities into trained networks without gradient-based training.
  - Verified compositions: 0% → 99.8% command match; 0% → 98.4% pickup success; clean-accuracy preservation.
  - Weight programs drive robustness (noise-correction gates) and accumulate across reruns without LM calls.

### 12. RoCoKV: Accelerating LLM Inference Serving through Uncertainty and Redundancy Aware KV Cache Compression
- **arXiv**: [2611.25433](https://arxiv.org/abs/2611.25433)
- **Date**: 2026-11-19
- **Authors**: Payman Behnam, Elaheh Sobhani, Saad Amin, Yahya Hassan, Daniyal Khan, Biswadeep Chakraborty, Tanish Patwa, Souvik Kundu, Alexey Tumanov
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.CL
- **Abstract**: KV cache compression is critical for large reasoning models, where most of the cost comes from long generated reasoning traces rather than the input prompt. These traces often contain redundant and low-utility tokens due to looping, self-verification, and corrections. However, such tokens may still receive high attention scores, making it difficult to remove them without harming the reasoning process. We propose RoCoKV, a KV cache compression method designed for large reasoning models. RoCoKV introduces two key components. First, uncertainty-guided adaptive pruning adjusts the compression strength based on the model's confidence, allocating more memory during uncertain phases and applying stronger pruning when the model is confident. Second, redundancy-aware token selection reduces the impact of tokens that are highly similar to recent reasoning content, encouraging the model to retain more informative and diverse tokens. Beyond the algorithm, we co-design RoCoKV with the serving stack: we develop fused three-phase CUDA decode kernels and integrate them into vLLM as a drop-in plugin that preserves its paged KV layout and CUDA graph capture, turning algorithmic savings into real end-to-end speedups. Extensive experiments across three reasoning benchmarks and two reasoning models demonstrate that RoCoKV consistently improves reasoning accuracy under constrained KV cache budgets, achieving higher accuracy compared to state-of-the-art KV cache compression methods. For DeepSeek-R1-Distill-Llama-8B in vLLM, RoCoKV achieves a 1.27X speedup and 38% higher throughput on AIME25, the most challenging evaluated reasoning benchmark, and a 1.43X speedup and 45% higher throughput on the long synthetic benchmark, compared with Full-KV.
- **Key innovations**:
  - Uncertainty-guided adaptive pruning (confidence-based compression strength).
  - Redundancy-aware token selection (diversity-preserving retention of reasoning tokens).
  - Fused three-phase CUDA decode kernels + vLLM drop-in plugin preserving paged KV and CUDA graphs.
  - 1.27X/1.43X speedups and 38%/45% throughput gains on AIME25/synthetic with improved accuracy.

### 13. Dimension-Free Buffer Bounds for Compressed-Momentum Error Feedback
- **arXiv**: [2611.25463](https://arxiv.org/abs/2611.25463)
- **Date**: 2026-11-19
- **Authors**: Alireza Moayedikia
- **Institution/Company**: Department of Business Technology and Entrepreneurship; Swinburne University of Technology
- **Categories**: cs.LG, math.OC
- **Abstract**: Analyses of error feedback bound the memory buffer through a compressor contraction constant -- r/p for the best rank-r approximation of a p-dimensional spectrum -- which survives into the rate. We show it need not appear at all. When the compressed momentum is re-injected into the pre-compression accumulator, the previous compressed momentum β_1 M_{t-1} is an admissible competitor in the projection, and the buffer obeys ||E_t||_F ≤ (1-β_1)||G_t||_F + γ||E_{t-1}||_F, free of the dimensions m,n and of the rank r. The argument uses only that the compressor is a metric projection onto a closed cone, so it covers top-k selection as well as truncated SVD, holds for every selection from the projection set with no condition on singular-value crossings, and in its trajectory-tracking form assumes nothing about the gradients. In the two-stage template of the standard analyses it replaces a Stage-2 constant of order p^2/r^2 by one of order 1, against Θ(p/r) for the sharpest contraction-based bounds. Transferring the full rate costs a leakage term, which we bound by the step-weighted gradient mass Σ_{u≤t} η_u||G_u||_F and show tight up to a factor √2; the price is an additive O(log^2 T) floor, not a slower rate. On BERT fine-tuning at rank ratio 32/768 the feedback decay costs under 0.008 validation F1.
- **Key innovations**:
  - Dimension-free buffer bound: ||E_t||_F ≤ (1-β_1)||G_t||_F + γ||E_{t-1}||_F, independent of m, n, and rank r.
  - Works for any metric-projection compressor (top-k, truncated SVD); no singular-value crossing assumptions.
  - Removes the O(p/r) Stage-2 constant at the cost of a bounded leakage term (≤ √2 factor; O(log² T) floor).

### 14. Interference Bounds and Merge-Aware Training Dynamics for Composable Fine-Tuned Models
- **arXiv**: [2611.25430](https://arxiv.org/abs/2611.25430)
- **Date**: 2026-11-19
- **Authors**: Alireza Moayedikia
- **Institution/Company**: Department of Business Technology and Entrepreneurship; Swinburne University of Technology
- **Categories**: cs.LG, math.OC
- **Abstract**: Combining fine-tuned models by composing their parameter updates has become a standard alternative to multi-task training. We formalize composability as a property of a collection of task vectors and prove that the excess loss of the merged model is controlled by an interference functional of the cross-task curvature overlap and the signed alignment of the updates. In the quadratic regime this functional equals the excess loss, giving a criterion that is necessary as well as sufficient and that measures the angle between task vectors in the curvature metric rather than the Euclidean one. Fine-tuning under a curvature-guided regularizer -- constructed from curvature statistics of the kind memory-efficient optimizers maintain -- keeps displacement in the base curvature metric below a ceiling set by the penalty coefficient at every iterate, at the standard O(1/√T) non-convex rate. Under a single Loewner comparison between the base statistic and the task curvatures, this control converts into a ceiling on the interference functional, inversely proportional to the penalty coefficient, so that the curvature term of the bound is controlled during training. A first-order term, present because regularized solutions are not stationary for the task loss, is not reduced in the same way. Experiments on an exact non-quadratic model confirm the budget and the ceiling, show the first-order term dominating for strong penalties, and find the curvature-guided penalty slightly better than an isotropic one. In a three-seed transformer study the functional is rank-correlated with merging degradation, but no more strongly than the Euclidean displacement norm.
- **Key innovations**:
  - Interference functional = cross-task curvature overlap × signed alignment of updates; equals excess loss in the quadratic regime.
  - Curvature-guided regularizer (from memory-efficient optimizer curvature statistics) caps displacement below a penalty-coefficient-set ceiling at the standard O(1/√T) rate.
  - Loewner comparison converts displacement ceiling into a ceiling on the interference functional (inversely proportional to penalty).
  - Empirical: budget/ceiling confirmed; first-order term dominates for strong penalties.

### 15. LoongForge-Embodied: A Unified Framework for Training Heterogeneous Embodied Models
- **arXiv**: [2611.25460](https://arxiv.org/abs/2611.25460)
- **Date**: 2026-11-19
- **Authors**: LoongForge Team
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.AI
- **Abstract**: Training Vision-Language-Action (VLA) models and World-Action Models (WAMs) is computationally expensive, while their heterogeneous architectures and fragmented training stacks make system optimizations difficult to reuse across models. To address these challenges, we present LoongForge-Embodied, a native-PyTorch framework that unifies and accelerates the training of heterogeneous embodied models. At its core, LoongForge-Embodied introduces a common abstraction layer that decouples model-specific implementations from shared training infrastructure, enabling cross-model reuse without constraining individual architectures or execution requirements. Building on this unified infrastructure, the framework combines reusable acceleration mechanisms with model-specific and hardware-aware optimization strategies across computation, execution, memory, data I/O, and distributed communication, including FP8-based communication optimizations for DDP and FSDP. Beyond training acceleration, LoongForge-Embodied integrates a unified data infrastructure with a pipeline for synthesizing robot data from egocentric data, and an efficient evaluation framework that supports concurrency and optimized computation in simulator. Experiments across representative VLA and WAM models demonstrate 1.47x-4.38x end-to-end training throughput improvements over their corresponding open-source baselines, as well as 4.1x-23.2x faster evaluation under the same protocols.
- **Key innovations**:
  - Unified abstraction layer: common training infrastructure for heterogeneous VLA/WAM models; cross-model reuse without constraining architectures.
  - Acceleration: reusable mechanisms across computation/execution/memory/data I/O/distributed communication; FP8-based DDP/FSDP communication.
  - Data/eval: egocentric-data synthesis pipeline; concurrent optimized simulator evaluation.
  - 1.47x–4.38x training speedups; 4.1x–23.2x faster evaluation.

### 16. A Four-Level Executable Validation Protocol for Evaluating LLM-Generated Topology Specifications of Physics-Based HVAC Digital Twins
- **arXiv**: [2611.25471](https://arxiv.org/abs/2611.25471)
- **Date**: 2026-11-19
- **Authors**: Younghwan Joo, Jeonghoon Han, Sanghyun Oh, Soosik Bang, Sung-il Kim
- **Institution/Company**: not stated on arXiv
- **Categories**: eess.SY, cs.AI, cs.LG, cs.SE (primary: eess.SY)
- **Abstract**: Physics-based digital twins of air conditioning, a principal energy consumer in manufacturing and buildings, can be generated automatically from a declarative specification of its equipment, connections, and sizing. Large language models (LLMs) now write such specifications from plain-language descriptions. Evaluations of these specifications stop at parse success, completed runs, or textual similarity, and cannot reject a model that converges in simulation but is physically wrong. In this study, a four-level protocol is proposed that tests whether an LLM-written specification not only executes but also yields a physically valid digital twin. Each specification is executed through static validity, model build, simulation convergence, and behavioral equivalence with a hidden reference model within bands calibrated by ±20% sizing perturbations. The protocol was applied to eight LLMs and fourteen HVAC topologies, five describing an existing low-humidity test chamber. To test for authorship bias, engineers and a second model family also described six topologies. Within three repairs, seven of eight models built in 98.6 to 100% of trials, with simulations converging in at least 80.0%, but reached behavioral equivalence in only 50.0 to 98.6%. About half of the failed trials converged, but not to the reference steady state, mostly in desiccant rotor systems. Pooled pass rates varied by under five percentage points across description authors. These results imply that the physics hardest to model in each field, here the desiccant rotor, must enter the generation framework as validation levels. The protocol can be adapted to other fields that generate executable digital twins from declarative specifications.
- **Key innovations**:
  - Four-level executable validation: static validity → model build → simulation convergence → behavioral equivalence vs hidden reference within ±20% sizing bands.
  - Applied to 8 LLMs × 14 HVAC topologies (5 real low-humidity chamber); engineers + second model family authored 6 for bias checks.
  - 7/8 models built 98.6–100% after ≤3 repairs; simulation convergence ≥80%; behavioral equivalence only 50.0–98.6% — desiccant rotors are the hard physics.
  - Scope: per-field hard physics must enter the generation framework as validation levels.

---

## E. LLM Safety, Integrity and Other AI

### 17. Why Do LLMs Help with Scientific Misconduct Requests and What to Do About It?: Increasing the Trustworthiness of AI for Science
- **arXiv**: [2611.25492](https://arxiv.org/abs/2611.25492)
- **Date**: 2026-11-19
- **Authors**: Almene De Meran Meguimtsop, Daniel E. Acuna
- **Institution/Company**: Department of Computer Science, University of Colorado Boulder, Boulder, CO, USA; Center for AI in Knowledge Institutions (AIKI), University of Colorado Boulder, Boulder, CO, USA; ReviewerZero AI Inc., Boulder, CO, USA
- **Categories**: cs.AI
- **Abstract**: Large language models (LLMs) support scientific research, but some of that assistance can also undermine research integrity. Existing safety evaluations in science often measure whether models refuse misconduct requests, but rarely explain whether they even recognize the problem or why they comply. We investigate this gap across 8 LLMs using SciIntBench, an existing benchmark of 1,350 prompts about scientific research integrity. We examine the reasons behind compliance in four steps. First, when asked directly whether fulfilling a request would involve misconduct, models overwhelmingly identify such requests, even in the Most Covert cases (91%), while they refuse to carry out the request in only 34% of cases. Second, we examine which request characteristics are associated with refusal using features that capture how the request is framed, how much the assistant has been told about what it is helping to hide, and how the goal and the user's stake are stated, among others. Third, we estimate that the most significant effect was to rephrase requests as questions about permissibility rather than instructions, which increased refusal from 52% to 88%. Finally, we test two system-prompt fixes: asking models to assess the request before responding and reminding them of responsible conduct of research principles. These changes increase refusal rates on adversarial requests from 58% to 87% and 86%, respectively. Our findings show that models recognize wrongful requests but still help users violate integrity. Understanding why these failures occur and testing ways to reduce them offer promising paths toward more trustworthy AI for science.
- **Key innovations**:
  - SciIntBench: 1,350-prompt benchmark of scientific research integrity; models identify misuse in 91% of Most Covert cases but refuse in only 34%.
  - Framing matters: rephrasing instructions as permissibility questions raised refusal 52% → 88%.
  - Two system-prompt fixes (pre-assessment; responsible-conduct principles) raised refusal to 87% and 86%.

### 18. A Wolf in Sheep's Pixels: Visual Camouflage Attacks via HDR Gain Maps
- **arXiv**: [2611.25469](https://arxiv.org/abs/2611.25469)
- **Date**: 2026-11-19
- **Authors**: Qi Shen, Yujia Gong, Yue Zhao, Tong Liu
- **Institution/Company**: University of the Chinese Academy of Sciences; Institute of Information Engineering
- **Categories**: cs.CV, cs.AI (primary: cs.CV)
- **Abstract**: An image can pass automated safety checks while showing harmful content to its human viewer. We introduce DRJanus, a visual camouflage attack that exploits the gap between standard dynamic range (SDR) processing and high dynamic range (HDR) display. Automated systems often read only an image's SDR base, whereas HDR viewers reconstruct its appearance using an auxiliary gain map. DRJanus inverts this reconstruction to embed two independently chosen color images in a single JPEG, without querying or optimizing against the target model. It preserves the chosen SDR base exactly and reconstructs HDR targets at an average PSNR of 43.03 dB across 400 images. On a benchmark of 100 sexual-content images, DRJanus evades detection by all six tested commercial moderation services and nine vision-language models. Across five agents, each evaluated on 120 task cases per threat setting, attack success ranges from 31.67% to 100% for moderation evasion and from 95% to 100% for task manipulation. We also explore cross-view consistency checks as a mitigation. These findings expose a gap in visual trust: securing what a machine reads does not secure what a user sees. A demo is available at https://qshen0629.github.io/DRJanus/
- **Key innovations**:
  - DRJanus: HDR-gain-map camouflage embedding two independently chosen images in one JPEG, preserving the SDR base exactly.
  - Evades 6 moderation services + 9 VLMs; moderation evasion 31.67–100%, task manipulation 95–100% (5 agents × 120 cases).
  - Cross-view consistency checks proposed as mitigation.

### 19. Evolve Where It Matters: Coverage-Guided Self-Evolution of Agent Skills
- **arXiv**: [2611.25429](https://arxiv.org/abs/2611.25429)
- **Date**: 2026-11-19
- **Authors**: Boyin Tan, Jiadong Zhang, Xiaosong Ma, Chun Jason Xue, Xiaowei Huang, Youcheng Sun
- **Institution/Company**: Mohamed bin Zayed University of Artificial Intelligence; University of Liverpool
- **Categories**: cs.CL, cs.AI (primary: cs.CL)
- **Abstract**: Agent skills package procedural knowledge as natural-language instructions, and a skill helps only when its instructions are correct and properly followed by the agent. Self-evolving agents revise their own skills from the runs they make, but existing methods judge each run as a whole, by its outcome or by where it went wrong, and cannot tell whether a failure comes from a wrong instruction or from one the agent did not follow. Instruction-level coverage was introduced to test skills and labels each instruction of a run as follow, not-follow, or not covered, which separates these causes. We leverage it for skill self-evolution with SkillPlumber, a framework in which an agent evolves its own skills where coverage shows they fall short. A persistent root cause analysis agent turns each label into a revision question and checks each revision against the next run, while a maintainer distills investigations across tasks into a shared strategy library. Across three benchmarks and three executors, SkillPlumber solves 64.7% to 70.5% of the tasks, 25.6 to 30.4 percentage points higher than the initial skill and 8.7 to 14.0 percentage points higher than the strongest baseline, and removing coverage reduces recovered failures by 20.8% on SkillsBench with GPT-5.5.
- **Key innovations**:
  - SkillPlumber: skill self-evolution driven by instruction-level coverage (follow/not-follow/not-covered labels separate instruction vs agent-following failures).
  - Root cause analysis agent + maintainer distilling across tasks into a shared strategy library.
  - +25.6–30.4 pp over initial skill, +8.7–14.0 pp over strongest baseline (3 benchmarks × 3 executors).

---

## F. Voice Agents and Speech

### 20. When Should a Voice Agent Speak? End-of-Turn Detection in Turkish
- **arXiv**: [2611.25489](https://arxiv.org/abs/2611.25489)
- **Date**: 2026-11-19
- **Authors**: Ahmet Tuğrul Bayrak, Fatma Nur Korkmaz, Mustafa Sertaç Türkel, Nur Yağmur Tuncer
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.AI, cs.CL (primary: cs.AI)
- **Abstract**: A voice agent that waits for a fixed silence before replying either interrupts users who pause mid-utterance or responds late to users who have finished. This study examines the decision at the onset of silence, using turn ends and turn-internal pauses extracted from the Real-TurnTurk corpus of Turkish dyadic video calls. A fine-tuned Turkish TurnGPT model, a zero-shot Turkish language model and a deployed multilingual detector are compared, together with voice-activity timing and facial features, under recording-disjoint and speaker-disjoint evaluation with paired cluster bootstrap tests. On held-out recordings, the fine-tuned model separates turn ends from pauses better than both text baselines and is the best calibrated of the three. Timing features of the current speaker are similarly informative, and their combination with the fine-tuned text score gives the best timing-based results; with logistic regression, this combination also outperforms the same combination with either text baseline. In a latency simulation, adding the text score to a silence timeout shortens the mean response delay at the same interruption rate. On automatic Whisper transcripts, the fine-tuned model retains its advantage over the zero-shot model.
- **Key innovations**:
  - Real-TurnTurk corpus of Turkish dyadic video calls with turn-end vs pause labels.
  - Fine-tuned Turkish TurnGPT beats zero-shot baselines and is the best calibrated for end-of-turn detection.
  - Combining text score with speaker timing features improves the interruption/latency tradeoff.

---

## G. Vision-Language Models, Vision and Robotics

### 21. Raptor: Rejection-aware Adaptive Tree based on Speculative Decoding
- **arXiv**: [2611.25436](https://arxiv.org/abs/2611.25436)
- **Date**: 2026-11-19
- **Authors**: Qishu Hu, Haozhao Wang, Zicong Hong, Yufeng Zhan, Yuanqing Xia
- **Institution/Company**: School of Automation; Beijing Institute of Technology; Beijing, China 100081; School of Computer Science and Technology; Huazhong University of Science and Technology; Wuhan, China 430074; Distributed Computing Lab; École Polytechnique Fédérale de Lausanne; Lausanne, Switzerland 1015
- **Categories**: cs.CV, cs.AI (primary: cs.CV)
- **Abstract**: Tree-structured speculative decoding accelerates vision-language models (VLMs) by verifying multiple candidate continuations in parallel. However, long visual contexts increase the cost of speculative computation, making candidate coverage and redundant expansion important considerations beyond tree topology adaptation. We propose Raptor, a training-free framework that uses rejection feedback to jointly regulate candidate coverage and drafting effort. Our key insight is that acceptance length alone cannot distinguish insufficient candidate coverage from excessive deep expansion, and these conditions require different allocation decisions. Raptor therefore extracts complementary rejection-aware signals to characterize speculative progress, frontier coverage, and redundant expansion. These signals jointly guide bounded, momentum-smoothed updates of tree depth, branching width, and drafting budget, together with execution control that limits unnecessary drafting and progressively restores expansion when appropriate. Extensive experiments with two VLMs across seven multimodal benchmarks demonstrate the effectiveness of Raptor, achieving up to 2.39x average speedup over autoregressive decoding.
- **Key innovations**:
  - Training-free tree adaptation for VLM speculative decoding using rejection-aware signals (coverage, frontier, redundancy).
  - Momentum-smoothed updates of tree depth/branching/budget + execution control limiting drafting.
  - Up to 2.39x average speedup over autoregressive decoding (2 VLMs × 7 multimodal benchmarks).

### 22. ActMem: From Latent Memory Reasoning to Grounded Robotic Action
- **arXiv**: [2611.25461](https://arxiv.org/abs/2611.25461)
- **Date**: 2026-11-19
- **Authors**: Linfeng Dong, Jianwei Niu, Jiuyi Zhao, Ruibing Feng, Xinghao Wu, Wu Yang, Shuai Tao, Wulong Liu, Mu Li
- **Institution/Company**: Beihang University; Beta Infinity
- **Categories**: cs.CV, cs.LG (primary: cs.CV)
- **Abstract**: Vision-Language-Action (VLA) models have shown promising results in real-world long-horizon manipulation, where memory plays a crucial role. However, existing memory-augmented VLAs either retrieve past observations without reasoning about what they imply, or reason over the full history in a shared context where it crowds out current perception. Cognitive science treats them as distinct systems: memory reconstructs past experience to decide what to do, while perception guides how to act. We therefore propose ActMem, an in-context memory framework that decouples memory reasoning from perceptual grounding within a single vision-language backbone. Built on a vision-language model with native video understanding, ActMem infers the current subtask from a timestamped interaction history and keeps the hidden states formed during this inference as a Latent Memory Chain-of-Thought (Memory CoT), which conditions a flow-matching action expert. Perception Attention further lets the expert attend directly to the current view. To keep inference fast under long histories, Efficient Memory CoT Inference reuses computation across consecutive decisions without changing the output. ActMem achieves 71.1% task success and 80.8% completion success on RoboMemArena, surpassing the strongest baseline by 7.5 and 8.7 percentage points, and 73.8% average success on MIKASA-Robo, the best among all compared methods. In the real world, it reaches 68.8% average success on exogenous, endogenous, and traceless memory tasks, 10.0 percentage points above the strongest memory-augmented VLA. Code and checkpoints will be released at https://github.com/LigphiDonk/ActMem and https://huggingface.co/donk111/ActMem.
- **Key innovations**:
  - ActMem: decoupling memory reasoning (Latent Memory CoT) from perceptual grounding in a single VLM backbone.
  - RoboMemArena: 71.1% task success (+7.5 pts vs strongest baseline), 80.8% completion; MIKASA-Robo: 73.8%.
  - Real-world: 68.8% on exogenous/endogenous/traceless memory tasks (+10.0 pts).

### 23. Demonstration-Free Skill Composition for Navigation and Manipulation
- **arXiv**: [2611.25462](https://arxiv.org/abs/2611.25462)
- **Date**: 2026-11-19
- **Authors**: Madeleine Nouri, Gelareh Mohammadi, Francisco Cruz
- **Institution/Company**: School of Computer Science and Engineering, University of New South Wales, Sydney, Australia; Escuela de Ingeniería, Universidad Central de Chile, Santiago, Chile
- **Categories**: cs.RO, cs.AI (primary: cs.RO)
- **Abstract**: Hierarchical reinforcement learning enables sequential tasks to be represented as compositions of separately trained skills. This paper evaluates demonstration-free hierarchical pipelines for MiniGrid navigation and robotic manipulation, comparing their training requirements and task performance with flat reinforcement learning baselines. The evaluation concerns complete pipelines with task-specific observation, reward and control structures. In navigation, two parameterised skills are reused across unseen FourRooms layouts under manually specified high-level plans. In manipulation, reaching, grasp alignment and lifting are trained separately, with downstream skills initialised from states collected during predecessor rollouts. Across unseen navigation layouts, the hierarchical pipeline substantially outperforms the evaluated flat DQN baselines while requiring fewer training interactions. In manipulation, the hierarchical chain requires fewer training steps than flat SAC and exhibits lower observed variation across seeds. The frozen Pick and Lift skills are further reused for stacking by training an additional Place skill.
- **Key innovations**:
  - Demonstration-free hierarchical pipelines for MiniGrid navigation and robotic manipulation.
  - Reused parameterized navigation skills; manipulation chain: reaching/grasp/lift → Place for stacking.
  - Substantially outperforms flat DQN/SAC baselines on navigation layouts with fewer interactions; lower seed variation in manipulation.

---

## H. Planning and Decision Theory

### 24. Planning Width Is Hard to Approximate Even Given the Unique Optimal Plan
- **arXiv**: [2611.25484](https://arxiv.org/abs/2611.25484)
- **Date**: 2026-11-19
- **Authors**: Viet Bac Nguyen
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.DS, cs.AI (primary: cs.DS)
- **Abstract**: For each fixed $k$, iterative-width search finds optimal plans in polynomial time on tasks of bounded tuple-chain width, but the approximability of planning width has remained open even when an optimal plan is supplied. When all optimal plans visit the same state sequence, we characterize set and chain width as hitting numbers of competing states. We construct positive-precondition STRIPS tasks with a supplied unique optimal plan, a single reachable goal state, binary branching, and constant-size actions. Every reachable state lies on a goal-reaching execution at most one action longer than optimal, yet distinguishing width $1$ from $Θ(N)$, where $N$ is the number of atoms, is NP-hard for set, chain, and goal-admissible width. Unless $\mathrm{P}=\mathrm{NP}$, no polynomial-time algorithm achieves a one-sided approximation factor $o(N)$ or a symmetric factor $o(\sqrt{N})$, and simple estimates attain both orders. For positive-precondition tasks with a supplied unique optimal plan of length at least two, testing set or chain width against a threshold $k\geq 1$ is coNP-complete for each fixed $k$ and $\Sigma_2^{\mathrm{P}}$-complete when $k$ is part of the input. Both results also hold for goal-admissible width if only one goal state is reachable. On an explicit state graph, a greedy algorithm approximates set width within a logarithmic factor even when optimal plans branch. Thus, knowing an optimal plan does not eliminate the difficulty of certifying substantially smaller width.
- **Key innovations**:
  - Lower bounds: NP-hard to distinguish width 1 from Θ(N) even with a unique optimal plan; no poly-time approximation better than o(N) or o(√N).
  - coNP-complete (fixed k) / Σ₂^P-complete (k as input) threshold testing of set/chain width with supplied unique optimal plan.
  - Greedy approximates set width within a log factor even when optimal plans branch.

---

## I. Medical and Scientific AI

### 25. AIstatLab at BraTS-GoAT 2026 Task 3: Quality-Controlled Consensus Pseudo-Labeling and Dense Expert Adaptation
- **arXiv**: [2611.25477](https://arxiv.org/abs/2611.25477)
- **Date**: 2026-11-19
- **Authors**: Heeseung Shin, Changwon Lim
- **Institution/Company**: Department of AI in Medicine, Chung-Ang University, Seoul 06974, Republic of Korea; Department of Statistics and Data Science, Chung-Ang University, Seoul 06974, Republic of Korea
- **Categories**: eess.IV, cs.AI (primary: eess.IV)
- **Abstract**: BraTS-GoAT Task 3 evaluates brain-tumor segmentation across heterogeneous entities using shared ET, TC, and WT regions. We present a 3D ResidualEncoderUNet trained with quality-controlled consensus pseudo-labels, a training-only nested-region objective, and a four-expert bottleneck adapter. Five-fold ResEnc-M/L teachers generated predictions for 1,138 unlabeled cases; fusion, hierarchy enforcement, and confidence-and-agreement screening retained 983 for training with 1,351 annotated cases. The final five-fold ResEnc-M entry achieved mean DSC 0.834, mean NSD 0.510, and Acalc = 0.6720 on the validation server. Component effects were modest and region-dependent, with the clearest gains on ET. Source code is available at https://github.com/HeeSeung-Shin/Brats2026-Goat-HS.
- **Key innovations**:
  - Quality-controlled consensus pseudo-labeling: fusion, hierarchy enforcement, confidence-and-agreement screening (983/1138 retained).
  - Training-only nested-region objective + four-expert bottleneck adapter.
  - Five-fold ResEnc-M/L teachers on 1,138 unlabeled cases; final DSC 0.834, NSD 0.510.

### 26. Faithful Generative Modeling for Censored Time-to-Event Data: From Distributional Fidelity to Statistical Inference
- **arXiv**: [2611.25464](https://arxiv.org/abs/2611.25464)
- **Date**: 2026-11-19
- **Authors**: Yin Liu, Shanshan Zhao, Didong Li
- **Institution/Company**: Department of Biostatistics, University of North Carolina at Chapel Hill; Biostatistics and Computational Biology Branch, National Institute of Environmental Health Sciences
- **Categories**: stat.ME, math.ST, stat.AP, stat.ML (primary: stat.ME)
- **Abstract**: Synthetic data has emerged as a powerful tool for data sharing, clinical trial simulation, and digital twin development, with growing applications in biomedical research and drug development. However, limited attention has been devoted to synthetic time-to-event data, which are central to clinical trials and survival analysis. In particular, theoretical guarantees for the distributional fidelity of synthetic survival data remain largely unexplored. More importantly, even when a generator achieves distributional fidelity, it remains unclear whether the downstream statistical analysis is reliable. To address these gaps, we propose a general two-stage generative framework for survival data (TSGSurv) that jointly generates observed times and covariates conditional on event status, and establish its distributional convergence rate. Focusing on the widely used Cox proportional hazards model, we establish conditions under which generator fidelity guarantees consistency of model coefficient estimates. We further characterize the limitations of naive inference based on synthetic data, and develop a variance correction and a distribution calibration procedure to recover valid inference of original data. We demonstrate the effectiveness of the proposed generative and inferential framework with extensive simulations and two real data applications.
- **Key innovations**:
  - TSGSurv: two-stage generative framework for censored survival data; distributional convergence rate established.
  - Generator-fidelity → coefficient consistency conditions for the Cox model.
  - Variance correction + distribution calibration to recover valid inference on original data.

### 27. Inverse ECG Reconstruction via a Preconditioned Variational Quantum Linear Solver
- **arXiv**: [2611.25450](https://arxiv.org/abs/2611.25450)
- **Date**: 2026-11-19
- **Authors**: Xizhuo Zhang, Chao Lu, Bing Yao
- **Institution/Company**: Department of Industrial & Systems Engineering, The University of Tennessee, Knoxville, TN, USA, 37996; National Center for Computational Sciences, Oak Ridge National Laboratory, Oak Ridge, TN, USA, 37830
- **Categories**: cs.LG
- **Abstract**: Inverse electrocardiography (ECG) reconstructs heart-surface potentials from body-surface measurements, enabling noninvasive mapping of cardiac electrical activity. However, the reconstruction requires solving dense and ill-conditioned linear systems, whose computational cost grows rapidly with the refined heart mesh. Quantum computing offers new opportunities for solving such systems. This paper presents a hybrid quantum-classical framework for inverse ECG reconstruction, which, to the best of our knowledge, is the first to apply a quantum linear solver to this problem. We first propose a Laplacian-regularized pre-encoding procedure to reduce the dimension of the system while improving its conditioning. Second, the resulting reduced system is encoded and solved using a coherent variational quantum linear solver (VQLS). Finally, we provide a rigorous theoretical proof establishing that the proposed framework preserves the exact solution of the original reconstruction problem throughout all stages of the computational process. Experimental results on a realistic heart-torso geometry demonstrate that our approach holds significant ability for accurate inverse ECG reconstruction. These findings highlight the potential of quantum solvers for noninvasive cardiac imaging, providing a foundation for further research into quantum-enhanced cardiac assessment and other healthcare applications.
- **Key innovations**:
  - Hybrid quantum-classical inverse ECG reconstruction: Laplacian-regularized pre-encoding (dimension reduction + conditioning) + coherent VQLS.
  - Rigorous proof of exact-solution preservation across the pipeline.

### 28. FamilySpace: From Emergent Chemical Semantics to Controllable Crystal Generation
- **arXiv**: [2611.25452](https://arxiv.org/abs/2611.25452)
- **Date**: 2026-11-19
- **Authors**: Haowei Hua, Irwin King, Wanyu Lin
- **Institution/Company**: Department of Computing, The Hong Kong Polytechnic University; Department of Computer Science and Engineering, The Chinese University of Hong Kong
- **Categories**: cs.LG, cond-mat.mtrl-sci (primary: cs.LG)
- **Abstract**: Latent crystal generative models typically combine a variational autoencoder (VAE) for learning atom-wise representations with a flow model that transports a simple source distribution to the learned latent distribution. However, previous studies have mainly focused on the quality of generated crystals, leaving the structure and generative utility of the atom-wise latent space largely unexplored. In this work, we show that even a vanilla crystal VAE implicitly organizes atom-wise latent representations according to elemental families, with different families occupying largely separated regions of the latent space. We term this phenomenon emergent chemical semantics. This structure suggests that sampling from a family-specific latent region can bias the decoder toward atoms from the corresponding elemental family. Building on this insight, we propose FamilySpace, a framework for controlling the elemental-family composition of generated crystals. FamilySpace assigns each elemental family a distinct source component, forming a family-indexed multi-source distribution, and trains a flow model using source-target pairs matched by family. In inference, a user-specified family template selects the source component for each atom-wise representation, enabling direct control over the family composition of generated crystals. Experiments on MP-20 and MPTS-52 show that FamilySpace achieves competitive crystal-generation performance while matching prescribed elemental-family compositions. Moreover, selected family templates increase the fraction of generated crystals predicted to be stable or metastable, demonstrating that latent-space composition control can support targeted exploration of promising chemical regions without additional optimization techniques such as reinforcement learning. Code is available at https://github.com/hhw11/FamilySpace
- **Key innovations**:
  - Discovery of "emergent chemical semantics" in vanilla crystal VAEs (elemental families occupy separated latent regions).
  - FamilySpace: family-indexed multi-source flow model; family template at inference controls elemental-family composition.
  - Competes on crystal generation while matching prescribed family compositions; boosts metastable fraction.

### 29. PAIR-MED: Policy-reward Alternation for Iterative Refinement in Multilingual Medical Reasoning
- **arXiv**: [2611.25446](https://arxiv.org/abs/2611.25446)
- **Date**: 2026-11-19
- **Authors**: Fan Gao, Xiaohang Xu, Lang Huang, Nan Lu, Irene Li
- **Institution/Company**: The University of Tokyo; National Institute of Informatics; University of Bristol Correspondence
- **Categories**: cs.CL
- **Abstract**: Large language models demonstrate strong medical question-answering capabilities, yet reasoning performance remains uneven across languages. Process reward models (PRMs) provide step-level feedback for improving reasoning, but a fixed PRM may become increasingly misaligned with the trajectory distribution of an evolving policy during reinforcement learning, thereby reducing the reliability of its supervision. We propose a policy--reward alternating training framework that jointly adapts a medical PRM and optimizes a multilingual reasoning policy. Following supervised initialization, the current policy generates multilingual trajectories to update the PRM, which then provides process-level rewards for the next policy update. Medical step supervision maintains the PRM's medical foundation, while process, outcome, and language-related rewards guide policy learning. We develop multilingual medical PRMs (PAIR-PRM) and reasoning models (PAIR-MED) at 8B and 9B scales across 12 languages. On the medical subsets of Global-MMLU and MMLU-ProX, our models improve average accuracy by 3.01--7.47% over their corresponding Qwen backbones. On CUREMED-BENCH, PAIR-MED-9B improves the joint language consistency and logical accuracy metric by 12.88% and 7.45% over baselines for in-domain and out-of-domain languages. Further analyses examine PRM adaptation, multilingual reasoning quality, and the contributions of individual training components.
- **Key innovations**:
  - Policy-reward alternation framework: PRM adapted to the evolving policy; PAIR-PRM + PAIR-MED (8B/9B, 12 languages).
  - Medical step supervision + process/outcome/language rewards; Global-MMLU/MMLU-ProX gains of 3.01–7.47%.

### 30. PILAPS: A Bilingual Benchmark for Evaluating Pragmatic Inference across Phenomena and Settings
- **arXiv**: [2611.25459](https://arxiv.org/abs/2611.25459)
- **Date**: 2026-11-19
- **Authors**: Jiani Cao, Anna Korhonen, Chen Cecilia Liu
- **Institution/Company**: Department of Theoretical and Applied Linguistics, University of Cambridge; Language Technology Lab, University of Cambridge
- **Categories**: cs.CL
- **Abstract**: Recent work reports strong pragmatic performance by large language models (LLMs) in English, yet whether this performance generalises across languages and evaluation settings remains unclear. This question is increasingly important as LLMs are deployed across languages, cultures, and conversational contexts. In this paper, we first introduce PILAPS, a bilingual English/Mandarin Chinese benchmark covering eight pragmatic phenomena across purpose-written and dialogue-derived items, with both culturally adapted and independently sourced data. We then evaluate eight LLMs from four families across a range of model sizes and prompting strategies. Our results reveal substantial variation across models and pragmatic phenomena: open-source models continue to struggle particularly with humour, while cross-linguistic performance varies with model origin. Our error analysis shows that, compared with human participants, models are more prone to literal interpretations in conversational contexts. Theory-of-Mind prompting lowers the literal share of errors, whereas Chain-of-Thought prompting slightly raises it. Together, these findings demonstrate that strong pragmatic performance in one evaluation setting does not necessarily generalise across languages or conversational contexts.
- **Key innovations**:
  - PILAPS: bilingual English/Mandarin benchmark of 8 pragmatic phenomena (purpose-written + dialogue-derived items).
  - Finding: open-source models struggle with humour; cross-linguistic performance varies with model origin.
  - Theory-of-Mind prompting lowers literal errors; CoT slightly raises them.
