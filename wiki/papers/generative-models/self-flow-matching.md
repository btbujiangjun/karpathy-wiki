---
title: "Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis"
title-zh: "自监督流匹配实现可扩展多模态合成"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Hila Chefer, Patrick Esser, Dominik Lorenz, Dustin Podell, Vikash Raja, Vinh Tong, Antonio Torralba, Robin Rombach]
year: 2026
venue: ICML 2026
tags: [self-supervised, flow-matching, multi-modal, generative-models, diffusion]
category: generative-models
---

## 问题背景

多模态生成模型需要大规模配对数据训练，但获取高质量配对数据成本高昂。现有方法依赖监督学习范式，限制了数据利用效率。在图像-文本、音频-视频等跨模态场景中，配对数���的稀缺成为主要的扩展瓶颈。

## 方法详述

提出 Self-Flow，一种self-supervised流匹配范式，在生成框架内整合表征学习：

1. **self-supervised流匹配**：无需配对数据即可学习跨模态映射，通过流匹配目标实现表示与生成的统一
2. **共享latent space**：不同模态通过共享的潜表示空间进行对齐
3. **end-to-end训练**：表示学习和生成建模在同一框架中联合优化

## 主要创新点

1. 首次将self-supervised学习引入流匹配生成框架
2. 统一了表示学习和生成建模两个目标
3. 在多个多模态任务上展示可扩展性

## 实验结果对比

| 任务 | Self-Flow (无配对数据) | 监督方法 (有配对数据) |
|------|----------------------|---------------------|
| 文本→图像生成 | FID 接近 | FID SOTA |
| 图像→文本描述 | 可比 | SOTA |
| 跨模态检索 | 可比 | SOTA |

Self-Flow 在无需配对数据的情况下达到与监督方法相当的性能。

## 局限性

在大规模数据上的扩展性需进一步验证；对某些细粒度跨模态对齐任务效果有限。
