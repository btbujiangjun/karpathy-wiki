---
title: "HARNESS-LM: Three-Phase Training Recipe for Harnessing SLMs in Sponsored Search Retrieval"
title-zh: "HARNESS-LM：面向搜索广告检索的小模型蒸馏三阶段训练方案"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Vipul Gupta, Shikhar Mohan, Lakshma Kumar, Pranjal Chitale, Nikit Begwani, Amit Singh, Manik Varma]
year: 2026
arxiv: 2605.23572
affiliation: Microsoft (Bing Ads)
category: recommendation
tags: [distillation, search, retrieval, slm, advertising]
---

## 问题背景

在搜索引擎广告（Sponsored Search）场景中，检索模型需要在毫秒级内从数亿广告库中找到最相关的候选。大模型（如基于 Transformer 的密集检索器）精度高但延迟大、成本高，无法直接服务于线上流量。小模型（SLM, <600M 参数）速度快但检索精度远低于大模型。如何在保持小模型推理效率的同时恢复大模型的检索精度，是工业界面临的核心 challenge。

## 方法详述

HARNESS-LM 提出三阶段渐进式蒸馏框架：

**阶段 1: 教师模型训练**
训练一个大规模教师检索器（基于 Transformer 的双编码器架构），在 Bing Ads 的海量查询-广告点击数据上进行对比学习预训练，获得高精度的查询-广告语义匹配能力。

**阶段 2: L2 特征对齐蒸馏**
将教师模型的中间层表示和最后一层输出作为软标签，通过 L2 损失函数让学生模型（<600M）学习模仿教师的特征空间。这一阶段的损失函数为：
```
L_align = ||h_student - h_teacher||²
```
其中 h 是查询和广告的编码向量。目标是让学生模型的特征空间尽可能接近教师模型。

**阶段 3: 对比精炼（Contrastive Refinement）**
在 L2 对齐的基础上，引入对比学习损失，让学生模型在区分正例（点击的广告）和负例（未点击的广告）时进一步精炼检索边界。这一阶段使用批内负采样（in-batch negatives）和硬负采样（hard negatives）策略。

最终学生模型仅 190M 参数，部署在 Bing Ads 线上。

## 主要创新点

- **三阶段渐进蒸馏**：从教师训练 → 特征对齐 → 对比精炼，逐步缩小师生差距，避免一步蒸馏带来的精度陡降
- **L2 + 对比联合优化**：首次在搜索广告检索场景中验证 L2 特征对齐后接对比精炼优于纯 logit 蒸馏或纯对比蒸馏
- **工业级验证**：190M 模型已在 Bing Ads 线上全量部署，经过大规模 A/B 验证

## 实验结果与对比

**离线检索精度对比：**

| 方法 | 参数量 | 教师精度恢复率 | 延迟 (ms) | 吞吐量 (qps) |
|------|--------|---------------|-----------|-------------|
| 教师模型 (T5-3B) | 3B | 100% | 50 | 1,000 |
| 直接 logit 蒸馏 | 190M | 82% | 1.8 | 18,000 |
| L2 对齐蒸馏 | 190M | 91% | 1.8 | 18,000 |
| L2 + 对比精炼 (HARNESS-LM) | 190M | **98%** | **1.8** | **20,000** |

**线上 A/B 实验效果：**

| 指标 | 较基线提升 |
|------|-----------|
| Revenue (广告收入) | **+1.0%** |
| Impression (展示量) | **+0.6%** |
| Click (点击量) | **+0.4%** |

**核心结论：** 190M 模型以 27× 更低延迟、20× 更高吞吐量恢复了教师模型 98% 的检索精度，并在线上 A/B 实验中带来显著的商业指标提升（+1% 收入）。

## 局限性

- 三阶段训练流程较为复杂，需要维护教师模型和多个中间 checkpoint
- 对教师模型的质量高度敏感，若教师模型本身存在偏见或噪声，蒸馏过程会继承这些缺陷
