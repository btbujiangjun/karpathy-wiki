---
title: "TokenMixer-Large: Scaling Up Large Ranking Models in Industrial Recommenders"
title-zh: "TokenMixer-Large: 工业推荐中大规模排序模型的硬件利用率优化扩展"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [ByteDance]
year: 2026
venue: arXiv
arxiv: 2602.06563
tags: [hardware-efficiency, scaling, tokenmixer, bytedance]
category: ctr
---

## 问题背景

RankMixer 在扩展至大规模时遭遇 GPU 硬件利用率不足问题——计算密集型操作的内存带宽瓶颈限制了实际吞吐。

## 方法详述

提出 TokenMixer-Large 硬件感知扩展方案：

1. **硬件利用率分析**：系统分析 RankMixer 在不同 GPU 上的计算/内存行为
2. **计算-存储重新平衡**：调整 MLP 扩展比和 TokenMixer 维度以匹配硬件特性
3. **Triton 自定义 Kernel**：为混合操作编写专用 Triton kernel
4. **渐进式扩展策略**：从 1B 到 10B 参数的分阶段部署方案
5. **工业部署优化**：量化 + 蒸馏 + 稀疏化的联合压缩

## 主要创新点

1. 硬件利用率视角的缩放优化（而非单纯增加参数量）
2. 首次在推荐系统领域提出硬件感知架构调整
3. 自定义 Triton kernel 的实际工业应用

## 实验结果对比

| 配置 | 参数量 | GPU 利用率 | 吞吐 (samples/s) | AUC |
|------|-------|-----------|-----------------|-----|
| RankMixer 2×直接放大 | 1B | 35% | 0.5× | 0.8050 |
| TokenMixer-Large | 1B | 78% | 1.2× | 0.8075 |
| TokenMixer-Large 4× | 4B | 72% | 0.8× | 0.8110 |

## 局限性

硬件感知设计需要针对特定 GPU 型号调优；Triton kernel 的可移植性需维护。
