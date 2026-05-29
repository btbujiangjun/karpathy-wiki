---
title: "MTFM: A Scalable and Alignment-Free Foundation Model for Industrial Recommendation in Meituan"
title-zh: "MTFM: 美团工业推荐中可扩展的无对齐基础模型"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Meituan]
year: 2026
venue: arXiv
arxiv: 2602.11235
tags: [foundation-model, alignment-free, cpu-gpu-pipeline, triton, meituan]
category: ctr
---

## 问题背景

推荐基础模型在扩展到多场景时面临对齐（Alignment）挑战——不同业务场景的数据分布差异导致联合训练困难。

## 方法详述

提出 MTFM 无对齐基础模型方案：

1. **Full Attn / Target Attn 交替**：无需显式的场景对齐，通过注意力模式的交替变换隐式适应不同场景
2. **CPU-GPU 流水线**：特征预处理在 CPU 端异步完成，GPU 专注前向计算
3. **定制 Triton Kernel**：将 PyTorch 操作替换为自定义 Triton kernel
4. **无对齐训练**：所有场景共享模型参数，无需特定场景适配层
5. **全国部署**：美团全量场景验证

## 主要创新点

1. 无对齐的基础模型训练范式
2. CPU-GPU 异步流水线优化
3. PyTorch → Triton 的工业级 kernel 迁移

## 实验结果对比

| 策略 | 跨场景 AUC | 训练吞吐 | 推理吞吐 | 工程复杂度 |
|------|-----------|---------|---------|-----------|
| 独立模型 | 基准 | 1.0× | 1.0× | 高 |
| 对齐联合训练 | +0.2% | 0.8× | 0.9× | 高 |
| MTFM | +0.4% | 1.5× | 1.3× | 低 |

## 局限性

无对齐方法在场景差异极大时可能失效；Triton kernel 需要硬件特定优化。
