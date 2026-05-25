---
title: "TubiFM"
type: entity
created: 2026-05-25
updated: 2026-05-25
type: Product
sources: [papers/tubifm-ranking.md]
tags: [recommendation, ranking, llm, streaming]
---
Unified ranking model from Tubi (Fox) using Llama 3.2 1B for item, carousel, and search ranking. Uses "user story" serialized representation unifying cross-surface history. Achieves +3.9% search TVT, +0.30% carousel TVT with p99 latency reduced from 500ms to 200ms on L40S GPUs.

## Source
[[tubifm-ranking]](papers/tubifm-ranking.md)
