---
title: 顶会论文专题报告 — 2026年6月全面版
type: synthesis
created: 2026-06-17
updated: 2026-06-17
sources: [arxiv-search]
tags: [conference-digest, ICML-2026, AAAI-2026, NeurIPS-2025, ICLR-2026, CVPR-2026, KDD-2026, ACL-2026, EMNLP-2025, SIGIR-2026, WWW-2026, CIKM-2025, RecSys-2025, LLM, recommendation, CTR, agents]
---

# 顶会论文专题报告 — 2026年6月全面版

> 基于 arXiv、各会议官网及 proceedings 的综合检索，覆盖 ICML 2026、AAAI 2026、NeurIPS 2025、ICLR 2026、CVPR 2026、KDD 2026、ACL 2026、EMNLP 2025、SIGIR 2026、WWW 2026、CIKM 2025、RecSys 2025 等 12+ 个会议/venues，收录 70+ 篇论文，涵盖 LLM、推荐系统/CTR、Agent 系统、多模态、代码执行预测、强化学习、序列建模等领域。

---

## 目录

1. [Frontier Model Reports — 前沿模型技术报告](#1-frontier-model-reports)
2. [ICML 2026 — 国际机器学习大会](#2-icml-2026)
3. [ICLR 2026 — 国际学习表征大会](#3-iclr-2026)
4. [AAAI 2026 — 人工智能顶级会议](#4-aaai-2026)
5. [NeurIPS 2025 — 神经信息处理系统大会](#5-neurips-2025)
6. [CVPR 2026 — 计算机视觉与模式识别](#6-cvpr-2026)
7. [ACL 2026 / EMNLP 2025 — 自然语言处理](#7-acl-2026--emnlp-2025)
8. [KDD 2026 — 知识发现与数据挖掘](#8-kdd-2026)
9. [SIGIR 2026 — 信息检索研究](#9-sigir-2026)
10. [WWW 2026 — 万维网大会](#10-www-2026)
11. [CIKM 2025 / RecSys 2025 — 信息管理/推荐系统](#11-cikm-2025--recsys-2025)
12. [Agents & Code Execution — Agent系统与代码执行预测](#12-agents--code-execution)
13. [生成模型与序列建模](#13-生成模型与序列建模)

---

## 1. Frontier Model Reports

### 1.1 GPT-5.5 System Card

| 项目 | 内容 |
|------|------|
| **标题** | GPT-5.5 System Card |
| **作者** | OpenAI |
| **时间** | 2026-04-23 |
| **链接** | https://openai.com/index/gpt-5-5-system-card/ |
| **代号** | Spud |

**关键信息：**
- 自 GPT-4.5 (2024年初) 以来首次完整重新预训练的基座模型
- 预训练语料：~18T tokens（去重后），合成数据占比 < 30%
- Post-training 四阶段管线：SFT → RLHF → Tool-use RL with verifiable rewards → Constitutional refinement
- 上下文窗口：1M tokens（922K 输入，128K 输出）
- 原生 Computer Use 能力，OSWorld-Verified 达 75.0%（超越人类基线 72.4%）
- SWE-bench Pro: 58.6%, Terminal-Bench 2.0: 82.7%, BrowseComp: 84.4%
- Arena text leaderboard ELO 1480

### 1.2 Claude Opus 4.7

| 项目 | 内容 |
|------|------|
| **标题** | Claude Opus 4.7 |
| **作者** | Anthropic |
| **时间** | 2026-04-16 |
| **链接** | https://www.anthropic.com/news/claude-opus-4-7 |
| **arXiv** | 2604.09881 |

**关键信息：**
- SWE-bench Verified: 87.6%（Opus 4.6 为 80.8%）
- SWE-bench Pro: 64.3%（Opus 4.6 为 53.4%）
- GPQA Diamond: 94.2%
- Terminal-Bench 2.0: 69.4%
- 上下文窗口：1M tokens，最大输出 128K tokens
- 新增 xhigh effort level
- 图像分辨率提升至 2,576px / 3.75MP
- 定价不变：$5/$25 per M input/output tokens
- ⚠️ 长上下文检索显著回退：8-needle @256k 从 91.9% 降至 59.2%
- 内部保留更强模型 Claude Mythos Preview 未公开发布

### 1.3 DeepSeek V4 Technical Report

| 项目 | 内容 |
|------|------|
| **标题** | DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence |
| **作者** | DeepSeek-AI |
| **时间** | 2026-04-24 |
| **链接** | https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro |
| **arXiv** | https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf |

**关键信息：**
- V4-Pro: 1.6T 总参数 / 49B 激活 (MoE)
- V4-Flash: 284B 总参数 / 13B 激活 (MoE)
- 均支持 1M token 上下文窗口
- 混合注意力架构：Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA)
- 相比 V3.2: 1M 上下文下推理 FLOPs 仅 27%，KV cache 仅 10%
- Manifold-Constrained Hyper-Connections (mHC) 增强残差连接
- Muon Optimizer 加速收敛
- 预训练 >32T tokens
- 后训练：两阶段范式（独立培养领域专家 → 模型整合）
- MIT 开源协议
- MMLU-Pro: 87.5, LiveCodeBench: 93.5, SWE Verified: 80.6
- 定价：$1.74/$3.48 per M input/output tokens（约 GPT-5.5 的 1/9）

### 1.4 前沿模型对比总览 (2026年4-5月)

| 维度 | DeepSeek V4-Pro | Claude Opus 4.7 | GPT-5.5 |
|------|--------|--------|--------|
| 参数 | 1.6T/49B active MoE | 未公开 | 未公开 |
| 架构 | MoE + Engram Memory | Transformer + Extended Thinking | Transformer (Spud pretrain) |
| 上下文 | 1M tokens | 1M/128K out | 1M tokens |
| 输入价格 | $1.74/M | $15/M (CAISI口径) | $5/M |
| 输出价格 | $3.48/M | $25/M | $30/M |
| 开源 | MIT | 否 | 否 |
| SWE-bench Pro | 55.4% | 64.3% | 58.6% |
| LiveCodeBench | 93.5 | 88.8 | — |
| GPQA Diamond | 90.1 | 94.2 | — |
| 定位 | 性价比/开源之王 | 代码/安全之王 | Agent/通用之王 |

---

## 2. ICML 2026

### 2.1 Reasoning & RL

#### From Reasoning Traces to Reusable Modules: RL for Compositional Generalization

| 项目 | 内容 |
|------|------|
| **标题** | From Reasoning Traces to Reusable Modules: Reinforcement Learning for Compositional Generalization in Language Model Reasoning |
| **作者** | Lingjing Kong, Xin Liu, Guangyi Chen, Martin Q. Ma, Xiangchen Song, Yuekai Sun, Mikhail Yurochkin, Taylor W. Killian, Russ Salakhutdinov, Kun Zhang, Eric Xing, Zhengzhong Liu |
| **Venue** | ICML 2026 Poster |
| **链接** | https://icml.cc/virtual/2026/poster/61216 |

**核心贡献：**
- 理论证明 RL 的探索性能够提供足够覆盖以识别潜在结构并实现组合泛化
- 提出 Hierarchical Latent Selection Model 框架
- 实验证明 RL 可从复合轨迹提取原子模块并重新组合解决新配置
- 关键发现：在复合轨迹上训练比在隔离原子模块上训练产生更强的泛化
- 有效协议：SFT 确保所有原子模块覆盖，RL 聚焦于 SFT 支持集之外的新组合

#### The Flexibility Trap: Rethinking Arbitrary Order in Diffusion Language Models

| 项目 | 内容 |
|------|------|
| **标题** | The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models |
| **作者** | Zanlin Ni, Shenzhi Wang, Yang Yue, Tianyu Yu, Weilin Zhao, Yeguo Hua, Tianyi Chen, Jun Song, Yu Cheng, Bo Zheng, Gao Huang |
| **Venue** | ICML 2026 Oral |
| **链接** | https://icml.cc/virtual/2026/oral/71086 |

**核心贡献：**
- 揭示 dLLM 的任意顺序生成可能限制推理潜力
- dLLM 倾向于利用顺序灵活性绕过高不确定性 token，导致解覆盖过早崩溃
- 提出 JustGRPO：放弃任意顺序，应用标准 GRPO
- GSM8K 达 89.1% 准确率，同时完全保留并行解码能力

#### In-Context Reinforcement Learning for Tool Use in LLMs

| 项目 | 内容 |
|------|------|
| **标题** | In-Context Reinforcement Learning for Tool Use in Large Language Models |
| **作者** | Yaoqi Ye, Yiran Zhao, Keyu Duan, Zeyu Zheng, Kenji Kawaguchi, Cihang Xie, Michael Qizhe Shieh |
| **Venue** | ICML 2026 |
| **arXiv** | 2603.08068 |
| **代码** | https://github.com/applese233/ICRL |

**核心贡献：**
- 提出 ICRL：纯 RL 框架，无需 SFT，通过 few-shot prompting 在教学阶段指导工具调用
- 训练过程中逐步减少 in-context 示例数量，最终达到 zero-shot 工具调用
- 在多种推理和工具使用基准上达到 SOTA

### 2.2 Agent Papers (ICML 2026 Agent Track)

ICML 2026 收录约 465 篇 Agent 相关论文，涵盖以下子方向：

| 方向 | 论文数 | 说明 |
|------|--------|------|
| Benchmarks & Evaluation | 99 | 长时域、GUI/Web、科学、金融等领域 Agent 评估 |
| Multi-Agent Systems & MARL | 93 | LLM 多智能体辩论、合作、协议选择、社会模拟 |
| Tool Use, Training & RL | 58 | 从 prompt-based 到可训练 Agent：tool-use RL、GRPO、trajectory-SFT |
| Safety, Security & Governance | 51 | Agent 安全、对齐、治理 |
| Theory, Behavior & Interpretability | 39 | Agent 理论、行为分析、可解释性 |
| GUI, Web & Computer-Use | 19 | 桌面、移动、Web GUI Agent |

---

## 3. ICLR 2026

### 3.1 Training LLMs to Reason in Parallel with Global Forking Tokens

| 项目 | 内容 |
|------|------|
| **标题** | Training Large Language Models To Reason In Parallel With Global Forking Tokens |
| **作者** | — |
| **Venue** | ICLR 2026 |
| **arXiv** | 2510.05132 |

**核心贡献：**
- 将并行推理视为 set-of-next-token-prediction 问题
- 提出 Set Supervised Fine-Tuning (SSFT)：使用二分匹配在全局分叉 token 和唯一推理轨迹之间建立对应
- Global Forking Policy Optimization (GFPO)：利用最大可引导 token 激励复杂推理
- 在数学推理和执行代码生成基准上持续优于 SFT + GRPO 对应模型

### 3.2 TIR-Judge: Tool-Integrated RL for LLM Judges

| 项目 | 内容 |
|------|------|
| **标题** | Incentivizing Agentic Reasoning in LLM Judges via Tool-Integrated Reinforcement Learning |
| **作者** | — |
| **Venue** | ICLR 2026 |
| **arXiv** | 2510.23038 |

**核心贡献：**
- 端到端 RL 框架：训练 LLM Judge 集成代码执行器进行精确评估
- 三大原则：可验证/不可验证领域的多样训练、灵活判断格式（pointwise/pairwise/listwise）、无蒸馏迭代 RL
- 7 个公开基准上超越强推理型 Judge 最高达 6.4%（pointwise）和 7.7%（pairwise）
- 8B 参数达到与 Claude-Opus-4 相当的 listwise 性能

### 3.3 ∇-Reasoner: Test-Time Gradient Descent in Latent Space

| 项目 | 内容 |
|------|------|
| **标题** | ∇-Reasoner: LLM Reasoning via Test-Time Gradient Descent in Latent Space |
| **作者** | — |
| **Venue** | ICLR 2026 |
| **arXiv** | 2603.04948 |

**核心贡献：**
- 将可微优化集成到解码循环中，在推理时精化策略
- Differentiable Textual Optimization (DTO)：利用 LLM 似然和奖励模型的梯度信号精化文本表征
- 结合拒绝采样和加速设计
- 理论上证明推理时梯度下降等价于 KL 正则化 RL 的 LLM 对齐
- 在数学推理基准上提升 >20% 准确率，同时减少 ~10-40% 模型调用

### 3.4 Mamba-3: Improved Sequence Modeling

| 项目 | 内容 |
|------|------|
| **标题** | Mamba-3: Improved Sequence Modeling using State Space Principles |
| **作者** | — |
| **Venue** | ICLR 2026 |

**核心贡献：**
- Mamba 架构的第三代演进
- 基于 State Space 原则改进序列建模能力
- 与 MoE、DeltaNet 等新架构共同推动非 Transformer 方案的发展

### 3.5 Rote Learning Considered Useful

| 项目 | 内容 |
|------|------|
| **标题** | Rote Learning Considered Useful: Generalizing over Memorized Data in LLMs |
| **作者** | — |
| **Venue** | ICLR 2026 |
| **arXiv** | 2507.21914 |

**核心贡献：**
- 提出 "memorize-then-generalize" 两阶段框架
- LLM 先死记硬背事实性主-客体关联（使用合成语义无意义 key token）
- 然后通过在少量语义有意义 prompt 上微调来泛化
- 8 个 LLM 上的实验证明模型可以通过语义有意义的 prompt 重新解释死记硬背的数据

### 3.6 Mixture-of-Experts Can Surpass Dense LLMs Under Equal Resource

| 项目 | 内容 |
|------|------|
| **标题** | Mixture-of-Experts Can Surpass Dense LLMs Under Strictly Equal Resource |
| **作者** | — |
| **Venue** | ICLR 2026 |

**核心贡献：**
- 在严格等资源条件下，MoE 可超越稠密 LLM
- 对 MoE 架构的边际效益进行了系统分析

### 3.7 ICLR 2026 Oral Highlights

| 论文 | 方向 |
|------|------|
| Benchmarking Empirical Privacy Protection for Adaptations of LLMs | 隐私保护 |
| MedAgentGym: Scalable Agentic Training for Biomedical Code Reasoning | Agent + 生物医学 |
| RAIN-Merging: Gradient-Free Enhancement for Instruction Following | 推理模型优化 |
| Universal Inverse Distillation for Matching Models with Real-Data Supervision | 蒸馏 |
| Vision-R1: Incentivizing Reasoning Capability in Multimodal LLMs | 多模态推理 |
| Half-order Fine-Tuning for Diffusion Model | 扩散模型 |
| Reducing Belief Deviation in RL for Active Reasoning of LLM Agents | Agent 推理 |
| Invisible Safety Threat: Malicious Finetuning via Steganography | 安全 |

---

## 4. AAAI 2026

### 4.1 LLM Reasoning (37 papers at AAAI 2026)

关键论文：

#### Trade-offs in Large Reasoning Models

| 项目 | 内容 |
|------|------|
| **标题** | Trade-offs in Large Reasoning Models: An Empirical Analysis of Deliberative and Adaptive Reasoning over Foundational Capabilities |
| **作者** | Weixiang Zhao, Xingyu Sui, Jiahe Guo, Yulin Hu, Yang Deng, Yanyan Zhao, Xuda Zhi, Yongbo Huang, Hao He, Wanxiang Che, Ting Liu, Bing Qin |
| **Venue** | AAAI 2026 |
| **链接** | https://doi.org/10.1609/aaai.v40i41.40802 |

**核心贡献：**
- 跨模型家族 (DeepSeek, Qwen, LLaMA) 和规模 (7B-32B) 的系统评估
- 揭示 deliberative reasoning 的获取显著降低了基础能力（helpfulness 和 harmlessness）
- 提出 adaptive reasoning 模式：Zero-Thinking, Less-Thinking, Summary-Thinking
- 自适应推理可有效缓解这些副作用

#### MathSmith: Synthetic Data for Hard Mathematical Reasoning

| 项目 | 内容 |
|------|------|
| **标题** | MathSmith: Towards Extremely Hard Mathematical Reasoning by Forging Synthetic Problems with a Reinforced Policy |
| **作者** | — |
| **Venue** | AAAI 2026 |
| **arXiv** | 2508.05592 |
| **代码** | https://github.com/Jasaxion/MathSmith |

**核心贡献：**
- 从零开始构建新问题（而非修改现有问题）
- 从 PlanetMath 随机采样概念-解释对，确保数据独立性
- 9 种预定义策略作为软约束
- RL 联合优化结构有效性、推理复杂度和答案一致性
- 在 GSM8K、MATH-500、AIME2024/2025、OlympiadBench 上持续优于基线

#### Time-Frequency Token Advantage Clipping for Efficient Large Reasoning Model

| 项目 | 内容 |
|------|------|
| **标题** | Time-Frequency Token Advantage Clipping for Training Efficient Large Reasoning Model |
| **Venue** | AAAI 2026 |

**核心贡献：**
- 将时频分析与 Token 优势裁剪结合
- 提升推理模型训练效率

### 4.2 AAAI 2026 其他值得关注的论文

| 论文 | 方向 |
|------|------|
| LogicCat: Chain-of-Thought Text-to-SQL Benchmark | Text-to-SQL / 推理 |
| TIV: Thought Injection via Vectors for Efficient Reasoning | 推理效率 |
| Identifying and Analyzing Performance-Critical Tokens in LLMs | LLM 分析 |
| Safe-Semantics-but-Unsafe-Interpretation (SSUI) | 多模态安全 |
| Language Models and Logic Programs for Trustworthy Tax Reasoning | 神经符号推理 |

---

## 5. NeurIPS 2025

### 5.1 Large Language Diffusion Models (LLaDA)

| 项目 | 内容 |
|------|------|
| **标题** | Large Language Diffusion Models |
| **作者** | — |
| **Venue** | NeurIPS 2025 |
| **链接** | https://openreview.net/pdf?id=KnqiC0znVF |

**核心贡献：**
- 挑战 "LLM 能力必须依赖自回归模型" 的普遍认知
- LLaDA: 从头训练的扩散模型，使用掩码扩散 (MDM)
- 前向数据掩码过程 + 反向生成过程，参数化为 Transformer 预测掩码 token
- 优化似然下界的变分方法
- LLaDA 8B 与 LLaMA3 8B 在 in-context learning 上可比
- 解决反转诅咒（reversal curse），在反转诗歌补全任务上超越 GPT-4o
- 预训练 2.3T tokens

### 5.2 Artificial Hivemind (Best Paper DB Track)

| 项目 | 内容 |
|------|------|
| **标题** | Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond) |
| **作者** | Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Yejin Choi |
| **Venue** | NeurIPS 2025 **Best Paper (DB Track)** |
| **链接** | https://neurips.cc/virtual/2025/poster/121421 |

**核心贡献：**
- 引入 Infinity-Chat：26K 多样化开放型用户查询数据集
- 首个全面分类法：6 个顶级类别、17 个子类别
- 31,250 个人类标注（每个样本 25 个独立标注）
- 揭示 Artificial Hivemind 效应：(1) 模型内重复，(2) 模型间同质化
- SOTA LLM、奖励模型和 LM Judge 对人类评分校准不足

### 5.3 Topology of Reasoning: Understanding Large Reasoning Models

| 项目 | 内容 |
|------|------|
| **标题** | Topology of Reasoning: Understanding Large Reasoning Models through Reasoning Graph Properties |
| **作者** | — |
| **Venue** | NeurIPS 2025 |

**核心贡献：**
- 利用 Qwen2.5 系列 (从 DeepSeek-R1 蒸馏) 1.5B-32B 分析推理图
- 关键发现：大型推理模型持续表现出 (1) 更高的循环性, (2) 更广的探索行为, (3) 明显的小世界特性
- 这些图结构特征与推理性能改善直接相关

### 5.4 STACKTRANS: Recursive Transformer with State Stack

| 项目 | 内容 |
|------|------|
| **标题** | Recursive Transformer: Boosting Reasoning Ability with State Stack |
| **作者** | — |
| **Venue** | NeurIPS 2025 |

**核心贡献：**
- 受下推自动机启发，引入可微隐藏状态栈到 Transformer
- STACKTRANS 可有效学习乔姆斯基层级语法
- 增强模型表示层级依赖和递归语法的能力

### 5.5 NeurIPS 2025 Other Highlights

| 论文 | 方向 |
|------|------|
| Causal Discovery and Inference through Next-Token Prediction | 因果推理 + LLM |
| Dynam3D: Dynamic Layered 3D Tokens for VLM Navigation | VLM + 导航 |
| Understanding Numerical Sources of Nondeterminism in LLM Inference | LLM 推理不确定性 |
| Representation Entanglement for Generation: Training DiT Is Much Easier | 扩散 Transformer |
| SAVVY: Spatial Awareness via Audio-Visual LLMs | 多模态空间感知 |
| From Condensation to Rank Collapse: Two-Stage Transformer Training Dynamics | Transformer 理论 |

---

## 6. CVPR 2026

### 6.1 VisPlay: Self-Evolving Vision-Language Models

| 项目 | 内容 |
|------|------|
| **标题** | VisPlay: Self-Evolving Vision-Language Models |
| **作者** | Yicheng He, Chengsong Huang, Zongxia Li, Jiaxin Huang, Yonghui Yang |
| **Venue** | CVPR 2026 |
| **链接** | https://openaccess.thecvf.com/content/CVPR2026/html/He_VisPlay_Self-Evolving_Vision-Language_Models_CVPR_2026_paper.html |

**核心贡献：**
- 自进化 RL 框架：单 VLM 扮演两个交互角色（Image-Conditioned Questioner + Multimodal Reasoner）
- 使用 GRPO 联合训练，引入多样性/难度奖励平衡问题难度和答案质量
- 在 Qwen2.5-VL 和 MiMo-VL 上跨 8 个基准（包括 MM-Vet, MMMU）持续改进
- 无需人工标注或任务特定启发式

### 6.2 Grounded Chain-of-Thought for MLLMs

| 项目 | 内容 |
|------|------|
| **标题** | Grounded Chain-of-Thought for Multimodal Large Language Models |
| **作者** | Qiong Wu, Xiangcong Yang, Yiyi Zhou, Chenxin Fang, Baiyang Song, Xiaoshuai Sun, Rongrong Ji |
| **Venue** | CVPR 2026 |
| **链接** | https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Grounded_Chain-of-Thought_for_Multimodal_Large_Language_Models_CVPR_2026_paper.html |

**核心贡献：**
- 提出 Grounded Chain-of-Thought (GCoT) 任务
- 构建 MM-GCoT 基准和一致性评估体系（答案准确率、接地准确率、答案-接地一致性）
- 12 个先进 MLLM 的评估揭示：(1) 多数 MLLM 在一致性评估上表现不佳；(2) 视觉幻觉与参数规模和通用多模态性能不直接相关

### 6.3 Predictive Regularization Against Visual Representation Degradation

| 项目 | 内容 |
|------|------|
| **标题** | Predictive Regularization Against Visual Representation Degradation in Multimodal Large Language Models |
| **作者** | Enguang Wang, Qiang Wang, Yuanchen Wu, Ke Yan, Xinbin Yuan, Shouhong Ding, Xialei Liu, Ming-Ming Cheng |
| **Venue** | CVPR 2026 |
| **链接** | https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Predictive_Regularization_Against_Visual_Representation_Degradation_in_Multimodal_Large_Language_CVPR_2026_paper.html |

**核心贡献：**
- 诊断发现 MLLM 中存在普遍视觉表征退化问题
- LLM 中间层视觉表征在全局功能和 patch 结构上都出现退化
- 归因于单一文本生成目标导致的视觉牺牲
- 提出 Predictive Regularization (PRe)：强制退化的中间特征预测初始视觉特征

### 6.4 GR3D: Grounded 3D-Aware Spatial VLM

| 项目 | 内容 |
|------|------|
| **标题** | Grounded 3D-Aware Spatial Vision-Language Modeling |
| **作者** | An-Chieh Cheng, Yang Fu, Yatai Ji, Ligeng Zhu, Guanqi Zhan, Zhuoyang Zhang, Zhaojing Yang, Song Han, Yao Lu, Pavlo Molchanov, Vidya Nariyambut Murali, Jan Kautz, Xiaolong Wang, Hongxu Yin, Sifei Liu (NVIDIA) |
| **Venue** | CVPR 2026 |
| **链接** | https://openaccess.thecvf.com/content/CVPR2026/html/Cheng_Grounded_3D-Aware_Spatial_Vision-Language_Modeling_CVPR_2026_paper.html |

**核心贡献：**
- 单一框架内实现三种互补接地能力：显式 2D 接地、隐式 2D 接地、单目 3D 接地
- 隐式接地机制在生成时识别实体提及并插入区域 token
- 区域提示的单目 3D 接地设计预测相机视角下的 3D 边界框
- 在有无接地任务上均取得一致改进

### 6.5 Scaling Long Video Understanding via Visual Memory

| 项目 | 内容 |
|------|------|
| **标题** | Scaling the Long Video Understanding of Multimodal Large Language Models via Visual Memory Mechanism |
| **作者** | Tao Chen, Kun Zhang, Qiong Wu, Xiao Chen, Chao Chang, Xiaoshuai Sun, Yiyi Zhou, Rongrong Ji |
| **Venue** | CVPR 2026 |
| **链接** | https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Scaling_the_Long_Video_Understanding_of_Multimodal_Large_Language_Models_CVPR_2026_paper.html |

**核心贡献：**
- 提出 FlexMem：训练自由方法，模拟人类观看视频行为
- 视觉 KV cache 作为记忆源，通过双路径压缩实现有效记忆转移和写入
- 探索不同视频理解任务的记忆读取策略
- 单张 3090 GPU 可处理 >1000 帧，性能与 GPT-4o、Gemini-1.5 Pro 可比

---

## 7. ACL 2026 / EMNLP 2025

### 7.1 ACL 2026 概览

ACL 2026 收录 1364 篇论文，主要方向分布：

| 方向 | 论文数 |
|------|--------|
| LLM Safety | 115 |
| Multimodal VLM | 94 |
| LLM Evaluation | 92 |
| LLM Reasoning | 81 |
| LLM Agent | 78 |
| Information Retrieval & RAG | 73 |
| Audio & Speech | 68 |
| Multilingual & Translation | 62 |

### 7.2 EMNLP 2025 Highlights

#### MathTutorBench: Measuring Pedagogical Capabilities of LLM Tutors

| 项目 | 内容 |
|------|------|
| **标题** | MathTutorBench: A Benchmark for Measuring Open-ended Pedagogical Capabilities of LLM Tutors |
| **作者** | Jakub Macina, Nico Daheim, Ido Hakimi, Manu Kapur, Iryna Gurevych, Mrinmaya Sachan |
| **Venue** | EMNLP 2025 |

**核心贡献：**
- 首个系统评估 LLM 在开放式教学场景中能力的基准

#### From Problem-Solving to Teaching Problem-Solving via RL

| 项目 | 内容 |
|------|------|
| **标题** | From Problem-Solving to Teaching Problem-Solving: Aligning LLMs with Pedagogy using Reinforcement Learning |
| **作者** | David Dinucu-Jianu, Jakub Macina, Nico Daheim, Ido Hakimi, Iryna Gurevych, Mrinmaya Sachan |
| **Venue** | EMNLP 2025 |

**核心贡献：**
- 用 RL 对齐 LLM 教学行为，从解题到教学能力迁移

#### SensorLLM: Aligning LLMs with Motion Sensors

| 项目 | 内容 |
|------|------|
| **标题** | SensorLLM: Aligning Large Language Models with Motion Sensors for Human Activity Recognition |
| **作者** | Zechen Li, Shohreh (等) |
| **Venue** | EMNLP 2025 |

**核心贡献：**
- 将 LLM 与运动传感器信号对齐，用于人类活动识别

---

## 8. KDD 2026

### 8.1 Field-Aware Transformer for CTR Prediction

| 项目 | 内容 |
|------|------|
| **标题** | From Scaling to Structured Expressivity: Rethinking Transformers for CTR Prediction |
| **作者** | — |
| **Venue** | KDD 2026 |
| **arXiv** | 2511.12081 |

**核心贡献：**
- 诊断 CTR 预测中 Transformer 的结构错位：标准 Transformer 假设序列组合性，CTR 数据需要字段异构组合推理
- 提出 Field-Aware Transformer (FAT)：用字段中心参数重构标准 Transformer block
- Basis-Composed Hypernetwork 合成字段特定参数，解耦模型容量与字段基数
- Rademacher complexity 理论支撑的形式化缩放律
- AUC 提升最高 +4.38%，在线 CTR +2.33%, RPM +0.66%

### 8.2 Scaling Recommender Transformers to One Billion Parameters

| 项目 | 内容 |
|------|------|
| **标题** | Scaling Recommender Transformers to One Billion Parameters |
| **作者** | — |
| **Venue** | KDD 2026 |
| **arXiv** | 2507.15994 |

**核心贡献：**
- 首个 1B 参数推荐 Transformer 的系统性缩放研究
- 分析现有 GR (HSTU) 框架在参数大于 176M 时的扩展性
- 提出专门为大规模推荐设计的 Transformer 架构改进

### 8.3 FCN: Fusing Cross Network for CTR

| 项目 | 内容 |
|------|------|
| **标题** | FCN: Fusing Exponential and Linear Cross Network for Click-Through Rate Prediction |
| **作者** | Honghao Li, Yiwen Zhang, Yi Zhang, Hanwei Li, Lei Sang, Jieming Zhu |
| **Venue** | KDD 2026 |
| **arXiv** | 2407.13349 |

**核心贡献：**
- 提出 Linear Cross Network (LCN) 和 Exponential Cross Network (ECN)
- 两种融合架构 FCN-p 和 FCN-sp 适应不同数据分布
- 同时显式捕获低阶和高阶特征交互

### 8.4 DeGRe: Dense-supervised Generative Reranking

| 项目 | 内容 |
|------|------|
| **标题** | DeGRe: Dense-supervised Generative Reranking for Recommendation |
| **作者** | — |
| **Venue** | KDD 2026 |
| **arXiv** | 2605.25749 |

**核心贡献：**
- 生成式重排序，解决传统重排序中的偏差和奖励稀疏问题
- 在线 A/B 测试：CTR +2.85%, ORDER +2.14%, GMV +3.75%
- 推理延迟仅增加 14.8ms

### 8.5 Beyond Interleaving: Causal Attention for Generative Recommender

| 项目 | 内容 |
|------|------|
| **标题** | Beyond Interleaving: Causal Attention Reformulations for Generative Recommender Systems |
| **作者** | — |
| **Venue** | KDD 2026 |
| **arXiv** | 2603.10369 |

**核心贡献：**
- 提出直接编码 item-action 因果关系无需交错处理的注意力变体
- 三种变体：Late Fusion、Mixed-Value Early Fusion、Attentional Gating
- 降低注意力噪声，提升表征学习效率

### 8.6 Macro Graph of Experts for Billion-Scale Multi-Task Recommendation

| 项目 | 内容 |
|------|------|
| **标题** | Macro Graph of Experts for Billion-Scale Multi-Task Recommendation |
| **作者** | Qihua Feng, Huan Gong, Feiran Huang |
| **Venue** | KDD 2026 |

**核心贡献：**
- 首个面向十亿级多任务推荐的图神经网络架构
- 提出 Macro Task Merging Graph (MTMG)
- Macro Prediction Tower 聚合多层级信息同时预测多个任务

### 8.7 CURec: Collaborative Content Understanding for Recommendation

| 项目 | 内容 |
|------|------|
| **标题** | Towards Comprehensible Recommendation with Large Language Model Fine-tuning |
| **作者** | — |
| **Venue** | KDD 2026 |
| **arXiv** | 2508.07595 |

**核心贡献：**
- 通过 LLM 生成可理解的推荐理由，弥合语义-协同鸿沟
- 设计基于传统推荐架构的奖励模型评估推荐理由质量
- 使用奖励信号通过 RL 优化 LLM

---

## 9. SIGIR 2026

### 9.1 InvariRank: Position-Invariant Listwise Reranking

| 项目 | 内容 |
|------|------|
| **标题** | One Pass, Any Order: Position-Invariant Listwise Reranking for LLM-Based Recommendation |
| **作者** | — |
| **Venue** | SIGIR 2026 |
| **arXiv** | 2604.27599 |

**核心贡献：**
- 解决 LLM 重排序中的位置偏差问题
- 通过结构化分段掩码和共享位置框架实现顺序不变性
- 无需排列集成或辅助不变性损失
- 在 MovieLens-32M 和 Amazon Books 上使用 Mistral 7B 和 LLaMA 3.2 3B 验证
- 达到近乎完美的排列鲁棒性（Kendall's τ, Spearman's ρ）

### 9.2 ProMax: LLM-Derived Profiles for Recommender Systems

| 项目 | 内容 |
|------|------|
| **标题** | ProMax: Exploring the Potential of LLM-derived Profiles with Distribution Shaping for Recommender Systems |
| **作者** | — |
| **Venue** | SIGIR 2026 |
| **arXiv** | 2604.26231 |

**核心贡献：**
- 重新审视 LLM 生成的 user/item profiles 用于推荐
- 双重分布重塑过程：profile distribution 作为引导信号
- 整合到 LightGCN 后在 Amazon-Book (+8.44%), Yelp (+4.71%), Steam (+3.31%) 上提升 NDCG@10

### 9.3 GenRec: Preference-Oriented Generative Framework

| 项目 | 内容 |
|------|------|
| **标题** | GenRec: A Preference-Oriented Generative Framework for Large-Scale Recommendation |
| **作者** | — |
| **Venue** | SIGIR 2026 |
| **arXiv** | 2604.14878 |

**核心贡献：**
- 解决生成式推荐的三项挑战：分页请求多正反馈、长历史序列计算开销、reward hacking
- 提出 GRPO-SR (Group Relative Policy Optimization with Supervised Regularization)
- 纯解码器架构中统一用户意图理解和物品检索

### 9.4 R3-REC: Reasoning-Driven Recommendation via Retrieval-Augmented LLMs

| 项目 | 内容 |
|------|------|
| **标题** | R3-REC: Reasoning-Driven Recommendation via Retrieval-Augmented LLMs over Multi-Granular Interest Signals |
| **作者** | — |
| **Venue** | SIGIR 2026 |
| **arXiv** | 2603.13730 |

**核心贡献：**
- 多层级兴趣信号上的检索增强推理：多级用户意图推理、物品语义提取、长短兴趣极性挖掘、相似用户协同增强
- ML-1M 上 HR@1 提升 +6.3%, Games 上 +9.9%, Bundle 上 +10.2%

### 9.5 Reasoning over Semantic IDs Enhances Generative Recommendation

| 项目 | 内容 |
|------|------|
| **标题** | Reasoning over Semantic IDs Enhances Generative Recommendation |
| **作者** | — |
| **Venue** | SIGIR 2026 |
| **arXiv** | 2603.23183 |

**核心贡献：**
- 将 RL 推理应用于语义 ID 上的序列生成推荐
- 超越传统序列推荐和现有生成推荐方法

---

## 10. WWW 2026

### 10.1 Search & Retrieval-Augmented AI 方向

| 论文 | 方向 |
|------|------|
| LongRanker: Efficient One-Pass Document Reranking with Long-Context LLMs | 长文本重排序 |
| OpenDecoder: LLM Decoding to Incorporate Document Quality in RAG | RAG 文档质量 |
| LiveNewsBench: Evaluating LLM Web Search with Freshly Curated News | Agentic 搜索评估 |
| Aligning LLMs with Searcher Preferences (Kuaishou) | 搜索偏好对齐 |
| Retrieval Collapses When AI Pollutes the Web | AI 内容污染检索 |
| What Should I Cite? CiteRAG Benchmark | 引文预测 RAG |
| Rethinking Soft Compression in RAG: Query-Conditioned Selector | RAG 软压缩 |

### 10.2 Aligning LLMs with Searcher Preferences (Kuaishou)

| 项目 | 内容 |
|------|------|
| **标题** | Aligning Large Language Models with Searcher Preferences |
| **作者** | Kuaishou |
| **Venue** | WWW 2026 |
| **arXiv** | 2603.10473 |

**核心贡献：**
- 提出 SearchLLM：专为开放域生成式搜索设计的 LLM
- 多维度奖励模型（事实依据、答案质量、格式合规）+ 行为优化（鲁棒性、用户需求对齐）
- 规则检查 + 人工校准 LLM Judge 生成可解释分数
- 在线 A/B 测试：Valid Consumption Rate +1.03%, Re-search Rate -0.81%

### 10.3 Retrieval Collapses When AI Pollutes the Web

| 项目 | 内容 |
|------|------|
| **标题** | Retrieval Collapses When AI Pollutes the Web |
| **作者** | — |
| **Venue** | WWW 2026 |
| **arXiv** | 2602.16136 |

**核心贡献：**
- 系统研究 AI 生成内容对检索生态的结构性风险
- MS MARCO 仿真实验：SEO 场景下 67% 池污染率导致 >80% 暴露污染率
- 对抗场景下 BM25 等基线严重脆弱（~19% 有害内容暴露）
- LLM ranker 在对抗场景下更具韧性

---

## 11. CIKM 2025 / RecSys 2025

### 11.1 CIKM 2025

#### STARec: Agent Framework for Recommender Systems

| 项目 | 内容 |
|------|------|
| **标题** | STARec: An Efficient Agent Framework for Recommender Systems via Autonomous Deliberate Reasoning |
| **作者** | — |
| **Venue** | CIKM 2025 |
| **arXiv** | 2508.18812 |

**核心贡献：**
- 将自主深思推理范式引入推荐 Agent

#### Climber: Efficient Scaling Laws for Large Recommendation Models

| 项目 | 内容 |
|------|------|
| **标题** | Climber: Toward Efficient Scaling Laws for Large Recommendation Models |
| **作者** | Songpei Xu, Shijia Wang, Da Guo, Xianwen Guo, Qiang Xiao, Bin Huang, Guanlin Wu, Chuanjiang Luo |
| **Venue** | CIKM 2025 |
| **arXiv** | 2502.09888 |

**核心贡献：**
- 面向大规模推荐模型的高效缩放律框架
- 在推荐场景中提出更实用的 scaling law 设计

### 11.2 RecSys 2025

#### GRACE: Journey-Aware Generative Recommendation (Walmart)

| 项目 | 内容 |
|------|------|
| **标题** | GRACE: Generative Recommendation with CoT Tokenization + Sparse Attention |
| **作者** | Walmart |
| **Venue** | RecSys 2025 |

**核心贡献：**
- 多行为生成式推荐：混合 tokenization（RQ-VAE 语义 ID + CoT 属性 token）
- Journey-Aware Sparse Attention：四个注意力范围（压缩长历史摘要、旅程内、旅程间、当前会话）
- Switch-Transformer backbone
- 激活参数减少 32-48%（seq len 50-2000）

#### Enhancing Sequential Recommender with LLM (Kuaishou)

| 项目 | 内容 |
|------|------|
| **标题** | Enhancing Sequential Recommender with Large Language Models for Joint Video and Comment Recommendation |
| **作者** | Bowen Zheng, Zihan Lin, Enze Liu, Chen Yang, Enyang Bai, Cheng Ling, Han Li, Wayne Xin Zhao, Ji-Rong Wen (Kuaishou / 中国人民大学) |
| **Venue** | RecSys 2025 |

**核心贡献：**
- 联合视频和评论推荐的 LLM 增强序列推荐

---

## 12. Agents & Code Execution

### 12.1 Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks

| 项目 | 内容 |
|------|------|
| **标题** | Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks via Code Execution with State-Diff-Based Evaluation |
| **作者** | — |
| **Venue** | — (arXiv 2026) |
| **arXiv** | 2602.11224 |

**核心贡献：**
- 提出 state-diff contract：将执行过程与结果分离
- 新颖沙箱提供标准化脚本层，所有模型通过统一代码执行沙箱调用外部 API (Slack, Box, Linear, Google Calendar)
- 9 个 LLM、224 个任务的企业软件工作流评估

### 12.2 FOREAGENT: Predict-Then-Verify for ML Agents

| 项目 | 内容 |
|------|------|
| **标题** | Can We Predict Before Executing Machine Learning Agents? |
| **作者** | — |
| **Venue** | — (arXiv 2026) |
| **arXiv** | 2601.05930 |

**核心贡献：**
- 验证 LLM 在提供 Verified Data Analysis Report 后具有显著预测能力（61.5% 准确率）
- FOREAGENT: Predict-then-Verify 循环，将探索与执行解耦
- 搜索空间扩展 3.2x，6x 加速收敛，性能 +6%

### 12.3 Self-Execution Simulation Improves Coding Models

| 项目 | 内容 |
|------|------|
| **标题** | Self-Execution Simulation Improves Coding Models |
| **作者** | — |
| **Venue** | — (arXiv 2026) |
| **arXiv** | 2604.03253 |

**核心贡献：**
- 在代码 LLM 上使用 SFT + RL 训练执行模拟能力
- 两个互补目标：(1) 给定代码和输入的输出预测，(2) 带真实/自我预测执行反馈的编程求解
- self-RLEF 框架持续优于官方 CWM 和 CWM-RL

### 12.4 Agentic Predictor: Multi-View Workflow Encoding

| 项目 | 内容 |
|------|------|
| **标题** | Multi-View Encoders for Performance Prediction in LLM-Based Agentic Workflows |
| **作者** | — |
| **Venue** | ICLR 2026 Workshop on Agents in the Wild |

**核心贡献：**
- 多视角工作流编码：代码架构、文本 prompt、交互图特征
- 跨领域无监督预训练
- 显著减少评估所需的工作流运行次数

---

## 13. 生成模型与序列建模

### 13.1 Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention

| 项目 | 内容 |
|------|------|
| **标题** | Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention |
| **作者** | — |
| **日期** | 2026-05-21 |
| **arXiv** | 2605.22791 |

**核心贡献：**
- Gated DeltaNet 的第二代，在线性注意力中解耦擦除和写入操作
- 与 Mamba-3 等共同推动状态空间/线性注意力模型的发展

### 13.2 Nemotron 3 Super: Open Hybrid Mamba-Transformer

| 项目 | 内容 |
|------|------|
| **标题** | Nemotron 3 Super: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning |
| **作者** | NVIDIA |
| **日期** | 2026-04-13 |
| **arXiv** | 2604.12374 |

**核心贡献：**
- 混合 Mamba-Transformer MoE 架构
- 开源模型，优化 Agentic 推理场景
- 代表了 MoE + State Space + Transformer 融合的前沿方向

### 13.3 MiniMax-M2: Mini Activations, Max Intelligence

| 项目 | 内容 |
|------|------|
| **标题** | The MiniMax-M2 Series: Mini Activations Unleashing Max Real-World Intelligence |
| **作者** | MiniMax AI |
| **日期** | 2026-05-25 |
| **arXiv** | 2605.26494 |

**核心贡献：**
- 激活参数极小化但保留最大智能的新型架构
- 230B 模型在 BrowseComp 等基准上表现突出

---

## 总结与趋势

### 2026年H1 关键趋势

1. **Frontier Model 三分天下**：OpenAI（Agent + 通用）、Anthropic（编码 + 安全）、DeepSeek（开源 + 性价比）各占一极，互有胜负

2. **Agent 系统爆发**：ICML 2026 收录约 465 篇 Agent 论文，Tool-use RL 成为核心范式，从 prompt-based 到可训练 Agent 是大势所趋

3. **生成式推荐成熟**：生成式范式（HSTU, GenRec, GRACE）在推荐系统中加速普及，RL 对齐（GRPO-SR）解决偏好优化问题

4. **扩散模型挑战自回归**：LLaDA (NeurIPS 2025 Best) 证明非自回归方法在语言建模上可行；ICML 2026 进一步探讨 dLLM 的灵活性与推理质量

5. **推理时计算深化**：∇-Reasoner（ICLR 2026）、GFPO（ICLR 2026）等推动从离散搜索到连续优化的推理范式转变

6. **多模态空间理解**：CVPR 2026 突出 MLLM 的空间感知、3D 接地、长视频理解能力

7. **推荐系统结构化缩放**：FAT (KDD 2026)、HSTU 等突破从参数缩放转向结构化表达性

8. **RL 驱动推理**：从 DeepSeek-R1 到多个会议的 RL for Reasoning 论文激增，组成性泛化理论形成
