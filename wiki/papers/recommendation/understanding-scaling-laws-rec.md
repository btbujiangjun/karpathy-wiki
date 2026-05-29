---
title: "Understanding Scaling Laws for Recommendation Models"
title-zh: "理解推荐模型的缩放定律"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Meta]
year: 2022
venue: arXiv
arxiv: 2208.08489
tags: [scaling-laws, dlrm, meta, recommendation]
category: recommendation
---

## 问题背景

大型语言模型（LLM）中的缩放定律已在 NLP 领域得到充分验证，但推荐系统中模型规模、数据量与性能之间的幂律关系尚未被系统研究。

## 方法详述

首次对 DLRM 风格的 CTR 模型进行系统缩放律研究：

1. **模型缩放维度**：考察 Embedding 维度、MLP 层深度与宽度、交叉网络层数
2. **数据缩放维度**：样本量、特征数、序列长度对模型性能的影响
3. **计算缩放**：FLOPs 与模型性能之间的幂律 + 常数关系建模
4. **跨域迁移**：在不同推荐场景（Feed、短视频、广告）间验证缩放律的普适性

## 主要创新点

1. 首个推荐系统缩放律系统研究
2. 揭示 DLRM 的幂律 + 常数行为模式
3. 建立了模型规模-计算量-性能的三维缩放关系图谱
4. 为后续 WuKong、Kunlun 等缩放律工作奠定方法论基础

## 实验结果对比

| 缩放维度 | 幂律指数 α | 观察范围 | 饱和趋势 |
|---------|-----------|---------|---------|
| 模型参数量 | 0.12-0.18 | 10M-1B | 存在 |
| 数据量 | 0.08-0.15 | 10M-10B | 较弱 |
| 计算量 (FLOPs) | 0.10-0.20 | 联合效应 | 存在 |

## 局限性

研究局限于 DLRM 类架构，未覆盖 Transformer 类模型；幂律指数较小，推荐模型缩放收益可能弱于 LLM。
