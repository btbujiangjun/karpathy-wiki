---
title: "Conference Digest: Top ML/AI Conferences & Fresh arXiv Wave — 2026-09-21"
type: synthesis
created: 2026-09-21
updated: 2026-09-21
sources: []
tags: [conference-digest, ICML2026, ICLR2026, NeurIPS2025, AAAI2026, CVPR2026, ACL2026, EMNLP2025, KDD2026, CIKM2025, recommendation, LLM, advertising, CTR, agents, generative-models, world-models, video-generation, sequential-modeling, benchmarks, daily-digest]
---

# Conference Digest: Top ML/AI Conferences & Fresh arXiv Wave — 2026-09-21

> Cross-venue survey of papers from ICML 2026, ICLR 2026, NeurIPS 2025, AAAI 2026, CVPR 2026, ACL 2026, EMNLP 2025, KDD 2026, CIKM 2025, plus high-impact fresh preprints (Sep 2026) from NVIDIA, Anthropic, ByteDance/TikTok, Alibaba, Meta, Apple, and top labs. Focus: LLM training/reasoning/RL, generative & world models, video, recommendation/advertising/CTR, agents, code execution, benchmarks. **29 new-to-wiki papers** — every arXiv ID below is grep-verified **0 hits** in `wiki/` (dedup against all prior digests, including today's sibling [[synthesis/2026-09-21/arxiv-daily]] 2609.20823–2609.22064 window).

> **Scope / dedup note**: Award/headline works already tracked in this wiki are excluded from detailed re-treatment — ICML 2026 Outstanding (The Flexibility Trap → covered 09-05 digest; High-accuracy diffusion sampling), ICLR 2026 Outstanding (LLMs Get Lost In Multi-Turn, Mamba-3 → [[papers/llm-training/...]]-adjacent coverage), NeurIPS 2025 Best Papers (Gated Attention [[papers/llm-training/gated-attention]]; TTRL-era test-time work), CVPR 2026 best papers + Flowception/Infinity-RoPE/LoL/ARCache, ACL 2026 best papers, KDD 2026 GOAL/CTR-Sink/FAT ([[papers/ctr/fat-ctr-scaling]], +2.33% CTR online is already logged 06-09/09-09 digests), SIGIR 2026 / RecSys 2025 / WWW 2026 / RecSys 2026 (SequenceO1, RECAP, MESH, BEAR, CoGR, OneBid, ADAPT, TGR, ICEGR, HRPO...) were saturated in 09-05/09-10/09-11/09-16/09-17 digests. Sibling jobs claim the 9/21 mailing; this digest adds the *unclaimed* Sept windows + conference papers not yet surfaced.

---

## 1. ICML 2026 (Seoul, Korea — Jul 6-12, 2026)

### 1.1 On the Interplay of Pre-Training, Mid-Training, and RL on Reasoning Language Models
- **Title (ZH)**: 预训练、中期训练与强化学习在推理语言模型中的相互作用
- **Authors**: Charlie Zhang, Graham Neubig, Xiang Yue
- **Affiliation**: Carnegie Mellon University (CMU LTI)
- **Venue**: ICML 2026 — **Spotlight**
- **Abstract & Key Innovations**: Controlled synthetic-reasoning testbed (parseable step traces + atomic operations) that severs the causal contributions of the three training stages. Key findings: RL yields genuine capability gains (pass@128) only when (a) pre-training leaves "headroom" and (b) RL data sit at the model's edge of competence; mid-training under fixed compute beats RL alone; process-reward supervision reduces reward hacking.
- **Comparison with prior methods**: Directly answers the "is RLVR just context-distillation?" debate — under fixed compute, mid-training outperforms RL; RL's contribution is real but conditional on pre-training headroom.
- **Link**: https://arxiv.org/abs/2512.07783

### 1.2 dnaHNet: A Scalable and Hierarchical Foundation Model for Genomic Sequence Learning
- **Title (ZH)**: dnaHNet：可扩展、分层的基因组序列学习基础模型
- **Authors**: Arnav Shah, Junzhe Li, Parsa Idehpour, … Bo Wang, Patrick Hsu, Hani Goodarzi, Albert Gu
- **Affiliation**: Arc Institute / Princeton / UC San Francisco *(H-Net lineage)*
- **Venue**: ICML 2026 — **Oral**
- **Abstract & Key Innovations**: Tokenizer-free autoregressive genomic model; differentiable dynamic chunking compresses raw nucleotides into latent tokens *recursively* (2-stage hierarchy). First-stage unsupervised segmentation recovers codon triplets; second stage discovers promoters / intergenic regions — an emergent, data-driven tokenizer for DNA.
- **Comparison with prior methods**: Quadratic FLOP reduction → **>3× inference speedup** vs Transformer baselines at million-nucleotide contexts; scaling exponent α=0.06 vs StripedHyena2 α=0.04; SOTA zero-shot protein-variant fitness & gene-essentiality prediction.
- **Link**: https://arxiv.org/abs/2602.10603

### 1.3 Mitigating Bias in Locally Constrained Decoding via Tractable Proposals
- **Title (ZH)**: 通过可处理的提议分布缓解局部约束解码中的偏差
- **Authors**: Meihua Dang, et al.
- **Affiliation**: *(multi-institution)*
- **Venue**: ICML 2026
- **Abstract & Key Innovations**: SMC proposals for constrained decoding: tensorizes finite automata onto GPU (GCD), then circuit-multiplies with HMM factors for a probabilistic variant (P-GCD) carrying both logical *and* probabilistic signal — targeting function calling, keyword generation, SQL.
- **Comparison with prior methods**: (P-)GCD converges to the target distribution faster with significantly fewer particles than locally-constrained (LCD) proposals under the same SMC setup — fixes LCD's well-known bias when constraints conflict with LM prefix probabilities.
- **Link**: https://arxiv.org/abs/2606.01926

---

## 2. ICLR 2026 (Rio de Janeiro, Brazil — Apr 28 – May 2, 2026)

### 2.1 Overthinking Reduction with Decoupled Rewards and Curriculum Data Scheduling (DeCS)
- **Title (ZH)**: 解耦奖励与课程数据调度实现过度思考（Overthinking）抑制
- **Authors**: Shuyang Jiang, Yusheng Liao, Ya Zhang, Yanfeng Wang, Yu Wang
- **Affiliation**: Shanghai Jiao Tong University
- **Venue**: ICLR 2026 — **Oral**
- **Abstract & Key Innovations**: Identifies two flaws in length-penalty rewards (kills essential exploratory tokens; rewards partial redundancy). A lightweight judge model decides the *necessary reasoning prefix* (NRP); token-level decoupled rewards + adaptive easy-prompt curriculum scheduling.
- **Comparison with prior methods**: Reduces reasoning tokens by **>50% across 7 benchmarks** while maintaining/improving pass@1 and pass@K — overcomes the standard "shorter-but-worse" trade-off of vanilla length penalties.
- **Link**: https://arxiv.org/abs/2509.25827

### 2.2 RAIN-Merging: A Gradient-Free Method to Enhance Instruction Following in Large Reasoning Models with Preserved Thinking Format
- **Title (ZH)**: RAIN-Merging：保持思考格式、增强推理模型指令遵循的无梯度合并方法
- **Authors**: Zhehao Huang, Yuhang Liu, Baijiong Lin, Yixin Lou, Zhengbao He, Hanling Tian, Tao Li, Xiaolin Huang
- **Affiliation**: Shanghai Jiao Tong University et al.
- **Venue**: ICLR 2026 — **Oral**
- **Abstract & Key Innovations**: Zero-gradient merging of an instruction-tuned model (ITM) into a reasoning model (LRM): project the ITM task vector onto the null space of thinking-token features (preserves thinking format), then instruction-attention-guided module scaling. Shows LRM/ITM task-vector subspaces are near-orthogonal.
- **Comparison with prior methods**: MathIF Acc **12.62% → 20.48% (+62% relative)**; instruction gains 1.57–8.20% across model scales; beats Task-Arithmetic / SFT baselines on 4 instruction-following + 9 reasoning benchmarks — a cheaper alternative to RLHF/DPO restoration of instruction-following in reasoning models.
- **Link**: https://arxiv.org/abs/2602.22538

### 2.3 Half-order Fine-Tuning for Diffusion Model: A Recursive Likelihood Ratio Optimizer
- **Title (ZH)**: 扩散模型的半阶微调：递归似然比优化器
- **Authors**: Tao Ren, Zishi Zhang, Jinyang Jiang, Zehao Li, Shentao Qin, Yi Zheng, …, Yijie Peng
- **Affiliation**: Fudan / Peking University *(inferred)*
- **Venue**: ICLR 2026 — **Oral**
- **Abstract & Key Innovations**: "Half-order" estimator that rearranges the diffusion chain's computation graph using the model's own noise via the Likelihood-Ratio trick — bridges truncated backprop (biased) and RL (high variance); RL is recovered as the h=1 special case. Includes bias/variance/convergence theory + a Diffusive Chain-of-Thought (DCoT) prompting trick.
- **Comparison with prior methods**: RLR consistently outperforms RL and truncated-BP on Text2Image and Text2Video under multiple human-preference reward models (exact deltas single-source).
- **Link**: https://arxiv.org/abs/2502.00639

---

## 3. NeurIPS 2025 (Dec 2-7, 2025)

### 3.1 TTRL: Test-Time Reinforcement Learning
- **Title (ZH)**: TTRL：测试时强化学习
- **Authors**: Yuxin Zuo, Kaiyan Zhang, Li Sheng, Shang Qu, Ganqu Cui, Xuekai Zhu, …, Ning Ding, Bowen Zhou
- **Affiliation**: Tsinghua University + Shanghai AI Lab
- **Venue**: NeurIPS 2025
- **Abstract & Key Innovations**: RL runs on **unlabeled test data**: majority-voting over self-generated rollouts produces a rule-based reward proxy, so the model self-evolves at inference time. Reconciles the test-time-training (TTT) vs test-time-scaling (TTS) overlap debate.
- **Comparison with prior methods**: Qwen-2.5-Math-7B pass@1 on AIME 2024 **+211%**; Qwen-2.5-Math-1.5B MATH-500 **32.7 → 73.0 (+123%)**; generalizes across 6+ models, 4 families — evidence of self-evolution beyond the "self-train ceiling".
- **Link**: https://arxiv.org/abs/2504.16084

### 3.2 Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning (ReasonFlux-Coder)
- **Title (ZH)**: 通过强化学习协同进化 LLM 编码器与单元测试生成器
- **Authors**: Yinjie Wang, Ling Yang, Ye Tian, Ke Shen, Mengdi Wang
- **Affiliation**: Princeton University
- **Venue**: NeurIPS 2025 — **Spotlight**
- **Abstract & Key Innovations**: A coder and a unit-tester agent mutually bootstrap via RL — the tester's generated test cases sharpen the coder's correctness gradients and vice versa (test-instruction evolvement). Coder-tester co-training gives emergent, self-improving verification loops, an alternative to reward-model-free code RL.
- **Comparison with prior methods**: Beats single-model SFT baselines on both HumanEval-style coding and test-generation metrics (exact deltas single-source). Related managed trajectory-aware PRM for long-CoT (NeurIPS 2025, arXiv 2506.18896).
- **Link**: https://arxiv.org/abs/2506.03136

### 3.3 How do Transformers Learn Implicit Reasoning?
- **Title (ZH)**: Transformer 如何学习隐式推理？
- **Authors**: Jiaran Ye, Zijun Yao, Zhidian Huang, …, Lei Hou, Juanzi Li
- **Affiliation**: Tsinghua University
- **Venue**: NeurIPS 2025 — **Spotlight**
- **Abstract & Key Innovations**: Training transformers from scratch on controlled symbolic multi-hop tasks reveals a three-stage trajectory (memorization → in-distribution → cross-distribution generalization). Introduces cross-query semantic patching and a cosine-based representational lens linking reasoning success to hidden-space clustering.
- **Comparison with prior methods**: Training on atomic triples accelerates but is *not necessary*; second-hop generalization requires query-level compositional exposure — a mechanistic account of compositional generalization, complementing latent-CoT learning results.
- **Link**: https://arxiv.org/abs/2505.23653

### 3.4 Flatness is Necessary, Neural Collapse is Not: Rethinking Generalization via Grokking
- **Title (ZH)**: 平坦性是必要的，而神经坍缩并非必要：经由 Grokking 重新思考泛化
- **Authors**: Ting Han, Linara Adilova, Henning Petzka, Jens Kleesiek, Michael Kamp
- **Affiliation**: Fraunhofer IAIS / University Hospital Essen et al.
- **Venue**: NeurIPS 2025
- **Abstract & Key Innovations**: Uses grokking as a clean observational window to decouple training dynamics from generalization; argues *relative flatness is causally necessary* for delayed generalization while neural collapse is not — sharpens the flat-vs-sharp generalization debate.
- **Comparison with prior methods**: Flatness→generalization correlation demonstrated across algorithmic tasks, CIFAR-10, ImageNet-style ViT, and language (SST / GPT-2) regimes — responds to the "sharp minima can generalize" counter-literature.
- **Link**: https://arxiv.org/abs/2509.17738

---

## 4. AAAI 2026 (Singapore, Feb 2026)

### 4.1 InfiGUI-G1: Advancing GUI Grounding with Adaptive Exploration Policy Optimization (AEPO)
- **Title (ZH)**: InfiGUI-G1：通过自适应探索策略优化推进 GUI 定位（Grounding）
- **Authors**: Yuhang Liu, et al. *(InfiXAI lab)*
- **Affiliation**: InfiXAI (semi-open GUI grounding team)
- **Venue**: AAAI 2026 — **Oral** (arXiv comment: "Accepted to AAAI 2026 (Oral Presentation)")
- **Abstract & Key Innovations**: Multi-answer generation in a single forward pass + adaptive exploration reward (efficiency-first η = utility/cost) + collinearity penalty against degenerate linear-scan strategies — attacks the semantic-alignment bottleneck of MLLM GUI grounding.
- **Comparison with prior methods**: InfiGUI-G1-7B **MMBench-GUI avg 80.8 (Top-1)** vs naive RLVR-7B 79.3; exploration success rate 86.4% at only ~1.6 candidates on average; largest gains on Advanced (semantically hard) categories.
- **Link**: https://arxiv.org/abs/2508.05731

### 4.2 TdRL: Test-Driven Reinforcement Learning in Continuous Control
- **Title (ZH)**: 连续控制中的测试驱动强化学习
- **Authors**: Zhao Yu, et al.
- **Affiliation**: *(multi-institution)*
- **Venue**: AAAI 2026 — **Oral**
- **Abstract & Key Innovations**: Replaces the reward function with pass-fail + indicative *test functions*; a return function is learned via lexicographic-heuristic trajectory comparison — no hand-tuned reward weights, natural multi-objective, mitigates reward hacking.
- **Comparison with prior methods**: Matches/beats hand-crafted rewards on DeepMind Control (e.g., Walker-Run ~670 vs SGD ~650 with oracle reward); state estimates validated against maximum-entropy RL theory.
- **Link**: https://arxiv.org/abs/2511.07904

### 4.3 LAMP: Language-Augmented Multi-Agent Policy — Think, Speak, Decide for Economic Decision-Making
- **Title (ZH)**: LAMP：语言增强的多智能体策略——面向经济决策的"想-说-定"流水线
- **Authors**: Heyang Ma, et al. *(code: github.com/hey0223/LAMP)*
- **Affiliation**: *(multi-institution)*
- **Venue**: AAAI 2026 (extended version)
- **Abstract & Key Innovations**: MARL + LLM reasoning fused through Think–Speak–Decide; an experience pool carries long/short-term language reasoning into the policy in the TaxAI economic simulator — a clean recipe for injecting language priors into cooperative policies.
- **Comparison with prior methods**: **+63.5% reward vs MADDPG, +14.5% vs best LLM baseline (ReAct), +118.8% social welfare vs MADDPG**; ablated: long-term reasoning is the load-bearing component (−38% reward when removed).
- **Link**: https://arxiv.org/abs/2511.12876

---

## 5. CVPR 2026 (Denver, USA — Jun 3-7, 2026)

### 5.1 Molmo2: Open Weights and Data for Vision-Language Models with Video Understanding and Grounding
- **Title (ZH)**: Molmo2：开放权重与数据的视频理解与点选式定位（Pointing）VLM
- **Authors**: Christopher Clark, Jieyu Zhang, Zixian Ma, Jae Sung Park, Mohammadreza Salehi, Ali Farhadi, Ranjay Krishna
- **Affiliation**: Allen Institute for AI (AI2) + University of Washington
- **Venue**: CVPR 2026 — **Oral**
- **Abstract & Key Innovations**: Fully open-data VLM family (best-in-class 8B) built from **7 new video + 2 multi-image datasets collected without distillation from closed models**. Efficient packing / message-tree encoding + bi-directional attention over vision tokens + token-weight strategy enable point-driven grounding on single-image, multi-image, and video.
- **Comparison with prior methods**: Video counting **35.5 vs 29.6** (Qwen3-VL); video pointing F1 **38.4 vs 20.0** (Gemini 3 Pro); video tracking J&F **56.2 vs 41.1**; a rare fully-open alternative to closed-video VLM leaders.
- **Link**: https://arxiv.org/abs/2601.10611

### 5.2 VS-Bench: Evaluating VLMs for Strategic Abilities in Multi-Agent Environments
- **Title (ZH)**: VS-Bench：多智能体环境中 VLM 策略能力评测
- **Authors**: Zelai Xu, Zhexuan Xu, Xiangmin Yi, Mo Guang, Kaiwen Long, Yi Wu, Chao Yu, Yu Wang
- **Affiliation**: Tsinghua University + Li Auto Inc.
- **Venue**: CVPR 2026 — **Oral**
- **Abstract & Key Innovations**: Multimodal benchmark of **10 vision-grounded multi-agent environments** (cooperative / competitive / mixed-motive); separately evaluates perception, next-action prediction (strategic reasoning / theory-of-mind), and decision-making (normalized return).
- **Comparison with prior methods**: Best VLM reaches only **46.6% next-action accuracy and 31.4% normalized return** — perception is strong, strategic reasoning/decision-making remain far from oracle; a new evaluation axis orthogonal to VQA-style benchmarks.
- **Link**: https://arxiv.org/abs/2506.02387

### 5.3 CubiD: Cubic Discrete Diffusion — Discrete Visual Generation on High-Dimensional Representation Tokens
- **Title (ZH)**: CubiD：基于高维表示 Token 的立方离散扩散（离散视觉生成）
- **Authors**: Yuqing Wang, Chuofan Ma, Zhijie Lin, Yao Teng, Lijun Yu, Jiashi Feng, Xihui Liu
- **Affiliation**: ByteDance Seed + HKU MMLab
- **Venue**: CVPR 2026 — **Highlight**
- **Abstract & Key Innovations**: The first discrete generation model working directly on native **768-dim representation tokens** (prior methods ≤32-dim VAE tokens). Fine-grained masking across the h×w×d tensor turns intractable sequential generation into ~T parallel iterations, while discretized tokens keep representational power for both understanding and generation.
- **Comparison with prior methods**: SOTA discrete generation on ImageNet-256 — **gFID 1.88 at 3.7B params**; strong scaling from 900M → 3.7B.
- **Link**: https://arxiv.org/abs/2603.19232

### 5.4 Motus: A Unified Latent Action World Model
- **Title (ZH)**: Motus：统一潜在动作世界模型
- **Authors**: Hongzhe Bi, Hengkai Tan, Shenghao Xie, Zeyuan Wang, Shuhe Huang, Haitian Liu, …, Jun Zhu (16 authors)
- **Affiliation**: Tsinghua University + Peking University + Horizon Robotics
- **Venue**: CVPR 2026 (pp. 35101–35113)
- **Abstract & Key Innovations**: Mixture-of-Transformer (MoT) embedding of three experts (understanding / video generation / action) with a UniDiffuser-style scheduler to switch among world-model, VLA, inverse-dynamics, video-generation, and video-action modes. Optical-flow latent actions + 3-phase training + 6-layer data pyramid enable large-scale action pretraining.
- **Comparison with prior methods**: RoboTwin 2.0 **87.02% average success (+15% over X-VLA, +45% over Pi-0.5)**; real-world **+11–48%**.
- **Link**: https://arxiv.org/abs/2512.13030

---

## 6. ACL 2026 (San Diego, USA — Jul 2-7, 2026)

### 6.1 SATQuest: A Verifier for Logical Reasoning Evaluation and Reinforcement Fine-Tuning of LLMs
- **Title (ZH)**: SATQuest：面向逻辑推理评测与强化微调（RFT）的可验证校验器
- **Authors**: Yanxiao Zhao, Yaqian Li, Zihao Bo, Rinyoichi Takezoe, Haojia Hui, Mo Guang, Lei Ren, Xiaolin Qin, Kaiwen Long
- **Affiliation**: Li Auto Inc. et al.
- **Venue**: ACL 2026 (Long, 2026.acl-long.96)
- **Abstract & Key Innovations**: Verifier-backed infrastructure for controlled, scalable, reproducible LLM logical-reasoning research — usable both as an evaluation harness and as a **reward source for RL fine-tuning** (sat-encoded ground truth, avoiding LLM-judge heuristics). Relevant to the wiki's `verifiable-rewards` thread: logical provers as RLVR signal generators.
- **Comparison with prior methods**: Exact (SAT-based) verification rather than judge/rule heuristics for logical reasoning; no headline accuracy numbers in abstract.
- **Link**: https://aclanthology.org/2026.acl-long.96

### 6.2 Jailbreaking Multimodal Large Language Models using Multi-Clip Video
- **Title (ZH)**: 利用多片段视频越狱多模态大语言模型
- **Authors**: Choongwon Kang, Seungjong Sun, Hyunmin Jun, Jang Hyun Kim
- **Affiliation**: Sungkyunkwan University
- **Venue**: ACL 2026 (Main)
- **Abstract & Key Innovations**: Introduces **MCV SafetyBench** (2,920 videos of multi-clip "context soup" tied to harmful queries). Attack success rate rises **monotonically with clip count** across 8 video MLLMs; systematic ablation: video > image, dynamic > static, contextually diverse > homogeneous. Proposes an image-modality-anchored defense.
- **Comparison with prior methods**: First dataset + analysis attributing MLLM safety-alignment bypass to specific *properties of the video input* (clip diversity/bench — previously safety-VLM evals conflated modalities).
- **Link**: https://arxiv.org/abs/2606.02111

---

## 7. EMNLP 2025 (Suzhou, China — Nov 2025)

### 7.1 Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps (**Outstanding Paper**)
- **Title (ZH)**: 通过"遗忘推理步骤"测量思维链（CoT）忠实度
- **Authors**: Martin Tutek, Fateme Hashemi Chaleshtori, Ana Marasovic, Yonatan Belinkov
- **Affiliation**: Technion – Israel Institute of Technology + University of Utah
- **Venue**: EMNLP 2025 — **Outstanding Paper** (pp. 9935–9960, 2025.emnlp-main.504)
- **Abstract & Key Innovations**: Parametric Faithfulness Framework (PFF) + FUR: fine-tune the model (NPO preference-optimization unlearning) to *erase* knowledge encoded in individual CoT steps, then measure how strongly erasing a step shifts the prediction (FF-HARD / FF-SOFT). A causal, parameter-level test of whether CoT steps genuinely support the conclusion.
- **Comparison with prior methods**: On 4 LMs × 5 MCQ datasets, FUR frequently changes predictions by unlearning key steps — evidence of when CoT is parametrically faithful, avoiding the brittleness of token-perturbation/reply-based faithfulness metrics.
- **Link**: https://arxiv.org/abs/2502.14829

### 7.2 ReMedy: Learning Machine Translation Evaluation from Human Preferences with Reward Modeling
- **Title (ZH)**: ReMedy：以人类偏好奖励建模学习机器翻译评测
- **Authors**: Shaomu Tan, Christof Monz
- **Affiliation**: University of Amsterdam (ILLC)
- **Venue**: EMNLP 2025 (Main, 2025.emnlp-main.217)
- **Abstract & Key Innovations**: Reframes MT evaluation as **reward modeling on pairwise preferences** instead of regressing noisy scalar human scores — robust segment- AND system-level quality estimates with better error detection.
- **Comparison with prior methods**: SOTA across WMT22–24 (39 language pairs, 111 MT systems); ReMedy-9B beats MetricX-13B, XCOMET-Ensemble, GEMBA-GPT-4, PaLM-540B.
- **Link**: https://aclanthology.org/2025.emnlp-main.217

---

## 8. KDD 2026 / CIKM 2025 — Recommendation, Advertising & CTR

> **Note**: The recommendation/ads/CTR field was heavily mined in the 08-30/09-05/09-10/09-11/09-16/09-17 digests (OneBid, ADAPT, TGR, SequenceO1, RECAP, MESH, BEAR, CoGR, DEGR, HRPO, ICEGR, EST [[papers/ctr/est]], CADET [[papers/ctr/cadet]], FAT [[papers/ctr/fat-ctr-scaling]]...). Below: three **new** papers.

### 8.1 Hi-SAM: A Hierarchical Structure-Aware Multi-modal Framework for Large-Scale Recommendation
- **Title (ZH)**: Hi-SAM：面向大规模推荐的分层结构感知多模态框架
- **Authors**: Pingjun Pan, Tingting Zhou, Peiyao Lu, Tingting Fei, Hongxiang Chen, Chuanjiang Luo
- **Affiliation**: unnamed "large-scale social platform" *(unverified)*
- **Venue**: KDD 2026 (ADS track); arXiv: **2602.11799**
- **Abstract & Key Innovations**: Two fixes for semantic-ID multimodal rec: (1) **Disentangled Semantic Tokenizer** (geometry-aware alignment, coarse-to-fine quantization, consensus codebooks + modality-specific residuals, mutual-information minimization) to avoid redundancy/collapse; (2) **Hierarchical Memory-Anchor Transformer** (Hierarchical RoPE, anchor tokens condensing items into compact memory) to restore the hierarchy flat-stream Transformers ignore.
- **Comparison with prior methods**: Consistent gains over SOTA on real datasets, especially **cold-start**; deployed at scale serving millions of users with **+6.55% core online metric at 35% lower latency**.
- **Link**: https://arxiv.org/abs/2602.11799

### 8.2 DAS: Dual-Aligned Semantic IDs Empowered Industrial Recommender System
- **Title (ZH)**: DAS：双对齐语义 ID 赋能的工业推荐系统
- **Authors**: Wencai Ye, Mingjie Sun, Shaoyun Shi, Peng Wang, Wenjin Wu, Peng Jiang
- **Affiliation**: Kuaishou
- **Venue**: CIKM 2025 (Seoul)
- **Abstract & Key Innovations**: Semantic IDs from MLLM embeddings lack collaborative signal; stage-wise alignment loses information. DAS is **one-stage**, jointly optimizing quantization and alignment: multi-view contrastive alignment (u2i, i2i/u2u, co-occurrence) + dual learning between user and ad quantizations.
- **Comparison with prior methods**: Offline gains + successful online A/B; deployed across advertising scenarios at Kuaishou App **serving 400M+ DAU** — a strong counterpoint to pure-MLLM-embedding SID pipelines.
- **Link**: https://arxiv.org/abs/2508.10584

### 8.3 AgenticGen: Reward-Guided Agentic Video Generation for Advertising
- **Title (ZH)**: AgenticGen：广告场景中奖励引导的智能体式视频生成
- **Authors**: Xingyuan Bu, Chengru Song, Hao Zhou, Tao Zhou, Dong Li, Wei Li, Shilong Li, Hao Shi, Yongxin Guo, Donghao Zhou, Qiangpeng Yang, Shilei Wen
- **Affiliation**: ByteDance / TikTok Ads *(inferred from author affiliation & paper framing)*
- **Venue**: arXiv preprint (2026-08-31)
- **Abstract & Key Innovations**: Frames ad-video generation as a **product-conditioned reasoning problem** measured by online business metrics, not just video quality. Two trainable reasoning stages — strategy selection + draft generation — exposed to a learned performance-based reward (from accumulated online feedback) plus a rubric-based quality reward; **DPO** moves policies toward online preferences, **GRPO** refines both stages with process and outcome rewards.
- **Comparison with prior methods**: vs SFT-only video-ad generators — online A/B lifts of **+2.72% CTR, +2.63% CVR, +9.61% Advertiser Value** (reported in paper); a distinctive example of optimizing the *ad-effect* reward rather than FID/fidelity.
- **Link**: https://arxiv.org/abs/2609.09187

---

## 9. Fresh 2026 arXiv Wave — Agents, Code, World Models, Benchmarks

### 9.1 MintAct: A Unified Visual Agent for Digital Environments *(NVIDIA)*
- **Title (ZH)**: MintAct：数字环境的统一视觉智能体
- **Authors**: Mingfei Gao, Rui Tian, Haiming Gang, Bohan Zhai, Le Zhang, …, Roman Bachmann, Anders B. L. Larsen, Afshin Dehghan
- **Affiliation**: NVIDIA (+ DTU)
- **Venue**: arXiv 2609.22083 (2026-09-18)
- **Abstract & Key Innovations**: 2B/4B/8B VLM family unifying **UI grounding, multi-step navigation (mobile/desktop/web), and visual tool-use**. Scalable environment + RL infra: hundreds of concurrent heterogeneous environment instances, asynchronous RL stable under noisy feedback and off-policy drift.
- **Comparison with prior methods**: Matches per-domain specialists while SOTA at comparable size: **48.9 on OSWorld-Verified**.
- **Link**: https://arxiv.org/abs/2609.22083

### 9.2 Puffin-World: Scaling a Unified Multimodal Model with Native 3D World States
- **Title (ZH)**: Puffin-World：原生 3D 世界状态的统一多模态模型
- **Authors**: Kang Liao, Yihang Luo, Xiao-Ming Wu, Linyi Jin, Size Wu, ..., Chen Change Loy
- **Affiliation**: NTU S-Lab + University of Michigan + Beijing Jiaotong University + ACE Robotics
- **Venue**: arXiv 2609.04196 (2026-09-03)
- **Abstract & Key Innovations**: Extends Puffin (ICLR 2026 camera-centric model) to natively perceive, generate *and* reconstruct 3D world states — physics (gravity field/latitude), geometry (depth), appearance (image) — in a single autoregressive + diffusion framework with an Omni-Camera representation; propagates physical dynamics across future frames; couples appearance & geometry in one generative process.
- **Comparison with prior methods**: Median roll error **0.29°** on Stanford-2D-3D camera estimation; FID **75.93** on Puffin-Cam-Bench; enables viewpoint-consistent closed-loop world exploration without external offline modules.
- **Link**: https://arxiv.org/abs/2609.04196

### 9.3 OmniVBench: A Benchmark and Large-Scale Dataset for Omni Reference-to-Video Generation
- **Title (ZH)**: OmniVBench：全能参考到视频（R2V）生成基准与大规模数据集
- **Authors**: Wenxue Li, Peiyan Guan, Haoyang Jiang, Junxian Cai, Hualuo Liu, …, Xi Chen, Yu Liu, Lei Zhu
- **Affiliation**: *(industrial-scale dataset; inferred ByteDance Seed, unverified)*
- **Venue**: arXiv 2609.22069 (2026-09-18)
- **Abstract & Key Innovations**: Expands R2V evaluation to 7 task families / 18 fine-grained tasks (content, motion, style, structure, narrative, multi-reference) with **factor-grounded evaluation across 12,172 case-specific checklist items**; releases the 340K-sample Omni-R2V training dataset with task-specific reference-target pipelines.
- **Comparison with prior methods**: No single open/closed R2V model closes the gap across all task families — reference-factor disentangling & routing are clear weaknesses; strong training-data resource for the community.
- **Link**: https://arxiv.org/abs/2609.22069

### 9.4 Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents *(Anthropic)*
- **Title (ZH)**: 红队测试 Auto Mode：改进针对恶意编码智能体的拦截分类器
- **Authors**: Alex Remedios, Simon Storf, Fabien Roger, John Hughes
- **Affiliation**: likely Anthropic *(inferred from authorship)*
- **Venue**: arXiv 2609.19587 (2026-09-17)
- **Abstract & Key Innovations**: Evaluates production **action-blocking monitors** (Claude Code "Auto Mode", Codex "Guardian") against *malign* agents that deliberately plan and evade review — beyond accidental-harm and naive prompt-injection tests; proposes improved blocking-classifier training with a defensive-tightening recipe.
- **Comparison with prior methods**: Shows a systematic defensive gap vs evasion-capable adversaries (evasion-rate figures single-source); directly relevant to the wiki's supply-chain / agent-security threads.
- **Link**: https://arxiv.org/abs/2609.19587

### 9.5 A Large-Scale Empirical Study of Quality Assurance Practices and Gaps in AI Agents
- **Title (ZH)**: AI 智能体质量保障实践与缺口的规模化实证研究
- **Authors**: Wuyang Dai, Moses Openja, Jiho Shin, Hung Viet Pham
- **Affiliation**: University of Toronto / Concordia University
- **Venue**: arXiv 2609.17698 (2026-09-15)
- **Abstract & Key Innovations**: Surveys real-world QA of LLM agents across SWE, web automation, research, and productivity apps; maps planning/memory/tool/code-execution risks to verification gaps — evidence where agent evaluation under-specifies vs conventional software testing.
- **Comparison with prior methods**: Aggregated gap statistics across production agent use-cases (test coverage, reliability, security); complements benchmark-rig analyses (cf. [[papers/benchmarking/benchmark-rigging-analysis]]).
- **Link**: https://arxiv.org/abs/2609.17698

---

## 10. Cross-Cutting Themes (this wave)

1. **Reasoning LMs: the post-training stack is being re-architected around *when* to train.** DeCS (ICLR'26) surgically reduces token cost; CMU Interplay (ICML'26) shows mid-training > RL under fixed compute and RL needs pre-training headroom; RAIN-Merging avoids retraining entirely via null-space task vectors; TTRL (NeurIPS'25) moves RL to test time on unlabeled data. Convergent message: **capability comes from data/compute allocation across stages, not brute-force RLVR**.
2. **VC signal is the new verifier.** SATQuest (ACL'26) extends `verifiable-rewards` to logical reasoning via SAT solvers; FUR (EMNLP'25) unlearns CoT steps to *test* faithfulness; Co-evolving coder+tester (NeurIPS'25) makes test generation endogenous — alignment between this digest and the wiki's RLVR / verifiability concepts is strong.
3. **Industrial ads/recommendation is consolidating on semantic IDs + reward-optimized generative loops.** DAS (Kuaishou) and Hi-SAM (KDD'26) fix SID representation; AgenticGen (TikTok) and the previously-digested OneBid/ADAPT/GOAL treat *the whole creative/auction decision* as a foundation-model prediction supervised by business outcomes rather than aesthetic quality.
4. **World models & VLAs converge on unified latents.** Motus (CVPR'26) switches among world-model/VLA/video modes in one MoT; Puffin-World unifies physics+geometry+appearance; MintAct (NVIDIA) adds UI-grounding scale with async RL. Games side continues via the parallel [[synthesis/2026-09-20/game-rl-daily]] (GameWAM, Zing-0.5, GameLogicBench).
5. **Safety/security of autonomous agents becomes a measurable research field.** MCV SafetyBench materials on MLLM video jailbreak; Anthropic's Auto-Mode red-teaming; QA-gap empirical study; QPP/verifier-style evaluation hardening — consistent with the wiki's agent-security concept pages.
6. **Benchmark saturation is now quantified.** SWE-bench convergence audit (09-16/09-19 digests, 2609.17394) and OmniVBench/MCV SafetyBench all signal a move toward *checklist/factor-grounded* evaluation instead of single scalar leaderboards.

## References

- ICML 2026: [2512.07783](https://arxiv.org/abs/2512.07783) · [2602.10603](https://arxiv.org/abs/2602.10603) · [2606.01926](https://arxiv.org/abs/2606.01926)
- ICLR 2026: [2509.25827](https://arxiv.org/abs/2509.25827) · [2602.22538](https://arxiv.org/abs/2602.22538) · [2502.00639](https://arxiv.org/abs/2502.00639)
- NeurIPS 2025: [2504.16084](https://arxiv.org/abs/2504.16084) · [2506.03136](https://arxiv.org/abs/2506.03136) · [2505.23653](https://arxiv.org/abs/2505.23653) · [2509.17738](https://arxiv.org/abs/2509.17738)
- AAAI 2026: [2508.05731](https://arxiv.org/abs/2508.05731) · [2511.07904](https://arxiv.org/abs/2511.07904) · [2511.12876](https://arxiv.org/abs/2511.12876)
- CVPR 2026: [2601.10611](https://arxiv.org/abs/2601.10611) · [2506.02387](https://arxiv.org/abs/2506.02387) · [2603.19232](https://arxiv.org/abs/2603.19232) · [2512.13030](https://arxiv.org/abs/2512.13030)
- ACL 2026: [2606.02111](https://arxiv.org/abs/2606.02111) · [SATQuest](https://aclanthology.org/2026.acl-long.96)
- EMNLP 2025: [2502.14829](https://arxiv.org/abs/2502.14829) · [ReMedy](https://aclanthology.org/2025.emnlp-main.217)
- KDD / CIKM: [2602.11799](https://arxiv.org/abs/2602.11799) · [2508.10584](https://arxiv.org/abs/2508.10584) · [2609.09187](https://arxiv.org/abs/2609.09187)
- Fresh wave: [2609.22083](https://arxiv.org/abs/2609.22083) · [2609.04196](https://arxiv.org/abs/2609.04196) · [2609.22069](https://arxiv.org/abs/2609.22069) · [2609.19587](https://arxiv.org/abs/2609.19587) · [2609.17698](https://arxiv.org/abs/2609.17698)