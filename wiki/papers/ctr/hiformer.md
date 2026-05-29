---
title: "Hiformer: Heterogeneous Feature Interactions Learning with Transformers for Recommender Systems"
title-zh: "Hiformer: 面向推荐系统的异构特征交互Transformer学习"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Google]
year: 2023
venue: arXiv
arxiv: 2311.05884
tags: [heterogeneous, feature-interactions, transformer, google]
category: ctr
---

## 问题背景

推荐系统的特征具有高维稀疏特性，且不同特征（用户、物品、上下文）的交互模式差异显著，标准 Transformer 难以有效处理异构特征。

## 方法详述

提出 Hiformer 异构特征交互 Transformer：

1. **异构编码**：不同类型特征的差异化嵌入策略（稀疏、稠密、序列）
2. **可学习的交互模式**：每层注意力学习特征的交互拓扑
3. **稀疏输入优化**：针对高维稀疏输入的稳定性机制
4. **分层聚合**：特征域级别的层次聚合
5. **Google 场景验证**

## 主要创新点

1. 可学习的特征交互拓扑
2. 异构特征的统一 Transformer 建模
3. 稀疏高维输入的处理方案

## 实验结果对比

| 模型 | AUC | LogLoss | 参数量 | 特征扩展性 |
|------|-----|---------|-------|-----------|
| DCN | 0.7930 | 0.4490 | 50M | 中 |
| AutoInt | 0.7970 | 0.4450 | 80M | 中 |
| Hiformer | 0.8015 | 0.4410 | 100M | 优 |

## 局限性

交互拓扑学习的收敛速度较慢；异构编码的设计需要人工调优。
