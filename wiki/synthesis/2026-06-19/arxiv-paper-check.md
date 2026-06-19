---
title: "arXiv Paper Check — AI & CTR (June 19, 2026)"
type: synthesis
created: 2026-06-19
updated: 2026-06-19
sources: [arxiv.org]
tags: [arxiv, ai, ctr, recommendation, generative-rec, llm-agents, retrieval]
---

# arXiv Paper Check — AI & CTR (June 19, 2026)

> Survey of Fri, 19 Jun 2026 submissions: cs.AI (73 new, 312 total) + cs.IR (11 new, 22 total). Highlights below.

---

## 🏆 Top Picks

### 1. G2Rec: Structuring and Tokenizing Distributed User Interest Context for Generative Recommendation
- **Authors:** Ruizhong Qiu, Yinglong Xia, Dongqi Fu, Hanqing Zeng et al.
- **arXiv:** 2606.20554 (cs.IR)
- **Key contribution:** Scalable framework unifying holistic graph-based user co-engagement modeling with semantic tokenization for industrial-scale generative recommendation. Enables recommendation models to capture holistic and semantically grounded user interest prototypes without requiring ground-truth user interests. Deployed online across product surfaces.
- **Tags:** generative recommendation, graph-based, tokenization, industrial

### 2. Token Factory: Efficiently Integrating Diverse Signals into Large Recommendation Models
- **Authors:** Xilun Chen, Shao-Chuan Wang, Baykal Cakici, Lukasz Heldt, Lichan Hong et al. (Google)
- **arXiv:** 2606.19635 (cs.IR)
- **Key contribution:** Transforms traditional signals into "soft tokens" processed directly by Large Recommendation Models (LRMs). Prevents prompt length explosion while enhancing model performance in a production-scale environment.
- **Tags:** large recommendation models, soft tokens, signal integration, production

### 3. ITNet: A Learnable Integral Transform That Subsumes Convolution, Attention, and Recurrence
- **Authors:** Ashim Dhor, Rasel Mondal, Pin Yu Chen
- **arXiv:** 2606.19538 (cs.AI)
- **Key contribution:** Unified architecture built around a learnable kernel (MLP) that models pairwise interactions. Shows convolution, self-attention (including multi-head), and autoregressive recurrence (LSTM, GRU, S4, Mamba) arise as special cases. Matches/Exceeds specialized baselines on ImageNet-1K, GLUE, ModelNet40, VQA v2, NLVR2.
- **Tags:** unified architecture, integral transform, attention, convolution, recurrence

### 4. ELVA: Exploring Ranking-Driven Universal Multimodal Retrieval
- **Authors:** Yuhan Liu, Pei Fu, Hang Li et al.
- **arXiv:** 2606.20280 (cs.IR, ECCV 2026)
- **Key contribution:** Extends RLVR (Reinforcement Learning with Verifiable Rewards) to retrieval tasks. Jointly optimizes ranking of negative samples while enlarging similarity gap between positive and negative. Introduces MRBench for multi-grain query scenarios. 13.1% improvement on MRBench.
- **Tags:** multimodal retrieval, rlvr, ranking, ecCV-2026

### 5. Denoising Implicit Feedback for Cold-start Recommendation (DIF)
- **Authors:** Gaode Chen, Shicheng Wang, Shikun Li et al. (Kuaishou)
- **arXiv:** 2606.19658 (cs.AI, KDD 2026 ADS Track)
- **Key contribution:** Model-agnostic denoising method for implicit feedback in cold-start scenarios. Uses content-similar warm items to infer pseudo-labels; models uncertainty via relative entropy and cold-start status. Deployed on billion-user scale Kuaishou with significant commercial metric improvements.
- **Tags:** cold-start, denoising, implicit feedback, KDD-2026, kuaishou

### 6. Beyond Entropy: Learning from Token-Level Distributional Deviations for LLM Reasoning
- **Authors:** Xuanzhi Feng, Zhengyang Li, Zeyu Liu et al.
- **arXiv:** 2606.19771 (cs.AI)
- **Key contribution:** Token-level distributional analysis for LLM reasoning improvement.
- **Tags:** llm-reasoning, token-level, distributional

### 7. Which Pairs to Compare for LLM Post-Training?
- **Authors:** Jiangze Han, Vineet Goyal, Will Ma
- **arXiv:** 2606.19607 (cs.AI)
- **Key contribution:** Formal analysis of comparison curation for DPO post-training. Provides matching upper/lower bounds on post-training optimality gap, linking label allocation to parameter estimation error and policy suboptimality.
- **Tags:** dpo, post-training, preference-optimization, sample-efficiency

### 8. VCG: A Multimodal Retrieval Framework for E-Commerce Video Feeds under Extreme Cold-Start
- **Authors:** Katya Mirylenka, Egor Malykh et al.
- **arXiv:** 2606.19627 (cs.IR)
- **Key contribution:** Scalable multimodal retrieval engine using domain-adapted CLIP for zero-shot video retrieval. Shows generative LLMs suffer from embedding space collapse in retrieval tasks. 50% uplift in deep video completion online.
- **Tags:** video-retrieval, cold-start, CLIP, e-commerce

### 9. Stellar: Scalable Multimodal Document Retrieval for Natural Language Queries
- **Authors:** Yuxiang Guo, Zhonghao Hu et al.
- **arXiv:** 2606.19960 (cs.IR)
- **Key contribution:** Disk-backed late interaction retrieval reducing memory overhead and query latency by 1-2 orders of magnitude. Uses lexical representation filtering + efficient disk-backed late interaction.
- **Tags:** multimodal-retrieval, RAG, disk-backed, scaling

### 10. PACMS: Submodular Context Selection as a Pluggable Engine for LLM Agents
- **Authors:** Manu Ghulyani, Arunabh Singh et al.
- **arXiv:** 2606.20047 (cs.IR)
- **Key contribution:** Replaces recency truncation with submodular context selection for LLM agent prompts. Selects from memory entries, conversation turns, and tool outputs as a single candidate pool by relevance at prompt assembly time.
- **Tags:** llm-agents, context-selection, submodular, memory

### 11. Hidden Anchors in Multi-Agent LLM Deliberation
- **Authors:** Apurba Pokharel, Ram Dantu
- **arXiv:** 2606.19494 (cs.AI)
- **Key contribution:** Models multi-agent LLM deliberation as closed-loop dynamical system with hidden internal belief "anchors." Shows anchors explain behavior classical consensus forbids: confidence can climb past initial beliefs. Recovered anchors predict held-out runs.
- **Tags:** multi-agent, deliberation, opinion-dynamics, theory

### 12. Diffusion Language Models: An Experimental Analysis
- **Authors:** Thomas Bertolani, Davide Bucciarelli et al.
- **arXiv:** 2606.19475 (cs.AI)
- **Key contribution:** Systematic evaluation of 8 state-of-the-art DLMs across 8 benchmarks (reasoning, coding, translation, knowledge). Analyzes impact of denoising steps, context length, block size, parallel unmasking. Shows generation-time design choices drive trade-offs between performance and efficiency.
- **Tags:** diffusion-lm, comprehensive-benchmark, generation-tradeoffs

### 13. SAFE-Cascade: Cost-Adaptive Vision-Language Routing for Chart QA
- **Authors:** Ayush Dwivedi et al.
- **arXiv:** 2606.19646 (cs.IR, CIKM 2026 demo)
- **Key contribution:** Selective modality routing: OCR + text-only LM for simple queries, escalate to VLM only when needed. Matches full-VLM performance while reducing VLM calls by 26.9% and estimated cost by 9.3%.
- **Tags:** VLM-routing, cost-efficiency, chart-QA, CIKM-2026

### 14. MonaVec: Training-Free Embedded Vector Search Kernel for Edge AI
- **Authors:** Oğuzhan Yenen
- **arXiv:** 2606.19458 (cs.IR)
- **Key contribution:** SQLite-like embedded vector search: one file, one function call. Training-free 4-bit quantization via Randomized Hadamard Transform. 0.960 Recall@10 in 27 MB. Deterministic (byte-identical) across architectures.
- **Tags:** vector-search, edge-ai, embedding-quantization, embedded

### 15. ScholarQuest: A Taxonomy-Guided Benchmark for Agentic Academic Paper Search
- **Authors:** Tingyue Pan, Mingyue Cheng et al.
- **arXiv:** 2606.20235 (cs.IR)
- **Key contribution:** Large-scale benchmark (1000+ CS topics, 4 research intents) for evaluating LLM search agents. Best-performing agent only achieves 0.314 Recall@100 — substantial room for improvement.
- **Tags:** benchmark, academic-search, llm-agents, retrieval

---

## 📊 Summary Statistics

| Category | Count | Top Themes |
|----------|-------|------------|
| **cs.AI — New** | 73 entries | Reasoning, multi-agent, alignment, post-training, diffusion LMs |
| **cs.AI — Total** | 312 entries | LLM agents, knowledge representation, RL, interpretability |
| **cs.IR — New** | 11 entries | Generative recommendation, multimodal retrieval, vector search, RAG |
| **cs.IR — Total** | 22 entries | Cold-start, semantic caching, metric learning, agent memory |
| **CTR/RecSys focused** | ~5 papers | G2Rec (generative rec), Token Factory (LRM soft tokens), DIF (cold-start denoising), VCG (video rec) |

---

## 🔑 Key Themes

1. **Generative Recommendation Productionization**: G2Rec and Token Factory (both with production deployment) show generative recommendation moving from research to industrial-scale deployment.
2. **Cold-Start & Denoising**: DIF (KDD 2026, Kuaishou) and VCG (video cold-start) tackle the persistent cold-start problem from different angles — denoising implicit feedback vs. zero-shot multimodal retrieval.
3. **Unified Architectures**: ITNet subsumes convolution/attention/recurrence into a single integral transform — a theoretical unification reminiscent of the Mamba/SSM wave.
4. **RLVR for Retrieval**: ELVA extends verifiable-reward RL to retrieval tasks, potentially opening a new training paradigm for ranking.
5. **Cost-Aware AI**: SAFE-Cascade (VLM routing), SLARouter (LLM routing), and MonaVec (embedded vector search) all optimize for cost/efficiency — a growing theme as inference scales.
6. **Agent Memory & Context**: PACMS introduces submodular context selection for agent prompts, targeting the key bottleneck of growing context windows.
7. **Multi-Agent Dynamics**: Hidden Anchors provides a formal dynamical-systems model for multi-agent LLM deliberation, explaining previously unmodeled behaviors.
