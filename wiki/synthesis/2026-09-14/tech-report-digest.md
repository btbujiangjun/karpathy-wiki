---
title: "LLM Tech Report Digest — 2026-09-14"
type: synthesis
created: 2026-09-14
updated: 2026-09-14
sources: []
tags: [tech-report, LLM, technical-report, system-card, arXiv, model-card, moe, reasoning, long-context, multimodal, hybrid-architecture, agentic, open-source, kv-cache, daily-digest]
---

# LLM Tech Report Digest — 2026-09-14

> 全球主要 AI 公司大模型技术报告速览（截至 2026-09-14）
> 本篇聚焦自 2026-09-13 摘要后的新增项（★ = 新收录；⭐ = 相对历史摘要的 catch-up，此前未被本 wiki 收录）
> 本日主线：**KV 缓存压缩极限之战（DeepSeek-V4.1-Flash 技术报告：890 bytes/token）** + **Flash 档模型卡密集补位（Gemini 3.8 Flash + Cyber 双卡）** + **紧凑端开放权重追补（Muse Glimmer / Intern-S2-Mobius / GLM-5.3）**

---

## 1. DeepSeek — DeepSeek-AI

### 1.1 DeepSeek-V4.1-Flash 技术报告（★ NEW — 本日头条）
- **中文标题**: DeepSeek-V4.1-Flash：将 KV 缓存压缩推向极限
- **英文标题**: DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression
- **发布机构**: DeepSeek-AI
- **模型名称**: DeepSeek-V4.1-Flash（MoE，552B backbone + 196B Engram 条件记忆，合计 763B）
- **发布日期**: 2026-09-10（DeepSeek 官网 Blog + HuggingFace / ModelScope 仓库）
- **核心参数**:
  - **CED（Causal Encoder-Decoder）架构**: 40 层 = 20 层因果编码器 + 20 层解码器；decoder 的全局 KV 由 encoder 末层 hidden states 投影而来 → **prefill 仅激活 8B / decode 激活 16B**（对 input-heavy agentic 负载成本友好）
  - **CSA2（Compressed Sparse Attention 2）**: 每层静态分配三种模式之一 —— **Full / Reindex / Reuse**（跨层共享主 KV 与索引 K、复用 Top-K 稀疏注意力索引）；decoder 用 **Hierarchical Sparse Indexer** 将深层索引限制在首个 Full Mode 层构建的候选池内
  - **SWA Bounded Replay**: 只重放最近 n_win tokens 重建缺失的 SWA KV 状态，避免持久化至 SSD → 持久 KV 足迹降至 V4-Flash 的 ~1/8
  - **FP4 主 KV 缓存（E2M1 格式，每 16 通道一个 E4M3 scale）** → 全局 KV 足迹 **890 bytes/token ≈ V4-Flash 的 1/4**
  - MoE 每层 **1 shared + 384 routed experts，6 个 routed 激活/token**；Single-Pass mHC（残差流混合重构）；DSpark 投机解码（semi-autoregressive draft + confidence-scheduled verification）
  - 多模态: 从头训练的 **DeepSeek-ViT**（2D-RoPE + 3×3 pixel-unshuffle 下采样）+ 2 层 MLP projector，图像与文本自 tokenizer 起联合处理
- **训练**: 原生多模态语料 **45T tokens** 从头预训练；稀疏注意力以 64K 序列长度训练，**34T tokens 处扩展到 1M 上下文**；后训练采用标准 **SFT → RL → on-policy distillation (OPD)**，创新集中于数据管线（大规模自动合成 agent 任务与环境，数据/任务/rollout 渐进扩展）
- **关键基准（技术报告 vs 前沿）**: Terminal-Bench 2.1 **90.6**（Opus-5.0 89.1 / GPT-5.6 Sol 88.8）、DeepSWE v1.1 **74.2**、Codeforces **3471**、Terminal-Bench 3.0 30.0、GPQA-Diamond 90.9、MathArena Apex 65.6
- **生态/状态**:
  - 许可 **MIT**；已上线 DeepSeek API（模型名 `deepseek-flash`），V4-Flash / V4-Flash-Vision-Exp 退役并临时路由至 V4.1-Flash
  - `deepseek-v4-pro` 自 **2026-09-14 12:00（北京时间）** 起临时路由至 V4.1-Flash 并按 Flash 价格计价，直至 V4.1-Pro 正式上线（延续 09-13 摘要，当天已生效）
  - 第三方（Ollama cloud）计价参照: $0.15–0.30/M input、$0.60–1.20/M output，1M context，763B 参数
- **链接**: [HF 模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) / [技术报告 PDF](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/resolve/main/DeepSeek_V41_Tech_Report.pdf) / [DeepSeek 官方 Blog](https://www.deepseek.com/en/news/deepseek-v4-1-flash) / [ModelScope](https://www.modelscope.cn/models/deepseek-ai/DeepSeek-V4.1-Flash) / [Ollama](https://ollama.com/library/deepseek-v4.1-flash:cloud)

### 1.2 DeepSeek-V4 家族（参照）
- DeepSeek-V4 Tech Report: [arXiv:2606.19348](https://arxiv.org/abs/2606.19348)（2026-04，"Towards Highly Efficient Million-Token Context Intelligence"）；V4-Pro 1.6T（49B active）、V4-Flash 284B（13B active）
- 意义: V4.1-Flash 用 CED+CSA2 在 8B/16B active 下达到超越 V4-Pro 的 benchmark 表现，标志 DeepSeek 从"参数稀疏"转向"结构稀疏 + KV 压缩"双线

---

## 2. OpenAI

### 2.1 GPT-6 Astra System Card（参照）
- 2026-09-03 发布 / 09-06 + 09-09 更新；首个 Preparedness Framework Critical 网络安全级模型
- **补充细节**: HealthBench Professional **length-adjusted 63.4**（系统卡官方口径）；context 1,050,000 / max output 128,000
- 本窗口无新增技术/系统卡；GPT-6 Astra 面向企业（Microsoft Foundry 等）GA 推进中
- 链接: [deploymentsafety.openai.com](https://deploymentsafety.openai.com/gpt-6-astra)

---

## 3. Anthropic — Claude

### 3.1 Claude Fable 5.1 & Mythos 5.1 System Card（参照，无新增）
- 2026-09-01；CB-1 化学/生物能力；Mythos 5.1 网络安全评估最强
- **状态**: 截至 2026-09-14 **Fable 5.2 仍未发布**（社区传闻 9 月中旬，未验证）；无新增系统卡

---

## 4. Meta AI — LLaMA / Muse

### 4.1 Muse Glimmer（⭐ NEW — catch-up，Meta Superintelligence Labs 首个开放模型）
- **中文标题**: Muse Glimmer：面向本地 Agent 工作流的开放权重模型
- **英文标题**: Muse Glimmer — An Open Agentic Model for Local Workflows (Meta Superintelligence Labs)
- **发布机构**: Meta Superintelligence Labs（Alexandr Wang 牵头；该部门首个开源模型，呼应 Zuckerberg"开放超级智能"路线）
- **模型名称**: Muse Glimmer（muse-glimmer-30b；dense 多模态）
- **发布日期**: **2026-08-10**（Meta Blog / HF / NVIDIA NIM / Ollama 多源一致）
- **核心参数**: **29.6B dense** 因果 Transformer（52 层文本 backbone，GQA 32 query / 2 KV heads，滑动+全注意力交替）+ **1.8B ViT-G/14 感知编码器**（50 层 vision tower）；vocab 202,048；默认 **128K** 上下文（可更长）；**Apache 2.0**；文本+图像输入、文本输出（原生 tool calling + 独立 reasoning 输出）
- **主要创新点**:
  - 从 **Muse Spark distillation** 而来（三阶段：logit distillation → agent-heavy mid-training → SFT + OPD + RL），定位为 Spark 的紧凑端侧弟弟，**不满足 Meta 自身 "Frontier AI" 定义**
  - 可控推理强度 **low / medium / high / xhigh** 四档
  - 专为 **always-on 本地 agent** 设计：单张消费级 GPU / 笔记本可跑（~4-bit 权重 <20GB，免云免联网）；Ollama MLX 引擎 + DFlash 在 Apple Silicon 上 1.5–1.8× 加速；支持 Claude Code / Codex / Pi / OpenClaw 等 harness
- **关键基准（模型卡）**: MCP Atlas **75.5**（vs Qwen3.6-27B 62.5 / Gemma 4 31B 54.2）、DeepSearch QA 74.6、**SWE-Bench Verified 76.0**、AIME 2026 **94.7**、OSWorld-Verified 65.9、Terminal-Bench 2.1 51.7、GPQA Diamond 83.5、MMMU Pro 74、HLE 22.0
- **链接**: [Meta Blog](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) / [HF meta-models/Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) / [dev.meta.ai](https://dev.meta.ai/docs/muse-glimmer) / [NVIDIA NIM](https://build.nvidia.com/meta/muse-glimmer-30b) / [Ollama Blog](https://ollama.com/blog/muse-glimmer)
- ⚠️ 说明: 2026-08-10 发布，此前 digest 未收录，今日补录（catch-up）

### 4.2 Muse Spark 1.3 / Safety & Preparedness Report（参照）
- Muse Spark 1.3（09-02, agentic & coding）与 Muse Spark Safety & Preparedness Report（2606.12429）均已收录于 09-12/09-13 摘要

---

## 5. Google DeepMind — Gemini

### 5.1 Gemini 3.8 Flash Model Card（★ NEW）
- **中文标题**: Gemini 3.8 Flash 模型卡
- **英文标题**: Gemini 3.8 Flash — Model Card (Google DeepMind)
- **发布机构**: Google DeepMind
- **模型名称**: Gemini 3.8 Flash（`gemini-3.8-flash`，GA；上一代 3.7 Flash 于 2026-08 发布，**六周内第三款 Flash 迭代**）
- **发布日期**: 2026-09-02（GA + 模型卡）
- **核心参数**: 上下文 **1,048,576**；最大输出 **65,536**；thinking 等级 **LOW / MEDIUM（默认）/ HIGH**（MINIMAL 不被支持）；输入 text/image/audio/video/PDF；知识截止 2026-03（部分域 2025-01，与 Gemini 3 家族一致）
- **主要提升**:
  - 相较 3.7 Flash，软件工程与 **长程 agentic / document-heavy 知识工作流**的大幅进步：Glean 实证称完成任务数 **3×+**（"completing more than three times as many tasks"）
  - 定价: **$0.75/M input、$3.75/M output**（Flash 档）
  - 更高 effort 档位会消费更多 token 以提性能，代价可控
- **关键基准（模型卡/评测页面）**: HLE-Verified **54.9%**；Terminal-Bench 2.1 90.8%（3.7 Flash 81.6%）；SWE-Bench Pro 61.6%；SWE-Atlas 51.9%；DeepSWE v1.1 73.7%；Vals Finance Agent V2 / Harvey Legal Agent 排前
- **安全**: 与 3.7 Flash 整体持平——Text-to-Text safety −0.4pp、Multilingual safety +5.4pp、Tone +0.2pp、unjustified refusals +1.1pp（非英语语言安全略降）
- **链接**: [模型卡](https://deepmind.google/models/model-cards/gemini-3-8-flash) / [产品页](https://deepmind.google/models/gemini/flash) / [API Docs](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash) / [Blog](http://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash)
- ⚠️ 更正: 09-13 摘要中 "Gemini 3.6 Flash（09-02 产品更新）" 实际应为 **Gemini 3.8 Flash**

### 5.2 Gemini 3.8 Flash Cyber Model Card（★ NEW）
- **定位**: 3.8 Flash 的网络安全专用变体（agentic cyber defense），与 3.8 Flash 同日（09-02）发布；接入 **Fairwind Program**（面向政府/企业的主动网络防御生态）并受限访问
- **要点（模型卡）**: 内部漏洞检测在 20+ 编程语言上 >70% 检出率；**CWE-Bench 47.2% pass@1**；Chrome 安全团队实测正确补丁产出 **2.6×**（相对既有工作流）
- **链接**: [Cyber 模型卡](https://deepmind.google/models/model-cards/gemini-3-8-flash-cyber) / [Fairwind 介绍](https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/) / [Blog](http://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash)
- ⚠️ 注: 上述 benchmark 数值以模型卡公开内容为准（部分为第三方转述）

### 5.3 Gemini 4 泄露线索 / Gemma 4（参照）
- Gemini 4（2026-10 发布传闻、3.5 Pro 搁置，low confidence）与 Gemma 4 Tech Report（2607.02770）均已收录于 09-12/09-13 摘要

---

## 6. Microsoft — Phi

### 6.1 Phi 系列（参照，无新增）
- Phi-4-reasoning-vision-15B 已收录；Phi-5 pre-release 阶段，正式技术报告未发布；Phi-Ground 仓库存在（grounding 模型线）但无新报告

---

## 7. Mistral AI

### 7.1 Mistral Small 4（参照，无新增）
- 已收录于 09-13 摘要（2026-03-16, 119B-A6B, 128e/4active, 256K, Apache 2.0, Magistral+Pixtral+Devstral 三合一）

---

## 8. Alibaba — Qwen

### 8.1 Qwen3.8-27B（参照，补充架构细节）
- 已收录于 09-13 摘要（09-02，Apache 2.0，vision-language）
- **架构补强**: 27B dense **混合注意力**——64 层中 **16 层 Gated Attention + 48 层 Gated DeltaNet**；原生 **262,144** 上下文（可经 YaRN 扩至 1M）；thinking 模式默认开启；与 09-12 摘要的 Qwen3.8-Flash-Next（125B-A6B 侧）互补
- Qwen3.8-2.4T-A95B（前 Qwen3-Max）为 custom license，非 Apache 2.0

---

## 9. xAI — Grok

### 9.1 Grok 4.7 持续跳票（★ 更新 — 仍未发布）
- **动态**: 截至 **2026-09-14 仍无 Grok 4.7 发布**；docs.x.ai 公开模型档位最高为 **grok-4.6**；马斯克 09-11 称还需 "a few more days" RL tuning（原 09-12 目标已三次落空）
- **参数传闻**: ~2.1T（较 Grok 4.6 的 1.5T 提升 ~40%，第三方报道，未验证）
- **状态**: 无 Grok 4.7 模型卡/系统卡；RL 延迟归因（response-length 惩罚过激 + 自我校验不足，Data Studios 分析）见 09-13 摘要
- 链接: [cryptobriefing](https://www.cryptobriefing.com/xai-delays-grok-4-7-release/) / [Data Studios](https://www.datastudios.org/post/xai-grok-4-7-delay-reinforcement-learning-self-checking)

---

## 10. NVIDIA — Nemotron

### 10.1 Nemotron 3.5 Lightning Model Card（★ 补强 — 模型卡细节补全）
- **中文标题**: Nemotron 3.5 Lightning 模型卡：面向长程 Agent 的混合架构推理模型
- **英文标题**: NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4 (Model Card)
- **发布机构**: NVIDIA
- **发布日期**: 2026-08-11（HF / Build.NVIDIA.com）
- **核心参数**:
  - **30B 总 / 3B active**；架构 = **Hybrid MoE：Mamba-2 + MoE + Attention 交错** + **MTP（Multi-Token Prediction）**；52 层 / hidden 2688；**128 routed experts（top-6）+ 1 shared**
  - 上下文 **最高 1M**；支持 EN+代码 + 西/法/德/意/日
  - **模型日期 2025-12 ~ 2026-05**；预训练数据截止 2025-09，后训练数据截止 2026-05
  - BF16 + **NVFP4** 双 checkpoint；DSpark / DFlash draft 模型（speculative decoding）
- **训练（recipe 公开）**: pretraining → SFT（12+ 数据源）→ **GRPO RL（multi-environment rewards）** → NVFP4 PTQ + Quantization-Aware Distillation（Model Optimizer）
- **关键基准**: MMLU Pro 81.94（BF16）/ 81.62（NVFP4）；GPQA-D 75.44/75.57；SciCode 32.60/31.38；HLE 11.72/10.47
- **定位**: always-on agents 执行层（OpenClaw / Hermes Agent + NemoClaw 安全栈）；宣称 **4× 吞吐、30% 更低任务完成时间** vs 同级开源
- **许可**: **OpenMDW-1.1**（权重+数据+recipes）；**无独立技术报告**——release blog + 模型卡 + recipe 即权威参考
- **链接**: [HF NVFP4](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4) / [NVIDIA NIM](https://build.nvidia.com/nvidia/nemotron-3.5-lightning-30b-a3b) / [Training Recipe](https://docs.nvidia.com/nemotron/nightly/nemotron/lightning35/README.html) / [Megatron Bridge](https://docs.nvidia.com/nemo/megatron-bridge/nightly/models/nemotron/nemotron3.5-lightning.html)

### 10.2 Nemotron 4 传闻（参照，低置信度）
- 2026-08-11 前后 Nemotron 4 在研（~1T）传闻；无官方报告（tentative）

---

## 11. Moonshot AI — Kimi

### 11.1 Kimi K3（参照，无新增）
- 已收录于 09-13 摘要（2.8T-A104B，KDA+AttnRes+Stable LatentMoE 16/896，1M ctx，arXiv:2607.24653 v2 2026-08-07）

---

## 12. Amazon — Nova

### 12.1 Amazon Nova 2 Technical Report & Model Card（★ NEW — 报告捕获 catch-up）
- **中文标题**: Amazon Nova 2：多模态推理与生成模型 — 技术报告与模型卡
- **英文标题**: Amazon Nova 2: Multimodal Reasoning and Generation Models — Technical Report and Model Card
- **发布机构**: Amazon AGI（Amazon Artificial General Intelligence）
- **模型名称**: Nova 2 家族四款（**Nova 2 Lite / Nova 2 Pro / Nova 2 Omni** 及一款实时对话语音模型）
- **发布日期**: 2025-12-02 Nova 2 Omni preview（AWS "What's New"）→ 完整技术报告与模型卡于 Amazon Science 出版（2026 年窗口捕获）
- **核心参数/创新点**:
  - **Lite / Pro**: 原生多模态（text/doc/image/video）+ 可配置 **"extended thinking"**（dynamic reasoning，按任务平衡 accuracy/speed/cost）
  - **Nova 2 Lite** 在 **~1/7 成本、最高 5× 更快**下超越前代旗舰 **Nova Premier**；在 multimodal perception / core reasoning / agentic benchmark 上匹配或超越 **GPT-5 Mini 与 Gemini 2.5 Flash**；RealKIE-FCC Verified 62.1%
  - **Nova 2 Omni**: **首个统一多模态推理模型** —— 输入 text/doc/image/video/**audio**，同时**生成 text 与 images**（reasoning + image generation/editing 双输出）；1M context、200+ 语言文本 / 10 语言语音；speech 评测 MLS WER 4.7（GPT-4o-transcribe 5.4 / Gemini 2.5 Flash 6.9）、CoVoST 2 BLEU 40.7、MMAU 81.8
  - 训练思路: 多模态全栈原生（vision encoder + 统一 model），面向 RAG / agentic / 企业多模态检索场景
- **生态动态**: **Nova Premier 已于 2026-09-14 EOL**（09-13 摘要），主力为 Nova 2 Omni（KTLO）；re:Invent 预期新前沿模型（第三方预期，未验证）
- **链接**: [技术报告 PDF](https://cdn.amazon.science/c5/3d/84514a224666b5be6de4b43ef4aa/nova-2-0-technical-report2.pdf) / [AWS 公告（Omni preview 2025-12-02）](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-nova-2-omni-preview) / [Nova Premier TR & Model Card](https://www.amazon.science/publications/amazon-nova-premier-technical-report-and-model-card)

---

## 13. Apple — Apple Intelligence Foundation Models

### 13.1 AFM 3 系列（参照，无新增）
- AFM 3（2026-06-08, 5 模型含 20B sparse on-device）；截至 **2026-09-14 年度技术报告仍未发布**（官方曾承诺 "later this summer"）

---

## 14. ByteDance — Seed / 豆包

### 14.1 Seed / Doubao（参照，无新增）
- Seed2.0 Model Card（2607.00248）与 Seed1.5-VL 已收录；本窗口无新报告

---

## 15. 智谱 AI — GLM

### 15.1 GLM-5.3 正式版（⭐ NEW — catch-up，此前摘要仅覆盖 Flash 线）
- **中文标题**: GLM-5.3：开源编程 / 智能体 / 网络安全前沿
- **英文标题**: Zhipu GLM-5.3（Z.AI / 智谱）
- **发布机构**: 智谱 AI（Z.AI）
- **发布/开源时间**: **2026-08-14 发布** → 08-19 API 正式上线（定价与 GLM-5.2 持平）→ 权重约两周后（~08-28）开源
- **核心参数**: 与 GLM-5.2 **相同基座**（总参数媒体口径 **743 0亿 / 753 0亿 不一致 —— 已 flag**）；纯**后训练 Scaling**（IndexShare + SAO + 迭代 Slime 训练框架）突破性能上限；**1M 上下文**（官方称真正可用）；reasoning 常开（`reasoning_effort`: low / high / max，默认 max）；`clear_thinking` 参数控制多轮思考透传
- **主要创新点**:
  - **编程/agentic**: 内部体感评测较 5.2 提升 **50%**；**Terminal-Bench 3.0 28.3（开源第一，超 Kimi K3）**、DeepSWE 1.1 66.9、Agents' Last Exam (CLI) 开源第一；编码/agent 能力接近 Claude Fable 5
  - **网络安全**: **CyberGym 84.5%**（>Mythos 5 83.8%、GPT-5.6 Sol 83.6%）；发布前两周联合安全团队发现 **2,404 个潜在漏洞（1,088 中高危）**，含潜伏 40 余年的 **DNS 协议级风险**（单请求可将服务器压力放大近 8 万倍，影响 >1,000 万公网 DNS）
  - **Token 效率**: High 档 31.4% 准确率 vs Claude Opus 4.8 最高档 29.5%，平均 ~5 万 tokens/任务 vs ~12 万 tokens
  - **"开源的盾"计划**: 对重点开源项目持续安全审计 + 免费模型额度（呼应 HuggingFace 入侵取证事件后黄仁勋"开放安全 AI"表态）
  - 许可: **GLM-5.3 License**（Z.AI；年收入 >$100 亿的 Model-as-a-Service 需过安全审查）
- **链接**: [HF zai-org/GLM-5.3](https://huggingface.co/zai-org/GLM-5.3)（+README/LICENSE）/ [中国基金报](https://www.chnfund.com/article/ARb52abd64-07c6-779f-577e-3a23111ee473) / [腾讯新闻](https://news.qq.com/rain/a/20260814A0BCAQ00) / [证券时报](https://www.stcn.com/article/detail/4075550.html)
- ⚠️ 说明: GLM-5.2 / GLM-5.3-Flash 已收录于 09-12 摘要，正式版 5.3 此前未收录，今日补录（catch-up）；⚠️ 总参数口径 7430 亿 vs 7530 亿不一致

---

## 16. InternLM / 上海 AI Lab

### 16.1 Intern-S2-Mobius（★ NEW）
- **中文标题**: Intern-S2-Mobius：知识-推理解耦的基础模型
- **英文标题**: Intern-S2-Mobius: Foundation Model with Decoupled Knowledge and Reasoning
- **发布机构**: 上海 AI Laboratory (InternLM)
- **模型名称**: Intern-S2-Mobius（35B，Mobius-v0 架构，Xtuner + LMDeploy 实现）
- **发布日期**: 2026-08-14（arXiv:2608.14290）；HF / GitHub 已发布（BF16）
- **核心参数**: 35B；从 **Qwen3.5-35B continual-pretraining** + SFT + RL；Apache 2.0
- **主要创新点（Mobius-v0）**:
  - **知识-推理解耦**: 把传统"按层绑定"的 FFN 知识存储改为**全局共享 Memory（FFN）+ 多个 Reasoners（Self-Attn）迭代查询/细化**隐藏状态
  - **Backward Residual Connection**: 浅层/深层推理阶段可跨层访问共享知识（超越局部层信息流）
  - **Dynamic Latent Reasoning**: 解码前以循环潜在迭代在**高密度连续状态**中内化 deliberation / refinement / multi-token prediction，降低对长可见 CoT 的依赖
  - **~4× 端到端推理加速**（相对 Qwen3.5-35B 基线，得分相当或更高、推理 trace 显著更短）
  - 可扩展性: 7B from-scratch 用基线 **62.6% 训练数据**取得相近下游分数
  - 科学任务大增益: Biology-Instructions / Mol-Instructions / MolecularIQ
- **链接**: [HF internlm/Intern-S2-Mobius](https://huggingface.co/internlm/Intern-S2-Mobius) / [GitHub](https://github.com/InternLM/Intern-S2-Mobius)（含 [Technical Report PDF](https://github.com/InternLM/Intern-S2-Mobius/blob/main/Technical_Report_Intern_S2_Mobius.pdf)）/ [arXiv:2608.14290](https://arxiv.org/abs/2608.14290)

### 16.2 Intern-S2-Preview-397B（参照，已收录于 09-12 摘要）
- 旗舰科学多模态模型（Memory Decoder，long-horizon agents）；BF16/FP8 权重，HF/ModelScope；35B 版本 arXiv:2608.13505

---

## 17. StepFun — 阶跃星辰

### 17.1 Step 系列（参照，无新增）
- Step-3.7-Flash（198B-A11B）/ Step3-VL-10B / Step AOS / STEPX Neo AI 手机已收录于 09-12/09-13 摘要；本窗口无新报告

---

## 18. 01.AI — Yi

### 18.1 Yi 系列（参照，无新增）
- 截至 2026-09-14 无 2026 年新 Yi 技术报告；最新综合报告 Yi-Lightning 2024-12

---

## 19. Baichuan

### 19.1 Baichuan 系列（参照，无新增）
- Baichuan-M3 已收录于 09-12 摘要（HealthBench-Hard 44.4 超 GPT-5.2）；本窗口无新报告

---

## 本日头条与动态（相对 2026-09-13 摘要的 Delta）

### 1. 技术报告集中补位：KV 压缩极限 + Flash 双卡 + Nova 2 报告
| 新增项 | 要点 | 类型 |
|--------|------|------|
| DeepSeek-V4.1-Flash 技术报告（★） | 890 bytes/token KV（V4-Flash 的 1/4、持久 KV 1/8）；CED 8B/16B active；CSA2 三模式；FP4 E2M1；DSpark；45T tokens；Terminal-Bench 2.1 90.6 | 技术报告 |
| Gemini 3.8 Flash + 3.8 Flash Cyber（★） | 六周内第三款 Flash；HLE-Verified 54.9%；长程 agentic 任务 3×+；Cyber 变体 CWE-Bench 47.2%、Fairwind 生态 | 模型卡 |
| Amazon Nova 2 技术报告（★） | Lite 以 1/7 成本超 Nova Premier；Omni 首个统一多模态（text+image 双输出、audio 输入） | 技术报告+模型卡 |

### 2. 紧凑端开放权重追补（今日 catch-up 主线）
| 模型 | 规模 | 定位/亮点 |
|------|------|----------|
| Meta Muse Glimmer（⭐） | 29.6B dense + 1.8B ViT | 本地 agent 工作流、Muse Spark 蒸馏、MCP Atlas 75.5、Apache 2.0 |
| InternLM Intern-S2-Mobius（★） | 35B | 知识-推理解耦（Memory+Reasoners）、~4× 推理加速、科学任务 |
| 智谱 GLM-5.3（⭐） | ~740–750B base | 纯后训练、Terminal-Bench 3.0 28.3 开源第一、CyberGym 84.5%、"开源的盾" |

### 3. 跳票 / 在研持续项
- **Grok 4.7**: 09-14 仍无发布（目标一再后移，RL tuning 中）
- **Anthropic Fable 5.2**: 9 月中旬传闻，未发布（low confidence）
- **Apple AFM 3 年度技术报告**: 持续爽约（promised "later this summer"）
- Open/在研: DeepSeek V4.1-Pro（发布待定）、Gemini 4（10 月传闻）、Nemotron 4（1T 传闻）、Phi-5（pre-release）

### 4. 今日新增/更新汇总（★ 共 8 项，含 2 项 catch-up）
| 公司 | 新增项 | 日期 | 类型 |
|------|--------|------|------|
| DeepSeek | V4.1-Flash 技术报告 ★ | 2026-09-10 | 技术报告 |
| Google | Gemini 3.8 Flash + Cyber 模型卡 ★ | 2026-09-02 | 双模型卡 |
| Amazon | Nova 2 技术报告+模型卡 ★ | 2025-12-02 起 | 技术报告 |
| NVIDIA | Nemotron 3.5 Lightning 模型卡细节补全 ★ | 2026-08-11 | 模型卡 |
| Meta | Muse Glimmer ⭐ catch-up | 2026-08-10 | 模型卡/开放权重 |
| 智谱 | GLM-5.3 正式版 ⭐ catch-up | 2026-08-14 | 模型卡/开放权重 |
| InternLM | Intern-S2-Mobius ★ | 2026-08-14 | 技术报告/开放权重 |
| xAI | Grok 4.7 跳票更新 | 2026-09-14 | 动态 |

### 5. 未发布新正式报告的公司
- OpenAI（GPT-6 Astra 系统卡 09-03，无技术报告）、Anthropic、Apple、ByteDance、Microsoft、Moonshot、Qwen、Mistral、StepFun、01.AI、Baichuan

---

## 交叉主题分析

### 1. KV 缓存成为新一代效率战场（本日主线）
- **DeepSeek V4.1-Flash** 把 KV 压缩推到新刻度: FP4 (E2M1) 主 KV + CSA2 跨层复用 + SWA Bounded Replay → **890 bytes/token、持久 KV 1/8**；其核心论点正是"cache-hit 费用占 agent 成本大头，压缩缓存直接降账单价"
- 与 09-12/09-13 摘要的 FP4 生态（Kimi K3 MXFP4 QAT、Nemotron NVFP4、Mistral NVFP4 checkpoint）呼应: **FP4 从权重量化走向 KV/激活全程量化**
- 呼应 arXiv 侧 KV 压缩/复用论文（C²KV、TwinKV、RoofLang "compact KV-cache design" 等）→ 该方向仍是推理系统研究热点

### 2. Flash / 工作机级模型迭代加剧
| 模型 | Active/总 | 效率卖点 |
|------|----------|---------|
| DeepSeek V4.1-Flash | 8B prefill / 16B decode（763B） | CED 结构稀疏 + FP4 KV |
| Gemini 3.8 Flash | 未公开 | 六周三款 Flash，长程 agentic 3×+ |
| Nemotron 3.5 Lightning | 3B / 30B | Mamba-2+MoE 混合，always-on agent |

### 3. 紧凑开放权重（sub-40B）密集发力
- **Muse Glimmer（29.6B dense）**: 影子蒸馏版"端侧 Muse"，单消费卡本地 agent
- **Intern-S2-Mobius（35B）**: 架构级创新（知识-推理解耦）挑战"推理必须长 CoT"
- 与 Qwen3.8-27B（dense hybrid attention）、GLM-5.3-Flash 拼成 2026Q3"紧凑智能"阵容；共性: 更短推理轨迹 + 更高吞吐

### 4. 后训练 / 数据管线成为能力分水岭
- GLM-5.3: 基座不变、纯后训练 Scaling（IndexShare + SAO + Slime）
- DeepSeek V4.1-Flash: SFT→RL→OPD，创新全在 agent 任务/环境数据合成管线
- Nemotron 3.5 Lightning: GRPO multi-environment RL + NVFP4 QAD recipe 全公开
- Muse Glimmer: 蒸馏 + agent-heavy mid-training + OPD
- 结论: 基础架构红利趋于收敛，**"后训练数据工程"成为开源阵营拉开差距的主战场**

### 5. 网络安全成为差异化叙事的新前线
- Gemini 3.8 Flash **Cyber** 变体 + Fairwind Program（Google, 09-02）
- GLM-5.3 CyberGym 84.5% + "开源的盾"（智谱, 08-14）
- GPT-6 Astra 首个 Preparedness Framework **Critical**（OpenAI, 09-03）
- 呼应黄仁勋"网络安全能力必须更开放"与 HuggingFace 入侵取证事件（GLM-5.2 本地分析 1.7 万条日志）→ 安全正从"评测指标"变成"营销+产品主线"