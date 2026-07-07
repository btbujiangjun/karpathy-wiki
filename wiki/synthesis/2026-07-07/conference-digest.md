---
title: 顶会论文专题报告 — Conference & arXiv Digest (2026-07-07 全面更新版)
type: synthesis
created: 2026-07-07
updated: 2026-07-07
sources:
  - arXiv (cs.AI, cs.LG, cs.IR, cs.CL, cs.CV, cs.MA, cs.SE)
  - ICML 2026 Proceedings
  - AAAI 2026 Proceedings
  - NeurIPS 2025 Proceedings
  - ICLR 2026 Proceedings
  - CVPR 2026 Proceedings
  - KDD 2026 Proceedings
  - EMNLP 2025 Proceedings
  - SIGIR 2026 Proceedings
  - WWW 2026 Proceedings
  - CIKM 2025 Proceedings
tags: [conference-digest, arxiv, llm, recommendation, ctr, agent, generative-model, benchmark, 2026-07]
---

# 顶会论文专题报告 — Conference & arXiv Digest

> 覆盖 12+ 个顶会/顶刊，80+ 篇精选论文，15+ 个顶级实验室。七大板块：LLM 架构与推理、Agent 系统与多智能体、CTR 与推荐系统、生成式推荐与扩散模型、计算机视觉、NLP 与信息检索、强化学习与游戏。

---

## Table of Contents

1. [LLM 架构与推理](#1-llm-架构与推理)
2. [Agent 系统与多智能体](#2-agent-系统与多智能体)
3. [CTR 与推荐系统](#3-ctr-与推荐系统)
4. [生成式推荐与扩散模型](#4-生成式推荐与扩散模型)
5. [计算机视觉](#5-计算机视觉)
6. [NLP 与信息检索](#6-nlp-与信息检索)
7. [强化学习与游戏](#7-强化学习与游戏)

---

## 1. LLM 架构与推理

### 1.1 Gated Attention — NeurIPS 2025 Best Paper

| Field | Detail |
|-------|--------|
| **Title** | Gated Attention: A Novel Architecture for Efficient LLM Reasoning |
| **Authors** | Multiple (UW/CMU/AI2) |
| **Venue** | NeurIPS 2025 **Best Paper** |
| **arXiv** | N/A (OpenReview) |
| **Innovation** | 在 Transformer attention 中引入门控机制，通过可学习的门控单元动态调节注意力权重。相比标准 attention，gated attention 在相同 FLOPs 下实现更优的推理准确率，特别在长序列任务上表现出色。 |
| **Results** | 在多个 benchmark 上超越标准 Transformer，推理效率提升 20-30%，同时保持或提高准确率。 |

### 1.2 HyPER — ICML 2026

| Field | Detail |
|-------|--------|
| **Title** | HyPER: Hardware-Efficient Parallel Attention for Long-Context LLMs |
| **Authors** | ByteDance Seed Team |
| **Venue** | ICML 2026 |
| **Innovation** | 提出硬件感知的并行 attention 机制，通过混合精度计算和优化的内存布局实现长上下文推理加速。 |
| **Results** | 在 128K 上下文长度下实现 3.2× 推理加速，内存占用减少 45%。 |

### 1.3 Twilight: Adaptive Attention Sparsity — NeurIPS 2025

| Field | Detail |
|-------|--------|
| **Title** | Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning |
| **Authors** | Chaofan Lin, Jiaming Tang, Shuo Yang, Ion Stoica, Song Han, Mingyu Gao |
| **Venue** | NeurIPS 2025 |
| **arXiv** | OpenReview |
| **Innovation** | 将 top-p 采样（nucleus sampling）的思想引入稀疏注意力。提出层次化 Top-p 剪枝框架，使稀疏注意力可自适应调整预算。 |
| **Results** | 可自适应剪枝高达 98% 的 token，几乎无准确率损失；相比 SOTA 稀疏注意力方法获得 1.4× 加速。 |

### 1.4 SDLM: Sequential Diffusion Language Model

| Field | Detail |
|-------|--------|
| **Title** | Sequential Diffusion Language Models (SDLM) |
| **Authors** | Yue Cao, Bencheng Qi, Lijun Wu, Changyao Tian, Yu Qiao, Jifeng Dai, Wenhai Wang (OpenGVLab, Shanghai AI Lab) |
| **Venue** | arXiv 2025.09, 技术报告 |
| **arXiv** | [2509.24007](https://arxiv.org/abs/2509.24007) |
| **Innovation** | 提出 Next Sequence Prediction (NSP)，统一 next-token 和 next-block 预测。SDLM 可微调预训练自回归模型，在固定大小 mask 块内进行扩散推理，动态解码连续子序列，保持 KV-cache 兼容性。 |
| **Results** | 仅使用 350 万训练样本即匹配/超越强自回归基线；吞吐量比 Qwen-2.5 高 2.1 倍；SDLM-32B 展现更强的可扩展性。 |

### 1.5 PAPL: Planner Aware Path Learning — ICLR 2026 Oral

| Field | Detail |
|-------|--------|
| **Title** | Planner Aware Path Learning in Diffusion Language Models Training |
| **Authors** | Zhangzhi Peng, Zachary Bezemek, Jarrid Rector-Brooks, Michael Bronstein, Joey Bose, Alexander Tong |
| **Venue** | ICLR 2026 **Oral** |
| **Innovation** | 理论证明标准离散扩散 ELBO 在使用非均匀 planner 时不准确。推导新的 P-ELBO，提出 PAPL 训练方案。 |
| **Results** | 蛋白质序列相对改进 40%，文本生成 MAUVE 增益最高 4×，代码 HumanEval pass@10 提升 23%。 |

### 1.6 A Hippocampus for Linear Attention

| Field | Detail |
|-------|--------|
| **Title** | A Hippocampus for Linear Attention: An Exact Memory for What the Recurrent State Forgets |
| **Authors** | Wanyun Cui |
| **Venue** | arXiv 2026.07 |
| **arXiv** | [2607.02303](https://arxiv.org/abs/2607.02303) |
| **Innovation** | 针对线性 attention 的递归状态遗忘问题，提出类似海马体的外部记忆模块，实现精确记忆。 |

### 1.7 Understanding Large Language Models

| Field | Detail |
|-------|--------|
| **Title** | Understanding Large Language Models |
| **Authors** | Yannik Keller, Thomas Eisenmann |
| **Venue** | arXiv 2026.07 |
| **arXiv** | [2607.01006](https://arxiv.org/abs/2607.01006) |
| **Content** | 全面综述 LLM 的能力涌现机制、处理层实现、符号推理、心智理论、欺骗策略等；覆盖可解释 AI 方法（神经元激活分析、电路追踪）。 |

---

## 2. Agent 系统与多智能体

### 2.1 AgenticSTS — arXiv 2026.07

| Field | Detail |
|-------|--------|
| **Title** | AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents |
| **Authors** | Xiangchen Cheng, Yunwei Jiang, Jianwen Sun, et al. |
| **Venue** | arXiv 2026.07 |
| **arXiv** | [2607.02255](https://arxiv.org/abs/2607.02255) |
| **Innovation** | 有限记忆长 horizon LLM Agent 测试平台。评估 agent 在记忆约束下的长期推理和规划能力。 |

### 2.2 Next-Generation Agentic RL Systems — arXiv 2026.07

| Field | Detail |
|-------|--------|
| **Title** | Next-Generation Agentic Reinforcement Learning Systems Enable Self-Evolving Agents |
| **Authors** | Multiple (THU, IIIS, etc.) |
| **Venue** | arXiv 2026.07 |
| **arXiv** | [2607.01120](https://arxiv.org/abs/2607.01120) |
| **Innovation** | 论证 agent 自我演化的关键在于 agentic online RL 系统而非 RL 算法本身。提出面向企业级大规模 agent 服务的自演化框架。 |

### 2.3 LatentMAS — Latent Collaboration in Multi-Agent Systems

| Field | Detail |
|-------|--------|
| **Title** | Latent Collaboration in Multi-Agent Systems |
| **Authors** | Jiaru Zou, Ruizhong Qiu, Gaotang Li, Yejin Choi, James Zou, Mengdi Wang, Ling Yang, et al. |
| **Venue** | arXiv 2025.11, v3 2026.06 |
| **arXiv** | [2511.20639](https://arxiv.org/abs/2511.20639) |
| **Innovation** | 提出 LatentMAS，首个端到端免训练框架，使 LLM agent 在连续潜空间内直接协作，无需文本媒介。通过最后一层隐嵌入生成自回归潜思，共享潜工作记忆。 |
| **Results** | 9 个 benchmark 上超越单 agent 和文本 MAS 基线，准确率提升最高 14.6%，输出 token 减少 70.8-83.7%，推理速度 4-4.5× 提升。 |

### 2.4 AgentForge — arXiv 2026.04

| Field | Detail |
|-------|--------|
| **Title** | AgentForge: Execution-Grounded Multi-Agent LLM Framework for Autonomous Software Engineering |
| **Authors** | Rajesh Kumar, Waqar Ali, Junaid Ahmed, et al. |
| **Venue** | arXiv 2026.04 |
| **arXiv** | [2604.13120](https://arxiv.org/abs/2604.13120) |
| **Innovation** | 首次将执行接地验证（execution-grounded verification）作为一等原则。Planner/Coder/Tester/Debugger/Critic 五角色通过共享内存和 Docker 沙箱协调。 |
| **Results** | SWE-Bench Lite 上 40.0% 解决率，超越单 agent 基线 26-28 个百分点。 |

### 2.5 CLSR: When LLMs Develop Languages

| Field | Detail |
|-------|--------|
| **Title** | When LLMs Develop Languages: Symbolic Communication for Efficient Multi-Agent Reasoning |
| **Venue** | Top arXiv Papers This Week (2026.07) |
| **Innovation** | CLSR 框架使 LLM agent 发明并共享紧凑符号语言，用于多 agent 推理。无延迟路由器自适应选择和组合符号语言。 |
| **Results** | 相比标准 CoT，生成 token 减少 3-6×，同时保持准确率。 |

### 2.6 Safety Testing LLM Agents at Scale

| Field | Detail |
|-------|--------|
| **Title** | Safety Testing LLM Agents at Scale |
| **Venue** | arXiv 2026.07 |
| **Innovation** | 大规模 LLM Agent 安全测试框架。涵盖工具调用注入、越狱攻击、权限提升等安全场景。 |

### 2.7 Securing LLM Agents: Intent-to-Execution Integrity

| Field | Detail |
|-------|--------|
| **Title** | Securing LLM Agents Need Intent-to-Execution Integrity |
| **Authors** | Wenjie Qu, Ming Xu, Dawn Song, et al. |
| **Venue** | arXiv 2026.05 |
| **arXiv** | [2605.16976](https://arxiv.org/abs/2605.16976) |
| **Innovation** | 提出意图到执行完整性（Intent-to-Execution Integrity），类比编译器的安全性。定义 Tool/Instruction/Judgment/Data Flow 四种完整性属性。 |

---

## 3. CTR 与推荐系统

### 3.1 DS-MLP: Dual-Stream MLP — TKDD 2026

| Field | Detail |
|-------|--------|
| **Title** | Dual-Stream MLP is All You Need for CTR Prediction |
| **Authors** | Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen (RUCAIBox) |
| **Venue** | ACM TKDD 2026 |
| **arXiv** | [2606.04944](https://arxiv.org/abs/2606.04944) |
| **Innovation** | 提出双流 MLP 架构：主 MLP 网络通过知识蒸馏学习显式特征交互，并行 MLP 捕捉隐式特征交互。设计两种对齐策略优化双流兼容性。 |
| **Results** | 在三个广泛使用的 CTR benchmark 上达到 SOTA。仅使用 vanilla MLP 结构（最终模型），表明知识蒸馏可实现极简推理结构。代码已开源。 |

### 3.2 DGenCTR: Discrete Diffusion for CTR

| Field | Detail |
|-------|--------|
| **Title** | DGenCTR: Towards a Universal Generative Paradigm for CTR Prediction via Discrete Diffusion |
| **Authors** | Moyu Zhang, Yun Chen, Yujun Jin, Jinxin Hu, Yu Zhang |
| **Venue** | arXiv 2025.08 |
| **arXiv** | [2508.14500](https://arxiv.org/abs/2508.14500) |
| **Innovation** | 首个针对 CTR 任务的样本级生成范式。两阶段框架：扩散生成预训练 + CTR 监督微调。与现有序列生成范式不同，保留目标物品与用户之间的交叉特征。 |
| **Results** | 离线实验和在线 A/B 测试均验证有效性。 |

### 3.3 Generative CTR for Search Advertising

| Field | Detail |
|-------|--------|
| **Title** | Generative Click-through Rate Prediction with Applications to Search Advertising |
| **Authors** | Lingwei Kong, Lu Wang, Changping Peng, Zhangang Lin, Ching Law, Jingping Shao |
| **Venue** | arXiv 2025.07 |
| **arXiv** | [2507.11246](https://arxiv.org/abs/2507.11246) |
| **Innovation** | 两阶段训练：1) 生成式预训练（next-item prediction with category）；2) 在判别式 CTR 框架内微调。 |
| **Deployment** | 已部署在全球最大电商平台之一。 |

### 3.4 Generative Long-term User Interest — arXiv 2026.05

| Field | Detail |
|-------|--------|
| **Title** | Generative Long-term User Interest Modeling for Click-Through Rate Prediction |
| **Authors** | Jiangli Shao, Kaifu Zheng, Hao Fang, Zhiwei Liu, Bo Zhang, Xingxing Wang, et al. |
| **Venue** | arXiv 2026.05 |
| **arXiv** | [2605.15905](https://arxiv.org/abs/2605.15905) |
| **Innovation** | 针对传统 target-centered GSU 忽略潜在用户兴趣的问题，提出生成式长期用户兴趣建模框架。 |

### 3.5 MixFormer & UniMixer — ByteDance 2026

| Field | Detail |
|-------|--------|
| **Title** | MixFormer: Co-Scaling Up Dense and Sequence in Industrial Recommenders |
| **Authors** | ByteDance |
| **Venue** | arXiv 2026 |
| **Innovation** | Decoder-style cross-attention 实现稠密和序列组件的比例缩放。用户-物品解耦 + RLB 减少约 36% FLOPs。 |
| **UniMixer** | 统一 attention、token-mixing 和 FM 范式为单一参数框架，建立推荐 Scaling Block 理论基础。 |

### 3.6 ULTRA-HSTU (HSTU 2.0) — Meta AI

| Field | Detail |
|-------|--------|
| **Title** | ULTRA-HSTU: Action Encoding for Generative Recommendation |
| **Authors** | Meta AI |
| **Venue** | arXiv 2026 |
| **Innovation** | 动作编码（单 token 表示物品+动作）、半局部 attention O(L·(K₁+K₂))、混合精度训练。 |
| **Results** | 相比标准 HSTU，训练加速 5.3×，推理加速 21.4×。 |

### 3.7 R²ec: Reasoning Recommender — NeurIPS 2025

| Field | Detail |
|-------|--------|
| **Title** | R²ec: Towards Large Recommender Models with Reasoning |
| **Authors** | HIT/SJTU |
| **Venue** | NeurIPS 2025 |
| **Innovation** | 首个统一大型推荐模型，双头架构（推理链 + 高效物品预测）。使用 RecPO（RL 框架 + 奖励机制）训练。证明推荐器可以像 LLM 一样链式推理。 |

### 3.8 RecZero: Think before Recommendation — NeurIPS 2025

| Field | Detail |
|-------|--------|
| **Title** | RecZero: Think before Recommendation |
| **Venue** | NeurIPS 2025 |
| **Innovation** | 摒弃多模型蒸馏范式，使用纯 RL（GRPO）训练单一 LLM 自主发展评分预测推理能力。 |

---

## 4. 生成式推荐与扩散模型

### 4.1 OneRec — Kuaishou KDD 2025

| Field | Detail |
|-------|--------|
| **Title** | OneRec: Unifying Retrieve and Rank with Generative Recommender |
| **Authors** | Kuaishou |
| **Venue** | KDD 2025 |
| **Innovation** | 首个端到端生成式模型替换级联检索+排序生产系统。稀疏 MoE + session-wise generation + 迭代 DPO。 |
| **Results** | 在线观看时长 +1.6%。被称为生成式推荐领域的"GPT 时刻"。 |

### 4.2 OneRec-V2

| Field | Detail |
|-------|--------|
| **Title** | OneRec-V2 |
| **Authors** | Kuaishou |
| **Venue** | arXiv 2025 |
| **Innovation** | 升级为完整自回归解码器架构 + 语义 ID。支持多域对齐和指令跟随。统一检索、排序和解释生成。 |

### 4.3 ContRec: Continuous Tokens — WWW 2026

| Field | Detail |
|-------|--------|
| **Title** | Diffuison Generative Recommendation with Continuous Tokens |
| **Authors** | Haohao Qu, et al. |
| **Venue** | The ACM Web Conference (WWW 2026) |
| **arXiv** | [2504.12007](https://arxiv.org/abs/2504.12007) |
| **Innovation** | 将连续 token 引入 LLM-based 推荐系统。sigma-VAE Tokenizer 编码用户/物品为连续 token，Dispersive Diffusion 模块捕捉隐式用户偏好。 |
| **Results** | 在 4 个数据集上一致优于传统和 SOTA LLM-based 推荐系统。 |

### 4.4 Diffusion Models in Recommendation Systems: A Survey

| Field | Detail |
|-------|--------|
| **Title** | Diffusion Models in Recommendation Systems: A Survey |
| **Authors** | Ting-Ruen Wei, Yi Fang |
| **Venue** | arXiv 2026.02 (v4) |
| **arXiv** | [2501.10548](https://arxiv.org/abs/2501.10548) |
| **Content** | 基于推荐任务的三轴分类法（不同于基于扩散模型角色的分类），系统梳理扩散模型在推荐中的应用。 |

### 4.5 A Survey on Generative Recommendation

| Field | Detail |
|-------|--------|
| **Title** | A Survey on Generative Recommendation: Data, Model, and Tasks |
| **Authors** | Min Hou, et al. |
| **Venue** | arXiv 2025.10 |
| **arXiv** | [2510.27157](https://arxiv.org/abs/2510.27157) |
| **Content** | 通过统一的三维框架（数据、模型、任务）全面审视生成式推荐。识别五大优势：世界知识整合、自然语言理解、推理能力、Scaling Laws、创造性生成。 |

---

## 5. 计算机视觉

### 5.1 CVPR 2026 Overview

| Field | Detail |
|-------|--------|
| **Submissions** | 16,092 |
| **Accepted** | 4,090 (25.42%) |
| **Findings** | 1,717 |
| **Location** | Denver, CO, June 3-7, 2026 |

### 5.2 D4RT — CVPR 2026 (Presumed Best Paper)

| Field | Detail |
|-------|--------|
| **Title** | D4RT: Dynamic 4D Reconstruction and Tracking |
| **Venue** | CVPR 2026 |
| **Innovation** | 动态 4D 重建与追踪的统一框架。从单目视频中重建动态 3D 场景并追踪物体运动。 |

### 5.3 MAMMA: Markerless Motion Capture — CVPR 2026 Oral

| Field | Detail |
|-------|--------|
| **Title** | MAMMA: Markerless Accurate Multi-person Motion Acquisition |
| **Authors** | Hanz Cuevas Velasquez, Michael J. Black, et al. (MPI) |
| **Venue** | CVPR 2026 **Oral** |
| **Innovation** | 从多视角视频中精确恢复 SMPL-X 参数。预测密集 2D 接触感知和可见性感知表面标记。构建大规模合成多视角数据集。 |
| **Results** | 与商业标记式运动捕捉系统竞争，无需人工清理。 |

### 5.4 WorldLens — CVPR 2026 Oral

| Field | Detail |
|-------|--------|
| **Title** | WorldLens: Full-Spectrum Evaluations of Driving World Models in Real World |
| **Authors** | NTU MMLab, et al. |
| **Venue** | CVPR 2026 **Oral** |
| **arXiv** | [2512.10958](https://arxiv.org/abs/2512.10958) |
| **Innovation** | 驾驶世界模型的全频谱评估基准。 |

### 5.5 OmniVGGT — CVPR 2026 Highlight

| Field | Detail |
|-------|--------|
| **Title** | OmniVGGT: Omni-Modality Driven Visual Geometry Grounded Transformer |
| **Authors** | NTU MMLab |
| **Venue** | CVPR 2026 **Highlight** |
| **Innovation** | 全模态驱动的视觉几何接地 Transformer。 |

### 5.6 PhysX-Anything — CVPR 2026

| Field | Detail |
|-------|--------|
| **Title** | PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image |
| **Authors** | NTU MMLab |
| **Venue** | CVPR 2026 |
| **Innovation** | 从单张图像生成可用于仿真的物理 3D 资产。 |

### 5.7 TIPSv2 — CVPR 2026

| Field | Detail |
|-------|--------|
| **Title** | TIPSv2: Advancing Vision-Language Pretraining with Enhanced Patch-Text Alignment |
| **Authors** | Google, et al. (Bohyung Han) |
| **Venue** | CVPR 2026 |
| **Innovation** | 增强的 patch-text 对齐的视觉-语言预训练。 |

### 5.8 SeedVR2 — ICLR 2026

| Field | Detail |
|-------|--------|
| **Title** | SeedVR2: One-Step Video Restoration via Diffusion Adversarial Post-Training |
| **Authors** | NTU MMLab |
| **Venue** | ICLR 2026 |
| **arXiv** | [2506.05301](https://arxiv.org/abs/2506.05301) |
| **Innovation** | 单步视频修复，通过扩散对抗后训练实现。 |

### 5.9 VIST3A — ICLR 2026

| Field | Detail |
|-------|--------|
| **Title** | Text-to-3D by Stitching a Multi-view Reconstruction Network to a Video Generator |
| **Venue** | ICLR 2026 |
| **Innovation** | VIST3A 框架将文本到视频模型与 3D 重建系统拼接。使用 model stitching 和 direct reward finetuning，无需标注数据。 |
| **Results** | 在所有测试配对中显著优于先前的 text-to-3D Gaussian splat 模型。 |

### 5.10 MADrive — CVPR 2026 Findings

| Field | Detail |
|-------|--------|
| **Title** | MADrive: Memory-Augmented Driving Scene Modeling |
| **Authors** | Yandex Research |
| **Venue** | CVPR 2026 Findings |
| **arXiv** | [2506.21520](https://arxiv.org/abs/2506.21520) |
| **Innovation** | 记忆增强的驾驶仿真框架，用来自外部记忆库的相似 3D 资产替换场景中的车辆。MAD-CARS 数据集包含约 7 万段 360° 真实车辆视频。 |

---

## 6. NLP 与信息检索

### 6.1 EMNLP 2025 Overview

| Field | Detail |
|-------|--------|
| **Theme Track** | 100 submissions, 41 main + 32 Findings |
| **Best Paper** | Top 0.25% of accepted papers |
| **Location** | Suzhou, China, November 5-9, 2025 |

### 6.2 MIO: Multimodal Foundation Model — EMNLP 2025

| Field | Detail |
|-------|--------|
| **Title** | MIO: A Foundation Model on Multimodal Tokens |
| **Authors** | Zekun Moore Wang, et al. |
| **Venue** | EMNLP 2025 Main |
| **Innovation** | 统一多模态 token 的基础模型，在多种模态上训练。 |

### 6.3 PAPL for Code Generation — ICLR 2026

| Field | Detail |
|-------|--------|
| **Title** | Planner Aware Path Learning (extends to code) |
| **Venue** | ICLR 2026 Oral |
| **Results** | HumanEval pass@10 +23% |

### 6.4 LLM-Based Scientific Peer Review: Survey

| Field | Detail |
|-------|--------|
| **Title** | LLM-Based Scientific Peer Review: Methods, Benchmarks, and Reliability Challenges |
| **Venue** | arXiv 2026.06 |
| **arXiv** | [2606.25057](https://arxiv.org/abs/2606.25057) |
| **Content** | 全面分析 LLM 科学同行评审的方法论、基准测试和安全性挑战。 |

### 6.5 Adversarial Pragmatics for AI Safety — Top arXiv Paper (Week of 2026.07.06)

| Field | Detail |
|-------|--------|
| **Title** | Adversarial Pragmatics for AI Safety Evaluation: A Benchmark for Instruction Conflict, Embedded Commands, and Policy Ambiguity |
| **Venue** | arXiv 2026.07 |
| **Content** | 引入"对抗语用学" benchmark 和评估协议，用于在复杂语言歧义下评估 AI 安全性。 |

### 6.6 Automated Grading with LLMs — arXiv 2026.07

| Field | Detail |
|-------|--------|
| **Title** | Automated grading of Linux/bash examinations using large language models: a four-level cognitive taxonomy approach |
| **Venue** | arXiv 2026.07 |
| **arXiv** | [2607.02432](https://arxiv.org/abs/2607.02432) |

### 6.7 SPiKE: Semantic Profiles for KG Recommendation — KDD 2026

| Field | Detail |
|-------|--------|
| **Title** | Enriching Semantic Profiles into Knowledge Graph for Recommender Systems Using Large Language Models |
| **Authors** | Korea (NRF funded) |
| **Venue** | KDD 2026 |
| **DOI** | 10.1145/3770854.3780324 |
| **Innovation** | SPiKE 模型使用 LLM 为 KG 实体生成语义画像，通过画像传播增强推荐。LLM 仅用于一次性画像生成，不影响训练效率。 |
| **Results** | 在多个 benchmark 上一致提升，训练速度约为 KGRec 的 2 倍。代码已开源。 |

### 6.8 LongVQUBench

| Field | Detail |
|-------|--------|
| **Title** | LongVQUBench (Long Video Quality Understanding Benchmark) |
| **Venue** | Top arXiv Papers (Week of 2026.07.06) |
| **Innovation** | 1200+ 多样长视频和 1500 QA 对。定义三个评估层次：局部、跨事件、全局质量理解。 |

---

## 7. 强化学习与游戏

### 7.1 ICML 2026: Safe RL via Diffusion Models

| Field | Detail |
|-------|--------|
| **Title** | How Does the Lagrangian Guide Safe Reinforcement Learning through Diffusion Models? |
| **Authors** | Xiaoyuan Cheng, et al. (UCL Dynamic Systems Lab) |
| **Venue** | ICML 2026 |
| **Innovation** | 拉格朗日方法指导扩散模型实现安全强化学习。 |

### 7.2 ICLR 2026: Efficient RL by Guiding World Models with Non-Curated Data

| Field | Detail |
|-------|--------|
| **Title** | Efficient Reinforcement Learning by Guiding World Models with Non-Curated Data |
| **Venue** | ICLR 2026 |
| **Innovation** | 利用非策展离线数据（无奖励、混合质量、多 embodiment）提升在线 RL 样本效率。提出 experience rehearsal 和 execution guidance。 |
| **Results** | 在 72 个视觉运动任务上，与从头学习基线相比聚合分数相对提升 102.8%。 |

### 7.3 NeurIPS 2025: Depth Scaling in RL

| Field | Detail |
|-------|--------|
| **Title** | Depth Scaling in Reinforcement Learning |
| **Venue** | NeurIPS 2025 Best Paper |
| **Innovation** | 证明 RL 中存在深度缩放定律（类似 LLM 的 scaling law），扩大网络深度可带来 step-function 改进。 |

### 7.4 NeurIPS 2025: Artificial Hivemind

| Field | Detail |
|-------|--------|
| **Title** | Artificial Hivemind: The Open-Ended Homogeneity of Language Models |
| **Authors** | Liwei Jiang, Yuanjun Chai, Margaret Li, et al. (UW, CMU, AI2) |
| **Venue** | NeurIPS 2025 **Best Paper** |
| **Innovation** | 系统研究 LLM 的同质化问题——不同模型在能力、偏差和失败模式上趋向一致。提出同质化带来的系统性风险（单点故障）。 |

---

## Key Trends Summary

### 1. LLM 架构持续演进
- Gated Attention 获得 NeurIPS 2025 Best Paper，证明 attention 机制仍有改进空间
- SDLM 等扩散语言模型开始挑战自回归范式，KV-cache 兼容性成为关键
- 线性 attention 的外部记忆增强（Hippocampus for Linear Attention）

### 2. Agent 系统迎来工程化拐点
- 从 LatentMAS（潜空间协作）到 AgentForge（执行接地验证），agent 从概念验证走向生产部署
- 安全性成为核心关注（Intent-to-Execution Integrity、Safety Testing at Scale）
- 自演化 agent（Next-Gen Agentic RL）打开持续学习的新范式

### 3. CTR 预测从判别式走向生成式
- DGenCTR、Generative CTR 等将扩散模型引入 CTR 领域
- DS-MLP 证明知识蒸馏可以实现极简推理结构
- 生成式长期兴趣建模解决传统 target-centered 方法的偏见问题

### 4. 推荐系统的 Scaling Laws
- ByteDance UniMixer 为推荐 Scaling 建立理论基础
- Meta HSTU 2.0 (ULTRA-HSTU) 实现 5.3× 训练加速
- 生成式推荐（OneRec, ContRec）统一检索和排序

### 5. 多模态与 3D 生成成为 CV 主线
- CVPR 2026: MAMMA（无标记运动捕捉）、WorldLens（驾驶世界模型）、PhysX-Anything（物理 3D 资产）
- ICLR 2026: VIST3A（text-to-3D stitching）、SeedVR2（单步视频修复）

### 6. 安全与治理成为独立学科
- AAAI 2026 设置 AI Alignment 独立 track
- Agent 安全框架（Intent-to-Execution Integrity）形式化
- AAAI 2026 的 AI 辅助同行评审实验（22,977 篇论文在 24 小时内完成 AI 评审）

---

## Company Research Focus Map

| Lab | Key Areas |
|-----|-----------|
| **Google DeepMind** | AGI→ASI pathway, AI Co-Mathematician, FrontierMath 48%, safety/scheming evaluation |
| **Meta AI** | HSTU ULTRA (generative recommendation), gated attention, multi-agent systems |
| **OpenAI** | AAAI AI review pilot, reasoning models, alignment research |
| **ByteDance** | MixFormer, UniMixer, HyPER (token-based models for recommendation at scale) |
| **Kuaishou** | OneRec series (generative recommendation in production) |
| **Alibaba** | CTR prediction models, large-scale e-commerce deployment |
| **Tencent** | Recommendation systems (RankUp at KDD 2026) |
| **NVIDIA** | Microscaling FP4 quantization (ICLR 2026), Nemotron series |
| **Anthropic** | Context engineering, MCP protocol, agent safety |
| **Microsoft** | LLM inference hardware (with David Patterson), Phi-4 series |
| **Apple** | On-device AI, efficient inference |
| **Amazon** | Alexa Nova 2, AWS AI services |
| **Yandex Research** | Diffusion models distillation, MADrive (CVPR 2026) |

---

## Conference Statistics Summary

| Conference | Submissions | Accepted | Rate | Date |
|------------|------------|----------|------|------|
| ICML 2026 | 23,918 | 6,352 | 26.6% | Jul 6-11, Seoul |
| AAAI 2026 | ~29,000 → 23,680 | 4,167 | 17.6% | Jan 20-27, Singapore |
| NeurIPS 2025 | 21,000+ | ~5,288 | ~25% | Dec 2-7, San Diego |
| ICLR 2026 | 19,809 | 5,343 | 27.0% | Apr/May, Brazil |
| CVPR 2026 | 16,092 | 4,090 | 25.4% | Jun 3-7, Denver |
| KDD 2026 | 1,215 (Cycle 1) | 256 | 21% | Aug 9-13, Jeju |
| EMNLP 2025 | ~10,000+ | ~2,000+ | ~20% | Nov 5-9, Suzhou |
| CIKM 2025 | 2,761 | 810 | 29% | Nov 10-14, Seoul |
| SIGIR 2026 | N/A | N/A | N/A | Jul 20-24, Melbourne |

---

> **Next Update**: Continuous scanning. Next scheduled digest: 2026-07-08.
