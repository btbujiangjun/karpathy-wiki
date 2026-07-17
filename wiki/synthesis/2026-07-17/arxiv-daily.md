---
title: arXiv Daily — 2026-07-17
type: synthesis
created: 2026-07-17
updated: 2026-07-17
tags: [arxiv, daily, llm, recommendation, ctr, sequential-modeling, games, advertising]
---

# arXiv Daily Digest — 2026-07-17

Curated selection of recent arXiv papers across LLMs, recommendation systems, CTR prediction, sequential modeling, games, and computational advertising.

---

## LLMs & Reasoning

### 1. LoRA is All You Need for Safety Alignment of Reasoning LLMs

| Field | Details |
|-------|---------|
| **Authors** | (Multiple authors) |
| **Institution** | Not specified in abstract |
| **arXiv** | [2507.17075](https://arxiv.org/abs/2507.17075v1) |

**Abstract:** Reasoning LLMs demonstrate remarkable breakthroughs but safety alignment fine-tuning degrades reasoning abilities (the "Safety Tax"). This work shows that using LoRA for SFT on refusal datasets effectively aligns the model for safety without harming reasoning. Restricting safety weight updates to a low-rank space minimizes interference with reasoning weights. Experiments on DeepSeek-R1-Distill-Qwen-7B and 14B across AIME, GPQA, HumanEval, and MBPP show safety comparable to full fine-tuning while preserving reasoning.

**Key Innovations:**
- LoRA-based safety alignment achieves full-model-level safety without reasoning degradation
- Low-rank updates are more orthogonal to reasoning weights than full-model updates
- Validated across math, science, and coding benchmarks (7B and 14B models)

---

### 2. Post-Training LLMs via Reinforcement Learning from Self-Feedback (RLSF)

| Field | Details |
|-------|---------|
| **Authors** | (Multiple authors) |
| **Institution** | Not specified in abstract |
| **arXiv** | [2507.21931](https://arxiv.org/abs/2507.21931v1) |

**Abstract:** LLMs often produce plausible but poorly-calibrated answers. RLSF uses the model's own confidence as an intrinsic reward, mimicking human learning without external feedback. After a frozen LLM generates chain-of-thought solutions, confidence of each answer span is computed to rank traces. These synthetic preferences fine-tune the policy via standard preference optimization. RLSF simultaneously refines calibration and strengthens step-by-step reasoning.

**Key Innovations:**
- Intrinsic reward based on model's own confidence for post-training
- No human labels, gold answers, or externally curated rewards required
- Improves both calibration and reasoning accuracy on arithmetic and MCQ tasks
- RLSF + PPO outperforms DPO, showing RL is well-suited for intrinsic motivation

---

### 3. Open-Source LLMs Collaboration Beats Closed-Source LLMs: SMACS

| Field | Details |
|-------|---------|
| **Authors** | (Multiple authors) |
| **Institution** | Not specified in abstract |
| **arXiv** | [2507.14200](https://arxiv.org/abs/2507.14200v1) |

**Abstract:** Proposes SMACS (Scalable Multi-Agent Collaboration System) that integrates 15 open-source LLMs to outperform leading closed-source models. Uses Retrieval-based Prior Selection (RPS) to assign proxy performance scores and select Top-k LLMs per instance, plus Exploration-Exploitation-Driven Posterior Enhancement (EPE) for diverse response generation and selection. SMACS surpasses Claude-3.7-Sonnet (+12.73%), GPT-4.1 (+5.36%), and GPT-o3-mini (+5.28%).

**Key Innovations:**
- Retrieval-based Prior Selection for instance-level LLM routing
- Exploration-Exploitation-Driven Posterior Enhancement with hybrid scoring
- Demonstrates open-source collectives can exceed closed-source performance ceilings
- Scalable: performance improves monotonically as more LLMs are added

---

### 4. Promptomatix: Automatic Prompt Optimization Framework

| Field | Details |
|-------|---------|
| **Authors** | (Multiple authors) |
| **Institution** | Not specified in abstract |
| **arXiv** | [2507.14241](https://arxiv.org/abs/2507.14241v1) |

**Abstract:** Zero-configuration framework that transforms natural language task descriptions into high-quality prompts. Supports both lightweight meta-prompt optimizer and DSPy-powered compiler. Analyzes user intent, generates synthetic training data, selects prompting strategies, and refines prompts using cost-aware objectives. Evaluated across 5 task categories with competitive or superior performance vs. existing libraries.

**Key Innovations:**
- Zero-config prompt optimization pipeline from intent analysis to evaluation
- Intelligent synthetic data generation eliminating data bottlenecks
- Cost-aware optimization enabling user-controlled quality-efficiency trade-offs
- Framework-agnostic: supports DSPy, AdalFlow, and meta-prompt backends

---

### 5. Beyond Context Limits: Subconscious Threads (TIM + TIMRUN)

| Field | Details |
|-------|---------|
| **Authors** | Philip Schroeder, Nathaniel W. Morgan, Hongyin Luo, James R. Glass et al. |
| **Institution** | MIT / Subconscious Systems |
| **arXiv** | [2507.16784](https://arxiv.org/abs/2507.16784v1) |

**Abstract:** Introduces TIM (Thread Inference Model), an LLM trained for recursive decompositional problem solving, and TIMRUN, an inference runtime enabling unlimited working memory via structured reasoning trees. Models language as reasoning trees measured by length and depth instead of linear sequences. TIMRUN maintains only relevant KV states via rule-based subtask-pruning, supporting 30+ tool calls in a single inference. TIM-large outperforms GPT-4o on BrowseComp and matches ReACT agents built on DeepSeek R1.

**Key Innovations:**
- Recursive task decomposition with structured JSON reasoning trajectories
- Subtask pruning for efficient KV cache management (up to 90% manipulation)
- Linear complexity per step enabling unlimited context within single inference
- No agent framework needed — model self-manages context

---

### 6. The Wall Confronting Large Language Models

| Field | Details |
|-------|---------|
| **Authors** | (Multiple authors) |
| **Institution** | Not specified in abstract |
| **arXiv** | [2507.19703](https://arxiv.org/abs/2507.19703v2) |

**Abstract:** Argues that scaling laws severely limit LLM ability to improve prediction uncertainty, making scientific-grade reliability intractable. The mechanism generating non-Gaussian outputs from Gaussian inputs may be the root of error pileup. Low scaling exponents indicate diminishing returns, compounded by spurious correlations increasing with data size. Proposes that avoiding "Degenerative AI" necessitates prioritizing insight and structural understanding over brute-force scaling.

**Key Innovations:**
- Theoretical analysis of scaling law limitations for LLM reliability
- Connection between low scaling exponents and non-Gaussian uncertainty
- "Degenerative AI" framework: error accumulation pathway in LLMs
- Argument for structural understanding over brute-force scaling

---

### 7. Scalpel vs. Hammer: GRPO Amplifies, SFT Replaces

| Field | Details |
|-------|---------|
| **Authors** | (Multiple authors) |
| **Institution** | Not specified in abstract |
| **arXiv** | [2507.10616](https://arxiv.org/abs/2507.10616v1) |

**Abstract:** Comparative analysis of GRPO (RL) and SFT for reasoning training. RL yields minor in-domain maths gains with slight MMLU degradation; SFT shows more pronounced in-domain gains but greater out-of-domain degradation. Both modify query/key weights most, but SFT additionally affects mid-layer MLPs, potentially causing knowledge degradation. Investigates freezing model parts during training with inconclusive results.

**Key Innovations:**
- Controlled comparison of GRPO vs. SFT on identical problems/model
- Parameter-level analysis showing SFT modifies more weights than GRPO
- Hypothesis: mid-layer MLP disruption causes SFT's out-of-domain degradation
- Preliminary evidence that RL "amplifies" while SFT "replaces" capabilities

---

## CTR Prediction & Recommendation

### 8. Field-Aware Transformer (FAT) for CTR Prediction

| Field | Details |
|-------|---------|
| **Authors** | (Multiple authors — Taobao/Ant Group) |
| **Institution** | Alibaba / Taobao |
| **arXiv** | [2511.12081](https://arxiv.org/abs/2511.12081v2) |

**Abstract:** Identifies that Transformers for CTR suffer diminishing returns due to structural misalignment — standard Transformers assume sequential compositionality while CTR data requires combinatorial reasoning over heterogeneous fields. FAT introduces Field-Decomposed Attention with field-aware parameters and Basis-Composed Hypernetwork. Theoretical scaling law based on Rademacher complexity. Achieves up to +4.38% AUC improvement offline; +2.33% CTR and +0.66% RPM in live Taobao production.

**Key Innovations:**
- Field-aware Transformer architecture aligned with CTR data semantics
- Scaling law showing generalization depends on field interactions, not vocabulary size
- Basis-Composed Hypernetwork reducing parameter complexity
- Validated on Taobao sponsored search (+2.33% CTR, +0.66% RPM)

---

### 9. MARS: Modality-Aligned Retrieval for Sequence Augmented CTR

| Field | Details |
|-------|---------|
| **Authors** | (Multiple authors — Kuaishou) |
| **Institution** | Kuaishou |
| **arXiv** | [2509.01184](https://arxiv.org/abs/2509.01184v1) |

**Abstract:** Addresses interaction sparsity for low-active users in CTR prediction. Uses Stein kernel-based method to align text and image features into unified semantic space for multimodal user embeddings. Retrieves, filters, and concentrates similar behavior sequences from high-active users. Deployed at Kuaishou serving hundreds of millions of users, with significant growth on core business metrics.

**Key Innovations:**
- Stein kernel-based multimodal alignment for user representation
- Cross-user behavior sequence augmentation via multimodal similarity
- Successful large-scale deployment at Kuaishou (hundreds of millions of users)
- Addresses low-active user scenario specifically

---

### 10. DiffuMIN: Diffusion-driven Multi-interest Network for CTR

| Field | Details |
|-------|---------|
| **Authors** | Weijiang Lai et al. |
| **Institution** | Not specified in abstract |
| **arXiv** | [2508.15311](https://arxiv.org/abs/2508.15311v1) |

**Abstract:** Two-stage model for long-term behavior modeling in CTR. Stage 1: target-oriented multi-interest extraction via orthogonal decomposition of target embeddings into interest channels. Stage 2: diffusion module guided by contextual interests generates augmented interests aligned with user interest latent spaces. Contrastive learning ensures generated interests match genuine preferences. Online A/B testing shows +1.52% CTR and +1.10% CPM.

**Key Innovations:**
- First application of diffusion modeling to user interests in CTR prediction
- Orthogonal multi-interest extraction with target-aware decomposition
- Contextual and channel-guided diffusion for personalized interest generation
- Contrastive calibration ensuring alignment with genuine preferences

---

### 11. Diff-MSIN: Diffusion-based Multi-modal Synergy Interest Network

| Field | Details |
|-------|---------|
| **Authors** | (Multiple authors) |
| **Institution** | Not specified in abstract |
| **arXiv** | [2508.21460](https://arxiv.org/abs/2508.21460v1) |

**Abstract:** Addresses limitations of ID-only CTR models by introducing multi-modal features. Three modules: MFE (Multi-modal Feature Enhancement) extracts common/special info across modalities using PLE-inspired expert networks; SRC (Synergistic Relationship Capture) uses diffusion for multi-step synergistic feature interaction; FDAF (Feature Dynamic Adaptive Fusion) reduces noise via attention-based fusion. Achieves at least 1.67% improvement on Rec-Tmall and Amazon datasets.

**Key Innovations:**
- Disentangles common, special, and synergistic information across modalities
- Diffusion-based multi-step cross-modal interaction modeling
- Knowledge Decoupling method for feature distinctiveness
- Adaptive fusion reducing multi-modal noise

---

### 12. CTR-Sink: Attention Sink for Language Models in CTR

| Field | Details |
|-------|---------|
| **Authors** | Zixuan Li, Binzong Geng et al. (Ant Group) |
| **Institution** | Ant Group |
| **arXiv** | [2508.03668](https://arxiv.org/abs/2508.03668) |

**Abstract:** Addresses semantic fragmentation in LM-based CTR prediction where discrete user behaviors with empty separators mismatch LM pre-training. Inserts sink tokens fused with recommendation signals (temporal distance) between behaviors. Two-stage training strategy guides attention to sink tokens; sink-specific attention mechanism amplifies inter-sink dependencies. Achieves 0.2-0.5% AUC improvement across industrial and public datasets on both RoBERTa and Qwen architectures.

**Key Innovations:**
- Behavior-level attention sinks tailored for recommendation scenarios
- Two-stage training explicitly guiding attention to behavioral boundaries
- Temporal distance signals embedded in sink tokens
- Architecture-agnostic: works with both encoder (RoBERTa) and decoder (Qwen) models

---

### 13. DMGIN: Multimodal LLMs for Lifelong User Post-click Behaviors

| Field | Details |
|-------|---------|
| **Authors** | (Multiple authors) |
| **Institution** | Not specified in abstract |
| **arXiv** | [2508.21801](https://arxiv.org/abs/2508.21801v1) |

**Abstract:** Uses Multimodal LLMs to group repeated shops via multimodal embeddings (name + images), reorganizing lifelong post-click behavior sequences from tens of thousands to hundreds. Pre-trains CLIP-like model for shop multimodal alignment. K-means clustering on shop embeddings with balance checks. Intra-group and inter-group transformers capture group traits and temporal evolution. Deployed in LBS advertising with +4.7% CTR and +2.3% RPM improvement.

**Key Innovations:**
- MLLM-based shop grouping for lifelong behavior sequence compression
- Near-zero additional computational overhead through offline shop embedding
- Intra-group + inter-group transformer architecture
- Successful production deployment in LBS advertising

---

### 14. ELEC: Efficient LLM-Empowered CTR Prediction

| Field | Details |
|-------|---------|
| **Authors** | (Multiple authors) |
| **Institution** | Not specified in abstract |
| **arXiv** | [2509.07594](https://arxiv.org/abs/2509.07594v1) |

**Abstract:** Pseudo-siamese network combining a gain network (with LLM) and vanilla network (without LLM). LLM's high-level representation vector is injected into collaborative CTR model. Knowledge distilled from gain to vanilla network at both score and representation levels. Vanilla network uses only tabular data but achieves comparable performance. Model-agnostic approach compatible with various LLMs and CTR models.

**Key Innovations:**
- Pseudo-siamese distillation: LLM-augmented → lightweight CTR model
- Dual-level distillation (score + representation)
- Efficiency: inference without LLM overhead
- Model-agnostic framework for LLM + CTR integration

---

## Sequential Modeling & User Behavior

### 15. Make It Long, Keep It Fast: 10K Sequence Modeling on Douyin

| Field | Details |
|-------|---------|
| **Authors** | Lin Guan et al. (ByteDance) |
| **Institution** | ByteDance (Douyin) |
| **arXiv** | [2511.06077](https://arxiv.org/abs/2511.06077) |

**Abstract:** End-to-end system scaling long-sequence modeling to 10K-length histories in production. STCA (Stacked Target-to-History Cross Attention) replaces history self-attention with stacked cross-attention, reducing complexity from O(n²) to O(n). RLB (Request Level Batching) aggregates multiple targets for same user to share encoding, reducing bandwidth by up to 84%. Length-extrapolative training: trains on ~2k average, serves on 10k. Deployed on Douyin with monotonic gains.

**Key Innovations:**
- Linear-complexity cross-attention (no history self-attention)
- Request Level Batching: 84% bandwidth reduction, 2.2× throughput
- 5× extrapolation ratio (2k train → 10k inference)
- Scaling-law-like predictable improvements with sequence length

---

### 16. ReaSeq: Reasoning-Enhanced Sequential Modeling on Taobao

| Field | Details |
|-------|---------|
| **Authors** | Chuan Wang, Gaoming Yang et al. (Taobao) |
| **Institution** | Alibaba / Taobao |
| **arXiv** | [2512.21257](https://arxiv.org/abs/2512.21257) |

**Abstract:** Addresses knowledge poverty in ID-based representations and systemic blindness to beyond-log interests. Two components: (1) Reasoning-Enhanced Representation — multi-agent collaboration distills product knowledge into enriched item representations via Chain-of-Thought; (2) Generative Behavior Reasoning — Diffusion LLM reconstructs plausible unobserved user behaviors. Deployed on Taobao: >6.0% IPV, >6.0% CTR, >2.9% Orders, >2.5% GMV.

**Key Innovations:**
- World-knowledge-enhanced sequential modeling via LLM reasoning
- Explicit CoT reasoning for product knowledge distillation
- Diffusion LLM for beyond-log behavior generation
- Full deployment on Taobao with substantial business gains

---

### 17. ULIM: User Long-Term Multi-Interest Retrieval Model

| Field | Details |
|-------|---------|
| **Authors** | (Multiple authors — Taobao) |
| **Institution** | Alibaba / Taobao |
| **arXiv** | [2507.10097](https://arxiv.org/abs/2507.10097v1) |

**Abstract:** Enables thousand-scale behavior modeling in retrieval stages. Category-Aware Hierarchical Dual-Interest Learning partitions long sequences into category-aware subsequences. Pointer-Enhanced Cascaded Category-to-Item Retrieval uses Pointer-Generator Interest Network (PGIN) for next-category prediction, then parallel item retrieval within predicted categories. Taobao deployment: +5.54% clicks, +11.01% orders, +4.03% GMV.

**Key Innovations:**
- Long-sequence modeling (thousands) in retrieval stage (not just ranking)
- Category-aware hierarchical dual-interest learning
- Pointer-generator cascaded retrieval reducing online computation
- Bridges retrieval-ranking gap with consistent long-sequence modeling

---

### 18. HiT-LBM: Hierarchical Tree Search for Lifelong Behavior Modeling

| Field | Details |
|-------|---------|
| **Authors** | (Multiple authors) |
| **Institution** | Not specified in abstract |
| **arXiv** | [2505.19505](https://arxiv.org/abs/2505.19505v1) |

**Abstract:** Uses LLMs for lifelong behavior modeling via Chunked User Behavior Extraction (CUBE) and Hierarchical Tree Search for Interests (HTS). CUBE divides lifelong behaviors into chunks with cascading interest learning. HTS generates candidate interests via hierarchical expansion and searches for optimal interest using process rating models. Temporal-aware Interest Fusion integrates chunk-level interests. Compatible with any ID-based recommendation backbone.

**Key Innovations:**
- LLM-based lifelong behavior modeling with chunked processing
- Hierarchical tree search with process rating for interest quality control
- Temporal-aware fusion of multi-chunk interests
- Model-agnostic: embeddable into any recommendation model

---

### 19. GAMER: Generative Sequential Recommendation via Hierarchical Behavior Modeling

| Field | Details |
|-------|---------|
| **Authors** | Zhefan Wang, Siyu Gu et al. |
| **Institution** | Not specified in abstract |
| **arXiv** | [2511.03155](https://arxiv.org/abs/2511.03155v1) |

**Abstract:** Multi-behavior generative recommendation with decoder-only backbone. Cross-level interaction layer captures hierarchical dependencies among behaviors (clicks, likes, shares → conversions). Sequential augmentation strategy improves robustness. Releases ShortVideoAD dataset from mainstream short-video platform with pretrained semantic IDs. Outperforms both discriminative and generative baselines with >20% gains on most metrics.

**Key Innovations:**
- Cross-level behavior interaction layer for hierarchical dependencies
- Multi-behavior sequential augmentation strategy
- ShortVideoAD: first short-video advertising multi-behavior dataset
- Decoder-only generative architecture for recommendation

---

### 20. STAR-Rec: Length Variance and Pattern Diversity in Sequential Recommendation

| Field | Details |
|-------|---------|
| **Authors** | Maolin Wang et al. |
| **Institution** | Not specified in abstract |
| **arXiv** | [2505.03484](https://arxiv.org/abs/2505.03484) |

**Abstract:** Addresses two underexplored challenges in sequential recommendation: length variance (users have vastly different behavior sequence lengths) and pattern diversity (users exhibit heterogeneous interaction patterns). Proposes STAR-Rec with specialized modules to handle both challenges simultaneously.

**Key Innovations:**
- Joint modeling of length variance and pattern diversity
- Specialized architecture for heterogeneous user behavior patterns

---

## Games & AI

### 21. Think-In Games (TiG): LLMs Learn to Reason via Game RL

| Field | Details |
|-------|---------|
| **Authors** | (Multiple authors) |
| **Institution** | Not specified in abstract |
| **arXiv** | [2508.21365](https://arxiv.org/abs/2508.21365v1) |

**Abstract:** Bridges declarative and procedural knowledge in LLMs by reformulating RL as language modeling. LLMs generate language-guided policies refined through online GRPO based on environmental feedback. Validated in Honor of Kings: Qwen-3-14B achieves 90.91% accuracy, outperforming DeepSeek-R1 (86.67%) which is 10× larger. Provides step-by-step natural language explanations for decisions.

**Key Innovations:**
- RL reformulated as language modeling task for game environments
- GRPO-based online learning from game state-action feedback
- Smaller models rival larger ones: Qwen-3-14B beats DeepSeek-R1
- Interpretable reasoning: step-by-step natural language explanations

---

### 22. SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning

| Field | Details |
|-------|---------|
| **Authors** | Bo Liu, Leon Guertler et al. |
| **Institution** | Not specified in abstract |
| **arXiv** | [2506.24119](https://arxiv.org/abs/2506.24119v3) |

**Abstract:** Self-play framework where LLMs learn by playing multi-turn zero-sum games (TicTacToe, Kuhn Poker, Negotiation) against improving versions of themselves. Proposes Role-conditioned Advantage Estimation (RAE) for stable multi-agent training. Multi-game training achieves up to +10.5% on 8 reasoning benchmarks across Qwen and Llama families. Even DeepSeek-R1-Distill-Qwen-7B benefits further.

**Key Innovations:**
- Zero-sum games as unlimited curriculum for LLM reasoning development
- Role-conditioned Advantage Estimation preventing thinking collapse
- Transferable cognitive patterns: spatial, probabilistic, strategic
- Multi-game training yields strongest synergistic results

---

### 23. Foundation Model Self-Play (FMSP)

| Field | Details |
|-------|---------|
| **Authors** | Aaron Dharna, Cong Lu, Jeff Clune |
| **Institution** | Not specified in abstract |
| **arXiv** | [2507.06466](https://arxiv.org/abs/2507.06466) |

**Abstract:** Three FMSP variants: (1) vFMSP refines policies via competitive self-play, (2) NSSP builds diverse strategy populations, (3) QDSP combines diversity and refinement. In Car Tag, FMSPs surpass human-designed strategies. In Gandalf (LLM jailbreaking), FMSPs automatically break through 6 defense levels and patch vulnerabilities. Demonstrates FM code generation enables exploration across policy space.

**Key Innovations:**
- Foundation model code generation for policy search in self-play
- Quality-Diversity Self-Play combining exploration and exploitation
- Automatic LLM red-teaming and vulnerability patching
- Diverse strategy discovery across multiple CS domains

---

### 24. Learning Game-Playing Agents with Generative Code Optimization

| Field | Details |
|-------|---------|
| **Authors** | Zhiyi Kuang, Ryan Rong et al. |
| **Institution** | Not specified in abstract |
| **arXiv** | [2508.19506](https://arxiv.org/abs/2508.19506) |

**Abstract:** Policies represented as Python programs refined via LLMs using the Trace framework. Self-evolving code with execution traces and natural language feedback. Applied to Atari games (Pong, Breakout, Space Invaders), achieves competitive performance with deep RL baselines using 52-98% less training time and far fewer environment interactions.

**Key Innovations:**
- Programmatic policy representations (Python programs) for game agents
- LLM-guided iterative policy refinement via execution traces
- Dramatic reduction in training time and environment interactions
- Interpretable, human-readable policies by design

---

## Computational Advertising & Auto-Bidding

### 25. LLM-Auction: Generative Auction for LLM-Native Advertising

| Field | Details |
|-------|---------|
| **Authors** | (Multiple authors) |
| **Institution** | Not specified in abstract |
| **arXiv** | [2512.10551](https://arxiv.org/abs/2512.10551) |

**Abstract:** First learning-based generative auction mechanism integrating auction and LLM generation. Formulates allocation as preference alignment between LLM outputs and mechanism objective balancing advertiser value and user experience. Post-trained LLM implicitly models allocation externalities without extra inference cost. First-price payment rule achieves favorable incentive properties. 59.1% revenue improvement over state-of-the-art.

**Key Innovations:**
- LLM itself implements allocation rule (no extra inference cost)
- Iterative Reward-Preference Optimization (IRPO) for mechanism training
- Theoretical guarantees: allocation monotonicity and continuity
- LLM-as-a-Judge simulation environment for evaluation

---

### 26. CBD: Generative Auto-Bidding via Diffusion Completer-Aligner

| Field | Details |
|-------|---------|
| **Authors** | Yewen Li et al. (Kuaishou) |
| **Institution** | Kuaishou |
| **arXiv** | [2509.03348](https://arxiv.org/abs/2509.03348v1) |

**Abstract:** Addresses generation uncertainty in diffusion-based auto-bidding. Completer: augments diffusion training with t-length historical sequence completion task. Aligner: trajectory-level return model refines generated trajectories. 29.9% improvement in conversion value on sparse-reward benchmarks. Deployed on Kuaishou: +2.0% target cost with significant improvements.

**Key Innovations:**
- Completer-Aligner framework for diffusion model uncertainty
- History-conditioned training for dynamic legitimacy
- Trajectory-level return model for objective alignment
- Deployed on Kuaishou advertising platform

---

### 27. GRAD: Generative Foundation Model for Auto-Bidding

| Field | Details |
|-------|---------|
| **Authors** | (Multiple authors — Meituan) |
| **Institution** | Meituan |
| **arXiv** | [2508.02002](https://arxiv.org/abs/2508.02002v2) |

**Abstract:** Scalable foundation model for auto-bidding with Action-Mixture-of-Experts for diverse bidding exploration and Causal Transformer value estimator for constraint-aware optimization. Addresses distribution shift, limited exploration, and CPM/ROI constraints. Deployed across Meituan's marketing scenarios: +2.18% GMV and +10.68% ROI.

**Key Innovations:**
- Mixture-of-Experts for constrained action space exploration
- Causal Transformer for counterfactual reward evaluation
- Scaling-law-inspired architecture design
- Multi-scenario deployment on Meituan

---

### 28. Bid2X: Bidding Foundation Model for Online Advertising

| Field | Details |
|-------|---------|
| **Authors** | Jiahao Ji et al. (Taobao) |
| **Institution** | Alibaba / Taobao |
| **arXiv** | [2510.23410](https://arxiv.org/abs/2510.23410) |

**Abstract:** First bidding foundation model generalizing across scenarios. Uniform series embeddings encode heterogeneous bidding data. Variable and temporal attention mechanisms capture complex dependencies. Zero-inflated projection module handles the unique distribution of bidding data. Evaluated on 8 large-scale datasets from Taobao. Online deployment outperforms MBRL across PV, Cost, GMV, and ROI.

**Key Innovations:**
- First bidding foundation model for cross-scenario generalization
- Zero-inflated distribution modeling for bidding data
- Variable-aware fusion for dynamic temporal dependencies
- Theoretical convergence guarantee to zero-inflated distribution

---

### 29. EGA-V1: End-to-End Generative Architecture for Unified Online Advertising

| Field | Details |
|-------|---------|
| **Authors** | (Multiple authors — Meituan) |
| **Institution** | Meituan |
| **arXiv** | [2505.19755](https://arxiv.org/abs/2505.19755v2) |

**Abstract:** Replaces multi-stage cascading architecture with a single generative model for ad ranking. RecFormer with cluster-attention mechanism models user interests and contextual externalities. Bi-stage training: pre-training + RL-based post-training. AucFormer generates ad sequences via non-autoregressive processing. Online A/B testing: +5.2% CTR, +13.6% RPM, +3.1% ROI.

**Key Innovations:**
- Unified single-model replacing cascaded pipeline
- Cluster-attention mechanism for efficiency and expressiveness
- Non-autoregressive sequence generation for real-time serving
- Eliminates goal conflicts between pipeline stages

---

### 30. Sponsored Questions and How to Auction Them

| Field | Details |
|-------|---------|
| **Authors** | Kshipra Bhawalkar, Alexandros Psomas, Di Wang |
| **Institution** | Not specified in abstract |
| **arXiv** | [2512.03975](https://arxiv.org/abs/2512.03975) |

**Abstract:** Formal model for "sponsored suggestion slots" in conversational AI where LLMs offer clarifying follow-up prompts with advertising potential. Investigates whether to jointly optimize (end-to-end) or decouple suggestion and ad slots. Shows VCG mechanism achieves efficient and truthful outcomes when jointly optimizing; modular approach has unbounded Price of Anarchy.

**Key Innovations:**
- Novel "sponsored questions" paradigm for LLM-native advertising
- Theoretical comparison of joint vs. decoupled auction mechanisms
- VCG for joint optimization achieving efficiency and truthfulness
- Price of Anarchy analysis for modular approaches

---

## Summary

| Category | Count | Key Themes |
|----------|-------|------------|
| LLMs & Reasoning | 7 | Safety alignment, self-feedback RL, multi-agent LLM collaboration, context limits, scaling laws |
| CTR & Recommendation | 7 | Field-aware Transformers, multimodal CTR, diffusion for interests, attention sinks, LLM-CTR integration |
| Sequential Modeling | 6 | 10K-length production modeling, reasoning-enhanced retrieval, lifelong behavior, generative sequential rec |
| Games & AI | 4 | LLM game reasoning, self-play for capability transfer, generative code optimization |
| Advertising | 6 | Generative auctions, diffusion auto-bidding, bidding foundation models, end-to-end ad ranking |

**Total papers: 30**

---

## Notable Trends

1. **Diffusion models** are entering CTR/recommendation (interest generation, auto-bidding) with strong results
2. **LLM + Recommendation** integration accelerating: distillation, multimodal grouping, reasoning-enhanced representations
3. **Self-play and game environments** as training grounds for transferable LLM reasoning
4. **Production deployment** is a differentiator: Taobao, Kuaishou, Meituan, Douyin all show online A/B results
5. **Scaling law analysis** extending beyond LLMs into CTR (FAT's Rademacher-based law)
6. **Foundation models** emerging for bidding/advertising, mirroring the LLM trend
