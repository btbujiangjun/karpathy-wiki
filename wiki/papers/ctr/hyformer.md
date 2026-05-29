---
title: "HyFormer: Revisiting the Roles of Sequence Modeling and Feature Interaction in CTR Prediction"
title-zh: "HyFormer: 重新审视序列建模与特征交互在CTR预测中的角色"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [ByteDance]
year: 2026
venue: arXiv
arxiv: 2601.12681
tags: [sequence-modeling, feature-interaction, architecture, bytedance]
category: ctr
---

## 问题背景

主流 CTR 模型同时包含序列建模（用户行为序列）和特征交互（多域特征交叉）模块，但两者在缩放中的各自贡献和最优资源分配尚不明确。

## 方法详述

系统重审序列建模与特征交互在 CTR 中的角色关系：

1. **解耦分析**：单独控制序列建模和特征交互的计算预算，观察各自对 AUC 的边际贡献
2. **交叉对比实验**：在固定总 FLOPs 下，调整序列建模/特征交互的算力分配比例
3. **效率约束下的最优分配**：给定推理延迟预算时的最优设计方案
4. **混合架构设计**：依据分析结论设计的 HyFormer 架构

## 主要创新点

1. 首次系统量化序列建模 vs 特征交互的边际收益
2. 揭示两者在 CTR 中的非线性互补关系
3. 提供效率约束下的架构设计指南

## 实验结果对比

| 算力分配 (序列:交互) | AUC | 综合收益 |
|---------------------|-----|---------|
| 25%:75% | 0.8050 | - |
| 50%:50% | 0.8095 | 最优 |
| 75%:25% | 0.8080 | - |
| HyFormer 自适应 | 0.8110 | 自适应最优 |

## 局限性

结论基于 ByteDance 特定场景；序列-交互最优比例可能随数据分布变化。
