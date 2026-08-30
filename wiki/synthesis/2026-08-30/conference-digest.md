---
title: "Conference & arXiv Daily Digest — 2026-08-30"
type: synthesis
created: 2026-08-30
updated: 2026-08-30
sources: []
tags: [conference-digest, icml-2026, iclr-2026, aaai-2026, neurips-2025, cvpr-2026, kdd-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2026, recsys-2026, recommendation, llm, agents, ctr, advertising, generative-models, sequential-modeling, games, code-execution, multimodal, world-models, benchmarks, daily-digest]
---

# Conference & arXiv Daily Digest — 2026-08-30

> Comprehensive survey of recent papers from top ML/AI conferences (2025–2026 cycle) and latest arXiv preprints (late-August 2026 wave, IDs ~2608.27xxx–2608.29xxx). Organized by venue and category. Focus on papers from top labs: Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, Netflix, NVIDIA, Anthropic, Apple, Amazon.

---

## 🏭 概述 Overview

本期收录 40+ 篇最新论文，按专题组织：**LLM 后训练与 RLVR**、**Agent 系统**、**推荐 / 广告 / CTR / 序列建模**、**生成模型与多模态**、**游戏与世界模型**、**代码执行**、**基准评测**。

热门主题：
1. **RLVR（可验证奖励强化学习）** 持续深化 —— 从探索崩溃（weak-model guidance）到跨域能力融合（fusion paradigms）；TTPO 打开"无标签"后训练。
2. **Harnessed Agentic RL / Agent 基础设施** —— Agent Lightning（微软）、Mixture of Roles 单模型多心智、WikiSkill 持久技能库。
3. **生成式推荐（Generative Recommendation）工业落地全面开花** —— Tencent（UniVA/OneRanker）、Kuaishou（GR4AD）、Baidu（GRAB）远多于纯学术。
4. **广告拍卖走向 token 级 / 生成式** —— LAMA Token-Level 拍卖机制。
5. **世界模型与交互式 AG-PLAY** —— ReWorld 长程记忆、Twin 测试时数字孪生、PlayWorld 评测、WorldMind NPC 行为解耦。
6. **代码执行与偏好优化** —— AgentExecutor（ASE'26）、Step-KTOder（EMNLP'26 Findings）函数级执行反馈。

---

## 🧠 LLM 后训练、RLVR 与 Scaling（LLM Post-training, RLVR & Scaling）

### 1. Test-Time Policy Optimization (TTPO)
- **中文标题**: 测试时策略优化（TTPO）
- **作者**: Aozhe Wang, Zhengxi Lu, Jianze Wang, Shangke Lv, Ying Liu, Weiming Lu, Jun Xiao, Yueting Zhuang, Hua Yang, Qianglong Chen, Yongliang Shen
- **机构**: 浙江大学（inferred）
- **Venue**: arXiv preprint
- **arXiv**: [2608.27448](https://arxiv.org/abs/2608.27448)
- **摘要与创新**: 无需标签的测试时训练（TTT）。观察拒绝采样伪标签的错误不对称：与伪标签不一致的 rollout 几乎总是错的。设计非对称目标——一致 rollout 用 On-Policy Self-Distillation (OPSD)，不一致 rollout 用 Grouped RL 惩罚，加上 token 级选择，使更新在频繁伪标签错误下稳健落桩。majority-vote 路由在模型变强时提供更紧自监督。
- **实验结果**: 无标签即与有监督 OPSD 在 5 个竞赛级 benchmark 持平；Qwen3-1.7B TTT 38.0%→45.2%；无 thinking 模式 +25.2% 至 +36.4%；跨任务泛化强。
- **对比**: 相对 vanilla OPSD / 伪标签监督，打开"无标签"场景且不牺牲正确性。

### 2. Boosting LLM Exploration via Weak-Model Guidance in RLVR
- **中文标题**: 通过弱模型引导提升 RLVR 中的 LLM 探索
- **作者**: Xingyu Shen, Huishuai Zhang, Peng Li, Yinchun Wang, Dongyan Zhao
- **机构**: 中科院计算所 / 北京大学（inferred）
- **Venue**: arXiv preprint
- **arXiv**: [2608.27420](https://arxiv.org/abs/2608.27420)
- **摘要与创新**: RLVR 常导致策略熵崩塌（entropy collapse），收窄推理覆盖、降低 pass@k。提出训练时强制目标模型基于更小更弱模型生成的部分推理轨迹作答，用"陌生前缀"破坏过度自信、促发不同推理路径；无需额外 SFT、复杂奖励或 prompt。
- **实验结果**: 多个数学 benchmark 稳定优于 vanilla RLVR；性能增益随 k 增大扩大；明显缓解熵崩塌。
- **对比**: 引入跨模型非参数扰动这一被忽视的探索维度。

### 3. Consolidating RLVR Capabilities Across Domains: A Deep Dive into Fusion Paradigms
- **中文标题**: 跨领域 RLVR 能力整合：融合范式深度剖析
- **作者**: Siye Wu, Kai Yang, Yuchen Cai, Xin Xu, Peng-Yuan Wang, Jiaxuan Wang, Jiashun Liu, Jiafei Lyu, Yangkun Chen, Saiyong Yang, Yanghua Xiao
- **机构**: 复旦大学等（inferred）
- **Venue**: arXiv preprint
- **arXiv**: [2608.27409](https://arxiv.org/abs/2608.27409)
- **摘要与创新**: 系统比较三种领域专家 RLVR 能力融合范式：**Merge**（合并专家 task vector）、**Mix RL**（混合数据训练）、**MOPD**（多教师 on-policy 蒸馏）。给出实用选型指南。
- **实验结果**: 平均性能差 ≤1.4 分，但单 benchmark 可差 8.6 分；域间差异与 task-vector 几何中的跨域关系相关。
- **对比**: 首次在共享专家与数据下进行统一受控跨规模比较。指南：已有专家选 Merge，需统一模型选 Mix RL，保域内增益选 MOPD。

### 4. Knowing When Not to Reuse: Conditional Experience Transfer in Autonomous LLM Post-Training
- **中文标题**: 知道何时不复用：自主 LLM 后训练的条件式经验迁移
- **作者**: Tingyun Li, Wenfeng Feng, Weiqing Li, Abudukelimu Wuerkaixi, Guohua Liu, Yuewei Zhang
- **机构**: 中国高校/工业界（inferred）
- **Venue**: arXiv preprint
- **arXiv**: [2608.26730](https://arxiv.org/abs/2608.26730)
- **摘要与创新**: 面向自主后训练提出"条件经验迁移"——父模型被后续训练改变后，过去更新证据不再必然适用。**BCIT**（Boundary-Calibrated Intervention Transfer）把观测影响绑定到来源上下文、检查适用条件、否决硬冲突、必要时用有界训练试验获取当前证据。
- **实验结果**: 4B 模型上跨 finance reasoning / text-to-SQL / function calling；BCIT 授权更少有害更新，等预算下获得更高最终模型质量。
- **对比**: 相对"历史成功=无条件许可"，显著降低计算浪费与训练轨迹退化。

### 5. Puro-2B: Poor Lab's Qwen2-1.5B Trained on RTX 5090 within $5090
- **中文标题**: Puro-2B：单张 RTX 5090 上、$5,090 预算内的低门槛预训练
- **作者**: Kairong Luo, Jiarui Cui, Yaorui Yin, Shengqi Chen, Yiming Yang, Linxiang Gao, Yanmohan Wang, Mingzhe Zhang, Kaiyue Wen, Kaifeng Lyu, Wenguang Chen
- **机构**: 清华大学（THU-PacMan）
- **Venue**: arXiv preprint
- **arXiv**: [2608.27370](https://arxiv.org/abs/2608.27370)
- **摘要与创新**: 面向消费级硬件的开源预训练食谱：FP8、单张消费级 RTX 5090 从零训练 Puro-2B。结合硬件选择、低精度训练、hyperball 优化、curriculum model averaging、数据配方；推导 **Puro Cost Scaling Law** 关联训练成本与平均性能。
- **实验结果**: 最佳模型在 <$6.9K 成本下接近 Qwen2.5-1.5B；Cost Scaling Law 表明 ~$4.4K 可达 Qwen2-1.5B 水平。对比 Llama-3.2-3B（>$1.5M）、SmolLM3-3B（>$700K），成本降 2–3 个数量级。
- **对比**: 大幅降低开源预训练门槛，首次提供数据课程影响下游的可控端到端研究。

---

## 🤖 Agent 系统与 Agentic RL（Agent Systems & Agentic RL）

### 6. Agent Lightning v1.0: Towards Harnessed Agentic RL
- **中文标题**: Agent Lightning v1.0：迈向"受约束"的智能体强化学习
- **作者**: Zhiyuan He, Yuqing Yang 等
- **机构**: 微软（Microsoft）
- **Venue**: arXiv preprint
- **arXiv**: [2608.17528](https://arxiv.org/abs/2608.17528)
- **摘要与创新**: 提出 **Harnessed Agentic RL** 范式——现代 agent 运行在 agent harness（管理工具、执行环境、上下文、控制流）中。现有 RL 框架对 coding agent 支持不足。提供完整数据清洗管线与可复现训练脚本，含 reward-hacking 防护，显式区分 harness 层。
- **实验结果**: 仅 ~6K 训练样本与适度算力，RL 将 Qwen3.5-9B 在 SWE-bench Verified 从 41.8% 提升到 56.4%（+14.6pp）。
- **对比**: 相对传统单 ReAct agent 无 harness，支持 multi-agent/subagent/handoff，在搜索、指令遵循、编码三类 agent 上验证。

### 7. One Model, Many Minds: Unlocking Multi-Agent Synergy via Mixture of Roles (MoRe)
- **中文标题**: 单模型多心智：通过"角色混合"实现多智能体协同
- **作者**: Zhichen Zeng, Huiyuan Chen, Jingru Cheng, Juan Zha, Ming Liu, Ying Chen, Xiyuan Yang, Chaosheng Dong, Haiyang Zhang, Hanghang Tong
- **机构**: 阿里/学术合作（inferred；Hanghang Tong 为 UIUC）
- **Venue**: arXiv preprint
- **arXiv**: [2608.27338](https://arxiv.org/abs/2608.27338)
- **摘要与创新**: 针对 MAS 多轮交互导致上下文/推理成本膨胀的问题，用单个 steer vector 编码多种角色。学习多样化角色 steering vector 码本，query-aware router 动态融合成综合 steering vector，对冻结 backbone 做单轮 steering。三阶段 SFT curriculum + GRPO。
- **实验结果**: reasoning 与 personality benchmark 平均比单 agent 基线高 2.2%，达到与 MAS 持平并 token 成本降 20×。
- **对比**: 相对单 agent 固定人设（无法适配多样 query）与多 agent 多轮高成本，在单 agent 单轮内实现多视角专业化。

### 8. WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution
- **中文标题**: WikiSkill：将智能体经验编入持久知识库以实现技能进化
- **作者**: Liyan Tang, Cyrus Rashtchian, Chun-Sung Ferng, Andrew Tomkins, Da-Cheng Juan, Tu Vu
- **机构**: Google
- **Venue**: arXiv preprint
- **arXiv**: [2608.27454](https://arxiv.org/abs/2608.27454)
- **摘要与创新**: 让智能体技能与一个持久知识库（wiki）共同进化，把原始执行经验、累积知识、可执行技能分离，持续整理经验供技能更新复用。
- **实验结果**: 多样 benchmark 一致优于 SOTA 技能进化方法与多数无技能基线；技能进化与模型规模互补——大模型从进化技能获益更多，小模型配技能可超过明显更大的无技能模型；技能可跨模型/跨家族迁移。
- **对比**: 相对把洞见散落在优化历史中，系统性积累与精炼智能体经验。

### 9. The Interaction Tax: When Communication Erases Diversity in Multi-Agent Teams
- **中文标题**: 交互税：当通信抹掉多智能体团队的多样性
- **作者**: Summer Eunhyung Ann, Haokun Liu, Chenhao Tan
- **机构**: 芝加哥大学
- **Venue**: ICML 2026 (PMLR 306)
- **arXiv**: [2608.23541](https://arxiv.org/abs/2608.23541)
- **摘要与创新**: 不同模型族找到结构不同的解，但当 agent 互相阅读完整输出时提案会在 1 轮内趋同，抹掉驱动多模型价值的多样性。匹配预算下，完整信息交互是弱默认项；独立提案生成可避免趋同。
- **实验结果**: 11 个 verifier-scored 优化任务上验证；完整解交互使 agent 贴近首个看到的解；critique 仅在违规规则易被 LLM 发现和修复时有用。
- **对比**: 多智能体性能更多取决于交换的信息而非 agent 数量。

### 10. GRAIN: Bridging Name and Narrative Shifts in Real-World Graph Reasoning
- **中文标题**: GRAIN：通过不变性奖励弥合真实世界图推理的命名与叙事漂移
- **作者**: Zike Yuan, Han Zhang, Jianzhi Yan, Le Liu, Cai Ke, Huozhi Zhou, Jian Xie, Jiran Yin, Yukun Cao, Yue Yu, Hui Wang, Ming Liu, Bing Qin
- **机构**: 哈尔滨工业大学等（inferred）
- **Venue**: arXiv preprint
- **arXiv**: [2608.27142](https://arxiv.org/abs/2608.27142)
- **摘要与创新**: 用 **Structure Invariance Reward** 的 RL 优化单 agent 图推理框架，模型推理作为语义解析 + 工具执行管线，通过校验抽取中间图与 ground-truth 拓扑，迫使学习稳健的文本→结构映射而非记忆语言伪影；避免多 agent 高延迟。
- **实验结果**: 比多智能体基线准确率高 16.45% 且延迟低 ~24%；将 SFT 模型的 OOD gap 从 15.77% 减半至 7.80%。
- **对比**: 单 agent + invariance reward 在精度与延迟双优；相对 SFT 显著降低 OOD 泛化 gap。

---

## ⚡ 模型效率：MoE、KV 缓存与推理（Efficiency: MoE, KV Cache & Inference）

### 11. CritICL: Inference-Time Weak-to-Strong Generalization from Small LLM Failure Modes
- **中文标题**: CritICL：利用小模型失败模式的测试时"弱到强"泛化
- **作者**: Yufan Wu, Yinghui He, Zhengyi Hu, Lang Wei, Ruichen Li, Qifan Yang, Ting Zhu 等
- **机构**: 中国高校（inferred）
- **Venue**: arXiv preprint
- **arXiv**: [2608.27455](https://arxiv.org/abs/2608.27455)
- **摘要与创新**: 关键洞见：同一模型族的失败模式在不同规模间存在结构模式。把弱模型导出的失败模式作为引导源，通过基于批判的 in-context example 注入推理。两变体：**CritICL-dynamic**（自适应预测输入特定失败模式并检索批判）、**CritICL-static**（全局失败模式档案）。
- **实验结果**: 一致优于标准 ICL，达到与测试时缩放方法相当或更优性能，同时显著减少生成次数与 token 成本（无需 repeated generation 或外部 verifier）。
- **对比**: 相对 repeated sampling / external verification 类测试时缩放方法更高效。

### 12. TwinKV: A Composable Repair Pass for KV Cache Eviction
- **中文标题**: TwinKV：基于成对键冗余的可组合 KV 缓存驱逐修复
- **作者**: Hong Chen, Yudong Zeng, Yongwei Huang, Zuhao Ouyang, Junyan Zhang, Xuming Hu
- **机构**: 中国高校/机构（inferred）
- **Venue**: arXiv preprint
- **arXiv**: [2608.27128](https://arxiv.org/abs/2608.27128)
- **摘要与创新**: 用受控 leave-one-out 探针发现 attention 大小与 token 对答案的因果贡献无关（Spearman ρ=-0.004），挑战主流驱逐方法前提。提出无训练、无 attention 的冗余信号——检测某 token 的 key 是否有近重复副本；作为可组合修复通道修复"孤儿"（已驱逐无存活副本）与"冗余供体"（保留但信息被复制）。
- **实验结果**: 与 4 种驱逐策略在 LongBench/LooGLE/RULER/MMLU-Pro、压缩率 {0.3,0.5,0.7} 组合；Qwen3-4B 多数配置提升，RULER 上 Llama-3.2-1B 全部评测单元改善。

### 13. InnerExpert: MoE Blocks Contain Strong Hallucination Detection Signals
- **中文标题**: InnerExpert：专家混合块包含强幻觉检测信号
- **作者**: Joao Fonseca, Rodrigo Rodrigues, Paolo Romano
- **机构**: INESC-ID / 里斯本高等理工学院（IST）
- **Venue**: arXiv preprint
- **arXiv**: [2608.17687](https://arxiv.org/abs/2608.17687)
- **摘要与创新**: 首个利用 MoE 特有信号（router entropy、expert disagreement、expert usage patterns）做逐 token 幻觉检测。将路由级 + 标准 transformer 信号合成特征向量，由轻量检测器分类，可连续更新。
- **实验结果**: 5 数据集、2 MoE 架构上优于现有方法，答案级 AUROC 最高 0.91、token 级 0.76，仅需一次前向。
- **对比**: 相对答案/句子级方法支持逐 token 细粒度定位，利用稀疏路由信号。

### 14. StickyMoE: Training MoE for Memory-Efficient Inference
- **中文标题**: StickyMoE：为内存高效推理训练的 MoE（粘性路由）
- **作者**: Ali Kayyam (BrainChip Inc.)
- **机构**: BrainChip Inc.
- **Venue**: arXiv preprint
- **arXiv**: [2607.08780](https://arxiv.org/abs/2607.08780)（六月投稿，效率方向相关工作）
- **摘要与创新**: MoE 相邻 token 频繁切换 expert 导致存储/内存持续换权重。提出可微 routing consistency loss 惩罚相邻 token 间 abrupt expert 切换，鼓励 router 在语义连贯片段内保持同一 expert；仅加一个超参 λ。
- **实验结果**: expert 切换率最多降 59%；中型模型困惑度还改善；cache miss 最多降 3.92×，在质量-局部性前沿 Pareto 支配后处理微调。
- **对比**: 相对系统级缓存启发式/后处理 router 微调，从根因入手，易用于现有架构。

---

## 📊 推荐系统（Recommendation Systems）

### 15. NMRL: Native Multimodal Representation Learning for CTR (Taobao/Alibaba)
- **中文标题**: 电商场景下点击率预测的原生多模态表示学习
- **作者**: Jiawei Feng, Sishuo Chen, Zhangming Chan, Xiang-Rong Sheng, Han Zhu 等（USTC + Alibaba）
- **机构**: 中国科学技术大学 + 阿里巴巴（淘宝展示广告）
- **Venue**: **CIKM 2026**（第 35 届 ACM CIKM，2026-11-07~11 罗马）；arXiv **2608.24091**
- **arXiv**: [2608.24091](https://arxiv.org/abs/2608.24091)
- **摘要与创新**: 发现**端到端联合训练多模态 encoder + CTR 模型会失败**（甚至退化），因原始 CTR 行为由多模态语义与非多模态因素共同驱动→监督模糊。提出 **Mine-Then-Train (NMRL)**：训练标注模型从 CTR 数据挖掘多模态可解释三元组，再在其上微调 SCL encoder，隔离模糊 CTR 监督。
- **实验结果**: 线上 A/B（淘宝展示广告）**CTR +1.5%、RPM +0.5%**；离线（8.4 亿用户、8800 万 item、19 亿样本）AUC/GAUC 优于两阶段与 E2EM；E2EM 实际 GAUC 下降 0.17pp。
- **对比**: 优于两阶段 SCL（CIKM 2024）与 plain E2EM；疑点消除 E2EM 的退化。

### 16. TSPORec: Token Selection via Preference Optimization for LLM Sequential Rec
- **中文标题**: 基于偏好优化的 LLM 序列推荐 Token 选择
- **作者**: Wenqiao Zhu, Chao Xu, Haipang Wu, Ji Liu
- **Venue**: arXiv preprint
- **arXiv**: [2608.09605](https://arxiv.org/pdf/2608.09605)
- **摘要与创新**: LLM-based SR 处理完整 item 文本太贵，现有方法截断首 token 丢信息。TSPORec 用冻结 LLM 训练策略头 + 可微代理奖励选择信息丰富 token chunk，再在精炼输入上重训。Qwen3-Embedding-0.6B / TinyLlama-1.1B backbone。
- **实验结果**: Amazon Books Recall@K 最多 +29.29%、NDCG@K 最多 +31.25%（均值 +29.43%）优于 SASRec；Pixel 最多 +19.63% R@K、+18.24% N@K；效率最多 -63.4%。
- **对比**: 相对截断方法与 truncation 基线显著提升且更便宜。*(preprint)*

### 17. OMEGA: Collaborative Memory Augmentation for Generative Recommendation (KDD'26)
- **中文标题**: 生成式推荐的协同记忆增强
- **作者**: Kuaishou/Tencent 等（inferred）
- **Venue**: **KDD 2026**（2026-08-09~13 济州岛），DOI 10.1145/3770855.3818179
- **arXiv**: [2608.01315](https://arxiv.org/html/2608.01315)
- **摘要与创新**: GR 通常只建模个体序列。**OMEGA**：潜在上下文压缩（可学习 query token 蒸馏用户序列→紧凑记忆），target-aware 检索（序列 + 目标相似度），gated cross-attention 整合检索到的协同记忆与局部上下文。兼容 SASRec/HSTU 等现有 GR。
- **实验结果**: 多个真实数据集上一致优于现有先进 GR 模型。

### 18. GALLM: Graph-Aware LLM for Sequential Recommendation
- **中文标题**: 让协同信号发挥价值：面向序列推荐的图感知 LLM
- **Venue**: arXiv preprint
- **arXiv**: [2608.12184](https://arxiv.org/html/2608.12184)
- **摘要与创新**: 通过 token 级协同图（Text-Text / Item-Text / Item-Item 从全局 item 共现）将全局协同结构注入 LLM attention，编码为轻量可学习 attention bias；无外部图 encoder、不改 LLM 结构。
- **实验结果**: 4 benchmark 上平均 **HR@5 +9.76%、NDCG@5 +7.62%** 优于最强基线（LLaRA/CoLLM/A-LLMRec/CoRA）；Item-Text attention alignment +54.2%/+10.0%。

### 19. DTE: Decoupled Temporal Encoding for Generative Recommendation (CIKM'26)
- **中文标题**: 生成式推荐中解耦的时间编码
- **Venue**: **CIKM 2026**（接受）
- **arXiv**: [2608.16274](https://arxiv.org/abs/2608.16274)
- **摘要与创新**: 位置编码只捕获 item 顺序，丢失时间戳/时间效应（recency、餐时峰、工作日-周末、促销爆点）。**DTE** 两模块：个性化宏时间模块（时间原语注入 item embedding）+ 时间门控微顺序模块（仅当交互时间密集时施加相对序偏置）。参数高效、易部署。

### 20. GOD: Enhancing Generalization via Deep Grafting for Sequential Rec (CIKM'26)
- **中文标题**: 通过深度嫁接提升序列推荐泛化性
- **Venue**: **CIKM 2026**，DOI 10.1145/3799682.3841117
- **arXiv**: [2608.16073](https://arxiv.org/html/2608.16073)
- **摘要与创新**: 组件级 KD：将学生 embedding 表/encoder 嫁接到冻结 teacher 获得组件级反馈，加 graft-aware contrastive；推理仅学生、零额外成本。
- **实验结果**: 3 个真实数据集最多 **+13.92%** 优于 SOTA；短/噪声/小序列场景增益最大（KD 困境区）。

---

## 🎯 广告与 CTR 预测、排名（Advertising, CTR Prediction & Ranking）

### 21. GR4AD: Generative Recommendation for Large-Scale Advertising (Kuaishou)
- **中文标题**: 大规模广告的生成式推荐
- **作者**: Ben Xue, Dan Liu, Lixiang Wang, Peng Wang, Pengfei Zhang 等
- **机构**: 快手（Kuaishou Technology）
- **Venue**: arXiv preprint
- **arXiv**: [2602.22732](https://arxiv.org/abs/2602.22732)
- **摘要与创新**: 生产级生成式推荐器，tokenization/learning/serving 协同设计：**UA-SID**（统一广告语义 ID，微调 MLLM embedding + MGMR RQ-Kmeans 量化减碰撞）、**LazyAR**（懒惰自回归 decoder，6/9 层共享近翻倍 QPS）、**VSL**（value-aware 监督学习）+ **RSPO**（排序引导 list-wise softmax 偏好优化，对齐 NDCG/eCPM）、**Dynamic Beam Serving**。
- **实验结果**: 线上 A/B 广告收入最多 **+4.2%** vs DLRM；中小广告主投放 +17.5%、CVR +10.17%、低活跃用户 CVR +7.28%；<100ms 延迟、每 L20 500+ QPS；全量服务 4 亿+ 用户。
- **对比**: 相对传统 DLRM 栈全面领先，是生成式广告工业落地的标杆。

### 22. MARCO: Click-Intent Decomposition for Calibrated Ads Conversion Prediction (Meta)
- **中文标题**: 基于点击意图分解的广告转化预测校准
- **机构**: Meta Platforms（广告平台）
- **Venue**: arXiv preprint；arXiv 2608.10562
- **arXiv**: [2608.10562](https://arxiv.org/html/2608.10562)
- **摘要与创新**: "并非所有点击都平等"——同一广告不同点击类型转化率差 **4×**；单一 CVR 模型混淆它们→系统偏差被完美聚合校准掩盖。**MARCO**：把转化率分解为 per-intent CTR/CVR head（用点击 UI 类型作自由标签），在预测意图分布下组合。证明分解从不会提升总体风险，给出 Oracle upper bound NE +2.268%。
- **实验结果**: Meta K=2 意图粒度部署，per-intent 校准 → ~100%；**每次点击转化 +2.80%**（[+2.50%,+3.10%]）、累计 top line +0.98%。CTR 容量 1×→5× 使路由效率 2.38%→4.06%。
- **对比**: 相对单 CVR 模型消除被校准掩盖的系统偏差，显著提升转化。

### 23. LAMA: Token-Level Advertising (Latent Advertiser Mixture Auction)
- **中文标题**: Token 级广告：潜在广告主混合拍卖机制
- **作者**: Hanbing Liu, Bowei Zhang, Changyuan Yu, Yinyu Ye, Qi Qi
- **Venue**: arXiv preprint（2026-08-26）
- **arXiv**: [2608.27382](https://arxiv.org/html/2608.27382)
- **摘要与创新**: 生成原生广告：广告主报告局部 continuation value 诱导广告主特定 next-token 策略，平台通过潜在混合解码并更新贝叶斯分配后验。证明 **Markov DSIC + IR** 与近最优 KL 正则福利。学习式实现从学习局部优势 + 根值在线重建报告。
- **实验结果**: 真实商业搜索 query 划分上最佳平台福利 (0.5205)、收入 (0.8305)、广告主价值 (0.8568)、用户质量 (66.52)；收入明显胜过 allocate-after baseline 且保持用户响应质量。
- **对比**: 机制设计/理论 + 模拟新范式（非工业系统）。

### 24. CRRN: Cascading Relevance-Driven Recommendation for CTR (Alibaba/Tmall)
- **中文标题**: 触发引入式推荐场景下级联相关性的 CTR 预测网络
- **机构**: 阿里巴巴（天猫）工业 + 公开数据
- **Venue**: arXiv preprint
- **arXiv**: [2608.22973](https://arxiv.org/html/2608.22973)
- **摘要与创新**: TIR 场景——用户点击 trigger item 表达即时兴趣，再看相关目标。**CRRN**：Trigger-Target Interaction 层 + Cascading Interest Fusion（预测 trigger 意图 + 级联 attention + 余弦相似度平衡即时/个性化兴趣）+ Category-assisted Pairwise Loss。
- **实验结果**: 线上 A/B 天猫（4/10-17）pCTR 最多 **+3.87%**；单模块 TTI 层 +0.54%；CRRN > DEI2N > DIHN/DIAN，均超 Wide&Deep/DIN。

### 25. GRAB: LLM-Inspired Sequence-First CTR Paradigm (Baidu)
- **中文标题**: 受 LLM 启发的序列优先点击率预测范式
- **机构**: 百度（商业广告/信息流）
- **Venue**: arXiv preprint
- **arXiv**: [2602.01865](https://arxiv.org/html/2602.01865)
- **摘要与创新**: 端到端生成式 CTR 框架，整合 **CamA**（Causal Action-aware Multi-channel Attention）于事件级行为 token，统一 DLRM 稀疏特征与 GR 序列建模；AUC 随序列增长单调 ~线性。
- **实验结果**: 线上 A/B（百度信息流广告 10% 流量 ~1 月）**CTR +3.49%、CPM +3.05%**；离线 +0.19% vs 最佳 GR baseline（DIN/SIM/TWIN/HSTU/LONGER）、线上 AUC +~2bp；推理成本与 DLRM 相当。

### 26. IDProxy: Cold-Start CTR with Multimodal LLMs (Xiaohongshu)
- **中文标题**: 小红书基于多模态 LLM 的冷启动 CTR 预测
- **机构**: 小红书（Explore Feed：内容+展示广告）
- **Venue**: arXiv preprint
- **arXiv**: [2603.01590](https://arxiv.org/html/2603.01590)
- **摘要与创新**: MLLM 生成 item 冷启动 proxy embedding，粗（对齐 ID 空间）→细（与 CTR ranker 端到端精修，轻量多粒度 adaptor），复用 ranker 序列/特征结构。
- **实验结果**: 线上 AUC 全局 +0.12–0.15%、**新笔记 +0.23–0.32%**（约 2× 强，印证冷启动收益）；Content Feed 与 Display Ads 指标 1% 显著性。服务数亿日活。

### 27. GOAL: Generative Optimization for Incentivized Advertising with Global Constraints (Kuaishou/KDD'26)
- **中文标题**: 全局约束下激励广告的生成式优化
- **作者**: Gege Chen, Ning Luo, Hao Jiang, Da Li（快手）、Fan Zhou（电子科大）等
- **机构**: 快手 + 电子科技大学
- **Venue**: **KDD 2026**，DOI 10.1145/3770855.3818423
- **arXiv**: [2608.04421](https://arxiv.org/html/2608.04421)
- **摘要与创新**: 激励分配视为条件序列生成 **GOAL**：分层因果状态 encoder（局部 + 长程动态）；**SCPO**（Safe Constrained Policy Optimization）用梯度的一系列 ROI 约束训练单一生成策略（Lagrangian multiplier embedding + constraint-aware MoE 路由），推理时不重训自适应。
- **实验结果**: 改善长期收入与留存，同时显著降低 ROI 违规率（RVR）vs DT/CDT/IQL/CAL/TREBI（大规模工业数据 + 合成疲劳感知环境）。

### 28. UniVA: Unified Value Alignment for Generative Recommendation in Online Advertising (Tencent)
- **中文标题**: 腾讯在线广告中生成式推荐的价值统一对齐
- **机构**: 腾讯（微信视频号广告团队）
- **Venue**: arXiv preprint
- **arXiv**: [2605.05803](https://arxiv.org/abs/2605.05803)
- **摘要与创新**: 生成式推荐（SID 基）高生成似然 ≠ 高广告效用。**UniVA** 全 SID 管线对齐商业价值：Commercial SID tokenization（商业属性 + bid 注入）、Generation-as-Ranking decoder（生成分数 + token 级价值估计融合）、Value-aware 约束 serving（个性化 trie 限制有效 SID 路径）。用 PPO + action-value 回归（非 GRPO）。
- **实验结果**: 离线 **HR@100 +37.04%** vs 最强 GR baseline；公开 benchmark +8.4% HR、+7.8% NDCG；线上 A/B（20% 流量）**GMV +1.5%**；SID 路径内 bid 离散度降低约 1 个数量级。

### 29. OneRanker: Unified Generation and Ranking with One Model (Tencent)
- **中文标题**: OneRanker：工业广告推荐中生成与排序的统一模型
- **机构**: 腾讯（微信视频号广告）
- **Venue**: arXiv preprint；arXiv 2603.02999v3
- **arXiv**: [2603.02999v3](https://arxiv.org/abs/2603.02999v3)
- **摘要与创新**: 端到端生成式广告三大挑战：interest-vs-value 对齐、target-agnostic 生成、生成/排序脱节。加入 (1) value-aware 多任务解耦（task-token 序列 + 因果 mask）；(2) coarse-to-fine target awareness（Fake Item Tokens + 排序 decoder）；(3) 输入输出双侧一致性（KV pass-through + Distribution Consistency loss）。联合 `L = αL_MTP + βL_rank + γL_DC`。
- **实验结果**: 微信视频号广告全量部署：线上 A/B **GMV-Normal +1.34%、Costs +0.72%**。

### 30. EST: Towards Efficient Scaling Laws in CTR Prediction (Alibaba/Taobao)
- **中文标题**: 面向点击率预测的高效 Scaling Law 统一建模
- **作者**: Mingyang Liu, Yong Bai, Zhangming Chan, Sishuo Chen, Xiang-Rong Sheng, Han Zhu 等
- **机构**: 阿里巴巴（淘宝展示广告）
- **Venue**: arXiv preprint；arXiv 2602.10811
- **arXiv**: [2602.10811](https://arxiv.org/pdf/2602.10811)
- **摘要与创新**: 识别 CTR vs LLM 不对称（非行为特征 N 与行为序列 B 的信息密度不对称、模态特定先验）。**EST**：Lightweight Cross-Attention (LCA) 剪冗余自交互；Content Sparse Attention (CSA) 用内容相似度选高信号行为。显示稳定 **power-law scaling**（ΔGAUC ∝ compute ∝ capacity，深度比宽度更陡）。
- **实验结果**: 淘宝"猜你喜欢"+"买后"部署：猜 CTR +1.22%、RPM +3.27%；买后 CTR +2.01%、RPM +2.66%。

---

## 🔄 检索与嵌入（Retrieval & Embedding）

### 31. OneShot: Index-in-Ranking with Neural Scoring (Meta/Instagram)
- **中文标题**: OneShot：基于神经评分的索引内排名大规模检索
- **作者**: Shuyao Li, Xufeng Cai, Xue Zou, Yiming Ma, Huiting Lu, Wujie Yan, Zhichen Zhao 等
- **机构**: Meta Platforms（Instagram）
- **Venue**: arXiv preprint；arXiv 2607.27475v2
- **arXiv**: [2607.27475v2](https://arxiv.org/html/2607.27475)
- **摘要与创新**: 解决索引-排名错位：学习与排名目标完全对齐的 item one-hot 编码层级（**Engagement IDs / EIDs**，in-model index、boosting 式层），将检索交互扩展到点积瓶颈之上。
- **实验结果**: 1% 工作点 recall +20%（0.4128 vs 0.3414 k-means baseline）；2 层达到 ANN 级 recall 且少排 90% item（10× 效率）；线上 **+0.04% sessions、+0.14% watch time、+61.6% 检索源贡献率**，Instagram 全球短视频全量部署。EIDs (0.4308) vs SIDs (0.1354) recall。
- **对比**: 相对 SID 与 k-means HNSW baseline，EID 对齐排序目标带来 recall/效率双重胜利。

### 32. EGR: Embedding-Native Generative Retrieval (Snap)
- **中文标题**: EGR：共享 LLM 的嵌入原生生成式检索
- **机构**: Snap（Snap DPA / ads）
- **Venue**: arXiv preprint；arXiv 2607.23038
- **arXiv**: [2607.23038](https://arxiv.org/abs/2607.23038)
- **摘要与创新**: 移除 prior GR 的 SID 量化/grounding 与独立 item/query encoder 分离：单共享 LLM 在同一空间产出 item embedding（元数据）与 user-query embedding（交互历史），用 item-pair + history-to-target 对比目标联合训练，服务用标准 ANN。
- **实验结果**: 优于 Amazon Reviews 已发布 baseline；Snap DPA 数据单调扩展、冷启动强、受益多模态；线上 A/B **CVR +2.91%**。*(preprint)*

---

## 🎨 生成模型与多模态（Generative Models & Multimodal）

### 33. Magnitude-Direction Decoupling for Fast Video Generation (MDD)
- **中文标题**: 流匹配视频生成中的幅度-方向解耦加速
- **作者**: Haonan Xu, Feiyang Chen, Songkui Chen, Hongpeng Pan, Zhefeng Wang, Xinyu Duan, Baoxing Huai, Yang Yang
- **机构**: 南京理工大学 + 华为
- **Venue**: arXiv preprint（2026-08-18 投稿）
- **arXiv**: [2608.17695](https://arxiv.org/abs/2608.17695v1)
- **摘要与创新**: 实证发现轻量小模型稳定捕捉大模型的 **magnitude**，残差复用/缓存提供可靠 **direction** 引导。提出 **MDD**：用"方向校准"轻量模型替代大步数重模型，对误差增长自适应重校准；结合 CFG 幅度复用降本；训练-free 即插即用。
- **实验结果**: Wan2.1 上最多 **2.95×** 加速、EasyAnimateV5.1 上 **1.90×**；保真 (Wan2.1: LPIPS 0.178, PSNR 22.72, SSIM 0.748)。
- **对比**: 相对 SRDiffusion（方向偏差输出）与 TeaCache（不变残差复用），幅度感知 + 方向校准获更高复用率与保真。

### 34. Stream Forcing: Unified Training Trajectory for Streaming Video Generation
- **中文标题**: Stream Forcing：统一训练轨迹的稳健流式视频生成
- **作者**: Yueting Zhu, Yuehao Song, Kaicheng Zhang, Bao Tang, Shaoyu Chen, Qian Zhang, Wenyu Liu, Xinggang Wang
- **机构**: 华中科技大学 + Anyverse Dynamics + 地平线
- **Venue**: arXiv preprint（2026-08-11 投稿）
- **arXiv**: [2608.10439](https://arxiv.org/abs/2608.10439)
- **摘要与创新**: 解决流式视频扩散 **train-inference mismatch**。将逐帧噪声级采样重建为"帧索引随机过程"，构建从独立采样（如 Diffusion Forcing）到渐进采样（如 rolling diffusion）的连续训练轨迹；joint calibration + Gaussian Copula 时序相关采样。面向 world modeling / 自动驾驶流式推理。
- **实验结果**: UCF-101 FVD **36.6%** 改进、Taichi-HD 4.7%；零样本长程外推（128 帧）UCF-101 27.9%、Taichi-HD 10.9%；nuScenes 自动驾驶同时改进 FID 与 FVD。
- **对比**: 相对独立采样（覆盖广但推理不一致）与渐进采样（推理一致但覆盖受限），统一课程实现平衡。

### 35. Towards Physics of Multimodal Pretraining (Meta FAIR)
- **中文标题**: 多模态预训练的物理：知识流动、模态协同、早期统一与配方
- **作者**: Junlin Han, Shengbang Tong, David Fan, Minghao Chen, Philip Torr, Filippos Kokkinos, Mike Lewis
- **机构**: Meta FAIR + Reality Labs + 牛津大学
- **Venue**: arXiv preprint（2026-08-05 投稿）
- **arXiv**: [2608.05000](https://arxiv.org/abs/2608.05000)
- **摘要与创新**: 受控实验揭示统一多模态预训练四大发现：(i) **Knowledge Flow**——语言是"万能助推器"，视觉理解是生成有力先验，但生成方向几乎不反向迁移；(ii) **Synergy vs Competition**——数据/任务复杂度决定协同还是竞争，共享 attention + 模态专属 FFN 促协同；(iii) **Early Unification**——早期联合训练优于晚期对齐，发现"vision laziness"；(iv) **Recipes**——仅 **5% 计算预算**即达强生成性能。
- **实验结果**: 13.5B MoE 模型、**2T tokens** 单变量受控缩放验证；生成数据高度数据高效，可按极大不对称比例分配算力给语言+理解。
- **对比**: 相对 late-fusion（Qwen3-VL 等）与 retrofit unified models，bottom-up early-fusion + 不对称数据混合为最优路径。

### 36. ANCHOR: Rectifying Modality Asynchrony in Multilingual MLLMs
- **中文标题**: 修复多语言 MLLM 中的模态异步
- **作者**: Yihang Du, Juhao Liang, Zhengzhao Lai, Siyu Li, Yan Hu
- **机构**: 香港中文大学（深圳）+ 深圳 Loop Area Institute + 国家健康数据研究院（深圳）
- **Venue**: arXiv preprint（2026-08-15 投稿）
- **arXiv**: [2608.15085](https://arxiv.org/abs/2608.15085v1)
- **摘要与创新**: 机制解释多语言 MLLM 非英语视觉推理退化：**Ghost Anchor 现象**——早期层语言表征收敛到英语语义流形，而视觉语义化未成熟。**ANCHOR** 用 **Proactive Visual Anchoring (PVA)**：以外部视觉基础模型（SigLIP-SO400M/14）为语义监督，对早期层 visual tokens 施加负余弦锚定损失，只微调 projector 与前 L_early 层。
- **实验结果**: 提升早期翻译阶段视觉因果影响（baseline LLaVA-1.5 ΔR_ET 近 0，ANCHOR 正向显著）；xMMMU/MaXM/CVQA 在 fine-tuned 与 zero-shot 下一致超过标准 baseline。
- **对比**: 相对数据驱动方案与输出层/全局对齐（mBLIP），直接在对齐窗口施层级视觉-语义同步。

---

## 🎮 游戏与世界模型（Games, World Models & Game Agents）

### 37. ReWorld: An Interactive World Model with Long-Horizon Memory
- **中文标题**: ReWorld：具有长程记忆的交互式世界模型
- **作者**: Zhifei Chen, Luozhou Wang, Guibao Shen, Dongyu Yan, Shuai Yang, Tianshuo Xu, Yihua Du, Wei Wang, Tianyi Gui, Lianghua Huang, Yingcong Chen
- **机构**: HKUST 方向，项目在阿里巴巴实习期间完成（部分待核实）*(tentative)*
- **Venue**: arXiv preprint（2026-08-23 投稿）
- **arXiv**: [2608.23565](https://arxiv.org/abs/2608.23565)
- **摘要与创新**: 解决交互式流式世界模型的张力：control 需短窗口、memory 需无限长。训练用 **mixed per-head attention windows**（多数 head 只看近窗，少数 global head 看全史）+ **random head routing** + 随机 chunk-dropping；推理用**有界 KV cache + pose-indexed landmark bank** 把全史压进固定预算。8 源数据引擎 + DMD 蒸馏 4-step LoRA。
- **实验结果**: 单 backbone 同时服务高保真多步与实时 4-step，**704×1280** 流式；较 6 个近期交互式 WM 最佳控制保真（**11.95° 旋转误差**）与最佳生成质量；分钟级 out-and-back rollout（64s、384 latents）固定 12-chunk cache 下仍重建起始视角（sliding window 已换出、full-KV OOM）。
- **对比**: 相对 sliding-window（无远距离记忆）与 Full-KV（OOM），用 landmark bank 检索实现"整个过去都在预算内"。

### 38. Twin: Playing an Unknown Game with a Test-Time Digital Twin
- **中文标题**: Twin：用测试时数字孪生玩未知游戏
- **作者**: Alexy Skoutnev, Kirill Acharya, Gaston Longhitano, Madeleine Udell, Kevin Ellis, Iddo Drori
- **机构**: Stanford（Udell, Acharya）、Columbia（Drori）、Cornell（Ellis）等
- **Venue**: arXiv preprint（2026-08-14 投稿）
- **arXiv**: [2608.14490](https://arxiv.org/abs/2608.14490)
- **摘要与创新**: Test-time World-model Inference：用前沿 coding agent（OpenAI Codex）测试时编写可执行 world model（逐条 transition 校验的 Python 程序）。harness 强制"每次真实动作前回放所有已观测 transition"，mismatch 即反例修复。核心洞见：**推断目标（goal）才是难点**——先假设 goal 用最省动作计划判别 rival goal。
- **实验结果**: ARC-AGI-3 25 个公开游戏 **23/25 游戏、179/183 关（97.8%）**；action-efficiency **93.3/100**（base 7.8%、off-the-shelf harness 61.1%）；比首次人类更高效通过 158/179 关；87.2%（156/179）在首 reward 前正确推断 goal；twin 精确预测 79% 未见 state-action。
- **对比**: 相对 OPINE-World/EWM/Schema，每次实动作前强制全史复盘校验，且先验 goal 假设。

### 39. PlayWorld: Benchmarking World Models with Agent Players (HKU/Kuaishou)
- **中文标题**: PlayWorld：用 Agent 玩家在长程目标上评测世界模型
- **作者**: Kaixin Ding, Xi Chen, Minghong Cai, Zhiyuan Xu, Yiyang Wang, Yuxiang Lu, Junyi Li, Shuyang Chen, Yuan Gao, Xin Tao, Pengfei Wan, Hengshuang Zhao
- **机构**: 香港大学 + 香港中文大学 + 浙江大学 + **快手可灵（Kling Team）**
- **Venue**: arXiv preprint（~2026-08-14）
- **arXiv**: [2608.13552](https://arxiv.org/abs/2608.13552)
- **摘要与创新**: "多模态 Agent Player"交互式评测：给定长程目标（如"转 360°"），Agent Player 观察生成帧并自适应 Keep/Stop/Extend/Correct/End。171 个带目标场景，覆盖几何一致性、交互保真度、视野外演化、洞见演化四维。
- **实验结果**: 评测 9 个世界模型（Genie 3、LingBot-World、HY-World2、SANA-WM、Hunyuan-GameCraft-2、Matrix-Game-3.0 等）；当前模型在长程交互目标上仍不可靠，尤其空间一致性与持久状态。
- **对比**: 相对固定动作条件评测，实现跨模型公平对比、诊断长程能力边界。

### 40. WorldMind: Decoupled Game World Model for State-Aware NPC Behavior
- **中文标题**: WorldMind：面向状态感知 NPC 行为的解耦游戏世界模型
- **作者**: Zhiyang Deng, Boran Zhang, Danze Chen, Yeying Jin
- **机构**: 香港方向（HKU），腾讯实习期间完成
- **Venue**: arXiv preprint（~2026-08-18）
- **arXiv**: [2608.21439](https://arxiv.org/abs/2608.21439)
- **摘要与创新**: 首个将 NPC 行为从视频生成显式解耦的游戏世界模型。四层：Understanding（重建 compact state，几何+技能双分支）→ Decision（通用 LM 规划下一步）→ Control（动作转时空对齐条件）→ Generation（视频扩散实时合成）。配套 **BOSS-140K** 数据集（144,631 片段、200+ 小时、14 boss，含 Hollow Knight、The Binding of Isaac）+ 自动采集 agent。
- **实验结果**: ~20 FPS 实时闭环；~70% 成对比较中被人类认为比基线更战术合理、更连贯。
- **对比**: 相对隐式（NPC 行为涌现）或显式外部控制，首次让 NPC 决策显式由游戏状态驱动。

### 41. Game2World Engine: Unlocking In-the-Wild Gameplay Videos for World Model Training
- **中文标题**: Game2World 引擎：解锁野生游戏视频用于世界模型训练
- **作者**: Wenxuan Shen, Dongna Jin, Dongping Chen
- **机构**: 待核实（github.com/Dongping-Chen/Game2World）*(tentative)*
- **Venue**: arXiv preprint（2026-08-26 投稿）
- **arXiv**: [2608.24680](https://arxiv.org/abs/2608.24680)
- **摘要与创新**: "世界模型缩放需要数据引擎，不只是更多爬取"。GameUI-Taxonomy 形式化游戏 HUD/UI；G2WEngine 自动从真实游戏视频提取复用 UI 资产并合成时间一致 UI overlay（96K 合成配对视频 + 1,079 真实剪辑、303 游戏、5,132 已验证 UI 元素 21 类）。**GameCleaner**：mask-free 游戏 UI 移除模型（语义理解去除 HUD 保留场景运动）。
- **实验结果**: UI-free 数据上世界模型 VideoReward **+6.83%**；GameCleaner 合成集 AAR **95.36**（超最强 mask baseline 57.3%）、真实集 AAR 80.05、背景保持 99.8%。
- **对比**: 相对 mask-based 视频对象移除，首个 interface-world 解耦 + mask-free 通用 UI 移除。

---

## 💻 代码执行与偏好优化（Code Execution & Code Preference Optimization）

### 42. AgentExecutor: Partial Code Execution via Agentic Context Generation (ASE'26)
- **中文标题**: 通过智能体化上下文生成实现部分代码执行
- **作者**: Junkai Chen, Chengran Yang, Xing Hu, Zhenhao Li, Xin Xia, David Lo
- **机构**: 新加坡管理大学 + 浙江大学 + 约克大学
- **Venue**: **ASE 2026**（第 41 届 IEEE/ACM ASE，慕尼黑 2026-10-12~16），DOI 10.1145/3832783.3834355
- **arXiv**: [2608.05959](https://arxiv.org/abs/2608.05959)
- **摘要与创新**: 运行任意代码片段难在缺上下文与缺依赖。三 agent 三阶段：EnvAgent（环境准备）→ RefAgent（覆盖引导动态探索 + coverage-guided 上下文剪枝）→ EvoAgent（程序合成生成 prefix 生成器系统化扩展搜索空间）。一改 prior（LExecutor 预测注入、Treefix 前缀树）的受限动作空间。
- **实验结果**: Stack Overflow snippets 代码覆盖 **94%**、开源项目 90%，超 SOTA Treefix **19.9% / 13.8%**；执行时间最多省 **80.3%**、成本最多降 56.6%。
- **对比**: 明确对比 LExecutor 与 Treefix，指出动作空间/反馈受限、优化僵硬。

### 43. Step-KTOder: Function-Level Execution Feedback for Code Preference Optimization (EMNLP'26)
- **中文标题**: Step-KTOder：用于代码偏好优化的函数级执行反馈
- **作者**: Idris Nechnech, Sehwan Kim, Jimin Seo, Yeongoon Kim, Minhae Oh, Sangwoo Hong, Jungwoo Lee
- **机构**: 首尔大学 + 建国大学
- **Venue**: **Findings of EMNLP 2026**
- **arXiv**: [2608.23632](https://arxiv.org/abs/2608.23632)
- **摘要与创新**: 把数学推理的 process supervision 移植到代码：step 定义为分解后多函数程序的模块级函数，用自动生成单元测试为每函数打二值正确性标签，outcome-level KTO + stepwise process 监督。关键发现：**执行标签不可或缺**——LLM-as-a-judge 与执行标签总体一致 73.2%，但对 passing 函数仅 52.2% 一致（系统性过度预测失败）。
- **实验结果**: 指令微调后 Qwen2.5-Coder：BigCodeBench Hard **+26.7%**、LiveCodeBench **+27.0%**；HumanEval(+)/MBPP(+)/BigCodeBench/LiveCodeBench 全面优于 outcome-only KTO 与 DPO。
- **对比**: 相对 outcome-only KTO/DPO 及推理期调试（S*、ORPS），把函数级执行反馈用于离线数据构建并更新策略。

---

## 📐 基准评测（Benchmarks & Evaluation）

### 44. StartupBench: Benchmarking General-Purpose Agents on Market-Validated Workflows (ByteDance)
- **中文标题**: 在市场验证的端到端工作流上评测通用 Agent
- **作者**: Liya Zhu, Xin Ma, Tao Liu, Haodong Wang, Ge Zhang（负责）+ 30+ 贡献者
- **机构**: ByteDance Seed + 南京大学 + M-A-P + TokenWave.AI
- **Venue**: arXiv preprint（~2026-08-18）
- **arXiv**: [2608.17800](https://arxiv.org/html/2608.17800)
- **摘要与创新**: 从**市场验证的 AI 原生创业公司**产品反推真实任务（访谈+调研），规避研究者自选任务的乐观偏差。97 任务覆盖 6 大领域（医疗/金融/法律/商业/STEM/教育人文），平均每任务 25.3 条细粒度 rubric，统一 Nanobot harness + GPT-5.5 judge。
- **实验结果**: 最强模型（Kimi-K3、GPT-5.6-sol 平均 73.67%/73.61%）在严格标准（score≥90）下完成率也不到 **1/3**；专业 agent（83.50/39.18%）显著高于通用 agent（64.26/19.74%，oracle best 71.75/28.06%）；主要失败来自复杂指令遵循与领域知识。
- **对比**: 相对 researcher-selected 任务基准（如 Workspace-Bench），以市场验证工作流衡量 E2E 交付。

### 45. EcoAgent-Bench: Economic Decision-Making in Budget-Constrained LLM Agents
- **中文标题**: 预算约束下 LLM Agent 的经济决策评测
- **作者**: Jie Wu, Ming Gong, Feixiang Cheng, Qinqin Zhao
- **机构**: 待核实 *(tentative)*
- **Venue**: arXiv preprint（2026-08-06 投稿）
- **arXiv**: [2608.05519](https://arxiv.org/abs/2608.05519)
- **摘要与创新**: 首个把"成本作为任务本身的部分"的 agent benchmark：304 个真实衍生任务（GAIA/HotpotQA/MuSiQue 改造），每动作标价、显式预算，测四类决策：避免不必要 escalate、证据不足时升级、选择 model tier、在无依据前提上停止。**economic-consistency** = min(升级向准确率, 省钱向准确率)。
- **实验结果**: Tool-API agents 仅 **3.9–24.0%** micro strict success（economic consistency 至多 7.3%）；workspace-CLI 形态（Claude Code/Codex）Econ 44.6–53.6%（Claude Code Opus 4.8 最高：Up 54%、Save 96%）。预算阈值扫描下 GPT-5.4 escalate 率 0%→3%——加预算数字≠给资源选择策略。
- **对比**: 相对只看 task completion 的基准，将预算可行性纳入严格成功定义。

### 46. FrontierFinance: Measuring Frontier Intelligence of Finance Agents (Samaya AI)
- **中文标题**: 衡量金融 Agent 前沿智能的挑战性基准
- **作者**: Yuhao Zhang, O. Ozan Koyluoglu, Thejas Venkatesh, Richard Diehl Martinez, Vishank Bhatia, Arash Alidoust, Ashwin Paranjape
- **机构**: Samaya AI
- **Venue**: arXiv preprint（2026-08-12 投稿）
- **arXiv**: [2608.11683](https://arxiv.org/abs/2608.11683)
- **摘要与创新**: 覆盖完整投资者工作流的开放金融基准：220 条专家级查询、11,543 条带来源归因 rubric、6 大用例；针对现有基准只测数据抽取、参考式度量、泛 LLM-judge 不足。
- **实验结果**: **工具 harness（而非模型本体）强烈塑造质量与效率**；Samaya 自研 56.0% 领先，超最强开放模型 Claude Fable 5 (49.2%) 且成本约低 2.2×；最强开源 Kimi K3 (46.4%) 以 4.5× 更低成本近乎追平最强闭源；最难的 Screening & Discovery 与 Sector/Industry/Macro 用例最强系统也只到 33%/39%。
- **对比**: 相对现有金融 QA/抽取基准（数据抽取接近饱和），对 open-ended 长形式分析做细粒度 rubric 评估。

---

## 📈 综合洞察（Key Takeaways）

1. **RLVR 进入"精细化"时代**：从"能不能 RL"转向"怎么稳定 RL"——探索崩溃（weak-model guidance）、跨域融合（Merge/Mix-RL/MOPD）、标签自由（TTPO）、可验证反馈形态（Step-KTOder 函数级执行标签）。执行标签已被证明是代码领域监督的"金标准"，LLM-as-judge 对 passing 函数系统性误报。
2. **Agent 训练从"prompt"走向"harness + 数据管线"**：Agent Lightning 定义 harnessed agentic RL；MoRe 把多模态角色注入单模型；WikiSkill 证明持久知识库可与技能共同进化并跨模型迁移。"交互税"提醒多 agent 通信会抹掉多样性。
3. **生成式推荐/广告进入全栈工业落地**：UniVA/OneRanker（腾讯）、GR4AD（快手）、GRAB（百度）、EST（淘宝）均报告线上显著收益（GMV/CTR/RPM/收入），生成式推荐正从"能不能做"进入"如何对齐商业价值与做对 serving"阶段。MARCO 指出被完美聚合校准掩盖的点击异质性是新优化空间。
4. **世界模型聚焦"长程记忆"与"评测"**：ReWorld 用 landmark bank 在固定预算内保留长程记忆；PlayWorld 用 Agent Player 交互式评测揭示当前模型长程不可靠；Twin 把世界模型推断变成"测试时写程序"并先验 goal 假设——在 ARC-AGI-3 上 97.8% 通过。
5. **多模态预训练的"物理"逐渐清晰**：Meta 的受控实验给出语言作为万能助推器、5% 计算预算达到强生成、早期统一优于晚期对齐等可操作配方。
6. **低门槛预训练成为现实**：Puro-2B 在 <$5K、单张消费级 GPU 上逼近 Qwen2-1.5B，开源预训练的工程门槛被系统性压低。
7. **Benchmark 转向"市场验证"与"经济理性"**：StartupBench 以市场验证工作流为基准，EcoAgent-Bench 把成本纳入成功定义，FrontierFinance 强调工具 harness 比模型本体更关键。

---
*Generated 2026-08-30. Papers verified via websearch against arXiv listings. Affiliations marked (inferred)/(tentative) where not explicit in abstract; several are Chinese academic/industry labs.*
