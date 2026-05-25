---
title: "LLM Retrieval for Stable and Predictable Ad Recommendations"
title-zh: "面向稳定可预测广告推荐的 LLM 检索方法"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Vinodh Kumar Sunkara, Satheeshkumar Karuppusamy, Hangjun Xu, Sai Deepika Regani, Kshitij Gupta, Gaby Nahum, Sneha Iyer, Jean-Baptiste Fiot, Yinglong Guo, Xiaowen Guo, Atul Jangra, Yucheng Liu, Jinghao Yan, Vijay Pappu, Benjamin Schulte, Deepak Chandra]
year: 2026
arxiv: 2605.21969
affiliation: LinkedIn (Microsoft)
venue: SIGIR 2026 AgentSearch Workshop
tags: [advertising, llm, retrieval, stability]
category: recommendation
---

## 问题背景

在线广告推荐系统的稳定性和可预测性对广告主至关重要。广告主希望他们的广告在特定用户画像下能够稳定展示，而非有时出现有时消失。但传统广告检索系统通常只优化相关性，导致广告展示的波动性大。LinkedIn 定义并解决了广告推荐中的"稳定性"问题——如何在保证相关性的前提下，让相同用户画像在短期内看到的广告集合尽可能一致。

## 方法详述

提出一个统一评估框架，包含三个关键组件：

**1. 稳定性-预测性评估框架**
形式化定义了广告推荐的稳定性和可预测性指标：
- 稳定性（Stability）：同一用户在不同时间段的请求中，top-K 广告集合的 Jaccard 相似度
- 预测性（Predictability）：给定用户特征，top-K 广告集合的条件熵

**2. LLM 语义候选生成**
使用微调后的 LLM 从广告库中生成语义相关的候选广告集合，替代传统基于词法匹配或简单 embedding 相似度的方法。LLM 能理解复杂的用户意图（如"适合家庭聚会的餐厅推荐"）并匹配对应的广告。

**3. 图扩展（Graph-Based Expansion）**
在 LLM 生成的候选基础上，通过广告-广告之间的知识图谱进行扩展（如同类产品广告、互补品类广告），确保候选覆盖的全面性和展示的一致性。

## 主要创新点

- **首次形式化定义广告推荐的稳定性**：为评估广告推荐系统提供了一个新维度（稳定性），补充了传统的精度-召回率指标
- **LLM + 图扩展的组合方法**：LLM 保证语义相关性，图扩展保证展示一致性
- **大规模工业验证**：在 LinkedIn 广告系统的真实流量上验证了框架的有效性

## 实验结果与对比

| 方法 | 相关性 (NDCG@10) | 稳定性 (Jaccard@10) | 预测性 (CondEntropy↓) |
|------|-----------------|-------------------|---------------------|
| 传统检索 (BM25) | 0.682 | 0.31 | 5.2 |
| 双编码器 Embedding | **0.723** | 0.35 | 4.8 |
| LLM 候选生成 | 0.718 | 0.42 | 4.1 |
| LLM + 图扩展 (本文) | 0.715 | **0.53** | **3.6** |

**核心结论：**
- LLM 语义生成的候选质量与传统 Embedding 方法相当，但在稳定性上显著更优
- 添加图扩展后，稳定性从 0.42 提升至 0.53（+26%），相关性仅下降 0.3%（可忽略）
- 预测性指标从 5.2 改善至 3.6，意味着广告展示的可预测性提高了 30%
- LinkedIn 已在生产环境中部署该框架，用于保障广告主投放体验的一致性

## 局限性

- 稳定性和相关性存在 trade-off，图扩展在提升稳定性的同时会略微降低相关性（0.7%）
- LLM 候选生成增加了推理复杂度，需要额外的延迟和成本考量
- 稳定性定义基于短期（同一天），长期稳定性的需求可能不同
