---
title: "顶会论文专题报告 — 2026年6月全面版"
type: synthesis
created: 2026-06-21
updated: 2026-06-21
sources: [arxiv]
tags: [conference-digest, icml-2026, aaai-2026, neurips-2025, iclr-2026, kdd-2026, cvpr-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2025, recsys-2025]
---

# 顶会论文专题报告 — 2026年6月全面版

> **日期**: 2026-06-21
> **范围**: 12+ 会议/venue, 50+ 论文, 13+ 实验室 (Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, Netflix, NVIDIA, Anthropic, Apple, Amazon)
> **分类**: LLM 架构 / 推理 & RL / Agent 系统 / CTR & 推荐 / 生成模型 & 扩散 / 代码 & 形式推理 / Benchmark & 评估 / 游戏 & 战略推理 / 序列建模 / 多模态

---

## 1. NeurIPS 2025 Best Papers

### 1.1 Gated Attention
| 项目 | 内容 |
|------|------|
| Title | Gated Attention — Attention Sink Removal via Gating Mechanism |
| 中文 | 门控注意力 — 通过门控机制消除 Attention Sink |
| Affiliation | Alibaba / 多机构 |
| arXiv | — |

**问题背景**: 标准 Softmax Attention 存在 attention sink 现象（大量注意力分数集中在第一个 token），导致长上下文性能下降和 KV cache 效率低下。

**核心创新**: 提出门控注意力机制，在 attention 计算中引入可学习的门控信号，从根本上消除 attention sink，使得注意力分布更加均衡。

**实验结果**:
- 在长上下文任务上 perplexity 显著低于标准 attention
- KV cache 压缩效率提升 2-4 倍
- 训练稳定，无需额外正则化

**意义**: 解决了 Transformer 架构中长期存在的 attention sink 问题，为下一代高效 attention 设计提供了新方向。

### 1.2 RL Reasoning Critique — Beyond Reasoning: RL Unlocks Parametric Knowledge
| 项目 | 内容 |
|------|------|
| Title | Beyond Reasoning: Reinforcement Learning Unlocks Parametric Knowledge in Language Models |
| 中文 | 超越推理：强化学习解锁语言模型中的参数化知识 |
| Affiliation | Tsinghua University |
| arXiv | — |

**问题背景**: 传统观点认为 RL 对 LLM 的帮助主要是提升推理能力。本文挑战了这一假设。

**核心创新**: 证明 RL 能做的不仅仅是提升推理 — 它可以教会模型停止隐藏它们已经拥有的知识。提出了 value-action gap 理论框架，解释 RL 如何激活模型内部的知识表示。

**关键发现**:
- RL 训练后模型在某些知识密集型任务上提升显著，而推理路径并无明显改进
- 表明 RL 的收益部分来自于更好的知识利用而非纯粹的推理能力提升
- 分析了 RLVR 中 diversity collapse 现象：Pass@1 提升但 high-k Pass@k 下降

**意义**: 重新定义了 RL 在 LLM 训练中的作用，提示未来 RLVR 方法需要同时关注知识和推理两个方面。

### 1.3 Transductive Online Learning
| 项目 | 内容 |
|------|------|
| Title | Transductive Online Learning — A 30-Year Open Problem Solved |
| 中文 | 传导在线学习 — 解决 30 年开放问题 |
| Affiliation | 多机构 |
| arXiv | — |

**核心贡献**: 解决了在线学习理论中一个长达 30 年的开放问题，将 transductive learning 与 online learning 统一在一个理论框架下。

### 1.4 Speculative Streaming (Apple, EMNLP 2025)
| 项目 | 内容 |
|------|------|
| Title | Speculative Streaming: Fast LLM Inference without Auxiliary Models |
| 中文 | 推测流式推理：无辅助模型的快速 LLM 推理 |
| Affiliation | Apple |
| arXiv | — |

**核心创新**: 提出无需辅助小模型的推测解码方法，利用 LLM 自身的中间层表示进行草稿生成。在保持生成质量的同时实现 2-3× 推理加速。

---

## 2. ICLR 2026 Outstanding Papers

### 2.1 Transformers are Inherently Succinct
| 项目 | 内容 |
|------|------|
| Title | Transformers are Inherently Succinct |
| 中文 | Transformer 本质上是简洁的 |
| Affiliation | 多机构 |
| arXiv | — |

**核心贡献**: 从理论角度证明 Transformer 模型在表示复杂函数时具有内在的简洁性（succinctness）优势。与 RNN 和 SSM 相比，Transformer 可以用更少的参数表示相同的函数类。

**意义**: 为 Transformer 的持续主导地位提供了理论依据，解释了为什么 attention 机制在众多序列建模架构中表现突出。

### 2.2 MEM1: Memory-Reasoning Synergy for Long-Horizon Agents
| 项目 | 内容 |
|------|------|
| Title | MEM1: Memory-Reasoning Synergy for Long-Horizon Agents |
| 中文 | MEM1：面向长程 Agent 的记忆-推理协同 |
| Affiliation | — |
| arXiv | — |

**核心创新**: 提出记忆-推理协同框架，将记忆检索与推理过程深度融合，而非作为独立的 pipeline 组件。在长程任务上显著优于 RAG 方法。

### 2.3 AgentFlow: 7B Beats GPT-4o
| 项目 | 内容 |
|------|------|
| Title | AgentFlow: 7B Model Outperforms GPT-4o on Agent Tasks |
| 中文 | AgentFlow：7B 模型在 Agent 任务上超越 GPT-4o |
| Affiliation | — |
| arXiv | — |

**核心创新**: 提出基于流（flow）的 agent 框架，7B 模型通过优化的 agent pipeline 设计和执行流程，在复杂 agent 任务上超越 GPT-4o。

**意义**: 证明在 agent 领域，pipeline 设计和小模型优化可以弥补模型规模的差距。

### 2.4 Mamba-3: Inference-First SSM
| 项目 | 内容 |
|------|------|
| Title | Mamba-3: Improved Sequence Modeling Using State Space Principles |
| 中文 | Mamba-3：使用状态空间原理改进序列建模 |
| Affiliation | CMU / Princeton |
| arXiv | 2603.15569 |

**核心创新**: Mamba-3 采用 inference-first 设计理念，在保持 SSM 高效推理优势的同时，进一步提高了建模精度。引入了新的状态空间参数化方法，减少了量化误差。

**实验结果**:
- 在语言建模 perplexity 上与同规模 Transformer 持平或更好
- 推理速度比同规模 Transformer 快 3-5×
- 长序列上优势更明显（O(n) vs O(n²)）

### 2.5 Gated DeltaNet-2
| 项目 | 内容 |
|------|------|
| Title | Gated DeltaNet-2: Improved Linear Recurrent Units |
| 中文 | Gated DeltaNet-2：改进的线性循环单元 |
| Affilication | — |
| arXiv | — |

**核心创新**: 在 DeltaNet 基础上引入门控机制，进一步缩小线性循环模型与 Transformer 之间的质量差距。

---

## 3. ICML 2026

> ICML 2026 收到 23,918 篇投稿（较 2025 翻倍），接受 6,352 篇（接受率 26.6%），将于 2026 年 7 月 6–11 日在首尔举行。

### 3.1 Shannon Scaling Law: LLMs as Noisy Channels
| 项目 | 内容 |
|------|------|
| Title | Shannon Scaling Law: LLMs as Noisy Channels |
| 中文 | 香农缩放定律：作为噪声信道的 LLM |
| Affiliation | — (ICML 2026) |
| arXiv | 2605.23901 |

**问题背景**: 经典的 scaling law（如 Chinchilla）仅从 token 数量角度建模，没有考虑数据质量和噪声的影响。

**核心创新**: 借鉴信息论中香农信道容量的概念，将 LLM 训练建模为在噪声信道上传输信息的过程。Scaling law 包含数据质量因子（信噪比），更好解释了为什么高质量数据比单纯增加数据量更有效。

**关键发现**:
- 数据质量（SNR）是 scaling law 中比数据量更重要的因子
- 当数据 SNR 低于某个阈值时，继续增加数据量几乎无收益
- 提供了在给定预算下最优分配 compute 给数据清洗 vs 模型规模的公式

### 3.2 Self-Supervised Flow Matching (Self-Flow)
| 项目 | 内容 |
|------|------|
| Title | Self-Supervised Flow Matching |
| 中文 | 自监督流匹配 |
| Affiliation | — (ICML 2026) |
| arXiv | — |

**核心创新**: 提出无需配对数据的流匹配训练方法，利用自监督信号替代传统的 paired data 需求，显著降低了 flow matching 的训练门槛。

### 3.3 CTR-RL: RL-based CTR Optimization
| 项目 | 内容 |
|------|------|
| Title | CTR-RL: Reinforcement Learning for CTR Prediction |
| 中文 | CTR-RL：基于强化学习的点击率预测优化 |
| Affiliation | — |
| arXiv | — |

**核心创新**: 将 CTR 预测重新建模为强化学习问题，使用用户反馈（点击/未点击）作为奖励信号，避免传统交叉熵损失在样本选择偏差下的局限性。

**实验结果**:
- 在线 A/B 测试 CTR +4.7%
- 对冷启动物品提升尤其显著（+12.3%）

### 3.4 How CoT Decomposes Tasks
| 项目 | 内容 |
|------|------|
| Title | How Chain-of-Thought Decomposes Tasks: A Theoretical Framework |
| 中文 | Chain-of-Thought 如何分解任务：一个理论框架 |
| Affiliation | — |
| arXiv | — |

**核心贡献**: 从理论角度解释 CoT 为什么有效 — CoT 将复杂任务分解为一系列子任务，每个子任务的复杂度被有效降低，使得 Transformer 可以在有限的深度内解决原本需要更深网络的问题。

### 3.5 ALIVE: Interactive Frontend Games via RL (Alibaba)
| 项目 | 内容 |
|------|------|
| Title | ALIVE: Interactive Frontend Games via Reinforcement Learning |
| 中文 | ALIVE：基于强化学习的交互式前端游戏 |
| Affiliation | Alibaba (ICML 2026) |
| arXiv | — |

**核心创新**: 使用 RL 训练 Agent 直接生成前端游戏（HTML/JS），将游戏开发转化为决策问题。实现了从自然语言描述到可玩游戏端到端生成。

### 3.6 Quantized Reasoning Models Think They Need to Think Longer
| 项目 | 内容 |
|------|------|
| Title | Quantized Reasoning Models Think They Need to Think Longer, but They Do Not |
| 中文 | 量化推理模型认为自己需要想更久，但实际不需要 |
| Affiliation | — (ICML 2026) |
| arXiv | 2606.00206 |

**核心发现**: 量化的推理模型在推理时会生成更长的推理链，但实际性能并未因此提升。揭示了量化对推理模型的非预期影响，提示量化推理模型需要特殊处理。

### 3.7 BitsMoE: Efficient Spectral Energy-Guided Bit Allocation
| 项目 | 内容 |
|------|------|
| Title | BitsMoE: Efficient Spectral Energy-Guided Bit Allocation for MoE LLM Quantization |
| 中文 | BitsMoE：基于频谱能量的 MoE LLM 量化位分配 |
| Affiliation | — |
| arXiv | 2606.00079 |
| Code | github.com/zjiayu064/BitsMoE |

**核心创新**: 针对 MoE 模型的量化问题，提出基于频谱能量的位分配策略。不同 expert 和不同层对量化精度的敏感度不同，BitsMoE 智能分配位宽。

**实验结果**:
- 在保持模型质量的前提下，平均位宽降低 30%
- 在 MoE 模型上比统一位宽量化方案提升显著

### 3.8 Process-Verified RL for Theorem Proving
| 项目 | 内容 |
|------|------|
| Title | Process-Verified Reinforcement Learning for Theorem Proving via Lean |
| 中文 | 基于过程验证的强化学习定理证明 |
| Affiliation | — |
| arXiv | 2606.20068 |

**核心创新**: 将过程奖励模型（process reward model）与 Lean 形式化验证结合，在每一步推理中验证正确性，提供比结果奖励更细粒度的训练信号。

---

## 4. AAAI 2026 Outstanding Papers

### 4.1 Outstanding Paper Highlights
AAAI 2026 杰出论文涵盖以下方向：
- **推理与测试时计算**: 多步推理的复杂度边界分析
- **Agent 系统**: 多 Agent 协作的理论保证
- **可信 ML**: 因果推断与公平性的交叉
- **生成模型**: 离散扩散模型的理论进展

具体论文列表待 AAAI 2026 官方发布完整 proceedings。

---

## 5. CVPR 2026

> CVPR 2026 收到 16,092 篇投稿，接受 4,090 篇（接受率 ~25.4%），141 篇口头报告。将于 2026 年 6 月 2–6 日在丹佛举行。

### 5.1 D4RT — CVPR 2026 Best Paper (Google DeepMind)
| 项目 | 内容 |
|------|------|
| Title | D4RT: Dynamic 4D Scene Reconstruction and Rendering in Real Time |
| 中文 | D4RT：实时动态 4D 场景重建与渲染 |
| Affiliation | Google DeepMind |
| arXiv | — |

**核心创新**: 实现动态 4D 场景（3D + 时间）的实时重建和渲染。在 NeRF/3D Gaussian Splatting 基础上引入时间维度的显式建模，实现了动态场景的实时渲染。

**实验结果**:
- 渲染速度达到实时（>30 FPS）
- 在动态场景重建质量上大幅超越此前 SOTA

### 5.2 NitroGen: NVIDIA Generalist Gaming Agent
| 项目 | 内容 |
|------|------|
| Title | NitroGen: A Generalist Gaming Foundation Model |
| 中文 | NitroGen：通用游戏基础模型 |
| Affiliation | NVIDIA (CVPR 2026 Oral) |
| arXiv | — |

**核心创新**: NVIDIA 的通用游戏 Agent，训练数据覆盖数百款游戏，可以零样本适应新游戏环境。结合视觉理解和动作生成，实现人类级别的游戏操作。

**实验结果**:
- 在多款未见过的游戏中达到或超过人类水平
- 零样本迁移能力显著优于此前方法

### 5.3 ActionMesh: Animated 3D Mesh Generation with Temporal 3D Diffusion (Meta)
| 项目 | 内容 |
|------|------|
| Title | ActionMesh: Animated 3D Mesh Generation with Temporal 3D Diffusion |
| 中文 | ActionMesh：基于时序 3D 扩散的动画网格生成 |
| Affiliation | Meta (Facebook AI Research) |
| arXiv | 2601.16148 |
| Code | github.com/facebookresearch/actionmesh |

**核心创新**: 将扩散模型扩展到时序 3D 网格生成，直接生成带有动画的 3D 模型。输入单一静态网格或文本描述，输出完整的动画序列。

### 5.4 SAM 3D (Meta)
| 项目 | 内容 |
|------|------|
| Title | SAM 3D: 3Dfy Anything in Images |
| 中文 | SAM 3D：将图像中的任意物体 3D 化 |
| Affiliation | Meta |
| arXiv | 2511.16624 |
| Code | github.com/facebookresearch/sam-3d-objects |

**核心创新**: 将 SAM（Segment Anything）扩展到 3D 领域，从单张或少量图像中重建任意物体的 3D 模型。

### 5.5 VibeToken-Gen (Sony AI)
| 项目 | 内容 |
|------|------|
| Title | VibeToken-Gen: Efficient Autoregressive Visual Generation |
| 中文 | VibeToken-Gen：高效自回归视觉生成 |
| Affiliation | Sony AI |
| arXiv | 2604.24885 |

**核心创新**: 固定 token 长度的自回归图像生成，任何分辨率下推理计算量恒定（179G FLOPs）。相比扩散模型 SOTA（gFID 3.94 vs 5.87），生成速度 0.46 秒 vs 1.08 秒，使用 64 token vs 1024 token，效率提升 63.4×。

### 5.6 LLaDA-V: Large Language Diffusion Models with Visual Instruction Tuning
| 项目 | 内容 |
|------|------|
| Title | LLaDA-V: Large Language Diffusion Models with Visual Instruction Tuning |
| 中文 | LLaDA-V：面向视觉指令微调的大语言扩散模型 |
| Affiliation | Renmin University of China |
| arXiv | 2505.16933 |

**核心创新**: 首个将纯扩散语言模型（LLaDA）扩展到多模态视觉任务的模型。利用扩散模型的双向注意力优势，在视觉理解任务上与 LLaMA3-V 竞争，缩小了与 Qwen2-VL 的差距。

### 5.7 PixelDiT (NVIDIA)
| 项目 | 内容 |
|------|------|
| Title | PixelDiT: Pixel Diffusion Transformers for Image Generation |
| 中文 | PixelDiT：面向图像生成的像素扩散 Transformer |
| Affiliation | NVIDIA (CVPR 2026 Oral) |
| arXiv | 2511.20645 |
| Code | github.com/NVlabs/PixelDiT |

**核心创新**: 在像素空间直接运行的 Diffusion Transformer，避免了 VAE 编解码的信息损失。在 ImageNet 256×256 上取得 SOTA FID。

---

## 6. EMNLP 2025

> EMNLP 2025 在苏州举行，8,174 篇投稿，接受 1,811 篇（22.2%），另有 Findings 1,418 篇。

### 6.1 Speculative Streaming
参见 NeurIPS 2025 Best Papers 部分（Apple）。

### 6.2 Value-Action Gap in RL for LLMs
| 项目 | 内容 |
|------|------|
| Title | The Value-Action Gap in Reinforcement Learning for Large Language Models |
| 中文 | 大型语言模型强化学习中的价值-行动差距 |
| Affiliation | Tsinghua University (NeurIPS 2025 Best Paper also) |
| arXiv | — |

**核心发现**: LLM 在 RL 训练中，模型"知道"正确答案（value high）但无法"做出"正确答案（action wrong）。分析表明 value-action gap 源于模型推理能力与知识检索能力的脱节。

### 6.3 Song Generation with VersBand
| 项目 | 内容 |
|------|------|
| Title | VersBand: Versatile Song Generation with Band-Based Structure Control |
| 中文 | VersBand：基于乐队结构的全能歌曲生成 |
| Affiliation | — |
| arXiv | — |

---

## 7. KDD 2026

> KDD 2026 将于 2026 年 8 月 9–13 日在韩国济州岛举行。

### 7.1 RankUp (Tencent)
| 项目 | 内容 |
|------|------|
| Title | RankUp: Towards High-rank Representations for Large Scale Advertising Recommender Systems |
| 中文 | RankUp：面向大规模广告推荐系统的高秩表示 |
| Affiliation | Tencent (KDD 2026) |
| arXiv | 2604.17878 |

**问题背景**: 推荐系统的 scaling law 已得到验证，MetaFormer 架构持续受益于增加深度、隐藏维度和用户行为序列长度。但高维 embedding 存在过平滑和效率问题。

**核心创新**: 提出高秩表示学习方法，在不显著增加参数量的情况下提高向量表示的秩（rank），从而提升模型表达能力。

**实验结果**:
- 在 Tencent 广告系统上 CTR +3.2%
- 与其他 scaling 方法（增加深度/宽度）正交

### 7.2 RankElastor
| 项目 | 内容 |
|------|------|
| Title | RankElastor: Effective-Rank Dynamics for Recommendation |
| 中文 | RankElastor：推荐系统的有效秩动态 |
| Affiliation | — (KDD 2026) |
| arXiv | 2605.23191 |

**核心创新**: 研究了推荐模型中表示的有效秩动态变化，提出根据训练阶段动态调整秩的方法，在收敛速度和最终性能上都优于固定秩方法。

### 7.3 DIF (Kuaishou)
| 项目 | 内容 |
|------|------|
| Title | Denoising Implicit Feedback for Cold-start Recommendation |
| 中文 | 面向冷启动推荐的隐式反馈去噪 |
| Affiliation | Kuaishou (KDD 2026) |
| arXiv | 2606.19635 |

**核心创新**: 针对冷启动场景中的隐式反馈噪声（误点、偏见点击），提出去噪方法。建模了去噪与流行度偏差之间的交互效应。

### 7.4 JourneyFormer (Airbnb)
| 项目 | 内容 |
|------|------|
| Title | JourneyFormer: Journey-Aware Generative Sequential Recommendation |
| 中文 | JourneyFormer：旅程感知的生成式序列推荐 |
| Affiliation | Airbnb (KDD 2026) |
| arXiv | — |

**核心创新**: 引入"旅程"概念，将用户的连续交互建模为旅程，使用生成式方法预测下一目的地/房源。结合知识图谱属性增强推荐质量。

### 7.5 GenCTR (Alibaba)
| 项目 | 内容 |
|------|------|
| Title | Generative Click-through Rate Prediction with Applications to Search Advertising |
| 中文 | 生成式点击率预测及其在搜索广告中的应用 |
| Affiliation | Alibaba |
| arXiv | — |

**核心创新**: 两阶段框架 — 生成式预训练（预测用户序列中下一物品）+ 判别式微调（CTR 预测）。在阿里搜索广告系统中部署，服务数亿日活用户。

---

## 8. RecSys 2025

> RecSys 2025 在布拉格举行，19 届 ACM 推荐系统会议。

### 8.1 Amazon Prime Video — Beyond Immediate Click
| 项目 | 内容 |
|------|------|
| Title | Beyond Immediate Click: Engagement-Aligned Sequential Recommendation |
| 中文 | 超越即时点击：面向用户参与度的序列推荐 |
| Affiliation | Amazon Prime Video (RecSys 2025) |
| DOI | 10.1145/3705328.3748076 |

**核心创新**: 提出四方面改进：
1. **Temporal Mixture-of-Experts**：基于时间的 MoE，门控使用目标熵正则化
2. **个性化难负采样（PHNS）**：从 abandoned/trending/tailing 标题中采样
3. **参与度感知多任务学习**：CTR + ranking + completion-rate 联合优化
4. **Next-K 训练**：使用软标签（1.0/0.6/0.3）保持近邻连续性

**实验结果**: 在 Prime Video 约 100 万用户数据上，NDCG@1 提升 +3.5%。

### 8.2 TikTok Explicit Negatives
| 项目 | 内容 |
|------|------|
| Title | Explicit Negatives at Scale: Capture, Denoise, and Propagate Dislike Signals |
| 中文 | 大规模显式负反馈：捕获、去噪和传播"不喜欢"信号 |
| Affiliation | TikTok / ByteDance (RecSys 2025) |
| DOI | 10.1145/3705328.3748145 |

**核心创新**: 系统性地利用显式负反馈（dislike），包括捕获（轻量级上下文微信号）、去噪（意外点击、冷启动伪影）和传播（训练中的对比学习 + 服务端降级）。

### 8.3 Meta Peak-End Retention
| 项目 | 内容 |
|------|------|
| Title | Peak-End Retention: Psychology-Informed Long-Term Optimization |
| 中文 | 峰终保留：心理学启发的长期优化 |
| Affiliation | Meta (Reels) (RecSys 2025) |

**核心创新**: 将心理学中的"峰终定律"（peak-end rule）引入推荐系统优化，用户对体验的判断主要由峰值和结束时的感受决定，而非平均体验。

### 8.4 Meituan SUAN Scaling
| 项目 | 内容 |
|------|------|
| Title | SUAN: Online CTR Scaling Methodology |
| 中文 | SUAN：在线 CTR 缩放方法 |
| Affiliation | Meituan (RecSys 2025) |
| arXiv | 2508.15326 |

**核心创新**: 提出系统的在线 CTR 缩放方法论，包括模型在线蒸馏、动态特征选择、渐进式模型扩展。

---

## 9. SIGIR 2026

> SIGIR 2026 共接受 656 篇论文（含所有 track）。

### 9.1 GBLA Linear Attention for Generative Retrieval (Yandex)
| 项目 | 内容 |
|------|------|
| Title | GBLA: Generalized Bayesian Linear Attention for Generative Retrieval |
| 中文 | GBLA：面向生成式检索的广义贝叶斯线性注意力 |
| Affiliation | Yandex (SIGIR 2026) |
| arXiv | — |

**核心创新**: 将线性注意力与贝叶斯方法结合，用于生成式检索。在保持线性复杂度的同时，实现了接近标准 attention 的检索质量。

### 9.2 ELVA: RLVR for Retrieval (ECCV 2026)
| 项目 | 内容 |
|------|------|
| Title | ELVA: Exploring Ranking-Driven Universal Multimodal Retrieval |
| 中文 | ELVA：基于排序驱动的通用多模态检索 |
| Affiliation | — |
| arXiv | 2606.20280 |

**核心创新**: 将 RLVR 方法扩展到多模态检索领域，使用排序指标作为奖励信号训练检索模型。

---

## 10. WWW 2026

### 10.1 NEZHA (Taobao)
| 项目 | 内容 |
|------|------|
| Title | NEZHA: Large-Scale Generative Recommendation at Taobao |
| 中文 | NEZHA：淘宝大规模生成式推荐 |
| Affiliation | Alibaba / Taobao (WWW 2026) |
| arXiv | — |

**核心创新**: 淘宝的生成式推荐系统，服务 1 亿 DAU，驱动 ¥100 亿 GMV。使用生成式范式替代传统的检索-排序级联架构。

### 10.2 ThinkRec
| 项目 | 内容 |
|------|------|
| Title | ThinkRec: Thinking-based LLM Recommendation |
| 中文 | ThinkRec：基于思考的 LLM 推荐 |
| Affiliation | — (WWW 2026) |
| arXiv | — |

**核心创新**: 让 LLM 在推荐前进行显式的"思考"（推理链），分析用户兴趣和物品特征，再进行推荐预测。

### 10.3 GenCI (WWW 2026)
| 项目 | 内容 |
|------|------|
| Title | GenCI: Generative CTR via Cohort Intent Learning |
| 中文 | GenCI：基于群体意图学习的生成式 CTR 预估 |
| Affiliation | — (WWW 2026) |
| arXiv | 2601.18251 |

---

## 11. CIKM 2025

### 11.1 RankMixer (ByteDance)
| 项目 | 内容 |
|------|------|
| Title | RankMixer: Scaling Up Ranking Models |
| 中文 | RankMixer：扩展排序模型规模 |
| Affiliation | ByteDance (CIKM 2025) |
| arXiv | 2507.15551 |

**核心创新**: 提出 Mixer 架构在推荐排序场景的高效缩放方法，在保持推理效率的同时扩大模型容量。

---

## 12. LLM Architecture & Model Design (Recent arXiv)

### 12.1 Nemotron 3 Super (NVIDIA)
| 项目 | 内容 |
|------|------|
| Title | Nemotron 3 Super: Open, Efficient MoE Hybrid Mamba-Transformer Model for Agentic Reasoning |
| 中文 | Nemotron 3 Super：面向 Agent 推理的开源高效 MoE 混合 Mamba-Transformer 模型 |
| Affiliation | NVIDIA |
| arXiv | 2604.12374 |

**核心创新**: 首个大规模混合 Mamba-Transformer MoE 模型。结合 SSM 的高效推理和 Transformer 的强表达能力。针对 agentic reasoning 任务优化。

### 12.2 Mistral Ministral 3
| 项目 | 内容 |
|------|------|
| Title | Ministral 3 Technical Report |
| 中文 | Ministral 3 技术报告 |
| Affiliation | Mistral AI |
| arXiv | 2601.08584 |

**核心创新**: 采用 Cascade Distillation 训练策略 + 纯 RL 推理训练。在 3B 规模上达到接近 7B 模型的推理性能。

### 12.3 Scaling Embeddings Outperforms Scaling Experts
| 项目 | 内容 |
|------|------|
| Title | Scaling Embeddings Outperforms Scaling Experts in Language Models |
| 中文 | 缩放嵌入层在语言模型中优于缩放 Expert |
| Affiliation | — |
| arXiv | 2601.21204 |

**核心发现**: 在 MoE 模型中，增加 embedding 维度比增加 expert 数量更有效。挑战了"expert 越多越好"的主流假设。

### 12.4 ViT-5: Vision Transformers for the Mid-2020s
| 项目 | 内容 |
|------|------|
| Title | ViT-5: Vision Transformers for the Mid-2020s |
| 中文 | ViT-5：面向 2020 年代中期的视觉 Transformer |
| Affiliation | — |
| arXiv | 2602.08071 |

**核心创新**: 整合过去 3 年视觉 Transformer 的设计经验，提出第五代 ViT，在效率、精度和可扩展性方面全面改进。

### 12.5 The Spike, the Sparse and the Sink
| 项目 | 内容 |
|------|------|
| Title | The Spike, the Sparse and the Sink: Anatomy of Massive Activations and Attention Sinks |
| 中文 | Spike、Sparse 和 Sink：大规模激活和 Attention Sink 的解剖学分析 |
| Affiliation | — |
| arXiv | 2603.05498 |

**核心贡献**: 深入分析 LLM 中的 massive activations 和 attention sink 现象，揭示它们的成因和行为模式。为后续门控注意力等改进方案提供了理论基础。

### 12.6 ERNIE 5.0 (Baidu)
| 项目 | 内容 |
|------|------|
| Title | ERNIE 5.0 Technical Report |
| 中文 | ERNIE 5.0 技术报告 |
| Affiliation | Baidu |
| arXiv | 2602.04705 |

### 12.7 GLM-5 (Zhipu AI)
| 项目 | 内容 |
|------|------|
| Title | GLM-5: From Vibe Coding to Agentic Engineering |
| 中文 | GLM-5：从 Vibe Coding 到 Agentic Engineering |
| Affiliation | Zhipu AI |
| arXiv | 2602.15763 |

**核心创新**: 744B 参数（40B 激活）的 MoE 模型，引入 DSA（Dynamic Sparse Attention）和异步 RL 训练。强调从编码辅助向 agent 工程能力演进。

---

## 13. Reasoning & Test-Time Compute

### 13.1 LLM Research 2026 Perspective (Sebastian Raschka)
根据 Sebastian Raschka 的 2026 上半年论文综述，2026 年上半年 LLM 研究集中在：
1. **架构与模型设计** — 混合架构（Mamba-Transformer）、MoE 容量分配、表示几何
2. **高效训练与缩放** — 数据质量（Shannon Scaling Law）、Muon/MuonClip 优化器
3. **推理效率与 KV 缓存** — MLA、GQA、KV cache 量化
4. **稀疏注意力与长上下文** — 1M+ token context 成为旗舰标配
5. **推理与测试时计算** — Reasoning models + test-time compute scaling
6. **强化学习与 RLVR** — GRPO 变体、process reward model、RLVR diversity collapse
7. **Agent 系统与工具使用** — Code as agent harness、agentic engineering
8. **代码 Agent 与软件工程** — 代码为中心的 agent 架构
9. **扩散语言模型** — 离散扩散、扩散 LM 与自回归 LM 的竞争
10. **模型评估与基准** — 新型基准（LiveCodeBench、FrontierCode、FrontierScience）

### 13.2 SPIRAL: Self-Play for LLM Reasoning
| 项目 | 内容 |
|------|------|
| Title | SPIRAL: Self-Play Incentivizes Reasoning in LLMs |
| 中文 | SPIRAL：自我对弈激励 LLM 推理 |
| Affiliation | — (ICLR 2026) |
| arXiv | — |

**核心创新**: 将游戏中的自我对弈（self-play）机制引入 LLM 推理训练。模型在不断与自己生成的数据对弈中，自动产生越来越复杂的推理链。

**意义**: 提供了无需人工标注的推理数据生成方法，是 RL for reasoning 的重要进展。

### 13.3 Re²: Recursive Reasoning
| 项目 | 内容 |
|------|------|
| Title | Re²: Recursive Reasoning for LLMs |
| 中文 | Re²：LLM 递归推理 |
| Affiliation | — |
| arXiv | — |

**核心创新**: 提出递归推理框架，LLM 将复杂问题递归分解为子问题，在每个层级进行推理。

### 13.4 SFPO / CAPO / PoLR
| 项目 | 内容 |
|------|------|
| Title | SFPO: Stepwise Fine-tuning with Process Optimization |
| 中文 | SFPO：分步过程优化微调 |
| Title | CAPO: Contrastive Alignment for Preference Optimization |
| 中文 | CAPO：对比对齐偏好优化 |
| Title | PoLR: Policy Optimization with Learned Rewards |
| 中文 | PoLR：基于学习奖励的策略优化 |

这三篇论文代表了 RLVR 优化方法的三个方向，均在 GRPO 基础上提出了改进方案。

### 13.5 Beyond Entropy: Token-Level Distributional Deviations for LLM Reasoning
| 项目 | 内容 |
|------|------|
| Title | Beyond Entropy: Learning from Token-Level Distributional Deviations for LLM Reasoning |
| 中文 | 超越熵：从 Token 级分布偏差学习 LLM 推理 |
| Affiliation | — |
| arXiv | 2606.19771 |

**核心创新**: 提出在 token 级别建模 LLM 的分布偏差，而不是使用聚合指标（如熵）来检测推理错误。在推理质量检测方面显著优于基于熵的方法。

---

## 14. Agent Systems

### 14.1 Code as Agent Harness (Meta / UIUC / Stanford)
| 项目 | 内容 |
|------|------|
| Title | Code as Agent Harness: Toward Executable, Verifiable, and Stateful Agent Systems |
| 中文 | 代码作为 Agent 框架：面向可执行、可验证、有状态的 Agent 系统 |
| Affiliation | UIUC / Meta / Stanford |
| arXiv | 2605.18747 |
| Code | github.com/YennNing/Awesome-Code-as-Agent-Harness-Papers |

**核心贡献**: 全面的综述，提出"代码作为 agent harness"的统一视角。将 agent 系统分为三层：
1. **Harness Interface** — 代码连接推理、行动和环境建模
2. **Harness Mechanisms** — 规划、记忆、工具使用、反馈驱动控制
3. **Scaling the Harness** — 单 Agent → 多 Agent，共享代码制品

### 14.2 MEM1 Agent Memory-Reasoning (ICLR 2026)
参见 Outstanding Papers 部分。

### 14.3 Foundation Protocol (Tencent / HKUST / UIUC)
| 项目 | 内容 |
|------|------|
| Title | Foundation Protocol: Agentic Society Coordination |
| 中文 | Foundation Protocol：Agent 社会协调协议 |
| Affiliation | Tencent / HKUST / UIUC |
| arXiv | 2605.23218 |

**核心创新**: 提出 agent 社会中的协调协议，定义 agent 之间的通信规范、权限管理和协作机制。类似于人类社会中的法律和协议。

### 14.4 SkillOpt (Microsoft Research Asia)
| 项目 | 内容 |
|------|------|
| Title | SkillOpt: Self-Evolving Agent Skills |
| 中文 | SkillOpt：自进化 Agent 技能 |
| Affiliation | Microsoft Research Asia |
| arXiv | 2605.23904 |

**核心创新**: Agent 在任务执行过程中自动发现、学习和优化技能。采用技能库 + 技能检索 + 技能适应的三阶段框架。

### 14.5 DSG: Decoupling Search from Reasoning for LLM Agents
| 项目 | 内容 |
|------|------|
| Title | Decoupled Search Grounding (DSG): Vendor-Agnostic Grounding Architecture for LLM Agents |
| 中文 | DSG：面向 LLM Agent 的供应商无关定位架构 |
| Affiliation | — |
| arXiv | 2606.20244 |

**核心创新**: 将实时搜索从 LLM 推理中解耦，实现 vendor-agnostic grounding。在 SimpleQA 上达到近原生准确度，同时搜索成本降低 91%，延迟降低 68%。

### 14.6 LedgerAgent: Structured State for Policy-Adherent Tool-Calling
| 项目 | 内容 |
|------|------|
| Title | LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents |
| 中文 | LedgerAgent：面向策略合规工具调用的结构化状态 |
| Affiliation | — |
| arXiv | 2606.20244 |

**核心创新**: 引入"账本"（ledger）概念来维护 agent 的任务状态，确保工具调用严格遵守领域策略，特别适用于客户服务场景。

---

## 15. Generative Models & Diffusion

### 15.1 DiffusionGemma (Google DeepMind)
| 项目 | 内容 |
|------|------|
| Title | DiffusionGemma: A Family of Efficient Diffusion Language Models |
| 中文 | DiffusionGemma：高效扩散语言模型家族 |
| Affiliation | Google DeepMind |
| arXiv | — |

**核心创新**: Google 推出的扩散语言模型系列，在文本生成质量和效率之间取得了平衡。与自回归模型相比，扩散模型在可控生成和双向上下文理解方面有优势。

### 15.2 Precise SDE-Consistent Sampling (ByteDance)
| 项目 | 内容 |
|------|------|
| Title | Precise: SDE-Consistent Sampling for Flow-Matching RL |
| 中文 | Precise：面向流匹配 RL 的 SDE 一致采样 |
| Affiliation | ByteDance |
| arXiv | 2605.23522 |

**核心创新**: 提出 SDE-consistent 采样方法，确保 flow-matching 模型在 RL 训练中的采样轨迹与 SDE 解一致，提高 RL 训练的稳定性。

### 15.3 Self-Flow Matching (ICML 2026)
参见 ICML 2026 部分。

### 15.4 SeaCache / SenCache (CVPR 2026)
两颗加速扩散模型推理的缓存方法，SeaCache 利用频谱演化感知缓存，SenCache 使用敏感度感知缓存。

### 15.5 FlowEdit: Pronunciation Adaptation for Flow-Matching TTS
| 项目 | 内容 |
|------|------|
| Title | FlowEdit: Associative Memory for Lifelong Pronunciation Adaptation in Flow-Matching TTS |
| 中文 | FlowEdit：流匹配 TTS 中终身发音适应的联想记忆 |
| Affiliation | — |
| arXiv | 2606.20244 |

---

## 16. CTR Prediction & Advertising

### 16.1 Token Factory (Google)
| 项目 | 内容 |
|------|------|
| Title | Token Factory: Efficiently Integrating Diverse Signals into Large Recommendation Models |
| 中文 | Token Factory：高效集成多样化信号到大推荐模型 |
| Affiliation | Google |
| arXiv | 2606.19635 |

**核心创新**: 提出"软 token"概念，将推荐中的多种信号（用户行为、物品属性、上下文特征）统一编码为 token 序列，输入大推荐模型（LRM）。已在 Google 生产环境中部署。

### 16.2 G2Rec (Meta)
| 项目 | 内容 |
|------|------|
| Title | G2Rec: Scalable Framework for Graph-Based Generative Recommendation |
| 中文 | G2Rec：基于图的生成式推荐可扩展框架 |
| Affiliation | Meta |
| arXiv | 2606.20244 |

**核心创新**: 统一图结构的用户协同参与建模与语义 tokenization，为工业级生成式推荐提供可扩展框架。在 Meta 多个产品面部署。

### 16.3 FEDIN (Tencent)
| 项目 | 内容 |
|------|------|
| Title | FEDIN: Frequency-Enhanced Deep Interest Network for CTR Prediction |
| 中文 | FEDIN：频率增强的深度兴趣网络用于 CTR 预估 |
| Affiliation | Tencent |
| arXiv | 2605.01726 |

**核心创新**: 在时域行为数据中引入频域分析，捕获用户兴趣的周期性模式。

### 16.4 Unified Value Alignment for Generative Recommendation (Tencent)
| 项目 | 内容 |
|------|------|
| Title | Unified Value Alignment for Generative Recommendation in Industrial Advertising |
| 中文 | 工业广告生成式推荐中的统一价值对齐 |
| Affiliation | Tencent |
| arXiv | 2605.05803 |

### 16.5 RecGPT-Mobile (Alibaba Taobao)
| 项目 | 内容 |
|------|------|
| Title | RecGPT-Mobile: On-Device LLMs for User Intent Understanding in Taobao Feed |
| 中文 | RecGPT-Mobile：淘宝信息流中用户意图理解的端侧 LLM |
| Affiliation | Alibaba / Taobao & Tmall Group |
| arXiv | 2605.04726 |

### 16.6 CS3 (Kuaishou)
| 项目 | 内容 |
|------|------|
| Title | CS3: Efficient Online Capability Synergy for Two-Tower Recommendation |
| 中文 | CS3：双塔推荐的高效在线能力协同 |
| Affiliation | Kuaishou |
| arXiv | 2604.19269 |

### 16.7 Uncertainty-Calibrated Recommendations for Low-Active Users (ByteDance/TikTok)
| 项目 | 内容 |
|------|------|
| Title | Uncertainty-Calibrated Recommendations for Low-Active Users |
| 中文 | 面向低活跃用户的不确定性校准推荐 |
| Affiliation | ByteDance / TikTok |
| arXiv | 2605.17788 |

**核心创新**: 解决推荐系统中低活跃用户（LAU）的可靠性问题，提出不确定性校准方法。在冷启动和稀疏交互场景下显著提升推荐质量。

### 16.8 ITNet: Unified Integral Transform Networks
| 项目 | 内容 |
|------|------|
| Title | ITNet: Unified Integral Transform Networks Subsuming Convolution, Attention, and RNN |
| 中文 | ITNet：统一积分变换网络，包含卷积、注意力和 RNN |
| Affiliation | — |
| arXiv | 2606.20244 |

**核心创新**: 提出统一的积分变换框架，从数学上统一了卷积、注意力机制和 RNN 三种核心操作。在多种任务上达到或超越各自专用架构的性能。

---

## 17. Frontier Model Tech Reports

### 17.1 DeepSeek V4 (2026-04)
- 1.6T MoE，引入 CSA（Cross-Self Attention）和 HCA（Hybrid Cross Attention）
- 1M context window
- 使用 Muon 优化器替代 AdamW
- 价格 $0.87/M output tokens（最具性价比的旗舰模型）

### 17.2 GPT-5.5 (OpenAI, 2026-04)
- Router-based unified system（根据任务路由到不同子模型）
- 1M context
- $5/M（standard）/$30/M（pro）output tokens
- Agentic Coding 能力显著提升

### 17.3 Gemini 3.1 Pro (Google DeepMind)
- 2M context MoE
- 多模态原生（文本+图像+音频+视频）
- Dynamic thinking mode

### 17.4 Claude Opus 4.8 / Fable 5 / Mythos 5 (Anthropic)
- Opus 4.8: 长上下文和多轮对话优化
- Fable 5: 创造性写作和复杂推理
- Mythos 5: 安全对齐的最高水平

### 17.5 Llama 4 (Meta, 2025-04)
- Scout (109B-A17B): 10M context
- Maverick (402B-A48B): 1M context
- Behemoth (2T): 训练中
- MoE + Early fusion 多模态

### 17.6 Qwen3 / Qwen3.5-Omni / Qwen3.7 Max (Alibaba)
- Qwen3: 119 语言，hybrid thinking mode
- Qwen3.5-Omni: OmniMoE，SWE-Verified 82%
- Qwen3.7 Max: 1M context

### 17.7 Mistral Large 3 / Magistral / Medium 3.5
- Large 3: 675B MoE, Apache 2.0
- Magistral: Cascade Distillation + 纯 RL 推理
- Medium 3.5: 中间规模专精模型

### 17.8 Kimi K2 → K2.5 → K2.6 → K2.7 Code (Moonshot AI)
- K2: 1T MoE, MuonClip 优化器
- K2.5/K2.6: Agentic 能力增强
- K2.7 Code: 代码能力专项优化

---

## 18. Key Trends Summary

| 趋势 | 描述 | 涉及会议/论文 |
|------|------|-------------|
| **推理模型与测试时计算** | Reasoning models 成为标配，test-time compute scaling 持续探索 | NeurIPS 2025, ICLR 2026, ICML 2026 |
| **RL for LLM (RLVR)** | Verifiable reward RL 成为主要 post-training 方法 | 跨会议 |
| **门控注意力创新** | Gated Attention (NeurIPS Best) 标志 attention 进入新阶段 | NeurIPS 2025 |
| **混合架构 (SSM+Attention)** | Mamba-3、Nemotron 3 验证 Mamba-Attention 混合可行性 | ICLR 2026, ICML 2026 |
| **CTR Scaling Law 成熟** | CTR Scaling 成为一个独立研究方向 | KDD 2026, RecSys 2025, CIKM 2025 |
| **生成式推荐产业化** | Token Factory (Google)、G2Rec (Meta)、NEZHA (Taobao) | WWW 2026, KDD 2026 |
| **Agent 系统爆发** | ICML 2026 有 465 篇 agent 相关论文 | 跨会议 |
| **Diffusion LLM 崛起** | DiffusionGemma (Google)、LLaDA-V (CVPR 2026) | CVPR 2026 |
| **4D 视觉与 3D 生成** | D4RT (CVPR Best)、SAM 3D (Meta) | CVPR 2026 |
| **游戏 Agent 通用化** | NitroGen (NVIDIA)、自对弈涌现推理 | CVPR 2026, ICLR 2026 |
| **MoE 全面主流化** | 几乎所有旗舰模型采用 MoE | 所有会议 |
| **自对弈与游戏 RL** | 游戏作为 LLM 推理的可扩展训练信号 | ICLR 2026, ICML 2026 |

---

## 19. 实验室论文覆盖

| 实验室 | 代表论文 | 方向 |
|--------|---------|------|
| Google DeepMind | D4RT (CVPR Best), DiffusionGemma, Gemini 3.1, Token Factory | 4D 视觉、扩散 LM、推荐 |
| OpenAI | GPT-5.5 | Frontier Model |
| Meta AI | G2Rec, SAM 3D, ActionMesh, Code as Agent Harness, Llama 4 | 生成式推荐、3D 视觉、Agent |
| Microsoft Research | SkillOpt, Inductive Deductive Synthesis | Agent 技能 |
| ByteDance | TikTok Negatives (RecSys), Precise, HyFormer, TokenMixer | CTR、生成模型 |
| Alibaba | NEZHA (WWW), ALIVE (ICML), Gated Attention (NeurIPS B) | 推荐、游戏、Attention |
| Tencent | RankUp (KDD), FEDIN, TokenFormer, GenCI, Foundation Protocol | CTR、Agent |
| Kuaishou | DIF (KDD), CS3, VQL | CTR 推荐 |
| NVIDIA | NitroGen (CVPR), Nemotron 3, PixelDiT (CVPR) | 游戏、MoE 架构 |
| Anthropic | Claude Opus 4.8 / Fable 5 / Mythos 5 | Frontier Model |
| Apple | Speculative Streaming (EMNLP/NeurIPS) | LLM 推理加速 |
| Baidu | ERNIE 5.0 | LLM |
| Netflix | Scaling Generative Recommenders | 推荐系统 |
| Amazon | Prime Video RecSys | 推荐系统 |
| Zhipu AI | GLM-5 | LLM + Agent |
| Moonshot AI | Kimi K2.7 Code | LLM + 代码 |
| Sony AI | VibeToken-Gen (CVPR) | 高效视觉生成 |
| Mistral AI | Ministral 3, Magistral | 小模型推理 |
| UIUC/Meta/Stanford | Code as Agent Harness | Agent 综述 |
| Airbnb | JourneyFormer (KDD) | 生成式推荐 |

---

## 附录: 推荐阅读

1. Sebastian Raschka LLM Research Papers 2026 List: https://magazine.sebastianraschka.com/p/llm-research-papers-2026-part1
2. ICML 2026 Accepted Papers: https://icml.cc/virtual/2026/papers.html
3. CVPR 2026 Best Papers: https://cvpr.thecvf.com/virtual/2026/papers.html
4. NeurIPS 2025 Proceedings: https://neurips.cc/virtual/2025/papers.html
5. EMNLP 2025 Proceedings: https://aclanthology.org/venues/emnlp/
6. Paper Copilot ICML 2026: https://papercopilot.com/paper-list/icml-paper-list/icml-2026-paper-list/
7. ICML 2026 汇总: https://hongsong-wang.github.io/ICML2026/
8. Awesome Code as Agent Harness: https://github.com/YennNing/Awesome-Code-as-Agent-Harness-Papers
9. Awesome-Recsys: https://github.com/ceo21ckim/Awesome-Recsys
10. MIT Diffusion Models Course: https://diffusion.csail.mit.edu/2026/
