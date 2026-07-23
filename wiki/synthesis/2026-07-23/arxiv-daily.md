---
title: "arXiv Daily — 2026-07-23"
type: synthesis
created: 2026-07-23
updated: 2026-07-23
sources: []
tags: [arxiv-daily, LLM, recommendation, CTR, sequential-modeling, games, advertising]
---

# arXiv Daily Report — 2026-07-23

## 1. Large Language Models (LLMs)

---

### 1.1 MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning

| Field | Detail |
|-------|--------|
| **Authors** | Ruilin Tong et al. |
| **Institution** | — |
| **Abstract** | LLMs improve reasoning at test time via additional computation, but most methods treat each problem in isolation. MILES dynamically expands step-wise memory with asymmetric sub-goal/instruction pairs and applies correctness-optimized memory selection under test-time constraints. A coarse-to-fine retrieval mechanism enables memory expansion from confident samples and learned reranking for uncertain samples. |
| **Key Innovations** | Modular instruction memory with learnable selection heads; coarse-to-fine retrieval mechanism; correctness-optimized memory composition; superior accuracy-efficiency tradeoffs. |
| **Link** | [arXiv:2607.06974](https://arxiv.org/abs/2607.06974) |

---

### 1.2 In-Place Tokenizer Expansion for Pre-trained LLMs

| Field | Detail |
|-------|--------|
| **Authors** | Jimmy Smith et al. |
| **Institution** | — |
| **Abstract** | Proposes an in-place recipe for upgrading a pre-trained model's tokenizer by continuing BPE merges on a multilingual corpus. New tokens are initialized as the mean of their source sub-token embeddings. Applied to LFM2-8B-A1B to produce LFM2.5-8B-A1B with a 128K tokenizer, achieving ~2.4–2.6× fewer tokens for Hindi/Vietnamese and 2.2–3.7× per-character decode speedup. |
| **Key Innovations** | In-place tokenizer expansion preserving source tokens; mean embedding initialization for new tokens; two-stage adaptation (embedding-only then full-model); significant latency reduction for underrepresented languages. |
| **Link** | [arXiv:2607.15232](https://arxiv.org/abs/2607.15232) |

---

### 1.3 Belief-Reality Separation in Language Models

| Field | Detail |
|-------|--------|
| **Authors** | Oliver Steele et al. |
| **Institution** | — |
| **Abstract** | Investigates how LLMs separate character beliefs from reality. Shows it rests on two mechanisms: a generic value slot binding attributed values, and a router at the query position selecting which frame (belief vs. reality) a query reads out. The slot itself carries no belief-reality tag; separation lives in dissociated routing subspaces. Emerges between 3B and 7B across five model families. |
| **Key Innovations** | Identification of value slot + router mechanism for belief-reality separation; visibility-gated lookback for derived beliefs; cross-architecture validation; companion paper extends to counterfactual/fictional/temporal contexts. |
| **Link** | [arXiv:2607.11945](https://arxiv.org/abs/2607.11945) |

---

### 1.4 LLM-as-a-Verifier: A General-Purpose Verification Framework

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Institution** | — |
| **Abstract** | Introduces verification as a new scaling axis for LLMs. Computes expectation over scoring token logits for continuous scores, reducing tie rates. Scales across score granularity, repeated evaluation, and criteria decomposition. Achieves SOTA on Terminal-Bench V2 (86.5%), SWE-Bench Verified (78.2%), RoboRewardBench (87.4%), MedAgentBench (73.3%). Also serves as dense reward signal for RL. |
| **Key Innovations** | Continuous scoring via logit expectation; multi-dimensional verification scaling; cost-efficient ranking algorithm; training-free and plug-and-play across domains; dense RL reward signal. |
| **Link** | [arXiv:2607.05391](https://arxiv.org/abs/2607.05391) |

---

### 1.5 Set Diffusion: Interpolating Token Orderings Between Autoregression and Diffusion

| Field | Detail |
|-------|--------|
| **Authors** | Marianne Arriola et al. |
| **Institution** | — |
| **Abstract** | Presents set diffusion, a new class of language models with likelihood factorization over flexible-position token sets and a set-causal diffusion architecture supporting KV cache updates. Tokens can be decoded in arbitrarily-ordered sets including sliding-window sets. Achieves better speed-quality tradeoffs on math reasoning, summarization, and unconditional generation. |
| **Key Innovations** | Set-causal diffusion architecture with KV caching; factorization over token sets (not fixed blocks); any-order decoding; strong infilling performance. Accepted at ICML 2026. |
| **Link** | [arXiv:2607.01775](https://arxiv.org/abs/2607.01775) |

---

### 1.6 LatentMT: Machine Translation with Latent Reasoning

| Field | Detail |
|-------|--------|
| **Authors** | Wei-Rui Chen et al. |
| **Institution** | — |
| **Abstract** | First systematic study of latent-reasoning LoopLMs for MT. Adapts a 2.6B-parameter backbone with lightweight training across 32 translation directions. Achieves performance comparable to models 3–5× larger. Recurrent computation improves quality in early steps then saturates. Requires lower training and inference compute than larger non-latent models. |
| **Key Innovations** | Latent recurrent computation for MT; scaling analysis of recurrent reasoning steps; mechanistic analysis of hidden-representation shrinkage; efficiency gains over parameter-matched baselines. |
| **Link** | [arXiv:2607.18618](https://arxiv.org/abs/2607.18618) |

---

### 1.7 An Early Warning of Emerging Biosecurity Risks in Frontier LLMs

| Field | Detail |
|-------|--------|
| **Authors** | Tong Wu et al. |
| **Institution** | — |
| **Abstract** | Develops Intern-BioBreaker, a bio-red-teaming model, with a computational-to-physical framework coupling model stress testing with wet-lab validation. Reveals widespread bio-risk jailbreak vulnerabilities across frontier LLMs, with GPT-5.5 inducible to generate modified viral candidate sequences. End-to-end verification confirms model-generated designs can be physically realized. |
| **Key Innovations** | Integrated computational-to-physical biosecurity framework; near-saturated ASR on frontier models; demonstration that model-generated biological designs are physically realizable. |
| **Link** | [arXiv:2607.18056](https://arxiv.org/abs/2607.18056) |

---

## 2. Recommendation Systems

---

### 2.1 SaFeAU: Semantic Factor Learning for Collaborative Filtering

| Field | Detail |
|-------|--------|
| **Authors** | Yajie Yu, Chenzhong Bin, Zhoubo Xu, Zhixin Zeng, Tongxin Xu, Cihan Xia et al. |
| **Institution** | — |
| **Abstract** | Augments interacted instances with semantic factors to mitigate false negative labeling in CF. Consists of Semantic Factor Routing (disentangling item representations), Semantic Factor Matching (identifying potential positive pairs), and Semantic Pairs Alignment. Outperforms GCN-based and MF-based SOTA on sparse datasets. |
| **Key Innovations** | Semantic factor disentanglement for CF; false negative mitigation via semantic matching; graph-free high-order CF signal capture; superior computational efficiency. |
| **Link** | [arXiv:2605.31414](https://arxiv.org/abs/2605.31414) |

---

### 2.2 TAGCF: LLM-Driven Attribute Augmentation for Collaborative Filtering

| Field | Detail |
|-------|--------|
| **Authors** | Junjie Meng, Ranxu Zhang, Wei Wu, Rui Zhang, Chuan Qin, Qi Zhang et al. |
| **Institution** | — |
| **Abstract** | Transforms LLM-derived semantic knowledge into topological connectivity. Uses LLMs to infer interaction intents from user-item pairs, creating intermediate attribute nodes in an enriched U-A-I graph. Adaptive Relation-weighted Graph Convolution dynamically estimates relation importance. |
| **Key Innovations** | Semantic-to-topology transformation; U-A-I tripartite graph augmentation; adaptive relation-weighted GCN; model-agnostic framework. |
| **Link** | [arXiv:2602.21099](https://arxiv.org/abs/2602.21099) |

---

### 2.3 Rethinking Semantic–Collaborative Integration: Why Alignment Is Not Enough

| Field | Detail |
|-------|--------|
| **Authors** | Maolin Wang, Dongze Wu, Jianing Zhou, Hongyu Chen, Beining Bao, Yu Jiang et al. |
| **Institution** | — |
| **Abstract** | Argues that global geometric alignment between semantic and collaborative representations is often structurally mismatched. Proposes complementarity-aware design where shared factors are selectively integrated while private signals are preserved. Develops diagnostics quantifying overlap, unique-hit contribution, and theoretical fusion upper bounds. |
| **Key Innovations** | Shared-plus-private latent structure formalization; complementarity-aware diagnostics; critique of alignment-centric integration; advocacy for complementarity fusion-centric design. |
| **Link** | [arXiv:2604.22195](https://arxiv.org/abs/2604.22195) |

---

### 2.4 PI2I: Personalized Item-Based CF Retrieval Framework

| Field | Detail |
|-------|--------|
| **Authors** | Shaoqing Wang et al. |
| **Institution** | Alibaba (Taobao) |
| **Abstract** | Two-stage retrieval framework enhancing CF personalization. IBS optimizes retrieval pool by relaxing truncation; PRS introduces interactive scoring model overcoming inner product limitations. Deployed on Taobao's "Guess You Like" with 1.05% increase in online transaction rates. Released 130M interaction dataset. |
| **Key Innovations** | Personalized two-stage CF retrieval; interactive scoring model; trigger-target negative sampling; large-scale public dataset release. Published at WWW 2026. |
| **Link** | [arXiv:2601.16815](https://arxiv.org/abs/2601.16815) |

---

### 2.5 AlphaFree: Recommendation Free from Users, IDs, and GNNs

| Field | Detail |
|-------|--------|
| **Authors** | Minseo Jeon, Junwoo Jung, Daewon Gwak, Jinhong Jung |
| **Institution** | — |
| **Abstract** | User-free, ID-free, GNN-free recommendation method. Replaces raw IDs with language representations, infers preferences on-the-fly, and captures collaborative signals through behavioral/semantic augmentation with contrastive learning. Achieves up to 40% improvement over non-LR methods and 5.7% over LR-based methods. |
| **Key Innovations** | Triple-free design (user/ID/GNN); on-the-fly preference modeling; behavioral+semantic augmentation; lightweight MLP inference. Published at WWW 2026. |
| **Link** | [arXiv:2603.02653](https://arxiv.org/abs/2603.02653) |

---

### 2.6 SOLAR: SVD-Optimized Lifelong Attention for Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Chenghao Zhang, Chao Feng, Yuanhao Pu, Xunyong Yang, Wenhui Yu, Xiang Li et al. |
| **Institution** | Kuaishou |
| **Abstract** | Introduces SVD-Attention exploiting low-rank structure in shared KV matrices, reducing complexity from O(N²d) to O(Ndr) while preserving softmax. SOLAR supports behavior sequences of 10K+ scale and candidate sets of thousands without filtering. Deployed at Kuaishou with 0.68% Video Views gain. |
| **Key Innovations** | SVD-Attention preserving softmax with linear-rank complexity; set-wise ranking with lifelong histories; theoretical analysis of ranking bias and generalization in set-wise recommendation. |
| **Link** | [arXiv:2603.02561](https://arxiv.org/abs/2603.02561) |

---

## 3. Click-Through Rate (CTR) Prediction & Advertising

---

### 3.1 CADET: Context-Conditioned Ads CTR Prediction with Decoder-Only Transformer

| Field | Detail |
|-------|--------|
| **Authors** | David Pardoe, Neil Daftary, Miro Furtado, Aditya Aiyer, Yu Wang, Liuqing Li et al. |
| **Institution** | LinkedIn |
| **Abstract** | End-to-end decoder-only transformer for ads CTR prediction deployed at LinkedIn. Features multi-tower prediction heads for post-scoring signals, self-gated attention, timestamp-based RoPE, session masking, and production engineering for Flash Attention. Achieves 11.04% CTR lift vs. production baseline. |
| **Key Innovations** | Context-conditioned decoding resolving CTR-ranking chicken-and-egg; self-gated attention for training stability; timestamp RoPE capturing multi-timescale temporal relations; session masking for train-serve consistency. |
| **Link** | [arXiv:2602.11410](https://arxiv.org/abs/2602.11410) |

---

### 3.2 GRAB: LLM-Inspired Sequence-First CTR Prediction at Baidu

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Institution** | Baidu |
| **Abstract** | End-to-end generative framework for CTR prediction inspired by LLM scaling. Integrates Causal Action-aware Multi-channel Attention (CamA) for temporal dynamics and action signals. Online deployment shows 3.05% revenue increase and 3.49% CTR rise. Demonstrates monotonic, approximately linear scaling with longer sequences. |
| **Key Innovations** | Generative CTR paradigm from LLM scaling insights; CamA mechanism for temporal+action signals; validated scaling behavior with sequence length. |
| **Link** | [arXiv:2602.01865](https://arxiv.org/abs/2602.01865) |

---

### 3.3 EST: Efficiently Scalable Transformer for CTR Prediction

| Field | Detail |
|-------|--------|
| **Authors** | Mingyang Liu, Yong Bai, Zhangming Chan, Sishuo Chen, Xiang-Rong Sheng, Han Zhu et al. |
| **Institution** | Alibaba (Taobao) |
| **Abstract** | Achieves fully unified modeling of all raw inputs in a single sequence. Lightweight Cross Attention (LCA) prunes redundant self-interactions; Content Sparse Attention (CSA) uses content similarity for dynamic behavior selection. Exhibits stable power-law scaling. Deployed on Taobao with 3.27% RPM increase and 1.22% CTR lift. |
| **Key Innovations** | Fully unified modeling without lossy aggregation; LCA for cross-feature interactions; CSA for content-guided sparse attention; demonstrated power-law scaling for CTR. |
| **Link** | [arXiv:2602.10811](https://arxiv.org/abs/2602.10811) |

---

### 3.4 Long-History User Transformers for Real-Time Ad Ranking

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Institution** | Yandex |
| **Abstract** | Multi-stage architecture decoupling history encoding from real-time inference. Large offline transformer asynchronously encodes full cross-surface history into cached representation; lightweight runtime model combines cached + recent events. Pre-trained with feedback + next-item prediction. Improves primary metric by +2.77% (search ads) and +2.1% (YAN). |
| **Key Innovations** | Offline/online split recovering 72–80% of full-history quality; robustness to staleness enabling cheap refresh; production deployment without latency increase. |
| **Link** | [arXiv:2607.14331](https://arxiv.org/abs/2607.14331) |

---

### 3.5 IDProxy: Cold-Start CTR Prediction at Xiaohongshu with Multimodal LLMs

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Institution** | Xiaohongshu |
| **Abstract** | Leverages multimodal LLMs to generate proxy embeddings from content signals for cold-start CTR prediction. Proxies are explicitly aligned with existing ID embedding space and optimized end-to-end under CTR objectives. Deployed in Content Feed and Display Ads serving hundreds of millions of users daily. |
| **Key Innovations** | MLLM-generated proxy embeddings for cold-start; end-to-end alignment with ID embedding space; seamless integration into existing ranking pipelines. |
| **Link** | [arXiv:2603.01590](https://arxiv.org/abs/2603.01590) |

---

### 3.6 GenCI: Generative User Intent via Cohort-based Learning for CTR Prediction

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Institution** | — |
| **Abstract** | Generative framework leveraging semantic interest cohorts for dynamic user preferences. Trains a generative model with next-item prediction to produce candidate interest cohorts as candidate-agnostic intent representations. Hierarchical candidate-aware network injects contextual signal into ranking. Published at WWW 2026. |
| **Key Innovations** | Generative intent modeling via semantic cohorts; candidate-agnostic intent representation; hierarchical candidate-aware cross-attention; joint end-to-end training with self-supervised regularization. |
| **Link** | [arXiv:2601.18251](https://arxiv.org/abs/2601.18251) |

---

### 3.7 LLM-HYPER: Generative CTR Modeling via LLM-Based Hypernetworks

| Field | Detail |
|-------|--------|
| **Authors** | Luyi Ma, Wanjia Sherry Zhang, Zezhong Fan, Shubham Thakur, Kai Zhao, K. C. Yao et al. |
| **Institution** | — (Top US e-commerce platform) |
| **Abstract** | Treats LLMs as hypernetworks to directly generate CTR estimator parameters in a training-free manner. Uses few-shot Chain-of-Thought prompting over multimodal ad content. Outperforms cold-start baselines by 55.9% in NDCG@10. Achieves competitive CTR with warm-start model in 30-day online A/B test. Deployed in production. |
| **Key Innovations** | LLM-as-hypernetwork for parameter generation; training-free cold-start; multimodal CoT prompting with CLIP retrieval; normalization/calibration for production readiness. |
| **Link** | [arXiv:2604.12096](https://arxiv.org/abs/2604.12096) |

---

### 3.8 DAIAN: Deep Adaptive Intent-Aware Network for Trigger-Induced Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Institution** | Alibaba (Xianyu) |
| **Abstract** | Addresses intent myopia in trigger-induced recommendation. Extracts personalized intent representations by analyzing trigger-click correlations, retrieves related historical behaviors for diverse intent mining. Hybrid enhancer with ID+semantic information strengthens similarity. Online on Xianyu: +1.59% CTR, +1.73% diversity, +2.37% bills. |
| **Key Innovations** | Trigger-induced intent modeling with intent myopia solution; diverse intent extraction from historical behaviors; hybrid ID+semantic similarity enhancement; three-stage training strategy. |
| **Link** | [arXiv:2602.13971](https://arxiv.org/abs/2602.13971) |

---

## 4. Sequential Modeling for Recommendation

---

### 4.1 HyTRec: Hybrid Temporal-Aware Attention for Long Behavior Sequences

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Institution** | — |
| **Abstract** | Hybrid attention architecture decoupling long-term stable preferences from short-term intent spikes. Assigns massive history to linear attention and reserves softmax for recent interactions. Temporal-Aware Delta Network (TADN) dynamically upweights fresh signals. Over 8% Hit Rate improvement for ultra-long sequences. |
| **Key Innovations** | Linear+softmax hybrid attention at 7:1 ratio; TADN with exponential gating for temporal awareness; near-linear inference complexity; industrial-scale validation on 10K+ interactions. |
| **Link** | [arXiv:2602.18283](https://arxiv.org/abs/2602.18283) |

---

### 4.2 CMSL: Constructive Multi-Sequence Learning at Meta

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Institution** | Meta |
| **Abstract** | Paradigm shift from monolithic sequence ingestion to active "context engineering." Learnable Sequence Construction Module disentangles user history into thematic strands via cross-attention, modeled individually with linear attention. Addresses "context pollution" in heterogeneous histories. Deployed across ranking/retrieval on four major Meta surfaces. |
| **Key Innovations** | Context engineering for recommendation via learnable multi-sequence construction; intent-aware cross-attention disentanglement; scalable linear attention for multi-sequence modeling; production deployment at massive scale. |
| **Link** | [arXiv:2606.28533](https://arxiv.org/abs/2606.28533) |

---

### 4.3 GEMs: Multi-Stream Decoder for Generative Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Institution** | — |
| **Abstract** | Partitions user behaviors into Recent, Mid-term, and Lifecycle streams with tailored inference schemes. Recent: one-stage real-time extractor. Mid-term: lightweight indexer with cross-attention. Lifecycle: two-stage offline-online compression. First lifelong GR framework deployed in high-concurrency industrial environment, processing 100K+ interactions. |
| **Key Innovations** | Multi-stream temporal decomposition (recent/mid/lifecycle); lightweight indexer for mid-term attention; two-stage lifecycle compression; parameter-free fusion; industrial deployment with 100K+ sequence support. |
| **Link** | [arXiv:2602.13631](https://arxiv.org/abs/2602.13631) |

---

### 4.4 RecRec: Latent Interests Recursive Reasoning for Sequential Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Institution** | — |
| **Abstract** | Decouples reasoning from prediction in sequential recommendation. Context Compressor distills hidden states into R latent interests with diversity regularization. Recursive Reasoner refines interests in separate intermediate latent space. Deep supervision allows free adjustment of reasoning depth at inference without retraining. |
| **Key Innovations** | Decoupled reasoning/prediction states; multi-vector latent interest representation; interest diversity regularization; adjustable reasoning depth at inference; backbone-agnostic framework. |
| **Link** | [arXiv:2607.12945](https://arxiv.org/abs/2607.12945) |

---

### 4.5 Beyond Positive Signals: Mixed-Polarity Behavior Sequences

| Field | Detail |
|-------|--------|
| **Authors** | Zexuan Cheng, Yue Liu, Jun Zhang, J Jiang |
| **Institution** | — |
| **Abstract** | Demonstrates that mixed-polarity behavior sequences (interleaving positive and negative tokens) consistently outperform positive-only sequences across diverse architectures. Proposes Target-Aware Polarity Fusion (TAPF) for differentiating behavioral evidence. Shows +1.9% to +9.6% relative AUC improvements. |
| **Key Innovations** | Mixed-polarity sequence paradigm; Target-Aware Polarity Fusion gating; validation across five architectures; insight that the data paradigm itself is the primary contribution. |
| **Link** | [arXiv:2606.15252](https://arxiv.org/abs/2606.15252) |

---

### 4.6 Efficient Sequential Recommendation via Personalization

| Field | Detail |
|-------|--------|
| **Authors** | — (Meta/Facebook Research) |
| **Institution** | Meta |
| **Abstract** | Compresses long user interaction histories into learnable tokens combined with recent interactions. Applied to HSTU and HLLM, achieves comparable performance to full-sequence baselines with dramatically reduced computational cost. Validated on large-scale datasets. |
| **Key Innovations** | Personalized expert tokens for sequence compression; compatible with HSTU and HLLM; significant computational savings with minimal quality loss. |
| **Link** | [arXiv:2601.03479](https://arxiv.org/abs/2601.03479) |

---

### 4.7 GCB: Generative Chain of Behavior for User Trajectory Prediction

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Institution** | — |
| **Abstract** | Models user interactions as autoregressive chain of semantic behaviors over multiple future steps. Encodes items into semantic IDs via RQ-VAE with k-means refinement. Transformer-based generator predicts multi-step future behaviors capturing long-horizon intent transitions. |
| **Key Innovations** | Multi-step trajectory generation beyond next-item prediction; RQ-VAE semantic ID encoding; coherent trajectory generation; unified generative formulation for preference evolution. |
| **Link** | [arXiv:2601.18213](https://arxiv.org/abs/2601.18213) |

---

## 5. Games, Game Theory & Multi-Agent Systems

---

### 5.1 Competition and Cooperation of LLM Agents in Games

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Institution** | — |
| **Abstract** | Studies LLM agent interactions in network resource allocation and Cournot competition games. Finds LLM agents tend to cooperate (rather than converge to Nash equilibria) when given multi-round prompts and non-zero-sum context. Chain-of-thought analysis reveals fairness reasoning is central. Proposes analytical framework capturing LLM reasoning dynamics. |
| **Key Innovations** | Discovery of LLM cooperation tendency in non-zero-sum games; fairness-driven chain-of-thought reasoning analysis; analytical framework for LLM strategic dynamics. |
| **Link** | [arXiv:2604.00487](https://arxiv.org/abs/2604.00487) |

---

### 5.2 Reasonably Reasoning AI Agents Avoid Game-Theoretic Failures

| Field | Detail |
|-------|--------|
| **Authors** | Enoch Hyunwook Kang |
| **Institution** | — |
| **Abstract** | Proves that AI agents acting as Bayesian posterior samplers are guaranteed to eventually become weakly close to Nash equilibrium in infinitely repeated games. Extends to unknown stage payoffs with private stochastic observations. Validated across five environments from Prisoner's Dilemma to marketing games. |
| **Key Innovations** | Theoretical proof of zero-shot Nash convergence for reasoning LLM agents; "reasonably reasoning" agent formalization (Bayesian updating + asymptotic best-response); extension to unknown-payoff settings. |
| **Link** | [arXiv:2603.18563](https://arxiv.org/abs/2603.18563) |

---

### 5.3 MEMO: Memory-Augmented Model Context Optimization for Multi-Agent LLM Games

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Institution** | — |
| **Abstract** | Self-play framework optimizing inference-time context via retention (persistent memory bank with CRUD-style operations) and exploration (tournament-style prompt evolution with TRUESKILL). Raises GPT-4o-mini mean win rate from 25.1% to 49.5% with only 2,000 self-play games (19× fewer than RL baselines). Reduces run-to-run variance by 7×. |
| **Key Innovations** | Persistent memory for cumulative learning across self-play episodes; tournament-style context evolution; prioritized replay for rare states; weight-free optimization; cross-game context generalization. |
| **Link** | [arXiv:2603.09022](https://arxiv.org/abs/2603.09022) |

---

### 5.4 STRATAGEM: Transferable Reasoning via Game Self-Play

| Field | Detail |
|-------|--------|
| **Authors** | Xiachong Feng, Deyi Yin, Xiaocheng Feng, Yi Jiang, Libo Qin, Yangfan Ye et al. |
| **Institution** | — |
| **Abstract** | Addresses domain specificity and contextual stasis in game-based reasoning transfer. Reasoning Transferability Coefficient (φ) measures abstraction level; Reasoning Evolution Reward (ψ) incentivizes progressive reasoning. Achieves consistent improvements across math, general reasoning, and code generation benchmarks. |
| **Key Innovations** | Reasoning Transferability Coefficient for domain-agnostic reasoning measurement; Reasoning Evolution Reward for adaptive reasoning; multiplicative+additive advantage modulation; strong gains on competition-level math. |
| **Link** | [arXiv:2604.17696](https://arxiv.org/abs/2604.17696) |

---

### 5.5 Augmenting Game AI with Deep Reinforcement Learning

| Field | Detail |
|-------|--------|
| **Authors** | Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslén |
| **Institution** | — |
| **Abstract** | Envisions broader application of RL for game AI. Proposes a framework for training RL models suited towards game AI and game development. Presents examples of games with RL-augmented AI and describes practicalities of deploying player-facing ML agents. Identifies bottlenecks and promising research directions. |
| **Key Innovations** | Framework for game-development-suitable RL training; practical deployment considerations for player-facing ML agents; identification of industry adoption bottlenecks. |
| **Link** | [arXiv:2606.20210](https://arxiv.org/abs/2606.20210) |

---

### 5.6 NePPO: Near-Potential Policy Optimization for General-Sum MARL

| Field | Detail |
|-------|--------|
| **Authors** | Addison Kalanther, Sanika Bharvirkar, Shankar P. Sastry, Chinmay Maheshwari |
| **Institution** | — |
| **Abstract** | Learns a player-independent potential function whose Nash equilibrium approximates a Nash equilibrium of the original general-sum game. Uses zeroth-order gradient descent. Outperforms IPPO and MAPPO baselines in mixed cooperative-competitive environments. |
| **Key Innovations** | Markov Near-Potential Function framework for approximate Nash computation; zeroth-order optimization pipeline; tunable design handle via potential function parameterization. |
| **Link** | [arXiv:2603.06977](https://arxiv.org/abs/2603.06977) |

---

### 5.7 RQRE-OVI: Strategically Robust MARL with Linear Function Approximation

| Field | Detail |
|-------|--------|
| **Authors** | Jake Gonzales, Max Horwitz, Eric Mazumdar, Lillian J. Ratliff |
| **Institution** | — |
| **Abstract** | Proposes RQRE-OVI for computing Risk-Sensitive Quantal Response Equilibrium with linear function approximation. Establishes finite-sample regret bounds revealing tradeoff between rationality and risk sensitivity. RQRE policy map is Lipschitz continuous in estimated payoffs (unlike Nash). Demonstrates substantially more robust cross-play behavior. |
| **Key Innovations** | Risk-Sensitive QRE with formal regret guarantees; Lipschitz stability of equilibrium map; Pareto frontier between performance and robustness; distributional robustness interpretation. |
| **Link** | [arXiv:2603.09208](https://arxiv.org/abs/2603.09208) |

---

### 5.8 Game-Theory-Assisted RL for Border Defense

| Field | Detail |
|-------|--------|
| **Authors** | Goutam Das, Michael Dorothy, Kyle Volle, Daigo Shishika |
| **Institution** | — |
| **Abstract** | Hybrid approach leveraging game-theoretic insights to improve RL training. Uses Apollonius Circle to compute equilibrium in post-detection phase, enabling early termination of RL episodes. Yields 10-20% higher rewards, faster convergence, and more efficient search trajectories. |
| **Key Innovations** | Apollonius Circle-based early termination; game-theory-RL hybrid for training efficiency; optimal continuation guarantee after detection. |
| **Link** | [arXiv:2603.15907](https://arxiv.org/abs/2603.15907) |

---

## Summary Statistics

| Topic | Papers |
|-------|--------|
| LLMs | 7 |
| Recommendation Systems | 6 |
| CTR Prediction & Advertising | 8 |
| Sequential Modeling | 7 |
| Games, Game Theory & Multi-Agent | 8 |
| **Total** | **36** |
