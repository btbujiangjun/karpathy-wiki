---
title: "MixFormer: Co-Scaling Up Dense and Sequence in Industrial Recommenders"
title-zh: "MixFormer: 工业推荐中稠密特征与序列特征的联合扩展"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [ByteDance]
year: 2026
venue: arXiv
arxiv: 2602.14110
tags: [co-scaling, user-item-decoupled, dense-sequence, bytedance]
category: ctr
---

## 问题背景

推荐模型中稠密特征（用户画像、物品属性）和序列特征（用户行为序列）的缩放行为不同，独立扩展可能导致性能瓶颈错配。

## 方法详述

提出用户-物品解耦的联合缩放架构 MixFormer：

1. **用户-物品解耦**：不含广告/物品侧序列，仅用户侧有行为序列
2. **稠密-序列联合缩放**：两种特征的统一缩放框架
3. **门控融合**：可学习的稠密-序列融合门控
4. **非对称计算分配**：稠密和序列使用不同的计算预算分配策略
5. **工业验证**：抖音场景的端到端部署

## 主要创新点

1. 用户-物品解耦架构（无广告侧序列）的正式化
2. 稠密-序列联合缩放视角
3. 非对称计算分配的量化建模

## 实验结果对比

| 缩放策略 | AUC | 计算增量 (dense:seq) |
|---------|-----|---------------------|
| 仅扩展稠密 | +0.18% | +50%:0% |
| 仅扩展序列 | +0.35% | 0%:+80% |
| 非对称 (MixFormer) | +0.45% | +30%:+50% |

## 局限性

无广告侧序列可能损失部分交叉信息；非对称分配策略需要场景特定调参。
