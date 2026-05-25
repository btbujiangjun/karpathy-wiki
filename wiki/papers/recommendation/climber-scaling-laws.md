---
title: "Climber: Toward Efficient Scaling Laws for Large Recommendation Models"
title-zh: "Climber: 面向大规模推荐模型的高效缩放定律"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [NetEase]
year: 2025
venue: WWW 2025
arxiv: 2502.09888
tags: [scaling-laws, online-scaling, netease, multi-scale]
category: recommendation
---

## 问题背景

推荐模型缩放的研究大多停留在离线验证阶段，如何在线上实际业务中持续、稳定地缩放模型缺乏公开经验。

## 方法详述

Climber 是首个公开文档化的持续线上缩放系统：

1. **多尺度序列提取 (Multi-Scale Sequence Extraction)**：从用户行为中提取不同时间粒度的序列特征
2. **动态温度调制 (Dynamic Temperature Modulation)**：根据训练阶段自适应调整 softmax 温度，改善收敛
3. **持续缩放机制**：逐步增加模型容量而不影响线上服务稳定性

## 主要创新点

1. 首个公开的持续线上缩放案例
2. 多尺度序列提取架构
3. 动态温度调制稳定训练

## 实验结果对比

| 缩放阶段 | 参数量 | 线上指标提升 | 累积提升 |
|---------|-------|------------|---------|
| 阶段 1 | 100M | +1.0% | +1.0% |
| 阶段 2 | 300M | +0.8% | +1.8% |
| 阶段 3 | 500M | +0.5% | +2.3% |

## 局限性

缩放收益边际递减；持续缩放需要配套的基建和 DevOps 支持。
