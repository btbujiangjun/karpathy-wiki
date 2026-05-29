---
title: "GPSD: Scaling Transformers for Discriminative Recommendation via Generative Pretraining"
title-zh: "GPSD: 通过生成式预训练扩展判别式推荐的Transformer"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Alibaba]
year: 2025
venue: KDD 2025
arxiv: 2506.03699
tags: [generative-pretraining, discriminative, ctr, cvr, alibaba]
category: ctr
---

## 问题背景

推荐系统传统上使用判别式模型（CTR/CVR 预测），但大型生成式模型的缩放经验表明，生成式预训练可提升下游判别任务的性能。

## 方法详述

提出生成式预训练 → 判别式下游微调的 GPSD 范式：

1. **生成式预训练**：在用户行为序列上做 next-item prediction 预训练
2. **判别式微调**：预训练权重初始化 CTR/CVR 模型，全量或部分微调
3. **桥接架构**：生成式 head 与判别式 head 的共享底层设计
4. **缩放实验**：预训练数据量、模型容量与下游 AUC 的缩放关系
5. **桥接两种范式**：生成式与判别式范式的统一

## 主要创新点

1. 首个在工业推荐中验证生成式预训练→判别式下游的有效性
2. 生成式与判别式范式的桥梁
3. 预训练-微调的缩放律

## 实验结果对比

| 策略 | CTR AUC | CVR AUC | 预训练成本 | 微调成本 |
|------|--------|--------|-----------|---------|
| 直接训练 (无预训练) | 0.8050 | 0.7820 | - | 1.0× |
| GPSD-100B | 0.8100 | 0.7885 | 2.0× | 0.8× |
| GPSD-1T | 0.8135 | 0.7920 | 5.0× | 0.8× |

## 局限性

预训练-微调间的分布漂移（pretrain-finetune gap）需要额外对齐；预训练的计算成本较高。
