---
title: Evaluating Game Difficulty in Tetris Block Puzzle
type: paper
created: 2026-05-18
updated: 2026-05-18
sources: [evaluating-game-difficulty-in-tetris-block-puzzle.pdf]
tags: [tetris, game-difficulty, sgaz, alpha-zero]
---

# Evaluating Game Difficulty in Tetris Block Puzzle

- **Authors**: Chun-Jui Wang, Jian-Ting Guo, Hung Guei, Chung-Chin Shih, Ti-Rong Wu, I-Chen Wu
- **Year**: 2026
- **Venue**: arXiv:2603.18994v2
- **Tags**: `#tetris` `#game-difficulty` `#sgaz`

## Problem

There is little principled assessment of which rule sets in Tetris Block Puzzle variants are more difficult, despite the game's popularity (tens of millions of downloads).

## Method

Uses **Stochastic Gumbel AlphaZero (SGAZ)**, a budget-aware planning agent for stochastic environments, as a strong evaluator. Modifies game rules across three dimensions:
1. Holding blocks (h)
2. Preview holding blocks (p)
3. Additional Tetris block variants (U, V, X, T-pentomino)

## Metrics

- **Training Rewards**: Average total rewards over the last 50 iterations
- **Convergence Iterations**: Iterations required to consistently reach max reward over 3 consecutive iterations

## Results

| Variant | Effect |
|---------|--------|
| Larger h | Lower difficulty, higher reward, faster convergence |
| Larger p | Lower difficulty, weaker effect than h |
| Additional blocks | Higher difficulty, especially T-pentomino |
| h=1, any p alone | Agent unable to converge without preview blocks |

## Limitations

- Uses a fixed simulation budget; human player perception not evaluated
- Only tested on a specific set of pentomino blocks
- Max reward cap of 6750 may limit measurement at the high end

## Related Wiki Pages

- [Source Summary](../sources/evaluating-game-difficulty-in-tetris-block-puzzle.md)
- [SGAZ](../methods/sgaz.md)
- [Game Difficulty Evaluation](../concepts/game-difficulty-evaluation.md)
- [Tetris Block Puzzle](../datasets/tetris-block-puzzle.md)
