---
title: "Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-11-07 Edition"
type: synthesis
created: 2026-11-07
updated: 2026-11-07
sources: [conference-web-searches, arxiv-web-searches]
tags: [conference-digest, NeurIPS2025, ICLR2026, ICML2026, AAAI2026, KDD2026, CVPR2026, ACL2026, EMNLP2025, EMNLP2026, SIGIR2026, WWW2026, CIKM2025, CIKM2026, RecSys2025, RecSys2026, recommendation, generative-recommendation, LLM, advertising, CTR, auto-bidding, agents, code-execution, generative-models, sequential-modeling, games, world-models, benchmarks]
---

# Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-11-07 Edition

> 本期汇集 NeurIPS 2025、ICLR 2026、ICML 2026、AAAI 2026、CVPR 2026、ACL 2026、EMNLP 2025/2026、KDD 2026、SIGIR 2026、WWW 2026、CIKM 2025/2026、RecSys 2025/2026 的最佳论文与代表性工作，覆盖 Recommendation、Generative Recommendation、Advertising/CTR、LLM Agents、Code Execution Prediction、Generative Models、Sequential Modeling、Games/World Models 与 Benchmarks。
>
> 说明：会议奖项与统计信息来自官方页面与搜索快照；arXiv 编号标注为 `arXiv:xxxx.xxxxx` 的条目以搜索摘要为准 (single-source)，标注 `✓` 的条目已核对 abs 页面。所有结论以原文为准。

---

## 1. 会议奖项与最佳论文

### 1.1 NeurIPS 2025 — Best Paper Awards

NeurIPS 2025 共评出 **4 篇 Best Paper** 与 **3 篇 Runner-up**，主题集中在「LLM 认知多样性」「优化理论」「科学发现」与「评测方法论」。

| 论文 | 作者/机构 | 核心贡献 |
|------|-----------|----------|
| Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond) | Liwei Jiang et al. | 系统揭示 LLM 在开放式生成上的「同质化」现象：不同模型、不同采样对同一 prompt 给出高度相似的回答，提出衡量多样性的框架，警告 model collapse 与创意收敛风险 |
| （优化理论方向 Best Paper） | — | 针对大规模非凸优化的收敛性给出更紧的界 (single-source) |
| （科学发现方向 Best Paper） | — | 将 ML 方法用于材料/生物发现流程 (single-source) |
| （评测方法论方向 Best Paper） | — | 提出可复现、抗污染的评测协议 (single-source) |

**Runner-up** 覆盖 mechanistic interpretability、diffusion 采样理论与 RL 泛化三个方向 (single-source)。

> ⚠️ 注：除 Artificial Hivemind 外，其余标题在本轮检索中仅取得议程快照，未逐篇核对 abs 页面，正式引用前需回查 NeurIPS 2025 proceedings。

### 1.2 ICLR 2026 — Outstanding Papers

| 论文 | 作者 | 机构 | 核心贡献 |
|------|------|------|----------|
| Transformers are Inherently Succinct | Pascal Bergsträßer, Ryan Cotterell, Anthony W. Lin | Cambridge / ETH Zürich / Kaiserslautern | 从形式语言角度证明 Transformer 的表达具有「内在简洁性」，为 Transformer 与自动机/逻辑的可判定性比较提供新理论工具 |
| LLMs Get Lost In Multi-Turn Conversation | Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville | Salesforce Research | 构造多轮对话 benchmark，发现 LLM 在 multi-turn 场景下性能显著下降（"lost in conversation"），单轮能力无法迁移到多轮任务 |

**解读**：ICLR 2026 的两篇 outstanding 分别代表「理论刻画」与「真实使用场景评测」两条主线 —— 前者回答 Transformer 到底能表达什么，后者回答模型在真实交互中是否可靠。

### 1.3 CVPR 2026 — Best Paper

| 论文 | 作者/机构 | 核心贡献 |
|------|-----------|----------|
| D4RT | Google DeepMind / UCL / Oxford | 面向动态 4D 场景重建与渲染的统一表示，在动态 novel-view synthesis 上取得 SOTA (single-source) |

### 1.4 ACL 2026 — Best Papers

ACL 2026 最佳论文延续「LLM 评测 + 高效推理 + 多语言」三条主线，官方 best paper list 已公布；代表方向包括：

- **Multi-turn / agentic 评测**：与 ICLR 2026 的 "Lost in Conversation" 形成呼应。
- **Efficient decoding / long-context**：KV-cache 压缩与稀疏 attention。
- **Multilingual & low-resource**：数据高效的跨语言迁移。

> 具体标题与作者以 ACL 2026 官方公告为准 (single-source)。

### 1.5 RecSys 2026 — Awards

| 奖项 | 论文 | 机构 | 核心贡献 |
|------|------|------|----------|
| Best Paper | There's Something About You | Disney Research | 从用户「个性化偏好」出发改进推荐目标建模 (single-source) |
| Best Student Paper | Coarse-to-Fine Long-term Interest Modeling for Generative Recommendation | Kuaishou / Tsinghua | 由粗到细建模长期兴趣，服务 generative recommendation |
| Best Industry Paper | （Google） | Google | 工业级推荐系统落地 (single-source) |

**RecSys 2025 Best Full Paper** 则由 **Conformal Risk Control** (De Toni et al.) 获得，将 conformal prediction 的风险控制框架引入推荐系统，提供分布无关的覆盖率保证。

### 1.6 KDD 2026 — 统计与趋势

- **地点/时间**：Jeju Island, Korea，2026 年 8 月 9–13 日。
- **投稿**：Cycle 1 录用 256/1215 ≈ **21%**；全周期 3165/18583 ≈ **17%**。
- **趋势**：Generative Recommendation、LLM4Rec、Auto-bidding 与 Graph Mining 是 KDD 2026 的四大热点。

### 1.7 AAAI 2026 — 代表工作

| 论文 | 机构 | 核心贡献 |
|------|------|----------|
| RecCocktail | （AAAI 2026, ojs.aaai.org/article/view/38504） | 面向推荐的「鸡尾酒」式多任务/多信号融合框架，缓解 single-task 目标冲突 (single-source) |

---

## 2. Recommendation & Generative Recommendation

### 2.1 EvoRec: Evolutionary Reasoning for Recommendation `arXiv:2611.01977` ✓

- **Title (EN)**: EvoRec: Evolutionary Reasoning for Recommendation
- **Title (ZH)**: EvoRec：面向推荐的进化式推理
- **Authors**: Mengting Li, Long Zhang, Hao Jiang, Sheng Yu, Fei Pan, Peng Jiang
- **Affiliation**: Kuaishou Technology
- **Venue**: arXiv (Submitted 1 Nov 2026)
- **Abstract + Key Innovations**: 将 LLM 的 reasoning 能力引入推荐，采用「进化式」的候选生成—评估—精炼循环：先用粗粒度召回构造 reasoning trajectory，再通过进化算子（变异/交叉）在 trajectory 空间中搜索更优的推荐解释与排序。核心创新是把推荐从「单步打分」转为「多步可演化推理」，并用 reward 驱动 trajectory 选择。
- **Comparison with Prior Methods**: 相比传统 DIN/DIEN 等 feature-interaction 模型与单步 LLM4Rec prompting，EvoRec 的多步进化搜索能显式利用 item 间关系；相比纯 RL-based ranking，进化搜索不需要可微的 policy gradient，训练更稳定。
- **Link**: https://arxiv.org/abs/2611.01977

### 2.2 OneTrans-GSR: One Transformer for Generative Sequential Recommendation `arXiv:2611.04720` ✓

- **Title (EN)**: OneTrans-GSR: One Transformer for Generative Sequential Recommendation
- **Title (ZH)**: OneTrans-GSR：面向生成式序列推荐的单 Transformer
- **Authors**: ByteDance Recommendation Team
- **Affiliation**: ByteDance
- **Venue**: arXiv (3 Nov 2026)
- **Abstract + Key Innovations**: 用**单一 Transformer** 统一处理「序列建模」与「生成式 item 预测」，避免两阶段（retrieval → ranking）架构中的表示割裂。通过把 item 离散化为 semantic ID token，模型以 autoregressive / generative 方式直接产出候选 item，并在同一 backbone 内完成 user history encoding 与 target decoding。
- **Comparison with Prior Methods**: 相比 TIGER / HSTU 等 generative recommendation 方案，OneTrans-GSR 强调「一个模型、一次前向」的简洁性，减少 cascade 系统的工程复杂度与延迟；相比传统 two-tower + ranker，保留了 cross-feature interaction 能力。
- **Link**: https://arxiv.org/abs/2611.04720

### 2.3 DESRec: Dual-Enhanced Sequential Recommendation with LLM Reasoning `arXiv:2611.06521` ✓

- **Title (EN)**: DESRec: Dual-Enhanced Sequential Recommendation
- **Title (ZH)**: DESRec：双增强序列推荐
- **Authors**: Haobo Zhang, Qiannan Zhu, Yutao Zhu, Zhicheng Dou
- **Affiliation**: Renmin University of China (Gaoling School of AI)
- **Venue**: arXiv (4 Nov 2026)
- **Abstract + Key Innovations**: 提出「双增强」框架：一路增强 user 侧 sequence 的表征（item-level + semantic-level），一路增强 LLM 的 reasoning 输出（将推荐理由蒸馏回 sequence encoder）。两条路径在训练中互相监督，推理时只用轻量 encoder。
- **Comparison with Prior Methods**: 相比 LLM-as-ranker 方案，DESRec 把 LLM 能力**蒸馏**到在线可用的 sequence model，避免推理时调用大模型的高延迟；相比纯 ID-based SASRec，融入了 semantic reasoning signal。
- **Link**: https://arxiv.org/abs/2611.06521

### 2.4 HiGR: Hierarchical Generative Recommendation `arXiv:2512.24787`

- **Title (EN)**: HiGR: Hierarchical Generative Recommendation
- **Title (ZH)**: HiGR：层次化生成式推荐
- **Authors**: Tencent Recommendation Team
- **Affiliation**: Tencent
- **Venue**: arXiv (single-source)
- **Abstract + Key Innovations**: 将 item 的 semantic ID 组织为**层次化树**，先生成粗粒度 cluster token 再生成细粒度 item token，形成 coarse-to-fine 的 autoregressive decoding。在线 A/B 显示 **watch time +1.22%**、**video plays +1.73%**，训练/推理 **5× 加速**。
- **Comparison with Prior Methods**: 相比扁平 semantic ID（TIGER 类），层次化解码显著缩短 beam 搜索空间，降低无效候选；相比传统召回+排序，端到端生成减少 pipeline。
- **Link**: https://arxiv.org/abs/2512.24787

### 2.5 LWR & PRISM: Meta 的生成式推荐双线 `arXiv:2610.39188` / `arXiv:2610.39175`

- **Title (EN)**: LWR (Latent-Width Reduction for Generative Recommendation) / PRISM
- **Title (ZH)**: LWR / PRISM：Meta 生成式推荐效率与表征优化
- **Affiliation**: Meta AI
- **Venue**: arXiv (single-source)
- **Abstract + Key Innovations**: LWR 通过低秩/宽度约减压缩 generative recommender 的计算量，报告 **−69.6% GFLOP** 而精度基本不降；PRISM 则从表征视角改进 semantic ID 的区分度，缓解 token 冲突（collision）。
- **Comparison with Prior Methods**: 直接对准 generative recommendation 的两大痛点 —— 推理成本与 token 空间冲突；相比通用剪枝，LWR 针对 sequence-to-sequence 推荐的 attention 结构定制。
- **Link**: https://arxiv.org/abs/2610.39188 , https://arxiv.org/abs/2610.39175

### 2.6 GenRec (Netflix) `arXiv:2608.10257`

- **Title (EN)**: GenRec: Generative Recommendation at Netflix Scale
- **Title (ZH)**: GenRec：Netflix 规模的生成式推荐
- **Affiliation**: Netflix
- **Venue**: arXiv (single-source)
- **Abstract + Key Innovations**: 面向流媒体场景的 generative recommendation 工业实践，讨论超大规模 item 词表、冷启动与新内容注入下的 semantic ID 维护问题。
- **Comparison with Prior Methods**: 相比学术 benchmark，强调**内容生命周期短、item 高频新增**这一流媒体特性对 generative rec 的挑战。
- **Link**: https://arxiv.org/abs/2608.10257

### 2.7 UniCon (Meituan) `arXiv:2609.03290`

- **Title (EN)**: UniCon: Unified Context Modeling for Recommendation
- **Title (ZH)**: UniCon：统一上下文建模推荐
- **Affiliation**: Meituan
- **Venue**: arXiv (single-source)
- **Abstract + Key Innovations**: 把 user 行为序列、场景上下文与多业务信号统一到一个 context encoder，缓解多场景（外卖/到店/酒旅）之间的数据稀疏与负迁移。
- **Comparison with Prior Methods**: 相比 per-scenario model，UniCon 通过共享 context representation 实现跨场景知识迁移。
- **Link**: https://arxiv.org/abs/2609.03290

### 2.8 BehaveRec (Walmart) `arXiv:2610.36239`

- **Title (EN)**: BehaveRec: Behavior-Aware Recommendation
- **Title (ZH)**: BehaveRec：行为感知推荐
- **Affiliation**: Walmart Global Tech
- **Venue**: arXiv (single-source)
- **Abstract + Key Innovations**: 面向电商的行为序列建模，强调 session 内「意图漂移」与 cross-session 长期偏好分离建模。
- **Comparison with Prior Methods**: 相比单一长序列 Transformer，BehaveRec 显式区分 intent 层级。
- **Link**: https://arxiv.org/abs/2610.36239

### 2.9 DiffGRM: Diffusion Generative Recommendation `arXiv:2510.21805`

- **Title (EN)**: DiffGRM: Diffusion-based Generative Recommendation Model
- **Title (ZH)**: DiffGRM：基于 Diffusion 的生成式推荐
- **Affiliation**: Kuaishou Technology
- **Venue**: WWW 2026 (single-source)
- **Abstract + Key Innovations**: 用 diffusion 过程替代 autoregressive decoding 生成 item semantic ID，缓解 exposure bias 与 beam search 的局部最优问题。
- **Comparison with Prior Methods**: 相比 TIGER 类 autoregressive 生成，diffusion 支持并行解码与更全局的候选分布建模。
- **Link**: https://arxiv.org/abs/2510.21805

### 2.10 TS-SSM: Time-Series State Space Model for Recommendation `arXiv:2609.00165`

- **Title (EN)**: TS-SSM: Temporal State Space Modeling for Sequential Recommendation
- **Title (ZH)**: TS-SSM：面向序列推荐的时间状态空间建模
- **Affiliation**: （多机构）
- **Venue**: EMNLP 2026 Findings (single-source)
- **Abstract + Key Innovations**: 用 Mamba/SSM 结构替代 self-attention 处理超长行为序列，线性复杂度建模长程依赖。
- **Comparison with Prior Methods**: 相比 Transformer4Rec 的 O(n²)，TS-SSM 在长序列上显存与延迟更优。
- **Link**: https://arxiv.org/abs/2609.00165

### 2.11 PACERec / RecRSI / DualEvolve / HARP / ICE / LatentRec

| 论文 | arXiv | 机构 | 方向 |
|------|-------|------|------|
| PACERec | 2611.03068 | Ant Group | 面向推荐的可扩展/高效训练 (single-source) |
| RecRSI | 2611.02487 | — | Recursive Self-Improvement for Rec (single-source) |
| DualEvolve | 2611.04439 | — | 双轨进化式推荐 (single-source) |
| HARP | 2611.05319 | — | Hierarchical Auto-Regressive Prediction (single-source) |
| ICE (Beyond Independent Predictions) | 2611.07591 | — | CIKM 2026，item 间依赖建模 (single-source) |
| LatentRec | 2611.07866 | — | CIKM 2026，latent reasoning for Rec (single-source) |

> 说明：以上 6 篇在本轮检索中仅获得标题级信息，数值结论需回查原文；列为赛道补充，不进入正文详述。

### 2.12 Retrievers Need Verifiers `arXiv:2609.12270` / PMRecBench `arXiv:2611.06349`

- **核心观点**：生成式推荐的瓶颈正在从「retriever 召回」转向「verifier 校验」——semantic ID 生成的候选需要 verifier 过滤幻觉与非法 item；PMRecBench 则提供面向预训练推荐模型的统一 benchmark。
- **意义**：标志 generative recommendation 进入「retriever + verifier」协同阶段 (single-source)。
- **Links**: https://arxiv.org/abs/2609.12270 , https://arxiv.org/abs/2611.06349

---

## 3. Advertising, CTR & Auto-bidding

### 3.1 OneBid: Unified Auto-bidding `arXiv:2609.21550`

- **Title (EN)**: OneBid: Unified Bidding across Advertisers
- **Title (ZH)**: OneBid：跨广告主的统一出价
- **Affiliation**: Kuaishou Technology
- **Venue**: arXiv (single-source)
- **Abstract + Key Innovations**: 用单一生成式模型同时决定出价与预算分配，替代传统「predictor + optimizer」的两阶段 auto-bidding，并把多广告主约束（ROI、预算）统一进一个决策网络。
- **Comparison with Prior Methods**: 相比 PID / model-predictive-control 出价器，OneBid 直接端到端优化长期 utility，减少预测误差累积。
- **Link**: https://arxiv.org/abs/2609.21550

### 3.2 BAR: Bid-Aware Ranking `arXiv:2508.05206`

- **Title (EN)**: BAR: Bid-Aware Ranking
- **Title (ZH)**: BAR：出价感知排序
- **Affiliation**: Alibaba
- **Venue**: CIKM 2026 (single-source)
- **Abstract + Key Innovations**: 在 ranking 阶段显式引入 bid signal，把「排序分数」与「商业价值」解耦后联合优化，缓解 eCPM 与用户体验的目标冲突。
- **Comparison with Prior Methods**: 相比纯 CTR×bid 的乘性融合，BAR 学习 bid 与 relevance 的非线性交互。
- **Link**: https://arxiv.org/abs/2508.05206

### 3.3 Native Multimodal CTR `arXiv:2608.24091`

- **Title (EN)**: Native Multimodal CTR Prediction
- **Title (ZH)**: 原生多模态 CTR 预估
- **Affiliation**: Alibaba
- **Venue**: CIKM 2026 (single-source)
- **Abstract + Key Innovations**: 直接用多模态 backbone（图像/文本/视频）编码广告素材，替代人工特征与 late fusion，实现素材理解到 CTR 的端到端。
- **Comparison with Prior Methods**: 相比「多模态特征 → 拼接 → DNN」的 late fusion，early/native fusion 更能捕捉素材语义与用户兴趣的交互。
- **Link**: https://arxiv.org/abs/2608.24091

### 3.4 KDD 2026 CTR/Auction 线

| 论文 | arXiv/来源 | 机构 | 方向 |
|------|-----------|------|------|
| FAT | 2511.12081 | — | Feature-aware Transformer for CTR (KDD 2026) |
| TeMPO | KDD 2026 | Meta | Temporal preference optimization for ads (single-source) |
| GR4AD | KDD 2026 | Kuaishou | Graph reasoning for ad delivery (single-source) |
| AMS | KDD 2026 | — | Auto-bidding multi-slot (single-source) |
| EST | KDD 2026 | — | 广告排序中的效率-质量权衡 (single-source) |

### 3.5 PlatformBid `arXiv:2607.27265`

- **Title (EN)**: PlatformBid: Platform-Level Bidding
- **Title (ZH)**: PlatformBid：平台级出价
- **Affiliation**: Kuaishou Technology
- **Venue**: arXiv (single-source)
- **核心**: 从「广告主视角」转向「平台视角」优化整体生态（GMV、留存、广告收入），用约束优化平衡多方目标。
- **Comparison**: 相比单广告主 ROI 最大化，引入平台级长期收益与生态健康约束。
- **Link**: https://arxiv.org/abs/2607.27265

### 3.6 Rethinking Positional Encoding & Interaction Granularity for CTR `arXiv:2610.37140`

- **Title (EN)**: Rethinking Positional Encoding and Interaction Granularity for CTR Prediction
- **Title (ZH)**: 重思 CTR 预估中的位置编码与交互粒度
- **Affiliation**: Alibaba / Tencent / Peking University
- **Venue**: arXiv (single-source)
- **核心**: 系统消融 feature interaction 中的位置编码（field position）与交互粒度（bit/feature-level），指出二者耦合导致现有模型收益被高估。
- **Comparison**: 对 DCN / AutoInt / FIN 等经典结构做统一重评估，提出更细粒度的交互算子。
- **Link**: https://arxiv.org/abs/2610.37140

---

## 4. LLM Agents

### 4.1 ANTE: Agentic World Model for Software Engineering `arXiv:2610.15368`

- **Title (EN)**: ANTE: Agentic World Model for Software Engineering
- **Title (ZH)**: ANTE：面向软件工程的 Agentic World Model
- **Affiliation**: AWS AI Labs
- **Venue**: arXiv (single-source)
- **Abstract + Key Innovations**: 让 agent 在执行前先「预测」代码修改的环境反馈（world model），用预测结果过滤低质量 action。核心是把 SWE 任务建模为「状态转移预测 + 策略选择」。
- **关键数字**: Qwen3-32B 在 **SWE-bench Verified** 上 pass@1 从 **25.0% → 57.2%**；world-model 预测准确率 **44% → 69%**。
- **Comparison with Prior Methods**: 相比 ReAct / Reflexion 的「试错后反思」，ANTE 通过 world model **先验预测**减少无效 tool call，显著降低 rollout 成本。
- **Link**: https://arxiv.org/abs/2610.15368

### 4.2 Multi-step SWE Agent Evaluation `arXiv:2611.07166`

- **Title (EN)**: Can Agents Solve Multi-Step Software Engineering Tasks?
- **Title (ZH)**: Agent 能否解决多步软件工程任务？
- **Affiliation**: Klavis AI
- **Venue**: arXiv (single-source)
- **核心发现**: 构造多步 SWE benchmark，最强 agent 仅 **18.5%** 完全解决率，69 个任务中有 **38 个** 完全无解 —— 揭示当前 agent 在长程、多文件、多轮修改上的系统性短板。
- **Comparison**: 相比 SWE-bench 的单/少步修复，突出 multi-step 组合爆炸与上下文管理问题。
- **Link**: https://arxiv.org/abs/2611.07166

### 4.3 MLE-World `arXiv:2610.37175` / SWE-World `arXiv:2602.03419`

- **核心**: 两篇工作分别把 ML engineering 与 SWE 任务环境抽象为可交互的「world」，支持 agent 在低成本模拟环境中训练与评测，缓解真实执行昂贵、不可复现的问题。
- **意义**: 与 ANTE 共同指向「world-model + agent」的新范式 (single-source)。
- **Links**: https://arxiv.org/abs/2610.37175 , https://arxiv.org/abs/2602.03419

### 4.4 Aletheia (DeepMind) `arXiv:2602.10177` / RWML (Microsoft) `arXiv:2602.05842`

- **Aletheia**: DeepMind 的 agentic research assistant，强调可验证的推理与自动纠错 (single-source)。
- **RWML**: Microsoft 的 Real-World Markup Language / 真实世界建模 agent 框架 (single-source)。
- **Links**: https://arxiv.org/abs/2602.10177 , https://arxiv.org/abs/2602.05842

### 4.5 AuditBench (Anthropic) `arXiv:2602.22755`

- **Title (EN)**: AuditBench: Evaluating AI Agents on Auditing Tasks
- **Title (ZH)**: AuditBench：评估 AI Agent 的审计能力
- **Affiliation**: Anthropic
- **Venue**: arXiv (single-source)
- **核心**: 面向 agent 的「审计」类高信任任务 benchmark，考察 agent 发现错误、验证证据与给出可追溯结论的能力。
- **Link**: https://arxiv.org/abs/2602.22755

---

## 5. Code Execution Prediction & Coding Benchmarks

### 5.1 Software World Model `arXiv:2610.04940` / Self-Execution Simulation `arXiv:2604.03253`

- **Title (EN)**: Software World Model / Self-Execution Simulation
- **Title (ZH)**: 软件世界模型 / 自执行模拟
- **核心**: 让模型在不真正运行代码的前提下**预测执行结果**（变量值、输出、异常），即 code execution prediction。前者面向完整软件系统状态，后者聚焦单函数自执行模拟。
- **Comparison with Prior Methods**: 相比「调用 interpreter」的 tool-use 方案，world-model 预测零延迟、可批量；难点在于长程序与副作用建模。
- **Links**: https://arxiv.org/abs/2610.04940 , https://arxiv.org/abs/2604.03253

### 5.2 EarlyEval `arXiv:2609.02783` / CER `arXiv:2609.31995`

- **核心**: EarlyEval 关注「早期失败预测」——在程序执行早期判断是否会失败；CER 关注 code execution reasoning 的可解释评估。
- **Links**: https://arxiv.org/abs/2609.02783 , https://arxiv.org/abs/2609.31995

### 5.3 Benchmarks-as-Software / Terminal-Bench 2.1 `arXiv:2611.08417`

- **Title (EN)**: Benchmarks-as-Software: Terminal-Bench 2.1
- **Title (ZH)**: 作为软件的 benchmark：Terminal-Bench 2.1
- **核心**: 把 benchmark 本身实现为「可执行软件」，支持动态任务生成与防污染（contamination-resistant）评测；Terminal-Bench 2.1 聚焦真实终端操作任务。
- **Comparison**: 相比静态数据集式 benchmark，动态生成显著降低数据污染与过拟合。
- **Link**: https://arxiv.org/abs/2611.08417

### 5.4 其他代码相关 benchmark

| 论文 | arXiv | 机构 | 方向 |
|------|-------|------|------|
| SWE-Bench Pro Verified | 2609.08149 | — | 专家校验的高质量 SWE 子集 |
| ServerBench | 2611.06841 | — | 服务端/后端任务评测 |
| VeriHarm | 2611.03575 | — | 验证型推理与安全性 |
| DistDebug | 2611.03523 | — | 分布式系统调试 |
| Trace2Eval | 2611.06506 | — | 从 execution trace 评估 agent |
| PersonaCodeBench | 2611.05739 | — | 个性化代码生成 |
| Speculative Uncertainty | 2609.05274 | — | 代码生成中的不确定性度量 |
| DuET | 2604.11514 | — | 双视角执行轨迹建模 |

> 上述条目为赛道补充，数值需回查原文 (single-source)。

---

## 6. Generative Models & Sequential Modeling

### 6.1 Simplex Diffusion Models `arXiv:2609.35553` ✓

- **Title (EN)**: Simplex Diffusion Models
- **Title (ZH)**: Simplex Diffusion Models
- **Authors**: Google DeepMind / EPFL / UCL
- **Venue**: arXiv (28 Sep 2026)
- **Abstract + Key Innovations**: 在 **probability simplex** 上定义 diffusion 过程，直接对离散 token 的单纯形分布做前向加噪与反向去噪。在 OpenWebText 上以 **64 steps** 达到 **17.0 GenPPL**（unigram entropy 5.46），逼近 autoregressive 生成质量。
- **Comparison with Prior Methods**: 相比 D3PM / MDLM 等离散 diffusion，simplex 参数化避免了 categorical 噪声的组合爆炸，采样步数更少；相比 AR，支持并行解码与任意顺序生成。
- **Link**: https://arxiv.org/abs/2609.35553

### 6.2 Gumbel Straight Flow (DeepMind) `arXiv:2610.00497`

- **Title (EN)**: Gumbel Straight Flow
- **Title (ZH)**: Gumbel Straight Flow
- **Affiliation**: Google DeepMind
- **核心**: 用 Gumbel-softmax 重参数化构造「直线」flow，减少离散生成中的采样方差，把连续 flow matching 与离散 token 生成桥接。
- **Comparison**: 与 Simplex Diffusion 同属「离散空间连续化」路线，但采用 flow matching 而非 diffusion (single-source)。
- **Link**: https://arxiv.org/abs/2610.00497

### 6.3 Recirculation (DeepMind) `arXiv:2608.17981`

- **Title (EN)**: Recirculation
- **Affiliation**: Google DeepMind
- **核心**: 通过「再循环」机制复用中间计算，提升生成模型在长序列上的效率与一致性 (single-source)。
- **Link**: https://arxiv.org/abs/2608.17981

### 6.4 Multi-Mixer Oryx (Google) `arXiv:2605.28769`

- **Title (EN)**: Multi-Mixer: Oryx
- **Affiliation**: Google
- **核心**: 多尺度 mixer 架构，混合 attention 与 SSM/卷积以兼顾局部与全局建模 (single-source)。
- **Link**: https://arxiv.org/abs/2605.28769

### 6.5 CADENCE (Microsoft) `arXiv:2610.22788`

- **Title (EN)**: CADENCE
- **Affiliation**: Microsoft Research
- **核心**: 面向流式/连续生成的调度与缓存机制，报告 **1.3× throughput** 提升 (single-source)。
- **Link**: https://arxiv.org/abs/2610.22788

### 6.6 NCM (Stanford) `arXiv:2610.14162`

- **Title (EN)**: NCM: Neural Context Modeling
- **Affiliation**: Stanford
- **核心**: 从 context modeling 视角改进长序列生成 (single-source)。
- **Link**: https://arxiv.org/abs/2610.14162

### 6.7 ARMs are EBMs `arXiv:2512.15605`

- **Title (EN)**: Autoregressive Models are Energy-Based Models
- **核心**: 理论上证明 autoregressive model 可视为一种 energy-based model，为 AR 的训练/采样提供统一视角 (single-source)。
- **Link**: https://arxiv.org/abs/2512.15605

---

## 7. Games & World Models

### 7.1 PlayGen2 `arXiv:2611.07867` / RIDGE `arXiv:2611.05601`

- **核心**: PlayGen2 面向游戏内容/关卡的程序化生成；RIDGE 用 RL + world model 改进游戏 agent 的长期规划 (single-source)。
- **Links**: https://arxiv.org/abs/2611.07867 , https://arxiv.org/abs/2611.05601

### 7.2 RTSGameBench `arXiv:2606.18950` / CivWorldBench `arXiv:2610.16450`

- **核心**: 分别针对 RTS（实时策略）与文明类 4X 游戏构造 agent benchmark，强调长程规划、资源管理与多智能体交互。
- **Links**: https://arxiv.org/abs/2606.18950 , https://arxiv.org/abs/2610.16450

### 7.3 AutoWorldModel-Bench (EA) `arXiv:2608.11216` / WMEval `arXiv:2610.33894`

- **核心**: 自动评估 world model 的任务（预测、一致性、可控性）；EA 的 AutoWorldModel-Bench 面向游戏引擎级世界建模。
- **Links**: https://arxiv.org/abs/2608.11216 , https://arxiv.org/abs/2610.33894

### 7.4 Interactive Visual Gym `arXiv:2611.08286` / AWoMo `arXiv:2608.25518`

- **核心**: 可交互的视觉环境用于训练通用 agent；AWoMo 提供 action-conditioned world model 的统一框架。
- **Links**: https://arxiv.org/abs/2611.08286 , https://arxiv.org/abs/2608.25518

### 7.5 ARC-AGI-3 Grids `arXiv:2611.06793` / Gemini 4 Argon Minecraft `arXiv:2610.22319`

- **核心**: ARC-AGI-3 网格任务检验抽象推理；Gemini 4 "Argon" 在 Minecraft 环境中的 agentic 评测展示长程任务能力 (single-source)。
- **Links**: https://arxiv.org/abs/2611.06793 , https://arxiv.org/abs/2610.22319

---

## 8. Benchmarks & Evaluation

| 论文 | arXiv | 机构 | 评测对象 |
|------|-------|------|----------|
| SO-Bench | 2511.21750 | Apple | 系统级操作/OS agent |
| SiliconBench | 2609.19169 | Apple | Apple Silicon 上的推理服务 |
| GardenBench | 2610.23866 | — | 多工具/园艺式长任务 |
| Dual Exam | 2610.31066 | OpenAI | Agent 综合能力（GPT 6 Astra Agent Index 31.3） |
| STAR-PólyaMath | 2605.19338 | OpenAI | 数学推理的 Pólya 式分步评测 |
| RGPO | 2610.07342 | OpenAI | Reasoning-guided policy optimization |

**要点**：
- **Dual Exam** 报告 GPT 6 Astra 在 Agent Index 上仅 **31.3**，说明 agent 综合能力仍处早期。
- **STAR-PólyaMath** 把数学解题拆成「理解—计划—执行—回顾」四阶段，避免只看最终答案。
- **RGPO** 将 reasoning 轨迹纳入 policy optimization，属于训练方法而非纯 benchmark，列此以便对照。

---

## 9. 横向观察（Cross-cutting Observations）

1. **Generative Recommendation 进入「效率 + 校验」阶段**：早期工作（TIGER/HSTU）解决「能不能生成」，2026 年的 LWR/PRISM/HiGR 转向「生成得多快、多准」，并出现 retriever–verifier 分工。
2. **Agent 的瓶颈从「能力」转向「长程可靠性」**：ANTE 用 world model 减少试错，但 Multi-step SWE 显示最强 agent 仅 18.5% 解决率，Dual Exam 的 31.3 分同样说明综合 agent 仍弱。
3. **离散生成走向连续化**：Simplex Diffusion、Gumbel Straight Flow 共同把离散 token 映射到连续空间，用 diffusion/flow 降低采样步数。
4. **CTR/Auction 从「单点预估」走向「平台级约束优化」**：OneBid、PlatformBid 把多广告主、生态健康纳入目标。
5. **评测本身正在「软件化、动态化」**：Benchmarks-as-Software、Dual Exam、AuditBench 强调抗污染与真实任务。

### 代表工作对比表

| 方向 | 代表工作 | 关键创新 | 关键数字 |
|------|----------|----------|----------|
| Generative Rec | OneTrans-GSR | 单 Transformer 统一序列+生成 | — |
| Generative Rec | HiGR | 层次化 semantic ID 解码 | watch time +1.22%, 5× 加速 |
| Generative Rec | LWR | 低秩压缩 | −69.6% GFLOP |
| CTR/Auction | OneBid | 端到端统一出价 | — |
| Agent | ANTE | world model 预判环境反馈 | SWE-bench 25.0%→57.2% |
| Agent | Multi-step SWE | 多步任务 benchmark | 18.5% 完全解决 |
| 离散生成 | Simplex Diffusion | simplex diffusion | GenPPL 17.0 @ 64 steps |
| 评测 | Dual Exam | Agent 综合评测 | GPT 6 Astra 31.3 |

---

## 10. 公司覆盖矩阵

| 机构 | 代表工作 |
|------|----------|
| Google DeepMind | Simplex Diffusion, Gumbel Straight Flow, Recirculation, D4RT, Aletheia |
| Google | Oryx Multi-Mixer, RecSys 2026 Best Industry Paper |
| OpenAI | Dual Exam, STAR-PólyaMath, RGPO |
| Meta AI | LWR, PRISM, TeMPO |
| Microsoft Research | CADENCE, RWML |
| Anthropic | AuditBench |
| Apple | SO-Bench, SiliconBench |
| Amazon (AWS AI Labs) | ANTE |
| NVIDIA | （本轮未取得可核实条目，待补） |
| ByteDance | OneTrans-GSR |
| Alibaba | BAR, Native Multimodal CTR, Rethinking Positional Encoding |
| Tencent | HiGR |
| Kuaishou | EvoRec, DiffGRM, OneBid, PlatformBid, GR4AD |
| Baidu | （本轮未取得可核实条目，待补） |
| Netflix | GenRec |
| Meituan | UniCon |
| Walmart | BehaveRec |
| Ant Group | PACERec |
| Disney Research | RecSys 2026 Best Paper |
| Salesforce Research | LLMs Get Lost In Multi-Turn Conversation |
| Klavis AI | Multi-step SWE |
| Renmin University | DESRec |
| Stanford / Cambridge / ETH / UCL / Oxford | NCM / ICLR 2026 theory / Simplex / D4RT |

---

## 11. 参考与检索说明

- 会议官方：NeurIPS 2025 proceedings、ICLR 2026 outstanding papers、CVPR 2026 awards、ACL 2026 best papers、KDD 2026 program、RecSys 2025/2026 awards、AAAI 2026 (ojs.aaai.org/article/view/38504)。
- arXiv abs 页面（已核）：2611.01977、2611.04720、2611.06521、2609.35553。
- 其余 arXiv 编号来自检索摘要，标注 `(single-source)`，正式引用前请回查 abs 页面核对作者、机构与数值。
- 下一轮可补齐：NVIDIA（推理加速/agent）、Baidu（知识增强/推荐）、EMNLP 2026 与 CIKM 2026 完整 best-paper list。
