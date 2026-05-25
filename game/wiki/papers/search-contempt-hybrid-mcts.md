---
title: "Search-contempt: a hybrid MCTS algorithm for training AlphaZero-like engines with better computational efficiency"
type: paper
created: 2026-05-18
updated: 2026-05-18
sources: [search-contempt-a-hybrid-mcts-algorithm.pdf]
tags: [search-contempt, mcts, alpha-zero, self-play]
---

# Search-contempt: a hybrid MCTS algorithm for training AlphaZero-like engines with better computational efficiency

- **Author**: Ameya Joshi
- **Year**: 2025
- **Venue**: arXiv:2504.07757v1
- **Tags**: `#search-contempt` `#mcts` `#alpha-zero`

## Problem

AlphaZero required tens of millions of self-play games (costing millions of dollars) to master chess. Training game generation needs a balance between variety and quality — temperature τ trades one for the other.

## Method

**Search-contempt**: A hybrid asymmetric MCTS that mixes:
1. **PUCT** (at root and player-to-move nodes, even depth ds)
2. **Thompson Sampling** (at opponent nodes, odd depth ds, after Nscl visits)

After Nscl visits at an opponent node, the visit distribution is frozen, and further samples are drawn proportionally — making the search "contemptuous" of the opponent by assuming weaker play.

## Key Results

- 70 Elo stronger training game generation than PUCT (same compute, same w+l/d ratio)
- 150 Elo improvement in Queen Odds Chess
- Win rate monotonically increases with more nodes (unlike PUCT which peaks then drops)
- 20-30x more "interesting" tactical positions per game
- No negative impact on game repetition rate

## Training Efficiency

Proposes a training schedule starting with N=1000, Nscl=5, gradually increasing both as the network improves. Estimated ~200K games for competitive strength (vs 44M for AlphaZero).

## Limitations

- Only tested on chess; transferability to other games (go, shogi) not demonstrated
- Requires asymmetric search trees (cannot share between players), doubling tree-building cost per move
- The 200K game training estimate is extrapolative, not experimentally verified for full training from zero

## Related Wiki Pages

- [Source Summary](../sources/search-contempt-a-hybrid-mcts-algorithm.md)
- [Search-contempt (Method)](../methods/search-contempt.md)
