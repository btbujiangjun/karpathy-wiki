---
title: "arXiv Daily Report — 2026-07-04"
type: synthesis
created: 2026-07-04
updated: 2026-07-04
tags: [arxiv, ai, llm, ctr, recommendation, rl, games, sequential-modeling]
sources: []
---

# arXiv Daily Report — 2026-07-04

Curated recent papers across AI, LLMs, recommendation, CTR prediction, sequential modeling, reinforcement learning, games, and advertising.

---

## 1. Large Language Models & Reasoning

### 1.1 DRIFTLENS: Measuring Memory-Induced Reasoning Drift in Personalized Language Models
- **Authors**: Xi Fang, Weijie Xu, Yingqiang Ge, Yuhui Xu, Stephanie Eckman, Chandan K. Reddy
- **Institution**: — (first author Xi Fang)
- **Date**: Jul 2, 2026
- **Abstract**: Personalization changes what a model says to a user; this paper shows it can also change the reasoning trajectory used to justify the response. Introduces DRIFTLENS, a ground-truth-free framework that maps reasoning steps to value categories and measures divergence between no-memory and memory-injected trajectories. User-attribute memory induces medium-to-large reasoning drift across 4 LLMs and 10 attribute categories, even when final answers remain fluent. Evaluates GRPO/DPO post-training for drift reduction.
- **Key Innovations**: Ground-truth-free drift measurement framework; systematic analysis of how user memory alters reasoning paths; first evaluation of alignment methods for mitigating reasoning drift.
- **Link**: https://arxiv.org/abs/2607.02374

### 1.2 A Hippocampus for Linear Attention: An Exact Memory for What the Recurrent State Forgets (HOLA)
- **Authors**: Wanyun Cui
- **Institution**: —
- **Date**: Jul 2, 2026
- **Abstract**: Linear-attention and state-space models compress prefix into a fixed-size recurrent state, losing exact memory. HOLA adds a hippocampal complement: a bounded exact KV cache alongside the delta-rule state. At 340M params trained on 15B tokens, lowers Wikitext perplexity from 27.32 to 22.92 (below full-attention Transformer++ at 26.88). Achieves best linear in-context retrieval and robust needle recall out to 32k tokens (16x training length).
- **Key Innovations**: Complementary Learning Systems inspired hybrid (compressive + exact cache); decoupled RMSNorm-gamma cache read for sharp retrieval; write policy based on prediction residual without learned eviction.
- **Link**: https://arxiv.org/abs/2607.02303

### 1.3 Does Reasoning Preserve Alignment? On the Trustworthiness of Large Reasoning Models
- **Authors**: Prajakta Kini, Avinash Reddy, Souradip Chakraborty, Satya Sai Srinath Namburi GNVV, Furong Huang, Amrit Singh Bedi, Alvaro Velasquez
- **Institution**: —
- **Date**: Jun 9, 2026
- **Abstract**: Studies whether converting instruction-tuned LLMs into reasoning models preserves alignment. Compares reasoning models via SFT, RL-based post-training, and distillation across 6 trustworthiness dimensions: safety, toxicity, stereotyping, machine ethics, privacy, OOD robustness. Reasoning models improve benchmarks but exhibit alignment regressions — increased toxicity, amplified stereotyping, miscalibrated refusal, privacy leakage.
- **Key Innovations**: First systematic audit of alignment preservation in reasoning model conversion; identifies behavioral drift measured by KL divergence; argues trustworthiness metrics must accompany reasoning gains.
- **Link**: https://arxiv.org/abs/2606.11046

### 1.4 Reasoning Structure of Large Language Models
- **Authors**: Frédéric Berdoz, Luca A. Lanzendörfer, Fabian Farestam, Roger Wattenhofer
- **Institution**: ETH Zurich (Wattenhofer group)
- **Date**: Jun 2, 2026
- **Abstract**: Introduces a scalable LRM benchmark of logic puzzles and a pipeline converting unstructured traces into verifiable reasoning graphs of claims and dependencies. Defines a reasoning efficiency metric quantifying how concentrated the model's logical flow is. Analysis shows structural measurements separate behaviors that token count and accuracy conflate.
- **Key Innovations**: Reasoning graphs as structured objects; efficiency metric for logical flow concentration; accepted at ICML 2026.
- **Link**: https://arxiv.org/abs/2606.03883

### 1.5 Constructive Alignment: Governing Preference Dynamics in Human-AI Interaction
- **Authors**: Max Kanwal, Caryn Tran
- **Institution**: — (AAAI-26 Workshop on Machine Ethics)
- **Date**: Apr 1, 2026
- **Abstract**: Reframes alignment as a control problem over evolving human preference trajectories rather than static preference satisfaction. Draws on behavioral economics, psychology, and constructivist social theory. Models preferences as layered state variables that evolve under AI interaction. Proposes a control-theoretic framework for governing long-term value formation.
- **Key Innovations**: Paradigm shift from static to dynamic preference alignment; control-theoretic formalization of preference evolution; interdisciplinary synthesis.
- **Link**: https://arxiv.org/abs/2607.00001

### 1.6 Understanding Large Language Models
- **Authors**: Yannik Keller, Thomas Eisenmann
- **Institution**: —
- **Date**: Jul 1, 2026
- **Abstract**: A chapter-length survey discussing emerging capabilities and mechanistic implementation of LLMs. Covers Transformer architecture, emergent capabilities (symbolic reasoning, theory of mind, deception), explainability approaches (neuron activation to circuit tracing), and debates on genuine understanding vs. pattern memorization.
- **Key Innovations**: Balanced treatment of anthropomorphism arguments; accessible synthesis of current LLM cognition debates.
- **Link**: https://arxiv.org/abs/2607.01006

---

## 2. Generative Recommendation & CTR Prediction

### 2.1 Implicit Reasoning for LLM-based Generative Recommendation (PauseRec)
- **Authors**: Yinhan He, Liam Collins, Bhuvesh Kumar, Jundong Li, Neil Shah, Donald Loveland
- **Institution**: —
- **Date**: Jun 12, 2026
- **Abstract**: Decomposes explicit reasoning training pipelines for LLM-based generative recommendation, revealing three limitations: weakened world-knowledge verbalization, SID/embedding misalignment, and rationale quality sensitivity. Proposes PauseRec, a lightweight implicit reasoning paradigm. Outperforms explicit CoT by up to 6.22%, reduces training cost by up to 65% GPU hours, speeds inference by up to 71.3%.
- **Key Innovations**: First systematic decomposition of explicit reasoning for generative recommendation; implicit reasoning avoids costly trace acquisition and alignment training; strong practical efficiency gains.
- **Link**: https://arxiv.org/abs/2606.14142

### 2.2 Dual-Stream MLP is All You Need for CTR Prediction (DS-MLP)
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution**: Renmin University of China (RUCAIBox)
- **Date**: Jun 3, 2026
- **Abstract**: Proposes dual-stream MLP framework leveraging knowledge distillation to consolidate explicit feature interaction learning into a main MLP, with a parallel MLP capturing implicit interactions. State-of-the-art across 3 benchmarks using only vanilla MLP structure.
- **Key Innovations**: Teacher-agnostic distillation from complex CTR models into pure MLP; dual alignment strategies for dual-stream compatibility; SOTA with minimal architecture.
- **Link**: https://arxiv.org/abs/2606.04944

### 2.3 Field Matters: A Lightweight LLM-enhanced Method for CTR Prediction (LLaCTR)
- **Authors**: Yu Cui, Feng Liu, Jiawei Chen, Xingyu Lou, Changwang Zhang, Jun Wang, Yuegang Sun, Xiaohu Yang, Can Wang
- **Institution**: Zhejiang University; (WWW '26)
- **Date**: Apr 2026 (WWW '26)
- **Abstract**: Identifies limitations of existing LLM-based CTR methods. Advocates for field-level (not instance-level) semantic knowledge from LLMs. Uses self-supervised fine-tuning to distill field knowledge for improving both feature representation and interaction. 10-100x lower computational overhead vs. other LLM-enhanced methods.
- **Key Innovations**: Field-level enhancement paradigm shift; self-supervised LLM distillation for CTR; extreme efficiency vs. prior LLM4CTR approaches.
- **Link**: https://arxiv.org/abs/2505.14057

### 2.4 IDProxy: Cold-Start CTR Prediction for Ads and Recommendation
- **Authors**: —
- **Institution**: —
- **Date**: Jun 23, 2026
- **Abstract**: Addresses cold-start CTR prediction where new items have no interaction history. Proxy-based approach using item features to bridge cold-start gap.
- **Key Innovations**: Proxy mechanism for cold-start items in CTR.
- **Link**: https://arxiv.org/abs/2603.01590

---

## 3. Reinforcement Learning & Games

### 3.1 IRumAI: Reinforcement Learning for Indian Rummy
- **Authors**: —
- **Institution**: —
- **Date**: Jun 20, 2026
- **Abstract**: First RL agent for Indian Rummy (hidden-information card game). Integrates PPO, meld-aware observation encoding, deadwood-driven reward shaping, and dual-branch convolutional architecture. Trained solely against weak heuristics after BC warm-start. Achieves 53.9% win rate vs. strongest search-based opponent. 0.33ms per action (7000x faster than search).
- **Key Innovations**: First RL treatment of Indian Rummy; meld-aware encoding for combinatorial card games; linear probing reveals network implicitly models opponent's hidden hand.
- **Link**: https://arxiv.org/abs/2606.21975

### 3.2 Causal Reinforcement Learning for Complex Card Games: A Magic The Gathering Benchmark (MTG-Causal-RL)
- **Authors**: Cristiano da Costa Cunha et al.
- **Institution**: —
- **Date**: May 7, 2026
- **Abstract**: Introduces MTG-Causal-RL benchmark coupling strategic partially-observed domain with explicit causal interface and statistical protocol. Masked PPO and CGFA-PPO reach competitive win rates. Provides causal credit assignment, structural transfer, and SCM-grounded policy auditability.
- **Key Innovations**: Causal RL meets complex card games; SCM interface for policy audit; benchmark for causal-RL, world-model, and LLM-agent research.
- **Link**: https://arxiv.org/abs/2605.06066

### 3.3 SlimDT: Beyond Autoregressive RTG in Decision Transformer
- **Authors**: Yongyi Wang, Hanyu Liu, Lingfeng Li, et al.
- **Institution**: —
- **Date**: May 7, 2026
- **Abstract**: Removes Return-to-Go from autoregressive sequence in Decision Transformer. Injects RTG information into state representations before sequential modeling. Reduces sequence length by 1/3, improving inference efficiency. Surpasses standard DT across D4RL tasks.
- **Key Innovations**: Decoupling sparse conditioning signal from information-rich sequence; 33% shorter sequences; competitive with SOTA offline RL methods.
- **Link**: https://arxiv.org/abs/2605.06104

### 3.4 MARLIN: Multi-Agent Game-Theoretic RL for Sustainable LLM Inference
- **Authors**: H. Moore, S. Qi, D. Milojicic, C. Bash, S. Pasricha
- **Institution**: —
- **Date**: May 13, 2026
- **Abstract**: Multi-agent game-theoretic RL framework for sustainable LLM inference serving in cloud datacenters. Co-optimizes time-to-first-token, carbon emissions, water usage, and energy costs. Achieves 18%+ TTFT reduction, 33% carbon reduction, 43% water reduction, 11% energy cost reduction vs. SOTA.
- **Key Innovations**: MARL for sustainability in LLM inference; joint optimization of latency + environmental metrics.
- **Link**: https://arxiv.org/abs/2605.13496

### 3.5 CART: Conservative Adversarially Robust Decision Transformer
- **Authors**: Xiaohang Tang, Zhuowen Cheng, Satyabrat Kumar
- **Institution**: — (NeurIPS 2025 Workshop)
- **Date**: Oct 13, 2025
- **Abstract**: First framework to enhance adversarial robustness of Decision Transformer in stochastic games. Formulates protagonist-adversary interaction as stage games with NashQ value conditioning. Produces less exploitable policies with conservative transition handling.
- **Key Innovations**: NashQ conditioning for sequence-modeling RL; adversarial robustness for Decision Transformer; stage-game formulation for stochastic transitions.
- **Link**: https://arxiv.org/abs/2510.11877

---

## 4. Sequential Modeling & State Space Models

### 4.1 SS4Rec: Continuous-Time Sequential Recommendation with State Space Models
- **Authors**: —
- **Institution**: —
- **Date**: 2025
- **Abstract**: Formulates sequential recommendation as a continuous time-varying system. Uses hybrid state space models (Mamba-based) to capture both temporal dynamics and sequential information. Handles irregular time intervals in user interaction sequences.
- **Key Innovations**: Continuous-time SSM perspective for recommendation; time-aware + relation-aware SSM blocks.
- **Link**: https://arxiv.org/abs/2502.08132

---

## 5. Multi-Agent Systems & Game Theory

### 5.1 GARL: Game-Theoretic Reinforcement Learning for Multi-Agent Strategic Prioritisation
- **Authors**: Yuxiao Ye, Yiwen Zhang, Huiyuan Xie, Yuqin Huang, Zhiyuan Liu
- **Institution**: —
- **Date**: Jun 3, 2026
- **Abstract**: Formalizes multi-agent strategic prioritisation as a two-stage game. Competing agents allocate resources over a shared set; arbiter produces final ranking. Game-theoretic utilities converted to RL signals. Enables small open-source LLMs to compete with strong closed-source LLM in legal-domain ranking.
- **Key Innovations**: Game-theoretic structure → RL reward design; two-stage game formalization for ranking; LLM-based multi-agent system.
- **Link**: https://arxiv.org/abs/2606.05002

### 5.2 Game-Theoretic MARL for Swarm Trajectory Planning in Low-Altitude Wireless Networks
- **Authors**: Nguyen Duc Minh Quang, Ruoxi Chong, Zhiqiang Wei, Chang Liu, Derrick Wing Kwan Ng
- **Institution**: —
- **Date**: Jun 15, 2026
- **Abstract**: Formulates UAV trajectory planning as cooperative stochastic congestion game with communication-and-mission-aware utility. Proposes CTDE-MAPPO algorithm maximizing social welfare under multi-cell RB congestion.
- **Key Innovations**: Stochastic congestion game formulation for multi-cell UAV planning; CTDE-MAPPO for wireless network trajectory optimization.
- **Link**: https://arxiv.org/abs/2606.16386

---

## Summary of High-Impact Themes

| Theme | Papers | Trend |
|-------|--------|-------|
| **LLM Alignment & Safety** | DRIFTLENS, Constructive Alignment, Reasoning Alignment | Growing concern about dynamic effects of personalization and reasoning model conversion |
| **Efficient LLM Architecture** | HOLA (hippocampal linear attention) | Hybrid exact + compressive memory to fix linear attention's recall |
| **Reasoning Analysis** | Reasoning Structure, Reasoning Failures survey | Moving beyond accuracy to structural reasoning quality |
| **Generative Rec / CTR** | PauseRec, DS-MLP, LLaCTR, IDProxy | Shift toward implicit reasoning, MLP distillation, and LLM-enhanced field knowledge |
| **RL for Games** | IRumAI, MTG-Causal-RL | Underserved games (Rummy, MTG) getting RL/causal RL treatment |
| **Efficient RL** | SlimDT | Removing RTG tokens from Decision Transformer |
| **MARL + Sustainability** | MARLIN, GARL, Swarm Planning | Multi-agent RL expanding to sustainability, legal, and wireless domains |
