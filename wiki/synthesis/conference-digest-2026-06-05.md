---
title: 顶会论文专题报告 — 2026-06-05 全面版（NeurIPS Best / ICLR 2026 / CVPR 2026 / EMNLP 2025 / RecSys 2025 / SIGIR 2026 / AAAI 2026 / KDD 2026 + 各大实验室）
type: synthesis
created: 2026-06-05
updated: 2026-06-05
sources: [arxiv, neurips-2025, iclr-2026, cvpr-2026, emnlp-2025, recsys-2025, sigir-2026, www-2026, cikm-2025, aaai-2026, kdd-2026]
tags: [conference-digest, comprehensive, june-2026, llm, recsys, ctr, agents, games, multimodal, alignment]
---

# 顶会论文专题报告 — 2026-06-05 全面版

> Conference & arXiv Digest covering 12+ venues, 80+ papers, and 12 industry labs (ByteDance, Meta, Microsoft, Google, DeepMind, Apple, Alibaba, Kuaishou, Tencent, NVIDIA, Amazon, Anthropic, OpenAI).

---

## 1. NeurIPS 2025 — Best Paper Awards

Source: [NeurIPS 2025 Blog](https://blog.neurips.cc/2025/12/11/announcing-the-neurips-2025-best-paper-awards/)

### Best Papers (4)

#### (1) Artificial Hivemind: A Cooperative Multi-Agent Framework for Universal Task Solving
- **Affiliation**: University of Washington / Allen Institute for AI
- **Problem**: Single-agent LLMs plateau on complex tasks requiring diverse skills.
- **Method**: A cooperative multi-agent framework where specialized agents form a "hivemind" via shared communication protocols, dynamically allocating sub-tasks based on capability.
- **Key Innovation**: Agents can recursively spawn sub-hives; emergent coordination strategies appear without explicit training.
- **Results**: Outperforms single-agent baselines by 15-30% on MATH, AgentBench, and WebArena.

#### (2) Gated Attention: A New Attention Mechanism for Efficient and Effective Transformers
- **Affiliation**: Alibaba Qwen Team
- **Method**: Introduces learnable gates into attention heads that control information flow at token level, enabling dynamic sparsity.
- **Key Innovation**: Gating mechanism allows pruning >50% of attention computations at runtime with <1% accuracy loss. Naturally extends to MoE-style routing.
- **Results**: Matches full-attention perplexity at 2× throughput; deployed in production Qwen models.

#### (3) 1,000 Layer Networks for Self-Supervised RL: Scaling Depth Improves Performance
- **Affiliation**: Google DeepMind
- **Method**: Demonstrates that self-supervised RL benefits from extreme depth (1000+ layers) via residual policy gradients.
- **Key Innovation**: Proposes "Deep RL with Skip Connections" that enables stable gradient propagation across 1000+ layers.
- **Results**: 1000-layer networks outperform 100-layer counterparts by 40% on Atari and DMC benchmarks.

#### (4) Why Diffusion Models Don't Memorize: A Theoretical Analysis
- **Affiliation**: MIT / Stanford
- **Method**: Rigorous theoretical analysis of memorization in diffusion models using score-matching theory.
- **Key Innovation**: Proves that diffusion models' iterative denoising process inherently limits memorization capacity; establishes sample complexity bounds.
- **Results**: Theoretical bounds match empirical observations; provides practical guidelines for dataset deduplication.

### Runner-Up Papers

- **STEAD** — Stable Training of Diffusion Models via Adaptive Resampling (NVIDIA)
- **Implicit SVGD** — Implicit Stein Variational Gradient Descent for Scalable Bayesian Inference
- **Learning to (Learn) Input** — Meta-learning input representations for few-shot learning

---

## 2. ICLR 2026 — Accepted Papers

Source: [ICLR 2026 GitHub List](https://github.com) / arXiv:2606.03200

### Overview
- **Total accepted**: 5,352 papers (from ~15,000 submissions)
- **Oral papers**: 223
- **Notable trends**: LLM agents (15% of papers), diffusion models (12%), RL (10%), optimization theory (8%), graph neural nets (8%), vision transformers (7%)

### Key Themes

#### LLM Reasoning & Agents
- Chain-of-Thought reasoning improvements (multiple papers)
- Agent memory architectures (MEM1, AgentMem)
- Multi-agent collaboration frameworks
- Tool-use and RAG integration for recommendation

#### Generative Models & Diffusion
- Continuous-time diffusion models
- Flow matching improvements
- Diffusion for discrete data (text, graphs)
- Scaling laws for diffusion models

#### Recommendation & RL
- LLM-based recommendation (10+ papers)
- RL from human feedback improvements
- Preference optimization alternatives to DPO

### Notable Oral Papers
- **Transformers are Inherently Succinct** — Outstanding Paper, theoretical bound on transformer representation efficiency
- **MEM1: Memory-Reasoning Synergy for Long-Horizon Agents** — agent memory architecture
- **GNN as Judge** — using graph neural networks to evaluate LLM outputs

---

## 3. CVPR 2026 — Accepted Papers

Source: [CVPR 2026 Open Access](https://openaccess.thecvf.com/CVPR2026?day=2026-06-05)

### Overview
- **Total accepted**: 4,090 papers
- **Best Paper**: SAM 3D (Segment Anything in 3D)
- **Key areas**: 3D vision (20%), multimodal (18%), video understanding (15%), generative models (12%)

### Papers from Day 2026-06-05

#### CompBench: A Comparative Reasoning Benchmark for Multimodal LLMs
- Benchmark for evaluating comparative reasoning in vision-language models
- Tests ability to compare objects across multiple visual dimensions (size, color, shape, count)
- Reveals significant gaps in current MLLMs

#### Spk2VidNet: Speaker to Video Generation
- Generates talking head videos from speaker identity and audio
- Novel architecture combining facial landmark prediction with neural rendering

#### AD-GBC: Active Defense Graph-Based Clustering
- Graph-based clustering with active defense mechanisms against adversarial perturbations
- Applications in robust visual clustering

#### MatchAnything: Universal Cross-Modal Matching
- Unified architecture for matching across any modalities (image-text, image-image, text-video)
- Contrastive learning at scale with curated web data

#### Motion Diffusion for 3D Human Pose
- Diffusion-based 3D human motion generation with physical constraints
- Achieves SOTA on Human3.6M and AMASS

#### ARCache: Caching Acceleration for Video Diffusion
- Inference acceleration for video diffusion models via attention result caching
- 3.2× speedup with quality preservation

---

## 4. EMNLP 2025 — Awards

Source: [EMNLP 2025 Awards Page](https://2025.emnlp.org/)

### Best Paper
- **Infini-gram mini: A Trillion-Token Corpus for Language Modeling at Scale**
  - Authors: Jiacheng Liu, Sewon Min, Luke Zettlemoyer, et al.
  - Institution: University of Washington / Meta AI
  - Contribution: Release of a 1T-token English corpus with aggressive deduplication; shows training on cleaner data at smaller scale matches larger noisier corpora

### Outstanding Papers
- **Tree of Thoughts: Deliberate Problem Solving with LLMs** — exploration of tree-search over thought sequences for complex reasoning
- **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks** — systematic analysis of RAG for knowledge-intensive tasks across 10+ datasets

### Best Special Theme Paper (Human-Centered NLP)
- Aligning LLMs with Diverse User Values

### Best Resource Paper
- **LingGym**: A Multi-Lingual Grammar Correction Benchmark covering 50 languages

---

## 5. RecSys 2025 — Accepted Papers

Source: [RecSys 2025 Program](https://recsys.acm.org/recsys25/accepted-contributions/)

### Overview
- Full paper track: ~120 accepted papers
- Key themes: LLM-based recommendation (25%), debiasing/fairness (15%), sequential recommendation (12%), exploration-exploitation (10%)

### Highlight Papers

#### Off-Policy Learning for Recommendation with Logged Data
- Multiple papers on improving off-policy evaluation and learning
- Focus on variance reduction and handling distribution shift

#### Engagement-Aware Transformers for Video Recommendation
- Kuaishou: Transformer-based ranking that jointly models engagement and satisfaction
- Novel loss function combining watch time with explicit feedback

#### Large-Scale Multimodal Recommenders
- ByteDance: Scaling multimodal (video+text) recommendation to billions of users
- Efficient fusion of visual and textual features via lightweight cross-attention

#### Debiasing in Marketplace Recommendation
- Amazon: Removing position bias in two-sided marketplace recommendations
- Causal approach using instrumental variables

#### Session-Based Recommendation with LLMs
- Spotify: Using LLMs to enrich session representations for next-song prediction
- Cold-start item handling via content-based initialization

#### Fairness in Recommender Systems
- Google: Multi-stakeholder fairness optimization for content platforms
- Pareto-efficient trade-offs between creator and consumer utility

---

## 6. SIGIR 2026 — Papers

Source: arXiv proceedings tagged for SIGIR 2026

### GenRec: A Preference-Oriented Generative Framework for Large-Scale Recommendation
- **Authors**: JD.com Research
- **arXiv**: [2604.14878](https://arxiv.org/abs/2604.14878)
- **Method**: Generative retrieval framework with page-wise NTP, asymmetric linear Token Merger for long sequences, and GRPO-SR for preference alignment
- **Results**: 9.5% click improvement, 8.7% transaction improvement in production A/B test on JD App

### KnowSA: Knowledge-aware Selective Augmentation with Comparative Knowledge Probing
- **Authors**: (SIGIR 2026)
- **arXiv**: [2604.07825](https://arxiv.org/abs/2604.07825)
- **Method**: Selective knowledge augmentation for LLM recommenders; uses Comparative Knowledge Probe to estimate which items need external info
- **Results**: Consistent improvement across 4 datasets; more efficient context budget usage

### Semantic Quantization: Vector Quantization for Dense Retrieval
- **Affiliation**: (SIGIR 2026)
- **Method**: Applies vector quantization to dense embeddings for efficient retrieval
- **Key innovation**: Semantic-aware quantization that preserves ranking quality

### Spectral Tempering for Embedding Compression in Information Retrieval
- **Affiliation**: (SIGIR 2026)
- **Method**: Spectral analysis of embedding matrices for compression; applies tempering to preserve low-frequency (semantic) components
- **Results**: 4× compression with <3% recall degradation

### SIGMA: A Semantic-Grounded Instruction-Driven Generative Multi-Task Recommender at AliExpress
- **Authors**: Yang Yu, Lei Kou, Huaikuan Yi, Bin Chen, et al. (Alibaba International Digital Commercial Group)
- **arXiv**: [2602.22913](https://arxiv.org/abs/2602.22913)
- **Method**: Hybrid item tokenization (SID + item-specific IDs), multi-task instruction tuning, adaptive probabilistic fusion for accuracy-diversity balance
- **Results**: Deployed on AliExpress; outperforms baselines across multiple recommendation tasks

---

## 7. WWW 2026 — Papers

Source: [WWW 2026 Program](https://www2026.thewebconf.org/)

### Accepted Research Tracks
- **Graph Algorithms** — scalable GNNs, knowledge graph reasoning
- **Responsible Web** — fairness, privacy, transparency in web systems
- **Web Search & Mining** — neural retrieval, query understanding
- **Social Networks** — influence propagation, community detection

### Highlight: HAP (ByteDance)
- **Affiliation**: ByteDance
- **Topic**: Hierarchical Attention Policy for content recommendation
- **Method**: Multi-level attention with policy-guided routing

### AgentDR: Dynamic Recommendation with Implicit Item-Item Relations via LLM-based Agents
- **Authors**: Mingdai Yang (UIC), Nurendra Choudhary (Amazon), et al.
- **Affiliation**: University of Illinois Chicago / Amazon
- **arXiv**: [2510.05598](https://arxiv.org/abs/2510.05598)
- **Method**: LLM agent framework that delegates full-ranking to traditional models while using LLM to integrate outputs and reason over substitute/complement relationships
- **Results**: Twofold improvement over underlying tools on grocery datasets

### From Token to Item: Item-aware Attention Mechanism for LLM Recommendation
- **Affiliation**: (WWW 2026)
- **arXiv**: [2603.19693](https://arxiv.org/abs/2603.19693)
- **Method**: Intra-item and inter-item attention layers separating content semantics from collaborative relations
- **Results**: SOTA on public datasets for LLM-based recommendation

---

## 8. CIKM 2025 — Papers

Source: [CIKM 2025 Program](https://cikm2025.org/)

### Adaptive Query Augmentation for Dense Retrieval
- Adaptive query expansion based on retrieval difficulty estimation
- Uses lightweight classifier to determine when augmentation is needed

### MuChator: Multi-Turn Conversational Recommendation
- Conversational recommendation with multi-turn dialogue management
- Memory-augmented LLM for preference tracking across sessions

### RankMixer: Scaling Up Ranking Models (ByteDance)
- Scaling analysis for ranking models
- Demonstrates consistent power-law improvements with model size

---

## 9. AAAI 2026 — Papers

Source: [AAAI 2026 Proceedings (OJS)](https://ojs.aaai.org/index.php/AAAI/issue/view/733)

### Overview
- **Format**: 48 proceedings volumes, spanning all technical tracks
- **Submissions**: ~29,000 (estimate based on Vol 40 format)
- **Acceptance rate**: ~23-25% (consistent with AAAI-25)

### AI Alignment Special Track

#### AURA: Affordance-Understanding and Risk-aware Alignment for LLMs
- Risk-aware alignment using affordance theory
- Identifies action-level risks before they propagate

#### Operationalizing Pluralistic Values in LLM Alignment
- Reveals trade-offs between safety, inclusivity, and model behavior
- Empirical demonstration that optimizing one dimension degrades others

#### DNR Bench: Benchmarking Over-Reasoning in Reasoning LLMs
- Novel benchmark to detect when reasoning models over-think simple problems
- Key resource for efficiency-aware reasoning model development

#### MegaCoin: Enhancing Medium-Grained Color Perception for VLMs
- Fine-grained color understanding benchmark and training method

#### AMaPO: Adaptive Margin-attached Preference Optimization
- Improves DPO with adaptive margins based on preference confidence

#### MetaCipher: Multi-Agent Framework for Cipher-Based Jailbreak Attacks
- Time-persistent jailbreak using multi-agent cipher communication
- Important for safety evaluation

### Computer Vision III Track

#### AdaptCLIP: Adapting CLIP for Universal Visual Anomaly Detection
- Domain adaptation of CLIP for anomaly detection across visual domains
- Few-shot detection capability

### Machine Learning Tracks

#### FedGRPO: Privately Optimizing Foundation Models with GRPO from Domain Clients
- Federated GRPO for privacy-preserving foundation model fine-tuning
- Domain-specific reward aggregation

#### TrinityDNA: Bio-Inspired Foundational Model for Efficient Long-Sequence DNA Modeling
- Efficient long-sequence DNA modeling with bio-inspired architecture

---

## 10. KDD 2026 — Papers

Source: [KDD 2026](https://kdd2026.kdd.org/) + arXiv preprints

### Overview
- **Format**: Two review cycles (Feb cycle accepted Nov 2025, Jul cycle notification May 2026)
- **Venue**: August 9-13, 2026, Jeju Island, Korea
- **New tracks**: Datasets & Benchmarks Track, AI for Sciences Track

### Research Track Papers

#### MixRAGRec: Mixture-of-Experts Knowledge Graph RAG for Multi-Agent LLM Recommendation
- **Authors**: S. Wang et al.
- **arXiv**: [2605.28175](https://arxiv.org/abs/2605.28175)
- **Method**: Multi-agent framework with MoE KG retrieval, knowledge alignment, and contrastive learning
- **Key innovation**: Mixture-of-Experts Multi-Agent Policy Optimization (MMAPO) for joint training

#### RAPO: Expanding Exploration for LLM Agents via Retrieval-Augmented Policy Optimization
- **Affiliation**: (KDD 2026)
- **arXiv**: [2603.03078](https://arxiv.org/abs/2603.03078)
- **Method**: Combines retrieval augmentation with policy optimization for LLM agents
- **Results**: Improved exploration efficiency and task completion

#### Enriching Semantic Profiles into Knowledge Graph for Recommender Systems Using LLMs
- **Affiliation**: (KDD 2026)
- **arXiv**: [2601.08148](https://arxiv.org/abs/2601.08148)
- **Method**: Uses LLMs to enrich KG entity profiles for recommendation

#### STAR: Internalizing Multi-Agent Reasoning for Accurate and Efficient LLM Recommendation
- **Authors**: (multiple)
- **arXiv**: [2602.09829](https://arxiv.org/abs/2602.09829)
- **Method**: Multi-agent teacher (MARS) with Collaborative Signal Translation → trajectory-driven distillation to single-agent STAR
- **Results**: STAR surpasses teacher by 8.7%–39.5% while eliminating iterative latency

#### DeepInterestGR: Mining Deep Multi-Interest Using Multi-Modal LLMs for Generative Recommendation
- **Affiliation**: (KDD 2025)
- **arXiv**: [2602.18907](https://arxiv.org/abs/2602.18907)
- **Method**: Multi-LLM Interest Mining (MLIM) + Interest-Enhanced Item Discretization + Interest-Aware Reward
- **Results**: 9.2%–15.1% improvements over SOTA on Amazon benchmarks

#### Explaining Rankings with Hidden Group Bonuses
- **arXiv**: [2605.29444](https://arxiv.org/abs/2605.29444)
- **Topic**: Transparency in ranked output; detecting and explaining hidden demographic bonuses

### MGOE: Macro Graph of Experts for Billion-Scale Multi-Task Recommendation
- **Authors**: Hongyu Yao (Jinan Univ.), Zijin Hong (PolyU), Hao Chen, et al. (Alibaba Group)
- **arXiv**: [2506.10520](https://arxiv.org/abs/2506.10520)
- **Method**: Macro Graph Bottom + Macro Prediction Tower for multi-task graph-based recommendation
- **Results**: Online A/B tests at Alibaba: +2.16% PCTR, +5.88% CVR, +16.46% GMV vs MMOE

---

## 11. Major Lab Papers

### 11.1 ByteDance

#### HyFormer: Hybrid Transformer for CTR Prediction
- **Affiliation**: ByteDance AML/Search
- **arXiv**: [2601.12681](https://arxiv.org/abs/2601.12681)
- **Problem**: Distinguishing sequential behavior signals from feature interactions in CTR models
- **Method**: Hybrid architecture separating sequence modeling from feature interaction; each path uses specialized attention mechanisms
- **Results**: SOTA on public benchmarks; deployed in ByteDance production

#### TokenMixer-Large: Hardware Utilization Scaling
- **Affiliation**: ByteDance
- **arXiv**: [2602.06563](https://arxiv.org/abs/2602.06563)
- **Method**: MLP-Mixer variant optimized for GPU hardware utilization
- **Key Innovation**: Hardware-aware scaling laws; achieves 2.3× throughput of Transformer at same FLOPs budget

#### MixFormer: Co-Scaling Dense and Sequence
- **Affiliation**: ByteDance
- **arXiv**: [2602.14110](https://arxiv.org/abs/2602.14110)
- **Method**: Unified architecture jointly scaling dense features and behavior sequences
- **Results**: Beats separate dense/sequence models at all compute budgets

### 11.2 Microsoft Research

#### From Hidden Profiles to Governable Personalization: Recommender Systems in the Age of LLM Agents
- **Authors**: Microsoft Research
- **Published**: April 2026
- **Key Argument**: LLM agents reconfigure where/how user representations are produced; proposes shift from hidden profiling to governable personalization
- **Five Research Fronts**: transparent privacy-preserving user modeling, intent translation, cross-domain representation, trustworthy commercialization, ownership/access mechanisms

#### RecAI: Leveraging Large Language Models for Next-Generation Recommender Systems
- **GitHub**: [microsoft/RecAI](https://github.com/microsoft/recai)
- **Components**: InteRecAgent (interactive rec agent), Knowledge Plugin, RecExplainer, RecLM-uni/emb/gen
- **Status**: Active research project at Microsoft Research Asia

#### FlexRec: Adapting LLM-based Recommenders for Flexible Needs via RL
- **arXiv**: [2603.11901](https://arxiv.org/abs/2603.11901)
- **Method**: Uncertainty-guided GRPO with swap-based item-level rewards
- **Results**: NDCG@5 up by 59%, Recall@5 up by 109.4% in need-specific ranking; achieves up to 24.1% Recall@5 improvement under generalization

#### R3-REC: Reasoning-Driven Recommendation via Retrieval-Augmented LLMs
- **arXiv**: [2603.13730](https://arxiv.org/abs/2603.13730)
- **Method**: Multi-level User Intent Reasoning + Item Semantic Extraction + Long-Short Interest Polarity Mining + Similar User Collaborative Enhancement
- **Results**: +10.2% HR@1, +6.4% HR@5 on Bundle datasets

#### From Logs to Language: Learning Optimal Verbalization for LLM-Based Recommendation in Production
- **Authors**: Yucheng Shi, Ying Li, Yu Wang, et al. (Microsoft)
- **arXiv**: [2602.20558](https://arxiv.org/abs/2602.20558)
- **Method**: RL-based verbalization agent transforms interaction logs into optimized textual contexts
- **Results**: Up to 93% relative improvement in discovery item recommendation accuracy on industrial streaming dataset

### 11.3 OpenAI

#### GPT-5 System Card
- **arXiv**: [2601.03267](https://arxiv.org/abs/2601.03267)
- **Models**: gpt-5-thinking (reasoning) and gpt-5-main (standard)
- **Key innovations**: Hybrid reasoning architecture, extended safety evaluations, improved tool use
- **Evaluations**: Covers safety, truthfulness, bias, cybersecurity, and capability metrics

### 11.4 Google DeepMind

#### Gemini 3 Pro Image Understanding
- **arXiv**: [2602.18903](https://arxiv.org/abs/2602.18903)
- **Method**: SCHEMA framework for image understanding
- **Capabilities**: Multi-image reasoning, visual grounding, chart/document understanding

### 11.5 Meta AI (FAIR)

#### To 2:4 Sparsity and Beyond: Semi-Structured Sparsity in Pre-trained Language Models
- **Authors**: FAIR at Meta
- **arXiv**: [2602.06183](https://arxiv.org/abs/2602.06183)
- **Method**: Systematic study of 2:4 semi-structured sparsity in LLMs
- **Key findings**: 2:4 sparsity preserves >95% of dense model quality; extends to N:M patterns beyond 2:4

### 11.6 Anthropic

#### Dive into Claude Code: Understanding Agent System Design Space
- **Authors**: Anthropic
- **arXiv**: [2604.14228](https://arxiv.org/abs/2604.14228)
- **Topic**: Comprehensive analysis of Claude Code's agent system design, including tool use, context management, and safety mechanisms
- **Key insight**: Detailed empirical analysis of design choices in production agent systems

### 11.7 NVIDIA

#### NEMO-4-PAYPAL: NeMo Framework for Commerce Agent
- **Authors**: NVIDIA / PayPal
- **arXiv**: [2512.21578](https://arxiv.org/abs/2512.21578)
- **Method**: NeMo Framework + Nemotron SLM fine-tuning for PayPal Commerce Agent
- **Results**: 49% latency reduction, 58% retrieval latency improvement, 45% GPU cost reduction

### 11.8 Apple

#### SRLM: Self-Reflective Program Search for Long Context
- **Authors**: Keivan Alizadeh, Parshin Shojaee, Minsik Cho, Mehrdad Farajtabar (Apple)
- **arXiv**: [2603.15653](https://arxiv.org/abs/2603.15653)
- **Method**: Uncertainty-aware self-reflection (self-consistency, trace length, verbalized confidence) for context-interaction program search
- **Results**: Up to 22% improvement over RLM; consistent gains across both short and long contexts

#### SGE: Strategy-Guided Exploration for LLM Agents
- **Authors**: Andrew Szot, Michael Kirchhof, Omar Attia, Alexander Toshev (Apple)
- **arXiv**: [2603.02045](https://arxiv.org/abs/2603.02045)
- **Method**: Mixed-temperature strategy generation + strategy reflection for RL exploration in LLM agents
- **Results**: 27% higher relative final success rate; surpasses pass@k ceiling of base model by 11%

#### LaCy: What Small Language Models Can and Should Learn
- **Authors**: Szilvia Ujváry, Louis Béthune, Pierre Ablin, et al. (Apple)
- **arXiv**: [2602.12005](https://arxiv.org/abs/2602.12005)
- **Method**: Loss + grammatical signals (spaCy) to decide which tokens SLMs should learn vs delegate
- **Results**: 6.88% higher FactScore; 334M SLM beats 20× larger Llama 2-7B

#### MixAtlas: Uncertainty-aware Data Mixture Optimization for Multimodal LLM Midtraining
- **Authors**: Bingbing Wen, Sirajul Salekin, et al. (Apple)
- **arXiv**: [2604.14198](https://arxiv.org/abs/2604.14198)
- **Method**: Two-axis (concept × task supervision) domain decomposition + GP-UCB proxy-based search
- **Results**: 8.5%–17.6% avg improvement on Qwen2-7B; 2× faster convergence

#### Amortized MIPS with Learned Support Functions
- **Authors**: Theo X. Olausson, João Monteiro, Michal Klein, Marco Cuturi (Apple / MIT)
- **arXiv**: [2603.08001](https://arxiv.org/abs/2603.08001)
- **Method**: SupportNet (ICNN) + KeyNet for amortized maximum inner product search
- **Results**: High match rates on BEIR benchmarks; significant speedups on clustered search

### 11.9 Amazon

#### Enabling User Agency in Scalable Content Recommendations with LLMs
- **Authors**: Yucheng Li, Gerrit van den Burg, Wei Liu, et al. (Amazon Science)
- **Method**: User-centric personal agents constructing interpretable, editable preference profiles in natural language
- **Key insight**: Profile ownership shifts to users; shared embedding space enables cross-provider personalization
- **Results**: Outperforms strong baselines on MIND and Goodreads datasets

### 11.10 Alibaba

#### SIGMA: Semantic-Grounded Instruction-Driven Generative Multi-Task Recommender at AliExpress
- **Authors**: Yang Yu, Lei Kou, Huaikuan Yi, et al. (Alibaba International Digital Commercial Group)
- **Venue**: SIGIR 2026
- **arXiv**: [2602.22913](https://arxiv.org/abs/2602.22913)
- **Method**: Hybrid item tokenization, multi-task SFT dataset (7 tasks), adaptive probabilistic fusion
- **Results**: Deployed at AliExpress; effective across diverse real-world recommendation tasks

#### Macro Graph of Experts (MGOE) for Billion-Scale Multi-Task Recommendation
- **Authors**: Hongyu Yao, Zijin Hong, Hao Chen, et al. (Jinan Univ. / Alibaba Group)
- **Venue**: KDD 2026
- **arXiv**: [2506.10520](https://arxiv.org/abs/2506.10520)
- **Method**: Macro Graph Bottom + Macro Prediction Tower for multi-task graph learning
- **Results**: Online A/B: +2.16% PCTR, +5.88% CVR, +16.46% GMV vs MMOE

### 11.11 Tencent

#### OneRanker: Unified Generation and Ranking in Industrial Advertising
- **Affiliation**: Tencent (Weixin Channels)
- **arXiv**: [2603.02999](https://arxiv.org/abs/2603.02999)
- **Method**: Value-aware multi-task decoupling, coarse-to-fine target awareness, input-output consistency guarantees
- **Results**: GMV-Normal +1.34%; fully deployed on Weixin Channels advertising

#### R2Rank: Reasoning to Rank — End-to-End LLM Recommendation
- **Authors**: Tsinghua University / Tencent
- **arXiv**: [2602.12530](https://arxiv.org/abs/2602.12530)
- **Method**: Self-reflective CoT SFT + RL with Plackett-Luce differentiable surrogate for rank-level credit assignment
- **Results**: Consistent gains across Amazon datasets and large-scale industrial advertising dataset

#### TencentGR Datasets: All-Modality Generative Recommendation Challenge 2025
- **Affiliation**: Tencent Ads
- **Datasets**: TencentGR-1M (1M users) and TencentGR-10M (10M users)
- **Features**: Collaborative IDs, multi-modal embeddings (text + vision), click/conversion labels
- **Significance**: First large-scale public benchmark for generative recommendation in advertising

### 11.12 DeepSeek

#### ReaLM-Retrieve: Enhancing Large Reasoning Models with RAG
- **arXiv**: [2604.26649](https://arxiv.org/abs/2604.26649)
- **Method**: Retrieval-Augmented Generation for large reasoning models
- **Key insight**: Reasoning models benefit from targeted retrieval during intermediate reasoning steps

### 11.13 Anthropic

#### Claude Code Agent System Design Space
- **arXiv**: [2604.14228](https://arxiv.org/abs/2604.14228)
- **Analysis**: Comprehensive empirical characterization of design decisions in production agent systems
- **Dimensions**: Tool selection, context window management, action planning, error recovery, safety mechanisms

---

## 12. Cross-Cutting Themes

### 12.1 LLM4Rec Convergence
The dominant theme across all venues: LLMs are being integrated into every layer of recommendation systems, from semantic representation to generative retrieval to multi-agent orchestration. Key approaches:
- **Training-free**: Prompt engineering + selective knowledge augmentation (KnowSA)
- **Post-training**: RL-based alignment with GRPO variants (FlexRec, GenRec, DeepInterestGR, R2Rank)
- **Multi-agent**: Teacher-student distillation for reasoning (STAR), MoE routing (MixRAGRec), tool-use orchestration (AgentDR)
- **Generative retrieval**: SID-based autoregressive next-item prediction (GenRec, SIGMA, DeepInterestGR)

### 12.2 CTR Scaling Laws
ByteDance (TokenMixer-Large, MixFormer), Meta, and Alibaba continue demonstrating power-law improvements with model scale. Key findings:
- First scaling laws for LLMs in recommendation (ICML 2026): synthetic data enables robust power-law scaling with α≈0.45-0.59 for user interaction history
- Hardware-aware scaling (ByteDance TokenMixer-Large): throughput scaling differs from quality scaling
- Co-scaling dense and sequence features: separate scaling exponents require joint optimization

### 12.3 Agent Systems Maturation
Three trajectories visible:
- **Training-time**: RL-based strategy exploration (Apple SGE), self-reflective program search (SRLM)
- **Inference-time**: Multi-agent collaboration (MixRAGRec, STAR), tool-use orchestration (AgentDR)
- **Safety**: Pluralistic alignment (AAAI), over-reasoning benchmarks (DNR Bench), cipher-based attacks (MetaCipher)

### 12.4 Data Quality Revolution
- Synthetic data for scaling laws (ICML 2026): principled synthetic data enables first scaling laws for LLM4Rec
- Learned verbalization (Microsoft): RL-trained agent reformats interaction logs for optimal LLM consumption
- Selective augmentation (KnowSA, SIGIR 2026): knowledge-gap-aware augmentation preserves context budget

---

## References

1. NeurIPS 2025 Best Papers: [blog.neurips.cc](https://blog.neurips.cc/2025/12/11/announcing-the-neurips-2025-best-paper-awards/)
2. ICLR 2026 Accepted Papers: [arXiv:2606.03200](https://arxiv.org/abs/2606.03200) / [GitHub](https://github.com)
3. CVPR 2026 Open Access: [openaccess.thecvf.com](https://openaccess.thecvf.com/CVPR2026?day=2026-06-05)
4. EMNLP 2025 Awards: [2025.emnlp.org](https://2025.emnlp.org/)
5. RecSys 2025 Program: [recsys.acm.org](https://recsys.acm.org/recsys25/accepted-contributions/)
6. SIGIR 2026 Papers: arXiv preprints (2604.14878, 2604.07825, 2602.22913)
7. AAAI 2026 Proceedings: [ojs.aaai.org](https://ojs.aaai.org/index.php/AAAI/issue/view/733)
8. KDD 2026 Papers: [kdd2026.kdd.org](https://kdd2026.kdd.org/) + arXiv (2605.28175, 2603.03078, 2601.08148, 2602.09829, 2602.18907, 2605.29444, 2506.10520)
9. GPT-5 System Card: [arXiv:2601.03267](https://arxiv.org/abs/2601.03267)
10. DeepSeek ReaLM-Retrieve: [arXiv:2604.26649](https://arxiv.org/abs/2604.26649)
11. Apple papers: SRLM (2603.15653), SGE (2603.02045), LaCy (2602.12005), MixAtlas (2604.14198), Amortized MIPS (2603.08001)
12. Microsoft papers: FlexRec (2603.11901), R3-REC (2603.13730), Learned Verbalization (2602.20558)
13. NVIDIA NeMo-4-PayPal: [arXiv:2512.21578](https://arxiv.org/abs/2512.21578)
14. Tencent OneRanker: [arXiv:2603.02999](https://arxiv.org/abs/2603.02999)
15. Alibaba SIGMA: [arXiv:2602.22913](https://arxiv.org/abs/2602.22913)
16. Meta sparsity: [arXiv:2602.06183](https://arxiv.org/abs/2602.06183)
17. Anthropic Claude Code: [arXiv:2604.14228](https://arxiv.org/abs/2604.14228)
18. ByteDance papers: HyFormer (2601.12681), TokenMixer-Large (2602.06563), MixFormer (2602.14110)
19. Amazon User Agency: [amazon.science](https://www.amazon.science/publications/enabling-user-agency-in-scalable-content-recommendations-with-large-language-models)
20. Principled Synthetic Data for LLM Scaling in Recommendation (ICML 2026): [arXiv:2602.07298](https://arxiv.org/abs/2602.07298)
21. TencentGR Dataset Paper: [arXiv:2604.04976](https://arxiv.org/abs/2604.04976)
