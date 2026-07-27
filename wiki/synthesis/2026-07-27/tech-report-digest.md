---
title: 2026-07-27 LLM Tech Report Digest
type: synthesis
created: 2026-07-27
updated: 2026-07-27
sources: [tech-report-digest.md]
tags: [llm, tech-report, 2026, moe, reasoning, multimodal, scaling-law]
---

## 2026-07-27 LLM Tech Report Digest

### 1. DeepSeek

**DeepSeek-V4**

- **Organization**: DeepSeek (深度求索)
- **Model**: DeepSeek-V4
- **Date**: July 2026
- **Core Parameters**: 1.6T total parameters; 49B and 284B parameter variants (DeepSeek-V4 & DeepSeek-V4.5)
- **Key Innovations**: Combined Sparse Attention (CSA) + Hybrid Context Attention (HCA) for efficient long-context processing; 1M context window; MoE architecture with efficient routing
- **ArXiv**: https://arxiv.org/abs/2507.06810

---

### 2. OpenAI

**GPT-5.6**

- **Organization**: OpenAI
- **Model**: GPT-5.6 (Sol/Terra/Luna variants)
- **Date**: 2026
- **Core Parameters**: Not disclosed
- **Key Innovations**: GPT-5.6 system card released June 26, 2026; family of models (Sol, Terra, Luna) targeting different use cases
- **ArXiv**: https://openai.com/gpt-5-6-system-card/

---

### 3. Meta AI

**Llama 4**

- **Organization**: Meta AI
- **Model**: Llama 4 Scout, Llama 4 Maverick
- **Date**: 2026
- **Core Parameters**: Scout (17B parameters, 16 experts); Maverick (17B parameters, 128 experts); Behemoth (preview)
- **Key Innovations**: Experts at 10B+ active parameters; Scout supports up to 10M context window; distributed expert architecture with 128 experts in Maverick
- **ArXiv**: https://ai.meta.com/blog/llama-4-multimodal-intelligence/

---

### 4. Google DeepMind

**Gemini**

- **Organization**: Google DeepMind
- **Model**: Gemini 2.5 Pro/Flash, Gemini 3.1 Pro
- **Date**: 2025-2026
- **Core Parameters**: Not disclosed
- **Key Innovations**: 3-hour video context understanding; 1M token context window; Gemini 3.1 Pro capabilities in reasoning and code generation
- **ArXiv**: https://deepmind.google/research/publications/

---

### 5. Anthropic

**Claude Opus 5**

- **Organization**: Anthropic
- **Model**: Claude Opus 5, Claude Mythos 5
- **Date**: July 24, 2026 (system card release)
- **Core Parameters**: Not disclosed
- **Key Innovations**: System card for Claude Opus 5 released July 24, 2026; Claude Mythos 5 announced as advanced reasoning model; safety and alignment improvements documented in system cards
- **ArXiv**: https://www.anthropic.com/research/system-card-claude-opus-5

---

### 6. Mistral AI

**Leanstral**

- **Organization**: Mistral AI
- **Model**: Leanstral (6B)
- **Date**: March 2026
- **Core Parameters**: 6B
- **Key Innovations**: Built for mathematical reasoning and proof generation; uses Lean 4 proof language for formal verification; Apache 2.0 open-source license; achieves ~85% on miniF2F benchmark through agentic proof refinement; generates correct proofs 44% of time
- **ArXiv**: https://arxiv.org/pdf/2603.14520

---

### 7. Qwen (Alibaba)

**Qwen3.5-Omni**

- **Organization**: Qwen Team (Alibaba Cloud)
- **Model**: Qwen3.5-Omni
- **Date**: 2026
- **Core Parameters**: Hybrid Attention MoE architecture
- **Key Innovations**: 256K context length; trained on 100M+ hours of audio-visual data; outperforms comparable models on 22/24 OmniBench metrics; strong performance on 8/9 benchmarks
- **ArXiv**: https://arxiv.org/html/2606.12863

---

### 8. Yi (01.AI)

**Yi-Lightning**

- **Organization**: 01.AI (Yi)
- **Model**: Yi-Lightning
- **Date**: 2026
- **Core Parameters**: Not disclosed
- **Key Innovations**: MoE architecture with enhanced routing mechanism; RLHF for alignment and safety; RAISE safety framework (Responsible AI Safety Ecosystem)
- **ArXiv**: https://docs.01.ai/

---

### 9. Baichuan

**Baichuan-M4**

- **Organization**: Baichuan (百川智能)
- **Model**: Baichuan-M4
- **Date**: 2026
- **Core Parameters**: Not disclosed
- **Key Innovations**: Clinical-grade medical agent performance; SPAR++ (Structured Prompting and Alignment for Reasoning); 3.3% hallucination rate (low)
- **ArXiv**: https://arxiv.org/abs/2507.11987

---

### 10. Microsoft

**Phi-4-reasoning-vision-15B**

- **Organization**: Microsoft
- **Model**: Phi-4-reasoning-vision-15B
- **Date**: March 2026
- **Core Parameters**: 15B
- **Key Innovations**: Open-weight multimodal reasoning model; vision + language capabilities; designed for agentic reasoning and coding tasks; strong performance on reasoning benchmarks relative to size
- **ArXiv**: https://arxiv.org/pdf/2603.12984

---

### 11. Apple

**Apple Intelligence Foundation Models**

- **Organization**: Apple
- **Model**: Apple Intelligence Foundation Models (3B on-device, server variants)
- **Date**: 2025
- **Core Parameters**: 3B on-device; PT-MoE for server
- **Key Innovations**: PT-MoE (Parallel Transfer MoE) architecture; KV-cache sharing for efficiency; 2-bit Quantization-Aware Training (QAT) for edge deployment; on-device inference optimization
- **ArXiv**: https://machinelearning.apple.com/research/appintellifm

---

### 12. NVIDIA

**Nemotron 3 Ultra**

- **Organization**: NVIDIA
- **Model**: Nemotron 3 Ultra
- **Date**: June 2026
- **Core Parameters**: 550B (55B active)
- **Key Innovations**: Mamba-Attention hybrid MoE architecture; 20T tokens training corpus; 1M context window; designed for enterprise AI applications; efficient inference through sparse activation
- **ArXiv**: https://arxiv.org/html/2507.24379

---

### 13. xAI

**Grok 4.5**

- **Organization**: xAI
- **Model**: Grok 4.5
- **Date**: July 14, 2026 (model card release)
- **Core Parameters**: Not disclosed
- **Key Innovations**: Model card released July 14, 2026; agentic and reasoning capabilities; SpaceXAI and Cursor integration for coding assistance; multimodal support
- **ArXiv**: https://docs.x.ai/docs/guides/model-cards/grok-4-5

---

### 14. Amazon

**Nova Family**

- **Organization**: Amazon (AWS)
- **Model**: Amazon Nova Pro, Nova Lite, Nova Micro, Nova Canvas, Nova Reel
- **Date**: 2024
- **Core Parameters**: Not disclosed
- **Key Innovations**: Nova Pro (multimodal), Nova Lite (lightweight), Nova Micro (text-only), Nova Canvas (image generation), Nova Reel (video generation); Amazon Nova Foundation Models technical report
- **ArXiv**: https://www.amazon.science/publications/amazon-nova-foundation-models-technical-report

---

### 15. Zhipu AI

**GLM-5**

- **Organization**: Zhipu AI (智谱AI)
- **Model**: GLM-5
- **Date**: 2026
- **Core Parameters**: Not disclosed
- **Key Innovations**: Dynamic Sparse Attention (DSA) for efficiency; asynchronous RL for post-training; agentic coding capabilities; achieves state-of-the-art on LMArena; optimized for reasoning and tool use
- **ArXiv**: https://arxiv.org/abs/2507.22078

---

### 16. InternLM

**Intern-S1-Pro**

- **Organization**: InternLM Team (Shanghai AI Laboratory)
- **Model**: Intern-S1-Pro
- **Date**: 2026
- **Core Parameters**: 1T total parameters
- **Key Innovations**: Scientific multimodal model with reasoning capabilities; RL training at 1T scale; covers 100+ scientific tasks; multimodal reasoning for scientific applications
- **ArXiv**: https://arxiv.org/html/2511.09157v3

---

### 17. Moonshot AI

**Kimi-K2.5**

- **Organization**: Moonshot AI (月之暗面)
- **Model**: Kimi-K2.5
- **Date**: 2026
- **Core Parameters**: 1T total, 32B active
- **Key Innovations**: MoonViT architecture for multimodal; 15T mixed token training; 256K context length; native multimodal and agentic capabilities; MoE with efficient expert routing
- **ArXiv**: https://arxiv.org/html/2511.05569v3

---

### 18. StepFun

**Step-DeepResearch**

- **Organization**: StepFun (阶跃星辰)
- **Model**: Step-DeepResearch
- **Date**: 2026
- **Core Parameters**: 32B
- **Key Innovations**: Deep research agent model; ADR-Bench benchmark; atomic capability synthesis approach; achieves strong performance on multi-hop reasoning and research tasks
- **ArXiv**: https://arxiv.org/html/2506.01432v1

---

### 19. ByteDance

**Seedream 2.0**

- **Organization**: ByteDance (字节跳动)
- **Model**: Seedream 2.0
- **Date**: March 2025
- **Core Parameters**: Not disclosed
- **Key Innovations**: Text-to-image generation model; RLHF for image generation alignment; bilingual (Chinese/English) support; Seedream 2.0 text-to-image technical report
- **ArXiv**: https://arxiv.org/pdf/2503.07703

---

## Key Trends Observed (2026)

### Architecture Evolution
- **MoE dominance**: Nearly all major players (DeepSeek, Meta, NVIDIA, Qwen, Moonshot, Mistral) use Mixture of Experts for efficiency
- **Hybrid attention**: DeepSeek (CSA+HCA), NVIDIA (Mamba-Attention), Qwen (Hybrid Attention MoE) combining different attention mechanisms
- **Massive scale**: 1T+ parameters becoming standard (InternLM, Moonshot, DeepSeek)

### Context Window Expansion
- **1M+ tokens**: DeepSeek-V4, NVIDIA Nemotron, Moonshot Kimi-K2.5 all support 1M context
- **10M context**: Meta Llama 4 Scout achieves 10M tokens
- **Video understanding**: Google Gemini handles 3-hour video context

### Reasoning and Agents
- **Dedicated reasoning models**: OpenAI GPT-5.6, Anthropic Claude Mythos 5, Mistral Leanstral
- **Deep research agents**: StepFun Step-DeepResearch, Zhipu GLM-5 with agentic coding
- **Formal verification**: Mistral Leanstral for mathematical proof generation

### Multimodal Integration
- **Native multimodal**: Qwen3.5-Omni, Moonshot Kimi-K2.5, Microsoft Phi-4-vision
- **Image/Video generation**: ByteDance Seedream 2.0, Amazon Nova Canvas/Reel
- **Scientific multimodal**: InternLM Intern-S1-Pro for science applications

### Efficiency and Deployment
- **Edge optimization**: Apple 2-bit QAT, 3B on-device models
- **Sparse activation**: NVIDIA 550B total with 55B active parameters
- **Open-source releases**: Mistral Leanstral (Apache 2.0), Microsoft Phi-4 open-weight

### Safety and Alignment
- **Safety frameworks**: Yi RAISE framework, Anthropic system cards
- **Medical safety**: Baichuan-M4 with 3.3% hallucination rate
- **Responsible AI**: Apple, Anthropic, Meta publishing system cards and safety reports

---

*Last updated: 2026-07-27*
