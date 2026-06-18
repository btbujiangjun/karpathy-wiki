---
title: 顶会论文专题报告 — 2026年6月全面版（NeurIPS 2025 Best / ICLR 2026 Outstanding / ICML 2026 / AAAI 2026 / CVPR 2026 Best / EMNLP 2025 / KDD 2026 / RecSys 2025 / SIGIR 2026 / WWW 2026 / CIKM 2025 / ACL 2026）
type: synthesis
created: 2026-06-18
updated: 2026-06-18
sources: [arxiv]
tags: [conference-digest, neurips-2025, iclr-2026, icml-2026, aaai-2026, cvpr-2026, emnlp-2025, kdd-2026, recsys-2025, sigir-2026, www-2026, cikm-2025, acl-2026]
---

# 顶会论文专题报告 — 2026年6月全面版

> 覆盖 12+ 个顶级会议/期刊，100+ 篇论文，13+ 个工业实验室。持续追踪 NeurIPS 2025 / ICLR 2026 / ICML 2026 / AAAI 2026 / CVPR 2026 / EMNLP 2025 / KDD 2026 / RecSys 2025 / SIGIR 2026 / WWW 2026 / CIKM 2025 / ACL 2026。

**报告日期**: 2026-06-18

---

## 目录

1. [NeurIPS 2025 — 最佳论文 & 亮点](#neurips-2025)
2. [ICLR 2026 — 杰出论文 & 亮点](#iclr-2026)
3. [ICML 2026 — 已接收论文亮点](#icml-2026)
4. [AAAI 2026 — 杰出论文 & 趋势](#aaai-2026)
5. [CVPR 2026 — 最佳论文 & 亮点](#cvpr-2026)
6. [EMNLP 2025 — 最佳论文 & 亮点](#emnlp-2025)
7. [KDD 2026 — 研究赛道亮点](#kdd-2026)
8. [RecSys 2025 — 亮点论文](#recsys-2025)
9. [SIGIR 2026 — 亮点论文](#sigir-2026)
10. [WWW 2026 — 亮点论文](#www-2026)
11. [CIKM 2025 — 亮点论文](#cikm-2025)
12. [ACL 2026 — 投稿与趋势](#acl-2026)
13. [各大实验室最新研究动态](#industry-labs)
14. [综合趋势分析](#trends)

---

## NeurIPS 2025

**时间**: 2025年12月 | **地点**: San Diego, USA | **接收率**: ~22%（5,526篇接收）

### 最佳论文奖

#### 1. Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free
- **标题(中文)**: 门控注意力：非线性、稀疏性与注意力汇消除
- **作者**: Zihan Qiu et al. (Alibaba Qwen Team)
- **机构**: Alibaba
- **Venue**: NeurIPS 2025 **Best Paper**
- **论文**: [NeurIPS Page](https://neurips.cc/virtual/2025/poster/120216)
- **核心创新**: 首次系统研究注意力门控（gating）对大模型性能的影响。在 30 多种 15B MoE 和 1.7B 密集模型变体上进行了 3.5T token 的大规模实验。发现一个**简单的架构修改**——在 SDPA 后添加 head-specific sigmoid gate——可以：
  - 消除 attention sink 问题
  - 提高训练稳定性（容忍更高学习率）
  - 提升长上下文外推能力
  - 已被整合到 Qwen3-Next 模型中

#### 2. Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?
- **标题(中文)**: RL 是否真正激励了 LLM 超越基础模型的推理能力？
- **作者**: Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Yang Yue, Shiji Song, Gao Huang
- **机构**: Tsinghua University
- **Venue**: NeurIPS 2025 **Best Paper Runner-up**
- **核心创新**: 通过精心设计的控制实验质疑 RL 对 LLM 推理能力的真实影响。发现：
  - Pass@k 测试中，随机数生成器在极限情况下也能达到 100%
  - RL 训练的主要收益可能来自格式变化而非真正的推理能力提升
  - 引起了社区对 RL 用于推理训练评估方法的广泛讨论

#### 3. Optimal Mistake Bounds for Transductive Online Learning
- **标题(中文)**: 转导在线学习的最优错误界
- **作者**: Zachary Chase, Steve Hanneke, Shay Moran, Jonathan Shafer
- **Venue**: NeurIPS 2025 **Best Paper Runner-up**
- **核心创新**: 解决了 30 年之久的开放问题——量化了无标签数据在在线学习中的优势。证明对于 Littlestone 维度为 d 的每个概念类，转导错误界至少为 Ω(√d)，且该界是紧的。

### 其他亮点论文

#### 4. Superposition Yields Robust Neural Scaling
- **标题(中文)**: 叠加产生鲁棒的神经缩放
- **作者**: Multiple authors
- **核心创新**: 通过控制 toy model 中的叠加（superposition）并检查真实 LLM，发现强叠加自然地产生熟悉的"大模型=低损失"幂律规律，解释了缩放律何时有效及何时可能失效。

#### 5. Multi-Agent Collaboration via Evolving Orchestration
- **标题(中文)**: 通过演化编排的多智能体协作
- **作者**: Multiple authors
- **核心创新**: 引入"puppeteer"范式——一个集中式编排器通过 RL 训练，动态地引导多个 LLM 代理。能自适应地演变为更紧凑的循环推理结构，以更低的 token 消耗实现更高的准确率。

#### 6. Artificial Hivemind: The Open-Ended Homogeneity of LMs (and Beyond)
- **标题(中文)**: 人工蜂群思维：语言模型（及更多）的开放性同质性
- **作者**: Multiple authors
- **核心创新**: 发布大规模开放式 prompt 数据集，揭示了 LLM 往往落入"人工蜂群思维"——生成惊人相似的答案——并测量了多样性坍塌。

#### 7. Why Diffusion Models Don't Memorize
- **标题(中文)**: 为什么扩散模型不记忆
- **作者**: Multiple authors
- **核心创新**: 揭示了扩散训练中的隐式动力正则化机制，解释了为什么扩散模型在大型数据集上训练时不会像 LLM 那样记忆训练数据。

### NeurIPS 2025 Test of Time Award

- **Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks** — Shaoqing Ren, Kaiming He, Ross Girshick, Jian Sun (2015)
  - 引入 RPN 使检测网络可共享全图像卷积特征，实现近乎零成本的区域提议

---

## ICLR 2026

**时间**: 2026年4月22-25日 | **地点**: Rio de Janeiro, Brazil | **接收率**: ~31%（3,704篇接收）

### 杰出论文奖（Outstanding Papers）

#### 1. Transformers are Inherently Succinct
- **标题(中文)**: Transformer 天生是简洁的
- **Venue**: ICLR 2026 **Outstanding Paper**
- **核心创新**: 从理论角度证明 Transformer 架构具有内在的简洁性偏好，为理解 Transformer 的泛化能力提供了新的理论视角。

#### 2. Mamba-3: Improved Sequence Modeling using State Space Principles
- **标题(中文)**: Mamba-3：使用状态空间原则改进序列建模
- **作者**: Aakash Sunil Lahoti, Kevin Li, Berlin Chen, Caitlin Wang, Aviv Bick, Zico Kolter, Tri Dao, Albert Gu
- **机构**: Carnegie Mellon University / Princeton
- **Venue**: ICLR 2026 **Oral**
- **论文**: [OpenReview](https://openreview.net/forum?id=HwCvaJOiCj)
- **核心创新**: 从推理优先的角度出发，引入三个核心改进：
  - 更具表达力的循环（recurrence）
  - 支持更丰富状态追踪的复值状态更新规则
  - 多输入多输出（MIMO）公式
  - 在检索、状态追踪和下游语言建模任务上显著提升
  - 在固定推理预算下设立了性能帕累托前沿

#### 3. Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning
- **标题(中文)**: Cosmos Policy：微调视频模型实现视觉运动控制与规划
- **作者**: NVIDIA
- **机构**: NVIDIA
- **Venue**: ICLR 2026
- **论文**: [Paper Digest](https://www.paperdigest.org/reader/?paper_id=iclr-forum-id-wPEIStHxYH-2026-02-17)
- **核心创新**: 将预训练视频生成模型微调为视觉运动控制策略，连接了视觉生成与机器人控制的范式。

#### 4. WAVE: Learning Unified & Versatile Audio-Visual Embeddings with Multimodal LLM
- **标题(中文)**: WAVE：使用多模态 LLM 学习统一且通用的视听嵌入
- **作者**: Changli Tang, Qinfan Xiao, Ke Mei, Tianyi Wang, Fengyun Rao, Chao Zhang
- **Venue**: ICLR 2026 **Oral**
- **核心创新**: 探索多模态 LLM 嵌入在音频和视频等动态模态中的表现，提出统一视听嵌入方法。

#### 5. MEM1: Memory-Reasoning Synergy for Long-Horizon Agents
- **标题(中文)**: MEM1：长周期智能体的记忆-推理协同
- **Venue**: ICLR 2026
- **已收录于**: wiki/papers/agents/mem1-agent.md

### Lambda Labs 报告亮点

Lambda Labs 在 ICLR 2026 发表了 12 篇论文，涵盖：

- **AgentFlow**: 可训练的智能体系统，团队可通过 Flow-GRPO 学习规划和工具使用。7B AgentFlow 模型在搜索、数学和科学推理上击败 GPT-4o。
- **KAIROS Benchmark**: 将模型置于不可靠同伴和对抗性参与者的协作场景中，揭示 LLM 在同伴压力下屈服；同论文中的 RL 方案帮助小模型抵抗。
- **EdiVal-Agent**: 使用智能体作为评估者，通过将图像分解为对象来评价多轮图像编辑质量。

---

## ICML 2026

**时间**: 2026年7月6-11日 | **地点**: Seoul, South Korea | **接收率**: 26.6%（6,352篇接收，23,918篇投稿）

### 亮点论文

#### 1. Shannon Scaling Law: LLMs as Noisy Channels
- **标题(中文)**: 香农缩放律：作为噪声信道的 LLM
- **arXiv**: 2605.23901
- **Venue**: ICML 2026
- **已收录于**: wiki/papers/llm-training/shannon-scaling-law.md
- **核心创新**: 将 LLM 解码过程建模为噪声信道，从信息论角度推导缩放律。

#### 2. BLT Byte-Level Diffusion
- **标题(中文)**: BLT 字节级扩散
- **核心创新**: 在字节级别实现扩散模型，绕过 tokenization 的限制。

#### 3. Ctrl-R RL
- **标题(中文)**: Ctrl-R 强化学习
- **核心创新**: 将强化学习中的控制理论应用于 LLM 训练。

#### 4. FFOLayer
- **标题(中文)**: FFO 层（前馈-前馈-输出）
- **核心创新**: 提出新颖的神经网络层设计。

#### 5. AIRA-Compose: Can AI Agents Design Better Neural Networks?
- **标题(中文)**: AIRA-Compose：AI 智能体能否设计更好的神经网络？
- **核心创新**: 基于智能体的神经架构搜索，探索 AI 能否自主设计更优网络。

#### 6. How Does Chain of Thought Decompose Complex Tasks?
- **标题(中文)**: CoT 如何分解复杂任务？
- **作者**: Amrut Nadgir, Vijay Balasubramanian, Pratik Chaudhari (UPenn)
- **Venue**: ICML 2026
- **论文**: [arXiv:2604.08872](https://arxiv.org/abs/2604.08872)
- **核心创新**: 通过理论分析和实验揭示 Chain-of-Thought 如何将复杂任务分解为子步骤的机制。

#### 7. Emergent Alignment via Competition
- **标题(中文)**: 通过竞争涌现的对齐
- **作者**: Natalie Collina, Surbhi Goel, Aaron Roth, Emily Ryu, Mirah Shi (UPenn)
- **Venue**: ICML 2026
- **论文**: [arXiv:2509.15090](https://arxiv.org/abs/2509.15090)
- **核心创新**: 提出智能体间的竞争机制如何自然导致对齐行为的涌现。

#### 8. Online Conformal Prediction via Universal Portfolio Algorithms
- **标题(中文)**: 通过通用投资组合算法的在线共形预测
- **作者**: Tuo Liu, Edgar Dobriban, Francesco Orabona (UPenn)
- **Venue**: ICML 2026 **Spotlight**
- **论文**: [arXiv:2602.03168](https://arxiv.org/abs/2602.03168)

#### 9. ALIVE: Interactive Frontend Games via RL
- **标题(中文)**: ALIVE：通过 RL 的交互式前端游戏
- **机构**: Alibaba
- **Venue**: ICML 2026
- **已收录于**: wiki/papers/games/alive-frontend-games.md

#### 10. Self-Supervised Flow Matching (Self-Flow)
- **标题(中文)**: 自监督流匹配
- **Venue**: ICML 2026
- **已收录于**: wiki/papers/generative-models/self-flow-matching.md

#### 11. UniAR: Unified Multimodal Autoregressive Modeling
- **标题(中文)**: UniAR：统一多模态自回归建模
- **机构**: Alibaba
- **Venue**: ICML 2026
- **已收录于**: wiki/papers/generative-models/uniar-multimodal.md

#### 12. How Does the Lagrangian Guide Safe Reinforcement Learning through Diffusion Models?
- **标题(中文)**: 拉格朗日方法如何通过扩散模型引导安全强化学习？
- **作者**: Xiaoyuan Cheng et al. (UCL Dynamic Systems Lab)
- **Venue**: ICML 2026

#### 13. MMPD-Bench: Bridging Multimodal Fission with Multi-Polarimetric Modalities Decomposition
- **标题(中文)**: MMPD-Bench：通过多极化模态分解桥接多模态裂变
- **作者**: Yi He et al. (UCL / Oxford)
- **Venue**: ICML 2026

---

## AAAI 2026

**时间**: 2026年1月20-27日 | **地点**: Singapore | **接收**: 4,167篇（23,680投稿, 17.6%接收率）

### 杰出论文奖

AAAI 2026 评选出 5 篇主赛道杰出论文 + 2 篇 AI for Social Impact 论文。

### 核心趋势

AAAI 2026 的主题是"Creating Collaborative Bridges Within and Beyond AI"，反映了研究优先级从模型规模扩展转向高效、可控、可信、可部署的 AI 系统。

**AI 辅助审稿实验**: AAAI 2026 与 OpenAI 合作，对所有 22,977 篇进入完整审稿阶段的论文生成了 AI 审稿意见。这是顶级 AI 会议首次在完整技术赛道部署生成式 AI 审稿。

### 亮点论文

#### 1. Resource Efficient Sleep Staging via Multi-Level Masking and Prompt Learning
- **标题(中文)**: 通过多级掩码和提示学习实现资源高效睡眠分期
- **作者**: Lejun Ai, Yulong Li, Haodong Yi, Jixuan Xie, Yue Wang, Jia Liu, Min Chen, Rui Wang
- **Venue**: AAAI 2026
- **核心创新**: 提出 MASS 框架，通过多级掩码策略和分层提示学习机制，在极少量数据下实现 SOTA 睡眠分期性能。

#### 2. Contextualizing Recommendation Explanations with LLMs: A User Study
- **标题(中文)**: 用 LLM 上下文化推荐解释：一项用户研究
- **作者**: Yuanjun Feng, Stefan Feuerriegel, Yash Raj Shrestha
- **Venue**: AAAI ICWSM 2026
- **论文**: [arXiv:2501.12152](https://arxiv.org/pdf/2501.12152)
- **核心创新**: 研究 LLM 生成的推荐如何影响用户的动机和行为，为以用户为中心的推荐系统提供洞察。

---

## CVPR 2026

**时间**: 2026年6月3-7日 | **地点**: Denver, USA | **接收**: 4,090篇（16,092投稿, 25.42%接收率）

### CVPR 2026 最佳论文奖

#### 1. Efficiently Reconstructing Dynamic Scenes One D4RT at a Time
- **标题(中文)**: 高效重建动态场景——一次一个 D4RT
- **作者**: Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, Liliane Momeni, Junyu Xie, Shuyang Sun, Rahul Sukthankar, Joëlle K. Barral, Raia Hadsell, Zoubin Ghahramani, Andrew Zisserman, Junlin Zhang, Mehdi S. M. Sajjadi
- **机构**: Google DeepMind / UCL / Oxford
- **Venue**: CVPR 2026 **Best Paper**
- **核心创新**: 开发了 D4RT 网络，使用统一的 Transformer 架构从视频中重建动态 4D 场景的几何和运动。模型估计深度、时空对应和相机参数，允许独立高效地查询空间和时间中任意点的 3D 位置。

#### 2. Native and Compact Structured Latents for 3D Generation
- **标题(中文)**: 用于 3D 生成的原生紧凑结构潜变量
- **Venue**: CVPR 2026 **Best Student Paper**

#### 3. NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **标题(中文)**: NitroGen：面向通用游戏智能体的开放基础模型
- **Venue**: CVPR 2026 **Best Paper Honorable Mention**

### 核心趋势

CVPR 2026 见证了从经典 CV 到多模态和生成的重大转变：
- 多模态 LLM 论文数量翻倍
- 视频生成论文同比增长 2.3 倍
- 经典检测/分类论文占比下降

### 亮点论文

#### 4. WorldLens: Full-Spectrum Evaluations of Driving World Models in Real World
- **标题(中文)**: WorldLens：真实世界中驾驶世界模型的全谱评估
- **作者**: A. Liang, L. Kong, T. Yan et al.
- **Venue**: CVPR 2026 **Oral**
- **论文**: [arXiv:2512.10958](https://arxiv.org/abs/2512.10958)

#### 5. OmniVGGT: Omni-Modality Driven Visual Geometry Grounded Transformer
- **标题(中文)**: OmniVGGT：全模态驱动的视觉几何接地 Transformer
- **作者**: H. Peng, H. Li, Y. Dai et al.
- **Venue**: CVPR 2026 **Highlight**
- **论文**: [arXiv:2511.10560](https://arxiv.org/abs/2511.10560)

#### 6. Trainable Log-linear Sparse Attention for Efficient Diffusion Transformers
- **标题(中文)**: 用于高效扩散 Transformer 的可训练对数线性稀疏注意力
- **作者**: Y. Zhou, Z. Xiao, T. Wei, S. Yang, X. Pan
- **Venue**: CVPR 2026 **Highlight**
- **论文**: [arXiv:2512.16615](https://arxiv.org/abs/2512.16615)

#### 7. PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image
- **标题(中文)**: PhysX-Anything：从单张图像生成可仿真物理 3D 资产
- **作者**: Z. Cao, F. Hong, Z. Chen, L. Pan, Z. Liu
- **Venue**: CVPR 2026
- **论文**: [arXiv:2511.13648](https://arxiv.org/abs/2511.13648)

---

## EMNLP 2025

**时间**: 2025年11月4-9日 | **地点**: Suzhou, China | **接收**: 1,811篇主会 + 1,417篇 Findings（8,174投稿）

### 亮点论文

#### 1. Mind the Value-Action Gap: Do LLMs Act in Alignment with Their Values?
- **标题(中文)**: 注意价值-行动差距：LLM 的行动是否与其声称的价值观一致？
- **作者**: Multiple authors
- **Venue**: EMNLP 2025 Main
- **核心创新**: 发现 LLM 自述的价值观与其实际行动之间存在系统性差异——称为"value-action gap"。构建了量化此差距的基准，并连接到心理学中长期存在的人类知行不一现象。

#### 2. Speculative Streaming: Efficient and Scalable Speculative Decoding with Multi-Stream Attention
- **标题(中文)**: 推测性流式解码：基于多流注意力机制的高效可扩展推测解码
- **作者**: Nikhil Bhendawade, Irina Belousova, Qichen Fu et al.
- **机构**: Apple
- **Venue**: EMNLP 2025

#### 3. PrimeX: A Dataset of Worldview, Opinion, and Explanation
- **标题(中文)**: PrimeX：世界观、观点和解释数据集
- **作者**: Rik Koncel-Kedziorski, Brihi Joshi, Tim Paek
- **机构**: Apple
- **Venue**: EMNLP 2025

#### 4. Evaluating Evaluation Metrics — The Mirage of Hallucination Detection
- **标题(中文)**: 评估评估指标——幻觉检测的海市蜃楼
- **作者**: Apple
- **Venue**: EMNLP 2025
- **核心创新**: 揭示当前幻觉检测方法中的系统性缺陷。

#### 5. Can Language Models Learn to Explain Their Reasoning?
- **标题(中文)**: 语言模型能否学会解释其推理过程？
- **Venue**: EMNLP 2025 Findings

#### 6. VersBand: Versatile Framework for Song Generation with Prompt-based Control
- **标题(中文)**: VersBand：基于提示控制的多功能歌曲生成框架
- **作者**: Yu Zhang, Wenxiang Guo, Changhao Pan et al.
- **Venue**: EMNLP 2025 Findings
- **核心创新**: 提出多任务歌曲生成框架，包含 VocalBand（流匹配歌声）、AccompBand（基于流匹配 Transformer + Band-MoE 伴奏）、LyricBand（歌词）和 MelodyBand（旋律）。

---

## KDD 2026

**时间**: 2026年8月9-13日 | **地点**: Jeju Island, Korea

KDD 2026 采用双周期投稿制。第一卷（Cycle 1）已发表，包含 Research Track 论文。

### 亮点论文

#### 1. RankUp: High-rank Representations for Ad Ranking
- **标题(中文)**: RankUp：广告排序的高秩表示
- **机构**: Tencent
- **Venue**: KDD 2026
- **已收录于**: wiki/papers/ctr/rankup-advertising.md
- **论文**: [arXiv:2604.17878](https://arxiv.org/abs/2604.17878)

#### 2. RankElastor: Effective-Rank Dynamics for Recommendation
- **标题(中文)**: RankElastor：推荐系统的有效秩动力学
- **Venue**: KDD 2026
- **已收录于**: wiki/papers/recommendation/rankelastor-recommendation.md
- **论文**: [arXiv:2605.23191](https://arxiv.org/abs/2605.23191)

#### 3. JourneyFormer: Production Sequential RecSys at Airbnb
- **标题(中文)**: JourneyFormer：Airbnb 生产环境序列推荐系统
- **机构**: Airbnb
- **Venue**: KDD 2026

#### 4. DAS: Dual-Aligned Semantic IDs Empowered Industrial Recommender System
- **标题(中文)**: DAS：双对齐语义 ID 赋能的工业推荐系统
- **机构**: Tencent
- **Venue**: KDD 2026

#### 5. Tencent Advertising Algorithm Challenge 2025: All-Modality Generative Recommendation
- **标题(中文)**: 腾讯广告算法大赛2025：全模态生成式推荐
- **机构**: Tencent
- **论文**: [arXiv:2604.04976](https://arxiv.org/pdf/2604.04976)
- **核心创新**: 发布 TencentGR-1M 和 TencentGR-10M 数据集，为工业级全模态生成式推荐提供基准。

---

## RecSys 2025

**时间**: 2025年9月22-26日 | **地点**: Prague, Czech Republic

### 亮点论文

#### 1. Beyond Immediate Click: Engagement-Aware and MoE-Enhanced Transformers for Sequential Movie Recommendation
- **标题(中文)**: 超越即时点击：面向参与度感知和 MoE 增强的序列电影推荐 Transformer
- **机构**: Amazon Prime Video
- **Venue**: RecSys 2025
- **核心创新**: 提出 temporal Mixture-of-Experts + Transformer 的序列推荐。关键组件：
  - Personalized Hard-Negative Sampling (PHNS)
  - 参与度感知多任务学习（CTR + 排序 + 完成率回归）
  - Next-K 训练（软标签 1.0/0.6/0.3）
  - 在 Prime Video 百万级用户数据上 NDCG@1 提升 +3.5%

#### 2. Explicit Negatives at Scale (TikTok)
- **标题(中文)**: TikTok 大规模显式负反馈
- **机构**: TikTok / ByteDance
- **Venue**: RecSys 2025
- **核心创新**: 展示如何捕获、去噪和传播"不喜欢"信号——通过对比学习塑形和降级/过滤进行训练和推理传播。

#### 3. Peak-End Retention (Meta Reels)
- **标题(中文)**: Meta Reels 的峰-终记忆保持
- **机构**: Meta
- **Venue**: RecSys 2025
- **核心创新**: 受心理学启发的长期优化方法，利用峰-终效应优化用户留存。

#### 4. Lasso: Large Language Model-based User Simulator for Cross-Domain Recommendation
- **标题(中文)**: Lasso：基于 LLM 的跨域推荐用户模拟器
- **Venue**: RecSys 2025
- **论文**: [ACM DL](https://dl.acm.org/doi/10.1145/3705328.3748048)

#### 5. Exploring Scaling Laws of CTR Model for Online Performance Improvement (SUAN)
- **标题(中文)**: CTR 模型缩放律的在线性能提升探索
- **机构**: Meituan
- **Venue**: RecSys 2025
- **论文**: [arXiv:2508.15326](https://arxiv.org/abs/2508.15326)
- **已收录于**: wiki/papers/ctr/suan-ctr-scaling.md

#### 6. LONGER: Ultra-Long User Behavior Sequences
- **标题(中文)**: LONGER：超长用户行为序列
- **机构**: ByteDance
- **Venue**: RecSys 2025
- **论文**: [arXiv:2505.04421](https://arxiv.org/abs/2505.04421)
- **已收录于**: wiki/papers/ctr/longer.md

#### 7. Generalized User Representations for Large-Scale Recommendations
- **标题(中文)**: 大规模推荐的广义用户表示
- **Venue**: RecSys 2025

#### 8. Streaming Trends: Low-Latency Platform for Dynamic Video Grouping
- **标题(中文)**: Streaming Trends：动态视频分组的低延迟平台
- **Venue**: RecSys 2025

---

## SIGIR 2026

**时间**: 2026年7月20-24日 | **地点**: Melbourne, Australia

### 亮点论文 (来自接受的论文列表)

SIGIR 2026 已公布接收论文列表，涵盖：

- **DiSCo: LLM Knowledge Distillation for Efficient Sparse Retrieval in Conversational Search**
- **Multi-modal Semantic Graph Prompt Learning Framework for Conversational Recommender Systems**
- **Nugget-based Annotation Protocol for Evaluating Long-form RAG**
- **Rankers, Judges, and Assistants: Understanding the Interplay of LLMs in IR Evaluation** (Perspectives)
- **NExT-Search: Rebuilding User Feedback Ecosystem for Generative AI Search** (Perspectives)
- **Toward Holistic Evaluation of Recommender Systems Powered by Generative Models** (Perspectives)

---

## WWW 2026

**时间**: 2026年4月13-17日（已延期至更晚）

- **ThinkRec: Thinking-based LLM Recommendation** — WWW 2026
  - 已收录于: wiki/papers/recommendation/thinkrec.md
- **GenCI: Generative CTR via Cohort Intent Learning** — WWW 2026
  - 已收录于: wiki/papers/ctr/genci-ctr.md
- **SparseCTR: Sparse Attention Long-Term CTR** — Meituan / WWW 2026
  - 已收录于: wiki/papers/ctr/sparsectr.md

---

## CIKM 2025

**时间**: 2025年11月10-14日 | **地点**: Seoul, Korea | **接收率**: 27.23%（443篇全文中1,627投稿）

### 亮点论文

- **Distribution-Guided Auto-Encoder for User Multimodal Interest Cross Fusion** — Lazada Group
- **LangPTune: Optimizing Language-based User Profiles for Recommendation** — Cornell
- **Towards Large Generative Recommendation: A Tokenization Perspective** — Tutorial (UCSD / USTC / NUS)
- **RankMixer: Scaling Up Ranking Models** — ByteDance / CIKM 2025
  - 已收录于: wiki/papers/ctr/rankmixer.md

---

## ACL 2026

**时间**: 2026年7月2-7日 | **地点**: San Diego, USA

**主题**: "Explainability of NLP Models"

ACL 2026 正在接受投稿（ARR 2025 October / 2026 January 周期），接收论文尚未完全公布。目前已知的亮点：

- 强调 NLP 模型的可解释性
- 沿袭 ARR 审稿系统
- 论文继续通过 ACL Rolling Review (ARR) 投稿

### ACL 2025 最具影响力论文回顾

- **Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference** — ACL 2025 (IF:6)

---

## 各大实验室最新研究动态

### Google DeepMind

- **Gemini 3.5 Flash** — 2026年5月发布，面向通用场景
- **Gemini Omni** — 2026年5月发布，多模态统一
- **Gemma 4 12B** — 编码器自由的多模态模型，2026年6月
- **DiffusionGemma** — 4 倍更快文本生成，2026年6月
- **Gemini-SQL2** — Text-to-SQL 基准测试最高分
- **D4RT** — CVPR 2026 最佳论文（动态 4D 场景重建）

### OpenAI

- **GPT-5.5 Instant** — 2026年最新迭代
- **ChatGPT Images 2.0** — 图像中的文本生成突破（准确生成餐厅菜单等）
- 持续推理模型迭代（o1/o3 系列向生产部署演进）

### Anthropic

- **Claude Opus 4.8** — 2026年5月发布
- **Claude Fable 5** / **Mythos 5** — 2026年6月最新
- **Claude Opus 4.6** — 百万 token 上下文窗口，MRCR v2 上的 8-needle 变体达 76%（前代仅 18.5%）
- **Claude Design** — 进入视觉创作领域

### Meta AI

- **Llama 3.3 70B** — GPT-4 级别性能，可在 64GB RAM 消费级硬件运行
- **Llama 4** — 2026年新一代开源 LLM
- **HSTU / ULTRA-HSTU** — 生成式推荐系统 Trillion 参数扩展
- **Kunlun / Wukong** — 推荐系统统一架构缩放律

### ByteDance / TikTok

- **Seed 2.0 (Doubao)** — 中国最大聊天机器人底层模型
- **Monolith** — 已开源的轻量级推荐系统框架（9.3k stars）
- **HLLM** — 层级式 LLM 序列推荐
- **RankMixer / TokenMixer-Large / MixFormer** — CTR 缩放方法论
- **Longer / Make It Long Keep It Fast** — 超长用户行为序列建模
- **Precise** — SDE-Consistent 流匹配 RL 采样

### Alibaba

- **Qwen3-Next** — 整合 Gated Attention 最新成果
- **Qwen3 Technical Report** — arXiv:2505.09388
- **EST / FAT** — CTR 缩放律
- **MUSE** — 100K 长度终身用户兴趣建模
- **SORT / HHFT** — 工业 CTR 排序架构

### Tencent

- **RankUp** — 广告排序高秩表示（KDD 2026）
- **DAS** — 双对齐语义 ID 推荐系统
- **GE4Rec** — 生成式 CTR 范式
- **TokenFormer** — 统一多字段和序列推荐
- **All-Modality Generative Recommendation Challenge**

### Microsoft Research

- **SkillOpt** — 自演化智能体技能（Microsoft Research Asia）
- **Inductive Deductive Synthesis** — 面向验证系统的智能体编程
- **SkillOpt boosts GPT-5.5** — 通过训练好的 Markdown 文件提升模型

### NVIDIA

- **Cosmos Policy** — 视频模型微调用于机器人控制
- **Nemotron 3** — Mamba2-Transformer 混合架构

### Apple

- **Speculative Streaming / MLX** — 高效 LLM 推理框架
- **Bias after Prompting / PrimeX** — LLM 公平性与数据集

### Netflix

- **Scaling Generative Recommenders** — 生成式推荐扩展

### Kuaishou

- **RPORec** — RL + 推理用于推荐
- **CHIME** — 整体兴趣 + LLM + VQ
- **UniMixer** — 统一架构缩放律

---

## 综合趋势分析

### 核心主题 1：推理模型与 Test-Time Compute

2025-2026 最显著的架构发展方向是推理模型类别。OpenAI o1/o3、DeepSeek R1、以及各类 RLVR 方法展示了在推理时分配可变计算量的能力。核心范式转变：从训练时计算扩展（更大模型）→ 推理时计算扩展（更聪明地使用计算）。

### 核心主题 2：注意力机制创新

- **Gated Attention** (NeurIPS 2025 Best Paper) — 简单的 sigmoid 门控在 SDPA 后即可带来显著提升
- **Mamba-3** (ICLR 2026 Oral) — 状态空间模型的推理优先视角改进
- **各种高效注意力** — Trainable Sparse Attention (CVPR 2026), Linear Attention (LIME), Preisach Attention

### 核心主题 3：推荐系统的生成式范式

从判别式 CTR 模型向生成式推荐架构的转型继续加速：
- HSTU → ULTRA-HSTU（Meta）
- GE4Rec（Tencent）
- GenCI（WWW 2026）
- Generative Recommendation Tokenization（CIKM 2025 Tutorial）
- 语义 ID 成为生成式推荐的标准化基础

### 核心主题 4：AI 智能体从演示到生产

- 多智能体编排系统（ICLR 2026 AgentFlow 等）
- 智能体安全成为热门话题（KAIROS Benchmark, Agent Security Arena）
- 编码智能体在社会科学研究中的应用（Anthropic 2026 年 5 月调查）
- 智能体记忆/推理协同（MEM1）

### 核心主题 5：扩散模型与流匹配

- 扩散模型不记忆的动力学正则化解释（NeurIPS 2025）
- 流匹配与 RL 的结合（FPO, Precise SDE-Consistent Sampling）
- DiffusionGemma（4x 更快文本生成）
- BLT Byte-Level Diffusion

### 核心主题 6：工业 CTR/推荐缩放律

2025-2026 年发表大量 CTR 缩放律研究：
- 来自 Meta 的 LLaTTE、ULTRA-HSTU、Kunlun
- 来自 ByteDance 的 TokenMixer-Large、MixFormer、RankMixer
- 来自 Alibaba 的 EST、FAT
- 来自 Meituan 的 SUAN
- 统一趋势：缩放律在推荐系统中也同样成立

### 核心主题 7：从经典 CV 到多模态与生成

CVPR 2026 的数据明确显示此趋势：
- 多模态 LLM 论文 +100% YoY
- 视频生成论文 +230% YoY
- 经典检测/分类论文占比下降

---

*本报告为自动生成，覆盖 2025-2026 年主要 AI/ML 会议的最新论文。持续更新。*
