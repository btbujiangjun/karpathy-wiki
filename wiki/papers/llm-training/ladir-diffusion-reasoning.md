---
title: "LaDiR: Latent Diffusion Enhances LLMs for Text Reasoning"
title-zh: "LaDiR: 潜扩散增强 LLM 文本推理"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: []
year: 2026
venue: ICLR 2026
arxiv: 2510.04573
tags: [diffusion, reasoning, latent-diffusion, llm-reasoning]
category: llm-training
---

## 问题背景

autoregressive LLM 在推理时缺乏迭代改进机制，易陷入局部最优。标准autoregressive解码从左到右逐 token 生成，没有机会回退和修正早期错误。这种"一条路走到黑"的推理方式限制了 LLM 在复杂推理任务上的表现。

## 方法详述

使用 VAE 将推理步骤编码为潜思考 token，利用潜扩散模型在latent space中迭代去噪：

1. **latent space推理编码**：通过 VAE 将文本推理步骤映射到连续latent space
2. **潜扩散去噪**：在latent space中应用扩散模型进行迭代优化
3. **多样性引导机制**：通过latent space的随机采样探索多推理路径

## 主要创新点

1. latent space扩散推理替代autoregressive解码
2. 多样性引导机制探索多推理路径
3. 迭代改进能力（非单遍生成）

## 实验结果对比

| 任务 | autoregressive LLM | LaDiR |
|------|-----------|-------|
| Countdown | 基线 | +30% |
| GSM8K | 基线 | +8% |
| 推理多样性 | 低 | 高 |

## 局限性

VAE+扩散的推理延迟高于纯autoregressive方法；latent space的可解释性有限。
