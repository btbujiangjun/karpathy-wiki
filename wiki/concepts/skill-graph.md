---
title: "Skill Graph"
type: concept
created: 2026-05-24
updated: 2026-05-24
sources: [papers/games/dark-souls-iii-lifelong.md]
tags: [lifelong-learning, hierarchical-rl, skill-transfer, games]
---

A directed graph representation of skills for real-time combat and control tasks. Upstream skills (camera, lock-on, movement) are phase-invariant and transferable across contexts; downstream skills (dodge, heal-attack) adapt under domain shift. Selective fine-tuning preserves upstream skills while adapting downstream ones.

## Key Claims

- Skill decomposition into upstream (transferable) and downstream (adaptable) components
- Hierarchical curriculum enables training of reusable skills
- Selective post-training succeeds under limited interaction budget

## Source

[[dark-souls-iii-lifelong]](papers/games/dark-souls-iii-lifelong.md)
