---
title: "顶会论文专题报告 — 2026年6月全面版 (v2)"
type: synthesis
created: 2026-06-22
updated: 2026-06-22
sources: [arxiv]
tags: [conference-digest, icml-2026, aaai-2026, neurips-2025, iclr-2026, kdd-2026, cvpr-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2025, recsys-2025]
---

# 顶会论文专题报告 — 2026年6月全面版 (v2)

> **日期**: 2026-06-22
> **范围**: 13 会议/venue, 80+ 论文, 15+ 实验室 (Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, Netflix, NVIDIA, Anthropic, Apple, Amazon, Tsinghua, Stanford, UC Berkeley, CMU)
> **分类**: LLM 架构 / 推理 & RL / Agent 系统 / CTR & 推荐系统 / 生成模型 & 扩散 / 代码 & 软件工程 / Benchmark & 评估 / 游戏 & 决策 / 序列建模 & State Space / 多模态 / 检索增强 (RAG) / 安全 & 对齐 / 3D 视觉 & 场景重建

---

## 1. ICML 2026 — Highlights & Outstanding Papers

**基本信息**: 2026年7月6-11日, 首尔, 韩国 | 23,918 投稿, 6,352 接收 (26.6%) | 168 Oral (0.7%)

### 1.1 Agentic Verifier — Execution-based Re-ranking for Competitive Coding
| 项目 | 内容 |
|------|------|
| Title | Agentic Verifier: Execution-based Re-ranking for Competitive Coding |
| 中文 | Agentic Verifier：基于执行的竞赛编程重排序 |
| Affiliation | — |
| arXiv | — |

**核心创新**: 针对 LLM 代码生成中的多采样场景，提出基于执行结果的 Agentic Verifier 进行重排序，替代传统的 pass@k 投票机制。利用执行反馈信号（测试通过/失败、错误类型）训练 verifier，在 Competitive Programming 数据集上实现显著提升。

### 1.2 Lagrangian Safe RL via Diffusion Models
| 项目 | 内容 |
|------|------|
| Title | How Does the Lagrangian Guide Safe Reinforcement Learning through Diffusion Models? |
| 中文 | 拉格朗日方法如何通过扩散模型引导安全强化学习 |
| Affiliation | UCL |
| arXiv | — |

**核心创新**: 将拉格朗日对偶方法与扩散模型结合，在安全约束强化学习场景中同时建模策略分布和约束边界。在 Safety Gym 等基准上实现比传统 safe RL 方法更优的 constraint satisfaction 表现。

### 1.3 Emergent Alignment via Competition
| 项目 | 内容 |
|------|------|
| Title | Emergent Alignment via Competition |
| 中文 | 通过竞争涌现对齐 |
| Affiliation | UPenn / 多机构 |
| arXiv | 2509.15090 |

**核心创新**: 提出通过多智能体竞争机制涌现对齐行为，无需显式的人类反馈或奖励建模。多个 LLM 在竞争性交互中自发学会遵循社会规范和合作行为。

### 1.4 Beyond Test-Time Training: Optimal Control Reasoning
| 项目 | 内容 |
|------|------|
| Title | Beyond Test-Time Training: Learning to Reason via Hardware-Efficient Optimal Control |
| 中文 | 超越测试时训练：通过硬件高效最优控制学习推理 |
| Affiliation | Meta AI / 多机构 |
| arXiv | 2603.09221 |

**核心创新**: 将推理过程建模为最优控制问题，提出硬件高效的控制视角来训练 LLM 的推理能力。与传统的 CoT 和监督微调不同，该方法利用控制理论的工具优化推理路径。

### 1.5 CORAL — Correctness-Optimized Residual Activation Lens
| 项目 | 内容 |
|------|------|
| Title | CORAL: Correctness-Optimized Residual Activation Lens — Transferrable and Calibration-Aware Inference-Time Steering |
| 中文 | CORAL：面向正确性优化的残差激活透镜 — 可迁移且校准感知的推理时引导 |
| Affiliation | UPenn |
| arXiv | 2602.06022 |

**核心创新**: 通过分析残差激活空间的校正方向实现推理时引导（inference-time steering），无需额外训练即可迁移到不同模型和任务。

### 1.6 FPTQuant — Efficient 4-bit Quantization
| 项目 | 内容 |
|------|------|
| Title | FPTQuant: Efficient 4-bit Quantization for Transformer Models |
| 中文 | FPTQuant：高效的 Transformer 4-bit 量化 |
| Affiliation | — |
| arXiv | — |

**核心创新**: 提出新型 4-bit 量化方法，利用浮点转定点技术在不显著牺牲精度的情况下实现 4× 模型压缩。

### 1.7 Test-Time Anchoring for Discrete Diffusion
| 项目 | 内容 |
|------|------|
| Title | Test-Time Anchoring for Discrete Diffusion Posterior Sampling |
| 中文 | 离散扩散后验采样的测试时锚定 |
| Affiliation | — |
| arXiv | — |

**核心创新**: 提出 Anchored Posterior Sampling (APS)，通过 quantized expectation 和 anchor guidance 两个关键创新解决离散扩散后验采样中的信号稀疏和维度灾难问题。

### 1.8 Bandit Social Learning
| 项目 | 内容 |
|------|------|
| Title | Bandit Social Learning with Exploration Episodes |
| 中文 | 带探索阶段的 Bandit 社会学习 |
| Affiliation | UPenn |
| arXiv | 2602.05835 |

**核心创新**: 将社会学习与 bandit 探索结合，研究智能体在社交网络中如何平衡自我探索和社会信息利用。

---

## 2. AAAI 2026 — Outstanding Papers & Highlights

**基本信息**: 2026年1月20-27日, 新加坡 | 23,680 投稿, 4,167 接收 (17.6%) | 主题: "Creating Collaborative Bridges Within and Beyond AI"

### 2.1 AI-Assisted Peer Review Pilot
| 项目 | 内容 |
|------|------|
| Title | AI-Assisted Peer Review Pilot |
| 中文 | AI辅助同行评审试点 |
| Affiliation | AAAI 2026 + OpenAI + 多所大学 |
| Link | aaai.org |

**核心创新**: AAAI 2026 进行了史上最大规模的 AI 辅助同行评审实验，为全部 22,977 篇论文生成了 AI 评审报告。AI 报告带有明确标识，不提供分数，不替代人类评审。

### 2.2 Resource Efficient Sleep Staging via Multi-Level Masking
| 项目 | 内容 |
|------|------|
| Title | Resource Efficient Sleep Staging via Multi-Level Masking and Prompt Learning |
| 中文 | 基于多级掩码和提示学习的资源高效睡眠分期 |
| Affiliation | 多机构 |
| Link | ojs.aaai.org |

**核心创新**: 提出 Mask-Aware Sleep Staging (MASS) 框架，通过多级掩码策略和层次化提示学习，在极少量 EEG 信号条件下实现可靠的睡眠分期，适用于可穿戴设备。

### 2.3 Agentic AI Benchmarks for Enterprise Tasks
| 项目 | 内容 |
|------|------|
| Title | Agentic AI Benchmarks and Applications for Enterprise Tasks |
| 中文 | 面向企业任务的 Agentic AI 基准与应用 |
| Affiliation | CMU / Keio / Fujitsu |
| Link | aaai.org |

**核心创新**: 提出了针对企业场景的 Agentic AI 评估框架，涵盖任务规划、工具使用、多轮对话等核心能力维度。

### 2.4 Theory of Mind for AI (ToM4AI)
| 项目 | 内容 |
|------|------|
| Title | Theory of Mind for AI — Workshop Highlights |
| 中文 | 面向 AI 的心智理论 |
| Affiliation | CMU / Oxford / BIU |
| Link | aaai.org |

**核心创新**: 探讨 LLM 的心智推理能力差距 — 当前模型缺乏个体层面、人际层面和文化层面的社会推理能力。提出 MindSpace Theory 框架。

---

## 3. NeurIPS 2025 — Best Papers & Highlights

**基本信息**: 2025年12月2-7日, 圣地亚哥 | ~15,671 投稿, ~4,035 接收 (25.75%)

### 3.1 Gated Attention — Attention Sink Removal
| 项目 | 内容 |
|------|------|
| Title | Gated Attention: Attention Sink Removal via Gating Mechanism |
| 中文 | 门控注意力 — 通过门控机制消除 Attention Sink |
| Affiliation | Alibaba / 多机构 |
| Award | Best Paper |

**核心创新**: 在 attention 计算中引入可学习的门控信号，从根本上消除 attention sink 现象。长上下文 perplexity 显著低于标准 attention，KV cache 压缩效率提升 2-4×。

### 3.2 Beyond Reasoning — RL Unlocks Parametric Knowledge
| 项目 | 内容 |
|------|------|
| Title | Beyond Reasoning: Reinforcement Learning Unlocks Parametric Knowledge in Language Models |
| 中文 | 超越推理：强化学习解锁语言模型中的参数化知识 |
| Affiliation | Tsinghua / 多机构 |
| Award | Best Paper Runner-up |

**核心创新**: 证明 RL 不仅仅是提升推理能力 — 可以教会模型更好利用已有知识。提出 value-action gap 理论框架。发现 RLVR 中的 diversity collapse 现象。

### 3.3 1,000-Layer RL Networks
| 项目 | 内容 |
|------|------|
| Title | Deep RL Networks at 1,024 Layers: Scaling Depth in Reinforcement Learning |
| 中文 | 1024 层深度强化学习网络 |
| Affiliation | 多机构 (UW, CMU) |
| Award | Best Paper |

**核心创新**: 打破了 RL 网络应保持浅层的传统假设，将网络扩展到 1,024 层，在 goal-conditioned self-supervised RL 中实现 2× 到 50× 的性能提升。

### 3.4 Hivemind — Social Dynamics of Foundation Models
| 项目 | 内容 |
|------|------|
| Title | Hivemind: Social Dynamics of Foundation Models |
| 中文 | 蜂群思维：基础模型的社会动力学 |
| Affiliation | 多机构 |
| Award | Best Paper |

**核心创新**: 研究基础模型在部署后产生的社会影响 — 模型之间的输出趋同现象，以及对文化多样性的潜在风险。

### 3.5 Transductive Online Learning — 30-Year Problem Solved
| 项目 | 内容 |
|------|------|
| Title | Transductive Online Learning — A 30-Year Open Problem Solved |
| 中文 | 传导在线学习 — 解决 30 年开放问题 |
| Affiliation | 多机构 |
| Award | Best Paper |

**核心创新**: 解决了在线学习理论中一个长达 30 年的开放问题，将 transductive learning 与 online learning 统一。

### 3.6 Speculative Streaming (Apple)
| 项目 | 内容 |
|------|------|
| Title | Speculative Streaming: Fast LLM Inference without Auxiliary Models |
| 中文 | 推测流式推理：无辅助模型的快速 LLM 推理 |
| Affiliation | Apple |
| arXiv | — |

**核心创新**: 利用 LLM 自身的中间层表示进行草稿生成，无需辅助小模型。实现 2-3× 推理加速。

---

## 4. ICLR 2026 — Outstanding Papers

**基本信息**: 2026年4月22-27日, 里约热内卢 | ~11,672 投稿, ~5,300+ 接收

### 4.1 Mamba-3 — Improved SSM Sequence Modeling
| 项目 | 内容 |
|------|------|
| Title | Mamba-3: Improved Sequence Modeling using State Space Principles |
| 中文 | Mamba-3：利用状态空间原理改进序列建模 |
| Affiliation | CMU / Princeton / 多机构 |
| arXiv | — |
| Award | ICLR 2026 Oral |

**核心创新**: 提出三个核心改进：1) 更富表达力的递推公式；2) 复数状态更新规则实现更丰富的状态追踪；3) 多输入多输出 (MIMO) 公式化。Mamba-3 在检索、状态追踪和语言建模任务上达到新的 Pareto 前沿。

### 4.2 Transformers are Inherently Succinct
| 项目 | 内容 |
|------|------|
| Title | Transformers are Inherently Succinct |
| 中文 | Transformer 本质上是简洁的 |
| Affiliation | 多机构 |
| Award | ICLR 2026 Outstanding |

**核心创新**: 从理论角度证明 Transformer 在表示复杂函数时的内在简洁性优势，比 RNN 和 SSM 用更少参数表示相同函数类。

### 4.3 MEM1: Memory-Reasoning Synergy for Agents
| 项目 | 内容 |
|------|------|
| Title | MEM1: Memory-Reasoning Synergy for Long-Horizon Agents |
| 中文 | MEM1：面向长程 Agent 的记忆-推理协同 |
| Affiliation | — |
| Award | ICLR 2026 Outstanding |

**核心创新**: 提出记忆-推理协同架构，将外部记忆系统与 LLM 推理循环深度整合。在长程任务中显著优于 MemGPT 等方法。

### 4.4 LeanPremise + LeanHammer — Neural Theorem Proving
| 项目 | 内容 |
|------|------|
| Title | LeanPremise: Neural Premise Selection for Lean — End-to-End Domain General Hammer |
| 中文 | LeanPremise：面向 Lean 证明助手的神经前提选择 |
| Affiliation | 多机构 |
| Award | ICLR 2026 Oral |

**核心创新**: 首个端到端领域通用的 Lean hammer 系统。比现有前提选择器多解决 21% 的目标，连接神经检索与符号推理。

### 4.5 AccelOpt — Self-Improving LLM Agent for AI Accelerator Kernel Optimization
| 项目 | 内容 |
|------|------|
| Title | AccelOpt: A Self-Improving LLM Agentic System for AI Accelerator Kernel Optimization |
| 中文 | AccelOpt：面向 AI 加速器内核优化的自改进 LLM Agent 系统 |
| Affiliation | Stanford |
| arXiv | 2511.15915 |

**核心创新**: 自改进 LLM agent 自动优化 AI 加速器的 kernel 代码，通过代码生成-评测-迭代循环实现超越手写 kernel 的性能。

### 4.6 Information Theoretic Perspective on Agentic Systems
| 项目 | 内容 |
|------|------|
| Title | An Information Theoretic Perspective on Agentic System Design |
| 中文 | 智能体系统设计的信息论视角 |
| Affiliation | Stanford (Hazy Research) |
| arXiv | 2512.21720 |

**核心创新**: 利用信息瓶颈和率失真理论分析 agentic 系统中的协作效率，提出 agent 协作的 scaling laws。

---

## 5. CVPR 2026 — Best Papers & Highlights

**基本信息**: 2026年6月, 美国 | 16,092 投稿, 4,089 接收

### 5.1 D4RT — Dynamic 4D Scene Reconstruction
| 项目 | 内容 |
|------|------|
| Title | Efficiently Reconstructing Dynamic Scenes One D4RT at a Time |
| 中文 | 高效重建动态场景 — D4RT |
| Affiliation | Google DeepMind / UCL / Oxford |
| Link | openaccess.thecvf.com |
| Award | **CVPR 2026 Best Paper** |

**核心创新**: 基于统一 Transformer 架构，从视频中同时估计深度、时空对应和完整相机参数。可独立高效查询 4D 空间中任意点在任意时刻的 3D 位置。训练和推理异常高效。

### 5.2 Native & Compact Structured Latents for 3D Generation
| 项目 | 内容 |
|------|------|
| Title | Native and Compact Structured Latents for 3D Generation |
| 中文 | 面向 3D 生成的原生紧凑结构潜变量 |
| Affiliation | Tsinghua / Microsoft Research / USTC / Microsoft AI |
| Award | **CVPR 2026 Best Student Paper** |

**核心创新**: 显著提升 AI 生成 3D 资产的质量和真实感，提出新的 3D 生成方法。

### 5.3 NitroGen — Open Foundation Model for Generalist Gaming Agents
| 项目 | 内容 |
|------|------|
| Title | NitroGen: An Open Foundation Model for Generalist Gaming Agents |
| 中文 | NitroGen：面向通用游戏智能体的开放基础模型 |
| Affiliation | 多机构 |
| Award | CVPR 2026 Best Paper Honorable Mention |

**核心创新**: 首个面向通用游戏智能体的开放基础模型，支持多种游戏环境和任务类型。

### 5.4 VLA-World — Vision-Language-Action World Models for Autonomous Driving
| 项目 | 内容 |
|------|------|
| Title | Learning Vision-Language-Action World Models for Autonomous Driving |
| 中文 | 面向自动驾驶的视觉-语言-行动世界模型 |
| Affiliation | 多机构 |
| arXiv | 2604.09059 |

**核心创新**: VLA-World 统一预测性想象与反思性推理：通过行动轨迹生成下一帧图像，然后对自生成的未来想象进行推理以优化轨迹。在规划和新框架生成基准上超越 SOTA。

### 5.5 OmniVGGT — Multi-Modal Spatial Foundation Model
| 项目 | 内容 |
|------|------|
| Title | OmniVGGT: A Foundation Model for Arbitrary Multi-Geometric Modalities |
| 中文 | OmniVGGT：任意多几何模态的基础模型 |
| Affiliation | — |

**核心创新**: 提出 GeoAdapter 编码深度和相机内外参，使用零初始化卷积渐进注入几何信息。支持训练和推理时任意数量的几何模态输入。

### 5.6 E-RayZer — Self-supervised 3D Reconstruction as Visual Pre-training
| 项目 | 内容 |
|------|------|
| Title | E-RayZer: Self-supervised 3D Reconstruction as Spatial Visual Pre-training |
| 中文 | E-RayZer：自监督 3D 重建作为空间视觉预训练 |
| Affiliation | 多机构 (CMU, Meta) |

**核心创新**: 第一个在 3D 空间中直接进行自监督重建的大规模 3D 视觉模型，无需标注数据。

---

## 6. KDD 2026 — Highlights

**基本信息**: 2026年8月9-13日, 济州岛, 韩国 | 1,215 投稿 (Cycle 1), 256 接收 (21%)

### 6.1 DIF — Denoised Item-based Filtering for Cold-Start (Kuaishou)
| 项目 | 内容 |
|------|------|
| Title | Denoised Item-based Filtering for Cold-Start Recommendation |
| 中文 | 面向冷启动物品推荐的去噪物品基过滤 |
| Affiliation | Kuaishou |
| arXiv | — |

**核心创新**: 针对推荐系统冷启动问题，提出去噪物品基过滤方法，有效降低稀疏交互中的噪声信号，在 Kuaishou 短视频推荐场景中取得显著提升。

### 6.2 RankMixer / TokenMixer — ByteDance Token-Based Ranking Series
| 项目 | 内容 |
|------|------|
| Title | RankMixer: Scaling Up Ranking Models in Industrial Recommenders |
| 中文 | RankMixer：工业推荐系统中排序模型的规模化 |
| Affiliation | ByteDance |
| Venue | KDD 2025 / KDD 2026 |

**核心创新**:
- **RankMixer** (KDD 2025): 硬件感知的 token mixing 设计，用 per-token 参数化 FFN + HeadMixing 替代 attention
- **TokenMixer-Large** (arXiv 2026): 扩展到 **7B 在线 / 15B 离线参数**，修复残差错位，加入 inter-layer residuals + Sparse Per-token MoE，MFU 达 60%。电商 GMV **+2.98%**，广告 ADSS **+2.0%**

### 6.3 Exploring Scaling Laws of CTR Model
| 项目 | 内容 |
|------|------|
| Title | Exploring Scaling Laws of CTR Model for Online Performance Improvement |
| 中文 | CTR 模型规模定律探索与在线性能提升 |
| Affiliation | ByteDance / 多机构 |
| arXiv | 2508.15326 |

**核心创新**: 首次系统研究了 CTR 模型中的 scaling laws，揭示了模型参数量、数据量与在线性能之间的关系。

### 6.4 Beyond Static Best-of-N — Bayesian List-wise Alignment for Rec
| 项目 | 内容 |
|------|------|
| Title | Beyond Static Best-of-N: Bayesian List-wise Alignment for LLM-based Recommendation |
| 中文 | 超越静态 Best-of-N：面向 LLM 推荐的贝叶斯列表级对齐 |
| Affiliation | USTC / 多机构 |
| Venue | SIGIR 2026 |

**核心创新**: 提出贝叶斯列表级对齐方法，替代传统的 Best-of-N 采样策略，在 LLM-based 推荐中实现更稳定和高质量的推荐列表。

---

## 7. ACL 2026 — Highlights

**基本信息**: 2026年7月, 圣地亚哥

### 7.1 Code as Agent Harness — Unified View
| 项目 | 内容 |
|------|------|
| Title | Code as Agent Harness: Toward Executable, Verifiable, and Stateful Agent Systems |
| 中文 | 代码作为 Agent 框架：走向可执行、可验证、有状态的 Agent 系统 |
| Affiliation | UIUC / Meta / Stanford |
| arXiv | 2605.18747 |

**核心创新**: 系统性地提出 "code as agent harness" 统一视角，代码不仅是目标输出，更是 agent 推理、行动、环境建模和基于执行的验证的操作基础。围绕三个层次组织：harness interface、harness mechanisms、scaling harness。

### 7.2 A-MEM — Agentic Memory for LLM Agents
| 项目 | 内容 |
|------|------|
| Title | A-MEM: Agentic Memory for LLM Agents |
| 中文 | A-MEM：LLM Agent 的 Agentic 记忆系统 |
| Affiliation | — |

**核心创新**: 受 Zettelkasten 启发的 agentic memory 系统，每个记忆条目自动生成结构化笔记，动态建立记忆间链接，在 LoCoMo 长对话 QA 基准上大幅超越 MemGPT。

### 7.3 AgentAuditor — Safety/Security Evaluation for LLM Agents
| 项目 | 内容 |
|------|------|
| Title | AgentAuditor: Human-Level Safety and Security Evaluation for LLM Agents |
| 中文 | AgentAuditor：LLM Agent 的人类级安全评估 |
| Affiliation | — |
| arXiv | — |

**核心创新**: 免训练的记忆增强推理框架，引入 ASSEBench 基准（2,293 条记录，15 种风险类型，29 个场景），实现人类专家级的评估准确率。

### 7.4 AgentChangeBench — Multi-Dimensional Goal-Shift Robustness
| 项目 | 内容 |
|------|------|
| Title | AgentChangeBench: A Multi-Dimensional Evaluation Framework for Goal-Shift Robustness |
| 中文 | AgentChangeBench：目标漂移鲁棒性的多维评估框架 |
| Affiliation | — |

**核心创新**: 首个评估 LLM agent 在目标漂移条件下适应性的基准：315 基础任务 × 9 变体 = 2,835 序列，覆盖银行/零售/航空 3 个企业领域和 5 个用户画像。

---

## 8. EMNLP 2025 — Highlights

**基本信息**: 2025年11月4-9日, 苏州, 中国 | 8,174 投稿, 1,811 接收 (22.2%)

### 8.1 S1 — Simple Test-Time Scaling
| 项目 | 内容 |
|------|------|
| Title | S1: Simple Test-time Scaling |
| 中文 | S1：简单的测试时扩展 |
| Affiliation | Stanford |
| PubMed | emnlp-2025.emnlp-main.1025 |

**核心创新**: 提出简洁的 test-time compute scaling 方法，无需复杂推理框架即可提升 LLM 推理质量。

### 8.2 Bias after Prompting — Persistent Discrimination in LLMs
| 项目 | 内容 |
|------|------|
| Title | Bias after Prompting: Persistent Discrimination in Large Language Models |
| 中文 | 提示后的偏见：LLM 中的持久歧视 |
| Affiliation | Apple |
| Link | machinelearning.apple.com |

**核心创新**: 揭示即使通过提示试图消除 LLM 偏见，歧视性行为仍然存在的现象。偏见具有持久性特征。

### 8.3 Speculative Streaming (Apple)
| 项目 | 内容 |
|------|------|
| Title | Speculative Streaming: Efficient and Scalable Speculative Decoding |
| 中文 | 推测流式推理：高效可扩展的推测解码 |
| Affiliation | Apple |

**核心创新**: 使用 Multi-Stream Attention 实现无辅助模型的推测解码，在 EMNLP 2025 上展示。

### 8.4 Evaluating Evaluation Metrics — Hallucination Detection Mirage
| 项目 | 内容 |
|------|------|
| Title | Evaluating Evaluation Metrics — The Mirage of Hallucination Detection |
| 中文 | 评估评估指标 — 幻觉检测的幻象 |
| Affiliation | Apple |

**核心创新**: 系统分析现有幻觉检测指标的可靠性，揭示当前指标存在的系统性偏差。

### 8.5 MLX Demo
| 项目 | 内容 |
|------|------|
| Title | MLX: Large Model Inference and Training on Device |
| 中文 | MLX：设备端大模型推理与训练 |
| Affiliation | Apple |

**核心创新**: Apple 的 MLX 框架在 EMNLP 2025 上展示设备端大模型训练和推理能力。

---

## 9. SIGIR 2026 & WWW 2026 — Information Retrieval & Web

### 9.1 FollowTable — Instruction-Following Table Retrieval (SIGIR 2026)
| 项目 | 内容 |
|------|------|
| Title | FollowTable: A Benchmark for Instruction-Following Table Retrieval |
| 中文 | FollowTable：面向指令跟随的表格检索基准 |
| Affiliation | — |
| arXiv | 2605.00400 |

**核心创新**: 提出评估 LLM 在表格检索场景中遵循指令能力的新基准。

### 9.2 MUDY — Multi-Granular Dynamic Keyphrase Extraction (SIGIR 2026)
| 项目 | 内容 |
|------|------|
| Title | MUDY: Multi-Granular Dynamic Candidate Contextualization for Unsupervised Keyphrase Extraction |
| 中文 | MUDY：多粒度动态候选上下文化无监督关键词提取 |
| Affiliation | — |
| arXiv | 2605.00597 |

**核心创新**: 提出多粒度动态上下文化方法用于无监督关键词提取。

### 9.3 Bridging Explicit and Implicit Intent — Joint Search-Recommendation (WWW 2026)
| 项目 | 内容 |
|------|------|
| Title | Bridging Explicit and Implicit Intent: Unified Interest Generative Method for Joint Search-Recommendation Modeling |
| 中文 | 桥接显式和隐式意图：面向搜索-推荐联合建模的统一兴趣生成方法 |
| Affiliation | 多机构 |
| Link | www2026.thewebconf.org |

**核心创新**: 统一搜索和推荐的兴趣建模方法，同时捕捉显式搜索意图和隐式推荐兴趣。

### 9.4 FeDecider — LLM-Based Federated Cross-Domain Recommendation (WWW 2026)
| 项目 | 内容 |
|------|------|
| Title | FeDecider: An LLM-Based Framework for Federated Cross-Domain Recommendation |
| 中文 | FeDecider：基于 LLM 的联邦跨域推荐框架 |
| Affiliation | 多机构 |
| Link | www2026.thewebconf.org |

**核心创新**: 利用 LLM 的跨域知识迁移能力，在联邦学习框架下实现跨域推荐。

### 9.5 ScotRec — Social Chain-of-Thought LLM Reasoning for Recommendation (WWW 2026)
| 项目 | 内容 |
|------|------|
| Title | ScotRec: Social Chain-of-Thought LLM Reasoning for Recommendation |
| 中文 | ScotRec：面向推荐的社会链式推理 |
| Affiliation | 多机构 |
| Link | www2026.thewebconf.org |

**核心创新**: 将社交关系的 CoT 推理引入 LLM-based 推荐系统。

### 9.6 AgentDR — Dynamic Recommendation with LLM Agents (WWW 2026)
| 项目 | 内容 |
|------|------|
| Title | AgentDR: Dynamic Recommendation with Implicit Item-Item Relations via LLM-based Agents |
| 中文 | AgentDR：基于 LLM Agent 的动态推荐与隐式物品关系挖掘 |
| Affiliation | Amazon / 多机构 |
| Link | www2026.thewebconf.org |

**核心创新**: 利用 LLM agent 自动发现和利用隐式物品关系，实现动态推荐。

---

## 10. CIKM 2025 — Highlights

**基本信息**: 2025年11月10-14日, 首尔, 韩国 | 1,627 投稿, 443 接收 (27.23%)

### 10.1 LangPTune — Language-based User Profiles for Recommendation
| 项目 | 内容 |
|------|------|
| Title | LangPTune: Optimizing Language-based User Profiles for Recommendation |
| 中文 | LangPTune：面向推荐的语言用户画像优化 |
| Affiliation | Cornell |
| Link | cikm2025.org |

**核心创新**: 使用 LLM 生成和优化自然语言形式的用户画像，替代传统的 ID embedding 用于推荐系统。

### 10.2 Distribution-Guided Auto-Encoder for Multimodal Interest Fusion
| 项目 | 内容 |
|------|------|
| Title | Distribution-Guided Auto-Encoder for User Multimodal Interest Cross Fusion |
| 中文 | 分布引导的自编码器用于用户多模态兴趣交叉融合 |
| Affiliation | Lazada (Alibaba) |

**核心创新**: 通过分布引导的自编码器实现用户多模态兴趣的交叉融合。

### 10.3 Hearable Image — On-Device Image-Driven Sound Generation
| 项目 | 内容 |
|------|------|
| Title | Hearable Image: On-Device Image-Driven Sound Effect Generation |
| 中文 | Hearable Image：设备端图像驱动音效生成 |
| Affiliation | Samsung |

**核心创新**: 在设备端通过图像分析自动生成对应音效。

---

## 11. RecSys 2025 — Highlights

**基本信息**: 2025年9月22-26日, 布拉格, 捷克

### 11.1 LEAF — Lightweight Embedding for Large-Scale Recommendation
| 项目 | 内容 |
|------|------|
| Title | LEAF: Lightweight, Efficient, Adaptive and Flexible Embedding for Large-Scale Recommendation Models |
| 中文 | LEAF：大规模推荐模型的轻量高效自适应嵌入 |
| Affiliation | — |
| Link | dl.acm.org |

**核心创新**: 提出轻量级 embedding 方法，在大规模推荐系统中显著减少参数量同时保持推荐质量。

### 11.2 Lasso — LLM-based User Simulator for Cross-Domain Recommendation
| 项目 | 内容 |
|------|------|
| Title | Lasso: Large Language Model-based User Simulator for Cross-Domain Recommendation |
| 中文 | Lasso：基于 LLM 的跨域推荐用户模拟器 |
| Affiliation | — |
| Link | dl.acm.org |

**核心创新**: 利用 LLM 模拟用户跨域行为，为跨域推荐提供训练数据增强。

### 11.3 Exploring Scaling Laws of CTR Model
| 项目 | 内容 |
|------|------|
| Title | Exploring Scaling Laws of CTR Model for Online Performance Improvement |
| 中文 | CTR 模型规模定律探索 |
| Affiliation | 多机构 |
| arXiv | 2508.15326 |

**核心创新**: 系统研究 CTR 模型的 scaling laws，揭示模型大小、数据量与在线指标之间的关系。

### 11.4 You Say Search, I Say Recs — Spotify's Agentic Query Understanding
| 项目 | 内容 |
|------|------|
| Title | You Say Search, I Say Recs: A Scalable Agentic Approach to Query Understanding and Exploratory Search at Spotify |
| 中文 | 搜索与推荐的统一：Spotify 的 Agentic 查询理解 |
| Affiliation | Spotify |

**核心创新**: 在 Spotify 生产环境中使用 agentic 方法统一搜索和推荐体验。

---

## 12. LLM 架构 & 高效推理

### 12.1 DiffusionGemma — 4x Faster Text Generation (Google DeepMind, June 2026)
| 项目 | 内容 |
|------|------|
| Title | DiffusionGemma: 4x Faster Text Generation |
| 中文 | DiffusionGemma：4 倍更快文本生成 |
| Affiliation | Google DeepMind |
| Link | blog.google |

**核心创新**: 首个将扩散模型应用于文本生成的大规模生产模型，实现 4 倍推理加速，同时保持 Gemma 系列的生成质量。

### 12.2 Nemotron 3 — Hybrid Architecture (NVIDIA)
| 项目 | 内容 |
|------|------|
| Title | Nemotron 3 Super: Hybrid Architecture for Long-Context Efficiency |
| 中文 | Nemotron 3 Super：面向长上下文效率的混合架构 |
| Affiliation | NVIDIA |
| Link | — |

**核心创新**: 混合架构设计，交替使用常规 attention 层和 Mamba-2 (SSM) 层。在保持推理质量的同时大幅提升长上下文效率。提供 Nano (4B) 到 Super (120B-A12B) 多规格版本。

### 12.3 GPT-5.5 / GPT-5.2 Series (OpenAI)
| 项目 | 内容 |
|------|------|
| Title | GPT-5.5: Frontier Intelligence with Unified Routing |
| 中文 | GPT-5.5：统一路由的前沿智能 |
| Affiliation | OpenAI |
| Link | openai.com |

**核心创新**: GPT-5.5 采用统一路由架构，根据任务难度自动选择推理路径。GPT-5.2 在 ARC-AGI 2 视觉推理上达到 85% 准确率。GPT-5.5 在 Humanity's Last Exam 上达到 ~43-65%。

### 12.4 Claude Opus 4.8 / Fable 5 / Mythos 5 (Anthropic)
| 项目 | 内容 |
|------|------|
| Title | Claude Mythos 5 / Fable 5 / Opus 4.8 Series |
| 中文 | Claude Mythos 5 / Fable 5 / Opus 4.8 系列 |
| Affiliation | Anthropic |
| Link | anthropic.com |

**核心创新**: Claude Mythos 5 以 95.5% 在 SWE Bench 上领先，64.5% 在 Humanity's Last Exam 上居首。Opus 4.8 在 GPQA Diamond 推理上达到 94.2%。

### 12.5 Gemini 3 / 3.5 / Omni (Google DeepMind)
| 项目 | 内容 |
|------|------|
| Title | Gemini 3.5: Frontier Intelligence with Action |
| 中文 | Gemini 3.5：具备行动能力的前沿智能 |
| Affiliation | Google DeepMind |
| Link | blog.google |

**核心创新**: Gemini 3 Pro 在 AIME 2025 数学推理上达到 100%。Gemini 3.5 原生支持工具使用和行动（action）能力。Gemini Omni 实现统一多模态架构。

### 12.6 DeepSeek V4 / R1 (DeepSeek)
| 项目 | 内容 |
|------|------|
| Title | DeepSeek V4 / R1 |
| 中文 | DeepSeek V4 / R1 |
| Affiliation | DeepSeek |
| Link | deepseek.com |

**核心创新**: DeepSeek R1 通过 RL 驱动的推理训练，在效率上实现突破。V4 进一步提升了推理和多模态能力。

### 12.7 Llama 4 Scout (Meta)
| 项目 | 内容 |
|------|------|
| Title | Llama 4 Scout |
| 中文 | Llama 4 Scout |
| Affiliation | Meta AI |
| Link | meta.com |

**核心创新**: Llama 4 Scout 达到 2600 tokens/s 的推理速度，是目前最快的开源模型之一，同时保持强大的多模态理解能力。

### 12.8 Qwen3 / 3.5 / 3.6 Series (Alibaba)
| 项目 | 内容 |
|------|------|
| Title | Qwen3.5-Omni / Qwen3.6 Series |
| 中文 | Qwen3.5-Omni / Qwen3.6 系列 |
| Affiliation | Alibaba (通义千问) |

**核心创新**: Qwen 系列持续迭代，3.5-Omni 版本支持原生多模态输入输出，在中文和英文基准上均达到 SOTA。

---

## 13. 推荐系统 & CTR 前沿

### 13.1 OneTrans — Unified Feature Interaction + Sequence Modeling (ByteDance, WWW 2025)
| 项目 | 内容 |
|------|------|
| Title | OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer |
| 中文 | OneTrans：统一特征交互与序列建模 |
| Affiliation | ByteDance |
| Link | dl.acm.org |

**核心创新**: 将序列（行为）和非序列（画像/上下文）特征统一为单个 token 序列，通过金字塔 Transformer 块处理。在线 A/B 测试：单用户 GMV **+5.68%**。

### 13.2 HyFormer — Query-Decoding Architecture (ByteDance, arXiv 2026)
| 项目 | 内容 |
|------|------|
| Title | HyFormer: Revisiting the Roles of Sequence Modeling and Feature Interaction |
| 中文 | HyFormer：重新审视序列建模与特征交互的角色 |
| Affiliation | ByteDance |

**核心创新**: 批判 OneTrans 的 `[SEP]` token 设计，提出 query-decoding（全局 token 交叉注意力到每个序列） + query-augmentation。超越 OneTrans。

### 13.3 G2Rec — Generative Recommendation with Graph Tokenization
| 项目 | 内容 |
|------|------|
| Title | G2Rec: Generative Recommendation with Graph Tokenization |
| 中文 | G2Rec：基于图标记化的生成式推荐 |
| Affiliation | — |
| arXiv | — |

**核心创新**: 将用户-物品交互图转换为 token 序列，使用生成式范式统一推荐流程。

### 13.4 Token Factory — Google Soft Tokens for Large Recommender Models
| 项目 | 内容 |
|------|------|
| Title | Token Factory: Soft Tokens for Large-Scale Recommender Models |
| 中文 | Token Factory：面向大规模推荐模型的软 Token |
| Affiliation | Google |

**核心创新**: 提出 soft token 机制替代传统 ID embedding，使推荐模型具备类似 LLM 的规模化能力。

### 13.5 Modeling Cascaded Delay Feedback for Net CVR (WWW 2026)
| 项目 | 内容 |
|------|------|
| Title | Modeling Cascaded Delay Feedback for Online Net Conversion Rate Prediction |
| 中文 | 面向在线净转化率预测的级联延迟反馈建模 |
| Affiliation | Alibaba |
| Link | www2026.thewebconf.org |

**核心创新**: 针对广告场景中的延迟转化问题，提出级联延迟反馈建模方案，提供基准、洞察和解决方案。

---

## 14. 安全 & 对齐

### 14.1 Safety Alignment Should Be Made More Than Just a Few Tokens Deep (ICLR 2025)
| 项目 | 内容 |
|------|------|
| Title | Safety Alignment Should Be Made More Than Just a Few Tokens Deep |
| 中文 | 安全对齐不应只深入几个 Token |
| Affiliation | 多机构 |
| arXiv | 2406.05946 |
| Award | ICLR 2025 Outstanding |

**核心创新**: 论证当前对齐（alignment）是"浅层"的——仅影响前几个输出 token。这解释了对抗后缀攻击、prefilling 攻击、解码参数攻击以及通过微调轻易移除安全性的根本原因。提出 deeper-token 训练修复。

### 14.2 Securing the future of AI agents (Google DeepMind, June 2026)
| 项目 | 内容 |
|------|------|
| Title | Securing the Future of AI Agents |
| 中文 | 确保 AI Agent 的未来安全 |
| Affiliation | Google DeepMind |
| Link | deepmind.google |

**核心创新**: 提出多 agent 系统的安全框架，涵盖身份验证、权限管理和行为边界。

### 14.3 MCP Protocol Security Analysis
| 项目 | 内容 |
|------|------|
| Title | Securing MCP: Protocol-Level Threat Surface and Governance Controls |
| 中文 | 确保 MCP 安全：协议级威胁面与治理控制 |
| Affiliation | 多机构 |
| arXiv | 2511.20920 |

**核心创新**: 首次系统分析 Model Context Protocol (MCP) 的安全威胁面，提出协议级治理方案。

---

## 15. 游戏 & 决策

### 15.1 NitroGen — Open Foundation Model for Generalist Gaming Agents (CVPR 2026 Honorable Mention)
| 项目 | 内容 |
|------|------|
| Title | NitroGen: An Open Foundation Model for Generalist Gaming Agents |
| 中文 | NitroGen：通用游戏智能体开放基础模型 |
| Affiliation | 多机构 |
| Award | CVPR 2026 Best Paper Honorable Mention |

**核心创新**: 面向通用游戏智能体的开放基础模型，支持多游戏环境和任务。

### 15.2 SPIRAL — Self-Improving Game Agents
| 项目 | 内容 |
|------|------|
| Title | SPIRAL: Self-Play Reinforcement Learning for Game Agents |
| 中文 | SPIRAL：面向游戏智能体的自对弈强化学习 |
| Affiliation | — |

**核心创新**: 通过自我对弈机制实现游戏智能体的持续进化。

### 15.3 Dreamer 4 — World Model Reinforcement Learning
| 项目 | 内容 |
|------|------|
| Title | Dreamer 4: Scaling World Models for Real-World Control |
| 中文 | Dreamer 4：面向真实世界控制的规模化世界模型 |
| Affiliation | — |

**核心创新**: 在 Dreamer 系列基础上进一步扩展世界模型规模，实现更精准的规划和控制。

---

## 16. 多模态 & 视觉基础模型

### 16.1 WAVE — Unified Audio-Visual Embeddings (ICLR 2026)
| 项目 | 内容 |
|------|------|
| Title | WAVE: Learning Unified & Versatile Audio-Visual Embeddings with Multimodal LLM |
| 中文 | WAVE：多模态 LLM 学习统一音频-视觉嵌入 |
| Affiliation | 多机构 |

**核心创新**: 利用多模态 LLM 学习统一的音频-视觉嵌入表示，在音视频联合理解任务上实现 SOTA。

### 16.2 Gemma 4 12B — Unified Encoder-Free Multimodal Model (Google, June 2026)
| 项目 | 内容 |
|------|------|
| Title | Gemma 4 12B: A Unified, Encoder-Free Multimodal Model |
| 中文 | Gemma 4 12B：统一的无编码器多模态模型 |
| Affiliation | Google DeepMind |
| Link | blog.google |

**核心创新**: 无编码器的统一多模态架构，直接处理文本、图像和音频输入，无需专门的编码器模块。

### 16.3 HumanScale — Egocentric Human Video for Embodied Pretraining (arXiv June 2026)
| 项目 | 内容 |
|------|------|
| Title | HumanScale: Egocentric Human Video Can Outperform Real-Robot Data for Embodied Pretraining |
| 中文 | HumanScale：第一人称人类视频可超越真实机器人数据用于具身预训练 |
| Affiliation | PKU |
| arXiv | 2606.20521 |

**核心创新**: 证明第一人称人类视频在具身预训练中可以超越真实机器人数据的有效性。

---

## 17. 序列建模 & State Space Models

### 17.1 Mamba-3 (ICLR 2026 Oral)
| 项目 | 内容 |
|------|------|
| Title | Mamba-3: Improved Sequence Modeling using State Space Principles |
| 中文 | Mamba-3：利用状态空间原理改进序列建模 |
| Affiliation | CMU / Princeton |
| Award | ICLR 2026 Oral |

**核心创新**: 三核心改进——更富表达力的递推公式、复数状态更新规则、MIMO 公式。在检索、状态追踪和语言建模上超越 Transformer 和 Mamba-2。

### 17.2 ITNet — Unified Integral Transform (arXiv June 2026)
| 项目 | 内容 |
|------|------|
| Title | ITNet: A Unified Integral Transform Network Subsuming Convolution, Attention, and RNN |
| 中文 | ITNet：统一积分变换网络，包含卷积、注意力和 RNN |
| Affiliation | — |
| arXiv | — |

**核心创新**: 提出统一积分变换框架，从数学上统一了卷积、注意力和 RNN 三种核心算子。在多种序列建模任务上超越各专有架构。

---

## 18. 研究趋势总结

### 趋势 1: Agent 系统全面爆发
2026 年上半年见证 agent harness 概念的成熟和 Agentic Engineering 的实践化。"Code as Agent Harness" 成为从单 agent 到多 agent 系统的组织原则。ICML 2026、ICLR 2026 和 ACL 2026 均有大量 agent 相关论文。

### 趋势 2: 推荐系统进入 Tokenization + Generative 时代
ByteDance 的 RankMixer/TokenMixer/OneTrans 系列、Google 的 Token Factory、G2Rec 等代表推荐系统正从 ID embedding 范式转向 tokenization + generative 范式。CTR 模型的 scaling laws 首次被系统研究。

### 趋势 3: 推理时计算（Test-Time Compute）成为新焦点
S1、CORAL、NF-CoT 等方法展示：通过合理地分配推理时计算资源，可以在不大幅增加模型规模的情况下显著提升性能。从"训练时 scaling" 转向 "推理时 scaling"。

### 趋势 4: 安全与对齐从"浅层"走向"深层"
ICLR 2025 Outstanding 论文揭示当前对齐的浅层性，推动 deeper-token training、竞争涌现对齐等新方法。MCP 安全治理成为 agent 安全的基础设施问题。

### 趋势 5: 3D 视觉与具身智能的融合
CVPR 2026 最佳论文 D4RT 展示了从视频到 4D 场景重建的巨大飞跃。HumanScale 等工作展示第一人称视频预训练的有效性。VLA-World 将世界模型引入自动驾驶。

### 趋势 6: SSM vs Transformer 的竞争格局
Mamba-3 以 ICLR 2026 Oral 代表的 SSM 学派持续挑战 Transformer 的主导地位。同时 "Transformers are Inherently Succinct" 从理论上捍卫 Transformer。Nemotron 3 的混合架构（Attention + Mamba-2）代表实用主义折中方案。
