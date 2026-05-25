---
title: Search-contempt MCTS
type: method
created: 2026-05-18
updated: 2026-05-18
sources: [search-contempt-a-hybrid-mcts-algorithm.pdf]
tags: [search-contempt, mcts, thompson-sampling, puct, alpha-zero]
---

# Search-contempt MCTS

A hybrid asymmetric MCTS algorithm that uses PUCT at player nodes and switches to Thompson Sampling at opponent nodes after Nscl visits, making the search "contemptuous" of the opponent.

## Motivation

PUCT-based MCTS assumes optimal opponent play, producing high-quality but low-variety training games (mostly draws). AlphaZero compensated by using high temperature τ for exploration, which weakens play. Search-contempt provides a better lever (Nscl) for controlling the win-draw-loss distribution without sacrificing play strength.

## Algorithm

**Parameters**:
- `Nscl`: Integer threshold for switching from PUCT to Thompson Sampling at opponent nodes
- `ds`: Depth from root (even = player nodes, odd = opponent nodes)

**Selection policy**:

At each MCTS visit, for state s and action a:

- If `ds` is even (player node) OR total visits ≤ Nscl: **PUCT** — deterministic selection of max(Q + U)
- If `ds` is odd (opponent node) AND total visits > Nscl: **Thompson Sampling** — sample proportional to frozen visit distribution Nscl(s,a) / Nscl

## Properties

- **Asymmetric**: Player and opponent use different search strategies
- **Nscl → ∞**: Degrades to standard PUCT-based MCTS
- **Self-adversarial**: Actively seeks positions where the neural network misevaluates, functioning as a more efficient policy/value improvement operator
- **Monotonic scaling**: Unlike PUCT, performance continues improving with more nodes (no peak-and-degrade in Odds Chess)

## Comparison with PUCT

| Aspect | PUCT-based MCTS | Search-contempt |
|--------|----------------|-----------------|
| Opponent assumption | Optimal play | Contemptuous (weaker) |
| w-d-l control lever | Temperature τ | Nscl |
| Training game quality | Lower at same w+l/d ratio | +70 Elo at same ratio |
| Odds Chess scaling | Peaks then degrades | Monotonically improves |
| Tree sharing | Shared between players | Separate (cleared each move) |
| Compute at same nodes | Baseline | Same total nodes, slightly more overhead |

## Related Wiki Pages

- [Search-contempt: a hybrid MCTS algorithm (Paper)](../papers/search-contempt-hybrid-mcts.md)
- [Source Summary](../sources/search-contempt-a-hybrid-mcts-algorithm.md)
