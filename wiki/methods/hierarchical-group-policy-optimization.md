---
title: "Hierarchy-of-Groups Policy Optimization (HGPO)"
type: method
created: 2026-05-24
updated: 2026-05-24
sources: [papers/agents/hgpo-policy-optimization.md]
tags: [rl, multi-turn, advantage-estimation, policy-optimization]
---

Addresses context explosion in multi-turn RL by grouping experiences by context depth and computing advantages within each group, then aggregating with adaptive weights. Produces low-bias, balanced-variance advantage estimates for long trajectories.

## Key Characteristics

- Context-aware hierarchical grouping of experiences
- Adaptive weighting across groups at different context depths
- Identical GPU memory to single-turn methods
- Captures advantages that emerge at different stages of a long trajectory

## Source

[[hgpo-policy-optimization]] — [[2602.22817|arXiv]]
