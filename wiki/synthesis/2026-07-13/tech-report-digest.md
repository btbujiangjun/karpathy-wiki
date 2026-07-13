---
title: "2026年7月 AI 大模型技术报告速览"
type: synthesis
created: 2026-07-13
updated: 2026-07-13
sources: [web-search]
tags: [tech-report, llm, moe, reasoning, multimodal, scaling-law]
---

# 2026年7月 AI 大模型技术报告速览

> 本汇总覆盖截至2026年7月的主要科技公司AI模型技术报告，聚焦 MoE/Mamba/hybrid架构、pre/post-training/alignment/RL、Scaling Law、多模态、长上下文、reasoning models 等方向。

---

## 1. DeepSeek

### DeepSeek-V3
- **中文标题**: DeepSeek-V3 技术报告
- **英文标题**: DeepSeek-V3 Technical Report
- **发布机构**: DeepSeek（深度求索）
- **模型名称**: DeepSeek-V3
- **发布日期**: 2025-01
- **核心参数**: 671B 总参数，37B 激活参数（MoE架构）
- **主要创新点**:
  - Multi-head Latent Attention (MLA) 实现高效推理
  - DeepSeekMoE 架构 + 无辅助损失负载平衡策略
  - 多 token 预测训练目标
  - FP8 混合精度训练，DualPipe 流水线并行
  - 14.8T token 预训练，总训练成本仅 $5.576M
- **链接**: [arXiv:2412.19437](https://arxiv.org/pdf/2412.19437)

### DeepSeek-R1
- **中文标题**: 通过强化学习激励LLM推理能力
- **英文标题**: DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
- **发布机构**: DeepSeek
- **模型名称**: DeepSeek-R1 / DeepSeek-R1-Zero
- **发布日期**: 2025-01-20
- **核心参数**: 671B（R1），6个蒸馏版本（1.5B-70B）
- **主要创新点**:
  - R1-Zero: 纯大规模RL训练（无SFT），自然涌现推理行为
  - R1: 多阶段训练 + cold-start data + RL
  - 性能对标 OpenAI o1-1217
  - 开源蒸馏模型（基于Qwen和Llama）
- **链接**: [arXiv:2501.12948](https://arxiv.org/abs/2501.12948)

---

## 2. OpenAI

### GPT-5
- **中文标题**: GPT-5 System Card
- **英文标题**: GPT-5 System Card
- **发布机构**: OpenAI
- **模型名称**: GPT-5 (main, thinking, mini, nano, pro)
- **发布日期**: 2025-07
- **核心参数**: 未公开
- **主要创新点**:
  - 统一了 thinking 和 main 模型（不再是 o3 + GPT-5 分离）
  - gpt-5-thinking-pro 使用并行 test-time compute
  - 多模态输入支持
  - 安全评估框架覆盖 malicious use 和 loss of control
- **链接**: [OpenAI System Card](https://openai.com)

### GPT-5.5
- **中文标题**: GPT-5.5 System Card
- **英文标题**: GPT-5.5 System Card
- **发布机构**: OpenAI
- **模型名称**: GPT-5.5, GPT-5.5 Mini, GPT-5.5 Nano, GPT-5.5 Pro, GPT-5.5 Chat
- **发布日期**: 2026-04-23
- **核心参数**: 未公开
- **主要创新点**:
  - 5个模型变体覆盖不同规模和用途
  - GPT-5.5 Pro 使用并行 test-time compute
  - 多模态输入支持
  - 安全评估框架包含 malicious use 和 loss of control 两个维度
- **链接**: [OpenAI System Card](https://openai.com)

---

## 3. Meta AI

### LLaMA 4
- **中文标题**: LLaMA 4 技术报告
- **英文标题**: The Llama 4 herd of models
- **发布机构**: Meta AI
- **模型名称**: LLaMA 4（Scout, Maverick等）
- **发布日期**: 2025-04
- **核心参数**: Scout: 109B 总参/17B激活; Maverick: 400B 总参/17B激活
- **主要创新点**:
  - 首次采用 MoE 架构（混合专家）
  - Scout 支持 10M token 超长上下文
  - 早期融合（early fusion）原生多模态训练
  - iRoPE 位置编码实现超长上下文
- **链接**: [Meta AI Blog](https://ai.meta.com)

---

## 4. Google DeepMind

### Gemini 2.5 Pro
- **中文标题**: Gemini 2.5 Pro 技术报告
- **英文标题**: Gemini 2.5 Pro Technical Report
- **发布机构**: Google DeepMind
- **模型名称**: Gemini 2.5 Pro
- **发布日期**: 2025-03
- **核心参数**: 未公开（MoE架构）
- **主要创新点**:
  - 原生多模态（文本、图像、音频、视频）
  - 1M token 上下文窗口
  - 强大的推理和编码能力
  - "thinking" 模式提升复杂任务表现
  - Deep Think 模式实现 GPQA 86.4%
  - TPUv5p 训练
- **链接**: [Google AI Blog](https://ai.google)

### Gemini 2.5 Flash
- **中文标题**: Gemini 2.5 Flash 技术报告
- **英文标题**: Gemini 2.5 Flash Technical Report
- **发布机构**: Google DeepMind
- **模型名称**: Gemini 2.5 Flash
- **发布日期**: 2025-06
- **核心参数**: 未公开（MoE架构）
- **主要创新点**:
  - 轻量级 thinking 模型
  - 速度和效率优化
  - 保持 strong performance 的同时降低成本
- **链接**: [Google AI Blog](https://ai.google)

---

## 5. Anthropic

### Claude Opus 4
- **中文标题**: Claude Opus 4 模型卡
- **英文标题**: Claude Opus 4 Model Card
- **发布机构**: Anthropic
- **模型名称**: Claude Opus 4
- **发布日期**: 2025-05
- **核心参数**: 未公开
- **主要创新点**:
  - Hybrid reasoning model，支持 extended thinking
  - ASL-3 安全等级
  - SWE-bench 72.5%
  - 编码和推理任务领先
- **链接**: [Anthropic](https://www.anthropic.com)

### Claude Sonnet 4
- **中文标题**: Claude Sonnet 4 模型卡
- **英文标题**: Claude Sonnet 4 Model Card
- **发布机构**: Anthropic
- **模型名称**: Claude Sonnet 4
- **发布日期**: 2025-05
- **核心参数**: 未公开
- **主要创新点**:
  - Hybrid reasoning model，支持 extended thinking
  - ASL-2 安全等级
  - 平衡性能和成本
- **链接**: [Anthropic](https://www.anthropic.com)

### Claude 4.5 Sonnet
- **中文标题**: Claude 4.5 Sonnet 模型卡
- **英文标题**: Claude 4.5 Sonnet Model Card
- **发布机构**: Anthropic
- **模型名称**: Claude 4.5 Sonnet
- **发布日期**: 2025-02
- **核心参数**: 未公开
- **主要创新点**:
  - 首次使用 "Model Spec" 进行行为规范
  - 引入 "computer use" 能力
  - SWE-bench 达 49.0%
  - 改进的长上下文处理
- **链接**: [Anthropic](https://www.anthropic.com)

---

## 6. Mistral AI

### Mistral Large 2
- **中文标题**: Mistral Large 2 技术报告
- **英文标题**: Mistral Large 2
- **发布机构**: Mistral AI
- **模型名称**: Mistral Large 2
- **发布日期**: 2025-07-24
- **核心参数**: 123B 参数
- **主要创新点**:
  - 支持 128K token 上下文
  - 多语言能力显著提升（支持80+语言）
  - 函数调用和JSON输出能力强
  - 在非英语语言任务上领先开源模型
- **链接**: [Mistral AI](https://mistral.ai)

### Magistral (Reasoning Model)
- **中文标题**: Mistral Magistral 推理模型
- **英文标题**: Mistral Magistral Reasoning Model
- **发布机构**: Mistral AI
- **模型名称**: Magistral
- **发布日期**: 2025-2026
- **核心参数**: 未公开
- **主要创新点**:
  - MoE 架构
  - Sliding window attention
  - 推理能力优化
- **链接**: [Mistral AI](https://mistral.ai)

### Devstral
- **中文标题**: Devstral 代码模型
- **英文标题**: Devstral Code Model
- **发布机构**: Mistral AI
- **模型名称**: Devstral
- **发布日期**: 2025
- **核心参数**: 未公开
- **主要创新点**:
  - 专为 agentic coding 优化
  - 支持多语言编程
  - 工具使用能力强
- **链接**: [Mistral AI](https://mistral.ai)

---

## 7. Qwen (通义千问)

### Qwen3
- **中文标题**: Qwen3 技术报告
- **英文标题**: Qwen3 Technical Report
- **发布机构**: 阿里云通义实验室
- **模型名称**: Qwen3-0.6B 到 Qwen3-235B-A22B
- **发布日期**: 2025-04
- **核心参数**: 0.6B - 235B（MoE，22B激活）
- **主要创新点**:
  - Hybrid Thinking Mode：支持思考/非思考模式切换
  - 119种语言和方言支持
  - 36T token 预训练（是Qwen2.5的2.5倍）
  - 支持100+编程语言
  - 工具调用、MCP协议支持
- **链接**: [Qwen Blog](https://qwenlm.github.io)

### Qwen2.5-VL
- **中文标题**: Qwen2.5-VL 视觉语言模型技术报告
- **英文标题**: Qwen2.5-VL Technical Report
- **发布机构**: 阿里云通义实验室
- **模型名称**: Qwen2.5-VL-3B/7B/72B
- **发布日期**: 2025-01
- **核心参数**: 3B / 7B / 72B
- **主要创新点**:
  - 动态分辨率处理（任意宽高比图像）
  - 多分辨率视频理解
  - 支持视频帧输入
  - 强大的OCR和文档理解能力
- **链接**: [Qwen Blog](https://qwenlm.github.io)

---

## 8. 01.AI (零一万物)

### Yi-Lightning
- **中文标题**: Yi-Lightning 技术报告
- **英文标题**: Yi-Lightning Technical Report
- **发布机构**: 01.AI（零一万物）
- **模型名称**: Yi-Lightning
- **发布日期**: 2024-10
- **核心参数**: 千亿参数 MoE 模型
- **主要创新点**:
  - Chatbot Arena 排名世界第六，中国第一
  - 在中文、数学、编码、困难提示等专项排名2-4位
  - 增强的 MoE 架构
  - 25页技术报告详细记录架构、训练流程和安全栈
- **链接**: [arXiv:2412.01253](https://huggingface.co/papers/2412.01253)

---

## 9. Baichuan (百川智能)

### Baichuan-M3
- **中文标题**: Baichuan-M3 医疗增强大模型
- **英文标题**: Baichuan-M3 Medical-Enhanced LLM
- **发布机构**: 百川智能
- **模型名称**: Baichuan-M3
- **发布日期**: 2026-01-13
- **核心参数**: 235B 参数
- **主要创新点**:
  - HealthBench + HealthBench Hard 双榜第一
  - 超越 OpenAI GPT-5.2 医疗能力
  - 医疗幻觉率降至3.5%，全球最低
  - "严肃问诊范式" + SCAN原则
  - SPAR算法解决长对话RL训练问题
  - 联合150+一线医生构建 SCAN-bench 评测
- **链接**: [百川官网](https://www.baichuan-ai.com)

### Baichuan-M4
- **中文标题**: Baichuan-M4 新一代医疗大模型
- **英文标题**: Baichuan-M4 Next-Gen Medical LLM
- **发布机构**: 百川智能
- **模型名称**: Baichuan-M4
- **发布日期**: 2026-05（预告）
- **核心参数**: 未公开
- **主要创新点**:
  - HealthBench + HealthBench Hard + HealthBench Professional 三榜第一
  - 超越 GPT-5.5、Opus 4.7、DeepSeek-V4-Pro
  - 事实性感知强化学习算法
  - 裸模型事实性幻觉率降至3.3%
- **链接**: [钛媒体报道](https://www.tmtpost.com/8002395.html)

---

## 10. Microsoft

### Phi-4
- **中文标题**: Phi-4 技术报告
- **英文标题**: Phi-4 Technical Report
- **发布机构**: Microsoft Research
- **模型名称**: Phi-4
- **发布日期**: 2024-12
- **核心参数**: 14B 参数
- **主要创新点**:
  - 14B参数规模，聚焦合成数据
  - 在STEM任务上超越 GPT-4
  - 高效的小规模模型训练方法论
  - 证明合成数据在小模型训练中的价值
- **链接**: [Microsoft Research](https://www.microsoft.com/en-us/research)

### Phi-4-Reasoning-Vision-15B
- **中文标题**: Phi-4-Reasoning-Vision-15B 多模态推理模型
- **英文标题**: Phi-4-Reasoning-Vision-15B Multimodal Reasoning Model
- **发布机构**: Microsoft Research
- **模型名称**: Phi-4-Reasoning-Vision-15B
- **发布日期**: 2026-03
- **核心参数**: 15B 参数
- **主要创新点**:
  - 多模态推理能力
  - 开源 open-weight
  - 视觉+语言联合推理
  - 推理任务表现优异
- **链接**: [arXiv:2603.03975](https://arxiv.org/abs/2603.03975)

---

## 11. Apple

### Foundation Models (On-device + Server)
- **中文标题**: Apple 基础模型技术报告
- **英文标题**: Apple Foundation Models Technical Report
- **发布机构**: Apple
- **模型名称**: Apple Foundation Models (on-device + server)
- **发布日期**: 2025-12
- **核心参数**: 未公开（on-device约3B）
- **主要创新点**:
  - 设备端+服务器协同架构
  - MoE 架构（服务器端）
  - LoRA adapters 实现个性化定制
  - 多语言支持
  - 强调隐私保护的端侧部署
- **链接**: [Apple Machine Learning Research](https://machinelearning.apple.com)

---

## 12. NVIDIA

### Nemotron 3 Ultra
- **中文标题**: Nemotron 3 Ultra 技术报告
- **英文标题**: Nemotron 3 Ultra Technical Report
- **发布机构**: NVIDIA
- **模型名称**: Nemotron 3 Ultra
- **发布日期**: 2026-06-10
- **核心参数**: MoE hybrid，128 expert groups
- **主要创新点**:
  - MoE hybrid 架构
  - 128个专家组 + cross-expert attention gates
  - 约20T token 训练
  - 跨专家注意力门控机制
  - 优化的企业级推理性能
- **链接**: [NVIDIA Blog](https://developer.nvidia.com)

---

## 13. xAI

### Grok 4
- **中文标题**: Grok 4 模型卡
- **英文标题**: Grok 4 Model Card
- **发布机构**: xAI
- **模型名称**: Grok 4
- **发布日期**: 2025-07-09
- **核心参数**: 未公开（推测MoE架构）
- **主要创新点**:
  - 在 Colossus 200K GPU 集群上进行大规模RL训练
  - RL计算效率提升6倍
  - 原生工具使用（代码解释器+网页浏览）
  - HLE (Humanity's Last Exam) 满分
  - 真实时间搜索集成
- **链接**: [xAI Blog](https://x.ai)

---

## 14. Amazon

### Amazon Nova
- **中文标题**: Amazon Nova 基础模型技术报告
- **英文标题**: Amazon Nova Foundation Models
- **发布机构**: Amazon Web Services
- **模型名称**: Nova Pro, Nova Lite, Nova Micro, Nova Canvas, Nova Reel
- **发布日期**: 2024-12
- **核心参数**: 未公开
- **主要创新点**:
  - Pro: 多模态理解旗舰模型
  - Lite: 低成本多模态模型
  - Micro: 纯文本高效模型
  - Canvas: 图像生成
  - Reel: 视频生成
  - 全栈生成式AI能力覆盖
- **链接**: [AWS Blog](https://aws.amazon.com)

---

## 15. Zhipu AI (智谱AI)

### GLM-5
- **中文标题**: GLM-5 技术报告
- **英文标题**: GLM-5 Technical Report
- **发布机构**: 智谱AI（Zhipu AI）
- **模型名称**: GLM-5
- **发布日期**: 2026-02
- **核心参数**: 744B MoE
- **主要创新点**:
  - DSA (Dynamic Sparse Attention) 架构
  - async Agent RL 训练
  - 200K token 上下文
  - 代码和推理任务大幅提升
- **链接**: [智谱AI](https://www.zhipuai.cn)

### GLM-4.7
- **中文标题**: GLM-4.7 技术报告
- **英文标题**: GLM-4.7 Technical Report
- **发布机构**: 智谱AI（Zhipu AI）
- **模型名称**: GLM-4.7
- **发布日期**: 2025-12
- **核心参数**: 358B MoE
- **主要创新点**:
  - Interleaved/persistent thinking 架构
  - 交替思考和生成
  - 多模态能力
- **链接**: [智谱AI](https://www.zhipuai.cn)

### GLM-4 / ChatGLM
- **中文标题**: GLM-4 技术报告
- **英文标题**: GLM-4 Technical Report
- **发布机构**: 智谱AI（Zhipu AI）
- **模型名称**: GLM-4 / ChatGLM
- **发布日期**: 2024-01
- **核心参数**: 未公开
- **主要创新点**:
  - 128K token 上下文窗口
  - 多模态能力（文生图、代码解释器）
  - 联网搜索功能
  - 10T tokens 预训练数据
  - 在多个基准上超越 GPT-4
- **链接**: [智谱AI](https://www.zhipuai.cn)

---

## 16. InternLM (书生·浦语)

### InternLM3
- **中文标题**: InternLM3 技术报告
- **英文标题**: InternLM3 Technical Report
- **发布机构**: 上海人工智能实验室
- **模型名称**: InternLM3-8B-Instruct
- **发布日期**: 2025-01-15
- **核心参数**: 8B 参数
- **主要创新点**:
  - 仅4T高质量token训练，节省75%+训练成本
  - 性能超越 Llama3.1-8B 和 Qwen2.5-7B
  - 支持深度思考模式（长链推理）
  - 支持普通响应模式
  - 在推理和知识密集任务上SOTA
- **链接**: [GitHub](https://github.com/InternLM/InternLM)

### Intern-S1
- **中文标题**: Intern-S1 科学多模态模型
- **英文标题**: Intern-S1 Scientific Multimodal Model
- **发布机构**: 上海人工智能实验室
- **模型名称**: Intern-S1
- **发布日期**: 2025-2026
- **核心参数**: 未公开
- **主要创新点**:
  - 科学领域多模态理解
  - OpenCompass 评测
  - 科学推理能力
- **链接**: [GitHub](https://github.com/InternLM/InternLM)

---

## 17. Moonshot AI (月之暗面)

### Kimi K2
- **中文标题**: Kimi K2 技术报告
- **英文标题**: Kimi K2 Technical Report
- **发布机构**: Moonshot AI（月之暗面）
- **模型名称**: Kimi K2
- **发布日期**: 2025-07
- **核心参数**: 1T 总参数，32B 激活参数（MoE）
- **主要创新点**:
  - 128×128 MoE 网格架构
  - 196K token 上下文窗口
  - 多模态理解能力
  - 在编码和推理任务上表现突出
  - MoE架构实现高效推理
- **链接**: [Moonshot AI](https://www.moonshot.ai)

### Kimi K2.5
- **中文标题**: Kimi K2.5 技术报告
- **英文标题**: Kimi K2.5 Technical Report
- **发布机构**: Moonshot AI（月之暗面）
- **模型名称**: Kimi K2.5
- **发布日期**: 2025-2026
- **核心参数**: 未公开
- **主要创新点**:
  - 高能力云端模型
  - 多模态能力
  - 推理优化
- **链接**: [Moonshot AI](https://www.moonshot.ai)

---

## 18. StepFun (阶跃星辰)

### Step 3
- **中文标题**: Step 3 技术报告
- **英文标题**: Step 3 Technical Report
- **发布机构**: 阶跃星辰（StepFun）
- **模型名称**: Step 3
- **发布日期**: 2025-07
- **核心参数**: 321B 总参数，38B 激活参数（MoE）
- **主要创新点**:
  - 原生多模态推理
  - 开源 Apache 2.0
  - MoE 架构实现高效推理
- **链接**: [StepFun Blog](https://static.stepfun.com)

### Step 3.7 Flash
- **中文标题**: Step 3.7 Flash 技术报告
- **英文标题**: Step 3.7 Flash Technical Report
- **发布机构**: 阶跃星辰（StepFun）
- **模型名称**: Step 3.7 Flash
- **发布日期**: 2026-05-29
- **核心参数**: 196B 总参数 + 1.8B ViT（约198B），11B 激活参数
- **主要创新点**:
  - 稀疏 MoE 架构，256K token 上下文
  - 最高400 Tokens/秒推理速度
  - 原生多模态理解（图像+视频）
  - 联网与视觉搜索增强
  - Advisor Mode：达到 Claude Opus 4.6 编码性能的97%，成本仅1/9
  - SWE-Bench Pro 56.26%
  - 开源协议：Apache 2.0
- **链接**: [StepFun Blog](https://static.stepfun.com/blog/step-3.7-flash/)

---

## 19. ByteDance (字节跳动)

### 豆包 2.0 (Doubao 2.0)
- **中文标题**: 豆包 2.0 大模型技术报告
- **英文标题**: Doubao 2.0 Technical Report
- **发布机构**: 字节跳动（ByteDance）
- **模型名称**: 豆包 2.0 (Pro/Lite/Mini) + Code 模型
- **发布日期**: 2026-02
- **核心参数**: 1T 参数
- **主要创新点**:
  - 1T 参数规模
  - Pro/Lite/Mini + Code 模型变体
  - 多模态 Agent 能力
  - 强大的代码生成能力
- **链接**: [字节跳动研究](https://research.bytedance.com)

### Seedream 2.0
- **中文标题**: Seedream 2.0 双语图像生成模型
- **英文标题**: Seedream 2.0 Bilingual Image Generation
- **发布机构**: 字节跳动（ByteDance）
- **模型名称**: Seedream 2.0
- **发布日期**: 2025
- **核心参数**: 未公开
- **主要创新点**:
  - 双语（中英文）图像生成
  - 高质量图像合成能力
  - 多语言文本渲染
- **链接**: [字节跳动研究](https://research.bytedance.com)

---

## 横向对比

| 公司 | 模型 | 架构 | 参数规模 | 上下文 | 关键特点 |
|------|------|------|----------|--------|----------|
| DeepSeek | V3 | MoE | 671B/37B active | 128K | 极低训练成本$5.6M |
| OpenAI | GPT-5 | 未知 | 未公开 | 未公开 | 统一thinking+main模型 |
| Meta | LLaMA 4 | MoE | Scout 109B/17B active | 10M | 超长上下文 |
| Google | Gemini 2.5 Pro | MoE | 未公开 | 1M | Deep Think, GPQA 86.4% |
| Anthropic | Opus 4 | 未知 | 未公开 | 200K | Hybrid reasoning, ASL-3 |
| Mistral | Large 2 | Dense | 123B | 128K | 多语言80+ |
| Qwen | Qwen3 | MoE | 235B/22B active | 128K | Hybrid Thinking |
| 01.AI | Yi-Lightning | MoE | 千亿级 | 未公开 | Chatbot Arena #6 |
| Baichuan | M3/M4 | 未知 | 235B (M3) | 未公开 | 医疗专用，幻觉率3.3% |
| Microsoft | Phi-4-RV | Dense | 15B | 未公开 | 多模态推理, open-weight |
| Apple | Foundation | MoE | ~3B(on-device) | 未公开 | 端侧隐私 |
| NVIDIA | Nemotron 3 Ultra | MoE hybrid | 未公开 | 未公开 | 128 expert groups |
| xAI | Grok 4 | MoE | 未公开 | 256K | Colossus 200K GPU |
| Amazon | Nova | 未知 | 未公开 | 未公开 | 全栈生成式AI |
| Zhipu | GLM-5 | MoE | 744B | 200K | DSA架构, async Agent RL |
| InternLM | InternLM3 | Dense | 8B | 未公开 | 低成本高效训练 |
| Moonshot | Kimi K2 | MoE | 1T/32B active | 196K | MoE网格架构 |
| StepFun | Step 3 | MoE | 321B/38B active | 256K | 原生多模态推理, 开源 |
| ByteDance | 豆包 2.0 | 未知 | 1T | 未公开 | 多模态Agent, Code模型 |

---

## 关键趋势总结

### 1. MoE 架构成为主流
几乎所有主要厂商（DeepSeek、Meta、Qwen、01.AI、NVIDIA、xAI、Moonshot、StepFun、Apple、Zhipu GLM-5）都在使用或转向 MoE 架构。MoE 通过稀疏激活实现了在保持强大能力的同时降低推理成本。

### 2. Reasoning 模型标配化
GPT-5 thinking、Claude Opus 4 extended thinking、Gemini 2.5 Deep Think、Mistral Magistral、StepFun Step 3 等 reasoning models 已成为标配。RL 驱动的推理能力提升是当前最重要的技术方向之一。

### 3. 长上下文竞赛升级
从128K到1M再到10M token，上下文窗口不断扩展。Meta LLaMA 4 Scout 支持10M token，Google Gemini 2.5 Pro 支持1M，GLM-5 支持200K，这使得处理超长文档和代码库成为可能。

### 4. 中国AI实验室 MoE + Reasoning 重投入
GLM-5 (744B MoE)、Step 3 (321B MoE)、Doubao 2.0 (1T)、Kimi K2 (1T MoE) 展示了中国AI实验室在 MoE + reasoning 方向的大规模投入。

### 5. 多模态成为标配
几乎所有新模型都支持多模态输入（文本+图像+视频），部分模型支持音频。多模态能力已成为大模型的基本要求。

### 6. Agent 和工具使用成为标配
Grok 4 的多代理架构、StepFun 的 Advisor Mode、Qwen3 的 MCP 协议支持、GLM-5 的 async Agent RL 都表明，模型原生的工具使用和代理能力正在成为核心竞争力。

### 7. 端侧部署受重视
Apple 的端侧模型、Phi-4 的小规模高效训练、InternLM3 的低成本方案都显示，在追求大模型能力的同时，如何在端侧高效部署同样重要。

### 8. 训练成本优化
DeepSeek-V3 以$5.576M完成训练，InternLM3 仅用4T token节省75%成本，Phi-4 聚焦合成数据——如何更高效地训练模型是持续的研究热点。
