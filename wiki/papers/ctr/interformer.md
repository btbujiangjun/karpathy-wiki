---
title: "InterFormer: Effective Heterogeneous Interaction Learning for Click-Through Rate Prediction"
title-zh: "InterFormer: 面向点击率预测的高效异构交互学习"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Meta]
year: 2024
venue: arXiv
arxiv: 2411.09852
tags: [heterogeneous-interaction, transformer, ctr, meta]
category: ctr
---

## 问题背景

现有 CTR 模型对用户画像、上下文、行为序列等异构特征的处理通常使用相同架构，忽略了不同特征类型间的交互模式差异。

## 方法详述

提出 InterFormer 异构交互学习框架：

1. **异构特征编码器**：为用户画像（离散型）、上下文（稠密型）、行为序列（序列型）分别设计专用编码器
2. **异构交叉注意力**：不同类型特征之间的非对称交叉注意力机制
3. **交互路由机制**：学习哪些特征对之间应当进行深度交互，减少冗余计算
4. **多粒度聚合**：从细粒度（单特征）到粗粒度（特征域）的多层次输出聚合

## 主要创新点

1. 显式建模异构特征间的差异化交互模式
2. 交互路由减少 O(n²) 计算复杂度
3. 首个专门处理推荐异构交互的 Transformer 变体

## 实验结果对比

| 模型 | AUC | LogLoss | 推理时间 |
|------|-----|---------|---------|
| DCN-V2 | 0.8012 | 0.4410 | 1.0× |
| AutoInt | 0.8034 | 0.4390 | 1.2× |
| InterFormer | 0.8081 | 0.4340 | 1.1× |

## 局限性

异构路由策略在大规模（>10B 样本）场景下的稳定性未验证；对长尾特征的交互学习仍不够充分。
