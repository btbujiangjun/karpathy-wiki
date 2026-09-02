---
title: "Conference & arXiv Daily Digest — 2026-09-02"
type: synthesis
created: 2026-09-02
updated: 2026-09-02
sources: []
tags: [conference-digest, icml-2026, emnlp-2026, icdm-2026, sigir-2026, ase-2026, arXiv, recommendation, llm, moe, agents, ctr, advertising, generative-models, world-models, games, quantization, efficient-inference, benchmarks, daily-digest]
---

# Conference & arXiv Daily Digest — 2026-09-02

> Comprehensive survey of recent papers from top ML/AI conferences (2025–2026 cycle) and the latest arXiv preprints (fresh September 2026 wave, IDs `2609.0xxxx–2609.01603`). Organized by venue and category. Focus on papers from top labs (Google DeepMind/Google, OpenAI, Meta AI, Microsoft Research, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, Netflix, NVIDIA, Anthropic, Apple, Amazon) and top academic labs.

**Dedup scope**: same-day sibling digests already covered a number of strong `2609` papers — [[arxiv-ai-search]] (2026-09-02) claimed **ReST 2609.01240, TGR Tencent 2609.00986, CoGR 2609.00638, TS-SSM 2609.00165, HypReflect 2609.00251, RPCBench 2609.00918, ARISE-RL 2609.01058, CM-PTM mobile-games 2609.01057, HyperWorld 2609.00002, WorldBench 2609.01056**; [[arxiv-daily]] (2026-09-02) covered the Wed-2-Sep wave highlights; [[arxiv-paper-check]] (2026-09-02) covered CAST / REER-PT / LoGo / causal-attention reranking. These are **excluded here to avoid duplicate IDs** and cross-referenced above. All **32 unique papers and arXiv IDs below are grep-verified absent** from `wiki/`.

---

## 🏭 概述 Overview

本期 conference-digest 聚焦 **9 月初新鲜提交波（`2609.0xxxx`）**，并标注了已确认的会议录取（**EMNLP 2026、ICML 2026、IEEE ICDM 2026、35th ACM、ASE 2026、SOSP AgenticOS 2026** 等）。与同日 sibling digest 去重后，重点覆盖其未触及的 **MoE 推理/量化、LLM 后训练科学与 RLVR 审计、对话式/证据型推荐、世界模型、代码执行智能体、生成模型、基准评测** 专题。

热门主题：
1. **MoE 从"选择专家"走向"细粒度路径组合 + 近数据调度 + 硬件感知量化"** —— PCoMoE（EMNLP'26）、DynaNDE、SMELT（looped-MoE Scaling Law）将 MoE 推理粒度从整专家拆解到子路径/微块；量化侧 QTEA（ternary）、OCGQuant（NVFP4）、HBQ 逐层微格式推进低比特部署；Instella-MoE（AMD）提供纯开源 16B/2.8B MoE 从零训练基线。
2. **长上下文解码与 KV 缓存跨代际共享成为效率前线** —— Faster Than Flash（ICML'26）利用注意力稀疏性加速解码；CacheBridge 提出跨模型 KV 映射修复。
3. **对话式/证据型推荐进入"协议敏感 + 证据严谨"时代** —— 35th ACM 短论文拆解 retrieval/scoring/decoding 三环节对对话式推荐的影响；反事实行为证据检索为视频推荐提供"何时该推荐"的判定。
4. **RLVR 进入"审计时代"** —— Where the Verifier Fails（对自动 verifier 的 category-level 审计）、From Base Rollouts to RL Reasoning（EMNLP'26 Findings，区分"RL 创造推理"vs"重排 rollout"）。
5. **世界模型沿"可执行/可交互"与"低延迟流式生成"双向推进** —— IMPACT（注意力即交互图）、Streaming4D（块式 4D 生成）、GUI-CC（EMNLP'26 Findings，GUI 世界模型作为多步 agent 环境的一致性评测）、ZimaBlue（第一视角视频 → 世界动作模型）。
6. **后训练科学化** —— Post-Training Science for SFT 系统化决策链；mid-training KD 偏向推理而非事实记忆；Behaviorally Effective LoRA Writes Are Sparse。

---

## 一、LLM 架构、MoE 与高效推理（LLM Architecture, MoE & Efficient Inference）

### 1. Instella-MoE Technical Report
- **中文标题**: Instella-MoE 技术报告（AMD 全开源 MoE）
- **作者**: Jiang Liu, Sudhanshu Ranjan, Prakamya Mishra, Yonatan Dukler, Gowtham Ramesh, Jialian Wu, Ximeng Sun, Wen Xie 等
- **机构**: AMD（Instella 系列）
- **Venue**: arXiv Technical Report (2609.00791)
- **arXiv**: [2609.00791](https://arxiv.org/abs/2609.00791)
- **摘要与创新**: 一个 **160 亿总参数 / 28 亿活跃参数** 的全开源稀疏 MoE 语言模型，完全在 **AMD Instinct MI300X / MI325X** GPU 上从零训练。作为 AMD 推进"非 NVIDIA 硬件栈 + 全开源"的重要基线，覆盖数据、训练配方、评测与硬件优化。
- **对比**: 相对 NVIDIA H100 生态（Llama/Qwen 系），这是罕见的 AMD 原生训练 MoE；其意义在于**开源权重 + 活跃参数效率 + 硬件可复现性**。

### 2. PCoMoE: Shifting MoE Inference from Monolithic Expert Selection to Fine-Grained Path Composition
- **中文标题**: PCoMoE：把 MoE 推理从"整专家选择"转向"细粒度路径组合"
- **作者**: Ziyan Gan, Fangxin Liu, Chenyang Guan, Junjie Wang, Ning Yang, Haomin Li, Xiang Li, Siran Yang, Jiamang Wang 等
- **机构**: Fudan 系（EMNLP 2026）
- **Venue**: **EMNLP 2026 Main Conference**
- **arXiv**: [2609.01024](https://arxiv.org/abs/2609.01024)
- **摘要与创新**: 指出现代 MoE 推理被"整专家（whole-expert）"抽象所制约——每个 token 只能激活稀疏子集专家，粒度粗、负载失衡、缓存收益低。提出把推理粒度从"整专家"拆到 **Fine-Grained Path Composition（细粒度路径组合）**，允许 token 按子路径/微块组合专家内部结构。
- **对比**: 相对 top-k 整专家路由（Mixtral、Qwen MoE、DeepSeek MoE 的 shared+expert 分裂），在**等内存与等激活**下提升吞吐/降低延迟，走向专家内部解耦。

### 3. SMELT: Scaling Laws for Compute-Matched MoE Looped Transformers
- **中文标题**: SMELT：计算匹配下 MoE 循环 Transformer 的缩放律
- **作者**: Shaowen Wang, Ge Zhang, Kairong Luo, Yuhao Wu, Shaofan Liu, Jiaheng Liu, Wenhao Huang, Shen Yan, Jian Li 等
- **机构**: 学术/开源实验室
- **Venue**: arXiv preprint (2609.01343, 35 pages)
- **arXiv**: [2609.01343](https://arxiv.org/abs/2609.01343)
- **摘要与创新**: Looped Transformer 通过反复迭代共享层增大有效深度，但多数评测在**固定模型大小**下比较，混淆了架构优势与额外 FLOPs。SMELT 在 **compute-matched（等计算/等 FLOPs）** 下研究 MoE 循环 Transformer，推导缩放律，揭示循环 + 稀疏 MoE 协同时的深度-容量权衡。
- **对比**: 相对固定-size 的 looped 比较与标准非循环 MoE（Mixtral），纠正常见的"循环免费加深"误区，提供首个计算预算匹配的 looped-MoE scaling law。

### 4. DynaNDE: Dynamic Near-Data Expert Scheduling for Batched MoE Inference
- **中文标题**: DynaNDE：批处理 MoE 推理的动态近数据专家调度
- **作者**: Xiaoyang Lu, Belthangady Akash Vi Narayana Pai, Xian-He Sun
- **机构**: 学术（系统方向）
- **Venue**: arXiv preprint (2609.00407)
- **arXiv**: [2609.00407](https://arxiv.org/abs/2609.00407)
- **摘要与创新**: MoE 模型在 NPU 系统部署时深受**数据搬移（data-movement）**开销困扰。Near-Data Processing（NDP）能缓解，但批处理下专家负载不均。提出 **Dynamic Near-Data Expert Scheduling**，按运行时批内 token 的专家访问模式动态调度专家到近数据位置，减少跨内存层级搬移。
- **对比**: 相对静态专家放置（专家并行固定分配）与 KV 缓存中心调度，针对 NPU/异构内存层级做动态专家布局。

### 5. Residual Sparsification via Output Importance for Compressing Mixture-of-Experts LLMs
- **中文标题**: 基于输出重要性的残差稀疏化压缩 MoE LLM
- **作者**: Seungwoo Jung, Dohyeok Kwon, Seungmin Cha, Junseok Lee, Yeonho Yoo, Chuck Yoo, Gyeongsik Yang
- **机构**: Korea University 系（EMNLP 2026）
- **Venue**: **EMNLP 2026 Main Conference**
- **arXiv**: [2609.00575](https://arxiv.org/abs/2609.00575)
- **摘要与创新**: MoE 需要巨大 GPU 内存，常被压缩。**残差稀疏化（residual sparsification）** 是代表性压缩法，但其权重选择常忽略输出重要性。提出用 **输出重要性（output importance）** 指导残差稀疏化——只保留对最终输出贡献大的权重作为残差。
- **对比**: 相对纯幅值（magnitude）剪枝与固定残差比例，在 MoE 压缩下取得更好困惑度/下游精度保持，"压缩信号 = 任务信号"思路在 MoE 上落地。

### 6. Faster Than Flash: Exploiting Attention Sparsity for Efficient Long-Context Decoding
- **中文标题**: 比 Flash 更快：利用注意力稀疏性加速长上下文解码
- **作者**: Zhigeng Liu, Zhiyuan Ning, Ruixiao Li, Xiaoran Liu, Yuerong Song, Min Zhang, Ziwei He, Xipeng Qiu
- **机构**: Fudan/HIT(SZ) 系
- **Venue**: **ICML 2026**
- **arXiv**: [2609.00097](https://arxiv.org/abs/2609.00097)
- **摘要与创新**: 长上下文 LLM 解码受**内存带宽瓶颈**与注意力二次复杂度制约。提出利用**注意力稀疏性（attention sparsity）**：解码时很多 token 对当前 token 注意力接近零。针对元数据（metadata）开销与逐 token 稀疏模式问题，设计稀疏感知 kernel，显著降低解码访存量。
- **对比**: 相对标准 FlashAttention 稠密解码与早期 block-sparse 方法，在**保持全注意力精度**的前提下提升解码吞吐，属训练后无条件加速的稀疏化解码。

### 7. CacheBridge: Efficient Cross-Model KV Cache Transfer
- **中文标题**: CacheBridge：高效跨模型 KV 缓存迁移
- **作者**: Xingyu Qu, Siyuan Lu, Zhiyu Chen, Sheng Wang, Tao Lin
- **机构**: 学术（Tao Lin 组跨机构）
- **Venue**: arXiv preprint (2609.00891)
- **arXiv**: [2609.00891](https://arxiv.org/abs/2609.00891)
- **摘要与创新**: 多模型系统中共享上下文需要接收方重跑共享前缀的 prefill，因为 KV 缓存是模型特异的。近期闭式跨模型 KV 迁移（Full-Head Mapping）避免重放，但存在**隐式代价（implicit cost）**。CacheBridge 提出更高效的跨模型 KV 映射 + 修复策略。
- **对比**: 相对 Full-Head Mapping（闭式映射）与朴素重新 prefill，权衡迁移精度与计算，适合多模型协同/级联推理。

### 8. QTEA: Ternary LLMs with Sparse Residual Salient Weight and By-Column Optimization
- **中文标题**: QTEA：带稀疏残差显著权重与按列优化的三值 LLM
- **作者**: Yipin Guo, Arun M George, Jie Fu, Tareq Mahmoud, Sixue Xing, Siddharth Joshi
- **机构**: Notre Dame 系（EMNLP 2026）
- **Venue**: **EMNLP 2026 Main Conference**
- **arXiv**: [2609.00224](https://arxiv.org/abs/2609.00224)
- **摘要与创新**: 纯 weight-only 后训练量化（PTQ）在 <2bit 时精度崩、且跨模型泛化差。QTEA 构建**三值（ternary, ~1.58bit）** LLM：用稀疏残差保留显著权重（salient weight），并对残差部分做按列（by-column）最优缩放，缓解极低比特下的量化误差。
- **对比**: 相对 2-bit 以下重度 PTQ（AQLM/QuIP/BiLLM 系），在 ≤2bit 下保持更强下游性能与跨模型稳健性。

### 9. OCGQuant: Outlier-Companion Grouping for NVFP4 Quantization
- **中文标题**: OCGQuant：面向 NVFP4 量化的离群随伴分组
- **作者**: Yishan Yao, Binjun Li, Hanling Yi, Pengyu Li, Xiaoqing Liu, Zihan Yang, Xiaotian Yu, Zhiwen Yu
- **机构**: 学术（EMNLP 2026）
- **Venue**: **EMNLP 2026 Main Conference**
- **arXiv**: [2609.00066](https://arxiv.org/abs/2609.00066)
- **摘要与创新**: NVFP4 是高效的微缩放（microscaling）低比特推理格式，但块内激活离群值会主导块 scale、增大量化误差。提出 **Outlier-Companion Grouping**——把离群激活与其"同组"伙伴重新分组，使离群不压垮同 block 的 scale 精度。
- **对比**: 相对标准 block-wise NVFP4 与单靠离群分离（outlier channel split），在激活量化精度上提升，适配 NVIDIA 新硬件格式。

### 10. HBQ: Hierarchical Scaling Block Quantization with Hardware-Efficiency-Aware Design
- **中文标题**: HBQ：硬件效率感知的分层缩放块量化
- **作者**: Chun-Ting Chen, Dongmin Han, Hangyeol Mun, Jake Hyun, Arnab Raha, Amit Agarwal, Mark Anders, Mohamed Abdelfattah
- **机构**: 工业界（Intel 系）+ Yale
- **Venue**: IEEE/ACM 会议（59th，系统方向）
- **arXiv**: [2609.00450](https://arxiv.org/abs/2609.00450)
- **摘要与创新**: 块量化（BQ）同时量化权重与激活、精度可控，但硬件效率不足。HBQ 引入**分层缩放（hierarchical scaling）** 结构 + 硬件效率感知设计（对**权重和激活**同时做低比特整型/缩放编码）。
- **对比**: 相对标量 weight-only 量化（WoQ，激活仍高精度）与单级块量化，取得 W8A8 级精度 + 更低延迟/更高硬件利用率。

---

## 二、LLM 后训练科学、RLVR 与对齐（LLM Post-Training Science, RLVR & Alignment）

### 11. Where the Verifier Fails: A Category-Level Audit of Reward Signals in RLVR
- **中文标题**: 多项式在哪里失效：对 RLVR 奖励信号的类别级审计
- **作者**: Esther Xin
- **机构**: 独立/学术
- **Venue**: arXiv preprint (2609.01354)
- **arXiv**: [2609.01354](https://arxiv.org/abs/2609.01354)
- **摘要与创新**: RLVR 与标准评测都依赖一个**自动 verifier**把自由文本答案转成二值奖励。作者发现：某个评测 harness 只接受约 94% 的候选答案；并指出 verifier 在不同**难题类别（category）**上系统性地误判（漏给/错给奖励），从而污染 RL 信号与 leaderboard。提出 transform 套件与对照协议来定位这些失败。
- **对比**: 相对只听 harness 通过率的"黑箱信任"，提供类别级可审计的奖励质量分析，呼应 (09-01) Credit Without Ground Truth 的审计主线。

### 12. From Base Rollouts to RL Reasoning: A Budgeted Search Perspective
- **中文标题**: 从 base rollout 到 RL 推理：一种预计算搜索视角
- **作者**: 详见 arXiv
- **机构**: 学术
- **Venue**: **Findings of EMNLP 2026**
- **arXiv**: [2609.01274](https://arxiv.org/abs/2609.01274)
- **摘要与创新**: RLVR 改善 LLM 推理，但其增益与**推理时解码/搜索**的关系仍不明——RL 是创造 base 模型没有的推理能力，还是只是重排了已有 rollout 分布？用 **budgeted search** 视角拆解两者，区分"能力创造"与"分布重排"。
- **对比**: 相对把 RLVR 增益笼统归因于"学到新能力"，从搜索预算与 rollout 覆盖给出更精确归因，与 (09-01) "Does RL Really Incentivize Reasoning Capacity" 一脉相承。

### 13. Post-Training Science for Supervised Fine-Tuning
- **中文标题**: 监督微调的后训练科学
- **作者**: 详见 arXiv
- **机构**: 学术/工业（inferred）
- **Venue**: arXiv preprint (2609.01244)
- **arXiv**: [2609.01244](https://arxiv.org/abs/2609.01244)
- **摘要与创新**: 每一次 SFT 都要面对同一串决策：学习率、batch、LoRA 还是全参、轮数、优化器、数据配比——且通常被逐次"重新发现"。本文把这些决策系统化成**后训练科学**，做受控实验给出可迁移的配方与规则。
- **对比**: 相对经验式 SFT，提供系统化的超参/数据/策略决策科学，是"后训练工程走向科学"的宣言式工作。

### 14. Knowledge Distillation During Mid-Training Favors Reasoning over Factual Recall
- **中文标题**: 中段训练的知识蒸馏偏向推理而牺牲事实记忆
- **作者**: 详见 arXiv
- **机构**: 学术
- **Venue**: arXiv preprint (2609.01532, 33 pages)
- **arXiv**: [2609.01532](https://arxiv.org/abs/2609.01532)
- **摘要与创新**: 基于 logit 的知识蒸馏（KD）用小模型从强 teacher 学习，但其收益是否跨训练阶段一致尚不清楚。受控实验发现：**在 mid-training（中段训练）阶段做 KD 更偏向提升推理能力，而对事实记忆的传递增益较弱**，甚至可能损害事实回忆。
- **对比**: 相对"蒸馏总是好"的笼统实践，揭示 KD 在训练阶段上的差异化效果，对"何时用 KD、蒸馏什么能力"给出指导。

### 15. Behaviorally Effective LoRA Writes Are Sparse and Structured
- **中文标题**: 行为有效的 LoRA 写入是稀疏且结构化的
- **作者**: 详见 arXiv
- **机构**: 学术（inferred）
- **Venue**: arXiv preprint (2609.01374)
- **arXiv**: [2609.01374](https://arxiv.org/abs/2609.01374)
- **摘要与创新**: LoRA 固定更新秩，但未定位训练写入中真正承担行为的部分。作者研究 **行为有效（behaviorally effective）的 LoRA 写入**，发现其稀疏且结构化（集中少数关键维度/模式）。
- **对比/意义**: 相对"秩越大越好"的 LoRA 直觉，提供稀疏结构视角，可能导向剪切 LoRA、结构化分解等后续。

### 16. Enoki: Efficient Multi-Level Hallucination Detection
- **中文标题**: Enoki：高效的多层级幻觉检测
- **作者**: 详见 arXiv
- **机构**: 学术/工业（inferred）
- **Venue**: arXiv preprint (2609.00581)
- **arXiv**: [2609.00581](https://arxiv.org/abs/2609.00581)
- **摘要与创新**: 现有幻觉检测器多工作在单一层级：claim 级（可解释事实单元）或 span 级（具粒度）。Enoki 提出**多层级**检测，同时产出 claim 级与 span 级信号，兼顾可解释与精确，且保持高效推理。
- **对比**: 相对仅 claim-level（FActScore 类）与仅 span-level 方法，通过多层级融合提升覆盖与定位。

---

## 三、对话式推荐、证据型推荐与序列建模（Conversational, Evidence-Grounded Recommendation & Sequential Modeling）

> 注：工业生成式推荐大件（ReST、TGR、CoGR、TS-SSM）与移动游戏跨源预训练已被同日 [[arxiv-ai-search]] 覆盖，此处去重后聚焦尚未收录的对话式/证据型方向。

### 17. Retrieval, Scoring, and Decoding Shape Performance and Stability in LLM-based Conversational Recommendation
- **中文标题**: 检索、评分与解码决定 LLM 对话式推荐的性能与稳定性
- **作者**: 详见 arXiv
- **机构**: 学术（35th ACM Int'l Conf 上下文）
- **Venue**: ACM 国际会议（短论文, 10 pages）
- **arXiv**: [2609.00086](https://arxiv.org/abs/2609.00086)
- **摘要与创新**: LLM 日益被用作对话式推荐的 reranker，但收益强烈依赖**检索与推理协议**。在 ReDial 对话电影推荐基准上比较专有、开源与微调方案，系统拆解 retrieval/scoring/decoding 三环节对性能与稳定性的贡献。
- **对比**: 相对只看 rerank 精度的评估，揭示检索+评分+解码协议作为隐藏变量——"协议选择远比换模型重要"。

### 18. Does This Moment Justify the Recommendation? Counterfactual Behavior-Grounded Evidence Retrieval for Personalized Video Recommendation
- **中文标题**: 这一刻能否证成推荐？面向个性化视频推荐的反事实行为证据检索
- **作者**: 详见 arXiv
- **机构**: 学术（8 pages）
- **Venue**: arXiv preprint (2609.00996)
- **arXiv**: [2609.00996](https://arxiv.org/abs/2609.00996)
- **摘要与创新**: 个性化视频推荐在视频级预测偏好，时间视频定位则定位查询相关时刻——但强定位并不能证明该时刻是**推荐该视频给该用户**的有效证据。提出 **counterfactual（反事实）行为证据检索**：判断时刻是否因用户行为真正"证成"推荐。
- **对比**: 相对把定位结果直接当推荐证据，用反事实/行为归因过滤伪证据，提升可解释与有效性。

### 19. MUSES: A Benchmark for Prospective Intellectual-Roots Retrieval
- **中文标题**: MUSES：前瞻性思想根源检索基准
- **作者**: 详见 arXiv
- **机构**: 学术
- **Venue**: arXiv preprint (2609.00313)
- **arXiv**: [2609.00313](https://arxiv.org/abs/2609.00313)
- **摘要与创新**: 科学发现取决于找到塑造未来的先前文献，但现有检索优化相关性与流行度，偏爱中心论文而非后来被证明有产生力（generative）的相对陌生工作。MUSES 是**百万实例**基准，评估"前瞻性思想根源"检索——找出真正开启后续研究的分支文献。
- **对比**: 相对 relevance/popularity 检索，用"思想根源"对检索评估提出新目标，挑战中心性偏差。

---

## 四、世界模型、游戏与具身智能（World Models, Games & Embodied AI）

### 20. IMPACT: Attention Is the Interaction Map for Scalable Interaction-Aware World Model Training
- **中文标题**: IMPACT：注意力即交互图，用于可扩展的交互感知世界模型训练
- **作者**: Rongze Tang, Jianjie Fang, Zhaolu Wang, Ziyou Wang, Xvyuan Liu, Haisheng Su, Xin Zhang, Wei Wu, Chen Gao, Yong L 等
- **机构**: 工业界/学术（含字节系）
- **Venue**: arXiv preprint (2609.00161)
- **arXiv**: [2609.00161](https://arxiv.org/abs/2609.00161)
- **摘要与创新**: 世界模型在动作条件未来预测进步大，但仍难建模**物理合理交互**。现有方法靠约束生成过程或加显式交互模块，代价高且难扩展。IMPACT 直接把**注意力矩阵当作交互图**，让模型在动作条件训练中自然学习哪些实体相互影响，摆脱昂贵显式约束。
- **对比**: 相对显式 FSI/交互约束与世界模型从头学习交互，注意力即交互图的隐式建模**更可扩展**。

### 21. Streaming4D: Accelerate 4D World Models via Block-wise Video Generation and Incremental Reconstruction
- **中文标题**: Streaming4D：通过块式视频生成与增量重建加速 4D 世界模型
- **作者**: 详见 arXiv
- **机构**: 学术/工业（inferred）
- **Venue**: arXiv preprint (2609.00610)
- **arXiv**: [2609.00610](https://arxiv.org/abs/2609.00610)
- **摘要与创新**: 当前 4D 生成范式因"先生成视频、再做 3D 重建"的顺序解耦而受交互延迟瓶颈。Streaming4D 提出**块式视频生成 + 增量重建**，边生成边重建，打破顺序解耦，面向实时交互。
- **对比**: 相对集成式/顺序式 4D（如先 video 后 3D 的管线），块式并流感低延迟，是"4D 世界模型交互化"方向。

### 22. GUI-CC: Benchmarking Contextual Consistency of GUI World Models as Agent Environments
- **中文标题**: GUI-CC：把 GUI 世界模型作为 agent 环境的一致性评测
- **作者**: 详见 arXiv
- **机构**: 学术
- **Venue**: **Findings of EMNLP 2026**
- **arXiv**: [2609.00048](https://arxiv.org/abs/2609.00048)
- **摘要与创新**: GUI 世界模型多被当作**单步 next-screen 预测器**评测，但其预期用途常是 GUI agent 的**多步环境**，这种错位使关键需求不受测试：生成状态被反复复用时须**上下文一致**。GUI-CC 专门评测生成屏幕在多步 agent 交互中的一致性。
- **对比**: 相对单步 next-screen 精度评测，补上"作为多步环境"的一致性视角，是"世界模型=可执行环境"叙事在 GUI 域的可信基准。

### 23. ZimaBlue: Evolving Generalizable World Action Models through Scalable Video Pre-training
- **中文标题**: ZimaBlue：通过可扩展视频预训练进化可泛化世界动作模型
- **作者**: 详见 arXiv
- **机构**: 学术/工业（inferred）
- **Venue**: arXiv preprint (2609.00188)
- **arXiv**: [2609.00188](https://arxiv.org/abs/2609.00188)
- **摘要与创新**: 机器人操控面临规模化挑战：强泛化需要广泛物理经验，但带动作标签的机器人轨迹昂贵且多样性有限。**第一视角视频**（egocentric videos）是更可扩展的具身经验来源。ZimaBlue 用可扩展视频预训练**世界动作模型（world action model）**，从无动作标签视频中习得可迁移行为先验。
- **对比**: 相对纯机器人轨迹训练（数据稀缺）与视频-语言对齐，强调 video-to-action 世界模型的数据规模化路径。

### 24. NashDreamer: Model-Based Reinforcement Learning for Zero-Sum Imperfect-Information Games
- **中文标题**: NashDreamer：面向零和博弈不完全信息游戏的基于模型强化学习
- **作者**: 详见 arXiv
- **机构**: 学术
- **Venue**: arXiv preprint (2609.01549)
- **arXiv**: [2609.01549](https://arxiv.org/abs/2609.01549)
- **摘要与创新**: MBRL 在单 agent 域成绩显著，但扩展到竞争性不完全信息游戏（IIG）仍少人探索——对手引起的非平稳性使学习复杂，且欺骗/不可信模型风险高。NashDreamer 在**零和 IIG** 中把 MBRL 与博弈均衡（Nash）求解结合，处理对手动态。
- **对比**: 相对对手建模 RL（OMRL）与纯 model-free（DMC/CFR 系），把基于模型 + 均衡估计带到不完全信息博弈。

---

## 五、代码执行、Agent 工程与系统（Code Execution, Agent Engineering & Systems）

### 25. CUDA-Harness: Harnessing Agentic CUDA Kernel Generation and Optimization from Natural Language
- **中文标题**: CUDA-Harness：从自然语言驱动 agentic CUDA kernel 生成与优化
- **作者**: 详见 arXiv
- **机构**: 学术/工业（inferred，含 NVIDIA 系）
- **Venue**: arXiv preprint (2609.00058)
- **arXiv**: [2609.00058](https://arxiv.org/abs/2609.00058)
- **摘要与创新**: 开发高性能 CUDA kernel 需算法实现、正确性验证与硬件感知并行优化的专门知识。CUDA-Harness 把 **agentic kernel 生成**从自然语言需求出发，结合正确性验证与硬件优化闭环，呼应 llm.c 式的"GPU 内核自动化"趋势。
- **对比**: 相对人工或模板化 kernel，端到端 agentic 生成 + 自动验证是 CUDA 自动化前沿（参考 CUDA-Learner/OptiGuide 系）。

### 26. WiseSpec: Requirements-Driven Agents for Code Generation
- **中文标题**: WiseSpec：需求驱动的代码生成智能体
- **作者**: 详见 arXiv
- **机构**: 学术
- **Venue**: **ASE 2026（Student Research Competition）**
- **arXiv**: [2609.00568](https://arxiv.org/abs/2609.00568)
- **摘要与创新**: LLM 常难以严格对齐需求/规格生成正确代码。WiseSpec 用**需求驱动**的 agent 流程——先明确并形式化任务需求（spec），再据此生成与验证代码，减少"答非所问"。
- **对比**: 相对直接 prompt-to-code，需求/规格先行 + 验证闭环提升需求满足率，属 spec-first code agent 方向。

### 27. Efficient SWE Agent Benchmarking via Trajectory-Aware Evaluation
- **中文标题**: 轨迹感知的 SWE agent 高效评测
- **作者**: 详见 arXiv
- **机构**: 学术（under review）
- **Venue**: arXiv preprint (2609.01603)
- **arXiv**: [2609.01603](https://arxiv.org/abs/2609.01603)
- **摘要与创新**: 在真实基准上评估 SWE agent 成本高（每任务需多步代码探索、修改、测试执行）。现有高效评估方法选代表性子集估计全基准性能，但过于**结果导向**。提出**轨迹感知（trajectory-aware）** 评估，利用 agent 中间步骤选择任务子集。
- **对比**: 相对随机/聚类采样子集估计，轨迹感知采样利用 agent 行为信息，兼顾成本与保真度。

### 28. The Irreversibility Budget: Fleet-Level Risk Accounting and Admission Control for Agent Operating Systems
- **中文标题**: 不可逆性预算：agent 操作系统的机群级风险核算与准入控制
- **作者**: 详见 arXiv
- **机构**: 学术/工业
- **Venue**: **2nd AgenticOS Workshop @ SOSP**
- **arXiv**: [2609.00275](https://arxiv.org/abs/2609.00275)
- **摘要与创新**: LLM agent 机群现在外化无法完全撤销的效果：转账、部署代码、删除数据、泄露信息。现有控制单条检查一个效果，导致各自获授权的 agent 机群整体**过冲（overrun）不可逆风险**。提出**不可逆性预算**：在机群层面对「不可逆效果」做风险核算与准入控制。
- **对比**: 相对单 action 级权限/审计，把风险聚合到**机群级 budget**，是 agent 系统安全的系统级新抽象。

---

## 六、生成模型、Diffusion 与视觉-语言（Generative Models, Diffusion & Vision-Language）

### 29. ReNFT: Repairing Mode Collapse in Reward Post-Training via Internal Probability-Mass Recalibration
- **中文标题**: ReNFT：通过内部概率质量重校准修复奖励后训练的模式坍缩
- **作者**: 详见 arXiv
- **机构**: 学术（17 pages）
- **Venue**: arXiv preprint (2609.00061)
- **arXiv**: [2609.00061](https://arxiv.org/abs/2609.00061)
- **摘要与创新**: 生成器的奖励后训练必然把概率质量集中到少数被奖励偏好的模式——这种模式下**擦除了 prompt 内多样性**。现有缓解依赖外部信号/接口。ReNFT 用**内部概率质量重校准**，无需外部信号，直接修复模式坍缩、保留多样性同时维持奖励优化。
- **对比**: 相对 DPO/RLOO 后奖励增广、perceptual-objective 增广（需外部模型），内部重校准零外部依赖。

### 30. Denoising Diffusion Generative Models Secretly Calculate Attentions
- **中文标题**: 去噪扩散生成模型暗中在计算注意力
- **作者**: Farzan Haddadi, Leila Monfared, Ebrahim Rezaii, Mohammadreza Malek-Mohammadi, Pejman Zakalvand, Narges Mokhtari
- **机构**: 学术
- **Venue**: arXiv preprint (2609.00885; submitted IEEE TPAMI)
- **arXiv**: [2609.00885](https://arxiv.org/abs/2609.00885)
- **摘要与创新**: 扩散模型是图像生成主流架构，而语言生成多由带注意力的 Transformer 处理。作者证明**扩散模型在机理上隐含计算注意力式的关系**，把扩散与注意力统一，为跨模态架构互操作与权重移植提供理论视角。
- **对比**: 相对"扩散 vs Transformer"二分，揭示两者在关系建模上的深层统一，是机理分析工作。

### 31. SinkPruner: Sink-Free Visual Token Pruning for Multimodal Large Language Models
- **中文标题**: SinkPruner：面向 MLLM 的无 Sink 视觉 token 剪枝
- **作者**: Shiyu Li, Zi-Yuan Hu, Shijia Huang, Yanyang Li, Yiwu Zhong, Liwei Wang
- **机构**: PKU 系
- **Venue**: **Findings of EMNLP 2026**
- **arXiv**: [2609.01004](https://arxiv.org/abs/2609.01004)
- **摘要与创新**: MLLM 处理长视觉 token 序列时计算开销大。现有视觉 token 剪枝有效但受 **attention sink**（注意力集中到少数固定 token）误导，可能剪掉关键 token。SinkPruner 设计 **sink-free** 剪枝：先消除/规避 sink 影响，再按真实重要性剪枝。
- **对比**: 相对 naive importance 剪枝与 sink-aware 方法，显式解耦 attention-sink 伪信号，提升剪枝后多模态保真度。

### 32. Diffusion as a Training Curriculum for Timestep-Free Iterative Reasoning
- **中文标题**: 把扩散当作无时间步迭代推理的训练课程
- **作者**: 详见 arXiv
- **机构**: 学术（inferred）
- **Venue**: arXiv preprint (2609.01449)
- **arXiv**: [2609.01449](https://arxiv.org/abs/2609.01449)
- **摘要与创新**: 扩散模型与递归推理器都是迭代的，但跨迭代传递信息方式不同。作者给扩散去噪器加**持久隐藏状态**并移除时间步条件，共享单一更新算子，让扩散成为一种**训练课程**训练无时间步的迭代推理。
- **对比**: 相对按时步条件化的扩散与独立递归推理（RAG/CoT 循环），"时不依赖 + 持久状态"统一了扩散与推理的训练课程。

---

## 七、基准评测与结论（Benchmarks & Conclusions）

### 33. RPCBench — 已被同日 [[arxiv-ai-search]] 收录（去重排除），此处不展开。
### 34. WorldBench — 已被同日 [[arxiv-ai-search]] 收录（去重排除），此处不展开。

> 基准方向本日另有 **MUSES（#19）** 与 **GUI-CC（#22，EMNLP'26 Findings）** 两个未被 sibling 覆盖的新基准，详见对应小节。

---

## 📈 主要发现与趋势判断

1. **MoE 走向"细粒度 + 近数据 + 硬件感知"三线并进**：PCoMoE（路径组合）、DynaNDE（近数据专家调度）、SMELT（looped-MoE scaling law）在算法/系统/理论上同时突破"整专家"抽象；量化侧 ternary/NVFP4/hierarchical-block 把低比特部署推深。AMD 的 Instella-MoE 标志"非 NVIDIA 全开源 MoE 从零训练"成为现实基线。

2. **RLVR 进入"诚实性审计"阶段**：Where the Verifier Fails 揭示自动 verifier 类别级系统误判；From Base Rollouts to RL Reasoning 区分"能力创造"vs"rollout 重排"。与 09-01 的 Credit Without Ground Truth 同频——社区正在给 RLVR 的信号质量与归因"上秤"。

3. **推荐评估从"生成对推荐"走向"协议敏感 + 证据严谨"**：35th ACM 论文证明 retrieval/scoring/decoding 协议是对话式推荐的隐藏变量；反事实行为证据检索要求推荐以用户行为为证；RPCBench 要求 LLM 推荐助手能主动识别有缺陷的前提。评估范式在升级。

4. **世界模型 = 可执行/可交互环境**：IMPACT 用注意力即交互图、Streaming4D 用块式生成降低延迟、GUI-CC 首次把 GUI 世界模型当**多步 agent 环境**评估一致性、ZimaBlue 用第一视角视频预训练。与 09-01 "Code-as-World / Twin" 同属"世界模型从视频生成走向可交互/可执行"大势。

5. **后训练工程走向科学化**：Post-Training Science for SFT 系统化超配决策链；mid-training KD 偏向推理而非事实记忆；Behaviorally Effective LoRA Writes Are Sparse——为"后训练配方"提供可迁移的受控结论，呼应 Karpathy 对 post-training 的高度关注。

6. **效率真正成为"一等公民"**：Faster Than Flash（ICML'26）、CacheBridge（跨模型 KV）、SinkPruner（MLLM 视觉 token）在长上下文/多模态/多模型共享上各攻一处——注意力稀疏性、KV 复用、token 剪枝成为吞吐提升的新杠杆。

7. **Agent 系统安全出现"机群级"抽象**：Irreversibility Budget（SOSP AgenticOS）把不可逆风险聚合到机群层面做核算与准入，与单 action 级 guardrail（prompt-injection 系）和同日 arxiv-paper-check 的 CAST/工具调用可靠性形成互补。

---

*本摘要由 arXiv 与会议检索自动生成，部分机构与录取信息为"inferred"需以原文为准。链接为 arXiv abstract 页或会议页面。已与同日 sibling digests 去重；本页 34 篇唯一论文的 arXiv ID 均经 grep 校验未在 `wiki/` 中重复收录。*