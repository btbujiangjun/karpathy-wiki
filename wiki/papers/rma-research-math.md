---
title: "RMA: An Agentic System for Research-Level Mathematical Problems"
title-zh: "RMA：面向研究级数学问题的智能体系统"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Zelin Zhao, Bo Yuan, Jaemoo Choi, Yongxin Chen]
year: 2026
arxiv: 2605.22875
tags: [agents, mathematics, problem-solving, code-execution]
category: code-reasoning
---

## 问题背景

数学推理是衡量 AI 能力的重要标尺。现有 LLM 在竞赛数学（如 MATH、IMO）上已有不错表现，但在**研究级数学问题**上——需要创造性思维、多步推理、以及检索/组合已知理论——LLM 的能力仍然有限。RMA 探索使用 Agent 系统来应对研究级数学问题。

## 方法详述

RMA（Research Math Agent）是一个多工具 Agent 系统：

1. **知识检索**：从数学论文和知识库中检索相关定理和已知结果
2. **符号计算**：调用符号计算工具（如 SymPy、Mathematica）进行精确推导
3. **假设验证**：生成中间假设并用反例搜索验证其有效性
4. **策略规划**：将问题分解为子问题，规划解决路径

## 主要创新点

- 将 Agent 方法论应用于研究级数学而非竞赛数学
- 工具集成（检索 + 符号计算 + 验证）解决需要外部知识的数学问题
- 探索 AI 在真实数学研究中的应用边界

## 局限性

- 研究级数学问题的验证标准难以自动化（需要人工判断"是否有洞察"）
- 工具调用的准确率限制了系统的整体可靠性
- 需要数学专家评估输出质量，规模化评测困难
