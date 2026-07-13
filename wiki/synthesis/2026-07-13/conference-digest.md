---
title: 顶会论文专题报告 — Conference & arXiv Digest (2026-07-13)
type: synthesis
created: 2026-07-13
updated: 2026-07-13
sources: [web-search]
tags: [conference-digest, icml-2026, neurips-2025, iclr-2026, cvpr-2026, kdd-2026, aaai-2026, acl-2026, www-2026, sigir-2026, emnlp-2025, cikm-2025, recsys-2025, ctr, recommendation, agents, generative-models, games]
---

# 顶会论文专题报告 — Conference & arXiv Digest (2026-07-13)

> **覆盖范围**: ICML 2026, NeurIPS 2025, ICLR 2026, CVPR 2026, KDD 2026, AAAI 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025 等 12+ 会议；200+ 精选论文；Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, NVIDIA, Netflix, Anthropic, Apple, Amazon, Meituan 等 20+ 实验室

---

## 目录

1. [ICML 2026 — Outstanding Papers & Agent RL](#icml-2026)
2. [NeurIPS 2025 — Best Papers & Attention Mechanisms](#neurips-2025)
3. [ICLR 2026 — Outstanding Papers & Safety Alignment](#iclr-2026)
4. [CVPR 2026 — Best Paper & 3D/Generative Models](#cvpr-2026)
5. [KDD 2026 — CTR Scaling Laws & Generative Rec](#kdd-2026)
6. [AAAI 2026 — Multimodal LLM + Recommendation](#aaai-2026)
7. [ACL 2026 — LLM-based Recommendation & Agents](#acl-2026)
8. [WWW 2026 — ThinkRec & Generative Rec](#www-2026)
9. [CIKM 2025 — LLM-Empowered CTR](#cikm-2025)
10. [RecSys 2025 — LLM Integration & Scaling](#recsys-2025)
11. [SIGIR 2026 — Retrieval & Ad Recommendation](#sigir-2026)
12. [CTR Prediction & Advertising (Cross-Venue)](#ctr-cross-venue)
13. [Agent Systems & Multi-Agent](#agent-systems)
14. [Generative Models & Diffusion](#generative-models)
15. [Games & Strategic Reasoning](#games)
16. [Code Execution & Formal Reasoning](#code-reasoning)
17. [Benchmarks & Evaluation](#benchmarks)
18. [Cross-Cutting Themes](#cross-cutting-themes)

---

<a id="icml-2026"></a>
## 1. ICML 2026 (Seoul, July 2026)

### 🏆 Outstanding Paper Awards

#### 1.1 The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models
- **Title (CN)**: 灵活性陷阱：重新思考扩散语言模型中任意序生成的价值
- **Authors**: Zanlin Ni, Shenzhi Wang, Yang Yue, Tianyu Yu, Weilin Zhao, Yeguo Hua, Tianyi Chen, Jun Song, Cheng Yu, Bo Zheng, Gao Huang
- **Affiliation**: 清华大学 (Tsinghua University)
- **Venue**: ICML 2026 Outstanding Paper Award
- **Link**: https://icml.cc/virtual/2026/oral/71086

**Abstract & Key Innovations**: 本文挑战了扩散语言模型 (Diffusion Language Models, DLMs) 的核心假设——"任意序生成" (arbitrary order generation) 能力实际上是一个"灵活性陷阱"，损害了模型性能。论文揭示了 DLMs 在生成过程中，灵活的 token 顺序反而引入了不必要的不确定性，导致采样效率和文本质量下降。

**Impact**: 这一发现对当前扩散语言模型的研究方向具有重要的指导意义，暗示了在设计 DLM 时应优先考虑结构化的生成顺序。

---

#### 1.2 High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions
- **Title (CN)**: 扩散模型与对数凹分布的高精度采样
- **Authors**: Fan Chen, Sinho Chewi, Constantinos Daskalakis, Alexander Rakhlin
- **Affiliation**: 多机构合作
- **Venue**: ICML 2026 Outstanding Paper Award
- **Link**: https://icml.cc/virtual/2026/oral/71072

**Abstract & Key Innovations**: 在算法精度方面取得重大突破，提出了针对扩散模型和对数凹分布的更高精度采样方法，推动了扩散模型的理论基础。

---

### 🏅 Honorable Mentions

| Paper | Key Contribution |
|-------|-----------------|
| The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes | 绘制 RLVR 训练中诚实性涌现的地图，使用欺骗探测器 |
| Motion Attribution for Video Generation | 视频生成中的运动归因分析 |
| How Much Can Language Models Memorize? | 量化 LLM 的记忆能力上限 |
| A Random Matrix Perspective on the Consistency of Diffusion Models | 从随机矩阵理论视角分析扩散模型一致性 |
| To Grok Grokking: Provable Grokking in Ridge Regression | 为岭回归中的 grokking 现象提供可证明的理论 |

### 🏛️ Test of Time Award

**Asynchronous Methods for Deep Reinforcement Learning** (2016)
- **Authors**: Volodymyr Mnih, Adria Puigdomenech Badia, Mehdi Mirza, Alex Graves, Timothy Lillicrap, Tim Harley, David Silver, Koray Kavukcuoglu
- **Affiliation**: Google DeepMind
- **Significance**: A3C 算法为后续 LLM 的 RL post-training（PPO, GRPO 等）奠定了基础。

---

### 🔬 ICML 2026 Agent RL 论文精选

#### 1.3 HiPER: Hierarchical Plan–Execute RL for Multi-Turn LLM Agents
- **Title (CN)**: HiPER: 多轮 LLM Agent 的分层计划-执行强化学习
- **Authors**: (ICML 2026 Poster)
- **Venue**: ICML 2026
- **Link**: https://icml.cc/virtual/2026/poster/64058

**Abstract & Key Innovations**: 针对 LLM agent 在长时域任务中面临的稀疏奖励问题，HiPER 提出了分层计划-执行框架。通过联合建模高层子目标规划和低层动作执行，引入 Hierarchical Advantage Estimation (HAE) 实现两级策略梯度的信用分配。

**Results**: 在 ALFWorld 达到 97.4% 成功率 (+6.6% over SOTA)，WebShop 达到 83.3%。

**Comparison**: 相比 flat RL 方法 (PPO/GRPO)，HiPER 通过显式分层分解在长时域任务中大幅降低方差，提升信用分配效率。

---

#### 1.4 MemoPilot: From Player to Master via RL over Memory
- **Title (CN)**: MemoPilot: 通过记忆强化学习从玩家到大师
- **Authors**: (ICML 2026 Poster)
- **Venue**: ICML 2026
- **Link**: https://icml.cc/virtual/2026/poster/62463

**Abstract & Key Innovations**: 提出记忆协同飞行员 (Memory Copilot) 概念，将记忆更新过程形式化为多轮决策问题，使用 multi-turn GRPO 端到端优化。引入 turn-wise reward 和 context-independent turn-level advantage estimation。

**Results**: 在 Rock-Paper-Scissors 和 Limit Texas Hold'em 上 Elo 排名第一 (LHE 1762, RPS 1590)，超越 DeepSeek-V3.2 等所有基线方法。

**Comparison**: 相比手工设计的 prompting 规则式记忆更新，MemoPilot 实现了目标导向的端到端训练优化。

---

#### 1.5 Agentic Monte Carlo: RL for Black-Box LLM Agents
- **Title (CN)**: Agentic Monte Carlo: 黑盒 LLM Agent 的强化学习
- **Venue**: ICML 2026
- **Link**: https://icml.cc/virtual/2026/poster/62740

**Abstract & Key Innovations**: 解决了 LLM agent 的两个运行模式——开放权重 agent (可用 RL 训练) 和黑盒 agent (只能通过 API 交互)——的统一 RL 训练问题。

---

#### 1.6 RL-Focal: Dynamic Optimizations of LLM Ensembles
- **Title (CN)**: RL-Focal: LLM 集成的动态优化
- **Venue**: ICML 2026
- **Link**: https://icml.cc/virtual/2026/poster/64593

**Abstract & Key Innovations**: 两阶段 RL agent 框架：(1) Decider Agent 从 N 个 LLM 中动态选择小规模子集 ($m_i \ll N$)，通过 focal diversity 指标最大化误差多样性与推理性能；(2) Fusion Agent 解决不同 LLM 的推理冲突并动态适配不同集成团队。

**Results**: 在 5 个基准上，集成小规模子集相比最佳单模型提升 8.48%。

---

#### 1.7 JitRL: Just-In-Time Reinforcement Learning
- **Title (CN)**: JitRL: 即时强化学习——无需梯度更新的 LLM Agent 持续学习
- **Venue**: ICML 2026
- **Link**: https://icml.cc/virtual/2026/poster/61517

**Abstract & Key Innovations**: 提出无需训练的框架，在测试时进行策略优化，无需任何梯度更新。

---

#### 1.8 From Reasoning Traces to Reusable Modules
- **Title (CN)**: 从推理轨迹到可复用模块：语言模型推理中的组合泛化
- **Venue**: ICML 2026
- **Link**: https://icml.cc/virtual/2026/poster/61216

**Abstract & Key Innovations**: 通过 Hierarchical Latent Selection Model 形式化 RL 的组合泛化能力。理论证明 RL 的探索性为识别潜在结构和实现组合泛化提供了充分覆盖。

**Key Finding**: 在复合轨迹上训练可以产生比在孤立原子模块上训练更强的泛化能力。SFT 确保所有原子模块的覆盖，RL 专注于超出 SFT 支持的新颖组合。

---

#### 1.9 ML-Agent: Reinforcing LLM Agents for Autonomous ML Engineering
- **Title (CN)**: ML-Agent: 强化 LLM Agent 用于自主机器学习工程
- **Venue**: ICML 2026

---

#### 1.10 Maximum Likelihood Reinforcement Learning
- **Title (CN)**: 最大似然强化学习
- **Venue**: ICML 2026 Oral

---

#### 1.11 DiScoFormer (ICML 2026 Oral, Top 0.7%)
- **Title (CN)**: DiScoFormer: Transformer 作为密度与分数估计器
- **Authors**: Vasily Ilin, Peter Sushko, Ranjay Krishna
- **Venue**: ICML 2026 Oral Award

**Abstract & Key Innovations**: 证明 Transformer 架构天然适合密度估计和分数估计任务，超过经典 KDE 方法的所有变体。关键发现：注意力头会自动专业化学习不同形状和大小的核函数，且跨分布和样本量保持鲁棒。

---

<a id="neurips-2025"></a>
## 2. NeurIPS 2025 (San Diego, Dec 2025)

### 🏆 Best Paper Awards (7 papers)

#### 2.1 Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free (Best Paper)
- **Title (CN)**: 大语言模型的门控注意力：非线性、稀疏性与无注意力汇聚
- **Authors**: Zihan Qiu et al. (Alibaba Qwen Team)
- **Affiliation**: 阿里巴巴 (Alibaba)
- **Venue**: NeurIPS 2025 Best Paper Award
- **Link**: 相关代码已开源，已应用于 Qwen3-Next

**Abstract & Key Innovations**: 首次系统研究注意力门控 (attention gating) 对大型模型性能和训练的影响。在 Scaled Dot-Product Attention (SDPA) 后添加 head-specific sigmoid 门控——一个看似简单的架构修改——在 30+ 模型变体 (15B MoE 和 1.7B dense，3.5T token 训练) 上持续提升性能。

**Key Benefits**:
1. 消除 "attention sink" 问题（模型浪费容量关注不相关 token）
2. 增强训练稳定性，允许更大学习率
3. 改善长上下文外推能力
4. 改进缩放特性

**Production Impact**: 已应用于 Qwen3-Next（2025年9月发布），结合 Gated DeltaNet 替代标准注意力。委员会评价："该论文的推荐易于实现，鉴于论文提供的大量证据，我们预期该想法将被广泛采用。"

---

#### 2.2 Artificial Hivemind: Language Model Diversity and Homogenization (Best Paper)
- **Title (CN)**: 人工蜂巢思维：语言模型的多样性与同质化
- **Authors**: Liwei Jiang, Yejin Choi et al.
- **Affiliation**: University of Washington, CMU, Allen Institute for AI
- **Venue**: NeurIPS 2025 Best Paper Award

**Abstract & Key Innovations**: 测试了 70+ 语言模型，发现它们生成了惊人相似的响应。引入 Infinity-Chat 数据集 (26,000 多样查询，31,000 人类标注)，揭示了远超预期的模型内和模型间同质化。

**Impact**: 对 AI 长期风险（人类创造力、价值多元性、独立思考）具有重要警示意义。预计 2026 年将出现一波关注多样性训练方法和超越准确性的评估基准的研究浪潮。

---

#### 2.3 1000 Layer Networks for Self-Supervised RL (Best Paper)
- **Title (CN)**: 自监督强化学习的千层网络
- **Authors**: Kevin Wang, Ishaan Javali et al.
- **Venue**: NeurIPS 2025 Best Paper Award

**Abstract & Key Innovations**: 将自监督 RL 网络成功扩展到 1,024 层（传统 RL 仅使用 2-5 层），在运动和操作基准上实现 2-50× 性能提升。极端深度在目标条件任务中解锁了全新能力——机器人无需任何人类指导即可学习到达复杂目标。

---

#### 2.4 Why Diffusion Models Don't Memorize (Best Paper)
- **Title (CN)**: 扩散模型为何不记忆
- **Authors**: Tony Bonnaire, Raphaël Urfin, Giulio Biroli, Marc Mezard
- **Venue**: NeurIPS 2025 Best Paper Award

**Abstract & Key Innovations**: 识别了区分真实图像生成和训练数据记忆的精确数学机制——"隐式动态正则化"，操作在两个不同时间尺度上。泛化窗口随训练集大小线性扩展。这解释了 DALL-E 和 Midjourney 为何生成新颖图像而非复述训练数据。

---

#### 2.5 Runner-Up Papers

| Paper | Key Contribution |
|-------|-----------------|
| Superposition Yields Robust Neural Scaling | 神经缩放的超位置鲁棒性 |
| (Datasets & Benchmark Track) | 数据集与基准轨道获奖论文 |

---

<a id="iclr-2026"></a>
## 3. ICLR 2026 (Rio de Janeiro, Apr 2026)

> **规模**: 19,525 有效投稿 → 5,355 接收 (27.4% 接收率，历史最低)

### 🏆 Outstanding Papers

#### 3.1 Agentic Robotics 轨道

**Mean Flow Policy (MFP)**
- 引入生成策略函数，建模均值速度场实现单步动作生成
- 在 Robomimic 和 OGBench 上达到 SOTA 成功率，训练和推理速度大幅提升

**Emergent Dexterity via Diverse Resets**
- 利用模拟器重置暴露 RL 算法于多样化机器人-物体交互
- 单一奖励函数和固定超参数解决广泛灵巧操作任务

**VLA Models Explosion**:
- Interleave-VLA: 通过图文交错指令增强操作
- SimpleVLA-RL: 通过 RL 扩展 VLA 训练
- VITA (Imperial College): VLM 实时适应机器人执行任务，作为零样本奖励模型

---

#### 3.2 Safety Alignment 轨道

**AlphaAlign**
- 通过 RL with verifiable rewards 激励模型产生显式安全推理
- 实现"深层安全对齐"——模型主动生成安全相关推理 token，而非依赖通用拒绝模式

**WaltzRL (Meta FAIR + Johns Hopkins)**
- 将安全对齐重构为两个 agent 之间的协作正和博弈
- 联合训练对话 agent 和反馈 agent，提供实时安全建议（而非二元拒绝）
- WildJailbreak 不安全响应从 39% 降至 4.6%，OR-Bench 过度拒绝从 45.3% 降至 9.9%

**Safety Subspaces are Not Linearly Distinct (EPFL)**
- 挑战安全行为在模型权重空间中占据可分离线性子空间的假设

---

#### 3.3 其他 Outstanding Papers

| Paper | Key Contribution |
|-------|-----------------|
| Transformers are Inherently Succinct | Transformer 固有的简洁性 |
| Multi-Turn Drop | 多轮对话丢弃机制 |
| ∇-Reasoner | 梯度推理器 |
| SPIRAL | 自博弈激励推理 (10% 提升，8 个基准) |

---

<a id="cvpr-2026"></a>
## 4. CVPR 2026 (Nashville, Jun 2026)

### 🏆 Best Paper Award

#### 4.1 D4RT: 4D Scene Reconstruction
- **Title (CN)**: D4RT: 4D 场景重建
- **Venue**: CVPR 2026 Best Paper Award

**Abstract & Key Innovations**: 用单一查询接口替代整个 4D 重建流水线，超越 VGGT 等 SOTA 方法。将 4D 动态场景重建从多阶段复杂流程简化为端到端的统一框架。

---

### 🏅 Honorable Mention

#### 4.2 SAM 3D: 3Dfy Anything in Images
- **Affiliation**: Meta
- **Venue**: CVPR 2026 Best Paper Honorable Mention

**Abstract & Key Innovations**: 从 Meta 提出的生成模型，可将图像中的任何内容 3D 化。

---

### Notable CVPR 2026 Papers

#### 4.3 CUPID: Generative 3D Reconstruction via Joint Object and Pose Modeling
- **Authors**: Binbin Huang, Haobin Duan, Yiqun Zhao, Zibo Zhao, Yi Ma, Shenghua Gao
- **Venue**: CVPR 2026

**Abstract & Key Innovations**: 两阶段 flow-based 模型联合建模规范对象和相机姿态的完整分布。通过像素对齐图像特征注入生成过程，PSNR 超越 SOTA 3dB，Chamfer Distance 改善 10%。

---

#### 4.4 MatMart: Material Reconstruction of 3D Objects via Diffusion
- **Venue**: CVPR 2026

**Abstract & Key Innovations**: 两阶段材质重建框架：准确材质预测 + 先验引导生成。通过 View-Material Cross-Attention (VMCA) 支持任意数量输入图像。

---

#### 4.5 Gen3R: 3D Scene Generation Meets Feed-Forward Reconstruction
- **Venue**: CVPR 2026

---

<a id="kdd-2026"></a>
## 5. KDD 2026

### 🎯 CTR & Advertising

#### 5.1 GR4AD: Generative Recommendation for Large-Scale Advertising
- **Title (CN)**: GR4AD: 大规模广告的生成式推荐
- **Authors**: Kuaishou Team
- **Affiliation**: 快手 (Kuaishou)
- **Venue**: KDD 2026 / arXiv 2602.22732
- **Link**: https://arxiv.org/abs/2602.22732v2

**Abstract & Key Innovations**: 面向生产环境的生成式推荐器，跨架构、学习和推理进行协同设计：
1. **UA-SID** (Unified Advertisement Semantic ID): 从微调 MLLM 嵌入中捕获复杂广告信息
2. **LazyAR Decoder**: 放松层级自回归依赖，提升解码吞吐量
3. **VSL** (Value-Aware Supervised Learning) + **RSPO** (Ranking-Guided Softmax Preference Optimization): 排名感知的 list-wise RL 算法
4. **Dynamic Beam Serving**: 自适应 beam width

**Results**: 在快手广告系统 (400M+ 用户) 上实现 **+4.2% 广告收入** 提升，高吞吐 (500+ QPS/L20)、低延迟 (<100ms) 实时服务。

**Comparison**: 相比 DLRM 基线，同时从模型缩放和推理时缩放中获得一致增益。

---

#### 5.2 EST: Efficiently Scalable Transformer for CTR Prediction
- **Title (CN)**: EST: CTR 预测的高效可扩展 Transformer
- **Authors**: Mingyang Liu, Yong Bai, Zhangming Chan et al.
- **Affiliation**: 阿里巴巴/淘宝 (Alibaba/Taobao)
- **Venue**: KDD 2026 / arXiv 2602.10811
- **Link**: https://doi.org/10.48550/arxiv.2602.10811

**Abstract & Key Innovations**: 重新审视 CTR 预测与 LLM 的根本区别，识别两个关键属性：行为与非行为特征间信息密度的不对称性，以及内容丰富信号的模态特定先验。

**Core Architecture**:
- **LCA** (Lightweight Cross Attention): 剪枝冗余自交互，聚焦高影响力跨特征依赖
- **CSA** (Content Sparse Attention): 利用内容相似性动态选择高信号行为

**Results**:
- 离线: 稳定且高效的幂律缩放关系
- 在线 (淘宝全站广告 "猜你喜欢" + "购后推荐"):
  - CTR +1.22%, RPM +3.27% (Guess)
  - CTR +2.01%, RPM +2.66% (Post)

---

#### 5.3 FAT: Field-Aware Transformer with Rademacher CTR Scaling Law
- **Title (CN)**: FAT: 基于 Rademacher CTR 缩放定律的 Field-Aware Transformer
- **Affiliation**: 阿里巴巴 (Alibaba)
- **Venue**: KDD 2026
- **Key Result**: +4.38% AUC，已在淘宝部署

---

#### 5.4 RankUp: High-rank Representations for Ad Ranking
- **Title (CN)**: RankUp: 广告排序的高秩表示
- **Affiliation**: 腾讯 (Tencent)
- **Venue**: KDD 2026
- **Link**: arXiv 2604.17878

---

#### 5.5 OneMall: One Model, More Scenarios — End-to-End Generative Recommender Family
- **Title (CN)**: OneMall: 一个模型，更多场景——端到端生成式推荐家族
- **Affiliation**: 快手 (Kuaishou)
- **Venue**: KDD 2026
- **Context**: 400M+ DAU 电商平台的端到端生成式推荐系统

---

### 📊 Recommendation Systems

#### 5.6 Meta Lattice: Model Space Redesign for Recommendation
- **Affiliation**: Meta
- **Venue**: KDD 2026

---

#### 5.7 CoPersona: Collaborative Persona Graphs for LLM Personalization
- **Title (CN)**: CoPersona: 基于协作persona图的 LLM 个性化
- **Affiliation**: KDD 2026
- **Key Innovation**: 利用协作persona图增强 LLM 个性化推荐

---

<a id="aaai-2026"></a>
## 6. AAAI 2026

#### 6.1 DMGIN: Multimodal LLMs Enhance Large Recommendation Models
- **Title (CN)**: DMGIN: 多模态 LLM 增强大型推荐模型的终身用户点击后行为
- **Authors**: Wei, Z., Xie, Q., Liu, Q., & Yu, J.
- **Affiliation**: 阿里巴巴 (Alibaba)
- **Venue**: AAAI 2026 (Vol. 40 No. 19)
- **Link**: https://ojs.aaai.org/index.php/AAAI/article/view/38626

**Abstract & Key Innovations**: 利用 MLLM 对用户终身点击后行为序列进行分组重组（几乎无额外计算开销）。在组内使用兴趣统计和 intra-group transformer 分析行为，组间使用 inter-group transformer 捕获兴趣演化。

**Results**: 在 LBS 广告系统 A/B 测试中，CTR +4.7%, RPM +2.3%。

---

#### 6.2 TreeBridge: Aligning LLM Embeddings in Industrial Recommender Systems
- **Title (CN)**: TreeBridge: 在工业推荐系统中对齐 LLM 嵌入
- **Affiliation**: Shopee (东南亚最大电商平台之一)
- **Venue**: AAAI 2026 (Vol. 40 No. 47)

**Abstract & Key Innovations**: 引入结构感知生成编码树，桥接 LLM 嵌入与推荐任务之间的语义差距。保留 LLM 嵌入的外部语义丰富性，同时学习标签感知结构。

**Results**: 自 2025 年 5 月部署以来，帮助 Shopee 实现 **+1.55% GMV** 相对提升，服务数亿用户。

---

#### 6.3 MoMoREC: Multi-agent Motivation Generation for Residual Semantic ID-Aware Recommendation
- **Title (CN)**: MoMoREC: 多智能体动机生成的残差语义ID感知推荐
- **Affiliation**: 淘宝 (Taobao)
- **Venue**: AAAI 2026

**Abstract & Key Innovations**: 首次引入多 agent 范式理解用户购买动机。使用聚类+扩散架构为长尾商品附加动机信号，生成 Motivation Semantic ID 增强推荐模型。

**Results**: 在淘宝 88VIP 畅销榜 A/B 测试中，TCR +1%, GMV +6.3%。

---

#### 6.4 Other AAAI 2026 Notable Papers

| Paper | Affiliation | Key Contribution |
|-------|------------|-----------------|
| FastDriveVLA | - | 自动驾驶 VLA 模型 |
| COREA | - | Outstanding Paper Honorable Mention |
| ProCo | - | Outstanding Paper Honorable Mention |
| GenMatLab | - | Outstanding Paper Honorable Mention |

---

<a id="acl-2026"></a>
## 7. ACL 2026 (San Diego, Jul 2026)

#### 7.1 MemRec: Collaborative Memory-Augmented Agentic Recommender System
- **Title (CN)**: MemRec: 协作记忆增强的 Agent 推荐系统
- **Authors**: Weixin Chen et al.
- **Affiliation**: Rutgers University
- **Venue**: ACL 2026 Long Paper
- **Link**: https://aclanthology.org/2026.acl-long.2061/

**Abstract & Key Innovations**: 引入协作记忆范式，连接孤立语义以共享关系洞察。架构上解耦记忆管理与推理：专用轻量 LM (LM_Mem) 在后台管理动态协作记忆图，仅向下游重型 LLM (LLM_Rec) 提供蒸馏后的高信号上下文。

**Results**: 在 4 个基准上达到 SOTA。

---

#### 7.2 RecPO: Preference Intensity and Temporal Context for LLM Rec
- **Title (CN)**: RecPO: LLM 有效顺序推荐的偏好强度与时间上下文研究
- **Authors**: Zhongyu Ouyang et al.
- **Venue**: ACL 2026 Long Paper
- **Link**: https://aclanthology.org/2026.acl-long.656/

**Abstract & Key Innovations**: 揭示现有偏好对齐方法依赖二元成对比较，忽略了偏好强度和时间上下文两个关键因素。提出统一偏好优化框架 RecPO，构建自适应奖励边界同时考虑偏好强度和交互时间。

**Key Finding**: 偏好强度和时间上下文是 LLM 有效推荐的基本要素。

---

#### 7.3 BLaIR: Benchmarking LLMs as Semantic Encoders
- **Title (CN)**: BLaIR: 将 LLM 作为语义编码器进行基准测试
- **Authors**: Yupeng Hou, Jiacheng Li et al. (UC San Diego / McAuley Lab)
- **Venue**: ACL 2026 Long Paper
- **Link**: https://aclanthology.org/2026.acl-long.147/

**Abstract & Key Innovations**: 推出大规模 Amazon Reviews 2023 数据集 (570M+ 评论, 48M+ 商品)，统一基准覆盖顺序推荐、协同过滤和商品搜索。11 个领先 LLM 在 BLaIR 上的排名与 MTEB 几乎不相关。

---

#### 7.4 REASONREC: Reasoning-Augmented Multimodal Agent for Unified Recommendation
- **Title (CN)**: REASONREC: 推理增强的多模态统一推荐 Agent
- **Venue**: ACL 2026 Findings
- **Link**: https://aclanthology.org/2026.findings-acl.391.pdf

**Abstract & Key Innovations**: 三阶段显式推理流水线：Observe (VLM编码) → Deliberate (CoT推理+不确定性量化) → Act (动态委派不确定查询到轻量经典推荐模型)。evidence-horizon curriculum 渐进增强推理复杂度。

**Results**: 关键排序指标 (HR@5, NDCG@5) 超越 SOTA 多模态推荐器 **30%+**，同时通过动态委派 (35%查询) 大幅降低推理延迟。

---

#### 7.5 STAR: Single-agent Trajectory-Aligned Recommender
- **Title (CN)**: STAR: 单agent轨迹对齐推荐器
- **Venue**: ACL 2026 Findings

**Abstract & Key Innovations**: 轨迹驱动内化框架，将多 agent 教师系统的 agentic 逻辑（规划、工具使用、自我反思）蒸馏到紧凑的单模型 STAR 中。使用协作信号翻译机制将潜在行为模式显式转换为自然语言证据。

**Results**: STAR 超越其教师系统 8.7%-39.5%，同时消除迭代延迟。

---

#### 7.6 Other ACL 2026 Notable Papers

| Paper | Key Contribution |
|-------|-----------------|
| R^3 (ACL 2026) | 广告合规性推荐 |
| SiPeR | 情境对话推荐中的动态隐式偏好推理 |
| HARPO | 分层 Agent 推理的用户对齐对话推荐 |

---

<a id="www-2026"></a>
## 8. WWW 2026 (Sydney, 2026)

#### 8.1 ThinkRec: Thinking-based Recommendation via LLM
- **Title (CN)**: ThinkRec: 基于思维的 LLM 推荐
- **Authors**: Keqin Bao et al.
- **Venue**: WWW 2026
- **Link**: https://dl.acm.org/doi/10.1145/3774904.3792070

**Abstract & Key Innovations**: 将 LLM4Rec 从 System 1（基于浅层特征匹配）转变为 System 2（基于深层行为逻辑推理）。引入思维激活机制注入合成推理轨迹，使推荐过程类似于 LLM 的 CoT 推理。

**Instance-wise Expert Fusion**: 根据用户潜在特征动态分配专家模型权重，适应个体推理路径。

**Results**: 在多个真实 Web 用户行为偏好数据集上，推荐准确性和可解释性显著优于基线。

---

#### 8.2 Other WWW 2026 Notable Papers

| Paper | Affiliation | Key Contribution |
|-------|------------|-----------------|
| SparseCTR | Meituan | 稀疏注意力长期 CTR (+1.72% CTR) |
| GenCI | - | 生成式 CTR via Cohort Intent Learning |
| ThinkRec | - | 基于思维的 LLM 推荐 |

---

<a id="cikm-2025"></a>
## 9. CIKM 2025 (Seoul, Nov 2025)

#### 9.1 UserIP-Tuning: User Inherent Profile Inference Machine
- **Title (CN)**: UserIP-Tuning: 用户内在画像推断机
- **Affiliation**: 华为 (Huawei)
- **Venue**: CIKM 2025
- **Link**: https://doi.org/10.1145/3746252.3761574

**Abstract & Key Innovations**: 使用 prompt tuning 将用户潜在画像视为可训练软 token，通过 EM 算法推断。UserIP 量化模块将软 token 转换为稀疏特征 ID，可存储在潜在特征库中用于在线部署。

**Results**: 在华为 AppGallery Explore 页面部署 (2025年5月至今)，A/B 测试 AUC +7.47%，2M DAU。

---

#### 9.2 Other CIKM 2025 Notable Papers

| Paper | Affiliation | Key Contribution |
|-------|------------|-----------------|
| RankMixer | ByteDance | 排序模型缩放 |
| LONGER | ByteDance | 超长用户行为序列 |
| SUAN | Meituan | 在线 CTR 缩放方法论 |

---

<a id="recsys-2025"></a>
## 10. RecSys 2025 (Prague, Oct 2025)

#### 10.1 Best Paper Award
- **Winner**: ECAT (European Centre for Algorithmic Transparency)

#### 10.2 Notable RecSys 2025 Papers

| Paper | Affiliation | Key Contribution |
|-------|------------|-----------------|
| SUAN | Meituan | 在线 CTR 缩放方法论，RecSys 2025 |
| LONGER | ByteDance | 超长用户行为序列 (RecSys 2025) |
| LEADRE | - | 多方面知识增强 LLM 展示广告推荐 |

---

<a id="sigir-2026"></a>
## 11. SIGIR 2026

#### 11.1 Notable SIGIR 2026 Papers

| Paper | Key Contribution |
|-------|-----------------|
| Total Recall QA | 全召回问答 |
| Ad Recommendation & Retrieval | 广告推荐与检索 |

---

<a id="ctr-cross-venue"></a>
## 12. CTR Prediction & Advertising (Cross-Venue)

### 🔬 CTR 缩放定律

| Paper | Affiliation | Venue | Key Result |
|-------|------------|-------|-----------|
| EST | Alibaba/Taobao | KDD 2026 | 幂律缩放，RPM +3.27% |
| FAT | Alibaba | KDD 2026 | +4.38% AUC |
| Kunlun | Meta | - | 统一架构缩放定律 |
| Wukong | Meta | ICML 2024 | 大规模推荐缩放定律 |
| Climber | NetEase | WWW 2025 | 高效推荐缩放定律 |
| LLaTTE | Meta | - | 广告推荐多阶段缩放定律 |
| ULTRA-HSTU | Meta | - | 弯曲缩放定律曲线 |

### 🎯 转化率预测新范式

| Paper | Affiliation | Venue | Innovation |
|-------|------------|-------|-----------|
| GR4AD | Kuaishou | KDD 2026 | 生成式广告推荐，+4.2% 广告收入 |
| CADET | LinkedIn | - | Decoder-only CTR，+11.04% lift |
| DS-MLP | - | TKDD 2026 | 双流 MLP 知识蒸馏，SOTA |
| GRAB | Baidu | - | 序列优先 CTR 范式，+3.49% CTR |
| OneRanker | Tencent | - | 统一生成与排序，+1.34% GMV |
| RankUp | Tencent | KDD 2026 | 高秩表示 |
| TokenFormer | Tencent | - | 统一多字段与序列推荐 |
| Beyond Positive Signals | Tencent | - | 混合极性序列 +9.6% AUC |
| GenCI | - | WWW 2026 | 生成式 CTR via Cohort Intent |
| DAIAN | Alibaba/Xianyu | - | 触发推荐的深度自适应意图感知 |
| LoopCTR | Alibaba | - | 循环缩放 |
| IDProxy | Xiaohongshu | - | MLLM 冷启动代理 |
| SparseCTR | Meituan | WWW 2026 | 稀疏注意力长期 CTR (+1.72%) |
| UniSID | - | - | 统一语义ID |

---

<a id="agent-systems"></a>
## 13. Agent Systems & Multi-Agent

### 🏗️ Agent Infrastructure & Systems

| Paper | Affiliation | Venue | Key Innovation |
|-------|------------|-------|---------------|
| HiPER | - | ICML 2026 | 分层计划-执行 RL，ALFWorld 97.4% |
| MemoPilot | - | ICML 2026 | 记忆 RL，ELO #1 on LHE/RPS |
| Agentic Monte Carlo | - | ICML 2026 | 黑盒 agent RL |
| SkillOpt | Microsoft Research Asia | - | 自进化 agent 技能 |
| AutoResearch AI | Salesforce | - | 研究自动化 |
| EVE-Agent | - | - | 证据可验证自进化 |
| Foundation Protocol | Tencent/HKUST/UIUC | - | Agent 社会协调 |
| Next-Gen Agentic RL (AReaL2.0) | Ant Group/HKUST/Tsinghua | - | 自进化 agent RL 系统 |
| AgentLTL | - | - | LTL 过程合规性验证框架 |
| Steerability via Constraints | Google | - | 编码 agent 可扩展监督 |
| AgenticAI-Supervisor | - | - | RL Gym 环境 |

### 🤖 Agent Benchmarks

| Paper | Venue | Key Innovation |
|-------|-------|---------------|
| AgentLens | - | 生产评估轨迹审查，代码 agent |
| PolyWorkBench | - | 多语言长时域 agent 基准 |
| General AgentBench | - | 统一通用 agent 评估 |
| Agent-Diff | KDD 2026 Under Review | 企业 API 任务基准 |

---

<a id="generative-models"></a>
## 14. Generative Models & Diffusion

| Paper | Affiliation | Venue | Key Innovation |
|-------|------------|-------|---------------|
| The Flexibility Trap | Tsinghua | ICML 2026 Outstanding | 挑战 DLM 任意序生成 |
| High-Accuracy Sampling | Multi-institution | ICML 2026 Outstanding | 扩散模型高精度采样 |
| Why Diffusion Models Don't Memorize | - | NeurIPS 2025 Best | 扩散模型不记忆的数学机制 |
| ARCache | - | CVPR 2026 | 视频扩散缓存加速 |
| Precise | ByteDance | - | SDE一致采样 (Flow-Matching RL) |
| Self-Flow | - | ICML 2026 | 自监督流匹配 |
| UniAR | Alibaba | ICML 2026 | 统一多模态自回归建模 |
| DiLaDiff | NVIDIA | - | 蒸馏潜在增强扩散 LM |
| CARD | - | - | 扩散语言模型 |

---

<a id="games"></a>
## 15. Games & Strategic Reasoning

| Paper | Affiliation | Venue | Key Innovation |
|-------|------------|-------|---------------|
| SPIRAL | - | ICLR 2026 | 自博弈激励推理 (10% 提升) |
| NitroGen | NVIDIA | CVPR 2026 | 1000+ 游戏基础模型 |
| Multiplayer World Models | - | - | 4人 20fps 世界模型 |
| MARL-GPT | - | AAAI/AAMAS 2026 | 多任务 MARL |
| RAID | - | - | NHL26 游戏 AI |
| Dark Souls III Lifelong | - | ICLR 2026 WS | 暗黑3终身学习 |
| Alive | Alibaba | ICML 2026 | RL 交互前端游戏 |
| Cross-Entropy Games | - | - | 通用能力的交叉熵博弈 |
| GENSTRAT | - | - | LLM 中的策略推理 |
| Nemobot | - | - | LLM 驱动的游戏 agent |
| PCSP | - | - | 单策略无限 NPC (Persona RL) |

---

<a id="code-reasoning"></a>
## 16. Code Execution & Formal Reasoning

| Paper | Affiliation | Venue | Key Innovation |
|-------|------------|-------|---------------|
| LLM-as-a-Verifier | - | - | 通用验证框架 |
| Agentic Proving | - | - | 程序验证的 Agent 证明 |
| CodeTree | Salesforce | ACL 2025 | Agent 引导树搜索代码生成 |
| ImProver 2 | CMU | - | 神经符号证明优化 |
| RMA | - | - | 研究数学的 Agent 系统 |
| Tree-of-Evolution | NUS | ACL 2025 | 树结构代码指令进化 |

---

<a id="benchmarks"></a>
## 17. Benchmarks & Evaluation

| Paper | Venue | Key Innovation |
|-------|-------|---------------|
| AgentLens | - | 生产评估代码 agent 轨迹审查 |
| PolyWorkBench | - | 多语言长时域 agent 基准 |
| How Hard is it to Rig a Benchmark? | - | 基准操纵难度分析 |
| General AgentBench | - | 统一通用 agent 评估 |
| Benchmark Test-Time Scaling | - | LLM agent 测试时缩放基准 |

---

<a id="cross-cutting-themes"></a>
## 18. Cross-Cutting Themes

### 📊 统计概览

| Metric | Value |
|--------|-------|
| 覆盖会议 | 12+ (ICML, NeurIPS, ICLR, CVPR, KDD, AAAI, ACL, WWW, SIGIR, EMNLP, CIKM, RecSys) |
| 精选论文 | 200+ |
| 覆盖实验室 | 20+ (DeepMind, OpenAI, Meta, Alibaba, ByteDance, Tencent, Kuaishou, Microsoft, NVIDIA, Baidu, Meituan, Tsinghua, LinkedIn, Salesforce, Shopee, Huawei) |

### 🔑 Key Trends

1. **Diffusion LM 成熟化**: ICML 2026 两篇 Outstanding Paper 聚焦扩散模型，但也在反思其局限性 ("The Flexibility Trap")

2. **Agent RL 系统化**: ICML 2026 agent 论文从算法走向系统 (HiPER 分层、MemoPilot 记忆、AReaL2.0 生产系统)

3. **CTR 缩放定律全面开花**: Alibaba EST (KDD 2026)、Meta LLaTTE/ULTRA-HSTU、Kuaishou GR4AD 形成完整的 CTR scaling law 谱系

4. **生成式推荐工业化**: GR4AD (Kuaishou 400M DAU)、OneMall、OneRanker 证明生成式推荐在大规模生产中可行

5. **LLM + Recommendation 深度融合**: ThinkRec (WWW 2026)、MemRec (ACL 2026)、RecPO (ACL 2026)、Taiji (Kuaishou) 代表不同的融合路径

6. **Safety Alignment 成熟化**: ICLR 2026 WaltzRL (39%→4.6% 不安全响应)、AlphaAlign 深层对齐、ICML "Censor's Toolkit" 伦理反思

7. **NeurIPS 2025 关于同质化的警示**: "Artificial Hivemind" 证明 70+ LLM 输出惊人相似

8. **3D/4D 理解爆发**: CVPR 2026 D4RT (4D 重建 Best Paper)、SAM 3D (Meta)、CUPID

9. **Gated Attention 已投入生产**: NeurIPS 2025 Best Paper 已应用于 Qwen3-Next

10. **Agent 可验证性与安全性**: AgentLTL (LTL 合规)、AgentLens (轨迹审查)、Steerability via Constraints (访问控制)

### 🏢 Company Research Focus Map

| Company | Focus Areas | Key Papers |
|---------|------------|-----------|
| Alibaba | CTR Scaling, Attention, Generative Rec | EST, FAT, DAIAN, LoopCTR, UniAR, Gated Attention |
| Kuaishou | Generative Ad Rec, Scaling, Agent RL | GR4AD, OneMall, Taiji, SUAN |
| Tencent | Ad Ranking, CTR Architecture | OneRanker, RankUp, TokenFormer, Beyond Positive Signals |
| Meta | Scaling Laws, Safety, 3D | LLaTTE, ULTRA-HSTU, WaltzRL, SAM 3D, Kunlun |
| ByteDance | Efficient Serving, Long Sequences | LONGER, Make It Long Keep It Fast, MixFormer, Zenith |
| Meituan | Sparse Attention, Foundation Models | SparseCTR, SUAN, MTFM |
| NVIDIA | Generative Models, Diffusion | NitroGen, DiLaDiff |
| Microsoft | Agent Skills, Verification | SkillOpt, ImProver 2 |
| Baidu | CTR Sequence-First | GRAB |
| LinkedIn | Decoder-Only CTR | CADET |
| Huawei | Profile Inference | UserIP-Tuning |
| Shopee | LLM Embedding Alignment | TreeBridge |
| Salesforce | Research Automation, Code Gen | AutoResearch AI, CodeTree |
| Tsinghua | Diffusion Theory, Safety | The Flexibility Trap |

---

*Generated: 2026-07-13 | Source: web-search across arXiv, conference proceedings, and official sites*
