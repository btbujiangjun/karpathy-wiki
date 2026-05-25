---
title: "Turn-Level Critic PPO"
type: method
created: 2026-05-24
updated: 2026-05-24
sources: [papers/odysseus-vlm-games.md]
tags: [rl, ppo, critic, vlm, games]
---

Adaptation of PPO with a lightweight turn-level critic for long-horizon decision-making (100+ turns). Each turn receives a learned value estimate, providing dense reward signal that substantially improves stability over critic-free methods like GRPO and Reinforce++.

## Key Characteristics

- Turn-level (per-action) value estimation
- Lightweight critic architecture with minimal overhead
- Works with pretrained VLMs as action priors

## Source

[[odysseus-vlm-games]] — [[2605.00347|arXiv]]
