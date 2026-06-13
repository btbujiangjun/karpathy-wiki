---
title: Conference & arXiv Digest — 2026-06-13 全面版
type: synthesis
created: 2026-06-13
updated: 2026-06-13
sources: []
tags: [conference-digest, icml-2026, aaai-2026, neurips-2025, iclr-2026, kdd-2026, cvpr-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2025, recsys-2025]
---

# Conference & arXiv Digest — 2026-06-13 全面版

> 覆盖 12+ 个顶会/顶刊 + arXiv 的 AI/ML 最新论文, 包含 LLM 训练与理论、推荐系统/CTR/广告、Agent 系统、游戏/RL、生成模型、代码推理、多模态等领域。涵盖 15+ 家机构实验室的最新成果。

---

## 目录

1. [ICML 2026 — 机器学习国际会议](#1-icml-2026)
2. [AAAI 2026 — 人工智能顶级会议](#2-aaai-2026)
3. [NeurIPS 2025 — 神经信息处理系统大会](#3-neurips-2025)
4. [ICLR 2026 — 表征学习国际会议](#4-iclr-2026)
5. [KDD 2026 — 知识发现与数据挖掘大会](#5-kdd-2026)
6. [CVPR 2026 — 计算机视觉与模式识别大会](#6-cvpr-2026)
7. [ACL 2026 & EMNLP 2025 — 自然语言处理](#7-acl-2026--emnlp-2025)
8. [SIGIR 2026 — 信息检索研究与发展](#8-sigir-2026)
9. [WWW 2026 — 万维网大会](#9-www-2026)
10. [CIKM 2025 — 信息与知识管理](#10-cikm-2025)
11. [RecSys 2025 — 推荐系统大会](#11-recsys-2025)
12. [arXiv 亮点 — GRPO 训练与推理最新进展](#12-arxiv-亮点--grpo-训练与推理)

---

## 1. ICML 2026

> **时间**: 2026年7月，首尔 | **接收率**: ~6,500 篇 (总投稿 ~18,000)
> **Key Theme**: Agent系统大规模涌入、生成式推荐成熟、推理模型基础理论深化

### 1.1 Causal Direct Preference Optimization for Distributionally Robust Generative Recommendation (CausalDPO)

| 项目 | 内容 |
|------|------|
| **标题** | Causal Direct Preference Optimization for Distributionally Robust Generative Recommendation |
| **中文** | 因果直接偏好优化实现分布鲁棒的生成式推荐 |
| **作者** | Chu Zhao, Enneng Yang, Jianzhe Zhao, Guibing Guo |
| **机构** | 东北大学 (中国) |
| **链接** | ICML 2026 Poster |

**问题背景**:
Direct Preference Optimization (DPO) 被广泛用于指导 LLM 生成符合用户历史行为的推荐。然而，系统性的实证和理论分析揭示：DPO 在 align 过程中会放大环境混淆变量 (environmental confounders) 导致的伪相关 (spurious correlations)，严重损害生成式推荐方法在分布外 (OOD) 场景的泛化能力。

**方法详述**:
提出 CausalDPO 扩展 DPO：(1) 在偏好对齐阶段引入 **后门调整策略 (backdoor adjustment)** 消除环境混淆变量干扰；(2) 通过 **软聚类 (soft clustering)** 显式建模潜在环境分布；(3) 通过 **不变性约束 (invariance constraints)** 增强跨环境的鲁棒一致性。

**实验结果**:
在 4 种代表性分布偏移设定下，CausalDPO 平均提升 24.10% 于 4 个评估指标，显著优于 DPO 及现有 OOD 推荐方法。

### 1.2 ML-Agent: Reinforcing LLM Agents for Autonomous Machine Learning Engineering

| 项目 | 内容 |
|------|------|
| **标题** | ML-Agent: Reinforcing LLM Agents for Autonomous Machine Learning Engineering |
| **中文** | ML-Agent: 强化 LLM Agent 用于自动化机器学习工程 |
| **作者** | Zexi Liu, Jingyi Chai, Xinyu Zhu, Shuo Tang, Rui Ye, Weiyu Ma, Bo Zhang, Lei Bai, Siheng Chen |
| **机构** | 上海交通大学 |
| **链接** | ICML 2026 Poster |

**问题背景**:
基于 LLM 的 Agent 在自动化 ML 工程方面取得显著进展。但当前的 prompt-based 范式存在局限：小模型缺乏从执行轨迹中学习泛化的能力，大模型计算开销巨大。

**方法详述**:
提出学习型 Agentic ML 训练框架，三大组件：(1) **探索增强微调** — 使 LLM Agent 生成多样化动作以增强 RL 探索；(2) **步级 RL** — 对单一动作步进行训练，加速经验收集；(3) **Agentic ML 特定奖励模块** — 将多样化 ML 反馈信号统一为一致奖励用于 RL 优化。基于 7B 的 Qwen-2.5 训练的 ML-Agent 在仅 9 个 ML 任务上训练后性能可与 GPT-5 Agent 媲美。

### 1.3 SciAgentGym: Benchmarking Multi-Step Scientific Tool-use in LLM Agents

| 项目 | 内容 |
|------|------|
| **标题** | SciAgentGym: Benchmarking Multi-Step Scientific Tool-use in LLM Agents |
| **中文** | SciAgentGym: LLM Agent 多步科学工具使用基准 |
| **作者** | Yujiong Shen, Yajie Yang, Zhiheng Xi 等 |
| **机构** | 复旦大学 |
| **arXiv** | 2602.12984 |

**方法详述**:
提供 1,780 个工具、长时域工作流的科学工具使用基准。报告了现有 Agent 在扩展轨迹上的系统性失败，并提出 SciForge 数据合成方法改善工具使用训练。**ICML 2026 Regular 接收**。

### 1.4 其他重要 ICML 2026 论文

| 论文 | 主题 | 机构 |
|------|------|------|
| PostTrainBench: Can LLM Agents Automate LLM Post-Training? | LLM Agent 自动化后训练 | — |
| LOCA-bench (Long-Context Agents) | 长上下文 Agent 基准 | — |
| Implicit Intelligence | 隐式智能评估框架 | — |
| AgentSelect: Benchmark for Narrative Query-to-Agent Recommendation | Agent 推荐基准 | — |
| Reducing Belief Deviation in RL for Active Reasoning | 信念偏差校正 RL | — |
| HyperAgents (DGM-H) | 元认知自改进 Agent | — |
| Group Cognition Learning | 两阶段 Agent 协作 | — |
| In-The-Flow Agentic System Optimization | Agent 系统规划与工具使用 | — |
| Position: Preregister Experiments with AI Agents | AI Agent 实验预注册 | — |

> **ICML 2026 趋势**: Agent 论文暴增（465 篇 agent 相关），工具使用 RL、多 Agent 协作、GUI Agent 预训练成为热点。Benchmark 类 99 篇，多 Agent/MARL 93 篇，工具使用 RL 58 篇。

---

## 2. AAAI 2026

> **时间**: 2026年1月20–27日，新加坡 | **投稿**: ~29,000 篇 (~23,000 有效)
> **Key Theme**: LLM 推荐深度融合、生成式推荐大规模落地

### 2.1 MoMoREC: A Multi-agent Motivation Generation Framework for Residual Semantic ID-Aware Recommendation

| 项目 | 内容 |
|------|------|
| **标题** | MoMoREC: A Multi-agent Motivation Generation Framework for Residual Semantic ID-Aware Recommendation |
| **中文** | MoMoREC: 多智能体动机生成框架用于残差语义 ID 感知推荐 |
| **作者** | Yige Wang, Mingming Li, Li Wang, Kaichen Zhao, Wangming Li, Weipeng Jiang, Xueying Li |
| **机构** | 阿里巴巴 淘天集团 / 西安交通大学 |
| **链接** | [AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/38623) |

**问题背景**:
LLM 在序列推荐中显示出增强 item embedding 和用户理解的潜力。但现有方法面临三大限制：(1) 对用户购买决策背后原因的理解不足；(2) LLM 产生的高维 embedding 与传统低维 ID embedding 不兼容；(3) 需要额外的微调和推理开销。

**方法详述**:
MoMoREC 利用 LLM 内在理解能力 + 残差语义 ID。通过多 Agent 框架分析用户购物动机并提取高维稠密 embedding，然后通过聚类 + 残差降维转换为低维 ID。无需辅助可训练模块，可适配任何序列推荐框架。

**实验结果**:
在 3 个基准数据集上显著提升传统推荐模型性能。

### 2.2 TreeBridge: Aligning LLM Embeddings in Industrial Recommender Systems

| 项目 | 内容 |
|------|------|
| **标题** | TreeBridge: Aligning LLM Embeddings in Industrial Recommender Systems |
| **中文** | TreeBridge: 工业推荐系统中 LLM Embedding 对齐 |
| **作者** | Y. Ni, C. Yuanpeng, W. Zhou, B. Hong, Z. Zhang, E. Cai, X. Li 等 |
| **机构** | Shopee (冬海集团) |
| **链接** | [AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/41478) |

**方法详述**:
TreeBridge 引入结构感知生成式编码树 (structure-aware generative encoding tree) 弥合 LLM embedding 与推荐任务之间的语义差距。保留外部语义丰富性同时学习标签信息结构。采用在线-离线混合服务范式确保低延迟部署。**已在 Shopee 部署 (2025年5月起)**，服务东南亚数亿用户，GMV 相对提升 1.55%。

### 2.3 Align³GR: Unified Multi-Level Alignment for LLM-based Generative Recommendation

| 项目 | 内容 |
|------|------|
| **标题** | Align³GR: Unified Multi-Level Alignment for LLM-based Generative Recommendation |
| **中文** | Align³GR: 统一的 LLM 生成推荐多级对齐框架 |
| **作者** | Wencai Ye, Mingjie Sun, Shuhang Chen, Wenjin Wu, Peng Jiang |
| **机构** | Kuaishou Technology |
| **链接** | [AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/38651) |

**方法详述**:
统一 token 级、行为建模级和偏好级对齐：(1) 双 tokenization 融合用户-物品语义和协同信号；(2) 增强行为建模 + 双向语义对齐；(3) 渐进式 DPO 策略结合自博弈 (SP-DPO) 和真实反馈 (RF-DPO)。

**实验结果**:
在公开数据集上 Recall@10 +17.8%，NDCG@10 +20.2%。线上 A/B 测试显著提升，已全量部署于大规模工业推荐平台。

### 2.4 STARec: An Efficient Agent Framework for Recommender Systems via Autonomous Deliberate Reasoning

| 项目 | 内容 |
|------|------|
| **标题** | STARec: An Efficient Agent Framework for Recommender Systems via Autonomous Deliberate Reasoning |
| **中文** | STARec: 通过自主审慎推理的高效推荐 Agent 框架 |
| **作者** | 多作者 |
| **机构** | — |
| **链接** | CIKM 2025 (arXiv: 2508.18812) |

**方法详述**:
每个用户建模为一个具有并行认知的 Agent：**快速响应**用于即时交互，**慢速推理**执行 Chain-of-Thought 推理。使用**锚定强化训练 (anchored reinforcement training)** 两阶段范式：从高级推理模型进行结构化知识蒸馏 + 偏好对齐奖励塑造。

**实验结果**:
使用仅 0.4% 的全训练数据，在 MovieLens 1M 和 Amazon CDs 上显著超越 SOTA 方法。

---

## 3. NeurIPS 2025

> **时间**: 2025年12月，San Diego | **Key Theme**: Reasoning-augmented RecSys, 推荐中的推理能力

### 3.1 RecZero: Think before Recommendation — Autonomous Reasoning-enhanced Recommender

| 项目 | 内容 |
|------|------|
| **标题** | Think before Recommendation: Autonomous Reasoning-enhanced Recommender (RecZero) |
| **中文** | RecZero: 推荐前思考 — 自主推理增强推荐系统 |
| **作者** | Xiaoyu Kong, Junguang Jiang, Bin Liu, Ziru Xu, Han Zhu, Jian Xu, Bo Zheng, Jiancan Wu, Xiang Wang |
| **机构** | 中国科学技术大学 / 阿里巴巴 |
| **链接** | NeurIPS 2025 Poster |

**问题背景**:
现有基于 LLM 的推荐方法多采用蒸馏方式，存在教师模型推荐能力不足、监督信号昂贵且静态、推理能力迁移浅层等问题。

**方法详述**:
提出 RecZero，抛弃传统多模型多阶段蒸馏，通过纯 RL 训练单个 LLM 自主发展推理能力。(1) **Think-before-Recommendation prompt 构造** — 使用结构化推理模板引导模型分步分析用户兴趣、物品特征和兼容性；(2) **基于规则的奖励建模** — 采用 GRPO 计算推理轨迹奖励并优化 LLM。还提出 RecOne 混合范式 (SFT + RL 结合)。

**实验结果**:
在多个基准数据集上显著优于基线方法，验证了 RL 范式在实现自主推理增强推荐方面的优越性。

### 3.2 R²ec: Towards Large Recommender Models with Reasoning

| 项目 | 内容 |
|------|------|
| **标题** | R²ec: Towards Large Recommender Models with Reasoning |
| **中文** | R²ec: 迈向具备推理能力的大型推荐模型 |
| **作者** | Runyang You, Yongqi Li, Xinyu Lin, Xin Zhang, Wenjie Wang, Wenjie Li, Liqiang Nie |
| **机构** | 哈尔滨工业大学 (深圳) |
| **链接** | [NeurIPS 2025](https://nips.cc/virtual/2025/loc/san-diego/poster/117677) / arXiv: 2505.16994 |

**方法详述**:
统一大型推荐模型，具有内在推理能力。**双头架构** (dual-head)：支持推理链生成 + 高效物品预测于单一模型。设计 **RecPO** (强化学习框架) 联合优化推理与推荐，使用新型融合奖励机制。

**实验结果**:
在 3 个数据集上超越传统、基于 LLM 和推理增强的推荐基线。推理延迟显著低于传统 LLM 推荐器。

### 3.3 IGD: Token Decisiveness Modeling via Information Gain in LLMs for Personalized Recommendation

| 项目 | 内容 |
|------|------|
| **标题** | IGD: Token Decisiveness Modeling via Information Gain in LLMs for Personalized Recommendation |
| **中文** | IGD: 基于信息增益的 LLM Token 决策性建模用于个性化推荐 |
| **作者** | Zijie Lin, Yang Zhang, Xiaoyan Zhao, Fengbin Zhu, Fuli Feng, Tat-Seng Chua |
| **机构** | 新加坡国立大学 / 中国科学技术大学 |
| **链接** | NeurIPS 2025 Poster / [OpenReview](https://openreview.net/forum?id=ygNaCTGUwJ) |

**问题背景**:
现有 LLM 推荐方法将所有 item token 平等对待，仅追求似然最大化。但许多 token 对物品辨识贡献极小却主导优化或解码过程。

**方法详述**:
将物品生成建模为决策过程，通过**信息增益 (Information Gain)** 衡量每个 token 在减少生成物品不确定性方面的贡献。IGD 在训练中降低低 IG token 权重，在解码中重新平衡以强调高 IG token。

**实验结果**:
在 4 个基准数据集 + 2 种 LLM 骨干上一致提升推荐准确率。

### 3.4 TagCF: Who You Are Matters — Bridging Topics and Social Roles via LLM-Enhanced Logical Recommendation

| 项目 | 内容 |
|------|------|
| **标题** | Who You Are Matters: Bridging Topics and Social Roles via LLM-Enhanced Logical Recommendation (TagCF) |
| **中文** | TagCF: 基于 MLLM 标签提取与 LLM 逻辑推理的推荐框架 |
| **作者** | 多作者 |
| **机构** | 工业界 (数亿用户平台) |
| **链接** | NeurIPS 2025 / arXiv: 2505.10940 |

**方法详述**:
(1) **MLLM 标签提取** — 从多模态物品特征提取用户角色标签和物品主题标签；(2) **LLM 协同逻辑过滤** — Qwen2.5-7B 推理标签关系构建双向逻辑图；(3) **标签-逻辑集成** — 通过标签编码器、对比学习增强、逻辑评分集成到 SASRec。

**实验结果**:
在线 A/B 测试：参与度 +0.946%，多样性 +0.102%；离线 NDCG@10 +8.06%。零 LLM 推理开销 (仅离线知识提取)。

### 3.5 RecPIE: Recommendation with Prediction-Informed Explanations

| 项目 | 内容 |
|------|------|
| **标题** | RecPIE: Recommendation with Prediction-Informed Explanations |
| **中文** | RecPIE: 基于预测信息的推荐解释框架 |
| **作者** | 多作者 |
| **机构** | — |
| **链接** | NeurIPS 2025 Workshop |

**方法详述**:
联合优化推荐和解释生成。在电影、餐厅、酒店等 4 个数据集上，RecPIE 一致超越 SOTA 黑盒、基于 LLM 和可解释推荐基线，AUC 提升 3–34%。

### 3.6 ORBIT: Open Recommendation Benchmark for Reproducible Research with Hidden Tests

| 项目 | 内容 |
|------|------|
| **标题** | ORBIT: Open Recommendation Benchmark for Reproducible Research with Hidden Tests |
| **中文** | ORBIT: 具有隐藏测试的开放可复现推荐基准 |
| **机构** | — |
| **链接** | NeurIPS 2025 / arXiv: 2510.26095 |

**方法详述**:
统一基准包含 5 个公开数据集 + 隐私安全的隐藏测试集 ClueWeb-Reco (来自真实用户浏览历史)。系统评估 12 种推荐模型，提出 **LLM-QueryGen 基线**（将推荐重构为检索任务，LLM 生成查询后进行 ANN 检索）。

**关键发现**: 基于内容的方法优于基于 ID 的方法；HLLM 整体最优；ClueWeb-Reco 揭示现实难度 — 面对 8700 万候选集所有模型性能急剧下降。

---

## 4. ICLR 2026

> **时间**: 2026年5月 | **接收**: 5,343 篇 (26.97%) | **Key Theme**: LLM Agent 推理、记忆与工具使用

### 4.1 T³: Reducing Belief Deviation in Reinforcement Learning for Active Reasoning of LLM Agents

| 项目 | 内容 |
|------|------|
| **标题** | Reducing Belief Deviation in Reinforcement Learning for Active Reasoning of LLM Agents |
| **中文** | 减少 RL 中的信念偏差用于 LLM Agent 主动推理 |
| **链接** | ICLR 2026 Oral |

**问题背景**:
主动推理要求 LLM Agent 与外部源交互并战略性收集信息。核心是信念追踪 (belief tracking)。但 LLM Agent 常常发生信念偏差 (belief deviation)，偏离真实问题状态。

**方法详述**:
提出 **T³** 方法：检测过度偏差并截断训练轨迹以抑制无信息尾部效应，保留信息性前缀的 credit，系统改善策略优化。

**实验结果**:
在 5 个挑战性任务上一致提升训练稳定性，性能提升达 30 个百分点，同时 token 成本降低最多 34%。

### 4.2 ExpA: Expanding the Action Space of LLMs to Reason Beyond Language

| 项目 | 内容 |
|------|------|
| **标题** | Expanding the Action Space of LLMs to Reason Beyond Language (ExpA) |
| **中文** | 扩展 LLM 动作空间以超越语言进行推理 |
| **链接** | ICLR 2026 |

**方法详述**:
将环境交互从语言中解耦，**内化到扩展动作空间 (ExpA)** — 超越词汇表。引入 **EARL** (ExpA RL)，使用反事实策略优化。模型可在语言环境和外部环境间切换。

**实验结果**:
在需要多轮交互和条件规划的任务上，EARL 超越词汇约束动作的强基线。在部分可观测排序问题上实现完美 Sort-4 准确率，算法效率堪比经典设计。

### 4.3 MedAgentGym: A Scalable Agentic Training Environment for Code-Centric Reasoning

| 项目 | 内容 |
|------|------|
| **标题** | MedAgentGym: A Scalable Agentic Training Environment for Code-Centric Reasoning in Biomedical Data Science |
| **中文** | MedAgentGym: 可扩展的 Agent 训练环境用于生物医学代码推理 |
| **链接** | ICLR 2026 Oral |

**方法详述**:
72,413 个任务实例，涵盖 129 个类别、12 个真实生物医学场景。封装于可执行沙箱环境。29 个 LLM 的广泛评估显示商业与开源模型间显著差距。

**实验结果**:
Med-Copilot 通过离线 RL 提升 +43.02%，在线 RL 提升 +45.28%，达到与 GPT-4o 竞争的性能。

### 4.4 MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent

| 项目 | 内容 |
|------|------|
| **标题** | MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent |
| **中文** | MemAgent: 基于多轮 RL 记忆重塑长上下文 LLM |
| **链接** | ICLR 2026 Oral |

**方法详述**:
通过多轮强化学习训练记忆管理策略，使 LLM 在超长上下文中有效利用历史信息。

---

## 5. KDD 2026

> **时间**: 2026年8月9–13日，韩国济州岛 | **Key Theme**: CTR 缩放理论、工业推荐系统前沿

### 5.1 FAT: From Scaling to Structured Expressivity — Rethinking Transformers for CTR Prediction

| 项目 | 内容 |
|------|------|
| **标题** | From Scaling to Structured Expressivity: Rethinking Transformers for CTR Prediction (FAT) |
| **中文** | FAT: 从缩放到结构化表达能力 — 重新思考 CTR 预测的 Transformer |
| **作者** | 多作者 |
| **机构** | Alibaba |
| **链接** | KDD 2026 |

**问题背景**:
深度 CTR 模型投入巨大但仍呈现快速递减收益，与 LLM 中可预测的缩放律形成鲜明对比。根源在于标准 Transformer 假设序列组合性，而 CTR 数据需要跨异构域的**组合推理** (combinatorial reasoning)。

**方法详述**:
提出 **Field-Aware Transformer (FAT)** — 使用域感知参数重构标准 Transformer 块。核心：**Basis-Composed Hypernetwork** 从共享基合成域特定参数。理论上基于 Rademacher 复杂度形式化缩放律。

**实验结果**:
AUC 提升最高 +4.38%，线上 CTR +2.33%，RPM +0.66%。P99 延迟仅 133ms 满足工业部署。

### 5.2 FCN: Fusing Exponential and Linear Cross Network for CTR Prediction

| 项目 | 内容 |
|------|------|
| **标题** | FCN: Fusing Exponential and Linear Cross Network for Click-Through Rate Prediction |
| **中文** | FCN: 融合指数和线性交叉网络的 CTR 预测 |
| **机构** | — |
| **链接** | KDD 2026 |

**方法详述**:
(1) **ECN (指数交叉网络)** — 捕获极高阶显式特征交互；(2) **LCN (线性交叉网络)** — 捕获线性增长的低阶特征交互；(3) 低代价聚合方法减少 23% 推理延迟。

**实验结果**:
在 6 个数据集上平均 AUC 提升 0.25% 超越最强基线，Logloss 降低 0.19%。

### 5.3 GR4AD: Generative Recommendation for Large-Scale Advertising

| 项目 | 内容 |
|------|------|
| **标题** | GR4AD: Generative Recommendation for Large-Scale Advertising |
| **中文** | GR4AD: 大规模广告的生成式推荐 |
| **作者** | 多作者 |
| **机构** | Kuaishou Technology |
| **链接** | arXiv: 2602.22732 |

**方法详述**:
面向广告的生产级生成式推荐：(1) **UA-SID** — 基于微调 MLLM embedding 的统一广告语义 ID；(2) **MGMR** — 多粒度多分辨率 RQ-Kmeans 量化；(3) **VSL** (价值感知监督学习) + **RSPO** (排序引导 Softmax 偏好优化，list-wise RL)；(4) **LazyAR** 解码器 — 放松层间自回归依赖。

**实验结果**:
广告收入提升最多 4.2%，已全量部署在 Kuaishou 广告系统，服务 4 亿+ 用户。延迟 <100ms, QPS 500+。

### 5.4 OneRanker: Unified Generation and Ranking with One Model in Industrial Advertising Recommendation

| 项目 | 内容 |
|------|------|
| **标题** | OneRanker: Unified Generation and Ranking with One Model in Industrial Advertising Recommendation |
| **中文** | OneRanker: 工业广告推荐中的统一生成与排序 |
| **作者** | 多作者 |
| **机构** | Tencent (微信广告) |
| **链接** | arXiv: 2603.02999 |

**方法详述**:
实现生成与排序架构级深度整合：(1) 价值感知多任务解耦架构；(2) 由粗到细的协同目标感知机制 (Fake Item Tokens + 排序解码器)；(3) 输入-输出双端一致性保证 (KV 穿透 + 分布一致性约束)。

**实验结果**:
全量部署于微信渠道广告系统，GMV +1.34%。

### 5.5 其他 KDD 2026 论文

| 论文 | 主题 | 机构 |
|------|------|------|
| HAP: Heterogeneity-Aware Adaptive Pre-ranking | 预排序异构自适应 | ByteDance (Toutiao) |
| KLAN: Kuaishou Landing-page Adaptive Navigator | 落地页个性化导航 | Kuaishou (DAU +0.205%) |
| OneMall: End-to-End Generative Recommender Family at Kuaishou | 多场景生成式推荐 | Kuaishou (GMV +4.9~14.7%) |
| OneLive: Dynamically Unified Generative Framework for Live-Streaming | 直播生成式推荐 | Kuaishou |
| Internalizing Multi-Agent Reasoning (STAR) | 多 Agent 推理内化 | Tencent |
| HAP: Heterogeneity-Aware Pre-ranking (HAP) | 异构预排序 | ByteDance |

---

## 6. CVPR 2026

> **时间**: 2026年6月 | **Key Theme**: 生成模型 + 推理融合、3D 生成

### 6.1 Thinking-while-Generating (TWIG): Interleaving Textual Reasoning throughout Visual Generation

| 项目 | 内容 |
|------|------|
| **标题** | Thinking-while-Generating: Interleaving Textual Reasoning throughout Visual Generation |
| **中文** | Thinking-while-Generating: 在整个视觉生成过程中交织文本推理 |
| **作者** | Ziyu Guo, Renrui Zhang, Hongyu Li, Manyuan Zhang 等 |
| **机构** | 上海人工智能实验室 / 北京大学 |
| **链接** | CVPR 2026 |

**方法详述**:
首个将文本推理保持在视觉生成循环中的交织框架。(1) 模型先解释指令并规划交织调度；(2) 生成每个区域时进行**即时文本推理**并基于当前视觉状态进行 grounding；(3) 推理步骤提供精细指导并审视已生成内容。

**关键技术路线**: 支持扩散、离散扩散、自回归多种生成范式。以 Janus-Pro 为骨干进行端到端训练。

### 6.2 Thoughtful3D: Structural Chain-of-Thought Reasoning for Consistent 3D Generation

| 项目 | 内容 |
|------|------|
| **标题** | Think-Then-Generate: Structural Chain-of-Thought Reasoning for Consistent 3D Generation |
| **中文** | Thoughtful3D: 结构链式推理实现一致 3D 生成 |
| **作者** | Xinyue Liu, Jin Liu, Hongbo Wang, Ran He, Huaibo Huang |
| **机构** | 中国科学院 |
| **链接** | CVPR 2026 |

**方法详述**:
(1) **3DBlueprint-CoT** — 通过文本语义解析和逻辑推导显式规划 3D 生成过程；(2) **3DRefine-CoT** — 动态评估跨视角不一致性，多轮迭代细化；(3) **跨视图语义外观对齐** — 建立不同视角相同特征的动态几何关联。

### 6.3 其他 CVPR 2026 重要论文

| 论文 | 主题 | 机构 |
|------|------|------|
| Gen3R: 3D Scene Generation Meets Feed-Forward Reconstruction | 3D 场景生成 + 重建 | — |
| PartDiffuser: Part-wise 3D Mesh Generation via Discrete Diffusion | 部分级 3D 网格生成 | — |
| Scone: Subject-Driven Image Generation | 主题驱动图像生成 (组合 + 区分) | — |
| SenseSearch: Empowering VLMs with High-Resolution Agentic Search-Reasoning via RL | VLM 搜索推理 | — |
| PersonaVLM: Long-Term Personalized Multimodal LLMs | 长期个性化多模态 LLM | — |
| UniVerse: Empower Unified Generation with Reasoning and Knowledge | 统一生成 + 推理 + 知识 | — |
| A Frame is Worth One Token: Efficient Generative World Modeling | 高效生成世界模型 (Delta Tokens) | NVIDIA |

---

## 7. ACL 2026 & EMNLP 2025

### 7.1 EMNLP 2025 — Agent 安全与工具使用

| 论文 | 主题 | 机构 |
|------|------|------|
| Preemptive Detection of Misaligned Actions in LLM Agents | Agent 错误动作预防检测 | — |
| IPIGuard: Defending Against Indirect Prompt Injection in LLM Agents | 间接提示注入防御 | — |
| DatawiseAgent: Notebook-Centric LLM Agent for Data Science | 数据科学 Agent | — |
| REARANK: Reasoning Re-ranking Agent via RL | RL 推理重排序 Agent | — |
| SAND: Boosting LLM Agents with Self-Taught Action Deliberation | 自教行动审慎 Agent | — |
| Search-o1: Agentic Search-Enhanced Large Reasoning Models | 搜索增强推理 | — |
| LMR-BENCH: Evaluating LLM Agent on Reproducing Language Modeling Research | 代码复现 Agent 基准 | — |
| AgentPro: Enhancing LLM Agents with Automated Process Supervision | 自动化过程监督 (MCTS + PRM) | — |
| LLM-based Conversational Recommendation Agents with Collaborative Verbalized Experience | 对话推荐 Agent | — |
| GenPilot: Multi-Agent System for Test-Time Prompt Optimization | 多 Agent prompt 优化 | — |

### 7.2 EMNLP 2025 — AgentPro 详细

| 项目 | 内容 |
|------|------|
| **标题** | AgentPro: Enhancing LLM Agents with Automated Process Supervision |
| **中文** | AgentPro: 自动化过程监督增强 LLM Agent |
| **链接** | EMNLP 2025 |

**方法详述**:
使用 MCTS 自动生成步级标注并训练过程奖励模型 (PRM)。通过拒绝采样策略动态调整生成概率分布，阻止错误路径继续。

**实验结果**:
HotpotQA 准确率 +6.32%，在 4 个数据集上显著超越现有 agent-based LLM 方法。

### 7.3 ManuSearch: Democratizing Deep Search — Open Multi-Agent Framework

| 项目 | 内容 |
|------|------|
| **标题** | ManuSearch: Democratizing Deep Search in LLMs with a Transparent and Open Multi-Agent Framework |
| **中文** | ManuSearch: 透明开放的多 Agent 深度搜索框架 |
| **链接** | EMNLP 2025 Findings |

**方法详述**:
三个协作 Agent：(1) 解决方案规划 Agent — 迭代制定子查询；(2) 互联网搜索 Agent；(3) 结构化网页阅读 Agent。配合 **ORION 基准** (开放网页长尾实体推理，中英双语)。

**实验结果**:
显著超越开源基线，甚至超越领先闭源系统。

---

## 8. SIGIR 2026

> **时间**: 2026年7月20–24日，澳大利亚墨尔本 | **Key Theme**: LLM 推荐、生成式检索、RAG

### 8.1 SIGMA: Semantic-Grounded Instruction-Driven Generative Multi-Task Recommender at AliExpress

| 项目 | 内容 |
|------|------|
| **标题** | SIGMA: A Semantic-Grounded Instruction-Driven Generative Multi-Task Recommender at AliExpress |
| **中文** | SIGMA: 阿里巴巴 AliExpress 语义驱动指令型生成式多任务推荐 |
| **作者** | 多作者 |
| **机构** | Alibaba (AliExpress) |
| **链接** | arXiv: 2602.22913 / SIGIR 2026 |

**方法详述**:
(1) **多视角对齐框架** — 在统一语义空间中对齐自然语言、世界知识和物品实体；(2) **混合物品 Tokenization** — SID 前缀 + 物品特定 ID token；(3) **大规模多任务 SFT 数据集**；(4) **三步物品生成流程** + 自适应概率融合机制。

**实验结果**:
在 AliExpress 多任务线上 A/B 测试中展示有效性。

### 8.2 GenRec: Preference-Oriented Generative Framework for Large-Scale Recommendation

| 项目 | 内容 |
|------|------|
| **标题** | GenRec: A Preference-Oriented Generative Framework for Large-Scale Recommendation |
| **中文** | GenRec: 面向偏好的大规模生成式推荐框架 |
| **链接** | SIGIR 2026 |

**方法详述**:
基于 SID 的表示 + **GRPO-SR** (带监督正则化的 GRPO) 偏好对齐。解决分页机制下多正例、长行为序列计算开销、奖励 hack 三大挑战。

### 8.3 GFlowGR: Fine-tuning Generative Recommendation with Generative Flow Networks

| 项目 | 内容 |
|------|------|
| **标题** | GFlowGR: Fine-tuning Generative Recommendation Frameworks with Generative Flow Networks |
| **中文** | GFlowGR: 基于 GFlowNet 的生成式推荐微调 |
| **链接** | SIGIR 2026 |

**方法详述**:
重新将 GR 构建为**序列集合生成问题**，使用 GFlowNet 目标提供 token 级学习信号。三大组件：(1) 轨迹采样器；(2) 行为感知奖励模型；(3) GFlowNet 目标。

**实验结果**:
年收入相对提升 4%。

### 8.4 其他 SIGIR 2026 论文

| 论文 | 主题 | 机构 |
|------|------|------|
| ItemRAG: Item-Based RAG for LLM Recommendation | 物品级 RAG | — |
| BEAR: Beam-Search-Aware Optimization for LLM Recommendation | Beam Search 感知优化 | — |
| SPRINT: Scalable and Predictive Intent Refinement for LLM-Enhanced Session-based Rec | 会话推荐意图提炼 | — |

---

## 9. WWW 2026

> **时间**: 2026年4月13–17日，迪拜 | **Key Theme**: LLM Agent 推荐、思考式推荐

### 9.1 ThinkRec: Thinking-based Recommendation via LLM

| 项目 | 内容 |
|------|------|
| **标题** | ThinkRec: Thinking-based recommendation via LLM |
| **中文** | ThinkRec: 基于思考的 LLM 推荐 |
| **作者** | 多作者 |
| **机构** | — |
| **链接** | [WWW 2026](https://dl.acm.org/doi/10.1145/3774904.3792070) |

**问题背景**:
现有 LLM4Rec 方法以 System 1 方式运作，依赖表面特征匹配，而非深入推理行为逻辑。

**方法详述**:
(1) **思考激活机制** — 注入合成推理轨迹使推荐过程类似 CoT 推理；(2) **实例级专家融合** — 基于用户潜在特征动态分配专家权重，自适应推理路径。

**实验结果**:
在多个真实 Web 行为偏好数据集上显著超越基线。

### 9.2 AgentDR: Dynamic Recommendation with Implicit Item-Item Relations via LLM Agents

| 项目 | 内容 |
|------|------|
| **标题** | AgentDR: Dynamic Recommendation with Implicit Item-Item Relations via LLM-based Agents |
| **中文** | AgentDR: 基于 LLM Agent 的隐式物品关系动态推荐 |
| **链接** | WWW 2026 |

**方法详述**:
LLM Agent 桥接 LLM 推理与可扩展推荐工具：(1) 基于个性化工具适用性整合多个推荐输出；(2) 基于替代和互补关系推理用户意图。

**实验结果**:
在公开杂货数据集上实现平均两倍于基线的全目录排名性能提升。

### 9.3 其他 WWW 2026 论文

| 论文 | 主题 | 机构 |
|------|------|------|
| ISRF: Iterative Semantic Reasoning from Individual to Group Interests | 个体到群体兴趣的迭代语义推理 | — |
| SEDIRec: LLM-Enhanced Semantic Diffusion for User-Centric Rec | 语义扩散推荐 | — |
| IAM: Item-aware Attention Mechanism for LLM Recommendation | 物品感知注意力 | — |
| HAP: Heterogeneity-Aware Adaptive Pre-ranking | 异构自适应预排序 | ByteDance |
| DualGR: Generative Retrieval with Long/Short-Term Interests | 长短期兴趣生成式检索 | Kuaishou |
| LLM Retrieval for Stable and Predictable Ad Recommendations | 广告稳定可预测 LLM 检索 | LinkedIn |

---

## 10. CIKM 2025

> **时间**: 2025年11月10–14日，韩国首尔

### 10.1 Climber: Toward Efficient Scaling Laws for Large Recommendation Models

| 项目 | 内容 |
|------|------|
| **标题** | Climber: Toward Efficient Scaling Laws for Large Recommendation Models |
| **中文** | Climber: 大规模推荐模型的高效缩放律 |
| **作者** | Songpei Xu, Shijia Wang, Da Guo 等 |
| **机构** | NetEase Cloud Music |
| **链接** | CIKM 2025 |

**方法详述**:
高效缩放框架，针对多尺度、多场景、多兴趣的推荐模型。提出特定的加速技术。

**实验结果**:
持续实现在线指标增长 (12.19% 整体提升)。已在网易云音乐成功部署。

### 10.2 其他 CIKM 2025 论文

| 论文 | 主题 |
|------|------|
| STARec: Agent Framework via Autonomous Deliberate Reasoning | 慢思考 Agent 推荐 |
| Prompt Tuning as User Inherent Profile Inference | prompt 调优用户画像 |
| MUFFIN: Mixture of User-Adaptive Frequency Filtering for Sequential Rec | 自适应频率过滤序列推荐 |
| LLMTreeRec: LLM for Cold-Start Recommendations | 冷启动 LLM 推荐 |
| LLM-Powered User Simulator for Recommender System | LLM 用户模拟器 |

---

## 11. RecSys 2025

> **时间**: 2025年9月，布拉格 | **Key Theme**: 负责任的推荐、用户控制

### 11.1 Best Paper: You Don't Bring Me Flowers — Mitigating Unwanted Recommendations Through Conformal Risk Control

| 项目 | 内容 |
|------|------|
| **标题** | You Don't Bring Me Flowers: Mitigating Unwanted Recommendations Through Conformal Risk Control |
| **中文** | 通过共形风险控制减少不想要的推荐 |
| **作者** | Giovanni De Toni, Erasmo Purificato, Emilia Gomez, Andrea Passerini, Bruno Lepri, Cristian Consonni |
| **机构** | European Commission JRC / University of Trento / FBK |
| **链接** | RecSys 2025 Best Paper |

**方法详述**:
应用**共形风险控制 (conformal risk control)** 为用户提供控制不想要推荐的能力。在方法论强度和社会影响方面获得评审委员会一致认可。

### 11.2 其他 RecSys 2025 论文

| 论文 | 主题 |
|------|------|
| RESA: Language Model-Based Playlist Generation | 播放列表生成 |
| GenSAR: SAR for Sequential Recommendation | 顺序推荐 |
| Enhancing Sequential Recommender with LLM for Joint Video and Comment Rec | 视频 + 评论联合推荐 |
| LONGER: Ultra-Long User Behavior Sequences | 超长用户行为序列 (ByteDance) |

---

## 12. arXiv 亮点 — GRPO 训练与推理

### 12.1 Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models

| 项目 | 内容 |
|------|------|
| **标题** | Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models |
| **中文** | GRPO 训练的高效预测缩放律 |
| **arXiv** | 2507.18014 |

**核心发现**:
GRPO reward 曲线可近似为**指数饱和**，三个阶段：(i) 初始缓慢进展，(ii) 快速提升，(iii) 饱和。约 80% 的单 epoch 训练后 reward 增益可忽略。预测缩放律使从业者可提前预测阶段转换并选择数据驱动停止点，大幅减少 GRPO 计算成本。

### 12.2 Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning

| 项目 | 内容 |
|------|------|
| **标题** | Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning |
| **中文** | Prompt 增强扩展 GRPO 数学推理训练 |
| **arXiv** | 2602.03190 |

**方法详述**:
引入 **prompt 增强** — 在多种模板和格式下生成推理轨迹，增加 rollout 多样性。无 KL 正则化项的 prompt 增强使模型能在低熵区域稳定训练。

**实验结果**:
Qwen2.5-Math-1.5B 在 AIME24、AMC、MATH500、Minerva、OlympiadBench 上达到 44.5 per-benchmark / 51.3 per-question 准确率 SOTA。

### 12.3 Multi-Task GRPO (MT-GRPO): Reliable LLM Reasoning Across Tasks

| 项目 | 内容 |
|------|------|
| **标题** | Multi-Task GRPO: Reliable LLM Reasoning Across Tasks |
| **中文** | MT-GRPO: 跨任务可靠的 LLM 推理 |
| **arXiv** | 2602.05547 |

**方法详述**:
(1) **改进感知任务重加权** — 动态调整任务权重以优化最差任务性能；(2) **比例保持采样器** — 确保任务策略梯度反映调整后的权重。

**实验结果**:
最差任务性能绝对提升 16–28%（vs GRPO），比 DAPO 高 6%。训练 3 任务设定中达到 50% 最差任务准确率所需步骤减少 50%。

### 12.4 GRPO-VPS: Enhancing GRPO with Verifiable Process Supervision

| 项目 | 内容 |
|------|------|
| **标题** | GRPO-VPS: Enhancing Group Relative Policy Optimization with Verifiable Process Supervision |
| **中文** | GRPO-VPS: 可验证过程监督增强 GRPO |
| **arXiv** | 2604.20659 |

**方法详述**:
通过探测模型在整个推理轨迹中对正确答案的条件概率进行分段监督。计算**可解释的段级进展度量**来细化 GRPO 的轨迹级反馈。

**实验结果**:
数学任务准确率 +2.6 分，推理长度 -13.7%；通用域任务 +2.4 分，长度 -4%。

### 12.5 Latent-GRPO: Group Relative Policy Optimization for Latent Reasoning

| 项目 | 内容 |
|------|------|
| **标题** | Latent-GRPO: Group Relative Policy Optimization for Latent Reasoning |
| **中文** | Latent-GRPO: 潜在推理的分组相对策略优化 |
| **arXiv** | 2604.27998 |

**方法详述**:
解决潜在推理 + RL 的三个耦合瓶颈：(1) 无内在潜在流形 → **无效样本优势掩码**；(2) 探索-优化错位 → **单侧噪声采样**；(3) 潜在混合非封闭性 → **最优正确路径首 Token 选择**。

**实验结果**:
低难度任务 (GSM8K-Aug) 上 +7.86 Pass@1，高难度任务 (AIME) 超越显式 GRPO 4.27 分，同时推理链长度缩短 3–4 倍。

### 12.6 iGRPO: Self-Feedback–Driven LLM Reasoning

| 项目 | 内容 |
|------|------|
| **标题** | iGRPO: Self-Feedback–Driven LLM Reasoning |
| **中文** | iGRPO: 自我反馈驱动的 LLM 推理 |
| **arXiv** | 2602.09000 |

**方法详述**:
两阶段：(1) 采样多个探索性草稿并选择最高 reward 草稿；(2) 将该最佳草稿附加到原始 prompt 进行 GRPO 更新。

**实验结果**:
OpenReasoning-Nemotron-7B 在 AIME24 上达到 85.62%，AIME25 上达到 79.64% SOTA。

### 12.7 Group DRO-Driven RL for LLM Reasoning

| 项目 | 内容 |
|------|------|
| **标题** | Group Distributionally Robust Optimization-Driven Reinforcement Learning for LLM Reasoning |
| **中文** | 分组分布鲁棒优化驱动的 LLM 推理 RL |
| **arXiv** | 2601.19280 |

**方法详述**:
(1) **Prompt-GDRO** — EMA 去偏乘性权重 bandit 采样器上重困难样本；(2) **Rollout-GDRO** — 影子价格控制器跨组重分配 rollout 预算。

**实验结果**:
Qwen3-Base (1.7B/4B/8B) 上 pass@8 相对提升 +9~13%。

### 12.8 Scaling Behaviors of LLM RL Post-Training

| 项目 | 内容 |
|------|------|
| **标题** | Scaling Behaviors of LLM Reinforcement Learning Post-Training: An Empirical Study in Mathematical Reasoning |
| **中文** | LLM RL 后训练的缩放行为实证研究 |
| **arXiv** | 2509.25300 |

**核心发现**:
(1) 固定预算下大模型少步训练始终优于小模型多步；(2) 固定数据量下大模型样本效率更高；(3) 数据受限时重复使用高质量数据高度有效；(4) 缩放行为在 base 和 instruct 模型上均鲁棒。

---

## 总结：2026-06-13 关键趋势

### 1. GRPO 成为推理训练的核心范式
从 Predictive Scaling Laws 到 Latent-GRPO、MT-GRPO、iGRPO，GRPO 的变体和理论分析齐头并进。核心挑战转向：稳定性、多任务平衡、过程监督、潜在空间适配。

### 2. 推荐系统全面进入「推理时代」
NeurIPS 2025 的 RecZero/R²ec、WWW 2026 的 ThinkRec、CIKM 2025 的 STARec，一致指向将 CoT/RL 推理能力注入推荐系统。生成式推荐 (SIGMA、GenRec、GFlowGR、OneMall) 从理论走向大规模工业部署。

### 3. Agent 系统「学习化」
ICML 2026 的 ML-Agent、KLong、SciAgentGym 标志着 Agent 从 prompt 工程转向学习范式。RL-based agent 训练 (MCTS、PRM、GRPO) 成为主流。

### 4. 游戏 RL 反哺 LLM 推理
SPIRAL、Stratagem、TiG、Odysseus 等研究表明：游戏环境的 self-play RL 训练可有效提升 LLM 的数学推理、代码生成和规划能力。

### 5. 多模态生成模型的推理融合
CVPR 2026 的 TWIG、Thoughtful3D 开启将链式推理直接注入视觉生成过程的新范式。

### 6. CTR 从「更深更宽」转向「结构化表达」
FAT (KDD 2026) 从理论上证明：CTR 需要组合推理而非序列组合性，提出域感知 Transformer + Rademacher 缩放律。
