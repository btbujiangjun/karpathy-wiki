---
title: 工程实践者导航
type: synthesis
created: 2026-06-02
updated: 2026-06-02
tags: [engineers, practitioners, coding, systems, tools]
---

# 工程实践者导航 — Engineering Practitioner's Guide

> 以代码实现为事实依据，综述本 wiki 中面向工程实践者的技术文档。所有内容锚定在 Karpathy 实际开源代码（llm.c, nanochat, nanogpt, micrograd 等）的实现细节之上。

---

## 总 — Engineering Substrate Overview

Karpathy 的工程思想有一条清晰的主线：**剥离抽象层，回归计算本质**。从 micrograd 的 100 行 autograd，到 llm.c 的纯 C/CUDA GPT-2 训练，再到 agentic-engineering 时代的编码方法论，所有内容都锚定在可运行的代码实现之上。

### 核心工程项目（按抽象层次排列）

| 项目 | 代码量 | 核心实现 |
|------|--------|----------|
| [[micrograd]] | ~100 行 Python | 标量 autograd 引擎，完整实现反向传播 |
| [[nanogpt]] | ~300 行 PyTorch | 最小化 GPT 预训练实现 |
| [[nanochat]] | ~8000 行 | 全流程 chat 模型：SFT → serving |
| [[llm-c]] | ~3000 行 C/CUDA | GPT-2 1.6B 纯 C 训练，手写 CUDA kernel |
| [[modded-nanogpt]] | — | 社区优化版 nanogpt |
| [[llm-council]] | — | 多模型编排应用（vibe-coded） |
| [[nanoclaw]] | — | 2026 agentic 工具 |

### 关键实现细节（代码即事实）

- **llm.c**: 所有内存启动时预分配，零动态分配，完全确定性无 OOM；`Packed128` 数据结构强制 NVCC 生成 128-bit load/store 指令；CUDA streams 被尝试后移除（"Ctrl-F for stream and nuke it"）；NCCL + ZeRO-1 支持多 GPU
- **nanochat**: 全流程管线（pretrain → SFT → serve）；GPT-2 用 $20 在 8×H100 上复现
- **micrograd**: 单文件标量 autograd，One page of code 即可学会 backprop 端到端
- **nanogpt**: torch.compile errors 触发了 llm.c 的诞生

### 工程范式演进

[[vibe-coding]]（2025 初）→ [[agentic-engineering]]（2026.2，正式命名）→ [[bacterial-code]] 风格 + [[verification-gap]] 意识

Agentic Engineering 核心实践（源自 Karpathy 2026.1.27 实际工作流）：
1. 给 success criteria，不给 step-by-step
2. 先写测试再通过
3. Naive correct → 要求优化且保持正确性
4. Declarative over imperative
5. 同时运行多个并发 agent（多个 Claude Code session + IDE）

---

## 分 — Technical Documentation

### 一、代码项目深度分析

#### 1.1 底层系统级

- [[entities/llm-c|llm.c 实现详解]] — CUDA kernel 手写、Packed128、确定性内存、NCCL ZeRO-1、训练性能（1 H100 node / 24h / ~$600）
- [[entities/micrograd|micrograd 实现详解]] — 100 行反向传播引擎，完整 DAG 自动微分

#### 1.2 训练管线

- [[entities/nanogpt|nanoGPT 实现详解]] — 最小 PyTorch GPT 预训练
- [[entities/nanochat|nanochat 全流程]] — 从 raw text 到 deployed chat 的完整管线（SFT + serving）
- [[entities/nanoclaw|nanoclaw]] — 2026 年的 agentic tool

#### 1.3 产品级工程

- [[entities/menugen|MenuGen]] — "weekend vibe-coded app" 的生产化案例：实际 1 周上线，大部分时间花在 DevOps 而非编码
- [[entities/modded-nanogpt|modded-nanoGPT]] — 社区驱动的 nanogpt 优化版本
- [[entities/llm-council|llm-council]] — 多模型编排的 vibe-coded 应用

### 二、工程概念与方法论

| 概念 | 核心主张 | 代码关联 |
|------|---------|----------|
| [[concepts/vibe-coding|Vibe Coding]] | 用自然语言描述需求让 LLM 写代码 | MenuGen 项目实战，DevOps crunch > 代码编写 |
| [[concepts/agentic-engineering|Agentic Engineering]] | Orchestrating agents + oversight 的专业学科 | Karpathy 2026.1.27 Claude 工作流实录 |
| [[concepts/bacterial-code|Bacterial Code]] | 自包含、无依赖、易提取的代码风格 | nanochat/fp8.py — 150 行 fp8 训练实现，比 torchao 快 3% |
| [[concepts/verification-gap|Verification Gap]] | Generation 成本归零但 Discrimination 成本不变 | Amdahl's law 分析，LLM 代码生成的根本瓶颈 |
| [[concepts/build-for-agents|Build for Agents]] | 设计让 LLM agent 易于使用的 API 和基础设施 | 逆 vibe-coding：不是给人写，是给机器写 |
| [[concepts/context-engineering|Context Engineering]] | 构造 LLM 上下文来引导行为 | Karpathy 高度认可的技术 |

### 三、工具与产品

| 实体 | 类型 | 来源相关性 |
|------|------|-----------|
| [[entities/claude-code|Claude Code]] | 产品 | Karpathy 主力 agentic coding 工具 |
| [[entities/cursor|Cursor]] | 产品 | AI-native IDE |
| [[entities/model-context-protocol|MCP]] | 协议 | Agent-tool 交互标准 |
| [[entities/github|GitHub]] | 平台 | Karpathy 代码托管 |
| [[entities/pytorch|PyTorch]] | 框架 | nanogpt 依赖 | 
| [[entities/hugging-face|Hugging Face]] | 平台 | 模型权重分发 |

### 四、相关论文中的工程视角

| 论文类别 | 工程关注点 |
|---------|-----------|
| [[papers/llm-training/|LLM Training & Theory]] | 训练效率、scaling law 工程含义 |
| [[papers/ctr/|CTR Prediction]] | 工业级 ranking 系统的工程架构（ByteDance/Meta/Alibaba 经验） |
| [[papers/agents/|Agent Systems]] | Agent 系统的编排、memory、persistence 工程实现 |
| [[papers/code-reasoning/|Code & Formal Reasoning]] | 代码生成、验证、测试的工程方法 |

### 五、系统与实践建议

1. **学习路径**: micrograd → nanoGPT → nanochat → llm.c（每层剥离一个抽象）
2. **当前最佳实践**: Agentic Engineering + Bacterial Code + Tests-First
3. **避免陷阱**: Verification Gap 是实际瓶颈，依赖膨胀是安全风险（[[supply-chain-attacks]]）
