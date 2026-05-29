---
title: "Make It Long, Keep It Fast: End-to-End 10K-Sequence Modeling at Billion Scale on Douyin"
title-zh: "让其变长，保持快速：抖音上十亿级端到端万级序列建模"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [ByteDance]
year: 2025
venue: arXiv
arxiv: 2511.06077
tags: [long-sequence, efficiency, douyin, end-to-end, bytedance]
category: ctr
---

## 问题背景

端到端万级用户行为序列建模虽然在 AUC 上优于两阶段检索，但高昂的计算成本限制了其工业落地。

## 方法详述

提出面向十亿级部署的端到端万级序列模型：

1. **计算优化**：Flash Attention + 稀疏化 + 并行化联合优化
2. **模型结构简化**：去除冗余层，仅保留核心序列建模单元
3. **高效 Serving**：请求级 batching 与 KV 缓存复用
4. **蒸馏策略**：万级教师 → 定长学生蒸馏
5. **抖音全量部署**：每日处理数十亿请求

## 主要创新点

1. 首个工业级端到端万级序列部署
2. 完整的高效 Serving 方案
3. 长序列蒸馏方法

## 实验结果对比

| 指标 | 基线 Transformer-1K | 端到端 10K | 蒸馏版 10K→1K |
|------|-------------------|-----------|--------------|
| AUC | 0.8060 | 0.8095 | 0.8080 |
| 推理延迟 | 8ms | 25ms | 9ms |
| QPS | 15K | 5K | 14K |

## 局限性

蒸馏版与完整 10K 模型仍有 AUC gap；对部署硬件要求较高。
