---
title: "EST: Towards Efficient Scaling Laws in Click-Through Rate Prediction via Unified Modeling"
title-zh: "EST: 通过统一建模实现高效的点击率预测缩放定律"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Alibaba]
year: 2026
venue: arXiv
arxiv: 2602.10811
tags: [efficient-scaling, unified-modeling, ctr, alibaba]
category: ctr
---

## 问题背景

现有 CTR 模型的缩放研究通常忽略早期聚合（early aggregation）的局限性，导致模型扩展带来的收益被架构瓶颈限制。

## 方法详述

提出 EST 高效统一缩放方案：

1. **统一建模**：消除传统 DLRM 的 early aggregation 限制
2. **高效缩放架构**：在统一模型中实现特征交互的线性复杂度
3. **缩放律验证**：在阿里场景验证从 100M 到 10B 参数的缩放曲线
4. **计算-性能建模**：统一框架下的 FLOPs-AUC 映射关系
5. **渐进式扩展**：分阶段扩展的数据和模型策略

## 主要创新点

1. 揭示 early aggregation 对缩放的限制
2. 统一建模下的线性复杂度特征交互
3. 阿里场景的大规模缩放验证

## 实验结果对比

| 模型 | 参数量 | AUC | FLOPs/sample | 缩放弹性 |
|------|-------|-----|-------------|---------|
| DLRM | 500M | 0.7990 | 1.0× | 低 |
| DCN-V2 | 500M | 0.8030 | 1.5× | 中 |
| EST | 500M | 0.8060 | 1.2× | 高 |
| EST-5B | 5B | 0.8125 | 3.0× | 高 |

## 局限性

统一建模增加早期训练成本；线性复杂度特征交互在高阶交叉场景存在表达力上限。
