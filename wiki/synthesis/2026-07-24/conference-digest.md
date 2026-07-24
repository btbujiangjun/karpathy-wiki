---
title: "Top ML/AI Conference & arXiv Paper Digest — 2026-07-24"
type: synthesis
created: 2026-07-24
updated: 2026-07-24
sources: [icml-2026, aaai-2026, neurips-2025, iclr-2026, kdd-2026, cvpr-2026, acl-2026, sigir-2026, www-2026, recsys-2025, cikm-2025, arxiv-jul-24]
tags: [conference-digest, icml, aaai, neurips, iclr, kdd, cvpr, acl, sigir, www, recsys, cikm, recommendation, ctr, agents, reasoning, diffusion, 3d-vision, sequential-modeling, games]
---

# Conference & arXiv Digest — 2026-07-24

> Comprehensive survey of recent papers from top ML/AI conferences and arXiv, organized by venue and category. Focus on LLMs, recommendation systems, advertising, CTR, games, code execution, agents, generative models, sequential modeling, and benchmarks. Papers from Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, Netflix, NVIDIA, Anthropic, Apple, Amazon, and top labs prioritized.

---

## ICML 2026 (Seoul, Jul 6–11, 2026)

**Stats**: 23,918 submissions → 6,352 accepted (26.6% acceptance rate). 536 Spotlight papers (2.2% of submissions).

### Outstanding Papers

| Paper | Authors | Affiliation | Key Innovation |
|-------|---------|-------------|----------------|
| **The Flexibility Trap** | Zanlin Ni, Shenzhi Wang, Yang Yue, Tianyu Yu, et al. | Tsinghua / Alibaba | Challenges core dLLM assumption: arbitrary order generation *hurts* reasoning by bypassing high-uncertainty tokens. For general tasks (math, coding), fixed autoregressive order is superior. |
| **High-Accuracy Sampling** | Fan Chen, Sinho Chewi, Constantinos Daskalakis, Alexander Rakhlin | MIT / Princeton | δ-error in polylog(1/δ) steps for diffusion model sampling — exponential improvement over prior results. First polylog(1/δ) sampler for general log-concave distributions. |

### Honorable Mentions

| Paper | Key Innovation |
|-------|----------------|
| **The Obfuscation Atlas** | Maps where honesty emerges in RLVR with deception probes — reveals where RL alignment accidentally produces truthful behavior. |
| **Motion Attribution for Video Generation** | Attribution method for video generative models — identifies which training data drives specific motions. |
| **How Much Can LMs Memorize?** | Estimates GPT-style model capacity at ~3.6 bits per parameter. Models memorize until capacity fills, then begin to generalize. |
| **Random Matrix Perspective on Diffusion Consistency** | Explains why diffusion models generate near-identical images from same seed across different training runs. |
| **To Grok Grokking** | Proves grokking occurs in simple ridge regression — not unique to complex neural networks. |

### Outstanding Position Paper
**Position: The Alignment Community is Unintentionally Building a Censor's Toolkit** (Sarah Ball, Phil Hackemann) — Argues alignment methods (RLHF) are dual-use technologies that may be misused for censorship and manipulation.

### Test of Time Award
**Asynchronous Methods for Deep Reinforcement Learning** (Volodymyr Mnih, David Silver, et al., DeepMind, 2016) — The A3C paper that shaped how RL is done today in LLM post-training.

### Other ICML 2026 Highlights (from prior digests)
- **MemoPilot**: ELO#1 — efficient memory-augmented planning agent
- **HiPER**: 97.4% ALFWorld success via hierarchical planning
- **JitRL**: 30× cheaper RL training for language models
- **Self-Flow**: Self-supervised flow matching
- **UniAR**: Unified multimodal autoregressive modeling (Alibaba)
- **Shannon Scaling Law**: LLMs as noisy channels — new information-theoretic scaling law
- **InTRO**: +20% math reasoning improvement
- **Clover**: FP4 training for efficient large-scale training

---

## NeurIPS 2025 (San Diego, Dec 2025)

**Stats**: 5,823 accepted papers.

### Best Papers

| Paper | Authors | Affiliation | Key Innovation |
|-------|---------|-------------|----------------|
| **Gated Attention for LLMs** ⭐ Best | Zihan Qiu, Zekun Wang, Bo Zheng, et al. (Qwen Team) | Alibaba | Simple head-specific sigmoid gate after SDPA consistently improves performance across 15B MoE and 1.7B dense models on 3.5T tokens. Eliminates attention sink, enhances scaling. Already shipped in Qwen3-Next. |
| **Artificial Hivemind** ⭐ Best (DB) | Liwei Jiang, Yuanjun Chai, et al. | AI2 / UW | Reveals pronounced mode collapse in LLMs — both intra-model repetition and inter-model homogeneity. Introduces Infinity-Chat dataset (26K queries, 70+ models). |
| **1000 Layer RL** ⭐ Best | Kevin Wang, et al. | Princeton / Warsaw | Scaling depth to 1024 layers in self-supervised RL boosts performance 2–50× on locomotion/manipulation. Agents develop qualitatively new behaviors. |
| **Why Diffusion Models Don't Memorize** ⭐ Best | Tony Bonnaire, et al. | Bocconi / ENS Paris | Identifies critical timescales in diffusion training where generalization phase grows with dataset size before memorization kicks in. |

### Runners-Up

| Paper | Key Innovation |
|-------|----------------|
| **Does RL Really Incentivize Reasoning Beyond Base Model?** (Yang Yue, Gao Huang, Tsinghua) | RLVR improves sampling efficiency but does *not* elicit fundamentally new reasoning patterns. Base models at large k match RLVR models. |
| **Superposition Yields Robust Neural Scaling** (Yizhou Liu, MIT/Harvard) | Strong representation superposition causes loss to scale inversely with model dimension across broad frequency distributions. |
| **Optimal Mistake Bounds for Transductive Online Learning** | Resolves 30-year open problem: quadratic gap between transductive and standard online learning. |

### Test of Time Award
**Faster R-CNN** (Shaoqing Ren, Kaiming He, Ross Girshick, Jian Sun) — Region Proposal Networks revolutionized object detection.

---

## ICLR 2026 (Rio de Janeiro, Apr 23–27, 2026)

**Stats**: 19,525 submissions → 5,355 accepted (27.4%). 225 Oral presentations (1.13%).

### Outstanding Papers

| Paper | Key Innovation |
|-------|----------------|
| **Transformers are Inherently Succinct** | Proves verification of transformer expressiveness is EXPSPACE-complete. Fundamental limits on what transformers can represent. |
| **LLMs Get Lost in Multi-Turn Conversation** | Quantifies 39% performance drop in multi-turn settings — models fail to track context across turns. |

### Key Oral Papers (selected)

| Paper | Affiliation | Key Innovation |
|-------|-------------|----------------|
| **TROLL: Trust Regions Improve RL for LLMs** | - | Replaces PPO clip with discrete differentiable trust region projection. Token-level KL constraints. Consistently outperforms PPO on training speed, stability, and success rates. |
| **MemAgent** | - | Multi-Conv RL-based memory agent for long-context LLMs — reshapes context handling. |
| **Mamba-3** | - | Improved sequence modeling using state space principles. |
| **Mixture-of-Experts Can Surpass Dense LLMs Under Strictly Equal Resource** | - | Formal proof that MoE can beat dense models at equal compute budget. |
| **Verifying Chain-of-Thought Reasoning via Its Computational Graph** | - | CoT verification through computational graph analysis. |
| **Depth Anything 3** | - | Recovering visual space from any views — advances 3D perception. |
| **Common Corpus** | - | Largest ethically sourced collection for LLM pre-training data. |
| **Q-RAG** | - | Value-based embedder training for long-context multi-step retrieval via RL. |
| **SafeDPO** | - | Simple constrained approach to DPO balancing helpfulness and safety. |
| **Why DPO is a Misspecified Estimator** | - | Exposes fundamental statistical flaw in DPO alignment algorithm. |
| **LongWriter-Zero** | - | Ultra-long text generation via RL without supervised data. |

### AI Safety at ICLR 2026
35 out of 223 Oral papers are AI safety-related. Key trends:
- Attack surfaces moved from prompts to steganography, dormant fine-tuning backdoors, pruning-time activation
- Interpretability became real-time safeguard (CoT verifiers, attention-head recalibration)
- Governance infrastructure went academic (legally clean pre-training corpora, watermarks, lineage tracing, certified unlearning)

---

## AAAI 2026 (Singapore, Jan 20–27, 2026)

**Stats**: 23,680 submissions → 4,167 accepted (17.6%).

### Outstanding Papers (Main Track)
- **CADYT**: Causal Structure Learning
- **LLM2CLIP**: Vision-language alignment
- **ReconVLA**: Vision-Language-Action for robotic manipulation
- **Model Change for Description Logic Concepts**
- **High-pass Matters for Hypergraph Neural Networks**

### Key Recommendation/CTR Papers

| Paper | Affiliation | Key Innovation |
|-------|-------------|----------------|
| **TWiCE-Rec: Think Wise, Collaborate Effectively** | - | Rationale-aware LLM recommender with confidence-weighted RL from collaborative signals. +8% CTR in online A/B test. |
| **MoMoREC** | Taobao / Alibaba | Multi-agent motivation generation with residual semantic IDs. +6.3% GMV improvement. |
| **TreeBridge** | Shopee | Structure-aware generative encoding tree for LLM embedding alignment. +1.55% GMV deployed on Shopee. |
| **MSR-Rec** | - | Multi-step reasoning-enhanced LLM for sequential recommendation. Bidirectional reasoning from user and item sides. |
| **AuditAgent** | - | LLM-powered GUI-agent for risk auditing in recommender systems — filter bubbles, unfairness, data misuse. |
| **Extracting Monosemantic Concepts in Rec** | - | Sparse Autoencoder extracts interpretable neurons from user/item embeddings. Supports post-hoc filtering without model modification. |
| **SpecGR** | UCSD / Julian McAuley | Inductive generative recommendation via retrieval-based speculation. |

---

## KDD 2026 (Jeju Island, Aug 9–13, 2026)

### CTR Prediction & Ranking

| Paper | Affiliation | Key Innovation |
|-------|-------------|----------------|
| **FAT: Field-Aware Transformer** | Alibaba / Taobao | +4.38% AUC, +2.33% CTR, +0.66% RPM in live Taobao production. Rademacher complexity scaling law for CTR. Field-centric parameters + Basis-Composed Hypernetwork. |
| **CTR-Sink: Attention Sink for LMs in CTR** | Ant Group | Identifies attention sink phenomenon in LMs applied to CTR. Random information yields negligible improvement; semantic similarity signals are key. Accepted at KDD 2026. |
| **DS-MLP: Dual-Stream MLP is All You Need** | Renmin University | Simple dual-stream MLP with knowledge distillation achieves SOTA on Criteo/Avazu/MovieLens. Simplicity wins in CTR. |
| **LLM-as-a-Judge for Rec Evaluation** | - | LLM as proxy evaluator for unbiased offline rec evaluation. Stronger correlation with ground truth than biased offline testing. |
| **Congrats: Consistent Graph-structured Generative Rec** | Kuaishou | Graph-structured non-autoregressive decoder expands decoding space. +7% Recall@6 over NAR4Rec. Deployed on Kuaishou (300M+ DAU). |

### Recommendation Systems

| Paper | Affiliation | Key Innovation |
|-------|-------------|----------------|
| **RankElastor** | - | Effective-rank dynamics for recommendation — novel training paradigm. |
| **RPORec** | Kuaishou | RL + reasoning for recommendation with causal residual learning. |
| **SIGMA** | AliExpress / Alibaba | Semantic-grounded instruction-driven generative multi-task recommender. |
| **EST** | Alibaba / Taobao | +3.27% RPM via efficient scaling laws for CTR. Power-law relationship between data/model and performance. |
| **GR4AD** | - | +4.2% revenue for automated display advertising. |

---

## CVPR 2026 (New York, Jun 10–16, 2026)

**Stats**: 16,092 submissions → 4,089 accepted (25.4%).

### Best Papers

| Paper | Authors | Affiliation | Key Innovation |
|-------|---------|-------------|----------------|
| **D4RT: Efficiently Reconstructing Dynamic Scenes** ⭐ Best | Chuhan Zhang, Guillaume Le Moing, et al. | Google DeepMind / Oxford / UCL | Unified transformer for depth, spatio-temporal correspondence, and camera parameters. Lightweight 4D scene reconstruction from video in seconds. |
| **O-Voxel: Native Compact Structured Latents for 3D Generation** ⭐ Best Student | Jianfeng Xiang, Xiaoxue Chen, et al. | Tsinghua / Microsoft Research / USTC | Novel O-Voxel representation captures complex shapes/surfaces. Far exceeds existing models in 3D generation quality. |

### Highlighted Paper

| Paper | Affiliation | Key Innovation |
|-------|-------------|----------------|
| **SAM 3D: 3Dfy Anything in Images** | Meta Superintelligence Labs | Generative model for 3D object reconstruction from single image. Predicts geometry, texture, layout. 5:1 human preference win rate over prior SOTA. Released code, model, benchmark (SA-3DAO). |

### Other CVPR 2026 Highlights
- **NitroGen** (NVIDIA): Foundation model for game content generation — 40K hours training, 1000+ games, 90.5% boss success rate
- **PixelDiT**: Pixel-space DiT achieving 1.61 FID on ImageNet 256
- **Molmo2**: Open-weights VLM with video understanding and grounding
- **AVGGT**: Training-free 8–10× speedup for VGGT multi-view 3D
- **OmniVGGT**: Multi-modality driven 3D foundation model
- **E-RayZer**: Self-supervised 3D pre-training outperforming DINOv2/CroCo on 3D tasks
- **CUPID**: Generative 3D reconstruction +3dB PSNR over SOTA
- **SeeThrough3D**: Occlusion-aware 3D layout-conditioned generation

---

## ACL 2026 (San Diego, Jul 2–7, 2026)

**Stats**: 12,148 submissions → 2,296 Main Conference + 2,163 Findings (18.9% main acceptance rate). 366 agent/reasoning papers (+224 from 2025).

### Best Papers

| Paper | Key Innovation |
|-------|----------------|
| **Visually-Guided Policy Optimization for Multimodal Reasoning** | Best Paper — multimodal reasoning with visual guidance |
| **Aligning Agents via Planning** | Best Paper — trajectory-level reward modeling for agent alignment |
| **Reasoning Over Space for Generative Next POI** | Best Paper — geographic reasoning for location recommendation |
| **No More Stale Feedback: Co-Evolving Critics** | Best Paper — open-world agent learning with evolving critics |

### Key Agent/Reasoning Papers

| Paper | Affiliation | Key Innovation |
|-------|-------------|----------------|
| **KARL** | Tsinghua (THUDM) | RL for LLM agents on multi-turn knowledge-intensive tasks. Qwen2.5-14B beats GPT-4o, Claude-4, o4-mini on knowledge graph and DB tasks. |
| **OctoTools** | Stanford (James Zou) | Training-free multi-agent framework with standardized tool cards. +9.3% over GPT-4o on 16 tasks. |
| **Graph Reasoning Paradigm (GRP)** | Baidu / NUDT | Structured symbolic reasoning via graph representations. PASC-GRPO for process-aware stratified clipping. |
| **SAVeR** | - | Self-audited verified reasoning — adversarial auditing for faithful reasoning in long-horizon agents. |
| **SafeAgent** | - | Automated risk simulator for LLM agents. +45% safety improvement via synthetic data generation. |
| **Proactive Interactive Reasoning (PIR)** | - | Transforms LLMs from passive solvers to proactive inquirers. +32.7% accuracy, 50% less compute. |
| **OneRec-Think** | Kuaishou | In-text reasoning for generative recommendation — integrates CoT into rec pipeline. |
| **AgencyBench** | - | Benchmarking autonomous agents in 1M-token real-world contexts. |

### Key Themes at ACL 2026
- **Agent + Reasoning**: Largest growth area (+224 papers). Agents can reason, retrieve, cite, explain, and fail less dangerously.
- **RLVR Maturation**: Process-aware GRPO variants replacing naive outcome-only rewards
- **Multimodal Reasoning**: Vision-guided policy optimization becoming dominant
- **Safety as First-Class**: 45% safety improvements possible with automated synthetic data

---

## SIGIR 2026 (Melbourne, Jul 20–24, 2026)

### Key Papers

| Paper | Affiliation | Key Innovation |
|-------|-------------|----------------|
| **L2Rec** | - | Dual-view understanding of LLMs for personalized rec. DPMoE for parameter-level behavioral/semantic adaptation. +9.24% CTR, +3.15% reply rate in online A/B test on 1.5M DAU platform. |
| **SIGMA** | AliExpress | Semantic-grounded instruction-driven generative multi-task recommender. |
| **L2Rec** (SIGIR '26) | - | Behavioral + semantic signals unified at parameter level via Dual-view Personalized MoE. |
| **Agentic Search** | - | 14M production requests — agentic search for real-world information retrieval. |
| **ACE** | - | Anisotropy-controllable embeddings — +12.4% improvement. |

---

## WWW 2026

### Key Papers

| Paper | Affiliation | Key Innovation |
|-------|-------------|----------------|
| **ThinkRec System** | - | System 2 reasoning for recommendation — shifts from intuitive to rational LLM4Rec. Thinking activation + instance-wise expert fusion. |
| **GenCI** | - | Generative cohort intent for CTR — cohort-level intent learning. |
| **SparseCTR** | Meituan | Sparse attention for long-term CTR — +1.72% CTR improvement. Deployed. |
| **GENSTRAT** | - | Strategic reasoning in LLMs via structured prompting. |

---

## RecSys 2025 / CIKM 2025

### Key Papers

| Paper | Venue | Affiliation | Key Innovation |
|-------|-------|-------------|----------------|
| **LO-FAR** | RecSys 2026 | - | CPU-only feature ranking — no GPU needed for industrial rec. |
| **DLMRec** | RecSys 2026 | - | Diffusion language model for recommendation. |
| **PRL** | RecSys 2026 | - | Causal residual learning for recommendation. |
| **LSVCR** | RecSys 2025 | Kuaishou | +4.13% improvement in live video+comment joint recommendation. |
| **LONGER** | RecSys 2025 | ByteDance | Ultra-long user behavior sequences for CTR. |
| **RankMixer** | CIKM 2025 | ByteDance | Scaling up ranking models — hardware-aligned design. |

---

## arXiv Highlights (Jul 20–24, 2026)

### LLM Reasoning & Efficiency

| Paper | Affiliation | Key Innovation |
|-------|-------------|----------------|
| **TRSP** | ICML 2026 | 83% accuracy at 8× training length — fixes representation collapse in long-context training. |
| **SOAP/Muon** | NVIDIA | Large-scale pretraining with new optimizer geometry. |
| **Codec-Gauge** | - | 44% KV cache compression improvement via codec-based gauge. |
| **DecodeShare** | - | Decode-time shared subspace for KV cache — reduces inference memory. |
| **CARGO** | - | Training-free LLM offloading — no fine-tuning needed for model partitioning. |
| **SonicSampler** | - | 16× sampling speedup for diffusion models. |

### Agent Systems

| Paper | Affiliation | Key Innovation |
|-------|-------------|----------------|
| **ATM** | - | Autonomous topology mutation — agent architecture evolves at runtime (3.3%→61.7% accuracy). <500μs overhead. |
| **Robust Critics** | - | Multi-turn MDP defense against adversarial agent attacks. |
| **VeriSimpl** | ICML 2026 | Optimization verification for agent planning. |
| **PhantomFill** | - | Form-caused hallucination in LLMs — 100% fabrication rate when forms induce misleading context. |

### CTR & Recommendation (New Jul 24)

| Paper | Affiliation | Key Innovation |
|-------|-------------|----------------|
| **BARGE** | Tencent | +0.60% CTR for generative recommendation with semantic IDs. Production-validated. |
| **SalesLoop** | - | RL for sales lead optimization — +8.7% in production A/B test. |
| **CCBR** | - | Controllable content-based recommendation. |
| **SHIFT** | - | Self-reconstruction for retrieval — improved item representation. |
| **UniRank** | - | Unified ranking benchmark for fair comparison. |

---

## Cross-Cutting Themes

### 1. Diffusion Models Dominate ICML 2026
Two Outstanding Papers on diffusion models + Honorable Mentions signal diffusion as the highest-density research area. DLMs (diffusion language models) face the "Flexibility Trap" — arbitrary order generation hurts reasoning. High-accuracy sampling reaches exponential improvement.

### 2. RL Post-Training Reaches Maturity — and Its Limits
NeurIPS 2025 Best Runner-Up (Yue et al.) shows RLVR doesn't create new reasoning patterns. ICML 2026 Obfuscation Atlas maps where honesty accidentally emerges. ICLR 2026 TROLL replaces PPO clip with principled trust regions. The community is moving from "RL makes LLMs smarter" to "RL makes LLMs sample more efficiently."

### 3. CTR Prediction: Architecture > Scale
FAT (KDD 2026) proves structured expressivity beats parameter inflation. DS-MLP shows vanilla MLP with distillation achieves SOTA. CTR-Sink identifies attention sink as key failure mode for LMs in CTR. The scaling law for CTR is fundamentally different from LLMs.

### 4. Generative Recommendation Goes Industrial
BARGE (Tencent +0.60% CTR), Congrats (Kuaishou deployed), SIGMA (AliExpress), GenCI (WWW 2026) — generative rec is no longer academic. Semantic IDs + graph-structured decoders enable production deployment.

### 5. Agent Safety and Reliability at Scale
ACL 2026: 366 agent/reasoning papers (+224 from 2025). SafeAgent (+45% safety), SAVeR (faithful reasoning), PhantomFill (100% fabrication). ICLR 2026: 35 AI safety oral papers. Agent safety is transitioning from a niche concern to a first-class engineering requirement.

### 6. 3D Vision Breakthroughs at CVPR 2026
D4RT (dynamic 4D reconstruction), O-Voxel (3D generation), SAM 3D (5:1 preference win) — 3D understanding reaches practical quality. Training-free acceleration (AVGGT 8–10×) enables real-time deployment.

### 7. MoE vs Dense: The Debate Settled
ICLR 2026 Oral proves MoE can surpass dense LLMs under strictly equal resource budgets. NeurIPS 2025 Gated Attention (shipped in Qwen3-Next) validates sparse gating for attention. The architecture debate is shifting from "which is better" to "how to optimize MoE routing."

### 8. Reasoning-Rec Convergence
ThinkRec (WWW 2026), OneRec-Think (ACL 2026), RPORec (Kuaishou), MSR-Rec (AAAI 2026) — Chain-of-Thought reasoning is being integrated into recommendation pipelines across all major venues. The question is no longer "should rec models reason" but "how to make reasoning efficient."

---

## Statistics Summary

| Venue | Year | Submissions | Accepted | Rate | Key Topic |
|-------|------|------------|----------|------|-----------|
| ICML | 2026 | 23,918 | 6,352 | 26.6% | Diffusion models, sampling theory |
| AAAI | 2026 | 23,680 | 4,167 | 17.6% | Efficiency over scale, RAG maturity |
| NeurIPS | 2025 | ~15,000+ | 5,823 | ~38% | Attention mechanisms, RL scaling |
| ICLR | 2026 | 19,525 | 5,355 | 27.4% | Safety, DPO fixes, agent memory |
| KDD | 2026 | ~5,000+ | ~1,500+ | ~30% | CTR scaling, generative rec |
| CVPR | 2026 | 16,092 | 4,089 | 25.4% | 3D reconstruction, diffusion DiT |
| ACL | 2026 | 12,148 | 2,296 | 18.9% | Agents, reasoning, RLVR |
| SIGIR | 2026 | ~3,000+ | ~600+ | ~20% | LLM-based rec, agentic search |
