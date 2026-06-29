---
title: "顶会论文专题报告 — 2026年6月全面版（ICML 2026 / AAAI 2026 / NeurIPS 2025 / ICLR 2026 / CVPR 2026 / KDD 2026 / ACL 2026 / EMNLP 2025 / WWW 2026 / SIGIR 2026 / CIKM 2025 / RecSys 2025）"
type: synthesis
created: 2026-06-29
updated: 2026-06-29
sources: []
tags: [conference-digest, icml-2026, neurips-2025, iclr-2026, aaai-2026, cvpr-2026, kdd-2026, acl-2026, emnlp-2025, www-2026, sigir-2026, cikm-2025, recsys-2025, llm, ctr, recommendation, agents, games, generative-models]
---

# 顶会论文专题报告 — 2026年6月全面版

> 覆盖: ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, CVPR 2026, KDD 2026, ACL 2026, EMNLP 2025, WWW 2026, SIGIR 2026, CIKM 2025, RecSys 2025 + arXiv Highlight
> 扫描范围: 2026年6月最新论文, 重点关注工业实验室 (Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, Netflix, NVIDIA, Anthropic, Apple, Amazon)

---

# Part I — 前沿模型架构 (Frontier Model Architectures)

## 1. Mamba-3: Improved Sequence Modeling using State Space Principles

| Field | Detail |
|-------|--------|
| **Title (EN)** | Mamba-3: Improved Sequence Modeling using State Space Principles |
| **Title (ZH)** | Mamba-3: 基于状态空间原理的改进序列建模 |
| **Authors** | Aakash Lahoti, Kevin Y. Li, Berlin Chen, Caitlin Wang, Aviv Bick, J. Zico Kolter, Tri Dao, Albert Gu |
| **Affiliation** | Princeton University, CMU, Together AI |
| **Venue** | arXiv 2603.15569 (ICLR 2026 关联) |
| **Links** | [arXiv](https://arxiv.org/abs/2603.15569) \| [GitHub](https://github.com/state-spaces/mamba) |

**Problem Background:** 随着推理时计算 (test-time compute) 的扩展，Transformer 的二次复杂度在长序列推理中成为效率瓶颈。尽管 Mamba-2 在训练效率上有显著提升，但推理效率仍是核心挑战。

**Key Innovations:**
1. **基于 SSM 离散化的更富表达力的递推关系 (Exponential-Trapezoidal Discretization):** 替代了 Mamba-2 的 Zero-Order Hold (ZOH) 离散化，提升了状态更新的精度。
2. **复数值状态更新 (Complex-Valued State Tracking):** 引入复数值 SSM，使模型能够处理状态追踪任务（如模算术、parity check），这是之前线性模型常失败的任务。
3. **MIMO (Multi-Input Multi-Output) 公式化:** 在不增加解码延迟的前提下，通过多输入多输出投影增强了模型性能。

**Architecture Details:**
- 采用交替的 Mamba-3 和 SwiGLU 块（类似 Llama 架构）
- 添加 BC/QK Normalization (RMSNorm) 以稳定训练
- 移除了 Mamba-2 的 post-gate RMSNorm，但在混合模型中保留以支持长上下文外推
- 添加可学习的 B、C 偏置，赋予模型卷积式行为
- 支持纯 SSM 和 Hybrid (SSM+Sliding-Window Attention) 两种配置

**Experimental Results:**
| Model | Avg Downstream Accuracy (1.5B) |
|-------|-------------------------------|
| Mamba-2 | — |
| Gated DeltaNet | baseline |
| Mamba-3 SISO | +0.6 pts vs GDN |
| Mamba-3 MIMO | +1.8 pts vs GDN |
- Mamba-3 在使用一半状态大小时达到与 Mamba-2 相当的 perplexity
- 在 1.5B 规模下，Mamba-3 SISO 在所有序列长度上实现了最快的 prefill+decode 延迟
- Hybrid 版本在检索任务上优于纯 Transformer

**Significance:** Mamba-3 在性能-效率 Pareto 前沿上确立了新的 SOTA 地位，是向推理优先模型设计的重要一步。

---

## 2. Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention

| Field | Detail |
|-------|--------|
| **Title (EN)** | Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention |
| **Title (ZH)** | Gated DeltaNet-2: 线性注意力中擦除与写入的解耦 |
| **Authors** | Ali Hatamizadeh, Yejin Choi, Jan Kautz |
| **Affiliation** | NVIDIA |
| **Venue** | arXiv 2605.22791 |
| **Links** | [arXiv](https://arxiv.org/abs/2605.22791) \| [GitHub](https://github.com/NVlabs/GatedDeltaNet-2) |

**Problem Background:** 线性注意力将 softmax 注意力的无界缓存替换为固定大小的递推状态。关键的挑战在于如何编辑这个压缩记忆而不破坏现有关联。Delta-rule 模型减去当前读取后再写入新值，但其活跃编辑仍使用单标量门来控制两件事：擦除多少旧内容（key 侧）和写入多少新内容（value 侧）。

**Key Innovations:**
1. **通道级擦除门 (Channel-wise Erase Gate) b_t 和通道级写入门 w_t:** 将 KDA 和 Gated DeltaNet 的共享标量门解耦为两个独立的通道级门控。
2. **Chunkwise WY 并行训练算法:** 将通道级衰减吸收为非对称擦除因子，支持高效并行训练。
3. **门控感知反向传播 (Gate-aware Backward Pass):** 保持高效并行训练的同时实现精确梯度传播。

**Experimental Results (1.3B params, 100B FineWeb-Edu tokens):**
| Model | Avg (Recurrent) | Avg (Hybrid) | NIAH-3 @ 8K |
|-------|----------------|--------------|-------------|
| Mamba-2 | — | — | — |
| Gated DeltaNet | — | — | — |
| KDA | 52.28 | — | 28.0 |
| Mamba-3 MIMO | 52.39 | 52.72 | 72.4 |
| **Gated DeltaNet-2** | **53.11** | **53.97** | **89.8** |
- 在长上下文 RULER needle-in-a-haystack 基准上改善最为显著
- 在纯递推和混合设置中均保持领先

**Significance:** Gated DeltaNet-2 是 NVIDIA 在高效序列建模领域的突破性工作，在匹配状态大小的条件下，通过更新规则（而非更多内存）实现了最佳结果。

---

## 3. GPT-5.6 Sol: OpenAI Next-Generation Model Preview

| Field | Detail |
|-------|--------|
| **Title** | Previewing GPT-5.6 Sol: a next-generation model |
| **Affiliation** | OpenAI |
| **Links** | [Blog](https://openai.com/index/previewing-gpt-5-6-sol) |

**Overview:** OpenAI 于 2026-06-26 发布 GPT-5.6 系列模型的有限预览：
- **Sol (旗舰):** $5/$30 per 1M tokens (input/output)
- **Terra (均衡):** $2.50/$15, 性能与 GPT-5.5 相当但成本减半
- **Luna (快速/经济):** $1/$6

**Capabilities:**
- 在 coding, biology, cybersecurity 方面展示改进的 agentic 能力
- 与 Cerebras 合作提供高达 750 tokens/sec 的推理速度（计划 2026年7月上线）
- 支持可预测的 prompt caching (cache writes @ 1.25×, cache reads 90% 折扣)

---

## 4. TabICLv2: Better, Faster, Scalable Tabular Foundation Model

| Field | Detail |
|-------|--------|
| **Authors** | Jingang Qu, David Holzmüller, Gaël Varoquaux, Marine Le Morvan |
| **Affiliation** | INRIA, Soda |
| **Venue** | ICML 2026 |
| **Links** | [arXiv](https://arxiv.org/abs/2602.11139) \| [GitHub](https://github.com/soda-inria/tabicl) |

**Overview:** TabICLv2 是一个为表格数据设计的 in-context learning (ICL) 基础模型。支持分类和回归任务，通过 ICL 范式在大量表格数据上预训练，可零样本迁移到新数据集。2M 和 16M 参数版本均已开源 (Apache 2.0)。

---

## 5. LimiX-2M: Structured-Data Foundation Model (ICML 2026)

| Field | Detail |
|-------|--------|
| **Affiliation** | Limix-LDM-AI, Stable AI |
| **Venue** | ICML 2026 |
| **Links** | [arXiv](https://arxiv.org/abs/2606.04485) \| [GitHub](https://github.com/limix-ldm-ai/LimiX) |

**Overview:** 结构化数据基础模型，支持分类、回归、缺失值插补。16M 和 2M 参数版本，Apache 2.0 开源。

---

# Part II — ICLR 2026 Outstanding Papers

## 1. Transformers are Inherently Succinct

| Field | Detail |
|-------|--------|
| **Authors** | Pascal Bergsträßer, Ryan Cotterell, Anthony Widjaja Lin |
| **Affiliation** | ETH Zurich |
| **Venue** | ICLR 2026 Outstanding Paper |
| **Type** | Theory |

**Overview:** 从理论上证明了 Transformer 相比 RNN 等替代架构在编码某些概念时的简洁性 (succinctness)。这一工作为 Transformer 的强大能力提供了理论解释，可能激发对 Transformer 表示简洁性的进一步理论与实证研究。

## 2. Multi-Turn LLM Evaluation (ICLR 2026 Outstanding)

**Overview:** 该论文设计了可扩展的多轮对话能力评估方法，揭示了 LLM 在多轮交互和指令不明确场景下的性能显著下降。尽管使用了一些较早的模型，但委员会认为其结论和方法仍然适用于最先进的模型。

## 3. The Polar Express: Optimal Matrix Sign Methods (Honorable Mention)

| Field | Detail |
|-------|--------|
| **Authors** | Noah Amsel, David Persson, Christopher Musco, Robert M. Gower |
| **Affiliation** | — |
| **Venue** | ICLR 2026 Honorable Mention |

**Overview:** 使用逼近论为 Polar 分解设计最优多项式逼近，应用于流行的 Muon 优化器。在 GPU 和低精度推理场景中进行了专门优化。

---

# Part III — CVPR 2026 Highlights

## Best Paper: D4RT — Dynamic 4D Scene Reconstruction

| Field | Detail |
|-------|--------|
| **Authors** | Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, Liliane Momeni, Junyu Xie, Shuyang Sun, Rahul Sukthankar, Joëlle K. Barral, Raia Hadsell, Zoubin Ghahramani, Andrew Zisserman, Junlin Zhang, Mehdi S. M. Sajjadi |
| **Affiliation** | Google DeepMind, UCL, University of Oxford |
| **Venue** | CVPR 2026 Best Paper |

**Overview:** D4RT 是一种可以从视频中重建动态 4D 场景几何和运动的网络。使用统一的 Transformer 架构，估计深度、时空对应关系和完整的相机参数，允许独立高效地探测任意点在时空中的 3D 位置。将传统计算密集型流程简化为轻量级、高度可扩展的方法。

## Best Paper: O-Voxel — Native Compact Structured Latents for 3D Generation

| Field | Detail |
|-------|--------|
| **Authors** | Jianfeng Xiang, Xiaoxue Chen, Sicheng Xu, Ruicheng Wang, Zelong Lv, Yu Deng, Hongyuan Zhu, Yue Dong, Hao Zhao, Nicholas Jing Yuan, Jiaolong Yang |
| **Affiliation** | Tsinghua University, Microsoft Research, USTC, Microsoft AI |
| **Venue** | CVPR 2026 Best Paper |

**Overview:** O-Voxel 是一种新的 3D 表示方法，可以准确捕获复杂形状和表面属性，显著提升了 AI 生成 3D 资产的质量和真实感。

## SAM 3D: 3Dfy Anything in Images

| Field | Detail |
|-------|--------|
| **Authors** | Xingyu Chen, FU-JEN CHU, Pierre Gleize, Kevin J Liang, Alexander Sax, Hao Tang, Weiyao Wang, Michelle Guo, Thibaut Hardin, Xiang Li, Aohan Lin, Jia-Wei Liu, Ziqi Ma, Anushka Sagar, Bowen Song, Xiaodong Wang, Jianing Yang, Bowen Zhang, Piotr Dollár, Georgia Gkioxari, Matt Feiszli, Jitendra Malik |
| **Affiliation** | Meta Superintelligence Labs |
| **Venue** | CVPR 2026 |

**Overview:** SAM 3D 是一个用于视觉基础 3D 物体重建的生成模型，从单张图像预测几何、纹理和布局。在人类偏好测试中，对真实世界物体和场景获得了至少 5:1 的胜率。

## Other CVPR 2026 Highlights:
- **Thinking-while-Generating (TwiG):** 首个交错框架，在视觉生成过程中实现共同演进的文本推理 (CVPR 2026, pp. 26295-26305)
- **BPGO (Bayesian Prior-Guided Optimization):** 通过贝叶斯先验引导优化扩展 GRPO，在图像和视频生成中提供更强的语义对齐 (pp. 34408-34417)
- **WorldGen:** 从单一文本提示生成大型、可导航的 3D 世界，兼容标准游戏引擎 (pp. 27124-27135)
- **Gen3R:** 桥接基础重建模型和视频扩散模型的先验，用于场景级 3D 生成 (pp. 25358-25369)
- **iMontage:** 将视频模型重新用于统一的、高动态的多对多图像生成 (pp. 16237-16247)
- **CoECT:** 基于事件链的因果推理，用于物理合理的视频生成 (pp. 38122-38131)
- **WorldForge:** 零样本相机控制，驯服视频模型用于 3D/4D 生成 (pp. 40352-40363)
- **Scone:** 统一理解-生成建模，兼顾主体驱动图像生成中的组合性和区分性 (pp. 7773-7783)

---

# Part IV — AAAI 2026 Highlights

> AAAI 2026 (Singapore, Jan 20-27) 收到 ~29,000 投稿，约 23,000 留在审稿流程中，接收 4,000+ 篇论文。中国贡献了约 20,000 投稿 (CV/ML/NLP 为三大热门方向)。

## Top Papers:
- **LENS:** 将可扩展的强化学习框架用于联合优化推理过程和分割，端到端地提升未见提示和领域的泛化能力
- **AURA (Affordance-Understanding Risk-aware Alignment):** 基于 Process Reward Models 的多层框架，提供步骤级逻辑连贯性和安全性评估
- **Towards Continually-Evolving AI:** 自适应可扩展多模态记忆架构，使具身 AI 系统在复杂多模态环境中持续增强能力
- **MonoScale (ICML 相关):** 多智能体系统持续扩展的安全可控方案，在 GAIA 和 Humanity's Last Exam 上验证稳定增益

---

# Part V — CTR Prediction & Advertising (Cross-Venue Survey)

## KDD 2026 ADS Track

### FAT: Field-Aware Transformer — CTR Scaling Law

| Field | Detail |
|-------|--------|
| **Title** | From Scaling to Structured Expressity: Rethinking Transformers for CTR Prediction |
| **Affiliation** | Alibaba |
| **Venue** | KDD 2026 |
| **Links** | [arXiv](https://arxiv.org/abs/2511.12081) |

**Key Insight:** CTR 模型与 LLM 不同，其快速收益递减源于结构不匹配 —— Transformer 假设序列组合性，而 CTR 数据需要跨异构域的组合推理。FAT 通过域感知参数重构 Transformer 块，将模型复杂度从词汇量 n 降为域数 F (n >> F)。使用 Basis-Composed Hypernetwork 合成域特定参数。

**Results:** +4.38% AUC, +2.33% CTR, +0.66% RPM (生产环境)

### CTR-Sink: Attention Sink for LMs in CTR

| Field | Detail |
|-------|--------|
| **Authors** | Zixuan Li, Binzong Geng, Jing Xiong, Yong He, Yuxuan Hu, Jian Chen et al. |
| **Affiliation** | Ant Group, SMBU, HKU |
| **Venue** | KDD 2026 |
| **Links** | [arXiv](https://arxiv.org/abs/2508.03668) \| [GitHub](https://github.com/UGUESS-lzx/CTR-SINK) |

**Key Insight:** 用户行为序列由通过语义空分隔符连接的离散行为组成，与 LM 预训练的连贯自然语言存在结构性差距。CTR-Sink 在行为间插入推荐信号融合的 [SINK] token，锚定注意力聚焦。AUC 提升 0.2-0.5%。

### RankUp: High-rank Representations for Tencent Advertising

| Field | Detail |
|-------|--------|
| **Affiliation** | Tencent |
| **Venue** | KDD 2026 |
| **Links** | [arXiv](https://arxiv.org/abs/2604.17878) |

**Results (Online A/B):** GMV +3.41% (Weixin Video Accounts), +4.81% (Moments), +2.12% (Official Accounts)。20% 流量在线测试，全量部署。

### ALF: Advertiser Large Foundation Model

| Affiliation | Meta |
|-------------|------|
| **Links** | KDD 2026 ADS Track |

多模态广告主理解基础模型，处理跨模态广告主信息。

## WWW 2026

### SparseCTR: Unleashing Potential of Sparse Attention on Long-term Behaviors

| Field | Detail |
|-------|--------|
| **Authors** | Weijiang Lai, Beihong Jin et al. |
| **Affiliation** | Meituan |
| **Venue** | WWW 2026 |
| **Links** | [arXiv](https://arxiv.org/abs/2601.17836) \| [GitHub](https://github.com/laiweijiang/SparseCTR) |

**Key Innovation:** 个性化分块 + 三分支稀疏自注意力（全局兴趣、兴趣转换、短期兴趣）。在线 A/B: CTR +1.72%, CPM +1.41%。展现显著的 Scaling Law 现象（在 FLOPs 三个数量级范围内保持改进）。

### GenCI: Generative Modeling of User Interest Shift for CTR

| Field | Detail |
|-------|--------|
| **Affiliation** | — |
| **Venue** | WWW 2026 |
| **Links** | [arXiv](https://arxiv.org/abs/2601.18251) |

**Key Insight:** 现有判别式范式（将候选项与用户历史匹配）过度拟合历史主导特征，无法适应快速兴趣转移。GenCI 使用生成式模型和 next-item prediction 目标，主动生成候选兴趣群组 (interest cohorts)。在三个数据集上超越 SOTA。

### ThinkRec: Thinking-based Recommendation via LLM

| Affiliation | — |
|-------------|---|
| **Venue** | WWW 2026 |
| **Links** | [arXiv](https://arxiv.org/abs/2505.15091) |

将 LLM 的推理能力引入推荐系统。AUC +9.13% (Yelp), +8.41% (ML1M)。

## SIGIR 2026

### OneRec-Think: In-Text Reasoning for Generative Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Zhanyu Liu, Shiyao Wang, Guorui Zhou et al. |
| **Affiliation** | Kuaishou |
| **Venue** | ACL 2026 / Kuaishou 部署 |
| **Links** | [ACL](https://aclanthology.org/2026.acl-long.123.pdf) |

**Key Innovation:** 首次将 LLM 的显式可控制推理能力集成到生成式推荐系统中。三阶段框架：Itemic Alignment（跨模态语义对齐）→ Reasoning Activation（推理支架）→ Reasoning Enhancement（推荐特定奖励函数）。在线 A/B: APP Stay Time +0.159%。

### GenRec: Preference-Oriented Generative Framework (JD)

| Field | Detail |
|-------|--------|
| **Affiliation** | JD.com |
| **Venue** | SIGIR 2026 |
| **Links** | [arXiv](https://arxiv.org/abs/2604.14878) |

**Key Innovation:** Page-wise NTP 任务 + 非对称线性 Token Merger（压缩 2×）+ GRPO-SR（GRPO + NLL 正则化 + 混合奖励）。在线 A/B: 点击数 +9.5%, 交易数 +8.7%。

### L2Rec: Dual-View Understanding of LLMs for Recommendation

| Affiliation | — |
|-------------|---|
| **Venue** | SIGIR 2026 |
| **Links** | [arXiv](https://arxiv.org/abs/2605.26717) |

通过 Dual-view Personalized Mixture-of-Experts (DPMoE) 机制，在同一 LLM 骨干网络参数级别整合行为和语义理解。在四个数据集上超越 SOTA。

### A²Gen: Action-Aware Generative Sequence Network (Kuaishou)

| Field | Detail |
|-------|--------|
| **Affiliation** | Kuaishou |
| **Venue** | SIGIR 2026 |
| **Links** | [arXiv](https://arxiv.org/abs/2604.25834) |

将用户行为（Like, Follow 等）编码为时间序列。Context-aware Attention Module + Hierarchical Sequence Encoder + Action-seq Autoregressive Generator。在线 A/B: watch time +0.34%, interaction rate +8.1%, Lifetime-7 +0.162%（≈1M DAU）。

## Baidu CTR

### GRAB: Generative Ranking for Ads at Baidu

| Field | Detail |
|-------|--------|
| **Authors** | Shaopeng Chen, Chuyue Xie et al. |
| **Affiliation** | Baidu |
| **Links** | [arXiv](https://arxiv.org/abs/2602.01865) |

**Key Innovation:** 受 LLM 启发的序列优先 CTR 框架，Causal Action-aware Multi-channel Attention (CamA)。全量部署: 收入 +3.05%, CTR +3.49%。展现单调接近线性的 scaling 行为。

## ByteDance CTR

### UG-Sep: Compute Only Once for Large Recommendation Models

| Affiliation | ByteDance |
|-------------|-----------|
| **Links** | [arXiv](https://arxiv.org/abs/2602.10455) |

用户-组分离 (User-Group Separation)，首次在 TokenMixer 架构中实现用户侧计算复用。在 Douyin Feed、Hongguo Feed、Chuanshanjia Ads、Qianchuan Ads 等场景中推理延迟降低 20%。

### SIF: Sample Is Feature — Sample-Level Tokens for Large Recommender Models

| Affiliation | ByteDance |
|-------------|-----------|
| **Links** | [arXiv](https://arxiv.org/abs/2604.15650) |

将序列 token 从 item 级提升到 sample 级。在线 A/B: CTR +2.03%, CVR +1.21%, GMV/session +1.35%。

## Kuaishou CTR

### GR4AD: Generative Recommendation for Large-Scale Advertising

| Affiliation | Kuaishou |
|-------------|----------|
| **Links** | [arXiv](https://arxiv.org/abs/2602.22732) |

**Key Innovation:**
- UA-SID: MLLM 指令微调 + 共现学习派生的统一广告语义 ID
- LazyAR: 松弛逐层自回归依赖的解码器
- VSL + RSPO: 价值感知监督学习 + 排序引导的 Softmax 偏好优化
- Dynamic Beam Serving: 动态束宽调整

**Results:** 营收 +4.2%, <100ms 延迟, 500+ QPS per L20。全量部署至 4 亿+用户。

### UniFormer: Efficient Unified Model-Centric Scaling

| Affiliation | Kuaishou |
|-------------|----------|
| **Links** | [arXiv](https://arxiv.org/abs/2606.27058) |

分解建模空间为特征空间和任务空间。Multi-Sequence Cross-Attention + Multi-View FFN。在线: App Stay Time +0.101%/+0.260%, Watch Time +0.729%/+1.113%。

### OneLive: Dynamically Unified Generative Framework for Live-Streaming

| Affiliation | Kuaishou |
|-------------|----------|
| **Links** | [arXiv](https://arxiv.org/abs/2602.08612) |

动态 Tokenizer (编码实时内容) + Time-Aware Gated Attention + Sequential MTP + 多目标对齐。日服务 4 亿用户。

### SARM: LLM-Augmented Semantic Anchor for Live-Streaming Ranking

| Affiliation | Kuaishou |
|-------------|----------|
| **Links** | [arXiv](https://arxiv.org/abs/2602.09401) |

可学习文本 token 形式的语义锚点，与排序特征联合优化。非对称部署策略保持低延迟。日服务 4 亿用户。

### HAP: Heterogeneity-Aware Pre-ranking (ByteDance Toutiao)

| Affiliation | ByteDance |
|-------------|-----------|
| **Links** | [arXiv](https://arxiv.org/abs/2603.03770) |

冲突敏感采样 + 定制损失设计，自适应分配计算预算。在 Toutiao 部署 9 个月: 用户使用时长 +0.4%, 活跃天数 +0.05%。

## Xiaohongshu CTR

### IDProxy: Cold-Start CTR with Multimodal LLMs

| Affiliation | Xiaohongshu |
|-------------|-------------|
| **Links** | [arXiv](https://arxiv.org/abs/2603.01590) |

利用 MLLM 生成代理嵌入 (proxy embeddings) 以对齐现有 ID 嵌入空间，用于冷启动物品 CTR 预测。成功部署在 Content Feed 和 Display Ads。

## Other CTR Highlights

### DS-MLP: Dual-Stream MLP is All You Need for CTR

| Affiliation | Renmin University, ByteDance, Meituan |
|-------------|--------------------------------------|
| **Links** | [arXiv](https://arxiv.org/abs/2606.04944) \| [GitHub](https://github.com/RUCAIBox/DS-MLP) |

用知识蒸馏将显式特征交互学习能力整合到主 MLP 网络中。在 Criteo, Avazu, Movielens 上达到 SOTA。

### DAIAN: Deep Adaptive Intent-Aware Network (Xianyu/Alibaba)

| Affiliation | Alibaba |
|-------------|---------|
| **Links** | [arXiv](https://arxiv.org/abs/2602.13971) |

解决触发诱导推荐中的"意图近视"问题。三阶段训练。在线 A/B (Xianyu TIR): CTR +1.59%, 多样性 +1.73%, 账单 +2.37%。

---

# Part VI — Agent Systems & Code Generation

## GrandCode: Grandmaster-Level Competitive Programming

| Field | Detail |
|-------|--------|
| **Title** | GrandCode: Achieving Grandmaster Level in Competitive Programming via Agentic RL |
| **Affiliation** | — |
| **Links** | [arXiv](https://arxiv.org/abs/2604.02721) |

**Key Innovation:** 多智能体 RL 系统，编排假设提议、求解器、测试生成器、摘要等模块。引入 **Agentic GRPO** 解决多阶段 agent rollout 中的延迟奖励和严重 off-policy 漂移。

**Results:** 首个在 Codeforces 实时竞赛中持续击败所有人类参与者的 AI 系统。Round 1087 (Mar 21), Round 1088 (Mar 28), Round 1089 (Mar 29) 全部第一。

## OpenGame: Open Agentic Coding for Games

| Affiliation | — |
|-------------|---|
| **Links** | [arXiv](https://arxiv.org/abs/2604.18394) |

首个专为端到端 Web 游戏创建设计的开源 agent 框架。核心是 GameCoder-27B（通过持续预训练 + SFT + 执行接地 RL 三阶段流水线专门化）。OpenGame-Bench 通过 headless 浏览器 + VLM 评判评估游戏可玩性。

## LLM-as-Code: Agentic Programming for Agent Harness

| Links | [arXiv](https://arxiv.org/abs/2606.15874) |

**核心论点:** Token 爆炸、控制流幻觉和不可靠完成不是实现 bug 而是架构后果 —— 将循环、分支和排序的确定性工作分配给概率系统。提出 Agentic Programming：程序控制所有控制流，LLM 仅在需要推理或生成时被调用 (LLM-as-Code)。DAG 结构上下文 + 多智能体协作 + 自编程进化。

## MonoScale: Scaling Multi-Agent System with Monotonic Improvement

| Affiliation | — |
|-------------|---|
| **Links** | [arXiv](https://arxiv.org/abs/2601.23219) |

当 agent 池从 3 扩展到 10 时，朴素扩展导致冷启动误路由和性能崩溃。MonoScale 形式化为上下文赌博机问题，使用 agent 熟悉化探测 + 可审计自然语言路由记忆。在 GAIA 和 Humanity's Last Exam 上验证稳定增益。

## HarnessBridge: Learnable Bidirectional Controller for LLM Agents

| Links | [arXiv](https://arxiv.org/abs/2606.12882) |

将 agent-环境接口参数化为可学习的双向投影（观察投影 + 动作投影）。在 Terminal-Bench 2.0 和 SWE-bench Verified 上匹配或超越强专业化 harness，同时显著降低 token 用量。

## PlayCoder: Making LLM-Generated GUI Code Playable

| Affiliation | Tencent |
|-------------|---------|
| **Links** | [arXiv](https://arxiv.org/abs/2604.19742) |

PlayEval (43 个多语言 GUI 应用) + Play@k 评估指标 + PlayTester 自动化交互测试 agent。PlayCoder 将 Exec@3 提升至 38.1%, Play@3 提升至 20.3%。

## Code as Agent Harness Survey

| Links | [arXiv](https://arxiv.org/abs/2605.18747) |

全面综述代码作为 agent harness 的统一视角：代码作为推理基板、动作接口、环境表示、规划/记忆/工具使用、从单 agent 扩展到多 agent 系统。

## Lacuna: Safe Agents as Recursive Program Holes

| Links | [arXiv](https://arxiv.org/abs/2605.28617) |

类型安全 agent 编程模型。每个 agent 动作是一个类型化调用 `agent[T](task)`，在运行时被 LLM 生成的代码填充，并在执行前进行类型检查。BrowseComp-Plus: 27.1% accuracy, τ²-bench: 76.0%。

## Securing LLM Agents: Intent-to-Execution Integrity

| Links | [arXiv](https://arxiv.org/abs/2605.16976) |

识别两个根本问题来源（不可信数据摄取 + 不可信工具执行），推导四个完整性属性：工具完整性、指令完整性、判断完整性、数据流完整性。

## Can We Predict Before Executing ML Agents?

| Affiliation | Zhejiang University |
|-------------|---------------------|
| **Links** | [ACL 2026](https://aclanthology.org/2026.acl-long.182.pdf) |

**ForeAgent:** 通过世界模型内部化执行先验，用预测推理替换昂贵运行时检查。61.5% 准确率 (DeepSeek-V3.2-Thinking)。6× 加速收敛，同时超越执行基线 +6%。

## DeepPlanner: Scaling Planning for Deep Research Agents

| Links | [ACL 2026 Findings](https://aclanthology.org/2026.findings-acl.370.pdf) |

Token 级别熵分析揭示计划阶段持续高熵是关键瓶颈。Advantage Shaping 将学习集中在不确定的规划决策和复杂轨迹上，直接扩展 agent 规划能力。

---

# Part VII — ACL 2026 & EMNLP 2025

## ACL 2026

### PaCoRe: Parallel Coordinated Reasoning

| Links | [ACL 2026](https://aclanthology.org/2026.acl-long.1253.pdf) |

学习通过并行协调推理扩展 test-time compute。在多任务上展示了并行思考路径的协同效果。

### Adaptive Constraint Propagation (MetaJuLS)

| Links | [ACL 2026](https://aclanthology.org/2026.acl-long.701.pdf) |

元强化学习学习自适应约束传播调度。在 10 种语言的依存解析上实现 1.5-2.0× 加速，精度在 0.2% 以内。

### From Interpretability to Performance: Optimizing Retrieval Heads

| Links | [ACL 2026 Findings](https://aclanthology.org/2026.findings-acl.1380.pdf) |

识别并优化 LLM 中的检索头 (retrieval heads)，提升长上下文推理性能。

### OneRec-Think: In-Text Reasoning for Generative Recommendation

| Links | [ACL 2026](https://aclanthology.org/2026.acl-long.123.pdf) |

见 Part V — Kuaishou 生成式推荐。

### Tracing Relational Knowledge Recall in LLMs

| Links | [ACL 2026 Findings](https://aclanthology.org/2026.findings-acl.2160.pdf) |

用线性探针研究 LLM 中的关系知识回忆机制，发现 per-head contribution features ∆att,h 是最强的探针输入。

## EMNLP 2025

> Suzhou, China, Nov 4-9, 2025. 1,810 main papers + 1,406 findings.

- **MovieCORE (EMNLP 2025 main):** 电影中的认知推理
- **GTA (Guess-Think-Answer):** 结合 SFT 效率和 RL 能力提升的统一训练范式，在三个文本分类基准上超越 SFT 和 RL 基线
- **LLMs as Realistic Microservice Trace Generators:** LLM 用于微服务追踪生成
- **NL-Debugging:** 自然语言作为代码调试的中间表示
- **GnnXemplar:** 基于范例理论的 GNN 全局可解释性方法 (NeurIPS 2025)
- **CondenseLM:** 长上下文 LLM 的高效压缩方法
- **RAG4GFM:** 图基础模型的检索增强生成

---

# Part VIII — Reinforcement Learning & Reasoning

## Google DeepMind: Efficient Exploration at Scale for RLHF

| Authors | Seyed Mohammad Asghari, Chris Chute, Vikranth Dwaracherla et al. |
|---------|------------------------------------------------------------------|
| **Links** | [arXiv](https://arxiv.org/abs/2603.17378) |

在线 RLHF 算法，在 Gemma LLM 上仅用 20K 标签即匹配 200K 标签的离线 RLHF（10× 数据效率提升）。外推显示 1M 标签可匹配 1B 标签（1,000× 提升）。关键组件：小肯定性 nudging、认知不确定性建模、信息导向探索。

## Google DeepMind: Improving Interactive ICL from Natural Language Feedback

| Authors | Martin Klissarov, Jonathan Cook, Diego Antognini et al. |
|---------|----------------------------------------------------------|
| **Links** | [arXiv](https://arxiv.org/abs/2602.16066) |

RL2F (Reinforcement Learning from Language Feedback) 框架在数学推理任务上训练，使 Gemini 2.5 Flash 模型几乎匹配 Gemini 2.5 Pro 的多轮交互性能。

## Google DeepMind: Aletheia — Autonomous Math Research

| Authors | Tony Feng, Trieu Trinh, Garrett Bingham et al. |
|---------|-------------------------------------------------|
| **Links** | [arXiv](https://arxiv.org/abs/2602.10177) |

Aletheia 数学研究 agent，能够迭代生成、验证和修改解决方案。基于 Gemini Deep Think、新的推理时 scaling law（从奥赛级扩展到博士级问题）和 Google Search/Web browsing 工具使用。已解决多个开放数十年的 Erdős 问题。

## Google DeepMind: Interpreting and Controlling Model Behavior via Constitutions

| Links | [AISTATS 2026](https://openreview.net/pdf?id=jEhTx67C6L) |

黑盒可解释性框架，学习可验证的"宪法"（自然语言行为规则）。使用原子概念编辑 (ACE) 系统分析并控制模型行为。发现: 文本到图像生成中 GPT-Image 侧重语法遵循，Imagen 4 侧重氛围连贯；数学推理中干扰变量使 GPT-5 困惑但 Gemini 2.5 和 o4-mini 几乎不受影响。

## SPACE: Noise Contrastive Estimation Stabilizes Self-Play Fine-Tuning (NeurIPS 2025)

| Venue | NeurIPS 2025 |

解决了 SPIN 等方法中的训练不稳定问题。

## GrandCode (Agentic GRPO)

见 Part VI — 在 Codeforces 上击败所有人类。

## Reinforcement Learning from Verifiable Rewards (RLVR) — Cross-Venue Theme

RLVR 成为 2026 年主流推理训练范式。重要方法:
- **VIMPO**: 无评论家的 RLVR (critic-free)，使用策略隐含值函数，在 AIME/OlympiadBench 上超越 GRPO
- **Beyond Entropy / ICT**: Token 级分布 RLVR, +4.58% pass@4
- **GRPO-SR**: GRPO + NLL 正则化 + 混合奖励 (JD GenRec)
- **Process-Verified RL (ICML 2026)** : 步骤级验证的 RL

---

# Part IX — NeurIPS 2025 Highlights

> 5,772 accepted papers (5,275 Main + 497 Datasets/Benchmarks), 23,704 unique authors

## Key Papers:
- **Gated Attention (Best Paper):** 消除 Attention Sink 的新注意力机制
- **RL Reasoning Critique (Best Paper):** 价值-动作间隙 (value-action gap) 分析
- **Artificial Hivemind / Infinity-Chat:** 大规模开放域查询数据集 (26K prompts, 31K human annotations)，揭示 LLM 的输出同质化和模式坍缩 (Intra-model repetition + Inter-model homogeneity)
- **LLMs as End-to-end Combinatorial Optimization Solvers:** 两阶段微调（SFT + FOARL），7B 参数超越 Deepseek-R1 和 GPT-o1 以及常用启发式算法，覆盖 7 个 CO 问题
- **Dynam3D (Oral):** VLN 的动态分层 3D token
- **Nemotron-Flash:** 延迟最优的 Hybrid Small Language Models
- **Scaling Up Active Testing to LLMs:** 风险估计误差降低 25-80%
- **Sparse MeZO:** 零阶 LLM 微调的更优参数选择
- **SubSpec:** 无损且无需训练的卸载 LLM 推测解码加速
- **GnnXemplar:** 范例驱动的 GNN 全局可解释性
- **EvoLM:** 全景 LLM 训练动态分析（pre-training, SFT, RL 各阶段的权衡）
- **RAG4GFM:** 图基础模型的图检索增强生成

---

# Part X — Generative Models & Multimodal

## Diffusion Language Models (Cross-Venue)
- **LaDiR (ICLR 2026):** 潜在扩散用于 LLM 文本推理
- **DiLaDiff (NVIDIA):** 蒸馏潜在增强扩散 LM
- **DiffusionGemma (Google):** 扩散 LM 的工业级部署版本
- **LLaDA-V (CVPR 2026 Best):** 扩散多模态大语言模型

## Image Generators are Generalist Vision Learners (Google DeepMind, Apr 2026)
图像生成器作为通用视觉学习者，挑战了生成/判别任务分离的传统认知。

## Video Models are Zero-shot Learners and Reasoners (Google DeepMind, Sep 2025)
视频模型作为零样本学习器和推理器，拓展了视频理解的边界。

## Gen3R (CVPR 2026): 3D Scene Generation Meets Feed-Forward Reconstruction
桥接基础重建模型 (VGGT) 和视频扩散模型。
- 通过适配器训练几何潜在变量，与视频扩散模型的外观潜在变量对齐
- 同时生成 RGB 视频 + 3D 几何（相机姿态、深度图、全局点云）

## Thinking-while-Generating (CVPR 2026)
零样本/SFT/RL (GRPO) 三种策略验证交错推理对视觉生成的增强效果。

## BPGO: Bayesian Prior-Guided Optimization (CVPR 2026)
贝叶斯先验引导优化扩展 GRPO，显式建模奖励不确定性。图像和视频生成中语义对齐一致增强。

---

# Part XI — LLM Safety, Evaluation & Benchmarking

- **Infinity-Chat (NeurIPS 2025 Oral):** 26K 真实开放域查询 + 31K 人工标注，系统研究 LLM 中的"人工蜂巢思维"效应
- **Artificial Hivemind:** 揭示 LLM 的 intra-model + inter-model 同质化，对 AI 安全有长期影响
- **Benchmarking Empirical Privacy Protection for LLM Adaptations (ICLR 2026):** LLM 适应的隐私保护基准
- **Scaling Reasoning, Losing Control (ICLR 2026):** 大型推理模型中的指令遵循评估
- **Beyond Static Leaderboards:** 预测有效性用于 LLM agent 评估，提出 12 层的测量架构
- **Humanity's Last Exam (MonoScale 中使用):** 最难的 AI 评估基准之一

---

# Part XII — Conference Statistics & Meta Trends

## AAAI 2026
- 29,000 submissions → ~23,000 留审 → 4,000+ accepted
- 75,000 unique authors, 28,000 审稿人
- 最大领域: CV, ML, NLP
- 中国占约 20,000 投稿

## NeurIPS 2025
- 5,772 accepted papers (91.4% Main, 8.6% Datasets/Benchmarks)
- 23,704 unique authors, 平均 5.87 作者/论文
- 5,275 poster, 739 spotlight, 84 oral

## ICLR 2026
- 19,809 submissions, 5,343 accepted (26.97%)
- 5,120 poster, 223 spotlight, 0 oral (ICLR 不再有 oral)

## CVPR 2026
- 16,092 submissions, 4,089 accepted (25.4%)
- Best Papers: D4RT (Google DeepMind), O-Voxel (Microsoft/Tsinghua)

## Key Themes Across All Venues

| Theme | Frequency |
|-------|-----------|
| RLVR/GRPO for LLM Reasoning | ⭐⭐⭐⭐⭐ (跨所有 venue) |
| CTR Scaling Laws | ⭐⭐⭐⭐⭐ (KDD, WWW, arXiv) |
| Generative Recommendation (SID-based) | ⭐⭐⭐⭐⭐ (KDD, SIGIR, WWW, RecSys) |
| Hybrid SSM-Attention | ⭐⭐⭐⭐ (ICLR, ICML, arXiv) |
| Multi-Agent Systems | ⭐⭐⭐⭐ (AAAI, ICML, ACL) |
| Diffusion Language Models | ⭐⭐⭐ (ICLR, ICML, CVPR) |
| Agentic Reinforcement Learning | ⭐⭐⭐⭐ (NeurIPS, ICML, ACL) |
| KV Cache Optimization | ⭐⭐⭐ (cross-venue trend) |
| Test-time Compute Scaling | ⭐⭐⭐⭐ (cross-venue trend) |
| Self-Play & Game-Based RL | ⭐⭐⭐⭐ (ICLR, ICML, NeurIPS) |
| 4D Scene Reconstruction & Generation | ⭐⭐⭐ (CVPR) |
| LLM Agent Safety & Alignment | ⭐⭐⭐ (AAAI, ICLR, ACL) |
| 3D Generation | ⭐⭐⭐ (CVPR, ICLR) |

---

# Appendix: Paper Index by Affiliation

| Affiliation | # Papers | Key Highlights |
|-------------|----------|----------------|
| Google DeepMind | 5 | D4RT (CVPR Best), Aletheia, Efficient Exploration, ICL from Feedback, Interpreting via Constitutions |
| OpenAI | 1 | GPT-5.6 Sol preview |
| Meta AI | 2 | SAM 3D (CVPR), ALF (KDD), NeurIPS papers |
| Microsoft Research | 2 | O-Voxel (CVPR Best), Agentic Proving |
| NVIDIA | 2 | Gated DeltaNet-2, Mamba-3 (contrib) |
| ByteDance | 4 | UG-Sep, SIF, HAP, TokenMixer-Large |
| Alibaba | 3 | FAT (KDD), DAIAN, various CTR papers |
| Tencent | 2 | RankUp (KDD), PlayCoder |
| Kuaishou | 6 | GR4AD, OneLive, SARM, UniFormer, OneRec-Think, A²Gen |
| Baidu | 1 | GRAB |
| Apple | 0 | Speculative Streaming (EMNLP 2025) |
| Amazon | 1 | Prime Video MoE (RecSys 2025) |
| Ant Group | 1 | CTR-Sink (KDD) |
| JD.com | 1 | GenRec (SIGIR) |
| Princeton/CMU | 2 | Mamba-3, GrandCode |
| Xiaohongshu | 1 | IDProxy |

---

> **Last Updated:** 2026-06-29
> **Next Update:** Ongoing — new arXiv submissions daily
