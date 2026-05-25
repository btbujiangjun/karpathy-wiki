---
title: Overview
type: overview
created: 2026-05-18
updated: 2026-05-18
sources: [evaluating-game-difficulty-in-tetris-block-puzzle.pdf]
tags: []

---

# 游戏研究 — Overview

> This page is the top-level synthesis of the entire knowledge base.
> It will be revised as sources are ingested and understanding deepens.

## Scope

a research topic about 游戏研究. Currently focused on AI-driven game analysis using AlphaZero-family methods, including game difficulty evaluation and computationally efficient self-play training.

## Current State

Two sources ingested:

1. **"Evaluating Game Difficulty in Tetris Block Puzzle"** (2026) — Uses Stochastic Gumbel AlphaZero (SGAZ) to assess rule variant difficulty in Tetris Block Puzzle. Key finding: holding block count has the strongest difficulty-reducing effect; T-pentomino has the strongest difficulty-increasing effect.

2. **"Search-contempt: a hybrid MCTS algorithm..."** (2025) — Introduces search-contempt MCTS (PUCT + Thompson Sampling) that improves training data quality by 70 Elo and enables training with ~200K games instead of 44M. Key insight: asymmetric search with frozen opponent visit distributions trains networks more efficiently.

## Key Themes

- **AI as game difficulty evaluator**: Using AlphaZero variants to objectively measure rule complexity
- **Stochastic Gumbel AlphaZero (SGAZ)**: Efficient training in stochastic puzzle games
- **Search-contempt MCTS**: Hybrid asymmetric search that trades optimal opponent assumption for more informative training positions
- **Computational efficiency**: Reducing self-play training cost from millions of dollars to consumer hardware

## Open Questions

- How do Tetris difficulty metrics correlate with human player perception?
- Can search-contempt generalize beyond chess to other games (go, shogi, stochastic puzzles)?
- Can search-contempt be combined with SGAZ for stochastic environments?
