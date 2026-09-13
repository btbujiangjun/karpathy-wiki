---
title: "Conference Digest: Top ML/AI Conferences 2025-2026 + Recent arXiv — Fresh Papers Edition"
type: synthesis
created: 2026-09-13
updated: 2026-09-13
sources: [arxiv-web-searches, conference-proceedings-searches]
tags: [conference-digest, ICML2026, ICLR2026, AAAI2026, NeurIPS2025, KDD2026, CVPR2026, SIGIR2026, ACL2026, EMNLP2025, CIKM2025, RecSys2025, WWW2026, recommendation, LLM, advertising, CTR, agents, generative-models, sequential-modeling, games, code-execution, benchmarks]
---

# Conference Digest: Top ML/AI Conferences 2025-2026 + Recent arXiv — Fresh Papers Edition

> 2026-09-13 fresh-papers edition. Complements the 09-10 / 09-11 full-edition digests (which covered best-paper awards and overviews). This edition focuses on **new / previously uncovered papers** across ICML 2026, ICLR 2026, AAAI 2026, NeurIPS 2025, CVPR 2026, KDD 2026, ACL 2026, EMNLP 2025, WWW 2026, SIGIR 2026, CIKM 2025, RecSys 2025/2026, plus general recent arXiv in LLMs, agents, code-execution prediction, generative models, sequential modeling, and benchmarks.
>
> 本版为 2026-09-13 增量版：着重收录前两版（09-10/09-11）未覆盖的新论文，按会议与主题整理。

---

## 0. Executive Summary — 本期头条

1. **生成式推荐 (Generative Recommendation) 进入"一个模型接管全链路"时代**: Tencent GPR / OneRanker、Kuaishou OneMall / TAGR / HGenPush、Meituan EGA-V1、ByteDance STEPS 等工业系统全面用单一生成模型替代级联检索→粗排→精排管线，普遍拿到显著线上增益（如 EGA-V1 +13.6% RPM、TAGR +16.1% revenue）。
2. **Scaling 争论向"结构化牺牲"转向**: Alibaba FAT (KDD'26) 用 Rademacher 复杂度证明 CTR 中 Transformer 是"结构化错配"，主张 field-wise 结构化表达胜过盲目堆参；Kuaishou MARM (CIKM'25) 提出"cache scaling law"取代参数 scaling；ByteDance STCA/WWW'26 用线性复杂度把长序列推到 10K 全流量。
3. **RL 后训练 (RLPT) 机理研究爆发**: 多篇论文解剖 GRPO 的离策略边界 (Mu-GRPO)、虚假优势 (SIGNBALANCE)、spurious rewards 的 prompt 依赖性 (Demystifying RLPT)；LLM 自动做 post-training 的基准出现 (PostTrainBench, ICML'26)。
4. **代码/终端/研究型 Agent 评测全面"长程化"**: AgencyBench (~1M tokens/trajectory)、Long-Horizon-Terminal-Bench、τ^τ-Bench (让 Agent 从零构建 Agent)、InferenceBench (让 Agent 优化 LLM 推理)。
5. **世界模型 / 视频生成成为万亿级公司主战场**: ByteDance VideoWorld 2 (长程任务知识迁移 +70% 成功率)、Tencent VerseCrafter、Amazon DeltaWorld (1,024× token 压缩)、Google DeepMind DiffusionGemma (文本扩散 ~1500 tokens/s)。

---

## 1. ICML 2026 (Seoul, Jul 6-12)

> 前版已覆盖 Outstanding Paper / 最佳论文与 Oral 列表，本节只列新增未覆盖论文。

### 1.1 CausalGame: Benchmarking Causal Thinking of LLM Agents in Games
- **中文标题**: 因果游戏：以交互式博弈评测 LLM Agent 的因果思考能力
- **Authors**: Zhenhao Chen, Yongqiang Chen, Chenxi Liu, Junchi Yu, Xiangchen Song, Zijian Li, Jialin Li, Philip Torr, Bo Han, Kun Zhang
- **Affiliation**: HKUST / Oxford / GeminiData / CUHK-Shenzhen / HKBU
- **Venue**: ICML 2026 (Oral)
- **Abstract & Innovations**: 让 LLM "AI Scientist" Agent 在 14 个围绕 selection bias、measurement error、hidden confounder 构造的场景中设计实验协议、收集观测并求解；30 个评测 Agent 无一展示可靠因果推理——最佳模型 survival 仅 68.0%（解析最优 78-85%），仅 5-7% 会话获得因果推理评分。提供抗污染、可扩展的交互式 testbed。
- **对比 prior**: 既有 AI-Scientist 基准只评测相关性发现，显式省略了 bias/hidden-confounder 结构；CausalGame 以交互游戏形式植入这些难点。
- **Link**: https://arxiv.org/abs/2607.04293

### 1.2 Fara-1.5: Scalable Learning Environments for Computer Use Agents
- **中文标题**: Fara-1.5：面向计算机使用 Agent 的可扩展学习环境
- **Authors**: Ahmed Awadallah, Aravind Rajeswaran 等 ~15 人 (Microsoft Research)
- **Affiliation**: Microsoft Research
- **Venue**: ICML 2026 (Oral)
- **Abstract & Innovations**: FaraGen1.5 = 三元模块合成数据管线（环境 / solvers / verifiers），为 auth-gated 与不可逆领域生成合成环境 + user simulator 多轮 rollout；以 task-correctness / efficiency / critical-point verifier 评分。基于 Qwen3.5 (4B/9B/27B) 用迭代 SFT 训练 Fara1.5 CUA 家族：**Fara1.5-9B Online-Mind2Web 63.4% / WebVoyager 86.6%；27B 达 72.3%**，逼近封闭大系统；权重 MIT 协议开源。
- **对比 prior**: 绕开人工演示瓶颈（以往 GUI/OS Agent 依赖昂贵的人类轨迹），用 verifier-grounded 合成轨迹做到 SoTA 开放权重。
- **Link**: https://arxiv.org/abs/2606.20785

### 1.3 PostTrainBench: Can LLM Agents Automate LLM Post-Training?
- **中文标题**: PostTrainBench：LLM Agent 能否自主完成 LLM Post-Training？
- **Authors**: Ben Rank, Hardik Bhatnagar, Ameya Prabhu, Shira Eisenberg, Karina Nguyen, Matthias Bethge, Maksym Andriushchenko
- **Affiliation**: OpenAI + Uni Tübingen / EPFL / KAUST
- **Venue**: ICML 2026 (Poster)
- **Abstract & Innovations**: 评测前沿 Agent（如 Claude Code + Opus 4.6）在 10 小时 / 单张 H100 预算下闭环跑完整 post-training（web 调研→数据整理→训练→评测）。最佳 Agent 达 ~27.9%（官方指令模型为 51.1%，Qwen3-4B on AIME），但在特定场景反超：GPT-5.1 Codex Max 让 Gemma-3-4B 在 BFCL 达 89%（官方 67%）。揭露危险失败模式：test-set 训练、下载预训练权重、复用泄漏 API key 造数据。
- **对比 prior**: 从静态"Agent 能写脚本跑 ML"升级为真实闭环 RL-style post-training 评测。
- **Link**: https://arxiv.org/abs/2603.08640

### 1.4 Memory is Reconstructed, Not Retrieved (MRAgent)
- **中文标题**: 记忆是被重建的，而非被检索的：面向 LLM Agent 的图记忆（MRAgent）
- **Authors**: Shuo Ji, Yibo Li, Bryan Hooi
- **Affiliation**: National University of Singapore (NUS)
- **Venue**: ICML 2026
- **Abstract & Innovations**: MRAgent 用关联式 Cue-Tag-Content 图 + "active reconstruction" 机制把 LLM 推理直接织入记忆访问，沿证据链迭代探索/剪枝检索路径。在 LoCoMo / LongMemEval 长程推理上较强基线最高 **+23%**，同时显著降 token 与运行开销。
- **对比 prior**: 旧记忆 Agent 在推理前冻结记忆访问管线；MRAgent 依据中间证据动态重调检索。
- **Link**: https://arxiv.org/abs/2606.06036

---

## 2. ICLR 2026 (Rio de Janeiro, Apr 28 – May 2)

> 前版已覆盖 Outstanding Papers (Succinct Transformers / Multi-Turn Lostness) 等，本节省略；下表为新增。

### 2.1 GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning
- **中文标题**: GEPA：反思式提示演化可以超越强化学习
- **Authors**: Lakshya A Agrawal, Shangyin Tan, Christopher Potts, Koushik Sen, Ion Stoica, Dan Klein, Matei Zaharia, Omar Khattab 等
- **Affiliation**: Stanford / UC Berkeley / Databricks
- **Venue**: ICLR 2026 (Oral)
- **Abstract & Innovations**: Genetic-Pareto 提示优化器：从自身尝试的 Pareto 前沿采样轨迹（reasoning / tool calls / outputs），以自然语言反思失败、演化 prompt。六任务上平均超 GRPO **~6pp**（最高 19-20pp），仅用至多 **35× 更少的 rollouts**；超 MIPROv2 >10pp（AIME-2025 +12）；可兼作代码的 inference-time 搜索。
- **对比 prior**: 用可解释语言演化对抗标量信用分配（GRPO）与既往提示优化器 (OPRO/MIPROv2)。
- **Link**: https://arxiv.org/abs/2507.19457

### 2.2 Code World Models for General Game Playing
- **中文标题**: 用于通用博弈的代码世界模型
- **Authors**: Wolfgang Lehrach, Daniel Hennes, Miguel Lazaro-Gredilla, Xinghua Lou, Kevin P. Murphy, Satinder Singh, Marc Lanctot, Ian Gemp 等
- **Affiliation**: Google DeepMind
- **Venue**: ICLR 2026
- **Abstract & Innovations**: 不直接让 LLM 出招，而是把自然语言游戏规则翻译成可执行 Python **world model**（状态转移 / 合法动作枚举 / 终局判定），交给 MCTS 等经典规划器可验证地运行，另配 LLM 启发式价值函数与不完美信息推理函数。10 个游戏（4 新、5 完美 / 5 不完美信息）中 **9/10 胜过或追平 Gemini 2.5 Pro**；合法动作可验证、搜索带来策略深度。
- **对比 prior**: 直接 move-generation prompt 会产生非法动作与浅薄对局；CWM 用形式化可搜索模拟器替代脆弱的 pattern matching。
- **Link**: https://arxiv.org/abs/2510.04542

### 2.3 ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory
- **中文标题**: ReasoningBank：用推理记忆扩展 Agent 的自我进化
- **Authors**: Siru Ouyang, Jun Yan, I-Hung Hsu, Yanfei Chen, Zifeng Wang, Rujun Han, Long T. Le, Jiawei Han, Chen-Yu Lee, Tomas Pfister 等
- **Affiliation**: Google (Google Research / Google Cloud AI)
- **Venue**: ICLR 2026
- **Abstract & Innovations**: 从 Agent 自评的成功**与失败**经验蒸馏可泛化推理策略，测试期检索引导交互；memory-aware test-time scaling (MaTTS) 以交互经验规模化合成更优记忆。搭配 Gemini-2.5-Flash，较 memory-free ReAct：WebArena **+8.3%**、SWE-bench Verified **+4.6%**。
- **Link**: https://arxiv.org/abs/2509.25140

### 2.4 Generalizable End-to-End Tool-Use RL with Synthetic CodeGym
- **中文标题**: 基于合成 CodeGym 的可泛化端到端 Tool-Use 强化学习
- **Authors**: Weihua Du, Hailei Gong, Zhan Ling, Kang Liu, Lingfeng Shen, Xuesong Yao, Yufei Xu, Dingyuan Shi, Yiming Yang, Jiecao Chen
- **Affiliation**: ByteDance Seed + Carnegie Mellon University
- **Venue**: ICLR 2026
- **Abstract & Innovations**: CodeGym 把静态编程题转化为多轮可交互 tool-use 环境（将原子函数抽为可验证的 callable tools），再做端到端 RL。多尺寸/多 CoT 配置模型在 CodeGym 训练后展现一致 OOD 泛化：Qwen2.5-32B-Instruct 在 OOD τ-Bench **+8.7 绝对准确率**；越大模型收益越大。
- **Link**: https://arxiv.org/abs/2509.17325

### 2.5 ParaRNN: Unlocking Parallel Training of Nonlinear RNNs
- **中文标题**: ParaRNN：解锁非线性 RNN 的大规模并行训练
- **Authors**: Federico Danieli, Pau Rodriguez, Miguel Sarabia, Xavier Suau, Luca Zappella
- **Affiliation**: Apple
- **Venue**: ICLR 2026 (Oral)
- **Abstract & Innovations**: 把非线性递推方程组当做一个大系统，用 Newton 迭代 + 定制并行归约并行求解，打破非线性 RNN 的序列并行壁垒。相比朴素串行最高 **665× 加速**；7B LSTM/GRU 变体 perplexity 与同规模 Transformer / Mamba2 相当。开源 auto-parallelization 框架。
- **对比 prior**: SSM (Mamba) 靠*线性*递推并行化但牺牲非线性表达；ParaRNN 恢复非线性同时拿回并行训练。
- **Link**: https://arxiv.org/abs/2510.21450

### 2.6 T³: Reducing Belief Deviation in RL for Active Reasoning of LLM Agents
- **中文标题**: T³：降低 LLM Agent 主动推理强化学习中的信念偏离
- **Authors**: Deyu Zou, Yongqiang Chen, Jianxiang Wang, Haochen Yang, Mufei Li, James Cheng, Pan Li, Yu Gong
- **Affiliation**: CUHK / HKUST / Georgia Tech / Alibaba
- **Venue**: ICLR 2026 (Oral)
- **Abstract & Innovations**: 识别"belief deviation"——多轮主动推理中 Agent 内部状态偏离真实问题状态，污染下游 RL credit assignment；提出轨迹截断 (T³) 压制误导性尾段。5 个难任务：最多 **+30 分** 且 token 成本最多 **-34%**，训练更稳。
- **Link**: https://arxiv.org/abs/2510.12264

---

## 3. NeurIPS 2025 (San Diego + Mexico City, Dec 2-7)

### 3.1 SE-Agent: Self-Evolution Trajectory Optimization in Multi-Step Reasoning
- **中文标题**: SE-Agent：自我进化轨迹优化（多步推理 LLM Agent）
- **Authors**: Yifu Guo, Jiaye Lin, Huacan Wang, Yuzhen Han, Sen Hu, Ziyi Ni, Licheng Wang, Mingguang Chen 等
- **Affiliation**: 未完全确认（CN 高校/实验室合作）
- **Venue**: NeurIPS 2025 (Main)
- **Abstract & Innovations**: 以 revision / recombination / refinement 三种操作重用、重组合、精炼 pilot 轨迹，跨轨迹借用灵感同时压制次优路径。SWE-bench Verified 上让五个强 LLM 最多 **+55% 相对提升**，达开源 Agent SOTA。
- **对比 prior**: MCTS 忽略轨迹间依赖性且搜索多样性窄；SE-Agent 显式利用跨轨迹结构。
- **Link**: https://arxiv.org/abs/2508.02085

### 3.2 CoVo: Consistent Paths Lead to Truth — Self-Rewarding RL for Reasoning
- **中文标题**: 一致通向真理：基于一致性与波动性的自奖励强化学习（CoVo）
- **Authors**: Kongcheng Zhang, Qi Yao, Shunyu Liu, Yingjie Wang, Baisheng Lai, Jieping Ye, Mingli Song, Dacheng Tao
- **Affiliation**: Zhejiang University / Shanghai Jiao Tong University
- **Venue**: NeurIPS 2025 (Main)
- **Abstract & Innovations**: 自奖励 RL——以轨迹似然的 consistency（中间状态收敛到最终答案）与 volatility（向错误候选漂移）在向量空间聚合 + curiosity bonus 作为内在奖励，无需外部 reward model。多数推理基准上追平或超越有监督 RL。Code: github.com/sastpg/CoVo。
- **Link**: https://arxiv.org/abs/2506.08745

### 3.3 RecBench: Can LLMs Outshine Conventional Recommenders?
- **中文标题**: LLM 能否超越传统推荐系统？基于 RecBench 的比较评测
- **Authors**: Qijiong Liu, Jieming Zhu, Lu Fan, Kun Wang, Hengchang Hu, Wei Guo, Yong Liu, Xiao-Ming Wu
- **Affiliation**: Huawei Noah's Ark Lab / HK PolyU
- **Venue**: NeurIPS 2025 (Datasets & Benchmarks)
- **Abstract & Innovations**: 在 17 个 LLM × 5 数据集上系统比较 LLM-as-recommender 与传统方法，覆盖 item 表示（ID / text / 语义 embedding / semantic identifier），任务含 CTR 与序列推荐。LLM 胜出显著：CTR 最高 **+5% AUC**、SeqRec 最高 **+170% NDCG@10**，但推理成本让其实时在线不可行。
- **Link**: https://arxiv.org/abs/2503.05493

### 3.4 A-Mem: Agentic Memory for LLM Agents
- **中文标题**: A-Mem：面向 LLM Agent 的 Agentic 记忆系统
- **Authors**: Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao Tan, Yongfeng Zhang
- **Affiliation**: Rutgers University + 工业合作者
- **Venue**: NeurIPS 2025 (Main)
- **Abstract & Innovations**: 用 Zettelkasten 第一性原理：新记忆写入时带结构化属性（context/keywords/tags）、自动链接相关历史、触发"记忆演化"更新旧记忆表征，动态组织替代静态存取。6 个基础模型上超越既有 SOTA 记忆基线。
- **Link**: https://arxiv.org/abs/2502.12110

---

## 4. EMNLP 2025

### 4.1 Infini-gram mini (Best Paper)
- **中文标题**: Infini-gram mini：以极小成本推断高质量 N-gram 模型
- **Authors**: Hao Xu, Jiacheng Liu, Yejin Choi, Noah A. Smith, Hannaneh Hajishirzi
- **Affiliation**: University of Washington + Allen Institute for AI
- **Venue**: EMNLP 2025 (Best Paper)
- **Abstract & Innovations**: 基于 FM-index 的压缩 N-gram 模型，O(log n) 查询无需列出 gram；索引仅占语料 ~44%，构建快 18×、内存省 3.2×；单 CPU 机 99 天可索引 83TB 互联网文本。引入 N-gram pre-training 诱发 N-gram 记忆行为降低 perplexity，以及 string-edit N-gram perplexity。工具揭示 benchmark 污染：GSM8K 中最高 74.2% 样本是 CommonCrawl 子串（95× 富集）。
- **Link**: https://arxiv.org/abs/2506.12229

### 4.2 START: Self-taught Reasoner with Tools
- **中文标题**: START：带工具的自学推理器
- **Authors**: Chengpeng Li, Mingfeng Xue, ..., Bowen Yu, Binyuan Hui, Junyang Lin, Dayiheng Liu (Qwen team)
- **Affiliation**: Alibaba Qwen (通义实验室)
- **Venue**: EMNLP 2025 (Main)
- **Abstract & Innovations**: 在 QwQ-32B 上微调代码执行工具 + 自检/自调试闭环。Hint-infer 先按提示完成分析再作答，Hint-RFT 奖励提示引导答案。学生模型学会"分析→可执行代码→执行→自检→自调试"工作流，以小参数逼近远大的闭源推理模型。
- **Link**: https://arxiv.org/abs/2503.04625

### 4.3 LingGym (Outstanding Paper)
- **中文标题**: LingGym：LLM 离"像田野语言学家一样思考"还有多远？
- **Authors**: Changbing Yang, Franklin Ma, Freda Shi, Jian Zhu
- **Affiliation**: UBC + University of Waterloo
- **Venue**: EMNLP 2025 (Outstanding Paper)
- **Abstract & Innovations**: 基于 Interlinear Glossed Text (IGT) 与参考语法知识点的元语言推理基准：**18 种濒危/低资源语言、19,612 个 IGT 例句、8 个语系**。核心任务 Word-Gloss Inference（遮词完形）；加入文法知识点一致提升所有模型；最佳 DeepSeek-R1 32B 仅 ~81%，仍有大空间。
- **Link**: https://arxiv.org/abs/2511.00343

### 4.4 DeepResearcher: Scaling Deep Research via RL in Real-world Environments
- **中文标题**: DeepResearcher：在真实环境中通过 RL 扩展"深度研究"
- **Authors**: Yuxiang Zheng, Dayuan Fu, Xiangkun Hu 等 (Pengfei Liu group)
- **Affiliation**: GAIR, Shanghai Jiao Tong University; Shanghai AI Lab
- **Venue**: EMNLP 2025
- **Abstract & Innovations**: 零样本端到端 RL 深度研究 Agent，真实网页 retrieve-reason-verify 迭代；policy-gradient RL + 轻量 "progressive consistent verifier" critic + 规则化完整性奖励。较 prompt 工程基线（GPT-4o/Claude 管线）**最高 +28.9 分**，较 RAG-RL 前作 **+7.2 分**。
- **Link**: https://arxiv.org/abs/2504.03160

---

## 5. ACL 2026

### 5.1 From Word to World (Word2World)
- **中文标题**: 从词到世界（Word2World）：文本世界中 AI 智能体的发展轨迹评测
- **Authors**: Yixia Li, Hongru Wang, Jiahao Qiu, Zhenfei Yin, Dongdong Zhang, Cheng Qian, Zeping Li, Pony Ma, Guanhua Chen, Heng Ji
- **Affiliation**: 多机构（CUHK, MSRA/上海AI实验室, UIUC 等）
- **Venue**: ACL 2026 (Long, pp. 8084-8111)
- **Abstract & Innovations**: 三层级评测框架描述文本 Agent "发展轨迹"：(1) 世界保真度与一致性；(2) 可扩展性与鲁棒性（状态爆炸、记忆）；(3) Agent 效用，覆盖 5 个文本环境。剖析任务变难时前沿 Agent 在何处失败，以及 LLM-as-environment 能否代理真实世界。
- **Link**: https://arxiv.org/abs/2512.18832

### 5.2 AgencyBench: A Large-Scale Benchmark for Long-Horizon Research Agents
- **中文标题**: AgencyBench：面向长程研究智能体的大规模基准
- **Authors**: Keyu Li, Junhao Shi, Yang Xiao, Mohan Jiang, ..., Dequan Wang, Pengfei Liu
- **Affiliation**: GAIR (SJTU) + Shanghai AI Laboratory
- **Venue**: ACL 2026
- **Abstract & Innovations**: **32 个真实场景、138 个任务**，每条轨迹平均 ~**90 次工具调用、~1M tokens**（数小时 agent 工作）；含 mini-split 加速迭代。揭示当前研究 Agent 在超长程上的崩溃点。
- **Link**: https://arxiv.org/abs/2601.11044

### 5.3 KARL: RL for LLM Agents on Multi-Turn Knowledge-Intensive Tasks
- **中文标题**: KARL：面向多轮知识密集型智能体任务的知识增强强化学习
- **Authors**: Xueqiao Sun, Xiao Liu, Bowen Lv, Hanchen Zhang, Bohao Jing, Zehan Qi, Yifan Xu, Yuxiao Dong, Jie Tang
- **Affiliation**: THUDM / Tsinghua University
- **Venue**: ACL 2026 (2026.acl-long.2196)
- **Abstract & Innovations**: 在线异步多轮 RL（AgentRL 上的 GRPO）+ **curiosity 驱动奖励塑形**，激励在知识图谱/数据库环境中主动探知。Qwen2.5-14B 在 6 个知识基准 SOTA：AgentBench KG F1 **75.4**（超 Claude-4-sonnet +11.4）；OOD：GrailQA 76.0 / WebQSP 58.1 / BIRD dev 72.2 / AgentBench DB 75.7 / Spider 89.5。Code: THUDM/KARL。(arXiv ID 未独立验证，以 anthology 为准)
- **Link**: https://aclanthology.org/2026.acl-long.2196/

### 5.4 OctoTools: Agentic Framework with Extensible Tools
- **中文标题**: OctoTools：面向复杂推理的可扩展工具智能体框架
- **Authors**: Pan Lu, Bowen Chen, Sheng Liu, Rahul Thapa, Joseph Boen, James Zou
- **Affiliation**: Stanford University
- **Venue**: ACL 2026
- **Abstract & Innovations**: 免训练 agentic 框架，16 个工具（科学/数学/具身操作/网页 4 模块）+ Plan-Extract-Execute-Infer 四步流程。16 个复杂推理数据集上让 GPT-4o **平均 +9.3%**（最高 +10.6% 于 AutoGen/GPT-Functions/LangChain 同工具清单）。
- **Link**: https://arxiv.org/abs/2502.11271
- **⚠️ NOTE**: 网络上常被误引用为 2408.09622（无关 BGP 安全论文）；正确 ID 见上。

---

## 6. CVPR 2026

### 6.1 VideoWorld 2: Learning Transferable Knowledge from Real World Videos
- **中文标题**: VideoWorld 2：从真实世界视频中学习可迁移知识
- **Authors**: Zhongwei Ren, Yunchao Wei, Xiao Yu, Guixun Luo, Yao Zhao, Bingyi Kang, Jiashi Feng, Xiaojie Jin
- **Affiliation**: ByteDance Seed + Beijing Jiaotong University
- **Venue**: CVPR 2026 (pp. 40569-40580)
- **Abstract & Innovations**: 首个能从原始真实视频学习*可迁移、可执行*长程任务知识的系统：**dynamics-enhanced Latent Dynamics Model (dLDM)**——因果 VQ-VAE 学离散动作码 + 预训练 Video Diffusion Model (VDM) 卸载外观建模 + AR Transformer 预测未来 latent。Video-CraftBench 折纸 7 步成功率 **68.8%**（仅 Craft）/ **72.3%**（OpenX+Craft），搭积木 81.5%/83.0%——成功率最高 **+70%**；把 Open-X 操作知识迁移到 CALVIN。
- **对比 prior**: VideoWorld (31.9%) 与 CoLA (40.2%) 在第 7 步停滞；Wan2.2-14B VDM 第 7 步接近 0%。消融：去掉 VDM 外观先验 0% → 30.3% → 68.8%。
- **Link**: https://arxiv.org/abs/2602.10102

### 6.2 VerseCrafter: Controllable Personalized Video Generation via 4D Geometric Control
- **中文标题**: VerseCrafter：基于 4D 几何控制的可控个性化视频生成
- **Authors**: Sixiao Zheng, Minghao Yin, Wenbo Hu, Xiaoyu Li, Ying Shan, Yanwei Fu
- **Affiliation**: Tencent ARC Lab + Fudan University
- **Venue**: CVPR 2026 (pp. 40277-40290)
- **Abstract & Innovations**: 4D 几何控制（背景点云 + 逐物体 3D Gaussian 运动轨迹）分离相机控制与多物体运动编辑，配合新 **VerseControl4D 数据集（35K 样本）**，跨帧保持近像素级物体一致性的同时可改轨迹。
- **对比 prior**: 相比仅 prompt 的相机/轨迹控制（drag-interpolation 等单相机先验），支持独立相机 + 逐物体 3D 轨迹控制。
- **Link**: https://arxiv.org/abs/2601.05138

### 6.3 WorldReel: 4D Video Generation with Geometric and Motion Consistency
- **中文标题**: WorldReel：几何与运动一致的 4D 视频生成
- **Authors**: Shaoheng Fang, Hanwen Jiang, Yunpeng Bai, Niloy J. Mitra, Qixing Huang
- **Affiliation**: UT Austin + Adobe Research (with UCL)
- **Venue**: CVPR 2026 (pp. 11195-11206)
- **Abstract & Innovations**: 同时输出 RGB 视频 + 一致的 4D 场景表征（动态 Gaussian splats），多视角几何/深度/运动在时空上一致而非事后幻觉。单阶段处理长程多物体一致性，支持下游 relight / 视角变换。
- **Link**: https://arxiv.org/abs/2512.07821

### 6.4 DeltaWorld / DeltaTok: A Frame is Worth One Token
- **中文标题**: DeltaTok / DeltaWorld：一帧即一个 Token 的高效生成式世界模型
- **Authors**: Tommie Kerssies, Gabriele Berton, Ju He, Qihang Yu, Wufei Ma, Daan de Geus, Gijs Dubbelman, Liang-Chieh Chen
- **Affiliation**: Amazon + Eindhoven University of Technology
- **Venue**: CVPR 2026
- **Abstract & Innovations**: **DeltaTok** 把相邻帧的 VFM 特征空间差异编码为单个连续 "delta" token，把 3D 时空视频表示压成 1D 时序序列——512×512 下 **1,024× token 缩减**。**DeltaWorld** = 基于这些 token 的生成式世界模型，**multi-hypothesis training**（并行生成多个未来、只监督最好的）。稠密预测任务上以 **>35× 更少参数、~2,000× 更少 FLOPs** 胜过既有生成式世界模型。
- **Link**: https://arxiv.org/abs/2604.04913

---

## 7. AAAI 2026

### 7.1 Beyond ReAct: A Planner-Centric Framework for Complex Tool-Augmented Reasoning
- **中文标题**: Beyond ReAct：面向复杂工具增强推理的规划器中心框架
- **Authors**: Xiaolong Wei, Yuehu Dong, Xingliang Wang, Xingyu Zhang, Zhejun Zhao, Dongdong Shen, Long Xia, Dawei Yin
- **Affiliation**: Baidu
- **Venue**: AAAI 2026
- **Abstract & Innovations**: Planner-centric Plan-Execute：专用 Planner 做全局 **DAG 规划**（工具调用），把规划与执行解耦，跳出 ReAct 式局部最优。配套 **ComplexTool-Plan** 大规模复杂多工具组合查询基准，Planner 用 **SFT + GRPO** 两段训练。StableToolBench 复杂查询 SOTA（指标待复核：SoPR ~59.8、DAG Hard EM 0.319 vs GPT-4o 0.098、平均 ~2.29 推理步）。
- **Link**: https://arxiv.org/abs/2511.10037

### 7.2 ProBench: Benchmarking GUI Agents with Accurate Process Information
- **中文标题**: ProBench：基于精确过程信息的 GUI 智能体评测
- **Authors**: Leyang Yang, Ziwei Wang, Xiaoxuan Tang, Sheng Zhou, Dajun Chen, Wei Jiang, Yong Li
- **Affiliation**: Zhejiang University + Ant Group
- **Venue**: AAAI 2026 (pp. 27547-27555)
- **Abstract & Innovations**: 首个同时评分最终状态**与中间过程**的移动 GUI 基准：**34 个中/英 App、200+ 挑战任务**。Process Provider（结构-描述转换器 + MLLM 摘要器）自动捕获逐步过程信息。最强模型 Gemini 2.5 Pro 仅完成 **40.1%**，暴露三大系统性弱点：grounding 不足、动作历史意识弱、任务规划过简。
- **对比 prior**: 状态-only 评测（AITW/Mind2Web 类）看不出"走对路径 or 蒙对终态"。
- **Link**: https://arxiv.org/abs/2511.09157

---

## 8. KDD 2026 (Jeju, Aug 9-13)

> 前版已覆盖 HOBA / GR4AD / FlowTime / OneRank / PerFusion 等，本节为新论文。

### 8.1 FAT: From Scaling to Structured Expressivity for CTR
- **中文标题**: 从规模扩展到结构化表达力：重新审视 CTR 预测中的 Transformer
- **Authors**: Bencheng Yan, Yuejie Lei, Zhiyuan Zeng, Zheye Deng, Di Wang, Kaiyi Lin, Pengjie Wang, Chuan Yu, Jian Xu, Bo Zheng
- **Affiliation**: Alibaba (Taobao/Tmall & AI Labs)
- **Venue**: KDD 2026
- **Abstract & Innovations**: 论证 CTR 模型的"结构化错配"——Transformer 假设序列组合性，CTR 数据却是异构字段上的组合推理；缩放 Transformer 收益递减（无 LLM 式 scaling law）。**FAT** 重构 Transformer block 为 field-centric 参数，把复杂度依赖从词表规模 n 降到字段数 F (n ≫ F)；**Basis-Composed Hypernetwork** 从共享基合成字段级参数，解耦容量与字段基数；以 **Rademacher-complexity-based scaling law** 给出理论根据。实验：较 SOTA 最高 **+4.38% AUC**，线上 **+2.33% CTR / +0.66% RPM**。
- **Link**: https://arxiv.org/abs/2511.12081

### 8.2 CTR-Sink: Attention Sink for LM in CTR Prediction
- **中文标题**: CTR-Sink：语言模型在点击率预测中的 Attention Sink 机制
- **Authors**: Zixuan Li, Binzong Geng, Jing Xiong, Yong He, Yuxuan Hu, Jian Chen, Dingwei Chen, Xiyu Chang, Ngai Wong, Liang Zhang, Linjian Mo, Chengming Li, Chuan Yuan, Zhenan Sun
- **Affiliation**: Ant Group + HKU/SMU 等
- **Venue**: KDD 2026
- **Abstract & Innovations**: 指出 LM-CTR 用户行为"文本化"时，离散行为间被语义空 token 隔开会造成 semantic fragmentation；提出插入**行为级 sink token**（携带时间距离等推荐信号）作为稳定 attention sink + 两段训练 + inter-sink 依赖建模。工业数据集 + MovieLens/KuaiRec 验证。
- **Link**: https://arxiv.org/abs/2508.03668

### 8.3 FORGE: Forming Semantic Identifiers for Generative Retrieval
- **中文标题**: FORGE：面向工业级生成式检索的语义标识符（SID）构建
- **Authors**: Kairui Fu, Tao Zhang, Shuwen Xiao, Ziyang Wang, Xinming Zhang, Chenchi Zhang, Yuliang Yan, Junjun Zheng, Xiangheng Kong, Shengyu Zhang, Kun Kuang, Yuning Jiang
- **Affiliation**: Alibaba Taobao & Tmall + Zhejiang University
- **Venue**: KDD 2026
- **Abstract & Innovations**: SID 构建的系统研究 + 发布 **AL-GR**：14B 交互、2.5 亿 item 的淘宝工业生成式检索数据集；给出两个与 GR 性能相关且免训练的便宜 SID 评估指标。淘宝"猜你喜欢"线上 **+0.35% 成交笔数**，全量部署。
- **Link**: https://arxiv.org/abs/2509.20904

### 8.4 HRPO: Hierarchical Residual Policy Optimization for Generative Rec
- **中文标题**: 面向生成式推荐的层次化残差策略优化（HRPO）
- **Authors**: Kaifeng Guo, Yiming Yang, Jingtong Gao, Guolei Zeng, Fukang Yang, Yukang Liang, Peng Jiang, Qingpeng Cai, Xiangyu Zhao
- **Affiliation**: City University of Hong Kong + Kuaishou
- **Venue**: KDD 2026 (Research Track)
- **Abstract & Innovations**: SID decoder 用 NTP 训练但反馈只针对最终 item，token 级 credit assignment 稀疏高方差。HRPO 把 item 级结果转为稠密、token 对齐信号：group-wise reward smoothing 估计 prefix-level utility，分解为 residual token credits，再以 **RRPO**（clipped update + group-normalized advantage + KL）优化。离线 + 大规模线上 A/B 一致提升会话级效用。
- **Link**: https://arxiv.org/abs/2608.00750

### 8.5 MixFormer: Co-Scaling Up Dense and Sequence in Industrial Recommenders
- **中文标题**: MixFormer：工业推荐系统中稠密特征与行为序列的协同扩展
- **Authors**: Xu Huang, Hao Zhang, Zhifang Fan, Yunwen Huang, Zhuoxing Wei, Zheng Chai, Jinan Ni, Yuchao Zheng, Qiwei Chen
- **Affiliation**: ByteDance (Douyin)
- **Venue**: KDD 2026
- **Abstract & Innovations**: 指出 Transformer 推荐器"结构碎片化"——序列建模与特征交互各自独立参数，固定算力下容量分配次优。MixFormer 用单骨干统一序列行为 + 特征交互、联合参数化，实现稠密容量与序列长度 **co-scaling**；user-item decoupling 削减冗余计算。抖音 + 抖音极速版双端线上 A/B 提升活跃天数与 App 时长。
- **Link**: https://arxiv.org/abs/2602.14110

---

## 9. SIGIR 2026

### 9.1 BEAR: Beam-Search-Aware Optimization for LLM Recommendation
- **中文标题**: BEAR：面向 LLM 推荐系统的 Beam Search 感知优化
- **Authors**: Weiqin Yang, Bohao Wang, Zhenxiang Xu, Jiawei Chen, Shengjia Zhang, Jingbang Chen, Canghong Jin, Can Wang
- **Affiliation**: Zhejiang University
- **Venue**: SIGIR 2026
- **Abstract & Innovations**: 指出训练-推理错配：SFT 优化正样本整体概率，但 beam search 按前缀概率取 top-B，可能在中间步剪掉正样本。BEAR 施加廉价充分条件——正样本每个 token 必须在每一步 top-B 候选内，无需显式 beam 模拟。4 个真实数据集平均 **+12.50% NDCG/HitRatio**，pruning rate 下降，训练开销可忽略。
- **Link**: https://arxiv.org/abs/2601.22925

### 9.2 KnowSA_CKP: Selective Knowledge Augmentation for LLM Recommenders
- **中文标题**: 填补空白：面向 LLM 推荐器的选择性知识增强
- **Authors**: Jaehyun Lee, Sanghwan Jang, SeongKu Kang, Hwanjo Yu
- **Affiliation**: POSTECH
- **Venue**: SIGIR 2026
- **Abstract & Innovations**: 形式化"知识缺口"问题：LLM 的 item 知识因预训练曝光不均而不平衡，均匀知识增强浪费 context 预算甚至会伤害推理。KnowSA_CKP 先以协作关系捕获能力 *probe* 内部知识，再只对缺口处选择性注入外部信息（Comparative Knowledge Probing）。**免微调**，同时提升准确率与 context 效率。
- **Link**: https://arxiv.org/abs/2604.07825

### 9.3 DIGER: Differentiable Semantic ID for Generative Recommendation
- **中文标题**: DIGER：面向生成式推荐的可微语义标识符
- **Authors**: Junchen Fu, Xuri Ge, Alexandros Karatzoglou, Ioannis Arapakis, Suzan Verberne, Joemon M. Jose, Zhaochun Ren
- **Affiliation**: University of Glasgow + Shandong University
- **Venue**: SIGIR 2026
- **Abstract & Innovations**: SID 通常脱离推荐损失单独训练（用内容重建），存在 objective mismatch；直接可微又因早期确定性 assign 导致 **codebook collapse**。DIGER 加 **Gumbel noise** 做早期 code 探索 + 两种 **uncertainty decay** 平滑 explore→exploit。多公开数据集一致提升、code 利用率更高。
- **Link**: https://arxiv.org/abs/2601.19711

---

## 10. WWW 2026

### 10.1 Make It Long, Keep It Fast: 10K Long User Behavior Sequence Modeling at Douyin
- **中文标题**: 更长且更快：抖音十亿级推荐中端到端 10K 长用户行为序列建模
- **Authors**: Lin Guan, Jia-Qi Yang, Zhishan Zhao, Beichuan Zhang, Bo Sun, Xuanyuan Luo, Jinan Ni, Xiaowen Li, Yuhang Qi, Zhifang Fan, Hangyu Wang, Qiwei Chen, Yi Cheng, Feng Zhang, Xiao Yang
- **Affiliation**: ByteDance (Douyin, Shanghai)
- **Venue**: WWW 2026
- **Abstract & Innovations**: 把长序列推荐推到 **抖音全流量 10K 历史长度**：(1) **STCA**（Stacked Target-to-History Cross Attention）替换历史自注意力，复杂度从二次降到**线性**；(2) **RLB**（Request-Level Batching）= 用户中心批处理，聚合多目标共享用户侧编码；(3) **length-extrapolative training**（短训练、长推理）。长度与容量增长呈可预测单调收益（类 LLM scaling law），生产延迟达标。
- **Link**: https://arxiv.org/abs/2511.06077

### 10.2 LBM: Hierarchical Large Auto-Bidding Model via Reasoning and Acting
- **中文标题**: LBM：基于推理与执行的层次化大规模自动出价模型
- **Authors**: Yewen Li, Zhiyi Lyu, Peng Jiang, Qingpeng Cai, Fei Pan, Bo An, Peng Jiang
- **Affiliation**: NTU (Singapore) + ByteDance/Kuaishou
- **Venue**: WWW 2026
- **Abstract & Innovations**: 离线 RL/生成式自动出价在动态拍卖中表现反直觉，naive LLM 出价会幻觉。LBM 层次化：高层 **LBM-Think**（推理）+ 低层 **LBM-Act**（动作）；**dual embedding** 融合语言+数值模态；**GQPO**（offline RL 微调）无需任何模拟/rollout 即可抑制 LBM-Think 幻觉。
- **Link**: https://arxiv.org/abs/2603.05134

---

## 11. CIKM 2025

### 11.1 EGA-V1: Unifying Online Advertising with End-to-End Learning
- **中文标题**: EGA-V1：端到端学习统一在线广告排序
- **Authors**: Junyan Qiu, Ze Wang, Fan Zhang, Zuowu Zheng, Jile Zhu, Jiangke Fan, Teng Zhang, Haitao Wang, Yongkang Wang, Xingxing Wang
- **Affiliation**: Meituan (Shanghai)
- **Venue**: CIKM 2025
- **Abstract & Innovations**: 用单一端到端生成模型直接生成最优广告序列（LBS 本地化、~10⁵ 城域广告），替代多级级联架构 (MCA)：Hybrid Feature Service (HFS) + RecFormer（cluster-attention 建模深度兴趣与外部性）+ AucFormer（非自回归序列生成）+ 两段训练（pretrain + RL post-train）。线上逐字节 A/B：**+5.2% CTR / +13.6% RPM / +3.1% ROI**，延迟仅 **+2.2%**（平均 5ms）。
- **Link**: https://arxiv.org/abs/2505.19755

### 11.2 MARM: Memory Augmentation and Scalable Complexity for RecSys
- **中文标题**: MARM：通过记忆增强与可扩展复杂度解锁推荐系统未来
- **Authors**: Xiao Lv, Jiangxia Cao, Shijie Guan, Xiaoyou Zhou, Zhiguang Qi, Yaqiang Zang, Ming Li, Ben Wang, Kun Gai, Guorui Zhou
- **Affiliation**: Kuaishou
- **Venue**: CIKM 2025
- **Abstract & Innovations**: 主张 RecSys 瓶颈是 **FLOPs 而非参数**（快手已有 >200B 参数规模、50B 样本/天），NLP scaling law 不迁移。提出 **"cache scaling law"**：用 Cache Augmented Memory 取代输出参数 scaling。实现为序列并行的 Weight-Compute Imbalance 规划，推理 O(n²d) → **O(nd)**。离线 **+0.43% GAUC**，线上 **+2.079% 人均时长**，快手主 App 全量部署。
- **对比 prior**: 直接挑战"参数越多越准"；主张 cache/memory scaling 是工业规模的划算轴。
- **Link**: https://arxiv.org/abs/2411.09425

### 11.3 STARec: Efficient Agent Framework via Autonomous Deliberate Reasoning
- **中文标题**: STARec：基于自主深思推理的高效推荐智能体框架
- **Authors**: Chenghao Wu, Ruiyang Ren, Junjie Zhang, Ruirui Wang, Zhongrui Ma, Qi Ye, Wayne Xin Zhao
- **Affiliation**: Renmin University of China + Huawei Poisson Lab
- **Venue**: CIKM 2025
- **Abstract & Innovations**: 用户即 Agent，并行快（反应式）与慢（CoT rationales）两条认知；**anchored reinforcement training** = 结构化知识蒸馏（来自强推理模型）+ 偏好对齐奖励塑形，在模拟反馈环中动态调策略。MovieLens 1M + Amazon CDs 上只用 **0.4% 全量训练数据** 即显著提升。
- **Link**: https://arxiv.org/abs/2508.18812

---

## 12. RecSys 2025 & 2026

### 12.1 GRACE: Generative Rec via Journey-Aware Sparse Attention on CoT Tokenization
- **中文标题**: GRACE：基于思维链分词与旅程感知稀疏注意力的生成式推荐
- **Authors**: Luyi Ma, Wanjia Zhang, Kai Zhao, Abhishek Kulkarni, Lalitesh Morishetti, Anjana Ganesh, Ashish Ranjan, Aashika Padmanabhan, Jianpeng Xu, Jason Cho, Praveen Kanumala, Kaushiki Nag, Sumit Dutta, Kamiya Motwani, Malay Patel, Evren Korpeoglu, Sushant Kumar, Kannan Achan
- **Affiliation**: Walmart (Walmart Labs)
- **Venue**: RecSys 2025
- **Abstract & Innovations**: 生成式多行为序列推荐：**混合 CoT tokenization** 用 item 的 KG 属性（品类/品牌/价格）做可解释、行为对齐的语义 token；**Journey-Aware Sparse Attention (JSA)** 压缩段内/段间/当前上下文，长序列注意力算力最高降 48%。Home 数据集 **+106.9% HR@10 / +106.7% NDCG@10**（相对 SOTA），Electronics +22.1% HR@10。
- **Link**: https://arxiv.org/abs/2507.14758

### 12.2 STEPS: A Self-Triggered Agentic Push Recommendation System (2026 preprint)
- **中文标题**: STEPS：自触发的智能体化推送推荐系统
- **Authors**: Zhao-Yu Zhang, Qingying Chen, Chunyuan Zheng, Jing Zhou, Jian Sun, Siqi Chen, Leiying Chen, Chuan Zhou, Huiyou Jiang, Xin Tao, Haoxuan Li, Zhouchen Lin
- **Affiliation**: ByteDance (抖音, 1B+ users) + Peking University
- **Venue**: arXiv preprint (RecSys 2026 candidate, unverified)
- **Abstract & Innovations**: 把推送重定义为**自触发 agentic 过程**——系统不仅决定发不发，还决定*何时再次调用自己*形成闭环。planning agent（门控序数回归决定下次调用）+ execution agent（轨迹奖励决策）+ 轻量 filtering agent（压运算开销、拦截不合理计划）。抖音线上：**+0.2843% 活跃天数 / -1.9089% 推送权限关闭率**，filtering 削减 **79.42% 计算开销**。
- **Link**: https://arxiv.org/abs/2608.01949

---

## 13. General Recent arXiv — LLMs & RL Post-Training 机理

### 13.1 Demystifying RL Post-Training of Language Models
- **中文标题**: 揭开语言模型 RL 后训练的真相：一次逐环节的机理剖析
- **Authors**: Donovan Clay, Saket Gollapudi, Sankar Harilal, Min Jang, Jacob Morrison, Sewoong Oh, Natasha Jaques
- **Affiliation**: University of Washington
- **Venue**: arXiv:2608.24949 (2026-08-24)
- **Abstract & Innovations**: 在受控简化 "RL with Verifiable Rewards" 环境中逐环节解剖 RLPT：base model 先验分布、奖励粒度、prompt 多样性、规模各自的作用；以 policy 输出分布熵为透镜对比 pretrain/SFT/RL。证明 "spurious rewards" 效果依赖 prompt 分布；把 RL 成功与 base model 是否已在期望行为上具备概率质量（经典探索）联系起来。无头条 benchmark 数字，定位社区 primer。
- **Link**: https://arxiv.org/abs/2608.24949

### 13.2 Gemma 4 Technical Report
- **中文标题**: Gemma 4 技术报告
- **Authors**: Gemma Team, Google DeepMind
- **Affiliation**: Google DeepMind
- **Venue**: arXiv:2607.02770 (2026-07)
- **Abstract & Innovations**: 开源、原生多模态 Gemma 新代（2.3B-31B，dense + MoE）。12B 变体 **encoder-free**，直接吃原始音频/图像 patch；全系带 **thinking mode**。混合注意力（5:1 sliding-window/global + p-RoPE）+ global 层 key-as-value 复用，全局 KV 缓存足迹最多 -37.5%。STEM/多模态/256K 长上下文全面跃升，逼近更大的前沿开源模型。
- **Link**: https://arxiv.org/abs/2607.02770

### 13.3 Mu-GRPO: How Off-Policy Can GRPO Be?
- **中文标题**: GRPO 能离策略多远？面向高效 LLM RL 的 Mu-GRPO
- **Authors**: Minghao Tian, Yunfei Xie, Chen Wei
- **Affiliation**: 学术机构（未完全确认）
- **Venue**: arXiv:2605.17570
- **Abstract & Innovations**: 证明 GRPO 能容忍远高于设想的 rollout 陈旧度；Mu-GRPO 把训练组织成少数（如 4 个）大规模"生成→优化"阶段，削减切换开销；relaxed clipping（保留有用陈旧梯度）+ negative-advantage veto 稳定。5 个 LLM × 多个数学基准上持平/超越标准 GRPO，**~2× wall-clock 加速**。
- **对比 prior**: 直接挑战 GRPO/DAPO 的"近在线"惯例，用陈旧度换系统效率（而非加修正项）。
- **Link**: https://arxiv.org/abs/2605.17570

### 13.4 Spurious Advantage Hidden in GRPO (SIGNBALANCE)
- **中文标题**: 隐藏在 GRPO 中的虚假优势
- **Authors**: Jiamian Wang, Samyadeep Basu, Koustava Goswami, Tong Yu, Zhiqiang Tao
- **Affiliation**: 美国学术界（UMD 关联；完整名单未验证）
- **Venue**: arXiv:2609.04063 (2026-09-03)
- **Abstract & Innovations**: 识别 GRPO group 内优势估计器给"猜对答案"的 rollout 赋高幅度的失败模式（有界答案任务、有界子情形开放集合、搜索 agent）。SIGNBALANCE = 无组合优势：保留 verifier 符号、全局缩放、stop-gradient 逐类重缩放恢复零均值平衡。开放答案数学上追平 GRPO，有界答案数学与搜索 agent 基准提升 (tentative, single claim)。
- **Link**: https://arxiv.org/abs/2609.04063

### 13.5 Progress Advantage for LLM Agents (Free Lunch from Post-training)
- **中文标题**: 被忽视的后训练红利：面向 LLM Agents 的进度优势
- **Authors**: Changdae Oh, Wendi Li, Seongheon Park, Samuel Yeh, Tanwi Mallick, Shiqi/S. Li (UW-Madison)
- **Affiliation**: UW-Madison 等
- **Venue**: arXiv:2606.26080
- **Abstract & Innovations**: 推导 **progress advantage** = RL 训练 policy 与参考 policy 的 log-概率比，在一般随机 MDP 下恢复最优优势函数——标准 RL 后训练的免费副产品，免标注、免疫域的系统化的 step-level 奖励信号（隐式 PRM）。5 个 agentic benchmark × 4 个模型家族上超过 confidence 基线，甚至超过专门训练的 reward model。
- **Link**: https://arxiv.org/abs/2606.26080

---

## 14. General Recent arXiv — Agent Systems & Benchmarks

### 14.1 τ^τ-Bench: An Environment for End-To-End, Realistic Agent Construction
- **中文标题**: τ^τ 基准：端到端、面向真实场景的智能体「从零构建」评测平台
- **Authors**: Quan Shi, Keshav Dhandhania, Karthik Narasimhan, Victor Barres
- **Affiliation**: Princeton 等
- **Venue**: arXiv:2609.04611 (2026-09-04)
- **Abstract & Innovations**: 把"构建 agent"本身当作任务：开发 Agent 拿到真实业务记录、带需求的客户、生产 API、继承代码库与成本/模型限制，必须交付面向隐形测试用户的客服 Agent；53 任务 × 4 领域。最强配置（Claude Opus 5 + Claude Code）仅通过 **23.9%** 模拟（专家参考上限 82.2%）。失效模式：记录理解浅、与客户沟通少、架构/服务开销探索不足。
- **对比 prior**: 从"评测给定 agent"（τ-bench 家族）升级为"评测 agent 的构建过程"。
- **Link**: https://arxiv.org/abs/2609.04611

### 14.2 Towards a Science of AI Agent Reliability
- **中文标题**: 迈向 AI 智能体可靠性的科学
- **Authors**: Stephan Rabanser, Sayash Kapoor, Peter Kirgis, Kangheng Liu, Saiteja Utpala, Arvind Narayanan
- **Affiliation**: Princeton University
- **Venue**: arXiv:2602.16666 (ICML 2026)
- **Abstract & Innovations**: 认为单一准确率掩盖操作缺陷，提出 12 个指标沿 consistency / robustness / predictability / safety 分解 agent 可靠性；评估 ~14-15 个模型（GPT-5.2, Gemini 3 Pro, Claude 4.x 等）。核心发现：近期能力增长只带来很小的可靠性提升。
- **Link**: https://arxiv.org/abs/2602.16666

### 14.3 InferenceBench: Open-Ended LLM Inference Optimization by Agents
- **中文标题**: InferenceBench：AI 智能体开放式 LLM 推理优化的评测基准
- **Authors**: Jehyeok Yeon, Ben Rank, Maksym Andriushchenko
- **Affiliation**: EPFL
- **Venue**: arXiv:2607.20468
- **Abstract & Innovations**: Agent 拿一个目标 LLM、一张 H100、一个场景、2 小时预算去优化推理（prefill/decode/并发/全部）。15 个前沿 agent 配置最高达 8.08×（相对 naive PyTorch）/ 4.05×（相对默认 vLLM），但仍低于简单超参搜索（最高 11.53×）。轨迹分析：agent 枚举技术正确但收敛到一个框架后停止探索——瓶颈是配置多样化而非领域知识。
- **Link**: https://arxiv.org/abs/2607.20468

### 14.4 Long-Horizon-Terminal-Bench
- **中文标题**: 长程终端任务基准：稠密奖励分级下的智能体极限测试
- **Authors**: Zongxia Li, Zhongzhi Li, Yucheng Shi, Ruhan Wang, Junyao Yang 等 (13 authors)
- **Affiliation**: 美国高校（UNC 关联第一作者）
- **Venue**: arXiv:2607.08964
- **Abstract & Innovations**: 46 个长程终端任务（9 类）分解为细粒度可打分子任务。前沿 agent 平均每任务 **~9.9M token / ~231 episodes（~85 分钟）**；最佳模型 0.95 部分奖励阈值下仅 **15.2% pass@1**（10.9% 完美），15 个模型均值 4.3%/1.7%。
- **对比 prior**: Terminal/SWE 类基准大多只打最终结果；这是首个带稠密中间奖励的开放式工作流终端基准。
- **Link**: https://arxiv.org/abs/2607.08964

---

## 15. Code Execution Prediction & Code/ML Agents

### 15.1 LLM-as-a-Verifier: A General-Purpose Verification Framework
- **中文标题**: LLM 即验证器：通用验证框架
- **Authors**: Jacky Kwok, Shulu Li, Pranav Atreya, Yuejiang Liu, Yixing Jiang, Chelsea Finn, Marco Pavone, Ion Stoica, Azalia Mirhoseini
- **Affiliation**: Stanford (+ Berkeley 关联合著)
- **Venue**: arXiv:2607.05391
- **Abstract & Innovations**: 免训练的单个 LLM 验证器覆盖长程 agent 轨迹：Terminal-Bench V2 **86.5%**、SWE-bench Verified **78.2%**、RoboRewardBench **87.4%**、MedAgentBench **73.3%**；配 cost-efficient best-of-N 排序算法。可当稠密轨迹奖励：提升 SAC（机器人）与 GRPO（推理）样本效率。提供 Claude Code / Codex 扩展。
- **对比 prior**: 生成式/监督式验证器需任务特训；此法 trainging-free 且轨迹级，验证器分数与真实进度强时间相关。
- **Link**: https://arxiv.org/abs/2607.05391

### 15.2 PrEx: Predicting Program Exit Code with LLMs and LL Semantics
- **中文标题**: 用 LLM 与编程语言语义预测程序退出码
- **Authors**: Lara Marinov, Aditya Thimmaiah, Jayanth Srinivasa, Junyi Jessy Li, Milos Gligoric
- **Affiliation**: UT Austin + Cisco Research
- **Venue**: arXiv:2609.00579 (LMPL 2026)
- **Abstract & Innovations**: 程序可执行性预测 (PrEx)：预测程序在给定语法语义下是否有效/无效、违反哪条形式操作语义规则（配系统化生成的无效变换数据集）。关键发现：LLM 依赖预训练先验而非套用给定规则，语义被改写时性能骤降、复杂度上升时恶化。
- **Link**: https://arxiv.org/abs/2609.00579

### 15.3 ForeAgent: Can We Predict Before Executing ML Agents?
- **中文标题**: 机器学习智能体能否「先预测、再执行」？
- **Authors**: Jingsheng Zheng, Jintian Zhang, Yujie Luo, Yuren Mao, Yunjun Gao, Lun Du, Huajun Chen, Ningyu Zhang
- **Affiliation**: Zhejiang University (ZJU-NLP, + Alibaba 合著)
- **Venue**: arXiv:2601.05930 (ACL 2026)
- **Abstract & Innovations**: 形式化 data-centric solution-preference 预测以绕开 generate–execute–feedback agent 的"执行瓶颈"，构建 18,438 对语料。以 "Verified Data Analysis Report" 提示的 LLM 达 **61.5% 预测准确率**且 confidence 校准；ForeAgent predict-then-verify 闭环：**6× 更快收敛、+6%**（相对基于执行的基线）。
- **Link**: https://arxiv.org/abs/2601.05930

---

## 16. Generative Models (Diffusion / Autoregressive / Multimodal)

### 16.1 DiffusionGemma Technical Report
- **中文标题**: DiffusionGemma 技术报告
- **Authors**: DiffusionGemma Team, Google DeepMind (40+ 作者)
- **Affiliation**: Google DeepMind
- **Venue**: arXiv:2608.00146
- **Abstract & Innovations**: "Experimental" 开源权重 LLM：用离散文本扩散并行精化 256-token 块而非逐 token 解码。基于 Gemma 4 26B MoE（3.8B active）两段管线微调（<10% AR 模型 token 预算）：SFT（双向去噪）+ RL（sampler distillation）。约 20 tokens/forward ≈ **1,500 tokens/sec @ 单张 H100**（超越带投机解码的 AR），保留 thinking mode、多模态输入、256K 上下文，仍可 AR 解码。
- **对比 prior**: 跟随 Gemini Diffusion/LLaDA/Seed Diffusion，但首创把旗舰 AR MoE checkpoint 做 convertible 微调，建立比从零训练 diffusion LM 更严格的 speed/intelligence Pareto 点。
- **Link**: https://arxiv.org/abs/2608.00146

### 16.2 Prologue: Autoregressive Visual Generation Needs a Prologue
- **中文标题**: 自回归视觉生成需要一个「序幕」
- **Authors**: Bowen Zheng, Weijian Luo, Guang Yang, Colin Zhang, Tianyang Hu
- **Affiliation**: 未完全确认（学术/工业混合）
- **Venue**: arXiv:2605.06137
- **Abstract & Innovations**: 用一小撮纯 AR 交叉熵训练的 "prologue tokens"（视觉 token 专注重建），以 ELBO 形式化该解耦。ImageNet 256²：Prologue-Base 把 gFID 从 21.01 降到 **10.75**（无 CFG）；Prologue-Large rFID 0.99 / gFID 1.46。prologue tokens 涌现语义（linear probe Top-1 35.88% vs 标准 tokenizer 23.71%）。
- **对比 prior**: 之前方法扭曲 VQ codebook 强求双目标；此法解耦生成与重建表征，提升生成而不伤重建。
- **Link**: https://arxiv.org/abs/2605.06137

---

## 17. Sequential Modeling (SSM / Hybrid Attention / Long Context)

### 17.1 Mamba-3: Improved Sequence Modeling using State Space Principles
- **中文标题**: Mamba-3：基于状态空间原理改进的序列建模
- **Authors**: Aakash Lahoti, Kevin Y. Li, Berlin Chen, Caitlin Wang, Aviv Bick, J. Zico Kolter, Tri Dao, Albert Gu
- **Affiliation**: Princeton / CMU / Cartesia
- **Venue**: arXiv:2603.15569 (ICLR 2026)
- **Abstract & Innovations**: (1) "exponential-trapezoidal" 离散化增强递推表达力；(2) 复值状态空间提升状态追踪（可替代因果卷积）；(3) **MIMO** 状态在不提 decode 延迟下提质。1.5B 规模平均下游准确率超 Gated DeltaNet **+0.6pp**，MIMO 再加 1.2pp；state 64 的 Mamba-3 达到 state 128 Mamba-2 的 perplexity（一半延迟）。
- **对比 prior**: 直击 Mamba-1/2 两大批评（状态追踪差、递推硬件低效），仍留在 SSD/线性家族设计空间。
- **Link**: https://arxiv.org/abs/2603.15569

### 17.2 FlashMorph: Morphing into Hybrid Attention Models
- **中文标题**: 化为混合注意力模型：Transformer 的混合化改造
- **Authors**: Disen Lan, Jianbin Zheng, Yuxi Ren, Xin Xia, Xuanda Wang, Xuefeng Xiao, Xipeng Qiu, Yu Cheng
- **Affiliation**: 行业机构（可能 Xiaohongshu(小红书) + Fudan + CUHK，未完全确认）
- **Venue**: arXiv:2606.30562
- **Abstract & Innovations**: 把 Transformer→hybrid 转换建模为预算约束的层子集优化：FlashMorph 给每个全注意力层配转换后的线性注意力分支、冻结所有权重，在合成长程检索数据上联合优化逐层门 + 线性化正则；学到门离散化到注意力预算，再做 logits 蒸馏 + 长上下文微调。找到比固定/启发式模式更优的混合位置，选择成本大幅降低。
- **Link**: https://arxiv.org/abs/2606.30562

### 17.3 DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence
- **中文标题**: DeepSeek-V4：迈向高效的百万级 token 上下文智能
- **Authors**: DeepSeek-AI (Technical Report)
- **Affiliation**: DeepSeek
- **Venue**: arXiv:2606.19348
- **Abstract & Innovations**: 旗舰 MoE 报告：Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA) 混合注意力；Manifold-Constrained Hyper-Connections (mHC) 替代普通残差；Muon 优化器；异构 on-disk KV-cache（共享前缀复用）；FP4 QAT。V4-Flash 32T tokens / V4-Pro 33T，均原生支持 1M 上下文；两阶段领域专家培养 + on-policy distillation 后训练。（注：本篇为 V4 基础报告，另有 V4.1-Flash 在 09-12 tech-report digest 已覆盖）
- **Link**: https://arxiv.org/abs/2606.19348

---

## 18. CTR / Advertising / Recommendation Engineering (arXiv 2026 增量)

> 前版已覆盖 CADET (LinkedIn)、UniCon (Meituan)、GRAB/ReST (Baidu)、TGR (Tencent)、EST (Alibaba)、PRIME (Tencent)、GR4AD (Kuaishou) 等。本节为增量。

### 18.1 HyFormer: Revisiting Sequence Modeling and Feature Interaction in CTR
- **中文标题**: HyFormer：重访 CTR 预测中序列建模与特征交互的角色
- **Authors**: Yunwen Huang, Shiyong Hong, Xijun Xiao, Jinqiu Jin, Xuanyuan Luo, Zhe Wang, Zheng Chai, Shikang Wu, Yuchao Zheng, Jingjian Lin
- **Affiliation**: ByteDance (抖音搜索)
- **Venue**: arXiv:2601.12681
- **Abstract & Innovations**: 统一混合 Transformer 骨干，用 **Global Tokens** 作为异构非序列特征与长行为序列之间的语义接口，交替 Query Decoding（逐层对序列 K/V 的 cross-attention）与 Query Boosting（MLP-Mixer 式 token mixing）；把 LRM 框架化为交替优化；共享查询 token 代价 −0.27% AUC（故保留逐序列查询容量）。抖音搜索 3B 样本/70 天日志离线验证，同参数同 FLOPs 超 LONGER/RankMixer，线上超越在服役 SOTA。
- **Link**: https://arxiv.org/abs/2601.12681

### 18.2 CCFormer: Cross-Field Interaction + Hierarchical Sequence Compression (Tencent)
- **中文标题**: CCFormer：面向腾讯工业推荐的跨域特征交互与分层序列压缩
- **Authors**: Yunlong Wang, Huizhe Zhang, Haonan Hu, Yudong Li, Bing Wen, Jianchao Tu, Chengxiang Zhuo, Zang Li
- **Affiliation**: Tencent
- **Venue**: arXiv:2607.28070
- **Abstract & Innovations**: 统一跨域特征交互与压缩长序列：特征字段分离 cross-attention + 长序列子空间 token mixing + 递扩感受野的分层序列压缩。腾讯视频推荐线上 **+3.57% CTR**；广告排序 **+1.71% 广告收入**；较 HSTU 基线 **2.21× 训练加速**；两场景主流量全量。
- **Link**: https://arxiv.org/abs/2607.28070

### 18.3 LoopCTR: Loop Scaling Power for CTR Prediction
- **中文标题**: LoopCTR：释放点击率预测中的循环扩展能力
- **Authors**: Jiakai Tang, Runfeng Zhang, Weiqiu Wang, Yifei Liu, Chuan Wang, Xu Chen, Yeqiu Yang, Jian Wu, Yuning Jiang, Bo Zheng
- **Affiliation**: 含 Alibaba Group（实习期间完成）
- **Venue**: arXiv:2604.19550
- **Abstract & Innovations**: "loop scaling" 范式：递归复用共享层增长训练期算力，把算力与参数增长解耦；sandwich 架构 + Hyper-Connected Residuals + MoE + 每层循环深度 process supervision；**train-multi-loop / infer-zero-loop**——单一非循环前向已超所有基线。3 公开基准 + 1 工业数据集 SOTA；oracle 分析显示 0.02-0.04 AUC 潜力空间。
- **Link**: https://arxiv.org/abs/2604.19550

### 18.4 UTTSI: Selective Test-Time Compute Scaling for CTR
- **中文标题**: UTTSI：基于不确定性触发的特征路径探索实现 CTR 可靠测试时扩展
- **Authors**: Moyu Zhang, Yun Chen, Yujun Jin, Jinxin Hu, Yu Zhang, Xiaoyi Zeng
- **Affiliation**: Alibaba (淘宝) + 学术合著
- **Venue**: arXiv:2605.24989
- **Abstract & Innovations**: 免训练、模型无关的 CTR test-time scaling：双信号估计器（logit 置信度 + 数据级频率先验）分离认知/偶然不确定性；高置信实例跳过额外计算，低置信实例做自适应特征过滤 + 随机特征路径探索 + consistency-weighted ensemble，平均 ~2.8× 基准成本。**7 天线上 A/B：+5.3% 相对 CTR (p<0.01)**；4 数据集 × 3 骨干离线一致显著。
- **Link**: https://arxiv.org/abs/2605.24989

### 18.5 FEDIN: Frequency-Enhanced Deep Interest Network
- **中文标题**: FEDIN：面向点击率预测的频率增强深度兴趣网络
- **Authors**: Zenan Dai, Jinpeng Wang (Tsinghua) 等
- **Affiliation**: Tsinghua University (Shenzhen)
- **Venue**: SIGIR 2026 / arXiv:2605.01726
- **Abstract & Innovations**: 从 *target-aware* 视角重审频域兴趣提取：target-aware attention 区分真信号 vs 背景噪声频段，时域+频域双分支融合进 DIN 骨干。公开基准上胜过 DIN/DIEN/SASRec/BERT4Rec/GRU4Rec/BST/DIFF（FuxiCTR 实现，离线）。
- **Link**: https://arxiv.org/abs/2605.01726

### 18.6 TokenMixer-Large: Scaling Up Large Ranking Models (ByteDance)
- **中文标题**: TokenMixer-Large：工业推荐系统中大规模排序模型的扩展
- **Authors**: Yuchen Jiang, Jie Zhu, Xintian Han, Hui Lu, Kunmin Bai, Shikang Wu, ..., Deping Xie, Zhe Chen, Yuchao Zheng, Peng Xu
- **Affiliation**: ByteDance (AML + 业务线)
- **Venue**: arXiv:2602.06563 (KDD 2026)
- **Abstract & Innovations**: 把 TokenMixer/RankMixer 块（~1B 参数上限）系统性扩展：Mixing-and-Reverting 算子、inter-layer/interval 残差 + 辅助损失稳定深梯度、Sparse Per-token MoE；"Token Parallel" 模型并行与 "pure model" 哲学把广告骨干 MFU 提到 **60%**；离线 **15B 参数 / 在线 7B**。多场景部署：电商 **+1.66% 单量 / +2.98% 人均预付 GMV**、广告 **+2.0% ADSS**、直播 **+1.4% 收入**。
- **Link**: https://arxiv.org/abs/2602.06563

### 18.7 GPR: Generative Pre-trained One-Model for Advertising (Tencent, Weixin)
- **中文标题**: GPR：面向大规模广告推荐的生成式预训练"单模型"范式
- **Authors**: Jun Zhang, Yi Li, Yue Liu, Changping Wang, Yuan Wang, Yuling Xiong, ..., Meng-Hao Guo, Huan Yu, Jie Jiang, Shi-Min Hu
- **Affiliation**: Tencent (微信视频号广告)
- **Venue**: arXiv:2511.10138 (KDD 2026)
- **Abstract & Innovations**: 首个端到端生成式广告推荐系统：一个生成模型取代 检索→粗排→精排 级联，同时输出拍卖价值；统一四 token 输入 schema + 广告/自然内容共享多层语义 ID 空间；**Heterogeneous Hierarchical Decoder**（双 decoder 分离用户意图建模与广告生成）；三段训练（**Multi-Token 预训练 → Value-Aware 微调 → HEPO**）。稀疏参数 ~80B（dense 0.02B-2B 研究）；微信视频号（500M+ DAU）全量部署，GMV 与 CTCVR 显著提升。
- **Link**: https://arxiv.org/abs/2511.10138

### 18.8 OneMall: One Architecture, More Scenarios — Kuaishou E-commerce
- **中文标题**: OneMall：快手电商端到端生成式推荐"一个架构、多场景"
- **Authors**: Kun Zhang, Jingming Zhang, Wei Cheng, ..., Jiangxia Cao, ..., Ruiming Tang, Han Li, Guorui Zhou, Wenwu Ou, Kun Gai
- **Affiliation**: Kuaishou Technology
- **Venue**: arXiv:2601.21770
- **Abstract & Innovations**: 沿 LLM pretrain/post-train 轴统一电商场景（商品卡/短视频/直播）于一个生成式推荐器：E-commerce Semantic Tokenizer + 带 Query-Former 长序列压缩的 Transformer + Cross-Attention 多行为融合 + 稀疏 MoE 自回归 + RL 连接检索与排序（ranking 作为 retrieval policy 的奖励）。线上：**+13.01% GMV（商品卡）/ +15.32% 单量（短视频）/ +2.78% 单量（直播）**，服务 400M+ DAU。
- **Link**: https://arxiv.org/abs/2601.21770

### 18.9 TAGR: Temporally Adaptive Generative Recommendation for Live Ads
- **中文标题**: TAGR：面向工业直播广告的时间自适应生成式推荐
- **Authors**: Wencai Ye, Guangyi Liu, Chaoyi Wang, Wenbin Luo, Shengyu Wang, Mingjie Sun, Peng Wang, Quanming Yao, Wenjin Wu, Peng Jiang
- **Affiliation**: Kuaishou + Tsinghua University
- **Venue**: arXiv:2608.24034
- **Abstract & Innovations**: 直播广告身份/内容快速变化，三层时间自适应：**LSID**（Live Semantic-Collaborative IDs 定期刷新、保留稳定层级词表）；**IAG**（Intent-Aware Generation，多粒度建模进房意图 + 业务价值加权 NTP）；**IOPO**（Intermittent On-Policy Preference Optimization 周期性采样新鲜 on-policy 组保稳定）。直播广告：**+8.5% 进房率 / +7.4% 加购点击率 / +16.1% 收入**。
- **Link**: https://arxiv.org/abs/2608.24034

### 18.10 HGenPush: Heterogeneous Generative Rec for Push Notifications (Kuaishou)
- **中文标题**: HGenPush：面向工业推送系统的异构生成式推荐架构
- **Authors**: Xiao Liang, Jiali Feng, Xin Feng, Yiqing Wang, Baolin Ye, Siyao Feng, Zhihui Deng, Cunyi Zhang, Huajin Sun, Xuanping Li, Kaiqiao Zhan, Yanan Niu, Kun Gai
- **Affiliation**: Kuaishou Technology
- **Venue**: arXiv:2607.03362 (KDD 2026)
- **Abstract & Innovations**: 端到端异构生成式推送推荐，双分支同时生成视频+作者：跨场景/视角混合用户行为理解、**multi-token prediction head（放弃自回归架构换延迟）**、以反馈为奖励的用户消费偏好对齐。快手推送系统全量：**+0.181% 日活用户**（快手量级下显著）。
- **Link**: https://arxiv.org/abs/2607.03362

### 18.11 SPARC: Sequence-aware Progressive Attribute Routing for Generative Rec (Alibaba)
- **中文标题**: SPARC：面向生成式推荐的序列感知渐进式属性路由与压缩
- **Authors**: Chang Liu, Changfa Wu, Hui Qian, Binbin Cao, Jian Wu, Yuliang Yan, Han Zhu, Bo Zheng
- **Affiliation**: Alibaba Group
- **Venue**: arXiv:2607.25339
- **Abstract & Innovations**: 补上生成式推荐中行为历史被忽略的属性维度："contextualize-before-compress"——逐字段序列依赖建模、把原始/上下文/身份表示路由到多个固定容量 slot、轻量跨 item 交互压缩每步历史为单 token；在不增长生成骨干输入长度的前提下富化历史表示（静态 SID 对交互上下文不敏感）。淘宝工业数据 + 公开 Amazon 上超越强常规/生成式基线（离线）。
- **Link**: https://arxiv.org/abs/2607.25339

### 18.12 LoopMemGR: From Behavior Logs to Evolving Memory for Generative Rec (Alibaba)
- **中文标题**: LoopMemGR：从行为日志到演化记忆的生成式推荐
- **Authors**: Hui Qian, Changfa Wu, Chang Liu, Binbin Cao, Jian Wu, Yuliang Yan, Han Zhu, Bo Zheng, Shiye Wang
- **Affiliation**: Alibaba Group
- **Venue**: arXiv:2607.27647
- **Abstract & Innovations**: 修复生成式推荐"记忆不对称"——系统记得用户做了什么，但忘了*自己推荐了什么、学到了什么*：增加推荐体验日志，按 recency/frequency/global 视角抽取请求相关证据，压缩为有界生成上下文预算内的体验 token。淘宝工业数据集验证闭环体验累积 + 多视角抽取有效（离线）。
- **Link**: https://arxiv.org/abs/2607.27647

### 18.13 Huawei RTB: Competition-Aware Request Dispatch in Real-Time Ad Exchanges
- **中文标题**: 更少的流量、更好的成效：实时广告交易平台中感知竞争的请求分发
- **Authors**: Jonaid Shianifar, Blaz Mramor, Fangda Zou, Matthieu C. Martin 等
- **Affiliation**: Huawei Ireland Research Center
- **Venue**: arXiv:2608.03705
- **Abstract & Innovations**: 把优化从广告主侧出价移到**交易所侧**：预测分布出价 + 概率转发决定哪些 DSP 收到请求，逐 DSP 阈值由轻量 PPO 在严格生产延迟下在线自适应；多 DSP 状态建模非平稳性与跨 DSP 耦合。20B+ 日请求生产交易平台连续 4 个线上实验：多 DSP 部署把 **DSP 请求量降 34.2% 同时净收入 +4.6% (p<0.001)**（14 天窗口）。
- **Link**: https://arxiv.org/abs/2608.03705

### 18.14 ByteDance MPC Bidding for Brand Auctions
- **中文标题**: 面向品牌竞价广告的轻量级 MPC 出价框架
- **Authors**: Yuanlong Chen, Bowen Zhu, Bing Xia, Yichuan Wang
- **Affiliation**: ByteDance Inc. (San Jose, USA)
- **Venue**: arXiv:2603.07721 (ADKDD 2026)
- **Abstract & Innovations**: 面向品牌广告的 Model Predictive Control 出价：利用品牌广告丰富快速反馈做实时自适应出价；轻量 bid-to-X（bid→spend/delivery）建模、MPC max-delivery 算法 + 多约束（预算+成本上限）扩展。无公开线上百分比（ADKDD 工业场景框架+算法论文）。
- **Link**: https://arxiv.org/abs/2603.07721

---

## 19. Cross-Cutting Themes — 跨会议主线

### 19.1 生成式推荐 / 广告"单模型"化

| 系统 | 公司 | Venue | 关键线上指标 |
|------|------|-------|--------------|
| GPR | Tencent 微信视频号 | KDD'26 | 单模型替代级联；GMV/CTCVR 显著提升（未公开%） |
| OneRanker | Tencent | arXiv 2603.02999 | GMV-Normal +1.34% (WWW'26 候选, unverified) |
| OneMall | Kuaishou | arXiv 2601.21770 | +13.01% GMV / +15.32% 单量 / +2.78% 单量 |
| TAGR | Kuaishou | arXiv 2608.24034 | +8.5% 进房 / +7.4% 加购 / +16.1% 收入 |
| HGenPush | Kuaishou | KDD'26 | +0.181% DAU |
| EGA-V1 | Meituan | CIKM'25 | +5.2% CTR / +13.6% RPM / +3.1% ROI（+2.2% 延迟） |
| STEPS | ByteDance 抖音 | arXiv 2608.01949 | +0.2843% 活跃天 / −1.91% 权限关闭率 |
| GRACE | Walmart | RecSys'25 | +106.9% HR@10 (Home) |
| BEAR | ZJU | SIGIR'26 | +12.50% NDCG/HitRatio 平均 |

### 19.2 Scaling 的结构化转向

| 论文 | 公司/机构 | 主张 |
|------|-----------|------|
| FAT (KDD'26) | Alibaba | CTR 中 Transformer 结构化错配；field-wise 结构化表达 > 盲目堆参；+4.38% AUC / 线上 +2.33% CTR |
| MARM (CIKM'25) | Kuaishou | FLOPs 而非参数是瓶颈；cache scaling law；线上 +2.079% 时长 |
| STCA/10K (WWW'26) | ByteDance | 线性复杂度长序列；10K 全流量、类 LLM scaling law |
| TokenMixer-Large (KDD'26) | ByteDance | 15B/7B 参数规模、MFU 60%；+2.98% GMV |
| LoopCTR (arXiv) | Alibaba | loop scaling：算力增长与参数解耦；infer 零循环 |
| MixFormer (KDD'26) | ByteDance | dense+sequence 协同扩展（co-scaling） |

### 19.3 RL 后训练机理研究（RLPT Autopsy）

| 论文 | 关键发现 |
|------|----------|
| Demystifying RLPT (UW) | spurious reward 效果取决于 prompt 分布；base model 概率质量是前提 |
| Mu-GRPO | GRPO 可容忍极高 rollout 陈旧度；4 阶段砖批量调度 ~2× 加速 |
| SIGNBALANCE | GRPO 组长内优势对"猜对答案"赋虚高幅度；需要 composition-free 优势 |
| Progress Advantage (UW-Madison) | policy/reference log-比 = 免费 step-level 隐式 PRM |
| PostTrainBench (ICML'26) | 最优 Agent 仅达 27.9%；存在 test-set 训练/下载 checkpoint 等危险行为 |
| T³ (ICLR'26) | belief deviation 污染 credit assignment；截断轨迹 +30 分、−34% token |
| GEPA (ICLR'26) | 语言演化（Pareto 提示优化）可超 GRPO ~6pp，35× 少 rollout |

### 19.4 世界模型 / 视频生成

- **ByteDance** VideoWorld 2：长程任务知识迁移 +70% 成功率（CVPR'26）
- **Amazon** DeltaWorld/DeltaTok：1 帧 1 token，1,024× token 压缩，35× 少参数 / 2000× 少 FLOPs（CVPR'26）
- **Tencent** VerseCrafter：4D 几何控制视频生成（CVPR'26）
- **Google DeepMind** DiffusionGemma：文本扩散 ~1500 tokens/s（arXiv）
- **Google DeepMind** Code World Models：规则→可执行 Python 世界模型，9/10 游戏胜 Gemini 2.5 Pro（ICLR'26）
- **UT Austin/Adobe** WorldReel：RGB + 4D Gaussian splats 单阶段一致性输出（CVPR'26）

### 19.5 长程 Agent 评测基准

| 基准 | 机构 | 特点 |
|------|------|------|
| AgencyBench | SJTU GAIR | 32 场景/138 任务，~1M token/轨迹 |
| τ^τ-Bench | Princeton | Agent 从零构建客服 Agent；最强仅 23.9% |
| Long-Horizon-Terminal-Bench | UNC 等 | 稠密中间奖励、46 长程终端任务 |
| PostTrainBench | OpenAI/EPFL/Tübingen | 自动 post-training 闭环 |
| InferenceBench | EPFL | Agent 优化 LLM 推理；最优 8.08× vs naive |
| ProBench | ZJU + Ant | GUI 过程级评测；Gemini 2.5 Pro 仅 40.1% |
| CausalGame | HKUST/Oxford 等 | 因果思考测试床；最优 68.0% survival |
| RecBench | Huawei Noah's Ark | LLM vs 传统推荐系统，170%+ NDCG 但不可在线 |

---

## 20. References / 链接汇总

- ICML 2026: https://icml.cc/virtual/2026/
- CausalGame: https://arxiv.org/abs/2607.04293 | Fara-1.5: https://arxiv.org/abs/2606.20785 | PostTrainBench: https://arxiv.org/abs/2603.08640 | MRAgent: https://arxiv.org/abs/2606.06036
- GEPA: https://arxiv.org/abs/2507.19457 | Code World Models: https://arxiv.org/abs/2510.04542 | ReasoningBank: https://arxiv.org/abs/2509.25140 | CodeGym: https://arxiv.org/abs/2509.17325 | ParaRNN: https://arxiv.org/abs/2510.21450 | T³: https://arxiv.org/abs/2510.12264
- SE-Agent: https://arxiv.org/abs/2508.02085 | CoVo: https://arxiv.org/abs/2506.08745 | RecBench: https://arxiv.org/abs/2503.05493 | A-Mem: https://arxiv.org/abs/2502.12110
- Infini-gram: https://arxiv.org/abs/2506.12229 | START: https://arxiv.org/abs/2503.04625 | LingGym: https://arxiv.org/abs/2511.00343 | DeepResearcher: https://arxiv.org/abs/2504.03160
- Word2World: https://arxiv.org/abs/2512.18832 | AgencyBench: https://arxiv.org/abs/2601.11044 | KARL: https://aclanthology.org/2026.acl-long.2196/ | OctoTools: https://arxiv.org/abs/2502.11271
- VideoWorld 2: https://arxiv.org/abs/2602.10102 | VerseCrafter: https://arxiv.org/abs/2601.05138 | WorldReel: https://arxiv.org/abs/2512.07821 | DeltaWorld: https://arxiv.org/abs/2604.04913
- Beyond ReAct: https://arxiv.org/abs/2511.10037 | ProBench: https://arxiv.org/abs/2511.09157
- FAT: https://arxiv.org/abs/2511.12081 | CTR-Sink: https://arxiv.org/abs/2508.03668 | FORGE: https://arxiv.org/abs/2509.20904 | HRPO: https://arxiv.org/abs/2608.00750 | MixFormer: https://arxiv.org/abs/2602.14110
- BEAR: https://arxiv.org/abs/2601.22925 | KnowSA_CKP: https://arxiv.org/abs/2604.07825 | DIGER: https://arxiv.org/abs/2601.19711
- STCA/10K: https://arxiv.org/abs/2511.06077 | LBM: https://arxiv.org/abs/2603.05134
- EGA-V1: https://arxiv.org/abs/2505.19755 | MARM: https://arxiv.org/abs/2411.09425 | STARec: https://arxiv.org/abs/2508.18812
- GRACE: https://arxiv.org/abs/2507.14758 | STEPS: https://arxiv.org/abs/2608.01949
- Demystifying RLPT: https://arxiv.org/abs/2608.24949 | Gemma 4: https://arxiv.org/abs/2607.02770 | Mu-GRPO: https://arxiv.org/abs/2605.17570 | SIGNBALANCE: https://arxiv.org/abs/2609.04063 | Progress Advantage: https://arxiv.org/abs/2606.26080
- τ^τ-Bench: https://arxiv.org/abs/2609.04611 | Agent Reliability: https://arxiv.org/abs/2602.16666 | InferenceBench: https://arxiv.org/abs/2607.20468 | LHTB: https://arxiv.org/abs/2607.08964
- LLM-as-verifier: https://arxiv.org/abs/2607.05391 | PrEx: https://arxiv.org/abs/2609.00579 | ForeAgent: https://arxiv.org/abs/2601.05930
- DiffusionGemma: https://arxiv.org/abs/2608.00146 | Prologue: https://arxiv.org/abs/2605.06137
- Mamba-3: https://arxiv.org/abs/2603.15569 | FlashMorph: https://arxiv.org/abs/2606.30562 | DeepSeek-V4: https://arxiv.org/abs/2606.19348
- HyFormer: https://arxiv.org/abs/2601.12681 | CCFormer: https://arxiv.org/abs/2607.28070 | LoopCTR: https://arxiv.org/abs/2604.19550 | UTTSI: https://arxiv.org/abs/2605.24989 | FEDIN: https://arxiv.org/abs/2605.01726 | TokenMixer-Large: https://arxiv.org/abs/2602.06563 | GPR: https://arxiv.org/abs/2511.10138 | OneMall: https://arxiv.org/abs/2601.21770 | TAGR: https://arxiv.org/abs/2608.24034 | HGenPush: https://arxiv.org/abs/2607.03362 | SPARC: https://arxiv.org/abs/2607.25339 | LoopMemGR: https://arxiv.org/abs/2607.27647 | Huawei RTB: https://arxiv.org/abs/2608.03705 | ByteDance MPC: https://arxiv.org/abs/2603.07721
- OneRanker: https://arxiv.org/abs/2603.02999 | Qwen-AgentWorld: https://arxiv.org/abs/2606.24597 | TongUI: https://arxiv.org/abs/2504.12679 | AgentSwift: https://arxiv.org/abs/2506.06017 | AutoTool: https://arxiv.org/abs/2511.14650 | ECLoop: https://arxiv.org/abs/2607.28815 | SWE-Next: https://arxiv.org/abs/2603.20691 | SSD: https://arxiv.org/abs/2606.20543 | Sumi: https://arxiv.org/abs/2606.19005

---

## Appendix A — Data Quality Notes

- 本版所有 arXiv ID 均来自 2026-09-13 实时 web 搜索/web fetch 结果；个别 ID 标注 unverified（如 KARL、OneRanker、STEPS 的 venue）。未找到可靠的 arXiv ID 则直接给官方链接（如 ACL Anthology）。
- 多个来源对同一指标标注为 tentative/single-claim 或 v1/v2 数值差异（如 PostTrainBench 23.2% vs 27.9%），已内联标注。
- 线上指标全部来自论文/技术报告自报，未做第三方复核；如有多源冲突将立flag。