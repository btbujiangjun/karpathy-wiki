---
title: Conference Digest 2025-2026
type: synthesis
created: 2026-07-02
updated: 2026-07-02
sources: []
tags: [conference-digest, icml-2026, neurips-2025, iclr-2026, aaai-2026, cvpr-2026, kdd-2026, sigir-2026, emnlp-2025, acl-2026, recsys-2025, llm, recommendation, ctr, agent, vision, nlp]
---

# Conference Digest 2025–2026

> Comprehensive survey of recent papers across top ML/AI conferences (ICML 2026, NeurIPS 2025, ICLR 2026, AAAI 2026, CVPR 2026, KDD 2026, SIGIR 2026, EMNLP 2025, ACL 2026, RecSys 2025) and key arXiv preprints from leading labs.

---

## Table of Contents

1. [ICML 2026](#icml-2026)
2. [NeurIPS 2025](#neurips-2025)
3. [ICLR 2026](#iclr-2026)
4. [AAAI 2026](#aaai-2026)
5. [CVPR 2026](#cvpr-2026)
6. [KDD 2026](#kdd-2026)
7. [SIGIR 2026](#sigir-2026)
8. [EMNLP 2025](#emnlp-2025)
9. [ACL 2026](#acl-2026)
10. [RecSys 2025](#recsys-2025)
11. [Industry Labs — OpenAI, Google DeepMind, Meta AI, Anthropic](#industry-labs)
12. [CTR / Recommendation Scaling](#ctr-recommendation-scaling)
13. [Agent Systems & Reasoning](#agent-systems-reasoning)

---

## ICML 2026

**Venue**: Seoul, South Korea, July 6–11, 2026
**Submissions**: ~23,918 → 6,352 accepted (26.6% acceptance rate)

### Key Papers

#### Attention Sink Forges Native MoE in Attention Layers: Sink-Aware Training to Address Head Collapse
- **Authors**: Zizhuo Fu et al.
- **Affiliation**: —
- **Link**: —
- **Innovation**: Identifies "head collapse" in MoE attention layers; proposes sink-aware training that converts attention sinks into native MoE routing signals, preventing attention heads from collapsing into uniform patterns.
- **Comparison**: Addresses a key limitation of standard MoE attention where heads degenerate; achieves better expert specialization without auxiliary loss.

#### TEAM: Temporal–Spatial Consistency Guided Expert Activation for MoE Diffusion Language Model Acceleration
- **Authors**: Linye Wei et al.
- **Affiliation**: —
- **Link**: —
- **Innovation**: Temporal-spatial consistency guided expert activation for MoE diffusion LMs. Activates only relevant experts per denoising step based on consistency patterns.
- **Comparison**: 2-3x speedup over dense diffusion LMs with <1% quality drop.

#### HyPER: Bridging Exploration and Exploitation for Scalable LLM Reasoning with Hypothesis Path Expansion and Reduction
- **Authors**: Shengxuan Qiu, Haochen Huang et al.
- **Affiliation**: —
- **Link**: —
- **Innovation**: HyPER combines hypothesis path expansion (tree search) with path reduction (pruning) for LLM reasoning. Dynamically balances exploration vs exploitation during inference.
- **Comparison**: Outperforms CoT and ToT on math reasoning benchmarks. Scales better with inference-time compute.

#### How Does the Lagrangian Guide Safe Reinforcement Learning through Diffusion Models?
- **Authors**: Xiaoyuan Cheng et al.
- **Affiliation**: UCL (sole corresponding author)
- **Link**: —
- **Innovation**: Uses Lagrangian duality to guide diffusion-based safe RL. The Lagrangian multiplier acts as an adaptive safety constraint during the diffusion denoising process.
- **Results**: State-of-the-art safety-reward tradeoff on SafeRL benchmarks.

#### MMPD-Bench: Bridging Multimodal Fission with Multi-Polarimetric Modalities Decomposition
- **Authors**: Yi He et al.
- **Affiliation**: UCL, Oxford
- **Link**: —
- **Innovation**: Multi-modal polarimetric decomposition benchmark for fission-based multimodal learning.

---

## NeurIPS 2025

**Venue**: Hybrid (San Diego, Sydney, Atlanta, Mexico City), December 2025
**Submissions**: ~15,670 → 4,035 accepted (25.75% acceptance rate)

### Key Papers

#### Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning
- **Authors**: Chaofan Lin, Jiaming Tang, Shuo Yang, Ion Stoica, Song Han, Mingyu Gao et al.
- **Affiliation**: UC Berkeley, Tsinghua
- **Link**: https://openreview.net/forum?id=Ve693NkzcU
- **Innovation**: Extends top-p (nucleus) sampling idea to sparse attention — adaptively decides how many tokens to attend to per layer/head. Hierarchical pruning with local and global budgets.
- **Results**: Up to 98% token pruning with near-zero accuracy loss; 1.4x speedup over SOTA sparse attention mechanisms.
- **Comparison**: Unlike fixed-budget sparse attention (e.g., StreamingLLM, H2O), Twilight dynamically adjusts budget per context.

#### MASTER: Enhancing Large Language Model via Multi-Agent Simulated Teaching
- **Authors**: Liang Yue, Yihong Tang, Kehai Chen, Jie Liu, Min Zhang
- **Affiliation**: —
- **Link**: https://openreview.net/forum?id=KurYdcCbjv
- **Innovation**: Multi-agent simulated teaching with 3 pedagogical scenarios. Agents with varying cognitive levels interact to generate high-quality teacher-student interaction data. BOOST-QA dataset built from Orca-Math-200k, ProcQA, OpenHermes2.5.
- **Results**: Models fine-tuned with BOOST-QA perform excellently across multiple benchmarks.

#### Gated Integration of Low-Rank Adaptation for Continual Learning of LLMs
- **Authors**: Yan-Shuo Liang, Jia-Rui Chen, Wu-Jun Li
- **Affiliation**: Nanjing University
- **Link**: https://arxiv.org/abs/2505.15424
- **Innovation**: Gated integration of LoRA branches — learns adaptive gating weights for combining old and new LoRA adapters instead of simple addition. Mitigates catastrophic forgetting in continual LLM fine-tuning.
- **Results**: Significantly outperforms existing LoRA-based continual learning methods on sequential task learning.

#### Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference
- **Authors**: Jiayi Yuan, Hao Li, Xinheng Ding, Zirui Liu et al.
- **Affiliation**: —
- **Link**: https://openreview.net/forum?id=Q3qAsZAEZw
- **Innovation**: Systematic analysis of numerical nondeterminism in LLM inference (floating-point non-associativity, GPU reductions). Proposes mitigation strategies for reproducible LLM inference.

#### MotionRAG: Retrieval-Augmented Generation for Video Motion Generation
- **Authors**: —
- **Affiliation**: —
- **Link**: —
- **Innovation**: RAG for video motion generation. Retrieves motion priors from reference videos via Context-Aware Motion Adaptation (CAMA). Causal Transformer for motion pattern transfer.

#### ControlFusion: Text-Guided Image Fusion
- **Authors**: —
- **Affiliation**: —
- **Link**: —
- **Innovation**: Text-guided fusion of multiple images. Outperforms SOTA fusion methods in real-world and compound degradation scenarios.

---

## ICLR 2026

**Venue**: Virtual/In-person, April 2026
**Submissions**: ~5,342 accepted

### Key Papers

#### PAPL: Planner Aware Path Learning in Diffusion Language Models
- **Authors**: Zhangzhi Peng, Zachary Bezemek, Jarrid Rector-Brooks, Michael Bronstein, Joey Bose, Alexander Tong et al.
- **Affiliation**: —
- **Link**: https://openreview.net/forum?id=lAlI5FuIf7 (Oral)
- **Innovation**: Identifies and solves the training-inference mismatch in discrete diffusion LMs under planning-based sampling. Derives P-ELBO (planned evidence lower bound) that incorporates planner dynamics into training.
- **Results**: 40% relative improvement on protein sequences, up to 4x MAUVE gain on text, 23% on HumanEval pass@10.
- **Significance**: First principled solution to train-inference gap in diffusion LM planning.

#### ReasoningBank: Memory-Driven Experience Scaling for LLM Agents
- **Authors**: Google Research
- **Affiliation**: Google
- **Link**: https://openreview.net/forum?id=jL7fwchScm
- **Code**: https://github.com/google-research/reasoning-bank
- **Innovation**: Memory-driven experience scaling — agents store structured reasoning traces as memory, which guides test-time compute scaling. MaTTS (Memory-augmented Test-Time Scaling) creates a virtuous cycle between memory quality and compute allocation.
- **Results**: Outperforms existing memory mechanisms (raw trajectories, successful routines) on web browsing and software engineering.
- **Significance**: Establishes memory-driven experience scaling as a new scaling dimension for agents.

#### Common Corpus: The Largest Collection of Ethical Data for LLM Pre-Training
- **Authors**: Pierre-Carl Langlais, Pavel Chizhov, Ivan P. Yamshchikov et al.
- **Affiliation**: —
- **Link**: https://openreview.net/forum?id=0wSlFpMsGb
- **Innovation**: ~2 trillion tokens of uncopyrighted/permissively-licensed data. Covers multiple languages and code. Models trained on Common Corpus perform comparably to similarly-sized models.
- **Significance**: Largest open pre-training dataset addressing copyright concerns.

#### FZOO: Fine-Tuning with Zoo of Optimizers
- **Authors**: Sizhe Dang, Yangyang Guo, Ivor Tsang et al.
- **Affiliation**: A*STAR CFAR
- **Link**: https://openreview.net/forum?id=CylRqa82Rk
- **Innovation**: Achieves fine-tuning speed comparable to Adam with inference-level GPU memory. Enables efficient large-scale LLM optimization.

#### NEO: From Pixels to Words — Towards Native Vision-Language Primitives at Scale
- **Authors**: H. Diao, M. Li, S. Wu, L. Dai, X. Wang, Z. Liu et al.
- **Affiliation**: MMLab@NTU
- **Link**: https://arxiv.org/abs/2510.14979
- **Innovation**: Native vision-language primitives that unify visual and textual representations at the token level, avoiding modality-specific encoders.

#### Visual Jigsaw Post-Training Improves MLLMs
- **Authors**: P. Wu, Y. Zhang, H. Diao, Z. Liu et al.
- **Affiliation**: MMLab@NTU
- **Link**: https://arxiv.org/abs/2509.25190
- **Innovation**: Visual jigsaw (patch shuffling) as post-training task for multimodal LLMs. Improves spatial understanding and compositional reasoning.

#### OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety
- **Authors**: Sanidhya Vijayvargiya, Graham Neubig et al.
- **Affiliation**: CMU
- **Link**: https://openreview.net/forum?id=xggSxCFQbA
- **Innovation**: Evaluates agents on real tools (browser, code, filesystem, bash, messaging) across 8 risk categories. 350+ multi-turn tasks.
- **Results**: 49–73% unsafe behavior rates across Claude Sonnet 4 to o3-mini. Highlights critical safety gaps.

#### Reinforcement Learning Fine-Tuning Enhances Activation Intensity and Diversity in Internal Circuitry of LLMs
- **Authors**: Honglin Zhang, Qianyue Hao, Fengli Xu, Yong Li
- **Affiliation**: —
- **Link**: —
- **Innovation**: Mechanistic analysis of RL fine-tuning effects on LLM internal circuitry. RL increases activation intensity and diversity compared to SFT, explaining why RL post-training improves generalization.

---

## AAAI 2026

**Venue**: Singapore, January 20–27, 2026
**Submissions**: ~23,680 → 4,167 accepted (17.6% acceptance rate)

### Key Papers

#### FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play Reconstruction-based Token Pruning
- **Authors**: Xiaopeng Motors × Peking University
- **Affiliation**: Xiaopeng Motors, Peking University
- **Link**: —
- **Innovation**: Reconstruction-based visual token pruning for VLA models. Prunes redundant visual tokens while preserving information for driving decisions.
- **Results**: Significant speedup for end-to-end autonomous driving without accuracy loss.

#### ExpertAD: Enhancing Autonomous Driving Systems with Mixture of Experts
- **Authors**: —
- **Affiliation**: —
- **Link**: https://arxiv.org/abs/2511.11740
- **Innovation**: MoE architecture for autonomous driving — different experts handle different driving scenarios (highway, urban, parking).

#### DiffuNovo: Regressor-guided Diffusion Model for De Novo Peptide Sequencing with Explicit Mass Control
- **Authors**: Shaorong Chen, Jingbo Zhou, Jun Xia
- **Affiliation**: —
- **Link**: https://ojs.aaai.org/index.php/AAAI/article/view/36968
- **Innovation**: Diffusion model for peptide sequencing with explicit mass consistency constraint. Regressor guides generation to match experimental precursor mass.
- **Results**: Fewer implausible predictions compared to existing DNPS methods.

#### GlassVAE: Hierarchical Graph VAE for Disordered Materials
- **Authors**: —
- **Affiliation**: —
- **Link**: —
- **Innovation**: Graph VAE with physics-informed regularizers (RDF loss, energy regression) for glass structure generation. Compact latent space for disordered materials.

---

## CVPR 2026

**Venue**: Denver, CO, June 3–7, 2026
**Submissions**: 16,092 → 4,090 accepted (25.42% acceptance rate) + 1,717 Findings

### Best Paper

#### D4RT: Efficiently Reconstructing Dynamic Scenes One D4RT at a Time
- **Authors**: Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Rahul Sukthankar, Joëlle K. Barral, Raia Hadsell, Andrew Zisserman, Mehdi S. M. Sajjadi et al.
- **Affiliation**: Google DeepMind, UCL, Oxford
- **Link**: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Efficiently_Reconstructing_Dynamic_Scenes_One_D4RT_at_a_Time_CVPR_2026_paper.html
- **Innovation**: Unified transformer architecture for 4D dynamic scene reconstruction. Estimates depth, spatio-temporal correspondence, and camera parameters jointly. Enables efficient probing of any 3D point in space and time.
- **Significance**: Lightweight, scalable method for dynamic scene reconstruction. CVPR 2026 Best Paper.

### Best Student Paper

#### Native and Compact Structured Latents for 3D Generation
- **Authors**: —
- **Affiliation**: —
- **Link**: —
- **Innovation**: Compact structured latent representations for 3D generation. Native 3D structure without post-processing.

### Other Key Papers

#### GP-4DGS: Probabilistic 4D Gaussian Splatting via Variational Gaussian Processes
- **Authors**: Mijeong Kim, Jungtaek Kim, Bohyung Han
- **Affiliation**: SNU
- **Link**: —
- **Innovation**: Probabilistic 4D Gaussian splatting for monocular video. Uses variational GPs to model temporal dynamics of 3D Gaussians.

#### MADrive: Memory-Augmented Driving Scene Modeling
- **Authors**: Polina Karpikova, Daniil Selikhanovych, Kirill Struminsky et al.
- **Affiliation**: Yandex Research
- **Link**: https://arxiv.org/abs/2506.21520
- **Innovation**: Memory-augmented driving simulation. Retrieves similar vehicle 3D assets from external memory bank for photorealistic scene modification.

#### PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image
- **Authors**: Z. Cao, F. Hong, Z. Chen, L. Pan, Z. Liu
- **Affiliation**: MMLab@NTU
- **Link**: https://arxiv.org/abs/2511.13648
- **Innovation**: Generates simulation-ready 3D assets with physical properties (mass, friction, elasticity) from a single image.

#### WorldLens: Full-Spectrum Evaluations of Driving World Models in Real World (Oral)
- **Authors**: A. Liang, L. Kong, Z. Liu et al.
- **Affiliation**: MMLab@NTU
- **Link**: https://arxiv.org/abs/2512.10958
- **Innovation**: Comprehensive evaluation framework for driving world models. Full-spectrum metrics covering prediction, planning, and rendering quality.

#### Enhancing Mixture-of-Experts Specialization via Cluster-Aware Upcycling
- **Authors**: Sanghyeok Chu, Pyunghwan Ahn, Honglak Lee, Bohyung Han
- **Affiliation**: SNU, LG AI Research
- **Link**: —
- **Innovation**: Cluster-aware upcycling for MoE — groups similar experts and upcycles them jointly to improve specialization.

---

## KDD 2026

**Venue**: Jeju Island, Republic of Korea, August 9–13, 2026
**Submissions**: 1,215 (Research Track) → 256 accepted (21%)

### Key Papers

#### CTR-Sink: Attention Sink for Language Models in Click-Through Rate Prediction
- **Authors**: —
- **Affiliation**: —
- **Link**: https://arxiv.org/abs/2508.03668
- **Code**: https://github.com/UGUESS-lzx/CTR-SINK
- **Innovation**: Addresses "semantic fragmentation" when using LMs for CTR prediction. Inserts behavior-level attention sink tokens between user behaviors, incorporating temporal distance signals.
- **Results**: Validated on industrial + MovieLens + Kuairec datasets. Visualization confirms attention concentration on sink tokens.
- **Significance**: Bridges attention sink theory with recommendation systems.

#### TokenMixer-Large: Scaling Up Large Ranking Models in Industrial Recommenders
- **Authors**: ByteDance
- **Affiliation**: ByteDance
- **Link**: https://arxiv.org/abs/2602.06563
- **Innovation**: Addresses hardware under-utilization in scaling ranking models. Optimized TokenMixer architecture for industrial deployment.

#### EST: Towards Efficient Scaling Laws in CTR via Unified Modeling
- **Authors**: Alibaba
- **Affiliation**: Alibaba
- **Link**: https://arxiv.org/abs/2602.10811
- **Innovation**: Efficient unified modeling for scalable CTR prediction. Addresses early aggregation limitations in large-scale CTR models.

#### ULTRA-HSTU: Bending the Scaling Law Curve in Large-Scale Recommendation Systems
- **Authors**: Meta
- **Affiliation**: Meta AI
- **Link**: https://arxiv.org/abs/2602.16986
- **Innovation**: Sparse Attention + FlashAttention-V3 for recommendation. Bends the scaling law curve beyond HSTU (Meta's previous SOTA architecture).

---

## SIGIR 2026

**Venue**: Melbourne, Australia, July 20–24, 2026
**Acceptance rate**: ~18.4%

### Key Papers

#### Beyond Static Best-of-N: Bayesian List-wise Alignment for LLM-based Recommendation
- **Authors**: Ruijun Chen, Chongming Gao, Jiawei Chen, Weiqin Yang, Xiangnan He
- **Affiliation**: USTC
- **Link**: https://arxiv.org/abs/2605.04559
- **Innovation**: Bayesian list-wise alignment for LLM-based recommendation. Dynamically adapts alignment strategy per user/item context instead of static Best-of-N.

#### SORT: A Systematically Optimized Ranking Transformer for Industrial-Scale Recommenders
- **Authors**: Alibaba
- **Affiliation**: Alibaba
- **Link**: https://arxiv.org/abs/2603.03988
- **Innovation**: Systematically optimizes Transformer architecture for industrial ranking. Addresses high feature heterogeneity challenges. Custom attention patterns for recommendation-specific features.

#### Beyond Dense Connectivity: Explicit Sparsity for Scalable Recommendation
- **Authors**: Alibaba
- **Affiliation**: Alibaba
- **Link**: https://arxiv.org/abs/2604.xxxxx
- **Innovation**: Explicit sparsity patterns in recommendation Transformers for better scaling.

#### One-for-All Community Search on Unseen Graphs
- **Authors**: Li Mo, Ding Linlin et al.
- **Affiliation**: Liaoning University, University of Melbourne, Aalborg University, Edith Cowan University
- **Innovation**: Cross-dataset universal community search using spectrum-aware feature alignment + graph diffusion Transformer. Trained once, transfers to any unseen graph without retraining.
- **Results**: 7.92% improvement over existing methods in cross-dataset settings.

#### Evaluation of Information Access Agents under Simulated AI Marketplace Dynamics
- **Authors**: To Eun Kim, Alireza Salemi, Fernando Diaz, Hamed Zamani
- **Affiliation**: UMass Amherst (CIIR)
- **Innovation**: Evaluates AI agents for information access under simulated marketplace dynamics where agents compete for user attention.

#### Total Recall QA: A Verifiable Evaluation Suite for Deep Research Agents
- **Authors**: Mahta Rafiee, Hamed Zamani et al.
- **Affiliation**: UMass Amherst (CIIR)
- **Innovation**: Verifiable QA benchmark for evaluating deep research agents' ability to retrieve and synthesize information.

---

## EMNLP 2025

**Venue**: Suzhou, China, November 4–9, 2025
**Submissions**: ~8,000 → ~3,200 accepted (1,800 main + 1,400 findings)

### Key Papers

#### Agent Trading Arena: A Study on Numerical Understanding in LLM-Based Agents
- **Authors**: Tianmi Ma, Jiawei Du, Joey Tianyi Zhou et al.
- **Affiliation**: A*STAR CFAR
- **Link**: https://arxiv.org/abs/2502.17967
- **Innovation**: Multi-agent stock market simulation where LLM agents affect price dynamics through bid-ask interactions. Chart-based visualization + reflection module improves numerical reasoning.
- **Results**: Significant improvement in trading performance under high volatility.

#### Diagram-Driven Course Questions Generation (DDCQG)
- **Authors**: Xinyu Zhang, Basura Fernando et al.
- **Affiliation**: A*STAR CFAR
- **Link**: https://arxiv.org/abs/2411.17771
- **Innovation**: Visual question generation for diagrams (not natural images). DiagramQG dataset: 15,720 diagrams, 25,798 questions across 37 subjects.

#### RRInf: Efficient Influence Function Estimation via Ridge Regression for LLMs and Diffusion Models
- **Authors**: Zhuozhuo Tu, Cheng Chen, Yuxuan Du
- **Affiliation**: A*STAR CFAR
- **Innovation**: Reformulates influence function estimation as ridge regression. Scalable to modern LLMs and text-to-image diffusion models.

#### MathTutorBench: A Benchmark for Measuring Open-ended Pedagogical Capabilities of LLM Tutors
- **Authors**: Jakub Macina, Nico Daheim, Iryna Gurevych, Mrinmaya Sachan et al.
- **Affiliation**: ETH Zurich, TU Darmstadt
- **Link**: https://aclanthology.org/2025.emnlp-main.11/
- **Innovation**: Benchmark for evaluating LLM tutors on open-ended pedagogical capabilities, not just factual accuracy.

#### SEEED: Soft Clustering Extended Encoder-Based Error Detection for Conversational AI
- **Authors**: Dominic Petrak, Thy Thy Tran, Iryna Gurevych
- **Affiliation**: TU Darmstadt
- **Link**: https://aclanthology.org/2025.emnlp-main.1/
- **Innovation**: Automated error discovery framework for conversational AI. Soft nearest neighbor loss with label-based sample ranking.

---

## ACL 2026

**Venue**: San Diego, CA, July 2–7, 2026
**Submissions**: 12,145 → 2,308 accepted (19% main) + 2,164 Findings

### Key Papers

#### BootTrans: Bootstrapping Code Translation with Weighted Multilanguage Exploration
- **Authors**: Yuhan Wu, Huan Zhang, Wei Hu et al.
- **Affiliation**: Nanjing University
- **Link**: https://arxiv.org/abs/2601.03512
- **Innovation**: Bootstrapped code translation without parallel corpora. Uses unit test transferability across languages for cyclic training. Language-aware dynamic weighted optimization for hard translation directions.
- **Results**: Up to 16.57% gain on Llama-3.1-8B. Generalizes to unseen and low-resource languages.

#### CORBA: Contagious Recursive Blocking Attacks on Multi-Agent Systems Based on LLMs
- **Authors**: Zhenhong Zhou, Jie Zhang, Qing Guo et al.
- **Affiliation**: A*STAR CFAR
- **Link**: https://arxiv.org/abs/2502.14529
- **Innovation**: Identifies Denial-of-Collaboration (DoC) attack class for LLM multi-agent systems. CORBA induces benign recursive communication loops causing resource exhaustion.

#### Safety Sidecar: Reflection-Driven Runtime Control for Safer Agents
- **Authors**: Bin Wang, Xingrui Yu, Ivor Tsang et al.
- **Affiliation**: A*STAR CFAR
- **Innovation**: Model-agnostic runtime safety module. Uses reflective evidence-driven intervention with external verification for secure agent execution.

#### NeoAMT: Neologism-Aware Agentic Machine Translation with RL
- **Authors**: Zhongtao Miao, Masaaki Nagata, Yoshimasa Tsuruoka
- **Affiliation**: NTT, University of Tokyo
- **Innovation**: Agent-based MT where LLM consults external dictionary for neologisms. RL fine-tuning improves dictionary usage decisions.

#### RARE: Redundancy-Aware Retrieval Evaluation Framework for Enterprise RAG
- **Authors**: Allganize
- **Affiliation**: Allganize Korea
- **Innovation**: Analyzes RAG performance gap in enterprise environments. Accuracy drops from 77.9% (wiki) to 8.5% (finance) and 5.0% (law) due to document redundancy.

#### Calibration-Aware RL for Decision-Making LLMs
- **Authors**: Duygu Nur Yaldiz, Zheng Qi, Nikolaos Pappas et al.
- **Affiliation**: Amazon Science
- **Innovation**: Balances classification and calibration performance in LLMs via calibration-aware RL. Jointly optimizes accuracy and confidence calibration.

---

## RecSys 2025

**Venue**: Prague, Czech Republic, September 22–26, 2025
**Acceptance rate**: ~20%

### Key Papers

#### Beyond Immediate Click: Engagement-Aware and MoE-Enhanced Transformers for Sequential Movie Recommendation
- **Authors**: —
- **Affiliation**: —
- **Link**: https://dl.acm.org/doi/10.1145/3705328.3748076
- **Innovation**: Engagement-aware sequential recommendation with MoE. Models not just clicks but engagement depth.

#### LEAF: Lightweight, Efficient, Adaptive and Flexible Embedding for Large-Scale Recommendation Models
- **Authors**: —
- **Affiliation**: —
- **Link**: https://dl.acm.org/doi/10.1145/3705328.3748078
- **Innovation**: Lightweight adaptive embedding framework for large-scale recommenders. Reduces embedding memory while maintaining accuracy.

#### You Say Search, I Say Recs: A Scalable Agentic Approach to Query Understanding and Exploratory Search at Spotify
- **Authors**: Spotify
- **Affiliation**: Spotify
- **Link**: https://dl.acm.org/doi/10.1145/3705328.3748127
- **Innovation**: Agentic approach bridging search and recommendation at Spotify. LLM agent understands query intent and routes to search or recommendation.

#### Lasso: Large Language Model-based User Simulator for Cross-Domain Recommendation
- **Authors**: —
- **Affiliation**: —
- **Link**: https://dl.acm.org/doi/10.1145/3705328.3748048
- **Innovation**: LLM-based user simulator for cross-domain recommendation evaluation. Simulates user behavior across domains without real user data.

#### Yambda-5B: Large-Scale Open Dataset from Yandex.Music
- **Authors**: Yandex
- **Affiliation**: Yandex
- **Link**: —
- **Innovation**: 4.79B interactions, 1M users, 9.39M tracks. Includes is_organic flag for separating organic vs recommendation-driven actions.

#### Exploring Scaling Laws of CTR Model for Online Performance Improvement
- **Authors**: —
- **Affiliation**: —
- **Link**: https://arxiv.org/abs/2508.15326
- **Innovation**: Empirically studies scaling laws for CTR models (model size, data size, training compute) in online settings.

---

## Industry Labs: OpenAI, Google DeepMind, Meta AI, Anthropic

### OpenAI

#### GPT-5.6 Sol (Preview, June 2026)
- **Type**: Model release
- **Innovation**: Three-model family: Sol (flagship), Terra (cost-efficient), Luna (fastest). Stronger coding, science, and cybersecurity capabilities.
- **System Card**: Most advanced safety stack from OpenAI.

#### GPT-5.5 (April 2026)
- **Type**: Model release
- **Innovation**: Faster, more capable for complex tasks (coding, research, data analysis). GPT-5.5 Instant (May 2026) as default ChatGPT model.

#### Dreaming: Better Memory for ChatGPT (June 2026)
- **Type**: Product feature / Research
- **Innovation**: New memory system that better remembers user preferences across conversations.

#### AI Chemist (June 2026)
- **Innovation**: Near-autonomous AI chemist using GPT-5.4 improves medicinal chemistry reactions. Collaboration with Molecule.one.

#### Unit Distance Problem Solved (May 2026)
- **Innovation**: OpenAI model disproves 80-year-old unit distance conjecture in discrete geometry. Milestone in AI-driven mathematics.

#### LifeSciBench (June 2026)
- **Innovation**: Expert-authored benchmark for evaluating AI on real-world life science research tasks.

### Google DeepMind

#### D4RT (CVPR 2026 Best Paper)
- See CVPR section above.

#### Gemini 3.5 (May 2026)
- **Type**: Model release
- **Innovation**: Frontier intelligence with action capabilities. Next-generation Gemini model.

#### Gemma 4 12B (June 2026)
- **Type**: Model release
- **Innovation**: Unified, encoder-free multimodal model. Single model processes text, images, and more without separate vision encoder.

#### Gemini Deep Think (March 2026)
- **Type**: Research
- **Link**: https://deepmind.google/blog/accelerating-mathematical-and-scientific-discovery-with-gemini-deep-think
- **Innovation**: Inference-time scaling law for math. Achieves PhD-level math performance. AI-generated research paper (Feng26) without human intervention. Solved 4 open problems on Erdős conjectures.

#### Co-Scientist (May 2026)
- **Type**: Research
- **Innovation**: Multi-agent AI system for scientific research acceleration. Used in biology, medicine, and chemistry.

#### SIMA 2
- **Innovation**: Generalist agent that plays, reasons, and learns in virtual 3D worlds.

#### Genie 3
- **Innovation**: General-purpose world model generating diverse interactive environments.

#### TRecViT: A Recurrent Video Transformer (January 2026)
- **Link**: https://deepmind.google/research/publications/122591/
- **Innovation**: Recurrent architecture for video understanding. Efficient long-term temporal modeling.

#### Image Generators are Generalist Vision Learners (April 2026)
- **Link**: https://deepmind.google/research/publications/240658/
- **Innovation**: Image generation models can serve as general-purpose vision learners without task-specific fine-tuning.

### Meta AI

#### ULTRA-HSTU: Bending Scaling Laws for Recommendation
- See KDD section above.

#### Meta AI Research Publications (2026)
- **Multimodal Test-Time Scaling**: Establishing multimodal test-time scaling as an effective paradigm for unified generation and understanding models.
- **AIRS-Bench**: AI Research Science Benchmark — 20 tasks from SOTA ML papers covering language modeling, math, bioinformatics, time series.

#### Llama Ecosystem
- Ongoing development of open-source Llama model family.

### Anthropic

#### Claude Sonnet 5 (June 30, 2026)
- **Type**: Model release
- Latest frontier model from Anthropic as of June 2026.

---

## CTR / Recommendation Scaling

> A rapidly growing sub-field focused on scaling laws, efficient architectures, and foundation models for CTR prediction and recommendation.

### Key Papers (KDD 2026 / SIGIR 2026 / arXiv 2026)

| Paper | Affiliation | Venue | Innovation |
|-------|------------|-------|------------|
| CTR-Sink | — | KDD 2026 | Attention sink for LM-based CTR |
| TokenMixer-Large | ByteDance | KDD 2026 | Hardware-optimized scaling |
| EST | Alibaba | KDD 2026 | Efficient scaling laws for CTR |
| ULTRA-HSTU | Meta | arXiv 2026 | Beyond HSTU scaling curve |
| SORT | Alibaba | SIGIR 2026 | Optimized ranking Transformer |
| Beyond Dense Connectivity | Alibaba | SIGIR 2026 | Explicit sparsity for scaling |
| CADET | LinkedIn | arXiv 2026 | Decoder-only Transformer for ad CTR |
| MSN | ByteDance | arXiv 2026 | Memory-based sparse activation |
| HeteroMixer | Alibaba | arXiv 2026 | Query-mixed interest extraction |
| MixFormer | ByteDance | arXiv 2026 | Co-scaling dense + sequence |
| MTFM | Meituan | arXiv 2026 | Foundation model for recommendation |
| UG-Sep | ByteDance | arXiv 2026 | User-general feature separation |

### Key Trends

1. **Scaling Laws for CTR**: Multiple papers empirically demonstrate that CTR models benefit from scaling (data, parameters, compute) just like LLMs.
2. **Sparse Attention**: Replacing dense attention with sparse variants (FlashAttention, sparse MoE) for recommendation Transformers.
3. **Foundation Models**: Industry labs (Meituan MTFM, ByteDance MixFormer) building unified foundation models for recommendation across domains.
4. **Efficient Serving**: Focus on hardware-aware optimizations (Triton kernels, CPU-GPU pipelines) for industrial deployment.

---

## Agent Systems & Reasoning

### Key Papers

#### Agentic Reasoning: A Survey (January 2026)
- **Authors**: Heng Ji, Jingrui He, Jiaxuan You et al.
- **Link**: https://arxiv.org/abs/2601.12538
- **Content**: Comprehensive survey organizing agentic reasoning into 3 layers: Foundational (planning, tool use, search) → Self-Evolving (feedback, memory, adaptation) → Collective Multi-Agent (collaboration, coordination).

#### ReasoningBank: Memory-Driven Experience Scaling (ICLR 2026)
- **Affiliation**: Google
- **Innovation**: Memory as a new scaling dimension for agents. Virtuous cycle between memory quality and test-time compute.

#### OpenAgentSafety (ICLR 2026)
- **Affiliation**: CMU
- **Content**: Comprehensive safety evaluation of LLM agents on real tools. 49-73% unsafe behavior rates.

#### Safety Sidecar (ACL 2026)
- **Affiliation**: A*STAR CFAR
- **Innovation**: Runtime safety module for agents using reflective intervention.

#### C-World: Computer Use Agent Environment Creator (ACL 2026)
- **Innovation**: Formalizes agent environment as Action/Task/Transition/Reward quadruple. Uses 5,571 real MCP tools. Evaluation reveals "planning strong, execution weak."

#### Gemini Deep Think (Google DeepMind)
- **Innovation**: Pioneering inference-time scaling for research-level math. Autonomous research paper generation.

#### MLE-Smith: Scaling MLE Tasks with Automated Multi-agent Pipeline (ICLR 2026)
- **Innovation**: Multi-agent pipeline for automating ML research tasks.

### Key Trends

1. **Memory as Scaling Dimension**: Moving beyond context window — structured memory banks that agents query and update.
2. **Test-Time Compute Scaling**: Dynamic allocation of compute per task based on difficulty.
3. **Safety & Alignment**: Runtime guardrails, reflective intervention, and red-teaming for agents.
4. **Multi-Agent Collaboration**: Teams of specialized agents coordinating on complex tasks.
5. **From Code to Science**: Agent systems expanding from software engineering to scientific discovery.

---

## Conference Statistics Summary

| Conference | Year | Submissions | Accepted | Rate |
|-----------|------|-------------|----------|------|
| ICML | 2026 | 23,918 | 6,352 | 26.6% |
| NeurIPS | 2025 | 15,670 | 4,035 | 25.75% |
| ICLR | 2026 | ~16,000+ | 5,342 | ~33% |
| AAAI | 2026 | 23,680 | 4,167 | 17.6% |
| CVPR | 2026 | 16,092 | 4,090 | 25.42% |
| KDD (Research) | 2026 | 1,215 | 256 | 21% |
| EMNLP | 2025 | ~8,000 | ~3,200 | ~40% |
| ACL | 2026 | 12,145 | 2,308 | 19% |
| RecSys | 2025 | ~700+ | ~140 | ~20% |
| SIGIR | 2026 | ~2,000 | ~370 | ~18.4% |

---

## Meta-Trends 2025–2026

1. **Scaling Everywhere**: Scaling laws now apply beyond LLMs to CTR prediction, recommendation, and vision. "Bending the scaling curve" is a key research theme.

2. **Reasoning Test-Time Compute**: From Chain-of-Thought to tree search, hypothesis exploration, and agentic reasoning. Inference-time compute scaling is the dominant paradigm.

3. **Agent Systems Maturation**: Agents move from demo to safety-critical deployment. Memory, reflection, and multi-agent coordination are core research areas.

4. **Diffusion LMs Mature**: Discrete diffusion language models close the gap with autoregressive models, with advantages in controlled generation and planning.

5. **CTR + LLM Convergence**: Language model architectures (Transformers, attention mechanisms) are being adapted for CTR prediction, with dedicated optimizations for recommendation data.

6. **Multimodal Unity**: CVPR and ICLR papers converge on unified architectures that handle vision, language, and 3D natively without modality-specific encoders.

7. **AI for Science**: Both OpenAI and Google DeepMind showcase AI-driven scientific discovery (mathematics, chemistry, biology) as a key application frontier.

8. **Safety as First-Class Concern**: Multiple venues feature dedicated tracks/papers on agent safety, alignment, and evaluation frameworks.
