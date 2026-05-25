---
title: "Wukong: Towards a Scaling Law for Large-Scale Recommendation"
title-zh: "Wukong: 面向大规模推荐的缩放定律"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Meta AI]
year: 2024
venue: ICML 2024
arxiv: 2403.02545
tags: [scaling-laws, recommendation, meta, dlrm]
category: recommendation
---

## 问题背景

深度学习推荐模型（DLRM）在工业界广泛应用，但其缩放行为缺乏系统研究。不同于 NLP/CV 中观察到的清晰Scaling Law，推荐模型的Feature Interaction模式复杂、输入稀疏，缩放规律尚不明确。

## 方法详述

提出 Wukong 框架，采用分解式堆叠交互层（Factorized Stacked Interaction Layers）实现参数有效缩放：

1. **分解式交互层**：将Feature Interaction分解为多个子层，每层捕获特定阶数的交互
2. **渐进式扩展**：通过增加交互层数而非层宽度来扩展模型容量
3. **缩放分析**：系统研究模型大小、数据量与计算量对推荐性能的影响

## 主要创新点

1. 首次在推荐系统中验证参数缩放的有效性
2. 提出适用于推荐场景的分解式架构
3. 建立推荐模型缩放的方法论框架

## 实验结果对比

| 规模 | 小模型 | 中模型 | 大模型 (Wukong) |
|------|-------|-------|----------------|
| 参数量 | 100M | 500M | 1B+ |
| AUC | 基线 | +0.3% | +0.8% |
| 线上指标 | 基线 | +1.5% | +3.2% |

## 局限性

缩放收益在大规模数据上边际递减；分解式架构在极端稀疏特征上的效率需优化。
