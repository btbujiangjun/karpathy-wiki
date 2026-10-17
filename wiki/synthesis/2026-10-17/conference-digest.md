---
title: "Conference Digest: Top ML/AI Venues 2025-2026 (ICML/NeurIPS/ICLR/AAAI/KDD/CVPR/SIGIR/WWW/ACL/EMNLP/CIKM/RecSys)"
type: synthesis
created: 2026-10-17
updated: 2026-10-17
sources: [conference-web-searches, arxiv-listings]
tags: [conference-digest, ICML2026, NeurIPS2025, ICLR2026, AAAI2026, KDD2026, CVPR2026, SIGIR2026, WWW2026, ACL2026, EMNLP2025, CIKM2025, RecSys2025, recommendation, LLM, advertising, CTR, agents, generative-models, sequential-modeling, games, code-execution, benchmarks, daily-digest]
---

# Conference Digest: Top ML/AI Venues 2025-2026 — 2026-10-17

> **Date:** 2026-10-17  ·  **Type:** Conference / proceedings harvest (scheduled job)
> **Window:** Accepted-paper lists and award announcements for ICML 2026, NeurIPS 2025, ICLR 2026, AAAI 2026, KDD 2026, CVPR 2026, SIGIR 2026, WWW 2026, ACL 2026, EMNLP 2025, CIKM 2025, RecSys 2025, plus general recent papers on the requested themes (LLM/agents/recommendation/advertising/CTR/games/code-execution/generative/sequential-modeling/benchmarks).
> **Method:** Web harvest of official conference pages (icml.cc, cvpr.thecvf.com, kdd2026.kdd.org, thewebconf, sigir2026.org, 2025.emnlp.org, recsys.acm.org, aaai.org), ACM DL proceedings, OpenReview, arXiv listing/abs pages, and lab/aggregator round-ups (Google Research, NVIDIA, Meta, Amazon Science, papernotes). arXiv **export API returned `HTTP 429` ("Rate exceeded")** on date-range queries this run, so paper metadata came from listing/abstract pages and proceedings indexes. Featured papers cross-checked against the recent sibling digests (`2026-10-15/16`, `2026-09-11`) to avoid re-featuring; IDs/links verified where public.
> **Language:** Source material is English → body in English; Chinese titles provided as `title-zh`.

> ⚠️ Venue dates. ICML 2026 was held in **Seoul (COEX), Jul 6-11, 2026**; ICLR 2026 in **Rio de Janeiro, Apr 23-27, 2026**; NeurIPS 2025 in **San Diego / Mexico City, Dec 2025**; CVPR 2026 in **Denver, Jun 2026**; KDD 2026 in **Jeju Island, Aug 9-13, 2026**; SIGIR 2026 in **Melbourne, Jul 20-24, 2026**; WWW 2026 (The Web Conference); EMNLP 2025 in **Suzhou, Nov 2025**; RecSys 2025 in **Prague, Sep 22-26, 2025**; CIKM 2025 in **Seoul, Nov 2025**; AAAI 2026 in **Singapore, Jan 2026**.

---

## 1. ICML 2026 (Seoul, Korea — Jul 6-11, 2026)

**Stats:** 23,918 submissions entered review → **6,352 accepted (26.6%)**; 536 spotlights (2.2%); 168 orals. Position-paper track: 742 reviewed → 215 accepted (29%). Google alone presented **130+ papers, 27 workshops, 6 position papers**. Coverage of ICML 2026 accepted-paper pages this run: 6,634 paper rows (6,060 poster / 406 spotlight / 168 oral).

### 1.1 Outstanding Paper Awards

#### 1.1.1 The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models
- **Title (zh):** 灵活性陷阱：重新审视扩散语言模型中任意顺序的价值
- **Authors:** Zanlin Ni, Shenzhi Wang, Yang Yue, Tianyu Yu, Weilin Zhao, Yeguo Hua, Tianyi Chen, Jun Song, Cheng Yu, Bo Zheng, Gao Huang
- **Affiliation:** Tsinghua University; Baidu (inferred from author block; Bo Zheng is Alibaba/Taobao-affiliated in other works) — *reported as printed*
- **Venue:** ICML 2026 Outstanding Paper Award
- **Abstract & key innovations:** Challenges the commonly held assumption that arbitrary token order in diffusion language models (DLMs) is always beneficial. The paper shows that unconstrained order flexibility can hurt reasoning quality; a structured (e.g. fixed left-to-right) rollout during RL training improves reasoning while still allowing parallel decoding at inference time.
- **Comparison with prior methods:** Contrasts with order-agnostic DLM training recipes (e.g. masked-diffusion variants that maximize order flexibility); the "flexibility trap" argument suggests prior work optimized a proxy that does not translate to downstream reasoning.
- **Links:** ICML 2026 awards — https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/

#### 1.1.2 High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions
- **Title (zh):** 扩散模型与对数凹分布的高精度采样
- **Authors:** Fan Chen, Sinho Chewi, Constantinos Daskalakis, Alexander Rakhlin
- **Affiliation:** MIT (Daskalakis/A. Rakhlin groups)
- **Venue:** ICML 2026 Outstanding Paper Award
- **Abstract & key innovations:** Achieves δ-error sampling in `polylog(1/δ)` steps — an exponential improvement over all prior results — for general log-concave distributions using only gradient evaluations. Under minimal assumptions complexity is `Õ(d·polylog(1/δ))`.
- **Comparison with prior methods:** Prior samplers required `poly(d, 1/δ)` (or worse) steps; this is the first `polylog(1/δ)`-complexity sampler for general log-concave targets.
- **Links:** ICML 2026 awards — https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/

### 1.2 Outstanding Paper Honorable Mentions

| Paper | Authors (lead) | Theme | Key finding |
|-------|----------------|-------|-------------|
| The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes | Mohammad Taufeeque, Stefan Heimersheim, Adam Gleave, Chris Cundy | Alignment / reward hacking | Studies whether training against deception probes yields honest behavior or mere evasion. |
| Motion Attribution for Video Generation | Xindi Wu, Despoina Paschalidou, Jun Gao, Antonio Torralba, Laura Leal-Taixé, Olga Russakovsky, Sanja Fidler, Jonathan Lorraine | Video generation | Tracks which training examples affect video-generation quality (attribution for video). |
| How much can language models memorize? | John Xavier Morris, Chawin Sitawarin, Narine Kokhlikyan, Chuan Guo, G. Edward Suh, Alexander M. Rush, Kamalika Chaudhuri, Saeed Mahloujifar | Memorization | Sharper reasoning about memorization vs. generalization in LLMs. |
| A Random Matrix Perspective on the Consistency of Diffusion Models | Binxu Wang, Jacob Zavatone-Veth, Cengiz Pehlevan | Diffusion theory | Explains why diffusion models produce similar outputs across runs. |
| To Grok Grokking: Provable Grokking in Ridge Regression | Mingyue Xu, Gal Vardi, Itay Safran | Theory | Shows grokking-like delayed generalization in simple linear settings. |

**Outstanding Position Paper Honorable Mention:** *Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII)* — Li Qiwei, Wells Lucas Santo, Sarita Schoenebeck, Eric Gilbert.

**Test of Time Award:** *Asynchronous Methods for Deep Reinforcement Learning* (A3C) — Volodymyr Mnih, Adrià Puigdomènech Badia, Mehdi Mirza, Alex Graves, Timothy P. Lillicrap, Tim Harley, David Silver, Koray Kavukcuoglu (**Google DeepMind**).

### 1.3 Selected ICML 2026 Papers — Top Labs

| Title (EN / zh) | Authors | Affiliation | Innovation |
|-----------------|---------|-------------|------------|
| Autoregressive Language Models Are Secretly Energy-Based Models / 自回归语言模型其实是能量模型 | Mathieu Blondel, Michaël E. Sander, Germain Vivier-Ardisson, Tianlin Liu, Vincent Roulet | Google DeepMind | Shows next-token prediction induces an implicit energy-based model; insights into lookahead capability. |
| ATLAS: Learning to Optimally Memorize the Context at Test Time / ATLAS：测试时最优上下文记忆 | Ali Behrouz, Zeman Li, Praneeth Kacham, Majid Daliri, Yuan Deng, Peilin Zhong, Meisam Razaviyayn, Vahab Mirrokni | Google Research | Test-time memory optimization for long-context sequence models. |
| AutoNumerics-Zero: Automated Discovery of SOTA Mathematical Functions / AutoNumerics-Zero：自动发现 SOTA 数学函数 | Esteban Real, Mirko Rossini, Connal de Souza, Manav Garg, Moritz Firsching, Quoc V. Le, Yao Chen, Akhil Verghese, Ekin Dogus Cubuk, David H. Park | Google DeepMind | Automated discovery of state-of-the-art numerical function approximations. |
| Extreme Meta-Black-Box Optimization / 元黑盒优化 | (ICML 2026) | — | Search guidance for expensive constrained multi-objective optimization. |
| OpenSage: Self-Programming Agent Generation Engine / OpenSage：自编程智能体生成引擎 | Hongwei Li, Zhun Wang, Qinrun Dai, Yuzhou Nie, Jinjun Peng, Ruitong Liu, Jingyang Zhang, Kaijie Zhu, Jingxuan He, Lun Wang, Yangruibo Ding, Yueqi Chen, Wenbo Guo, Dawn Song | Google / UC Berkeley (Dawn Song) | Self-programming engine that generates agent architectures. |
| PaperBanana: Automating Academic Illustration for AI Scientists / PaperBanana：为 AI 科学家自动生成学术插图 | Dawei Zhu, Rui Meng, Yale Song, Xiyu Wei, Sujian Li, Tomas Pfister, Jinsung Yoon | Google Cloud AI Research | Automates academic figure generation for AI research papers. |
| PLANTAIN: Plan-Answer Interleaved Reasoning | (Google) | Google | Interleaving planning and answering in reasoning models. |
| CANDI: Hybrid Discrete-Continuous Diffusion Models / CANDI：离散-连续混合扩散模型 | Patrick Pynadath, Jiaxin Shi, Ruqi Zhang | Purdue | Hybridizing discrete and continuous diffusion. |
| Divergence: Beyond Markovian — Reflective Exploration via Bayes-Adaptive RL for LLM Reasoning | Shenao Zhang, Yaqing Wang, Yinxiao Liu, Tianqi Liu, Peter Grabowski, Eugene Ie, Zhaoran Wang, Yunxuan Li | Google (ICLR/ICML track) | Bayes-adaptive RL for reflective exploration beyond Markovian assumptions. |
| SCaLoRA: Optimally Scaled Low-Rank Adaptation | (ICML 2026) | — | Optimal scaling for efficient high-rank fine-tuning. |
| Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective | (ICML 2026) | — | Unified information-theoretic KV eviction. |
| ScaleEnv: Scaling Environment Synthesis from Scratch for Generalist Interactive Tool-Use Agent Training | (ICML 2026) | — | Synthesizes interactive tool-use environments for agent training. |

---

## 2. NeurIPS 2025 (San Diego / Mexico City — Dec 2025)

**Awards:** 7 papers honored — 4 Best Papers (one from the Datasets & Benchmarks track) and 3 Runner-ups — spanning diffusion theory, self-supervised RL, attention for LLMs, LLM reasoning, online learning theory, neural scaling laws, and benchmark methodology.

### 2.1 Best Papers

#### 2.1.1 Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?
- **Title (zh):** 强化学习真的能激发 LLM 超越基座模型的推理能力吗？
- **Authors:** Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Yang Yue, Shiji Song, Gao Huang
- **Affiliation:** Tsinghua University (Gao Huang / Andrew Zhao group)
- **Venue:** NeurIPS 2025 **Best Paper Runner-up**
- **Abstract & key innovations:** Systematic probe of RLVR (RL with Verifiable Rewards) capability boundaries across model families, RL algorithms, and math/coding/visual reasoning benchmarks, using `pass@k` at large `k`. Finding: RLVR improves **sampling efficiency** toward correct paths but does **not** elicit fundamentally new reasoning patterns — base models achieve higher `pass@k` at large `k`, and the reasoning boundary often **narrows** as RLVR training progresses. Reasoning paths generated by RLVR models are already in the base model's sampling distribution.
- **Comparison with prior methods:** Directly challenges the prevailing belief that RLVR enables continual self-improvement; shows six popular RLVR algorithms behave similarly and remain far from optimal. Distillation, by contrast, **can** introduce new reasoning patterns from a teacher.
- **Links:** https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/

#### 2.1.2 Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free
- **Title (zh):** 大语言模型的门控注意力：非线性、稀疏性与无注意力汇
- **Authors:** Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, Junyang Lin
- **Affiliation:** Alibaba (Qwen team), with academic collaborators (Sea AI Lab / MIT — Songlin Yang)
- **Venue:** NeurIPS 2025 **Best Paper** (Oral/Poster)
- **Abstract & key innovations:** Comprehensive comparison of 30 gating-augmented softmax attention variants across 15B MoE and 1.7B dense models trained on a 3.5T-token dataset. Central finding: applying a **head-specific sigmoid gate after Scaled Dot-Product Attention (SDPA)** consistently improves performance, enhances training stability, tolerates larger learning rates, and improves scaling. Attributed to (1) non-linearity on the low-rank softmax mapping and (2) query-dependent sparse gating scores.
- **Comparison with prior methods:** Improves on standard softmax attention and prior gating placements; directly relevant to the Qwen3 line and modern LLM attention design.
- **Links:** https://neurips.cc/virtual/2025/awards_detail

#### 2.1.3 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities
- **Title (zh):** 用于自监督 RL 的 1000 层网络：扩展深度可以带来新的目标达成能力
- **Authors:** Kevin Wang, Ishaan Javali, Michał Bortkiewicz, Tomasz Trzcinski, Benjamin Eysenbach
- **Affiliation:** Princeton University (Eysenbach); Warsaw University of Technology (Trzcinski)
- **Venue:** NeurIPS 2025 **Best Paper** (Oral/Poster)
- **Abstract & key innovations:** In unsupervised goal-conditioned RL, scaling network depth to **1024 layers** boosts performance on simulated locomotion/manipulation by **2×–50×** over a self-supervised contrastive RL algorithm, without demonstrations or rewards. Increased depth qualitatively changes learned behaviors.
- **Comparison with prior methods:** Most RL papers use 2-5 layer networks; this work shows depth scaling is a first-class lever in RL, mirroring gains seen in language/vision.
- **Links:** https://neurips.cc/virtual/2025/awards_detail

#### 2.1.4 Superposition Yields Robust Neural Scaling
- **Title (zh):** 叠加带来稳健的神经网络 Scaling
- **Authors:** Yizhou Liu, Ziming Liu, Jeff Gore
- **Affiliation:** MIT
- **Venue:** NeurIPS 2025 **Best Paper Runner-up**
- **Abstract & key innovations:** Proposes that **representation superposition** (representing more features than dimensions) is a key driver of neural scaling laws. Using weight decay to control superposition degree in Anthropic's toy model: when superposition is weak, power-law loss scaling requires power-law feature frequencies; under strong superposition, loss generically scales inversely with dimension across broad frequency distributions due to geometric overlap of representation vectors. Confirms open LLMs operate in the strong-superposition regime.
- **Links:** https://neurips.cc/virtual/2025/awards_detail

### 2.2 Datasets & Benchmarks Track Best Paper
- **Artificial Hivemind / Infinity-Chat** — large-scale study of mode collapse in open-ended LM generation; a dataset of 2M+ user queries with a taxonomy of 6 top-level categories / 17 subcategories; reveals "Artificial Hivemind" intra-model repetition.

### 2.3 Test of Time Award
- **Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks** — Shaoqing Ren, Kaiming He, Ross Girshick, Jian Sun (Microsoft Research). Introduced the Region Proposal Network (RPN) sharing full-image convolutional features with the detection network.

### 2.4 Notable NeurIPS 2025 Papers — Agents / Reasoning / Systems

| Title | Authors | Affiliation | Key result |
|-------|---------|-------------|------------|
| Bag of Tricks for Inference-time Computation of LLM Reasoning (DB track) | (multi-institution) | — | Empirically: instruction prompts matter most; self-evaluation often fails; reward models inflate scores; best configs beat prior baselines across 8 reasoning tasks (20,000+ A100-hours). |
| MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents | Zhou Zijian et al. | NUS / SMART / MIT | RL agent maintains a compact dynamic internal state; lower memory, faster inference; **Best Paper, NeurIPS 2025 Workshop on Multi-Turn Interactions** (selected from 230 submissions). |
| Reasoning Gym: Reasoning Environments for RL with Verifiable Rewards | (multi) | — | Procedural environments for RLVR. |
| Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge | (multi) | — | Agentic-search benchmark. |
| AbstentionBench: Reasoning LLMs Fail on Unanswerable Questions | (multi) | — | LLMs fail at abstention. |
| ICPC-Eval: Probing LLM Reasoning with Competitive Programming Contests | (multi) | — | Contest-grade coding eval. |
| RewardModeling / Distributional LLM-as-a-Judge | (multi) | — | Judge reliability. |
| The Automated LLM Speedrunning Benchmark: Reproducing NanoGPT Improvements | (multi) | — | Automating LLM speedrunning. |

---

## 3. ICLR 2026 (Rio de Janeiro, Brazil — Apr 23-27, 2026)

**Stats:** 223-224 accepted oral papers (top slice). Google contributed many papers including several orals.

### 3.1 Selected Orals — Reasoning & Agents

#### 3.1.1 DECS: Overthinking Reduction with Decoupled Rewards and Curriculum Data Scheduling
- **Title (zh):** DECS：解耦奖励与课程数据调度以缓解过度思考
- **Authors:** Shuyang Jiang, Yusheng Liao, Ya Zhang, Yanfeng Wang, Yu Wang
- **Affiliation:** Shanghai Jiao Tong University; Shanghai AI Laboratory
- **Venue:** ICLR 2026 **Oral**
- **Abstract & key innovations:** Identifies two flaws in existing length rewards — (1) erroneous penalization of essential exploratory tokens, (2) inadvertent rewarding of partial redundancy. Introduces (i) a **decoupled token-level reward** that distinguishes and penalizes redundant tokens, and (ii) a **curriculum batch scheduling** strategy. Reduces reasoning tokens by **>50%** across **seven benchmarks** while maintaining or improving performance.
- **Comparison with prior methods:** Outperforms trajectory-level length-penalty baselines that cause performance degradation due to misalignment between trajectory-level rewards and token-level optimization.
- **Links:** https://www.iclr.cc/virtual/2026/events/oral · code: https://github.com/pixas/DECS

#### 3.1.2 Reducing Belief Deviation in Reinforcement Learning for Active Reasoning of LLM Agents (T³)
- **Title (zh):** 减少 LLM 智能体主动推理中强化学习的信念偏移
- **Authors:** Deyu Zou, Yongqiang Chen, Jianxiang Wang, Garry Yang, Mufei Li, Qing Da, James Cheng, Pan Li, Yu Gong
- **Affiliation:** Case Western Reserve University; Purdue University; CUHK; Amazon
- **Venue:** ICLR 2026 **Oral**
- **Abstract & key innovations:** Identifies **belief deviation** — LLM agents' internal beliefs drift from the true problem state in multi-turn active reasoning, causing uninformative/repetitive actions and compounding errors in RL trajectories. Proposes **T³**: detects excessive deviation and **truncates training trajectories** to suppress uninformative tail effects, preserving credit for informative prefixes. Across **5 challenging tasks**: gains up to **+30 points** and token cost cut by up to **34%**.
- **Links:** https://www.iclr.cc/virtual/2026/events/oral

#### 3.1.3 Reasoning with Sampling: Your Base Model is Smarter Than You Think
- **Title (zh):** 通过采样推理：你的基座模型比你以为的更聪明
- **Authors:** Aayush Karan, Yilun Du
- **Affiliation:** Harvard University (Karan); MIT (Du)
- **Venue:** ICLR 2026 **Oral**
- **Abstract & key innovations:** Inspired by MCMC for sampling from sharpened distributions, proposes a simple **iterative sampling algorithm** leveraging the base model's own likelihoods. Boosts reasoning to nearly match and even outperform RL post-training on MATH500, HumanEval, and GPQA — with **no training, curated data, or verifier** — and avoids the diversity collapse characteristic of RL post-training.
- **Comparison with prior methods:** Directly challenges the RL-posttraining necessity narrative (echoing the NeurIPS 2025 RLVR negative result).
- **Links:** https://iclr.cc/virtual/2026/oral/10009094

#### 3.1.4 Generative Universal Verifier as Multimodal Meta-Reasoner (OmniVerifier)
- **Title (zh):** 生成式通用验证器作为多模态元推理器
- **Authors:** Xinchen Zhang, Xiaoying Zhang, Youbin Wu, Yanbin Cao, Renrui Zhang, Ruihang Chu, Ling Yang, Yujiu Yang, Guang Shi
- **Affiliation:** **ByteDance Seed**; Tsinghua University
- **Venue:** ICLR 2026 **Oral**
- **Abstract & key innovations:** (1) Builds **ViVerBench**, spanning 16 categories of visual-outcome verification tasks; (2) trains **OmniVerifier-7B**, the first omni-capable generative verifier (ViVerBench +8.3); (3) proposes **OmniVerifier-TTS**, a sequential test-time scaling paradigm bridging image generation and editing. Improves T2I-ReasonBench (+3.7) and GenEval++ (+4.3), outperforming Best-of-N.
- **Links:** https://iclr.cc/virtual/2026/oral/10010787

### 3.2 Other Notable ICLR 2026 Papers

| Title | Authors (lead) | Affiliation | Topic |
|-------|----------------|-------------|-------|
| MedAgentGym: Scalable Agentic Training Environment for Code-Centric Reasoning in Biomedical Data Science | Ran Xu, Yuchen Zhuang, Yishan Zhong et al. | **Google DeepMind** | Agentic training env (Oral) |
| OpenApps: Simulating Environment Variations to Measure UI Agent Reliability | Karen Ullrich, Jingtong Su, Claudia Shi et al. | **Meta AI** | UI agent reliability (Oral) |
| AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making via Multi-Turn RL | Zhiheng Xi, Jixuan Huang, Chenyang Liao et al. | Fudan University | Open multi-turn RL framework (Oral) |
| DepthLM: Metric Depth from Vision Language Models | Zhipeng Cai, Ching-Feng Yeh, Hu Xu et al. | **Meta** | Metric depth from VLMs (Oral) |
| DTO-KD: Dynamic Trade-off Optimization for Knowledge Distillation | Zeeshan Hayder, Ali Cheraghian, Lars Petersson et al. | Google | KD (Oral) |
| RAIN-Merging: Gradient-Free Instruction Following in Large Reasoning Models | Zhehao Huang, Yuhang Liu et al. | SJTU | Null-space model merging (Oral) |
| Revela: Dense Retriever Learning via Language Modeling | (ICLR 2026) | — | Self-supervised dense retrieval (Oral) |
| Verifying Chain-of-Thought Reasoning via Its Computational Graph | Zheng Zhao, Yeskendir Koishekenov, Xianjun Yang, Naila Murray, Nicola Cancedda | Meta AI | CoT verification (Oral) |
| Actions Speak Louder than Prompts: A Large-Scale Study of LLMs for Graph Inference | Ben Finkelshtein, Silviu Cucerzan, Sujay Kumar Jauhar, Ryen White | Microsoft Research | Graph inference with LLMs (Oral) |
| Incentivizing Agentic Reasoning in LLM Judges via Tool-Integrated RL | Ran Xu, Jingjing Chen, Jiayu Ye, Yu Wu, Jun Yan, Carl Yang, Hongkun Yu | Google | Tool-integrated judge RL |
| LLMs are Greedy Agents: Effects of RL Fine-tuning | Jörg Bornschein, Janusz Marecki et al. | Google DeepMind | RL fine-tuning agent behavior |
| Universal Model Routing for LLM Inference | Wittawat Jitkrittum et al. | Google | Model routing |
| MesaNet: Sequence Modeling by Locally Optimal Test-Time Training | (Google) | Google | Sequence modeling |
| ATLAS: Transfer Scaling Laws for Multilingual Pretraining | (Google) | Google | Multilingual scaling |

---

## 4. KDD 2026 (Jeju Island, Korea — Aug 9-13, 2026)

**Stats:** 1,157 of 5,395 submissions accepted (**21%**). Four core tracks: Research, Applied Data Science (ADS), Dataset & Benchmark, AI for Science. The **Taobao/Alibaba-Mama group alone had 13+ accepted papers**; Tencent, Kuaishou, Meituan, Baidu all heavily represented.

### 4.1 Generative Recommendation & Advertising

#### 4.1.1 GR4AD: Generative Recommendation for Large-Scale Advertising
- **Title (zh):** GR4AD：面向大规模广告的生成式推荐
- **Authors:** Ben Xue, Dan Liu, Lixiang Wang, Mingjie Sun, Wang Peng, Pengfei Zhang, et al.
- **Affiliation:** **Kuaishou Technology**
- **Venue:** KDD 2026 (Applied Data Science)
- **Abstract & key innovations:** Production-oriented generative recommender co-designed across architecture, learning, and serving. (1) **UA-SID** (Unified Advertisement Semantic ID) tokenization captures complex business information; (2) **LazyAR**, a lazy autoregressive decoder relaxing layer-wise dependencies for short multi-candidate generation; (3) **VSL** (Value-Aware Supervised Learning) + **RSPO** (Ranking-Guided Softmax Preference Optimization), a ranking-aware list-wise RL algorithm; (4) **dynamic beam serving** adapting beam width to load.
- **Experimental results:** Large-scale online A/B tests: up to **+4.2% ad revenue** over the existing DLRM stack, with consistent gains from model scaling and inference-time scaling; fully deployed on Kuaishou (400M+ users).
- **Comparison with prior methods:** Extends generative-recommendation ideas (HSTU/OneRec) to advertising with ad-specific tokenization and value-aware list-wise RL.
- **Links:** https://arxiv.org/abs/2602.22732 · ACM DL 10.1145/3770855.3818424

#### 4.1.2 GPR: Towards a Generative Pre-trained One-Model Paradigm for Large-Scale Advertising Recommendation
- **Title (zh):** GPR：面向大规模广告推荐的生成式预训练单模型范式
- **Authors:** Jie Jiang, Jun Zhang, Yi Li, Yue Liu, Changping Wang, Yuan Wang, et al.
- **Affiliation:** **Tencent (China)**
- **Venue:** KDD 2026
- **Abstract & key innovations:** A generative pre-trained "one-model" paradigm unifying large-scale advertising recommendation; builds on prior Tencent efforts (LEADRE, "Scaling Transformers for Discriminative Recommendation via Generative Pretraining" KDD 2025).
- **Links:** https://doi.org/10.1145/3770855.3818425

### 4.2 CTR Prediction — Scaling Laws

#### 4.2.1 EST: Towards Efficient Scaling Laws in Click-Through Rate Prediction via Unified Modeling
- **Title (zh):** EST：通过统一建模实现 CTR 预测的高效 Scaling Law
- **Authors:** Mingyang Liu, Yong Sheng Bai, Zhangming Chan, Sishuo Chen, Xiang-Rong Sheng, Han Zhu, et al.
- **Affiliation:** **Alibaba (Taobao / Alimama)**
- **Venue:** KDD 2026
- **Abstract & key innovations:** Revisits CTR-vs-LLM distinctions (asymmetry in information density between behavioral and non-behavioral features; modality-specific priors of content-rich signals). Proposes **EST**, achieving fully unified modeling by processing all raw inputs in a single sequence **without lossy aggregation**. Modules: **Lightweight Cross-Attention (LCA)** pruning redundant self-interactions, and **Content Sparse Attention (CSA)** selecting high-signal behaviors via content similarity.
- **Experimental results:** Stable, efficient **power-law scaling**; deployed on Taobao display advertising: **+3.27% RPM** and **+1.22% CTR** over production baselines.
- **Comparison with prior methods:** Overcomes the information bottleneck of early-aggregation approaches (e.g. partial-unification models).
- **Links:** ACM DL 10.1145/3770855.3818400 · arXiv 2602.10811

#### 4.2.2 FAT: From Scaling to Structured Expressivity — Rethinking Transformers for CTR Prediction
- **Title (zh):** FAT：从 Scaling 到结构化表达力——重新思考 CTR 预测的 Transformer
- **Authors:** Bencheng Yan, Yuejie Lei, Zhiyuan Zeng, Zheye Deng, Di Wang, Kaiyi Lin, Pengjie Wang, Chuan Yu, Jian Xu, Bo Zheng
- **Affiliation:** **Alibaba (Taobao / Alimama)**
- **Venue:** KDD 2026
- **Abstract & key innovations:** Diagnoses rapidly diminishing returns of scale in CTR as a **structural misalignment**: standard Transformers assume sequential compositionality while CTR demands combinatorial reasoning over heterogeneous fields. Introduces **Field-Aware Transformer (FAT)** with field-centric parameters, shifting complexity dependence from total vocabulary size to the number of fields. A **Basis-Composed Hypernetwork** synthesizes field-specific parameters from shared bases. Grounded by a formal Rademacher-complexity scaling law.
- **Experimental results:** Up to **+4.38% AUC** offline; live production: **+2.33% CTR** and **+0.66% RPM**; FAT-Large (~0.5B params) maintains P99 latency (45→48ms) with MFU surging from 5% to 34%.
- **Comparison with prior methods:** Beats DeepCTR, FFM, DeepFM, AutoInt, DCNv2, Wukong, HSTU, HiFormer, RankMixer on Taobao and MovieLens-20M; FAT-XL (1.5B) shows no saturation.
- **Links:** https://doi.org/10.1145/3770855.3818420 · arXiv 2511.12081

#### 4.2.3 Breaking the Listwise-Shuffle Dilemma: A Streaming-Compatible Listwise Framework for Industrial CTR
- **Title (zh):** 打破 Listwise-Shuffle 困境：面向工业 CTR 的流式兼容 Listwise 框架
- **Authors:** Junlin He, Rui Tang, Liyin Hong
- **Affiliation:** **Kuaishou Technology**
- **Venue:** KDD 2026
- **Abstract & key innovations:** Identifies the **Listwise–Shuffle Dilemma**: listwise objectives require session-level aggregation, conflicting with shuffling for stable stochastic optimization. Proposes **Decoupled Listwise Learning (DLL)** reconstructing session supervision without session batching, plus **Margin-Regularized Self-Correction (MRSC)** tolerating benign fluctuations while penalizing regressions.
- **Experimental results:** +0.95 pp GAUC offline; **+2.71% CTR / +4.55% effective play-through rate (EPR)** online; deployed in a production short-video search system.
- **Links:** ACM DL 10.1145/3770855.3818327

#### 4.2.4 DAES: Distribution-Aware End-to-End Embedding for Streaming Numerical Features in CTR
- **Title (zh):** DAES：面向 CTR 流式数值特征的分布感知端到端 Embedding
- **Authors:** Jiahao Liu (Fudan), Hongji Ruan, Weimin Zhang, Ziye Tong, Derick Tang, Zhanpeng Zeng, Qinsong Zeng, Peng Zhang, Tun Lu, Ning Gu (Tencent)
- **Affiliation:** **Tencent** + Fudan University
- **Venue:** KDD 2026
- **Abstract & key innovations:** Tackles numerical feature embedding in streaming (non-i.i.d.) training via a reservoir-sampling-based distribution estimator and two field-aware distribution modulation strategies, replacing static offline binning that causes semantic drift.
- **Experimental results:** **+2.307% advertiser value** in A/B tests; deployed on a leading short-video platform with hundreds of millions of DAU.
- **Links:** https://doi.org/10.1145/3770855.3818111

#### 4.2.5 MGTA: Multi-scale Graph Tokens Alignment for CTR Prediction via PLMs
- **Title (zh):** MGTA：通过预训练语言模型的多尺度图 Token 对齐用于 CTR 预测
- **Authors:** Zhongzhen Wu, Yating Ren, Shuochen Li, Huobin Tan
- **Affiliation:** (academic)
- **Venue:** KDD 2026
- **Abstract & key innovations:** Aligns multi-scale graph tokens with pre-trained language models for CTR; relates to FLIP, ClickPrompt, MGTA's lineage.
- **Links:** https://doi.org/10.1145/3770855.3818060

### 4.3 Taobao / Alibaba-Mama KDD 2026 Highlights (13+ papers)

| Paper | Focus | Key result |
|-------|-------|------------|
| AIGQ: End-to-End Hybrid Generative Architecture for E-commerce Query Recommendation | Query rec | IL-SFT + IL-GRPO; beats Qwen-3-30B/Gemini 3 Pro/GPT-5.1; online: +10.31% transactions, +10.68% GMV, +7.42% UCTR, +3.73% 7-day retention |
| EST (see §4.2.1) | CTR scaling | +3.27% RPM / +1.22% CTR |
| FAT (see §4.2.2) | CTR scaling | +4.38% AUC / +2.33% CTR |
| RecBot: Interactive Recommendation Flow with Dual Agents | Agentic rec | PEHE 1.145→0.854; +0.86% ROI online |
| (Additional papers) | Auto-bidding, two-stage auctions, generative world models, uplift modeling, long-term causal estimation | — |

---

## 5. CVPR 2026 (Denver, USA — Jun 2026)

**Stats:** **4,089 accepted of 16,092 submissions.** Two Best Papers named; NVIDIA 59 accepted papers; MMLab@NTU 8 papers.

### 5.1 Best Papers

#### 5.1.1 Efficiently Reconstructing Dynamic Scenes One D4RT at a Time (D4RT)
- **Title (zh):** 用 D4RT 高效重建动态场景
- **Authors:** Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, Liliane Momeni, Junyu Xie, Shuyang Sun, Rahul Sukthankar, Joëlle K. Barral, Raia Hadsell, Zoubin Ghahramani, Andrew Zisserman, Junlin Zhang, Mehdi S. M. Sajjadi
- **Affiliation:** **Google DeepMind** + University College London + University of Oxford
- **Venue:** CVPR 2026 **Best Paper**
- **Abstract & key innovations:** A unified transformer that reconstructs geometry and motion of dynamic 4D scenes from video, jointly estimating depth, spatio-temporal correspondence, and full camera parameters. Allows independent/efficient probing of any 3D point in space and time; lightweight and highly scalable.
- **Comparison with prior methods:** Simplifies a traditionally computationally intensive process, enabling more efficient training and inference.
- **Links:** https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers

#### 5.1.2 Native and Compact Structured Latents for 3D Generation (O-Voxel)
- **Title (zh):** 用于 3D 生成的原生紧凑结构化 Latent（O-Voxel）
- **Authors:** Jianfeng Xiang, Xiaoxue Chen, Sicheng Xu, Ruicheng Wang, Zelong Lv, Yu Deng, Hongyuan Zhu, Yue Dong, Hao Zhao, Nicholas Jing Yuan, Jiaolong Yang
- **Affiliation:** Tsinghua University + **Microsoft Research** + USTC + Microsoft AI
- **Venue:** CVPR 2026 **Best Paper**
- **Abstract & key innovations:** Introduces **O-Voxel**, a novel 3D representation capturing complex shapes and surface attributes, significantly improving quality/realism of AI-generated 3D assets.
- **Links:** https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers

### 5.2 Highlighted / Notable CVPR 2026 Papers

| Title | Authors (lead) | Affiliation | Innovation |
|-------|----------------|-------------|------------|
| SAM 3D: 3Dfy Anything in Images | Xingyu Chen, Fu-Jen Chu, Pierre Gleize, ... Piotr Dollár, Georgia Gkioxari, Matt Feiszli, Jitendra Malik | **Meta Superintelligence Labs** | Generative 3D object reconstruction from a single image; ≥5:1 win rate in human preference tests; releases code/weights + new benchmark. |
| NitroGen: An Open Foundation Model for Generalist Gaming Agents | Loïc Magne, Anas Awadalla, Guanzhi Wang, ... Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi Fan | **NVIDIA** + Stanford + Caltech + UChicago + UT Austin | Vision-action foundation model trained on **40,000 hours** of gameplay across **>1,000 games**. |
| StreamDiT: Real-Time Streaming Text-to-Video Generation | Akio Kodaira, Tingbo Hou, Ji Hou, ... Yue Zhao | UC Berkeley + **Meta** | Moving-buffer flow matching with progressive denoising + multistep distillation; 4B model reaches real-time **512p @ 16 FPS** on one GPU; infinite streaming. |
| TV2TV: A Unified Framework for Interleaved Language and Video Generation | Xiaochuang Han, Youssef Emad, ... Luke Zettlemoyer, Emily Dinan | **Meta FAIR** | Mixture-of-Transformers jointly learning LM + video flow matching; "think in words, act in pixels"; preferred 91% over T2V on CS:GO data, +19 pts instruction following. |
| WMReward: Inference-time Physics Alignment of Video Generative Models with Latent World Models | Jianhao Yuan, Xiaofeng Zhang, ... Adriana Romero-Soriano | **FAIR, Meta Superintelligence Labs** | Re-purposes VJEPA-2 surprise score as reward; PhysicsIQ 62.0% (+6.78% SOTA); wins ICCV 2025 Perception Test PhysicsIQ challenge (62.64%, +7.42%). |
| HoloCine: Holistic Generation of Cinematic Multi-Shot Long Video Narratives | Yihao Meng, Hao Ouyang, ... Yujun Shen, Huamin Qu | — | Window Cross-Attention + Sparse Inter-Shot Self-Attention; minute-scale multi-shot narratives with character/scene memory. |
| Transition Models: Rethinking the Generative Learning Objective (TiM) | ZiDong Wang, Yiyuan Zhang, ... Wanli Ouyang, Lei Bai | Shanghai AI Lab | Exact continuous-time transition equation; 865M-param TiM beats SD3.5 (8B) and FLUX.1 (12B) across all step counts; monotonic quality with sampling budget. |
| Inference-time Physics Alignment ... (see WMReward) | — | — | — |
| Editing / MatAnyone2: Scaling Video Matting via a Learned Quality Evaluator | P. Yang, S. Zhou, K. Hao, Q. Tao | MMLab@NTU | CVPR 2026 Highlight |
| Trainable Log-linear Sparse Attention for Efficient Diffusion Transformers | Y. Zhou, Z. Xiao, T. Wei, S. Yang, X. Pan | MMLab@NTU | CVPR 2026 Highlight |
| OmniVGGT: Omni-Modality Driven Visual Geometry Grounded Transformer | H. Peng, H. Li, Y. Dai et al. | MMLab@NTU | CVPR 2026 Highlight (3D) |
| SpecTemp: Thinking with Drafts — Speculative Temporal Reasoning for Long Video | Pengfei Hu, Meng Cao, ... Bo Zheng, Xiaodan Liang | (Alibaba/fold) | Lightweight draft MLLM + powerful target MLLM; SpecTemp-80K dataset. |

---

## 6. AAAI 2026 (Singapore — Jan 2026)

**Stats:** ~23,000 papers reviewed after policy-compliance filtering (~2× AAAI-25); >75,000 unique authors; China ≈ 20,000 submissions. Largest areas: Computer Vision, ML, NLP.

### 6.1 Selected AAAI 2026 Papers

#### 6.1.1 Think-J: Learning to Think for Generative LLM-as-a-Judge
- **Title (zh):** Think-J：让生成式 LLM-as-a-Judge 学会思考
- **Authors:** Hui Huang, Yancheng He, Hongli Zhou, Rui Zhang, Wei Liu, Weixun Wang, Jiaheng Liu, Wenbo Su
- **Affiliation:** **Alibaba Group** + Nanjing University
- **Venue:** AAAI 2026
- **Abstract & key innovations:** Improves generative LLM-as-a-Judge by *learning how to think*: first curate data to develop initial judgment-thinking, then optimize judgment thinking traces via RL — with both offline (critic-model) and online (rule-based reward) variants. Surpasses generative and classifier-based LLM-Judge without extra human annotation.
- **Links:** https://ojs.aaai.org/index.php/AAAI/article/view/40377

#### 6.1.2 TIV: Thought Injection via Vectors for Efficient Reasoning in Large Reasoning Models
- **Title (zh):** TIV：通过向量注入 Thought 实现大型推理模型的高效推理
- **Authors:** Yi Cao, Weijie Shi, Wei-Jie Xu, Yucheng Shen, Yue Cui, Hanghui Guo, Shimin Di, Ziyi Liu, Jiaming Li, Alexander Zhou, Jia Zhu, Jiajie Xu
- **Affiliation:** Soochow University; HKUST; Nanjing University; **Alibaba Group**; **ByteDance**; Southeast University; HK PolyU
- **Venue:** AAAI 2026
- **Abstract & key innovations:** Compresses token-level reasoning into compact **learnable vectors** injected into post-attention hidden states rather than generating explicit thought tokens; two-stage RL calibrates then distills a vector-based policy optimizing accuracy + brevity.
- **Experimental results:** Preserves **>99% accuracy** while reducing output length by **>65%** on average (up to 80%) across three reasoning benchmarks.
- **Links:** https://ojs.aaai.org/index.php/AAAI/article/view/40264

#### 6.1.3 Agentic Reasoning Papers — Highlights

| Paper | Affiliation | Key result |
|-------|-------------|------------|
| AutoGLM: Autonomous Foundation Agents for GUIs | Zhipu AI | **55.2%** success on VAB-Lite (+18.2 over prior). |
| iMAD: Intelligent Multi-Agent Debate for Efficient and Accurate LLM Inference | Virginia Tech | Selective MAD triggering via 41 hesitation features + FocusCal loss; token usage down **up to 92%**, accuracy up **to +13.5%**. |
| DALA: Dynamic Auction-based Language Agent | Sun Yat-sen Univ. / others | Communication as scarce resource via auction; **84.32% MMLU**, **91.21% pass@1 HumanEval**, only 6.25M tokens. |
| AgentSwift: Efficient LLM Agent Design via Value-guided Hierarchical Search | (AAAI 2026) | +8.34% average across 7 benchmarks. |
| AutoTool: Efficient Tool Selection for LLM Agents | (AAAI 2026) | Tool-selection efficiency. |
| BayesAgent: Bayesian Agentic Reasoning Under Uncertainty via Verbalized PGM | (AAAI 2026) | vPGM framework; better accuracy + calibration. |
| S-DAG: Subject-Based DAG for Multi-Agent Heterogeneous Reasoning | (AAAI 2026) | GNN infers subject interdependence; outperforms task-level MoE. |
| Towards Trustworthy Multi-Turn LLM Agents via Behavioral Guidance | (AAAI 2026) | Task profiler + reasoning + generation modules. |
| Incorporating Self-Rewriting into LLM Reasoning Reinforcement | BIT + **ByteDance** | +0.6 accuracy with **−46%** reasoning length; +7.2 LLM-judge score. |
| Think-J (see §6.1.1) | Alibaba | — |

### 6.2 Amazon Science at AAAI 2026

| Paper | Area |
|-------|------|
| RECoRD: Multi-agent LLM framework for reverse engineering codebase to causal relational diagram | Computer vision / agents |
| Breaking the safety-capability tradeoff: RL with verifiable rewards maintains safety guardrails in LLMs | Optimization |
| Align to structure: Aligning LLMs with structural information | Machine learning |
| Keyword search is all you need: RAG-level performance without vector databases using agentic tool use | Robotics / RAG |
| Symbolic planning and multi-agent path finding in dense environments with unassigned agents | Conversational AI |
| PRECISE: Reducing bias of LLM evaluations using prediction-powered ranking estimation | ML |

### 6.3 Alibaba DAMO at AAAI 2026
- **Style4D-Bench: A Benchmark Suite for 4D Stylization** — Beiqi Chen, Shuai Shao, et al. (HIT / Great Bay Univ. / NU / SYSU / Alibaba).
- **EarthCrafter: Scalable 3D Earth Generation via Dual-Sparse Latent Diffusion** — Shang Liu, Chenjie Cao, et al. (Alibaba DAMO Academy Hupan Lab).

---

## 7. ACL 2026 / EMNLP 2025 (NLP)

### 7.1 EMNLP 2025 (Suzhou — Nov 2025)

**Awards:** 7 Outstanding Papers from >3,000 accepted papers.

| Paper (EN / zh) | Authors | Affiliation | Key finding |
|-----------------|---------|-------------|-------------|
| LingGym: How Far Are LLMs from Thinking Like Field Linguists? / LingGym：LLM 距离像田野语言学家一样思考还有多远 | Changbing Yang, Franklin Ma, Freda Shi, Jian Zhu | University of Waterloo / UBC | Task-oriented benchmark for meta-linguistic reasoning over 18 endangered/low-resource languages using interlinear glossed text; structured linguistic cues consistently improve reasoning. |
| Mind the Value-Action Gap: Do LLMs Act in Alignment with Their Values? / 价值-行动差距：LLM 的行为与其价值观一致吗 | Hua Shen, Nicholas Clark, Tanu Mitra | University of Washington | Measures value-action gap in LLMs. |
| DiscoSG: Discourse-Level Text Scene Graph Parsing through Iterative Graph Refinement / DiscoSG：通过迭代图精炼的篇章级文本场景图解析 | Shaoqing Lin, Chong Teng, Fei Li, Donghong Ji, Lizhen Qu, Zhuang Li | RMIT / Monash / Wuhan Univ. | Extends scene-graph parsing from sentence to document level via new dataset + iterative graph refinement. |
| Generative or Discriminative? Revisiting Text Classification in the Era of Transformers / 生成式还是判别式？Transformer 时代文本分类再审视 | Siva Rajesh Kasa et al. | — | Revisits discriminative vs generative text classification. |
| Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps / 通过遗忘推理步骤衡量 CoT 忠实性 | Martin Tutek, Fateme Hashemi Chaleshtori, Ana Marasović, Yonatan Belinkov | UKP / Technion | Unlearning-based CoT faithfulness measurement. |
| MiCRo: Mixture Modeling and Context-aware Routing for Personalized Preference Learning / MiCRo：面向个性化偏好学习的混合建模与上下文感知路由 | Jingyan Shen, Jiarui Yao, Rui Yang, Yifan Sun, Feng Luo, Rui Pan, Tong Zhang, Han Zhao | — | Mixture modeling + routing for personalized preference learning. |
| R2I-Bench: Benchmarking Reasoning-Driven Text-to-Image Generation / R2I-Bench：评测推理驱动的文生图 | Kaijie Chen, Zihao Lin, Zhiyang Xu, ... Lifu Huang | Virginia Tech | Outstanding Paper Award. |

**Notable accepted EMNLP 2025 papers:** REARANK (Reasoning Re-ranking Agent via RL — Le Zhang, Bo Wang, Xipeng Qiu, Siva Reddy, Aishwarya Agrawal), "Thinking Out Loud: Do Reasoning Models Know When They're Right?" (Qingcheng Zeng, Weihao Xuan, Leyang Cui, Rob Voigt), "Models Have Intrinsic X-Cognition, but Need a Good Lens".

### 7.2 ACL 2026 — Code Execution & Reasoning (see §11)

| Paper | Venue | Key result |
|-------|-------|------------|
| The Path Not Taken: Duality in Reasoning about Program Execution (DexBench) | ACL 2026 Long | 445 paired instances; dual-path reasoning as robust proxy for dynamic code understanding. |
| DUET: Dual Execution for Test Output Prediction with Generated Code and Pseudocode | ACL 2026 Findings | LiveCodeBench test-output prediction SOTA; **+13.6 pp Pass@1** over prior SOTA; combines direct code execution + LLM pseudocode execution via functional majority voting. |
| CoRE: A Fine-Grained Code Reasoning Benchmark Beyond Output Prediction | ACL 2026 Findings | 255 implementations, 4.1/prob; reveals Robustness Gap + Superficial Execution; GPT-5 has I=84.62 but Ws=18.96 under IO prompting. |

---

## 8. SIGIR 2026 / WWW 2026 (IR & Web)

### 8.1 SIGIR 2026 (Melbourne — Jul 20-24, 2026)

**Stats:** 234 of 1,271 submissions accepted (**18%**). Large-scale landscape survey: 668 accepted papers; theme counts — **RAG (48)**, **Generative & Sequential Recommendation (62)**, Dense/Sparse/Neural Retrieval & Embeddings (20), LLM-based Ranking & Reranking (20), Evaluation/Benchmarks/Datasets (53), Conversational & Agentic Search (19).

**Selected SIGIR 2026 papers (LLM recommendation / retrieval):**

| Paper | Authors (lead) | Affiliation | Innovation |
|-------|----------------|-------------|------------|
| ProMax: LLM-derived Profiles with Distribution Shaping | Yi Jun Zhang et al. | — | Retrieval-perspective dual distribution-reshaping using LLM profiles. |
| GFlowGR: Fine-tuning Generative Recommendation with GFlowNets | Yejing Wang, Shengyu Zhou, Jinyu Lu et al. | CityU HK + Alibaba | GFlowNet fine-tuning for generative rec. |
| ReaLM-Retrieve (from landscape survey #167) | — | — | Segmentation of reasoning into 127-token units + REINFORCE intervention policy; +5.8% F1 over IRCoT with 47% fewer retrieval calls. |
| STRIDE (landscape survey #189) | — | — | Strategy/control/execution decomposition for multi-hop QA; +5.3 EM on MuSiQue with 54-71% fewer tokens. |
| CoveR (#202) | — | — | Coverage-contrastive/distillation training; +10 pts nugget coverage. |
| NuggetIndex (#138) | — | — | Atomic facts as retrieval unit with temporal validity; +42% nugget recall, 55% lower conflict rate. |
| ItemRAG (#474) | — | — | Item-based RAG for LLM recommendation; co-purchase + semantic similarity. |
| LRAT: Learning to Retrieve from Agent Trajectories (#149) | — | — | Mines supervision from deep-research agent browsing; +28.6% success, +27.5% evidence recall. |
| Judge-R1 (#483) | — | — | GRPO-trained agentic retrieval; +14 pts statute citation recall (legal). |
| DyKnow-RAG (#559) | — | Taobao | Deployed at billions of daily requests; +10% GSB lift (e-commerce relevance search). |

### 8.2 WWW 2026 (The Web Conference 2026)

**Selected accepted papers (research & industry tracks):**

| Paper | Authors (lead) | Affiliation | Innovation |
|-------|----------------|-------------|------------|
| PLUM: Adapting Pre-trained Language Models for Industrial-scale Generative Recommendations | Ruining He, Łukasz Heldt, Lichan Hong, ... Ed Chi, Cristos Goodrow | **Google DeepMind / YouTube** | PLM adaptation for YouTube-scale generative recommendations (Industry track). |
| OneTrans: Unified Feature Interaction and Sequence Modeling | (ByteDance) | **ByteDance** | Unified feature interaction + sequence modeling (Industry track). |
| LSIG: Long Semantic IDs for Generative Recommendation | Zhao Li, FengYang Qi, et al. | Zhejiang Univ. + Taotian Group (Alibaba) | Long semantic IDs (Industry track). |
| NEZHA: Zero-sacrifice Hyperspeed Decoding for Generative Recommendations | Yejing Wang, Shengyu Zhou, et al. | CityU HK + Alibaba | Decoding architecture for generative rec (Industry). |
| AliBoostV2: CTR-Growth Balanced Boosting in Billion-Scale Rec | Qijie Shen, Yuanchen Bei, et al. | **Alibaba** | CTR-growth balanced boosting (Industry). |
| Hierarchical Semantic RL: Dynamic Action Space for RL-based Recommendations | Minmao Wang, Xingchen Liu, et al. | Fudan + **Kuaishou** | Hierarchical semantic RL (Industry). |
| DOS: Dual-Flow Orthogonal Semantic IDs for Recommendation in Meituan | Junwei Yin, Senjie Kou, et al. | **Meituan** | Orthogonal semantic IDs (Short paper). |
| DualGR: Generative Retrieval with Long/Short-Term Interests | Zhongchao Yi, Kai Feng, et al. | USTC + **Kuaishou** | Dual interest modeling (Short paper). |
| LLM Reasoning for Cold-Start Item Recommendation | Shijun Li, Yu Wang, Jin Wang, Ying Li, Joydeep Ghosh, Anne Cocos | UT Austin + Capital One + **Netflix** | LLM reasoning for cold-start (Short paper). |
| Multi-Agent Collaborative Filtering: Orchestrating Users and Items for Agentic Recommendations | Yu Xia, Sungchul Kim, Tong Yu, Ryan A. Rossi, Julian McAuley | UCSD + **Adobe Research** | Multi-agent CF. |
| GPU-accelerated Multi-relational Parallel Graph Retrieval for Web-scale Recommendations | Zhuoning Guo, Guangxing Chen, et al. | HKUST(GZ) + **Baidu** | GPU graph retrieval (Industry). |
| Large Reasoning Embedding Models: Towards Next-Generation Dense Retrieval | Jianting Tang, Dongshuai Li, et al. | USTC + (Alibaba) | Reasoning embedding models (Industry). |
| BanditLP: Large-Scale Stochastic Optimization for Personalized Recommendations | Phuc Nguyen et al. | **LinkedIn** | Bandit-based personalization (Industry). |
| Real-Time Trend Prediction via Continually-Aligned LLM Query Generation | Zijing Hui, Wenhan Lyu, et al. | **Meta Platforms** | Trend prediction via LLM query gen. |
| Retrieval Collapses When AI Pollutes the Web | Hongyeon Yu, Dongchan Kim, Young-Bum Kim | NAVER | Web-pollution impact on retrieval (Short). |
| Not All Candidates are Created Equal: Heterogeneity-Aware Re-ranking | Pengfei Tong, Siyuan Chen, et al. | **ByteDance** | Heterogeneity-aware reranking (Industry). |
| P-Aligner: Pre-Aligning LLMs via Principled Instruction Synthesis | Feifan Song, Bofei Gao, et al. | Peking Univ. + **Alibaba** | Instruction synthesis (Short). |

---

## 9. CIKM 2025 / RecSys 2025 (RecSys & Data Mining)

### 9.1 CIKM 2025 (Seoul — Nov 2025)

**Stats:** 1,984 accepted of 9,274 submissions (**21%**).

| Paper | Authors | Affiliation | Innovation |
|-------|---------|-------------|------------|
| MARM: Unlocking the Recommendation Cache Scaling-Law through Memory Augmentation and Scalable Complexity | Xiao Lv, Jiangxia Cao, Shijie Guan, ... Guorui Zhou | **Kuaishou** | Memory augmentation + scalable complexity for rec scaling law. |
| UniROM: Unifying Online Advertising Ranking as One Model | Junyan Qiu, Ze Wang, ... Xingxing Wang | **Meituan** | One-model unified online advertising ranking. |
| Twin-Flow Generative Ranking Network for Recommendation | Hao Guo, Erpeng Xue, et al. | **Meituan** + Renmin Univ. | Twin-flow generative ranking. |
| MPFormer: Adaptive Framework for Industrial Multi-Task Personalized Sequential Retriever | Sun Yijia, Huang Shanshan, ... Gai Kun, Zhou Guorui | **Kuaishou** | Multi-task sequential retriever. |
| QARM: Quantitative Alignment Multi-Modal Recommendation at Kuaishou | Xinchen Luo, Jiangxia Cao, et al. | **Kuaishou** | Item Alignment + Quantitative Code for trainable multimodal IDs; 400M users daily. |
| MTGR: Industrial-Scale Generative Recommendation Framework in Meituan | Ruidong Han, Bin Yin, et al. | **Meituan** | Industrial-scale GR. |
| UniECS: Unified Multimodal E-Commerce Search with Gated Cross-modal Fusion | Zihan Liang, Yufei Ma, et al. | **Kuaishou** | Unified multimodal e-commerce search. |
| SG-Filter: Similar Text Retrieval via Hierarchical Summarized-Semantic Index | Jiancai Ye, Jun Liu, ... Guohao Dai | SJTU + Tsinghua + **ByteDance** | Efficient similar-text retrieval. |

### 9.2 RecSys 2025 (Prague — Sep 22-26, 2025)

**Best Full Paper:** *You Don't Bring Me Flowers: Mitigating Unwanted Recommendations Through Conformal Risk Control* — Giovanni De Toni, Erasmo Purificato, Emilia Gómez, Andrea Passerini, Bruno Lepri, Cristian Consonni.
**Best Short Paper:** *Beyond Top-1: Addressing Inconsistencies in Evaluating Counterfactual Explanations for Recommender Systems* — Amir Reza Mohammadi, Andreas Peintner, Michael Müller, Eva Zangerle.

**Selected RecSys 2025 papers:**

| Paper | Authors (lead) | Affiliation | Key result |
|-------|----------------|-------------|------------|
| GRACE: Generative Recommendation via Journey-Aware Sparse Attention on CoT Tokenization | Luyi Ma, Wanjia Zhang, Kai Zhao, ... Kannan Achan | **Walmart Global Tech** | Hybrid CoT tokenization + Journey-Aware Sparse Attention; **+106.9% HR@10 / +106.7% NDCG@10** (Home), +22.1% HR@10 (Electronics); attention compute −48%. |
| GenSAR: Unifying Balanced Search and Recommendation with Generative Retrieval | Teng Shi, Jun Xu, Xiao Zhang, Xiaoxue Zang, Kai Zheng, Yang Song, Enyun Yu | Renmin Univ. + **Kuaishou** | Joint S&R identifier balancing semantic + collaborative info; unified generative retrieval. |
| R⁴ec: Reasoning, Reflection, and Refinement Framework | Hao Gu, Rui Zhong, ... Kun Gai | CASIA + **Kuaishou** | Reasoning-reflection-refinement for rec. |
| Semantic ID prefix-ngram (Meta Ads) | (Meta) | **Meta** | Improves Semantic ID: embedding stability, tail-ID modeling; integrated into Meta production Ads ranking. |
| Scaling Generative Recommendations with Context Parallelism on HSTU | Yue Dong, Han Li, Shen Li, Nikhil Patel, Xing Liu, Xiaodong Wang, Chuanhao Zhuge | **Meta** | Context parallelism with jagged-tensor support → **5.3× longer sequences**, 1.55× training throughput. |
| Multi-Granularity Distribution Modeling for Video Watch Time Prediction via Exponential-Gaussian Mixture Network | Xu Zhao, Ruibo Ma, et al. | **Kuaishou** | Watch-time prediction via EG mixture. |
| IP2: Entity-Guided Interest Probing for Personalized News Recommendation | Youlin Wu, Yuanyuan Sun, et al. | Dalian Univ. of Technology | Entity-guided interest probing. |
| A Non-Parametric Choice Model That Learns How Users Choose Between Recommended Options | Thorsten Krause, Harrie Oosterhuis | Radboud University | Non-parametric choice modeling. |

---

## 10. Cross-Cutting Theme: Code Execution Prediction & Program Reasoning

A distinct cluster of 2025-2026 work studies whether LLMs can *predict program behavior* (outputs, intermediate states) rather than just generate code. **arXiv export API was rate-limited this run**, so this cluster is assembled from ACL Anthology, arXiv abstract pages, and proceedings.

| Paper | Authors | Affiliation | Venue | Key result |
|-------|---------|-------------|-------|------------|
| DUET: Dual Execution for Test Output Prediction with Generated Code and Pseudocode | (ACL 2026 Findings) | — | ACL 2026 Findings | Combines direct code execution + LLM-based pseudocode execution via functional majority voting; **+13.6 pp Pass@1** over prior SOTA on LiveCodeBench test-output prediction; best Pass@1 on BigCodeBench-Hard, DevEval, HumanEval(+). |
| CoRE: A Fine-Grained Code Reasoning Benchmark Beyond Output Prediction | Jun Gao, Yun Peng, Qian Qiao, ... Xiaoxue Ren | Zhejiang Univ.; CUHK; CSIRO Data61; Fudan; Yale | ACL 2026 Findings | 255 implementations (4.1/problem), 4 intermediate-state probe dims (Arithmetic/Logic/State/Boundary); reveals **Robustness Gap** and **Superficial Execution** (GPT-5: output 84.62 vs process fidelity 18.96 under IO). |
| The Path Not Taken: Duality in Reasoning about Program Execution (DexBench) | Eshgin Hasanov, Md. Mahadi Hassan, Santu Karmaker, Aashish Yadavally | — | ACL 2026 Long | 445 paired instances; dual-path reasoning (predict behavior / mutate input toward objective) as discriminative proxy; reduces contamination. |
| Evaluating Exact Output and Checkpoint-State Prediction in Real Programs | (arXiv 2610.11889) | — | arXiv 2026 | 400 cases / 371 Python+C++ programs; reasoning-enabled settings beat off by **33.1-55.2 pp**; strongest setting 93.0% (short output) → 77.0% (long) → 65.5%/63.5% (state tasks). |
| SWE-Flux: Can LLMs Reason About Runtime Behavior? A Repository-Level Dynamic Benchmark | (York University Toronto) | York University | arXiv 2609.28449 | 480 execution-grounded instances / 12 Python repos; best model only **37%** accuracy; runtime dataflow hardest (6%); perturbation pipeline harvests 90% valid harder variants (GPT-5.4 100%→43%). |
| Self-Execution Simulation Improves Coding Models | (arXiv 2604.03253) | — | arXiv 2026 | SFT on natural-language execution traces + RLVR; up to **+43%** on CruxEval output prediction and **+39%** on competitive programming; best@k self-verification +2-8 pts; small simulation gap vs ground-truth execution. |
| How Robustly do LLMs Understand Execution Semantics? | Claudio Spiess, Prem Devanbu, Earl T. Barr | UC Davis / UCL | arXiv 2604.16320 | Frontier model GPT-5.2 scores 99% on CRUXEval but drops 20-24% under perturbation — significant brittleness; open reasoning models (DeepSeek-R1) more stable (38-67%). |
| RepoReasoner: Evaluating Repository-Level Code Reasoning of Long-Context LLMs | (arXiv 2607.25996) | — | arXiv 2026 | Even with oracle context, best model only **69.1% Pass@1** on Output Prediction; call-chain prediction high precision / low recall (<20% EM). |

---

## 11. Cross-Cutting Theme: LLM Agents, Memory & RLVR

| Paper | Affiliation | Venue | Innovation |
|-------|-------------|-------|------------|
| T³: Reducing Belief Deviation for Active Reasoning of LLM Agents | Case Western / Purdue / CUHK / Amazon | ICLR 2026 Oral | Trajectory truncation via belief-deviation detection; up to +30 pts, −34% tokens. |
| DECS: Overthinking Reduction | SJTU / Shanghai AI Lab | ICLR 2026 Oral | Decoupled token-level rewards + curriculum scheduling; −50% tokens. |
| OmniVerifier (Generative Universal Verifier) | ByteDance Seed / Tsinghua | ICLR 2026 Oral | Generative verifier + sequential test-time scaling. |
| OpenApps | Meta AI | ICLR 2026 Oral | UI agent reliability under environment variation. |
| MedAgentGym | Google DeepMind | ICLR 2026 Oral | Code-centric biomedical agent training env. |
| AgentGym-RL | Fudan | ICLR 2026 Oral | Multi-turn RL for long-horizon agents. |
| MEM1: Memory-Reasoning Synergy for Long-Horizon Agents | NUS / SMART / MIT | NeurIPS 2025 Workshop (Best Paper) | Compact dynamic internal state via RL. |
| Does RL Really Incentivize Reasoning Beyond the Base Model? | Tsinghua | NeurIPS 2025 Best Paper Runner-up | Negative result on RLVR capability expansion. |
| Reasoning with Sampling: Your Base Model is Smarter Than You Think | Harvard / MIT | ICLR 2026 Oral | Training-free MCMC sampling matches RL post-training. |
| iMAD: Intelligent Multi-Agent Debate | Virginia Tech | AAAI 2026 | Selective MAD; −92% tokens, +13.5% accuracy. |
| DALA: Dynamic Auction-based Language Agent | Sun Yat-sen / others | AAAI 2026 | Auction for communication bandwidth; 84.32% MMLU. |

---

## 12. Cross-Cutting Theme: Generative Models & Video

| Paper | Affiliation | Venue | Innovation |
|-------|-------------|-------|------------|
| D4RT (dynamic 4D reconstruction) | Google DeepMind + UCL + Oxford | CVPR 2026 Best Paper | Unified transformer for depth + correspondence + camera. |
| O-Voxel (structured 3D latents) | Tsinghua + MSR + USTC + Microsoft AI | CVPR 2026 Best Paper | Native compact structured latents for 3D. |
| SAM 3D | Meta Superintelligence Labs | CVPR 2026 | Single-image 3D reconstruction; ≥5:1 human preference win. |
| StreamDiT | UC Berkeley + Meta | CVPR 2026 | Real-time streaming T2V (4B @ 16 FPS). |
| TV2TV | Meta FAIR | CVPR 2026 | Interleaved language + video generation; 91% human preference. |
| WMReward | FAIR, Meta Superintelligence Labs | CVPR 2026 | Latent-world-model reward for physics alignment; PhysicsIQ SOTA. |
| Transition Models (TiM) | Shanghai AI Lab | CVPR 2026 Highlight | 865M params beats SD3.5 (8B) / FLUX.1 (12B). |
| HoloCine | — | CVPR 2026 Highlight | Multi-shot long video narrative generation. |
| NitroGen | NVIDIA + Stanford + Caltech + UChicago + UT Austin | CVPR 2026 | Generalist gaming-agent foundation model (40K hours, 1,000+ games). |

---

## 13. Cross-Cutting Theme: Sequential Modeling & CTR/Advertising Scaling

| Paper | Affiliation | Venue | Result |
|-------|-------------|-------|--------|
| EST | Alibaba | KDD 2026 | +3.27% RPM / +1.22% CTR; power-law scaling. |
| FAT | Alibaba | KDD 2026 | +4.38% AUC / +2.33% CTR / +0.66% RPM. |
| GR4AD | Kuaishou | KDD 2026 | +4.2% ad revenue; UA-SID + LazyAR + RSPO. |
| GPR | Tencent | KDD 2026 | Generative pre-trained one-model for advertising. |
| DLL + MRSC | Kuaishou | KDD 2026 | +2.71% CTR / +4.55% EPR (streaming listwise). |
| DAES | Tencent + Fudan | KDD 2026 | +2.307% advertiser value. |
| QARM | Kuaishou | CIKM 2025 | Trainable multimodal IDs; 400M users daily. |
| GRACE | Walmart Global Tech | RecSys 2025 | +106.9% HR@10 on Home domain. |
| Semantic ID prefix-ngram | Meta | RecSys 2025 | Production Ads ranking gains. |
| HSTU Context Parallelism | Meta | RecSys 2025 | 5.3× longer sequences, 1.55× throughput. |

---

## 14. Cross-Cutting Theme: Games & Strategic Reasoning

| Paper | Affiliation | Venue | Innovation |
|-------|-------------|-------|------------|
| NitroGen: Open Foundation Model for Generalist Gaming Agents | NVIDIA + Stanford + Caltech + UChicago + UT Austin | CVPR 2026 | Vision-action foundation model over 1,000+ games (40K hours). |
| TV2TV (CS:GO controlled experiments) | Meta FAIR | CVPR 2026 | "Think in words, act in pixels"; 91% preference over T2V. |
| A2Flow / AgentSwift / AutoTool | (AAAI 2026) | AAAI 2026 | Agentic workflow generation & tool selection. |
| Cross-Entropy Games for General Capabilities | — | (wiki paper page) | Curriculum for general capabilities. |
| SPIRAL: Self-Play Incentivizes Reasoning | — | (wiki paper page) | Self-play for reasoning. |

> See `wiki/synthesis/2026-10-17/game-rl-daily.md` (sibling) for the daily game-RL/world-model paper harvest.

---

## 15. Takeaways

1. **Scaling laws have migrated from LLMs into industrial recommendation/CTR.** KDD 2026 is dominated by scaling-law papers with live A/B numbers (EST +3.27% RPM, FAT +4.38% AUC, GR4AD +4.2% revenue). The narrative is "structured expressivity" (FAT) and "unified modeling without lossy aggregation" (EST), echoing the wiki's existing CTR-scaling landscape.
2. **Generative recommendation is now the default industrial paradigm** (Kuaishou OneRec/GR4AD, Tencent GPR, Meta HSTU/prefix-ngram, Google PLUM, Meituan MTGR) — consistent with the 2025 inflection noted in `wiki/synthesis`.
3. **RLVR's limits are being mapped from multiple angles.** NeurIPS 2025's Best-Paper Runner-up (RLVR does not expand reasoning beyond base models) is echoed by ICLR 2026's *Reasoning with Sampling* (training-free sampling matches RL). Meanwhile, agentic-RL works (T³, DECS, AgentGym-RL) focus on **efficiency and trajectory quality** rather than raw capability expansion.
4. **Code execution prediction is emerging as its own benchmark axis** (DUET, CoRE, DexBench, SWE-Flux, CRUXEval-extension), exposing that correct outputs often hide "superficial execution" — a reliability gap directly relevant to coding agents.
5. **Video/3D generative models** continue to consolidate: CVPR 2026 best papers are 4D reconstruction (D4RT) and structured 3D latents (O-Voxel); Meta's StreamDiT/TV2TV push real-time and interleaved generation; NVIDIA's NitroGen generalizes game agents.
6. **Top-lab concentration:** Google DeepMind (ICML 130+ papers, ICLR orals, CVPR Best Paper), Meta (CVPR, WWW PLUM, RecSys), Alibaba (KDD CTR/rec, AAAI Think-J, ICML attention), Kuaishou/Tencent/ByteDance/Meituan (KDD/CKM/RecSys industrial), NVIDIA (CVPR NitroGen), ByteDance Seed (ICLR OmniVerifier, AAAI self-rewriting).

---

## Contradictions / Open Questions

> ⚠️ **Tension (not a contradiction):** The NeurIPS 2025 RLVR negative result and ICLR 2026 *Reasoning with Sampling* both argue RL post-training does not create new reasoning ability, yet Alibaba's *Gated Attention* (NeurIPS 2025 Best Paper) and KDD/AAAI RLVR-based systems report large industrial gains. Reconciliation: RLVR improves **sampling efficiency** (pass@1) and downstream product metrics, while base-model **capability boundaries** (large-k pass) do not expand. Both are consistent; the conflict is in interpretation, not measurement.

> ⚠️ **Reporting caveat:** Some affiliations above are inferred from author blocks or lab round-ups (marked in text). Number/date discrepancies across sources were resolved in favor of official conference pages; where only secondary sources were available, results are reported as-is.

## Sources

- ICML 2026 papers & awards — https://icml.cc/virtual/2026/papers.html · https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/ · https://research.google/conferences-and-events/google-at-icml-2026/
- NeurIPS 2025 awards — https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/ · https://neurips.cc/virtual/2025/awards_detail
- ICLR 2026 orals — https://www.iclr.cc/virtual/2026/events/oral · https://openreview.net/group?id=ICLR.cc/2026/Conference
- KDD 2026 — https://kdd2026.kdd.org/papers/ · ACM DL proceedings 10.1145/3770855.*
- CVPR 2026 — https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers · https://www.nvidia.com/en-us/events/cvpr/
- AAAI 2026 — https://ojs.aaai.org/index.php/AAAI/ · https://www.amazon.science/conferences-and-events/aaai-2026
- EMNLP 2025 awards — https://2025.emnlp.org/program/awards/
- SIGIR 2026 — https://sigir2026.org/en-AU/pages/program/accepted-papers · ACM DL 10.1145/3805712
- WWW 2026 — https://www2026.thewebconf.org/accepted/short-papers.html · https://www2026.thewebconf.org/accepted/industry.html
- CIKM 2025 — https://cikm2025.org/program/accepted-papers
- RecSys 2025 — https://recsys.acm.org/recsys25/accepted-contributions/ · https://recsys.acm.org/best-papers/
- ACL/EMNLP 2025-2026 paper pages — https://aclanthology.org/2026.findings-acl.2144.pdf · https://aclanthology.org/2026.findings-acl.460.pdf · https://aclanthology.org/2026.acl-long.735/
- arXiv abstract pages — https://arxiv.org/abs/2602.22732 · https://arxiv.org/abs/2602.10811 · https://arxiv.org/abs/2609.28449 · https://arxiv.org/abs/2610.11889 · https://arxiv.org/abs/2604.03253 · https://arxiv.org/abs/2604.16320
