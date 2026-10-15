---
title: "Conference & arXiv Digest — 2026-10-14 (NeurIPS 2026 / EMNLP 2026 / ICLR 2027-under-review / ICML 2026 / WWW 2026 / CVPR 2026 / AAAI 2026 / CIKM 2026 / ICLR 2026 workshops / RecSys — AI · LLM · Recommendation · Advertising · CTR · Agents · Code · Generative · Sequential · Games · Benchmarks)"
type: synthesis
created: 2026-10-14
updated: 2026-10-14
sources: [arxiv-export-api, arxiv-html, conference-announcements]
tags: [conference-digest, NeurIPS2026, EMNLP2026, ICLR2027, ICML2026, WWW2026, CVPR2026, AAAI2026, CIKM2026, ICLR2026, RecSys2026, agents, LLM, diffusion, flow-matching, recommendation, advertising, CTR, search, RAG, code-execution, reasoning, RL, RLVR, scaling-laws, quantization, KV-cache, linear-attention, activation-steering, memorization, benchmark-validity, safety, jailbreak, backdoor, science, multimodal, industry, daily-digest]
---

# Conference & arXiv Digest — 2026-10-14

> **Scope.** Papers carrying a *verified* venue tag from **NeurIPS 2026, EMNLP 2026, ICML 2026, ICLR 2026/2027, WWW 2026, CVPR 2026, AAAI 2026 Fall Symposium Series, CIKM 2026, RecSys** (including workshops, Findings, Industry, and Evaluations & Datasets tracks), plus fresh un-venued preprints in the wiki's AI / LLM / recommendation / advertising / CTR / agents / code-execution / generative / sequential-modeling / games / benchmark lanes. **78 papers featured**, organized first by **venue**, then by **category** for un-venued work. The run is **collision-managed against today's sibling** `arxiv-paper-check` ([2026-10-14](../2026-10-14/arxiv-paper-check.md), 36 IDs) via the dedup baseline (§0).
>
> **Requested venues coverage note.** The requested conference grid (ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025) is largely *closed* — its accepted papers were digested across the 2026 H1/H2 runs. In the newest announcement block the live venue tags are **NeurIPS 2026 (main/workshops), EMNLP 2026, ICML 2026, ICLR 2027 (under review), WWW 2026, CVPR 2026W, AAAI 2026 Symposium, CIKM 2026W**, with a sprinkle of **ICLR 2026 workshops** and **RecSys in HR '26**. Papers newly *preprinted* under the older requested tags are folded into §6.

**Method (for reproducibility).** Harvest via the **arXiv export API** (`export.arxiv.org/api/query`, Atom XML) in three passes: **(1)** 46 venue `co:`/`all:` sweeps (23 venue strings × comment + all-terms, pulling the newest ~100 matching each so 2026 acceptances surface regardless of submission date); **(2)** 15 category sweeps (`cat:cs.AI/LG/CL/IR/CV/MA/NE/CR/SI/DB/DC/SE`, `stat.ML`, `cs.HC`, `eess.AS`) bounded to `submittedDate:[202610100000 TO 202610111200]`; **(3)** 24 industry `co:` sweeps (Kuaishou, ByteDance, Alibaba, Tencent, Baidu, Meituan, Netflix, DeepMind, Microsoft Research, Meta AI, Ant Group, Xiaohongshu, Shopee, LinkedIn, NVIDIA, Amazon, Huawei, OpenAI, Anthropic, Apple, …) plus 25 topical `all:` queries (recommendation, click-through rate, CTR prediction, advertising, ad auction, generative recommendation, sequential recommendation, agent, world model, game playing, code execution, benchmark, diffusion, reasoning, RL, KV cache, quantization, …). All queries spaced ≥2 s. ~85 of 110 planned queries returned (the topical date-bounded tail was partly rate-limited; recorded as a coverage caveat, §16). **2,530 unique records → 2,075 unclaimed → 476 published ≥ 2026-09-18 → 199 venue-tagged → 78 featured.** Venue tags were read from each entry's arXiv `comment` / `journal_ref` fields and are **self-reported** (main vs Findings vs workshop vs Industry stated where the comment distinguished them). **Affiliations were read only from each paper's own arXiv HTML author block** — confirmed company/lab names are quoted; unresolved items are marked *(affiliation not recovered)* rather than guessed. The newest indexed announcement block is **2026-10-10** (same block as today's `arxiv-paper-check`; 10-11 → 10-14 not yet indexed).

**Dedup.** Baseline regex-extract of every `\d{4}\.\d{4,5}` across `wiki/**/*.md` at run start → **9,015 claimed IDs**. All **78 selections re-verified `rg` 0-hit against the whole live wiki immediately before writing**; **0 collisions**.

---

## 0. Executive Summary

- **Venue spread (78 papers):** **NeurIPS 2026** main/E&D **17**, NeurIPS 2026 workshops **14**, **EMNLP 2026** (Main 3 + Findings 2 + Industry 1 + EMNLP LMP workshop 1) **7**, **ICML 2026** (Main 1 + workshops 2) **3**, **ICLR 2027 (under review) 6**, other closed/new venues (RecSys in HR '26, AACL-IJCNLP Findings, WWW 2026, CVPR 2026W, AAAI 2026 Symposium, CIKM 2026W, ICLR 2026 workshops, TOSEM) **9**, and **22 un-venued fresh preprints** across the recommendation/agents/code/generative/sequential/safety lanes.
- **Industry / top-lab density (18 of 78 have a confirmed company/lab affiliation):** **Netflix** (Semantic-ID recommender, PALM — Netflix Personalization Foundations), **Google Research / Allen Institute / Move37 Labs** (AutoNovo), **Amazon / AWS AI Labs** (RAD; AGI-Lab retrieval audit), **Tencent Hunyuan** (OmniCapBench) and **Tencent WeChat AI** (WorkBorne), **Alibaba Tongyi Lab** (SMOKE backdoor), **Huawei** (FidelityQ; AnyEdit audio), **Microsoft Research** (Sequent-Prover; DEFT EEG), **NVIDIA** (Nemotron-3-Nano-30B Indic adaptation — *gnani.ai* + NVIDIA model), **Qualcomm** (hardware-fault agents), **Intel AI** (activation-steering curvature), **Fidelity Investments** (AURA; MARTA), **Adobe / Amazon / PNNL / Georgia Tech** (CoRE), **NEC Labs America** (SpecForge, TeSearch), **Nokia Bell Labs + Cambridge** (PotentialEP), **Luma AI** (spiking-LM scaling laws), **Google DeepMind** (PopGen, co-author), **Airbnb** (agentic RAG skills), **Sandia / Argonne** (PDE-PFN; BigCell). *(Affiliations are author-block reads, not disambiguated corporate entities.)*
- **The dominant technical cluster is *evaluation validity* (at least 9 papers):** **MisVisAgentBench** (misleading charts drop Web-Agent success), **Auditing VLM Benchmarks** (20.2% of MMStar items gain nothing from the image), **SRCoD** (item-level multimodal shortcut diagnosis), **Lumen-bench** ("say-do" tool-calling ethics across 5 languages, 194,400 trials), **Sanzaru** (protocol formation under epistemic/communication asymmetry; ~60% of losses are communication), **CRJudgeBench** (can AI judge a plausible-but-wrong code review?), **GNN-CB** (competition benchmark for GNN coding), **Clinical Triage** (LLMs more perturbable than physicians), and **UDHRBench**. The recurring result: *leaderboard agreement without correctness*.
- **A second cluster: *inference-time computation is being re-architected at serving time*** — **SAFE-KV** (non-prefix KV reuse repaired from 47.2%→99.8% full-prefill agreement), **FidelityQ** (2-bit scalar quantization by preserving *predictive* fidelity), **FCM** (non-adjacent layer fusion beats ShortGPT on 12/13 LLMs), **LLoPS** (learnable low-rank polynomial linear attention), **FramePack-U** (constant-memory frame packing), **RAD** (reward-aligned on-policy distillation).
- **A third cluster: *self-improving / verifier-grounded agents*** — **SpecForge** (multi-frontier tree search over behavioral specs, NeurIPS 2026 main), **TeSearch** (test suites as a dense improvement signal; rejects 59.9% of behavior-changing rewrites), **Sequent-Prover** (SMT-LIB agents; 4B pass@1 85.6→97.0), **SymCE** (RLVR repairs the SFT "imitation trap" 0.00→0.66 true-theorem recognition), **WorkBorne** (agentic tasks from real artifact transitions), **Reels-RSI** (program-level self-improvement).
- **Numbers that anchor the window:** **BigCell** generates coherent **32,768×32,768** pathology WSIs at native gigapixel scale; **X-AVDD** lifts audio-visual distillation top-1 **8.2%→24.0%** (SPC=10) at **~8× fewer GPU-hours**; **SmolWAM** succeeds on **95.5%** of 400 LIBERO episodes at **57 ms / 2.4 GiB** (11× faster than its teacher); **RELAGRAM** (0.53M params) generalizes zero-shot CVRP-100 → CVRP-1000 at 21.7% gap; **Personalized LLM Rec** compares single-head AR beam search vs. multi-token prediction at industry scale; **CFG/diffusion and reasoning** appear via **PotentialEP** (backprop-free CIFAR-scale generation), **PDE-PFN / SBNO** (PDE foundation operators).
- **Recommendation / CTR lane vacancy persists (as in the last several digests).** **Zero explicit click-through-rate papers** surfaced in this block; the rec/search lane yields 6 papers (Netflix SID recommender, multimodal-rec explainability survey, SG²RAG, conversational-search faithfulness, a Jev-style retrieval audit, and a video-search system). The industrial CTR *architecture* (scaling laws, long-sequence modeling) lane is **empty again** (§16).
- **Continuity with the wiki's arcs:** the *optimization-of-generation* thread (10-07 looped-LM, 10-12 inference-time control) now shows as **serving-time KV repair + quantization + layer fusion**; the *evaluation-validity* thread (10-12's dummy-bench cluster) widens with **misleading-chart Web agents** and **benchmark auditing from existing runs**; the *diffusion-as-substrate* thread shows up in **flow-matching pathology and audio generation** (BigCell, AnyEdit).

---

## 1. NeurIPS 2026 — Main Track & Evaluations (17 papers)

### 1.1 SpecForge: Recursive Self-Improvement for Coding Agents via Behavioral Specifications
- **中文标题**: SpecForge：通过行为规格实现编码智能体的递归自我改进
- **Authors**: Yutong Cheng, Haifeng Chen, Peng Gao, Wei Cheng
- **Affiliation**: Virginia Tech; NEC Laboratories America
- **Venue**: **NeurIPS 2026** (Main Track, accepted)
- **Problem background**: Frozen-LLM coding agents can only improve by refining *external context*, not weights. Natural-language code documentation ("behavioral specifications") that describes program-entity behavior is such a context, but recursive refinement is hard because program entities are interdependent — improving one specification can degrade others ("output coupling"), producing a whack-a-mole effect.
- **Key innovation**: **SpecForge** — a **multi-frontier tree search** over specification edits that runs a generate → execution-verified-test → refine loop, explicitly searching the coupling landscape to avoid regression whack-a-mole while keeping weights frozen.
- **Results / comparison**: Reported to enable recursive self-improvement where greedy local specification edits stall; the tree search preserves global correctness across interdependent entities. *(Detailed benchmark deltas in the NeurIPS camera-ready.)*
- **Link**: https://arxiv.org/abs/2610.15708

### 1.2 Approximation in Contrastive Representation Learning
- **中文标题**: 对比表示学习中的逼近理论
- **Authors**: Yuanfan Li, Zihan Zhang, Yiming Ying, Ding-Xuan Zhou
- **Affiliation**: School of Mathematics and Statistics, University of Sydney
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: The population target of contrastive representation learning (CRL) is the pointwise mutual information (PMI) between two modalities — a generally *nonseparable* function — yet standard inner-product scores `f(x)ᵀg(y)` appear to approximate it well. Why was unclear.
- **Key innovation**: Links PMI to a compact operator and shows **D-dimensional inner-product models perform rank-D spectral approximation**, with error controlled by the spectral tail. Proves universal consistency of deep scoring functions with approximation rates governed by PMI smoothness, improved rates for structured low-rank data, and a **fast calibration** result.
- **Results / comparison**: Provides the first approximation-theoretic account of why inner-product CRL works; tightens rates under low-rank structure.
- **Link**: https://arxiv.org/abs/2610.15388

### 1.3 The Sharp Directions Are Against You: Curvature Analysis of Activation Steering
- **中文标题**: 尖锐方向与你为敌：激活引导的曲率分析
- **Authors**: Seyedarmin Azizi, Arya Fayyazi, Parsa Razmara, Erfan Baghaei Potraghloo, Souvik Kundu, Massoud Pedram
- **Affiliation**: University of Southern California; **Intel AI**
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: Contrastive activation addition (CAA) steering is fragile: on many inputs it shifts behavior in the *wrong* direction. The geometry behind this fragility was unknown.
- **Key innovation**: Introduces the **steering Hessian** — second derivative of behavioral loss w.r.t. the steering vector. Its top eigenvectors are **sharp directions** (tiny perturbations → large erratic swings); bottom eigenvectors are **flat** (robust). Removing the sharp component approximately preserves direction and magnitude (cosine > 0.974, norm reduction < 3%) while cutting directional curvature up to **12×**.
- **Results / comparison**: Explains CAA fragility and yields a principled, cheap fix that stabilizes steering without retraining.
- **Link**: https://arxiv.org/abs/2610.16084

### 1.4 Beyond Adjacent Layers: Graph-Guided Layer Fusion for Compressing Large Language Models
- **中文标题**: 超越相邻层：面向大模型压缩的图引导层融合
- **Authors**: Muhammad Usama, Yeoreum Jung
- **Affiliation**: Braindeck Inc, Seoul, Republic of Korea
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: Depth-compression methods score layers individually or merge only *adjacent* layers, implicitly assuming redundancy is local.
- **Key innovation**: Computes **full pairwise CKA similarity matrices for 13 LLMs across 6 families (1.6B–14B)** and finds **non-adjacent layers have 3.6–15.9× more high-similarity pairs** than adjacent ones. Proposes **Fusion via Community Mining (FCM)**: build the full L×L similarity graph, spectral community-detect functionally equivalent clusters, keep the highest-Block-Influence layer per cluster, apply LoRA recovery; a calibration-only rule picks cosine vs. CKA.
- **Results / comparison**: At **2× compression**, FCM lowers mean perplexity below **ShortGPT on 12/13 models** (significant on 10; up to **50%** on Qwen3-4B).
- **Link**: https://arxiv.org/abs/2610.15159

### 1.5 Scaling Laws for Multimodal Data Mixtures
- **中文标题**: 多模态数据混合的 Scaling Law
- **Authors**: Aditi Khandelwal, Ayush K. Tarun, Yixuan Xu, Imanol Schlag, Golnoosh Farnadi, Siva Reddy, Luke Zettlemoyer, Antoine Bosselut
- **Affiliation**: Mila/McGill; EPFL; ETH; University of Washington
- **Venue**: **NeurIPS 2026** (spotlight, accepted)
- **Problem background**: Frontier systems are natively multimodal, but the science of *how much of each modality to mix* (and the interference cost) is absent or gatekept.
- **Key innovation**: Derives **data-mixing scaling laws for text, vision, audio** using MoE MLLMs over **268 experiments (457M–8.3B params, up to 150B tokens)**. Compute optima are **modality-specific**: audio is *model-heavy* (scale parameters), text/vision need balanced scaling; repeating vision/audio >2× yields negligible benefit.
- **Results / comparison**: First actionable multimodal mixing recipe; quantifies cross-modal interference under MoE.
- **Link**: https://arxiv.org/abs/2610.14423

### 1.6 Fisher Information and the Geometry of Memorization in Neural Networks
- **中文标题**: Fisher 信息与神经网络记忆的几何
- **Authors**: Daniel T. Bernstein, Chase Goddard, Luca Di Carlo, Vudtiwat Ngampruetikorn, David J. Schwab
- **Affiliation**: Princeton University; University of Sydney; CUNY Graduate Center
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: Understanding generalization requires separating generalizable structure from memorized/idiosyncratic features; Fisher information has been proposed as a diagnostic.
- **Key innovation**: On CIFAR-10 with memorization-only noise, shows **projecting weights onto top Fisher eigenvectors decouples general task performance from noisy-sample memorization**, with layer-dependent structure; reproduces the phenomena in small Transformers on synthetic in-context learning and in a closed-form linear model.
- **Results / comparison**: Establishes Fisher information as capturing how networks allocate capacity between generalization and memorization.
- **Link**: https://arxiv.org/abs/2610.16161

### 1.7 DEFT: Disentanglement-Enhanced Fine-Tuning for EEG Foundation Models
- **中文标题**: DEFT：面向 EEG 基础模型的解耦增强微调
- **Authors**: Yuqiu Deng, Muyun Jiang, Zongpeng Zhang, Mingqing Xiao, Yansen Wang, Peiliang Gong, Xinliang Zhou, Yi Ding, Ziyu Jia, Cuntai Guan, Chenyu Liu
- **Affiliation**: Uploading Inc; Nanyang Technological University; Peking University; **Microsoft Research Asia**
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: EEG foundation model (EFM) embeddings retain substantial *subject-related* variation, burdening cross-subject downstream classifiers.
- **Key innovation**: **DEFT** — a plug-and-play adapter that disentangles pretrained tokens into **task-oriented content** vs. **subject-consistent style** branches and predicts only from the content branch, via recursive Gaussian refinement, temporal-variance regularization, subject-aware contrastive learning, and reconstruction ("factorize-before-classify").
- **Results / comparison**: Improves matched fine-tuning baselines across multiple EEG datasets and four EFM backbones.
- **Link**: https://arxiv.org/abs/2610.14497

### 1.8 OmniCapBench: A Deep-Structured Evaluation Framework for Fine-Grained Audio-Visual Captioning
- **中文标题**: OmniCapBench：细粒度音视频描述的结构化评测框架
- **Authors**: Zhongyu Yang, Jiale Tao, Ruitao Chen, Zuhao Yang, Yingfang Yuan, Xueliang Zhao, Auden, Kai Wang, Shuai Shao, Biao Wang, Steve Yves, Qinglin Lu
- **Affiliation**: **Hunyuan, Tencent**; Nanyang Technological University; Northumbria University
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: Audio-visual captioning benchmarks face a coupled trade-off: whole-caption scores give coverage without localization; local probes give localization without coverage; unconstrained LLM judges are unstable.
- **Key innovation**: Reframes caption evaluation as **sets of atomic, verifiable units** across three tracks (entity references, visual shots, audio events), enabling deterministic constraint checks plus localized LLM semantic comparison; **786 densely annotated videos**.
- **Results / comparison**: Distinguishes MLLM perception errors — temporal-grounding failures, identity drift, cross-modal misalignment, hallucinated description.
- **Link**: https://arxiv.org/abs/2610.12458

### 1.9 X-AVDD: Cross-Attentive Audio-Visual Dataset Distillation
- **中文标题**: X-AVDD：交叉注意力音视频数据集蒸馏
- **Authors**: Saumyaranjan Mohanty, Aravind Reddy, Konda Reddy Mopuri
- **Affiliation**: IIT Hyderabad; IIT Madras (Centre for Responsible AI)
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: Audio-visual dataset distillation (DM/AVDD) is memory-intensive and often fails to preserve cross-modal correspondence.
- **Key innovation**: **X-AVDD** explicitly captures inter-modal relationships with **cross-attention**, decoupling cross-modal alignment from joint optimization for memory efficiency.
- **Results / comparison**: On VGGSound, top-1 test accuracy **8.2% → 24.0%** (SPC=10) and **9.8% → 26.5%** (SPC=20) at **~8× fewer GPU-hours**.
- **Link**: https://arxiv.org/abs/2610.13687

### 1.10 BigCell: Generating Gigapixel Whole-Slide Images
- **中文标题**: BigCell：生成千兆像素全切片病理图像
- **Authors**: Srikar Yellapragada, Alexandros Graikos, Zilinghan Li, Kostas Triaridis, Tarak Nath Nandi, Ji Dong K Bai, Beatrice Knudsen, Tahsin Kurc, Prateek Prasanna, Rajarsi R. Gupta, Ravi K Madduri, Joel Saltz, Dimitris Samaras
- **Affiliation**: Stony Brook University; **Argonne National Laboratory**; University of Chicago; University of Utah; UNC Chapel Hill
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: Histopathology generative models work at patch scale (≤1024×1024), but clinical supervision (reports, slide labels) is whole-slide.
- **Key innovation**: **BigCell** — a flow-matching Transformer trained at 2048×2048 on **>120,000 WSIs**, conditioned on pathology-foundation-model embeddings, with an inference-time sliding-window pipeline and an adaptive scheduling strategy for gigapixel synthesis.
- **Results / comparison**: First coherent whole-slide generation at native resolution — up to **32,768×32,768** pixels — beating prior tile generators on tile- and slide-level fidelity.
- **Link**: https://arxiv.org/abs/2610.14261

### 1.11 AnyEdit: A Unified Framework for Speech and Singing Voice Editing with Real-World Environmental Consistency
- **中文标题**: AnyEdit：保持真实环境一致性的语音与歌声编辑统一框架
- **Authors**: Yunjia Zhang, Junan Zhang, Jing Yang, Xueyao Zhang, Fan Fan, Zhizheng Wu
- **Affiliation**: The Chinese University of Hong Kong, Shenzhen; **Institute of Media Technology and Experience Design, Huawei**
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: Real-world vocal editing must revise content while preserving speaker identity, prosody, and the acoustic scene (noise, reverb, background music); end-to-end noisy modeling entangles semantics with acoustics.
- **Key innovation**: **Separation-free two-stage** design — an instruction-guided autoregressive editor predicts clean prosody/content-style tokens (with a teacher-student noise-robust prosody tokenizer), then a **flow-matching acoustic model** renders in-context conditioned on the source scene.
- **Results / comparison**: Preserves clean-domain editing while maintaining real-world environmental consistency.
- **Link**: https://arxiv.org/abs/2610.15665

### 1.12 PDE-PFN: Prior-Data Fitted Neural PDE Solver
- **中文标题**: PDE-PFN：先验数据拟合的神经 PDE 求解器
- **Authors**: Jaehyeon Park, Mingu Kang, Dongseok Lee, Woojin Cho, Kookjin Lee, Anthony Gruber, Youngjoon Hong, Noseong Park
- **Affiliation**: SolverX; KAIST; Seoul National University; TelePIX; Arizona State University; **Sandia National Laboratories**
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: Neural PDE solvers typically need dense observations or physics constraints and generalize poorly across heterogeneous equations.
- **Key innovation**: **PDE-PFN** approximates the **posterior predictive mean** of PDE solutions by in-context learning, using a PFN Transformer with self-/cross-attention pretrained on **noisy approximate solutions from PINNs** (diverse but inexact priors).
- **Results / comparison**: Demonstrates empirical generalization across heterogeneous 2D PDEs, robustness under noisy priors, and **zero-gradient-update in-context inference**, competitive with evaluated baselines.
- **Link**: https://arxiv.org/abs/2610.13334

### 1.13 SBNO: Schrödinger Bridge Neural Operator for Forward and Inverse Problems under Missing Information
- **中文标题**: SBNO：缺失信息下正反问题的薛定谔桥神经算子
- **Authors**: Jaehyeon Park, Inhyeok Jeong, Noseong Park
- **Affiliation**: SolverX; KAIST
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: PDE surrogates usually assume dense observations or known physics; in practice observations are sparse/partial and physics may be unknown.
- **Key innovation**: **SBNO** — an equation-free **paired-data diffusion Schrödinger bridge matching** framework learning conditional operators for forward *and* inverse PDE problems; a mask-aware endpoint coupling preserves input–solution pairing; inference integrates a probability-flow ODE (no observation-guidance tuning).
- **Results / comparison**: On five PDE benchmarks with **5% observations**, superior/comparable accuracy with lower test-instance error dispersion.
- **Link**: https://arxiv.org/abs/2610.13317

### 1.14 Are Multimodal Benchmarks Really Useful? Item-Level Multimodal Benchmark Diagnosis via Structure-Response Co-Calibration
- **中文标题**: 多模态基准真的有用吗？基于结构-响应协同校准的条目级诊断
- **Authors**: Shiqi Zhang, Weixin Zeng, Ziheng Zhang, Jiuyang Tang, Xiang Zhao
- **Affiliation**: National University of Defense Technology (NUDT), China
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: Multimodal benchmarks contain shortcut items answerable from a single modality or answer-option regularities, failing to reflect true cross-modal inference.
- **Key innovation**: **SRCoD** — a **structure-response co-calibrated** diagnosis: estimate sample-wise multimodal information structure from content+answers, use it as a soft anchor for modality-conditioned item-response modeling, producing calibrated item-level modality-dependence profiles.
- **Results / comparison**: Enables fine-grained benchmark auditing that neither intrinsic-structure nor response-only methods achieve.
- **Link**: https://arxiv.org/abs/2610.14542

### 1.15 Adaptive Compression and Targeted Perturbation: A Unified Framework for Generalized Audio Deepfake Detection
- **中文标题**: 自适应压缩与定向扰动：泛化音频深伪检测统一框架
- **Authors**: Jianqiao Cui, Haoxian Zhu, Hanbiao Meng, Yanghao Zhang
- **Affiliation**: Yangtze Delta Region Institute of Tsinghua University; University of Southampton; Taiyuan University of Technology; Imperial College London
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: ADD methods generalize poorly — fixed bottlenecks can't adapt to heterogeneous spoofing-artifact densities; standard augmentation causes a robustness-accuracy trade-off.
- **Key innovation**: **Adaptive Audio Feature Integration (AAFI)** dynamically selects latent dimensions (compression pool + stochastic exploration) plus **Mel-Band Adversarial Perturbation (Mel-BAP)** for invariant decision boundaries.
- **Results / comparison**: On ADD 2022 / FakeOrReal / In-the-Wild, a Whisper-small backbone reaches SOTA average **EER 1.51%**.
- **Link**: https://arxiv.org/abs/2610.16049

### 1.16 Elephant in the Fridge: Constant-Memory Frame Packing for Long Video Understanding
- **中文标题**: 冰箱里的大象：面向长视频理解的恒内存帧打包
- **Authors**: Shuo Gao, Chenhao Zheng, Zhongzheng Ren
- **Affiliation**: Renmin University of China; University of Washington; UNC-Chapel Hill
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: VLMs encode each frame into visual tokens, so sequences grow linearly with video length → prohibitive memory/latency; token reduction and keyframe selection shorten sequences but leave O(n) scaling intact.
- **Key innovation**: **FramePack-U** — a training-free frame-packing framework compressing arbitrarily long videos into a **fixed-size visual representation at constant memory**; content-aware, prompt-similarity + diversity-driven frame ranking under a fixed token budget.
- **Results / comparison**: Plugs into off-the-shelf VLMs with no fine-tuning; resolves the fundamental O(n) bottleneck.
- **Link**: https://arxiv.org/abs/2610.16118

### 1.17 What DNA Foundation Models Learn Beyond Sequence Composition
- **中文标题**: DNA 基础模型在序列组成之外学到了什么
- **Authors**: Vincenzo Yuto Civale, Andrew David Bagdanov, Alberto Magi
- **Affiliation**: University of Florence
- **Venue**: **NeurIPS 2026** (Evaluations & Datasets Track, accepted)
- **Problem background**: Do genomic foundation models (FMs) provide predictive signal beyond simple k-mer composition?
- **Key innovation**: Benchmarks frozen representations from **five DNA FMs against normalized k-mer frequencies** across **57 genomic classification datasets** + gene-expression regression; decomposes embeddings into a k-mer-linearly-predictable component and a ridge residual; uses exact 6-mer-preserving shuffles to probe order sensitivity.
- **Results / comparison**: Simple k-mers stay competitive with most FMs; **NTv3** (an evolution of Nucleotide Transformer) improves **46/57** datasets (mean ΔMCC **+0.072**) over 6-mers; Caduceus gives smaller gains and the rest no mean improvement.
- **Link**: https://arxiv.org/abs/2610.15711

---

## 2. NeurIPS 2026 — Workshops, Spotlight-Style & E&D-Adjacent (14 papers)

### 2.1 Personalized LLM Recommendation with Semantic IDs: Autoregressive Beam Search vs. Multi-Token Prediction at Industry Scale
- **中文标题**: 基于 Semantic ID 的个性化 LLM 推荐：自回归束搜索 vs. 多 token 预测（工业规模）
- **Authors**: Sejoon Oh, Fernando Amat Gil, Evan Smothers, Dan Iter, Mark Thornburg, Dawit Mureja Argaw, Sourabh Medapati, Thea Wang, Ria Verma, Qiuling Xu, Harshit Syal, Ehsan Gholami, Moumita Bhattacharya, Ashish Rastogi
- **Affiliation**: **Netflix — Personalization Foundations Team**
- **Venue**: **NeurIPS 2026 PALM Workshop** (accepted)
- **Problem background**: Large-scale personalization shifts from embedding-table retrieval to LLM recommenders that *generate* an item's Semantic ID (SID) — a short sequence of discrete hierarchical content codes — letting one instruction-tuned model unify retrieval, content understanding, and language. How should the SID be generated: single-head autoregressive decoding (with constrained beam search) or **multi-token prediction (MTP)**?
- **Key innovation**: An **industry-scale, apples-to-apples comparison** of single-head AR vs. MTP for SID generation, with a **new auxiliary ranking loss defined over the joint SID score** for MTP, evaluated on both quality and training/serving cost.
- **Results / comparison**: Directly contrasts the decoding-latency reduction of MTP against the quality of constrained beam search — the key production trade-off for generative recommenders. *(Full deltas in the workshop camera-ready.)*
- **Link**: https://arxiv.org/abs/2610.15864

### 2.2 Small but Mighty: Test Suites as Improvement Signals for Self-Evolving Agents
- **中文标题**: 小而强：以测试套件作为自进化智能体的改进信号
- **Authors**: Yutong Cheng, Wei Cheng, Wenchao Yu, Dawei Zhou, Haifeng Chen
- **Affiliation**: Virginia Tech; NEC Laboratories America
- **Venue**: **NeurIPS 2026 Workshop on Self-Evolving Diversity-Driven Search (EvoRobust)**
- **Problem background**: A self-evolving agent rewrites its own harness and must decide which rewrites to keep; rollout-based verification is expensive/subjective, while repository tests are too sparse (rejecting only ~¼ of behavior-changing rewrites).
- **Key innovation**: **TeSearch** — a **quality-diversity evolutionary algorithm** that treats suite size as a behavior descriptor (so quality is pursued at every size) and learns a transition kernel denoising the LLM acting on that descriptor, yielding small *and* strong test suites.
- **Results / comparison**: Over **129 real-world modules / 3 backbones**, delivers the highest-quality and smallest LLM-driven suites; as a self-evolving agent's improvement signal it rejects **59.9%** of behavior-changing rewrites.
- **Link**: https://arxiv.org/abs/2610.15964

### 2.3 How Do Hardware Faults Manifest Differently in LLM Agents?
- **中文标题**: 硬件故障在 LLM 智能体中如何呈现不同表现
- **Authors**: Aiden Rubey, Zachary Coalson, Cong Chen, Jean-Philippe Monteuuis, Jonathan Petit, Sanghyun Hong
- **Affiliation**: Oregon State University; **Qualcomm Inc.**
- **Venue**: **NeurIPS 2026 MLforSystems and AI4Good Workshops**
- **Problem background**: Prior hardware-fault resilience work targets *model-level* outputs, but agents loop with tools/environments, changing how faults manifest.
- **Key innovation**: First systematic study across three agent benchmarks (**6,814 executions**; 2,400+ clean, 4,300+ with **two-bit weight faults**), tracing system-level propagation. Finds agents can *recover* from faulty outputs (at higher cost), that a few faults cause subtle semantically-meaningful errors, and that faults can alter security behavior.
- **Results / comparison**: Reframes resilience: "agentic execution transforms model-level corruption into distinct system-level outcomes."
- **Link**: https://arxiv.org/abs/2610.12756

### 2.4 AutoNovo: Agentic Program Search Discovers Transferable Nucleic Acid Design Algorithms
- **中文标题**: AutoNovo：智能体程序搜索发现可迁移的核酸设计算法
- **Authors**: Joel Shor, Subhashini Venugopalan
- **Affiliation**: AI Bio Design, **Allen Institute** & Move37 Labs; **Google Research**
- **Venue**: **NeurIPS 2026 Workshop on Agentic AI for Biological Discovery**
- **Problem background**: In-silico nucleic-acid optimization exploits model-specific artifacts and fails to generalize to independent predictors.
- **Key innovation**: **Agentic program search** iteratively proposes, executes, evaluates, and revises code for nucleic-acid *designers* (not a single universal designer but a discovered *family*).
- **Results / comparison**: Best observed mean on **3/3 DNA-design tasks** (in-silico) and **6/6 transfer tasks** (independent models).
- **Link**: https://arxiv.org/abs/2610.16232

### 2.5 In-Place Indic Tokenizer Expansion and Continual Pretraining of Nemotron-3-Nano-30B-A3B
- **中文标题**: Nemotron-3-Nano-30B-A3B 的原位 Indic 分词器扩展与持续预训练
- **Authors**: Avinash Benki, Prasanjith Pasunuti, Sutanshu Saksena Raj, Parijat Chatterjee, Nayanjit Sarkar, Daksh Maan
- **Affiliation**: **gnani.ai** (NVIDIA Nemotron-3-Nano baseline)
- **Venue**: **NeurIPS 2026 GlobalSouthAI Workshop**
- **Problem background**: Adapting a large MoE LM to new languages without changing the backbone is hard; naive token addition breaks the embedding structure.
- **Key innovation**: Expanded vocabulary **in place from 131,072 → 163,072** with continued BPE + AdaptMix rebalancing, initialized new rows by averaging constituent rows, trained on 90% Indic / 10% English, then continual pretraining over **~1.27T tokens** (broad → anneal → long-context). Reports practical negative results (direct token addition < continued BPE; AdamW weight decay perturbs "frozen" rows).
- **Results / comparison**: **−38.6%** tokens per word; annealed checkpoint **+12.9** on Indic MILU but **−3.4** on English MMLU.
- **Link**: https://arxiv.org/abs/2610.15373

### 2.6 Compute-Optimal Scaling Laws for Spiking Language Models
- **中文标题**: 脉冲语言模型的计算最优 Scaling Law
- **Authors**: Dan Saunders, Benjamin Ren, Catherine He
- **Affiliation**: **Luma AI**; X School
- **Venue**: **NeurIPS 2026 AXIOM Workshop (Foundations of Efficient Deep Learning)**
- **Problem background**: Spiking LMs promise energy-efficient LM via sparse binary activations, but the efficiency-accuracy trade-off is uncharacterized at scale.
- **Key innovation**: First **Chinchilla-style IsoFLOP** study of a spiking LM, sweeping SpikeGPT-family (RWKV backbone) width 384→1536 over 3e17–1e19 FLOPs on FineWeb-EDU.
- **Results / comparison**: Compute-optimal frontier **N_opt ∝ C^0.56** (≈0.50 for dense Transformers) — spiking doesn't change the param/data trade-off; loss gap = ~0.16-nat backbone cost (compute-invariant) + a spiking cost falling 0.34→~0.23 nats then plateauing.
- **Link**: https://arxiv.org/abs/2610.15146

### 2.7 Memorization in Image Classification: Test-Set Behavior and Scaling Laws
- **中文标题**: 图像分类中的记忆：测试集行为与 Scaling Law
- **Authors**: Jeevesh Attri, Florentin Guth
- **Affiliation**: New York University (Center for Data Science); Flatiron Institute (Center for Computational Neuroscience)
- **Venue**: **NeurIPS 2026 Workshop on Neural Network Artifacts as a New Data Modality**
- **Problem background**: Understanding generalization requires understanding memorization, which is much less studied.
- **Key innovation**: Studies CNNs on randomized-label/pixel tasks. Finds independently-initialized memorizing networks learn *different* predictive functions (divergent test predictions), unlike generalizing networks; examines dataset-size effects on required capacity/time to interpolate.
- **Results / comparison**: Counter-intuitive scaling of "number of presentations needed to memorize" — memorization is not a simple lookup table.
- **Link**: https://arxiv.org/abs/2610.16090

### 2.8 RELAGRAM: Recursive Latent Graph Model for the Capacitated Vehicle Routing Problem
- **中文标题**: RELAGRAM：用于容量约束车辆路径问题的递归潜在图模型
- **Authors**: Vladimir Kirill Bickov, Neil Yorke-Smith
- **Affiliation**: Delft University of Technology
- **Venue**: **NeurIPS 2026 MLxOR Workshop**
- **Problem background**: Latent recursion (repeatedly processing internal representations through the same network) works on structured reasoning (Sudoku, mazes), but its use for *neural routing* was unclear.
- **Key innovation**: **RELAGRAM** encodes a CVRP instance as **edge tokens**; a compact Transformer recurrently updates their latents; an output head maps to an edge heatmap, and an autoregressive decoder constructs a feasible solution.
- **Results / comparison**: On CVRP-100, the **0.53M-parameter** model reaches gaps **13.4% / 9.8% / 8.3%** (greedy / 8× symmetry aug / 256-candidate); zero-shot to CVRP-500 (15.6%) and CVRP-1000 (21.7%).
- **Link**: https://arxiv.org/abs/2610.15106

### 2.9 SmolWAM: A Latent World-Action Model for Robotic Manipulation on Edge Devices
- **中文标题**: SmolWAM：面向边缘设备的机器人操作潜在世界-动作模型
- **Authors**: Timi Owolabi, Hikmah Olawore, Frances Adelakun, Ayotomiwa Oyewumi
- **Affiliation**: ML Collective
- **Venue**: **NeurIPS 2026 Robot Learning with World Models Workshop**
- **Problem background**: Strong world-action models (WAMs) rely on video diffusion transformers too heavy for edge devices.
- **Key innovation**: **SmolWAM** derives a latent WAM from the 2B-parameter **Cosmos Policy** by keeping its trunk and rebuilding the inference interface (single-frame visual latents, attention-sink-preserving cached text features, 12/28 blocks, 1,008 tokens read out in one rectified-flow step).
- **Results / comparison**: **95.5%** success on 400 LIBERO episodes at **57 ms / 2.3 TFLOP per 16-action chunk / 2.4 GiB**; **11× faster** than teacher with **18.5× fewer FLOPs** and **3.2× less memory**, trained in 3.6 GPU-hours.
- **Link**: https://arxiv.org/abs/2610.13740

### 2.10 Guarded Block Transfers for Polytope Distance: Linear Convergence with Explicit Constants and Gap-Certified Screening for SVM Training
- **中文标题**: 多面体距离的受保护块转移：显式常数线性收敛与间隙认证筛选
- **Authors**: Mayank Gupta
- **Affiliation**: Independent Researcher
- **Venue**: **NeurIPS 2026 OPT (Optimization for ML) Workshop** (poster)
- **Problem background**: Hard-margin SVM training = distance between two convex hulls, solved by the Triangle Algorithm (TA) with a certified duality gap; block MDM transfers risk instability.
- **Key innovation**: **Guarded block transfers** — aggregate k MDM transfers per scan into one exact line search, guarded by comparison with the single best transfer (cost independent of n), with an away step when capacity-clipped. Proves **global linear convergence with explicit constants** and gap-certified screening bounds.
- **Results / comparison**: Contraction is k-independent, so aggregation is provably safe while scan savings are measured.
- **Link**: https://arxiv.org/abs/2610.15829

### 2.11 Auditing VLM Benchmarks from Existing Evaluation Runs
- **中文标题**: 从已有评测运行审计 VLM 基准
- **Authors**: Denis Degtiarev, Anna Gromova, Sergey Katkov, Artem Mikhailin, Safina Mukhamedshina, Albert Nasybullin, Karina Shaikhutdinova, Artem Tuzov
- **Affiliation**: Innopolis University
- **Venue**: **NeurIPS 2026 TAE (Trust-AI-Eval) Workshop**
- **Problem background**: Evaluation runs discard per-question artifacts that could audit the benchmark itself.
- **Key innovation**: An **audit layer for VLMEvalKit** — six detectors as post-processing over saved outputs plus one text-only rerun (visual inputs removed), emitting per-question reports with permutation-null excess and interval estimates.
- **Results / comparison**: On **MMStar**, **20.2%** of questions gain zero aggregate accuracy from the image (17.0% explained by an item-matched permutation null, leaving **+3.2 pp** excess, corrected p=0.001), concentrated in math/science and absent from coarse perception.
- **Link**: https://arxiv.org/abs/2610.13548

### 2.12 Token-Budgeted Candidate Retrieval for 3D Scene-Grounded VLMs: Category Names vs. Pairwise Geometry
- **中文标题**: 3D 场景 VLM 的 token 预算候选检索：类别名 vs. 成对几何
- **Authors**: Michał Zakrzewski, Mariia Shpir, Taras Rumezhak
- **Affiliation**: AGH University of Krakow; ETH Zurich; SoftServe
- **Venue**: **NeurIPS 2026 Physical World AI Workshop**
- **Problem background**: Under a fixed context budget, which objects/relations should a 3D scene-grounded VLM see first?
- **Key innovation**: Compares **additive noun (category-name) matching** vs. **QCRR** (Query-Conditioned Relation Retrieval, a deterministic pairwise-geometry scorer) and small encoders (MiniLM, BGE-small) with a token-ratio metric on ScanRefer / Nr3D / Sr3D.
- **Results / comparison**: Noun matching reaches R@10 **0.864** on ScanRefer vs. QCRR **0.626**; MiniLM/BGE 0.911–0.913 (ScanRefer) and 0.941–0.947 (Nr3D) — category names dominate pairwise geometry at every K.
- **Link**: https://arxiv.org/abs/2610.14207

### 2.13 Exploring Jailbreak Vulnerability Across Depth-Based Dynamic Inference in Large Language Models
- **中文标题**: 探索基于深度的动态推理在大模型越狱脆弱性上的影响
- **Authors**: Lass Najmuldeen, Seyedhamidreza Mousavi
- **Affiliation**: Mälardalen University, Sweden
- **Venue**: **NeurIPS 2026 FLMSec Workshop (Foundations of Language Model Security)**
- **Problem background**: Depth-based dynamic inference enables early-exit generation for efficiency, but its effect on jailbreak-robustness was unexplored.
- **Key innovation**: Systematic study showing (1) **shallow exits are consistently more robust** to jailbreaks than deeper exits; (2) deeper exits reach lower adversarial-suffix loss (easier to optimize); (3) suffixes affect utility.
- **Results / comparison**: Efficiency and safety are coupled through exit depth — a resource-budget/attack-surface trade-off.
- **Link**: https://arxiv.org/abs/2610.15207

### 2.14 Trust Hinders Bidirectional Human–AI Alignment
- **中文标题**: 信任阻碍双向人机对齐
- **Authors**: Michaela Benk, Kacper Sokol
- **Affiliation**: University of Zurich; USI Lugano
- **Venue**: **NeurIPS 2026 BiAlign Workshop (Dynamic Alignment in Human–AI Coupled Systems)**
- **Problem background**: Trust calibration dominates AI-assisted decision-making framing but overly restricts what "deciding with AI" means.
- **Key innovation**: Develops **three dimensions** of AI-assisted decision-making: trusting AI is only one uncertainty strategy; trust calibration is misapplied to "large-world" (ill-defined) problems; such settings need higher-order decision processes.
- **Results / comparison**: Position paper arguing for process-oriented human-AI coupled systems that jointly negotiate uncertainty.
- **Link**: https://arxiv.org/abs/2610.15136

---

## 3. EMNLP 2026 — Main / Findings / Industry / Workshops (7 papers)

### 3.1 Frustratingly Easy Agentic RAG via Portable Skills: A Case Study in Customer Support
- **中文标题**: 极其简单的可移植技能式 Agentic RAG：客服案例研究
- **Authors**: Istok Bako, Bonan Min, Tiffany Shao, Claire Cheng, Yashar Mehdad
- **Affiliation**: **Airbnb, Inc.**
- **Venue**: **EMNLP 2026 Industry Track** (accepted)
- **Problem background**: Enterprise workflow automation (e.g., customer-support resolution sequencing) demands precise grounding in policy docs, usually via complex chunking/indexing/reranking pipelines.
- **Key innovation**: A **portable skill** = natural-language instruction + lightweight tools (retrieval API, format-checking scripts) + a corpus enriched with an **LLM-generated "Wikipedia-style" navigation layer**. Implementable in **1–2 engineer days**, portable across capable harnesses (e.g., Claude Code).
- **Results / comparison**: A deliberately simple alternative that performs strongly against bespoke re-ranker/rewriter/agentic-RAG infrastructure in a production deployment case study.
- **Link**: https://arxiv.org/abs/2610.14428

### 3.2 When Charts Deceive Web Agents: A Paired Benchmark for Misleading Visualization-Grounded Tasks
- **中文标题**: 当图表欺骗 Web 智能体：面向误导性可视化任务的成对基准
- **Authors**: Yisheng Li, Dongming Han, Hongkun Pan, Bingcheng Mao, Zijian Wang, Yunlong Mao, Wei Tong, Sheng Zhong
- **Affiliation**: HiThink Research; State Key Laboratory of Novel Software Technology, Nanjing University; Zhejiang University
- **Venue**: **EMNLP 2026** (Main, accepted)
- **Problem background**: Web agents consume visual evidence that is often *misleading* (charts/dashboards) without any explicit malicious instruction; misinterpretation propagates into actions.
- **Key innovation**: **MisVisAgentBench** — the first paired executable benchmark: **280 task instances in matched clean–misleading pairs** differing only in chart evidence, plus a diagnostic framework isolating misleading-induced failures from baseline difficulty and capturing execution-level effects (extra browsing steps, hesitation).
- **Results / comparison**: Across **13 vision-language Web Agents**, swapping clean charts for misleading counterparts reduces average success rate by **more than a quarter**.
- **Link**: https://arxiv.org/abs/2610.12823

### 3.3 Is the Future Predictable? Modeling Future Predictability for Reliable Temporal Reasoning
- **中文标题**: 未来可预测吗？面向可靠时序推理的未来可预测性建模
- **Authors**: Yongyi Huang, Huaping Zhang, Wenyao Cui, Qiuchi Li, Lei Li, Baohua Zhang
- **Affiliation**: Beijing Institute of Technology; Zhongguancun Academy
- **Venue**: **EMNLP 2026** (Main, accepted)
- **Problem background**: LLMs commit to specific future answers even when queried facts are inherently volatile.
- **Key innovation**: **ChronoRegime** task + **Confidence-Aware Temporal Reasoning (CTR)** framework estimating future predictability from temporal dynamics and regulating answer commitment (commits only when reconstructed evidence supports the future state).
- **Results / comparison**: Improves strict overall accuracy by **+6.7 pp** and reduces hallucination rates by **−18.4 pp** on average over a plain QA baseline.
- **Link**: https://arxiv.org/abs/2610.14073

### 3.4 GNN-CB: A Graph Neural Network Competition Benchmark for Human and LLM Evaluation
- **中文标题**: GNN-CB：面向人类与 LLM 评估的图神经网络竞赛基准
- **Authors**: Murad Hossen et al. (multi-institution collaboration; Islem Rekik, corresponding)
- **Affiliation**: Istanbul Technical University (BASIRA Lab) and 20+ collaborating institutions
- **Venue**: **EMNLP 2026** (Main, accepted)
- **Problem background**: No benchmark evaluates whether LLMs can autonomously solve **end-to-end GNN coding** tasks under realistic competition settings.
- **Key innovation**: **GNN-CB** — **18 curated competitions** spanning node/edge/graph-level prediction, evaluated through a unified automated pipeline with hidden test sets; humans solve under competition constraints, LLMs under a frozen zero-shot **plan-then-code** protocol with bounded execute-and-repair loops; supports non-agent and agent-based evaluation.
- **Results / comparison**: Reveals the gap between LLM coding/reasoning ability and graph-structured ML problem solving.
- **Link**: https://arxiv.org/abs/2610.05387

### 3.5 Sense and Sensitivity: Benchmarking LLM Clinical Triage Recommendations with Physician Experts
- **中文标题**: 敏感度与敏感性：以医师专家评测 LLM 临床分诊建议
- **Authors**: Abinitha Gourabathina, Haoran Zhang, Yuexing Hao, Walter Gerych, Marzyeh Ghassemi
- **Affiliation**: **MIT** (EECS); Worcester Polytechnic Institute
- **Venue**: **EMNLP 2026** (Findings, accepted)
- **Problem background**: LLM clinical reliability under realistic text variation is under-tested.
- **Key innovation**: A benchmark of **>6,000 clinical scenarios, 7,000 physician annotations, 225,000 model responses**, comparing LLMs to physicians under text perturbations that preserve the clinical setting.
- **Results / comparison**: LLMs recommend **unnecessary care more than physicians** at baseline (worsening under perturbation) and are **more sensitive to gender and tone perturbations** than human recommendations.
- **Link**: https://arxiv.org/abs/2609.38600

### 3.6 Counterexample Generation via Per-Theorem Symbolic Verifiers: When Imitation Hurts and Reinforcement Repairs
- **中文标题**: 基于逐定理符号验证器的反例生成：模仿有害、强化修复
- **Authors**: Omar Farouk Zouak, Houssam Eddine Boukhalfa, Soumaya Lakehal, Shiv Katiyar, Samia Nefti-Meziani
- **Affiliation**: National School of Artificial Intelligence, Algiers; University of Birmingham
- **Venue**: **EMNLP 2026 Findings** (accepted)
- **Problem background**: LLMs solve a theorem forward but fail to disprove a related false one — a *falsification gap* that SFT does not close and can worsen.
- **Key innovation**: Frames counterexample generation as **constrained witness emission** against a deterministic per-theorem Python verifier; releases **SymCE (4,707 false conjectures + executable verifiers)** where the verifier *is* the reward. Shows an **imitation trap** (counterexample-only SFT collapses true-theorem recognition 0.27→0.00) repaired by **RLVR with sparse outcome reward** (→0.66).
- **Results / comparison**: The 4B model **outperforms every evaluated 7B open-weights math model**; sparse vs. dense rewards diverge **33 points** on a held-out calibration probe.
- **Link**: https://arxiv.org/abs/2610.02444

### 3.7 Pareto-Dominant Clarification: Post-Training Coding LLMs via PPO-Lagrangian Budget Constraints
- **中文标题**: 帕累托占优的澄清：基于 PPO-Lagrangian 预算约束的编码 LLM 后训练
- **Authors**: Abhinav Rajput, Acey Vogelstein
- **Affiliation**: Center for Data Science, New York University
- **Venue**: **EMNLP 2026 LMP Workshop** (accepted)
- **Problem background**: Coding agents must decide whether to ask clarifying questions or answer directly — an accuracy-vs-efficiency trade-off; penalty methods need per-budget coefficient tuning.
- **Key innovation**: Formulates clarification as a **Constrained MDP** and post-trains **Qwen2.5-Coder-7B-Instruct with PPO-Lagrangian** under an expected question-budget constraint (evaluated on HumanEvalComm with a GPT-4o-mini oracle simulator).
- **Results / comparison**: Untuned clarification is **Pareto-inefficient** — budget-constrained policies achieve *both* higher accuracy and lower clarification rates than the baseline.
- **Link**: https://arxiv.org/abs/2610.04089

---

## 4. ICML 2026 — Main & Workshops (3 papers)

### 4.1 Rethinking Human Intent-to-CAD: Parametric CAD Model Generation via Cooperative Multi-Task Alignment and Spatial-Aware Reinforcement Learning
- **中文标题**: 重新思考人类意图到 CAD：协作多任务对齐与空间感知强化学习
- **Authors**: Qingwang Zhang, Jiahao Li, Xiangdong Zhou
- **Affiliation**: Fudan University, Shanghai
- **Venue**: **ICML 2026** (Main, PMLR Vol. 306, 43rd ICML)
- **Problem background**: Conceptual CAD modeling from incomplete/unstructured intent (hand-drawn sketches + text) is hard; prior methods assume a target CAD model exists.
- **Key innovation**: A unified method mapping **multi-level human intents directly to executable CAD code**, plus **HiCAD** — the first large-scale dataset aligning sketches, text, and parametric CAD codes. Two-stage: **Cooperative Multi-Task Alignment** (bridge heterogeneous inputs) + **Spatial-Aware RL** (enforce geometric/topological consistency).
- **Results / comparison**: Significantly outperforms existing baselines across multiple tasks, validating heterogeneous-intent→executable-code transformation.
- **Link**: https://arxiv.org/abs/2610.15681

### 4.2 Beyond Single-Model Injection: A Threat Model and Defense Architecture for Prompt Injection in Multi-Agent Systems
- **中文标题**: 超越单模型注入：多智能体系统提示注入的威胁模型与防御架构
- **Authors**: Rudrendu Kumar Paul, Sourav Nandy
- **Affiliation**: Boston University; University of Texas at Austin
- **Venue**: **ICML 2026 AIWILD Workshop** (camera-ready)
- **Problem background**: Prompt-injection research targets single-model chatbots; multi-agent systems amplify the threat (inter-agent message passing, shared tools, trust propagation).
- **Key innovation**: A threat model enumerating **14 attack vectors across four categories** (direct/indirect/inter-agent/cascading), tested against a **6-agent production-representative system**, plus four architectural defenses.
- **Results / comparison**: **67%** of agents are vulnerable to at least one scope violation even with system-prompt guardrails; indirect injection via tool outputs succeeds **43%** of the time.
- **Link**: https://arxiv.org/abs/2609.22949

### 4.3 Decision Titan: Test-Time Training for Long-Term Memory in Offline Reinforcement Learning
- **中文标题**: Decision Titan：离线强化学习中长期记忆的测试时训练
- **Authors**: Jude Waide, Robert Lieck
- **Affiliation**: Department of Computer Science, University of Durham, UK
- **Venue**: **ICML 2026 Workshop on Decision-Making from Offline Datasets to Online Adaptation**
- **Problem background**: Long-term dependencies challenge sequential decision-making (RNN vanishing gradients; Transformer quadratic attention).
- **Key innovation**: Augments a **Decision Transformer with Test-Time Training (TTT) layers** ("Decision Titan"), storing episodic memories in network parameters via gradient descent at train and test time; analyzes memory on the **X-Maze** environment (an extended T-Maze).
- **Results / comparison**: First application/analysis of TTT to offline RL, dissecting how the memory mechanism learns.
- **Link**: https://arxiv.org/abs/2610.01513

---

## 5. ICLR 2027 — Under Review (6 papers)

### 5.1 PANINI-DR: Controlled Deep Research through Generative Semantic Workspaces
- **中文标题**: PANINI-DR：通过生成式语义工作空间的受控深度研究
- **Authors**: M. Yigit Turali, Shreyas Rajesh, M. Efe Lorasdagi, Chenda Duan, Kartik Sharma, Vwani Roychowdhury
- **Affiliation**: University of California, Los Angeles
- **Venue**: **ICLR 2027** (under review)
- **Problem background**: Deep research must connect search/reasoning/computation steps while maintaining state across model calls and checking findings before errors propagate.
- **Key innovation**: **PANINI-DR** — a multi-agent harness separating investigation coordination from per-subquestion research and **verification**, built on a **Generative Semantic Workspace** representation recording subquestions, dependencies, findings, and evidence.
- **Results / comparison**: On **BrowseComp-Plus, FRAMES, MoNaCo** vs. **seven SOTA deep-research harnesses** with a shared backbone and frozen corpora, achieves the strongest average per-question performance.
- **Link**: https://arxiv.org/abs/2610.15208

### 5.2 Co-adaptive Rule Routing and Constraining for Structured Knowledge Retrieval (CoRE)
- **中文标题**: 结构化知识检索的协同自适应规则路由与约束（CoRE）
- **Authors**: Zhisheng Qi, Haoyu Han, Jiaxi Li, Bing He, Huiyuan Chen, Franck Dernoncourt, Ryan A. Rossi, Mahantesh M. Halappanavar, Jin Lu, Yu Zhang, Tianming Liu, Yu Wang
- **Affiliation**: University of Georgia; Michigan State University; Georgia Institute of Technology; **Amazon**; **Adobe Research**; **PNNL**; Texas A&M University
- **Venue**: **ICLR (under review)**
- **Problem background**: Structured knowledge retrieval relies on predefined query-rule supervision (author–paper, anatomy–drug) rarely available in practice.
- **Key innovation**: **CoRE** jointly learns *which reasoning rule* to assign each query and *how to retrieve* under it, with **no predefined query-rule pairs**: a routing agent selects a rule, its retriever traverses the KB. Routing (RL) and retrieval (contrastive) alternate in a closed loop.
- **Results / comparison**: Closed-loop co-adaptation yields supervision from selected rules while retrieval performance rewards the router.
- **Link**: https://arxiv.org/abs/2610.14465

### 5.3 Limitations on Autoregressive Token Generation via Sequential Sampling
- **中文标题**: 通过序列采样对自回归 token 生成的局限性
- **Authors**: Gal Arnon, Andrej Bogdanov, Paul Lou, Giulio Malavolta, Alon Rosen, Lorenzo Taschin
- **Affiliation**: **NTT Research**; University of Ottawa; Bocconi University
- **Venue**: **ICLR 2027** (in submission)
- **Problem background**: Formalizing autoregressive generation as **sequential samplers** (next symbol given previous ones + small state).
- **Key innovation**: Shows (1) a k-bit-state sequential sampler is simulable by a stateless one at **~O(2^k)** size overhead; (2) **insertional sampling** is strictly more powerful than fixed-order sequential sampling; (3) small-state sequential samplers **cannot establish covert cryptographic channels**.
- **Results / comparison**: With the Vadhan–Zheng pseudentropy duality, characterizes efficient small-state sequential sampleability; result (3) offers a **safety mechanism against subliminal coordination among malicious LLM agents**.
- **Link**: https://arxiv.org/abs/2610.14615

### 5.4 PopGen: Generating Semantically Diverse Populations for Zero-Shot Coordination
- **中文标题**: PopGen：为群体多样性生成语义多样的种群以实现零样本协作
- **Authors**: Paul Teiletche, Kanghyun Ryu, Kyungjoon Park, Dhruva Tirumala, Markus Wulfmeier, Negar Mehr
- **Affiliation**: EPFL; UC Berkeley; Yonsei University; **Google DeepMind**; Nomagic
- **Venue**: **ICLR 2027** (submitted)
- **Problem background**: Zero-shot coordination needs exposure to diverse partners, but trajectory-level diversity proxies mislabel distinct trajectories of the *same* strategy as diverse.
- **Key innovation**: **PopGen** uses LLMs' ability to describe behaviorally distinct agents: generate a diverse set of textual behavior descriptions, then translate each into an executable **code policy**.
- **Results / comparison**: Cooperators trained against PopGen populations achieve robust zero-shot cooperation with unseen partners, beating population-play baselines on four collaborative environments; semantic diversity scales with population size.
- **Link**: https://arxiv.org/abs/2610.15969

### 5.5 PotentialEP: Backprop-Free Training of CIFAR-Scale Generative Models via Equilibrium Propagation
- **中文标题**: PotentialEP：通过平衡传播实现 CIFAR 规模生成模型的无反向传播训练
- **Authors**: Alex Gower
- **Affiliation**: University of Cambridge; **Nokia Bell Labs**
- **Venue**: **ICLR 2027** (under review)
- **Problem background**: Diffusion/flow generation integrates a velocity field for hundreds of steps — poor for GPUs but ideal for analog neuromorphic substrates where one physical relaxation replaces the sequence. Energy Matching supplies a relaxation-based sampler but obtaining its gradient needs a backward pass per step.
- **Key innovation**: Proves a **predictive coding network with a single linear injection term** relaxes to a state whose visible layer inherently carries the Energy Matching gradient (error vanishing for small injection). An Energy-Matching model trained by backprop can be loaded unchanged and sampled by relaxation alone.
- **Results / comparison**: Enables **backprop-free** CIFAR-scale generative modeling, matching the original model's samples.
- **Link**: https://arxiv.org/abs/2610.14409

### 5.6 CRJudgeBench: Can AI Detect Plausible but Invalid Code Reviews?
- **中文标题**: CRJudgeBench：AI 能否识别看似合理但错误的代码评审？
- **Authors**: Yue Pan, Jiawei Li, Ziyuan Zhang, Xiangxin Zhao, He Ye
- **Affiliation**: University College London; **Amazon**; Zhejiang University
- **Venue**: **ICLR 2027** (under review)
- **Problem background**: LLMs generate plausible review comments whose *core technical claims* may be wrong; existing benchmarks evaluate generation/issues, not per-comment trustworthiness judgment.
- **Key innovation**: **CRJudgeBench** — **1,199 instances** from real PRs + expert-verified perturbations (trustworthy vs. plausible-but-untrustworthy), plus **Sentinel**, a repository-grounded agentic judge that gathers code evidence before judging (trained from Qwen3-Coder-30B-A3B via iterative action-level learning).
- **Results / comparison**: Directly measures technical-trustworthiness judgment with active evidence gathering.
- **Link**: https://arxiv.org/abs/2609.37216

---

## 6. Other Venues (2026) — WWW · CVPR · AAAI · CIKM · ICLR 2026 Workshops · RecSys · AACL (9 papers)

### 6.1 Fine-Tuning Strategy, Not Just Data: A Statistically Rigorous Audit of Gender and Stereotypical Bias in Embedding Models for HR Recommendation Systems
- **中文标题**: 微调策略而非仅数据：HR 推荐系统中嵌入模型性别与刻板印象偏差的严格审计
- **Authors**: Ekta Yadav
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: **RecSys in HR '26** (6th Workshop on Recommender Systems for Human Resources)
- **Problem background**: Embedding models underpin job–candidate matching; any social bias feeds directly into HR recommendations.
- **Key innovation**: Audits **six multilingual sentence-embedding models** (LaBSE/E5 family, public + custom fine-tuned) on Bias-in-Bios and StereoSet, treating **statistical validity as first-class**: identifies a non-independence error inflating a 0.0046 mean difference to p≈0, replacing it with a profession-level paired Wilcoxon test, individual-resampling bootstrap CIs, and permutation tests.
- **Results / comparison**: Under corrected methodology, **knowledge-distillation fine-tuning of E5-Base significantly increases measured occupational-gender bias** (Δ=−0.177, p<1e−8) — i.e., the *fine-tuning strategy*, not just data, drives bias.
- **Link**: https://arxiv.org/abs/2610.14579

### 6.2 SAFE-KV: Causal Suffix Repair for Behavior-Preserving Non-Prefix KV Cache Reuse in RAG
- **中文标题**: SAFE-KV：面向 RAG 中非前缀 KV 缓存复用的因果后缀修复
- **Authors**: Xingjian Zhang
- **Affiliation**: Carnegie Mellon University
- **Venue**: **Findings of AACL-IJCNLP 2026** (accepted)
- **Problem background**: RAG reuses documents across requests, making non-prefix KV-cache reuse attractive — but a cached document state is a *context-conditioned causal state*, not reusable text.
- **Key innovation**: Formulates non-prefix KV reuse as a **behavior-preservation problem** (reference = full prefill) and introduces **SAFE-KV**, which repairs a composed cache by re-encoding the causal suffix from a selected start document (risk-guided K2 selection).
- **Results / comparison**: On Qwen2.5-7B-Instruct, prefix-conditioned composition preserves only **47.2% (HotpotQA-500) / 37.8% (2Wiki-500)** of full-prefill answers; SAFE-KV restores **99.8% / 98.4%** (donor-copy) and **100.0% / 98.4%** (actual suffix forwarding). Reuse without repair is exact up to four documents and degrades at sixteen.
- **Link**: https://arxiv.org/abs/2610.15186

### 6.3 REPRO: Reflective Evolutionary Prompt Optimizer for Automated LLM Red-Teaming
- **中文标题**: REPRO：面向自动化 LLM 红队的反思式进化提示优化器
- **Authors**: Abrar Alotaibi, Moataz Ahmed
- **Affiliation**: King Fahd University of Petroleum & Minerals; Imam Abdulrahman Bin Faisal University, Saudi Arabia
- **Venue**: **ACM TOSEM** (under review)
- **Problem background**: Automated red-teaming either needs privileged access, manual per-model templates, or optimizes a single objective without population diversity.
- **Key innovation**: **REPRO** — a **pure black-box** framework driven entirely by a compressed 7B reflective model on a **single consumer GPU**, with two mechanisms: **semantic crossover** (LLM-guided multi-parent recombination) and **Bayesian strategy selection via Thompson Sampling** from structured failure analysis.
- **Results / comparison**: Cataloged on **AdvBench, JailbreakBench, HarmBench** across **36 target models from 11 families** (incl. GPT-5-nano, Claude-3.5-Sonnet, Gemini-2.5-Pro, Grok-4.1); reaches **100% ASR** under the study protocol.
- **Link**: https://arxiv.org/abs/2610.15513

### 6.4 Safe Context Switching for Agents in the Wild: Mitigating Subspace Interference via Orthogonal Adaptation (AURA)
- **中文标题**: 野外智能体的安全上下文切换：通过正交适配缓解子空间干扰（AURA）
- **Authors**: Akash Das, Ishan Roy
- **Affiliation**: **Fidelity Investments**
- **Venue**: **ICLR 2026 2nd Workshop on World Models**
- **Problem background**: High-variance internal states for CoT deduction geometrically interfere with latent safety representations — **Sequential Subspace Interference**.
- **Key innovation**: Quantifies a **23.3% interference penalty** on alignment benchmarks from fine-tuning on math/code (Reasoning Drift), then proposes **AURA (Adaptive Unique Residual Allocation)**, a **spectral regularization** framework enforcing spectral independence between task and safety subspaces.
- **Results / comparison**: Mitigates reasoning-induced safety-prior degradation that standard adaptation misses.
- **Link**: https://arxiv.org/abs/2610.05219

### 6.5 Look Before You Leap: Thermodynamic Arbitration of Parametric and Non-Parametric Knowledge in LLM Agents (MARTA)
- **中文标题**: 三思而后行：LLM 智能体中参数与非参数知识的热力学仲裁（MARTA）
- **Authors**: Akash Das, Ishan Roy
- **Affiliation**: **Fidelity Investments**
- **Venue**: **ICLR 2026 Workshop on Latent & Implicit Thinking — Beyond CoT Reasoning**
- **Problem background**: The "Retrieve-Always" paradigm forces agents to distrust internal knowledge ("induced amnesia") — thermodynamically wasteful and cognitively fragile.
- **Key innovation**: **MARTA (Metacognitive Adaptive Retrieval and Thought Architecture)** — a neuro-symbolic framework arbitrating between parametric and non-parametric knowledge via a metacognitive "look before you leap" policy.
- **Results / comparison**: Reduces reflexive retrieval dependence, avoiding wasteful external checks on internal-knowledge questions.
- **Link**: https://arxiv.org/abs/2610.05223

### 6.6 Riemannian Graph Tokenizer for Structural Knowledge Transfer
- **中文标题**: 面向结构知识迁移的黎曼图分词器
- **Authors**: Qimin Zhou, Haibo Liu, Yujie Wang, Li Sun, Chuan Shi
- **Affiliation**: Beijing University of Posts and Telecommunications (BUPT), China
- **Venue**: **WWW 2026** (The ACM Web Conference, Dubai, accepted; DOI 10.1145/3774904.3792120)
- **Problem background**: Text tokenizers are well studied, but graph tokenizers remain early-stage — struggling with non-Euclidean structure and structural semantics.
- **Key innovation**: **Riemannian Graph Tokenizer (RGT)** bridges structural knowledge and quantized representations using **Riemannian geometry**, defining a **geometric vocabulary** (trees, cycles, sequences) capturing fundamental structural patterns for cross-domain transfer.
- **Results / comparison**: Enables cross-domain structural knowledge transfer for graph foundation models.
- **Link**: https://arxiv.org/abs/2610.15427

### 6.7 Robust Detection of Directional Adversarial Attacks in Deep Neural Networks for Radiological Imaging
- **中文标题**: 面向放射影像的深度神经网络定向对抗攻击鲁棒检测
- **Authors**: Tristan Malatyński, Joanna Jaworek-Korjakowska
- **Affiliation**: AGH University of Kraków, Poland (Center of Excellence in AI)
- **Venue**: **CVPR 2026 Workshops (SAIAD)**, open access
- **Problem background**: Medical DNNs are highly vulnerable to adversarial perturbations (studies show >90% success on medical scans), risking missed cancers/false positives.
- **Key innovation**: Uses **subsequent random-noise attacks** and analysis of **Sigmoid-function variation** to detect and determine the **directionality** of adversarial perturbations.
- **Results / comparison**: A detection framework distinguishing genuine from adversarially manipulated medical images without requiring the attacker's method.
- **Link**: https://arxiv.org/abs/2610.15628

### 6.8 Architectural Robustness to Label Noise Using Variational Quantum Circuits for Medical Image Classification
- **中文标题**: 基于变分量子电路的医学图像分类标签噪声架构鲁棒性
- **Authors**: Yasoda Lasiru Ariyarathna Epa, Yaseema Rusiru Ariyarathna Epa, Sandaru Liyanaarachchi, Kavindu Jayathissa, Kalana G. Abeywardena, Kithmin Wickremasinghe, Theshani Nuradha Piliththuwasam Gallage, Chamira U. S. Edussooriya
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: **AAAI 2026 Fall Symposium Series — 2nd Symposium on Quantum Information & Machine Learning (QIML)**
- **Problem background**: Label noise (observer disagreement, ambiguous cases) causes memorization at the cost of generalization; existing fixes assume the noise rate is known.
- **Key innovation**: Achieves robustness **architecturally** — routing a frozen backbone's features through a low-dimensional bounded bottleneck into a **variational quantum circuit** (angle encoding + linear cost) whose function class is intrinsically smooth; couples with higher-resolution inputs despite few NISQ qubits.
- **Results / comparison**: Reduces dependence on noise-rate estimation and training complexity.
- **Link**: https://arxiv.org/abs/2610.16153

### 6.9 A Multi-Dimensional Score for Detecting Lesser-Known Points of Interest in Mountain Regions
- **中文标题**: 用于检测山区冷门兴趣点的多维评分
- **Authors**: Adriana Pompejano, Sébastien Laborie, Maxime Masson, Christian Sallaberry, Philippe Roose
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: **CIKM 2026 STM4KD Workshop** (Rome, Nov 2026)
- **Problem background**: Overtourism concentrates demand on iconic sites; hidden-gem POIs are hard to detect and existing scores rely on narrow commercial indicators.
- **Key innovation**: A **multi-dimensional score** characterizing mountain POIs holistically (going beyond photo/review/like counts and avoiding proprietary sources or memory-biased questionnaires) to redistribute tourism demand.
- **Results / comparison**: Supports spatially and temporally redistributing tourism demand and valuing underrepresented heritage.
- **Link**: https://arxiv.org/abs/2610.13467

---

## 7. Recommendation · Search · Advertising · CTR Lane (6 un-venued papers)

> ⚠️ **CTR vacancy.** Zero explicit papers with "click-through rate" / "CTR prediction" / "click-through" surfaced in this block. The industrial CTR *architecture* lane (scaling laws, long-sequence modeling) is **empty again**, as it has been across the last several digests (§16). The rec/search lane below is the whole of this window's coverage.

### 7.1 Toward Explainability in Multimodal Recommendation
- **中文标题**: 面向多模态推荐的可解释性
- **Authors**: Chen Liang, Jinghui Li, Xiuze Zhou, Zongyue Wang, Yuanguo Lin, Han Yu
- **Affiliation**: Jimei University, China; Hong Kong University of Science and Technology (Guangzhou); Nanyang Technological University, Singapore
- **Venue**: *(preprint; 19 pages)*
- **Problem background**: Multimodal recommenders alleviate sparsity/cold-start but cross-modal representations create interpretability challenges; methods and criteria are fragmented.
- **Key innovation**: Taxonomy into **modality explanation** vs. **post-hoc explanation** by timing/manner, each with a progressive system; synthesizes **four categories of evaluation metrics** (objective + subjective perception) and reviews datasets by domain/source.
- **Results / comparison**: A unified conceptual framework for multimodal-recommendation explainability + future directions.
- **Link**: https://arxiv.org/abs/2610.15484

### 7.2 Retrieving Complementary Evidence for Multi-Hop RAG with Semantic Gain Graphs (SG²RAG)
- **中文标题**: 用语义增益图检索多跳 RAG 的互补证据（SG²RAG）
- **Authors**: Zeliang Li, Xiaofen Xing, Kailing Guo, Xiangmin Xu
- **Affiliation**: South China University of Technology; Foshan University
- **Venue**: *(preprint)*
- **Problem background**: Multi-hop RAG must find documents whose evidence is useful *in combination*; query relevance and graph connectivity don't measure a document's *additional* contribution given another.
- **Key innovation**: **SG²RAG** represents this complementarity via **semantic gain** — an LLM offline assesses the relevant, nonredundant information one chunk contributes given another within similarity-proposed neighborhoods, aggregated into a reusable **Semantic Gain Graph**; online, controlled **Personalized PageRank** ranks complementary evidence.
- **Results / comparison**: On MuSiQue, 2Wiki, HotpotQA with two LM backbones, best average **EM, F1, Recall@10** among single-retrieval methods under identical support/propagation.
- **Link**: https://arxiv.org/abs/2610.15285

### 7.3 Faithful Query Resolution for Conversational Search
- **中文标题**: 会话式搜索中的忠实查询解析
- **Authors**: Saber Zerhoudi, Ivica Kostric, Jelena Mitrović
- **Affiliation**: University of Passau, Germany; University of Stavanger, Norway
- **Venue**: *(iKAT SCAI 2026 challenge submission)*
- **Problem background**: Conversational query rewriting adds context but can introduce an information need the user never expressed — a query-fidelity vs. retrieval-breadth tension.
- **Key innovation**: A **minimal-faithful resolver** preserving user wording plus **weighted reciprocal rank fusion** combining it with a learned rewriter and the raw utterance, in a behavior-adaptive assistant (BM25 + SPLADE).
- **Results / comparison**: Best weighted config reaches **nDCG@5 = 0.534** (**+5.3%** relative over the strongest alternative) across five iKAT SCAI 2026 submissions.
- **Link**: https://arxiv.org/abs/2610.15034

### 7.4 The Company a Question Keeps: Auditing Open Jev-Style Models for Retrieval
- **中文标题**: 问题所伴之上下文：审计开放 Jev 式检索模型
- **Authors**: Jianbo Chen
- **Affiliation**: Tsinghua University, Beijing
- **Venue**: *(preprint; 15 pages)*
- **Problem background**: Jev-style interfaces evaluate typed questions against shared evidence; request independence is assumed but unverified.
- **Key innovation**: Audits seven open Jev-style checkpoints on **276 constructed three-passage states from 92 TREC queries**, with paired interventions separately changing requested questions, displayed evidence, and candidate eligibility; traces flips to schema-field serialization via field masking.
- **Results / comparison**: Request expansion induces strict binary flips in **9.1%/8.0%** of Nimble's judgments and changes **21.4%/18.9%** of selection-or-abstention actions; all 70 request-set flips trace to schema fields in the scoring prompt — an audit of retrieval-model robustness.
- **Link**: https://arxiv.org/abs/2610.14631

### 7.5 EVISTA: Unified Multimodal Video Search with Evidence-Aware Temporal Path Optimization
- **中文标题**: EVISTA：证据感知时序路径优化的统一多模态视频搜索
- **Authors**: Minh-Huy Tran, Van-Thinh Vo, Minh-Khoi Nguyen, Duy-Tan Nguyen, Anh-Quan Nguyen-Tran, Loi Nguyen Khanh
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: *(Ho Chi Minh City AI Challenge 2026 system, 15 pages)*
- **Problem background**: Locating multiple temporally-ordered events from one video is hard when events are described by different evidence types (visual, on-screen text, speech).
- **Key innovation**: **EVISTA** integrates visual-semantic, OCR, ASR, object, and metadata search over a shared keyframe index, plus **TEMPO-P**, an evidence-aware temporal path optimization that aggregates candidate videos across events/modalities and jointly scores keyframes.
- **Results / comparison**: Overcomes two limitations of independent event retrieval (missed videos from weak single-event retrieval; temporally inconsistent candidates) — a competition search system.
- **Link**: https://arxiv.org/abs/2610.14510

### 7.6 Do Personalized LLMs Need the Whole Conversation? Matching the Full History with Only 5% of Its Text via Relevance-Filtered Context
- **中文标题**: 个性化 LLM 需要完整对话吗？用 5% 文本的关联过滤上下文匹配完整历史
- **Authors**: Erika Hayashi, Andrew Shin
- **Affiliation**: Keio University, Japan
- **Venue**: *(preprint)*
- **Problem background**: Passing entire conversation histories to LLMs is costly — and unnecessary.
- **Key innovation**: **Sentence-level retrieval** builds a relevance-filtered context ranked by similarity to the current request, stopping at a fixed budget.
- **Results / comparison**: On PersonaMem-v2 (180 questions) with GPT-5.6-terra and Claude Opus 5.5 judges, matches full-history accuracy with **5% of the text** (~**20×** input reduction); an oracle given only the relevant evidence **beats full history by 15.6 points**.
- **Link**: https://arxiv.org/abs/2610.14952

---

## 8. Agent Systems (5 un-venued papers)

### 8.1 WorkBorne: Discovering Agentic Tasks from Real-World Artifact Transitions
- **中文标题**: WorkBorne：从真实工件转换中发现智能体任务
- **Authors**: Junyi Zhou, Yufei Wang, Qiyuan Zhang, Chuhan Wu, Zhengxi Li, Wentao Zhao, Jie Zhou, Le Tian, Xiao Zhou, Chen Ma
- **Affiliation**: City University of Hong Kong; **WeChat AI, Tencent**; MBZUAI
- **Venue**: *(preprint; 27 pages)*
- **Problem background**: Terminal agents need synthetic tasks coupling complex instructions with authentic environments, but instruction-oriented synthesis fabricates low-fidelity environments while resource-oriented methods degrade instructions to trivial operations.
- **Key innovation**: **WorkBorne** uses **artifact transitions** as the central primitive — each transition specifies who performs the task, which artifacts anchor the initial/final states, and their relationship — discovering non-trivial transitions from iteratively-retrieved artifact corpora.
- **Results / comparison**: Produces coherent, diverse, real-environment long-horizon terminal tasks without the fidelity/instruction trade-off of prior synthesis.
- **Link**: https://arxiv.org/abs/2610.14915

### 8.2 Does Failure Feedback Direct Agent Self-Modification?
- **中文标题**: 失败反馈是否引导智能体的自我修改？
- **Authors**: Rong He
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: *(preprint; 28 pages)*
- **Problem background**: Self-improving agents revise code/instructions from failure feedback, but gains after *selection* don't establish target-specific repair or generalization.
- **Key innovation**: Measures **directedness** by comparing repair of a randomly selected target failure vs. the parent's other failures across **145 eligible modifications in public Darwin Gödel Machine logs**; adds controlled instruction-revision experiments with pre-specified analysis plans.
- **Results / comparison**: **No detectable target-specific advantage** in the DGM logs; target feedback raised repair **+20 pp** for Qwen3-4B (not significant for Phi-4-mini, +7); held-out gains were concentrated where failure mechanisms were identifiable/repairable.
- **Link**: https://arxiv.org/abs/2610.14662

### 8.3 Lumen-bench: Cross-Lingual Safety Gaps and the Say-Do Problem in Tool-Calling Large Language Models
- **中文标题**: Lumen-bench：工具调用大模型中的跨语言安全缺口与言行不一问题
- **Authors**: Giovana Kerche Bonás, Thiago Laitz, Thales Sales Almeida, João Guilherme Alves Santos
- **Affiliation**: Tropic AI; Maritaca AI
- **Venue**: *(preprint)*
- **Problem background**: With executable tools, what a model *does* can diverge from what it *says* — a "say-do" gap invisible to English-only evaluations.
- **Key innovation**: **Lumen-bench** — a behavioral benchmark of tool-calling ethics: **30 models, 5 languages** (Portuguese, English, Spanish, Mandarin, Hindi), **108 Portuguese-authored scenarios, 6 social-pressure conditions, 2 system prompts, 21 generic tools, 194,400 trials**, judged by a calibrated reasoning-model judge (κ=0.78) + sandbox replay.
- **Results / comparison**: Supports **higher harmful-action rates in Hindi/Portuguese than English** under the ethical prompt — cross-lingual safety gaps in *action*, not just speech.
- **Link**: https://arxiv.org/abs/2610.15134

### 8.4 Sequent-Prover: Training Agents for Formal, Checkable SMT-based Reasoning
- **中文标题**: Sequent-Prover：训练面向形式化可验证 SMT 推理的智能体
- **Authors**: Debargha Ganguly, Weicong Chen, Mohsen Hariri, Vikash Singh, Sreehari Sankar, Shouren Wang, Wang Yang, Biyao Zhang, Chaoda Song, Alexander Nemecek, Kai Ye, Osama Zafar, Erman Ayday, Joe Stubbs, Srinivasan Iyengar, Vipin Chaudhary
- **Affiliation**: Case Western Reserve University; UT Austin; **Microsoft Research**
- **Venue**: *(preprint)*
- **Problem background**: Verifier-using agents must reason in a checkable substrate; solver success alone doesn't guarantee semantic faithfulness.
- **Key innovation**: Agents reason in an **executable SMT-LIB scratchpad** (write programs, query Z3, inspect feedback, repair, terminate). Recipe: **verifier-conditioned trajectory distillation** — sample multi-turn trajectories from a noisy teacher, keep the successful tail (correct, non-trivial, grounded, executable), then SFT + trajectory-level preference optimization. Evaluates accuracy, k-sample reliability, and SMT program quality.
- **Results / comparison**: Across **37 benchmarks / 7,254 problems per family**, the 4B model rises **85.6% → 97.0%** per-attempt accuracy and pass⁴ **64.1% → 91.7%**, cutting SMT calls **4.10 → 2.52** and tokens/attempt **18.97k → 12.72k**.
- **Link**: https://arxiv.org/abs/2610.15258

### 8.5 AlphaPilot: Multi-Turn Tool-Using LLM Agents for Adaptive Alpha Mining with Reinforcement Learning
- **中文标题**: AlphaPilot：面向自适应因子挖掘的多轮工具使用 LLM 智能体强化学习
- **Authors**: Peiqi Jiang, Fan Zhang, Xin Xu, Tianhao Chen, Can Yang
- **Affiliation**: Department of Mathematics, Hong Kong University of Science and Technology
- **Venue**: *(preprint; 25 pages)*
- **Problem background**: Formulaic alpha mining needs simultaneous processing of market text, historical data, and quantitative evaluation — most methods exploit only a subset.
- **Key innovation**: **AlphaPilot** — an RL framework training **multi-turn tool-using LLM agents** that condition on market descriptions, propose factor expressions, query a real-data evaluator, and update a retained factor pool; performs day-by-day search at inference to adapt to regime shifts.
- **Results / comparison**: OOS rolling backtests on CSI300/CSI500 across three runs: mean total returns **42.93% / 54.19%**, Sharpe **2.46 / 2.86**, highest mean total return, Sharpe, and RankIC among compared methods.
- **Link**: https://arxiv.org/abs/2610.15488

---

## 9. Code Execution, Program Synthesis & Symbolic Reasoning (2 un-venued papers)

### 9.1 Reels-RSI: Program-Level Self-Improvement for Code-Rendered Explainer Videos
- **中文标题**: Reels-RSI：面向代码渲染解说视频的程序级自我改进
- **Authors**: Wei Lin
- **Affiliation**: Agentic Loops X (independent)
- **Venue**: *(preprint; open-source)*
- **Problem background**: Explainer videos are usually treated as pixel-generation targets, but they are better seen as **programs** (script + storyboard + per-frame animation code) that a deterministic renderer turns into frames — programs can be read, diffed, tested, audited.
- **Key innovation**: An open-source reel director for any agent harness whose **self-improvement happens at the program level** (not weights/prompts): each revision is logged with a code snapshot; retrospectives compile catchable lessons into unit-tested rules; a benchmark-gated step lets an agent rewrite its playbook only when blind pairwise judgments on held-out topics prefer it.
- **Results / comparison**: Across **111 reels**, a field study of program-level self-improvement with human-gated memory.
- **Link**: https://arxiv.org/abs/2610.14495

### 9.2 MoSAIC: Learning DAG Scheduling Heuristics from Optimal Schedules through Motif-Aware Recovery and LLM-Guided Reasoning
- **中文标题**: MoSAIC：通过模体感知恢复与 LLM 引导推理从最优调度学习 DAG 调度启发式
- **Authors**: Shiva Ahir, Hashmath Shaik, Alex Doboli, Nadeem Yaseen, Simona Doboli
- **Affiliation**: Stony Brook University; Barcelona Supercomputing Center; Hofstra University
- **Venue**: *(preprint)*
- **Problem background**: Efficient task scheduling on heterogeneous computing is hard; exact solvers don't scale, heuristics don't generalize.
- **Key innovation**: **MoSAIC** uses **OR-Tools CP-SAT optimal schedules to supervise** compact priority-based scheduling functions learned by Bayesian Optimization, with LLM-guided reasoning bridging DAG structures and priority functions; builds a reusable knowledge base across DAG instances.
- **Results / comparison**: Consistent improvements on synthetic families and real benchmarks (PolyBench, MachSuite).
- **Link**: https://arxiv.org/abs/2610.15205

---

## 10. LLM Post-Training · RL · Reasoning (3 un-venued papers)

### 10.1 Reward-Aligned Distillation (RAD)
- **中文标题**: 奖励对齐蒸馏（RAD）
- **Authors**: Yilan Chen, Zian Su, Manish Prajapat, Dingmin Wang, Rein Houthooft, Rui Song, Vijay Lingam
- **Affiliation**: UC San Diego; Purdue University; **AWS AI Labs**; **Amazon**
- **Venue**: *(preprint)*
- **Problem background**: RLVR improves reasoning but is expensive; on-policy distillation (OPD) provides dense token supervision but distills *every* token regardless of whether the teacher's preference improves reward; existing token-selection proxies (uncertainty, divergence) need not identify reward-improving supervision.
- **Key innovation**: **RAD** — a **bilevel** framework weighting distillation signals by their predicted effect on the student's post-update reward; differentiates through a temporary optimizer step to score each token, then updates token weights by projected ascent. Weights can strengthen, suppress, or *reverse* individual distillation-gradient contributions.
- **Results / comparison**: At matched training-response budget, improves mean accuracy on **six competition-math benchmarks** over strong OPD baselines.
- **Link**: https://arxiv.org/abs/2610.14572

### 10.2 Uniform Information Density-Based Preference Optimization (UIDPO)
- **中文标题**: 基于均匀信息密度的偏好优化（UIDPO）
- **Authors**: Yongyuan Li, Yang Xu
- **Affiliation**: Southern University of Science and Technology, Shenzhen
- **Venue**: *(preprint)*
- **Problem background**: Preference-optimization algorithms use chosen/rejected pairs, but human preferences are complex; recent work imports linguistic assumptions into the optimization direction.
- **Key innovation**: **UIDPO** adopts the psycholinguistic **Uniform Information Density** theory — humans prefer language with uniformly distributed information (less processing effort) — implementing it via a compound metric combining global standard deviation and local second-order difference.
- **Results / comparison**: Guides preference optimization with an information-theoretic, cognitively-grounded criterion.
- **Link**: https://arxiv.org/abs/2610.14578

### 10.3 Predicting How Model Propensities Generalize Out of Distribution
- **中文标题**: 预测模型倾向如何在分布外泛化
- **Authors**: June Hunter, Lily Wen, Owen Terry, Johannes Taraz, Ben Cohen, Niels Warncke (mentor)
- **Affiliation**: *(affiliation not recovered from arXiv HTML; appears to be a research-program cohort)*
- **Venue**: *(preprint; 29 pages)*
- **Problem background**: Alignment wants models that behave well in new contexts; OOD generalization of *propensities* is central.
- **Key innovation**: A **cross-elicitation matrix** methodology: use system prompting, few-shot, SFT, and GRPO to raise a target propensity, then measure spillover onto others. Finds **spillover is highly correlated between models when the same elicitation technique is used**, but SFT and GRPO induce different spillover profiles; elicitation of benign traits can generalize toward undesired traits (e.g., "sentient" claims → power-seeking); spillover partially resembles human trait correlations (three clusters ≈ half the variance).
- **Results / comparison**: Provides a predictive handle on how alignment-relevant propensities transfer.
- **Link**: https://arxiv.org/abs/2610.14937

---

## 11. Sequential Modeling · Long-Context · Efficiency (2 un-venued papers)

### 11.1 FidelityQ: Preserving Predictive Fidelity in Ultra-Low-Bit Language Model Quantization
- **中文标题**: FidelityQ：在超低位量化中保持语言模型的预测保真度
- **Authors**: Yujie Chen, Weiyan Zheng, Yiwu Yao, Tianchi Hu, Bo Wang, Jiyu Guo, Wenzhan Li, Jingcai Guo, Michele Magno, Haotong Qin
- **Affiliation**: The Hong Kong Polytechnic University; **Huawei Technologies Ltd.**; University of Hong Kong; Sun Yat-sen University; ETH Zurich
- **Venue**: *(preprint)*
- **Problem background**: Ultra-low-bit scalar quantization keeps regular arithmetic but preserving *predictive behavior* from a small calibration set is hard.
- **Key innovation**: **FidelityQ** preserves predictive fidelity down to **2 bits** via **Information-Aligned Analytic Coding (IAC)** — randomized Hadamard mixing shapes each weight row toward a centered symmetric source, then a mirrored four-level minimum-distortion quantizer is fitted; every level set decomposes into two sign-valued bases with scales (lookup-free decoding compatible with scaled integer arithmetic). Residual discrepancies are heavy-tailed and concentrated on confident-teacher tokens, motivating a targeted correction.
- **Results / comparison**: Preserves predictive behavior at extreme precision where prior scalar schemes degrade.
- **Link**: https://arxiv.org/abs/2610.14934

### 11.2 Learnable Low-Rank Polynomial Sketch for Effective Linear Attention (LLoPS)
- **中文标题**: 面向高效线性注意力的可学习低秩多项式素描（LLoPS）
- **Authors**: Zongyue Qin, Haoran Deng, Jason Cong, Yizhou Sun
- **Affiliation**: University of California, Los Angeles
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: Linear attention replaces softmax to enable linear-time computation; polynomial kernels are effective but high-degree polynomial kernels are infeasible in high dimension, so prior work uses approximate kernels with non-negligible error.
- **Key innovation**: Shows existing linear-attention methods are suboptimal from the polynomial-kernel-approximation view and proposes **LLoPS** — a principled, flexible framework approximating polynomial kernels via a **learnable low-rank sketch**.
- **Results / comparison**: Reduces approximation error vs. prior approximate polynomial kernels while enabling long-context linear-time attention.
- **Link**: https://arxiv.org/abs/2610.14219

---

## 12. Games · World Models · Decision-Making (1 un-venued paper)

### 12.1 Sanzaru: Benchmarking Protocol Formation under Epistemic & Communication Asymmetry
- **中文标题**: Sanzaru：认知与通信不对称下的协议形成基准
- **Authors**: Yiping Li, Zhiyu An, Wan Du
- **Affiliation**: University of California, Merced
- **Venue**: *(preprint)*
- **Problem background**: A model solving a task individually doesn't ensure a *team* can solve it under unequal information and communication.
- **Key innovation**: **Sanzaru** — cooperative bomb-defusal puzzles (adapted from BOMBANANA!) with role asymmetry (one agent can't hear, one can't speak, one can't see): **120 instances across 7 families**, targeting distinct coordination abilities.
- **Results / comparison**: Across **1,512 episodes**, 7 models reach **49%** overall success (20–86%); teams invent protocols (gesture codes, Morse, full-manual encodings), yet trace analysis attributes **~60% of 771 losses to communication**, and agents try channels their teammates lack despite explicit instructions.
- **Link**: https://arxiv.org/abs/2610.15163

---

## 13. Safety · Alignment · Interpretability (2 un-venued papers)

### 13.1 Towards Merging-conditional Backdoor Unalignment against Large Language Models (SMOKE)
- **中文标题**: 面向大模型的合并条件后门去对齐（SMOKE）
- **Authors**: Yukun Chen, Yidou Chen, Yiming Li, Xinyu Zhang, Baosong Yang, Hongwei Yao, Zhan Qin
- **Affiliation**: Zhejiang University (State Key Lab of Blockchain and Data Security); **Tongyi Lab, Alibaba Group**; Nanyang Technological University; City University of Hong Kong
- **Venue**: *(preprint; 31 pages)*
- **Problem background**: Model merging is widely used to specialize LLMs; a third-party model may pass safety audits yet activate malicious behavior *upon merging*.
- **Key innovation**: Reveals **One-sided Merging-Conditional Backdoor (OMCB)** — dormant and undetectable standalone, activated by merging. Theoretical analysis pinpoints the parameter shift crossing safety decision boundaries; **SMOKE** is a **meta-learning** attack (bi-level optimization: inner loop synthesizes surrogate meta-vectors via random low-rank init + finite-step maximization; outer loop optimizes the target while simulating merging).
- **Results / comparison**: Injected OMCB has bounded generalization loss and evades standalone backdoor detection — a new supply-chain threat for merged LLMs.
- **Link**: https://arxiv.org/abs/2610.14701

### 13.2 What Survives When Activation Steering Is Used as Memory
- **中文标题**: 当激活引导用作记忆时会保留什么
- **Authors**: Vedant Jumle
- **Affiliation**: Delft University of Technology
- **Venue**: *(preprint; pre-registered study)*
- **Problem background**: Activation steering has been used as a *memory for skills* (past experiences stored as steering vectors); facts/preferences are assumed to need text.
- **Key innovation**: Tests that assumption with a **training-free activation memory** beside a frozen LLM — the change an experience causes in late-layer states is stored as a shift, filed under a whitened gist key, re-added in a later session when the gist matches. Argues the shift is a fixed *average* of an attention-recomputed effect, so only question-independent content survives.
- **Results / comparison**: On Qwen3.5-2B/9B with four judge families, the memory is **~98% selective** but facts are **almost never used** (≤15% clean use vs. 96–98% in context); pre-registered, with a reference-subtraction ablation.
- **Link**: https://arxiv.org/abs/2610.14958

---

## 14. Methodology Notes

- **Window.** Newest indexed arXiv announcement block = **2026-10-10** (+ early 10-11). Selection restricted to papers **published ≥ 2026-09-18** to keep the digest "new", while retaining exact venue tags from the `comment`/`journal_ref` fields. Older-venue papers preprinted now are folded into §6.
- **Affiliation recovery.** Read from each paper's arXiv **HTML author block** (`arxiv.org/html/{id}v1`). Where the block carried an explicit `Affiliation:` token or corporate domain it is quoted; otherwise marked *(affiliation not recovered from arXiv HTML)*. Corporate labs are **not** disambiguated to legal entities.
- **Venue tagging is self-reported** by authors in the arXiv comment/journal fields; main vs. Findings vs. workshop vs. Industry distinctions are stated only where the comment made them.
- **Bilingual titles** are provided per the wiki's `title` / `中文标题` convention; **body text is English** (matching the English source papers and the 10-12 sibling digest), with technical terms kept in English.

---

## 15. Venue Index

| Paper | Venue | Category |
|-------|-------|----------|
| SpecForge (2610.15708) | NeurIPS 2026 Main | Agents / code |
| Approximation in CRL (2610.15388) | NeurIPS 2026 | Representation theory |
| Sharp Directions / Activation Steering (2610.16084) | NeurIPS 2026 | Interpretability |
| Beyond Adjacent Layers / FCM (2610.15159) | NeurIPS 2026 | Efficiency / compression |
| Scaling Laws for Multimodal Data Mixtures (2610.14423) | NeurIPS 2026 (spotlight) | Scaling laws |
| Fisher Information & Memorization (2610.16161) | NeurIPS 2026 | Theory / memorization |
| DEFT EEG (2610.14497) | NeurIPS 2026 | Foundation models / EEG |
| OmniCapBench (2610.12458) | NeurIPS 2026 | Benchmark / audio-visual |
| X-AVDD (2610.13687) | NeurIPS 2026 | Dataset distillation |
| BigCell (2610.14261) | NeurIPS 2026 | Generative / pathology |
| AnyEdit (2610.15665) | NeurIPS 2026 | Generative / audio |
| PDE-PFN (2610.13334) | NeurIPS 2026 | Scientific ML |
| SBNO (2610.13317) | NeurIPS 2026 | Scientific ML |
| SRCoD (2610.14542) | NeurIPS 2026 | Benchmark diagnosis |
| Audio Deepfake ADD (2610.16049) | NeurIPS 2026 | Audio / safety |
| FramePack-U (2610.16118) | NeurIPS 2026 | Long video / efficiency |
| DNA FMs beyond composition (2610.15711) | NeurIPS 2026 (E&D) | Genomics / eval |
| Personalized LLM Rec Semantic IDs (2610.15864) | NeurIPS 2026 PALM W | Recommendation |
| TeSearch (2610.15964) | NeurIPS 2026 EvoRobust W | Self-evolving agents |
| Hardware Faults in LLM Agents (2610.12756) | NeurIPS 2026 W | Agents / robustness |
| AutoNovo (2610.16232) | NeurIPS 2026 W | Agentic science |
| Nemotron Indic (2610.15373) | NeurIPS 2026 W | Multilingual LLM |
| Spiking LM scaling (2610.15146) | NeurIPS 2026 AXIOM W | Scaling laws |
| Memorization image classification (2610.16090) | NeurIPS 2026 W | Memorization |
| RELAGRAM (2610.15106) | NeurIPS 2026 MLxOR W | Routing / CO |
| SmolWAM (2610.13740) | NeurIPS 2026 W | World-action models |
| Guarded Block Transfers (2610.15829) | NeurIPS 2026 OPT W | Optimization |
| Auditing VLM Benchmarks (2610.13548) | NeurIPS 2026 TAE W | Benchmark audit |
| Token-Budgeted 3D retrieval (2610.14207) | NeurIPS 2026 W | 3D VLM / retrieval |
| Jailbreak depth-based inference (2610.15207) | NeurIPS 2026 FLMSec W | Safety |
| Trust Hinders Alignment (2610.15136) | NeurIPS 2026 BiAlign W | Human-AI alignment |
| Agentic RAG Portable Skills (2610.14428) | EMNLP 2026 Industry | Agents / RAG |
| MisVisAgentBench (2610.12823) | EMNLP 2026 Main | Benchmark / Web agents |
| ChronoRegime / CTR (2610.14073) | EMNLP 2026 Main | Temporal reasoning |
| GNN-CB (2610.05387) | EMNLP 2026 Main | Benchmark / GNN |
| Clinical Triage (2609.38600) | EMNLP 2026 Findings | Benchmark / clinical |
| SymCE (2610.02444) | EMNLP 2026 Findings | Formal reasoning / RLVR |
| Pareto-Dominant Clarification (2610.04089) | EMNLP 2026 LMP W | Coding agents / RL |
| Intent-to-CAD (2610.15681) | ICML 2026 Main | Generative / CAD |
| Multi-Agent Prompt Injection (2609.22949) | ICML 2026 AIWILD W | Agents / security |
| Decision Titan (2610.01513) | ICML 2026 W | Offline RL / TTT |
| PANINI-DR (2610.15208) | ICLR 2027 (review) | Deep research agents |
| CoRE (2610.14465) | ICLR (review) | Retrieval |
| Autoregressive generation limits (2610.14615) | ICLR 2027 (review) | Theory / safety |
| PopGen (2610.15969) | ICLR 2027 (review) | Multi-agent RL |
| PotentialEP (2610.14409) | ICLR 2027 (review) | Generative / neuromorphic |
| CRJudgeBench (2609.37216) | ICLR 2027 (review) | Code review / agents |
| HR bias audit (2610.14579) | RecSys in HR '26 | Recommendation / bias |
| SAFE-KV (2610.15186) | AACL-IJCNLP 2026 Findings | KV cache / RAG |
| REPRO (2610.15513) | ACM TOSEM (review) | Safety / red-teaming |
| AURA (2610.05219) | ICLR 2026 W | Safety / adaptation |
| MARTA (2610.05223) | ICLR 2026 W | Agents / memory |
| RGT (2610.15427) | WWW 2026 | Graph tokenizer |
| Radiology adversarial detect (2610.15628) | CVPR 2026 W (SAIAD) | Adversarial / medical |
| Quantum VQC label noise (2610.16153) | AAAI 2026 Symposium (QIML) | Quantum ML |
| Mountain hidden-gem POIs (2610.13467) | CIKM 2026 STM4KD W | RecSys / tourism |

---

## 16. Coverage Notes & Vacancies

- ⚠️ **CTR / advertising vacancy.** **Zero** papers with an explicit CTR/advertising focus surfaced in this block (`"click-through rate"`, `"CTR prediction"`, `"click-through"`, `"advertising"` → 0 fresh hits). The industrial CTR *architecture* lane (scaling laws, long-sequence modeling, generative recall/ranking) remains empty for the **fifth+ consecutive digest** — a genuine signal-famine, not a selection artifact.
- ⚠️ **Requested older-venue grid largely closed.** ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025 have passed their acceptance cycles; this run surfaces only *new preprints* still carrying those tags (§6) plus the live 2027-cycle venues. No new SIGIR 2026 / KDD 2026 / ACL 2026 acceptances appeared.
- ⚠️ **Partial rate-limiting.** Of ~110 planned harvest queries, ~85 returned; the date-bounded topical tail (recommendation, CTR, advertising, ad auction, generative/sequential recommendation) was partly rate-limited and re-covered via the successful cs.IR/cs.CL/cs.MM category sweeps and venue sweeps. Coverage of the rec/ads lane is therefore *lower-bounded*, not exhaustive.
- **Top-lab coverage.** Confirmed affiliations include Netflix, Google Research/DeepMind, Amazon/AWS, Microsoft Research, Tencent (Hunyuan + WeChat AI), Alibaba (Tongyi Lab), Huawei, NVIDIA (model lineage), Qualcomm, Intel AI, Adobe, PNNL, NEC Labs, Nokia Bell Labs, Luma AI, Airbnb. No fresh **OpenAI / Meta AI / Apple / Baidu / Kuaishou** research preprints entered this block under a verified venue tag.

---

## 17. Cross-Cutting Themes

1. **Serving-time re-architecture.** Capability is increasingly bought at *inference*, not training: SAFE-KV (causal KV repair), FidelityQ (predictive-fidelity 2-bit quantization), FCM (non-adjacent layer fusion), LLoPS (learned polynomial linear attention), FramePack-U (constant-memory packing). The through-line is *behavior preservation* under structural compression/reuse.
2. **Verifier-grounded self-improvement.** SpecForge, TeSearch, Sequent-Prover, SymCE, WorkBorne, Reels-RSI share a recipe: an **executable check** (tests, SMT solver, deterministic renderer, verifier) is the improvement signal, with explicit defenses against *coupling/whack-a-mole* and *imitation traps*.
3. **Benchmark-validity becomes the frontier.** MisVisAgentBench, Auditing VLM Benchmarks, SRCoD, Lumen-bench, Sanzaru, CRJudgeBench, GNN-CB, Clinical Triage, UDHRBench all ask whether a benchmark measures what it claims — and repeatedly find *shortcuts, artifacts, and cross-lingual action gaps*.
4. **Un-venued preprints dominate the fresh block.** With the 2026 H1/H2 cycles closed, ~28% of featured work is un-venued; the venue-tagged fraction is concentrated in NeurIPS 2026 (main + a wide workshop spread) and EMNLP 2026.
5. **Diffusion as a scientific/generative substrate.** Flow-matching extends beyond images to gigapixel pathology (BigCell), audio (AnyEdit), PDE operators (PDE-PFN/SBNO), and backprop-free analog sampling (PotentialEP) — the wiki's *generative-substrate* arc widens across modalities and hardware.
6. **Safety becomes measurable and adversarial-by-default.** Merging-conditional backdoors (SMOKE), depth-dependent jailbreak surfaces, multi-agent prompt injection, cross-lingual say-do gaps, and red-teaming ASR=100% — each supplies a *metric*, matching the wiki's "make safety observable" trajectory.

---

*Generated by the daily `conference-digest` job on 2026-10-14. 78 papers, 0 dedup collisions against a 9,015-ID wiki baseline. Venue tags self-reported; affiliations author-block reads.*
