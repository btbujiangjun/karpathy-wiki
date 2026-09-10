---
title: 全球大模型技术报告速览（2025-2026）
title-zh: 全球大模型技术报告速览
type: synthesis
created: 2026-09-10
updated: 2026-09-10
sources: []
tags: [tech-report, LLM, technical-report, system-card, arXiv]
---

# 全球 AI 大模型技术报告速览

> 汇总各主要 AI 公司/组织最新发布的模型技术报告（Tech Report / Technical Report / System Card），覆盖架构、训练方法、Scaling Law、多模态、长上下文与推理模型等关键维度。数据基于公开报告，截至 2026-09-10。

---

## 总结速览（Top 5 关注点）

1. **MoE + 混合架构成为主流**：几乎所有头部模型（DeepSeek-V3, Qwen3-235B, Llama 4, Gemini 2.5, Kimi K2, NVIDIA Nemotron 3, Step 3）均采用 MoE；NVIDIA 与 StepFun 进一步引入 **Mamba-Transformer 混合架构**（Nemotron 3）与 **Hybrid SWA 架构**（Step 3.5 Flash），Samba 等线性注意力路线开始进入前沿模型。
2. **推理模型（Reasoning/Thinking）全面铺开**：OpenAI o3/o4 与 GPT-5 思考模型、DeepSeek-R1/V4、Gemini 2.5 Thinking、Grok 3 (Think)、Qwen3 Thinking 模式、Phi-4-reasoning、Kimi K2 均主打"在推理上做 RL"，test-time compute（思考预算）成为新 Scaling 维度。
3. **长上下文竞赛白热化**：Llama 4 Scout 做到 10M 上下文（iRoPE），Gemini 2.5 Pro 覆盖 1M，Grok 3、Claude Opus 5、NVIDIA Nemotron 3 均支持 1M，Qwen3-2507 系列支持 1M。
4. **合成数据与 token 效率成为训练核心**：DeepSeek 强调 14.8T token 只在 2.788M H800 GPU hours 完成；Phi-4 以合成数据为主训练；Kimi K2 提出 MuonClip 优化器宣称零 loss spike；Qwen3 与 Ministral 3 用知识蒸馏大幅降低小模型训练成本。
5. **Scaling Law 从"参数/数据翻倍"转向"通胀优化"**：2026 年各论文普遍报告 MoE 增大 expert 数与稀疏度带来"继续稀疏仍有效"的结论；混合 Mamba 架构在推理吞吐/准确率帕累托前端上占据主导（NVIDIA Nemotron 3 报告最多 5.9×/7.5× 吞吐提升）。

---

## 1. DeepSeek（深度求索）

### DeepSeek-V3 Technical Report
- **中文标题**：DeepSeek-V3 技术报告
- **模型系列**：DeepSeek V3（Base + Instruct）
- **发布日期**：2024-12-27（arXiv）
- **核心参数**：
  - 总参数 671B，激活 37B/token（MoE）
  - 预训练 14.8T tokens；两阶段上下文扩展至 128K
  - 训练总成本仅 **2.788M H800 GPU hours**；若按 $2/GPU-hour 计约 $5.576M
  - FP8 训练，DualPipe 流水线并行（无显存瓶颈的流水线并行）
- **主要创新点**：
  1. **MLA（Multi-head Latent Attention）**：隐性低秩压缩 KV，大幅降低推理成本；
  2. **DeepSeekMoE**：细粒度 expert + shared expert。
  3. **Auxiliary-loss-free 负载均衡**（辅助损失无关负载平衡）。
  4. **Multi-Token Prediction (MTP)**：多 token 预测目标，同时可做投机采样。
  5. 全程无不可恢复 loss spike，训练稳定。
- **重点数据/结论**：MMLU 88.5、MMLU-Pro 75.9、GPQA 59.1，与 GPT-4o、Claude-3.5-Sonnet 相当；开源模型中最强的基座与 chat 版本（截至发布时）。
- **链接**：https://arxiv.org/abs/2412.19437

### DeepSeek-R1：Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
- **中文标题**：DeepSeek-R1：通过强化学习激发 LLM 推理能力
- **模型系列**：DeepSeek R1 / R1-Zero（基于 V3-Base，671B/37B）
- **发布日期**：2025-01（arXiv: 2501.12948）
- **核心参数**：MoE 671B 总参数，激活 37B；上下文 128K
- **主要创新点**：
  1. **纯 RL 推理训练（R1-Zero）**：绕过 SFT，直接用 GRPO 在 V3-Base 上做 RL，仅凭规则奖励就涌现自我验证、反思、策略动态调整等推理行为——首个大规模公开验证。
  2. **冷启动数据 + 多阶段流水线（R1）**：SFT 冷启动 + 推理 RL + rejection sampling SFT + 全面 RL，解决可读性/语言混合问题。
  3. **推理蒸馏**：将 R1 推理模式蒸馏到 1.5B-70B 的 Qwen/Llama 稠密模型，32B 蒸馏模型已超越 o1-mini。
- **重点数据**：AIME 2024 pass@1 从 15.6% → 71.0%（R1-Zero），majority voting 86.7%；与 OpenAI o1-1217 相当。已发表于 Nature 645:633-638（2025-09-17）。
- **链接**：https://arxiv.org/abs/2501.12948

### DeepSeek V4 系列（路线图/未发布技术报告）
- **状态**：据 2026 年公开报道（Dataconomy 2026-01、Reuters/The Information 2025-06、AI Learning Guides 2026-07 等），V4 系列（V4-Pro / V4-Flash）于 2026-04-24 发布；R2 多次延期，CEO 梁文锋对性能不满，曾尝试华为昇腾后回退 Nvidia 训练（这些为二手报道，缺少官方技术报告 = single-source，需谨慎标注）。
- **相关方法论论文**（2025-12~2026-01，官方发布）：
  - "Manifold-Constrained Hyper-Connections"（mHC，梁文锋共同作者）——用于大规模训练稳定性与成本控制。
  - "Engram"（条件记忆技术）——缓解高带宽显存（HBM）瓶颈。
- ⚠️ 以上 V4/R2 信息多数来自二手新闻源，未核对官方 technical report。置信度：**低（single-source）**。

---

## 2. OpenAI

### OpenAI o3 and o4-mini System Card
- **中文标题**：OpenAI o3 与 o4-mini 系统卡
- **模型系列**：o3（旗舰推理模型）、o4-mini（低成本推理）、o3-pro
- **发布日期**：2025-04-16
- **核心参数**：未公开参数量（高速推理模型 + 思考模型路线）；o3-pro 于 2025-06-10 发布
- **主要创新点**：
  1. **工具增强推理链（agentic CoT）**：o3/o4-mini 在思考过程中自主动用工具——web 搜索、Python、图像分析/剪裁、图像生成、canvas 等。
  2. **为工具使用训练做大规模 RL + deliberative alignment（审慎对齐）/Refusal 训练**。
  3. o4-mini 在 AIME 2024/2025 为最强 benchmark 模型；配合 Python 工具时 AIME 2025 达 99.5% pass@1。
  4. 首个在 **Preparedness Framework v2** 下发布的系统卡；评测覆盖生物/化学、网络安全、AI 自我改进，均低于 High 阈值。
- **链接**：https://openai.com/index/o3-o4-mini-system-card/

### GPT-5 System Card
- **中文标题**：GPT-5 系统卡
- **模型系列**：GPT-5 系统（gpt-5-main / gpt-5-thinking / mini / nano / pro）
- **发布日期**：2025-08-07（首次系统卡发布）
- **核心参数**：参数量未公开。系统 = 快速模型 + 深度推理模型 + 实时 router。
- **主要创新点**：
  1. **统一系统 + 实时路由**：按对话类型/复杂度/tool 需求自动分派到 main 或 thinking 模型，且路由随真实信号持续训练。
  2. **Safe-Completions**（安全完成）：从"硬拒绝/二元判断"转向"以输出安全性为中心"，提高双用途场景（生物/网络）的安全性同时保持助益性。
  3. **大幅降低幻觉与谄媚**：gpt-5-thinking 相比 o3 的主要事实错误次数减少 78%；股票式 sycophancy 显著下降。
  4. 健康领域最强（HealthBench Hard 46.2%）；Preparedness 框架按生物/化学 High 能力预防性管理。
- **链接**：https://openai.com/index/gpt-5-system-card/ ；arXiv 镜像 https://arxiv.org/abs/2601.03267

---

## 3. Anthropic

### System Card: Claude Opus 4 & Claude Sonnet 4
- **中文标题**：Claude Opus 4 与 Claude Sonnet 4 系统卡
- **模型系列**：Opus 4 / Sonnet 4（hybrid reasoning 模型）
- **发布日期**：2025-05（System Card May 2025；介绍文 2025-05-22）
- **核心参数**：未公开参数量；上下文 1M（Alpaca API 报 1M context）
- **主要创新点**：
  1. **混合推理（hybrid）**：快速响应与 extended thinking（64K thought token）二合一。
  2. 编码最强：SWE-bench Verified Opus 4 72.5%、Sonnet 4 72.7%（甚至 79.4/80.2% 带 rejection sampling 重评分）；Terminal-bench 43.2%。
  3. 首个包含 **alignment assessment** 与 **model welfare assessment** 的系统卡；Release 决策 Opus 4 = ASL-3、Sonnet 4 = ASL-2。
- **链接**：https://www.anthropic.com/news/claude-4

### System Card: Claude Opus 5
- **中文标题**：Claude Opus 5 系统卡
- **模型系列**：Opus 5（thoughtful, proactive, 贴近 frontier）
- **发布日期**：2026-07-24
- **核心参数**：上下文 1M；最大输出 128K；知识截断 2026-05；输入 $5/MTok、输出 $25/MTok
- **主要创新点**：
  1. **adaptive thinking（自适应思考）默认启用**，由 effort 参数控制。
  2. 代理编码/计算机使用/长时程知识工作的最大提升；Frontier-Bench v0.1、GDPval-AA 新 SOTA；ARC-AGI 3 较次优模型高 3 倍。
  3. 对齐度为其历史最佳（misaligned behavior 评分 2.3，所有模型中最低），符合宪法高于 Opus 4.8/Sonnet 5/Fable 5。
  4. 网络安全能力接近 Mythos 5（漏洞发现），但漏洞利用明显落后；生物研究按保守 ASL-3 保护。
- **链接**：https://www.anthropic.com/research/claude-opus-5

---

## 4. Meta AI（LLaMA）

### The Llama 4 Herd（MODEL_CARD + Announcement）
- **中文标题**：Llama 4 模型家族（Scout/Maverick/Behemoth）
- **模型系列**：Llama 4 Scout（17B×16E）、Llama 4 Maverick（17B×128E）、Llama 4 Behemoth（teacher，未发布）
- **发布日期**：2025-04-05
- **核心参数**：
  | 模型 | 激活参数 | 总参数 | 上下文 | 训练 token |
  |---|---|---|---|---|
  | Scout | 17B | 109B | **10M** | ~40T |
  | Maverick | 17B | 400B | 1M | ~22T |
- **主要创新点**：
  1. Meta 首个原生多模态 + MoE 模型（early fusion 统一文本与视觉 token 进单一 backbone）。
  2. **iRoPE（interleaved attention，无位置编码层交错 + 推理期温度缩放）**实现长度泛化，Scout 上下文 10M。
  3. 训练用 FP8，Behemoth 训练达到 390 TFLOPs/GPU（32K GPU）；>30T token 多模态数据（文本/图/视频）。
  4. 混合 dense + shared expert + routed experts 交替层设计，降低推理成本。
- **重点数据**：Maverick 在编码/推理上竞争 DeepSeek V3，一张 H100 DGX host 即可跑；Scout 单个 H100（int4）可跑。
- **链接**：
  - Model Card: https://github.com/meta-llama/llama-models/blob/main/models/llama4/MODEL_CARD.md
  - Blog: https://ai.meta.com/blog/llama-4-multimodal-intelligence/

---

## 5. Google DeepMind

### Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities
- **中文标题**：Gemini 2.5：以高级推理、多模态、长上下文与下一代代理能力推动前沿
- **模型系列**：Gemini 2.X（2.5 Pro / 2.5 Flash / 2.0 Flash / 2.0 Flash-Lite / 2.5 Deep Think）
- **发布日期**：2025-06-16（技术报告 PDF）；arXiv 2025-07-07
- **核心参数**：MoE 稀疏 Transformer；原生多模态（文本/图像/音频）；上下文 1M+；视频处理达 3 小时
- **主要创新点**：
  1. **原生思考（Thinking）**：模型自行决定思考时长，并支持 **Thinking budget** 可控 tradeoff 推理质量/成本。
  2. **Deep Think**：并行假设生成 + 批判的推理方式，Olympiad/USAMO、LiveCodeBench、MMMU SOTA。
  3. 在**训练稳定性、信号传播与优化动力学**上取得重大进展——无 RL 纯预训练 checkpoint 相对 1.5 有显著性能提升。
  4. 2.5 Pro AIME 2025 = 88.0%、GPQA 88.4%（推理时放大）、LOFT/MRCR 长上下文 SOTA、唯一支持 1M+ 上下文。
  5. 系列横跨能力/成本 Pareto 前沿。
- **链接**：https://arxiv.org/abs/2507.06261；PDF https://storage.googleapis.com/deepmind-media/gemini/gemini_v2_5_report.pdf

---

## 6. Microsoft（Phi）

### Phi-4 Technical Report
- **中文标题**：Phi-4 技术报告
- **模型系列**：Phi-4（14B 稠密 + Phi-4-mini / Phi-4-multimodal 扩展，2025-06）
- **发布日期**：2024-12-12
- **核心参数**：14B 参数；上下文 4K 训练、16K midtraining；约 10T token（合成数据为主体）
- **主要创新点**：
  1. **以数据质量为中心的训练配方**：合成数据占预训练主体，方法包括 multi-agent prompting、self-revision workflows、instruction reversal。
  2. 蒸馏之外：核心基准（GPQA、MATH）**超过教师模型 GPT-4o**，证明合成数据/课程/后训练超越蒸馏上限。
  3. **Pivotal Token Search (PTS) DPO**：围绕"关键 token"生成偏好对，显著提升推理任务。
  4. 后训练 = SFT + 第一轮 PTS-DPO + 第二轮 judge-guided DPO。
  5. AMC 11 月新题表现优于同级别甚至大幅更大的模型（防过拟合证据）。
- **链接**：https://arxiv.org/abs/2412.08905

### Phi-4-reasoning Technical Report
- **中文标题**：Phi-4-reasoning 技术报告
- **模型系列**：Phi-4-reasoning / Phi-4-reasoning-plus
- **发布日期**：2025-04-30
- **核心参数**：14B；基于 Phi-4 后训练（o3-mini 教长 CoT）
- **主要创新点**：
  1. **可教学提示（teachable prompts）**数据选择 + o3-mini 推理示范生成。SFT 于 1.4M+ STEM/编码问题。
  2. **短时基于结果的 RL（outcome-based RL）**自演进，将响应长度平均延长 1.5× 提升准确率（reasoning-plus）。
  3. 14B 模型在多数任务上超过 DeepSeek-R1-Distill-Llama-70B 与 o1-mini，逼近完整 R1；推理作为"可迁移元技能"。
- **链接**：https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-technical-report/

---

## 7. Mistral AI

### Ministral 3（arXiv: 2601.08584）
- **中文标题**：Ministral 3 模型家族
- **模型系列**：Ministral 3（3B / 8B / 14B 各含 base、instruct、reasoning 三变体）
- **发布日期**：2026 年初（arXiv 2601.08584，预印本）
- **核心参数**：
  - 稠密模型；上下文 256K（reasoning 变体 128K）；131K 词表；GQA + RoPE + SwiGLU + RMSNorm
  - 训练仅 1-3T token（对比 Qwen3 36T / Llama3 15T）
- **主要创新点**：
  1. **Cascade Distillation（级联蒸馏）**：从 Mistral Small 3.1（24B 父模型）迭代剪枝 + 继续蒸馏，14B 以 <40% 体量接近父模型性能。
  2. 每变体均带视觉能力（410M ViT 冻结 + 新 projection）。
  3. reasoning 变体 `SFT → GRPO → ODPO` 三阶段训练。
- **已有 Pixtral 12B**（2024-10，arXiv:2410.07073）：12B 解码器 + 400M **RoPE-2D** ViT 视觉编码器，原生支持任意分辨率/宽高比，Apache 2.0。
- **链接**：https://arxiv.org/abs/2601.08584 ；Pixtral https://arxiv.org/abs/2410.07073

---

## 8. Qwen（阿里巴巴）

### Qwen3 Technical Report
- **中文标题**：Qwen3 技术报告
- **模型系列**：Qwen3（0.6B–235B；6 个稠密 + 2 个 MoE；现含 Qwen3-2507 更新）
- **发布日期**：2025-05-13/14（arXiv 2505.09388）
- **核心参数**：
  - 旗舰 **Qwen3-235B-A22B**：总参数 235B、激活 22B
  - 预训练 **36T tokens**，覆盖 **119 种语言/方言**（Qwen2.5 为 29 种）
  - 2507 更新支持 256K-1M 长上下文（qwen3-2507 系列）
- **主要创新点**：
  1. **Thinking / Non-thinking 双模式统一框架**：同一模型内切换，配合 **thinking budget** 动态控制推理 token 数。
  2. 性能对标 o1/o3-mini/DeepSeek-V3：AIME'24 = 85.7、AIME'25 = 81.5、LiveCodeBench v5 = 70.7、BFCL v3 = 70.8。
  3. 235B-A22B-Base 在 14/15 个基准上超过 DeepSeek-V3-Base（1/3 总参数量、2/3 激活量）。
  4. **强-弱蒸馏（Strong-Weak Distillation）**：将旗舰知识蒸馏到小模型，大幅降低小型模型训练成本。
  - 全部 Apache 2.0 开源。
- **链接**：https://arxiv.org/abs/2505.09388

---

## 9. xAI（Grok）

### Grok 3 Beta — The Age of Reasoning Agents
- **中文标题**：Grok 3 Beta —— 推理体时代（发布博客，未同步技术报告/系统卡）
- **模型系列**：Grok 3 / Grok 3 mini（Think 变体）
- **发布日期**：2025-02-19
- **核心参数**：上下文 **1M tokens**（较 Grok 2 大 8 倍）；参数量未官方确认（外部第三方推测从 1.2T 到 2.7T 不等，未经官方确认 = 低置信度）
- **主要创新点**：
  1. **大规模 RL 训练推理**：在 Colossus 超算上训练，官方称 10× 前代 SOTA compute；可自我回溯纠错、探索替代路径、验证自身方案。
  2. **测试时计算（Think 模式）**：高 compute 档位 AIME 2025 93.3%（cons@64）、GPQA 84.6%、LiveCodeBench 79.4%。
  3. **DeepSearch agent**：实时搜索 + 深度研究/综合报告。
  4. 非推理模式数据：LOFT(128k) 83.3% 长上下文 SOTA；MMMU 73.2%、EgoSchema 74.5%（视频理解）。
- ⚠️ 注意：第三方分析指官方未披露 cons@1 与完整评测方法学，声称的 @1 成绩可能有选择性上报（第三方批评，需交叉验证）。
- **链接**：https://x.ai/blog/grok-3

---

## 10. Apple / NVIDIA / Amazon / 其他

### Apple
- 截至本次速览，Apple 未针对其基础模型（如 Apple Intelligence / Siri 相关）发布标准化 open technical report 形式的参量明细报告。官方网站公开的模型描述（约 2024-2025）指出其端侧模型采用 **~3B 参数**级别、量化低于 4bit/万亿词汇当量、具备 8K 上下文与适配器（adapter）持久本地化优化（这部分来自 Apple 官方页面与媒体综述，非完整技术报告，置信度中等）。

### NVIDIA — Nemotron 3 家族
- **中文标题**：Nemotron 3 系列白皮书与各型号技术报告
- **发布时间**：白皮书 + Nano 2025-12-15；Super 2026-04-03；Ultra 2026-06-09
- **核心参数**：
  | 模型 | 总参数 | 激活参数 | 训练 token | 上下文 |
  |---|---|---|---|---|
  | Nano 3 | 30B | 3.2B | 25T | 1M |
  | Super 3 | 120B | 12B | 25T | 1M |
  | Ultra 3 | 550B | 55B | 20T | 1M |
- **主要创新点**：
  1. **MoE Hybrid Mamba-Transformer**：Mamba-2 线性状态 + 少量全局 self-attention"anchor"层交错，显著降低 KV cache 与推理延迟；Ultra 在 8K/64K 设置下是 GLM-5.1-754B 的 **5.9×**、Kimi-K2.6-1T 的 **4.8×** 推理吞吐。
  2. **NVFP4 低精度预训练**：权重/激活/梯度 4 比特预训练（E2M1），为迄今最大规模（20-25T token）稳定 NVFP4 训练。
  3. **LatentMoE**（Super/Ultra）：优化 accuracy-per-parameter 与 per-FLOP。
  4. **Multi-Token Prediction (MTP)** + 投机解码；**Multi-teacher On-Policy Distillation (MOPD)**（Ultra）与 **多环境 RLVR/RLHF**，具备**推理预算控制**。
- **链接**：
  - 白皮书：https://arxiv.org/abs/2512.20856
  - Ultra: https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf

### Amazon（Amazon Nova）
- **中文标题**：Amazon Nova 模型家族技术报告与模型卡
- **模型系列**：Nova Pro / Lite / Micro（理解）、Nova Canvas（图像）、Nova Reel（视频）、Nova Premier（2025-04-30 增补）
- **发布日期**：2024-12-03（原报告）→ 2025-03-17（arXiv 更新，含 Premier 增补）
- **核心参数**：Transformer 架构；多语言训练（重点 15 种语言，覆盖 200+ 语言数据）；Pro/Lite 多模态（文本/图像/文档/视频输入）
- **主要创新点**：
  1. 首推视频理解能力上超大规模（Bedrock）的模型。
  2. **价格性能比**为设计目标——Micro 在 MMLU/GPQA/MATH 等文本基准同档最强，Lite/Pro 在视频/DocVQA/BFCL/agentic 多模态基准同类领先。
  3. 后训练：SFT + RM + DPO/PPO 对齐。
- **链接**：https://arxiv.org/abs/2506.12103

### Moonshot AI（Kimi）
- **中文标题**：Kimi K2：开放代理式智能（Open Agentic Intelligence）
- **模型系列**：Kimi K2（Base + Instruct）
- **发布日期**：2025-07-28（arXiv 2507.20534）
- **核心参数**：
  - **MoE 1T 总参数 / 32B 激活**；上下文 **128K**
  - 预训练 **15.5T tokens**，零 loss spike
  - 术语：MLA + 384 experts（每 token 选 8）+ 1 shared expert
- **主要创新点**：
  1. **MuonClip 优化器**：在 token 高效的 Muon 优化器上引入 QK-Clip 解决训练不稳定——最大规模（1T 参数）Muon 应用。
  2. **Scaling Law 分析**：稀疏度持续提高仍带来显著性能提升 → 将 expert 数从 V3 的 256 扩至 384。
  3. **agentic 数据合成管线 + 联合 RL**（真实与合成环境交互），SWE-bench Verified 65.8%、τ²-Bench 66.1、ACEBench 76.5、SWE-bench Multilingual 47.3（非思考模式下超越多数开放/封闭基线，逼近 Claude 4）。
  4. LMSYS Arena 开源 No.1 / 总榜第 5（2025-07-17 统计）。
- **链接**：https://arxiv.org/abs/2507.20534

### StepFun（阶跃星辰）
- **Step 3（Step-3 is Large yet Affordable）**：MoE 总 321B/激活 38B；原生多模态推理。创新：**Multi-Matrix Factorization Attention (MFA)** + **Attention-FFN Disaggregation (AFD)** 模型-系统协同设计，面向低成本解码。arXiv 2507.19427（2025-07）。
- **Step 3.5 Flash（2026-02-12 更新）**：196B / 激活 11B；**MTP-3 三步 token 预测**，生成 100-350 tok/s；**3:1 Sliding Window Attention (SWA):Full Attention**（256K 上下文）；SWE-bench Verified 74.4%、Terminal-Bench 2.0 51.0%；可在 mac Studio/DGX Spark 本地运行。
- **Step 3.7 Flash（2026-05-29）**：196B+1.8B(ViT)/激活 11B；Agent 生态兼容（Claude Code/KiloCode/OpenClaw/Skills）；Advisor Mode（小执行者 + frontier 顾问，Opus 4.6 97% 编码性能、1/9 成本）；DeepSeekSearchQA 92.82% F1。
- **Step-DeepResearch（2025-12-24 arXiv 2512.20491）**：端到端深度研究 agent；32B 下 ResearchRubrics 61.4% 与 OpenAI/Gemini Deep Research 相当。
- 链接：https://github.com/stepfun-ai/Step3 ；https://github.com/stepfun-ai/StepDeepResearch

---

## 交叉主题分析

### 架构趋势：MoE 之外
| 主题 | 代表 | 关键点 |
|---|---|---|
| MoE sparse | V3/V4, Qwen3-235B, Llama4, K2, GLM | 稀疏度高，激活参数少，accuracy/FLOPS 帕累托优 |
| Hybrid Mamba-Transformer | NVIDIA Nemotron 3, Samba/Mamba2 | 线性注意力+全局 anchor，21×-5.9× 推理吞吐提升 |
| 混合注意力（SWA+FA） | Step 3.5 Flash | 3:1 SWA，256K 上下文低成本长文本 |
| 长上下文位置编码 | Llama4 iRoPE, Gemini 2.5, Nemotron3（无 RoPE） | 长度泛化 vs. 推理稳定性的权衡 |

### 训练方法趋势
- **SFT → RL → distillation** 成为标准三段式，但 2026 年各家差异性落到：
  - **信源 RL（RLHF/RLVR）环境多样化**（Nemotron 3 多环境同时 RL；K2 真实+合成环境联合 RL）
  - **合成数据管线**（Phi-4；OpenAI；Meta 的 >30T 多模态数据）
  - **低成本优化器/精度**（MuonClip；NVFP4；FP8）

### 推理模型：test-time Scaling 统一范式
- 思考预算（thinking budget）、effort 参数、cons@64、Deep Think、Think 模式、hybrid reasoning 均指向同一方向：**显式控制推理时 token/compute**，将推理成本作为可调旋钮。

### Scaling Law 的新讨论点
- K2 报告指出"sparsity 继续增大仍有效"；NVIDIA 主张 Mamba 架构改变 accuracy-throughput 前沿；Qwen3 论证 MoE 相比稠密的换算收益；DeepSeek 强调成本/硬件协同优化。

---

## 未检索到官方报告的机构（备注）

- **Yi (01.AI)**：截至 2026-09 未检索到新的官方技术报告（早期 Yi-34B/1.5 报告为 2024 年；未见 2025-2026 重大新发布）。
- **Baichuan**：漫川大模型（2025-01）为系列述职形式发布，完整技术报告公开度低。
- **Zhipu AI (GLM)**：市场上活跃（GLM-4.5/4.6，Ultra 报告中被比较的 GLM-5.1-754B-A40B 等），但本次速览未抓到一篇公开 arXiv 级技术报告；建议后续单独追踪。
- **InternLM**：上海 AI Lab 持续发布开源模型（InternLM3 等），本文档搜索被限流未取到最新技术报告，建议后续补充。

---

## 附注

- 本文档为综合网络检索产物，信息来自官方 arXiv/报告正文与可信第三方综述。
- 标注 `(single-source)` 或 `低置信度` 的条目（如 Grok 3 参数量、DeepSeek V4/R2 路线图）未经官方报告确认，请勿作为采购/技术决策依据。
- Gemma 3、GPT-OSS、GLM 等未纳入本次目标名单，但出现在对比表中时已如实引用。