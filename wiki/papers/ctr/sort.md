---
title: "SORT: A Systematically Optimized Ranking Transformer for Industrial-Scale Recommenders"
title-zh: "SORT: 面向工业级推荐系统的系统优化排序Transformer"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Alibaba]
year: 2026
venue: arXiv
arxiv: 2603.03988
tags: [system-optimization, ranking, transformer, alibaba]
category: ctr
---

## 问题背景

Transformer 在排序模型中面临高特征异构性带来的挑战：不同特征域的维度、稀疏度、分布差异巨大，导致注意力计算不稳定。

## 方法详述

提出 SORT 系统优化框架：

1. **系统化特征处理**：标准化流程处理异构特征——归一化、缩放、门控
2. **特征感知注意力**：根据特征域特性自适应调整注意力计算
3. **分层优化管线**：从特征工程→模型架构→推理优化的全链路系统优化
4. **稳定性机制**：LayerNorm、Residual 连接、梯度裁剪的系统化配置
5. **工业部署**：阿里搜索推荐全场景

## 主要创新点

1. 系统化而非模块化的优化方法论
2. 特征感知注意力
3. 全链路系统优化视角

## 实验结果对比

| 优化阶段 | AUC | 训练稳定性 | 推理延迟 |
|---------|-----|-----------|---------|
| 基线 Transformer | 0.8080 | 不稳定 | 1.0× |
| + 特征标准化 | 0.8100 | 稳定 | 1.0× |
| + 特征感知注意 | 0.8125 | 稳定 | 1.1× |
| + 推理优化 (SORT) | 0.8125 | 稳定 | 0.8× |

## 局限性

系统化方案依赖领域经验；特征感知模块增加了模型复杂度。
