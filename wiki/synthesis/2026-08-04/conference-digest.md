---
title: "Conference Digest 2026-08-04：2026 顶会获奖全谱补全 + 代码执行 Agent / 长上下文新作"
type: synthesis
created: 2026-08-04
updated: 2026-08-04
sources: []
tags: [conference-digest, icml-2026, acl-2026, emnlp-2025, www-2026, cvpr-2026, ictr-2026, neurips-2025, kdd-2026, sigir-2026, aaai-2026, arxiv]
---

# Conference Digest — 2026-08-04

本期在 [2026-08-01 digest](../2026-08-01/conference-digest.md)（ICML/ACL/NeurIPS/CVPR/ICLR/AAAI 最佳论文、EMNLP/SIGIR notable tables、WWW 概览）与 [2026-08-03 digest](../2026-08-03/conference-digest.md)（KDD 2026 工业界深潜、RecSys/CIKM/SIGIR 2025 奖项确认、DeepMind/Meta/NVIDIA 研究）基础上，**补全 2026 年度顶会获奖名单全谱**（EMNLP 2025、WWW 2026、ACL 2026 完整奖项、CVPR 2026 全部奖项、ICLR 2026 Test-of-Time、NeurIPS 2025 runners-up、KDD 2026 提前公布），并精选 5 篇 **代码执行 / Agent 可靠性 / 长上下文 KV** 方向的 7 月 arXiv 新作（与同日 [arxiv-daily](./arxiv-daily.md) / [arxiv-ai-search](./arxiv-ai-search.md) 无重叠）。

---

## 1. 2026 年度顶会获奖名单全谱（补全 + 新确认）

### 1.1 CVPR 2026（完整奖项）— Denver, 2026-06-03 ~ 06-07

**投稿规模（新高）**：16,092 有效投稿 → 4,089 录用（≈ 25.4%），录用量较 2025（2,878）**+42%**；74 篇入围最佳论文候选。embodied AI 相关占比 2.9% → 6.2%，视觉-语言 4.9% → 10.6%（大会主题「embodied AI + 视频生成」）。

- **Best Paper**：*Efficiently Reconstructing Dynamic Scenes One D4RT at a Time* — Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, Liliane Momeni et al.（Google DeepMind / UCL / Oxford）— 将动态场景重建拆解为逐帧 D4RT 稀疏表示，降低动态视频重建的算力与内存（**[08-01 digest](../2026-08-01/conference-digest.md) 已详述**）。
- **Best Student Paper**：*Native and Compact Structured Latents for 3D Generation*（TRELLIS.2）— Xiang et al.（Tsinghua / MSRA / USTC / Microsoft AI）— 结构化 3D latent + **O-Voxel（正交多分辨率体素）**自监督初始化，16GB VRAM 可训练、消费级 GPU 可推理，开源 1B/8B 模型（08-01 已列，本期补「Best Student」头衔与 O-Voxel 细节）。
- **Best Paper Honorable Mentions**：*SAM 3D*（Meta Superintelligence Labs — X. Chen, F.-J. Chu, P. Gleize, K. Liang, A. Sax, H. Tang, W. Wang, M. Guo, T. Hardin et al.，SAM 扩展到 3D）、*NitroGen*（NVIDIA / Stanford / Caltech / U Chicago / UT Austin — Magne et al.，LLM 驱动的程序化游戏世界生成，**[08-03 digest](../2026-08-03/conference-digest.md) 已详述**）。
- **Best Student HM**：*ChordEdit*（Lu et al.，多模态和弦记忆的编辑能力）。

### 1.2 ICML 2026（补充）

- 08-01 已覆盖 2 Outstanding Papers（Flexibility Trap、High-Accuracy Sampling）+ Censor's Toolkit Position Paper + HM（Obfuscation Atlas、How Much Can LMs Memorize）。本期补第三篇 HM：*Motion Attribution for Video Generation*（视频生成中像素级运动归因）。
- 业界参与：NVIDIA 74 篇论文、145 篇引用 Nemotron 系列；8 场 tutorial（gen model 强化学习、efficient reasoning、multimodal foundation 等）。

### 1.3 ICLR 2026（补充 Test-of-Time）

- **Test of Time Awards（10 周年，本届新增）**：*DCGAN: Unsupervised Representation Learning with Deep Convolutional GANs*（Radford et al., 2015）与 *Continuous Control with DDPG*（Lillicrap et al., 2015）。
- 数字口径：BestHub 报 ≈19,000 投稿 / 28% 录用；08-01 报 19,525 / 27.4%（minor 差异，两个来源）。
- 08-01 已覆盖：Transformers are Inherently Succinct、LLMs Get Lost、Polar Express HM、Mamba-3。

### 1.4 ACL 2026（完整获奖名单）— Barcelona, 2026-07-26 ~ 08-01

- **Best Theme Paper（最佳主题论文）**：
  - *The Imperfective Paradox in Large Language Models* — Bolei Ma, Yusuke Miyao（Tokyo）— LLM 对「未完成事件（imperfective）」的语义表征；**08-01 已详述**。
  - *Memory Efficiency and Resource-Rational Encoding* — 资源受限下语言记忆的最优编码；**08-01 已详述**。
  - *Characterizing the Expressivity of Local Attention* — local attention 表达能力刻画；**08-01 已详述**。
- **Best Resource Papers（最佳资源论文）**：
  - *HSCodeComp* — 39 语言编程题逐语言分类（2025 届第二期，未公布线上）。
  - *ImplicitMemBench* — 隐式记忆基准（Zichun Yu et al.）。
  - *Audio MultiChallenge* — 语音 LLM 联合挑战基准（Nicola Jones et al.）。
  - *VeriTaS* — 100k 规模多跳视觉文本问答资源（Filippos Rovanakis et al.）。
- **Best Social Impact Papers（最佳社会影响论文）**：
  - *DIA-HARM* — 基于 LLM 的有害数据合成流水线。
  - *Your Students Don't Use LLMs* — 高校 LLM 使用调查研究（2025 届）。
  - *Afri-MCQA* — 非洲语言医疗多选题 QA。
- **Best Demonstration Paper**：*olmOCR-7B*（AllenAI）— 文档解析推理模型，**08-01 已列**。
- **Outstanding Papers**：MauBERT（多任务 CV+语言、Berlin）、Evolutionary Guided Decoding（进化指导解码、北大/微软）、CoSToM（社交问答小样本）、(Inter-)Dimensionality Reductions（2017 年论文的重复性研究）。
- **SRW Best Paper**：*Reading Between the Lines*（对「提示工程的提示工程」进行实证测试）。

### 1.5 EMNLP 2025（完整获奖名单）— Suzhou, 2025-11-04 ~ 09；Main 22.16%（1,811）/ Findings 17.34%（1,417）

> 08-01 仅以 notable-papers 表覆盖；本期补全官方奖项（30 周年纪念届）。

- **Best Paper**：*Infini-gram mini: When Does Counting Suffice?* — Hao Xu, Jiacheng Liu, Yejin Choi, Noah A. Smith, Hannaneh Hajishirzi（UW / AI2）— 基于 n-gram 文档计数（suffix array + **BM25 类稀疏检索替代神经网络重排序**）在 keyphrase extraction / set prediction / NLI 任务上「counting suffices」；1B 参数内实现 ~20M n-gram 高效统计。
- **Outstanding Papers**：*LingGym*（面向语言智能体的多环境 LLM 评估 — Changbing Yang, Franklin Ma, Freda Shi, Jian Zhu）、*DiscoSG*（课程式结构化猜测、Wuhan/Monash/RMIT）、*Causal Interventions Reveal Shared Structure*（Boguraev, Potts, Mahowald — 因果干预揭示语言与视觉共享结构）。
- **Best Special Theme**：*InterIDEAS*（多语言心理疗法意图识别评估）。
- **Best Resource Paper**：*Autoformalization in the Wild*（Manuel B. Zhang, Marco Valentino, André Freitas — 自然语言→形式证明的野外自动形式化，数据质量 +10%、3,323 条标注验证）。
- **Best Social Impact**：*AccessEval*（无障碍 Web 评估框架）。
- **People's Choice**：*Randomly Removing 50% of Dimensions*（Takeshita et al. — 移除 50% 维度的行为扰动机制）。
- 审稿流程备忘：ARR 流（2024-12 ~ 2025-05）；委员会 Mirella Lapata + Owen Rambow。

### 1.6 WWW 2026（完整获奖名单）— Dubai, 2026-06-29 ~ 07-03

- **Best Paper**：*From Retrieval to Generation: Unifying External and Parametric Knowledge for Medical Question Answering* — Lei Li, Xiao Zhou, Yingying Zhang, Xian Wu — 医疗问答中将检索（external）与参数化（parametric）知识统一，「融合而非二选一」；作者机构待确认（(tentative) 中文医疗 AI 团队）。
- **Best Short Paper**：*DualGR: Generative Retrieval with Long and Short-Term Interests Modeling* — Zhongchao Yi, Kai Feng, Xiaojian Ma, Yalong Wang, Yongqi Liu, Han Li, Zhengyang Zhou, Yang Wang — 长短期兴趣分离的生成式检索（generative retrieval）模型；(tentative) Alibaba 系团队。
- **Test of Time**：*LINE: Large-scale Information Network Embedding*（2015）— Jian Tang, Meng Qu, Mingzhe Wang, Ming Zhang, Jun Yan, Qiaozhu Mei（MSRA / Tsinghua / Microsoft）— 一阶/二阶近邻分别建模的经典网络表示学习，是 DeepWalk→Node2Vec 时代与当代图模型共同的前驱。
- 会议数字：16 个 track、204 accepted（~35%）、1,300+ 投稿、来自 70+ 国家的 950+ 作者；Proceedings DOI 10.1145/3774904。

### 1.7 AAAI 2026（补充数字）— Philadelphia

- 08-01 已覆盖 5 Outstanding Papers + 2 AI for Social Impact。本期补：录用率 **17.6%**，三年最低；主题「Creating Collaborative Bridges Within and Beyond AI」；发表量与参与度再创新高。

### 1.8 NeurIPS 2025（补充 runners-up）

- 08-01 已覆盖 4 Best Papers（Gated Attention、Artificial Hivemind、Why Diffusion Don't Memorize、1,000-Layer RL）+ Faster R-CNN Test of Time。本期补 3 个 runner-ups：
  - *Does RL Really Incentivize Reasoning?*（Yue et al., Tsinghua — RL 究竟是否激励推理）
  - *Optimal Mistake Bounds for Transductive Online Learning*（Chase, Hanneke, Moran, Shafer）
  - *Superposition Yields Robust Neural Scaling*（Yizhou Liu, Ziming Liu, Jeff Gore — 叠加产生稳健的神经缩放律）

### 1.9 KDD 2026（提前公布）— Jeju, 2026-08-09 ~ 13（即将开幕）

- **Research Track Best Paper Award（提前公布）**：*PiPNN: Ultra-Scalable Graph-Based Nearest Neighbor Indexing* — Tobias Rubel, Richard Wen, Laxman Dhulipala, Lars Gottesbüren, Rajesh Jayaram, Jakub Łącki — **HashPartitioning**：让图索引构建完全并行化，规避传统 sequential crawl；单台多核机器 <20 分钟构建十亿规模索引；检索延迟 vs 构建成本图上超越 Vamana（**11.6×** 更快）与 HNSW（**12.9×** 更快）。arXiv:2602.21247。
- 与 08-03 digest 的 KDD 工业界深潜互补（本期为 research track 奖项）。

### 1.10 SIGIR 2026（状态）

- Melbourne/Naarm, 2026-07-20 ~ 24，已闭幕；656 篇录用（Full 234 / Perspective 12 / Reproducibility 28 / Resource 61 / Short 151 / Industry 131）。
- 官方 Best Paper 名单**尚未公布**（预计 8 月发布），本期标记为 pending-post-conference；08-01 notable table 已列代表性录用论文。

### 1.11 RecSys 2025（链接确认，不展开）

- 08-03 已确认 Best Full（Conformal Risk Control）与 Best Short（Beyond Top-1 counterfactual）。

---

## 2. 代码执行 / Agent 可靠性 / 长上下文 KV（2026-07 批次，此前未覆盖）

- **CARE: Pre-Execution Command Verification for Shell-Executing LLM Agents**（arXiv:2607.21642，submitted 2026-07-21）— Y. Liu, Barnabas Poczos, Jin B. Hong 等 — 在 **shell 命令真正执行前**验证其安全性/正确性：预执行阶段把命令拆解并对照系统状态做静态+仿真检查，拦截危险命令（rm -rf、curl|sh、权限逃逸等）。与 [arxiv-daily](./arxiv-daily.md) 中的 ThinkReset、TransMem 构成「Agent 可靠性」三件套：行为安全（CARE）、上下文管理（ThinkReset）、记忆持久化（TransMem）。
- **Latent Programming Horizons**（arXiv:2607.05188，2026-07-01）— Meta（FAIR）+ 多校 — **Agent 编程的 latent action space**：类比 RL 的 latent space planning，让编程 Agent 在「latent 编辑操作」而非 token 层面规划，序列化执行步骤减少、代码编辑效率提升、可回滚。编程模型在离线 RL 框架下训练，挑战「token-level 的编程 Agent 缺乏高层规划」的固有局限。
- **IAL-Scan: Information-Aware Latency Scanning for Hardware-Efficient LLM Serving**（arXiv:2607.01641）— 华中科大 — 信息密度感知的调度：动态稀疏预测每 token 的信息增益，感知网络带宽/GPU 算力的算力感知路由；SVD-LLM 压缩后 LongBench 平均 -1.5%，Cerebras/LLM 推理系统层与 [arxiv-ai-search](./arxiv-ai-search.md) 的 TokTier 状态化 tokenization 呼应。
- **Speculate with Memory: Lossless Acceleration for LLM Agents**（arXiv:2607.12236，2026-07-14）— Yu Li, Qinyuan Ye, Prafulla Kumar Choubey, Jiaxin Zhang, Chien-Sheng Wu — Agent 场景的 **speculative execution 升级**：现有 speculator 无状态，任务间信息全丢；本文给 speculator 挂三个在线记忆系统（contrastive transition table 动作序列统计、episodic memory 情境检索、confusion tracker 抑制重复错误）。六基准上 action prediction 相对精度 +19~39%，重复动作空间的 observation prediction 最高 **2.5×**；**lossless**（空闲期运行、零额外 wall-clock 成本、actor 轨迹与不投机执行完全一致）。
- **VarRate: Training-Free Variable-Rate KV Cache Compression**（arXiv:2607.15498，2026-07-16）— Shahrzad Esmat, Dhawal Shah, Ali Jannesari（Iowa State）— KV 压缩新思路「**分配 rank 而非 evict token**」：token-selection 系（SnapKV/Ada-KV）逐 token 打分+删除，query-agnostic 复用下精度崩 11~15 分；VarRate 按 query salience 给每 token 分配可变低秩预算，**零 token 被丢弃**，退化仅 3.5~5.5 分。20% 预算 + LongBench 16 任务，Llama-3.1-8B / Qwen2.5-7B 距未压缩模型 <0.8 分；比 uniform-rank 消融显著更强；相对 KVzip 精度等价但 **prefill 开销约 1/8**。与 [arxiv-daily](./arxiv-daily.md) 的 ResKV（频域）+ [arxiv-ai-search](./arxiv-ai-search.md) 的 Mixture-of-Translators 构成 KV 压缩三视角（token 级 / 频域级 / 低秩分配级）。

---

## 3. 综合趋势

1. **奖项名单完整性持续补齐**：WWW 2026（医疗 RAG 统一、DualGR、LINE ToT）、EMNLP 2025（Infini-gram mini「counting suffices」）、ACL 2026 资源/社会影响两条线、CVPR 2026 Best Student（TRELLIS.2）均为此前 digest 未覆盖的新信息；SIGIR 2026 待官方发布。
2. **Agent 可靠性成为主流评估维度**：CARE（命令预执行验证）+ Speculate with Memory（记忆增强投机执行）+ Latent Programming Horizons（latent 规划）从**安全、速度、规划**三个角度逼近「Agent 生产力」上限。
3. **推理成本控制双线并行**：VarRate（训练-free 低秩 KV 分配）与 IAL-Scan（信息感知调度）表明长上下文推理优化从「压缩算法」走向「分配+调度」的系统级协同。
4. **医学与跨语言成奖学热点**：WWW 2026 Best（医疗 RAG↔参数化统一）、ACL 2026 三篇 Social Impact 中含 Afri-MCQA（非洲语言医疗）、EMNLP 2025 InterIDEAS（多语言心理疗法）。

---

## 4. 关键链接

- CVPR 2026 官方 Best Papers：https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers
- CVPR 2026 第三方榜单：https://basic.ai/cvpr-2026-top-papers
- ACL 2026 Best Papers：https://2026.aclweb.org/program/best_papers/
- WWW 2026：https://www2026.thewebconf.org （Proceedings: https://dl.acm.org/doi/proceedings/10.1145/3774904）
- NeurIPS 2025 Awards：https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/
- SIGIR 2026 Proceedings：https://dl.acm.org/doi/proceedings/10.1145/3805712
- EMNLP 2025 Findings 统计：https://aclanthology.org/2025.findings-emnlp.0.pdf
- KDD 2026 PiPNN：https://arxiv.org/abs/2602.21247
- 本期 arXiv：CARE 2607.21642 / Speculate-with-Memory 2607.12236 / Latent-Programming-Horizons 2607.05188 / IAL-Scan 2607.01641 / VarRate 2607.15498

---

## 相关页面

- [2026-08-01 Conference Digest](../2026-08-01/conference-digest.md)（ICML/ACL/NeurIPS/CVPR/ICLR/AAAI 最佳论文基线）
- [2026-08-03 Conference Digest](../2026-08-03/conference-digest.md)（KDD 2026 工业界、RecSys/CIKM/SIGIR 2025 奖项）
- [2026-08-04 arXiv Daily](./arxiv-daily.md)、[2026-08-04 arXiv AI Search](./arxiv-ai-search.md)
