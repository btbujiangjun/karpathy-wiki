---
title: "arXiv Daily Report (2026-11-21) — AI, LLMs, Recommendation, Advertising, CTR, Sequential Modeling, Games"
type: synthesis
created: 2026-11-21
updated: 2026-11-21
sources: [arxiv.org]
tags: [arxiv, daily, ai, llm, agentic, agent, recommendation, retrieval, advertising, ctr, sequential-modeling, games, diffusion-lm, distillation, fairness]
---

# arXiv Daily Report (2026-11-21)

> **Query time**: 2026-11-21. This report covers the newest arXiv batch across AI, LLMs, recommendation, advertising/CTR, sequential modeling, games, and related areas.
>
> **Method**: arXiv Export API sweeps over `cat:cs.CL` (LLMs), `cat:cs.IR` (recommendation), `cat:cs.LG` (ML / sequential modeling), `cat:cs.GT` (games), and the keyword query `all:advertising`, all sorted by `submittedDate` descending (newest-first). Papers are deduplicated across sweeps by arXiv id. **Numbers are author-reported, not independently reproduced.**

## Summary

- **LLMs / agents**: Beam — a 501B MoE with frontier coding/reasoning and a fully-async RL post-training loop; dLoop — pre-commitment latent computation for faster diffusion LMs; AutoMaster — LLM-driven behavioral shaping of teachers; HiSA — sparsifying attention's hidden dimension; GLiDE — single-pass calibrated decision models distilled from reasoning teachers.
- **Recommendation**: LSER integrates LLM session embeddings into retrieval at Autodesk; CACO adds coverage-aware coordination to continuous generative retrievers; Generative news recommenders reproduce popularity via training-data memorization.
- **Advertising / CTR**: DNA unlocks depth scaling in Taobao CTR; X-split ARGUS cuts serving cost via reusable history tokens; Iterative Scarcity-Guided Exploration bootstraps auto-bidding; CutAgent builds high-CTR ad videos with a gene-driven dual-agent pipeline.
- **Sequential modeling**: the observation window outweighs data/capacity/architecture ("the window lever"); Neural CGM learns latent dynamics with closed-form DA updates.
- **Games**: safe subgame resolving in multiplayer poker; temporal fair division for chores.

---

## A. AI / LLMs (8)

### 1. Beam Model Technical Report
- **arXiv**: [2611.26358](https://arxiv.org/abs/2611.26358)
- **Date**: 2026-11-19
- **Authors**: Reflection Team — Adam Abdulhamid (co-author list on arXiv lists him followed by many others; the group name “Reflection Team” is credited)
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.CL, cs.AI
- **Abstract**: Beam is a sparse Mixture-of-Experts (MoE) model with 501.3B total parameters and 23.4B active parameters, specifically built and optimized for coding, reasoning, and agentic workloads. Beam delivers frontier level reasoning, while requiring 3-4x less inference compute than many models of its class. Pretrained on 23.8T diverse, curated, high-quality tokens, Beam features a 1M-token context window achieved through a novel two-stage midtraining phase, built on verifiable, correctness-anchored data. Post-training leveraged a large-scale, fully asynchronous reinforcement learning (RL) campaign across 10.5K GB300 GPUs, generating over 100M rollouts over 4 weeks of training. We believe this is one of the largest scale RL runs conducted by any open lab to date. Across our evaluation suite, capabilities continued to improve as we increased RL compute, with no sign of a plateau. Supported by deep hardware-model co-design, FP8/NVFP4 quantization, and a 1.93B-parameter speculative decoding drafter (DFlash 2), Beam maximizes serving throughput with efficient, flexible deployment. Averaged across conversation turns and harm categories, Beam refuses or pivots on 88.9% of harmful requests while complying with 81.5% of harmless requests, achieving the highest refusal/pivot rate on harmful requests among open-weight models on the Pareto frontier.
- **Key innovations**:
  - Sparse MoE at 501.3B/23.4B scale, optimized for coding, reasoning and agentic workloads.
  - 1M-token context via a novel two-stage midtraining phase on verifiable, correctness-anchored data.
  - Fully asynchronous RL post-training at 10.5K GB300 GPUs (>100M rollouts over 4 weeks), with no plateau observed as RL compute grows.
  - Hardware-model co-design: FP8/NVFP4 quantization and a 1.93B-parameter speculative drafter (DFlash 2).
  - High refusal/pivot rate on harmful requests (88.9%), best among open-weight models on the Pareto frontier.

### 2. AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control
- **arXiv**: [2611.26613](https://arxiv.org/abs/2611.26613)
- **Date**: 2026-11-19
- **Authors**: Yiyang Du, Yuxuan Kuang, Qitao Zhao, Yixuan Wang, Zhanqiu Guo, Yi Xu, Xin Li, Wenbin He, Liu Ren, Chenyan Xiong
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.RO, cs.CL, cs.CV
- **Abstract**: Frontier multimodal language agents such as GPT-6 Astra have demonstrated strong capabilities in controlling robots directly via low-level numerical actions without high-level primitives. However, existing benchmarks report only episode-level success rates, which show neither how these agents succeed nor where they fail. In this paper, we present a systematic action-level analysis of frontier agents on direct robot control across 12 manipulation benchmarks. We introduce AgentRoboCritic, an intent-grounded critique framework in which the policy agent states a local intent alongside each action, and a critic evaluates the action's outcome and failure mode against this intent. Our action-level analysis demonstrates the promising capabilities of frontier agents on direct robot control, including closed-loop recovery from local execution failures, reliable semantic grounding across diverse scenes, and strong zero-shot manipulation without task-specific adaptation. It also identifies their current limitations, including task-relevant physical execution bottlenecks such as grasping and alignment, and uneven recovery across failure modes. Finally, we validate our critic on a 400-action human-annotated benchmark and release a dataset of 12,844 annotated actions alongside a fine-tuned open-source critic, Muse-Glimmer-30B, whose failure-mode accuracy rises from 32.58% to 74.24%, enabling low-cost action-level analysis.
- **Key innovations**:
  - Intent-grounded critique framework (policy agent + independent critic) for frontier robots agents.
  - Action-level analysis across 12 benchmarks: 12,844 annotated actions; Muse-Glimmer-30B failure-mode accuracy rises 32.58% → 74.24%.
  - Documents closed-loop recovery, semantic grounding, and uneven recovery patterns of frontier agents.

### 3. AutoMaster: Autonomous Post-Training by Making the Same Model a Better Teacher
- **arXiv**: [2611.26510](https://arxiv.org/abs/2611.26510)
- **Date**: 2026-11-19
- **Authors**: Guoxin Chen, Shuang Sun, Fanzhe Meng, Xinyu Tang, Ruihua Song, Wayne Xin Zhao
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.CL
- **Abstract**: Task success alone does not specify which behaviors post-training should reinforce. Even successful teacher trajectories can contain unsupported assumptions, unproductive repetition, or superficial verification. We propose Skill-FT (Skill-Guided Fine-Tuning), which uses natural-language skills to suppress undesirable habits and elicit underrepresented effective behaviors during teacher rollouts, then fine-tunes a target model on the resulting trajectories. We introduce AutoMaster, an autonomous post-training system in which an LLM agent develops these interventions through trajectory analysis, skill design, data selection, and feedback from rollouts and target-model evaluation. Across Terminal, Search, and software engineering tasks with 4B and 9B target models, AutoMaster improves mean performance over Vanilla SFT on successful unguided teacher trajectories by 1.42–8.99 percentage points, with the teacher, task pool, training set size, and SFT recipe held fixed. Together with the ablations and trajectory analyses, these results suggest that behavioral shaping can make a fixed model a more effective teacher. We further find that retaining skill instructions during SFT yields higher mean performance than removing them across all six settings, despite their absence at evaluation and identical supervised outputs.
- **Key innovations**:
  - Skill-FT: skills suppress bad habits and elicit underrepresented behaviors in teacher rollouts.
  - AutoMaster agent autonomously develops interventions (trajectory analysis, skill design, data selection, rollout/eval feedback).
  - +1.42–8.99 pp over Vanilla SFT with fixed teacher/task/dataset across Terminal/Search/SWE tasks.
  - Skill context retained during SFT improves behavior internalization beyond its eval-time absence.

### 4. GLiDE: A Fast, Calibrated Decision Model Distilled from Reasoning Teachers
- **arXiv**: [2611.26509](https://arxiv.org/abs/2611.26509)
- **Date**: 2026-11-19
- **Authors**: Sahibzada Allahyar, Julia White, Dhruv Atreja, George Hurn-Maloney, Urchade Zaratiana
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.AI, cs.CL
- **Abstract**: Decision models enable fast, confidence-aware decisions by scoring candidate answers in a single forward pass, without generating text or intermediate reasoning. Yet reasoning can substantially improve decision quality, raising the question of whether its benefits can be retained without the cost of generating it. We investigate this question with **GLiDE**, a family of decision models spanning 0.4B to 27B parameters. Building on Qwen hybrid language models, GLiDE enables bidirectional interactions between the context, question, and candidate answers by removing causal masking from full-attention layers. To transfer reasoning capabilities into single-pass inference, we combine soft-target distillation from multiple teachers, including a reasoning model, with progressive post-training on diverse decision tasks. We further explore parameter-free recurrent depth to increase inference-time computation without generating tokens. Across five model sizes, GLiDE lies on the performance–parameter Pareto frontier, with each model outperforming evaluated alternatives of equal or smaller size. **DM2** (27B) achieves a hidden-set score of 71.52, with an expected calibration error of 2.0% and a median latency of 92.9ms on a single GPU. Further checkpoint averaging and parameter-free recurrent depth yield GLiDE 27B, which reaches 73.37 with an expected calibration error of 2.1%.
- **Key innovations**:
  - GLiDE family (0.4B–27B) distilled from reasoning teachers via soft-target distillation + progressive post-training.
  - Bidirectional attention enabled by removing causal masking from full-attention layers.
  - Parameter-free recurrent depth for extra inference-time computation without token generation.
  - Pareto frontier performance-vs-size; 27B: score 71.52–73.37, calibration error ≈2%, latency 92.9ms.

### 5. HiSA: Sparsifying the Hidden Dimension of RoPE Attention in LLMs
- **arXiv**: [2611.26363](https://arxiv.org/abs/2611.26363)
- **Date**: 2026-11-19
- **Authors**: Ambroise Borbely, Mathieu Salzmann, Olivier Verscheure
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.LG, cs.CL
- **Abstract**: Attention in large language models (LLMs) scores every query against every key with a full dot product. We investigate whether this dot product must be computed completely for attention to be effective. We propose Hidden Sparse Attention (HiSA), which keeps the query and key projections intact but only computes a partial dot product, following a static, parameter-free rule set by the token positions: attention becomes sparse in the hidden (feature) dimension, an axis much less explored than token sparsity, rather than over tokens as in almost all sparse attention methods. Based on the structure of rotary position embeddings (RoPE), we decompose keys and queries into parts which can be omitted when computing attention. By training LLMs from scratch with HiSA, we find that this partial dot product does not hurt but improves performance compared with the complete product while computing only about a third of the query-key products. During inference HiSA improves decoding speed and shrinks memory footprint. We also extend HiSA to FlashAttention-3 kernels for training and inference. Finally, we motivate our approach by showing that dense attention learns to suppress the attention score parts that HiSA drops.
- **Key innovations**:
  - Sparsity in the **hidden (feature) dimension** of attention — an axis almost unexplored (all sparse attention sparsifies tokens).
  - RoPE-structure-based decomposition: only a third of q·k products computed, accuracy improves or matches dense.
  - FlashAttention-3 kernel extension for training/inference; inference speedup and memory shrinkage.

### 6. dLoop: Looped Diffusion Language Models via Recurrent Latent Refinement
- **arXiv**: [2611.26275](https://arxiv.org/abs/2611.26275)
- **Date**: 2026-11-19
- **Authors**: Handa Li, Pengxiang Li, Mingyu Cao, Xilu Wang, Li Shen, Da Li, Lu Yin
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.CL
- **Abstract**: Diffusion language models (DLMs) support parallel generation, yet they often require many denoising steps because only a fraction of token predictions are sufficiently reliable to be committed at each step. Existing acceleration methods primarily optimize confidence learning or commitment policies. However, these approaches operate on the outputs of a single denoising forward pass, in which information from the prompt, previously committed tokens, and uncommitted positions may not yet be fully integrated. Consequently, some predictions remain under-refined when the commitment decision is made, and modifying the commitment policy alone cannot improve their underlying representations. We introduce dLoop, which restructures a pretrained diffusion language model into a Prelude-Loop-Coda architecture and recurrently applies a parameter-shared intermediate block to the same partially masked state. Rather than advancing the denoising process, each additional loop provides further latent computation, allowing information distributed across uncommitted positions to continue interacting and become more fully integrated before commitment. Experiments on GSM8K, MATH, MBPP, and HumanEval show that dLoop achieves the highest or tied-highest accuracy on every benchmark. With tokens per forward pass (TPF) adjusted for loop computation, it outperforms Fast-dLLM in both accuracy and TPF on all four benchmarks and dParallel on three, and is more accurate than d3LLM on all four, while d3LLM attains higher TPF; no compared method surpasses dLoop in both. Mechanistic analyses show that extra loops mainly help on slow, unstable trajectories and that updates at uncommitted positions drive changes in token decisions and later generation.
- **Key innovations**:
  - dLoop: recurrent latent refinement — parameter-shared loop applies extra latent compute to the partially masked state before commitment.
  - Pre-commitment refinement of predictions that commitment policies alone cannot repair.
  - Wins accuracy-vs-TPF on GSM8K, MATH, MBPP, HumanEval vs Fast-dLLM, dParallel, d3LLM.

### 7. Represented but misread: Post-training changes how language models read out what they represent
- **arXiv**: [2611.26584](https://arxiv.org/abs/2611.26584)
- **Date**: 2026-11-19
- **Authors**: Jochen Laubrock
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.CL, cs.LG
- **Abstract**: Does post-training change what a language model represents, or how this representation is read out into an answer? We compared linear probes with the models' own answers, analyzed with signal detection theory, in six open-weight base models and their post-trained versions. For judgments of whether German texts were written by a human or an AI, probes and word n-gram classifiers separated the classes well, but the answers did not and often ordered the texts inversely. Post-training lowered the sensitivity of the answers on average (Δd′ = −0.34 across model families; −0.29 across three prompts). It also changed the use of a stated base rate: Base models shifted their log-odds by less than the stated change in prior odds, most post-trained models by more. In two models with stage-wise checkpoints, the change occurred during supervised fine-tuning, model stitching implicated the early layers, and from mid-depth on internal states at positions after the text, not those of the text, transferred the change between checkpoints. In a training study, adding 2,000 correctly labeled authorship judgments of news texts to otherwise identical fine-tuning data improved the answers on our newspaper and textbook corpora and inverted them on the chats, where they followed a news-trained probe of the base model. Post-training thus changed how a judgment is read out of what a model represents, and a small training signal can set its direction.
- **Key innovations**:
  - Proves post-training changes **readout** of representations more than the representations themselves (Δd′ = −0.34 averaged).
  - Mechanistic: change surfaces in late-layer post-text positions; a small fine-tuning signal can invert answer direction.

### 8. MemFolder: Structure-Guided Memory Folding for Efficient Agent Memory Management
- **arXiv**: [2611.26427](https://arxiv.org/abs/2611.26427)
- **Date**: 2026-11-19
- **Authors**: Xuyang Liu, Chenwen Lu, Junxi Wang, Siyu Ren, Xinying Lin, Siteng Huang, Hongli Sun, Linfeng Zhang, Honggang Chen
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.CL, cs.CV
- **Abstract**: Long-term agents accumulate large external memory stores as interactions unfold, increasing the costs of storage, retrieval, and response generation. Efficiency is constrained by two coupled factors: a growing record count increases retrieval overhead, while longer retrieved contexts increase prefill computation and decoding-time attention costs. Existing methods prune or consolidate records, but pruning can discard useful evidence, whereas consolidation may produce fewer yet longer retrieval units. We introduce MemFolder, a structure-guided memory folding framework that sequentially reduces record count and context length. The framework comprises two core components that share memory groups, using cross-record structure to guide both evidence consolidation and compact representation. RecordFolder grounds entity mentions, progressively selects representative yet complementary anchors, and combines semantic and entity affinity with temporal chaining to consolidate compatible records into fewer retrieval units. ContextFolder encodes the original records within these groups into compact text and uses verification feedback to revise encodings when key facts cannot be recovered. Experiments on the three text-based memory benchmarks LoCoMo, PersonaMem, and LongMemEval and the two multimodal benchmarks M3-Bench-web and M3-Bench-robot demonstrate the strong performance of our methods. Notably, on Mem0, RecordFolder retains 99.0% of the original average performance across the three text-based benchmarks with 50% fewer records, exceeding the strongest baseline by 1.9 percentage points in performance retention.
- **Key innovations**:
  - MemFolder: structure-guided memory folding with two components (RecordFolder + ContextFolder).
  - RecordFolder: entity grounding + complementary anchor selection + semantic/entity affinity + temporal chaining → fewer retrieval units.
  - ContextFolder: compact encoding of records with verification feedback for unrecoverable facts.
  - On Mem0: 99.0% retained performance with 50% fewer records.

---

## B. Recommendation (5)

### 9. From Sessions to Serving: Integrating LLM-Based Embeddings into Retrieval for Production Content Recommendation
- **arXiv**: [2611.26096](https://arxiv.org/abs/2611.26096)
- **Date**: 2026-11-19
- **Authors**: Zhixiong Hu, Meng Li, Maggie Zhang, Deborshi Goswami, David Bailey, James Bradley
- **Institution/Company**: Autodesk Inc. (explicitly stated in abstract; production system “for autodesk.com”)
- **Categories**: cs.IR, cs.LG
- **Abstract**: Personalized content recommendation on large marketplace websites must reconcile heterogeneous candidate content (e.g., customer stories, product pages, industry pages, and learning content) with sparse, fast-changing user behavior, placing increasing demands on the retrieval stage to represent user interest well, not just the downstream ranking stage. We present LSER (LLM Session Embedding Retrieval), a production content recommendation system for autodesk.com that derives session- and history-level embeddings from a pretrained large language model (LLM) and adds them as auxiliary user-side features in the retrieval-stage user tower alongside existing learned sequence encoders. To keep user-side embeddings fresh under real-time behavior, we build a nearline serving path that asynchronously refreshes sequential and LLM-derived user vectors for our main content recommendation server. We validate the incremental value of the LLM features through an ablation study across our full multi-content-type catalog. Our results indicate that integrating LLM-derived embeddings as additional retrieval signals, together with production-grade nearline serving, is technically feasible and can improve model performances.
- **Key innovations**:
  - LSER (LLM Session Embedding Retrieval) for marketplace content recommendation at Autodesk.
  - LLM-derived session/history embeddings used as auxiliary retrieval-stage user features.
  - Nearline serving path that asynchronously refreshes sequential + LLM user vectors.
  - Ablation across multi-content-type catalog; notes improvement in model performance.

### 10. CACO: Coverage-Aware Coordinated Optimization for Continuous Generative Retrieval
- **arXiv**: [2611.25738](https://arxiv.org/abs/2611.25738)
- **Date**: 2026-11-19
- **Authors**: Pan Zhang, Nan Zhuang, Yongkang Zhang, Kun Xú, Zhongtao Jiang, Zhiwei Wang, Kun Xǔ, Youhuan Li
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.IR
- **Abstract**: Continuous generative retrievers powered by flow matching and diffusion sample multiple queries in item embedding space for parallel approximate nearest-neighbor (ANN) search under fixed retrieval budgets. However, optimizing distribution diversity or target-level interest separation ignores set-level retrieval geometry: sampled queries collapse onto overlapping ANN neighborhoods, while discrete top-K lookup and single-target supervision block end-to-end coverage optimization. We introduce CACO (Coverage-Aware Coordinated Optimization), a lightweight self-supervised post-training framework that coordinates queries from frozen flow-matching and diffusion retrievers toward complementary item coverage with negligible additional inference latency. CACO uses empirical retrieval frequencies across sampled reference queries as a relevance proxy, formulating a label-free coverage objective that improves recall across all 30 backbone-dataset settings in offline greedy selection experiments. To avoid the inference overhead of generating a large query pool, CACO employs a coordinated query adjustment network that combines inter-query bidirectional attention with gated relative directions, finally updating queries by bounded tangent-space projection and spherical retraction. During training, CACO applies tangential antithetic perturbations and measures each query's marginal gain via counterfactual single-query replacement, yielding an unbiased gradient estimator of smoothed set coverage across non-differentiable ANN search. On eight public benchmarks and an in-house 24-partition streaming industrial dataset, CACO improves Recall@100 by up to 23.7% and Recall@400 by up to 23.9% over the strongest baseline, cuts inter-query overlap by 53.3%–64.9%, and adds only 0.5%–3.0% inference latency.
- **Key innovations**:
  - CACO: label-free coverage objective (empirical retrieval frequencies as relevance proxy) for continuous generative retrievers.
  - Coordinated query adjustment network (inter-query attention + gated relative directions + tangent-space projection) → complementary coverage, low latency.
  - Unbiased gradient estimator via counterfactual single-query replacement.
  - Recall@100 +23.7%, Recall@400 +23.9%, inter-query overlap −53.3%–64.9% (8 benchmarks + industrial stream).

### 11. Generative News Recommendation Reproduces Popularity: A Memorization-Based Analysis
- **arXiv**: [2611.25606](https://arxiv.org/abs/2611.25606)
- **Date**: 2026-11-19
- **Authors**: Shotaro Ishihara
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.IR, cs.CL
- **Abstract**: Text-based generative recommenders can go beyond ranking existing items by directly generating item titles or other textual representations. In the news domain, this raises a societal concern that models may repeatedly surface already popular articles and thereby narrow the diversity of information to which users are exposed. We investigate training-data memorization as one mechanism behind this concentration. Using approximately 20 million browsing sessions from a Japanese news service, we continually trained an instruction-tuned Llama 3 8B model to generate the next article title in a session. The generated-title distribution was more concentrated and less diverse than the distribution of titles observed in the browsing logs. Frequently repeated target titles exhibited greater verbatim and approximate memorization, and more strongly memorized titles were generated in response to a wider range of prompts. These findings support a pathway in which popularity in behavioral logs becomes repeated training text, is preferentially memorized, and is subsequently reproduced by a generative recommender. An exploratory target-level deduplication condition reduced both memorization and output concentration, while substantially reducing the training-set size and recommendation accuracy. Our results suggest that popularity bias in generative recommendation may arise not only from user preferences or ranking objectives, but also from the model's tendency to reproduce frequently encountered strings, with important implications for information diversity on news platforms.
- **Key innovations**:
  - Empirically links popularity bias in generative recommenders to training-data memorization of popular titles.
  - Uses signal detection/approximate memorization analysis on ~20M sessions of a Japanese news service.
  - Target-level dedup reduces memorization + concentration; analyses show it also cuts accuracy.

### 12. AutoRAGBench: A Benchmark for LLM Agents Automating RAG System Development
- **arXiv**: [2611.25582](https://arxiv.org/abs/2611.25582)
- **Date**: 2026-11-19
- **Authors**: Hang Zhang, Yuzhi Pan, Ziyao Zhong, Chaokun Wang, Shuo Cao, Zeyu Huang, Yue Xue, Fang Niu, Bofan Xie, Guanchen Ge, Zecheng Li, Leqi Zheng, Ziyang Liu, Wei Wang, Miao Gu
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.CL, cs.AI, cs.IR
- **Abstract**: Retrieval-augmented generation (RAG) is a well-established paradigm for augmenting large language models (LLMs) with information retrieved from external corpora. However, developing effective RAG systems requires substantial engineering effort and iterative experimentation, as effective design choices vary across tasks and domains. With rapid advances in LLM agent capabilities, we ask how well these agents can autonomously build RAG systems and how effectively they can improve them through iteration. In this paper, we propose AutoRAGBench, the first benchmark to evaluate how well LLM agents develop RAG systems from scratch in an open code space. It comprises nine RAG system development tasks. For each task, agents build RAG systems from scratch without starter code or prescribed strategies, under a six-hour budget on a single H800 GPU. They analyze task data, implement RAG pipelines, and iteratively refine their designs based on experimental feedback. We evaluate nine agent configurations and analyze both the effectiveness of the resulting RAG systems and their development trajectories. GPT-6.1 Sol with Codex CLI achieves the highest average score of 56.1. The composite Human-SOTA baseline averages 44.4. These results show that LLM agents can automate effective RAG system development. When starting from a human-designed system on each of seven tasks, GPT-6.1 Sol with Codex CLI improves the score by 16.6 points on average.
- **Key innovations**:
  - First benchmark for LLM agents automating RAG development (9 tasks, 6h/task, 1 H800 GPU).
  - GPT-6.1 Sol + Codex CLI reaches avg 56.1 vs Human-SOTA 44.4.
  - Agents build RAG from scratch; +16.6 points when seeded with human-designed systems.

### 13. LQ-Rec: Late Quantization for Sequential Recommendation
- **arXiv**: [2611.25256](https://arxiv.org/abs/2611.25256)
- **Date**: 2026-11-18
- **Authors**: Satoshi Koide, Yueqi Wang, Julian McAuley
- **Institution/Company**: Toyota Motor North America; UC San Diego (from 2026-11-20 digest)
- **Categories**: cs.IR
- **Abstract**: Generative retrieval (GR) for sequential recommendation compresses each item into a short semantic ID and trains an autoregressive decoder to generate next-item codes from a user history. While appealing for cold-start handling and storage, autoregressive GR suffers a structural scaling limit: typically, longer semantic IDs reduce quantization error in principle but degrade ranking quality and quadratic memory usage against semantic ID length. We propose Late Quantization (LQ), a non-autoregressive paradigm that confines discretization to the output (item) side of the pipeline. The encoder and scoring rule operate in continuous space, while items are stored and matched as semantic IDs produced by an end-to-end-trained residual quantizer. This architectural shift permits an additive error decomposition and a pairwise ordering theorem that jointly bound the quantization-induced ranking drop, a structural guarantee absent in prior semantic-ID recommenders. Across four public benchmarks, the resulting recommender, LQ-Rec, delivers three capabilities simultaneously: ranking quality improves monotonically with the semantic-ID length and outperforms existing baselines; a single trained model supports anytime compression, tuning ranking quality against inference cost without retraining; and LQ-Rec shows superior generalization on a memorization/generalization partition.
- **Key innovations**:
  - LQ (Late Quantization): non-autoregressive generative retrieval; discretization moved to output side.
  - Additive error decomposition + pairwise ordering theorem bounding quantization ranking drop.
  - Quality-vs-ID-length monotonicity; anytime compression without retraining.
  - Stronger generalization on memorization/generalization split.

---

## C. Advertising and CTR (7)

### 14. DNA: Unlocking Depth Scaling in CTR Models
- **arXiv**: [2611.25659](https://arxiv.org/abs/2611.25659)
- **Date**: 2026-11-19
- **Authors**: Caiyuan Li, Wenjie Wu, Yuheng Huang, Xiao Zhou, Silu Zhou, Ke Chen, Zinan Zhao, Xinrui Zeng, Hanmo Xu, Chaoqun Song, Hua Zong, Zongyuan Wu, Hongbin Zhou, Huimin Yi, Zhixuan Zhang, Dan Ou, Haihong Tang (17 others; context: Taobao search)
- **Institution/Company**: Alibaba (Taobao search; inferred from abstract context — "on Taobao search")
- **Categories**: cs.IR
- **Abstract**: Long user behavior sequences are among the strongest signals for click-through rate (CTR) prediction. Cross-attention makes these sequences practical for industrial ranking by keeping compute linear in sequence length. Yet the gains from stacking cross-attention layers taper off: on Taobao search, growing a cross-attention stack from 16 to 28 layers adds only 0.02 percentage points (pt) of AUC. We argue that the key-value side is the bottleneck. Each layer projects the same behavior sequence into keys and values, so adding depth gives the model more reads of a fixed sequence. We propose DNA (Dual-stream Nexus Attention), which lets the sequence itself evolve with depth. At each layer, the request representation (the search query, user features and scene) first reads the sequence. Each behavior token then attends to the updated request representation and uses what it reads to update itself, so the next layer reads a sequence shaped by the current request. The update runs once per request, all candidates share the resulting sequence, and both the reads and the update keep linear complexity in sequence length. At comparable forward FLOPs, DNA improves AUC over cross-attention stacks by 0.08 to 0.26 pt and keeps improving in the depth range where those stacks level off. DNA-4 is deployed in Taobao search. In an online A/B test against the production model, it improves CTR by 0.8% and GMV by 0.5%.
- **Key innovations**:
  - DNA (Dual-stream Nexus Attention): sequence evolves with depth — tokens update themselves from the updated request representation.
  - Unblocks the depth ceiling of cross-attention: +0.08–0.26 pt AUC (16–28 layers, comparable FLOPs).
  - DNA-4 deployed at Taobao; online A/B: CTR +0.8%, GMV +0.5%.

### 15. X-split Argus: Learning Reusable History Tokens for Efficient CTR Prediction
- **arXiv**: [2611.24283](https://arxiv.org/abs/2611.24283)
- **Date**: 2026-11-18
- **Authors**: Alexander Ploshkin, Nikita Stepanov, Alexey Pismenny, Viacheslav Ovchinnikov, Nikolay Savushkin
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.IR
- **Abstract**: Accurate click-through rate (CTR) prediction depends on user representations that capture both persistent preferences and recent intent, yet processing extensive behavioral histories for every ranking request is costly under production compute and latency constraints. We present X-split ARGUS, a framework for ad ranking whose history compressor and online ranker are trained end to end. The compressor encodes past interactions into a compact set of tokens that are computed offline and reused across candidates, while the online ranker scores ads through cross-attention to these tokens and representations of recent events. Training combines an autoregressive loss for click feedback with distillation of candidate-specific click logits from a larger teacher that scores each candidate using the uncompressed history. The number of compressed history tokens and the length of recent history can be adjusted to fit serving compute and latency budgets. Offline evaluation shows a 0.81% relative reduction in normalized entropy (NE) compared with the production baseline. Deployment in a large-scale real-time bidding system increases online inference cost by 15% relative to the production baseline. An online A/B test against this baseline yields relative gains of 4.65% in a business metric reflecting the monetary value of conversions generated for advertisers and 2.96% in clicks.
- **Key innovations**:
  - X-split ARGUS: end-to-end history compressor → offline reusable token sets; online ranker cross-attends to them.
  - Teacher distillation of candidate-specific click logits from uncompressed-history teacher.
  - Budget knobs: compressed token count and recent-history length.
  - Offline NE −0.81%; A/B +4.65% business metric / +2.96% clicks.

### 16. Iterative Scarcity-Guided Exploration: Bootstrapping Generative Auto-bidding from Narrow Support
- **arXiv**: [2611.26060](https://arxiv.org/abs/2611.26060)
- **Date**: 2026-11-19
- **Authors**: Qingmao Yao, Guangzheng Hu, Yusen Huo, Zhilin Zhang, Chuan Yu, Jian Xu, Xu Chu, Bo Zheng, Xiaotie Deng
- **Institution/Company**: Alibaba Group / Ant Group (GitHub code at github.com/alimama-tech/ISGE)
- **Categories**: cs.LG
- **Abstract**: Auto-bidding is a core algorithmic component in online advertising auctions. In practical cold-start settings, iterative training is commonly used to compensate for low-quality, narrowly supported historical data. Unfortunately, in iterative training, representative diffusion-based AI-Generated Bidding (AIGB) methods fail to sustain extrapolation beyond the narrow data support and stagnate at a suboptimal level. In this paper, we theoretically attribute this stagnation to Signal-to-Noise Ratio (SNR) collapse: the weak radial return signal is overwhelmed by a curvature-induced penalty. To break this stagnation, we propose Iterative Scarcity-Guided Exploration (ISGE), which introduces a guidance handoff: as the return signal collapses, scarcity subsequently takes over as an exploratory signal to elevate the SNR above a critical threshold. Specifically, ISGE iteratively alternates between a Judger that assigns scarcity scores to trajectories and an Explorer that performs guided generation of high-scarcity and high-return trajectories, thereby bootstrapping from the narrow support with such self-generated trajectories. Extensive experiments on the industrial AuctionNet benchmark demonstrate that ISGE, starting from cold-start datasets, effectively surpasses the performance of the Full-Dataset baseline within three iterations.
- **Key innovations**:
  - Theoretical attribution of AIGB stagnation to SNR collapse in iterative cold-start training.
  - ISGE: Judger + Explorer alternating; scarcity takes over as the exploratory signal when return signal collapses.
  - Reaches Full-Dataset baseline performance within 3 iterations on AuctionNet.

### 17. CutAgent: Creative-Gene-Driven Planning and Experience-Guided Self-Refinement for High-CTR E-commerce Advertising Video Creation
- **arXiv**: [2611.22418](https://arxiv.org/abs/2611.22418)
- **Date**: 2026-11-17
- **Authors**: Xuyue Huang, Guanbo Huang, Jiasong Feng, Run Ling, Ao Ma, Xi Zhao, Yaoyu Li, Jie Gao, Ke Cao, Wei Feng, Zhanjie Zhang, Hao Wang, Jinghe Hu
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.CV
- **Abstract**: E-commerce advertising video creation requires both high-level creative planning and reliable multi-modal production. However, existing methods often map product attributes directly to scripts or editing decisions without explicitly modeling advertising strategies, narrative structures, and production styles. They also have limited ability to reuse past production failures. To address these limitations, we propose CutAgent, a dual-agent framework that formulates advertising video creation as a Plan–Execute–Self-Evolve process. CutAgent comprises two collaborative agents, GeneAgent and VideoAgent, connected by a structured creative gene that bridges product understanding and video production. GeneAgent maps multi-modal product inputs—textual attributes together with product images—to creative genes that specify narrative units and production rules. To train GeneAgent, we construct CutAgent-70K with approximately 70K samples of product attributes/images, reverse-extracted creative genes, cleaned clip pools, and real-world CTR, and apply high-CTR supervised fine-tuning followed by CTR-guided GRPO. Guided by the generated gene, VideoAgent retrieves category-then-gene failure–correction experiences from a long-term memory as constraints for shot-script planning, then coordinates material retrieval, narration, subtitles, music, and timeline rendering. Independently, a reflection loop diagnoses quality defects, revises deficient production decisions, and writes verified corrections back to memory for later retrieval. Experiments on CutAgent-Eval show that CutAgent outperforms representative baselines in e-commerce advertising video creation, achieving the highest online CTR of 2.21%.
- **Key innovations**:
  - CutAgent: Plan–Execute–Self-Evolve dual-agent framework (GeneAgent + VideoAgent) with structured creative gene.
  - CutAgent-70K (70K samples, reverse-extracted genes, CTR) + high-CTR SFT + CTR-guided GRPO.
  - VideoAgent uses long-term memory of category-then-gene failure corrections; reflection loop writes verified corrections back to memory.
  - Online CTR 2.21% on CutAgent-Eval (highest reported).

### 18. Bajillion: Cryptographic Clearing for Micropayments
- **arXiv**: [2611.21883](https://arxiv.org/abs/2611.21883)
- **Date**: 2026-11-16
- **Authors**: Patrick O'Grady, Guru-Vamsi Policharla
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.CR
- **Abstract**: Much of the web is funded by advertising, a model that erodes as humans delegate browsing to AI agents acting on their behalf. A natural replacement is for agents to pay for what they consume, often a fraction of a cent per request. At the scale of web traffic, this could mean tens or even hundreds of millions of payments per second. We present Bajillion, a clearing protocol for scalable micropayments. A sender signs a payment request, and an untrusted operator answers with a preconfirmation, which promises the receiver that it will be paid. Periodically, the operator closes an epoch by posting only the net effect of its payments on chain. Bajillion guarantees that a malicious operator can only omit payments -- it can never debit a sender beyond what it signed, nor misdirect a transfer. Posted balances are therefore finalized immediately and can be withdrawn. By design, senders never have to raise disputes, making it suitable for ephemeral AI agents. A receiver that is shortchanged can prove that a close omitted a preconfirmed payment, which halts the protocol and lets every user exit with its finalized balance.
- **Key innovations**:
  - Bajillion: scalable micropayment clearing protocol with sender-signed requests + operator preconfirmation.
  - Epoch close posts only net effect; balances finalized immediately; withdrawal allowed.
  - Malicious operator can only omit payments (never overcharge); receivers can prove shortfalls and halt the protocol.
  - Aimed at AI-agent-driven web advertising replacements.

### 19. Who Pays for Product Returns? Advertising and Return Policies
- **arXiv**: [2611.22370](https://arxiv.org/abs/2611.22370)
- **Date**: 2026-11-17
- **Authors**: Sanxi Li, Yufan Wu, Jun Yu, Mingsheng Zhang
- **Institution/Company**: not stated on arXiv
- **Categories**: econ.TH
- **Abstract**: An online marketplace decides how consumers, firms, and the platform share the cost of product returns. We study this decision when the platform earns commissions and sells prominent placement. Consumers inspect, try, and return products; firms bid for the first position and then set prices. Earlier display attracts more trials but can retain a smaller fraction of them. For small positive losses, assigning return costs to consumers raises the value of prominence relative to reimbursing firms by the same amount. Advertising therefore shifts the platform's preferred division of a given return bill toward consumers. We characterize the joint allocation for small positive return losses and give a cost condition under which the platform pays nothing. In markets with frequent returns, the platform can instead share the bill with consumers: a higher commission makes it pay more to encourage shopping and retained sales. Results at finite losses show that advertising can change the optimal policy from firm-paid free returns to full consumer payment, reducing both commissions and consumer surplus.
- **Key innovations**:
  - Ad payment choice shifts optimal return-cost division toward consumers (for small return losses).
  - Cost condition for platform paying nothing (no free returns under advertising).
  - Explanation of welfare implications of AD-driven return-cost policy changes.

### 20. Platform Recommendation and Competition in Search Markets
- **arXiv**: [2611.24464](https://arxiv.org/abs/2611.24464)
- **Date**: 2026-11-18
- **Authors**: Sanxi Li, Jun Yu, Mingsheng Zhang
- **Institution/Company**: not stated on arXiv
- **Categories**: econ.TH
- **Abstract**: Recommendation rules affect both sellers' incentives and the alternatives consumers expect to find. We develop a framework for evaluating these rules with heterogeneous sellers, endogenous pricing and advertising, and costly consumer search. For a broad class of separable recommendation scores, we establish conditions under which a unique market equilibrium exists. Three applications illustrate the use of the framework. A stronger reward for low prices does not necessarily lower equilibrium prices and benefit consumers when products are sufficiently differentiated in qualities. Quality guidance can lower the price of each product and benefit consumers while raising the average transaction price. With heterogeneous match distributions, a reward for the best initial inspection can help consumers with advertising fixed and harm them when advertising adjusts. A two-type design extension shows that no finite optimum over implementable outcomes uses positive weights on both quality and low prices, even when the platform values consumer surplus.
- **Key innovations**:
  - Framework for evaluating recommendation rules in search markets (heterogeneous sellers, endogenous pricing/advertising, costly search).
  - Conditions for unique market equilibria under separable recommendation scores.
  - Three applications: price-reward effects; quality guidance; heterogeneous match distributions.

### 21. Match Rate Is Not Match Quality
- **arXiv**: [2611.23851](https://arxiv.org/abs/2611.23851)
- **Date**: 2026-11-18
- **Authors**: Tobias B. Konitzer, David M. Rothschild
- **Institution/Company**: not stated on arXiv
- **Categories**: econ.EM
- **Abstract**: Third-party identity-resolution vendors commonly emphasize match rate, the share of submitted records they can link to identifiers for advertising activation, as their core metric of quality. Yet a high match rate does not necessarily mean that those matched identifiers belong to the submitted records (i.e., the intended targets). In this paper we explore match quality as an alternative metric to match rate, utilizing a unique data set to evaluate match quality. We are able to compare two demographics, age and gender, from a submitted record (voter files) to the same demographics in self-reported surveys matched to mobile advertising identifiers linked together by two leading identity-resolution vendors. The data and matching was from 2019-20. There is substantial ambiguity in match quality of the returned records. First, both vendors' activation files contain multiple device identifiers per match. Second, match quality among audited pairs (Vendor A) and for explicitly labeled individual-level matches (Vendor B) is only 21.8% and 23.6%, respectively. Utilizing a mixture model that assumes that correct links always agree on these two demographics and incorrect links agree 10% of the time, these rates imply conditional identity-level precisions of approximately 15% and 13%, respectively. This paper utilizes identity-resolution products that are several years old, but the question we address remains fundamental: match rate alone cannot establish whether advertisers are reaching the people they intended. Evaluating identity resolution requires independent evidence of match quality alongside match rate.
- **Key innovations**:
  - Matches records' age/gender to self-reported surveys via mobile device identifiers from two vendors.
  - Audited match-quality rates only ~21.8%–23.6%; mixture model implies identity-level precision ~15%–13%.
  - Positioning: match rate alone cannot establish intended-target reach.

---

## D. Sequential Modeling (3)

### 22. The Window Lever: Longer Observation Windows Outweigh the Observed Effects of Data, Capacity, and Architecture in Customer Behavior Forecasting
- **arXiv**: [2611.26521](https://arxiv.org/abs/2611.26521)
- **Date**: 2026-11-19
- **Authors**: Tara Sowrirajan, Yanqiao Wang
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.LG, cs.IR
- **Abstract**: In our experiments on long-horizon customer-behavior forecasting, a longer observation window outweighed the observed effects of more data, more capacity and newer architectures. The window is the weeks of history a model sees before the week it forecasts from. Going from an 8- to a 16-week window adds a raw +0.070 to 0.107 log-space R² in every family at 1M. Matched test cohorts, which score the same customer-weeks at every window, show this raw comparison understates the gain in every family they cover. The direction holds on five public datasets, four spanning over a year (ridge and our transformer on all five). On our internal data, longer windows admit up to 10% more and colder training customers, which matching does not fix. Our design does not separate window length from calendar coverage, because every test anchor (the week a forecast is made from) falls in one eight-week band. On training-period anchors, the weekly ridge probe's gain persists outside the holiday season, keeping about 72% of it. We therefore report a robust positive association with longer windows and do not identify the magnitude of a calendar-independent history effect. Of four internally registered predictions, the only fully blind one failed. An activity-mixture model predicted +0.014 from 24 to 32 weeks; the weekly-aggregate probe returned −0.0004. For the sequence families, the other three levers are about an order of magnitude smaller, bounded and unresolved. Their observed effects are at most 0.006 between the nominal 1M and 10M tiers and 0.0052 among five sequence families at 16 weeks with clocks as built, both single-seed on the full test split, and 0.006 for capacity on three-seed means. These are observed intervals, not equivalence bounds. Our claim is the order-of-magnitude contrast between the window and those bounds. A team building on this class of data should start by lengthening the window.
- **Key innovations**:
  - "The Window Lever": matched-cohort experiments show longer observation windows dominate data/capacity/architecture effects (+0.070–0.107 log R², 8→16 weeks, at 1M).
  - Robust result across 5 public datasets (4 spanning a year); direction-only claim on the magnitude of a calendar-independent effect.
  - Order-of-magnitude contrast vs. bounded data/capacity effects (<0.006).

### 23. Neural Conditional Gaussian Model: Efficient Data Assimilation with Sequential Uncertainty Quantification for Nonlinear Dynamics
- **arXiv**: [2611.26463](https://arxiv.org/abs/2611.26463)
- **Date**: 2026-11-19
- **Authors**: Chuanqi Chen, Nan Chen
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.LG, math.DS
- **Abstract**: Data assimilation (DA) in partially observed nonlinear systems requires repeated estimation of both hidden states and their uncertainty. Conventional nonlinear filtering can be computationally expensive and often relies on an explicit dynamical model. In this paper, we develop the Neural Conditional Gaussian Model (Neural CGM), a data-driven dynamical model that maps unobserved physical states into a learned latent space, where the dynamics of the latent states follow a conditional Gaussian structure. This structure allows closed-form DA updates in the latent space, while nonlinear encoder-decoder mappings retain the flexibility needed to represent complex dynamics in physical space. A key feature of Neural CGM is its treatment of uncertainty in DA. The latent posterior mean and covariance are mapped to the physical variables through a Gaussian decoder that combines local moment propagation with learned nonlinear corrections. The resulting physical-space posterior statistics depend on the sequentially updated latent distribution rather than on a separate post-processing estimate. The same statistics enter a Gaussian negative log-likelihood during training, so both the posterior mean and uncertainty affect the learned model. Because Neural CGM learns the dynamical model itself, it can also be used for state forecasting and simulation without explicit knowledge of the governing equations. Numerical experiments on benchmark nonlinear dynamical systems show accurate state estimation and forecasting while substantially reducing online assimilation cost relative to conventional nonlinear DA methods. Neural CGM is therefore suited to repeated state estimation, uncertainty quantification, and prediction from partial observations.
- **Key innovations**:
  - Neural CGM: learned latent-space Gaussian dynamics enabling closed-form DA updates; data-driven dynamics (no explicit model needed).
  - Gaussian decoder = local moment propagation + learned nonlinear corrections; uncertainty enters training via NLL.

### 24. Ordinal Hegselmann-Krause Systems
- **arXiv**: [2611.24449](https://arxiv.org/abs/2611.24449)
- **Date**: 2026-11-18
- **Authors**: Martin Hoefer, Tim Koglin, Jakob Lindner, Jannis Schramek
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.GT, cs.DS, cs.SI
- **Abstract**: We study opinion formation in the popular Hegselmann-Krause model when agents replace the traditional averaging update by a median update or more general ordinal aggregation methods. We analyze the convergence properties of synchronous and asynchronous dynamics. For asynchronous dynamics, we show that every HKS with a 1-Lipschitz ordinal aggregation function converges in worst-case time O(n⁴). For the special case of median aggregation and for the family of k-large aggregation functions, in which agents select the k-th largest opinion in their neighborhood, we obtain sharper bounds of O(n³). For general ordinal aggregation, some sequence of O(n²) updates reaches an equilibrium from every initial state. Nevertheless, other update sequences may cycle, and uniform random activation can require exponentially many updates with overwhelming probability. For synchronous dynamics, we obtain a tight characterization. Ordinal aggregation functions satisfying the 1-Lipschitz condition are shown to guarantee convergence in linear time. This result applies to many natural examples such as minimum, maximum, median, and k-large functions. When the Lipschitz condition is violated, there exist instances in which synchronous dynamics do not converge at all.
- **Key innovations**:
  - Ordinal Hegselmann-Krause: median/k-large/Lipschitz ordinal aggregations (vs. average).
  - Async convergence: O(n⁴) (O(n³) for median/k-large); some general aggregations reach equilibrium in O(n²) updates.
  - Sync: Lipschitz aggregations converge in linear time; non-Lipschitz can cycle.

---

## E. Games (3)

### 25. Safe Subgame Resolving in Multiplayer Games
- **arXiv**: [2611.25981](https://arxiv.org/abs/2611.25981)
- **Date**: 2026-11-19
- **Authors**: Boning Li, Longbo Huang
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.GT, cs.AI
- **Abstract**: Poker and other games with hidden information are too large to solve in one pass. Strong systems compute a complete blueprint strategy offline and refine it in real time inside the reached subgame. In 2p0s games, a safety theorem guarantees that subgame resolving never increases how much an adversary can gain by exploiting the resolved strategy relative to the blueprint strategy. With three or more players acting independently, no such guarantee exists yet, and heuristic resolving can increase the profile's best-response gap. We prove the first conditional safety theorem for uncorrelated multiplayer subgame resolving, a post-hoc certificate for any delivered update. The best-response gap of the resolved profile exceeds that of the blueprint by at most four terms. Two concern the resolver: the subgame value the blueprint promised without realizing (A_i^S) and the resolver's subgame solve error (ε_i). The other two are the opponents' best-response gains inside the subgame over their promised values (Σ_q M_q) and a structural tax (Θ), which measures how much the players' total utility can change. The tax is zero in constant-sum games, including every rake-free poker variant. Constructions attain each term with equality. On three-player Leduc poker and on Kuhn poker with up to six players, resolving without a certificate raises the gap beyond a small tolerance in 12% to 100% of the updates. The certificate flags every such update and accepts 41% (Kuhn) and 86% (Leduc) of the standard resolving updates. A resolver that keeps the blueprint whenever the certificate exceeds the tolerance delivers no harmful update. The certificate needs only one best-response pass per opponent inside the subgame, so real-time multiplayer solvers that refine a blueprint can attach it as a safety check.
- **Key innovations**:
  - First conditional safety certificate for multiplayer subgame resolving (best-response gap ≤ blueprint + 4 terms).
  - Tax term zero in constant-sum (rake-free) poker; two resolver terms + two opponent-gain terms.
  - Benchmarks: Leduc (accepts 86% of resolving updates) and Kuhn (41%); 12–100% of standard updates certified as harmful without certificate.
  - Attaches as a safety check to real-time multiplayer solvers (e.g., Leduc poker).

### 26. Closing Gaps in Temporal Fair Division for Chores
- **arXiv**: [2611.25892](https://arxiv.org/abs/2611.25892)
- **Date**: 2026-11-19
- **Authors**: Nicholas Teh
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.GT
- **Abstract**: We study the fair division of indivisible chores that must be assigned in a prescribed order. The complete instance is known in advance, but assignments cannot be changed. Temporal envy-freeness up to one chore (TEF1) requires envy-freeness up to one chore after every arrival. For goods, TEF1 allocations need not exist, and deciding whether one exists is NP-hard. For chores, Elkind et al. (AAMAS 2025) showed that TEF1 allocations exist for two agents, but left open whether they always exist, conjecturing that they do not, and whether deciding their existence is hard. We resolve both questions, confirming the conjecture in a strong form: for every n≥3 and every finite factor, some n-agent instance admits no allocation satisfying TEF1 even up to that factor. This holds even when all agents have the same multiset of individual chore costs, with nine chores sufficing for three agents. Deciding TEF1 existence is NP-complete for every fixed n≥3, even when all costs lie within a factor 1+2⁻ᵐ of one another, where m is the number of chores. Instances without TEF1 allocations exist arbitrarily close to the uniform cost matrix with O(n log n) chores, and just nineteen for three agents. We then relate fairness to social cost. Even when a TEF1 allocation is supplied, minimizing social cost subject to TEF1 admits no polynomial-time approximation within any factor polynomial in the number of chores unless P=NP, already for three agents with strictly positive normalized costs. In contrast, for every fixed number of agents, we give an FPTAS for the optimal temporal EF1 factor, the smallest factor up to which TEF1 can be satisfied, whose output has social cost no larger than that of the cheapest allocation attaining this factor. Thus a slight relaxation of fairness permits a social-cost guarantee that, unless P=NP, no polynomial-time algorithm can provide under exact TEF1.
- **Key innovations**:
  - Proves TEF1 does not always exist for chores (n≥3; 9 chores for 3 agents); NP-complete existence checking (even near-uniform).
  - FPTAS for optimal temporal EF1 factor with social-cost guarantee under slight relaxation.

### 27. Temporal Fair Division: Simultaneous Guarantees for Goods and Chores
- **arXiv**: [2611.23782](https://arxiv.org/abs/2611.23782)
- **Date**: 2026-11-18
- **Authors**: Tianqi Chen
- **Institution/Company**: not stated on arXiv
- **Categories**: cs.GT
- **Abstract**: We study temporal fair division of indivisible items in both the goods and chores settings, with n ≥ 2 agents and nonnegative additive values or costs. Items arrive one at a time and must be assigned immediately and irrevocably. The arrival order and all agents' values or costs are known in advance, and the cumulative allocation must satisfy the fairness requirements after each arrival. For goods, we give a polynomial-time algorithm that simultaneously achieves exact temporal proportionality up to one item (TPROP1), a 1/n approximation to temporal maximin share (TMMS), and a 1/(n-1) approximation to temporal envy-freeness up to one item (TEF1). The TMMS factor is optimal. For chores, we give a polynomial-time algorithm that simultaneously achieves exact TPROP1 and a 2−1/n approximation to TMMS. Classical scheduling lower bounds based on fixed sequences carry over to chores TMMS, establishing the optimality of this factor for n=2,3. For every n ≥ 2, we further show that 2−1/n is the optimal TMMS factor subject to exact TPROP1. For every fixed n ≥ 3 and every finite β≥1, we construct an instance of chores admitting no β-TEF1 allocation.
- **Key innovations**:
  - Goods: simultaneous exact TPROP1 + 1/n TMMS (optimal) + 1/(n−1) TEF1.
  - Chores: simultaneous exact TPROP1 + 2−1/n TMMS (optimal for n=2,3; general optimality proven).
