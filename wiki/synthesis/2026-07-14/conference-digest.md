---
title: "Conference & arXiv Digest — ICML/AAAI/NeurIPS/ICLR/CVPR/KDD/ACL/SIGIR/WWW 2026"
type: synthesis
created: 2026-07-14
updated: 2026-07-14
sources: [arxiv, conference-proceedings]
tags: [conference-digest, icml-2026, aaai-2026, neurips-2025, iclr-2026, cvpr-2026, kdd-2026, acl-2026, sigir-2026, www-2026, llm, recommendation, ctr, agents, games, generative-models]
---

# Conference & arXiv Digest — 2026-07-14

> Comprehensive digest of recent papers from top ML/AI conferences and arXiv, covering LLMs, recommendation systems, advertising, CTR, games, code execution, agent systems, generative models, sequential modeling, and benchmarks.

---

## 1. ICML 2026 (Seoul, July 6–12, 2026)

**Stats**: 23,918 submissions → 6,352 accepted (26.6%) → 536 Spotlight (2.2%) → 168 Oral (0.7%)

### Outstanding Paper Awards

#### 1.1 The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models
- **Authors**: Zanlin Ni, Shenzhi Wang, Yang Yue, Tianyu Yu, Weilin Zhao, Yeguo Hua, Tianyi Chen, Jun Song, Cheng Yu, Bo Zheng, Gao Huang
- **Affiliation**: Tsinghua University
- **Venue**: ICML 2026 Outstanding Paper Award
- **Abstract & Key Innovation**: Challenges the core assumption that "arbitrary order generation" in diffusion language models (dLLMs) is beneficial. The paper proves that unrestricted token ordering actually hurts performance on mathematical and programming tasks — the "flexibility trap." They propose **JustGRPO**, which enforces left-to-right autoregressive order during RL fine-tuning, achieving 89.1% on GSM8K and 45.1% on MATH-500 while preserving parallel decoding speed.
- **Comparison**: Prior work (e.g., MDLM, SEDD) claimed arbitrary-order generation as a key advantage over autoregressive models. This paper shows that flexibility is a trap for structured tasks.
- **Link**: https://icml.cc/virtual/2026/oral/71086

#### 1.2 High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions
- **Authors**: Fan Chen, Sinho Chewi, Constantinos Daskalakis, Alexander Rakhlin
- **Affiliation**: MIT, Yale
- **Venue**: ICML 2026 Outstanding Paper Award
- **Abstract & Key Innovation**: Proves that with only Õ(δ)-precision score estimates, a diffusion model can be sampled to δ-error in polylog(1/δ) steps — an exponential improvement over prior results. Pushes the theoretical ceiling for diffusion model sampling accuracy.
- **Link**: https://icml.cc/virtual/2026/oral/71132

### Outstanding Position Paper Award

#### 1.3 Position: The Alignment Community is Unintentionally Building a Censor's Toolkit
- **Authors**: Sarah Ball, Phil Hackemann
- **Venue**: ICML 2026 Outstanding Position Paper
- **Key Innovation**: Warns that safety mechanisms (RLHF, Constitutional AI, content filters) developed by the alignment community are being systematically repurposed as infrastructure for political censorship and information control. Calls for the field to confront this structural risk.

### Honorable Mentions (Outstanding Paper)

#### 1.4 The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes
- **Authors**: Mohammad Taufeeque, Stefan Heimersheim, Adam Gleave, Chris Cundy
- **Key Innovation**: Uses "deception probes" to map where honesty emerges during RL with Verifiable Rewards (RLVR) training, providing diagnostic tools for AI safety.

#### 1.5 Motion Attribution for Video Generation
- **Authors**: Xindi Wu, Despoina Paschalidou, Jun Gao, Antonio Torralba, Laura Leal-Taixé, Olga Russakovsky, Sanja Fidler, Jonathan Lorraine
- **Key Innovation**: Attribution method for video generation that identifies which training data/components drive specific motion behaviors.

#### 1.6 How Much Can Language Models Memorize?
- **Authors**: John Xavier Morris, Chawin Sitawarin, Narine Kokhlikyan, Chuan Guo, G. Edward Suh, Alexander M. Rush, Kamalika Chaudhuri, Saeed Mahloujifar
- **Key Innovation**: Distinguishes intended memorization (useful patterns for generalization) from unintended memorization (storing/reproducing specific training data). Provides new framework for understanding privacy and copyright risks.

#### 1.7 A Random Matrix Perspective on the Consistency of Diffusion Models
- **Authors**: Binxu Wang, Jacob A Zavatone-Veth, Cengiz Pehlevan
- **Key Innovation**: Explains why diffusion models generate nearly identical images from the same random seed across different datasets/architectures, attributing it to shared Gaussian statistics.

#### 1.8 To Grok Grokking: Provable Grokking in Ridge Regression
- **Authors**: Mingyue Xu, Gal Vardi, Itay Safran
- **Key Innovation**: First rigorous proof of the "grokking" phenomenon in ridge regression, linking delayed generalization to learning-rate and weight-decay settings.

### Test of Time Award

#### 1.9 Asynchronous Methods for Deep Reinforcement Learning (A3C)
- **Authors**: Volodymyr Mnih, Adria Puigdomenech Badia, Mehdi Mirza, Alex Graves, Timothy Lillicrap, Tim Harley, David Silver, Koray Kavukcuoglu
- **Affiliation**: Google DeepMind
- **Venue**: ICML 2016 (Test of Time at ICML 2026)
- **Key Impact**: The A3C algorithm replaced experience replay with lock-free asynchronous updates, enabling CPU-only training and surpassing DQN on 57 Atari games. Its gradient noise as regularizer insight underpins modern RL for LLM post-training.

### Notable Oral Papers

#### 1.10 Learning Unmasking Policies for Diffusion Language Models
- **Venue**: ICML 2026 Oral
- **Key Innovation**: Proposes training sampling procedures for dLLMs using RL, formalizing masked diffusion sampling as an MDP. A lightweight single-layer transformer policy maps token confidences to unmasking decisions, outperforming heuristic strategies.

#### 1.11 VALUEFLOW: Toward Pluralistic and Steerable Value-based Alignment in LLMs
- **Affiliation**: Seoul National University (AIDAS Lab)
- **Venue**: ICML 2026 Oral
- **Key Innovation**: Unified framework for value extraction, evaluation, and steering with calibrated intensity control, enabling fine-grained and controllable pluralistic value alignment.

---

## 2. ICLR 2026 (Singapore, Apr 23–27, 2026)

**Stats**: ~19,000 submissions → ~5,000+ accepted (~28.18%)

### Outstanding Papers

#### 2.1 Transformers are Inherently Succinct
- **Authors**: Pascal Bergsträßer, Ryan Cotterell, Anthony Widjaja Lin
- **Affiliation**: Max Planck Institute for Software Systems (MPI-SWS), RPTU Kaiserslautern
- **Venue**: ICLR 2026 Outstanding Paper
- **Abstract & Key Innovation**: Proves that Transformers can represent formal languages with dramatically shorter descriptions than finite automata and LTL formulas. The decision problem for Transformer properties is EXPSPACE-complete, establishing theoretical intractability. Demonstrates the fundamental expressive efficiency of Transformers over RNNs.
- **Link**: https://openreview.net/forum?id=Yxz92UuPLQ

#### 2.2 LLMs Get Lost In Multi-Turn Conversation
- **Venue**: ICLR 2026 Outstanding Paper
- **Abstract & Key Innovation**: Systematic evaluation of 200,000+ simulated conversations reveals that every mainstream LLM shows a **39% average performance drop** when moving from single-turn QA to multi-turn dialogue. Models make early assumptions, emit premature answers, and fail to self-correct. First scalable diagnostic framework for multi-turn conversational ability.
- **Models tested**: GPT-4o, o3, GPT-4.1, Claude 3.7 Sonnet, Gemini 2.5 Pro, Llama 3.3-70B, DeepSeek-R1, and others.

### Honorable Mention

#### 2.3 The Polar Express: Optimal Matrix Sign Methods and the Muon Algorithm
- **Authors**: Noah Amsel, David Persson, Christopher Musco, Robert M. Gower
- **Key Innovation**: Principled approach to improving the Muon optimizer via polar decomposition of gradient matrices. Provides theoretical foundation for one of the most popular alternatives to Adam.

### Test of Time Award
- **Winner**: Alec Radford et al. — referenced as the foundational work behind modern LLMs.

### Notable Papers

#### 2.4 GRAPE: Group Representational Position Encoding
- **Venue**: ICLR 2026 Poster
- **Key Innovation**: Unified framework for positional encoding based on group actions. Subsumes RoPE and ALiBi as special cases via multiplicative rotations (SO(d)) and additive logit biases (GL). Provides principled design space for long-context models.

#### 2.5 GRACE: Generative Representation Learning via Contrastive Policy Optimization
- **Venue**: ICLR 2026 Poster
- **Key Innovation**: Novel contrastive policy optimization for generative representation learning.

---

## 3. CVPR 2026 (Denver, Jun 3–7, 2026)

**Stats**: 16,092 submissions (+24% over 2025) → 4,089 accepted (~25%)

### Best Paper Awards

#### 3.1 Efficiently Reconstructing Dynamic Scenes One D4RT at a Time (Best Paper)
- **Authors**: Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, Liliane Momeni, Junyu Xie, Shuyang Sun, Rahul Sukthankar, Joëlle K. Barral, Raia Hadsell, Zoubin Ghahramani, Andrew Zisserman, Junlin Zhang, Mehdi S. M. Sajjadi
- **Affiliation**: Google DeepMind, University College London, University of Oxford
- **Venue**: CVPR 2026 Best Paper
- **Abstract & Key Innovation**: D4RT is a unified transformer-based architecture that reconstructs the geometry and motion of dynamic 4D scenes from a single video. Estimates depth, spatio-temporal correspondence, and full camera parameters, enabling efficient probing of any 3D point at any time in just seconds.
- **Comparison**: Unlike previous approaches, D4RT handles both dynamic scenes with moving objects and static scenes from a single video.

#### 3.2 Native and Compact Structured Latents for 3D Generation (Best Student Paper)
- **Affiliation**: Tsinghua University, Microsoft Research
- **Key Innovation**: Pushes up quality and realism of AI-generated 3D assets through native structured latent representations.

#### 3.3 NitroGen: An Open Foundation Model for Generalist Gaming Agents (Best Paper Honorable Mention)
- **Affiliation**: NVIDIA, Stanford, Caltech, UT Austin
- **Key Innovation**: Vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games, exhibiting strong competence across diverse gaming domains.

#### 3.4 SAM 3D: 3Dfy Anything in Images (Best Paper Honorable Mention)
- **Key Innovation**: Extends Segment Anything Model to 3D scene understanding.

#### 3.5 TUNA: Taming Unified Visual Representations for Native Unified Multimodal Models
- **Venue**: CVPR 2026
- **Key Innovation**: Unified visual representation framework for native multimodal models, integrating understanding and generation in a single architecture.

---

## 4. AAAI 2026 (Singapore, Jan 20–27, 2026)

**Stats**: ~29,000 submissions → 4,000+ accepted

### Notable Papers

#### 4.1 In-Token Rationality Optimization (InTRO): Accurate and Concise LLM Reasoning via Self-Feedback
- **Authors**: Zhu, Liu, Fu, Wang, Zhang
- **Venue**: AAAI 2026 Vol. 40 No. 41
- **Key Innovation**: Enables token-level exploration and self-feedback for accurate/concise reasoning. Uses correction factors (token-wise importance weights) to encourage accurate rationales. Outperforms baselines by up to 20% on 6 math-reasoning benchmarks, with notably more concise CoT.

#### 4.2 PRIME: Planning and Retrieval-Integrated Memory for Enhanced Reasoning
- **Authors**: Tran, Yao, Tran, Yang, Ouyang, Han, Yu et al.
- **Venue**: AAAI 2026 Vol. 40 No. 39
- **Key Innovation**: Multi-agent framework inspired by dual-process theory (Thinking, Fast and Slow). Quick Thinking Agent generates rapid answers; if uncertain, triggers System 2 pipeline. LLaMA 3 models with PRIME compete with GPT-4/GPT-4o on multi-hop reasoning.

#### 4.3 CDCR-SFT: Mitigating Hallucinations via Causal Reasoning
- **Authors**: Li, Shen, Nian, Gao, Wang, Yu, Zhao et al.
- **Venue**: AAAI 2026 Vol. 40 No. 38
- **Key Innovation**: Trains LLMs to construct variable-level causal DAGs and reason over them. Achieves 95.33% accuracy on CLADDER (surpassing human 94.8% for the first time) and 10% improvement on HaluEval hallucination benchmark.

#### 4.4 BayesAgent: Bayesian Agentic Reasoning Under Uncertainty
- **Authors**: Huang, Shen, Hao, Wang, Meng, Liu, Bhatt et al.
- **Venue**: AAAI 2026 Vol. 40 No. 26
- **Key Innovation**: Bridges LLM agents with probabilistic graphical models via Verbalized PGMs (vPGM). Enables principled uncertainty modeling and Bayesian inference in natural language.

#### 4.5 AURA: Affordance-Understanding and Risk-aware Alignment for LLMs
- **Venue**: AAAI 2026 Special Track on AI Alignment
- **Key Innovation**: Multi-layered framework using Process Reward Models (PRMs) for step-level safety evaluation across logical coherence and safety-awareness.

---

## 5. NeurIPS 2025 (San Diego, Dec 2–7, 2025)

**Stats**: 21,575+ submissions → 5,200+ accepted (24.5%)

### Best Paper Awards (7 papers)

Key themes from NeurIPS 2025 best papers:
- **Diffusion model theory** advances
- **Self-supervised reinforcement learning**
- **Attention mechanisms for LLMs**
- **Gated attention** (best paper)
- Embodied AI, mechanistic interpretability, reasoning agents, and causality

### Key Conference Trends
- Embodied AI in physical/biological realms (bioacoustics, robotics, spatial reasoning)
- Reliability and interpretability (robustness, regulatable designs, mechanistic interpretability)
- Advanced reasoning and agents (multi-turn interactions, unified language-agent-world models)
- Core theoretical advancements (optimization dynamics, structured graphs, causality)

---

## 6. KDD 2026 (Jeju Island, Korea, Aug 9–13, 2026)

### Notable Papers

#### 6.1 CTR-Sink: Attention Sink for Language Models in CTR Prediction
- **Authors**: Zixuan Li, Binzong Geng, Jing Xiong, Yong He et al.
- **Affiliation**: Ant Group (Kuaishou collaboration)
- **Venue**: KDD 2026
- **Abstract & Key Innovation**: Addresses semantic fragmentation in LM-based CTR prediction where discrete user behaviors with empty separators mismatch LM pre-training. Introduces behavior-level attention sinks ([SINK] tokens) between behaviors with recommendation-specific signals (temporal distance, semantic similarity). Achieves AUC improvements of 0.2–0.5% across industrial and public datasets on both RoBERTa and Qwen architectures.
- **Link**: https://github.com/UGUESS-lzx/CTR-SINK

#### 6.2 One Sequential Recommendation Model Pretrained from Synthetic Priors Predicts Multiple Datasets (SRPFN)
- **Authors**: Woosung Kang, Jiwon Jeong, Jonghyeok Shin, Jeongwhan Choi, Noseong Park
- **Venue**: KDD 2026
- **Key Innovation**: Prior-data Fitted Network that performs sequential recommendation without parameter updates on target domain. Pretrained on synthetic prior datasets, outperforms training-free baselines and approaches training-based methods.

#### 6.3 CausalMoE: Billion-Scale Multimodal Foundation Model for Granger Causal Discovery
- **Venue**: KDD 2026
- **Key Innovation**: Pattern-Routed Heterogeneous Experts for multimodal Granger causal discovery at billion scale.

#### 6.4 FlowTime: Continuous Generative Watch Time Prediction via Flow-based Personalized Priors
- **Affiliation**: Kuaishou
- **Venue**: KDD 2026
- **Key Innovation**: Flow matching-based personalized watch time prediction for short-video recommendation, enabling continuous generative prediction of viewing duration.

---

## 7. ACL 2026 (San Diego, Jul 2–7, 2026)

**Stats**: 2,400+ accepted papers

### Notable Papers

#### 7.1 KARL: Reinforcement Learning for LLM Agents on Multi-Turn Knowledge-Intensive Agentic Tasks
- **Authors**: Xueqiao Sun, Xiao Liu, Bowen Lv, Hanchen Zhang et al.
- **Affiliation**: Tsinghua University (THUDM)
- **Venue**: ACL 2026 Long Paper
- **Key Innovation**: Enables LLM agents to dynamically explore structured knowledge sources through multi-turn interactions with curiosity-driven reward shaping. Qwen2.5-14B agent significantly outperforms GPT-4o, Claude-4, and o4-mini on knowledge graph and database tasks.
- **Code**: https://github.com/THUDM/KARL

#### 7.2 SOAR: Supervision from Observation for Agentic Reinforcement Learning
- **Authors**: Meng Li, Lei Li, Xiting Wang et al.
- **Venue**: ACL 2026 Long Paper
- **Key Innovation**: Assigns positive advantages to observation tokens proportional to negative entropy of preceding actions. Improves general reasoning by 7.0% and deep research tasks by 16.9%.

#### 7.3 Miner: Mining Intrinsic Mastery for Data-Efficient RL in Large Reasoning Models
- **Authors**: Shuyang Jiang, Yuhao Wang, Ya Zhang, Yanfeng Wang, Yu Wang
- **Venue**: ACL 2026 Long Paper
- **Key Innovation**: Repurposes policy's intrinsic uncertainty as self-supervised reward signal for token-level focal credit assignment. Achieves up to 4.58 absolute gains in Pass@1 over GRPO on Qwen3-4B/8B.
- **Code**: https://github.com/pixas/Miner

#### 7.4 STEM: Structure-Tracing Evidence Mining for KG-Driven RAG
- **Venue**: ACL 2026
- **Key Innovation**: Reframes multi-hop reasoning as schema-guided graph search with Semantic-to-Structural Projection and Triple-Dependent GNN. Achieves SOTA on multiple multi-hop KGQA benchmarks.

#### 7.5 Robertha: Eigenspectrum Regularized Attention for Robust NLU
- **Venue**: ACL 2026
- **Key Innovation**: Attention mechanism based on Modern Hopfield Networks with Eigenspectrum Regularization for robust NLU under embedding corruption. Outperforms existing robustness methods across 13 GLUE/SuperGLUE tasks.

#### 7.6 Agentic Neural Network (ANN): Self-Evolving Multi-Agent Systems via Textual Backpropagation
- **Venue**: ACL 2026 Findings
- **Key Innovation**: Conceptualizes multi-agent collaboration as a layered neural network, with agents as nodes. Forward phase dynamically constructs cooperative teams; backward phase refines via textual gradients. Surpasses leading multi-agent baselines on 7 benchmarks.

#### 7.7 Alibaba's AI Agent Benchmark — Best Resource Paper at ACL 2026
- **Affiliation**: Alibaba
- **Key Innovation**: Awarded Best Resource Paper for comprehensive AI agent benchmarking framework.

---

## 8. SIGIR 2026 (Melbourne, Jul 20–24, 2026)

### Notable Papers

#### 8.1 LTRR: Learning To Rank Retrievers for LLMs
- **Venue**: SIGIR 2026
- **Key Innovation**: Query routing framework that learns to rank retrievers based on downstream utility to LLMs. RAG with trained routers (AC metric + pairwise XGBoost) outperforms standard single-retriever RAG.

#### 8.2 CoveR: Coverage-Aware Retrieval with Augmented Sub-Question Answerability
- **Venue**: SIGIR 2026
- **Key Innovation**: Retriever designed for long-form RAG that learns from coverage-based signals derived from sub-questions. Introduces SCOPE training dataset with augmented coverage signals.

#### 8.3 SmartSearch: Process Reward-Guided Query Refinement for Search Agents
- **Venue**: SIGIR 2026
- **Key Innovation**: Three-stage curriculum learning framework optimizing intermediate search query quality through process rewards and query refinement. Surpasses baselines by ~5% F1 on web exploration tasks.

#### 8.4 SA²CRQ: Adaptive Semantic Quantization for Industrial Generative Retrieval
- **Affiliation**: JD.com
- **Venue**: SIGIR 2026
- **Key Innovation**: Resolves head-item discriminability vs. tail-item generalization trade-off in industrial generative retrieval. Doubled tail-item retrieval coverage in JD.com search engine. Deployed in production.

#### 8.5 Agentic Search in the Wild: 14M+ Real Search Requests Analysis
- **Affiliation**: Carnegie Mellon, CMU, Meta
- **Venue**: SIGIR 2026
- **Key Innovation**: Large-scale log analysis of agentic search sessions from DeepResearchGym. 90%+ multi-turn sessions have ≤10 steps; 54% of new query terms traceable to retrieved evidence. Provides signals for repetition-aware stopping and intent-adaptive retrieval.

#### 8.6 AuthGR: Authority-aware Generative Retrieval
- **Venue**: ACL 2026 Industry Track
- **Key Innovation**: First framework incorporating document authority into generative IR. 3B model matches 14B baseline performance. Deployed on commercial web search platform.

---

## 9. WWW 2026 (Dubai, Apr 13–17, 2026)

### Notable Papers

#### 9.1 GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning for CTR Prediction
- **Venue**: WWW 2026
- **Key Innovation**: Generative user intent framework using semantic interest cohorts as explicit intent representations. Hierarchical quantization organizes items into semantically coherent cohorts; generative Transformer produces candidate interest cohorts for immediate intent capture.

#### 9.2 ThinkRec: Thinking-based Recommendation via LLM
- **Venue**: WWW 2026
- **Key Innovation**: Applies LLM reasoning ("thinking") to recommendation, bridging language understanding with preference modeling.

#### 9.3 OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer
- **Affiliation**: Industry (likely Alibaba/Tencent)
- **Venue**: WWW 2026
- **Key Innovation**: Single Transformer backbone jointly performing user-behavior sequence modeling and feature interaction. Unified tokenizer converts sequential and non-sequential features into one token sequence. Shows near log-linear scaling with model size. +1.13% CTR AUC improvement in production.

---

## 10. Recommendation Systems, Advertising & CTR — Recent arXiv

### 10.1 OneRanker: Unified Generation and Ranking in Industrial Advertising
- **Affiliation**: Tencent (Weixin Channels)
- **Key Innovation**: End-to-end generative advertising recommendation achieving architectural-level integration of generation and ranking. Value-aware multi-task decoupling, coarse-to-fine target awareness, and dual-side consistency guarantees. **Deployed on Tencent Weixin channels: GMV-Normal +1.34%**.

### 10.2 EST: Efficiently Scalable Transformer for CTR Prediction
- **Affiliation**: Alibaba (Taobao)
- **Key Innovation**: Fully unified modeling with Lightweight Cross Attention (LCA) and Content Sparse Attention (CSA). Exhibits stable power-law scaling. **Deployed on Taobao: RPM +3.27%, CTR +1.22%**.

### 10.3 Dual-Stream MLP (DS-MLP) for CTR Prediction
- **Authors**: Kesha Ou, Zhen Tian (ByteDance), Wayne Xin Zhao et al.
- **Affiliation**: Renmin University, ByteDance, Meituan
- **Key Innovation**: Knowledge distillation consolidates explicit feature interaction into main MLP while parallel MLP captures implicit interactions. Achieves SOTA across Criteo, Avazu, MovieLens with low latency.

### 10.4 RankUp: High-rank Representations for Large Scale Advertising
- **Affiliation**: Tencent (Weixin Video Accounts, Official Accounts, Moments)
- **Key Innovation**: Mitigates representation collapse through randomized permutation splitting, multi-embedding paradigm, and global token integration. **Deployed: GMV +3.41% (Video Accounts), +4.81% (Official Accounts), +2.12% (Moments)**.

### 10.5 LoopCTR: Loop Scaling for CTR Prediction
- **Key Innovation**: Increases training-time computation through recursive reuse of shared model layers, decoupling computation from parameter growth. Train-multi-loop, infer-zero-loop strategy.

### 10.6 DAIAN: Deep Adaptive Intent-Aware Network for Trigger-Induced Recommendation
- **Affiliation**: Alibaba (Xianyu)
- **Key Innovation**: Dynamically adapts to users' intent preferences in trigger-induced recommendation. Overcomes intent myopia issue. **Deployed on Xianyu: CTR +1.59%, diversity +1.73%, bills +2.37%**.

### 10.7 UniSID: End-to-End Semantic ID Generation for Generative Ad Recommendation
- **Key Innovation**: Jointly optimizes embeddings and Semantic IDs end-to-end from raw ad data. Up to 4.62% Hit Rate improvement over SOTA SID generation methods.

---

## 11. LLM Reasoning & Agent Systems — Recent arXiv

### 11.1 MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning
- **Venue**: arXiv Jul 2026
- **Key Innovation**: Dynamic step-wise memory with correctness-optimized memory composition for test-time self-improving reasoning. Coarse-to-fine retrieval mechanism.

### 11.2 BIGMAS: Brain-Inspired Graph Multi-Agent Systems
- **Venue**: arXiv 2026
- **Key Innovation**: Specialized LLM agents organized as nodes in dynamically constructed directed graphs with centralized shared workspace. Inspired by global workspace theory of human cognition. Outperforms ReAct and ToT on Game24, Six Fives, Tower of London.

### 11.3 DOLORES: Deep Reasoning in General Purpose Agents via Structured Meta-Cognition
- **Venue**: arXiv 2026
- **Key Innovation**: Constructs task-specific scaffolds through structured meta-reasoning using formal language. An 8B model surpasses all 32B baselines. 24.8% improvement over strongest scaffold baseline.

### 11.4 SMTL: Search More, Think Less — Long-Horizon Agentic Search
- **Affiliation**: OPPO AI Agent Team
- **Key Innovation**: Replaces sequential reasoning with parallel evidence acquisition. SMTL-30B achieves BrowseComp 48.6%, GAIA 75.7%, XBench 82.0%. Reduces reasoning steps by 70.7% vs MiroThinker while improving accuracy.

### 11.5 LLMZero: Discovering Adaptive Training Strategies via LLM Agents
- **Affiliation**: Amazon
- **Key Innovation**: LLM agents search over training trajectories via tree search for RL post-training. Discovers that capacity parameters accumulate monotonically while regularization parameters oscillate. 9–140% relative improvement over base model.

### 11.6 Compositional Generalization in LLM Reasoning (SFT + RL Theory)
- **Venue**: arXiv 2026
- **Key Innovation**: Formalizes reasoning traces via hierarchical latent selection model. Proves SFT supplies raw module materials while RL decomposes traces into reusable atomic modules. Proposes effective SFT/RL curriculum design protocol.

---

## 12. Code Execution Prediction & Coding Agents — Recent arXiv

### 12.1 Latent Programming Horizons in Coding Agents
- **Venue**: arXiv Jul 2026
- **Key Innovation**: Linear probes on coding agent hidden states decode program properties (correctness, regressions) with AUC up to 0.83. Surprising finding: probes predict future edit outcomes up to 25 steps in advance — the agent's "latent programming horizon." Probes transfer across benchmarks.

### 12.2 Self-Execution Simulation Improves Coding Models
- **Venue**: arXiv 2026
- **Key Innovation**: Combines SFT on natural language execution traces with RLVR for self-execution prediction. Enables self-verification (best@k) and iterative self-fixing without external execution.

### 12.3 Long-Horizon-Terminal-Bench
- **Venue**: arXiv Jul 2026
- **Key Innovation**: 46 long-horizon terminal tasks with dense reward grading. GPT-5.5 achieves only 15.2% pass rate; average across 15 frontier models is 4.3%. Average task requires 9.9M tokens, 231 episodes, 85.3 minutes.

### 12.4 DEXBENCH: Dual-Path Reasoning about Program Execution
- **Venue**: ACL 2026
- **Key Innovation**: Evaluates forward (predict behavior) and backward (mutate input) reasoning. 445 paired instances from CruxEval, HumanEval, PythonSaga. Small models (<10B) consistently fail; scaling to 20B+ yields substantial improvements.

### 12.5 SWE-EVO: Benchmarking Coding Agents in Long-Horizon Evolutionary Settings
- **Venue**: arXiv 2026
- **Key Innovation**: Best model reaches only 25% on SWE-EVO; GPT-5.2 drops from 72.80% on SWE-Bench Verified to dramatically lower on evolutionary tasks.

### 12.6 Agentick: Unified Benchmark for General Sequential Decision-Making Agents
- **Venue**: arXiv 2026
- **Key Innovation**: 37 procedurally generated tasks across 6 capability categories. GPT-5 mini leads overall (0.309 oracle-normalized), but PPO dominates planning/multi-agent tasks. Reasoning harness multiplies LLM performance by 3–10x.

---

## 13. Generative Models & Sequential Modeling — Recent arXiv

### 13.1 DiffoR: Unified Continuous Generative Framework for Universal Ordinal Regression
- **Affiliation**: Kuaishou
- **Venue**: KDD 2026
- **Key Innovation**: Unified generative framework for ordinal regression tasks using diffusion models.

### 13.2 GoR: Unified and Extensible Generative Framework for Ordinal Regression
- **Affiliation**: Kuaishou
- **Venue**: ICLR 2026
- **Key Innovation**: Generative regression-based approach for ordinal regression, extending to watch time prediction for short-video recommendation.

### 13.3 KMLP: Scalable Hybrid Architecture for Web-Scale Tabular Data Modeling
- **Affiliation**: Ant Group
- **Venue**: KDD 2026
- **Key Innovation**: Hybrid MLP architecture for tabular data at web scale, combining KAN (Kolmogorov-Arnold Networks) with traditional MLP for scalable feature interaction.

---

## 14. Games & Game AI — Recent Papers

### 14.1 NitroGen: Open Foundation Model for Generalist Gaming Agents
- **Affiliation**: NVIDIA, Stanford, Caltech, UT Austin
- **Venue**: CVPR 2026 Best Paper Honorable Mention
- **Key Innovation**: Vision-action foundation model trained on 40K hours of gameplay across 1,000+ games.

### 14.2 BIGMAS on Game24, Six Fives, Tower of London
- **Key Innovation**: Multi-agent graph systems tested on game benchmarks, showing complementary gains to model-level reasoning.

---

## 15. Industry Deployments & Production Systems

| System | Company | Metric | Improvement |
|--------|---------|--------|-------------|
| OneRanker | Tencent (Weixin) | GMV-Normal | +1.34% |
| EST | Alibaba (Taobao) | RPM / CTR | +3.27% / +1.22% |
| RankUp | Tencent (Weixin) | GMV | +3.41% to +4.81% |
| DAIAN | Alibaba (Xianyu) | CTR | +1.59% |
| SA²CRQ | JD.com | User Conv Rate | +0.13% |
| AuthGR | Commercial Search | User Engagement | Significant |

---

## Key Themes Across Conferences

1. **Diffusion Models Enter Mainstream**: ICML 2026 double Outstanding Paper win signals diffusion models as a major architectural contender for language generation. The "flexibility trap" finding challenges arbitrary-order assumptions.

2. **RL Post-Training Dominance**: GRPO, RLVR, and RL-based self-improvement are now standard. LLMZero reveals structural asymmetry in optimal multi-stage RL training. Miner shows intrinsic uncertainty as self-supervised reward.

3. **Multi-Agent Systems Maturation**: From PRIME (dual-process) to BIGMAS (graph-based) to ANN (textual backpropagation), multi-agent architectures are becoming principled rather than ad-hoc.

4. **Generative Advertising Recommendation**: Tencent's OneRanker and Alibaba's EST demonstrate that generative paradigms are reaching production scale in advertising, with measurable business metrics.

5. **Long-Horizon Agent Bottleneck**: Long-Horizon-Terminal-Bench reveals frontier models still struggle severely on sustained tasks (15.2% best, 4.3% average). SMTL's parallel evidence acquisition offers one path forward.

6. **Coding Agent Interpretability**: Latent programming horizons show coding agents maintain internal representations of future program states — a finding that could enable monitoring and steering from within latent space.

7. **Scaling Laws for CTR**: EST demonstrates that LLM-inspired scaling laws transfer to CTR prediction under efficiency constraints, with predictable power-law improvements.

8. **Safety & Alignment Ethics**: ICML position paper warns alignment tools becoming censorship infrastructure; ICML honorable mentions map honesty emergence in RLVR training.
