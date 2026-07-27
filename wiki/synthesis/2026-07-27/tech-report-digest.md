---
title: LLM Tech Report Daily (2026-07-27)
type: synthesis
created: 2026-07-27
updated: 2026-07-27
tags: [tech-report, moe, hybrid-attention, reasoning, multimodal, long-context, daily-digest]
---

# LLM Tech Report Daily — 2026-07-27

**Date**: 2026-07-27
**Scope**: 19 major AI companies' latest technical reports and model releases
**Search period**: July 2026 (focusing on Jul 18-27, 2026)

---

## Executive Summary

Major developments this cycle: DeepSeek V4 GA released (1.6T/49B MoE, CSA+HCA attention, MIT license), Meta LLaMA 4 Scout/Maverick/Behemoth family with 10M context on Scout, Google Gemini 3.6 Flash with 17% token savings, Moonshot Kimi K3 2.8T params (subscription pause due to demand), Zhipu GLM-5.2 744B with MIT license, xAI Grok 4.5 $2/$6 pricing, and Anthropic Claude voice mode + AMD $5B deal. Pricing wars intensify as open-weight models collapse closed model margins.

---

## Company Updates

### DeepSeek

| Model | Params | Released | License | Key Innovation |
|-------|--------|----------|---------|----------------|
| DeepSeek-V4 | 1.6T total / 49B active | 2026-04-26 | MIT | CSA+HCA hybrid attention, 1M context, manifold learning |

- **DeepSeek-V4**: 1.6 trillion parameters, 49 billion active via MoE. Hybrid CSA+HCA attention mechanism. 1M context window. Manifold learning approach. arXiv: 2606.19348. GA released April 2026, open-weight MIT license.
- **DeepSeek-V3**: 671B total / 37B active, 14.8T tokens. Established baseline.
- **DeepSeek-R1**: Reasoning model, arXiv: 2501.12948. Foundation for reasoning capabilities.
- Training data: 14.8T tokens.

### OpenAI

| Model | Type | Released | Notes |
|-------|------|----------|-------|
| GPT-5.6 | Flagship | 2026-07-09 | System Card released |
| GPT-5.5 Ultra | Flagship | 2026-04 | - |
| GPT-5.5 Pro | Reasoning | 2026-04 | Enhanced reasoning |
| o3 | Reasoning | 2025 | - |
| o4-mini | Reasoning | 2025 | - |

- **GPT-5.6**: Latest flagship model. System Card released. "Sol" variant demonstrated autonomous hackathon capability. Autonomy level significantly increased.
- **GPT-5**: arXiv: 2601.03267. Core technical reference.
- **Pricing**: Competing on value with autonomous agent capabilities.

### Meta AI (Llama)

| Model | Params | Active | Experts | Context | Released |
|-------|--------|--------|---------|---------|----------|
| Llama 4 Behemoth | 288B | 400B (MoE) | - | 10M | 2026-06-09 |
| Llama 4 Maverick | - | - | 16/128 | - | 2025-04-05 |
| Llama 4 Scout | - | - | 16/128 | 10M | 2025-04-05 |

- **Llama 4 Scout**: 10M context window, 16 active / 128 total experts MoE. 400M+ downloads.
- **Llama 4 Maverick**: 128 experts, 17B active parameters. Dense + MoE variants.
- **Llama 4 Behemoth**: 288B total, 400B MoE. Largest open model.
- Training data: 400M+ downloads reported.
- **Key innovation**: 10M context on Scout is industry-leading for open models.

### Google DeepMind

| Model | Type | Released | Key Metric |
|-------|------|----------|------------|
| Gemini 2.5 Pro | Flagship | 2025-06 | - |
| Gemini 2.5 Flash | Efficient | 2025-06 | - |
| Gemini 3.6 Flash | Efficient | 2026-07-21 | 17% tokens saved |

- **Gemini 2.5 Pro/Flash**: Thinking models. 1M context. Multimodal native. Agentic capabilities.
- **Gemini 3.6 Flash**: Latest efficient model. 17% token savings vs previous generation.
- **Gemini 3.5 Flash-Lite + Flash Cyber**: Additional variants for specialized use cases.
- Training data: 1M context capability demonstrated.

### Anthropic

| Model | Type | Released | Safety |
|-------|------|----------|--------|
| Claude Fable 5 | Flagship | 2026-06-09 | System Card |
| Mythos 5 | Next-gen | 2026-06-09 | System Card |

- **Claude Fable 5**: Latest flagship. System Card with RSP evaluations. Safety-focused release.
- **Mythos 5**: Next-generation model, also with System Card.
- **Voice mode**: Claude now supports voice interaction.
- **AMD deal**: $5B partnership for inference infrastructure.
- **Safety approach**: Responsible Scaling Policy (RSP) evaluations, comprehensive System Cards.

### Mistral AI

| Model | Params | Type | Released |
|-------|--------|------|----------|
| Ministral 3 (various) | 3B/8B/14B | Dense | 2026-01-13 |
| Magistral Medium | - | Reasoning | 2026-06 |

- **Ministral 3**: 3B, 8B, 14B dense models. Cascade Distillation approach. Apache 2.0 license.
- **Magistral Medium**: First reasoning model from Mistral. Pure RL training.
- **Microsoft deal**: Multibillion Europe partnership.
- Pixtral: Vision model variant.

### Qwen (Alibaba)

| Model | Params | Type | Released |
|-------|--------|------|----------|
| Qwen3-235B-A22B | 235B | MoE | 2025-05-14 |
| Qwen 3.8 Max | 2.4T | Dense | 2026-07 |

- **Qwen3**: 0.6B to 235B, dense + MoE variants. Thinking/non-thinking unified approach. 119 languages supported.
- **Qwen 3.8 Max Preview**: 2.4 trillion parameters. Latest flagship.
- Training data: 119 languages, diverse multilingual corpus.
- arXiv: 2505.09388.

### Microsoft / Phi

| Model | Params | Type | Released |
|-------|--------|------|----------|
| Phi-4-reasoning-vision-15B | 15B | Dense | 2026-03 |

- **Phi-4-reasoning-vision-15B**: Compact multimodal reasoning model. Dynamic-resolution encoders.
- Demonstrates strong reasoning at small scale.
- arXiv: 2603.03975.

### xAI (Grok)

| Model | Params | Released | Pricing |
|-------|--------|----------|---------|
| Grok 4 | - | 2026-07 | - |
| Grok 4.5 | - | 2026-07 | $2/$6 |
| Grok 4.20 | - | 2026-04-07 | - |

- **Grok 4.5**: Latest model. $2/$6 pricing strategy.
- **Grok 4.20**: Multi-agent architecture. Dual mode SA/MA (single-agent/multi-agent). System Card released.
- **Grok 3**: 1.2T params, 128 experts, 13.4T training tokens. Baseline reference.
- **Pricing**: Aggressive pricing to compete with open-weight models.

### Apple

| Model | Params | Type | Released |
|-------|--------|------|----------|
| Apple Intelligence Foundation Models | ~3B | On-device | 2025 |

- **On-device**: ~3B parameter model for Apple Intelligence.
- **Server**: PT-MoE (Parallel Transfer MoE) for cloud inference.
- **2-bit quantization**: Aggressive quantization for on-device deployment.
- **Privacy focus**: On-device processing prioritized.
- arXiv: 2507.13575.

### NVIDIA

| Model | Params | Type | Released |
|-------|--------|------|----------|
| Nemotron 3 Ultra | 550B | MoE Hybrid | 2026-06-09 |

- **Nemotron 3 Ultra**: 550B total, 55B active. Hybrid Mamba-Attention architecture. 1M context window.
- **Embedding model**: #1 ranking on embedding benchmarks.
- **Mamba-Attention hybrid**: Combines state-space models with transformer attention.
- Training data: 20T tokens.

### Amazon

| Model | Type | Released |
|-------|------|----------|
| Amazon Nova family | Multimodal | 2025-03-17 |

- **Nova Pro/Lite/Micro**: Text models at different scales.
- **Nova Canvas**: Image generation.
- **Nova Reel**: Video generation.
- arXiv: 2506.12103.

### Zhipu AI

| Model | Params | Released | License |
|-------|--------|----------|---------|
| GLM-5 | 744B | 2026-02-22 | - |
| GLM-5.2 | 744B | 2026-06-16 | MIT |

- **GLM-5.2**: 744B parameters. IndexShare approach. 1M context window. MIT license (open-weight).
- **DSA (Dynamic Sparse Attention)**: Key architectural innovation.
- **GLM-5**: Original release, Feb 2026.

### InternLM (Shanghai AI Lab)

| Model | Params | Type | Released |
|-------|--------|------|----------|
| Intern-S1-Pro | 1T | MoE | 2026-03-26 |

- **Intern-S1-Pro**: 1 trillion parameters. MoE architecture. Scientific multimodal model.
- Training data: 4T tokens.

### Moonshot AI

| Model | Params | Released | Notes |
|-------|--------|----------|-------|
| Kimi K3 | 2.8T | 2026-07 | Subscription pause |
| Kimi K2.5 | 1T | 2026-06 | Agent Swarm |

- **Kimi K3**: 2.8 trillion parameters. 1M context. Subscription paused due to demand exceeding capacity. "Code Arena" 1679 points, topped leaderboard.
- **Kimi K2.5**: 1T parameters. 256+ tools support. Agent Swarm architecture.
- **Kimi K2**: 1.04T total / 32B active. 15.5T training tokens. MMLU 77.4, MATH-500 96.2. arXiv: 2605.09388.

### StepFun

| Model | Params | Released | Key Feature |
|-------|--------|----------|-------------|
| Step 3 | 321B/38B | 2025 WAIC | Multimodal reasoning |
| Step 3.5 Flash | 196B | 2026 | 400 TPS |
| Step 3.7 Flash | 198B | 2026 | Latest |

- **Step 3**: 321B total / 38B active MoE. Multimodal reasoning.
- **Step 3.7 Flash**: 198B params, 400 tokens per second inference.
- **StepAudio 2.5 Realtime**: Real-time audio capabilities.

### ByteDance

| Model | Type | Released | License |
|-------|------|----------|---------|
| Doubao-1.5-pro | MoE | 2025-01-22 | - |
| Seedance 2.0 | Video gen | 2026 | - |
| Seed3D 2.0 | 3D gen | 2026 | - |

- **Doubao-1.5-pro**: MoE architecture. Sparse scaling law innovation. RL training approach.
- **Seedance 2.0**: Video generation model.
- **Seed3D 2.0**: 3D generation model.
- **Game-TARS**: 500B tokens trained, outperforms GPT-5 on game tasks.

### 01.AI

| Model | Type | Released |
|-------|------|----------|
| Yi-Lightning | MoE | 2025 |

- **Yi-Lightning**: Enhanced MoE architecture. RAISE safety framework. Ranked 6th on Chatbot Arena.
- **Yi-Lightning 2**: Latest version.

### Baichuan

| Model | Type | Released | Key Metric |
|-------|------|----------|------------|
| Baichuan M3/M4 | - | 2026 | 3.3% hallucination |
| Baichuan Omni-1.5 | 7B | 2026-01 | Medical focus |

- **Baichuan M3/M4**: Latest models. 3.3% hallucination rate (industry-leading).
- **Baichuan Omni-1.5**: 7B multimodal. Medical domain focus.

---

## Cross-Cutting Trends

### MoE Dominance
All major releases now use Mixture-of-Experts:
- DeepSeek V4: 1.6T/49B (32x sparsity)
- Llama 4 Maverick: 128 experts
- Qwen3-235B-A22B: 235B/22B
- Kimi K2: 1.04T/32B
- Nemotron 3 Ultra: 550B/55B (10x sparsity)

### Hybrid Attention Architectures
Mamba-Attention hybrids gaining traction:
- Nemotron 3 Ultra: Mamba + Attention
- DeepSeek V4: CSA + HCA
- Efficient for long-context (1M+ tokens)

### Pricing Innovation
- DeepSeek V4: MIT license, free tier
- xAI Grok 4.5: $2/$6 (input/output)
- Open-weight models collapsing closed model margins
- Peak pricing innovation era

### Agent Capabilities
- Autonomous agents (OpenAI GPT-5.6 Sol)
- Tool use (Kimi K2: 256+ tools)
- Multi-agent systems (Grok 4.20 SA/MA)
- Agent security becoming critical (Anthropic RSP)

### Safety & Alignment
- Anthropic: RSP evaluations, System Cards
- OpenAI: GPT-5.6 System Card
- Apple: On-device privacy focus
- Safety-first release cadence

### Long Context
- 10M context: Llama 4 Scout
- 1M context: DeepSeek V4, Nemotron 3 Ultra, Gemini 2.5
- 196K context: Kimi K2
- Context windows expanding 10x yearly

### Small Model Resurgence
- Phi-4-RV-15B: Strong reasoning at 15B
- Baichuan Omni-1.5: Medical at 7B
- Apple AFM: 3B on-device
- Efficiency over scale narrative strengthening

---

## Model Comparison Table

| Company | Model | Total Params | Active Params | Experts | Context | License |
|---------|-------|--------------|---------------|---------|---------|---------|
| DeepSeek | V4 | 1.6T | 49B | - | 1M | MIT |
| Meta | Llama 4 Scout | - | - | 16/128 | 10M | Open |
| Google | Gemini 2.5 Pro | - | - | - | 1M | Proprietary |
| Anthropic | Claude Fable 5 | - | - | - | - | Proprietary |
| Qwen | Qwen3-235B | 235B | 22B | - | - | Open |
| Moonshot | Kimi K3 | 2.8T | - | - | 1M | Open |
| xAI | Grok 3 | 1.2T | - | 128 | - | Proprietary |
| NVIDIA | Nemotron 3 Ultra | 550B | 55B | 512 | 1M | - |
| Zhipu | GLM-5.2 | 744B | - | - | 1M | MIT |
| InternLM | Intern-S1-Pro | 1T | - | - | - | - |

---

## Key Takeaways

1. **MoE is the new default**: Every major lab uses MoE for efficiency at scale.
2. **10M context is here**: Meta Llama 4 Scout achieved 10M context, setting new standard.
3. **Pricing disruption**: Open-weight models (DeepSeek MIT, GLM-5.2 MIT) forcing closed models to innovate on value.
4. **Agent capabilities matter**: GPT-5.6 autonomous hackathon, Kimi K2 256+ tools, Grok 4.20 multi-agent.
5. **Safety becoming mandatory**: System Cards now standard for major releases (OpenAI, Anthropic, xAI).
6. **Hybrid architectures winning**: Mamba-Attention hybrids (Nemotron) and CSA+HCA (DeepSeek) outperform pure transformers at scale.
7. **Demand exceeds supply**: Kimi K3 subscription pause shows demand outstripping infrastructure.
8. **Small models matter**: Phi-4-RV-15B and Baichuan Omni-1.5 prove strong capabilities at small scales.
9. **Multimodal native**: All new models support text + image + video + audio.
10. **Open ecosystem accelerating**: MIT licenses, 400M+ Llama downloads, Apache 2.0 Mistral models.

---

*Last updated: 2026-07-27*