---
title: Conference Digest — ICML 2026, NeurIPS 2025, ICLR 2026, AAAI 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025
type: synthesis
created: 2026-07-30
updated: 2026-07-30
tags: [conference-digest, icml-2026, neurips-2025, iclr-2026, aaai-2026, kdd-2026, cvpr-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2025, recsys-2025]
sources: []
---

# 会议摘要：2025–2026 顶级 ML/AI 会议论文纵览

> 覆盖 ICML 2026、NeurIPS 2025、ICLR 2026、AAAI 2026、KDD 2026、CVPR 2026、ACL 2026、EMNLP 2025、SIGIR 2026、WWW 2026、CIKM 2025、RecSys 2025 的获奖论文与亮点研究。

---

## 1. ICML 2026（首尔，2026年7月6–11日）

- 投稿数：6,500+ 接受论文
- 地点：韩国首尔 COEX

### Outstanding Paper Awards（最佳论文奖）

#### 🏆 The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models
- **作者**: Zanlin Ni, Shenzhi Wang, Yang Yue, Tianyu Yu, Weilin Zhao, Yeguo Hua, Tianyi Chen, Jun Song, Cheng Yu, Bo Zheng, Gao Huang (清华大学 LeapLab / 阿里巴巴)
- **论文**: https://arxiv.org/abs/2601.15165 | https://github.com/LeapLabTHU/JustGRPO
- **关键词**: Diffusion LLM, RL, Reasoning, JustGRPO
- **核心发现**: 传统观念认为扩散语言模型（dLLM）的任意顺序生成能力优于自回归约束。本文证明这一"灵活性"在强化学习训练中反而有害——模型会利用自由度回避高不确定性的"分叉词"（如 Therefore、Since），导致 entropy degradation。作者提出 JustGRPO，在 RL 训练阶段强制左到右顺序，推理时保留双向注意力与并行解码。GSM8K 89.1%, MATH-500 45.1%, 超过所有专门的 diffusion-RL 方法。

#### 🏆 High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions
- **作者**: Fan Chen, Sinho Chewi, Constantinos Daskalakis, Alexander Rakhlin (MIT)
- **关键词**: Diffusion sampling, log-concave, high-accuracy
- **核心贡献**: 为扩散模型和对数凹分布提供了高精度采样算法，理论保证与实用性能兼备。

### Outstanding Position Paper

#### Position: The Alignment Community is Unintentionally Building a Censor's Toolkit
- **作者**: Sarah Ball, Phil Hackemann
- **核心观点**: 对齐研究社区的工具（RLHF、红队测试等）可能被滥用于内容审查。呼吁反思双用途风险。

### Honorable Mentions

- **The Obfuscation Atlas**: 用"欺骗探针"映射 RLVR 中诚信涌现的位置
- **Motion Attribution for Video Generation**: 视频生成中的运动归因
- **How much can language models memorize?**: LLM 记忆能力的量化研究
- **Training AI Co-Scientists Using Rubric Rewards**: 用评分奖励训练 AI 合著科学家
- **Wait, Wait, Wait… Why Do Reasoning Models Loop?**: 推理模型为何陷入循环

### Other Notable ICML 2026 Papers

- **CodeClash**: LLM 在多轮锦标赛中构建代码库的基准
- **Position: To Defend Against Cyber Attacks, We Must Teach AI Agents to Hack**: 安全攻防立场论文
- **Don't Drop Dropout**: LLM 训练中 layer dropout 的最佳实践
- **Position: The AI Imperative: Scaling High-Quality Peer Review in ML**: AI 辅助同行评审
- **Towards A Generative Protein Evolution Machine with DPLM-Evo**: 蛋白质进化生成模型
- **Foundation Model Operating System (FMOS)**: 提出基础模型操作系统的概念

---

## 2. NeurIPS 2025（圣地亚哥 / 墨西哥城，2025年12月）

- 投稿数：21,575 | 接受：5,290 (24.5%)

### Best Paper Awards（最佳论文奖）

#### 🏆 Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)
- **作者**: Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu 等
- **关键词**: LLM diversity, hivemind, INFINITY-CHAT
- **核心贡献**: 揭示 LLM 的"人工蜂巢思维"现象——不同模型回答趋同。发布 INFINITY-CHAT 数据集用于研究真实世界开放查询中的多样性。

#### 🏆 Gated Attention: An Empirical Study
- **作者**: Alibaba Qwen Team
- **关键词**: Gated attention, softmax, LLM architecture
- **核心贡献**: 在 softmax attention 后引入 head-specific sigmoid gating，全面提升训练稳定性、减少 attention sink、增强长上下文。已在 Qwen3-Next 中部署。30+ 实验验证。

#### 🏆 Why Diffusion Models Don't Memorize
- **作者**: Giulio Biroli 等
- **关键词**: Diffusion model, memorization, generalization, implicit regularization
- **核心贡献**: 证明扩散模型训练动力学在泛化→记忆之间存在两个可预测的时间尺度。早期数据集无关的泛化阶段 + 后期线性记忆阶段。

#### 🏆 1,000 Layer Networks for Self-Supervised RL (Best Paper + Datasets & Benchmarks)
- **作者**: Kevin Wang, Ishaan Javali 等
- **关键词**: Deep RL, self-supervised, 1024-layer
- **核心贡献**: 将自监督 RL 网络从 2-5 层扩展到 1024 层，在 locomotion/manipulation 上实现 2-50x 性能提升。

### Best Paper Runners-Up

- **Transductive Online Learning**: 解决 30 年悬而未决的转导在线学习最优错误界问题
- **Neural Scaling Laws via Superposition**: 证明表示叠加（representation superposition）是神经 scaling law 的核心驱动机制
- **RLVR Reasoning Capabilities**: GRPO 数学推理能力涌现研究（清华团队）

### Test of Time Award

- **Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks** (Ren, He, Girshick, Sun, 2015)

---

## 3. ICLR 2026（里约热内卢，2026年4月23–27日）

- 投稿数：19,525 | 接受：5,355 (27.4%) | Oral：225 | 评审危机（45% 身份泄露、21% AI 生成评审）

### Oral Papers Highlights

#### Common Corpus: Ethical LLM Pre-training Data
- **关键词**: Open data, ethical AI, pretraining corpus
- **核心贡献**: 构建大规模开放伦理预训练数据集

#### Q-RAG: Multi-step Retrieval via RL-Trained Embedders
- **关键词**: RAG, retrieval, RL, embedding
- **核心贡献**: 使用强化学习训练嵌入器实现多步检索

#### FIRE: Stability-Plasticity Reinitialization
- **关键词**: Continual learning, stability-plasticity
- **核心贡献**: 在新任务上选择性重初始化部分参数以平衡稳定性与可塑性

#### WebDevJudge: LLM-as-a-Judge for Web Development
- **关键词**: LLM evaluation, web development, judge
- **核心贡献**: 压力测试 LLM 在开放网页开发任务中的评判能力

#### SafeDPO: Safe Direct Preference Optimization
- **关键词**: Alignment, safety, DPO
- **核心贡献**: 无需辅助网络即可平衡 helpfulness 与 safety 的约束 DPO

#### MedAgentGym: 72,000+ Biomedical Tasks for Agent Training
- **关键词**: Medical agent, training environment, benchmark

#### Why DPO is a Misspecified Estimator
- **关键词**: Alignment theory, DPO, statistical flaw
- **核心贡献**: 揭露 DPO 在统计上的根本性误设问题

### Notable Papers

- **MicroMix (NVIDIA)**: 新型混合精度量化硬件格式
- **DeepCompress**: 压缩推理链以防止大推理模型在简单问题上"过度思考"
- **From Pixels to Words (NEO)**: 原生视觉语言基元
- **La-Proteina**: 基于部分隐变量表示的原子级蛋白质设计
- **Discount Model Search**: 高质量多样性优化（Oral）
- **FingerTip 20K**: 主动个性化移动 LLM Agent 基准
- **InclusiveVidPose**: 肢体缺陷人群的人体姿态估计数据集
- **MedAraBench**: 阿拉伯语医疗 QA 数据集

---

## 4. AAAI 2026（新加坡，2026年1月20–27日）

- 接受论文：4,902 篇 | 主题：人工智能社会影响 + AI 对齐

### Highlights

- **10 Open Challenges Steering the Future of Vision-Language-Action Models**: VLA 模型的 10 大开放挑战
- **2D-CrossScan Mamba**: 带有空间一致多路径 2D 信息传播的状态空间模型
- **3D Gaussian Splatting for Large Sparse Environments**: 大尺度稀疏环境 3D 重建
- **Resource Efficient Sleep Staging via Multi-Level Masking**: 多级掩码与提示学习的资源高效睡眠分期
- **ViG-RAG**: 视觉基础模型 + RAG 的视频问答
- **Competitor-Discovery AI Agent**: 制药竞争情报的 AI Agent 系统
- **2D Gaussians Spatial Transport**: 点监督密度回归

---

## 5. KDD 2026（济州岛，韩国，2026年8月9–13日）

- 双周期提交 | 主会场：Research Track + Applied Data Science Track

### Key Themes & Notable Papers

- **Large-Scale Sequential Recommendation**: 基于 LLM 的大规模序列推荐
- **Graph Neural Networks for E-Commerce**: 电商图神经网络最新进展
- **Federated Learning for Recommendation**: 联邦推荐系统隐私保护
- **Causal Recommendation**: 因果推断用于推荐去偏
- **Time-Series Foundation Models**: 时序基础模型
- **MOCHEE**: 无源域数据的语音分类器合并框架（SNU）
- **SharVeT**: 基于向量调优的参数共享 LLM 压缩（SNU, ACL 2026 跨录）

> KDD 2026 正在进行中，更多获奖论文将在会后更新。

---

## 6. CVPR 2026（丹佛，2026年6月）

- 投稿数：16,092 | 接受：4,089

### Best Paper

#### 🏆 Efficiently Reconstructing Dynamic Scenes One D4RT at a Time
- **关键词**: Dynamic scene reconstruction, 4D, transformer
- **核心贡献**: 统一的 transformer 架构同时估计深度、时空对应和相机参数。高度可扩展的动态场景重建方法。

#### 🏆 Native and Compact Structured Latents for 3D Generation (Best Student Paper)
- **关键词**: 3D generation, structured latents, compact
- **核心贡献**: 原生紧凑结构化隐空间用于高效 3D 生成。

### Honorable Mentions

#### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **关键词**: Gaming agent, foundation model, open-source
- **核心贡献**: 开源通用游戏 AI Agent 基础模型。这是 CVPR 关注游戏 AI 的一个有趣信号。

#### Real-Time One-Step Image Editing
- **关键词**: Image editing, one-step, real-time
- **核心贡献**: 免训练、免反转的单步图像编辑，实现真正实时编辑。

### Other Notable

- **O-Voxel**: 超越现有模型的三维生成体积方法
- **Beyond Raw Signals**: 未解码生成隐变量作为特权合成数据（SynData4CV Best Short Paper）
- **BadVLM**: VLM 后门攻击

---

## 7. ACL 2026（圣地亚哥，2026年7月2–7日）

- 投稿数：12,148 | Main：2,296 (18.9%) | Findings：2,163 (17.8%) | 特殊主题：可解释性

### Best Papers

#### 🏆 The Imperfective Paradox in Large Language Models
- **关键词**: Linguistic semantics, aspectual reasoning
- **核心贡献**: 测试 LLM 是否真正理解语言学中的"未完成体悖论"（如"正在画画"vs"画了画"的逻辑差异）。

#### 🏆 Memory Efficiency and Resource-Rational Encoding in Sentence Processing
- **关键词**: Psycholinguistics, memory, efficiency
- **核心贡献**: 资源理性工作记忆分配模型在人脑句子处理中的神经实现。

#### 🏆 Characterizing the Expressivity of Local Attention in Transformers
- **关键词**: Transformer theory, local attention, expressivity
- **核心贡献**: 理论刻画当 attention 被限制在局部窗口时 Transformer 变体可以（和不可以）表达什么的精确边界。

### Key Trends

- **Agent & Reasoning**: 从 2025 年的 142 篇增长至 366 篇，增幅最大
- **RAG & Retrieval**: ReasonEmbed、BordaRAG 等推动检索增强推理
- **Multimodal NLP**: Uni-MMMU 基准、FastV-RAG 视频问答
- **Citation Integrity**: ACL 对 AI 生成参考文献实行零容忍政策
- **Big Tech**: Google、Meta、Microsoft、阿里巴巴等均有大量论文

### Notable Papers

- **LightReasoner**: 小模型教大模型推理
- **Process Reward Models Meet Planning**: 基于规划的 PRM 数据生成
- **ReasonEmbed**: 推理密集型文档检索的文本嵌入
- **FastV-RAG**: 快速精细视频问答 + RAG
- **Uni-MMMU**: 大规模多学科多模态统一基准

---

## 8. EMNLP 2025（苏州，2025年11月4–9日）

- 接受：Main 1,811 (22.16%) | Findings 1,417 (17.34%)
- 特殊主题：效率（Efficiency in Model Algorithms, Training, and Inference）

### Best & Outstanding Papers

- **Thinking Out Loud: Do Reasoning Models Know When They're Right?**: 推理模型的自我认知研究
- **SLoW: Select Low-frequency Words**: 基于低频词选择的 LLM 翻译词典
- **ViMUL-Bench**: 14 语言多语言视频 LMM 基准
- **Cross-Linguistic T2I Bias**: 语法性别如何影响文生图模型（覆盖 5 种性别语言 + 2 种中性语言控制）
- **FinRetrieval**: 金融数据检索 Agent 基准（Claude Opus 结构化 API 90.8% vs 纯网页搜索 19.8%）

---

## 9. SIGIR 2026（墨尔本，2026年7月20–24日）

- 投稿：1,271 | 接受：234 (18.41%)

### Notable Papers

- **Agentic Spatio-Temporal Grounding via Collaborative Reasoning**: 时空视频定位的 Agent 框架（A*STAR）
- **Time-Interval-Aware Disentangled Expert Modeling for Next-Basket Recommendation**: 时间间隔感知的下一篮推荐
- **Robust Multimodal Recommendation via Graph Retrieval-Enhanced Modality Completion**: 图检索增强的多模态推荐
- **Beyond Static Best-of-N: Bayesian List-wise Alignment for LLM-based Recommendation**: 贝叶斯列表级对齐用于 LLM 推荐
- **RAG-Enhanced LLMs for Dynamic Content Expiration Prediction**: RAG 增强的动态网页过期预测
- **Bridging Behavior and Semantics for Time-aware Cross-Domain Sequential Recommendation**: 跨域序列推荐
- **When More Reformulations Hurt: Avoiding Drift using Ranker Feedback**: 检索中的查询重构漂移问题

---

## 10. WWW 2026（迪拜，2026年4月13–17日）

- ACM 完全开放获取元年

### Notable Papers

- **Recommender Systems with LLMs**: 大模型增强推荐系统多篇
- **Graph Neural Networks for Web Mining**: 图神经网络应用于网页挖掘
- **Unlock a Simple Solution for Data Sparsity and Class Imbalance in Recommender System**: 推荐系统数据稀疏和类别不平衡
- **Web Agent Systems**: 网页 Agent 系统研究

---

## 11. CIKM 2025（首尔，2025年11月10–14日）

- 投稿：2,761 | 接受：810 (29%)

### Notable Papers

- **Improving Text Embedding Models with Positive-aware Hard-negative Mining** (NVIDIA): 正例感知的难负样本挖掘
- **CEM: A Data-Efficient Method for LLMs to Continue Evolving From Mistakes**: 从错误中持续进化的 LLM
- **BordaRAG**: 基于排序理论的冲突文档选择（人大）
- **ClariLM**: 合成大规模澄清数据增强 LLM 澄清能力
- **FollowGPT**: 从对话日志挖掘用户追问意图
- **PKGRec**: 联邦推荐中的个人知识图谱构建
- **KUG**: 内外部知识联合增强的 RAG
- **Collaborative Interest Mining Network for KG-based Recommendation**: 知识图谱推荐协同兴趣挖掘

---

## 12. RecSys 2025（布拉格，2025年9月22–26日）

### Key Papers

- **LLM4Rec**: LLM 增强推荐系统的范式转移
  - R²ec (NeurIPS 2025): 首个具有推理链的统一大规模推荐模型 + RecPO RL 框架
  - RecZero: 纯 RL (GRPO) 训练单个 LLM 自主发展评分推理能力
- **OneRec / OneRec-V2 (Kuaishou)**: 生成式推荐取代级联检索+排序生产线。在线观看时长 +1.6%
- **ULTRA-HSTU (Meta)**: HSTU 2.0，动作编码+半局部注意力，训练 5.3x、推理 21.4x 加速
- **Netflix Foundation Model for Personalized Recommendation**: Netflix 自回归Transformer 推荐基础模型
- **Actions Speak Louder than Words (HSTU, Meta ICML 2024)**: 生成式推荐 scaling law 开创性工作
- **LEAF (NVIDIA)**: 轻量高效自适应灵活嵌入用于大规模推荐
- **You Say Search, I Say Recs (Spotify)**: 基于 Agent 的查询理解与探索性搜索
- **Lasso**: 基于 LLM 的跨域用户模拟器

---

## 13. 综合性 Trends 分析

### 最突出的研究趋势

| 趋势 | 说明 | 代表会议 |
|------|------|----------|
| 扩散模型统治 | ICML 两项最佳论文均为扩散模型 | ICML 2026 |
| LLM Agent 与推理 | Agent 论文数量翻倍增长 | ACL 2026, ICLR 2026 |
| 生成式推荐 | 用生成模型替代级联检索+排序 | RecSys 2025, KDD 2026 |
| 效率压倒规模 | 量化、蒸馏、压缩成为主流假设 | ICLR 2026, AAAI 2026 |
| 对齐与安全成熟化 | DPO 被质疑、safeRL 兴起 | ICLR 2026, ICML 2026 |
| 多模态理解深化 | 视频理解、VLM、文生图交叉 | CVPR 2026, ACL 2026 |
| 可解释性受重视 | ACL 2026 特殊主题 | ACL 2026 |
| RAG 升级 | RL 训练检索器、多步推理 | ICLR 2026, SIGIR 2026 |
| Scaling Law 理论基础 | 叠加理论解释 scaling | NeurIPS 2025 |

### 重点实验室/公司方向

| 机构 | 重点方向 |
|------|----------|
| Google DeepMind | AGI→ASI 路线图、AI 安全、视频理解 |
| OpenAI | 推理模型 (o3/o4)、Agent SDK |
| Anthropic | 宪法 AI、计算机操控、可解释性 |
| Meta | HSTU 生成式推荐、Llama 4 开源模型 |
| Microsoft | Phi 系列小模型、Copilot Agent |
| 阿里巴巴 (Qwen) | Gated Attention (NeurIPS Best Paper)、Qwen3-Next |
| 字节跳动 | TokenMixer/RankMixer 序列模型 |
| 快手 (Kuaishou) | OneRec 生成式推荐 |
| NVIDIA | MicroMix 量化、LEAF 嵌入 |
| 清华大学 | The Flexibility Trap (ICML Best)、JustGRPO |
| Netflix | 自回归推荐基础模型 |

---

## 14. 关键论文链接汇总

| 论文 | Venue | 链接 |
|------|-------|------|
| The Flexibility Trap | ICML 2026 | https://arxiv.org/abs/2601.15165 |
| High-Accuracy Sampling for Diffusion | ICML 2026 | https://icml.cc/virtual/2026/oral/71132 |
| Artificial Hivemind | NeurIPS 2025 | https://openreview.net/forum?id=saDOrrnNTz |
| Gated Attention (Qwen) | NeurIPS 2025 | https://openreview.net/forum?id=57 |
| Why Diffusion Models Don't Memorize | NeurIPS 2025 | https://neurips.cc/virtual/2025/awards_detail |
| D4RT Dynamic Scene Reconst. | CVPR 2026 | https://openaccess.thecvf.com/content/CVPR2026/html/Zhang |
| NitroGen Gaming Agent | CVPR 2026 HM | https://prnewswire.com |
| JustGRPO Code | ICML 2026 | https://github.com/LeapLabTHU/JustGRPO |
| OneRec-V2 | KDD/arXiv 2025 | Kuaishou |
| R²ec | NeurIPS 2025 | HIT/SJTU |
| ULTRA-HSTU | arXiv 2026 | Meta |
| Netflix Foundation Model | Netflix Tech Blog 2025 | Netflix |
| Q-RAG | ICLR 2026 Oral | OpenReview |
| SafeDPO | ICLR 2026 Oral | OpenReview |
| FinRetrieval | arXiv 2026 | Claude Opus eval |
| MedAgentGym | ICLR 2026 Oral | OpenReview |
| From AGI to ASI | DeepMind 2026 | arXiv:2606.12683 |
| Agentic STG (ASTG) | SIGIR 2026 | https://arxiv.org/abs/2602.13313 |
