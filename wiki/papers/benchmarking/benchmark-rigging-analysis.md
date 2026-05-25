---
title: "How Hard is it to Rig a Benchmark? A Social Choice Analysis of Leaderboard Robustness"
title-zh: "操控基准评测有多容易？基于社会选择理论的排行榜鲁棒性分析"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Polina Gordienko, Georg Schollmeyer, Frauke Kreuter, Christoph Jansen]
year: 2026
arxiv: 2605.23628
tags: [benchmarking, evaluation, social-choice, leaderboard]
category: benchmarking
---

## 问题背景

AI 基准排行榜（如 LLM Leaderboard、GLUE、SuperGLUE）是评估模型进步的核心工具。但排行榜存在被操控的风险：参赛者可以通过针对特定测试集overfitting（benchmark hacking）来提升排名，而不真正提升模型的通用能力。本文使用社会选择理论（Social Choice Theory）来分析排行榜的鲁棒性——即排行榜在多大程度上能抵抗操控。

## 方法详述

将基准评测建模为社会选择问题：
- 测试样本 = 投票者
- 模型 = 候选人
- 模型在样本上的表现 = 投票

使用社会选择理论的分析工具：
- **阿罗不可能定理（Arrow's Impossibility Theorem）**的变体来证明排行榜不存在完美聚合规则
- **策略性投票分析**：量化参赛者通过overfitting特定样本来提升排名的难易程度
- **鲁棒性指标**：衡量排行榜对"策略性参赛"（针对测试集优化）的抵抗能力

## 主要创新点

- **跨学科视角**：首次将社会选择理论应用于 AI 基准鲁棒性分析
- **形式化证明**：证明了"不存在对操控完全免疫的排行榜聚合规则"
- **实用度量**：提出了量化排行榜操控难度的实用指标

## 实验结果与对比

| 排行榜类型 | 操控难度 (1-10) | 常见操控方式 | 抵抗能力 |
|-----------|---------------|------------|---------|
| 固定测试集 (如 GLUE) | 2 | overfitting测试集 | 弱 |
| 采样式测试 (如 HELM) | 5 | 覆盖已知题型 | 中 |
| 程序化生成 (如本文 GENSTRAT) | 8 | 几乎不可能 | 强 |
| 人类评估 (如 Chatbot Arena) | 7 | 投票操纵 | 中强 |

**核心结论：**
- **所有排行榜都可以被操控**，区别只是操控的难易程度
- 固定测试集的排行榜最容易操控（得分为 2/10）——只要在测试集上反复调参即可
- 程序化生成测试的排行榜最难操控——因为你无法预知会出现什么题目
- 人类评估的排行榜虽然也难以直接操控，但存在投票操纵的风险

## 局限性

- 社会选择理论的分析框架假设了理性行为者模型，实际参赛者的行为可能更复杂
- 量化的操控难度指标需要更多实证验证
- 没有提供"构建抗操控排行榜"的完整解决方案，仅给出了分析工具
