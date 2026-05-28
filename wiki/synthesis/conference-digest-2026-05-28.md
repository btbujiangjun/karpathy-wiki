---
title: 顶会论文专题报告 — 2026年5月全面版
type: synthesis
created: 2026-05-28
updated: 2026-05-28
sources: [neurips-2025-best-papers, iclr-2026-outstanding-papers, icml-2026, aaai-2026, cvpr-2026, emnlp-2025, kdd-2025, recsys-2025, sigir-2026]
tags: [conference-digest, neurips, iclr, icml, aaai, cvpr, emnlp, kdd, recsys, sigir]
---

# 顶会论文专题报告 — 2026年5月全面版

> 覆盖 NeurIPS 2025、ICLR 2026、ICML 2026、AAAI 2026、CVPR 2026、EMNLP 2025、KDD 2025、RecSys 2025、SIGIR 2026 等顶级会议及最新 arXiv 亮点论文。

---

## 目录

1. [NeurIPS 2025 — 最佳论文专题](#1-neurips-2025--最佳论文专题)
2. [ICLR 2026 — 杰出论文专题](#2-iclr-2026--杰出论文专题)
3. [AAAI 2026 — 亮点论文](#3-aaai-2026--亮点论文)
4. [ICML 2026 — 趋势与亮点](#4-icml-2026--趋势与亮点)
5. [CVPR 2026 — 最佳论文与 Oral 论文](#5-cvpr-2026--最佳论文与-oral-论文)
6. [EMNLP 2025 — 亮点论文](#6-emnlp-2025--亮点论文)
7. [KDD 2025 — 数据挖掘亮点](#7-kdd-2025--数据挖掘亮点)
8. [RecSys 2025 — 推荐系统前沿](#8-recsys-2025--推荐系统前沿)
9. [SIGIR 2026 — 信息检索前沿](#9-sigir-2026--信息检索前沿)
10. [跨领域趋势综述](#10-跨领域趋势综述)

---

## 1. NeurIPS 2025 — 最佳论文专题

> 会议时间：2025年12月（San Diego + Mexico City双城），接受率约 25%（5,300/21,000+ 投稿）

### 1.1 Best Papers（4篇）

#### 🏆 Paper 1: Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)

| 项目 | 内容 |
|------|------|
| **中文标题** | 人工蜂群思维：语言模型在开放式生成中的同质化现象 |
| **作者** | Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Yejin Choi |
| **机构** | University of Washington, CMU, Allen Institute for AI, Lila Sciences, Stanford |
| **论文链接** | [OpenReview](https://openreview.net/forum?id=saDOrrnNTz) |
| **代码** | [GitHub](https://github.com/liweijiang/artificial-hivemind) |

**问题背景：** 当前 LLM 在开放式创意生成任务中是否真正具备多样性？当多个模型面临同一个开放式问题时（例如"写一个关于时间的比喻"），不同模型往往产生高度相似的输出，呈现"人工蜂群思维"现象。然而，现有的多样性评估方法局限于随机数生成、名字生成等狭窄任务。

**方法与创新：**
1. **Infinity-Chat 数据集**：包含 26K 真实世界开放式用户查询，涵盖 6 大顶层类别和 17 个子类别，配有 31,250 条人工偏好标注
2. **系统化多样性评估框架**：首次提出全面的开放式提示分类法
3. **发现"人工蜂群思维"效应**：包括 (1) 模型内部重复 — 同一模型反复生成相似答案；(2) 跨模型同质化 — 不同模型家族输出惊人相似
4. **揭示校准问题**：当前奖励模型、LM 评判器在具有分歧偏好的生成上校准不良

**实验结果：** 覆盖 70+ 主流 LLM，发现即使使用不同温度系数和模型集成，多样性仍然有限。

---

#### 🏆 Paper 2: Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free

| 项目 | 内容 |
|------|------|
| **中文标题** | 门控注意力机制：非线性、稀疏性与无注意力汇 |
| **作者** | Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, Junyang Lin |
| **机构** | Alibaba Qwen Team |
| **论文链接** | [OpenReview](https://openreview.net/forum?id=1b7whO4SfY) |
| **代码/模型** | [GitHub](https://github.com/qiuzh20/gated_attention), [HuggingFace](https://huggingface.co/QwQZh/gated_attention) |

**问题背景：** 门控机制在 LSTM、Highway Networks、状态空间模型和线性注意力中广泛应用，但其在 softmax 注意力中的具体效果缺乏系统研究。

**方法与创新：**
1. 在 30+ 种 gated softmax attention 变体上进行系统比较，使用 15B MoE 和 1.7B dense 模型在 3.5T token 上训练
2. **核心发现**：在 SDPA（Scaled Dot-Product Attention）后添加 head-specific sigmoid gate 能持续提升性能
3. 该修改增强了训练稳定性、允许更大学习率、改善了扩展特性
4. **消除注意力汇（Attention Sink）**：稀疏门控机制显著缓解 massive activation 和 attention sink 现象，提升长上下文外推能力

**实验结果：** 该发现已集成到 Qwen3-Next 模型中（2025年9月发布）。实验覆盖 400B、1T、3.5T token 规模。

---

#### 🏆 Paper 3: 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities

| 项目 | 内容 |
|------|------|
| **中文标题** | 千层网络自监督强化学习：深度扩展带来新能力 |
| **作者** | Kevin Wang, Ishaan Javali, Michał Bortkiewicz, Tomasz Trzcinski, Benjamin Eysenbach |
| **机构** | - |
| **论文链接** | [OpenReview](https://openreview.net/forum?id=s0JVsx3bx1) |

**问题背景：** 自监督学习在语言和视觉领域通过扩展带来突破，但在 RL 中进展有限。近年来多数 RL 论文使用浅层网络（2-5层），本文质疑深度是否同样适用于 RL。

**方法与创新：**
1. 证明 RL 能从网络深度扩展中获益，将深度扩展到 1024 层
2. 在无监督目标条件设置下（无演示、无奖励），agent 必须从零开始探索并学会达成指定目标
3. 性能提升 2-50 倍，超越现有目标条件基线
4. 分析了 batch size 在深度对比 RL 中的关键作用

**实验结果：** 在模拟 locomotion 和 manipulation 任务上，深度扩展不仅提升成功率，还带来质变的行为模式涌现。

---

#### 🏆 Paper 4: Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training

| 项目 | 内容 |
|------|------|
| **中文标题** | 扩散模型为何不记忆：隐式动力学正则化的作用 |
| **作者** | Tony Bonnaire, Raphaël Urfin, Giulio Biroli, Marc Mezard |
| **机构** | - |
| **论文链接** | [OpenReview](https://openreview.net/forum?id=BSZqpqgqM0) |

**问题背景：** 扩散模型能在高度过参数化设置下避免记忆训练数据，实现泛化，其机制尚不清晰。

**方法与创新：**
1. 识别两个不同的时间尺度：泛化时间 t_gen（与数据无关）和记忆化时间 t_mem（与训练集大小线性相关）
2. t_gen 与 t_mem 之间存在不断扩大的时间窗口，模型在此期间有效泛化
3. 只有当 t_gen > 模型相关阈值时，过拟合才在无穷训练时间下消失
4. 通过随机特征模型和随机矩阵理论提供了严格的理论分析

**实验结果：** 使用标准 U-Net 架构在合成和真实数据集上的实验验证了理论预测。

---

### 1.2 Runners-Up（3篇）

#### Paper 5: Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?

| 项目 | 内容 |
|------|------|
| **中文标题** | RLVR 真的能激发超越基座模型的推理能力吗？ |
| **作者** | Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Yang Yue, Shiji Song, Gao Huang |
| **机构** | 清华大学等 |
| **论文链接** | [OpenReview](https://openreview.net/forum?id=4OsgYD7em5) |

**核心发现：** 通过 pass@k（k 较大时）系统评估多种 RLVR 算法（6种），发现 RLVR 确实提升了采样效率（小 k），但并未引入根本性的新推理模式。基座模型在 k 较大时 pass@k 评分更高。RLVR 的推理路径已经包含在基座模型的采样分布中。而蒸馏（distillation）则可以引入教师模型的新的推理模式。

---

#### Paper 6: Optimal Mistake Bounds for Transductive Online Learning

| 项目 | 内容 |
|------|------|
| **中文标题** | 转导式在线学习的最优错误界 |
| **作者** | Zachary Chase, Steve Hanneke, Shay Moran, Jonathan Shafer |

**核心贡献：** 解决了 30 年悬而未决的问题，精确量化了转导式 vs 标准在线学习的差距，证明转导式错误界为 Ω(√d) 且紧，展示了无标签数据的二次方优势。

---

#### Paper 7: Superposition Yields Robust Neural Scaling

| 项目 | 内容 |
|------|------|
| **中文标题** | 叠加表示带来稳健的神经缩放律 |
| **作者** | Yizhou Liu, Ziming Liu, Jeff Gore |

**核心发现：** 提出表示叠加（representation superposition）是神经缩放律的核心驱动因素。强叠加条件下，损失与模型维度成反比幂律关系。经验证，开源 LLM 处于强叠加状态，其损失缩放与 Chinchilla 缩放律一致。

---

### 1.3 Test of Time Award

| 论文 | 作者 | 引用量 |
|------|------|--------|
| **Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks** | Shaoqing Ren, Kaiming He, Ross Girshick, Jian Sun | 56,700+ |

---

## 2. ICLR 2026 — 杰出论文专题

> 会议时间：2026年4月23-27日，巴西里约热内卢；接受率 27.4%（5,355/19,525）；Oral 225 篇

### 2.1 Outstanding Papers

#### 🏆 Paper 1: Transformers are Inherently Succinct

| 项目 | 内容 |
|------|------|
| **中文标题** | Transformer 天生简洁：编码效率的理论解释 |
| **作者** | Pascal Bergsträßer, Ryan Cotterell, Anthony Widjaja Lin |
| **论文链接** | [OpenReview](https://openreview.net/forum?id=Yxz92UuPLQ) |

**核心贡献：** 提出了解释 Transformer 架构能力的新视角——编码简洁性（succinctness），即 Transformer 编码某些概念时比 RNN 等替代模型更"简洁"。该理论工作可能刺激对 Transformer 概念表示简洁性的进一步理论与实证研究。

---

#### 🏆 Paper 2: LLMs Get Lost In Multi-Turn Conversation

| 项目 | 内容 |
|------|------|
| **中文标题** | LLM 在多轮对话中迷失 |
| **作者** | Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville |
| **机构** | - |
| **论文链接** | [OpenReview](https://openreview.net/forum?id=VKGTGGcwl6) |

**核心贡献：** 揭示了训练数据（文本补全/单轮对话）与实际部署（多轮对话）之间的显著不匹配。设计可扩展的多轮对话评估方法，发现当交互涉及多轮和模糊指令时，LLM 能力和可靠性显著下降。

---

### 2.2 Honorable Mention

#### Paper: The Polar Express: Optimal Matrix Sign Methods and their Application to the Muon Algorithm

| 项目 | 内容 |
|------|------|
| **中文标题** | 极地特快：最优矩阵符号方法及其在 Muon 优化器中的应用 |
| **作者** | Noah Amsel, David Persson, Christopher Musco, Robert M. Gower |

**核心贡献：** 使用逼近论为极分解设计最优多项式逼近，应用于流行的 Muon 优化器，特别关注 GPU 和低精度计算场景。

---

### 2.3 ICLR 2026 研究趋势

根据对 5,357 篇接受论文的分析，关键趋势包括：
- **GRPO** 出现于 157 篇论文，DPO 仅 55 篇——学术社区已从 DPO 转向 GRPO
- **RLVR** 125 篇 vs RLHF 54 篇——可验证奖励场景优先
- **Test-time compute** 257 篇——推理时计算扩展已成为主流
- **Mamba/SSM** 202 篇——状态空间模型仍是活跃方向
- **Agent 安全** — MCP Security Bench 显示更好的指令遵循能力反而增加工具注入漏洞风险

> ⚠️ ICLR 2026 遭遇审查危机：OpenReview API 漏洞导致约 45% 会议论文的作者/审稿人身份泄露；21% 同行评审被确认完全由 AI 生成。

---

## 3. AAAI 2026 — 亮点论文

> 会议时间：2026年1月20-27日，新加坡；约 29,000 投稿，~23,000 有效评审，接受率 17.6%

### 3.1 会议概况

AAAI-26 规模巨大：Program Committee 扩至 28,000+ 成员（去年同期 3 倍）。中国贡献约 20,000 投稿。三大研究领域为 CV、ML、NLP。

### 3.2 亮点论文

#### ReconVLA（Oral, 分数 88887）

| 项目 | 内容 |
|------|------|
| **中文标题** | 视觉语言动作模型的视觉表示重构学习 |
| **作者** | Song Wenxuan 等 |
| **机构** | 香港科技大学（广州） |
| **核心创新** | 通过引入"视觉 token"引导"注视区域"重构的辅助任务，隐式增强 VLA 的实际操作能力 |

#### VLA-Adapter（Oral, GitHub 1.6k stars）

| 项目 | 内容 |
|------|------|
| **中文标题** | 轻量级 VLA 基座模型适配器 |
| **作者** | Song Wenxuan 等 |
| **机构** | 香港科技大学（广州） |
| **核心创新** | 仅 0.5B 的小模型在 CALVIN、LIBERO 等主流基准上实现 SOTA |

#### MPAS: Parallel Multi-Agent System（Oral）

| 项目 | 内容 |
|------|------|
| **中文标题** | 基于图消息传递的并行多智体系统 |
| **机构** | 南洋理工大学 |
| **核心创新** | 打破序列通信限制，通信时间从 84.6s 降至 14.2s，显著增强后门鲁棒性 |

#### SECURE: Fine-Tuning Security Constraint（Oral）

| 项目 | 内容 |
|------|------|
| **中文标题** | 微调安全约束方法 |
| **机构** | 南洋理工大学 |
| **核心创新** | 惩罚正交更新以将模型保持在"窄安全盆地"中，减少 7.6% 有害行为，性能提升 3.4% |

#### 其他亮点论文

| 论文 | 机构 | 方向 |
|------|------|------|
| GeoShield | 南洋理工大学 | VLM 地理隐私保护 |
| EmoAgent | 南洋理工大学 | 多模态情感安全 |
| PhysPatch | 南洋理工大学 | 自动驾驶对抗补丁 |
| GlassVAE | - | 无序材料生成 |
| DiffuNovo | - | 从头多肽测序 |

---

## 4. ICML 2026 — 趋势与亮点

> 会议时间：2026年7月，韩国首尔；投稿 24,371，接受 6,352（26.6%）

### 4.1 关键统计数据

- 投稿量较 2025 年（12,107）翻倍，创历史新高
- 2.2% 被选为 Spotlight
- 论文领域分布广泛，RL、优化、统计学习理论占比突出

### 4.2 亮点论文

#### Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis

| 项目 | 内容 |
|------|------|
| **中文标题** | 自监督流匹配实现可扩展多模态合成 |
| **论文链接** | [PaperDigest](https://www.paperdigest.org/paper/?paper_id=icml-65011-2026-05-05) |

#### Enhancing Protein-Protein Interaction Prediction with Hierarchical Motif-Based Multimodal Protein Embedding

| 项目 | 内容 |
|------|------|
| **作者** | Z. Yang, S.P.-M. Choi, J. Kwok |
| **机构** | HKUST |

#### SPARD: Defending Harmful Fine-Tuning Attack via Safety Projection

| 项目 | 内容 |
|------|------|
| **作者** | S. Chen, W. Jiang, Y. Gong 等 |
| **机构** | HKUST 等 |

#### Causal Effect Identifiability in the Presence of Latent Confounders

| 项目 | 内容 |
|------|------|
| **作者** | X.-C. Li, J. Kwok, J. Guo, T. Liu |
| **机构** | HKUST |

#### Group Cognition Learning: Making Everything Better Through Governed Two-Stage Agents Collaboration

| 项目 | 内容 |
|------|------|
| **中文标题** | 群体认知学习：两阶段受控智体协作 |
| **状态** | ICML 2026 接受 |
| **链接** | [arXiv:2605.00370](https://arxiv.org/abs/2605.00370) |

#### ResRL: Boosting LLM Reasoning via Negative Sample Projection Residual Reinforcement Learning

| 项目 | 内容 |
|------|------|
| **中文标题** | 负样本投影残差 RL 增强 LLM 推理 |
| **链接** | [arXiv:2605.00380](https://arxiv.org/abs/2605.00380) |

#### ALIVE: Interactive Frontend Games via RL

| 项目 | 内容 |
|------|------|
| **机构** | Alibaba / ICML 2026 |
| **链接** | - |

#### UniAR: Unified Multimodal Autoregressive Modeling

| 项目 | 内容 |
|------|------|
| **机构** | Alibaba / ICML 2026 |
| **链接** | - |

---

## 5. CVPR 2026 — 最佳论文与 Oral 论文

> 会议时间：2026年6月，美国丹佛；投稿 16,092，接受 4,090（25.4%）

### 5.1 最佳论文

#### 🏆 SAM 3D: 3Dfy Anything in Images

| 项目 | 内容 |
|------|------|
| **中文标题** | SAM 3D：将任何图像转化为 3D |
| **作者** | Jianing Yang, Georgia Gkioxari, Anushka Sagar 等 |
| **机构** | Meta AI / Facebook Research |
| **论文链接** | [arXiv:2511.16624](https://arxiv.org/abs/2511.16624) |
| **代码** | [GitHub](https://github.com/facebookresearch/sam-3d-objects) |

**核心创新：** 将 SAM 的零样本分割能力扩展到 3D 领域，实现从单张图像生成高质量 3D 模型。Oral + Best Paper。

### 5.2 Oral & Highlight 论文

#### WorldLens: Full-Spectrum Evaluations of Driving World Models (Oral)

| 项目 | 内容 |
|------|------|
| **作者** | A. Liang, L. Kong, T. Yan 等 |
| **机构** | MMLab@NTU |
| **论文链接** | [arXiv:2512.10958](https://arxiv.org/abs/2512.10958) |

#### OmniVGGT: Omni-Modality Driven Visual Geometry Grounded Transformer (Highlight)

| 项目 | 内容 |
|------|------|
| **作者** | H. Peng, H. Li, Y. Dai 等 |
| **机构** | MMLab@NTU |
| **论文链接** | [arXiv:2511.10560](https://arxiv.org/abs/2511.10560) |

#### MatAnyone2: Scaling Video Matting via a Learned Quality Evaluator (Highlight)

| 项目 | 内容 |
|------|------|
| **作者** | P. Yang, S. Zhou, K. Hao, Q. Tao |
| **机构** | MMLab@NTU |
| **论文链接** | [arXiv:2512.11782](https://arxiv.org/abs/2512.11782) |

#### LLSA: Trainable Log-linear Sparse Attention for Efficient Diffusion Transformers (Highlight)

| 项目 | 内容 |
|------|------|
| **中文标题** | 可训练对数线性稀疏注意力加速扩散 Transformer |
| **作者** | Y. Zhou, Z. Xiao, T. Wei 等 |
| **机构** | MMLab@NTU |
| **论文链接** | [arXiv:2512.16615](https://arxiv.org/abs/2512.16615) |

#### B³-Seg: Camera-Free, Training-Free 3DGS Segmentation (Highlight)

| 项目 | 内容 |
|------|------|
| **作者** | Hiromichi Kamata, Samuel Arthur Munro, Fuminori Homma |
| **论文链接** | [arXiv:2602.17134](https://arxiv.org/abs/2602.17134) |

### 5.3 其他方向

| 论文方向 | 代表论文 | 机构 |
|---------|---------|------|
| 3D Vision | SAM 3D (Best Paper), B³-Seg | Meta, Sony |
| Video Generation | VIRAL (Sim-to-Real Locomanipulation) | - |
| Medical | Open-Med-Reasoner, MDAE | Microsoft Research |
| Efficient CV | LLSA (Sparse Attention for DiT) | MMLab@NTU |
| Driving | WorldLens | MMLab@NTU |

---

## 6. EMNLP 2025 — 亮点论文

> 会议时间：2025年11月4-9日，中国苏州；8,174 投稿，1,811 接受（22.16%）

### 6.1 会议概况

- Main Track: 1,811 篇接受（22.16%）
- Findings: 1,418 篇接受（17.35%）
- 投稿量较 2024（6,105）增长 34%

### 6.2 Apple 亮点论文

| 论文 | 方向 | 链接 |
|------|------|------|
| Bias after Prompting: Persistent Discrimination in LLMs | 公平性 | [Apple ML Research](https://machinelearning.apple.com/research/persistent-discrimination) |
| Speculative Streaming: Efficient Speculative Decoding | 推理加速 | [Apple ML Research](https://machinelearning.apple.com/research/llm-inference) |
| Evaluating Evaluation Metrics — The Mirage of Hallucination Detection | 幻觉检测评估 | [Apple ML Research](https://machinelearning.apple.com/research/hallucination-detection) |
| PrimeX: A Dataset of Worldview, Opinion, and Explanation | 数据集 | [Apple ML Research](https://machinelearning.apple.com/research/primex) |
| Toward Machine Interpreting | 机器口译 | [Apple ML Research](https://machinelearning.apple.com/research/toward-machine-interpreting) |

### 6.3 主要研究方向

- LLM 推理与推理加速
- 幻觉检测与事实性
- 多语言与低资源 NLP
- 大模型对齐与安全
- 代码生成与程序合成

---

## 7. KDD 2025 — 数据挖掘亮点

> 会议时间：2025年8月3-7日，加拿大多伦多

### 7.1 Snap 亮点论文

| 论文 | 方向 | 机构 |
|------|------|------|
| GiGL: Large-Scale Graph Neural Networks at Snapchat | 图神经网络系统 | Snap |
| Revisiting Self-Attention for Cross-Domain Sequential Recommendation | 跨域序列推荐 | Snap |
| On the Role of Weight Decay in Collaborative Filtering | 协同过滤分析 | Snap |

### 7.2 A*STAR 亮点论文

| 论文 | 方向 |
|------|------|
| BurstGPT: A Real-World Workload Dataset to Optimise LLM Serving Systems | LLM 服务系统数据集（Azure OpenAI GPT, 10.31M traces, 213天） |
| TERSE: Temporal Restoration and Spatial Rewiring for Source-Free MTS Domain Adaptation | 时间序列域适应 |
| FreRA: A Frequency-Refined Augmentation for Contrastive Learning on Time Series | 时间序列对比学习 |

### 7.3 代表性方向

- 大规模图神经网络部署
- 时序数据分析与域适应
- 推荐系统冷启动与流行度偏差
- LLM 服务系统优化
- 因果推断与机器学习

---

## 8. RecSys 2025 — 推荐系统前沿

> 会议时间：2025年9月22-26日，捷克布拉格

### 8.1 Beyond CTR — 长期用户价值优化

| 论文 | 机构 | 核心创新 |
|------|------|---------|
| Beyond Immediate Click: Engagement-Aware MoE Sequential Rec | Prime Video / Amazon | 时序 MoE + 个性化硬负采样 + 多任务学习（CTR + 排序 + 完成率），NDCG@1 提升 +3.5% |
| Explicit Negatives at Scale | TikTok | 捕获/去噪/传播"不喜欢"信号，训练与推理双阶段利用 |
| Peak-End Retention | Meta Reels | 心理学启发的长期优化方法 |

### 8.2 LLM 与推荐系统融合

| 论文 | 机构 | 核心创新 |
|------|------|---------|
| Balancing Fine-tuning and RAG for Dynamic LLM Recommendation | Google Research | 混合策略：周期性微调 + RAG 更新用户兴趣，YouTube 大规模测试验证 |
| Lasso: LLM-based User Simulator for Cross-Domain Rec | - | 大模型驱动的跨域用户模拟器 |
| You Say Search, I Say Recs | Spotify | 面向查询理解与探索式搜索的 Agent 方法 |

### 8.3 模型架构与效率

| 论文 | 机构 | 核心创新 |
|------|------|---------|
| LEAF: Lightweight Embedding for Large-Scale Rec | - | 轻量高效嵌入 |
| Exploring Scaling Laws of CTR Model | Meituan | CTR 模型缩放律（RecSys 2025） |
| Multi-Granularity Distribution Modeling for Video Watch Time | - | 指数-高斯混合网络预测观看时间 |
| User Long-Term Multi-Interest Retrieval | - | 长期多兴趣检索 |
| Zero-shot Cross-domain Knowledge Distillation | YouTube Music | 零样本跨域知识蒸馏 |

### 8.4 关键趋势

| 趋势 | 描述 |
|------|------|
| 超越 CTR | 从即时点击优化转向长期用户价值（完成率、满意度、留存） |
| LLM 时代推荐 | 知识蒸馏 + RAG + 多智能体架构深度融合 |
| 负反馈利用 | TikTok 等平台系统化使用"不喜欢"信号纠正反馈循环 |
| 缩放律持续 | 工业界持续追求更大模型、更多数据带来的性能提升 |
| 离线-在线一致性 | Bridge gap 方法成为评估系统设计的重要方向 |

---

## 9. SIGIR 2026 — 信息检索前沿

> 会议时间：2026年7月20-24日，澳大利亚墨尔本

### 9.1 亮点论文

#### Revisiting Text Ranking in Deep Research

| 项目 | 内容 |
|------|------|
| **中文标题** | 重新审视深度研究中的文本排序 |
| **作者** | Chuan Meng, Litu Ou, Sean MacAvaney, Jeff Dalton |
| **机构** | University of Glasgow 等 |
| **论文链接** | [arXiv:2602.21456](https://arxiv.org/abs/2602.21456) |
| **代码** | [GitHub](https://github.com/ChuanMeng/text-ranking-in-deep-research) |

**核心创新：** 系统评估深度研究 Agent 在访问不同检索器和重排序器时的文本排序性能。覆盖 2 个 Agent、5 个检索器（BM25、SPLADE-v3、RepLLaMA、Qwen3-Embedding-8B、ColBERTv2）和 3 个重排序器（monoT5-3B、RankLLaMA-7B、Rank1-7B）。

---

## 10. 跨领域趋势综述

### 10.1 LLM 基础架构

| 趋势 | 具体表现 | 代表论文 |
|------|---------|---------|
| GRPO 取代 DPO | ICLR 2026 中 GRPO 论文数是 DPO 的 3 倍 | 多篇 |
| RLVR 超越 RLHF | 可验证奖励优于人类偏好数据 | ICLR 趋势 |
| Gated Attention | 简单门控修改持续提升 Transformer 性能 | Gated Attention (NeurIPS 2025 Best) |
| 推理时计算扩展 | 257 篇论文在 ICLR 2026 | 多篇 |
| 表示叠加理论 | 解释神经缩放律的核心机制 | Superposition Yields Scaling (NeurIPS 2025) |

### 10.2 推荐系统与广告

| 趋势 | 描述 |
|------|------|
| 从 CTR 到长期价值 | Prime Video、TikTok、Meta 等头部公司全面转向 |
| Scaling Laws 工业化 | FAT (Alibaba)、SUAN (Meituan)、Wukong (Meta) 等 |
| LLM 全方位融合 | Fine-tuning + RAG + Agent + Synthetic Data |
| 负反馈系统化 | TikTok Explicit Negatives 范式 |

### 10.3 多模态与视觉

| 趋势 | 描述 |
|------|------|
| 3D 基础模型 | SAM 3D (CVPR 2026 Best Paper) |
| 视频生成加速 | SANA-Video (ICLR 2026 Oral)、LLSA (CVPR 2026) |
| VLA 模型 | ReconVLA、VLA-Adapter (AAAI 2026 Oral) |
| 自动驾驶世界模型 | WorldLens (CVPR 2026 Oral) |

### 10.4 Agent 系统

| 趋势 | 描述 |
|------|------|
| 多 Agent 协作 | Foundation Protocol、MPAS |
| Agent 安全悖论 | 能力越强越易受攻击（MCP Security Bench, ICLR 2026） |
| 长期任务规划 | MEM1 (ICLR 2026)、SkillOpt (Microsoft) |

### 10.5 安全与对齐

| 关键发现 | 论文/来源 |
|----------|----------|
| 浅层安全对齐是脆弱性根源 | ICLR 2025 Outstanding Paper |
| RLVR 不引入新推理模式，蒸馏才能 | NeurIPS 2025 Best Paper Runner-Up |
| 人工蜂群思维降低多样性 | NeurIPS 2025 Best Paper |
| 多轮对话中 LLM 可靠性显著下降 | ICLR 2026 Outstanding Paper |

---

## 附录：会议规模对比

| 会议 | 年份 | 投稿数 | 接受数 | 接受率 | 地点 |
|------|------|--------|--------|--------|------|
| AAAI | 2026 | ~29,000 | ~4,000 | 17.6% | 新加坡 |
| ICML | 2026 | 24,371 | 6,352 | 26.6% | 首尔 |
| ICLR | 2026 | 19,525 | 5,355 | 27.4% | 里约热内卢 |
| CVPR | 2026 | 16,092 | 4,090 | 25.4% | 丹佛 |
| NeurIPS | 2025 | ~21,000 | ~5,300 | ~25% | 圣迭戈+墨西哥城 |
| EMNLP | 2025 | 8,174 | 1,811 | 22.2% | 苏州 |
| KDD | 2025 | - | ~250 (V1) | - | 多伦多 |
| RecSys | 2025 | - | - | - | 布拉格 |
| SIGIR | 2026 | - | - | - | 墨尔本 |

> 数据来源：各大会议官网、Paper Digest、OpenReview、DBLP 等。论文摘要与解读由 LLM 辅助整理，建议读者核实原文。
