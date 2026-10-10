---
title: Conference & arXiv Digest — 2026-10-10
type: synthesis
created: 2026-10-10
updated: 2026-10-10
sources: []
tags: [conference-digest, ICML2026, ICLR2026, NeurIPS2025, AAAI2026, CVPR2026, ACL2026, EMNLP2025, SIGIR2026, WWW2026, CIKM2025, RecSys2025, recommendation, advertising, CTR, LLM, reasoning, RLVR, agents, world-models, video-generation, generative-models, benchmarks, sequential-modeling, games, code-execution, daily-digest]
---

# Conference & arXiv Digest (2026-10-10)

> Focus: Top ML/AI conferences and recent arXiv papers from Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, Netflix, NVIDIA, Anthropic, Apple, Amazon, and top labs. Coverage: AI, LLMs, recommendation systems, advertising, CTR, games, code execution prediction, agent systems, generative models, sequential modeling, and benchmarks.

## 1. Conference Highlights (Recent Proceedings)

### 1.1 ICML 2026
- Notable focus areas: reasoning RL, large-scale model training efficiency, recommendation systems, diffusion models, and agentic workflows
- Key trends: test-time scaling, length-aware RL, and calibration for recommender systems

### 1.2 NeurIPS 2025
- Test-Time Reinforcement Learning (TTRL): Self-evolution on unlabeled test data via majority voting rewards
- Co-evolving coder and unit tester agents via RL for autonomous verification
- Flatness vs Neural Collapse analysis, implicit reasoning in Transformers

### 1.3 ICLR 2026
- DeCS: Decoupled rewards and curriculum for reducing overthinking in reasoning models (>50% token reduction while preserving performance)
- RAIN-Merging: Gradient-free merging preserving thinking format while enhancing instruction-following
- Half-order fine-tuning for diffusion models (Recursive Likelihood Ratio optimizer)

### 1.4 AAAI 2026
- Multi-agent RL for LLM collaboration
- AutoTool: Efficient tool selection for LLM agents
- GUI grounding, think-speak-decide architectures for social welfare

### 1.5 CVPR 2026
- Molmo2: Open-data video VLM with strong counting performance
- VS-Bench: Strategic VLM evaluation for next-action prediction
- CubiD: 768-dim discrete diffusion with strong gFID scores
- Motus: Latent-action world models for robotic VLA

### 1.6 ACL/EMNLP 2025-2026
- CoT faithfulness via unlearning, reward modeling for MT evaluation
- Multi-clip safety evaluation for MLLMs
- SAT-based verification for RLVR rewards

### 1.7 RecSys/CIKM/KDD 2025-2026 (Rec/Ads/CTR)
- Hi-SAM (KDD'26 ADS): +6.55% online gain
- DAS (CIKM'25): Dual-aligned SIDs for recommendation
- AgenticGen (TikTok Ads): Reward-guided ad-video generation with CTR/AdvV gains
- HSTU-style architectures, one-stage recommender systems, exposure calibration

## 2. Industry Labs - Recent Focus
- **Google DeepMind/Google**: Reasoning, agentic systems, world models, multimodality
- **OpenAI**: Reasoning models, tool use, agentic workflows, safety
- **Anthropic**: Claude with thinking, red-teaming, agent safety benchmarks
- **Meta AI**: LLaMA family, multimodal, recsys at scale, open science
- **Microsoft Research**: Agent systems, reasoning, alignment, infrastructure
- **ByteDance (Seed)**: Large models, video generation, recommendation, search
- **Alibaba (Tongyi)**: Qwen family, multimodal, agents, recsys/ads
- **Tencent**: Hunyuan, recommender systems, advertising
- **Kuaishou**: Short-video recsys (OneRec lineage), multimodality
- **Baidu (ERNIE)**: ERNIE models, agents, industry applications
- **NVIDIA**: Agentic systems (MintAct), world models, acceleration
- **Apple**: On-device models, privacy-preserving learning
- **Amazon**: Alexa/agents, recsys, advertising
- **Netflix**: RecSys, personalization at scale

## 3. Synthesis
The recent wave (late 2025 through 2026) shows convergence on: (1) test-time adaptation/self-evolution (TTRL, reasoning bootstrapping), (2) co-evolving systems (coder-tester, reward-model+verifier), (3) token/compute efficiency in reasoning (DeCS), (4) world models + VLA unification, (5) industrial consolidation around SID-based representations and reward loops in ads/recs, and (6) increasing emphasis on measurable safety/agent benchmarks.
