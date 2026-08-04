---
title: "arXiv Daily Digest — 2026-08-04"
type: synthesis
created: 2026-08-04
updated: 2026-08-04
tags: [arxiv, survey, llm, evaluation, alignment, reasoning, agents, recommendation, user-modeling, rl, bandits, sequential-modeling, diffusion]
---

# arXiv Daily Digest — 2026-08-04

> Curated from the **Mon Aug 3, 2026** arXiv listings (the latest batch available at generation time: cs.AI 43 new, cs.IR 13, cs.LG 82, cs.CL 51). **No overlap** with the [Aug 3 arXiv AI scan](../2026-08-03/arxiv-ai-search.md), the [Aug 3 paper check](../2026-08-03/arxiv-paper-check.md), or the [Jul 31 digest](../2026-07-31/arxiv-daily.md). The batch's flagship recommendation/CTR/ads papers (TransX, SnapLGR, GALA, Think2Go, PaletteID, RecHarness, MerchantBench, GenCDSR) were already covered in the Aug 3 digests; this edition curates the remaining high-signal papers across LLM evaluation & alignment, reasoning efficiency, user modeling, agents, and RL theory. 26 papers curated.

---

## 1. LLM Evaluation & Alignment

### Chain-of-Models: Cross-Model Auditing for Bias-Robust LLM Judges
- **Authors**: Qian Wang, Zhanzhi Lou, Zhenheng Tang, Nuo Chen, Bingsheng He (NUS)
- **Date**: 2026-08-02
- **Link**: [2607.28636](https://arxiv.org/abs/2607.28636)
- **Abstract**: LLM-as-a-judge remains vulnerable to cognitive biases; prompt-debiasing is brittle across bias types and human evaluation doesn't scale. CoM is an automated audit pipeline where a second model inspects the first model's reasoning trace before issuing the final judgment. Across 9 models from 6 families, 4 cognitive biases, and 4 factual datasets, auditor identity matters in two ways: standalone bias resistance does **not** predict audit effectiveness (Kimi-K2.5 is strongest standalone but a weak auditor for Qwen2.5-72B's biased traces), and the best auditor is **bias-specific** (GPT-4o strongest on bandwagon/authority/distraction; GLM-5 strongest on sycophancy). A per-bias auditor-selection rule reaches 0.884 accuracy on biased slices vs 0.824 for the best fixed auditor and 0.805 for no audit.
- **Key Innovation**: Operationalizes a per-bias *auditor selection* rule (functional diversity + per-bias standalone resistance + calibrated audit effectiveness) — the first evidence that judge debiasing should be a routed, cross-model pipeline rather than a single prompt fix.

### The Formalism Trap: Are LLM-as-a-Judge Evaluators Blinded by Consensus Mimicry under Social Load?
- **Authors**: Dahlia Shehata, Ming Li
- **Date**: 2026-08-02
- **Link**: [2607.28641](https://arxiv.org/abs/2607.28641)
- **Abstract**: Introduces the *Agentic Formalism Trap* and the Evaluative Dissonance Index ($D_E$), quantifying how LLM-as-a-Judge systems conflate structural proceduralism with semantic truth under adversarial load. Analyzing 22,500 trajectories across GAIA, SWE-bench, and Multi-Challenge, the authors extract a semantic taxonomy of hallucination maneuvers (validated via deterministic lexical grounding, $p<10^{-120}$), isolate the exact syntactic triggers of evaluator capture (ROC-AUC 0.8779), and show the vulnerability is domain-agnostic via zero-shot Leave-One-Domain-Out transfer (mean ROC-AUC 0.7482). Distinct simulated swarm topologies induce mathematically disparate semantic blind spots.
- **Key Innovation**: Shows closed-loop agent evaluation is *structurally* capturable — a formal metric ($D_E$) plus a taxonomy linking syntactic triggers to hallucination, arguing for architecture-specific vigilance filters in agentic eval.

### CalibratedRubric: Task-Adaptive Rubric Banks for Open-Ended LLM Evaluation
- **Authors**: Mengting Chen, Yanshu Sun, Wanting Liang, Beidi Luan, Rui Sun, Dezhi Chen, Jing Li, Zuo Bai
- **Date**: 2026-08-02
- **Link**: [2607.29252](https://arxiv.org/abs/2607.29252)
- **Abstract**: Expert rubric curation is costly and automated pipelines rely on strict judge unanimity + binary variance filters, which can't separate measurable rubrics from informative ones. CalibratedRubric combines type-specific scoring, Bayesian rubric-measurability filtering (Beta–Bernoulli agreement posterior), and item-response-theory (IRT) bank assembly with a submodular information-coverage objective. Measurability filtering improves human-gold agreement on JudgmentBench from κ=0.604→0.743; IRT greedy selection needs only 49 rubrics instead of 131 to hit target correlation on FinResearchBench.
- **Key Innovation**: Replaces unanimity/binary-variance rubric filtering with an uncertainty-aware Beta–Bernoulli measurability posterior + IRT-based compact bank assembly — calibration depends on judge redundancy.

### Know It, Act on It: Investigating Memory Utilization in LLM Personalization
- **Authors**: Zhaoxin Feng, Jianfei Ma, Emmanuele Chersoni (Hong Kong Polytechnic University)
- **Date**: 2026-08-02
- **Link**: [2607.29433](https://arxiv.org/abs/2607.29433)
- **Abstract**: LLM agents may fail to act on relevant user preferences even when the preference is fully present in context. The authors introduce a decoupled evaluation paradigm administering paired *Know* (recall) and *Act* (behavioral application) tests to the same preference. Across 16 systems, 5 memory architectures, and 1,000 preferences at 3 expression-strength levels, there is a large Know–Act gap: agents often pass recall but fail to apply the preference in the paired behavioral scenario. Memory architectures narrow the gap, but utilization stays weakest for health/therapy preferences — where failures to act carry the highest stakes.
- **Key Innovation**: A decoupled Know/Act benchmark that separates *storage/retrieval* failure from *utilization* failure in LLM personalization — a measurement discipline that applies directly to memory-based recommenders and companion agents.

### Language Models Agree With Each Other, Not With Readers
- **Authors**: Kazuki Nakayashiki, Keisuke Watanabe
- **Date**: 2026-08-02
- **Link**: [2607.29274](https://arxiv.org/abs/2607.29274)
- **Abstract**: Claims that LLMs homogenize are usually measured against human judgments collected for the study — a crowdworker given the model's instruction is "running the model's prompt." This paper measures convergence against a human reference nobody built for the purpose: 2,523 reader mark sets across 120 web documents, produced by people highlighting for their own reasons. Agreement is overlap between two size-matched sentence sets minus expected overlap (null calibrated within 0.006 of zero). Median document: readers share 4.1 sentences, models 8.7; median of 153 model pairs is +0.093 vs a human yardstick of +0.040, with 99 model pairs above the human interval. Two frontier models reach +0.203 — twice what GPT-4o agrees with itself on a second call. The effect is not determinism/prompting/vendor/routing and is graded: smallest models agree at the human level. None of four out-of-sample models clears the human interval.
- **Key Innovation**: The cleanest methodological correction yet to the "model homogenization" literature — an organic human reference (nobody optimized for agreement) that shows model-model convergence is real and large, while model-human agreement is indistinguishable from human-human.

### TokenSwap: Benchmarking and Reducing the Modality Gap in Multimodal LLMs
- **Authors**: Andong Hua, Colton Bishop, Igor Mordatch, Arian Hosseini, Jindong Gu, Aleksandra Faust, Rebecca Roelofs, Yao Qin
- **Date**: 2026-08-02
- **Link**: [2607.28640](https://arxiv.org/abs/2607.28640)
- **Abstract**: MLLMs should respond consistently to semantically equivalent inputs across modalities, but exhibit a systematic "modality gap." TokenSwap constructs such inputs by replacing textual concepts with semantically aligned images (interleaved visual+text tokens), turning text benchmarks like MMLU into image-interleaved TokenSwap-Bench. Across 42 MLLMs, performance drops 4.2%–47.4% when moving to image-interleaved inputs (avg 19.6%). Reasoning models show smaller gaps (10.1% vs 25.5% for non-reasoning). Neither prompting nor scaling compute alone reliably reduces the gap, but training with TokenSwap mitigates it while preserving text-only and vision-language performance.
- **Key Innovation**: A cheap, controllable cross-modal equivalence probe (TokenSwap) + a training-time intervention that reduces the modality gap — quantifies a systematic consistency failure across 42 models.

---

## 2. LLM Reasoning & Efficiency

### BLADE: Boundary-Expanded and Layer-Adaptive Dynamic Exit for Efficient LLM Reasoning
- **Authors**: Keshu Fu, Keqin Peng, Jun Bai, Shuhan Qin, Chen Li, Junzhu Liang, Yefei Chen, Jiaqi Li, Yuanxin Ouyang
- **Date**: 2026-08-02
- **Link**: [2607.28966](https://arxiv.org/abs/2607.28966)
- **Abstract**: Long reasoning traces waste compute on redundant verification/revision. Existing probe-based early-exit methods only inspect explicit self-doubt expressions; BLADE expands inspection to ordinary reasoning boundaries (sentence, self-doubt, paragraph) and learns a compact subset of informative probe layers rather than fixed choices. Calibrated predictions combine with checkpoint-specific confirmation rules to balance responsiveness vs premature-exit risk. On Qwen3-8B it preserves near-baseline accuracy while cutting generated tokens 24.8% (Qwen3-4B: 15.8%).
- **Key Innovation**: Boundary-expanded multi-granular checkpoints + *learned* layer selection for dynamic exit — addresses the "where to probe" problem, not just "when to stop."

### Demystifying Entropy-based Selection for Chain-of-Thought Compression in Large Reasoning Models
- **Authors**: Sara Candussio, Daniel Scalena, Luca Bortolussi, Elisabetta Fersini, Malvina Nissim, Gabriele Sarti
- **Date**: 2026-08-02
- **Link**: [2607.28707](https://arxiv.org/abs/2607.28707)
- **Abstract**: Entropy-based CoT step pruning is claimed to compress reasoning with negligible loss. This paper shows low/high-entropy *sentence* selection offers no advantage over random pruning in any setting; low-entropy *token* retention only appears effective on math benchmarks — because numeric tokens are inherently low-entropy yet semantically loaded. Patching a subset of CoT tokens with their original activations recovers near-perfect performance, causal evidence that task information is *distributed across the full chain*, not concentrated in heuristic-identifiable tokens.
- **Key Innovation**: A rigorous negative result that deflates entropy-based CoT compression claims (mirroring the reflection/re-generation negative result from Aug 3), plus a causal-activation-patching diagnostic.

### LARA: Lightweight Adapters in the Residual Stream for Composable Adaptation and Alignment
- **Authors**: Pascal Ekin, Hyosun Choi, Wei Jie
- **Date**: 2026-08-02
- **Link**: [2607.28669](https://arxiv.org/abs/2607.28669)
- **Abstract**: LARA (Lightweight Additive Residual Adaptation) adapts a frozen model by reading the hidden state at a small set of layers and adding a low-rank correction back to the *residual stream*, leaving all base weights untouched — unlike LoRA's weight-matrix updates. It matches LoRA at equal parameter counts on code fine-tuning and DPO. Because adaptation is frozen-base + residual, LARA exposes a scale γ applied at inference that interpolates between base and adapted behavior (graded control weight-space adaptation can't offer), and multiple behaviors can be held resident and routed per-token: seven behaviors on one frozen 1.5B model for ~33 MB overhead.
- **Key Innovation**: Adaptation as residual-stream additive modules enables per-token *composable* behavior routing and inference-time continuous control — a post-training alternative to weight-space PEFT.

### Hierarchical Copula-Gumbel-Top-K Routing: Two-Sided Dependence Control for Frozen Mixture-of-Experts at Fixed Per-Token Routing Laws
- **Authors**: Richard Yi Da Xu
- **Date**: 2026-08-02
- **Link**: [2607.28670](https://arxiv.org/abs/2607.28670)
- **Abstract**: A stochastic Gumbel-Top-K router defines a *routing law* (distribution over ordered expert lists and mixture weights) per token. This paper characterizes which *joint* distributions over tokens' routing choices are reachable while every token's marginal routing law stays fixed. The construction, CGA, uses an exchangeable Gaussian copula to positively correlate Gumbel perturbations within a group (raising expert-set coherence) and a tunable antithetic construction to add negative dependence across groups. Both operations provably preserve each token's marginal routing law and conditional expected expert traffic. Positive within-group coupling inflates realized load variance; nonnegative cross-group opposition reduces it — two complementary "dependence dials." Because the base model is untouched, the dials are driven by a small controller trained with a score-function estimator (frozen network forward-only).
- **Key Innovation**: A formal dependence-control framework for MoE routing at fixed marginal laws — coherent expert grouping + load-dispersion control without retraining the frozen MoE, trainable purely via a small controller.

### PTP: Previous-Token Prediction based LLM Inversion for Near-Exact Prompt Reconstruction
- **Authors**: Pirzada Suhail, Nagasai Saketh Naidu, Atanu R. Sinha, Amit Sethi
- **Date**: 2026-08-02
- **Link**: [2607.29378](https://arxiv.org/abs/2607.29378)
- **Abstract**: Prompt recovery from LLM outputs is normally framed as *semantic* reconstruction, requiring fine-tuned seq2seq models, model weights, or logits. PTP instead trains an explicit inverse language model **from scratch on synthetic data generated by the target LLM itself**, using *previous-token prediction* (the dual of next-token prediction) — establishing a generative link between forward and inverse processes that enables faithful reconstruction. It supports diverse prompt reconstruction via sampling (all candidate prompts induce similar target-LLM responses), generalizes across datasets, and transfers to reconstructing prompts from different LLMs. Outperforms prior work on token-based reconstruction metrics.
- **Key Innovation**: Black-box, weight-free LLM inversion via previous-token prediction — the inverse process mirrors the forward autoregressive process, making it model-agnostic and training-data-free.

---

## 3. Recommendation, Search & User Modeling

### MMShopBench: A Real-Log Benchmark for Multimodal, Multi-Turn Shopping Agents
- **Authors**: Zeying Hao, Hao Guo, Mengtao Xu, Yimin Hu, Yuheng Song, Zesheng Zhou, Jinsong Lan, Xiaoyong Zhu
- **Date**: 2026-08-02
- **Link**: [2607.29002](https://arxiv.org/abs/2607.29002)
- **Abstract**: Shopping agents increasingly must infer purchase intent and mandatory product requirements jointly from user images and multi-turn dialogue. Existing benchmarks are mostly text-only or synthetic. MMShopBench is the first *real-log* benchmark for multimodal, multi-turn shopping agents, built from cleaned and manually annotated shopping logs with ground-truth purchase-intent and mandatory-requirement annotations. Agents must retrieve candidates through image+text search and verify each against product images and structured attributes via an evidence-grounded multimodal protocol. An offline shopping sandbox enables reproducible evaluation; fine-tuning an open-source model on the companion training set substantially narrows the gap to leading proprietary models.
- **Key Innovation**: Real-world, evidence-grounded multimodal shopping-agent benchmark with a reproducible offline sandbox and an open fine-tuning recipe — directly relevant to e-commerce agentic search and advertising ecosystems.

### SERUM: State Extraction and Refinement for User Modeling
- **Authors**: Andy J. Phu, James Mooney, Karin de Langis, Khanh Chi Le, Dongyeop Kang
- **Date**: 2026-08-02
- **Link**: [2607.29181](https://arxiv.org/abs/2607.29181)
- **Abstract**: Proactive, personalized assistants need structured models of user intent and workflow, but building them from raw screen activity is open. SERUM extracts finite-state behavioral models directly from unstructured egocentric screen video using hierarchical VLM annotation: a sliding window alternates activity-recognition and intent-inference passes, each refining labels with accumulated context (reducing hallucination/temporal conflation), then merges synonymous states via sentence embeddings. Across 61 egocentric videos in 4 domains, iterative refinement converges to a stable state vocabulary ("schematic equilibrium"); normalized Markov models beat frequency baselines on action prediction, with largest gains on structured tasks like coding.
- **Key Innovation**: First system to produce interpretable process (state-machine) models of user behavior from raw screen video with zero manual annotation — a scalable pathway for user modeling in the wild.

### MBDiff: Multi-view Behavior-aware Diffusion Model for Probabilistic Utility Data Imputation
- **Authors**: Rongchao Xu, Lin Jiang, Dahai Yu, Ximiao Li, Guang Wang
- **Date**: 2026-08-02
- **Link**: [2607.29177](https://arxiv.org/abs/2607.29177)
- **Abstract**: Sensor/device failures leave large gaps in utility consumption data (electricity/water/gas), hurting billing and forecasting. Most prior work trains on aggregated data and ignores rich user-behavior signal. MBDiff uses (i) a multi-view User Behavior Extraction module (global/local/instance-level views) and (ii) a behavior-aware conditional diffusion model with a reference-selection module and conditional attentional denoising. With a major Florida utility provider, it improves block-missingness imputation by 7.04% (electricity) and 29.1% (water) over SOTA.
- **Key Innovation**: Behavior-conditioned probabilistic imputation — diffusion conditioned on multi-view user behavior for missing time-series, evaluated in production-scale deployment.

---

## 4. Agents & Multi-Agent Systems

### Autonomous Repair for Multi-Agent Systems via Monte-Carlo Tree Search (MARS)
- **Authors**: Hanxiao Lu, Tianyi Zhang (Purdue)
- **Date**: 2026-08-02
- **Link**: [2607.29055](https://arxiv.org/abs/2607.29055)
- **Abstract**: When multi-agent systems produce wrong outputs, users must manually attribute failures and repair outputs. MARS formulates MAS repair as an MCTS search over repairs, with diagnosis-guided expansion and taxonomy-augmented evaluation; it evaluates via *partial* rollouts to cut token consumption. Introduces StateMAS, a large MAS-repair benchmark of 1,310 replayable multi-agent failure trajectories across 4 agent architectures and 4 LLM backbones. MARS improves over SOTA by 3.0–12.1% absolute across settings at comparable token cost.
- **Key Innovation**: First search-based automated repair for multi-agent systems (diagnosis-guided MCTS + partial-rollout evaluation) plus a large replayable failure-trajectory benchmark.

### Harnessing the Wisdom of LLM Crowds through Complementarity-Driven Iterative Collaboration (WILC)
- **Authors**: Yanbin Fang, Xuan Wei, Wei Chen
- **Date**: 2026-08-02
- **Link**: [2607.29087](https://arxiv.org/abs/2607.29087)
- **Abstract**: Individual LLMs have model-specific capability boundaries; static ensembles fix model combination in advance. WILC treats collective LLM intelligence as *relay-style complementarity*: each successor is selected to address the specific bottleneck identified in the predecessor's output. A dual-gate mechanism governs transitions — prospective complementarity fit (PCF) picks the worker best suited to the current bottleneck, and posterior complementarity gain (PCG) verifies the transition improved the solution. Across 4 benchmarks, WILC matches the average performance of GPT-5.2 at roughly **7× lower estimated per-query cost**, with self-hosted deployment preserving data sovereignty.
- **Key Innovation**: Sequential, bottleneck-driven model routing (PCF/PCG dual gate) that outperforms fixed ensembles and self-refinement at a fraction of frontier-API cost.

### CAGE: Certified Authorization under Typed-Return Uncertainty for Tool-Using Agents
- **Authors**: Blaise Delattre, Cong Wang, Yang Cao
- **Date**: 2026-08-02
- **Link**: [2607.29190](https://arxiv.org/abs/2607.29190)
- **Abstract**: Runtime permission gates authorize an observed tool return and action, but leave the decision unprotected against small binding/drift errors. CAGE asks whether a candidate action stays authorized over a declared neighborhood of plausible correctly-bound returns (one admissible binding fault + bounded numerical drift). A key result: certifying the categorical and numerical channels *separately does not compose* — perturbations safe on each channel alone can jointly make an action unsafe. CAGE certifies the joint neighborhood directly (exact discrete enumeration + continuous certification per branch). Across synthetic, policy-as-code, regulatory, and real-transaction settings it removes in-budget false allows while keeping a useful fraction of decisions autonomous.
- **Key Innovation**: The first *joint* certified authorization for tool-use under typed-return uncertainty, with a non-compositionality proof that refutes naive channel-wise safety gating.

### Tool Specifications Matter: Uncovering and Mitigating Safety Risks in AI Agents (SafeKeep)
- **Authors**: Minghui Pan, Jiayuxuan Yang, Yuanyuan Yuan, Yu Jiang, Zhenpeng Chen
- **Date**: 2026-08-02
- **Link**: [2607.29254](https://arxiv.org/abs/2607.29254)
- **Abstract**: LLMs become substantially less safe when deployed as agents; this paper identifies **schema-formatted tool specifications** as a primary source of degradation, showing via white-box representation analysis that they weaken the model's internal refusal signals. SafeKeep, an inference-time safeguard, decouples safety judgment from tool execution: it assesses requests using *flattened textual* tool specs while retaining schema-formatted specs for execution. Across 2 benchmarks and 4 LLMs (white- and black-box), SafeKeep raises refusal for harmful requests from 23.8%→70.6% and cuts prompt-injection attack success from 25.6%→2.5%, while preserving task-handling.
- **Key Innovation**: A mechanistic explanation (schema specs erode refusal representations) plus a minimal inference-time fix that re-couples safety to readable specs without changing execution.

### Beyond Component Testing: Validating Agentic AI Systems
- **Authors**: Fabio Orazio Mirto, Luca D'Agati, Giuseppe Tricomi, Stefano Silvestri, Francesco Longo, Antonio Puliafito, Giovanni Merlino
- **Date**: 2026-08-02
- **Link**: [2607.29405](https://arxiv.org/abs/2607.29405)
- **Abstract**: A survey synthesizing 257 papers across agent evaluation, software assurance, cyber-physical systems, runtime monitoring, and regulatory guidance. Organized around a five-dimension taxonomy (behavioral, safety, temporal, regulatory, multi-agent), it maps current approaches and exposes coverage gaps: behavioral evaluation is mature, while temporal validity, runtime-evidence maintenance, regulatory legibility, and open-ended multi-agent assurance remain under-developed. Three cross-domain case studies (medical care, industrial operations, smart mobility) ground the taxonomy; concludes with a lifecycle research agenda (bounded-autonomy specs, adversarial trajectory generation, runtime monitoring, audit-ready evidence).
- **Key Innovation**: A consolidated, cross-discipline validation taxonomy for agentic systems and an explicit gap analysis — argues trustworthy deployment requires validating *trajectories in context*, not isolated components.

### Beyond Retrieval: Analytic Memory for Multimodal Agents (AdaMM)
- **Authors**: Zhoujin Tian, Yao Tian, Hao Zhang, Cheng Chen, Yakun Li, Lei Zhang, Xiaofang Zhou
- **Date**: 2026-08-02
- **Link**: [2607.29440](https://arxiv.org/abs/2607.29440)
- **Abstract**: Long-term multimodal memory must not only retrieve but also *compute over* accumulated observations. Existing systems emphasize retrieval memory (summaries + indexes). AdaMM formalizes *analytic memory*: organizing recurring multimodal observations into queryable structures supporting filtering, aggregation, ranking, and temporal comparison. It extracts provenance-linked attribute-value observations from dialogue, images, and metadata, discovers recurring field structures, and materializes them; a memory-aware planner decomposes queries into retrieval vs analytic operations and routes to the right tools. On MemEye and MemGallery, AdaMM improves performance by up to 11.3% and 7.3%.
- **Key Innovation**: A complementary "analytic memory" abstraction — treating memory as a queryable database over accumulated multimodal evidence rather than a retrieval store.

---

## 5. Reinforcement Learning & Bandits

### Gated Q-learning: Add Off-Policy Bias to Taste
- **Authors**: Brett Daley (Dartmouth)
- **Date**: 2026-08-02
- **Link**: [2607.28916](https://arxiv.org/abs/2607.28916)
- **Abstract**: For 30 years Q(λ) forced a binary choice: Watkins (eliminate off-policy bias, truncated traces) vs Peng (learn faster, inject error). Modern importance-sampling estimators collapse under Q-learning's greedy target policy. Gated Q-learning replaces IS with a continuous, state-action-dependent *gating* mechanism that selectively attenuates eligibility traces in an exploration-aware manner. The expected operator is proved to be a contraction with an exact fixed point; intermediate gating safely enables longer credit-assignment horizons, yielding faster initial learning than either extreme.
- **Key Innovation**: A simple, theoretically grounded interpolation between Watkins and Peng Q(λ) — continuous control of the effective multistep horizon and off-policy bias without importance sampling.

### Parameter-Free Heavy-Tailed Bandits
- **Authors**: Gianmarco Genalti, Alberto Maria Metelli (Politecnico di Milano)
- **Date**: 2026-08-02
- **Link**: [2607.29460](https://arxiv.org/abs/2607.29460)
- **Abstract**: Heavy-tailed rewards (financial investment, online advertising, network management) are usually modeled with unknown tail exponent ε and moment bound u — exactly the quantities hardest to infer from limited data. Resolving an open problem posed at COLT 2025, this paper proves every algorithm unaware of u must obey a sharp trade-off between distribution-dependent and distribution-free regret; gives a scheduled-exploration algorithm matching the adaptation frontier up to log factors; and shows the same algorithm adapts without ε by calibrating to ε=1 — sublinear regret for every fixed ε>0, while no algorithm achieves uniform sublinear regret over all ε∈(0,1].
- **Key Innovation**: Sharp, assumption-free characterization of the regret cost of unknown heavy-tail parameters, with an algorithm that attains the frontier — directly relevant to ads/bidding regret bounds.

### Convergence and Regret of the Policy Gradient for Multi-Armed Bandits in Diffusion Environments
- **Authors**: Yanwei Jia, Du Ouyang
- **Date**: 2026-08-02
- **Link**: [2607.29593](https://arxiv.org/abs/2607.29593)
- **Abstract**: Studies policy-gradient updates for MABs in a diffusion (SDE) environment under the continuous-time RL framework. With logit parameterization, the policy converges almost surely to the optimal arm under arbitrary constant learning rate, and the non-asymptotic regret is O(log T) below a time-invariant threshold — improving the analysis in Lattimore (2026a) for the same SDE via a novel Lyapunov function, which also helps analyze discrete-time policy gradient.
- **Key Innovation**: A clean convergence + O(log T) regret proof for continuous-time policy gradient in stochastic environments, with a reusable Lyapunov tool.

### LEMUR: Learning to Align with Multi-Objective RL from Preference Feedback
- **Authors**: Manith Adikari, Bei Peng, Samuele Vinanzi, Angelo Cangelosi
- **Date**: 2026-08-02
- **Link**: [2607.29559](https://arxiv.org/abs/2607.29559)
- **Abstract**: Real-world decision tasks involve competing objectives (performance vs efficiency) where reward functions are hard to specify. MORL assumes per-objective reward functions; PbRL learns rewards from feedback but mostly in single-objective settings. LEMUR bridges the gap: an agent interactively learns from preferences of multiple humans to jointly learn policies *and* multiple objective-specific reward models, enabling balance of competing objectives during learning. Beats baseline methods across multi-objective benchmarks.
- **Key Innovation**: Preference-based multi-objective RL with per-objective learned reward models and multi-human preference input — no pre-specified reward functions needed.

---

## 6. Sequential Modeling & Generative Efficiency

### Transcript-Managed Transformers: Monotone Multi-Agent Collapse and Universality with Two Pop-Enabled Transcripts
- **Authors**: Sergey Salishev
- **Date**: 2026-08-02
- **Link**: [2607.29496](https://arxiv.org/abs/2607.29496)
- **Abstract**: A formal study of transcript management for fixed, finite-precision causal Transformers. Transcripts are partitioned into channels of bounded blocks; a `PopContext` operation deletes the newest block on a channel and exposes its predecessor. The pop-free (append-only) Restricted Transcript-Managed Transducer realizes exactly the deterministic finite-state transductions for every fixed k and monotone multi-agent protocols. Admitting pop restores a stack: k=1 gives DCFL, k≥2 gives RE (recursively enumerable) via the Hopcroft–Ullman hierarchy — so **two pop-enabled transcripts (in one agent or two) suffice for universality**. State/alpha/cost bounds and invariance results are stated.
- **Key Innovation**: A precise computational-hierarchy characterization of transformer "memory management" (append-only vs pop): pop-restored stacks jump from finite-state to full Turing universality, a formal lens on context compaction/forgetting mechanisms in sequence models.

### OnlineCache: Learning Dynamic Caching Policies with Error Correction for Efficient Diffusion Inference
- **Authors**: Zhikang Xie, Xichen Ye, Yifan Wu, Haoshen Yu, Li Chenan, Peizhu Gong, Weizhong Zhang, Cheng Jin
- **Date**: 2026-08-02
- **Link**: [2607.29398](https://arxiv.org/abs/2607.29398)
- **Abstract**: Cache-based diffusion acceleration relies on static, sample-agnostic schedules, ignoring that generation difficulty varies across prompts and error sensitivity fluctuates across timesteps. OnlineCache jointly learns *when to cache* (a lightweight policy-gradient network for adaptive speed-quality trade-offs) and *how to correct* caching-induced errors (a learnable corrector), both optimized under a bilevel framework. On FLUX.1-dev it achieves nearly 3× speedup with preserved fidelity; competitive acceleration on DiT and CogVideoX, outperforming cache-based baselines across the board.
- **Key Innovation**: Sample- and timestep-adaptive caching with a jointly trained error corrector — treats diffusion caching as a learned allocation problem rather than a fixed schedule.

---

## 7. Cross-Cutting Trends

| Trend | Description | Representative Papers |
|-------|-------------|----------------------|
| **Judge evaluation is being formalized** | LLM-as-judge reliability moves from prompt tricks to measurable pipelines: cross-model auditing, evaluative-dissonance indices, IRT rubric banks | Chain-of-Models, Formalism Trap, CalibratedRubric |
| **Negative results accumulate for cheap inference tricks** | Entropy-based CoT compression has no advantage over random (day 2 after "Reflection or Re-Generation"); task info is distributed across the chain | CoT entropy, (recall) Reflection-or-Re-Generation |
| **Adaptation moves out of the weights** | Residual-stream adapters (LARA), frozen-MoE routing laws (CGA), and composable per-token behavior routing | LARA, Copula-Gumbel-Top-K |
| **Agent memory splits into storage vs use vs analysis** | Know/Act decoupling for personalization, analytic memory (compute-over-memory), zero-token memory (from Aug 3) | Know-It-Act-On-It, AdaMM, (recall) Zero-Mem |
| **Agent safety becomes mechanistic** | Tool-schema specs erode refusal representations (SafeKeep); certified joint authorization (CAGE); MCTS-based autonomous repair | SafeKeep, CAGE, MARS |
| **Multi-LLM orchestration is "relay-style"** | Sequential bottleneck-driven model routing beats static ensembles and self-refinement at ~7× lower cost | WILC |
| **RL theory keeps tightening heavy-tailed/off-policy bounds** | Parameter-free heavy-tailed bandits (COLT '25 open problem), continuous-time PG regret, gated Q(λ) interpolation | Heavy-Tailed Bandits, PG-MAB-Diffusion, Gated Q-learning |

---

## Key Takeaways

1. **The judge problem is now an engineering problem**: Chain-of-Models shows bias resistance is *per-bias* and auditor identity matters (route the auditor per bias type); Formalism Trap and CalibratedRubric provide quantitative instruments (dissonance index, measurability posterior) to measure and fix evaluator capture.
2. **A clean methodological correction to "model homogenization"**: "Language Models Agree With Each Other, Not With Readers" uses an organic human reference and finds frontier models agree with each other ~2.3× more than with the human baseline — a result independent of prompt/design artifacts.
3. **Reasoning-efficiency claims keep getting stress-tested**: BLADE (learned-layer dynamic exit, -24.8% tokens) advances the positive direction, while the entropy-based CoT compression study lands a negative result — task information is distributed, not concentrated in low-entropy tokens.
4. **The personalization frontier is utilization, not recall**: Know-It-Act-On-It decouples memory storage from application and finds agents systematically fail to *act* on remembered preferences (worst for health/therapy) — a directly actionable eval design for memory-based recommenders.
5. **Adaptation and routing are decoupling from training**: LARA (residual-stream behavior modules, 33 MB for 7 behaviors) and the copula-MoE routing-law controller (frozen base, score-function-trained dials) both push post-training customization toward per-token, on-device control.
6. **Agent safety is getting mechanistic and certified**: SafeKeep links unsafe tool execution to schema-formatting (a representation-level explanation), CAGE certifies authorization under binding uncertainty, and MARS automates repair — safety moves from prompting to provable properties.
7. **Sequential modeling gains a formal memory hierarchy**: Transcript-Managed Transformers proves append-only transcript management caps at finite-state, while two pop-enabled transcripts reach Turing-universality — a clean computational lens on context/forgetting designs.

> ⚠️ Note on sourcing: All papers verified against arXiv (Mon Aug 3, 2026 batch, IDs 2607.28636–2607.29678). This digest intentionally excludes the batch's flagship recommendation/CTR/ads papers already covered in the [Aug 3 digests](../2026-08-03/); see those for TransX, SnapLGR, GALA, Think2Go, PaletteID, EvoReason, RecHarness, GenCDSR, MerchantBench.
