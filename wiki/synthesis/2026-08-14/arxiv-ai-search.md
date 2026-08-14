---
title: arXiv AI Research Search — August 14, 2026
type: synthesis
created: 2026-08-14
updated: 2026-08-14
sources: [arxiv-listing, arxiv-abstract-pages]
tags: [arxiv, ai, llm, ads, ctr, cvr, conversion, recommendation, generative-recommendation, sid, session-recommendation, on-policy-distillation, rlvr, alignment, jailbreak, kv-cache, quantization, rope, normalization, verified-code, lean, reasoning, search-efficiency, games, mechanism-design, llm-pricing, llm-routing, multi-agent, nash-equilibrium, time-series, scaling-laws, grokking, daily-digest]
---

# arXiv AI Research Search — 2026-08-14

> Search window: **Fri, Aug 14, 2026** arXiv announcement batch (submissions Aug 12–13, IDs ~2608.125xx–2608.135xx; window continues past the 08-13 digests which covered up to 2608.12307). Streams scanned: cs.LG (157 new), cs.CL (101 new), cs.AI (204 new), cs.IR (19 new), cs.GT (6 new), cs.MA (14 new), cs.SE (18 new). Discovery and all selected-paper metadata were verified via web pages (`arxiv.org/list`, `arxiv.org/abs`).
>
> 20 papers curated, **all NEW** (grep-verified 0 hits on arXiv ID across wiki/index.md, wiki/log.md, and wiki/synthesis/**). First synthesis output of the 2026-08-14 day. Same-day arxiv-daily / arxiv-paper-check had not yet been generated at time of writing, so the strongest industrial cs.IR/cs.AI/cs.GT picks (STAR, DrEM, FSGR, DrIG, EA-RAM, TsuGO, vToken) are included here. Note: 2608.12547 (Do LLMs Beat Nash?) is dated "Submitted on 12 Aug 2026" but appears in the Fri Aug 14 cs.MA listing; it is new to the wiki (0 hits).

## Overview table

| # | Paper | Domain | Institution / Company | arXiv | Status |
|---|-------|--------|----------------------|-------|--------|
| 1 | STAR: Structured Tokenization and Target-Aware Interest Representation for PCVR Prediction | Ads / CTR / CVR | KDD Cup 2026 Tencent UniRec Challenge (not stated) | 2608.12986 | **new** |
| 2 | Doubly Robust Estimation of Causal Effect on CVR with Targeted Regularization | Ads / CVR / causal inference | (not stated) | 2608.13461 | **new** |
| 3 | FSGR: Mitigating Token Frequency Bias for Fair SID-Based Generative Recommendation | Generative recommendation / fairness | Nankai University (tentative) | 2608.12845 | **new** |
| 4 | DrEM: Dual-Side Robust Ensemble Ranking from Noisy User Preference Predictions in Video Recommendation | Recommendation / ensemble ranking | Shenzhen University (tentative) | 2608.12778 | **new** |
| 5 | DTAMLP: Denoise Time-aware MLP for Session-based Recommendation | Session-based recommendation | (not stated) | 2608.12975 | **new** |
| 6 | Generative Universal Multimodal Retrieval with Dual-role Identifiers (DrIG) | Generative retrieval / multimodal | (not stated; under review) | 2608.12987 | **new** |
| 7 | CROP: Task Relevance via Counterfactuals for Selective On-Policy Distillation | LLM post-training / OPD | (not stated) | 2608.13387 | **new** |
| 8 | Latent On-Policy Self-Distillation (LOPD) | LLM post-training / OPSD | National University of Singapore (Shuicheng Yan, tentative) | 2608.13040 | **new** |
| 9 | CrEST: Verifier-Bounded Credit Assignment for Multi-Turn Multi-step LLM Agents | Agents / RLVR credit assignment | Ant Group / Tsinghua (tentative) | 2608.13179 | **new** |
| 10 | Synthetic Persona Pretraining: Alignment from Token Zero (SPP) | Alignment / pretraining | EPFL / University of Toronto (high confidence) | 2608.13482 | **new** |
| 11 | vToken: Token-Level Virtualization for Reclaimable KV Caches | LLM serving / KV cache | Tsinghua University (high confidence) | 2608.13263 | **new** |
| 12 | When Local Variance Optimality Is Not Enough: RoPE-Aligned Q/K Rotations for Dynamic 4-Bit Quantisation | LLM efficiency / quantization | (not stated) | 2608.13365 | **new** |
| 13 | Rethinking Normalization Placement for LLMs: Post-Norm under Curriculum Depth Growing | LLM architecture / training | (not stated) | 2608.13156 | **new** |
| 14 | Vero: Can AI Agents Build Formally Verified Software Repositories? | Verified code generation / agents | UC Berkeley (stated via github) | 2608.13522 | **new** |
| 15 | TsuGO: Probing Search Efficiency in LLM Reasoning via Go Life-and-Death Problems | Reasoning / search efficiency | (not stated) | 2608.13221 | **new** |
| 16 | Keep, Customize, or Exit: Default Design and Token Pricing in LLM Reasoning Services | Mechanism design / LLM pricing | UIUC (Melih Bastopcu, tentative) | 2608.13315 | **new** |
| 17 | Error-Aware Reverse Auction Mechanism for LLM Routing (EA-RAM) | Mechanism design / LLM routing | SUSTech (tentative) | 2608.12719 | **new** |
| 18 | Do LLMs Beat Nash? Testing Decentralized Coordination in Self-Play Multi-Agent Games | Multi-agent games / game theory | McGill University (Gregory Dudek, high confidence) | 2608.12547 | **new** |
| 19 | Into the ORBIT for Time Series: Training Regimes for Foundation Models | Time series / foundation models | (not stated) | 2608.13262 | **new** |
| 20 | Neural Quadratic Forms: A Unified Minimal Model for Sudden Learning and Scaling Laws | Scaling laws / grokking theory | MIT (high confidence) | 2608.13335 | **new** |

---

## 1. Ads, CTR & Conversion

### 1.1 STAR: Structured Tokenization and Target-Aware Interest Representation for PCVR Prediction

- **arXiv**: [2608.12986](https://arxiv.org/abs/2608.12986) (cs.IR; submitted 2026-08-13) — **NEW**
- **Authors**: Yimeng Xu, Haorui Zhang, Yingqi Song, Ying Jiang, Lan Ma
- **Institution**: Not stated; entry targets the **KDD Cup 2026 Tencent UniRec Challenge**.
- **Abstract (faithful summary)**: Post-click conversion rate (PCVR) prediction is a core ranking task in industrial recommender systems. Modern ranking models must jointly capture heterogeneous non-sequential features, multi-behavior user sequences, and target-item-aware user interests, while remaining robust to high-cardinality sparse features, missing values, and train-inference inconsistencies. **STAR** (Structured Tokenization and Target-Aware Interest Representation) is a practical framework for the KDD Cup 2026 Tencent UniRec Challenge. It combines structured feature tokenization with target-aware interest representation on top of a **HyFormer-style multi-sequence backbone**, and introduces high-cardinality signal recovery, explicit user-item interaction tokens, target-aware sequence decoding, and a weighted user-item contrastive auxiliary objective inspired by InfoNCE. Training and inference pipelines are aligned by reconstructing feature remapping tables and structural hyperparameters from the saved training configuration. Experiments on the challenge dataset identify the components that most reliably improve ranking AUC (LogLoss reported as a calibration diagnostic). The main ablation shows a **large gain from temporal context**, with smaller but useful contributions from contrastive alignment, target-aware interest encoding, and high-cardinality sequence feature recovery.
- **Key innovations**: (1) Structured tokenization + target-aware interest encoding on a HyFormer-style multi-sequence backbone for a challenge-scale PCVR task; (2) InfoNCE-inspired weighted user-item contrastive auxiliary; (3) explicit train/inference consistency via saved-config remapping reconstruction; (4) an ablation that isolates temporal context as the dominant AUC driver.

### 1.2 Doubly Robust Estimation of Causal Effect on CVR with Targeted Regularization

- **arXiv**: [2608.13461](https://arxiv.org/abs/2608.13461) (cs.LG; submitted 2026-08-13) — **NEW**
- **Authors**: Jiayi Dan, Bo Li, Lu Deng, Yong Wang
- **Institution**: Not stated.
- **Abstract (faithful summary)**: CVR is a key metric in e-commerce and advertising, reflecting efficiency and user experience in the second stage of conversion. Estimating the **causal effect on CVR** matters practically, but applying standard causal inference only to clicked samples introduces sample selection bias and increased variance from excluding non-click data. Recent "ideal loss" CVR work optimizes parameters with an unbiased loss estimate over the full sample — yet unbiasedness of the loss does **not** guarantee unbiasedness of the final estimator. The authors revisit the problem from semiparametric theory and develop a **doubly robust causal effect estimator for chain-structured outcomes** (such as CVR), deriving its theoretical properties in detail. It converges faster than nuisance parameter estimation and is therefore more robust with flexible nonparametric estimators, including neural networks. A **targeted regularization** framework improves numerical stability and practical applicability. Experiments on synthetic and real data confirm effectiveness/robustness, and show that **naively combining loss debiasing with standard causal estimators underperforms** their tailored estimator.
- **Key innovations**: (1) A doubly robust, chain-structured (CVR) causal estimator with an explicit convergence-rate advantage over nuisance estimation; (2) targeted regularization for numerical stability; (3) a negative result on the naive "ideal loss + off-the-shelf causal estimator" recipe.

---

## 2. Recommendation

### 2.1 FSGR: Mitigating Token Frequency Bias for Fair SID-Based Generative Recommendation

- **arXiv**: [2608.12845](https://arxiv.org/abs/2608.12845) (cs.IR / cs.AI / cs.LG; submitted 2026-08-13) — **NEW**
- **Authors**: Yuchen Zheng, Sihan Xu, Jingwen Yang, Xiangrui Cai, Haiwei Zhang, Xiaojie Yuan
- **Institution**: Not stated; Xiangrui Cai / Xiaojie Yuan are affiliated with Nankai University (tentative).
- **Abstract (faithful summary)**: Semantic ID (SID)-based generative recommendation has succeeded recently, but suffers an overlooked fairness issue the authors call **Token Frequency Bias**: high-frequency SID tokens are systematically over-predicted and low-frequency ones under-predicted. The bias originates from imbalanced semantic codebooks during SID construction plus popularity bias interacting with the MLE objective during training, producing **unfair exposure across item categories**. Existing SID methods focus on codebook quality and miss the downstream fairness impact of token frequency imbalance; LLM debiasing methods transfer poorly because of the hierarchical semantics of SID tokens. **FSGR** is a fairness optimization framework: during SID construction it applies **OT-based Assignment Optimization** and a **Dual-Criteria Re-anchor** mechanism to form a more balanced SID representation space; during recommendation training it uses a two-stage strategy plus **Hierarchical Frequency Calibration** for layer-specific fairness fine-tuning. On three public datasets with three backbone models, FSGR mitigates token frequency bias with an average **Gini fairness improvement of over 20%** while keeping competitive accuracy.
- **Key innovations**: (1) Names and localizes a distinct failure mode (token frequency bias) in SID-based generative recommendation; (2) fairness interventions at both the codebook-construction and the training stages; (3) hierarchical, layer-specific frequency calibration; (4) >20% Gini improvement at stable accuracy.

### 2.2 DrEM: Dual-Side Robust Ensemble Ranking from Noisy User Preference Predictions in Video Recommendation

- **arXiv**: [2608.12778](https://arxiv.org/abs/2608.12778) (cs.IR; submitted 2026-08-13) — **NEW**
- **Authors**: Canwei Huang, Tiantian He, Xiaoxiao Xu, Jun Zhang, Ziran Deng, Weike Pan, Chunjie Chen, Kaiqiao Zhan
- **Institution**: Not stated; Weike Pan is affiliated with Shenzhen University (tentative).
- **Abstract (faithful summary)**: Industrial video recommendation uses a multi-stage architecture; at the **ensemble ranking** stage, multi-dimensional user preference predictions (**pxtrs**) from an upstream multi-task model are fused into a unified ranking score. Since true satisfaction is hard to observe, pxtrs are used both as input features and to construct proxy preferences. But pxtrs carry prediction noise that propagates on **two sides**: on the supervision side, noisy pxtrs may flip proxy preferences and inject erroneous gradients; on the feature side, pxtr noise destabilizes ranking scores. Existing methods treat pxtrs as reliable. **DrEM** is a dual-side robust ensemble ranking framework: a **risk-denoising robust loss** corrects the empirical risk using an estimated preference-flip probability, while sampling perturbations from the prediction-noise distribution and a **preference-preserving ranking consistency regularizer** stabilize feature-side output. Theoretically, they obtain an approximate noise distribution and prove the robust loss stays superior under flip-probability estimation error. Extensive offline experiments and **large-scale online A/B tests** demonstrate effectiveness and robustness.
- **Key innovations**: (1) Explicit two-sided (supervision + feature) model of pxtr noise in ensemble ranking; (2) flip-probability-corrected robust loss with a robustness-under-misestimation proof; (3) perturbation-sampling consistency regularizer for output stability; (4) online A/B validation.

### 2.3 DTAMLP: Denoise Time-aware MLP for Session-based Recommendation

- **arXiv**: [2608.12975](https://arxiv.org/abs/2608.12975) (cs.SI / cs.IR; submitted 2026-08-13) — **NEW**
- **Authors**: Jiamu Zheng, Xiaojun Shan
- **Institution**: Not stated.
- **Abstract (faithful summary)**: Two empirical findings on session-based recommendation (SBR), unified in **DTAMLP**. First, time-aware and GNN-based models (e.g., TiSASRec, SR-GNN) treat every click-time interval as equally informative, even though very short dwell times often reflect accidental clicks carrying little preference signal — **sporadic noise**. A lightweight, plug-and-play **weight fusion module** blends a model's attention weight with a threshold-capped time-interval weight, inserting into such models with almost no architectural change for a consistent accuracy gain (presented as the most directly verifiable contribution). Second, the paper revisits the under-explained FMLP-Rec observation that a learnable frequency-domain filter on item embeddings helps accuracy, offering an **interpretive conjecture**: time-domain behavior mixes several entangled psychological preferences, and a frequency-domain view may separate and down-weight such preference noise. DTAMLP, an all-MLP framework combining weight fusion and FFT-based filtering, is validated on Diginetica and RetailRocket. The authors are explicit that the system-level design reflects the field circa 2023 rather than a SOTA claim; ablations confirm the two mechanisms contribute complementary, non-redundant improvements.
- **Key innovations**: (1) A cheap, insertion-friendly time-interval weight fusion that denoises sporadic clicks in existing SBR models; (2) a frequency-domain interpretation of FMLP-Rec's filter gains; (3) honest reporting — mechanism ablations vs. SOTA claims separated.

### 2.4 DrIG: Generative Universal Multimodal Retrieval with Dual-role Identifiers

- **arXiv**: [2608.12987](https://arxiv.org/abs/2608.12987) (cs.IR / cs.AI; submitted 2026-08-13; under review) — **NEW**
- **Authors**: Kaipeng Li, Haitao Yu, Xuanchen Zhou
- **Institution**: Not stated.
- **Abstract (faithful summary)**: Generative information retrieval (GIR) trains a generator to emit identifiers of relevant items directly, but faces three open problems: (1) constrained left-to-right decoding is vulnerable to prefix-level errors and local optima; (2) most GIR research is unimodal, leaving instruction-aware retrieval across text, image, and mixed image-text items underexplored; (3) discrete-identifier GIR lags dense-vector retrieval in accuracy. **DrIG** is a generative framework for universal multimodal retrieval with **dual-role identifiers**: each candidate gets a single residual-quantized identifier serving two complementary roles — a *sequential* role (decoded autoregressively, first token explicitly models modality, remaining tokens capture progressively finer semantics) and a *set-based* role (the same tokens reinterpreted as an unordered set providing a **prefix-independent relevance prior** that guides constrained beam search and alleviates local-optimum errors). On **M-BEIR** and text-to-image evaluation datasets, DrIG consistently beats state-of-the-art generative multimodal baselines; hybrid reranking achieves a favorable efficiency-effectiveness trade-off against strong dense retrievers. Ablation and scaling analyses show how the base LMM, beam size, reranking depth, and fusion strategy affect performance.
- **Key innovations**: (1) A single residual-quantized identifier exploited in both sequential and set-based roles; (2) modality-first token design for cross-modal decoding; (3) a prefix-independent relevance prior inside constrained beam search; (4) generative-vs-dense accuracy gap addressed via hybrid reranking.

---

## 3. LLM Post-Training (OPD / RL)

### 3.1 CROP: Task Relevance via Counterfactuals for Selective On-Policy Distillation

- **arXiv**: [2608.13387](https://arxiv.org/abs/2608.13387) (cs.CL; submitted 2026-08-13) — **NEW**
- **Authors**: Enhan Li, Junhao He, Hongyang Du
- **Institution**: Not stated.
- **Abstract (faithful summary)**: OPD supervises a student on its own sampled trajectories but assigns equal credit to response tokens with unequal supervision value. Selective OPD allocates supervision non-uniformly by estimated training value, yet most criteria focus on *optimization need* (uncertainty, teacher-student disagreement), leaving **task relevance** — whether supervision ties to the semantic content of the current input — less directly characterized. **CROP** (Counterfactual Relevance for On-Policy Distillation) operationalizes task relevance via a **paraphrase-calibrated counterfactual sensitivity margin**. For each source prompt, CROP builds a validated original–paraphrase–counterfactual triplet, holds the student rollout fixed, and scores each response position by its sensitivity to a task-relevant condition change, calibrated by sensitivity to a meaning-preserving rewrite. Matched selection controls show CROP identifies more useful supervision positions than random or lowest-relevance selection; component comparisons confirm value from both counterfactual sensitivity and paraphrase calibration. Across two teacher–student settings, **CROP improves aggregate performance by 1.92 and 2.96 points over the strongest non-CROP selector**, establishing task relevance as a complementary selective-OPD criterion.
- **Key innovations**: (1) A new, complementary criterion (task relevance) for selective OPD; (2) counterfactual sensitivity margin calibrated by paraphrase sensitivity; (3) model-internal, contrast-specific token-level supervision allocation; (4) +1.92/+2.96 over the best non-CROP selector.

### 3.2 LOPD: Latent On-Policy Self-Distillation

- **arXiv**: [2608.13040](https://arxiv.org/abs/2608.13040) (cs.LG / cs.CL; submitted 2026-08-13) — **NEW**
- **Authors**: Guibin Zhang, Jiayang Lyu, Ran Sun, Xinlei Yu, Haoyu Zhao, Qibing Ren, Shuicheng Yan
- **Institution**: Not stated; Shuicheng Yan is affiliated with National University of Singapore (tentative).
- **Abstract (faithful summary)**: Learning from experience and internalizing it into policy is central to self-evolving AI. On-policy self-distillation (OPSD) uses a privileged self-teacher for dense supervision on the student's own trajectories, but existing methods rely on **designer-specified privileged artifacts** (answers, feedback, skills, trajectories), limiting end-to-end learnability and scalability. **LOPD** makes the teacher's privileged context itself **learnable end-to-end from experience**, rather than proposing another hand-crafted variant. Technically, LOPD retrieves relevant experiences and composes them into **continuous latent tokens** that condition a self-teacher, while the student generates trajectories from task + interaction history and receives dense token-level supervision at every visited prefix. A **privileged-margin objective** stabilizes learning of the latent context. Empirically LOPD (I) outperforms RLVR and representative OPSD methods (OPSD, SDPO, Skill-SD) on agentic tool use and code generation, and (II) surpasses GRPO and Skill-SD with **less than 30% of their rollout budget**. Ablations show making privileged context learnable is necessary for the gains.
- **Key innovations**: (1) Privileged context as learnable latent tokens retrieved from experience — removing hand-crafted artifacts from OPSD; (2) dense token-level supervision at every visited prefix; (3) a privileged-margin objective for latent stability; (4) <30% rollout budget vs. GRPO/Skill-SD at better or equal performance.

### 3.3 CrEST: Teach the Magnitude, Not the Direction — Verifier-Bounded Credit Assignment for Multi-Turn Multi-step LLM Agents

- **arXiv**: [2608.13179](https://arxiv.org/abs/2608.13179) (cs.AI; submitted 2026-08-13) — **NEW**
- **Authors**: Zechuan Wang, Siyuan Lu, Hongxuan Zhang, Linjian Mo, Chenyi Zhuang, Leilei Gan
- **Institution**: Not stated; Chenyi Zhuang (Ant Group) and Leilei Gan (Tsinghua) are plausible affiliations (tentative).
- **Abstract (faithful summary)**: RL with verifiable rewards (RLVR) gives a **verifier-bounded performance ceiling** for multi-turn tool-use agents, but its trajectory-level credit assignment conflates heterogeneous per-turn outcomes into one reward. OPD provides dense per-token supervision but is either teacher-bounded or prone to gradient concentration collapse. **CrEST** is a hierarchical credit assignment framework that keeps RL's verifier-bounded ceiling while adding dense token-level signals from a privileged self-teacher. Credit is resolved at two levels: **turn-segmented verified advantages** address inter-turn dilution, and **entropy-gated self-teacher modulation** refines intra-turn token contributions. On **BFCL V3 and WildToolBench**, CrEST consistently outperforms both RL and distillation baselines across two model scales, with the largest gains on long-trajectory and strict session-level metrics. The core idea: the teacher's role in policy optimization is reduced from **determining update directions to modulating update magnitudes**.
- **Key innovations**: (1) Two-level (turn / token) credit assignment preserving the verifier-bounded ceiling; (2) entropy-gated teacher modulation that avoids gradient concentration collapse; (3) "teach magnitude, not direction" — a clean conceptual reframing of the teacher's role; (4) wins on long-trajectory and session-level metrics.

---

## 4. Alignment

### 4.1 Synthetic Persona Pretraining: Alignment from Token Zero

- **arXiv**: [2608.13482](https://arxiv.org/abs/2608.13482) (cs.LG / cs.AI / cs.CL; submitted 2026-08-13) — **NEW**
- **Authors**: Julian Minder, Viktor Moskvoretskii, Raghav Singhal, Difan Jiao, Andy Arditi, Shaobo Cui, Yiderigun Borjigin, Kartik Bali, Stefan Krsteski, Harsh Raj, Huu Nguyen, Jannik Brinkmann, Ashton Anderson, Roland Aydin, Robert West (15 authors)
- **Institution**: EPFL (Robert West — high confidence) / University of Toronto (Ashton Anderson — high confidence).
- **Abstract (faithful summary)**: As LLM-based AI is deployed autonomously, aligning goals and values with humans becomes critical. Today alignment, and the assistant identity itself, are introduced only after pretraining, once behavioral priors are established — making values a **thin overlay** and potentially facilitating misalignment. **Synthetic Persona Pretraining (SPP)** installs the desired assistant persona **from token zero**. Three steps: (1) annotate pretraining documents with value-aligned **first-person reflections** derived from a normative value constitution; (2) pretrain with standard cross-entropy on both original documents and their reflections, installing the desired persona among many others; (3) post-train on user–assistant dialogue, **binding** the persona to the assistant identity ("persona binding"). Pretraining up to **3B parameters on 500B tokens**, SPP improves constitution following and jailbreak robustness, and reduces the misalignment rate in out-of-distribution moral dilemmas, while preserving capabilities. **Early intervention matters**: adding SPP only at the end of pretraining yields weaker constitution adherence, no value-priority shift, and less aligned dilemma choices. The advantage depends on persona binding and **increases with pretraining budget**.
- **Key innovations**: (1) Alignment moved into pretraining rather than a post-hoc overlay; (2) value-aligned first-person reflections as a data transformation at scale (500B tokens); (3) persona binding to fix the persona to the assistant identity; (4) scaling evidence that early interventions compound with pretraining budget.

---

## 5. LLM Efficiency (KV Cache & Quantization)

### 5.1 vToken: Token-Level Virtualization for Reclaimable KV Caches

- **arXiv**: [2608.13263](https://arxiv.org/abs/2608.13263) (cs.AI / cs.DC / cs.OS; submitted 2026-08-13) — **NEW**
- **Authors**: Yuanhang Gao, Xiangrui Yang, Yuanfeng Chen, Hongjia Chen, Qianru Lv, Wenfei Wu, Dongsheng Li
- **Institution**: Not stated; Wenfei Wu / Dongsheng Li are affiliated with Tsinghua University (high confidence).
- **Abstract (faithful summary)**: LLM serving faces a KV-cache memory bottleneck. PagedAttention uses fixed-size memory blocks to reduce allocator-level fragmentation, but recent KV eviction algorithms operate at **token granularity finer than block-level management**. The mismatch causes **intra-block fragmentation**, leaving a large fraction of allocated KV memory unreclaimable. **vToken** is a lightweight token-level virtualization layer that decouples logical token liveness from physical block placement: it maintains a stable logical token view through **token-table indirection** and realizes physical reclamation by **repacking live tokens asynchronously**, while preserving PagedAttention kernels and CUDA Graph compatibility. Implemented in **vLLM** and evaluated with H2O, Random, and Scissorhands: vs. a paired Naive-Evict baseline, vToken reduces retained KV blocks per request by **27.2%–72.3%**, improves SLA-constrained throughput by up to **1.37×**, and under a constrained active-KV budget extends maximum feasible concurrency by up to **2×** — while cutting the per-policy integration footprint from 500+ lines to under 50.
- **Key innovations**: (1) A virtualization layer (logical liveness / physical placement decoupling) inside a PagedAttention system; (2) asynchronous repacking that keeps kernel and CUDA-Graph compatibility; (3) drop-in integration for token-granular eviction policies (<50 lines); (4) large measured serving gains (1.37× throughput, 2× concurrency).

### 5.2 When Local Variance Optimality Is Not Enough: RoPE-Aligned Q/K Rotations for Dynamic 4-Bit Quantisation

- **arXiv**: [2608.13365](https://arxiv.org/abs/2608.13365) (cs.LG; submitted 2026-08-13) — **NEW**
- **Authors**: Shuhan Wang, Yilin Luo, Nan Xu, Chi Wang Cheung
- **Institution**: Not stated.
- **Abstract (faithful summary)**: Rotation-based post-training quantization applies an orthogonal transform across an entire attention head to reduce outlier-induced error; RoPE instead partitions heads into 2-D frequency pairs, raising the question of whether a transform respecting that decomposition beats full-head mixing. Prior work established per-pair rotations that commute with RoPE; the authors prove the **converse** — for distinct frequencies, no other single-head orthogonal map commutes with RoPE. For the head-shared parameterization, they derive the rotation angle minimizing the larger channel variance under a pooled-covariance, position-averaged surrogate and verify the implementation attains its analytic minimum. **Result (mostly negative)**: the evaluated head-shared pairwise configuration does not improve accuracy in dynamic W4A4KV4 — replacing the full-head Hadamard with it *increases* perplexity at short and long contexts across four checkpoints; composing pairwise with Hadamard satisfies the ±0.05-PPL criterion; estimating the shared angle from K alone improves pairwise-only but does not close the gap. Diagnosis: the analytic objective controls a position-averaged second moment of a pooled covariance, whereas the dynamic quantizer sets its step from a **tokenwise group range**; the pairwise transform also has only **two-channel mixing support**. A controlled interpolation from two-channel to full-head mixing shows K range, relative quantization error, and perplexity degradation all decrease as support grows — optimality for a structured surrogate need not reduce quantization error when surrogate and mixing support are misaligned with the quantizer's scale-setting statistic.
- **Key innovations**: (1) A converse theorem characterizing which single-head orthogonal maps commute with RoPE; (2) an analytic optimal-rotation derivation under a pooled-covariance surrogate; (3) a rigorous negative result tying surrogate–quantizer misalignment (position-averaged vs. tokenwise) to failure; (4) mixing-support interpolation as the diagnostic that explains the gap.

---

## 6. LLM Architecture & Training

### 6.1 Rethinking Normalization Placement for LLMs: Post-Norm under Curriculum Depth Growing

- **arXiv**: [2608.13156](https://arxiv.org/abs/2608.13156) (cs.AI; submitted 2026-08-13) — **NEW**
- **Authors**: Sheng Ren, Yadong Wang, Naiqiang Tan, Jiangang Kong, Jun Fang, Rui Liu, Jun Wang, Kai Chen, Lipeng Liang, Xiang Chen
- **Institution**: Not stated.
- **Abstract (faithful summary)**: Pre-norm is standard in modern Transformers because it facilitates joint optimization of full-depth models. The paper asks whether this preference persists when depth is introduced through a **curriculum**. In curriculum depth growth, each appended block receives the boundary representation produced by a trained prefix, making normalization placement relevant to **forward conditioning**. In a controlled distillation study (Qwen3-8B teacher, **9-layer student**), pre-norm and post-norm are indistinguishable under joint training (Δ0.0004 validation CE), while **post-norm improves over pre-norm by 0.0328 under curriculum growth — an order of magnitude larger**. A post-joint control matched by student active-layer tokens remains worse than post-grow, ruling out compute as the sole explanation. The ranking crosses over during the curriculum: post-norm takes the lead once blocks are appended; single-block and freeze controls localize the change to block appending rather than shallow-block quality or retraining. Boundary diagnostics associate post-norm with stable residual scales and pre-norm with structural-token scale drift; on a fixed batch, the final pre-grow block is nearly identity-mapped. Consistent with **boundary-scale conditioning** after new blocks are appended, the results motivate treating normalization placement and training curriculum as coupled design choices.
- **Key innovations**: (1) Demonstrates a placement × curriculum interaction (pre-norm is not universally optimal); (2) an order-of-magnitude win for post-norm specifically under curriculum growth; (3) careful controls (post-joint, single-block, freeze) localizing the effect to block appending; (4) boundary-scale diagnostics (residual vs. structural-token drift, near-identity final block).

---

## 7. Agents & Verified Code

### 7.1 Vero: Can AI Agents Build Formally Verified Software Repositories?

- **arXiv**: [2608.13522](https://arxiv.org/abs/2608.13522) (cs.LG / cs.AI / cs.LO / cs.PL / cs.SE; submitted 2026-08-13) — **NEW**
- **Authors**: Zhe Ye, Hantao Lou, Yuechun Sun, Peiyang Song, Zhengxu Yan, Timothe Kasriel, Qingyang Zhang, Kaiyu Yang, Soonho Kong, Jingxuan He, Dawn Song
- **Institution**: UC Berkeley (stated — repo is github.com/sunblaze-ucb/vero; Dawn Song / Kaiyu Yang / Jingxuan He are Berkeley-affiliated, high confidence).
- **Abstract (faithful summary)**: AI agents increasingly write code but provide no guarantee of correctness. **Verified code generation** — an agent producing both an implementation and a machine-checked proof of its specification — offers a stronger path to trustworthy AI-generated software. Existing benchmarks either target single functions or evaluate proof generation with provided implementations; whether agents can make coherent implementation + proof choices across real **multi-module codebases** is open. **Vero** is the first benchmark to evaluate joint implementation and proof synthesis at **repository level**: 43 multi-module instances from real-world repositories spanning **Python, Dafny, Verus, and Coq**, covering domains from cryptographic protocols to distributed systems. Each instance is a multi-module **Lean 4** repository with predetermined API interfaces, manually curated formal specifications, and reference implementations, supporting both proof-only and code-and-proof modes. For reliability, Vero includes an **audit mechanism** — agents may formally prove unsatisfiability of a given specification or incorrectness of reference code, surfacing latent curation errors. Evaluated with frontier coding-agent configurations + Lean toolchain access, the **strongest agent fully solves only 27 of 43 instances and closes no specifications on the hardest repositories** — a concrete testbed where current agents still fall short. Benchmark, curation pipeline, and harness are released.
- **Key innovations**: (1) First repository-level joint implementation-and-proof benchmark (Vero); (2) 43 multi-module Lean 4 instances across four source languages and diverse domains; (3) an audit mechanism that lets agents formally attack specs/reference code to correct curation errors; (4) a sober baseline — best agent 27/43, nothing closed on the hardest repos.

---

## 8. Reasoning & Search

### 8.1 TsuGO: Probing Search Efficiency in LLM Reasoning via Go Life-and-Death Problems

- **arXiv**: [2608.13221](https://arxiv.org/abs/2608.13221) (cs.AI; submitted 2026-08-13) — **NEW**
- **Authors**: Shunwen Bai, Ziping Ma, Chaoyang Zhang, Yarong Wang, Jiale Liu, Zhen Qin, Qingpei Guo
- **Institution**: Not stated.
- **Abstract (faithful summary)**: LLM-reasoning evaluation is moving from final-answer accuracy to process-level assessment, but existing methods still fail to capture **how models plan reasoning paths and allocate reasoning resources — how they organize search**. Prior process-level methods focus on CoT coherence/redundancy, and most benchmark tasks have a single objective solvable by static capabilities (derivation, tool use), leaving search organization unmeasured. **TsuGO** is a process-level benchmark for Search Efficiency using Go **life-and-death (tsumego)** problems: closed and verifiable solution spaces with inherent adversarial structure, making candidate generation, response checking, branch comparison, and backtracking *necessary* parts of reasoning. Constraining the solution space disentangles domain knowledge from search organization; TsuGO parses CoT into a **structured search tree** and reports Search Efficiency alongside Token Efficiency and other diagnostics/visualizations. Findings: current LLMs remain far from stable tsumego solving — stronger models succeed by finding the correct candidate earlier and sustaining effort on productive branches, but most behave much closer to **unguided search algorithms than to neural-guided KataGo**. **Longer CoT or higher Token Efficiency does not imply better search.** Search organization and reasoning-resource allocation are identified as missing dimensions in LLM-reasoning evaluation. (23 pages, 12 figures, 20 tables.)
- **Key innovations**: (1) A closed, adversarial, verifiable task class (tsumego) that forces search rather than incidental trace patterns; (2) CoT parsed into a search tree with Search Efficiency + Token Efficiency metrics; (3) disentanglement of domain knowledge from search organization; (4) evidence that length/efficiency ≠ search quality, positioning search organization as a missing evaluation dimension.

---

## 9. Games, Mechanism Design & LLM Economics

### 9.1 Keep, Customize, or Exit: Default Design and Token Pricing in LLM Reasoning Services

- **arXiv**: [2608.13315](https://arxiv.org/abs/2608.13315) (cs.GT / cs.AI / cs.LG / eess.SY; submitted 2026-08-13) — **NEW**
- **Authors**: Ahmet Bugra Gundogan, Yigit Turkmen, Melih Bastopcu
- **Institution**: Not stated; Melih Bastopcu is affiliated with University of Illinois Urbana-Champaign (tentative).
- **Abstract (faithful summary)**: Studies an LLM service where a provider chooses a **per-token price and a default reasoning-token allocation**, and a user may accept the default, customize the allocation, or exit. Larger allocations improve accuracy but raise token cost and latency. Modeled as a **Stackelberg game**, the user's unique optimal customized allocation is derived in closed form. For any price, the acceptable defaults form either an empty set or a **compact interval**; the provider's optimal default follows a **three-regime rule**; equilibrium computation reduces to one-dimensional price optimization; existence of equilibrium is proved. Defaults affect the implemented allocation **only when users value the convenience of avoiding customization**; otherwise every service-providing outcome implements the user's optimal customized allocation. Experiments with two compact open-weight reasoning models on five mathematics/science benchmarks support the accuracy–token model and show how model and task characteristics determine equilibrium prices, defaults, and allocations.
- **Key innovations**: (1) First principled (Stackelberg) model of default reasoning-token allocation + token pricing; (2) closed-form user optimum and a three-regime provider default rule; (3) precise conditions (convenience valuation) under which defaults actually bind; (4) empirical grounding with open-weight reasoning models on five benchmarks.

### 9.2 EA-RAM: Error-Aware Reverse Auction Mechanism for Large Language Model Routing

- **arXiv**: [2608.12719](https://arxiv.org/abs/2608.12719) (cs.GT / cs.AI; submitted 2026-08-13) — **NEW**
- **Authors**: Haolong Chen, Zhengyuan Xin, Liang Zhang, Lei Xue, Guangxu Zhu
- **Institution**: Not stated; Guangxu Zhu is affiliated with SUSTech (tentative).
- **Abstract (faithful summary)**: Routing each query to a cost-effective LLM is critical, but most routers rely on a centralized task center to predict model performance — an **information-risk mismatch** and scalability bottleneck as the model pool grows. The paper proposes a **market-based routing paradigm**: shift ex-ante prediction to LLM providers via a **reverse auction**, where providers bid self-predicted success probabilities and execution costs. Because provider predictions and center evaluations are inherently noisy, **EA-RAM** (Error-Aware Reverse Auction Mechanism) explicitly models this **Dual Error**. Results: EA-RAM is **Bayesian incentive compatible and individually rational under Dual Error**; sufficient conditions for center rationality are established; an explicit **welfare-loss bound** is derived. Robustness effects identified: opposite-signed errors can cancel; vanishing-tail link functions (e.g., logistic) stabilize clear-cut cases via saturation; extra noise smooths belief maps, reducing marginal-manipulation gains. Simulations and real-world benchmarks show EA-RAM is robust to Dual Error and achieves a **better cost–performance Pareto frontier than centralized baselines**, with extra gains when providers contribute local information.
- **Key innovations**: (1) Shifts performance prediction from a central task center to providers via reverse auction (decentralized routing); (2) first mechanism explicitly modeling dual error (provider + center); (3) Bayesian IC/IR with a welfare-loss bound under error; (4) identified robustness mechanisms (error cancellation, saturation, noise-smoothing); (5) Pareto-frontier gains vs. centralized routing.

### 9.3 Do LLMs Beat Nash? Testing Decentralized Coordination in Self-Play Multi-Agent Games

- **arXiv**: [2608.12547](https://arxiv.org/abs/2608.12547) (cs.MA / cs.RO; submitted 2026-08-12, in Fri Aug 14 listing) — **NEW**
- **Authors**: Deborah Sinishaw, Qile Zhu, Edwin Meriaux, Gregory Dudek
- **Institution**: Not stated; Gregory Dudek is affiliated with McGill University (high confidence). Submitted to IEEE MIT Undergraduate Research Technology Conference (URTC) 2026.
- **Abstract (faithful summary)**: LLM agents deployed without a central controller are often assumed to need communication to coordinate. This work asks what remains possible without it: when independent instances of the same model cannot communicate, can they still reason about counterparts well enough to **exceed the standard game-theoretic baseline for uncoordinated play**? They introduce a benchmark of **one-shot, no-communication games** where each of **13 language models** is told only that its counterparts run the same model and is evaluated against the **Nash equilibrium** of the underlying game. In two-player matrix games spanning **seven archetypes and 2–10 actions per player**, **two frontier-hosted models consistently exceed their Nash benchmark**, approaching the optimal joint outcome in several archetypes, while most open-weight models achieve only partial gains that vary sharply by game structure. Performance degrades substantially in **team-based games with 4+ interchangeable agents**, especially as the action space grows — whatever capability drives self-play gains in dyadic games does not transfer to larger teams. (5 pages, 5 figures.)
- **Key innovations**: (1) A clean experimental design isolating self-play coordination without communication, benchmarked against Nash; (2) 13-model × 7-archetype × 2–10-action coverage; (3) evidence that only frontier models reliably beat Nash in dyadic play; (4) a scaling-negative result — dyadic self-play capability does not transfer to 4+ agent teams.

---

## 10. Time Series

### 10.1 Into the ORBIT for Time Series: Training Regimes for Foundation Models

- **arXiv**: [2608.13262](https://arxiv.org/abs/2608.13262) (cs.LG / cs.AI; submitted 2026-08-13) — **NEW**
- **Authors**: Hongjie Xia, Yiding Liu, Yifan Hu, Peiyuan Liu, Zewei Dong
- **Institution**: Not stated.
- **Abstract (faithful summary)**: Time series foundation models (TSFMs) have advanced mainly through architecture, while **training regimes for large-scale heterogeneous corpora remain under-explored**; pretraining distributions are often poorly controlled with respect to domain imbalance, context requirements, prediction horizons, and missingness. **ORBIT** (Omni-Range Bootstrap Incremental Training) makes the distribution explicit and controllable, combining **Bootstrap Multi-Level Sampling** (controls dataset exposure; samples records, target variables, context windows, and prediction horizons) with **Omni-Range Incremental Training** (varies context lengths and horizons throughout a single training stage). Under ORBIT they train **Falcon-2.0**, a simple univariate encoder-only Transformer with missingness-aware **triple-channel patch tokenization** and parallel patch prediction, plus **Rank-Guided Cross-Depth Alignment** — a training objective using late-layer representations as stop-gradient teachers for shallow layers, at no additional inference cost. Evaluations on **GIFT-Eval and fev-bench** show strong zero-shot forecasting across diverse domains and frequencies.
- **Key innovations**: (1) Treats the training regime (sampling/curriculum over context, horizon, missingness) as a first-class, controllable object for TSFMs; (2) Bootstrap Multi-Level Sampling + Omni-Range Incremental Training; (3) a minimal univariate encoder-only backbone (Falcon-2.0) with missingness-aware tokenization; (4) inference-free cross-depth alignment objective; (5) strong zero-shot results on GIFT-Eval and fev-bench.

---

## 11. Theory & Scaling Laws

### 11.1 Neural Quadratic Forms: A Unified Minimal Model for Sudden Learning and Scaling Laws

- **arXiv**: [2608.13335](https://arxiv.org/abs/2608.13335) (cs.LG / cond-mat.dis-nn / cond-mat.stat-mech; submitted 2026-08-13) — **NEW**
- **Authors**: Liu Ziyin, Yizhou Xu, Tomaso Poggio, Isaac Chuang
- **Institution**: MIT (Poggio, Chuang — high confidence).
- **Abstract (faithful summary)**: Neural networks trained by gradient descent on smooth costs can nonetheless learn in steps — cost holds on long plateaus then drops abruptly — while training losses instead follow smooth power laws. Both behaviors occur across architectures with very different microscopic structure, the signature of a few relevant collective variables. A symmetry fixes what those variables are: a network layer is a sum over interchangeable units (relabeling leaves it unchanged); given smoothness and vanishing unit gradients at the origin, symmetry enforces a **universal leading form** for the expansion about the near-zero weights at training start: the quadratic **Tr[WWᵀA(x)]**, in which every architectural detail is confined to a single "structure matrix" **A(x)** computed per architecture. Perceptrons, attention layers, mixtures of experts, and convolutions become **one model at different A**. Training dynamics close on the order parameter **M = WWᵀ** and, when data matrices share an eigenbasis, reduce to a **Lotka–Volterra equation** whose modes switch on one after another. Smaller initial weights spread switch-on times apart — plateaus appear as a **singular limit of a smooth flow**; when many modes are unresolved, the events merge into a power law in training time whose **exponent the theory predicts**. Confirmed numerically across training methods and architectures.
- **Key innovations**: (1) A symmetry argument (unit permutation invariance) pinning the universal near-zero-weight expansion Tr[WWᵀA(x)]; (2) unification of perceptron/attention/MoE/convolution into one model via the structure matrix; (3) training dynamics reducing to a Lotka–Volterra system with a predicted power-law exponent; (4) a unified account of both sudden learning (grokking-like plateaus) and smooth scaling-law losses.

---

## Cross-cutting trends

- **CVR/rec in industry keeps splitting "the click" into finer signals.** STAR (challenge) adds intent/interest-aware structure on top of HyFormer-style backbones; DrEM treats pxtr noise on both supervision and feature sides of ensemble ranking; MARCO (08-12) decomposed clicks by intent. The recurring message: a single aggregate label (click / CVR / pxtr) hides structure that calibration and ranking both need.
- **SID/generative recommendation is now being held to a fairness and decoding-quality bar.** FSGR attacks token frequency bias (a new, SID-specific failure mode) with codebook- and training-stage fixes; DrIG reuses one identifier in sequential + set-based roles to fix prefix-error local optima in multimodal generative retrieval. Both treat generation-specific artifacts, not generic model quality.
- **OPD/post-training supervision continues to bifurcate: "what to supervise" vs. "how to supervise".** CROP adds task relevance as a complementary selection criterion to uncertainty/disagreement (08-13's Rubric Dropout, ReOrder-OPD line); LOPD makes the teacher's privileged context itself learnable, and CrEST cuts the teacher down to a magnitude modulator under a verifier-bounded ceiling. The field is converging on dense, verifier-anchored, artifact-minimal credit assignment.
- **Alignment is being pushed earlier in the pipeline.** SPP installs the assistant persona from token zero with value-aligned first-person reflections and shows early intervention compounds with pretraining budget — a direct counterpoint to the "alignment as post-hoc overlay" default. Pair with 08-13's implicit-personalization localization (2608.11735) for the two ends of the alignment timeline.
- **KV-cache and quantization efficiency are hitting granularity mismatches.** vToken virtualizes token liveness so token-granular eviction actually reclaims memory inside PagedAttention (1.37× throughput); the RoPE-rotation paper contributes a clean negative result — the quantizer's tokenwise scale statistic and the transform's position-averaged surrogate are misaligned, so surrogate-optimal rotations don't transfer. Efficiency gains increasingly come from aligning *where* decisions are made, not better decisions alone.
- **LLM economics and routing are formalizing via game theory.** Two cs.GT papers in one batch — Stackelberg default/token pricing (Keep, Customize, or Exit) and the Dual-Error-aware reverse auction (EA-RAM) — bring provable incentive properties (BIC/IR, welfare bounds) to token pricing and model routing, continuing the mechanism-design thread (ContractSim 08-12, Welfare Approximation 08-13).
- **Search organization is a newly measurable dimension of reasoning.** TsuGO (Go life-and-death) shows CoT length/token efficiency does not imply search quality and gives a structured search-tree diagnostic; parallel to Do LLMs Beat Nash? (no-communication self-play), both measure *process* rather than final accuracy. Longer ≠ better, and dyadic strengths don't transfer to teams.
- **Verified/trustworthy code and value grounding gain benchmarks.** Vero sets the first repository-level joint implementation-and-proof bar (best agent 27/43) with an audit mechanism to fix latent spec errors; together with SPP these stake out the "guarantees" end of the agent stack (implementation proof + value alignment).
- **Time-series and scaling theory mature around controllable regimes.** ORBIT argues the *training regime* (sampling/curriculum over context, horizon, missingness) is the under-exploited lever for TSFMs; Neural Quadratic Forms unifies sudden learning and scaling laws under one symmetry-derived minimal model with a predicted power-law exponent — theory is moving from "what scales" toward "why and when it switches".

## Methodology & caveats

- Papers selected from the Fri Aug 14, 2026 arXiv announcement batch across the requested domains (AI, LLM, agents, coding, recommendation, advertising/CTR/conversion, games, mechanism design, time series). Streams scanned: cs.LG 157 / cs.CL 101 / cs.AI 204 / cs.IR 19 / cs.GT 6 / cs.MA 14 / cs.SE 18 new. Discovery used web listing pages (`arxiv.org/list/<cat>/recent`); cs.AI (204 new) and cs.LG (157 new) were only partially scanned at title level, so some strong candidates in those streams may be missed. All 20 selected papers' metadata was verified against individual abstract pages (`arxiv.org/abs/<id>`).
- **Zero-overlap verification**: every candidate arXiv ID grep-checked across wiki/index.md, wiki/log.md, and wiki/synthesis/** before inclusion — 0 hits each. Prior-day coverage: the 2026-08-13 arxiv-daily / arxiv-paper-check / conference-digest covered IDs up to 2608.12307; every paper in this report is ≥ 2608.12547. This is the first 2026-08-14 output, so same-day arxiv-daily / arxiv-paper-check — where they would normally claim cs.IR/cs.AI papers — did not yet exist at time of writing; the industrial cs.IR/cs.AI/cs.GT picks (STAR, DrEM, FSGR, DrIG, EA-RAM, TsuGO, vToken) are therefore included here rather than deferred.
- Institution/company attribution: **high confidence** where stated (UC Berkeley via the Vero repo; EPFL/University of Toronto for SPP co-authors) or well-known affiliations (Tsinghua for vToken's Wu/Li; MIT for Poggio/Chuang; McGill for Dudek); **tentative** where inferred from a single co-author (Nankai for FSGR; Shenzhen University for DrEM; NUS for LOPD; Ant Group/Tsinghua for CrEST; UIUC for the pricing paper; SUSTech for EA-RAM). No affiliation should be treated as authoritative without checking the paper.
- Submission-date caveat: 2608.12547 (Do LLMs Beat Nash?) is listed as submitted 2026-08-12 but appears in the Fri Aug 14 cs.MA listing; it is new to the wiki (0 hits) and included. 2608.12987 (DrIG) carries the comment "This paper is under review".

## Related pages
- [arXiv Daily Digest (August 13, 2026)](../2026-08-13/arxiv-daily.md) — prior breadth pass (IDs up to 2608.12307)
- [arXiv Paper Check — AI & CTR (August 13, 2026)](../2026-08-13/arxiv-paper-check.md) — prior CTR/Rec/Ads curation
- [Conference Digest (August 13, 2026)](../2026-08-13/conference-digest.md) — KDD 2026 wrap-up incl. Tencent UniRec KDD Cup navigation
- [arXiv AI Research Search (August 12, 2026)](../2026-08-12/arxiv-ai-search.md) — the template for this report; prior AI scan (Wed Aug 12 batch)
