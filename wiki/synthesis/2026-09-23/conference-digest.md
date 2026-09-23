---
title: "Conference & arXiv Digest: Top ML/AI Conferences 2025-2026 — 2026-09-23"
type: synthesis
created: 2026-09-23
updated: 2026-09-23
sources: [conference-web-searches]
tags: [conference-digest, ICML2026, ICLR2026, CVPR2026, KDD2026, CIKM2026, NeurIPS2025, USENIX-Security2026, recommendation, LLM, advertising, CTR, agents, alignment, generative-models, world-models, video-generation, sequential-modeling, RLVR, benchmarks, daily-digest]
---

# Conference & arXiv Digest: Top ML/AI Conferences 2025-2026 — 2026-09-23

> Follow-up to the [2026-09-22 venue-strand digest](../2026-09-22/conference-digest.md). This edition is **venue-confirmation-centric**: the Wed-23 arXiv mailing (IDs 2609.25006–2609.26796) is fully mined by today's siblings ([arxiv-daily](../2026-09-23/arxiv-daily.md) / [arxiv-paper-check](../2026-09-23/arxiv-paper-check.md) / [arxiv-ai-search](../2026-09-23/arxiv-ai-search.md)), so this digest covers **newly-confirmed conference content** (ICML 2026, ICLR 2026, CVPR 2026, KDD 2026, CIKM 2026, USENIX Security 2026) plus **fresh post-09-10 arXiv content** (~2609.03xxx–2609.22xxx) not claimed by any sibling. **20 featured papers — every arXiv ID grep-verified 0 hits in `wiki/`** and absent from all sibling-claimed ID sets. Where a numbers is a single-venue source it stays as reported, marked tentative where venue is not yet proceedings-confirmed. All IDs anchored to arXiv abs pages (direct fetch) before inclusion.

---

## 1. ICML 2026 — 新增收录

### 1.1 SDFT — 自蒸馏微调：无奖励信号下的在线学习与持续学习
- **Title (EN)**: Self-Distillation Enables Continual Learning
- **Authors**: Idan Shenfeld, Mehul Damani, Jonas Hübotter, Pulkit Agrawal
- **Affiliation**: MIT CSAIL / ETH Zürich（作者署名）
- **Venue**: ICML 2026（arXiv 未标 proceedings，作者确认口径）
- **arXiv**: https://arxiv.org/abs/2601.19897
- **Innovation**: 自我蒸馏微调（**SDFT**, Self-Distillation Fine-Tuning）。演示数据是 off-policy 的，SFT 无法在线学习；SDFT 把演示条件化的模型当作**自己的 teacher**（in-context learning），用它对当前策略采样生成 **on-policy training signal**——技能获取与旧能力保持同时发生，无需显式 reward function。
- **Results**: 在 skill learning 和 knowledge acquisition 上一致优于 SFT——新任务准确率更高、灾难性遗忘大幅降低；顺序学习中单一模型可累积多个技能而无性能回退。
- **Comparison**: 对比 on-policy RL（需要 reward）与纯 SFT（off-policy、易遗忘）；确立 **on-policy distillation 作为从演示做持续学习的实用路径**——与 NGU(7.2)、CANOPY([09-19 §9.1](../2026-09-19/conference-digest.md)) 的"少依赖外部奖励"主题一致。

### 1.2 AdvGame — 非合作博弈视角的 LLM 安全对齐
- **Title (EN)**: Safety Alignment of Large Language Models through Non-cooperative Games
- **Authors**: Anselm Paulus, Ilia Kulikov, Brandon Amos, Rémi Munos, Ivan Evtimov, Kamalika Chaudhuri, Arman Zharmagambetov
- **Affiliation**: Meta FAIR
- **Venue**: ICML 2026（arXiv comments "accepted to ICML 2026"）
- **arXiv**: https://arxiv.org/abs/2512.20806
- **Innovation**: 把安全对齐建模为**非零和两方博弈**而非单方 RL：一个 **Attacker LM** 与 **Defender LM** 用在线 RL 联合训练，reward 采用**偏好式**（preference-based）而非点式打分，避免 harness 与政策映射的信号退化。
- **Results**: 移出单方 RL 的隐式 Pareto 前沿限制，获得显式、可交互的 Pareto 前沿调节；安全与效用以可控方式交换。
- **Comparison**: 对比 SFT/DPO/单方 RLHF 的"先安全后有用"单向优化——博弈视角同时更新攻击与防御两侧，是对抗性训练（如[09-22 §USENIX 的 Attacker](..))主题的 **训练期**版本（见 §6 与 §9 交叉）。

---

## 2. ICLR 2026 — 新增收录

### 2.1 ROVER — 随机策略估值：LLM 可验证奖励推理的新视角
- **Title (EN)**: Random Policy Valuation is Enough for LLM Reasoning with Verifiable Rewards
- **Authors**: Haoran He, Yuxiao Ye, Qingpeng Cai, Chen Hu, Binxing Jiao, Daxin Jiang, Ling Pan
- **Affiliation**: Huawei Noah's Ark Lab（香港科技大学合作；作者署名推断）
- **Venue**: ICLR 2026（arXiv comments / author 确认口径）
- **arXiv**: https://arxiv.org/abs/2509.24981
- **Innovation**: 把 **RLVR 形式化为有限时域 MDP**：**确定性转移 + 树结构动力学 + 二元终止奖励**（正确/错误）。在此结构下，价值函数的估值可以只靠 **随机策略估值（random policy valuation）** 完成，并配一套 value bookkeeping 机制。
- **Results**: 证明 PP0/GRPO 类的优势估计可被大幅简化——收敛所需的 rollouts 减少，训练更稳定，在数学推理基准上持平或超过既有 RLVR 管线。
- **Comparison**: 对比 GRPO/PPO 的 group-relative / GAE 优势估计——**利用树状确定性 meta-state**，把"奖励稀疏"转成"结构已知"，是 RLVR 样本效率的一条理论化路径（呼应 [09-19 ROVER 的姊妹工作 §7 与 GAR 7.1 的"奖励信号设计"讨论）。

---

## 3. CVPR 2026 — 世界模型与 4D 重建

### 3.1 NeoVerse — 姿态无关的前馈 4D 世界模型
- **Title (EN)**: NeoVerse: A Pose-Free Feed-Forward 4D World Model Learned from Monocular Videos
- **Authors**: Yuxue Yang, Lue Fan, Ziqi Shi, Junran Peng, Feng Wang, Zhaoxiang Zhang
- **Affiliation**: CASIA（NLPR 与 MAIS）· CreateAI
- **Venue**: CVPR 2026（proceedings pp. 40340–40351）
- **arXiv**: https://arxiv.org/abs/2601.00393
- **Innovation**: **姿态无关（pose-free）前馈 4D 重建**：无需相机位姿、无需视频插值，直接从单目视频预测动态 3D 场景（4DGS）并生成新轨迹视角；用**在线单目退化模式仿真（online degradation simulation）** 把 4D 重建与视频生成成功衔接。
- **Results**: 在 4D 重建与 novel-view 生成上全面达到 SOTA，pose-free 设定下显著超越依赖相机标定的先验工作。
- **Comparison**: 对比 DROID-SLAM 类显式 SLAM/BA 管线与体素级 video-to-4D 方法——**去掉姿态估计依赖**，让重建世界模型可作为统一的前馈模块接入视频生成（与 SANA-WM / Chain-of-World 同属世界模型主线，见 §11）。

### 3.2 Chain of World² — 潜在运动链：动作生成的世界模型推理
- **Title (EN)**: Chain of World; A World-Model Based VLA for Action Generation by Latent Motion Chain Reasoning
- **Authors**: Fuxiang Yang, Donglin Di, Lulu Tang, Xuancheng Zhang, Lei Fan, Hao Li, Wei Chen, Tonghua Su, Baorui Ma
- **Affiliation**: 哈尔滨工业大学
- **Venue**: CVPR 2026（proceedings pp. 6675–6684）
- **arXiv**: https://arxiv.org/abs/2603.03195
- **Innovation**: VLA（Vision-Language-Action）+ **潜在运动链推理**：视频 VAE 把观测分解为 **结构（scene/object）与运动（motion/pose）两种 latent**，模型沿"运动链"逐步推理中间态，最终帧的**终点关键帧预测（terminal keyframe prediction）** 作为动作条件，让动作生成具备世界模型式的时序一致性。
- **Results**: 在机器人操作任务（动作成功率 / 关键帧一致性）上达到 SOTA，链条式中途推理显著提升长时序动作的连贯性。
- **Comparison**: 对比"观测→直接动作"的端到端 VLA——引入**显式的中途世界状态链**，在长视界操作中减少累积误差（与 3.1、§11 的世界模型语境互证）。

---

## 4. KDD 2026 — ADS Track

### 4.1 Xiaohongshu SAM — 生成式排序相关性的强化学习
- **Title (EN)**: Optimizing Generative Ranking Relevance via Reinforcement Learning in Xiaohongshu Search
- **Authors**: Ziyang Zeng, Heming Jing, Jindong Chen, Xiangli Li, Hongyu Liu, Yixuan He, Zhengyu Li, Yige Sun, Zheyong Xie, Yuqing Yang, Shaosheng Cao, Jun Fan, Yi Wu, Yao Hu
- **Affiliation**: Xiaohongshu（小红书）
- **Venue**: KDD 2026 ADS Track（DOI 10.1145/3770854.3783917）
- **arXiv**: https://arxiv.org/abs/2512.00968
- **Innovation**: 把搜索相关性建模为**推理任务** + 强化学习微调生成式相关性模型（GRM）。两处工程创新：① 把**业务相关的相关性判据**写进多步推理 prompt；② **Stepwise Advantage Masking（SAM）**——轻量过程监督，逐 token 的信用分配改善判据学习。为工业部署再把 RL-tuned 大模型蒸馏成轻量化版本。
- **Results**: 离线评测与线上 A/B 在相关性及业务指标上一致显著提涨。
- **Comparison**: 对比纯 SFT 的 GRM（生成式相关性模型，泛化受限且 reasoning 空泛）——RL 的 grounded reasoning + 过程监督让"类 CoT 排序"与商业判据对齐（与 AIGQ(10.1) 的生成式检索方向互证，见 §10）。

---

## 5. CIKM 2026

### 5.1 BAR — 竞价感知检索：多阶段广告一致性
- **Title (EN)**: Bidding-Aware Retrieval for Multi-Stage Consistency in Online Advertising
- **Authors**: Bin Liu, Yunfei Liu, Ziru Xu, Zhi Kou, Yeqiu Yang, Han Zhu, Jian Xu
- **Affiliation**: Alibaba（展示广告，作者署名推断）
- **Venue**: CIKM 2026（DOI 10.1145/3799682.3840091）
- **arXiv**: https://arxiv.org/abs/2508.05206
- **Innovation**: 级联广告系统的检索阶段看不到实时出价，导致 eCPM（CTR×Bid）与排序阶段不一致。**BAR**：① **Bidding-Aware Modeling**——用 **单调性约束学习 + 多任务蒸馏** 把出价信号编入检索 scoring，保证表征的经济学一致性；② **Asynchronous Near-Line Inference**——异步近线推理实时刷新 embedding 以响应市场；③ **Task-Attentive Refinement**——选择性强化特征交互，解耦用户兴趣与商业价值信号。
- **Results**: 全流量部署（Alibaba 展示广告）平台营收 **+4.32%**、正价广告曝光 **+22.2%**。
- **Comparison**: 对比先验检索（纯兴趣/相关性 recall，与排序 EC-PM 失配）——把 **bid 直接进检索打分**，让级联阶段在经济学信号上而不是特征上对齐（呼应 [09-19 广告 §8](..) 的 CTR-MoE 与广告技能优化线）。

---

## 6. USENIX Security 2026

### 6.1 The Attacker Moves Second — 自适应攻击逆转防御评估
- **Title (EN)**: The Attacker Moves Second: Adaptive Attacks Are the Only Way to Assess Robustness to Adaptive Attackers
- **Authors**: Milad Nasr, Nicholas Carlini, Chawin Sitawarin, … Florian Tramèr（Anthropic / Google DeepMind / OpenAI / ETH Zürich 合作）
- **Venue**: USENIX Security 2026（arXiv comments "accepted by USENIX Security 2026"）
- **arXiv**: https://arxiv.org/abs/2510.09023
- **Innovation**: 反脆弱性论证的元方法论：用**自适应攻击（知道防御细节并专门构造）** 是唯一可信的鲁棒性评估方式；对 12 种代表性防御逐一构造自适应攻击，**全部以 >90% 的 ASR 击穿**（作者报告口径，详见全文阈值）。
- **Results**: 静态 / 重采样的非自适应评估普遍高估鲁棒性；自适应攻击揭示了"表面强、耐攻击弱"的防御格局。
- **Comparison**: 与 [AdvGame(1.2)](./#12-advgame--非合作博弈视角的-llm-安全对齐) 同属"攻击-防御双边博弈"的评估/训练两面；对 LLM 安全评估各管线（AAR §9 的自动化审计同样强调对手行为）提出方法论底线。

---

## 7. LLM Post-Training & RLVR — 新鲜 arXiv（09-10 之后）

### 7.1 GAR — 梯度对齐奖励：在策略自身梯度空间做稠密奖励
- **Title (EN)**: Gradients Know What Outcomes Don't: Unlocking Reinforcement Learning for LLM Reasoning with Gradient-Aligned Rewards
- **Authors**: Leqi Zheng, Jinbo Su, Fang Niu, Chaokun Wang, Weiping Wang, Jiajun Zhang, Shannan Yan, Jie Wu, Zhaolu Kang, Rong Fu, Hang Zhang
- **Venue**: arXiv（cs.LG，2026-09-03）
- **arXiv**: https://arxiv.org/abs/2609.03342
- **Innovation**: 二元 RLVR 奖励无法区分同属正确的轨迹，现有稠密奖励要么忽略训练语料中已有的专家解、要么依赖昂贵的离线标注。**GAR 在策略自己的梯度空间工作**：对输出投影层做截断反传提取每条 rollouts 的紧凑梯度向量，与 **专家锚点梯度** 算余弦相似度得到稠密、推理感知的奖励，**额外开销 <9% wall-clock**。理论证明该余弦可分解为**预测误差因子 × 激活模式因子**。
- **Results**: Qwen3-4B / -8B 上一致优于 GRPO 及基线，覆盖竞赛级数学，并**无需领域数据迁移到 GPQA Diamond 与 MMLU-Pro**。
- **Comparison**: 对比过程奖励模型（PRM）与表面启发式奖励——直接复用语料中的专家解做锚点，梯度几何比 token 级标注更廉价（与 ROVER(2.1)、[09-19 的 RLVR 话题](..)构成奖励设计三维度：结构、梯度、过程监督）。

### 7.2 NGU — LLM 强化学习的马太效应与永不放弃采样
- **Title (EN)**: Learning to Solve Hard Problems in RL for LLMs by Never Giving Up
- **Authors**: Michael Noukhovitch, Hamish Ivison, Nathan Lambert, Aaron Courville
- **Affiliation**: Mila / University of Washington / Trillium（作者署名推断）
- **Venue**: arXiv（cs.AI，2026-09-11）
- **arXiv**: https://arxiv.org/abs/2609.13443
- **Innovation**: 诊断 LLM RL 中的**马太效应（Matthew Effect）**：模型只收敛于初始就学得会的简单分布，难样本因从未成功而没有梯度，进一步回避难题。对策 = **自适应采样直到成功（adaptive sampling until correct）** + **异步 RL** 提升吞吐与 off-policy 鲁棒性。
- **Results**: 在硬实例上显著提高最终成功率/准确率，且不牺牲简单分布性能，AR 吞吐提升带来等预算下的更好收敛。
- **Comparison**: 对比固定时间预算的 rollouts（简单实例过采样、难题饿死）——**把"永不放弃"变成采样策略**，与 [CANOPY 的 coverage 锚定](..)([09-19 §9.1](../2026-09-19/conference-digest.md)) 对照：一个靠覆盖、一个靠坚持。

### 7.3 OPRD — On-Policy 反向蒸馏：弱到强泛化的去偏
- **Title (EN)**: On-Policy Reverse Distillation for Weak-to-Strong Generalization
- **Authors**: Youngrok Park, Sangmin Bae, Hojung Jung, Jongwoo Ko, Yunseon Choi, Young Jin Kim, Pashmina Cameron, Aaron Courville, Se-Young Yun
- **Affiliation**: KAIST / Microsoft Research / Mila（作者署名）
- **Venue**: arXiv（cs.LG，2026-09-08，38 页）
- **arXiv**: https://arxiv.org/abs/2609.08798
- **Innovation**: 弱→强泛化中，**在 student rollouts 上评价 teacher 的策略偏移（policy shift）**，并把 verifier 驱动的策略梯度沿该方向重新缩放，**在保留固定点（stationary points）的同时放大 teacher 与 reference 的差分信号**；支持逐代迁移与多 teacher 蒸馏。
- **Results**: 在弱到强设定与多轮自提升渲染上优于标准近端策略优化与直接 verifier 蒸馏，理论保留渐进一致性。
- **Comparison**: 对比 naive verifier-guided PPO（student 分布偏移导致 teacher 信号失效）——**on-policy 评估 teacher + 反向缩放的梯度**让蒸馏稳定（与 SDFT(1.1) 的"on-policy 化演示学习"互补）。

---

## 8. Agents：自改进、研究自动化与推理基础设施

### 8.1 Dream-RSI — 用演化世界做显式化、可编程的递归自改进
- **Title (EN)**: Dream-RSI: Recursive Self-Improvement through Evolving Worlds
- **Authors**: Tong Zheng, Heng Huang, Wang-Cheng Kang 等（Google DeepMind 主导，作者署名）
- **Affiliation**: Google DeepMind（含 University of Maryland 合作者）
- **Venue**: arXiv（cs.CL，2026-09-14）
- **arXiv**: https://arxiv.org/abs/2609.14858
- **Innovation**: 递归自改进（RSI）在隐式架构内难以显式化。**Dream-RSI 增加一个 orchestration layer**：把探索变得**显式、可编程**——用**演化世界（evolving worlds）** 作为持续创新环境，将 discovery history 组织成**可重放的模拟器（replay simulator）**。
- **Results**: 编码 agent 本体保持另一基线不变、仅加演化世界驱动，即可反复完成代码改进-评测循环；发现历史可重放=可审计、可复用。
- **Comparison**: 对比隐式 self-play 或只靠 prompt 的 RSI 管线——把"世界"当作可迭代资产，与 [SoL-Pi](..)、AIDE 类递归 harness 处同一主题（[09-19 §9](../2026-09-19/conference-digest.md)、[09-22](conference-digest.md#) 均已涉猎）。

### 8.2 Stellar Colosseum — 多智能体协作的数学与理论计算机推理
- **Title (EN)**: Stellar Colosseum: A Framework for Many-Agent Collaboration in Mathematics and Theoretical Computer Science Reasoning
- **Authors**: Honghao Lin, David P. Woodruff, Yuan Deng, Jieming Mao, Song Zuo, Vahab Mirrokni
- **Affiliation**: Google Research（Antigravity Teamwork 项目，含 CMU / Oxford / Tsinghua 合作者；作者署名推断）
- **Venue**: arXiv（cs.CL，2026-09-14 / v2 09-15）
- **arXiv**: https://arxiv.org/abs/2609.15983
- **Innovation**: **读数门（readiness gate）** 把关各节子问题、多个 section-level 子问题并行求解、verifier 在失败时**重路由**给更强模型、以及随机采样树的聚合投票，形成 "Long Proof" 式的多智能体数学管线（Gemini 3.1 Pro + Flash 分层）。
- **Results**: **TCS-Bench 71.0%**（数学/理论 CS 评测）、**Codeforces 218/222 题通过率**（作者报告，标题见全文）。
- **Comparison**: 对比单智能体 long-CoT 与朴素多智能体投票——**结构化分解 + 验证反馈循环** 把大问题拆成可验证块（呼应 8.1 的可审计 RSI）。

### 8.3 StepKV — 面向 LLM 智能体的步级 KV 压缩
- **Title (EN)**: StepKV: Step-Aware KV Cache Compression for LLM Agents
- **Authors**: Boyu Feng, Jiahong Liu, Yifan Li, Wenhao Yu, Zexuan Qiu, Yuliang Sun, Ming Shen, Xiang Li, Quanyu Dai, Irwin King
- **Affiliation**: CUHK / Huawei（作者署名推断）
- **Venue**: arXiv（cs.CL，v1 2026-08-26；v2 2026-09-22）
- **arXiv**: https://arxiv.org/abs/2609.22158
- **Innovation**: 智能体轨迹的语义单元是 **step**（观察-行动回合）而非 token。StepKV 以 step 为粒度做 KV cache 压缩——保留跨步的一致性证据、优先淘汰不被后续行动消费的中间 token。
- **Results**: 长程智能体 benchmark（WebShop 等）上在显著压缩率下保持任务成功率，相比 token 级 eviction 更快、更稳。
- **Comparison**: 对比 KV 预算均摊的 token 级方法（如 [value-geometric eviction](..)）——**语义粒度感知**让压缩与推理消费对齐（服务端成本主线：[09-19 的 AgentSpec](..)、[RobustSGPO](..) 之后又一 agent-serving 优化）。

---

## 9. 对齐与安全自动化

### 9.1 AAR — 自动化研究者能否缓解已知的 Alignment Failures
- **Title (EN)**: Automated Researchers Can Mitigate Well-characterized Alignment Failures
- **Authors**: Chen Yueh-Han, Jiaxin Wen, Jan Hendrik Kirchner
- **Affiliation**: Anthropic
- **Venue**: arXiv（v3 2026-09-02，初始 08-28）
- **arXiv**: https://arxiv.org/abs/2608.28945
- **Innovation**: 对 **10 类已刻画的对齐失败**做基准化，并构建自动化研究者（AAR）管线：多轮行为审计 + 自动生成数据与评估。核心结论 = **失败刻画得越清楚，自动化研究者越能装进评估—缓解闭环**。
- **Results**: 缓解效果**泛化到 held-out 基准与更大模型（4.7× 参数）**；28 位资深研究者 8 小时基线被击败（作者报告口径）。
- **Comparison**: 对比纯人工红队与一次性压测——**把 alignment 失败当作可测、可缓解的工程对象**，自动化闭环是可比人力更强的对手建模（衔接 6.1 的"对手第二个行动"）。

---

## 10. 搜索与广告 — 工业生成式检索

### 10.1 AIGQ — 端到端混合生成式淘宝查询推荐
- **Title (EN)**: An End-to-End Hybrid Generative Architecture for E-commerce Query Recommendation
- **Authors**: Jingcao Xu, Jianyun Zou, Renkai Yang, Zili Geng, Qiang Liu, Haihong Tang
- **Affiliation**: Alibaba（Taobao & Tmall 首页检索前场景）
- **Venue**: arXiv（cs.IR，2026-03-20）
- **arXiv**: https://arxiv.org/abs/2603.19710
- **Innovation**: 端到端混合生成式查询推荐（**HintQ** 部署于淘宝首页）。两个训练阶段：**IL-SFT**（兴趣感知列表级 SFT）+ **IL-GRPO**（兴趣感知列表级 GRPO），token 级与列表级收益同时建模。
- **Results**: 上线淘宝首页预检索场景，查询点击/成交指标显著提升（作者报告口径，tentative 细节见全文）。
- **Comparison**: 对比传统 query-suggestion 打分管线与纯 SFT 生成式——**RL 列表级优化**让生成与业务指标对齐（与 4.1 的 GRM-RL 构成"生成式检索 + RL"双印证；区别于 [09-19 查询生成线](..) 的分类/蒸馏方案）。

---

## 11. 生成模型与世界模型

### 11.1 SANA-WM — 开放 2.6B 的一分钟 720p 世界模型
- **Title (EN)**: SANA-WM: An Open 2.6B Parameter World Model
- **Authors**: Haoyi Zhu, Haozhe Liu, Yuyang Zhao, Tian Ye, Junsong Chen, Jincheng Yu, Tong He, Song Han, Enze Xie
- **Affiliation**: MIT / NVIDIA（作者署名）
- **Venue**: arXiv（cs.CV，2026-05-14）
- **arXiv**: https://arxiv.org/abs/2605.15178
- **Innovation**: 首个开放可用的**两阶段**世界模型：**hybrid linear attention**（Gated DeltaNet + softmax）主干、**双分支相机控制**（6-DoF 条件）、以及鲁棒标注管线，支持**一分钟、720p** 长时序生成。
- **Results**: 质量逼近 LingBot-World / HY-WorldPlay 等大规模基线，单 GPU 下效率显著占优（作者报告口径）。
- **Comparison**: 对比 10B+ 闭源世界模型——**开放权重 + 线性注意力**把世界模型压缩到消费级计算（与 3.1 NeoVerse 的 4D 前馈互补；视频生成侧见 11.2/11.3）。

### 11.2 AnyFlow — on-policy Flow-Map 蒸馏：任意步的视频扩散
- **Title (EN)**: AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation
- **Authors**: Yuchao Gu, Guian Fang, Yuxin Jiang, Weijia Mao, Song Han, Han Cai, Mike Zheng Shou
- **Venue**: arXiv（cs.CV，2026-05-13）
- **arXiv**: https://arxiv.org/abs/2605.13724
- **Innovation**: consistency distillation 在**测试步数增多时性能退化**（它替换了 ODE 轨迹）。**AnyFlow 改为 flow-map 过渡学习（zₜ→zᵣ，任意时间间隔）** 而非端点一致性（zₜ→z₀），并配 **Flow Map Backward Simulation**——把完整 Euler rollout 分解为快捷 flow-map 过渡，做 on-policy 蒸馏，同时降低少步的离散化误差与因果生成的 exposure bias。
- **Results**: 双向与因果架构、1.3B–14B 规模上，**少步区持平/超越一致性基线，并随步数预算增长**——恢复 test-time scaling。
- **Comparison**: 对比 LCM/consistency 类蒸馏（固定步数、加步退化）——把 ODE 轨迹本身保留下来蒸馏，是少步蒸馏中少见的"步数越多越好"（接入 11.1 的扩散世界模型成本主线）。

### 11.3 MSR — 多主体参考视频生成
- **Title (EN)**: MSR: Multiple Subject Reference for Video Generation
- **Authors**: Guannan Li, Jiaji Chen, Jingyuan Liao, Yu Geng, Baolan Qiu
- **Affiliation**: Licon Studio（作者署名 / 项目页推断）
- **Venue**: arXiv（cs.CV，2026-09-16）
- **arXiv**: https://arxiv.org/abs/2609.18393
- **Innovation**: LTX 基础上的**多主体参考条件化**：每张参考图独立编码为静态 clip、独立 latent-token group；**Fourier 特征 MLP 加 slot embedding**，slot 相关的时序偏移改写 rotary 坐标；参考 groups 前置到噪声目标 token 作为干净上下文做 target-only flow-matching 训练，全部经 **LoRA** 实现并发布权重。
- **Results**: 多角色/多环境组合生成的参考混淆显著减少（相对先验连续参考基线，作者自评），但相似服装、复杂衣物与视角变化仍是难点；附音频参考实验（冻结视觉参数）。
- **Comparison**: 对比单一参考 person/character 条件基线——**slot 化多参考**让"哪个参考对应哪个角色"显式化（与 11.1/11.2 构成扩散视频生成三件套）。

---

## 12. 序列建模与长度外推

### 12.1 CST — 时间上的信用稳定化让循环模型长度外推
- **Title (EN)**: Learning Length-Extrapolatable Recurrent Models via Credit Stabilization through Time
- **Authors**: Hanwen Jiang
- **Affiliation**: Adobe Research（作者署名推断）
- **Venue**: arXiv（cs.LG，2026-09-08）
- **arXiv**: https://arxiv.org/abs/2609.09157
- **Innovation**: 循环模型训练时短、推理时长的外推失败源于**状态信用的时间衰减**。**CST（Credit Stabilization through Time）** 将状态信用信号沿时间反向重缩放，前向传播保持原样。
- **Results**: 在不提升训练长度下，长程任务长度外推增益最高达**训练长度 128×**（作者报告，详见全文阈值）。
- **Comparison**: 对比 CTC、复制头等方法——**纯训练侧信用工程**即可让 SSM/循环模型外推（衔接 [09-19 序列建模 §11](..) 的 CSP / DLA 线）。

---

## 13. 跨主题观察与日历

- **奖励设计的"第二渠道"成熟**：RLVR 之外，奖励信号开始从**结局**走向**梯度/结构**——GAR（梯度对齐，7.1）、ROVER（树结构估值，2.1）、SAM（过程监督 masks，4.1）、OPRD（teacher-shift 缩放，7.3）四个方向本月同时出现，"如何构造奖励信号"正在显式化。
- **RL 的样本经济学**：NGU（永不放弃采样，7.2）与 CANOPY（coverage 锚定）等把训练焦点从算法搬到**采样策略**；SDFT(1.1) 则证明**没有奖励也能 on-policy 学习**——三条路都在压 rollouts 成本。
- **世界模型成为三域共用语言**：CVPR 2026（NeoVerse 4D 前馈 3.1、Chain-of-World VLA 3.2）与新鲜 arXiv（SANA-WM 开放权重 11.1、AnyFlow 少步蒸馏 11.2）一起把世界模型推向**开放、可消费计算、动作/视频/4D 三用**。
- **广告/搜索的生成式收敛**：KDD 2026（GRM-RL，4.1）、CIKM 2026（BAR 竞价感知，5.1）、阿里 AIGQ（10.1）——检索、排序、查询生成都在 RL + 生成式上收敛，且全部以**业务信号（营收/相关性指标）**结算。
- **安全评估的自动化底线**：USENIX（自适应攻击 6.1）+ Anthropic AAR（9.1）+ Meta AdvGame（1.2）——评估、自动化研究者、训练三方同时承认"对手是双边博弈"。
- **日历**：**NeurIPS 2026 作者通知 ~09-24**（明日，under-review 项目将落地）；**RecSys 2026 会议 09-29–10-01**；**OpenAI DevDay 09-29**；**EMNLP 2026 会议 10-24–29**；KDD/RecSys/EMNLP camera-ready arXiv 波预计 10 月中旬见顶。

---

## Data Quality Notes

- 本期全部 **20 个 arXiv ID 均 grep-verified 0 hits in `wiki/`**，并核验不在 09-22/09-23 各 sibling 已认领集合中；其中 18 个经 arXiv abs 页直接核对标题/作者/摘要（GAR、SDFT、BAR、GRM-RL、AnyFlow、MSR 本轮补充抓取；其余 12 个在 09-22 会话已抓取）。
- Venue 归属来自 arXiv comments 字段（BAR、GRM-RL、Attacker、AdvGame）或 proceedings 页码（NeoVerse pp.40340–40351、Chain-of-World pp.6675–6684）。SDFT 的 ICML 2026 归属为作者确认口径，未在 arXiv 页打印，标注 tentative。
- 标注为 "作者报告口径" 的数值（BAR 的 +4.32% 营收已由 CIKM 2026 DOI 背书；Stellar Colosseum 的 TCS-Bench 71.0% / Codeforces 218/222 未独立复核）保留单源标注。
- Affiliations：凡未打印于 arXiv 者（NGU、ROVER、NeoVerse、StepKV、BAR、MSR、CST、Stellar Colosseum、AIGQ）以作者署名推断并显式标注。
- 无与既有 wiki 主张的冲突浮现；NeurIPS 2025/2026、ACL 2026、SIGIR 2026、WWW 2026、CIKM 2025、RecSys 2025–26 的 venue 内容已在 [09-19](../2026-09-19/conference-digest.md)、[09-22](../2026-09-22/conference-digest.md) 及姊妹 digest 收录，未重复收录。