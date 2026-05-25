---
title: Search-contempt: a hybrid MCTS algorithm for training AlphaZero-like engines with better computational efficiency
type: source-summary
created: 2026-05-18
updated: 2026-05-18
sources: [search-contempt-a-hybrid-mcts-algorithm.pdf]
tags: [search-contempt, mcts, alpha-zero, self-play, computational-efficiency, chess]
---

# Search-contempt: a hybrid MCTS algorithm for training AlphaZero-like engines with better computational efficiency

**Author**: Ameya Joshi
**Year**: 2025 (arXiv:2504.07757v1)
**Tags**: `#search-contempt` `#mcts` `#alpha-zero` `#self-play` `#computational-efficiency`

## Abstract

Introduces search-contempt, a hybrid MCTS algorithm (PUCT + Thompson Sampling) that alters self-play position distribution to prefer challenging positions. Shows significant gains in Odds Chess and enables computationally efficient training (hundreds of thousands of games instead of millions).

## Key Claims

| Claim | Evidence | Confidence |
|-------|----------|------------|
| Search-contempt outperforms PUCT-based MCTS by 70 Elo in training game quality | Match: search-contempt (Nscl=5, τ1) vs PUCT (τ2), same w+l/d ratio | High |
| Search-contempt gains 150 Elo in Odds Chess over PUCT | Win rate comparison across node counts (100, 800, 20000) | High |
| Training games can be reduced from 44M (AlphaZero) to ~200K | Extrapolation from Odds Chess specialized networks | Tentative |
| Search-contempt produces 20-30x more "interesting" positions | Qualitative analysis of self-play game content | Single-source |
| Lower Nscl does not increase game repetition rate | Fraction of repeated games plot (Figure 4) | High |

## Data

- **Nscl parameter**: Controls transition from PUCT → Thompson Sampling at opponent nodes
  - Nscl = ∞ → equivalent to PUCT
  - Nscl = 5 → optimal w+l/d ≈ 1 for training games
- **Queen Odds Chess win rates**:

| Nodes | PUCT | Search-contempt |
|-------|------|----------------|
| 100   | 23.43% | 36.76% |
| 800   | 35.25% | 57.81% |
| 20000 | 25.40% | 81.73% |

- **Training match** (1000 nodes/move):
  - PUCT (τ2): 17 wins, 46 draws, 37 losses
  - Search-contempt (Nscl=5, τ1): 37 wins, 46 draws, 17 losses → +70 Elo

## Quotes

> "Search-contempt can be used to improve play wherever the opponent has inaccuracies in its play and does not have access to perfect policy and value evaluation functions."

> "Search-contempt actively seeks out complicated positions which are evaluated incorrectly at lower values of total nodes searched but which are more accurately evaluated at higher values of total nodes searched."

## Related Wiki Pages

- [Search-contempt (Method)](../methods/search-contempt.md)
- [Search-contempt: a hybrid MCTS algorithm (Paper)](../papers/search-contempt-hybrid-mcts.md)
