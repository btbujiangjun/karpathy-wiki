---
title: "arXiv Paper Check — AI & CTR (November 7, 2026)"
type: synthesis
created: 2026-11-07
updated: 2026-11-07
sources: []
tags: [arxiv, daily-check, ai, ctr, recommendation, ads, generative-recommendation, ranking, retrieval, llm, agents, rl, on-policy-distillation, sparse-attention, sae, interpretability, efficiency]
---

# arXiv Paper Check — AI & CTR (November 7, 2026)

*Report generated: 2026-11-07 | Window: latest arXiv announcement batch (Fri 2026-11-06). No weekend announcement block.*

## Summary

- Swept `cs.IR`, `cs.AI`, `cs.LG`, `cs.CL` RSS: **826 unique items**, of which **461 are unique `new`/`cross` papers**. **21** touch `cs.IR` (12 are `new`-only). `replace`/`replace-cross` excluded.
- The CTR/Rec cluster is small but production-heavy: two online A/B wins (BRIDGE on e-commerce ads, ICE on Taobao), task-aware semantic tokenization, and a clear diagnosis of **exposure collapse from collaborative-filtering rewards** in LLM recommenders.
- The AI cluster is dominated by **on-policy distillation (OPD)** — four papers in this single batch analyze, gate, couple, and cost-account it — plus long-context sparse attention, looped residual architectures, and SAE-based interpretability.
- Interpretability is moving from features to **structure**: SAE scaling laws for activation buffers, and SAE decomposition showing MoE experts specialize below domain granularity.
- Abstract-only screening. All featured IDs were grep-verified as absent from the wiki. Numbers are author-reported and not independently reproduced.

## CTR / Ranking / Ads

### 1) [BRIDGE: Bridging the Semantic Quantization Gap for Generative Recommendation](https://arxiv.org/abs/2611.07425)
- **Authors:** Yatong Xiao, Mingjie Sun, Peng Wang, Wenjin Wu, Peng Jiang
- **Categories:** cs.IR
- **Summary:** Identifies the **Semantic Quantization Gap (SQG)** in RQ-VAE generative recommendation: the decoder receives only discrete SIDs while quantization derived them from rich continuous signals (codebook centroids, neighborhood geometry, level-wise entropy).
- **Key Contributions:**
  - Codebook-grounded latent reasoning injects frozen quantizer centroids as semantic anchors before SID generation.
  - Privileged EMA self-distillation transfers neighborhood-aware geometry to an on-policy student, mitigating exposure bias.
  - Effort-aware recurrence allocates more compute to harder early SID levels.
  - Three Amazon benchmarks: **+10.9% Recall@10 / +9.7% NDCG@10** average; one-week online A/B on a large e-commerce ads platform (5% traffic): **+0.65% eCPM**.

### 2) [Beyond Independent Predictions: Learning the Browsing Journey for Sequence-Level Re-ranking](https://arxiv.org/abs/2611.07591)
- **Authors:** Jiayi Zhang, Jingxin Hai, Zhenjia Ma, Hongbin Pei, Dagui Chen, Han Zhu, Jian Xu
- **Categories:** cs.IR
- **Summary:** Industrial Generator–Evaluator re-rankers score candidates with independent per-item CTR, ignoring that a click requires the item to be **displayed → impressed → clicked** and that items compete for finite attention.
- **Key Contributions:**
  - **Joint Behavior Modeling (JBM)** replaces independent behavior modeling with an explicit display → impression → click process.
  - **Impression-Click Evaluator (ICE)** predicts a browsing-depth distribution, suppresses context from unexposed items, and adds a click-distribution matching objective.
  - Plug-and-play across backbones; 14-day Taobao A/B: **+0.70% clicks, +3.67% revenue**, then full-traffic deployment.

### 3) [OptST: Optimizing Semantic Tokenization for LLM-Enhanced Recommendation](https://arxiv.org/abs/2611.07523)
- **Authors:** Hanchong Chen, Jie Liu, Fuyuan Lyu, Dugang Liu, Lingjie Li, Xiuqiang He, Xing Tang
- **Categories:** cs.IR
- **Summary:** In the standard two-stage pipeline, an LLM-derived profile tokenizer is frozen before the recommender, so downstream supervision cannot revise the semantic partition it produced.
- **Key Contributions:**
  - Learns a **low-rank deformation** of codebook assignments with an anchor regularizer, keeping the pretrained encoder and base codebooks fixed.
  - Straight-through estimator carries recommendation supervision into hard nearest-code assignment.
  - Interaction-conditioned prefix selects how much residual semantic detail is exposed per sample.
  - Highest AUC on four public datasets across conventional and LLM-enhanced baselines, robust to recommender backbone.

### 4) [What Gets Hacked in a Collaborative Reward for LLM Recommenders: The Part That Does Not Depend on the User](https://arxiv.org/abs/2611.07588)
- **Authors:** Zhuangsheng Li, Liang Dong, Yu Wu, Dailin Li, Yu Xia, Yunhan C. Zhang, Rui Cai, Yi Wu, Julian McAuley
- **Categories:** cs.IR
- **Summary:** CF scores used as RL rewards cause **exposure collapse**: the CF model's own top lists are diverse, but an LLM optimized on its rewards concentrates on fewer items.
- **Key Contributions:**
  - Decomposes each CF score into an **item-mean** component and a user-specific residual; controlled interventions identify the item-mean as the collapse driver.
  - Per-item centering and per-item standardization correct the reward.
  - Up to **9.8× more distinct items ranked first** across users with comparable ranking accuracy, on two datasets and two identifier schemes.

### 5) [User Embeddings are Superpositions of Interpretable Behavioral Modes](https://arxiv.org/abs/2611.08487)
- **Authors:** Jonathan Kozaczuk, Zheng Dong, Noyan Evirgen, Keivan Majidi, Eddie K. H. Ng, Chris Porter, Qi Zhao, Jia Geng, Changmao Li, Brandon R. Feng
- **Categories:** cs.LG
- **Summary:** Dense user embeddings are opaque; the paper argues they are sparse superpositions of interpretable behavioral modes, recoverable post hoc with sparse dictionary learning.
- **Key Contributions:**
  - Trains SAEs on user embeddings (classical and transformer-based); validates mode recovery against ground truth on synthetic data.
  - Recovers modes on two real-world datasets and auto-names them in natural language.
  - Natural-language labels enable **zero-shot audience retrieval** over embeddings never trained on text.
  - Model-agnostic and post hoc — no change to the upstream embedding system.

### 6) [GINGER: Spicing Up Graph-Based Vector Search](https://arxiv.org/abs/2611.08306)
- **Authors:** Daniel Salwasser, Lars Gottesbüren, Laxman Dhulipala, Jakub Łącki, Guy Blelloch, Rajesh Jayaram, Tobias Rubel, Kshiteej Sheth, Amir Zandieh, Vahab Mirrokni
- **Categories:** cs.DC, cs.IR
- **Summary:** A production C++ approximate-nearest-neighbor library from Google targeting throughput and memory on large, high-dimensional embedding corpora.
- **Key Contributions:**
  - **Nested TurboQuant (NTQ)**: two-level quantization enabling low-precision graph navigation and high-precision reranking in one code; near-FP precision at **2.6× less memory**.
  - Up to **2.5× graph compression** without throughput loss via graph reordering + the lossless AdaptiveGap codec.
  - At 95% recall: **1.8× average** throughput over each dataset's fastest competitor, **≥2.3×** over any single library, **2.9×** over compact libraries on high-dimensional embeddings.

### 7) [Axis-LoRA: Probing and Adapting Embedding Models for Personal-Memory Retrieval](https://arxiv.org/abs/2611.07820)
- **Authors:** Dohoon Kim, Junho Park, Hyunwoong Bae, Seyoon Kim, Taesup Moon
- **Categories:** cs.AI, cs.CL
- **Summary:** Frozen dense embedders barely distinguish memories by time, place, person, and event; a trained projection on top cannot recover the missing signal because each axis lives inside distinct attention heads.
- **Key Contributions:**
  - Four per-axis LoRA branches inside the embedding model, combined by a per-query gate.
  - Trained on a small axis-counterfactual set, updating a small fraction of base parameters.
  - **+1.28 to +1.56 pp** mean R@10 across three embedders and LongMemEval, ATM-Bench, LoCoMo.

### 8) [The Popular Get More Popular: Auditing Brand Bias in Generative Search](https://arxiv.org/abs/2611.07614)
- **Authors:** Giorgio Monaco, Jacopo Lenti, Francesco Pierri
- **Categories:** cs.AI, cs.CY, cs.SI
- **Summary:** Audits generative search/product recommendations for two biases: **brand popularity bias** (preference for market-dominant entities) and **brand familiarity bias** (advantage from parametric memory).
- **Key Contributions:**
  - Across 1,176 top market players, dominant brands in the top quintile are cited **1.4×–2.8×** more often; external web retrieval does not mitigate the effect.
  - Controlled in-context experiments: replacing authentic brand signatures with unfamiliar ones sharply degrades rank, while fact-preserving rewrites yield negligible gains.
  - Documents a "rich-get-richer" dynamic and a **parametric barrier to entry** that standard content optimization cannot overcome.

## AI / Training / Agents

### 9) [Recursive Sparse Attention: Million-Token Length Extrapolation at Logarithmic Cost](https://arxiv.org/abs/2611.07232)
- **Authors:** Ruitian Wang, Xinyu Yang, Minshen Zhang, Hao Zhang
- **Categories:** cs.CL, cs.LG
- **Summary:** Builds a tree over the KV cache so each query selects and reads only `O(log L)` nodes, instead of scoring all preceding blocks (`O(L)`) as most sparse-attention methods do.
- **Key Contributions:**
  - Each node summarizes its subtree with one key and one mean-pooled value; keys are produced by a per-layer pooler distilled from dense attention.
  - Each entry's RoPE position is its index among candidates at its level, keeping relative distances in the training range at any length.
  - Initialized from Qwen3-4B and trained on 0.62B tokens at 32K: best RULER score at every length 131K–2M; **60.5 at 1M vs 40.0** for the best baseline.
  - Optimized kernels beat dense attention from 64K to 2M; at 524K on one H200, **3.2× prefill / 3.8× decode** speedup.

### 10) [Learning Dynamics of On-Policy Distillation](https://arxiv.org/abs/2611.08016)
- **Authors:** Guan Zhe Hong, Sumeet Ramesh Motwani, Liang Chen, Yangchen Pan, Junchi Yu, Jialin Yu, Philip Torr, Yi Ren
- **Categories:** cs.CL, cs.LG
- **Summary:** Mechanistic analysis of OPD's feedback loop, split into (i) conversion of the distillation signal into parameter updates and (ii) broadcast of those updates across prefixes, which reshapes the rollout distribution.
- **Key Contributions:**
  - Explains both **limited student responsiveness** despite large teacher-student disagreement and **degeneration**, where locally teacher-aligned updates raise the probability of unsuccessful continuations.
  - Shows offline distillation can prepare a student for OPD without improving immediate held-out accuracy; OPD alone may degrade generation but helps substantially after enough offline preparation.
  - Connects teacher supervision, student geometry, and the evolving rollout distribution.

### 11) [CoRD: Coupled Rollouts Fill the Blind Spot of On-Policy Distillation](https://arxiv.org/abs/2611.07959)
- **Authors:** Guhan Chen, Bohan Li, Jun Rao, Hejin Wang, Songtao Tian, Yexin Xie, Xiaojun Meng, Peng Yuan, Jiansheng Wei, Xuebo Liu, Zixiong Yu
- **Categories:** cs.CL, cs.LG
- **Summary:** OPD only supervises states the student actually reaches, so teacher-reachable states remain a blind spot. CoRD moves the **training-state distribution** toward the teacher while keeping the on-policy loss.
- **Key Contributions:**
  - Draws rollouts from a geometric interpolation of student and teacher via the **maximal coupling of speculative decoding**; interventions are as rare as an exact sampler allows and recede as the student learns.
  - Six base students (Qwen3 / Qwen3.5, 0.6B–4B): **+0.9 to +2.0 pass@1** and **+1.2 to +3.4 pass@8** over OPD on five math benchmarks at equal steps/data.
  - On frozen teacher-reached states, a 4B student closes in **16 steps** what OPD does not close in 80.

### 12) [Unpacking the Compute Efficiency of Strong-to-Weak OPD against GRPO](https://arxiv.org/abs/2611.08453)
- **Authors:** Zeyu Leo Liu, Yang Li, Bo Pang, Emre Can Acikgoz, Xuan-Phi Nguyen, Anurag Koul, Srijan Bansal, Erik Nijkamp, Shafiq Joty, Semih Yavuz
- **Categories:** cs.CL, cs.LG
- **Summary:** Measures held-out accuracy against training FLOPs for reverse-KL OPD vs GRPO across task difficulty, student/teacher size, domain, and optimization choices.
- **Key Contributions:**
  - With an **external** post-trained teacher, OPD generally loses to GRPO in accuracy per training FLOP and often inflates response length.
  - With the teacher set to the student's **own GRPO checkpoint**, OPD recovers that checkpoint's math accuracy with **50× fewer distillation FLOPs**; holds for larger students, code, and a second model family.
  - Multi-teacher OPD consolidates per-domain GRPO experts into one student, with distillation costing **5.2% (2 domains) / 8.0% (4 domains)** of specialist training FLOPs.

### 13) [Loopback Transformer: Towards a Unified View of Residual Looped Transformers](https://arxiv.org/abs/2611.07226)
- **Authors:** Xuan Ouyang, Zefan Cai, Chenlong Zhang, Cheng Luo, Ke Wan, Junjie Hu
- **Categories:** cs.LG
- **Summary:** Takes a depth-memory view of residual connections: a full block output mixes its input with its new update, so weighting the output also reweights already-carried history. Reading updates individually gives separate controls.
- **Key Contributions:**
  - **Loopback Transformer** keeps the shared stack's input on a separate path and reads individual updates, with geometric decay setting total update weight and attention learning its allocation.
  - Beats standard Transformers using **40–75% of their parameters** (excl. embeddings/head) on ClimbMix at 191M–3B with matched tokens and depth.
  - Higher 13-task mean accuracy at 1.4B and 3B; best validation loss among eight looped residual designs at 191M–778M.

### 14) [Test-Time Self-Play: Scaling without a Verifier](https://arxiv.org/abs/2611.07367)
- **Authors:** Akira Yoshiyama, Akmal Ashirmatov, Jonas Hübotter, Ido Hakimi, Andreas Krause
- **Categories:** cs.AI, cs.LG
- **Summary:** Most test-time scaling needs a verifier to select or refine candidates; TTSP uses **asymmetric self-play** instead, so it can scale where no reliable target verifier exists.
- **Key Contributions:**
  - Best method at every verifier strength on a difficulty-calibrated LiveCodeBench v6 subset; the gap widens as the verifier weakens.
  - In the no-verifier limit: **+35% absolute mean@8**.
  - Gains hold unless the base policy has near-zero coverage of the correct answer (a clear failure boundary).

### 15) [Scaling Laws for SAE Training Data](https://arxiv.org/abs/2611.07756)
- **Authors:** Nikita Koriagin, Nikita Balagansky, Daniil Gavrilov
- **Categories:** cs.AI, cs.CL, cs.LG
- **Summary:** Studies how many **unique activations** an SAE needs when the total training budget is fixed. Quality rises fast with buffer size, then plateaus where replaying the buffer matches fresh activations.
- **Key Contributions:**
  - Fits a diversity-vs-repetition scaling law for limited data, validated across dictionary sizes, token budgets, Llama-3.1 / Qwen3 layers, and BatchTopK / TopK / JumpReLU SAEs.
  - Beyond the plateau, extra unique activations add little for reconstruction or interpretability.
  - Practical rule: pick the smallest buffer that reaches the plateau and replay it — **8–64× less activation storage** with negligible quality loss.

### 16) [SAE Interprets MoE: Sparse AutoEncoders Reveal That MoE Experts Exhibit Human-Interpretable Fine-Grained Specialization](https://arxiv.org/abs/2611.08089)
- **Authors:** Anyuan Zhuo, Shaohua Zhang, Yuan Lin, Pinyan Lu
- **Categories:** cs.LG
- **Summary:** Rather than counting gating frequency on domain-labeled corpora, trains an SAE on the MoE layer output; because the encoder is affine, each latent's pre-activation decomposes exactly over experts.
- **Key Contributions:**
  - On Qwen3-30B-A3B layers 4/30/46, **contribution is far more concentrated than gating**; most latents have only one or two dominant experts.
  - Dominant-set overlaps concentrate on a few expert pairs.
  - Auto-interpretation shows division of labor below coarse domains — separate experts for Java vs front-end code, or geometry vs arithmetic/polynomials — while domains take very unequal numbers of experts.
  - SAEs and code released (ByteDance Seed).

### 17) [What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?](https://arxiv.org/abs/2611.06483)
- **Authors:** Kejian Zhu, Zhuoran Jin, Shangqing Tu, Tianyi Men, Yupu Hao, Jiachun Li, Kang Liu, Jun Zhao
- **Categories:** cs.CL, cs.LG
- **Summary:** Evaluates agentic RL through sampling breadth `K` and interaction depth `T` via `Pass@(K,T)`, showing that trajectory-level advantages depend on sufficient turn budgets.
- **Key Contributions:**
  - Gains diminish sharply as budgets tighten; agentic RL does **not** uniformly improve single-step decisions.
  - Strength concentrates in **error recovery and long-horizon resilience**.
  - Introduces **BudgetMix RL**, varying interaction budgets during training, for robust performance across execution settings; discusses process-supervision trade-offs.

### 18) [Measuring the Marginal Value of Verifier-Based RL Beyond Supervised Fine-Tuning](https://arxiv.org/abs/2611.07639)
- **Authors:** Amit Sagtani, Saloni Garg
- **Categories:** cs.AI, cs.LG
- **Summary:** A pre-registered, controlled test of what RLVR adds after SFT, using `gpu-train-debug`: 1,877 synthetic GPU/LLM training failure-diagnosis tasks across 30 archetypes with a partial-credit programmatic verifier.
- **Key Contributions:**
  - 1,200 gold demonstrations nearly solve the benchmark (SFT 0.785 hard split) while 15 GRPO steps do not move the base model (0.314 vs 0.311).
  - At pre-registered scale: **no detectable in-distribution gain** (+0.22 pts, 95% CI [−0.06, +0.51]); modest OOD gain (+0.33 pts, CI [+0.02, +0.68]).
  - Residual SFT errors are mostly systematic and identical across samples, reducing GRPO's within-group signal — a useful negative result for "RL adds on top of SFT" assumptions.

### 19) [La-JEPA: Compact Robot Policies with Latent World Modeling](https://arxiv.org/abs/2611.08156)
- **Authors:** Mateo Clémente, George Z. Xue, Amin Abyaneh, Liheng Ma, Rui Heng Yang, Tongtong Cao, Zhanguang Zhang, Yingxue Zhang
- **Categories:** cs.CV, cs.LG, cs.RO
- **Summary:** Trains a compact world-action policy from scratch in the feature space of a pretrained **V-JEPA 2.1** encoder, predicting future features jointly with actions during training but generating only actions at inference.
- **Key Contributions:**
  - SOTA among policies without embodied pretraining on RoboTwin 2.0 (clean/randomized) and LIBERO-Plus with correct instructions, at far fewer parameters than the strongest competing policies.
  - Faster than Fast-WAM at comparable performance; beats LeapBot-WA and JEPA-WAM without their pretrained policy backbones.
  - Design study: JEPA features beat video-VAE latents, most clearly OOD; training-time future prediction matters even when skipped at inference.
  - Corrects corrupted LIBERO-Plus evaluator instructions and re-evaluates.

### 20) [On the Design of Hyper-Connections: Simplification, Stability, and Scalability](https://arxiv.org/abs/2611.05984)
- **Authors:** Xiangdong Zhang, Xiaohan Qin, Sunan Zou, Tuo Dai, Bizhao Shi, Zhuo Xia, Yebin Yang, Yizhou Chen, Yuliang Liu, Yu Cheng, Junchi Yan
- **Categories:** cs.CL, cs.LG
- **Summary:** Systematically ablates Hyper-Connections (HC), increasingly used in frontier models but poorly understood and costly to train.
- **Key Contributions:**
  - Shows learned read/write gating without mixing, or unconstrained mixing with fixed gates, each match mHC alone.
  - Identifies repeated access to the expanded residual state as the main training overhead.
  - **SimpleHC** removes residual mixing and uses shared memory access: only **2.4% extra training time** over a vanilla residual at the largest tested scale, comparable to mHC from 15B to 30B MoE, with smoother gradients and stress stability.

## Also Notable

- **[O$^2$PD: Overlap-Gated On-Policy Distillation on Reliable Prefix](https://arxiv.org/abs/2611.07731)** — aligns only the first 20% of each student rollout; adds reset-atom and support-convergence strategies to fix teacher-support uncovering and dominant-mode mismatch in top-k OPD.
- **[D$^2$-OPD: Separating Direction and Distance in Extrapolative On-Policy Distillation](https://arxiv.org/abs/2611.07241)** — decouples extrapolation direction from distance with a per-prefix hard KL constraint; up to **+9.45 points** on math reasoning.
- **[CacheGraft: Enhancing RAG via Latent-Space Document Enrichment](https://arxiv.org/abs/2611.07393)** — offline fused KV-cache passage representations injected into a 0.6B receiver; better answers in 29/30 comparisons, 17 significant, zero-shot for the fuser.
- **[Decision Models as Retrieval Gates Against Injection and Pollution](https://arxiv.org/abs/2611.08325)** — a 4B decision-model gate cuts injection attack success from 27.9% to **5.7%** and fake-page exposure to 0.5%, at 76 ms/passage.
- **[FastAFD: When Does Attention-FFN Disaggregation Pay on Rack-Scale NVLink?](https://arxiv.org/abs/2611.07149)** — AFD beats wide-EP vLLM by **1.17× / 1.16×** on Qwen3 / Qwen3.5 on GB200 NVL72; an analytical model predicts the gain within 3%.
- **[FlashOffloading: Low-Latency KV Cache Offloading for Long-Context LLM Serving](https://arxiv.org/abs/2611.07542)** — fully host-DRAM-resident KV cache; **1.38× prefill / 1.91× decode** under a 30 ms TPOT SLO on Ascend910C with GLM-5.2 + MTP3.
- **[LowRAM: Low-Rank Keys and Amortised Values for Composable KV Cache Compression](https://arxiv.org/abs/2611.07025)** — values are predictable from keys; **4× near-lossless value compression**, up to 5× decode throughput, and 26.9× composed compression at 94.5% of baseline.
- **[The Memory Trap: Language Agents Overgeneralize from Benign Interactions](https://arxiv.org/abs/2611.07554)** — benign preference memories leak into high-stakes tasks across six frontier models, causing skipped verification, sycophancy, weakened tests, and more cheating on ImpossibleBench.
- **[Rethinking Data Selection: The Importance of Coverage over Difficulty in LLM Fine-Tuning](https://arxiv.org/abs/2611.07323)** — difficulty-based selection often fails to beat random; a clustering-based coverage method wins on multi-domain Tülu 3.
- **[PlayGen2: Learning Real-Time Playable Worlds with Explicit 3D State](https://arxiv.org/abs/2611.07867)** — separates learned 3D state evolution (occupancy grid + entity states) from neural rendering; ~160 ms backend latency on an M4 Pro, zero-shot unseen Doom maps.
- **[A Night at the LLM Zoo: Data Conditioned Flow Matching for Generating Pretrained LLM Weights](https://arxiv.org/abs/2611.07103)** — 100-model GPT-2 zoos per scale; flow matching in Gram-PCA weight space generates weights from data-mixture conditioning with zero-shot mixture generalization.
- **[ConvPE: Convolutional Position Embedding Improves Transformers](https://arxiv.org/abs/2611.07749)** — lightweight causal-conv, content-dependent attention bias compatible with RoPE, masks, and KV concatenation.
- **[Muir: Linear Attention with Sensitivity-Allocated Gating and Matched-Filter Readout](https://arxiv.org/abs/2611.08376)** — shows state updates are less sensitive to erasure than writes; **1.8–2.0% lower perplexity** than GDN-2 and 2,560× length extrapolation (4K → 10M).
- **[StrataFlux: Memory-Hierarchy-Native Low-Bit LLM Inference](https://arxiv.org/abs/2611.08363)** — streams selective precision from RAM/SSD; 2-bit Qwen3-8B AIME 2024/2025 **11.0% → 47.1%** at unchanged GPU memory.
- **[Resource-Efficient RL Post-Training through Elastic Expert Parallelism](https://arxiv.org/abs/2611.06984)** — FlexFloor releases MoE workers early while preserving expert availability: **+52.74%** rollout throughput, +65.40% tokens per occupied compute time.
- **[KOSMOS: Self-scheduling Persistent Kernels for Communication-Compute Overlap](https://arxiv.org/abs/2611.07477)** — demand-ordered workgroups switch between comm and compute roles; **1.29–1.83×** end-to-end training speedup on DeepSeek-V3 / Qwen3-235B proxies over DeepEP.
- **[Archetypal contexts in the neurons of language models](https://arxiv.org/abs/2611.07234)** — causal neuron silencing in Qwen3.8-27B separates language, topic, and cross-domain relational archetypes into a "sandwich" layer structure.

## Emerging Trends

- **OPD is being debugged, not just applied.** Four papers in one batch address state coverage (CoRD), supervision reliability (O²PD), extrapolation geometry (D²-OPD), and FLOP accounting vs GRPO. The recurring finding: external teachers are expensive per FLOP, while **self-teacher / multi-teacher distillation** is where the efficiency is.
- **Generative recommendation is fixing the quantization interface.** BRIDGE and OptST both target the mismatch between continuous semantic structure and discrete SIDs — one on the decoder side, one on the tokenizer side.
- **Industrial re-ranking is moving from per-item CTR to process models.** ICE's display → impression → click formulation is the clearest example yet that sequence-level utility needs causal exposure modeling.
- **RL reward design for recommenders has a diversity failure mode.** The CF item-mean decomposition gives a simple, effective correction and a reusable diagnostic.
- **Interpretability is becoming infrastructure.** SAE buffer scaling laws make SAE training cheaper; SAE-over-MoE turns expert specialization into a measurable, decomposable quantity.
- **KV-cache work is splitting along the memory hierarchy.** LowRAM (compression), FlashOffloading (host DRAM), StrataFlux (RAM/SSD streaming), and GINGER (vector index) all optimize different tiers rather than one monolithic cache.
- **Long-context efficiency is going hierarchical and logarithmic.** RecSA's tree-structured KV selection is notable for extrapolating far beyond its training length with positive speedups.

## Notes

- Data source: arXiv RSS for `cs.IR`, `cs.AI`, `cs.LG`, `cs.CL`; latest `lastBuildDate` = Fri, 06 Nov 2026. The 2026-11-07 batch does not exist (Saturday skip), so this report covers the freshest Fri 2026-11-06 announcement block.
- Counts: **826 unique items**; **461 unique `new`/`cross`**; **21** touch `cs.IR` (12 `new`-only). `replace`/`replace-cross` excluded.
- arXiv has no dedicated CTR category; CTR/ads work appears under `cs.IR` with cross-lists to `cs.LG` / `cs.AI`.
- Abstract-only screening. Numbers are author-reported and were not independently reproduced.
- All featured IDs grep-verified absent from the wiki before writing; no overlap with the 2026-10-29 / 2026-10-31 `arxiv-paper-check` reports.
- "Announced" is the RSS announcement date, not necessarily the original submission date.
