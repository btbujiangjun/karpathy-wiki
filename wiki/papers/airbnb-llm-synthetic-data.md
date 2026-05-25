---
title: "Bridging Cold-Start Gap: LLM-Powered Synthetic Data for NL Search at Airbnb"
title-zh: "弥合冷启动鸿沟：Airbnb 中基于 LLM 的合成数据生成助力自然语言搜索"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Wendy Ran Wei, Hao Li, Weiwei Guo, Xiaowei Liu, Xueyin Chen, Dillon Davis, Malay Haldar, Soumyadip Banerjee, Kedar Bellare, Huiji Gao, Stephanie Moyerman, Sanjeev Katariya]
year: 2026
arxiv: 2605.21812
affiliation: Airbnb
tags: [cold-start, synthetic-data, llm, search, recommendation]
category: recommendation
---

## 问题背景

Airbnb 的自然语言搜索（Natural Language Search）允许用户用自然语言描述需求，如"带泳池、适合家庭聚会的海景房"。这种搜索方式用户体验好，但面临冷启动问题——新上线房源缺乏搜索日志，无法被自然语言搜索系统匹配到。传统的人工标注成本高、覆盖低，无法满足数亿房源规模的冷启动需求。

## 方法详述

提出一个基于 LLM 的合成数据生成框架，包含三个步骤：

**Step 1: 种子查询生成（Seed-Guided Query Generation）**
选取一批高质量的真实用户查询作为种子，让 LLM 基于这些种子生成语义相似但表达不同的新查询。通过对比学习构造查询-房源的对比对。

**Step 2: 合成对比对构建**
对于每个生成的查询，从房源库中采样正例（匹配的房源）和负例（不匹配的房源）。LLM 根据房源描述判断查询-房源的对齐程度，生成标注。

**Step 3: 虚拟裁判标注（Virtual Judge Labeling）**
引入一个 LLM-as-Judge 的机制，让 LLM 对生成的查询-房源对进行评分。相比简单的是/否标签，虚拟裁判可以提供细粒度的对齐分数，覆盖更广泛的匹配模式。

## 主要创新点

- **种子引导的查询生成**：基于真实用户查询引导 LLM 生成新查询，保证合成数据与真实分布一致而非天马行空
- **虚拟裁判替代人工标注**：LLM 裁判的标注质量在分布内场景接近人工，但成本低 1000×
- **工业级冷启动流水线**：已在 Airbnb 生产环境中每日运行，持续生成训练数据

## 实验结果与对比

| 方法 | KL 散度 (vs 真实用户) | 属性类型 KL | 标注成本 | 搜索 NDCG@10 |
|------|---------------------|-----------|---------|-------------|
| 人工标注 | 基准 (0.00) | 0.00 | 最高 | 0.523 |
| InPars (已有方法) | 4.95 | 3.21 | 低 | 0.487 |
| 随机 LLM 生成 | 2.13 | 1.87 | 低 | 0.505 |
| **本文方法 (种子引导)** | **0.66** | **0.04** | **低** | **0.518** |

**核心结论：**
- 种子引导方法生成的查询分布与真实用户分布极其接近（KL 散度 0.66，比 InPars 好 7.5×）
- 属性类型分布的 KL 散度仅 0.04，几乎完美恢复真实用户的意图分布
- 使用合成数据训练的搜索模型 NDCG 达到 0.518，接近真人标注的 0.523（差距仅 1%）
- 该框架已在 Airbnb 生产环境中每日运行，持续为冷启动房源生成训练数据

## 局限性

- 种子查询的质量决定了合成数据的上限——种子需要覆盖足够的意图多样性
- LLM 虚拟裁判存在已知偏见（如对特定描述风格偏好），可能引入系统性偏差
- 合成数据的长期影响（如模型是否会在合成数据上overfitting）尚未评估
