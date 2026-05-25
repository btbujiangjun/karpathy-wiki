---
title: "Lifelong Learning in Dark Souls III"
title-zh: "黑暗之魂 III 中的终身学习"
type: paper
created: 2026-05-24
updated: 2026-05-24
authors: [multi-institutional]
year: 2026
arxiv: 2601.17923
venue: ICLR '26 Lifelong Agent Workshop
category: games
tags: [lifelong-learning, games, skill-graph, hierarchical-rl, dark-souls]
---

## Problem

Real-time combat in complex games requires reusable skills that can adapt under domain shift without catastrophic forgetting.

## Method

Models combat control as a directed skill graph with 5 reusable skills trained via hierarchical curriculum. Selective post-training under domain shift: upstream skills (camera, lock-on, movement) remain reusable; downstream skills (dodge, heal-attack) adapt.

## Key Results

- Upstream skills are phase-invariant and transferable across different game states
- Selective fine-tuning succeeds under limited interaction budget
- Demonstration on Dark Souls III real-time combat

## Key Innovations

- Real-time combat modeled as structured skill graph
- Selective fine-tuning distinguishes transferable vs. adaptable skills
- Upstream/downstream skill decomposition for lifelong learning

## Links

- arXiv: [2601.17923](https://arxiv.org/abs/2601.17923)
