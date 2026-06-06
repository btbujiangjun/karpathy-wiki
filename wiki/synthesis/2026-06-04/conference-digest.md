---
title: 顶会论文专题报告 — 2026年6月全面版（ICML / AAAI / NeurIPS / ICLR / KDD / CVPR / ACL / EMNLP / SIGIR / WWW / CIKM / RecSys）
type: synthesis
created: 2026-06-04
updated: 2026-06-04
sources: [arXiv, ICML 2026, ICLR 2026, NeurIPS 2025, AAAI 2026, CVPR 2026, KDD 2026, WWW 2026, SIGIR 2026, CIKM 2025, RecSys 2025, ACL 2025, EMNLP 2025]
tags: [conference-digest, icml-2026, iclr-2026, neurips-2025, aaai-2026, cvpr-2026, kdd-2026, www-2026, sigir-2026, cikm-2025, recsys-2025, acl-2025, emnlp-2025, ctr, recommendation, agent, llm, systems, code-generation, multi-agent, generative-ai, diffusion]
---

# 顶会论文专题报告 — 2026年6月全面版

> 覆盖 ICML 2026、AAAI 2026、NeurIPS 2025、ICLR 2026、KDD 2026、CVPR 2026、ACL/EMNLP 2025、SIGIR 2026、WWW 2026、CIKM 2025、RecSys 2025 等 12+ 会议的最新接收论文。聚焦 LLM 训练理论、推荐系统/CTR 预测、智能体系统、对齐与安全、游戏与多智能体 RL、代码生成、多模态与生成模型、CV/3D 生成、大规模系统和工程优化。

---

## 目录

1. [ICML 2026 论文精选](#1-icml-2026-论文精选)
2. [ICLR 2026 论文精选](#2-iclr-2026-论文精选)
3. [NeurIPS 2025 论文精选（Best Papers）](#3-neurips-2025-论文精选best-papers)
4. [AAAI 2026 / CVPR 2026 论文精选](#4-aaai-2026--cvpr-2026-论文精选)
5. [KDD 2026 论文精选](#5-kdd-2026-论文精选)
6. [ACL / EMNLP 2025 论文精选](#6-acl--emnlp-2025-论文精选)
7. [SIGIR 2026 推荐系统论文精选](#7-sigir-2026-推荐系统论文精选)
8. [WWW 2026 推荐系统论文精选](#8-www-2026-推荐系统论文精选)
9. [CIKM 2025 论文精选](#9-cikm-2025-论文精选)
10. [RecSys 2025 论文精选](#10-recsys-2025-论文精选)
11. [各大实验室最新成果](#11-各大实验室最新成果)
12. [智能体系统与代码生成](#12-智能体系统与代码生成)
13. [LLM 训练理论、Scaling Law 与对齐](#13-llm-训练理论scaling-law-与对齐)
14. [多模态与生成模型](#14-多模态与生成模型)

---

## 1. ICML 2026 论文精选

> ICML 2026 将于 2026年7月6-11日在韩国首尔举行。本届收到 23,918 篇投稿，录用 6,352 篇（接受率 26.6%），较 ICML 2025 翻倍。

### 1.1 Shannon Scaling Law: LLMs as Noisy Channels

| 属性 | 内容 |
|------|------|
| **标题** | Shannon Scaling Law: LLMs as Noisy Channels |
| **中文标题** | 香农缩放定律：将 LLM 视为噪声信道 |
| **Venue** | ICML 2026 |
| **arXiv** | 2605.23901 |

**核心创新**：将 LLM 的行为解释为带噪声的信息传输信道，借用香农信息论中的信道容量概念来推导预训练损失的理论下界。推导出训练损失随数据量和模型参数的双指数衰减规律，在多个 LLaMA/OLMo 系列模型上验证了该理论与经验数据的高度拟合。

### 1.2 M+Adam: Low-Precision Training via Mantissa–Exponent Optimization

| 属性 | 内容 |
|------|------|
| **标题** | M+Adam: Low-Precision Training via Mantissa–Exponent Optimization |
| **中文标题** | M+Adam: 基于尾数-指数优化的低精度训练 |
| **机构** | Aarhus University 等 |
| **Venue** | ICML 2026 |
| **链接** | opt-ml.org/papers/2025/paper141.pdf |

**核心创新**：提出新的低精度训练优化器，将浮点数的尾数（mantissa）和指数（exponent）分开处理以在有限精度下最大化信息保存。在多种规模和任务上验证了 FP8/FP4 训练的有效性，大幅降低了训练显存消耗。

### 1.3 How Does the Lagrangian Guide Safe RL through Diffusion?

| 属性 | 内容 |
|------|------|
| **标题** | How Does the Lagrangian Guide Safe Reinforcement Learning through Diffusion Models? |
| **中文标题** | 拉格朗日方法如何引导安全强化学习通过扩散模型？ |
| **机构** | UCL |
| **Venue** | ICML 2026 |

**核心创新**：将拉格朗日松弛（Lagrangian relaxation）与扩散模型结合来解决安全强化学习中的约束满足问题。在多个安全 Gym 环境中验证，比传统 Safe RL 方法在成本约束违反率上降低 30-50%。

### 1.4 Revenue Efficiency of Correlated Equilibria in First Price Auctions (Spotlight)

| 属性 | 内容 |
|------|------|
| **标题** | Revenue Efficiency of Correlated Equilibria in First Price Auctions |
| **中文标题** | 第一价格拍卖中关联均衡的收入效率 |
| **机构** | Aarhus University |
| **Venue** | ICML 2026 (Spotlight) |

**核心创新**：理论分析第一价格拍卖中关联均衡（correlated equilibria）的收入效率。证明拍卖方可以通过设计信息结构来影响投标人之间的关联程度，从而最大化预期收入。对广告拍卖机制设计有直接指导意义。

### 1.5 Self-Supervised Flow Matching (Self-Flow)

| 属性 | 内容 |
|------|------|
| **标题** | Self-Supervised Flow Matching |
| **中文标题** | 自监督流匹配 |
| **Venue** | ICML 2026 |

**核心创新**：提出无需配对数据的流匹配训练方法，利用数据流形的几何结构自动构建从简单先验到数据分布的传输路径。在图像生成任务上接近监督 Flow Matching 质量，大幅扩展了流匹配的应用场景。

### 1.6 UniAR: Unified Multimodal Autoregressive Modeling

| 属性 | 内容 |
|------|------|
| **标题** | UniAR: Unified Multimodal Autoregressive Modeling |
| **中文标题** | UniAR：统一多模态自回归建模 |
| **机构** | Alibaba |
| **Venue** | ICML 2026 |

**核心创新**：将图像、视频、文本、音频等多模态数据统一编码为自回归 token 序列，使用单一 Transformer 架构进行端到端训练。在跨模态理解、生成和转换任务上达到或超越专用模型性能。

### 1.7 ALIVE: Interactive Frontend Games via RL

| 属性 | 内容 |
|------|------|
| **标题** | ALIVE: Interactive Frontend Games via RL |
| **中文标题** | ALIVE：基于强化学习的交互式前端游戏 |
| **机构** | Alibaba |
| **Venue** | ICML 2026 |

**核心创新**：使用强化学习训练智能体直接从 HTML/CSS/JavaScript 生成可交互的前端游戏。结合代码生成和 RL 微调，生成的游戏在可玩性和交互质量上显著优于基座模型。

### 1.8 The Optimal Sample Complexity of Linear Contracts

| 属性 | 内容 |
|------|------|
| **标题** | The Optimal Sample Complexity of Linear Contracts |
| **中文标题** | 线性契约的最优样本复杂度 |
| **机构** | Aarhus University |
| **Venue** | ICML 2026 |
| **arXiv** | 2601.01496 |

**核心创新**：理论刻画了在线性契约（线性激励合约）学习中达到 ε-最优所需的最少样本量，证明了该样本复杂度的信息论下界并给出了可匹配的算法。

---

## 2. ICLR 2026 论文精选

> ICLR 2026 于 2026年4月23-27日在巴西里约热内卢举行。本届收到 19,809 篇投稿，录用 5,343 篇（接受率 26.97%），其中 Oral 论文 223 篇（1.13%）。

### 2.1 Mamba-3: Improved Sequence Modeling using State Space Principles (Oral)

| 属性 | 内容 |
|------|------|
| **标题** | Mamba-3: Improved Sequence Modeling using State Space Principles |
| **中文标题** | Mamba-3：基于状态空间原则的改进序列建模 |
| **机构** | 包含 Zico Kolter、Tri Dao、Albert Gu 等 |
| **Venue** | ICLR 2026 (Oral) |

**核心创新**：从推理优先（inference-first）视角出发，基于状态空间模型视角对线性模型进行三项核心改进：1) 更具表达力的循环结构；2) 复数状态更新规则以实现更丰富的状态追踪；3) 多输入多输出（MIMO）形式化以更好利用硬件并行性。在检索、状态追踪和语言建模任务上建立性能-推理预算的帕累托前沿。

### 2.2 Transformers are Inherently Succinct (Outstanding Paper)

| 属性 | 内容 |
|------|------|
| **标题** | Transformers are Inherently Succinct |
| **中文标题** | Transformer 本质上是简洁的 |
| **Venue** | ICLR 2026 (Outstanding Paper) |

**核心创新**：理论证明了 Transformer 在表示某些函数类时比深度神经网络或循环神经网络在参数效率上具有本质优势。该结果为 Transformer 在 LLM 中的主导地位提供了理论佐证。

### 2.3 Common Corpus: The Largest Collection of Ethical Data for LLM Pre-Training (Oral)

| 属性 | 内容 |
|------|------|
| **标题** | Common Corpus: The Largest Collection of Ethical Data for LLM Pre-Training |
| **中文标题** | Common Corpus：最大的 LLM 预训练伦理数据集 |
| **Venue** | ICLR 2026 (Oral) |

**核心创新**：发布了迄今为止最大的合乎伦理要求的数据集，专注于版权合规、来源透明和许可友好。为开源 LLM 社区提供了高质量训练数据替代方案。

### 2.4 Why DPO is a Misspecified Estimator and How to Fix It (Oral)

| 属性 | 内容 |
|------|------|
| **标题** | Why DPO is a Misspecified Estimator and How to Fix It |
| **中文标题** | 为什么 DPO 是错误指定的估计器以及如何修复 |
| **Venue** | ICLR 2026 (Oral) |

**核心创新**：理论分析了直接偏好优化（DPO）在偏好学习中的偏差来源——DPO 假设偏好概率是 Bradley-Terry 模型的严格形式，但实际偏好数据往往不符合该假设。提出修正方法在多个对齐基准上显著提升性能。

### 2.5 SafeDPO: Direct Preference Optimization with Enhanced Safety (Oral)

| 属性 | 内容 |
|------|------|
| **标题** | SafeDPO: A Simple Approach to Direct Preference Optimization with Enhanced Safety |
| **中文标题** | SafeDPO：增强安全性的简单直接偏好优化方法 |
| **Venue** | ICLR 2026 (Oral) |

**核心创新**：在 DPO 训练中显式加入安全约束偏好对，在不降低通用能力的前提下显著提升模型安全性。在有害 prompt 拒绝率上提升 15-20%。

### 2.6 Gated Attention for LLMs (NeurIPS 2025 Best Paper, also at ICLR)

参见 NeurIPS 2025 Best Paper 部分。

### 2.7 Apple at ICLR 2026 精选论文

| 属性 | 内容 |
|------|------|
| **机构** | Apple |

Apple 在 ICLR 2026 展示了多项研究：

1. **AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking** — 通过强化抽象思维来增强 LLM 推理能力（作者: Silin Gao, Antoine Bosselut, Samy Bengio, Emmanuel Abbe）
2. **Trained on Tokens, Calibrated on Concepts: The Emergence of Semantic Calibration in LLMs** — 研究发现 LLM 在 token 上训练但会涌现出对概念层面的校准能力（作者: Preetum Nakkiran, Arwen Bradley 等）
3. **VLSU: Mapping the Limits of Joint Multimodal Understanding for AI Safety** — 多模态理解边界的系统映射

---

## 3. NeurIPS 2025 论文精选（Best Papers）

> NeurIPS 2025 于 2025年11月30日-12月5日在圣地亚哥举行。公布 7 项大奖：4 Best Papers + 3 Runners-Up。

### 3.1 Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free (Best Paper)

| 属性 | 内容 |
|------|------|
| **标题** | Gated Attention for LLMs |
| **中文标题** | 门控注意力：非线性、稀疏性与消除注意力汇 |
| **作者** | Zihan Qiu 等 |
| **Venue** | NeurIPS 2025 Best Paper |
| **机构** | 该设计现已用于 Qwen3-Next 模型 |

**核心创新**：在 SDPA（softmax dot-product attention）之后引入简单的 head-specific sigmoid 门控机制。与数十种门控注意力变体在 15B MoE 和 1.7B dense 模型上对比，发现简单的单门控设计一致性最优。效果包括：稳定训练、减少 attention sink、提升长上下文性能。

**实验结果**：在多种规模的 LLM 训练中，Gated Attention 相比标准注意力在长上下文任务上提升 5-10%，在训练稳定性上有显著改善。

### 3.2 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities (Best Paper)

| 属性 | 内容 |
|------|------|
| **标题** | 1000 Layer Networks for Self-Supervised RL |
| **中文标题** | 千层网络用于自监督强化学习 |
| **作者** | Kevin Wang 等 |
| **Venue** | NeurIPS 2025 Best Paper |

**核心创新**：挑战了"RL 不兼容极深网络"的传统认知。使用对比学习、目标条件化自监督方法，证明深度从数十层扩展到 1024 层时，强化学习智能体的目标达成能力涌现性地提升。在模拟机器人任务中，深层网络展现出更丰富的涌现行为和更高的成功率。

### 3.3 Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training (Best Paper)

| 属性 | 内容 |
|------|------|
| **标题** | Why Diffusion Models Don't Memorize |
| **中文标题** | 扩散模型为何不会记忆——隐式动力正则化的作用 |
| **Venue** | NeurIPS 2025 Best Paper |

**核心创新**：从动力系统角度解释了扩散模型相比 GAN/VAE 更不容易记忆训练数据的根本原因——扩散模型的连续时间前向-反向过程天然具有正则化效应，阻止了模型对单个训练样本的过拟合。提供了理论分析和实验验证。

### 3.4 Artificial Hivemind: Open-Ended Homogeneity of Language Models (Best Paper, D&B Track)

| 属性 | 内容 |
|------|------|
| **标题** | Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond) |
| **中文标题** | 人工蜂群思维：语言模型的开放同质性 |
| **作者** | Liwei Jiang 等 |
| **Venue** | NeurIPS 2025 Best Paper (Datasets & Benchmarks) |

**核心创新**：提出 Infinity-Chat 基准（26,000 个开放结束查询 + 密集人工标注），大规模分析 LLM 生成的多样性和"人工蜂群思维"效应。发现模型内高度重复（同一模型多次生成相似内容）和模型间高度同质化（不同模型生成类似内容）的双重问题，引发了对长期创造力和价值多元化的担忧。

---

## 4. AAAI 2026 / CVPR 2026 论文精选

### 4.1 AAAI 2026

> AAAI 2026 于 2026年1月20-27日在新加坡举行。AAAI 是 CCF-A 类人工智能综合会议。

**关联虚拟现实与多模态**：AAAI 2026 收录了大量多模态学习、知识图谱推理和强化学习相关工作。重点包括大语言模型的知识编辑、多模态融合、因果推理等方向。

### 4.2 CVPR 2026

> CVPR 2026 将于 2026年6月3-7日在美国丹佛举行。本届收到 16,092 篇投稿，录用 4,090 篇（接受率 25.42%），含 141 篇 Oral 论文。

#### WorldLens: Full-Spectrum Evaluations of Driving World Models in Real World (Oral)

| 属性 | 内容 |
|------|------|
| **标题** | WorldLens: Full-Spectrum Evaluations of Driving World Models |
| **中文标题** | WorldLens：驾驶世界模型的全光谱评估 |
| **机构** | MMLab@NTU 等 |
| **Venue** | CVPR 2026 Oral |
| **arXiv** | 2512.10958 |

**核心创新**：提出首个全面的驾驶世界模型评估框架，覆盖感知、预测、规划全链条。在多个真实驾驶数据集上系统评估了现有世界模型的优缺点。

#### LLSA: Trainable Log-linear Sparse Attention for Efficient Diffusion Transformers (Highlight)

| 属性 | 内容 |
|------|------|
| **标题** | Trainable Log-linear Sparse Attention for Efficient Diffusion Transformers |
| **中文标题** | 可训练的对数线性稀疏注意力用于高效扩散 Transformer |
| **机构** | MMLab@NTU 等 |
| **Venue** | CVPR 2026 Highlight |
| **arXiv** | 2512.16615 |

**核心创新**：提出可训练的对数线性复杂度稀疏注意力机制，专为扩散 Transformer（DiT）设计。将标准注意力的 O(N²) 复杂度降低到 O(N log N)，在保持生成质量的同时显著提升了扩散模型的训练和推理速度。

#### MatAnyone2: Scaling Video Matting via a Learned Quality Evaluator (Highlight)

| 属性 | 内容 |
|------|------|
| **标题** | MatAnyone2: Scaling Video Matting |
| **中文标题** | MatAnyone2：通过学习质量评估器扩展视频抠图 |
| **机构** | MMLab@NTU |
| **Venue** | CVPR 2026 Highlight |
| **arXiv** | 2512.11782 |

**核心创新**：通过学习一个质量评估器来引导视频抠图模型的训练和推理，实现了高分辨率、长视频的高质量抠图效果。

#### OmniVGGT: Omni-Modality Driven Visual Geometry Grounded Transformer (Highlight)

| 属性 | 内容 |
|------|------|
| **标题** | OmniVGGT: Omni-Modality Driven Visual Geometry Grounded Transformer |
| **中文标题** | OmniVGGT：全模态驱动的视觉几何 Transformer |
| **机构** | MMLab@NTU |
| **Venue** | CVPR 2026 Highlight |
| **arXiv** | 2511.10560 |

**核心创新**：提出全模态（RGB、深度、法线、点云等）驱动的视觉几何 Transformer，在 3D 重建和场景理解任务上实现 SOTA。

#### PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image

| 属性 | 内容 |
|------|------|
| **标题** | PhysX-Anything |
| **中文标题** | PhysX-Anything：从单张图像生成可模拟的物理 3D 资产 |
| **机构** | MMLab@NTU |
| **Venue** | CVPR 2026 |

**核心创新**：从单张 RGB 图像生成可直接用于物理模拟的 3D 资产（含材质、刚体属性、碰撞体等），打通了 3D 生成到仿真部署的断点。

---

## 5. KDD 2026 论文精选

> KDD 2026 将于 2026年8月9-13日在韩国济州岛举行。

### 5.1 RankElastor: Effective-Rank Dynamics for Recommendation

| 属性 | 内容 |
|------|------|
| **标题** | RankElastor: Effective-Rank Dynamics for Recommendation |
| **中文标题** | RankElastor：推荐系统的有效秩动力学 |
| **Venue** | KDD 2026 |
| **arXiv** | 2605.23191 |

**核心创新**：提出有效秩（effective rank）概念作为衡量推荐模型表示能力的指标，并据此设计动态调整模型容量的机制。在大规模推荐场景中，动态秩调整的模型在保持相同计算预算下 AUC 提升 0.5-1%。

### 5.2 RankUp: High-rank Representations for Ad Ranking

| 属性 | 内容 |
|------|------|
| **标题** | RankUp: High-rank Representations for Ad Ranking |
| **中文标题** | RankUp：用于广告排序的高秩表示 |
| **机构** | Tencent |
| **Venue** | KDD 2026 |
| **arXiv** | 2604.17878 |

**核心创新**：通过分解和重组合阶高秩表示来提升广告排序模型的表示能力。在腾讯广告平台上实现了显著的 CTR 和 CPM 提升。

---

## 6. ACL / EMNLP 2025 论文精选

### 6.1 ACL 2025

> ACL 2025 于 2025年7月27日-8月1日在奥地利维也纳举行。

**CodeTree: Agent-guided Tree Search for Code Generation**

| 属性 | 内容 |
|------|------|
| **标题** | CodeTree: Agent-guided Tree Search Code Generation |
| **中文标题** | CodeTree：智能体引导的树搜索代码生成 |
| **机构** | Salesforce |
| **Venue** | ACL 2025 |

**核心创新**：结合多智能体协作与树搜索策略进行代码生成。多个智能体分别负责代码生成、测试、调试和优化，通过树搜索探索不同的生成路径。

**Tree-of-Evolution: Tree-Structured Code Instruction Evolution**

| 属性 | 内容 |
|------|------|
| **标题** | Tree-of-Evolution: Tree-Structured Code Instruction Evolution |
| **中文标题** | Tree-of-Evolution：树结构代码指令进化 |
| **机构** | NUS |
| **Venue** | ACL 2025 |

**核心创新**：使用进化算法树状结构生成多样化的代码指令数据，显著提升了代码 LLM 的训练数据质量和多样性。

### 6.2 EMNLP 2025

> EMNLP 2025 于 2025年11月4-9日在中国苏州举行。Main Track 收到 8,174 篇投稿，录用 1,811 篇（22.16%），Findings 录用 1,418 篇（17.35%）。

**RRInf: Efficient Influence Function Estimation via Ridge Regression for LLMs and Diffusion Models**

| 属性 | 内容 |
|------|------|
| **标题** | RRInf: Efficient Influence Function Estimation via Ridge Regression |
| **中文标题** | RRInf：基于岭回归的高效影响函数估计 |
| **机构** | A*STAR CFAR |
| **Venue** | EMNLP 2025 |

**核心创新**：将影响函数估计问题重新形式化为岭回归，从而实现了在 LLM 和扩散模型上的高效影响函数计算。可用于训练数据归因、数据清理和模型调试。

**Agent Trading Arena: A Study on Numerical Understanding in LLM-Based Agents**

| 属性 | 内容 |
|------|------|
| **标题** | Agent Trading Arena: Numerical Understanding in LLM-Based Agents |
| **中文标题** | Agent 交易竞技场：基于 LLM 智能体的数值理解研究 |
| **机构** | A*STAR CFAR |
| **Venue** | EMNLP 2025 |
| **arXiv** | 2502.17967 |

**核心创新**：构建竞争性多智能体股票市场模拟环境，研究发现结合图表可视化和反思模块能显著提升 LLM 智能体的数值推理和交易性能，特别是在高波动市场条件下。

---

## 7. SIGIR 2026 推荐系统论文精选

> SIGIR 2026 将于 2026年7月20-24日在澳大利亚墨尔本举行。主研究轨道收到 1,271 篇投稿，录用 234 篇（18.41%）。据知乎专栏统计，约 90 篇推荐系统相关 Full Papers。

### 7.1 LLM 推荐方向

**HUM: Heterogeneous User Modeling for LLM-based Recommendation**

| 属性 | 内容 |
|------|------|
| **标题** | Heterogeneous User Modeling for LLM-based Recommendation |
| **中文标题** | 基于 LLM 推荐的异构用户建模 |
| **机构** | NUS / USTC |
| **Venue** | SIGIR 2026 |

**核心创新**：提出包含压缩增强器（compression enhancer）和鲁棒性增强器（robustness enhancer）的异构用户建模方法。压缩增强器通过定制 prompt 将异构行为压缩为定制 token；鲁棒性增强器引入领域重要性分数来缓解领域跷跷板现象。

**LLM-RecG: Semantic Bias-Aware Framework for Zero-Shot Sequential Recommendation**

| 属性 | 内容 |
|------|------|
| **标题** | LLM-RecG: Semantic Bias-Aware Framework for Zero-Shot Sequential Recommendation |
| **中文标题** | LLM-RecG：语义偏差感知的零样本序列推荐框架 |
| **机构** | UIUC |
| **Venue** | SIGIR 2026 |

**核心创新**：解决跨域零样本推荐中的域语义偏差问题。在 item 级别引入泛化损失来对齐跨域嵌入，在序列级别通过聚类源域用户序列迁移行为模式。

### 7.2 生成式推荐方向

**GRACE: Generative Recommendation via Journey-Aware Sparse Attention on CoT Tokenization**

| 属性 | 内容 |
|------|------|
| **标题** | GRACE: Generative Recommendation via Journey-Aware Sparse Attention |
| **中文标题** | GRACE：基于旅程感知稀疏注意力的生成式推荐 |
| **机构** | Walmart Global Tech |
| **Venue** | SIGIR 2026 |

**核心创新**：提出混合 Chain-of-Thought tokenization 方法，将知识图谱属性编码到 token 中。设计 Journey-Aware Sparse Attention (JSA) 机制，选择性关注压缩后上下文段。在 Home 域 HR@10 提升 106.9%，NDCG@10 提升 106.7%。

**GenSAR: Unifying Balanced Search and Recommendation with Generative Retrieval**

| 属性 | 内容 |
|------|------|
| **标题** | GenSAR: Unifying Balanced Search and Recommendation |
| **中文标题** | GenSAR：通过生成式检索统一平衡搜索与推荐 |
| **机构** | Renmin University / Kuaishou |
| **Venue** | SIGIR 2026 |

**核心创新**：利用生成式检索（generative retrieval）统一搜索和推荐。为每个 item 分配多个 identifier 以同时捕获语义和协同信息，将 S&R 都形式化为 sequence-to-sequence 任务。

### 7.3 CTR/排序方向

**LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders**

| 属性 | 内容 |
|------|------|
| **标题** | LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders |
| **中文标题** | LONGER：工业推荐中的长序列建模扩展 |
| **机构** | ByteDance |
| **Venue** | SIGIR 2026 (also RecSys 2025) |

**核心创新**：长序列 Transformer 工业推荐系统。包含 global token 机制稳定注意力、InnerTransformer 轻量 token merge、混合精度训练和 KV cache serving 等工程优化。已在 ByteDance 10+ 场景全面部署。

**Revisiting Text Ranking in Deep Research**

| 属性 | 内容 |
|------|------|
| **标题** | Revisiting Text Ranking in Deep Research |
| **中文标题** | 重新审视深度研究中的文本排序 |
| **机构** | CMU / Microsoft |
| **Venue** | SIGIR 2026 |
| **arXiv** | 2602.21456 |

**核心创新**：系统复现和评估了 2 种 deep research agent + 5 种检索器 + 3 种重排序器的组合，在深度研究场景下的文本排序效果。揭示了不同组件组合的性能特征。

---

## 8. WWW 2026 推荐系统论文精选

> WWW 2026（The Web Conference）原定于 2026年4月在迪拜举行，后推迟。尽管如此，论文列表已公布。

**ThinkRec: Thinking-based LLM Recommendation**

| 属性 | 内容 |
|------|------|
| **标题** | ThinkRec: Thinking-based LLM Recommendation |
| **中文标题** | ThinkRec：基于思考的 LLM 推荐 |
| **Venue** | WWW 2026 |

**核心创新**：在推荐过程中引入"思考"（Chain-of-Thought-like）过程，让 LLM 在生成推荐前先推理用户偏好和物品匹配度。相比直接推荐，思考式推荐在准确性和可解释性上均有提升。

**GenCI: Generative CTR via Cohort Intent Learning**

| 属性 | 内容 |
|------|------|
| **标题** | GenCI: Generative CTR via Cohort Intent Learning |
| **中文标题** | GenCI：通过群体意图学习的生成式 CTR |
| **Venue** | WWW 2026 |
| **arXiv** | 2601.18251 |

**核心创新**：将 CTR 预测重新形式化为生成式任务，通过群体意图（cohort intent）学习来捕获用户的集体行为模式。在多个工业数据集上优于传统判别式 CTR 模型。

---

## 9. CIKM 2025 论文精选

> CIKM 2025 于 2025年11月10-14日在韩国首尔举行。收到 2,890 篇投稿（含 1,627 篇 full papers），录用 862 篇。1,436 人现场参会，来自 46 个国家。

**RankMixer: Scaling Up Ranking Models in Industrial Recommenders**

| 属性 | 内容 |
|------|------|
| **标题** | RankMixer: Scaling Up Ranking Models in Industrial Recommenders |
| **中文标题** | RankMixer：工业推荐中排序模型的规模化扩展 |
| **机构** | ByteDance |
| **Venue** | CIKM 2025 |
| **arXiv** | 2507.15551 |

**核心创新**：硬件感知的 token mixing 设计。用 per-token 参数化 FFN + HeadMixing 替代注意力机制。ByteDance token-based 推荐系列的基础工作。

**Lasso: LLM-based User Simulator for Cross-Domain Recommendation**

| 属性 | 内容 |
|------|------|
| **标题** | Lasso: LLM-based User Simulator for Cross-Domain Recommendation |
| **中文标题** | Lasso：基于 LLM 的跨域推荐用户模拟器 |
| **机构** | Sichuan University / Kuaishou |
| **Venue** | CIKM 2025（also RecSys 2025） |

**核心创新**：使用 LLM 作为用户模拟器来生成跨域用户行为。提出 Personalized Candidate Pool (PCP) 和 Confidence-Guided Inference (CGI) 模块提升效率和准确性。

---

## 10. RecSys 2025 论文精选

> RecSys 2025 于 2025年9月22-26日在捷克布拉格举行。

### 10.1 核心推荐模型

**Beyond Immediate Click: Engagement-Aware MoE-Enhanced Transformers (Prime Video)**

| 属性 | 内容 |
|------|------|
| **标题** | Beyond Immediate Click: Engagement-Aware MoE-Enhanced Transformers |
| **中文标题** | 超越即时点击：参与度感知的 MoE 增强 Transformer |
| **机构** | Amazon Prime Video |
| **Venue** | RecSys 2025 |

**核心创新**：在序列推荐中引入：1) temporal Mixture-of-Experts；2) personalized hard-negative sampling (PHNS)；3) engagement-aware multi-task learning (CTR + ranking + completion rate)；4) next-K training with soft labels。在 Prime Video 百万级用户数据上 NDCG@1 提升 3.52%。

**LEAF: Lightweight, Efficient, Adaptive and Flexible Embedding**

| 属性 | 内容 |
|------|------|
| **标题** | LEAF: Lightweight, Efficient, Adaptive and Flexible Embedding |
| **中文标题** | LEAF：轻量、高效、自适应、灵活的 Embedding |
| **机构** | USC |
| **Venue** | RecSys 2025 |

**核心创新**：多级哈希框架压缩大规模 Embedding 表。利用流式算法在线估计访问分布，多哈希函数最小化碰撞率。在 Criteo Kaggle 等四个数据集上 AUC 提升 1.2-2.8%。

**SUAN: Stacked Unified Attention Network (CTR Scaling Laws)**

| 属性 | 内容 |
|------|------|
| **标题** | SUAN: Stacked Unified Attention Network (CTR Scaling Laws) |
| **中文标题** | SUAN：堆叠统一注意力网络（CTR 缩放定律探索） |
| **机构** | Meituan |
| **Venue** | RecSys 2025 |
| **arXiv** | 2508.15326 |

**核心创新**：提出 CTR 模型在模型等级和数据量上的缩放定律。SUAN 使用统一注意力块（UAB）同时编码序列和非序列特征。蒸馏版 LightSUAN 在线 CTR 提升 2.81%，CPM 提升 1.69%。

### 10.2 用户行为与公平性

**Measuring Interaction-Level Unlearning Difficulty for Collaborative Filtering**

| 属性 | 内容 |
|------|------|
| **标题** | Measuring Interaction-Level Unlearning Difficulty for CF |
| **中文标题** | 协同过滤中交互级遗忘难度衡量 |
| **机构** | Taiyuan University of Technology / Shandong University |
| **Venue** | RecSys 2025 |

**核心创新**：首次从交互级别衡量推荐系统中的"被遗忘"难度。提出了评估每条交互对模型影响程度的方法，为推荐系统的数据删除合规提供理论基础。

---

## 11. 各大实验室最新成果

### 11.1 ByteDance

ByteDance 在推荐系统和 LLM 领域持续高产：

- **LONGER**（RecSys 2025 / SIGIR 2026）：超长用户行为序列建模，10+ 场景部署
- **TokenMixer-Large**（arXiv 2026）：7B 在线 / 15B 离线参数，MoE 设计，EC GMV +2.98%，AD SS +2.0%
- **HyFormer**（arXiv 2026）：改进 OneTrans 的 `[SEP]` token 设计，提出 query-decoding 机制
- **OneTrans**（WWW 2025）：统一特征交互 + 序列建模，GMV +5.68%
- **Zenith**（arXiv 2601.21285）：十亿级直播排序系统
- **Precise**：SDE-Consistent Sampling for Flow-Matching RL

### 11.2 Meta AI

- **AdLlama**：LLM for call-to-action text，CTR 提升 6.7%
- **Foundation-Expert Paradigm**：CTR 领域的基础模型-专家范式
- **ULTRA-HSTU**：Bending Scaling Law Curve 的生成式推荐架构
- **InterFormer**：异构交互学习
- **Peak-End Retention (Reels)**：基于心理学的长期留存优化
- **LLaTTE**：多阶段广告推荐缩放定律

### 11.3 Microsoft Research

- **SkillOpt**（2605.23904）：智能体技能自进化框架，零部署推理开销
- **Inductive Deductive Synthesis**：与 UC Berkeley 合作的验证系统自动合成
- **Revisiting Text Ranking in Deep Research**（SIGIR 2026）：深度研究中的文本排序

### 11.4 Google DeepMind

DeepMind 继续在 RL 理论、基础模型和 AI for Science 方向输出高水平工作。ICML 2026 有大量理论贡献，包括博弈论、优化和强化学习方向。

### 11.5 Apple

ICLR 2026 参展多项研究（参见 ICLR 章节）。

### 11.6 Alibaba

- **SORT**（arXiv 2603.03988）：系统优化排序 Transformer
- **EST**（arXiv 2602.10811）：CTR 高效缩放定律
- **FAT**（arXiv 2511.12081）：Rademacher CTR 缩放定律
- **UniAR**（ICML 2026）：统一多模态自回归建模
- **MUSE**（arXiv 2512.07216）：10 万长度终身用户兴趣建模

### 11.7 Kuaishou

- **CDUM**（RecSys 2025）：粗到细动态提升建模框架
- **LSVCR**（RecSys 2025）：LLM 增强序列推荐
- **UNiMixer**（arXiv 2604.00590）：统一架构缩放定律
- **GenSAR**（SIGIR 2026）：统一搜索与推荐的生成式检索

### 11.8 Tencent

- **RankUp**（KDD 2026）：广告排序高秩表示
- **TokenFormer**（arXiv 2604.13737）：统一多字段和序列推荐
- **GE4Rec**（arXiv 2512.14041）：生成式 CTR 范式

### 11.9 Meituan

- **SUAN**（RecSys 2025）：CTR 缩放定律方法论
- **MTFM**（arXiv 2602.11235）：无对齐基础模型
- **SparseCTR**（WWW 2026）：稀疏注意力长期 CTR
- **DOS**（arXiv 2602.04460）：双流正交语义 ID

### 11.10 Netflix / LinkedIn / Other

- **Netflix**: Scaling Generative Recommenders（arXiv 2605.23312）
- **Pinterest**: UniPinRec（统一检索+排序）
- **LinkedIn**: LiRank, CADET, LLM Retrieval for Ads
- **Walmart**: GRACE（SIGIR 2026 生成式推荐）
- **Airbnb**: LLM-Powered Synthetic Data for NL Search

---

## 12. 智能体系统与代码生成

### 12.1 智能体技能与优化

**SkillOpt: Executive Strategy for Self-Evolving Agent Skills** (Microsoft Research Asia)

| 属性 | 内容 |
|------|------|
| **标题** | SkillOpt: Executive Strategy for Self-Evolving Agent Skills |
| **中文标题** | SkillOpt：自进化智能体技能的执行策略 |
| **arXiv** | 2605.23904 |
| **GitHub** | github.com/microsoft/SkillOpt（4.63k stars） |

**核心创新**：系统性文本空间优化器，将技能作为外部智能体状态训练，稳定更新且零部署推理开销。在多个基准和运行环境上实现更优性能。

**Foundation Protocol: Agentic Society Coordination** (Tencent/HKUST/UIUC)

| 属性 | 内容 |
|------|------|
| **标题** | Foundation Protocol: Agentic Society Coordination |
| **中文标题** | Foundation Protocol：智能体社会协调协议 |
| **arXiv** | 2605.23218 |

**核心创新**：提出智能体社会中协调互动的协议框架，涵盖通信、协商、任务分配和冲突解决。

**AutoResearch AI: Research Automation** (Salesforce)

| 属性 | 内容 |
|------|------|
| **标题** | AutoResearch AI: Research Automation |
| **中文标题** | AutoResearch AI：研究自动化 |
| **arXiv** | 2605.23204 |

**核心创新**：端到端的研究自动化系统，从文献检索到实验设计到论文撰写。

### 12.2 游戏与决策

**SPIRAL: Self-Play Incentivizes Reasoning**

| 属性 | 内容 |
|------|------|
| **标题** | SPIRAL: Self-Play Incentivizes Reasoning |
| **中文标题** | SPIRAL：自对弈激励推理 |

**核心创新**：通过自对弈机制激励 LLM 提升推理能力，类似于 AlphaGo 的 self-play 训练范式在语言模型上的应用。

**GENSTRAT: Strategic Reasoning in LLMs**

| 属性 | 内容 |
|------|------|
| **标题** | GENSTRAT: Strategic Reasoning in LLMs |
| **中文标题** | GENSTRAT：LLM 中的战略推理 |
| **arXiv** | 2605.23238 |

**核心创新**：系统研究 LLM 在博弈场景中的战略推理能力，包括纳什均衡逼近、对手建模和长期策略规划。

### 12.3 代码推理

**Agentic Proving for Program Verification**

| 属性 | 内容 |
|------|------|
| **标题** | Agentic Proving for Program Verification |
| **中文标题** | 智能体化程序验证证明 |
| **arXiv** | 2605.23772 |

**核心创新**：将 LLM 智能体用于程序验证的形式化证明生成，结合交互式定理证明器实现端到端验证。

**ImProver 2: Neurosymbolic Proof Optimization** (CMU)

| 属性 | 内容 |
|------|------|
| **标题** | ImProver 2: Neurosymbolic Proof Optimization |
| **中文标题** | ImProver 2：神经符号证明优化 |
| **机构** | CMU |
| **arXiv** | 2605.22885 |

**核心创新**：神经符号方法结合 LLM 和传统证明搜索优化数学证明。

---

## 13. LLM 训练理论、Scaling Law 与对齐

### 13.1 训练理论

**Shannon Scaling Law**（ICML 2026）：将 LLM 视为噪声信道，推导预训练损失的理论下界。

**Transformers are Inherently Succinct**（ICLR 2026 Outstanding）：证明 Transformer 在表示某些函数类时具有参数效率本质优势。

**Complete-muE: MoE Hyperparameter Transfer**：MoE 架构超参数迁移方法。

### 13.2 对齐与安全

**SafeDPO**（ICLR 2026 Oral）：增强安全性的 DPO 方法。

**Why DPO is Misspecified**（ICLR 2026 Oral）：DPO 偏差理论分析及修正。

**AbstRaL**（Apple / ICLR 2026）：通过强化抽象思维增强 LLM 推理。

### 13.3 蒸馏与压缩

**Strong Teacher Not Needed? LLM Distillation**：挑战"强教师模型"在大模型蒸馏中的必要性假设。

**DiLaDiFF: Distilled Latent-Augmented Diffusion LM**（NVIDIA）：扩散语言模型的蒸馏方法。

---

## 14. 多模态与生成模型

### 14.1 扩散模型与流匹配

- **Self-Flow Matching**（ICML 2026）：无需配对数据的流匹配训练
- **Precise: SDE-Consistent Sampling for Flow-Matching RL**（ByteDance）：流匹配 RL 的一致性采样
- **Why Diffusion Models Don't Memorize**（NeurIPS 2025 Best Paper）：扩散模型不记忆的动力学解释
- **LLSA**（CVPR 2026 Highlight）：对数线性稀疏注意力扩散 Transformer

### 14.2 视频与 3D 生成

- **SeedVR2: One-Step Video Restoration**（ICLR 2026）：单步视频修复
- **WorldLens**（CVPR 2026 Oral）：驾驶世界模型全面评估
- **PhysX-Anything**（CVPR 2026）：单图生成可模拟 3D 资产
- **PI-Light**（ICLR 2026）：物理启发的扩散全图重光照

### 14.3 多模态理解

- **UniAR**（Alibaba / ICML 2026）：统一多模态自回归建模
- **WAVE: Unified Audio-Visual Embeddings with Multimodal LLM**（ICLR 2026）：音视频统一嵌入
- **OmniVGGT**（CVPR 2026 Highlight）：全模态视觉几何 Transformer

---

> **数据来源**：ICML 2026 官方 / ICLR 2026 OpenReview / NeurIPS 2025 OpenReview / AAAI 2026 dblp / CVPR 2026 官方 / KDD 2026 dblp / ACL/EMNLP 2025 官方 / SIGIR 2026 官方 / WWW 2026 官方 / CIKM 2025 dblp / RecSys 2025 官方 / arXiv.
>
> **总览**：本期报告覆盖 12+ 会议，收录 100+ 篇重点论文，涵盖 LLM 训练理论、推荐系统/CTR 预测、智能体系统、多模态与生成模型、游戏 AI、代码生成等研究方向。
