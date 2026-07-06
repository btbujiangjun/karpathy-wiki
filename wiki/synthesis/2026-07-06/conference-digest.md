---
title: "顶会论文专题报告 — 2026年7月全面版"
type: synthesis
created: 2026-07-06
updated: 2026-07-06
sources: [arxiv.org, openreview.net, paperdigest.org, papercopilot.com, icml.cc, iclr.cc, neurips.cc, aaai.org, cvpr.thecvf.com, kdd.org, aclweb.org, sigir.org]
tags: [conference-digest, icml-2026, aaai-2026, neurips-2025, iclr-2026, cvpr-2026, kdd-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2025, recsys-2025, llm, ctr, recommendation, agents, games, generative-models, benchmarks]
---

# 顶会论文专题报告 — Conference & arXiv Digest

> **2026年7月6日更新** | 覆盖 12+ 顶会/期刊, 80+ 精选论文, 15+ 研究机构
> 涵盖: LLM 架构与训练, 推荐系统 & CTR, 智能体系统, 游戏 AI, 扩散模型, 代码推理, 基准测试

---

## 目录

1. [ICML 2026 — 机器学习国际会议](#1-icml-2026)
2. [NeurIPS 2025 — 神经信息处理系统大会](#2-neurips-2025-best-paper-awards)
3. [ICLR 2026 — 学习表征国际会议](#3-iclr-2026)
4. [AAAI 2026 — 人工智能促进会](#4-aaai-2026)
5. [CVPR 2026 — 计算机视觉与模式识别](#5-cvpr-2026)
6. [KDD 2026 — 知识发现与数据挖掘](#6-kdd-2026)
7. [ACL 2026 & EMNLP 2025 — 自然语言处理](#7-acl-2026--emnlp-2025)
8. [SIGIR 2026 & WWW 2026 — 信息检索与万维网](#8-sigir-2026--www-2026)
9. [CIKM 2025 & RecSys 2025 — 信息与知识管理 / 推荐系统](#9-cikm-2025--recsys-2025)
10. [推荐系统 & CTR 预测 — 工业界前沿](#10-推荐系统--ctr-预测--工业界前沿)
11. [LLM 架构与训练 — 2026 前沿进展](#11-llm-架构与训练--2026-前沿进展)
12. [智能体系统 (Agents)](#12-智能体系统-agents)
13. [游戏 AI & 强化学习](#13-游戏-ai--强化学习)
14. [生成模型 & 扩散语言模型](#14-生成模型--扩散语言模型)
15. [代码推理 & 形式化验证](#15-代码推理--形式化验证)
16. [基准测试 & 评估](#16-基准测试--评估)

---

## 1. ICML 2026

**时间**: 2026年7月6-11日 | **地点**: COEX, Seoul, South Korea
**规模**: 接受论文 6,500+ 篇 (历史最高); ICML 三大顶会之一 (与 NeurIPS, ICLR 并列)

### 1.1 ICML 2026 最佳论文 & 亮点

#### Attention Sink Forges Native MoE in Attention Layers
- **作者**: Zizhuo Fu 等
- **机构**: Meng Li 团队
- **核心贡献**: 提出 Sink-Aware Training 方法解决注意力头坍缩问题, 在注意力层中实现原生 MoE 结构
- **背景**: Transformer 注意力头在训练中往往出现冗余和坍缩, 形成"注意力下沉 (attention sink)"现象, 即模型将大量注意力分配给无关标记
- **方法**: 通过检测和利用 attention sink 模式, 在注意力层中自然地形成专家路由, 无需额外 MoE 路由网络
- **实验结果**: 在语言建模和下游任务上取得显著改进

#### TEAM: Temporal–Spatial Consistency Guided Expert Activation for MoE Diffusion
- **作者**: Linye Wei 等
- **机构**: Meng Li 团队
- **核心贡献**: 为 MoE 扩散语言模型加速设计时空一致的专家激活策略
- **方法**: 利用扩散过程的时间一致性指导专家路由选择, 显著减少推理时的专家切换开销
- **实验结果**: 在保持生成质量的同时实现 2-3x 推理加速

#### HyPER: Bridging Exploration and Exploitation for Scalable LLM Reasoning
- **作者**: Shengxuan Qiu, Haochen Huang 等
- **机构**: Meng Li 团队
- **核心贡献**: 提出假设路径扩展与缩减 (Hypothesis Path Expansion and Reduction) 方法
- **方法**: 结合树搜索的探索能力与贪心解码的开发特性, 通过动态路径缩减控制推理成本
- **实验结果**: 在数学推理、代码生成等任务上超越标准 CoT 和 ToT 方法

### 1.2 ICML 2026 强化学习 & 推理方向

#### ResRL: Boosting LLM Reasoning via Negative Sample Projection Residual Reinforcement Learning
- **arXiv**: [2605.00380](https://arxiv.org/abs/2605.00380)
- **作者**: Zihan Lin 等
- **核心贡献**: 提出残差强化学习 (ResRL) 解决 RLVR 中正样本过激励导致的多样性下降问题
- **方法**: 通过 SVD 将负样本隐表示投影到正样本低秩子空间, 用投影残差调节负梯度, 保留正负样本共享语义的同时惩罚真正有害的偏差
- **理论**: 将 Lazy Likelihood Displacement (LLD) 与正负梯度干扰建立了理论联系
- **实验结果**: 在 12 个基准测试 (数学/代码/Agent/函数调用) 上平均优于基线; 数学推理上 Avg@16 提升 9.4%, Pass@128 提升 7.0%

#### Stratified GRPO: Handling Structural Heterogeneity in RL of LLM Search Agents
- **核心贡献**: 提出分层 GRPO 算法, 对 LLM 搜索智能体中结构异构的搜索路径进行精细的组间相对偏好优化
- **方法**: 将搜索轨迹按结构特征 (路径长度、分支数等) 分层, 在各层内分别应用 GRPO

#### Just-In-Time Reinforcement Learning: Continual Learning in LLM Agents Without Gradient Updates
- **核心贡献**: 提出无需梯度更新的持续学习方法, 通过上下文记忆和奖励信号缓存实现 LLM Agent 的即时强化学习
- **方法**: 在推理时维护经验缓存, 使用非参数方法更新策略

### 1.3 ICML 2026 LLM Agent 论文 (59篇)

#### 代表性论文:
- **AgentXRay: White-Boxing Agentic Systems via Workflow Reconstruction** — 使用 MCTS 从黑盒 Agent 系统中重建等效白盒工作流, 实现可解释性
- **Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control** — 对 Agent 系统的过度承诺问题建模, 提出校准的声明级特异性控制
- **AutoRPA: Efficient GUI Automation through LLM-Driven Code Synthesis** — 自动将 ReAct 风格 GUI Agent 交互轨迹蒸馏为可复用 RPA 函数, 节省 82-96% token
- **Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information** — 利用一阶精度信息和二阶相关性信息聚合 LLM 响应, 证明优于多数投票
- **A Minimal Agent for Automated Theorem Proving (AxProverBase)** — 仅用"编译器反馈+自管理笔记本+轻量工具搜索"三组件, 用未微调的前沿 LLM 超越专用系统, 成本降低 100 倍
- **NSI: Neuro-Symbolic Skill Induction** — 将 LLM Agent 交互轨迹提升为带条件分支和动态变量绑定的神经符号工作流图
- **Position: The AI Imperative: Scaling High-Quality Peer Review in ML** — 呼吁用 AI 提升 ML 领域同行评审质量和规模

### 1.4 ICML 2026 其他亮点

#### Shannon Scaling Law: LLMs as Noisy Channels
- **已在 Wiki 中**: [Shannon Scaling Law](../../papers/llm-training/shannon-scaling-law.md)
- **核心**: 将 LLM 视为噪声信道, 推导出新的 scaling law, 解释模型规模与数据质量之间的交互

#### Self-Supervised Flow Matching (Self-Flow)
- **核心**: 无需配对数据的自监督流匹配训练方法, 可应用于生成建模

#### Principled Synthetic Data Enables Scaling Laws for LLMs in Recommendation
- **作者**: Meta
- **核心**: 首次为基于 LLM 的推荐系统建立可预测的 scaling law

---

## 2. NeurIPS 2025 Best Paper Awards

**时间**: 2025年11月30日-12月7日 (San Diego + Mexico City 双城)
**规模**: 5,290 篇接受论文, 21,575 篇投稿

### 2.1 Best Papers (4篇)

#### 🏆 Gated Attention for Large Language Models
- **作者**: Zihan Qiu 等 (Qwen Team, Alibaba)
- **arXiv**: [2505.06708](https://arxiv.org/abs/2505.06708)
- **中文**: 门控注意力 — 非线性、稀疏性与消除注意力下沉
- **核心贡献**: 系统研究 30+ 种门控注意力变体, 发现在 SDPA 输出后添加 head-specific sigmoid 门控一致提升性能
- **已应用于**: Qwen3-Next 模型, 开源代码已发布
- **关键发现**:
  - 在 15B MoE 和 1.7B Dense 模型上训练 3.5T token 进行全面对比
  - PPL 降低 0.05-0.27 (取决于配置)
  - BOS token 注意力从 46.7% 降至 4.8% (attention sink 几乎消除)
  - 训练稳定性显著提升, 可容忍更大学习率
  - 长上下文外推能力增强
  - 门控仅增加 <2% 延迟
- **NeurIPS 评选委员会评论**: "该论文的主要建议易于实现, 鉴于提供的广泛证据, 预计这一想法将被广泛采用"

#### 🏆 Artificial Hivemind: The Open-Ended Homogeneity of Language Models
- **作者**: Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Yejin Choi
- **机构**: University of Washington, CMU, Allen Institute for AI, Lila Sciences, Stanford
- **核心贡献**: 揭示 LLM 的"人工蜂群思维"效应 — 单个模型内和跨模型间输出高度同质化
- **数据集**: Infinity-Chat — 26,000 个开放式查询 + 31,000+ 人工标注
- **关键发现**: 70+ 个模型测试显示相同模式; 当前模型与个人偏好对齐不良; 长期风险包括创造力丧失和价值多元化降低

#### 🏆 1000 Layer Networks for Self-Supervised RL
- **作者**: Kevin Wang, Ishaan Javali 等
- **核心贡献**: 成功将自监督 RL 网络扩展到 1024 层, 实现 2-50x 性能提升
- **突破**: 打破"RL 与深层网络不兼容"的假设; 机器人无需人类示教即可学习复杂目标
- **方法**: 使用对比式目标条件自监督 (contrastive RL), actor-critic 架构

#### 🏆 Why Diffusion Models Don't Memorize: Implicit Dynamical Regularization
- **核心贡献**: 从理论角度证明扩散模型的隐式动力正则化机制解释了其不记忆训练数据的特性
- **意义**: 为扩散模型在隐私敏感场景的部署提供了理论基础

### 2.2 Runners-Up (3篇)

#### Explaining Scaling Laws via Superposition
- **核心贡献**: 证明表征叠加 (representation superposition) 是神经 scaling law 的主要驱动机制
- **方法**: 通过受控"玩具模型"研究叠加如何随模型规模影响损失缩放
- **关键发现**: 开放 LLM 工作在强叠加区, 损失随模型维度呈逆幂律缩放; Chinchilla scaling law 与此行为一致

#### (其他2篇 Runner-Up 论文: 涵盖在线学习理论和推理极限研究)

---

## 3. ICLR 2026

**时间**: 2026年4月 (巴西)
**规模**: 接受论文 5,300+ 篇; Oral 论文 223 篇

### 3.1 ICLR 2026 Oral 代表论文

#### Common Corpus: The Largest Collection of Ethical Data for LLM Pre-Training
- **核心**: 构建最大规模合规预训练数据集, 解决版权和伦理问题
- **意义**: 为开放 LLM 研究提供关键基础设施

#### Q-RAG: Long Context Multi-Step Retrieval via Value-Based Embedder Training
- **核心**: 提出基于价值的嵌入器训练方法, 实现长上下文多步检索

#### Why DPO is a Misspecified Estimator and How to Fix It
- **核心**: 证明 DPO (Direct Preference Optimization) 是错误指定的估计量, 并提出修正方法
- **意义**: 对偏好对齐领域的理论基础产生深远影响

#### SafeDPO: Enhanced Safety with Direct Preference Optimization
- **核心**: DPO 的安全增强版本, 在保持对齐性能的同时提高输出安全性

#### Efficient Autoregressive Inference for Transformer Probabilistic Models
- **机构**: University of Helsinki
- **核心**: 提出 Transformer 概率模型的高效自回归推理方法

### 3.2 ICLR 2026 其他亮点

#### SigLIP-HD By Fine-to-Coarse Supervision
- **核心**: 从细到粗的监督策略提升 SigLIP 高分辨率理解能力

#### ERGO: Efficient High-Resolution Visual Understanding for Vision-Language Models
- **核心**: 高效高分辨率视觉理解的 VLM 方法

#### Critique-Coder: Enhancing Coder Models by Critique Reinforcement Learning
- **核心**: 通过批评式强化学习增强代码模型能力

#### WebGen-Agent: Enhancing Interactive Website Generation
- **核心**: 多级反馈与逐步强化学习提升网站生成智能体

---

## 4. AAAI 2026

**时间**: 2026年1月20-27日 | **地点**: Singapore
**规模**: 23,680 篇投稿, 4,167 篇接受 (接受率 17.6%); 近 29,000 篇提交至主赛道, 约 23,000 篇合规审查

### 4.1 统计亮点
- 中国贡献约 20,000 篇投稿
- 三大研究领域: 计算机视觉、机器学习、自然语言处理
- 评审委员会扩展至 28,000+ 成员 (前一年的 3 倍)
- 新增 AI Alignment 和 AI for Social Impact 特设轨道

### 4.2 代表论文

#### FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play Reconstruction-based Token Pruning
- **机构**: XPeng Motors + Peking University
- **核心**: 为端到端自动驾驶 VLA 模型定制的高效视觉 token 剪枝框架
- **方法**: 基于重建的即插即用 token 剪枝, 减少视觉编码器的计算开销

#### ExpertAD: Enhancing Autonomous Driving Systems with Mixture of Experts
- **arXiv**: [2511.11740](https://arxiv.org/abs/2511.11740)
- **核心**: 使用 MoE 增强自动驾驶系统, 按场景动态激活专家模块

#### Regressor-guided Diffusion Model for De Novo Peptide Sequencing
- **核心**: 提出回归器引导的扩散模型 DiffuNovo, 实现精确的肽段从头测序

#### GlassVAE: Hierarchical Graph VAE for Disordered Materials
- **核心**: 基于层次图 VAE 实现无序材料的结构生成与性质预测

### 4.3 AAAI 2026 Bridge 主题
- 年度主题: "桥梁" (Bridges) — 促进 AI 不同子领域之间的协作
- 新增 Bridge Program: 鼓励跨社区合作

---

## 5. CVPR 2026

**时间**: 2026年6月3-7日 | **地点**: Denver, Colorado
**规模**: 16,092 篇投稿, 4,090 篇接受 (25.42%); 较 2025 年增长 42%

### 5.1 CVPR 2026 Best Paper

#### 🏆 D4RT: Efficiently Reconstructing Dynamic Scenes One D4RT at a Time
- **作者**: Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, Liliane Momeni, Junyu Xie, Shuyang Sun, Rahul Sukthankar, Joëlle K. Barral, Raia Hadsell, Zoubin Ghahramani, Andrew Zisserman, Junlin Zhang, Mehdi S. M. Sajjadi
- **机构**: Google DeepMind, UCL, University of Oxford
- **核心**: 统一 Transformer 架构从视频中重建动态 4D 场景的几何和运动
- **方法**: 同时估计深度、时空对应关系和完整相机参数, 可独立高效地查询任意点在空间和时间中的 3D 位置
- **突破**: 将传统计算密集型 4D 重建简化为轻量级、高可扩展方法

#### 🏆 CVPR 2026 Best Student Paper
- **Native and Compact Structured Latents for 3D Generation** — 高效 3D 生成的结构化潜变量方法

### 5.2 CVPR 2026 趋势

#### 多模态 LLM 论文份额翻倍 (4.9% → 10.6%)
- 视觉-语言和多模态 LLM 研究是增长最快的子领域

#### 视频生成论文增长 2.3 倍
- Video generation 和 image/video synthesis 成为投稿量最高的类别

#### 代表性 Highlight 论文:
- **SAM 3D: 3Dfy Anything in Images** (Meta/Facebook Research) — 将 SAM 扩展到 3D 对象分割
- **NitroGen: Open-Source Vision-Action Foundation Model** (NVIDIA, Stanford, Caltech 等) — 在 40,000+ 小时游戏数据上训练的视觉-动作基础模型, 覆盖 1,000+ 游戏
- **WorldLens: Full-Spectrum Evaluations of Driving World Models** — 驾驶世界模型的全面评估框架
- **Trainable Log-linear Sparse Attention for Efficient Diffusion Transformers** — 高效扩散 Transformer 的可训练对数线性稀疏注意力
- **Scal3R: Scalable Test-Time Training for Large-Scale 3D Reconstruction** — 大规模 3D 重建的可扩展测试时训练

---

## 6. KDD 2026

**时间**: 2026年8月9-13日 | **地点**: Jeju Island, South Korea

### 6.1 KDD 2026 代表论文

#### SkillTracer: Structural Failure Attribution and Refinement of Agentic Skills in Long-Horizon Web Tasks
- **机构**: A*STAR CFAR
- **核心**: 用可编辑的程序化验证计划图替代单体技能宏, 支持将执行故障定位到特定节点并进行结构性修复
- **方法**: 将长周期 Web Agent 技能分解为有向图结构, 节点级故障定位与修复

#### Causal Scaffolding for Physical Reasoning: A Benchmark for VLMs
- **机构**: A*STAR CFAR
- **核心**: 用于评估 VLM 因果物理世界理解的数据集和基准

#### Meta Lattice: Model Space Redesign for Cost-Effective Industry-Scale Ads Recommendations
- **机构**: Meta
- **核心**: 对工业级广告推荐系统空间进行重新设计, 在成本约束下最大化模型性能
- **方法**: 系统性地探索模型架构、容量分配、训练策略的设计空间

#### RankUp: Towards High-rank Representations for Large Scale Advertising Recommender Systems
- **机构**: Tencent
- **arXiv**: [2604.17878](https://arxiv.org/abs/2604.17878)
- **核心**: 通过随机排列分裂 (randomized permutation splitting)、多嵌入范式、全局 token 集成和交叉预训练嵌入 token 来提升表征秩、防止表征坍缩
- **背景**: RankMixer 揭示 token 表征的有效秩随层深呈阻尼振荡, 不随深度一致增长

#### Scaling Recommender Transformers to One Billion Parameters
- **机构**: Yandex
- **核心**: 建立推荐 Transformer 到 10 亿参数的训练方法体系

### 6.2 其他 KDD 2026 亮点
- **新设 Track**: Datasets & Benchmarks Track, AI for Sciences Track
- **两个审稿周期**: 第一周期 2025 年 8 月, 第二周期 2026 年 2 月

---

## 7. ACL 2026 & EMNLP 2025

### 7.1 ACL 2026

#### BootTrans: Bootstrapping Code Translation with Weighted Multilanguage Exploration
- **机构**: Nanjing University
- **arXiv**: [2601.03512](https://arxiv.org/abs/2601.03512)
- **核心**: 无需并行语料的引导式代码翻译框架, 利用单元测试跨语言可迁移性构建循环训练机制
- **创新**: 语言感知动态加权优化策略; HumanEval-X 上 Llama-3.1-8B 最高提升 16.57%

#### KARL: Reinforcement Learning for LLM Agents on Multi-Turn Knowledge-Intensive Tasks
- **核心**: 针对多轮知识密集型任务设计的 LLM Agent 强化学习方法

#### Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier
- **核心**: 使用灵活生成验证器的推理时扩展策略

#### Self-Guided Alignment: Adaptive Preference Sensing for Multi-Objective Generation
- **核心**: 自适应偏好感知的多目标生成对齐方法

#### Awakening Dormant Experts: Counterfactual Routing to Mitigate MoE Hallucinations
- **核心**: 通过反事实路由激活休眠专家, 缓解 MoE 幻觉问题

#### TokDrift: When LLM Speaks in Subwords but Code Speaks in Grammar
- **核心**: 分析 LLM 子词分词与代码语法之间的漂移问题

### 7.2 EMNLP 2025

**时间**: 2025年11月4-9日 | **地点**: Suzhou, China
**规模**: 主会 1,811 篇 (22.16%), Findings 1,417 篇 (17.34%), 合计 3,228 篇

#### 代表论文:
- **Towards Automated Error Discovery in Conversational AI** — SEEED 框架: 基于软聚类的编码器错误检测
- **Bias Mitigation or Cultural Commonsense? Evaluating LLMs with a Japanese Dataset** — LLM 文化常识偏差评估
- **Thinking Out Loud: Do Reasoning Models Know When They're Right?** — 推理模型的自我校准能力研究
- **A Unified Framework for N-ary Property Information Extraction in Materials Science** — 材料科学信息抽取

---

## 8. SIGIR 2026 & WWW 2026

### 8.1 SIGIR 2026

**时间**: 2026年7月20-24日 | **地点**: Melbourne, Australia

#### 代表论文:
- **Total Recall QA: A Verifiable Evaluation Suite for Deep Research Agents** (UMass CIIR) — 深度研究 Agent 的可验证评估套件
- **Uncertainty Quantification for Retrieval-Augmented Reasoning** (UMass CIIR) — 检索增强推理的不确定性量化
- **Learning from Natural Language Feedback for Personalized Question Answering** (UMass CIIR) — 从自然语言反馈中学习个性化问答
- **Beyond Static Best-of-N: Bayesian List-wise Alignment for LLM-based Recommendation** — SIGIR 2026, 贝叶斯列表式对齐方法

### 8.2 WWW 2026

#### 代表论文:
- **GORAG: Graph-based Online Retrieval Augmented Generation** — 基于图的在线 RAG 框架
- **ThinkRec: Thinking-based LLM Recommendation** — 基于思维的 LLM 推荐 (已在 Wiki 中)
- **Make It Long, Keep It Fast: End-to-End 10K-Sequence Modeling at Billion Scale** (ByteDance) — 十亿级 10K 序列建模
- **GenCI: Generative CTR via Cohort Intent Learning** — 基于群体意图学习的生成式 CTR (已在 Wiki 中)
- **SparseCTR: Sparse Attention Long-Term CTR** (Meituan) — 稀疏注意力长期 CTR 建模

---

## 9. CIKM 2025 & RecSys 2025

### 9.1 CIKM 2025
- **RankMixer: Scaling Up Ranking Models in Industrial Recommenders** (ByteDance) — 已在 Wiki 中详细记录
- **TWIN V2: Scaling Ultra-Long User Behavior Sequence Modeling** (Kuaishou) — 超长用户行为序列建模

### 9.2 RecSys 2025
- **LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders** (ByteDance) — 超长序列建模在工业推荐中的应用
- **SUAN: Online CTR Scaling Methodology** (Meituan) — 在线 CTR Scaling 方法论

---

## 10. 推荐系统 & CTR 预测 — 工业界前沿

### 10.1 LinkedIn — CADET
- **arXiv**: [2602.11410](https://arxiv.org/abs/2602.11410)
- **标题**: CADET: Context-Conditioned Ads CTR Prediction with Decoder-Only Transformer
- **核心**: LinkedIn 部署的端到端 decoder-only Transformer 广告 CTR 预测模型
- **创新**:
  - **条件自条件解码** — 解决后评分上下文信号 (如广告位置) 的 chicken-and-egg 问题
  - **自门控注意力** — 每头 sigmoid 门控, 独立于 Qwen 门控注意力
  - **时间感知 RoPE** — 从秒到月的时差编码
  - **会话掩码** — 解决训练-服务不一致

### 10.2 ByteDance — HyFormer
- **arXiv**: [2601.12681](https://arxiv.org/abs/2601.12681)
- **核心**: 重新审视序列建模和特征交互在 CTR 中的作用
- **实验**: 在抖音搜索系统 3B 样本上验证, HyFormer 以 418 推理时间 (3.9ms) 超越全 Transformer 的 450 推理时间 (21.9ms), AUC +0.17%
- **方法**: 解耦序列建模和特征交互, 分别优化

### 10.3 DS-MLP: Dual-Stream MLP for CTR Prediction
- **arXiv**: [2606.04944](https://arxiv.org/abs/2606.04944)
- **机构**: Renmin University of China (TKDD 2026)
- **核心**: 使用知识蒸馏将显式特征交互学习能力浓缩到主 MLP 网络, 并行 MLP 捕获隐式交互
- **创新**: 双流对齐策略; 最终模型仅为 vanilla MLP 结构
- **结果**: 在三个广泛使用的基准上达到 SOTA

### 10.4 GenLI: Generative Long-term User Interest for CTR
- **arXiv**: [2605.15905](https://arxiv.org/abs/2605.15905)
- **核心**: 通过生成式方法建模长期用户兴趣, 使用兴趣生成模块产生多个兴趣分布
- **创新**: 目标无关的兴趣生成, O(1) 时间复杂度的行为检索

### 10.5 RankUp (Tencent, KDD 2026)
- **arXiv**: [2604.17878](https://arxiv.org/abs/2604.17878)
- **核心**: 通过随机排列分裂、多嵌入范式、全局 token 集成提升表征秩
- **方法**: 解决 deep 层表征秩退化问题

### 10.6 Meta Lattice (Meta, KDD 2026)
- **核心**: 模型空间重新设计, 系统探索工业广告推荐的最佳架构配置
- **方法**: 在成本约束下进行架构-容量-训练策略联合搜索

### 10.7 LinkedIn — Generative Recommendation for Advertising
- **核心**: 将广告选择建模为生成问题而非排序问题
- **优势**: 更高效率、更好推荐质量

### 10.8 Alibaba — EST: Efficient Scaling Laws for CTR
- **arXiv**: [2602.10811](https://arxiv.org/abs/2602.10811)
- **核心**: 通过统一建模实现 CTR 预测的高效缩放定律

### 10.9 Scaling Laws for Behavioral Foundation Models
- **arXiv**: [2606.05257](https://arxiv.org/abs/2606.05257)
- **机构**: Unbox AI
- **核心**: 在 ~600 次运行和 10^15-10^19 FLOPs 范围内系统研究行为基础模型的缩放定律
- **发现**: 最优嵌入器大小约 2%, 数据密集型训练占主导

---

## 11. LLM 架构与训练 — 2026 前沿进展

### 11.1 Nemotron 3 (NVIDIA)
- **arXiv**: [2604.12374](https://arxiv.org/abs/2604.12374)
- **核心**: 混合架构设计 — 交替使用标准注意力层和 Mamba-2 SSM 层
- **版本**: 120B-A12B (大), 4B Nano 版
- **特点**: 长上下文效率优先, 适合 Agent 场景已被用于 NVIDIA AI-Q 企业 Agent 蓝图

### 11.2 Mamba-3
- **arXiv**: [2603.15569](https://arxiv.org/abs/2603.15569)
- **核心**: 状态空间模型的第三代, 进一步缩小与 Transformer 在语言建模上的差距

### 11.3 Gated Attention (NeurIPS 2025 Best Paper) — 已应用于 Qwen3-Next
- 见 2.1 节详细分析
- Qwen3-Next 已开源包含 Gated DeltaNet 和 Gated Attention 的组合

### 11.4 SDLM: Sequential Diffusion Language Model
- **arXiv**: [2509.24007](https://arxiv.org/abs/2509.24007)
- **机构**: OpenGVLab (Shanghai AI Lab)
- **核心**: 提出下一序列预测 (NSP) 统一 next-token 和 next-block 预测, 可低代价改造预训练 ALM
- **方法**: 在固定大小掩码块内进行扩散推理, 基于模型置信度动态解码连续子序列
- **实验结果**: 仅用 3.5M 训练样本即匹配/超越强自回归基线; 吞吐量比 Qwen-2.5 高 2.1 倍
- **SDLM-32B**: 效率增益更显著

### 11.5 Introspective Diffusion Language Model (I-DLM)
- **arXiv**: [2604.11035](https://arxiv.org/abs/2604.11035)
- **核心**: 通过因果注意力和内省步进解码解决 DLM 与 AR 推理引擎的不兼容
- **创新**: 保持因果结构, 可直接集成到现有 AR 服务栈

### 11.6 Scaling Embeddings Outperforms Scaling Experts
- **arXiv**: [2601.21204](https://arxiv.org/abs/2601.21204)
- **核心**: 扩展嵌入层容量比扩展专家数量更有效地提升 MoE 模型性能

### 11.7 Step 3.5 Flash
- **arXiv**: [2602.10604](https://arxiv.org/abs/2602.10604)
- **核心**: 仅 11B 激活参数达到前沿级智能水平

### 11.8 Symmetry in Language Statistics Shapes the Geometry of Model Representations
- **arXiv**: [2602.15029](https://arxiv.org/abs/2602.15029)
- **核心**: 语言统计对称性塑造模型表征的几何结构

### 11.9 The Spike, the Sparse and the Sink
- **arXiv**: [2603.05498](https://arxiv.org/abs/2603.05498)
- **核心**: 分析 Transformer 激活行为中的尖峰、稀疏和下沉模式

---

## 12. 智能体系统 (Agents)

### 12.1 Agent Skills Survey
- **arXiv**: [2602.12430](https://arxiv.org/abs/2602.12430)
- **核心**: 全面综述 LLM Agent 技能体系, 涵盖架构基础、技能获取、安全性和未来路径
- **框架**: 按需加载的可组合指令、代码和资源包; 渐进式披露 + MCP 集成

### 12.2 Hierarchical Control in Multi-Agent Games (LLM Planning + RL Execution)
- **arXiv**: [2606.20014](https://arxiv.org/abs/2606.20014)
- **核心**: 预训练 LLM 作为集中式战略控制器, 选择专用 RL 技能策略; RL 策略处理反应式低级执行
- **实验**: 在多人游戏环境中展现竞争性协调和行为可信度

### 12.3 Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks
- **arXiv**: [2602.11224](https://arxiv.org/abs/2602.11224)
- **核心**: 基于容器化环境 + 状态差分的代码执行评估框架, 专为企业 API 任务设计
- **创新**: 解决黑盒企业 SaaS API 评估难题

### 12.4 EvoRoute: Experience-Driven Self-Routing LLM Agent Systems
- **arXiv**: [2601.02695](https://arxiv.org/abs/2601.02695)
- **核心**: 自演进模型路由系统, 在子任务粒度动态选择最优 LLM
- **机制**: 检索→帕累托过滤→轻量决策模型三阶段路由

### 12.5 Code as Agent Harness (Survey)
- **arXiv**: [2605.18747](https://arxiv.org/abs/2605.18747)
- **核心**: 将代码重新定义为 Agent 基础设施的核心, 提出"代码即 Agent 框架"的统一视角
- **三层**: 框架接口 (推理/行动/环境) → 框架机制 (规划/记忆/工具) → 框架扩展 (多 Agent 协作)

### 12.6 NSI: Neuro-Symbolic Skill Induction (ICML 2026)
- **核心**: 将 LLM Agent 交互轨迹提升为含条件分支和动态变量绑定的神经符号工作流图
- **结果**: ALFWorld 98.0%, WebShop 76.5%, TextCraft 95.2%

### 12.7 Google DeepMind — Co-Scientist
- **发布时间**: 2026年5月
- **核心**: 多 Agent AI 协作加速科学研究
- **框架**: 多个专业化 Agent 分别负责假设生成、实验设计、结果分析

### 12.8 NVIDIA AI-Q Blueprint
- **发布时间**: 2026年2月
- **核心**: 企业 Agent 框架, 集成 Nemotron 3 Super 120B, MCP 工具集成, NeMo Agent Toolkit
- **功能**: CLI/Web UI/异步任务; Docker Compose/Helm 部署

---

## 13. 游戏 AI & 强化学习

### 13.1 NitroGen (CVPR 2026, NVIDIA)
- **核心**: 开源视觉-动作基础模型, 在 40,000 小时 1,000+ 游戏数据上训练
- **机构**: NVIDIA, Stanford, Caltech, University of Chicago, UT Austin
- **意义**: 游戏 AI 基础模型的里程碑

### 13.2 Hierarchical Control in Multi-Agent Games
- **arXiv**: [2606.20014](https://arxiv.org/abs/2606.20014)
- **见 12.2 节**

### 13.3 SPIRAL: Self-Play Incentivizes Reasoning (ICLR 2026)
- **核心**: 自我博弈机制激发推理能力的理论和方法

### 13.4 GENSTRAT: Strategic Reasoning in LLMs
- **arXiv**: [2605.23238](https://arxiv.org/abs/2605.23238)
- **核心**: 评估和提升 LLM 的战略推理能力

### 13.5 Odysseus: Scaling VLMs to 100+ Turn Decision-Making
- **arXiv**: [2605.00347](https://arxiv.org/abs/2605.00347)
- **核心**: 将 VLM 扩展到百轮以上的决策任务

### 13.6 PCSP: One Policy, Infinite NPCs (Persona RL)
- **arXiv**: [2605.23652](https://arxiv.org/abs/2605.23652)
- **核心**: 通过角色条件共享策略实现 NPC 行为个性化, 单一策略支持无限角色

---

## 14. 生成模型 & 扩散语言模型

### 14.1 SDLM — Sequential Diffusion Language Models
- 见 11.4 节详细分析

### 14.2 Diffusion Language Models Survey
- **arXiv**: [2508.10875](https://arxiv.org/abs/2508.10875)
- **全面综述**: DLM 预训练策略、后训练方法、推理优化 (并行解码、KV 缓存、生成质量)

### 14.3 Diffusion Language Models Experimental Analysis
- **arXiv**: [2606.19475](https://arxiv.org/abs/2606.19475)
- **核心**: 系统分析 8 种 SOTA DLM 在 8 个基准上的推理质量和计算效率
- **关键发现**: DLM 行为受生成时设计选择强烈影响, 存在性能-效率权衡

### 14.4 D4RT — Dynamic 4D Scene Reconstruction
- 见 5.1 节 (CVPR 2026 Best Paper)

### 14.5 DiLaDiff: Distilled Latent-Augmented Diffusion LM (NVIDIA)
- **已在 Wiki 中**

### 14.6 LaDiR: Latent Diffusion for LLM Text Reasoning (ICLR 2026)
- **已在 Wiki 中**

---

## 15. 代码推理 & 形式化验证

### 15.1 ResRL — 提升 LLM 数学/代码推理
- 见 1.2 节 (ICML 2026)

### 15.2 BootTrans — 代码翻译 (ACL 2026)
- 见 7.1 节

### 15.3 Agentic Proving for Program Verification
- **arXiv**: [2605.23772](https://arxiv.org/abs/2605.23772)
- **核心**: 使用 LLM Agent 进行程序验证的形式化证明

### 15.4 ImProver 2: Neurosymbolic Proof Optimization
- **arXiv**: [2605.22885](https://arxiv.org/abs/2605.22885)
- **机构**: CMU
- **核心**: 神经符号方法优化形式化证明

### 15.5 A Minimal Agent for Automated Theorem Proving (ICML 2026)
- 见 1.3 节

---

## 16. 基准测试 & 评估

### 16.1 重要基准更新

| 基准名称 | 领域 | 机构 | 说明 |
|---------|------|------|------|
| Infinity-Chat | LLM 输出多样性 | UW/CMU/AI2 | 26K 开放式查询, 评估"人工蜂群思维" |
| HistBench | 历史推理 | ICML 2026 | 414 题多难度层级问题 |
| Agent-Diff | 企业 API Agent | arXiv 2026 | 容器化状态差分评估 |
| Total Recall QA | 深度研究 Agent | UMass CIIR / SIGIR 2026 | 可验证评估套件 |
| NitroGen | 游戏视觉-动作 | NVIDIA / CVPR 2026 | 1,000+ 游戏, 40,000 小时 |

### 16.2 LLM 研究论文趋势 (2026年1-5月)

根据 Sebastian Raschka 的年度清单, 2026 年 LLM 研究方向聚焦:

1. **架构与模型设计** — 混合架构、SSM 层、MoE 容量分配
2. **高效训练与缩放** — Scaling Law 持续深化
3. **推理效率 & KV Cache** — 推理优化成为主线
4. **稀疏注意力 & 长上下文** — 长上下文是 Agent 场景关键
5. **推理 & 测试时计算** — RLVR/CoT 持续演进
6. **强化学习 & RLVR** — RL from Verifiable Rewards
7. **Agent 系统 & 工具使用** — Agent 框架爆发
8. **编码 Agent & 软件工程** — SWE-bench, coding agents
9. **扩散语言模型** — DLM 成为 AR 范式的有力竞争者
10. **模型评估与基准** — 更全面的评估体系

---

## 附录: 主要机构研究动态

### Google DeepMind
- **D4RT** (CVPR 2026 Best Paper) — 动态 4D 场景重建
- **Co-Scientist** — 多 Agent AI 科研伙伴
- **Gemini 3.5** — 支持计算机使用的多模态模型
- **SIMA 2** — 3D 世界游戏 Agent
- **Genie 3** — 通用世界模型
- **Gemma 4** — 高效开放模型

### OpenAI
- **GPT-5.6 系列** (Sol/Terra/Luna) — 多尺寸混合专家模型 (2026)
- **Operator** — 网络任务自动 Agent

### Anthropic
- **Claude Tag** — 企业工作流持久化多会话 Agent 角色
- **Claude 4.5/Opus 4** — SWE-Bench 72.5% 编码领先

### Meta
- **Meta Lattice** (KDD 2026) — 工业广告推荐模型重设计
- **Llama 4** — Scout/Maverick 多模态变体
- **SAM 3D** (CVPR 2026) — 3D 分割基础模型

### NVIDIA
- **Nemotron 3** (120B-A12B + 4B Nano) — 混合注意+SSM 架构
- **NitroGen** (CVPR 2026) — 游戏视觉-动作基础模型
- **AI-Q Blueprint** — 企业 Agent 框架

### ByteDance (抖音/字节跳动)
- **HyFormer** — CTR 序列与特征交互再思考 (3B 样本)
- **LONGER** — 超长序列建模 (RecSys 2025)
- **TokenMixer-Large** — 硬件利用率导向的缩放
- **RankMixer** — 排序模型缩放 (CIKM 2025)

### Alibaba (阿里巴巴)
- **Gated Attention** (NeurIPS 2025 Best Paper) — 门控注意力
- **Qwen3-Next** — 已集成 Gated Attention + Gated DeltaNet
- **EST** — 高效 CTR 缩放定律
- **GenCI** — 生成式 CTR (WWW 2026)

### Tencent (腾讯)
- **RankUp** (KDD 2026) — 广告推荐的高秩表征
- **Foundation Protocol** — Agent 社会协调协议

### Kuaishou (快手)
- **CHIME** — 全息兴趣建模 (LLM+VQ)
- **RPORec** — RL + 推理推荐
- **UniMixer** — 统一缩放架构

### Microsoft Research
- **SkillOpt** — 自演化 Agent 技能
- **Inductive Deductive Synthesis** — 验证系统 (with UC Berkeley)

---

> ⚠️ **注意**: 本报告基于 arXiv、OpenReview、官方会议网站和 Paper Digest/Paper Copilot 等第三方来源的信息汇总。部分论文的详细数据可能因信息更新滞后而存在偏差。建议读者查阅原始论文和会议官方页面获取最新信息。
