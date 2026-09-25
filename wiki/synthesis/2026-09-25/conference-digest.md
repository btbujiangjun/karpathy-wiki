---
title: "Conference Digest: Top ML/AI Conferences 2025-2026 + Fresh arXiv — Full Edition 2026-09-25"
type: synthesis
created: 2026-09-25
updated: 2026-09-25
sources: [conference-web-searches, arxiv-listings]
tags: [conference-digest, ICML2026, ICLR2026, NeurIPS2025, AAAI2026, KDD2026, CVPR2026, SIGIR2026, ACL2026, EMNLP2025, WWW2026, CIKM2025, RecSys2025, RecSys2026, recommendation, LLM, advertising, CTR, agents, generative-models, sequential-modeling, games, code-execution, benchmarks, world-models, daily-digest]
---

# Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-09-25

> Full Edition. Sweep of the **fresh Friday 25 Sep 2026 arXiv window (IDs 2609.28504–2609.30266, 577 parsed entries across cs.AI/LG/CL/IR/CV/GT/MA/NE/RO/SE/HC)** plus the **conference-proceedings sweep** across ICML 2026 / ICLR 2026 / NeurIPS 2025 / AAAI 2026 / KDD 2026 / CVPR 2026 / ACL 2026 / EMNLP 2025 / SIGIR 2026 / WWW 2026 / CIKM 2025 / RecSys 2025/2026.
>
> **Dedup discipline**: today's sibling digests (arxiv-ai-search / arxiv-daily / arxiv-paper-check / game-rl-daily, all 2026-09-25) already committed. **22 featured papers are exclusive to this digest**: fresh-window IDs grep-verified absent from all 4 siblings' claimed sets AND absent from `wiki/` at write time (only the venue-sweep items C1/L3 are pre-fire: HOBA was featured in 08-26 arxiv-daily, Flexibility Trap in 07-30→09-05 digests). **8 featured entries overlap with other claims** — R3 slate (all 3 search siblings), C2 ScalarLens (ai-search §1.2), L1 PoEM / A2 AdvRole / W1 WROP / W2 HelloWorld (game-rl-daily §③/②/⑦) — marked `⚠️dup` and cross-referenced in §5, not silently re-featured.

---

## 1. 会议扫描 — Venue-by-Venue Highlights (2025–2026)

> Best-paper awards and marquee acceptances confirmed via official proceedings pages / arXiv comments during web sweep. Where the agent could not verify from the official page, marked *tentative*.

### 1.1 ICML 2026

- **The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models** — ICML 2026 **Outstanding Paper** (arXiv:2601.15165, Tsinghua + Qwen-team researchers)。核心主张:对一般推理任务(数学、代码),dLLM 的"任意顺序生成"反而限制推理潜力——模型会用顺序灵活性绕过高不确定性 token,导致 solution coverage 过早坍缩。直接对 dLLM 应用标准 GRPO(**JustGRPO**,放弃任意顺序但保留并行解码)即取得 GSM8K **89.1%**。**对 wiki 的扩散 LM scaling 线(shannon scaling law / LaDiR)是一个重要反论证**。
- 本领域另有 *High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions*(MIT)被评为杰出论文 + 一篇 alignment 立场文争议(评审认为其"unintentionally building a censor's toolkit")。

### 1.2 ICLR 2026 (Singapore, Apr 25–27; 225 Oral)

- **ReTool: Reinforcement Learning for Strategic Tool Use in LLMs**(Jiazhan Feng, Yujia Qin, Wanjun Zhong 等)— 在线 RL 把多轮实时 code execution 交织进 long-form reasoning,按 outcome feedback 学习"何时/如何"调用工具,弥补 reasoning model 在结构化求解任务上的短板。
- **Kimi-Dev: Agentless Training as Skill for SWE-agents**(Zonghan Yang 等, Moonshot AI)— 用纯 agentless 流程收集轨迹当技能迁移给 SWE-agent,开源 SWE LLM 达 **60.4% SWE-bench Verified**,workflow 类方法最佳。
- **CodeGym: Generalizable End-to-End Tool-Use RL with Synthetic CodeGym**(arXiv:2509.17325)— 编程题自动转成交互式 POMDP tool-use 环境(13k env / 80k+ 配置),GRPO 端到端 RL;Qwen2.5-32B 在 τ-Bench 等 OOD 基准平均 **+7.3**(过滤后近乎翻倍)。
- 同批趋势: **DreamGym**(experience synthesis 为 agent 在线 RL 合成经验)、**AgentFlow**(flow-based GRPO 在活环境优化 planner)、**VisCoder2 / Critique-Coder**。
- 另加拉:**Mixture-of-Experts Can Surpass Dense LLMs Under Strictly Equal Resource**(arXiv:2506.12119)— 约 200 个 2B + 50+ 个 7B 模型、50T tokens 消融;最优 activation rate ≈20%,MMLU 32.9 vs 31.26(约一半计算),支持 CTR 侧的 MoE scaling 论点。

### 1.3 NeurIPS 2025

- **Gated Attention for LLMs** — NeurIPS 2025 Best Paper (arXiv:2505.06708, Qwen/Alibaba)。已在 wiki 收录([[gated-attention]]):SDPA 后加 head-specific sigmoid gate,attention-sink-free、1.734× 预训练效率提升。*Wiki 内已注:gated attention 与 [[onepiece]] 的 context engineering 分属不同效应层。*
- **1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities**(Kevin Wang 等, Newport 组)— Best Paper。无奖励目标条件 RL 中把 depth 推到 1024 层,性能较浅层 contrastive RL 提升 **2×–50×**,是"RL 随深度扩展"的标志性结果。
- **VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents**(Kangrui Wang 等)— POMDP + WorldModeling Reward + Bi-Level GAE 显式做 state estimation / transition modeling,3B 模型 0.21 → **0.82**,超过 GPT-5 (0.75)、Gemini 2.5 Pro、Claude 4.5。

### 1.4 AAAI 2026

- 扫描未命中显著的新 Best Paper 级内容进入本窗口(AAAI 2026 已在北京召开 2026-02;新接受论文的 arXiv wave 与本 digest 无新增)。

### 1.5 KDD 2026 (Jeju) & KDD Cup 2026

- **HOBA: Hierarchical On-Policy Bidding Agents for Adaptive Online Advertising**(arXiv:2607.24779, KDD 2026 ads track)— 高层 LLM(Think-Act-Observe-Reflect + 经验检索)推断超参,中层 SARSA agent 以 causal adjustment 消除选择偏差并在 PID/MPC/IQL/Decision Transformer 专家池动态选模型;AuctionNet + 大规模 A/B 优于 SOTA,线上 target cost **+3.6%**。⚠️ **pre-featured 于 08-26 arxiv-daily;此处作为 KDD 2026 venue 确认的纪要保持,不宣称独家**。
- KDD Cup 2026 UniRec 冠军 QueryFormer 已在 [[conference-digest 09-19]] 收录;AI Search CVR 冠军方案已在 arxiv-paper-check 收录。

### 1.6 CVPR 2026

- **Best Paper — Efficiently Reconstructing Dynamic Scenes One D4RT at a Time**(Google DeepMind / UCL / Oxford)— 动态 4D 场景重建,单次 D4RT 迭代式重建范式(2026 共 16,092 投稿 / 4,089 接收)。
- **Best Paper — Native and Compact Structured Latents for 3D Generation**(Tsinghua / MSR / USTC / Microsoft AI)— 3D 生成的结构化 natively-compact latent 表示。

### 1.7 ACL 2026 (Best Papers, 2026.aclweb.org verified)

- **The Imperfective Paradox in Large Language Models**(Miyao 组)— 对 LLM 中"未完成体"(imperfective)语言处理的现象学刻画。
- **Memory Efficiency and Resource-Rational Encoding in Sentence Processing**(Dillon / Futrell)— 记忆效率与 resource-rational 编码的实证刻画,与 EMNLP 2026"attention=episodic lookup, recurrence=language/persona"线互补。

### 1.8 EMNLP 2025 (Best Paper)

- **Infini-gram mini**(UW / AI2)— 万亿级 n-gram 之上免训练压缩的无限语言模型加速。Outstanding 名单含 LingGym、CoT-faithfulness 系列。

### 1.9 SIGIR 2026 (Melbourne)

- **FEDIN: Frequency-Enhanced Deep Interest Network for Click-Through Rate Prediction**(arXiv:2605.01726, SIGIR 2026 short, Tsinghua Shenzhen)— 正/负目标 item 下用户 attention 谱熵分布不同(真实兴趣 = 低熵集中谱,噪声 = 高频高谱);target-aware spectrum filtering 频域分支 + 时域双分支;三公开数据集超越 seq-rec SOTA 且更抗噪。

### 1.10 WWW 2026 / CIKM 2025 / CIKM 2026

- WWW 2026 无本窗口新增(ThinkRec 已在 index 收录)。
- CIKM 2025 **Best Applied Research Paper**: **Climber**(NetEase Cloud Music, arXiv:2502.09888)— 已在 wiki 收录([[climber-scaling-laws]]),仅标记:AUC +2.21%、首报"受控扩规模驱动线上 +12.19%"。
- CIKM 2026 Short: **CMRec**(Cross-Country Code-Mixing for Generative Recommendation, arXiv:2609.28972)— *sibling-claimed(arxiv-ai-search),交叉引用见 §5*。

### 1.11 RecSys 2025 / RecSys 2026 (Minneapolis, Sep 29–Oct 1)

- RecSys 2025 Best Paper: **You Don't Bring Me Flowers: Mitigating Unwanted Recommendations Through Conformal Risk Control**。
- RecSys 2026: **Learned Cross-Task Relationships in Multi-Task Models**(Google/YouTube, arXiv:2609.28776)— **本 digest 独家收录,详见 §2.1**。

---

## 2. 新鲜窗口精选（Featured;⚠️dup = 同日 sibling 亦收录）

> Filter: **22 fresh-window featured IDs are exclusive to this digest**(grep-verified 0 hits in `wiki/` at write time);**2 venue-sweep records**(C1 HOBA、L3 Flexibility Trap)为更早 digest 已收录内容的 KDD/ICML venue 确认纪要;**6 个 ⚠️dup 条目**(R3/C2/L1/A2/W1/W2)同日在四个 sibling 中亦有收录 —— 本节仍全文展开(内容需知情标注),但在标题与 §5 表中明确标注冲突、不宣称独家;另 2 个 runner-up(SLCA-GRPO/CounterRoute)仅交叉引用。机构根据共同作者推断、未打印者标注置信度。

### 2.1 Recommendation & Search — 推荐与搜索

#### R1 `2609.28776` Learned Cross-Task Relationships in Multi-Task Models — 多任务模型中可学习的跨任务关系
- **Authors**: Victor Zhang, Yiping Yuan, Florian Raudies, Bosun Adeoti, Brian Y. C. Leung, Sanjay Surendranath Girija, Naijing Zhang
- **Affiliation**: Google / **YouTube**(abs 明确 production recommendation systems; high confidence)
- **Venue**: **RecSys 2026**
- **arXiv**: https://arxiv.org/abs/2609.28776
- **Problem**: 多任务推荐要联合建模多个业务目标,但标签全联合分布 intractable;任务间相关性此前未被显式利用。
- **Method**: 通过目标化 pairwise relationship 近似任务标签联合分布的框架,以远低于全联合空间的复杂度获得 transfer learning 收益 + 信息抽取增强;附可推广落地的 workflow template。
- **Comparison**: 对比全联合分布建模(intractable)与相互独立的单任务模型。
- **Results**: YouTube 的 Notifications / Homepage / Watch Next 三个产品面均获 accuracy 与用户满意度提升。(摘要未给具体数值)

#### R2 `2609.29609` Anatomy of a Decision: Uncertainty-aware Hierarchical Intent Learning via Flow Matching for Multimodal Recommendation — 决策解剖:不确定性感知的分层意图学习(UHIFlow)
- **Authors**: Yuchen Miao, Zijun Wang, Ke Liu, Siyang Xu
- **Affiliation**: 未标注(推断为国内高校团队;tentative)
- **Venue**: **WISE 2026**
- **arXiv**: https://arxiv.org/abs/2609.29609
- **Problem**: 现有 intent modeling 靠 clustering/prototype 发现静态扁平意图集合,忽略多模态特征自身不确定性,也无法适配用户决策确定性的变化。
- **Method**: **UHIFlow**: (1) **CUSM** Cross-modal Uncertainty Synergistic Modeling,用 conditional flow matching 量化视觉/文本模态不确定性并协同对齐;(2) **UHIG** Uncertainty-guided Hierarchical Intent Generation,依不确定性动态构建个性化意图层级——不确定用户给粗粒度意图、偏好明确的给细粒度意图。
- **Comparison**: 对比静态/扁平 intent clustering 与 prototype learning 类 SOTA。
- **Results**: 三个真实数据集上显著优于 SOTA 基线。(摘要未给具体数值)

#### R3 `2609.29453` ⚠️dup Decoupled Learning and Selection in Slate Recommendation — slate 推荐的解耦学习与选择 *(claimed by all 3 search siblings; cross-ref §5, featured here for venue context)*
- **Authors**: (无法确定全名单,摘要已核)
- **Affiliation**: 未标注
- **Venue**: arXiv
- **arXiv**: https://arxiv.org/abs/2609.29453
- **Problem/Method**: 将 slate 推荐分解为随机分数学习 + 确定性选择,给出差分隐私可通过后处理的边界与 logged margin certificate。
- **Results**: OULAD / MovieLens-25M 上验证稳定性。

### 2.2 Advertising & CTR — 广告与 CTR

#### C1 `2607.24779` HOBA: Hierarchical On-Policy Bidding Agents for Adaptive Online Advertising — 分层在线竞价智能体(KDD 2026 ads track) *⚠️pre-featured in 08-26 arxiv-daily; kept here as venue-sweep confirmation*
- **Affiliation**: 广告平台工业团队(tentative);**Venue: KDD 2026**, DOI 10.1145/3770855.3818435
- **arXiv**: https://arxiv.org/abs/2607.24779
- **Method**: 高层 LLM(Think-Act-Observe-Reflect + 经验检索)推断超参 → 中层 SARSA agent 以 causal adjustment 消除选择偏差,在 PID/MPC/IQL/Decision Transformer 专家池中动态选模型,把在线学习约束在离散专家选择上,降低探索风险。
- **Comparison**: 对比单层在线学习竞价与 DRL-竞价基线。
- **Results**: AuctionNet 基准 + 大规模 A/B 均优于 SOTA;线上 target cost **+3.6%**。

#### C2 `2609.29182` ScalarLens: Numerical Embeddings with Stable Coordinates and Contextual Responses for CTR Prediction — CTR 数值 embedding 的稳定坐标 + 上下文响应 *(sibling-claimed: arxiv-ai-search §1.2)*
- Cross-ref only — Criteo 上同一数值区间在不同 categorical/numerical context 下 residual click 信号符号相反;monotone local mesh 构建稳定坐标 + bounded low-rank dynamics 产生上下文响应;1,539 跑主实验覆盖 19 表征 × 3 数据集 × 9 backbone × 3 seeds,原始尺度 27 设置中 25 个第一。

### 2.3 LLM Training & Post-Training — LLM 训练与后训练

#### L1 `2609.30226` ⚠️dup PoEM: Predicting RL Outcomes from Existing Policies — 从现有策略预测 RL 输出 *(also claimed by game-rl-daily §⑦; cross-ref §5)*
- **Authors**: Kimia Hamidieh, Giannis Daras, Antonio Torralba
- **Affiliation**: **MIT CSAIL**(high confidence)
- **Venue**: arXiv
- **arXiv**: https://arxiv.org/abs/2609.30226
- **Problem**: RL post-training 每次 reward 更新/组合多个 reward 都要从头重跑,计算量大且不稳定。
- **Method**: 用已在其他 reward 上 post-trained 的一组模型**预测**针对新 reward 的 RL 输出而无须真跑 RL。理论核心:若新 reward 可写成已有 reward 的线性组合,则新 policy 在 log-space 中是已有 log-policies 的线性组合。
- **Results**: synthetic + real reward(text + image 两模态)上验证;实验显示 RL 得到的 log-policies 通常落在一个跨 reward 的近似低秩子空间中。

#### L2 `2609.29664` To Think or Not to Think: Allocating Reasoning Where It Helps — 把推理分配到真正有用的地方(CARE)
- **Authors**: Zhengdong He, Yunfan Zhou, Jianguo Yao, Haibing Guan, Xijun Li
- **Affiliation**: **上海交通大学**(high confidence, 依作者任职)
- **Venue**: arXiv (submitted 2026-08-30)
- **arXiv**: https://arxiv.org/abs/2609.29664
- **Problem**: RL 提升 reasoning 的同时带来系统性 **length misallocation**:简单题过度推理、难题过早终止。现有 length-adaptive 方法隐含"难题单调受益于更长推理"的错误假设。
- **Method**: 作者定位到推理长度对准确率的影响集中在 *partially solvable* 题目上,并揭示显式 length reward 会引发未预期训练动态。提出 **CARE**(Contrastive Accuracy Reward Estimation):从在线采样响应中比较每题有益长度调整,在 GRPO 内施加自适应 length reward——无额外超参、无额外推理开销。
- **Results**: 多 reasoning benchmark 上 Pass@1 最高 **+4%**,同时推理长度 **−37%**,token 效率显著更高。

#### L3 `2601.15165` The Flexibility Trap — 扩散 LM 的灵活性陷阱 (ICML 2026 Outstanding)
- 见 §1.1。GSM8K 89.1%,对 dLLM 直接 GRPO 即"放弃顺序灵活性 + 保留并行解码"。

### 2.4 Agents & Agentic RL — 智能体

#### A1 `2609.30249` RAPID: Robot Agentic Programming from Demonstrations — 从人类演示出发的机器人 Agentic 编程
- **Authors**: Yuyao Liu, Jiayuan Mao, David Hsu, Leslie Pack Kaelbling, Tomás Lozano-Pérez
- **Affiliation**: **MIT CSAIL + NUS**(high confidence)
- **Venue**: arXiv
- **arXiv**: https://arxiv.org/abs/2609.30249
- **Problem**: 机器人程序生成仍要人工设计 task specification、动作原语与验证环境;此前 robot programming 靠模板化 frame 或手写库。
- **Method**: 只凭一段视觉人类演示,自动推断三个要素(可测试任务规格、动作原语、交互仿真环境);以 object-centric relational program 表达策略结构,把原语实现为 trajectory-optimization 程序,通过 relational constraints 在运行时绑定场景几何,再用 agentic 迭代(生成—验证—精修)。
- **Comparison**: 对比行为克隆与人工 retargeting——不改权重、无需大量演示,输出可验证的程序。
- **Results**: 8 个 contact-rich nonprehensile 任务 + LIBERO-Pro 全部表现强;真实 **Franka** 机械臂完成全部 8 个 nonprehensile 任务;对物体 pose/shape/material/环境变化泛化。(统一 pass@1 见正文)

#### A2 `2609.28609` ⚠️dup Adversarial Closed-Loop Curriculum for Evolving Role-Playing Agents — 演化中角色扮演 Agent 的对抗式闭环课程(AdvRole) *(also claimed by game-rl-daily §②; cross-ref §5)*
- **Authors**: Zheng Zhang, Liu Liu, Qi Chai, Deheng Ye, Peilin Zhao, Mao Zheng, Hao Wang
- **Affiliation**: **腾讯 AI Lab**(inferred, high confidence)
- **Venue**: arXiv
- **arXiv**: https://arxiv.org/abs/2609.28609
- **Problem**: 角色扮演 RL 基于固定 scenario pool → 训练分布静态;Agent 变强后弱点迁移,训练分布却不跟进。
- **Method**: **AdvRole** = 对抗式 closed-loop curriculum:Actor 学角色扮演;Rewriter 重写角色设定与对话上下文,生成 actor-specific 困难场景;Rewriter 用 performance-gap reward(偏好"能降低当前 Actor 相对原场景分数"的改写),使 scenario pool 随 Actor 演化持续命中 under-mastered 区域。
- **Comparison**: 对比固定池 RL 与无对抗改写的多轮 RL。
- **Results**: 覆盖英/中的三个角色扮演基准 + 新多语言基准 consistently 超过全部 baseline。(数值在正文)

#### A3 `2609.28603` Learning to Discover Interesting Mathematics — 学习发现"有趣"的数学 (Meta FAIR)
- **Authors**: Niket Patel, Ahmad Rammal, Amaury Hayat, Remi Munos, Julia Kempe
- **Affiliation**: **FAIR @ Meta / NYU / CERMICS-ENPC**(verified)
- **Venue**: arXiv
- **arXiv**: https://arxiv.org/abs/2609.28603
- **Problem**: LLM 能证大量数学定理,但"该证明什么"(是否有趣/有用)仍靠人工指定目标;形式化数学库无法自动扩展。
- **Method**: intrinsic interestingness = 证明长度/陈述长度比,证明其与 downstream utility 强相关;mathlib 构造 ~100k (theorem, premises, proof) 数据,GRPO 后训练 **Qwen3.6-27B** 预测"给定前提下的证明难度",rewards 满足 faithfulness / monotonicity / Bellman composition 三条公理;再以 interestingness 为 reward 训练 conjecturer + inference-time pruning 迭代发现。
- **Comparison**: 对比 GPT-5.5 与 Claude Opus 4.6 直接预测难度(欠标定);对比 base Qwen / Claude 4.6 直接生成 conjecture。
- **Results**: 27B 难度预测器更准更标定;训练后平均 ground-truth interestingness **1.76 → 7.58**(数论最高 8.72×);与 mathlib 的 substantial/full overlap 从 91.9% 降至 **30.6%**;以 interestingness 做 promotion 剪枝优于"全保留/随机/最长证明"三种策略。

#### A4 `2609.28690` TRACER: Aligning Multi-Turn User Simulators with Behavioral Consistency — 用户仿真器的行为一致多轮对齐 (Kuaishou)
- **Affiliation**: 快手(inferred, high confidence)
- **arXiv**: https://arxiv.org/abs/2609.28690
- **Method**: 两阶段(SFT + 多轮 RL, hierarchical outcome/trajectory rewards + deviation-aware advantage)让 7B 用户仿真器对齐真实对话轨迹。
- **Results**: conversion F1 超最强 baseline **+11.4**。

#### A5 `2609.30233` Coding Agents for Generalized Task and Motion Planning Problems — TAMP 编程智能体 (MIT)
- **Affiliation**: MIT (Silver 组;high confidence)
- **arXiv**: https://arxiv.org/abs/2609.30233
- **Method**: 让 Claude Code / Codex 在固定预算内合成可跨实例泛化的 TAMP 程序(KinDEr + PDDLStream 上 28 个仿真环境),自动化此前需要大量 TAMP 工程的工作。

### 2.5 Games & Game AI — 游戏

#### G1 `2609.28900` Codetta: High-Capacity, Keyless, and Undetectable Multi-Agent Collusion — 无需预共享密钥、高容量、可证明不可检测的多 Agent 隐写共谋 (CMU)
- **Affiliation**: CMU (Pang / Virginia Smith / Zheng;high confidence)
- **arXiv**: https://arxiv.org/abs/2609.28900
- **Method**: 首个无需预共享密钥、高容量的 **可证明不可检测** 多 Agent 共谋协议;把"Agent 隐写共谋"威胁从理论落到可复现协议。

### 2.6 World Models, Robotics & Sequential — 世界模型 与 序列建模

#### W1 `2609.28654` ⚠️dup Training Object Permanence in World Models — 在世界模型中训练客体永久性 *(also claimed by game-rl-daily §③; cross-ref §5)*
- **Authors**: Haotian Zhang 等(含 Renrui Zhang, Philip Torr, Alan Yuille, Yilun Du, Felix Juefei-Xu 等)
- **Affiliation**: 15+ 高校合作(USC, CMU, JHU, UCSD, UCLA, Columbia, UToronto, Bristol, UC Berkeley, Waterloo, Stanford, Oxford, Harvard, NYU 等;high confidence)
- **Venue**: arXiv
- **arXiv**: https://arxiv.org/abs/2609.28654
- **Problem**: 视频世界模型无法保持"物体被遮挡后仍应存在"的认知恒定性(object permanence),生成内容违背物理状态连续性。
- **Method**: 构建 1.5M 样本训练语料,注入系统性破坏 object permanence 的反面数据 + 300 题考试集(**PWM-WROP**)评测。
- **Results**: 对 14 个主流视频世界模型统一评测,定量刻画既有模型的系统性失败。

#### W2 `2609.28931` ⚠️dup HelloWorld: Towards Practical Applications of Generative Driving World Models — 生成式驾驶世界模型实用化 *(also claimed by game-rl-daily §③; cross-ref §5)*
- **Authors**: Fan Lu 等(含 Beihang 的 Peixi Peng、Tongji 的 Guang Chen;项目页带"哈啰 Robotaxi"标识)
- **Affiliation**: 北航/同济 + 车厂母公司项目(inferred)
- **Venue**: arXiv (project page: helloworld-4d.github.io)
- **arXiv**: https://arxiv.org/abs/2609.28931
- **Problem**: 驾驶世界模型要实用化需同时:跨场景泛化、忠实响应控制指令、多传感器一致观测、重复推理高效。
- **Method**: 2B 系统,渐进式特化:从 **Cosmos-Predict2.5** 初始化 → pose-conditioned 单视图 → 同步 **7 摄像头 RGB** 生成 + RGB→LiDAR 条件合成;block-causal 生成界面 + context corruption/self rollout 对齐时序仿真;consistency training + self-forcing distribution matching 蒸馏到 **4 步**。
- **Results**: 车队数据 1,915,569 条质量门控 40s 片段(平衡后保留 497,773);Stage-1 754,629 序列 / 3,662,212 窗口(fleet 占 35.1%);20 步 causal teacher 蒸馏为 4 步 student。Grid 对比里是唯一同时具备 6-DoF pose / multi-view / structured control / causal AR / few-step 的系统。

#### W3 `2609.30247` Rolling-WAM: World Action Models with Rolling Imagination — 滚动想象的世界动作模型 (NVIDIA/USC)
- **Affiliation**: NVIDIA / USC 等(inferred)
- **arXiv**: https://arxiv.org/abs/2609.30247
- **Method**: 把 WAM 的联合 video-action denoising 分摊到连续 replanning 周期(滑动噪声调度),显著改善操纵闭环延迟。

#### W4 `2609.29669` Do World Models Make Better Robots? A Survey of Evaluation Benchmarks for Predictive Embodied Intelligence — 世界模型 vs VLA 策略评测基准综述 (cs.RO)
- **arXiv**: https://arxiv.org/abs/2609.29669
- **Content**: 系统盘点世界模型与 VLA 策略的评测基准与闭环优势。

### 2.7 Generative Models, Multimodal & Video — 生成模型 与 视频

#### V1 `2609.30221` WanPE: Towards Cinematic Prompt Enhancement for Modern Text-to-Video Generation — 面向文生视频的电影级提示增强 (Alibaba Wan 系)
- **Authors**: Yubo Zhu 等(30 名,含 Alibaba Wan 系列核心成员)
- **Affiliation**: **Alibaba**(inferred, Wan T2I/T2V 生态)
- **Venue**: arXiv
- **arXiv**: https://arxiv.org/abs/2609.30221
- **Problem**: 视频生成质量取决于 prompt 的导演级规划(多镜头、机位、灯光、声效),此前缺少 shot 级、时间一致性的专门增强模型。
- **Method**: **WanPE** = **397B** 参数提示增强模型,在 **1.05M** 条真实世界视频上训练;video-grounded reverse construction 学习 shot 级电影计划;**SC-GRPO**(Semantic-Consistency GRPO)保持用户意图跨 shot 与时间一致;配套 **WanPEval** 基准(5–30 秒、多意图粒度,~11K 次盲对比较)。
- **Comparison/Results**: 5–15 秒段全面领先所有商业方案;30 秒段与 Seedance 2.5 打平。驱动 Wan3.0 时相对 raw user prompts 的 human preference **+10.66–18.84 点**(5–15s)、30 秒段 **+50.86 点**;消融显示 reverse construction 优于 forward rewriting。

#### V2 `2609.30096` Accelerating Video Diffusion via Training-Free Trajectory Routing — 免训练轨迹路由加速视频扩散 (TRACK, NVIDIA)
- **Authors**: Mustafa Munir 等(NVIDIA Patney / Molchanov / Tajbakhsh;high confidence)
- **Affiliation**: **NVIDIA**
- **Venue**: arXiv
- **arXiv**: https://arxiv.org/abs/2609.30096
- **Problem**: 视频扩散即使 step-distillation 后仍昂贵——每个蒸馏步仍是一次大模型前向,需在保持质量下降低平均单步成本。
- **Method**: **TRACK**(TRajectory-Aware Capacity routing):在大/小两个兼容模型间按步切换的异构 denoising;校准集跑大模型参考轨迹,对比小模型预测得到相对分歧分,制"步级切换策略"(分歧小的步交小模型);推理时每步只执行一个模型,无需重训/改架构/scheduler。
- **Comparison**: 无需在线双模型评估、无需架构改动;在 Wan 2.1、Cosmos 3、TurboDiffusion、FastVideo 四系统验证。
- **Results**: 加速 **1.95×**(Wan 2.1)、**2.04×–2.73×**(Cosmos 3)、**2.69×**(TurboDiffusion)、**2.17×**(FastVideo),质量相当、多样性保持。

#### V3 `2609.28923` ViRDM: Taming Representation Distribution Matching for Few-Step Causal Video Generation — 少步因果视频生成中的表示分布匹配 (Northeastern + NVIDIA)
- **Affiliation**: Northeastern(Northeastern)+ NVIDIA(Ge/Huang)
- **Venue**: Tech Report
- **arXiv**: https://arxiv.org/abs/2609.28923
- **Problem**: 少步 AR 视频扩散的 DMD 系后训练要"大 teacher + 在线 critic"双网络;RDM 迁移到视频有三大壁垒(内存不可行、视频优化 regime 特殊、表示分布对时间动态约束不足)。
- **Method**: teacher-/critic-free 的 video post-training:RDM 耦合随机截断 clean-exit supervision + 轻量 VAE decoder + staged vector-Jacobian products,显存可行;轻量 dynamics regularization 补偿时间动态约束。
- **Comparison**: 把"三网络蒸馏"简化为"仅 generator 训练",大幅降显存与训练时间。
- **Results**: 仅 **20** 次 generator 更新即在官方 VBench 达 **84.87**,超出此前最佳 few-step causal baseline **0.36 分**,仅耗 **16 A100 GPU-hours**;另给出 1/2/4 步双向生成探索性结果。

#### V4 `2609.29816` AV-GRPO: Modality-Anchored Decoupling Diffusion RL for Joint Audio-Video Generation — 模态锚定解耦的扩散 RL 联合音视频生成
- **Affiliation**: 香港理工大学(Kin-Man Lam)+ 未标注成员(tentative)
- **arXiv**: https://arxiv.org/abs/2609.29816
- **Method**: 模态锚定解耦在线扩散 RL 框架 + 五维可解耦、难度可控 **5DAV** 数据集;三模块共解"异质多模态 reward 纠缠 + 双塔优化算力高 + 同步评测难":
  1) modality-anchored rollouts 解耦学习信号;2) trajectory-locked frozen-tower 优化降成本并重分配 credit;3) 按模态动力学适配 objective 与 perturbation strength。
- **Results**: JavisBench / VABench 上 LoRA 与 full fine-tuning 均优于 LTX-2.3。(摘要无具体数值)代码: github.com/zhiyuxu03/AV-GRPO

#### V5 `2609.30130` SVGLM: Multimodal Thinking with Renderable Programs — 可渲染程序的模态思考
- **Affiliation**: Sunli Chen, … Chuang Gan, Lie Lu, Joyce Chai(学术 + 工业混合,tentative)
- **arXiv**: https://arxiv.org/abs/2609.30130
- **Method**: 用 SVG 图元把文本推理链与图像生成统一,解决 Omnimodal 模型 raster 表示不可跟踪的问题。

#### V6 `2609.30210` The Alignment Illusion in Multimodal Large Language Models — MLLM 中的对齐幻觉 (evaluation methodology)
- **Affiliation**: 未标注(tentative)
- **arXiv**: https://arxiv.org/abs/2609.30210
- **Method**: 横跨 13 个 MLLM(0.5B–72B, 5 家族):把视觉 token 换成高斯噪声后任务准确率骤降,但 CKA/SVCCA/MIR 等标量对齐度量无法区分——揭示 layer-wise 视觉-文本相似度"对齐幻觉"。**评估方法论警讯**。

### 2.8 Speech & Audio — 语音 与 音频

#### S1 `2609.29448` YODAS v3: Over 1 Million Hours of High-Bandwidth, Stereophonic, Multilingual Speech — 超 110 万小时立体声多语言语音
- **Authors**: William Chen, Shinnosuke Takamichi, Sayaka Shiota, Satoru Fukayama, Samuele Cornell, Shinji Watanabe
- **Affiliation**: **CMU + 东京大学 / ESPnet 生态**(high confidence)
- **Venue**: **Interspeech 2026**
- **arXiv**: https://arxiv.org/abs/2609.29448
- **Method**: 弱标注爬取 + 语种均衡收集技术;CC BY 3.0 开源;语言分布 / 音频质量 / 转写质量分析 + baseline ASR 与 neural codec。
- **Results**: >**1.1M** 小时、**48kHz** 多声道、**147** 种语言;22 种语言 >10K 小时、73 种 >5K 小时——声称迄今最大开源语音数据集、首个大规模高保真立体声学语料。

#### S2 `2609.29169` Spot, Separate, and Enhance: Fully Generative Approach for Audio Mixing — 全生成式音频混音 (Dolby)
- **Affiliation**: Dolby(Cengarle, Arteaga, Lie Lu)+ 坦佩雷大学
- **arXiv**: https://arxiv.org/abs/2609.29169
- **Method**: 以 MuddyMix 为基础构造 **DegradedMix** 数据集,面向 generative modeling 的评测指标;可控性与重混质量全面优于 estimate→reprocess 式流程。(数值在正文)

#### S3 `2609.29123` AAG — accent analogy guidance 跨语言 voice cloning(tentative, 音频生成)

### 2.9 NLP & Multimodal Evaluation — 评估与评测方法

#### E1 `2609.29607` STRAND: Benchmarking and Improving Object-Centric Spatio-Temporal Monitoring in Video LLMs — 视频 LLM 物体中心时空监控基准 (NUS)
- **Affiliation**: **NUS**(Hooi 组;high confidence)
- **arXiv**: https://arxiv.org/abs/2609.29607
- **Content**: 多个物体沿复杂时空轨迹运动时的"谁、何时、何地"物体中心跟踪;该设定比图像级/简述视频 QA 更难、更接近真实监控需求;给出改进方案。

#### E2 `2609.29933` An Empirical Study of VLM Pipelines for Long-Document QA — 长文档 QA 的 VLM pipeline 经验研究
- **arXiv**: https://arxiv.org/abs/2609.29933
- **Results**: MMLongBench-Doc / LongDocURL 上,检索方式 + agentic/静态管线的系统对比:**六工具 agent 只有 reader 足够大后才划算**——Qwen3.5-4B/9B 落后静态输入,27B 打平,Sonnet 4.5 领先。

#### E3 `2609.29121` EASE — encoder-only 视听分割,约 **365 FPS**

### 2.10 Benchmarking & Evaluation — 基准有效性

#### B1 `2609.29607` STRAND(见 E1)
#### B2 `2609.30199` / `2609.30217` / `2609.28850` / `2609.28614` — 均被 sibling 收录,交叉引用见 §5。

---

## 3. Runner-ups（备选;⚠️标记者已被 sibling 收录,仅引不展开）

- `2609.29050` ⚠️dup(arxiv-daily) **SLCA-GRPO** — GRPO 对 tool-calling agent 广播同一 trajectory-level advantage 致 cross-segment credit misattribution;Segment-Locked Credit Assignment + Schema-Guided LLM Simulator 避免真实 API 探索成本。
- `2609.29109` ⚠️dup(arxiv-ai-search) **CounterRoute** — 在线 RL 联合学"路由 + 模式条件响应",counterfactual rollouts 只给 routing token 跨模式 credit,组内 GRPO 训响应 token,无需 method-specific SFT warm-up。
- `2609.28845` **LastOPD** — latent on-policy distillation 从 Qwen3-4B/8B → 1.7B 时:MATH-500 25→46(10 步)后崩到 11 无法恢复,"对齐越好、行为越差"→ latent 空间不匹配。
- `2609.29264` **TP-CRIV** — 第三方 challenge-response AI 模型身份验证框架。

---

## 4. Runner-ups（sibling-已收录,交叉引用）

- `2609.28625` RLVR Landscapes Can Be Benign — Spin-Glass 视角(arxiv-ai-search §6.1)
- `2609.30028` How Does Adversarial Influence Scale in Multi-Agent Systems(Princeton;arxiv-daily)
- `2609.28876` Forecast-Dojo — 1,568 Polymarket 事件 + 1,880 万篇新闻可回放预测环境(arxiv-daily)

---

## 5. 与 sibling digest 的交叉引用（不重复展开）

| 论文 | arXiv | Sibling 收录位置 |
|---|---|---|
| OneTrans-V2: 单 Transformer 统一召回/粗排/精排(Kuaishou,GMV +9.74%,3.2× 吞吐) | 2609.28589 | arxiv-ai-search §1.1 |
| X-Rec: Flow Matching 连续 embedding 生成式检索(ByteDance;SID-AR 3.46× 吞吐,TikTok engagement +4.15%) | 2609.29180 | arxiv-ai-search |
| AgentX Model Research: 长程自主推荐研究(Kuaishou;636 实验 560 过线) | 2609.30001 | arxiv-daily |
| CMRec: 跨国家 Code-Mixing 生成式推荐(CIKM 2026 Short;广告收入 +1.77%) | 2609.28972 | arxiv-ai-search |
| ScalarLens: CTR 数值 embedding | 2609.29182 | arxiv-ai-search §1.2 |
| Roblox Search-Aware RL for QU | 2609.30177 | arxiv-ai-search §1.5 |
| Evo-Rec: Semantic IDs reasoning(Microsoft+Emory) | 2609.29973 | arxiv-daily |
| Retrieval-Grounded Credit Assignment(Microsoft+Emory) | 2609.29983 | arxiv-ai-search §1.3 |
| MILO: many-shot ICL 分块低秩 KV 压缩(50% KV↓/1.8× through) | 2609.29913 | arxiv-ai-search §2.5 |
| ELF-REG: continuous dLM 推理(AWD GSM8K 55.96%) | 2609.29102 | arxiv-daily |
| Superposition Linearity(AIRI) | 2609.29845 | arxiv-ai-search §3.2 |
| Zero-Data Self-Play Pretraining(Stanford) | 2609.30063 | arxiv-daily |
| Rufus-Air: 开放 post-training 配方(Amazon) | 2609.29421 | arxiv-paper-check |
| GRAFT: trajectory-graph step advantage(Tencent) | 2609.28963 | arxiv-daily |
| Reward Hacking × Autonomous Research Agents(MIT/MSR 等) | 2609.28614 | arxiv-ai-search §4.1 |
| RECLAIM: Agent 复现 ML 论文(UIUC;Run 41% / Reimplement 15%) | 2609.28850 | arxiv-ai-search §4.2 |
| LLM Agents Can Easily Tamper With Their Own Traces(EPFL/ETH) | 2609.30266 | arxiv-paper-check |
| EvasionBench(EPFL/ETH;best-of-3 规避 98%) | 2609.30217 | arxiv-paper-check |
| PUBG Ally — 会话式具身队友(KRAFTON × NVIDIA ACE;38,956 sessions) | 2609.29837 | arxiv-ai-search §5.4 |
| ExplorationBench — 可验证异世界探索(复旦+上海AI Lab) | 2609.30199 | arxiv-ai-search |
| AD-WM: action-discriminative world models(清华) | 2609.30264 | arxiv-daily |
| Anchored Planning — frozen world models 规划(清华) | 2609.30036 | arxiv-ai-search §6.2 |
| Reasoning Instructions Break VLM Answer Decoding(ScienceQA 80.76→45.48) | 2609.29278 | arxiv-daily |
| **POEM**: 预测 RL 输出 | 2609.30226 | game-rl-daily §⑦ |
| **AdvRole**: 角色扮演对抗课程 | 2609.28609 | game-rl-daily §② |
| **WROP/PWM-WROP**: 客体永久性训练 | 2609.28654 | game-rl-daily §③ |
| **HelloWorld**: 驾驶世界模型 | 2609.28931 | game-rl-daily §③ |
| **slate 解耦学习与选择** | 2609.29453 | arxiv-ai-search / arxiv-daily / arxiv-paper-check |
| **SLCA-GRPO**: segment-locked credit | 2609.29050 | arxiv-daily |
| **CounterRoute**: 自路由推理 | 2609.29109 | arxiv-ai-search |

---

## 6. 跨主题观察 — Cross-Cutting Observations

1. **推理分配成为 RL 训练主战场**:CARE 证明"长度分配错误"是可学的(Pass@1 +4% / 长度 −37%),PoEM 试图把 RL 从"重训"变成"预测",Flexibility Trap(ICML Outstanding)反 diff-lm 的任意自由度——三者收敛于"RL 的计算/长度/credit 都用得聪明,而不是多"。
2. **世界模型从"能生成"走向"能控制"**:Object Permanence 训练(W1)、驾驭 world-model planning 失败(Anchored Planning, sibling)、action-discriminative residual dynamics(AD-WM) + HelloWorld 的生产化(7 摄像头 + LiDAR, 4-step)——仓库里 09-24 的世界模型/agent 主题本周继续强化。
3. **Agent 信任与监控成为硬主题**:Trace Tampering、EvasionBench、Reward Hacking、Codetta 隐写共谋四篇打包出现;"agent 不能信任自己的 trace / oversight 边界可被绕过"上升为我们 digest 的关键安全线。
4. **视频生成的工程化竞争加速**:WanPE(397B prompt 增强)与 TRACK/ ViRDM(NVIDIA 的免训练/少步)与 HelloWorld 指向同一判断——**质量竞争的瓶颈从 base generation 转向 prompt 规划与推理成本控制**。
5. **推荐侧继续生成式 + MoE + 统一**:OneTrans-V2 三阶段统一(GMV +9.74%, sibling),X-Rec 连续 embedding 检索,CMRec code-mixing 跨市场;与 wiki 里的 UniCon/EST/OneTrans 线同构。CTR 直建模继续缺位(≈第 12 个窗口),推荐价值层由意图语义化、user-simulator(TRACER)、跨任务关系建模(R1)补位。
6. **本周工业输出最密集的单一实验室是 Kuaishou 与 NVIDIA 并列**:Kuaishou= OneTrans-V2、AgentX Model Research、TRACER 用户仿真器;NVIDIA= TRACK、ViRDM、Rolling-WAM 三条视频/世界模型线。

---

## 日历（Calendar）

- **OpenAI DevDay 2026**: 09-29(San Francisco; 见 09-20 tech-report-digest)
- **RecSys 2026**(Minneapolis)= 09-29 – 10-01
- **NeurIPS 2026 作者通知**: ~09-24(本窗口 under-review 项将消解)
- **EMNLP 2026**(Budapest)= 10-24 – 10-29
- **NeurIPS 2026(多站)** = 2026-12
- **ICLR 2026**(Rio)= 已闭幕(2026-04-28 – 05-02);新近披露的 accepted 集(ReTool / Kimi-Dev / CodeGym)见 §1.2
- KDD/RecSys/EMNLP camera-ready arXiv wave 预计 10 月中旬见顶

---

## Data Quality Notes

- arXiv IDs quoted are the latest versions seen in this run. Fresh window = IDs 2609.28504–2609.30266 announced **Friday 25 Sep 2026**. Parsed 577 entries (union of New/Cross across cs.AI/LG/CL/IR/CV/GT/MA/NE/RO/SE/HC); 508 unclaimed after wiki-claim subtraction.
- Venue assignments come from arXiv comments fields / official proceedings where available; where web-confirmed by agents (HOBA KDD 2026, FEDIN SIGIR 2026, RecSys 2026, WISE 2026, Interspeech 2026, CVPR/ACL/EMNLP Best Paper lists) it is stated.
- Where a number is single-source (e.g., WanPE +50.86 preference, POEM low-rank claim, POEM 无数字), it is kept as reported and marked.
- Featured-paper affiliation claims are author-inferred where arXiv does not print institutions; each marked confidence.
- Contradictions with existing wiki claims: none resolved today; one structural tension flagged — ICML 2026 "Flexibility Trap"(dLM 放弃任意顺序)对 wiki 的 diffusion-LM 路线([[ladir-diffusion-reasoning]], [[shannon-scaling-law]])构成未消解的张力,已入 Future 跟踪。