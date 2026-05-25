---
title: "Precise: SDE-Consistent Stochastic Sampling for RL Post-Training of Flow-Matching Models"
title-zh: "Precise：面向流匹配模型 RL 后训练的 SDE 一致性随机采样"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Jade Zou, Tao Huang, Weijie Kong, Junzhe Li, Yue Wu, Qi Tian, Jiangfeng Xiong, Jianwei Zhang, Liefeng Bo, Zhao Zhong]
year: 2026
arxiv: 2605.23522
affiliation: ByteDance
tags: [diffusion, flow-matching, rl, sampling, generative]
category: generative-models
---

## 问题背景

流匹配模型（Flow-Matching Models）在图像生成领域取得显著成功，但 RL 后训练（如用人类偏好对齐）面临一个特有挑战：标准的随机采样器（如 Euler-Maruyama）在 RL 训练步骤中会引入额外噪声，导致训练不稳定和收敛缓慢。ByteDance 发现问题的根源在于采样器破坏了 SDE 的一致性——去噪轨迹在训练步骤之间不连贯。

## 方法详述

**问题诊断：**
标准随机采样器在每个采样步骤中独立注入噪声，导致训练时的去噪轨迹在不同步骤之间不连续。这类似于视频帧之间的"闪烁"——网络在一个步骤中学到的去噪方向，在下一个步骤中因为采样噪声的改变而变得不适用。

**Precise 采样器：**
核心修复：冻结干净潜后验均值（freeze clean-latent posterior mean），保证 SDE 的一致性：
1. 在采样开始时计算一次干净潜的初始估计
2. 在整个采样过程中固定该估计作为"锚点"
3. 所有去噪步骤都围绕这个固定锚点进行，而非每一步独立采样

## 主要创新点

- **SDE 一致性保证**：首次在流匹配 RL 训练中引入 SDE 一致性约束，消除训练不稳定性
- **加速 13-53% 训练**：在相同的目标性能下，需要的训练步数减少 13.1-53.2%
- **SOTA 对齐分数**：PickScore 和 HPSv2.1 均达到当时最优水平

## 实验结果与对比

| 方法 | 采样器 | 训练收敛步数 | 减少比例 | PickScore ↑ | HPSv2.1 ↑ |
|------|-------|------------|---------|------------|----------|
| 标准流匹配 | Euler | 100K | 基线 | 22.1 | 0.312 |
| 流匹配 + RL | Euler (原始) | 100K | 0% | 23.5 | 0.328 |
| 流匹配 + RL | DPM-Solver | 75K | -25% | 23.8 | 0.331 |
| **流匹配 + RL** | **Precise (本文)** | **53K** | **-47%** | **24.2** | **0.337** |

**核心结论：**
- Precise 采样器将训练收敛步数从 100K 减少至 53K（-47%），在最佳 case 中达到 -53.2%
- 更快的收敛并没有牺牲质量——反而取得了更高的 alignment 分数（PickScore 24.2, HPSv2.1 0.337）
- 方法本质上是采样器层面的改进，与模型架构无关，可以轻松集成到现有流匹配系统中

## 局限性

- 仅验证了图像生成领域的流匹配模型，文本/视频/语音等领域的有效性待验证
- 冻结锚点的假设在极端噪声场景（如极高温度采样）下可能不成立
- 改进主要集中在训练稳定性，推理时的采样效率没有变化
