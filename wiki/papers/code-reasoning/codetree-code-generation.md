---
title: "CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models"
title-zh: "CodeTree: 智能体引导的树搜索代码生成"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Salesforce Research]
year: 2025
venue: NAACL 2025 / ACL Related
tags: [code-generation, tree-search, multi-agent, code-generation]
category: code-reasoning
---

## 问题背景

复杂编码任务搜索空间大，当前智能体方法在多阶段规划、生成和调试中仍有困难。单一 LLM 在需要多步推理的复杂编程任务中容易出错，缺乏系统性的错误纠正机制。

## 方法详述

统一树结构显式探索不同编码策略，Critic agent 引导树搜索决策：

1. **多智能体协作**：Thinker（规划编码策略）、Solver（实现代码）、Debugger（识别和修复错误）
2. **Critic 引导的树搜索**：排序、终止、扩展三种操作控制搜索过程
3. **统一树结构搜索空间**：将多种编码策略纳入同一搜索框架

## 主要创新点

1. 统一的树结构搜索空间
2. 多智能体专业化协作
3. Critic 驱动的搜索决策

## 实验结果对比

| 基准 | 现有方法 SOTA | CodeTree |
|------|-------------|----------|
| HumanEval | ~90% | 95.1% |
| MBPP | ~87% | 98.7% |
| CodeContests | ~35% | 43.0% |
| SWE-bench | 基线 | 显著提升 |

## 局限性

需要强推理能力的 LLM 作为基座；多智能体系统的计算开销较大。
