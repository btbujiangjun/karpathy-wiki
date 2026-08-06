---
title: "arXiv Daily Digest — 2026-08-06"
type: synthesis
created: 2026-08-06
updated: 2026-08-06
tags: [arxiv, llm, agents, memory, skills, reasoning, rl, evaluation, safety, kv-cache, efficiency, recommendation, advertising, serving, infrastructure]
---

# arXiv Daily Digest — 2026-08-06

> Curated from the **Thu Aug 6, 2026** arXiv batch (new submissions announced on the Thu listing; submitted Aug 4–5, 2026). Stream sizes: cs.AI 41 new, cs.CL 72 new, cs.LG 96 new, cs.IR 8 new. **24 papers curated. No overlap** with the [Aug 5 digest](../2026-08-05/arxiv-daily.md), [Aug 5 AI scan](../2026-08-05/arxiv-ai-search.md), [Aug 4 digest](../2026-08-04/arxiv-daily.md), or [Aug 4 paper check](../2026-08-04/arxiv-paper-check.md). Two papers at this window's boundary (TurnSight 2608.04007, WorldCup Arena 2608.04008) were already carried by the Aug 5 digest and are excluded here. This edition's signature theme is **agent memory & skills as engineered, measurable components** — with strong secondary clusters on RL credit assignment, evaluation hygiene for safety/confidence claims, KV/efficiency redesigns, and industrial rec/ads serving.

---

## 1. Agent Memory Systems

### Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems (ScrubJay-MEM)
- **Authors**: Kartikey Singh Bhandari, Aarya Wadhwani, Dhruv Kumar, Pratik Narang
- **Institution**: BITS Pilani
- **Date**: 2026-08-05
- **Link**: [2608.04746](https://arxiv.org/abs/2608.04746)
- **Abstract**: LLM agents that persist across sessions accumulate memories whose validity decays at wildly different rates, yet existing memory architectures treat all memories as equally persistent and systematically contaminate retrieved context with outdated facts. ScrubJay-MEM operationalizes the type-conditioned temporal decay of western scrub jay episodic memory as an auto-classified coefficient πᵢ in an external memory store: each memory is encoded as a jointly-bound What–Where–When tuple with an estimated perishability and utility horizon, retrieved via query-adaptive scoring, and revised retroactively at O(1) LLM calls per update. Introduces the Temporal Generalization Test (TGT) with a held-out-retention Generalization Gap (GenGap) metric. On TGT, ScrubJay-MEM is the only retrieval-based system with substantially positive GenGap (+0.108); on MemoryAgentBench EventQA-64k it improves F1 by +2.66 over Mem0 and +3.09 over Qwen3-Embedding-4B. A decay ablation collapses GenGap 5.7×, establishing type-conditioned decay as necessary. Gains narrow under stronger backbones and reverse on fact-consolidation tasks — the contribution is scoped to temporal reasoning over perishable facts.
- **Key Innovation**: Per-memory, type-conditioned temporal decay as a first-class mechanism in external agent memory, plus a benchmark (TGT/GenGap) that actually tests generalization to held-out retention intervals.

### MemoryCPT: An End-to-End Agent Memory Framework for Cost-Performance Trade-off
- **Authors**: Songxin Lei, Kun Ouyang, Weilin Ruan, Yuqian Wu, Zhijiang Guo, Yushi Sun, Fugee Tsung
- **Institution**: Hong Kong University of Science and Technology (HKUST)
- **Date**: 2026-08-05
- **Link**: [2608.04843](https://arxiv.org/abs/2608.04843)
- **Abstract**: Long-horizon LLM agents need memory systems that recover useful evidence from large interaction histories without passing excessive context downstream, but existing pipelines rely on hand-crafted heuristics and repeated LLM calls. MemoryCPT is an end-to-end trainable agent memory pipeline spanning offline memory construction and online query-conditioned context generation: Query-agnostic Distillation (QAD) distills a modular memory-construction pipeline into a compact model using explicit reasoning traces, and Query-aware Retrieval and Summarization (QAR) combines reciprocal rank fusion (RRF) with a LoRA-based summarizer trained via GRPO under a cost-aware reward. Introduces Quality per Cost (QPC) to quantify answer quality per unit inference cost. Improves the cost-performance trade-off over baselines on LoCoMo and LongMemEval, with ablations characterizing each component.
- **Key Innovation**: Making the whole memory pipeline — construction, retrieval, and summarization — end-to-end trainable under a cost-aware reward, measured by a cost-normalized quality metric (QPC).

---

## 2. Agent Skills: Retrieval, Valuation & Native Training

### Skills Know Their Neighbors: Cluster-Contrastive Capability Pages for Skill Retrieval (Capability Pages)
- **Authors**: Zifei Wang, Wei Wen, Qiang Ji, Ruizhi Qiao
- **Institution**: Rensselaer Polytechnic Institute / Tencent
- **Date**: 2026-08-05
- **Link**: [2608.04482](https://arxiv.org/abs/2608.04482)
- **Abstract**: As skill libraries grow, candidates often share topic and vocabulary while implementing different capabilities; retrieval is limited not only by the scorer but by the document being scored. The authors formalize a skill's capability as its *executable region* and view its document as a lossy observation of that region — exposing a document-imposed component of retrieval error that improving the retriever alone cannot remove. *Capability Pages* are cluster-contrastive skill representations containing a positive trigger, a negative boundary, and a discriminative body, written by an offline compiler that compares neighboring skills; at inference the index uses the trigger/body for candidate recall while the router uses the negative boundary to reject confusable alternatives. On SRA-Bench (26,262 skills, 5,400 questions) Capability Pages improve Recall@10 for all five tested retrievers (mean +2.94 points); adding the negative boundary to candidate cards improves end-to-end task success +3.62 points across four executors. Transfers to Chinese SSL-SkillDiscovery (73.07% MRR@50).
- **Key Innovation**: Fixing skill retrieval by rewriting the offline skill library — making each document state which similar requests should be routed elsewhere — with no modification to the online models.

### What Is a Skill Worth? Structure-Aware Shapley Valuation of Agent Skills (SkillSV)
- **Authors**: Tao Li, Junfeng Liu, Qinghua Zhao, Yifan Li, Lei Wang, Bo Shao, Xuejun Liu, Linjun Shou
- **Date**: 2026-08-05
- **Link**: [2608.04562](https://arxiv.org/abs/2608.04562)
- **Abstract**: Skills are increasingly optimized by automated feedback loops, producing long structured artifacts whose internal value is unclear. SkillSV is a structure-aware Shapley-style valuation framework for assigning credit to internal units of a fixed skill (rules, examples, scripts, heuristics) under a fixed agent and held-out task distribution. It compiles a skill into units, dependencies, and hierarchy so that only valid counterfactual skills are evaluated, uses paired deletion and length-neutral padding to separate content value from context cost, and estimates values with a rollout-budgeted estimator for noisy agent evaluations. On four agentic benchmarks it recovers unit interactions, preserves aggregate skill lift, and guides safe pruning and compression.
- **Key Innovation**: Extends data-valuation (Shapley) to structured skill units with explicit dependency validity — decomposing a skill's value while separating content value from prompt-context cost.

### Toward Skill-Native LLMs: Skill Entropy for Benchmarking and Training Long-Horizon Reasoning (Skill²-Bench)
- **Authors**: Yinghui He, Ling Yang, Jiarui Liu, Yongjin Yang, Lechen Zhang, Yingcheng Wu, Zhenfei Yin, Mengdi Wang, Sanjeev Arora
- **Institution**: Princeton / Peking University
- **Date**: 2026-08-05
- **Link**: [2608.05139](https://arxiv.org/abs/2608.05139)
- **Abstract**: Long-horizon reasoning demands switching between distinct skills inside a single chain (e.g., math derivation, then using the result to plan a schedule). The authors introduce Skill Entropy, a measure of cross-skill switching difficulty, and Skill²-Bench, a benchmark of cross-skill long-horizon tasks built over 558 skills across 9 verifiable and open-ended domains, with per-task entropy scores and three difficulty levels. Evaluating 8 frontier and 4 open models reveals a skill-switching gap: accuracy decreases on higher-entropy tasks. Skill-Entropy RL turns entropy into a training signal — the model predicts both the answer and the skill used at each step, with a reward combining step-level correctness and alignment between predicted and gold skill sequences. On Qwen3-4B-Instruct and Qwen3-1.7B it lifts Skill²-Bench from 34.4%→68.4% and 14.6%→40.1%, beating competitive baselines, and transfers to off-the-shelf data such as OpenR1-Math.
- **Key Innovation**: Skill switching as a measurable and trainable quantity — a skill-sequence-alignment reward that is a reusable training signal beyond the benchmark itself.

> ℹ️ Pairs with the Aug 5 digest's Field-Aware Agent Skill Retrieval (field-wise skill representations) and ContinualSkillBench (adaptation vs consolidation): the skill layer of agents is becoming a full research program.

---

## 3. LLM Reasoning & RL Post-Training

### ABSeeker: Training Long-Horizon Search Agents via Answer-Backtracked Credit Assignment (ABC)
- **Authors**: Yijun Lu, Rui Ye, Jiajun Wang, Yuwen Du, Tian Jin, Songhua Liu, Siheng Chen
- **Institution**: Shanghai Jiao Tong University
- **Date**: 2026-08-05
- **Link**: [2608.05102](https://arxiv.org/abs/2608.05102)
- **Abstract**: Long-horizon search agents must make many sequential search/retrieve/verify/integrate steps, but existing SFT and RL treat all steps uniformly, failing to distinguish useful actions from erroneous or redundant ones. ABC converts sparse trajectory-level outcomes into dense step-level supervision: Answer-Backtracked Clue Recovery traces from the ground-truth answer to recover intermediate clues, and Clue-Anchored Step Scoring evaluates each search step against those clues — rewarding useful actions even in failed trajectories. This yields ABC-SFT (per-turn loss reweighting) and ABC-GRPO (step-level rewards). ABSeeker, trained on Qwen3.5-4B with only 8.5k examples, reaches 37.3% on BrowseComp and 39.1% on BrowseComp-ZH (55.3%/52.9% with context management), outperforming same-scale 4B agents and matching ~30B ones.
- **Key Innovation**: Dense, answer-anchored step-level credit for search agents — the reward target is intermediate clue recovery, not just final correctness.

### Agentic Reinforcement Learning with Observation-Calibrated Self-Distillation (OCSD)
- **Authors**: Yi Yang, Cong Qin, Xiaodan Liu, Chishui Chen, Qing Dong, Yan Zhang, Cao Liu, Zhao Yang, Lu Pan, Jiaye Lin, Yi Feng
- **Institution**: Meituan
- **Date**: 2026-08-05
- **Link**: [2608.04788](https://arxiv.org/abs/2608.04788)
- **Abstract**: On-Policy Self-Distillation (OPSD) rescoring tokens under a privileged replay view gives dense token-level supervision, but the resulting support confounds the privileged information with score shifts induced by the replay scaffold itself — especially when future environment observations are the privileged information, since replaying them requires reconstructing an extended scaffold. OCSD contrasts two structurally matched replay views (Full vs Observation-Ablated), differing only in whether the actual future observation is present, to derive an observation residual that discounts scaffold-shared score changes; the residual modulates token-level GRPO updates at high-uncertainty steps while preserving trajectory-level direction. On ALFWorld, WebShop, and Search-QA across three Qwen3 model scales, OCSD consistently outperforms strong baselines, and the calibrated residual aligns better with local environment feedback.
- **Key Innovation**: Paired-view differencing that isolates observation-derived credit from the replay-scaffold artifact in self-distilled RL — an experimental-design fix for a confounding in privileged-replay training.

### SpecRoll: Fast-Slow Verifier-Feedback Adaptation for Speculative Reinforcement Learning Rollouts
- **Authors**: Nhat Minh Pham, Duy Tung Doan, Thi Duyen Ngo, Vinh Van Nguyen, Khac-Hoai Nam Bui
- **Date**: 2026-08-05
- **Link**: [2608.04962](https://arxiv.org/abs/2608.04962)
- **Abstract**: RL post-training improves reasoning but is bottlenecked by autoregressive rollout generation; speculative decoding can help, but the target policy continually evolves — static proposers go stale while frequent drafter updates add overhead. SpecRoll is a speculative rollout engine that preserves the target model's sampling distribution while adapting at two timescales: lightweight future-token heads generate parallel proposals, a *Reflex* module uses delayed verifier feedback for bounded, trajectory-local hidden-state corrections (no backpropagation), and a slow path updates head parameters only on sustained degradation. Combined with concurrency-aware sparse-tree and exact target verification, the GRPO objective and rollout distribution are left unchanged. Across five models (1.5B–14B) and three math datasets: 1.26–2.15× generation and 1.21–2.04× end-to-end speedups over vanilla GRPO, beating FastGRPO in all 15 matched settings (average pairwise e2e +1.18×).
- **Key Innovation**: Speculative rollout with two-timescale adaptation (fast trajectory-local verifier-feedback corrections + slow head refresh) that accelerates RL rollouts without disturbing the target policy's distribution.

### Reasoning Core: Designing Broad Procedural Data for Completion-Supervised Reasoning Training
- **Authors**: Damien Sileo, Valentin Lacombe, Dimitri Kachler
- **Institution**: Inria Lille
- **Date**: 2026-08-05
- **Link**: [2608.05148](https://arxiv.org/abs/2608.05148)
- **Abstract**: Procedural generators produce useful verifiable reasoning problems at scale but have received less attention as completion-supervised fine-tuning data. Reasoning Core is a collection of 50 generators spanning mathematics, logic, planning, state tracking, formal languages, structured data, games, causality, and code, with semantic scorers, difficulty controls, and task evaluators. Under a matched completion-supervised protocol, it is compared against Procedural Warmup, Reasoning Gym, and SynLogic across four base models and multiple training durations; in the primary 3B comparison Reasoning Core achieves the highest mean scores on DROP, LogiQA, and ARC-Challenge. Task-level analysis shows semantic validity alone does not ensure training utility — compact targets and calibrated difficulty are the important design factors. Audits combining model-assisted review, human adjudication, and regression testing reveal subtle mismatches among generation, rendering, targets, and scoring, in this and the other collections.
- **Key Innovation**: An engineered procedural-data library with audit evidence that generation correctness ≠ training signal quality — with practical design guidance (compact targets, calibrated difficulty).

---

## 4. Evaluation, Safety & Trustworthiness

### Social Pressure Breaks Majority Voting in LLM Safety Panels
- **Authors**: Yibo Hu, Jiaming Qu
- **Date**: 2026-08-05
- **Link**: [2608.04415](https://arxiv.org/abs/2608.04415)
- **Abstract**: Combining judgments from a panel of LLMs is a common way to correct individual mistakes on unsafe-content detection, but the benefit disappears when every model sees the same misleading context before voting. In a controlled two-round experiment, each of six open-weight LLMs judges an item alone, then again after six simulated peers either assert the wrong label or abstain. The wrong-label peer message raises the average reviewer false-alarm rate from 56.5% (silent peers) to 87.5%, and majority voting raises the panel false-alarm rate to 100%; without an asserted label, the same panel outperforms its average member. The effect is strongly asymmetric — reviewers follow pushes toward "unsafe" ~75% of the time vs ~17% toward "safe" — so panel false alarms rise sharply while the harmful-miss rate changes little. Proprietary models vary substantially. The authors provide a simple pre-deployment diagnostic.
- **Key Innovation**: Identifies susceptibility to shared social cues as a failure mode of safety panels — panel diversity does not protect against correlated context; the harm is a one-way (unsafe-pushing) ratchet.

### Item Response Theory for AI Safety
- **Authors**: Joshua Fonseca Rivera, Neil Shah, David Demitri Africa, Konstantinos Voudouris
- **Date**: 2026-08-05
- **Link**: [2608.05086](https://arxiv.org/abs/2608.05086)
- **Abstract**: Aggregated safety-benchmark scores are hard to trust: benchmarks duplicate one another, correlate heavily, and models may sandbag when they detect evaluation. The authors fit IRT models to eight safety benchmarks across 192 models — the largest psychometric analysis of LLM safety evaluations. Three interpretable factors (refusal strictness, truthfulness, contextual harm) explain most of the variance between models; psychometrically selected items recover full benchmark scores with lower error than random subsets of the same size, and ~10 adaptively chosen items suffice for several benchmarks, cutting evaluation cost by 97–99%. IRT also supports individual-model audits, detecting naive sandbagging and model changes behind APIs.
- **Key Innovation**: A ready-made psychometric toolkit for reading, reducing, and auditing safety benchmarks — factor structure plus adaptive item selection plus per-model sandbagging diagnostics.

### Evaluation Pitfalls and Sparsity Limitations in LLM-based Confidence Estimates for Classification
- **Authors**: Elena Merdjanovska, Omar Zaidan, Andreas Rücklé
- **Institution**: University of Tübingen
- **Date**: 2026-08-05
- **Link**: [2608.04899](https://arxiv.org/abs/2608.04899)
- **Abstract**: Confidence estimation is essential when LLMs are used for classification, but verbalized confidence is extremely sparse — Qwen3-32B verbalizes only eight unique confidence values on SST-2, over half of which are exactly 95%, a pattern that holds across four datasets and two LLMs. Beyond limiting practical utility, this sparsity corrupts evaluation: the choice of interpolation in area under the accuracy-rejection curve (AUARC) dramatically alters rankings, with consistency sampling dropping from best to worst under stepwise vs linear interpolation. The authors advocate standardizing stepwise interpolation, under which weighting verbalized digits by token probabilities ("verbalization logprobs") addresses sparsity and achieves the best AUARC (+2.3 points over vanilla verbalization) at zero extra inference cost. Findings of ACL 2026.
- **Key Innovation**: Shows the confidence metric itself is confounded by output sparsity, and offers a free fix (logprob-weighted verbalized digits) plus a standardization recommendation (stepwise AUARC interpolation).

### Mind the Cap: Output-Budget Regimes Change the Measured Multilingual Reasoning Gap
- **Authors**: Ankit Goyal, Jaideep Ray
- **Institution**: Sandia National Laboratories
- **Date**: 2026-08-04
- **Link**: [2608.04160](https://arxiv.org/abs/2608.04160)
- **Abstract**: Multilingual evaluations report accuracy at a single output-token cap, but languages need different numbers of tokens to express the same content, making the cap a hidden experimental variable. For MGSM (German, Thai, Swahili) with Qwen3-8B and Llama-3.1-8B-Instruct under four prompting strategies, the measured native-vs-translate gap swings by up to 57 points across budgets, length normalization moves it by up to 38.9 points where the cap binds, and at tight caps normalization can reverse which strategy scores higher. A prospectively frozen sweep (three peaks plus a near-zero value at 1024) evaluated on 540,000 independently hard-capped decodes rejects every null except the saturated case. Announcing a different budget at a fixed enforced cap alone moves Thai native accuracy by 5.1 points, so accuracy is not a function of the enforced cap alone. Verdict: treat the output cap as an independent variable and report accuracy across the budget regime.
- **Key Innovation**: Demonstrates that the multilingual native-vs-translate "reasoning gap" is partly an output-token-budget artifact, using a prospective frozen-sweep design that isolates the cap as the causal variable.

### The Personalization Mirage: How LLMs Fabricate User Profiles, and Why Self-Monitoring Misleads (MirageBench)
- **Authors**: Yushi Sun, Yanjie Zhang, Rui Sheng
- **Date**: 2026-08-05
- **Link**: [2608.04570](https://arxiv.org/abs/2608.04570)
- **Abstract**: Personalized LLMs with persistent memory are increasingly deployed, yet the faithfulness of their user models is unexamined. MirageBench (150 personas balanced across stereotypical, counter-stereotypical, and neutral profiles; 6 tasks; a four-way faithfulness taxonomy validated by an independent judge; 12 models across 7 families; 143,616 judged claims) finds over-inference (OI) — fabricating user attributes beyond the evidence — is pervasive: every model over-infers 35–49% of its claims (cross-model mean 41.6%). Most strikingly, a Self-Monitoring Inversion: at the model-selection level, self-assessed OI is negatively rank-correlated with judge-measured OI (ρ = −0.60, p = 0.044), so the models reporting least over-inference fabricate the most; within a single model, self-audit still ranks its own claims moderately well (AUROC 0.58–0.83). OI is task-dependent (27–59%) and accumulates approximately linearly over turns with little revision.
- **Key Innovation**: Positions external verification, not model self-report, as the reliable foundation for trustworthy personalization — with a benchmark and a caution against using self-assessed confidence for model selection.

---

## 5. Efficiency: KV Cache, Attention & MoE Optimizers

### Spend Bits Where Queries Look: KV Cache Vector Quantization with Attention-Preserving Transforms (NOVA-KV)
- **Authors**: Samuel Fernández-Menduiña, Amir Ziashahabi, Eduardo Pavez, Antonio Ortega, Salman Avestimehr
- **Institution**: University of Southern California (USC)
- **Date**: 2026-08-04
- **Link**: [2608.04074](https://arxiv.org/abs/2608.04074)
- **Abstract**: Long-context decoding is bandwidth-bound: loading the KV cache takes longer than computing attention over it, so shrinking the cache raises decoding speed and serving capacity. The authors formulate KV quantization as a transform-coding problem whose distortion is the error in the attention products, and derive closed-form optimal key/value transforms from calibration statistics under a high-resolution model. The optimal key transform is non-orthogonal and satisfies a generalized Parseval relation, making the attention-aware distortion MSE in the transform domain — so MSE-optimal vector quantizers apply directly to transformed key coefficients. Grouping coefficients into equal-volume partitions makes fixed-width codebooks attain the variable-rate optimum. At 2 bits per element, NOVA-KV recovers most of the long-context retrieval accuracy lost by scalar quantization at comparable throughput.
- **Key Innovation**: Deriving KV transforms from the actual distortion criterion (attention error) rather than variance equalization — a principled departure from random/Hadamard-rotation quantizers.

### Training-Free Hashing-Based Attention via Binary Principal Components (BinaryPC)
- **Authors**: Daohai Yu, Zhanpeng Zeng, Keyu Chen, Wenhao Li, Zhifeng Shen, Luxi Lin, Ruizhi Qiao, Xing Sun, Rongrong Ji
- **Institution**: Xiamen University / Tencent
- **Date**: 2026-08-05
- **Link**: [2608.04405](https://arxiv.org/abs/2608.04405)
- **Abstract**: Self-attention remains a major efficiency bottleneck for long-context LLMs, especially during decoding, because the ever-growing KV cache must be repeatedly processed. Existing sparse attention either degrades accuracy, requires additional training, or relies on expensive hashing. BinaryPC is a training-free, data-aware hashing-based sparse attention that constructs compact binary hash codes and hash functions from the binary principal components of the data — explicitly preserving data structure without gradient-based training, unlike data-independent LSH or learned non-linear hashing. It preserves accuracy relative to full attention across model families and long-context benchmarks while outperforming sparse and hashing baselines; on modern GPUs it improves end-to-end decoding throughput 3.56× over FlashAttention. ICML 2026.
- **Key Innovation**: Data-aware hashing with zero training cost — binary PCs of the data as the attention hash function, sitting between data-independent LSH and learned hashing.

### MESH: Memory-Efficient Sinkhorn Optimization for Mixture-of-Experts Training
- **Authors**: Masato Fujitake
- **Date**: 2026-08-05
- **Link**: [2608.04407](https://arxiv.org/abs/2608.04407)
- **Abstract**: Memory-efficient matrix optimizers (Sinkhorn gradient descent) remove most AdamW optimizer state for dense Transformer matrices, but applying them to Mixture-of-Experts (MoE) training is unreliable: in a controlled 110M-parameter DeepSeek-style MoE pretraining setup, a SAGE/Sinkhorn hybrid cuts optimizer state from 0.883GB to 0.331GB but degrades evaluation loss to 3.8265 vs AdamW's 3.58–3.64. Routed expert matrices are the dominant failure point — their gradients are conditional, temporally varying, and poorly served by stateless Sinkhorn normalization. MESH restores a temporal first-moment signal through the gradient-buffer lifecycle without storing expert first-moment state, with an optional block-preconditioned variant adding a coarse neuron/block inverse-RMS multiplier. Temporal smoothing before normalization is the primary causal ingredient. Across ablations MESH/MESH-B cut optimizer-state memory 62.5% and peak PyTorch CUDA allocation ~12.6% vs AdamW with a modest evaluation-loss gap; full-state diagnostic variants recover AdamW-like performance, showing MoE experts need temporal smoothing but not necessarily full coordinate-wise AdamW state.
- **Key Innovation**: Diagnoses why stateless optimizers fail on MoE experts (conditional, time-varying routed gradients) and fixes it with hidden momentum — temporal smoothing without per-expert optimizer state.

---

## 6. Recommendation, Advertising & Live-Streaming Serving

### DEGR: Dual Exploration-Driven Generative Re-Ranking for Adaptive Cross-Request Context Bridging
- **Authors**: Binglei Zhao, Xuanhua Yang, Xiwei Zhao, Sulong Xu
- **Institution**: JD.com
- **Date**: 2026-08-05
- **Link**: [2608.04809](https://arxiv.org/abs/2608.04809)
- **Abstract**: In industrial recommendation, the re-ranking stage balances business objectives and diversity for sequence-level optimization, but fixed upstream supply caps further gains — especially under low-quality supply. DEGR lets re-ranking actively balance immediate and exploratory value, e.g. prioritizing exploratory exposure under low-quality supply to preserve browsing potential and enable serendipitous conversions. It uses a hybrid supervised-reinforcement exploration and optimization paradigm guided by an exploratory reward model: supervised learning + an exploration diversity constraint + adaptive reward-weighted ORPO for preference optimization, making the generator an adaptive cross-request contextual bridge. Offline and online experiments show up to +1.22% UCTR and +0.20% PV in JD's e-commerce recommendation system. KDD 2026 ADS Track.
- **Key Innovation**: Exploration value made an explicit objective of generative re-ranking — dual (supervised + reinforcement) exploration with production gains at JD.

### Generative Optimization for Incentivized Advertising with Global Level Constraints (GOAL)
- **Authors**: Gege Chen, Ning Luo, Hao Jiang, Da Li, Wenzheng Shu, Teng Sha, Yanxiang Zeng, Wenxin Tai, Fan Zhou, Xialong Liu
- **Date**: 2026-08-05
- **Link**: [2608.04421](https://arxiv.org/abs/2608.04421)
- **Abstract**: Incentivized advertising allocates monetary or virtual rewards to drive user engagement; the key challenge is optimizing continuous incentive magnitudes under strict global constraints, complicated by high-frequency interaction, delayed feedback, and non-Markovian user dynamics such as fatigue — which limit uplift modeling and constrained RL. GOAL is a constraint-aware generative framework that formulates incentive allocation as conditional sequence generation: generate incentive magnitudes conditioned on user histories and system-level global pressure, with a hierarchical causal state encoder capturing local behavioral dynamics and long-range dependencies. Safe Constrained Policy Optimization (SCPO) learns a single generative policy that generalizes across a spectrum of ROI constraints without retraining. On large-scale real-world data and a synthetic fatigue-aware environment, GOAL improves long-term revenue and user retention while substantially reducing ROI violation rates vs strong baselines.
- **Key Innovation**: Sequence-generative incentive allocation with a constraint-generalizing policy (SCPO) — one policy covering the ROI-constraint spectrum without retraining per constraint.

### Multi-Objective Ranking for Live-Streaming: Balancing Fresh and Delayed Signals with Segment-Aware Targeting
- **Authors**: Xiaoyi Gu, Julia Tavares, Eder Santana, Carlos Mendoza-Cardenas, Nikita Mishra, Saad Ali
- **Institution**: Amazon
- **Date**: 2026-08-05
- **Link**: [2608.04455](https://arxiv.org/abs/2608.04455)
- **Abstract**: Live-streaming recommendation is hard because user behaviors are sparse and delayed, and interaction data is biased across user segments; viewers engage in concurrent watching/chatting/following/spending with varying delays, unlike linear e-commerce sequences. Contributions: ① a delayed-window approach that extends feedback collection beyond immediate response; ② a multi-model architecture combining fresh and delayed signals with a segment-aware targeting module that optimizes ranking scores per user lifecycle stage; ③ Multi-gate Mixture-of-Experts (MMoE) jointly modeling correlated targets while cutting parameters 41.9% vs independent models. Online A/B: +0.09% Daily Active Viewers (millions more annual active viewer days), +0.56% capped ARPU among highly engaged viewers, segment targeting +0.15% DAV for newer/less-engaged viewers, MMoE +0.08% DAV / +0.27% new follows. Transfer on the Twitch mobile live feed: +1.12% positive user-channel interactions. RecSys 2026 Industry Track.
- **Key Innovation**: A production-tested recipe for multi-objective live-stream ranking that handles delayed feedback windows and lifecycle-segment heterogeneity — with a clean decomposition of gains by component.

### The Price of Isolation: Estimating the Ecosystem Cost of Symmetric Two-Sided A/B Testing
- **Authors**: Yuanyuan Shen, Yiren Yan, Wenjie Li, Chunhui Zhu
- **Date**: 2026-08-05
- **Link**: [2608.04432](https://arxiv.org/abs/2608.04432)
- **Abstract**: Symmetric two-sided isolation — assigning matched fractions of creators and viewers to isolated treatment/control submarkets — is widely used for creator-side and cold-start experiments because it removes cross-arm marketplace interference, but it thins each viewer's candidate catalog. Intuition suggests the engagement cost should fade as the platform grows. In an order-statistics model of engagement, whether it fades depends on the upper tail of match quality: extreme-value theory yields a sharp dichotomy — light/bounded tails make the loss vanish as the pool grows, while heavy tails make it converge to a size-independent constant (expanding the pool by orders of magnitude does not asymptotically eliminate it). Two production experiments on a platform with millions of active creators are consistent: a pure A/A traffic sweep shows a measurable depth-graded cost, a one-sided catalog ablation shows per-viewer thinning contributes, and a tail index calibrated on the small exploration pool predicts the far-larger full-catalog ablation. The authors give practitioners a preflight procedure estimating the cost before launch.
- **Key Innovation**: A tail-class law for the ecosystem cost of two-sided A/B isolation — heavy-tailed match quality means the cost does not scale away — plus a preflight estimator.

---

## 7. Agent Infrastructure & Population-Scale Simulation

### MatrAIx: Simulating the World with 8.3 Billion Persona Agents
- **Authors**: Xiaomin Li, Yuexing Hao, Jianheng Hou, et al. (large multi-institution author list)
- **Institution**: Stanford / MIT / CMU / Oxford (multi-institution)
- **Date**: 2026-08-04
- **Link**: [2608.04205](https://arxiv.org/abs/2608.04205)
- **Abstract**: Human evaluation of AI systems and digital products is costly, slow, and hard to scale, while offline evaluations abstract away human diversity and interactivity. MatrAIx is a population-scale simulated-user evaluation infrastructure: Persona 8B contains 8.3 billion persona records over 1,290 categorical dimensions (sampled from a dependency graph preserving correlated attributes or derived from human-authored profiles; a quality-filtered ~1M coreset of 599,847 human-grounded + 400,000 synthetic records); the Playground provides Survey, AI Chatbot, Web, and App environments; and 1,010 application tasks span 25+ domains. 18,189 evaluation trials across eight tasks with persona agents powered by Claude Opus 4.8, GPT 5.5, and Claude Haiku 4.5 capture how decisions vary by persona background (hesitation after a price increase, continuation after an AI assistant failure, latency tolerance). Validation: 91.5% persona adherence in a 400-trial controlled study; human + LLM judges evaluated human-grounded persona extraction quality.
- **Key Innovation**: Population-scale (8.3B-persona) simulated-user evaluation infrastructure with behavioral-grounded persona adherence — evaluation as infrastructure rather than a single benchmark.

### Architectural Implications of Agentic AI Workflows
- **Authors**: Jirong Yang, Peizhe Liu, Chaojie Zhang, Jovan Stojkovic
- **Institution**: Microsoft
- **Date**: 2026-08-05
- **Link**: [2608.04458](https://arxiv.org/abs/2608.04458)
- **Abstract**: Agentic AI is emerging in datacenters, but its architectural implications are unexplored. This is the first architectural characterization of agentic workflows, combining a production study at Microsoft Azure with a controlled study of open-source frameworks. Agentic execution is fragmented and heterogeneous: requests expand into workflows of LLM inferences, tool invocations, and orchestration decisions that repeatedly cross the CPU-GPU boundary. The CPU sits on the critical path; load stays low with sudden spikes; model composition sets how evenly the workflow uses GPUs, and task/tool diversity widens the range. These characteristics mismatch conventional uniform servers — fragmented execution strands CPU and GPU capacity despite bursty demand, homogeneous CPU provisioning is inefficient, and multiplexing many agents degrades microarchitectural locality. Agora, a commodity-server prototype, dynamically harvests idle CPU cores for co-located throughput work while protecting agent tail latency, oversubscribes GPU memory with state prefetching, pools cores by role with affinity-aware scheduling, and auto-tunes — improving utilization and server throughput.
- **Key Innovation**: A measurement-driven taxonomy of agentic workload resource demand and a concrete server-design response (Agora) — the systems layer forming under multi-agent deployment.

### A/B Agent: A Self-Evolving Agent for Strategy Iteration in Industrial A/B Testing
- **Authors**: Zhuohang Jiang, Yuxin Chen, Yongsen Pan, Zheng Hu, Wenqi Fan, Qing Li, Hongyang Wang, Jun Wang, Wenwu Ou
- **Date**: 2026-08-05
- **Link**: [2608.04625](https://arxiv.org/abs/2608.04625)
- **Abstract**: Industrial recommendation strategy iteration relies heavily on large-scale A/B experimentation, but manual tuning is labor-intensive and historical knowledge fragments. Existing RAG agents partially help but organize experience flatly, overlooking the hierarchy of business scenarios, recommendation stages, optimization objectives, and experimental contexts. A/B Agent is a closed-loop agent with three coupled components: Historical Strategy Knowledge Organization (a hierarchical experience tree), Autonomous Target-Aware Strategy Generation (multi-path Tree-RAG retrieval → executable strategies), and Experiment-Guided Strategy Self-Evolution (analyze online A/B feedback, tune parameters, update the tree). Offline and online evaluations show +4.829% GMV in a real-world short-video e-commerce recommendation system with positive gains across all guardrail metrics.
- **Key Innovation**: Closing the A/B iteration loop — hierarchical experience tree + Tree-RAG generation + feedback-driven self-evolution — an agentic replacement for manual experiment iteration at production scale.

---

## Cross-Cutting Trends

| Trend | Description | Representative Papers |
|-------|-------------|----------------------|
| **Agent memory becomes engineered, not appended** | Memory moves from retrieval plumbing to a designed component with decay curves (ScrubJay-MEM, biologically inspired), end-to-end training under cost-aware rewards (MemoryCPT, QPC metric), and faithfulness audits (MirageBench over-inference) | ScrubJay-MEM, MemoryCPT, MirageBench |
| **The agent skill layer matures into a full lifecycle** | Retrieval rewritten offline so documents state their executable regions (Capability Pages); Shapley valuation of internal skill units (SkillSV); cross-skill switching as a trainable signal (Skill²-Bench); engineered procedural data (Reasoning Core) — building on Aug 5's Field-Aware Skill Retrieval | Capability Pages, SkillSV, Skill²-Bench, Reasoning Core |
| **RL credit assignment gets finer and cheaper** | Answer-anchored step rewards (ABSeeker), observation-calibrated self-distillation (OCSD), speculative rollouts preserving the target distribution (SpecRoll) | ABSeeker, OCSD, SpecRoll |
| **Evaluation defends itself against confounded metrics** | IRT factor structure + 97–99% eval-cost cut for safety benchmarks; output-cap as an independent variable (Mind the Cap); AUARC interpolation standardization; shared-context defeating safety panels | IRT for AI Safety, Mind the Cap, Confidence Sparsity, Social Pressure Panels |
| **Serving efficiency targets fundamentals** | Attention-aware KV transform coding (NOVA-KV), training-free data-aware hashing attention (BinaryPC), hidden-momentum MoE optimizers (MESH) | NOVA-KV, BinaryPC, MESH |
| **Industrial rec/ads adds new control surfaces** | Exploration value in generative reranking (DEGR, JD), constraint-generalizing generative incentives (GOAL/SCPO), delayed-signal live-stream multi-objective ranking (Amazon), ecosystem cost of two-sided A/B isolation | DEGR, GOAL, Live-Stream Ranking, Price of Isolation |
| **Agent-scale infrastructure and simulation arrive** | 8.3B-persona simulated-user evaluation (MatrAIx), agentic-workload-aware server design (Azure/Agora), closed-loop A/B experimentation agent | MatrAIx, Agentic AI Workflows, A/B Agent |

---

## Key Takeaways

1. **Agent memory is the day's signature theme — engineered, costed, and audited.** ScrubJay-MEM adds type-conditioned perishability to memories (with a proper generalization benchmark, TGT/GenGap), MemoryCPT makes construction+retrieval+summarization end-to-end trainable under a cost-aware reward, and MirageBench warns that persistent-memory user models over-infer on 41.6% of claims with self-report that inverts model ranking. Memory now has decay curves, cost budgets, and faithfulness taxonomies.
2. **The agent "skill" is becoming a measurable asset class.** Capability Pages, SkillSV, Skill²-Bench, and Reasoning Core attack skills from four angles (retrieval, valuation, training signal, data). Combined with Aug 5's Field-Aware Skill Retrieval and ContinualSkillBench, the skill layer is the most coherent research program of the week.
3. **RL post-training is refining credit granularity and rollout cost at the same time.** ABSeeker (answer-anchored step rewards), OCSD (observation-calibrated self-distillation), and SpecRoll (speculative rollouts that leave the target distribution intact) target the two soft spots of reasoning RL: sparse reward and rollout expense.
4. **Evaluation hygiene is a strong secondary wave.** IRT reads/reduces/audits safety benchmarks; Mind the Cap shows the multilingual reasoning gap is partly a token-budget artifact; the AUARC paper shows metric choice flips rankings; the safety-panel paper shows shared context defeats majority voting. The theme: "is the metric measuring what we think it measures" remains a live research area.
5. **Serving efficiency pushes toward attention- and optimizer-level redesigns.** NOVA-KV derives KV quantizers from the actual distortion (attention error); BinaryPC gets data-aware hashing without training; MESH restores temporal momentum to MoE expert updates without optimizer state. Three complementary attacks on the memory/bandwidth wall.
6. **Industrial rec/ads keeps producing production-scale, causal results.** DEGR adds exploration value to reranking at JD (+1.22% UCTR), GOAL generates incentives under global ROI constraints with a single constraint-generalizing policy, Amazon's live-stream ranking handles delayed signals and segments (+0.09% DAV), and the two-sided A/B isolation paper gives a preflight estimator for an overlooked ecosystem cost.
7. **The systems layer around agents is forming.** MatrAIx (8.3B personas), Microsoft's Azure agentic-workflow characterization (Agora), and A/B Agent represent evaluation, capacity planning, and experimentation as first-class engineering problems for multi-agent deployment.

> ⚠️ Note on sourcing: All papers verified against the arXiv **Thu Aug 6, 2026** announcement listing (new submissions in ID range ~2608.04012–2608.05148; submitted Aug 4–5, 2026; stream sizes cs.AI 41 / cs.CL 72 / cs.LG 96 / cs.IR 8 new). The arXiv API was rate-limited (HTTP 429) during curation, so metadata was verified via arXiv listing and abs pages. TurnSight (2608.04007) and WorldCup Arena (2608.04008), at this window's boundary, were already covered in the [Aug 5 digest](../2026-08-05/arxiv-daily.md) and are excluded. Later scans (arxiv-ai-search, arxiv-paper-check) may overlap with residual listings.
