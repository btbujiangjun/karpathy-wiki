---
title: "SDE-Consistent Sampling for Flow-Matching RL (Precise)"
type: method
created: 2026-05-25
updated: 2026-05-25
sources: [papers/precise-sde-sampling.md]
tags: [diffusion, flow-matching, rl, sampling, generative]
---
A new stochastic sampler for RL post-training of flow-matching models. Freezes clean-latent posterior mean to maintain SDE consistency during RL training, resolving excess noise issues in standard samplers. Reduces wall-clock training time by 13-53% while achieving SOTA alignment scores.

## Source
[[precise-sde-sampling]] — [[2605.23522|arXiv]]
