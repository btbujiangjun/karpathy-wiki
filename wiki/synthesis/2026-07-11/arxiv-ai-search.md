---
title: "arXiv AI/LLM/Rec/CTR/Games Paper Search Report"
type: synthesis
created: 2026-07-11
updated: 2026-07-11
sources: []
tags: [arxiv, llm, recommendation, ctr, sequential-modeling, advertising, games, reinforcement-learning, multi-agent]
---

# arXiv Recent AI Paper Search Report — 2026-07-11

> Papers collected from arXiv across LLMs, recommendation systems, CTR prediction, sequential modeling, advertising, and AI games. All papers are from 2026.

---

## 1. LLMs & Reasoning

### 1.1 LLM-as-a-Tutor: Policy-Aware Prompt Adaptation for Non-Verifiable RL
- **Authors**: Yujin Kim, Namgyu Ho, Sangmin Hwang, Joonkee Kim, Yongjin Yang, Sangmin Bae, Seungone Kim, Jaehun Jung, Se-Young Yun, Hwanjun Song
- **Institution**: KAIST, Upstage, University of Toronto, Carnegie Mellon University, NVIDIA
- **Abstract**: Addresses the misalignment between prompt difficulty and policy capability in non-verifiable RL. Introduces LLM-as-a-Tutor framework where a single model acts as both examiner (pairwise comparison to detect non-challenging prompts) and generator (appends atomic constraints to increase difficulty). This append-only design monotonically raises difficulty in step with the policy's capability, producing a self-calibrating training signal.
- **Key Innovations**: Self-calibrating prompt difficulty mechanism; append-only constraint generation; joint examiner-generator model; no external difficulty schedules needed.
- **Link**: https://arxiv.org/abs/2607.04412

### 1.2 Online Safety Monitoring for LLMs
- **Authors**: Mona Schirmer, Metod Jazbec, Alexander Timans, Christian Naesseth, Maja Waldron, Eric Nalisnick
- **Institution**: (not specified in search results)
- **Abstract**: Studies real-time monitoring of LLM outputs using a verifier signal thresholded via risk control. The simple design is competitive with sequential hypothesis testing methods on mathematical reasoning and red teaming datasets, while detecting failures earlier in generation.
- **Key Innovations**: Risk-control-based real-time monitoring; competitive with complex sequential hypothesis testing; universal applicability across safety risks.
- **Link**: https://arxiv.org/abs/2607.02510

### 1.3 Mechanistically Eliciting Latent Behaviors in Language Models
- **Authors**: Andrew Mack, Nina Panickssery, Alexander Matt Turner
- **Institution**: Principles of Intelligence, Anthropic, Independent
- **Abstract**: Introduces Causal Perturbative Elicitation (CPE), an unsupervised method for discovering interpretable LoRA adapters that surface hidden behavioral modes. CPE decomposes transformer computations via tensor decomposition, learning interpretable LoRAs from a single example. Competitive with GRPO on Countdown task (85% vs 87%), recovers sandbagging behavior, and eliminates alignment-faking.
- **Key Innovations**: Unsupervised LoRA discovery; single-example data efficiency; weight-space exploration (vs token-space); eliminates alignment-faking in Llama3-70B.
- **Link**: https://arxiv.org/abs/2606.29604

### 1.4 Resource-Efficient Reinforcement for Reasoning LLMs via Dynamic One-Shot Policy Refinement (DoPR)
- **Authors**: Yunjian Zhang, Sudong Wang, Yang Li, Peiran Xu, Conghao Zhou, Xiaoyue Ma et al.
- **Institution**: (not specified)
- **Abstract**: Proposes DoPR, an uncertainty-aware RL strategy that dynamically selects a single informative training sample per batch for policy updates. Reduces rollout overhead by nearly an order of magnitude while preserving reasoning accuracy. Establishes theoretical lower bound on sample complexity for RLVR.
- **Key Innovations**: Single-sample-per-batch policy refinement; entropy-modulated UCB acquisition; order-of-magnitude rollout reduction; theoretical sample complexity bound.
- **Link**: https://arxiv.org/abs/2602.00815

### 1.5 MINER: Mining Intrinsic Mastery for Data-Efficient RL in Large Reasoning Models
- **Authors**: Shuyang Jiang, Yuhao Wang, Ya Zhang, Yanfeng Wang, Yu Wang
- **Institution**: Fudan University, Shanghai Jiao Tong University, Shanghai AI Laboratory
- **Abstract**: Repurposes policy's intrinsic uncertainty as a self-supervised reward signal for positive-homogeneous prompts where all rollouts are correct. Token-level focal credit assignment amplifies gradients on critical uncertain tokens. Achieves +4.58 Pass@1 gains over GRPO with zero additional inference overhead.
- **Key Innovations**: Intrinsic uncertainty as reward signal; token-level focal credit assignment; adaptive advantage calibration; zero additional rollout cost.
- **Link**: https://aclanthology.org/2026.acl-long.237

### 1.6 LEASH: Adaptive Length Penalty and Reward Shaping for Efficient Large Reasoning Models
- **Authors**: Yanhao Li, Lu Ma, Jiaran Zhang, Lexiang Tang, Wentao Zhang, Guibo Luo
- **Institution**: (not specified)
- **Abstract**: Formulates reasoning-length control as constrained optimization with Lagrangian primal-dual method. Reduces average reasoning length by 60% across diverse tasks while maintaining competitive performance on mathematical reasoning, coding, and instruction following.
- **Key Innovations**: Adaptive dual-variable length penalty; one-sided penalized reward; primal-dual optimization for automatic length control.
- **Link**: https://aclanthology.org/2026.acl-long.129

### 1.7 OpenRLHF: Easy-to-use, Scalable, High-performance RLHF Framework
- **Authors**: (large team)
- **Institution**: (multiple institutions)
- **Abstract**: Open-source RLHF/RLVR framework built on Ray, vLLM, DeepSpeed, and HuggingFace. Achieves 1.22x-1.68x speedup over verl across model sizes. Simplified design with clear code structure. Adopted by leading institutions.
- **Key Innovations**: Ray-based distributed orchestration; vLLM-accelerated CoT inference; 3D parallelism; asynchronous dataflow.
- **Link**: https://arxiv.org/abs/2405.11143v6

---

## 2. CTR Prediction & Sequential Recommendation

### 2.1 GRAB: An LLM-Inspired Sequence-First Click-Through Rate Prediction Modeling Paradigm
- **Authors**: Shaopeng Chen, Chuyue Xie, Huimin Ren, Shaozong Zhang, Han Zhang, Ruobing Cheng et al.
- **Institution**: Baidu
- **Abstract**: End-to-end generative framework for CTR prediction at Baidu. Integrates Causal Action-aware Multi-channel Attention (CamA) to capture temporal dynamics and action signals. Online deployment: 3.05% revenue increase, 3.49% CTR increase. Demonstrates scaling behavior with longer sequences.
- **Key Innovations**: Generative CTR paradigm; CamA mechanism for temporal + action signals; monotonic scaling with sequence length; full industrial deployment.
- **Link**: https://arxiv.org/abs/2602.01865

### 2.2 SparseCTR: Sparse Attention on Long-term Behaviors for CTR Prediction
- **Authors**: Weijiang Lai, Beihong Jin, Di Zhang, Siru Chen, Jiongyan Zhang, Yuhang Gou et al.
- **Institution**: (not specified)
- **Abstract**: Proposes personalized behavior sequence chunking and three-branch sparse self-attention for global interests, interest transitions, and short-term interests. Composite relative temporal encoding via learnable head-specific bias. Exhibits scaling law across three orders of magnitude in FLOPs. Online: CTR +1.72%, CPM +1.41%.
- **Key Innovations**: Personalized chunking; three-branch sparse attention; composite temporal encoding; demonstrated scaling law for CTR.
- **Link**: https://arxiv.org/abs/2601.17836

### 2.3 Generative Long-term User Interest Modeling for CTR Prediction
- **Authors**: Jiangli Shao, Kaifu Zheng, Hao Fang, Huimu Ye, Zhiwei Liu, Bo Zhang et al.
- **Institution**: (not specified)
- **Abstract**: Models long-term user interests with massive historical behaviors to enhance CTR prediction.
- **Key Innovations**: Generative modeling of long-term user interests.
- **Link**: https://arxiv.org/abs/2605.15905

### 2.4 HyTRec: Hybrid Temporal-Aware Attention for Long Behavior Sequential Recommendation
- **Authors**: Lei Xin, Yuhao Zheng, Ke Cheng, Changjiang Jiang, Zifan Zhang, Fanhu Zeng
- **Institution**: Shanghai Dewu Information Group, Wuhan University, USTC, Beihang University
- **Abstract**: Hybrid attention architecture decoupling long-term stable preferences (linear attention) from short-term intent spikes (softmax attention). Temporal-Aware Delta Network (TADN) upweights fresh signals. Over 8% improvement in Hit Rate for ultra-long sequences with linear inference speed.
- **Key Innovations**: Hybrid linear+softmax attention; TADN for interest drift; industrial-scale (10K interactions); linear inference complexity.
- **Link**: https://arxiv.org/abs/2602.18283

### 2.5 FuXi-γ: Efficient Sequential Recommendation with Exponential-Power Temporal Encoder
- **Authors**: Dezhi Yi, Wei Guo, Wenyang Cui, Wenxuan He, Huifeng Guo, Yong Liu, Zhenhua Dong, Ye Lu
- **Institution**: Nankai University, Huawei Technologies
- **Abstract**: Decoder-only Transformer with exponential-power temporal encoder (inspired by Ebbinghaus forgetting curve) and diagonal-sparse positional mechanism. Training accelerated 4.74x, inference 6.18x. KDD 2026.
- **Key Innovations**: Exponential-power temporal encoding; diagonal-sparse positional mechanism; continuous memory access; 4-6x speedup.
- **Link**: https://arxiv.org/abs/2512.12740

### 2.6 MVCrec: Multi-View Contrastive Learning for Sequential Recommendation
- **Authors**: Xiaofan Zhou, Kyumin Lee
- **Institution**: (not specified)
- **Abstract**: Integrates ID-based sequential and graph-based views with three contrastive objectives (within-sequential, within-graph, cross-view). Multi-view attention fusion with global+local mechanisms. Up to 14.44% NDCG@10 improvement over strongest baseline on five benchmarks.
- **Key Innovations**: ID+graph multi-view contrastive learning; cross-view contrastive objective; multi-view attention fusion.
- **Link**: https://arxiv.org/abs/2604.14114

### 2.7 Mixture of Sequence: Theme-Aware Mixture-of-Experts for Long-Sequence Recommendation
- **Authors**: Xiao Lin, Zhicheng Tang, Weilin Cong, Mengyue Hang, Kai Wang, Yajuan Wang et al.
- **Institution**: (not specified)
- **Abstract**: Theme-aware MoE architecture for long-sequence recommendation.
- **Key Innovations**: Theme-aware MoE routing for long sequences.
- **Link**: https://arxiv.org/abs/2604.20858

### 2.8 DiffuMIN: Diffusion-driven Multi-interest Network for CTR Prediction
- **Authors**: Weijiang Lai, Beihong Jin, Yapeng Zhang, Yiyuan Zheng, Rui Zhao, Jian Dong et al.
- **Institution**: (not specified)
- **Abstract**: Two-stage model: target-oriented multi-interest extraction via orthogonal decomposition of target embeddings, then diffusion module to generate augmented interests. Online A/B: CTR +1.52%, CPM +1.10%.
- **Key Innovations**: Diffusion modeling for user interests in CTR; orthogonal interest channel decomposition; target-oriented multi-interest extraction; contrastive learning for augmented interests.
- **Link**: https://arxiv.org/abs/2508.15311

---

## 3. Recommendation with LLMs & Knowledge Graphs

### 3.1 Memento: Personalized RAG-Style Long-Retention Data Scaling for META Ads Recommendation
- **Authors**: Xiaoyu Chen, Ruichen Wang, Jieming Di, Suofei Feng, Nafis Abrar, Lilly Kumari et al.
- **Institution**: Meta
- **Abstract**: RAG-style approach for META ads recommendation with long-retention data scaling.
- **Key Innovations**: Personalized RAG for ads recommendation; long-retention data utilization.
- **Link**: https://arxiv.org/abs/2605.24051

### 3.2 Filling the Gaps: Selective Knowledge Augmentation for LLM Recommenders (KnowSA)
- **Authors**: (not fully specified)
- **Institution**: (not specified)
- **Abstract**: Training-free framework addressing knowledge gap problem in LLM recommenders. Estimates LLM's internal knowledge via Comparative Knowledge Probing (CKP) and selectively injects external info only where needed. Avoids wasting context budget on well-known items.
- **Key Innovations**: Comparative Knowledge Probing; selective augmentation based on collaborative patterns; no fine-tuning needed; efficient context budget usage.
- **Link**: https://arxiv.org/abs/2604.07825

### 3.3 Enhancing LLM-based Recommendation with Preference Hint Discovery from Knowledge Graph (PIDLR)
- **Authors**: (not specified)
- **Institution**: (not specified)
- **Abstract**: Discovers preference hints from interaction-integrated KG to enhance LLM recommendation. Collaborative preference hint extraction from similar users' interactions; instance-wise dual-attention for preference credibility. 3.02% average improvement over baselines.
- **Key Innovations**: KG-based preference hint discovery; collaborative hint extraction for unseen items; dual-attention preference credibility scoring; flattened hint organization.
- **Link**: https://arxiv.org/abs/2601.18096

### 3.4 Leveraging LLMs and Heterogeneous Knowledge Graphs for Persona-Driven Session-Based Recommendation
- **Authors**: (not specified)
- **Institution**: (not specified)
- **Abstract**: Two-stage framework: Heterogeneous Deep Graph Infomax learns KG-grounded user personas, then integrates with LLM-derived item embeddings for candidate retrieval. Combines stable long-term preferences with short-term session intent.
- **Key Innovations**: Heterogeneous KG persona learning; unsupervised persona extraction via HDGI; LLM-initialized KG; two-stage retrieval+reranking.
- **Link**: https://arxiv.org/abs/2604.06928

### 3.5 E-MMKGR: Unified Multimodal Knowledge Graph Framework for E-commerce
- **Authors**: Jiwoo Kang, Yeon-Chang Lee
- **Institution**: (not specified)
- **Abstract**: Constructs e-commerce-specific Multimodal Knowledge Graph with item-modality and cross-item edges. GNN propagation with KG-oriented RotatE loss. Up to 10.18% Recall@10 for recommendation, 21.72% improvement for product search.
- **Key Innovations**: E-commerce multimodal KG construction; unified representations for recommendation + search; modal-modal edges for cross-item semantics.
- **Link**: https://arxiv.org/abs/2602.20877

### 3.6 Synthetic Consumer Insight Generation with Large Language Models
- **Authors**: Stephen L. France, Pia A. Albinsson
- **Institution**: (not specified)
- **Abstract**: Tests LLM-generated synthetic consumer data for projective techniques. Substantial overlap in broad topics between human and LLM responses, but differences in style and linguistic structure.
- **Key Innovations**: LLM-generated synthetic consumer data; multi-task, multi-model evaluation framework.
- **Link**: https://arxiv.org/abs/2607.05761

---

## 4. Advertising & Sponsored Search

### 4.1 OneRanker: Unified Generation and Ranking with One Model in Industrial Advertising Recommendation
- **Authors**: (not fully specified)
- **Institution**: (not specified)
- **Abstract**: Single model handling both generation and ranking in industrial advertising.
- **Key Innovations**: Unified generation+ranking paradigm.
- **Link**: https://arxiv.org/abs/2603.02999

### 4.2 Unified Supervision for Walmart's Sponsored Search Retrieval
- **Authors**: Shasvat Desai
- **Institution**: Walmart
- **Abstract**: Bi-encoder training for sponsored search using semantic relevance as primary supervision with engagement only as preference among relevant items. Combines cross-encoder teacher relevance labels, multichannel retrieval priors, and user engagement. Accepted to SIGIR 2026 Industry Track.
- **Key Innovations**: Relevance-first supervision with engagement as preference; cross-encoder teacher distillation; multichannel retrieval prior integration.
- **Link**: https://arxiv.org/abs/2604.07930

### 4.3 From Hidden Profiles to Governable Personalization: Recommender Systems in the Age of LLM Agents
- **Authors**: (not specified)
- **Institution**: (not specified)
- **Abstract**: Proposes shift from hidden platform profiling to governable personalization where user representations become inspectable.
- **Key Innovations**: Governable personalization framework; inspectable user representations.
- **Link**: https://arxiv.org/abs/2604.20065

---

## 5. Multi-Agent Games & AI

### 5.1 Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games
- **Authors**: (not fully specified)
- **Institution**: (not specified)
- **Abstract**: RL-based framework improving LLMs' strategic reasoning in multi-agent games.
- **Key Innovations**: RL-enhanced strategic reasoning for LLMs.
- **Link**: https://arxiv.org/abs/2605.04906

### 5.2 MARL-GPT: Foundation Model for Multi-Agent Reinforcement Learning
- **Authors**: (not fully specified)
- **Institution**: (not specified)
- **Abstract**: Single GPT-based model trained via offline RL on expert trajectories (400M-1B) across SMACv2, Google Research Football, and POGEMA. Competitive with specialized baselines in all environments without task-specific tuning.
- **Key Innovations**: First multi-task MARL foundation model; scale of expert trajectory training (up to 1B); zero task-specific tuning; competitive with specialized single-task baselines.
- **Link**: https://arxiv.org/abs/2604.05943

### 5.3 FAMOU: Co-Evolutionary Mechanisms for LLM-Driven Strategy Evolution in Adversarial Games
- **Authors**: (not fully specified)
- **Institution**: (not specified)
- **Abstract**: LLM-driven code evolution for 3v3 maritime CTF (MCTF 2026). Three mechanisms: evaluator co-evolution, hierarchical deep evaluation, weakness pressure. FAMOU outperforms OpenEvolve and ShinkaEvolve, achieving 68% win rate. 1st place hardware round-robin at AAMAS 2026 MCTF.
- **Key Innovations**: Evaluator co-evolution; hierarchical deep evaluation; weakness pressure; LLM-generated tactical structures (lookahead search, EWMA interception) absent from seeds.
- **Link**: https://arxiv.org/abs/2606.10389

### 5.4 MEMO: Memory-augmented Model Context Optimization for Multi-Agent LLM Games
- **Authors**: (not fully specified)
- **Institution**: (not specified)
- **Abstract**: Weight-free self-play framework coupling persistent memory bank with tournament-style prompt evolution. Raises GPT-4o-mini mean win rate from 25.1% to 49.5%, Qwen-2.5-7B from 20.9% to 44.3% using 2000 self-play games (19x fewer than RL baselines). Reduces run-to-run variance by 7x.
- **Key Innovations**: Persistent memory bank for trajectory distillation; tournament-style context evolution; prioritized replay; 19x sample efficiency vs RL; cross-game generalization.
- **Link**: https://arxiv.org/abs/2603.09022

### 5.5 Fluid-Agent Reinforcement Learning
- **Authors**: Shishir Sharma, Doina Precup, Theodore J. Perkins
- **Institution**: (not specified)
- **Abstract**: Framework allowing agents to create other agents in fluid-agent environments.
- **Key Innovations**: Agent creation by agents; fluid-agent environment framework.
- **Link**: https://arxiv.org/abs/2602.14559

### 5.6 NePPO: Near-Potential Policy Optimization for General-Sum Multi-Agent RL
- **Authors**: Addison Kalanther, Sanika Bharvirkar, Shankar P. Sastry, Chinmay Maheshwari
- **Institution**: (not specified)
- **Abstract**: Policy optimization for general-sum multi-agent games.
- **Key Innovations**: Near-potential policy optimization for general-sum games.
- **Link**: https://arxiv.org/abs/2603.06977

### 5.7 ConventionPlay: Capability-Limited Training for Robust Ad-Hoc Collaboration
- **Authors**: Abhishek Sriraman, Eleni Vasilaki, Robert W. Loftin
- **Institution**: (not specified)
- **Abstract**: RL approach extending cognitive hierarchies with adaptive followers. Agent learns to probe partner's repertoire, leading when possible and following when necessary.
- **Key Innovations**: Capability-limited partner training; probing + leading/following strategy.
- **Link**: https://arxiv.org/abs/2604.18123

---

## 6. Other Notable AI Papers

### 6.1 Causal Methods for LLM Development and Evaluation
- **Authors**: Dennis Frauen, Marie Brockschmidt, Konstantin Heß, Haorui Ma, Yuchen Ma, Abdurahman Maarouf, Maresa Schröder et al.
- **Institution**: (multiple)
- **Abstract**: Argues many central questions in LLM development are inherently causal. Maps opportunities across pretraining, alignment, routing, agentic workflows, and evaluation.
- **Key Innovations**: Causal inference framework for LLM pipeline; identification of confounding in logged data; principled estimation methods.
- **Link**: https://arxiv.org/abs/2605.25998

### 6.2 A Hierarchical Language Model with Predictable Scaling Laws
- **Authors**: Jason Gaitonde, Frederic Koehler, Elchanan Mossel, Joonhyung Shin, Allan Sly
- **Institution**: (academic)
- **Abstract**: Synthetic hierarchical languages with exact analysis of context length and reasoning. Proves Ω(n) lower bound on context length for faithful sampling, but Θ(log n) reasoning model achieves exact sampling.
- **Key Innovations**: Exact k-gram ansatz; formal scaling law derivation; exponential advantage of reasoning over bounded context.
- **Link**: https://arxiv.org/abs/2605.13687

### 6.3 NaviGen: Navigating User Behavior toward Personalized Multimodal Generation
- **Authors**: (not specified)
- **Institution**: (not specified)
- **Abstract**: Unified framework turning user behavior sequences into generation-ready creation instructions for personalized AIGC.
- **Key Innovations**: Behavior-to-creation-instruction pipeline; personalized multimodal generation.
- **Link**: https://arxiv.org/abs/2606.24196

---

## Summary Table

| # | Paper | Topic | Key Contribution | Link |
|---|-------|-------|-----------------|------|
| 1 | LLM-as-a-Tutor | LLM/RL | Self-calibrating prompt difficulty | [2607.04412](https://arxiv.org/abs/2607.04412) |
| 2 | Online Safety Monitoring | LLM Safety | Risk-control-based real-time monitoring | [2607.02510](https://arxiv.org/abs/2607.02510) |
| 3 | CPE | LLM Mechanistic | Unsupervised LoRA discovery, eliminates alignment-faking | [2606.29604](https://arxiv.org/abs/2606.29604) |
| 4 | DoPR | LLM/RL Efficiency | Single-sample-per-batch RL, 10x rollout reduction | [2602.00815](https://arxiv.org/abs/2602.00815) |
| 5 | MINER | LLM/RL Efficiency | Intrinsic uncertainty as reward, +4.58 Pass@1 | ACL 2026 |
| 6 | LEASH | LLM Reasoning | 60% length reduction, adaptive penalty | ACL 2026 |
| 7 | OpenRLHF | LLM Infra | 1.2-1.7x speedup, scalable RLHF | [2405.11143v6](https://arxiv.org/abs/2405.11143v6) |
| 8 | GRAB | CTR/Ads | Generative CTR at Baidu, +3.05% revenue | [2602.01865](https://arxiv.org/abs/2602.01865) |
| 9 | SparseCTR | CTR | Three-branch sparse attention, scaling law | [2601.17836](https://arxiv.org/abs/2601.17836) |
| 10 | HyTRec | Sequential Rec | Hybrid attention, 8% HR gain, linear speed | [2602.18283](https://arxiv.org/abs/2602.18283) |
| 11 | FuXi-γ | Sequential Rec | Exponential-power temporal encoder, 4-6x speedup | [2512.12740](https://arxiv.org/abs/2512.12740) |
| 12 | MVCrec | Sequential Rec | ID+graph multi-view contrastive learning | [2604.14114](https://arxiv.org/abs/2604.14114) |
| 13 | DiffuMIN | CTR | Diffusion for user interests, CTR+1.52% | [2508.15311](https://arxiv.org/abs/2508.15311) |
| 14 | Memento | Ads/Rec | Personalized RAG for META ads | [2605.24051](https://arxiv.org/abs/2605.24051) |
| 15 | KnowSA | LLM Rec | Selective knowledge augmentation | [2604.07825](https://arxiv.org/abs/2604.07825) |
| 16 | PIDLR | LLM Rec+KG | KG preference hint discovery | [2601.18096](https://arxiv.org/abs/2601.18096) |
| 17 | E-MMKGR | E-commerce | Multimodal KG for rec+search | [2602.20877](https://arxiv.org/abs/2602.20877) |
| 18 | Walmart Search | Sponsored Search | Relevance-first supervision | [2604.07930](https://arxiv.org/abs/2604.07930) |
| 19 | MARL-GPT | Multi-Agent | First MARL foundation model | [2604.05943](https://arxiv.org/abs/2604.05943) |
| 20 | FAMOU | Multi-Agent Games | LLM code evolution, 1st at AAMAS 2026 | [2606.10389](https://arxiv.org/abs/2606.10389) |
| 21 | MEMO | LLM Games | Persistent memory, 19x sample efficiency | [2603.09022](https://arxiv.org/abs/2603.09022) |
