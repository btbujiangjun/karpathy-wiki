---
title: "HARNESS-LM"
type: entity
created: 2026-05-25
updated: 2026-05-25
type: Framework
sources: [papers/harness-lm-bing-ads.md]
tags: [distillation, search, retrieval, advertising]
---
Three-phase training framework from Microsoft Bing Ads for distilling large teacher retrievers into sub-600M student models. Uses L2 alignment + contrastive refinement. Achieves 98% teacher precision with 27× lower latency, 20× higher throughput. 190M parameter model deployed in production with +1% Revenue A/B uplift.

## Source
[[harness-lm-bing-ads]](papers/harness-lm-bing-ads.md)
