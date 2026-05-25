---
title: "FAT: From Scaling to Structured Expressivity — Rethinking Transformers for CTR Prediction"
title-zh: "FAT: 从缩放到结构化表达力——重新思考 CTR 预测的 Transformer 架构"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Alibaba]
year: 2025
venue: arXiv
arxiv: 2511.12081
tags: [fat, scaling-law, rademacher, ctr, transformer, alibaba]
category: ctr
---

## 问题背景

Transformer 在 NLP/CV 中表现优异，但在 CTR 预测中是否真的需要复杂Attention来建模Feature Interaction？现有工作主要关注参数数量对性能的影响，缺乏对表征复杂度（expressivity）的正式分析。

## 方法详述

提出 Field-Aware Transformer (FAT)，基于 Rademacher 复杂度首次给出 CTR 模型的正式缩放律：

1. **域感知分解 (Field-Aware Decomposition)**：将Feature Interaction分解为域内和跨域交互，减少参数浪费
2. **内容对齐 (Content Alignment)**：通过内容对齐机制提高交互层的有效秩
3. **Rademacher 复杂度分析**：从理论上证明 FAT 的表达力缩放边界，形式化参数-性能关系

## 主要创新点

1. 首个基于 Rademacher 复杂度的 CTR 缩放律（理论证明）
2. 域感知分解降低冗余交互计算
3. 内容对齐提升深层表示的有效秩

## 实验结果对比

| 方法 | 参数量 | AUC | 理论缩放边界 |
|------|-------|-----|------------|
| 标准 Transformer | 1× | 基线 | 未知 |
| FAT | 0.6× | +0.5% | O(√(d log n)) |
| DLRM | 0.5× | -0.2% | O(d) |

## 局限性

Rademacher 复杂度上界可能在大规模场景下较为宽松；域划分策略依赖人工设定。
