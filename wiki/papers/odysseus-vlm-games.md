---
title: "Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games"
type: paper
created: 2026-05-24
updated: 2026-05-24
authors: [multi-institutional]
year: 2026
arxiv: 2605.00347
tags: [vlm, games, rl, ppo, mario, decision-making]
---

## Problem

Vision-language models (VLMs) struggle with long-horizon decision-making in game environments requiring 100+ consecutive turns.

## Method

Adapted PPO with a lightweight turn-level critic for RL-based training of VLMs. Pretrained VLMs provide strong action priors for sample efficiency.

## Key Results

- At least 3× average game progress over frontier models
- Substantially outperforms GRPO and Reinforce++
- Emergent in-game and cross-game generalization without losing general-domain capabilities

## Key Innovations

- Turn-level critic substantially improves stability over critic-free methods
- Pretrained VLMs provide strong action priors, improving sample efficiency
- Lightweight critic architecture adds minimal overhead

## Links

- arXiv: [2605.00347](https://arxiv.org/abs/2605.00347)
