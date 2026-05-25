---
title: "Persona Conditioned Shared Policy (PCSP)"
type: method
created: 2026-05-25
updated: 2026-05-25
sources: [papers/games/pcsp-npc-shared-rl.md]
tags: [games, rl, npc, persona, shared-policy]
---
Single RL policy conditioned on frozen LLM embeddings of persona descriptions. Uses PPO + InfoNCE consistency loss + KL diversity regularization. Enables compositional zero-shot persona identification 17× above chance with 22× faster inference than LLM-as-policy baselines.

## Source
[[pcsp-npc-shared-rl]] — [[2605.23652|arXiv]]
