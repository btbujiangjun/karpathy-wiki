---
title: 顶会论文专题报告 — 2026年6月全面版（ICML / AAAI / NeurIPS / ICLR / KDD / CVPR / ACL / EMNLP / SIGIR / WWW / 各大实验室）
type: synthesis
created: 2026-06-01
updated: 2026-06-01
sources: [arXiv, ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026]
tags: [conference-digest, icml-2026, aaai-2026, neurips-2025, iclr-2026, kdd-2026, cvpr-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, agent, llm, ctr, recommendation, diffusion, games, benchmark]
---

# 顶会论文专题报告 — 2026年6月全面版

> 覆盖 ICML 2026、AAAI 2026、NeurIPS 2025、ICLR 2026、KDD 2026、CVPR 2026、ACL 2026、EMNLP 2025、SIGIR 2026、WWW 2026 等主要会议的最新接收论文与 arXiv 前沿工作，并覆盖 DeepMind、OpenAI、Meta、ByteDance、NVIDIA、Apple 等主要实验室的最新成果。

---

## 目录

1. [ICML 2026](#1-icml-2026)
2. [AAAI 2026](#2-aaai-2026)
3. [NeurIPS 2025 — Best Papers & Awards](#3-neurips-2025--best-papers--awards)
4. [ICLR 2026 — Outstanding Papers](#4-iclr-2026--outstanding-papers)
5. [KDD 2026](#5-kdd-2026)
6. [CVPR 2026](#6-cvpr-2026)
7. [ACL 2026 / EMNLP 2025](#7-acl-2026--emnlp-2025)
8. [SIGIR 2026 / WWW 2026](#8-sigir-2026--www-2026)
9. [主要实验室最新成果](#9-主要实验室最新成果)
10. [综合趋势分析](#10-综合趋势分析)

---

## 1. ICML 2026

ICML 2026 共接受约 6,500 篇论文（含 500+ 篇精选亮点），大会将于首尔举行。

### 1.1 Key Papers

| Paper | Affiliation | arXiv | 核心贡献 |
|-------|-----------|-------|---------|
| Shannon Scaling Law | - | 2605.23901 | LLM 作为噪声信道的缩放律理论，打破了传统 scaling law 仅基于 token 计数的局限 |
| Self-Supervised Flow Matching (Self-Flow) | - | - | 自监督流匹配训练，无需配对数据 |
| Complete-muE | - | 2605.23893 | MoE 超参数迁移的统一方法论 |
| Training-Free Looped Transformers | Google? | 2605.23872 | 无需训练的循环 Transformer，推理时动态增加深度 |
| Strong Teacher Not Needed | - | 2605.23857 | 弱教师蒸馏同样有效，挑战传统知识蒸馏假设 |
| DiLaDi: DiLaDiff | NVIDIA | 2605.23605 | 蒸馏潜增强扩散语言模型 |
| Bi-NAC | UCF | 2605.24547 | 双层自然语言 Actor-Critic，Stackelberg 规划 |
| R2-Write | - | 2604.03004 | 反思与修订的深度推理写作框架 |
| BigMac | - | - | 突破多模态 LLM 训练计算-内存帕累托前沿 |
| ALIVE | Alibaba | - | 交互式前端游戏 RL，纯视觉输入无需环境代码 |
| UniAR | Alibaba | - | 统一多模态自回归建模 |
| Vector Prompt Interfaces | - | 2603.04292 | 提倡向量提示作为公共定制化接口 |

### 1.2 其他值得关注的 ICML 2026 论文

- **Preisach Attention** — 基于磁滞模型的序列记忆注意力机制 (arXiv:2605.23603)
- **Dimensionality Barrier for Retrieval** — MIT 提出维度对检索的影响理论 (arXiv:2605.23556)
- **Agentic Proving** — 智能体自动程序验证 (arXiv:2605.23772)
- **GenStrat** — LLM 策略推理的形式化框架 (arXiv:2605.23238)
- **AutoResearch AI** — Salesforce 全自动研究流程 (arXiv:2605.23204)

---

## 2. AAAI 2026

AAAI 2026 收到 29,000 多份投稿，评审约 23,000 篇，接收率竞争激烈。

| Paper | Affiliation | 核心贡献 |
|-------|-----------|---------|
| StreamingTalker | - | 高保真流媒体数字人技术，首帧生成仅需 0.25 秒 |
| ReconVLA | - | 视觉语言动作基础模型，AAAI 2026 Oral |
| VLA-Adapter | - | 参数高效视觉语言动作迁移 |
| HGPO | - | Hierarchy-of-Groups Policy Optimization，分组层次化策略优化 |
| MEMENTO | Meta | 基于 RAG 的记忆增强推荐，长期 CTR +1% |

---

## 3. NeurIPS 2025 — Best Papers & Awards

### 3.1 Best Paper Awards

| Paper | Affiliation | 核心贡献 |
|-------|-----------|---------|
| **Artificial Hivemind** | UW / Allen AI | 多 LLM 协作构成"集体思维"，超越单个大模型能力 |
| **Gated Attention** | Alibaba Qwen | 门控注意力机制突破 Transformer 注意力瓶颈 |
| **1000-Layer RL** | - | 证明深度 RL 网络可扩展至 1000+ 层，打破"深 RL 不工作"共识 |
| **Why Diffusion Models Don't Memorize** | - | 严格理论证明扩散模型在温和条件下不会记忆训练数据 |

### 3.2 Best Paper Runners-Up

| Paper | Core Contribution |
|-------|------------------|
| **RLVR Critique** | 对 RL from Verifiable Rewards (RLVR) 的系统性批评和改进建议 |
| **SPIRAL** | Self-Play 激励 LLM 推理能力涌现 |

---

## 4. ICLR 2026 — Outstanding Papers

| Paper | 荣誉 | Core Contribution |
|-------|------|------------------|
| **Transformers are Inherently Succinct** | Outstanding Paper | 严格证明 Transformer 在处理长序列时具有内在的简洁表示能力 |
| **Polar Express** | Honorable Mention | 高效快速的多模态 Transformers 推理加速方法 |
| **LaDiR** | - | 潜扩散模型用于 LLM 文本推理 (arXiv:2510.04573) |
| **MEM1** | - | Memory-Reasoning 协同的长时域智能体 |

---

## 5. KDD 2026

| Paper | Affiliation | Core Contribution |
|-------|-----------|------------------|
| **RankUp** | Tencent WeChat | 高秩表征增强微信广告排序，KDD 2026 Ads Track |
| **HyFunc** | - | LLM 函数调用能力增强框架 |
| **Causal Attention for Generative Recommendation** | - | Beyond Interleaving — 因果注意力替代传统交替训练 |
| **BenchBench** | - | 基准测试的元评估，衡量 benchmarks 本身的可靠性 |
| **AutoSci** | - | 全自动科研生命周期智能体系统 |
| **RankElastor** | - | 有效秩动力学分析 CTR 模型表征瓶颈 (arXiv:2605.23191) |

---

## 6. CVPR 2026

CVPR 2026 接收 4,090 篇论文（来自 16,092 篇投稿）。

| Paper | Affiliation | Core Contribution |
|-------|-----------|------------------|
| **SAM 3D** | Best Paper | 分割一切模型扩展到 3D 空间 |
| **ARCache** | - | 视频扩散模型的缓存加速推理（arXiv 2605 系列） |
| **Semantic Communication** | - | 面向 6G 时代的语义通信 |
| **Text-to-Speech on Face** | - | 从人脸视频直接合成语音 |

---

## 7. ACL 2026 / EMNLP 2025

### 7.1 ACL 2026

已公布接收论文列表（RIKEN 等机构贡献 21 篇），大规模接收在即。

### 7.2 EMNLP 2025 Awards

| 类别 | Paper | Affiliation | Core Contribution |
|------|-------|-----------|------------------|
| **Best Paper** | Infini-gram mini | - | 无限 n-gram 的高效近似，双 token 和短语级别的 EMNLP 2025 最佳 |
| **Outstanding** | LingGym | - | 语言能力的全面评估"健身房" |
| **Outstanding** | Mind the Value-Action Gap | - | 发现 LLM 表达价值观与实际行动之间的系统性差距 |
| **Outstanding** | CodeTree | Salesforce | 智能体引导的树搜索代码生成 |

---

## 8. SIGIR 2026 / WWW 2026

### 8.1 SIGIR 2026

| Paper | Affiliation | Core Contribution |
|-------|-----------|------------------|
| **ACE** | - | 自适应点击率预估增强 |
| **FLASH-MAXSIM** | - | 快速最大相似度检索 |
| **FEDIN** | - | 频域特征交互网络，SIGIR 2026 |
| **FFT-UI** | - | FFT 加速用户行为序列建模 |

### 8.2 WWW 2026

| Paper | Affiliation | Core Contribution |
|-------|-----------|------------------|
| **ThinkRec** | - | 思考链增强的 LLM 推荐 |
| **CARE** | - | Cascaded Reasoning 生成式推荐 |
| **GenCI** | Alibaba | 生成式 CTR 通过 Cohort Intent 学习 |
| **SparseCTR** | Meituan | 稀疏注意力长周期 CTR 预测 |

---

## 9. 主要实验室最新成果

### 9.1 Meta AI

| Paper | Core Contribution |
|-------|------------------|
| **Credit Assignment with Resets in LLM Reasoning** | 重置机制改进 LLM 推理中的信用分配 |
| **HSTU** | 万亿参数生成式推荐系统 (ICML 2024, updated) |
| **ULTRA-HSTU** | 弯曲 scaling law 曲线 |
| **Foundation-Expert** | 基础模型+专家范式 |

### 9.2 ByteDance

| Paper | Core Contribution |
|-------|------------------|
| **Lance** | Unified multimodal model — 统一多模态理解生成 |
| **Precise** | SDE-Consistent Sampling for Flow-Matching RL (arXiv:2605.23522) |
| **RankMixer** | Scaling up ranking models with Mixer architecture |
| **HyFormer** | 序列 vs 特征交互统一 |
| **MixFormer** | 稠密与序列共缩放 |

### 9.3 Apple

| Paper | Core Contribution |
|-------|------------------|
| **SGE (Strategy-Guided Exploration)** | 树搜索策略指导 LLM Agent 探索，显著提升任务完成率 |

### 9.4 NVIDIA

| Paper | Core Contribution |
|-------|------------------|
| **Nemotron 3 Super** | Hybrid Mamba-Transformer MoE，性能超越同级 Transformer |
| **DiLaDiff** | Distilled Latent-Augmented Diffusion Language Model |

### 9.5 Meta + Cross-Lab

| Paper | Core Contribution |
|-------|------------------|
| **LiveAgentBench** | 跨 6 实验室的实时 Agent 评估基准 |

### 9.6 Microsoft Research Asia

| Paper | Core Contribution |
|-------|------------------|
| **SkillOpt** | Self-Evolving Agent Skills (arXiv:2605.23904) |

### 9.7 Google DeepMind

| Paper | Core Contribution |
|-------|------------------|
| **Gemini Embedding 2** | 新一代文本嵌入模型 |
| **AGI Cognitive Framework** | 通用人工智能认知框架 |

---

## 10. 综合趋势分析

### 10.1 顶会趋势总览（2026）

| 趋势 | 涉及会议/实验室 | 关键观察 |
|------|---------------|---------|
| **推理模型爆发** | ICML, ICLR, NeurIPS, KDD | 从思维链到搜索/反思/自博弈，推理成为所有顶会核心主题 |
| **推荐系统步入大模型时代** | SIGIR, WWW, RecSys, KDD | 生成式推荐超越传统检索-排序两阶段范式，LLM 深度融入 CTR |
| **MoE 成为主流** | 几乎所有实验室 | MoE 架构几乎成为所有新发布模型的标准配置 |
| **Hybrid Attention** | Meta, ByteDance, NVIDIA | Mamba+Transformer 混合架构开始挑战纯 Attention |
| **Agentic AI 全面爆发** | ICML, AAAI, KDD | 从单一工具使用到自主研究/代码生成/长期记忆的多 Agent 系统 |
| **RLVR 成为后训练标准** | NeurIPS, ICML | 从 RLHF 到可验证奖励，RL 再次成为 LLM 核心训练范式 |
| **Scaling Law 理论深化** | ICML, NeurIPS | Shannon 缩放律、Rademacher 复杂度、有效秩等更精细的理论工具 |
| **评估回归本质** | KDD, NeurIPS | BenchBench 等元评估工具揭示基准测试本身的质量危机 |

### 10.2 技术演进路径

1. **LLM 训练**: 纯 Attention → Hybrid Mamba-Transformer → 循环/扩散推理
2. **推荐系统**: ID Embedding → 生成式 → 推理增强 → 多模态端到端
3. **Agent 架构**: 单 Agent 工具使用 → 多 Agent 协作 → Agent Society → 全自动科研
4. **后训练**: RLHF → RLVR → Process Reward → Multi-turn Critic
5. **多模态**: 独立 VLM → 统一多模态自回归 → 世界模型

---

> **后续跟踪**: 重点关注 ICML 2026 完整接收论文列表、ACL 2026 主会程序、NeurIPS 2026 Call for Papers、各大实验室最新技术报告。
