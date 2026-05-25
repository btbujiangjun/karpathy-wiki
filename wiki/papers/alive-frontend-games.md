---
title: "Bringing Code ALIVE: Optimizing Interactive Frontend Mini-Games Via Automated Play and Reinforcement Learning at Scale"
title-zh: "ALIVE：通过自动化游玩和 RL 优化交互式前端小游戏"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Jiajun Zhang, Yuheng Jing, Zeyu Cui, Hao Zheng, Wentao Chen, Kaixin Li, Jiaxi Yang, Tianbao Xie]
year: 2026
venue: ICML 2026
tags: [frontend-games, rl, code-generation, interactive]
category: games
---

## 问题背景

评估 LLM 生成的前端交互式小游戏面临可扩展性与可靠性之间的权衡——现有方法要么无法捕捉动态交互性，要么计算成本过高。如何在规模化场景下自动评估和优化生成游戏的质量是核心挑战。

## 方法详述

ALIVE (Aligning LLMs via Interactive Visual Execution) 高通量框架：

1. **一次性规划（One-Shot Planning）**：基于用户需求一次性生成完整游戏
2. **基于 DOM 的分析**：自动化游戏质量评估管道，分析交互元素的合理性和游戏性
3. **视觉执行反馈的 RL 优化**：结合游戏执行结果的强化学习优化

## 主要创新点

1. 自动化的游戏质量评估管道
2. 结合视觉执行反馈的 RL 优化
3. 实现大规模并行化部署（6670 FPS）

## 实验结果对比

| 评估方式 | 现有方法 | ALIVE |
|---------|---------|-------|
| 自动化评分 | 基线 | +31% |
| 人工评估偏好 | 基线 | +24% |
| 推理速度 | 受限 | 6670 FPS |

## 局限性

仅适用于基于 DOM 分析的网页游戏；对复杂 3D 游戏评估能力有限。
