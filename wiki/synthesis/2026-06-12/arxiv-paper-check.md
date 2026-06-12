---
title: "arXiv Paper Check — AI & CTR (June 12, 2026)"
type: synthesis
created: 2026-06-12
updated: 2026-06-12
sources: [arxiv.org/list/cs.AI/new, arxiv.org/list/cs.IR/new, arxiv.org/list/cs.LG/new]
tags: [arxiv, daily, ai, ctr, recommendation, agents, llm, formal-proving, unlearning, retrieval]
---

# arXiv Paper Check — AI & CTR (June 12, 2026)

> Surveyed: Fri 12 Jun 2026 — cs.AI (86 new), cs.IR (7 new, 4 cross, 12 replacements), cs.LG (121 new)

---

## 🧠 AI / LLM / Agents

### 1. Pythagoras-Prover — Advancing Efficient Formal Proving via Augmented Lean Formalisation
- **Authors**: Joshua Ong Jun Leang, Zheng Zhao, Mihaela Cătălina Stoian, Qiyuan Xu, Haonan Li, Wenda Li, Shay B. Cohen, Eleonora Giunchiglia
- **Key contribution**: Open-source Lean prover family (4B & 32B autoregressive, 4B diffusion-based). Pythagoras-Prover-4B surpasses DeepSeek-Prover-V2-671B at pass@32 on MiniF2F-Test (86.1% vs 82.4%) with ~167× fewer parameters. 32B sets open-source SOTA at 93.0% on MiniF2F-Test, solves 93/672 PutnamBench problems. Introduces Augmented Lean Formalisation (ALF) for expanding scarce verified proof data.

### 2. Arbor — Tree Search as a Cognition Layer for Autonomous Agents
- **Authors**: Neha Prakriya, Chaojun Hou, Zheng Gong, Huasha Zhao, Xi Zhao, Mou Li, Zhenyu Gu, Emad Barsoum
- **Key contribution**: Multi-agent framework that uses structured tree search as shared working memory across agents. Validated on full-stack LLM inference optimization — achieves up to 193% throughput-latency Pareto improvement over vendor-optimized baselines. Single agent without harness plateaus at +33% and crashes within hours.

### 3. From AGI to ASI (DeepMind)
- **Authors**: Tim Genewein, Matija Franklin, Alexander Lerchner, Laurent Orseau, Samuel Albanie, Adam Bales, Cole Wyeth, Stephanie Chan, Iason Gabriel, Joel Z. Leibo, Allan Dafoe, Marcus Hutter, Thore Graepel, Shane Legg
- **Key contribution**: DeepMind report analyzing the transition from human-level AGI to artificial superintelligence. Discusses four pathways (scaling, paradigm shifts, recursive improvement, multi-agent collectives) and frictions/bottlenecks. Argues progress may be a series of transformative changes rather than a single step change.

### 4. Prefill Awareness in Large Language Models
- **Authors**: Andy Wang, Parv Mahajan, David Demitri Africa, Alexandra Souly, Jordan Taylor, Robert Kirk
- **Key contribution**: Investigates whether frontier LLMs can detect tampered assistant-side context (prefilling). Claude Opus 4.5 detects opposing prefills in 9-35% of cases with 0% false positive rate. Significant confound for safety eval methods that rely on prefill-based techniques. Submitted to NeurIPS 2026.

### 5. SciAgentArena — Benchmarking AI Agents for Scientific Challenges
- **Authors**: Tianyu Liu et al. (multi-institutional, including Marinka Zitnik, James Zou, Hua Xu, Hongyu Zhao)
- **Key contribution**: ~200-task benchmark for AI agents in real scientific research scenarios with stepwise verification. Current agents work well for well-specified data-analysis workflows but struggle with novel insight generation, self-directed exploration, and open-ended research.

### 6. MLUBench — A Benchmark for Lifelong Unlearning Evaluation in MLLMs (ICML 2026)
- **Authors**: He Li, Haoang Chi, Qizhou Wang, Yunxin Mao, Zhiheng Zhang, Jie Tan, Tongliang Liu, Wenjing Yang, Bo Han
- **Key contribution**: 127 entities across 9 classes for multimodal LLM lifelong unlearning. Reveals existing methods suffer severe cumulative degradation. Proposes LUMoE to mitigate degradation while preserving multimodal alignment.

### 7. ToolSense — A Diagnostic Framework for Auditing Parametric Tool Knowledge in LLMs
- **Authors**: Ashutosh Hathidara, Sai Shruthi Sistla, Sebastian Schreiber, Sahil Bansal
- **Key contribution**: Open-source framework that generates three benchmarks (RRB, MCQ, QA) from any tool catalog. Reveals knowledge-retrieval dissociation in parametric tool models — RRB performance collapses 50-64pp below fully-specified benchmarks, some models score near-random on factual probes.

### 8. Topical Phase Transitions in AI Research
- **Authors**: Rasul Khanbayov, Hasan Kurban
- **Key contribution**: Analyzes 80,814 papers from ACL/CVPR/ICLR/ICML/NeurIPS (2017-2025). Shows AI topics advance through abrupt phase transitions. Early-warning signature flags reasoning/test-time compute, agentic AI, multimodal LLMs, RAG, and world models as 2026-2028 monitors.

### 9. Evoflux — Inference-Time Evolution of Executable Tool Workflows for Compact Agents
- **Authors**: Kushal Raj Bhandari, Ling Yue, Ching-Yun Ko, Dhaval Patel, Shaowu Pan, Pin-Yu Chen, Jianxi Gao
- **Key contribution**: Evolutionary search method for repairing tool workflows in compact LMs. Raises execution feasibility from ~3% to 17-24% across small planners on MCP-Bench (250 tools). SFT/DPO on same data match or collapse below zero-shot.

### 10. Boltzmann Attention — Learnable Ising Couplings for Cooperative Attention
- **Authors**: Gilhan Kim, Daniel K. Park
- **Key contribution**: Energy-based attention generalization where patterns are governed by an interacting Ising model. Learns pairwise couplings between positions beyond softmax. Advantage grows with sequence length. Diabatic quantum annealing provides practical training method.

### 11. The Hidden Power of Scaling Factor in LoRA Optimization
- **Authors**: Zicheng Zhang, Haoran Li, Jiaxing Wang et al.
- **Key contribution**: Shows LoRA's α is the dominant driver of effective optimization, not learning rate. Proposes Signal-Drift framework. Optimal α follows square-root law with rank. Proposes LoRA-α for principled scaling.

### 12. Zero-source LLM Hallucination Detection with Human-like Criteria Probing (ICML 2026)
- **Authors**: Jiahao Yang, Shuhai Zhang, Hailong Kang, Feng Liu, Qi Chen, Mingkui Tan
- **Key contribution**: HCPD — emulates human evaluator multi-faceted reasoning for zero-source hallucination detection (no model internals or external references). Uses reward-based alignment with weak supervision. Outperforms SOTA baselines.

### 13. (Human) Attention Is (Still) All You Need — Human oversight makes AI-assisted social science reliable
- **Authors**: Chen Zhu, Xiaolu Wang, Weilong Zhang
- **Key contribution**: Human-in-the-Loop Economic Research (HLER) architecture with pre-commitment, decision sequencing, accountability. Unconstrained multi-agent baseline failed in 72% of runs; HLER reduced to 16% using same underlying model.

### 14. Teach-and-Repeat — Extracting Operational Knowledge from Mobile Screen Demonstrations (Honor)
- **Authors**: Yudong Zhang, Lei Hu et al. (Honor Device Co.)
- **Key contribution**: Teach VLM translates mobile screen trajectories into step-wise operational knowledge. Systematic data flywheel for scalable training. Consistent Task Success Rate improvements for downstream GUI agents.

### 15. GeoNatureAgent Benchmark — LLM Agents for Environmental Geospatial Analysis
- **Authors**: Gabriel Diaz-Ireland et al.
- **Key contribution**: First benchmark for environmental analysis agents with 93 tasks + real API. Claude Sonnet 4 leads (60.8%), DeepSeek V3.2 offers 93% capability at 11× lower cost. Comparison tasks remain universally unsolved (0%).

---

## 📊 CTR / Recommendation / Retrieval

### 1. OneRetrieval — Unifying Multi-Branch E-commerce Retrieval with Editable Generative Model (Kuaishou)
- **Authors**: Xuxin Zhang, Ben Chen, Yue Lv et al. (Kuaishou)
- **Key contribution**: One-model generative retrieval with Keyword-Aligned Encoding (KAE). Preserves real-time editability of inverted index — reserved slots in codebooks bind new terms post-deployment without retraining. Replacing inverted-index branch improves CTR and order volume. Serves hundreds of millions PVs daily.

### 2. Helmsman — Building Cost-Effective and High-Performance ANNS at Scale (OSDI'26, RedNote/Xiaohongshu)
- **Authors**: Yuchen Huang, Baiteng Ma et al. (RedNote/Xiaohongshu)
- **Key contribution**: Clustering-based ANNS on all-flash servers combining userspace storage stack, leveling-learned pruning, GPU-accelerated construction. Saves 90%+ hardware costs, enables billion-scale index rebuilds within hours. 40 machines now host workloads requiring ~35,000 cores + 0.35 PB DRAM.

### 3. CQC-RAG — Robust RAG via Cross-Query Consistency
- **Authors**: Yanjia Sun, Sifan Liu, Jie Shao
- **Key contribution**: Cross-Query Consistency Hypothesis — correct answers maintain high confidence across semantically equivalent but syntactically diverse queries. Rewrites queries, reranks shared document pool, selects by confidence stability. Outperforms strongest multi-query baseline by +4.76pp EM on TriviaQA, +9.12pp on MuSiQue.

### 4. CFALR — Collaborative Filtering-Augmented LLM for Fashion Outfit Recommendation
- **Authors**: Yujuan Ding, Junrong Liao, Yunshan Ma et al.
- **Key contribution**: First LLM-based architecture for personalized outfit recommendation. CF-enhanced generative mechanism navigates item combination space. Trainable projection layers integrate relational and content features. Superior on Polyvore and IQON benchmarks.

### 5. CoDeR — Local Constraint-Compatible Retrieval Beyond Semantic Similarity
- **Authors**: Xingkun Yin, Xuebin Tang, Hongyang Du
- **Key contribution**: Separates topical relevance from constraint compatibility. Compatibility scorer trained with lexical-polarity supervision. No external LLM calls at inference. Reduces V@2 by 20.59-5.77 points across antonymy/negation/exclusion diagnostics.

### 6. HiGR — Industrial-Scale Hierarchical Generative Slate Recommendation (Tencent, replacement)
- **Authors**: Yunsheng Pang et al. (Tencent)
- **Key contribution**: Prefix-Contrastive Residual Quantized VAE (PCRQ-VAE) for structured SIDs. Hierarchical Slate Decoder shifts from token-level to coarse-grained preference embeddings. 5× inference speedup, +1.22% watch time, +1.73% video plays online. Deployed on multiple Tencent platforms.

### 7. LENS — Staged Design for Interaction Granularity in Sequential CTR Prediction (replacement)
- **Authors**: Yuan Wang, Yue Liu et al.
- **Key contribution**: Target-Conditioned Query Gate + Target-Conditioned Position Bias for restoring target-specific control in latent-query backbones. Positive gain across 12 backbone-dataset cells. Identifies density-dependent conditioning rule.

### 8. AdaGRPO — Adaptive Loss Balancing for Noise-Robust GRPO in Generative Recommendation
- **Authors**: Kewei Xu, Junbo Qi et al.
- **Key contribution**: Gates GRPO by per-sample diagnostics (policy difficulty + reward discriminability). On large-scale e-commerce, improves HR@10 from 11.01% to 12.18% while constraining hallucination <0.22%. Statistically significant CTR and dwell time gains in production A/B tests.

---

## 🔬 Notable cs.LG Mentions

### 1. DynamicPTQ — Mitigating Activation Quantization Collapse via Residual-Stream Dynamics
- **Key contribution**: Identifies phase-wise massive activation pattern across network depth. DynamicPTQ assigns 8-bit to sensitive layers while keeping others at W4A4KV4. Improves perplexity and QA on LLaMA-2/3.

### 2. μVLA — On Recurrent Memory for Partially Observable Manipulation in VLA Models
- **Key contribution**: Controlled study of minimal recurrence in VLA backbones. Average success improves from 0.42 to 0.84 on training tasks, 0.07→0.23 on held-out tasks.

### 3. Rubric-Guided Self-Distillation — Post-Training Without Rubric Verifiers
- **Key contribution**: Verifier-free RGSD — base policy conditioned on rubric serves as teacher. Dense per-token signals replace sparse trajectory-level rewards. Comparable to judge-based GRPO without verifier overhead.

---

## 📈 Trends

1. **Formal proving efficiency**: Pythagoras-Prover shows 4B can match 671B — massive inference-time savings
2. **Agent safety maturity**: Prefill Awareness, Containment Gap, and lie detection papers all point to growing concern about agent eval validity
3. **Generative retrieval goes production**: OneRetrieval (Kuaishou) proves editable generative retrieval at scale
4. **CTR fine-grained interaction**: LENS + AdaGRPO both explore condition-aware granularity in ranking/recommendation
5. **Attention innovation**: Boltzmann Attention brings Ising model / quantum annealing to attention mechanisms
6. **MLLM unlearning**: MLUBench reveals lifelong unlearning as a new challenge distinct from static unlearning
7. **AI topic phase transitions**: Empirical evidence that AI research reorganizes through abrupt transitions, not gradual growth
