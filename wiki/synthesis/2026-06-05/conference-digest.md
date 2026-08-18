---
title: Conference & arXiv Daily Digest (2026-06-05)
type: synthesis
created: 2026-06-05
updated: 2026-06-05
sources: []
tags: [conference-digest, arxiv, iclr-2026, icml-2026, cvpr-2026, aaai-2026, neurips-2025, acl-2026, emnlp-2025, kdd-2026, sigir-2026, recommendation, llm, agent, ctr]
---

# Conference & arXiv Daily Digest — 2026-06-05

> 按会议/专题整理的最新论文摘要，覆盖 LLM、推荐系统、广告、CTR、Agent、生成模型、序列建模、代码生成、Benchmark 等方向。

---

## 1. ICLR 2026 (Rio de Janeiro, Apr 23–27, 2026)

**概况**: 19,814 篇投稿，5,340 篇录用（26.95%），其中 Oral 223 篇（1.13%），Poster 5,117 篇。

### 1.1 推荐系统 / CTR / 广告

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 1 | **ALM-MTA: Front-Door Causal Multi-Touch Attribution for Creator-Ecosystem Optimization** | Kuaishou Team | 快手 | 对抗学习中介变量代理未观测混杂因子，通过 front-door identification 解决大规模推荐系统的多触点归因问题。在 40 亿 DAU、3000 亿样本的生产系统中，DAU 提升 0.04%，日活创作者提升 0.6%，曝光效率提升 670%。AUUC 相比 SOTA 提升最高 0.070。 |
| 2 | **DNR: Denoising Neural Reranker for Recommender Systems** | Kuaishou Team | 快手 | 将重排建模为对召回分数的去噪过程，耦合去噪重排器与噪声生成模块，分解为样本增强去噪、对抗样本探索、召回分数分布对齐三个子目标。在 3 个公开数据集和工业系统上超越现有 SOTA 重排器。 |
| 3 | **GoalRank: Group-Relative Optimization for a Large Ranking Model** | Kuaishou Team | 快手 | 证明足够大的纯生成器可近似最优排序策略优于任何有限 Generator-Evaluator 系统。使用 Group-Relative Optimization (GRO) 训练单一生成器，在 50 亿+ DAU 短视频平台上验证有效。 |
| 4 | **Mix-Ecom: Mixed-Type E-Commerce Dialogues with Complex Domain Rules** | Kuaishou Team | 快手 | 构建 4,799 条真实客服对话数据集，覆盖 4 种对话类型、3 类电商任务、82 条领域规则。揭示当前 Agent 在混合类型对话和规则密集场景下的局限性。 |

### 1.2 LLM / Agent / 推理

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 5 | **DIVA-GRPO: Difficulty-Adaptive Variant Advantage for Multimodal Reasoning** | Kuaishou Team | 快手 | 动态评估问题难度，在适当难度级别采样变体，通过难度加权归一化计算优势值。在 6 个推理基准上实现更快收敛和更高推理性能。 |
| 6 | **DreamOn: Diffusion Language Models for Code Infilling Beyond Fixed-Size Canvas** | Kuaishou Team | 快手 | 引入两种长度控制状态使扩散语言模型在扩散过程中自主扩展或收缩输出长度。基于 Dream-Coder-7B，在 HumanEval-Infilling 上匹配 SOTA 自回归模型。 |
| 7 | **GoR: A Unified Generative Framework for Ordinal Regression** | Kuaishou Team | 快手 | 将数值预测重构为自回归 token 生成任务，发射"加法语义"token 序列并以动态 `<EOS>` 终止。在 5 个领域 15 个基准上设立新 SOTA。 |
| 8 | **Multimodal Visual Jigsaw Post-Training Improves MMLMs** | P. Wu et al. | MMLab@NTU | 通过视觉拼图后训练提升多模态大语言模型能力。[arXiv:2509.25190](https://arxiv.org/abs/2509.25190) |
| 9 | **Setting the Record Straight on Transformer Oversmoothing** | Gbètondji J-S Dovonon et al. | Mila / Georgia Tech | 重新审视 Transformer 过平滑问题，提供理论分析。 |
| 10 | **Visual Symbolic Mechanisms: Emergent Symbol Processing in VLMs** | Rim Assouel et al. | Mila / Yoshua Bengio | 发现视觉语言模型中涌现的符号处理机制。ICLR 2026 Oral。 |

### 1.3 生成模型 / 扩散

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 11 | **SeedVR2: One-Step Video Restoration via Diffusion Adversarial Post-Training** | J. Wang et al. | MMLab@NTU | 通过扩散对抗后训练实现单步视频修复。[arXiv](https://arxiv.org/abs/2512.11782) |
| 12 | **Multimodal From Pixels to Words - Towards Native Vision-Language Primitives at Scale** | H. Diao et al. | MMLab@NTU | 原生视觉-语言原语的规模化。[arXiv:2510.14979](https://arxiv.org/abs/2510.14979) |

---

## 2. ICML 2026 (Seoul, Jul 6–11, 2026)

**概况**: 6,634 篇录用，涵盖 Image Generation (141)、Model Compression (117)、AI Safety (114)、RL (110)、Interpretability (92)、Multimodal VLM (89)、LLM Reasoning 等方向。

### 2.1 LLM / 推理 / MoE

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 13 | **Attention Sink Forges Native MoE in Attention Layers: Sink-Aware Training to Address Head Collapse** | Zizhuo Fu et al. | Meng Li Lab (Texas A&M) | 提出 Sink-Aware Training 解决 MoE 注意力层中的 head collapse 问题。 |
| 14 | **TEAM: Temporal–Spatial Consistency Guided Expert Activation for MoE Diffusion Language Model Acceleration** | Linye Wei et al. | Meng Li Lab (Texas A&M) | 通过时空一致性引导的专家激活加速 MoE 扩散语言模型。 |
| 15 | **HyPER: Bridging Exploration and Exploitation for Scalable LLM Reasoning with Hypothesis Path Expansion and Reduction** | Shengxuan Qiu, Haochen Huang et al. | Meng Li Lab (Texas A&M) | 通过假设路径扩展与缩减平衡 LLM 推理中的探索与利用。 |
| 16 | **DocHop: Benchmarking Out-of-domain Multi-hop Reasoning in Information-Dense Documents** | Zhuoran Yu et al. | Kookmin AILab / Wisconsin-Madison / IBM Research | 多跳推理基准测试。 |

### 2.2 Kuaishou ICML 2026 论文

快手技术团队在 ICML 2026 上有多篇论文被录用，包括一篇 Spotlight 论文关于隐喻视觉理解（metaphor visual understanding），以及在 AI 多个子领域的工作。

### 2.3 CVLab@SNU ICML 2026 论文

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 17 | **Infinite-Precision Autoregressive Modeling for Vector Graphics and Layouts** | Yeonsang Shin et al. | SNU CVLab | 无限精度自回归建模用于矢量图形和布局。 |
| 18 | **Score-Repellent Monte Carlo: Efficient Non-Markovian Sampler with Constant Memory** | Jie Hu et al. | SNU CVLab | 常数内存的高效非马尔可夫采样器。 |
| 19 | **Hybrid Space-Aware Randomized Defense for Adversarial Robustness** | Joy Dhar et al. | SNU CVLab + 多机构 | 混合空间感知随机防御提升对抗鲁棒性。 |

---

## 3. CVPR 2026 (Denver, Jun 3–7, 2026)

**概况**: 16,092 篇投稿，4,090 篇录用（~25.4%）。Best Paper 获奖者包括 SAM 3D 和 SAM 3D Body。

### 3.1 计算机视觉 / 3D

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 20 | **🏆 SAM 3D: 3Dfy Anything in Images** | Jianing Yang et al. | Meta AI (FAIR) | 将 SAM 扩展到 3D 重建，从图像中生成 3D 场景。CVPR 2026 Best Paper。[arXiv:2511.16624](https://arxiv.org/abs/2511.16624) |
| 21 | **🏆 SAM 3D Body: Robust Full-Body Human Mesh Recovery** | Xitong Yang et al. | Meta AI (FAIR) | 全身人体网格恢复。CVPR 2026 Best Paper。[arXiv:2602.15989](https://arxiv.org/abs/2602.15989) |
| 22 | **Molmo2: Open-Source Multimodal Model** | Allen AI | Allen AI | 开源多模态模型，CVPR 2026 Oral。 |

### 3.2 MMLab@NTU CVPR 2026 论文

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 23 | **MatAnyone2: Scaling Video Matting via Learned Quality Evaluator** | P. Yang et al. | MMLab@NTU | CVPR 2026 Highlight，扩展视频抠像。[arXiv:2512.11782](https://arxiv.org/abs/2512.11782) |
| 24 | **Trainable Log-linear Sparse Attention for Efficient Diffusion Transformers** | Y. Zhou et al. | MMLab@NTU | CVPR 2026 Highlight，高效扩散 Transformer 的可训练稀疏注意力。[arXiv:2512.16615](https://arxiv.org/abs/2512.16615) |

### 3.3 Meta AI / Google 等顶会论文

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 25 | **AToken: A Unified Tokenizer for Vision** | - | Meta AI | 统一视觉 tokenizer。 |
| 26 | **AVATAR: Reinforcement Learning to See, Hear, and Reason Over Video** | - | Meta AI | 视频理解的多模态 RL。 |

---

## 4. AAAI 2026 (Singapore, Jan 20–27, 2026)

**概况**: 23,680 篇投稿，4,167 篇录用（17.6%）。

### 4.1 自动驾驶 / 多模态

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 27 | **FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play Reconstruction-based Token Pruning** | 小鹏汽车 + 北大 | 小鹏汽车 / 北京大学 | 高效视觉 token 剪枝框架，专为端到端自动驾驶 VLA 模型定制。 |

### 4.2 AI Safety / 多智能体

AAAI 2026 接收了大量 AI Safety (45篇)、3D Vision (79篇)、Image Generation (79篇)、Medical Imaging (75篇)、Multimodal VLM (75篇)、Reinforcement Learning (58篇)、Autonomous Driving (56篇) 等方向论文。

---

## 5. ACL 2026

**概况**: 南京大学大模型研究中心 9 篇录用（5 Main + 4 Findings）。

### 5.1 LLM / NLP

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 28 | **Bootstrapping Code Translation with Weighted Multilanguage Exploration (BootTrans)** | Yuhan Wu et al. | 南京大学 | 无需平行语料的自举代码翻译框架。[arXiv:2601.03512](https://arxiv.org/abs/2601.03512) |
| 29 | **Reasoning While Asking: PIR** | Xin Chen et al. | 南京大学 / 深圳先进院 | 将推理 LLM 从被动求解器转变为主动询问者。[arXiv:2601.22139](https://arxiv.org/abs/2601.22139) |
| 30 | **A Data-Efficient Path to Multilingual LLMs: DeltaMoE** | Hao Zhou et al. | 南京大学 / 通义实验室 | 通过 MoE 升级实现低成本多语言扩展，避免灾难性遗忘。 |
| 31 | **How Do Answer Tokens Read Reasoning Traces?** | Haoyang Chen et al. | 南京大学 | 研究推理 LLM 中答案 token 如何读取推理轨迹。 |
| 32 | **To Diff or Not to Diff? Structure-Aware Output Formats for LLM-based Code Editing** | Wei Cheng et al. | 南京大学 / 通义实验室 | 优化输出格式和生成策略提升代码编辑效率，延迟和 token 成本降低 30%+。 |

### 5.2 中国 NLP 社区 ACL 2026 论文

ACL 2026 覆盖代码模型、视觉模型、跨学科 NLP 应用等方向，体现了 NLP 与科学、教育、医学等领域的交叉融合。

---

## 6. NeurIPS 2025 (San Diego, Dec 2–7, 2025)

**概况**: 5,526 篇投稿，5,275 篇录用（95.46% 社区数据），其中 Poster 4,515、Spotlight 683、Oral 77 篇。

### 6.1 机器人 / RL

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 33 | **Enhancing Tactile-based Reinforcement Learning for Robotic Control** | Elle Miller et al. | U. Edinburgh | 自监督学习利用触觉观测，agent 在复杂接触任务上达到超人类灵巧度。[arXiv:2510.21609](https://arxiv.org/abs/2510.21609) |

### 6.2 跨领域研究

NeurIPS 2025 覆盖 federated learning、foundation models for biology、LLM reasoning 等广泛方向。

---

## 7. EMNLP 2025 (Suzhou, Nov 4–9, 2025)

**概况**: 8,174 篇提交，1,811 篇 Main Conference 录用（22.16%），1,417 篇 Findings 录用（17.34%）。

### 7.1 LLM / NLP

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 34 | **Selective Preference Optimization via Token-Level Reward Function Estimation** | Kailai Yang et al. | Athena Research / Manchester | Token 级别奖励函数估计的选择性偏好优化。 |
| 35 | **Masked Diffusion Language Models with Frequency-Informed Training** | Despoina Kosmopoulou et al. | Athena Research / Athens | 频率信息训练的掩码扩散语言模型。 |
| 36 | **Towards Automated Error Discovery in Conversational AI** | Dominic Petrak et al. | TU Darmstadt | 对话 AI 中的自动错误发现。 |

---

## 8. KDD 2026 (Jeju Island, Aug 9–13, 2026)

**概况**: 第 32 届 ACM SIGKDD 会议，超过 1,400 篇录用。

### 8.1 推荐系统 / 数据挖掘

KDD 2026 接收了大量推荐系统、数据挖掘、知识发现方向论文。会议涵盖 Research Track、ADS Track 和 Data & Benchmark Track 三个赛道。

---

## 9. SIGIR 2026 (Melbourne, Jul 20–24, 2026)

**概况**: 信息检索顶会，已发布录用论文列表。

### 9.1 信息检索 / 推荐

SIGIR 2026 覆盖信息检索、推荐系统、搜索排序等方向。

---

## 10. 工业界推荐系统论文盘点 (2026 年初至今)

### 10.1 字节跳动 (ByteDance)

字节跳动 2026 年以来在推荐系统方向的论文覆盖：
- **生成式推荐 / Semantic ID**
- **超长序列建模**
- **大规模 Ranking Transformer**
- **预排序 / 重排序**
- **多模态 / 多业务建模**
- **Agent 化推荐**

ByteDance 在 ICLR 2026 上共 115 篇论文被录用，其中 12 篇 Oral（占提交量的 10.4%，远超会议平均的 4.2%）。

### 10.2 美团 (Meituan)

美团 2026 年推荐方向论文覆盖类似技术方向。

### 10.3 阿里巴巴 (Alibaba)

阿里 2026 年推荐方向论文，包括 Qwen 系列模型在推荐场景的应用。

### 10.4 快手 (Kuaishou)

快手在 ICLR 2026 上有 9 篇论文被录用（见上文 1.1-1.3 节），在 ICML 2026 上有多篇论文包括 Spotlight。

---

## 11. LLM Agent / 推理 / 代码执行

### 11.1 Agent 系统

| # | Title | Source | Key Innovation |
|---|-------|--------|----------------|
| 37 | **From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review** | arXiv 2504.19678 | 综述 LLM-based agents 在软件工程、科学研究、数学问题求解等领域的应用。 |
| 38 | **Agon: Autonomous Large-Scale Omnidisciplinary Research System** | arXiv 2606.24177 | 基于 Prompt Economy 构建的自主大规模全学科研究系统。 |
| 39 | **Forge Reasoning Attacks on LLM Agent Memory** | arXiv 2607.05029 | 揭示 LLM Agent 持久记忆的安全漏洞，提出伪造推理攻击。 |

### 11.2 LLM Research Papers 2026 (Sebastian Raschka 整理)

2026 年 1-5 月 LLM 研究论文重点领域：
1. **Architecture & Model Design**: Nemotron 3 (hybrid attention + Mamba-2), Arcee Trinity, Mamba-3, Gated DeltaNet-2
2. **Efficient Training & Scaling**: Deep Delta Learning, MiMo-V2-Flash
3. **Inference Efficiency & KV Cache**
4. **Sparse Attention & Long Context**
5. **Reasoning & Test-Time Compute**
6. **Reinforcement Learning & RLVR**
7. **Agent Systems & Tool Use**
8. **Coding Agents & Software Engineering**
9. **Diffusion Language Models**
10. **Model Evaluation & Benchmarks**

---

## 12. CTR Prediction / 广告

### 12.1 最新 CTR 论文

| # | Title | Authors/Affiliation | Venue | Key Innovation |
|---|-------|---------------------|-------|----------------|
| 40 | **CADET: Context-Conditioned Ads CTR Prediction with a Decoder-Only Transformer** | LinkedIn | AdKDD 2026 | 将 decoder-only Transformer 用于广告 CTR 预测，处理 post-scoring contextual signals。已部署于 LinkedIn 广告平台，相比 LiRank baseline 提升 4.04% CTR。[arXiv:2602.11410](https://arxiv.org/abs/2602.11410) |
| 41 | **Dual-Stream MLP is All You Need for CTR Prediction (DS-MLP)** | Kesha Ou et al. | SIGIR 2026 | 提出 DS-MLP 框架，解决特征交互学习复杂度高和显隐式模块不平衡两大挑战。[arXiv:2606.04944](https://arxiv.org/abs/2606.04944) |
| 42 | **EST: Towards Efficient Scaling Laws in CTR Prediction via Unified Modeling** | Mingyang Liu et al. (阿里) | arXiv 2026-02 | 统一建模实现 CTR 预测的高效 Scaling Law，解决 token-level 信号信息瓶颈。[arXiv:2602.10811](https://arxiv.org/abs/2602.10811) |
| 43 | **IDProxy: Cold-Start CTR Prediction with Multimodal LLMs** | 小红书 (Xiaohongshu) | arXiv 2026-03 | 利用多模态大语言模型解决冷启动 CTR 预测。 |
| 44 | **Field Matters: Lightweight LLM-enhanced Method for CTR Prediction** | ACM DL 2026 | KDD 2026 | 轻量级 LLM 增强 CTR 方法。 |
| 45 | **Feature Interaction using Similarity-based Adaptive Graph Attention Network** | Taylor & Francis | Neural Computing and Applications | 图注意力网络建模特征交互。 |

---

## 13. Google DeepMind / OpenAI / Meta AI 最新研究

### 13.1 Google DeepMind

| # | Title/Topic | Date | Key Innovation |
|---|-------------|------|----------------|
| 46 | **From AGI to ASI** | 2026-06-10 | 57 页论文映射从 AGI 到 ASI 的四条路径：Scaling、范式转变、递归改进、多智能体集体。arXiv:2606.12683，54,000+ 浏览。 |
| 47 | **Gemini 3.7 Flash** | 2026-08 | 最新 Gemini 模型。 |
| 48 | **DiffusionGemma** | 2026-06 | 4x 更快的文本生成。 |
| 49 | **TRecViT: A Recurrent Video Transformer** | 2026-01 | 循环视频 Transformer。 |
| 50 | **Decoupled DiLoCo** | 2026-04 | 解耦分布式训练的基础设施论文。arXiv:2604.20761 |
| 51 | **Vision Banana** | 2026-04 | 训练图像生成模型以更好理解图像。arXiv:2604.18547 |

### 13.2 OpenAI

| # | Title/Topic | Date | Key Innovation |
|---|-------------|------|----------------|
| 52 | **GPT-5.5 + Images 2.0** | 2026-04-23 | 推理内置于图像生成管线的旗舰模型。 |
| 53 | **Astra** | 2026 | 研究发布，涉及 agentic coding 和 cybersecurity 能力。 |

### 13.3 Meta AI

| # | Title/Topic | Date | Key Innovation |
|---|-------------|------|----------------|
| 54 | **SAM 3D / SAM 3D Body** | CVPR 2026 | 3D 重建最佳论文。 |
| 55 | **AI Business Assistant** | 2026-04-24 | 全球部署的 Agent 化广告工具，监控账户数据、自动排障、优化广告投放。 |
| 56 | **Llama 系列** | 2026 | 持续开源大语言模型。 |

---

## 14. 趋势总结

### 14.1 推荐系统趋势
- **生成式推荐**：从判别式范式向生成式范式转变（GenCTR, DGenCTR, EST）
- **LLM 增强推荐**：轻量级 LLM 增强传统 CTR 模型（Field Matters）
- **多模态 CTR**：利用多模态 LLM 解决冷启动（IDProxy）
- **因果归因**：front-door identification 用于大规模推荐系统（ALM-MTA）
- **重排序去噪**：将重排建模为去噪问题（DNR）

### 14.2 LLM/Agent 趋势
- **推理 LLM**：从被动求解到主动询问（PIR, HyPER）
- **MoE 扩散语言模型**：加速推理（TEAM, DreamOn）
- **Agent 安全**：记忆伪造攻击防御
- **多 Agent 协调**：agentic RAG、协作研究系统

### 14.3 视觉/生成趋势
- **SAM 3D**：从 2D 到 3D 的 foundation model 扩展
- **扩散 Transformer 效率**：稀疏注意力、单步生成
- **视频理解**：多模态 RL 用于视频推理

---

*Generated on 2026-06-05 by karpathy-wiki maintenance agent.*
