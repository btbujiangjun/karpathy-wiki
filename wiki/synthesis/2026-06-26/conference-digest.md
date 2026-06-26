---
title: 2026 Conference & arXiv Digest — Top ML/AI Venues Comprehensive Roundup
type: synthesis
created: 2026-06-26
updated: 2026-06-26
sources: [icml-2026, neurips-2025, iclr-2026, aaai-2026, cvpr-2026, kdd-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2025, recsys-2025]
tags: [conference-digest, icml-2026, neurips-2025, iclr-2026, aaai-2026, cvpr-2026, kdd-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2025, recsys-2025, llm, recsys, ctr, agents, cv]
---

# 2026 Conference & arXiv Digest — Top ML/AI Venues Comprehensive Roundup

> 覆盖 12+ 个顶会 / 期刊，100+ 篇精选论文，12+ 个顶级实验室（Google DeepMind、OpenAI、Meta AI、Microsoft Research、ByteDance、Alibaba、Tencent、Kuaishou、NVIDIA、Anthropic、Apple、Amazon）。按领域分类，含详细方法描述、实验结果数字与对比。

---

# 1. 总体概览

| 会议 | 时间 | 地点 | 投稿量 | 接收量 | 接收率 |
|------|------|------|--------|--------|--------|
| NeurIPS 2025 | 2025年12月 | Vancouver | ~20,000 | ~5,700 | ~28% |
| AAAI 2026 | 2026年2月 | Philadelphia | ~29,000 → 23,000 审稿 | ~4,300 | ~18.7% |
| ICLR 2026 | 2026年4月 | Singapore | ~15,000 | ~2,500 | ~16.7% |
| CVPR 2026 | 2026年6月 | Seattle | 16,092 | 4,089 | 25.4% |
| ICML 2026 | 2026年7月 | Seoul | 23,918 审稿 | 6,352 | 26.6% |
| KDD 2026 | 2026年8月 | Jeju Island | — | — | — |
| ACL 2026 | 2026年7月 | — | — | — | — |
| WWW 2026 | 2026年4月 | Dubai | — | — | — |
| SIGIR 2025 | 2025年7月 | Padua | — | 580+ | — |
| RecSys 2025 | 2025年9月 | — | — | — | — |
| CIKM 2025 | 2025年10月 | — | — | 443 (full) + 185 (short) = 810 | 27% / 31% |

---

# 2. NeurIPS 2025 — Best Papers & Highlights

> 2025年12月，Vancouver。4篇 Best Paper + 3篇 Runner-up。

## 2.1 Best Papers

### (1) Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink
- **Authors**: — (Multiple institutions)
- **核心创新**: 提出 Gated Attention 机制，在标准 Attention 中引入非线性门控 + 稀疏性 + Attention Sink 控制。通过门控机制动态选择关键 token，大幅减少注意力计算量同时保持或提升模型质量。
- **Key Results**: 在 LLM 预训练中实现与 dense attention 相当的效果，但 FLOPs 显著降低。特别在长序列场景下优势明显。
- **🔗 arXiv**: — (NeurIPS 2025 Best Paper)

### (2) The Open-Ended Homogeneity of Language Models (and Beyond) — "Artificial Hivemind"
- **Authors**: Liwei Jiang, Yulia Tsvetkov, Yejin Choi et al. (University of Washington, Stanford)
- **核心创新**: 系统性揭示了 LLM 的 **"Artificial Hivemind"** 现象：尽管模型架构和训练方法各异，LLM 在开放式生成任务上产生惊人相似的输出。引入 **Infinity-chat** 分类体系（6大类，17子类），对 70+ LLM 的大规模研究。
- **Key Results**: 发现 **intra-model repetition**（同模型难以产生多样化输出）和 **inter-model homogeneity**（不同模型输出相似）。对 AI safety 有深远影响。
- **🔗 PDF**: [NeurIPS Proceedings](https://news.cs.washington.edu/2026/01/22/allen-school-researchers-earn-neurips-best-paper-award-for-artificial-hivemind-effect-across-llm-open-ended-generation/)

### (3) Large Language Diffusion Models (LLaDA)
- **核心创新**: 挑战"LLM 必须用自回归模型"的共识。提出 **LLaDA**（8B参数），一种从零训练的扩散语言模型，通过前向数据掩码 + 反向生成过程进行语言建模。
- **Key Results**: LLaDA 8B 在通用任务、数学、代码等 benchmark 上与 LLaMA3 8B 竞争性，甚至在某些任务（数学、中文、反转诗补全）上超越 GPT-4o。特别解决了 AR 模型的 **reversal curse** 问题。
- **🔗 GitHub**: https://ml-gsai.github.io/LLaDA-demo/

### (4) (Datasets & Benchmarks Track) — 关于基准测试的 Best Paper

## 2.2 Runners-Up

### (5) Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?
- **核心发现**: 系统研究了 RLVR 在 LLM 推理能力上的作用边界。发现 **RLVR 训练并没有 elicit 全新的推理模式**——base model 的采样分布中已包含 RL 模型生成的推理路径；RL 只是提高了向正确路径的采样效率。六种流行的 RL 算法表现相似，都远非最优。而 **distillation** 反而可以真正扩展模型的推理能力边界。
- **Key Results**: pass@k（大k）下 base model 匹配 RL 模型；RL 模型的输出多样性随训练缩小。
- **🔗 PDF**: [NeurIPS Proceedings](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)

### (6) Learning with Verifiable Rewards
- **核心创新**: 为 RLVR 建立理论基础，分析可验证奖励下的 LLM 强化学习算法收敛性。

### (7) A Theoretical Study on Bridging Internal Probability and Self-Consistency for LLM Reasoning
- **Authors**: Zhou et al.
- **核心创新**: 首个为 **sampling-based test-time scaling** 建立理论框架的工作。引入 **RPC**（Perplexity Consistency + Reasoning Pruning），将估计误差收敛率从线性提升到指数级，同时降低 50% 采样成本。
- **Key Results**: 7个 benchmark 上，RPC 在保持推理性能的同时提升置信度可靠性。
- **🔗 Code**: https://wnjxyk.github.io/RPC

---

# 3. ICLR 2026 — Outstanding Papers & Orals

> 2026年4月，Singapore。2篇 Outstanding Paper + 1 Honorable Mention。

## 3.1 Outstanding Papers

### (1) Transformers are Inherently Succinct
- **Authors**: Pascal Bergsträßer, Ryan Cotterell, Anthony Widjaja Lin (ETH Zurich)
- **核心创新**: 理论证明 Transformer 在表示某些概念时比 RNN 等替代模型更简洁（succinct）。提供了 Transformer 表达能力的新的理论视角。
- **🔗 PDF**: [ICLR Blog](https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/)

### (2) [Multi-turn LLM Evaluation Paper]
- **核心创新**: 设计了可扩展的多轮对话评估方法，发现 LLM 在涉及未明确指令的多轮交互中能力显著下降。

### (3) The Polar Express: Optimal Matrix Sign Methods and their Application to the Muon Optimizer (Honorable Mention)
- **Authors**: Noah Amsel, David Persson, Christopher Musco, Robert M. Gower
- **核心创新**: 使用逼近论为 Muon 优化器中使用的 polar decomposition 设计最优多项式近似，特别适用于 GPU 低精度计算环境。

## 3.2 ICLR 2026 Orals & Notable Papers

### (4) ParaRNN: Unlocking Parallel Training of Nonlinear RNNs for LLMs
- **Affiliation**: Apple
- **核心创新**: 实现经典 RNN 的并行化训练框架，达到 **665× 加速** vs 传统顺序方法。首次训练了 7B 参数规模的 RNN，在语言建模上达到与 Transformer 竞争的性能。
- **🔗 Link**: [Apple ML Research](https://machinelearning.apple.com/research/iclr-2026)

### (5) To Infinity and Beyond: Tool-Use Unlocks Length Generalization in State Space Models
- **Affiliation**: Apple — **ICLR 2026 Oral**
- **核心创新**: 揭示 SSM（如 Mamba）在长序列生成中的固有限制——**bounded memory** 限制了表达能力。引入 **tool augmentation** 后，SSM 可以学习解决任意问题长度的任务，实现 strong length generalization。
- **🔗 Link**: [Apple ML Research](https://machinelearning.apple.com/research/iclr-2026)

### (6) MANZANO: A Simple and Scalable Unified Multimodal Model with a Hybrid Vision Tokenizer
- **Affiliation**: Apple
- **核心创新**: 统一的多模态框架，使用混合视觉分词器减少理解与生成之间的性能权衡。在不同模型尺寸下都能工作。
- **🔗 Link**: [Apple ML Research](https://machinelearning.apple.com/research/iclr-2026)

### (7) MUX: Continuous Reasoning via Multiplexed Tokens
- **核心创新**: 将离散推理步骤压缩为连续向量的加权线性叠加（multiplexing），实现 **lossless 压缩**。证明简单的位置相关权重（几何衰减）支持无损多路复用，且复用推理可以并行探索搜索空间。在 16 个评估设置上与强 continuous reasoning 基线竞争或胜出。
- **Key Results**: 在 LLaMA 3.2 1B 上，MultiArith 提升 +22%，GSM-Hard 提升 +15.1%。

### (8) CALM: Continuous Autoregressive Language Models
- **核心创新**: 从离散 next-token prediction 到 **continuous next-vector prediction** 的范式转变。使用高保真自编码器将 K 个 token 压缩为单个连续向量，减少 K 倍生成步数。
- **Key Results**: 371M CALM-M 模型达到 281M Transformer-S 的 BrierLM 分数，但训练 FLOPs 减少 44%，推理 FLOPs 减少 34%。

### (9) AgentFlow: Flow-GRPO for Agentic Systems
- **Affiliation**: Lambda Labs / Academia
- **核心创新**: **Flow-GRPO**，训练模块化 agent 的高效方法，将轨迹优化分解为单步更新并传播奖励信号。7B 模型在搜索、数学、科学推理上 **beat GPT-4o**。
- **🔗 Link**: [Lambda Blog](https://lambda.ai/blog/iclr-2026-12-papers)

### (10) RAIN-Merging: Gradient-Free Method to Enhance Instruction Following in Large Reasoning Models
- **核心创新**: 无需梯度的模型合并方法，提升大推理模型的指令遵循能力，同时保留思考格式。

### (11) LongWriter-Zero: Mastering Ultra-Long Text Generation via RL
- **核心创新**: 使用强化学习实现超长文本生成，无需监督数据。

### (12) Mamba-3: Improved Sequence Modeling using State Space Principles
- **核心创新**: Mamba 系列第三代，进一步改进 SSM 架构。

### (13) Mixture-of-Experts Can Surpass Dense LLMs Under Strictly Equal Resource
- **核心创新**: 严格等资源条件下（相同 FLOPs/参数量），MoE 可以超越 dense LLM。

### (14) Universal Inverse Distillation for Matching Models with Real-Data Supervision (No GANs)
- **核心创新**: 无需 GAN 的通用逆蒸馏方法，用真实数据监督来匹配模型。

---

# 4. ICML 2026 — Key Papers

> 2026年7月6-11日，Seoul。23,918 审稿 → 6,352 接收（26.6%）。以下为重点 Highlight。

## 4.1 Oral Papers

### (1) Maximum Likelihood Reinforcement Learning (MaxRL)
- **Authors**: Fahim Tajwar et al.
- **核心创新**: 证明在二值正确性任务中，expected-reward RL 是最大似然目标的一阶近似，在低成功输入上学习信号消失。提出 **MaxRL**，基于 pass@k 展开的 compute-indexed 采样目标族，在计算量增加时在标准 RL 和精确最大似然之间插值。
- **Key Results**: 跨多个领域，MaxRL 始终优于标准 RL 和 GRPO，获得更高的 pass@1 和 pass@k。
- **🔗 Link**: [ICML Oral](https://icml.cc/virtual/2026/oral/71072)

### (2) Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis (Self-Flow)
- **Authors**: Hila Chefer, Patrick Esser, Dominik Lorenz, Dustin Podell, Antonio Torralba, Robin Rombach et al.
- **核心创新**: 自监督流匹配范式，在生成框架中整合表示学习。
- **🔗 Link**: [ICML 2026](https://www.paperdigest.org/2026/05/icml-2026-papers-highlights/)

### (3) You Can Learn Tokenization End-to-End with Reinforcement Learning
- **Authors**: Sam Dauncey, Roger Wattenhofer
- **核心创新**: 使用 score function estimates 学习 token 边界，相比 straight-through estimates 提供更紧的理论保证。直接从优化离散 token 边界来最小化损失。

### (4) Reinforcement Learning with Discrete Diffusion Policies for Combinatorial Action Spaces
- **Authors**: Haitong Ma, Ofir Nabati, Aviv Rosenberg, Bo Dai, Oran Lang, Craig Boutilier, Na Li, Shie Mannor, Lior Shani, Guy Tennenholtz
- **核心创新**: 训练离散扩散模型作为组合动作空间 RL 策略。使用 **policy mirror descent (PMD)** 定义理想正则化目标策略分布，将策略更新转化为分布匹配问题。FKL vs RKL 权衡分析。
- **Key Results**: 在 DNA 序列生成、macro-action RL、多智能体系统等组合 benchmark 上达到 SOTA 和更强的 sample efficiency。

## 4.2 Notable Papers

### (5) SWE-Perf: Can Language Models Optimize Code Performance on Real-World Repositories?
- 评估 LLM 优化真实仓库代码性能的能力。

### (6) AutoWebWorld: Synthesizing Infinite Verifiable Web Environments via Finite State Machines
- 使用 FSM 合成无限可验证的 Web 环境。

### (7) WorldCompass: Reinforcement Learning for Long-Horizon World Assistants in Mobile Scenarios
- 移动场景下长 horizon world assistant 的 RL 训练。

### (8) LithoDreamer: A Physics-Informed World Model for Multi-Stage Computational Lithography
- 物理信息世界模型用于计算光刻。

### (9) DLM: Unified Decision Language Models for Offline Multi-Agent Sequential Decision Making
- 统一决策语言模型用于离线多智能体序贯决策。

### (10) How Does the Lagrangian Guide Safe Reinforcement Learning through Diffusion Models?
- **Affiliation**: UCL
- 扩散模型指导安全 RL 的拉格朗日方法。

### (11) MMPD-Bench: Bridging Multimodal Fission with Multi-Polarimetric Modalities Decomposition
- **Affiliation**: UCL / Oxford

### (12) StepCodeReasoner: Aligning Code Reasoning with Stepwise Execution Traces via RL

### (13) Closing the Loop: Universal Repository Representation with RPG-Encoder

### (14) Towards Professional-Grade Financial Agents

### (15) PathwayLLM: Explainable Clinical Trajectory Modeling for Sepsis Prediction

---

# 5. AAAI 2026 — Outstanding Papers

> 2026年2月，Philadelphia。~23,000 审稿 → ~4,300 接收。

## 5.1 Outstanding Paper Awards

### (1) LLM2CLIP: Powerful Language Model Unlocks Richer Cross-Modality Representation
- **Authors**: Weiquan Huang, Aoqi Wu, Yifan Yang, Xufang Luo, Yuqing Yang, Liang Hu, Qi Dai, et al.
- **核心创新**: 使用强大的 LLM 作为文本编码器来提升 CLIP 风格的跨模态表示。

### (2) ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver
- **Authors**: Wenxuan Song et al.
- **核心创新**: 重建式视觉-语言-动作模型，作为机器人感知器。

### (3) Causal Structure Learning for Dynamical Systems with Theoretical Score Analysis
- **Authors**: Nicholas Tagliapietra et al.
- **核心创新**: 动力系统的因果结构学习 + 理论分数分析。

### (4) Model Change for Description Logic Concepts
- **Authors**: Ana Ozaki, Jandson S Ribeiro

### (5) High-Pass Matters: Theoretical Insights and Sheaflet-Based Design for Hypergraph Neural Networks
- **Authors**: Ming Li et al.

### (6) On the Alignment of Large Language Models with Global Human Opinion (Best Paper — AI Alignment Track)
- **Authors**: Yang Liu, Masahiro Kaneko, Chenhui Chu

## 5.2 Key Technical Papers

### (7) SPIRAL: Symbolic LLM Planning via Grounded and Reflective Search
- **Authors**: Yifan Zhang et al. (Vanderbilt / IBM Research)
- **核心创新**: 将三个专用 LLM agent（Planner、Simulator、Critic）嵌入 MCTS 循环。Planner 提出创意步骤，Simulator 预测实际结果，Critic 提供密集奖励信号。
- **Key Results**: DailyLifeAPIs 上 83.6% 准确率，比次优搜索框架提升 16+ 个百分点，同时 token 效率更优。
- **🔗 Link**: [AAAI Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/40975)

### (8) InTRO: In-Token Rationality Optimization
- **Authors**: Mingye Zhu et al. (USTC)
- **核心创新**: 实现 token 级探索和自我反馈。使用 correction factors（根据生成策略和答案条件化策略之间的信息差异估计的 token 级重要性权重），在单次前向传播中进行 token 级探索。
- **Key Results**: 6 个数学推理 benchmark 上，准确率比 base model 提升高达 20%。CoT 更简洁，并可跨领域迁移。
- **🔗 Link**: [AAAI Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/40826)

### (9) IndexTTS2: Breakthrough in Emotionally Expressive TTS
- **核心创新**: 自回归 TTS 中实现精确语音时长控制和情绪-音色解耦。三阶段训练范式 + GPT latent 表示 + Qwen3 软指令。
- **Key Results**: 在 WER、说话人相似度、情绪保真度上超越 SOTA zero-shot TTS。
- **🔗 Link**: [AAAI Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/40820)

### (10) Bonsai: Interpretable Tree-Adaptive Grounded Reasoning
- **Authors**: Kate Sanders, Benjamin Van Durme (JHU)
- **核心创新**: 组合概率推理系统，通过检索相关证据计算子 claim 的似然值，生成可适应推理树。支持文本、照片、视频、音频、数据库等多种模态。
- **Key Results**: 匹配领域特定黑盒方法的性能，同时生成可解释、基于证据、感知不确定性的推理轨迹。
- **🔗 Link**: [AAAI Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/40569)

### (11) SRPO: Safety-aware Reasoning Path Optimization for Multimodal LLMs
- **Authors**: Wei Cai et al. (Peking University / TeleAI, China Telecom)
- **核心创新**: 提出 **SSUI** 数据集（Safe-Semantics-but-Unsafe-Interpretation），包含可解释的推理路径。SRPO 框架对齐 MLLM 的内部推理过程与人类安全价值观。
- **Key Results**: 在安全 benchmark 上达到 SOTA，显著超越开源和商业 MLLM。
- **🔗 Link**: [AAAI Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/40840)

### (12) LENS: Learning to Segment Anything with Unified Reinforced Reasoning
- **核心创新**: 可扩展的 RL 框架，联合优化推理过程和分割。

---

# 6. CVPR 2026 — Best Papers & Highlights

> 2026年6月，Seattle。16,092 投稿 → 4,089 接收（25.4%）。

## 6.1 Best Paper Awards

### (1) D4RT: Efficiently Reconstructing Dynamic Scenes One D4RT at a Time
- **Authors**: Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, Liliane Momeni, Junyu Xie, Shuyang Sun, Rahul Sukthankar, Joëlle K. Barral, Raia Hadsell, Zoubin Ghahramani, Andrew Zisserman, Junlin Zhang, Mehdi S. M. Sajjadi
- **Affiliation**: Google DeepMind, UCL, Oxford
- **核心创新**: 统一的 Transformer 架构从视频中重建动态 4D 场景的几何和运动。同时估计深度、时空对应和完整相机参数。
- **Key Results**: 轻量级、高可扩展性，实现显著高效的训练和推理。
- **🔗 Link**: [CVPR 2026 News](https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers)

### (2) Native and Compact Structured Latents for 3D Generation
- **Authors**: J. Xiang, X. Chen, S. Xu, R. Wang, Z. Lv, Y. Deng, H. Zhu, Y. Dong, H. Zhao, N. Yuan, J. Yang
- **Affiliation**: Tsinghua University, Microsoft Research, USTC, Microsoft

## 6.2 Award Candidates & Notable Papers

### (3) NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang et al.
- **Affiliation**: NVIDIA, Stanford, Caltech, UChicago, UT Austin
- **核心创新**: Vision-action 基础模型，在 40,000 小时游戏视频（1000+ 游戏）上训练。统一视觉动作模型 + 大规模行为克隆。
- **Key Results**: 在 3D 动作游戏、2D 平台游戏、程序生成探索等领域 strong competence。相对成功率提升 20%+。
- **🔗 Link**: [CVPR 2026](https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers)

### (4) SAM 3D: 3Dfy Anything in Images
- **Authors**: Xingyu Chen et al.
- **Affiliation**: Meta Superintelligence Labs
- **核心创新**: 从单张图像预测几何、纹理和布局的生成式 3D 重建模型。
- **Key Results**: 人类偏好测试中 5:1 胜率。
- **🔗 Link**: [CVPR 2026](https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers)

### (5) Scaling Spatial Intelligence with Multimodal Foundation Models (SenseNova-SI)
- **Authors**: Zhongang Cai et al. (SenseTime / Shanghai AI Lab)
- **核心创新**: 系统构建 **SenseNova-SI-8M**（800万多样本），在严谨的空间能力分类体系下。基于 Qwen3-VL 和 InternVL3。
- **Key Results**: VSI-Bench 68.8%, MMSI 43.3%, MindCube 85.7%, MMBench-En 84.9%。同时分析了数据缩放、过拟合风险、空间 CoT 推理等。
- **🔗 Link**: [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Cai_Scaling_Spatial_Intelligence_with_Multimodal_Foundation_Models_CVPR_2026_paper.html)

### (6) TUNA: Taming Unified Visual Representations for Native Unified Multimodal Models
- **Authors**: Zhiheng Liu et al.
- **核心创新**: 通过级联 VAE 编码器和表示编码器构建统一的连续视觉表示空间。统一图像/视频的理解与生成。
- **Key Results**: 在图像/视频理解、生成、编辑方面超越解耦表示方案和 Show-o2，达成 SOTA。
- **🔗 Link**: [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_TUNA_Taming_Unified_Visual_Representations_for_Native_Unified_Multimodal_Models_CVPR_2026_paper.pdf)

### (7) Chorus: Multi-Teacher Pretraining for 3D Gaussian Splatting Scene Encoder
- **核心创新**: 从 2D 基础模型中蒸馏互补信号到 3DGS 场景编码器，支持开放词汇语义分割、实例分割等。
- **Key Results**: 使用 39.9× 更少的训练场景即超越点云基线。

### (8) Molmo2: Open Multimodal VLM with Video Understanding
- **核心创新**: 开放权重/数据的 VLM，在视频理解任务上达到 SOTA，包括视频指向（32.9% vs Gemini 2.5 Pro 17%）。

### (9) mVLM: A Vision Language Model for mNPUs
- **核心创新**: 首个为微神经处理单元（mNPU）设计的轻量级 VLM。OverMod 编码器 + AttSSM 解码器。
- **Key Results**: COCO Karpathy test split CIDEr 117.8，首次在 mNPU 上实现毫秒级 VLM 推理。
- **🔗 Link**: [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_mVLM_A_Vision_Language_Model_for_mNPUs_CVPR_2026_paper.html)

---

# 7. KDD 2026 — CTR & Recommendation

> 2026年8月9-13日，Jeju Island。

## 7.1 CTR Prediction & Scaling

### (1) FAT: Rademacher CTR Scaling Law (From Scaling to Structured Expressivity)
- **核心创新**: 揭示标准 Transformer 与 CTR 数据之间 **fundamental structural misalignment**——Transformer 假设 token 间等距依赖，而 CTR 需要组合推理。提出 **Feature-Aware Transformer (FAT)** 和 **Basis-Compression (BC)** 机制，将模型容量与词汇量解耦。正式推导 CTR Scaling Law。
- **Key Results**: FAT 超越现有 SOTA CTR 模型。
- **🔗 arXiv**: [2511.12081](https://arxiv.org/html/2511.12081v2)

### (2) FCN: Fusing Exponential and Linear Cross Network for CTR
- **核心创新**: 提出指数交叉网络（ECN，捕获阶数随深度指数增长的高阶交互）和线性交叉网络（LCN，低阶交互）。Low-cost Aggregation 方法。
- **Key Results**: 参数减少 22%，推理延迟降低约 23%。
- **🔗 Link**: [arXiv](https://arxiv.org/pdf/2407.13349)

### (3) CTR-Sink: Attention Sink for Language Models in CTR
- **Authors**: Zixuan Li et al. (Ant Group)
- **核心创新**: 解决 LM 在 CTR 中的 **semantic fragmentation** 问题。在行为之间插入 [SINK] token，锚定注意力在行为边界。引入时间距离等推荐信号。
- **Key Results**: 在 MovieLens/Amazon 等数据集上 AUC 提升 0.2-0.5%。
- **🔗 arXiv**: [2508.03668](https://arxiv.org/pdf/2508.03668v3) | **🔗 GitHub**: [UGUESS-lzx/CTR-SINK](https://github.com/UGUESS-lzx/CTR-SINK)

### (4) HeMix: Query-Mixed Interest Extraction and Heterogeneous Interaction
- **核心创新**: Query-Mixed Interest Extraction + HeteroMixer block（统一 local/global 交互）。
- **Key Results**: AMAP 平台上线：+3.61% GMV, +2.78% PV_CTR, +2.12% UV_CVR。超越 DLRM 和 RankMixer。
- **🔗 arXiv**: [2602.09387](https://arxiv.org/pdf/2602.09387)

### (5) GenCI: Generative CTR via Cohort-based Intent Learning
- **核心创新**: 生成式用户意图框架，使用语义兴趣 cohort 建模动态用户偏好。NTP 预训练 + 分层量化 + cross-attention 注入上下文信号。
- **Key Results**: 三个数据集上有效。
- **🔗 arXiv**: [2601.18251](https://arxiv.org/html/2601.18251v1)

### (6) BEYOND INTERLEAVING: Causal Attention Reformulations for Generative Recommender Systems
- **核心创新**: 提出 AttnLFA（因果掩码注意力晚融合）和 AttnMVP（混合值早融合），从信息论角度减少注意力噪声。
- **Key Results**: 在因果有效和对齐的交互上约束聚合，提升表示效率。

### (7) DS-MLP: Dual-Stream MLP is All You Need for CTR
- **Authors**: Kesha Ou et al. (Renmin University)
- **核心创新**: 知识蒸馏框架，将显式高阶特征交互从 teacher（如 DCNv2, FCN）蒸馏到 dual-stream MLP。
- **Key Results**: 三项 CTR benchmark SOTA，平衡精度与效率。
- **🔗 arXiv**: [2606.04944](https://arxiv.org/pdf/2606.04944v1) | **🔗 GitHub**: [RUCAIBox/DS-MLP](https://github.com/RUCAIBox/DS-MLP)

### (8) LLM-as-a-Judge for Reliable and Explainable Offline Evaluation in Top-K Recommendation
- **核心创新**: 使用 LLM 作为偏好语义代理，超越 MNAR 反馈，提供可解释的离线评估。

---

# 8. ACL 2026 — Highlights

## 8.1 Best Papers & Notable Papers

### (1) PaCoRe: Learning to Scale Test-Time Compute with Parallel Coordinated Reasoning
- **核心创新**: 通过消息传递架构驱动大规模并行探索。多轮并行推理轨迹 → 压缩为上下文边界消息 → 合成指导下一轮。
- **Key Results**: 8B 模型在 HMMT 2025 上达到 94.5%，**超越 GPT-5 的 93.2%**，有效 TTC 扩展至约 200 万 token。
- **🔗 PDF**: [ACL 2026](https://aclanthology.org/2026.acl-long.1253.pdf)

### (2) AFT: The Best of Both Worlds — Combining Parallel and Sequential Inference Scaling
- **核心创新**: Aggregation Fine-Tuning（AFT），结合顺序细化和并行采样的 propose-and-aggregate 框架。
- **Key Results**: Llama3.1-8B-Base AFT-on-policy 达到 LC win rate 41.3%，超越 Llama3.1-405B Instruct 和 GPT-4。
- **🔗 PDF**: [ACL 2026](https://aclanthology.org/2026.findings-acl.1568.pdf)

### (3) Deliberative Searcher: Improving LLM Reliability via RL with Constraints
- **核心创新**: 使用约束 RL 优化检索增强 LLM 的置信度校准。GRPO + 自适应 Lagrange 乘子。
- **Key Results**: 7B 模型将 false-certain rate 从 54% 降至 2%（降低 96%），计算成本减少 4×。
- **🔗 PDF**: [ACL 2026](https://aclanthology.org/2026.acl-long.199.pdf)

### (4) Adaptive Constraint Propagation: Meta-Reinforcement Learning for Structured Inference
- **核心创新**: **MetaJuLS**，使用元 RL 学习自适应约束传播策略，加速 LLM 结构化推理。
- **Key Results**: 1.5-2.0× 加速，精度损失仅 0.2%。学习到的调度策略在约束编程中发现非平凡启发式（如嵌套子句的 middle-out 策略）。
- **🔗 PDF**: [ACL 2026](https://aclanthology.org/2026.acl-long.701.pdf)

### (5) Beyond Token Length: Step Pruner for Efficient Reasoning
- **核心创新**: Step Pruner (SP) RL 框架，偏好紧凑推理步，减少 overthinking。动态停止机制防止 hacking。
- **Key Results**: AIME24 上 token 使用减少 69.7%。
- **🔗 PDF**: [ACL 2026](https://aclanthology.org/2026.findings-acl.94.pdf)

### (6) COMPASS: Enhancing Agent Long-Horizon Reasoning with Evolving Context
- **Affiliation**: Google Cloud AI / University of Virginia
- **核心创新**: 三层分层架构：Main Agent（执行）、Meta-Thinker（监控+策略干预）、Context Manager（维护简洁进度简报）。
- **Key Results**: GAIA、BrowseComp、HLE 上准确率提升最高 20%。
- **🔗 PDF**: [ACL 2026](https://aclanthology.org/2026.acl-long.152.pdf)

### (7) ONEREC-THINK: In-Text Reasoning for Generative Recommendation
- **Affiliation**: Kuaishou
- **核心创新**: OneRec-Think 统一对话、推理和个性化推荐。Itemic Alignment + Reasoning Scaffolding + 推荐特定奖励函数（多有效性）。
- **Key Results**: Kuaishou 线上 A/B 测试 APP 停留时间提升 0.159%（工业推荐中 0.1% 即被认为显著）。
- **🔗 PDF**: [ACL 2026](https://aclanthology.org/2026.acl-long.123.pdf)

### (8) DeepPlanner: Scaling Planning Capability for Deep Research Agents
- **核心创新**: 首次系统分析规划如何影响基于 RL 的深度研究 Agent。token 级熵分析揭示规划阶段的高熵瓶颈。引入 **advantage shaping** 集中学习规划决策。
- **🔗 PDF**: [ACL 2026](https://aclanthology.org/2026.findings-acl.370.pdf)

---

# 9. EMNLP 2025 — Highlights

### (1) From Implicit Exploration to Structured Reasoning
- **核心创新**: 从成功轨迹中提取结构化推理模式，从失败中提取反思信号。推理时 step-by-step guideline + refinement。
- **Key Results**: BBH, GSM8K, MATH-500, MBPP, HumanEval 上持续超越 CoT、ReAct、ToT 等基线。

### (2) Teaching Language Models To Gather Information Proactively
- **核心创新**: 主动信息收集范式——LLM 识别上下文缺口，通过目标性问题引导隐式用户知识。
- **Key Results**: Qwen-2.5-7B 在自动评估上超越 o3-mini 18%，人类评估中 clarification 问题偏好 42%，最终输出偏好 28%。

### (3) Enabling LLM Knowledge Analysis via Extensive Materialization (GPTKB)
- **核心创新**: 通过递归查询和结果整合，从 GPT-4o-mini 提取了 **1.01 亿关系三元组**，涵盖 290 万实体。
- **Key Results**: 构建 GPTKB（3.8 GB download），提供在线浏览和 SPARQL 查询接口。
- **🔗 Link**: https://gptkb.org

---

# 10. WWW 2026 — Recommendation & LLM

> 2026年4月13-17日，Dubai。

### (1) ThinkRec: Thinking-based Recommendation via LLM
- **核心创新**: System 1 → System 2 转变。思考激活机制（合成推理轨迹注入）+ instance-wise expert fusion。
- **Key Results**: 显著超越 baselines，提供更深的用户意图理解。
- **🔗 GitHub**: [Yu-Qi-hang/ThinkRec](https://github.com/Yu-Qi-hang/ThinkRec)

### (2) RE2: From Prediction to Understanding — Leveraging Reasoning in LLM-based Recommendations
- **核心创新**: 三步法：Reasoning Collection → Pattern Imitation (SFT) → Pattern Internalization (RL)。LLM 在推荐前显式生成推理内容。
- **Key Results**: 提升推荐性能 + 生成高质量推理内容，同时缓解 popularity bias。
- **🔗 GitHub**: [zhiyuanc2001/RE2](https://github.com/zhiyuanc2001/RE2)

### (3) AgentDR: Dynamic Recommendation with Implicit Item-Item Relations via LLM-based Agents
- **核心创新**: LLM agent 框架，利用常识推理捕获替代品和互补品关系。全排序任务委托给传统模型，LLM 整合多工具输出。
- **Key Results**: 平均 2 倍提升 over underlying tools。提出新的 LLM-based 评估指标。

### (4) IAM: From Token to Item — Item-aware Attention for LLM-based Recommendation
- **核心创新**: 揭示 LLM-based 推荐方法的一个关键限制——主要关注 token-token 关系而忽略 item-level 协同信息。引入 item-aware attention 机制，区分 item 内和 item 间 token 关系。
- **Key Results**: Prec@10 提升 25.81%（Grocery），71.00%（Cellphones）。

### (5) ISRF: Iterative Semantic Reasoning from Individual to Group Interests
- **核心创新**: 三步推理：多步双向属性推理 → 语义用户特征 + 基于相似度的用户图 → 迭代批次优化。
- **Key Results**: Sports、Beauty、Toys 数据集上超越 SOTA。

### (6) SPiKE: Enriching Semantic Profiles into Knowledge Graph for Recommendation Using LLMs
- **核心创新**: LLM 从知识库中提取用户/物品语义画像，通过 KG 传播偏好信号。

### (7) Guiding Generative Recommender Systems with Structured Human Priors via Multi-head Decoding
- **核心创新**: 多 head 解码架构，将人类先验知识注入生成式推荐系统。Adapter head 仅占 HSTU 参数的 0.14%。

### (8) Large Language Models-Enhanced Semantic Diffusion for User-Centric Recommendation (SEDIRec)
- **核心创新**: LLM 构建用户侧知识 + knowledge-aware graph diffusion model + semantic transitions 生成对比视图。
- **Key Results**: Book-Crossing 数据集上 Recall@50 提升 9.78%，NDCG@50 提升 15.64%。

---

# 11. SIGIR 2025 & RecSys 2025

## SIGIR 2025

### (1) CoT-Rec: Improving LLM-powered Recommendations with Personalized Information
- **核心创新**: 将两个 CoT 过程（用户偏好分析 + 物品感知分析）集成到 LLM 推荐流水线。
- **Key Results**: 在 retrieval 和 ranking 阶段均有效，降低位置偏差。

### (2) Toward Holistic Evaluation of Recommender Systems Powered by Generative Models (Gen-RecSys)
- **Authors**: Yashar Deldjoo, Nikhil Mehta (Google DeepMind), Maheswaran Sathiamoorthy, Shuai Zhang et al.
- **核心创新**: 分类 Gen-RecSys 评估挑战为两类：(i) 被生成输出加剧的现有问题（偏差、隐私），(ii) 全新风险（物品幻觉、矛盾解释）。提出 holistic evaluation approach。

### (3) ETEGRec: Generative Recommender with End-to-End Learnable Item Tokenization

### (4) ReARTeR: Retrieval-Augmented Reasoning with Trustworthy Process Rewarding

### (5) DisenCRS: Beyond Whole Dialogue Modeling for Conversational Recommendation

## RecSys 2025

### (1) You Don't Bring Me Flowers: Mitigating Unwanted Recommendations Through Conformal Risk Control (Best Full Paper)
- **Authors**: Giovanni De Toni et al.

### (2) Beyond Top-1: Addressing Inconsistencies in Evaluating Counterfactual Explanations for Recommender Systems (Best Short Paper)

---

# 12. CIKM 2025 — Highlights

> 2025年10月。443 full papers (27%), 185 short (31%)。

### (1) Climber: Toward Efficient Scaling Laws for Large Recommendation Models (Best Applied Research Paper)
- **Authors**: Songpei Xu et al.
- **核心创新**: 统一高效架构 + 协同设计加速。多尺度序列提取降低时间复杂度常数因子。

### (2) Generative Recommendation with Semantic IDs: A Practitioner's Handbook (Best Resource Paper)
- **Authors**: Clark Mingxuan Ju et al. (Snap)
- **核心创新**: SID 生成式推荐的实践指南，系统对比不同语义 ID 方法和生成策略。

### (3) STARec: An Efficient Agent Framework for Recommender Systems via Autonomous Deliberate Reasoning
- **Authors**: Chenghao Wu et al. (Renmin University / Huawei)

### (4) DAC4Rec: Diffusion-enhanced Actor-Critic for RL-based Recommendation
- **核心创新**: 扩散模型 + Q-value 引导策略优化，6 个离线数据集 + 在线模拟环境中验证。

### (5) MDT4Rec: Maximum In-Support Return Modeling for Dynamic Recommendation with LM Prior
- **核心创新**: 基于 Decision Transformer，使用 LLM 初始化 + LoRA 微调，处理次优反馈和稀疏用户数据。

### (6) Local LLMs for Recommendation
- **核心创新**: 基于 CF embedding 构建局部社区，每社区训练独立 LLM 推荐器。模型无关框架。

### (7) EvalAgent: Towards Evaluating News Recommender Systems with LLM-based Agents
- **Authors**: Guangping Zhang et al. (Fudan / Microsoft Research)

### (8) M-LLM3REC: A Motivation-Aware User-Item Interaction Framework

---

# 13. 重点实验室论文汇总

## 13.1 Google DeepMind

| 论文 | 会议/期刊 | 核心方向 |
|------|----------|---------|
| D4RT | CVPR 2026 Best | 动态 4D 场景重建 |
| A Subgoal-driven Framework for Improving Long-Horizon LLM Agents | arXiv | Agent 规划 + MiRA RL |
| COMPASS | ACL 2026 | Agent 长 horizon 推理 |
| MaxRL | ICML 2026 Oral | 最大似然强化学习 |
| Gated Attention | NeurIPS 2025 Best | LLM 高效注意力 |

## 13.2 Apple

| 论文 | 会议 | 核心方向 |
|------|------|---------|
| ParaRNN | ICLR 2026 Oral | 并行 RNN 训练，665× 加速 |
| To Infinity and Beyond | ICLR 2026 Oral | SSM + Tool-use 长度泛化 |
| MANZANO | ICLR 2026 | 统一多模态模型 |

## 13.3 Meta AI

| 论文 | 会议 | 核心方向 |
|------|------|---------|
| SAM 3D | CVPR 2026 | 单图 3D 生成 |
| NitroGen (w/ NVIDIA) | CVPR 2026 | 游戏通用 Agent 基础模型 |
| LLM2CLIP | AAAI 2026 Outstanding | 跨模态表示 |

## 13.4 NVIDIA

| 论文 | 会议 | 核心方向 |
|------|------|---------|
| NitroGen | CVPR 2026 | 游戏通用 Agent |
| ProRL | NeurIPS 2025 | RL 扩展推理边界 |
| DiLaDiff | arXiv | 扩散语言模型蒸馏 |

## 13.5 ByteDance

| 论文 | 会议 | 核心方向 |
|------|------|---------|
| TokenMixer-Large | KDD 2026 | 7B/15B CTR 模型，1.66% 订单增长 |
| UG-Sep | arXiv | TokenMixer 推理加速 20% |
| Precise SDE Sampling | arXiv | Flow-Matching RL 一致性采样 |

## 13.6 Alibaba

| 论文 | 会议 | 核心方向 |
|------|------|---------|
| FAT (Rademacher CTR Scaling Law) | KDD 2026 | CTR Scaling Law |
| HeMix | KDD 2026 | +3.61% GMV |
| ENCODE | TKDE 2025 | 长周期兴趣聚类 |
| MUSE | arXiv | 100K 长度终身兴趣 |

## 13.7 Kuaishou

| 论文 | 会议 | 核心方向 |
|------|------|---------|
| OneRec-Think | ACL 2026 | 生成式推理推荐 +0.159% Stay Time |
| OneMall | arXiv | 生成式电商推荐，+14.7% GMV |
| SARM | arXiv | 直播 ranking 语义锚点 |
| UniMixer | arXiv | 统一 CTR 缩放架构，+15% CAD |
| MaRI | arXiv | 推理加速 1.3× 无损 |
| DualGR | arXiv | 生成式检索，+0.527% 视频观看 |

## 13.8 Tencent

| 论文 | 会议 | 核心方向 |
|------|------|---------|
| GE4Rec | arXiv | 生成式 CTR 范式 |
| RankUp | KDD 2026 | 广告排序高秩表示 |
| TokenFormer | arXiv | 统一多域和序列 CTR |

---

# 14. 关键趋势总结

## 14.1 RL + LLM 推理
- RLVR 成为 LLM 推理能力提升的核心范式，但 NeurIPS 2025 质疑其是否能真正扩展推理边界（对比 ProRL 发现可以）
- GRPO 变体（Flow-GRPO, Step Pruner, SPIRAL）广泛应用于 agent 优化
- Test-time compute scaling 成为主流：PaCoRe (200万 token TTC) > GPT-5

## 14.2 扩散语言模型
- LLaDA 8B 挑战自回归统治地位，ICLR 2026 多篇扩散 LM 论文
- CALM（连续自回归语言模型）提供 new scaling axis

## 14.3 工业推荐系统
- **Scaling Laws for CTR** 成为热门方向（FAT, TokenMixer-Large, UniMixer）
- **生成式推荐**从 HSTU 演进到 OneMall/OneRec-Think，加入推理能力
- **LLM for Recommendation** 从简单 prompt 进化到完整 CoT + RL 训练范式
- 中厂（Kuaishou, ByteDance, Alibaba）贡献大量生产级系统论文

## 14.4 Agent Systems
- Agent 长 horizon 推理（COMPASS, DeepPlanner, DeepAgent, MiRA）
- Agent-as-Judge / Agent-as-Evaluator（EvalAgent, LLM-as-a-Judge）
- 从单一 agent 到多 agent coordination（AgentFlow, Foundation Protocol）

## 14.5 计算机视觉
- 4D 场景重建（D4RT）
- 通用游戏 Agent（NitroGen）
- 统一理解与生成（TUNA, MANZANO）

---

*Generated on 2026-06-26. 100+ papers curated from 12+ conferences/venues and 12+ industry labs.*
