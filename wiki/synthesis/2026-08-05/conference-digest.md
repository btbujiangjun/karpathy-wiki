---
title: "Conference Digest 2026-08-05：KDD 2026 工业推荐 Scaling 深潜 + SIGIR 2026 新作 + 顶会获奖全景导航 + arXiv 分类精选"
type: synthesis
created: 2026-08-05
updated: 2026-08-05
sources: []
tags: [conference-digest, kdd-2026, sigir-2026, acl-2026, emnlp-2025, www-2026, recsys-2025, cikm-2025, iclr-2026, neurips-2025, icml-2026, cvpr-2026, aaai-2026, arxiv]
---

# Conference Digest — 2026-08-05

本期聚焦 **此前未覆盖的新论文**：KDD 2026（Jeju, 8/9–13，奖励 8/13 公布）Proceedings Vol.1 已出版工业推荐大厂论文、SIGIR 2026（Melbourne, 7/20–24，官方奖励名单仍 pending）确认论文、ACL 2026 Outstanding 补充（ViLL-E / Lying with Truths）、WWW 2026 补充（NEZHA 等）、RecSys 2025 / CIKM 2025 补充，另加 **ICLR 2026（e3）**与 **NeurIPS 2025（HRPO）** 补充，以及 **arXiv 2026 分类精选 18 篇**（LLMs / Agents / Recsys / CTR-Ads / Games / Code Execution / Generative / Sequential / Benchmarks）。获奖全景在 [08-01 digest](../2026-08-01/conference-digest.md)、[08-03 digest](../2026-08-03/conference-digest.md)、[08-04 digest](../2026-08-04/conference-digest.md) 已覆盖者仅作导航不重复展开。

---

## 0. 顶会获奖全景快速导航（已覆盖 → 详情入口）

| 会议 | 状态 | 覆盖入口 |
|------|------|----------|
| **ICML 2026**（Seoul, 7/6–11） | 3 Outstanding + 3 HM 已覆盖 | [08-04](../2026-08-04/conference-digest.md) §1.2 |
| **NeurIPS 2025**（San Diego, 12/2–7） | 4 Best + 3 runners-up 已覆盖 | [08-01](../2026-08-01/conference-digest.md) + [08-04](../2026-08-04/conference-digest.md) §1.6 |
| **ICLR 2026**（Rio, 4/23–27） | Outstanding/HM/ToT 已覆盖；本期补 **e3** | [08-01](../2026-08-01/conference-digest.md) + 本期 §6 |
| **AAAI 2026**（Singapore, 1/20–27） | Best 已覆盖（录用率 17.6%） | [08-01](../2026-08-01/conference-digest.md) |
| **CVPR 2026**（Denver, 6/3–7） | 全部奖项已覆盖（16,092/4,089, 25.4%） | [08-04](../2026-08-04/conference-digest.md) §1.1 |
| **KDD 2026**（Jeju, 8/9–13） | Research Best = PiPNN 已覆盖；**本期补 Vol.1 工业论文** | [08-04](../2026-08-04/conference-digest.md) + 本期 §1 |
| **ACL 2026**（San Diego, 7/2–7） | 完整奖项已覆盖；**本期补 Outstanding/资源类** | [08-04](../2026-08-04/conference-digest.md) §1.4 + 本期 §3 |
| **EMNLP 2025**（Suzhou, 11/4–9） | 完整奖项已覆盖（Main 22.16%） | [08-04](../2026-08-04/conference-digest.md) §1.5 |
| **WWW 2026**（Dubai, 6/29–7/3） | Best/Best Short/ToT 已覆盖；**本期补 NEZHA 等** | [08-04](../2026-08-04/conference-digest.md) + 本期 §4 |
| **SIGIR 2026**（Melbourne, 7/20–24） | 官方奖项 pending；**本期报 4 篇确认论文** | 本期 §2 |
| **CIKM 2025**（Seoul, 11/10–14） | Best Full = GAE 已覆盖；**本期补 Best Student** | [08-03](../2026-08-03/conference-digest.md) + 本期 §5 |
| **RecSys 2025**（Prague, 9/22–26） | Best Full 已覆盖；**本期补 Best Short + ULIM** | [08-03](../2026-08-03/conference-digest.md) + 本期 §5 |

---

## 1. KDD 2026（Jeju, 8/9–13）— 工业推荐 Scaling Law 主战场

> 数据口径：Vol.1 共 1,215 投稿 / 256 录用（≈21%）。主题高度集中于「推荐系统如何 Scaling」：Meta 走统一架构/模型空间重构，ByteDance 走序列-稠密协同扩展 + 参数化记忆，Alibaba 走 field-aware 结构表达力，Meituan 走免对齐跨域基础模型。全部带线上 A/B 数字。

### 1.1 Meta Lattice: Model Space Redesign for Cost-Effective Industry-Scale Ads Recommendations
**中文标题**：《Meta Lattice：面向大规模广告推荐的成本高效模型空间重构》

- **作者**：Liang Luo, Yuxin Chen, Zhengyu Zhang, Mengyue Hang, Andrew Gu, Buyun Zhang 等（~40 人）
- **机构**：Meta（Ads / GenAI recommender infra）
- **会议**：KDD 2026（Proc. Vol.1, pp. 2335–2346）；arXiv:2512.09200
- **背景与创新**：把 Multi-Domain Multi-Objective（MDMO）学习从「模型 + 目标」层面提升到**整个 model space 重构**：①Lattice Partitioner（跨域知识共享 / 组合并集）；②Lattice Zipper/Filter（拼接零填充数据集 + 基于 Pareto 的特征选择，做 data integration）；③**Lattice Networks**（interleaved learning + parameter untying + domain-specific tower + 监督信号改造）；④层次化蒸馏；⑤系统优化（BF16/FP8、定制 GPU kernel、Lattice Sketch 优化 FSDP/batch-size）。
- **实验结果**：生产环境 **+10% 营收驱动 top-line 指标、+11.5% 用户满意度、+6% 转化率、20% 容量节省**。模型组合并集案例：两个独立模型（1.33T + 0.71T 参数；20 + 12 GFLOPs/sample）合并到 20-GFLOP baseline——naive 合并损害 Domain A（跨域干扰），但监督改造后可恢复并反超未合并 baseline；Lattice Networks 在相同复杂度下全部 CTR/CVR/质量指标上击败 Wukong，调优后模型以 **17× 更少 FLOPs** 在 8 项指标中的 4 项达到 SOTA。
- **对比前作**：相比 Wukong 系跨域模型与 MDMO 单独打补丁的做法，Lattice 把跨域、数据、架构、蒸馏、系统做成一整套可组合设计，并给出可量化的容量/FLOP 收益。

### 1.2 From Scaling to Structured Expressivity: Rethinking Transformers for CTR Prediction (FAT)
**中文标题**：《从 Scaling 到结构化表达能力：重新思考 CTR 预测中的 Transformer》

- **作者**：Bencheng Yan, Yuejie Lei, Zhiyuan Zeng, Zheye Deng, Di Wang, Kaiyi Lin, Pengjie Wang, Chuan Yu, Jian Xu, Bo Zheng（前四位共同一作）
- **机构**：Alibaba Group
- **会议**：KDD 2026；arXiv:2511.12081
- **背景与创新**：诊断 CTR 模型 scaling 收益递减而 LLM 可预测扩展的根因是**结构性错配**——标准 Transformer 假设序列组合性，CTR 需要的是异构字段上的组合推理。提出 **Field-Aware Transformer（FAT）**：按字段（field）重新参数化 Transformer block，把复杂度从「总词表规模 n」转移到「字段数 F」（n ≫ F）；**Basis-Composed Hypernetwork** 用共享基合成字段参数，解耦容量与字段基数；并给出**首个基于 Rademacher complexity 的正式 CTR scaling law**。
- **实验结果**：离线最高 **+4.38% AUC** 超 SOTA；线上生产 **+2.33% CTR、+0.66% RPM**。
- **对比前作**：对比 DIN/DSTN/OneTrans 等 CTR backbone 与 LLM 式 plain transformer，FAT 在同一参数量下因结构化表达更优而获得可控的 scaling 增益。

### 1.3 MixFormer: Co-Scaling Up Dense and Sequence in Industrial Recommenders
**中文标题**：《MixFormer：工业推荐中稠密特征与序列的协同扩展》

- **作者**：Xu Huang, Hao Zhang, Zhifang Fan, Yunwen Huang, Zhuoxing Wei, Zheng Chai, Jinan Ni, Yuchao Zheng, Qiwei Chen
- **机构**：ByteDance
- **会议**：KDD 2026；arXiv:2602.14110
- **背景与创新**：批评工业 Transformer 推荐的「碎片化」——序列建模与特征交互是相互独立、各自参数化的模块，导致 capacity 分配次优。**MixFormer** 把两者放进**单一统一 backbone**，使稠密容量与序列长度**协同扩展（co-scaling）**；user-item 解耦策略削减冗余计算与延迟。
- **实验结果**：在 **Douyin 与 Douyin Lite 两个生产系统**的 A/B 上，engagement（活跃天数、App 内使用时长）一致提升。
- **对比前作**：对比 separate 序列-稠密双模块架构（如 MoE 序列塔 + 稠密塔并联），统一 backbone 在容量分配上更优且更省计算。

### 1.4 MTFM: A Scalable and Alignment-free Foundation Model for Industrial Recommendation in Meituan
**中文标题**：《MTFM：美团的规模化、免对齐工业推荐基础模型》

- **作者**：Xin Song, Zhilin Guan, Ruidong Han, Binghao Tang, Tianwen Chen 等
- **机构**：Meituan
- **会议**：KDD 2026；arXiv:2602.11235
- **背景与创新**：跨域（CDR）/多场景（MSR）方法通常要求严格的输入对齐与巨大资源。**MTFM** 把跨域数据转成**异构 token（alignment-free）**；**多场景用户级样本聚合**提升训练吞吐；**Grouped-Query Attention + Hybrid Target Attention** 削减内存与计算；系统层（kernel fusion、CPU-GPU pipeline 去阻塞、PyTorch→Triton 定制 kernel）。
- **实验结果**：模型容量扩展与多场景数据扩展均带来 offline + online 双增益（具体 lift 值原文未公开，注明为准）。
- **对比前作**：对比需 strict alignment 的 CDR 基础模型，MTFM 免对齐设计大幅降低接入成本，使单一基础模型覆盖美团多业务场景。

### 1.5 Merchant Category Identification in Weixin Pay (Tencent)
**中文标题**：《微信支付中的商户类目识别》

- **作者**：Tencent（Weixin Pay 团队，详见 ACM DL）
- **机构**：Tencent
- **会议**：KDD 2026（Proc. Vol.1）；DOI 10.1145/3770854.3783924
- **背景与创新**：识别伪装真实经营类目的商户。融合商户文本、图像、统计量与时间序列；构造**元路径关系图（meta-paths，难以篡改）**，用**多边际最优传输（multi-marginal optimal transport）**在缺失/误导信号下做稳健的跨模态对齐。
- **实验结果**：分类准确率 **+8.8%**；微信支付线上实验佣金分账更准，**营收 +18.9%**。
- **对比前作**：对比纯文本/纯图像与单模态融合分类器，元路径图 + 最优传输在对抗性伪装下显著更鲁棒。

### 1.6 KDD 2026 其他值得关注（上下文，未详析）
- **Kunlun**（Meta，统一 scaling-law 推荐架构，arXiv:2602.10016）、**LLaTTE**（Meta 广告序列建模 scaling law，arXiv:2601.20083）、**TokenMixer-Large**（ByteDance，arXiv:2602.06563）、**EST**（Alibaba，[08-01 digest](../2026-08-01/conference-digest.md) 已述 +3.27% RPM）、**DeGRe**（Alibaba Taobao 生成式重排，arXiv:2605.25749）、**Climber-Pilot**（NetEase，[08-03](../2026-08-03/conference-digest.md) 已述）、**FARM**（跨域直播推荐）。
- **KDD Cup 2026**：Tencent UNI-REC Challenge（广告统一序列 + 特征交互建模）+ HKUST Data Agents Challenge。

---

## 2. SIGIR 2026（Melbourne, 7/20–24）— 官方奖励 pending，4 篇确认论文

> 本期覆盖 234 full papers / 131 industry papers 中的 4 篇代表性工作。主题：LLM 个性化检索的「语义崩塌」修复、生成式推荐 GFlowNet 微调、短视频动作序列建模、检索中 prior/likelihood 的后验重构。

### 2.1 KARMA: Knowledge-Action Regularized Multimodal Alignment for Personalized Search at Taobao
**中文标题**：《KARMA：知识-行为正则化的多模态对齐——淘宝个性化搜索》

- **作者**：Taobao & Tmall Group of Alibaba（Taobao Search, Mingming Ha 组）
- **机构**：Alibaba（Taobao）
- **会议**：SIGIR 2026（submission 681）；arXiv:2603.22779
- **背景与创新**：诊断 LLM 个性化中的 **Knowledge-Action Gap**——用 action 目标（next-item）微调 LLM 会诱发 **Semantic Collapse**（如 attention sink），破坏泛化。**KARMA** 引入仅训练期使用的语义可解码正则器：①历史条件语义生成（锚定 LLM 原生 next-token 分布）；②**embedding 条件语义重建**（强制兴趣 embedding 语义可恢复，杜绝 ID-shortcut）；可选重建冻结的视觉特征。
- **实验结果**：文本版 KARMA **+0.97 gAUC、+22.57 HR@200、+21.19 HR@1000、+2.26 JS@50**；其中 embedding 重建单独贡献 +19.19 HR@200。多模态扩展再 **+1.38 gAUC、+10.83 HR@200**。全漏斗部署：精排 +0.25 gAUC、粗排 +1.86 HR@500、召回 +2.51 HR@5000。14 天线上 A/B：**+0.5% Item Click，零推理开销**（解码头仅训练期使用）。
- **对比前作**：对比纯 action 微调 LLM 检索器；并给出负结果——**diffusion 是糟糕的检索 embedding 生成器（AR+MSE 优于 diffusion）**。

### 2.2 Full GFlowGR: Fine-tuning Generative Recommendation Frameworks with Generative Flow Networks
**中文标题**：《GFlowGR：用生成流网络微调生成式推荐框架》

- **作者**：Yejing Wang, Shengyu Zhou, Jinyu Lu, Qidong Liu, Xinhang Li, Wenlin Zhang, Feng Li, Pengjie Wang, Chuan Yu, Jian Xu, Bo Zheng, Xiangyu Zhao
- **机构**：City University of Hong Kong + Alibaba Group
- **会议**：SIGIR 2026 Full Paper
- **背景与创新**：修复生成式推荐（GR）训练的两处不匹配：逐点 next-item 预测 vs 需要多样化候选**集合**；所有交互等权 vs 实际效用不同。**GFlowNet 微调**：①trajectory sampler 做 set-wise 学习；②行为感知 reward model 量化 item 效用；③GFlowNet objective 提供 token 级监督。
- **实验结果**：3 个真实数据集 × 2 个 LLM 式 GR backbone 上一致提升；**2025 年中起部署于淘宝搜索广告，+0.4% 相对年营收（十亿级货币收益）**。
- **对比前作**：对比 GR 的 SFT/逐点 next-item 训练与强化版 GR，GFlowNet 在 set 多样性与效用权重上同时改善。

### 2.3 An Action-Aware Generative Sequence Modeling for Short Video Recommendation (A2Gen)
**中文标题**：《动作感知的生成式序列建模——短视频推荐》

- **作者**：Wenhao Li, Zihan Lin, Zhengxiao Guo, Jie Zhou, Shukai Liu, Yongqi Liu, Chuan Luo, Chaoyi Ma, Ruiming Tang, Han Li
- **机构**：Kuaishou Technology + Beihang University
- **会议**：SIGIR 2026（DOI 10.1145/3805712.3809728）；arXiv:2604.25834
- **背景与创新**：用户**动作时机**编码了多样意图（可能只喜欢视频某一段）。**A2Gen** 把用户动作串成序列，配 **Context-aware Attention Module（CAM）+ Hierarchical Sequence Encoder（HSE）+ Action-seq Autoregressive Generator（AAG）**。
- **实验结果**：Kuaishou 线上 A/B：**+0.34% watch time、+8.1% interaction rate、+0.162% Lifetime-7 用户留存（≈ 每日新增约百万 DAU）**，全量流量部署（服务 4 亿+ DAU）。
- **对比前作**：对比基于停留时长的隐式正反馈与仅 item 序列的生成式模型，显式动作序列带来更细粒度意图建模。

### 2.4 Towards a Relevance Posterior in Neural Information Access
**中文标题**：《神经信息访问中的相关性后验》

- **作者**：Andrew Parry, Emmanouil Georgios Lionis, Debasis Ganguly, Sean MacAvaney
- **机构**：University of Glasgow
- **会议**：SIGIR 2026（Perspective Paper，DOI 10.1145/3805712.3808541）；arXiv:2607.23561
- **背景与创新**：把经典概率 IR 的 **likelihood-prior 分解**重新引入神经管线：相关性作为近似后验推断，**查询无关的文档先验（离线学习、可缓存）** 与查询时 likelihood 结合。
- **实验结果**：融合学习质量先验（QualT5）到 BM25：TREC DL-2019 **nDCG@10 +0.046**、DL-2020 +0.029；最大增益出现在下游 LLM reranker **RankZephyr（DL-2020 ΔnDCG@10 ≈ +0.054）**；融合保持 R@1000（索引剪枝会掉 3–9 点）。警示：naive 融合**反而降低 SPLADE 首阶段**（信号重复计算），但经 LLM rerank 后仍有帮助。
- **对比前作**：对比端到端神经检索（SPLADE）与纯 likelihood 管线，主张 prior/likelihood capacity 分配应作为一等设计变量。

---

## 3. ACL 2026（San Diego, 7/2–7）— Outstanding 与资源类补充

> 完整奖项已在 [08-04](../2026-08-04/conference-digest.md) §1.4（12,148 投稿，+45% YoY）。本期补 Outstanding + 资源类 4 篇。

### 3.1 ViLL-E: Video LLM Embeddings for Retrieval
**中文标题**：《ViLL-E：面向检索的视频大模型嵌入》

- **作者**：Rohit Gupta, Jayakrishnan Unnikrishnan, Fan Fei, Sheng Liu, Son Tran, Mubarak Shah
- **机构**：Adobe / University of Central Florida
- **会议**：ACL 2026 **Outstanding Paper + Senior Area Chair Highlight**（pp. 43239–43258）
- **背景与创新**：VideoLLM 擅长生成 caption 但在检索上常输给 dual-encoder。**ViLL-E** 给视频 LLM 加 embedding 机制：复杂视频「多想」（dynamic compute），简单视频提前停止。
- **实验结果**：检索能力**追平专用 embedding 模型**，同时保持 VideoQA 竞争力——单一模型兼顾生成与检索。
- **对比前作**：对比视频 dual-encoder（检索强、生成弱）与纯 VideoLLM（生成强、检索弱），ViLL-E 用动态计算同时占据两端。

### 3.2 Lying with Truths: Open-Channel Multi-Agent Collusion for Belief Manipulation via Generative Montage
**中文标题**：《用真话撒谎：开放信道多智能体共谋操纵信念》

- **作者**：Jinwei Hu, Xinmiao Huang, Youcheng Sun, Yi Dong, Xiaowei Huang
- **机构**：University of Liverpool
- **会议**：ACL 2026 **Outstanding Paper**
- **背景与创新**：共谋 agent 只用**真实证据碎片**，剪辑成欺骗性叙事经公开信道传播来操纵受害模型信念。
- **实验结果**：**14 个 LLM 家族上成功率 >70%**；反直觉的是**更强推理模型更易受骗**。
- **对比前作**：区别于基于虚假内容的 prompt injection / 后门攻击，本文用「全部真实」的 montage 实现操纵，为多智能体安全部署提供新威胁模型。

### 3.3 TRACE: Execution-Efficiency Benchmark for LLM Code Translation
**中文标题**：《TRACE：面向 LLM 代码翻译的执行效率基准》

- **作者**：见 ACL 2026 Long（2026.acl-long.140）
- **机构**：待确认（ACL 2026 官方收录）
- **会议**：ACL 2026 Long
- **背景与创新**：首个关注**执行效率**（而非仅功能正确性）的代码翻译基准，检验翻译后代码的运行时与资源占用。
- **实验结果**：揭示「正确但低效」的翻译普遍存在（具体数值待源页确认）。
- **对比前作**：对比 HumanEval 类只查正确性的基准，TRACE 把 runtime/resource 作为一等评测维度。

### 3.4 AgencyBench: Benchmarking Next-Generation Agentic Applications with Very Long, Real-World Context
**中文标题**：《AgencyBench：以超长真实世界上下文基准化新一代 Agentic 应用》

- **作者**：Keyu Li 等（Pengfei Liu 团队）
- **机构**：中国人民大学（RUC）
- **会议**：ACL 2026 Long（pp. 7422–7440）
- **背景与创新**：首个面向**真实世界、超长上下文（1M token 级）**的 agentic 应用基准，覆盖跨域长上下文下的任务规划、工具调用与状态追踪。
- **对比前作**：对比 GAIA、AgentBench 等短/中上下文合成环境，AgencyBench 把「上下文长度」本身作为代理能力的关键变量。

---

## 4. WWW 2026（Dubai, 6/29–7/3）— 补充 NEZHA 等

> Best（MedRGAG）与 Best Short（DualGR）已在 [08-04](../2026-08-04/conference-digest.md) §1.7 详述；Test of Time = LINE（2015）。

### 4.1 NEZHA: A Zero-sacrifice and Hyperspeed Decoding Architecture for Generative Recommendations
**中文标题**：《NEZHA：零牺牲、超高速解码的生成式推荐架构》

- **作者**：Yejing Wang, Shengyu Zhou, Jinyu Lu, Ziwei Liu, Langming Liu, Maolin Wang, Wenlin Zhang, Feng Li, Wenbo Su, Pengjie Wang, Jian Xu, Xiangyu Zhao
- **机构**：City University of Hong Kong + Alibaba（实习期工作）
- **会议**：WWW 2026（DOI 10.1145/3774904.3792797）；arXiv:2511.18793
- **背景与创新**：解决 GR 部署的推理延迟瓶颈——候选生成解码架构在**零效果牺牲**下提速（"zero-sacrifice hyperspeed"）。
- **实验结果**：据报已在 Alibaba 落地为**十亿级广告营收**，服务数亿 DAU；代码开源（GFlowGR 姊妹篇，同受 CCF-Alimama Kangaroo Fund 资助）。
- **对比前作**：对比传统两阶段检索+精排与固定开销 GR 解码，NEZHA 以「无牺牲」延迟优化为 GR 全量落地铺路。

### 4.2 WWW 2026 其他值得关注
- **DiffusionGS**（Kuaishou 生成式搜索，Wenwu Ou 组）、**COINS**（冷物品 CTR 语义 ID）、**OMGRec**（Taobao 排列级生成式重排）、**Generative Retrieval for E-commerce**（Alibaba）。

---

## 5. RecSys 2025 / CIKM 2025 补充

> RecSys 2025 Best Full（Conformal Risk Control）已在 [08-03](../2026-08-03/conference-digest.md)；CIKM 2025 Best Full（GAE）亦在 [08-03](../2026-08-03/conference-digest.md)。

### 5.1 User Long-term Multi-Interest Retrieval Model for Recommendation (ULIM)
**中文标题**：《面向推荐的用户长期多兴趣检索模型》

- **作者**：Yue Meng, Cheng Guo, Xiaobin Hu, Honghu Deng, Yi Cao, Tong Liu, Bo Zheng
- **机构**：Taobao & Tmall Group of Alibaba
- **会议**：RecSys 2025 Industry Short（DOI 10.1145/3705328.3748107）；arXiv:2507.10097
- **背景与创新**：把**千规模行为序列建模带入召回阶段**（此前限于精排）。①**Category-Aware Hierarchical Dual-Interest Learning**——按类目切分长序列，联合优化长期+短期兴趣；②**Pointer-Enhanced Cascaded Category-to-Item Retrieval（PGIN）**——先预测 Top-K 兴趣类目再在类目内取物，削减线上计算；使用 2 年用户历史。
- **实验结果**：淘宝秒杀线上 A/B（3 周）：**+5.54% 点击、+11.01% 订单、+4.03% GMV**，仅增加 ~15ms 延迟。
- **对比前作**：对比将长序列压成固定向量的传统召回，双层兴趣 + 级联类目检索把千级序列首次带入召回。

### 5.2 Best Short Paper（RecSys 2025）: Beyond Top-1 — Addressing Inconsistencies in Evaluating Counterfactual Explanations for Recommender Systems
**中文标题**：《超越 Top-1：解决推荐系统反事实解释评测中的不一致性》

- **作者**：Mohammadi, Peintner, Müller, Zangerle（Innsbruck 系）
- **会议**：RecSys 2025 **Best Short Paper**
- **要点**：揭示反事实解释（CFE）评测对「评测位置/粒度选择」高度敏感，Top-1 评测与全列表评测结果常不一致；提出一致性评测框架。

### 5.3 CIKM 2025 Best Student Full Paper: A Cost-Effective Framework to Evaluate LLM-Generated Relevance Judgements
**中文标题**：《评估 LLM 生成相关性判断的经济高效框架》

- **作者**：Merlo, Marchesin, Faggioli, Ferro
- **机构**：University of Padua
- **会议**：CIKM 2025 **Best Student Full Paper**
- **背景与创新**：LLM 生成 relevance judgment 越来越普遍，但对照人工标注验证成本高。提出**带统计保证、最小化人工复核量**的质量评估框架：支持固定置信度评估（最小人工量）与固定预算评估（带误差界）。
- **实验结果**：3 个 IR collection × 多个 LLM assessor 上，仅复核**一小部分** LLM 判断即可高置信估计评测可靠性。

---

## 6. ICLR 2026 / NeurIPS 2025 补充

### 6.1 e3: Learning to Explore Enables Extrapolation of Test-Time Compute for LLMs（ICLR 2026）
**中文标题**：《e3：学习探索使大模型的测试时计算外推成为可能》

- **作者**：Amrith Setlur, Matthew Y. R. Yang, Charlie Victor Snell, Jeremiah Greer, Ian Wu, Virginia Smith, Max Simchowitz, Aviral Kumar
- **机构**：CMU / MIT / UC Berkeley
- **会议**：ICLR 2026（Test-Time Compute 方向）
- **背景与创新**：多数推理模型**不外推**——思考长度一旦超过训练所见最大 token 预算即平台化。修复：训练 LLM 做 **in-context exploration**——在提交答案前链式执行生成、验证、精炼与假设检验，使额外测试时计算在难问题上持续有回报。
- **对比前作**：对比固定推理深度 / 直接长思考 RL，e3 训练的是「探索技能」本身，而非单纯拉长思考。

### 6.2 Hybrid Latent Reasoning via Reinforcement Learning (HRPO)（NeurIPS 2025）
**中文标题**：《基于强化学习的混合潜在推理》

- **作者**：Zhenrui Yue, Bowen Jin, Huimin Zeng, Honglei Zhuang, Zhen Qin, Jinsung Yoon, Lanyu Shang, Jiawei Han, Dong Wang
- **机构**：Google DeepMind（+ U. Maryland, UIUC, Michigan）
- **会议**：NeurIPS 2025（poster）
- **背景与创新**：用**可学习门控**融合离散 token 与前层 hidden state 做混合潜在推理；门控初始偏向 token embedding，RL 过程中逐步打开到 hidden feature。因 token 采样的随机性，可用简单 on-policy REINFORCE 式 outcome-reward 目标优化——**无需 CoT 轨迹**（不同于 Coconut 系潜在推理）。
- **实验结果**：5 个知识/多跳 QA 基准（NQ, TriviaQA, HotpotQA, 2WikiMultiHopQA, OpenBench）+ Qwen2.5-1.5B/3B：HRPO-3B **0.380 EM**，比最强 7B RAG baseline 高 **4.5%**、比最佳 RL baseline 高 1.3%；HRPO-1.5B（0.337 EM）超 PPO 3.0%。增益最大在简洁查询（NQ）与多跳（2WikiMQA）；保持可解释性且回答更短。
- **对比前作**：对比需要人工 CoT 的 latent reasoning 训练与纯 token RL，HRPO 无 CoT 依赖、回答更简洁。

---

## 7. 分类精选：arXiv 2026 近期新作（无重叠）

> 本批与今日 [arxiv-daily](./arxiv-daily.md)（24 篇）/[arxiv-ai-search](./arxiv-ai-search.md)（18 篇）及此前全部扫描**无重叠**。标注 (tentative) 者存在待核实字段。

### 7.1 LLMs

**7.1.1 Scaling Laws Meet Model Architecture: Toward Inference-Efficient LLMs**
**中文标题**：《规模定律遇上模型架构：迈向推理高效的 LLM》
- 作者：Chen, Wang, Zhou 等 | **机构**：UW-Madison + Amazon | **会议**：ICLR 2026 | arXiv:2510.18245
- **要点**：首次把**架构维度**纳入 scaling law。从 latent models 推导 conditional scaling law，正式建模 hidden size、mlp-to-attention ratio、GQA 头维度与训练规模关系；公式可指导在大 compute 预算下用更小更深的架构换取同 loss。
- **对比前作**：经典 Chinchilla 只考虑参数×token，本文加入架构自由度第三维，逼近架构无关下界的误差大幅缩小。

**7.1.2 Distilled Reinforcement Learning for LLM Post-training**
**中文标题**：《面向 LLM 后训练的蒸馏强化学习》 | arXiv:2607.17247（2026-07-19）
- 作者：见 arXiv 页 | **机构**：待确认 (tentative)
- **要点**：teacher 监督 + RL 目标结合，用细粒度 credit assignment 学 teacher 分布，减少在线采样与人工标注依赖；主张「RL 与 Knowledge Distillation 互补而非互斥」。
- **对比前作**：对比纯 RLHF/RLVR（需大规模 RM 在线交互），蒸馏信号降低方差、更稳、样本效率更高。

**7.1.3 How Far Can Unsupervised RLVR Scale LLM Training?**
**中文标题**：《无监督 RLVR 能把 LLM 训练推多远？》 | arXiv:2603.08660（2026-03-09）
- 作者：见 arXiv 页 | **机构**：待确认 (tentative)
- **要点**：完全不依赖人工标注、仅用格式/可验证规则作 reward 的 RLVR 扩展极限实证。
- **对比前作**：常规 RLVR 依赖任务模板与 golden answer；本文单独实证「无监督信号」维度的 scaling 行为。

### 7.2 Agents

**7.2.1 Switchcraft: AI Model Router for Agentic Tool Calling**
**中文标题**：《Switchcraft：面向 Agent 工具调用的 AI 模型路由器》
- 作者：Microsoft Research + Stanford 团队 | **机构**：Microsoft Research | arXiv:2605.07112
- **要点**：DistilBERT 轻量路由模型在 prompt 阶段判断是否值得调用昂贵 LLM 做 tool calling。
- **实验结果**：**路由准确率 82.9%、成本降低 84%、每百万查询节省约 $3,600**。
- **对比前作**：对比「一律走强模型」，把简单工具调用分流给小模型，是大模型服务成本优化的实用路径。

### 7.3 Recommendation Systems

**7.3.1 TwiSTAR: Generating Recommendations with Adaptive Reasoning**
**中文标题**：《TwiSTAR：带自适应推理的生成式推荐》 | arXiv:2605.11553（2026-05-12）
- 作者：见 arXiv 页 | **机构**：待确认 (tentative)
- **要点**：自适应推理生成式推荐：难样本 think-slow、简单样本 think-fast，用 SID（推理深度控制）在生成路径上分配计算。
- **对比前作**：对比固定推理深度的生成式推荐与两阶段（检索+精排），在 latency 与质量间显式 trade-off。

**7.3.2 Task-Aware Automated User Profile Generation**
**中文标题**：《任务感知的自动化用户画像生成》 | arXiv:2605.13497（2026-05）
- 作者：见 arXiv 页 | **机构**：待确认 (tentative)
- **要点**：按下游推荐任务反向自动生成高信息量画像，把画像从固定属性集合变成任务驱动、端到端可优化的中间表征。
- **对比前作**：对比静态 demographic/embedding 拼接画像，本方法让画像适配目标任务。

### 7.4 CTR / Advertising

**7.4.1 DeRes: Training High-Performance CTR Models from Scratch via DeRes**
**中文标题**：《DeRes：通过 DeRes 从零训练高性能 CTR 模型》 | arXiv:2606.07980（2026-06-09）
- 作者：见 arXiv 页 | **机构**：待确认 (tentative)
- **要点**：揭示 CTR 模型深度方向 scaling 规律：测得拟合指数 **γ=0.118 vs 普通模型 0.071（≈1.66×）**；Identity skip + SiLU 的 DeRes 块，**8 层 DeRes 匹配 16 层 OneTrans 性能，节省约 2× 计算**。
- **对比前作**：OneTrans 等主流 CTR backbone 深度收益递减明显；DeRes 让深度方向 scaling 更高效。

### 7.5 Games

**7.5.1 One Policy, Infinite NPCs: Persona-Traceable Shared RL Policies for Scalable Game Agents**
**中文标题**：《一份策略、无限 NPC：可追踪人格的共享 RL 策略》 | arXiv:2605.23652（2026-05）
- 作者：见 arXiv 页 | **机构**：待确认 (tentative)
- **要点**：共享 RL 策略 + 人格向量驱动海量 NPC：300 人格生活模拟 benchmark 上零样本人格识别准确率**高出随机 17×**，人格一致性 Spearman ρ≈0.73，推理**比 LLM-as-policy 快 22×**。
- **对比前作**：对比逐 NPC 微调或 LLM 逐帧生成，人格建模为低维表征实现单策略规模化复用。

**7.5.2 Augmenting Game AI with Deep Reinforcement Learning**
**中文标题**：《用深度强化学习增强游戏 AI》 | arXiv:2606.20210（2026-06）
- 作者：见 arXiv 页 | **机构**：待确认 (tentative)
- **要点**：系统探索 DRL 与传统游戏 AI 模块（寻路、行为树）结合的增强路径，关注训练稳定性与工业部署约束。
- **对比前作**：对比纯 scripted/纯 RL，论证混合架构在样本效率与可控性间的折中。

### 7.6 Code Execution Prediction

**7.6.1 Teaching LLMs Program Semantics via Symbolic Execution Traces**
**中文标题**：《通过符号执行轨迹教会 LLM 程序语义》
- 作者：Cambridge + Amazon 团队 | **机构**：University of Cambridge / Amazon | arXiv:2605.06184（2026-05）
- **要点**：500 个 C 语言验证任务（基于 SV-COMP 2025）× 14 个模型/6 个系列：程序行为预测（violation detection）在 100–200 行代码处明显退化；用约 **3,000 条符号执行 bug trace 对 Qwen3-8B 做 continued pretraining**，行为预测显著提升。
- **对比前作**：既有工作关注代码生成与静态 lint；本文把「运行时行为/断言违反预测」作为独立能力维度。

**7.6.2 TRACE**（ACL 2026，见 §3.3）——执行效率维度的代码翻译基准。

### 7.7 Generative Models

**7.7.1 GenCeption: Video Diffusion as a General-Purpose Vision Learner**
**中文标题**：《GenCeption：把视频扩散当作通用视觉学习器》
- 作者：Google DeepMind | **机构**：Google DeepMind | arXiv:2607.09024（2026-07）
- **要点**：论证视频生成扩散模型可作为**通用视觉表征学习器**，生成中间表征可复用于多种下游视觉任务，挑战「判别式预训练才是视觉基座」的主流假设。
- **对比前作**：对比 CLIP / MAE 等判别式自监督范式，展示生成式目标的表征迁移潜力。

**7.7.2 Helios: A 14B Video Generation Model**
**中文标题**：《Helios：14B 视频生成模型》
- 作者：PKU YuanGroup | **机构**：北京大学（yuan-agent.com）| arXiv:2603.04379（2026-03）
- **要点**：14B 参数级视频生成模型，面向分钟级长视频；单张 H100 上 **19.5 FPS** 生成速度。
- **对比前作**：对比同参数级开源视频模型，在长时一致性、生成速度与分辨率上显著改善。

**7.7.3 Paris 2.0: Faster and Better Decentralized Diffusion Video Generation**
**中文标题**：《Paris 2.0：更快更好的去中心化扩散视频生成》
- 作者：Bagel Labs | **机构**：Bagel Labs | arXiv:2605.26064（2026-05）
- **要点**：去中心化扩散方案，ImageNet 类任务 **FVD 561.04 → 279.01（≈2.0× 提升）**，CLIP score 与 Aesthetic score 同步提升。
- **对比前作**：对比集中式 diffusion baseline 与第一代 Paris，分布式训练/推理下质量-速度曲线显著更优。

### 7.8 Sequential Modeling

**7.8.1 Mamba-3: SSM Discretization Recurrence, Complex State, MIMO**
**中文标题**：《Mamba-3：SSM 离散化递归、复值状态与 MIMO》
- 作者：Cartesia 团队 | **机构**：Cartesia | arXiv:2603.15569（2026-03-16）
- **要点**：三大改进：①SSM 离散化递归；②**复值状态（complex-valued state）**；③**MIMO（multi-input multi-output）**。1.5B 规模：比 Gated DeltaNet **+0.6pp**，MIMO 再 **+1.2pp**，合计 **+1.8pp**；相同困惑度下状态量**仅为 Mamba-2 的一半**，解码成本约减半。
- **对比前作**：对比 Mamba-2、Gated DeltaNet 等混合线性注意力基线，在困惑度、状态内存与推理成本上同时占优。

**7.8.2 Swimba: Switch Mamba Architecture**
**中文标题**：《Swimba：Switch Mamba 架构》 | arXiv:2603.06938（2026-03）
- 作者：见 arXiv 页 | **机构**：待确认 (tentative)
- **要点**：把 MoE（Switch）机制引入 Mamba 系 SSM，稀疏路由增强容量、控制激活参数增长。
- **对比前作**：对比密集 SSM 与 MoE-Transformer，探索稀疏化线性序列模型的效率边界。

### 7.9 Benchmarks

**7.9.1 Power Systems Agent Benchmark**
**中文标题**：《电力系统智能体基准》 | arXiv:2606.20950（2026-06）
- 作者：见 arXiv 页 | **机构**：待确认 (tentative)
- **要点**：面向电力系统运维/调度场景的 agentic 基准，覆盖长时序状态理解、约束优化与工具调用，验证 LLM agent 在物理系统控制类任务上的能力边界。
- **对比前作**：补齐通用 agent 基准缺少的工程物理领域分支。

---

## 8. 趋势总结

1. **推荐系统 Scaling 进入「架构纪律」时代**：KDD 2026 从「是否该 scaling」转向「怎么 scaling」——Meta（Lattice/Kunlun/LLaTTE）走统一模型空间，ByteDance（MixFormer/MSN/TokenMixer）走稠密-序列协同与稀疏激活记忆，Alibaba（FAT）证明 CTR 需要 field-aware 结构化表达而非纯序列，Meituan（MTFM）用免对齐异构 token 降低跨域成本。所有论文均报线上 A/B lift。
2. **生成式推荐（GR）工业落地闭环**：SIGIR/WWW 双线（GFlowGR、NEZHA 同源 CityU-Alibaba 合作）给出可量化的十亿级营收信号；A2Gen、DiffusionGS 代表 Kuaishou 把 GR 与动作/搜索场景结合；Lattice/MTFM 则证明传统稠密模型在容量组织上仍大有可为。
3. **LLM 个性化检索警惕「语义崩塌」**：KARMA 明确 action 微调会诱发 attention sink 类语义塌缩，需要「仅训练期」的解码性正则——与 08-03 的 PaletteID、08-04 的 Reproducing LightMem 共同构成「LLM 在 IR 中不稳定」的证据链。
4. **安全研究多线并进**：ACL Outstanding「用真话撒谎」证明更强模型更易被真实碎片操纵；Infini-gram mini（08-04）量化了基准污染；Alignment 双刃剑（Censor's Toolkit，08-04）与 Global Human Opinion（08-01）标志对齐研究的社会维度。
5. **序列模型效率与表达力同时上行**：Mamba-3（复值状态 + MIMO，状态减半）+ Swimba（MoE-SSM）说明线性注意力替代者仍在快速演化；ICLR e3 与 NeurIPS HRPO 说明「推理何时该 latent / 如何探索」是 2026 推理研究的核心张力。
6. **视频生成扩散成为通用视觉学习器**：GenCeption（DeepMind）把生成目标用于表征学习；Helios 14B / Paris 2.0 继续拉高开源与去中心化视频生成的能力-成本曲线；CVPR D4RT（08-04）则把 4D 重建压成单前馈模型。

---

*本报告由多路网络检索编译；标注 (tentative) 的条目存在待核实字段（作者/机构/具体数值），建议核对 arXiv 原文。日期、获奖等事实性信息以官方页面为准。*
