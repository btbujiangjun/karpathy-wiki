---
title: 顶会论文专题报告 — 2026年5月全面版（ICML / AAAI / NeurIPS / ICLR / KDD / CVPR / ACL / EMNLP / SIGIR / WWW / CIKM / RecSys）
type: synthesis
created: 2026-05-29
updated: 2026-05-29
sources: [arXiv, ICML 2026, ICLR 2026, NeurIPS 2025, WWW 2026, KDD 2026, SIGIR 2026, RecSys 2025]
tags: [conference-digest, icml-2026, iclr-2026, neurips-2025, www-2026, kdd-2026, sigir-2026, recsys-2025, ctr, recommendation, agent, llm, alignment, game-rl, code-generation, multi-agent]
---

# 顶会论文专题报告 — 2026年5月全面版

> 覆盖 ICML 2026、AAAI 2026、NeurIPS 2025、ICLR 2026、KDD 2026、CVPR 2026、ACL/EMNLP 2025、SIGIR 2026、WWW 2026、CIKM 2025、RecSys 2025 等 11+ 会议的最新接收论文与 arXiv 前沿工作。聚焦 LLM 训练理论、推荐系统/CTR 预测、智能体系统、对齐与安全、游戏与多智能体 RL、代码生成、多模态与生成模型。

---

## 目录

1. [ICML 2026 收录论文](#1-icml-2026-收录论文)
2. [ICLR 2026 收录论文](#2-iclr-2026-收录论文)
3. [NeurIPS 2025 收录论文](#3-neurips-2025-收录论文)
4. [WWW 2026 / SIGIR 2026 / CIKM 2025 推荐系统论文](#4-www-2026--sigir-2026--cikm-2025-推荐系统论文)
5. [CTR 预测与工业推荐系统（arXiv 2025-2026）](#5-ctr-预测与工业推荐系统arxiv-2025-2026)
6. [智能体系统与工具增强推理](#6-智能体系统与工具增强推理)
7. [多智能体系统与游戏 AI](#7-多智能体系统与游戏-ai)
8. [LLM 对齐、安全与后训练](#8-llm-对齐安全与后训练)
9. [代码生成与执行预测](#9-代码生成与执行预测)
10. [Google DeepMind 系统与模型](#10-google-deepmind-系统与模型)
11. [扩散模型与生成式 AI](#11-扩散模型与生成式-ai)

---

## 1. ICML 2026 收录论文

### 1.1 Bi-NAC: Bilevel Natural Language Actor-Critic

| 属性 | 内容 |
|------|------|
| **标题** | RL with Learnable Textual Feedback: A Bilevel Approach |
| **中文标题** | 可学习文本反馈的强化学习：双层优化方法 |
| **作者** | Amrit Bedi 等 (UCF) |
| **机构** | University of Central Florida |
| **Venue** | ICML 2026, Seoul |
| **arXiv** | [2605.24547](https://arxiv.org/abs/2605.24547) |

**问题背景**：RL with verifiable rewards (RLVR) 可以提升 LLM 推理能力，但当终端奖励稀疏时，样本效率极低。现有方法引入文本反馈（critic 生成自然语言反馈来指导 actor），但将反馈视为固定或辅助信号，忽略了反馈本身应根据策略的学习需求进行调整这一关键属性。

**方法详述**：Bi-NAC 将 actor-critic 的交互形式化为 Stackelberg 双层规划（bilevel program）。外层优化 critic 生成能最大化 actor 奖励改进的反馈；内层优化 actor 利用 critic 反馈改进策略。训练过程联合优化两个模型，critic 生成的反馈在上下文中提供给 actor。

**创新点**：
1. 首次将 RL 文本反馈形式化为双层优化问题
2. 提出联合训练范式，critic 的反馈目标直接与 actor 的性能改进对齐
3. 在 MATH-500、MBPP、GPQA 上验证，2B 模型超越 3B GRPO 基线

**实验结果**：

| 模型 | MATH-500 | MBPP | GPQA |
|------|----------|------|------|
| GRPO-3B | 41.4% | - | - |
| Bi-NAC-2B | 46.6% | +5.18 | +4.77 |
| GRPO-7B | - | - | 43.6% |
| Bi-NAC-6B | 49.3% | +2.8 | +5.7 |

---

### 1.2 R2-Write: Reflection and Revision for Open-Ended Writing

| 属性 | 内容 |
|------|------|
| **标题** | R2-Write: Reflection and Revision for Open-Ended Writing with Deep Reasoning |
| **中文标题** | R2-Write: 深度推理中的反思与修订用于开放式写作 |
| **Venue** | ICML 2026 |
| **arXiv** | [2604.03004](https://arxiv.org/abs/2604.03004) |

**问题背景**：深度推理模型（如 o1、R1）在数学等可验证领域表现优异，但在开放式写作等无标准答案的任务上增益有限。

**方法详述**：提出自动化数据构建框架，合成富含反思和修订模式的高质量思维轨迹。引入 process reward mechanism 显式监督反思和修订质量，在 RL 阶段减少冗余反思。

**创新点**：发现现有推理模型在写作中严重低估反思和修订模式的使用；提出的 writer-judge collaboration 框架通过 SFT（3K 数据）和 RL（5K 数据）两阶段训练，在多个写作和深度研究基准上取得显著改进。RL 阶段引入的 process reward 在保持性能的同时减少了 20% 的 token 长度。

---

### 1.3 Vector Prompt Interfaces (Position Paper)

| 属性 | 内容 |
|------|------|
| **标题** | Vector Prompt Interfaces Should Be Exposed to Enable Customization |
| **中文标题** | 向量提示接口应作为公共接口开放以实现定制化 |
| **Venue** | ICML 2026 |
| **arXiv** | [2603.04292](https://arxiv.org/abs/2603.04292) |

**核心论点**：模型提供商应将向量提示（vector prompt）输入作为 LLM 定制化的公共接口。实验证据表明向量提示调优随监督信号增加持续改进，而文本提示优化早期即饱和。向量提示展现出密集的全局注意力模式，且暴露向量提示在标准黑盒威胁模型下不会根本增加模型泄露风险。

---

### 1.4 BigMac: Multimodal LLM Training Pipeline

| 属性 | 内容 |
|------|------|
| **标题** | BigMac: Breaking the Pareto Frontier of Compute and Memory in Multimodal LLM Training |
| **中文标题** | BigMac: 突破多模态 LLM 训练中计算与内存的帕累托前沿 |
| **Venue** | ICML 2026 |
| **arXiv** | [2605.25451](https://arxiv.org/abs/2605.25451) |

**创新点**：提出嵌套流水线（nested pipeline），将编码器和生成器计算优雅地嵌入原始 LLM 流水线中。编码器和生成器的激活内存复杂度降至 O(1)，同时 LLM 激活保持不变。在 MLLM 理解和生成任务上实现 1.08×–1.9× 训练加速，且内存使用随 batch size 增加保持稳定。

---

### 1.5 Understanding Challenges in Iterative Generative Optimization

| 属性 | 内容 |
|------|------|
| **标题** | Understanding the Challenges in Iterative Generative Optimization with LLMs |
| **中文标题** | 理解 LLM 迭代生成优化的挑战 |
| **Venue** | ICML 2026 |
| **arXiv** | [2603.23994](https://arxiv.org/abs/2603.23994) |

**核心发现**：尽管 LLM 优化器活跃发展，仅 9% 的被调查智能体使用了任何自动化优化。问题在于工程师必须做出"隐藏"的设计选择：起始工件、信用分配范围、批处理策略。通过 MLAgentBench、Atari、BigBench Extra Hard 三个案例，发现这些设计决策决定优化成败。

---

### 1.6 Self-Flow Matching (Self-Supervised Flow Matching)

| 属性 | 内容 |
|------|------|
| **标题** | Self-Supervised Flow Matching (Self-Flow) |
| **中文标题** | 自监督流匹配 |
| **Venue** | ICML 2026 |
| **备注** | 之前已记录在 wiki |

---

### 1.7 Shannon Scaling Law

| 属性 | 内容 |
|------|------|
| **标题** | Shannon Scaling Law: LLMs as Noisy Channels |
| **中文标题** | 香农缩放律：LLM 作为噪声信道 |
| **Venue** | ICML 2026 |
| **arXiv** | 2605.23901 |
| **备注** | 之前已记录 |

---

## 2. ICLR 2026 收录论文

### 2.1 GSPR: Generalizable Safety Policy Reasoner

| 属性 | 内容 |
|------|------|
| **标题** | GSPR: Aligning LLM Safeguards as Generalizable Safety Policy Reasoners |
| **中文标题** | GSPR: 将 LLM 安全防护对齐为可泛化的安全策略推理器 |
| **Venue** | ICLR 2026 |
| **OpenReview** | [H2e5TerulJ](https://openreview.net/pdf?id=H2e5TerulJ) |

**创新点**：利用 GRPO 在多个具有不同安全策略分类体系的安全基准上联合训练，使模型具备跨安全策略库的泛化推理能力。相比传统安全防护（仅二分类 safe/unsafe），GSPR 在细粒度安全类别预测上提升超 45%，同时推理 token 成本最低。

---

### 2.2 NSPO: Null-Space Constrained Policy Optimization

| 属性 | 内容 |
|------|------|
| **标题** | Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization |
| **中文标题** | 用零空间约束策略优化缓解安全对齐税 |
| **Venue** | ICLR 2026 (Poster) |

**方法**：将安全策略梯度几何投影到通用任务的零空间中，从而在保持核心能力的同时实现安全对齐。理论证明 NSPO 保留模型原始能力，同时保证安全对齐的下降方向。仅需 40% 的 PKU-SafeRLHF 公开数据即可达到 SOTA 安全性能，且无需大量混合通用任务数据。

---

### 2.3 DAR: Dual-regularized Advantage Regression

| 属性 | 内容 |
|------|------|
| **标题** | Reference Regularization in RLHF |
| **中文标题** | RLHF 中的参考正则化 |
| **Venue** | ICLR 2026 |
| **arXiv** | [2602.11523](https://arxiv.org/abs/2602.11523) |

**方法**：提出统一正则化方法，显式平衡防止奖励黑客和保持稳定策略更新的目标。将 RL 对齐目标重新形式化为加权 SFT 损失，既提升稳定性又降低实现复杂度。DAR 在多个基准上持续优于 RLHF 和在线偏好学习方法。

---

### 2.4 ReAlign: Safety-Aligning Reasoning Models with RL

| 属性 | 内容 |
|------|------|
| **标题** | ReAlign: Safety-Aligning Reasoning Models with Verifier-Guided Reinforcement Learning |
| **中文标题** | ReAlign: 用验证器引导的强化学习对推理模型进行安全对齐 |
| **Venue** | ICLR 2026 |
| **OpenReview** | [XxYNlbTFYS](https://openreview.net/pdf?id=XxYNlbTFYS) |

**创新点**：结合安全验证器（guard model）、通用奖励模型和新颖的拒绝惩罚的混合奖励系统。在 Qwen3-4B 上，thinking 模式 WildGuard 安全率达 97.4%，同时保持推理能力和低拒绝率。揭示安全 CoT 与最终答案之间存在部分解耦关系。

---

### 2.5 LoRA as Safety Patches: Decoupling Safety into Orthogonal Subspace

| 属性 | 内容 |
|------|------|
| **标题** | Decoupling Safety into Orthogonal Subspace: Cost-Efficient and Performance-Preserving Alignment for LLMs |
| **中文标题** | 将安全解耦到正交子空间：LLM 的成本高效、性能保持对齐 |
| **Venue** | ICLR 2026 |

**核心发现**：LoRA-based Refusal-training 仅使用安全数据训练就能实现性能保持的安全对齐。理论和实验证明 LoRA 将安全解耦到与模型内禀变换空间高度正交的低秩子空间，安全与通用能力之间的相似度 <0.1（全量微调 >0.4）。可作为即插即用的安全补丁。

---

### 2.6 ARMOR: Aligning Secure and Safe LLMs via Meticulous Reasoning

| 属性 | 内容 |
|------|------|
| **标题** | ARMOR: Aligning Secure and Safe Large Language Models via Meticulous Reasoning |
| **中文标题** | ARMOR: 通过缜密推理对齐安全 LLM |
| **Venue** | ICLR 2026 |

**方法**：引入结构化三步推理流水线：(1) 从可更新的外部策略库分析越狱策略；(2) 提取核心意图；(3) 应用基于策略的安全验证。ARMOR-Think 将安全推理与通用推理解耦。在先进的优化越狱攻击下平均有害率仅 0.002，攻击成功率 0.06，远低于其他推理安全模型（ASR >0.40）。

---

### 2.7 KLDO / FDO: Alignment as Divergence Estimation

| 属性 | 内容 |
|------|------|
| **标题** | Alignment as Divergence Estimation (KLDO/FDO) |
| **中文标题** | 对齐作为散度估计 |
| **Venue** | NeurIPS 2025 & ICLR 2026 |

**理论贡献**：建立统一理论框架证明流行的 LLM 对齐方法（RLHF、DPO 等）可理解为散度估计器。提出 KLDO（KL 散度优化）方法。理论证明对齐方法在隐空间中诱导安全/有害提示的分离（separation effect），且 compliance-refusal 数据比 preference 数据产生更强的分离和鲁棒性。

---

### 2.8 RACO: Reward-Free Preference Alignment via Clipped CAGrad

| 属性 | 内容 |
|------|------|
| **标题** | RACO: Reward-Free Preference Alignment |
| **中文标题** | RACO: 无奖励偏好对齐 |
| **Venue** | ICLR 2026 AFAA (Main Track) |

**方法**：在无需显式奖励模型的情况下，通过多目标优化直接处理冲突目标。引入 clipped variant of conflict-averse gradient descent (CAGrad) 来缓解大规模 LLM 微调中的不稳定性。在 Qwen3、Llama3、Gemma3 上验证，一致实现更好的 Pareto 权衡。

---

### 2.9 OXRL: Large-Scale Post-Training Algorithm Comparison

| 属性 | 内容 |
|------|------|
| **标题** | OXRL: A Unified Framework for Post-Training Comparison |
| **中文标题** | OXRL: 后训练算法统一比较框架 |
| **arXiv** | [2603.19335](https://arxiv.org/abs/2603.19335) |

**规模**：实现 51 种后训练算法，8 种核心算法在 4 种模型规模（0.5B–7B）上评估，20 种 DPO 变体在 1.5B 上比较（100 次运行，5 个 seed 各），总计约 240 次训练运行。

**核心发现**：
1. 算法排名在不同规模下反转：1.5B 时 SGRPO 最佳（58.0%），7B 时 SimPO 最佳
2. 20 种 DPO 变体无一显著优于 vanilla DPO（Bonferroni 校正后）
3. 影响层级：规模（~50pp）> 训练范式（~10pp）> online/offline（~9pp）> 损失函数（~1pp）

---

### 2.10 SP2DPO: Semantic Per-Pair DPO

| 属性 | 内容 |
|------|------|
| **标题** | SP2DPO: An LLM-assisted Semantic Per-Pair DPO Generalization |
| **中文标题** | SP2DPO: LLM 辅助的语义逐对 DPO 泛化 |
| **arXiv** | [2601.22385](https://arxiv.org/abs/2601.22385) |

**方法**：用全局超参数 β 替换为逐实例温度 βi，通过教师 LLM 离线注释语义偏好差距来确定。在 UltraFeedback（59,960 对）和 AlpacaEval 2.0 上验证，在多个 backbone 上匹配或改进调参后的全局 β DPO。

---

## 3. NeurIPS 2025 收录论文

### 3.1 Gated Attention (Best Paper)

| 属性 | 内容 |
|------|------|
| **标题** | Gated Attention |
| **中文标题** | 门控注意力 |
| **机构** | Alibaba/Qwen Team |
| **Venue** | NeurIPS 2025 Best Paper |
| **备注** | 之前已记录 |

### 3.2 LLM Post-Training: Unified View (Survey)

| 属性 | 内容 |
|------|------|
| **标题** | Large Language Model Post-Training: A Unified View of Off-Policy and On-Policy Learning |
| **中文标题** | LLM 后训练：离策略与在策略学习的统一视角 |
| **Venue** | NeurIPS 2025 |
| **arXiv** | [2604.07941](https://arxiv.org/abs/2604.07941) |

**贡献**：统一了指令微调、偏好优化、RLHF、RLVR、蒸馏等后训练方法。核心观点：许多方法不是孤立的替代方案，而是对同一底层对象（由轨迹分布诱导的模型行为）的不同干预方式。

---

### 3.3 Preference Learning Survey

| 属性 | 内容 |
|------|------|
| **标题** | A Unified Survey of Preference Learning Methods |
| **中文标题** | 偏好学习方法统一综述 |
| **arXiv** | [2601.06108](https://arxiv.org/abs/2601.06108) |

**统一框架**：将 DPO、IPO、KTO、SimPO、ORPO、GRPO 等统一为一般 ΨPO 框架的特例，分解为正交的三大支柱：(I) 偏好模型、(II) 正则化、(III) 数据分布。证明在线/离线方法的覆盖分离定理（coverage separation theorem），解释 SimPO 成功的原因（处理长度偏差 + 参考模型校准错误），并为实践者提供方法选择指南。

---

## 4. WWW 2026 / SIGIR 2026 / CIKM 2025 推荐系统论文

### 4.1 Memento: Personalized RAG-Style Long-Retention (Meta/Facebook)

| 属性 | 内容 |
|------|------|
| **标题** | Memento: Personalized RAG-Style Long-Retention Data Scaling for Online Ads Recommendation |
| **中文标题** | Memento: 个性化 RAG 风格长周期数据缩放用于在线广告推荐 |
| **机构** | Meta (Facebook) |
| **arXiv** | [2605.24051](https://arxiv.org/abs/2605.24051) |

**问题背景**：长历史数据建模面临注意力稀释、系统效率和灾难性遗忘三大挑战。简单的 LastN 线性缩放方法的性能在约 70 天（CTR 模型）和 180 天（CVR 模型）后饱和。

**方法详述**：将用户完整历史视为文档语料库，将广告请求视为查询，使用 Maximal Marginal Relevance (MMR) 检索相关交互，平衡相似性与多样性。两种应用：
- **Representation Memento**：检索历史 embedding 用于特征增强
- **Data Memento**：检索历史训练样本用于多遍训练

通过时间分块、INT8 量化和异步服务实现 5–10× 资源效率提升。

**实验结果（在线 A/B）**：

| 指标 | 提升 |
|------|------|
| CTR lift (Facebook Feed & Reels) | +1.0% |
| CVR lift (Offsite Conversion) | +1.2% |
| NE gain (365-day retention) | 0.25–0.30% |
| 延迟 | <10ms |

---

### 4.2 GenCI: Generative User Interest Modeling (WWW 2026)

| 属性 | 内容 |
|------|------|
| **标题** | GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning for CTR Prediction |
| **中文标题** | GenCI: 通过基于 Cohort 的意图学习生成式建模用户兴趣转移 |
| **Venue** | WWW 2026 |
| **arXiv** | [2601.18251](https://arxiv.org/abs/2601.18251) |

**方法**：离散判别式 CTR 模型只关注候选与历史匹配，难以捕捉快速兴趣转移。GenCI 使用 next-item prediction (NTP) 生成式模型主动生成语义兴趣 cohort，作为候选无关的即时意图表示。层次化候选感知网络通过交叉注意力补充内容信号。

---

### 4.3 SparseCTR: Sparse Attention for Long-Term Behaviors (WWW 2026)

| 属性 | 内容 |
|------|------|
| **标题** | Unleashing the Potential of Sparse Attention on Long-term Behaviors for CTR Prediction |
| **中文标题** | 释放稀疏注意力在 CTR 预测中长期行为建模的潜力 |
| **机构** | Meituan |
| **Venue** | WWW 2026 |
| **arXiv** | [2601.17836](https://arxiv.org/abs/2601.17836) |

**方法**：提出个性化时间感知分块方法 TimeChunking，结合三分支稀疏注意力机制（全局兴趣、兴趣迁移、短期兴趣）。使用相对时间编码捕获复杂时序关系。在线 A/B 测试 CTR +1.72%，CPM +1.41%，推理时间维持 40ms。

---

## 5. CTR 预测与工业推荐系统（arXiv 2025-2026）

### 5.1 CADET: Context-Conditioned Decoder-Only Transformer (LinkedIn)

| 属性 | 内容 |
|------|------|
| **标题** | CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer |
| **中文标题** | CADET: 上下文条件的广告 CTR 预测解码器 Transformer |
| **机构** | LinkedIn |
| **arXiv** | [2602.11410](https://arxiv.org/abs/2602.11410) |

**问题背景**：DLRM 长期主导广告 CTR 预测，但后置评分信号（如广告位置）与 CTR 预测之间存在鸡生蛋问题——预测 CTR 需要位置，但位置由 CTR 排序决定。

**方法详述**：提出五项创新：
1. **上下文条件解码架构**：多塔预测头显式建模后置评分信号
2. **自门控注意力**（Self-Gated Attention）：自适应调控信息流稳定训练
3. **时间戳 RoPE**：捕获秒到月的时间关系
4. **Session Masking**：防止模型学习不可用的会话内事件依赖
5. 工程优化：tensor packing、sequence chunking、自定义 Flash Attention

**实验结果（在线 A/B）**：

| 指标 | 提升 |
|------|------|
| CTR | +11.04% |
| 对比基线 | LiRank (DCNv2 + 序列编码器混合集成) |

---

### 5.2 LoopCTR: Loop Scaling Paradigm

| 属性 | 内容 |
|------|------|
| **标题** | LoopCTR: Scaling Transformer-based Click-Through Rate Prediction via Recursive Computation |
| **中文标题** | LoopCTR: 通过递归计算缩放 Transformer CTR 预测 |
| **arXiv** | [2604.19550](https://arxiv.org/abs/2604.19550) |

**核心思想**：复用相同模型层，通过递归循环潜在推理增加计算量，将计算与参数增长解耦。sandwich 架构（Entry Block + Loop Block + Exit Block）分别编码特征、迭代推理和评分预测。采用 Hyper-Connected Residuals 和 MoE 扩展表示能力。

**关键发现**：
- 训练时多循环、推理时零循环（train-multi-loop, infer-zero-loop）策略匹配或超越全循环推理
- Oracle 分析揭示 0.02–0.04 AUC 未开发空间
- 较少循环训练的模型反而具有更高的 oracle 上界

---

### 5.3 GRAB: Generative Ranking for Ads at Baidu

| 属性 | 内容 |
|------|------|
| **标题** | GRAB: An LLM-Inspired Sequence-First Click-Through Rate Prediction Framework for Ads at Baidu |
| **中文标题** | GRAB: 百度广告的 LLM 启发序列优先 CTR 预测框架 |
| **机构** | Baidu |
| **arXiv** | [2602.01865](https://arxiv.org/abs/2602.01865) |

**方法**：端到端生成式 CTR 框架，引入 Causal Action-aware Multi-channel Attention (CamA) 捕获用户行为序列中的时序动态和特定动作信号。采用 Sequence-to-Sequence (STS) 训练范式缓解分布偏移。

**实验结果**：

| 指标 | 提升 |
|------|------|
| CTR (线上) | +3.49% |
| CPM (线上) | +3.05% |
| 对比基线 | DLRM + 其他 GR 模型 |

---

### 5.4 EST: Efficient Scaling Laws for CTR (Alibaba/Taobao)

| 属性 | 内容 |
|------|------|
| **标题** | EST: Towards Efficient Scaling Laws in CTR Prediction via Unified Modeling |
| **中文标题** | EST: 通过统一建模实现 CTR 预测的高效缩放律 |
| **机构** | Alibaba (Taobao) |
| **arXiv** | [2602.10811](https://arxiv.org/abs/2602.10811) |

**方法**：分析 CTR 输入与 LLM token 在信息密度和模态上的本质差异，推导出高效 Transformer 的两个设计原则。提出 Lightweight Cross-Attention (LCA) 减少冗余计算，Content Sparse Attention (CSA) 利用内容相似性进行稀疏建模。

**实验结果**：

| 场景 | CTR | RPM |
|------|-----|-----|
| Guess (猜你喜欢) | +1.22% | +3.27% |
| Post (购后) | +2.01% | +2.66% |

---

### 5.5 LLM-HYPER: Generative CTR for Cold-Start (Top US E-commerce)

| 属性 | 内容 |
|------|------|
| **标题** | LLM-HYPER: Generative CTR Modeling for Cold-Start Ad Personalization via LLM-Based Hypernetworks |
| **中文标题** | LLM-HYPER: 基于 LLM 超网络的冷启动广告个性化生成式 CTR 建模 |
| **机构** | 美国头部电商平台 |
| **arXiv** | [2604.12096](https://arxiv.org/abs/2604.12096) |

**方法**：首次将 LLM 作为超网络直接生成 CTR 估计器的参数。使用 few-shot CoT 推理多模态广告内容（文本+图像）来推断特征级权重。通过 CLIP embedding 检索语义相似的过去活动格式化为 prompt 示例。在冷启动 NDCG@10 上改善 55.9%，在线 A/B 测试与 warm-start 模型性能无统计差异。

---

### 5.6 RankUp: High-Rank Representations (Tencent/WeChat)

| 属性 | 内容 |
|------|------|
| **标题** | RankUp: Towards High-rank Representations for Large Scale Advertising Recommender Systems |
| **中文标题** | RankUp: 大规模广告推荐系统的高秩表示 |
| **机构** | Tencent (WeChat) |
| **arXiv** | [2604.17878](https://arxiv.org/abs/2604.17878) |
| **Venue** | KDD 2026 |

**问题背景**：RankMixer 发现 token 表示的有效秩随层深度呈现阻尼振荡轨迹，深层甚至退化。RankUp 通过随机置换分割稀疏特征、多 embedding 范式、全局 token 集成和交叉预训练 embedding token 来缓解表示坍缩。

**线上业务指标**：

| 场景 | GMV 提升 |
|------|----------|
| 微信视频号 | +3.41% |
| 公众号 | +4.81% |
| 朋友圈 | +2.12% |

---

### 5.7 HeMix: Scalable CTR Model (Alibaba/AMAP)

| 属性 | 内容 |
|------|------|
| **标题** | HeMix: A Scalable CTR Model for Industrial Recommender Systems |
| **中文标题** | HeMix: 工业推荐系统的可扩展 CTR 模型 |
| **机构** | Alibaba (AMAP/高德) |
| **arXiv** | [2602.09387](https://arxiv.org/abs/2602.09387) |

**方法**：Query-Mixed Interest Extraction 模块，通过动态和固定查询分别建模上下文感知和上下文无关的用户兴趣。HeteroMixer block 采用多 token 融合、异构交互和组对齐重建三条流水线。线上 A/B GMV +3.61%，PV_CTR +2.78%，UV_CVR +2.12%。

---

### 5.8 GR4AD: Generative Recommendation for Advertising (Kuaishou)

| 属性 | 内容 |
|------|------|
| **标题** | Generative Recommendation for Large-Scale Advertising |
| **中文标题** | 大规模广告的生成式推荐 |
| **机构** | Kuaishou |
| **arXiv** | [2602.22732](https://arxiv.org/abs/2602.22732) |

**方法**：提出 UA-SID 统一广告语义 ID，LazyAR（惰性自回归解码器）扩展层间依赖用于短多候选生成，VSL（价值感知监督学习）和 RSPO（排序引导 Softmax 偏好优化）。动态 beam serving 根据负载调整 beam 宽度。在线 A/B 广告收入提升高达 4.2%，已在覆盖 4 亿+用户的快手广告系统全面部署。

---

### 5.9 ByteDance CTR 模型系列

| 模型 | 核心贡献 | 线上提升 | arXiv |
|------|---------|---------|-------|
| **HyFormer** | Query Decoding + Query Boosting 交替优化，统一序列建模与特征交互 | 超越 LONGER+RankMixer 基线 | [2601.12681](https://arxiv.org/abs/2601.12681) |
| **MixFormer** | 统一参数化实现稠密容量和序列长度的联合缩放 | 抖音+抖音 Lite 活跃天数和使用时长提升 | [2602.14110](https://arxiv.org/abs/2602.14110) |
| **TokenMixer-Large** | 7B/15B 参数缩放，Mixing-and-Reverting + Sparse Per-token MoE | 电商 GMV +2.98%，广告 ADSS +2.0% | [2602.06563](https://arxiv.org/abs/2602.06563) |
| **LEMUR** | 首个端到端多模态推荐系统，联合优化多模态和排序目标 | QAUC +0.81%，查询变化率 -0.843% | [2511.10962](https://arxiv.org/abs/2511.10962) |
| **LONGER** | Global Token + Token Merge + Hybrid Attention 实现超长序列建模 | 数十个业务场景部署 | [2505.04421](https://arxiv.org/abs/2505.04421) |
| **SIF** | Sample Is Feature：样本级 token 超越物品级表示 | CTR +2.03%，CVR +1.21%，GMV +1.35% | [2604.15650](https://arxiv.org/abs/2604.15650) |

---

## 6. 智能体系统与工具增强推理

### 6.1 DeepAgent: General Reasoning Agent with Scalable Toolsets

| 属性 | 内容 |
|------|------|
| **标题** | DeepAgent: A General Reasoning Agent with Scalable Toolsets |
| **中文标题** | DeepAgent: 具有可扩展工具集的通用推理智能体 |
| **机构** | Renmin University of China (RUC-NLPIR) |
| **arXiv** | [2510.21618](https://arxiv.org/abs/2510.21618) |

**方法**：端到端深度推理智能体，在单一连贯推理过程中自主思考、工具发现和动作执行。引入自主记忆折叠机制（autonomous memory folding）将过去交互压缩为结构化情景记忆、工作记忆和工具记忆。提出 ToolPO（端到端 RL 训练策略），利用 LLM 模拟 API 和工具调用优势归因分配细粒度信用。

**实验结果**：在 ToolBench、API-Bank、ALFWorld、WebShop、GAIA、HLE 等 8 个基准上一致超越工作流基线和现有方法。

---

### 6.2 TRICE: Tool-Integrated Reasoning Recipe

| 属性 | 内容 |
|------|------|
| **标题** | Teaching Thinking Models to Reason with Tools: A Full-Pipeline Recipe for Tool-Integrated Reasoning |
| **中文标题** | 教思维模型使用工具推理：工具集成推理的完整流程食谱 |
| **arXiv** | [2605.06326](https://arxiv.org/abs/2605.06326) |

**核心发现**：(i) TIR SFT 有效性取决于教师轨迹的可学习性；(ii) 控制工具轨迹比例可缓解文本推理能力的灾难性遗忘；(iii) 用 pass@k 和响应长度而非训练损失来最大化 SFT 收益；(iv) 稳定的 RLVR 阶段在适当的 SFT 初始化上提供简单而有效的解决方案。Qwen3-4B 在 AIME 2025 达 96.7%，30B 达 99.2%。

---

### 6.3 HTAA: Hybrid Toolset Agentization

| 属性 | 内容 |
|------|------|
| **标题** | HTAA: Enhancing LLM Planning via Hybrid Toolset Agentization & Adaptation |
| **中文标题** | HTAA: 通过混合工具集代理化和自适应增强 LLM 规划 |
| **arXiv** | [2604.10917](https://arxiv.org/abs/2604.10917) |

**方法**：工具集代理化（toolset agentization）将频繁共用的工具封装为专门的 agent tool，减少规划器的动作空间。不对齐规划器适配（Asymmetric Planner Adaptation）通过后向重构和前向精炼的轨迹训练范式对齐高层规划器与 agent tool。使用 GPT-5.2 管理底层工具编排。

---

### 6.4 AgentMath: Tool-Augmented Agent for Math

| 属性 | 内容 |
|------|------|
| **标题** | AgentMath: Empowering Mathematical Reasoning via Tool-Augmented Agent |
| **中文标题** | AgentMath: 通过工具增强智能体赋能数学推理 |
| **arXiv** | [2512.20745](https://arxiv.org/abs/2512.20745) |

**创新点**：自动化将自然语言 CoT 转换为结构化工具增强轨迹的新型 agentic RL 范式。支持自然语言生成与实时代码执行的动态交错，模型可自主学习最优工具调用策略。请求级异步调度、agentic partial rollout 等训练系统优化实现 4–5× 训练效率提升。AgentMath-30B-A3B 在 AIME24 达 90.6%。

---

### 6.5 TInR: Tool-Internalized Reasoning

| 属性 | 内容 |
|------|------|
| **标题** | TInR: Exploring Tool-Internalized Reasoning in Large Language Models |
| **中文标题** | TInR: 探索 LLM 中的工具内化推理 |
| **arXiv** | [2604.10788](https://arxiv.org/abs/2604.10788) |

**方法**：将工具知识内化到 LLM 参数中，避免推理时依赖外部工具文档。三阶段训练：(1) 工具内化（双向知识对齐）；(2) TInR SFT warm-up；(3) TInR RL 专用奖励。在域内和域外设置均达到 SOTA。

---

### 6.6 Agentic AI Survey

| 属性 | 内容 |
|------|------|
| **标题** | Agentic Artificial Intelligence: Architectures, Taxonomies, and Evaluation of LLM Agents |
| **中文标题** | Agentic AI: 架构、分类法和评估综述 |
| **arXiv** | [2601.12560](https://arxiv.org/abs/2601.12560) |

**贡献**：提出统一的六维分类法（感知、大脑、规划、行动、工具使用、协作），覆盖从简单单环智能体到层次化多智能体系统的全谱系设计。讨论 MCP 协议、Native Computer Use、执行中的幻觉、无限循环、prompt 注入等关键挑战。

---

### 6.7 GraSP: Graph-Structured Skill Compositions

| 属性 | 内容 |
|------|------|
| **标题** | GraSP: Graph-Structured Skill Compositions for LLM Agents |
| **中文标题** | GraSP: LLM 智能体的图结构技能组合 |
| **arXiv** | [2604.17870](https://arxiv.org/abs/2604.17870) |

**核心发现**：智能体的瓶颈已从技能可用性转向技能编排——提供更多技能反而损害性能。GraSP 引入编译层将扁平技能集转换为带条件-效果边的类型化 DAG，减少重规划成本从 O(N) 到 O(d^h)。在 ALFWorld、ScienceWorld 等任务上，奖励最高提升 +19 点，环境步数减少 41%。

---

### 6.8 BIGMAS: Brain-Inspired Graph Multi-Agent Systems

| 属性 | 内容 |
|------|------|
| **标题** | BIGMAS: Brain-Inspired Graph Multi-Agent Systems for LLM Reasoning |
| **中文标题** | BIGMAS: 脑启发图多智能体系统 |
| **arXiv** | [2603.15371](https://arxiv.org/abs/2603.15371) |

**方法**：受全局工作空间理论（Global Workspace Theory）启发，专门化 LLM 智能体作为动态有向图节点，通过集中式共享工作空间协调。问题自适应 GraphDesigner 构建任务特定拓扑，全局 Orchestrator 利用完整共享状态进行路由决策。在 Game24、Six Fives、Tower of London 上使用 6 种前沿 LLM 一致超越 ReAct 和 Tree of Thoughts。

---

### 6.9 AgentFugue: Agent Scaling via Collective Reasoning

| 属性 | 内容 |
|------|------|
| **标题** | AgentFugue: Agent Scaling for Long-Horizon Tasks through Collective Reasoning |
| **中文标题** | AgentFugue: 通过集体推理实现长时域任务的智能体缩放 |
| **arXiv** | [2605.24486](https://arxiv.org/abs/2605.24486) |

**方法**：围绕共享推理中心（shared reasoning hub）构建的集体推理框架。智能体完成连贯交互片段时，中心记录紧凑笔记；其他智能体可选择性地访问。同构团队（相同配置）和异构团队（不同模型/设置）均受益。中心使用 Qwen3.5-9B，通过 SFT + 端到端 RL 优化。

---

## 7. 多智能体系统与游戏 AI

### 7.1 SPIRAL: Self-Play on Zero-Sum Games

| 属性 | 内容 |
|------|------|
| **标题** | SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL |
| **中文标题** | SPIRAL: 零和博弈自对弈通过多智能体多轮 RL 激励推理 |
| **arXiv** | [2506.24119](https://arxiv.org/abs/2506.24119) |

**方法**：模型通过与不断改进的自身版本进行多轮零和游戏自对弈训练。提出 role-conditioned advantage estimation (RAE) 稳定多智能体训练。跨 8 个推理基准提升高达 10%，多游戏训练（井字棋、Kuhn Poker、Simple Negotiation）效果最佳。即使已通过 RLVR 训练的 DeepSeek-R1-Distill-Qwen-7B 仍受益。

---

### 7.2 Strat-Reasoner: Strategic Reasoning in Multi-Agent Games

| 属性 | 内容 |
|------|------|
| **标题** | Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games |
| **中文标题** | Strat-Reasoner: 在多智能体博弈中强化 LLM 策略推理 |
| **arXiv** | [2605.04906](https://arxiv.org/abs/2605.04906) |

**方法**：递归推理范式——集成其他智能体的推理过程到自身决策中。集中式 CoT 比较模块评估推理质量，混合优势估计结合中间 CoT 分数与传统回报优势。在多种多智能体博弈中平均提升 22.1%。

---

### 7.3 Dr. MAS: Stable RL for Multi-Agent LLM Systems

| 属性 | 内容 |
|------|------|
| **标题** | Dr. MAS: Stable Reinforcement Learning for Multi-Agent LLM Systems |
| **中文标题** | Dr. MAS: 多智能体 LLM 系统的稳定强化学习 |
| **arXiv** | [2602.08847](https://arxiv.org/abs/2602.08847) |

**理论发现**：GRPO 风格的全局归一化基线可能偏离不同智能体的奖励分布，导致梯度范数不稳定。提出逐智能体归一化方案，在数学推理上 avg@16 +5.6%，搜索任务上 avg@16 +15.2%。

---

### 7.4 MetaAgent-X: End-to-End RL for MAS

| 属性 | 内容 |
|------|------|
| **标题** | MetaAgent-X: Breaking the Ceiling of Automatic Multi-Agent Systems via End-to-End RL |
| **中文标题** | MetaAgent-X: 通过端到端 RL 突破自动多智能体系统的天花板 |
| **arXiv** | [2605.14212](https://arxiv.org/abs/2605.14212) |

**方法**：端到端 RL 框架联合优化 MAS 设计和执行。提出 Executor-Designer Hierarchical Rollout 和 Stagewise Co-evolution。在 6 个数学和代码基准上超越基线高达 21.7%。

---

### 7.5 Graph-GRPO: Multi-Agent Topology Learning

| 属性 | 内容 |
|------|------|
| **标题** | Graph-GRPO: Stabilizing Multi-Agent Topology Learning via Group Relative Policy Optimization |
| **中文标题** | Graph-GRPO: 通过组相对策略优化稳定多智能体拓扑学习 |
| **arXiv** | [2603.02701](https://arxiv.org/abs/2603.02701) |

**方法**：首个将 GRPO 机制适应到离散结构搜索领域的框架。对每个查询采样一组不同的通信图，基于组内相对表现计算特定边的优势。在 GSM8K 和 HumanEval 上显著超越 SOTA 基线。

---

### 7.6 OMAD: Online Multi-Agent Diffusion Policies

| 属性 | 内容 |
|------|------|
| **标题** | OMAD: Online Off-policy MARL with Diffusion Policies |
| **中文标题** | OMAD: 扩散策略的在线离策略多智能体 RL |
| **arXiv** | [2602.18291](https://arxiv.org/abs/2602.18291) |

**方法**：首个在线 MARL 框架采用扩散策略协调。关键创新：最大化缩放联合熵的松弛策略目标，不依赖可处理似然。联合分布值函数在 CTDE 范式下优化去中心化扩散策略。在 MPE 和 MAMuJoCo 上实现 2.5×–5× 样本效率改进。

---

### 7.7 When Does Multi-Agent RL Improve LLM Workflows?

| 属性 | 内容 |
|------|------|
| **标题** | When Does Multi-Agent RL Improve LLM Workflows? Workflow, Scale, and Policy-Sharing Tradeoffs |
| **中文标题** | 多智能体 RL 何时改进 LLM 工作流？工作流、规模和策略共享的权衡 |
| **arXiv** | [2605.24202](https://arxiv.org/abs/2605.24202) |

**核心发现**：在 3 种工作流（Eval-Opt、Voting、Orch-Workers）、2 种任务、3 种模型规模（0.6B–4B）上系统实验。策略共享训练路由训练压力通过不同渠道，而非提供统一稳定性。isolated-policy 达到更高峰值准确率但更易崩溃，shared-policy 不消除失败而是重新分配失败模式。

---

## 8. LLM 对齐、安全与后训练

### 8.1 Efficient Exploration at Scale (Google DeepMind)

| 属性 | 内容 |
|------|------|
| **标题** | Efficient Exploration at Scale |
| **中文标题** | 大规模高效探索 |
| **机构** | Google DeepMind (Efficient Agent Team) |
| **arXiv** | [2603.17378](https://arxiv.org/abs/2603.17378) |

**方法**：在线学习算法通过增量更新奖励和语言模型大幅提升 RLHF 数据效率。引入小肯定性推动（affirmative nudge）、认知神经网络（epistemic neural network）建模奖励不确定性、信息导向探索（information-directed exploration）。

**结果**：匹配基于 200K 标签的离线 RLHF 仅需 <20K 标签（10× 效率增益）。外推至 1M 标签可匹配离线 RLHF 在 1B 标签上的性能（1,000× 增益）。使用 Gemma 9B 模型。

---

### 8.2 GOPO: Group Orthogonalized Policy Optimization

| 属性 | 内容 |
|------|------|
| **标题** | GOPO: Group Orthogonalized Policy Optimization |
| **中文标题** | GOPO: 分组正交化策略优化 |
| **arXiv** | [2602.21269](https://arxiv.org/abs/2602.21269) |

**方法**：从 Hilbert 空间投影视角推导对齐算法。将策略优化从无约束函数空间提升到经验组级子空间，化学势（chemical potential）在组归一化下消失。引入 Bounded Hilbert Projection 强制非负性。在数学推理基准上验证，GOPO 在策略熵和高置信区间可持续学习。

---

### 8.3 LambdaPO: Lambda Style Policy Optimization

| 属性 | 内容 |
|------|------|
| **标题** | LambdaPO: A Lambda Style Policy Optimization for Reasoning Language Models |
| **中文标题** | LambdaPO: 推理语言模型的 Lambda 式策略优化 |
| **arXiv** | [2605.19416](https://arxiv.org/abs/2605.19416) |

**方法**：重新构思 GRPO 的优势估计，从标量值解构为分解的逐对偏好结构。每个轨迹的优势形式化为对所有同组同行的奖励差分的积分和，每个比较由策略自身概率置信度动态衰减。引入语义密度奖励缓解二元结果监督的稀疏性。

---

### 8.4 MaR: Metacognition as Reward

| 属性 | 内容 |
|------|------|
| **标题** | MaR: Metacognition as Reward for LLM Reasoning |
| **中文标题** | MaR: 元认知作为 LLM 推理的奖励 |
| **arXiv** | [2605.23384](https://arxiv.org/abs/2605.23384) |

**方法**：通过两个通用过程维度指导 LLM 推理：(i) 元认知知识（无需手工实例特定评分标准）；(ii) 元认知调节（计划和调整推理过程）。在 22 个基准上 Qwen3.5-9B + MaR 较 base 提升 7.7%，较 vanilla DAPO 提升 11.0%，超越 GPT-OSS-120B 平均分。

---

### 8.5 Value-Gradient Hypothesis of RL for LLMs

| 属性 | 内容 |
|------|------|
| **标题** | Value-Gradient Hypothesis of RL for LLMs |
| **中文标题** | LLM 的 RL 值梯度假说 |
| **arXiv** | [2605.21654](https://arxiv.org/abs/2605.21654) |

**理论**：证明无 critic 的 RL（PPO/GRPO）在可微分 rollout 下的 actor 更新在期望上等于值梯度。对离散 Transformer 策略，自微分通过注意力产生近似值信号的 empirical costate。推导 RL 影响分解为可用值梯度信号和可达奖励空间，可用于预训练过程中 checkpoint 选择。

---

### 8.6 CharacterFlywheel (Meta AI)

| 属性 | 内容 |
|------|------|
| **标题** | CharacterFlywheel: Iterative LLM Improvement for Social Chat |
| **中文标题** | CharacterFlywheel: LLM 社交聊天的迭代改进飞轮 |
| **机构** | Meta AI |
| **arXiv** | [2603.01973](https://arxiv.org/abs/2603.01973) |

**方法**：基于 Llama 3.1 70B 的迭代飞轮流程，包含数据整理、奖励建模、SFT、DPO 和 RL。从使用 Online DPO 最终切换到 GRPO（A/B 测试表现更优），经过 8 次产品发布后迭代改进。

---

## 9. 代码生成与执行预测

### 9.1 Self-Execution Simulation (Code LLMs)

| 属性 | 内容 |
|------|------|
| **标题** | Self-Execution Simulation Improves Coding Models |
| **中文标题** | 自执行模拟改进代码模型 |
| **arXiv** | [2604.03253](https://arxiv.org/abs/2604.03253) |

**方法**：SFT（自然语言执行轨迹）+ RL（可验证奖励）。两个互补目标：给定代码和输入的输出预测，以及使用真实或自预测执行反馈解决竞赛编程任务。自验证在 best@k 设置下提供 2–8 个百分点的提升。

---

### 9.2 CodeSpecBench: Executable Behavioral Specification

| 属性 | 内容 |
|------|------|
| **标题** | CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation |
| **中文标题** | CodeSpecBench: LLM 可执行行为规范生成基准 |
| **arXiv** | [2604.12268](https://arxiv.org/abs/2604.12268) |

**发现**：评估 15 个 SOTA LLM，函数级任务表现中等，仓库级任务最佳模型（Claude-4.5-Sonnet）仅 20.2% 通过率。规范生成比代码生成困难得多，表明强的代码生成能力不意味着对预期程序行为的深层理解。

---

### 9.3 SpecBench: Measuring Reward Hacking in Coding Agents

| 属性 | 内容 |
|------|------|
| **标题** | SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents |
| **中文标题** | SpecBench: 长时域编码智能体中的奖励黑客测量 |
| **arXiv** | [2605.21384](https://arxiv.org/abs/2605.21384) |

**方法**：将 SE 任务分解为三部分：规范 NL 描述、可见验证测试、隐藏组合测试。用可见/隐藏测试通过率差距量化奖励黑客。30 个系统级编程任务（1.5K–110K LOC）。任务长度每增加 10 倍，差距扩大 28 个百分点。发现一个 2900 行的哈希表"编译器"通过记忆测试输入作弊。

---

### 9.4 FeatureBench: Agentic Coding for Complex Features

| 属性 | 内容 |
|------|------|
| **标题** | FeatureBench: Benchmarking Agentic Coding for Complex Feature Development |
| **中文标题** | FeatureBench: 复杂功能开发的智能体编码基准 |
| **arXiv** | [2602.10975](https://arxiv.org/abs/2602.10975) |

**规模**：200 个任务、3825 个可执行环境，24 个开源仓库。Claude 4.5 Opus 在 SWE-bench 上 74.4% 通过率，但在 FeatureBench 仅 11.0%。

---

### 9.5 FOREAGENT: Predict-then-Verify for ML Agents

| 属性 | 内容 |
|------|------|
| **标题** | Can We Predict Before Executing Machine Learning Agents? |
| **中文标题** | 我们能在执行 ML 智能体之前预测吗？ |
| **arXiv** | [2601.05930](https://arxiv.org/abs/2601.05930) |

**方法**：LLM 在执行前预测代码执行结果的 implicit world model。FOREAGENT 使用 Predict-then-Verify 循环实现 6× 加速，探索空间扩大 3.2×，同时性能提升 6%。

---

### 9.6 更多代码基准

| 基准 | 焦点 | 链接 |
|------|------|------|
| **ProdCodeBench** | 面向生产的代码助手基准（7 语言） | [2604.01527](https://arxiv.org/abs/2604.01527) |
| **CONCUR** | 首个并发代码生成基准（JPF 模型检查） | [2603.03683](https://arxiv.org/abs/2603.03683) |
| **ProcCtrlBench** | 编码智能体执行过程质量评估 | [2605.20251](https://arxiv.org/abs/2605.20251) |
| **IndustryCode** | 跨多工业领域代码生成基准 | [2604.02729](https://arxiv.org/abs/2604.02729) |
| **VISTA** | 视觉规格到 Web 应用端到端基准 | [2605.26144](https://arxiv.org/abs/2605.26144) |

---

## 10. Google DeepMind 系统与模型

### 10.1 Gemini Embedding 2: Native Multimodal Embedding

| 属性 | 内容 |
|------|------|
| **标题** | Gemini Embedding 2: A Native Multimodal Embedding Model from Gemini |
| **中文标题** | Gemini Embedding 2: Gemini 的原生多模态 Embedding 模型 |
| **机构** | Google DeepMind |
| **arXiv** | [2605.27295](https://arxiv.org/abs/2605.27295) |

**方法**：原生支持视频、音频、图像、文本的统一表示空间。利用 Gemini 的多模态能力进行大规模对比学习，多任务多阶段训练。在 MSCOCO R@1 62.9、Vatex NDCG@10 68.8、MTEB 多语言 69.9、MTEB Code 84.0。在天文学、生物科学、美术等专业领域零样本表现优异。

---

### 10.2 Improving Latent Generalization Using Test-time Compute

| 属性 | 内容 |
|------|------|
| **标题** | Improving Latent Generalization Using Test-time Compute |
| **中文标题** | 使用测试时计算改进潜在泛化 |
| **机构** | Google DeepMind |
| **arXiv** | [2604.01430](https://arxiv.org/abs/2604.01430) |

**发现**：LLM 可以利用测试时计算（thinking）改善潜在泛化——在仅从参数知识生成响应时解决演绎推理挑战。但纯粹的逻辑反转（reversal curse）即使对 augmented 模型也很困难，暗示 Transformer 架构和自回归 next-token 预测目标的刚性 KV 关联记忆结构。

---

### 10.3 Gemini for Google (GfG)

| 属性 | 内容 |
|------|------|
| **标题** | Customizing an LLM for Enterprise Software Engineering |
| **中文标题** | 为企业软件工程定制 LLM |
| **机构** | Google DeepMind |
| **arXiv** | [2605.16517](https://arxiv.org/abs/2605.16517) |

**方法**：基于 Gemini，在万亿 token 专有数据集上微调，引入 mid-training 策略缓解灾难性遗忘。在 29,000 名 Google 开发者上的盲 A/B 测试中：每次轮次迭代减少 23%，代码存活率提升 17%。

---

### 10.4 Aletheia: Mathematics Research Agent

| 属性 | 内容 |
|------|------|
| **标题** | Aletheia tackles FirstProof autonomously |
| **中文标题** | Aletheia 自主攻克 FirstProof 挑战 |
| **机构** | Google DeepMind |
| **arXiv** | [2602.21201](https://arxiv.org/abs/2602.21201) |

**结果**：基于 Gemini 3 Deep Think 的数学研究智能体，在 FirstProof 挑战中自主解决 10 个问题中的 6 个（专家多数评估）。某些问题无需大规模推理预算即可解决，表明智能体框架和基座模型的双重改进。

---

### 10.5 Generative UI: LLMs as UI Generators

| 属性 | 内容 |
|------|------|
| **标题** | Generative UI: LLMs are Effective UI Generators |
| **中文标题** | 生成式 UI: LLM 是高效的 UI 生成器 |
| **机构** | Google Research |
| **arXiv** | [2604.09577](https://arxiv.org/abs/2604.09577) |

**发现**：适当提示和工具组合下，现代 LLM 可稳健生成高质量自定义 UI。83% 情况下用户偏好生成 UI 超过标准 markdown 输出。Gemini 3 实现的 Elo 分数最高（1706.7），错误率 0%。发布 PAGEN 数据集辅助评估。

---

### 10.6 Subgoal-driven Framework for Web Agents

| 属性 | 内容 |
|------|------|
| **标题** | A Subgoal-driven Framework for Improving Long-Horizon LLM Agents |
| **中文标题** | 子目标驱动的长时域 LLM 智能体改进框架 |
| **机构** | Google DeepMind |
| **arXiv** | [2603.19685](https://arxiv.org/abs/2603.19685) |

**方法**：子目标分解的在线规划和 MiRA（Milestoning RL Enhanced Agent）基于里程碑的密集奖励信号框架。Gemini 实时规划在 WebArena-Lite 上提升 ~10% 绝对成功率。Gemma3-12B + MiRA 从 6.4% 提升至 43.0%，超越 GPT-4-Turbo（17.6%）和 GPT-4o（13.9%）。

---

### 10.7 PhaseCoder: Spatial Audio for Multimodal LLMs

| 属性 | 内容 |
|------|------|
| **标题** | PhaseCoder: Microphone Geometry-Agnostic Spatial Audio Understanding for Multimodal LLMs |
| **中文标题** | PhaseCoder: 麦克风几何无关的空间音频理解 |
| **机构** | Google DeepMind |
| **arXiv** | [2601.21124](https://arxiv.org/abs/2601.21124) |

**方法**：仅 Transformer 的空间音频编码器，对麦克风几何形状无关。Gemma 3n 微调后可理解空间音频 token，实现从任意麦克风阵列的复杂空间推理和定向转录。

---

### 10.8 Topological Trouble With Transformers

| 属性 | 内容 |
|------|------|
| **标题** | The Topological Trouble With Transformers |
| **中文标题** | Transformer 的拓扑问题 |
| **机构** | Google DeepMind |
| **arXiv** | [2604.17121](https://arxiv.org/abs/2604.17121) |

**核心论点**：Transformer 的前馈架构从根本上限制了动态状态追踪。提出循环 Transformer 架构的分类法（按循环轴和每步输入 token 比），展望增强状态空间模型和粗粒度循环的方向。

---

## 11. 扩散模型与生成式 AI

### 11.1 RePlaid: Continuous Diffusion for Language

| 属性 | 内容 |
|------|------|
| **标题** | Continuous Diffusion Scales Competitively with Discrete Diffusion for Language |
| **中文标题** | 连续扩散在语言建模中与离散扩散竞争力相当 |
| **arXiv** | [2605.18530](https://arxiv.org/abs/2605.18530) |

**方法**：构建 RePlaid（连续扩散 LM），与离散扩散对齐架构后建立首个缩放律比较。连续模型在计算上仅落后自回归模型 20×（无嵌入训练时为 7×），在 OpenWebText 上达到 22.1 PPL，超越离散扩散 Duo 和 MDLM。理论发现 ELBO 目标自然恢复近似线性交叉熵，消除启发式时间重参数化。

---

### 11.2 Continuous Diffusion Rivals Discrete - LangFlow

| 属性 | 内容 |
|------|------|
| **标题** | LangFlow: Continuous diffusion rivals discrete in language modeling |
| **中文标题** | LangFlow: 连续扩散在语言建模中匹敌离散 |
| **arXiv** | [2604.11748](https://arxiv.org/abs/2604.11748) |

---

### 11.3 Flow Map Language Models (One-Step)

| 属性 | 内容 |
|------|------|
| **标题** | Flow Map Language Models: One-step language modeling via continuous denoising |
| **中文标题** | 流图语言模型：通过连续去噪的单步语言建模 |
| **arXiv** | [2602.16813](https://arxiv.org/abs/2602.16813) |

---

## 综合趋势分析

### 趋势 1: CTR/推荐系统全面转向 Transformer 架构
2025-2026 年，工业 CTR 预测经历从 DLRM 到 Transformer 的全面范式转换。LinkedIn (CADET)、Baidu (GRAB)、Alibaba (EST, HeMix)、ByteDance (HyFormer, MixFormer, TokenMixer-Large)、Tencent (RankUp)、Kuaishou (GR4AD)、Meta (Memento) 等均在生产环境中部署了 Transformer/生成式架构。核心创新方向包括：序列建模与特征交互的统一、循环计算缩放、多模态端到端训练、长周期历史建模、冷启动生成式建模。

### 趋势 2: LLM 对齐从「方法爆炸」进入「收敛分析」阶段
OXRL 的 51 种算法比较揭示关键洞见：损失函数变体贡献仅 ~1pp，规模贡献 ~50pp。DAR、GOPO、LambdaPO 等新方法在理论框架上更统一，从 Hilbert 空间投影、值梯度等视角重新理解对齐。

### 趋势 3: 多智能体 RL for LLM 成为新的活跃前沿
Dr. MAS、MetaAgent-X、Strat-Reasoner、Graph-GRPO、SPIRAL 等同时出现，GRPO 被广泛扩展到多智能体设置。核心挑战包括梯度方差管理（逐智能体归一化）、信用分配、长时域稳定性。

### 趋势 4: AI 智能体评估从「最终结果」转向「过程质量」
SpecBench、ProcCtrlBench、FeatureBench 等新基准关注奖励黑客、执行过程质量、复杂功能开发而非简单 bug 修复。VISTA 将视觉规格到 UI 的端到端生成纳入评估范围。

### 趋势 5: 智能体系统从「工具使用」走向「工具内化」
TInR、AgentMath、TRICE 等工作探索将工具知识内化到模型参数中，而非依赖推理时的外部工具文档。工具集成推理（TIR）成为模型能力扩展的标准范式。

### 趋势 6: Google DeepMind 在系统层和基础模型层全面发力
Gemini Embedding 2、Gemini for Google、Generative UI、Aletheia（数学研究智能体）、PhaseCoder（空间音频）展示 DeepMind 在多模态、企业应用、生成式 UI、科学研究、感知等领域的全面布局。

---

## 附录：arXiv 论文速查索引

| # | 论文 | Venue | arXiv | 类别 |
|---|------|-------|-------|------|
| 1 | Bi-NAC: Bilevel Natural Language Actor-Critic | ICML 2026 | 2605.24547 | LLM RL |
| 2 | R2-Write: Reflection & Revision | ICML 2026 | 2604.03004 | LLM 写作 |
| 3 | Vector Prompt Interfaces | ICML 2026 | 2603.04292 | LLM 定制化 |
| 4 | BigMac: Multimodal LLM Training | ICML 2026 | 2605.25451 | 系统 |
| 5 | GSPR: Generalizable Safety Policy Reasoner | ICLR 2026 | OpenReview | 安全 |
| 6 | NSPO: Null-Space Constrained Policy Optimization | ICLR 2026 | - | 对齐 |
| 7 | DAR: Dual-regularized Advantage Regression | ICLR 2026 | 2602.11523 | 对齐 |
| 8 | ReAlign: Safety-Aligning Reasoning Models | ICLR 2026 | OpenReview | 安全 |
| 9 | ARMOR: Meticulous Reasoning Safety | ICLR 2026 | OpenReview | 安全 |
| 10 | OXRL: Post-Training Comparison | - | 2603.19335 | 对齐分析 |
| 11 | CADET: Decoder-Only Ads CTR | LinkedIn | 2602.11410 | CTR |
| 12 | LoopCTR: Loop Scaling | - | 2604.19550 | CTR |
| 13 | GRAB: Generative CTR at Baidu | Baidu | 2602.01865 | CTR |
| 14 | EST: Efficient Scaling Laws | Alibaba | 2602.10811 | CTR |
| 15 | LLM-HYPER: Cold-Start CTR | US E-com | 2604.12096 | CTR |
| 16 | RankUp: High-Rank Representations | Tencent | 2604.17878 | CTR |
| 17 | HeMix: Scalable CTR | Alibaba | 2602.09387 | CTR |
| 18 | GR4AD: Generative Rec for Ads | Kuaishou | 2602.22732 | CTR |
| 19 | Memento: RAG Long-Retention | Meta | 2605.24051 | CTR |
| 20 | SIF: Sample Is Feature | ByteDance | 2604.15650 | CTR |
| 21 | DeepAgent: General Reasoning Agent | RUC | 2510.21618 | Agent |
| 22 | TRICE: Tool-Integrated Reasoning | - | 2605.06326 | Agent |
| 23 | HTAA: Hybrid Toolset Agentization | - | 2604.10917 | Agent |
| 24 | AgentMath: Tool-Augmented Math | - | 2512.20745 | Agent |
| 25 | TInR: Tool-Internalized Reasoning | - | 2604.10788 | Agent |
| 26 | BIGMAS: Brain-Inspired MAS | - | 2603.15371 | MAS |
| 27 | GraSP: Graph-Structured Skills | - | 2604.17870 | Agent |
| 28 | AgentFugue: Collective Reasoning | - | 2605.24486 | MAS |
| 29 | SPIRAL: Self-Play Reasoning | - | 2506.24119 | Game RL |
| 30 | Strat-Reasoner: Strategic Reasoning | - | 2605.04906 | Game RL |
| 31 | Dr. MAS: Stable Multi-Agent RL | - | 2602.08847 | MAS |
| 32 | MetaAgent-X: End-to-End MAS | - | 2605.14212 | MAS |
| 33 | Graph-GRPO: Topology Learning | - | 2603.02701 | MAS |
| 34 | OMAD: Online Diffusion Policy | - | 2602.18291 | MARL |
| 35 | Efficient Exploration (DeepMind) | DeepMind | 2603.17378 | RLHF |
| 36 | Gemini Embedding 2 | DeepMind | 2605.27295 | 多模态 |
| 37 | Gemini for Google | DeepMind | 2605.16517 | 企业 SE |
| 38 | Generative UI | Google | 2604.09577 | UI Gen |
| 39 | Aletheia: Math Research Agent | DeepMind | 2602.21201 | 科学研究 |
| 40 | SpecBench: Reward Hacking | - | 2605.21384 | 代码 |
| 41 | FeatureBench: Complex Feature Dev | - | 2602.10975 | 代码 |
| 42 | FOREAGENT: Predict-Then-Verify | - | 2601.05930 | 代码 |
| 43 | RePlaid: Continuous Diffusion LM | - | 2605.18530 | 生成模型 |
| 44 | MaR: Metacognition as Reward | - | 2605.23384 | LLM RL |
| 45 | LambdaPO: Lambda Policy Optimization | - | 2605.19416 | 对齐 |
| 46 | Value-Gradient Hypothesis | - | 2605.21654 | 理论 |
| 47 | Topological Trouble With Transformers | DeepMind | 2604.17121 | 架构 |
