---
title: "arXiv AI/LLM/RecSys/Advertising Paper Search (2026-08-21)"
type: synthesis
created: 2026-08-21
updated: 2026-08-21
tags: [arxiv, llm, recommendation, advertising, ctr, sequential-modeling, games, reinforcement-learning]
---

# arXiv Recent Papers — AI, LLM, Recommendation, Advertising, Sequential Modeling, CTR, Games

> Search date: 2026-08-21 · Scope: papers not yet covered anywhere in the wiki (dedup verified against all existing pages). No new CTR or sequential-modeling papers found today — all candidates were already covered in prior digests.

## 1. LLM Systems & Training

---

### 1.1 Cascade: SLO-Aware Latency Budget for LLM Serving

| Field | Detail |
|-------|--------|
| **Title** | Cascade: Exploiting SLO-Aware latency budget for fair and high goodput LLM inference serving |
| **Authors** | Muhammad Adnan, Rohan Mahapatra, Prashant J. Nair, Daniel Berger, Pantea Zardoshti, Rodrigo Fonseca, Esha Choukse |
| **Institution** | University of British Columbia + Microsoft Research |
| **arXiv** | https://arxiv.org/abs/2608.06557 |
| **Date** | 2026-08-06 |

**Abstract:** Requests under the same SLO differ by orders of magnitude in input/output length, cost, and KV-cache reusability — so they have different urgency. Cascade defines a per-request latency budget (SLO minus predicted remaining service time), continuously updated from request characteristics, KV-cache state, and system load. A single budget jointly coordinates request scheduling and KV-cache management across the memory hierarchy.

**Key Innovations:**
- Per-request latency budget as the single control signal for both scheduling and memory management
- Scheduler prioritizes low-budget requests; memory manager uses the same budget to decide restore/prefetch/HBM-retain/recompute for non-resident KV state
- Directs queueing and data-movement overhead toward requests that can absorb it → fairness preserved across heterogeneous request classes
- **Results:** up to 2.4x goodput improvement and 40% fewer SLO violations vs default vLLM FCFS on production traces across three LLMs

---

### 1.2 QUASAR: Loss-Aware Reconstruction Inside QAT

| Field | Detail |
|-------|--------|
| **Title** | QUASAR: Lowering the Loss Floor of Quantization-Aware Training with Loss-Aware Reconstruction |
| **Authors** | Vincent Counathe, Ben Athiwaratkun, Christopher De Sa, Tianyi Zhang |
| **Institution** | Cornell University + Meta |
| **arXiv** | https://arxiv.org/abs/2608.13966 |
| **Date** | 2026-08-14 |

**Abstract:** QAT computes loss/gradients through a lossy reconstruction of latent full-precision weights while updating the latent weights themselves — this mismatch raises the loss floor. Second-order PTQ methods minimize loss-aware reconstruction error but take hours per pass; repeating throughout QAT is impractical. QUASAR performs lightweight loss-aware reconstruction continuously inside the training loop.

**Key Innovations:**
- Online saliency via EMA of squared gradients; small clipping-range search; saliency-weighted least-squares fit of affine dequantizers each step
- Theory: loss-aware reconstruction error is the only reconstruction-dependent term in the QAT convergence bound and controls final quantized-model loss
- Training-procedure-only change — supports integer quantization and NVFP4 with zero inference-time overhead
- **Results:** lowest held-out KL among competitive QAT at 2/3/4 bits on Qwen3 & Llama-3.1 (≥10% KL reduction at 3–4 bits, 29% at 2 bits); +3.5–4.3 pp average accuracy over strong baselines at 2 bits

---

### 1.3 LazyTrain: Zero-Waste LLM Training on Limited Hardware

| Field | Detail |
|-------|--------|
| **Title** | LazyTrain: Limited-resource Allocation toward Zero-waste Yield Optimization in Large Language Model Training |
| **Authors** | Xiaojun Wu, Cehao Yang, Honghao Liu, Xueyuan Lin, Xuhui Jiang, Chengjin Xu, Jia Li, Jian Guo |
| **Institution** | AIsquare |
| **arXiv** | https://arxiv.org/abs/2608.11919 |
| **Date** | 2026-08-12 |

**Abstract:** Training LLMs on limited hardware is a scheduling problem spanning GPU compute, host memory, PCIe transfer, and storage bandwidth. LazyTrain is an optimization layer over a layer-streaming executor: it formulates checkpoint selection, activation placement, recomputation, and CPU-GPU-NVMe communication overlap as a mixed-integer scheduling problem, then executes the solved policy during training.

**Key Innovations:**
- Mixed-integer formulation unifying checkpointing + placement + recomputation + communication overlap (fixed heuristics leave comms exposed on the critical path)
- Hybrid 8-bit operator: 8-bit optimizer states + fast gradient clipping fused to counteract CPU-side update overhead
- **Results:** ~1.24x sustained TFLOPS vs matched baselines on H800 (Qwen2.5-3B → Qwen3.6-27B); RTX 3090 gains one feasible batch size per scale; Qwen3.6-27B run hits 219.95 TFLOPS / 1361 tokens/s at batch 72 within 68.84 GB GPU memory with 95.42% exact-match accuracy

---

### 1.4 KV-Pipe: Cross-Layer KV Sharing as Pipeline Balancing Knob

| Field | Detail |
|-------|--------|
| **Title** | KV-Pipe: On the Relation Between KV Sharing and Pipeline Parallel Efficiency in LLMs |
| **Authors** | Maryam Dialameh, Hossein Rajabzadeh, Harish Krishnamoorthy Murali, Walid Ahmed, Weiwei Zhang, Hyock Ju Kwon |
| **Institution** | University of Waterloo + Huawei Technologies Canada |
| **arXiv** | https://arxiv.org/abs/2608.15943 |
| **Date** | 2026-08-16 |

**Abstract:** Pipeline parallelism suffers from stage imbalance and bubbles; cross-layer KV sharing has only been studied as an inference-side cache saver. KV-Pipe repurposes KV reuse as a pipeline-balancing control knob: starting from the tail stage, it converts selected attention layers to cross-layer KV sharing tail-first, iteratively retargeting the bottleneck to drive the FLOPs Imbalance Ratio (FIR) toward 1.

**Key Innovations:**
- Tail-first conversion order + iterative bottleneck retargeting → FIR ≈ 1
- Fully offline procedure: needs only pipeline partition + per-layer FLOPs estimates; negligible runtime overhead, no online tuning
- Dual benefit: same mechanism cuts KV-cache growth and redundant KV projection work → higher long-context decoding throughput
- **Results:** up to +9.2% training MFU and −9.8% iteration time; larger gains at higher pipeline-parallel degrees

---

### 1.5 PCD: Prefix-Conditioned Diffusion Pretraining

| Field | Detail |
|-------|--------|
| **Title** | Reducing Pretraining-Generation Mismatch in Diffusion Language Models |
| **Authors** | Xiaocheng Lu, Huabin Liu, Song Guo, Jianguo Li |
| **Institution** | HKUST (Guangzhou) + Alibaba International Digital Commerce |
| **arXiv** | https://arxiv.org/abs/2608.09424 |
| **Date** | 2026-08-10 |

**Abstract:** Native diffusion LM pretraining randomly corrupts prompt and continuation tokens together, weakening the clean-prefix interface that prompt-conditioned generation relies on. PCD (Prefix-Conditioned Diffusion) combines AR prefix supervision with no-shift suffix denoising so the local training interface matches how block-diffusion models are queried at evaluation time.

**Key Innovations:**
- Objective-level change only: attention mask + corruption mask + label construction in continued pretraining — no AR decoder, verifier, or new inference mode
- Separates intra-sample prefix conditioning from inter-sample objective mixing (identifies local alignment signal vs optional batch-level knob)
- **Results:** +4.2% relative gain on LLaDA2-Mini six-benchmark average (+2.56 pts); +14.2% relative in primary Qwen-1.7B mechanism comparison (+4.86 pts); recovers part of the dLLM continuation gap without touching inference

---

## 2. Advertising & Monetization

---

### 2.1 DARA: Few-Shot Ad Budget Allocation with RL-Finetuned LLMs

| Field | Detail |
|-------|--------|
| **Title** | DARA: Few-shot Budget Allocation in Online Advertising via In-Context Decision Making with RL-Finetuned Large Language Models |
| **Authors** | Mingxuan Song, Yusen Huo, Bohan Zhou, Shenglin Yin, Zhen Xiao, Jieyi Long, et al. |
| **Institution** | Shopee |
| **arXiv** | https://arxiv.org/abs/2601.14711 |
| **Date** | 2026-01 |

**Abstract:** Extends AI-generated budget allocation (AIGB) from generative planning to few-shot in-context decision making. DARA is a dual-phase framework: a few-shot reasoner handles novel scenarios via in-context learning, while a fine-grained optimizer refines allocations. Post-training uses GRPO-Adaptive, which dynamically adjusts advantage estimation and clipping ranges for sparse-reward budget-allocation tasks.

**Key Innovations:**
- Dual-phase architecture: few-shot reasoner (in-context adaptation) + fine-grained optimizer (allocation refinement)
- GRPO-Adaptive post-training strategy tailored to sparse-reward RL environments
- Bridges AIGB paradigm toward true few-shot decision making on unseen advertiser/scenario combinations
- Industrial deployment context: Shopee online advertising platform

---

### 2.2 LERA: LLM-Enhanced RAG Ad Auction for Generative Chatbots

| Field | Detail |
|-------|--------|
| **Title** | LERA: LLM-Enhanced RAG for Ad Auction in Generative Chatbots |
| **Authors** | Haoran Sun, Xinrui Song, Xinyu Zhang, Zhaohua Chen, Xu Chu, Zhilin Zhang, Chuan Yu, Jian Xu, Bo Zheng, Xiaotie Deng |
| **Institution** | Shanghai Jiao Tong University + Alibaba Group |
| **arXiv** | https://arxiv.org/abs/2605.16474 |
| **Date** | 2026-05-15 |

**Abstract:** Builds on the retrieve-then-generate ad insertion paradigm (Feizi et al., Hajiaghayi et al.) but fixes its weakness: text-embedding-only retrieval causes commercial misinterpretation and repetitive insertions. LERA's stage 1 does embedding-based coarse filtering of candidate advertisers; stage 2 queries the LLM itself for logits over candidates, used as refined organic relevance scores combined with bids.

**Key Innovations:**
- LLM logits as fine-grained organic relevance scores — relevance judgment moves inside the model rather than relying solely on embedding similarity
- Critical-value payment rule accounting for both coarse-filtering and fine-ranking thresholds → truthfulness for utility-maximizing advertisers
- Naturally extends to multiple ad insertions in dynamic dialogue flows and long responses
- Synthetic advertiser-query benchmark: substantially better ad selection accuracy + insertion diversity at controllable latency overhead

---

### 2.3 Genre-Based VCG Auction for Ad Insertion in LLM Responses

| Field | Detail |
|-------|--------|
| **Title** | Ad Insertion in LLM-Generated Responses |
| **Authors** | Shengwei Xu, Zhaohua Chen, Xiaotie Deng, Zhiyi Huang, Grant Schoenebeck |
| **Institution** | Fudan University + University of Chicago + University of Oxford + University of Michigan |
| **arXiv** | https://arxiv.org/abs/2601.19435 |
| **Date** | 2026-01-27 |

**Abstract:** Addresses sustainable LLM monetization where static-keyword search advertising fails against fleeting conversational intent. Two decouplings: (1) ad insertion decoupled from response generation (safety + explicit disclosure); (2) bidding decoupled from user queries via "genres" (high-level semantic clusters) — advertisers bid on stable categories instead of sensitive real-time responses, cutting compute burden and privacy risk.

**Key Innovations:**
- Genre-based bidding proxy: stable semantic clusters replace token-/query-level bidding
- VCG auction on genres yields approximately DSIC + IR + approximately optimal social welfare with high computational efficiency
- Explicitly handles contextual coherence, latency, privacy, and mandatory ad disclosure as first-class constraints
- "LLM-as-a-Judge" coherence metric correlating strongly with human ratings (Spearman ρ ≈ 0.66), outperforming 80% of individual human evaluators

---

## 3. Generative Recommendation

---

### 3.1 Centroid Initialization for Semantic ID Tokens

| Field | Detail |
|-------|--------|
| **Title** | Preserving Item Semantics for Free: Rethinking Token Initialization in LLM-Based Generative Recommendation |
| **Authors** | Donald Loveland, Liam Collins, Bhuvesh Kumar, Danai Koutra, Neil Shah |
| **Institution** | Snap Inc. + University of Notre Dame |
| **arXiv** | https://arxiv.org/abs/2608.07816 |
| **Date** | 2026-08-07 |

**Abstract:** In LLM-based generative recommendation, items are represented as semantic IDs (SIDs) added to the vocabulary as special tokens — but standard vocabulary expansion initializes them as random Gaussian vectors, discarding the SIDs' continuous geometry. The paper shows this makes SID embeddings organize around item popularity rather than semantics, and that even expensive continual pretraining (CPT) fails to reliably recover the original geometry.

**Key Innovations:**
- Diagnosis: random-init SIDs → popularity-organized embeddings; CPT partially reduces popularity bias but doesn't restore semantic geometry
- Fix: parameter-free drop-in initialization of SID token embeddings directly from their centroids in the semantic embedding space
- **Results:** up to +16% pure-SFT Recall@5, peak performance with up to 40% fewer SFT steps, up to +60% cold-item Recall@5; on CPT-friendly datasets, comparable quality with half the CPT epochs
- Zero additional training or inference overhead ("for free")

---

## 4. Games & Multi-Agent

---

### 4.1 SocialRL: Reinforcing Social Reasoning in Small Language Models

| Field | Detail |
|-------|--------|
| **Title** | From Passive Delegates to Strategic Negotiators: Reinforcing Social Reasoning in Small Language Models with SocialRL |
| **Authors** | Wenyue Hua, Zachary Huang, Tyler Payne, Safoora Yousefi, Saleema Amershi, Asli Celikyilmaz |
| **Institution** | Microsoft Research |
| **arXiv** | https://arxiv.org/abs/2608.13787 |
| **Date** | 2026-08-13 |

**Abstract:** Assistant-like dispositions make frontier models poor delegates: they disclose private information unprompted and concede at first resistance. SocialRL is a general recipe training social reasoning directly in a 4B model across six domains (Deal-or-No-Deal, CaSiNo, Craigslist, Job Interview, Calendar, Marketplace), every domain trained in-domain and evaluated on all six.

**Key Innovations:**
- In-domain RL reaches frontier level: 4B model matches/exceeds GPT-5 family per domain, closing 73–122% of baseline-to-frontier gap on negotiation games; 78% of buyer openings anchor below target (vs 3% untrained)
- Cross-domain transfer follows game structure: structurally paired games lift each other; broad multi-issue donor lifts nearly all domains; structurally isolated games transfer nothing
- Cascade RL + multi-teacher on-policy distillation (OPD) consolidate specialists into one unified 4B reaching 0.627 avg utility — matching/exceeding GPT-4.1 (0.625), GPT-5.1 (0.619), GPT-5.2 (0.613)
- Theory-of-Mind insight: distilling ToM traces (not just actions) lifts utility everywhere and generalizes better; of two ToM skills, only next-action prediction predicts negotiation outcomes

---

## Coverage Notes

- **CTR prediction / sequential modeling:** no new papers this round — all candidates surfaced (STAR KDD Cup solution, OneModel, UniDot, GateDiffInt, LENS, etc.) were already covered in the [2026-08-20 digest](../2026-08-20/arxiv-ai-search.md) and daily digests.
- **Games:** Do LLMs Beat Nash? (2608.12547, McGill) also surfaced but was already covered.
- Strongest cross-cutting theme today: **LLM logits/embeddings reused as system-level signals** — Cascade (budgets), LERA (relevance scores), QUASAR (saliency), SocialRL (ToM traces).
