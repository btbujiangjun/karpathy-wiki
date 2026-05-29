---
title: "OnePiece: Bringing Context Engineering and Reasoning to Industrial Cascade Ranking System"
title-zh: "OnePiece: 将上下文工程与推理引入工业级级联排序系统"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Shopee]
year: 2025
venue: arXiv
arxiv: 2509.18091
tags: [context-engineering, reasoning, cascade-ranking, shopee]
category: ctr
---

## 问题背景

工业级联排序系统（Cascade Ranking）中，粗排到精排的信息传递存在上下文丢失，且缺乏显式的推理机制。

## 方法详述

提出 OnePiece 上下文工程与推理框架：

1. **LLM 风格上下文工程**：将推荐请求组织为类似 LLM 的上下文格式（prompt-like）
2. **分块潜推理（Block-wise Latent Reasoning）**：在级联各阶段之间嵌入潜推理块
3. **跨阶段信息传递**：保留和传递推理中间结果
4. **级联联合优化**：粗排-精排-重排的端到端优化
5. **Shopee 电商场景验证**

## 主要创新点

1. 推荐系统中首次引入 LLM 风格的上下文工程
2. 分块潜推理增强级联决策
3. 跨阶段信息传递机制

## 实验结果对比

| 模型 | 粗排 AUC | 精排 AUC | 整体 CTR | 推理延迟 |
|------|---------|---------|---------|---------|
| 标准级联 | 0.7500 | 0.8000 | 基准 | 1.0× |
| OnePiece | 0.7580 | 0.8080 | +2.8% | 1.2× |

## 局限性

上下文工程的 prompt 设计需要大量实验；潜推理块的计算开销随级联阶段数线性增长。
