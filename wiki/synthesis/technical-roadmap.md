---
title: Technical Roadmap — AI Research Directions (2025-2026)
type: synthesis
created: 2026-05-25
updated: 2026-05-25
sources: [arxiv-broad-2026-05-25.md]
tags: [roadmap, knowledge-distillation, rl-alignment, moe-scaling, generative-rec, agent-skills, code-execution]
---

# Technical Roadmap — AI Research Directions (2025-2026)

> Analysis of ~121 recent papers organized by technical route, tracing the evolution of each direction.

---

## 1. Knowledge Distillation Route

### Evolution

```
2024: Static KD (teacher logits) 
  → 2025: On-policy distillation (GKD)
    → 2026: Adaptive curriculum distillation (PACED)
      → 2026: Cross-architecture distillation (CAB: Transformer→Mamba)
        → 2026: Low-rank KD theory (convergence + generalization bounds)
```

### Key Papers

| Paper | Date | Technique | Result |
|-------|------|-----------|--------|
| PACED (2603.11178) | Mar 2026 | Beta-kernel pass-rate weighting | +9.8 MATH-500, +13.6 AIME 2025; near-zero forgetting on MMLU |
| Low-Rank KD Theory (2603.22355) | Mar 2026 | Theoretical framework for LRC | Convergence O(1/√T); optimal rank r* = O(√n) |
| CAB Distillation | ICLR 2026 | Attention Bridge for Transformer→SSM | First token-level cross-architecture distillation |
| UNICOMP (2602.09130) | Feb 2026 | Unified compression evaluation | KD has weaker reliability preservation vs pruning/quantization |
| HARNESS-LM (2605.23572) | May 2026 | SLM distillation for sponsored search | Microsoft Bing Ads deployment |

### Open Problems
- Theoretical gap between on-policy and off-policy distillation
- Cross-architecture distillation at scale (Transformer→Mamba for 70B+ models)
- Distillation for reasoning chains vs. final outputs

---

## 2. RL Alignment Route

### Evolution

```
2024: RLHF / DPO
  → 2025: GRPO / Reinforce++ (critic-free)
    → Early 2026: Process reward models / turn-level critics
      → Mid 2026: Credit assignment methods (47 papers surveyed)
        → 2026: Agentic RL (multi-turn POMDP framing)
```

### Key Papers

| Paper | Date | Technique | Result |
|-------|------|-----------|--------|
| SPINAL (2601.06238) | Jan 2026 | DPO alignment geometry diagnostic | Terminal decoder block calibration; cross-model audit tool |
| Topology-Enhanced Alignment (2605.07172) | May 2026 | Persistent homology regularization | Outperforms non-topological baselines on UltraChat |
| TMPC (ICLR 2026) | Apr 2026 | MPC-inspired test-time alignment | Hierarchical RL for inference-time steering |
| Credit Assignment Survey (2604.09459) | Apr 2026 | Taxonomy of 47 CA methods | 3 independent hindsight/counterfactual papers in one week (Mar 2026) |
| SAMPO (2602.21534) | Feb 2026 | Stable agentic policy optimization | 25.2% improvement over GRPO; stability analysis |
| SML (2602.16488) | Feb 2026 | Social meta-learning via online RL | Cross-domain transfer (math→code); online RL > SFT |
| Efficient Exploration (2603.17378) | Mar 2026 | RLHF scaling laws | Online uncertainty-guided exploration; first systematic RLHF scaling study |

### Convergence Signal
The field is converging on **hindsight/counterfactual credit assignment** as the natural paradigm for agentic RL. Three independent papers (HCAPO, C3, CCPO) appeared within a single week in March 2026.

---

## 3. MoE Scaling Route

### Evolution

```
2024: DeepSeekMoE (fine-grained routing)
  → 2025: Qwen3 MoE / DeepSeek-V2/V3
    → Early 2026: Megatron Core MoE, Arcee Trinity Large
      → Mid 2026: FineRMoE (output dimension), MOUE (virtual width)
        → 2026: HyperP (hypersphere LR transfer), Swimba (MoE + SSM)
```

### Key Papers

| Paper | Date | Technique | Result |
|-------|------|-----------|--------|
| Megatron Core MoE (2603.07685) | Mar 2026 | Systems: FP8, NVFP4, Parallel Folding | 1,233 TFLOPS/GPU for DeepSeek-V3-685B |
| HyperP (2603.28743) | Mar 2026 | Hypersphere LR transfer; SqrtGate | 1.58× CEL; 3.38× for MoE at 13.3B |
| FineRMoE (2603.13364) | Mar 2026 | Fine-grained → output dimension | 6× parameter efficiency; 281× lower prefill latency |
| MOUE (2603.04971) | Mar 2026 | Virtual Width via depth-width transformation | Up to 4.2% gains over MoE baselines |
| Arcee Trinity Large (2602.17004) | Feb 2026 | 685B MoE; SMEBU; Muon optimizer | Open-weight; 17T tokens pre-training |
| Swimba (2603.06938) | Mar 2026 | MoE-parameterized SSM | Single-pass recurrence; 14B model |
| Batch Size Scheduling (2602.14208) | Feb 2026 | Late-switch BSS for MoE | Consistent outperformance across dense and MoE |

### Scaling Dimensions Discovered
1. **Fine-grained intermediate dimension** → saturation at threshold
2. **Output dimension** (FineRMoE) → new scaling axis
3. **Virtual Width** (MOUE) → depth→width conversion
4. **Expert count + sparsity** (Swimba) → MoE-SSM hybrid

---

## 4. Unified Ranking Route (Recommendation + CTR)

### Evolution

```
2024: DLRM / DCNv2 (separate feature interaction + sequence)
  → 2025: OneTrans, LONGER (unified backbones)
    → Early 2026: GRAB, CADET, OneRanker (generative ranking)
      → Mid 2026: GR4AD, OneRec-V2, OneMall (end-to-end generative)
        → 2026: LoopCTR (recursive computation scaling)
```

### Key Papers

| Paper | Date | Architecture | Online Gain |
|-------|------|-------------|-------------|
| GRAB (Baidu, 2602.01865) | Feb 2026 | Generative CTR + CamA | +3.05% CPM, +3.49% CTR |
| CADET (LinkedIn, 2602.11410) | Feb 2026 | Decoder-only with context conditioning | +11.04% CTR |
| OneRanker (Tencent, 2603.02999) | Mar 2026 | Unified generation + ranking | +1.34% GMV |
| GR4AD (Kuaishou, 2602.22732) | Feb 2026 | UA-SID + LazyAR + RSPO | +4.2% ad revenue |
| OneMall (Kuaishou, 2601.21770) | Jan 2026 | E2E generative for e-commerce | +14.7% GMV |
| LONGER (ByteDance, 2505.04421) | Jul 2025 | Long-sequence transformer | Deployed at Douyin |
| LoopCTR (2604.19550) | Apr 2026 | Train-multi-loop, infer-zero-loop | 0.02-0.04 AUC headroom |
| RankUp (Tencent, 2604.17878) | Apr 2026 | High-rank representation | +3.41-4.81% GMV |
| HeMix (Alibaba, 2602.09387) | Feb 2026 | Query-mixed extraction + HeteroMixer | +3.61% GMV |

### Convergence Pattern
The industry is converging on a **unified generative architecture** where:
- One model handles retrieval + ranking (OneRanker, GR4AD)
- Autoregressive decoding replaces pointwise scoring (CADET, GRAB)
- Scaling laws emerge for CTR just as in LLMs (EST)
- RL fine-tuning replaces supervised fine-tuning (GFlowGR, GR4AD's RSPO)

---

## 5. Agent Skill Optimization Route

### Evolution

```
2024: ReAct / Reflexion (prompt-based agents)
  → 2025: Tool-use fine-tuning (Gorilla, ToolLLM)
    → Early 2026: SkillOpt, EVE-Agent (self-evolving skills)
      → Mid 2026: AgentArk (multi-agent → single-agent distillation)
        → 2026: Mass, AgentConductor (topology optimization)
```

### Key Papers

| Paper | Date | Route | Contribution |
|-------|------|-------|-------------|
| SkillOpt (2605.23904) | May 2026 | Self-evolving agent skills | Microsoft Research Asia; structured optimization for skill acquisition |
| EVE-Agent (2605.22905) | May 2026 | Evidence-verifiable self-evolution | Formal guarantees on agent improvement |
| AgentArk (2602.03955) | Feb 2026 | Multi-agent→single-agent distillation | Three hierarchical distillation strategies |
| Mass (2502.02533) | Feb 2025 | Automated prompt+topology optimization | Local→global optimization stages |
| AgentConductor (2602.17100) | Feb 2026 | RL-optimized dynamic topology | 14.6% pass@1 improvement; 68% token cost reduction |
| Agent Q-Mix (2604.00344) | Apr 2026 | MARL for topology selection | 20.8% on HLE with Gemini backbone |
| SAMPO (2602.21534) | Feb 2026 | Stable agentic policy optimization | 25.2% improvement over GRPO |

### Key Insight
The field is moving from **manually designed agent workflows** toward **learned topologies** where an orchestrator is trained via RL to dynamically construct interaction graphs per task.

---

## 6. Code Execution Prediction & Program Repair Route

### Evolution

```
2024: Standard APR (LLM-based patch generation)
  → 2025: Feedback-based repair (ChatRepair, ThinkRepair)
    → Early 2026: Execution-grounded repair (DynaFix, Verify Before You Fix)
      → Mid 2026: Multimodal repair (SVRepair, FailureMem)
        → 2026: Memory-augmented repair (ExpeRepair)
          → 2026: Specification inference (Prometheus)
```

### Key Papers

| Paper | Date | Technique | Benchmark Result |
|-------|------|-----------|-----------------|
| DynaFix (2512.24635) | Dec 2025 | ByteTrace execution traces | Closed-loop dynamic feedback |
| SVRepair (2602.06090) | Feb 2026 | Structured visual reasoning | 36.47% on SWE-Bench M; 95.12% on CodeVision |
| SYNTHFIX (2604.17184) | Apr 2026 | Neuro-symbolic; adaptive SFT/RFT | 18% CodeBLEU improvement; 32% Exact Match |
| DebugRepair (2604.19305) | Apr 2026 | Simulated instrumentation | 51.3% more bugs fixed than vanilla |
| FailureMem (2603.17826) | Mar 2026 | Failure Memory Bank | +3.7% on SWE-Bench M over GUIRepair |
| Verify Before You Fix (2604.10800) | Apr 2026 | uAST + execution validation | 69.74% resolution; 131.7% fewer unnecessary repairs |
| ExpeRepair (2506.10484) | Jun 2025 | Dual-memory (episodic + semantic) | 74.6% pass@1 on SWE-Bench Verified |
| Prometheus (2604.17464) | Apr 2026 | BDD specification inference | 93.97% correct patch rate on Defects4J |
| ReinFix (2506.23100) | Jun 2025 | Repair ingredients search | 146 bugs fixed on Defects4J V1.2 |

### Convergence Pattern
Program repair is evolving from **code generation** toward **specification inference** (Prometheus: "fix this bug" → "reverse-engineer the missing requirement"). Execution grounding is becoming mandatory, and multimodal inputs (screenshots, GUI) are now being incorporated.

---

## 7. Diffusion Models Route

### Evolution

```
2024: DiT / SD3 / FLUX (static computation)
  → 2025: Long video (Self-Forcing, LongLive)
    → Early 2026: Efficient diffusion (DyDiT++, Drift-AR)
      → Mid 2026: Hybrid AR-Diffusion (GPDiT, Causal Forcing)
        → 2026: MLLM-guided generation (Bernini)
          → 2026: Inference-time scaling (LatSearch, Meta Flow Maps)
```

### Key Papers

| Paper | Date | Technique | Result |
|-------|------|-----------|--------|
| ViBe (2603.23326) | Mar 2026 | Image-only training; Relay LoRA | Outperforms high-res video-trained models |
| GPDiT (2505.07344) | May 2025 | AR diffusion in continuous space | Unifies AR + diffusion for video |
| PixelGen (2602.02493) | Feb 2026 | Pixel diffusion with perceptual loss | FID 5.11 on ImageNet-256; no VAE needed |
| DyDiT++ (2504.06803) | Apr 2025 | Timestep/spatial dynamic width | 51% FLOPs reduction; 1.73× speedup |
| Bernini (2605.22344) | May 2026 | MLLM planner + DiT renderer | SOTA video generation and editing |
| LatSearch (2603.14526) | Mar 2026 | Latent reward-guided search | Improved VBench-2.0 over Wan2.1 |
| Causal Forcing (2602.02214) | Feb 2026 | AR teacher ODE distillation | 19.3% Dynamic Degree improvement |
| Meta Flow Maps (2601.14430) | Jan 2026 | Stochastic one-step posterior sampling | Beats Best-of-1000 at fraction of compute |

### Key Trend
The boundary between **autoregressive** and **diffusion** models is blurring. GPDiT, Drift-AR, and Causal Forcing all explore hybrid AR-diffusion designs. MBLLM-guided generation (Bernini) suggests a future where a language model plans and a diffusion model renders.

---

## 8. SSM and Efficient Sequence Modeling Route

### Evolution

```
2024: Mamba-1 / Mamba-2 (pure SSM)
  → 2025: Hybrid Transformer-Mamba (Jamba, TransMamba)
    → Early 2026: Mamba-3 (complex-valued states, MIMO)
      → Mid 2026: MoE-SSM (Swimba), GSP-SSM (HADES)
        → 2026: Attention-in-recurrence (Sessa)
```

### Key Papers

| Paper | Date | Technique | Result |
|-------|------|-----------|--------|
| Mamba-3 (2603.15569) | Mar 2026 | Complex-valued state; MIMO | 1.8 pp accuracy gain over Gated DeltaNet at 1.5B |
| InfoMamba (2603.18031) | Mar 2026 | Concept-bottleneck filtering + SSM | Outperforms Transformer and SSM baselines |
| TransMamba (2503.24067) | Mar 2025 | Sequence-level hybrid with shared params | Superior efficiency vs. single/hybrid baselines |
| Swimba (2603.06938) | Mar 2026 | MoE-parameterized SSM | Improved avg. performance at 14B |
| HADES (2603.22333) | Mar 2026 | GSP-inspired hierarchical filter bank | 58.9% parameters of Mamba2 |
| Sessa (2604.18580) | Apr 2026 | Attention in recurrence feedback path | Power-law memory tails; flexible selective retrieval |
| Understanding Mamba (2506.11891) | Jun 2025 | S6 = Haar wavelet projection | Analytical solutions to MQAR |
| LongMamba (2504.16053) | Apr 2025 | Training-free receptive field expansion | Extended long-context capability |
| CAB Distillation | ICLR 2026 | Transformer→Mamba knowledge transfer | Data-efficient SSM training |

### Key Insight
The field is converging on **hybrid architectures** that combine SSM efficiency with attention's retrieval capability. Pure SSMs (Mamba-3) are improving but hybrids (TransMamba, InfoMamba) currently offer the best trade-off.

---

## 9. Evaluation & Benchmarking Route

### Evolution

```
2024: Static leaderboards (Open LLM Leaderboard)
  → 2025: Redundancy analysis, saturation detection
    → 2026: Skill-based evaluation (factor analysis)
      → 2026: Interactive/user-defined evaluation
        → 2026: Metacognition benchmarks
```

### Key Papers

| Paper | Date | Technique | Finding |
|-------|------|-----------|---------|
| Benchmark Saturation (2602.16763) | Feb 2026 | Saturation analysis across 60 benchmarks | Nearly half saturated; hidden test data shows no protective effect |
| Benchmark Redundancy (2603.00394) | Mar 2026 | PCA on 6 standard benchmarks | 2 PCs explain 97.4% variance; ARC + TruthfulQA sufficient |
| IQ Test for LLMs (2507.20208) | Jul 2025 | Factor analysis on 60×44 models | 8 latent skills; scale ≠ skill specialization |
| Interactive Leaderboards (2604.21769) | Apr 2026 | LMArena dataset analysis | Heavy topic skew; model rankings vary across prompt slices |
| MEDLEY-BENCH (2604.16009) | Apr 2026 | Metacognition benchmark | Scale buys evaluation but not control |
| RubricEval (2603.25133) | Mar 2026 | Rubric-level meta-evaluation | GPT-4o only 55.97% on Hard subset |
| GraphOmni (2504.12764) | Apr 2025 | Graph reasoning benchmark | 241K samples; models far from human performance |

### Key Insight
The benchmark community is moving from **aggregate scores** toward **structured evaluation** (skill decomposition, interactive leaderboards). The redundancy finding (2 PCs explain 97% variance) has practical implications for evaluation cost reduction.

---

## Cross-Cutting Themes

| Theme | Papers | Trajectory |
|-------|--------|------------|
| **Scaling laws everywhere** | Train-to-Test, EST, HyperP, Game BC, RLHF, LoopCTR | Scaling laws now established in CTR, games, RLHF, and distillation |
| **End-to-end generative** | OneRec-V2, GR4AD, GRAB, OneRanker | Industry replacing cascaded pipelines with generative models |
| **Hybrid architectures** | TransMamba, InfoMamba, Swimba, GPDiT | Convergence of previously separate paradigms (SSM+Attention, AR+Diffusion) |
| **Execution grounding** | DynaFix, VerifyBeforeYouFix, Prometheus | Code repair agents validated through execution, not just prediction |
| **Agent→tool optimization** | Mass, AgentConductor, Agent Q-Mix | Learning agent topologies replaces hand-design |
| **Inference-time scaling** | Train-to-Test, LatSearch, TMPC, Meta Flow Maps | Compute shifted from training to inference across modalities |

---

## References

See [arxiv-broad-2026-05-25.md](./arxiv-broad-2026-05-25.md) for the full categorized paper list with arXiv IDs.
