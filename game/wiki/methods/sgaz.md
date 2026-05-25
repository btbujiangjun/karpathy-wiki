---
title: Stochastic Gumbel AlphaZero (SGAZ)
type: method
created: 2026-05-18
updated: 2026-05-18
sources: [evaluating-game-difficulty-in-tetris-block-puzzle.pdf]
tags: [sgaz, alpha-zero, mcts, stochastic, gumbel]
---

# Stochastic Gumbel AlphaZero (SGAZ)

Combines Gumbel AlphaZero and Stochastic AlphaZero to improve training efficiency in stochastic environments.

## Background

- **AlphaZero**: Zero-knowledge learning using MCTS + neural network policy/value
- **Gumbel AlphaZero**: Uses Gumbel-Top-k trick and sequential halving at root; guarantees policy improvement under small simulation budgets. Uses Q-based training targets instead of visit-count distributions
- **Stochastic AlphaZero**: Introduces afterstates and learned model (afterstate dynamic function ϕ, afterstate prediction function ψ) for stochastic environments. Tree alternates between decision nodes and chance nodes
- **SGAZ**: Merges both approaches

## Key Components

1. **Gumbel-Top-k trick**: Without-replacement candidate selection on policy logits
2. **Sequential halving**: Progressively prunes weaker candidates
3. **Afterstate separation**: Separates agent action from environment randomness
4. **Learned model**: ϕ (afterstate dynamic), ψ (afterstate prediction + probabilities), g (chance outcome → next state)

## Effectiveness

SGAZ achieves near-optimal performance under small simulation budgets, making it ideal for efficient, reproducible comparisons across rule sets in stochastic puzzle games. Demonstrated effective on Tetris Block Puzzle and (in prior work) on 2048.

## Related Wiki Pages

- [Evaluating Game Difficulty in Tetris Block Puzzle (Paper)](../papers/evaluating-game-difficulty-in-tetris-block-puzzle.md)
- [Game Difficulty Evaluation](../concepts/game-difficulty-evaluation.md)
