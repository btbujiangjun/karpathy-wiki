---
title: "Towards Generalizable and Efficient Large-Scale Generative Recommenders"
title-zh: "面向可泛化且高效的大规模生成式推荐系统——Netflix 实践经验"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Qiuling Xu, Ko-Jen Hsiao, Moumita Bhattacharya]
year: 2026
arxiv: 2605.23312
affiliation: Netflix
tags: [generative-recommendation, scaling, llm]
category: recommendation
---

## 问题背景

生成式推荐（Generative Recommendation）将推荐建模为序列生成任务：给定用户行为序列，直接生成推荐 item ID。相比于传统的检索-排序两阶段方法，生成式推荐更简洁且能end-to-end优化。但 Netflix 在将生成式推荐器从 2M 参数扩展到 1B 参数的过程中发现：简单扩大模型规模并不总是有效，不同任务对模型容量的需求差异极大。

## 方法详述

Netflix 对生成式推荐器的 scaling 进行了系统实验，关键组件包括：

**1. 多 token 预测**
在训练时让模型同时预测序列中接下来的多个 item，而非逐个预测。一方面与推理时的重排延迟对齐，另一方面提供更强的学习信号。

**2. 采样式 softmax（Sampled Softmax）**
由于候选集极大（数百万 item），标准的 softmax 计算不可行。使用采样式 softmax 在训练时只采样一部分负样本计算梯度，大幅降低计算成本。

**3. 投影式解码头（Projected Decoding Head）**
将 item ID 映射到低维隐空间后再解码，减少输出层参数量。

**4. 偏移Scaling Law（Offset Scaling Law）**
提出新的 scaling 诊断方法：对不同的推荐任务分别拟合偏移Scaling Law，通过偏移量判断该任务是否还有容量提升空间。

## 主要创新点

- **偏移Scaling Law作为诊断工具**：首次提出用 scaling-law 偏移量判断任务是否有 headroom（容量空间），避免盲目扩大模型
- **多 token 预测对齐推理**：训练时预测多个 token 以匹配推理时的一次生成多个推荐，消除训练-推理不一致
- **工业级 scaling 经验**：2M→1B 参数的系统性扩展，覆盖训练、部署、shadow eval 全流程

## 实验结果与对比

| 推荐任务 | 2M 模型 MRR | 1B 模型 MRR | 提升幅度 | 偏移缩放诊断 |
|---------|------------|------------|---------|------------|
| 主页推荐 | 0.452 | **0.498** | +10.2% | 有 headroom |
| 相关推荐 | 0.387 | **0.412** | +6.5% | 有 headroom |
| 搜索推荐 | 0.523 | **0.531** | +1.5% | 接近饱和 |
| 个性化榜单 | 0.335 | **0.352** | +5.1% | 有 headroom |

**核心结论：**
- 1B 模型在所有任务上均优于 2M 模型，但提升幅度与任务相关（1.5%~10.2%）
- 偏移Scaling Law准确预测了搜索推荐任务的 headroom 有限（只有 +1.5%），避免在此任务上继续浪费算力
- 多 token 预测在 shadow eval 中表现最佳，且与推理阶段直接对齐
- 采样式 softmax 是训练大规模生成式推荐器的关键使能技术

## 局限性

- 1B 模型的训练和推理成本显著高于 2M 模型，部署可行性需要结合业务指标综合评估
- 偏移Scaling Law目前是经验观察，缺乏严格的数学推导
- 生成式推荐器在冷启动和长尾 item 上的表现未详细分析
