---
title: "Conference & arXiv Daily Digest — 2026-09-03"
type: synthesis
created: 2026-09-03
updated: 2026-09-03
sources: []
tags: [conference-digest, ICML2026, AAAI2026, NeurIPS2025, ICLR2026, CVPR2026, KDD2026, ACL2026, EMNLP2025, SIGIR2026, WWW2026, CIKM2025, RecSys2025, recommendation, LLM, advertising, CTR, agents, generative-models, sequential-modeling, benchmarks, daily-digest]
---

# Conference & arXiv Daily Digest — 2026-09-03

> Cross-venue survey of recent papers from top ML/AI conferences and arXiv. Focus on Google DeepMind, OpenAI, Meta, Microsoft, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, Netflix, NVIDIA, Anthropic, Apple, Amazon, and top academic labs. Organized by venue then category.

---

## 1. NeurIPS 2025 — Best Paper Awards (Nov 2025)

### 1.1 Gated Attention for Large Language Models (Best Paper)
- **Title**: Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free
- **Authors**: Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, Junyang Lin
- **Affiliation**: Alibaba Group
- **Venue**: NeurIPS 2025 (Best Paper)
- **Abstract & Key Innovations**: Comprehensive comparison of 30 gating-augmented softmax attention variants across 15B MoE and 1.7B dense models on 3.5T tokens. Core finding: a simple head-specific sigmoid gate after SDPA consistently improves performance, training stability, and scaling. Two key factors: (1) non-linearity on the low-rank softmax mapping, and (2) query-dependent sparse gating scores. Notably mitigates "attention sink" phenomenon and enhances long-context extrapolation.
- **Comparison**: Outperforms standard softmax attention variants across all scales; tolerates larger learning rates.
- **Link**: https://neurips.cc/virtual/2025/awards_detail

### 1.2 Why Diffusion Models Don't Memorize (Best Paper)
- **Title**: Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training
- **Authors**: Tony Bonnaire, Raphaël Urfin, Giulio Biroli, Marc Mezard
- **Affiliation**: - (Academic)
- **Venue**: NeurIPS 2025 (Best Paper)
- **Abstract & Key Innovations**: Identifies two distinct timescales in diffusion training: τ_gen (quality generation) and τ_mem (memorization onset). τ_mem grows linearly with dataset size n while τ_gen stays constant, creating a widening generalization window. Early stopping within this window yields generalization without memorization, even for over-parameterized models.
- **Link**: https://arxiv.org/abs/2505.17638

### 1.3 1000 Layer Networks for Self-Supervised RL (Best Paper)
- **Title**: 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities
- **Authors**: Kevin Wang, Ishaan Javali, Michał Bortkiewicz, Tomasz Trzcinski, Benjamin Eysenbach
- **Venue**: NeurIPS 2025 (Best Paper)
- **Abstract & Key Innovations**: Demonstrates increasing network depth to 1024 layers in self-supervised contrastive RL. Performance increases 2×–50× over goal-conditioned baselines. Depth qualitatively changes agent behaviors in locomotion and manipulation tasks without demonstrations or rewards.
- **Link**: https://neurips.cc/virtual/2025/awards_detail

### 1.4 Artificial Hivemind (Best Paper, DB Track)
- **Title**: Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)
- **Authors**: Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Yejin Choi
- **Affiliation**: Allen AI + Multiple
- **Venue**: NeurIPS 2025 (Best Paper, DB Track)
- **Abstract & Key Innovations**: Introduces Infinity-Chat (26K open-ended queries) and reveals "Artificial Hivemind" effect — LLMs generate surprisingly similar creative outputs. Characterized by intra-model repetition and inter-model homogeneity.
- **Link**: https://neurips.cc/virtual/2025/awards_detail

### 1.5 Runners-Up
- **Superposition Yields Robust Neural Scaling** (Anthropic) — representation superposition as key driver of neural scaling laws, loss scales inversely with dimension under strong superposition
- **Does RL Really Incentivize Reasoning Beyond the Base Model?** — critical examination of RL-based reasoning gains
- **Optimal Mistake Bounds for Transductive Online Learning** — resolves 30-year-old open problem, proves Θ(√d) bound

---

## 2. AAAI 2026 (Jan 20–27, 2026, Singapore)

> 29,000 submissions → ~4,300 accepted papers. Largest areas: CV, ML, NLP.

### 2.1 LLM Planning & Reasoning
- **SPIRAL: Symbolic LLM Planning via Grounded and Reflective Search**
  - **Authors**: Yifan Zhang et al. (IBM Research)
  - **Key Innovations**: Three specialized LLM agents (Planner, Simulator, Critic) embedded in MCTS loop. 83.6% on DailyLifeAPIs (+16pp over next-best search framework).
  - **Link**: https://ojs.aaai.org/index.php/AAAI/article/view/40975

### 2.2 CTR & Recommendation
- **Length-Adaptive Interest Network for Balancing Long and Short Sequence Modeling in CTR Prediction**
  - AAAI 2026 Technical Track
- **Dual-Horizon Interest Model for Unified Search and Recommendation**
  - AAAI 2026 Technical Track

### 2.3 Multi-Agent Systems
- Extensive Multiagent Systems track covering MARL, cooperative/competitive agents, path planning, text generation with multi-agent frameworks

### 2.4 LLM Training & Efficiency
- **SpecQuant**: Spectral Decomposition for Ultra-Low-Bit LLM Quantization
- **MP-ISMoE**: Mixed-Precision Interactive Side MoE for Efficient Transfer Learning
- **Differentially Private Subspace Fine-Tuning for LLMs**
- **FedSEA-LLaMA**: Federated Splitting Framework for LLMs

---

## 3. ICLR 2026 (Apr 23–27, 2026, Rio de Janeiro)

### 3.1 Representation Learning
- **GRACE: Generative Representation Learning via Contrastive Policy Optimization**
  - **Authors**: Jiashuo Sun, Shixuan Liu et al.
  - **Key Innovations**: Recasts contrastive signals as RL rewards guiding generative rationales. LLM produces interpretable explanations then encodes via mean pooling. +11.5% on MTEB (supervised), +6.9% (unsupervised) across 4 backbones.
  - **Link**: https://openreview.net/pdf?id=hs9lwjH1bJ

### 3.2 Diffusion Models & Generalization
- **Generalization of Diffusion Models Arises with a Balanced Representation Space**
  - **Authors**: Zekai Zhang, Xiao Li, Xiang Li et al.
  - Proves memorization = localized/spiky representations; generalization = balanced representations in ReLU DAEs. Proposes representation-based memorization detection and training-free editing.
  - **Link**: https://iclr.cc/virtual/2026/poster/10011499

### 3.3 Mechanistic Interpretability
- **Decomposing Representation Space into Interpretable Subspaces with Unsupervised Learning**
  - **Authors**: Xinting Huang, Michael Hahn
  - Neighbor Distance Minimization (NDM) finds interpretable subspaces without supervision. Validated on GPT-2 circuits and scalable to 2B models.
- **From Compression to Expression: A Layerwise Analysis of In-Context Learning**
  - Discovers "Layerwise Compression-Expression" phenomenon in ICL across diverse LLMs.

### 3.4 Vector Institute Highlights (48 accepted papers)
- Advancing representation learning, autonomous AI agents, trustworthy AI, and scientific discovery.

---

## 4. CVPR 2026 (Jun 2026)

### 4.1 Generative Models & Diffusion
- **Back to Basics: Let Denoising Generative Models Denoise** (Tianhong Li, Kaiming He)
  - Advocates predicting clean data (not noise). Simple large-patch Transformers (JiT) on pixels — no tokenizer, no pre-training, no extra loss. Competitive on ImageNet 256/512.
  - **Link**: https://openaccess.thecvf.com/content/CVPR2026/html/Li_Back_to_Basics_CVPR_2026_paper.html

- **Patch Forcing: Difficulty-Aware Adaptive Sampling for Image Generation**
  - Per-patch noise scales + lightweight difficulty head. Spatially adaptive denoising where confident regions advance first. Improves over SiT baselines on ImageNet and text-to-image.
  - **Link**: https://openaccess.thecvf.com/content/CVPR2026/papers/Schusterbauer_Patch_Forcing_CVPR_2026_paper.pdf

### 4.2 Multimodal & Visual Generation
- **Thinking-while-Generating (TWIG)** — First interleaved text-reasoning framework during visual generation. SFT + TWIG-GRPO RL show feasibility of co-evolving text reasoning.
- **SIGMA: Selective-Interleaved Generation with Multi-Attribute Tokens** — 700K interleaved examples, multi-reference image composition with disentangled attribute tokens.
- **MRT: Masked Region Transformer (20B)** — Multi-layer transparent image generation, outperforms Qwen-Image-Layered, 10–100× faster inference.
- **iMontage** — Repurposes video model for unified many-to-many image generation.
- **DPP-GRPO: Diverse Video Generation** — Determinantal Point Processes + GRPO for set-level diversity in T2V models.
- **TGT: Text-Grounded Trajectories** — Point-trajectory + localized text for locally controlled video generation.

---

## 5. ACL 2026 (Jul 2–7, 2026, San Diego)

### 5.1 LLM Steering & Control
- **Compositional Steering of LLMs with Steering Tokens**
  - **Authors**: Gorjan Radevski et al. (University of Mannheim)
  - Self-distillation of behavior into dedicated input tokens; generalizes to unseen compositions. Outperforms activation steering and LoRA merging for multi-behavior constraints.
  - **Link**: https://aclanthology.org/2026.acl-long.1435/

### 5.2 LLM Reasoning & Test-Time Compute
- **PaCoRe: Parallel Coordinated Reasoning**
  - **Authors**: Jingcheng Hu et al.
  - Message-passing architecture enabling massive parallel exploration. PaCoRe-8B achieves 94.5% on HMMT 2025, surpassing GPT-5's 93.2% by scaling effective TTC to ~2M tokens. Open-source checkpoints released.
  - **Link**: https://aclanthology.org/2026.acl-long.1253.pdf

- **Deliberative Searcher: Improving LLM Reliability via RL with Constraints**
  - **Link**: https://aclanthology.org/2026.acl-long.199.pdf

### 5.3 Sentence-Level Processing
- **Think in Sentences** — Sentence boundary delimiters as inference anchors; +7.7% on GSM8k, +12.5% on DROP across 7B–600B models. Seg-FT outperforms pause-based SFT.

### 5.4 Cognitive Science & NLP
- **Memory efficiency and resource-rational encoding** (ACL 2026 Award) — noise injection into hidden states as working memory constraint; improves alignment with human reading times.

### 5.5 RAG & Retrieval
- **Disco-RAG: Discourse-Aware RAG** — RST trees + inter-chunk rhetorical graphs + discourse-aware planning. +12.74 LLM Score on Loong benchmark.

---

## 6. EMNLP 2025 (Nov 2025, Suzhou) & EMNLP 2026 Accepted

### 6.1 EMNLP 2025
- **StepSearch: Igniting LLMs Search Ability via Step-Wise PPO**
  - **Authors**: Xuhui Zheng et al.
  - Step-level process supervision + redundancy penalties. +11.2% (3B) and +4.2% (7B) over global-reward baselines on multi-hop QA. Open-source.
  - **Link**: https://aclanthology.org/2025.emnlp-main.1106/

### 6.2 EMNLP 2026 (Accepted Papers)
- **EVAR: Evidence-Validated Hypothesis Admission for Budget-Aware Narrative Reasoning**
  - Immutable evidence store + hypothesis validation challenges + sufficiency-based stopping. Improves task performance and evidence faithfulness.
  - **Link**: https://arxiv.org/abs/2608.29835

---

## 7. SIGIR 2026 (Jul 20–24, 2026, Melbourne)

### 7.1 Retrieval & Ranking
- **Towards a Relevance Posterior in Neural Information Access** — Frames retrieval as approximate posterior inference; learned document-utility prior improves first-stage retrieval (+0.046 nDCG@10) and LLM re-ranking (+0.054).
- **CoveR: Coverage-Aware Retrieval** — Coverage contrastive + self-distillation for long-form RAG. Improves nugget coverage while preserving relevance.
- **SmartSearch: Process Reward-Guided Query Refinement** — Three-stage curriculum (imitation→alignment→generalization) for search agents.
- **APR: Adaptive Personalised Reranking for Conversational Search** — Intent-based query routing with instruction-following reranker.

### 7.2 E-Commerce & Multimodal
- **MMRM: Multiplex Multimodal Representation Model** (JD.com, deployed)
  - MLLM + 4 collaborative signals via task-specific tokens. Single-inference multiplex representations. Online: UCTR +0.42%, UACR +0.37%, UCVR +0.35%.
  - **Link**: https://arxiv.org/html/2607.11030v1

### 7.3 Agentic Search
- **Agentic Search in the Wild** — Analysis of 14.44M search requests from DeepResearchGym. 90%+ multi-turn sessions ≤10 steps; 54% of new query terms traceable to prior evidence.

---

## 8. KDD 2026 (Aug 9–13, 2026, Jeju Island)

### 8.1 CTR Prediction — Scaling Laws
- **Field-Aware Transformer (FAT)** (Alibaba/Taobao)
  - **Authors**: - (Alibaba Group)
  - **Key Innovations**: Reconstructs Transformer with field-centric parameters. Basis-Composed Hypernetwork synthesizes field-specific params. Rademacher complexity-based scaling law. +4.38% AUC offline; +2.33% CTR / +0.66% RPM in Taobao live production. P99 latency 45→48ms.
  - **Link**: https://arxiv.org/html/2511.12081v2

### 8.2 Generative Recommendation for Advertising
- **GR4AD: Generative Recommendation for Advertising** (Kuaishou, deployed)
  - UA-SID (Unified Advertisement Semantic ID) + LazyAR decoder + RSPO (Ranking-Guided Softmax Preference Optimization) + Dynamic Beam Serving. Up to +4.2% ad revenue in online A/B; 400M+ users.
  - **Link**: https://arxiv.org/abs/2602.22732v1

### 8.3 CTR & Long-Term Behavior
- **SUAN + LightSUAN** (Meituan) — Unified Attention Block for CTR scaling. Scaling laws spanning 3 orders of magnitude. Online: CTR +2.81%, CPM +1.69%.
- **DiffuMIN** (Meituan) — Diffusion-driven multi-interest network. Online: CTR +1.52%, CPM +1.10%.
- **MARS** (Kuaishou, deployed) — Modality-aligned retrieval for low-active user augmentation. Serves hundreds of millions of users.

---

## 9. RecSys 2025 (Sep 2025)

### 9.1 CTR & User Behavior
- **SUAN: Exploring Scaling Laws of CTR Model** (Meituan) — Stacked UAB + online distillation from high-grade teacher. Deployed online.
- **DiffuMIN: Diffusion-driven Multi-interest Network** (Meituan) — Target-oriented multi-interest extraction + diffusion augmentation.
- **MARS: Modality-Aligned Retrieval** (Kuaishou) — Stein kernel multimodal alignment for sparse user augmentation. Deployed to main traffic.

### 9.2 Recommendation Systems
- **Beyond Immediate Click: Engagement-Aware MoE-Enhanced Transformers**
- **LEAF: Lightweight Efficient Adaptive Flexible Embedding**
- **GenSAR: Unified Search and Recommendation with Generative Retrieval**
- **PinFM: Foundation Model for User Activity at Billion-Scale** (Pinterest)
- **User Long-Term Multi-Interest Retrieval Model**

---

## 10. CIKM 2025 (Oct 2025)

### 10.1 Advertising & Ranking
- **UniROM: Unifying Online Advertising Ranking as One Model** (Meituan)
  - End-to-end unified model for online advertising ranking.

### 10.2 Recommendation
- **NMRL: Native Multimodal CTR** (+1.5% online)
- **DTE: Temporal Encoding for Recommendation**
- **GOD: Deep Graft-Oriented Distillation** (+13.92%)

---

## 11. WWW 2026

### 11.1 Recommendation & CTR
- **SparseCTR: Sparse Attention for Long-Term CTR** (Meituan)
- **ThinkRec: Thinking-based LLM Recommendation**
- **GenCI: Generative CTR via Cohort Intent Learning**

---

## 12. Top Lab Highlights — Cross-Conference

### 12.1 Google DeepMind
- **Recirculation** — Training-free inference-time recurrence for transformers. On Gemma3: -23% perplexity, +21% GSM8k accuracy. Adaptive variant requires no weight modification.
  - **Link**: https://arxiv.org/html/2608.17981v1
- **Scaffolding Minds** — Learnable scaffolding encoder + Gaussian latent policy for multimodal reasoning. +9.5% on FrozenLake, +5.2% average across 9 visual reasoning benchmarks.
  - **Link**: https://arxiv.org/html/2608.19669
- **Visual General Intelligence: A White Paper** (Aug 2026)

### 12.2 Anthropic
- **Evaluating and Improving LLM Self-Modeling** — Benchmark + synthetic data pipeline for LLM behavioral self-prediction. RL improves self-modeling across 3 open-source model families. Released code.
  - **Authors**: Siqi Zeng et al.
  - **Link**: https://arxiv.org/html/2608.30980
- **Fine-Tuned Lie Detectors Failed to Generalize** — Cross-category AUROC plateaus at 0.70–0.75; larger prompted models often outperform fine-tuned detectors. Qwen3-235B achieves 0.98–0.99 with prompting.
  - **Link**: https://alignment.anthropic.com/2026/lie-detectors/

### 12.3 OpenAI / DeepMind / Anthropic — Joint Work
- **Positive Alignment: AI for Human Flourishing** — Cross-lab paper introducing "positive attractors" (wisdom, autonomy, truth-seeking) as training targets. Shifts from harm prevention to active flourishing.
- **A Global Workspace in Language Models** (Anthropic) — Interpretability research on global workspace theory in LLMs, with Neuronpedia demo.

### 12.4 Moonshot AI (Kimi)
- **Kimi K3: Open Frontier Intelligence** — 2.8T parameter MoE (104B activated), 1M context. KDA + Attention Residuals + Stable LatentMoE (896 routed experts, 16 active). 2.5× scaling efficiency over Kimi K2. Trails Claude Fable 5 / GPT-5.6 Sol but outperforms all other open models. Full weights released.
  - **Link**: https://arxiv.org/html/2607.24653v2

### 12.5 Tencent
- **OneRanker: Unified Generation and Ranking in Advertising** — Value-aware multi-task decoupling + Fake Item Tokens for target awareness. Deployed on WeChat Channels. GMV-Normal +1.34%.
  - **Link**: https://arxiv.org/abs/2603.02999v3
- **GPR: Generative Pre-trained Recommender** — First end-to-end generative advertising system deployed at scale. Heterogeneous Hierarchical Decoder + HEPO algorithm. GMV/CTCVR improvements on WeChat Channels.
  - **Link**: https://arxiv.org/pdf/2511.10138

### 12.6 LLM Reasoning — PaCoRe
- **PaCoRe-8B** achieves 94.5% on HMMT 2025 (surpassing GPT-5 at 93.2%) by scaling test-time compute to ~2M tokens via parallel coordinated reasoning. Open-sourced.

---

## 13. LLM Training & Scaling — arXiv Highlights (Aug–Sep 2026)

- **CARE: Contrastive Anchor-based Rubric Evolution** — Dynamic rubric evolution for RL post-training. SOTA on Arena-Hard-2.0, InfoBench, FollowBench. Only method with sustained improvement over 300 training steps. Qwen2.5-7B + CARE reaches 47% win rate vs GPT-4.1 anchor.
  - **Link**: https://arxiv.org/html/2609.00892
- **Matryoshka Language Model Suites** — Nested architecture trains 500M/1.5B/3B jointly with 36% less compute. 14–26% higher speculative decoding throughput.
  - **Link**: https://arxiv.org/html/2608.09703
- **Recipes for Steering and Scaling LLMs via Sampling** — SMC and Replica Exchange algorithms for powered/tilted distributions. Outperform Best-of-N and MCMC on MATH500.

---

## 14. Code Agents & Benchmarks — arXiv Highlights

- **SWE-EVO** — Benchmark for long-horizon software evolution. Best model (GPT-5.4) only 25% on release-sized tasks; GPT-5.2 drops from 72.8% (SWE-bench) to 22.9%.
- **RACE-bench** — 528 feature addition instances, dual-track evaluation (patch + reasoning). Resolved Rate 29–70% across agents.
- **REPOREASON** — White-box diagnostic benchmark for repository-level abductive reasoning. Reveals "Aggregation Deficit" in frontier models.
- **FOREAGENT** — Predict-then-Verify loop: 6× acceleration, +6% performance via world model filtering.
- **Agentic Coding Task-Level Prediction** — IRT-based framework predicting agent success without evaluation data.

---

## 15. Information Retrieval — SIGIR 2026 + arXiv

- **LLM Retrieval for Stable Ad Recommendations** (LinkedIn) — Semantic candidate generation via fine-tuned LLMs. +0.4% online topline, -8.62% A/A' difference (improved predictability).
  - **Link**: https://arxiv.org/html/2605.21969v1
- **GEM-Rec** — Unified framework integrating commercial relevance + monetization into generative recommendation with control tokens + Bid-Aware Decoding.
  - **Link**: https://www.arxiv.org/pdf/2603.22231
- **SA²CRQ: Adaptive Semantic Quantization** — Dynamic code length allocation for generative retrieval. Recall@2k +12.1% over TIGER; deployed in JD.com search.
- **KGSR-ADS** — Knowledge Graph + LLM-based semantic recommendation database for ads.

---

## 16. Sequential Modeling & Feature Interaction

- **HyFormer** (ByteDance) — Revisits sequence modeling vs feature interaction in CTR. Hybrid architecture balancing both.
- **FCN: Fusing Cross Network** — Exponential + Linear Cross Networks explicitly model extremely high-order interactions. -50% parameters, -23% latency via low-cost aggregation. SOTA on 6 benchmarks.
- **DS-MLP: Dual-Stream MLP** — Distillation + alignment framework achieving SOTA with vanilla MLP structure. State-of-the-art on Avazu/Criteo/KDD12.
- **SFG: Supervised Feature Generation** (ICML 2025) — Generative paradigm shift for CTR: encoder-decoder with supervised loss. Mitigates embedding collapse.

---

## Cross-Cutting Themes

1. **Structured Expressivity > Blind Scaling**: FAT (KDD'26), Gated Attention (NeurIPS'25), and FCN demonstrate that architectural alignment with data semantics matters more than raw parameter count.

2. **Generative Recommendation at Scale**: GPR, GR4AD, OneRanker, and GEM-Rec show end-to-end generative advertising is production-ready (Kuaishou, Tencent, LinkedIn).

3. **Test-Time Compute as a New Scaling Axis**: PaCoRe (2M tokens → surpassing GPT-5), Kimi K3 (1M context + agentic RL), and Recirculation (training-free recurrence) push inference-time capabilities.

4. **RL Post-Training Enters Rubric Era**: CARE's dynamic rubric evolution, StepSearch's step-wise PPO, and EVAR's evidence-validated hypothesis admission all move beyond static reward functions.

5. **Agentic Search & Agents**: SIGIR's 14M+ request analysis, SWE-EVO's evolution benchmark, and FOREAGENT's predict-then-verify paradigm show agents becoming measurable systems.

6. **CTR Scaling Laws Mature**: SUAN/EST scaling laws, FAT's Rademacher analysis, and DS-MLP's distillation framework provide principled scaling approaches for recommendation.

7. **Multimodal Convergence**: MMRM (JD.com), MARS (Kuaishou), and MidR (multimodal document retrieval) demonstrate multimodal representations are now integral to ranking systems.
