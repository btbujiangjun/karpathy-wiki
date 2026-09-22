---
title: "Conference & arXiv Digest: Top ML/AI Conferences 2025-2026 — 2026-09-22"
type: synthesis
created: 2026-09-22
updated: 2026-09-22
sources: [conference-web-searches]
tags: [conference-digest, ICML2026, ACL2026, EMNLP2026, KDD2026, NeurIPS2025, RecSys2026, CVPR2026, AGI2026, LLM, agents, world-models, generative-models, LoRA, agent-memory, LLM-inference, GEO, multimodal, benchmarks, daily-digest]
---

# Conference & arXiv Digest: Top ML/AI Conferences 2025-2026 — 2026-09-22

> Tuesday 22 Sep 2026 edition. This issue is a **venue-strand digest**, not a fresh-mailing sweep: today's Tue-22 arXiv window (2609.22087–2609.24554) was fully mined by the sibling digests [arxiv-daily](../2026-09-22/arxiv-daily.md), [arxiv-paper-check](../2026-09-22/arxiv-paper-check.md), and [arxiv-ai-search](../2026-09-22/arxiv-ai-search.md). This digest therefore covers **conference-confirmed venue content** (ICML 2026, ACL 2026, EMNLP 2026, KDD 2026, AGI 2026) whose camera-ready/preprint IDs post-dated earlier conference-digest editions, plus venue-calendar news (NeurIPS 2025 awards, CVPR 2026, RecSys 2026). Every featured paper's arXiv ID was **grep-verified absent (0 hits) from `wiki/`**.

---

## 1. NeurIPS 2025 — Best Paper Awards (cross-reference, no new IDs)

- **Best Paper — "Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)"** (Liwei Jiang, Yejin Choi et al., UW/CMU/AI2; arXiv 2510.22954) and **Best Paper Runner-up — "Superposition Yields Robust Neural Scaling"** (arXiv 2505.10465) are **already covered** in the wiki's earlier conference-editions (09-04/09-16 [conference-digest](../2026-09-04/conference-digest.md), etc.). No re-entry here.
- NeurIPS 2026 author notifications are due **~Sep 24, 2026** — this week's "under review" items resolve in the next digest windows.

---

## 2. ICML 2026 (Seoul — Jul 6–11, 2026)

### 2.1 Beyond Prediction — 面向 LLM 推理的尾部感知调度
- **Title (EN)**: Beyond Prediction: Tail-Aware Scheduling for LLM Inference
- **Authors**: Yueying Li, Yuanfan Chen, Jiayang Chen, Esha Choukse, Haoran Qiu, G. Edward Suh, Rodrigo Fonseca, Ziv Scully, Udit Gupta
- **Affiliation**: Cornell University / Microsoft Research / Meta (HAIlab lineage)
- **Venue**: ICML 2026
- **arXiv**: https://arxiv.org/abs/2606.18431
- **Innovation**: Attacks the fragility of prediction-driven LLM schedulers (SJF/SRPT approximations via predicted decode length). Proposes a **distribution-aware, prediction-free** framework that replaces explicit length prediction with **soft priority boosting driven by lightweight statistical signals**, co-optimizing scheduling with **cache-aware preemption** to handle memory-coupled decode dynamics under workload mixes.
- **Results**: Reduces **P99 TTLT by up to 35–50%** relative to SRPT with *perfect* length knowledge, and TTFT by **34–47%** across production + open-source traces (reasoning-heavy and chat-heavy mixes). Shows prediction-driven policies are fragile under distribution shift, bursty arrivals, and GPU memory pressure.
- **Comparison**: Strong negative result for the length-prediction scheduling line (this wiki's inference/KV-thread: ValueDiff 2609.23314, WaveFront 2609.23033) — tail latency is controllable without prediction when distributional signal substitutes for length estimates.

### 2.2 MSR ICML 2026 spotlight (news note)
- Microsoft Research ICML 2026 page highlights **HOBIT** (Hardness Optimized Batch Sampling for InfoNCE training, Spotlight) and Memora-class multimodal latent LM work; the exact arXiv IDs for these were not independently confirmed this run — flagged for the next sweep.

---

## 3. ACL 2026

### 3.1 STAPO — 轨迹感知的 LLM 智能体选择性策略优化
- **Title (EN)**: STAPO: Selective Trajectory-Aware Policy Optimization for LLM Agent Training
- **Authors**: Qiuyi Qi, Tian Liang, Mutian Bao, Jinjian Zhang, Dongnan Liu, Wei Zhou, Linjian Mo, Ming Kong, Jie Liu, Feng Zhang, Qiang Zhu
- **Affiliation**: (author-affiliation inferred, *tentative*)
- **Venue**: ACL 2026 Main
- **arXiv**: https://arxiv.org/abs/2607.04963
- **Innovation**: Diagnoses **trajectory neglect** — RL agents lose focus on the task goal and interaction history on long-horizon tasks. Prior step-level supervision used Shannon-entropy uncertainty, which conflates state complexity with agent confidence. STAPO introduces **normalized entropy** (confidence deviation from the agent's average behavior given a state) to localize outlier steps, then a **hierarchical group-based RL** that optimizes those steps with a joint trajectory-aware reward + trajectory-independent penalty.
- **Results**: SOTA on ALFWorld, WebShop, and Search-Augmented QA while substantially alleviating trajectory neglect.
- **Comparison**: Fixes the reliability gap of entropy-based step supervision; complements the trajectory-aware evaluation line (PTA-IRT 2609.01603, EarlyEval 2609.02783 below) with a **training-side** trajectory focus.

### 3.2 LightMem — 用小型语言模型实现的轻量智能体记忆
- **Title (EN)**: Lightweight LLM Agent Memory with Small Language Models
- **Authors**: Jiaquan Zhang, Chaoning Zhang, Shuxu Chen, Zhenzhen Huang, Pengcheng Zheng, Zhicheng Wang, Ping Guo, Fan Mo, Sung-Ho Bae, Jie Zou, Jiwei Wei, Yang Yang
- **Affiliation**: Kyung Hee University + collaborators (author-affiliation inferred, *tentative*)
- **Venue**: ACL 2026 Main
- **arXiv**: https://arxiv.org/abs/2604.07798
- **Innovation**: **LightMem** — agent memory driven by **Small Language Models (SLMs)**: modularizes retrieval, writing, and long-term consolidation; separates online processing from offline consolidation; organizes memory into short/mid/long-term tiers with user identifiers for multi-user isolation. Online two-stage selection (vector coarse retrieval → semantic consistency re-rank) under a fixed retrieval budget; offline abstraction of reusable interaction evidence into LTM.
- **Results**: **+2.5 avg F1 over A-MEM** on LoCoMo across model scales, median 83ms retrieval / 581ms end-to-end latency.
- **Comparison**: Occupies the middle ground between cheap-but-unstable retrieval memory and accurate-but-latency-heavy repeated-large-model calls; relevant to the agent-memory strand (RPMem 2609.23466, PSD 2609.23449).

---

## 4. EMNLP 2026 (Budapest — Oct 24–29, 2026)

### 4.1 CoMAP — 世界模型与智能体策略的共同演化
- **Title (EN)**: CoMAP: Co-Evolving World Models and Agent Policies for LLM Agents
- **Authors**: Youwei Liu, Jian Wang, Hanlin Wang, Wenjie Li
- **Affiliation**: The Hong Kong Polytechnic University
- **Venue**: EMNLP 2026 Main
- **arXiv**: https://arxiv.org/abs/2606.02372 (v2, Sep 3 2026)
- **Innovation**: Closed-loop co-evolution of **textual world models and agent policies**: the world model predicts future state feedback for candidate actions; the agent does future-aware reflection (estimating feedback reliability, refining the action); on-policy trajectories update the world model via **self-distillation** so it tracks the agent's evolving interaction distribution instead of staying frozen post-training.
- **Results**: Consistently beats baselines on embodied task planning, Web navigation, tool-use; **+16.75% relative** with Qwen3-4B; prediction accuracy improves over the co-evolution loop. Code: github.com/loyiv/CoMAP.
- **Comparison**: Directly counters "world models fixed after training" — connects the symbolic/code world-model line (Code World Models, D4RT) to the agent-RL thread (STAPO above, CANOPY).

### 4.2 TaRA — 训练感知的低秩适配初始化
- **Title (EN)**: TaRA: Training-Aware Low-Rank Adaptation Initialization
- **Authors**: Taehyeon Kim, Eunhyeok Park
- **Affiliation**: Korea Advanced Institute of Science and Technology (KAIST)
- **Venue**: EMNLP 2026 Main
- **arXiv**: https://arxiv.org/abs/2609.02639
- **Innovation**: LoRA performance is highly sensitive to initialization under the low-rank information bottleneck. Prior init schemes exploit principal components of pretrained weights/activations/gradients but ignore full-rank **training dynamics**. **TaRA** initializes LoRA so the gradients induced by low-rank factors closely approximate the full-rank weight matrix's gradient — derived from a mathematical formulation, at negligible overhead.
- **Results**: Consistently outperforms prior LoRA-init SOTA across diverse fine-tuning tasks.
- **Comparison**: Moves LoRA init from static PCA-style signal to training-aware gradient fidelity; relevant to the PEFT/adaptation strand of this wiki.

### 4.3 Counter-GEO-Bench — 对抗信息扭曲型生成引擎优化的防御基准
- **Title (EN)**: Counter-GEO-Bench: Evaluating Defenses Against Information-Distorting Generative Engine Optimization
- **Authors**: Bing Zheng, Zongyao Zhao, Wenming Yang
- **Affiliation**: (author-affiliation inferred, *tentative*)
- **Venue**: EMNLP 2026 Main (17 pages, 5 figures)
- **arXiv**: https://arxiv.org/abs/2609.02316
- **Innovation**: First controlled-defense benchmark for **information-distorting GEO** — adversaries publish ordinary-looking GEO-optimized docs that LLMs retrieve and synthesize into distorted answers. Pairs 247 human-verified quality-gated queries with information-preserving vs information-distorting rewrites; measures ASR, false-positive rate, answer quality across 3 victim LLMs.
- **Results**: Off-the-shelf guardrails (Granite Guardian, Llama Guard 3, NeMo Self-Check) cut ASR by **≤5.7% relative** (Granite's reduction not statistically significant) — safety-taxonomy guardrails target policy violations while GEO misinformation reads as fluent content. Proposed **C-GEO Guard** baseline cuts ASR **47.6% relative** at near-zero utility loss.
- **Comparison**: Connects to the AI-search audit strand (Scoring-With-the-Engine 2609.22655, source-exposure audit 2609.24407) — shifts from measurement to **defense benchmarking** of generative-engine manipulation.

---

## 5. KDD 2026 (Philadelphia — Aug 9–13, 2026)

### 5.1 MemeBridge — 跨文化梗解读的双向文化鸿沟数据集
- **Title (EN)**: MemeBridge: A Dataset for Benchmarking and Mitigating the Bidirectional Cultural Gap in Meme Interpretation
- **Authors**: Hangxiao Zhu, Suliu Qin, Zhuoyan Li, Ming Jiang, Yu Zhang, Meng Xia
- **Affiliation**: (U.S.-China university collaborators; author-affiliation inferred, *tentative*)
- **Venue**: KDD '26 proceedings, Vol. 1 — DOI 10.1145/3770854.3785691
- **arXiv**: https://arxiv.org/abs/2609.00491
- **Innovation**: A curated dataset of **U.S.-originated memes** with two complementary perspectives: (1) how Chinese participants interpret them, and (2) how U.S. participants *anticipate* other-culture misunderstanding. Built via multi-stage crowdsourcing with human-agreement + GPT-based verification; annotated with sentiment, emotion, cultural significance, knowledge type. Key finding: **anticipated misunderstandings are often inaccurate** — asymmetry in cultural understanding.
- **Results**: Probing shows cross-culture models only partially bridge the gap; **fine-tuning on MemeBridge improves cross-cultural interpretation** — evidence for culturally grounded resources in multilingual LLM training.
- **Comparison**: Extends the cultural-gap benchmark line (DRISHTIKON, EA-Culture) to the **bidirectional "expression vs perception"** framing — rarely benchmarked both ways.

---

## 6. AGI 2026 & General Agents / World-Models Strand

### 6.1 Executable World Models for ARC-AGI-3 — 编码智能体的可执行世界模型
- **Title (EN)**: Executable World Models for ARC-AGI-3 in the Era of Coding Agents
- **Authors**: Sergey Rodionov
- **Venue**: AGI-2026 (DOI 10.1007/978-3-032-33195-3_15)
- **arXiv**: https://arxiv.org/abs/2605.05138 (v2, Jun 6 2026)
- **Innovation**: A **deliberately generic coding-agent system** for ARC-AGI-3: maintains an executable Python world model, verifies it against observations, refactors toward simpler abstractions (an MDL-like simplicity bias proxy), and plans through the model before acting — no game-specific prompts/logic/harness anywhere. Audits unintended information channels that earlier vulnerable harnesses leaked.
- **Results**: GPT-5.5 high-effort: fully solved **15/25** public ARC-AGI-3 games, mean per-game RHAE 58.12%; GPT-5.4 high-effort: solved 8 games, RHAE 41.29%. Private validation pending. Code: github.com/astroseger/arc-3-agents-baseline1.
- **Comparison**: Directly parallels the ICLR-2026 "Code World Models" (DeepMind) idea — LLM-as-world-model-compiler + classical verification — now applied to ARC-AGI-3, with careful leakage-channel methodology shared with this wiki's benchmark-validity thread.

### 6.2 EarlyEval — 通过早期结果预测降低智能体评测成本
- **Title (EN)**: EarlyEval: Cheaper Agent Evaluation via Early Outcome Prediction
- **Authors**: Yuling Shi, Zhensu Sun, Junsen Dong, Chengcheng Wan, David Lo, Xiaodong Gu
- **Affiliation**: Singapore Management University / Shanghai Jiao Tong University
- **Venue**: arXiv (agent-evaluation methodology)
- **arXiv**: https://arxiv.org/abs/2609.02783
- **Innovation**: A **complementary axis** to benchmark distillation: instead of cutting the number of tasks, cut cost *within each task* by **early outcome prediction** — an agent's final outcome is often evident mid-run. Trains a pair of **LightGBM success/failure classifiers** over behavioral/textual/reference-solution features and halts a run once a calibrated confidence threshold is crossed (negligible per-step overhead).
- **Results**: On SWE-bench Verified, TerminalBench, Toolathlon: eliminates **13–26% of agent steps**, up to **44.1% input tokens / 29.4% output tokens** at 89–97% prediction accuracy, perturbing resolve rates by only 1–2 pp. Code: github.com/inphotoo/earlyeval.
- **Comparison**: Extends the eval-cost line (PTA-IRT 2609.01603, benchmark distillation) from task-subset selection to **within-trajectory early stopping** — a serving-side complement to the "coding agents have converged" measurement discussion.

---

## 7. Generative Models & Multimodal Architectures

### 7.1 LatentLM — 基于 next-token diffusion 的多模态潜空间语言模型
- **Title (EN)**: Multimodal Latent Language Modeling with Next-Token Diffusion
- **Authors**: Yutao Sun, Hangbo Bao, Wenhui Wang, Zhiliang Peng, Li Dong, Shaohan Huang, Jianyong Wang, Furu Wei
- **Affiliation**: Microsoft Research
- **Venue**: arXiv (Dec 2024; featured for the latent-diffusion-LM scaling relevance)
- **arXiv**: https://arxiv.org/abs/2412.08635
- **Innovation**: **LatentLM / σ-VAE** — unifies discrete (text/code) + continuous (image/audio/video) data under a causal Transformer: a VAE maps continuous data to latent vectors, and **next-token diffusion** autoregressively generates them; σ-VAE addresses variance collapse, which is critical for AR modeling.
- **Results**: Image generation surpasses Diffusion Transformers in performance and scalability; in MLLMs, favorable vs Transfusion and vector-quantized models under scaled training tokens; TTS beats **VALL-E 2** in speaker similarity/robustness at **10× fewer decoding steps**.
- **Comparison**: The cleanest end-to-end statement of the latent-vs-token diffusion tradeoff in a single backbone — builds straight on the "next-token diffusion" hybrid-diffusion thread (dLLM stack, Zarya hybrid AR+dLM 2609.19868) from 09-20/09-18 windows.

---

## 8. Cross-Cutting Observations & Calendar

- **World models are now a first-class agent primitive across venues**: EMNLP (CoMAP co-evolution), AGI-2026 (executable world models for ARC-AGI-3), ICLR-2026 precedent (Code World Models), ICML-2026 serving (tail-aware scheduling). The dominant agent-AI narrative this cycle is *models that build/verify/update their own environment models*, not better policies on raw observations.
- **Trajectory efficiency is the shared currency**: STAPO (training-side trajectory awareness), EarlyEval (eval-side early stopping), PTA-IRT (subset selection) — agent cost is being attacked simultaneously at the RL, evaluation, and serving layers.
- **The GEO/manipulation line matures from measurement to defense**: Counter-GEO-Bench shows existing safety-taxonomy guardrails fail on information-distorting content (≤5.7% ASR cut), echoing the source-exposure audits already in this wiki — an open industrial problem for AI-Search/answer engines.
- **RecSys 2026 (Minneapolis, Sep 29 – Oct 1)** arrives next week — the final program becomes the anchor for the next digest. NeurIPS 2026 notifications ~Sep 24. EMNLP 2026 conference Oct 24–29.
- **Calendar note**: NeurIPS 2025 best-paper and CVPR 2026 best-paper (D4RT, arXiv 2512.08924) winners are already captured in earlier digest editions — not re-reported.

---

## Data Quality Notes

- All 10 featured arXiv IDs grep-verified **0 hits in `wiki/`** and disjoint from the 2026-09-22 sibling sets (arxiv-daily / arxiv-paper-check / arxiv-ai-search).
- Venue assignments from arXiv comments fields / journal references: CoMAP, TaRA, Counter-GEO-Bench (EMNLP 2026 Main); STAPO, LightMem (ACL 2026 Main); Tail-Aware Scheduling journal-ref ICML 2026; MemeBridge KDD '26 DOI; Executable World Models AGI-2026 DOI.
- Author affiliations marked *tentative* where arXiv does not print them and none was confirmed this run.
- NeurIPS 2025 / CVPR 2026 winners referenced only (already in wiki); the MSR ICML-2026 HOBIT/Memora spotlight IDs unverified this run — flagged for next sweep.
- No contradictions with existing wiki claims surfaced.