---
title: "OpenGame: Open Agentic Coding for Games"
type: paper
created: 2026-05-24
updated: 2026-05-24
authors: [multi-institutional]
year: 2026
arxiv: 2604.18394
category: games
tags: [game-creation, agentic-coding, code-generation, rl]
---

## Problem

End-to-end web game creation remains difficult for LLMs due to the complexity of game logic, visual design, and debugging across multiple iterations.

## Method

Open-source agentic framework with two core components:

- **Game Skill**: Template + Debug skill with a living protocol of verified fixes
- **GameCoder-27B**: Domain-specialized code model via 3-stage pipeline (Continue Pretraining → SFT → execution-grounded RL)

Evaluation via OpenGame-Bench: Build Health, Visual Usability, Intent Alignment using headless browser + VLM judge.

## Key Results

- SOTA on 150 diverse game prompts
- GameCoder-27B produces playable games with high intent alignment

## Key Innovations

- First open-source agentic framework for end-to-end game creation
- Execution-grounded RL for code generation
- Living protocol of verified fixes (Debug Skill)

## Links

- arXiv: [2604.18394](https://arxiv.org/abs/2604.18394)
