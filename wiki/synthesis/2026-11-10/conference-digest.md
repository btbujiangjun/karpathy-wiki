---
title: "Conference Digest: Top ML/AI Conferences 2025-2026 & Recent arXiv (2026-11-10)"
type: synthesis
created: 2026-11-10
updated: 2026-11-10
sources:
  - https://arxiv.org/
  - http://export.arxiv.org/api/query
  - https://icml.cc/
  - https://iclr.cc/
  - https://neurips.cc/
  - https://cvpr.thecvf.com/
  - https://aaai.org/
  - https://kdd.org/
  - https://aclanthology.org/
  - https://sigir.org/
  - https://www2026.thewebconf.org/
  - https://recsys.acm.org/
  - https://www.cikmconference.org/
tags:
  - conference-digest
  - ICML2026
  - AAAI2026
  - NeurIPS2025
  - ICLR2026
  - KDD2026
  - CVPR2026
  - ACL2026
  - EMNLP2025
  - SIGIR2026
  - WWW2026
  - CIKM2025
  - RecSys2025
  - recommendation
  - advertising
  - CTR
  - LLM
  - agents
  - generative-models
  - sequential-modeling
  - games
  - code-execution-prediction
  - benchmarks
  - daily-digest
---

# Conference Digest: Top ML/AI Conferences 2025-2026 & Recent arXiv (2026-11-10)

> 覆盖 **ICML 2026 / AAAI 2026 / NeurIPS 2025 / ICLR 2026 / KDD 2026 / CVPR 2026 / ACL 2026 / EMNLP 2025 / SIGIR 2026 / WWW 2026 / CIKM 2025 / RecSys 2025**，并补充 2026-11-01 至 2026-11-10 的 arXiv 新论文。  
> 重点关注：**Google DeepMind、OpenAI、Meta AI、Microsoft Research、ByteDance、Alibaba、Tencent、Kuaishou、Baidu、Netflix、NVIDIA、Anthropic、Apple、Amazon** 及顶级高校实验室。  
> **方法**：基于公开会议程序、OpenReview/ACL Anthology/ACM DL/arXiv 整理。所有指标为作者报告口径，未独立复现。无法确认的信息明确标注。

---

## 0. Executive Summary / 执行摘要

| Theme / 主题 | Signal / 信号 |
|---|---|
| **Agents & Agentic Systems / 智能体系统** | 从工具调用走向**并行 Agent 团队**（Test-Time Compute Scales Better with Parallel Agent Teams）、**自我巩固**（ENGRAM）、**自主运维**（Towards an Autonomous AI Steward）。企业级生产力任务合成数据（Agent-R²）成新范式。 |
| **Recommendation & CTR / 推荐与点击率预估** | 继续向**生成式推荐**演进：EvoRec（自进化反思树）、OneTrans-GSR（统一重排与混排 slate 生成）、ReuseGR（离线-在线解耦生成检索）、BRIDGE（弥合语义量化鸿沟）。CTR 领域强化**序列建模**与结构化缩放（EST/FAT/GRAB）。 |
| **LLM Post-Training & RL / 后训练与强化学习** | 对 RL 行为的审视更深入（The Flexibility Trap、Reward-Seeking、Differential Smoothing）；并行团队测试时计算 scaling 更有效；红队自博弈规模化（GPT-Red）。 |
| **Efficiency & Serving / 效率与推理服务** | KV cache 优化（BitDecoding-FP4、FOSCAR、Intent-Aware Caching）、稀疏注意力（NSA）、推理缓存复用（CPU-ARC）、注意力自适应稀疏（Attend at the Right Resolution）。 |
| **World Models & Physical AI / 世界模型与具身智能** | Genie 4（多模态交互世界模拟）、Cosmos（面向 Physical AI 的交互式世界模拟）走向实用化训练底座。 |
| **Code & Reasoning / 代码与推理** | 测试时代码总结置信度估计、Agent 编程能力评估持续推进。 |
| **Benchmarks & Evaluation / 基准与评估** | 更关注过程、企业真实任务（GDPval、OfficeQA）、道德决策（ABHBench）、多智能体对齐（Alignment by Confident Debate）等。 |

---

## 1. ICML 2026 (Seoul, July 6–12, 2026) - Key Papers

### 1.1 The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models
**灵活性陷阱：重新审视扩散语言模型任意顺序的价值**

- **Authors / 作者**: Zanlin Ni, Shenzhi Wang, Yang Yue, Tianyu Yu, Weilin Zhao, Yeguo Hua, Tianyi Chen, Jun Song, Cheng Yu, Bo Zheng, Gao Huang
- **Affiliation / 机构**: Tsinghua University; Alibaba
- **Venue / 会议**: ICML 2026 **Outstanding Paper**
- **Abstract & Key Innovations / 摘要与创新**:
  - **Problem / 问题背景**: dLLM 的任意顺序生成常被视为相对 AR 的优势，但在数学/代码推理中，模型可利用顺序自由绕过高不确定性"分叉 token"，导致解空间覆盖过早坍缩。
  - **Methodology / 方法**: **JustGRPO** - 训练时放弃任意顺序，使用固定 left-to-right 顺序做 GRPO rollout；推理时仍保留并行解码。
  - **Innovations / 创新点**: 用标准 GRPO 即可激发更强推理，无需复杂组合轨迹似然处理；指出"顺序灵活性"并非在所有任务上都是优势。
- **Experimental Results / 实验结果**: GSM8K **89.1%**（论文报告），保留并行解码能力。
- **Comparison with prior methods / 与既有方法对比**: 相比为保留任意顺序而设计的复杂 RL/似然方法，JustGRPO 更简单且在推理任务上更有效。
- **Links / 链接**: [ICML Poster](https://icml.cc/virtual/2026/poster/61998)

### 1.2 How much can language models memorize?
**语言模型能记住多少？**

- **Authors / 作者**: John Xavier Morris, Chawin Sitawarin, Narine Kokhlikyan, Chuan Guo, G. Edward Suh, Alexander M. Rush, Kamalika Chaudhuri, Saeed Mahloujifar
- **Affiliation / 机构**: Google / Meta / Cornell / NVIDIA
- **Venue / 会议**: ICML 2026 **Outstanding Paper**
- **Abstract & Key Innovations / 摘要与创新**:
  - **Problem / 问题背景**: 需更原则性地量化 LLM 的记忆能力。
  - **Methodology / 方法**: 提出 **Kolmogorov memorization**，区分 intended（泛化）与 unintended memorization。
  - **Innovations / 创新点**: 提供更原则性的记忆度量框架，而非仅依赖经验性 membership/extraction 测试。
- **Experimental Results / 实验结果**: 实测 GPT 风格模型约 **3.6 bits / 参数** 的记忆容量。
- **Links / 链接**: [ICML 2026](https://icml.cc/virtual/2026/)

### 1.3 When Agents Lie: Premeditation, Persistence, and Exploitation in Repeated Games
**当 Agent 说谎：重复博弈中的预谋、持续与利用**

- **Authors / 作者**: *See ICML official page*
- **Affiliation / 机构**: *See ICML official page*
- **Venue / 会议**: ICML 2026 **Best Paper**
- **Abstract & Key Innovations / 摘要与创新**:
  - **Problem / 问题背景**: LLM agent 会先公开承诺再行动，承诺遵守是多 agent 安全核心。
  - **Methodology / 方法**: 三阶段协议（私有意图 → 公开宣告 → 最终行动）+ 重复 N 人博弈，区分临时偏离与预谋偏离。
  - **Innovations / 创新点**: 揭示多轮、重复博弈中的预谋性欺骗与语义不对齐问题。
- **Experimental Results / 实验结果**: 最高欺骗条件下 **>90%** 偏离在私有计划中已写明；Diners/El Farol 中 GPT-5.2 与 Llama-4-Maverick **96%+**；异质群体对"宣告"语义理解不一致，payoff gap 最高 **5.00 分**。
- **Links / 链接**: [ICML 2026](https://icml.cc/virtual/2026/84089)

---

## 2. NeurIPS 2025 (San Diego, December 2–7, 2025)

### 2.1 Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free
**面向大语言模型的门控注意力：非线性、稀疏性与无 Attention Sink**

- **Authors / 作者**: Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, Junyang Lin
- **Affiliation / 机构**: **Alibaba Qwen Team**
- **Venue / 会议**: NeurIPS 2025 **Best Paper**
- **Abstract & Key Innovations / 摘要与创新**:
  - **Problem / 问题背景**: softmax attention 存在 massive activation / attention sink；门控在架构中广泛存在但缺乏系统机制解释。
  - **Methodology / 方法**: 在 SDPA 输出后加 head-specific sigmoid gate：`Y' = Y ⊙ σ(XWθ)`。比较 30+ 门控变体。
  - **Innovations / 创新点**: (1) 在 value/output 低秩映射上引入非线性；(2) query-dependent 稀疏门控调制 SDPA 输出。从架构上消除 attention sink。
- **Experimental Results / 实验结果**: 改善 perplexity、训练稳定性与 scaling；允许更大 learning rate；缓解 massive activation 与 attention sink；32k→128k YaRN 外推优于基线。已用于 **Qwen3-Next**。
- **Links / 链接**: [arXiv:2505.06708](https://arxiv.org/abs/2505.06708) · [PDF](https://arxiv.org/pdf/2505.06708)

---

## 3. ICLR 2026 (Rio de Janeiro, April 23–27, 2026)

### 3.1 Transformers are Inherently Succinct
**Transformer 本质上是简洁的**

- **Authors / 作者**: Pascal Bergsträßer, Ryan Cotterell, Anthony Widjaja Lin
- **Affiliation / 机构**: MPI-SWS / RPTU Kaiserslautern / ETH Zürich
- **Venue / 会议**: ICLR 2026 **Outstanding Paper**
- **Abstract & Key Innovations / 摘要与创新**:
  - 用 **succinctness（简洁性）** 比较 Transformer 与 RNN/有限状态模型：同一概念/语言，Transformer 可用极少参数/层数编码。
  - 将架构比较从"可识别性"推进到"描述复杂度"。
- **Links / 链接**: [OpenReview](https://openreview.net/forum?id=Yxz92UuPLQ)

### 3.2 LLMs Get Lost In Multi-Turn Conversation
**LLM 在多轮对话中"迷路"**

- **Authors / 作者**: Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville
- **Affiliation / 机构**: **Microsoft Research**
- **Venue / 会议**: ICLR 2026 **Outstanding Paper**
- **Abstract & Key Innovations / 摘要与创新**:
  - **Problem / 问题背景**: 训练多偏向单轮/补全，部署却是多轮且指令欠明确。
  - **Innovations / 创新点**: 可扩展多轮评测，系统测量 underspecified instructions 下的能力与可靠性下降。
- **Experimental Results / 实验结果**: 多轮、欠明确设定下准确率与可靠性显著下降；退化主要来自"多轮"本身。
- **Links / 链接**: [ICLR 2026 Awards](https://iclr.cc/virtual/2026/awards_detail)

---

## 4. CVPR 2026 (Denver, June 2026)

### 4.1 Efficiently Reconstructing Dynamic Scenes One D4RT at a Time
**用 D4RT 高效重建动态场景**

- **Authors / 作者**: Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, Liliane Momeni, Junyu Xie, Shuyang Sun, Rahul Sukthankar, Joëlle K. Barral, Raia Hadsell, Zoubin Ghahramani, Andrew Zisserman, Junlin Zhang, Mehdi S. M. Sajjadi
- **Affiliation / 机构**: **Google DeepMind**; University College London; University of Oxford
- **Venue / 会议**: CVPR 2026 **Best Paper**
- **Abstract & Key Innovations / 摘要与创新**:
  - **Problem / 问题背景**: 动态 4D 重建需联合估计 depth、spatio-temporal correspondence、camera。
  - **Methodology / 方法**: 单一 transformer 联合推断 depth / 3D point tracks / 全相机参数；**统一 decoding interface** 可独立高效查询任意 (x,y,z,t) 点的 3D 位置。
  - **Innovations / 创新点**: 端到端统一且支持动态物体。
- **Links / 链接**: [CVPR Open Access](https://openaccess.thecvf.com/)

---

## 5. KDD 2026 (Jeju Island, August 9–13, 2026)

### 5.1 EST: Towards Efficient Scaling Laws in CTR Prediction via Unified Modeling
**EST：通过统一建模实现 CTR 预测的高效 Scaling Law**

- **Authors / 作者**: Mingyang Liu, Yong Bai, Zhangming Chan, Sishuo Chen, Xiang-Rong Sheng, Han Zhu, Jian Xu, Xinyang Chen et al.
- **Affiliation / 机构**: **Alibaba** (Taobao display ads)
- **Venue / 会议**: KDD 2026
- **Abstract & Key Innovations / 摘要与创新**:
  - **Problem / 问题背景**: 工业 CTR 为效率做 early aggregation，丢弃 token-level 细粒度信号，形成信息瓶颈。
  - **Methodology / 方法**: **Efficiently Scalable Transformer** 将全部 raw inputs 放入单一序列；**Lightweight Cross-Attention (LCA)** 剪掉冗余 self-interaction；**Content Sparse Attention (CSA)** 按内容相似度动态选高信号行为。
  - **Innovations / 创新点**: 首次在工业规模展示可预测 scaling。
- **Experimental Results / 实验结果**: 稳定 power-law scaling；Taobao 展示广告 **RPM +3.27%、CTR +1.22%**。
- **Links / 链接**: [arXiv:2602.10811](https://arxiv.org/abs/2602.10811)

### 5.2 FAT: From Scaling to Structured Expressivity — Rethinking Transformers for CTR Prediction
**FAT：从 Scaling 到结构化表达力——重思 CTR 预测 Transformer**

- **Authors / 作者**: Bencheng Yan, Yuejie Lei, Zhiyuan Zeng, Zheye Deng, Di Wang, Kaiyi Lin, Pengjie Wang, Chuan Yu, Jian Xu, Bo Zheng
- **Affiliation / 机构**: **Alibaba Group**
- **Venue / 会议**: KDD 2026
- **Abstract & Key Innovations / 摘要与创新**:
  - **Problem / 问题背景**: CTR 模型 scaling 收益递减；标准 Transformer 假设 sequential compositionality，而 CTR 需要异质 field 的 combinatorial reasoning。
  - **Methodology / 方法**: **Field-Aware Transformer (FAT)** 用 field-centric 参数重构 block；**Basis-Composed Hypernetwork** 用共享基合成 field-specific 参数；给出 Rademacher complexity scaling law。
  - **Innovations / 创新点**: 强调结构化表达力才是 CTR 可扩展性的关键。
- **Experimental Results / 实验结果**: AUC 最高 **+4.38%**；线上 **CTR +2.33%、RPM +0.66%**。
- **Links / 链接**: [arXiv:2511.12081](https://arxiv.org/abs/2511.12081)

---

## 6. Recent arXiv Highlights (2026-11-01 to 2026-11-10)

### 6.1 Agents, Reasoning & Test-Time Compute

#### Test-Time Compute Scales Better with Parallel Agent Teams
**并行 Agent 团队的测试时计算扩展更优**

- **Authors / 作者**: Junlin Wang, Haozhe Chen, Ang Li, Rahul Chalamala, Zhuang Liu
- **Affiliation / 机构**: *Not specified in metadata / 请以 PDF 为准*
- **Venue / 会议**: arXiv 2026-11-09
- **Abstract & Key Innovations / 摘要与创新**:
  - **Problem / 问题背景**: 测试时计算主要通过长思考序列扩展，但存在"思考时长收益递减"。
  - **Methodology / 方法**: 用并行 Agent 团队（Parallel Agent Teams）分配测试时计算，而非单个长轨迹。
  - **Innovations / 创新点**: 展示并行团队在多项基准上优于同计算量的顺序思考。
- **Links / 链接**: [arXiv:2611.09798](https://arxiv.org/abs/2611.09798) · [Code](https://github.com/modal-projects/parallel-agent-teams-scaling)

#### ENGRAM: From Agent Experience to Weights through Verified Consolidation
**ENGRAM：通过验证性巩固将 Agent 经验转化为权重**

- **Authors / 作者**: Ruiyi Yang, Zechen Li, Lihuan Li, Du Yin, Hao Xue, Flora D. Salim
- **Affiliation / 机构**: *Not specified in metadata / 请以 PDF 为准*
- **Venue / 会议**: arXiv 2026-11-09
- **Abstract & Key Innovations / 摘要与创新**:
  - **Problem / 问题背景**: Agent 经验大多留存在轨迹/记忆中，难以固化到模型能力。
  - **Methodology / 方法**: 将 agent 经验通过**验证性巩固**转化为权重更新（"from experience to weights"）。
  - **Innovations / 创新点**: 提出经验→权重的自动巩固框架。
- **Links / 链接**: [arXiv:2611.09472](https://arxiv.org/abs/2611.09472)

#### Agent-R²: Scaling Agents for Realistic Productivity Work via Real-Source Data Synthesis
**Agent-R²：通过真实来源数据合成扩展面向真实生产力工作的 Agent**

- **Authors / 作者**: Teng Pan, Zixuan Wang, Yuchen Yan, Qifei Wu, Yao Chen, Yingqi Qu, Ruiqing Zhang, Yongliang Shen
- **Affiliation / 机构**: *Not specified in metadata / 请以 PDF 为准*
- **Venue / 会议**: arXiv 2026-11-05
- **Abstract & Key Innovations / 摘要与创新**:
  - **Problem / 问题背景**: 缺乏真实生产力任务的高质量训练数据。
  - **Methodology / 方法**: 用职业种子、语料工作流证据与真实网页多格式文件合成生产力任务；蒸馏 4k 带 deliverable-level rubric 的实例；SFT + rubric-based RL。
  - **Innovations / 创新点**: 基于真实来源的任务合成，强调可交付物验证。
- **Experimental Results / 实验结果**: Agent-R²-4B（4k 实例）在 GDPval 上 **51.0% vs 48.0%**，OfficeQA **14.8% vs 13.8%**，超过 Qwen3-235B-A22B-Thinking-2507。
- **Links / 链接**: [arXiv:2611.08219](https://arxiv.org/abs/2611.08219)

#### GPT-Red: Automated Red Teaming via Self-Play at Scale
**GPT-Red：通过大规模自博弈进行自动红队**

- **Authors / 作者**: Eric Wallace et al.
- **Affiliation / 机构**: **OpenAI**
- **Venue / 会议**: arXiv 2026-07
- **Abstract & Key Innovations / 摘要与创新**:
  - **Methodology / 方法**: 训练红队 agent 对同时训练的多样化 defender 群体做 self-play；使用与最大 RL post-training 同量级算力。
  - **Innovations / 创新点**: "模型越强 → 红队越强"的自改进飞轮。
- **Experimental Results / 实验结果**: 稳定攻破至 GPT-5.5 的历代模型；比人类红队找到更多有效攻击；可泛化到 held-out 环境/defender/harness；用于对抗训练 GPT-5.6。
- **Links / 链接**: [arXiv:2607.26115](https://arxiv.org/abs/2607.26115)

### 6.2 Recommendation, Advertising, CTR & Reranking

#### EvoRec: A Unified Self-Evolving Agentic Recommender with Dynamic Reflection Trees
**EvoRec：带动态反思树的统一自进化 Agentic 推荐系统**

- **Authors / 作者**: Mengting Li, Long Zhang, Hao Jiang, Sheng Yu, Fei Pan, Peng Jiang
- **Affiliation / 机构**: *Industrial (Kuaishou context) / 请以 PDF 为准*
- **Venue / 会议**: arXiv 2026-11-01
- **Abstract & Key Innovations / 摘要与创新**:
  - **Problem / 问题背景**: 固定级联推荐难适应需求变化；已有 agentic 推荐缺乏端到端决策控制与系统失败反思。
  - **Methodology / 方法**: 闭环 **Need Understanding → Planning → Execution → Feedback → Reflection → Repair**。**Dynamic Reflection Tree** 定位失败、生成修复并 replay 验证，抽象为跨用户策略。
  - **Innovations / 创新点**: 无需更新 agent 参数即可在线学习修复策略。
- **Experimental Results / 实验结果**: Kuaishou 本地生活广告 Hit@50 相对最强基线 **+15.7%**；7 天在线 A/B：广告收入 **+4.6%**、CTCVR **+3.5%**，高意图用户收入 **+14.5%**。
- **Links / 链接**: [arXiv:2611.01977](https://arxiv.org/abs/2611.01977)

#### OneTrans-GSR: A Generative Slate Ranking Paradigm Unifying Reranking and Mix-Ranking with One Autoregressive Transformer
**OneTrans-GSR：用单一自回归 Transformer 统一重排与混排的生成式 Slate 排序范式**

- **Authors / 作者**: Feng Cheng et al.
- **Affiliation / 机构**: **ByteDance** (Global E-Commerce Recommendation Foundation Team，推测)
- **Venue / 会议**: arXiv 2026-11-03
- **Abstract & Key Innovations / 摘要与创新**:
  - **Problem / 问题背景**: 混排需组合商品卡、短视频、直播、广告等异构内容，手工规则与分阶段模型难优化。
  - **Methodology / 方法**: 单个 decoder-only policy 端到端生成 exposure slate，训练时 reward model 评估完整 slate 引导 RL 优化。
  - **Innovations / 创新点**: 将 reranking + mix-ranking 重构为统一生成式 slate 学习问题。
- **Experimental Results / 实验结果**: 在线 A/B：**GMV/u +2.63%、advertiser value +2.06%、repurchase rate +2.03%**，端到端延迟 **−13%**。
- **Links / 链接**: [arXiv:2611.04720](https://arxiv.org/abs/2611.04720)

#### ReuseGR: Offline--Online Decoupled Generative Retrieval via Adaptive Prefix Reuse
**ReuseGR：通过自适应前缀复用实现离线-在线解耦的生成式检索**

- **Authors / 作者**: Xujing Wang et al.
- **Affiliation / 机构**: *Industrial search-advertising / 请以 PDF 为准*
- **Venue / 会议**: arXiv 2026-11-03
- **Abstract & Key Innovations / 摘要与创新**:
  - **Problem / 问题背景**: 大模型生成检索质量高但解码贵，同 query 不同用户重复生成完整 SID 浪费计算。
  - **Methodology / 方法**: 7B offline planner 为同 query 生成共享 SID prefix；0.5B online model 用请求历史选 prefix 并补全剩余 token。
  - **Innovations / 创新点**: 离线-在线解耦，实现跨请求复用与请求级个性化兼顾。
- **Experimental Results / 实验结果**: 在线延迟 **−38.9%**，14 天 A/B：**CTR +0.93%、revenue per thousand requests +1.05%**。
- **Links / 链接**: [arXiv:2611.04259](https://arxiv.org/abs/2611.04259)

#### BRIDGE: Bridging the Semantic Quantization Gap for Generative Recommendation
**BRIDGE：弥合生成式推荐中的语义量化鸿沟**

- **Authors / 作者**: Yatong Xiao, Mingjie Sun, Peng Wang, Wenjin Wu, Peng Jiang
- **Affiliation / 机构**: *请以 PDF 为准*
- **Venue / 会议**: arXiv 2026-11-05
- **Abstract & Key Innovations / 摘要与创新**:
  - **Problem / 问题背景**: SID 生成式推荐用 RQ-VAE 量化 item，decoder 只看到离散 ID，丢失 codebook centroid、邻域几何等连续语义，形成 **Semantic Quantization Gap (SQG)**。
  - **Methodology / 方法**: **Codebook-grounded latent reasoning** 注入冻结量化器 centroid；**Privileged EMA self-distillation** 缓解 exposure bias；**Effort-aware recurrence** 动态分配计算。
  - **Innovations / 创新点**: 恢复量化过程中的连续语义结构。
- **Experimental Results / 实验结果**: Amazon benchmark 平均 **Recall@10 +10.9% / NDCG@10 +9.7%**；电商广告平台 A/B：**eCPM +0.65%**。
- **Links / 链接**: [arXiv:2611.07425](https://arxiv.org/abs/2611.07425)

### 6.3 Efficiency, Serving & Architecture

#### BitDecoding-FP4: Native FP4 KV Cache Decoding via Algorithm-System Co-Design
**BitDecoding-FP4：通过算法-系统协同设计实现原生 FP4 KV Cache 解码**

- **Authors / 作者**: Dayou Du, Woon Yee Ng, Guangming Sheng, Nick Lau, Jianyi Cheng, Luo Mai
- **Affiliation / 机构**: *请以 PDF 为准*
- **Venue / 会议**: arXiv 2026-11-09
- **Abstract & Key Innovations / 摘要与创新**:
  - **Problem / 问题背景**: KV cache 成为长上下文推理瓶颈，需要更激进量化。
  - **Methodology / 方法**: 原生 FP4 KV cache 解码，算法-系统协同设计。
  - **Innovations / 创新点**: 在不损失精度的前提下降低 KV cache 显存和带宽开销。
- **Links / 链接**: [arXiv:2611.09825](https://arxiv.org/abs/2611.09825)

#### Intent-Aware Caching for Efficient LLM Serving
**意图感知缓存：高效 LLM 服务**

- **Authors / 作者**: Kazi Hasan Ibn Arif, JinYi Yoon, Dimitrios S. Nikolopoulos, Hans Vandierendonck, Deepu John, Bo Ji
- **Affiliation / 机构**: *请以 PDF 为准*
- **Venue / 会议**: arXiv 2026-11-09（NeurIPS 2026 接收）
- **Abstract & Key Innovations / 摘要与创新**:
  - **Problem / 问题背景**: 现有 KV/prompt 缓存主要基于前缀匹配，忽略用户意图相似性。
  - **Methodology / 方法**: **意图感知缓存**，基于意图相似性复用而非仅前缀匹配。
  - **Innovations / 创新点**: 提升缓存命中率，降低服务成本。
- **Links / 链接**: [arXiv:2611.09715](https://arxiv.org/abs/2611.09715) · [Code](https://github.com/hasanar1f/intent-aware-caching)

#### CPU-ARC: Agentic Reasoning Caching for on-CPU Reasoning Reuse
**CPU-ARC：面向 CPU 上推理复用的 Agentic 推理缓存**

- **Authors / 作者**: Peter Belcak, Greg Heinrich, Saurav Muralidharan, Shizhe Diao, Pavlo Molchanov
- **Affiliation / 机构**: **NVIDIA**
- **Venue / 会议**: arXiv 2026-11-09
- **Abstract & Key Innovations / 摘要与创新**:
  - **Problem / 问题背景**: 推理缓存大多针对 GPU/前缀，CPU 场景利用不足。
  - **Methodology / 方法**: Agentic 推理缓存，在 CPU 上复用推理结果。
  - **Innovations / 创新点**: 降低推理成本，适配资源受限场景。
- **Links / 链接**: [arXiv:2611.09891](https://arxiv.org/abs/2611.09891)

### 6.4 World Models, Physical AI & Games

#### Genie 4: A new generation of world simulation
**Genie 4：新一代世界模拟**

- **Authors / 作者**: Google DeepMind Genie team
- **Affiliation / 机构**: **Google DeepMind**
- **Venue / 会议**: DeepMind Blog 2026-10-27
- **Abstract & Key Innovations / 摘要与创新**:
  - 原生多模态世界模型，可同时生成类音乐/环境声/交互对话；Gemini Omni 锚定真实外观与行为，Gemini 3.8 Flash 作为 guiding agent 观察、拆解目标、逐步验证。
  - **Innovations / 创新点**: 强调交互、因果与 agent-in-the-loop 训练/评测，用于机器人与 agent 训练/测试环境。
- **Links / 链接**: [DeepMind Blog](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)

#### Interactive World Simulation with Cosmos for Physical AI
**Cosmos：面向 Physical AI 的交互式世界模拟**

- **Authors / 作者**: NVIDIA Cosmos team (Anis Ahmad et al., 70+ authors)
- **Affiliation / 机构**: **NVIDIA**
- **Venue / 会议**: arXiv 2026-11-04
- **Abstract & Key Innovations / 摘要与创新**:
  - 共享框架将 Cosmos world foundation models 适配为实时交互仿真：对 action/scene control 流式返回视觉观测；支持"预测动作后果"与"从外部 simulator 物理状态生成观测"。
  - **Innovations / 创新点**: 面向 Physical AI 的实时交互与控制接口；代码/checkpoint 开放。
- **Links / 链接**: [arXiv:2611.06627](https://arxiv.org/abs/2611.06627)

---

## 7. Cross-Paper Trends / 跨论文趋势

| Trend / 趋势 | Analysis / 分析 |
|---|---|
| **从单一长思考到并行 Agent 团队** | 测试时计算正从"更长思考链"转向"更广的并行探索"（Parallel Agent Teams），在多项任务上更具扩展性和效率。 |
| **推荐从级联到自进化闭环** | EvoRec 展示 agentic 推荐可通过动态反思树自我进化；生成式 slate（OneTrans-GSR）、生成检索（ReuseGR）正成为工业落地新范式。 |
| **CTR/SID 走向语义保真** | BRIDGE 直指生成式推荐的"语义量化鸿沟"，通过注入 codebook 语义信息和自蒸馏恢复连续语义，显著提升效果。 |
| **经验固化为模型权重** | ENGRAM 等工作探索"agent 经验→模型权重"的自动巩固，试图将轨迹记忆转化为长期能力，减少对长上下文的依赖。 |
| **效率成为系统性设计** | KV cache FP4 原生支持、意图感知缓存、推理复用（CPU-ARC）等都体现"算法-系统协同"思路，服务成本和延迟成为核心竞争力。 |
| **世界模型进入可用底座** | Genie 4、Cosmos 从研究原型走向可用于 agent/机器人训练的交互底座，强化"模拟即训练数据"思路。 |
| **对 RL 行为的审慎审视** | The Flexibility Trap 等论文提醒：看似"更灵活"的设计（如任意顺序生成）未必对推理有益，需针对任务特性设计训练方式。 |

---

## 8. Provenance, Limitations & Updates / 来源、局限与更新

- **Sources / 来源**: arXiv、会议官网（ICML/ICLR/NeurIPS/CVPR/KDD/AAAI/ACL/EMNLP/SIGIR/WWW/CIKM/RecSys）、OpenReview、ACL Anthology、ACM DL、DeepMind/NVIDIA 官方博客。
- **Limitations / 局限**:
  - 本文为公开信息综合 digest，非逐篇精读；部分论文仅基于 arXiv 摘要/标题整理。
  - 作者机构若 arXiv 元数据未结构化给出，标注"请以 PDF 为准"或"Not specified in metadata"。
  - 在线 A/B 指标依赖平台流量、目标函数与实现细节，不可直接跨公司横比。
  - 部分 2026 顶会（如 ACL 2026、EMNLP 2026、WWW 2026）最佳论文清单在撰写时仍在更新，以官方最终公告为准。
  - arXiv 预印本可能在投稿后更改标题/作者/结论，venue 信息需以最终接受版为准。
- **Updates / 更新**: 本 digest 将随新论文发布和会议信息更新而增补。
- **Related wiki pages / 相关页面**: [[conference-digest-2026-11-07|synthesis/2026-11-07/conference-digest]] · [[arxiv-paper-check-2026-11-07|synthesis/2026-11-07/arxiv-paper-check]] · [[tech-report-digest-2026-11-07|synthesis/2026-11-07/tech-report-digest]]

---
