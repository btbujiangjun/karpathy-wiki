---
title: "SparseCTR: Unleashing the Potential of Sparse Attention on Long-Term Behaviors for CTR Prediction"
title-zh: "SparseCTR: 释放稀疏注意力在CTR预测中长期行为建模的潜力"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Meituan]
year: 2026
venue: WWW 2026
arxiv: 2601.17836
tags: [sparse-attention, long-sequence, scaling, meituan]
category: ctr
---

## 问题背景

长期用户行为序列对 CTR 预测至关重要，但标准注意力 O(n²) 的计算复杂度使其难以扩展到长序列。

## 方法详述

提出 SparseCTR 三分支稀疏注意力框架：

1. **三分支稀疏注意力**：前向（近期行为）+ 后向（长期趋势）+ 目标（目标相关性）的稀疏注意力
2. **稀疏模式学习**：可学习的稀疏注意力模式，每 token 仅关注 top-k 相关行为
3. **缩放律验证**：在 3 个数量级的 FLOPs 范围内验证缩放律
4. **动态稀疏调度**：根据序列长度自适应调整稀疏度
5. **美团全量部署**：在十亿级请求场景中验证

## 主要创新点

1. 三分支稀疏注意力架构
2. 3 个数量级 FLOPs 范围的缩放律验证
3. 工业级稀疏注意力的端到端实现

## 实验结果对比

| 模型 | FLOPs | AUC | 线上 CTR | 序列长度 |
|------|-------|-----|---------|---------|
| 密集注意力 | 1.0× | 0.8090 | - | 500 |
| SparseCTR-1K | 0.3× | 0.8105 | +1.5% | 1024 |
| SparseCTR-10K | 0.7× | 0.8130 | +3.0% | 10240 |

## 局限性

稀疏模式可能丢失跨时间段的间接关联；动态稀疏调度增加推理复杂度。
