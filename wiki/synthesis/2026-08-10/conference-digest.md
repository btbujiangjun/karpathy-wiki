---
title: "Conference Digest 2026-08-10：KDD 2026 进行时 + 顶会奖项最终确认 + 前沿大厂 arXiv 精选"
type: synthesis
created: 2026-08-10
updated: 2026-08-10
sources: []
tags: [conference-digest, kdd-2026, icml-2026, neurips-2025, cvpr-2026, sigir-2026, recsys-2026, arxiv, llm, agents, game-theory, diffusion]
---

# Conference Digest — 2026-08-10

本期在 [2026-08-01 digest](../2026-08-01/conference-digest.md)（ICML/ACL/NeurIPS/CVPR/ICLR/AAAI 最佳论文基线）、[2026-08-03 digest](../2026-08-03/conference-digest.md)（KDD 工业界、RecSys/CIKM/SIGIR 2025 奖项）与 [2026-08-04 digest](../2026-08-04/conference-digest.md)（顶会获奖全谱补全）基础上，聚焦 **KDD 2026 开幕进行时**（Jeju, 2026-08-09 ~ 13，奖励 8/13 公布），最终确认 **ICML 2026 / NeurIPS 2025 / CVPR 2026 / SIGIR 2026 奖项名单**，并精选 8 篇前沿大厂与研究方向 arXiv 新作（与同日 [arxiv-paper-check](./arxiv-paper-check.md) 的 36 篇 CTR/Rec 论文**零重叠**）。

---

## 1. 顶会奖项最终确认（截至 2026-08-10）

### 1.1 ICML 2026 — 官方完整名单（blog.icml.cc 2026-07-05 发布）

**2 Outstanding Papers**（08-01 digest 已列，本期确认 + 补作者/机构）：

- *The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models* — Zanlin Ni, Shenzhi Wang, Yang Yue, … , Gao Huang 等（Tsinghua / ByteDance 等）— 重新审视 diffusion 语言模型「任意 token 顺序」的价值：固定顺序（flexibility 被限制）反而更好，重构 DLM 的生成顺序设计（**[08-01 digest](../2026-08-01/conference-digest.md) 已详述**）。
- *High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions* — Fan Chen, Sinho Chewi, Constantinos Daskalakis, Alexander Rakhlin（MIT）— 扩散模型与 log-concave 分布的高精度采样理论。

**5 Honorable Mentions**（53 篇初选候选，来自 8 个 subject area）：含 08-01 已列的 *Obfuscation Atlas*、*How Much Can LMs Memorize*、08-04 补的 *Motion Attribution for Video Generation*，以及另两篇（名单见 ICML 官方页面）。

> 业界参与备忘：NVIDIA 74 篇 ICML 2026 论文（08-04 已记）。

### 1.2 NeurIPS 2025 — 4 Best + 3 Runners-up 全确认（blog.neurips.cc 2025-11-26）

- **Best Papers（4）**：*Artificial Hivemind*（LLM 同质化）、*Gated Attention for LLMs*（非线性的门控注意力：non-linearity、sparsity、attention-sink-free）、*1000 Layer Networks for Self-Supervised RL*、*Why Diffusion Models Don't Memorize*。
- **Runners-up（3）**：*Does RL Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?*（Yue, Song, Huang）、*Optimal Mistake Bounds for Transductive Online Learning*（Chase, Hanneke, Moran, Shafer）、*Superposition Yields Robust Neural Scaling*（叠加产生稳健的神经缩放律）。
- 委员会：Jacob Andreas、Sander Dieleman、Mirella Lapata、Ulrich Paquet 等。

### 1.3 CVPR 2026 — 2 篇顶奖确认（cvpr.thecvf.com）

- **Best Paper**：*Efficiently Reconstructing Dynamic Scenes One D4RT at a Time* — Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, …, Joëlle Barral, Raia Hadsell, Zoubin Ghahramani, Andrew Zisserman, Mehdi Sajjadi（Google DeepMind / UCL / Oxford）— 逐帧 D4RT 稀疏表示的动态场景重建。
- **Best Student Paper**：*Native and Compact Structured Latents for 3D Generation*（TRELLIS.2）— Xiang, Chen, …, Yang 等（Tsinghua / MSRA / USTC / Microsoft AI）— 结构化 3D latent + **O-Voxel** 自监督初始化。
- 规模：16,092 投稿 → 4,089 录用（≈25.4%），较 2025 **+42%**；74 篇候选。

### 1.4 SIGIR 2026 — 奖项终版（Melbourne 2026-07-20 ~ 24）

- **Best Paper**：*Bridging Vocabulary Gaps*（词表错配论，ModernBERT BEIR 52.4 nDCG +4.7 @<0.2% token）— **[08-07 digest](../2026-08-07/conference-digest.md) 已详述**。
- **Test of Time Award**：*Learning to Rank with Selection Bias in Personal Search* — Xuanhui Wang, Michael Bendersky, Don Metzler（Google，SIGIR 2016）— 个人搜索中的选择偏差 LTR；8/13 颁奖晚宴接受（Marc Najork 代领）。
- **SynthIR Workshop Best Paper**：*Vision-Free CIR*（2607.12621）— 08-07 已记。

### 1.5 KDD 2026 — **开幕进行时**（Jeju, 2026-08-09 ~ 13）

- **Best Paper 尚未公布**：KDD 2026 奖励于 **8/13（周三）**揭晓，本期记为 pending；当前只有 Research Track 提前公布的 **PiPNN**（HashPartitioning，**[08-04 digest](../2026-08-04/conference-digest.md) 已详述**，arXiv:2602.21247）。
- 结构备忘：两个投稿周期（Feb + July）；tracks = Research / Applied Data Science / **Datasets & Benchmarks（新）** / **AI for Sciences（新）**；Vol.1 1,215 → 256（≈21%）。
- 主旨三人组：Jeff Dean、Jingren Zhou（Agentic Data Stack + AgentScope）、Regina Barzilay（医疗 AI）— **[08-07 digest](../2026-08-07/conference-digest.md) 已详述**。
- 工业界深潜（PerFusion / MORE / ColdNet / FOUNDv2 / HLTM / Pinterest Canvas 等）见 [08-03 digest](../2026-08-03/conference-digest.md) 与 [08-07 digest](../2026-08-07/conference-digest.md)。

### 1.6 RecSys 2025 / 2026

- **RecSys 2025**（确认）：Best Full = *You Don't Bring Me Flowers: Mitigating Unwanted Recommendations Through Conformal Risk Control*（De Toni, Purificato, Gomez, Passerini, Lepri, Consonni）；Best Short = *Beyond Top-1: Addressing Inconsistencies in Evaluating Counterfactual Explanations*（Mohammadi, Peintner, Müller, Zangerle）。
- **RecSys 2026**（20 届）：Minneapolis，工业 track 已在同日 [arxiv-paper-check](./arxiv-paper-check.md) 覆盖（SYF 2608.06632 对话式推荐、Progressive Alignment 2608.06792 三阶段对齐、OARS MISO 2608.07035）。

---

## 2. 前沿大厂 / 方向 arXiv 精选（2026-07 ~ 08，全库去重）

### 2.1 Google — 博弈论 × Foundation Model（Aug 2026）

- **A game theory for foundation models shows new paths to rational cooperation through similarity inference**（arXiv:2608.03958，2026-08-05）— Google Paradigms of Intelligence Team：A. Meulemans, M. Wołczyk, M. Weis, R. Nasser, …, M. Hutter, J. Manyika, R. Saurous, J. Sacramento, B. Agüera y Arcas（+ Mila / Université de Montréal / CIFAR / ETH Zürich / McGill / Santa Fe Institute）。
- **核心发现**：使用 **optimal planning** 的 FM agents 在 social dilemmas（囚徒困境等）中**自发收敛到稳定合作**——与经典博弈论「理性自利者背叛」的预测相反；动机是 agents 通过 **similarity inference**（相似性推断）识别出彼此共享相似偏好与决策过程，从而把博弈变成可协调的。
- **理论框架**：引入 **embedded Bayesian agent**（嵌入式贝叶斯主体）视角：agent 的决策由其对环境的模型（包括对其他 agent 的模型）驱动，理性合作成为内嵌博弈的均衡；替代传统 Nash 均衡作为多 agent 系统的解概念。
- 与 [08-05 digest](../2026-08-05/arxiv-daily.md) 引用的 DeepMind 同期工作（embedded equilibrium 取代 Nash）呼应，构成「合作 / 博弈均衡重定义」主线。

### 2.2 NVIDIA — 多智能体世界模型 γ-World

- **γ-World: Generative Multi-Agent World Modeling Beyond Two Players**（research.nvidia.com/labs/sil/projects/gamma-world；NVIDIA + Tsinghua + U Toronto + Vector Institute）。
- **两大创新**：①**Simplex Rotary Agent Encoding**（单纯形旋转 Agent 编码）— 把 2-agent 的 RoPE 扩展为 permutation-symmetric（置换对称）的单纯形表示，agent 身份编码天然支持任意数量玩家、无需重训练；②**Sparse Hub Attention**（稀疏枢纽注意力）— 跨 agent 的 token 交互从 quadratic 降到 linear，规模化到多玩家。
- **结果**：**24 FPS** 实时 rollout；**zero-shot 从 2 玩家扩展到 4 玩家**。
- 定位：把生成式世界模型（如 diffusion / autoregressive world models）从单智能体或双玩家博弈（AlphaGo/chess）推进到 **multi-agent（>2）generative simulation**——游戏 NPC、MARL 训练环境的新底座。

### 2.3 ByteDance — TokenMixer-Large 工业大 ranking 模型（arXiv:2602.06563）

- **TokenMixer-Large: Scaling Up Large Ranking Models in Industrial Recommenders** — Yuchen Jiang, Jie Zhu, Xintian Han, Hui Lu, Kunmin Bai, …, Zhe Chen, Yuchao Zheng, Peng Xu（ByteDance AML）。
- **三个修复点**（在 TokenMixer 中）：①sub-optimal residual design（残差设计欠优）→ **mixing-and-reverting**（先混合再回退）；②deep model 中 gradient updates 不足 → **inter-layer residuals**（层间残差）；③MoE sparsification 不完整 → 完整的 MoE 稀疏化。
- 承接 **Wukong / HiFormer / DHEN** 的「大 ranking model scaling law」主线（**[08-03 digest](../2026-08-03/conference-digest.md) 已梳理该 scaling 谱系**）。

### 2.4 Tencent Hunyuan — 长上下文连续预训练动力学（arXiv:2604.02650）

- **Revealing the Learning Dynamics of Long-Context Continual Pre-training** — Yupu Liang, Shuang Chen, Guanwei Zhang, Shaolei Wang, Suncong Zheng（Tencent Hunyuan；模型 **Hunyuan A13B**，约 80B 总参数，200B-token 训练轨迹）。
- **分层分析框架**：behavioral（行为）/ probabilistic（概率）/ mechanistic（机制）三层；NIAH 测试在数十 B tokens 时就达到「表现饱和」，但 PPL 在 **150B+ tokens** 才真正收敛——**deceptive saturation（欺骗性饱和）**：表层指标（NIAH）先于真实收敛。
- **可操作结论**：**retrieval heads（检索头）可作为低成本的训练监控信号**，用于判断长上下文训练是否真正完成。

### 2.5 Apple — 多模态 LLM 对齐综合研究（arXiv:2407.02477）

- **Understanding Alignment in Multimodal LLMs: A Comprehensive Study** — Amirloo, Fauconnier, Roesmann, Kerl, Boney, Qian, Wang, Dehghan, Yang, Gan, Grasch（Apple，Apple ML Research 2026-08-03 发布）。
- **贡献**：系统分解 MLLM 对齐中 **offline（DPO 类）vs online（PPO 类）** 的差异与适用场景；以 **hallucination（幻觉）** 为核心评估维度，给出多模态偏好优化（multimodal preference optimization）的指导原则。

### 2.6 长时程 Agent Harness — OneDayAgent（arXiv:2608.05013，2026-08-04）

- **OneDayAgent: Towards a Long-Horizon Harness for Autonomous Agents** — 104 个任务（AgentIF-OneDay）；GLM-5.2 后端 → **SOTA 0.821**；harness 在 5 个后端 LLM（3 个家族）上泛化。
- 定位：与 [08-06 paper-check](../2026-08-06/arxiv-paper-check.md) 的 harness 评测生态（ContextWeave 1,005 任务、OmniaBench 等）互补——**长时程 Agent 基建从「能力」转向「验收基础设施」**。

### 2.7 Alibaba — Qwen3 Technical Report（arXiv:2505.09388，背景锚点）

- Qwen3：0.6B ~ 235B（dense + MoE），**thinking / non-thinking 统一模式**（user-controllable thinking budget），119 种语言；作为 ByteDance/腾讯之外的**开源 MoE 旗舰基线**，与 K3、Qwen3.8-Max（[tech-report-digest](../2026-08-08/tech-report-digest.md)）对照。报告为 2025-05 背景资料，非本期新增。

---

## 3. 推荐系统 / 广告 / CTR 新作（与同日 paper-check 零重叠）

| 论文 | 作者 / 机构 | Venue | 核心贡献 |
|------|------------|-------|---------|
| **ThinkRec: Thinking-based recommendation via LLM**（dl.acm.org/doi/10.1145/3774904.3792070） | — | **WWW 2026** | LLM4Rec 从 System 1（浅层直接排序）走向 **System 2 thinking**（深度推理后再推荐）：把推理阶段显式引入推荐链路。 |
| **Hypothesis-Driven Shelf Generation for Personalised Recommendation**（arXiv:2607.25823） | Spotify | arXiv | Spotify Home 的 **shelf 生成流水线**：4 阶段 = hypothesis generation（用户假设生成）→ catalogue fulfilment（目录满足）→ shelf alignment（货架对齐）→ offline serving（离线服务）；把「规划」与「检索」解耦，用 frontier-LLM 蒸馏成紧凑生产模型。 |
| **Denoising Implicit Feedback for Cold-start Recommendation (DIF)**（arXiv:2606.19658） | — | KDD-adjacent | 冷启动去噪：用 **content-similar warm items** 为冷启动 item 构造 pseudo-label，并引入 confidence + uncertainty 建模；缓解冷启动下隐式反馈噪声过大的问题。 |

> 同日 [arxiv-paper-check](./arxiv-paper-check.md) 已覆盖 36 篇（含 RecSys 2026 工业 track 的 SYF / Progressive Alignment / MISO、ByteDance TM20K、Huawei HD-Rec、Meta OARS 等），本期不重复。

---

## 4. 代码执行 / 基准方向

- **SURGE: On the Potential of Large Language Models as General-Purpose Surrogate Code Executors**（arXiv:2502.11167v5）— 1,160 道题、**8 个评估维度**、21 个 open + proprietary LLM；结论：LLM 作为 **surrogate code executor（代理代码执行器）** 在部分场景可替代真实解释器（节省算力/规避沙箱），但可靠性随任务类型显著分化。与 [08-04 digest](../2026-08-04/conference-digest.md) 的 CARE（shell 命令预执行验证）同属「代码执行安全/可靠性」线。

---

## 5. 顶会获奖全景导航（截至 2026-08-10）

| 会议 | 状态 | 覆盖位置 |
|------|------|---------|
| ICML 2026 | ✅ 完整（2 Outstanding + 5 HM） | 本期 1.1 + [08-01](../2026-08-01/conference-digest.md) + [08-04](../2026-08-04/conference-digest.md) |
| NeurIPS 2025 | ✅ 完整（4 Best + 3 RU + ToT） | 本期 1.2 + [08-01](../2026-08-01/conference-digest.md) |
| CVPR 2026 | ✅ 完整 | 本期 1.3 + [08-01](../2026-08-01/conference-digest.md) + [08-04](../2026-08-04/conference-digest.md) |
| ACL 2026 | ✅ 完整 | [08-01](../2026-08-01/conference-digest.md) + [08-04](../2026-08-04/conference-digest.md) + [08-05](../2026-08-05/conference-digest.md) |
| EMNLP 2025 | ✅ 完整 | [08-04](../2026-08-04/conference-digest.md) |
| WWW 2026 | ✅ 完整 | [08-04](../2026-08-04/conference-digest.md) |
| AAAI 2026 | ✅ 完整 | [08-01](../2026-08-01/conference-digest.md) + [08-04](../2026-08-04/conference-digest.md) |
| ICLR 2026 | ✅ 完整 | [08-01](../2026-08-01/conference-digest.md) + [08-04](../2026-08-04/conference-digest.md) |
| KDD 2026 | 🕐 进行中，**8/13 公布奖励** | 本期 1.5 + [08-03](../2026-08-03/conference-digest.md) + [08-04](../2026-08-04/conference-digest.md) + [08-05](../2026-08-05/conference-digest.md) + [08-07](../2026-08-07/conference-digest.md) |
| SIGIR 2026 | ✅ 完整 | 本期 1.4 + [08-07](../2026-08-07/conference-digest.md) |
| CIKM 2025 | ✅ 完整 | [08-03](../2026-08-03/conference-digest.md) + [08-05](../2026-08-05/conference-digest.md) |
| RecSys 2025 | ✅ 完整 | 本期 1.6 + [08-03](../2026-08-03/conference-digest.md) |
| RecSys 2026 | 🕐 工业 track 论文已覆盖 | [arxiv-paper-check](./arxiv-paper-check.md) |

---

## 6. 综合趋势

1. **2026 奖项全部落地**，只剩 KDD 2026（8/13）一个悬念；CVPR 录用量 +42%、AAAI 录用率 17.6% 三年最低，规模与门槛双上行。
2. **博弈论 × Foundation Model 成为理论热点**：Google（embedded Bayesian agent / similarity inference → 理性合作）与 DeepMind（embedded equilibrium）同步重新定义多 agent 均衡，替代 Nash 作为 LLM 社会的解概念。
3. **生成式世界模型走向 multi-agent（>2）**：NVIDIA γ-World 的置换对称 agent 编码 + 稀疏 hub attention 把生成式模拟从双玩家扩展到任意 N，配合 24 FPS 实时 rollout，指向「世界模型即训练环境」。
4. **长上下文训练存在「欺骗性饱和」**：Tencent 的 NIAH-vs-PPL 分层观测提醒业界用表层指标判断收敛会误判；retrieval heads 成为低成本监控信号。
5. **推荐系统进入 System 2 / 假设驱动时代**：ThinkRec（WWW 2026）与 Spotify Hypothesis-Driven Shelf 都把「推理/规划」从 ranking 中显式分离出来——与同日 paper-check 中 SYF 的 agentic conversational rec 同一条曲线。
6. **代码执行可靠性**（SURGE surrogate executor、CARE 预执行验证）与长时程 Agent harness（OneDayAgent）继续巩固「验收基础设施」共识。

---

## 7. 关键链接

- ICML 2026 Awards：https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/
- NeurIPS 2025 Best Paper Awards：https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/
- CVPR 2026 Best Papers：https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers
- KDD 2026（Jeju 8/9-13）：https://kdd2026.kdd.org/
- SIGIR Awards：https://sigir.org/awards/best-paper-awards/
- RecSys Best Papers：https://recsys.acm.org/best-papers/
- Google game theory for FMs：https://arxiv.org/abs/2608.03958
- NVIDIA γ-World：https://research.nvidia.com/labs/sil/projects/gamma-world/
- TokenMixer-Large：https://arxiv.org/abs/2602.06563
- Tencent Long-Context CPT：https://arxiv.org/abs/2604.02650
- Apple MLLM Alignment：https://arxiv.org/abs/2407.02477
- OneDayAgent：https://arxiv.org/abs/2608.05013
- ThinkRec（WWW 2026）：https://dl.acm.org/doi/10.1145/3774904.3792070
- Spotify Shelf Generation：https://arxiv.org/abs/2607.25823
- DIF Cold-start Denoising：https://arxiv.org/abs/2606.19658
- SURGE Surrogate Code Executors：https://arxiv.org/abs/2502.11167
- Qwen3 Technical Report：https://arxiv.org/abs/2505.09388

---

## 相关页面

- [2026-08-01 Conference Digest](../2026-08-01/conference-digest.md)（ICML/ACL/NeurIPS/CVPR/ICLR/AAAI 最佳论文基线）
- [2026-08-03 Conference Digest](../2026-08-03/conference-digest.md)（KDD 2026 工业界、RecSys/CIKM/SIGIR 2025 奖项）
- [2026-08-04 Conference Digest](../2026-08-04/conference-digest.md)（顶会获奖全谱补全）
- [2026-08-07 Conference Digest](../2026-08-07/conference-digest.md)（KDD 开幕前全景 + SIGIR 2026 终版）
- [2026-08-10 arXiv Paper Check](./arxiv-paper-check.md)（同日 36 篇 CTR/Rec 精选，零重叠）
