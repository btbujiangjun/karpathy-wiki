---
title: "Conference & arXiv Paper Digest — 2026-07-23"
type: synthesis
created: 2026-07-23
updated: 2026-07-23
sources: []
tags: [arxiv, conferences, icml-2026, iclr-2026, aaai-2026, cvpr-2026, neurips-2025, kdd-2026, emnlp-2025, sigir-2026, cikm-2025, recsys-2025, ctr, recommendation, agents, llm, generative-models, sequential-modeling, benchmarks]
---

# Conference & arXiv Paper Digest — 2026-07-23

> 扫描近期顶级会议（已发布/接收）及 arXiv 热门论文，聚焦 AI Agents、LLM、CTR/推荐、Generative Models、Sequential Modeling、Benchmarks 等方向。按会议分组，每篇含中英文标题、作者、机构、摘要、创新点、与 prior work 对比、链接。

---

## 一、ICML 2026（Seoul, Korea · Jul 6–11, 2026）

- 接收 6,352 篇 / 23,918 提交，录取率 26.6%
- Oral 168 · Spotlight 406 · Poster 6,060

### 1.1 Agent 系统与多智能体

**AOrchestra: Automating Sub-Agent Creation for Agentic Orchestration**
自动创建子智能体的智能编排
- Authors: DeepWisdom et al.
- Affiliation: DeepWisdom, HKUST(GZ), Renmin, UCLA, McGill, Yale
- 问题背景：现有 agent 是固定 prompt chain，缺乏动态编排能力。
- 方法：将 agent 建模为 (Instruction, Context, Tools, Model) 四元组，由编排器按需创建子 agent，分离编排与执行。
- 创新点：统一抽象 + cost-aware in-context optimization + supervised fine-tuning。
- 对比：GAIA / Terminal-Bench 2.0 / SWE-Bench-Verified 上超过现有 agentic baselines。
- Link: https://arxiv.org/abs/2602.03786

**InfoPO: Information-Driven Policy Optimization for User-Centric Agents**
信息驱动的用户中心智能体策略优化
- Authors: DeepWisdom et al.
- Affiliation: DeepWisdom, HKUST(GZ), Renmin, UCLA
- 问题背景：用户中心 agent 应学会何时提问、何时行动。
- 方法：通过 turn-level information gain 度量用户反馈对 agent 下一动作分布的改变量，与 outcome reward 组合做多轮策略优化，引入 adaptive variance-gated fusion。
- 创新点：信息增益驱动的多轮 RL，避免仅优化最终答案。
- 对比：UserGym / ColBench / τ²-Bench 上超过 prompting 和多轮 RL baseline。
- Link: https://arxiv.org/abs/2602.03786

**InteractComp: Evaluating Search Agents With Ambiguous Queries**
评估模糊查询下的搜索智能体
- Authors: Mingyi Deng et al.
- Affiliation: DeepWisdom, HKUST(GZ), Renmin, UCLA, McGill, Yale
- 问题背景：搜索 agent 假设用户查询完整无歧义，实际中用户意图经常模糊。
- 方法：构建 ambiguous query benchmark，评估 agent 是否能主动澄清意图。
- 创新点：揭示现有 agent 在模糊查询下过度自信，不主动提问；强制交互可大幅提升性能。

**AutoWebWorld: Scalable Web Environments for Agent Training**
可扩展 Web 环境用于智能体训练
- Authors: DeepWisdom et al.
- 方法：用 coding agent 将 FSM 规范转为交互网站，BFS 生成候选轨迹，执行验证后产出 29 个 web 环境 / 11,663+ verified trajectories，成本仅 $0.04/trajectory。
- 创新点：可扩展、可控、内在可验证的 web agent 训练/评估环境。

**MindFlow: Mind Supernet Powered Thinking Flows for Research Idea Innovation**
思维超级网络驱动的研究创意创新
- Authors: Mengdi Liu et al.
- Affiliation: ICT CAS, PKU, DeepWisdom, SJTU, RUC
- 问题背景：研究 idea 生成是开放式多目标任务（novelty, significance, effectiveness, feasibility）。
- 方法：将思维过程显式化、可控化、可优化化，提出 structured thinking flows 框架。

### 1.2 LLM Reasoning & Training

**A Formal Comparison Between Chain of Thought and Latent Thought**
CoT 与 Latent Thought 的形式化比较
- 对 Chain of Thought 和 latent thought 进行系统性形式化对比分析。

**Efficient Training-Free Multi-Token Prediction via Embedding-Space Probing (ESP)**
无需训练的嵌入空间多 token 预测
- 方法：在冻结 LLM 输入序列中注入 mean prompt embeddings 作为 mask tokens，单次 forward pass 同时探测多个未来 token。
- 结果：LLaMA3 / Qwen3 上相比 LADE / STAND / PLD，acceptance length 提升 7–11%，throughput 提升 15–19%。

**Ekka: Automated Diagnosis of Silent Errors in LLM Inference**
LLM 推理静默错误自动诊断
- 问题：LLM serving 中输出退化但无显式错误（silent errors）。
- 方法：以 HuggingFace 参考实现为 oracle，建模为 differential debugging task。

**Clover: Accurate LLM Pre-Training in NVFP4 by Improved Unbiased Gradient Estimation**
FP4 精度下的 LLM 高精度预训练
- 创新：改进的无偏梯度估计使 NVFP4 精度下的 LLM pre-training 精度接近 FP16。

**Clipping Low-Probability Tokens in SFT Yields a Generalizable Initialization for RL**
SFT 中裁剪低概率 token 作为 RL 泛化初始化
- 创新：SFT 阶段裁剪低概率 token 可生成更适合 RL 训练的初始化。

### 1.3 AI Safety

- ICML 2026 有 114 篇 AI Safety 相关论文（共 6,634 篇中），涵盖 alignment, robustness, interpretability。

### 1.4 Reinforcement Learning

- ICML 2026 有 110+ RL 论文，涵盖 multi-agent RL, safe RL, offline RL, model-based RL。

---

## 二、ICLR 2026（Rio de Janeiro, Brazil · Apr 23–27, 2026）

- 接收 5,300+ 篇，Oral 223 篇

### 2.1 推荐系统与 CTR

**iFusion: Diffusion-based User Interest Fusion for CTR Prediction**
基于扩散模型的用户兴趣融合用于 CTR 预测
- 问题背景：现有方法分别建模长期/短期兴趣，融合时存在特征空间不对齐、短期噪声传播。
- 方法：将兴趣融合重构为条件生成过程，以短期兴趣为条件引导扩散去噪整合长期表示。
- 创新点：Decoupled Classifier-Free Guidance (DCFG) + Mixed Autoregressive Denoising Network (MARN)。
- 对比：消除线性融合假设依赖。

**BridgeDrive: Diffusion Bridge Policy for Closed-Loop Trajectory Planning**
扩散桥策略用于闭环轨迹规划
- 方法：用 diffusion bridge 替代 truncated diffusion，确保 forward/backward 过程理论对称。
- 结果：Bench2Drive 闭环评估中 success rate 74.99% (PDM-Lite) / 89.25% (LEAD)，超越前 SOTA 7.72% / 2.45%。

### 2.2 Agent 系统

**SPIRAL: Self-Play on Zero-Sum Games Incentivises Reasoning via Multi-Agent Multi-Turn RL**
通过零和博弈自我对弈激励推理
- Authors: A*STAR CFAR et al.
- 方法：多智能体多轮 RL 中的 self-play 激励推理能力。

**A Framework for Studying AI Agent Behavior: Evidence from Consumer Choice Experiments**
研究 AI 智能体行为的框架：消费者选择实验
- 从行为经济学角度研究 agent 决策行为。

### 2.3 LLM Reasoning

**Safe Exploration via Policy Priors (SOOPER)**
基于策略先验的安全探索
- 方法：使用 suboptimal 但保守的策略作为先验，通过概率动态模型乐观探索、悲观回退。
- 结果：在 key safe RL benchmarks 和真实硬件上验证 safety guarantee + convergence to optimal policy。

### 2.4 Model Compression

- ICLR 2026 有 240 篇 Model Compression 论文。

---

## 三、AAAI 2026（Singapore · Jan 20–27, 2026）

- 接收 ~4,167 篇 / ~23,000+ 提交，录取率 17.6%
- 48 期 proceedings

### 3.1 自动驾驶与机器人

**FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play Reconstruction-based Token Pruning**
高效端到端驾驶：即插即用的重建式 Token 裁剪
- Authors: 小鹏汽车 & 北京大学
- 问题背景：VLA 模型在端到端自动驾驶中效率低下。
- 方法：提出 Reconstruction-based Token Pruning 框架，专门优化视觉 token 效率。
- 创新点：针对 VLA 的高效视觉 token 剪枝。

### 3.2 LLM 与 NLP

- AAAI 2026 有 37 篇 LLM Reasoning 论文，29 篇 LLM (Other) 论文。
- LLM Efficiency: 9 篇；Knowledge Editing: 4 篇；Text Generation: 3 篇。

### 3.3 多模态与视觉

- Image Generation: 79 篇；Multimodal VLM: 75 篇；3D Vision: 79 篇。
- Video Understanding: 27 篇；Object Detection: 29 篇。

### 3.4 AI Safety

- 45 篇 AI Safety 论文。

---

## 四、CVPR 2026（Denver, CO · Jun 3–7, 2026）

- 提交 16,092 篇，接收 4,090 篇（25.42%录取率）
- Oral · Highlight · Poster

### 4.1 Best Papers

**Best Paper: Efficiently Reconstructing Dynamic Scenes One D4RT at a Time**
- 问题：动态场景重建效率低。
- 创新：提出 D4RT 方法实现高效动态场景重建。

**Best Student Paper: Native and Compact Structured Latents for 3D Generation**
- 创新：3D 生成中的原生紧凑结构化 latent 表示。

**Best Paper Honorable Mentions + Best Student Paper Honorable Mention**
- 另有两篇最佳论文提名和一篇最佳学生论文提名。

### 4.2 关键论文

**TIPSv2: Advancing Vision-Language Pretraining with Enhanced Patch-Text Alignment**
- Authors: Google Research et al.
- 创新：增强的 patch-text alignment 用于视觉语言预训练。

**WorldLens: Full-Spectrum Evaluations of Driving World Models in Real World**
驱动世界模型的全频谱真实世界评估
- Authors: NTU MMLab et al. (CVPR 2026 Oral)
- 创新：WorldLens 框架全面评估 driving world models。

**OmniVGGT: Omni-Modality Driven Visual Geometry Grounded Transformer**
全模态驱动的视觉几何 Grounded Transformer
- Authors: NTU MMLab (CVPR 2026 Highlight)
- 创新：融合全模态信息的视觉几何 transformer。

**PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image**
从单张图片生成仿真就绪的物理 3D 资产
- 创新：物理属性感知的 3D 生成。

**Trainable Log-linear Sparse Attention for Efficient Diffusion Transformers**
可训练的对数线性稀疏注意力
- Authors: NTU MMLab (CVPR 2026 Highlight)
- 创新：将 attention 复杂度降至 O(n log n)，提升 DiT 效率。

---

## 五、NeurIPS 2025（San Diego · Dec 2025）

- 接收 5,275+ 篇（Poster 4,515 · Spotlight 683 · Oral 77）

### 5.1 LLM 与推理

**Gated Integration of Low-Rank Adaptation for Continual Learning of Large Language Models**
门控集成 LoRA 用于 LLM 持续学习
- Authors: Yan-Shuo Liang et al., Nanjing University
- 问题背景：LLM 在序列学习下游任务时出现 catastrophic forgetting。
- 方法：门控机制整合多个 LoRA adapter，平衡新旧任务性能。

**Trust Region Reward Optimization and Proximal Inverse Reward Optimization**
信任域奖励优化
- 创新：改进 RLHF 中的奖励优化策略。

**Test-Time Reinforcement Learning (TTRL)**
测试时强化学习
- 创新：LLM 在推理时利用未标注数据通过 RL 自我进化。
- 结果：在 ARC 和 BIG-Bench Hard 上显著提升。

### 5.2 Agent 系统

**Scaling Agent Learning via Experience Synthesis (DreamGym)**
通过经验合成扩展智能体学习
- 方法：在合成环境中训练 LLM-based agents 的可扩展 RL 框架。

### 5.3 Apple at NeurIPS 2025

**SimpleFold: Folding Proteins is Simpler than You Think**
- Apple 研究，蛋白质折叠简化方法。

**PersonaTeaming: Exploring How Introducing Personas Can Improve Automated AI Red-Teaming**
- Apple 研究，通过角色引入改进自动化 AI 红队测试。

**MLX Technical Demo**
- 展示在 iPad Pro M5 芯片上用扩散模型生成图像，4-Mac Studio M3 Ultra 集群运行 1 万亿参数模型。

---

## 六、KDD 2026（Jeju Island, Korea · Aug 9–13, 2026）

- 第 32 届 ACM SIGKDD Conference on Knowledge Discovery and Data Mining
- Proceedings 已在 ACM Digital Library 发布

### 6.1 关键主题

- Data Mining, Recommendation Systems, CTR Prediction
- Industrial-scale ML, Sequential Pattern Mining

---

## 七、EMNLP 2025（Suzhou, China · Nov 4–9, 2025）

- 提交 8,174 篇，Main Conference 接收 1,811 篇（22.16%），Findings 接收 1,417 篇（17.34%）
- Best Paper · Outstanding Paper 奖项

### 7.1 关键论文

- **Towards Automated Error Discovery: A Study in Conversational AI** — 对话 AI 中的自动错误发现
- **Automating Alternative Generation in Decision-Making** — 决策中的备选方案自动生成

### 7.2 主题轨道

- 特别主题："Advancing our Reach – Interdisciplinary Recontextualization of NLP"
- 41 篇主会论文 + 32 篇 Findings 论文

---

## 八、SIGIR 2025 / SIGIR 2026

### 8.1 SIGIR 2025（Padua, Italy · Jul 13–18, 2025）

- 接收 900 篇 / 4,526 提交（20%录取率）
- 关键 Session：Conversational IR and Intelligent Agents, RecSys (Sequential, FATE, LLMs, Collaborative Filtering), Search and Ranking

### 8.2 SIGIR 2026（Melbourne, Australia · Jul 20–24, 2026）

- 即将召开，关注 LLM-based IR, Agent Search, RAG 评估。

---

## 九、ACL 2026（Vienna, Austria · Jul 2026）

### 9.1 关键论文

**AgencyBench: Benchmarking the Frontiers of Autonomous Agents in 1M-Token Real-World Contexts**
百万 Token 真实上下文中的自主智能体前沿评估
- Authors: Keyu Li et al. (ACL 2026 Long Paper)
- 问题背景：现有 benchmark 聚焦单一能力，无法捕捉长周期真实场景。
- 方法：6 核心 agentic 能力 × 32 真实场景 × 138 任务，平均需 90 次 tool calls、1M tokens。
- 创新点：user simulation agent + Docker sandbox 进行自动化评估。
- 结果：闭源模型 (48.4%) 显著优于开源模型 (32.1%)。

---

## 十、CIKM 2025（Seoul, Korea · Nov 10–14, 2025）

- Proceedings 已在 ACM Digital Library 发布
- 关键论文：**ExplorAct** — 基于上下文感知的 next-action recommendation 框架

---

## 十一、2026 工业界推荐系统 / CTR / Ads 重点论文

> 以下来自 ByteDance、Alibaba、Meta、Kuaishou、Tencent 等工业界 2026 年 arXiv 论文。

### 11.1 ByteDance

**HyFormer: Revisiting the Roles of Sequence Modeling and Feature Interaction in CTR Prediction**
重新审视序列建模与特征交互在 CTR 预测中的角色
- Authors: ByteDance
- 问题背景：CTR 预测中序列建模和特征交互的角色分配不清。
- 方法：在抖音搜索系统上评估，统一序列建模与特征交互。
- Link: https://arxiv.org/abs/2601.12681

**MixFormer: Co-Scaling Up Dense and Sequence in Industrial Recommenders**
工业推荐系统中 Dense 和 Sequence 的协同扩展
- Authors: ByteDance

**TokenMixer-Large: Scaling Up Large Ranking Models in Industrial Recommenders**
扩展工业推荐系统中的大型排序模型
- Authors: ByteDance

**Zenith: Scaling up Ranking Models for Billion-scale Livestreaming Recommendation**
十亿级直播推荐的排序模型扩展
- Authors: ByteDance

**IAT: Instance-As-Token Compression for Historical User Sequence Modeling**
历史用户序列建模的实例即 Token 压缩
- Authors: ByteDance
- Link: https://arxiv.org/abs/2604.08933

**MDL: A Unified Multi-Distribution Learner via Tokenization**
通过 Tokenization 的统一多分布学习器
- Authors: ByteDance

**R³-VAE: Reference Vector-Guided Rating Residual Quantization VAE for Generative Recommendation**
参考向量引导的评分残差量化 VAE 生成式推荐
- Authors: ByteDance
- Link: https://arxiv.org/abs/2604.11440

### 11.2 Alibaba

**EST: Towards Efficient Scaling Laws in CTR Prediction via Unified Modeling**
通过统一建模实现 CTR 预测的高效 Scaling Law
- Authors: Alibaba
- Link: https://arxiv.org/abs/2602.10811

**SORT: A Systematically Optimized Ranking Transformer for Industrial-scale Recommenders**
系统优化的工业级排序 Transformer
- Authors: Alibaba
- Link: https://arxiv.org/abs/2603.03988

**Rethinking Recommendation Paradigms: From Pipelines to Agentic Recommender Systems**
从流水线到智能体推荐系统的范式重思
- Authors: Alibaba
- Link: https://arxiv.org/abs/2603.26100

**RecGPT-Mobile: On-Device LLMs for User Intent Understanding in Taobao Feed Recommendation**
淘宝 Feed 推荐中的端侧 LLM 用户意图理解
- Authors: Taobao & Tmall, Alibaba

**MAC: A Conversion Rate Prediction Benchmark Featuring Labels Under Multiple Attribution Mechanisms**
多归因机制下的转化率预测 Benchmark
- Authors: Alibaba
- Link: https://arxiv.org/abs/2603.02184

**Beyond Dense Connectivity: Explicit Sparsity for Scalable Recommendation Models (SSR)**
超越密集连接：可扩展推荐模型的显式稀疏化
- Authors: Alibaba
- Link: https://arxiv.org/abs/2604.08011

### 11.3 Meta

**Kunlun: Establishing Scaling Laws for Massive-Scale Recommendation Systems through Unified Architecture Design**
通过统一架构设计建立大规模推荐系统的 Scaling Law
- Authors: Meta

**LLaTTE: Scaling Laws for Multi-Stage Sequence Modeling in Large-Scale Ads Recommendation**
大规模广告推荐中多阶段序列建模的 Scaling Law
- Authors: Meta

**ULTRA-HSTU: Bending the Scaling Law Curve in Large-Scale Recommendation Systems**
弯曲大规模推荐系统的 Scaling Law 曲线
- Authors: Meta

### 11.4 Kuaishou

**OneRec: Unifying Retrieve and Rank with Generative Recommender and Preference Alignment**
统一召回与排序的生成式推荐与偏好对齐
- Authors: Kuaishou

**DualGR: Generative Retrieval with Long and Short-Term Interests Modeling**
长短兴趣建模的生成式检索
- Authors: Kuaishou

**Disentangled Interest Network for Out-of-Distribution CTR Prediction**
用于 OOD CTR 预测的解耦兴趣网络
- Authors: Kuaishou

**Towards End-to-End Alignment of User Satisfaction via Questionnaire in Video Recommendation**
视频推荐中通过问卷的端到端用户满意度对齐
- Authors: Kuaishou
- Link: https://arxiv.org/abs/2601.20215

### 11.5 Tencent

**FEDIN: Frequency-Enhanced Deep Interest Network for CTR Prediction**
频率增强的深度兴趣网络用于 CTR 预测
- Authors: Tencent
- 问题背景：序列推荐模型难以捕捉用户兴趣中的潜在周期模式。
- 方法：利用频域信号增强时域行为数据中的周期性模式。

**Distribution-Aware End-to-End Embedding for Streaming Numerical Features in CTR Prediction**
CTR 预测中流式数值特征的分布感知端到端 Embedding
- Authors: Tencent
- Link: https://arxiv.org/abs/2602.03223

### 11.6 Meituan

**MBGR: Multi-Business Prediction for Generative Recommendation at Meituan**
美团多业务生成式推荐预测
- Authors: Meituan
- Link: https://arxiv.org/abs/2604.02684

**Next-Scale Generative Reranking: A Tree-based Generative Rerank Method at Meituan**
美团基于树的生成式重排序
- Authors: Meituan
- Link: https://arxiv.org/abs/2604.05314

---

## 十二、Agentic Systems & Benchmarks（2026 热点）

**General AgentBench: Benchmark Test-Time Scaling of General LLM Agents**
通用 LLM 智能体的测试时 Scaling 评估
- 问题背景：LLM agent 在域内到通用评估间存在显著 robustness gap。
- 创新点：揭示 sequential scaling 受限于 context ceiling，parallel scaling 受限于 verification gap。
- Link: https://arxiv.org/abs/2602.18998

**Agents' Last Exam (ALE)**
智能体的终极考试
- Authors: UC Berkeley et al.
- 结果：最难 "Last-Exam" 层级上前沿 agent 平均仅 2.6% full pass rate。
- Link: https://arxiv.org/abs/2606.05405

**MalSkillBench: Runtime-Verified Benchmark of Malicious Agent Skills**
恶意智能体技能的运行时验证 Benchmark
- 3,944 恶意样本（3,214 合成 + 703 野生 + 27 确认恶意）。
- 覆盖 code injection, prompt injection, mixed attacks。
- Link: https://arxiv.org/abs/2606.07131

**Benchmarking AI Agents for Addressing Scientific Challenges Across Scales**
跨尺度科学挑战的 AI Agent Benchmark
- 评估 AI agent 在真实研究场景中的实际能力。
- Link: https://arxiv.org/abs/2606.12736

**ReSearch: Learning to Reason with Search for LLMs via RL**
通过 RL 训练 LLM 使用搜索进行推理
- 方法：无需监督推理步骤数据，纯 RL 训练 LLM 在推理中自然展现 reflection 和 self-correction。

**Rethinking Agentic RL In Large Language Models**
重新思考 LLM 中的智能体 RL
- 综述：概念基础、方法创新、有效设计，识别关键挑战与未来方向。
- Link: https://arxiv.org/abs/2604.27859

---

## 十三、关键趋势总结

### 13.1 CTR / 推荐系统

| 趋势 | 代表工作 | 机构 |
|------|---------|------|
| Scaling Law 进入推荐系统 | Kunlun, LLaTTE, ULTRA-HSTU, EST | Meta, Alibaba |
| 生成式推荐兴起 | OneRec, R³-VAE, MBGR, GenCI | Kuaishou, ByteDance, Meituan, Alibaba |
| 序列建模持续深化 | HyFormer, MixFormer, TokenMixer-Large | ByteDance |
| Agent 范式进入推荐 | Agentic Recommender Systems | Alibaba |
| 模型效率优化 | UG-Sep, DeRes, DS-MLP | ByteDance, Alibaba, Pinterest |

### 13.2 Agent 系统

| 趋势 | 代表工作 |
|------|---------|
| 动态编排子 agent | AOrchestra (ICML 2026) |
| Agent 自我进化 | TTRL, Test-Time RL |
| Agent 安全评估 | NEXUS, MalSkillBench |
| Agent Benchmark 升级 | AgencyBench (ACL 2026), General AgentBench, ALE |
| 用户中心交互 | InfoPO, InteractComp |

### 13.3 LLM 推理与训练

| 趋势 | 代表工作 |
|------|---------|
| CoT vs Latent Thought | ICML 2026 formal comparison |
| 高效推理（多 token 预测） | ESP (ICML 2026) |
| FP4 训练 | Clover (ICML 2026) |
| RL 作为泛化初始化 | Clipping in SFT (ICML 2026) |
| 扩散语言模型 | ICLR 2026 multiple papers |

### 13.4 计算机视觉

| 趋代 | 代表工作 |
|------|---------|
| 动态场景重建 | D4RT (CVPR 2026 Best Paper) |
| 3D 生成 | Native Compact Structured Latents (CVPR 2026 Best Student Paper) |
| 高效 DiT | Trainable Log-linear Sparse Attention (CVPR 2026 Highlight) |
| VLM 预训练 | TIPSv2 (Google, CVPR 2026) |
| Driving World Model | WorldLens (CVPR 2026 Oral) |
