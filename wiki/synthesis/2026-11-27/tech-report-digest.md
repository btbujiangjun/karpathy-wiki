---
title: LLM 技术报告速览 — 2026-11-27
type: synthesis
created: 2026-11-27
updated: 2026-11-27
sources: [www.deepseek.com/news/deepseek-v4-1-flash, huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/DeepSeek_V41_Tech_Report.pdf, arxiv.org/abs/2606.19348, api-docs.deepseek.com/zh-cn/quick_start/pricing, deploymentsafety.openai.com/gpt-6-2-chatgpt, deploymentsafety.openai.com/gpt-6-2-chatgpt/gpt-6-2-chatgpt.pdf, deploymentsafety.openai.com/gpt-6-2-astra-sol, deploymentsafety.openai.com/gpt-6-2-astra-sol/gpt-6-2-astra-sol.pdf, research.meta.ai/blog/muse-ember, research.meta.ai/static/muse-ember-evaluation-report, research.meta.ai/blog/muse-wonder, research.meta.ai/static/muse-wonder-model-card, research.meta.ai/blog/muse-spark-open, research.meta.ai/static/muse-spark-open-evaluation-methodology, huggingface.co/meta-models/Muse-Spark-Open-816B-A42B, huggingface.co/meta-llama, ai.meta.com/llama, storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Neon-Model-Card.pdf, storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Hydrogen-Model-Card.pdf, storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Carbon-Model-Card.pdf, storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Argon-Model-Card.pdf, blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon, deepmind.google/models/gemini, www.anthropic.com/claude-fable-and-mythos-5-2, www.anthropic.com/document/claude-fable-5-2-mythos-5-2-system-card, assets.claude.com/27d60918d218125e7504bc7354c4b4626ec56b11.pdf, mistral.ai/news/mistral-large-4, mistral.ai/news/mistral-large-4-oss, docs.mistral.ai/models/mistral-large-4-0, www.alphaxiv.org/abs/2611.mistral-large-4, huggingface.co/mistralai/Mistral-Large-4-1T-A52B, community.alibabacloud.com/blog/alibaba-unveils-qwen4-max-new-ai-teammate-for-work-creativity-and-discovery_603783, qwen.ai/research, www.01.ai, arxiv.org/abs/2403.04652, github.com/baichuan-inc, github.com/baichuan-inc/Baichuan-M3-235B, arxiv.org/abs/2602.06570, arxiv.org/abs/2509.02208, huggingface.co/microsoft/Phi-4-reasoning-vision-15B, aka.ms/Phi-4-reasoning-vision-15B-TR, huggingface.co/microsoft/FrogNano-4B-2609, machinelearning.apple.com/research/apple-foundation-models-tech-report-2025, arxiv.org/abs/2507.13575, apple.com/ai, machinelearning.apple.com/research/apple-intelligence-foundation-language-models, arxiv.org/abs/2611.22161, arxiv.org/abs/2611.20771, arxiv.org/abs/2610.02665, huggingface.co/nvidia, developer.nvidia.com/blog, x.ai/news/grok-4-7, aws.amazon.com/nova, aws.amazon.com/nova/models, docs.aws.amazon.com/nova/latest/nova2-userguide/getting-started-nova-2.html, docs.z.ai/guides/llm/glm-5.4, docs.z.ai/guides/llm/glm-5.3, github.com/zai-org/GLM-5, arxiv.org/abs/2602.15763, z.ai, github.com/InternLM, github.com/InternLM/Sage-S2.1-Flash, arxiv.org/abs/2611.21072, www.kimi.ai/blog/kimi-k3-1-pro, github.com/MoonshotAI/Kimi-K3, github.com/MoonshotAI/Kimi-K3/blob/main/k3_tech_report.pdf, github.com/stepfun-ai/Step-5-Preview, platform.stepfun.ai/blog/inside-step-5-preview, github.com/stepfun-ai/Step-3.7-Flash, seed.bytedance.com, arxiv.org/abs/2607.00248, arxiv.org/abs/2603.20633]
tags: [tech-report, LLM, technical-report, system-card, model-card, ArXiv, moe, mamba, hybrid-architecture, sparse-attention, reasoning, long-context, multimodal, scaling-law, alignment, rl, cybersecurity, open-weights, daily-digest]
---

# LLM 技术报告速览 — 2026-11-27

> 各公司最新一手 Tech Report / Technical Report / System Card / Model Card 索引。
> 核验时间：2026-11-27（今日，UTC 2026-11-27）。覆盖目标机构：DeepSeek、OpenAI、Meta AI (LLaMA)、Google DeepMind (Gemini)、Anthropic (Claude)、Mistral AI、Qwen (Alibaba)、Yi (01.AI)、Baichuan、Microsoft (Phi)、Apple、NVIDIA、xAI (Grok)、Amazon (Amazon Nova)、Zhipu AI (GLM/ChatGLM)、InternLM (Shanghai AI Lab)、Moonshot AI (Kimi)、StepFun (阶跃星辰)、ByteDance (豆包/Doubao)。
> 方法：本环境 `websearch` 不可用（返回 “Web search cancelled”），改用等价 HTTPS 抓取（webfetch / `curl`）各公司官网、官方 Newsroom/Research 页、系统卡/模型卡 PDF（用 pypdf 抽取核验）、GitHub 官方组织仓库与 README、arXiv Export API（`export.arxiv.org/api/query`，按 submittedDate 降序）逐项核验。**口径**：系统卡/模型卡/技术博客/模型页披露层级不一；部分参数与训练数据量为厂商自报或未公开，标注“未公开”；无法访问或未找到一手来源的条目如实标注，不臆造；指标均为厂商自报；链接已做 HEAD/GET 可达性检查（PDF 类无法在 webfetch 内渲染，但已用 curl+pypdf 下载解析或确认 HTTP 200）。按用户给定机构顺序排列。每篇结构：**中文标题 + 英文标题 / 发布机构 / 模型名称/系列 / 发布日期 / 核心参数（参数量、训练数据量、上下文长度等）/ 主要创新点（含重点关注：新架构 MoE-Mamba-Hybrid、训练方法 pre/post-training+alignment+RL、Scaling Law、多模态、长上下文、推理模型）/ arXiv-论文链接**。

## 重点关注方向速览（2026-11-27）

| 方向 | 代表进展（今日核验口径） |
|---|---|
| 新架构（MoE / Mamba / Hybrid / Sparse） | DeepSeek-V4.1-Flash（**Causal-Encoder-Decoder 非对称 MoE**，8B prefill/16B decode，**CSA2 + FP4 KV**，KV 890 B/token）；DeepSeek-V4（hybrid **CSA+HCA**，mHC，Muon）；**NVIDIA Nemotron 3.5 Super**（hybrid **MoE+Mamba**，120B/12B）；**Zhipu GLM-5.4**（**Loop Transformer** 复用 28 层×2，750B 基座，对标 2T–3T）；**Zhipu GLM-5.3-Flash**（hybrid **sparse+linear attention**，mHC）；**Qwen4-Max**（sparse MoE 升级 Gated DeltaNet + Qwen Sparse Attention + Gated Residual + N-gram，2.4T/71B）；**Kimi K3/K3.1**（**KDA + AttnRes + Stable LatentMoE 16/896**，2.8T/3T-class）；**Mistral Large 4**（hybrid instruct-and-reasoning MoE，1T/52B，DSA+YOCO+LeRoPE+SSMax+NVFP4）；**Meta Muse Spark Open**（816B/42B）；**Meta Muse Ember**；**Gemini 4 Argon**（large-scale sparse MoE）；**NVIDIA Nemotron-Labs-Sigma**（连续扩散 LM）；**StepFun Step 5**（Gated Sliding Window + sparse full attention + Sparse GQA，600B/27B，92 层）；**Apple** PT-MoE server model + ~3B on-device（KV-cache sharing + 2-bit QAT）。 |
| 训练方法（Pre/Post/Alignment/RL） | **NVIDIA Nemotron 3.5 Super**（**纯 RL、无 SFT**，CISPO rank-32 LoRA，5 个 expert-built 数据集）；**Kimi K3.1 Pro**（post-trained K3 + **大规模 joint RL across hundreds of domains**；为 open-weight **移除 cyber 相关数据**）；**Zhipu GLM-5.3**（同基座 GLM-5.2 + **纯 post-training**；**GLM-5.4 Loop** 继续训练适配）；**Mistral Large 4**（SFT + **RL at scale**，**multiple-teacher distillation** → Low/Medium/High；agent-native verified environments；**33B/day trainable RL tokens**）；**Google Gemini 4**（instruction tuning + **RL** + human preference；RL 多步推理/定理证明）；**OpenAI GPT-6.2**（**RL-trained reasoning**，长 internal CoT；Critical cyber + High bio；Astra **High AI Self-Improvement**；Control Room；抗 distillation）；**Anthropic Fable/Mythos 5.2**（pretraining + substantial post-training/fine-tuning；**Constitutional** alignment；RSP/FCF；dual-use safeguards；**Fable vs Mythos** 两档）；**DeepSeek-V4.1-Flash**（SFT + RL + **on-policy distillation**，改动在 data pipeline；45T multimodal pretraining）；**Meta Muse**（scaling ladder + **RL**；Muse Ember 由 Muse Wonder Full 训练；Active Memory/Active Focus；安全对齐 + prompt-injection 抵抗）；**Apple**（SFT + **async RL**；Private Cloud Compute；responsible AI）；**StepFun Step 5**（agent-native 数据合成 + RL for long rollouts）；**InternLM Sage**（**verifiable environments** 后训练）。 |
| Scaling Law / 缩放分析 | **GLM-5.4**（Loop Transformer 权重复用 → “effective compute” 上移，对标 2T–3T；**continued training adaptation** vs from-scratch）；**GLM-5**（355B/32B → **744B/40B**；pretraining **23T→28.5T**；DSA；**IndexShare 2.9× FLOPs @1M**）；**Qwen4-Max**（2.4T，**25% fewer activated** vs Qwen3.8-Max；token 效率）；**Kimi K3**（MoE sparsity 16/896 → **~2.5× scaling efficiency vs K2**）；**Mistral Large 4**（RL at scale **33B tokens/day**，3800 Grace Blackwell；未来更多 scaling）；**Meta Muse Wonder**（“Capabilities That Generalize”：**test-time compute scaling** 分析；stronger base → better OOD；scaling ladder）；**DeepSeek-V4**（**1M ctx 仅 27% FLOPs + 10% KV vs V3.2**；45T pretraining；DSec horizontal scaling）；**NVIDIA Nemotron**（RL scaling → 单调提升，“no saturation”）；**Apple**（PT-MoE cost/quality）。 |
| 多模态模型 | **Gemini 4**（natively multimodal text+image+audio+video；1M）；**Mistral Large 4**（natively multimodal；vision encoder 1.6B；Dense200 42%）；**Qwen4-Max**（native vision；**1M lossless**）；**Kimi K3/K3.1**（native vision + 1M；K3.1 3D/多模态）；**DeepSeek-V4.1-Flash**（native multimodal vision）；**Meta Muse Ember/Spark/Wonder**（text+image+audio+video；Muse Spark Open 816B natively multimodal）；**GLM-5.3-Flash / GLM-5.4**（image/video/text/file input）；**StepFun Step 5**（text+image+video；Step 3.7 Flash VL）；**NVIDIA Nemotron 3.5 Super VL**；**Apple**（multimodal on-device + server）；**Phi-4-reasoning-vision-15B**（SigLIP-2 + LM mid-fusion）；**Baichuan-Omni-1.5** / **Baichuan-M3**；**InternLM Sage**（Sage SciPerception >10 scientific modalities）；**Amazon Nova 2**（text+image+video+speech；Nova 2.5 Sonic speech-to-speech）；**Seed2.0**（world-leading visual understanding；SeedRealtime omni-modal；Seedream/Seedance）；**ByteDance Seed**。 |
| 长上下文模型 | **1M 已成常态**：Gemini 4（1M unified + 64K sync/1M background output）；Mistral Large 4（1M）；Qwen4-Max（1M）；Kimi K3/K3.1（1M）；DeepSeek-V4.1-Flash（1M + 384K output）；Muse Ember（1M + 512K output）；GLM-5.4/5.3/5.2（1M + 128K output）；StepFun Step 5（1M）；Nemotron 3.5 Super（1M）；**DeepSeek-V4.1-Flash KV-cache 压缩**（890 B/token，~1/4 vs V4-Flash，437× vs V1；SWA Bounded Replay ~1/8 persistent）；**GLM-5.3-Flash hybrid sparse+linear 降本**；**IndexShare**；**Mistral DSA+YOCO 16× KV reduction + 1.7× prefill @1M**；**Amazon Nova 2 Lite 1M**；**AFM ~3B KV-cache sharing**。 |
| 推理模型 / Reasoning | **OpenAI GPT-6.2**（RL reasoning；长 internal CoT；GPT-6.2 Astra **High AI Self-Improvement**；GPQA Diamond 97%；评估感知 <3%）；**Anthropic Fable/Mythos 5.2**（novel math/science reasoning；thinking；FrontierSWE/FrontierCode 等）；**NVIDIA Nemotron 3.5 Super**（长 CoT；RL）；**Kimi K3/K3.1**（long-horizon agentic；KDA）；**Mistral Large 4**（hybrid instruct-and-reasoning；3 modes；思考 token 效率）；**GLM-5.3/5.4**（always-on thinking；reasoning_effort；Loop deeper reasoning；part shifts into implicit loop depth）；**Zhipu GLM-4.5+** reasoning；**Meta Muse**（Active Focus；test-time compute scaling）；**Phi-4-reasoning-vision-15B**（multimodal reasoning；Chain-of-Thought；computer-use）；**Apple AFM**（reasoning + tool calls）；**StepFun Step 5**（agentic reasoning）；**Nemotron-Labs-Sigma**（continuous diffusion reasoning）。 |

## 逐家详情

### 1. DeepSeek

- **中文标题**：DeepSeek-V4.1-Flash：突破 KV Cache 压缩极限
- **英文标题**：DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression
- **发布机构**：DeepSeek（杭州深度求索）
- **模型名称/系列**：DeepSeek V4.1 Flash（API `deepseek-flash`；model version `DeepSeek-V4.1-Flash-1017`；同系 `DeepSeek-V4-Pro` `DeepSeek-V4-Pro-0813`；前序 `DeepSeek-V4` preview V4-Pro/V4-Flash；API 原生支持网页搜索与抓取）
- **发布日期**：2026-09-10（V4.1 Flash 首发）；model version **1017** 更新（**DeepSeek-V4.1-Flash-1017**，站点 banner + API 文档口径，约 2026-10-17）；技术报告 51 页；V4 preview arXiv 2026-04-26
- **核心参数**：**552B** backbone 参数；**1M** 上下文；max output **384K**；**Causal-Encoder-Decoder (CED)** 非对称 MoE：**8B prefill / 16B decode** 激活；40 层（20-layer causal encoder + 20-layer decoder）；global + sliding-window attention；RMSNorm + SwiGLU；**pretraining 45T multimodal tokens**；native multimodal（text+image）；comprehensive post-training：**SFT + RL + on-policy distillation (OPD)**；**CSA2 (Compressed Sparse Attention 2) cross-layer KV reuse + FP4 KV caching** → global KV **890 bytes/token**（~1/4 vs V4-Flash；~1/4 HBM / ~1/8 SSD vs 上一代；总 **437× vs V1**）；**SWA Bounded Replay** → persistent KV（SSD/host）~1/8 vs V4-Flash；**Muon** optimizer（V4）；**mHC (Manifold-Constrained Hyper-Connections)**（V4）；定价（API，人民币/百万 tokens，峰谷：闲时=高峰 1/2）：输入缓存命中 0.02/0.04、未命中 1/2、输出 4/8（V4.1 Flash）；具体 per-M 美元口径见官方页面。前序 **DeepSeek-V4-Pro 1.6T/49B + V4-Flash 284B/13B，1M，CSA+HCA + mHC + Muon，>32T tokens**（arXiv:2606.19348；1M 仅 27% FLOPs + 10% KV vs V3.2）
- **主要创新点（含重点关注）**：
  - **大模型新架构**：CED 非对称 MoE（prefill/decode 不对称激活）；streamlined V4 + efficient extensions；hybrid CSA+HCA；**CSA2**；**FP4 KV**；**SWA Bounded Replay**；mHC；Muon；native multimodal（3×3 pixel-unshuffle + linear projection vision）。
  - **长上下文/效率**：1M ctx；KV-cache 压缩极限；prefill 成本下降；Agent workload 成本下降；DeepSeek-V4 系列持续 KV 缩减。
  - **训练方法**：45T multimodal pretraining；SFT + RL + OPD；大规模自动化 data synthesis + environments；**DSec** horizontally scaling compute（sharding + relaxed consistency，scale units）；V4 完整 post-training pipeline；reasoning（思考模式 + 非思考可切换）。
  - **Scaling Law/缩放分析**：KV cache 缩放规律（每代 ~437× vs V1）；计算/存储/带宽 co-scaling；DSec 规模扩展。
  - **开源/系统**：open weights（HF `deepseek-ai/DeepSeek-V4.1-Flash`；版本 `DeepSeek-V4.1-Flash-1017`）；OpenAI/Anthropic 兼容 API；FIM（非思考）；Responses API；tool calls；JSON output。
- **arXiv/论文链接**：技术报告 PDF（官方链接）[DeepSeek_V41_Tech_Report.pdf](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/DeepSeek_V41_Tech_Report.pdf)（51 pages, “DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression”）；[官方新闻](https://www.deepseek.com/news/deepseek-v4-1-flash/)；[HF model](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)；[HF version 1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)；[API 定价/模型](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)；[DeepSeek-V4 arXiv:2606.19348](https://arxiv.org/abs/2606.19348)。**V4.1-Flash 本身不在 arXiv.org，报告以官方 PDF 形式发布。**

### 2. OpenAI

- **中文标题**：GPT-6.2 in ChatGPT 系统卡；GPT-6.2 系统卡（GPT-6.2 Astra 与 GPT-6.2 Sol）
- **英文标题**：GPT-6.2 in ChatGPT System Card; GPT-6.2 System Card (GPT-6.2 Astra and GPT-6.2 Sol)
- **发布机构**：OpenAI
- **模型名称/系列**：**GPT-6.2**；GPT-6.2 in ChatGPT（ChatGPT 优化版）；**GPT-6.2 Astra** / **GPT-6.2 Sol**；同系列 GPT-6.2（定价口径见官方）。OpenAI Deployment Safety Hub 当前最新条目：**GPT-6.2 in ChatGPT 系统卡（2026-11-23）** > GPT-6.2 系统卡（2026-11-17，Change log 更新至 2026-11-22）> OpenAI CSAM Image Classifier Model Card（2026-11-16）> GPT-6 Cyber（2026-11-05）> ChatGPT Images 2.6（2026-11-04）> GPT-Rosalind-6（2026-10-30）> GPT-6 Luna addendum（2026-10-29）> GPT-6.1 Terra（2026-10-26）。其他近期：GPT-6 Astra、GPT-6.1 Sol/Terra/Luna、GPT-Live、GPT-Rosalind-6
- **发布日期**：GPT-6.2 in ChatGPT 系统卡 **2026-11-23**；GPT-6.2 Astra/Sol 系统卡 **2026-11-17**（Change log 2026-11-22）
- **核心参数**：**参数量/架构/训练数据量未公开**；模型类型为 **reasoning model**（RL 训练，长 internal Chain-of-Thought，think-before-answer）；定价（官方页面/本窗口公开口径）：GPT-6.2 in ChatGPT $8/$0.40 cached/$40 per M in/out；GPT-6.2 Astra $8/$0.40/$40；GPT-6.2 Sol $2/$0.10/$10；GPT-6.2 in ChatGPT 生成 token 比 GPT-6 Astra 少约 22%（GDPval v2，自报）；模态以官方 API 页面为准；口径限制见系统卡 footnote
- **主要创新点（含重点关注）**：
  - **推理模型**：reasoning 通过 **reinforcement learning** 训练；长内部 CoT；自我纠错；refine thinking；evaluation-awareness **<3%** turns（系统卡口径）；CoT-evasion/private-reasoning distillation 抵抗（<1%；adaptive red-team <1% success）。
  - **训练方法**：diverse 经过过滤、去除 PII 的数据；RL；**GPT-6.2 in ChatGPT NanoGPT 训练节省 42.87%**（自报）；GPQA Diamond **95.6%**（in ChatGPT 口径）/ **97%**（Astra）；AI Self-Improvement 工程评测 Internal Research Debugging ~81.85–82.21%、KernelGen 1P ~74–77%。
  - **对齐/安全**：Preparedness Framework；**Critical threshold Cybersecurity**；**High threshold Biological & Chemical**；GPT-6.2 Astra **High AI Self-Improvement**（first externally released），Sol 不达 High；**Control Room**（track workloads across research infra, fast stop）；**Model Misalignment Reporting Framework**；stronger safeguards；Safe Completions；jailbreak resistance；indirect prompt injection robustness；**unauthorized distillation** 防护；hallucination；FGF Loss-of-Control Tier 1。
  - **网络安全**：Critical cyber；ExploitBench V8 100%；Sandbox Bench；tightened restrictions + vetting；UK AISI 88.6% 等自报对比；coding/bio sciences capability。
  - **Scaling Law**：系统卡不单列 Scaling Law 表；报告更强调 capability + safeguards；自报 token 效率（fewer generated tokens）。
- **arXiv/论文链接**：**非 arXiv**，Deployment Safety Hub 系统卡：[GPT-6.2 in ChatGPT 系统卡](https://deploymentsafety.openai.com/gpt-6-2-chatgpt) + [PDF](https://deploymentsafety.openai.com/gpt-6-2-chatgpt/gpt-6-2-chatgpt.pdf)；[GPT-6.2 Astra & Sol 系统卡](https://deploymentsafety.openai.com/gpt-6-2-astra-sol) + [PDF](https://deploymentsafety.openai.com/gpt-6-2-astra-sol/gpt-6-2-astra-sol.pdf)；[Change log](https://deploymentsafety.openai.com/gpt-6-2-astra-sol/change-log)；[Deployment Safety Hub](https://deploymentsafety.openai.com)；[Preparedness Framework](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf)；[FGF](https://cdn.openai.com/pdf/e37d949b-8c9f-4d76-b99e-4272f4631a7e/openai-frontier-governance-framework.pdf)。

### 3. Meta AI (LLaMA)

- **中文标题**：Introducing Muse Ember（我们最小、最高效的模型）；Introducing Muse Wonder；Introducing Muse Spark Open（最强美国开放权重模型）；Muse Spark 1.3
- **英文标题**：Introducing Our Smallest, Most Efficient Model: Muse Ember; Muse Wonder: A Frontier Model For Personal & Professional AI Agents; Introducing Muse Spark Open, The Most Capable US Open-Weight Model to Date; Introducing Muse Spark 1.3
- **发布机构**：Meta AI（Meta Platforms；research.meta.ai）
- **模型名称/系列**：**Muse** 家族（personal superintelligence）。最新日期：**Muse Ember `muse-ember-1.0`（2026-11-09）**；**Muse Wonder + Muse Wonder Full（2026-10-12）**；**Muse Spark Open（2026-10-15）**；Muse Spark **1.3（2026-09-02）/1.2/1.1**；Muse Wonder Full powers Muse Ember training；Muse Code / Meta Model API；SAM 3.1、Muse Image/Voice/Glimmer 等。**LLaMA** 系列：最新开放权重仍为 **LLaMA 4**（Scout 17B/16E ~109B MoE；Maverick 17B/128E ~400B MoE；natively multimodal；Scout 长上下文至 10M / Maverick 1M 口径以 Meta press/HF 为准；2025-04；Llama-Guard-4-12B 等安全模型）；本窗口未确认 LLaMA 5。HF org `meta-llama`（gated）。
- **发布日期**：Muse Ember **2026-11-09**；Muse Wonder **2026-10-12**；Muse Spark Open **2026-10-15**；Muse Spark 1.3 **2026-09-02**；LLaMA 4 **2025-04**
- **核心参数**：
  - **Muse Ember**：1M-token context + up to **512K output**；natively multimodal（text+image+audio+video）；API `muse-ember-1.0`；pricing $0.10 in / $0.50 out per M + cached $0.004（prompts ≤200K；longer $0.30/$1.50 + $0.012）；trained using **Muse Wonder Full**；Reasoning-effort settings；Responses API；参数量未公开；**evaluation report** 而非 full arXiv technical report。指标：AA Intelligence Index 36 / Coding Agent Index 46 / Terminal-Bench 4.0 40.9% / FrontierCode 2.0 27.2%（vs Claude Haiku 5.5 34.9%）/ OSWorld 2.1 69.5% partial / PerceptionBench 80.6%（with tools）/ AutomationBench-AA 37.8% 等（Meta 自报）。
  - **Muse Wonder / Full**：frontier personal+professional agents；**Active Memory** + **Active Focus**；stronger base models；scaling ladder；训练于 **Prometheus** gigawatt-scale；trained on diverse long-running tasks；CBRN + cyber safeguards；**model card** `/static/muse-wonder-model-card`；full safety report “available soon”；参数未公开。
  - **Muse Spark Open**：**816B total / 42B active**；natively multimodal；**1M ctx**；open-weight（Muse Model License）；US open-weight SOTA；custom auto-tunable **Helion** GPU kernels in SGLang（1.03–3.95× kernel speedups；3% e2e AMD MI350）；runs on 2× Apple M5 Ultra Mac Studio via MLX；SGLang/vLLM/TensorRT-LLM/Transformers/llama.cpp；additional safety post-training；Meta Superintelligence Scaling Framework；HF `meta-models/Muse-Spark-Open-816B-A42B`；eval methodology `/static/muse-spark-open-evaluation-methodology`；full evaluation report “available soon”；weights on HF/SageMaker/GC/MS Foundry. 另有 **Muse Glimmer** on-device open agentic。
  - **LLaMA 4**：open-weight；natively multimodal；MoE；Scout 17B/16E；Maverick 17B/128E；参数未在本窗口复核（gated HF）；technical report/ model card 见 Meta press + HF（未在本窗口抓取）。
- **主要创新点（含重点关注）**：
  - **大模型新架构**：Muse Spark Open sparse MoE 816B/42B；Muse Spark hybrid/multimodal；LLaMA 4 MoE + multimodal；**Muse Ember** 高效小模型；Helion kernels；Apple Silicon MLX。
  - **训练方法**：scaling ladder；large-scale pretraining + RL；**Active Memory/Active Focus**；test-time compute scaling；“Capabilities That Generalize”（in-distribution vs OOD scaling 分析）；Muse Ember trained by Muse Wonder Full；stronger base → better post-training transfer；safety alignment + prompt-injection resistance + private info handling + human-in-the-loop.
  - **Scaling Law/缩放分析**：Muse Wonder scaling 研究 + test-time compute scaling；Muse Spark 预测性 scaling；Meta Superintelligence Scaling Framework；LLaMA 4 scaling。
  - **多模态**：Muse Ember/Spark/Wonder natively multimodal；Muse Spark Open；LLaMA 4。
  - **长上下文**：Muse Ember 1M + 512K output；Muse Spark Open 1M；LLaMA 4 Scout 长上下文。
  - **推理模型**：Muse Active Focus；reasoning effort；Muse Wonder 多小时自主工作；SWE-Marathon；FocusBench；Muse Spark agentic coding。
- **arXiv/论文链接**：Muse Ember **非 arXiv**，[evaluation report](https://research.meta.ai/static/muse-ember-evaluation-report) + [announcement](https://research.meta.ai/blog/muse-ember)；Muse Wonder [model card](https://research.meta.ai/static/muse-wonder-model-card) + [announcement](https://research.meta.ai/blog/muse-wonder) + [scaling framework](https://research.meta.ai/blog/developing-capable-models-responsibly)；Muse Spark Open [eval methodology](https://research.meta.ai/static/muse-spark-open-evaluation-methodology) + [HF](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B) + [announcement](https://research.meta.ai/blog/muse-spark-open)；[Muse Spark 1.3](https://research.meta.ai/blog/introducing-muse-spark-1-3)；[Meta research blog](https://research.meta.ai/blog)；[LLaMA](https://ai.meta.com/llama/)；[meta-llama HF](https://huggingface.co/meta-llama)。**LLaMA 4 technical report 本窗口未抓取到一手 PDF（HF gated），不臆造。**

### 4. Google DeepMind (Gemini)

- **中文标题**：Introducing Gemini 4 Neon；Gemini 4 Neon Model Card；Gemini 4 Hydrogen；Gemini 4 Carbon；Gemini 4 Argon Model Card
- **英文标题**：Introducing Gemini 4 Neon; Gemini 4 Neon Model Card; Introducing Gemini 4 Hydrogen; Gemini 4 Carbon; Gemini 4 Argon Model Card
- **发布机构**：Google DeepMind
- **模型名称/系列**：**Gemini 4**。四档：**Gemini 4 Argon**（base/frontier，not a fine-tune；2026-10）→ **Gemini 4 Carbon**（flagship long-horizon；adapted from Argon；2026-10/11）→ **Gemini 4 Neon**（adapted from Carbon；**latest announcement 2026-11**）& **Gemini 4 Hydrogen**（adapted from Carbon；fast everyday；2026-11）；plus Gemini Omni / Nano Banana / Gemini Audio / Veo / Gemma。最新 model card：Neon（Published November 2026）。
- **发布日期**：Argon 2026-10；Carbon 2026-10-27 + now available 2026-11；**Hydrogen 2026-11；Neon 2026-11-18（页面/公告 November 2026）**；model cards Published November/October 2026
- **核心参数**：**参数量未公开**；**1M unified context window**（combined input+output；inputs text+image+audio+video）；output up to **64K default synchronous / up to 1M background long decode**；定价（Neon 公告口径 $3/$15 per M in/out；cached $0.15/M，95% discount；Argon/Hydrogen 价格见官方）；Neon balances depth+efficiency；Carbon frontier; Hydrogen speed/efficiency; Neon adapted from Carbon; Hydrogen adapted from Carbon; Carbon based on Argon; Argon not modification/fine-tune.
- **主要创新点（含重点关注）**：
  - **大模型新架构**：**large-scale sparse Mixture-of-Experts (MoE) transformer**（Argon）；natively multimodal（text+vision+audio）；model dependencies（Neon←Carbon←Argon；Hydrogen←Carbon）；frontier-sparse / long-context efficiency；safety hardening；“previously next-era frontier”。
  - **训练方法**：large-scale diverse multimodal pre-training（public web + text + code + images + audio + video）；post-training instruction tuning + **reinforcement learning** + human-preference；RL for **multi-step reasoning, problem-solving, theorem-proving**；safety RL; Frontier Safety Framework; prompt-injection resistance; misalignment monitoring.
  - **Scaling Law**：model cards 不披露 scaling-law 数值；Google 强调 scale + RL；Gemini 4 benchmark methodology 公开。
  - **多模态**：natively multimodal; any-modality in; text out; 1M.
  - **长上下文**：1M unified; GraphWalks BFS F1 95.2% (256k→1M) 等自报.
  - **推理模型**：Gemini 4 reasoning; long-horizon agentic; AA Index/Vals 等自报; HLE-Diamond 等.
  - **评测**：methodology https://deepmind.google/models/evals-methodology/gemini-4-neon/ 等.
- **arXiv/论文链接**：**Google 以 Model Card 而非 arXiv technical report 发布**。[Gemini 4 Neon Model Card (PDF)](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Neon-Model-Card.pdf)；[Gemini 4 Hydrogen Model Card](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Hydrogen-Model-Card.pdf)；[Gemini 4 Carbon Model Card](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Carbon-Model-Card.pdf)；[Gemini 4 Argon Model Card](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Argon-Model-Card.pdf)；[Introducing Gemini 4 Neon (blog)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)；[Introducing Gemini 4 Hydrogen](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)；[Gemini 4 Carbon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)；[Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)；[Gemini 4 safety](https://blog.google/innovation-and-ai/technology/safety-security/gemini-4-model-safety-security/)；[models page](https://deepmind.google/models/gemini/)。

### 5. Anthropic (Claude)

- **中文标题**：Introducing Claude Fable 5.2 and Claude Mythos 5.2；System Card: Claude Fable 5.2 & Claude Mythos 5.2
- **英文标题**：Introducing Claude Fable 5.2 and Claude Mythos 5.2; System Card: Claude Fable 5.2 & Claude Mythos 5.2
- **发布机构**：Anthropic, PBC
- **模型名称/系列**：**Claude Fable 5.2** / **Claude Mythos 5.2**（同一 new LLM 两种 configuration）；同系 Claude **Opus 5.5**（2026-09-22）、**Sonnet 5.5**（2026-09-28）、**Haiku 5.5**（2026-10-07）。Fable=general use + safeguards in high-risk dual-use domains（biology/cybersecurity）；Mythos=more permissive safeguards；Mythos direct access limited to vetted individuals/orgs via **trusted access programs**；Mythos powers **Claude Security**（all Claude Enterprise）。Claude Security 等。
- **发布日期**：**2026-11-09**；System Card **November 9, 2026**（264 pages；Change log within）
- **核心参数**：**参数量/架构/训练数据量未公开**；no mixture-of-experts disclosure；multilingual; text-only output; knowledge cutoff 页面未在本卡展开。定价 $8/M input、$40/M output；Fast mode $16/$80（+2.5× speed）；output up to 30% faster; pricing 口径以官方为准。基准（自报）：FrontierCode 2.0 Fable 49.1%; FrontierSWE v2 69.9%; AA-Briefcase v1.1 66.1%; AutomationBench 51.4%; Mythos CyScenarioBench 76.3%/CVE Rediscovery 89.6%/OSWorld 2.1 89.3%; "千代理两周内正式化 Fermat's Last Theorem" 等.
- **主要创新点（含重点关注）**：
  - **训练方法**：**pretraining + substantial post-training & fine-tuning**；alignment to **Claude's constitution**；**Responsible Scaling Policy (RSP)** + **Frontier Compliance Framework (FCF)**；system card covers **seven areas** pre-deployment evals; **autonomy threat model 1/2** assessment; transparent web crawler (identifiable + preference signals); hallucination mitigation; safeguards.
  - **对齐/安全**：Fable vs Mythos safeguard split; dual-use CBRN/cyber; **best-ever distillation defenses** (illicit distillation −90%+; Cyber Verification Program); **misalignment monitoring**; independent evaluators (METR...); **reasoning/CoT monitorability** evaluation.
  - **推理模型**：novel mathematical & scientific reasoning; long-horizon agentic; thinking; coding/sciences/finance.
  - **Scaling Law/缩放分析**：system card 含 scaling/acceleration 分析（AECI lagging indicator; breakpoint/one-time jump 分析；不单列“Scaling Law”公式）；RSP scaling thresholds.
  - **多模态**：Claude Fable/Mythos 5.2 text model；Anthropic 多模态产品另计；本卡“model outputs text only”. **长上下文**：见官方（本卡未显式给数值，不臆造）.
- **arXiv/论文链接**：**非 arXiv**。[Announcement](https://www.anthropic.com/claude-fable-and-mythos-5-2) / [news](https://www.anthropic.com/news/claude-fable-and-mythos-5-2)；[**System Card PDF**](https://www.anthropic.com/document/claude-fable-5-2-mythos-5-2-system-card)（redirect → [assets.claude.com PDF](https://assets.claude.com/27d60918d218125e7504bc7354c4b4626ec56b11.pdf)）；[RSP](https://www.anthropic.com/responsible-scaling-policy)；[Claude Security]...；[distillation defenses](https://www.anthropic.com/news/distillation-defenses)。**未在本卡发现 arXiv 链接。**

### 6. Mistral AI

- **中文标题**：Introducing Mistral Large 4（Le Chonk）；Mistral Large 4 技术报告；Le Chonk：Built for Coders, Trusted by Defenders.
- **英文标题**：Introducing Mistral Large 4; Mistral Large 4 (Technical Report); Le Chonk: Built for Coders, Trusted by Defenders. (We release the weights of Le Chonk...)
- **发布机构**：Mistral AI
- **模型名称/系列**：**Mistral Large 4 (ML4, “le Chonk”)**；**Open-weight hybrid instruct-and-reasoning MoE + natively multimodal**；unifies instruction + reasoning + agentic；**Le Chonk** open-weight release；API `mistral-large-4` / `mistral-large-4-0`；Mistral Ecosystem Open-Weight license；Microsoft Foundry / NVIDIA NIM / TensorRT-LLM / NeMo AutoModel 等。前序 Mistral Medium 3.5、Small 4、Voxtral 3 等。
- **发布日期**：**Mistral Large 4 public preview 2026-10-06**；**weights released (“Le Chonk”) 2026-10-29**（official “released end of month”）；**improved open-weight version** 同时发布；**technical report submitted 2026-11-03**（alphaXiv `2611.mistral-large-4`）；“3 weeks additional RL” 改进版口径
- **核心参数**：**1 trillion total parameters / 52B active**（官网 “1 trillion-parameter...52 billion active”；docs 表列 **1050B total / 52B active**；HF repo `Mistral-Large-4-1T-A52B`；technical report “52B active, 1T total”；此前速览 1.05T 口径已纠正）；**1M context**；natively multimodal；vision encoder ~1.6B；trained from scratch **3,800 NVIDIA Grace Blackwell GPUs**（Mistral European datacenters）；**160+ languages**（含所有 EU 官方语言）；post-training **SFT + RL**；RL environments composable；**~33B tokens/day RL rollouts（16B trainable completion tokens after filtering/masking）@3k GPUs**；**multiple-teacher distillation** → **Low / Medium / High reasoning modes**（High default；“replaces None”）；**sparse attention + DSA + YOCO + LeRoPE + SSMax + optimized context parallelism + prefill-decode disaggregation + speculative decoding (DSpark)**；**NVFP4 calibrated 606GB checkpoint on 4 GB300 GPUs**；KV-cache 16× reduction; YOCO 1.7× prefill @1M（技术报告口径，未完全独立复现）；pricing $0.7/$0.07 cached/$2.1 per M. 
- **主要创新点（含重点关注）**：
  - **大模型新架构**：1T/52B sparse MoE; natively multimodal; hybrid instruct-and-reasoning; **DSA (DeepSeek Sparse Attention, top-2048)**; **YOCO** KV sharing; **LeRoPE**; **SSMax**; ragged MLA→surgery→full attention + sparse; NVFP4; CLA/YOCO restoration; (technical report details).
  - **训练方法**：SFT + **RL at scale**; composable environments (single-turn→long-horizon tool use; safety/factuality; reward models + unit tests + LLM judges + static checks); **agent-based pipeline authoring & verifying executable environments** (software eng, cyber, knowledge work); async actor fleet; long-trajectory rollouts; off-policy drift minimization; **multiple-teacher distillation**; three reasoning modes; “RL still in flight, no saturation”.
  - **Scaling Law/缩放分析**：RL scaling (more RL → gains, no saturation); “loss vs agentic penalty” observation（perplexity doesn't predict SWE-bench Verified; sparse attention later efficiency）; “scaling RL”; infra scaling; (技术报告 + blog).
  - **多模态**：natively multimodal; visual grounding; Dense200 42% vs GPT-6-Astra 41%; ChartQA Pro; GDP.pdf.
  - **长上下文**：1M; sparse attention efficiency; long-context serving; YOCO; prefill disaggregation.
  - **推理模型**：hybrid instruct-and-reasoning; 3 reasoning modes; long-horizon agentic; coding; cyber.
  - **开源/系统**：open weights; Mistral Ecosystem Open-Weight license; **full technical report**; training environment reused by customers (Forge); self-host; cyber variant for vetted partners; safety guardrails; harmful-cyber refusal 96.6%.
- **arXiv/论文链接**：[Introducing Mistral Large 4](https://mistral.ai/news/mistral-large-4/)；[Le Chonk open-weight + technical report](https://mistral.ai/news/mistral-large-4-oss/)；[docs](https://docs.mistral.ai/models/mistral-large-4-0)；[model card](https://docs.mistral.ai/models/mistral-large-4-0)；**[Technical Report (alphaXiv `2611.mistral-large-4`, submitted 2026-11-03)](https://www.alphaxiv.org/abs/2611.mistral-large-4)** + [PDF](https://www.alphaxiv.org/pdf/2611.mistral-large-4)；[HF weights](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B)；[technical_report.pdf (HF)](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B/blob/main/assets/technical_report.pdf)；[license](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B/blob/main/LICENSE)。**注意：技术报告发布在 alphaXiv，而非 arXiv.org；用户称 arXiv 但本报告不在 arXiv.org。**

### 7. Qwen (Alibaba)

- **中文标题**：Alibaba Unveils Qwen4-Max: New AI Teammate for Work, Creativity, and Discovery；Qwen4-Max: One Flagship for Complex Work, at a Price That Scales
- **英文标题**：Alibaba Unveils Qwen4-Max: New AI Teammate for Work, Creativity, and Discovery; Qwen4-Max: One Flagship for Complex Work, at a Price That Scales
- **发布机构**：Alibaba / Alibaba Cloud（Qwen Team；Alibaba Cloud Community 发布）
- **模型名称/系列**：**Qwen4-Max**（Qwen4 架构；最强 Qwen4 flagship）；API on **QwenCloud** + QwenWork + QwenStudio；"Qwen4-Max"；input implicit-cache-hit $0.075/1M；open-weight smaller Qwen4 coming；Qwen4 系列。新 research blog 迁至 **qwen.ai/research**（qwenlm.github.io 重定向；旧 blog 停留 Qwen3 时代，如 Qwen3Guard/GSPO）。
- **发布日期**：**2026-11-16**（Hangzhou，Alibaba Cloud Community）；后续 2026-11-17 Enterprise 场景文；本窗口核验 2026-11-27
- **核心参数**：**2.4 trillion total parameters / 71 billion active per token**（官方；“activates only 71B per token”；**25% fewer activated params vs Qwen3.8-Max** @2.4T；更少 activation）；**native vision**；**1-million-token context window**（“up to 1M”；前序速览称 lossless；以官方为准）；**Qwen4 architecture sparse MoE upgrades across attention, residual connections, and embeddings**；**Gated DeltaNet + Qwen Sparse Attention + Gated Residual + N-gram embedding**（前序核验 + 官方“Gated DeltaNet + Qwen Sparse Attention + Gated Residual + N-gram”；N-gram embedding ~328B 口径见前序，本窗口未在官方页复核数字）；Cloud Resource Scheduling（自主闭环）;**open-weight smaller Qwen4 coming**。训练数据量未在该页公开。基准自报：Code Arena #6; Work360 35% fewer tokens @High effort + ~60% lower cost/task vs Qwen3.8-Max; etc.
- **主要创新点（含重点关注）**：
  - **大模型新架构**：Qwen4 sparse MoE 升级；**Gated DeltaNet**（linear attention）+ **Qwen Sparse Attention** + **Gated Residual** + **N-gram embedding**；native vision; 2.4T/71B; 1M.
  - **训练方法**：post-training efficiency; coding-security checks in SWE training; defensive data kept + offensive removed; dedicated safety datasets + post-training CBRN; governance;（Qwen4 技术报告细节本窗口未确认，不臆造）。
  - **Scaling Law/缩放分析**：2.4T scale + 25% fewer activated; total-vs-active scaling; token efficiency; long-horizon 48h agent runs; (前序速览口径；官方该页不单列 Scaling Law 公式)。
  - **多模态**：native vision.
  - **长上下文**：1M; (lossless 口径见前序/官方措辞，不独立复核).
  - **推理模型**：long-horizon agents; agentic coding; knowledge work; scientific discovery; professional workflows.
- **arXiv/论文链接**：**本窗口未发现 Qwen4-Max 独立 arXiv 技术报告**；官方社区博客 [Alibaba Unveils Qwen4-Max](https://community.alibabacloud.com/blog/alibaba-unveils-qwen4-max-new-ai-teammate-for-work-creativity-and-discovery_603783)；[Qwen4-Max: One Flagship...](https://community.alibabacloud.com/blog/qwen4-max-one-flagship-for-complex-work-at-a-price-that-scales_603806)；[QwenCloud](https://www.qwencloud.com)；[Qwen research](https://qwen.ai/research)；[Qwen4-Max tag]...；HF `Qwen` org（本窗口未见 Qwen4 权重，open-weight 待发布）。**不臆造 arXiv ID。**

### 8. Yi (01.AI)

- **中文标题**：Yi: Open Foundation Models by 01.AI；Yi-Lightning
- **英文标题**：Yi: Open Foundation Models by 01.AI; Yi-Lightning
- **发布机构**：01.AI（零一万物，Beijing；Kai-Fu Lee）
- **模型名称/系列**：**Yi**（Yi-6B/34B；chat; 200K; depth-upscaled; vision-language; **Yi-Lightning** 100B MoE 2024-10；**Yi-Coder**；**Yi-VL**）。最新已知 model **Yi-Lightning**（2024-10-16；LMSYS 盲测 global #6 / China #1）。01.AI 网站现转向企业产品（TrueNorth / Boss AI / WorldWise 等），未见 2026 新模型/报告。最新 technical report **Yi: Open Foundation Models**（2024-03）。
- **发布日期**：Yi technical report **2024-03-07**（arXiv 2403.04652）；Yi-Lightning **2024-10-16**；本窗口未确认 2026 新报告。
- **核心参数**：Yi base **6B / 34B**；pretraining **3.1T tokens**；classic transformer; multilingual; 200K long context variants; multimodal extensions; **Apache 2.0**; chat; data quality emphasis; Yi-Lightning **100B MoE**（2024-10）。无 2026 参数更新。
- **主要创新点**：data-engineering/data-quality; classical transformer + scale; long-context 200K; multimodal; MoE (Yi-Lightning); human-preference; instruction tuning; scaling via data quality（“primarily data quality”）. 本窗口无新增架构/训练信息。
- **arXiv/论文链接**：[Yi: Open Foundation Models by 01.AI (arXiv:2403.04652)](https://arxiv.org/abs/2403.04652)；[01.AI](https://www.01.ai)；[GitHub 01-ai](https://github.com/01-ai)；[lingyiwanwu](https://www.lingyiwanwu.com)。**无 2026 新 arXiv 技术报告。**

### 9. Baichuan（百川智能）

- **中文标题**：Baichuan-M3: Modeling Clinical Inquiry for Reliable Medical Decision-Making；Baichuan-M2: Beyond the Model: Scaling Medical Capability with a Large Verifier System
- **英文标题**：Baichuan-M3: Modeling Clinical Inquiry for Reliable Medical Decision-Making; Baichuan-M2: Beyond the Model: Scaling Medical Capability with a Large Verifier System
- **发布机构**：Baichuan Intelligent Technology（百川智能）
- **模型名称/系列**：**Baichuan-M3-235B**（医疗增强 LLM；clinical-grade decision support；2026-02；GPTQ-INT4）；**Baichuan-M2-32B**（医疗增强推理；Qwen2.5-32B 基座；2025-09；MTP；W4）；**Baichuan-M1-14B**；**Baichuan-Omni-1.5**；**Baichuan-Audio**；Baichuan2/7B/13B 等。
- **发布日期**：Baichuan-M3-235B **2026-02-06**（arXiv）/ repo updated 2026-02-09；technical report; tech blog baichuan-ai.com/blog/baichuan-M3; Baichuan-M2 **2025-09** (arXiv 2509.02208). 本窗口官网 www.baichuan-ai.com **不可达**，改用 GitHub 官方 `baichuan-inc`。
- **核心参数**：M3 **235B**；M2 **32B**（base Qwen2.5-32B）；Apache 2.0; HF `baichuan-inc/Baichuan-M3-235B` + GPTQ-INT4; **W4 quantization −74% memory; Gated Eagle3 speculative decoding +96% speed**; medical + general. 训练数据量未在摘要公开。
- **主要创新点**：
  - **训练方法**：model **clinical decision-making workflow**; **proactive information acquisition**; **long-horizon reasoning**; **adaptive hallucination suppression**; **Fact-Aware RL**; **Large Verifier System**（patient simulator + multi-dim verification；medical domain adaptation mid-training；**multi-stage RL** hierarchical；M2）.
  - **多模态**：Baichuan-Omni-1.5; (M3 focus medical text).
  - **推理模型**：medical reasoning; evidence synthesis; low hallucination; SCAN-bench; HealthBench.
  - **Scaling Law**：“Scaling Medical Capability with a Large Verifier System” (M2 title); verifier scaling; not a general Scaling-Law paper.
  - **评测**：HealthBench SOTA; HealthBench-Hard +28pp; HealthBench-Hallu; **SCAN-bench** (clinical inquiry/lab/diagnosis); beats GPT-5.2 in clinical inquiry/advisory/safety; M2 HealthBench 60.1 vs GPT-5 etc.
- **arXiv/论文链接**：[Baichuan-M3 arXiv:2602.06570](https://arxiv.org/abs/2602.06570) + [PDF](https://arxiv.org/pdf/2602.06570)；[GitHub Baichuan-M3-235B](https://github.com/baichuan-inc/Baichuan-M3-235B)；[HF](https://huggingface.co/baichuan-inc/Baichuan-M3-235B)；[Baichuan-M2 arXiv:2509.02208](https://arxiv.org/abs/2509.02208)；[GitHub org](https://github.com/baichuan-inc)。**官网本窗口不可达。**

### 10. Microsoft (Phi)

- **中文标题**：Phi-4-Reasoning-Vision-15B；Phi-4-Reasoning-Vision: The Lessons of Training a Multimodal Reasoning Model；FrogNano-4B（未确认技术报告）
- **英文标题**：Phi-4-Reasoning-Vision-15B; Phi-4 Reasoning Vision and the Lessons of Training a Multimodal Reasoning Model; FrogNano-4B (unverified technical report)
- **发布机构**：Microsoft（Microsoft Research / Microsoft Corporation；Microsoft Foundry；Windows/Edge 口径另计）
- **模型名称/系列**：**Phi-4-Reasoning-Vision-15B**（compact open-weight multimodal reasoning；`microsoft/Phi-4-reasoning-vision-15B`；API `Phi-4-Reasoning-Vision-15B`）；Phi-4 / Phi-4-reasoning / Phi-4-mini / Phi-4-multimodal；Phi-4-reasoning-plus; **FrogNano-4B-2609**（HF `microsoft/FrogNano-4B-2609`）；Phi-3.5 等。Microsoft 自家 Copilot 模型不在此；本项聚焦 **Phi**。
- **发布日期**：**Phi-4-Reasoning-Vision-15B release 2026-03-04**；HF lastModified 2026-08-31；technical report **arXiv 2511.19663**（页面 Paper 2511.19663；**release 2026-03-04 vs arXiv 提交时间以 arXiv 页面为准**）；Microsoft Research blog；FrogNano-4B-2609 created 2026-09-17（**本窗口未确认 standalone technical report**；前序速览 FrogNano-4B 2026-11-15 口径未在官方一手复核）。
- **核心参数**：**15B**；**16,384-token context**；inputs text+images; output text; **Phi-4-Reasoning backbone + SigLIP-2 vision encoder; mid-fusion**；**MIT license**；**Training GPUs 240 B200s; 4 days; training dates 2025-02-03→2026-02-21**；model dependency Phi-4-Reasoning; reasoning + vision + math + OCR + GUI-grounding + computer-use; Chain-of-Thought; LoRA-ready. FrogNano-4B **4B**（qwen3_5 tag; no verified params/tech report）. 
- **主要创新点**：
  - **大模型新架构**：mid-fusion vision-LLM; SigLIP-2; pretrained LM + projected visual tokens; Phi-4-reasoning base.
  - **训练方法**：multimodal reasoning training; compact data; few GPUs; (see technical report); 
  - **多模态**：vision+reasoning; OCR; ChartQA; MathVista; MMMU; ScreenSpot-V2; GUI grounding; computer-use.
  - **推理模型**：Phi-4-Reasoning; Chain-of-Thought; thinking.
  - **Scaling Law**：“lessons of training a multimodal reasoning model”; small-model scaling; no separate Scaling-Law table.
- **arXiv/论文链接**：[Phi-4-Reasoning-Vision-15B HF](https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B)；[Technical Report (arXiv:2511.19663)](https://arxiv.org/abs/2511.19663) / [aka.ms/Phi-4-reasoning-vision-15B-TR](https://aka.ms/Phi-4-reasoning-vision-15B-TR)；[Microsoft Research blog](https://www.microsoft.com/en-us/research/blog/phi-4-reasoning-vision-and-the-lessons-of-training-a-multimodal-reasoning-model/)；[Microsoft Foundry](https://aka.ms/Phi-4-r-v-foundry)；[GitHub](https://github.com/microsoft/phi-4-reasoning-vision-15B)；[Phi-4 technical report arXiv:2412.08905]...（Phi-4 原报，本窗口未复核）；[FrogNano-4B-2609 HF](https://huggingface.co/microsoft/FrogNano-4B-2609)。**FrogNano 无已验证 arXiv。**

### 11. Apple

- **中文标题**：Apple Intelligence Foundation Language Models Tech Report 2025；Apple Intelligence Foundation Language Models；Introducing Siri AI（Apple Intelligence 与 Siri 下一代）
- **英文标题**：Apple Intelligence Foundation Language Models Tech Report 2025; Apple Intelligence Foundation Language Models; Introducing Siri AI
- **发布机构**：Apple（Apple Machine Learning Research）
- **模型名称/系列**：**Apple Intelligence Foundation Language Models (AFM)**；~3B on-device + server model; **Apple Foundation Model 3 (AFM 3)** / AFM 3 Cloud（产品页口径）; **Siri AI** next generation; Private Cloud Compute; Foundation Models framework. 最新已验证 **technical report = Tech Report 2025**（July 2025）；本窗口 apple.com/ai 显示 Siri AI/AFM 3 产品但 **未见新的 AFM 3 arXiv technical report**。
- **发布日期**：Tech Report 2025 **July 2025**（updates introduced June 9, 2025）；原始 **Apple Intelligence Foundation Language Models** **2024-07-29**；Siri AI / next-gen Apple Intelligence **2026-11**（产品，页面未标具体日期）。
- **核心参数**：on-device **~3B**；server **PT-MoE (Parallel-Track Mixture-of-Experts)**（track parallelism + MoE sparse + interleaved global-local attention）；on-device **KV-cache sharing + 2-bit quantization-aware training**；multilingual + multimodal; image understanding + tool calling; **Private Cloud Compute**; no user data retained; no public total server params; AFM 3 ~**20B sparse**（apple.com/ai footnote 口径 “AFM 3”，本窗口未在 research 技术报告复核）. 
- **主要创新点**：
  - **大模型新架构**：on-device 3B efficient + server **PT-MoE**; KV-cache sharing; 2-bit QAT; interleaved global-local attention; track parallelism.
  - **训练方法**：large-scale multilingual/multimodal data（responsible web crawling + licensed + synthetic）; **SFT + reinforcement learning on new asynchronous platform**; responsible AI; safeguards; Private Cloud Compute.
  - **多模态**：image understanding; tool calling; multilingual.
  - **推理模型**：foundation models for Apple Intelligence; Siri AI; tool use; guided generation; constrained tool calling.
  - **Scaling Law**：not explicitly; PT-MoE cost/quality; Private Cloud Compute scaling; Swift Foundation Models framework. 
  - **开发**：**Foundation Models framework**; guided generation; constrained tool calling; **LoRA adapter fine-tuning**.
- **arXiv/论文链接**：[Apple Foundation Models Tech Report 2025](https://machinelearning.apple.com/research/apple-foundation-models-tech-report-2025) + [arXiv:2507.13575](https://arxiv.org/abs/2507.13575); [Apple Intelligence Foundation Language Models (2024)](https://machinelearning.apple.com/research/apple-intelligence-foundation-language-models); [Apple Intelligence & Siri AI](https://www.apple.com/ai/); [Apple ML Research](https://machinelearning.apple.com/research/); [Foundation Models framework](https://developer.apple.com/apple-intelligence/). **无 AFM 3 arXiv technical report 本窗口。**

### 12. NVIDIA

- **中文标题**：What RL on Expert-Built Tasks Teaches Nemotron 3.5 Super；Nemotron 3.5 Bolt E4B 4GB: An Open and Efficient Small Language Model for Fast Conversational Agents；Nemotron-Labs-Sigma / Large Language Continuous Diffusion Models
- **英文标题**：What RL on Expert-Built Tasks Teaches Nemotron 3.5 Super; Nemotron 3.5 Bolt E4B 4GB: An Open and Efficient Small Language Model for Fast Conversational Agents; Large Language Continuous Diffusion Models (Nemotron-Labs-Sigma); Nemotron-Labs-VisualCreation: Pixel as Code for Agentic Visual Creation
- **发布机构**：NVIDIA
- **模型名称/系列**：**NVIDIA Nemotron**（**Nemotron 3.5 Super**；**Nemotron 3.5 Bolt (E4B 4GB)**；**Nemotron 3.5 Lightning**；**Nemotron 3** / 3 Ultra；**Nemotron-Labs-Sigma**；**Nemotron-Labs-VisualCreation**；**Nemotron-Labs-Diffusion-Uni**；VL variant；**Nemotron-Safety** 等）；NeMo / Tinker / NIM / TensorRT / **NVFP4**。最新 flagship **Nemotron 3.5 Super 2026-11-17**。
- **发布日期**：Nemotron 3.5 Super **2026-11-17**（arXiv 2611.22161）；Nemotron 3.5 Bolt **2026-11-16**（arXiv 2611.20771）；Nemotron-Labs-Sigma arXiv 2610.02665 v2 2026-10-02；Nemotron-Labs-VisualCreation **2026-11-23**（arXiv 2611.31358）；Nemotron 3 Ultra 2026-09-10；Nemotron 3.5 Lightning arXiv 2610.38095.
- **核心参数**：**Nemotron 3.5 Super: 120B total / 12B active**；**hybrid MoE + Mamba (Mamba-Transformer hybrid, hybrid-routing Mamba)**；**1M context**；VL variant；RL on **5 expert-built datasets**; **rank-32 LoRA + CISPO** on Tinker; **no SFT stage**; twelve headline benchmarks; SWE-bench Pro V2 86.9→92.1%; Terminal-Bench 2.1 63.9→70.3%; GDP_pdf 10.4→24.2% etc. Bolt **E4B 4GB** small efficient conversational agents. Sigma **continuous diffusion LLM**. **NVFP4** quantization（Mistral Large 4 report also uses NVIDIA NVFP4/GB300）. 其他 Nemotron 参数/训练数据未公开；NVIDIA 以 model cards + arXiv post-training report 而非单一 “Nemotron technical report” 发布。
- **主要创新点**：
  - **大模型新架构**：**hybrid MoE+Mamba**; hybrid-routing; **continuous diffusion language model** (Sigma); pixel-as-code VLA/visual creation; small efficient 4GB model; NVFP4.
  - **训练方法**：**pure RL post-training, no SFT**; **CISPO**; rank-32 LoRA; expert-built task datasets; verifiable rewards; long-horizon; Tinker; async RL; “no saturation”; RL scaling.
  - **Scaling Law/缩放分析**：RL scaling; hybrid MoE+Mamba efficiency; KV/cache efficiency; NVFP4; small-model scaling.
  - **多模态**：VL variant; scientific/visual; Nemotron-Labs-VisualCreation.
  - **长上下文**：1M.
  - **推理模型**：long CoT; RL; reasoning; agentic; tool use.
- **arXiv/论文链接**：[Nemotron 3.5 Super arXiv:2611.22161](https://arxiv.org/abs/2611.22161)；[Nemotron 3.5 Bolt arXiv:2611.20771](https://arxiv.org/abs/2611.20771)；[Nemotron-Labs-Sigma arXiv:2610.02665](https://arxiv.org/abs/2610.02665)；[Nemotron-Labs-VisualCreation arXiv:2611.31358](https://arxiv.org/abs/2611.31358)；[Nemotron 3.5 Lightning arXiv:2610.38095];[nvidia HF](https://huggingface.co/nvidia);[NVIDIA technical blog](https://developer.nvidia.com/blog);[NVIDIA Nemotron page]...。**多为 NVIDIA 官方 arXiv + model cards，非单一整体技术报告。**

### 13. xAI (Grok)

- **中文标题**：Introducing Grok 4.7；Grok 4.7 Model（无独立技术报告）
- **英文标题**：Introducing Grok 4.7; Grok 4.7 (no standalone technical report in this window)
- **发布机构**：xAI（**SpaceXSI / SpaceX Super Intelligence LLC**；xAI joined SpaceX 2026-02-02）
- **模型名称/系列**：**Grok 4.7**（`grok-4.7` / xhigh; fast variant）；Grok 4.6; Grok 4.5; Grok 4; **Grok Bot 1.0**（agent product 2026-11-11）; Grok Voice 3.0; Grok Imagine；**Grok-1** open-weight **314B MoE**（2024-03-17）. 
- **发布日期**：**Grok 4.7 2026-09-21**；Grok 4.6 2026-08-12；Grok Bot 1.0 2026-11-11；本窗口核验 2026-11-27。
- **核心参数**：**参数量未公开**；**new, larger base model** vs Grok 4.6; served same price/speed; **longer reinforcement learning** on harder multi-hour tasks; better self-verification; longer context management; **Grok Bot harness** native; new safeguard stack; pricing $2 in / $6 out per M (fast variant 2× price + 2× output speed; served same as 4.6 headline); benchmarks CursorBench 4.0 46.3%; DeepSWE v1.1 71.0%*; EEBench 64.0%; AA Briefcase v1.1 1,657; Terminal-Bench 4.0 37.6%; Harvey Legal 19.6%; HealthBench Professional 56.7%; GDPval etc. (自报). Grok-1 open 314B MoE known but Grok 4.x not open.
- **主要创新点**：**RL scaling** (longer RL, harder tasks, multi-hour); self-verification; context management; agent harness; **safety & cyber** (jailbreak resistance; dual-use; defensive cyber; bio safety; invite-only red-team); long-context; coding + knowledge work. **新架构细节未公开；无 arXiv technical report。**
- **arXiv/论文链接**：[Introducing Grok 4.7 (x.ai)](https://x.ai/news/grok-4-7)；[Grok 4.6](https://x.ai/news/grok-4-6)；[xAI news](https://x.ai/news)；[Grok-1 open release](https://x.ai/news/grok-os);[docs.x.ai](https://docs.x.ai). **本窗口未找到 Grok 4.7 arXiv 技术报告。**

### 14. Amazon (Amazon Nova)

- **中文标题**：Amazon Nova 2 / Amazon Nova 2 Lite / Amazon Nova 2.5 Sonic；Amazon Nova 系列
- **英文标题**：Amazon Nova 2; Amazon Nova 2 Lite; Amazon Nova 2.5 Sonic; Amazon Nova
- **发布机构**：Amazon Web Services (AWS)
- **模型名称/系列**：**Amazon Nova 2**（**Nova 2 Lite**；**Nova 2.5 Sonic**；Nova Multimodal Embeddings；**Nova 2 Sonic**；Nova 2 base models via Bedrock）；**Nova Act**（custom Nova 2 Lite computer-use agent；GA）；**Nova Forge**（build your own frontier）；**Nova** original (Pro/Lite/Micro/Premier + Canvas/Reels...)。Nova 2 **released 2025-12-02**（前序口径）；本窗口 AWS 页面核验 Nova 2.5 Sonic **2026-10** + Nova 2 Lite。
- **发布日期**：Nova 2 2025-12-02（前序）；Nova 2 Lite AWS blog 2025-12；**Nova 2.5 Sonic what's-new 2026-10**；Nova Act GA；本窗口核验 2026-11-27；**Nova 2 Lite** current. 
- **核心参数**：**参数量未公开**；Nova 2 Lite **1M-token context**; thinking effort on/off/low/medium/high; built-in **Web Grounding + Code Interpreter + remote MCP**; multimodal text+image+video+speech; **pre-training + SFT + RFT (reinforcement fine-tuning)** customization; Nova Forge; **Nova 2.5 Sonic** speech-to-speech, real-time, async tool use, voice+text, up to 1M ctx; Nova 2 Sonic speech-to-speech; safe content filters + non-configurable child-safety + privacy; no arXiv technical report. 
- **主要创新点**：reasoning + **extended thinking** (low/med/high); long context 1M; agentic tools; **Nova Act**; **Nova Forge**; customization; safety; Nova Multimodal Embeddings; speech-to-speech. Not a published standalone technical report; AWS docs + service card.
- **arXiv/论文链接**：**非 arXiv**。[Amazon Nova](https://aws.amazon.com/nova/);[Nova models](https://aws.amazon.com/nova/models/);[Nova 2 getting started](https://docs.aws.amazon.com/nova/latest/nova2-userguide/getting-started-nova-2.html);[Nova 2 Lite blog](https://aws.amazon.com/blogs/aws/introducing-amazon-nova-2-lite-a-fast-cost-effective-reasoning-model/);[Nova 2.5 Sonic](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-nova-2.5-Sonic/);[Nova Act];[Nova Forge];[responsible AI service card](https://aws.amazon.com/ai/responsible-ai/resources/#service). 

### 15. Zhipu AI (GLM/ChatGLM)

- **中文标题**：GLM-5.4；GLM-5.3；GLM-5.3-Flash；GLM-5.2；GLM-5 技术报告
- **英文标题**：GLM-5.4; GLM-5.3; GLM-5.3-Flash; GLM-5.2; GLM-5 Technical Report; IndexShare
- **发布机构**：Zhipu AI（智谱；**Z.ai**；Shanghai；ChatGLM / GLM）
- **模型名称/系列**：**GLM-5.4**（latest flagship，**Loop Transformer**）；**GLM-5.3**；**GLM-5.3-Flash / FlashX**；**GLM-5.2**；**GLM-5.1**; **GLM-5**; **GLM-5.3-Flash**; ChatGLM; GLM-4.5/4.6/4.7; GLM-V; GLM-OCR; CogAgent. Z.ai 首页 “powered by GLM-5.3-Flash”; docs 列出 **GLM-5.4 New**。
- **发布日期**：**GLM-5.4** docs latest（available to GLM Coding Plan; Model API after security assessment）；GLM-5.3 **2026-11-12**（前序）/ docs; GLM-5.3-Flash; GLM-5.2 1M ctx; **GLM-5 technical report arXiv 2602.15763**; **IndexShare arXiv 2603.12201**; 本窗口核验 2026-11-27。
- **核心参数**：
  - **GLM-5.4**: **Loop Transformer**; **loops 28 layers of GLM-5 base for two iterations** (weight-shared); **continued training adaptation** (not from scratch); **gated progressive updates** (per-token gates; first pass conservative, second refine); optimized KV caching + sparse attention; intelligence **comparable to 2T–3T parameter models**; **1M context**; max output **128K**; input video/image/text/file; output text; thinking mode; “marathon thinking” limitation; base scale ~**750B** (“Architectural Modifications at 750B Scale”; GLM-5 base **744B/40B active**); no separate total param count for 5.4 yet; model API pending security assessment. 
  - **GLM-5.3**: **same base model as GLM-5.2**, all gains post-training; text-only; **1M ctx**; **128K output**; always-on reasoning; `reasoning_effort` low/high/max (default max); 50% coding gain on Z.ai Code Bench; emergent cyber; CyberGym SOTA; vulnerability exploitation >2×. 
  - **GLM-5.3-Flash**: **newly trained base**; **hybrid sparse + linear attention**; **mHC (Manifold-Constrained Hyper-Connections)**; **30T-token multimodal pre-training corpus**; multimodal; lower serving cost; `reasoning_effort`. 
  - **GLM-5.2**: 1M ctx; **IndexShare** (reuse same indexer across every four sparse attention layers; **2.9× per-token FLOPs reduction @1M**); improved **MTP** speculative decoding **+20% acceptance**. 
  - **GLM-5**: **744B total / 40B active** (vs GLM-4.5 355B/32B); **28.5T tokens** (vs 23T); **DSA (DeepSeek Sparse Attention)**; long-horizon agentic; long context; open-weights; GLM-5 technical report.
- **主要创新点**：
  - **大模型新架构**：**Loop Transformer / looped transformer**; weight-shared layers; **gated progressive updates**; **Universal Transformer** lineage; hybrid sparse+linear; **mHC**; **DSA**; **IndexShare**; **MTP**; **MoE**; GLM-5.3-Flash efficiency.
  - **训练方法**：GLM-5.3 pure post-training on GLM-5.2 base; **scaling post-training** (emergent cyber); GLM-5.4 continued training adaptation; RL/reasoning; “reasoning shifts into implicit loop depth”; multimodal pretraining 30T; **memory-intensive vs reasoning-intensive** distinction.
  - **Scaling Law/缩放分析**：**Loop scaling** (scale loop depth + model size in parallel; match larger models); GLM-5 scaling (355B→744B; 23T→28.5T); GLM-5.4 effective compute; GLM-5.3 post-training scaling; IndexShare FLOPs; mHC scaling.
  - **多模态**：GLM-5.4 multimodal in; GLM-5.3-Flash multimodal; GLM-5.3 text-only.
  - **长上下文**：1M; 128K output; 1M efficiency.
  - **推理模型**：always-on thinking; reasoning_effort; Loop deeper reasoning; agentic coding; long-horizon.
- **arXiv/论文链接**：[GLM-5.4 docs](https://docs.z.ai/guides/llm/glm-5.4);[GLM-5.3 docs](https://docs.z.ai/guides/llm/glm-5.3);[GLM-5.3 blog](https://z.ai/blog/glm-5.3);[GLM-5.3-Flash blog](https://z.ai/blog/glm-5.3-flash);[GitHub zai-org/GLM-5](https://github.com/zai-org/GLM-5);[GLM-5 technical report arXiv:2602.15763](https://arxiv.org/abs/2602.15763);[IndexShare arXiv:2603.12201](https://arxiv.org/abs/2603.12201);[Z.ai](https://z.ai);[docs.z.ai](https://docs.z.ai). **GLM-5.4 目前 docs 页面，未见独立 arXiv 技术报告；基座 GLM-5 技术报告 arXiv 已收录。**

### 16. InternLM (Shanghai AI Lab)

- **中文标题**：Sage S2.1 Flash Technical Report；Sage S2.1 Flash（科学多模态技术报告）
- **英文标题**：Sage S2.1 Flash Technical Report; Sage S2.1 Flash: A scientific multimodal model. Explore through reasoning. Verify through action.
- **发布机构**：**Shanghai AI Laboratory**（InternLM / 书生；OpenGVLab 合作）
- **模型名称/系列**：**InternLM Sage S2.1 Flash**（`Sage-S2.1-Flash`）；**Sage Sci-Perception / Sage-SciPerception**; **Intern-S1**; **InternVL**; InternLM3-8B-Instruct; InternLM2.5; InternLM-Math; **Intern-Decision**; XTuner/LMDeploy/OpenCompass/Lagent. 
- **发布日期**：**Sage S2.1 Flash 2026-11-16**（arXiv 2611.21072；repo updated 2026-11-17）；Intern-S1; InternLM3 2025-01; InternLM technical report arXiv 2403.17297 2024-03-17. 本窗口核验 2026-11-27。
- **核心参数**：**320-billion-parameter general-purpose MoE**; scientific multimodal; **Sage Sci-Perception** dedicated encoders for molecular graphs + biological sequences + spectra (ordered measurement patches); modality-specific projectors into shared backbone; **>10 scientific input types** (molecular graphs, crystals, protein sequences/3D structures...); text+images; tool use; **verifiable environments** (tool use, search, coding, ML experiments, scientific software; check execution results/state/artifacts); **33 benchmarks across seven domains**; **MIT** open weights; model downloads HF + ModelScope; `Sage-SciPerception`. 
- **主要创新点**：
  - **大模型新架构**：scientific multimodal MoE; **Sage SciPerception**; unified representation; shared backbone.
  - **训练方法**：**post-training in verifiable environments**; agentic scientific workflows; execution-result checking; tool use; 
  - **多模态**：scientific multimodal (bio/chem/spectra...).
  - **推理模型**：scientific evidence reasoning + action; multi-round verification; MLE-bench Lite; OSWorld-Verified; WebArena-Verified; DeepResearch Bench II; OfficeQA Pro; SpreadsheetBench 2; Harvey LAB.
  - **Scaling Law**：not explicitly.
- **arXiv/论文链接**：[Sage S2.1 Flash arXiv:2611.21072](https://arxiv.org/abs/2611.21072);[GitHub InternLM/Sage-S2.1-Flash](https://github.com/InternLM/Sage-S2.1-Flash);[HF internlm/Sage-SciPerception];[GitHub InternLM org](https://github.com/InternLM);[InternLM technical report arXiv:2403.17297];[Intern-S1];[InternVL]. 

### 17. Moonshot AI (Kimi)

- **中文标题**：Kimi K3.1 Pro（K3.1 系列首个模型）；Kimi K3 技术报告
- **英文标题**：Introducing Kimi K3.1 Pro; Kimi K3 Technical Report; Kimi K3
- **发布机构**：Moonshot AI（Kimi；月之暗面）
- **模型名称/系列**：**Kimi K3.1 Pro** / **Kimi K3.1 Pro Highspeed**; **Kimi K3.1** series; **Kimi K3**; Kimi K2.7 Code; Kimi K2.6; Kimi K2.5; Kimi K2; Kimi-Linear; Kimi-VL; Kimi-Audio. 
- **发布日期**：**Kimi K3.1 Pro 2026-10-24**；K3.1 weights by **Nov 4, 2026**; **Kimi K3** technical report + tech blog; API `kimi-k3.1-pro` / `kimi-k3.1-pro-highspeed`; K3 open-weight. 本窗口核验 2026-11-27。
- **核心参数**：
  - **K3.1 Pro**: **3T-class open-weight**; post-trained version of **Kimi K3** with substantially larger post-training compute; **1M-token context**; Highspeed 2–3× speed; reasoning effort 'max'; temperature 1.0 top-p 0.95 (eval note); full weights by Nov 4; hallucination reduction (claim-level 23.4%→8.3% on Kimi Hallu Bench Hard; etc.); **cyber capability data removal** for open-weight (mid-training + RL filtering); cyber retained-but-reduced. 
  - **Kimi K3**: **2.8T-parameter**; **open-weight**; **native multimodal (vision)**; **1M context**; **Kimi Delta Attention (KDA)** + **Attention Residuals (AttnRes)**; **Stable LatentMoE** activating **16 out of 896 experts**; **~2.5× scaling efficiency vs K2**; world's first open 3T-class; **full technical report `k3_tech_report.pdf`**; Kimi K3 license. 
- **主要创新点**：
  - **大模型新架构**：**KDA (Kimi Delta Attention, hybrid linear attention)** + **AttnRes**; **Stable LatentMoE**; sparse MoE scaling 16/896; native vision; long context; Kimi Linear.
  - **训练方法**：**large-scale joint RL across hundreds of downstream domains**; RL framework/long-context inference/efficiency/sandbox/rollout scheduling/environment-quality; **post-trained K3** K3.1; safety data removal; hallucination/factual accuracy; scaling post-training.
  - **Scaling Law/缩放分析**：MoE sparsity scaling; **~2.5× overall scaling efficiency vs K2**; K3→K3.1 post-training scaling; RL scaling; (K3 report).
  - **多模态**：native vision; 3D creation; documents; charts.
  - **长上下文**：1M.
  - **推理模型**：long-horizon coding; agentic; knowledge work; reasoning; factual accuracy; cyber (reduced for open-weight).
- **arXiv/论文链接**：**K3.1 Pro 技术博客非 arXiv**；K3 **[Full Report k3_tech_report.pdf](https://github.com/MoonshotAI/Kimi-K3/blob/main/k3_tech_report.pdf)** + [K3 tech blog](https://www.kimi.com/blog/kimi-k3);[Kimi K3.1 Pro tech blog](https://www.kimi.ai/blog/kimi-k3-1-pro);[GitHub MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3);[Kimi.ai research](https://www.kimi.ai). **K3.1 Pro 本身不另发 arXiv。**

### 18. StepFun（阶跃星辰）

- **中文标题**：Step 5 Preview；Inside Step 5 Preview: Architecture and Training for Agentic Work；Step 3.7 Flash
- **英文标题**：Step-5-Preview; Inside Step 5 Preview: Architecture and Training for Agentic Work; Step 3.7 Flash
- **发布机构**：StepFun（阶跃星辰）
- **模型名称/系列**：**Step 5 Preview**（`Step-5-Preview`；flagship agentic；Step 5）；**Step 3.7 Flash**；Step 3.5 Flash; Step-Code; Step1X-Edit; **SteptronOss**; Step Realtime. 
- **发布日期**：**Step 5 Preview repo updated 2026-11-09**；tech blog **Inside Step 5 Preview 2026-10-15**; model page www.stepfun.com/step-5-preview; HF FP8 + BF16 + ModelScope; API platform.stepfun.ai; Step 3.7 Flash. 本窗口核验 2026-11-27。
- **核心参数**：**Step 5 Preview: sparse MoE 600B total / 27B active**; **1M-token context**; text+image+video; **narrow-but-deep 92 transformer blocks**; **Gated Sliding Window Attention + sparse full-attention layers**; **Sparse GQA** full-attention path; sustained reasoning + tool use. **Step 3.7 Flash**: **198B MoE (196B LM + 1.8B vision encoder)**; ~11B active; **256K ctx**; ~400 tokens/s; 3 reasoning levels (low/med/high); vision-language; BF16/FP8/NVFP4/GGUF. 训练数据量未公开。 
- **主要创新点**：
  - **大模型新架构**：narrow-but-deep; **Gated Sliding Window Attention** + sparse full attention; **Sparse GQA**; MoE; numerical precision/gradient stability; (looped transformer research discussed but not adopted as flagship; note in blog) 
  - **训练方法**：**agent-native data construction** (agents synthesize under expert-defined principles + quality control); **RL for long rollouts**: training-inference mismatch, rollout efficiency, context management, **credit assignment**; implicit reasoning during prefill; multi-hop reasoning. 
  - **Scaling Law/缩放分析**：depth/multi-hop reasoning scaling; agentic scaling; not a standalone Scaling-Law paper. 
  - **多模态**：text+image+video; Step 3.7 VL.
  - **长上下文**：1M (Step 5); 256K (3.7 Flash); efficient long-context training/inference.
  - **推理模型**：agentic work; long tool-heavy trajectories; finance; knowledge work; coding.
- **arXiv/论文链接**：**非 arXiv.org**；[Step-5-Preview GitHub](https://github.com/stepfun-ai/Step-5-Preview);[tech blog platform.stepfun.ai/blog/inside-step-5-preview];[model page www.stepfun.com/step-5-preview];[HF stepfun-ai/Step-5-Preview];[docs platform.stepfun.ai];[Step 3.7 Flash GitHub + model page];[StepFun GitHub org]. **未找到 Step 5 arXiv technical report。**

### 19. ByteDance（豆包/Doubao）

- **中文标题**：Seed2.0 Model Card: Towards Intelligence Frontier for Real-World Complexity；Seed1.8 Model Card: Towards Generalized Real-World Agency；豆包（Doubao）Seed 系列
- **英文标题**：Seed2.0 Model Card: Towards Intelligence Frontier for Real-World Complexity; Seed1.8 Model Card: Towards Generalized Real-World Agency; SeedRealtime; Seedream 5.5; Seedance 2.5
- **发布机构**：ByteDance Seed（字节跳动；Doubao/豆包；ByteDance）
- **模型名称/系列**：**Seed2.0**; **Seed1.8**; **SeedRealtime**; **Seedream 5.5**; **Seedance 2.5**; **Seed Audio 1.0**; **Seed Edge**; Doubao; Seed 系列；**EdgeBench**（new scaling law）。豆包 consumer app；火山引擎/BytePlus。 
- **发布日期**：**Seed2.0 Model Card 2026-06-30** (arXiv 2607.00248); **Seed1.8 2026-03-21** (arXiv 2603.20633); SeedRealtime **2026-08-05**; Seedream 5.5 **2026-11-09**; Seedance 2.5 **2026-11-16**; Seed Audio 1.0 **2026-11**; 本窗口核验 2026-11-27。
- **核心参数**：Seed2.0 model series；not disclose total/active params in abstract；targets **long-tail knowledge** + **complex instruction following**; **world-leading reasoning intelligence, visual understanding, search**; real-world complex tasks; hundreds of millions users; evaluation-first (genuine needs → reliable benchmarks → realistic scenarios). Seed1.8 “Generalized Real-World Agency”. Seedream/Seedance 视觉模型参数未在本卡公开。训练数据量未公开。 
- **主要创新点**：
  - **训练方法**：**evaluation-first** (construct reliable forward-looking eval from real needs); target long-tail + instruction following; agentic real-world; 
  - **Scaling Law/缩放分析**：**EdgeBench: measuring real-world environment learning and discovering a new scaling law** (Seed site); Seed2.0 scaling; 
  - **多模态**：world-leading visual understanding; SeedRealtime omni-modal audio-visual full-duplex; Seedream/Seedance; 
  - **推理模型**：reasoning intelligence; long-horizon; complex instruction; 
  - **长上下文**：见 model card/官方（未在 abstract 公开，不臆造）.
- **arXiv/论文链接**：[Seed2.0 Model Card arXiv:2607.00248](https://arxiv.org/abs/2607.00248);[Seed1.8 arXiv:2603.20633];[Seed site seed.bytedance.com];[博客&论文];[SeedRealtime];[Seedream 5.5];[Seedance 2.5];[EdgeBench]. **豆包/Doubao 产品本身不另发 arXiv；LLM model card 以 Seed2.0 为最新。**

---

## 标记说明（honesty / 口径）

- **本窗口无新增一手技术报告**：Yi(01.AI)（最新仍为 Yi-Lightning 2024 + arXiv 2403.04652）、xAI Grok（无 Grok 4.7 arXiv；仅 Grok-1 开放权重）、Amazon Nova（AWS docs/service card）、Apple AFM 3（产品页；research 技术报告仍为 2025）、Microsoft FrogNano（HF 见 `microsoft/FrogNano-4B-2609`，无已验证 arXiv 技术报告）。以上如实标注，不臆造。
- **参数/训练数据未公开**：OpenAI GPT-6.2、Anthropic Fable/Mythos 5.2、Google Gemini 4、xAI Grok 4.7、Amazon Nova、Zhipu GLM-5.4、StepFun Step 5（训练数据）、Meta Muse（部分）、ByteDance Seed2.0（部分）等标注“未公开”。
- **arXiv 口径**：Mistral Large 4 技术报告在 **alphaXiv `2611.mistral-large-4`**，**非 arXiv.org**；GLM-5.4 **docs only**（基座 GLM-5 arXiv:2602.15763）；Kimi K3 **GitHub `k3_tech_report.pdf`**；Kimi K3.1 Pro **tech blog**；Google **model card**；OpenAI/Anthropic **system card**。用户要求“arXiv/论文链接”处，凡无 arXiv 给出官方报告链接并说明。
- **本窗口核验新增/纠正**：DeepSeek **DeepSeek-V4.1-Flash-1017**；Meta **Muse 家族**（含 Muse Ember 2026-11-09、Muse Wonder 2026-10-12、Muse Spark Open 2026-10-15；LLaMA 4 仍为最新 LLaMA 开放权重）；**Zhipu GLM-5.4**（Loop Transformer，此前速览只到 GLM-5.3）；**Amazon Nova 2.5 Sonic 2026-10**；**Kimi K3.1 Pro + K3 full report**；**Mistral Large 4 technical report 2026-11-03**；**NVIDIA Nemotron 3.5 Super 2026-11-17 + Bolt + Nemotron-Labs-Sigma/VisualCreation**；**Mistral total 1T/1050B**（此前 1.05T 口径纠正）；**Qwen4-Max 2.4T/71B**；**Baichuan-M3-235B arXiv 2602.06570**；**Phi-4-reasoning-vision-15B arXiv 2511.19663**；**InternLM Sage S2.1 Flash arXiv 2611.21072**；**Seed2.0 arXiv 2607.00248**。此前速览的部分口径（如 Kimi “3T-class” vs K3 2.8T；GLM-5.3 z.ai 抓取失败；Meta 抓取失败）已在本页按今日核验更新。
- **访问限制**：`websearch` 在本环境不可用；部分页面需 JS 渲染（z.ai blog、Alibaba Qwen HF 权重未公开、Baichuan 官网、Meta LLaMA gated HF、some AWS/Anthropic PDF via webfetch），已用 `curl`/原始 JSON/PDF 解析核验；无法访问项标注。无法确认即写“未确认/未公开”，不编造链接或数字。
- 指标均为厂商自报；本文不替读者独立复现；不构成任何投资建议。

## 参考链接索引

| 报告 | 链接 |
|---|---|
| DeepSeek V4.1 Flash tech report | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/DeepSeek_V41_Tech_Report.pdf |
| DeepSeek V4.1 Flash news | https://www.deepseek.com/news/deepseek-v4-1-flash/ |
| DeepSeek V4.1-Flash-1017 | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017 |
| DeepSeek-V4 arXiv | https://arxiv.org/abs/2606.19348 |
| OpenAI GPT-6.2 in ChatGPT system card | https://deploymentsafety.openai.com/gpt-6-2-chatgpt |
| OpenAI GPT-6.2 in ChatGPT PDF | https://deploymentsafety.openai.com/gpt-6-2-chatgpt/gpt-6-2-chatgpt.pdf |
| OpenAI GPT-6.2 Astra/Sol system card | https://deploymentsafety.openai.com/gpt-6-2-astra-sol |
| OpenAI GPT-6.2 Astra/Sol PDF | https://deploymentsafety.openai.com/gpt-6-2-astra-sol/gpt-6-2-astra-sol.pdf |
| OpenAI Deployment Safety Hub | https://deploymentsafety.openai.com |
| Meta Muse Ember | https://research.meta.ai/blog/muse-ember |
| Meta Muse Ember evaluation report | https://research.meta.ai/static/muse-ember-evaluation-report |
| Meta Muse Wonder | https://research.meta.ai/blog/muse-wonder |
| Meta Muse Wonder model card | https://research.meta.ai/static/muse-wonder-model-card |
| Meta Muse Spark Open | https://research.meta.ai/blog/muse-spark-open |
| Meta Muse Spark Open eval methodology | https://research.meta.ai/static/muse-spark-open-evaluation-methodology |
| Meta Muse Spark Open HF | https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B |
| Meta LLaMA | https://ai.meta.com/llama/ |
| Meta meta-llama HF | https://huggingface.co/meta-llama |
| Gemini 4 Neon | https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/ |
| Gemini 4 Neon model card PDF | https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Neon-Model-Card.pdf |
| Gemini 4 Hydrogen model card PDF | https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Hydrogen-Model-Card.pdf |
| Gemini 4 Carbon model card PDF | https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Carbon-Model-Card.pdf |
| Gemini 4 Argon model card PDF | https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Argon-Model-Card.pdf |
| Gemini 4 evals methodology | https://deepmind.google/models/evals-methodology/gemini-4-neon/ |
| Anthropic Claude Fable/Mythos 5.2 | https://www.anthropic.com/claude-fable-and-mythos-5-2 |
| Anthropic Fable 5.2/Mythos 5.2 system card | https://www.anthropic.com/document/claude-fable-5-2-mythos-5-2-system-card |
| Anthropic system card PDF | https://assets.claude.com/27d60918d218125e7504bc7354c4b4626ec56b11.pdf |
| Mistral Large 4 | https://mistral.ai/news/mistral-large-4/ |
| Mistral Large 4 Le Chonk weights | https://mistral.ai/news/mistral-large-4-oss/ |
| Mistral Large 4 technical report (alphaXiv) | https://www.alphaxiv.org/abs/2611.mistral-large-4 |
| Mistral Large 4 HF weights | https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B |
| Qwen4-Max | https://community.alibabacloud.com/blog/alibaba-unveils-qwen4-max-new-ai-teammate-for-work-creativity-and-discovery_603783 |
| Qwen research | https://qwen.ai/research |
| Yi: Open Foundation Models arXiv | https://arxiv.org/abs/2403.04652 |
| 01.AI | https://www.01.ai |
| Baichuan-M3-235B arXiv | https://arxiv.org/abs/2602.06570 |
| Baichuan-M3-235B GitHub | https://github.com/baichuan-inc/Baichuan-M3-235B |
| Baichuan-M2-32B arXiv | https://arxiv.org/abs/2509.02208 |
| Baichuan org | https://github.com/baichuan-inc |
| Phi-4-Reasoning-Vision-15B HF | https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B |
| Phi-4-Reasoning-Vision-15B technical report arXiv | https://arxiv.org/abs/2511.19663 |
| Phi-4-Reasoning-Vision MSR blog | https://www.microsoft.com/en-us/research/blog/phi-4-reasoning-vision-and-the-lessons-of-training-a-multimodal-reasoning-model/ |
| Apple Foundation Models Tech Report 2025 | https://machinelearning.apple.com/research/apple-foundation-models-tech-report-2025 |
| Apple AFM arXiv | https://arxiv.org/abs/2507.13575 |
| Apple Intelligence & Siri AI | https://www.apple.com/ai/ |
| NVIDIA Nemotron 3.5 Super arXiv | https://arxiv.org/abs/2611.22161 |
| NVIDIA Nemotron 3.5 Bolt arXiv | https://arxiv.org/abs/2611.20771 |
| NVIDIA Nemotron-Labs-Sigma arXiv | https://arxiv.org/abs/2610.02665 |
| NVIDIA nvidia HF | https://huggingface.co/nvidia |
| NVIDIA technical blog | https://developer.nvidia.com/blog |
| xAI Grok 4.7 | https://x.ai/news/grok-4-7 |
| Amazon Nova | https://aws.amazon.com/nova/ |
| Amazon Nova models | https://aws.amazon.com/nova/models/ |
| Amazon Nova 2 docs | https://docs.aws.amazon.com/nova/latest/nova2-userguide/getting-started-nova-2.html |
| Amazon Nova 2.5 Sonic | https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-nova-2.5-Sonic/ |
| Zhipu GLM-5.4 docs | https://docs.z.ai/guides/llm/glm-5.4 |
| Zhipu GLM-5.3 docs | https://docs.z.ai/guides/llm/glm-5.3 |
| Zhipu GLM-5.3-Flash blog | https://z.ai/blog/glm-5.3-flash |
| Zhipu GLM-5 repo | https://github.com/zai-org/GLM-5 |
| GLM-5 technical report arXiv | https://arxiv.org/abs/2602.15763 |
| IndexShare arXiv | https://arxiv.org/abs/2603.12201 |
| Z.ai | https://z.ai |
| InternLM Sage S2.1 Flash arXiv | https://arxiv.org/abs/2611.21072 |
| InternLM Sage-S2.1-Flash repo | https://github.com/InternLM/Sage-S2.1-Flash |
| InternLM org | https://github.com/InternLM |
| Kimi K3.1 Pro tech blog | https://www.kimi.ai/blog/kimi-k3-1-pro |
| Kimi K3 GitHub | https://github.com/MoonshotAI/Kimi-K3 |
| Kimi K3 full report PDF | https://github.com/MoonshotAI/Kimi-K3/blob/main/k3_tech_report.pdf |
| StepFun Step-5-Preview | https://github.com/stepfun-ai/Step-5-Preview |
| StepFun Inside Step 5 Preview | https://platform.stepfun.ai/blog/inside-step-5-preview |
| StepFun Step 3.7 Flash | https://github.com/stepfun-ai/Step-3.7-Flash |
| StepFun org | https://github.com/stepfun-ai |
| ByteDance Seed | https://seed.bytedance.com |
| Seed2.0 Model Card arXiv | https://arxiv.org/abs/2607.00248 |
| Seed1.8 Model Card arXiv | https://arxiv.org/abs/2603.20633 |

<!-- 核验时间 2026-11-27；本页为合成产物，未写入 raw/；仅新增本页并更新 wiki/index.md + wiki/log.md。 -->
