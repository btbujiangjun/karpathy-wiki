---
title: "Conference Digest: Top ML/AI Conferences 2025–2026 (ICML/ICLR/NeurIPS/AAAI/KDD/CVPR/ACL/EMNLP/SIGIR/WWW/CIKM/RecSys)"
type: synthesis
created: 2026-10-30
updated: 2026-10-30
sources: [conference-web-searches, arxiv-abs, openreview, acm-dl]
tags: [conference-digest, ICML2026, ICLR2026, NeurIPS2025, AAAI2026, KDD2026, CVPR2026, ACL2026, EMNLP2025, SIGIR2026, WWW2026, CIKM2025, RecSys2025, recommendation, advertising, CTR, agents, agent-systems, generative-models, sequential-modeling, games, code-execution, benchmarks, daily-digest]
---

# Conference Digest: Top ML/AI Conferences 2025–2026

> 2026-10-30 版。按**会议/venue**组织，再按**研究类别**做横向汇总。覆盖 ICML 2026、ICLR 2026、NeurIPS 2025、AAAI 2026、CVPR 2026、KDD 2026、SIGIR 2026、WWW 2026、ACL 2026、EMNLP 2025、CIKM 2025、RecSys 2025，以及 agent systems / games / code execution / generative models / sequential modeling / benchmarks 六条主线。
>
> **信息口径**：以会议官网 awards/program、ACM DL / OpenReview / ACL Anthology 和 arXiv abs 为主；厂商自报的线上 A/B 指标单独标注为「作者自报、未独立复现」。部分 2026 会议论文的 arXiv 版本尚未公开，此时保留会议入口。

---

## 0. 本期速览

| # | 论文 | Venue | 机构 | 一句话贡献 |
|---|------|-------|------|-----------|
| 1 | Gated Attention for LLMs | NeurIPS 2025 Best | Alibaba Qwen + MIT/Stanford 等 | SDPA 后加 head-wise sigmoid gate，30 种变体/3.5T tokens 系统验证，缓解 attention sink |
| 2 | Does RL Really Incentivize Reasoning? | NeurIPS 2025 Best | Tsinghua / SJTU | RLVR 只提升 pass@1，增大采样数后被 base model 反超；蒸馏才带来新推理模式 |
| 3 | Transformers are Inherently Succinct | ICLR 2026 Outstanding | RPTU / MPI-SWS / ETH | 从「概念表示简洁性」解释 Transformer 相对 RNN 的表达优势 |
| 4 | LLMs Get Lost In Multi-Turn Conversation | ICLR 2026 Outstanding | Microsoft Research 等 | 多轮、欠约束指令下 LLM 能力与可靠性显著下降 |
| 5 | Autobidding Auctions with LLM-Powered Creatives | ICML 2026 | RUC / Tsinghua | 把 LLM 创意生成成本与质量分纳入 Stackelberg auto-bidding 拍卖 |
| 6 | Principled Synthetic Data → First Scaling Laws for LLM4Rec | ICML 2026 | Meta | 用分层合成数据课程首次给出推荐 LLM 的 scaling law |
| 7 | ReconVLA | AAAI 2026 Outstanding | HKUST(GZ) / Westlake / ZJU | 以「重建 gaze 区域」做隐式 visual grounding 的 VLA |
| 8 | LLM2CLIP | AAAI 2026 Outstanding | Tongji / Microsoft / Macquarie | 用 LLM 替换 CLIP 文本塔，caption-to-caption 对比微调，训练快约 4× |
| 9 | D4RT | CVPR 2026 Best | Google DeepMind / UCL / Oxford | 单一 transformer 从视频重建动态 4D 几何、对应关系与相机参数 |
| 10 | NitroGen | CVPR 2026 Honorable Mention | NVIDIA / Stanford / Caltech 等 | 40,000 小时、1,000+ 游戏的 vision-action 通用游戏 agent 基础模型 |
| 11 | MixFormer | KDD 2026 | ByteDance | 稠密特征与长序列协同 scaling 的工业推荐 backbone |
| 12 | CTR-Sink | KDD 2026 | Ant Group / CASIA / HKU | 为行为序列插入 behavior-level attention sink，修复语义碎片化 |
| 13 | SIGMA | SIGIR 2026 | AliExpress / Alibaba | 语义 grounding + 混合 item tokenization 的多任务生成式推荐 |
| 14 | GFlowGR | SIGIR 2026 | CityU / Alibaba | 用 GFlowNet 做 set-generation 微调，淘宝搜索广告年收入 +0.4% |
| 15 | DARA | WWW 2026 | Alibaba 等 | RL 微调 LLM 做 few-shot 预算分配（AIGB） |
| 16 | Reconsidering GAE in Link Prediction | CIKM 2025 Best | PKU | 调好的 GAE 即可匹配复杂 GNN，提醒 baseline 过时问题 |
| 17 | You Don't Bring Me Flowers | RecSys 2025 Best | Trento / FBK / JRC | 用 conformal risk control + 二元反馈可证地限制不想要的推荐 |
| 18 | Infini-gram mini | EMNLP 2025 Best | UW / AI2 | FM-Index 实现互联网规模精确 n-gram 检索 |
| 19 | DUET | ACL 2026 Findings | (见正文) | 代码执行 + 伪代码执行双路投票，LiveCodeBench Pass@1 +13.6pp |
| 20 | SWE-Flux | arXiv 2026 | York University | 仓库级 runtime reasoning benchmark，最强模型仅 37.71% |

---

## 1. NeurIPS 2025（San Diego + Mexico City，2025-12-02 ~ 12-07）

**规模**：约 21,575 投稿 → 5,200+ 接收（约 24.5%）。官方共颁出 4 篇 Best Paper + 3 篇 Runner-up。

### 1.1 Best Paper — Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free

- **中文标题**：面向大语言模型的门控注意力：非线性、稀疏性与无 Attention Sink
- **作者**：Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, Junyang Lin
- **机构**：Alibaba Qwen 团队，联合 MIT / Stanford / Edinburgh / Tsinghua 等
- **Venue**：NeurIPS 2025 Best Paper
- **摘要与创新**：系统比较 30 种 gating-augmented softmax attention 变体，在 15B MoE 与 1.7B dense 模型、3.5T token 上训练。核心结论：在 SDPA 之后加一个 **head-specific sigmoid gate** 稳定提升效果，同时改善训练稳定性、允许更大 learning rate、改善 scaling。作者把收益归因于两点：(1) 在 softmax attention 的低秩映射上引入非线性；(2) query-dependent 的稀疏 gate 调制 SDPA 输出。该机制还缓解 massive activation / attention sink，并改善 long-context 外推。
- **对比 prior**：此前 gating 多见于 LSTM、Highway、SSM、linear attention，softmax attention 内的 gating 缺少系统研究；本文给出统一对照，并把最优形式落到 Qwen3-Next。
- **链接**：[arXiv 2505.06708](https://arxiv.org/abs/2505.06708) · [代码](https://github.com/qiuzh20/gated_attention)

### 1.2 Best Paper — 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities

- **中文标题**：1000 层网络用于自监督强化学习：加深网络可解锁新的目标到达能力
- **作者**：Kevin Wang, Ishaan Javali, Michał Bortkiewicz, Tomasz Trzciński, Benjamin Eysenbach
- **机构**：Princeton / Warsaw University of Technology / IDEAS NCBR
- **摘要与创新**：RL 网络长期停留在 2–5 层。本文在无奖励、无示范的 goal-conditioned 设定下，把深度推到 **1024 层**，在 locomotion 与 manipulation 上把 contrastive RL 成功率提升 **2–50×**，并观察到定性上不同的行为。说明 depth scaling 在 RL 中同样是一等公民。
- **对比 prior**：主流 RL 论文依赖浅层 MLP + 大量环境交互；本文把「深度」而非「宽度/数据」作为主要 scaling 轴。
- **链接**：[arXiv 2503.14858](https://arxiv.org/abs/2503.14858)

### 1.3 Best Paper — Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training

- **中文标题**：扩散模型为何不记忆：训练中的隐式动力学正则化
- **作者**：Tony Bonnaire, Raphaël Urfin, Giulio Biroli, Marc Mézard
- **机构**：ENS / PSL / CNRS（法国）
- **摘要与创新**：识别出两个时间尺度：早期的「开始生成高质量样本」与后期的「开始记忆训练集」。记忆出现时间随训练集规模线性增长，而生成质量达标时间基本不变，因此存在一个随数据量扩张的「泛化窗口」；只有当记忆时间超过模型相关阈值，过拟合才会在无限训练时消失。
- **对比 prior**：把扩散模型的 memorization 从静态容量问题改写为训练动力学问题，解释了经验上「训练久反而不崩」的现象。
- **链接**：[arXiv 2505.17638](https://arxiv.org/abs/2505.17638)

### 1.4 Best Paper (Datasets & Benchmarks) — Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)

- **中文标题**：人工蜂巢心智：语言模型在开放式生成中的同质化
- **作者**：Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Yejin Choi
- **机构**：University of Washington / CMU / Stanford / Allen AI
- **摘要与创新**：发布 **Infinity-Chat**：26K 条真实开放式 query（无唯一答案），6 大类 / 17 子类 taxonomy，附 31,250 条人工标注（每例 25 人）。发现两类 mode collapse：(1) intra-model repetition；(2) inter-model homogeneity。SOTA LM、reward model、LLM judge 在「个体偏好分歧大」的样本上校准更差。
- **对比 prior**：以往多样性评测局限于随机数/名字生成或单模型重复采样；本文首次给出互联网规模、多模型、多人标注的开放式多样性基准。
- **链接**：[arXiv 2510.22954](https://arxiv.org/abs/2510.22954) · [数据集](https://huggingface.co/datasets/liweijiang/infinite-chats-taxonomy)

### 1.5 Runner-ups

| 论文 | 作者/机构 | 核心结论 | 链接 |
|------|----------|---------|------|
| Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? | Yang Yue 等，Tsinghua / SJTU | RLVR 在小采样预算下涨点，但大 k 时 base model 反超；蒸馏才引入新推理模式 | [arXiv 2504.13837](https://arxiv.org/abs/2504.13837) |
| Optimal Mistake Bounds for Transductive Online Learning | Chase, Hanneke, Moran, Shafer；Kent State / Purdue / Technion | 解决 30 年开放问题：transductive mistake bound 为 Θ(√Littlestone)，相对标准 online learning 指数级优势 | [OpenReview](https://openreview.net/forum?id=EoebmBe9fG) |
| Superposition Yields Robust Neural Scaling | Yizhou Liu, Ziming Liu, Jeff Gore；MIT | 表示叠加（superposition）是 neural scaling law 的机制解释；强叠加区 loss ∝ 模型规模 | [OpenReview](https://openreview.net/forum?id=knPz7gtjPW) |

**Test of Time**：Faster R-CNN（Ren, He, Girshick, Sun, 2015）。

---

## 2. ICLR 2026（Rio de Janeiro，2026-04-23 ~ 04-27）

**规模**：19,525 投稿 → 5,355 接收（27.4%）。官方 Outstanding Paper 2 篇 + Honorable Mention 1 篇。

### 2.1 Outstanding — Transformers are Inherently Succinct

- **中文标题**：Transformer 本质上是简洁的
- **作者**：Pascal Bergsträßer, Ryan Cotterell, Anthony Widjaja Lin
- **机构**：RPTU Kaiserslautern-Landau / MPI-SWS / ETH Zürich
- **摘要与创新**：从「表达同一概念所需的描述长度」切入，证明 Transformer 相对 RNN 等序列模型具有本质 succinctness：某些函数 Transformer 可紧凑表示，而其他架构需要指数级更多参数。为「为什么 Transformer 有效」提供了与 expressivity / parallelism 不同的理论视角。
- **对比 prior**：以往理论多讨论 Transformer 的可识别语言类或并行性；本文把比较轴换成表示简洁性（succinctness）。
- **链接**：[OpenReview Yxz92UuPLQ](https://openreview.net/forum?id=Yxz92UuPLQ)

### 2.2 Outstanding — LLMs Get Lost In Multi-Turn Conversation

- **中文标题**：LLM 在多轮对话中迷失
- **作者**：Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville
- **机构**：Microsoft Research
- **摘要与创新**：训练数据以单轮/文本补全为主，部署却天然多轮。作者设计可扩展的多轮评测方法，在「指令欠约束 + 多轮」条件下测得 LLM 能力与可靠性显著下降，并给出失败模式诊断。委员会特别肯定了实验设计与现实相关性。
- **对比 prior**：此前多轮评测多为小规模人工集；本文提供可规模化、可复现的诊断协议。
- **链接**：[arXiv 2505.06120](https://arxiv.org/abs/2505.06120)

### 2.3 Honorable Mention — The Polar Express: Optimal Matrix Sign Methods and their Application to the Muon Algorithm

- **中文标题**：极地特快：最优矩阵符号方法及其在 Muon 中的应用
- **作者**：Noah Amsel, David Persson, Christopher Musco, Robert M. Gower
- **机构**：NYU / Stanford 等
- **创新**：用逼近论为 polar decomposition 设计最优多项式逼近，面向 GPU 与低精度算术；为 Muon optimizer 提供更原理化的矩阵符号迭代。

### 2.4 其他值得关注

- **Code World Models for General Game Playing**（Poster）：Wolfgang Lehrach, Daniel Hennes, Miguel Lazaro-Gredilla, Xinghua Lou, Carter Wendelken（Google DeepMind）。不让 LLM 直接出招，而是把自然语言规则翻译成可执行 Python world model（状态转移/合法动作/终止判定）+ MCTS；在 10 个游戏（5 完全信息、5 不完全信息）中 9 个 match/超过 Gemini 2.5 Pro。[OpenReview](https://openreview.net/forum?id=1UoB7IWiku)
- **Mamba-3**：继续以 selective SSM 挑战 Transformer 的 long-range 序列建模效率。
- **MemAgent**：多轮 RL 的 memory agent，重塑 long-context LLM。
- **SPIRAL**：零和游戏 self-play 激励多轮推理。

---

## 3. ICML 2026（Seoul，2026-07-06 ~ 07-12）

**规模**：23,918 投稿 → 6,352 接收（26.6%）→ 536 spotlight → 168 oral。

### 3.1 广告拍卖与机制设计

#### 3.1.1 Autobidding Auctions with LLM-Powered Creatives

- **中文标题**：LLM 创意驱动的自动出价拍卖
- **作者/机构**：中国人民大学 / 清华大学
- **Venue**：ICML 2026 Poster
- **摘要与创新**：把 LLM 创意增强纳入 auto-bidding 拍卖。平台是 Stackelberg leader，广告主 autobidder 是预算约束下的 follower；模型显式计入 LLM 推理成本、素材质量分变化与竞价响应。核心问题从「pCTR/pCVR 多准」升级为「平台是否值得为某广告实时调用 LLM 生成素材」。
- **对比 prior**：传统 auto-bidding 把创意视为外生；GenAI 创意工具与拍卖机制分开建模。本文把生成成本、质量分、预算消耗与延迟放进同一机制。
- **链接**：[ICML poster 65017](https://icml.cc/virtual/2026/poster/65017)

#### 3.1.2 Model Monotonicity in Autobidding Auctions: When Do Better Predictions Lead to Better Outcomes?

- **中文标题**：自动出价拍卖中的模型单调性：更好的预测何时带来更好的结果？
- **机构**：Uber
- **创新**：用 cluster refinement 定义「模型改进」，分析不同 auction format 与 autobidder 行为下 ECM / 收入 / liquid welfare 是否单调。结论：提升预估 AUC 不等于拍卖目标自动改善，离线模型评估必须与机制指标联动。
- **链接**：[ICML poster 60993](https://icml.cc/virtual/2026/poster/60993)

#### 3.1.3 Risk-Averse and Optimistic Advertiser Incentive Compatibility in Auto-bidding

- **中文标题**：自动出价中的风险厌恶与乐观广告主激励兼容
- **机构**：Google
- **创新**：既有 AIC 要求「真实报告的最坏结果不差于任意偏离的最好结果」，过严。本文引入 risk-averse / optimistic 视角处理多均衡下的策略性报告，说明平台暴露的约束输入会改变可报告空间。
- **链接**：[arXiv 2508.16823](https://arxiv.org/abs/2508.16823)

#### 3.1.4 Incentivized Exploration with Stochastic Covariates: A Two-Stage Mechanism Design for Recommender System

- **中文标题**：随机协变量下的激励探索：推荐系统的两阶段机制设计
- **机构**：UCLA / Meta
- **创新**：用户协变量在线随机到达，平台既要探索新品，又要让自利用户愿意接受推荐。延续 Bayesian Incentive Compatibility，但利用线性结构设计两阶段机制，在激励约束下争取次线性 regret。
- **链接**：[ICML poster 64632](https://icml.cc/virtual/2026/poster/64632)

### 3.2 生成式推荐与 LLM4Rec

#### 3.2.1 Principled Synthetic Data Enables the First Scaling Laws for LLMs in Recommendation

- **中文标题**：有原则的合成数据首次给出推荐 LLM 的 Scaling Law
- **机构**：Meta
- **摘要与创新**：把 LLM4Rec 难以 scaling 归因于原始交互数据的噪声、偏差与不完整，提出分层 synthetic data curriculum，并给出模型规模 / 数据规模 / 任务质量之间的稳定 scaling law。工程含义：继续堆日志不一定划算，清洗与合成课程可能更可预测。
- **对比 prior**：此前推荐 scaling law 多针对 DLRM/HSTU 等判别式架构；本文首次把 LLM4Rec 纳入可预测扩展框架。
- **链接**：[arXiv 2602.07298](https://arxiv.org/abs/2602.07298)

#### 3.2.2 Can Recommender Systems Teach Themselves? A Recursive Self-Improving Framework with Fidelity Control (RSIR)

- **中文标题**：推荐系统能否自我教学？带保真度控制的递归自改进框架
- **作者/机构**：中国科学技术大学 / 华为
- **创新**：闭环自举：当前模型生成可能的用户交互序列 → fidelity control 过滤与用户偏好似然流形一致的样本 → 训练后继模型。理论分析表明它像数据驱动的隐式正则，平滑优化地形。风险是过滤不强时会把偏差放大成 self-consuming loop。
- **链接**：[arXiv 2602.15659](https://arxiv.org/abs/2602.15659)

#### 3.2.3 Sparse by Design: Relevance-Driven Scaling for Recommender Systems

- **中文标题**：按设计稀疏：推荐系统的相关性驱动 Scaling
- **机构**：Meta
- **创新**：指出把 Sparse MoE 直接搬到推荐并不自然：token-level routing 与 user-item relevance prediction 不匹配，推荐相关性来自分布式、多阶段交互。提出 relevance-driven scaling，让稀疏计算围绕相关性信号设计，而不是照搬 LLM 的 token routing。
- **链接**：[ICML poster 66202](https://icml.cc/virtual/2026/poster/66202)

#### 3.2.4 Mitigating Reward Hacking in LLM-based Recommendation: A Preference Optimization Approach

- **中文标题**：缓解 LLM 推荐中的 Reward Hacking：偏好优化路径
- **机构**：中国科学技术大学
- **创新**：从梯度角度定义 ε-insensitive region，说明 pairwise update 可能无法改变正样本与未采样负样本的排序，导致训练 loss 降但真实排序不涨。给出 Bradley-Terry 框架下的诊断，并强调必须监控全候选排序与在线目标。
- **链接**：[ICML poster 66384](https://icml.cc/virtual/2026/poster/66384)

#### 3.2.5 Hyperbolic RQ-VAE enhanced Generative Recommendation with Differential-Length Codebook Strategy (HG-Rec)

- **中文标题**：双曲 RQ-VAE 与可变长码本的生成式推荐
- **机构**：南京大学 / 南京邮电大学
- **创新**：把 RQ-VAE 放进双曲空间，显式建模 codebook 层级关系；利用双曲空间指数体积增长设计 differential-length / pyramidal codebook，压缩码本并提升利用率。重点看可变码本长度是否比固定等宽更适配树状 item 目录。
- **链接**：[ICML poster 65614](https://icml.cc/virtual/2026/poster/65614)

#### 3.2.6 VENOMREC: Cross-Modal Interactive Poisoning for Targeted Promotion in Multimodal LLM Recommender Systems

- **中文标题**：多模态 LLM 推荐中的跨模态交互投毒与定向推广
- **机构**：NTU / 北航 / 阿里
- **创新**：跨模态共识能缓解单模态投毒，但同步多模态投毒会沿稳定语义方向操控融合表示。提出 Exposure Alignment 找高曝光区域，再做 Cross-modal Interactive Perturbation 实现目标推广。
- **链接**：[arXiv 2602.06409](https://arxiv.org/abs/2602.06409)

#### 3.2.7 HVAE: Hyperbolic Variational Autoencoder For Flexible Knowledge Transfer Across Multiple Domains

- **中文标题**：面向多域灵活知识迁移的双曲 VAE
- **机构**：阿里 / 蚂蚁 / 中国海洋大学
- **创新**：真实 user-item 交互呈幂律与层级结构，欧氏 embedding 难以低失真表示。用双曲 VAE 解缠 domain-invariant preference 与 domain-specific interest。
- **链接**：[ICML poster 61457](https://icml.cc/virtual/2026/poster/61457)

### 3.3 可靠推荐、安全与可控性

| 论文 | 机构 | 核心思路 | 入口 |
|------|------|---------|------|
| CARE: Adaptive Calibration for Reliable Recommendations | UTS | 包裹任意 backbone，输出可变大小推荐集合，交互流上给有限样本性能保证 | [62132](https://icml.cc/virtual/2026/poster/62132) |
| CORAL: Uncertainty-Aware Regulation of Exposure Concentration | UTS | 把曝光调控建成带约束序列决策，用 UCB 风险界控制 category saturation | [63919](https://icml.cc/virtual/2026/poster/63919) |
| Obliviate: Efficient Unlearning in Recommender Systems | Sony Research India / IIT Roorkee | 两阶段 unlearning，避免全量重训，兼顾完整性/可扩展性/效用 | [64974](https://icml.cc/virtual/2026/poster/64974) |
| CRAMER: Control via Request-Aware Masking for Editing Recommenders | RUC / Dalhousie | 用 request-aware masking 让序列推荐即时响应用户自然语言请求，不重训 | [62968](https://icml.cc/virtual/2026/poster/62968) |
| Cold-Start Personalization via Training-Free Priors from Structured World Models (PEP) | UW / Meta FAIR / Ai2 | 从结构化 world model 取跨人群偏好先验，减少冷启动提问与探索 | [arXiv 2602.15012](https://arxiv.org/abs/2602.15012) |
| ProRL: Effective RL for Proactive Recommendation | Fudan | rectified policy gradient 修正长度依赖偏差与 path-level 高方差 | [61903](https://icml.cc/virtual/2026/poster/61903) |

### 3.4 图推荐与 Agent 推荐

- **CCLRec**（中北大学/哈工大/Penn State）：consensus-driven contrastive learning 让 GNN 结构信号与 LLM 语义信号形成共识监督。[65594](https://icml.cc/virtual/2026/poster/65594)
- **GCIB**（天津大学/安徽大学）：Graph Contrastive Information Bottleneck，对辅助行为图做结构剪枝 + 跨行为对比。[62097](https://icml.cc/virtual/2026/poster/62097)
- **Negative Sampling From the Ground Up**（Cornell/Meta）：从手工 negative distribution 转向逼近潜在真实负分布。[61482](https://icml.cc/virtual/2026/poster/61482)
- **AgentSelect**（UTS/Rutgers/阿里）：把「选哪个 LLM agent 配置」建成 query-to-agent recommendation，候选包含 backbone + toolkit。[arXiv 2603.03761](https://arxiv.org/abs/2603.03761)

### 3.5 ICML 2026 奖项（补充）

- **Outstanding Paper**：The Flexibility Trap: Rethinking Arbitrary Order in Diffusion Language Models。
- **Outstanding Paper**：High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions（δ-error 采样做到 polylog(1/δ) 步）。
- **Outstanding Position Paper**：The Alignment Community is Unintentionally Building a Censor's Toolkit。
- **Test of Time**：Asynchronous Methods for Deep Reinforcement Learning (A3C)，Google DeepMind。

---

## 4. AAAI 2026（Singapore，2026-01-20 ~ 01-27）

**规模**：23,680 投稿 → 4,167 接收（17.6%）。5 篇 Outstanding + 2 篇 AI for Social Impact。

### 4.1 Outstanding — ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver

- **中文标题**：重建式视觉-语言-动作模型：让机器人「看见」该看的地方
- **作者**：Wenxuan Song, Ziyang Zhou, Han Zhao, Jiayi Chen, Pengxiang Ding, Haodong Yan, Yuxin Huang, Feilong Tang, Donglin Wang, Haoang Li
- **机构**：香港科技大学（广州）/ 西湖大学 / 浙江大学 / Monash University
- **摘要与创新**：实证发现现有 VLA 的视觉注意力分散，无法稳定落到目标区域。ReconVLA 用 diffusion transformer 在模型视觉输出条件下**重建 gaze 区域**，以隐式 grounding 迫使模型学习细粒度表示并正确分配注意力。构建 >100K 轨迹、2M 样本的预训练数据，sim + real 均验证精确操作与泛化。
- **对比 prior**：显式 grounding 依赖额外检测/分割标注；本文把 grounding 变成重建自监督信号。
- **链接**：[arXiv 2508.10333](https://arxiv.org/abs/2508.10333) · [项目页](https://zionchow.github.io/ReconVLA/)

### 4.2 Outstanding — LLM2CLIP: Powerful Language Model Unlocks Richer Cross-Modality Representation

- **中文标题**：LLM2CLIP：用强语言模型解锁更丰富的跨模态表示
- **作者**：Weiquan Huang, Aoqi Wu, Yifan Yang, Xufang Luo, Yuqing Yang, Usman Naseem, Chunyu Wang, Qi Dai, Xiyang Dai, Dongdong Chen, Chong Luo, Lili Qiu, Liang Hu
- **机构**：同济大学 / Microsoft / Macquarie University
- **摘要与创新**：CLIP 的文本塔容量限制了长而复杂 caption 的理解。LLM2CLIP 用预训练 LLM 替换/增强文本编码器，并用 **caption-to-caption contrastive fine-tuning** 解决 LLM 自回归输出判别性不足的问题；相比 LoRA 类方法训练快约 4×，在 zero-shot 多模态检索、跨语言检索、MLLM 预训练上超过 CLIP / EVA02 / SigLIP2。
- **链接**：[arXiv 2411.04997](https://arxiv.org/abs/2411.04997) · [项目页](https://microsoft.github.io/LLM2CLIP/)

### 4.3 其他 Outstanding

| 论文 | 机构 | 贡献 | 链接 |
|------|------|------|------|
| Causal Structure Learning for Dynamical Systems with Theoretical Score Analysis (CaDyT) | Bosch AI Center / TU Darmstadt / IKIM | 基于 Difference-based causal models + 精确 GP 推断，处理不规则采样连续时间因果发现 | [arXiv 2512.14361](https://arxiv.org/abs/2512.14361) |
| Model Change for Description Logic Concepts | University of Oslo / Cardiff | 形式化 DL 概念的 eviction/reception/revision，证明 revision 不可约化为二者组合 | 暂无公开链接 |
| High-Pass Matters: Sheaflet-Based Hypergraph NN | ZJNU / CityU / NTU / Cambridge | 从 high-pass 滤波理论设计 sheaflet hypergraph 网络 | 暂无公开链接 |

---

## 5. CVPR 2026（Denver，2026-06-03 ~ 06-07）

**规模**：16,092 投稿 → 4,089 接收。

### 5.1 Best Paper — Efficiently Reconstructing Dynamic Scenes One D4RT at a Time

- **中文标题**：一次一个 D4RT：高效重建动态场景
- **作者**：Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, Liliane Momeni, Junyu Xie, Shuyang Sun, Rahul Sukthankar, Joëlle K. Barral, Raia Hadsell, Zoubin Ghahramani, Andrew Zisserman, Junlin Zhang, Mehdi S. M. Sajjadi
- **机构**：Google DeepMind / UCL / University of Oxford
- **摘要与创新**：单一 transformer 从视频重建动态 4D 场景的几何与运动，同时估计 depth、spatio-temporal correspondence 与完整相机参数；可在任意时空点独立 probe 3D 位置。相比传统多阶段、计算密集的 4D reconstruction pipeline，训练与推理都更轻、更可扩展。
- **对比 prior**：把 depth / correspondence / camera 从分开的子问题统一进一个 backbone，避免级联误差。
- **链接**：[CVPR 2026 Best Papers](https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers)

### 5.2 Best Student Paper — Native and Compact Structured Latents for 3D Generation (O-Voxel)

- **中文标题**：面向 3D 生成的原生紧凑结构化 latent
- **作者**：Jianfeng Xiang, Xiaoxue Chen, Sicheng Xu, Ruicheng Wang, Zelong Lv, Yu Deng, Hongyuan Zhu, Yue Dong, Hao Zhao, Nicholas Jing Yuan, Jiaolong Yang
- **机构**：清华大学 / Microsoft Research / USTC / Microsoft AI
- **摘要与创新**：提出 **O-Voxel** 表示，能同时精确刻画复杂形状与表面属性；几何与生成质量显著超过现有 3D 生成模型。
- **链接**：[CVPR 2026 Best Papers](https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers)

### 5.3 Honorable Mention — NitroGen: An Open Foundation Model for Generalist Gaming Agents

- **中文标题**：NitroGen：面向通用游戏智能体的开放基础模型
- **作者**：Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi Fan
- **机构**：NVIDIA / Stanford / Caltech / University of Chicago / UT Austin
- **摘要与创新**：三个要素——(1) 从公开 gameplay 视频自动抽取玩家动作，构建 **40,000 小时、1,000+ 游戏**的 video-action 数据集；(2) 跨游戏 benchmark；(3) 统一 vision-action 模型 + 大规模 behavior cloning。零样本可玩 3D 动作、2D 平台、程序生成世界；微调后相对 from-scratch 模型任务成功率最高 **+52%**。作者明确其定位是 fast-reacting System-1 感知模型，不做长程规划/语言指令。
- **对比 prior**：此前游戏 agent 多为单游戏专用；NitroGen 把「互联网视频 → 动作标签 → 通用策略」做成开放基础模型，并开源数据/评测/权重。
- **链接**：[CVPR Open Access PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Magne_NitroGen_An_Open_Foundation_Model_for_Generalist_Gaming_Agents_CVPR_2026_paper.pdf)

### 5.4 其他亮点

| 论文 | 机构 | 贡献 |
|------|------|------|
| SAM 3D: 3Dfy Anything in Images | Meta Superintelligence Labs | 单图预测几何/纹理/布局，真实物体与场景人评至少 5:1 胜率 |
| VISTA: A Test-Time Self-Improving Video Generation Agent | (multi-agent) | refine-critique 多 agent 测试时自我改进，对 Veo 3 最高 60% 配对胜率，人评 66.4% |
| Reward Forcing | (streaming video) | 双向视频扩散蒸馏为少步自回归学生，单 H100 23.1 FPS 流式生成 |
| HoloCine | (multi-shot video) | 窗口交叉注意力 + 稀疏镜头间自注意力，分钟级多镜头叙事 |
| Phantom: Physics-Infused Video Generation | (physics) | V-JEPA2 物理 latent + 双向交叉注意力，VideoPhy PC +50.4% |
| LinVideo | (efficiency) | 后训练选择性线性化注意力，1.43–1.71× 加速，配合蒸馏 15.9–20.9× |
| M4V: Multimodal Mamba for T2V | (efficiency) | 用 Mamba 替换二次注意力，768×1280 长视频混合层 FLOPs −45% |

---

## 6. KDD 2026（San Jose，2026-08）

### 6.1 工业推荐 backbone

#### 6.1.1 MixFormer: Co-Scaling Up Dense and Sequence in Industrial Recommenders

- **中文标题**：MixFormer：工业推荐中稠密特征与行为序列的协同 Scaling
- **作者**：Xu Huang, Hao Zhang, Zhifang Fan, Yunwen Huang, Zhuoxing Wei, Zheng Chai, Jinan Ni, Yuchao Zheng, Q. M. Chen 等
- **机构**：ByteDance
- **摘要与创新**：工业推荐同时受限于稠密特征交互与长行为序列，两者往往分开 scaling。MixFormer 用统一 backbone 协同放大 dense 与 sequence 容量，在保持线上延迟的前提下提升效果（具体线上数字见论文）。
- **对比 prior**：相对 RankMixer / OneTrans / HSTU 的单轴 scaling，强调「稠密 + 序列」联合扩展。
- **链接**：[ACM DL 10.1145/3770855.3818447](https://doi.org/10.1145/3770855.3818447)

#### 6.1.2 MSN: A Memory-based Sparse Activation Scaling Framework for Large-scale Industrial Recommendation

- **中文标题**：MSN：大规模工业推荐的记忆化稀疏激活 Scaling 框架
- **机构**：ByteDance
- **创新**：用 memory-based sparse activation 在超大参数空间中按样本激活，兼顾容量与 serving 成本。
- **链接**：[ACM DL 10.1145/3770855.3818451](https://doi.org/10.1145/3770855.3818451)

#### 6.1.3 MDL: A Unified Multi-Distribution Learner in Large-scale Industrial Recommendation through Tokenization

- **中文标题**：MDL：通过 Tokenization 统一多分布学习的大规模工业推荐
- **机构**：ByteDance
- **摘要与创新**：把 scenario / task 信息当作 **specialized tokens**，而不是辅助输入或 gating。统一 tokenization + feature token self-attention + domain-feature attention + domain-fused aggregation，让场景/任务像 prompt 一样自底向上激活大参数空间。抖音搜索线上一个月：LT30 **+0.0626%**，change query rate **−0.3267%**，已全量。
- **链接**：[ACM DL 10.1145/3770855.3818445](https://doi.org/10.1145/3770855.3818445)

#### 6.1.4 CCFormer: Efficient Cross-Field Interaction and Hierarchical Sequence Compression for Industrial Recommendation at Tencent

- **中文标题**：CCFormer：腾讯工业推荐的高效跨域交互与层级序列压缩
- **机构**：腾讯 PCG
- **摘要与创新**：feature-field separated cross attention + long-sequence subspace token mixing + 层级序列压缩（逐步扩大感受野）。两个公开 benchmark + 腾讯工业数据；线上视频推荐 **CTR +3.57%**、广告 **revenue +1.71%**，相对 HSTU 训练加速 **2.21×**，已全量。
- **对比 prior**：HSTU/OneTrans 类统一 attention 在长序列上成本高；CCFormer 用层级压缩换效率。
- **链接**：[arXiv 2607.28070](https://arxiv.org/abs/2607.28070)

### 6.2 CTR 与 LLM 行为建模

#### 6.2.1 CTR-Sink: Attention Sink for Language Models in Click-Through Rate Prediction

- **中文标题**：CTR-Sink：面向 CTR 预测的语言模型 Attention Sink
- **作者**：Zixuan Li, Binzong Geng, Jing Xiong, Yong He, Yuxuan Hu, Jian Chen, Dingwei Chen, Xiyu Chang, Ngai Wong, Liang Zhang, Linjian Mo, Chengming Li, Chuan Yuan, Zhenan Sun
- **机构**：Ant Group / 中科院自动化所 NLPR / 香港大学 / 香港城市大学 / 中山大学 等
- **摘要与创新**：用户行为序列是离散动作 + 语义空分隔符，与 LM 预训练的连贯自然语言结构不匹配，造成 **semantic fragmentation**，注意力散乱。CTR-Sink 在相邻行为间插入带推荐信号（如时间距离）的 **behavior-level sink tokens**，并用两阶段训练把 LM 注意力引向 sink；再用 inter-sink 依赖增强行为相关性建模。工业数据 AUC +0.1%，MovieLens +0.12%，KuaiRec +0.08%（CTR 中 0.001 AUC 已属显著）。
- **对比 prior**：此前 LM4CTR 直接把行为转文本，假设 LM 自动理解；本文指出结构性错配并给出机制级修复。
- **链接**：[arXiv 2508.03668](https://arxiv.org/abs/2508.03668) · [代码](https://github.com/UGUESS-lzx/CTR-SINK)

#### 6.2.2 QueryFormer: Winning Solution for KDD Cup 2026 Tencent UniRec Challenge

- **中文标题**：QueryFormer：KDD Cup 2026 腾讯 UniRec 冠军方案
- **作者**：Yuanzhe Zhou, Zhaoyang Zeng
- **机构**：腾讯（UniRec 赛题）
- **摘要与创新**：pCVR 需要同时建模 feature interaction 与行为序列。现有统一架构多用 projection MLP 生成 query token，缺少显式 token-to-query attention。QueryFormer 用可堆叠 unified field–sequence block，以 cross-attention 生成 query，并把 sequence query 打包进 shared-parameter attention。Industrial Track 官方 test AUC **0.83254**（赛后扩规模 0.832713）；H=8 推理延迟仅为 H=1 的 **1.89×**。
- **对比 prior**：在同等预算下优于 HyFormer；消融显示 query generation 贡献最大。
- **链接**：[arXiv 2609.16548](https://arxiv.org/abs/2609.16548)

#### 6.2.3 FORGE: Forming Semantic Identifiers for Generative Retrieval in Industrial Datasets

- **中文标题**：FORGE：面向工业数据集的生成式检索 Semantic ID 构建
- **机构**：Alibaba / Taobao
- **摘要与创新**：系统研究 SID 构建策略对下游 GR 的影响，提出无需完整 GR 训练的两个 SID 评估指标；淘宝「猜你喜欢」线上交易数 **+0.35%**，策略已全量。开源 AL-GR 数据集：**140 亿交互、2.5 亿 item**、含多模态特征。
- **链接**：[ACM DL 10.1145/3770855.3817477](https://doi.org/10.1145/3770855.3817477)

### 6.3 其他

- **OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer**（ByteDance）：单 Transformer 统一特征交互与序列建模。[ACM DL](https://dl.acm.org/doi/epdf/10.1145/3774904.3792838)
- **Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks via Code Execution with State-Diff-Based Evaluation**：以「环境状态差分契约」而非轨迹/参数匹配判定任务成功；容器化企业 API sandbox，9 个 LLM / 260 任务。[ACM DL](https://dl.acm.org/doi/abs/10.1145/3770855.3817555)

---

## 7. SIGIR 2026（Melbourne，2026-07-20 ~ 07-24）

**规模**：1,271 投稿 → 234 接收（18%）。

### 7.1 SIGMA: A Semantic-Grounded Instruction-Driven Generative Multi-Task Recommender at AliExpress

- **中文标题**：SIGMA：AliExpress 语义接地、指令驱动的生成式多任务推荐
- **机构**：Alibaba / AliExpress
- **摘要与创新**：现有生成式推荐多停留在 interaction-driven next-item prediction，难以覆盖多样业务任务。SIGMA 把 item 实体 ground 到统一 latent space（通用语义 + 协同信号），用 hybrid item tokenization 兼顾精确建模与高效生成；构建大规模多任务 SFT 数据；推理时三步 item generation + adaptive probabilistic fusion，按任务调节 accuracy/diversity。离线 + 线上 A/B 均验证。
- **对比 prior**：相对单任务 next-item GR，强调 instruction-following 与多任务统一。
- **链接**：[ACM DL 10.1145/3805712.3808421](https://doi.org/10.1145/3805712.3808421)

### 7.2 GFlowGR: Fine-tuning Generative Recommendation Frameworks with Generative Flow Networks

- **中文标题**：GFlowGR：用生成流网络微调生成式推荐框架
- **作者**：Yejing Wang, Shengyu Zhou, Jinyu Lu, Qidong Liu, Xinhang Li, Wenlin Zhang, Feng Li, Pengjie Wang, Chuan Yu, Jian Xu, Bo Zheng, Xiangyu Zhao
- **机构**：City University of Hong Kong / Alibaba
- **摘要与创新**：GR 训练有两个错配：point-wise 单 ground-truth 优化 vs 部署需要多样高价值候选集；所有交互等权 vs 效用不同。GFlowGR 把 GR 重述为 sequential set-generation，用 trajectory sampler + behavior-aware reward model + GFlowNet token-level 监督，让生成概率对齐 item utility。三个真实数据集、两个 LLM-based GR backbone 稳定提升；淘宝搜索广告自 2025 年中上线，年收入相对 **+0.4%**（十亿级金额）。
- **对比 prior**：reward-based fine-tuning 缺 token-level 监督；GFlowNet 提供 set-wise + token-level 对齐。
- **链接**：[SIGIR 2026 program](https://sigir2026.org/SIGIR2026_program.pdf) · [代码](https://github.com/Applied-Machine-Learning-Lab/SIGIR26_GFlowGR)

### 7.3 其他值得关注

| 论文 | 机构 | 贡献 | 入口 |
|------|------|------|------|
| Verifiable Reasoning for LLM-based Generative Recommendation (VRec) | NUS / Meta AI | mixture-of-verifiers + proxy prediction 目标，兼顾可靠性与多维偏好验证 | [SIGIR program](https://sigir2026.org/SIGIR2026_program.pdf) |
| LWGR: Lagrangian-Constrained Personalized World Knowledge for GR | 中科院信工所 / Alibaba International | 个性化 soft instruction 抽取 LLM world knowledge，Lagrangian primal-dual 控制融合；最高 +11.23%，广告平台收入 +1.35% | [ACM DL](https://doi.org/10.1145/3805712.3809677) |
| RIGER: Reasoning-Grounded Intent Injection for Generative Recommendation | (阿里电商广告) | 离线 LLM 意图蒸馏 + SID-native 注入 + beam-aware GRPO；线上 clicks +1.6%，advertiser spend +1.3% | [ACM DL](https://doi.org/10.1145/3805712.3808423) |
| Full Retraining, Incremental Fine-tuning, and Hybrid Serving | (industrial GR) | 讨论生成式推荐模型更新与 serving 的分布偏移/灾难遗忘权衡 | [ACM DL](https://doi.org/10.1145/3805712.3808403) |
| GNN-Based Item Indexing for LLM-Enhanced Recommendation (GID) | (见论文) | 属性增强共现图 + 层次凝聚聚类 + 局部消息传递；HR@10 平均 +7.9% | [ACM DL](https://doi.org/10.1145/3805712.3809568) |

---

## 8. WWW 2026（2026）

### 8.1 DARA: Few-shot Budget Allocation in Online Advertising via In-Context Decision Making with RL-Finetuned LLMs

- **中文标题**：DARA：RL 微调 LLM 的上下文决策做少样本广告预算分配
- **作者**：Mingxuan Song, Yusen Huo, Bohan Zhou, Shenglin Yin, Zhen Xiao, Jieyi Long, Zhilin Zhang, Chuan Yu 等
- **机构**：Alibaba（AIGB 方向）
- **摘要与创新**：AIGB 下广告主目标个性化但历史交互少，传统 RL few-shot 效果差；LLM 有 in-context 泛化但缺数值精度。提出 **GRPO-Adaptive**（训练中动态更新 reference policy），再把决策拆成 few-shot reasoner（生成初始计划）+ fine-grained optimizer（反馈驱动精修）。真实与合成环境均优于 baseline。
- **对比 prior**：纯 RL 在 few-shot 不稳；纯 LLM prompt 缺精度。DARA 做双阶段互补。
- **链接**：[ACM DL 10.1145/3774904.3792129](https://doi.org/10.1145/3774904.3792129)

### 8.2 NEZHA: A Zero-sacrifice and Hyperspeed Decoding Architecture for Generative Recommendations

- **中文标题**：NEZHA：生成式推荐的零损失超高速解码架构
- **作者**：Yejing Wang, Shengyu Zhou, Jinyu Lu, Z. Liu, Langming Liu, Maolin Wang 等
- **机构**：CityU / Alibaba
- **摘要与创新**：GR 的自回归解码延迟高。NEZHA 在主模型内嵌 nimble autoregressive draft head 做 self-drafting，用 hash-set 的 model-free verifier 抑制 hallucination。淘宝自 2025-10 部署，业务 **+1.2%**（十亿级广告收入），服务数亿 DAU。
- **对比 prior**：传统 speculative decoding 需独立 draft model + model-based verifier，额外训练与延迟；NEZHA 去掉两者。
- **链接**：[ACM DL 10.1145/3774904.3792797](https://doi.org/10.1145/3774904.3792797)

### 8.3 其他

- **LBM: Hierarchical Large Auto-Bidding Model via Reasoning and Acting**（rfp0939）：把 auto-bidding 建成分层 LLM reasoning + acting 框架。
- **Field Matters: A Lightweight LLM-enhanced Method for CTR Prediction**（Yu Cui, Feng Liu, Jiawei Chen 等）：轻量 LLM 增强 CTR，WWW 2026 pp.6365–6376。
- **Position Auctions in AI-Generated Content**（Google Research：Balseiro, Bhawalkar, Deng, Feng, Mao, Mehta, Mirrokni, Paes Leme, Wang, Zuo）：AIGC 场景下的位置拍卖理论。
- **RecoWorld**（Meta，workshop）：为 agentic recommender 构建模拟环境。
- **Multi-relational Parallel Graph Retrieval for Web-scale Recommendations**（HKUST(GZ)/Baidu，industry track）。

---

## 9. CIKM 2025（Seoul，2025-11-10 ~ 11-14）

**规模**：2,890 投稿，870 篇进入 proceedings，整体接收率约 30%。

### 9.1 Best Full Paper — Reconsidering the Performance of GAE in Link Prediction

- **中文标题**：重新审视 GAE 在链接预测中的表现
- **作者**：Weishuo Ma, Yanbo Wang, Xiyuan Wang, Muhan Zhang
- **机构**：北京大学
- **摘要与创新**：近年 GNN link prediction 新模型层出不穷，但 baseline 可能过时。作者用 model-agnostic tricks + 超参搜索系统重调 Graph Autoencoder，发现在结构主导、特征有限的数据上，调好的 GAE 可匹配复杂模型且更高效；在 **ogbl-ppa** 上达到 SOTA，并逐项分析 trick 贡献。
- **对比 prior**：对「新模型涨点」的叙事提出 baseline 校准质疑，强调更新 baseline 才能准确评估进展。
- **链接**：[ACM DL 10.1145/3746252.3761108](https://doi.org/10.1145/3746252.3761108)

### 9.2 Best Applied Research Paper — Climber: Toward Efficient Scaling Laws for Large Recommendation Models

- **中文标题**：Climber：面向大型推荐模型的高效 Scaling Law
- **作者**：Songpei Xu, Shijia Wang, Da Guo, Xianwen Guo, Qiang Xiao, Bin Huang, Guanlin Wu, Chuanjiang Luo
- **机构**：NetEase Cloud Music
- **摘要与创新**：推荐场景多源异构 + 结构错配导致 scaling 不理想，且几十毫秒延迟约束随序列变长更紧。Climber 用 multi-scale sequence extraction 降常数复杂度、dynamic temperature modulation 适配场景、single-user multi-item batching + memory-efficient KV cache 提吞吐。离线 scaling 曲线更理想，受控 scaling 带来持续线上增益；网易云音乐服务数千万 DAU。
- **链接**：[ACM DL 10.1145/3746252.3761561](https://doi.org/10.1145/3746252.3761561)

### 9.3 Best Resource Paper — Semantic IDs in Generative Recommendation: A Practitioner's Handbook (GRID)

- **中文标题**：生成式推荐中的 Semantic ID：实践者手册
- **作者**：Clark Mingxuan Ju, Liam Collins, Leonardo Neves, Bhuvesh Kumar, Louis Yufeng Wang, Tong Zhao, Neil Shah
- **机构**：Snap Inc.
- **创新**：开源模块化 GR + SID 框架 **GRID**，支持组件替换与快速迭代；系统消融显示被忽视的架构组件会强烈影响 SID-based GR 表现。
- **链接**：[ACM DL 10.1145/3746252.3761612](https://doi.org/10.1145/3746252.3761612)

### 9.4 其他

- **SMTIR: Scenario-Aware Multi-Trigger Induction Network for CTR Prediction**（Xuan Ma 等，Tencent）：场景感知多触发归纳网络。[ACM DL](https://doi.org/10.1145/3746252.3761509)
- **A Cost-Effective Framework to Evaluate LLM-Generated Relevance Judgements**（Padova，Best Student）：小比例人工复核即可高置信估计 LLM 判读质量。
- **Data-centric Prompt Tuning for Dynamic Graphs**、**Transferable Deep Clustering Model**（Runner-up）。

---

## 10. RecSys 2025（Prague，2025-09-22 ~ 09-26）

### 10.1 Best Full Paper — You Don't Bring Me Flowers: Mitigating Unwanted Recommendations Through Conformal Risk Control

- **中文标题**：你不必送我花：用 Conformal Risk Control 缓解不想要的推荐
- **作者**：Giovanni De Toni, Erasmo Purificato, Emilia Gomez, Andrea Passerini, Bruno Lepri, Cristian Consonni
- **机构**：University of Trento / Fondazione Bruno Kessler / European Commission JRC
- **摘要与创新**：首个只用用户**二元反馈**即可**可证地**限制不想要推荐曝光的方法。基于 conformal risk control，结合 watch-time 等信号，模型无关；在大型视频平台数据上减少 unwanted content 且不牺牲准确率。委员会一致选中，肯定方法与社影响。
- **对比 prior**：传统做法靠后处理黑名单或重训；本文给出有限样本风险保证。
- **链接**：[RecSys 2025 Awards](https://recsys.acm.org/recsys25/awards/) · [代码](https://github.com/geektoni/mitigating-harm-recsys)

### 10.2 Best Short Paper — Beyond Top-1: Addressing Inconsistencies in Evaluating Counterfactual Explanations for Recommender Systems

- **中文标题**：不止 Top-1：推荐系统反事实解释评估中的不一致性
- **作者**：Amir Reza Mohammadi, Andreas Peintner, Michael Müller, Eva Zangerle
- **机构**：University of Innsbruck
- **创新**：指出反事实解释评测过度依赖 Top-1，提出更一致的多位置评估协议。

### 10.3 工业界重点

| 论文 | 机构 | 贡献 | 链接 |
|------|------|------|------|
| SUAN: Stacked Unified Attention Network（CTR scaling + distillation） | Meituan | 统一 attention block 跨三个数量级保持 scaling law；蒸馏 LightSUAN 线上 CTR +2.81%、CPM +1.69% | [RecSys 2025](https://recsys.acm.org/recsys25/accepted-contributions/) |
| GRACE: Generative Recommendation via Journey-Aware Sparse Attention on CoT Tokenization | Walmart Global Tech | 混合 CoT tokenization + journey-aware sparse attention；Home HR@10 +106.9%，Electronics +22.1%，attention 计算 −48% | [同上](https://recsys.acm.org/recsys25/accepted-contributions/) |
| LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders | ByteDance | global token + token merge + 工程优化；10+ 场景全量、十亿用户 | [同上](https://recsys.acm.org/recsys25/accepted-contributions/) |
| Hierarchical Graph Information Bottleneck for Multi-Behavior Recommendation | CUHK / WeChat Tencent | 图信息瓶颈 + 可学习边 dropout，抑制辅助行为噪声与负迁移 | [同上](https://recsys.acm.org/recsys25/accepted-contributions/) |
| Scaling Generative Recommendations with Context Parallelism on HSTU | (industrial) | jagged tensor 的 context parallelism，序列长度 5.3×，训练吞吐 1.55× | [RecSys 2025 industry](https://recsys.acm.org/recsys25/poster-2/) |

---

## 11. EMNLP 2025 / ACL 2026（NLP 侧）

### 11.1 EMNLP 2025 Best Paper — Infini-gram mini: Exact n-gram Search at the Internet Scale with FM-Index

- **中文标题**：Infini-gram mini：基于 FM-Index 的互联网规模精确 n-gram 检索
- **作者**：Hao Xu, Jiacheng Liu, Yejin Choi, Noah A. Smith, Hannaneh Hajishirzi
- **机构**：University of Washington / Allen Institute for AI
- **摘要与创新**：把 infini-gram 的精确 n-gram 统计从「需要巨大 suffix array」推进到 FM-Index 实现，在互联网规模语料上显著降低存储与查询成本，同时保持精确计数。对数据归因、污染检测、n-gram 语言模型分析都是基础设施级贡献。
- **链接**：[EMNLP 2025 Awards](https://2025.emnlp.org/program/awards/)

### 11.2 EMNLP 2025 其他

- **Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps**（Martin Tutek 等）：用 unlearning 检验 CoT 是否真正承载预测依据。
- **Collab-Overcooked: Benchmarking LLMs as Collaborative Agents**：多智能体协作 benchmark。
- **ReSo: A Reward-driven Self-organizing LLM-based Multi-Agent System**：奖励驱动的多 agent 自组织。
- **HMoE: Heterogeneous Mixture of Experts for Language Modeling**（Tencent Hunyuan）：异构专家粒度/容量。

### 11.3 ACL 2026 — code execution prediction 专题

| 论文 | 作者/机构 | 核心发现 | 链接 |
|------|----------|---------|------|
| DUET: Dual Execution for Test Output Prediction with Generated Code and Pseudocode | (见论文) | 代码执行易被小错误击穿，伪代码执行易幻觉；两路 functional majority voting 互补。LiveCodeBench Pass@1 **+13.6pp**，并在 BigCodeBench-Hard / DevEval / HumanEval(+) 过滤任务最佳 | [ACL Anthology](https://aclanthology.org/2026.findings-acl.2144.pdf) |
| The Path Not Taken: Duality in Reasoning about Program Execution | Eshgin Hasanov, Md. Mahadi Hassan, Santu Karmaker, Aashish Yadavally | 提出执行理解的对偶性：给定输入预测行为 vs 给定行为反推输入变更；DexBench 445 对实例、13 个 LLM | [ACL Anthology](https://aclanthology.org/2026.acl-long.735/) |
| CoRE: A Fine-Grained Code Reasoning Benchmark Beyond Output Prediction | Jun Gao 等 | 8 个 frontier LLM 存在 implementation-invariance 鲁棒性差距与「浅层执行」：答案对但中间状态错 | [ACL Anthology](https://aclanthology.org/2026.findings-acl.460/) |

---

## 12. 横向专题

### 12.1 Agent Systems

**核心趋势**：从「让 LLM 直接出招/出答案」转向「让 LLM 构造可验证的执行结构（code world model / harness / memory / state-diff）」。

| 工作 | Venue | 要点 |
|------|-------|------|
| Code World Models for General Game Playing | ICLR 2026 | LLM 生成 Python world model + MCTS；10 游戏 9 个 match/超 Gemini 2.5 Pro |
| Agent-Diff | KDD 2026 | 企业 API 任务用 state-diff 契约判成功，容器化 sandbox，260 任务/9 LLM |
| AgentSelect | ICML 2026 | 把 agent 配置选择建成 query-to-agent recommendation |
| TRAJEVAL | arXiv 2603.24631 | 把 code agent 轨迹拆成 search/read/edit 三段；16,758 轨迹、3 架构、7 模型；实时反馈 +2.2–4.6pp，成本 −20–31% |
| SPADE | arXiv 2608.19197 | Self-play：一个 LLM 当 Environment Designer 写 Gym 环境，一个当 Reasoning Agent；30B 规模，8 benchmark 平均 +5.3，BFCL-v4 +5.7，ACEBench-Agent +13.9 |
| MEMO | arXiv 2603.09022 | 多轮多 agent 游戏 context optimization；GPT-4o-mini 25.1%→49.5%，Qwen2.5-7B 20.9%→44.3% |

**解读**：agent 的瓶颈正在从「模型会不会」转向「环境是否可验证、状态是否可观测、失败是否可诊断」。Code world model 与 state-diff 是同一思想在不同域的实现：把开放世界压成可执行、可回放的契约。

### 12.2 Games & Generalist Game Agents

- **NitroGen**（CVPR 2026 Honorable Mention）：40,000 小时 / 1,000+ 游戏，微调后 +52% 相对任务成功率；定位 System-1 感知，不做长程规划。
- **Twin**（arXiv 2608.14490）：coding agent 在测试时写可执行 world model，ARC-AGI-3 通关 **179/183（97.8%）**，158/179 比人类更高效；base model 直接玩仅 7.8%，加 harness 61.1%，加 twin 93.3%。
- **GameBoyWorlds**（arXiv 2609.32093）：500 个执行任务，frontier model <50%；两个 fan-made Pokémon 长程通关，复杂 agent 连第一个里程碑都过不了。
- **Learning in Dreams, Winning in Reality**（arXiv 2610.08033）：十英雄 MOBA world model + Dyna loop，真实游戏 radiant 胜率 **70.2%**（421/600），dream-only 0%，loop 前 33.7%；世界模型对「policy 自己的对局」不准是核心问题。
- **Generalist Game Agents survey**（arXiv 2605.09965）：Dataset / Model / Harness / Benchmark 四支柱 + 五个根本 trade-off。

**解读**：游戏 agent 的共识是「策略不能只活在想象里」。world model 在训练分布内准确 ≠ 对 policy 诱导分布准确；在线锚定（Dyna / replay / twin validation）决定成败。

### 12.3 Code Execution Prediction & Repository-Level Reasoning

| 工作 | 规模 | 最强结果 | 关键 failure |
|------|------|---------|-------------|
| DUET (ACL 2026) | LiveCodeBench 等 | Pass@1 +13.6pp | 直接执行怕代码错，伪代码怕幻觉 |
| DexBench (ACL 2026) | 445 对实例 / 13 LLM | 双路径推理可区分动态理解 | 单路径 benchmark 易污染 |
| CoRE (ACL 2026) | 8 frontier LLM | 揭示鲁棒性差距 | 输出对但中间状态错 |
| SWE-Flux (arXiv 2609.28449) | 480 实例 / 12 repos | 最佳 37.71% | runtime dataflow 仅 6%；扰动后 GPT-5.4 100%→43.1% |
| RepoReasoner (arXiv 2607.25996) | 7 LLM | 最佳 69.1% Pass@1（oracle context） | 跨文件推理、call-chain recall 低 |
| TRAJEVAL (arXiv 2603.24631) | 16,758 轨迹 | Pass@1 预测 MAE 0.87–2.1% | 过度探索：read precision 仅 4–5% |

**解读**：代码能力评测正在从「最终输出对不对」转向「中间状态、等价实现、跨文件数据流、轨迹效率」。这对 agent 训练信号设计（process reward / state diff / trajectory feedback）直接影响。

### 12.4 Generative Models

- **4D / 3D 重建与生成**：D4RT（CVPR Best）、O-Voxel（CVPR Best Student）、SAM 3D（Meta，人评 5:1）。
- **视频生成**：VISTA（测试时多 agent 自我改进，对 Veo 3 最高 60% 胜率）、Reward Forcing（H100 23.1 FPS 流式）、HoloCine（多镜头长叙事）、Phantom（物理一致性，VideoPhy PC +50.4%）、LinVideo（1.43–1.71×，蒸馏后 15.9–20.9×）、M4V（Mamba 替换 attention，FLOPs −45%）。
- **评测**：VABench（音视频同步，15 指标 + 9 立体声指标）、VideoThinkBench（视频生成作为多模态推理载体）。
- **理论**：Why Diffusion Models Don't Memorize（NeurIPS Best）给出泛化窗口的动力学解释。

### 12.5 Sequential Modeling

- **架构层**：Gated Attention（NeurIPS Best）证明 SDPA 后 head-wise sigmoid gate 的稳定收益；Mamba-3（ICLR 2026）继续推进 selective SSM；HMoE（EMNLP 2025）探索异构专家。
- **推荐序列层**：CTR-Sink 用 behavior-level sink 修复语义碎片化；CCFormer 用层级压缩把长序列成本降下来（相对 HSTU 训练 2.21×）；MixFormer 做 dense + sequence 协同 scaling；LONGER 做超长序列的工程化。
- **视频序列层**：LoL（Longer than Longer）定位自回归长视频的 sink-collapse 到 RoPE 周期性与多头同质化，用 Multi-Head RoPE Jitter 做到小时级流式生成。

### 12.6 Benchmarks

- **多样性/开放性**：Artificial Hivemind / Infinity-Chat（26K query、31K 标注）。
- **Agent / 工具**：Agent-Diff（state-diff）、AgentSelect（agent 配置推荐）、TRAJEVAL（轨迹诊断）。
- **代码执行**：SWE-Flux、RepoReasoner、CoRE、DexBench、RACE-bench。
- **游戏**：GameBoyWorlds、NitroGen 跨游戏 suite、Twin（ARC-AGI-3）。
- **生成模型**：VABench、VideoThinkBench、PhysicsIQ。
- **CTR/推荐**：FORGE（SID 评估指标 + AL-GR 14B 交互）、GRID（SID GR 模块化 benchmark）。

---

## 13. 方法学与信息质量说明

1. **来源分层**：会议官网 awards/program > ACM DL / OpenReview / ACL Anthology > arXiv abs > 二手汇总。所有「线上 A/B」数字均为作者/厂商自报，未独立复现。
2. **时间窗**：本报告是截至 2026-10-30 的**会议全集回顾 + 近期 arXiv 补充**，不是单日新论文列表；与 `wiki/synthesis/2026-10-29/arxiv-paper-check.md`、`wiki/synthesis/2026-10-27/game-rl-daily.md` 等 sibling digest 存在主题重叠，但本页以 venue 归档为主。
3. **未证实项**：部分 ICML 2026 poster 仅公开摘要，具体数值/数据集/显著性未核验；已在正文标为「见论文」或省略具体数字。
4. **潜在冲突**：
   - ICML 2026 接收数在不同聚合页出现 6,352 / 6,634 两个口径，本页采用官方 6,352（26.6%）。
   - CVPR 2026 接收数出现 4,089 / 4,090 两个口径，本页采用官方新闻稿 4,089。
   - RecSys 2025 SUAN 的线上 +2.81% CTR / +1.69% CPM 为作者自报。
5. **术语**：正文保留 Scaling Law、Attention、Embedding、Token、Agent、World Model、RLVR、GRPO 等英文原词，避免翻译造成歧义。

---

## 14. 相关页面

- [[synthesis/2026-10-29/arxiv-paper-check|arXiv Paper Check — 2026-10-29]]
- [[synthesis/2026-10-27/game-rl-daily|Game RL Daily — 2026-10-27]]
- [[synthesis/2026-09-21/conference-digest|Conference Digest — 2026-09-21]]
- [[synthesis/2026-09-11/conference-digest|Conference Digest — 2026-09-11（Full Edition）]]
- [[ctr-scaling-landscape|CTR Scaling Landscape]]
- [[affiliation-landscape|Affiliation Landscape]]
