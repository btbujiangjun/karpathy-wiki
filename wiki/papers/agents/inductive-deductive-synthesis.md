---
title: "Inductive Deductive Synthesis: AI-Generated Formally Verified Systems"
title-zh: "归纳-演绎综合：AI 生成的正式验证系统"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Shubham Agarwal, Alexander Krentsel, Shu Liu, Mert Cemri, Audrey Cheng, Rui Meng, Tomas Pfister, Chun-Liang Li, Sylvia Ratnasamy, Aditya Parameswaran, Matei Zaharia, Ion Stoica, Mohsen Lesani]
year: 2026
arxiv: 2605.23109
affiliation: UC Berkeley, Microsoft
tags: [formal-verification, code-generation, agents]
category: agents
---

## 问题背景

LLM 可以生成代码但无法保证正确性。正式验证可以证明代码满足规约但编写验证证明门槛极高。本文结合两者，让 AI 生成经过正式验证的代码。

## 方法详述

归纳-演绎综合（IDS）框架包含两个交替阶段：

1. **归纳阶段**：LLM 从自然语言描述和示例中生成候选实现代码
2. **演绎阶段**：形式化验证工具（Lean/Coq）检查代码是否满足规约，失败则返回反例

两个阶段迭代循环直到验证通过或达到上限。

## 主要创新点

- AI + 形式化验证协同：LLM 提供生成能力，验证器提供保证能力
- 可证明正确的 AI 生成代码
- UC Berkeley + Microsoft 联合

## 实验结果与对比

| 方法 | 验证通过率 | 需要人工 |
|------|----------|---------|
| 纯 LLM 生成 | ~30% | 无 |
| LLM + 测试驱动 | ~45% | 编写测试 |
| IDS (本文) | ~78% | 形式规约 |

## 局限性

- 依赖形式规约编写，门槛高于写测试
- 迭代验证成本高
- 主要支持功能正确性，难以处理非功能属性
