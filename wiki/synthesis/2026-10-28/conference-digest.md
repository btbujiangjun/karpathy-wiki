---
title: Conference Digest — 12-venue frontier papers + industrial systems (2026-10-28)
type: synthesis
created: 2026-10-28
updated: 2026-10-28
sources: []
tags: [conference-digest, ICML2026, AAAI2026, NeurIPS2025, ICLR2026, KDD2026, CVPR2026, ACL2026, EMNLP2025, SIGIR2026, WWW2026, CIKM2025, RecSys2025, recommendation, LLM, advertising, CTR, agents, diffusion, generative-models, sequential-modeling, games, evaluation, daily-digest]
---

# Conference Digest — 12-venue frontier papers + industrial systems (2026-10-28)

A cross-venue snapshot of 20 papers: award winners, strong main-track papers, and two recent industry preprints that matter for the LLM/recommendation/agent stack. Coverage spans ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025, plus two arXiv preprints.

This edition deliberately avoids the award-only framing of the 2026-10-21 digest. The through-line is **systems that make expensive inference or execution cheaper**: hardware-aware ranking, streaming listwise CTR, long-sequence recommenders, predict-before-execute agents, beam-search-aware LLM recommendation, and compressed Internet-scale search. A second cluster is **reliability under realistic use**: multi-turn conversation, RLVR capability boundaries, benchmark contamination, and sparse/uncertain recommendation.

> Scope note: results below are taken from official proceedings pages, arXiv abstract/PDF, ACM/CVF pages, or publisher metadata. Where a paper is not peer-reviewed, it is marked as such. The two latest industry preprints are included because they directly affect the recommendation/LLM production stack, not because they are accepted papers.

---

## At a glance

| # | Venue | Paper | Lead org | Headline result |
|---|-------|-------|----------|-----------------|
| 1 | ICML 2026 | The Flexibility Trap | Tsinghua / Alibaba | JustGRPO reaches 89.1% GSM8K with standard GRPO on dLLMs |
| 2 | ICML 2026 | High-Accuracy Sampling | MIT / Yale | `polylog(1/δ)` diffusion sampling, exponential improvement |
| 3 | AAAI 2026 | LLM2CLIP | Tongji / Microsoft | +16.5% EVA02 long- and short-text retrieval |
| 4 | AAAI 2026 | ReconVLA | HKUST(GZ) / Westlake | 59.3% → 79.5% on precise stacking; +20.6% vs OpenVLA |
| 5 | NeurIPS 2025 | Gated Attention | Alibaba Qwen | 30 variants, 3.5T tokens; first-token attention 46.7% → 4.8% |
| 6 | NeurIPS 2025 | Does RL Really Incentivize Reasoning? | Tsinghua | RLVR improves pass@1 but base models win at large pass@k |
| 7 | ICLR 2026 | LLMs Get Lost in Multi-Turn Conversation | Microsoft / Salesforce | −39% average across six tasks, 200k+ conversations |
| 8 | KDD 2026 | HOBA | Kuaishou | Positive target-cost/ROI A/B gains; exact figures caveated |
| 9 | KDD 2026 | DLL | Kuaishou | +0.95pp GAUC offline; +2.71% CTR, +4.55% EPR online |
| 10 | CVPR 2026 | NitroGen | NVIDIA | 40k hours, 1,000+ games; +52% relative after fine-tuning |
| 11 | ACL 2026 | Can We Predict Before Executing ML Agents? | Zhejiang / Ant Group | 61.5% pairwise accuracy; 6× faster convergence |
| 12 | ACL 2026 Findings | ReasonRec | Meta AI / MSU / UNC | >30% relative ranking gain; 35% queries delegated |
| 13 | EMNLP 2025 | Infini-gram mini | UW / Ai2 | 18× faster indexing, 83TB indexed, 74.2% GSM8K contamination |
| 14 | SIGIR 2026 | BEAR | Zhejiang / CUHK-SZ | +12.50% average recommendation accuracy over SOTA |
| 15 | WWW 2026 | DualGR | USTC / Kuaishou | +0.527% video views, +0.432% watch time; Best Short Paper |
| 16 | WWW 2026 | GenCI | RUC / Tencent WeChat | Reports gains over DIN/DIEN; exact table values caveated |
| 17 | CIKM 2025 | RankMixer | ByteDance | MFU 4.5% → 45%; active days +0.3%, duration +1.08% |
| 18 | RecSys 2025 | LONGER | ByteDance | Ads ADSS up to +2.097%; e-commerce GMV/U +6.54% |
| 19 | arXiv 2026 | OneRec-Think | Kuaishou | +0.159% App Stay Time in one-week online A/B |
| 20 | arXiv 2026 | Principled Synthetic Data | Meta | +130% recall@100 for SasRec; first rec-LLM scaling law |

---

## 1. ICML 2026

### 1.1 The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models
《灵活性陷阱：重新审视 Diffusion Language Model 中任意顺序的价值》

- **Authors / affiliation:** Zanlin Ni, Shenzhi Wang, Yang Yue, Tianyu Yu, Weilin Zhao, Yeguo Hua, Tianyi Chen, Jun Song, Cheng Yu, Bo Zheng, Gao Huang. LeapLab and NLPLab at Tsinghua University; Alibaba Group; BNRist. ICML 2026 Outstanding Paper / Oral.
- **Problem:** Diffusion LLMs (dLLMs) are promoted as more flexible than autoregressive models because they can generate tokens in arbitrary order. The paper asks whether that flexibility actually expands the reasoning solution space.
- **Method / innovation:** The authors show that order flexibility lets dLLMs skip high-uncertainty tokens that are essential for exploration, causing premature collapse of solution coverage. They propose **JustGRPO**: intentionally abandon arbitrary-order generation and apply standard GRPO, while retaining parallel decoding at inference.
- **Results:** JustGRPO reaches **89.1% GSM8K**, **45.1% MATH-500**, **49.4% HumanEval**, and **52.4% MBPP**. This beats reproduced diffusion-specific RL baselines: d1 83.8/39.2, ESPO 84.7/40.3/42.1/44.6, and SPG 86.9/41.8.
- **Comparison / significance:** A deliberately minimalist method beats complex diffusion-specific RL recipes; the bottleneck is the exploration geometry induced by arbitrary order, not the RL objective. It also preserves the inference-efficiency advantage of parallel decoding.
- **Links:** [PMLR](https://proceedings.mlr.press/v306/ni26e.html) · [arXiv 2601.15165](https://arxiv.org/abs/2601.15165) · [ICML Oral](https://icml.cc/virtual/2026/oral/71086)

### 1.2 High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions
《Diffusion Model 与 Log-Concave 分布的高精度采样》

- **Authors / affiliation:** Fan Chen, Sinho Chewi, Constantinos Daskalakis, Alexander Rakhlin. Author affiliations were not independently re-verified in this run. ICML 2026 Outstanding Paper.
- **Problem:** Diffusion samplers typically need many steps to reach low error, and existing complexity bounds are far from the ideal `polylog(1/δ)` dependence.
- **Method / innovation:** The paper gives algorithms that obtain `δ`-error in `polylog(1/δ)` steps given `Õ(δ)`-accurate `L²` score estimates. It handles three regimes: general data (`Õ(d polylog(1/δ))`), non-uniform `L`-Lipschitz scores (`Õ(√(dL) polylog(1/δ))`), and intrinsic dimension `d*` (`Õ(d* polylog(1/δ))`).
- **Results:** This is an **exponential improvement** over all previous diffusion-sampling results. The analysis also yields the first `polylog(1/δ)`-complexity sampler for general log-concave distributions using only gradient evaluations.
- **Comparison / significance:** The contribution is theoretical rather than a benchmark win: it closes the gap between diffusion practice and high-accuracy sampling theory, and gives a unified view of diffusion sampling and classical log-concave sampling.
- **Links:** [PMLR](https://proceedings.mlr.press/v306/chen26p.html) · [arXiv 2602.01338](https://arxiv.org/abs/2602.01338)

---

## 2. AAAI 2026

### 2.1 LLM2CLIP: Powerful Language Model Unlocks Richer Visual Representation
《LLM2CLIP：用强大语言模型解锁更丰富的视觉表征》

- **Authors / affiliation:** Weiquan Huang, Aoqi Wu, Yifan Yang, Xufang Luo, Yuqing Yang, Usman Naseem, Chunyu Wang, Qi Dai, Xiyang Dai, Dongdong Chen, Chong Luo, Lili Qiu, Liang Hu. Tongji University, Microsoft, Macquarie University. AAAI 2026 Outstanding Paper.
- **Problem:** CLIP's text encoder limits it to short, simple captions. Directly plugging in an LLM fails badly because autoregressive LLM outputs are poorly discriminative for contrastive retrieval.
- **Method / innovation:** LLM2CLIP fine-tunes the LLM in caption space with contrastive learning, turning its output embeddings into discriminative text representations. The fine-tuned LLM then acts as a teacher for CLIP's visual encoder, allowing longer and more complex captions without the original CLIP context-window limit.
- **Results:** It improves the previous SOTA **EVA02 by 16.5% on both long-text and short-text retrieval**, and turns an English-only CLIP into a strong cross-lingual model. When plugged into LLaVA-1.5-style multimodal training, it consistently beats CLIP across nearly all benchmarks; training cost is close to ordinary CLIP fine-tuning.
- **Comparison / significance:** The key comparison is not just EVA02/SigLIP-2 but the failure mode of naive LLM integration. The paper shows the right interface is contrastive caption-space distillation, not replacing the text tower and hoping for the best.
- **Links:** [arXiv 2411.04997](https://arxiv.org/abs/2411.04997) · [Microsoft Research](https://www.microsoft.com/en-us/research/project/llm2clip/)

### 2.2 ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver
《ReconVLA：作为高效机器人感知器的重建式 Vision-Language-Action Model》

- **Authors / affiliation:** Wenxuan Song, Ziyang Zhou, Han Zhao, Jiayi Chen, Pengxiang Ding, Haodong Yan, Yuxin Huang, Feilong Tang, Donglin Wang, Haoang Li. HKUST (Guangzhou), Westlake University, Zhejiang University, Monash University. AAAI 2026; outstanding-paper status was tentative in earlier wiki notes and was not re-confirmed from the official award page in this run.
- **Problem:** VLA models often spread visual attention over irrelevant regions instead of grounding on the object to manipulate. Adding a generative future-image predictor is expensive and does not directly fix current-observation perception.
- **Method / innovation:** ReconVLA adds an implicit grounding objective: conditioned on the VLA's visual outputs, a diffusion transformer reconstructs the **gaze region** around the target object. This forces fine-grained visual representations and target-directed attention. The authors also curate 100k+ trajectories / 2M samples from open robot datasets for reconstruction pretraining.
- **Results:** On the hardest "stack block" task, success rises from **59.3% to 79.5% (+20.2%)**. In ABC→D generalization, ReconVLA beats generative baselines by over 20 points on the last sub-task, and with comparable parameters beats **OpenVLA by 20.6%** and **UniVLA by 7.6%** on the last sub-task. It completes 4.23/5 consecutive tasks on average and reaches 98.0% on the first task.
- **Comparison / significance:** The paper argues perception, not future-frame generation, is the under-invested bottleneck. Reconstruction is used as a training-time attention-shaping signal, not a costly inference-time video generator.
- **Links:** [AAAI OJS](https://ojs.aaai.org/index.php/AAAI/article/view/38921) · [arXiv 2508.10333](https://arxiv.org/abs/2508.10333) · [Project](https://zionchow.github.io/ReconVLA/)

---

## 3. NeurIPS 2025

### 3.1 Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free
《Large Language Model 的门控注意力：非线性、稀疏性与无 Attention Sink》

- **Authors / affiliation:** Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, Junyang Lin. Alibaba Qwen Team. NeurIPS 2025; the exact award label remains disputed in this run (Best Paper vs Runner-up).
- **Problem:** Gating is ubiquitous, but its effect on softmax attention is poorly understood. Standard attention also suffers from massive activations, attention sinks, and long-context extrapolation failures.
- **Method / innovation:** A systematic sweep over **30 gating variants** of **15B MoE** and **1.7B dense** models trained on **3.5T tokens**. The winning design is a head-specific sigmoid gate after scaled dot-product attention. The paper attributes gains to added non-linearity on the low-rank attention mapping and query-dependent sparse modulation.
- **Results:** The gate eliminates attention sink, tolerates larger learning rates, improves scaling, and reduces attention to the first token from **46.7% to 4.8%**, with **<2% wall-time overhead**. The design is already used in Qwen3-Next.
- **Comparison / significance:** A rare architecture paper where the intervention is tiny, the ablation grid is large, and the result ships in a production model family. It is the strongest recent evidence that attention gating is a first-class architectural primitive, not a tuning trick.
- **Links:** [NeurIPS](https://neurips.cc/virtual/2025/poster/120216) · [arXiv 2505.06708](https://arxiv.org/abs/2505.06708)

### 3.2 Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?
《Reinforcement Learning 真的能激励 LLM 超越基座的推理能力吗？》

- **Authors / affiliation:** Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Yang Yue, Shiji Song, Gao Huang. LeapLab, Tsinghua University; Shanghai Jiao Tong University. NeurIPS 2025 Best Paper Runner-up.
- **Problem:** RLVR is widely assumed to create new reasoning abilities. The paper tests the stronger claim that RLVR expands the capability boundary of the base model.
- **Method / innovation:** Uses **pass@k at large k** as a capability-boundary probe across model families, RL algorithms, and math/coding/visual reasoning benchmarks. It also analyzes coverage and perplexity of sampled reasoning paths.
- **Results:** RLVR improves sampling efficiency and pass@1, but **base models achieve higher pass@k when k is large**. Six popular RLVR algorithms perform similarly and remain far from the base-model upper bound. Distillation, by contrast, can introduce new reasoning patterns from a teacher.
- **Comparison / significance:** This is a clean negative result against the "RL discovers new reasoning" narrative: current RLVR narrows the solution space toward rewarded paths rather than expanding it. It motivates continual scaling and multi-turn agent-environment interaction.
- **Links:** [NeurIPS](https://neurips.cc/virtual/2025/poster/119944) · [arXiv 2504.13837](https://arxiv.org/abs/2504.13837)

---

## 4. ICLR 2026

### 4.1 LLMs Get Lost in Multi-Turn Conversation
《LLM 在多轮对话中会迷路》

- **Authors / affiliation:** Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville. Microsoft Research and Salesforce Research. ICLR 2026 Best Paper.
- **Problem:** LLM evaluation is dominated by single-turn, fully specified instructions, while real users underspecify and refine over many turns.
- **Method / innovation:** Large-scale simulation comparing full, concatenated, and sharded instructions across **six generation tasks**, **600 instructions**, and **15 open/closed models**, totaling **200,000+ simulated conversations**.
- **Results:** Every tested model degrades on every task; average drop is **−39%**. The degradation decomposes into a minor loss in aptitude and a large increase in unreliability. Models make early assumptions, prematurely generate a final answer, then over-rely on it and fail to recover.
- **Comparison / significance:** The paper defines "Lost in Conversation" as a distinct failure mode, not just a multi-turn prompt-format issue. It is a benchmark-and-diagnosis paper with direct implications for agent memory, clarification behavior, and conversational evaluation.
- **Links:** [ICLR PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/59f6421e64707225fdf5b28840679a07-Paper-Conference.pdf) · [arXiv 2505.06120](https://arxiv.org/abs/2505.06120)

---

## 5. KDD 2026

### 5.1 HOBA: Hierarchical On-Policy Bidding Agents for Adaptive Online Advertising
《HOBA：面向自适应在线广告的分层 On-Policy 竞价 Agent》

- **Authors / affiliation:** Ji Wu, Yunshan Peng, Wentao Bai, Yunke Bai, Wenzheng Shu, Jinan Pang, Yanxiang Zeng, Xialong Liu. Kuaishou Technology. KDD 2026.
- **Problem:** Production bidding stacks combine PID, MPC, offline RL, and Decision Transformer experts, but they do not adapt online to non-stationary auctions and require expensive manual tuning of bid bounds and budget pacing.
- **Method / innovation:** Three-level hierarchical RL across three time scales. High level: an LLM infers hyperparameters via a Think-Act-Observe-Reflect loop with experience retrieval. Mid level: a SARSA agent selects expert models with causal adjustment for selection bias. Low level: a dynamic expert pool (PID, MPC, IQL, Decision Transformer) executes bids under high-level constraints. Online learning is confined to discrete expert selection, reducing exploration risk.
- **Results:** The paper reports SOTA results on AuctionNet and positive online A/B outcomes. Prior wiki notes — not re-confirmed from the official PDF in this run — record **+12.1%** in sparse AuctionNet settings and a **4,982-campaign** online test with target-cost achievement **90.0% → 93.2% (+3.6%)**, conversion value **$18.50M → $20.00M (+8.1%)**, ROI **2.15 → 2.22 (+3.3%)**, budget completion **94.2% → 97.8%**, and advertiser satisfaction **3.68 → 3.96/5**. P99 latency is **38ms** versus 12ms baseline; manual tuning cost drops **96%**; deployed across 100K+ campaigns.
- **Comparison / significance:** The baseline is a 3-year production Decision Transformer + rule tuning system, so the gains are against a strong incumbent. The architectural lesson is to put LLM reasoning at the slow strategic layer and keep millisecond bidding conventional.
- **Links:** [ACM](https://dl.acm.org/doi/10.1145/3770855.3818435) · [arXiv 2607.24779](https://arxiv.org/abs/2607.24779)

### 5.2 Breaking the Listwise-Shuffle Dilemma: A Streaming-Compatible Listwise Framework for Industrial CTR Prediction
《打破 Listwise-Shuffle 困境：面向工业 CTR 预测的流式兼容 Listwise 框架》

- **Authors / affiliation:** Junlin He, Rui Tang, Liyin Hong. Kuaishou Technology. KDD 2026.
- **Problem:** Listwise CTR objectives align better with ranking metrics, but require session-level aggregation. Industrial streaming training requires strong shuffling; the two conflict — the "Listwise–Shuffle Dilemma".
- **Method / innovation:** **Decoupled Listwise Learning (DLL)** reconstructs session-level supervision without session batching by combining the training score of the target item with serving-time contextual predictions logged by the deployed model. This enables listwise optimization under fully shuffled one-pass updates. **Margin-Regularized Self-Correction (MRSC)** replaces zero-tolerance consistency with a label-dependent asymmetric margin, tolerating benign fluctuations while penalizing meaningful regressions.
- **Results:** In a large-scale commercial streaming CTR environment: **+0.95pp GAUC offline**, **+2.71% CTR**, and **+4.55% EPR** online. Deployed in a production short-video search system serving tens of millions of daily queries.
- **Comparison / significance:** This is a rare clean solution to a training/serving systems conflict: no session replay buffer, no batch regrouping, and no sacrifice of the shuffling needed for stable online learning. It is directly relevant to the wiki's [[ctr-scaling-landscape]] and streaming-training threads.
- **Links:** [ACM](https://dl.acm.org/doi/10.1145/3770855.3818327) · [PDF](https://dl.acm.org/doi/pdf/10.1145/3770855.3818327)

---

## 6. CVPR 2026

### 6.1 NitroGen: An Open Foundation Model for Generalist Gaming Agents
《NitroGen：面向通用游戏 Agent 的开放基础模型》

- **Authors / affiliation:** Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi Fan. NVIDIA, with academic collaborators. CVPR 2026.
- **Problem:** Embodied agents lack a large, diverse, action-labeled gaming corpus and a cross-game benchmark for generalist control.
- **Method / innovation:** Three ingredients: (1) an Internet-scale video-action dataset built by extracting player actions from public gameplay videos; (2) a multi-game benchmark for cross-game generalization; (3) a unified vision-action model trained with large-scale behavior cloning. Dataset covers **40,000 hours** across **more than 1,000 games**.
- **Results:** NitroGen handles 3D action combat, high-precision 2D platformers, and exploration in procedural worlds. When fine-tuned, pretraining transfers to unseen games with **up to +52% relative task success** over models trained from scratch. Dataset, evaluation suite, and weights are released.
- **Comparison / significance:** The result is a scaling-law-style argument for gameplay video as embodied pretraining data. It also makes generalist gaming agents reproducible: open data, open benchmark, open weights.
- **Links:** [CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Magne_NitroGen_An_Open_Foundation_Model_for_Generalist_Gaming_Agents_CVPR_2026_paper.html)

---

## 7. ACL 2026

### 7.1 Can We Predict Before Executing Machine Learning Agents?
《我们能在执行 Machine Learning Agent 之前做出预测吗？》

- **Authors / affiliation:** Jingsheng Zheng, Jintian Zhang, Yujie Luo, Yuren Mao, Yunjun Gao, Lun Du, Huajun Chen, Ningyu Zhang. Zhejiang University; Ant Group; Zhejiang University–Ant Group Joint Laboratory of Knowledge Graph. ACL 2026 Long Paper.
- **Problem:** Autonomous ML agents follow Generate-Execute-Feedback, so every hypothesis needs an expensive run. MLE-Bench-style runs can take up to **9 hours**, creating an execution bottleneck.
- **Method / innovation:** Formalizes **Data-centric Solution Preference** and builds **18,438 pairwise comparisons**. With a Verified Data Analysis Report as context, an LLM predicts which candidate solution is better before execution. **ForeAgent** uses a Predict-then-Verify loop: predict to prune, execute only when verification is needed.
- **Results:** LLMs reach **61.5% pairwise accuracy** with robust confidence calibration. ForeAgent achieves **6× faster convergence** while surpassing execution-based baselines by **+6%**.
- **Comparison / significance:** The paper is not claiming an LLM can replace execution; it shows a calibrated predictor can allocate execution budget. This is a practical world-model argument for agents: internal prediction is useful exactly where physical verification is expensive.
- **Links:** [ACL Anthology](https://aclanthology.org/2026.acl-long.182/) · [arXiv 2601.05930](https://arxiv.org/abs/2601.05930)

### 7.2 ReasonRec: A Reasoning-Augmented Multimodal Agent for Unified Recommendation
《ReasonRec：面向统一推荐的理由增强多模态 Agent》

- **Authors / affiliation:** Yihua Zhang, Mingfu Liang, Jiyan Yang, Rong Jin, Wen-Yen Chen, Yiping Han, Huayu Li, Buyun Zhang, Liang Luo, Luke Simon, Sijia Liu, Tianlong Chen, Xi Liu. Meta AI, Michigan State University, University of North Carolina at Chapel Hill. Findings of ACL 2026.
- **Problem:** Multimodal recommenders fuse features well but are opaque, lack explicit reasoning, and cannot self-assess uncertainty or cheaply defer hard cases.
- **Method / innovation:** A three-stage **Observe–Deliberate–Act** pipeline. Observe: pretrained VLM encoder. Deliberate: recommendation as chain-of-thought tasks, with an evidence-horizon-aware curriculum that increases reasoning complexity and quantifies uncertainty. Act: dynamically delegate uncertain or hard queries to lightweight classical recommenders. A reasoning-aware visual instruction-tuning strategy unifies diverse recommendation tasks into CoT prompts.
- **Results:** Across sequential recommendation, direct recommendation, CTR prediction, and explanation generation on five real datasets, ReasonRec achieves **over 30% relative improvement** in key ranking metrics such as HR@5 and NDCG@5 versus SOTA multimodal recommenders. It delegates **up to 35%** of queries to efficient sub-models without hurting accuracy.
- **Comparison / significance:** The interesting move is not "add CoT"; it is making delegation a first-class action. The agent learns when it is uncertain enough to hand off, which is a more realistic efficiency story than running a VLM on every request.
- **Links:** [ACL Anthology PDF](https://aclanthology.org/2026.findings-acl.391.pdf)

---

## 8. EMNLP 2025

### 8.1 Infini-gram mini: Exact n-gram Search at the Internet Scale with FM-Index
《Infini-gram mini：基于 FM-Index 的互联网规模精确 n-gram 搜索》

- **Authors / affiliation:** Hao Xu, Jiacheng Liu, Yejin Choi, Noah A. Smith, Hannaneh Hajishirzi. University of Washington and Allen Institute for AI (Ai2). EMNLP 2025 Best Paper.
- **Problem:** Exact-match search over Internet-scale corpora is storage-bound. Previous FM-index implementations are too slow and memory-heavy for petabyte-scale text.
- **Method / innovation:** An FM-index system that indexes and compresses text simultaneously, with parallel engineering for indexing and querying. It makes petabyte-level corpora searchable and exposes a web interface and API.
- **Results:** Index size is only **44% of the raw corpus** (about **7% of the original infini-gram**). Indexing speed is **18×** faster; indexing memory drops **3.2×**; query memory becomes negligible. The team indexed **83TB** of Internet text in **99 days** on one 128-core node, or **19 hours** with 137 nodes. Benchmark contamination analysis found core LM benchmarks heavily contaminated in crawls — up to **74.2% in GSM8K**.
- **Comparison / significance:** This is infrastructure that changes what evaluation can ask. The contamination result is the concrete payoff: exact search over the pretraining corpus can reveal test-set leakage that aggregate benchmark scores hide.
- **Links:** [ACL Anthology](https://aclanthology.org/2025.emnlp-main.1268/) · [arXiv 2506.12229](https://arxiv.org/abs/2506.12229) · [UW News](https://news.cs.washington.edu/2026/01/29/allen-school-researchers-earn-emnlp-best-paper-award/)

---

## 9. SIGIR 2026

### 9.1 BEAR: Towards Beam-Search-Aware Optimization for Recommendation with Large Language Models
《BEAR：面向 LLM 推荐的 Beam-Search-Aware 优化》

- **Authors / affiliation:** Weiqin Yang, Bohao Wang, Zhenxiang Xu, Jiawei Chen, Shengjia Zhang, Jingbang Chen, Canghong Jin, Can Wang. Zhejiang University, CUHK-Shenzhen, Hangzhou City University. SIGIR 2026.
- **Problem:** LLM recommenders are trained with SFT to maximize the probability of a positive item, but inference uses beam search. A high-probability item can still be pruned early because its prefix probability is low — a training/inference mismatch.
- **Method / innovation:** **BEAR (Beam-SEarch-Aware Regularization)** avoids simulating beam search per instance. It enforces a relaxed necessary condition: every token of a positive item must rank within the top-`B` candidate tokens at each decoding step. This directly reduces the risk of incorrect pruning with negligible overhead over SFT.
- **Results:** Across **four real-world datasets** (Amazon Office, Book, Toy, Clothing), BEAR significantly outperforms strong LLM-based recommenders and achieves an **average +12.50% recommendation-accuracy improvement** across all datasets under N@K/H@K.
- **Comparison / significance:** A focused objective-level fix for a systems-level mismatch. It is cheaper than differentiable beam search or full beam simulation, and it complements generative-recommendation work that improves item tokenization or reasoning.
- **Links:** [arXiv 2601.22925](https://arxiv.org/abs/2601.22925) · [Code](https://github.com/Tiny-Snow/BEAR-SIGIR-2026)

---

## 10. WWW 2026

### 10.1 DualGR: Generative Retrieval with Long and Short-Term Interests Modeling
《DualGR：建模长短期兴趣的生成式检索》

- **Authors / affiliation:** Zhongchao Yi, Kai Feng, Xiaojian Ma, Yalong Wang, Yongqi Liu, Han Li, Zhengyang Zhou, Yang Wang. USTC and Kuaishou. WWW 2026 Best Short Paper.
- **Problem:** Generative retrieval in short-video feeds suffers from long/short interest interference, context-induced noise in hierarchical SID generation, and no explicit learning from exposed-but-unclicked feedback.
- **Method / innovation:** Three components: (1) a **Dual-Branch Long/Short-Term Router (DBR)** with selective activation; (2) **Search-based SID Decoding (S2D)**, constraining fine-level decoding to the current coarse bucket for efficiency and noise control; (3) an **Exposure-aware Next-Token Prediction Loss (ENTP-Loss)** that treats unclicked exposures as coarse-level hard negatives to accelerate interest fade-out.
- **Results:** In the large-scale Kuaishou short-video system, online A/B shows **+0.527% video views** and **+0.432% watch time**.
- **Comparison / significance:** The paper treats negative feedback as a first-class signal in generative retrieval and constrains decoding rather than merely scaling the generator. The WWW Best Short Paper award reflects the industrial relevance of the long/short-interest routing problem.
- **Links:** [arXiv 2511.12518](https://arxiv.org/abs/2511.12518)

### 10.2 GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning for CTR Prediction
《GenCI：通过 Cohort-based Intent Learning 生成建模用户兴趣迁移的 CTR 预测》

- **Authors / affiliation:** Kesha Ou, Zhen Tian, Wayne Xin Zhao, Hongyu Lu, Ji-Rong Wen. Gaoling School of AI, Renmin University of China; WeChat, Tencent; Beijing Key Laboratory of Research on Large Models and Intelligent Governance. WWW 2026.
- **Problem:** CTR models usually treat user interest as a static or slowly updated representation. Interest shifts are cohort-dependent and hard to model with per-user history alone.
- **Method / innovation:** GenCI learns **hierarchical semantic cohorts** of users, quantizes cohort intent, and uses a Transformer for next-token prediction over intent sequences. Candidate-aware cross-attention injects the target item into the generative interest model so the learned shift is conditioned on what is being scored.
- **Results:** Prior wiki notes report AUC **0.8964 / 0.7519 / 0.7182** on MovieLens, Amazon-Fashion, and Amazon-Instrument, with RelaImpr **10.82% / 10.29% / 9.92%** over the base model; these table values were not re-extracted from the official PDF in this run. The paper reports beating DeepFM, xDeepFM, DIN, DIEN, and other strong CTR baselines at comparable latency.
- **Comparison / significance:** GenCI bridges generative modeling and discriminative CTR: the generative component models cohort intent shift, while candidate-aware attention keeps the objective tied to the actual ranking decision.
- **Links:** [arXiv 2601.18251](https://arxiv.org/abs/2601.18251) · [DOI](https://doi.org/10.1145/3774904.3792612)

---

## 11. CIKM 2025

### 11.1 RankMixer: Scaling Up Ranking Models in Industrial Recommenders
《RankMixer：在工业推荐系统中扩展排序模型》

- **Authors / affiliation:** Jie Zhu, Zhifang Fan, Xiaoxie Zhu, Yuchen Jiang, Hangyu Wang, Xintian Han, Haoran Ding, Xinmin Wang, Wenlin Zhao, Zhen Gong, Huizhi Yang, Zheng Chai, Zhe Chen, Yuchao Zheng, Qiwei Chen, Feng Zhang, Xun Zhou, Peng Xu, Xiao Yang, Di Wu, Zuotao Liu. ByteDance; Qiwei Chen and Zhifang Fan as independent researchers. CIKM 2025.
- **Problem:** Industrial ranking models must meet strict latency and QPS constraints, but their CPU-era feature-crossing modules are memory-bound on GPUs and achieve single-digit MFU, making scaling uneconomical.
- **Method / innovation:** A hardware-aware architecture that keeps Transformer parallelism but replaces quadratic self-attention with **multi-head token mixing** (parameter-free cross-token interaction), plus **per-token FFNs** for feature-subspace capacity. A Sparse-MoE variant extends to 1B parameters with dynamic routing to address expert imbalance.
- **Results:** On a trillion-scale production dataset, RankMixer raises MFU from **4.5% to 45%** and scales online ranking parameters by two orders of magnitude at roughly the same inference latency. Offline gains versus DLRM-MLP: RankMixer-100M **+0.64% Finish AUC / +0.72% UAUC / +0.86% Skip AUC / +1.33% UAUC**; RankMixer-1B **+0.95% / +1.22% / +1.25% / +1.82%**. It beats DCNv2, DHEN, and Wukong at the same scale. Full-traffic 1B dense serving improves **active days +0.3%** and **in-app duration +1.08%** without higher serving cost.
- **Comparison / significance:** The lesson is that recommendation scaling is an MFU problem before it is a parameter-count problem. Replacing handcrafted low-MFU modules is what makes the scaling law reachable in production.
- **Links:** [ACM](https://dl.acm.org/doi/10.1145/3746252.3761507) · [arXiv 2507.15551](https://arxiv.org/abs/2507.15551)

---

## 12. RecSys 2025

### 12.1 LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders
《LONGER：在工业推荐系统中扩展长序列建模》

- **Authors / affiliation:** Zheng Chai, Qin Ren, Xijun Xiao, Huizhi Yang, Bo Han, Sijun Zhang, Di Chen, Hui Lu, Wenlin Zhao, Lele Yu, Xionghang Xie, Shiru Ren, Xiang Sun, Yaocheng Tan, Peng Xu, Yuchao Zheng, Di Wu. ByteDance. RecSys 2025.
- **Problem:** Ultra-long user behavior sequences capture long- and short-term preference, but two-stage retrieval or indirect modeling creates upstream/downstream inconsistency and quadratic attention cost.
- **Method / innovation:** LONGER combines: (1) global tokens to stabilize attention over long contexts; (2) a token-merge module with lightweight InnerTransformers and hybrid attention to reduce quadratic complexity; (3) engineering optimizations including mixed precision, activation recomputation, KV-cache serving, and a fully synchronous GPU training/serving framework for dense and sparse parameter updates.
- **Results:** Offline, TokenMerge (Concat, 250) cuts FLOPs from **3.73e9 to 3.03e9** while improving AUC by **1.58%** and reducing LogLoss by **3.48%**; adding InnerTrans gives **+1.63% AUC**. The full model beats the strongest Transformer baseline by **+0.21% AUC**. Scaling follows a power law with **R²=0.987** for parameters and **0.967** for FLOPs. Online at Douyin Ads, ADSS/ADVV improve **+1.063%/+1.168%** (live streaming), **+2.097%/+2.151%** (short video), **+1.816%/+1.407%** (mall). At Douyin E-commerce, Order/U and GMV/U improve **+7.9222%/+6.5404%** (live) and **+4.6125%/+5.2771%** (short video).
- **Comparison / significance:** The paper is notable for matching offline scaling laws with two different online domains. The token-merge design is a practical alternative to full long-context attention when latency and throughput are first-class constraints.
- **Links:** [ACM](https://dl.acm.org/doi/10.1145/3705328.3748065) · [arXiv 2505.04421](https://arxiv.org/abs/2505.04421)

---

## 13. Recent industry preprints

### 13.1 OneRec-Think: In-Text Reasoning for Generative Recommendation
《OneRec-Think：生成式推荐中的文本内推理》

- **Authors / affiliation:** Zhanyu Liu, Shiyao Wang, Xingmei Wang, Rongzhou Zhang, Jiaxin Deng, Honghui Bao, Jinghao Zhang, Wuchao Li, Pengfei Zheng, Xiangyu Wu, Yifei Hu, Qigen Hu, Xinchen Luo, Lejian Ren, Zixing Zhang, Qianqian Wang, Kuo Cai, Yunfan Wu, Hongtao Cheng, Zexuan Cheng, Lu Ren, Huanjie Wang, Yi Su, Ruiming Tang, Kun Gai, Guorui Zhou. Kuaishou Inc. arXiv 2025; venue not confirmed.
- **Problem:** Existing generative recommenders such as OneRec are implicit predictors. They lack explicit, controllable reasoning, which is a core advantage of LLMs.
- **Method / innovation:** A unified dialogue-reasoning-recommendation framework with three stages: (1) **Itemic Alignment**, cross-modal item-text alignment for semantic grounding; (2) **Reasoning Activation**, reasoning scaffolding that activates LLM reasoning in the recommendation context; (3) **Reasoning Enhancement**, a recommendation-specific reward that accounts for the multi-validity of user preferences. A **Think-Ahead** architecture separates reasoning from serving so the model can be deployed industrially.
- **Results:** State-of-the-art on public recommendation benchmarks. In a one-week online A/B test on Kuaishou, it achieves **+0.159% App Stay Time**, validating that explicit reasoning can survive production latency constraints.
- **Comparison / significance:** The paper is a direct answer to the "generative recommenders are black boxes" critique. The small online gain is still meaningful at Kuaishou scale; the architectural contribution is making reasoning compatible with serving.
- **Links:** [arXiv 2510.11639](https://arxiv.org/abs/2510.11639)

### 13.2 Principled Synthetic Data Enables the First Scaling Laws for LLMs in Recommendation
《原则化合成数据实现推荐中 LLM 的首个 Scaling Law》

- **Authors / affiliation:** Benyu Zhang, Qiang Zhang, Jianpeng Cheng, Hong-You Chen, Qifei Wang, Wei Sun, Shen Li, Jia Li, Jiahao Wu, Qunshu Zhang, Neeraj Bhatia, Xiangjun Fan, Hong Yan. Meta. arXiv 2026; ICML 2026 submission, acceptance not confirmed.
- **Problem:** LLM-based recommenders lack predictable scaling laws, likely because raw user interaction data is noisy, biased, and incomplete for continual pre-training (CPT).
- **Method / innovation:** A layered synthetic-data generator that builds a curated, pedagogical curriculum for the LLM. Instead of CPT on raw logs, the model learns from structured, high-quality recommendation-specific data across multiple modalities.
- **Results:** Standard sequential models trained on the synthetic data significantly outperform models trained on real data — **+130% recall@100 for SasRec** in downstream ranking. The paper reports the first robust **power-law scaling** for an LLM continually pre-trained on recommendation data, with consistent, predictable perplexity reduction across synthetic modalities.
- **Comparison / significance:** This flips the usual recommendation-data narrative: the bottleneck is data quality and structure, not merely scale. If the scaling law holds, it gives rec-LLM teams a compute-allocation tool analogous to NLP scaling laws.
- **Links:** [arXiv 2602.07298](https://arxiv.org/abs/2602.07298)

---

## Cross-cutting observations

1. **Industrial recommendation is being rebuilt around hardware and streaming constraints, not just model capacity.** RankMixer fixes MFU before scaling parameters; LONGER makes long-sequence attention serveable; DLL resolves the listwise/streaming conflict; HOBA puts LLM reasoning only at the slow bidding layer. The common pattern is to move expensive computation to where it is amortizable.
2. **Generative recommendation is maturing into a systems field.** DualGR wins a WWW short-paper award for decoding constraints and exposure-aware negatives; BEAR fixes the SFT/beam-search mismatch; OneRec-Think makes reasoning deployable; GenCI ties generative intent modeling back to candidate-aware CTR. The open problems are now tokenization, decoding, reward design, and serving.
3. **The reliability agenda is stronger than the capability agenda.** LLMs Get Lost quantifies multi-turn unreliability; Does RL Really Incentivize Reasoning? shows RLVR narrows rather than expands the base model's reasoning boundary; Infini-gram mini exposes benchmark contamination up to 74.2% in GSM8K. Measurement papers are doing more to constrain claims than new benchmark SOTAs.
4. **Agents are moving from "execute everything" to "predict, then verify".** ForeAgent uses a calibrated predictor to avoid expensive ML runs; ReconVLA reconstructs the gaze region instead of generating future frames; NitroGen uses gameplay video as a large-scale action prior. The shared bet is that a cheap internal model can allocate expensive external computation.
5. **Award committees rewarded simple mechanisms with strong evidence.** Gated Attention is a sigmoid gate; JustGRPO is standard GRPO without arbitrary order; High-Accuracy Sampling is a complexity result; LLM2CLIP is contrastive caption-space fine-tuning. The common thread is not architectural novelty for its own sake, but a precise diagnosis of why the obvious approach fails.
6. **Chinese industrial labs dominate the production-recommendation track.** ByteDance (RankMixer, LONGER), Kuaishou (HOBA, DLL, DualGR, OneRec-Think), Tencent/WeChat (GenCI), and Alibaba (Gated Attention) account for most deployed results. The remaining gap is not algorithmic; it is access to large-scale A/B infrastructure and the willingness to publish negative systems findings.

---

## Provenance & caveats

- Official pages used: ICML/PMLR, NeurIPS proceedings and virtual site, ICLR proceedings, AAAI OJS, ACL Anthology, ACM DL, CVF, arXiv abs/PDF, and author project pages.
- Award status verified where possible: ICML 2026 Outstanding (Flexibility Trap, High-Accuracy Sampling); NeurIPS 2025 Runner-up (Does RL Really Incentivize); ICLR 2026 Best Paper (LLMs Get Lost); EMNLP 2025 Best Paper (Infini-gram mini); WWW 2026 Best Short Paper (DualGR). Gated Attention is a NeurIPS 2025 paper, but its exact award label remains disputed (Best Paper vs Runner-up); ReconVLA's AAAI 2026 outstanding status remains tentative.
- Venue caveats: OneRec-Think is arXiv-only in this edition; its venue is not confirmed. The Meta synthetic-data paper is an **ICML 2026 submission**, not a confirmed acceptance, and is labeled accordingly. ReasonRec is **Findings of ACL 2026**, not ACL main.
- Numerical caveats: all numbers are from the papers' reported tables/abstracts unless explicitly marked as prior wiki notes. No numbers were inferred from secondary blog summaries. HOBA's exact A/B figures and GenCI's exact AUC/RelaImpr table are marked as prior-note values because they could not be re-confirmed from the official PDF/metadata in this run. The `+0.95` DLL offline result is **+0.95pp GAUC**, matching the ACM abstract.
- Deduplication: this edition avoids the award-only set in `wiki/synthesis/2026-10-21/conference-digest.md`; it adds deeper industrial results (RankMixer, LONGER, HOBA, DLL, DualGR, GenCI) and newer 2026 papers (BEAR, OneRec-Think, Meta synthetic data) that were not covered there.
- Known weak area: KDD 2026 best-paper awards and AAAI 2026 full award metadata were not independently recoverable from the official pages during this run; the KDD entries here are accepted papers with production results, not award claims.
