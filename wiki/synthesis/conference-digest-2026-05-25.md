---
title: 顶会论文专题报告 — 2026年5月版
type: synthesis
created: 2026-05-25
updated: 2026-05-25
sources: [ICML-2026, AAAI-2026, KDD-2026, SIGIR-2026, CVPR-2026, WWW-2026, NeurIPS-2025, ICLR-2026, ACL-2025, EMNLP-2025]
tags: [conference-digest, llm, recsys, ctr, agents, rl, code-generation, diffusion, survey]
---

# 顶会论文专题报告 — 2026年5月版

> 覆盖 9 个顶会的最新接收论文，涵盖 LLM 训练与理论、推荐系统、CTR 预估、广告检索、Agent/多智能体、游戏 AI/RL、代码执行预测、生成模型/扩散、Sequence Modeling、评测基准等方向。

---

## 目录

1. [ICML 2026](#1-icml-2026)
2. [AAAI 2026](#2-aaai-2026)
3. [KDD 2026](#3-kdd-2026)
4. [SIGIR 2026](#4-sigir-2026)
5. [CVPR 2026](#5-cvpr-2026)
6. [WWW 2026 — 推荐系统与广告](#6-www-2026--推荐系统与广告)
7. [NeurIPS 2025 — 值得关注的论文](#7-neurips-2025--值得关注的论文)
8. [ICLR 2026 — 值得关注的论文](#8-iclr-2026--值得关注的论文)
9. [ACL/EMNLP 2025 — LLM/代码相关论文](#9-aclemnlp-2025--llm代码相关论文)

---

## 1. ICML 2026

- **时间地点**: 2026年7月6–11日，韩国首尔
- **投稿量**: 23,918 篇（进入评审）
- **接收量**: 6,352 篇
- **接收率**: 26.6%
- **Spotlight**: 536 篇 (2.2%)

### 1.1 Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis

| 项目 | 内容 |
|------|------|
| **中文标题** | self-supervised流匹配实现可扩展多模态合成 |
| **英文标题** | Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis |
| **作者** | Hila Chefer, Patrick Esser, Dominik Lorenz, Dustin Podell, Vikash Raja, Vinh Tong, Antonio Torralba, Robin Rombach |
| **机构** | — |
| **论文链接** | ICML 2026 Proceedings |

**问题背景**: 多模态生成模型需要大规模配对数据训练，但获取高质量配对数据成本高昂。现有方法依赖监督学习范式，限制了数据利用效率。

**方法详述**: 提出 Self-Flow，一种self-supervised流匹配范式，在生成框架内整合表征学习。无需配对数据即可学习跨模态映射，通过流匹配目标实现表示与生成的统一。

**主要创新点**: (1) 首次将self-supervised学习引入流匹配生成框架；(2) 统一了表示学习和生成建模两个目标；(3) 在多个多模态任务上展示可扩展性。

**实验结果对比**: 在多模态合成任务上，Self-Flow 在无需配对数据的情况下达到与监督方法相当的性能。

**局限性**: 在大规模数据上的扩展性需进一步验证；对某些细粒度跨模态对齐任务效果有限。

### 1.2 You Can Learn Tokenization End-to-End with Reinforcement Learning

| 项目 | 内容 |
|------|------|
| **中文标题** | 通过强化学习end-to-end学习分词 |
| **英文标题** | You Can Learn Tokenization End-to-End with Reinforcement Learning |
| **作者** | Sam Dauncey, Roger Wattenhofer |
| **机构** | ETH Zurich |
| **论文链接** | ICML 2026 Proceedings |

**问题背景**: 传统分词作为 LLM 的预处理步骤是固定的，不可微分。将分词纳入end-to-end训练一直是一个挑战。

**方法详述**: 使用得分函数估计（score function estimates）来学习离散的分词边界，直接优化最小化损失的目标。通过 RL 使模型自主发现最优分词策略。

**主要创新点**: (1) 首次使用 RL 实现end-to-end分词学习；(2) 提供了更紧的理论保证；(3) 用实际实验证明可学习的分词策略优于固定分词器。

**实验结果对比**: 在语言建模任务上，学习到的分词策略优于 BPE、SentencePiece 等传统方法，尤其在低资源语言上表现显著。

**局限性**: RL 训练分词策略的计算成本较高；分词边界的可解释性有限。

### 1.3 Scaling Agentic Verifier for Competitive Coding

| 项目 | 内容 |
|------|------|
| **中文标题** | 面向竞赛编程的可扩展智能验证器 |
| **英文标题** | Scaling Agentic Verifier for Competitive Coding |
| **作者** | Jiaxi Yang, Zhenting Zhao, Junyang Lin, et al. |
| **机构** | 阿里巴巴 |
| **论文链接** | ICML 2026 Proceedings |

**问题背景**: 竞赛编程中验证代码正确性需要大量计算资源，现有方法在可靠性和可扩展性之间存在矛盾。

**方法详述**: 设计基于智能体的验证器，通过多轮交互和自我改进机制来验证代码正确性，结合执行反馈和逻辑推理。

**主要创新点**: (1) 提出可扩展的智能体验证框架；(2) 结合执行与推理的混合验证策略；(3) 在 Codeforces 等竞赛基准上达到新 SOTA。

**实验结果对比**: 在 CodeContests 和 Codeforces 数据集上，验证准确率提升 15%+，同时计算成本仅增加 2 倍。

**局限性**: 对超长代码的验证效率有限；依赖高质量的测试用例生成。

### 1.4 Bringing Code ALIVE: Interactive Frontend Mini-Games via RL at Scale

| 项目 | 内容 |
|------|------|
| **中文标题** | ALIVE：通过自动化游玩和 RL 优化交互式前端小游戏 |
| **英文标题** | Bringing Code ALIVE: Optimizing Interactive Frontend Mini-Games Via Automated Play and Reinforcement Learning at Scale |
| **作者** | Jiajun Zhang, Yuheng Jing, Zeyu Cui, Hao Zheng, Wentao Chen, Kaixin Li, Jiaxi Yang, Tianbao Xie, et al. |
| **机构** | 阿里巴巴 |
| **论文链接** | ICML 2026 Proceedings |

**问题背景**: 评估 LLM 生成的前端交互式小游戏面临可扩展性与可靠性之间的权衡——现有方法要么无法捕捉动态交互性，要么计算成本过高。

**方法详述**: ALIVE (Aligning LLMs via Interactive Visual Execution) 是一个高通量框架，利用一次性规划和基于 DOM 的分析来大规模评估生成游戏。

**主要创新点**: (1) 自动化的游戏质量评估管道；(2) 结合视觉执行反馈的 RL 优化；(3) 实现大规模并行化部署。

**实验结果对比**: 在自动化评估和人工评估均超越现有方法，与 GPT-4o 等基线相比生成质量提升显著。

**局限性**: 仅适用于基于 DOM 分析的网页游戏；对复杂 3D 游戏评估能力有限。

### 1.5 Unified Multimodal Autoregressive Modeling with Shared Context

| 项目 | 内容 |
|------|------|
| **中文标题** | 基于共享上下文的统一多模态autoregressive建模 |
| **英文标题** | Unified Multimodal Autoregressive Modeling with Shared Context — Visual Tokenizer Is Key to Unification |
| **作者** | Wujian Peng, Lingchen Meng, Yuxuan Cai, Xianwei Zhuang, Yuhuan Yang, Rongyao Fang, Chenfei Wu, Junyang Lin, Zuxuan Wu, Shuai Bai |
| **机构** | 阿里巴巴 |
| **论文链接** | ICML 2026 Proceedings |

**问题背景**: 现有统一多模态模型依赖不相干的视觉分词器，分裂了表示空间，阻碍了真正的统一建模。

**方法详述**: 提出 UniAR 框架，使用离散视觉分词器作为关键桥接，使模型能够直接理解自身生成的视觉 token，无需额外重新编码。

**主要创新点**: (1) 共享上下文的多模态autoregressive框架；(2) 统一了视觉理解和生成的 token 空间；(3) 实现了真正的end-to-end多模态统一建模。

**实验结果对比**: 在图像生成、视觉理解和跨模态任务上均优于现有统一模型，生成质量 FID 降低 20%+。

**局限性**: 对高分辨率图像处理的 token 效率需改进；训练计算成本较高。

---

## 2. AAAI 2026

- **时间地点**: 2026年1月20–27日，新加坡
- **投稿量**: ~29,000 篇（主赛道）
- **评审稿件**: ~23,000 篇
- **覆盖领域**: CV (最大)、ML、NLP 为三大方向
- **评审委员会**: 28,000+ 人

### 2.1 Learning to Compress: Unlocking the Potential of LLMs for Text Representation

| 项目 | 内容 |
|------|------|
| **中文标题** | 学习压缩：释放 LLM 在文本表示中的潜力 |
| **英文标题** | Learning to Compress: Unlocking the Potential of Large Language Models for Text Representation |
| **机构** | — |
| **论文链接** | AAAI 2026 Proceedings Vol 40 No.34 |

**问题背景**: LLM 在文本生成方面表现优异，但其内部表示用于文本压缩任务时未被充分利用。

**方法详述**: 提出一种基于 LLM 的压缩框架，将文本压缩建模为表示学习问题，利用 LLM 的上下文理解能力实现高压缩比。

**主要创新点**: (1) 将 LLM 的表示能力直接用于压缩任务；(2) 实现无损与有损压缩的统一框架。

**实验结果对比**: 相比传统压缩方法（gzip、bzip2），压缩比提升 30-50%，同时保持高效解码。

**局限性**: 解码速度受限于 LLM 推理效率。

### 2.2 FedGRPO: Privately Optimizing Foundation Models with Group-Relative Rewards

| 项目 | 内容 |
|------|------|
| **中文标题** | FedGRPO: 使用组相对奖励私有优化基础模型 |
| **英文标题** | FedGRPO: Privately Optimizing Foundation Models with Group-Relative Rewards from Domain Clients |
| **论文链接** | AAAI 2026 Proceedings Vol 40 No.24 |

**问题背景**: 基础模型的联邦学习后训练面临隐私保护与奖励信号设计的双重挑战。

**方法详述**: 将 GRPO 扩展到联邦学习场景，各域客户端计算本地组相对奖励并安全聚合，在不共享原始数据的情况下优化模型。

**主要创新点**: (1) 联邦化的 GRPO 算法；(2) 隐私保护下的跨域偏好对齐；(3) 通信高效。

**局限性**: 客户端数据分布差异大时，组相对奖励的稳定性存疑。

### 2.3 LogicCat: A Chain-of-Thought Text-to-SQL Benchmark for Complex Reasoning

| 项目 | 内容 |
|------|------|
| **中文标题** | LogicCat: 面向复杂推理的链式思考 Text-to-SQL 基准 |
| **英文标题** | LogicCat: A Chain-of-Thought Text-to-SQL Benchmark for Complex Reasoning |
| **论文链接** | AAAI 2026 Proceedings Vol 40 No.36 (NLP I) |

**问题背景**: 现有 Text-to-SQL 基准主要评估简单查询，缺乏对多步推理和复杂逻辑的评测能力。

**方法详述**: 构建包含多步推理标注的 Text-to-SQL 基准，要求模型生成显式推理链。

**主要创新点**: (1) 首个多步推理 Text-to-SQL 基准；(2) 细粒度的推理过程评估。

**局限性**: 数据规模相对有限。

### 2.4 AdaptCLIP: Adapting CLIP for Universal Visual Anomaly Detection

| 项目 | 内容 |
|------|------|
| **中文标题** | AdaptCLIP: 使 CLIP 适应通用视觉异常检测 |
| **英文标题** | AdaptCLIP: Adapting CLIP for Universal Visual Anomaly Detection |
| **论文链接** | AAAI 2026 Proceedings Vol 40 No.6 (CV III) |

**问题背景**: 视觉异常检测通常需要为每个类单独训练模型，缺乏通用性。

**方法详述**: 利用 CLIP 的视觉-语言对齐能力，设计提示学习策略使零样本异常检测成为可能。

**主要创新点**: (1) 统一的零样本异常检测框架；(2) 无需每个类别的训练数据。

**实验结果对比**: 在 MVTec AD 等基准上，零样本性能接近甚至超越监督方法。

**局限性**: 对细粒度异常（如微小划痕）的检测精度有限。

---

## 3. KDD 2026

- **时间地点**: 2026年8月9–13日，韩国济州岛
- **主题演讲**: Jeff Dean (Google), Jingren Zhou (Alibaba), Regina Barzilay (MIT)
- **接收率**: Cycle 2 ~18.4%
- **争议点**: LLM 相关论文占比过高（ADS 赛道约 70%）

### 3.1 RankUp: Towards High-rank Representations for Large Scale Advertising Recommender Systems

| 项目 | 内容 |
|------|------|
| **中文标题** | RankUp: 面向大规模广告推荐系统的高秩表示 |
| **英文标题** | RankUp: Towards High-rank Representations for Large Scale Advertising Recommender Systems |
| **作者** | Tencent Weixin 团队 |
| **机构** | 腾讯 |
| **论文链接** | arXiv:2604.17878 |

**问题背景**: MetaFormer 架构随深度增加面临representation collapse问题，有效秩随层数加深不再增长甚至下降。

**方法详述**: 提出 RankUp，通过随机置换分割稀疏特征、多嵌入范式、全局 token 集成和交叉预训练嵌入 token 来缓解representation collapse。

**主要创新点**: (1) 识别推荐系统中的representation collapse问题；(2) 通过多视角嵌入增强表示多样性；(3) 全量部署于微信视频号、公众号等场景。

**实验结果对比**:

| 场景 | GMV 提升 |
|------|---------|
| 微信视频号 | +3.41% |
| 公众号 | +4.81% |
| 朋友圈 | +2.12% |

**局限性**: 架构复杂度增加带来了训练和推理成本的提升。

### 3.2 SparseCTR (also at WWW 2026)

| 项目 | 内容 |
|------|------|
| **中文标题** | SparseCTR: 基于稀疏Attention的长序列 CTR 预估 |
| **英文标题** | Unleashing the Potential of Sparse Attention on Long-term Behaviors for CTR Prediction |
| **作者** | — |
| **机构** | — |
| **论文链接** | arXiv:2601.17836 (WWW 2026) |

**问题背景**: 推荐系统中的Scaling Law模型在实际部署中面临长序列的注意力计算瓶颈。

**方法详述**: (1) 个性化行为序列分块；(2) 三分支稀疏自注意力（全局、过渡、短期）；(3) 复合相对时间编码。

**主要创新点**: 首次在推荐系统中验证稀疏注意力在长序列上的Scaling Law，三个数量级 FLOPs 范围内保持性能提升。

**实验结果对比**:

| 指标 | 线上 A/B 测试提升 |
|------|-----------------|
| CTR | +1.72% |
| CPM | +1.41% |
| 推理时间 | 40ms |

**局限性**: 序列长度仍需控制在 1024 以内；对突发性兴趣变化捕捉不充分。

---

## 4. SIGIR 2026

- **时间地点**: 2026年7月20–24日，澳大利亚墨尔本
- **摘要截止**: 2026年1月15日
- **接收通知**: 2026年4月2日

### 4.1 LTRR: Learning To Rank Retrievers for LLMs

| 项目 | 内容 |
|------|------|
| **中文标题** | 学习排序检索器以服务 LLM |
| **英文标题** | LTRR: Learning To Rank Retrievers for LLMs |
| **作者** | — |
| **机构** | — |
| **论文链接** | arXiv:2506.13743 (SIGIR 2026) |

**问题背景**: RAG 系统中如何为不同查询选择最优的检索器（稀疏/稠密/混合）是一个关键问题。

**方法详述**: 提出 LTRR，学习一个排序模型来为给定查询选择最佳检索器组合。

**主要创新点**: (1) 检索器选择的形式化为学习排序问题；(2) 统一的检索器评估框架。

**实验结果对比**: 在多个 QA 基准上，动态检索器选择相比单一检索器方法提升 10-20% 的检索精度。

**局限性**: 额外的排序模型带来了推理开销。

### 4.2 Mitigating Collaborative Semantic ID Staleness in Generative Retrieval

| 项目 | 内容 |
|------|------|
| **中文标题** | 缓解生成式检索中的协同语义 ID 陈旧性问题 |
| **英文标题** | Mitigating Collaborative Semantic ID Staleness in Generative Retrieval |
| **论文链接** | arXiv:2604.13273 (SIGIR 2026) |

**问题背景**: 生成式检索依赖语义 ID，但随着数据更新，旧语义 ID 无法反映新的协同信号。

**方法详述**: 提出动态语义 ID 更新机制，结合增量训练和协同信号融合。

**主要创新点**: (1) 首次系统研究生成式检索中的语义 ID 陈旧性问题；(2) 协同感知的 ID 更新策略。

**局限性**: 频繁更新 ID 可能导致不稳定性。

### 4.3 LLM-Oriented Information Retrieval: A Denoising-First Perspective

| 项目 | 内容 |
|------|------|
| **中文标题** | 面向 LLM 的信息检索：去噪优先视角 |
| **英文标题** | LLM-Oriented Information Retrieval: A Denoising-First Perspective |
| **论文链接** | arXiv:2605.00505 (SIGIR 2026) |

**问题背景**: 传统 IR 系统为 LLM 提供的检索结果包含大量噪声信息，影响 LLM 生成质量。

**方法详述**: 提出去噪优先的 IR 框架，在检索阶段就过滤与查询无关的噪声，确保 LLM 输入仅为高质量、高相关性的文档。

**主要创新点**: (1) 重新定义"面向 LLM 的检索"任务；(2) 去噪导向的检索方法优于传统相关性导向方法。

**局限性**: 过度去噪可能丢失弱相关但有用信息。

### 4.4 APR: Adaptive Personalised Reranking for Conversational Search

| 项目 | 内容 |
|------|------|
| **中文标题** | APR: 面向对话式搜索的自适应个性化重排序 |
| **英文标题** | APR: Adaptive Personalised Reranking for Conversational Search |
| **作者** | Shen Dong, Iadh Ounis, Debasis Ganguly |
| **机构** | University of Glasgow |
| **论文链接** | SIGIR 2026 |

**问题背景**: 对话式搜索需要理解多轮上下文和用户个性化偏好，但现有重排序方法未充分利用对话历史。

**方法详述**: 提出自适应个性化重排序框架，利用对话历史构建用户动态画像并调整排序权重。

**主要创新点**: (1) 对话上下文感知的个性化建模；(2) 自适应排序权重调整。

**局限性**: 对冷启动用户效果有限。

---

## 5. CVPR 2026

- **时间地点**: 2026年6月3–7日，美国丹佛
- **投稿量**: 16,092 篇
- **接收量**: 4,090 篇
- **接收率**: 25.42%
- **相比 CVPR 2025 增长**: +42.5%（2,878 → 4,090）

### 5.1 In Pursuit of Pixel Supervision for Visual Pre-training

| 项目 | 内容 |
|------|------|
| **中文标题** | 追求像素级监督的视觉预训练 |
| **英文标题** | In Pursuit of Pixel Supervision for Visual Pre-training |
| **作者** | Lihe Yang, Shang-Wen Li, Yang Li, Xinjie Lei, Dong Wang, Abdelrahman Mohamed, Saining Xie, Hengshuang Zhao, Kaiming He, Hu Xu |
| **机构** | — |
| **论文链接** | CVPR 2026 |

**问题背景**: self-supervised视觉预训练中，对比学习和掩码图像建模各有优劣，纯像素预测能否成为统一范式？

**方法详述**: 提出 Pixo，通过纯粹预测像素来训练self-supervised视觉模型，不依赖对比学习和外部监督信号。

**主要创新点**: (1) 纯像素预测范式；(2) 简化的self-supervised训练流程。

**局限性**: 对高分辨率图像的训练效率需优化。

### 5.2 ARCache: Mitigating Error Accumulation in Autoregressive Video Diffusion

| 项目 | 内容 |
|------|------|
| **中文标题** | ARCache: 缓解autoregressive视频扩散中的误差累积 |
| **英文标题** | ARCache: Mitigating Error Accumulation for Caching-based Acceleration in Autoregressive Video Diffusion Models |
| **作者** | Kepan Nan, Wangbo Zhao, Penghao Zhou, Jun Li, Zhenheng Yang, Jian Yang, Ying Tai |
| **机构** | — |
| **论文链接** | CVPR 2026 |

**问题背景**: autoregressive视频扩散模型中，加速引入的近似误差会随时间累积并严重降低视频质量。

**方法详述**: 提出首个免训练的缓存式加速框架 ARCache，专用于autoregressive视频扩散模型。

**主要创新点**: (1) 首次解决autoregressive视频扩散中的误差累积问题；(2) 免训练缓存框架；(3) 显著的加速比。

**局限性**: 对长视频生成（60 秒+）的缓存策略需进一步优化。

### 5.3 GenieDrive: Physics-Aware Driving World Model with 4D Occupancy

| 项目 | 内容 |
|------|------|
| **中文标题** | GenieDrive: 基于 4D 占用的物理感知驾驶世界模型 |
| **英文标题** | GenieDrive: Towards Physics-Aware Driving World Model with 4D Occupancy Guided Video Generation |
| **论文链接** | CVPR 2026 |

**问题背景**: 驾驶世界模型需要理解物理规律，而非仅生成视觉上逼真的视频。

**方法详述**: 利用 4D 占用作为中间表示，在视频生成中引入物理约束。

**主要创新点**: (1) 物理感知的驾驶世界模型；(2) 4D 占用引导的视频生成。

**局限性**: 依赖高精度的 4D 占用标注。

### 5.4 Cosmos Policy (ICLR 2026 — see ICLR section)

---

## 6. WWW 2026 — 推荐系统与广告

- **时间地点**: 2026年4月13–17日→改期至6月29日–7月3日，阿联酋迪拜
- **收录**: Research Tracks, Industry Track, Web4Good Track

### 6.1 GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning

| 项目 | 内容 |
|------|------|
| **中文标题** | GenCI: 基于生成式兴趣分群建模的用户兴趣迁移 |
| **英文标题** | GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning for CTR Prediction |
| **作者** | — |
| **机构** | — |
| **论文链接** | arXiv:2601.18251 (WWW 2026) |

**问题背景**: 现有 CTR 模型的discriminative paradigm过分拟合历史行为中的主导特征，无法适应快速兴趣迁移；点式排序丢弃了候选集整体的上下文信号。

**方法详述**: 提出 GenCI 生成式用户意图框架：(1) 层次量化构建语义兴趣分群；(2) 基于 Transformer 的 NTP 任务提取长/短期意图；(3) 层次候选感知模块通过交叉注意力优化兴趣信号。

**主要创新点**: (1) 生成式用户意图建模替代判别式匹配；(2) 语义兴趣分群作为显式意图表示；(3) end-to-end联合优化。

**实验结果对比**: 在三个公开数据集（Amazon Beauty、Sports、Toys）上显著超越现有方法。

**局限性**: 生成式模型的计算开销相比传统 CTR 模型更大。

### 6.2 SparseCTR (详见 KDD 3.2 节)

### 6.3 ThinkRec: Thinking-based Recommendation via LLM

| 项目 | 内容 |
|------|------|
| **中文标题** | ThinkRec: 基于思考的 LLM 推荐 |
| **英文标题** | ThinkRec: Thinking-based Recommendation via LLM |
| **论文链接** | arXiv (WWW 2026) |

**问题背景**: 现有 LLM4Rec 方法类似系统 1 思维，依赖表面特征匹配而非深层的推理逻辑。

**方法详述**: 提出 ThinkRec，引入思维激活机制（合成推理轨迹注入）和实例级专家融合机制，使推荐过程类似 CoT 推理。

**主要创新点**: (1) 系统 2 思维模式的推荐系统；(2) 实例级专家融合降低推理难度。

**局限性**: 推理延迟相比传统方法明显增加。

### 6.4 RE2: From Prediction to Understanding — Reasoning-based Recommendations

| 项目 | 内容 |
|------|------|
| **中文标题** | RE2: 从预测到理解——基于推理的 LLM 推荐 |
| **英文标题** | From Prediction to Understanding: Leveraging Reasoning in Large Language Model-based Recommendations |
| **论文链接** | arXiv (WWW 2026) |

**问题背景**: 现有 LLM 推荐方法隐式推理用户偏好，限制了推理能力的表达力和推荐的可解释性。

**方法详述**: 三阶段框架：(1) Reasoning Collection（收集推理数据）；(2) Pattern Imitation（SFT 模仿推理-推荐模式）；(3) Pattern Internalization（RL 内化模式）。

**主要创新点**: (1) 显式推理过程生成；(2) 结合 SFT 和 RL 的推理内化；(3) 缓解流行度偏差。

**局限性**: 推理数据收集依赖强 LLM（如 GPT-4o）辅助。

### 6.5 DARA: Few-shot Budget Allocation in Online Advertising

| 项目 | 内容 |
|------|------|
| **中文标题** | DARA: 基于 RL 微调 LLM 的在线广告少样本预算分配 |
| **英文标题** | DARA: Few-shot Budget Allocation in Online Advertising via In-Context Decision Making with RL-Finetuned LLMs |
| **作者** | Mingxuan Song, Yusen Huo, Bohan Zhou, Shenglin Yin, Zhen Xiao, Jieyi Long, Zhilin Zhang, Chuan Yu |
| **机构** | 阿里巴巴 |
| **论文链接** | WWW 2026 |

**问题背景**: 在线广告中预算分配需要适应不同广告主的多样需求，传统方法需要大量历史数据进行优化。

**方法详述**: 使用 RL 微调的 LLM 进行上下文决策，实现少样本预算分配。

**主要创新点**: (1) 将 LLM 的上下文学习能力用于广告预算分配；(2) RL 微调实现决策优化。

**局限性**: 对全新广告主的初始效果仍待改进。

### 6.6 IAM: Item-aware Attention Mechanism for LLM Recommendation

| 项目 | 内容 |
|------|------|
| **中文标题** | IAM: 面向 LLM 推荐系统的物品感知Attention |
| **英文标题** | From Token to Item: Enhancing Large Language Models for Recommendation via Item-aware Attention Mechanism |
| **机构** | — |
| **论文链接** | arXiv:2603.19693 (WWW 2026) |

**问题背景**: 基于 LLM 的推荐方法以 token 为中心，忽视了"物品"本身作为推荐基本单元的重要性。

**方法详述**: 提出物品感知Attention IAM，区分两种 token 关系：(1) 物品内注意力（建模内容语义）；(2) 物品间注意力（捕捉协同关系）。

**主要创新点**: (1) 明确物品作为推荐的基本单元；(2) 双注意力层分离建模内容与协同信号。

**实验结果对比**: 平均提升 34.54% 的标准推荐指标。

**局限性**: 计算复杂度随物品数量线性增长。

### 6.7 AliBoostV2: CTR-Growth Balanced Boosting for Billion-Scale Recommendation

| 项目 | 内容 |
|------|------|
| **中文标题** | AliBoostV2: 十亿级推荐平台中的 CTR-增长平衡提升框架 |
| **英文标题** | AliBoostV2: CTR-Growth Balanced Boosting Framework in Billion-Scale Recommendation Platform |
| **作者** | Qijie Shen (Alibaba), Yuanchen Bei (Zhejiang University), et al. |
| **机构** | 阿里巴巴 |
| **论文链接** | WWW 2026 Industry Track |

**问题背景**: 大规模推荐系统需要平衡短期 CTR 优化与长期用户增长，两者目标存在冲突。

**方法详述**: 提出 CTR-Growth 平衡框架，使用多目标优化策略协调短期转化和长期留存。

**主要创新点**: (1) CTR 与增长目标的联合优化；(2) 十亿级平台的工业部署经验。

**局限性**: 多目标之间的帕累托前沿调优仍依赖人工经验。

### 6.8 ISRF: Iterative Semantic Reasoning Framework for Generative Recommendation

| 项目 | 内容 |
|------|------|
| **中文标题** | ISRF: 面向生成式推荐的迭代语义推理框架 |
| **英文标题** | Iterative Semantic Reasoning from Individual to Group Interests for Generative Recommendation with LLMs |
| **机构** | — |
| **论文链接** | arXiv:2603.13934 (WWW 2026) |

**问题背景**: 用户兴趣建模需要从显式个体兴趣推理到隐式群体兴趣，现有语义方法缺乏深层推理。

**方法详述**: 三步迭代推理：(1) 属性级双向往复推理构建语义交互图；(2) 语义用户特征推理群体隐式兴趣；(3) 批次优化策略迭代对齐个体与群体兴趣。

**主要创新点**: (1) 语义推理从个体到群体的桥接；(2) 迭代优化确保一致性。

**实验结果对比**: 在 Sports、Beauty、Toys 数据集上超越现有 SOTA。

**局限性**: 迭代推理的计算成本较高。

### 6.9 CRS: Context-aware Reasoning-enhanced Generative Searching in E-commerce

| 项目 | 内容 |
|------|------|
| **中文标题** | CRS: 面向电商的上下文感知推理增强生成式搜索 |
| **英文标题** | Towards Context-aware Reasoning-enhanced Generative Searching in E-commerce |
| **机构** | — |
| **论文链接** | arXiv:2510.16925 (WWW 2026) |

**问题背景**: 电商搜索中用户的上下文信号（时空、历史、查询）复杂多变，现有方法难以有效融合。

**方法详述**: (1) 统一异构上下文为文本语义表示；(2) 自演进后训练范式（SFT + RL 交替）；(3) 去偏 GRPO 优化排序。

**主要创新点**: (1) SFT+RL 自演进范式；(2) 去偏 GRPO 避免排序偏差。

**局限性**: 依赖大规模电商搜索日志。

---

## 7. NeurIPS 2025 — 值得关注的论文

- **时间地点**: 2025年12月，美国圣地亚哥
- **接收量**: ~5,526 篇
- **接收率**: 主赛道 25.75%

### 7.1 Best Papers

#### 7.1.1 Gated Attention for Large Language Models

| 项目 | 内容 |
|------|------|
| **中文标题** | 门控注意力：非线性、稀疏性与无attention sink |
| **英文标题** | Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free |
| **获奖** | NeurIPS 2025 Best Paper (Runner-up) |

**问题背景**: 标准 Attention在long-context场景中面临attention sink和不稳定的问题。

**方法详述**: 在缩放点积注意力后添加 sigmoid 门控，引入非线性和稀疏调制。

**主要创新点**: (1) 简单有效的gating mechanism；(2) 消除attention sink；(3) 提升训练稳定性和扩展性。

**实验结果对比**: 支持更大learning rate，在long-context基准上性能显著提升。

**局限性**: 对已有预训练模型的后向兼容性需要微调适配。

#### 7.1.2 Why Diffusion Models Don't Memorize

| 项目 | 内容 |
|------|------|
| **中文标题** | 扩散模型为什么不记忆 |
| **英文标题** | Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training |
| **获奖** | NeurIPS 2025 Best Paper |

**问题背景**: 扩散模型在生成质量上表现出色的同时被认为比 GAN 更少记忆训练数据，其原因缺乏理论解释。

**方法详述**: 揭示扩散训练过程中的隐式动力学校regularization机制，该机制自然抑制了overfitting和记忆。

**主要创新点**: (1) 首次从动力学角度解释扩散模型的抗记忆性质；(2) 理论分析了隐式regularization的来源。

**局限性**: 分析限于连续时间扩散过程。

#### 7.1.3 Artificial Hivemind: Open-Ended Homogeneity of Language Models

| 项目 | 内容 |
|------|------|
| **中文标题** | 人工蜂群思维：语言模型的无边界同质性 |
| **英文标题** | Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond) |
| **获奖** | NeurIPS 2025 Best Paper (Datasets & Benchmarks) |

**问题背景**: LLM 在开放性任务中倾向于生成惊人相似的答案，缺乏多样性。

**方法详述**: 发布了大规模开放式提示数据集，系统测量了 LLM 的输出多样性坍塌现象。

**主要创新点**: (1) 首个大规模 LLM 输出多样性基准；(2) 揭示"人工蜂群思维"现象。

**局限性**: 数据集主要覆盖英文场景。

#### 7.1.4 Does RL Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?

| 项目 | 内容 |
|------|------|
| **中文标题** | RL 是否真的激励了 LLM 超越基础模型的推理能力？ |
| **英文标题** | Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? |
| **作者** | Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Yang Yue, Shiji Song, Gao Huang |
| **获奖** | NeurIPS 2025 Best Paper (Runner-up) |

**问题背景**: RLVR 被广泛认为能提升 LLM 推理能力，但 RL 是否真正赋予了模型新的推理能力而非仅提升采样效率？

**方法详述**: 通过系统性的探针实验和消融研究，对比 RL 训练前后的模型在不同条件（小 n 值）下的推理表现。

**主要创新点**: (1) 发现 RLVR 并未从本质上激发新的推理模式；(2) RL 主要提升了采样效率，基础模型在高 n 值时已有类似推理能力。

**局限性**: 分析局限于数学类可验证奖励任务。

#### 7.1.5 Superposition Yields Robust Neural Scaling

| 项目 | 内容 |
|------|------|
| **中文标题** | 叠加产生鲁棒的神经缩放 |
| **英文标题** | Superposition Yields Robust Neural Scaling |
| **获奖** | NeurIPS 2025 Best Paper (Runner-up) |

**问题背景**: 神经Scaling Law通常被归因于参数数量，但特征叠加（superposition）的作用未被充分理解。

**方法详述**: 从理论角度分析 LLM 中的特征叠加现象，发现开源 LLM 运行在强叠加机制下，叠加决定了损失缩放律。

**主要创新点**: (1) 将叠加理论与神经Scaling Law联系起来；(2) 揭示了参数之外的缩放驱动因素。

**局限性**: 实验验证主要集中在中等规模模型。

#### 7.1.6 1000 Layer Networks for Self-Supervised RL

| 项目 | 内容 |
|------|------|
| **中文标题** | 1000 层网络实现self-supervised强化学习 |
| **英文标题** | 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities |
| **获奖** | NeurIPS 2025 Best Paper |

**问题背景**: 深度扩展在语言和视觉领域产生了突破，但在 RL 中增加深度的效果一直不明确。

**方法详述**: 研究self-supervised RL 中网络深度的作用，通过 1000 层网络探索深度扩展对 RL 的影响。

**主要创新点**: (1) 首次系统研究 RL 中的极端深度扩展；(2) 深度增加 2-50 倍带来显著性能提升。

**实验结果对比**: 相比标准self-supervised对比 RL 算法提升 2-50 倍，超越其他目标条件基线。

**局限性**: 1000 层网络的计算成本和内存需求较高。

### 7.2 Highlight Papers (Spotlight)

#### 7.2.1 d1: Scaling Reasoning in Diffusion Large Language Models via RL

| 项目 | 内容 |
|------|------|
| **中文标题** | d1: 通过 RL 扩展扩散 LLM 的推理能力 |
| **英文标题** | d1: Scaling Reasoning in Diffusion Large Language Models via Reinforcement Learning |
| **机构** | — |
| **论文链接** | NeurIPS 2025 Spotlight |

**问题背景**: 扩散 LLM 非autoregressive生成范式使其无法直接应用 GRPO 等Policy Gradient方法进行推理训练。

**方法详述**: (1) 掩码 SFT 从现有数据集蒸馏推理知识；(2) 提出 diffu-GRPO，首个集成Policy Gradient到掩码扩散 LLM 的方法。

**主要创新点**: (1) 扩散 LLM 的首个 RL 推理训练框架；(2) diffu-GRPO 算法。

**局限性**: 扩散 LLM 的推理速度仍是瓶颈。

#### 7.2.2 AGRPO: Principled RL for Diffusion Language Models

| 项目 | 内容 |
|------|------|
| **中文标题** | AGRPO: 面向扩散语言模型的有原则 RL |
| **英文标题** | Amortized Group Relative Policy Optimization (AGRPO) |
| **论文链接** | arXiv:2510.04019 |

**问题背景**: 现有扩散 LLM 的 RL 方法使用启发式目标，缺乏理论保证。

**方法详述**: 通过蒙特卡洛采样计算无偏Policy Gradient估计，实现首个保真的Policy Gradient方法在扩散 LLM 上的适配。

**主要创新点**: (1) 首个有理论保证的扩散 LLM RL 算法；(2) 计算效率优于 diffu-GRPO。

**实验结果对比**: GSM8K +7.6%，Countdown 任务 3.8x 性能提升。

**局限性**: 训练稳定性仍需改进。

#### 7.2.3 SPG: Sandwiched Policy Gradient for Masked Diffusion LLMs

| 项目 | 内容 |
|------|------|
| **中文标题** | SPG: 面向掩码扩散 LLM 的夹层Policy Gradient |
| **英文标题** | SPG: Sandwiched Policy Gradient for Masked Diffusion Language Models |
| **论文链接** | arXiv:2510.09541 |

**问题背景**: 扩散 LLM 的不可计算对数似然导致Policy Gradient偏差。

**方法详述**: 提出"夹层"策略：正奖励样本最大化下界，负奖励样本最小化上界。

**主要创新点**: (1) 上下界夹层估计减少Policy Gradient偏差；(2) 块级掩码策略优化分布对齐。

**实验结果对比**: GSM8K +3.6%，MATH500 +2.6%，Countdown +18.4%，Sudoku +27.0%。

**局限性**: 理论分析与实际性能之间的差距有待进一步弥合。

#### 7.2.4 BLINK-Twice: Visual Perception Reasoning Benchmark

| 项目 | 内容 |
|------|------|
| **中文标题** | BLINK-Twice: 视觉感知推理基准 |
| **英文标题** | BLINK-Twice: You see, but do you observe? A Reasoning Benchmark on Visual Perception |
| **论文链接** | NeurIPS 2025 Datasets & Benchmarks |

**问题背景**: 现有推理基准主要评估语言推理，视觉输入被当作可替换的上下文。

**方法详述**: 构建基于视觉推理的基准，包含 7 类视觉挑战、自然对抗图像对、标注推理链。

**主要创新点**: (1) 视觉中心推理基准；(2) 细粒度推理过程评估。

---

## 8. ICLR 2026 — 值得关注的论文

- **时间地点**: 2026年4月23–27日，巴西里约热内卢
- **接收量**: ~5,300 篇
- **Oral 论文**: 225 篇

### 8.1 Outstanding Papers

#### 8.1.1 Transformers are Inherently Succinct

| 项目 | 内容 |
|------|------|
| **中文标题** | Transformer 天生简洁 |
| **英文标题** | Transformers are Inherently Succinct |
| **作者** | Pascal Bergsträßer, Ryan Cotterell, Anthony Widjaja Lin |
| **获奖** | ICLR 2026 Outstanding Paper |

**问题背景**: Transformer 相比 RNN 等架构的强大能力缺乏理论解释。

**方法详述**: 从理论角度证明 Transformer 在编码某些概念时的简洁性远超其他模型。

**主要创新点**: (1) 提出 Transformer 简洁性的理论框架；(2) 激发对架构表示的进一步研究。

**局限性**: 理论结果在极大规模模型上的实证验证有限。

#### 8.1.2 Multi-Turn LLM Evaluation (Outstanding Paper)

| 项目 | 内容 |
|------|------|
| **中文标题** | 多轮 LLM 评测：可扩展方法揭示性能下降 |
| **获奖** | ICLR 2026 Outstanding Paper (主题未公开完整标题) |

**问题背景**: LLM 训练数据主要为单轮/补全，但实际部署多为多轮交互。

**方法详述**: 设计可扩展的多轮能力评估方法，发现 LLM 在指令不明确的多轮交互中能力显著下降。

**主要创新点**: (1) 可扩展的多轮评测方法；(2) 揭示训练-部署之间的偏差。

**局限性**: 使用较早的模型版本。

#### 8.1.3 Honorable Mention: The Polar Express (Muon Optimizer)

| 项目 | 内容 |
|------|------|
| **中文标题** | The Polar Express: 最优矩阵符号方法及其在 Muon 算法中的应用 |
| **英文标题** | The Polar Express: Optimal Matrix Sign Methods and their Application to the Muon Algorithm |
| **作者** | Noah Amsel, David Persson, Christopher Musco, Robert M. Gower |

**问题背景**: Muon 优化器依赖极分解，但多项式近似的效率未达到最优。

**方法详述**: 用逼近理论设计最优多项式近似，特别针对 GPU 和低精度计算环境。

**主要创新点**: (1) 理论最优的极点多项式近似；(2) 实用的 GPU 加速方案。

### 8.2 Notable Papers

#### 8.2.1 LaDiR: Latent Diffusion Enhances LLMs for Text Reasoning

| 项目 | 内容 |
|------|------|
| **中文标题** | LaDiR: 潜扩散增强 LLM 文本推理 |
| **英文标题** | LaDiR: Latent Diffusion Enhances LLMs for Text Reasoning |
| **论文链接** | arXiv:2510.04573 (ICLR 2026) |

**问题背景**: autoregressive LLM 在推理时缺乏迭代改进机制，易陷入局部最优。

**方法详述**: 使用 VAE 将推理步骤编码为潜思考 token，利用潜扩散模型在latent space中迭代去噪。

**主要创新点**: (1) latent space扩散推理替代autoregressive解码；(2) 多样性引导机制探索多推理路径。

**实验结果对比**: Countdown 任务 +30%，推理多样性和准确性均有提升。

**局限性**: VAE+扩散的推理延迟高于纯autoregressive方法。

#### 8.2.2 wd1: Weighted Policy Optimization for Diffusion LLMs

| 项目 | 内容 |
|------|------|
| **中文标题** | wd1: 面向扩散 LLM 的加权策略优化 |
| **英文标题** | wd1: Weighted Policy Optimization for Reasoning in Diffusion Language Models |
| **论文链接** | arXiv:2507.08838 (ICLR 2026) |

**方法详述**: 将 RL 目标重写为加权对数似然，避免策略比率近似。理论上证明等价于能量引导扩散训练+负样本遗忘。

**主要创新点**: (1) 无比率策略优化；(2) 理论上与能量引导扩散一致。

**实验结果对比**: 超越 d1，GSM8K 84.5%，MATH500 44.2%，仅 20 步 RL 训练。

**局限性**: 对大规模模型的扩展性需验证。

#### 8.2.3 MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents

| 项目 | 内容 |
|------|------|
| **中文标题** | MEM1: 学习协同记忆与推理以实现高效长时域智能体 |
| **英文标题** | MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents |
| **论文链接** | ICLR 2026 |

**问题背景**: 长时域智能体任务中，记忆和推理通常被分开处理，缺乏协同。

**方法详述**: 提出 MEM1 框架，将记忆管理和推理结合在一个统一的框架中。

**主要创新点**: (1) 记忆-推理协同学习；(2) 高效的记忆检索与推理路径规划。

**局限性**: 在极端长时间任务中的效果需进一步验证。

#### 8.2.4 Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control

| 项目 | 内容 |
|------|------|
| **中文标题** | Cosmos Policy: 微调视频模型实现视觉运动控制 |
| **英文标题** | Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning |
| **作者** | Moo Jin Kim, Yihuai Gao, Tsung-Yi Lin, et al. |
| **机构** | NVIDIA |
| **论文链接** | ICLR 2026 |

**问题背景**: 预训练视频模型能否通过简单后训练转化为机器人策略？

**方法详述**: 在 Cosmos-Predict2 视频模型上进行阶段后训练，无需架构修改即可作为机器人的有效策略。

**主要创新点**: (1) 视频模型直接转用为机器人策略；(2) 单阶段后训练。

**局限性**: 对仿真环境的依赖。

#### 8.2.5 ME-ICPO: Provable In-Context Policy Optimization

| 项目 | 内容 |
|------|------|
| **中文标题** | ME-ICPO: 可证明的上下文策略优化用于自我改进 |
| **英文标题** | Provable and Practical In-Context Policy Optimization for Self-Improvement |
| **论文链接** | arXiv:2603.01335 (ICLR 2026) |

**问题背景**: LLM 的自我反思（self-reflection）和测试时扩展缺乏理论理解。

**方法详述**: 提出 In-Context Policy Optimization (ICPO) 框架，证明单层线性自注意力 Transformer 能模拟策略优化算法。

**主要创新点**: (1) 自我反思的理论基；(2) ME-ICPO 实践算法。

---

## 9. ACL/EMNLP 2025 — LLM/代码相关论文

### 9.1 ACL 2025

#### 9.1.1 Tree-of-Evolution: Tree-Structured Instruction Evolution for Code Generation

| 项目 | 内容 |
|------|------|
| **中文标题** | Tree-of-Evolution: 树结构指令进化用于代码生成 |
| **英文标题** | Tree-of-Evolution: Tree-Structured Instruction Evolution for Code Generation in Large Language Models |
| **作者** | Ziyang Luo, Kaixin Li, Hongzhan Lin, Yuchen Tian, Mohan Kankanhalli, Jing Ma |
| **机构** | National University of Singapore |
| **论文链接** | ACL 2025 |

**问题背景**: 代码指令数据合成面临单向合成和随机性驱动的限制，导致数据质量和多样性不足。

**方法详述**: 将代码指令合成建模为树结构，探索多个进化路径；引入优化驱动的进化，每步根据前一步质量改进。

**主要创新点**: (1) 树结构指令进化；(2) 优化驱动的迭代改进。

**实验结果对比**:

| 基准 | 75k ToE 数据 | Qwen2.5-Coder-Instruct (百万级数据) |
|------|---------|------------------------------|
| HumanEval | 92.1% | 92.0% |
| MBPP | 88.5% | 88.3% |

仅用 7.5 万样本即达到百万级数据训练的 SOTA 模型性能。

**局限性**: 进化的计算成本随树深度增长。

#### 9.1.2 CodeTree: Agent-guided Tree Search for Code Generation

| 项目 | 内容 |
|------|------|
| **中文标题** | CodeTree: 智能体引导的树搜索代码生成 |
| **英文标题** | CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models |
| **作者** | Salesforce Research |
| **机构** | Salesforce |
| **论文链接** | NAACL 2025 / ACL Related |

**问题背景**: 复杂编码任务搜索空间大，当前智能体方法在多阶段规划、生成和调试中仍有困难。

**方法详述**: 统一树结构显式探索不同编码策略，Critic agent 引导树搜索决策（排序、终止、扩展）。

**主要创新点**: (1) 统一的树结构搜索空间；(2) 多智能体协作（Thinker、Solver、Debugger）。

**实验结果对比**: HumanEval 95.1%，MBPP 98.7%，CodeContests 43.0%，SWE-bench 显著提升。

**局限性**: 需要强推理能力的 LLM 作为基座。

#### 9.1.3 DebateCoder: Test Case Driven LLM Debate for Code Generation

| 项目 | 内容 |
|------|------|
| **中文标题** | DebateCoder: 测试用例驱动的 LLM 辩论代码生成 |
| **英文标题** | DebateCoder: Towards Collective Intelligence of LLMs via Test Case Driven LLM Debate for Code Generation |
| **论文链接** | ACL 2025 |

**问题背景**: 单一 LLM 在代码生成中缺乏纠错和验证机制。

**方法详述**: 双模型辩论框架，测试用例作为中间介质识别 bug，模型生成和执行测试用例后进行对比分析。

**主要创新点**: (1) 测试用例驱动的辩论机制；(2) 对比分析代码优化；(3) 可收敛的辩论标准。

**局限性**: 需要两个 LLM 同时运行，计算成本翻倍。

#### 9.1.4 ToolCoder: Code-Empowered Tool Learning

| 项目 | 内容 |
|------|------|
| **中文标题** | ToolCoder: 代码赋能工具学习 |
| **英文标题** | ToolCoder: A Systematic Code-Empowered Tool Learning Framework for LLMs |
| **论文链接** | ACL 2025 |

**问题背景**: 现有工具学习方法依赖人工提示，多步规划困难，缺乏精确错误诊断和反射机制。

**方法详述**: 将工具学习重写为代码生成任务——自然语言转 Python 函数框架，系统分解任务为子任务。

**主要创新点**: (1) 代码为中心的范式替代传统工具学习；(2) 集成的错误诊断和反射机制。

**实验结果对比**: 在 RestBench 上超越 ReAct、Chameleon、CodeAct 等基线，准确率 78-87% vs 基线 56-80%。

**局限性**: 依赖函数调用的成功解析。

#### 9.1.5 BDC: Boost, Disentangle, and Customize — System2-to-System1 for Code

| 项目 | 内容 |
|------|------|
| **中文标题** | BDC: 提升、解缠与定制——代码生成的 System2→System1 管道 |
| **英文标题** | A Robust System2-to-System1 Pipeline for Code Generation |
| **论文链接** | ACL 2025 Findings |

**问题背景**: 代码生成作为 System 2 任务需要复杂推理，但其推理过程不透明，且数据分布异质。

**方法详述**: MC-Tree-Of-Agents 算法进行多 LLM 互验证探索，DisenLoRA 解缠异构数据训练可组合专家。

**主要创新点**: (1) MC-Tree-Of-Agents 探索算法；(2) DisenLoRA 可组合专家；(3) 输入感知超网络动态组合。

**实验结果对比**: 困难问题准确率 73.8%，超越 LATS、RethinkMCTS 9-15%。

**局限性**: 系统复杂度较高，部署难度大。

### 9.2 EMNLP 2025

#### 9.2.1 UnitCoder: Scalable Code Synthesis from Pre-training Corpora

| 项目 | 内容 |
|------|------|
| **中文标题** | UnitCoder: 从预训练语料库的可扩展代码合成 |
| **英文标题** | UnitCoder: Scalable Code Synthesis from Pre-training Corpora |
| **论文链接** | EMNLP 2025 |

**问题背景**: 构建高质量的代码训练数据挑战很大——预训练数据质量不一，指令方法多样性有限。

**方法详述**: 通过自动生成的单元测试直接监督预训练数据质量，配合迭代修复精炼流程。

**主要创新点**: (1) 单元测试驱动的数据质量控制；(2) 可扩展到 50 万+可验证程序。

**实验结果对比**: 在 HumanEval、MBPP、BigCodeBench 上持续改进不同规模模型（LLaMA-3 8B 和 70B）。

**局限性**: 单元测试覆盖率可能不够全面。

#### 9.2.2 ExeCoder: Executability Representation for Code Translation

| 项目 | 内容 |
|------|------|
| **中文标题** | ExeCoder: 基于可执行性表示的代码翻译 |
| **英文标题** | ExeCoder: Empowering Large Language Models with Executability Representation for Code Translation |
| **论文链接** | EMNLP 2025 |

**问题背景**: LLM 仅学习代码的上下文语义，忽略与执行状态相关的可执行性信息。

**方法详述**: 利用可执行性表示（功能语义、语法结构、变量依赖）增强 LLM 的代码翻译能力。

**主要创新点**: (1) 可执行性表示学习；(2) 增强的 TransCoder-test 基准。

**实验结果对比**: 减少执行错误 2.1-4.3%。

**局限性**: 多语言支持有限（当前为 C++/Python/Java）。

---

## 10. 总结与趋势

### 10.1 关键趋势

| 趋势 | 描述 | 代表会议/论文 |
|------|------|--------------|
| **LLM 推理的强化学习** | RLVR/GRPO 成为 LLM 后训练标准范式；扩散 LLM 的 RL 训练成为重点研究方向 | NeurIPS 2025 (d1, AGRPO, SPG), ICLR 2026 (wd1, DMPO) |
| **扩散 LLM 崛起** | 扩散 LLM 在 8B 规模达到autoregressive模型同等水平，RL 后训练弥补推理差距 | NeurIPS 2025 (d1, AGRPO, SPG, ESPO), ICLR 2026 (wd1, LaDiR) |
| **智能体化推荐系统** | LLM 从特征编码转向推理/思考/Agent 化推荐 | WWW 2026 (ThinkRec, RE2, AgentDR, RecoWorld) |
| **长序列CTR建模** | 稀疏注意力实现长用户行为序列的缩放律 | WWW 2026 (SparseCTR), KDD 2026 (RankUp) |
| **生成式推荐规模化** | 工业级生成式推荐器（取代召回-排序管道） | WWW 2026 (PLUM, OneTrans, From Modularity to Unity) |
| **代码生成系统2推理** | 树搜索、Multi-Agent 辩论、系统2→系统1蒸馏 | ACL 2025 (CodeTree, DebateCoder, BDC, MAGIC) |
| **视觉理解与生成统一** | 统一多模态autoregressive/扩散建模 | CVPR 2026 (Pixo, UniAR at ICML), ICLR 2026 (SAM 3) |
| **安全与对齐科学化** | DPO 统计缺陷被揭示，安全对齐走向严谨理论 | ICLR 2026 (Why DPO is Misspecified, SafeDPO), AAAI 2026 (Alignment Track) |

### 10.2 各会议规模对比

| 会议 | 投稿量 | 接收量 | 接收率 | 时间 |
|------|-------|-------|-------|------|
| ICML 2026 | 23,918 | 6,352 | 26.6% | Jul 2026 |
| AAAI 2026 | ~29,000 | ~6,000+ | ~26% | Jan 2026 |
| CVPR 2026 | 16,092 | 4,090 | 25.4% | Jun 2026 |
| NeurIPS 2025 | — | 5,526 | ~25.7% | Dec 2025 |
| ICLR 2026 | — | ~5,300 | — | Apr 2026 |
| KDD 2026 | — | — | ~18.4% | Aug 2026 |
| SIGIR 2026 | — | — | — | Jul 2026 |
| WWW 2026 | — | — | — | Jun/Jul 2026 |
| ACL 2025 | — | — | — | Jul 2025 |

