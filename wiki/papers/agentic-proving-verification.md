---
title: "Agentic Proving for Program Verification"
title-zh: "面向程序验证的智能体化证明方法"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Alessandro Sosso, Akhil Arora, Bas Spitters]
year: 2026
arxiv: 2605.23772
tags: [code-execution, formal-verification, agents, program-verification]
category: code-reasoning
---

## 问题背景

程序验证（Program Verification）——证明程序满足给定规约——通常需要深厚的专业知识和大量手工劳动。LLM 有潜力自动化这一过程，但直接生成的验证证明往往不完整或包含错误。本文提出使用智能体（Agent）系统，让 LLM 以"代理"的形式自主完成程序验证任务。

## 方法详述

**Agentic Proving 流程：**
1. **规约理解**：Agent 分析给定的程序规约（如 Hoare triple 或 ACSL 注解）
2. **验证策略选择**：Agent 选择适合的验证策略（如符号执行、归纳推理、抽象解释）
3. **证明构建**：Agent 逐步构建验证证明，每一步使用 LLM 生成并让验证器检查
4. **错误恢复**：当证明步骤错误时，Agent 分析错误原因并调整策略

## 主要创新点

- 将程序验证建模为 Agent 任务，而非一次性生成任务
- 结合 LLM 的生成能力和验证工具的检查能力
- 结构化的多步骤验证流程替代end-to-end的黑盒生成

## 局限性

- 验证过程依赖 LLM 的理解，复杂规约可能被误解
- 当前主要验证简单到中等复杂度的程序
- Agent 的推理步数限制了可验证的程序规模
