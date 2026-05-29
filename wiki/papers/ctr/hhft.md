---
title: "HHFT: Hierarchical Heterogeneous Feature Transformer for Recommendation Systems"
title-zh: "HHFT: 面向推荐系统的层次异构特征Transformer"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Alibaba]
year: 2025
venue: arXiv
arxiv: 2511.20235
tags: [hierarchical, heterogeneous, transformer, alibaba]
category: ctr
---

## 问题背景

DNN 在处理大规模异构推荐特征时存在容量瓶颈，Transformer 虽然表达能力更强但缺乏针对异构特征的层次化设计。

## 方法详述

提出 HHFT 层次异构特征 Transformer：

1. **层次划分**：按特征语义和粒度分层（粗粒度：用户画像 / 中粒度：场景上下文 / 细粒度：物品属性）
2. **层内-层间双重注意力**：层内 self-attention 建模同层交互，层间 cross-attention 建模跨层交互
3. **层次压缩**：高维特征在进入上层前自动降维
4. **异构编码器**：不同类型特征的差异化编码策略
5. **端到端训练**：层次间梯度直通

## 主要创新点

1. 层次异构的显式建模
2. 层内-层间双重注意力机制
3. 特征的层次自动压缩

## 实验结果对比

| 模型 | AUC | 参数量 | 训练速度 |
|------|-----|-------|---------|
| DCN-V2 | 0.8045 | 150M | 1.0× |
| AutoInt | 0.8070 | 180M | 0.9× |
| HHFT | 0.8105 | 200M | 0.8× |

## 局限性

层次划分的粒度和数量需要人工设定；层间注意力的计算量随层数呈二次增长。
