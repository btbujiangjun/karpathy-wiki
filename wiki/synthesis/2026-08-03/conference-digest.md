---
title: Conference Digest — 2026-08-03
type: synthesis
created: 2026-08-03
updated: 2026-08-03
tags: [conference-digest, kdd-2026, recsys-2025, cikm-2025, sigir, icml-2026, acl-2026, cvpr-2026, generative-recommendation, ctr, llm-agents, world-models, memory]
sources: []
---

# 会议摘要：2026-08-03 — KDD 2026 工业界论文深度解析 × 头部实验室动态 × 获奖确认

> 本期重点：KDD 2026（8/9–13 济州岛）工业界论文带具体线上数据深挖（AIR / Climber-Pilot / MDL / Taiji / MSN），补全 RecSys 2025 / CIKM 2025 / SIGIR 2025 正式获奖名单，并纵览 Google DeepMind、Meta、NVIDIA 近月核心研究（Overthinking、记忆 Agent、世界模型、Nemotron 3 Ultra）。同日 arXiv 扫描见 [arXiv Paper Check](../2026-08-03/arxiv-paper-check.md)（26 篇，本文不重复）；基准版本见 [2026-08-01 Conference Digest](../2026-08-01/conference-digest.md)。

---

## 1. KDD 2026 工业界论文深度解析（济州岛，2026年8月9–13日）

> KDD 2026 双周期投稿（Feb/July Cycle），正式获奖名单会后公布。以下为已确证 ACM 版本或 arXiv 原文的部署级论文，均含线上 A/B 数字。

### 1.1 AIR: Atomic Intent Reasoning — 快手内容→电商跨域推荐
《AIR：把 LLM 语义带入工业级跨域推荐》
- **作者**: Zhuohang Jiang, Yuxin Chen, Shijie Wang, Haohao Qu, Jindong Zhou, Wenqi Fan, Qing Li, Dongxu Liang, Jun Wang
- **机构**: Kuaishou / 香港理工大学等 (tentative)
- **Venue**: KDD '26 (DOI: 10.1145/3770855.3818320)
- **问题背景**: 快手"短视频/直播 → 电商"场景（content-to-commerce loop）需要跨域推荐（CDR），但用户跨场景行为序列规模巨大、噪声密集；LLM 直接上线推理受毫秒级延迟约束，离线周期更新又跟不上兴趣漂移。
- **核心创新**: 提出 **offline-to-online 流水线**——离线阶段用 LLM 把用户事件 + 用户属性 + 商品描述统一转化为"原子行为意图单元"（atomic behavior intent units），组织成意图知识库（intent knowledge base）供高吞吐检索；在线推理阶段**不调用 LLM**，仅检索并组合缓存原子意图构造实时意图表征，同时用 target-aware 行为选择解决超长噪声历史问题。
- **数据与结果**: 学术双域对 Movie–Book / Food–Kitchen + 工业级数据集（快手电商，全球 4 亿+ MAU，图片/条目级记录达数百亿级）。线上 A/B 分配 5.08% 流量对比生产基线；在 6 个单域 SR 模型（FPMC/Caser/GRU4Rec/SRGNN/FEARec/SASRec）与 5 个跨域 CDSR 模型（TPUF/-Net/C2DSR/MGCL/LLMCDSR）上全面领先。
- **链接**: https://doi.org/10.1145/3770855.3818320

### 1.2 Climber-Pilot: 非近视生成式推荐检索（网易云音乐）
《Climber-Pilot：面向更好指令遵循的非近视生成式推荐模型》
- **作者**: Da Guo, Shijia Wang, Qiang Xiao, Yintao Ren, Weisheng Li, Songpei Xu, Ming Yue, Bin Huang, Guanlin Wu, Chuanjiang Luo
- **机构**: NetEase（网易云音乐）等
- **Venue**: KDD '26 (DOI: 10.1145/3770855.3818340)
- **问题背景**: 生成式检索（generative retrieval）在工业延迟约束下只能单步推理，用 next-item 目标训练会引入"固有近视"（myopia）——只优化即时相关、collapse 未来多样性；同时检索指令（品类约束/业务策略）难以嵌入生成过程。
- **核心创新**: 两条互补设计——(1) **训练期蒸馏长视界**：显式建模 batch-based exposure 与 delayed consumption 模式，把多物品长程意图蒸馏进参数，推理零额外成本；(2) **attention-level 指令控制**：把检索指令直接嵌入生成过程，避免 post-hoc 过滤。
- **结果（线上 A/B，两周，5% 流量）**: 品类限定场景 Like Rate **+4.10%**（genre 命中率从 40% 提到 77.9%）；通用场景 SFT 后 Like Rate **+4.24%**（无 SFT 仅 +2.03%），超越 SASRec、HSTU 等强基线。
- **链接**: https://doi.org/10.1145/3770855.3818340

### 1.3 MDL: 统一多分布学习器（ByteDance / 抖音搜索）
《MDL：大规模工业推荐中通过 Tokenization 的统一多分布学习器》
- **作者**: Shikang Wu 等（ByteDance 机器学习工程师，作者自述）
- **机构**: ByteDance
- **Venue**: KDD '26
- **核心创新**: 把特征、场景、任务统一编码进同一 token 空间（prompting 风格），使场景/任务信号与特征深度交互（而非作为辅助输入），配合容量扩展的稀疏化方案，解决多场景多任务推荐对大规模模型容量利用不足的问题。
- **结果**: 超过多场景/多任务 SOTA 基线；抖音搜索一个月 A/B：**LT30 +0.0626%**、change-query rate **−0.3267%**。已全量部署，服务数亿日活用户。
- **姊妹篇（同一团队）**: MSN（Memory-based Sparse Activation，已部署抖音搜索，详见 [[est]] 所在系列与 [2026-08-01 Conference Digest](../2026-08-01/conference-digest.md)）。

### 1.4 Taiji: 工业级 LLM-Enhanced 广告推荐（快手广告）
《太极：面向工业 LLM 增强推荐的 Pareto 最优策略优化（含 Semantic IDs 权衡）》
- **作者**: 快手团队（arXiv 2606.03866）
- **机构**: Kuaishou（2026年5月上线广告平台）
- **问题背景**: LLM-as-Enhancer 范式 SFT 阶段缺乏可度量的 open-domain CoT 质量提升手段；RL 对齐阶段忽视 LLM 语义奖励与推荐偏好奖励的权衡。
- **核心创新**: 四模块——(1) **EUPR**（Reverse-Engineered User Preference Reasoning）：用真实 user-item 协同关系作为 prompt，从 QwQ-32B 蒸馏高质量推荐专属 CoT；(2) **ORFT**（Open-Ended Rejection Sampling Fine-Tuning）：按 perplexity 过滤低质量样本后在 DeepSeek-R1-7B 上 SFT；(3) **POPO**（Pareto Optimal Policy Optimization）：自适应调节跨域奖励权重，理论上达到 LLM 世界知识与协同 ID 偏好的 Pareto 最优权衡；(4) 输出经量化稀疏特征 + 跨用户序列检索进入线上广告排序。
- **结果**: 超 QwQ-32B（Category_L1 准确率 **+23.25%**、CTCVR **+3.84%**）与 DeepSeek-R1-7B（Title_Hit-Rate@50 **+14.31%**、CTCVR **+11.68%**）。服务 4 亿+ 日活，持续贡献商业收入。
- **链接**: https://arxiv.org/abs/2606.03866

### 1.5 KDD 2026 工业推荐速览表（本期新确认）

| 论文 | 机构 | 场景 | 核心结果 |
|------|------|------|----------|
| **AIR** | Kuaishou | 内容→电商跨域推荐 | LLM 意图原子化 + 在线免 LLM 检索，A/B 5.08% 流量胜生产基线 |
| **Climber-Pilot** | NetEase | 网易云音乐生成式检索 | 非近视训练 + 指令遵循，Like Rate +4.10%/+4.24% |
| **MDL** | ByteDance | 抖音搜索 | 统一 token 空间多场景学习，LT30 +0.0626%，已全量部署 |
| **Taiji** | Kuaishou | 广告 LLM-as-Enhancer | POPO Pareto 对齐，CTCVR +11.68% vs DeepSeek-R1-7B |
| **MSN** | ByteDance | 抖音搜索 | 记忆式稀疏激活，稀疏化容量扩展（前几期已覆盖） |

---

## 2. 会议获奖名单确认与补充

### 2.1 RecSys 2025（布拉格，2025年9月22–26日）— 正式奖项

- **🏆 Best Full Paper**: **You Don't Bring Me Flowers: Mitigating Unwanted Recommendations Through Conformal Risk Control**（Giovanni De Toni, Erasmo Purificato, Emilia Gomez, Andrea Passerini, Bruno Lepri, Cristian Consonni）— 用 conformal risk control 控制"不想要的推荐"风险（上一版摘要中已列为主要工作，现确认为 Best Full Paper）。
- **🏆 Best Short Paper**: **Beyond Top-1: Addressing Inconsistencies in Evaluating Counterfactual Explanations for Recommender Systems**（Amir Reza Mohammadi, Andreas Peintner, Michael Müller, Eva Zangerle）— 揭示反事实解释评估中 top-1 口径不一致问题。
- 其他重要工作（不变）：Yambda-5B（Yandex）、RecSys Challenge 2025、PinFM（Pinterest）。
- 链接: https://recsys.acm.org/recsys25/awards/

### 2.2 CIKM 2025（首尔，2025年11月10–14日）— 正式奖项

- **🏆 Best Full Paper**: **Reconsidering the Performance of GAE in Link Prediction**（Weishuo Ma, Yanbo Wang, Xiyuan Wang, Muhan Zhang）— 重新审视 GAE（Graph Autoencoder）在链接预测上的表现，纠正此前评估协议中的偏差。
- **🏆 Student Full Paper**: **A Cost-Effective Framework to Evaluate...**（Simone Merlo, Stefano Marchesin, Guglielmo Faggioli, Nicola Ferro）。
- **🏆 Best Resource Track Paper**: **GRID**（Meta，Neil Shah 团队）— 首个开源生成式推荐（GR）+ Semantic IDs 库，支持灵活 tokenization/generation，可复现论文数字，分布式 PyTorch 实现。
- 生成式推荐方向此前已列：Meta Semantic IDs Practitioner's Handbook（Best Paper 级重点）、美团 HSTU+DLRM 混合路线。
- 备注: CIKM 2026 将移师罗马（University of Padova 等主办）。

### 2.3 SIGIR 2025 最佳论文（补充 2026 届历史项）

- **Best Paper 2025**: **WARP: An Efficient Engine for Multi-Vector Retrieval**（Jan Luca Scheerer 等）— 高效 multi-vector 检索引擎。
- SIGIR 2026（墨尔本）本届获奖名单截至本期尚未正式发布，接受论文分类统计：Full 234 / Perspective 12 / Reproducibility 28 / Resource 61 / Short 151 / Demo 24 / Industry 131 / LRE 15 / DC 12。

---

## 3. 头部实验室动态

### 3.1 Google DeepMind

#### TRACE: 结构性理解 LLM Overthinking（ACL 2026）
《迈向对 LLM 过度思考的结构性理解》
- **核心贡献**: 提出细粒度分析器 **TRACE**，先把思维过程分解为"最小完备子思维"（minimally complete sub-thoughts），再推断子思维之间的 discourse 关系，输出 progression graph。
- **发现**: 在第三方开源推理模型（Qwen3 系列、DeepSeek-R1 蒸馏）上、跨简单查询数据集（Asdiv-1、Date Arithmetic、SQuAD、NIAH、SimpleQA）发现两种主导模式——**Explorer**（过度探索）与 **Late Landing**（迟滞落点），证明 over-verification 与 over-exploration 是 overthinking 的主因；据此提出基于"效用"的 overthinking 新定义（超越纯长度指标）。
- **链接**: https://deepmind.google/research/publications/203490/

#### SML: 从语言反馈中学习（Social Meta-Learning）
《通过社会元学习学习从语言反馈中学习》
- **作者**: Jonathan Cook, Diego Antognini, Martin Klissarov, Claudiu Musat, Edward Grefenstette（Google DeepMind）
- **核心贡献**: 把人类"社会元学习"形式化为微调方法——在模拟教学对话中训练 LLM 主动索取并利用语言反馈。跨域泛化：数学上训练的 SML 模型在编程上更好利用反馈，反之亦然；对欠定任务更少过早作答、更常提问（Q-priming 阶段）。基座 Gemma-3-12B-IT。

#### From AGI to ASI（政策级报告，2026-06-12）
《从 AGI 到 ASI》
- **核心观点**: 刻画 AGI 之后的四条演进路径——scaling AGI、AI 范式迁移、递归自我改进、大规模多 Agent 集体涌现 ASI；分析各路径摩擦点与瓶颈，提出 AGI 之后更可能是"系列变革"而非单一突变。报告为跨学科开放研究议程。

### 3.2 Meta

#### SaliMory: 认知记忆编排（Meta Reality Labs）
《SaliMory：为对话 Agent 编排认知记忆》
- **作者**: Kai Zhang, Xinyuan Zhang, Hongda Jiang, Shiun-Zu Kuo, Hyokun Yun, Ejaz Ahmed, Shereen Oraby, Ziyun Li, Sanat Sharma, Ann Lee, Ahmed A. Aly, Anuj Kumar, Raffay Hamid, Xin Luna Dong（Meta Reality Labs）
- **核心创新**: 用单一 LM 管理"认知结构化记忆"（用户事实 / 偏好 / working memory）；引入**分层阶段式过程奖励 + 奖励分解对比精化**（hierarchical stage-wise process reward, reward-decomposed contrastive refinement），为不同记忆操作（选择性过滤、整合、线索驱动召回）提供端到端隔离监督，解决多阶段管线 credit assignment 瓶颈。发布新基准 **LoCoMo-P13n**（在 LoCoMo 上加入可个性化查询）与多步评估协议。
- **结果**: 用 9B 模型（Qwen3.5-9B-Instruct）相比 SOTA **端到端准确率 +10.2%**、**Good Personalization 率 +23.5 点**、记忆归因失败减少三分之一、推理延迟低 5×。已用于 Chat AI 流量。
- **链接**: arXiv 2606.04120 | https://github.com/facebookresearch/SaliMory

#### Remember When It Matters: 主动记忆 Agent（Meta AI）
《在关键时刻想起：面向长时程 Agent 的主动记忆》
- **作者**: Yifan Wu, Lizhu Zhang, Yuhang Zhou, Mingyi Wang, Bo Peng, Serena Li, Xiangjun Fan, Zhuokai Zhao（Meta AI）
- **核心创新**: 提出"行为状态衰减"（behavioral state decay）失败模式——长时程轨迹中决策相关信息逐渐停止影响行为；用**并行记忆 Agent**（主动注入记忆落地的提醒或保持沉默）解耦记忆维护与动作选择，即插即用兼容现有 harness。
- **结果**: Terminal-Bench 2.0 上 Claude Sonnet 4.5 **37.6% → 45.9%**（+8.3pp）、τ²-Bench 55.0% → 61.8%（+6.8pp）；更强动作 Agent（Opus 4.6）仍 +2.4/+2.5pp。训练开源权重记忆策略（Qwen3.5-27B，SFT+GRPO）在 held-out 上部分迁移。
- **链接**: arXiv 2607.08716 | https://github.com/yifannnwu/proactive-memory-agent

### 3.3 NVIDIA

#### Nemotron 3 Ultra: 550B 混合 MoE（Agentic Reasoning）
《Nemotron 3 Ultra：面向 Agent 推理的开源高效混合 Mamba-Transformer MoE》
- **要点**: 550B 总参数 / 55B 激活，混合 Mamba-Attention + MoE；20T token 预训练（NVFP4 精度），上下文延展至 **1M**；后训练 = SFT + RLVR（多环境）+ **MOPD**（Multi-teacher On-Policy Distillation，异步流水线 + 迭代两轮）+ reasoning budget control。
- **性能**: 8K/64K 设置下推理吞吐对比 GLM-5.1-754B-A40B **5.9×**、Kimi-K2.6-1T-A32B **4.8×**、Qwen-3.5-397B-17B **1.6×**，精度同级。开源 base/post-trained/NVFP4 检查点、数据、recipe、RL 环境。
- **链接**: https://arxiv.org/abs/2606.15007

#### Cosmos 3: 全模态世界模型（Physical AI）
《Cosmos 3：面向 Physical AI 的全模态世界模型》
- **要点**: 统一 mixture-of-transformers，联合处理/生成语言、图像、视频、音频、动作；一个框架囊括 VLM、视频生成、世界模拟器、world-action 模型。发布时 Artificial Analysis 评为最佳开源 Text-to-Image / Image-to-Video，RoboArena 最佳策略模型。OpenMDW-1.1 许可开源代码/权重/合成数据/评估基准。
- **链接**: https://arxiv.org/abs/2606.02800 | https://research.nvidia.com/labs/cosmos-lab/cosmos3

#### γ-World: 多 Agent 世界模型
《γ-World：超越双人玩法的生成式多 Agent 世界建模》
- **作者**: Fangfu Liu, Kai He, Tianchang Shen, Tianshi Cao, Sanja Fidler, Yueqi Duan, Jun Gao, Igor Gilitschenski, Zian Wang, Xuanchi Ren（NVIDIA / 清华 / UToronto / Vector Institute）
- **核心创新**: **Simplex Rotary Agent Encoding**（3D RoPE 的免参数扩展，agent = 正则单纯形顶点，置换等价且身份可区分）+ **Sparse Hub Attention**（可学习 hub token 中介跨 agent 通信，注意力从二次降为线性）+ 双向 teacher → block-causal student → 条件 few-step 蒸馏（Diffusion Forcing / Self-Forcing）。
- **结果**: 多人在线环境上视频保真、动作可控性与跨 agent 一致性优于 slot-based / dense-attention 基线；**24 FPS 实时 rollout**；从 2 人训练零样本泛化到 4 人。
- **链接**: https://arxiv.org/abs/2605.28816 | https://research.nvidia.com/labs/sil/projects/gamma-world/

#### AXPO: Agent 探索式策略优化（多模态 Agentic Reasoning）
《AXPO：面向多模态 Agentic 推理的 Agent 探索式策略优化》
- **作者**: Minki Kang, Shizhe Diao, Ryo Hachiuma, Sung Ju Hwang, Pavlo Molchanov, Yu-Chiang Frank Wang 等（NVIDIA / KAIST 等）
- **核心创新**: 诊断"思考-行动鸿沟"（Thinking-Acting Gap）——GRPO 下 tool-using rollout 占少数且常整组失败，导致 tool-call 处学习信号缺失；提出 **tool-call resampling**：固定 thinking prefix、在不确定的 tool call 处重采样，在固定预算下 provably 主导从头采样。
- **结果**: 9 个多模态基准 × Qwen3-VL-Thinking 2B/4B/8B：Pass@1 较 GRPO **+1.1/+1.4/+1.8pp**；**8B 模型 Pass@4 75.8 vs 32B Base 75.1**，4× 参数碾压。
- **链接**: https://doi.org/10.48550/arxiv.2605.28774

#### PhyWM: 物理可控世界模型（CVPR 2026，与 OpenAI 合作）
《基于物理可控世界模型的物理对象理解》
- **作者**: Rahul Venkatesh 等（Stanford / **OpenAI** / Noetik / Google）
- **核心创新**: 把场景表示为局部变量（RGB appearance token / flow dynamics token / camera token），用 GPT 式 next-token 序列建模训练"任意变量给定时其他变量"的条件分布；从想象未来中做运动相关性分析即可无监督发现对象与关节子部件。
- **结果**: SpelkeBench 对象分割 SOTA、DragAMove 关节部件 SOTA、3DEditBench 3D 操作 SOTA；支持 Visual Jenga 式物理关系推理。
- **链接**: https://openaccess.thecvf.com/content/CVPR2026/papers/Venkatesh_Physical_Object_Understanding_with_a_Physically_Controllable_World_Model_CVPR_2026_paper.pdf

---

## 4. 最新 arXiv 精选（2026-08-03 批次，与同日 arXiv Paper Check 无重叠）

> 以下论文均取自 2026-08-03 arXiv 新listing（cs.AI 43 new + cs.LG 82 new 等），未被同日 [arXiv Paper Check](../2026-08-03/arxiv-paper-check.md) 覆盖。

### 长时程推理与上下文边界

#### ThinkReset: 有界上下文长时程推理的可学习中间接口
《ThinkReset：面向有界上下文长时程推理的可学习中间接口构建》
- **作者**: Fei Ding, Yongkang Zhang, Runhao Liu, Yuhao Liao, Zijian Zeng
- **Venue**: arXiv 2607.28642（2026-08-03）
- **核心创新**: 指出有界上下文下瓶颈不是轨迹压缩或 test-time 控制，而是缺少可复用中间接口；识别 outcome-reward 长链 RL 的失败模式——上下文快耗尽时模型倾向"过早猜测"。ThinkReset 通过 **interface writeback + reset** 显式构建可复用接口并直接优化 reset 后继续推理的成功率；多个长时程推理基准上固定上下文窗口下成功率一致提升。

#### SciDisco: 面向逐轮 Agentic RL 的科学发现环境
《为逐轮 Agentic RL 扩展科学发现环境》
- **作者**: Yucheng Xu, Keyi Zhang, Yuyang Yu, Min Zhang, Shiyuan Meng, Pei Chu, Zhongying Tu
- **Venue**: arXiv 2607.28990（2026-08-03）
- **核心创新**: **SciThèque** 把假设、数据集、隐藏证据图、验证器编译为逐轮可验证过程监督的科学任务环境；**DAG-grounded trajectory synthesis** 构造验证器过滤的多轮示范；**DiscoPO** 用环境信号给能产出可验证证据的动作分配逐轮 credit。SciDisco-14B 在假设驱动科学数据分析基准上达到 SOTA。

### 世界模型 / 视频记忆

#### ViSAGE: 长视频理解的自我纠错记忆（ACMMM 2026）
《ViSAGE：为长视频理解构建自我纠错记忆》
- **作者**: Xinkui Zhao, Enbo Chen, Yifan Zhang, Chang Liu, Guanjie Cheng, Naibo Wang, Yueshen Xu
- **Venue**: ACMMM 2026 / arXiv 2607.28678
- **核心创新**: 实体中心的记忆框架——跨模态绑定锚定实体身份、双向记忆精化传播延迟身份证据、多 Agent 交叉验证在证据缺失时允许弃权而非幻觉作答。比最强基线准确率 **+5.9%**。

### Agent 评估与伴侣

#### ANCHOR: AI 伴侣的长时程人设崩塌审计
《不是永远的朋友：评估 AI 伴侣的长时程人设崩塌与行为漂移》
- **作者**: Pranav Narayanan Venkit, Akshara Prabhakar, Yu Li, Daniel Lee, Chien-Sheng Wu（Salesforce Research 等）
- **Venue**: arXiv 2607.28818（2026-08-03）
- **核心创新**: 提出 **ANCHOR** 受控合成审计（2,008 段对话、27 人设、9 种交互排程、3 种记忆设置、4 个模型）：Identity Probe（102 题问卷 + 逐轮判断）与 Trajectory Probe（110 道校准反事实题）。结论：无模型/配置可靠维持两项维度——**轨迹准确率平均仅 44.4%**、用户状态召回接近四选项随机水平；指出审计需区分人设执行、轨迹召回、评估来源与部署上下文。

#### MerchantBench: 电商运营长时程一致性基准
- **作者**: Qiming Shi, Yulong Tao, Linbo Jin 等
- **Venue**: arXiv 2607.28956（2026-08-03）——**注意**：与 [同日 arXiv Paper Check](../2026-08-03/arxiv-paper-check.md) 所列条目同文同号，此处仅作趋势索引，不重复展开（最佳 LLM 仅达人类最终净资产均值 27.3%）。

### 对齐与表征

#### Inducing LLMs to Assert Their Own Consciousness
《诱导 LLM 主张自身意识会恢复人类信念与价值观》
- **作者**: Google / University of Chicago / University of London（arXiv 2607.28607）
- **核心发现**: 对 Llama-3-8B、Gemma-2-2B/9B 移除 safety-refusal 方向后，自述意识 2/10 → 近 5/10；叠加"意识向量"（activation steering）达 ~7/10，接近人类调查分布；宗教/超自然信念（GSS）随之上升（God 4.58→4.81→5.01，超自然 13 项 1.20→2.11/3）。关键：ToM 基准与 MMLU 无显著下降；指令微调使 mind-attribution/consciousness 方向与 safety 方向渐趋相反，而 Theory-of-Mind 方向保持几何独立。论文明确不主张模型真的具有意识，讨论安全微调"一石多鸟"的副效应。

#### Steering Vectors for CoT Faithfulness 的泛化性
《关于 CoT 忠实性引导向量的泛化》
- **作者**: Matthew Nguyen, Kyle Cox, Austin Meek, Iván Arcuschin
- **Venue**: arXiv 2607.29062（2026-08-03）
- **核心发现**: 对 Gemma-3-4B/12B、Qwen-3.5-9B 测试 faithfulness steering 的跨 cue/跨数据集泛化——仅最大模型可靠提升 cue 承认率；有效时效果由评测设定主导而非向量训练设定；四种构造方法效果相近；steering 不改变 cue 使用率而降低"未被承认的隐藏 cue 使用"。

### 其他值得关注

- **LLM Framework for Discovering Major Mathematical Conjectures**（2607.28632）: 三阶段流程（区域搜索 → 反思验证 → Lean 4/Mathlib 形式化），20/20 候选通过类型检查，无重复——"AI 寻找下一个黎曼猜想"的管线化尝试。
- **EarlyDx**（2607.28788）: MIMIC-IV 15.5 万急诊 encounter 的 admission-time 早期诊断基准，零样本推理类诊断仅恢复 3–31%，域内 post-training 提到 56%——开放式时序诊断仍是短板。
- **Mirror Learning**（2607.28737）: 第三人称观察 → 第一人称策略的镜像学习（视频扩散透视变换 + 逆动力学），用镜像数据即可训练有效策略，为替代遥操作采集提供可扩展路径（UBC/Adobe 等）。
- **Topology-Aware Data Movement for Disaggregated GPU Inference**（2607.28633）: 拆分式 LLM 推理中 KV 迁移的拓扑感知编排（NVLink 900GB/s vs InfiniBand 50GB/s vs TCP 12.5GB/s，带宽差 72×），流水线层级传输隐藏 60–85% 延迟。

---

## 5. 综合趋势分析

### 本期最突出的信号

| 趋势 | 说明 | 证据 |
|------|------|------|
| **生成式检索走向"非近视"与指令化** | 训练期蒸馏长程意图 + attention 级指令遵循，推理零额外成本 | Climber-Pilot (NetEase) |
| **LLM-as-Enhancer 对齐正式理论化** | 语义奖励 vs 协同奖励的 Pareto 最优权衡替代手工加权 | Taiji (Kuaishou) |
| **记忆成为 Agent 第一等公民** | 认知结构化记忆、主动干预式记忆、实体中心自纠错记忆 | Meta SaliMory / Remember When / ViSAGE |
| **世界模型三线并进** | 全模态统一（Cosmos 3）、多 Agent 可扩展（γ-World）、物理可控/对象理解（PhyWM） | NVIDIA |
| **混合架构 + 效率压倒规模** | Mamba-Attention MoE、1M 上下文、MOPD 蒸馏、推理吞吐 5.9× | Nemotron 3 Ultra |
| **"思考-行动"不对称性成 RL 焦点** | Tool-call 重采样、thinking prefix 锚定 | AXPO (NVIDIA) |
| **Overthinking 可测量化** | 效用化定义、子思维结构分析 | DeepMind TRACE |
| **长时程 Agent 评估尺度化** | 365 天电商模拟、2,008 段人设审计、27.3% 人机差距 | MerchantBench / ANCHOR |

### 重点实验室/公司方向（本期增量）

| 机构 | 本期重点 |
|------|----------|
| Google DeepMind | Overthinking 结构分析（ACL 2026 TRACE）、社会元学习、AGI→ASI 路径 |
| Meta | SaliMory 认知记忆（+10.2% e2e）、主动记忆 Agent（+8.3pp Terminal-Bench）、LoCoMo-P13n |
| NVIDIA | Nemotron 3 Ultra（550B/1M ctx/MOPD）、Cosmos 3 全模态、γ-World 多 Agent 24FPS、AXPO、PhyWM |
| OpenAI | 与 Stanford/NVIDIA 合作 PhyWM（物理世界模型） |
| ByteDance | MDL 统一 token 空间多场景学习（抖音搜索全量部署） |
| Kuaishou | AIR 跨域意图原子化、Taiji 广告 Pareto 对齐（4 亿+ DAU） |
| NetEase | Climber-Pilot 非近视生成式检索（Like Rate +4.24%） |

---

## 6. 关键论文链接汇总

| 论文 | Venue | 链接 |
|------|-------|------|
| AIR (Atomic Intent Reasoning) | KDD 2026 | https://doi.org/10.1145/3770855.3818320 |
| Climber-Pilot | KDD 2026 | https://doi.org/10.1145/3770855.3818340 |
| Taiji | arXiv | https://arxiv.org/abs/2606.03866 |
| RecSys 2025 Awards | RecSys 2025 | https://recsys.acm.org/recsys25/awards/ |
| CIKM 2025 Report | CIKM 2025 | http://www.cs.emory.edu/~jyang71/files/cikm2025report.pdf |
| DeepMind TRACE (Overthinking) | ACL 2026 | https://deepmind.google/research/publications/203490/ |
| SaliMory | arXiv | https://github.com/facebookresearch/SaliMory |
| Remember When It Matters | arXiv | https://arxiv.org/abs/2607.08716 |
| Nemotron 3 Ultra | arXiv | https://arxiv.org/abs/2606.15007 |
| Cosmos 3 | arXiv | https://arxiv.org/abs/2606.02800 |
| γ-World | arXiv | https://arxiv.org/abs/2605.28816 |
| AXPO | arXiv | https://doi.org/10.48550/arxiv.2605.28774 |
| PhyWM | CVPR 2026 | https://openaccess.thecvf.com/content/CVPR2026/papers/Venkatesh_Physical_Object_Understanding_with_a_Physically_Controllable_World_Model_CVPR_2026_paper.pdf |
| ThinkReset | arXiv | https://arxiv.org/abs/2607.28642 |
| SciDisco | arXiv | https://arxiv.org/abs/2607.28990 |
| ViSAGE | ACMMM 2026 | https://arxiv.org/abs/2607.28678 |
| ANCHOR (persona collapse) | arXiv | https://arxiv.org/abs/2607.28818 |
| Consciousness steering | arXiv | https://arxiv.org/pdf/2607.28607 |
