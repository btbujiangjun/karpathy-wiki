---
title: "Conference & arXiv Digest: 2026-07-22"
type: synthesis
created: 2026-07-22
updated: 2026-07-22
sources: []
tags: [arxiv, conference, ICML, AAAI, NeurIPS, ICLR, KDD, CVPR, ACL, SIGIR, WWW, CIKM, RecSys, LLMs, recommendation, CTR, agents, generative-models, benchmarks]
---

# Conference & arXiv Digest: 2026-07-22

## Table of Contents

1. [ICML 2026](#icml-2026)
2. [AAAI 2026](#aaai-2026)
3. [NeurIPS 2025](#neurips-2025)
4. [ICLR 2026](#iclr-2026)
5. [KDD 2026](#kdd-2026)
6. [CVPR 2026](#cvpr-2026)
7. [ACL 2026](#acl-2026)
8. [SIGIR 2026](#sigir-2026)
9. [WWW 2026](#www-2026)
10. [CIKM 2026](#cikm-2026)
11. [Industry Lab Highlights](#industry-lab-highlights)

---

## ICML 2026

**Venue:** Seoul, Korea | **Date:** July 6–11, 2026  
**Stats:** 6,352 accepted / 23,918 submitted (26.6% acceptance rate)

### LLM Reasoning & Optimization

#### InTRO: In-Token Rationality Optimization
- **Title (EN/CN):** In-Token Rationality Optimization: Towards Accurate and Concise LLM Reasoning via Self-Feedback / 基于自反馈的Token级理性优化：实现精确简洁的LLM推理
- **Authors:** Zhu et al.
- **Affiliation:** Not specified
- **Venue:** ICML 2026
- **Abstract:** Proposes InTRO, enabling token-level exploration and self-feedback for accurate and concise reasoning. Uses correction factors (token-wise importance weights) estimated by information discrepancy between generative policy and answer-conditioned counterpart.
- **Key Innovations:** Token-level exploration within a single forward pass; self-generated feedback mechanism; achieves up to 20% relative improvement over base model on math-reasoning benchmarks
- **Comparison:** Outperforms SFT and RL baselines across six math-reasoning benchmarks; chains of thought are notably more concise
- **Link:** https://ojs.aaai.org/index.php/AAAI/article/view/40826

#### To Grok Grokking: Provable Grokking in Ridge Regression
- **Title (EN/CN):** To Grok Grokking: Provable Grokking in Ridge Regression / 深入理解Grokking：Ridge回归中的可证明Grokking
- **Authors:** Not specified
- **Affiliation:** Not specified
- **Venue:** ICML 2026
- **Abstract:** Studies grokking (onset of generalization long after overfitting) in ridge regression with gradient descent and weight decay. Proves end-to-end grokking results and provides first rigorous quantitative bounds on generalization delay.
- **Key Innovations:** First quantitative bounds on "grokking time"; demonstrates grokking can be amplified or eliminated through hyperparameter tuning
- **Comparison:** First rigorous theoretical analysis of grokking phenomenon
- **Link:** https://icml.cc/virtual/2026/poster/66206

### RL & Policy Optimization

#### Reinforcement Learning with Discrete Diffusion Policies
- **Title (EN/CN):** Reinforcement Learning with Discrete Diffusion Policies for Combinatorial Action Spaces / 基于离散扩散策略的组合动作空间强化学习
- **Authors:** Not specified
- **Affiliation:** Not specified
- **Venue:** ICML 2026
- **Abstract:** Introduces framework for training discrete diffusion models as policies in combinatorial action spaces. Uses policy mirror descent (PMD) for stable target policy distribution, framing policy update as distributional matching.
- **Key Innovations:** Efficient online training for diffusion policies; decoupled approach for stable learning; achieves SOTA on DNA sequence generation, macro-actions, and multi-agent systems
- **Comparison:** Superior sample efficiency compared to baselines; trade-off between FKL (faster convergence) and RKL (higher asymptotic performance)
- **Link:** https://icml.cc/virtual/2026/poster/61107

#### Contextual Slate GLM Bandits with Limited Adaptivity
- **Title (EN/CN):** Contextual Slate GLM Bandits with Limited Adaptivity / 有限自适应性上下文Slate GLM Bandits
- **Authors:** Not specified
- **Affiliation:** Not specified
- **Venue:** ICML 2026
- **Abstract:** Investigates contextual slate bandit problem with generalized linear rewards under limited adaptivity. Proposes batched (O(log log T) batches) and rarely-switching (O(d log T) updates) algorithms.
- **Key Innovations:** Computationally efficient algorithms requiring only poly(N) time per round; regret bounds independent of non-linearity parameter κ
- **Comparison:** Outperforms existing batched baselines; matches fully adaptive Slate-GLM-OFU with slight modification
- **Link:** https://icml.cc/virtual/2026/poster/66297

### Representation Learning

#### Alignment-Sensitive Minimax Rates for Spectral Algorithms with Learned Kernels
- **Title (EN/CN):** Alignment-Sensitive Minimax Rates for Spectral Algorithms with Learned Kernels / 基于学习核的谱算法的对齐敏感极小极大率
- **Authors:** Not specified
- **Affiliation:** Not specified
- **Venue:** ICML 2026
- **Abstract:** Introduces effective span dimension (ESD) as alignment-sensitive complexity measure. Proves minimax excess risk scales as σ²K for models with ESD at most K.
- **Key Innovations:** ESD framework applicable to arbitrary kernels and signals without eigen-decay or source conditions; demonstrates how adaptive feature learning improves generalization through signal-kernel alignment
- **Comparison:** Novel perspective on generalization beyond fixed-kernel theories
- **Link:** https://icml.cc/virtual/2026/poster/66370

---

## AAAI 2026

**Venue:** Singapore | **Date:** January 20–27, 2026  
**Stats:** ~29,000 submissions; 23,000+ under review

### LLM Planning & Reasoning

#### SPIRAL: Symbolic LLM Planning via Grounded and Reflective Search
- **Title (EN/CN):** SPIRAL: Symbolic LLM Planning via Grounded and Reflective Search / SPIRAL：基于接地和反思搜索的符号LLM规划
- **Authors:** Zhang, Ganapavarapu, Jayaraman, Agrawal, Patel, Fokoue
- **Affiliation:** Not specified
- **Venue:** AAAI 2026
- **Abstract:** Embeds three specialized LLM agents (Planner, Simulator, Critic) into MCTS loop. Transforms MCTS from brute-force search into guided, self-correcting reasoning process.
- **Key Innovations:** Integrated planning pipeline with dense reward signals; 83.6% accuracy on DailyLifeAPIs (16+ percentage points improvement)
- **Comparison:** Substantially surpasses Chain-of-Thought and other SOTA agents
- **Link:** https://ojs.aaai.org/index.php/AAAI/article/view/40975

#### PRIME: Planning and Retrieval-Integrated Memory for Enhanced Reasoning
- **Title (EN/CN):** PRIME: Planning and Retrieval-Integrated Memory for Enhanced Reasoning / PRIME：增强推理的规划与检索集成记忆
- **Authors:** Tran, Yao, Tran, Yang, Ouyang, Han, Yu et al.
- **Affiliation:** Not specified
- **Venue:** AAAI 2026
- **Abstract:** Multi-agent reasoning framework integrating System 1 (fast, intuitive) and System 2 (slow, deliberate) thinking. Uses specialized agents for planning, hypothesis generation, retrieval, integration, and decision-making.
- **Key Innovations:** Dynamic integration of dual-process cognition; enables open-source LLMs to compete with GPT-4/GPT-4o on multi-hop and knowledge-grounded reasoning
- **Comparison:** Competitive with GPT-4 and GPT-4o using LLaMA 3 models
- **Link:** https://ojs.aaai.org/index.php/AAAI/article/view/40612

#### Symmetry-Aware Transformer Training for Automated Planning
- **Title (EN/CN):** Symmetry-Aware Transformer Training for Automated Planning / 面向自动规划的对称感知Transformer训练
- **Authors:** Fritzsche, Gestrin, Seipp
- **Affiliation:** Not specified
- **Venue:** AAAI 2026
- **Abstract:** Addresses transformer extrapolation failure from easy to hard planning problems via contrastive learning objective for symmetry awareness. Combines with architectural improvements.
- **Key Innovations:** Novel contrastive learning for symmetry awareness; efficiently trains transformers for plan-generation or heuristic-prediction
- **Comparison:** Effectively addresses PlanGPT limitations across multiple planning domains
- **Link:** https://ojs.aaai.org/index.php/AAAI/article/view/40942

### LLM Safety & Alignment

#### AURA: Affordance-Understanding and Risk-aware Alignment
- **Title (EN/CN):** AURA: Affordance-Understanding and Risk-aware Alignment Technique for Large Language Models / AURA：面向大语言模型的可供性理解与风险感知对齐技术
- **Authors:** Adak, Chatterjee, Banerjee, Hazra, Aditya, Mukherjee
- **Affiliation:** Not specified
- **Venue:** AAAI 2026
- **Abstract:** Multi-layered framework using Process Reward Models (PRMs) for step-level evaluations across logical coherence and safety-awareness. Combines introspective self-critique, fine-grained PRM assessments, and adaptive safety-aware decoding.
- **Key Innovations:** Proactive safety intervention during reasoning; dynamically guides models toward safer reasoning trajectories
- **Comparison:** Significantly surpasses existing methods in logical integrity and affordance-sensitive safety
- **Link:** https://ojs.aaai.org/index.php/AAAI/article/view/41051

---

## NeurIPS 2025

**Venue:** San Diego, USA | **Date:** December 2025  
**Stats:** 5,823 papers

### LLM Reasoning & Code Generation

#### PIPS: Per-Instance Program Synthesis
- **Title (EN/CN):** Once Upon an Input: Reasoning via Per-Instance Program Synthesis / 从输入开始：基于实例级程序合成的推理
- **Authors:** Not specified
- **Affiliation:** Not specified
- **Venue:** NeurIPS 2025
- **Abstract:** Generates and refines programs at instance-level using structural feedback without task-specific guidance or explicit test cases. Incorporates confidence metric for dynamic choice between direct inference and program synthesis.
- **Key Innovations:** 65.1% reduction in undesirable program generations; 8.6% absolute improvement in harmonic mean accuracy over PoT; well-calibrated switching between CoT and synthesis
- **Comparison:** Outperforms PoT and CoT across 30 benchmarks including BBEH, VQA, relational reasoning
- **Link:** https://proceedings.neurips.cc/paper_files/paper/2025/file/c828f33af3c3f669690c2e28ae7af5e2-Paper-Conference.pdf

### Sequence Modeling & Architecture

#### Nested Learning: The Illusion of Deep Learning Architectures
- **Title (EN/CN):** Nested Learning: The Illusion of Deep Learning Architectures / 嵌套学习：深度学习架构的幻象
- **Authors:** Behrouz, Razaviyayn, Zhong, Mirrokni
- **Affiliation:** Not specified
- **Venue:** NeurIPS 2025
- **Abstract:** Presents new learning paradigm coherently representing models as nested, multi-level optimization problems. Reveals existing deep learning methods learn through compressing their own context flow; explains emergence of in-context learning.
- **Key Innovations:** Deep Optimizers (gradient-based optimizers as associative memory); Self-Modifying Titans; Continuum Memory System; HOPE architecture
- **Comparison:** Outperforms Transformers and modern RNNs (DeltaNet, Titans) on language modeling and benchmark tasks
- **Link:** https://proceedings.neurips.cc/paper_files/paper/2025/file/4309616aaed8e848009bc4a7ef73b493-Paper-Conference.pdf

#### Learning to Generalize: Information Perspective on Neural Processes
- **Title (EN/CN):** Learning to Generalize: An Information Perspective on Neural Processes / 学习泛化：神经过程的信息视角
- **Authors:** Li, Liu, Lin, Shi, Fu, Jing
- **Affiliation:** Beijing Jiaotong University
- **Venue:** NeurIPS 2025
- **Abstract:** Proposes information-theoretic framework to analyze generalization bounds of Neural Processes. Introduces dynamical stability regularization to minimize sharpness and improve optimization dynamics.
- **Key Innovations:** Noise-injected parameter updates complementing regularization; tighter generalization bounds validated on 1D regression, image completion, Bayesian optimization
- **Comparison:** Superior predictive performance compared to CNPs, NPs, ANPs, BNPs, TNPs
- **Link:** https://proceedings.neurips.cc/paper_files/paper/2025/file/be187f9b0c9fa3fc0426cde180e96612-Paper-Conference.pdf

---

## ICLR 2026

**Venue:** Brazil | **Date:** 2026  
**Stats:** 5,300+ papers

### Representation Learning

#### GRACE: Generative Representation Learning via Contrastive Policy Optimization
- **Title (EN/CN):** GRACE: Generative Representation Learning via Contrastive Policy Optimization / GRACE：基于对比策略优化的生成式表示学习
- **Authors:** Sun et al.
- **Affiliation:** Not specified
- **Venue:** ICLR 2026
- **Abstract:** Reimagines contrastive signals as rewards guiding generative policy. LLM produces explicit, interpretable rationales encoded into embeddings via mean pooling. Optimized with policy gradient.
- **Key Innovations:** First evidence that contrastive rewards can train policy models for improved representation; transparent decision traces through rationales; 11.5% improvement on MTEB (supervised), 6.9% (unsupervised)
- **Comparison:** Broad cross-category gains on MTEB while preserving general capabilities
- **Link:** https://openreview.net/pdf?id=hs9lwjH1bJ

#### Unsupervised Representation Learning - Invariant Risk Minimization
- **Title (EN/CN):** Unsupervised Representation Learning - an Invariant Risk Minimization Perspective / 无监督表示学习——不变风险最小化视角
- **Authors:** Not specified
- **Affiliation:** Not specified
- **Venue:** ICLR 2026
- **Abstract:** Extends IRM to settings without labels via feature distribution alignment. Introduces PICA (linear method) and VIAE (deep generative model) for separating environment-invariant and environment-dependent factors.
- **Key Innovations:** Novel unsupervised structural causal model; environment-conditioned sample generation and intervention
- **Comparison:** Effective in capturing invariant structure without labels on MNIST, CelebA
- **Link:** https://iclr.cc/virtual/2026/poster/10009942

### RL & Representation

#### Spectral Bellman Method
- **Title (EN/CN):** Spectral Bellman Method: Unifying Representation and Exploration in RL / 谱Bellman方法：统一RL中的表示与探索
- **Authors:** Not specified
- **Affiliation:** Not specified
- **Venue:** ICLR 2026
- **Abstract:** Introduces framework derived from Inherent Bellman Error condition. Discovers fundamental spectral relationship: under zero-IBE, Bellman operator transformation of value functions links to feature covariance structure.
- **Key Innovations:** Theoretically-grounded objective for Bellman-aligned features; structured exploration via feature covariance alignment; extends to multi-step Bellman operators
- **Comparison:** Improves performance in hard-exploration and long-horizon tasks
- **Link:** https://iclr.cc/virtual/2026/poster/10006992

---

## KDD 2026

**Venue:** Jeju Island, Korea | **Date:** August 9–13, 2026  
**Stats:** 256 accepted / 1,215 submissions (21%)

### Recommendation Systems

#### SRPFN: One Sequential Recommendation Model Pretrained from Synthetic Priors
- **Title (EN/CN):** One Sequential Recommendation Model Pretrained from Synthetic Priors Predicts Multiple Datasets / 基于合成先验预训练的序列推荐模型预测多数据集
- **Authors:** Kang, Jeong, Shin, Choi, Park
- **Affiliation:** KAIST
- **Venue:** KDD 2026
- **Abstract:** Pretrained on synthetic datasets from parametric prior (hierarchical degree-corrected stochastic block model), adapts predictions in update-free manner via support set conditioning.
- **Key Innovations:** Single forward pass inference without gradient updates; 7.53% average improvement over second-best method; ~1 minute inference per dataset vs minutes-hours for baselines
- **Comparison:** Outperforms training-free baselines by substantial margin; competitive with models trained directly on target data
- **Link:** https://arxiv.org/pdf/2606.15752v1

#### DeGRe: Dense-supervised Generative Reranking
- **Title (EN/CN):** DeGRe: Dense-supervised Generative Reranking for Recommendation / DeGRe：用于推荐的稠密监督生成式重排序
- **Authors:** Song, Zhang, Chen, Sang, Zhao, Cao, Wu, Cai, Jia
- **Affiliation:** Zhejiang University / Alibaba (Taobao)
- **Venue:** KDD 2026
- **Abstract:** Offline-online decoupled design: Lookahead Evaluator mines high-value sequences offline; distills into lightweight Online Generator for single greedy decoding pass online.
- **Key Innovations:** Cumulative-regression-based lookahead evaluation; dense supervision signals; 29.90%-53.19% absolute improvement over SOTA on public benchmarks
- **Comparison:** Outperforms GoalRank, NAR4Rec; deployed on Taobao Flash Shopping with +2.85% CTR, +3.75% GMV
- **Link:** https://arxiv.org/html/2605.25749v1

#### SPiKE: Enriching Semantic Profiles into Knowledge Graph for Recommender Systems Using LLMs
- **Title (EN/CN):** SPiKE: Enriching Semantic Profiles into Knowledge Graph for Recommender Systems Using LLMs / SPiKE：使用LLM为推荐系统丰富知识图谱语义轮廓
- **Authors:** Not specified
- **Affiliation:** Not specified
- **Venue:** KDD 2026
- **Abstract:** Uses LLMs to enrich knowledge graph entity profiles with hierarchical semantic attributes. Three components: entity profile enrichment, profile-aware KG aggregation, and pairwise profile preference matching.
- **Key Innovations:** Broader preference modeling through LLM-enhanced profiles; consistent performance gains
- **Comparison:** Novel approach to integrating LLMs with knowledge graphs for recommendation
- **Link:** https://arxiv.org/html/2601.08148v1

### Human Simulation

#### HumanLLM: Towards Personalized Understanding and Simulation of Human Nature
- **Title (EN/CN):** HumanLLM: Towards Personalized Understanding and Simulation of Human Nature / HumanLLM：迈向人类本性的个性化理解与模拟
- **Authors:** Not specified
- **Affiliation:** Not specified
- **Venue:** KDD 2026
- **Abstract:** Framework for personalized understanding and simulation of human nature using LLMs.
- **Key Innovations:** Combines LLM capabilities with human behavior modeling
- **Link:** https://arxiv.org/html/2601.15793v1

---

## CVPR 2026

**Venue:** June 2026

### Multimodal Models

#### TUNA: Taming Unified Visual Representations for Native Unified Multimodal Models
- **Title (EN/CN):** TUNA: Taming Unified Visual Representations for Native Unified Multimodal Models / TUNA：为原生统一多模态模型驯服统一视觉表示
- **Authors:** Liu et al.
- **Affiliation:** Multiple institutions
- **Venue:** CVPR 2026
- **Abstract:** Builds unified continuous visual representation by cascading VAE encoder with representation encoder. Enables end-to-end processing for understanding and generation.
- **Key Innovations:** Unified visual space avoids representation format mismatches; stronger pretrained encoders consistently yield better performance; joint training benefits both understanding and generation
- **Comparison:** Outperforms decoupled alternatives; competitive with leading understanding-only and generation-only models
- **Link:** https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_TUNA_Taming_Unified_Visual_Representations_for_Native_Unified_Multimodal_Models_CVPR_2026_paper.pdf

#### Franca: Nested Matryoshka Clustering for Scalable Visual Representation Learning
- **Title (EN/CN):** Franca: Nested Matryoshka Clustering for Scalable Visual Representation Learning / Franca：用于可扩展视觉表示学习的嵌套Matryoshka聚类
- **Authors:** Venkataramanan et al.
- **Affiliation:** Not specified
- **Venue:** CVPR 2026
- **Abstract:** First fully open-source (data, code, weights) VFM matching/surpassing proprietary models. Uses Matryoshka multi-head clustering and RASA post-pretraining.
- **Key Innovations:** CyclicMask for semantic feature learning; Matryoshka embeddings for multi-resolution representations; RASA removes spatial position biases
- **Comparison:** Outperforms DINOv2 by up to 3% on in-context learning; surpasses on OOD detection and 3D understanding
- **Link:** https://openaccess.thecvf.com/content/CVPR2026/papers/Venkataramanan_Franca_Nested_Matryoshka_Clustering_for_Scalable_Visual_Representation_Learning_CVPR_2026_paper.pdf

### Vision-Language Models

#### TTRV: Test-Time Reinforcement Learning for Vision Language Models
- **Title (EN/CN):** TTRV: Test-Time Reinforcement Learning for Vision Language Models / TTRV：视觉语言模型的测试时强化学习
- **Authors:** Singh et al.
- **Affiliation:** Not specified
- **Venue:** CVPR 2026
- **Abstract:** Enhances VLMs by adapting on-the-fly at inference time without labeled data. Uses GRPO with frequency-based and entropy-based rewards.
- **Key Innovations:** Improvements up to 52.4% on recognition, 29.8% on VQA; even single randomly chosen unlabeled example yields 5.5% improvement; outperforms GPT-4o by 2.3% on image classification
- **Comparison:** Consistent gains across 16 datasets; demonstrates GRPO activates latent capabilities from pretraining
- **Link:** https://openaccess.thecvf.com/content/CVPR2026/papers/Singh_TTRV_Test-Time_Reinforcement_Learning_for_Vision_Language_Models_CVPR_2026_paper.pdf

#### Taxonomy-Aware Representation Alignment (TARA)
- **Title (EN/CN):** Taxonomy-Aware Representation Alignment for Hierarchical Visual Recognition with Large Multimodal Models / 面向大视觉语言模型层级视觉识别的分类感知表示对齐
- **Authors:** He, Tan, Peng
- **Affiliation:** Peking University
- **Venue:** CVPR 2026
- **Abstract:** Injects taxonomic knowledge into LMMs by aligning with biology foundation model representations. Enables recognition of both known and novel categories.
- **Key Innovations:** Aligns intermediate LMM features with BFM targets; flexible bridging between contextualized visual features and categories
- **Comparison:** Consistently enhances hierarchical consistency and leaf node accuracy with only 1-shot supervision
- **Link:** https://openaccess.thecvf.com/content/CVPR2026/papers/He_Taxonomy-Aware_Representation_Alignment_for_Hierarchical_Visual_Recognition_with_Large_Multimodal_CVPR_2026_paper.pdf

---

## ACL 2026

**Venue:** San Diego, California | **Date:** July 2–7, 2026  
**Theme:** "Explainability of NLP Models"

### Agent Systems

#### KARL: Reinforcement Learning for LLM Agents on Multi-Turn Knowledge-Intensive Agentic Tasks
- **Title (EN/CN):** KARL: Reinforcement Learning for LLM Agents on Multi-Turn Knowledge-Intensive Agentic Tasks / KARL：面向多轮知识密集型智能体任务的LLM智能体强化学习
- **Authors:** Sun, Liu, Lv, Zhang, Jing, Qi, Xu, Dong, Tang
- **Affiliation:** Not specified
- **Venue:** ACL 2026
- **Abstract:** RL framework for LLM agents on multi-turn knowledge-intensive tasks.
- **Key Innovations:** Combines RL with knowledge retrieval for multi-turn agent tasks
- **Link:** https://aclanthology.org/2026.acl-long.2196/

#### Grammar Search for Multi-Agent Systems
- **Title (EN/CN):** Grammar Search for Multi-Agent Systems / 多智能体系统的语法搜索
- **Authors:** Singh, Yadav, Malay, Nayak, Rajeswar, Madhusudhan, Blanco
- **Affiliation:** Not specified
- **Venue:** ACL 2026
- **Abstract:** Proposes grammar-based search approach for multi-agent systems.
- **Key Innovations:** Novel grammar search methodology for agent coordination
- **Link:** https://aclanthology.org/2026.acl-long.75/

### LLM Reasoning

#### MTSQL-R1: Towards Long-Horizon Multi-Turn Text-to-SQL Via Agentic Training
- **Title (EN/CN):** MTSQL-R1: Towards Long-Horizon Multi-Turn Text-to-SQL Via Agentic Training / MTSQL-R1：通过智能体训练实现长时域多轮Text-to-SQL
- **Authors:** Guo, Wang, Liu, Golalikhani, Chen, Zhang, Reddy
- **Affiliation:** Not specified
- **Venue:** ACL 2026
- **Abstract:** Agentic training framework for long-horizon multi-turn Text-to-SQL.
- **Key Innovations:** Combines agentic training with SQL generation
- **Link:** https://www.paperdigest.org/2026/06/acl-2026-papers-highlights/

#### Think in Sentences: Explicit Sentence Boundaries Enhance Language Model's Capabilities
- **Title (EN/CN):** Think in Sentences: Explicit Sentence Boundaries Enhance Language Model's Capabilities / 以句子思考：显式句子边界增强语言模型能力
- **Authors:** Not specified
- **Affiliation:** Not specified
- **Venue:** ACL 2026
- **Abstract:** Shows that sentence boundary delimiters improve performance on various tasks including DROP (12.5% improvement).
- **Key Innovations:** Validates that sentence awareness improves language modeling; improvements across 7B to 70B parameter models
- **Comparison:** Up to 7.7% improvement on various benchmarks
- **Link:** https://aclanthology.org/2026.acl-long.104.pdf

---

## SIGIR 2026

**Venue:** Melbourne, Australia | **Date:** July 20–24, 2026

### Agentic Search

#### Agentic Search in the Wild: Intents and Trajectory Dynamics from 14M+ Real Search Requests
- **Title (EN/CN):** Agentic Search in the Wild: Intents and Trajectory Dynamics from 14M+ Real Search Requests / 野外智能体搜索：来自1400万+真实搜索请求的意图与轨迹动态
- **Authors:** Ning, Coelho, Kong, Long, Martins, Magalhães, Callan, Xiong
- **Affiliation:** Carnegie Mellon University / others
- **Venue:** SIGIR 2026
- **Abstract:** Large-scale log analysis of 14.44M search requests (3.97M sessions). Analyzes agentic search behavior, intent-conditioned reformulation patterns, and evidence traceability.
- **Key Innovations:** Context-driven Term Adoption Rate (CTAR) metric; finding that 54% of new query terms are traceable to retrieved evidence; 90%+ multi-turn sessions contain at most 10 steps
- **Comparison:** First large-scale empirical study of agentic search dynamics
- **Link:** https://export.arxiv.org/pdf/2601.17617

### Retrieval Models

#### CoveR: Coverage-Aware Retrieval with Augmented Sub-Question Answerability
- **Title (EN/CN):** CoveR: Coverage-Aware Retrieval with Augmented Sub-Question Answerability / CoveR：基于增强子问题可答性的覆盖感知检索
- **Authors:** Ju, Yang, Adriaanse, Verberne, Yates
- **Affiliation:** University of Amsterdam / others
- **Venue:** SIGIR 2026
- **Abstract:** Bi-encoder trained with coverage contrastive and coverage self-distillation losses. Creates SCOPE training dataset with augmented coverage signals.
- **Key Innovations:** Coverage-based training for long-form RAG; improves nugget coverage without harming relevance; strong performance on BEIR benchmark
- **Comparison:** Outperforms SPLADE-v3, Nomic-Embed, Qwen3-Embed on coverage metrics
- **Link:** https://arxiv.org/pdf/2605.28522v1

#### Revisiting BM25 Feedback Models using HyDE
- **Title (EN/CN):** Revisiting BM25 Feedback Models using HyDE / 使用HyDE重新审视BM25反馈模型
- **Authors:** Jedidi, Lin
- **Affiliation:** University of Waterloo
- **Venue:** SIGIR 2026
- **Abstract:** Shows BM25 feedback models (Rocchio, RM3) can benefit from HyDE-generated documents. Demonstrates mutual benefit: feedback models improve HyDE by up to 2.2 points on BEIR.
- **Key Innovations:** First proper comparison of different feedback mechanisms with LLM-generated feedback; reveals traditional PRF literature remains highly relevant
- **Comparison:** HyDE + Rocchio achieves 4.2% improvement over string concatenation approach
- **Link:** https://cs.uwaterloo.ca/~jimmylin/publications/Jedidi_Lin_SIGIR2026.pdf

#### LTRR: Learning To Rank Retrievers for LLMs
- **Title (EN/CN):** LTRR: Learning To Rank Retrievers for LLMs / LTRR：面向LLM的检索器排序学习
- **Authors:** Not specified
- **Affiliation:** Not specified
- **Venue:** SIGIR 2026
- **Abstract:** Query routing framework that learns to rank retrievers based on downstream utility to LLMs. Trained routers using AC utility metric and pairwise learning-to-rank.
- **Key Innovations:** Utility-aware retriever selection; generalizes to unseen query types
- **Comparison:** Outperforms standard single-retriever RAG systems
- **Link:** https://arxiv.org/html/2506.13743v2

---

## WWW 2026

**Venue:** Dubai, UAE | **Date:** April 13–17, 2026

### Recommendation Systems

#### Don't Waste It: Guiding Generative Recommenders with Structured Human Priors
- **Title (EN/CN):** Don't Waste It: Guiding Generative Recommenders with Structured Human Priors via Multi-head Decoding / 不要浪费：通过多头解码引导结构化人类先验的生成式推荐器
- **Authors:** Zhang, Zhang, Lin, Qiu, Yu, Liu, Xia, Yu, Zheng, Yang et al.
- **Affiliation:** Meta AI / UC Berkeley / UC Santa Cruz
- **Venue:** WWW 2026
- **Abstract:** Backbone-agnostic framework integrating human priors directly into end-to-end training via prior-conditioned adapter heads. Introduces hierarchical composition for complex prior interactions.
- **Key Innovations:** Lightweight adapter heads (0.14% of model params each); disentangles user intent along human-understandable axes; enhances accuracy, diversity, novelty, and personalization
- **Comparison:** Consistent improvements over HSTU and HLLM backbones; enables effective use of longer context and larger models
- **Link:** https://arxiv.org/pdf/2511.10492

#### CTRL-Rec: Controlling Recommender Systems With Natural Language
- **Title (EN/CN):** CTRL-Rec: Controlling Recommender Systems With Natural Language / CTRL-Rec：用自然语言控制推荐系统
- **Authors:** Carroll, Foote, Feng, Williams, Dragan, Knox et al.
- **Affiliation:** FAIR at Meta
- **Venue:** WWW 2026
- **Abstract:** Allows natural language control of traditional recommender systems in real-time. Uses LLM to simulate user approval, trains embedding models to approximate judgments.
- **Key Innovations:** Single LLM embedding computation per request; real-time control; distills synthetic LLM judgments
- **Comparison:** Significant enhancement in users' sense of control and satisfaction without reducing engagement
- **Link:** https://doi.org/10.48550/arxiv.2510.12742

#### NEZHA: A Zero-sacrifice and Hyperspeed Decoding Architecture for Generative Recommendations
- **Title (EN/CN):** NEZHA：面向生成式推荐的零牺牲超高速解码架构 / NEZHA：A Zero-sacrifice and Hyperspeed Decoding Architecture for Generative Recommendations
- **Authors:** Wang, Zhou, Lu, Liu, Liu, Wang, Zhang, Li, Su, Wang, Xu, Zhao
- **Affiliation:** City University of Hong Kong / Alibaba Group
- **Venue:** WWW 2026
- **Abstract:** Self-drafting architecture with model-free hash set verification. Eliminates need for separate draft model; verifies via near-instantaneous hash lookup.
- **Key Innovations:** 2.6× algorithm-level speedup; deployed on Taobao since October 2025; 1.2% business improvement (billion-level advertising revenue)
- **Comparison:** Zero-sacrifice accuracy while reducing latency to production-viable levels
- **Link:** https://arxiv.org/html/2511.18793v2

---

## CIKM 2026

**Venue:** Rome, Italy | **Date:** 2026

### Industrial Recommendation

#### HiGR: Industrial-Scale Hierarchical Generative Slate Recommendation Framework
- **Title (EN/CN):** HiGR: Industrial-Scale Hierarchical Generative Slate Recommendation Framework in Tencent / HiGR：腾讯工业级层级生成式Slate推荐框架
- **Authors:** Pang, Liu, Li, Zhu, Luo, Yu, Wu, Shen, Xu, Wang, Jiang, Zhuo, Li
- **Affiliation:** Tencent
- **Venue:** CIKM 2026
- **Abstract:** Hierarchical framework bridging generative recommendation to industrial slate recommendation. Uses PCRQ-VAE for structured SIDs, Hierarchical Slate Decoder, and ORPO-based listwise alignment.
- **Key Innovations:** Prefix Contrastive Residual Quantized VAE; coarse-to-fine slate generation; multi-objective alignment (ranking fidelity, user interest, diversity)
- **Comparison:** Outperforms SOTA by >10% offline; 5× inference speedup; online improvements: +1.22% watch time, +1.73% video plays
- **Link:** https://arxiv.org/pdf/2512.24787v5

---

## Industry Lab Highlights

### Google DeepMind

#### Towards Structural Understanding of LLM Overthinking
- **Title (EN/CN):** Towards Structural Understanding of LLM Overthinking / 迈向LLM过度思考的结构化理解
- **Authors:** Google DeepMind team
- **Venue:** ACL 2026
- **Abstract:** Analyzes thought processes in third-party LLMs (Qwen3, DeepSeek-R1 distilled). Proposes TRACE analyzer decomposing thoughts into sub-thoughts with discourse relationships.
- **Key Innovations:** Two prevalent patterns: Explorer and Late Landing; over-verification and over-exploration as primary drivers; utility-based definition beyond length metrics
- **Link:** https://deepmind.google/research/publications/203490/

#### How LLMs Detect and Correct Their Own Errors
- **Title (EN/CN):** How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals / LLM如何检测和纠正自身错误：内部置信度信号的作用
- **Authors:** Kumaran, Patraucean, Osindero, Veličković, Daw
- **Affiliation:** Google DeepMind / Princeton
- **Venue:** Not specified
- **Abstract:** Investigates error detection through second-order confidence models. Discovers PANL (post-answer newline) token caches confidence representation causally driving verbal confidence.
- **Key Innovations:** PANL predicts error detection beyond verbal confidence; predicts which errors can be corrected; causal interventions confirm PANL signals rescue error detection
- **Comparison:** Replicates across Gemma 3 27B and Qwen 2.5 7B
- **Link:** https://arxiv.org/html/2604.22271v1

#### Code-Space Response Oracles (CSRO)
- **Title (EN/CN):** Code-Space Response Oracles: Generating Interpretable Multi-Agent Policies with LLMs / 代码空间响应预言机：使用LLM生成可解释的多智能体策略
- **Authors:** Hennes, Li, Schultz, Lanctot
- **Affiliation:** Google DeepMind
- **Venue:** Not specified
- **Abstract:** Replaces RL oracles with LLMs that generate policies as human-readable code. Uses iterative refinement and AlphaEvolve for optimization.
- **Key Innovations:** Interpretable policy generation; leverages LLM pretrained knowledge; competitive with black-box RL policies while providing full transparency
- **Link:** https://arxiv.org/pdf/2603.10098v1

#### Discovering Multiagent Learning Algorithms with LLMs
- **Title (EN/CN):** Discovering Multiagent Learning Algorithms with Large Language Models / 使用大语言模型发现多智能体学习算法
- **Authors:** Li, Schultz, Hennes, Lanctot
- **Affiliation:** Google DeepMind
- **Venue:** Not specified
- **Abstract:** Uses AlphaEvolve to navigate design spaces of CFR and PSRO. Discovers VAD-CFR and SHOR-PSRO competitive with SOTA across 18-game evaluation suite.
- **Key Innovations:** Automated algorithm discovery; distillation to minimal solvers (WOP-CFR, PM-PSRO); methodology for LLMs in algorithmic discovery
- **Comparison:** Competitive with human-designed baselines; distilled versions achieve superior generalization
- **Link:** https://arxiv.org/pdf/2602.16928

#### Efficient Online RLHF (10x-1000x Data Efficiency)
- **Title (EN/CN):** Online RLHF with 10x-1000x Data Efficiency / 具有10x-1000x数据效率的在线RLHF
- **Authors:** Asghari, Chute, Dwaracherla et al.
- **Affiliation:** Google DeepMind
- **Venue:** Not specified
- **Abstract:** Online learning algorithm incrementally updating reward and language models. Uses epistemic neural network for reward uncertainty and information-directed exploration.
- **Key Innovations:** Matches offline RLHF (200K labels) with <20K choices (10x gain); projected 1,000x gain at 1M labels; unprecedented data efficiency
- **Comparison:** First demonstration of such large efficiency gains with LLMs
- **Link:** https://arxiv.org/pdf/2603.17378

### OpenAI

#### GPT-5.6 Family (Sol, Terra, Luna)
- **Title (EN/CN):** GPT-5.6: Frontier intelligence that scales with your ambition / GPT-5.6：随雄心扩展的前沿智能
- **Authors:** OpenAI
- **Venue:** Product release (July 9, 2026)
- **Abstract:** Three-model family: Sol (flagship), Terra (balanced), Luna (cost-efficient). Sol achieves 53.6 on Agents' Last Exam, 80 on Artificial Analysis Coding Agent Index, 92.2% on BrowseComp, 62.6% on OSWorld 2.0.
- **Key Innovations:** New `max` reasoning effort; `ultra` mode with parallel agents; 6x fewer prompt injection failures vs. GPT-5.5; state-of-the-art on Terminal-Bench 2.1, DeepSWE
- **Comparison:** Outperforms Claude Fable 5 by 13.1 points on Agents' Last Exam; 61% less time at half cost on Intelligence Index
- **Link:** https://openai.com/index/gpt-5-6/

#### GPT-Red: Self-Improvement for Robustness
- **Title (EN/CN):** GPT-Red: Unlocking Self-Improvement for Robustness / GPT-Red：解锁自我改进的鲁棒性
- **Authors:** OpenAI
- **Venue:** Blog post (July 15, 2026)
- **Abstract:** Automated red-teaming model trained via self-play RL. Used to generate prompt injections for GPT-5.6 training, achieving 6x robustness improvement.
- **Key Innovations:** Self-play training for safety; GPT-Red finds 84% of attacks vs 13% for humans; applied during training of production models since GPT-5.3
- **Comparison:** GPT-5.6 Sol fails on only 0.05% of GPT-Red's direct prompt injections
- **Link:** https://openai.com/index/unlocking-self-improvement-gpt-red

#### GeneBench: Multi-Stage Inference in Genomics
- **Title (EN/CN):** GeneBench: Assessing AI Agents for Multi-Stage Inference Problems in Genomics / GeneBench：评估AI智能体在基因组学多阶段推理问题中的表现
- **Authors:** OpenAI / Herasight
- **Venue:** Paper (April 23, 2026)
- **Abstract:** 103 evaluations across 10 genomics domains requiring multi-step analysis. GPT-5.5 reaches 25.0% pass rate; GPT-5.5 Pro reaches 33.2%.
- **Key Innovations:** Captures broader scope of computational science work; measures emerging capability that remains unreliable
- **Comparison:** Strongest external baseline (Gemini 3.1 Pro) achieves 11.2%
- **Link:** https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf

### Meta AI

#### LLM Retrieval for Stable and Predictable Ad Recommendations
- **Title (EN/CN):** LLM Retrieval for Stable and Predictable Ad Recommendations / 用于稳定可预测广告推荐的LLM检索
- **Authors:** Sunkara, Karuppusamy, Xu et al.
- **Affiliation:** Meta Platforms
- **Venue:** Not specified
- **Abstract:** Introduces evaluation framework for stability and predictability of ads recommender systems. Uses fine-tuned LLMs for semantic candidate generation.
- **Key Innovations:** Hierarchical semantic attributes from ad creatives; graph-based expansion for semantic variants; 0.45% topline lift, 1.2% recall improvement, 8.62% reduction in A/A' difference, 45% MAD improvement
- **Comparison:** Significant improvements in predictability and traditional performance metrics
- **Link:** https://arxiv.org/html/2605.21969v1

#### Efficient Retrieval Scaling with Hierarchical Indexing (HILL)
- **Title (EN/CN):** Efficient Retrieval Scaling with Hierarchical Indexing for Large Scale Recommendation / 大规模推荐中层级索引的高效检索扩展
- **Authors:** Yang et al.
- **Affiliation:** Meta
- **Venue:** EDBT 2026
- **Abstract:** Jointly learns hierarchical index using cross-attention and residual quantization. Successfully deployed at Meta for daily ads recommendations.
- **Key Innovations:** "Test-time training" via fine-tuning on intermediate node data; deployed supporting billions of Facebook/Instagram users; 2.57% online ads metric gain
- **Comparison:** Novel approach to foundation retrieval model deployment
- **Link:** https://ar5iv.labs.arxiv.org/html/2604.12965

### ByteDance

#### TokenMixer-Large: Scaling Up Large Ranking Models
- **Title (EN/CN):** TokenMixer-Large: Scaling Up Large Ranking Models in Industrial Recommenders / TokenMixer-Large：在工业推荐系统中扩展大型排序模型
- **Authors:** Jiang, Zhu, Han, Lu, Bai et al.
- **Affiliation:** ByteDance AML
- **Venue:** Not specified
- **Abstract:** Scales recommendation models to 7B parameters online (15B offline). Introduces mixing-and-reverting operation, inter-layer residuals, and Sparse Per-token MoE.
- **Key Innovations:** Successfully deployed across Douyin; +1.66% orders, +2.98% GMV (e-commerce); +2.0% ADSS (ads); +1.4% revenue (live streaming)
- **Comparison:** Outperforms Wukong, HiFormer, DHEN, Group Transformer, FAT, RankMixer
- **Link:** https://arxiv.org/html/2602.06563v2

#### UG-Separated TokenMixer for Efficient Inference
- **Title (EN/CN):** Compute Only Once: UG-Separated TokenMixer for Efficient Large Recommendation Models / 仅计算一次：用于高效大型推荐模型的UG分离TokenMixer
- **Authors:** Lu, Chai, Bai, Zhang et al.
- **Affiliation:** ByteDance AML
- **Venue:** Not specified
- **Abstract:** Enables user-side computation reusable in TokenMixer-based models. Explicitly disentangles user-side and item-side information flows.
- **Key Innovations:** Up to 20% inference latency reduction; W8A16 quantization for memory bottleneck; deployed across Douyin, Hongguo, Chuanshanjia, Qianchuan
- **Comparison:** Maintains stable online metrics while achieving significant acceleration
- **Link:** https://arxiv.org/html/2602.10455v2

### Alibaba

#### SIGMA: Semantic-Grounded Instruction-Driven Generative Multi-Task Recommender
- **Title (EN/CN):** SIGMA: A Semantic-Grounded Instruction-Driven Generative Multi-Task Recommender at AliExpress / SIGMA：AliExpress上基于语义的指令驱动生成式多任务推荐器
- **Authors:** Not specified
- **Affiliation:** Alibaba Group (AliExpress)
- **Venue:** SIGIR 2026
- **Abstract:** LLM-powered generative recommendation reshaping recommender system paradigm.
- **Key Innovations:** Semantic-grounded instruction-driven approach for multi-task recommendation
- **Link:** https://dl.acm.org/doi/10.1145/3805712.3808421

#### GFlowGR: Fine-tuning Generative Recommendations with GFlowNets
- **Title (EN/CN):** GFlowGR: Fine-tuning Generative Recommendation Frameworks with Generative Flow Networks / GFlowGR：使用生成式流网络微调生成式推荐框架
- **Authors:** Wang, Zhou, Lu, Liu, Li, Zhang, Li, Wang, Xu, Zheng, Zhao
- **Affiliation:** City University of Hong Kong / Alibaba Group
- **Venue:** Not specified
- **Abstract:** GFlowNet-based fine-tuning with trajectory sampler, reward model, and flow-matching objectives. Deployed across Taobao's advertising businesses since May 2025.
- **Key Innovations:** Learning from item sets; diverse trajectory sampling; multi-faceted reward modeling; 1% revenue increase (billion-level)
- **Comparison:** Significantly outperforms GRPO and SFT baselines
- **Link:** https://arxiv.org/html/2506.16114v2

---

## Cross-cutting Themes

### 1. Generative Recommendation at Scale
- **Key Papers:** NEZHA (Alibaba), GFlowGR (Alibaba), HiGR (Tencent), SRPFN (KDD), DeGRe (Alibaba/Taobao)
- **Trend:** Industrial deployment of LLM-based generative recommendation is accelerating, with solutions addressing inference latency (speculative decoding, hierarchical generation) and training efficiency (GFlowNets, dense supervision)

### 2. LLM Agent Systems
- **Key Papers:** KARL (ACL), SPIRAL (AAAI), PRIME (AAAI), CSRO (DeepMind), Agentic Search (SIGIR)
- **Trend:** Multi-agent frameworks combining planning, retrieval, and reasoning; self-play for algorithm discovery; real-world deployment of agentic search

### 3. Test-Time Adaptation & Self-Improvement
- **Key Papers:** TTRV (CVPR), GPT-Red (OpenAI), Efficient RLHF (DeepMind)
- **Trend:** Models improving at inference time without labeled data; automated red-teaming for robustness; dramatic data efficiency gains in RLHF

### 4. Unified Multimodal Models
- **Key Papers:** TUNA (CVPR), Franca (CVPR), TARA (CVPR)
- **Trend:** Unified visual representations for understanding and generation; open-source models matching proprietary performance; test-time RL for VLMs

### 5. Industrial Recommendation at ByteDance/Alibaba/Meta
- **Key Papers:** TokenMixer-Large (ByteDance), HILL (Meta), LLM Retrieval (Meta), UG-Sep (ByteDance)
- **Trend:** Scaling recommendation models to 7B+ parameters; hierarchical indexing for efficient retrieval; semantic-aware candidate generation for stability

### 6. Safety & Alignment
- **Key Papers:** GPT-Red (OpenAI), AURA (AAAI), Towards Structural Understanding of LLM Overthinking (DeepMind)
- **Trend:** Automated safety testing at scale; process reward models for step-level safety; understanding overthinking patterns

---

*Generated on 2026-07-22 by karpathy-wiki maintainer*
