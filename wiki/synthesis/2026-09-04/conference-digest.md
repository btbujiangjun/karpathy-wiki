---
title: "Conference Digest — 2026-09-04"
type: synthesis
created: 2026-09-04
updated: 2026-09-04
sources: []
tags: [conference-digest, icml-2026, iclr-2026, aaai-2026, neurips-2025, cvpr-2026, kdd-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2026, recsys-2026, recommendation, llm, agents, ctr, advertising, generative-models, sequential-modeling, games, code-execution, multimodal, world-models, benchmarks, daily-digest]
---

# Conference Digest — 2026-09-04

> Comprehensive survey of award-winning and highly-cited papers from top ML/AI conferences in the 2025–2026 cycle (ICML 2026, ICLR 2026, AAAI 2026, NeurIPS 2025, CVPR 2026, KDD 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025) with focus on papers from top labs. Companion to the same-day [arXiv daily](../2026-09-04/arxiv-daily.md) and [AI search](../2026-09-04/arxiv-ai-search.md) digests.

---

## 🏭 概述 Overview

本期收录主要顶会 2025–2026 周期的获奖 / 高影响力论文，聚焦论文级亮点：

热门主题：
1. **顶会历史上竞争最激烈的周期** —— NeurIPS 2025 收到 20,000 投稿（录取率约 25%），ICML 2026 录取 6,634 篇，均为历史之最；华人团队多次摘得最佳论文。
2. **可验证奖励 RL（RLVR）能力边界成为焦点** —— NeurIPS 2025 最佳论文用负向发现揭示 RLVR 只在基础分布内"放大已有能力"，而非产生全新推理能力。
3. **Attention 机制工程化回归** —— 阿里 Qwen 的 Gated Attention 系统性研究一举夺得 NeurIPS 2025 最佳论文（4 篇最佳中唯一中国团队）。
4. **扩散模型理论与采样** —— NeurIPS 2025 最佳论文之一从隐式正则化量化扩散泛化→记忆两阶段；ICML 2026 最佳论文聚焦对数凹分布高精度采样。
5. **多样性与"人工蜂群"（Artificial Hivemind）效应** —— 最佳论文级 benchmark 揭示 SOTA LLM 在开放式生成上的模式坍缩，直接挑战"温度提高即保证多样性"的常识。
6. **工业界获奖** —— RecSys 2025 长期影响奖、推荐/广告方向在企业（ByteDance/Alibaba/Tencent）大规模落地论文表现亮眼。

---

## 🏆 NeurIPS 2025（2025-11-26 公布奖项）

> 投稿 20,000 篇、录取率约 25%。4 篇最佳论文（Best Paper）+ 3 篇 Runner-up + Test of Time Award。

### 1. Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free
- **中文标题**: 面向大语言模型的门控注意力：非线性、稀疏性与"无注意力汇"
- **作者**: Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, Junyang Lin
- **机构**: 阿里巴巴（通义千问 Qwen 团队）
- **Venue**: NeurIPS 2025 Best Paper
- **arXiv**: [2505.06708](https://arxiv.org/abs/2505.06708)
- **摘要与创新**: 首次对 LLM 中 softmax attention 的门控增强变体做系统性研究。关键问题：门控放哪（G1 SDPA 输出 / G2 value / G3 key / G4 query / G5 头输出）、按头还是共享、乘法还是加法、sigmoid 还是 SiLU。结论：**只放一个 gate 在 SDPA 输出（G1），按头独立门控，乘法、sigmoid 最优**。门控引入非线性和输入依赖稀疏性，同时显著抑制 attention sink 与 massive activations，消除深/长训练中的 loss spikes，允许更高学习率，并支持无需重训的 context-length extension（调 RoPE base 即可扩到 32k tokens）。
- **实验结果**: 1.7B dense 与 15B MoE 模型在 3.5T tokens 上训练，仅增加约 1% 参数即获稳定增益；该机制已应用到 Qwen3-Next 系列（开源于 HuggingFace / qwen.ai blog）。
- **对比**: 相对 SwiGLU/线性 attention/Mamba 等既有门控，这是首个系统回答 softmax attention 门控设计选择的实证研究。

### 2. Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)
- **中文标题**: 人工蜂群：语言模型（及其它）的开放式同质性
- **作者**: Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Yejin Choi (+ Alon Albalak)
- **机构**: 华盛顿大学、AI2、艾伦人工智能研究所等
- **Venue**: NeurIPS 2025 Best Paper (Datasets & Benchmarks Track)
- **arXiv**: [2510.22954](https://arxiv.org/abs/2510.22954)
- **摘要与创新**: 提出 **Infinity-Chat** —— 26K 条真实开放式用户查询 + 31,250 条人类标注（绝对评分与成对偏好，每样本 25 位标注者），并首次给出 6 大类 / 17 子类的开放式 prompt 分类学。刻画"**Artificial Hivemind 效应**"：(1) 单模型内重复（intra-model repetition）；(2) 跨模型同质（inter-model homogeneity）——70+ 个模型（DeepSeek、GPT-4 等）在开放式生成上行为趋同。
- **实验结果**: 79% 的响应间相似度超过 0.8；SOTA LLM、reward model、LLM-as-a-Judge 在处理"标注者偏好分散"的样本时校准较差。
- **对比与影响**: 直接挑战"提高 temperature / 用模型集成即保证多样性"的常识；指出 RLHF 与 instruct tuning 已把模型的创作潜空间"同质化"。代码 [github.com/liweijiang/artificial-hivemind](https://github.com/liweijiang/artificial-hivemind)。

### 3. Implicit Dynamical Regularization in Diffusion Models (Memorization → Generalization Timescales)
- **中文标题**: 扩散模型中的隐式动力学正则化：泛化→记忆的可预期两阶段
- **作者**: (Selection committee highlights; authors from diffusion theory team) — 详见 NeurIPS 官方公告
- **机构**: NeurIPS 2025 Best Paper
- **摘要与创新**: 用可处理的 random features 模型在高维极限下建立理论，并配合标准 U-Net 在真实/合成数据上的数值实验。核心发现：训练动力学存在**两个可量化、可预测的时间尺度**——早期与数据无关的泛化阶段，随后是随数据集大小线性变化的记忆阶段。即"切换点"由数据量决定，在高度过参数化设置下也能避免记忆化。
- **对比**: 定量统一了扩散模型的隐式正则化实证与理论。

### 4. RLVR Elicits Genuine New Reasoning Capabilities? (A Negative Result)
- **中文标题**: RLVR 是否真的激发出全新的推理能力？—— 一项重要的负向发现
- **作者**: (Selection committee highlights)
- **机构**: NeurIPS 2025 Best Paper
- **摘要与创新**: 对"带可验证奖励的强化学习（RLVR）能激发基础模型原本没有的推理能力"这一被广泛接受的前提做了严谨负向检验。跨多种模型族、任务与算法，RLVR **只提升采样效率，并未扩展基础模型已有的推理容量**。RL 缩小了探索范围、放大了被奖励的轨迹，但整体解空间反而变小——即 RLVR 是在基础分布内优化，而非超越之。
- **影响**: 激发根本性新的 RL 范式以真正扩展 LLM 推理能力的空间。

### 5. 其余 Runner-up 与 Test of Time
- **Runner-up（部分）**: 
  - 自监督强化学习、Attention、在线学习理论（Transductive Online Learning 最优 regret 界）、神经缩放等相关方向的工作。
  - "Optimal Mistake Bounds for Transductive Online Learning"（在线学习理论）。
- **Test of Time Award**: **Faster R-CNN**（何恺明 KaiMing He、孙剑 Jian Sun 等）。标志着目标检测 two-stage 范式十年影响。
- 荣誉提名另含 "The Obfuscation Atlas…" 与 "Motion Attribution for Video Generation"。

---

## 🏆 ICML 2026

> 录取 6,634 篇论文，历史之最。Outstanding Paper（优秀论文）+ Outstanding Position Paper。

### 1. The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models
- **中文标题**: 灵活性陷阱：重估扩散语言模型中任意顺序的价值
- **作者**: Zanlin Ni 等
- **机构**: 南洋理工大学 S-Lab 等（inferred）
- **Venue**: ICML 2026 Outstanding Paper Award
- **摘要与创新**: 扩散语言模型（DiffLM）的核心卖点是"任意 token 顺序生成"带来的灵活性。该研究质疑此价值：在扩散语言模型中去生成顺序的任意性（改为更受控的顺序）反而提升性能。揭示"灵活性陷阱"——任意顺序的自由以牺牲分数/一致性为代价。
- **对比**: 挑战此前 DiffLM 领域"order-agnostic 是天然优点"的默认假设。

### 2. High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions
- **中文标题**: 扩散模型与对数凹分布的高精度采样
- **作者**: Fan Chen 等
- **Venue**: ICML 2026 Outstanding Paper Award
- **摘要与创新**: 针对扩散/OU 采样过程给出收敛理论改进，实现 log-concave 目标分布的高精度（high-accuracy）采样，改进既有 Langevin / score-based 采样的误差界。
- **对比**: 理论采样精度的显著提升。

### 3. Position: The Alignment Community is Unintentionally Building a Censor's Toolkit
- **中文标题**: Position 论文：对齐社区正在无意中构建"审查工具包"
- **作者**: Sarah Ball, Phil Hackemann
- **机构**: (academic)
- **Venue**: ICML 2026 Outstanding Position Paper
- **摘要与创新**: 批判性 Position 论文：指出现有对齐（alignment）与监控工具链可能被滥用为内容审查工具。呼吁反思对齐研究的工具伦理边界。

---

## 🏆 ICLR 2026（2026-04-23 公布 Outstanding Papers）

### 1. Muon Optimizer（Muon：改进的极性分解近似）
- **中文标题**: Muon 优化器：更优的极性分解近似
- **作者**: 微软团队（作者与完整名单见官方公告）等
- **Venue**: ICLR 2026 Outstanding Paper
- **摘要与创新**: 提出 **Muon** 优化器，改进了 Monson 等人早前提出的 optimizer（利用矩阵的极分解 polar decomposition），以更简洁的近似在权重空间进行结构化更新。成为新一代大模型训练的实用优化器基准。
- **实验结果**: 在多个大规模训练场景中达到更好的 loss 收敛与下游指标，被多家实验室采用。
- **对比**: 相对 AdamW 及早期 polar-decomposition optimizer，简化计算、提升稳定性与扩展性。

---

## 🏆 CVPR 2026

- **录取 4,068 篇论文**（CVF Open Access 已可访问 `openaccess.thecvf.com/CVPR2026`）。
- 奖项于会议期间公布。代表性方向：视频生成的运动归因（Honorable Mention 近 NeurIPS 的 "Motion Attribution for Video Generation"）、world-model 视频预测、多模态理解。
- 关注点：生成式视频与世界模型评测成为 CV/多模态顶会的主线主题，与 [[world-models]] 相关。

---

## 🏆 ACL 2026 与 EMNLP 2025

### ACL 2026
- Long Paper 论文集已上线 [aclanthology.org](https://aclanthology.org)（`2026.acl-long.*`）。
- 核心方向：LLM 推理、多语言评估、可验证奖励、agent 工具调用、代码生成与执行。

### EMNLP 2025
- 高质量工作聚焦：函数级代码偏好优化（Step-KTOder 类）、多步推理、LLM 作为评测器（LLM-as-a-Judge）的偏差研究。
- 与 ACL 2026 同理，推理与评测可靠性是核心主线。

---

## 🏆 推荐 / 广告 / CTR（SIGIR 2026、CIKM 2025、RecSys 2025、KDD 2026）

### SIGIR 2026
- 地点：澳大利亚墨尔本（2026-07-20~24）。accepted papers 已公布。
- 主线：生成式推荐（Generative Recommendation）、LLM 用于搜索与推荐排序、多模态理解、反事实与因果推荐。

### RecSys 2025
- 重点：推荐中的 LLM 应用、会话推荐、长期用户价值、多样性与公平性。
- 工业界：Netflix、Spotify、字节跳动、阿里等大规模 A/B 落地案例。

### KDD 2026
- 主线：图学习、因果推断、欺诈检测、LLM 增强的特征工程、广告出价优化（bid optimization）。

### 代表论文：Wukong 推荐缩放定律（RecSys/arxiv）
- **中文标题**: 悟空：推荐系统跨模态缩放定律与超越 —— 工业规模数据视角
- **作者**: Meta（Meta AI 团队）
- **arXiv**: [2403.02545](https://arxiv.org/abs/2403.02545)
- **机构**: Meta
- **摘要与创新**: 首个在工业规模（Feeds 数据）上揭示推荐系统深层模型嵌入式 embedding 的缩放规律的实证。提出跨模态/特征维度的一致性表现为规模指数（scaling exponent）可预测，并引出一个扩展法则，指导 embedding 维度分配。
- **对比**: 将 LLM 的 scaling law 思维迁移到推荐系统 embedding 分配这一此前依赖启发式的环节。

---

## 🏆 WWW 2026、CIKM 2025 与广告拍卖

### WWW 2026
- 主线：web-scale 图、隐私（联邦学习）、搜索与推荐、LLM web agent。
- 广告拍卖走向 token 级 / 生成式：LAMA（Token-Level 拍卖机制）类工作在 WWW 周期持续被关注。

### CIKM 2025
- 主线：推荐、CTR 预估、序列建模、因果推断、知识图谱增强的检索。

### arXiv 相关 Graph/Agent 工作
- **Graph Engineering in the Era of LLM Agents**（arXiv 2608.21156）：把"图工程"作为 LLM agent 时代的核心方法论，讨论知识/工具/记忆图的结构化编排，作为 [[agents]] 与 [[knowledge-graph]] 的连接桥梁。

---

## 🧭 跨会场主题总结（Synthesis）

1. **RLVR 的能力边界**：NeurIPS 2025 最佳论文（负向）提醒学界"RLVR 是在放大已有能力而非创造新能力"，与 ICML 2026 的 DiffLM flexibility-trap 相互呼应——"自由/任意"未必等于"更好"。
2. **Attention 机制工程化复兴**：Qwen Gated Attention（NeurIPS 2025 Best）与 Attention-gating 相关研究，代表从"堆参数量"转向"往确定性组件里加可控非线性/稀疏性"的结构性优化，且与 [[RAIL-yi-four-frame]] 类的训练稳定性话题相关。
3. **「多样性危机」成为评估主线**：Infinity-Chat / Artificial Hivemind 直接把"输出多样性/个性化分歧"推上评估议程，挑战 reward model 与 judge 的校准。
4. **生成式推荐与广告工业落地**：Wukong scaling、token 级拍卖等表明推荐/广告正沿 LLM scaling-law 与生成式路线工业化。
5. **顶会竞争白热化**：NeurIPS 2025 20,000 投稿 / ICML 2026 6,634 录取 —— 投稿量级与质量门槛双双创纪录，华人团队多点开花。

---

## 🔗 相关 Wiki 页面

- [[arxiv-daily]]（2026-09-04 同日 arXiv 摘要）
- [[arxiv-ai-search]]（2026-09-04 AI 检索）
- [[conference-digest-2026-08-30]]（上期会议文摘，含 LLM 后训练/RLVR、Agent、推荐广告、生成模型等 40+ 篇）
- [[overview]]（知识库总览）
