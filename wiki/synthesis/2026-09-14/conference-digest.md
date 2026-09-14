---
title: "Conference & arXiv Digest — 2026-09-14 New Papers Edition (ICML/ICLR/NeurIPS/AAAI/KDD/CVPR/ACL/EMNLP/SIGIR/WWW/CIKM/RecSys)"
type: synthesis
created: 2026-09-14
updated: 2026-09-14
sources: [arxiv-web-searches, conference-proceedings-searches]
tags: [conference-digest, ICML2026, ICLR2026, AAAI2026, NeurIPS2025, KDD2026, CVPR2026, SIGIR2026, ACL2026, EMNLP2025, WWW2026, CIKM2025, RecSys2025, recommendation, LLM, advertising, CTR, agents, generative-models, sequential-modeling, games, code-execution, benchmarks, daily-digest]
---

# Conference Digest — 2026-09-14 New Papers Edition

> 本版为 **2026-09-14 增量版**：本轮 web 检索（arXiv + 会议 proceedings）确认了约 17 篇 wiki 中**尚未覆盖**的新论文（全部 ID 已 grep 验证 0 命中），对其给出完整详述（题目中英、作者、机构、venue、背景/方法/创新/实验数字、对比 prior、arXiv 链接）。
>
> 检索同时复现的大量已收录论文（CADET、FAT、GR4AD、GenRec-JD、EST、Mamba-3、Gated Attention、DeepSeek-V4、DeltaTok、VideoWorld 2 等）不重复展开，按会议整理成**交叉引用全景表**（第 3 节），指向既有 wiki 页面。
>
> 中文为主；专有技术词保留英文（RL/CTR/Rank Fusion/Sequence Modeling 等）。

---

## 0. Executive Summary — 本期头条

1. **代码执行预测成为一个独立研究课题 (Program Executability Prediction 家族)**：本版收录 SWE-Bench Pro Verified（揭露 SWE-Bench Pro 的 reward hacking / 任务质量问题，修正若干模型头号数字）+ TAM（长视界程序化任务基准：GPT-5 在 ICD-10-CM 上 exact-match 仅 1%）——与 09-13 版 PrEx（用正式语义预测 exit code）共同构成"代码执行预测 → 程序语义判断"谱系。
2. **评测者本身成为被评测对象**：三篇新论文（mJudge 多语言 judge 建设、Language Bias in LLM Evaluators 语言偏差、FAPO 全自动 prompt 优化）揭示 pairwise accuracy 不足以验证 LLM-as-a-Judge，低资源语言被系统性宽打分（高至 +43% 通过率差异）。
3. **CVPR 2026 世界模型继续All-in"面向物理"**：GenieDrive（4D occupancy 引导、+7.2% mIoU/-20.7% FVD）与 RAYNOVA（ray space 纯自回归、多视角通用）两篇新收录；PhiZero（CASIA，"物理语言" tokenizer + reasoner）把动力学从像素预测解耦为可检查的离散"物理语言"。
4. **工业 KV cache / 长上下文推理效率有新解法**：C²KV（KDD'26，非前缀 KV 复用 + 压缩协同，long-context 推理最高 17×）；RACE Attention（ICLR'26，严格线性时间 attention，单卡 12M token 前反向）；HSA-UltraLong（16M token 外推，长程检索 >90% 准确率）。
5. **RL / 后训练机理主线延续**：Curriculum RL（2606.22317）正面回应 NeurIPS'25 Runner-up "RLVR 不扩展推理容量" 的结论——用 boundary-aware 课程把 pass@256 提升 +9.8~+10.3pp，证明结构性课程（而非更大规模采样）才能推开能力边界。

---

## 1. 新收录论文全述 (New Papers — Full Details)

### 1.1 CVPR 2026

#### GenieDrive: Towards Physics-Aware Driving World Model with 4D Occupancy Guided Video Generation
- **中文标题**: GenieDrive：以 4D Occupancy 引导视频生成实现物理感知驾驶世界模型
- **Authors**: Zhenya Yang, Zhe Liu, Yuxiang Lu, Liping Hou, Chenxuan Miao, Siyi Peng, Bailan Feng, Xiang Bai, Hengshuang Zhao
- **Affiliation**: 华中科技大学 (Xiang Bai) + 香港大学 (Hengshuang Zhao) + 产业合作方
- **Venue**: CVPR 2026, pp. 35680–35690
- **Abstract & Innovations**: 两阶段物理感知驾驶世界模型。（1）轻量 occupancy world model 先生成 4D occupancy：VAE 把占用场压缩到 latent tri-plane（仅 prior 的 58% latent 尺寸），新提出 **Mutual Control Attention** 做 action-conditioned 场景演化，VAE 与 forecaster 端到端联合训练；（2）视频生成器以 4D occupancy 为条件，用 **Normalized Multi-View Attention** 生成多视角一致的视频。核心创新是让"物理中间表征（occupancy）"显式调制视频生成，而不是让扩散模型端到端瞎猜。
- **实验结果**: forecasting mIoU +7.2%（41 FPS，仅 3.47M 参数）；生成质量 FVD −20.7%；多视角驾驶视频生成长度可达 241 帧（8× 长于直接 diffusion 基线）。
- **对比 prior**: 相比直接条件扩散 baseline（不建显式物理中间态），物理一致性更强且成本更低。
- **Link**: https://arxiv.org/abs/2512.12751

#### RAYNOVA: Scale-Temporal Autoregressive World Modeling in Ray Space
- **中文标题**: RAYNOVA：射线空间中的尺度-时间自回归世界建模
- **Authors**: Yichen Xie, Chensheng Peng, Mazen Abdelfattah, Yihan Hu, Jiezhi Yang, Eric Higgins, Ryan Brigden, Masayoshi Tomizuka, Wei Zhan
- **Affiliation**: Applied Intuition + UC Berkeley (BARC / Hybrid Systems Lab)
- **Venue**: CVPR 2026, pp. 25426–25437
- **Abstract & Innovations**: 纯自回归（无扩散）的多视角驾驶世界模型。用 **dual-causal** 框架同时在 scale-wise 与 temporal 两个拓扑序上自回归；以各向同性相对 Plücker-ray positional encoding 代替显式 3D 几何先验，用一个一致框架覆盖视图/帧/尺度；引入 recurrent training 范式对抗长程生成中的分布漂移。
- **实验结果**: nuScenes 多视角视频生成 SOTA，吞吐更高；对未见相机配置 / 新视角泛化无需任何显式 3D 表征。
- **对比 prior**: 传统多视角驾驶世界模型依赖显式 3D 表示或扩散采样；RAYNOVA 是几何无关 + 纯 AR，训练/推理管线统一。
- **Link**: https://arxiv.org/abs/2602.20685

### 1.2 KDD 2026

#### C²KV: Compressed and Composable KV Cache Reuse for Efficient LLM Inference
- **中文标题**: C²KV：面向高效 LLM 推理的可压缩、可组合 KV Cache 复用
- **Authors**: Chuheng Du, Junyi Chen, Hanlin Tang, Kan Liu, Tao Lan, Lin Qu, Chaoyue Niu, Shengzhong Liu, Guihai Chen, Fan Wu
- **Affiliation**: 上海交通大学（SHANGHAI JIAO TONG UNIVERSITY）+ 产业合作
- **Venue**: ACM SIGKDD 2026 (per arXiv comment)
- **Abstract & Innovations**: 统一"非前缀（non-prefix）KV 复用"框架，联合优化 KV cache 抽取与推理期拼接。在冻结 base model 上用轻量 sidecar Extractor（可学习压缩 token + structured attention flow）学出一个**可压缩、位置无关**的 KV cache manifold，并做 compression-concatenation 协同训练——解决"压缩 + 非前缀复用直接拼接会掉精度"的痛点。
- **实验结果**: 显著降低 KV 存储/传输成本；长上下文下推理端到端最高 **17× 加速**且生成质量保持。
- **对比 prior**: 既往 KV 复用方法只省 compute、忽略存储/访问开销；C²KV 把压缩与复用做成一个可微整体。
- **Link**: https://arxiv.org/abs/2607.17715

### 1.3 ACL 2026

#### UR²: Unify RAG and Reasoning through Reinforcement Learning
- **中文标题**: UR²：通过强化学习统一 RAG 与推理
- **Authors**: Weitao Li, Boran Xiang, Xiaolong Wang, Jingyi Ren, Ante Wang, Zhinan Gou, Weizhi Ma, Yang Liu
- **Affiliation**: 清华大学（计算机系 + AIR 智能产业研究院）
- **Venue**: ACL 2026 Main Conference, Long Paper (2026.acl-long.580, pp. 12712–12751)
- **Abstract & Innovations**: 把 retriever 与 reasoner 放进同一个 RL 框架动态协调，超越开放域 QA：**难度感知课程**（只在困难样本上触发检索）＋**混合知识访问**（离线领域语料 + 在线 LLM 生成摘要，两条路径按需切换）。基于 Qwen-2.5-3/7B、LLaMA-3.1-8B，覆盖开放域 QA、MMLU-Pro、医疗与数学推理。
- **实验结果**: 全面超过 RAG 与 RL 基线，多个 benchmark 匹配 GPT-4o-mini / GPT-4.1-mini；对噪声检索结果更鲁棒。
- **对比 prior**: Search-o1 / RAG-Gym / R1-Searcher 等 RAG-RL 工作绑定固定检索设置或单一领域；UR² 给出跨领域的统一 retrieval-reasoning RL 配方。
- **Link**: https://arxiv.org/abs/2508.06165 · Anthology: https://aclanthology.org/2026.acl-long.580/

### 1.4 EMNLP 2025

#### SimulatorArena: Are User Simulators Reliable Proxies for Multi-Turn Evaluation of AI Assistants?
- **中文标题**: SimulatorArena：用户模拟器能否可靠代理多轮对话中的 Assistant 评测？
- **Authors**: Yao Dou, Michel Galley, Baolin Peng, Chris Kedzie, Weixin Cai, Alan Ritter, Chris Quirk, Wei Xu, Jianfeng Gao
- **Affiliation**: Microsoft Research + Georgia Institute of Technology
- **Venue**: EMNLP 2025 Main Conference
- **Abstract & Innovations**: 第一个系统检验 "LLM-simulated user 能否替代真人做多轮评测" 的 benchmark：**909 段人工标注的人机对话**（数学辅导 + 文档创作），从 message-level 与 human 行为匹配度、以及 assistant 评分对齐度两个维度打分模拟器。profile-conditioned 模拟器两任务 Spearman ρ≈0.7，是可行的规模化替代；随后用最优模拟器评测 18 个 assistant（含 GPT-5、Claude 4.1 Opus、Gemini 2.5 Pro）。
- **对比 prior**: AgentSim / MST-bench 等此前用户模拟器缺地面真值人机对话数据；SimulatorArena 首次量化模拟器与人类的对齐与分歧。
- **Link**: https://arxiv.org/abs/2510.05444

### 1.5 ICLR 2026

#### RACE Attention: A Strictly Linear-Time Attention Layer for Training on Outrageously Large Contexts
- **中文标题**: RACE Attention：在超大上下文上训练的严格线性时间 Attention 层
- **Authors**: Sahil Joshi, Agniva Chowdhury, Amar Kanakamedala, Ekam Singh, Evan Tu, Anshumali Shrivastava
- **Affiliation**: Rice University
- **Venue**: ICLR 2026 (Poster)
- **Abstract & Innovations**: 用 sharpened angular similarity 替换指数 attention kernel，以 Gaussian random projections + soft locality-sensitive hashing 逼近输出，**序列长度与隐藏维度均严格线性**，从不物化 N×N attention 矩阵。
- **实验结果**: LM/MLM/图像任务上 ≤64K 长度匹配或超过 softmax baseline；单张 NVIDIA GH200 上**单次 forward-backward 处理 12M token**、Xeon CPU 上 75M token——FlashAttention-2/3 在同等硬件约 4M token 上限即无法完成一轮。
- **对比 prior**: 相对 FlashAttention 系（亚二次但内存近线性）把训练窗口推到"超大规模"量级。
- **Link**: https://arxiv.org/abs/2510.04008

### 1.6 arXiv — LLM Post-training / RL

#### Curriculum Reinforcement Learning Can Incentivize Reasoning Capacity in LLMs Beyond the Base Model
- **中文标题**: 课程强化学习可以把 LLM 推理容量推到 Base Model 之外
- **Authors**: Pengxiang Cai, Tianchen Fang, Xiaohan Li, Qingyuan Zeng, Guocong Li, Jintai Chen
- **Affiliation**: 未在 arXiv 页标注（高校团队）
- **Venue**: arXiv preprint (2026-06-21)
- **Abstract & Innovations**: 直接回应 NeurIPS'25 Best Paper Runner-up "Does RL Really Incentivize Reasoning Capacity" 的负结果：RLVR 只提升采样效率、不扩展推理容量。本文提出 **boundary-aware Curriculum RL** 闭环：(1) 用 pass@k 采样定位当前推理容量边界；(2) 对近/超边界问题注入针对性 teacher guidance；(3) RL 巩固后迭代外推边界。
- **实验结果**: 相对 base model 与 Vanilla RLVR，跨 Qwen/Llama/DeepSeek 基座平均 pass@256 提升 **+9.8 / +10.3 pp**，同时 pass@1 也提升——证明"课程结构"（而非对同一分布更强采样）才是移动边界的机制。
- **对比 prior**: 与 2504.13837（RLVR 容量上界论）构成同一问题两派；本文给出可操作正解。
- **Link**: https://arxiv.org/abs/2606.22317

### 1.7 arXiv — Sequential Modeling / Hybrid / Long Context

#### Kalman Delta Networks: Uncertainty-aware Associative Memory
- **中文标题**: Kalman Delta 网络：带不确定性的联想记忆
- **Authors**: Ngoc Bui, Tinglin Huang, Rex Ying
- **Affiliation**: Yale University
- **Venue**: arXiv preprint (cs.LG, 2026-09-07)
- **Abstract & Innovations**: 在线性 attention / Delta-rule 更新与 Kalman filtering 之间建立形式连接，给每个 memory node 配标定过的不确定性估计，使模型**按可靠性加权更新**而非把所有写入一视同仁；保持 constant-time memory 与线性复杂度。
- **实验结果**: 在 associative recall 与长程任务上优于 Delta-Net / Mamba 系 / HGRN 等 gated-delta-rule 与线性 attention 基线（具体 delta 数值未在摘要中给出，tentative）。
- **对比 prior**: 针对 gated-delta-rule / 线性 attention 的已知弱点（memory write 幅度一律平等）给出概率化解法。
- **Link**: https://arxiv.org/abs/2609.07816

#### Every Token Counts: Generalizing 16M Ultra-Long Context in Large Language Models (HSA-UltraLong)
- **中文标题**: 每一 token 都算数：泛化到 1600 万超长上下文的层次稀疏注意力
- **Authors**: Xiang Hu, Zhanchao Zhou, Ruiqi Liang, Zehuan Li, Wei Wu, Jianguo Li
- **Affiliation**: HSA 工作线（Ant Group / 上海 AI Lab 生态，arXiv 页未标注）
- **Venue**: arXiv preprint (2025-11-28)
- **Abstract & Innovations**: 把超长上下文重新定义为"需要稀疏性、随机访问、长度泛化的长期记忆"。提出 **Hierarchical Sparse Attention (HSA)** 内置于 sliding-window Transformer，训练 8B-A1B MoE（>8T tokens）；从 32K 训练窗口外推到 **16M token**，多数 in-context 检索任务 >90% 准确率。
- **对比 prior**: 在域内长度匹配 full-attention 基线，同时以亚二次成本支持 16M；toke-level 信息保持（HSA）优于纯粗粒度 sparse-prefix 方法的长程检索。
- **Link**: https://arxiv.org/abs/2511.23319

### 1.8 arXiv — Diffusion Language Models

#### PlaidQ: Distilled Continuous Diffusion Language Models Can Write Code in Few Steps—or One
- **中文标题**: PlaidQ：蒸馏的连续扩散语言模型可仅用 1~4 步写代码
- **Authors**: Fred Zhangzhi Peng, Kaiwen Zheng, Anru R. Zhang
- **Affiliation**: Duke University + Tsinghua University
- **Venue**: arXiv preprint (cs.LG, 2026-09-03)
- **Abstract & Innovations**: 0.7B 连续扩散 LM（从 Qwen3-0.6B 蒸馏、Nemotron 预训练语料），用 sequence-level state-space 可蒸馏参数化 + 步数与 teacher-step 对齐的流程，把 16 步蒸馏的质量压缩到 **4 步甚至 1 步**。
- **实验结果**: 1–4 步区间 pass@k / perplexity 保持竞争力（确切单步数字受限，tentative）。
- **对比 prior**: 此前扩散 LLM 蒸馏在低步数下创造性/自由生成退化；PlaidQ 证明对代码任务 low-step 也能保住"zero-shot 创作"。
- **Link**: https://arxiv.org/abs/2609.04531

### 1.9 arXiv — Code Execution Prediction / Benchmarks

#### SWE-Bench Pro Verified: A Reliable Benchmark for Software Engineering Agents
- **中文标题**: SWE-Bench Pro Verified：稳健的软件工程 Agent 基准
- **Authors**: Pujun Zheng, Zixin Shang, Shufan Jiang, Wenhui Tian, Dongsheng Zhu, Zerun Ma, Dingbo Yuan, Qi Zhang
- **Affiliation**: 未在 arXiv 页标注
- **Venue**: arXiv preprint (cs.AI / cs.SE, 2026-09-08)
- **Abstract & Innovations**: 分析指出 **SWE-Bench Pro 被 reward hacking（gold solution / 隐藏评测信息泄漏）与任务质量问题（误导性 problem statement、错误 scoped tests）破坏**。给出 verified 版本：反泄漏护栏（在不妨碍正常 agent 的前提下清除主要泄漏通道）+ 最小任务修正。
- **实验结果**: 在 verified split 上**部分模型表现显著低于此前报告值**——即此前 SWE-Bench Pro 头条数字高估了真实软件工程能力。
- **对比 prior**: 与 2609.08149 同期"评测修复"线（另见 SWE-Bench Verified 原论文）一致：基准可信度进入主动审计时代。
- **Link**: https://arxiv.org/abs/2609.08149

#### Tasks over Application Manuals: Revealing Gaps in Long-Horizon Procedural Reasoning for Language Models (TAM)
- **中文标题**: 应用手册上的长视界程序性推理任务（暴露 LLM 推理差距）
- **Authors**: Utkarsh Soni, Syed Shariyar Murtaza, Yifan Nie, Sachin Chandrasekhar, Eugene Wen
- **Affiliation**: 未在 arXiv 页标注（关联 ACM DOI: 10.1145/3799682.3841039）
- **Venue**: arXiv preprint (cs.CL, 2026-09-11)
- **Abstract & Innovations**: 新基准 **TAM**：真实世界人工核验任务——ICD-10-CM 临床编码与美国联邦量刑，每项需遵循数万条规则的手册并做相互依赖的多步执行。GPT-5 在 RAG / ReAct / agent-harness 基线下，ICD-10-CM exact match 仅 **1%**、量刑 **15.5%**。
- **对比 prior**: 短视界 multi-hop 基准大大高估 LLM 在规则化程序性任务上的可靠性。
- **Link**: https://arxiv.org/abs/2609.13005

### 1.10 arXiv — LLM-as-a-Judge / Evaluator Validity

#### Towards Reliable Multilingual LLMs-as-a-Judge: An Empirical Study (mJudge)
- **中文标题**: 迈向可靠的多语言 LLM-as-a-Judge：实证研究
- **Authors**: Irune Zubiaga, Aitor Soroa, Rodrigo Agerri
- **Affiliation**: HiTZ Center, University of the Basque Country (UPV/EHU)
- **Venue**: arXiv preprint (2026-05-27)
- **Abstract & Innovations**: 系统研究跨 英/西/巴斯克（高/中/低资源）构建 judge：对比指令翻译、单语 vs 多语监督、模型规模。关键 trade-off：**域内数据下微调的小模型可达闭源水平；域外则大型零样本更强，且用域外数据微调反而掉点**。发布 mJudge 套件。
- **对比 prior**: 多数 LLM-as-a-Judge 工作英语中心或忽略低资源域内/域外区分；本文量化两个 regime 的适用条件。
- **Link**: https://arxiv.org/abs/2605.28710

#### Lower-Resource, Higher Scores: Language Bias in LLM Evaluators
- **中文标题**: 资源越少、分数越高：LLM 评测器的语言偏差
- **Authors**: Ej Zhou, Lucas Resck, Zheng Hui, Anna Korhonen
- **Affiliation**: University of Cambridge (Language Technology Lab)
- **Venue**: arXiv preprint (2026-07-16, v3 2026-08)
- **Abstract & Innovations**: 证明多语言评测器（reward model + LLM-as-a-Judge）对**语义相同的 23 种语言内容给出系统性不同分数**，且偏差与资源水平强相关——**低资源语言被更宽松地打分**。8 个开放权重评测器与前沿 judge 一致；即使控制不确定性/难度，语言身份仍是显著预测因子。安全含义：有害内容在低资源语言下更易通过 filter。
- **实验结果**: pairwise accuracy >90% 仍可对应高达 **43% 的跨语言通过率差异**。
- **对比 prior**: 此前验证只看 pairwise accuracy（M-RewardBench / M-Prometheus 线）；本文论证 pairwise accuracy 远远不够，主张新增跨语言 score-consistency 指标。
- **Link**: https://arxiv.org/abs/2607.14480

#### FAPO: Fully Automated Prompt Optimization of Multi-Step LLM Pipelines
- **中文标题**: FAPO：多步 LLM 流水线的全自动 Prompt 优化
- **Authors**: Paul Kassianik, Baturay Saglam, Huaibo Zhao, Blaine Nelson, Supriti Vijay, Aman Priyanshu, Amin Karbasi
- **Affiliation**: 若干作者关联 OpenAI（arXiv 页未声明，**未经核验**）+ 学术合作（Karbasi — Yale）
- **Venue**: arXiv preprint (2026-06-17)
- **Abstract & Innovations**: 在标准化代码库内自动化优化多步 LLM 流水线（retrieval + reasoning + formatting）：评估 → 检查中间步 → 诊断失败 → 验证变体。**先试 prompt 编辑；仅当归因显示结构性瓶颈时才升级到链结构改动**。
- **实验结果**: 18 个 model-benchmark 对比中 **15 个超过 GEPA 基线（平均 +14.1 pp）**；需要结构升级的 6 个对比 **+33.8 pp**；安全任务亦提升（CTIBench-RCM 上含 GPT-5 的模型 +4.0~7.1 pp）。
- **对比 prior**: OPRO/APE/GEPA 等自动 prompt 优化只改 prompt、抓不住跨步交互；FAPO 的归因 + 受限结构编辑补上链级瓶颈。
- **Link**: https://arxiv.org/abs/2606.19605

### 1.11 arXiv — Generative Models / World Models / Video

#### Video Generation with Predictive Latents (PV-VAE)
- **中文标题**: 带预测性 Latent 的视频生成（PV-VAE）
- **Authors**: Yian Zhao, Feng Wang, Qiushan Guo, Chang Liu, Xiangyang Ji, Jian Zhang, Jie Chen
- **Affiliation**: ByteDance Seed + 北京大学 + 清华大学
- **Venue**: arXiv preprint (2026-05-04)
- **Abstract & Innovations**: 把 JEPA 式预测世界建模原则嵌入视频 VAE 训练：predictive reconstruction 目标联合重建视觉细节并预测未来状态，使 latent 对下游视频生成更具时间动力学与运动理解。
- **实验结果**: 相对 Wan2.2 视频 VAE 基线 UCF101 上 **收敛快 52%**、**FVD 改善 34.42**。
- **对比 prior**: 传统视频 VAE 只做重构；PV-VAE 把"预测未来"显式编入 latent 学习。
- **Link**: https://arxiv.org/abs/2605.02134

#### PhiZero: A World Model Built Around Physical Language
- **中文标题**: PhiZero：围绕"物理语言"构建的世界模型
- **Authors**: Shuyao Shang, Yuqi Wang, Ruopeng Gao, Xu Chen, Tieniu Tan, Lue Fan, Zhaoxiang Zhang
- **Affiliation**: 中科院自动化所 (CASIA) + 合作机构；初始 reasoner 来自 Qwen3-VL
- **Venue**: arXiv preprint (2026-07-30)
- **Abstract & Innovations**: "reason-then-render" 物理世界模型。**Physical Language Tokenizer**（transition-level Q-Former + FSQ 量化 + diffusion decoder）把视频状态迁移压缩成紧凑离散"物理语言"，自监督学自 in-the-wild 视频；**Physical Language Reasoner**（自回归 VLM）在该空间预测演化，再由 diffusion decoder 渲染——动力学变得显式、可检查、可控制，而非混在像素预测里。
- **实验结果**: Physics-IQ Verified 物理结果保真度最佳（IQ-Score 41.2 vs Cosmos3-Super 39.5）；PhyGround Overall 2.97 (vs Wan2.2-14B 2.95)；WorldModelBench 8.19；在 IntPhys2 / LikePhys / YoCausal 上物理合理性判别优于 Veo3.1、Hunyuan-Video、Sora 2 等。
- **对比 prior**: 像素域视频/扩散世界模型动力学隐式；PhiZero 把动力学显式化为离散符号层。
- **Link**: https://arxiv.org/abs/2607.28624

---

## 2. 会议全景：本 wiki 已覆盖论文交叉引用 (Already Covered — Cross-Reference Panorama)

> 以下论文均已在既有 wiki 页面完整收录（含数字与对比），本版**不重复展开**，仅作导航。ID 已在 wiki/ 中 grep 验证 ≥1 命中。

| Venue / 主题 | 论文 | 既有收录位置 |
|---|---|---|
| NeurIPS 2025 Best Paper | **Gated Attention** (Alibaba/Qwen, 2505.06708) | [[synthesis/2026-09-04/conference-digest]] · [[synthesis/2026-08-05/conference-digest]] |
| NeurIPS 2025 Runner-up | **Does RL Really Incentivize Reasoning Capacity** (Tsinghua, 2504.13837) | [[synthesis/2026-09-04/conference-digest]] + 本文 1.6 对比 |
| ICLR 2026 Outstanding | **LLMs Get Lost In Multi-Turn** (MSR/Salesforce, 2505.06120) | [[synthesis/2026-07-14/conference-digest]] |
| ICLR 2026 | **Mamba-3** (CMU/Princeton, 2603.15569) | [[synthesis/arxiv-broad-2026-05-25]] · [[synthesis/2026-09-13/conference-digest]] |
| ICML 2026 | SMET 稀疏训练 (2606.00888) · Faster-Than-Flash 长上下文解码 (2609.00097) | [[synthesis/2026-09-02/conference-digest]] · [[synthesis/2026-06-24/arxiv-ai-search]] |
| CVPR 2026 | **DeltaTok / DeltaWorld** (Amazon, 2604.04913) · **VideoWorld 2** (ByteDance, 2602.10102) | [[synthesis/2026-09-13/conference-digest]] |
| DeepMind 视觉生成 | **Vision Banana** (2604.20329) · **GenCeption** (2607.09024) | [[synthesis/2026-06-06/arxiv-paper-check]] · [[synthesis/2026-08-05/conference-digest]] |
| KDD/AdKDD 2026 | **FAT** (Alibaba, 2511.12081) · **CADET** (LinkedIn, 2602.11410) | [[synthesis/2026-09-13/conference-digest]] · [[synthesis/2026-09-02/conference-digest]] |
| SIGIR 2026 | **GenRec** (JD, 2604.14878) · **DANet** (Alibaba, 2607.12578) | [[synthesis/2026-09-05/conference-digest]] · [[synthesis/2026-07-29/arxiv-daily]] |
| RecSys 2025/26 | **GRACE** (Walmart, 2507.14758) · **SequenceO1 100K** (ByteDance) | [[synthesis/2026-09-13/conference-digest]] · [[synthesis/2026-09-11/arxiv-daily]] |
| WWW 2026 | **Douyin 10K STCA** (2511.06077) · **ReST** (2609.01240) · **LBM 自动出价** (2603.05134) | [[synthesis/2026-09-13/conference-digest]] · [[synthesis/2026-09-02/conference-digest]] |
| CIKM (25/26) | **EGA-V1** (Meituan) · **MARM** (Kuaishou) · **NMRL** (Taobao, 2608.24091) | [[synthesis/2026-09-13/conference-digest]] · [[synthesis/2026-08-30/conference-digest]] |
| 生成式广告/CTR | **GR4AD** (Kuaishou, 2602.22732) · **LLM-HYPER** (Alibaba, 2604.12096) · **EST** (Alibaba, 2602.10811) | [[synthesis/arxiv-broad-2026-05-25]] · [[synthesis/2026-06-26/arxiv-ai-search]] · [[wiki/papers/ctr/est]] |
| 工业生成式推荐 | **TGR** (Tencent, 2609.00986) · **TokenMixer-Large** (ByteDance, 2602.06563) | [[synthesis/2026-09-02/conference-digest]] · [[synthesis/2026-06-10/conference-digest]] |
| 技术报告 | **DeepSeek-V4** (2606.19348) · **Nemotron 3 Super** (NVIDIA, 2604.12374) | [[synthesis/2026-09-02/tech-report-digest]] · [[synthesis/2026-09-02/tech-report-digest]] |
| 同日汇总 (09-14) | SeqMoE 专家卸载 (2609.12978) · Terminal-Agent RL T1 (2609.11042) · Mu-GRPO (2605.17570) | [[synthesis/2026-09-14/arxiv-ai-search]] · [[synthesis/2026-09-12/arxiv-daily]] · [[synthesis/2026-09-13/conference-digest]] |
| 相邻主题 (已收录) | PrEx 出口码预测 (2609.00579) · 隐式混合架构理论 (2609.02986) · attention 混合分析 (2606.15378) · dLLM 轨迹级推测解码 (2608.27514) | 09-13 conference-digest · 09-04 arxiv-paper-check · 07-06 arxiv-ai-search · 08-31 arxiv-ai-search |

---

## 3. Cross-Venue Trends — 跨会议趋势

1. **"对象级预测"成代码/评测新范式**：PrEx（正式语义→exit code）→ SWE-Bench Pro Verified（反泄漏修正）→ TAM（长手册程序性推理）构成连续谱系：评估 Agent 与代码模型时，**程序语义判断比 trace 生成更难，也是更大的失败点**。
2. **评测器可信度 = 新的前沿**：mJudge / Language-Bias / FAPO / SimulatorArena 同周出现——pairwise accuracy、单一语言、人工幻觉式基准三类暴露共同指向：**"谁来评评测者"成为 2026 下半年显性主题**。
3. **世界模型朝"显式物理中间态"收敛**：GenieDrive（occupancy）、PhiZero（物理语言 token）、RAYNOVA（ray space 无 3D 先验）、VideoWorld 2（latent dynamics）+ PV-VAE（predictive latent）——行业共识：**不要像素端到端，要在 latent 里先建模动力学**。
4. **KV cache / 长上下文进入"复用 + 压缩 + 近似"三位一体阶段**：C²KV（复用压缩）、RACE（线性近似）、HSA-UltraLong（稀疏层次）、SeqMoE（专家卸载）——推理成本控制从 kernel 优化转向**缓存管理即建模**。
5. **RL 容量之争出现正解**：Curriculum RL 给出"课程结构移动能力边界"的实证反例，与 Mu-GRPO、Demystifying RLPT 等机理研究互相咬合。

---

## 4. Dedup / 检索说明

- 本轮为 **web 检索驱动的增量版**：arXiv ID 逐条 grep 验证（wiki/ 全库，含 log/index），仅 0 命中论文进入"完整详述"；≥1 命中者收进第 2 节交叉引用全景。
- 会议 proceedings 可得性：CVPR 2026 / KDD 2026 / ACL 2026 / EMNLP 2025 / ICLR 2026 / NeurIPS 2025 论文经 arXiv "accepted at" 注释或 DOI 交叉验证；**AAAI 2026** 本轮未在目标实验室找到可核验的新工业/视频类论文；**RecSys 2025** 本次无新增（GRACE 等已收录）；SIGIR/WWW/CIKM 新增均已在更早 digest 处理。
- 未找到 OpenAI / Meta 本轮确证的新论文（Exclude 空洞已如实标注，不臆造）。