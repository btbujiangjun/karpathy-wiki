---
title: "LiRank: Industrial Large Scale Ranking Models at LinkedIn"
title-zh: "LiRank: LinkedIn 工业级大规模排序模型"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [LinkedIn]
year: 2024
venue: arXiv
arxiv: 2402.06859
tags: [ranking, linkedin, industrial, quantization, transformer]
category: recommendation
---

## 问题背景

工业推荐系统中，需要在模型效果和推理延迟之间取得平衡。LinkedIn 面对全球数亿用户的 Feed 推荐场景，需要一个兼具表达力和效率的统一排序模型。

## 方法详述

提出 LiRank，融合 Residual DCN、Transformer 和 Dense Gating 的混合架构：

1. **Residual DCN (Deep & Cross)**：深度交叉网络的Feature Interaction能力
2. **Transformer 层**：Sequence Modeling和上下文感知
3. **Dense Gating**：动态特征选择机制
4. **量化与压缩**：训练后量化+Knowledge Distillation实现低延迟部署

## 主要创新点

1. Residual DCN + Transformer + Dense Gating 的混合架构
2. 大规模工业排序的量化与压缩经验
3. LinkedIn Feed 场景的全量部署验证

## 实验结果对比

| 组件 | AUC 贡献 | 延迟影响 |
|------|---------|---------|
| Base DLRM | 基线 | 1ms |
| +Transformer | +0.4% | +0.5ms |
| +Dense Gating | +0.2% | +0.1ms |
| +量化压缩 | 无损 | -40% |

## 局限性

架构设计针对 Feed 场景优化，迁移到其他场景需调优；量化部署依赖硬件支持。
