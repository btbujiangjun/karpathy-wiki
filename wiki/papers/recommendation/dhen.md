---
title: "DHEN: A Deep and Hierarchical Ensemble Network for Large-Scale Click-Through Rate Prediction"
title-zh: "DHEN: 面向大规模点击率预测的深度层次集成网络"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Meta]
year: 2022
venue: arXiv
arxiv: 2203.11014
tags: [ensemble, hierarchical, efficiency, meta]
category: recommendation
---

## 问题背景

工业 CTR 模型在规模扩展时面临异构特征交互的高计算开销，传统 DLRM 的 MLP 交叉层无法有效建模多层次特征关系。

## 方法详述

提出深度层次集成网络：

1. **层次异构集成**：将特征划分为多个层次（用户层、物品层、上下文层），每层使用异构交互模块
2. **层次间门控融合**：自顶向下的门控机制逐层融合多层次表征
3. **协同训练系统**：与训练框架协同设计，支持模型并行与数据并行
4. **层次剪枝**：推理时根据重要性动态跳过部分层次

## 主要创新点

1. 首次将层次集成思想引入 CTR 大规模建模
2. 模型-系统协同设计（co-design）
3. 异构交互模块的灵活组合
4. 训练效率显著提升

## 实验结果对比

| 指标 | DLRM | DCN-V2 | DHEN |
|------|------|--------|------|
| AUC 提升 | - | +0.08% | +0.37% |
| 训练吞吐 (samples/s) | 1.0× | 1.1× | 1.8× |
| 参数量 | 100% | 135% | 95% |

## 局限性

层次划分依赖领域知识；异构模块的选择缺乏自动化；集成架构的推理延迟控制仍需优化。
