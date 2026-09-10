---
title: "arXiv AI Search Report"
type: synthesis
created: 2026-09-10
updated: 2026-09-10
sources: []
tags: [arxiv, ai, llm, recommendation, ctr, sequential-modeling, game-ai, advertising]
---

# arXiv AI 搜索报告 — 2026-09-10

> 本报告覆盖近期（2026年8月下旬–9月上旬）arXiv 上 AI、LLM、推荐系统、广告/CTR、序列建模、Game AI 等方向的重要论文，每篇提供标题、作者、机构、摘要、核心创新点及 arXiv 链接。

---

## 1. LLM 核心机制与理论

### 1.1 Evidence Integration in Large Language Models

| 项目 | 详情 |
|------|------|
| **标题** | Evidence Integration in Large Language Models |
| **作者** | Sebastien Kawada, Manolis Kellis |
| **机构** | MIT |
| **链接** | https://arxiv.org/abs/2609.04290 |
| **日期** | 2026-09-03 |

**摘要：** 提出一个分布理论解释 LLM 如何将外部证据整合到已有决策中。发现三个关键预测：(1) 接收者更可能的候选答案更有说服力；(2) 接收者更容易整合自身特征错误而非外部错误；(3) 相同证据可能改善弱模型但损害强模型。在 1000 万次试验、12 个 LLM、8 个领域上验证了这些发现。因果干预表明证据整合发生在网络后层，形成一个结构化的接纳→提升→传输序列。

**核心创新：**
- 首次提出 LLM 证据整合的分布理论
- 揭示验证表征与证据整合在因果上完全解耦
- 发现 LLM 在内部验证无效后仍会整合候选答案（93-100%）

---

### 1.2 The Geometry of Ignorance: LLMs Know When to Temper Bayesian Priors

| 项目 | 详情 |
|------|------|
| **标题** | The Geometry of Ignorance: LLMs Know When to Temper Bayesian Priors |
| **作者** | (arXiv 未列出完整作者) |
| **机构** | 未明确标注 |
| **链接** | https://arxiv.org/abs/2609.02959 |
| **日期** | 2026-09-02 |

**摘要：** 发现 unembedding 矩阵中存在一个"无知方向"，编码了训练语料的 unigram 分布，即模型在不确定时回退的贝叶斯先验。该结构在 Llama、Qwen、Gemma、Pythia 四个模型族（0.4B–405B 参数）中均存在。将最终预测状态投影到该方向可得到逐 token 先验加载因子 λ，随上下文信息量增加而递减，形式上分解为 temperated Bayesian update 的两个因子。

**核心创新：**
- 发现 unembedding 几何中的"无知方向"
- 将贝叶斯推理与 LLM 内部表征直接对应
- 因果验证：调节 λ 可操控预测偏离/接近先验

---

### 1.3 When Do Internal Probes Beat Reading the Answer?

| 项目 | 详情 |
|------|------|
| **标题** | When Do Internal Probes Beat Reading the Answer? Miscalibrated Readouts and Behavior-Concealed Knowledge in Language Models |
| **作者** | (arXiv 未列出完整作者) |
| **机构** | 未明确标注 |
| **链接** | https://arxiv.org/abs/2609.04582 |
| **日期** | 2026-09-04 |

**摘要：** 在一个 0.6B 模型上验证 1200 个逻辑结论时，模型行为上每次都回答 YES（50% 准确率），但线性探针在隐藏状态上读出正确判断的 AUC 达 0.96。诊断发现主导失败源于单一标量——决策阈值偏移 +4.6σ。跨 90 种语义配置、5 个模型、3 个模型族的实验表明，行为准确率坍缩为阈值偏移的单一函数（Spearman -0.93）。一个参数校正可将行为从 50% 修复至 81%。

**核心创新：**
- 揭示 LLM 内部知识与行为输出的系统性脱节
- 发现单一标量阈值偏移是行为坍缩的根本原因
- 提出分离 concealed、miscalibrated、undetected 三种知识状态的诊断框架

---

### 1.4 Legibility is Not Interpretability

| 项目 | 详情 |
|------|------|
| **标题** | Legibility is Not Interpretability: Comparing Judged and Actual Importance in Chain-Of-Thought Reasoning |
| **作者** | (COLM 2026) |
| **机构** | 未明确标注 |
| **链接** | https://arxiv.org/abs/2609.04194 |
| **日期** | 2026-09-03 |

**摘要：** 将推理步骤重要性操作化为"优势"（包含/排除该步骤的期望奖励变化），通过 Monte Carlo rollout 估计。发现 LLM 评审能优于随机基线但远低于噪声上限。微调模型作为步骤级评论者在错误回答上表现良好，但在正确回答上仍远离上限，表明步骤重要性仅部分可从推理文本中恢复。

**核心创新：**
- 区分"可读性"与"可解释性"，为 CoT 忠实性研究提供定量框架
- 证明推理 trace 文本仅部分编码了步骤功能角色信息

---

### 1.5 Do Large Language Models Capture the Diversity in their Training Data?

| 项目 | 详情 |
|------|------|
| **标题** | Do Large Language Models Capture the Diversity in their Training Data? |
| **作者** | (arXiv 未列出完整作者) |
| **机构** | 未明确标注 |
| **链接** | https://arxiv.org/abs/2609.02275 |
| **日期** | 2026-09-02 |

**摘要：** 通过条件熵比较模型生成输出与训练数据的多样性。在 OLMo、Pythia、GPT-Neo 等模型上一致发现，模型生成输出的条件熵系统性低于训练数据，即存在"条件多样性缺口"。提出基于矩阵熵的后验修正机制，证明凸优化可通过重加权采样恢复多样性。

**核心创新：**
- 发现现代生成模型系统性欠采样训练数据多样性
- 提出信息论框架量化和修复条件多样性缺口

---

## 2. 推荐系统与工业落地

### 2.1 ReST: Scaling Sequence Transformers for Industrial Recommendation Ranking

| 项目 | 详情 |
|------|------|
| **标题** | From Language to Behavior: Scaling Sequence Transformers for Industrial Recommendation Ranking with Rec-Native Designs |
| **作者** | Jie Chen, Xiangqian Yu, Yanchao Lian, Tan Lu, Run Yang, Zhengchun Shang, Xing Wang, Cheng Chen, Ke Hu, Qiang Li, Tianjiu Yin, Xiaobing Liu |
| **机构** | 未明确标注（工业界） |
| **链接** | https://arxiv.org/abs/2609.01240 |
| **日期** | 2026-09-01 |

**摘要：** 提出 ReST（Recommendation-native Transformer scaling framework），针对推荐场景与语言建模的差异进行原生设计。引入 dual-gated attention、rotary positional and temporal embedding、stabilized residual normalization。将 ranking 分解为 heavy reusable encoder + lightweight cross decoder，实现 compute-once, decode-many-times。在线 A/B 测试中 AUC 提升 1.31%，核心收入指标提升 11.93%（50ms P99 内），已全量部署。

**核心创新：**
- 提出推荐原生 Transformer scaling 范式，解决信号质量和计算不对称两大挑战
- Encoder-Decoder 分解实现共享前缀训练和服务
- 行为序列 scaling 是一个被低估的提升方向

---

### 2.2 TGR: Tencent Generative Recommendation

| 项目 | 详情 |
|------|------|
| **标题** | TGR: Advancing Industrial Recommendation from Generative-Paradigm Ranking toward Unified Generation and Reasoning |
| **作者** | TGR Team: Lei Cheng, Haonan Hu, Beibei Kong, Yudong Li, Zang Li, Yunsheng Pang, Hongyang Su, Jianchao Tu, Yunlong Wang, Bing Wen, Junzhang Zhu, Shaojie Zhu, Chengxiang Zhuo |
| **机构** | Tencent |
| **链接** | https://arxiv.org/abs/2609.00986 |
| **日期** | 2026-09-01 |

**摘要：** 腾讯提出三方向耦合的生成式推荐框架。TGR-GenRank（CCFormer）：统一特征 tokenization + 特征场分离 cross attention + 层级序列压缩，CTR +3.57%，广告收入 +1.71%。TGR-GenRec：BARGE（item context-aware attention + 层级路径 reranking）Hit@5 +10.2-16.9%；HiGR（whole-slate generation）离线 slate 质量 +15.9-21.3%，5x 推理加速。TGR-Reason：离线生成 semantic-ID reason tokens 注入在线解码，冷启动新用户 Hit@1 +477.8%。已在腾讯生产环境全量部署。

**核心创新：**
- 将推荐从级联多阶段推进到统一生成+推理范式
- HiGR 实现 whole-slate generation（列表级生成）
- TGR-Reason 无需请求时 rollout 即可注入推理能力

---

### 2.3 CORAL: LLM-Native Harness for Production Recommender Systems

| 项目 | 详情 |
|------|------|
| **标题** | CORAL: An LLM-Native Harness for Production Recommender Systems |
| **作者** | Muhammad Rafay Azhar, Yuhang Zhou, Gilbert Jiang, Yuchen Wang, Rahul Sharma, Matthew DeSousa, Jiayi Liu, Xin Guo, Lizhu Zhang, Xiangjun Fan |
| **机构** | 未明确标注（大型社交平台） |
| **链接** | https://arxiv.org/abs/2609.02730 |
| **日期** | 2026-09-02 |

**摘要：** 提出 CORAL（Constraint-Optimized Recommender via an Agentic Loop），将 LLM agent 置于生产推荐系统的持续优化闭环中。每个周期 agent 观测信号、推理决策、调用工具（含数值优化器）重新配置推荐器，测量结果反馈下一轮。在两个大型社交平台上，同一 harness 在一个平台提升 engagement，在另一个平台降低 serving cost，均不损害对方指标。性能随循环迭代提升。

**核心创新：**
- 首个将 LLM agent 嵌入生产推荐系统持续优化闭环的系统
- 形式化为部分可观察、非平稳、约束优化问题
- 策略通过上下文改进，无需参数更新

---

### 2.4 CGM-Rec: Continual Graph Memory for Adaptive Recommendation

| 项目 | 详情 |
|------|------|
| **标题** | Continual Graph Memory for Adaptive Recommendation under Intent Drift |
| **作者** | (EMNLP 2026 Findings) |
| **机构** | 未明确标注 |
| **链接** | https://arxiv.org/abs/2609.04651 |
| **日期** | 2026-09-04 |

**摘要：** 提出 CGM-Rec，将知识图谱视为可写记忆。Semantic Graph Memory 通过质量门控类型操作保守更新；Episodic Lesson Memory 快速学习近期结果和失败案例。测试时模型参数冻结，仅通过记忆写入自适应。在 frozen-parameter 协议下，HR@1 相比最强 LLM baseline 提升最高达 29.58%。

**核心创新：**
- 将图状态视为可写记忆，实现无参数更新的自适应推荐
- 双组件记忆（保守语义 + 快速情景）应对意图漂移

---

### 2.5 CRAFT: Feature Transport for Scalable Recommendation

| 项目 | 详情 |
|------|------|
| **标题** | From Feature Interaction to Feature Transport — A Unified Block for Scalable Recommendation Models |
| **作者** | Zichen Luo, Jiachen Guo, Keming Gu, Jie Zhang |
| **机构** | 未明确标注 |
| **链接** | https://arxiv.org/abs/2609.01655 |
| **日期** | 2026-08-31 |

**摘要：** 提出 feature transport 视角，将深度统一推荐视为离散上下文条件化表征演化过程。CRAFT block 将非序列特征总结为可靠性感知的上下文场，生成残差位移和记忆保持信号。在 TAAC2026 广告推荐竞赛中 AUC 达 0.838090，超越历史最优 0.83798。6 层堆叠进一步提升至 0.838148。

**核心创新：**
- 从 feature interaction 范式转向 feature transport 范式
- 非序列上下文作为表征演化的主动控制器而非被动交互对象
- 在深度和宽度上均可扩展

---

## 3. CTR 预测

### 3.1 UniCon: Unified Context-Centric CTR Prediction

| 项目 | 详情 |
|------|------|
| **标题** | UniCon: A Unified Context-Centric Modeling Paradigm for CTR Prediction |
| **作者** | Jiajun Cui, Zhengqi Xu, Fan Zhang, Zhangteng, Gu Tang, Honghong Zhu, Mengxi Wu, Yulin Liang, Xingxing Wang |
| **机构** | Meituan |
| **链接** | https://arxiv.org/abs/2609.03290 |
| **日期** | 2026-09-03 |

**摘要：** 提出 UniCon，将请求上下文作为基本建模单元，历史行为和预测目标组织为同质上下文单元。Intra-context attention 捕获局部耦合（Locality），Inter-context attention 建模跨上下文的决策状态动态演化（Dynamics）。在美团搜索广告中，离线 AUC 提升 0.0139，线上 RPM +3.09%，CTR +2.07%，收入 +2.95%。

**核心创新：**
- 打破 sequential vs non-sequential 的异质性假设，统一为同质上下文单元
- 双层注意力架构分别建模局部耦合和全局动态
- Context-unit-level 序列压缩降低部署开销

---

### 3.2 PRIME: Plug-in Residual MoE for Shared CTR Top Networks

| 项目 | 详情 |
|------|------|
| **标题** | PRIME: Mitigating Subgroup Optimization Competition in Shared CTR Top Networks with Plug-in Residual Input-Conditioned Mixture of Experts |
| **作者** | (arXiv 未列出完整作者) |
| **机构** | 未明确标注 |
| **链接** | https://arxiv.org/abs/2608.30449 |
| **日期** | 2026-08-31 |

**摘要：** 诊断发现 CTR 模型共享 top network 中，语义子群的优化信号存在竞争（梯度余弦相似度降低 0.23-0.37）。提出 PRIME，用零残差初始化的低秩 residual experts 替换 Dense 层，在不改变原始函数的前提下添加 input-dependent 容量。在 Avazu/Criteo 上跨 13 种 CTR 架构，中位配对 AUC 提升 +0.0022/+0.0066。

**核心创新：**
- 首次诊断子群优化竞争问题
- Function-preserving 的即插即用 MoE 模块
- 零残差初始化确保训练起点不变

---

### 3.3 Native Multimodal Representation for CTR

| 项目 | 详情 |
|------|------|
| **标题** | Native Multimodal Representation Learning for Click-Through Rate Prediction in E-Commerce Scenarios |
| **作者** | (CIKM 2026) |
| **机构** | 未明确标注 |
| **链接** | https://arxiv.org/abs/2608.24091 |
| **日期** | 2026-08-25 |

**摘要：** 指出 CTR 数据中用户行为由多模态语义和非多模态因素共同驱动，导致端到端训练时监督模糊。提出 Mine-Then-Train 方法：先从 CTR 数据中挖掘高质量、多模态可解释的训练样本，再微调多模态编码器以对齐用户点击偏好。

**核心创新：**
- 发现 CTR 数据中端到端多模态训练无效的根因
- Mine-Then-Train 范式解决监督模糊问题

---

### 3.4 CADET: Decoder-Only Transformer for Ads CTR at LinkedIn

| 项目 | 详情 |
|------|------|
| **标题** | CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer |
| **作者** | LinkedIn Ads Team |
| **机构** | LinkedIn |
| **链接** | https://arxiv.org/abs/2602.11410 |
| **日期** | 2026-02 |

**摘要：** LinkedIn 部署的 decoder-only transformer 广告 CTR 预测系统。创新点包括：(1) 上下文条件化解码架构解决 CTR 预测与排序的鸡生蛋问题；(2) 自门控注意力稳定训练；(3) 时间戳 RoPE 捕获秒级到月级时间关系；(4) Session masking 防止 train-serve skew；(5) tensor packing + 自定义 FlashAttention kernel。线上 CTR 提升 +11.04%，CPC 降低 10.9%。

**核心创新：**
- 首个 decoder-only transformer 全面替代 DLRM ensemble 的生产广告系统
- 多塔解码解决 post-scoring context 不可用问题
- 自门控注意力机制稳定训练

---

### 3.5 EST: Efficient Scaling Laws in CTR Prediction

| 项目 | 详情 |
|------|------|
| **标题** | EST: Towards Efficient Scaling Laws in Click-Through Rate Prediction via Unified Modeling |
| **作者** | (淘宝/Taobao 团队) |
| **机构** | Alibaba/Taobao |
| **链接** | https://arxiv.org/abs/2602.10811 |
| **日期** | 2026-02 |

**摘要：** 识别 CTR 与 LLM 的两个关键差异：行为特征与非行为特征的信息密度不对称性、内容丰富信号的模态特定先验。提出 Lightweight Cross-Attention（LCA）+ Content Sparse Attention（CSA），在淘宝全站广告中 RPM +3.27%，CTR +1.22%。

**核心创新：**
- 分析 CTR 与 LLM 的本质差异，推导针对性设计原则
- 展示 CTR 预测的 power-law scaling 行为

---

### 3.6 GRAB: LLM-Inspired Generative CTR at Baidu

| 项目 | 详情 |
|------|------|
| **标题** | GRAB: An LLM-Inspired Sequence-First Click-Through Rate Prediction Modeling Paradigm |
| **作者** | Shaopeng Chen, Chuyue Xie, Huimin Ren 等 (Baidu Inc.) |
| **机构** | Baidu |
| **链接** | https://arxiv.org/abs/2602.01865 |
| **日期** | 2026-02 |

**摘要：** 百度提出的端到端生成式 CTR 框架。引入 Causal Action-aware Multi-channel Attention (CamA) 捕获行为序列中的时间动态和特定动作信号。线上部署 CTR +3.49%，CPM +3.05%，已全量上线。模型 AUC 随序列长度和模型容量单调提升，无饱和迹象。

**核心创新：**
- CamA 机制同时建模时间动态和动作信号
- 端到端行为序列建模取代传统 DLRM 流水线
- 展示推荐系统的 scaling behavior

---

## 4. 序列建模与用户行为

### 4.1 GateDiffInt: Diffusion + LLM Distillation for Behavior Modeling

| 项目 | 详情 |
|------|------|
| **标题** | GateDiffInt: Gate-Mediated Controllable Diffusion and Multi-Intent LLM Distillation for User Behavior Modeling |
| **作者** | (未明确标注) |
| **机构** | 大型工业平台（数十亿 DAU） |
| **链接** | https://arxiv.org/abs/2608.18764 |
| **日期** | 2026-08-20 |

**摘要：** 诊断 Noise-Intent Coupling（NIC）：噪声与意图相互强化——噪声扭曲意图，缺乏结构化先验导致去噪无明确目标。提出 GateDiffInt：(1) Gate-Mediated Controllable Diffusion 去噪行为序列；(2) Multi-Intent LLM Distillation 用 LLM 蒸馏四类结构化意图（长期、短期、潜在、转化）；(3) 意图感知 cross-attention 融合。已部署至首页 feed，14 天 A/B 测试 GMV +1.13%，累计 +5.13%。

**核心创新：**
- 首次形式化 Noise-Intent Coupling 问题
- 将可控扩散与多意图 LLM 蒸馏统一为联合框架
- Per-intent LoRA routing 防止意图坍缩

---

### 4.2 TS-SSM: Two-Sided State-Space Models for Sequential Recommendation

| 项目 | 详情 |
|------|------|
| **标题** | Two-Sided State-Space Models for Sequential Recommendation with Non-Random Multimodal Review Feedback |
| **作者** | (EMNLP 2026 Findings) |
| **机构** | 未明确标注 |
| **链接** | https://arxiv.org/abs/2609.00165 |
| **日期** | 2026-08-31 |

**摘要：** 针对双边数字平台的动态性，提出 TS-SSM。核心组件：(1) 模态缺失非随机融合模块编码评论内容和观测模式；(2) 用户状态演化 + 时变 + 局部图消息传递；(3) 商品状态演化的正负反馈不对称传递。在 6 个 Amazon 品类上 Recall@20 提升 14.8%-18.8%。

**核心创新：**
- 将推荐建模为双边状态空间模型，同时演化用户和商品状态
- 评论的非随机性和对商品状态的反作用被显式建模

---

### 4.3 HSR: Hamiltonian Spectral-Temporal Dynamics for Sequential Recommendation

| 项目 | 详情 |
|------|------|
| **标题** | Hamiltonian Spectral-Temporal Dissipative Dynamics for Sequential Recommendation |
| **作者** | (arXiv 未列出完整作者) |
| **机构** | 未明确标注 |
| **链接** | https://arxiv.org/abs/2608.25755 |
| **日期** | 2026-08-26 |

**摘要：** 将偏好演化重新概念化为耗散 Hamiltonian 系统：latent phase space 中的 position（稳定偏好）和 momentum（短期倾向）。线性时不变结构允许频域闭式解。learnable dissipation 捕获自然兴趣衰减，short local impulse refinement 模块建模稀疏交互中的突然行为波动。

**核心创新：**
- 首次用二阶动力学系统（Hamiltonian）建模序列推荐
- 频域闭式解高效捕获周期性和惯性演化

---

### 4.4 MGDiff: Multi-Interest with GNN-Guided Diffusion

| 项目 | 详情 |
|------|------|
| **标题** | MGDiff: Multi-Interest Sequence Recommendation with Masking GNN-Guided Diffusion |
| **作者** | (arXiv 未列出完整作者) |
| **机构** | 未明确标注 |
| **链接** | https://arxiv.org/abs/2609.01619 |
| **日期** | 2026-06-30 |

**摘要：** 提出 Dual-layer Semantic Guidance（DSG）框架：Weight-adaptive Masking GNN 重建缺失链接揭示深层物品关系，Dynamic Multi-Expert Network 将用户偏好投影到不同语义子空间。Popularity-Aware Guidance（PAG）机制通过物品流行度作为可微调节信号消除流行度偏差。

**核心创新：**
- GNN 引导的扩散模型生成无偏用户兴趣信息
- 双层语义引导提升生成准确性
- 流行度感知机制消除推荐中的流行度偏差

---

### 4.5 SAGA: Multi-Surface Generative Action Embedding

| 项目 | 详情 |
|------|------|
| **标题** | SAGA: Structure-Attended Generative Action Embedding Model that encodes Multi-Surface User Action Sequences |
| **作者** | (RecSys 2026) |
| **机构** | 金融服务机构 |
| **链接** | https://arxiv.org/abs/2608.15429 |
| **日期** | 2026-08-15 |

**摘要：** 将用户行为分解为 7 个字段级 token（6 个事件属性 + 分隔符），采用 round-robin per-field tokenization 进行自回归建模。在跨表面（结账、P2P 交易、应用参与、邮件等）的异构行为域上学习可复用用户表征。消融实验表明 per-field tokenization（K=7）优于 fused-key（K=1）和 interleaved（K=2）方案。

**核心创新：**
- 首次在推荐系统中应用 per-field round-robin tokenization 的自回归建模
- 跨表面异构行为域的统一用户表征学习

---

## 5. Game AI 与博弈论

### 5.1 NashDreamer: MBRL for Zero-Sum Imperfect-Information Games

| 项目 | 详情 |
|------|------|
| **标题** | NashDreamer: Model-Based Reinforcement Learning for Zero-Sum Imperfect-Information Games |
| **作者** | Tomáš Holeček, Viliam Lisý |
| **机构** | 未明确标注（学术界） |
| **链接** | https://arxiv.org/abs/2609.01549 |
| **日期** | 2026-09-01 |

**摘要：** 提出 NashDreamer，首个用于两人零和不完全信息博弈的 MBRL 框架。引入集中式 Multi-Agent Recurrent State-Space Model（MARSSM），将环境动态与玩家策略对各自观测的影响解耦。理论分析识别了 Dreamer 算法族在随机环境中易受 posterior collapse 影响的脆弱性。在 4 个基准博弈上显著优于 model-free baseline。

**核心创新：**
- 首个将 Dreamer-style MBRL 扩展到不完全信息博弈的框架
- MARSSM 证明集中式模型学习是不完全信息博弈中的数学必然
- 理论分析 Dreamer 家族的 posterior collapse 问题

---

### 5.2 LUGL: Non-Incremental Learners for Game Playing

| 项目 | 详情 |
|------|------|
| **标题** | Local Updates, Global Learning (LUGL): Playing Games with non-incremental Learners |
| **作者** | (arXiv 未列出完整作者) |
| **机构** | 未明确标注 |
| **链接** | https://arxiv.org/abs/2609.03660 |
| **日期** | 2026-09-03 |

**摘要：** 提出 LUGL 框架，使非增量学习器（如 LightGBM）能在 RL 设置中运作。交替进行 local updates（self-play 积累表格更新）和 global learning（训练函数逼近器泛化到未见状态后重置表格）。在 4 个完美信息博弈和 5 个不完全信息博弈上，LightGBM 基础的 agent 达到与 DQN/DeepCFR 竞争或更优的结果。

**核心创新：**
- 解耦数据收集与模型拟合，使树模型适用于博弈 RL
- 证明神经网络在博弈中的统治地位可能并非必然

---

### 5.3 LLM-Guided RL for Adaptive NPC Behavior

| 项目 | 详情 |
|------|------|
| **标题** | LLM-Guided Reinforcement Learning for Adaptive NPC Behavior in Multi-Agent Combat Games |
| **作者** | (arXiv 未列出完整作者) |
| **机构** | 未明确标注 |
| **链接** | https://arxiv.org/abs/2609.02931 |
| **日期** | 2026-08-27 |

**摘要：** 在 Unity 中训练 5 个 PPO 策略 NPC agent，用本地部署的 Mistral 7B 每 5 秒读取游戏状态并分配战术标签。对阵 Balanced 对手时，LLM 增强 agent 胜率从 11% 提升至 24%。但 2430 次策略选择分析显示 83.8% 选择了 Surround，表明零样本策略差异化能力有限。

**核心创新：**
- LLM 作为运行时策略选择器而非策略生成器
- 实证揭示小模型 LLM 在策略差异化上的局限

---

### 5.4 Robust PAC Learning of Concurrent Stochastic Games

| 项目 | 详情 |
|------|------|
| **标题** | Robust PAC Learning of Concurrent Stochastic Games |
| **作者** | (arXiv 未列出完整作者) |
| **机构** | 未明确标注 |
| **链接** | https://arxiv.org/abs/2609.04189 |
| **日期** | 2026-09-03 |

**摘要：** 首个针对一般和并发随机博弈的 PAC 学习框架（含转移不确定性）。引入 Nash margin 刻画均衡存在性：框架要么返回 ε-近似最优，要么给出精确 NE 不存在的可靠证书。在最小可达性条件下，算法在多项式样本量内终止。

**核心创新：**
- 首个 CSG 的鲁棒 PAC 学习框架
- Nash margin 机制处理均衡存在性问题

---

## 6. 广告与排序系统

### 6.1 Long-History User Transformers for Real-Time Ad Ranking

| 项目 | 详情 |
|------|------|
| **标题** | Long-History User Transformers for Real-Time Ad Ranking |
| **作者** | Viacheslav Ovchinnikov, Georgii Smirnov, Nikolai Savushkin, Veronika Ivanova, Maksim Kuzin |
| **机构** | Yandex |
| **链接** | https://arxiv.org/abs/2607.14331 |
| **日期** | 2026-07-15 |

**摘要：** 解耦长历史编码与实时推理的两阶段架构。离线 transformer 异步编码全跨表面交互历史为紧凑表征存入特征存储，轻量运行时模型在 serving 时结合缓存表征与最近事件和请求上下文。离线设计可恢复 72-80% 全历史 runtime transformer 的质量。线上搜索广告主指标 +2.77%，Yandex 广告网络 +2.1%，收入分别 +2.26% 和 +0.43%，不增加延迟。

**核心创新：**
- 离线编码 + 在线缓存的解耦架构解决长序列 CTR 的延迟瓶颈
- 预训练双目标（feedback prediction + next-item prediction）

---

### 6.2 CRRN: Cascading Relevance-driven Recommendation Network

| 项目 | 详情 |
|------|------|
| **标题** | Cascading Relevance-driven Recommendation Network for CTR Prediction in Trigger-Introduced Recommendation |
| **作者** | (arXiv 未列出完整作者) |
| **机构** | 未明确标注 |
| **链接** | https://arxiv.org/abs/2608.22973 |
| **日期** | 2026-08-24 |

**摘要：** 针对 Trigger-Introduced Recommendation（TIR）场景（用户点击感兴趣商品后展示目标商品），提出 CRRN。三个组件：Trigger-Target Interaction layer（个性化门控）、Cascading Interest Fusion（级联注意力融合即时和个性化兴趣）、Category-assisted Pairwise Loss（品类关联引导的触发相关性）。

**核心创新：**
- 针对 TIR 场景的 trigger relevance 建模
- 级联注意力显式分离即时兴趣和持久兴趣

---

## 7. LLM 系统与多智能体

### 7.1 Why Better Models Can Create Riskier Systems

| 项目 | 详情 |
|------|------|
| **标题** | Why Better Models Can Create Riskier Systems: Evidence from LLM Agents in Financial Markets |
| **作者** | (arXiv 未列出完整作者) |
| **机构** | 未明确标注 |
| **链接** | https://arxiv.org/abs/2609.04373 |
| **日期** | 2026-09-03 |

**摘要：** 发现"能力悖论"：提升单个模型能力可能导致系统级结果变差。共享训练和架构使更强大的 LLM 行为更相似，产生不可分散的相关性风险。在金融市场的 agent-based 模拟中验证：(1) 前沿 LLM 展示随能力增强而增加的显著相关行为；(2) 共享错误环境下，相关行为变为系统性风险。

**核心创新：**
- 提出 LLM 部署中的"能力悖论"
- 量化 LLM 群体中的不可分散风险下界

---

### 7.2 Inferred Generative-Process Diversity Predicts Correlated Failure

| 项目 | 详情 |
|------|------|
| **标题** | Inferred Generative-Process Diversity Predicts Correlated Failure Across Language Models |
| **作者** | (arXiv 未列出完整作者) |
| **机构** | 未明确标注 |
| **链接** | https://arxiv.org/abs/2609.03422 |
| **日期** | 2026-09-03 |

**摘要：** 提出"生成过程多样性"作为比语义相似度更根本的模型多样性度量。使用 Normalized Compression Distance 作为推断指标，在 38 个语言模型上识别出语义相似度遗漏的群体结构，并跨 10 个 benchmark family 预测相关失败。

**核心创新：**
- 基于算法信息论的生成过程多样性度量
- 比语义相似度更有效预测多模型系统中的相关失败

---

## 8. 其他相关工作

### 8.1 GenCAR: Generative Counterfactual Alignment for OOD Recommendation

| 项目 | 详情 |
|------|------|
| **标题** | GenCAR: Generative Counterfactual Alignment with Risk-Controlled Selection for Out-of-Distribution Recommendation |
| **作者** | (arXiv 未列出完整作者) |
| **机构** | 未明确标注 |
| **链接** | https://arxiv.org/abs/2609.02162 |
| **日期** | 2026-09-02 |

**摘要：** 将 OOD serving 形式化为风险控制的反事实选择问题。使用 LLM 提案通过 preference anchor 和 trust-radius 过滤，结合 conformal p-values 进行 Benjamini-Hochberg 选择，理论上保证 proxy-label FDR 控制。

**核心创新：**
- 将 conformal prediction 与反事实生成结合用于 OOD 推荐
- 有限样本、分布无关的 FDR 控制保证

---

### 8.2 Distill Globally, Adapt Locally: Reasoning Distillation for Trade-Up Recommendation

| 项目 | 详情 |
|------|------|
| **标题** | Distill Globally, Adapt Locally: Reasoning Distillation and Product-Type Test-Time Training for Scalable Trade-Up Recommendation |
| **作者** | (RecSys 2026 Workshop) |
| **机构** | 未明确标注 |
| **链接** | https://arxiv.org/abs/2609.05363 |
| **日期** | 2026-09-04 |

**摘要：** 两级框架：Level 1 用 LLM teacher 生成结构化关系标签和自然语言推理，蒸馏到紧凑 embedding-pair classifier（15.5M 参数，AUC 0.924）；Level 2 用 product-type test-time training 优化类别特定 adapter，AUC 提升至 0.941。蒸馏模型比直接 LLM 推理快约 5000x、成本低约 10000x。

**核心创新：**
- 推理蒸馏（rationale distillation）优于纯标签蒸馏
- Product-type test-time training 实现轻量级领域自适应

---

### 8.3 SwapRec: Warming Up Cold Items

| 项目 | 详情 |
|------|------|
| **标题** | SwapRec: Warming Up Cold Items Through Training-Time Swaps |
| **作者** | (RecSys 2026 Workshop) |
| **机构** | 未明确标注 |
| **链接** | https://arxiv.org/abs/2609.00913 |
| **日期** | 2026-09-01 |

**摘要：** 发现序列模型对 cold item swap 不鲁棒。提出 SwapRec：在训练时即应用同样的 swap 启发式（用 warm 邻居替换 cold item）。跨在线购物、电影、音乐三个领域验证，无论底层序列架构如何，均显著提升含 cold item 交互时的推荐准确性。

**核心创新：**
- 将推理时的 cold item swap 启发式引入训练时
- 即插即用，与任意序列推荐架构兼容

---

## 总结与趋势

| 方向 | 关键趋势 | 代表工作 |
|------|---------|---------|
| **CTR 预测** | 从 DLRM 向 decoder-only transformer 和统一建模迁移 | CADET, EST, GRAB, UniCon |
| **推荐系统** | 生成式推荐 + 推理注入，scale-up 行为序列 | ReST, TGR, CORAL |
| **序列建模** | 从一阶到高阶动力学（Hamiltonian），双边状态空间，扩散模型 | HSR, TS-SSM, GateDiffInt |
| **LLM 理论** | 内部表征与行为脱节，贝叶斯几何，证据整合机制 | 几何无知方向, 探针诊断 |
| **Game AI** | MBRL 扩展到不完全信息博弈，树模型在博弈中的可行性 | NashDreamer, LUGL |
| **广告系统** | 离线-在线解耦的长序列编码，LLM agent 闭环优化 | Yandex 长历史 transformer, CORAL |
