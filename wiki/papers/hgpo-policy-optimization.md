---
title: "HGPO: Hierarchy-of-Groups Policy Optimization for Long-Horizon Agentic Tasks"
type: paper
created: 2026-05-24
updated: 2026-05-24
authors: [multi-institutional]
year: 2026
arxiv: 2602.22817
tags: [rl, multi-turn, policy-optimization, agents, long-horizon]
---

## Problem

Multi-turn RL suffers from context explosion — advantage estimation becomes unreliable as trajectories grow long, and computational cost scales poorly.

## Method

Context-aware hierarchical grouping with adaptive weighting advantage estimation. Groups experiences by context depth and computes advantages within each group, then aggregates with adaptive weights.

## Key Results

- Outperforms baselines on ALFWorld and WebShop
- Identical GPU memory footprint to single-turn methods
- Minimal additional time cost

## Key Innovations

- Low-bias, balanced-variance advantage estimator for multi-turn settings
- Hierarchical grouping captures advantages at different context depths
- Context-aware grouping prevents long-trajectory instability

## Links

- arXiv: [2602.22817](https://arxiv.org/abs/2602.22817)
