---
title: "Conference Digest: Top ML/AI Conferences 2025-2026 — Full Edition"
type: synthesis
created: 2026-09-11
updated: 2026-09-11
sources: [conference-web-searches]
tags: [conference-digest, ICML2026, ICLR2026, AAAI2026, NeurIPS2025, KDD2026, CVPR2026, SIGIR2026, ACL2026, EMNLP2025, CIKM2025, RecSys2025, WWW2026, recommendation, LLM, advertising, CTR, agents, generative-models, sequential-modeling, games, code-execution, benchmarks]
---

# Conference Digest: Top ML/AI Conferences 2025-2026 — Full Edition

> Comprehensive compilation of papers from ICML 2026, ICLR 2026, NeurIPS 2025, CVPR 2026, KDD 2026, SIGIR 2026, ACL 2026, EMNLP 2025, WWW 2026, CIKM 2025, RecSys 2025. Structured by venue and category.

---

## 1. ICML 2026 (Seoul, Korea — Jul 6-12, 2026)

**Stats**: 23,918 submissions → 6,352 accepted (26.6%) → 536 spotlight (2.2%) → 168 oral (0.7%)

### 1.1 Outstanding Paper Awards

#### 1.1.1 The Flexibility Trap: Rethinking Arbitrary Order in Diffusion Language Models
- **Authors**: Zanlin Ni, Shenzhi Wang, Yang Yue, Tianyu Yu, Weilin Zhao, Yeguo Hua, Tianyi Chen, Jun Song, Cheng Yu, Bo Zheng, Gao Huang
- **Affiliation**: (Multiple institutions)
- **Key Innovation**: Challenges the assumption that arbitrary token order is always beneficial in diffusion language models (DLMs). Shows that fixed left-to-right RL rollouts can improve reasoning while preserving parallel decoding at inference.
- **Significance**: First systematic critique of a core DLM design assumption; suggests diffusion models may benefit from structured generation order.

#### 1.1.2 High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions
- **Authors**: Fan Chen, Sinho Chewi, Constantinos Daskalakis, Alexander Rakhlin
- **Key Innovation**: Achieves δ-error sampling in polylog(1/δ) steps — an exponential improvement over all previous results. Under minimal assumptions, complexity is Õ(d·polylog(1/δ)).
- **Significance**: First polylog(1/δ) complexity sampler for general log-concave distributions using only gradient evaluations.

#### 1.1.3 Outstanding Position Paper: The Alignment Community is Unintentionally Building a Censor's Toolkit
- **Authors**: Sarah Ball, Phil Hackemann
- **Key Innovation**: Argues alignment techniques are dual-use — tools built to constrain harmful model behavior can be repurposed for censorship.
- **Significance**: Raises critical ethical concern about the alignment research direction.

### 1.2 Honorable Mentions

| Paper | Theme | Key Finding |
|-------|-------|-------------|
| The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes | Alignment, reward hacking | Studies whether training against deception probes produces honest behavior or better evasion |
| Motion Attribution for Video Generation | Video generation | Tracks which training examples affect video generation quality |
| How Much Can Language Models Memorize? | Memorization | Sharper reasoning about what LLMs memorize vs generalize |
| A Random Matrix Perspective on Consistency of Diffusion Models | Diffusion theory | Explains why diffusion models produce similar outputs across runs |
| To Grok Grokking: Provable Grokking in Ridge Regression | Theory | Shows grokking-like behavior in simple linear settings |

### 1.3 Test of Time Award
- **Paper**: Asynchronous Methods for Deep Reinforcement Learning (A3C)
- **Authors**: Volodymyr Mnih, Adria Puigdomenech Badia, Mehdi Mirza, Alex Graves, Timothy P. Lillicrap, Tim Harley, David Silver, Koray Kavukcuoglu
- **Affiliation**: Google DeepMind

### 1.4 Oral Papers — Key Selected Works

| Paper | Authors | Affiliation | Innovation |
|-------|---------|-------------|------------|
| dnaHNet | Arnav Shah et al. | Stanford | Differentiable dynamic chunking for genomic sequences, >3× inference speedup |
| daVinci-Dev | Ji Zeng et al. | (Agentic SE) | Agent-native mid-training for software engineering; contextually-native + environmentally-native trajectories |
| Walrus | Michael McCabe et al. | (Astrophysics/Cosmo) | Cross-domain foundation model for continuum dynamics, 19 scenarios |
| UniAR | Wujian Peng et al. | Alibaba/Qwen | Unified multimodal autoregressive framework with single visual tokenizer |
| Set Diffusion | Marianne Arriola, Volodymyr Kuleshov | Cornell | Interpolating token orderings between AR and diffusion for fast decoding |
| Spurious Rewards | Rulin Shao et al. | (Multiple) | RLVR can elicit strong math reasoning even with spurious rewards |
| LIMSSR | Huangbiao Xu et al. | Peking Univ. | LLM-driven multimodal sequence-to-score reasoning under training-time incomplete observations |
| TabICooL | Jingang QU et al. | (Tabular FM) | Novel synthetic data + Muon optimizer for tabular foundation model |
| D2 | Guanghan Wang et al. | (Diffusion LM) | Reasoning framework for masked diffusion language models |

### 1.5 Spotlight Papers — Additional Highlights

| Paper | Theme | Key Finding |
|-------|-------|-------------|
| Detecting the Semantic Fixed Point | Early exit | Geometric criterion reduces FLOPs 30-35% while retaining >98% accuracy on LLaMA-2 |
| PlotCraft | Benchmark | 1k challenging visualization tasks for evaluating LLM data visualization |
| τ²-Bench | Agent eval | Dual-control telecom domain for evaluating conversational agents |
| Behavioral Plasticity in LLMs | Analysis | Token-conditional generation reveals intrinsic behavioral plasticity |
| Joint-Embedding Predictive Learning of Latent Market States | Finance | JEPA for useful representations of U.S. equity markets |

---

## 2. ICLR 2026 (Rio de Janeiro, Brazil — Apr 28 – May 2, 2026)

**Stats**: 19,525 submissions → 5,355 accepted (27.4%)

### 2.1 Outstanding Papers

#### 2.1.1 Transformers are Inherently Succinct
- **Authors**: Pascal Bergsträßer, Ryan Cotterell, Anthony Widjaja Lin
- **Key Innovation**: Proves that Transformers are inherently succinct — they can represent certain functions compactly that require exponentially more parameters for other architectures.

#### 2.1.2 LLMs Get Lost In Multi-Turn Conversation
- **Authors**: Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville
- **Key Innovation**: Systematic study showing LLMs degrade significantly in multi-turn conversations; identifies specific failure modes in contextual understanding across turns.

### 2.2 Honorable Mention

#### The Polar Express: Optimal Matrix Sign Methods and their Application to the Muon Algorithm
- **Authors**: Noah Amsel, David Persson, Christopher Musco, Robert M. Gower
- **Key Innovation**: Optimal polynomial approximations for matrix sign methods; theoretical foundation for the Muon optimizer used in modern deep learning.

### 2.3 Notable Papers

| Paper | Theme | Key Finding |
|-------|-------|-------------|
| Mamba-3 | Sequence modeling | Improved sequence modeling using state space principles |
| MemAgent | Long-context | Reshaping long-context LLM with multi-conv RL-based memory agent |
| Mixture-of-Experts Can Surpass Dense LLMs Under Strictly Equal Resource | MoE theory | Formal proof that MoE can outperform dense models under equal resource constraints |
| P-GenRM | Personalized rec | Personalized generative reward model with test-time user-based scaling |
| Verifying Chain-of-Thought Reasoning via its Computational Graph | Reasoning | CoT verification through computational graph analysis |
| Benchmarking Empirical Privacy Protection for LLMs | Privacy | Comprehensive privacy protection benchmark for LLM adaptations |
| SPIRAL | Multi-agent RL | Self-play on zero-sum games incentivizes reasoning via multi-agent multi-turn RL |
| FZOO | Optimization | Fast zeroth-order optimizer achieving Adam-scale speed for LLM fine-tuning |
| BARREL | Reasoning reliability | Boundary-aware reasoning for factual and reliable large reasoning models |
| DSA | Video generation | Distributed sparse attention for accelerating diffusion-based video generation |

---

## 3. NeurIPS 2025 (San Diego + Mexico City — Dec 2-7, 2025)

**Stats**: ~21,575 submissions → 5,200+ accepted (24.5%)

### 3.1 Best Paper Awards

#### 3.1.1 Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free (Best Paper)
- **Authors**: Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, Junyang Lin
- **Affiliation**: Alibaba/Qwen Team
- **Key Innovation**: Simple head-specific sigmoid gate after Scaled Dot-Product Attention consistently improves performance across 30 variants of 15B MoE and 1.7B dense models trained on 3.5T tokens.
- **Key Findings**: (1) Eliminates "attention sink" phenomenon; (2) Tolerates larger learning rates; (3) Reduces attention to first token from 46.7% to 4.8%; (4) <2% wall-time latency overhead.
- **Impact**: Already integrated into Qwen3-Next architectures; widely adopted as standard modification.

#### 3.1.2 1000 Layer Networks for Self-Supervised RL (Best Paper)
- **Authors**: Kevin Wang, Ishaan Javali, Michał Bortkiewicz, Tomasz Trzcinski, Benjamin Eysenbach
- **Key Innovation**: Increasing network depth to 1024 layers in self-supervised RL achieves 2-50× performance improvement on goal-conditioned tasks.
- **Significance**: Demonstrates that depth scaling, previously neglected in RL, is a critical factor for performance.

#### 3.1.3 Artificial Hivemind: The Open-Ended Homogeneity of Language Models (Best Paper)
- **Key Innovation**: First systematic study of LLM behavior on open-ended requests; shows LLMs converge on same ideas even when diverse solutions exist.

### 3.2 Best Paper Runners Up

| Paper | Theme | Key Finding |
|-------|-------|-------------|
| Optimal Mistake Bounds for Transductive Online Learning | Theory | Resolves 30-year-old open problem; exponential improvement in transductive mistake bounds |
| Superposition Yields Robust Neural Scaling | Scaling laws | Representation superposition explains neural scaling laws; open-source LLMs operate in strong superposition regime |
| Why Diffusion Models Don't Memorize | Diffusion | Implicit dynamical regularization prevents memorization; generalization window grows linearly with dataset size |

### 3.3 Additional Notable NeurIPS 2025 Papers

| Paper | Theme | Key Finding |
|-------|-------|-------------|
| TTRL (Test-Time RL) | Reasoning | Test-time reinforcement learning for reasoning improvement |
| Perception Encoder (Meta AI) | Multimodal | Large-scale perception encoder for multimodal understanding |
| In Search of Adam's Secret Sauce | Optimization | Extensive empirical study comparing Adam to simplified variants across 1500+ language models |
| Transformers Provably Learn CoT Reasoning | Theory | First optimization guarantee that constant-depth transformers provably learn NC1-complete problems with CoT |
| State Entropy Regularization | Robust RL | State entropy regularization improves robustness to structured perturbations |

---

## 4. CVPR 2026 (Denver, USA — Jun 3-7, 2026)

**Stats**: 16,092 submissions → 4,089 accepted (25.4%)

### 4.1 Best Paper Awards

#### 4.1.1 Efficiently Reconstructing Dynamic Scenes One D4RT at a Time (Best Paper)
- **Authors**: Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco et al.
- **Affiliation**: Google DeepMind, UCL, University of Oxford
- **Key Innovation**: D4RT — unified transformer-based architecture estimating depth, spatio-temporal correspondence, and camera parameters for dynamic 4D scene reconstruction from video.

#### 4.1.2 Native and Compact Structured Latents for 3D Generation (Best Student Paper)
- **Authors**: Jianfeng Xiang, Xiaoxue Chen, Sicheng Xu et al.
- **Affiliation**: Tsinghua University, Microsoft Research, USTC, Microsoft AI
- **Key Innovation**: O-Voxel representation capturing complex shapes and surface attributes; TRELLIS.2 framework significantly advancing 3D generative modeling.

### 4.2 Best Paper Honorable Mentions

#### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang et al.
- **Affiliation**: NVIDIA, Stanford, Caltech, Chicago, UT Austin
- **Key Innovation**: Vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games; exhibits strong cross-domain gaming competence.

#### SAM 3D: 3Dfy Anything in Images
- **Authors**: Xingyu Chen et al.
- **Affiliation**: Meta Superintelligence Labs
- **Key Innovation**: Generative model for visually grounded 3D object reconstruction; 5:1 win rate in human preference tests.

### 4.3 Key Research Trends at CVPR 2026

| Theme | Share Change YoY | Representative Papers |
|-------|-------------------|---------------------|
| Multimodal LLMs/VLMs | 4.9% → 10.6% (+5.7pp) | HiSpatial, LLaDA-V, PersonaVLM |
| Video Generation & World Models | 3.8% → 8.8% (+5.0pp) | ARCache, GenieDrive, SURF |
| Embodied AI & Robotics | 2.9% → 6.2% (+3.3pp) | DrivePI, Visual Sim-to-Real, Gallant |
| Classic CV (detection/seg/tracking) | 3.8% → 1.2% (-2.6pp) | Declining share |

---

## 5. KDD 2026 (Jeju Island, Korea — Aug 9-13, 2026)

**Stats**: 1,215+ submissions (first cycle) → 256 accepted (21%); total conference ~1,400+ papers across all tracks

### 5.1 Keynote Speakers
- Jeff Dean (Google Chief Scientist)
- Jingren Zhou (Alibaba Chief AI Architect)
- Regina Barzilay (MIT)

### 5.2 Notable Papers

| Paper | Authors/Affiliation | Key Innovation | Online Results |
|-------|---------------------|----------------|----------------|
| HOBA: Hierarchical On-Policy Bidding Agents | Kuaishou | Three-level bidding: LLM hour-level constraints + causal SARSA expert selection + PID/MPC/IQL expert pool | +3.6% target cost, +8.1% conversion value |
| GR4AD: Generative Recommendation for Ads | Kuaishou | Unified semantic ID (UA-SID) + LazyAR + value-aware SL + RSPO | Up to +4.2% revenue |
| FlowTime | Kuaishou | Continuous generative regression via VAE + normalizing flows for watch-time | Significant watch time improvement |
| OneRank | Alibaba | Unified Transformer-native ranking for recommendation | Deployed at scale |
| VideoRAG | Xubin Ren et al. | RAG framework for extreme long-context videos | New paradigm for video understanding |
| GenCI | WWW 2026 | Generative user intent via cohort-based learning for CTR | Consistently outperforms SOTA baselines |
| MAC: CTR Benchmark | Multiple | Multiple attribution mechanisms for CTR prediction | MoAE architecture |
| REALM-Bench | Multiple | Multi-agent system benchmark for real-world planning | Comprehensive evaluation framework |

### 5.3 Industry Papers

| Company | Paper | Key Result |
|---------|-------|------------|
| Pinterest | Pinterest Canvas | 18.0% engagement lift (background), 12.5% (outpainting) |
| LinkedIn | Hierarchical Long-Term Semantic Memory | +5% answer correctness, +10% retrieval F1 |
| Alibaba | PerFusion | +13% CTR and conversion rate |
| ByteDance | One Model, Multiple Goals | Adaptive multi-objective e-commerce dialogue |
| Amazon | ColdNet | Treatment effect estimation for cold-start |

### 5.4 KDD Cup 2026
- Tencent UNI-REC Challenge (large-scale recommendation)
- HKUST Data Agents Challenge (autonomous data analysis)

---

## 6. SIGIR 2026 (Melbourne, Australia — Jul 20-24, 2026)

### 6.1 Notable Papers

| Paper | Affiliation | Key Innovation |
|-------|-------------|----------------|
| GenRec | JD.com | Preference-oriented generative retrieval with GRPO-SR; +9.5% clicks, +8.7% transactions in online A/B |
| L2Rec | (Multiple) | Dual-view understanding (behavioral + semantic) via DPMoE; +0.72% CTR online |
| InvariRank | (LLM Rec) | Permutation-invariant listwise LLM reranking via architectural enforcement |
| ItemRAG | (Multiple) | Item-level RAG shifting from coarse user-history to fine-grained item retrieval |
| ProMax | (Multiple) | LLM-derived profiles with distribution reshaping; +8.44% NDCG@10 over best baseline |
| OnePass | (Netflix-style) | Position-invariant listwise reranking for LLM-based recommendation |
| GenRec | JD.com | Generative retrieval with preference alignment; offline + online validated |

---

## 7. ACL 2026 (San Diego, USA — Jul 2-7, 2026)

**Stats**: 12,148 submissions → 2,296 main accepted (18.9%) → 2,163 Findings; 504 oral presentations

### 7.1 Best Paper Awards

#### The Imperfective Paradox in Large Language Models
- **Key Innovation**: Investigates the Imperfective Paradox — LLMs systematically hallucinate completion for goal-oriented events, revealing they operate as predictive narrative engines rather than logical reasoners.

### 7.2 Key Trends

| Theme | 2025 Papers | 2026 Papers | Change |
|-------|-------------|-------------|--------|
| LLM Reasoning, Agents, Tool Use | 142 | 366 | +224 (+8.2pp) |
| Model Training, Fine-tuning, RL | 196 | 295 | +99 (+1.2pp) |
| RAG, QA, Knowledge Editing | 174 | 244 | +70 (+0.2pp) |
| Multimodal, Vision-Language | 79 | 116 | +37 (+0.4pp) |

### 7.3 Notable Papers

| Paper | Theme | Key Finding |
|-------|-------|-------------|
| PaCoRe: Parallel Coordinated Reasoning | Reasoning | 8B model reaches 94.5% on HMMT 2025, surpassing GPT-5 (93.2%) via 2M-token effective TTC |
| Disco-RAG | RAG | Discourse-aware RAG with rhetorical structure theory; +12.74 points LLM Score on Loong |
| Compositional Steering Tokens | Alignment | Multi-behavior steering via input-space tokens; generalizes to unseen compositions |
| SADA: State-Aligned Distillation Adapters | Efficiency | Bridges ICL and fine-tuning; comparable to ICL with reduced memory/latency |
| ChiKhaPo | Multilingual | 2700+ language benchmark for lexical comprehension and generation |

---

## 8. EMNLP 2025

### 8.1 Notable Papers

| Paper | Theme | Key Finding |
|-------|-------|-------------|
| KOPA-Bench + EDGE | Tool calling | Korean public API multi-step tool calling; GRPO 9B ≈ untuned 27B |
| TRILOGUE | Multilingual | Trilingual (EN/RU/KZ) spoken dialogue fact-checking |
| RefactorPlatform | Code agents | Repository-level refactoring; RAG single agent 86% vs sub-agent 66% |
| PRAGMA | Agent memory | Personalized memory alignment for lifelong conversations |
| JarvisGUI | GUI agents | Cross-device GUI agents |

---

## 9. WWW 2026 (Dubai, UAE — Apr 13-17, 2026)

### 9.1 Notable Papers

| Paper | Affiliation | Key Innovation |
|-------|-------------|----------------|
| GraphRAG-R1 | (Multiple) | Process-constrained RL for graph RAG; +38-84% F1 on multi-hop QA |
| Context-Aware Graph RAG | (Multiple) | Unified framework for context-aware and relation-aware graph retrieval |
| GenCI | (CTR) | Generative user intent framework for CTR prediction |
| CRS: Context-aware Reasoning for Search | E-commerce | Self-evolving post-training with SFT+RL for search-based recommendation |
| PLUM | Spotify | Adapting pre-trained LMs for industrial-scale generative recommendations |

---

## 10. CIKM 2025 (Seoul, Korea — Nov 10-14, 2025)

**Stats**: 2,890 submissions → 870 papers accepted (30% overall)

### 10.1 Best Paper Awards

| Award | Paper | Key Finding |
|-------|-------|-------------|
| Best Full Paper | Reconsidering Performance of GAE in Link Prediction | Warns about over-claiming improvements in GNN link prediction |
| Best Applied Research | Climber: Efficient Scaling Laws for Large Rec Models | Deployed on NetEase Cloud Music serving tens of millions daily |
| Best Resource Paper | Generative Recommendation with Semantic IDs: A Practitioner's Handbook | GRID open-source framework for GR with SIDs |

---

## 11. RecSys 2025 (Prague, Czech Republic — Sep 22-26, 2025) & RecSys 2026 (Minneapolis — Sep 28 – Oct 2, 2026)

### 11.1 Notable Work (SIGIR/RecSys 2025-2026)

| Paper | Theme | Key Finding |
|-------|-------|-------------|
| GenRec (JD.com, SIGIR'26) | Generative rec | Preference-oriented GR with GRPO-SR; +9.5% clicks online |
| OneRank (Alibaba, KDD'26) | Unified ranking | Transformer-native ranking for recommendation at scale |
| IntuRec (KDD'26) | Latent reasoning | Latent reasoning for recommendation |
| Climber-Pilot (KDD'26) | Non-myopic rec | Non-myopic generative recommendation |

---

## 12. Cross-Conference Themes

### 12.1 Recommendation Systems — Production Deployments

| System | Company | Venue | Key Metric |
|--------|---------|-------|------------|
| GR4AD | Kuaishou | KDD'26 | +4.2% revenue (generative ads) |
| HOBA | Kuaishou | KDD'26 | +3.6% target cost (bidding) |
| GenRec | JD.com | SIGIR'26 | +9.5% clicks (generative retrieval) |
| UniCon | Meituan | arXiv 2026 | +3.09% RPM (context-centric CTR) |
| ReST | Baidu | arXiv 2026 | +11.93% revenue (sequence transformers) |
| TGR | Tencent | arXiv 2026 | +3.57% CTR (generative ranking) |
| CADET | LinkedIn | arXiv 2026 | +11.04% CTR (decoder-only) |
| EST | Alibaba | arXiv 2026 | +3.27% RPM (CTR scaling) |

### 12.2 LLM Reasoning & Post-Training

| Paper | Venue | Key Innovation |
|-------|-------|----------------|
| PaCoRe | ACL'26 | 8B model surpasses GPT-5 on HMMT via parallel coordinated reasoning |
| Gated Attention | NeurIPS'25 | Simple sigmoid gate eliminates attention sink, improves scaling |
| The Flexibility Trap | ICML'26 | Challenges DLM arbitrary order assumption |
| Spurious Rewards | ICML'26 | RLVR elicits strong math reasoning even with spurious rewards |
| Uncertainty-Aware RM | arXiv | Calibrated uncertainty in reward models prevents reward hacking |
| MeRLa | arXiv | Meta-learned reward shaping; 90.8% LC win rate on AlpacaEval 2.0 |
| CausalRM | arXiv | Factored causal representation learning for robust reward modeling |

### 12.3 Agent Systems & Tool Use

| Paper | Venue | Key Innovation |
|-------|-------|----------------|
| NitroGen | CVPR'26 | Foundation model for generalist gaming agents (40K hours, 1000+ games) |
| daVinci-Dev | ICML'26 | Agent-native mid-training for software engineering |
| Procedural Graphs | arXiv | Self-evolving execution structures for LLM agents |
| HEART | arXiv | Tool primitives + ToolFace repository; outperforms GPT-5.4/Claude-4.6 |
| A-MLE | arXiv | Agentic ML exploration for ads ranking automation |
| DMRL | arXiv | Document-mediated RL for skill optimization in ads |

### 12.4 Generative Models & Diffusion

| Paper | Venue | Key Innovation |
|-------|-------|----------------|
| High-Accuracy Sampling | ICML'26 | Exponential improvement in diffusion sampling efficiency |
| D4RT | CVPR'26 | Dynamic 4D scene reconstruction from video |
| SAM 3D | CVPR'26 | Single-image 3D reconstruction (Meta) |
| Set Diffusion | ICML'26 | Interpolating AR and diffusion for fast decoding |
| LLaDA-V | CVPR'26 | Large language diffusion models with visual instruction tuning |

### 12.5 CTR Prediction & Feature Interaction

| Paper | Venue | Key Innovation |
|-------|-------|----------------|
| CADET | arXiv | Decoder-only transformer for CTR; self-gated attention + timestamp RoPE |
| UniCon | arXiv | Unified context-centric architecture for CTR |
| PRIME | arXiv | Plug-in residual input-conditioned MoE for CTR top networks |
| GRAB | arXiv | LLM-inspired sequence-first CTR at Baidu (+3.05% revenue) |
| GenCI | WWW'26 | Generative cohort-based intent learning for CTR |
| PaletteID | arXiv | Prototype-composed semantic identifiers for multimodal CTR |
| FAT | KDD'26 | Field-aware transformer with CTR scaling law (Alibaba) |

### 12.6 Games & Code Execution

| Paper | Venue | Key Innovation |
|-------|-------|----------------|
| NitroGen | CVPR'26 | Open foundation model for generalist gaming agents |
| τ²-Bench | ICML'26 | Dual-control environment for evaluating conversational agents |
| CIRBench | ICML'26 | Evaluating LLMs as LLVM IR optimizers |
| SPIRAL | ICLR'26 | Self-play on zero-sum games incentivizes reasoning |
| GPU-CFR | arXiv | 80× CFR speedup via CUDA graphs |
| Procedural Graphs | arXiv | Self-evolving execution structures for agents |
| Speculative Uncertainty | arXiv | Failure prediction for agentic coding without logits |

---

## 13. Key Industry Lab Highlights

### Google DeepMind
- **CVPR 2026**: D4RT Best Paper (dynamic 4D reconstruction)
- **NeurIPS 2025**: Gated Attention collaboration (Qwen team)
- **ICML 2026**: Test of Time Award (A3C)

### Meta AI
- **CVPR 2026**: SAM 3D Best Paper Honorable Mention
- **NeurIPS 2025**: Perception Encoder

### Alibaba/Qwen
- **NeurIPS 2025**: Gated Attention Best Paper (Qwen Team)
- **ICML 2026**: UniAR (unified multimodal AR)
- **KDD 2026**: OneRank (unified ranking), PerFusion (+13% CTR)

### ByteDance/Douyin
- **RecSys 2026**: SequenceO1 (100K ultra-long sequences)
- **KDD 2026**: One Model Multiple Goals

### Kuaishou
- **KDD 2026**: 25 papers accepted, 3 oral; HOBA (+3.6% target cost), GR4AD (+4.2% revenue), FlowTime

### Tencent
- **KDD 2026**: TGR (generative recommendation framework), PRIME

### Baidu
- **KDD 2026**: GRAB (+3.05% revenue, sequence-first CTR)

### LinkedIn
- **KDD 2026**: Hierarchical Long-Term Semantic Memory (+5% answer correctness)
- **arXiv**: CADET (+11.04% CTR, decoder-only)

### Meituan
- **arXiv**: UniCon (+3.09% RPM), SparseCTR (WWW'26)

### NVIDIA
- **CVPR 2026**: NitroGen Best Paper Honorable Mention

---

## References

- ICML 2026: https://icml.cc/virtual/2026/
- ICLR 2026: https://iclr.cc/virtual/2026/
- NeurIPS 2025: https://neurips.cc/virtual/2025/
- CVPR 2026: https://cvpr.thecvf.com/Conferences/2026/
- KDD 2026: https://kdd2026.kdd.org/
- SIGIR 2026: https://sigir.org/sigir-2026/
- ACL 2026: https://2026.aclweb.org/
- WWW 2026: https://www2026.thewebconf.org/
- CIKM 2025: https://cikm2025.org/
- RecSys 2025: https://recsys.acm.org/recsys25/
