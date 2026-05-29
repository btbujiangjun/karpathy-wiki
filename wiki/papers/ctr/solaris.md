---
title: "SOLARIS: Speculative Offloading for Serving Large Recommendation Foundation Models"
title-zh: "SOLARIS: 面向大规模推荐基础模型服务的投机卸载"
type: paper
created: 2026-05-29
updated: 2026-05-29
authors: [Meta]
year: 2026
venue: arXiv
arxiv: 2604.12110
tags: [serving, offloading, infrastructure, meta]
category: ctr
---

## 问题背景

推荐基础模型参数规模持续增长，GPU 显存难以容纳完整模型，传统模型并行推理引入高延迟。

## 方法详述

提出投机卸载（Speculative Offloading）推理框架：

1. **投机执行**：利用推荐请求的重复模式，预判所需模型部分并提前加载
2. **分层卸载策略**：高频参数驻留 GPU，低频参数卸载至 CPU 内存/SSD
3. **缓存感知调度**：根据缓存命中率动态路由请求
4. **异步预取**：基于历史访问模式预取可能需要的参数

## 主要创新点

1. 首次将投机执行概念用于推荐模型服务
2. 分层卸载突破 GPU 显存限制
3. 无需修改模型架构即可部署更大规模模型

## 实验结果对比

| 策略 | 模型容量 | P99 延迟 | GPU 显存需求 |
|------|---------|---------|------------|
| 全 GPU 部署 | 200B | 15ms | 800GB |
| 模型并行 | 500B | 28ms | 400GB |
| SOLARIS | 500B | 18ms | 200GB |

## 局限性

依赖请求模式的可预测性；冷启动场景下预测准确率下降；SSD 卸载场景可能引入 I/O 瓶颈。
