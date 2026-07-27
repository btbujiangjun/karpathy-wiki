---
title: arXiv Daily Report — 2026-07-25
type: synthesis
created: 2026-07-25
updated: 2026-07-25
sources: []
tags: [arxiv, daily, ai, llm, recommendation, ctr, sequential-modeling, games, advertising]
---

# arXiv Daily Report — 2026-07-25

Curated selection of recent arXiv papers across AI, LLMs, recommendation systems, advertising, sequential modeling, CTR prediction, and games.

---

## LLM Reasoning & Architecture

### PoTRE: Test-Time Reasoning inspired by Cognitive Heterogeneity

- **Authors:** Anmol Kankariya et al.
- **Institution:** (Not specified in abstract)
- **Abstract:** Introduces PoTRE (Poly-Topological Reasoning Ensembles), a heterogeneous framework that decouples inference into four agents: Adversarial Refinement Agent, Hierarchical Strategic Planning Agent, Spectrum Search Agent, and Direct Chain Agent. A Task-Adaptive Aggregation Layer dynamically reconciles perspectives via candidate selection, semantic synthesis, or neuro-symbolic verification. Achieves state-of-the-art accuracy of 49.92% on HLE (Humanity's Last Exam), surpassing the previous best official score.
- **Key Innovations:** Heterogeneous multi-agent reasoning ensemble; dynamic aggregation layer; architectural heterogeneity outperforms homogeneous baselines with similar/fewer inference tokens.
- **Link:** https://arxiv.org/abs/2607.20268

---

### MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning

- **Authors:** Ruilin Tong et al.
- **Institution:** (Not specified)
- **Abstract:** Proposes MILES, a framework that dynamically expands step-wise memory and applies correctness-optimized memory composition under test-time constraints. Maintains modular memory units (asymmetric pairs of sub-goal embeddings and sub-instructions) with learnable selection heads. Uses coarse-to-fine retrieval: coarse level expands memory and collects supervision, fine stage applies learned selection heads to rerank candidates.
- **Key Innovations:** Modular instruction memory with learnable selection; coarse-to-fine retrieval mechanism; correctness-optimized memory composition for self-improving reasoning.
- **Link:** https://arxiv.org/abs/2607.06974

---

### Loop the Loopies! (Loopie)

- **Authors:** Zitian Gao, Yilong Chen, Yihao Xiao, Xinyu Yang, Ran Tao, Joey Zhou, Bryan Dai
- **Institution:** (Not specified)
- **Abstract:** Presents Loopie, the most powerful looped Transformer to date. Two MoE models: 20B-parameter (2B active) and 6B-parameter (0.6B active). Addresses the long-standing challenge that increasing parameter count by N usually outperforms looping a model N times. Extensive ablations show Loopie substantially outperforms vanilla Transformer baselines at the same compute budget. Achieves gold-medal performance at 2025 IMO and IPhO without tools.
- **Key Innovations:** Breakthrough looped Transformer architecture; MoE-based design; competitive with much larger models; novel post-training pipeline for reasoning.
- **Link:** https://arxiv.org/abs/2607.16051

---

### LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget

- **Authors:** Changhai Zhou et al.
- **Institution:** (Not specified)
- **Abstract:** Architecture-aware execution stack for million-token RL post-training under fixed GPU budgets. Uses GRPO (Group Relative Policy Optimization). Evaluates shared prompt without autograd, retains only model-specific state, replays short response branches one at a time. Implemented for Qwen3.6-27B and GLM-5.2 MoE. On 8 H20 GPUs, completes grouped scoring at 2.1M positions for groups of 2 and 8; stress test reaches 4.46M positions.
- **Key Innovations:** Architecture-aware execution for million-token RL post-training; reduces live training graph at cost of replay time; validated on hybrid recurrent and MoE architectures.
- **Link:** https://arxiv.org/abs/2607.14952

---

### Recursive Harness Self-Improvement (RHI)

- **Authors:** Hyunin Lee, Jinglue Xu, Jeffrey Seely, Donghyun Lee, Matei Zaharia, Yujin Tang
- **Institution:** Sakana AI, UC Berkeley
- **Abstract:** Introduces RHI, which represents the harness as a prompt-level specification of the agent loop and iteratively refines it using pairwise feedback over its own revision history. Across 30 synthetic ML research tasks, few RHI iterations suffice to raise the performance ceiling of low-reasoning-effort agents, exceeding maximum-reasoning-effort settings while reducing inference cost by up to 60%. Gains arise from improved task-specific context management.
- **Key Innovations:** Harness-as-prompt optimization; trajectory-local self-comparison; information-theoretic hypothesis for implicit optimization objective; model-harness co-evolution.
- **Link:** https://arxiv.org/abs/2607.15524

---

### LatentMT: Machine Translation with Latent Reasoning

- **Authors:** Wei-Rui Chen, Samar M. Magdy, Chiyu Zhang, Wenhui Zhu, Zhipeng Wang, Muhammad Abdul-Mageed
- **Institution:** (Not specified)
- **Abstract:** First systematic study of latent-reasoning LoopLMs for machine translation. Adapts a 2.6B-parameter backbone with lightweight training. Across 32 translation directions, achieves performance comparable to models 3-5x larger. SOTA on mid-resource and low-resource languages. Recurrent computation improves quality in early steps then saturates.
- **Key Innovations:** Latent-reasoning for MT; compact model matching much larger models; mechanistic analysis of saturation behavior; efficient training and inference.
- **Link:** https://arxiv.org/abs/2607.18618

---

### Scalable Visual Pretraining for Language Intelligence

- **Authors:** Yiming Zhang, Zhonghan Zhao, Wenwei Zhang, Haiteng Zhao, Tianyang Lin, et al.
- **Institution:** Shanghai AI Laboratory, USTC, Zhejiang University, SJTU
- **Abstract:** Challenges the default assumption that LMs must be trained on text-only representations. Visual Pretraining (VP) framework learns directly from raw documents without text extraction. VP outperforms text-only pretraining while using only 25% of the token budget. Strengthens cross-modal alignment without image-text pair supervision.
- **Key Innovations:** Autoregressive visual pretraining from raw documents; 3.75x token efficiency over text-only pretraining; cross-modal alignment without paired data.
- **Link:** https://arxiv.org/abs/2607.09657

---

### Sparse Delta Memory (SDM): Scaling Linear RNN State through Sparsity

- **Authors:** (Meta FAIR, Inria Paris, University of Tubingen)
- **Institution:** Meta FAIR, Inria Paris & ENS-PSL, University of Tubingen
- **Abstract:** Introduces Sparse Delta Memory, extending Gated DeltaNet by replacing dense key-value outer product with sparse reads/writes to large explicit memory. Scales hidden state by 3 orders of magnitude while maintaining same compute budget. At 8B activated parameters on 1T+ tokens, SDM reaches lower loss and slightly better short-context accuracy than full attention.
- **Key Innovations:** Sparse addressing for 1000x state size scaling; learned initial state as parametric memory; iso-FLOP advantage over full attention; constant compute/memory footprint.
- **Link:** https://arxiv.org/abs/2607.07386

---

### Mamba-3: Improved Sequence Modeling using State Space Principles

- **Authors:** Aakash Lahoti, Kevin Y. Li, Berlin Chen, Caitlin Wang, Aviv Bick, J. Zico Kolter, et al.
- **Institution:** (Not specified, likely CMU/industry)
- **Abstract:** Three core improvements: (1) exponential-trapezoidal discretization for more expressive dynamics, (2) complex-valued state update rule for richer state tracking, (3) MIMO formulation for better performance without increased decode latency. At 1.5B scale, Mamba-3 (MIMO) improves downstream accuracy by +2.2 over Transformers, +1.9 over Mamba-2. Achieves comparable perplexity to Mamba-2 with half the state size.
- **Key Innovations:** Exponential-trapezoidal discretization; complex-valued SSM for state tracking; MIMO formulation; inference-first design.
- **Link:** https://arxiv.org/abs/2603.15569

---

### Black-Mamba: Biologically-Inspired Leaky Accumulation for Conceptual Knowledge under Distribution Drift

- **Authors:** (Not fully specified)
- **Institution:** (Not specified)
- **Abstract:** Event-triggered memory architecture for inference-time adaptation. Augments a base predictor with dynamic memory updated when temporally accumulated surprisal provides sufficient evidence of regime change. Adapts selectively rather than continuously, significantly reducing memory updates during inference while maintaining competitive predictive performance.
- **Key Innovations:** Evidence-gated state tracking; accumulated surprisal for regime change detection; biological memory consolidation inspiration; selective event-driven adaptation.
- **Link:** https://arxiv.org/abs/2607.18899

---

## Recommendation Systems & CTR Prediction

### SAM: Satiation-Aware Mechanism for Post-Purchase Redundancy in Sequential Recommendation

- **Authors:** (Not fully specified)
- **Institution:** (Industrial, likely Chinese e-commerce)
- **Published:** SIGIR 2026
- **Abstract:** Addresses "Interest Exit" in e-commerce where purchases signal intent termination rather than continuation. SAM introduces Dual-path Cross-Attention for intent localization and rhythm estimation, Adaptive Satiation Gating Unit (ASGU) for time-sensitive soft masking, and self-supervised Time-to-Next-Purchase auxiliary task. Reduces Post-Purchase Repeat Rate by over 60%. Online A/B: +1.1% CTR, +0.9% GMV.
- **Key Innovations:** Explicit interest lifecycle modeling; retroactive suppression of fulfilled intents; personalized repurchase cycle prediction; dramatically reduces redundant recommendations.
- **Link:** https://arxiv.org/abs/2607.12714

---

### GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning for CTR Prediction

- **Authors:** (Not fully specified)
- **Institution:** (Not specified)
- **Published:** WWW 2026
- **Abstract:** Proposes generative user intent framework leveraging semantic interest cohorts. Generative model trained with NTP objective produces candidate interest cohorts. Hierarchical candidate-aware network injects contextual signal into ranking via cross-attention. End-to-end training with self-supervised regularization. Outperforms competitive baselines on three datasets.
- **Key Innovations:** Generative paradigm for CTR; semantic interest cohorts as explicit intent representations; hierarchical candidate-aware modeling; end-to-end recall-ranking alignment.
- **Link:** https://arxiv.org/abs/2601.18251

---

### IDProxy: Cold-Start CTR Prediction with Multimodal LLMs at Xiaohongshu

- **Authors:** (Xiaohongshu team)
- **Institution:** Xiaohongshu
- **Abstract:** Leverages multimodal LLMs to generate proxy embeddings from rich content signals for new items without usage data. Proxy embeddings are explicitly aligned with existing ID embedding space and optimized end-to-end under CTR objectives. Deployed in Content Feed and Display Ads serving hundreds of millions of users daily.
- **Key Innovations:** MLLM-generated proxy embeddings for cold-start; end-to-end alignment with ID embedding space; production deployment at scale.
- **Link:** https://arxiv.org/abs/2603.01590

---

### Long-History User Transformers for Real-Time Ad Ranking

- **Authors:** (Yandex team, likely Khrylchenko et al. referenced)
- **Institution:** Yandex
- **Abstract:** Multi-stage transformer architecture decouples history encoding from real-time inference. Large offline transformer asynchronously encodes full cross-surface interaction history into cached representation. Lightweight runtime model combines cached representation with recent events. Recovers 72-80% of full-history quality. Production A/B: +2.77% Search Ads, +2.1% YAN ranking metric, +2.26% Search revenue.
- **Key Innovations:** Offline/online split for deployable long-history modeling; autoregressive pre-training with dual objective (feedback + next-item prediction); production-validated latency-free gains.
- **Link:** https://arxiv.org/abs/2607.14331

---

### FAT: Field-Aware Transformer for CTR Prediction

- **Authors:** (Not fully specified)
- **Institution:** Alibaba/Taobao (based on production deployment)
- **Published:** KDD 2026
- **Abstract:** Addresses structural misalignment between sequential Transformers and combinatorial CTR data. FAT reconstructs Transformer block with field-centric parameters. Basis-Composed Hypernetwork synthesizes field-specific parameters from shared bases. Theoretical scaling law via Rademacher complexity. Live on Taobao: +2.33% CTR, +0.66% RPM with P99 latency 45ms→48ms.
- **Key Innovations:** Field-decomposed attention; structured expressivity aligned with heterogeneous fields; basis-composed hypernetwork for parameter efficiency; formal scaling law for CTR.
- **Link:** https://arxiv.org/abs/2511.12081

---

### UniRec: Bridging Generative and Discriminative Recommendation via Chain-of-Attribute

- **Authors:** (Shopee team)
- **Institution:** Shopee
- **Abstract:** Chain-of-Attribute (CoA) prefixes each SID sequence with structured attribute tokens (category, seller, brand) before decoding, recovering item-side feature crossing. Capacity-constrained SID suppresses token collapse. Conditional Decoding Context stabilizes multi-scenario decoding. Joint RFT and DPO alignment. Outperforms strongest baseline by +22.6% HR@50. Online A/B: +5.37% PVCTR, +4.76% orders, +5.60% GMV.
- **Key Innovations:** Chain-of-Attribute as speculate-then-refine paradigm; proven per-step entropy reduction; capacity-constrained SID for long-tail fairness; end-to-end generative recommendation at 110ms latency.
- **Link:** https://arxiv.org/abs/2604.12234

---

### DAIAN: Deep Adaptive Intent-Aware Network for Trigger-Induced Recommendation

- **Authors:** Zhihao Lv, Longtao Zhang, Ailong He, Shuzhi Cao, Shuguang Han, Jufeng Chen
- **Institution:** (Xianyu/Alibaba)
- **Abstract:** Addresses "intent myopia" in Trigger-Induced Recommendation where systems overemphasize trigger items. DAIAN extracts personalized intent representations via correlation analysis, retrieves related historical behaviors for diverse intents, and uses hybrid enhancer with ID and semantic information. Online on Xianyu: +1.59% CTR, +1.73% diversity, +2.37% bills.
- **Key Innovations:** Intent distribution modeling (explicit + implicit); hybrid ID+semantic similarity enhancer; adaptive selection for diverse intents; three-stage training strategy.
- **Link:** https://arxiv.org/abs/2602.13971

---

### Sparse Attention on Long-term Behaviors for CTR Prediction

- **Authors:** (Not fully specified)
- **Institution:** (Not specified)
- **Abstract:** Explores sparse attention mechanisms for long-term user behavior modeling in CTR prediction. Addresses the computational challenge of applying attention to very long behavior sequences in industrial recommendation systems.
- **Key Innovations:** Efficient sparse attention for long-term behaviors; practical deployment considerations for industrial CTR.
- **Link:** https://arxiv.org/abs/2601.17836

---

## Sequential Modeling & Time Series

### User-Centric Modeling of Transactional Sequences with Explainable State Space Models

- **Authors:** (Not fully specified)
- **Institution:** (Not specified)
- **Published:** July 22, 2026
- **Abstract:** Hybrid approach combining contrastive representation learning (CoLES) with Mamba SSMs for transactional event sequences. Two integration strategies: initializing Mamba hidden state with CoLES embedding, and prepending projected CoLES embedding as prefix token. Converges 2-3x faster than plain SSM baseline. Explainability via discretization-step maps and Integrated Gradients.
- **Key Innovations:** CoLES-Mamba hybrid for user sequence modeling; faster convergence; novel explainability insights into transactional event filtering.
- **Link:** https://arxiv.org/abs/2607.20228

---

### Expanding Flow Maps (EFMs)

- **Authors:** Sophia Tang, Pranam Chatterjee
- **Institution:** (Not specified)
- **Abstract:** Introduces Expanding Generative Flows (EFlows) defining flows between distributions of increasing dimensionality. Proposes EFMs that distill expanding interpolant into efficient few-step generative models. Each EFM factors the map into expand operator and transport map. Extends to discrete simplex for variable-size graph generation and variable-length sequence generation.
- **Key Innovations:** Flows across increasing dimensionality; expand + transport factorization; variable-size/variable-length generation; unified continuous and discrete framework.
- **Link:** https://arxiv.org/abs/2607.21585

---

### Accelerating A/B-Tests with Counterfactual Estimation

- **Authors:** Olivier Jeunen et al.
- **Institution:** (Not specified)
- **Abstract:** Proposes experimental protocol exploiting policy overlap to accelerate A/B testing. Frames randomized treatment assignment as meta-policy, leverages Delta-Off-Policy Estimation for unbiased average treatment effect estimates. Variance scales with divergence between policies rather than raw outcome variance. Dominates standard Difference-in-Means when policies have common support.
- **Key Innovations:** Policy-overlap-based A/B test acceleration; variance reduction via structural policy relationships; applicable to recommender systems and LLM interfaces.
- **Link:** https://arxiv.org/abs/2607.14604

---

## Games & Multi-Agent Systems

### Augmenting Game AI with Deep Reinforcement Learning

- **Authors:** Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslen
- **Institution:** EA SPORTS (implied by FC 25 context)
- **Abstract:** Proposes framework for training RL models for game AI in AAA production. Demonstrates SAC-based goalkeeper AI in EA SPORTS FC 25 with strict 200us inference budget. Achieves overnight training via high update-to-data ratio, network resets, offline data, and scenario-based training (4 days → 12 hours). 300K parameter MLP achieves 170us inference.
- **Key Innovations:** Production-constrained RL for game AI; overnight training pipeline; modular integration with existing game AI; strict runtime inference constraints.
- **Link:** https://arxiv.org/abs/2606.20210

---

### PR-MRE: Minimax-Regret Equilibria for Adversarial Team Games under Asymmetric Information

- **Authors:** (Not fully specified)
- **Institution:** (Not specified)
- **Abstract:** Introduces Probabilistically Robust Minimax-Regret Equilibrium (PR-MRE) combining distribution-free robustness with probabilistic type distribution information. Formulated as robust bilinear program with tractable semidefinite relaxation. PRMRE-PSRO meta-solver enables population-based learning via deep RL best responses. Shows substantially improved worst-case performance under strategic distribution shifts.
- **Key Innovations:** PR-MRE equilibrium concept; robust bilinear program formulation; semidefinite relaxation; PRMRE-PSRO meta-solver.
- **Link:** https://arxiv.org/abs/2607.09993

---

### Paradoxes of Game Theoretic Equilibria and Price of Anarchy

- **Authors:** Ioannis Piliouras, Ian Gemp, Siqi Liu, Luke Marris (DeepMind, implied)
- **Institution:** (Not fully specified)
- **Abstract:** Proves static equilibria are topologically unstable and discrete-time learning in congestion games leads to Li-Yorke chaos and exponential efficiency degradation. Interior Nash equilibria lack C1 vector field information. Worst-case pure Nash equilibria are topologically unstable strict saddles. Non-atomic congestion games destabilize into chaos with exponentially degrading time-averaged inefficiency.
- **Key Innovations:** Topological instability of Nash equilibria; Li-Yorke chaos in congestion games; exponential efficiency degradation; challenges foundations of static equilibrium frameworks.
- **Link:** https://arxiv.org/abs/2607.11752

---

### Mean Field Reinforcement Learning (Monograph)

- **Authors:** Mathieu Lauriere et al.
- **Institution:** (Not fully specified)
- **Abstract:** Comprehensive introduction to mean field RL through MDPs from large-population stochastic control. Covers dynamic programming, propagation-of-chaos limits, tabular Q-learning, policy gradient methods, and deep RL (DDPG). Bridges mean field control theory and RL methodology for large stochastic populations.
- **Key Innovations:** Unified bridge between mean field control theory and RL; mathematical framework for large-population learning; theoretical analyses of tabular and deep methods.
- **Link:** https://arxiv.org/abs/2607.01525

---

### NePPO: Near-Potential Policy Optimization for General-Sum MARL

- **Authors:** Addison Kalanther, Sanika Bharvirkar, Shankar P. Sastry, Chinmay Maheshwari
- **Institution:** (Not specified)
- **Abstract:** Proposes learning a player-independent potential function such that Nash equilibrium of a cooperative game with this potential approximates Nash equilibrium of the original general-sum game. Uses zeroth-order gradient descent. Shows superior performance compared to IPPO and MAPPO on matrix games and multi-particle environments.
- **Key Innovations:** Potential function learning for Nash approximation; works in general-sum (not just zero-sum/cooperative); zeroth-order optimization pipeline; outperforms IPPO/MAPPO.
- **Link:** https://arxiv.org/abs/2603.06977

---

### Reasonably Reasoning AI Agents Avoid Game-Theoretic Failures in Zero-Shot

- **Authors:** Enoch Hyunwook Kang
- **Institution:** (Not specified)
- **Abstract:** Proves that AI agents acting as Bayesian posterior samplers are guaranteed to eventually become weakly close to Nash equilibrium in infinitely repeated games. Extends to settings with unknown stage payoffs and private stochastic observations. Empirically validated across five repeated-game environments from Prisoner's Dilemma to marketing promotion games.
- **Key Innovations:** Theoretical guarantee of zero-shot Nash convergence; Bayesian learning (not expected utility maximization); grain-of-truth condition; no strategic post-training required.
- **Link:** https://arxiv.org/abs/2603.18563

---

### Equilibrium with Internal Transfers (SETE & M-SETE)

- **Authors:** (Not fully specified)
- **Institution:** (Not specified)
- **Published:** ACM EC 2026
- **Abstract:** Introduces Self-Enforcing Transfer Equilibrium (SETE) where players commit to nonnegative peer-to-peer transfers paid only if recipient does not deviate. For polymatrix games, any socially optimal strategy profile can be sustained as SETE. Mediated variant (M-SETE) makes transfers binding, supporting any socially optimal profile in any finite game. Polynomial-time algorithm for polymatrix games.
- **Key Innovations:** Internal transfers for welfare improvement; polynomial-time computation (vs PPAD-hard NE); decentralized learning dynamic; budget-balanced mechanism.
- **Link:** https://arxiv.org/abs/2606.20960

---

### RL: From Algorithms To Foundation Models (PhD Thesis)

- **Authors:** Zihan Ding
- **Institution:** Princeton University
- **Abstract:** Studies RL from two perspectives: algorithms in games (two-player zero-sum, video games, multi-player general-sum) and RL in foundation model era (diffusion-based world models, RL for video generation, generative models as policy classes, interactive video world models). Unified view of RL as objective-driven adaptation in complex sequential domains.
- **Key Innovations:** Comprehensive thesis connecting game-theoretic RL with foundation model applications; diffusion-based world models; generative models as policy classes.
- **Link:** https://arxiv.org/abs/2607.17560

---

*Report generated: 2026-07-25*
