---
title: "顶会论文专题报告 — Conference & arXiv Digest (2026-07-11 全面更新版)"
type: synthesis
created: 2026-07-11
updated: 2026-07-11
sources: [web-search-arxiv.md, web-search-proceedings.md]
tags: [ICML, ICLR, AAAI, NeurIPS, CVPR, KDD, ACL, EMNLP, SIGIR, WWW, CIKM, RecSys, conference, papers, survey]
---

# 顶会论文专题报告 — Conference & arXiv Digest (2026-07-11)

> 覆盖 12+ 顶会/顶刊, 200+ 精选论文, 20+ 实验室
> 生成时间: 2026-07-11

---

## 目录

1. [会议概览](#1-会议概览)
2. [ICML 2026 (Seoul, Jul 6-11)](#2-icml-2026)
3. [ICLR 2026 (Rio de Janeiro, Apr 23-27)](#3-iclr-2026)
4. [AAAI 2026 (Singapore, Jan 20-27)](#4-aaai-2026)
5. [NeurIPS 2025 (San Diego, Dec 2-7)](#5-neurips-2025)
6. [CVPR 2026 (Denver, Jun 3-7)](#6-cvpr-2026)
7. [KDD 2026 (Jeju Island, Aug 9-13)](#7-kdd-2026)
8. [ACL 2026 (Jul 2-7)](#8-acl-2026)
9. [EMNLP 2025 (Suzhou, Nov 4-9)](#9-emnlp-2025)
10. [SIGIR 2026 / WWW 2026 / CIKM 2025 / RecSys 2025](#10-recsys-ir)
11. [按实验室分类汇总](#11-lab-summary)
12. [关键趋势总结](#12-trends)

---

## 1. 会议概览

| 会议 | 地点 | 时间 | 投稿数 | 录用数 | 录用率 | Oral率 |
|------|------|------|--------|--------|--------|--------|
| **ICML 2026** | Seoul, Korea | Jul 6-11, 2026 | 23,918 | ~6,500+ | ~27% | 0.7% |
| **ICLR 2026** | Rio de Janeiro, Brazil | Apr 23-27, 2026 | ~19,814 | 5,340 | 26.95% | 1.13% |
| **AAAI 2026** | Singapore | Jan 20-27, 2026 | 23,680 | 4,167 | 17.6% | — |
| **NeurIPS 2025** | San Diego + Mexico City | Dec 2-7, 2025 | 21,575 | 5,290 | 24.52% | — |
| **CVPR 2026** | Denver, CO | Jun 3-7, 2026 | 16,092 | 4,089 | 25.4% | — |
| **KDD 2026** | Jeju Island, Korea | Aug 9-13, 2026 | — | — | — | — |
| **ACL 2026** | — | Jul 2-7, 2026 | — | 2,400+ | — | — |
| **EMNLP 2025** | Suzhou, China | Nov 4-9, 2025 | — | 3,214 | — | — |

---

## 2. ICML 2026

**43rd ICML · Seoul, South Korea · July 6–11, 2026 · 23,918 submissions, ~6,500+ accepted, Oral rate 0.7%**

### 2.1 最佳论文 & Oral Papers

#### ATLAS: Learning to Optimally Memorize the Context at Test Time
- **Title (CN):** ATLAS：在测试时学习最优记忆上下文
- **Authors:** Ali Behrouz, Zeman Li, Praneeth Kacham, Majid Daliri, Yuan Deng, Peilin Zhong, Meisam Razaviyayn, Vahab Mirrokni
- **Affiliation:** Google Research
- **Venue:** ICML 2026 **Oral**
- **Abstract & Innovations:** 提出 ATLAS 用于测试时上下文记忆化,具有理论保证。在测试时动态学习记忆策略,而非预训练固定上下文窗口。突破了 Transformer 固定上下文长度的限制。
- **Link:** https://arxiv.org/pdf/2505.23735

#### DPO Unchained: Your Training Algorithm Is Secretly Disentangled
- **Title (CN):** DPO解链：你的训练算法在人类选择理论中被秘密解耦
- **Authors:** Wenxuan Zhou, Shujian Zhang, Brice Magdalou, John Lambert, Ehsan Amid, Richard Nock, Andrew Hard
- **Affiliation:** Google Research
- **Venue:** ICML 2026 **Oral**
- **Abstract & Innovations:** 对 DPO 训练进行理论分析,揭示了其解耦特性。为理解偏好优化训练提供了新的理论视角。
- **Link:** https://arxiv.org/pdf/2507.07855

#### How Much Do Language Models Memorize?
- **Title (CN):** 语言模型记住了多少？
- **Authors:** John X. Morris, Chawin Sitawarin, Chuan Guo, Narine Kokhlikyan, G. Edward Suh, Alexander M. Rush, Kamalika Chaudhuri, Saeed Mahloujifar
- **Affiliation:** Google Research / Cornell
- **Venue:** ICML 2026 **Oral**
- **Abstract & Innovations:** 量化语言模型中的记忆化程度,提供理论和实证分析。对理解 LLM 的泛化能力与隐私风险具有重要意义。

#### Equivalence of Context and Parameter Updates in Modern Transformer Blocks
- **Title (CN):** 现代Transformer块中上下文与参数更新的等价性
- **Authors:** Adrian Goldwaser, Michael Munn, Xavi Gonzalvo, Benoit Dherin
- **Affiliation:** Google DeepMind
- **Venue:** ICML 2026 **Oral**
- **Abstract & Innovations:** 证明了 Transformer 块中上下文更新与参数更新的理论等价性。为理解 Transformer 的工作机理提供了新视角。
- **Link:** https://arxiv.org/pdf/2511.17864

#### TokSuite: Measuring The Impact Of Tokenizer Choice On Language Model Behavior
- **Title (CN):** TokSuite：衡量分词器选择对语言模型行为的影响
- **Authors:** Gül Sena Altıntaş, Malikeh Ehghaghi, Brian Lester, Fengyuan Liu, Wanru Zhao, Marco Ciccone, Colin Raffel
- **Affiliation:** Google Research
- **Venue:** ICML 2026 **Oral**
- **Abstract & Innovations:** 全面研究分词器选择对 LLM 行为的影响。提供了系统化的评估框架 TokSuite。
- **Link:** https://arxiv.org/pdf/2512.20757

#### Rational Transductors
- **Title (CN):** 有理传导器
- **Authors:** Mehryar Mohri et al.
- **Affiliation:** Google Research
- **Venue:** ICML 2026 **Oral**
- **Abstract & Innovations:** 新型 transducer 框架,提供理论学习保证。

### 2.2 Agent & 研究自动化

#### MARS: Modular Agent With Reflective Search For Automated AI Research
- **Title (CN):** MARS：用于自动化AI研究的反思性搜索模块化智能体
- **Authors:** Jiefeng Chen, Bhavana Dalvi Mishra, Jaehyun Nam, Rui Meng, Tomas Pfister, Jinsung Yoon
- **Affiliation:** Google Research
- **Venue:** ICML 2026
- **Abstract & Innovations:** 模块化 agent 系统用于自动化 AI 研究,集成反思搜索机制。代表 AI for Science 的重要方向。
- **Link:** https://arxiv.org/pdf/2602.02660

#### Toward Generalist Autonomous Research via Hypothesis-Tree Refinement (Arbor)
- **Title (CN):** 通过假设树细化实现通用自主研究
- **Authors:** Microsoft Research
- **Affiliation:** Microsoft Research
- **Venue:** ICML 2026
- **Abstract & Innovations:** Arbor 框架实现自主研究。在 MLE-Bench Lite 上使用 GPT-5.5 达到 86.36%; 在研究任务上超越 Codex 和 Claude Code 2.5 倍。
- **Link:** https://www.microsoft.com/en-us/research/publication/toward-generalist-autonomous-research-via-hypothesis-tree-refinement/

#### RE-TRAC: Recursive Trajectory Compression for Deep Search Agents
- **Title (CN):** RE-TRAC：深度搜索智能体的递归轨迹压缩
- **Authors:** Microsoft Research
- **Affiliation:** Microsoft Research
- **Venue:** ICML 2026
- **Abstract & Innovations:** Agentic 框架进行跨轨迹探索,使用结构化状态表示; 超越 ReAct 15-20%。

### 2.3 高效训练 & 推理

#### ECO: Quantized Training Without Full-Precision Master Weights
- **Title (CN):** ECO：无需全精度主权重的量化训练
- **Authors:** Mahdi Nikdan, Amir Zandieh, Dan Alistarh, Vahab Mirrokni
- **Affiliation:** Google Research
- **Venue:** ICML 2026
- **Abstract & Innovations:** 实现无需全精度主权重的训练,大幅降低内存成本。

#### Beyond Prediction: Tail-Aware Scheduling for LLM Inference
- **Title (CN):** 超越预测：LLM推理的尾部感知调度
- **Affiliation:** Microsoft Research
- **Venue:** ICML 2026
- **Abstract & Innovations:** LLM 推理的尾部感知调度策略,优化服务延迟。

#### Understand and Accelerate Memory Processing Pipeline for LLM Inference
- **Title (CN):** 理解与加速LLM推理的内存处理管线
- **Authors:** Amazon / UCLA collaborators
- **Affiliation:** Amazon / UCLA
- **Venue:** ICML 2026
- **Abstract & Innovations:** 统一 4 步内存处理管线; GPU-FPGA 异构加速; 比 GPU baseline 最快 2.2 倍,能耗降低 4.7 倍。

### 2.4 扩散模型

#### Spectrally-Guided Diffusion Noise Schedules
- **Title (CN):** 频谱引导的扩散噪声调度
- **Authors:** Carlos Esteves, Ameesh Makadia
- **Affiliation:** Google Research
- **Venue:** ICML 2026
- **Abstract & Innovations:** 基于频谱分析的扩散模型新型噪声调度方法。

#### Reinforcement Learning With Discrete Diffusion Policies For Combinatorial Action Spaces
- **Title (CN):** 组合动作空间的离散扩散策略强化学习
- **Authors:** Haitong Ma, Ofir Nabati, Aviv Rosenberg, Bo Dai, Oran Lang, Craig Boutilier, Na Li, Shie Mannor, Lior Shani, Guy Tenneholtz
- **Affiliation:** Google DeepMind
- **Venue:** ICML 2026
- **Abstract & Innovations:** 训练离散扩散模型作为组合设置中的策略; 在 DNA 序列生成和多智能体系统中达到 SOTA。
- **Link:** https://arxiv.org/pdf/2509.22963

#### FUSE: Ensembling Verifiers With Zero Labeled Data
- **Title (CN):** FUSE：零标注数据的验证器集成
- **Authors:** Joonhyuk Lee, Virginia Ma, Sarah Zhao, Yash Nair, Asher Spector, Regev Cohen, Emmanuel Candès
- **Affiliation:** Google Research / Stanford
- **Venue:** ICML 2026
- **Abstract & Innovations:** 无需标注数据即可集成验证模型。
- **Link:** https://arxiv.org/pdf/2604.18547

### 2.5 机器人 & 具身智能

#### DreamDojo: Robot World Models from Human Video
- **Title (CN):** DreamDojo：从人类视频中学习的机器人世界模型
- **Affiliation:** NVIDIA / Google DeepMind
- **Venue:** ICML 2026
- **Abstract & Innovations:** 从人类视频学习物理世界行为; 基于 NVIDIA Cosmos 预测机器人与从未训练过的物体/环境的交互。
- **Link:** https://arxiv.org/abs/2602.06949

### 2.6 安全 & 对齐

#### Modular Pretraining Enables Access Control (GRAM)
- **Title (CN):** 模块化预训练实现访问控制
- **Authors:** Ethan Roland, Murat Cubuktepe, Erick Martinez, Stijn Servaes et al.
- **Affiliation:** AE Studio + Anthropic
- **Venue:** ICML 2026 **Spotlight**
- **Abstract & Innovations:** 引入 Gradient-Routed Auxiliary Modules (GRAM),将危险知识隔离到可切换模块中。单个 GRAM 模型近似多个数据过滤模型 (50M 到 5B 参数)。通过开关模块实现访问控制。
- **Link:** https://alignment.anthropic.com/2026/modular-pretraining/
- **Code:** https://github.com/agencyenterprise/modular-pretraining

#### How Well Do Models Follow Their Constitutions?
- **Title (CN):** 模型在多大程度上遵循其宪法？
- **Affiliation:** Multi-lab (Anthropic/OpenAI specs audited)
- **Venue:** ICML 2026 (AIWIL workshop)
- **Abstract & Innovations:** 对 Anthropic 宪法 (205 条) 和 OpenAI Model Spec 的多方法审计。Claude 系列违规率从 15.0% (Sonnet 4) 降至 2.0% (Sonnet 4.6)。

#### The Deterministic Horizon: When Extended Reasoning Fails
- **Title (CN):** 确定性边界：扩展推理何时失败
- **Authors:** Dongxin Guo, Jikun Wu, Siu Ming Yiu
- **Venue:** ICML 2026
- **Link:** https://arxiv.org/abs/2606.00376

### 2.7 其他 ICML 2026 重要论文

| 论文 | 机构 | 创新点 | 链接 |
|------|------|--------|------|
| **TCEC** (Spotlight+Oral, Top 0.7%) | ByteDance Seed / NVIDIA | 量化扩散的误差传播机制与补偿策略 | arXiv |
| **BitDance** | ByteDance + CUHK + SJTU | 用二值token扩展自回归生成模型; FID 1.24; 30x加速 | [2602.14041](https://arxiv.org/abs/2602.14041) |
| **MotionCache** | ByteDance Seed | 运动感知缓存的高效自回归视频生成 | arXiv |
| **DualSparse-MoE** | ByteDance | MoE 架构中 tensor/neuron 级稀疏性协调 | arXiv |
| **D³** | Microsoft Research | LLM训练的动态方向图约束数据调度 | arXiv |
| **Breaking Dual Bottlenecks** | Tencent WeChat Vision + SJTU | 多模态模型演进为自适应视觉推理器 | ICML 2026 |
| **SAI** (Position Paper) | Meta AI / NYU / Columbia (LeCun) | 超人适应性智能作为 AGI 替代方案 | ICML 2026 |
| **Rethinking LLM Ensembling** (Spotlight) | NTU / Data61 | ME (混合模型式集成) 质量等价, 1.78-2.68x 加速 | [2605.00419](https://arxiv.org/abs/2605.00419) |
| **ProbeLLM** | IBM Research + 多机构 | 层次化 MCTS 的 LLM 故障系统化诊断 | [2602.12966](https://arxiv.org/abs/2602.12966) |
| **SAGE** | — | 推理模型隐含地知道何时停止思考; SAGE-RL 持续减少 CoT 长度 | [2602.08354](https://arxiv.org/abs/2602.08354) |
| **D-ARL** | ByteDance (Volcengine) | 分布匹配异步 RL 用于 LLM 后训练 | [GitHub](https://github.com/YinqiBai962/D-ARL) |
| **Stop Automating Peer Review** (Spotlight) | — | 在没有严格评估的情况下停止自动化同行评审 | [2605.03202](https://arxiv.org/abs/2605.03202) |

---

## 3. ICLR 2026

**ICLR 2026 · Rio de Janeiro, Brazil · April 23–27, 2026 · ~19,814 submissions, 5,340 accepted (26.95%), 223 oral (1.13%)**

### 3.1 杰出论文奖 (Outstanding Papers)

#### Transformers are Inherently Succinct
- **Title (CN):** Transformer 本质上是简洁的
- **Authors:** Pascal Bergsträßer, Ryan Cotterell, Anthony Widjaja Lin
- **Affiliation:** ETH Zürich / University of Bristol
- **Venue:** ICLR 2026 **Outstanding Paper**
- **Abstract & Innovations:** 证明 Transformer 可以比有限自动机和 LTL 公式指数级更简洁地表示形式语言。验证 Transformer 属性是 EXPSPACE-complete。为理解 Transformer 表达能力提供了新的理论透镜。
- **Link:** https://openreview.net/forum?id=Yxz92UuPLQ

#### LLMs Get Lost In Multi-Turn Conversation
- **Title (CN):** LLM 在多轮对话中会迷失
- **Authors:** Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville
- **Affiliation:** Microsoft Research
- **Venue:** ICLR 2026 **Outstanding Paper**
- **Abstract & Innovations:** 大规模模拟表明所有测试的 LLM (GPT-4o, Claude 3.7 Sonnet, Gemini 2.5 Pro, Llama 3 等) 在多轮设置中性能**下降约 39%**。模型做出早期假设且无法恢复。提供了可扩展的诊断方法。
- **Link:** https://openreview.net/forum?id=VKGTGGcwl6 | arXiv: [2505.06120](https://arxiv.org/abs/2505.06120)

#### The Polar Express (Honorable Mention)
- **Title (CN):** 极地快车：最优矩阵符号方法及其在 Muon 算法中的应用
- **Authors:** Noah Amsel, David Persson, Christopher Musco, Robert M. Gower
- **Affiliation:** NYU / Meta AI
- **Venue:** ICLR 2026 **Honorable Mention**
- **Abstract & Innovations:** 最优矩阵符号计算方法,应用于 Muon 优化器,推进高效大规模优化。
- **Link:** https://openreview.net/forum?id=yRtgZ1K8hO

### 3.2 精选 Oral Papers

| 论文 | 机构 | 创新点 | 链接 |
|------|------|--------|------|
| **Di3PO** | Google DeepMind | DPO 用于扩散模型,通过 diptych 训练进行定向改进 | [2602.06355](https://arxiv.org/abs/2602.06355) |
| **Mamba-3** | Together AI / Princeton | 第三代 Mamba 架构,更表达性的递归、复数状态更新、MIMO 公式 | OpenReview |
| **Why DPO is Misspecified** | — | DPO 有设定错误的理论证明,提出修复方案 | OpenReview |
| **Energy-Based Transformers** | — | 基于能量的 Transformer,通过能量最小化实现隐式推理 | OpenReview |
| **MoE Can Surpass Dense LLMs** | ByteDance-affiliated | 严格等资源条件下 MoE 超越稠密 LLM | OpenReview |
| **TileLang** | — | DSL 编写融合 attention 内核,H100 上 5x 超越 Triton,AMD 6x; 代码量减少 90% | OpenReview |
| **Planner Aware Path Learning (PAPL)** | Google DeepMind | 修复扩散语言模型的训练-推理不匹配 | OpenReview |
| **LoongRL** | ByteDance-affiliated | RL 训练 LLM 在超长上下文中推理 | OpenReview |
| **Speculative Actions** | — | 将推测解码应用于 agent 动作预测,实现无损加速 | OpenReview |
| **NextStep-1** | ByteDance Seed | 连续 token 的大规模自回归图像生成 | OpenReview |
| **SANA-Video** | NVIDIA | 块线性 Diffusion Transformer 的高效视频生成 | OpenReview |
| **Depth Anything 3** | TikTok / ByteDance | 单目/多视图深度估计基础模型,第三代 | OpenReview |
| **Hubble** | — | 推进 LLM 记忆研究的模型套件和基准 | OpenReview |
| **Pre-training under Infinite Compute** | — | 无限算力下的预训练 Scaling Laws 理论与实证 | OpenReview |
| **The Coverage Principle** | — | 预训练如何赋能后训练的理论框架 | OpenReview |
| **Common Corpus** | Hugging Face / Partnership on AI | 最大伦理 LLM 预训练语料库 | OpenReview |
| **OpenThoughts** | — | 推理模型训练的数据配方 | OpenReview |

### 3.3 实验室特色论文

#### Google DeepMind @ ICLR 2026
- Di3PO (DPO for diffusion), PAPL (planner-aware diffusion LM), Image Generators as Vision Learners, Efficient RL Guiding World Models (102.8% improvement across 72 tasks)

#### Meta AI @ ICLR 2026
- The Polar Express (Honorable Mention), FERRET (multimodal red-teaming), UniT (multimodal CoT TTS)

#### Microsoft Research @ ICLR 2026
- LLMs Get Lost In Multi-Turn (Outstanding), LLM Fingerprinting via Watermarks (Chain & Hash), Forward-Learned Discrete Diffusion, Parallel Sampling from Masked Diffusion

#### NVIDIA @ ICLR 2026
- SANA-Video (efficient video generation), TileLang (5x Triton), VideoNSA (native sparse attention for video)

---

## 4. AAAI 2026

**AAAI 2026 · Singapore · January 20–27, 2026 · 23,680 submissions, 4,167 accepted (17.6%)**

### 4.1 杰出论文奖 (7 papers)

#### LLM2CLIP (Outstanding Paper)
- **Title (CN):** LLM2CLIP：强大的语言模型解锁更丰富的跨模态表征
- **Authors:** Weiquan Huang, Aoqi Wu, Yifan Yang, Xufang Luo, Yuqing Yang, Liang Hu, Qi Dai, Chunyu Wang, Xiyang Dai, Dongdong Chen, Chong Luo, Lili Qiu
- **Affiliation:** Microsoft Research / Tongji University
- **Venue:** AAAI 2026 **Outstanding Paper**
- **Abstract & Innovations:** 两阶段框架将 vanilla LLM (Llama3) 微调为判别式嵌入模型,通过对比学习,然后与预训练 CLIP 视觉编码器耦合。SigLIP-2 零样本检索在长标题上提升 +14.8/+15.8,多语言任务 +11.9/+15.2。
- **arXiv:** [2411.04997](https://arxiv.org/abs/2411.04997)
- **Code:** https://github.com/microsoft/LLM2CLIP (670 stars)

#### ReconVLA (Outstanding Paper)
- **Title (CN):** ReconVLA：重建式视觉-语言-动作模型作为有效的机器人感知器
- **Authors:** Wenxuan Song, Ziyang Zhou, Han Zhao et al.
- **Affiliation:** HKUST(GZ), Westlake University, Zhejiang University
- **Venue:** AAAI 2026 **Outstanding Paper**
- **Abstract & Innovations:** 集成轻量级扩散 Transformer 从噪声重建潜在"注视区域",让 VLA 模型隐式学习注视位置。长 horizon 操作高达 85% 成功率,显著超越 OpenVLA 和 GraspVLA。
- **arXiv:** [2508.10333](https://arxiv.org/abs/2508.10333)

### 4.2 大厂论文

#### Microsoft Research @ AAAI 2026
| 论文 | 创新点 |
|------|--------|
| **GENMAC** | 多智能体协作的组合式文本到视频生成 |
| **JUPITER** | 基于蒙特卡洛树搜索的LLM数据分析; NbQA (38,635 pairs from 1.6M notebooks) |
| **HTSIR** | 层级两阶段摘要的信息检索; 四个长文本基准 SOTA |

#### Amazon @ AAAI 2026
| 论文 | 创新点 |
|------|--------|
| **COREA** | 置信度校准的大小模型协作; ~21.5% 推理成本降低 |
| **PRECISE** | 减少LLM评估偏差; 仅100个人类标注即可统计可靠 |
| **CausalFusion** | LLM与图证伪的因果发现; 超越经典算法 |
| **Temporal-Consistent Video** | 基于预训练扩散模型的时间一致性视频修复 |
| **NCLMCTT** | 神经编解码语言模型的零样本音色迁移 |

#### Huawei @ AAAI 2026
| 论文 | 创新点 |
|------|--------|
| **SemanticVLA** | 语义对齐的视觉-语言-动作模型; 超越 OpenVLA 21.1%, 3x 更少训练成本 |

#### Alibaba / ByteDance @ AAAI 2026
| 论文 | 创新点 |
|------|--------|
| **Video SimpleQA** (Alibaba + ByteDance) | 视频语境事实性评估的首个综合基准 |

#### Meituan @ AAAI 2026
| 论文 | 创新点 |
|------|--------|
| **MACRec** (Oral) | 用于生成式推荐的多方面跨模态量化 | [2511.15122](https://arxiv.org/abs/2511.15122) |

### 4.3 AAAI 2026 特别项目

#### AI-Assisted Peer Review at Scale
- **Affiliation:** AAAI + OpenAI (GPT-5 sponsored) + multiple universities
- **Venue:** AAAI 2026
- **Abstract & Innovations:** 首个大规模 AI 辅助同行评审部署: 22,977 篇论文在 24 小时内由 AI 审稿, 每篇成本 < $1。使用 5 步管线 (Story → Presentation → Evaluations → Correctness → Significance)。调查 5,834 位受访者; AI 审稿在 9 个质量维度中 6 个超越人类。
- **arXiv:** [2604.13940](https://arxiv.org/abs/2604.13940)

---

## 5. NeurIPS 2025

**NeurIPS 2025 · San Diego + Mexico City · December 2–7, 2025 · 21,575 submissions, 5,290 accepted (24.52%)**

### 5.1 最佳论文

#### Gated Attention for Large Language Models (Best Paper)
- **Title (CN):** 门控注意力机制：非线性、稀疏性与无注意力汇聚
- **Authors:** Zihan Qiu et al. (Qwen Team)
- **Affiliation:** Alibaba (Qwen / 通义千问)
- **Venue:** NeurIPS 2025 **Best Paper**
- **Abstract & Innovations:** LLM 中注意力门控的首次系统研究。在 SDPA 后添加 head-specific sigmoid 门控。在 1.7B dense 和 15B MoE 模型 (3.5T tokens) 上比较 30+ 门控变体。降低困惑度 0.05-0.27, 抑制训练 loss spikes, 大幅减少 attention sink (BOS token attention: 46.7% → 4.8%)。仅增加 1% 参数。已纳入 **Qwen3-Next**。
- **arXiv:** [2505.06708](https://arxiv.org/abs/2505.06708)
- **Code:** https://github.com/qiuzh20/gated_attention

#### Artificial Hivemind (Best Paper, Datasets & Benchmarks)
- **Title (CN):** 人工蜂巢思维：语言模型的开放式同质性
- **Authors:** Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Yejin Choi
- **Affiliation:** UW, CMU, AI2, Stanford
- **Venue:** NeurIPS 2025 **Best Paper**
- **Abstract & Innovations:** 引入 Infinity-Chat 数据集 (26K 开放式查询 + 31K+ 人类标注),评估 70+ LLM 输出多样性。发现强烈的模型内重复和模型间同质性("人工蜂巢思维")。当前奖励模型与个人偏好和多元化不匹配。
- **arXiv:** [2510.22954](https://arxiv.org/abs/2510.22954)
- **Code:** https://github.com/liweijiang/artificial-hivemind

#### 1000 Layer Networks for Self-Supervised RL (Best Paper)
- **Title (CN):** 千层网络自监督强化学习
- **Authors:** Kevin Wang, Ishaan Javali, Michał Bortkiewicz, Tomasz Trzcinski, Benjamin Eysenbach
- **Affiliation:** CMU
- **Venue:** NeurIPS 2025 **Best Paper**
- **Abstract & Innovations:** 证明自监督 RL agent 使用多达 **1024 层** 无需显式奖励或演示即可实现强目标到达。使用对比、目标条件自监督。性能比基线提升 2x-50x。

#### Why Diffusion Models Don't Memorize (Best Paper)
- **Title (CN):** 为什么扩散模型不会过拟合
- **Venue:** NeurIPS 2025 **Best Paper**
- **Abstract & Innovations:** 证明扩散模型在训练中表现出隐式正则化,防止记忆化。

### 5.2 最佳论文Runner-up

| 论文 | 创新点 |
|------|--------|
| **RL Really Incentivize Reasoning?** (Runner-up) | RLVR 方法提高采样效率但不产生根本新推理模式; 蒸馏才能真正扩展能力 |
| **Superposition Yields Robust Neural Scaling** (Runner-up, Oral) | 用表示叠加解释神经缩放定律; 与 Anthropic 合作 (Ziming Liu) |
| **Optimal Mistake Bounds** (Runner-up) | 解决了 30 年开放问题,传导式学习实现二次优势 |

### 5.3 实验室特色论文

#### Google Research @ NeurIPS 2025 (175 accepted)
| 论文 | 创新点 |
|------|--------|
| **Titans** | 神经长期记忆模块,处理 2M+ 上下文; 三种架构变体 (MAC/MAG/MAL) | [2501.00663](https://arxiv.org/abs/2501.00663) |
| **Nested Learning** | 嵌套学习范式,将 ML 模型表示为多级并行优化问题 | [2512.24695](https://arxiv.org/abs/2512.24695) |
| **MIRAS** | 泛化 Titans 方法,设计测试时记忆的序列建模架构 | [2504.13173](https://arxiv.org/abs/2504.13173) |

#### Meta FAIR @ NeurIPS 2025
| 论文 | 创新点 |
|------|--------|
| **Perception Encoder** (Oral) | 对比视觉-语言训练可产生 SOTA 嵌入; 但最佳特征在中间层; 2B参数模型; 86.6 ImageNet | [2504.13181](https://arxiv.org/abs/2504.13181) |

#### ByteDance @ NeurIPS 2025
| 论文 | 创新点 |
|------|--------|
| **SALMONN-omni** | 首个无需 Codec 注入的全双工语音 LLM; 30%+ 提升 | [GitHub](https://github.com/bytedance/SALMONN) |
| **Q-Insight** (Spotlight) | 视觉 RL 的图像质量理解 | arXiv |
| **Repo2Run** | LLM agent 自动化构建可执行测试环境; 420 Python repos | arXiv |

#### Microsoft Research @ NeurIPS 2025 (150+ accepted)
| 论文 | 创新点 |
|------|--------|
| **Machine Unlearning** (Oral) | 挑战机器遗忘的常见假设,生成式AI政策启示 | — |
| **Lost in Transmission** | LLM 全局推理失败模式分析 | — |
| **Numerical Nondeterminism** (Oral) | 缓解 LLM 推理中数值不确定性 | — |

#### Tsinghua / UCAS @ NeurIPS 2025
| 论文 | 创新点 |
|------|--------|
| **Tensor Product Attention** (Spotlight) | 张量分解紧凑表示 Q/K/V,大幅缩小 KV cache; 超越 MHA/MQA/GQA/MLA | [2501.06425](https://arxiv.org/abs/2501.06425) |

---

## 6. CVPR 2026

**CVPR 2026 · Denver, CO · June 3–7, 2026 · 16,092 submissions, 4,089 accepted**

### 6.1 最佳论文

#### D4RT: Efficiently Reconstructing Dynamic Scenes (Best Paper)
- **Title (CN):** D4RT：高效重建动态场景
- **Authors:** Chuhan Zhang, Guillaume Le Moing, Skanda Koppula et al.
- **Affiliation:** Google DeepMind, UCL, Oxford
- **Venue:** CVPR 2026 **Best Paper**
- **Abstract & Innovations:** 统一 Transformer 架构从普通视频重建动态 4D 场景。同时估计深度、时空对应和完整相机参数。推理速度 200+ FPS, 比 VGGT 快 9 倍, 比 MegaSaM 快 100 倍。
- **arXiv:** [2512.08924](https://arxiv.org/abs/2512.08924)

#### NitroGen (Best Paper Honorable Mention)
- **Title (CN):** NitroGen：通用游戏智能体的开放基础模型
- **Authors:** Loïc Magne, Anas Awadalla, Guanzhi Wang et al.
- **Affiliation:** NVIDIA, Stanford, Caltech, UT Austin
- **Venue:** CVPR 2026 **Honorable Mention**
- **Abstract & Innovations:** 视觉-动作基础模型,基于 40,000 小时游戏视频 (1,000+ 款游戏) 训练,零样本泛化任务成功率最高提升 52%。由 NVIDIA 研究员 Jim Fan 领衔。

#### SAM 3D (Best Paper Honorable Mention)
- **Title (CN):** SAM 3D：3Dfy Anything in Images
- **Affiliation:** Meta Superintelligence Labs
- **Venue:** CVPR 2026 **Honorable Mention**
- **Abstract & Innovations:** SAM 系列 3D 扩展,从单张图像预测物体几何、纹理和布局。人类偏好测试中对真实物体胜率至少 5:1。

#### CLAY (Best Student Paper)
- **Title (CN):** CLAY：原生结构化潜在空间用于3D生成
- **Affiliation:** Tsinghua, Microsoft Research, CAS, Microsoft AI
- **Venue:** CVPR 2026 **Best Student Paper**
- **Abstract & Innovations:** O-Voxel 新型表示 + 40 亿参数 flow matching 模型,生成的 3D 资产质量远超现有方法。

### 6.2 Google DeepMind @ CVPR 2026

| 论文 | 创新点 |
|------|--------|
| **TIPSv2** | 增强 patch-text 对齐的基础视觉-语言预训练 | [2604.12012](https://arxiv.org/abs/2604.12012) |
| **BlazeEdit** | 195M 参数设备端图像编辑, Pixel 10 上仅 290ms |
| **Project Genie** | 实验性无限交互世界生成器 |
| **OVI-MAP** | 开放词汇实例-语义映射 | [2603.26541](https://arxiv.org/abs/2603.26541) |
| **CURVE** | 文化和多语言长视频推理基准 | [2601.10649](https://arxiv.org/abs/2601.10649) |
| **VISTA** | 测试时自我改进的视频生成 Agent | [2510.15831](https://arxiv.org/abs/2510.15831) |

---

## 7. KDD 2026

**KDD 2026 · Jeju Island, Korea · August 9–13, 2026**

### 7.1 重点论文

#### Kunlun: Scaling Laws for Massive-Scale Recommendation Systems (Meta)
- **Title (CN):** Kunlun：大规模推荐系统的可预测Scaling Laws
- **Authors:** Meta Platforms (31 位作者) + OpenAI
- **Affiliation:** Meta + OpenAI
- **Venue:** KDD 2026
- **Abstract & Innovations:** 提出可扩展架构 Kunlun,建立大规模推荐系统的可预测 Scaling Laws。通过 GDPA, HSP, Sliding Window Attention 等优化,以及 Computation Skip 和 Event-level Personalization。MFU 从 17% 提升至 37% (NVIDIA B200), Scaling 效率提升 2 倍。已部署于 Meta 主要广告模型,topline 指标提升 1.2%。
- **arXiv:** [2602.10016](https://arxiv.org/abs/2602.10016)

#### CausalMoE: Billion-Scale Multimodal Foundation Model for Granger Causal Discovery
- **Title (CN):** CausalMoE：十亿级多模态Granger因果基础模型
- **Affiliation:** Tencent (腾讯)
- **Venue:** KDD 2026
- **Abstract & Innovations:** Pattern-Routed Mixture of Heterogeneous Experts (MoHE),首次将 LLM 和 VLM 整合到因果发现循环中。
- **arXiv:** [2606.13024](https://arxiv.org/abs/2606.13024)

#### AIGP: LLM-Based Framework for Long-Term Value Alignment in E-Commerce Pricing
- **Title (CN):** AIGP：基于LLM的电子商务定价长期价值对齐框架
- **Affiliation:** Alibaba (淘宝 & 天猫)
- **Venue:** KDD 2026
- **arXiv:** [2606.26787](https://arxiv.org/abs/2606.26787)

#### DeGRe: Dense-supervised Generative Reranking for Recommendation
- **Title (CN):** DeGRe：密集监督的生成式重排序
- **Affiliation:** Alibaba (淘宝) + 浙江大学
- **arXiv:** [2605.25749](https://arxiv.org/abs/2605.25749)

#### FlowTime: Continuous Generative Watch Time Prediction
- **Title (CN):** FlowTime：基于 Flow 个性化先验的连续生成式观看时长预测
- **Affiliation:** Kuaishou (快手) + 复旦大学
- **arXiv:** [2606.01352](https://arxiv.org/abs/2606.01352)

---

## 8. ACL 2026

**ACL 2026 · July 2–7, 2026 · 2,400+ papers accepted**

### 8.1 重点论文

#### Think in Sentences
- **Title (CN):** 在句子中思考
- **Authors:** Zhichen Liu, Yongyuan Li, Yang Xu
- **Venue:** ACL 2026 Main
- **Abstract & Innovations:** 在 LLM 中显式插入句子边界标记,提升多种任务表现。
- **arXiv:** [2604.10135](https://arxiv.org/abs/2604.10135)

#### Thinking with Reasoning Skills: Fewer Tokens, More Accuracy (Industry Track)
- **Title (CN):** 用推理技能思考：更少Token,更高准确率
- **Affiliation:** Industry
- **Venue:** ACL 2026 Industry Track
- **Abstract & Innovations:** 从长链推理中蒸馏"可复用推理技能"作为检索引导的捷径。编程和数学任务上 token 减少 30-40% 同时提升准确率。
- **arXiv:** [2604.21764](https://arxiv.org/abs/2604.21764)

#### WebAnchor (Findings)
- **Title (CN):** WebAnchor：锚定Agent规划以稳定长horizon Web推理
- **Affiliation:** Alibaba (通义实验室) + 哈工大
- **Venue:** ACL 2026 Findings
- **Abstract & Innovations:** 发现"Plan Anchor"现象 — 第一步推理对长期 web 推理影响不成比例。Anchor-GRPO 两阶段 RL 框架。WebAnchor-30B 在 BrowseComp 达 46.0% pass@1, GAIA 达 76.4%。

#### GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR
- **Title (CN):** GeoRA：面向RLVR的几何感知低秩自适应
- **Affiliation:** Meituan
- **Venue:** ACL 2026
- **Abstract & Innovations:** 专为 RLVR 设计的几何感知 LoRA; 在 Qwen3-8B 和 Llama-3.1-8B 上持续优于 MiLoRA, PiSSA, LoRA。

#### DEEPPLANNER (Findings)
- **Title (CN):** DEEPPLANNER：通过优势塑造扩展深度研究代理的规划能力
- **Affiliation:** Industry (ByteDance Seed 引用)
- **Venue:** ACL 2026 Findings
- **Abstract & Innovations:** 优势塑造的端到端 RL 框架。3,072 queries × 8 rollouts 达 SOTA; 前代需 10x 训练样本。

---

## 9. EMNLP 2025

**EMNLP 2025 · Suzhou, China · November 4–9, 2025 · 3,214 papers (1,809 Main + 1,405 Findings)**

### 9.1 重点论文

| 论文 | 机构 | 创新点 |
|------|------|--------|
| **Improving Neutral POV with PE-RLHF** | Google DeepMind + Google | 数据和参数高效的 RLHF 方法用于中立文本生成 |
| **DeepResearcher** | 上海交通大学 | 通过真实环境中的 RL 扩展深度研究能力 | [2504.03160](https://arxiv.org/abs/2504.03160) |
| **OmniThink** | Alibaba (通义) | 通过思维机制扩展机器写作的知识边界 |
| **Audio-Aware LLM Judges** | Microsoft Research + NTU | 音频感知 LLM 作为说话风格评判者 |
| **CODI** | — | 将 CoT 压缩到连续空间,通过自蒸馏减少推理开销 |
| **On Domain-Adaptive Post-Training for MLLMs** | Microsoft Research Asia | 多模态 LLM 的域自适应后训练 |
| **Bag of Tricks for Sparse MoE** | — | 稀疏 MoE 高效训练技巧基准测试 |
| **Toolscaler** | — | 可扩展的生成式工具调用 |

---

## 10. SIGIR 2026 / WWW 2026 / CIKM 2025 / RecSys 2025

### 10.1 SIGIR 2026 (Melbourne, Jul 20-24, 2026)

#### L2Rec: Dual-View Understanding of LLMs for Personalized Recommendation
- **Title (CN):** L2Rec：面向个性化推荐的LLM双视图理解
- **Affiliation:** Large-scale social platform (~1.5M DAU)
- **Venue:** SIGIR '26
- **Abstract & Innovations:** 通过 Dual-view Personalized MoE (DPMoE) 在 LLM 参数级别统一行为和语义理解。仅更新 32M 参数 (~5% backbone)。在线 A/B: **+9.24% CTR, +3.15% 回复率**。
- **arXiv:** [2605.26717](https://arxiv.org/abs/2605.26717)

#### SIDReasoner
- **Title (CN):** 在语义ID上进行推理增强生成式推荐
- **Affiliation:** Alibaba-affiliated
- **Venue:** SIGIR '26
- **Abstract & Innovations:** 两阶段框架: (1) 多任务 SID-语言对齐; (2) GRPO RL 自探索 SID 上的推理模式。强跨域泛化能力。
- **arXiv:** [2603.23183](https://arxiv.org/abs/2603.23183)

#### SIGMA (AliExpress)
- **Title (CN):** SIGMA：阿里速卖通基于语义的指令驱动生成式多任务推荐
- **Affiliation:** Alibaba/AliExpress
- **Venue:** SIGIR '26

### 10.2 WWW 2026 (Dubai, Apr 13-17, 2026)

| 论文 | 创新点 |
|------|--------|
| **CARE** | 通过级联排序将推理引入生成式推荐; 改进准确率和多样性 | [2602.03692](https://arxiv.org/abs/2602.03692) |
| **GenCI** | 基于兴趣队列的生成式用户兴趣迁移建模用于 CTR | [2601.18251](https://arxiv.org/abs/2601.18251) |
| **From Token to Item** | 物品感知注意力机制增强 LLM 推荐 | [2603.19693](https://arxiv.org/abs/2603.19693) |

### 10.3 CIKM 2025 (Seoul, Nov 10-14, 2025)

| 论文 | 创新点 |
|------|--------|
| **ORCA** (Huawei Noah's Ark) | 因果解耦框架缓解多任务停留时长预测的过度依赖 | [2508.16573](https://arxiv.org/abs/2508.16573) |
| **KSER** (Alibaba/Tencent) | 从LLM中选择和利用高质量知识用于推荐 | [2508.07223](https://arxiv.org/abs/2508.07223) |

### 10.4 RecSys 2025 (Prague, Sep 22-26, 2025)

| 论文 | 创新点 |
|------|--------|
| **Semantic IDs for Joint Search & Rec** | 为搜索和推荐联合构建有效语义 ID | [2508.10478](https://arxiv.org/abs/2508.10478) |
| **eSASRec** (Yandex) | 模块化增强 Transformer 推荐; 比 SOTA 提升 23% | [2508.06450](https://arxiv.org/abs/2508.06450) |
| **DiffuMIN** (Kuaishou) | 首个将扩散模型应用于用户兴趣建模; 在线 +1.52% CTR | [2508.15311](https://arxiv.org/abs/2508.15311) |
| **CTR Scaling Laws** | 探索 CTR 模型的缩放定律以提升在线性能 | [2508.15326](https://arxiv.org/abs/2508.15326) |

---

## 10.5 工业部署论文 (CTR / RecSys / Advertising)

### 已部署系统论文

| 论文 | 机构 | 关键创新 | 部署效果 |
|------|------|---------|---------|
| **EST** | Alibaba/Taobao | 统一建模 + 轻量交叉注意力 + 内容稀疏注意力; 功率律缩放 | +3.27% RPM, +1.22% CTR | [2602.10811](https://arxiv.org/abs/2602.10811) |
| **FAT** | Alibaba/Taobao (KDD 2026) | 字段感知注意力分解 + 基复合超网络; 首个 CTR 形式化缩放定律 | +2.33% CTR, +0.66% RPM | [2511.12081](https://arxiv.org/abs/2511.12081) |
| **PRECTR-V2** | Alibaba Xianyu | 搜索相关性 + CTR 统一; 冷启动个性化挖掘 | +1.39% 订单, +3.18% GMV | [2602.20676](https://arxiv.org/abs/2602.20676) |
| **OneRanker** | Tencent/WeChat | 价值感知多任务解耦 + 因果掩码 + 分布一致性约束 | +1.34% GMV | [2603.02999](https://arxiv.org/abs/2603.02999) |
| **GR4AD** | Kuaishou | UA-SID (MLLM) + LazyAR 解码器 + RSPO 排名引导 RL | +4.2% 广告收入 | [2602.22732](https://arxiv.org/abs/2602.22732) |
| **DeRes** | TikTok/ByteDance | 双路径层间连接器; 8层匹配16层 OneTrans 性能 | ~2x 算力节省 | [2606.07980](https://arxiv.org/abs/2606.07980) |
| **IDProxy** | Xiaohongshu (小红书) | MLLM 生成冷启动物品代理嵌入 + 粗到细适配器 | 新物品 AUC +0.23%-0.32% | [2603.01590](https://arxiv.org/abs/2603.01590) |
| **UniRec** | Shopee | Chain-of-Attribute 前缀 SID + RFT+DPO | +5.37% PVCTR, +5.60% GMV | [2604.12234](https://arxiv.org/abs/2604.12234) |
| **OneRec** | Kuaishou | 首个端到端生成式推荐超越级联系统; Encoder-decoder + sparse MoE | +1.6% 观看时长 | [2502.18965](https://arxiv.org/abs/2502.18965) |
| **OneRec-Think** | Kuaishou | 生成式推荐中的文本内推理 + Itemic Alignment | +0.159% APP 停留时长 | [2510.11639](https://arxiv.org/abs/2510.11639) |
| **EMER** | Kuaishou | 端到端多目标集成排序替代手工启发式公式 | +1.39% APP 停留时长 | [2508.05093](https://arxiv.org/abs/2508.05093) |
| **CADET** | Amazon | Decoder-only Transformer 用于广告 CTR + 上下文条件 | arXiv | [2602.11410](https://arxiv.org/abs/2602.11410) |
| **DS-MLP** | Meituan / RUC | 双流 MLP + 知识蒸馏; 简单结构达到 SOTA | TKDD 2026 | [2606.04944](https://arxiv.org/abs/2606.04944) |
| **LoopCTR** | — | 循环缩放 (train-multi-loop, infer-zero-loop) + MoE | arXiv | [2604.19550](https://arxiv.org/abs/2604.19550) |
| **ML-DCN** | Pinterest | 掩码低秩深度交叉网络 | arXiv | [2602.09194](https://arxiv.org/abs/2602.09194) |
| **L2Rec** | Social Platform | DPMoE 双视图 LLM 推荐 | +9.24% CTR | [2605.26717](https://arxiv.org/abs/2605.26717) |

---

## 11. 按实验室分类汇总

### Google DeepMind
- **ICML 2026:** 130+ papers, 6 Orals (ATLAS, DPO Unchained, Rational Transductors, How Much Memorize, Equivalence, TokSuite)
- **ICLR 2026:** Di3PO (Oral), PAPL (Oral), Efficient RL Guiding World Models (+102.8%)
- **NeurIPS 2025:** 175 papers; Titans, Nested Learning, MIRAS
- **CVPR 2026:** D4RT (Best Paper), TIPSv2, BlazeEdit, VISTA
- **Research focus:** Test-time memorization, world models, attention gating, scaling laws

### OpenAI
- **ICML 2026:** Short proofs in combinatorics (entirely AI-generated), SWE-Bench Pro, SciPredict, SpreadsheetArena
- **AAAI 2026:** Sponsored AI peer review pilot (GPT-5)
- **Research focus:** Mathematical discovery, agent benchmarks, AI-assisted peer review

### Meta AI
- **ICML 2026:** SAI position paper (LeCun, alternative to AGI)
- **ICLR 2026:** The Polar Express (Honorable Mention, Muon optimizer)
- **NeurIPS 2025:** Perception Encoder (Oral, SOTA embeddings)
- **CVPR 2026:** SAM 3D (Honorable Mention)
- **KDD 2026:** Kunlun (Scaling Laws for RecSys, deployed at Meta)
- **Research focus:** Visual embeddings, MoE scaling, recommendation scaling laws

### Microsoft Research
- **ICML 2026:** Arbor (86.36% MLE-Bench), RE-TRAC (+15-20% vs ReAct), D³, Tail-Aware Scheduling
- **ICLR 2026:** LLMs Get Lost In Multi-Turn (Outstanding), LLM Fingerprinting
- **AAAI 2026:** LLM2CLIP (Outstanding), GENMAC, JUPITER, HTSIR
- **NeurIPS 2025:** 150+ papers; Machine Unlearning, Lost in Transmission
- **CVPR 2026:** CLAY (Best Student Paper)
- **Research focus:** Multi-turn LLM failure, autonomous research, cross-modal learning

### ByteDance / TikTok
- **ICML 2026:** TCEC (Spotlight+Oral), MotionCache, BitDance, DualSparse-MoE, D-ARL
- **ICLR 2026:** NextStep-1 (Oral), Depth Anything 3 (Oral), LoongRL (Oral), MoE Can Surpass Dense
- **NeurIPS 2025:** SALMONN-omni, Q-Insight (Spotlight), Repo2Run
- **RecSys/CTR:** DeRes, HyFormer, MixFormer, OneTrans, TokenMixer-Large
- **Research focus:** Autoregressive generation, depth estimation, efficient CTR, multi-modal

### Alibaba (Qwen)
- **NeurIPS 2025:** Gated Attention (**Best Paper**, incorporated into Qwen3-Next)
- **AAAI 2026:** Video SimpleQA
- **KDD 2026:** AIGP (e-commerce pricing), DeGRe (generative reranking)
- **ACL 2026:** WebAnchor (Plan Anchor + GRPO)
- **CTR/RecSys:** EST, FAT, PRECTR-V2, SIDReasoner
- **Research focus:** Attention gating, generative recommendation, e-commerce AI

### Anthropic
- **ICML 2026:** GRAM (Spotlight, access control via modular pretraining), Constitution audit
- **NeurIPS 2025:** Superposition paper co-author (Ziming Liu)
- **Research focus:** Alignment, safety, access control, interpretability

### NVIDIA
- **ICML 2026:** 74 papers; DreamDojo (robot world models), Cosmos 3, BioNeMo
- **ICLR 2026:** SANA-Video (Oral), TileLang (Oral, 5x Triton)
- **CVPR 2026:** NitroGen (Honorable Mention, 1000+ games)
- **NeurIPS 2025:** Alpamayo-R1 (autonomous driving)
- **Research focus:** Robotics, video generation, game foundation models, efficient kernels

### Amazon
- **ICML 2026:** Scalable multi-agent (Oral), LLM memory pipeline (2.2x faster)
- **AAAI 2026:** COREA, PRECISE, CausalFusion, Temporal-Consistent Video, NCLMCTT
- **NeurIPS 2025:** CodeAssistBench
- **RecSys:** CADET (ads CTR)
- **Research focus:** LLM evaluation, causal discovery, multi-agent systems

### Kuaishou (快手)
- **KDD 2026:** FlowTime
- **RecSys 2025:** DiffuMIN (+1.52% CTR), CTR Scaling Laws
- **Industrial:** GR4AD (+4.2% ad revenue), OneRec (+1.6% watch time), OneRec-Think, EMER (+1.39% stay time)
- **Research focus:** Generative recommendation, RL-based ranking, multi-objective optimization

### Tencent (腾讯)
- **ICML 2026:** Breaking Dual Bottlenecks (multimodal reasoning)
- **KDD 2026:** CausalMoE (billion-scale causal discovery)
- **Industrial:** OneRanker (+1.34% GMV, WeChat ads)
- **Research focus:** Multimodal reasoning, causal discovery, unified advertising

---

## 12. 关键趋势总结

### 趋势 1: RL for LLM 后训练达到新阶段
- RLVR 方法的局限性被揭示 (NeurIPS Best Paper Runner-up: RL 不产生根本新推理模式)
- GRPO 及其变体成为主流 (D-ARL, Anchor-GRPO, GeoRA)
- 测试时推理效率成为关键 (SAGE, Thinking with Reasoning Skills)

### 趋势 2: 扩散模型在语言/多模态领域成熟
- 离散扩散语言模型从理论走向实用 (ICML 多篇)
- 扩散模型用于图像生成的 DPO 优化 (Di3PO ICLR 2026)
- 视频生成进入高效时代 (SANA-Video, DreamDojo)

### 趋势 3: 生成式推荐 & CTR Scaling Laws 爆发
- Kunlun (Meta) 首次建立推荐系统可预测 Scaling Laws
- Alibaba EST/FAT 证明 CTR Transformer 的功率律缩放
- 生成式推荐在工业界全面部署 (Kuaishou OneRec, GR4AD, Shopee UniRec)
- Semantic ID 成为生成式推荐的核心表示

### 趋势 4: Agent 系统与自主研究
- ICML 2026 是 "AI Agent Safety Era" (23,918 submissions)
- Arbor (Microsoft) 自主研究框架在 MLE-Bench 达 86.36%
- MARS (Google) 模块化研究 agent
- RE-TRAC 超越 ReAct 15-20%

### 趋势 5: 多模态统一架构
- 从 token 到多模态: 4D 场景重建 (D4RT CVPR Best), 3D 理解 (SAM 3D), 语音 LLM (SALMONN-omni)
- 深度估计成为基础能力 (Depth Anything 3, TikTok)
- 游戏基础模型: NitroGen (NVIDIA, 1000+ games)

### 趋势 6: 安全、对齐与对齐审计
- GRAM (Anthropic) 模块化预训练实现访问控制
- Constitution 审计显示 Claude 违规率从 15% 降至 2%
- 机器遗忘的局限性被揭示 (NeurIPS 2025 Oral)
- AI 辅助同行评审大规模部署 (AAAI 2026)

### 趋势 7: 高效推理 & 架构创新
- TileLang: <80 行 Python 实现融合 attention 内核, H100 上 5x 超越 Triton
- TileLang DSL 代码量减少 90%
- Mamba-3: 第三代 SSM 架构
- Tensor Product Attention: 紧凑 KV cache 表示

### 趋势 8: 记忆化 & 上下文管理
- Titans (Google): 神经长期记忆 + 2M 上下文
- ATLAS (Google ICML Oral): 测试时上下文记忆化
- LLMs Get Lost In Multi-Turn (ICLR Outstanding): 多轮 39% 性能下降
- Hubble: LLM 记忆研究模型套件
