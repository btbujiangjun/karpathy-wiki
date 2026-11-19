# arXiv Daily Digest — 2026-11-19

**Topics:** AI, LLMs, recommendation, advertising, sequential modeling, CTR, games, and related areas.
**Source:** arXiv API (`export.arxiv.org`), papers submitted 2026-11-09 → 2026-11-19, sorted by submission date (newest first). 24 papers.

---

## 1. NarrowSpec: Draft Hidden Width Need Not Match the Target in Speculative Decoding

- **arXiv ID:** 2611.23835v1
- **Published:** 2026-11-18
- **Authors:** Alagappan Valliappan, Ankit More, Dheevatsa Mudigere, Jatin Mitra
- **Institution/Company:** N/A (not provided in arXiv API)
- **Categories:** cs.CL, cs.LG, cs.PF
- **Link:** https://arxiv.org/abs/2611.23835v1
- **Abstract:** Speculative decoding is widely used to speed up generation in large language models (LLMs), with a small draft model proposing tokens that one forward pass of the target model verifies. Draft models that read the target's hidden states, such as DFlash and EAGLE-3, typically inherit the target's hidden width. We show that the draft's whole residual stream can run at half or a quarter of that width while largely preserving acceptance. For DFlash, which borrows the target's vocabulary projection, the trained output adapter folds into it, giving one narrower projection with logits unchanged up to floating-point rounding. We test two drafter families, DFlash and EAGLE-3, on two targets, Qwen3-8B (NVFP4) and GPT-OSS-20B (MXFP4), in SGLang on a B200 and a DGX Spark (GB10). At batch size 1 and temperature 0, narrowing the draft to half or a quarter width speeds up end-to-end decoding by 1.06–1.12x on B200 and 1.13–1.44x on GB10.
- **Key innovations:**
  - Draft residual stream at half/quarter width with preserved acceptance; logits unchanged up to fp rounding via output adapter folding.
  - End-to-end speedups 1.06–1.12x (B200), 1.13–1.44x (GB10); up to 1.21x across batch sizes.

## 2. When Do LLMs Model the Right Target? Problem Formulation in High-Stakes Risk Prediction

- **arXiv ID:** 2611.23638v1
- **Published:** 2026-11-18
- **Authors:** Jennifer Zhang, Amanda Coston
- **Institution/Company:** N/A
- **Categories:** cs.CY, cs.LG, stat.ME
- **Link:** https://arxiv.org/abs/2611.23638v1
- **Abstract:** Generative AI is increasingly used to assist with data science tasks, yet fundamental questions remain about its ability to correctly formulate analytical problems. We investigate how well large language models (LLMs) can formulate prediction problems when developing models for high-stakes decision making. We focus on decision dependency (historical decisions affect observed outcomes). LLM-generated code and explanations are evaluated: whether the code implements a procedure appropriate for estimating the intended outcome under the study's assumptions. When prompts specify the target, the needed assumption, and the procedure, target-aligned implementation reaches 99–100%; a simple prompt description of how decisions affect outcomes suffices for frontier models.
- **Key innovations:**
  - Quantifies LLM failure to address decision dependency without guidance; 99–100% target-aligned implementation when prompts fully specify target/assumption/procedure.
  - Validity-centered guidelines for LLM-assisted predictive modeling; establishes validity as necessary before deployment.

## 3. ReflectScene: MLLM-Guided Closed-Loop Diffusion for 3D Indoor Scene Generation

- **arXiv ID:** 2611.23845v1
- **Published:** 2026-11-18
- **Authors:** Jiawei Shen, Jie Feng, Junpeng Zhang, Guanbin Li, Wanyi Chen, Weisheng Dong, Guangming Shi
- **Institution/Company:** N/A
- **Categories:** cs.AI, cs.CV
- **Link:** https://arxiv.org/abs/2611.23845v1
- **Abstract:** Text-conditioned 3D indoor scene generation requires layouts satisfying geometric, functional, and semantic constraints; existing diffusion methods rely primarily on static textual conditions, limiting their ability to assess evolving scenes and translate semantic discrepancies into executable object-level corrections. MLLM-based post-hoc refinement provides semantic feedback but remains decoupled from denoising, potentially disrupting scene coherence. We propose ReflectScene, an MLLM-guided closed-loop diffusion framework: (1) Hierarchical Prior-Grounded Scene Understanding aligns structured layouts with multi-view visual evidence via a frozen MLLM; (2) MLLM-Guided Semantic Reward Evaluation distills MLLM diagnoses into a lightweight Reward Predictor; (3) Decision-Conditioned Trajectory-Consistent Diffusion integrates selected corrections through transient conditioning and persistent clean-estimate projection.
- **Key innovations:**
  - Closed-loop MLLM feedback into diffusion denoising; hierarchical prior-grounded scene understanding via multi-view visual evidence.
  - Lightweight reward predictor enabling correction decisions with reduced compute; preserves non-target arrangements during denoising.

## 4. Re-Testing LLM-Based C-to-Rust Translations Against Their Original C

- **arXiv ID:** 2611.23839v1
- **Published:** 2026-11-18
- **Authors:** Muhammad Hassnain
- **Institution/Company:** N/A
- **Categories:** cs.SE
- **Link:** https://arxiv.org/abs/2611.23839v1
- **Abstract:** Most C-to-Rust translators use LLMs and report success rates from their own correctness checks. We survey 34 LLM-based translators; only one reports testing its check; 11 release runnable C and Rust. We re-test all 11 by running both on generated inputs and comparing every output (divergence counted only where C has no UB). All 11 release defective translations: 160 defects found, 93 outright errors on ordinary inputs. Their own checks accepted 86 defective translations; for 81, the released check never compared on an input exposing the defect. Success rates are unreliable unless compared on unseen inputs.
- **Key innovations:**
  - Empirical audit: 160 defects in 11 released translators, 93 outright errors; own checks accepted 86 defective translations.
  - Recommendations: compare every output with C's on repair-loop-unseen inputs; check verifiers reach assertions; release exactly what checks accept.

## 5. Reliability is a user-specific property of large language models

- **arXiv ID:** 2611.23732v1
- **Published:** 2026-11-18
- **Authors:** Xingyu Zhao
- **Institution/Company:** N/A
- **Categories:** cs.AI, cs.SE
- **Link:** https://arxiv.org/abs/2611.23732v1
- **Abstract:** Public benchmarks compare LLM capabilities, but users experience the same ranked model differently. We argue LLM reliability should be assessed for specified users and conditions of use. We distinguish testing-to-discover-faults from testing-to-assess-reliability, identify ten modelling considerations, and propose a six-workstream roadmap: claim specification, dynamic operational profiles, graded outcomes, local probabilistic robustness, interaction dependence, statistical inference with reassessment.
- **Key innovations:**
  - Versioned operational claims stating whose requirements are covered, under which conditions, with what uncertainty.
  - Local probabilistic robustness addressing behavioural variation hidden when different inputs are treated as the same task.

## 6. Modeling LLM Reasoning Dynamics with Structural Representations

- **arXiv ID:** 2611.23749v1
- **Published:** 2026-11-18
- **Authors:** Ilia Karpov, Andrey Atamanyuk, Dmitry Ilvovsky, Aleksandr Anokhin, Alex Elizov, Dmitry Zagorulkin, Sergei O. Kuznetsov
- **Institution/Company:** N/A
- **Categories:** cs.AI
- **Link:** https://arxiv.org/abs/2611.23749v1
- **Abstract:** Language-model reasoning alternates between sustained activities and local operations. T/E/S combines text, local events, and spans of activity. Across reasoning and information-seeking tasks, events and spans improve next-outcome prediction in 70/76 evaluation groups (Transformer) and 74/76 (Qwen with LoRA). Bounds that cancel shared continuation mass recover full DP actions while reducing mean inference CPU time by 77.7%.
- **Key innovations:**
  - Structural observer (text/events/spans) predicting whether a fixed inference procedure finishes within a CPU allowance; Brier loss 0.0836 → 0.0756 on HotpotQA/MuSiQue.
  - Proves counting hardness under explicit encodings; budget-allocation bounds recovering optimal actions with 77.7% less inference time.

## 7. Learning Martial Arts Motion Skills for Animating Opponents in VR Sparring Games

- **arXiv ID:** 2611.23825v1
- **Published:** 2026-11-18
- **Authors:** Jiqing Wen, Qixuan Shi, Robert LiKamWa, Pavan Turaga
- **Institution/Company:** N/A
- **Categories:** cs.AI, cs.HC, cs.MM, cs.RO
- **Link:** https://arxiv.org/abs/2611.23825v1
- **Abstract:** Animating virtual opponents in martial arts games requires physically plausible motions with technique, timing, transitions, and target-directed intent. Traditional handcrafted animations are labor-intensive. We present a framework: pretrain martial arts motion skills from a Tang Soo Do MOCAP dataset using RL with adversarial style rewards, then adapt with target-directed striking and threat-aware evasion rewards. A user study evaluates plausibility/smoothness/form; a VR sparring prototype (Meta Quest) combines policy-generated clips with lightweight state control.
- **Key innovations:**
  - RL pretraining of a reusable martial arts skill repertoire + adaptation to target-directed behavior.
  - VR prototype for interactive opponent animation in sparring games.

## 8. Thinking Fast, Anywhere: One System-1 for the Decision Points of Any Agent Workflow

- **arXiv ID:** 2611.23751v1
- **Published:** 2026-11-18
- **Authors:** Rui Li, Liyang He, Zheng Zhang, Zhenya Huang, Qi Liu
- **Institution/Company:** N/A
- **Categories:** cs.AI, cs.CL, cs.LG
- **Link:** https://arxiv.org/abs/2611.23751v1
- **Abstract:** Autonomous LLM agents invoke a large model (System-2) at every step even when choices are among known candidates. We present AnyS1: turns human-authored procedural skills into shared, domain-general decision points (offline mining of 1,000+ public skills, execution-grounded trajectory collection, Any-DP dataset) and trains a single calibrated 4B pointer System-1. At runtime, compiled workflows resolve routine decisions in one forward pass, falling back to System-2 below a calibrated threshold.
- **Key innovations:**
  - AnyS1 framework turning skill instructions into domain-general decision points; Any-DP dataset of execution-grounded trajectories.
  - Cuts episode cost by 75–91% and model-call time by 63–92% while preserving reliability.

## 9. Evaluating Governed LLM-Driven ML Experimentation: Lifecycle, Provenance, and Failure Metrics

- **arXiv ID:** 2611.23678v1
- **Published:** 2026-11-18
- **Authors:** Dowling Wong
- **Institution/Company:** N/A
- **Categories:** cs.AI, cs.LG, cs.SE
- **Link:** https://arxiv.org/abs/2611.23678v1
- **Abstract:** Autonomous ML agents are judged by best score, but not how: staying in edit scope, trial bookkeeping (keep/discard), and provenance. We propose a control plane owning trial lifecycle with edit-scope checks and a keep/discard decision recorded to an append-only ledger; governance metrics (invalid-action rate, repeated-bad rate, provenance completeness). Across six tasks and 1,445 trials the same contract applies unchanged; failures that score hides (120-trial no-memory arm, out-of-scope proposals, rerun after hash-detected reproducibility failure) are exposed.
- **Key innovations:**
  - Ledger-based governance: invalid-action rate, repeated-bad rate, provenance completeness; all 1,445 trial ledgers released for recomputation.
  - Exposes hidden failures (silent trial drops, out-of-scope proposals, reproducibility resets) a score-only metric misses.

## 10. Plug-and-Play Multi-Licensee Robust Watermarking for Mixture-of-Experts LLMs

- **arXiv ID:** 2611.23838v1
- **Published:** 2026-11-18
- **Authors:** Jianshuo Liu, Kang G. Shin, Haining Wang
- **Institution/Company:** N/A
- **Categories:** cs.CR
- **Link:** https://arxiv.org/abs/2611.23838v1
- **Abstract:** MoE LLMs offer high capacity but distribute weights expose IP leakage risk. Existing watermarking is fragile under MoE routing or needs costly retraining per licensee. We present PPMoE: trains a compact set of mergeable incremental weight modules steering the MoE router to distinct, mutually compatible routing patterns; owners merge modules on the fly per licensee without retraining. Attribution via white-box (inspect routing/merged modules) or black-box (output token likelihood ratios); robust against adaptive removal.
- **Key innovations:**
  - First plug-and-play multi-licensee watermarking for MoE LLMs: selective merging of pre-trained modules per licensee at distribution time.
  - High attribution accuracy with preserved utility; robust across five MoE models, seven benchmarks, varying licensees.

## 11. Rented Oscillations: Multi-Tenant Data Center Workload Synchronization Attacks and Mitigation

- **arXiv ID:** 2611.23666v1
- **Published:** 2026-11-18
- **Authors:** Zaint A. Alexakis, Li Zhou, S. Gokul Krishnan, Charalambos Konstantinou
- **Institution/Company:** N/A
- **Categories:** cs.CR, eess.SY
- **Link:** https://arxiv.org/abs/2611.23666v1
- **Abstract:** Adversaries rent workstations and run unoptimized LLM training, synchronizing consumption into large periodic oscillations while individual workloads are indistinguishable from benign. Characterize oscillation periodicity; small/large-signal assessment; weak points in network; MW-scale oscillations saturate generators; Floquet analysis shows lightly damped mode. Mitigation: signal-energy detection and re-timing workloads to minimize oscillatory energy.
- **Key innovations:**
  - Stealthy oscillation attack model on multi-tenant data centers via rented LLM training; MW-scale network impact.
  - Detection + mitigation (re-timing) validated with power hardware-in-the-loop experiments on a surrogate transmission model.

## 12. Localizing Text Anonymization for Trustworthy AI: Extending RAT-Bench to Malaysian Microdata and PII

- **arXiv ID:** 2611.23704v1
- **Published:** 2026-11-18
- **Authors:** David Hong Liang Chew, Zexi Yao, Nataša Krčo, Matthieu Meeus, Waqas Khalid Obeidy, Yves-Alexandre de Montjoye
- **Institution/Company:** N/A
- **Categories:** cs.CL
- **Link:** https://arxiv.org/abs/2611.23704v1
- **Abstract:** LLM-based anonymizers provide strong privacy-utility trade-offs on Malaysian English and Bahasa Malaysia: reduces Easy/Hard re-identification risk to 23–29% with BLEU 0.77–0.94 (vs. severe over-redaction in non-LLM tools). Transfer of anonymizers to new deployment settings (languages, PII formats, cultural contexts) matters before deploying in public-sector, workplace, or local AI pipelines.
- **Key innovations:**
  - Extends RAT-Bench to Malaysia (microdata, PII formats, cultural transcripts) with LLM attacker evaluation.
  - NER- and LLM-based anonymizers' privacy-utility trade-off quantified across languages/formats; empirical transfer insights.

## 13. RACE: Ranking-Uncertainty Aware Capacity-Adaptive Customization for Efficient Sequential Recommendation

- **arXiv ID:** 2611.18244v1
- **Published:** 2026-11-13
- **Authors:** Tianqi Liu, Kaipu Sun, Kairui Fu, Wenkai Wang, Sihao Liu, Hui Zang, Ran Chen, Tao Wang, Shengyu Zhang
- **Institution/Company:** N/A
- **Categories:** cs.AI, cs.IR
- **Link:** https://arxiv.org/abs/2611.18244v1
- **Abstract:** Efficient sequential recommendation: deploying models under resource-constrained environments requires compression; existing methods apply uniform compression ratios, causing a Capacity-Complexity Mismatch. RACE (Ranking-uncertainty Aware Capacity-Adaptive Customization for Efficient Sequential Recommendation) dynamically adapts model structures and input sequences with uncertainty-aware compression ratios. RACE captures the model's intrinsic prediction uncertainty of top-K distributions (list-wise ranking-uncertainty metric from distributional stability) as a proxy for instance complexity; a lightweight predictor (trained via self-supervision from early-layer features) anticipates it. Instance-specific slimming in two dimensions: hypernetwork-style channel sensitivity extractor identifies parameter redundancy; importance-aware progressive sequence filtering mitigates data redundancy.
- **Key innovations:**
  - RACE framework: uncertainty-aware capacity adaptation, structure + input sequence customization.
  - Extensive experiments on four datasets: better accuracy/efficiency/adaptability than SOTA compression baselines.

## 14. CONCORD-Rec: Catalog-Conditioned Modality Utility for Semantic-ID Diffusion Recommendation

- **arXiv ID:** 2611.23710v1
- **Published:** 2026-11-18
- **Authors:** Haopeng Jin, Bingkang Shi, Tao Yu, Yifei Ma, Hao Liu, Hongzhu Yi, Jinwen Luo
- **Institution/Company:** N/A
- **Categories:** cs.IR
- **Link:** https://arxiv.org/abs/2611.23710v1
- **Abstract:** Multimodal generative recommendation with semantic IDs struggles to distinguish modalities that alter token predictions from those that reduce catalog-level ambiguity. CONCORD-Rec: reliability-conditioned discrete diffusion recommender supervised by counterfactual catalog-partition utility; evaluates out-of-fold teacher coalitions over the exact feasible catalog support; counterfactual loss differences supervise an availability-masked tokenwise gate. Improves NDCG by 4% (and 14.63% under 30% conflict); full-vs-uniform T=16 sweep improves 2.00–3.58% while reducing p95 latency by up to 86.89%.
- **Key innovations:**
  - Counterfactual catalog-partition utility for discrete diffusion recommenders; theoretical ranking stability bounds under gate perturbations.
  - Handles missing/degraded/conflicting audio-visual-text streams; reduces p95 latency up to 86.89%.

## 15. Cluster-Guided Decoding with Trust-Region Constraints for Personalized Recommendation

- **arXiv ID:** 2611.22163v1
- **Published:** 2026-11-17
- **Authors:** Gezheng Wen, Chao Shen, Raviteja Anantha, Tan Shen Cliff Chung, Layne C. Price
- **Institution/Company:** N/A
- **Categories:** cs.IR
- **Link:** https://arxiv.org/abs/2611.22163v1
- **Abstract:** CG2R: learns a hierarchy of semantic clusters; cluster-level prior steers item ranking directly (adds prior to the item scoring rule, unlike pre-filtering). Cold-start users remain served (prior from centroids). Outperforms classical/neural/LLM baselines in Recall/nDCG, with gains widening as catalogs grow sparser; millisecond serving latency as low-latency first-stage retrieval.
- **Key innovations:**
  - Cluster-prior added directly to scoring rule (not just candidate pre-selection); cold-start-compatible via centroid priors.

## 16. IntentFlow: An Intent-Driven Real-Time Multimodal Search System with Image-Text Queries at Xiaohongshu

- **arXiv ID:** 2611.20448v1
- **Published:** 2026-11-16
- **Authors:** Dongjia Zhao, Yuchen Ma, Chunsheng Shi, Ziqiu Gui, Chao Yuan, Jianing Zhu, Zhaoxing Zhang, Yahui Liu, Daoxin Zhang, Yi Wu, Yao Hu, Cheng Chen
- **Institution/Company:** N/A
- **Categories:** cs.IR
- **Link:** https://arxiv.org/abs/2611.20448v1
- **Abstract:** Multimodal search for UGC notes via image-text queries; query-note relevance depends on retrieval intent, not just visual/topical similarity. IntentFlow: hierarchical intent taxonomy guides data construction, embedding, reranking; offline agentic data workflow builds training supervision; embedding combines intent-aware contrastive learning, graded ranking, distillation; compact reranker assesses evidence conditioned on intents. A/B test: +28.17% Top-4 query CTR, +18.96% query CTR, +12.56% time spent per user; P50 latency 1.07s.
- **Key innovations:**
  - Intent taxonomy aligning retrieval and reranking; CTR improvements (28.17% Top-4, 18.96% Top-1) in A/B test at scale.

## 17. UrbanROI: Causal Modeling for Regional ROI Forecasting under POI Entry

- **arXiv ID:** 2611.20180v1
- **Published:** 2026-11-15
- **Authors:** Zhaoqi Zhang, Miao Xie, Linyou Cai, Qianlong Xie, Xingxing Wang, Siqiang Luo, Gao Cong
- **Institution/Company:** N/A
- **Categories:** (not listed)
- **Link:** https://arxiv.org/abs/2611.20180v1
- **Abstract:** Regional ROI forecasting under POI entry: predict future ROI trajectory of a commercial region after a new POI is introduced; captures interaction effects among surrounding POIs. UrbanROI: Intervention-aware causal forecasting; Interaction-aware Regional Graph Module models competitive relationships among POIs (spatial proximity, request contexts, signals); constructs treatment/control graphs to simulate factual/counterfactual states. Outperforms baselines on advertising datasets.
- **Key innovations:**
  - Intervention-aware causal regional ROI forecasting with treatment/control graph construction.
  - Interaction-aware Regional Graph Module; competitive POI relationships learned from request contexts.

## 18. Bajillion: Cryptographic Clearing for Micropayments

- **arXiv ID:** 2611.21883v1
- **Published:** 2026-11-16
- **Authors:** Patrick O'Grady, Guru-Vamsi Policharla
- **Institution/Company:** N/A
- **Categories:** (not listed)
- **Link:** https://arxiv.org/abs/2611.21883v1
- **Abstract:** Web advertising is budget-dependent; replacement: AI agents pay fraction-of-a-cent per request at web scale. Bajillion: clearing protocol for scalable micropayments; sender signs request; untrusted operator gives preconfirmation; periodic epoch close posts only net effect; operator can only omit payments (never debit beyond signed or misdirect). Shortchanged receivers prove omission → halt protocol. Senders never dispute; suitable for ephemeral AI agents.
- **Key innovations:**
  - At-most-once debit via signed requests + preconfirmations + epoch closing; no sender disputes needed.
  - Reusable agent-friendly micropayment protocol scalable to tens of millions of payments/sec.

## 19. Media Trading with Censored Auction Prices: A Stochastic Control and Reinforcement Learning Approach

- **arXiv ID:** 2611.16992v1
- **Published:** 2026-11-12
- **Authors:** Yun-Ithry Gamrani, Huyên Pham
- **Institution/Company:** N/A
- **Categories:** (not listed)
- **Link:** https://arxiv.org/abs/2611.16992v1
- **Abstract:** Real-time bidding: agencies balance performance, margins, budget; market-clearing prices observed only on successful bids → information for decisions depends on policy. Stochastic control model with latent price process; exploratory subcampaigns with randomized bids construct consistent price estimator (N^-1 MSE). Model-based calibration (forward equations + HJB policy iteration + PINN) and entropy-regularized actor-critic (model-free) methods; synthetic experiments.
- **Key innovations:**
  - Consistent censored auction-price estimator from exploratory randomized subcampaigns (N^-1 error bound).
  - Stochastic-control + RL pipeline for media trading under budget/margin constraints.

## 20. Data-Driven Robust Inventory Planning and Advertising under Product Return

- **arXiv ID:** 2611.16778v1
- **Published:** 2026-11-12
- **Authors:** Hongyan Zhang, Yugang Yu, Qinshen Tang, Ye Shi, Li Chen
- **Institution/Company:** N/A
- **Categories:** (not listed)
- **Link:** https://arxiv.org/abs/2611.16778v1
- **Abstract:** Advertising drives demand and returns; joint inventory + advertising decisions across a season. Linear net-demand/return models with cross-product spillovers; estimate-then-robustify (ETR) in data-driven robust satisficing; finite-sample out-of-sample profit guarantee for any parameter estimator; asymptotically optimal when data is sufficient.
- **Key innovations:**
  - Joint inventory/advertising robust optimization under partial observability of ad clicks; ETR approach with asymptotic optimality.

## 21. TokenFormer V2: Breaking the Resolution-Complexity Dilemma in Unified Recommendation

- **arXiv ID:** 2611.19074v1
- **Published:** 2026-11-14
- **Authors:** Kaihui Wu, Guoming Li, Liang Guo, Yifeng Zhou, Yuehong Hu, Junwei Pan, Zhixiang Feng, Chengguo Yin, Wenqi Fan, Haijie Gu, Jie Jiang
- **Institution/Company:** N/A
- **Categories:** cs.IR, cs.LG
- **Link:** https://arxiv.org/abs/2611.19074v1
- **Abstract:** Industrial recommendation's resolution–complexity dilemma: dense interactions are expensive to model, compact summaries lose detail. TokenFormer V2: decouples representation resolution from interaction density via group-wise token layout, hierarchical group merging, NS Fusion and Global Sync modules. On Tencent Advertising Algorithm Competition 2026 (TAAC 2026): top-ranking accuracy, 5.1× fewer FLOPs vs. leading baselines; on WeChat Channels advertising: +0.07pp AUC; live A/B test +2.33% GMV.
- **Key innovations:**
  - Local–global decomposition: Full-Resolution Readout preserves every encoded event; 5.1× FLOP reduction.
  - +2.33% GMV in live A/B testing on WeChat Channels advertising.

## 22. Incremental Roseland: Batch-wise Landmark Diffusion via Kernelized Sequential Karhunen--Loève Update

- **arXiv ID:** 2611.23414v1
- **Published:** 2026-11-17
- **Authors:** Jeanie Schreiber
- **Institution/Company:** N/A
- **Categories:** (not listed)
- **Link:** https://arxiv.org/abs/2611.23414v1
- **Abstract:** Roseland computes diffusion-map-style spectral embeddings from landmark affinity via SVD of degree-normalized data-to-landmark kernel. Incremental Roseland (iRoseland): landmark affinity as row-growing matrix, kernelized Sequential K-L update, degree correction via first-order expansion; single pass, bounded memory independent of points processed. Forgetting factor for drifting distributions. Experiments: agreement with Roseland on stationary data; exceeds equal-memory Roseland by an order of magnitude on long streams.
- **Key innovations:**
  - Incremental SVD update (kernelized Sequential K-L) for streaming landmark diffusion; sample-size-invariant embeddings.
  - Order-of-magnitude improvement on drifting data; single-pass, bounded memory.

## 23. Split-and-Learn: Decoupled Learning for Reactive Transport in Heterogeneous Marine Sediments

- **arXiv ID:** 2611.23748v1
- **Published:** 2026-11-18
- **Authors:** Maria Vasilyeva, Siu Wun Cheung, Jihoon Kim, Richard B. Coffin, Ingo Pecher
- **Institution/Company:** N/A
- **Categories:** math.NA
- **Link:** https://arxiv.org/abs/2611.23748v1
- **Abstract:** Reactive transport in heterogeneous marine sediments: coupled flow/multicomponent transport with nonlinear chemistry, evolving porosity/permeability — simulation is expensive under uncertainty. Split-and-Learn keeps the sequential operator-splitting scheme, replacing each stage with data-driven surrogates (multiscale reduced maps or Galerkin/least-squares Petrov-Galerkin local atoms). Chemistry: bounded reaction extents with stoichiometric reconstruction. Flow: learned interface traces + reduced mixed multiscale solve enforcing mass balance. Stability proofs; bound on learned solver error by accumulated one-step errors.
- **Key innovations:**
  - Decoupled surrogate learning per sequential stage (transport, chemistry, flow) with stability guarantees.
  - 2D/3D heterogeneous marine sediment benchmarks; accuracy and cost vs. full-order split solver.

---

## Coverage summary

| Topic | Papers |
|---|---|
| AI / LLMs | NarrowSpec, When Do LLMs Model the Right Target, Reliability of LLMs, Plug-and-Play MoE, Localizing Text Anonymization, Thinking Fast Anywhere, Evaluating Governed LLM-Driven ML, Rented Oscillations, Split-and-Learn, Modeling LLM Reasoning Dynamics |
| Recommendation | CONCORD-Rec, Cluster-Guided Decoding, TokenFormer V2, RACE |
| Advertising | UrbanROI, IntentFlow, Bajillion, Media Trading with Censored Auction Prices, Data-Driven Inventory Planning and Advertising |
| Sequential modeling | Incremental Roseland, Split-and-Learn, TokenFormer V2 |
| CTR | IntentFlow (CTR metrics) |
| Games | Learning Martial Arts Motion Skills for VR Sparring Games |
