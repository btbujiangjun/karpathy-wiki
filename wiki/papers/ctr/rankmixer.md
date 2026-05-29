---
title: "RankMixer: Scaling Up Ranking Models in Industrial Recommenders"
title-zh: "RankMixer: 工业推荐系统中排序模型的规模化扩展"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [ByteDance]
year: 2025
venue: CIKM 2025
arxiv: 2507.15551
tags: [tokenmixer, scaling, ranking, bytedance]
category: ctr
---

## 问题背景

工业推荐排序模型在规模扩展时面临训练和推理成本的双重压力，传统 DLRM 架构的计算-性能瓶颈难以突破。

## 方法详述

提出基于 TokenMixer 的排序模型缩放架构：

1. **TokenMixer 核心**：用混合操作（Mixer）替代传统注意力作为特征交互主干
2. **分层混合**：Field 级和 Bit 级的双层混合机制
3. **计算效率优化**：线性复杂度的特征交互
4. **工业部署适配**：支持模型并行、量化、知识蒸馏
5. **渐进式缩放**：从百亿到千亿参数的分阶段扩展策略

## 主要创新点

1. TokenMixer 在排序场景的首次工业验证
2. 线性复杂度的特征交互突破 O(n²) 瓶颈
3. 完整的规模化部署方案

## 实验结果对比

| 模型 | AUC | 训练吞吐 | 推理延迟 | 参数量 |
|------|-----|---------|---------|-------|
| DLRM | 0.7900 | 1.0× | 1.0× | 100M |
| DCN-V2 | 0.7945 | 0.9× | 1.1× | 150M |
| RankMixer | 0.7988 | 1.2× | 0.9× | 120M |
| RankMixer-Large | 0.8020 | 0.9× | 1.2× | 500M |

## 局限性

混合操作在高稀疏场景下的表达能力弱于注意力机制；长序列建模能力有待验证。
