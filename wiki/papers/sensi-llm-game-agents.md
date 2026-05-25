---
title: "Sensi: Structured Test-Time Learning for LLM Game Agents"
type: paper
created: 2026-05-24
updated: 2026-05-24
authors: [multi-institutional]
year: 2026
arxiv: 2603.17683
tags: [llm, game-agents, test-time-learning, arc-agi, curriculum]
---

## Problem

LLM agents solving abstract reasoning tasks (ARC-AGI-3) require excessive environment interactions, with state-of-the-art systems needing 1600–3000 attempts per level.

## Method

Two-player architecture separating perception and action into distinct modules. Curriculum learning managed by state machine. Database-as-control-plane: agent's cognitive state stored and managed via SQLite tables. LLM-as-judge with dynamically generated evaluation rubrics.

## Key Results

- 50–94× greater sample efficiency than comparable systems (~32 vs 1600–3000 attempts)
- Honest negative result reporting: v2 solves 0 levels but at extreme efficiency

## Key Innovations

- Database-as-control-plane for cognitive state management
- LLM-as-judge with dynamic evaluation rubric generation
- Two-player architecture separating perception from action

## Links

- arXiv: [2603.17683](https://arxiv.org/abs/2603.17683)
