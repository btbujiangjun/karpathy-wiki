---
title: Game Difficulty Evaluation
type: concept
created: 2026-05-18
updated: 2026-05-18
sources: [evaluating-game-difficulty-in-tetris-block-puzzle.pdf]
tags: [game-difficulty, evaluation, ai]
---

# Game Difficulty Evaluation

The practice of using strong AI agents to quantitatively assess the difficulty of game rule variants.

## Approach

Following the "assessment via a strong agent" paradigm:
- Train a strong AI (e.g., AlphaZero variant) on each rule variant
- Measure difficulty via objective metrics (training reward, convergence speed)
- Higher reward + faster convergence → easier game

## Common Metrics

- **Training Rewards**: Average rewards toward end of training
- **Convergence Iterations**: Iterations to reach maximum performance
- **Draw rates** / **Expected scores** (used in chess variant analysis)

## Relation to DDA

Dynamic Difficulty Adjustment (DDA) adapts AI strength online to match player skill. Difficulty evaluation is the analysis/measurement side, distinct from real-time adjustment.

## Sources Using This Paradigm

- [Evaluating Game Difficulty in Tetris Block Puzzle (2026)](../papers/evaluating-game-difficulty-in-tetris-block-puzzle.md) — uses SGAZ on Tetris Block Puzzle variants
- Tomašev et al. (2020) — uses AlphaZero to analyze chess rule variants

## Related Wiki Pages

- [SGAZ](../methods/sgaz.md)
- [Tetris Block Puzzle](../datasets/tetris-block-puzzle.md)
