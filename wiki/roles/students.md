---
title: 学习者导航
type: synthesis
created: 2026-06-02
updated: 2026-06-02
tags: [students, learners, education, courses, pedagogy]
---

# 学习者导航 — Student's & Learner's Guide

> 面向学生的本 wiki 学习路径。从 micrograd 的 100 行 autograd 到 Software 3.0 全景，覆盖 Karpathy 的课程、教学理念和由浅入深的知识阶梯。

---

## 总 — 学习路线全景

Karpathy 的教学设计有一条清晰的哲学：**ramps to knowledge** — 每一层剥离一个抽象，让学习者看到最本质的实现。从自动微分（micrograd）到完整的 chat 模型管线（nanochat），再到纯 C 的 LLM 训练（llm.c），每一步都是可运行、可理解的代码。

### 学习路径（由浅入深）

```
┌─────────────────────────────────────────────────────────┐
│  Step 1: CS231n / Zero to Hero → 理解基础               │
│  Step 2: micrograd → 手动实现 autograd                   │
│  Step 3: nanoGPT → 最小 GPT 预训练                       │
│  Step 4: nanochat → 完整 chat 模型管线                    │
│  Step 5: llm.c → 纯 C/CUDA 训练，底层原理                │
│  Step 6: Karpathy 2025-2026 概念 → 前沿理解              │
└─────────────────────────────────────────────────────────┘
```

---

## 分 — 按学习阶段

### 一、入门 — 深度学习基础

#### [[entities/zero-to-hero|Zero to Hero 系列]]
Karpathy 的 YouTube 教学系列，从零构建神经网络。核心内容：
- micrograd — 100 行实现 autograd
- nanoGPT — PyTorch 实现 GPT 预训练
- 配套视频逐步讲解

#### [[entities/cs231n|CS231n: Convolutional Neural Networks for Visual Recognition]]
Karpathy 在 Stanford 教授的经典课程。虽然教的是 CNN，但其教学风格和作业设计已体现了后来所有教学项目的 DNA。

#### [[entities/llm101n|LLM101n]]
Karpathy 设想的"LLM 版 CS231n" — 端到端 LLM 教学课程，目前属于概念阶段。

### 二、进阶 — 动手实践

#### 代码项目阶梯

| 项目 | 代码量 | 学习价值 | 入口 |
|------|--------|---------|------|
| [[entities/micrograd|micrograd]] | ~100 行 Python | 理解反向传播本质 | [[entities/zero-to-hero|Zero to Hero]] |
| [[entities/nanogpt|nanoGPT]] | ~300 行 PyTorch | 最小 GPT 训练 | GitHub + 视频 |
| [[entities/nanochat|nanochat]] | ~8000 行 | 完整模型管线（SFT → serving） | GitHub |
| [[entities/modded-nanogpt|modded-nanoGPT]] | — | 社区优化技巧 | GitHub |
| [[entities/llm-c|llm.c]] | ~3000 行 C/CUDA | LLM 训练底层原理 | GPU MODE IRL 2024 |

#### 关键实现锚点

- **micrograd**: One page of code, 完整 DAG 自动微分, 标量反向传播
- **nanoGPT**: "The simplest, fastest repository for training/finetuning medium-sized GPTs"
- **nanochat**: "Strong baseline" ramp to knowledge — 覆盖 pretrain → SFT → serve
- **llm.c**: 确定性内存分配、手写 CUDA kernel、无依赖、Packed128

### 三、高级 — 前沿概念

#### Karpathy 核心框架

| 概念 | 一句话 | 难度 |
|------|--------|------|
| [[concepts/software-3-0|Software 3.0]] | LLM 是新的操作系统 | ★★☆ |
| [[concepts/llm-os|LLM OS]] | 模型作为操作系统的类比 | ★★☆ |
| [[concepts/vibe-coding|Vibe Coding]] | 用自然语言描述需求写代码 | ★☆☆ |
| [[concepts/agentic-engineering|Agentic Engineering]] | Orchestrating coding agents 的专业学科 | ★★★ |
| [[concepts/verification-gap|Verification Gap]] | 生成成本归零但验证没变化 | ★★☆ |
| [[concepts/bacterial-code|Bacterial Code]] | 自包含、无依赖的代码风格 | ★★☆ |

#### 理解 LLM 能力

| 概念 | 核心观点 |
|------|---------|
| [[concepts/animals-vs-ghosts|Animals vs Ghosts]] | LLM 不是"另一种智能"，而是"非智能的镜子" |
| [[concepts/people-spirits|People Spirits]] | 用户把 LLM 当人是因为人类心智的"过度解读"本能 |
| [[concepts/ai-psychosis|AI Psychosis]] | LLM 在没有接地信号时的输出退化 |
| [[concepts/jagged-intelligence|Jagged Intelligence]] | AI 能力边界不规则 — 有些难事轻松，有些易事做不到 |

#### 学习与教育理念

| 概念 | 教学含义 |
|------|---------|
| [[concepts/ramps-to-knowledge|Ramps to Knowledge]] | 每层剥离一个抽象，逐步深入 |
| [[concepts/10000-hours|10,000 Hours]] | 深度专注 vs 碎片化学习的辩论 |
| [[concepts/eureka|Eureka]] | AI-native 个性化教育平台的愿景 |
| [[concepts/education|Education (X posts)]] | AI detectors 无效、in-class grading、AI-capable + AI-free |

### 四、学习资源汇总

- [[synthesis/technical-roadmap|技术路线图]] — 了解当前 AI 研究的完整版图
- [[concepts/|全部概念列表（53 个）]] — 按需查阅
- [[entities/andrej-karpathy|Andrej Karpathy 档案]] — 导师背景
