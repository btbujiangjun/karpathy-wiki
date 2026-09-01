---
title: "Conference & arXiv Daily Digest — 2026-09-01"
type: synthesis
created: 2026-09-01
updated: 2026-09-01
sources: []
tags: [conference-digest, icml-2026, iclr-2026, aaai-2026, neurips-2025, cvpr-2026, kdd-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2025, recsys-2025, recommendation, llm, agents, ctr, advertising, generative-models, sequential-modeling, games, world-models, benchmarks, daily-digest]
---

# Conference & arXiv Daily Digest — 2026-09-01

> Comprehensive survey of recent papers from top ML/AI conferences (2025–2026 cycle) and latest arXiv preprints (late-August 2026 wave, IDs ~2608.17xxx–2608.27xxx). Organized by venue and category. Focus on papers from top labs: Google DeepMind/Google Cloud AI, OpenAI, Meta AI/Meta, Microsoft Research, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, Netflix, NVIDIA, Anthropic, Apple, Amazon, and top academic labs.

---

## 🏭 概述 Overview

本期收录 **45+** 篇最新论文，按专题组织：**LLM 后训练与 RLVR / RL 信用分配**、**Agent 系统与 Agentic RL**、**推荐 / 广告 / CTR / 序列建模（工业落地密集）**、**世界模型与游戏**、**生成模型**、**基准评测与会议趋势（ICLR 2026 / NeurIPS 2025）**。

热门主题：
1. **RL 信用分配（Credit Assignment）成为后训练核心战场** —— 大量工作从“奖励证据”转向“运输算子”（CompPO/CCT architecture-aware credit transport）、step-level 审计（Credit Without Ground Truth）、self-reflective dense reward（SRPO）、value function 回归（Le Critique / Privileged Value Functions）。
2. **Agentic RL 密集发力** —— Google Cloud（EnvHarness 环境重塑性）、开源 harness（Prime Agent）、自我蒸馏（AHEAD）、经验蒸馏（EDGE）、环境内化（EnvACE）、多智能体拓扑可解释（E2-Explainer / Consilience / DeAR / ExRole）。
3. **生成式推荐工业落地成为绝对主流** —— Kuaishou（PushDualGen、HRPO、UniMoMo、动态 SID codebook、GR4AD）、Tencent（OneRanker、STAR、UniDot KDD Cup）、Baidu（GRAB）、Alibaba（CRRN）。学术侧 ICML 2026 亦有多篇（CausalDPO、ProRL、CFlower、RSIR、Tournament Graphs）。
4. **世界模型从“生成视频”走向“可执行/可推理”** —— Code World Model、Code-as-World、Twin（test-time 数字孪生）、WorldMind（NPC 状态解耦）、WALL-SS（long-horizon 机器人仿真）、LDR（外推到 OOD 的动力学推理）、ForgeWM（few-step 因果蒸馏）。
5. **CTR 规模化从“参数堆量”转向“结构化表达力”** —— FAT（Field-Aware Transformer，KDD'26）给出基于 Rademacher 复杂度的 CTR Scaling Law。

---

## 🧠 LLM 后训练、RLVR 与信用分配（LLM Post-training, RLVR & Credit Assignment）

### 1. SRPO: Self-Reflective Policy Optimization for Long-Horizon Reasoning
- **中文标题**: SRPO：面向长程推理的自反思策略优化
- **作者**: Galleons2029 团队（详见 arXiv）
- **机构**: 学术/开源团队
- **Venue**: arXiv preprint (2608.23493, Aug 24 2026)
- **arXiv**: [2608.23493](https://arxiv.org/abs/2608.23493)
- **摘要与创新**: 把自反思（self-reflection）作为稠密奖励生成机制。LLM 分析自己完整轨迹，把错误提炼为"reflection patches"，再用反思条件化的 teacher 对 student on-policy rollouts 打分生成 token 级稠密训练信号。无需外部 critic、reward model 或更大 teacher。引入 reset-with-memory 机制，"training with reflection, inference without"。
- **实验结果**: Qwen3-8B 在 AIME'24 达 73.3%，仅用 scaled SFT 训练 FLOPs 的 8%；WebShop 64.7%、ALFWorld 76.8%、SWE-Bench-Lite 31.2%；约比 GRPO 少 3.8× 总 FLOPs。
- **对比**: 相对 Reflexion/SCoRe/R3L/RISE 等反思基线及 72B 外部 teacher 蒸馏，以更少算力达到或超越；把稀疏终点奖励（O(1) bits）转为稠密 token 级信号（O(T) bits）。

### 2. CompPO: Let Credit Follow Computation — Architecture-Aware Credit Transport for LLM RL
- **中文标题**: 计算条件化信用分配：面向 LLM RL 的架构感知信用传输
- **作者**: 详见 arXiv
- **机构**: 学术/工业界（inferred）
- **Venue**: arXiv preprint (2608.21501, Aug 2026)
- **arXiv**: [2608.21501](https://arxiv.org/abs/2608.21501)
- **摘要与创新**: 提出计算条件化信用传输（CCT）框架——用策略内部计算的 detached 统计量参数化因果核（kernel），把下游价值经 rollout 传输。CompPO 把 attention concentration 映射为有界 per-token 保留门（retention gate），用于一步 bootstrap 与 path-dependent GAE 轨迹（Comp-GAE），并设计对齐 critic（TAC）复用 actor 隐状态。常数门退化为固定系数 GAE。任务奖励与 clipped PPO 目标不变。
- **实验结果**: 5 个 Qwen3-4B seeds 上 CompPO 达 61.4% hold-out 准确率 vs GRPO 53.8%；PPO stress grid 中 10/12 runs 稳定 vs 3/12；冻结评估超 GRPO 4.3（Qwen3-4B）与 3.9（Llama-3.1-8B）greedy pass@1 点。
- **对比**: 相对 fixed-discount GAE 与 group-relative 广播，首次把策略内部计算作为信用传输的一等变量。

### 3. Le Critique: Privileged Value Functions for LLM Reinforcement Learning
- **中文标题**: Le Critique：面向 LLM RL 的特权价值函数
- **作者**: 详见 arXiv
- **机构**: 学术/工业界（inferred）
- **Venue**: arXiv preprint (2608.16739, Aug 17 2026)
- **arXiv**: [2608.16739](https://arxiv.org/abs/2608.16739)
- **摘要与创新**: 论证价值函数（critic）在一次 rollout 采样之外提供 token 级信用却不受 straggler 与 off-policy 问题困扰。提出两种策略：(1) **Privileged Value Functions (Pvf)**——注入额外任务相关 token 级信号而不偏置策略目标；(2) **Tether**——根据价值函数准确度在 group-relative 与 value baseline 间自适应插值。
- **实验结果**: 多个推理任务上一致超越标准 value function baseline，与 mean-baseline GRPO 竞争或超越。
- **对比**: 相对 GRPO（仅序列级信用、straggler 阻塞训练）与 critic-free 方法，重新审视 critic 的效用；相对 EVPO（硬切换）用平滑插值。

### 4. CoKL: Plasticity-Preserving KL Regularization for Capability Retention in LLM RL
- **中文标题**: CoKL：面向能力保持的保持可塑性 KL 正则
- **作者**: Lumina04 团队（详见 arXiv）
- **机构**: 学术/工业界
- **Venue**: arXiv preprint (2608.01743)
- **arXiv**: [2608.01743](https://arxiv.org/abs/2608.01743)
- **摘要与创新**: 标准全策略 KL 正则约束整条响应分布，可能不必要地限制探索。CoKL（Correctness-Conditioned KL）把保持约束从全输出分布收窄到"正确性条件化分布"，解耦总正确概率与正确响应间的相对概率分配，避免在参考策略不完美时产生严格最优正确性 gap。
- **实验结果**: 多解环境与持续后训练中多个规模下，CoKL 在目标任务改进与既有能力保持间取得更优平衡。
- **对比**: 相对 full-policy forward/reverse KL（过多限制）与无 KL（能力遗忘风险），提供精准约束。

### 5. Efficient RLVR Scheduling via Graph-Structured Online Difficulty Estimation
- **中文标题**: 基于图结构在线难度估计的高效 RLVR 调度
- **作者**: 详见 arXiv
- **机构**: 学术（inferred）
- **Venue**: arXiv preprint (2608.17941, Aug 18 2026)
- **arXiv**: [2608.17941](https://arxiv.org/abs/2608.17941)
- **摘要与创新**: RLVR 依赖昂贵 rollout 探索，均匀分配探索预算低效。提出可插拔的基于图的在线难度估计器，在相关样本间共享 rollout 反馈并持续更新难度估计。构建 difficulty-aware sample graph（语义/推理相似性），用 Potts prior 鼓励邻居共享 latent difficulty 状态，Beta-Binomial 聚合，在线 mean-field 变分算法更新。
- **实验结果**: 多个 base model、RL scheduler、benchmark 上在匹配 rollout 预算下取得更好性能。
- **对比**: 相对 dedicated probing（高开销）与 history-based 估计（冷启动/陈旧），利用样本间关系缓解冷启动与陈旧。

### 6. Continual Reasoning Gym: Diagnosing and Harnessing Shared Reasoning in Continual RLVR
- **中文标题**: Continual Reasoning Gym：诊断与利用持续 RLVR 中的共享推理
- **作者**: 详见 arXiv
- **机构**: 学术（inferred）
- **Venue**: arXiv preprint (2608.18574)
- **arXiv**: [2608.18574](https://arxiv.org/abs/2608.18574)
- **摘要与创新**: 研究持续 RLVR（任务逐批到达更新现有模型）能否达到联合训练（MTRL）性能。引入 CRG 环境（5 条任务序列、30 阶段、文本+视觉推理）。发现 Sequential RLVR 遗忘温和但最终性能低于 MTRL；识别"shared reasoning"（可迁移推理结构）。提出 **Continual Prompt Replay (CPR)**——重放先前任务 prompt 并用当前策略重新生成响应。
- **实验结果**: CPR 平均 CTM 1.03（Seq. RLVR 为 0.88），是唯一达到 MTRL 级性能的持续学习方法。
- **对比**: 相对 replay sample（旧轨迹）提升依赖用当前策略重新生成响应（CPR 63.3% vs sample replay 47.5%）。

### 7. GCPO: Diagnosing and Constraining Subspace Geometry in Rollout RL for LLMs
- **中文标题**: GCPO：诊断与约束 rollout RL 的子空间几何
- **作者**: 详见 arXiv
- **机构**: 学术（inferred）
- **Venue**: arXiv preprint (2608.11674)
- **arXiv**: [2608.11674](https://arxiv.org/abs/2608.11674)
- **摘要与创新**: GRPO 类 on-policy 方法常遭训练不稳定、跨任务退化、响应长度膨胀。提出 Principal-Subspace Overlap（对预训练权重主奇异子空间的维度校正度量），发现 transient spikes 先于性能退化。提出 GCPO 用硬双边正交投影约束更新到互补子空间。
- **实验结果**: Qwen3-8B / GLM4-9B 上数学、代码、工具使用任务一致超越 GRPO、DAPO、GSPO，最高 +27.69 点（vs base）/+2.37 点（vs 最强基线）。
- **对比**: 相对只从 objective/输出行为干预的方法，从参数更新几何角度诊断并预防不稳定。

### 8. Policy Iteration with Human Feedback (PIHF): Bringing Post-Training RL to In-context Learning
- **中文标题**: PIHF：把后训练 RL 引入上下文学习（罕见病诊断）
- **作者**: 详见 arXiv
- **机构**: 学术/临床（inferred）
- **Venue**: arXiv preprint (2608.16831, Aug 16 2026)
- **arXiv**: [2608.16831](https://arxiv.org/abs/2608.16831)
- **摘要与创新**: 用预训练 LLM 作为固定权重执行底座，把持久化修订放到版本化自然语言策略+工具集。LLM critic 与临床专家审查完整推理/工具轨迹，定位反复失败、形成候选修订；专家保留 admission/rollback 权。Recall@1/Recall@5 做结果验证。
- **实验结果**: 一个专有执行器与三个 open-weight 执行器（3–49B）上 Recall@1 提高（GPT-5.4 +32.7 pp、Qwen3.6-35B +31.1 pp）；liteOdyssey 研究 Recall@1 从 26.5%→59.3%（1,243 案例）。
- **对比**: 相对固定权重 prompt-only ICL，把策略修订持久化到外部 artifact 并跨 backbone 复用。

### 9. RISE-RL: Rubric-Informed Selective Exploration for Open-Ended RL
- **中文标题**: RISE-RL：面向开放式强化学习的选择性探索
- **作者**: 详见 arXiv
- **机构**: 学术/工业界（inferred）
- **Venue**: arXiv preprint (2608.09123)
- **arXiv**: [2608.09123](https://arxiv.org/abs/2608.09123)
- **摘要与创新**: 现有 rubric-based RL 把细粒度标准级反馈压成标量奖励，难以针对持续能力缺口。RISE-RL 用反复错过的 rubric 标准诱发特权轨迹；仅保留完整 rubric 奖励高于自然 rollout 均值的轨迹，再在原始 prompt 下重评，通过独立辅助目标优化引导信号，收益递减后移除。
- **实验结果**: 4B/14B 模型在写作、聊天、健康、科学上无引导评测下最高均分；相对 Rubric-RL 平均 +1.3（4B）/+3.3（14B），CreativeWriting-V3 +6.0。
- **对比**: 相对把引导轨迹混入共享 group-relative 目标的耦合变体，独立辅助目标更优。

### 10. Ahead: Adaptive Hindsight with Environment-Augmented Distillation for Agentic RL
- **中文标题**: AHEAD：面向 Agentic RL 的环境增强蒸馏的自适应后见
- **作者**: 详见 arXiv
- **机构**: 学术（inferred）
- **Venue**: arXiv preprint (2608.24114, Aug 25 2026)
- **arXiv**: [2608.24114](https://arxiv.org/abs/2608.24114)
- **摘要与创新**: 针对多轮 agent RL 的轨迹级奖励无法识别成败步骤问题。AHEAD 为不同类型步骤匹配不同监督来源：teacher 在所有步骤接收环境反馈（grounded dense signal），在错误步骤额外接收 LLM 生成的纠正 hint。对标准 GRPO 改动极小。
- **实验结果**: ALFWorld、WebShop、Search-based QA、3 个模型规模上，7B 相对 GRPO 任务成功率 +13.3（ALFWorld）/ +11.0（WebShop）。
- **对比**: 相对 uniform privileged information 方法（SDAR/RLSD/Skill-SD），按步骤类型分配异构监督来源。

<!-- pagebreak -->

---

## 🤖 Agent 系统与 Agentic RL（Agent Systems & Agentic RL）

### 11. EnvHarness: Awakening Static Worlds for Agent Learning（Google Cloud AI Research）
- **中文标题**: EnvHarness：唤醒静态环境用于 Agent 学习（Google Cloud）
- **作者**: Chengsong Huang, Zifeng Wang, Rujun Han, Jun Yan, Yanfei Chen, Zoey CuiZhu, Ke Jiang, Peng Xia, Han Yu, Yufan Zhuang, Yifei Ming, Jiaqi Pan, Bhavana Dalvi Mishra, Jiaxin Huang, Burak Gokturk, Tomas Pfister, Chen-Yu Lee
- **机构**: Google Cloud AI Research（+ UNC Chapel Hill、WashU）
- **Venue**: arXiv preprint
- **arXiv**: [2608.19880](https://arxiv.org/abs/2608.19880)
- **摘要与创新**: LLM agent 学习的环境手工构建且静态，对 agent 弱点视而不见。EnvHarness（Environment Harness）是可编程的插拔组件层，包装静态环境以重塑其行为而不改底层逻辑，保留原 verifier。EnvRigger 把目标策略当黑盒，观察执行轨迹合成 EnvHarness 组件定位缺陷，并用新 rollout 验证。
- **实验结果**: 5 个 benchmark（4 个域）上超越原始环境与域特定环境生成管线，hold-out 实例最多 +9.0 点、执行步骤 -9.8%。
- **对比**: 相对 hand-built 静态 env 与一次生成静态 env 的方法，实现策略与环境的持续共演化。

### 12. Prime Agent: A Self-Improving RLM Harness
- **中文标题**: Prime Agent：自改进的递归语言模型 harness
- **作者**: PrimeIntellect 团队
- **机构**: PrimeIntellect（开源）
- **Venue**: arXiv preprint (2608.23552, Aug 24 2026)
- **arXiv**: [2608.23552](https://arxiv.org/abs/2608.23552)
- **摘要与创新**: 开源长程评估与 coding-agent harness。持久 IPython REPL 遵循 Recursive Language Model 抽象做程序化上下文处理与 test-time compute；Continual Harness 跨轨迹保存历史/记忆/技能/prompt/subagent 规格；递归 subagent 通过直连 agent-to-agent 通信协调。
- **实验结果**: ARC-AGI-3 RHAE Best@1 从 30% 提到 95.5%；在长上下文编码、GPU-kernel 生成、emulator 构建、autonomous nanoGPT speedrun 上匹配或超越主流 harness；Factorio 上支持持续技术推进与并行 subagent。
- **对比**: 相对充当"膜"的标准 harness，通过可表达原语让固定模型扩展可达策略集。

### 13. EDGE: Experience-Distillation for Guided Exploration in Agentic RL
- **中文标题**: EDGE：面向 Agentic RL 引导探索的经验蒸馏
- **作者**: xvolcano02 团队
- **机构**: 学术（inferred）
- **Venue**: arXiv preprint (2608.21946)
- **arXiv**: [2608.21946](https://arxiv.org/abs/2608.21946)
- **摘要与创新**: GRPO 类结果导向 RL 中轨迹里的可复用探索模式在一次更新后被丢弃。EDGE 把检索到的经验当作临时 training-time scaffold，逐步内化到参数化策略。把每组 rollout 分成经验条件化/经验无关轨迹估计并只接受正边际增益，再用 reverse-KL 蒸馏到 base policy；共演化经验银行从新兴失败模式合成引导并修剪过时条目。
- **实验结果**: 具身、web、search-based QA 上相对强 RL baselines 最高 +12.5 点，无 inference-time scaffold 或专属 reflector 仍有效。
- **对比**: 相对 EMPO2/SKILL0（内存/技能回收），用配对 rollout 增益验证并蒸馏在线经验。

### 14. EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic RL
- **中文标题**: EnvACE：通过世界预演内化环境动力学
- **作者**: 详见 arXiv
- **机构**: 学术/工业界（inferred）
- **Venue**: arXiv preprint (2608.06197)
- **arXiv**: [2608.06197](https://arxiv.org/abs/2608.06197)
- **摘要与创新**: 主张 agent 策略不只应行动还应建模环境如何响应其行动。EnvACE 给策略两个角色——与 env 交互的 actor 与提供反馈的 env，无需真实环境交互，把 action-induced response 内化进参数。
- **实验结果**: FinMCP-Bench TF1 46.78%（超 EnvScaler-8B +3.10%、AWM-8B +4.28%），工具精度 54.04%。
- **对比**: 相对依赖真实环境交互或外部模拟器的方法（EnvScaler/AWM），世界预演提供更可扩展的范式。

### 15. E2-Explainer: Explainable Communication Topologies for LLM-based MAS via Causal Inference
- **中文标题**: E2-Explainer：基于因果推断的多智能体通信拓扑可解释
- **作者**: 详见 arXiv
- **机构**: 学术（inferred）
- **Venue**: arXiv preprint (2608.12921, Aug 13 2026)
- **arXiv**: [2608.12921](https://arxiv.org/abs/2608.12921)
- **摘要与创新**: 现有拓扑生成方法用黑盒优化只靠任务奖励，难以解释边选择。E2-Explainer 是 model-agnostic 框架，把拓扑解释建模为因果归因：识别受边级"任务保持"证据支持的紧凑通信子图。用 Granger 式目标度量 masking 各通道如何改变任务结果与回答稳定性，再蒸馏成 amortized explainer。
- **实验结果**: 6 benchmark（AQuA/GSM8K/MultiArith/SVAMP/MMLU/HumanEval）上把 token 用量减少 10.6%–44.0%，精度在 16/24 组合提升；跨未见拓扑生成器可迁移（+0.44–0.58 精度、成本降 20.1%–25.6%）。
- **对比**: 相对 G-Designer/ARG/OFA-MAS/AgentPrune 等黑盒拓扑生成，提供 post-hoc 因果解释并可剪枝冗余通信边。

### 16. Consilience: Conformally Calibrated Communication Control for Hidden-Profile Multi-Agent Reasoning
- **中文标题**: Consilience：面向隐藏信息多智能体推理的保形标定通信控制
- **作者**: 详见 arXiv
- **机构**: 学术（inferred）
- **Venue**: arXiv preprint (2608.20564, Aug 20 2026)
- **arXiv**: [2608.20564](https://arxiv.org/abs/2608.20564)
- **摘要与创新**: 隐藏信息设置下每个 agent 只持部分证据。Consilience 是 inference-time 编排框架，每轮用紧凑状态（不确定性、分歧、证据增益、冗余、过早共识）选择通信干预（挑战/澄清/寻求证据/路由）。核心是 round-wise 保形标定，提供分布无关、有限样本保证：每轮 one-step regret 有界于标定阈值。
- **实验结果**: 12 个 open/closed 模型上 HiddenBench + GroupTravelBench，决策精度与通信效率优于固定/非结构化讨论，有时超全信息基线。
- **对比**: 相对 round-robin 与无约束 LLM orchestrator，提供通信动作适当性的统计保证。

### 17. DeAR: Decentralized Agentic Reasoning via Capability Grounding and Collaborative Thought Navigation
- **中文标题**: DeAR：基于能力落地与协作思维导航的去中心化 Agentic 推理
- **作者**: 详见 arXiv
- **机构**: 学术（inferred）
- **Venue**: arXiv preprint (2608.17282)
- **arXiv**: [2608.17282](https://arxiv.org/abs/2608.17282)
- **摘要与创新**: 从中心化协议转向自治点对点协作。三大机制：(1) 去中心化能力落地（agent 从技术报告/model card 的可验证基准落地能力，而非静态角色）；(2) 思维图导航（根据查询需求与 agent 置信度动态构建推理路径）；(3) 拓扑更新（自适应纠错）。
- **实验结果**: 9 个多模态/文本 QA benchmark 一致超越近期基线。
- **对比**: 相对 AutoGen/AgentVerse/DyLAN 等中心化框架（路由瓶颈、静态角色、信息聚合错误），去中心化自适应协作。

### 18. HyperAgent: Planning and Acting over Tool-Schema Hypergraphs for Tool-Use LLM Agents
- **中文标题**: HyperAgent：基于工具-模式超图的工具使用 LLM Agent 规划与执行
- **作者**: 详见 arXiv
- **机构**: 学术（inferred）
- **Venue**: arXiv preprint (2608.02650)
- **arXiv**: [2608.02650](https://arxiv.org/abs/2608.02650)
- **摘要与创新**: 现有工具使用 agent 从文本描述推断工具组合，低效且不可靠。在 schema 层建模工具关系构建有向 Tool-Schema Hypergraph；HyperAgent 先提取任务相关工具上下文图引导构建 schema-aware Task DAG，执行时通过 deficit-oriented support graph expansion 构造状态条件的工具支持子图。
- **实验结果**: AppWorld 上改进任务完成率并减少多余 API 调用、LLM 交互与 token 消耗，超越 ReAct/PlanExec/FullCodeRefl 及 SFT/DPO/RL/NFT 基线。
- **对比**: 相对语义 Top-K 检索与 In-N-Out 图检索，恢复隐性先决工具、减少试错探索。

### 19. ExRole: From Team Trajectories to Executable Roles in Multi-Agent Language Models
- **中文标题**: ExRole：从团队轨迹到可执行角色
- **作者**: 详见 arXiv
- **机构**: 学术（inferred）
- **Venue**: arXiv preprint (2608.11949)
- **arXiv**: [2608.11949](https://arxiv.org/abs/2608.11949)
- **摘要与创新**: 多数多智能体把角色当手写 prompt 标签。ExRole 提出角色应为可执行控制变量：从前缀局部团队轨迹学习未来感知的角色原型，解析为可读指令与 token 对齐角色标记，可选地用 turn 对齐信用路由共享 LoRA rank slots。
- **实验结果**: MuSiQue 相对单 agent 搜索 +15.0 EM/+14.4 F1；2WikiMultiHopQA +13.5/+16.1。
- **对比**: 相对 role-free/manual/random/shuffled 角色，轨迹诱导的角色绑定在策略优化中更优。

---

## 📊 推荐系统、广告、CTR 与序列建模（Recommendation, Advertising, CTR & Sequential Modeling）

### 20. FAT: Field-Aware Transformer for CTR Prediction（KDD'26）
- **中文标题**: FAT：面向 CTR 预测的字段感知 Transformer
- **作者**: 详见 arXiv
- **机构**: 工业 CTR 团队（inferred）
- **Venue**: KDD 2026 (V2)
- **arXiv**: [2511.12081](https://arxiv.org/abs/2511.12081)
- **摘要与创新**: 论证 CTR 模型"diminishing returns"根因是结构错配：标准 Transformer 假设顺序组合，而 CTR 数据需要跨异构字段的组合推理。FAT 用字段中心参数重建 Transformer 块：Field-Decomposed Attention 把二次对变换分解为字段感知内容对齐（O(Fd²)）+ 字段对交互调制（O(F²)）；Field-Aware FFN；Basis-Composed Hypernetwork 从共享基合成字段特异参数。给出基于 Rademacher 复杂度的正式 CTR Scaling Law（泛化误差取决于字段交互组合结构而非总词表大小 n）。
- **实验结果**: 大基准上新 SOTA，最多 +4.38% AUC；线上 +2.33% CTR、+0.66% RPM。
- **对比**: 相对标准 LLM 式 Transformer 移植（tokenize CTR 特征）与 DLRM，实现"结构化表达力"的规模化。

### 21. GOAL: Generative Optimization for Incentivized Advertising with Global Level Constraints（KDD'26）
- **中文标题**: GOAL：带全局约束的激励广告生成式优化
- **作者**: Gege Chen, Ning Luo, Hao Jiang, Da Li, Wenzheng Shu, Teng Sha, Yanxiang Zeng, Wenxin Tai, Fan Zhou, Xialong Liu（corr.）
- **机构**: Kuaishou Technology + UESTC
- **Venue**: KDD 2026 (V2)
- **arXiv**: [2608.04421](https://arxiv.org/abs/2608.04421)
- **摘要与创新**: 激励广告在严格全局约束下优化连续激励幅度。GOAL 把激励分配建模为条件序列生成，集成层次因果状态编码器（局部动态+长程依赖）；**SCPO**（Safe Constrained Policy Optimization）学习单一生成策略，无需重训练即可跨 ROI 约束谱泛化。
- **实验结果**: 大规模真实数据+合成疲劳环境上提升长期收入与留存、显著降低 ROI violation；4 周线上 A/B（65% 用户）ROI +2.184%、收入 +2.559%（p=0.03）。
- **对比**: 相对 uplift modeling（敏感/短视）与 offline RL（Markovian 假设违背/保守），统一生成式控制。

### 22. HRPO: Hierarchical Residual Policy Optimization for Generative Recommendations（KDD'26）
- **中文标题**: HRPO：生成式推荐的层次残差策略优化
- **作者**: Kaifeng Guo, Yiming Yang, Jingtong Gao, Guolei Zeng, Fukang Yang, Yukang Liang, Peng Jiang, Qingpeng Cai (corr.), Xiangyu Zhao (corr.)
- **机构**: Kuaishou Technology + City University of Hong Kong
- **Venue**: KDD 2026 (V2)
- **arXiv**: [2608.00750](https://arxiv.org/abs/2608.00750)
- **摘要与创新**: SID 解码器经 SFT 训练只模仿日志轨迹。HRPO 把 item 级结果转为稠密 token 对齐学习信号：组级奖励平滑估计 SID 前缀效用 → 分解为残差 token 信用 → 累积为 credit-to-go → RRPO 用 clipped updates + group-normalized advantages + KL 优化。
- **实验结果**: KuaiRand + 大规模广告系统线上 A/B，session 级效用与核心业务指标一致提升。
- **对比**: 相对 item 级/把终结信号广播到所有 SID token 的后训练，提供 token 级、layer-aware 的保守信用分配。

### 23. PushDualGen: Enabling LLMs to Generate Semantic IDs with Interpretable Copy（Kuaishou）
- **中文标题**: PushDualGen：支持生成式语义 ID + 可解释文案的推送推荐
- **作者**: 详见 arXiv
- **机构**: Kuaishou Technology
- **Venue**: arXiv preprint (2608.07989)
- **arXiv**: [2608.07989](https://arxiv.org/abs/2608.07989)
- **摘要与创新**: 推送推荐中 OneRec-Thinking 的 CoT 增加推理成本。PushDualGen 是轻量生成器：先生成 SID，再生成可跳过的解释性文案。已部署于快手推送通知（近 10 亿用户、~100K QPS）。
- **实验结果**: 150M 用户 14 天 A/B：有效播放率相对 +8.50%，不满率相对 -37.70%，长尾视频曝光提升。
- **对比**: 相对 OneRec-Thinking（CoT 高成本），生成 SID 后再选择性生成文案，兼顾可解释性与效率。

### 24. From Static Multi-Level Small Semantic Codebook to Dynamic Single-Level Large Semantic Codebook（Kuaishou）
- **中文标题**: 从静态多级小组语义码本到动态单级大语义码本
- **作者**: Tianlu Xie, Xin Ku, Mingjie Sun, Yunhao Sha, Lixiang Wang, Peng Wang, Yiyu Wang, Wenjin Wu, Zhaojie Liu, Peng Jiang, Wenwu Ou（详见 arXiv）
- **机构**: Kuaishou Technology
- **Venue**: arXiv preprint (2608.21012)
- **arXiv**: [2608.21012](https://arxiv.org/abs/2608.21012)
- **摘要与创新**: 生成式推荐中常用多级（三层）SID（两语义码+一协作文义消歧码）。提出单级大语义码本 + 独立协作文义消歧 token 减少解码步数；引入 exposure-aware 动态码本更新（时间加权衰减 + EMA 中心更新 + SID 变化曝光加权惩罚）；构造离线评估框架（表示质量/码利用/负载/碰撞/时间稳定性）。
- **实验结果**: 公共数据集 Recall@10 +5.0%–8.8%、NDCG@10 +4.1%–8.5%（OneRec）；自回归解码 FLOPs 降 47.93%–48.70%，单卡 QPS +28.57%–47.0%；5 天线上 A/B（2.5% 流量）主消费指标 +0.792%。
- **对比**: 相对三层 residual quantization SID，简化解码、缓解码本漂移。

### 25. UniMoMo: Expert Merging-Based MoE Acceleration for Large Recommendation Models
- **中文标题**: UniMoMo：基于专家合并的大规模推荐 MoE 加速
- **作者**: Lei Xin, Bin Gu, Peize Li, Zitong Wang, Jianbo Zhao, Changjiang Jiang, Yanyue Xie, Chao Huang, Xuyang Zhao, Zunhai Su, Fanhu Zeng, Zhenglun Kong
- **机构**: Kuaishou、ByteDance (Seed/Douyin)、Alibaba (Ant)、HKU、Harvard 等
- **Venue**: arXiv preprint (2608.08627)
- **arXiv**: [2608.08627](https://arxiv.org/abs/2608.08627)
- **摘要与创新**: MoE 层扩展容量但训练后仍存储/路由全专家库。UniMoMo 把部署问题建模为约束图粗化：基于功能相似性（用未标注校准集测专家对推荐状态响应）分组专家，layer-adaptive 保护机制限制高流量专家合并。
- **实验结果**: Amazon Beauty/KuaiRec/TenRec 上 4-expert 检查点 NDCG@10 保持 99.92%–102.30%，A100 加速 1.28×–1.63×；2-expert top-1 达 98.36%–104.24%、加速 1.47×–2.21×。
- **对比**: 相对参数距离分组，用功能相似性分组保留更多性能。

### 26. CRRN: Cascading Relevance-driven Recommendation Network for CTR（Alibaba / Tmall）
- **中文标题**: CRRN：触发式推荐 CTR 的级联相关性驱动推荐网络
- **作者**: Kaixuan Chen, Wenwen Wang, Xing Fang, Yang Huang, Jing Wang
- **机构**: Taobao & Tmall Group of Alibaba
- **Venue**: arXiv preprint (2608.22973)
- **arXiv**: [2608.22973](https://arxiv.org/abs/2608.22973)
- **摘要与创新**: 针对 Trigger-Introduced Recommendation（用户点击触发商品后进入承接页）场景，强调 trigger-target 交互与相关性。三组件：Trigger-Target Interaction 层（个性化门控提取交互特征）、Cascading Interest Fusion（级联注意力自适应融合即时+个性化兴趣）、Category-assisted Pairwise Loss（类别关联引导 trigger 相关性）。
- **实验结果**: 工业+公共数据超 SOTA；Tmall 线上 A/B pCTR +3.87%，已上线服务。
- **对比**: 相对 DIN/DIHN/DIAN/DEI2N 等 trigger-based 方法，综合利用 trigger-target 复杂关系与相关性表示。

### 27. STAR: Structured Tokenization and Target-Aware Interest Representation for PCVR Prediction
- **中文标题**: STAR：面向 PCVR 预测的结构化分词与目标感知兴趣表示
- **作者**: 详见 arXiv
- **机构**: KDD Cup 2026 参赛团队
- **Venue**: KDD Cup 2026 Tencent UniRec Challenge
- **arXiv**: [2608.12986](https://arxiv.org/abs/2608.12986)
- **摘要与创新**: 在 HyFormer-style 多序列 backbone 上合并结构化特征分词与目标感知兴趣表示：高基数信号恢复、显式 user-item 交互 token、目标感知序列解码、加权 user-item 对比辅助目标（InfoNCE 启发）。对齐训练/推理管线。
- **实验结果**: 主消融显示时间上下文增益最大，其次是对比对齐、目标感知编码、高基数恢复。

### 28. UniDot: Unified Network for Sequence Modeling and Feature Interaction（KDD Cup'26 亚军）
- **中文标题**: UniDot：序列建模与特征交互的统一网络
- **作者**: 详见 arXiv
- **机构**: KDD Cup 2026 Tencent UniRec Challenge 参赛团队
- **Venue**: KDD Cup 2026 Tencent UniRec Challenge Workshop
- **arXiv**: [2608.16797](https://arxiv.org/abs/2608.16797)
- **摘要与创新**: 从 FM 视角统一特征交互与序列建模：embedding 内积与 attention query·key 打分为同一原语。把非序列字段与多域行为序列 token 化到共享 token 空间，单 macro-block 内 token-mixing bus 与 sequence-retrieval bus 并行、经 MLP-Mixer fusion 逐层交换状态，FM Highway 携带显式逐层点积交互直达分类器。
- **实验结果**: TAAC×KDD Cup 2026 Industrial track 亚军，AUC 0.83217。
- **对比**: 相对分离发展的特征交互模型与序列模型，用单一原语（token 点积）统一两大模型族。

### 29. OneRanker: Unified Generation and Ranking with One Model（Tencent）
- **中文标题**: OneRanker：单模型统一生成与排序（微信广告）
- **作者**: 详见 arXiv
- **机构**: Tencent（Weixin Channels 广告）
- **Venue**: arXiv preprint (2603.02999v3)
- **arXiv**: [2603.02999](https://arxiv.org/abs/2603.02999)
- **摘要与创新**: 生成式广告推荐三挑战：兴趣目标与业务价值错配、生成过程 target-agnostic、生成与排序断裂。OneRanker 用价值感知多任务解耦、coarse-to-fine 协作目标感知（Fake Item Tokens + 排序解码器）、输入输出双端一致性保证（KV pass-through + Distribution Consistency 损失）实现架构级深度融合。
- **实验结果**: 微信视频号广告全量上线，GMV-Normal +1.34%、Costs +0.72%。
- **对比**: 相对 stage decoupling 与 single-stage fusion 两难，实现"价值引导生成、粗细协作感知、双端一致性"。

### 30. GRAB: Sequence-First CTR Prediction（Baidu）
- **中文标题**: GRAB：百度序列优先的 CTR 预测范式
- **作者**: 详见 arXiv
- **机构**: Baidu
- **Venue**: arXiv preprint (2602.01865)
- **arXiv**: [2602.01865](https://arxiv.org/abs/2602.01865)
- **摘要与创新**: 传统 DLRM 有"强记忆弱推理"瓶颈、收益递减。GRAB 是端到端生成式 CTR 框架，集成 **CamA**（Causal Action-aware Multi-channel Attention）捕获时间动态与特定动作信号；提出 STS 训练范式缓解分布偏移。
- **实验结果**: 首页 feed 广告线上 A/B：CTR +3.49%、CPM +3.05%（约一个月、10% 流量），已全量部署；缩放行为接近线性提升。
- **对比**: 相对 DLRM 与 GR 基线，seq-first 生成式 + CamA 保留更丰富长序列与动作语义。

### 31. CausalDPO: Causal Direct Preference Optimization for Distributionally Robust Generative Recommendation（ICML'26）
- **中文标题**: CausalDPO：面向分布鲁棒生成式推荐的因果直接偏好优化
- **作者**: 详见 ICML 2026
- **机构**: 学术/工业界（inferred）
- **Venue**: ICML 2026 (Poster)
- **链接**: [ICML 2026 poster 63635](https://icml.cc/virtual/2026/poster/63635)
- **摘要与创新**: 理论+实证揭示 DPO 在对齐过程放大环境混杂产生的虚假相关，损害 LLM 生成式推荐的 OOD 泛化。CausalDPO 在对齐阶段引入因果不变学习：backdoor adjustment 消除环境混杂、软聚类显式建模潜在环境分布、不变约束增强跨环境鲁棒一致性。
- **实验结果**: 4 种分布偏移下 4 个指标平均性能 +24.10%。
- **对比**: 相对 vanilla DPO（放大 spurious correlation），捕获跨环境的用户稳定偏好结构。

### 32. ProRL: RL for Proactive Recommendation via Rectified Policy Gradient（ICML'26）
- **中文标题**: ProRL：通过矫正策略梯度估计实现主动推荐的强化学习
- **作者**: Hongru Hou, Tiehua Mei, Denghui Geng, Jinhui Huang, Ao Xu, Hengrui Chen, Jiaqing Liang, Deqing Yang
- **机构**: 复旦系（Fudan）
- **Venue**: ICML 2026 (Poster)
- **链接**: [ICML 2026 poster 61903](https://icml.cc/virtual/2026/poster/61903)
- **摘要与创新**: 主动推荐系统（PRS）引导用户偏好转向目标商品。识别朴素策略梯度的两个缺陷：(1) 路径级奖励分解为步级奖励产生长度相关偏差（favors path extension）；(2) 每步权重全路径奖励导致高方差。提出 Stepwise Reward Centering + Position-Specific Advantage Estimation。
- **实验结果**: 3 个真实数据集上显著超越 SOTA PRS。
- **对比**: 相对 naive 策略梯度，精确瞄准路径质量而非路径长度。

### 33. CFlower: Conservative Generative Flow Networks for LLM-Based Recommenders（ICML'26）
- **中文标题**: CFlower：面向 LLM 推荐器的保守生成流网络
- **作者**: Xuan Yu, Feng Niu, Rui Zhu, Yudong Zhang, Xu Wang, Yang Wang
- **机构**: 学术（inferred）
- **Venue**: ICML 2026 (Poster)
- **链接**: [ICML 2026 poster 65235](https://icml.cc/virtual/2026/poster/65235)
- **摘要与创新**: 离线 LLM 推荐中用 SubTB 会非可辨识并任意分配概率质量到不支持区域。识别三类非可辨识源（流高估、前向质量泄漏、后向补偿）。提出 **CFlower**：保守 SubTB 目标显式惩罚不支持的前向流质量 + 数据集约束策略学习 + token-prefix DAG 上 on-policy 采样。
- **实验结果**: 3 个 Amazon 数据集上改进分布匹配与 accuracy-exposure 权衡，提供更可靠的下游 RL 参考策略。
- **对比**: 相对 Flower/SFT 与 naive SubTB，离线约束下更贴近数据支持的证据。

### 34. RSIR: Recursive Self-Improving Recommendation（ICML'26）
- **中文标题**: RSIR：循环自改进推荐框架
- **作者**: Luankang Zhang, Hao Wang, Zhongzhou Liu, Mingjia Yin, Yonghao Huang, Jiaqi Li, Wei Guo, Yong Liu, Huifeng Guo, Defu Lian, Enhong Chen
- **机构**: USTC + 工业界
- **Venue**: ICML 2026 (Poster)
- **链接**: [ICML 2026 poster 60941](https://icml.cc/virtual/2026/poster/60941)
- **摘要与创新**: 推荐数据极度稀疏。RSIR 让模型自举自身性能：当前模型生成合理用户交互序列 → 保真度质量控制在偏好流形上过滤 → 后继模型在扩充数据上训练。理论分析显示其是数据驱动的隐式正则器。
- **实验结果**: 多个 benchmark 与架构上一致累积增益；小/弱模型也能受益，弱模型可为强模型生成有效训练课程。
- **对比**: 相对依赖外部数据或教师模型，模型无关的循环自改进克服数据稀疏。

### 35. Principled Zero-shot Ranking Agents with Tournament Graphs（ICML'26）
- **中文标题**: 基于锦标赛图的原理化零样本排序 Agent
- **作者**: Sheshansh Agrawal, Thien Nguyen, Douwe Kiela
- **机构**: 学术/工业界（inferred，Kiela 为 Contextual AI）
- **Venue**: ICML 2026 (Poster)
- **链接**: [ICML 2026 poster 62762](https://icml.cc/virtual/2026/poster/62762)
- **摘要与创新**: LLM 是强大零样本 reranker。锦标赛图框架中每次 k 文档比较揭示 C(k,2) 对偏好；聚合到全局偏好图，其传递闭包无需更多模型调用即得更多排序。形式化"可认证确定"的排名，设计贪心信息增益查询调度；对非传递偏好用等价类折叠成 tiered rankings。
- **实验结果**: 14 benchmark、5 个 LLM 上实现 Pareto 支配：匹配/超越精度同时比可比方法少 25%–40% token、比 pairwise 少 7×。
- **对比**: 相对 heuristic reranker 与低效方法，原理化利用每次排序决策揭示的信息。

---

## 🎮 世界模型、游戏与具身智能（World Models, Games & Embodied AI）

### 36. Code World Model: Coding Agent as World Brain
- **中文标题**: Code World Model：编码 Agent 作为世界大脑
- **作者**: Yiwen Chen, Guosheng Lin, Chi Zhang
- **机构**: Westlake University（西湖大学 AGI Lab）+ NTU
- **Venue**: arXiv preprint (2608.25927)
- **arXiv**: [2608.25927](https://arxiv.org/abs/2608.25927)
- **摘要与创新**: 现有视频世界模型从视觉观测学动态，只显现结果而非底层规则/机制。Code World Model 分离世界演化与视觉实现：coding agent 作为"世界大脑"推理事件后果并生成可执行代码维护持久世界状态；引入 proxy 表示（编码逐帧时空约束），编译为 proxy video 条件化视频模型渲染高保真观测。
- **实验结果**: 在配对 gameplay 数据微调后，MiniMax-H3 遵循基于 proxy 的时空规范并保留丰富视觉细节。
- **对比**: 相对纯视觉视频世界模型，用代码提供持久、规则一致的演化。

### 37. Code as Worlds: Agentic Discovery of Executable World Representations
- **中文标题**: Code-as-World：物理推理的可执行世界表示的智能体发现
- **作者**: 详见 arXiv
- **机构**: 学术（inferred）
- **Venue**: arXiv preprint (2608.27549, Aug 27 2026)
- **arXiv**: [2608.27549](https://arxiv.org/abs/2608.27549)
- **摘要与创新**: 把物理世界表示为可执行代码（物理组合、动态演化、视觉外观）。通过溯因式智能体发现循环（propose–instantiate–execute–render–verify）从多模态观测构造。用验证过的可执行世界为 VLMs 提供量化物理推理的可扩展监督。
- **实验结果**: Code-as-World-VL 在 QuantiPhy 达 SOTA，超越领先专有模型。
- **对比**: 相对被动像素预测，用可执行世界表示显式建模 object state/物理参数/支配动力学。

### 38. Twin: Playing an Unknown Game with a Test-Time Digital Twin
- **中文标题**: Twin：用测试时数字孪生游玩未知游戏
- **作者**: 详见 arXiv
- **机构**: 学术（inferred）
- **Venue**: arXiv preprint (2608.14490)
- **arXiv**: [2608.14490](https://arxiv.org/abs/2608.14490)
- **摘要与创新**: 前沿 coding agent 为持续学习任务（如 ARC-AGI-3 游戏）编写可执行世界模型，仅从仿真与交互构造。replay 验证发生在 twin 世界模型中；每次模型预测与实际行动结果不匹配成为反例用于修复世界模型。action 在程序复现每个历史转换前不会发出。
- **实验结果**: 通过 183 关中的 179 关（97.8%），其中 158 关比人类首次游玩更高效（88.3%）；23/25 游戏满分 93.3（直跑基线仅 7.8、off-the-shelf harness 61.1）。
- **对比**: 相对 MuZero/DreamerV3 只学习参数化 latent 动态，Twin 在测试时从少量转换诱导符号源代码并执行引导修复。

### 39. WorldMind: Decoupled Game World Model for State-Aware NPC Behavior
- **中文标题**: WorldMind：面向状态感知 NPC 行为的解耦游戏世界模型
- **作者**: 详见 arXiv
- **机构**: 学术/工业界（inferred）
- **Venue**: arXiv preprint (2608.21439)
- **arXiv**: [2608.21439](https://arxiv.org/abs/2608.21439)
- **摘要与创新**: 现有游戏世界模型中 NPC 行为要么隐含纠缠于视频生成、要么外部规定。WorldMind 是首个把状态重建与 NPC 决策从视觉生成解耦的框架：Understanding（构造紧凑状态）、Decision（推理规划下一动作）、Control（转为时序条件）、Generation（合成视觉结果）四层闭环。引入 BOSS-140K 数据集（配对内部游戏状态）。
- **实验结果**: 约 70% 成对比较中 WorldMind 被偏好，动作有效性与序列契合第一。
- **对比**: 相对 COMBAT（隐式）与 ReactiveGWM（外部标签），状态落地显式决策。

### 40. WALL-SS: Scaling Long-horizon World Models via Next-Scale Autoregression
- **中文标题**: WALL-SS：通过下一尺度自回归扩展长程世界模型
- **作者**: 详见 arXiv
- **机构**: 学术/工业界（inferred）
- **Venue**: arXiv preprint (2608.26239, Aug 26 2026)
- **arXiv**: [2608.26239](https://arxiv.org/abs/2608.26239)
- **摘要与创新**: 生成式世界模型为机器人提供预测/规划/策略评估。WALL-SS 用 Scale-wise autoregressive Scaling 生成视觉未来，把具身轨迹表示为因果序列的观察+行动，coarse-to-fine 生成。三大组件：action-conditioned next-scale prediction、scale-compressed long-horizon memory（可复用因果状态流式扩展）、on-policy alignment（把 next-scale 生成当随机策略，用 action-following + 长期一致性奖励优化）。
- **实验结果**: 改进行动遵循与轨迹精度，支持有界记忆下分钟级流式 rollout；闭环部署与物理世界标定一致。
- **对比**: 相对 clip-level 视频扩散预测，显式组织 action-consequence 共享因果历史并支持可变时长/流式/概率优化接口。

### 41. ForgeWM: Progressive Causal Training for Few-Step Action-Conditioned Video World Models
- **中文标题**: ForgeWM：渐进因果训练实现少步行动条件视频世界模型
- **作者**: 详见 arXiv
- **机构**: CUHK / Tencent PCG / FDU / Shanghai AI Lab / HKUST（inferred）
- **Venue**: arXiv preprint (2608.14022)
- **arXiv**: [2608.14022](https://arxiv.org/abs/2608.14022)
- **摘要与创新**: 把双向行动条件视频生成器转为高效 few-step 世界模型。四阶段：域适应、teacher-forced 因果训练、因果一致性蒸馏、与双向 teacher 的 on-policy 分布匹配。产出 1/2/4 步专用学生；支持双路部署（延迟关键交互 + 可选 replay 细化）。
- **实验结果**: Minecraft 配对轨迹上在成像质量、动作信号精度、鼠标控制精度领先，最低 reference LPIPS；FPS 游戏（gamepad）四段配方可迁移。
- **对比**: 相对 Matrix-Game 2.0 与 HY-WorldPlay，few-step 显著降延迟，replay 细化贴近真实轨迹。

### 42. LDR: Latent Dynamics Reasoning for Extrapolative Video World Models
- **中文标题**: LDR：外推式视频世界模型的潜动力学推理
- **作者**: 详见 arXiv
- **机构**: 学术（inferred）
- **Venue**: arXiv preprint (2608.09926)
- **arXiv**: [2608.09926](https://arxiv.org/abs/2608.09926)
- **摘要与创新**: 视频扩散模型拟合像素而非时间转移规律。LDR 把潜转移建模为显式运动学积分：低阶动态数值积分，模型只回归第三阶及以上残差；在结构化潜表示（SL）上运行以更好外推。这是首个把学到的动力学外推到训练分布之外的视频世界模型。
- **实验结果**: 五个动力学任务上 ID-OOD 误差 gap 比 DiT 基线小 20× 以上，参数量少 26×、快 143×（4.1M vs 106.1M 参数）。
- **对比**: 相对 DiT/JEPA（直接回归未来潜），通过动力学推理捕获"世界如何演化"。

---

## 📚 基准评测与会议趋势（Benchmarks & Conference Trends）

### 43. ICLR 2026 全景趋势（Rio de Janeiro, Apr 23–27, 2026）
- **中文标题**: ICLR 2026 全景：论文趋势与评审危机
- **数据**: 19,525 submissions、5,355 accepted（27.4%）、225 Oral
- **来源**: [bohrium roundup](https://www.bohrium.com/en/blog/research-notes/iclr-2026-accepted-papers-highlights/) + [paperdigest](https://www.paperdigest.org/2026/04/iclr-2026-papers-with-code-data/)
- **要点**: 主题从"原生能力"转向"可靠部署"。代表性 Oral：**Common Corpus**（伦理预训练数据）、**Q-RAG**（价值型 RL 训练 embedder 的多步检索）、**WebDevJudge**（LLM-as-a-judge web 开发评测）、**SafeDPO**（约束式安全 DPO）、**Why DPO is a Misspecified Estimator**（指出 DPO 统计缺陷）。Efficiency-over-scale 成默认假设（MicroMix、DeepCompress 压缩推理链）。评审危机：约 45% 身份泄露、21% 评审由 AI 生成。

### 44. NeurIPS 2025 最佳论文回顾
- **中文标题**: NeurIPS 2025 最佳论文
- **来源**: [NeurIPS blog](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)
- **要点**: 4 篇 best + 3 runner-up，覆盖扩散模型理论、自监督 RL、LLM attention 机制、推理能力、在线学习理论、神经缩放律与多样性基准。Runner-up 之一《Does RL Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?》系统探测 RLVR 能力边界：现训练不引出本质新推理模式，base model 与 RL 模型采样分布高度重叠，六个主流 RLVR 算法表现相近且远离 base model 上限；蒸馏可真正扩展能力。
- **相关基准**: LTD-Bench（让模型画图测空间推理，183 任务，暴露语言-空间双向映射缺陷）；KORGym（KOR-Bench+Gymnasium 的游戏化推理评测平台，50+ 游戏，19 个 LLM + 8 个 VLM）。

### 45. ICDM/构建效度视角的 LLM benchmark 系统评审（NeurIPS 2025 D&B）
- **中文标题**: 测量重要之事：LLM 基准的构念效度
- **作者**: 29 位专家评审团队
- **机构**: 跨机构
- **Venue**: NeurIPS 2025 Datasets & Benchmarks Track
- **链接**: [paper](https://papers.neurips.cc/paper_files/paper/2025/file/1967e0fc3aa6cbbace562f5cb8e3954e-Paper-Datasets_and_Benchmarks_Track.pdf)
- **摘要与创新**: 对 445 个 LLM benchmark（46,114 候选论文筛选自 ICML/ICLR/NeurIPS/ACL/NAACL/EMNLP 2018–2024）做系统评审。发现 measured phenomena/tasks/scoring metric 的缺陷破坏宣称有效性。给出 8 项建议与可操作指南。

### 46. TFRBench: A Reasoning Benchmark for Evaluating Forecasting Systems（ICML'26）
- **中文标题**: TFRBench：评估预测系统推理的基准
- **作者**: Atik Ahamed 等（含 Google Cloud AI 的 Tomas Pfister 等）
- **机构**: Google Cloud / ServiceNow 等
- **Venue**: ICML 2026
- **链接**: [ICML 2026](https://icml.cc/virtual/2026/papers.html)
- **摘要与创新**: 区别于现有预测基准，TFRBench 提供协议评估预测系统生成的推理——对跨通道依赖、趋势与外部事件的分析。用多智能体迭代验证循环合成数值落地推理轨迹。

---

## 📈 主要发现与趋势判断

1. **RL 信用分配是最活跃方法论前沿**：从"组内相对"（GRPO）到"架构感知运输算子"（CompPO/CCT）再到"step-level 因果审计"（Credit Without Ground Truth，Audit 发现 implicit credit 只是复制策略流利度、outcome 条件化无因果信息）。后训练社区正在对"每步 credit 是否有意义"做出方法学反思。
2. **生成式推荐已在工业全面扎根**：Kuaishou/Tencent/Baidu/Alibaba 均上线生成式 SID 系统（PushDualGen、OneRanker、GRAB、GR4AD、CRRN），学界（ICML/KDD）同步从"能否"转向"如何 token 级信用、如何约束 ROI、如何动态维护 codebook"。
3. **CTR 规模化转向"结构化表达力"**：FAT 证明字段感知结构 + 正式 Scaling Law（Rademacher complexity）能突破 LLM 式盲目堆参的收益递减，代表 CTR 序列建模的一个理论抓手。
4. **世界模型走向"可执行/可推理"**：Code World Model、Code-as-World、Twin 用可执行代码表达世界以支持规则一致演化与 OOD 外推，是对"像素级视频世界模型"的有力反范式。

---

*本摘要由 arXiv 与会议检索自动生成，部分作机构为"inferred"需以原文为准。链接为 arXiv abstract 页或会议页面。*
