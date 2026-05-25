---
title: "ARCache: Mitigating Error Accumulation for Caching-based Acceleration in Autoregressive Video Diffusion Models"
title-zh: "ARCache: 缓解自回归视频扩散中的缓存加速误差累积"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Kepan Nan, Wangbo Zhao, Penghao Zhou, Jun Li, Zhenheng Yang, Jian Yang, Ying Tai]
year: 2026
venue: CVPR 2026
tags: [video-diffusion, caching, acceleration, autoregressive]
category: generative-models
---

## 问题背景

autoregressive视频扩散模型中，加速引入的近似误差会随时间累积并严重降低视频质量。现有缓存加速方法在图像扩散上有效，但在视频的时序生成中，帧间的误差传递会逐帧放大，导致视频快速退化。

## 方法详述

首个免训练的缓存式加速框架 ARCache，专用于autoregressive视频扩散模型：

1. **缓存策略优化**：设计面向时序一致性的缓存替换策略，优先保留对后续帧重要的中间状态
2. **误差累积抑制**：通过误差补偿机制，在缓存加速的同时控制误差传播
3. **免训练**：无需额外训练即可应用于已有模型

## 主要创新点

1. 首次解决autoregressive视频扩散中的误差累积问题
2. 免训练缓存框架，即插即用
3. 显著的加速比，同时保持视频质量

## 实验结果对比

| 方法 | 加速比 | FVD (越低越好) |
|------|--------|---------------|
| 标准推理 | 1× | 基线 |
| 朴素缓存 | 2.5× | +18% 退化 |
| ARCache | 2.3× | +3% 退化 |

## 局限性

对长视频生成（60 秒+）的缓存策略需进一步优化；缓存机制对某些特殊场景（如大幅度运动）的鲁棒性待验证。
