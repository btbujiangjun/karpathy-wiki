---
title: Tetris Block Puzzle
type: dataset
created: 2026-05-18
updated: 2026-05-18
sources: [evaluating-game-difficulty-in-tetris-block-puzzle.pdf]
tags: [tetris, puzzle-game, stochastic]
---

# Tetris Block Puzzle

A single-player stochastic puzzle game where the player arranges blocks on an 8×8 grid to complete lines.

## Game Description

- **Grid**: 8×8
- **Blocks**: Tetromino blocks (I, O, T, S, Z, J, L)
- **Rules**: Holding blocks (h) are candidates to choose from each turn. Preview holding blocks (p) are upcoming replacements.
- **Scoring**: 1 point per line cleared. Max reward cap: 6750

## Rule Variants

| Parameter | Range | Effect |
|-----------|-------|--------|
| Holding blocks (h) | 1–3+ | More = easier |
| Preview holding blocks (p) | 0–6+ | More = slightly easier |
| Additional block types | U/V/X/T-pentomino | Added = harder; T-pentomino hardest |

## Classic Configuration

h = 3, p = 0, no additional blocks.

## Used In

- [Evaluating Game Difficulty in Tetris Block Puzzle](../papers/evaluating-game-difficulty-in-tetris-block-puzzle.md) — uses SGAZ to evaluate difficulty under variant rules

## Related Wiki Pages

- [Game Difficulty Evaluation](../concepts/game-difficulty-evaluation.md)
- [SGAZ](../methods/sgaz.md)
