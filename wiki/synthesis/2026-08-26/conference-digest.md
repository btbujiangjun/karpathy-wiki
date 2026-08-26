---
title: "Conference & arXiv Daily Digest — 2026-08-26"
type: synthesis
created: 2026-08-26
updated: 2026-08-26
sources: []
tags: [conference-digest, icml-2026, iclr-2026, aaai-2026, neurips-2025, cvpr-2026, kdd-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2025, recsys-2025, recommendation, llm, agents, ctr, advertising, generative-models, sequential-modeling, games, code-execution, daily-digest]
---

# Conference & arXiv Daily Digest — 2026-08-26

> Comprehensive survey of recent papers from top ML/AI conferences (2025–2026 cycle) and latest arXiv preprints. Organized by venue and category. Focus on papers from top labs: Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, Netflix, NVIDIA, Anthropic, Apple, Amazon.

---

## 📊 Conference Overview (2025–2026 Cycle)

| Conference | Dates | Location | Papers Submitted | Papers Accepted | Acceptance Rate |
|-----------|-------|----------|-----------------|----------------|-----------------|
| ICML 2026 | Jul 6–12, 2026 | Hawaii | 23,918 | 6,352 | ~26.6% |
| ICLR 2026 | Apr 23–27, 2026 | Rio de Janeiro | ~12,000+ | 5,300+ | ~44% |
| AAAI 2026 | Jan 20–27, 2026 | Singapore | 29,000 | 4,300+ | ~14.8% |
| NeurIPS 2025 | Dec 2025 | San Diego | ~15,000+ | ~3,500+ | ~23% |
| CVPR 2026 | Jun 3–9, 2026 | Denver | 16,092 | 4,089 | ~25.4% |
| KDD 2026 | Aug 9–13, 2026 | Jeju | TBD (Cycle 1+2) | TBD | TBD |
| ACL 2026 | Jul 2–7, 2026 | San Diego | 12,148 | 4,459 (Main+Findings) | 18.9% (Main) |
| EMNLP 2025 | Nov 4–9, 2025 | Suzhou | ~10,000+ | 2,088+ | ~21% |
| WWW 2026 | Jun 29–Jul 3, 2026 | Virtual | 3,370 | 676 | 20% |
| SIGIR 2026 | TBD | TBD | TBD | TBD | TBD |
| CIKM 2025 | 2025 | TBD | 1,627 | 443 | 27.2% |
| RecSys 2025 | 2025 | TBD | ~850+ | ~179+ | ~21% |

---

## 🏆 CVPR 2026 — Best Paper Awards & Highlights

### Best Paper: Efficiently Reconstructing Dynamic Scenes One D4RT at a Time
- **Title**: D4RT: Efficiently Reconstructing Dynamic Scenes One D4RT at a Time
- **Authors**: Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, Liliane Momeni, Junyu Xie, Shuyang Sun, Rahul Sukthankar, Joëlle K. Barral, Raia Hadsell, Zoubin Ghahramani, Andrew Zisserman, Junlin Zhang, Mehdi S. M. Sajjadi
- **Affiliation**: Google DeepMind, University College London, University of Oxford
- **Venue**: CVPR 2026
- **Key Innovation**: Unified transformer-based architecture for dynamic 4D reconstruction and tracking from video. Estimates depth, spatio-temporal correspondence, and full camera parameters in a single feedforward pass. Lightweight decoder queries 3D position of any point across space and time. Significantly simpler and more scalable than traditional multi-stage pipelines.
- **Link**: [CVPR 2026 Best Paper](https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers)

### Best Student Paper: Native and Compact Structured Latents for 3D Generation
- **Title**: O-Voxel (TRELLIS.2)
- **Authors**: Jianfeng Xiang, Xiaoxue Chen, Sicheng Xu, Ruicheng Wang, Zelong Lv, Yu Deng, Hongyuan Zhu, Yue Dong, Hao Zhao, Nicholas Jing Yuan, Jiaolong Yang
- **Affiliation**: Tsinghua University, Microsoft Research, University of Science and Technology of China, Microsoft AI
- **Venue**: CVPR 2026
- **Key Innovation**: O-Voxel sparse omni-voxel representation encoding both geometry and appearance for 3D generation. Sparse Compression VAE produces compact latent space; 4B-parameter flow-matching model generates high-quality 3D assets. Significant gains in geometry and material quality.

### Best Paper Honorable Mention: SAM 3D
- **Title**: SAM 3D: 3Dfy Anything in Images
- **Authors**: Xingyu Chen, Fu-Jen Chu, Pierre Gleize, Kevin J. Liang, Alexander Sax, Hao Tang, Weiyao Wang, Michelle Guo, Thibaut Hardin, Xiang Li, Aohan Lin, Jia-Wei Liu, Ziqi Ma, Anushka Sagar, Bowen Song, Xiaodong Wang, Jianing Yang, Bowen Zhang, Piotr Dollár, Georgia Gkioxari, Matt Feiszli, Jitendra Malik
- **Affiliation**: Meta Superintelligence Labs
- **Venue**: CVPR 2026
- **Key Innovation**: Generative model for visually grounded 3D object reconstruction from single images. Predicts geometry, texture, and layout. Human-in-the-loop annotation with model proposals + human selection. At least 5:1 win rate in human preference tests on real-world objects.

### Best Paper Honorable Mention: NitroGen
- **Title**: NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: NVIDIA, Stanford, Caltech, University of Chicago, UT Austin et al.
- **Affiliation**: NVIDIA
- **Venue**: CVPR 2026
- **Key Innovation**: Foundation model for generalist gaming agents trained via internet-scale vision-action learning. 52% relative improvement in unseen game win rates vs. training from scratch.

### CVPR 2026 Highlighted Papers — Generative Models
| Paper | Key Innovation | Affiliation |
|-------|---------------|-------------|
| Transition Models (TiM) | Arbitrary-step transitions in generative modeling; 865M params surpasses SD3.5 (8B) and FLUX.1 (12B) | - |
| PixelDiT | Single-stage pixel-space diffusion transformer; FID 1.61 on ImageNet 256 | - |
| Improved MeanFlow (iMF) | Velocity prediction reformulation + guidance-scale conditioning; 1-step FID 2.74 on ImageNet 256 | - |
| VMonarch | Structured Monarch matrix attention for Video DiTs; sub-quadratic attention | - |
| LLSA (Log-linear Sparse Attention) | Hierarchical Top-K selection; reduces attention from quadratic to log-linear | - |
| UltraFlux | Data-model co-design for native 4K T2I; Resonance 2D RoPE + SNR-Aware Huber Wavelet | - |

---

## 🏆 ACL 2026 — Best Paper Awards & Highlights

### Best Papers (3 awards)
1. **The Imperfective Paradox in Large Language Models** — Bolei Ma, Yusuke Miyao (LMU Munich / University of Tokyo)
   - Exposed "teleological bias" in LLMs: they assume goal-oriented actions succeed even without evidence. 7B–9B models systematically violate event-entailment patterns. Scale helps in Qwen family (1.5B→32B).

2. **Memory Efficiency and Resource-Rational Encoding in Sentence Processing** — Weijie Xu, Brian Dillon, Richard Futrell (UC Irvine / UMass Amherst)
   - Constraining Transformer memory with noise injection mimicking human working memory limits produces more human-like representations. Precision decay learning emerges naturally under resource cost.

3. **Characterizing the Expressivity of Local Attention in Transformers** — Jiaoda Li, Ryan Cotterell (ETH Zurich)
   - Proved local attention strictly increases Transformer expressive power via formal language theory. Global+local hybrid is strictly richer than either alone.

### ACL 2026 — Outstanding Papers (selected)
| Paper | Category | Key Finding |
|-------|----------|-------------|
| Evolutionary Guided Decoding | RLVR | Iterative value refinement for LLM decoding |
| Rethinking Entropy Interventions in RLVR (STEER) | RLVR | Token-level reweighting stabilizes entropy dynamics |
| GeoRA: Geometry-Aware LoRA for RLVR | RLVR | SVD-based adapter init in geometrically constrained subspace |
| CAR-bench | Agents | BMW in-car assistant benchmark; best agent pass@3 high but pass³ poor (0.42 max consistency) |
| MediEval | Benchmark | Links MIMIC-IV EHRs to medical knowledge base; CoRFu DPO method +16.4 macro-F1 |
| Mind the (DH) Gap | Safety | Reasoning models rational; conversational models human-like risk-averse |
| Lying with Truths | Safety | Multi-agent collusion via truthful evidence montage; 70%+ success across 14 LLM families |
| CxMP | Linguistics | Construction Grammar benchmark; syntactic competence emerges early, constructional understanding lags |
| Mapping the Circumplex of Affect | Best Theme | Hyperspherical contrastive learning for emotion representations |

### ACL 2026 — Key Statistics
- **12,148 submissions** → 2,296 main conference + 2,163 findings = 4,459 total accepted
- **Main acceptance rate**: 18.9%
- **54% of authors from Mainland China**
- **LLM/LLMs in 23% of titles**, "Reasoning" in 18%, "Multi" in 11%
- New tracks: AI/LLM Agents, LLM Safety & Alignment, Mathematical & Symbolic Reasoning, Code Models, LLM Efficiency

---

## 🏆 ICML 2026 — Key Papers

### Reproducibility: HuggingFace Reproduces 2,200+ ICML Papers
- 1,221 community members, 6,816 reproduction logbooks
- 2,226 papers attempted (34% of conference), 35,908 claims judged
- 51% of papers had at least one claim verified; 266 fully reproduced
- **Key finding**: 51% verification rate suggests AI research reproducibility is improving with agent-based verification

### Selected ICML 2026 Papers
| Paper | Key Innovation | Category |
|-------|---------------|----------|
| High-accuracy sampling for diffusion models | Polylog(1/δ) complexity sampler; exponential improvement over prior work | Generative Models |
| Rethinking Hardness of PbRL | Dual Episodic Eluder Dimension (DEED); √T regret for preference-based RL | RL Theory |
| Nonparametric LLM Evaluation from Preference Data | DMLRank framework; generalized ranking scores (GARS) for LLM leaderboards | Evaluation |
| Outcome-Aware Spectral Feature Learning | Augmented spectral features for causal IV regression | Causal Inference |
| Respecting Modality Gap in OOD Detection | Online pseudo-supervised visual prototype learning; SOTA OOD detection | Vision-Language |

---

## 🏆 ICLR 2026 — Key Papers

### SphereAR: Hyperspherical Latents for Autoregressive Image Generation
- **Authors**: Guolin Ke (DP Technology), Hui Xue (Microsoft Research)
- **Affiliation**: Microsoft Research
- **Key Innovation**: Hyperspherical VAE constrains AR inputs/outputs to fixed-radius hypersphere. SphereAR-H (943M) achieves FID 1.34 on ImageNet 256×256 — **first pure next-token AR generator to surpass diffusion and masked-generation models at comparable scale**.

### In-Context Policy Optimization (ICPO) / ME-ICPO
- **Affiliation**: Salesforce Research, others
- **Key Innovation**: Theoretical framework for test-time self-reflection in LLMs. Single-layer linear self-attention provably imitates policy optimization. ME-ICPO achieves competitive math reasoning with affordable inference costs.

### OpenThoughts: Data Recipes for Reasoning Models
- **Key Innovation**: Open-source data recipes for training reasoning models; systematic study of data composition for reasoning.

### Robustness of Reasoning LLMs
- **Paper**: Are Reasoning LLMs Robust to Interventions on Their Chain-of-Thought?
- **Key Finding**: Investigates whether CoT reasoning is robust to perturbations — relevant to safety and reliability.

---

## 🏆 AAAI 2026 — Key Papers

### SPIRAL: Symbolic LLM Planning via Grounded and Reflective Search
- **Affiliation**: IBM Research
- **Key Innovation**: Embeds 3 LLM agents (Planner/Simulator/Critic) in MCTS loop. 83.6% accuracy on DailyLifeAPIs, +16pp over next-best. Transforms MCTS from brute-force to guided self-correcting reasoning.

### Bonsai: Interpretable Tree-Adaptive Grounded Reasoning
- **Affiliation**: Johns Hopkins / others
- **Key Innovation**: Compositional probabilistic reasoning with retrieval-augmented evidence. Tunable at test-time via evidence scaling. Handles transcripts, photos, video, audio, databases.

### Length-Adaptive Interest Network (for CTR Prediction)
- **Key Innovation**: Balances long and short sequence modeling in CTR prediction; adaptive length selection.

---

## 🏆 NeurIPS 2025 — Key Trends

### Gated Attention (Best Paper)
- **Key Innovation**: Gated attention mechanism for efficient Transformer computation.

### Scale & Performance
- Focus on scaling laws, efficient training, and reasoning capabilities
- Strong representation in multimodal learning and reinforcement learning

---

## 🏆 WWW 2026 — Recommendation & Web

### Statistics
- 3,370 submissions → 676 accepted (20% acceptance rate)
- **Recommendation**: Largest track with 110 papers
- **Graph Algorithms**: 99 papers
- **Security & Privacy**: 88 papers

### Key Recommendation Papers
| Paper | Key Innovation |
|-------|---------------|
| Diffusion Generative Recommendation with Continuous Tokens (ContRec) | LLM-based RecSys with continuous token integration |
| GenRec (Netflix) | LLM-backed recommendation ranker; prefill-only inference; +1.6% MRR offline |
| ReasonRec | Reasoning-augmented multimodal agent for unified recommendation; 30%+ improvement |
| CoRRe | Training-free LLM recommendation with post-LLM item refinement using collaborative signals |

---

## 🏆 KDD 2026 — Industrial AI

### Conference Info
- **Dates**: Aug 9–13, 2026, Jeju, Korea
- **Two submission cycles per year** (new format)
- Topics: Knowledge discovery, data science, AI applications

---

## 🏆 EMNLP 2025 — NLP

### Key Trends
- StepSearch: Step-Wise PPO for LLM search ability
- RECALL: Representation-aligned catastrophic-forgetting alleviation via hierarchical model merging
- Strong focus on reasoning, agents, and tool use

---

## 🏆 CIKM 2025 & RecSys 2025

### CIKM 2025
- 1,627 submissions → 443 accepted (27.2%)
- Focus on information retrieval, knowledge management

### RecSys 2025
- Key papers from Kuaishou, Amazon, Tsinghua
- RESEnhancing Sequential Recommender with LLMs (Kuaishou)
- GenSAR: Generative Search and Recommendation (Kuaishou)
- LEAF: Lightweight Embedding for Large-Scale Recommendation

---

## 🔬 Latest arXiv Preprints — Industry & Research Labs

### 🔴 Netflix
#### GenRec: An LLM-Backed Recommendation Ranker
- **Authors**: Netflix Research team
- **Affiliation**: Netflix
- **Problem**: Traditional recommendation stacks use feature engineering; LLMs can shift to context engineering.
- **Methodology**: Two-phase framework — Phase 1 adapts open-source LLM to Netflix data; Phase 2 post-trains with recommendation-specific data and reward signals. Catalog-aware ranking head enables single-forward-pass ranking. Prefill-only inference for cost efficiency.
- **Key Results**: +1.6% MRR offline with 40× less Phase-2 labeled data than production model. Statistically significant improvement in large-scale A/B test (10% traffic, 4 weeks).
- **Innovation**: Context engineering over feature engineering; shared foundation backbone replacing bespoke architectures.
- **Link**: [arXiv:2608.10257](https://arxiv.org/abs/2608.10257)

### 🔴 Google DeepMind
#### Scaffolding Minds: Optimizing Latent Visual Target Representations for Multimodal Reasoning
- **Authors**: Haoqiang Kang, Yinpeng Chen, Luyang Liu et al.
- **Affiliation**: Google DeepMind
- **Problem**: Latent visual reasoning has limitations in both SFT (suboptimal vision encoder targets) and RL (deterministic regularization without exploration).
- **Methodology**: Learns a scaffolding encoder for optimized latent targets + Scaffolding RL with learned Gaussian policy for residual latent actions. Two-stage complementary improvements.
- **Key Results**: +9.5% on FrozenLake (widening to +19% at 32×32); +5.2% average across 9 visual reasoning benchmarks.
- **Link**: [arXiv:2608.19669](https://arxiv.org/abs/2608.19669)

#### Recirculation: Training-Free Recurrence for Transformers
- **Authors**: Michael C. Mozer, Shoaib Ahmed Siddiqui et al.
- **Affiliation**: Google DeepMind
- **Problem**: Feedforward transformers have bounded state updates due to fixed depth.
- **Methodology**: Inference-time architectural enhancement adding recurrence without retraining. Adaptive variant tunes hyperparameters while freezing original weights.
- **Key Results**: 23% perplexity reduction on Gemma3 family; 21% accuracy increase on GSM8k; training-free.
- **Link**: [arXiv:2608.17981](https://arxiv.org/abs/2608.17981)

#### WhiteMatter: All-to-All Cross-Layer Connections via KV Mixing
- **Affiliation**: Google DeepMind
- **Problem**: Each Transformer layer only attends to its own KV; deeper representations unavailable to shallow layers.
- **Methodology**: Router mixes all L layer states into k shared KV channels per token. Consumer layers select channels. Full-cache lowers perplexity 8.2% over vanilla; half-cache retains 6.3% reduction.
- **Link**: [arXiv:2608.18486](https://arxiv.org/abs/2608.18486)

#### Proteus: Incremental Memory Activation for Long-Context Sequence Modeling
- **Affiliation**: Google DeepMind / Others
- **Problem**: Static memory capacity in recurrent models is suboptimal for long contexts.
- **Methodology**: Progressively expands effective memory capacity as context grows. Applied to SWLA, Comba, Titans, and Hope-Attention with no additional cost.
- **Key Results**: Consistent improvements on language modeling and reasoning; gains grow at longer context lengths.
- **Link**: [arXiv:2608.16844](https://arxiv.org/abs/2608.16844)

### 🔴 Kuaishou
#### GR4AD: Generative Recommendation for Advertising
- **Authors**: Ben Xue, Dan Liu, Lixiang Wang et al.
- **Affiliation**: Kuaishou Technology
- **Problem**: Deploying real-time generative recommendation in large-scale advertising requires designs beyond LLM-style training/serving.
- **Methodology**: UA-SID tokenization for business information; LazyAR lazy autoregressive decoder (nearly 2× QPS); VSL + RSPO value-aware optimization; Dynamic beam serving.
- **Key Results**: Up to **4.2% ad revenue improvement** over DLRM baseline; 10.17% ad conversion rate improvement; fully deployed serving 400M+ users. <100ms latency, 500+ QPS per L20.
- **Link**: [arXiv:2602.22732](https://arxiv.org/abs/2602.22732)

#### OneMall: End-to-End Generative Recommender at Kuaishou E-Commerce
- **Authors**: Kun Zhang et al.
- **Affiliation**: Kuaishou Technology
- **Problem**: Unified generative recommendation across multiple e-commerce scenarios.
- **Methodology**: E-commerce Semantic Tokenizer + Transformer backbone (Query-Former, Cross-Attention, Sparse MoE) + RL pipeline connecting retrieval and ranking models.
- **Key Results**: +13.01% GMV in product-card, +15.32% Orders in Short Video, +2.78% Orders in Live-Streaming. Deployed serving 400M+ daily active users.
- **Link**: [arXiv:2601.21770](https://arxiv.org/abs/2601.21770)

### 🔴 Alibaba
#### GALA: Generative Aligned Learning for Multimodal Recommendation (Taobao)
- **Authors**: Taobao Shangou team
- **Affiliation**: Alibaba
- **Problem**: Mismatch between static content-aligned embeddings and dynamic behavioral goals (CTR/CVR) in multimodal recommendation.
- **Methodology**: Three-stage pipeline: behavior-aware triplet pretraining → GRPO-based generative RL alignment → adaptive gating with hybrid loss for multimodal+ID fusion.
- **Key Results**: 0.55% order volume increase in online A/B test; deployed serving 200M+ daily active users. Consistent offline gains (+0.12/+0.20 AUC).
- **Link**: [arXiv:2607.29213](https://arxiv.org/abs/2607.29213)

### 🔴 Tencent
#### UniVA: Unified Value Alignment for Generative Advertising
- **Authors**: Jie Jiang et al.
- **Affiliation**: Tencent
- **Problem**: High generation likelihood in GR doesn't imply high advertising utility; valuable ads may be pruned during decoding.
- **Methodology**: Commercial SID Tokenization + Generation-as-Ranking SID Decoder + Value-Aware Constrained Serving with personalized trie.
- **Key Results**: 37.04% relative improvement in offline Hit Rate@100; 1.5% GMV lift in online A/B tests on WeChat Channels.
- **Link**: [arXiv:2605.05803](https://arxiv.org/abs/2605.05803)

#### SIREN: Multi-Modal Lifelong User Interest Modeling
- **Affiliation**: Tencent
- **Problem**: Integrating multi-modal features into lifelong interest modeling is challenging due to misalignment between multi-modal and collaborative spaces.
- **Methodology**: Unified multi-granularity semantic interaction; SemID-based hard retrieval for industrial serving; coarse similarity buckets + prefix-encoded SemIDs.
- **Key Results**: +2.28% GMV in WeChat Moments, +3.87% in WeChat Official Accounts, +1.61% in WeChat Channels. Fully launched for full-traffic serving.
- **Link**: [arXiv:2605.25726](https://arxiv.org/abs/2605.25726)

### 🔴 ByteDance
#### TokenMixer-Large: Scaling Up Large Ranking Models
- **Authors**: Yuchen Jiang et al.
- **Affiliation**: ByteDance
- **Problem**: Existing DLRM architectures struggle to scale beyond traditional boundaries while maintaining hardware efficiency.
- **Methodology**: Mixing-and-reverting operation, inter-layer residuals, Sparse Per-token MoE. Successfully scales to 7B and 15B parameters.
- **Key Results**: E-commerce: +1.66% orders, +2.98% per-capita GMV. Advertising: +2.0% ADSS. Live Streaming: +1.4% revenue. Deployed across ByteDance scenarios.
- **Link**: [arXiv:2602.06563](https://arxiv.org/abs/2602.06563)

### 🔴 LLM Reasoning & Agents
#### ReasonRec: Reasoning-Augmented Multimodal Agent for Recommendation
- **Authors**: Yihua Zhang et al.
- **Problem**: Multimodal recommenders lack explicit reasoning and self-awareness of uncertainty.
- **Methodology**: Three-stage reasoning pipeline; reasoning-aware visual instruction tuning; evidence-horizon curriculum; uncertainty-guided delegation.
- **Key Results**: 30%+ relative improvement in key ranking metrics; dynamically delegates 35% of queries to efficient sub-models without accuracy loss.
- **Link**: [arXiv:2606.28357](https://arxiv.org/abs/2606.28357)

#### STAR: Single-agent Trajectory-Aligned Recommender
- **Authors**: Yang Wu et al.
- **Problem**: Multi-agent recommendation systems have prohibitive inference latency.
- **Methodology**: Multi-agent teacher system with Collaborative Signal Translation → trajectory-driven distillation into single STAR model using SFT + GRPO.
- **Key Results**: STAR surpasses its teacher by 8.7%–39.5% while eliminating iterative latency.
- **Link**: [arXiv:2602.09829](https://arxiv.org/abs/2602.09829)

#### DREAM: Autonomous Optimization Control for Recommendation (Taobao)
- **Affiliation**: Alibaba
- **Problem**: Industrial recommender pipelines suffer from information fragmentation, scattered optimization, and weak real-time intent awareness.
- **Methodology**: Intent Engine (3-tier L0/L1/L2 intent with edge-cloud trigger chain) + Meta Engine (M1→M2→M3 layered reasoning) + Reward Dual Loop (offline simulation + online feedback).
- **Key Results**: Re-ranking control: IPV +2.06%, Core IPV +2.39%, GMV +0.88%. Extending to fine ranking: IPV +2.71%, Core IPV +3.06%, GMV +1.31%.
- **Link**: [arXiv:2608.09408](https://arxiv.org/abs/2608.09408)

### 🔴 Reasoning & Evaluation
#### BDH-CQ: In-Context Learning with Recurrent Latent Reasoning
- **Affiliation**: Pathway Research
- **Problem**: In-context learning and latent reasoning haven't been effectively combined in compact systems.
- **Methodology**: Dragon Hatchling architecture with recurrent memory updated by demonstrations; iterative computation in high-dimensional latent space without verbalizing reasoning.
- **Key Results**: 150M-parameter model reaches 29.5% pass@2 on ARC-AGI-1 at $0.0007/task — **new state of the art in cost efficiency**, ~57× cheaper than GPT 5.6 Luna.
- **Link**: [arXiv:2608.09888](https://arxiv.org/abs/2608.09888)

#### CARA: Cognitive Adaptive Recommendation Agent
- **Affiliation**: Various
- **Problem**: Existing LLM-based recommendation agents rely on semantic matching without explicit decision process modeling.
- **Methodology**: Dual-perspective decision modeling (affective + rational judgment); boundary-aware KTO for training; candidate filtering → dual-perspective decisions → confidence-adaptive ranking.
- **Key Results**: Up to 10.15% relative improvement over baselines on Amazon Reviews datasets.
- **Link**: [arXiv:2608.16919](https://arxiv.org/abs/2608.16919)

#### UniLang: Unified Generative Framework for Machine-Native Symbols
- **Authors**: Su Yan, Rakesh Iyer (Google)
- **Affiliation**: Google
- **Problem**: LLMs can't directly operate on machine-native symbols (e.g., item IDs, structured data) without verbalization.
- **Methodology**: Extends LLM vocabulary with grounded machine-native representations; joint autoregressive modeling of text + symbolic tokens.
- **Key Results**: Up to 151% improvement in NDCG@5 on MovieLens-20M for sequential recommendation; 49% improvement in Recall@1 for legal precedent prediction. Same framework across structurally different tasks.
- **Link**: [arXiv:2608.19529](https://arxiv.org/abs/2608.19529)

### 🔴 HRPO: Hierarchical Residual Policy Optimization (KDD 2026)
- **Authors**: Kaifeng Guo et al. (Kuaishou + CityU HK)
- **Affiliation**: Kuaishou Technology
- **Problem**: SID decoders trained via supervised NTP don't directly optimize downstream utility; item-level feedback causes sparse token-level credit assignment.
- **Methodology**: Group-wise reward smoothing → residual token credit decomposition → RRPO with clipped updates + KL regularization.
- **Key Results**: Consistent gains on KuaiRand public dataset; positive online A/B test results across IAA traffic segments.
- **Link**: [arXiv:2608.00750](https://arxiv.org/abs/2608.00750)

### 🔴 LLM Training & Architecture
#### When Machines Speak (UniLang for Machine-Native Symbols)
- See above under Google section.

#### REAM: Reasoning-Head-Aware Merging for Recommendation
- **Problem**: Slow-thinking models generate verbose reasoning; fast-thinking models lack accuracy.
- **Methodology**: First model merging framework for reasoning compression in recommender systems. Head-level coefficients based on retrieval criticality + decision faithfulness + sensitivity.
- **Key Results**: Reduces reasoning length by up to 24.3% while maintaining recommendation accuracy.
- **Link**: [arXiv:2608.10447](https://arxiv.org/abs/2608.10447)

### 🔴 Games & Code Execution
#### NitroGen (CVPR 2026 Honorable Mention)
- See CVPR section above.

---

## 📈 Cross-Conference Trends (2025–2026)

### 1. LLM-Based Generative Recommendation Reaches Production
- **Netflix GenRec**: LLM-backed ranker in production A/B test
- **Kuaishou GR4AD**: 4.2% ad revenue, deployed 400M+ users
- **Kuaishou OneMall**: 13% GMV improvement, deployed 400M+ DAU
- **Alibaba GALA**: GRPO-based alignment, deployed 200M+ DAU
- **Tencent UniVA/GPR/SIREN**: Multiple production deployments
- **ByteDance TokenMixer-Large**: 7B–15B ranking models in production

### 2. RLVR (RL with Verifiable Rewards) Dominates Post-Training
- ACL 2026: 3 of 18 Outstanding Papers on RLVR
- ICML 2026: Multiple papers on PbRL and preference-based alignment
- **STEER**, **GeoRA**, **Evolutionary Guided Decoding** address specific RLVR weaknesses

### 3. Agent Systems & Tool Use
- **ACL 2026**: Largest growth area (+224 papers, 366 total on agents/reasoning)
- **AAAI 2026**: SPIRAL (MCTS + LLM agents), Bonsai (interpretable agents)
- **DREAM** (Alibaba): Full autonomous optimization control for recommendation

### 4. Latent Reasoning & Test-Time Compute
- **BDH-CQ**: 150M model beats 57× larger models on ARC-AGI-1
- **ICPO/ME-ICPO**: Theoretical grounding for self-reflection
- **Recirculation** (DeepMind): Training-free recurrence for existing models

### 5. Multimodal Foundation Models
- **CVPR 2026**: SAM 3D, Molmo2, VMonarch, UltraFlux
- **ACL 2026**: Uni-MMMU, FastV-RAG, MathFlow
- **Production**: SIREN (Tencent), GALA (Alibaba) — multimodal at scale

### 6. Efficiency & Scaling
- **WhiteMatter**: 8.2% perplexity reduction via cross-layer KV mixing
- **Proteus**: Incremental memory activation for long contexts
- **TokenMixer-Large**: 15B ranking models with sparse MoE
- **LazyAR** (Kuaishou): Nearly 2× QPS for autoregressive generation

### 7. Code Execution & Program Synthesis
- **NeurIPS 2025**: Program synthesis via test-time transduction
- **ACL 2026**: ReEx-SQL, Discover and Prove (Lean 4 theorem proving)
- **AAAI 2026**: SPIRAL for API planning

---

## 🔗 Cross-References

### Related Wiki Pages
- [[concepts/rlvr|RL with Verifiable Rewards]]
- [[concepts/generative-recommendation|Generative Recommendation]]
- [[concepts/llm-agents|LLM Agents]]
- [[methods/rlhf|RLHF]]
- [[papers/recommendation/hstu-generative-recommendation|HSTU: Trillion-Parameter Generative Recommendation]]

---

*Generated: 2026-08-26 | Sources: arXiv, OpenReview, conference proceedings, CVF Open Access, ACL Anthology, ACM Digital Library*
