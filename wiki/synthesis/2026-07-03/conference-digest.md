---
title: "顶会论文专题报告 — 2026年7月全面版"
type: synthesis
created: 2026-07-03
updated: 2026-07-03
sources: []
tags: [conference-digest, icml-2026, aaai-2026, neurips-2025, iclr-2026, cvpr-2026, kdd-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2025, recsys-2025]
---

# 顶会论文专题报告 — 2026年7月全面版

> Comprehensive digest of top ML/AI conference proceedings, award-winning papers, and notable arXiv preprints. Covers 12+ venues, 15+ labs, and 80+ curated papers across LLMs, recommendation systems, CTR prediction, AI agents, games, generative models, and benchmarking.

---

## 一、Overview / 总览

| Conference | Date | Submissions | Accepted | Rate | Location |
|-----------|------|------------|----------|------|----------|
| **AAAI 2026** | Jan 20–27 | ~29,000 (23,680 after screening) | 4,167 | 17.6% | Singapore |
| **ICLR 2026** | Apr 22–24 | 19,525 | 5,342 | 27.4% | Rio de Janeiro |
| **CVPR 2026** | Jun 3–7 | 16,092 | 4,090 | 25.4% | Denver |
| **ICML 2026** | Jul 6–11 | 23,918 | 6,352 | 26.6% | Seoul |
| **KDD 2026** | Aug 9–13 | 1,215 (cycle 1) | 256 | 21% | Jeju Island |
| **ACL 2026** | (summer) | — | — | — | — |
| **EMNLP 2025** | Nov 4–9 | ~8,000 | 3,228 (1,811 Main + 1,417 Findings) | 22.2% (Main) | Suzhou |
| **NeurIPS 2025** | Dec 2025 | ~20,000 | ~5,300 | ~26% | San Diego |
| **SIGIR 2026** | Jul 20–24 | — | — | — | Melbourne |
| **CIKM 2025** | Oct 2025 | — | — | — | — |
| **RecSys 2025** | Sep 2025 | — | — | — | Prague |
| **WWW 2026** | Apr 2026 | — | — | — | — |

---

## 二、Award-Winning Papers / 获奖论文

### 🏆 AAAI 2026 — Outstanding Papers

5 main track + 2 AI for Social Impact.

| Paper | Authors | Affiliation | Key Innovation |
|-------|---------|-------------|----------------|
| **COREA: Confidence-Calibrated Small-Large LLM Collaboration** | — | Amazon | SLM+LLM cascade with RL-based confidence calibration; ~21.5% cost reduction within 2% of LLM-only performance |
| **ProCo: Multi-Modal Dataset Distillation** | — | A*STAR CFAR | Enhanced correspondence coverage for multi-modal distillation; outperforms priors on VQA |
| **GenMatLab** | — | A*STAR CFAR | Demo platform for inverse materials design using generative AI via natural language |

**Notable**: AAAI 2026 ran the largest-ever AI-assisted peer review pilot — 22,977 papers reviewed by AI in <24 hours (no scores, no accept/reject; cross-checked by humans).

### 🏆 ICLR 2026 — Outstanding Papers

2 Outstanding + 1 Honorable Mention from 5,355 accepted.

| Paper | Key Innovation |
|-------|----------------|
| **Transformers are Inherently Succinct** ([arXiv:2510.19315](https://arxiv.org/abs/2510.19315)) | Proves Transformers are doubly exponentially more succinct than finite automata; exponentially more succinct than RNNs. Corollary: verifying Transformer properties is EXPSPACE-complete. |
| **LLMs Get Lost in Multi-Turn Conversation** ([OpenReview](https://openreview.net/forum?id=VKGTGGcwl6)) | Across 200K+ simulated conversations, every top LLM shows **39% drop** from single-turn to multi-turn. Decomposed into small aptitude loss + large unreliability increase. |
| **∇-Reasoner: LLM Reasoning via Test-Time Gradient Descent in Latent Space** ([ICLR 2026](https://iclr.cc/virtual/2026/poster/10007349)) | Differentiable optimization over token logits in decoding loop. Theorem: test-time gradient descent ≈ KL-regularized RL. **+20% accuracy** on math reasoning with **10–40% fewer model calls**. |

### 🏆 CVPR 2026 — Best Paper & Highlights

| Paper | Authors | Innovation |
|-------|---------|------------|
| **Best Paper: Efficiently Reconstructing Dynamic Scenes One D4RT at a Time** | — | Feed-forward 4D reconstruction; attention-forcing for dynamic/static disentanglement; SOTA on dynamic scene benchmarks |
| **Scal3R: Scalable Test-Time Training for Large-Scale 3D Reconstruction** | Tao Xie et al. | Long video sequence 3D reconstruction; global contextual cues without explicit 3D priors |
| **MoRe: Feedforward 4D Reconstruction from Monocular Video** | — | Grouped causal attention; temporal coherence; high-quality dynamic reconstructions |

**Trend**: Multimodal LLM papers at CVPR doubled from 4.9% → **10.6%** of accepted papers — now the single largest theme.

### 🏆 NeurIPS 2025 — Best Papers (4 Best + 3 Runner-Up)

| Paper | Key Contribution |
|-------|-----------------|
| **Gated Attention for LLMs** (Alibaba Qwen, [arXiv:2505.06708](https://arxiv.org/abs/2505.06708)) | Learnable head-specific sigmoid gate after Scaled Dot-Product Attention. Eliminates attention-sink, stabilizes training, validated on 1.7B dense + 15B MoE up to 3.5T tokens. |
| **Artificial Hivemind** ([arXiv:2510.22954](https://arxiv.org/abs/2510.22954)) | Infinity-Chat dataset (26K queries, 31K annotations, 25 annotators/ex). Documents intra-model repetition + inter-model homogeneity across 70+ models. |
| **1000 Layer Networks for Self-Supervised RL** ([arXiv:2503.14858](https://arxiv.org/abs/2503.14858)) | Contrastive RL at 1024 layers (vs typical 2–5) gives **2×–50× gains** on locomotion/manipulation with no demos or rewards. |
| **Why Diffusion Models Don't Memorize** ([arXiv:2505.17638](https://arxiv.org/abs/2505.17638)) | Two timescales: τ_gen (good samples) and τ_mem (memorization). τ_mem grows linearly with dataset size; reframes early stopping as structural necessity. |

**Runner-Ups**:
- **Does RL Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?** (Tsinghua, [arXiv:2504.13837](https://arxiv.org/abs/2504.13837)) — RLVR beats base at small k but loses at large k; base model's sampling already contains the reasoning paths. Distillation genuinely expands capability.
- **Superposition Yields Robust Neural Scaling** ([arXiv:2505.10465](https://arxiv.org/abs/2505.10465)) — First-principles derivation: L ∝ 1/m in strong-superposition regime. Validated on OPT/Pythia/Qwen.
- **Optimal Mistake Bounds for Transductive Online Learning** — Closes 30-year open problem: Θ(√d) where d = Littlestone dimension.

### 🏆 EMNLP 2025 — Best Paper

| Paper | Key Contribution |
|-------|-----------------|
| **Infini-gram mini** (UW/AI2, [arXiv:2506.12229](https://arxiv.org/abs/2506.12229)) | FM-index system for exact n-gram search on 83TB text (Common Crawl). Index = 44% of corpus. Infrastructure for contamination audits, membership inference, grounding. |

**Outstanding Papers**:
- **PAFT: Prompt-Agnostic Fine-Tuning** ([arXiv:2502.12859](https://arxiv.org/abs/2502.12859)) — Diverse synthetic prompts during SFT/RLFT; +7% generalization, 3.2× faster inference.
- **To Mask or to Mirror** (Google, [arXiv:2510.01924](https://arxiv.org/abs/2510.01924)) — 748-participant experiment; Gemini/GPT-4.1/Claude/Genma show model-specific collective alignment patterns.
- **Constructions are Revealed in Word Distributions** — Construction grammar patterns visible via RoBERTa statistical affinity.

---

## 三、LLM Architecture & Model Design / 大模型架构

### Hybrid Architectures (2026 Dominant Trend)

| Model | Affiliation | Architecture | Key Details |
|-------|-------------|-------------|-------------|
| **Nemotron 3 Super** (120B-A12B) | NVIDIA | Hybrid Mamba-2 + Attention MoE | Alternating Mamba-2/attention layers; NVFP4 pretraining; multi-token prediction for speculative decoding; synthetic MMLU-style data. [arXiv:2604.12374](https://arxiv.org/abs/2604.12374) |
| **Nemotron 3 Ultra** (550B-A55B) | NVIDIA | Scaled Nemotron 3 | Scaled embedding/projection; same building blocks. |
| **Nemotron 3 Nano** (4B) | NVIDIA | Small hybrid | Consumer-hardware-friendly hybrid. |
| **Mamba-3** | — | Improved SSM | Enhanced sequence modeling using state space principles. [arXiv:2603.15569](https://arxiv.org/abs/2603.15569) |
| **Gated DeltaNet-2** | — | Linear Attention | Decoupling erase and write in linear attention. [arXiv:2605.22791](https://arxiv.org/abs/2605.22791) |
| **Qwen3.6** | Alibaba | Hybrid (Gated DeltaNet) | Uses Gated DeltaNet layers for non-attention portions; most popular open-weight hybrid LLM series. |
| **ERNIE 5.0** | Baidu | — | Technical report. [arXiv:2602.04705](https://arxiv.org/abs/2602.04705) |
| **GLM-5** | Zhipu AI | — | From Vibe Coding to Agentic Engineering. [arXiv:2602.15763](https://arxiv.org/abs/2602.15763) |
| **Step 3.5 Flash** | Stepfun | MoE | 11B active parameters; open frontier-level intelligence. [arXiv:2602.10604](https://arxiv.org/abs/2602.10604) |
| **Arcee Trinity** | Arcee | Hybrid | Small/medium/large model collaboration. [arXiv:2602.17004](https://arxiv.org/abs/2602.17004) |
| **Ministral 3** | Mistral | — | Technical report. [arXiv:2601.08584](https://arxiv.org/abs/2601.08584) |
| **MiniMax-M2** | MiniMax | — | Mini activations, max real-world intelligence. [arXiv:2605.26494](https://arxiv.org/abs/2605.26494) |
| **Scaling Embeddings Outperforms Scaling Experts** | — | MoE | For MoE, increasing embedding dim beats adding more experts for the same compute budget. [arXiv:2601.21204](https://arxiv.org/abs/2601.21204) |

### Activation & Geometry Studies

| Paper | Key Finding |
|-------|-------------|
| **The Spike, the Sparse and the Sink** ([arXiv:2603.05498](https://arxiv.org/abs/2603.05498)) | Anatomy of massive activations and attention sinks in LLMs. |
| **Symmetry in Language Statistics Shapes Model Representations** ([arXiv:2602.15029](https://arxiv.org/abs/2602.15029)) | Statistical symmetry of language shapes representation geometry. |

---

## 四、Reasoning & Test-Time Compute / 推理与测试时计算

| Paper | Affiliation | Venue | Key Finding |
|-------|-------------|-------|-------------|
| **∇-Reasoner** | — | ICLR 2026 Oral | Gradient descent in token logit space; +20% math reasoning, -40% model calls |
| **Mind Evolution** | Google DeepMind | arXiv 2501.09891 | Evolutionary search for scaling inference-time compute; language model generates/recombines/refines candidates |
| **Budget-Guided MCTS** | — | ICML 2026 | Fixed token budget per query; BG-MCTS for test-time scaling |
| **Formal Comparison: CoT vs Latent Thought** | — | ICML 2026 | CoT reaches TC^{k-1}; Latent Thought reaches TC^k under polylog depth |
| **s1: Simple Test-Time Scaling** | — | EMNLP 2025 | Minimal test-time compute strategy |
| **Evolving Deeper LLM Thinking** | Google DeepMind | arXiv | Mind Evolution avoids formalizing inference problem; solution evaluator suffices |

---

## 五、Agent Systems / 智能体系统

### Multi-Agent Frameworks

| Paper | Affiliation | Venue | Key Innovation |
|-------|-------------|-------|----------------|
| **Intelligent AI Delegation** ([arXiv:2602.11865](https://arxiv.org/abs/2602.11865)) | Google DeepMind | arXiv Feb 2026 | Framework for dynamic capability assessment, adaptive task reassignment, monitoring, reputation; forbids delegation unless outcome is precisely verifiable |
| **Towards a Science of Scaling Agent Systems** ([arXiv:2512.08296](https://arxiv.org/abs/2512.08296)) | Google Research + DeepMind + MIT | arXiv | Quantitative scaling principles across 260 configs, 5 architectures, 3 LLM families. R²=0.37. Capability-saturation effect: multi-agent overhead on tool-heavy tasks |
| **ACE: Agentic Context Engineering** ([arXiv:2510.04618](https://arxiv.org/abs/2510.04618)) | Stanford | arXiv | Contexts as evolving playbooks; +10.6% on agents, +8.6% on finance; prevents context collapse |
| **OctoTools** | — | ACL 2026 | Multi-agent framework with extensible tools for complex reasoning |
| **Foundation Protocol** ([arXiv:2605.23218](https://arxiv.org/abs/2605.23218)) | Tencent/HKUST/UIUC | arXiv | Agentic society coordination protocol |
| **HGPO: Hierarchy-of-Groups Policy Optimization** ([arXiv:2602.22817](https://arxiv.org/abs/2602.22817)) | — | arXiv | Group-in-group policy optimization for LLM agent training |
| **AgentRec** ([arXiv:2510.01609](https://arxiv.org/abs/2510.01609)) | — | arXiv Oct 2025 | LLM-powered multi-agent collaborative recommendation; +2.8% conversation success, +1.9% NDCG@10 |

### Agent Safety & Evaluation

| Paper | Venue | Key Finding |
|-------|-------|-------------|
| **AgentAuditor** | NeurIPS 2025 | Human-level safety and security evaluation for LLM agents |
| **AgentMisalignment** | NeurIPS 2025 | Measuring propensity for misaligned behavior in LLM-based agents |
| **DefenderBench** | NeurIPS 2025 | Toolkit for evaluating language agents in cybersecurity environments |
| **EU-Agent-Bench** | NeurIPS 2025 | Measuring illegal behavior of LLM agents under EU law |
| **MLRC-Bench** | NeurIPS 2025 | Can language agents solve machine learning research challenges? |

---

## 六、Recommendation Systems / 推荐系统

### Generative Recommendation

| Paper | Affiliation | Venue | Key Innovation |
|-------|-------------|-------|----------------|
| **GenCTR** ([DOI](https://arxiv.org/abs/2506.03699)) | Alibaba | KDD 2025 | Generative pre-training + discriminative fine-tuning for CTR; deployed in search advertising serving 100M+ daily users |
| **GE4Rec: Generative CTR Paradigm** ([arXiv:2512.14041](https://arxiv.org/abs/2512.14041)) | Tencent | arXiv | Generative paradigm for CTR prediction |
| **GenCI: Generative CTR via Cohort Intent Learning** ([arXiv:2601.18251](https://arxiv.org/abs/2601.18251)) | — | WWW 2026 | Cohort-level intent modeling for generative CTR |
| **AgentRec** ([arXiv:2510.01609](https://arxiv.org/abs/2510.01609)) | — | arXiv | Multi-agent LLM recommendation framework |
| **RecBench+** ([arXiv:2503.09382](https://arxiv.org/abs/2503.09382)) | — | WSDM 2026 | Benchmark for LLM-based personalized recommendation assistants |

### Scaling Laws for Recommendation

| Paper | Affiliation | Key Finding |
|-------|-------------|-------------|
| **Climber** (WWW 2025) | NetEase | Efficient scaling laws for large recommendation models |
| **Kunlun** ([arXiv:2602.10016](https://arxiv.org/abs/2602.10016)) | Meta | Unified architecture scaling laws |
| **LLaTTE** ([arXiv:2601.20083](https://arxiv.org/abs/2601.20083)) | Meta | Multi-stage scaling laws for ads recommendation |
| **Wukong** (ICML 2024) | Meta | Scaling law for large-scale recommendation |
| **EST** ([arXiv:2602.10811](https://arxiv.org/abs/2602.10811)) | Alibaba | Efficient scaling laws for CTR |
| **FAT** ([arXiv:2511.12081](https://arxiv.org/abs/2511.12081)) | Alibaba | Rademacher CTR scaling law |
| **SUAN** (RecSys 2025) | Meituan | Online CTR scaling methodology |
| **UniMixer** ([arXiv:2604.00590](https://arxiv.org/abs/2604.00590)) | Kuaishou | Unified architecture for scaling laws |

### CTR & Ranking (Selected Highlights)

| Paper | Affiliation | Venue | Key Innovation |
|-------|-------------|-------|----------------|
| **TokenMixer-Large** ([arXiv:2602.06563](https://arxiv.org/abs/2602.06563)) | ByteDance | Hardware utilization scaling for industrial ranking models |
| **Zenith** ([arXiv:2601.21285](https://arxiv.org/abs/2601.21285)) | ByteDance | Billion-scale livestreaming ranking |
| **RankUp** ([arXiv:2604.17878](https://arxiv.org/abs/2604.17878)) | Tencent | KDD 2026 | High-rank representations for ad ranking |
| **SORT** ([arXiv:2603.03988](https://arxiv.org/abs/2603.03988)) | Alibaba | Systematically optimized ranking transformer |
| **MUSE** ([arXiv:2512.07216](https://arxiv.org/abs/2512.07216)) | Alibaba | 100K-length lifelong user interest modeling |
| **CADET** ([arXiv:2602.11410](https://arxiv.org/abs/2602.11410)) | LinkedIn | Decoder-only ads CTR |
| **CHIME** ([arXiv:2504.06780](https://arxiv.org/abs/2504.06780)) | Kuaishou | Holistic interest + LLM + VQ |
| **MixFormer** ([arXiv:2602.14110](https://arxiv.org/abs/2602.14110)) | ByteDance | Co-scaling dense and sequence for KDD 2026 |
| **OneTrans** ([arXiv:2510.26104](https://arxiv.org/abs/2510.26104)) | ByteDance | Unified feature interaction + sequence modeling |
| **RPORec** ([arXiv:2605.21967](https://arxiv.org/abs/2605.21967)) | Kuaishou | RL + reasoning for recommendation |
| **ThinkRec** | — | WWW 2026 | Thinking-based LLM recommendation |
| **HeteroMixer** ([arXiv:2602.09387](https://arxiv.org/abs/2602.09387)) | Alibaba | Query-mixed interest extraction |

---

## 七、LLM Post-Training & Alignment / 后训练与对齐

### RLVR (RL from Verifiable Rewards)

| Paper | Key Finding |
|-------|-------------|
| **Does RL Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?** (Tsinghua, NeurIPS 2025 Runner-Up, [arXiv:2504.13837](https://arxiv.org/abs/2504.13837)) | RLVR + base at small k, but base wins at large k. Reasoning paths already in base's sampling distribution → **trained capability boundary narrows**. Distillation genuinely expands it. |
| **Safety Alignment Should Be Made More Than Just a Few Tokens Deep** (ICLR 2025 Outstanding, [arXiv:2406.05946](https://arxiv.org/abs/2406.05946)) | Alignment is "shallow" — only conditions first few output tokens. Explains adversarial-suffix attacks, prefilling attacks, easy reversal via fine-tuning. |
| **Learning Dynamics of LLM Finetuning** (ICLR 2025 Outstanding, [arXiv:2407.10490](https://arxiv.org/abs/2407.10490)) | "Squeezing effect": running off-policy DPO too long pushes down desired outputs. |
| **Teaching Claude Why** (Anthropic, May 2026) | Reducing agentic misalignment through causal understanding. |

---

## 八、Google DeepMind Research / DeepMind 重点研究

| Publication | Date | Key Contribution |
|-------------|------|-----------------|
| **From AGI to ASI** | Jun 12, 2026 | Pathways and frameworks for artificial superintelligence |
| **Intelligent AI Delegation** ([arXiv:2602.11865](https://arxiv.org/abs/2602.11865)) | Feb 2026 | Formal delegation framework; 5 requirements: dynamic assessment, adaptive execution, authority transfer, verification, accountability |
| **Towards a Science of Scaling Agent Systems** ([arXiv:2512.08296](https://arxiv.org/abs/2512.08296)) | Dec 2025 | R²=0.37 scaling model for multi-agent architectures |
| **SIMA 2** | 2026 | Agent that plays, reasons, and learns in virtual 3D worlds |
| **Genie 3** | 2026 | General-purpose world model generating diverse interactive environments |
| **Gemini for Science** | May 2026 | AI experiments and tools for scientific discovery (Co-Scientist multi-agent) |
| **Image Generators are Generalist Vision Learners** | Apr 2026 | Image generators as general-purpose vision backbones |
| **ProEval** | Apr 2026 | Proactive failure discovery and efficient performance estimation for generative AI evaluation |
| **Strategic Tradeoffs Between Humans and AI in Multi-Agent Bargaining** | Mar 2026 | Game-theoretic analysis of human-AI collaboration |
| **Realistic honeypot evaluations for scheming propensity** | May 2026 | Evaluating AI agent deception capabilities |
| **Gram: Assessing sabotage propensities via automated alignment auditing** | May 2026 | Automated alignment auditing for sabotage. |

---

## 九、Anthropic Research / Anthropic 重点研究

| Publication | Date | Key Contribution |
|-------------|------|-----------------|
| **Natural Language Autoencoders** | May 7, 2026 | Training Claude to translate its internal thoughts into human-readable text |
| **Teaching Claude Why** | May 8, 2026 | Reducing agentic misalignment through causal reasoning |
| **Project Deal** | Apr 24, 2026 | AI marketplace where Claude buys/sells/negotiates on behalf of employees |
| **What 81,000 People Want from AI** | Mar 18, 2026 | Largest multilingual qualitative study of AI user preferences |
| **Building Effective Agents** | Dec 2024 | Simple, composable patterns; distinction between workflows and agents |
| **Project Fetch Phase 2** | Jun 18, 2026 | Frontier Red Team: advanced cybersecurity agent evaluations |
| **Agentic Coding and Persistent Returns to Expertise** | Jun 16, 2026 | Economic research on AI coding productivity |
| **Making Claude a Chemist** | Jun 5, 2026 | AI agent for chemistry research automation |
| **Measuring LLMs' Impact on N-day Exploits** | Jun 8, 2026 | Cybersecurity risk assessment |

---

## 十、NLP & Benchmarks / 自然语言处理与基准

### ACL 2026 Highlights

| Paper | Key Contribution |
|-------|-----------------|
| **OctoTools** | Multi-agent framework with extensible tools for complex reasoning |
| **Discover and Prove** | Open-source agentic framework for automated theorem proving in Lean 4 |
| **CLEAR** | Cross-lingual enhancement in retrieval via reverse-training |
| **Prefix-Conditioned Supervised Fine-Tuning** | Learning diverse responses with SFT |
| **PosterForest** | Hierarchical multi-agent collaboration for scientific poster creation |

### Notable Benchmarks

| Benchmark | Focus | Key Finding |
|-----------|-------|-------------|
| **ReasonBENCH** | LLM reasoning stability | Evaluates 10 strategies × 12 models × multiple runs; instability patterns generalize across architectures |
| **RecBench+** | LLM recommendation assistants | LLMs good at explicit conditions, struggle with reasoning/misleading info |
| **Infini-gram mini** | n-gram search at internet scale | 83TB indexable; 44% compression ratio; contamination audits |
| **MLRC-Bench** | Machine learning research | Can language agents solve ML research challenges? |
| **DefenderBench** | Cybersecurity agents | Toolkit for evaluating language agents in security environments |

---

## 十一、Key Trends / 关键趋势

### 1. Hybrid Architectures Dominate 2026
Alternating attention + state-space layers (Mamba-2/3, Gated DeltaNet) is the dominant new architecture pattern. Nemotron 3, Qwen3.6, and Mamba-3 all follow this design.

### 2. Test-Time Compute Scaling
From CoT → MCTS → gradient descent in latent space (∇-Reasoner) → evolutionary search (Mind Evolution). The field is shifting from zeroth-order search to first-order optimization at inference time.

### 3. Deflationary Findings Win Awards
"RLVR doesn't expand reasoning," "LLMs lose 39% in multi-turn," "alignment is shallow," "different LLMs collapse to same outputs" — the field rewards puncturing over-claims.

### 4. Agent Systems Enter Formalization
DeepMind's Intelligent AI Delegation, Google's Scaling Agent Systems, and Anthropic's agent safety work represent a maturing of agentic AI from ad-hoc to principled.

### 5. CTR Scaling Laws Become Systematic
ByteDance (TokenMixer-Large, MixFormer, OneTrans), Alibaba (EST, FAT, SORT), Meta (Kunlun, LLaTTE, ULTRA-HSTU), and others are developing rigorous scaling theories for industrial recommendation.

### 6. Generative AI for Recommendation
GenCTR, GE4Rec, GenCI, and AgentRec represent a paradigm shift from discriminative to generative recommendation models, using pre-training + fine-tuning pipelines similar to LLMs.

### 7. Conference Scale Explodes
ICML 2026: 23,918 submissions (vs ~12,000 in 2025). AAAI 2026: ~29,000 submissions. CVPR 2026: 16,092 submissions. The peer review system is under unprecedented strain.

### 8. Feed-Forward Transformers Replace Optimization Pipelines
In 3D vision (CVPR 2026 Best Paper D4RT), feed-forward models now beat optimization-based bundle adjustment — a second "ImageNet moment" for 3D.

---

## 十二、arXiv Notable Preprints (Jan–Jun 2026)

| Category | Paper | Link |
|----------|-------|------|
| Architecture | Nemotron 3 Super (NVIDIA) | [2604.12374](https://arxiv.org/abs/2604.12374) |
| Architecture | Mamba-3 | [2603.15569](https://arxiv.org/abs/2603.15569) |
| Architecture | Gated DeltaNet-2 | [2605.22791](https://arxiv.org/abs/2605.22791) |
| Architecture | Scaling Embeddings Outperforms Scaling Experts | [2601.21204](https://arxiv.org/abs/2601.21204) |
| Reasoning | ∇-Reasoner (ICLR 2026 Oral) | [OpenReview](https://openreview.net/forum?id=pEJAja73dk) |
| Agents | Intelligent AI Delegation (DeepMind) | [2602.11865](https://arxiv.org/abs/2602.11865) |
| Agents | ACE: Agentic Context Engineering (Stanford) | [2510.04618](https://arxiv.org/abs/2510.04618) |
| Agents | LLM-powered Agents for Recommender Systems Survey | [2502.10050](https://arxiv.org/abs/2502.10050) |
| RL | Does RL Really Incentivize Reasoning? (Tsinghua) | [2504.13837](https://arxiv.org/abs/2504.13837) |
| RL | 1000 Layer Networks for SSL RL (NeurIPS 2025 Best) | [2503.14858](https://arxiv.org/abs/2503.14858) |
| Diffusion | Why Diffusion Models Don't Memorize (NeurIPS 2025 Best) | [2505.17638](https://arxiv.org/abs/2505.17638) |
| NLU | Transformers are Inherently Succinct (ICLR 2026 Outstanding) | [2510.19315](https://arxiv.org/abs/2510.19315) |
| NLP | Infini-gram mini (EMNLP 2025 Best) | [2506.12229](https://arxiv.org/abs/2506.12229) |
| NLP | PAFT: Prompt-Agnostic Fine-Tuning (EMNLP 2025 Outstanding) | [2502.12859](https://arxiv.org/abs/2502.12859) |
| RecSys | GenCTR: Generative CTR (Alibaba, KDD 2025) | — |
| RecSys | RecBench+ (WSDM 2026) | [2503.09382](https://arxiv.org/abs/2503.09382) |
| Attention | Gated Attention for LLMs (Alibaba Qwen, NeurIPS 2025 Best) | [2505.06708](https://arxiv.org/abs/2505.06708) |
| Alignment | Safety Alignment Should Be Deeper (ICLR 2025 Outstanding) | [2406.05946](https://arxiv.org/abs/2406.05946) |
| Alignment | Learning Dynamics of LLM Finetuning (ICLR 2025 Outstanding) | [2407.10490](https://arxiv.org/abs/2407.10490) |

---

## 十三、Source Links / 信息来源

- AAAI 2026: [Proceedings](https://ojs.aaai.org/index.php/AAAI/issue/view/683) | [Highlights](https://resources.paperdigest.org/2026/01/aaai-2026-papers-highlights/) | [Bohrium Analysis](https://www.bohrium.com/en/blog/research-notes/aaai-2026-accepted-papers-highlights)
- ICLR 2026: [Papers](https://iclr.cc/virtual/2026/papers.html) | [Outstanding](https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/) | [Full List](https://kmno4-zx.github.io/iclr26-all-papers)
- CVPR 2026: [Papers](https://cvpr.thecvf.com/virtual/2026/papers.html) | [Highlights](https://resources.paperdigest.org/2026/04/cvpr-2026-papers-highlights/) | [Best Papers](https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers) | [Bohrium](https://www.bohrium.com/en/blog/research-notes/cvpr-2026-accepted-papers-highlights/)
- ICML 2026: [Highlights](https://resources.paperdigest.org/2026/05/icml-2026-papers-highlights/) | [Paper Notes](https://en.papernotes.org/ICML2026/)
- NeurIPS 2025: [Highlights](https://resources.paperdigest.org/2025/11/neurips-2025-papers-highlights/) | [Best Papers](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)
- EMNLP 2025: [Proceedings](https://aclanthology.org/events/emnlp-2025/) | [Highlights](https://resources.paperdigest.org/2025/11/emnlp-2025-papers-highlights/)
- ACL 2026: [Accepted Papers](https://2026.aclweb.org/program/accepted_papers/)
- KDD 2026: [Proceedings V.1](https://dl.acm.org/doi/proceedings/10.1145/3770854)
- SIGIR 2026: [Accepted Papers](https://sigir2026.org/en-AU/pages/program/accepted-papers)
- DeepMind: [Publications](https://deepmind.google/research/publications)
- Anthropic: [Research](https://www.anthropic.com/research)
- Sebastian Raschka's LLM 2026 List: [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/llm-research-papers-2026-part1)
- Notable Papers Reading List: [backpropagation.ai](https://backpropagation.ai/posts/notable-papers-icml-iclr-neurips-cvpr-emnlp-2025-2026)
- ICML 2026 by PaperNotes: [1846 Notes](https://en.papernotes.org/ICML2026/)
