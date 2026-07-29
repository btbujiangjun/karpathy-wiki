---
title: "arXiv Daily — July 29, 2026"
type: synthesis
created: 2026-07-29
updated: 2026-07-29
sources: []
tags: [arxiv, daily, llm, recommendation, ctr, games, sequential-modeling, advertising]
---

# arXiv Daily — July 29, 2026

Curated recent papers across AI, LLMs, recommendation, advertising, CTR, sequential modeling, games, and related areas. Primarily covering submissions from late July 2026.

---

## LLMs & Foundation Models

### 1. Understanding Large Language Models
- **Authors:** Yannik Keller, Thomas Eisenmann
- **Institution:** — (independent)
- **Link:** [2607.01006](https://arxiv.org/abs/2607.01006)
- **Date:** Jul 1, 2026
- **Abstract:** Comprehensive overview of LLM mechanisms, emergent cognitive capabilities, and the ongoing debate regarding machine understanding vs. pattern memorization. Synthesizes research on architecture, emergent behaviors, and interpretability.
- **Key Innovations:** Philosophical argument against reductionist views of AI cognition; synthesis of emergent cognitive-like behaviors across scales.

### 2. Agora: Enhancing LLM Agent Reasoning Via Auction-Based Task Allocation
- **Authors:** Kaiji Zhou, Ales Leonardis, Yue Feng
- **Institution:** — (multi-affiliation)
- **Link:** [2607.09600](https://arxiv.org/abs/2607.09600)
- **Date:** Jul 10, 2026
- **Abstract:** Introduces an incentive-compatible auction mechanism for dynamically allocating reasoning tasks to expert models and tools. Treats reasoning steps as tradeable items; agents bid based on rectified competence.
- **Key Innovations:** Competence-calibrated auctions for multi-agent LLM orchestration; multi-stage pipeline (decomposition, calibration, auction); significant gains on MMLU-Pro and SPIQA.

### 3. Super Weights in LLMs and the Failure of Selective Training
- **Authors:** Ivan Ilin, Philip Zmushko, Peter Richtárik
- **Institution:** — (multi-affiliation)
- **Link:** [2607.09287](https://arxiv.org/abs/2607.09287)
- **Date:** Jul 10, 2026
- **Abstract:** Investigates "super weights" in LLMs and why simple pruning-inspired sparse fine-tuning fails. Proposes LIFT (Low-rank Informed Sparse Fine-Tuning) which updates only top 5% principal weights after rank reduction.
- **Key Innovations:** Identifies principal weights after low-rank approximation as critical for fine-tuning; LIFT outperforms full FT on reasoning while retaining 20% more source-domain knowledge.

### 4. Can Agents Generalize to the Open World? Unveiling the Fragility of Static Training in Tool Use
- **Authors:** Song-Lin Lv, Weiming Wu, Rui Zhu, Zi-Jian Cheng, Lan-Zhe Guo
- **Institution:** LAMDA Group, Nanjing University
- **Link:** [2607.01084](https://arxiv.org/abs/2607.01084)
- **Date:** Jul 1, 2026
- **Abstract:** Identifies generalization gap of LLM agents in open-world environments. Proposes perturbation-augmented fine-tuning to enhance robustness against environmental shifts.
- **Key Innovations:** OpenAgent benchmark; perturbation-augmented training for tool-use agents.

### 5. Unified Scaling Law for LLM Training
- **Authors:** Fabian Schaipp
- **Institution:** — (independent)
- **Link:** [2607.01487](https://arxiv.org/abs/2607.01487)
- **Date:** Jul 1, 2026
- **Abstract:** Proposes a three-term unified scaling law that can derive scaling laws for suboptimal batch sizes and matches previous empirical findings on critical batch size.
- **Key Innovations:** Unified three-term scaling law bridging data allocation and batch size scaling; compute-efficient prescriptive approach.

### 6. Towards Next-Generation LLM Training: From the Data-Centric Perspective
- **Authors:** Hao Liang, Zhengyang Zhao, Zhaoyang Han et al.
- **Institution:** Peking University, Institute for Advanced Algorithms Research, OriginHub Technology, MemTensor Technology, HKUST
- **Link:** [2603.14712](https://arxiv.org/abs/2603.14712)
- **Date:** Mar 16, 2026 (updated Jul 28, 2026)
- **Abstract:** Comprehensive survey on data-centric LLM training. Introduces agent-guided automatic data preparation system and vision for Unified Data–Model Interaction Training System.
- **Key Innovations:** Agent-guided data prep pipeline; vision for dynamic data-model interaction during training.

### 7. Benchmarking Fine-tuning and Retrieval Strategies for a Multimodal Language Model on the NRC Reactor Operator Licensing Examination
- **Authors:** — (multi-author)
- **Institution:** — (multi-affiliation)
- **Link:** [2607.22067](https://arxiv.org/abs/2607.22067)
- **Date:** Jul 27, 2026
- **Abstract:** Benchmarks Gemma 4 31B-IT on NRC Reactor Operator exam with 8 model-retrieval configs. SFT with fixed-size RAG passed 8 of 14 exams (79.7% accuracy).
- **Key Innovations:** Domain-specific RAG + SFT for specialized licensure exams; demonstrates necessity of fine-tuning for technical domains.

### 8. DBA-Bench: A Production-Fidelity Benchmark for LLM-Based Database Operations Agents
- **Authors:** — (multi-author)
- **Institution:** — (multi-affiliation)
- **Link:** [2607.22165](https://arxiv.org/abs/2607.22165)
- **Date:** Jul 27, 2026
- **Abstract:** Production-fidelity benchmark for LLM database agents using instrumented PostgreSQL. 106 scenarios across 7 task domains.
- **Key Innovations:** Reveals significant gaps between LLM performance and human DBAs; outcome-first evaluation methodology.

### 9. Copy Less, Ground More: Overcoming Repetitive Copying in Long-Context Reasoning via Evidence-Aware Reinforcement Learning (GEAR)
- **Authors:** — (multi-author)
- **Institution:** — (multi-affiliation)
- **Link:** [2607.19345](https://arxiv.org/abs/2607.19345)
- **Date:** Jul 21, 2026
- **Abstract:** Identifies "repetitive copying" as critical failure mode in long-context LLMs. GEAR uses reward shaping with grounding rewards for key evidence and penalties for irrelevant context.
- **Key Innovations:** Evidence-aware RL for long-context reasoning; automated pipeline for evidence-annotated training data.

---

## Recommendation Systems & CTR Prediction

### 10. LaRec: Unleashing LLM-based Latent Reasoning for Generative Recommendation
- **Authors:** Yu Xia, Zihan Lin, Wei Yang, Rui Zhong, Cheng Chen, Huan Ren, Yao Hu
- **Institution:** Xiaohongshu (小红书)
- **Link:** [2607.24617](https://arxiv.org/abs/2607.24617)
- **Date:** Jul 27, 2026
- **Abstract:** Generative recommendation framework that enhances LLM latent reasoning by providing fine-grained supervision and exploring diverse user interests.
- **Key Innovations:** Fine-grained supervision for latent reasoning in generative RecSys; exploration of diverse user interest spaces.

### 11. UniR²: Unifying Generative Recall and Multi-Objective Ranking in a Single Decoder-Only Sequence
- **Authors:** Ruochen Yang, Shuang Wen, Pengbo Xu et al.
- **Institution:** — (multi-affiliation)
- **Link:** [2607.24439](https://arxiv.org/abs/2607.24439)
- **Date:** Jul 27, 2026
- **Abstract:** Unifies generative recall and multi-objective ranking in a single decoder-only Transformer for recommendation systems.
- **Key Innovations:** Single-model architecture for both recall and ranking; multi-objective optimization in generative setting.

### 12. CogRec: Structure-Cognitive Fast-and-Slow Reasoning for Generative Recommendation
- **Authors:** Xiang Liu, Jingsong Su, Shuqi Zhao et al.
- **Institution:** — (multi-affiliation)
- **Link:** [2607.24402](https://arxiv.org/abs/2607.24402)
- **Date:** Jul 27, 2026
- **Abstract:** Structure-cognitive fast-and-slow reasoning framework for generative recommendation, grounding reasoning in Semantic ID topology.
- **Key Innovations:** Dual-system reasoning (fast/slow) for RecSys; Semantic ID topology grounding.

### 13. OxygenREC-v2: Internalizing Discrimination into Generative Recommendation
- **Authors:** Guo Tang, Hanye Wu, Changjiang Han et al.
- **Institution:** — (multi-affiliation)
- **Link:** [2607.24255](https://arxiv.org/abs/2607.24255)
- **Date:** Jul 27, 2026
- **Abstract:** Internalizes user behavior signals into generative recommendation backbone, improving e-commerce metrics by 1.6–6.8%.
- **Key Innovations:** Discriminative signal integration into generative backbone.

### 14. Diffusion Language Model for Recommendation (DLMRec)
- **Authors:** Chengyi Liu, Yongqi Zhou, Junwei Pan et al.
- **Institution:** — (multi-affiliation)
- **Link:** [2607.21519](https://arxiv.org/abs/2607.21519)
- **Date:** Jul 23, 2026
- **Abstract:** Introduces discrete diffusion language model for recommendation, addressing autoregressive limitations with collaborative tokenization and curriculum training.
- **Key Innovations:** Discrete diffusion for RecSys (vs. autoregressive); collaborative tokenization; curriculum training schedule.

### 15. Bridging the Structural Gap: Adapting Autoregressive Generation for Recommendation (BARGE)
- **Authors:** Junchao Zeng, Junzhang Zhu, Junyang Chen et al.
- **Institution:** — (multi-affiliation)
- **Link:** [2607.21028](https://arxiv.org/abs/2607.21028)
- **Date:** Jul 23, 2026
- **Abstract:** Improves generative recommendation by addressing structural gaps and semantic drift with Item Context-Aware Attention and Hierarchical Path Reranking.
- **Key Innovations:** Item Context-Aware Attention; Hierarchical Path Reranking for semantic drift mitigation.

### 16. PinEqualizer: Full Funnel Content Exploration and Debiasing System at Pinterest
- **Authors:** Olafur Gudmundsson, Bo Zhao, Huayi Liao et al.
- **Institution:** Pinterest
- **Link:** [2607.22518](https://arxiv.org/abs/2607.22518)
- **Date:** Jul 24, 2026
- **Abstract:** Production system at Pinterest addressing content cold-start by debiasing exploration across the full funnel, improving engagement.
- **Key Innovations:** Full-funnel debiasing for cold-start; deployed at Pinterest scale.

### 17. Dual-Stream MLP is All You Need for CTR Prediction
- **Authors:** Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution:** Renmin University of China
- **Link:** [2606.04944](https://arxiv.org/abs/2606.04944)
- **Date:** Jun 2026
- **Abstract:** Proposes lightweight dual-stream MLP using knowledge distillation from powerful teacher (e.g., GDCN). A simple three-layer MLP with parallel augmentation stream captures what the main branch misses.
- **Key Innovations:** Knowledge distillation for lightweight CTR; dual-stream MLP competitive with complex architectures.

### 18. Cheaper is Better: A Discount-Aware Network for Conversion Rate Prediction (DANet)
- **Authors:** Ruocong Tang, Yang Huang, Xing Fang, Chenyi Yan, Chuike Sun, Jing Wang
- **Institution:** — (multi-affiliation)
- **Link:** [2607.12578](https://arxiv.org/abs/2607.12578)
- **Date:** Jul 14, 2026 (SIGIR '26 Industry Track)
- **Abstract:** Models the relationship between item discount rates and CVR, addressing data sparsity, SSB, and delayed feedback.
- **Key Innovations:** First systematic modeling of discount rate impact on CVR; released at [github.com/tangrc/DANet](https://github.com/tangrc/DANet).

### 19. IDProxy: Cold-Start CTR Prediction for Ads and Recommendation at Xiaohongshu with Multimodal LLMs
- **Authors:** — (multi-author)
- **Institution:** Xiaohongshu (小红书)
- **Link:** [2603.01590](https://arxiv.org/abs/2603.01590)
- **Date:** Mar 2, 2026
- **Abstract:** Leverages MLLMs to generate proxy embeddings from rich content signals for cold-start items, aligned with existing ID embedding space and optimized end-to-end under CTR objectives.
- **Key Innovations:** MLLM-generated proxy embeddings for item cold-start; end-to-end alignment with ranking pipeline.

---

## Advertising & Auto-Bidding

### 20. Strategy-Aware Parameter-Efficient Adaptation for LLM-based Auto-Bidding (SAGE)
- **Authors:** Songyue Cai, Lianyu Wang, Shan Gu et al.
- **Institution:** — (multi-affiliation)
- **Link:** [2607.24232](https://arxiv.org/abs/2607.24232)
- **Date:** Jul 27, 2026
- **Abstract:** Parameter-efficient LLM-based auto-bidding framework that improves performance and reduces fine-tuning costs for constrained advertising.
- **Key Innovations:** Strategy-aware PEFT for advertising auto-bidding.

### 21. LO-FAR: A Cost-Aware Local Filter for Sparse Feature Ranking in Industrial Ad Recommendation
- **Authors:** Egemen Erbayat, Luis Duque, Sohini Roychowdhury et al.
- **Institution:** — (multi-affiliation)
- **Link:** [2607.20873](https://arxiv.org/abs/2607.20873)
- **Date:** Jul 23, 2026
- **Abstract:** CPU-only, model-agnostic workflow for cost-aware sparse feature ranking in industrial ad recommendation.
- **Key Innovations:** Cost-aware feature selection for CPU-only industrial ad serving.

---

## Sequential Modeling & Transformers

### 22. NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation
- **Authors:** — (multi-author)
- **Institution:** — (multi-affiliation)
- **Link:** [2601.02204](https://arxiv.org/abs/2601.02204)
- **Date:** Jan 5, 2026
- **Abstract:** Unified decoder-only autoregressive transformer trained on 6 trillion interleaved text-image discrete tokens for multimodal understanding and generation.
- **Key Innovations:** Single unified model for multimodal seq modeling; 6T token interleaved training.

### 23. Mamba-3: Improved Sequence Modeling Using State Space Principles
- **Authors:** — (multi-author)
- **Institution:** — (multi-affiliation)
- **Link:** [2603.15569](https://arxiv.org/abs/2603.15569)
- **Date:** Mar 16, 2026
- **Abstract:** Third generation of Mamba architecture with improved state space model principles for efficient sequence modeling.
- **Key Innovations:** Architecture refinements for SSM-based sequence modeling.

---

## Reinforcement Learning & Games

### 24. Reinforcement Learning: From Algorithms to Foundation Models
- **Authors:** Zihan Ding
- **Institution:** Princeton University (PhD Thesis)
- **Link:** [2607.17560](https://arxiv.org/abs/2607.17560)
- **Date:** Jul 21, 2026
- **Abstract:** Thesis covering RL from two perspectives: multi-agent RL in games (two-player zero-sum, large-scale video games, general-sum) and RL with generative/foundation models (diffusion world models, RL for video generation, generative models as policy classes).
- **Key Innovations:** Unified view of RL as objective-driven adaptation; diffusion-based world models; interactive video world models.

### 25. LLM-SoccerArena: Benchmarking LLMs on Real-World Predictions in Sports
- **Authors:** Jonas Schröder, Jonas Schweisthal, Oliver Müller, Markus Weinmann, Stefan Feuerriegel
- **Institution:** — (multi-affiliation)
- **Link:** [2607.24567](https://arxiv.org/abs/2607.24567)
- **Date:** Jul 27, 2026
- **Abstract:** Benchmarks LLMs on real-world sports prediction tasks.
- **Key Innovations:** Novel benchmark bridging LLM capabilities and real-world prediction in sports domain.

---

## RAG & Information Retrieval

### 26. APS-RAG: A Corrective Agentic Hybrid RAG for Scientific Facilities
- **Authors:** Rajat Sainju, Dariusz Jarosz, Hairong Shang et al.
- **Institution:** — (multi-affiliation)
- **Link:** [2607.24663](https://arxiv.org/abs/2607.24663)
- **Date:** Jul 27, 2026
- **Abstract:** Hybrid retrieval-augmented generation system for scientific facilities with corrective agentic loop for improved knowledge access.
- **Key Innovations:** Corrective agentic loop for RAG; operations-grounded evaluation for scientific facilities.

### 27. RAGAL: A Frugal, Fully Local RAG Assistant for Technical Support at a Government Agency
- **Authors:** — (multi-author)
- **Institution:** — (government agency)
- **Link:** [2607.18756](https://arxiv.org/abs/2607.18756)
- **Date:** Jul 21, 2026
- **Abstract:** Fully local RAG demonstrating retrieval engineering + fine-tuning crucial under data-locality constraints. Hybrid retrieval with intent routing raised accuracy from 62% to 81%.
- **Key Innovations:** Local-only deployment constraints; fine-tuned bge-m3 embedder improved recall@10 from 0.663 to 0.850 in 72 min; GenQ for domain adaptation.

### 28. VecTree-RAG: An Agentic RAG Framework Combining Vector and Tree Retrieval
- **Authors:** Xinyan Zhong, Yuwei Shi, Yuqi Wei, Chen Shen, Tianhang Zhou
- **Institution:** — (multi-affiliation)
- **Link:** [2607.23006](https://arxiv.org/abs/2607.23006)
- **Date:** Jul 26, 2026
- **Abstract:** Agentic RAG combining vector and tree retrieval structures for improved efficiency and accuracy.
- **Key Innovations:** Hybrid vector + tree retrieval; agentic orchestration for retrieval strategy selection.

---

## Weekly Highlights (July 22–29, 2026)

| # | Paper | Category | One-Line TLDR |
|---|-------|----------|---------------|
| 1 | Benchmarking Fine-tuning and Retrieval for Multimodal LLM on NRC Exam | LLM Applications | SFT + RAG passes 8/14 nuclear reactor exams (79.7%) |
| 2 | MeetingToM: Theory-of-Mind in Multi-Party Meetings | LLM Benchmark | New benchmark evaluating MLLMs on complex social reasoning |
| 3 | Appearance Pointers — Multimodal Region Control of Diffusion Transformers | Image Generation | Region-aware multimodal control without retraining |
| 4 | DBA-Bench: LLM Database Operations Agents | LLM Agents | 106 scenarios reveal LLMs far from human DBA performance |
| 5 | Agentic Real2Sim: Physics-based World Modeling | Robotics | VLM agents automate real-to-sim conversion |
| 6 | MV-Bench: MLLMs for Multi-View Interface Construction | MLLM Benchmark | MLLMs struggle with data binding and interaction logic |
| 7 | SciCodePile: 128GB Scientific Code Generation Benchmark | Code Generation | 15 LLMs scored 12.30% Pass@1 — scientific code is hard |
| 8 | GEAR: Evidence-Aware RL for Long-Context Reasoning | LLM Reasoning | Reward shaping reduces repetitive copying in long context |
| 9 | RAGAL: Fully Local RAG for Government Tech Support | RAG | Retrieval engineering + fine-tuning key under data-locality |
| 10 | KineBench: Embodied World Models Benchmark | Robotics | IDM-free closed-loop benchmark for physical consistency |

---

## Emerging Themes

1. **Generative Recommendation is mainstreaming** — LaRec, CogRec, OxygenREC-v2, UniR², DLMRec all adopt generative paradigms for RecSys, moving beyond traditional retrieval+ranking pipelines.

2. **LLMs for advertising** — SAGE (auto-bidding), LO-FAR (ad feature ranking), and Fine-Tuned LLM as Complementary Predictor show practical LLM integration in ad systems.

3. **Cold-start & debiasing** — IDProxy (MLLM for cold-start CTR), PinEqualizer (full-funnel debiasing at Pinterest), and DANet (discount-aware CVR) tackle practical deployment challenges.

4. **Agentic RAG** — APS-RAG, VecTree-RAG, and RAGAL all incorporate agentic loops for corrective retrieval and multi-strategy orchestration.

5. **LLM reasoning architectures** — Agora (auction-based allocation), GEAR (evidence-aware RL), and LIFT (principal-weight sparse FT) push reasoning capabilities without fully scaling model size.

6. **Efficient architectures** — Dual-Stream MLP for CTR and Mamba-3 for general sequence modeling demonstrate that simpler/alternate architectures can compete with large Transformers.
