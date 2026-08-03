---
title: arXiv Paper Check — AI & CTR (August 3, 2026)
type: synthesis
created: 2026-08-03
updated: 2026-08-03
sources: [arxiv-cs.AI, arxiv-cs.IR, arxiv-cs.LG, arxiv-cs.CL]
tags: [arxiv, daily-check, ai, ctr, recommendation, ads, reasoning, rl, agents]
---

# arXiv Paper Check — AI & CTR (August 3, 2026)

> Curated from the Mon, Aug 3, 2026 arXiv listing (cs.AI 146 new, cs.LG 137, cs.IR 15, cs.CL 68). 26 papers curated. arXiv IDs in parentheses.

## 🔥 Highlights

### CTR, Recommendation & Advertising

| Paper | Authors | Key Contribution |
|-------|---------|------------------|
| **TransX** (2607.28940) | Da Xu, Liyan Fang, Divya Venugopalan, et al. (LinkedIn) | Production encoder-decoder that reformulates recommendation as seq2seq *action transduction*: explicitly decouples nearline behavior-stream modeling from real-time serving events and conditions next-action decoding on cross-attention between them. Co-designed amortized serving (incremental behavior encoding + per-request KV caching) makes latency insensitive to sequence length. Online A/B: **+6.0% CTR, +4.4% conversion, ~80% online compute reduction**. |
| **PaletteID** (2607.29000) | Huanyu Liu, Baining Chen, Hui Liu, et al. | Prototype-composed Semantic Identifiers for multimodal CTR: builds a prototype "palette" via Semantic Quality-Aware Determinantal Point Process (SQ-DPP), then aggregates a retrieved sequence of semantically related prototypes per item. Preserves fine-grained continuous signal lost by residual codebook SIDs, scales better than prefix-dependent hierarchical IDs, and gives larger gains on long-tail items with more interpretable tokens. |
| **EvoReason** (2607.29010) | Zhuang Zhuang, Zhipeng Wei, Rongfeng Guo, et al. | Self-evolving *reasoning-primitive*-guided on-policy distillation for latent reasoning in generative recommendation. Extracts reusable reasoning primitives from agentic trajectories, has the teacher reason with them (less redundant, more consistent CoT), then runs a closed-loop co-evolution where supervision adapts to the student's latent reasoning outcomes — fixing raw-CoT-distillation's redundant/unstable supervision. |
| **GALA** (2607.29213) | Jiping Liu, Zhongmin Zhang, Zisen Sang, et al. (Taobao Shangou) | Three-stage multimodal pipeline for food-delivery rec (200M+ DAU): behavior-aware triplet pretraining → a novel intermediate **"generative RL alignment"** stage that refines embeddings via conversion-reward GRPO → adaptive gating with hybrid loss. +0.12/+0.20 AUC offline; **+0.55% order volume** in large-scale online A/B. |
| **Think2Go** (2607.28997) | Zhuang Zhuang, Shanshan Feng, Hangwei Qian, et al. | Generative next-POI recommendation that unifies SFT and RL-based reasoning in one architecture, with two advantage-weighting calibrators: kernel-density *prompt epistemic uncertainty* (promote exploration when query-history alignment is weak) and *reward-informed advantage scaling* (normalize by reward max). Implicit instance-aware curriculum prevents entropy collapse. |
| **SnapLGR** (2607.28895) | Liam Collins, Jiwen Ren, Donald Loveland, et al. (Snapchat) | Full production LLM-based generative retrieval for short-video rec: PPR-co-engagement contrastive learning on multimodal SIDs (better codebook utilization, fewer collisions), continued pretraining to ground SID tokens before SFT, TensorRT-LLM CUDA beam search + decentralized worker-loop serving. Live A/B: +0.37% View Time, +0.18% Deep Sessions vs the TIGER-style baseline. |
| **RecHarness** (2607.29241) | Haoran Ling, Yuecheng Li, Zeyu Song, et al. | Bandit-routed agentic harness for *automated recommender optimization*: a bandit router picks the next modification direction from historical validation feedback while the LLM only generates the hypothesis + executable code edit within that direction. Jump-basin arm triggers structural jumps when local edits stagnate. 7-day online A/B on short-video ads: **+2.084% ADVV, +0.534% Revenue, +0.559% Exposure**. |
| **GenCDSR** (2607.28659) | Yuxuan Hu, Yuhao Wang, Tianbo Huang, et al. | Cross-domain sequential recommendation via hybrid tokenization (multi-tower shared-specific + fine-grained codebooks capturing cross-domain commonalities vs domain-specific distinctions) and a **serial-parallel decoding** strategy exploiting hierarchical SID structure. +1.5% accuracy and **-85.1% inference latency** vs SOTA. |
| **MerchantBench** (2607.28956) | Qiming Shi, Yulong Tao, Linbo Jin, et al. | 365-day order-level e-commerce simulation grounded in 98,843 real product records, 26 tools, evaluating LLM agents on *Long-Term Coherence* (sourcing, listing/pricing, cash-flow, mixed-latency feedback). Across 8 LLMs × 2 frameworks × 48 runs, the best LLM reaches only **27.3% of human mean final net assets** — a stark agent-human gap on long-horizon operational tasks. |

### LLM Reasoning & RL Post-Training

| Paper | Authors | Key Contribution |
|-------|---------|------------------|
| **PRISM — Don't Mix Rewards, Mix Policies** (2607.29246) | Ruiming Liang, Yi Zhong, Yizhen Yuan, et al. | Multi-reward RL via *policy-space decomposition and composition*: optimize a set of standalone positive policies plus one global negative policy instead of fusing rewards. Avoids alignment-tax conflicts between objectives and adds inference-time controllability by flexible policy composition. Wins on scientific reasoning, tool-use, and helpfulness-safety alignment. |
| **LatentRM** (2607.29185) | Sanwoo Lee, Clive Bai, Hsiu-Yuan Huang, et al. | Reward modeling that learns intermediate reasoning traces as **discrete latent variables** to explicitly maximize downstream scalar reward likelihood (on-policy, end-to-end). Unifies the robustness of generative RMs with the probabilistic interpretability of scalar RMs; beats scalar, generative, and hybrid RMs on preference modeling, OOD tasks, and RLHF. |
| **TwT — Translation with Thought** (2607.29287) | Yongshi Ye, Biao Fu, Chongxuan Huang, et al. | Resource-rational translation: learns to modulate between intuitive and deliberate reasoning per-domain difficulty. SFT on difficulty-aware long-CoT traces distilled from DeepSeek-R1 / rewritten by GPT-4o, then RL with a hybrid quality-efficiency reward. TwT-7B/14B beat much larger SOTA reasoning models across 15 benchmarks + 59 unseen languages while cutting token use **32–60%**. |
| **CaRL — Knowing When to Quit** (2607.29211) | Xinyan Guan, Jiali Zeng, Chunlei Xin, et al. | Diagnoses *futile reasoning* (expensive but semantically void reasoning on beyond-capability tasks, dominated by "specious reasoning") and finds capability-behavior miscalibration. Capability-aligned RL: reward shaping that incentivizes refusal over futile reasoning + hindsight refusal augmentation — cuts futile reasoning while preserving performance. |
| **SAF-OPD** (2607.29209) | Yifan Ding, Xincheng Wei, Yoshua Y. Li, et al. | Diagnoses why GRPO+OPD advantage fusion collapses: magnitude mismatch (token-level OPD advantages spike past bounded RLVR advantages) + temporal mismatch (persistent teacher pull limits surpassing it). Fixes with a four-stage sparsify-then-compress + warm-up-then-anneal pipeline. On Qwen3-1.7B/4B/8B, +0.51–2.70% aggregate over fixed-coefficient fusion with stable training. |
| **Adaptive FastOPD** (2607.29494) | Qian Tan, Huaifei Liang, Xuanyu Zhu, et al. | Progress-aware rollout-horizon expansion: only extends the OPD horizon when learning near the boundary plateaus (measured by four teacher–student signals relative to entry values) and the current horizon is sufficiently used. Cuts training time **49.1–71.2%** vs OPD 15K at equal-or-better quality, robust to hyperparameters. |
| **DASH-OPD** (2607.29078) | Yuchen Xia, Qianguo Sun, Chao Song, et al. | Discrepancy-aware switching with hysteresis for multi-turn agent OPD: accumulates normalized student-teacher log-probability-ratio evidence over turns and switches executors (student↔teacher) bidirectionally only past thresholds, preventing high-frequency flips. Beats baselines on ALFWorld with better train/deploy efficiency. |
| **WCM — World Critic Model** (2607.29613) | Senyu Fei, Xiaopeng Yu, Siyin Wang, et al. | Fixes VLA-RL critic partial observability: a lightweight **LeJEPA** critic that jointly predicts future latent states and estimates values, so the representation captures temporal dynamics instead of regressing scalar returns. Seamless with Pi0/Pi0.5/OpenVLA-OFT; SOTA on 149 tasks/4 benchmarks (in- and out-of-distribution) and 7 real-world manipulation tasks. |

### Agents & Agent Evaluation

| Paper | Authors | Key Contribution |
|-------|---------|------------------|
| **SESA — Self-Play Meets Skill Evolution** (2607.29468) | Zenghuang Fu, Zhaoyang Li, Qiuyuan Ai, et al. | Self-Evolving Skill-Augmented Agent: challenger poses problems, solver alone retrieves skills; informative failures are distilled into reusable skills written back to memory, which reshapes the challenger's reward and the future problem distribution — task generation and skill memory *co-evolve*. +1.2–3.2 pts over SSP across 7 QA benchmarks; gains persist in model weights (memory-free deployment). |
| **MAGA** (2607.29320) | Hang Yan, Zhangxuan GU, Beitong Zhou, et al. | Multi-platform GUI agent self-fusion via *structured action distillation*: merges mobile/web/desktop experts by re-allocating distillation signal toward erroneous action tokens (the only environment interface) and adding a training-only hint. Beats weight-merging and vanilla OPD; +2.0% mean success vs strongest baseline at 8B. |
| **AgentHPOBench** (2607.29626) | Tianyu Huai, Tingshuo Fan, Xinchi Chen, et al. | Benchmark for LLM agents as *sequential hyperparameter optimizers*: 30 executable ML tasks / 7 categories, each starting from a validated baseline where the agent observes accumulated configs/metrics/logs before each intervention. 12 agents evaluated — real experimental-optimization ability, but weak at sustained iterative refinement and complex log diagnosis. |
| **Zero-Mem** (2607.29377) | Yilin Xiao, Zhehan Zhu, Yujing Zhang, et al. | Zero-token memory operations for LLM agents: preserves raw interaction traces, organized as an entity–context graph plus a temporal hierarchy, with deterministic calibration discarding conflicting evidence — **no LLM call or token spent outside final QA**. -57.6% memory-operation time vs fastest baseline at competitive accuracy on long-memory benchmarks. |
| **Model or Harness?** (2607.28802) | Harsh Raj, Vipul Gupta, Anas Mahmoud, et al. | Interaction-centric taxonomy to *localize* agent failures: 41 failure modes assigned to edges between model/harness/user/tool/memory/environment with a fault side indicating where the repair belongs. Model-side → post-training, harness-side → scaffolding/tools, environment/grader → redesign. Reproducible: strongest judge reaches κ=0.76 vs human labels across four frontier models. |

### Serving, Memory & Efficiency

| Paper | Authors | Key Contribution |
|-------|---------|------------------|
| **TokTier** (2607.29678) | Zhenyu Zhang, Zhichao Cao | Exact *stateful tokenization* service for agentic serving: re-tokenizes a small window around appends, splices after a per-request stable-boundary check (window-widening fallback); GPU regex+BPE for cold starts; shadow verifier on live traffic. Zero divergence over 1.5×10¹⁰ split checks / 12.4 TB corpus; incremental repair **437× faster than HF**; median TTFT down 16–34%, P99 -23% with vLLM. |
| **ResKV** (2607.29591) | Yuhang Zhan, Lisi Chen, Shuo Shang | Fixed-budget KV compression that *reconstructs omitted attention contributions*: splits the budget into an exact main cache + compact residual cache participating in the same softmax normalization (restoring both numerator and denominator mass), with a construction-time validation proxy for allocation and a decode-time dynamic gate. Broad gains over eviction/merging baselines under the same budget on LongBench/RULER. |
| **DeltaServe** (2607.28848) | Jiaxuan Chen, Jianshu She, Ye Yuan, et al. | Host-agnostic co-serving that converts idle inference capacity into **LoRA fine-tuning throughput** while preserving inference SLOs, via a compact multi-LoRA-batching hook + SLO-aware scheduler driven by a CUDA-graph-aware latency model. On a production trace: **2.9× fine-tuning throughput vs LLMStation at 100% SLO compliance** (vs 85%), no extra hardware. |
| **TransMem** (2607.29032) | Haodong Lei, Junming Liu, Yirong Chen, et al. | Inference-time parametric memory that transforms *sparse historical hidden states* of a frozen LLM into reusable memory via a lightweight gating network, trained by evidence-conditioned self-distillation (memory-augmented student ↔ evidence-only teacher). +11.58–29.25 F1 on LoCoMo, +10.20–13.03 F1 on HotpotQA, MemoryAgentBench 29.54%→40.00%. |

### Evaluation & Interpretability

| Paper | Authors | Key Contribution |
|-------|---------|------------------|
| **Safety, or Just Capability?** (2607.28685) | Youting Wang, Xiao Han, Dingyan Shang, et al. | Validity audit of four agent-safety benchmarks (R-Judge, InjecAgent, AgentHarm, AgentDojo) on up to 41 models. Metric artifact: on any F1-scored trace-judgment benchmark an "always positive" policy scores F1=2π/(1+π); on R-Judge that's 0.690, above 5 of 21 discriminating models. Ranking depends on small-panel artifacts; capability predicts task success (ρ=+0.60) but negatively correlates with misalignment safety. Verdict: name the benchmark, metric, target behavior, and panel for any safety claim. |
| **Reflection or Re-Generation?** (2607.28908) | Yefan Tao, Gerald Friedland, Madhusudhanan Chandrasekaran, et al. | Controlled two-pass Human-LLM Reflection Framework (HRF) + per-iteration cross-entropy analysis: LLM "reflection" yields ~zero information gain on objective tasks (indistinguishable from re-sampling) and *negative* gain on subjective ones, while human revision improves both. Cross-agent tests localize the failure to the revision step — structurally, self-conditioned revision cannot reduce target uncertainty. Direct follow-up to the "Sample More, Reflect Less" result. |
| **SARE — Step-Aware Reasoning Energy** (2607.28674) | Hui Wei, Junda Wu, Sheldon Yu, et al. | Geometric (CKA-based) measure of reasoning effort per CoT step across transformer layers. Energy is highly non-uniform with phase-like transitions invisible to trajectory-level metrics; incorrect trajectories show lower energy at critical junctions; SARE features match or beat output-confidence baselines for prediction. |

## 📊 Summary Statistics

- **Total curated**: 26 papers (from cs.AI 146 / cs.LG 137 / cs.IR 15 / cs.CL 68 new; 281 unique across categories)
- **CTR, Recommendation & Advertising**: 9 papers
- **LLM Reasoning & RL Post-Training**: 8 papers
- **Agents & Agent Evaluation**: 5 papers
- **Serving, Memory & Efficiency**: 4 papers (incl. TransMem)
- **Evaluation & Interpretability**: 3 papers

## 🔑 Key Trends

1. **OPD has become a mature, industrialized recipe**: three new variants attack its failure modes head-on — SAF-OPD (advantage magnitude/temporal mismatch), Adaptive FastOPD (efficiency: -49–71% training time), DASH-OPD (multi-turn hysteresis) — while EvoReason imports on-policy distillation into generative recommendation's latent reasoning. The privileged-teacher debate from the Aug 1 check continues to consolidate into engineering.
2. **RL post-training shifts from reward-space to policy/latent space**: PRISM composes policies instead of rewards for multi-reward control; LatentRM turns reasoning traces into latent variables to teach scalar reward models end-to-end; CaRL shapes rewards to teach *when to refuse* rather than push capability.
3. **Rec ranking stays on the "scale within a serving budget" frontier**: TransX (LinkedIn, -80% compute / +6.0% CTR via behavior/serving stream separation + amortized serving), SnapLGR (production LLM generative retrieval at Snapchat), RecHarness (bandit-routed agentic auto-optimization) — plus semantic-identifier innovation for multimodal/long-tail CTR (PaletteID).
4. **Agent evaluation is moving from outcomes to interactions and long horizons**: Model-or-Harness (41 failure modes localized to components), the agent-safety validity audit (metric/panel artifacts), AgentHPOBench (sequential evidence interpretation), and MerchantBench (long-term coherence; best LLM at 27.3% of human performance) all treat evaluation as a measurement problem.
5. **Serving infrastructure is optimizing the whole agent loop, not just KV**: TokTier makes *tokenization* stateful (TTFT -16–34%), ResKV reconstructs rather than discards evicted attention, DeltaServe farms idle inference GPUs for fine-tuning — the cost structure of long-lived agent sessions is now the optimization target.
6. **LLM reflection keeps losing to structural arguments**: Reflection-or-Re-Generation gives an information-theoretic account (self-conditioned revision cannot reduce uncertainty, ΔI≈0/negative) reinforcing the "Sample More, Reflect Less" finding — an increasingly robust negative result for method-driven eval narratives.
