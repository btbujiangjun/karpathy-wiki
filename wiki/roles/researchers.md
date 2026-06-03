---
title: AI/ML 研究人员导航
type: synthesis
created: 2026-06-02
updated: 2026-06-02
tags: [researchers, papers, methods, theoretical]
---

# AI/ML 研究人员导航 — Researcher's Guide

> 面向 AI/ML 研究者的本 wiki 论文与方法综述。覆盖 76+ 篇论文摘要、7 种方法文档、53 个概念中的理论内容。

---

## 总 — 研究全景

本 wiki 的论文体系覆盖 9 个研究方向，跨 30+ 机构（含学术界与工业界），时间跨度 2024–2026。核心研究主题包括：

### 当前研究热点（基于 arXiv 每日追踪）

1. **LLM Training & Theory**: Scaling law 精细化（Shannon Scaling Law）、Diffusion LM、MoE 超参数迁移
2. **CTR Prediction / Recommendation Scaling**: 工业界最活跃的 scaling law 战场，49+ 篇论文
3. **Agent Systems**: Multi-agent 协调、self-evolving agents、长期记忆
4. **Game & Strategic Reasoning**: RL 驱动的策略推理、多轮 decision-making
5. **Generative Models**: Flow Matching RL、Video Diffusion 加速
6. **Code & Formal Reasoning**: Agentic proving、neurosymbolic optimization

### 关键交叉发现

- CTR scaling law 方法（EST, FAT, SUAN）与 LLM training scaling law 共享理论基础
- RLVR / 可验证奖励 从 LLM 后训练渗透到 recommendation（RPORec）
- Diffusion 模型被应用于 LLM reasoning（LaDiR）和推荐（GE4Rec）两个领域

---

## 分 — 按研究方向

### 🧠 LLM Training & Theory — [[papers/llm-training/|8 篇论文]]

| 论文 | 核心贡献 | 机构 |
|------|---------|------|
| [[papers/llm-training/shannon-scaling-law|Shannon Scaling Law]] | LLM 作为噪声信道的新 scaling law 框架 | ICML 2026 |
| [[papers/llm-training/gated-attention|Gated Attention]] | NeurIPS 2025 Best Paper | — |
| [[papers/llm-training/transformers-inherently-succinct|Transformers are Inherently Succinct]] | ICLR 2026 Outstanding | — |
| [[papers/llm-training/complete-mue-moe|Complete-muE]] | MoE 超参数迁移方法 | — |

### 📊 Recommendation — [[papers/recommendation/|15 篇论文]]

工业推荐系统的 scaling law 研究前沿，Meta (HSTU, Kunlun, Wukong)、Netflix、LinkedIn、Airbnb、Kuaishou 等机构的最新成果。

| 关键论文 | 核心发现 |
|---------|---------|
| [[papers/recommendation/hstu-generative-recommendation|HSTU]] | Generative recommendation 范式，万亿级参数 |
| [[papers/recommendation/kunlun-scaling-law|Kunlun]] | 统一架构的 scaling law |
| [[papers/recommendation/wukong-scaling-law|Wukong]] | 大规模推荐系统 scaling law（ICML 2024） |

### 🎯 CTR Prediction — [[papers/ctr/|36 篇论文]]

最活跃的研究方向，覆盖 ByteDance、Meta、Alibaba、Kuaishou、Tencent 等工业巨头的实际系统经验。

| 子方向 | 代表论文 |
|--------|---------|
| Scaling Law 方法论 | [[papers/ctr/est|EST]], [[papers/ctr/fat-ctr-scaling|FAT]], [[papers/ctr/suan-ctr-scaling|SUAN]] |
| 超长用户序列 | [[papers/ctr/longer|LONGER]], [[papers/ctr/make-it-long-keep-it-fast|Make It Long]], [[papers/ctr/muse|MUSE]] |
| Decoder-only CTR | [[papers/ctr/cadet|CADET]]（LinkedIn, Decoder-Only Ads CTR） |
| LLM + CTR | [[papers/ctr/chime|CHIME]], [[papers/ctr/onepiece|OnePiece]] |

### 🤖 Agents — [[papers/agents/|7 篇论文]]

Research automation、self-evolving agents、agentic 社会协调。

### 🎮 Games — [[papers/games/|10 篇论文]]

LLM strategic reasoning、RL in games、lifelong learning。

### 🎨 Generative Models — [[papers/generative-models/|4 篇论文]]

Flow matching RL、video diffusion、unified multimodal AR。

### 💻 Code & Reasoning — [[papers/code-reasoning/|5 篇论文]]

Agentic proving、neurosymbolic optimization、tree-search code gen。

### 🔄 Sequential Modeling — [[papers/sequential-modeling/|2 篇论文]]

Retrieval dimensionality barrier、hysteretic attention。

### 📐 Benchmarking — [[papers/benchmarking/|1 篇论文]]

Benchmark rigging analysis。

---

## 方法文档

| 方法 | 来源论文数 | 核心思想 |
|------|-----------|---------|
| [[methods/reinforcement-learning|Reinforcement Learning]] | 4 篇 | RL framework + 变体 |
| [[methods/hierarchical-group-policy-optimization|HGPO]] | 1 | 分层组策略优化 |
| [[methods/pcsp-shared-policy|PCSP]] | 1 | 人设条件共享策略 |
| [[methods/structured-test-time-learning|Structured Test-Time Learning]] | 1 | Test-time 结构化 learning |
| [[methods/cross-entropy-curriculum|Cross-Entropy Curriculum]] | 1 | 游戏课程学习 |
| [[methods/sde-consistent-sampling|SDE-Consistent Sampling]] | 1 | Flow matching 的 SDE 一致性采样 |
| [[methods/turn-level-critic|Turn-Level Critic PPO]] | 1 | 回合级 critic PPO |

## 综合研究资源

- [[synthesis/ctr-scaling-landscape|CTR Scaling 全景]] — 49 篇论文的 CTR scaling law 综合分析
- [[synthesis/technical-roadmap|技术路线图]] — 跨 121 篇论文的研究方向汇总
- [[synthesis/affiliation-landscape|机构研究分布]] — 121 篇论文的机构归属分析
- [[synthesis/conference-digest-2026-06-01|顶会论文专题报告]] — 10 会议 60+ 篇论文的跨会分析
