---
title: "DiLaDiff: Distilled Latent-Augmented Diffusion for Language Modeling"
title-zh: "DiLaDiff：面向语言建模的蒸馏潜空间增强扩散模型"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Jean-Marie Lemercier, Tomas Geffner, Karsten Kreis, Morteza Mardani, Arash Vahdat, Ante Jukić]
year: 2026
arxiv: 2605.23605
affiliation: NVIDIA
tags: [diffusion, language-modeling, consistency-distillation]
category: llm-training
---

## 问题背景

扩散语言模型（Diffusion Language Models, DLMs）通过逐步去噪生成文本，是一种autoregressive模型以外的文本生成范式。但扩散 LM 面临两个问题：(1) 连续的latent space表示与离散 token 之间存在语义错位；(2) 推理时多步去噪速度慢于autoregressive的单步解码。NVIDIA 提出的 DiLaDiff 同时解决这两个问题。

## 方法详述

DiLaDiff 由三个组件构成：

**1. 连续latent space（Continuous Latent Space）**
使用一个经过掩码扩散 LM 编码器将离散 token 映射到连续latent space。这个latent space保留了语义结构，同时允许连续空间中的平滑插值和操作。

**2. 潜扩散先验（Latent Diffusion Prior）**
在latent space上训练一个扩散先验模型，学习从纯噪声到有意义的潜表示的映射。与直接在 token 空间扩散不同，latent space扩散利用了语义化的连续表征。

**3. 一致性蒸馏（Consistency Distillation）**
训练一个一致性模型（Consistency Model），将多步去噪蒸馏为单步或少步生成。生成时只需 1-2 步即可完成高质量文本生成。

## 主要创新点

- **latent space + 扩散的双层架构**：首次将潜扩散模型（Stable Diffusion 的思想）应用于语言建模
- **解决 token 相关问题**：latent space扩散天然解决了离散 token 生成中的相关性丢失问题
- **一致性蒸馏加速**：将多步去噪压缩为 1-2 步，推理速度接近autoregressive模型

## 实验结果与对比

| 方法 | 类型 | PPL ↓ (OpenWebText) | 推理步数 | 生成速度 |
|------|------|-------------------|---------|---------|
| GPT-2 (autoregressive) | AR | 35.7 | 1 | 基准 |
| Diffusion-LM | Discrete DLM | 42.1 | 1000+ | 极慢 |
| Plaid (连续 DLM) | Continuous DLM | 38.2 | 100+ | 慢 |
| DiLaDiff (无蒸馏) | Continuous DLM | **36.8** | 100+ | 慢 |
| DiLaDiff (蒸馏, 1步) | Continuous DLM | **37.5** | **1** | 接近 AR |
| DiLaDiff (蒸馏, 2步) | Continuous DLM | **37.1** | **2** | 接近 AR |

**核心结论：** DiLaDiff 在 PPL 指标上优于所有现有扩散 LM（包括离散和连续），一致性蒸馏版本仅用 1-2 步即可达到接近autoregressive的推理速度。latent space扩散确实比直接在 token 空间扩散更有效（解决了 token 相关性问题）。

## 局限性

- PPL 仍然高于同规模autoregressive模型（约 5-10%），生成质量差距需要进一步缩小
- latent space编码器需要额外的训练阶段，整体训练流程更复杂
- 论文仅验证了中小规模（~1B），在更大规模上的扩展性未知
