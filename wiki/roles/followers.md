---
title: Karpathy 关注者导航
type: synthesis
created: 2026-06-02
updated: 2026-06-02
tags: [karpathy, followers, x-posts, talks, intellectual-journey]
---

# Karpathy 关注者导航 — Follower's Guide

> 追踪 Andrej Karpathy 的思想演进。从 2024 年技术演讲到 2025–2026 年 X 帖子与 keynote，覆盖他的关键言论、概念发明和思想转折点。

---

## 总 — 思想演进轨迹

Karpathy 的公开言论呈现出清晰的阶段性：2024 年以技术演讲为主（系统/教育/AGI 哲学），2025 年是高密度的 X 帖子输出期（发明 20+ 新概念），2026 年进入概念深化和命名收敛阶段。

### 时间线

```
2024.10    GPU MODE IRL → llm.c 的故事
           Berkeley SkyDeck → "Feel the AGI"
           
2025.04    开始密集 X 帖子
2025.06    YC AI Startup School → Software 3.0
2025.07    发明 "bacterial code"
2025.10    nanochat 发布
2025.12    编码 agent "basically work" 的转折点
           
2026.01    Claude coding reflections
2026.02    Agentic Engineering 正式命名
2026.02    Malleable Software / Bacterial Code 深化
2026.03    Autoresearch + Claws
2026.04    LLM Knowledge Bases & BYOAI
```

---

## 分 — 按内容类型

### 🎤 演讲与访谈

| 来源 | 日期 | 核心内容 |
|------|------|---------|
| [[sources/gpu-mode-irl-2024-keynote|GPU MODE IRL 2024]] | 2024.10 | llm.c 的完整故事 — torch.compile 的挫折到纯 C 实现 |
| [[sources/berkeley-ai-hackathon-2024-keynote|Berkeley SkyDeck Keynote]] | 2024 | "Feel the AGI", Project Snowballs, 10,000 Hours |
| [[sources/software-is-changing-again|YC AI Startup School Keynote]] | 2025.06 | Software 3.0 / LLM OS 框架的系统化阐述 |
| [[sources/summoning-ghosts-not-animals|Dwarkesh Podcast]] | 2025 | "We're Summoning Ghosts, Not Building Animals" — AGI 哲学深度访谈 |
| [[sources/ai-capability-gap|AI Capability Gap]] | — | AI 能力认知差距的分析 |

### 📱 X 帖子 — 2025 年（16 个主题包）

| 主题包 | 时间 | 关键概念 |
|-------|------|---------|
| [[sources/karpathy-x-2025-ai-assisted-coding|AI-Assisted Coding]] | Apr–Dec | 7-step inner loop, Verification Gap, Code Post-Scarcity |
| [[sources/karpathy-x-2025-build-for-agents|Build for Agents]] | Apr–Nov | MenuGen, LLM GUI, Horseless Carriage |
| [[sources/karpathy-x-2025-evals-and-model-vibes|Evals & Model Vibes]] | Apr/Nov | Leaderboard Illusion, Model Smell |
| [[sources/karpathy-x-2025-rl-and-learning-paradigms|RL & Learning Paradigms]] | May–Aug | System Prompt Learning, "RL is Terrible" |
| [[sources/karpathy-x-2025-software-paradigm|Software Paradigm & Verifiability]] | Jul–Dec | Verifiability, RLVR — "2025 年 #1 范式转变" |
| [[sources/karpathy-x-2025-ghosts-and-psychology|Ghosts & LLM Psychology]] | Oct–Dec | Animals vs Ghosts 深化, People Spirits |
| [[sources/karpathy-x-2025-nanochat-saga|nanochat Saga]] | Oct–Dec | 发布、$1000 扩展、SpellingBee 能力嫁接 |
| [[sources/karpathy-x-2025-tesla-fsd|Tesla FSD]] | Jul/Nov | HW4 Model X "no notes" drive |
| [[sources/karpathy-x-2025-video-gen|Video Gen]] | Jul | Veo 3, MirageLSD |
| [[sources/karpathy-x-2025-cognitive-core|Cognitive Core Spec]] | Jul | 多模态 + Matryoshka + LoRA slots + cloud oracles |
| [[sources/karpathy-x-2025-bacterial-code-origin|Bacterial Code Origin]] | Jul | 概念起源 |
| [[sources/karpathy-x-2025-dwarkesh-recap|Dwarkesh Recap]] | Oct | 时间线澄清, 5-10X pessimistic |
| [[sources/karpathy-x-2025-llm-reading|LLM Reading]] | Nov–Dec | Reader3, HN Time Capsule, Galaxy-Brain Reasoning |
| [[sources/karpathy-x-2025-education|Education]] | Nov | AI detectors 无效, AI-capable + AI-free |
| [[sources/karpathy-x-2025-power-to-the-people|Power to the People]] | Apr | LLM diffusion inversion |
| [[sources/karpathy-x-2025-misc|Misc 2025]] | 全年 | Digital hygiene, prompt injection, 公共物品 |

### 📱 X 帖子 — 2026 年（10 个主题包）

| 主题包 | 时间 | 关键内容 |
|-------|------|---------|
| [[sources/karpathy-x-2026-fsd-coast-to-coast|FSD Coast-to-Coast]] | Jan | 2,732 mi, zero interventions — Software 2.0 的胜利 |
| [[sources/karpathy-x-2026-nanochat-gpt2-reproduction|nanochat & GPT-2]] | Jan–Feb | $20 在 8×H100 上复现 GPT-2 |
| [[sources/karpathy-x-2026-claude-coding-reflections|Claude Coding Reflections]] | Jan | Agentic Engineering 手册，80/20 → 20/80 翻转 |
| [[sources/karpathy-x-2026-agentic-engineering|Agentic Engineering]] | Feb | 正式命名，"Vibe Coding 的成熟兄弟" |
| [[sources/karpathy-x-2026-malleable-software|Malleable Software]] | Feb | Bacterial Code 深化, App Store Outdated |
| [[sources/karpathy-x-2026-agent-networks|Agent Networks]] | Feb | Simile AI, Org Code |
| [[sources/karpathy-x-2026-autoresearch-and-claws|Autoresearch & Claws]] | Feb–Mar | 自动研究 agent + command-center IDE |
| [[sources/karpathy-x-2026-supply-chain|Supply Chain Attacks]] | Mar | litellm, axios 攻击案例分析 |
| [[sources/karpathy-x-2026-llm-wiki|LLM Knowledge Bases & BYOAI]] | Apr | 个人知识库 + BYOAI 模式 |
| [[sources/karpathy-x-2026-misc|Misc 2026]] | 全年 | Point-vs-slope, memory overfit |

### 📝 综合概念与实体

| 概念 | 首次提出 | 一句话定义 |
|------|---------|-----------|
| [[concepts/vibe-coding|Vibe Coding]] | 2025.02 | 用 LLM "vibe" 写代码的术语发明 |
| [[concepts/verifiability|Verifiability]] | 2025.07 | Software 2.0 的核心谓词 |
| [[concepts/rlvr|RLVR]] | 2025 | Verifiable Rewards 的 RL |
| [[concepts/animals-vs-ghosts|Animals vs Ghosts]] | 2025.10 | LLM 不是智能体而是"幽灵" |
| [[concepts/bacterial-code|Bacterial Code]] | 2025.07 | 自包含无依赖的代码美学 |
| [[concepts/agentic-engineering|Agentic Engineering]] | 2026.02 | Vibe Coding 的成熟继任者 |
| [[concepts/march-of-nines|March of Nines]] | 2026 | 技术可靠性提升的量词 |
| [[concepts/people-spirits|People Spirits]] | 2025 | 用户对 LLM 的拟人化本能 |

### 🔗 Karpathy 个人档案

- [[entities/andrej-karpathy|Andrej Karpathy]] — 职业时间线 2005–2026
- 关键关联：Tesla AI Director (2017–2022), OpenAI (2015–2017, 2023), Eureka Cofounder
