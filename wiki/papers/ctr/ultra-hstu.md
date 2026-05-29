---
title: "ULTRA-HSTU: Bending the Scaling Law Curve in Large-Scale Recommendation Systems"
title-zh: "ULTRA-HSTU: 在大规模推荐系统中弯曲缩放定律曲线"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Meta]
year: 2026
venue: arXiv
arxiv: 2602.16986
tags: [sparse-attention, flash-attention, scaling, hstu, meta]
category: ctr
---

## 问题背景

HSTU 架构已达到万亿参数量级，但标准密集注意力机制的 O(n²) 计算瓶颈使进一步缩放面临收益递减。

## 方法详述

提出 ULTRA-HSTU 突破 HSTU 缩放曲线：

1. **稀疏注意力**：引入可学习稀疏模式替代 HSTU 的全局注意，将每 token 关注范围从 O(n) 减至 O(log n)
2. **FlashAttention-V3 适配**：专门优化 HSTU 架构在 FlashAttention-V3 上的执行
3. **缩放曲线弯曲**：通过稀疏化+硬件优化，在相同 FLOPs 下获得更高的 AUC 收益
4. **端到端系统优化**：GPU kernel 融合与显存管理

## 主要创新点

1. 首次展示"弯曲"推荐缩放曲线（在相同计算预算下获得更高性能）
2. 稀疏注意力与 FlashAttention-V3 的联合设计
3. 为 HSTU 家族开辟新的缩放维度

## 实验结果对比

| 架构 | 参数量 | FLOPs/样本 | AUC | 推理延迟 |
|------|-------|-----------|-----|---------|
| HSTU Base | 500M | 1.0× | 0.8120 | 1.0× |
| HSTU Large | 2B | 4.0× | 0.8175 | 3.8× |
| ULTRA-HSTU Base | 500M | 1.2× | 0.8145 | 1.1× |
| ULTRA-HSTU Large | 2B | 2.2× | 0.8198 | 2.0× |

## 局限性

稀疏注意力的模式可能无法泛化到所有推荐场景；FlashAttention-V3 依赖特定 GPU 架构。
