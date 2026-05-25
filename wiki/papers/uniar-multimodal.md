---
title: "Unified Multimodal Autoregressive Modeling with Shared Context — Visual Tokenizer Is Key to Unification"
title-zh: "基于共享上下文的统一多模态自回归建模"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Wujian Peng, Lingchen Meng, Yuxuan Cai, Xianwei Zhuang, Yuhuan Yang, Rongyao Fang, Chenfei Wu, Junyang Lin, Zuxuan Wu, Shuai Bai]
year: 2026
venue: ICML 2026
tags: [multimodal, autoregressive, visual-tokenizer, unification]
category: generative-models
---

## 问题背景

现有统一多模态模型依赖不相干的视觉分词器，分裂了表示空间，阻碍了真正的统一建模。不同模态使用不同的 tokenizer 和表示空间，导致模型无法跨模态共享语义信息。

## 方法详述

提出 UniAR 框架，使用离散视觉分词器作为关键桥接：

1. **共享上下文**：所有模态（文本、图像、视频）在统一的 token 空间中建模
2. **视觉分词器为核心**：模型能够直接理解自身生成的视觉 token，无需额外重新编码
3. **统一的预训练范式**：在共享上下文中同时训练视觉理解和生成

## 主要创新点

1. 共享上下文的多模态autoregressive框架
2. 统一了视觉理解和生成的 token 空间
3. 实现真正的end-to-end多模态统一建模

## 实验结果对比

| 任务 | 现有统一模型 | UniAR |
|------|------------|-------|
| 图像生成 FID | 基线 | -20% |
| 视觉理解（VQA） | 基线 | +5.3% |
| 跨模态检索 | 基线 | +8.1% |

## 局限性

对高分辨率图像处理的 token 效率需改进；训练计算成本较高。
