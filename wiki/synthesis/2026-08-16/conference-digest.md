---
title: "Conference Digest: 2025-2026 Top ML/AI Venues (2026-08-16)"
type: synthesis
created: 2026-08-16
updated: 2026-08-16
sources: []
tags: [conference-digest, ICML2026, AAAI2026, NeurIPS2025, ICLR2026, CVPR2026, KDD2026, ACL2026, EMNLP2025, SIGIR2026, WWW2026, CIKM2025, RecSys2025, recommendation, LLM, advertising, CTR, agents, generative-models, benchmarks]
---

# Conference Digest: 2025-2026 Top ML/AI Venues

> Compiled 2026-08-16. Covers ICML 2026, ICLR 2026, NeurIPS 2025, AAAI 2026, CVPR 2026, KDD 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025, plus general arXiv (Jul–Aug 2026). Focus areas: LLM training/scaling, RL, agent systems, code execution, generative models, world models, recommendation, advertising/CTR, benchmarks.
>
> ⚠️ 会议勘误 (venue corrections vs. earlier digests): **WWW 2026 实际在迪拜 (Dubai, UAE)**，悉尼是 WWW 2025；**CIKM 2025 实际在首尔 (Seoul)**，贝尔法斯特是 CIKM 2024；**AAAI 2026 在新加坡 (Jan 20–27)**。
>
> Convention: entries marked "link not confirmed" were verified in search results but had no arXiv link surfaced. Chinese titles《》are translations, not official.

---

## 1. ICML 2026 (Seoul, July 6–11)

**Scale**: ~24,661 valid submissions, ~6,352 accepted (~27%). Awards: 2 Outstanding Papers + 1 Outstanding Position Paper, 5 Honorable Mentions; Test of Time → **A3C** (DeepMind, 2016).

### 1.1 Outstanding Papers

#### The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models (《灵活性的陷阱：重新审视扩散语言模型任意顺序生成的价值》)
- **Authors**: Zanlin Ni, Shenzhi Wang, Yang Yue, Tianyu Yu, Weilin Zhao, Yeguo Hua, Tianyi Chen, Jun Song, Cheng Yu, Bo Zheng, Gao Huang
- **Affiliation**: Tsinghua University (Gao Huang group)
- **Venue**: **ICML 2026 Outstanding Paper** (Oral) — 20+ 年来首个完全由中国机构完成的 ICML Outstanding Paper
- **arXiv**: link not confirmed (code: github.com/LeapLabTHU/JustGRPO)
- **Abstract & Key Innovations**: 揭示扩散语言模型 (dLLM) 号称的"任意顺序生成"优势其实限制推理——模型会回避高不确定性的 "hinge" token，导致解覆盖崩溃。提出 **JustGRPO**：直接对 dLLM 施加标准从左到右的 GRPO，保留并行解码同时提升推理。
- **Comparison**: 与保持任意顺序的复杂 dLLM-RL 方法对照，反直觉地更简单更有效。
- **Experimental numbers**: GSM8K 上 89.1% 准确率。

#### High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions (《扩散模型与对数凹分布的高精度采样》)
- **Authors**: Fan Chen, Sinho Chewi, Constantinos Daskalakis, Alexander Rakhlin
- **Affiliation**: MIT / Yale
- **Venue**: **ICML 2026 Outstanding Paper**
- **arXiv**: link not confirmed
- **Abstract & Key Innovations**: 在 Õ(δ) 精度 score 估计下实现 polylog(1/δ) 步内 δ 误差采样——对先前所有扩散采样复杂度结果是**指数级改进**；并给出通用 log-concave 分布首个仅依赖梯度求值的 polylog 复杂度采样器。
- **Experimental numbers**: 复杂度 Õ(d·polylog(1/δ))；L-Lipschitz 条件下 Õ(√(dL)·polylog(1/δ))。

### 1.2 Oral Highlights

#### Maximum Likelihood Reinforcement Learning (MaxRL) (《最大似然强化学习》)
- **Affiliation**: not confirmed
- **Venue**: ICML 2026 Oral
- **Abstract & Key Innovations**: 证明标准期望奖励 RL 只是"正确 rollouts 上似然"的一阶近似；提出 MaxRL，在 RL 与最大似然之间用 compute-indexed 目标插值，标准 RL 代码一行改动。
- **Comparison / Numbers**: 在测试的模型/任务上 Pareto 占优；test-time scaling 效率相对 GRPO 最高 **20×**；在迷宫导航、图像识别、数学推理上验证。

#### daVinci-Dev: Agent-native Mid-training for Software Engineering (《面向软件工程的智能体原生中训练》)
- **Venue**: ICML 2026 Oral
- **Abstract & Key Innovations**: 首个针对 coding agents 的 *agentic mid-training* 系统研究：用 "contextually-native" + "environmentally-native" 的轨迹数据（73.1B tokens）作为纯 RL post-training 的廉价替代。
- **Comparison / Numbers**: 从非 coder 的 Qwen2.5-Base 出发，SWE-Bench Verified 上 **56.1% (32B) / 58.5% (72B)**，开放配方在该尺寸下 SOTA；mid-training tokens 不到 Kimi-Dev 的一半。

#### WeDLM: Reconciling Diffusion Language Models with Standard Causal Attention for Fast Inference (《WeDLM：用标准因果注意力实现扩散语言模型快速推理》)
- **Authors**: Aiwei Liu 等（含 Jie Zhou）
- **Affiliation**: Tencent AI Lab / Tsinghua（推断）
- **Venue**: ICML 2026 Oral
- **Abstract & Key Innovations**: 通过 Topological Reordering 让 dLLM 解码完全基于因果注意力，prefix-KV-cache 兼容（可直接跑在 vLLM 上）；流式解码持续提交高置信 token。
- **Comparison / Numbers**: 挑战性推理基准上约 **3× 加速**，低熵场景最高 **10×**（对照 vLLM 部署的 AR 骨干）。

#### LIVE: Long-horizon Interactive Video World Modeling (《LIVE：长视界交互式视频世界建模》)
- **Affiliation**: Microsoft Research
- **Venue**: ICML 2026
- **Abstract & Key Innovations**: 用 cycle-consistency 目标（前向 rollout 后反向重建初始状态）约束 action-conditioned 视频世界模型的误差累积，无需 teacher distillation。
- **Comparison / Numbers**: 长视界基准 SOTA；能在超过训练 rollout 长度的范围维持高质量视频。

#### Learning Unmasking Policies for Diffusion Language Models (《为扩散语言模型学习去掩码策略》)
- **Affiliation**: **Apple** (ml-rl-dllm)
- **Venue**: ICML 2026 Oral
- **Abstract & Key Innovations**: 把 masked-diffusion 采样建模为 MDP，用 RL 训练轻量单层 Transformer unmasking policy，替换手工启发式置信阈值。
- **Comparison**: 半自回归 (block) 模式下追平 SOTA 启发式；full-diffusion 模式下超越。

#### DR Tulu: Reinforcement Learning with Evolving Rubrics for Deep Research (《DR Tulu：基于进化评分准则的深度研究强化学习》)
- **Affiliation**: AI2 生态（Tulu 谱系）
- **Venue**: ICML 2026 Oral
- **Abstract & Key Innovations**: RLER——评分准则 (rubrics) 与 policy 在训练中共演化。产出 Deep Research Tulu-8B，首个直接为开放式长篇幅深度研究训练的全开放模型。
- **Numbers**: 平均比 Tongyi DR **+15.6%**、比 OpenAI DR **+0.7%**；每次查询成本约为 OpenAI DR 的 1/1000。

#### ThreadWeaver: Adaptive Threading for Efficient Parallel Reasoning in Language Models (《ThreadWeaver：语言模型高效并行推理的自适应线程化》)
- **Affiliation**: not confirmed（Qwen3-8B 上训练）
- **Venue**: ICML 2026 Oral
- **Abstract & Key Innovations**: 两阶段并行轨迹生成 + trie-based rollout（兼容任意自回归引擎）+ 并行化感知 RL，平衡精度与并行效率。
- **Numbers**: AIME24 **79.9%**，六个数学基准平均 71.9%；token 延迟最高 **1.53×** 加速。

### 1.3 Advertising & Auctions

#### Model Monotonicity in Autobidding Auctions: When Do Better Predictions Lead to Better Outcomes? (《自动出价拍卖中的模型单调性：更好的预测何时带来更好的结果？》)
- **Authors**: Ashwinkumar Badanidiyuru 等
- **Affiliation**: **Google Research**
- **Venue**: ICML 2026
- **arXiv**: https://arxiv.org/abs/2605.31036
- **Abstract & Key Innovations**: 用 cluster-refinement/filtration 关系形式化 "model improvement"，刻画 pCTR/pCVR 预测变好在哪些拍卖机制（tCPA/max-CPA × FPA/SPA/VCG × 有无预算）下真正提升平台收益/福利。
- **Numbers**: 所研究设定中仅 3 个保证单调性；max-CPA+FPA 反例在指定乘子下造成 **66% 收入损失**、0.09% 福利损失。

### 1.4 MoE, Diffusion & RL Systems

#### Skill-Based Mixture-of-Experts: Adaptive Routing for Heterogeneous Reasoning via Inferred Skills (《Skill-MoE：基于技能推断的异构推理自适应路由》)
- **Authors**: Justin Chih-Yao Chen 等（UNC）
- **Venue**: ICML 2026
- **arXiv**: https://arxiv.org/abs/2503.05641
- **Abstract & Key Innovations**: 免梯度、符号化技能驱动的实例级专家选择；batch inference 让 16 个模型跑在单 GPU。
- **Numbers**: 相对最佳 multi-agent 基线平均 **+8.15%**（MMLU-Pro, GPQA, AIME, MedMCQA）。

#### Critique-GRPO (rollout-efficient GRPO variant) & WS-GRPO
- **Venue**: ICML 2026 Posters
- **arXiv**: https://arxiv.org/abs/2506.03106 (Critique-GRPO)
- **Notes**: 利用自然语言 critique 提升 rollout 效率的 GRPO 变体，延续 RLVR 效率竞争主线。

#### SWE-Bench Pro (《SWE-Bench Pro：长视界编码智能体基准》)
- **Venue**: ICML 2026
- **Abstract & Key Innovations**: 1,865 个长视界任务；最佳模型 public <45%、private <20%（而 SWE-bench Verified 上公开模型 >70%），揭示"Benchmark saturation"问题。

#### Scaling Beyond Masked Diffusion Language Models
- **Venue**: ICML 2026
- **Abstract & Key Innovations**: uniform-state diffusion 在 1.7B 下 GSM8K 优于 AR/Masked，尽管 perplexity 更差。

---

## 2. ICLR 2026 (Rio de Janeiro, Apr 23–27)

**Scale**: 19,525 submissions, 5,355 accepted (27.4%), ~223 orals. Outstanding Paper ×2.

### 2.1 Outstanding Papers

#### Transformers are Inherently Succinct (《Transformer 天然地紧凑》)
- **Authors**: Pascal Bergsträßer, Ryan Cotterell, Anthony W. Lin
- **Affiliation**: TU Darmstadt / ETH Zürich
- **Venue**: **ICLR 2026 Outstanding Paper** (Oral)
- **arXiv**: https://arxiv.org/abs/2510.19315 (OpenReview: Yxz92UuPLQ)
- **Abstract & Key Innovations**: 提出 *succinctness* 作为表达能力度量；证明固定精度 (unique-hard attention) transformer 比 LTL 与 RNN/SSM 指数级更紧凑，比有限自动机双重指数级更紧凑（通过 attention 实现双指数计数器）。
- **Comparison**: 把先前 transformer→LTL 的双指数翻译改进为指数；把 NEXP-hard 验证强化为 **EXPSPACE-complete**。

#### LLMs Get Lost In Multi-Turn Conversation (《LLM 在多轮对话中迷失》)
- **Authors**: Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville
- **Affiliation**: **Microsoft Research**
- **Venue**: **ICLR 2026 Outstanding Paper** (Oral)
- **arXiv**: https://arxiv.org/abs/2505.06120
- **Abstract & Key Innovations**: 大规模 "sharded simulation" 把单轮指令变成逐步揭示的多轮对话，暴露"指令欠明确"场景。把退化分解为 aptitude loss（次要）与 unreliability（主要）：模型过早假设、过早提出最终方案、过度依赖早期错误答案——"一旦走错转弯就迷路且无法恢复"。
- **Numbers**: 6 个生成任务 × 15 个模型平均 **39% 性能下降**（多轮 65% vs 单轮 90%）；unreliability 上升 ~112%（20 万+模拟对话）。

### 2.2 Oral / Notable

#### Mamba-3: Improved Sequence Modeling using State Space Principles (《Mamba-3：基于状态空间原理改进序列建模》)
- **Authors**: Aakash Lahoti, Kevin Y. Li, Berlin Chen, Caitlin Wang, Aviv Bick, J. Zico Kolter, Tri Dao, Albert Gu
- **Affiliation**: Princeton / CMU
- **Venue**: ICLR 2026 Oral
- **arXiv**: https://arxiv.org/abs/2603.15569
- **Abstract & Key Innovations**: 推理优先 SSM：指数梯形 (exponential-trapezoidal) 离散化、复值状态更新（等价 data-dependent RoPE）、MIMO 递推提升 decode 算术强度（固定 state 下 decode FLOPs 最高 +4×，无延迟增加）。
- **Numbers**: 1.5B：相对 Gated DeltaNet **+0.6pp**，加 MIMO 共 **+1.8pp**；一半 state 大小追平 Mamba-2 perplexity；修复线性模型的 state-tracking 弱点（parity、模运算）。

#### Q-RAG: Long Context Multi-Step Retrieval via Value-Based Embedder Training (《Q-RAG：基于价值函数训练的嵌入器多步检索》)
- **Affiliation**: AIRI / Skoltech
- **Venue**: ICLR 2026 Oral
- **Abstract & Key Innovations**: 训练轻量 *embedder agent*（PQN 风格 value-based RL，无 replay buffer）在 embedding 空间做多步检索，LLM 保持冻结——检索的 RL 化。
- **Comparison / Numbers**: 单张 A100-80GB、~12 小时（vs R1-Searcher/Search-R1 的 ~8×A100 集群）；BabiLong 与 RULER 长上下文（至 10M token）SOTA；从 4K→1M 训练长度泛化无精度损失。

#### ATLAS: Adaptive Transfer Scaling Laws for Multilingual Pretraining (《ATLAS：多语言预训练的自适应迁移缩放定律》)
- **Affiliation**: **Google DeepMind / Google Research**
- **Venue**: ICLR 2026
- **Abstract & Key Innovations**: 最大规模多语言预训练研究：774 次训练 run、10M–8B 参数、400+ 语言、48 语言评估；跨语言迁移矩阵 + 自适应 scaling law + 从零训练 vs 微调 crossover 规则。
- **Numbers**: 语言翻倍 (2·K) 需模型 **1.18×**、数据 **1.66×**；2B 下微调-预训练 crossover 通常出现在 ~144B–283B tokens。

#### GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning (《GEPA：反思式提示进化可以超越强化学习》)
- **Venue**: ICLR 2026 Oral
- **Abstract & Key Innovations**: Genetic-Pareto prompt 优化器，用自然语言反思轨迹诊断/更新 prompt。
- **Numbers**: 平均超 GRPO **6pp**、最高 19pp，rollouts 少 **35×**；AIME-2025 +12pp；超 MIPROv2 >10pp。

#### DECS: Overthinking Reduction with Decoupled Rewards and Curriculum Data Scheduling (《DECS：解耦奖励与课程数据调度降低过度思考》)
- **Authors**: Shuyang Jiang, Yusheng Liao, Ya Zhang, Yanfeng Wang, Yu Wang
- **Affiliation**: Shanghai Jiao Tong University
- **Venue**: ICLR 2026 Oral
- **Abstract & Key Innovations**: 识别长度惩罚两大缺陷（惩罚必要探索 token、奖励部分冗余），提出解耦 token 级奖励 + 课程批次调度。
- **Numbers**: 七个基准上推理 token **>50% 减少**，性能保持或提升。

#### Beyond Markovian RL: Reflective Exploration in LLMs via Bayesian RL (BARL) (《超越马尔可夫强化学习：基于贝叶斯强化学习的反思性探索》)
- **Affiliation**: Northwestern University / **Google DeepMind** / Google
- **Venue**: ICLR 2026
- **Abstract & Key Innovations**: 证明马尔可夫 RL policy 不诱导反思性探索；用对 MDP 后验的 Bayesian RL 重新建模，得到不确定性自适应策略，能缝合/切换策略。

#### iFusion: Integrating Dynamic Interest Streams via Diffusion Model for Click-Through Rate Prediction (《iFusion：基于扩散模型的动态兴趣流融合用于点击率预测》)
- **Venue**: ICLR 2026
- **Abstract & Key Innovations**: 把长/短期兴趣融合重铸为条件扩散生成，Disentangled CFG (DCFG) + Mixture Autoregressive Denoising Network (MARN)；一致性损失支持单步推理。
- **Numbers**: AUC 0.8512 (Amazon) / 0.9347 (Taobao) / 0.6652 (Ali Ads) / 0.7685 (工业)；在线 A/B **CTR +2.44%**、**eCPM +2.61%** (p<0.001)；TP99 延迟 +0.302%。

#### Prophet: Diffusion Language Model Knows the Answer Before It Decodes (《Prophet：扩散语言模型在解码前已知答案》)
- **Venue**: ICLR 2026 Oral
- **Numbers**: LLaDA-8B / Dream-7B 上解码步数最多减少 **3.4×**。

#### R-Horizon: How Far Can Your Large Reasoning Model Really Go? (《R-Horizon：大型推理模型在广度与深度上能走多远？》)
- **Affiliation**: Fudan University / Xiaomi（推断）
- **Venue**: ICLR 2026
- **Abstract & Key Innovations**: 用 query 组合构造长视界推理基准，暴露 frontier LRM 的有限 *有效推理长度* 与思考预算错配。
- **Numbers**: RLVR on R-Horizon 数据提升多视界性能，AIME2024 **+7.5**（相对单视界训练）。

#### Enhancing Generative Auto-bidding with Offline Reward Evaluation and Policy Search
- **Venue**: ICLR 2026 **Oral**（广告/自动出价）
- **Abstract**: 生成式自动出价与离线奖励评估 + policy search 结合。

---

## 3. NeurIPS 2025 (San Diego, Dec 2–7)

**Scale**: ~20,000 submissions, 25% acceptance, 5,290 accepted papers.

### 3.1 Best Papers

#### Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond) (《人工蜂群思维：语言模型的开放式同质化》)
- **Authors**: Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Yejin Choi
- **Affiliation**: UW / CMU / Allen Institute for AI
- **Venue**: **Best Paper** (Datasets & Benchmarks track)
- **arXiv**: https://arxiv.org/abs/2510.22954
- **Abstract & Key Innovations**: INFINITY-CHAT 数据集（26K+ 开放问题、31K+ 人工标注），评估 70+ LLM，发现普遍的 "artificial hivemind"——模型内/模型间极端 mode collapse（不同家族收敛到惊人相似输出）。RLHF 与 instruction tuning 使创意潜空间同质化；现有 reward model 对多样人类偏好校准差。
- **Comparison**: 温度缩放与模型集成不能保证多样性。

#### Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free (《Gated Attention：非线性、稀疏与免注意力汇聚》)
- **Authors**: Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, Junyang Lin
- **Affiliation**: **Alibaba Qwen Team** — 中国机构在该届唯一 Best Paper
- **Venue**: **Best Paper** (Oral)
- **arXiv**: https://arxiv.org/abs/2505.06708
- **Abstract & Key Innovations**: 系统比较 30+ 变体（5 个 gating 位置 × 15B MoE / 1.7B dense，3.5T tokens）。核心发现：SDPA 后加 head-specific sigmoid gate 持续提升性能，消除 attention sink、稳定训练、容忍更大学习率、改善 scaling。
- **Comparison**: 已被 Qwen3-Next 生产架构采纳；开源 github.com/qiuzh20/gated_attention。

#### 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities (《1000 层网络用于自监督强化学习》)
- **Authors**: Kevin Wang, Ishaan Javali, Michał Bortkiewicz, Tomasz Trzciński, Benjamin Eysenbach
- **Venue**: **Best Paper** (Oral)
- **Abstract & Key Innovations**: 无奖励/演示的无监督 goal-conditioned 设定下把深度推到 **1,024 层**，性能 **2×–50×** 提升，打破 RL 网络应浅（2–5 层）的惯例。

#### Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training (《扩散模型为何不记忆：训练中隐含动态正则化的作用》)
- **Authors**: Tony Bonnaire, Raphaël Urfin, Giulio Biroli, Marc Mézard
- **Venue**: **Best Paper** (Oral)
- **arXiv**: https://arxiv.org/abs/2505.17638
- **Abstract & Key Innovations**: 两个时间尺度：τ_gen（学会生成高质量样本）与 τ_mem（开始记忆训练样本）；τ_mem 随训练集大小 n 线性增长而 τ_gen 不变，形成随 n 增长的"泛化窗口"。

### 3.2 Runner-Ups

#### Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? (《强化学习真的能在基座模型之上激励推理能力吗？》)
- **Authors**: Yang Yue, Gao Huang 等（Tsinghua）
- **Venue**: **Runner-up** (Oral)
- **Abstract & Key Innovations**: 系统性量化 RL post-training 相对基座模型在推理容量上的真实增益与边界。

#### Superposition Yields Robust Neural Scaling (《叠加产生稳健的神经缩放》)
- **Venue**: **Runner-up** (Oral)
- **Abstract & Key Innovations**: 基于 Anthropic 的 toy model，用 weight decay 控制 superposition 程度研究 loss 如何随模型大小缩放；开源 LLM 处于强 superposition 区，loss 随维度倒数缩放。

#### Optimal Mistake Bounds for Transductive Online Learning (《转导在线学习的最优错误界》)
- **Venue**: **Runner-up**
- **Abstract**: 解决 30 年开放问题：Littlestone 维 d 的概念类，transductive mistake bound 至少 Ω(√d)，指数改进先前的下界。

#### Test of Time Award
- **Faster R-CNN**（Shaoqing Ren, Kaiming He, Ross Girshick, Jian Sun, 2015）。

---

## 4. AAAI 2026 (Singapore, Jan 20–27)

**Scale**: ~29,000 submissions → ~23,000 进入评审（AAAI-25 的近 2 倍），4,167 accepted (17.6%)。中国贡献约 20,000 篇投稿。

### 4.1 Outstanding Papers

#### LLM2CLIP: Powerful Language Model Unlocks Richer Cross-Modality Representation (《LLM2CLIP：强大语言模型解锁更丰富的跨模态表示》)
- **Authors**: Weiquan Huang, Aoqi Wu, Yifan Yang, Xufang Luo, Yuqing Yang, Liang Hu, Qi Dai, Chunyu Wang, Xiyang Dai, Dongdong Chen, Chong Luo, Lili Qiu
- **Affiliation**: Microsoft Research / 中科院（推断）
- **Venue**: **AAAI 2026 Outstanding Paper**
- **Abstract & Key Innovations**: 用强大 LLM 的表示增强 CLIP 式跨模态学习，突破弱文本编码器瓶颈（持续被 Agent 3 检索到的视觉骨干演进线）。

#### ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver (《ReconVLA：重建式视觉-语言-动作模型》)
- **Authors**: Wenxuan Song 等
- **Venue**: **AAAI 2026 Outstanding Paper**
- **Abstract & Key Innovations**: 通过重建目标强化 VLA 感知，作为机器人 perceiver 更有效。

#### Model Change for Description Logic Concepts / Causal Structure Learning for Dynamical Systems (CADYT) / High-Pass Matters: Sheaflet-Based Hypergraph NNs
- **Venue**: **AAAI 2026 Outstanding Papers**
- **Notes**: 理论方向（description logic、因果发现、超图 sheaflet 理论）。

### 4.2 Special Track & Alignment

#### On the Alignment of Large Language Models with Global Human Opinion (《LLM 与全球人类意见的对齐》)
- **Authors**: Yang Liu, Masahiro Kaneko, Chenhui Chu
- **Venue**: **AAAI 2026 Best Paper (AI Alignment track)**
- **Abstract**: 研究 LLM 对齐是否真正反映全球多样观点而非西方中心偏好。

#### PlantTraitNet & Generalizable Slum Detection with MoE (AI for Social Impact)
- **Venue**: **AAAI 2026 Outstanding Papers (AISI track)**
- **Abstract**: 植物性状多模态预测 / 卫星影像贫民窟检测的 MoE 方法。

---

## 5. CVPR 2026 (Denver, June 3–7)

### 5.1 Best Paper

#### Efficiently Reconstructing Dynamic Scenes One D4RT at a Time (《一次性高效重建动态场景：D4RT》)
- **Authors**: Chuhan Zhang 等（含 Andrew Zisserman, Raia Hadsell, Zoubin Ghahramani）
- **Affiliation**: **Google DeepMind** / UCL / Oxford
- **Venue**: **CVPR 2026 Best Paper**
- **Link**: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Efficiently_Reconstructing_Dynamic_Scenes_One_D4RT_at_a_Time_CVPR_2026_paper.pdf
- **Abstract & Key Innovations**: 前馈 transformer 联合推断深度、时空对应与相机参数，轻量 decoder 按需探测任意空间-时间点的 3D 位置，把 4D 重建任务统一到单模型。
- **Comparison**: 超越 MegaSaM、ε³、SpatialTrackerV2；只有 D4RT 能完整重建动态视频所有像素。

### 5.2 Honorable Mentions

#### SAM 3D: 3Dfy Anything in Images (《SAM 3D：从单张图像生成三维内容》)
- **Authors**: Xingyu Chen 等（含 Piotr Dollár, Georgia Gkioxari, Jitendra Malik）
- **Affiliation**: **Meta Superintelligence Labs**
- **Venue**: **CVPR 2026 Best Paper Honorable Mention**
- **Abstract & Key Innovations**: 单图生成物体几何/纹理/布局的生成模型；人-模型-in-the-loop 标注 + 合成预训练→真实对齐，突破 "3D data barrier"。
- **Numbers**: 真实物体 5:1、场景 6:1 人类偏好胜率；SA-3DAO 基准（1K artist mesh）；ADD-S@0.1 联合形状+布局生成提升至 77%。

#### NitroGen: An Open Foundation Model for Generalist Gaming Agents (《NitroGen：通用游戏智能体开源基础模型》)
- **Authors**: Loïc Magne, Anas Awadalla 等（含 Yejin Choi, Yuke Zhu, Linxi Fan）
- **Affiliation**: **NVIDIA** + Stanford / Caltech / UChicago / UT Austin
- **Venue**: **CVPR 2026 Best Paper Honorable Mention** (Oral)
- **Abstract & Key Innovations**: vision-action 基础模型，**40,000 小时**、**1,000+ 游戏**的游戏视频训练，展示跨领域通用游戏能力。

### 5.3 Generative & World Models

#### A Frame is Worth One Token: Efficient Generative World Modeling with Delta Tokens (《一帧一个 Token：基于 Delta Token 的高效生成式世界模型》)
- **Affiliation**: TU Eindhoven + **ByteDance**
- **Venue**: CVPR 2026
- **Link**: https://openaccess.thecvf.com/content/CVPR2026/papers/Kerssies_A_Frame_is_Worth_One_Token_Efficient_Generative_World_Modeling_CVPR_2026_paper.pdf
- **Abstract & Key Innovations**: DeltaTok tokenizer 把相邻帧特征差编码为单个连续 "delta" token，3D 时空→1D 时间；Best-of-Multi-hypothesis 训练（并行生成多样未来，只监督最优）。
- **Numbers**: 512×512 帧 **1,024× token 减少**；参数 **>35×**、FLOPs **2,000×** 少于现有生成式世界模型；Cityscapes mIoU +1.9；predictor 仅占推理 FLOPs ~0.5%。

#### HoloCine: Holistic Generation of Cinematic Multi-Shot Long Video Narratives (《HoloCine：电影级多镜头长视频叙事的整体生成》)
- **Affiliation**: HKUST / Ant Group / **ByteDance**（Wan2.2 14B 基础）
- **Venue**: CVPR 2026 Highlight
- **arXiv**: https://arxiv.org/abs/2510.20822
- **Abstract & Key Innovations**: 单次扩散生成整个多镜头场景；Window Cross-Attention 逐镜头定位文本来实现导演级控制；Sparse Inter-Shot Self-Attention 把二次复杂度降到近线性，支持分钟级生成。
- **Comparison**: 超越 StoryDiffusion / IC-LoRA 两阶段管线与 CineTrans；多镜头叙事理解上与 Sora 2 定性相当。

#### TV2TV: A Unified Framework for Interleaved Language and Video Generation (《TV2TV：语言与视频交错生成的统一框架》)
- **Affiliation**: **Meta FAIR**
- **Venue**: CVPR 2026
- **Abstract & Key Innovations**: Transfusion 风格 omni 模型 + Mixture-of-Transformers：联合 next-token 语言建模与 next-frame flow matching；推理时在"用词思考"与"用像素行动"间交替，支持中途文本干预。
- **Numbers**: 人类评估 91% 偏好；对比 think-then-act (Think2V) 细粒度指令跟随 **+19pt**；扩展到 8K 小时 VLM 标注交错体育视频。

#### Recurrent Video Masked Autoencoders (《循环视频掩码自编码器》)
- **Affiliation**: **Google DeepMind**
- **Venue**: CVPR 2026
- **Abstract & Key Innovations**: 非对称 masking AE + transformer 循环核心，纯像素重建训练，线性时间/内存聚合信息；通用编码器跨视频+空间任务。
- **Numbers**: 相对 VideoMAEv2-g / DINOv2-g（约 30× 大）平均任务超越；80+ 帧稳定特征传播。

#### CURVE: A Benchmark for Cultural and Multilingual Long Video Reasoning (《CURVE：文化多语言长视频推理基准》)
- **Affiliation**: **Google DeepMind** + UC Berkeley
- **Venue**: CVPR 2026
- **Abstract & Key Innovations**: 540 个区域文化视频、18 个地区、2,400 个人类撰写问题与多步推理链；证据图迭代错误定位。
- **Numbers**: 人类 95.22% vs 最佳模型 Gemini-2.5-Pro 45.07%；Telugu 28.0% / Tamil 31.6%；~75% 失败源于文化视觉感知。

#### GenieDrive / VerseCrafter / TMD / AVGGT
- **GenieDrive** (CVPR 2026, HKU, 4D occupancy 引导的物理感知驾驶世界模型); **VerseCrafter** (Tencent + SJTU, VerseControl4D); **TMD** (NVIDIA, Wan2.1-14B 蒸馏至 NFE=1.38, VBench 84.24); **AVGGT** (Google DeepMind, VGGT 全局注意力加速, CVPR Highlight)。

---

## 6. KDD 2026 (Jeju Island, Aug 9–13)

### 6.1 Awards
- 🏅 Best Paper (Datasets & Benchmark): **Multi-modal Multi-turn Comprehensive RAG Benchmark**（Meta）
- 🏅 Best Paper (Applied Data Science): **MCGrad: Multicalibration at Web Scale**
- 注：Research Track Best Paper 获奖者未能从公开来源确认。

### 6.2 CTR / LLM4Rec

#### CTR-Sink: Attention Sink for Language Models in Click-Through Rate Prediction (《CTR-Sink：语言模型在点击率预估中的注意力汇聚》)
- **Authors**: Zixuan Li, Binzong Geng, Jing Xiong, Yong He, Yuxuan Hu 等（含 Ngai Wong）
- **Affiliation**: **Ant Group**（蚂蚁集团）+ 香港大学
- **Venue**: KDD 2026
- **arXiv**: https://arxiv.org/abs/2508.03668
- **Abstract & Key Innovations**: 把 attention sink 机制引入 LLM 基 CTR 预估——添加"sink token"为 CTR 任务提供稳定注意力锚点，缓解 LLM 在稠密特征/长序列下的注意力漂移。
- **Comparison**: 面向 LLM4Rec 的架构层改进，与 DLRM/序列基线对照。

#### 继承性参考（非本次新增，见 07-27 digest）
- **GR4AD**: Kuaishou 生成式广告推荐，线上 **+4.2% 广告收入**，400M+ 用户全量部署（arXiv:2602.22732）。

### 6.3 SE/Agent Workshop
#### When Does Restricting a Coding Agent to execute_code Help? (《何时限制编码智能体仅用 execute_code 有帮助？》)
- **Authors**: Yang, Yu, Desell (RIT)
- **Venue**: KDD 2026 SE 3.0 Workshop
- **arXiv**: https://arxiv.org/abs/2607.10569
- **Abstract & Key Innovations**: 对 coding agent 工具面（IDE primitives / Bash / MCP execute_code-only）做受控消融。对照 SWE-agent ACI (+10.7pp) 与 mini-SWE-agent bash-only >74% SWE-bench Verified 的既有结论，测其边界。

---

## 7. ACL 2026 (San Diego, Jul 2–7)

**Scale**: 2,296 main + 2,163 findings。

### 7.1 Best Paper

#### The Imperfective Paradox in Large Language Models (《大语言模型中的未完成体悖论》)
- **Authors**: Bolei Ma, Yusuke Miyao
- **Affiliation**: University of Tokyo / NII
- **Venue**: **ACL 2026 Best Paper** (Long Papers)
- **Link**: https://aclanthology.org/2026.acl-long.689/
- **Abstract & Key Innovations**: 用语言学"未完成体悖论"（进行体下的事件蕴涵模式）揭示 LLM 事件推理的系统性失败：许多 7B–9B 开放模型即使有显式语境线索也违反基本蕴涵模式，更像"预测性叙事引擎"而非忠实逻辑推理者；存在表示-推理分离。

### 7.2 Outstanding Papers

#### DeepPlanning: Benchmarking Long-Horizon Agentic Planning with Verifiable Constraints (《DeepPlanning：可验证约束下的长时程智能体规划基准》)
- **Authors**: Yinger Zhang, Shutong Jiang, Renhao Li 等（含 Junyang Lin）
- **Affiliation**: **Alibaba/Qwen**
- **Venue**: ACL 2026 (Long Papers)
- **arXiv**: https://arxiv.org/abs/2601.18137
- **Abstract & Key Innovations**: 要求主动信息获取 + 局部约束推理 + 全局约束优化的多日旅行规划（120 ZH + 120 EN, 9 APIs）与多产品购物规划（120 EN, 15 APIs），离线沙箱 + 规则验证器。发现 frontier agents "脆弱"：约束级得分高但端到端 case 准确率低。
- **Numbers**: 最佳模型旅行规划全对仅 **35.0%**；Gemini-3-Flash-Preview 购物 60.0%；榜单头部 Claude-4.6-Opus 58.9%、GPT-5.2-high 48.2%。

#### Evolutionary Guided Decoding: Iterative Value Refinement for LLMs (《进化引导解码：LLM 的迭代价值精化》)
- **Affiliation**: **NVIDIA**（Jing Shao）+ Soochow University
- **Venue**: ACL 2026 Outstanding Paper
- **Abstract & Key Innovations**: 值函数在窄输出切片上训练表现不佳；每轮用改进后的值函数生成更好的训练数据，迭代自改进闭环。

#### CAR-bench: Evaluating Consistency and Limit-Awareness of LLM Agents under Real-World Uncertainty (《CAR-bench：现实不确定性下 LLM 智能体的一致性与边界感知评估》)
- **Affiliation**: BMW Research + Augsburg University
- **Venue**: ACL 2026 Outstanding Paper
- **Abstract & Key Innovations**: 车内助手基准：58 个互连工具 + 故意模糊/不可能请求，用 pass³ 评估一致性。最佳 agent 一致性仅 **0.42**，歧义消解是最难技能。

#### Lychee-FD: Hierarchical Acoustic-Semantic Modeling for Full-Duplex SLMs (《Lychee-FD：全双工口语模型的层次化声学-语义建模》)
- **Affiliation**: HIT Shenzhen / Huawei Noah's Ark Lab（推断）
- **Venue**: ACL 2026 Outstanding Paper
- **Link**: https://aclanthology.org/2026.acl-long.419/
- **Abstract & Key Innovations**: 全双工 SLM 共享深度参数导致声学/语义梯度冲突；Lychee-FD 层次化分离 + 专用语义对齐通道。
- **Numbers**: 口语 QA **+7.4%**、交互流畅度 **+28.5%**。

#### CxMP: Linguistic Minimal-Pair Benchmark for Constructional Understanding (《CxMP：构式理解的语言学最小对基准》)
- **Affiliation**: NAIST / NII
- **Venue**: ACL 2026 Outstanding Paper
- **Abstract**: 基于构式语法，检验模型对 let-alone、caused-motion、ditransitive 等由语法形式承载的意义的理解；句法能力早现但构式理解即使规模化仍有限。

#### ViLL-E: Video LLM Embeddings for Retrieval (《ViLL-E：用于检索的视频 LLM 嵌入》)
- **Affiliation**: **Meta** + UCF
- **Venue**: ACL 2026 Outstanding Paper
- **Abstract**: 从 VideoLLM 直接提取检索嵌入（此前 VideoLLM 字幕能力强但在端到端检索上输给文本嵌入检索器）。

#### 其他 Outstanding Papers（仅标题）
- **GeoRA** (Geometry-Aware Low-Rank Adaptation for RLVR, Jiaying Zhang et al.)；**CURE** (Critique-Driven Unified RL for Test-Time Self-Improvement)；**MediEval** (TU Dresden)；**Lying with Truths** (多智能体串通，14 个 LLM 家族 >70% 成功率)。

---

## 8. EMNLP 2025 (Suzhou, Nov 4–9)

### 8.1 Best Paper

#### Infini-gram mini: Exact n-gram Search at the Internet Scale with FM-Index (《Infini-gram mini：基于 FM-Index 的互联网级精确 n-gram 检索》)
- **Authors**: Hao Xu, Jiacheng Liu, Yejin Choi, Noah A. Smith, Hannaneh Hajishirzi
- **Affiliation**: UW / AI2
- **Venue**: **EMNLP 2025 Best Paper**
- **Link**: https://aclanthology.org/2025.emnlp-main.1268/
- **Abstract & Key Innovations**: 用 FM-Index 在 Infini-gram 网络语料上构建互联网级精确 n-gram 索引，索引远小于 suffix-array 方案，支持大规模统计语言模型分析。

### 8.2 Outstanding Papers

#### DeepResearcher: Scaling Deep Research via RL in Real-World Environments (《DeepResearcher：在真实环境中通过强化学习规模化深度研究》)
- **Authors**: Yuxiang Zheng, Dayuan Fu, Xiangkun Hu 等
- **Affiliation**: GAIR / SJTU
- **Venue**: EMNLP 2025 (Main)
- **arXiv**: https://arxiv.org/abs/2504.03160
- **Abstract & Key Innovations**: 首个对 live web search 做端到端 RL（仅 outcome-based reward）的深度研究框架；多智能体 + 专用 browsing agents。真实 web 训练涌现规划、交叉验证、自反思与"诚实"（无答案时拒答）。
- **Numbers**: 相对 prompt-engineering 基线最高 **+28.9**、相对 RAG-RL (R1-Searcher 含 web) **+7.2**；开源 DeepResearcher-7b。

#### LingGym / Measuring Chain of Thought Faithfulness by Unlearning / Mind the Value-Action Gap
- **Venue**: EMNLP 2025 Outstanding Papers
- **Abstract**: 田野语言学元推理基准 (LingGym)；用"遗忘"单个推理步骤做 CoT 忠实度因果测试；LLM 声明的价值观与行动行为的 "value-action gap"。

#### Autoformalization in the Wild (Best Resource Paper)
- **Abstract**: 真实世界数学定义上的自动形式化基准，捕捉受控形式化与杂乱真实定义之间的差距。

---

## 9. SIGIR 2026 (Melbourne, Jul 20–24)

**Scale**: 234 full + 12 perspective + 28 reproducibility + 61 resource + 151 short + 24 demo + 131 industry 论文。Program 含 **CTR Prediction 专场（6 篇）** 与 **Item Tokenization 专场（6 篇）**。

#### SilverTorch: A Unified Model-based System to Democratize Large-Scale Recommendation on GPUs (《SilverTorch：在 GPU 上普惠大规模推荐的全栈系统》)
- **Affiliation**: **Meta**
- **Venue**: SIGIR 2026 (full paper)
- **Abstract & Key Innovations**: 统一 GPU 推荐栈（训练+推理+特征管线）从 CPU 迁移到 GPU，保持稀疏模型语义、降低接入成本。与 TorchRec 同源团队。
- **Numbers**: **23.7× 更高吞吐**、**20.9× 计算成本效率**（vs CPU 方案）。

#### HyFormer: Revisiting the Roles of Sequence Modeling and Feature Interaction in CTR Prediction (《HyFormer：重探序列建模与特征交互在 CTR 预估中的作用》)
- **Affiliation**: **ByteDance**
- **Venue**: SIGIR 2026 (CTR 专场)
- **Abstract**: 统一建模 sequence modeling 与 feature interaction 在 CTR 中的角色（对照 DLRM/DeepFM 系 + 序列模型）。

#### Verifiable Reasoning for LLM-based Generative Recommendation (《LLM 生成式推荐的可验证推理》)
- **Affiliation**: **Meta** + NUS
- **Venue**: SIGIR 2026
- **Abstract**: 为 LLM 生成式推荐加入可验证推理链，应对幻觉与可解释性。

#### Generative Bid Shading in Real-Time Bidding Advertising (《实时竞价广告中的生成式 Bid Shading》)
- **Venue**: SIGIR 2026 (CTR/广告专场)

#### 仅标题确认
- **Beyond Static Best-of-N: Bayesian List-wise Alignment for LLM-based Recommendation** (Chen, Gao, Chen, Yang, He)；**DCGL: Dual-Channel Graph Learning with LLMs**；**ProMax: LLM-derived Profiles with Distribution Shaping**；**Multimodal LLMs with Adaptive Preference Optimization for Sequential Recommendation**；**FedMM: Federated CTR Multi-Market**；**HE-DeepFM: FHE Inference for CTR**。

---

## 10. WWW 2026 (Dubai, UAE, Apr 28–May 2)

> ⚠️ 勘误：悉尼是 WWW 2025。

### 10.1 Awards
- 🏅 Best Paper: **From Retrieval to Generation: Unifying External and Parametric Knowledge for Medical Question Answering**（Lei Li, Xiao Zhou 等）
- 🏅 Best Short Paper: **DualGR: Generative Retrieval with Long and Short-Term Interests Modeling**（Zhongchao Yi 等）
- 🏆 Test of Time: **LINE: Large-scale Information Network Embedding**（Tang et al., 2015）

### 10.2 Notable

#### TESLA: Network Conversion Cascaded Modeling and Debiasing (《TESLA：网络转化级联建模与去偏》)
- **Authors**: Mingxuan Luo, Guipeng Xv, Sishuo Chen 等（含 Zhangming Chan）
- **Affiliation**: **Alibaba（阿里妈妈）**
- **Venue**: WWW 2026
- **arXiv**: https://arxiv.org/pdf/2601.19965 (code: github.com/alimama-tech/NetCVR)
- **Abstract & Key Innovations**: 广告点击→转化→后续 (CVR-RFR cascaded) 建模的两处偏差：**stage-wise debiasing** + **delay-time-aware ranking loss**，直接对齐真实 RFR 目标。
- **Numbers**: NetCVR 上相对 CASCADE **RI-AUC +12.41%**、**RI-PRAUC +14.94%**。

#### PLUM: Adapting Pre-trained Language Models for Industrial-scale Generative Recommendations (《PLUM：为工业级生成式推荐适配预训练语言模型》)
- **Affiliation**: **Google / YouTube**
- **Venue**: WWW 2026 (DOI 10.1145/3774904.3792802)
- **Abstract & Key Innovations**: Semantic IDs + 两阶段 (CPT) 预训练把 PLM 适配为生成式推荐（LFM 路线）。
- **Numbers**: YouTube **数十亿用户** 全量上线——LFM 范式在工业界最大规模落地证据之一。

---

## 11. CIKM 2025 (Seoul, Nov 10–14)

> ⚠️ 勘误：首尔，非贝尔法斯特。

### 11.1 Awards
- 🏅 Best Full Paper: **Reconsidering the Performance of GAE in Link Prediction**（Weishuo Ma, Yanbo Wang, Xiyuan Wang, Muhan Zhang）
- 🏅 Best Student Full Paper: **A Cost-Effective Framework to Evaluate LLM-Generated Relevance Judgements**（Merlo, Marchesin, Faggioli, Ferro）
- Runner-up: **Transferable Deep Clustering Model**

### 11.2 Notable
#### Personalized Multi Modal Alignment Encoding for CTR-Recommendation in WeChat (《微信 CTR 推荐中的个性化多模态对齐编码》)
- **Authors**: Jiawei Zheng, Hao Gu, Lingling Yi, Jie Wen, Chuan Chen
- **Affiliation**: **Tencent**（微信场景）+ 中山大学
- **Venue**: CIKM 2025, pp. 6301–6308
- **Abstract**: 微信场景多模态（文本/图像）对齐编码用于 CTR。

---

## 12. RecSys 2025 (Prague, Sep 22–26)

### 12.1 Awards
- 🏅 **Best Full Paper**（评委全票一致）: **You Don't Bring Me Flowers: Mitigating Unwanted Recommendations Through Conformal Risk Control**（《用共形风险控制抑制不受欢迎的推荐》）
  - **Authors**: Giovanni De Toni, Erasmo Purificato, Emilia Gomez, Andrea Passerini, Bruno Lepri, Cristian Consonni
  - **Affiliation**: University of Trento / FBK / ECAT (JRC)
  - **Abstract**: 用 conformal risk control 抑制用户不想看到的推荐，控制"不受欢迎推荐"风险。获欧盟委员会 ECAT 官方报道，方法学强度 + 社会影响并重。
- 🏅 Best Short Paper: **Beyond Top-1: Addressing Inconsistencies in Evaluating Counterfactual Explanations for Recommender Systems**（Innsbruck）
- 注：Best Industry Paper 未在官方 awards 页列出（not confirmed）。

### 12.2 Notable
#### RESLONGER: Long-sequence Optimized Transformer for GPU-Efficient Recommenders (《RESLONGER：面向 GPU 高效推荐的序列优化 Transformer》)
- **Affiliation**: **ByteDance**
- **Venue**: RecSys 2025
- **Abstract & Key Innovations**: 面向工业超长用户行为序列的 Transformer 架构优化（sequence packing / kernel 优化）。
- **Numbers**: 部署到 ByteDance **10+ 场景**，广告与电商均有 offline + 线上 A/B 正向收益。

---

## 13. General arXiv (Jul–Aug 2026)

### 13.1 LLM 架构 / Scaling

#### Seed 2.0 Model Card (《Seed 2.0 模型卡》)
- **Affiliation**: **ByteDance Seed**
- **arXiv**: https://arxiv.org/abs/2607.00248
- **Abstract**: 面向长尾知识与复杂指令遵循的模型系列，宣称同类中领先的推理与视觉理解能力（Model Card 形式发布）。

#### HiLS-Attention: Hierarchical Sparse Attention Done Right, Toward Infinite Context Modeling (《HiLS-Attention：迈向无限上下文建模的层级稀疏注意力》)
- **Affiliation**: **Tencent Hunyuan**
- **arXiv**: https://arxiv.org/abs/2607.02980
- **Abstract & Key Innovations**: 端到端在语言建模 loss 下学习 chunk 选择的 chunk-wise 稀疏注意力；压缩 chunk key 估计 chunk-mass surrogate，inter/intra-chunk softmax 分解避免完整 QK 计算。原生稀疏训练。
- **Numbers**: 仅 **50B** 续训 token 继承 full-attention 能力，4× 以上超长上下文外推（超 YaRN 扩展），HiLS-Attention-7B 开源。

#### Compute-Optimal Is Not Cluster-Optimal (《计算最优并不等于集群最优》)
- **arXiv**: https://arxiv.org/abs/2608.10605
- **Abstract**: 系统级视角：稀疏 MoE 的 loss-optimal（专家数、路由稀疏度）与考虑加速器利用率、内存、互联约束后的 cluster-optimal 配置不同。

#### Qwen-Audio-VAE Technical Report (《Qwen-Audio-VAE 技术报告》)
- **Affiliation**: **Alibaba (Qwen Team)**
- **arXiv**: https://arxiv.org/abs/2607.11738
- **Abstract**: 低比特率、快速编码的连续音频 autoencoder 套件；因果编解码 + window Transformer + 多判别器；5M 小时多域音频训练。
- **Numbers**: **32 分钟音频仅 541ms 编码**。

#### Linear Attention Architectures: Mechanisms, Trade-offs, and Cross-Layer Routing (《线性注意力架构：机制、权衡与跨层路由》)
- **Affiliation**: ETH Zürich
- **arXiv**: https://arxiv.org/abs/2607.07953
- **Abstract**: 统一 recurrent-memory 记法下分析 DeltaNet / Gated DeltaNet / Kimi Delta Attention / Gated DeltaNet-2 的机制与跨层路由。

### 13.2 Agents & Code Execution

#### SINKFLEX-RL: Efficient RL for Long-Horizon Tool-Use Agents (《面向长程工具使用智能体的高效强化学习》)
- **arXiv**: https://arxiv.org/abs/2608.10357
- **Abstract**: 模块化训练系统：Gymnasium 兼容 wrapper + VERL 式 dataflow + GRPO + 内存优化 FlexAttention 路径，处理长多轮上下文与延迟可验证奖励。

#### Self-Evolving Coding Agents: A Survey (《自演化编码智能体：综述》)
- **arXiv**: https://arxiv.org/abs/2608.03392
- **Abstract**: 对象中心 taxonomy（framework/memory/skills/tools/models/collaboration 演化）+ SE 特有挑战（反馈可靠性、benchmark 过拟合、安全、成本、泛化）。

#### Understanding the Architecture of Coding Agents (《理解编码智能体的架构》)
- **arXiv**: https://arxiv.org/abs/2608.10934
- **Abstract**: 引入 Ark (Agent Research Kit) 最小开源 coding agent 与 ArkBench（10 任务）。
- **Numbers**: Ark + gpt-5.4-mini 解决 **8/10** ArkBench 任务。

#### Stealing Reasoning Traces from Proprietary LLM APIs (《从专有 LLM API 窃取推理轨迹》)
- **Affiliation**: ELLIS Tübingen / MPI-IS 等
- **arXiv**: https://arxiv.org/abs/2608.09867
- **Abstract**: 加密 reasoning block（OpenAI/Anthropic/Google）在提供方生态内架构兼容，可在无 jailbreak 下 1:1 恢复隐藏推理；含 replay 与 side-channel 攻击。披露后厂商已推缓解措施（Fig.1 不可复现）。

#### EMPO²: Exploratory Memory-Augmented LLM Agent via Hybrid On- and Off-Policy Optimization (《EMPO²：混合在线/离线策略优化的探索式记忆增强智能体》)
- **Affiliation**: **Microsoft Research**
- **arXiv**: https://arxiv.org/abs/2602.23008 (ICLR 2026)
- **Numbers**: ScienceWorld **+128.6%**；WebShop +11%。

#### RA-RFT: Learning to Reason by Analogy via Retrieval-Augmented RL Fine-Tuning (《通过检索增强强化微调学习类比推理》)
- **Affiliation**: **Meta Superintelligence Labs** + Rice
- **arXiv**: https://arxiv.org/abs/2606.13680
- **Abstract**: 用"预期推理收益"而非语义重叠排序上下文，再用可验证结果 RL 微调。
- **Numbers**: AIME 2025 avg@32：Qwen3-1.7B **+7.1**、Qwen3-4B **+2.8**（相对 GRPO）。

### 13.3 Generative / World Models / Multimodal

#### Visual prompt engineering for video models (VIPE) (《视频模型的视觉提示工程》)
- **Affiliation**: **Google DeepMind**
- **arXiv**: https://arxiv.org/abs/2607.25537
- **Abstract**: 自动改写任务图像本身（如草图→照片级参考）而非文本 prompt 来引导视频模型；部分视觉推理基准上超越文本 prompt 工程甚至 test-time scaling。

#### MiniWorld: Democratizing the Training of Video World Models from Scratch (《MiniWorld：视频世界模型从零训练的普及化》)
- **arXiv**: https://arxiv.org/abs/2608.01127
- **Abstract**: 从零训练视频世界模型的训练/推理代码库 + 预训练 checkpoint。

#### PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives (《PlayWorld：基于智能体玩家的长程目标世界模型基准测试》)
- **Affiliation**: **Kuaishou** + 高校
- **arXiv**: https://arxiv.org/abs/2608.13552
- **Abstract**: 让 agent "玩家"在生成环境中追求长视界目标，把评估从帧级保真度转向 goal-directed rollouts（与 08-14 game-rl-daily 交叉参考）。

#### V-RAE: Rethinking Video Latent Spaces for Generation (《V-RAE：重新思考用于生成的视频隐空间》)
- **Affiliation**: NUS / Oxford
- **arXiv**: https://arxiv.org/abs/2608.13556
- **Abstract**: 在冻结视觉基础模型之上构建视频表示 autoencoder，冻结语义表示可支撑多种视频建模任务；新 tFVD 指标。

#### OmniScientist: An Omni-Modal Omni-Discipline AI Scientist (《OmniScientist：全模态全学科 AI 科学家》)
- **Affiliation**: NUS / Oxford
- **arXiv**: https://arxiv.org/abs/2608.13558
- **Abstract**: 端到端全模态管线，从原始证据到论文的完整工作流；36 个真实案例评估。

### 13.4 Recommendation / CTR / Ads

#### LLaTTE: Scaling Laws for Multi-Stage Sequence Modeling in Large-Scale Ads Recommendation (《LLaTTE：大规模广告推荐中多阶段序列建模的 Scaling Laws》)
- **Affiliation**: **Meta AI**
- **arXiv**: https://arxiv.org/abs/2601.20083
- **Abstract**: 广告推荐多阶段序列建模（候选/行为/广告序列）的 power-law scaling laws 与模型规模扩展策略。
- **Numbers**: Facebook Feed 与 Reels **+4.3% 转化提升**；已作为 **Meta 最大用户模型** 部署。

#### EST: Towards Efficient Scaling Laws in CTR Prediction via Unified Modeling (《EST：统一建模的 CTR 高效缩放定律》)
- **Affiliation**: **Alibaba（淘宝展示广告）**
- **arXiv**: https://arxiv.org/abs/2602.10811
- **Numbers**: 线上 **RPM +3.27%**、**CTR +1.22%**。

#### WhisperRec: Latent Reasoning for Efficient Foundation Recommendation Models (《WhisperRec：面向高效基础推荐模型的潜在推理》)
- **Affiliation**: **Kuaishou**（含 Wenwu Ou, Peng Jiang）
- **arXiv**: https://arxiv.org/abs/2607.26621
- **Abstract**: 把 CoT 蒸馏到潜在空间实现 foundation recommendation model 的潜在推理，提升效率。

#### MixFormer: Co-Scaling Up Dense and Sequence Modeling (《MixFormer：稠密与序列建模联合放大》)
- **Affiliation**: **ByteDance**
- **arXiv**: https://arxiv.org/abs/2602.14110
- **Numbers**: 已在**抖音与抖音极速版**上线；A/B 提升活跃天数与 App 使用时长。

#### Autobidding Equilibria in Sponsored Shopping (《赞助购物中的自动出价均衡》)
- **Affiliation**: Google 系（Paes Leme 等）
- **arXiv**: https://arxiv.org/abs/2602.21966
- **Abstract**: 证明赞助购物拍卖中 autobidding equilibria 存在性，GSP 与 VCG 下 **tight PoA = 2**。

#### Towards Generalizable and Efficient Large-Scale Generative Recommenders (《迈向通用且高效的大规模生成式推荐系统》)
- **Affiliation**: **Netflix Research**
- **arXiv**: https://arxiv.org/abs/2605.23312
- **Numbers**: 生成式推荐器从 2M 扩到 **1B backbone**；Task A **MRR +22.5%**；100 万用户一周线上 shadow test。

#### Towards Efficient Reasoning in LLM-Based Recommender Systems via Model Merging (《基于模型合并的 LLM 推荐系统高效推理》)
- **Affiliation**: University of Queensland
- **arXiv**: https://arxiv.org/abs/2608.10447

### 13.5 其他值得注意

- **Learning to Coordinate Symbolic Tools: LLM Agents for Verified Sum-of-Squares Certificates** — arXiv:2608.00326（符号工具协调 + 形式化验证）
- **Numeracy in Large Language Models** — arXiv:2608.13129（数值能力综述 + Numerical Grounding Framework）
- **Qwen3.8-Max**（08-03 发布，2.4T sparse MoE / 95B active，1M context）— 无 arXiv card 确认（第三方跟踪）
- **MiniMax M3 / Gemini 3.7 Flash GA / GPT-5.6 / Grok 4.6 / Kimi K3** — 详见同目录 tech-report-digest

---

## Cross-Venue Trends (2026-08-16)

1. **Diffusion LLM 从"任意顺序"转向"顺序化 + RL"**：The Flexibility Trap (ICML Outstanding) 反直觉地证明任意顺序限制推理；JustGRPO、WeDLM、Learning Unmasking Policies (Apple) 共同指向 dLLM 需向标准因果/顺序化 + RL 靠拢。ICML 两篇 Outstanding Paper 都与 diffusion 理论/RL 相关。
2. **World Models 全面爆发**：CVPR (DeltaTok, HoloCine, GenieDrive, VerseCrafter) × ICML (LIVE) × KDD/arXiv (PlayWorld, MiniWorld, Alaya-EVOKE) 多线推进；评估向 agent-player long-horizon rollouts 迁移（PlayWorld）。
3. **Scaling Laws 进入广告/推荐/多语言**：LLaTTE (Meta) / EST (Alibaba) / ATLAS (DeepMind) 把 Chinchilla 式定律扩展到多阶段广告序列、CTR 与多语言迁移；"compute-optimal ≠ cluster-optimal" 反思 MoE 系统设计。
4. **RLVR 效率军备竞赛**：MaxRL (20× test-time scaling)、GEPA (35× fewer rollouts)、Q-RAG (单卡)、BARL、DECS——从算法、prompt、检索多角度压缩 RL 成本。
5. **生成式推荐工业落地继续扩大**：PLUM (Google/YouTube 数十亿用户)、WhisperRec (Kuaishou)、GR4AD (Kuaishou)、LLaTTE (Meta)——Semantic ID + autoregressive 范式成为工业标准。
6. **Agent 评估转向可靠性/一致性**：CAR-bench (pass³)、DeepPlanning (约束验证)、LLMs Get Lost in Multi-Turn (ICLR Outstanding)、CURVE (文化长视频)——从单次成功率转向重复一致性、边界感知与多轮恢复能力。
7. **CTR 架构注意力锚点与扩散融合**：CTR-Sink (Ant)、iFusion (diffusion 兴趣融合, +2.44% CTR) 表明 attention sink 与生成式建模进入工业 CTR。

---

## Key Industrial Deployments (updated 2026-08-16)

| Paper | Company | Scale | Metric |
|-------|---------|-------|--------|
| Gated Attention | Alibaba Qwen | Qwen3-Next production | Best Paper NeurIPS 2025 |
| GR4AD | Kuaishou | 400M+ users | +4.2% ad revenue |
| PLUM | Google/YouTube | Billions of users | Full deployment |
| LLaTTE | Meta | Largest user model | +4.3% conversion (Feed+Reels) |
| MixFormer | ByteDance | Douyin + Lite | Active days & usage A/B wins |
| EST | Alibaba Taobao Ads | Online | RPM +3.27%, CTR +1.22% |
| iFusion | (industrial) | Online A/B | CTR +2.44%, eCPM +2.61% |
| TESLA | Alibaba Alimama | NetCVR | RI-AUC +12.41% |
| RESLONGER | ByteDance | 10+ scenarios | Online A/B wins |
| SilverTorch | Meta | GPU rec stack | 23.7× throughput, 20.9× cost-eff |

---

## Cross-references

- 继承 [[synthesis/2026-07-27/conference-digest]] 与 [[synthesis/2026-07-26/conference-digest]]（ICML/ICLR/AAAI/NeurIPS/CVPR 详情基线）
- 同日板块：[[synthesis/2026-08-16/arxiv-daily]]、[[synthesis/2026-08-16/arxiv-ai-search]]、[[synthesis/2026-08-16/arxiv-paper-check]]（CTR/推荐当日新论文）、[[synthesis/2026-08-16/game-rl-daily]]（PlayWorld/Alaya-EVOKE 世界模型）、[[synthesis/2026-08-16/tech-report-digest]]（MiniMax M3 / Gemini 3.7 Flash / GPT-5.6 / Kimi K3）
