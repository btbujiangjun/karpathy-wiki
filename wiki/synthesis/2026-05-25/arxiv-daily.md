---
title: "arXiv Daily Digest — 2026-05-25"
type: synthesis
created: 2026-05-25
updated: 2026-05-25
sources: []
tags: [arxiv, daily-digest, llm, recsys, ctr, advertising, games, sequential-modeling, code-execution]
---

# arXiv Daily Digest — 2026-05-25

> Papers submitted Mon 25 May — Fri 22 May 2026. Categories: cs.AI, cs.LG, cs.IR, cs.CL.

---

## 1. Large Language Models & Training

### 1.1 LLMs as Noisy Channels: A Shannon Perspective on Model Capacity and Scaling Laws
- **Authors:** Xu Ouyang, Deyi Liu, Yuhang Cai, Jing Liu, Yuan Yang, Chen Zheng, Thomas Hartvigsen, Yiyuan Ma
- **Affiliation:** —
- **Abstract:** Proposes the Shannon Scaling Law, a unified framework modeling LLM training as information transmission over a noisy channel. Maps model parameters to channel bandwidth and training tokens to signal power, revealing a fundamental Shannon capacity for LLMs. Explains non-monotonic phenomena like catastrophic overtraining and quantization degradation.
- **Key Contributions:**
  - First unified theory connecting Shannon-Hartley theorem to LLM scaling laws
  - Explains U-shaped performance degradation under noise (quantization, overtraining)
  - Validated on Pythia and OLMo2; predicts 12B model at 307B tokens (R²=0.847)
- **Venue:** ICML 2026
- **Link:** https://arxiv.org/abs/2605.23901

### 1.2 Strong Teacher Not Needed? On Distillation in LLM Pretraining
- **Authors:** Taiming Lu, Zhuang Liu
- **Affiliation:** —
- **Abstract:** Challenges the assumption that stronger teachers yield better students in LLM pretraining distillation. Shows that with proper mixing of LM and KD losses, even small/undertrained teachers improve larger students, and stronger teachers can saturate or reverse gains.
- **Key Contributions:**
  - Weak-to-strong distillation works with proper loss mixing
  - Stronger teachers can hurt — non-monotonic distillation behavior
  - Distillation improves OOD and downstream generalization more than in-domain fitting
- **Link:** https://arxiv.org/abs/2605.23857

### 1.3 Complete-muE: Optimal Hyperparameter Transfer and Scaling for MoE Models
- **Authors:** Hongwu Peng, Ohiremen Dibua, Yuanjun Xiong, Yifan Gong, Jianming Zhang, Yan Kang
- **Affiliation:** —
- **Abstract:** Framework for hyperparameter transfer across dense FFN and any MoE setup. Two-bridge system: Bridge I maps dense ↔ dense MoE via active-width µP, Bridge II maps dense MoE ↔ sparse MoE via activated-expert scaling.
- **Key Contributions:**
  - "Tune dense once, transfer to all" practical recipe for MoE
  - Covers changes in activated experts, capacity, granularity, shared/group-balanced hybrids
  - Accelerated MoE convergence without costly hyperparameter search
- **Link:** https://arxiv.org/abs/2605.23893

### 1.4 DiLaDiff: Distilled Latent-Augmented Diffusion for Language Modeling
- **Authors:** Jean-Marie Lemercier, Tomas Geffner, Karsten Kreis, Morteza Mardani, Arash Vahdat, Ante Jukić
- **Affiliation:** NVIDIA
- **Abstract:** Proposes a latent diffusion architecture for language modeling with consistency distillation. Combines continuous latent space from masked diffusion LM, latent diffusion prior, and consistency model for few-step generation.
- **Key Contributions:**
  - Latent-guided diffusion outperforms masked diffusion baselines
  - Consistency distillation makes latent generation near-negligible vs discrete decoding
  - Solves the correlation problem between decoded tokens in diffusion LMs
- **Link:** https://arxiv.org/abs/2605.23605

### 1.5 Training-Free Looped Transformers
- **Authors:** Lizhang Chen, Jonathan Li, Chen Liang, Ni Lao, Qiang Liu
- **Affiliation:** Google? (Ni Lao)
- **Abstract:** —
- **Key Contributions:** Training-free approach to looped transformer inference
- **Link:** https://arxiv.org/abs/2605.23872

---

## 2. Recommendation Systems

### 2.1 TubiFM: Unified Item, Carousel, and Search Ranking for Streaming Discovery
- **Authors:** Alexandre Salle, Chenglei Niu, Suchismit Mahapatra, Xiaoxiao Chen, Suvash Sedhain, Yaqi Wang, Shervin Shahryari, Saurabh Agrawal, Qiang Chen, Michael Tamir
- **Affiliation:** Tubi (Fox)
- **Abstract:** Introduces "user story" serialized representation unifying cross-surface history into a single token sequence. A Llama 3.2 1B model trained on user stories and prompted to rank items, carousels, or search without task-specific architectures.
- **Key Contributions:**
  - Single model outperforms specialist baselines across item/carousel/search ranking
  - Online: +3.9% search TVT, +0.30% carousel TVT
  - p99 latency reduced from 500ms to 200ms on L40S GPUs
- **Link:** https://arxiv.org/abs/2605.23702

### 2.2 Towards Generalizable and Efficient Large-Scale Generative Recommenders
- **Authors:** Qiuling Xu, Ko-Jen Hsiao, Moumita Bhattacharya
- **Affiliation:** Netflix
- **Abstract:** Experience scaling a generative recommender from 2M to 1B backbone parameters. Studies task-dependent scaling behavior, multi-token prediction, sampled softmax, projected decoding head, semantic item towers for cold-start.
- **Key Contributions:**
  - Offset scaling-law fits as diagnostic for task headroom
  - Multi-token prediction for serving-latency alignment
  - 1B model achieves higher MRR than 2M baseline across all tasks in production shadow eval
- **Link:** https://arxiv.org/abs/2605.23312

### 2.3 HARNESS-LM: Three-Phase Training Recipe for Harnessing SLMs in Sponsored Search Retrieval
- **Authors:** Vipul Gupta, Shikhar Mohan, Lakshya Kumar, Pranjal Chitale, Nikit Begwani, Amit Singh, Manik Varma
- **Affiliation:** Microsoft (Bing Ads)
- **Abstract:** Three-phase framework: (1) train large teacher retriever, (2) distill into sub-600M student via L2 alignment, (3) contrastive refinement. Deployed on Bing Ads.
- **Key Contributions:**
  - 98% of teacher precision recovered with 27x lower latency, 20x higher throughput
  - Online A/B: +1% Revenue, +0.6% Impression, +0.4% Click uplift
  - 190M parameter model deployed in production
- **Venue:** —
- **Link:** https://arxiv.org/abs/2605.23572

### 2.4 LLM Retrieval for Stable and Predictable Ad Recommendations
- **Authors:** Vinodh Kumar Sunkara, Satheeshkumar Karuppusamy, Hangjun Xu, Sai Deepika Regani, Kshitij Gupta, Gaby Nahum, Sneha Iyer, Jean-Baptiste Fiot, Yinglong Guo, Xiaowen Guo, Atul Jangra, Yucheng Liu, Jinghao Yan, Vijay Pappu, Benjamin Schulte, Deepak Chandra
- **Affiliation:** LinkedIn (Microsoft)
- **Abstract:** Introduces evaluation framework for stability/predictability of ads recommender systems. Uses fine-tuned LLMs for semantic candidate generation with graph-based expansion ensuring consistent ad delivery.
- **Key Contributions:**
  - First formal framework for ads recommendation stability and predictability
  - LLM-powered semantic candidate generation with graph-based expansion
  - Validated in large-scale industrial ads system
- **Venue:** SIGIR 2026 AgentSearch Workshop
- **Link:** https://arxiv.org/abs/2605.21969

### 2.5 Reinforced Preference Optimization for Reasoning-Augmented Recommendations (RPORec)
- **Authors:** Jingtong Gao, Zeyu Song, Chi Lu, Xiaopeng Li, Derong Xu, Maolin Wang, Peng Jiang, Kun Gai, Qingpeng Cai, Xiangyu Zhao
- **Affiliation:** Kuaishou
- **Abstract:** Two-stage framework: (1) Reasoning-Augmented Recommendation Modeling with CoT to guide Rechead; (2) Advanced Reasoning Refinement using RL with verifiable rewards from Rechead.
- **Key Contributions:**
  - RL alignment of LLM reasoning for recommendation objectives
  - Verifiable reward from dedicated recommendation head
  - Outperforms SOTA LLM-based rec methods in online deployment
- **Link:** https://arxiv.org/abs/2605.21967

### 2.6 Bridging the Cold-Start Gap: LLM-Powered Synthetic Data Generation for Natural Language Search at Airbnb
- **Authors:** Wendy Ran Wei, Hao Li, Weiwei Guo, Xiaowei Liu, Xueyin Chen, Dillon Davis, Malay Haldar, Soumyadip Banerjee, Kedar Bellare, Huiji Gao, Stephanie Moyerman, Sanjeev Katariya
- **Affiliation:** Airbnb
- **Abstract:** Framework for generating synthetic queries and labels using LLMs for Airbnb's natural language search. Combines contrastive listing pairs with seed queries. Virtual Judge labeling for broader coverage.
- **Key Contributions:**
  - Seed-guided query generation achieves KL divergence 0.66 vs real users (7.5x better than InPars)
  - Attribute type distribution KL divergence of 0.04
  - Production pipelines generating synthetic examples daily
- **Link:** https://arxiv.org/abs/2605.21812

### 2.7 Expand More, Shrink Less: Shaping Effective-Rank Dynamics for Dense Scaling in Recommendation (RankElastor)
- **Authors:** Guoming Li, Shangyu Zhang, Junwei Pan, Wentao Ning, Jin Chen, Gengsheng Xue, Chao Zhou, Shudong Huang, Haijie Gu, Menglin Yang
- **Affiliation:** —
- **Abstract:** Identifies embedding collapse in RankMixer as damped oscillatory effective-rank evolution. Proposes RankElastor with parameterized full mixing and GLU-improved P-FFNs for spectrum-robust representations.
- **Key Contributions:**
  - Theoretical analysis of embedding collapse in recommendation scaling
  - RankElastor provably mitigates collapse
  - Consistent improvements on large-scale industrial datasets
- **Venue:** KDD 2026
- **Link:** https://arxiv.org/abs/2605.23191

---

## 3. CTR Prediction & Advertising

### 3.1 SkillOpt: Executive Strategy for Self-Evolving Agent Skills
- **Authors:** Yifan Yang, Ziyang Gong, Weiquan Huang, Qihao Yang, Ziwei Zhou, Zisu Huang, Yan Li, Xuemei Gao, Qi Dai, Bei Liu, Kai Qiu, Yuqing Yang, Dongdong Chen, Xue Yang, Chong Luo
- **Affiliation:** Microsoft Research Asia
- **Abstract:** First systematic controllable text-space optimizer for agent skills. Optimizer model turns scored rollouts into bounded edits; accepted only when improving held-out validation score. Includes textual learning-rate budget, rejected-edit buffer, epoch-wise slow/meta update.
- **Key Contributions:**
  - Best or tied on all 52 evaluated (model, benchmark, harness) cells
  - +23.5 points on GPT-5.5 direct chat, +24.8 in Codex, +19.1 in Claude Code
  - Zero inference-time overhead at deployment
- **Link:** https://arxiv.org/abs/2605.23904

---

## 4. Games & Strategic Reasoning

### 4.1 One Policy, Infinite NPCs: Persona-Traceable Shared RL Policies for Scalable Game Agents
- **Authors:** Yoosung Hong
- **Affiliation:** —
- **Abstract:** PCSP (Persona Conditioned Shared Policy) — single RL policy conditioned on frozen LLM embeddings of persona descriptions. PPO + InfoNCE consistency + KL diversity. Validated on 300-persona life-simulation benchmark and UE5 deployment.
- **Key Contributions:**
  - Compositional zero-shot persona identification 17x above chance
  - Spearman ρ ≈ 0.73 semantic-behavioral alignment
  - 22x faster inference than LLM-as-policy baseline
  - UE5 deployment with 64 agents at sub-frame inference
- **Link:** https://arxiv.org/abs/2605.23652

### 4.2 GENSTRAT: Toward a Science of Strategic Reasoning in Large Language Models
- **Authors:** Vartan Shadarevian, Kia Ghods, Alex Kenich, Anany Kotawala
- **Affiliation:** —
- **Abstract:** Procedurally generated two-player zero-sum imperfect-information card games for evaluating strategic reasoning. Capability-profile methodology across 6 axes with jaggedness measure. 50 benchmark games, 9 LLMs, 36K+ matches.
- **Key Contributions:**
  - Evergreen evaluation resistant to contamination via procedural generation
  - gpt-5 and claude more locally volatile than gemini-3.1-pro despite similar overall strength
  - Deployment-relevant diagnostic beyond overall ranking
- **Link:** https://arxiv.org/abs/2605.23238

---

## 5. Agents & Multi-Agent Systems

### 5.1 Foundation Protocol: A Coordination Layer for Agentic Society
- **Authors:** Bang Liu, Yongfeng Gu, Jiayi Zhang, Zhaoyang Yu, Sirui Hong, Maojia Song, Xiaoqiang Wang, Mingyi Deng, Zijie Zhuang, Ronghao Wang, Mingzhe Cao, Yutong Zhu, Xingjian Li, Yifan Wu, Jianhao Ruan, Yiran Peng, Shuangrui Chen, Jinlin Wang, Yizhang Lin, Dongjie Zhang, Dekun Wu, Chen Ma, Lizi Liao, Han Yu, Jian Pei, Heng Ji, Qiang Yang, Yuyu Luo, Chenglin Wu
- **Affiliation:** Multiple (incl. Tencent, HKUST, UIUC, etc.)
- **Abstract:** A coordination protocol for agentic ecosystems enabling structured inter-agent communication and cooperation.
- **Key Contributions:**
  - Standardized coordination layer for multi-agent systems
  - Large collaboration across academia and industry
- **Link:** https://arxiv.org/abs/2605.23218

### 5.2 AutoResearch AI: Towards AI-Powered Research Automation for Scientific Discovery
- **Authors:** Guiyao Tie, Jiawen Shi, Dingjie Song, Yixiao Huang, Ziji Sheng, Xueyang Zhou, Daizong Liu, Pan Zhou, Yongchao Chen, Ran Xu, Lifang He, Qingsong Wen, Manling Li, Cong Lu, Shuai Li, Pengtao Xie, Yixuan Yuan, Rui Meng, Lei Xing, Lichao Sun, Caiming Xiong, Philip S. Yu, Jianfeng Gao
- **Affiliation:** Salesforce Research, multiple universities
- **Abstract:** Comprehensive framework for automated scientific research covering hypothesis generation, experiment design, execution, and analysis.
- **Key Contributions:**
  - End-to-end AI research automation pipeline
  - Covers full research lifecycle from hypothesis to analysis
- **Link:** https://arxiv.org/abs/2605.23204

### 5.3 Inductive Deductive Synthesis: Enabling AI to Generate Formally Verified Systems
- **Authors:** Shubham Agarwal, Alexander Krentsel, Shu Liu, Mert Cemri, Audrey Cheng, Rui Meng, Tomas Pfister, Chun-Liang Li, Sylvia Ratnasamy, Aditya Parameswaran, Matei Zaharia, Ion Stoica, Mohsen Lesani
- **Affiliation:** UC Berkeley, Microsoft
- **Abstract:** AI framework for generating formally verified systems combining inductive and deductive synthesis.
- **Key Contributions:**
  - Bridges AI code generation with formal verification
  - Generates provably correct system implementations
- **Link:** https://arxiv.org/abs/2605.23109

### 5.4 EVE-Agent: Evidence-Verifiable Self-Evolving Agents
- **Authors:** Yamato Arai, Yuma Ichikawa
- **Affiliation:** —
- **Abstract:** Self-evolving agents with evidence-verifiable improvement mechanisms.
- **Link:** https://arxiv.org/abs/2605.22905

### 5.5 Push Your Agent: Measuring and Enforcing Quantitative Goal Persistence in Long-Horizon LLM Agents
- **Authors:** Yuandao Cai, Yuzhang Zhu, Liyou Gao, Wensheng Tang, Shengchao Qin
- **Affiliation:** —
- **Abstract:** Framework for measuring and enforcing goal persistence in long-horizon LLM agent tasks.
- **Link:** https://arxiv.org/abs/2605.23574

---

## 6. Generative Models & Diffusion

### 6.1 Precise: SDE-Consistent Stochastic Sampling for RL Post-Training of Flow-Matching Models
- **Authors:** Jade Zou, Tao Huang, Weijie Kong, Junzhe Li, Yue Wu, Qi Tian, Jiangfeng Xiong, Jianwei Zhang, Liefeng Bo, Zhao Zhong
- **Affiliation:** ByteDance
- **Abstract:** New stochastic sampler for RL post-training of flow-matching models. Freezes clean-latent posterior mean to maintain SDE consistency. Resolves excess noise issue in standard samplers.
- **Key Contributions:**
  - 13.1-53.2% less wall-clock training time to match best in-domain performance
  - SOTA alignment scores (PickScore, HPSv2.1)
  - SDE-consistent sampling formulation
- **Link:** https://arxiv.org/abs/2605.23522

---

## 7. Code & Formal Reasoning

### 7.1 ImProver 2: Iteratively Self-Improving LMs for Neurosymbolic Proof Optimization
- **Authors:** Riyaz Ahuja, Tate Rowney, Jeremy Avigad, Sean Welleck
- **Affiliation:** Carnegie Mellon University
- **Abstract:** Iterative self-improvement for LMs in formal proof optimization through neurosymbolic techniques.
- **Link:** https://arxiv.org/abs/2605.22885

### 7.2 Agentic Proving for Program Verification
- **Authors:** Alessandro Sosso, Akhil Arora, Bas Spitters
- **Affiliation:** —
- **Abstract:** Agent-based approach to automated program verification using LLMs.
- **Link:** https://arxiv.org/abs/2605.23772

### 7.3 RMA: An Agentic System for Research-Level Mathematical Problems
- **Authors:** Zelin Zhao, Bo Yuan, Jaemoo Choi, Yongxin Chen
- **Affiliation:** —
- **Abstract:** Agentic system designed for solving research-level mathematical problems.
- **Link:** https://arxiv.org/abs/2605.22875

---

## 8. Sequential Modeling & Transformers

### 8.1 Preisach Attention: A Hysteretic Model of Sequential Memory
- **Authors:** Piotr Frydrych
- **Affiliation:** —
- **Abstract:** Novel attention mechanism based on Preisach hysteresis model for sequential memory, offering an alternative to standard transformer attention.
- **Link:** https://arxiv.org/abs/2605.23603

### 8.2 Is Dimensionality a Barrier for Retrieval Models?
- **Authors:** Kiril Bangachev, Guy Bresler, Jonathan Kogan, Yury Polyanskiy
- **Affiliation:** MIT
- **Abstract:** Theoretical analysis of dimensionality barriers in retrieval models.
- **Link:** https://arxiv.org/abs/2605.23556

---

## 9. Benchmarking & Evaluation

### 9.1 How Hard is it to Rig a Benchmark? A Social Choice Analysis of Leaderboard Robustness
- **Authors:** Polina Gordienko, Georg Schollmeyer, Frauke Kreuter, Christoph Jansen
- **Affiliation:** —
- **Abstract:** Social choice theory analysis of benchmark leaderboard robustness and manipulation.
- **Link:** https://arxiv.org/abs/2605.23628

---

## Summary

| Category | Count | Key Companies |
|----------|-------|---------------|
| LLM Training & Theory | 5 | NVIDIA, Google |
| Recommendation Systems | 7 | Netflix, Microsoft/Bing, Tubi/Fox, Kuaishou, Airbnb |
| CTR & Advertising | 1 | Microsoft Research Asia |
| Games & Strategic Reasoning | 2 | — |
| Agents & Multi-Agent | 5 | Microsoft, UC Berkeley, Salesforce, Tencent |
| Generative Models | 1 | ByteDance |
| Code & Formal Reasoning | 3 | CMU |
| Sequential Modeling | 2 | MIT |
| Benchmarking | 1 | — |
| **Total** | **27** | |
