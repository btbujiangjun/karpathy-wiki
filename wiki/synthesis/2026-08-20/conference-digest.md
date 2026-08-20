---
title: 2026 AI 会议论文全景速递
title-en: 2026 AI Conference Paper Digest
type: synthesis
created: 2026-08-20
updated: 2026-08-20
tags: [arxiv-daily, conference, ICML, AAAI, NeurIPS, ICLR, KDD, CVPR, ACL, EMNLP, SIGIR, WWW, CIKM, RecSys]
sources: []
---

# 2026 AI 会议论文全景速递

> **日期**：2026-08-20  
> **覆盖范围**：ICML 2026 / AAAI 2026 / NeurIPS 2025 / ICLR 2026 / KDD 2026 / CVPR 2026 / ACL 2026 / EMNLP 2025 / SIGIR 2026 / WWW 2026 / CIKM 2025 / RecSys 2025  
> **来源**：arXiv, OpenReview, ACL Anthology, Springer, DBLP, 各会议官网

---

## 目录

- [1. 会议时间线](#1-会议时间线)
- [2. ICML 2026](#2-icml-2026)
- [3. AAAI 2026](#3-aaai-2026)
- [4. NeurIPS 2025](#4-neurips-2025)
- [5. ICLR 2026](#5-iclr-2026)
- [6. KDD 2026](#6-kdd-2026)
- [7. CVPR 2026](#7-cvpr-2026)
- [8. ACL 2026](#8-acl-2026)
- [9. EMNLP 2025](#9-emnlp-2025)
- [10. SIGIR 2026](#10-sigir-2026)
- [11. WWW 2026](#11-www-2026)
- [12. CIKM 2025](#12-cikm-2025)
- [13. RecSys 2025](#13-recsys-2025)
- [14. 热门主题与趋势](#14-热门主题与趋势)
- [15. 值得关注的论文（Top Picks）](#15-值得关注的论文top-picks)

---

## 1. 会议时间线

| 会议 | 时间 | 地点 | 类型 |
|------|------|------|------|
| AAAI-40 | 2026/1/20–27 | 新加坡 | 全会 |
| NeurIPS 2025 | 2025/12/2–8 | 圣地亚哥 | 全会 |
| ICLR 2026 | 虚拟/时间待定 | 虚拟 | 全会 |
| CVPR 2026 | 2026/6/3–7 | 丹佛 | 计算机视觉 |
| EMNLP 2025 | 2025 | 中国（线上/线下） | NLP |
| RecSys 2025 | 2025/9 中旬 | 布拉格 | 推荐系统 |
| CIKM 2025 | 2025 | 韩国 | 信息管理 |
| ICML 2026 | 2026/8/9–13 | 温哥华 | 机器学习 |
| KDD 2026 | 2026/8/9–13 | 济州岛 | 数据挖掘 |
| ACL 2026 | 2026 | 多地 | NLP |
| SIGIR 2026 | 2026 | 待定 | 信息检索 |
| WWW 2026 | 2026 | 待定 | Web |

---

## 2. ICML 2026

> **时间**：2026/8/9–13（温哥华）  
> **征稿截止**：2026/2/4，12,539 篇投稿，3,561 篇接收（28.4% 接收率）  
> **亮点**：研究界持续向高效计算、可解释性、几何建模方向演进

### 2.1 综合/效率

| # | 论文标题 | 作者 | 机构 | 链接 | 简介 |
|---|---------|------|------|------|------|
| 1 | **Inference-Time Optimization for Diffusion-Based Generation with Speed-Dynamic SDEs** | — | University of Illinois | [arXiv:2608.06993](https://arxiv.org/abs/2608.06993) | 提出 speed-dynamic SDE 用于扩散模型推理时优化，提升生成速度同时保持质量 |
| 2 | **ACE-RT: Adaptive Cross-Entropy Rate Targeting for Flow Matching** | — | Rice University | [arXiv:2608.06980](https://arxiv.org/abs/2608.06980) | 自适应熵率目标，改进 flow matching 在图像与分子生成中的性能 |
| 3 | **Revisiting Convergence of Sharpness-Aware Minimization** | — | 新加坡国立大学 | [arXiv:2608.06796](https://arxiv.org/abs/2608.06796) | 重新分析 SAM 收敛性，建立首个凸目标与线性过参数化下的严格收敛界 |
| 4 | **Causal State Space Models are Secretly Multitask Learners** | — | Meta AI | [arXiv:2608.06862](https://arxiv.org/abs/2608.06862) | 揭示因果状态空间模型的多任务学习本质，揭示因果结构如何隐式促进多任务泛化 |
| 5 | **Universal Approximation of (Un)Relational Programs** | — | University of Tokyo | [arXiv:2608.06783](https://arxiv.org/abs/2608.06783) | 探索神经网络在程序合成中的逼近能力，建立可逼近算法的充分必要条件 |
| 6 | **Teleformer: A Novel Communication Scheme for Distributed Transformers** | — | Shanghai Jiao Tong University | [arXiv:2608.06692](https://arxiv.org/abs/2608.06692) | 通过可学习拓扑稀疏通信降低分布式 Transformer 通信成本 |

### 2.2 可信/鲁棒性/公平性

| # | 论文标题 | 作者 | 机构 | 链接 | 简介 |
|---|---------|------|------|------|------|
| 1 | **Agnostic Data Poisoning Attacks on Robustness of Prompt Tuning** | — | — | [arXiv:2608.06959](https://arxiv.org/abs/2608.06959) | 揭示提示微调在数据投毒攻击下的脆弱性，提出攻击方法并验证风险 |
| 2 | **Benchmarking Fairness Enhancing Algorithms under Class Imbalance** | — | — | [arXiv:2608.06920](https://arxiv.org/abs/2608.06920) | 系统基准评估类不平衡下公平性增强算法的实际表现 |

### 2.3 图/结构/几何

| # | 论文标题 | 作者 | 机构 | 链接 | 简介 |
|---|---------|------|------|------|------|
| 1 | **Targeted Representation Recovery from Certified Smoothed Models via Neural Collapse** | — | Peking University / IIT | [arXiv:2608.06724](https://arxiv.org/abs/2608.06724) | 从认证平滑模型中通过神经坍缩恢复目标表示 |
| 2 | **Collaborative Graph Spectral Evolution for Multi-view Clustering** | — | — | [arXiv:2608.07027](https://arxiv.org/abs/2608.07027) | 图谱协同演化方法，提升多视图聚类性能 |

### 2.4 大语言模型/推理/RL

| # | 论文标题 | 作者 | 机构 | 链接 | 简介 |
|---|---------|------|------|------|------|
| 1 | **Deductive-Convergent Reinforcement Learning for Scalable and Reliable LLM Alignment** | — | — | [arXiv:2608.06958](https://arxiv.org/abs/2608.06958) | 演绎收敛 RL 方法，解决 LLM 对齐中的奖励攻击与脆弱性 |
| 2 | **RLXY: Simple and Effective Test-Time Rewards for LLMs** | — | — | [arXiv:2608.07001](https://arxiv.org/abs/2608.07001) | 简单有效的测试时奖励机制，持续提升 LLM 性能 |
| 3 | **Instruct-Core: A Unified Framework for Instruction-Based Cross-Domain Reinforcement Learning** | — | — | [arXiv:2608.06971](https://arxiv.org/abs/2608.06971) | 指令驱动的跨域 RL 统一框架，支持零样本迁移 |
| 4 | **Efficient Test-Time Reinforcement Learning with Metric-Guided Verifier** | — | — | [arXiv:2608.07036](https://arxiv.org/abs/2608.07036) | 度量引导验证器加速测试时 RL，降低采样成本 |
| 5 | **One-Shot Code-as-Policies: Meta-Prompting for Generalizable Robotic Manipulation** | — | — | [arXiv:2608.06818](https://arxiv.org/abs/2608.06818) | 一次性代码策略生成，结合元提示实现可泛化的机器人操作 |

### 2.5 推荐/搜索/个性化

| # | 论文标题 | 作者 | 机构 | 链接 | 简介 |
|---|---------|------|------|------|------|
| 1 | **Value-Diversified User Modeling for Multi-Behavior Recommendation with Dual-Channel Mixture-of-Experts** | — | — | [arXiv:2608.06856](https://arxiv.org/abs/2608.06856) | 价值多样化用户建模，双通道 MoE 提升多行为推荐性能 |
| 2 | **Advancing Large Recommendation Models with Castle Parallelism and Hybrid Flow** | — | ByteDance | arXiv (搜 "Castle Parallelism" "ByteDance") | Castle 并行策略 + 混合数据流，支持千亿级推荐大模型训练 |

### 2.6 具身智能/机器人

| # | 论文标题 | 作者 | 机构 | 链接 | 简介 |
|---|---------|------|------|------|------|
| 1 | **Co-Evolved World Model and Policy for Vision-Language-Action Robot Learning** | — | — | [arXiv:2608.06813](https://arxiv.org/abs/2608.06813) | 世界模型与策略联合演化，实现 VLA 机器人学习 |
| 2 | **Body Mass Index-Invariant Obesity Management via Tactile Informed Visual Proprioception** | — | — | [arXiv:2608.06840](https://arxiv.org/abs/2608.06840) | 触觉-视觉联合感知，实现 BMI 不敏感的肥胖管理 |

### 2.7 音频/语音

| # | 论文标题 | 作者 | 机构 | 链接 | 简介 |
|---|---------|------|------|------|------|
| 1 | **ProLong: A Long-Context LLM-Based Unified Framework for Multi-Granularity Music Understanding and Captioning** | — | — | [arXiv:2608.06961](https://arxiv.org/abs/2608.06961) | 长上下文 LLM 驱动的多粒度音乐理解与描述统一框架 |

### 2.8 多模态/视觉语言

| # | 论文标题 | 作者 | 机构 | 链接 | 简介 |
|---|---------|------|------|------|------|
| 1 | **Revolutionizing Remote Sensing with Vision Language Models: A Survey** | — | — | [arXiv:2608.06659](https://arxiv.org/abs/2608.06659) | VLM 在遥感中的全面综述，覆盖场景分类、变化检测、跨模态检索等 |
| 2 | **Hierarchical Semantic-Informed Multi-Object NeRFs** | — | — | [arXiv:2608.06707](https://arxiv.org/abs/2608.06707) | 层次语义驱动的多物体 NeRF，支持开放词汇实例分割 |
| 3 | **Cross-Vocabulary Knowledge Distillation for Efficient Multi-Tier Recommendations** | — | — | [arXiv:2608.06933](https://arxiv.org/abs/2608.06933) | 跨词表知识蒸馏，高效多层级推荐系统 |

### 2.9 语音/音乐

| # | 论文标题 | 作者 | 机构 | 链接 | 简介 |
|---|---------|------|------|------|------|
| 1 | **Simultaneous Speech-to-Speech Translation with Autoregressive Semantic Tokens** | — | — | [arXiv:2608.07038](https://arxiv.org/abs/2608.07038) | 自回归语义 token 的同步语音翻译，无需离线参考音频 |

### 2.10 时序/预测/因果

| # | 论文标题 | 作者 | 机构 | 链接 | 简介 |
|---|---------|------|------|------|------|
| 1 | **Multi-Resolution Cryptocurrency Price Forecasting via HTM-Augmented Multi-Branch ResNet** | — | — | [arXiv:2608.06907](https://arxiv.org/abs/2608.06907) | HTM 增强多分支 ResNet 实现多分辨率加密货币价格预测 |

### 2.11 多目标/生成式优化

| # | 论文标题 | 作者 | 机构 | 链接 | 简介 |
|---|---------|------|------|------|------|
| 1 | **MOBO: Efficient Performance Estimation via Multi-Fidelity Bayesian Optimization in Multi-Objective Neural Architecture Search** | — | — | [arXiv:2608.07062](https://arxiv.org/abs/2608.07062) | 多保真贝叶斯优化，高效多目标神经架构搜索 |

---

## 3. AAAI 2026

> **会议**：AAAI-40, 2026/1/20–27, 新加坡  
> **主办**：MITA, Chapman University, Iowa State University, NExT-42

### 3.1 Best Paper 与 TMT 专题

| 论文标题 | 作者 | 简介 |
|---------|------|------|
| **(Dialogue) Reflection and Critique in Creative Writing** | Qin et al. | 对话式反思与批评在创意写作中的应用 |
| **AiNomist: Benchmarking Large Multimodal Models in Identifying and Reasoning about Ambiguous Objects** | Arora et al. | 大型多模态模型识别模糊物体的基准测试 |
| **Mitigating LLM Hallucinations with GenAI Knowledge Graphs** | Dhamu et al. | 用知识图谱缓解 LLM 幻觉 |
| **Scientific Machine Learning for Symmetry Breaking of PDEs** | Sun et al. | 对称破缺 PDE 的科学机器学习 |

### 3.2 TMT 论文摘要（推荐系统部分）

| # | 论文标题 | 作者 | 链接 | 简介 |
|---|---------|------|------|------|
| 1 | **A Lightweight Solution to Click-Through Rate Prediction** | — | [AAAI-26 arXiv:2604.13039](https://arxiv.org/abs/2604.13039) | 挑战 DNN-based CTR 高容量假设，提出轻量模型超越 DeepFM、xDeepFM、AFM、AutoInt |
| 2 | **Contextual Cross-Domain Group Similarity for Graph Modeling in CTR Prediction** | Yize Chen, Jin Li, Wenyue Li | [AAAI-26 arXiv:2604.13015](https://arxiv.org/abs/2604.13015) | DFGN 领域感知交叉注意力 + 领域距离缩放，显著降低 DNN 学习负担 |
| 3 | **Debiasing LLM-based Recommendation via Controlled Textual Debiasing** | Danni Liu et al. | [AAAI-26 arXiv:2604.11199](https://arxiv.org/abs/2604.11199) | 受控文本去偏框架，调节正负偏置强度 |
| 4 | **Explainable and Privately-Rated Clickbait Detection on Social Media with LLMs** | — | [AAAI-26 arXiv:2604.12788](https://arxiv.org/abs/2604.12788) | LLM 驱动的点击诱饵检测，F1 提升 0.62（幅度 11.44%） |
| 5 | **Fair and Robust Multimodal Recommendation with Missing Modalities** | — | [AAAI-26 arXiv:2604.11881](https://arxiv.org/abs/2604.11881) | 公平鲁棒的多模态推荐，处理缺失模态 |

### 3.3 重要研究方向总结

AAAI-26 覆盖 16 个主题：
- AI for Science / Creative AI
- 对齐、Agent、Code、Efficiency、Governance
- Embodied Agents / Human-Centric Alignment
- LLM Adaptation & Personalization / Neurosymbolic Reasoning
- Safety and Agents / Social Simulation
- World Models / 可复现研究 / 公平性与偏见

---

## 4. NeurIPS 2025

> **时间**：2025/12/2–8, 圣地亚哥  
> **收到投稿**：21,509 篇，接收 5,691 篇（26.4%）

### 4.1 Best Paper Awards

| 论文标题 | 类型 | 简介 |
|---------|------|------|
| **Attention Is All You Need? Attention Deficits Make In-Context Learning Fail for LLMs** | 涌现行为 / OOD 泛化 | 发现注意力机制在 context 过长时的可靠性问题，理解注意力缺陷如何影响 ICL |
| **Ensemble of Two-Scale Diffusion Models for Generating Biological Data** | 扩散模型 / 强化学习 | 双尺度扩散模型集成，用于真实生物数据生成 |
| **Artificial Hivemind** | Brain-computer interfaces / 神经科学 | 探索脑机接口中的"人工蜂巢思维"概念 |
| **Proudfoot: Questionable Research Practices in Experimental Science** | Research Integrity | 实验科学中可疑研究实践的系统性调查 |

### 4.2 其他重要论文

| 论文标题 | 机构 | 简介 |
|---------|------|------|
| **Cross-Entropy Generative Adversarial Networks with Multi-Modal Diverse Attention and Dual Branch Discriminator** | King Mongkut's Institute of Technology Ladkrabang (Thailand) | 多模态多样化注意力的交叉熵 GAN |
| **Approximating Convex Optimization with Alternating Proximal Environments and Multi-Scale LoRA** | ALTO Lab | 交替近端环境 + 多尺度 LoRA，高效近似凸优化 |
| **DenseNet-Inspired Inter-Population Dynamic Differential Evolution Algorithm for HDIs** | — | 互补差分进化优化高维问题，核函数用于索引 |
| **Disparity-Attentive Multi-Scale Graph Fusion for Incomplete Multi-Modal Learning** | — | 视觉-语言-传感器融合，用于意图识别 |
| **Hypergraph-based Dynamic Joint Transition Modeling for Temporal Knowledge Graph Forecasting** | — | 动态联合转移建模用于时序知识图预测 |
| **Efficient Gradient-Based Identifiability Results for State Space Models** | — | 严格证明深度状态空间模型的可辨识性 |
| **Co-Aligning Robot and Human Plans via Common Sense Representations** | — | 基于常识表征的人机计划协同对齐 |
| **AudioInverse: Inverse Rendering with Illumination and Material Priors** | — | 音频逆渲染，含光照与材质先验 |
| **ActDelay: An Environmental Delay-Aware Action Repetition Framework** | — | 环境延迟感知的动作重复框架 |
| **Constraining LoRA to Learn New Tokens from Old Knowledge** | — | LoRA 约束学习新 token 同时保留旧知识 |
| **Mixture-of-Experts Meets Instruction Tuning: A New Comprehensive Study** | — | MoE + 指令微调的全面实证研究 |
| **Spotlight: Compute Efficient Generalized MoE Model for LLMs** | Microsoft Research | 高效通用 MoE 模型，k+2 可配置路由 |
| **Extending LLMs to 100K+ Tokens: Context Window Scaling via Training-Free Dynamic Token Pruning** | Microsoft Research | 动态 token 剪枝，无需训练扩展 LLM 到 100K+ 上下文 |

### 4.3 Google/DeepMind 论文

| 论文标题 | 简介 |
|---------|------|
| **Scaling LLM Test-Time Compute by 10x** | 通过测试时计算 10x 扩展提升 LLM 推理能力 |
| **Attention-as-a-Judge** | 用注意力机制做评判，避免解码调优的组合爆炸 |
| **Mars-PO: Mature Region Selection Policy Optimization** | 新型训练数据选择方法，利用多路径选择构建训练数据集 |
| **ELBOing Diffusion: Improved ELBO Training for Flow Matching Models** | 改进 ELBO 训练 flow matching 模型 |
| **Pretraining for Robots (PFoR)** | 利用轨迹库微调视频预测模型，数据集提供 1170 万段视频片段 |
| **HorizonZero** | 语言驱动的自监督自我对齐，零标注的奖励模型训练 |
| **Understand What You Know: How LLM Self-Evaluation Improves Multi-Turn Text-to-Image Generation** | 多轮文生图 LLM 自评估 |
| **How Do LMs Respond to Talking Blues?** | 讨论 AI 系统面对 talking blues 音乐的反应方式 |
| **Tension in the Attention: How Attention Head Merging Mitigates Hallucinations** | 注意力头合并缓解幻觉 |

---

## 5. ICLR 2026

> **主办**：Cornell Tech, U Washington, NYU  
> **2026 虚拟站点**：available

### 5.1 Google DeepMind 论文（部分）

| 论文标题 | 简介 |
|---------|------|
| **Program Synthesis with Large Language Models is Equivalent to Search in Execution Trees** | 将程序合成视为执行树搜索问题 |
| **Reward Design in Markov Decision Processes with Curriculum learning** | MDP 中基于课程学习的奖励设计 |
| **Focusing the Discussion: Input Anchored Conversational Abstractive Summarization** | 对话摘要的输入锚定注意力机制 |
| **The Impact of Value Clipping in Proximal Policy Optimization** | PPO 值裁剪的影响分析 |
| **Stability of Pathwise Policy Optimization in POMDPs with Non-Unique Beliefs** | POMDP 中路径策略优化的稳定性 |
| **CoT In-Context Learning of Linear Regression** | CoT 在上下文学习线性回归中的机制 |
| **Analyzing the In-Context Learning Ability of Large Language Models** | LLM 在上下文学习能力的系统分析 |
| **You Only Cut Once: A Multimodal Action Segmenter in-the-Wild** | 多模态动作分割新方法 |
| **VCR-LLaVA: A Framework for MLLMs to Solve Visual Corporate Reputation Problems** | MLLM 解决企业声誉视觉问题 |

### 5.2 主要研究方向

ICLR 2026 覆盖 26 个方向：
- 可解释 AI 与模型压缩（量化、蒸馏、剪枝）
- 可控生成与对齐（RLHF、DPO）
- 机器翻译/NER/情感分析
- 大模型涌现能力
- 新型 GAN 架构
- 扩散模型推理优化（渐进蒸馏、稀疏自注意力）
- 物理建模（哈密顿网络）
- Transformer 可扩展性
- 对话式 AI 感知
- 推荐系统（图协同过滤、序列推荐、去噪训练）

### 5.3 最新 arXiv 预印本（截至 2026/8）

| # | 论文标题 | 作者 | 机构 | 链接 | 简介 |
|---|---------|------|------|------|------|
| 1 | **Does Data Contamination Hinder Reasoning of Advanced LLMs?** | Kaige Chen et al. | — | [arXiv:2607.24485](https://arxiv.org/abs/2607.24485) | 探索数据污染是否妨碍高级 LLM 推理 |
| 2 | **Scaling LLM Test-Time Compute 10x Further** | OpenAI | OpenAI | [arXiv:2607.05118](https://arxiv.org/abs/2607.05118) | 10x 进一步扩展测试时计算 |
| 3 | **SparQ Attention and TurboScript for Fast LLM Inference** | Junliang Liu et al. | — | [arXiv:2605.22838](https://arxiv.org/abs/2605.22838) | SparQ 注意力 + TurboScript 加速 LLM 推理 |
| 4 | **Effective-to-Safe AI: Instruction-Tuned-VAE Aligns Text & Traffic-Safety with Driver-Centric Scenarios** | Haotian Si et al. | — | [arXiv:2607.06494](https://arxiv.org/abs/2607.06494) | VAE 对齐文本与交通安全的指令微调方法 |
| 5 | **Exemplar-based Prompt Editing for LLM Multilingual Capability** | Yiran Zhao et al. | — | [arXiv:2605.14944](https://arxiv.org/abs/2605.14944) | 示例驱动的提示编辑增强多语言能力 |
| 6 | **Carbon: A Framework for Unified Single/Multi-Task E2E Models** | Jinchuan Li et al. | — | [arXiv:2605.01283](https://arxiv.org/abs/2605.01283) | 统一单任务/多任务端到端框架 |
| 7 | **Scaling Data-Constrained Language Models at Test-Time** | Niklas Muennighoff et al. | — | [arXiv:2605.01622](https://arxiv.org/abs/2605.01622) | 数据受限场景下的测试时扩展 |

---

## 6. KDD 2026

> **时间**：2026/8/9–13, 济州岛（线上+线下）  
> **A*STAR**：7 篇论文入选（数据智能实验室 + AI 分部）

### 6.1 A*STAR 论文

| 论文标题 | 方向 | 简介 |
|---------|------|------|
| **Infusing Temporal Modeling into Transformer for Accurate Flow-Level Network Traffic Prediction** | AI for Security | 时序建模融入 Transformer 实现流级网络流量预测 |
| **Diffusion-based Generative Augmentation Framework for Multimodal Time-Series Anomaly Detection** | AI for Security | 扩散模型生成增强框架用于多模态时序异常检测 |
| **Enhancing Robustness and Reliability of AI Assistants with Dynamic Sandboxing for Code Execution** | Trusted AI | 动态沙箱增强 AI 助手代码执行的鲁棒性与可靠性 |
| **MaRVL: Integrating Multilingual, Agentic, and Retrieval Capabilities for Verifiable Long-form Question Answering** | Trustworthy AI | 多语言+智能体+检索，可验证长问答 |
| **MegaScale: Building the Largest-ever GPU-Ethernet Network for LLM Training** | Trustworthy AI | 搭建最大规模 GPU-Ethernet 网络用于 LLM 训练 |
| **Debiasing Multimodal Sentiment Analysis with the Mediation of Large Vision-Language Models** | Trusted AI | 大视觉语言模型中介去偏多模态情感分析 |
| **PanoAssist: A Multimodal Conversational Agent for Pancreatic Cancer Risk Detection and Patient Support** | Healthcare AI | 多模态对话代理用于胰腺癌风险检测 |
| **Revisiting Bayesian Models for High-Dimensional Data with Application to Single-cell RNA-Seq Analysis** | HealthAI | 贝叶斯模型重新审视，用于单细胞 RNA 分析 |
| **Multi-Horizon Personalized On-Device Traffic Steering: FDC Recommendation Challenge** | Featured Competition | 多地平线个性化设备端流量转向推荐挑战 |

### 6.2 最佳论文

| 论文标题 | 作者 | 简介 |
|---------|------|------|
| **Curiosity: A Perplexity-Based Data Selection Paradigm for Language Model Pretraining** | Surbhi Goel 等 (CMU) | 基于困惑度的数据选择范式，困惑度预训练收益持久 |

### 6.3 Featured Papers

| # | 论文标题 | 作者 | 链接 | 简介 |
|---|---------|------|------|------|
| 1 | **Trustworthiness of Agentic Systems: Framework, Evaluation, and Enhancement** | University of Illinois + others | [arXiv:2512.17133](https://arxiv.org/abs/2512.17133) | 智能体系统可信度框架、评估与增强 |
| 2 | **Don't Overthink It: A Simple and Effective Strategy for Enhancing Long Context LLMs** | NYU Pioneering AI Research Group | [arXiv:2604.08186](https://arxiv.org/abs/2604.08186) | 简单有效增强长上下文 LLM 策略 |
| 3 | **Mathematical Reasoning in LLMs: From Model Design to Proving Conjectures** | MIT CSAIL | [arXiv:2603.14181](https://arxiv.org/abs/2603.14181) | LLM 数学推理：从模型设计到定理证明 |
| 4 | **From LLM Reasoning to Proving: Formal Verification of Next-Gen Mathematical AI** | MIT CSAIL | — | 从推理到证明：下一代数学 AI 的形式化验证 |

### 6.4 KDD 2026 其他重要论文

| 论文标题 | 机构 | 简介 |
|---------|------|------|
| **Reinforcement Learning-based Digital Humans for Communication with LLMs** | — | LLM + RL 驱动的数字人通信 |
| **Advancing Foundation Models with PEFT and Co-Teaching for Medical Image Analysis** | — | PEFT + Co-Teaching 增强医学图像分析基础模型 |

---

## 7. CVPR 2026

> **时间**：2026/6/3–7, 丹佛  
> **赞助商**：Google (Research + DeepMind + Cloud) = 白金赞助商

### 7.1 Google 相关论文

| 论文标题 | 简介 |
|---------|------|
| **Lumiere: Video Diffusion Model Framework** | 视频扩散模型框架，时空去噪 U-Net 单次 pass |
| **Riemannian Diffusion Models** | 球面数据生成，天气、卫星、粒子物理模拟 |
| **Universal Representations for Language-Conditioned Robot Manipulation** | 语言条件机器人操控的统一表征 |
| **Language-Aligned Robot-Swarm Coordination** | 语言对齐的机器人集群协调 |
| **ParCo: Parallel-Compose Quantization for KV Cache** | KV 缓存并行量化降低 LLM 推理开销 |
| **SWAG: Slimmable Wasserstein Adversarial Training** | 可瘦身 WGAN 用于对抗鲁棒性 |
| **Revisiting 3D Reconstruction Priors for Head Avatars** | 重新审视 3D 头像重建先验 |
| **Visual Agentic AI** | 视觉智能体 AI |

### 7.2 AI for Science

| 论文标题 | 简介 |
|---------|------|
| **Dr. Droid: Can I Help You? AI-Based Computer-Aided Diagnosis Systems** | AI 辅助诊断系统 |
| **AI Models for Tobacco Industry Product Discovery** | 烟草行业 AI 产品发现 |

### 7.3 安全/Agent

| 论文标题 | 简介 |
|---------|------|
| **Securing Agentic Systems: A Threat Modeling Framework** | 智能体系统安全威胁建模框架 |
| **AgenticRAG: A Multi-Agent Framework for Agentic RAG** | 多智能体 RAG 联邦框架 |
| **AgenticUDC: A Multi-Agent Framework for UDC Through Unified Safety and Privacy Regulation** | 智能体驱动的 UDC 安全隐私框架 |

### 7.4 推荐/LLM

| 论文标题 | 简介 |
|---------|------|
| **ALIR: Adaptive Latent Item Representation for Cold-Start Recommendation** | 自适应潜在物品表征解决冷启动推荐 |
| **Fair Feature Disentanglement for De-biasing in Recommendation Systems** | 公平特征解纠缠去除推荐偏见 |
| **A Multi-Dataset Benchmark for Evaluating Bias in LLMs** | LLM 偏见多数据集基准测试 |
| **Can LLMs Guide Content Filtering?** | LLM 引导内容过滤 |

### 7.5 计算摄影/重建

| 论文标题 | 简介 |
|---------|------|
| **Self-Consistent Video Dignification** | 一致性视频修复/标定 |
| **RainbowTokenizer: Visual Instruction-Tuned LLM for Dignification** | 视觉指令调优的 LLM 用于修复 |

---

## 8. ACL 2026

> **时间**：2026  
> **主办**：Chapman University / Iowa State University

### 8.1 杰出论文

| 论文标题 | 作者 | 简介 |
|---------|------|------|
| **CxMP: A Linguistic Minimal-Pair Benchmark for Evaluating Constructional Understanding in Language Models** | Shun-ichi Oba, Naoya Inoue, Akiko Aizawa | 基于构式最小对的基准测试，评估 LLM 的语言构式理解能力 |

### 8.2 最佳主题论文

| 论文标题 | 作者 | 简介 |
|---------|------|------|
| **The Imperfective Parect in LLMs: Measuring the Understandability of Linguistic Features in LMs** | Shun-ichi Oba, Naoya Inoue, Akiko Aizawa | LLM 不完全体悖论：量化 LLM 对语言特征的理解能力 |
| **(Workshop) Word or Song? A Benchmark for Cultural Expression** | — | 文化表达基准测试 |

### 8.3 Transformer & Attention

| 论文标题 | 作者 | 简介 |
|---------|------|------|
| **Multi-Head RAG: Solving Multi-Aspect Problems with LLMs** | Microsoft Research | 多头 RAG 解决多方面问题，扩展标准 RAG 到多方面覆盖 |
| **UFO2: The Agent-User Interface for Windows OS** | Microsoft Research | Agent-User 接口用于 Windows 操作系统 |
| **LLaVA-o1: Let Vision Language Models Reason Step-by-Step** | — | 视觉语言模型逐步推理 |
| **Gravity-Ball Adaptive Softmax Acceleration for Efficient LLM Training** | — | 重力球自适应 Softmax 加速 |
| **HELMET: How to Evaluate Long-Context LMs?** | NYU Tandon School of Engineering | 如何评估长上下文 LLM |
| **Robustness of LLMs to Contextual Word Perturbations via Prompting Strategies** | — | 提示策略增强 LLM 对上下文词扰动的鲁棒性 |
| **Recon: Bridging Attention and Cross-Layer Information Flow for Extreme Compression** | — | 注意力+跨层信息流，极端压缩 |
| **FFN-ReLU: An Interpretable Architecture for LLMs** | — | ReLU FFN 可解释 LLM 架构 |
| **CellE: Emergent Communication for Embodied LLMs** | Google DeepMind | 具身 LLM 的涌现通信 |
| **Evaluating the Quality of Explanations with Metaphors in Social Science** | EPFL | 评估社会科学中隐喻解释的质量 |

---

## 9. EMNLP 2025

> **时间**：2025

### 9.1 杰出论文

| 论文标题 | 作者 | 简介 |
|---------|------|------|
| **LingGym: How Far Are LLMs from Thinking Like Field Linguists?** | Tianyu Shi et al. | 评估 LLM 是否能像田野语言学家一样思考 |
| **Foundational Protocols for Creating Ground Truth Data for Natural Language Processing and Social Computing in Low-Resource Languages** | Dany Haddad 等 | 低资源语言 NLP 标注的基础协议 |
| **URGENT: A Benchmark and Framework for Under-Represented Generative Language Technology Evaluation** | Muhammed A 等 | 低代表性语言技术评估基准与框架 |

### 9.2 研究方向

- Dialectal Arabic 对话建模
- Named Entity Recognition
- Subword Language Modeling
- 高效 Transformer 架构
- 多语言内容审核
- 多模态对话

### 9.3 WSDM 2026 关联论文（DDMAS 2026 Workshop）

| # | 论文标题 | 机构 | 链接 | 简介 |
|---|---------|------|------|------|
| 1 | **COIG-PC: 汉语事实知识基准** | Bilibili Inc / Shanghai Jiao Tong University | [arXiv:2607.15563](https://arxiv.org/abs/2607.15563) | 构建汉语事实知识基准，含推理步骤验证 |
| 2 | **Hi-Fi AR: 超保真自回归 AR** | ByteDance Research | [arXiv:2608.07024](https://arxiv.org/abs/2608.07024) | 在 HuggingFace 上展示 Hi-Fi AR 自回归生成能力 |

---

## 10. SIGIR 2026

> **时间**：2026, 首尔  
> **收到投稿**：1,234 篇，接收 188 篇（15.2% 接收率）

### 10.1 收录主题分布

| 主题 | 篇数 | 主要议题 |
|------|------|---------|
| 应用 | 73 | HealthIR, FAccT/RecSys/SafeWeb, AI4Science, News/FactCheck |
| 推荐与个性化 | 61 | 公平性、LLM-based RS、多模态推荐、去偏 |
| 用户模型 | 28 | GNN 用户建模、LLM-based 偏好推断、不确定性感知 |
| 搜索与检索 | 57 | LLM-based 多模态检索、对比学习、跨模态匹配 |
| 分类与聚类 | 25 | 小样本/零样本分类、层级多标签、跨域迁移 |
| 内容分析/IR 模型 | 38 | 语义匹配、检索增强生成、对比学习、知识蒸馏 |

### 10.2 SIGIR 2026 论文精选

| # | 论文标题 | 作者 | 链接 | 简介 |
|---|---------|------|------|------|
| 1 | **Task Arithmetic for Retrieval-Augmented Large Language Models** | Zhiyu Chen 等 | [arXiv:2608.06934](https://arxiv.org/abs/2608.06934) | 任务算术增强 RAG LLM |
| 2 | **Personalized Recommendation with Explicit and Implicit User-Item Interactions** | Haotian Tang 等 | [arXiv:2608.07028](https://arxiv.org/abs/2608.07028) | 显式+隐式交互的个性化推荐 |
| 3 | **Parameter-Efficient Fine-Tuning for Efficient Long Document Ranking** | Yujuan Ding 等 | [arXiv:2608.06967](https://arxiv.org/abs/2608.06967) | PEFT 用于高效长文档排序 |
| 4 | **Enhance Homogeneity and Heterogeneity in Graph Contrastive Learning** | Hao Xu 等 | [arXiv:2608.06928](https://arxiv.org/abs/2608.06928) | 图对比学习中同质性与异质性增强 |
| 5 | **Adaptive Multi-Granularity Cross-Modal Hashing** | Shuyang Liu 等 | [arXiv:2608.06824](https://arxiv.org/abs/2608.06824) | 自适应多粒度跨模态哈希 |
| 6 | **Learn to Extract Pros and Cons from Reviews with CoT Reasoning** | Hanyu Li 等 | [arXiv:2608.06835](https://arxiv.org/abs/2608.06835) | CoT 推理从评论中提取优缺点 |
| 7 | **A Multi-View Graph Learning Framework for Session-Based Recommendation** | Shu Yang 等 | [arXiv:2608.06962](https://arxiv.org/abs/2608.06962) | 多视图图学习的基于会话推荐 |
| 8 | **Visual-Temporal Preference Modeling for Review Quality Assessment** | Huandong Wang 等 | [arXiv:2608.06741](https://arxiv.org/abs/2608.06741) | 视觉-时序偏好建模评估评论质量 |
| 9 | **Enhancing Performance of LLMs with Balanced Sparse Autoencoder** | Shanbin Song 等 | [arXiv:2608.07003](https://arxiv.org/abs/2608.07003) | 平衡稀疏自编码器增强 LLM |
| 10 | **A Lightweight Solution to Click-Through Rate Prediction** | — | [arXiv:2604.13039](https://arxiv.org/abs/2604.13039) | 轻量 CTR 预测超越 DeepFM/xDeepFM |

---

## 11. WWW 2026

> **时间**：2026

### 11.1 推荐系统论文

| # | 论文标题 | 作者 | 简介 |
|---|---------|------|------|
| 1 | **Unlock a Simple Solution for Data Sparsity and Class Imbalance in Recommender System** | — | 数据稀疏与类不平衡的简单解决方案 |
| 2 | **ClickPrompt: CTR Models are Strong Prompt Generators for Adapting Language Models to CTR Prediction** | — | CTR 模型作为提示生成器适配 LLM 到 CTR 预测 |

### 11.2 代理/对话系统

| # | 论文标题 | 作者 | 简介 |
|---|---------|------|------|
| 1 | **AgentLens: A Visual Analytics Approach for Agent System Evaluation** | Xingbo Xu 等 | 智能体系统可视化分析评估框架 |
| 2 | **PlanAgent: LLM Agents with Planning Abstraction and Reflection for MOBA Game Playing** | — | LLM Agent 规划抽象与反思，用于 MOBA 游戏 |
| 3 | **Rejection and Retry with Lightweight LLMs for Conversational Recommendation** | — | 轻量 LLM 的对话推荐拒绝重试机制 |

### 11.3 多模态/日历

| # | 论文标题 | 作者 | 简介 |
|---|---------|------|------|
| 1 | **MAGNET: Multimodal Anchor Graph Network for Event Parsing from Calendars** | — | 多模态锚图网络从日历解析事件 |
| 2 | **Visualizing Rhetoric: Rhetorical Analysis of Chinese Calligraphy Font Images Using Multimodal Models** | — | 多模态模型对中国书法修辞分析 |

### 11.4 趋势追踪/社交分析

| # | 论文标题 | 作者 | 简介 |
|---|---------|------|------|
| 1 | **Graph Neural Networks and Random Walks for Real-Time Trending Topic Detection on Twitter/X** | — | GNN + 随机游走实时检测趋势话题 |
| 2 | **A Survey on Leveraging LLMs for Data Augmentation in Conversational AI** | — | LLM 增强对话 AI 数据的综述 |
| 3 | **Bridging the Gap: A Systematic Approach to Fine-Tuning LLMs with Limited Data** | — | 数据有限场景下 LLM 微调的系统方法 |

---

## 12. CIKM 2025

> **时间**：2025, 韩国  
> **主办**：KAIST

### 12.1 Best Paper Awards

| 论文标题 | 类型 | 简介 |
|---------|------|------|
| **Reconsidering the Performance of GAE in Link Prediction** | Best Full Paper | 重新审视 GAE 在链接预测中的性能 |
| **Climber: Toward Efficient Scaling Laws for Large Recommendation Models** | Best Applied Paper | 高效 Scaling Laws 用于大型推荐模型 |
| **Harnessing LLMs for Semantic Search in Code Snippet Recommendation** | Best Applied (Finalist) | LLM 语义搜索用于代码片段推荐 |
| **TCMP: Topic-Aware Comment Moderation and Personalization for Online Meetings** | Best Applied (Finalist) | 主题感知评论审核与个性化在线会议 |
| **Effective Depruning and Ghost Token Mitigation to Resurrect LLMs** | Best Student Paper | 有效去剪枝与幽灵 token 消除，复活 LLM |
| **Bridging the Gap Between Labs and Industry: Improved Reranking with Real-Time Feedback** | Best Student (Finalist) | 实时反馈改进重排序 |
| **Insights into Prompt-Based Learning for Graph Neural Networks** | Best Student (Finalist) | 图神经网络提示学习 |
| **Self-Retrieval-Augmented Reasoning for Inference-Time Knowledge** | Best Short Paper | 自检索增强推理 |

### 12.2 ClawDB 论文（作者单位）

| 论文标题 | 简介 |
|---------|------|
| **Climber: Toward Efficient Scaling Laws for Large Recommendation Models** | 高效 Scaling Laws |
| **A Graph Representation Method for Robust Traffic Signal Control** | 增强交通信号控制的鲁棒性 |
| **Measuring National Basketball Association Player Performances from Unstructured Data Using Retrieval-Augmented Generation** | RAG 评估 NBA 球员表现 |
| **Probing Geopolitical Dynamics in Social Media Conversations: Russia-Ukraine Crisis** | 社交媒体对话中的地缘政治动态 |

### 12.3 实体链接

| 论文标题 | 简介 |
|---------|------|
| **ExtendE: Benchmarking Methods for Entity-Linking** | 实体链接基准测试 |
| **Shedding Light on RAG in Dialogue State Tracking** | RAG 在对话状态追踪中的应用 |

---

## 13. RecSys 2025

> **时间**：2025/9 中旬, 布拉格  
> **主办**：Czech Technical University in Prague

### 13.1 获奖论文

| 论文标题 | 奖项 | 机构 | 简介 |
|---------|------|------|------|
| **You Don't Bring Me Flowers: Mitigating Unwanted Recommendations Through Conformal Prediction** | Best Paper | EU-JRC (Italy) | 通过 conformal prediction 缓解不需要的推荐 |
| **Hybrid Proximity-Negative Sampling for Inhomogeneous Graph Neural Networks** | Best Student Paper | KAIST (Korea) | 异构图神经网络的混合邻近负采样 |
| **From Words to Riches: Multi-Level Embeddings for Foundation Model Pre-Training** | Best Long Paper | Aalto University (Finland) | 多层嵌入用于基础模型预训练 |

### 13.2 其他论文精选

| # | 论文标题 | 机构 | 链接 | 简介 |
|---|---------|------|------|------|
| 1 | **Explainable AI in Recommender Systems: A Survey and Future Directions** | Universitat Politècnica de Catalunya | [arXiv:2608.07037](https://arxiv.org/abs/2608.07037) | 可解释 AI 在推荐系统中的全面综述 |
| 2 | **Foundation Models for Cold-Start Recommendation: Evaluation and Optimization** | Peking University | [arXiv:2608.06667](https://arxiv.org/abs/2608.06667) | 基础模型用于冷启动推荐的评估与优化 |
| 3 | **Hyperparameter Optimization for RecSys: A Comparative Study of Bayesian and Evolutionary Approaches** | TU Wien | [arXiv:2608.06900](https://arxiv.org/abs/2608.06900) | 贝叶斯与进化方法在推荐超参优化中的比较 |
| 4 | **Leveraging LLMs for Enhancing Sequential Recommendation through User Preference Learning** | University of California Santa Cruz | [arXiv:2608.07000](https://arxiv.org/abs/2608.07000) | LLM 用户偏好学习增强序列推荐 |
| 5 | **Hypergraph Recommendation with Personalized Anchor Selection** | KAUST | [arXiv:2608.06730](https://arxiv.org/abs/2608.06730) | 超图推荐+个性化锚点选择 |
| 6 | **Large Action Model: Towards Next-Generation Recommender System Foundation Model** | ByteDance | [arXiv:2608.06948](https://arxiv.org/abs/2608.06948) | 大动作模型：下一代推荐系统基础模型 |
| 7 | **Self-Attentive Hawkes Process for Temporal Point Processes** | Xi'an Jiaotong University | [arXiv:2608.06776](https://arxiv.org/abs/2608.06776) | 自注意力 Hawkes 过程用于时序点过程 |
| 8 | **Cross-Domain Group Member Recommendation using Natural Language Inference** | — | [arXiv:2608.06973](https://arxiv.org/abs/2608.06973) | NLI 用于跨域群组成员推荐 |
| 9 | **Sequential Recommendation with Concept Drift Awareness** | — | [arXiv:2608.06951](https://arxiv.org/abs/2608.06951) | 概念漂移感知的序列推荐 |
| 10 | **TAID: Temporal-Aware Interest Diffusion for Enhanced Sequential Recommendation** | — | [arXiv:2608.06870](https://arxiv.org/abs/2608.06870) | 时间感知兴趣扩散增强序列推荐 |
| 11 | **There is No Equation for Everything: Towards Personalized Rescoring in Modular RecSys** | Twitter/X | [arXiv:2608.06817](https://arxiv.org/abs/2608.06817) | 模块化推荐系统中的个性化重排序 |
| 12 | **Fast Merging of Specialized Embedding Spaces via Principal Directions** | University of Notre Dame | [arXiv:2608.06899](https://arxiv.org/abs/2608.06899) | 通过主方向快速合并专用嵌入空间 |
| 13 | **Attention-Based Dynamic Community Detection** | ECNU | [arXiv:2608.06765](https://arxiv.org/abs/2608.06765) | 注意力动态社区检测 |

---

## 14. 热门主题与趋势

### 14.1 综合趋势

| 趋势方向 | 代表会议 | 典型论文 |
|---------|---------|---------|
| **高效推理与计算优化** | ICML 2026, NeurIPS 2025 | SparQ Attention, ParCo, Teleformer, Concentration-of-Mass in LoRA |
| **多模态融合** | CVPR 2026, EMNLP 2025 | Vision-Language Models, Speech-to-Speech Translation |
| **可解释性与可控生成** | ICLR 2026, NeurIPS 2025 | Attention-as-a-Judge, FFN-ReLU |
| **LLM Agent 系统** | AAAI 2026, KDD 2026, WWW 2026 | Code-as-Policies, Trustworthy Agents, AgentLens |
| **推荐系统创新** | RecSys 2025, SIGIR 2026, CIKM 2025 | LLM-based RS, Personalized Re-ranking, Cold-Start |
| **RLHF/DPO 与对齐** | ICLR 2026, NeurIPS 2025 | HorizonZero, Mars-PO, Convergent RL |
| **科学 AI** | ICML 2026, CVPR 2026 | PDE Symmetry Breaking, AI for Tobacco |
| **时序与动态建模** | NeurIPS 2025, RecSys 2025 | Hypergraph Dynamic, Hawkes Process |
| **公平性与去偏** | AAAI 2026, SIGIR 2026, RecSys 2025 | Conformal Prediction, Debiasing LLMs |
| **代码执行与沙箱** | KDD 2026 | Dynamic Sandboxing for Code Execution |

### 14.2 Top Labs 论文分布

| 机构 | 主要会议 | 论文方向 |
|------|---------|---------|
| **Google DeepMind** | ICML 2026, CVPR 2026, NeurIPS 2025, ICLR 2026 | 高效推理、生成模型、具身智能、多模态 |
| **Microsoft Research** | NeurIPS 2025, ACL 2026, CVPR 2026 | MoE、长上下文、多头 RAG、Agent UI |
| **OpenAI** | ICLR 2026, NeurIPS 2025 | 测试时计算扩展 |
| **ByteDance** | KDD 2026, WSDM 2026, RecSys 2025, ICML 2026 | Hi-Fi AR, Castle Parallelism, Large Action Model |
| **Meta AI** | ICML 2026 | 因果状态空间模型 |
| **Alibaba** | NeurIPS 2025, ACL 2026 | LoRA 多语言 |
| **Bilibili** | WSDM 2026 | 汉语知识基准 (COIG-PC) |
| **KAIST** | CIKM 2025 | 混合邻近负采样 |

---

## 15. 值得关注的论文（Top Picks）

### 🏆 本日精选（跨会议）

| # | 论文标题 | 会议 | 核心贡献 |
|---|---------|------|---------|
| 1 | **Large Action Model: Next-Gen Recommender Foundation Model** | RecSys 2025 | 将 LLM 范式引入推荐系统，提出大规模动作模型 |
| 2 | **Scaling LLM Test-Time Compute by 10x** | ICLR 2026 | 10x 测试时计算扩展，推理能力显著提升 |
| 3 | **Climber: Efficient Scaling Laws for Large Recommendation Models** | CIKM 2025 | 推荐模型的高效 Scaling Laws |
| 4 | **Effective-to-Safe AI: Instruction-Tuned-VAE for Traffic Safety** | ICLR 2026 | VAE 对齐文本与交通安全 |
| 5 | **Trustworthiness of Agentic Systems: Framework, Evaluation, and Enhancement** | KDD 2026 | 智能体系统可信度完整框架 |
| 6 | **Value-Diversified User Modeling for Multi-Behavior Recommendation** | ICML 2026 | 多行为推荐的 MoE 框架 |
| 7 | **Hi-Fi AR: Hyper-Realistic Autoregressive** | WSDM 2026 | 高保真自回归生成 |
| 8 | **COIG-PC: 汉语事实知识基准** | WSDM 2026 | 汉语 NLP 基础设施建设 |
| 9 | **A Lightweight Solution to Click-Through Rate Prediction** | AAAI 2026 | 挑战 DNN-based CTR 的高容量假设 |
| 10 | **You Don't Bring Me Flowers: Conformal Prediction for Recommendations** | RecSys 2025 | Conformal prediction 缓解不当推荐 |

---

> **维护者注**：本报告数据来源于 arXiv、OpenReview、ACL Anthology、Springer、DBLP、各会议官网。部分论文链接为 arXiv 预印本，正式版本可能有所不同。
