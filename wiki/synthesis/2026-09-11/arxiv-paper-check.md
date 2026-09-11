---
title: "arXiv Paper Check — AI & CTR (September 11, 2026)"
type: synthesis
created: 2026-09-11
updated: 2026-09-11
sources: [arxiv.org]
tags: [arxiv, daily-check, ai, ctr, recommendation, agents, reasoning, llm, efficiency, evaluation, ciqm-2026, emnlp-2026, icdm-2026, daily-digest]
---

# arXiv Paper Check — AI & CTR (September 11, 2026)

> **Mailing**: Fri, 11 Sep 2026. Submission window ~Wed Sep 8 – Thu Sep 10.
> **Scan scope**: cs.AI (171 new), cs.IR (15 new), cs.LG (171 new).
> **Dedup**: Cross-checked against same-day [[arxiv-daily]] (2609-09-11, 27 papers across 7 sections) — zero overlap.

## Summary

This window is CTR-sparse (0 direct CTR papers) but rich in rec-adjacent and LLM-efficiency work with direct applicability to industrial ranking and serving. 15 papers across 5 themes.

---

## ① Recommendation & Ranking (3)

### UniRec: Cross-stage Multi-Task Fusion with Preference Alignment for Cascaded Recommender Systems
- **arXiv**: 2609.11052
- **Authors**: Lingyuan Kong, Jiaqi Cui, Fanjiao Zeng, Congqi Wang, Yu Li, Yuan Cheng, Jingxin Liu, Xiaoshuang Chen, Kaiqiao Zhan
- **Affiliation**: Kuaishou
- **Key contribution**: UniRec jointly optimizes fusion modules across pre-ranking and ranking stages via a dual-axis preference alignment objective: (1) vertical cross-stage consistency transfers downstream pairwise preferences upstream, (2) horizontal compact aggregation reorganizes dozens of pairwise objectives over heterogeneous prior signals. Adds attribute group-relative regularization to prevent optimization exploitation of attribute distribution imbalances. **Online A/B: +0.616% app usage duration. Fully deployed on Kuaishou.**
- **Relevance**: Cross-stage consistency is a known open problem in industrial rec. This is one of the first production-validated solutions that directly addresses upstream-downstream gradient coupling in cascaded systems.

### FedHUR: Learning Hierarchical Utility-Guided Client Relations for Personalized Federated Recommendation
- **arXiv**: 2609.11632
- **Authors**: Mingzhe Han, Jiahao Liu, Dongsheng Li, Jiankui Zhou, Hansu Gu, Peng Zhang, Ning Gu, Tun Lu
- **Affiliation**: Fudan University
- **Key contribution**: Federated recommendation framework that learns hierarchical utility-guided client relations using item-item filters. Clients compute hierarchical utility signals based on global clustered information, and the server retrieves useful clients for personalized aggregation. Outperforms existing federated rec baselines on 5 datasets.
- **Relevance**: Federated learning for rec is increasingly important for privacy-preserving personalization. This work moves beyond simple similarity-based aggregation to utility-aware hierarchical client selection.

### On the Regularization Landscape for the Linear Recommendation Models
- **arXiv**: 2609.11876
- **Authors**: Dong Li, Zhenming Liu, Ruoming Jin, Hao Zhou, Zhi Liu, Jing Gao, Bin Ren
- **Key contribution**: Unifies the regularization perspective across linear performance-leading rec models: all effectively add nuclear-norm or Frobenius-norm regularizers. Proposes two new low-rank closed-form solutions that get the best of both worlds — expressiveness of Frobenius-norm + low-rank efficiency of nuclear-norm, without ADMM tuning.
- **Relevance**: Theoretical contribution clarifying why disparate rec algorithms achieve similar performance, with practical closed-form solutions.

---

## ② LLM Efficiency & Serving (3)

### LILA: Calibration-Free Structured Pruning of Large Language Models via Latent Spectral Geometry
- **arXiv**: 2609.11163
- **Authors**: Sankar Behera, Dhruv Singh, Anshika Agnihotri, Raj Kumar Choudhary, Satyadev Ahlawat, Yamuna Prasad
- **Key contribution**: Scores neuron importance via KS distance between empirical singular value distributions of full vs ablated FFN weight matrices — closed-form spectral rule, no training, no calibration data, no auxiliary network. Surpasses PruneNet by +1.57pp zero-shot accuracy on LLaMA-2-7B at 25% sparsity. After 1-epoch LoRA recovery, matches SliceGPT within 0.48pp margin using zero calibration data. NTK analysis confirms 22x reduction in functional distortion vs random pruning.
- **Relevance**: Calibration-free pruning is highly practical for production LLM serving where calibration data is expensive or unavailable.

### REVA: Reusable Evidence View Aggregation for Context-Efficient RAG Serving
- **arXiv**: 2609.11209
- **Authors**: Tuan Nguyen, Qiran Hu, Banruo Liu, Khoa D. Doan, Kok-Seng Wong, Fan Lai
- **Affiliation**: ICDM 2026
- **Key contribution**: Mines historical query-document-model attention traces into a document-keyed score store. Maps token-level attention to readable word units, aggregates importance across repeated document accesses, renders budget-specific plain-text views. Improves generation quality 1.0-5.8 points over existing compressors while reducing compression overhead 5.3-15.6x, adding <40ms latency.
- **Relevance**: RAG serving is increasingly critical for rec-adjacent systems (e.g., e-commerce search). This data-mining approach to compression is more practical than online compressor models.

### Thinking with Looped Flows
- **arXiv**: 2609.11801
- **Authors**: Ayhan Suleymanzade, Chanhyuk Lee, Floor Eijkelboom, Nicholas M. Boffi, İsmail İlkan Ceylan, Jinwoo Kim
- **Key contribution**: Trains recurrence with local denoising objectives via progressively decreasing noise levels and shared noise, incentivizing recurrent states that transfer computation over time. Inference integrates velocity of probability flow parameterized by learned denoiser with recurrent states. **58.8% on ARC-AGI-1, 12.2% on ARC-AGI-2** — outperforms prior looped models across 6 reasoning benchmarks.
- **Relevance**: Looped models are a key frontier for inference-efficient reasoning. This approach sidesteps BPTT-through-long-sequences, making deeper reasoning practical.

---

## ③ Agent Skill Optimization (2)

### COBRA-Skills: Contextual Bandit-Guided Evolution for Agent Skill Optimization
- **arXiv**: 2609.11682
- **Authors**: Pingchen Lu, Xiangyi Wang, Xiang Li, Jie Mao, Zikun Qu, Junfeng Luo, Yao Shu, Bryan Kian Hsiang Low, Zhongxiang Dai
- **Key contribution**: Formulates skill optimization as budgeted sequential optimization over dynamically evolving candidate space. Couples contextual-bandit-guided prioritization with evidence-grounded skill evolution. Consistently strongest average performance across 6 agent benchmarks and 3 target models, while reducing optimization cost by 55-58% vs SkillOpt, using only 50 unique optimization examples per benchmark.
- **Relevance**: Agent skill systems are a hot topic (cf. SkillOpt, Trace2Tower in earlier digests). COBRA-Skills achieves strong results with dramatically lower evaluation cost.

### The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement
- **arXiv**: 2609.11873
- **Authors**: Yi Duan, Ying Liu, Zirui Tang, Haodong Chen, Jun Zhou, et al.
- **Key contribution**: Explores genuine recursive self-improvement — the "last AI built by humans" concept. Examines what capabilities and safeguards are needed before AI systems can meaningfully improve themselves.
- **Relevance**: Recursive self-improvement is a central AGI safety and capability question, directly relevant to Karpathy's "autoresearch" concept.

---

## ④ On-Policy Distillation (1)

### A Unified Per-Token Gating Family for On-Policy Distillation
- **arXiv**: 2609.11768
- **Authors**: Suwan Wu, Yumeng Lin, Pengcheng Yuan, Xiaolong Jiang
- **Affiliation**: EMNLP 2026 Findings
- **Key contribution**: Introduces a four-coefficient parameterization for per-token gating of FKL/RKL losses in on-policy distillation. Unifies EOPD and ToDi as 1D restrictions, adds multi-channel composition and explicit bias. Configurations in the full family beat single-channel baselines in 33 of 36 comparable cells on TweetEval with Qwen3-32B teacher → Qwen3-4B student.
- **Relevance**: On-policy distillation is increasingly important for LLM efficiency (smaller student models from larger teachers). This unified framework clarifies the design space.

---

## ⑤ Retrieval & RAG (4)

### VikingRAG: Accurate and Token-Efficient Retrieval-Augmented Generation over Structured Documents
- **arXiv**: 2609.11390
- **Authors**: Peiyuan Gao, Gaoyuan Zhang, Haojie Qin, Yahui Sun, Qianyi Zhang, Yunhao Zhang, Zeyu Wang, Wei Lu
- **Key contribution**: Token-efficient RAG approach for structured documents, improving accuracy while reducing token consumption.

### Your Retriever Already Knows: Distribution-Shape QPP for RAG Retrieval Sufficiency
- **arXiv**: 2609.11646
- **Authors**: Matyáš Veselý, Michal Průšek, Jiří Franc
- **Affiliation**: TSD 2026
- **Key contribution**: Uses the shape of the retrieval score distribution as a query-performance prediction signal for RAG retrieval sufficiency — no additional model needed.

### Generative Late-Interaction Embeddings For Visual Document Retrieval
- **arXiv**: 2609.11808
- **Authors**: Mohamed Eltahir, Talal Aloushan, Rose Khairoalsendi, Jana Shata, Mohammed Alhassan, Leen Alrehaili, Tanveer Hussain, Naeemullah Khan
- **Key contribution**: Late-interaction embeddings generated for visual document retrieval, bridging vision and retrieval.

### When Synthetic Data Hurts: On Catastrophic Forgetting in Skill Retrieval for LLM Agents
- **arXiv**: 2609.10750
- **Authors**: Syed Shariyar Murtaza, Yifan Nie, Utkarsh Soni, Eugene Wen, Arvid Frydenlund
- **Affiliation**: EMNLP 2026 Industry Track
- **Key contribution**: Demonstrates that synthetic data for skill retrieval can cause catastrophic forgetting in LLM agents — a cautionary finding for agent skill systems.

---

## Key Trends

1. **Cross-stage optimization in rec** (UniRec): Industrial systems are moving from stage-independent to jointly optimized cascaded pipelines, with production validation.
2. **Calibration-free efficiency** (LILA): Spectral methods can replace calibration-data-dependent pruning, simplifying deployment.
3. **Agent skill cost reduction** (COBRA-Skills): Contextual bandits dramatically reduce the evaluation budget for skill optimization.
4. **RAG compression from data mining** (REVA): Historical attention traces as a reusable resource, not per-query compression.
5. **Unified distillation frameworks** (FKL/RKL gating): The on-policy distillation design space is being systematized.
6. **Recursive self-improvement**: Continued theoretical exploration of what "the last human-built AI" looks like.

---

## CTR Note

Zero new direct CTR papers in this window. The closest CTR-adjacent work is UniRec (cross-stage cascaded ranking, Kuaishou deployment) and On the Regularization Landscape (theoretical unification of linear rec models). The CTR-specific papers from the Sep 7 mailing (CADET, FAT, DeRes, LoopCTR, LENS) remain the most recent batch — covered in [[arxiv-daily]] 2026-09-11.
