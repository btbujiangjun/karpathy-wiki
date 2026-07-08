---
title: arXiv Paper Check — AI & CTR (July 8, 2026)
type: synthesis
created: 2026-07-08
updated: 2026-07-08
sources: []
tags: [arxiv, ai, ctr, daily]
---

# arXiv Paper Check — AI & CTR (July 8, 2026)

Scanned cs.AI (49 new), cs.LG (58 new), cs.IR (11 new) from Wednesday, July 8, 2026 listings. No new CTR-specific papers found today; recent CTR highlights from prior days included for reference.

---

## Top AI Papers

### 1. SearchEyes: Frontier Multimodal Deep Search Intelligence
- **arXiv**: 2607.05943
- **Authors**: Zhengbo Jiao et al.
- **Key contribution**: Uses a typed knowledge graph as backbone of a simulated search world. Proposes Perception-Knowledge Chains (PKC) to sample constrained multi-hop paths over Wikidata5M, and Hop-Anchored Policy Optimization (HaPO) for step-level credit assignment without a separate process reward model. **SearchEyes-27B** improves over strongest open-source baseline by **6.2 points avg** on 6 multimodal benchmarks.

### 2. Memory in the Loop: In-Process Retrieval as Extended Working Memory
- **arXiv**: 2607.05690
- **Authors**: Yusuf Khan, Carlo Lipizzi
- **Key contribution**: Moves memory inside the agent loop (read/write every step). Shows that in-process stores (~100us) eliminate the latency tax: redundant actions rise monotonically with latency (0/12 at in-process speed vs 7.2/12 at 110ms cloud round-trip). Demonstrates recall improves from 0/5 to 3.6-4.8/5 with in-loop memory across GPT-5-class models.

### 3. NapMem: Learning to Use Memory as a Structured Action Space
- **arXiv**: 2607.05794
- **Authors**: Yue Xu et al.
- **Key contribution**: Organizes user history into a linked multi-granularity memory pyramid (raw conversations → typed records → topic tracks → user profiles). Agent trained via memory-tool RL to select appropriate granularity. Competitive on PersonaMem-v2, LongMemEval, and LoCoMo while preserving general reasoning.

### 4. Akashic: Low-Overhead LLM Inference with MemAttention
- **arXiv**: 2607.05708
- **Authors**: Yang Liu et al.
- **Key contribution**: MemAttention organizes context into bounded chunks with semantic cross-chunk relationships, plus hardware-software co-designed memory placement. Improves task accuracy by up to **10.2 points**, throughput by **1.21x**, and sustainable request rate by **1.88x** over strong baselines.

### 5. CSTutorBench: Benchmarking SLMs as Tutors for Block-Based Programming
- **arXiv**: 2607.05571
- **Authors**: H. Chad Lane, Bryson Kageler
- **Key contribution**: 17 scenario-based questions scored against a pedagogical rubric. Across 11 models (4B-120B), models perform well on surface-level criteria but struggle with deeper pedagogy (answer leakage, engaging with student debugging). Model family and instruction-tuning predict quality better than parameter count.

### 6. Narrative World Model: Narratology-Grounded Writer Memory
- **arXiv**: 2607.05577
- **Authors**: Mohammad Saifullah et al.
- **Key contribution**: Pairs a narratology-grounded typed temporal-state graph with query-conditioned hybrid retrieval. Substantially outperforms Graphiti/Zep on multi-hop narratological QA. The advantage is representational — survives rebuilding baseline with NWM's own extractor.

### 7. TurnOPD: Efficient On-Policy Distillation for Long-Horizon Agents
- **arXiv**: 2607.05804
- **Authors**: Yuhang Zhou et al.
- **Key contribution**: Identifies two inefficiencies in vanilla agent OPD: wasteful tail turns and token-level KL imbalance. Proposes adaptive rollout-depth budgeting + progressive turn-normalized loss budgeting. Superior accuracy under equal wall-clock budgets on ALFWorld, WebShop, and Multi-Hop Search.

### 8. PolyWorkBench: Multilingual Long-Horizon LLM Agents
- **arXiv**: 2607.06008
- **Authors**: Hongliang Li et al.
- **Key contribution**: 67 tasks across 5 domains (commerce, legal, localization, etc.) requiring multilingual inputs/outputs. Proposes hybrid evaluation framework (structural grading + executable verification + semantic assessment). State-of-the-art agents suffer significant degradation in multilingual settings vs monolingual.

### 9. StateFuse: Deterministic Conflict-Preserving Memory for Multi-Agent Systems
- **arXiv**: 2607.05844
- **Authors**: Sergey Volkov et al.
- **Key contribution**: Conflict-aware replicated memory contract built on OpSet/CRDT merge. Preserves contradictions visible for safer abstention and correction. On 282-question MemoryAgentBench slice, tied on accuracy but conflict-preserving surfaces enable safer behavior.

### 10. FirstResearch: Auditable Question Formation for LLM Scientific Discovery Agents
- **arXiv**: 2607.05682
- **Authors**: Yufeng Wang
- **Key contribution**: Introduces a Research Question Certificate (primitive definitions, assumptions, mechanism model, falsifiable hypothesis, minimal test). Certificate-only scoring reaches 4.90/5 vs 4.38/5 for strongest baseline; removing certificates drops below 1/5.

### 11. ArtisanCAD: Industrial-Level CAD Agent with Expert-Grounded Knowledge Distillation
- **arXiv**: 2607.05750
- **Authors**: Yunhan Xu et al.
- **Key contribution**: CAD-IR representation encoding parameters, operations, MCP tool bindings, dependencies. Distills expert CATIA recordings into reusable skills. Reduces mean Chamfer Distance from 14.83 to 9.88 on intermediate prompts.

### 12. Controlling Tool Use with Heading-Specific Activation Steering
- **arXiv**: 2607.05790
- **Authors**: Yuqi Chen et al.
- **Key contribution**: Steering vectors from heading-anchor positions exert bidirectional causal control over tool-invocation. Finds tool-use steering vectors differ geometrically from parametrically-grounded concepts — diffuse, bimodal alignment rather than clean linear structure.

---

## Top Machine Learning Papers

### 13. FourTune: Towards Fully 4-Bit Efficient Post-Training for Diffusion Models
- **arXiv**: 2607.05711
- **Authors**: Bowen Xue et al.
- **Key contribution**: End-to-end W4A4G4 paradigm. Triple-branch hybrid pipeline with frozen numerical stabilizer to isolate quantization-sensitive outliers. On FLUX.1-dev (12B): **2.25× memory reduction** and **2.27× training throughput** increase vs BF16 LoRA.

### 14. λ-VAE: Variance Equalization for Posterior Collapse
- **arXiv**: 2607.05531
- **Authors**: Girum Demisse
- **Key contribution**: Unifies two causes of posterior collapse (gradient imbalance + information gap). λ-VAE scales sampling noise by per-dimension exponent while KL penalty retains original posterior variance. Up to **2.8× nats** information capacity gain, **+0.33 BPD** on benchmarks.

### 15. Exogenous Dropout: Simple Strong Baseline for Robust Time Series Forecasting
- **arXiv**: 2607.05452
- **Authors**: Hao Hu, Xue-shan Ai
- **Key contribution**: Model-agnostic method that randomly zeros whole exogenous channels during training. Substantially improves robustness under Gaussian noise, temporal misalignment, and missing channels while preserving clean accuracy. Unbounded model + exogenous dropout beats explicitly bounded architectural foil.

### 16. Stochastic Token Steering (STS/SBS): Bernoulli Sparse Steering of LLMs
- **arXiv**: 2607.05615
- **Authors**: Nima Eshraghi et al.
- **Key contribution**: Gating only 50% of tokens recovers most of dense-steering effect while preserving fluency. Optimal steering magnitude scales inversely with intervention ratio — cumulative signal dosage matters, not per-token perturbation.

### 17. LLM-Driven Neural Network Generation with Same-Family Architecture Guidance
- **arXiv**: 2607.05704
- **Authors**: Kabir Dev Paul Baghel et al.
- **Key contribution**: Source-guided candidate-generation protocol using stronger same-family source model. On CIFAR-10: +0.2651 accuracy over non-source candidate (0.5049 vs 0.2398). LLM adapts rather than copies — hp_transfer 0.7880 vs source-recipe copy 0.1959.

---

## Top Information Retrieval Papers

### 18. PORTS: Preference-Optimized Retrievers for Tool Selection
- **arXiv**: 2607.05441
- **Authors**: Lorenzo Molfetta et al.
- **Key contribution**: Odds ratio preference optimization using perplexity-inspired signal from frozen LLM. Fine-tunes retriever to find helpful tools by correlating selection probabilities with downstream performance. Demonstrated on 6 datasets, 2 encoders, 3 LLMs.

### 19. SCOReD: Student-Aware CoT Optimization for Recommendation Distillation
- **arXiv**: 2607.05734
- **Authors**: Haz Sameen Shahgir et al.
- **Key contribution**: Parses teacher traces into typed segments, scores importance via student LLM attention, dynamically selects edits (KEEP/REWRITE/FUSE/PRUNE). Improves over baseline SFT by **1.56% NDCG** and **1.9% Recall@5**, reduces reasoning length by **27.3%**.

### 20. Signed MaxSim: Quantifying and Expanding Theoretical Capacity of Late-Interaction Retrieval
- **arXiv**: 2607.05803
- **Authors**: Julian Killingback et al.
- **Key contribution**: Proves MaxSim can exactly replicate any non-negative k-sparse inner product. Introduces Signed MaxSim that can replicate any real-valued inner product. On negation-only queries: nDCG@10 from 0.008 to **0.788**.

---

## CTR Papers (Recent, from prior days — no new CTR listings today)

| arXiv | Title | Date | Key Result |
|-------|-------|------|------------|
| 2606.07980 | DeRes: Dual-Path Residual CTR Scaling | late Jun | 2× compute savings at equiv AUC |
| 2606.04944 | DS-MLP: Dual-Stream MLP Distillation (TKDD) | Jun 2026 | SOTA on Criteo/Avazu/Movielens |
| 2604.19550 | LoopCTR: Loop Scaling for CTR | Apr 2026 | Train-multi-loop, infer-zero-loop |
| 2602.10811 | EST: Efficient Scaling Laws (Taobao deployed) | Feb 2026 | +3.27% RPM, +1.22% CTR online |
| 2602.01865 | GRAB: LLM-Inspired CTR at Baidu | Feb 2026 | +3.05% revenue, +3.49% CTR |
| 2602.20676 | PRECTR-V2: Unified Relevance-CTR | Feb 2026 | +3.60% AUC, LLM-distilled encoder |
| 2601.18251 | GenCI: Generative CTR via Cohort Intent (WWW 2026) | Jan 2026 | Generative NTP for intent modeling |

---

## Key Themes

1. **Memory Architectures Dominate** — 4 of the top papers (MemAttention, NapMem, Memory-in-the-Loop, StateFuse) reimagine memory for agents: in-process, multi-granularity, conflict-preserving
2. **Agent Evaluation Maturing** — Benchmarks for multilingual (PolyWorkBench), pedagogical (CSTutorBench), long-horizon (TurnOPD), and scientific (FirstResearch) capabilities
3. **4-bit Training Arrives for Diffusion** — FourTune proves W4A4G4 matches full-precision for diffusion model post-training
4. **Verification as Scaling Axis** — FirstResearch's certificate-based approach echoes the verification theme prominent in prior days
5. **CTR Quiet Day** — No new CTR papers today; the field continues processing recent hits (DeRes, DS-MLP, LoopCTR, EST)
