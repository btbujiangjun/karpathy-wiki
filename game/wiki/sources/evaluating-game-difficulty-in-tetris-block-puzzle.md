---
title: Evaluating Game Difficulty in Tetris Block Puzzle
type: source-summary
created: 2026-05-18
updated: 2026-05-18
sources: [evaluating-game-difficulty-in-tetris-block-puzzle.pdf]
tags: [tetris, game-difficulty, sgaz, alpha-zero, puzzle-game]
---

# Evaluating Game Difficulty in Tetris Block Puzzle

**Authors**: Chun-Jui Wang, Jian-Ting Guo, Hung Guei, Chung-Chin Shih, Ti-Rong Wu, I-Chen Wu
**Year**: 2026 (arXiv:2603.18994v2)
**Tags**: `#tetris` `#game-difficulty` `#sgaz` `#alpha-zero`

## Abstract

Tetris Block Puzzle is a single-player stochastic puzzle. This paper uses Stochastic Gumbel AlphaZero (SGAZ) to evaluate difficulty under different rule variants: holding blocks (h), preview holding blocks (p), and additional Tetris block types.

## Key Claims

| Claim | Evidence | Confidence |
|-------|----------|------------|
| Increasing h and p reduces difficulty | Higher training reward and faster convergence iterations | High |
| Increasing h has stronger impact than increasing p | Larger reward delta and convergence speed change | High |
| Adding new block types increases difficulty | Lower training rewards vs baseline | High |
| T-pentomino causes the largest difficulty increase | Slowest convergence across all experiments | High |
| SGAZ achieves near-optimal performance under small simulation budgets | Training curves show stable convergence to max reward | High |

## Data

- **Game setup**: 8×8 grid, tetromino blocks, max reward 6750
- **Training**: SGAZ, 500 iterations, four 1080Ti GPUs
- **Metrics**: Training Rewards (avg reward over last 50 iterations), Convergence Iterations (iterations to reach max reward for 3 consecutive iterations)
- **Baseline (h=3, p=0)**: Reward 6544, convergence at iteration 61

### Key Results

**Holding Blocks (h) variation (p=0):**
| h | Reward | Convergence |
|---|--------|-------------|
| 1 | 39.0 | Did not converge |
| 2 | 4126.1 | 160 |
| 3 | 6544.0 | 61 |

**T-pentomino impact (h=2, p=0, single block added):**
- Worst convergence among all pentomino blocks
- Many two-block combinations did not converge

## Quotes

> "Increasing either the number of holding blocks or the number of preview holding blocks makes the game easier, though the former has a markedly stronger impact."

> "Adding new block types significantly makes the game harder, especially for the T-pentomino block."

## Related Wiki Pages

- [SGAZ (Stochastic Gumbel AlphaZero)](../methods/sgaz.md)
- [Game Difficulty Evaluation](../concepts/game-difficulty-evaluation.md)
- [Tetris Block Puzzle](../datasets/tetris-block-puzzle.md)
- [Evaluating Game Difficulty in Tetris Block Puzzle (Paper)](../papers/evaluating-game-difficulty-in-tetris-block-puzzle.md)
