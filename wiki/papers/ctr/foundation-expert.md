---
title: "Realizing Scaling Laws in Recommender Systems: A Foundation-Expert Paradigm for Hyperscale Model Deployment"
title-zh: "推荐系统中缩放定律的实现：面向超大规模部署的基础模型-专家范式"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Meta]
year: 2025
venue: arXiv
arxiv: 2508.02929
tags: [foundation-model, moe, deployment, hyperscale, meta]
category: ctr
---

## 问题背景

推荐系统缩放面临核心矛盾：单个统一模型难以适配所有业务场景（Feed、视频、Marketplace 等），而每个场景独立训练又代价高昂。

## 方法详述

提出 Foundation-Expert 范式及 HyperCast 部署基础设施：

1. **Foundation 模型**：在全部数据上预训练大容量基础模型，捕获通用知识
2. **场景专家（Surface Expert）**：每个业务场景保有轻量级专家模块，在 Foundation 输出上微调
3. **HyperCast 服务架构**：Foundation 模型与 Expert 之间的高效通信与路由机制
4. **动态路由**：请求级别选择/组合多个专家
5. **知识蒸馏**：Foundation → Expert 的知识传递流程

## 主要创新点

1. 首个大规模 Foundation-Expert 部署范式
2. HyperCast 基础设施实现高效的推理训练分离
3. 解决了单一模型 vs 多场景部署的核心矛盾
4. Meta 全量部署验证

## 实验结果对比

| 策略 | 单场景 AUC | 跨场景 AUC | 总计算成本 |
|------|-----------|-----------|-----------|
| 独立训练 | 基准 | - | 10× |
| 全共享模型 | -0.5% | - | 1× |
| Foundation-Expert | +0.3% | +0.6% | 1.2× |

## 局限性

依赖高质量的场景划分；专家数量增加时路由决策优化复杂；团队需要模型并行推理基础设施。
