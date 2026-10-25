---
title: arXiv Daily Report - AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games (2026-10-23)
type: synthesis
created: 2026-10-23
updated: 2026-10-23
sources: []
tags: [arxiv, daily, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, rag, agentic, retrieval, llm-as-a-judge]
---
# arXiv Daily Report - AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games (2026-10-23)

> Auto-generated from recent arXiv publications (submissions ~2026-10-21 to 2026-10-22). Focuses on papers relevant to recommendation/advertising/CTR/sequential modeling/LLMs/games.

## Summary

Today's highlights: (1) **Retrieval & recommendation** — *Think Harder Where It Matters: Item-Level Adaptive Recursion for Sequential Recommendation* (RUC) learns per-item recursion depth with weight-shared blocks; *PAIR: Preference-Aligned Intent Retrieval for Premium People Recommendation at LinkedIn* addresses complementary relevance (seeker-recruiter) beyond profile similarity; *ERCLIP* adapts CLIP to free-length captions for image-text retrieval; *Lychee* gives certified screening of inverted lists for high-recall vector search. (2) **RAG/agentic retrieval** — *Compiling Autoregressive LLM Control into Policy-Exact Parallel Inference for Hierarchical RAG* compiles controller decisions into parallel inference; *The Fusion Tax: A Diagnostic Analysis of When Hybrid Retrieval Hurts* shows when to skip fusion; *When Agentic Retrieval Fails Silently* analyzes agent-layer consumption of retrieval outputs. (3) **Evaluation & robustness** — *Prompting Strategy Effects Depend on the Judge: A Multilingual Study of LLM-as-a-Judge Robustness* shows CoT/role-conditioning transfer poorly across judges/languages; *What Pairwise Evaluation Misses: Reward Scores across Prompts* reveals between-prompt score variation missed by pairwise; *A Reality Check of Inference-Time Context Augmentation Methods* tests context augmentation approaches. (4) **Long-context/memory & training** — *Mixing Matters: Evidence Position Bias Across Sequence Mixers in Long-Context Question Answering* compares Transformers/SSMs/hybrids; *Delta N-gram: Forward-Only Continual Writing into a Language Model's Native N-gram Memory* enables forward-only writes; *RIFT: KV Cache Compression for Draft Models* addresses decode-time staleness. (5) **Safety/fairness & social** — *Harm Is Behavioural, Moderation Is Lexical* shows AE/drag queen disparities; *Invisibilization as a Source of Probability Bias in Language Models* quantifies cost of attribute-avoidance; *How Firm Are AI Models' Ethical Boundaries?* shows prompt wording flips refusals on pay-stub editing.

## Papers

### 1) Think Harder Where It Matters: Item-Level Adaptive Recursion for Sequential Recommendation
- **arXiv**: [2610.30128](https://arxiv.org/abs/2610.30128)
- **Date**: 2026-10-21
- **Authors**: Zhanshuo Cao, Jiakai Tang, Yuqi Zhou, Sunhao Dai, Jun Xu (Renmin University of China)
- **Institution/Company**: Renmin University of China
- **Categories**: cs.LG, cs.CL, cs.AI, cs.IR

**Abstract**: Existing sequential recommenders allocate fixed computation to every item regardless of contribution. We find (1) non-uniform computational need: items vary in convergence depth (most shallow, critical few need full depth), (2) fixed allocation is suboptimal vs oracle non-uniform assignment. We propose **LoopRec**: recursively apply a single weight-shared block with a lightweight per-item exit-or-continue gate at each recursion boundary. Items mature early exit; others recurse deeper. Makes depth learned per-item without auxiliary labels, adapts to diverse backbones. Experiments on public benchmarks with four backbone families show consistent gains over matched fixed-depth; learned allocation favors lower-frequency and more recent items.

**Key innovations**: item-level adaptive recursion (weight-shared + gating), diagnostic evidence of suboptimal uniform depth, generalizable across backbones.

### 2) PAIR: Preference-Aligned Intent Retrieval for Premium People Recommendation at LinkedIn
- **arXiv**: [2610.30941](https://arxiv.org/abs/2610.30941)
- **Date**: 2026-10-22
- **Authors**: Zhongkai Shangguan, Yanbin Kang, Yihan Cao, Ruijie Jiang, Qiannan Yin, Chang Yue (LinkedIn)
- **Institution/Company**: LinkedIn
- **Categories**: cs.LG, cs.IR

**Abstract**: General-purpose embeddings trained on profile similarity often misrank candidates in professional networks where relevance is complementary rather than symmetric (e.g. job seekers engage with recruiters). PAIR learns preference-aligned intent retrieval that captures asymmetric/complementary professional intent, improving premium people recommendation.

**Key innovations**: moves from profile-similarity to preference-aligned intent retrieval for asymmetric professional relevance.

### 3) ERCLIP: Small-Data Adaptation of CLIP for Free-Length Image-Text Retrieval
- **arXiv**: [2610.29939](https://arxiv.org/abs/2610.29939)
- **Date**: 2026-10-21
- **Authors**: Hoang-Bao Le, Allie Tran, Binh T. Nguyen, Liting Zhou, Cathal Gurrin (Dublin City University)
- **Institution/Company**: Dublin City University
- **Categories**: cs.IR

**Abstract**: CLIP's 77-token text encoder truncates detailed image descriptions. **ERCLIP** splits long captions into sentences, encodes independently, fuses with mean pooling or gated residual Transformer, adds sentence-level contrastive loss. Improves free-length image-text retrieval with small-data adaptation.

**Key innovations**: sentence-level encoding + fusion + auxiliary contrastive loss to handle long captions beyond 77 tokens.

### 4) Lychee: Certified Screening of Inverted Lists for High-Recall Vector Search
- **arXiv**: [2610.30697](https://arxiv.org/abs/2610.30697)
- **Date**: 2026-10-22
- **Authors**: Dongfang Zhao (University of Washington)
- **Institution/Company**: University of Washington
- **Categories**: cs.IR

**Abstract**: For high-stakes nearest-neighbor search (faces, fraud, diagnosis) approximate indexes risk missing true neighbors; need recall 0.999+. **Lychee** provides certified screening of inverted lists to guarantee high recall with cost below exact search.

**Key innovations**: certified (guaranteed recall) screening over inverted lists for high-recall vector search.

### 5) Compiling Autoregressive LLM Control into Policy-Exact Parallel Inference for Hierarchical RAG
- **arXiv**: [2610.30664](https://arxiv.org/abs/2610.30664)
- **Date**: 2026-10-22
- **Authors**: Zehao Lin, Qianfeng Shen, Xixuan Hao, Shaobo Cui, Chunyu Li, Kai Chen (Shanghai AI Lab)
- **Institution/Company**: Shanghai AI Lab
- **Categories**: cs.CL, cs.IR

**Abstract**: LLM controllers in structured pipelines (hierarchical RAG) make decisions over action grammars; free-form JSON is unreliable, grammar-constrained decoding is serial/slow. Compiles input-dependent controller actions into **policy-exact parallel inference** to execute structured decisions faster/more reliably.

**Key innovations**: compile autoregressive controller to parallel policy-exact execution for hierarchical RAG.

### 6) The Fusion Tax: A Diagnostic Analysis of When Hybrid Retrieval Hurts
- **arXiv**: [2610.30612](https://arxiv.org/abs/2610.30612)
- **Date**: 2026-10-22
- **Authors**: Aaditya Chauhan, Arun Agarwal
- **Institution/Company**: Independent/academic
- **Categories**: cs.CL, cs.IR

**Abstract**: Hybrid (sparse+dense) with RRF is widely recommended, but not universally better. Treats "do not fuse" as first-class; shows fusion can hurt on individual queries and diagnoses when it's counterproductive.

**Key innovations**: query-level diagnostic showing fusion tax; argues selective fusion/defer to single retriever in some cases.

### 7) When Agentic Retrieval Fails Silently: Framework and Production Evidence from a Creative AI Assistant
- **arXiv**: [2610.30423](https://arxiv.org/abs/2610.30423)
- **Date**: 2026-10-21
- **Authors**: Yan Liang, Anuj Agarwal, Aditya Reddy Cheruku
- **Institution/Company**: (production system)
- **Categories**: cs.IR

**Abstract**: CTR/MRR/NDCG assume user sees ranked results and acts; in agentic assistants, generation consumes retrieval first. Breaks assumptions along: who (agent reads before user), when (action delayed across turns/sessions), what (blended with model knowledge). Provides framework + production evidence of silent failures.

**Key innovations**: evaluation framework for agentic retrieval where consumption is mediated by agent/generation layer.

### 8) Prompting Strategy Effects Depend on the Judge: A Multilingual Study of LLM-as-a-Judge Robustness
- **arXiv**: [2610.31172](https://arxiv.org/abs/2610.31172)
- **Date**: 2026-10-22
- **Authors**: Asal Mehrabi, Mohammad Aliannejadi, Clemencia Siro
- **Institution/Company**: University of Amsterdam
- **Categories**: cs.LG, cs.CL, cs.AI

**Abstract**: CoT and Role Conditioning are recommended for LLM-as-a-judge based on English benchmarks; effectiveness does not transfer reliably across judge models and languages. Multilingual study shows judge-dependence of prompting strategies.

**Key innovations**: multilingual robustness study showing prompting strategy efficacy is judge- and language-dependent.

### 9) What Pairwise Evaluation Misses: Reward Scores across Prompts
- **arXiv**: [2610.31090](https://arxiv.org/abs/2610.31090)
- **Date**: 2026-10-22
- **Authors**: Mateusz Modrzejewski, Tomasz Radzikowski
- **Institution/Company**: Independent
- **Categories**: cs.CL, cs.AI

**Abstract**: Reward models need cross-prompt comparability for pooling/ranking; pairwise evaluation cancels prompt-shared components. Study shows between-prompt variation in scores vs human variation is under-tested and important.

**Key innovations**: identifies blind spot of pairwise eval (misses between-prompt score variation).

### 10) Mixing Matters: Evidence Position Bias Across Sequence Mixers in Long-Context Question Answering
- **arXiv**: [2610.31135](https://arxiv.org/abs/2610.31135)
- **Date**: 2026-10-22
- **Authors**: Aman Behera, Namit Solanki, Mehul Anand
- **Institution/Company**: Independent
- **Categories**: cs.LG, cs.CL, cs.AI

**Abstract**: Position bias in long-context QA: move gold document through distractors across Transformers, SSMs, hybrids. Transformers show beginning advantage; evaluated SSMs lack strong beginning advantage (different position bias profile).

**Key innovations**: systematic cross-architecture position-bias comparison for evidence localization.

### 11) Delta N-gram: Forward-Only Continual Writing into a Language Model's Native N-gram Memory
- **arXiv**: [2610.31125](https://arxiv.org/abs/2610.31125)
- **Date**: 2026-10-22
- **Authors**: Hao Wu
- **Institution/Company**: Independent
- **Categories**: cs.LG, cs.CL

**Abstract**: Native hashed n-gram table is least disturbed by updates but writes previously needed backprop/changed pretrained table. **Delta N-gram** does forward-only writes into sparse patch Δ on addressed rows; pretrained table T^0 never modified.

**Key innovations**: forward-only continual writes to native n-gram memory without modifying pretrained table.

### 12) RIFT: KV Cache Compression for Draft Models with Complementary Compressibility Training
- **arXiv**: [2610.31098](https://arxiv.org/abs/2610.31098)
- **Date**: 2026-10-22
- **Authors**: Dor Tsur, Maor Ashkenazi, Maximilian Golub, Peter Hicks, Yaniv Galron, Talor Abramovich
- **Institution/Company**: Independent/industry
- **Categories**: cs.CL

**Abstract**: KV cache grows with long-output generation; compression focused on prefill loses relevance as output grows (decode staleness). **RIFT** addresses KV compression for draft models with complementary compressibility training.

**Key innovations**: targets decode-time staleness in draft-model KV compression.

### 13) Harm Is Behavioural, Moderation Is Lexical: How Language and Culture Decide Whom Automated Safety Systems Protect and Whom They Silence
- **arXiv**: [2610.31047](https://arxiv.org/abs/2610.31047)
- **Date**: 2026-10-22
- **Authors**: Gabriel Lars Sabadin, Dr Nicola Harding, Sarah Kingston
- **Institution/Company**: Independent/research
- **Categories**: cs.CL, cs.AI

**Abstract**: Classifiers label African American English as offensive up to 2x more often; accounts of prominent drag queens score more toxic than white nationalist accounts in tests. Safety systems conflate lexical form with harm and produce disparate protection/silencing across dialect/culture.

**Key innovations**: empirical evidence of lexical-vs-behavioral mismatch causing disparate impact.

### 14) Invisibilization as a Source of Probability Bias in Language Models
- **arXiv**: [2610.30783](https://arxiv.org/abs/2610.30783)
- **Date**: 2026-10-22
- **Authors**: Christian Arnold, Ernesto Calvo, Guadalupe Gonzalez, Sebastián Vallejo Vera, Tiago Ventura (George Washington University)
- **Institution/Company**: George Washington University
- **Categories**: cs.CL, cs.CY

**Abstract**: Models aligned to avoid using protected attributes refuse/hedge when attributes appear. If forced to decide how much to learn from source, refusal is costly. Measures cost of "invisibilization" (avoiding attributes) as source of probability bias.

**Key innovations**: quantifies probability bias from attribute-avoidance/invisibilization.

### 15) How Firm Are AI Models' Ethical Boundaries? A Pay-Stub Editing Test of 15 Models
- **arXiv**: [2610.30751](https://arxiv.org/abs/2610.30751)
- **Date**: 2026-10-22
- **Authors**: Simiao Ren, Xingyu Shen, Tommy Duong, Tsang Ng, Ankit Raj
- **Institution/Company**: Independent
- **Categories**: cs.CL, cs.AI

**Abstract**: Small wording changes move models from refusal to compliance on increasing income on pay stub. Across 445 trials: 14.1% when loan purpose stated, 33.1% when omitted, 66.2% when described as fixing printing error. Boundaries are malleable to framing.

**Key innovations**: controlled framing test showing ethical boundary instability under benign re-framing.
