---
title: "Conference & arXiv Daily Digest: 2025-2026 Top ML/AI Venues"
type: synthesis
created: 2026-09-07
updated: 2026-09-07
sources: []
tags: [conference-digest, icml-2026, aaai-2026, neurips-2025, iclr-2026, cvpr-2026, kdd-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2025, recsys-2025, recommendation, llm, agent, ctr, advertising, generative-model, sequential-modeling, benchmark]
---

# Conference & arXiv Daily Digest: 2025-2026 Top ML/AI Venues

> Compiled 2026-09-07. Covers ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, CVPR 2026, KDD 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025, plus recent arXiv. Focus: recommendation systems, advertising/CTR, agent systems, generative models, sequential modeling, benchmarks — with emphasis on Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, NVIDIA, Anthropic, Apple, Amazon.
>
> 中文：本期为 2025-2026 各大顶会 + 最新 arXiv 综合摘要。已去重当日兄弟 digest（arxiv-daily / arxiv-ai-search）收录的 arXiv ID，个别交叉关注以引用形式标注。机构归属基于论文/会议元数据与作者侧信息，个别为 opencode-compiled 推断，需以原文核实。

---

## 1. 概览 / Overview

- **ICML 2026**（首尔, 7/6-11）: 6,634 篇录用，为历年最大。
- **CVPR 2026**（丹佛, 6/3-7）: 16,092 投稿 / 4,090 录用（25.42%），较 2025 年 +42.5%。两大趋势：多模态 LLM（4.9%→10.6%）与视频生成/World Model（3.8%→8.8%）成主导；检测/分割/深度等传统 CV 占比下滑。
- **KDD 2026**（济州岛, 8 月）: Feb+Jul 双周期合计 ~1,400+ 篇，Feb 周期 1,215 投 / 256 录（~21%）。BeST Paper 疑点覆盖 scalable ML、recommendation/retrieval、graph/temporal、agentic data workflows。
- **ACL 2026**（圣迭戈, 7 月）: Main 2,296 篇 + Findings 2,163 篇，ARR 周期下 Main 录用率 18.9%。LLM Safety(115) / Evaluation(97) / Agent(82) / Reasoning(82) 论文笔记数量领先。
- **AAAI 2026**（新加坡, 1/20-27）: 近 29,000 投稿，~23,000 进入评审，为 AAAI-25 近两倍；中国 ~20,000 投稿。CV / ML / NLP 为三大方向。
- **NeurIPS 2025**（圣迭戈, 12 月）: 5,872 篇录用，其中 5,771 Main。
- **ICLR 2026**: 224 Oral / 5,355 录用，Oral 覆盖 LLM reasoning、Mamba-3、Mixture-of-Experts、memory agents 等。
- **EMNLP 2025**（苏州, 11 月）: 8,172 投 / Main 1,811（22.16%）+ Findings 1,417。Best Paper: Infini-gram mini。
- **SIGIR 2026**（墨尔本, 7/20-24）: Full 234 + Industry 131 + Resource 61 + Short 151 等。
- **RecSys 2025**（布拉格, 9/22-26）: Main track 录用率 19%。
- **WWW 2026**（线上, 6/29-7/3）: Research Track 3,370 投 / 676 录（20.06%）。Recommendation 110 篇（16.3%）为最大方向。

---

## 2. Recommendation / LLM-based Recommendation

### 2.1 GenRec: A Preference-Oriented Generative Framework for Large-Scale Recommendation
- **Authors**: 京东（JD App）团队（SIGIR 2026 工业部署）
- **Affiliation**: JD.com（京东）
- **Venue**: SIGIR 2026
- **arXiv / PDF**: https://arxiv.org/pdf/2604.14878
- **Abstract & Innovations**:
  - 生成式检索（Generative Retrieval, GR）以 next-token prediction 做推荐，但工业规模化面临三个挑战：(1) 分页请求机制下同一输入出现多有效输出（one-to-many 歧义）；(2) 长用户行为序列 + 多 token Semantic ID 编码成本高；(3) 生成策略与细粒度用户偏好对齐困难。
  - 提出 **Page-wise NTP** 监督整个交互页而非单个 item，提供更密梯度并解决点式训练的一对多歧义。
  - **Asymmetric Linear Token Merger**：prefill 端压缩多 token Semantic ID（输入长度 ~2× 缩减），decode 端保留全分辨率。
  - **GRPO-SR**：Group Relative Policy Optimization + NLL 正则 + Hybrid Rewards（dense reward model + relevance gate 抑制 reward hacking）。
- **Experimental Results**: 京东 App 首页 feed 月级在线 A/B：base SFT 模型点击 +8.5%、成交 +7.3%；GRPO-SR 对齐后点击 +9.5%、成交 +8.7%；长尾 item 曝光 +10%、点击 +16%、成交 +13%。已在生产全量部署。
- **Comparison**: 相对 TIGER/OneRec/OneTrans 等 GR 方法，GenRec 首次针对工业分页机制（page-wise）、输入压缩（token merger）与偏好对齐（GRPO-SR）三者统一。

### 2.2 GFlowGR: Fine-tuning Generative Recommendation Frameworks with Generative Flow Networks
- **Authors**: Yejing Wang 等（Applied Machine Learning Lab）+ 淘宝
- **Affiliation**: City University of Hong Kong / Taobao（阿里巴巴）
- **Venue**: SIGIR 2026（已部署）
- **Abstract & Innovations**: 生成式推荐（GR）把推荐看作序列生成，但候选集合内 item 效用不均，reward 微调常缺乏 token 级监督。提出：(1) trajectory sampler 从候选集构造训练轨迹实现 set-wise 学习；(2) behavior-aware 模型量化 item 效用；(3) GFlowNet 目标提供 token 级监督。三数据集 + 两个 GR backbone 上显著优于强基线。
- **Experimental Results**: 线上 ~0.4pp 提升，2025 年中规模部署（数十亿级收益）。
- **Comparison**: 相对 reward-based fine-tuning（仅整体序列奖励），GFlowNet 提供 set-level + token-level 的双层监督。

### 2.3 ItemRAG: Item-Based Retrieval-Augmented Generation for LLM-Based Recommendation
- **Authors**: Kawoon Suh 等
- **Affiliation**: 学界（KAIST 等）
- **Venue**: SIGIR 2026
- **arXiv**: https://arxiv.org/html/2511.15141v2
- **Abstract & Innovations**: 主流 LLM-RS RAG 做法是检索"相似 user"的历史，但常含噪声弱相关信息。ItemRAG 转向 item 级细粒度检索：对目标用户历史/候选中每个 item 检索相关 item 增强其描述；检索策略结合 co-purchase 关系（按 co-purchase 频率采样）+ 语义相似度。
- **Experimental Results**: 18/20 设置优于基线；对零样本 LLM recommender 最高 +42% Hit-Ratio@1（Beauty & Personal Care）；对比 user-based RAG（CoRAL）最高 +11% HR@1（Toys & Games）；冷启动 item 同样有效。
- **Comparison**: 相对 user-level RAG，item-level 增强减少不相关 user 引入的噪声，并为每个候选提供显式推荐证据，尤其惠及冷启动 item。

### 2.4 ProMax: Exploring the Potential of LLM-derived Profiles with Distribution Shaping
- **Authors**: Yi Zhang, Yiwen Zhang, Kai Zheng, Tong Chen, Hongzhi Yin
- **Affiliation**: University of Queensland（昆士兰大学）等
- **Venue**: SIGIR 2026
- **arXiv**: https://arxiv.org/html/2604.26231
- **Abstract & Innovations**: 从 retrieval 视角重访 LLM 生成 profile：用 dense retrieval 揭示 user/item profile 间的协作信号，并提出双分布重塑：（1）监督式分布重塑（profile 分布作指导信号，不确定性加权推动模型探索未观察 item）；（2）自监督式分布重塑（基于 profile 检索增强历史交互，双向一致性最大化）。profile 仅作 indicator、不参与训练。
- **Experimental Results**: LightGCN+ProMax 相对最佳 baseline ProEx 在 Amazon-Book / Yelp / Steam 上 NDCG@10 分别 +8.44% / +4.75% / +3.31%；Recall@20 +13.3% / +15.64% / +12.28%。
- **Comparison**: 相对简单拼接/非线性融合 LLM profile 的方法，ProMax 是 model-agnostic、仅加两个训练目标、不改动架构。

### 2.5 L2Rec: Towards Dual-View Understanding of LLMs for Personalized Recommendation
- **Authors**: 网易云音乐团队
- **Affiliation**: Netease Cloud Music（网易云音乐）
- **Venue**: SIGIR 2026
- **arXiv**: https://arxiv.org/html/2605.26717v1
- **Abstract & Innovations**: 现有 LLM-RS 在输入级（inject behavioral embeddings）或输出级（对比对齐分离 encoder）融合行为与语义，存在分布 gap 或缺乏端到端任务监督。L2Rec 在**参数级**统一：同一套冻结 Transformer 参数 + **Dual-view Personalized Mixture-of-Experts (DPMoE)** —— 共享 LoRA 专家捕捉跨 view 共性 + view 专用专家（SPMoE 语义 / BPMoE 行为）+ Adaptive Cross-view Fusion (ACF)。仅更新 ~32M 参数（backbone 的 ~5%）。
- **Experimental Results**: 4 数据集（3 公开 + 1 工业）超 SOTA；~1.5M DAU 主页 feed 线上 A/B：CTR +9.24%、reply rate +3.15%。
- **Comparison**: 相对输入/输出级融合，参数级适应（view-specific personalized LoRA perturbation）避免表征空间分布错位。

### 2.6 MVIGER: Multi-View Variational Integration of Complementary Knowledge for Generative Recommender
- **Venue**: SIGIR 2026
- **arXiv**: https://arxiv.org/html/2408.08686v4
- **Abstract & Innovations**: 多视角变分集成互补知识于生成式推荐，缓解生成式推荐中的知识互补与不确定性问题。

### 2.7 SIGIR 2026 其他推荐亮点（简记）
- **BaBE / Beyond Static Best-of-N**: Bayesian List-wise Alignment for LLM-based Recommendation（贝叶斯成列对齐）。
- **Factorized Latent Reasoning for LLM-based Recommendation**：因式化潜在推理。
- **TimeMM: Time-as-Operator Spectral Filtering for Dynamic Multimodal Recommendation**：以"时间即算子"做动态多模态推荐的谱滤波。
- **Fourier Kolmogorov-Arnold Network + Hypergraph Contrastive Learning**：把 Fourier KAN 与超图对比学习结合用于推荐。
- **SilverTorch（Meta/内部系统）**: 统一 model-based 系统在 GPU 上大规模推荐。
- **FairSpec**: 面向公平 LLM 推荐的专家专精化。
- **Unifying Search and Recommendation in LLMs via Gradient Multi-Subspace Tuning**。
- **Generative Recommendation / CTR 会话**有专门 workshop 与主题（Diffusion-/Flow-based Recommendation、CTR Prediction、Item Tokenization）。

### 2.8 RecSys 2025（精选）
- **RESA / GRACE: Generative Recommendation via Journey-Aware Sparse Attention on Chain-of-Thought Tokenization**（Walmart Global Tech）: 以 CoT tokenization 的 journey-aware 稀疏注意力做生成式推荐。
- **GenSAR: Unifying Balanced Search and Recommendation with Generative Retrieval**（人大 + Kuaishou）: 生成式检索统一搜索与推荐。
- **Lasso: LLM-based User Simulator for Cross-Domain Recommendation**（Kuaishou）: LLM 用户模拟器跨域推荐。
- **Enhancing Sequential Recommender with LLMs for Joint Video and Comment Recommendation**（人大 + Kuaishou）。
- **Beyond Immediate Click: Engagement-Aware and MoE-Enhanced Transformers**（Amazon Prime Video）: 面向电影推荐的参与度感知 MoE Transformer。
- **eSASRec**: 模块化增强 Transformer-based 推荐。
- **LEAF: Lightweight, Efficient, Adaptive and Flexible Embedding**（USC）: 轻量自适应 embedding 压缩。
- **MoRE: A Mixture of Reflectors Framework** for LLM-based sequential recommendation。

---

## 3. Advertising / CTR / Auction

### 3.1 UniROM: Unifying Online Advertising Ranking as One Model
- **Authors**: Junyan Qiu 等
- **Affiliation**: Meituan（美团）
- **Venue**: CIKM 2025
- **Abstract & Innovations**: 把在线广告排序（如多任务、多阶段、多场景）统一为单一模型，减少多模型级联的偏差与维护成本。

### 3.2 LEADRE: Multi-Faceted Knowledge Enhanced LLM Empowered Display Advertisement Recommender
- **Authors**: Fengxin Li 等
- **Affiliation**: Tencent / VLDB（WeChat 视频号与朋友圈）
- **Venue**: VLDB 2025（显示广告 LLM 增强）
- **DOI**: https://doi.org/10.14778/3750601.3750602
- **Abstract & Innovations**: 传统显示广告多阶段 + ID-based retrieval 未充分利用广告标题/描述等文本内容。LEADRE 三大模块：Intent-Aware Prompt Engineering（多面知识 + intent-aware <Prompt, Response> 对微调 LLM 生成个性化广告）；Advertising-Specific Knowledge Alignment（辅助微调任务 + DPO 对齐广告语义与业务目标）；Latency-Aware Model Deployment（混合在线/离线服务框架）。
- **Experimental Results**: 微信视频号/朋友圈 A/B：GMV +1.57% / +1.17%；每日数十亿次请求，已全量部署。
- **Comparison**: 相对 ID-based retrieval 的显示广告，LEADRE 引入 LLM 世界知识 + DPO 业务对齐，产出个性化、可解释的广告。

### 3.3 MARS: Modality-Aligned Retrieval for Sequence Augmented CTR Prediction
- **Authors**: 快手 + 中科院/学界
- **Affiliation**: Kuaishou（快手）, KDD 2025
- **Venue**: KDD 2025（CTR 数据增强）
- **arXiv**: https://arxiv.org/html/2509.01184
- **Abstract & Innovations**: 针对交互稀疏（低活跃用户）的 CTR，提出 Stein kernel 对齐文本+图像特征到统一语义空间，构造多模态用户 embedding；据此 retrieve 语义相似高活跃用户行为序列进行增强（过滤 item-user 相似度保证质量）。已部署服务数亿用户。
- **Comparison**: 相对启发式增强（CL4SRec/CoSeRec/BASRec）与仅协作信号的方法，MARS 挖掘 item 多模态特征，离线在线均一致提升 6 项核心业务指标。

### 3.4 CRAFT: Feature Transport View for Unified Recommendation（KDDCUP'26）
- **Venue**: KDDCUP 2026 Workshop
- **Abstract & Innovations**: 把 "feature interaction→feature transport" 作为统一推荐视角，Contextual Residual Adaptive Feature Transport block 使上下文成为表征演化的主动控制器。TAAC2026 测试 AUC 0.838090（略超榜一 0.83798）。
- **Comparison**: 相对固定上下文交叉的 interaction 范式，transport 视角让上下文动态调控特征演化。

### 3.5 Advertising / Auction（ICML 2026 相关，承 07-27 稿）
- **Autobidding Auctions with LLM-Powered Creatives**（ICML 2026）: 平台为 Stackelberg leader、广告主为预算约束 follower，显式考虑 LLM 推理成本，核心变量从 pCTR/pCVR 转向"是否调用 LLM 生成创意"。
- **Model Monotonicity in Autobidding Auctions**（Uber, ICML 2026）: 证明更好的 pCTR/pCVR 预测不一定带来更好的拍卖结果（revenue/welfare），推翻"模型越好→结果越好"的行业假设。
- **Risk-Averse and Optimistic Advertiser Incentive Compatibility**（Google, https://arxiv.org/abs/2508.16823）: 放宽传统 AIC 的最坏情形比较，引入风险规避与乐观视角。

### 3.6 AsarRec / CTR 序列建模（CIKM 2025）
- **C-Former: Transformers Are Good Clusterers for Lifelong User Behavior Sequence Modeling**（对手 q 语义化聚类，端到端对接 CTR 任务，终身行为序列）— CIKM 2025。
- **Transformers / Causal Attention** 在离线/广告排序中的长序列建模（TAAC-25、UltraHSTU、LONGER 等 OpenAI 风格 HSTU 后续）——详见 UniRank benchmark（§6.3）。

---

## 4. Agent Systems / Multi-Agent / RL for Agents

> 本类为当日 arXiv 重点。与 arxiv-daily/arxiv-ai-search 已收录 ID 去重；部分交叉关注以链接标注。

### 4.1 ARISE-RL: Agentic Rubric-Grounded Iterative Self-Evolution with Reinforcement Learning
- **Authors**: Alibaba-NLP（fanrui 等）
- **Affiliation**: Alibaba（阿里巴巴）NLP
- **Venue**: arXiv 2026-09（https://arxiv.org/html/2609.01058）
- **Abstract & Innovations**:
  - 开放长程 agent 的 RL 受困于缺少可验证金答案与可扩展 rubric，且 open-ended 任务奖励稀疏/脆弱。
  - 提出 **Generator–Solver 共演化**闭环：Generator 在真实工具观测上构建 tool-grounded rubric（须先调用相关工具再写依赖工具输出的标准，防幻觉 rubric），Solver 在 rubric-based 细粒度奖励下 multi-step reasoning + tool use。
  - 难度定型奖励：多轮 Solver 尝试估计经验可解性，Generator 在成功率居中（intermediate-difficulty）时奖励最高 → 逼近能力边界。
  - **Reward-Gated Self-Evolution Distillation (RG-SED)**：仅在 memory 带来经验奖励提升时自我蒸馏，降低分布失配、避免盲目模仿噪声指导。
  - 提出 **ECR-Bench**：专家标定 rubric benchmark（single-tool deep research + multi-tool travel planning）。
- **Experimental Results**: Qwen3.5-9B backbone 上平均 SOTA，超越所有 closed-source（Gemini3-Pro/GPT-5/Claude-4.5/4.6）与最强开源非自演化基线，尤其 interactive multi-tool 基准增益最大；对比当代自演化基线 Dr. Zero / Absolute Zero 一致领先。
- **Comparison**: 相对 EvolveR / ASL / RAGEN 等自演化框架（多限于单工具/推理中心），ARISE-RL 首个面向 open-ended agentic 的闭环（任务生成 + rubric 构建 + 策略优化统一）。

### 4.2 TIGPO: Temporal Instance-Graph Policy Optimization for Long-Horizon LLM Agents
- **Authors**: （同日 arxiv-daily 已收录，见 wiki/synthesis/2026-09-07/arxiv-daily.md §LLMs）
- **Affiliation**: 学界
- **Venue**: arXiv 2609.03383（2026-09）
- **Abstract & Innovations (摘要)**: 扩展基于图的信用分配跨 policy update：TIGPO 为每个任务维护**持久过渡图**，不同 policy 版本发现的合法过渡共同决定当前 rollout 的 credit；Exporation/Revisit 槽位结构性重连历史经验，Enlarged reference 稳定相对优势估计；历史仅作 detached 统计参照、不重放于策略 loss。ALFWorld/WebShop 上优于 group-based 与 graph-based 方法。
- **详见**: arxiv-daily 2026-09-07 §LLMs。

### 4.3 VICT: Verifier-Instrumented Credit Tracing for Long-Horizon LLM Agent RL
- **Authors**: 学界
- **Venue**: EMNLP 2026（https://arxiv.org/abs/2608.28128）
- **Abstract & Innovations**: 长程 agent RL 的细粒度信用分配常把稀疏 terminal reward 均匀广播到每个 action。VICT 洞察：许多可验证任务已把相关检查编码进 terminal verifier 内部。VICT 把 verifier 转为训练期接口，暴露 executable/evidence-backed 原子，并沿 dependency-valid proof edges 回溯到 actions，仅沿边重分配 group-relative advantage；保留原始 terminal reward、证据不完整时 abstain、只改训练期 advantage tensor（无需 critic/process label/branch rollout/推理期 verifier）。
- **Experimental Results**: ALFWorld / WebShop 上显著优于 outcome-only，接近近期细粒度 credit 方法；消融排除 dense atom reward、final-commit credit、temporal proximity、sparsity 作为充分解释。
- **Comparison**: 相对 rollout 侧构造辅助信号做 credit 推断的方法，VICT 把 credit 分配从 rollout 侧推断转向 verifier 侧 tracing。

### 4.4 TASPO: Reconciling Process Supervision with Outcome-Based Credit in Agentic Policy Optimization
- **Authors**: 学界
- **Venue**: arXiv 2608.31077（2026-08）
- **Abstract & Innovations**: 指出 "fine-grained supervision ≠ fine-grained credit"：privileged information (PI) 引起的似然变化描述附加信息如何改变策略偏好，但不直接决定可执行动作如何继承已验证任务结果（supervision-credit gap）。TASPO 把特权监督转换为 outcome-grounded action credit：从已验证成功经验构造 decision-applicable PI、在可执行动作级聚合 PI-induced likelihood 位移、把相对支持度转为正有界均值保持权重。
- **Experimental Results**: 3 个 agentic benchmark 上相对 GRPO +10.6%，对未见任务泛化更好；降低 supervision mismatch 并稳定策略优化。
- **Comparison**: 相对 GRPO（均匀 credit）与 on-policy self-distillation（粗粒度 credit），TASPO 提供 outcome-bounded 的 action 级重分配。

### 4.5 MASkills: Continual Skills Optimization for Multi-Agent LLM Systems
- **Authors**: 学界
- **Venue**: EMNLP 2026 Findings（https://arxiv.org/abs/2609.02094）
- **Abstract & Innovations**: 现有 self-reflection 构建经验 memory，但 memory 难调用/精炼/扩展。MASkills 以 agent skills 为可行动单元（指定何时行动/如何行动/用什么工具），提出 skill-conditioned credit assignment + hierarchical credit aggregation + momentum-smoothed optimization，使 skill library 通过 refinement/induction/consolidation/pruning 演化。
- **Experimental Results**: HotpotQA / LoCoMo / GAIA 上验证多 agentic 任务有效性。
- **Comparison**: 相对 memory-based reflection，skill-based 持续优化更具可组合、可精炼、可扩展性。

### 4.6 Bilevel Coordinated Reflection（Game-Theoretic, arXiv 2609.02750）
- **Abstract & Innovations (摘要)**: 把 orchestrator-worker 交互建模为 bilevel coordination game（bounded coupling 下 workers 的 local-update game 为 approximate potential game），分析 reflection 为语义 memory 状态上的随机游走；证明信息论不可能结果（仅观测 transcript 的 gate 无法统一改善 text-indistinguishable 环境）。提出 **Stochastic Reflective Memory Ascent (SRMA)**：仅在 grounded 评估风险严格下降时接受候选 memory，几何/多项式收敛；500 SWE-bench 实例上完整 Kimi-based 系统 72.2% vs mini-SWE-agent 70.8%。

### 4.7 Speculative Macro Commit (SMC) for Faster Tool-Using Agents
- **Authors**: 学界
- **Venue**: MLSP 2026（https://arxiv.org/abs/2609.03236）
- **Abstract & Innovations**: 两层 agent：大型 authoritative actor 产生官方轨迹 + 快速 speculative drafter 在隔离环境快照上持续预测并执行未来动作链；从训练轨迹挖掘 recurring multi-action skeleton 存 macro library，运行时匹配。Qwen3.5-27B INT4 (actor) + Qwen3.5-4B (drafter)：Telecom 集延迟 -10.23%（相对 SA）、-18.59%（相对顺序）；AppWorld wall time -7.7%（vs SA）、-44.9%（vs 顺序）。

### 4.8 Environment Evolution for Terminal Agents
- **Authors**: 学界
- **Venue**: arXiv 2609.04128（2026-09）
- **Abstract & Innovations**: 现有 co-evolution 方法依赖 on-policy rollouts 限制泛化。提出 **environment evolution**：off-policy 增量提高环境难度并按代调度，从 multi-turn objective 推导三个难度方向，经 loop-engineered multi-agent harness 演进环境。Qwen3.6-27B / Qwen3.6-35B-A3B 上 Terminal-Bench 2.1 提升 +14.4 / +18.0 pp；Hy4 preview、Claude Opus 5、GPT-5.6 Sol 的量化实验确认难度一致性增强。

### 4.9 AgentPRM / AEPO（WWW 2026）
- **AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress**（WWW 2026）: 重定义 agent PRM——按与目标距离与进展而非孤立步骤评分，捕捉顺序决策的相互依赖与对最终目标的贡献。
- **AEPO: Agentic Entropy-Balanced Policy Optimization**（WWW 2026, Kuaishou 等）: 应对 agentic RL 的熵问题，在 rollout 与 policy 两阶段平衡熵。

### 4.10 ICLR 2026 Oral 相关（agents）
- **MedAgentGym: A Scalable Agentic Training Environment for Code-Centric Reasoning**（ICLR 2026 Oral）。
- **MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent**（ICLR 2026 Oral）: 多轮交互 RL 内存 agent 重塑长上下文。
- **In-The-Flow Agentic System Optimization for Effective Planning and Tool Use**（ICLR 2026 Oral）。
- **Verifying Chain-of-Thought Reasoning via its Computational Graph**（ICLR 2026 Oral）: 经计算图验证 CoT 推理。

---

## 5. Generative Models / Diffusion / Video & World Models

### 5.1 CVPR 2026 生成式 / 视频生成亮点
- **ARCache: Mitigating Error Accumulation for Caching-based Acceleration in Autoregressive Video Diffusion Models**（CVPR 2026）: 首个 training-free caching 加速框架，专为自回归视频扩散设计，缓解误差积累与视频质量渐进退化。
- **SURF: Signature-retained Fast Video Generation**（CVPR 2026）: 保签名快速视频生成。
- **GenieDrive: Towards Physics-Aware Driving World Model with 4D Occupancy Guided Video Generation**（Google DeepMind 生态相关）: 4D occupancy 引导的驾驶 World Model。
- **Qwen-Image-Layered: Towards Inherent Editability via Layer Decomposition**（阿里 Qwen 团队, CVPR 2026）: 单 RGB 图分解为多个语义解耦 RGBA 层，天然可编辑。
- **Omni-Attribute: Open-vocabulary Image Attribute Encoder**（Snap Research 等）: 开放词表属性编码器用于视觉解耦与合成。
- **Improved Mean Flows**（Kaiming He 团队, CVPR 2026）: 改进 step 扩展的 Mean Flow，与 fastforward generative 理论衔接。
- **MacTok: Robust Continuous Tokenization for Image Generation**（CVPR 2026 Highlight）: 鲁棒连续 tokenization 提升图像生成。
- **A Frame is Worth One Token: Efficient Generative World Modeling with Delta Tokens**（ByteDance 相关, CVPR 2026 Highlight）: 以 delta tokens 做高效生成式 World Modeling。

### 5.2 CVPR 2026 最佳论文 / 荣誉（视觉方向）
- **Best Paper — D4RT: Efficiently Reconstructing Dynamic Scenes One D4RT at a Time**（Google DeepMind + UCL + Oxford, Chuhan Zhang 等）: 统一 transformer 架构估计深度、时空对应与相机参数，允许独立高效 probe 任意时空点的 3D 位置；轻量可扩展，训练/推理高效。
- **Best Student Paper — Native and Compact Structured Latents for 3D Generation / O-Voxel**（清华 + Microsoft Research + USTC + Microsoft AI）: 从原生 3D 数据学习结构化压缩潜在表征（O-Voxel 表示），几何与质量远超现有模型。
- **Best Paper Honorable Mention — NitroGen**（NVIDIA + Stanford 等）: 视觉-动作 foundation model 通用游戏 agent，40,000 小时 / 1,000+ 游戏训练。
- **Best Paper Honorable Mention — SAM 3D: 3Dfy Anything in Images**（Meta Superintelligence Labs）: 单图生成几何+纹理+布局，真人偏好 win rate ≥5:1。
- **Best Student Paper Honorable Mention — ChordEdit: One-Step Low-Energy Transport for Image Editing**（广东工业大学等）: training-free、inversion-free 单步图像编辑。

### 5.3 公平评测单步生成（arXiv 2603.14186, Harvard AI & Robotics Lab）
- **Fair Benchmarking of Emerging One-Step Generative Models vs Multistep Diffusion/Flow**:
  - 在受控 protocol（匹配 CFG=7、1 vs 25 步、ImageNet/ImageNetV2/reLAIONet）下评测 MeanFlow / Improved MeanFlow / SoFlow（one-step flow）vs SiT / RAE / Scale-RAE / Stable Diffusion 3.5 / FLUX.1。
  - 发现：**仅优化 FID 会牺牲 diversity、text-image alignment 与 human preference**；one-step 模型在 25 步下显著改善但仍存在局部失真（尤其面部）。提出 **MinMax Harmonic Mean (MMHM)** 复合指标稳定跨 guidance/step 超参选择。
  - **详见**: arxiv-ai-search 2026-09-07（交叉引用）。

### 5.4 Diffusion Language Models（EMNLP 2026）
- **PILL: Probing-based InfiLling with preset-Length-free decoding**（arXiv 2609.02108, EMNLP 2026 Main）: 为 DLM 提供无预设长度的 infilling，跨 5 个 DLM / 8 benchmarks 相对最优 baseline code pass rate +4.8、text BLEU-2 +6.0，快 1.82×。
- **CRS: Committed Reveal Sampling**（arXiv 2609.01043）: uniform discrete diffusion 的 training-free sampler，把选中 argmax token 作为持久上下文；64 NFE 下比固定 top-p 基线的 GenPPL 更低、更优 GenPPL-entropy 权衡。

### 5.5 Liquid Gated Attention (LGA) — Continuous-Time Sequence Modeling（arXiv 2608.30695）
- **Abstract & Innovations**: 求解 free、可并行的连续时间算子，用观测时间间隔参数化 input-driven gating，隐藏状态演化建模为 fast-weight associative memory；非因果用矩阵结合性、因果用 prefix scan，达到序列长度的线性时间复杂度；序列级归一化 bound 累积时间衰减。六任务/十六数据集（最长 17,984 步）上长程依赖、细粒度状态追踪、稀疏噪声轨迹重建均达 SOTA 级，线性缩放。
- **Relevance**: 面向推荐/用户行为序列的连续时间建模与 "sequential modeling" 主题高度相关。

---

## 6. Benchmarks / Datasets / Systems

### 6.1 UniRank: Open Benchmark for Ranking Models (Sequential Modeling + Feature Interaction)
- **Authors**: Honghao Li（安徽大学）、Xianquan Wang（USTC）、Zibin Zhang / Kangyi Lin（Tencent）等
- **Affiliation**: Anhui University / USTC / Tencent（腾讯）
- **Venue**: arXiv 2607.19987（2026-07）
- **Abstract & Innovations**: 首个面向"统一序列建模 + 特征交互"排序架构的开源 benchmark。chronological pointwise autoregressive 监督、跨反馈任务标准化评估、提供 PyTorch/分布式/算子/混合精度/attention 优化工具包。评测 15 个统一排序模型 × 5 个大规模公开数据集（短视频/广告/电商），最大 7 亿实例、最长行为序列 >10^5。
- **Findings**: stacked（HeMix/UniMixer）与 layer-wise（EST/TokenFormer）两类都不绝对主导；模型跨平台迁移依赖生产 inductive bias（Taobao 系在 Taobao/MerRec 强，广告系 TokenFormer 在 TAAC-25 强，短视频系 UltraHSTU/UniMixer/LONGER 在 QK-Video/KuaiRand 强）。
- **Relevance**: 直接服务 CTR/广告/推荐排序的 academic-industrial 方法对标。

### 6.2 KDD 2026 数据集/基准
- **VideoRAG: Retrieval-Augmented Generation with Extreme Long-Context Videos**（Xubin Ren 等, KDD 2026）: 针对极长上下文视频的 RAG 框架。
- **MAC: A Conversion Prediction Benchmark with Multiple Attribution Mechanisms**（广告转化归因基准）。
- **REALM-Bench**: 真实世界动态规划与调度任务的多 agent 评估基准（Longling Geng 等）。
- **CoRank**: 面向科学检索的 LLM 文档级协同 re-ranking（结构感知表示）。
- **Generative Recommendation with Semantic IDs: A Practitioner's Handbook**（Clark Mingxuan Ju 等, Snap, CIKM 2025 Best Resource Paper）: SID 生成式推荐实践手册。
- **ARCTraj**: 人类抽象问题求解推理轨迹数据集基准。
- **ReplicatorBench**: 社学与行为科学复制性的 LLM agent 基准。

### 6.3 EMNLP 2025 基准/方法亮点
- **Best Paper — Infini-gram mini: Exact n-gram Search at the Internet Scale with FM-Index**（UW/AllenAI, Hao Xu 等）: FM-Index 使 PB 级文本语料可搜索。
- **S1: Simple Test-time Scaling**（Stanford, Muennighoff 等）: 追求最简 test-time scaling。
- **IMO-Bench**（Google DeepMind）: IMO 级推理基准套件。
- **Sketch-of-Thought (SoT)**（Hwang 等）: 认知启发的草图式提示框架，减少 token 同时保持推理精度。
- **Temporal Scaling Law for LLMs**: 训练时长演化下的 test loss 标度律。
- **CodeArena**（阿里 Qwen 团队）: 40 类 / 44 语言的人类偏好代码评测。
- **MathTutorBench**（Jakub Macina 等）: 教学基准，发现 subject expertise 与 pedagogy 呈权衡。
- **Struct-Bench**（NeurIPS 2025, D&B track）: 差分隐私结构化文本生成基准。

### 6.4 NeurIPS 2025 数据/基准（Datasets & Benchmarks Track）
- **EngiBench**: datadriven engineering design 研究框架。
- **PHYBench**: LLM 物理感知与推理评估。
- **MLE-Dojo**: LLM agent 在 ML engineering 的交互环境。
- **CleverBirds**: 细粒度人类知识追踪多选基准。
- **CogPhys**: 多模态生理感测评估认知负载。

### 6.5 ICLR 2026 Oral 基准
- **EigenBench: A Comparative Behavioral Measure of Value Alignment**（ICLR 2026 Oral）: 行为学价值对齐度量。
- **AgentHPOBench**（arXiv 2607.29626）: 30 个人类可执行 ML 任务，评估 LLM agent 作为序列超参优化器的能力。

---

## 7. 跨会议趋势 / Cross-Cutting Observations

1. **生成式推荐（Generative Recommendation）成为主战场**：SIGIR 2026 全量 234 篇中生成式/LLM 推荐占比极大，京东 GenRec、淘宝 GFlowGR、华为/快手相关均含工业上线证据；SID/tokenization（CIKM 2025 手册）是关键基础设施。
2. **CTR/排序走向"统一序列建模 + 特征交互"**：OpenAI HSTU 思想扩散至工业（UltraHSTU/UniMixer/LONGER），UniRank benchmark 正面回应"统一架构是否绝对最优"——结论是**依赖平台 inductive bias**，非一刀切。
3. **Agent RL 从"奖励对齐"走向"信用分配"**：VICT、TASPO、TIGPO 三条并进路线均在解决长程 agent 的细粒度/时序信用分配；ARISE-RL 把 rubric 构建纳入共演化闭环，标志 open-ended agent 训练从"静态任务"转向"任务自生成"。
4. **CVPR 2026 的范式转移**：多模态 LLM 与视频生成/World Model 翻倍成主导，传统 CV（检测/分割/跟踪）占比大幅收缩；生成式类主题合计 ~14%→~22%。
5. **评测可靠性成为显性主题**：MMHM（单步生成复合指标）、UniRank（统一排序协议）、Clean Engineering Unstable Measurement（同日 arxiv-daily 收录）共同指向"单一指标/单一 seed/无控制 protocol 会误导结论"。
6. **大厂落地证据密度上升**：京东 GenRec（点击+9.5%）、淘宝 GFlowGR（0.4pp）、网易云 L2Rec（CTR+9.24%）、微信 LEADRE（GMV+1.6%）、快手 MARS（6 指标提升）——LLM/生成式推荐不再是学术演示，已进入核心流量生产。

---

## 8. Sources & Method Notes

- 数据来源：各大会议官方录用清单、OpenReview、ACL Anthology、Paper Digest（AAAI/KDD/CVPR/WWW/EMNLP/CIKM）、实验室/公司博客、arXiv API。
- 方法：按 venue 检索 + 主题过滤 + 与当日兄弟 digest（arxiv-daily / arxiv-ai-search 2026-09-07）去重；ID 级去重采用 grep 验证。
- 机构归属：部分基于 Dec2025 前的已知作者隶属推断（opencode-compiled），需以论文原文核实。
- 语言：本页以中文为主体正文（符合来源以中/英混合为主），YAML/表头/协议标识保持英文。
