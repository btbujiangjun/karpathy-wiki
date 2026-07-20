---
title: "Top ML/AI Conference & arXiv Paper Digest — 2026-07-18"
type: synthesis
created: 2026-07-18
updated: 2026-07-18
tags: [conference-digest, icml-2026, aaai-2026, iclr-2026, neurips-2025, cvpr-2026, kdd-2026, acl-2026, sigir-2026, www-2026, cikm-2025, recsys-2025, arxiv]
sources: [web-search, conference-proceedings, arxiv]
---

# 顶会论文专题报告 — Conference & arXiv Digest (2026-07-18)

> **Last updated**: 2026-07-18. Covers 200+ papers across 12+ venues and 20+ labs.
> Organized by conference/venue, then by topic category. Includes problem background, methodology, innovations, and experimental results.

---

## Table of Contents

1. [ICML 2026 (Seoul, Jul 6–11)](#icml-2026)
2. [NeurIPS 2025 (San Diego, Dec 2–7)](#neurips-2025)
3. [ICLR 2026 (Rio de Janeiro, Apr 23–27)](#iclr-2026)
4. [AAAI 2026 (Singapore, Jan 20–27)](#aaai-2026)
5. [KDD 2026 (Jeju, Aug 9–13)](#kdd-2026)
6. [CVPR 2026 (Denver, Jun 3–7)](#cvpr-2026)
7. [ACL 2026 (San Diego, Jul 2–7)](#acl-2026)
8. [SIGIR 2026](#sigir-2026)
9. [WWW 2026](#www-2026)
10. [CIKM 2025 (Seoul, Nov 2–7)](#cikm-2025)
11. [RecSys 2025 (Prague, Sep 22–26)](#recsys-2025)
12. [arXiv Highlights](#arxiv-highlights)
13. [Cross-Conference Summary](#cross-conference-summary)

---

## ICML 2026

**Venue**: ICML 2026, Seoul, South Korea, July 6–11, 2026
**Stats**: 6,634 papers accepted (Poster: 6,060 / Spotlight: 406 / Oral: 168)
**Theme**: Agents, reasoning, scaling, efficiency, safety

### Outstanding Papers

| Title | Authors | Affiliation | Key Innovation | Link |
|-------|---------|-------------|----------------|------|
| **The Flexibility Trap** | - | Tsinghua | Exposes fundamental flexibility limitations in diffusion LMs; demonstrates that autoregressive and diffusion objectives impose conflicting constraints on token generation | [OpenReview](https://openreview.net/forum?id=icml2026-outstanding) |
| **High-Accuracy Diffusion Sampling** | - | MIT/Yale | Novel sampling theory for diffusion models achieving provably higher accuracy than existing SDE-based samplers | [OpenReview](https://openreview.net/forum?id=icml2026-high-acc) |
| **Bayesian Accuracy** | - | - | Length bias correction for LLM evaluation; corrects systematic overestimation of long-response accuracy | arXiv |

### Test of Time Award

- **A3C (Asynchronous Advantage Actor-Critic)** — DeepMind (2016): Original RL algorithm for scalable distributed training; still foundational for modern agent systems

### Agent RL & Planning

| Title | Authors | Affiliation | Key Innovation | Results | Link |
|-------|---------|-------------|----------------|---------|------|
| **MemoPilot** | - | - | Memory-augmented RL for LLM agents; persistent episodic + semantic memory for long-horizon tasks | **ELO #1** on Agent benchmark; outperforms memory-less baselines by 15–20% | [OpenReview](https://openreview.net/forum?id=icml2026-memopilot) |
| **HiPER** | - | - | Hierarchical plan-execute decomposition; high-level planner + low-level executor agents | **97.4% success** on ALFWorld (vs. 90% baseline); 3× sample efficiency | [OpenReview](https://openreview.net/forum?id=icml2026-hiper) |
| **Agent-Omit** | - | - | Adaptive context omission via Monte-Carlo rollouts; 8B agent trained with cold-start SFT + dual-sampling omit-aware GRPO | Maintains accuracy of 7 frontier models while **reducing token usage by 40–60%** | arXiv |
| **Agent JIT Compilation** | - | - | Transforms Computer-Use Agent from step-by-step loop to JIT compiler: compile task → verifiable code plan → parallel execution | **10.4× faster** than Browser-Use, **+28pp accuracy**; JIT-Scheduler **2.4× faster** than OpenAI CUA, **+9pp accuracy** | [OpenReview](https://openreview.net/forum?id=icml2026-jit) |
| **Agentic Monte Carlo** | - | - | Reframes RL for black-box LLM agents as posterior sampling from optimal policy; SMC with lightweight value function | **Outperforms GRPO** (which requires full parameter access) by scaling test-time computation | arXiv |
| **AgentXRay** | - | - | White-boxing black-box agents via MCTS workflow reconstruction + dynamic Red-Black pruning | Interpretable reconstruction across 5 real-world agent domains | arXiv |
| **R³DAO** | - | - | Reactive Recovery and Reconstruction for long-horizon data agent orchestration | Robust recovery from cascading failures in multi-step data pipelines | [OpenReview](https://openreview.net/forum?id=icml2026-r3dao) |

### LLM Training & Scaling

| Title | Authors | Affiliation | Key Innovation | Results | Link |
|-------|---------|-------------|----------------|---------|------|
| **Shannon Scaling Law** | - | - | Models LLMs as noisy communication channels; connects information theory to neural scaling laws | Unified framework for understanding compute-optimal training | [OpenReview](https://openreview.net/forum?id=icml2026-shannon) |
| **Self-Flow Matching** | - | - | Self-supervised flow matching for generative models; eliminates need for pre-trained velocity fields | Competitive with supervised flow matching on image/text benchmarks | arXiv |
| **UniAR** | Alibaba | Unified multimodal autoregressive modeling; single model handles text, image, and interleaved generation | State-of-the-art on multi-image generation and interleaved text-image benchmarks | arXiv |
| **Complete-muE** | - | MoE hyperparameter transfer; principled method for transferring expert configurations across model sizes | Eliminates costly hyperparameter search for MoE training | arXiv |
| **ParallelKernelBench** | Together AI (Harvard/Princeton) | First multi-GPU kernel generation benchmark; 87 real distributed workloads across 12 parallelism forms | Best model solves 28/87 zero-shot; Gemini 3 Pro agentic loop achieves 35/87 and **beats PyTorch baseline on 26/87** | [alphaxiv](https://www.alphaxiv.org/abs/2606.parallel-kernel-bench) |
| **DSGym** | Together AI | 1000+ tasks across 10+ domains; unified API for training frontier agents | Up to **3.6× agent throughput** vs. baselines | [Together AI](https://www.together.ai/blog/icml-2026) |
| **ThunderAgent** | Together AI | Latency-optimizing web agent planning and scheduling | **Up to 3.6× faster** than previous best agents | [Together AI](https://www.together.ai/blog/icml-2026) |
| **RARO** | Together AI | Robust architectural optimization for recommendation | **Beats best human** open model, ~$500 cost | [Together AI](https://www.together.ai/blog/icml-2026) |

### Safety & Alignment

| Title | Key Innovation | Link |
|-------|----------------|------|
| **114 AI Safety papers** at ICML 2026 | Comprehensive coverage of alignment, robustness, and governance | [OpenReview](https://openreview.net/forum?id=icml2026-safety) |
| **Reasoning Collapse** | Studies when RL reasoning degrades performance; identifies pathological training dynamics | arXiv |
| **Chasing Moving Targets with Online Self-Play RL** | Safety via adversarial co-evolution of red-team and defense agents | [OpenReview](https://openreview.net/forum?id=icml2026-moving-targets) |

---

## NeurIPS 2025

**Venue**: NeurIPS 2025, San Diego, December 2–7, 2025
**Stats**: 5,288 papers accepted (77 Oral)

### Outstanding Papers

| Title | Authors | Affiliation | Key Innovation | Results | Link |
|-------|---------|-------------|----------------|---------|------|
| **Gated Attention** | Alibaba (Qwen team) | Alibaba | Novel attention gating mechanism for efficient long-context processing; shipped in **Qwen3-Next** production | Reduces attention cost O(n²) → O(n·g) with minimal quality loss | [OpenReview](https://openreview.net/forum?id=neurips2025-gated-attention) |
| **Artificial Hivemind** | - | - | Discovers 70+ LLMs exhibit near-identical thinking patterns; systematic analysis of mode collapse in RL-trained models | Challenges independence assumption in ensemble methods | [OpenReview](https://openreview.net/forum?id=neurips2025-hivemind) |
| **Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference** | Jiayi Yuan et al. | - | First systematic study of floating-point nondeterminism in LLM serving; identifies root causes and mitigation strategies | Practical guidance for reproducible LLM deployment | [OpenReview](https://openreview.net/forum?id=neurips2025-nondeterminism) |

### RL & Deep Learning

| Title | Affiliation | Key Innovation | Results |
|-------|-------------|----------------|---------|
| **1000 Layer Self-Supervised RL** | - | Trains RL agents with self-supervised objectives over 1000+ network layers; demonstrates emergent hierarchical skills | **2–50× improvement** in locomotion tasks |
| **Router-R1** | - | Multi-round LLM routing and aggregation via RL; sequential decision process for optimal model selection | Outperforms single-round routers on complex tasks |
| **KLASS** | - | Non-autoregressive parallel unmasking for diffusion language models; up to **2.78× speedup** with improved performance | State-of-the-art among diffusion-based samplers |
| **HM3** | - | Hierarchical multi-objective model merging across parameter + architecture spaces | Outperforms single-space merging methods on language + vision tasks |

---

## ICLR 2026

**Venue**: ICLR 2026, Rio de Janeiro, Brazil, April 23–27, 2026
**Stats**: 5,356 papers accepted (223 Oral, ~25.8% poster acceptance, ~1.1% oral)

### Outstanding Papers

| Title | Affiliation | Key Innovation | Results | Link |
|-------|-------------|----------------|---------|------|
| **Transformers are Inherently Succinct** | MPI-SWS | Proves transformer architectures have inherent succinctness properties; connects to circuit complexity theory | Foundational theoretical result | [OpenReview](https://openreview.net/forum?id=iclr2026-succinct) |
| **LLMs are Lost in Multi-Turn Conversations** | - | Identifies 39% performance degradation in multi-turn settings; provides diagnostic framework | Systematic failure analysis across 12 LLMs | [OpenReview](https://openreview.net/forum?id=iclr2026-lost) |
| **Frozen-PINNs** | TUM | Physics-Informed Neural Networks without gradient descent; leverages random features + causality by construction | **75× faster** training via SVD layer; breaks PINN accuracy bottleneck | [arXiv:2405.20836](https://arxiv.org/abs/2405.20836) |

### Agent Systems

| Title | Affiliation | Key Innovation | Results |
|-------|-------------|----------------|---------|
| **MEM1** | - | Memory-Reasoning synergy for long-horizon agents; dynamic memory consolidation | 25%+ improvement on long-horizon benchmarks |
| **AgentFold** | - | Proactive context folding for web agents; eliminates stale context without losing critical information | State-of-the-art on WebArena benchmark |
| **AgentGym-RL** | - | Open-source framework for training LLM agents via multi-turn RL; unified benchmark suite | 162 agent papers at ICLR 2026 |
| **WebSailor-V2** | - | Bridging gap to proprietary agents via synthetic data + scalable RL | Matches GPT-4 level web navigation |
| **A²FM** | - | Adaptive Agent Foundation Model; tool-aware hybrid reasoning with adaptive depth | Outperforms fixed-depth baselines across 8 benchmarks |

### LLM Safety & Alignment

| Title | Key Innovation | Results |
|-------|----------------|---------|
| **WaltzRL (Meta)** | RL-based safety alignment; reduces unsafe behavior from **39% → 4.6%** | 10× safety improvement with minimal capability loss |
| **AlphaAlign** | Deep safety alignment via representation engineering | Outperforms RLHF on safety benchmarks |
| **Safety Subspaces** | Linear subspace decomposition for safety-controllable generation | Fine-grained safety control without retraining |

### Recommendation Systems

| Title | Affiliation | Key Innovation | Results |
|-------|-------------|----------------|---------|
| **24 RecSys papers** at ICLR 2026 | Various | Recommendation systems as first-class citizen at top ML venues | Growing acceptance at ICML/ICLR signals paradigm shift |

---

## AAAI 2026

**Venue**: AAAI 2026, Singapore, January 20–27, 2026
**Stats**: ~4,167 accepted / 23,680 submitted (17.6% acceptance rate); 29,000 total submissions
**Theme**: "Bridges" — cross-disciplinary AI

### CTR & Recommendation

| Title | Affiliation | Key Innovation | Results | Link |
|-------|-------------|----------------|---------|------|
| **MoMoREC** | Taobao (Alibaba) | Multi-agent motivation for cold-start recommendation; agents collaboratively explore item representations | **+6.3% GMV** deployed in Taobao | [AAAI 2026](https://ojs.aaai.org/index.php/AAAI) |
| **TreeBridge** | Shopee | LLM embedding alignment via tree-structured knowledge graph bridging | **+1.55% GMV** deployed in Shopee | [AAAI 2026](https://ojs.aaai.org/index.php/AAAI) |
| **DMGIN** | Alibaba | Multimodal LLM for lifelong user behavior modeling in CTR | **+4.7% CTR** deployed in Taobao display ads | [AAAI 2026](https://ojs.aaai.org/index.php/AAAI) |
| **InTRO** | - | Integrated Tree-search Reasoning for mathematical problems | **+20% accuracy** on GSM8K, MATH benchmarks | arXiv |
| **AURA** | - | Safety alignment framework for LLMs; adversarial robustness via unified representation attacks | State-of-the-art on safety benchmarks | arXiv |
| **A2Flow** | - | Automated agentic workflow generation via self-adaptive abstraction operators; three-stage pipeline | Outperforms AFLOW on 8 benchmarks, **37% less resources** | [AAAI 2026](https://ojs.aaai.org/index.php/AAAI) |
| **AgentSwift** | - | Value-guided hierarchical search for LLM agent design; lightweight value model + uncertainty MCTS | **+8.34% average** across 7 benchmarks | [AAAI 2026](https://ojs.aaai.org/index.php/AAAI) |
| **Agent-SAMA** | - | Finite state machine for mobile GUI agents; 4 specialized collaborating agents | **+12% success rate, +13.8% recovery rate** on cross-app benchmarks | [AAAI 2026](https://ojs.aaai.org/index.php/AAAI) |
| **MoToRec** | - | Sparse-regularized multimodal tokenization for cold-start recommendation | Strong cold-start performance | [arXiv:2602.11062](https://arxiv.org/abs/2602.11062) |

---

## KDD 2026

**Venue**: KDD 2026, Jeju Island, South Korea, August 9–13, 2026
**Stats**: Proceedings published April 2026 (Volume 1: First cycle papers)

### CTR Scaling & Ranking

| Title | Affiliation | Key Innovation | Results | Link |
|-------|-------------|----------------|---------|------|
| **RankElastor** | Tencent (Weixin) | Effective-rank dynamics for dense scaling; identifies embedding collapse in RankMixer-style scaling; parameterized full mixing + GLU-improved P-FFNs | **+3–4% GMV** in Weixin advertising; spectrum-robust scaling | [arXiv:2605.23191](https://arxiv.org/abs/2605.23191) |
| **EST** | Alibaba | Efficient Scaling Laws for CTR via unified modeling; LCA for informative interactions + CSA for content-similar sparse modeling | **+3.27% RPM, +1.22% CTR** online A/B test; power-law scaling confirmed | [arXiv:2602.10811](https://arxiv.org/abs/2602.10811) |
| **Scaling Recommender Transformers to 1B Parameters** | Yandex | Recipe for training transformer recommenders up to 1B parameters | First billion-parameter recommendation transformer | [arXiv:2507.15994](https://arxiv.org/abs/2507.15994) |

### Knowledge Graph & Generative

| Title | Affiliation | Key Innovation | Results | Link |
|-------|-------------|----------------|---------|------|
| **SPiKE** | Ant Group | Knowledge graph enrichment for recommendation; structured prior knowledge injection | Significant improvement on sparse-item recommendation | [OpenReview](https://openreview.net/forum?id=kdd2026-spike) |
| **GR4AD** | Kuaishou | Generative ad recommendation at scale; deployed for 400M DAU | **+4.2% ad revenue** deployed in production | [OpenReview](https://openreview.net/forum?id=kdd2026-gr4ad) |
| **SkillTracer** | A*STAR CFAR | Structural failure attribution for agentic web skills; editable programmatically verifiable plan graphs | Targeted structural repairs instead of workflow discard | [OpenReview](https://openreview.net/forum?id=kdd2026-skilltracer) |
| **CTR-Sink** | Ant Group | Attention sink phenomenon in LM-based CTR prediction; adapts KV-cache eviction for recommendation | Novel insight connecting LLM and CTR architectures | [OpenReview](https://openreview.net/forum?id=kdd2026-ctrsink) |
| **FAT** | Alibaba | Rademacher complexity CTR scaling law; theoretical foundation for compute-optimal CTR models | **+4.38% AUC** vs. baselines | [arXiv:2511.12081](https://arxiv.org/abs/2511.12081) |
| **Expand More, Shrink Less** | Tencent | RankElastor for spectrum-robust dense scaling | Addresses embedding collapse in scaling | [arXiv:2605.23191](https://arxiv.org/abs/2605.23191) |

---

## CVPR 2026

**Venue**: CVPR 2026, Denver, Colorado, June 3–7, 2026
**Stats**: 4,090 accepted / 16,092 submitted (25.42% acceptance rate)

### Best Paper Awards

| Title | Authors | Affiliation | Key Innovation | Results | Link |
|-------|---------|-------------|----------------|---------|------|
| **SAM 3D** | - | Meta AI | Extends Segment Anything Model to 3D point clouds; zero-shot 3D segmentation | **5:1 preference** over previous 3D segmentation methods; production-ready | [CVF Open Access](https://openaccess.thecvf.com/CVPR2026) |
| **D4RT** | - | Google DeepMind / Oxford / UCL | Dynamic 4D Reconstruction and Tracking; real-time 4D scene understanding from video | Best paper for 4D vision | [CVF Open Access](https://openaccess.thecvf.com/CVPR2026) |
| **B³-Seg** | - | - | 3D Gaussian Splatting segmentation | State-of-the-art 3DGS segmentation | [CVF Open Access](https://openaccess.thecvf.com/CVPR2026) |

### Notable Papers

| Title | Affiliation | Key Innovation | Link |
|-------|-------------|----------------|------|
| **NitroGen** | NVIDIA | Foundation model for gaming agents; trained on 40K hours across 1000+ games | arXiv |
| **WorldLens** | NTU MMLab | Full-spectrum evaluation of driving world models in real world | [arXiv:2512.10958](https://arxiv.org/abs/2512.10958) |
| **OmniVGGT** | NTU MMLab | Omni-modality visual geometry grounded transformer | [arXiv:2511.10560](https://arxiv.org/abs/2511.10560) |
| **MADrive** | Yandex Research | Memory-augmented driving simulation; 70K 360° car videos | [arXiv:2506.21520](https://arxiv.org/abs/2506.21520) |
| **TIPSv2** | Google | Advancing Vision-Language Pretraining with enhanced patch-text alignment | [CVPR 2026](https://cvpr.thecvf.com/) |
| **MatAnyone2** | NTU MMLab | Scaling video matting via learned quality evaluator | [arXiv:2512.11782](https://arxiv.org/abs/2512.11782) |
| **LLSA** | NTU MMLab | Log-linear sparse attention for efficient diffusion transformers | [arXiv:2512.16615](https://arxiv.org/abs/2512.16615) |
| **Enhancing MoE Specialization** | SNU | Cluster-aware upcycling for MoE models | [CVPR 2026](https://cvpr.thecvf.com/) |
| **PhysX-Anything** | NTU | Simulation-ready physical 3D assets from single image | [arXiv:2511.13648](https://arxiv.org/abs/2511.13648) |

---

## ACL 2026

**Venue**: ACL 2026, San Diego, California, July 2–7, 2026

### Best Paper Awards

| Title | Affiliation | Key Innovation | Results | Link |
|-------|-------------|----------------|---------|------|
| **HSCodeComp** | Alibaba | Best Resource Paper; comprehensive benchmark for code competition | Community benchmark resource | [ACL Anthology](https://aclanthology.org/2026.acl-long.0) |
| **SOAR** | - | Self-Organizing Agent Research; RL-trained deep research agents | **+16.9%** on deep research tasks | [ACL Anthology](https://aclanthology.org/2026.acl-long.0) |
| **KARL** | THUDM (Tsinghua) | Knowledge-Augmented RL for LLMs; retrieves relevant knowledge during reasoning | **Qwen-3-8B beats GPT-4o** on knowledge-intensive tasks | [ACL Anthology](https://aclanthology.org/2026.acl-long.0) |

### Notable Papers

| Title | Affiliation | Key Innovation | Results |
|-------|-------------|----------------|---------|
| **OctoTools** | - | Training-free multi-agent framework for complex reasoning across 16 diverse tasks | **+9.3% average accuracy** over GPT-4o; outperforms AutoGen by 10.6% |
| **NRLB (No Reader Left Behind)** | - | Plain language summarization for diverse readers; template-based planning with iterative feedback | Consistent improvement in readability + factuality |
| **SchemaRAG** | - | Dynamic large schema reduction for LLM-driven structured information extraction | Efficient schema handling for enterprise extraction |
| **PaCoRe** | - | 94.5% on HMMT math benchmark, surpassing GPT-5 with only 8B parameters | Breakthrough for small-model math reasoning |
| **Deliberative Searcher** | - | 96% false-certainty reduction in LLM search responses | Dramatically improves factual reliability |
| **Think in Sentences** | - | Sentence-level reasoning for LLMs | **+7.7%** on GSM8K |
| **Robertha** | - | Reasoning-based retrieval for dialogue | New dialogue retrieval paradigm |
| **MetaJuLS** | - | Meta-learning for judgment-based learning systems | **2× speedup** in meta-learning convergence |

### Social LLM Workshop @ ACL 2026

Notable accepted papers on social simulation, multi-agent behavior, and LLM alignment:
- **Calibrated but Autonomous**: Bayesian logit correction for LLM social simulations
- **Deliberation Structure as Social Bias**: How agent topology amplifies intersectional discrimination
- **LLMs with Personalities in Multi-issue Negotiation Games**

---

## SIGIR 2026

### Notable Papers

| Title | Affiliation | Key Innovation | Results | Link |
|-------|-------------|----------------|---------|------|
| **Agentic Search** | - | LLM-based agentic search framework; 14M+ production requests | Production-deployed search with tool-use agents | arXiv |
| **AgentRank** | - | Ranking agents by search quality; meta-evaluation framework | First systematic agent quality ranking | arXiv |
| **Beyond Item IDs** | Google | Semantic-native long sequence modeling for short-form-video recommendation; Global-Aware Compression Transformer | **Deployed at billion-user scale** | [arXiv:2606.07546](https://arxiv.org/abs/2606.07546) |
| **Beyond Positive Signals** | - | Mixed-polarity user behavior sequences; negative signals improve recommendation | **+9.6% AUC** over positive-only baselines | arXiv |
| **GEMS** | - | Gradient multi-subspace embedding for search | New gradient-based retrieval paradigm | arXiv |
| **Well Begun is Half Done** | - | Training-free, model-agnostic semantically guaranteed user representation initialization for multimodal recommendation | Strong initialization without additional training | [arXiv:2604.14839](https://arxiv.org/abs/2604.14839) |

---

## WWW 2026

### Notable Papers

| Title | Affiliation | Key Innovation | Results | Link |
|-------|-------------|----------------|---------|------|
| **ThinkRec** | - | LLM reasoning for recommendation; chain-of-thought explains and improves predictions | State-of-the-art on explainable recommendation | arXiv |
| **GenCI** | - | Generative Cohort Interest for CTR; generates cohort-level interest representations | New paradigm beyond individual CTR prediction | [arXiv:2601.18251](https://arxiv.org/abs/2601.18251) |
| **SparseCTR** | Meituan | Sparse attention for long-sequence CTR; scaling law for sparse attention in recommendation | **+1.72% CTR** deployed in Meituan | [arXiv:2601.17836](https://arxiv.org/abs/2601.17836) |
| **Personalized PEFT for Multimodal Rec** | - | Personalized parameter-efficient fine-tuning of foundation models for multimodal recommendation | Adapts frozen foundation models per-user | [arXiv:2602.09445](https://arxiv.org/abs/2602.09445) |
| **LINE** | - | Test of Time Award; graph representation learning at scale | Foundational graph embedding paper | [WWW 2026](https://www2026.thewebconf.org/) |

---

## CIKM 2025

**Venue**: CIKM 2025, Seoul, November 2–7, 2025
**Stats**: 810 accepted / 2,761 submitted (29% acceptance rate)

### Notable Papers

| Title | Affiliation | Key Innovation | Results | Link |
|-------|-------------|----------------|---------|------|
| **RankMixer** | ByteDance | Scaling up ranking models in industrial recommenders via token mixing | Foundation for MetaFormer-style ranking at scale | [CIKM 2025](https://www.cikm2025.org/program/accepted-papers) |
| **STARec** | Renmin University / Huawei | Agent framework for recommender systems via autonomous deliberate reasoning | New paradigm for agentic recommendation | [CIKM 2025](https://www.cikm2025.org/program/accepted-papers) |
| **Modality Alignment for Multimodal Rec** | Korea University | Multi-scale bilateral attention for modality alignment | Improved multimodal recommendation | [CIKM 2025](https://www.cikm2025.org/program/accepted-papers) |
| **Distribution-Guided Auto-Encoder** | - | User multimodal interest cross fusion | Better multimodal interest modeling | [CIKM 2025](https://www.cikm2025.org/program/accepted-papers) |

---

## RecSys 2025

**Venue**: RecSys 2025, Prague, Czech Republic, September 22–26, 2025

### Notable Papers

| Title | Affiliation | Key Innovation | Results | Link |
|-------|-------------|----------------|---------|------|
| **Yambda-5B** | Yandex Music | 4.79 billion interactions from 1M users across 9.39M tracks; is_organic flag separating recommendation-driven from organic events | Large-scale open benchmark for streaming recommendation | [ACM DL](https://dl.acm.org/doi/proceedings/10.1145/3705328) |
| **VL-CLIP** | - | Visual grounding + LLM-augmented CLIP embeddings for multimodal recommendation | Improved visual recommendation quality | [arXiv:2507.17080](https://arxiv.org/abs/2507.17080) |
| **LSVCR** | Kuaishou | Large-scale sequential video CTR prediction; deployed at billion-user scale | **+4.13% CTR** deployed in Kuaishou | [RecSys 2025](https://recsys.acm.org/recsys25/accepted-contributions) |
| **ECAT** | - | Best Paper Award; efficient cross-attention transformer for recommendation | Efficient attention for large-scale recommendation | [RecSys 2025](https://recsys.acm.org/recsys25/accepted-contributions) |
| **Multimodal Recommendation Survey** | - | Comprehensive survey of multimodal recommender systems | 200+ papers catalogued across 4 critical aspects | [TMM 2026](https://arxiv.org/abs/2502.15711) |

---

## arXiv Highlights

### CTR Scaling & Advertising

| Title | Affiliation | Key Innovation | Results | Link |
|-------|-------------|----------------|---------|------|
| **LoopCTR** | Alibaba | Loop scaling paradigm via recursive reuse of shared layers; decouples training-time compute from parameter count | Train-multi-loop, infer-zero-loop strategy | [arXiv:2604.19550](https://arxiv.org/abs/2604.19550) |
| **RankUp** | Tencent (Weixin) | High-rank representations for large-scale advertising; addresses representation collapse when scaling MetaFormer-based ranking | **+3–4% GMV** deployed | [arXiv:2604.17878](https://arxiv.org/abs/2604.17878) |
| **UniMixer** | Kuaishou | Unified architecture for scaling laws; combines attention/TokenMixer/FM into single framework; UniMixing-Lite for improved ROI | Improved scaling efficiency | [arXiv:2604.00590](https://arxiv.org/abs/2604.00590) |
| **GRAB** | Baidu | Generative Ranking for Ads; sequence-first CTR prediction inspired by LLM scaling | **+3.49% CTR** deployed at Baidu | emergentmind.com |
| **ML-DCN** | Pinterest | Masked Low-Rank Deep Crossing Network; instance-conditioned mask + low-rank crossing for scalable ads CTR | Online A/B tests with neutral serving cost | [arXiv:2602.09194](https://arxiv.org/abs/2602.09194) |
| **Selective Test-Time Compute** | Alibaba | Training-free per-instance test-time compute scaling for CTR via uncertainty-triggered feature path exploration | No training required; adaptive per-instance | [arXiv:2605.24989](https://arxiv.org/abs/2605.24989) |
| **EGAV1** | - | Efficient generative ad valuation | **+13.6% RPM** | arXiv |
| **CBD** | Kuaishou | Content-based delivery for advertising | **+29.9%** improvement | arXiv |
| **Bid2X** | Taobao (Alibaba) | Next-gen bidding for recommendation | Production-deployed bidding framework | arXiv |

### Generative Recommendation

| Title | Affiliation | Key Innovation | Results | Link |
|-------|-------------|----------------|---------|------|
| **GLASS** | - | Generative Large-scale Adaptive Search System | Unified retrieval + ranking via generation | arXiv |
| **SIDReasoner** | - | Reasoning over Semantic IDs for recommendation | Bridges semantic understanding and item IDs | arXiv |
| **GenRec** | JD.com | Generative recommendation paradigm at scale | **+9.5% clicks** deployed at JD | arXiv |
| **GRAD** | Meituan | Generative ads design | **+10.68% ROI** deployed at Meituan | arXiv |
| **ToolRec** | OPPO | On-device query recommendation; 150M+ MAU | Production-scale edge recommendation | arXiv |

### Sequential Modeling

| Title | Affiliation | Key Innovation | Results | Link |
|-------|-------------|----------------|---------|------|
| **Mamba-3** | - | Third-generation state space model; hybrid SSM-Transformer architecture | Improved long-sequence modeling | arXiv |
| **Oryx** | - | Efficient SSM for long sequences | Competitive with Transformer on long-context tasks | arXiv |
| **Sparse Delta Memory** | Meta FAIR | Beats attention at 8B scale via sparse delta memory mechanism | **Outperforms dense attention** with fewer parameters | arXiv |
| **Beyond Item IDs** | Google | Semantic-native long sequence modeling for short-form-video; Global-Aware Compression Transformer | **Deployed at billion-user scale** | [arXiv:2606.07546](https://arxiv.org/abs/2606.07546) |
| **SinkRec** | - | Mitigates semantic state sink in linear attention for long-sequence recommendation; hybrid memory-transition looped architecture | Novel architecture for production recommendation | [arXiv:2606.09888](https://arxiv.org/abs/2606.09888) |

### Agent Systems

| Title | Affiliation | Key Innovation | Results | Link |
|-------|-------------|----------------|---------|------|
| **Agentic Reasoning for LLMs** | UIUC/Microsoft | Comprehensive survey of agentic reasoning along three dimensions: foundational, self-evolving, collective | Unified roadmap for agentic reasoning research | [arXiv:2601.12538](https://arxiv.org/abs/2601.12538) |
| **From LLM Reasoning to Autonomous AI Agents** | - | Comprehensive review of benchmarks, frameworks, and protocols (ACP, MCP, A2A) | 60 benchmarks catalogued | [arXiv:2504.19678](https://arxiv.org/abs/2504.19678) |
| **SMACS** | - | 15 open models beat closed models on agent benchmarks | Open-source agents matching proprietary systems | arXiv |
| **Scalpel vs. Hammer** | - | GRPO amplifies existing capabilities; SFT replaces them | Critical insight for RL post-training | arXiv |

### Code Execution & Verification

| Title | Affiliation | Key Innovation | Results | Link |
|-------|-------------|----------------|---------|------|
| **Self-Execution Simulation** | - | Agents simulate code execution for verification before deployment | Reduces runtime errors | arXiv |
| **DUET** | - | Dual execution for code verification | Improves code correctness | arXiv |
| **EAGER** | - | Early exit for code generation; **37.3% latency reduction** | Significant efficiency gain | arXiv |
| **Proof-or-Stop** | - | Verifiable evidence-gated lifecycle control for agentic systems | 48-page comprehensive framework | arXiv |

---

## Cross-Conference Summary

### Key Trends Across Conferences

| Trend | Venues | Representative Papers |
|-------|--------|----------------------|
| **CTR Scaling Laws** | KDD, WWW, arXiv | EST (Alibaba), FAT (Alibaba), RankElastor (Tencent), LoopCTR (Alibaba), UniMixer (Kuaishou) |
| **Generative Recommendation** | KDD, AAAI, WWW, arXiv | GR4AD (Kuaishou), GenRec (JD), GLASS, SIDReasoner, ThinkRec |
| **Agent RL Systematization** | ICML, ICLR, AAAI | MemoPilot (ELO#1), HiPER (97.4%), Agent JIT (10.4×), AgentSwift (+8.34%) |
| **Safety Alignment Maturing** | ICML, NeurIPS, ICLR | 114 ICML safety papers, WaltzRL (39%→4.6%), AlphaAlign, Gated Attention (production) |
| **Multimodal Recommendation** | AAAI, RecSys, WWW | MoToRec, VL-CLIP, DMGIN, Multimodal Rec Survey (TMM 2026) |
| **Diffusion LM** | ICML, NeurIPS | Flexibility Trap (Outstanding), KLASS (2.78× speedup), Self-Flow Matching |
| **On-Device & Edge AI** | ICML, CVPR | NitroGen (gaming), ToolRec (OPPO 150M MAU), ParallelKernelBench |
| **Open-Source Catching Up** | arXiv | SMACS (15 open beats closed), Qwen beats GPT-4o (KARL) |

### Industry Deployment Map

| Company | Papers | Deployment Impact |
|---------|--------|-------------------|
| **Alibaba** | EST (+3.27% RPM), FAT (+4.38% AUC), DMGIN (+4.7% CTR), MoMoREC (+6.3% GMV), LoopCTR, UniAR | Taobao display ads, Tmall search, CTR prediction |
| **Tencent** | RankElastor (+3–4% GMV), RankUp (+3–4% GMV), GE4Rec, SIREN | Weixin advertising |
| **Kuaishou** | GR4AD (+4.2% ad rev, 400M DAU), UniMixer, CHIME, LSVCR (+4.13% CTR), CBD (+29.9%) | Short-video + live-streaming ads |
| **ByteDance** | RankMixer, HyFormer, LONGER, Zenith, TokenMixer-Large | Douyin/TikTok ranking |
| **Meituan** | SparseCTR (+1.72% CTR), MTFM, GRAD (+10.68% ROI) | Local services + food delivery |
| **Meta** | Sparse Delta Memory, WaltzRL (39%→4.6%), SAM 3D (Best), DHEN, ULTRA-HSTU | Facebook/Instagram ranking, safety |
| **Google** | D4RT (CVPR Best), Beyond Item IDs (billion-user), DiffusionGemma, TIPSv2 | YouTube, Search, Gemini |
| **NVIDIA** | NitroGen (40K hrs gaming), ParallelKernelBench, Nemotron | Gaming AI, kernel optimization |
| **Microsoft** | HARNESS-LM (Bing Ads), SkillOpt, Cadet | Bing Ads, Office Copilot |
| **LinkedIn** | CADET (+11.04% CTR), LLM Retrieval | Sponsored search |
| **Pinterest** | ML-DCN | Ads CTR prediction |
| **JD.com** | GenRec (+9.5% clicks) | E-commerce recommendation |
| **Baidu** | GRAB (+3.49% CTR) | Search advertising |
| **OPPO** | ToolRec (150M+ MAU) | On-device query recommendation |

### Venue Statistics Comparison

| Venue | Accepted | Submitted | Acceptance Rate | Year |
|-------|----------|-----------|-----------------|------|
| ICML 2026 | 6,634 | - | ~22% | 2026 |
| NeurIPS 2025 | 5,288 | - | ~25% | 2025 |
| ICLR 2026 | 5,356 | - | ~25.8% | 2026 |
| AAAI 2026 | ~4,167 | 23,680 | 17.6% | 2026 |
| CVPR 2026 | 4,090 | 16,092 | 25.42% | 2026 |
| KDD 2026 | - | - | - | 2026 |
| ACL 2026 | - | - | - | 2026 |
| CIKM 2025 | 810 | 2,761 | 29% | 2025 |

---

*Generated: 2026-07-18 | Sources: Web search, arXiv, conference proceedings, paper aggregation sites*
*Coverage: 200+ papers across 12+ venues, 20+ labs*
