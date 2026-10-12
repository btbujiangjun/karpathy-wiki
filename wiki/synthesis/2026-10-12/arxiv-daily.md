---
title: arXiv Daily AI/LLM/RecSys/CTR/Games (2026-10-12)
type: synthesis
created: 2026-10-12
updated: 2026-10-12
sources: []
tags:
  - arxiv
  - ai
  - llm
  - recommendation
  - advertising
  - sequential-modeling
  - ctr
  - games
  - daily-digest
---

# arXiv Daily Report (2026-10-12)

Search scope: the arXiv export API has advanced to the **2026-10-09 (Fri) announcement block** — `submittedDate:[20261009 TO 20261010]` returns **1,129 papers**, the first new mailing since 2026-10-08 (Sat/Sun/Mon blocks are not yet indexed: `[20261010 TO 20261013]` → 0). This is therefore a **fresh block**, distinct from the 2026-10-05 → 2026-10-08 window reported by the 2026-10-11 digests. Harvest combined full category sweeps (`cs.AI`, `cs.LG`, `cs.CL`, `cs.IR`, `cs.GT`, `cs.MA`, `cs.MM`, `cs.CY`, `cs.NE`) with 30 topical `all:` sweeps (recommendation, generic/sequential/generative rec, CTR, advertising, auctions, sponsored search, bandits, mechanism design, games, scaling, test-time, agents, GRPO, MCP, RLHF, time-series, sequence modeling). **424 unique papers** collected in the block, **all new to the wiki** (grep-verified 0-hit against the 7,238-ID repo-wide baseline). The **50 featured papers below are all new to the wiki**, spread over eight sections — including, for the first time in several digests, a **non-empty CTR / ad-serving / recommender lane (§6)** with four directly topical papers.

> ⚠️ Metadata note: the arXiv Atom API does **not** expose author affiliations. **Institution/company** is stated only where the abstract, comments, or code link name one; otherwise marked `not stated (arXiv metadata omits affiliations)`, with an author-list hint flagged `unconfirmed` where relevant. One HTTP 429 was observed on a late `all:"user engagement"` query (returned 0; not re-queried).

> ℹ️ Lane note: after several rounds of empty CTR/ads lanes, **§6 is back** — CTR-driven ad-image editing (ECC, #37), industrial recommender feature-deprecation (FORTE, #38), GSP autobidding complexity (#40), and generative recommendation beyond semantic IDs (#36). §5 retrieval and §4 memory/personalization remain the deepest clusters, and §2 (RLVR/GRPO family) is again the most crowded section with three new trust-region/divergence papers (#10–#12) plus cross-tokenizer and multi-teacher OPD (#13–#14).

## Core AI / LLM / Agents

### 1. Can Language Models Play the Wikipedia Game?
- **Authors**: Alexander Hickey, Joanna Knight, James Bishop
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI; cs.IR
- **Abstract**: Tests LLMs and embedding models on the Wikipedia Game (reach a target article using only article links) as an information-retrieval proxy requiring specialist knowledge. Builds very large local graphs of Wikipedia pages and of paper citations from OpenAlex, with released code, so navigation can be studied without third-party APIs. Compares against human and TF-IDF benchmarks across five Wikipedia languages and five academic-literature datasets.
- **Key innovations**: No model significantly outperformed humans, but the best models (GPT-o3 mini, GPT-4o, QwQ:32B, DeepSeek-R1:70B) reached comparable success; rankings and performance vary sharply across languages and topics. 64 pages, 17 figures, 10 tables.
- **arXiv**: https://arxiv.org/abs/2610.13948

### 2. RSI-Anything: Unlocking Recursive Self-Improvement with World Models
- **Authors**: Taoyong Cui, Pinxian Zeng, Wanghan Xu, Hao Xiao, Shuhan Xue, Qiang Gao, Wanli Ouyang, Pheng Ann Heng, Zhenfei Yin, Yingcheng Wu, Ling Yang
- **Institution**: not stated (Gen-Verse org, github.com/Gen-Verse/RSI-Anything; CUHK-adjacent author list, unconfirmed)
- **Subjects**: cs.CL
- **Abstract**: Recursive self-improvement (RSI) aims to turn interaction experience into persistent gains, but external feedback is costly and world-model predictions go stale as policies evolve. RSI-Anything built on JEPA-Anything uses predictive world models to guide action and learning-data selection, with component/compatibility checks governing which updated policy-model pairs are retained.
- **Key innovations**: In code repair with a frozen coder, success rises 26.3% (static verifier) → 29.2% (predictive selection) → 31.2% (world-model adaptation) at comparable test usage; GUI tasks complete more with average actions down 39.4%; lab-planning scores more than double across five policy versions (21.80% → 46.01%); in reaction optimization, 96.15% mean best observed yield vs 82.16% for Bayesian optimization under the same 40-experiment budget. Includes an end-to-end immune-science application.
- **arXiv**: https://arxiv.org/abs/2610.13912

### 3. RoleWorld: Knowledge Transfer in World Modeling with Functional Role Abstractions
- **Authors**: Boyuan Xiao, Pu Wang, Ji Feng, Yao-Xiang Ding
- **Institution**: not stated (project: future-item.github.io; unconfirmed)
- **Subjects**: cs.AI
- **Abstract**: Symbolic world models organize dynamics as rules/programs, which in principle transfer across environments, but existing approaches tie knowledge to environment-specific objects. RoleWorld instead uses reusable prototypes plus environment-specific parameter values as **functional role abstractions** for how objects behave in interactions. A teacher LLM extracts role prototypes and transition rules from trajectories, plus a skill guiding the actor; in a target world the actor applies the skill with its current role assignments, actively testing role hypotheses when uncertainty matters — with no LLM parameter updates and fixed transition rules.
- **Key innovations**: Robust generalization on MARS across environments with significantly altered object behavior, suggesting functional role abstractions are an effective transfer component for world modeling.
- **arXiv**: https://arxiv.org/abs/2610.13172

### 4. Mitigating Capability Degradation in LLM Self-Improvement via Representation Geometry Regularization
- **Authors**: Jiaqi Tian, Ting Long
- **Institution**: not stated (code: github.com/supermachinelearner/RGR)
- **Subjects**: cs.AI
- **Abstract**: On-Policy Self-distillation (OPSD) lets one LLM serve as both teacher and student, but this work shows OPSD methods progressively degrade earlier-acquired capabilities — queries correct at earlier training stages become wrong later, even as aggregate performance improves. The degradation coincides with deteriorating representation geometry: reduced intra-cluster compactness and inter-cluster separation.
- **Key innovations**: Representation Geometry Regularization (RGR) preserves geometry during post-training by encouraging within-cluster compactness and cross-cluster separation, plugging into existing OPSD methods without changing their optimization. Generally alleviates capability degradation while retaining capability improvements across multiple OPSD methods and benchmarks.
- **arXiv**: https://arxiv.org/abs/2610.12855

### 5. Competence-Aware Orchestration for LLM-Based Multi-Agent Systems
- **Authors**: Songmiao Wang, Yuchen Wang, Chenglin Yu, Hongxia Yang, Ming Li
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: More collaboration is not always better for LLM multi-agent systems — richer coordination helps on hard cases but adds token cost and redundant interactions. This work proposes a two-stage framework that models the LLM backbone's task-conditioned competence on the current query, then uses that signal to adapt role activation and the communication graph.
- **Key innovations**: Across six benchmarks, average score 93.81%. With six LLM backbones, collaboration adapts to inferred competence: for high-competence backbones accuracy rises 87.22 → 89.97 while token cost drops 36.26%; for low-competence backbones it adds a further 4.58 points over existing methods. Holds on unseen backbones.
- **arXiv**: https://arxiv.org/abs/2610.13144

### 6. Host-Aware Web Crawling for LLM Pretraining Data
- **Authors**: Malte Ostendorff
- **Institution**: not stated (accepted at WaC-13 @ EMNLP 2026)
- **Subjects**: cs.CL
- **Abstract**: Web-crawling pipelines discard much of what they crawl; this paper asks how a crawler should allocate budget across and within hosts to collect more high-quality pretraining data. Combining document-level quality classifier scores, web-graph centrality, and Common Crawl's per-host coverage, roughly **half the variation in classifier scores is between hosts**; a few sampled pages estimate a host's remaining quality well.
- **Key innovations**: Simulated crawls show common centrality-based host selection yields limited gains over random ordering (sometimes worse); sampling a few pages then fetching deeper from top-scoring hosts collects **several times more high-quality pages per fetch** than uniform-depth or centrality-based allocation. Estimates tens of millions of high-quality pages remain among known-but-uncrawled URLs, concentrated on a small share of hosts.
- **arXiv**: https://arxiv.org/abs/2610.13321

### 7. Agentic Large Language Models
- **Authors**: Max van Duijn, Michiel van der Meer, Aske Plaat, Niki van Stein
- **Institution**: not stated (textbook; Leiden-adjacent author list, unconfirmed)
- **Subjects**: cs.AI
- **Abstract**: A 472-page textbook on agentic LLMs — on how language models can act directly in the world, interact with each other, and what that means for users — covering how agentic LLMs work, act, and interact.
- **Key innovations**: Full-length open textbook (472 pages) consolidating the agentic-LLM landscape: architectures, acting, interaction, and implications.
- **arXiv**: https://arxiv.org/abs/2610.13455

## Reasoning / RL / Post-Training / Test-Time

### 8. Rollout-Time Intervention: Unlocking Agentic Reinforcement Learning Beyond Policy Limits
- **Authors**: Chen Xi, Ding Ruixue, Wang Zhigaoyuan, Zhang Fanrui, Zhang Qiang, Chen Boli, Wang Shihang, Wang Tianfu, Ren Ailin, Wang Pengyong, Xie Pengjun, Xiong Hui
- **Institution**: Alibaba (Alibaba-NLP; code: github.com/Alibaba-NLP/qqr)
- **Subjects**: cs.AI
- **Abstract**: Agent RL for LLMs hits an on-policy reasoning bottleneck: tasks beyond the model's capability boundary yield extremely sparse successful trajectories, so training collapses. Rollout-Time Intervention (RTI) uses reward-side evidence (evaluation rubrics) during rollout to convert erroneous trajectories into successful ones, providing learning signals for tasks the policy rarely solves alone.
- **Key innovations**: Off-policy intervention trajectories effectively guide policy optimization when large-distribution-shift trajectories are filtered out. Across five benchmarks RTI consistently beats RL baselines, letting the post-trained policy approach substantially stronger contemporary LLMs and transcend its original capability boundary.
- **arXiv**: https://arxiv.org/abs/2610.13438

### 9. AdaC-GRPO: Towards Mastering Long-Horizon Visual Sudoku Puzzles via Adaptive Curriculum Learning
- **Authors**: Sida Li, Yuanxin Liu, Linli Yao, Shicheng Li, Xu Sun, Haoli Bai, Xiaohui Li
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: RLVR improves LLM reasoning but is underexplored on long-horizon multimodal tasks. Visual Sudoku requires multi-step deduction over local constraints and global dependency chains; frontier MLLMs fail on complex 9×9 boards, and this near-zero success rate causes reward sparsity that halts standard RLVR.
- **Key innovations**: Introduces **FG-Sudoku**, a fine-grained benchmark categorized by grid size and required deductive steps, and **AdaC-GRPO**, which adaptively builds training batches by tracking the model's Zone of Proximal Development via online rollout accuracy. Qwen2.5-VL-7B approaches Gemini-2.5-Flash and bridges 62.2% of the accuracy gap to Gemini-2.5-Pro; generalizes to InternVL-3.5 and Qwen3-VL.
- **arXiv**: https://arxiv.org/abs/2610.13184

### 10. Generalized Proximal Policy Optimization: Unifying LLM RL Algorithms from the Perspective of Divergence
- **Authors**: Zhicheng Cai, Xinyuan Guo, Hanlin Wu, Weinan Dai, Yuyan Zhou, Wei-Ying Ma, Ya-Qin Zhang, Hao Zhou
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG; cs.AI
- **Abstract**: PPO's clipping proxy is geometrically degenerate — it cannot adapt resistance to policy shifts, causing premature clipping and degraded exploration; later variants fix this via fragmented heuristics. The paper proposes Generalized Proximal Policy Optimization (GPPO), a unified framework understood through the lens of divergence, with generalized **$f$-divergence trust-region theory** and a monotonic improvement guarantee. New estimator topologies give more faithful divergence estimates than single-sample Monte Carlo.
- **Key innovations**: PPO, DAPO, DPPO, and RIPO emerge as special cases — a principled **{Divergence × Estimator}** design space. On eight competition-level math and coding benchmarks both dimensions matter; the best GPPO instantiation beats standard GRPO by up to **50% (math) and 14% (coding)**, SOTA.
- **arXiv**: https://arxiv.org/abs/2610.13015

### 11. Trajectory-Aware Policy Optimization: Closing the State Distribution Gap in Long-Horizon LLM RL
- **Authors**: Zhicheng Cai, Weinan Dai, Yuyan Zhou, Wei-Ying Ma, Ya-Qin Zhang, Hao Zhou
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG
- **Abstract**: Long-horizon autoregressive rollouts let local policy mismatch compound into severe state-distribution shift; GRPO/GSPO control mismatch at token/sequence level but ignore this trajectory-induced shift, causing instability and collapse as horizon grows. Trajectory-Aware Policy Optimization (TAPO) derives the state-distribution correction from the off-policy policy gradient and folds it into the RL objective.
- **Key innovations**: Uses a geometric-mean estimator for variance reduction plus length-aware dynamic clipping preventing overly deviated trajectory updates. Beats existing LLM RL algorithms on eight competition-level benchmarks — up to 48% and 12% over GRPO on math reasoning and algorithmic coding, with markedly better training stability.
- **arXiv**: https://arxiv.org/abs/2610.13020

### 12. Matched-Context Group Policy Optimization for LLM Agent Training
- **Authors**: Chenxu Zhang, Yaorui Shi, Wenlong Zhang, Jianchao Tan, Zihan Wang, Yiming Cheng
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Training long-horizon LLM agents needs credit assignment to intermediate decisions from sparse terminal feedback; useful comparisons between sibling rollouts depend on their context and the evidence entering learning. Matched-Context Group Policy Optimization (MCGPO) builds weighted action preferences from already-collected trajectories, using pre-action state summaries and observed rubric progress as comparison contexts.
- **Key innovations**: Two-action support with ordered exact/coarse matching; fixed folds separate candidate decisions from terminal outcomes; support-dependent evidence weights scale an auxiliary pairwise objective beside shared GraphGPO. Across six environment-backbone settings: +0.47–1.46 pts over matched GraphGPO on ALFWorld/WebShop with Qwen2.5-1.5B/7B, +3.96/5.16 pts on WebShop with Qwen3-4B/8B — critic-free, reusing rollout data.
- **arXiv**: https://arxiv.org/abs/2610.13755

### 13. CAST: Credit Alignment for Cross-Tokenizer On-Policy Distillation
- **Authors**: Jingru Yang, Jinhang Wu, Minjing Shi, Shengfeng He, Xuyan Li, Man Tan, Biye Li
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG; cs.CL
- **Abstract**: Cross-tokenizer on-policy distillation (OPD) needs teacher/student sequence alignment before scores can be compared. Decoded-text alignment gives chunk-level correspondence but leaves **credit alignment** unresolved: how a chunk-level signal distributes across student tokens, while tokens with no teacher correspondence stay unconstrained.
- **Key innovations**: CAST (Chunk-aware credit Assignment with Selective Token Anchoring) redistributes each chunk's advantage via predictive uncertainty and local teacher-signal smoothness (exact solution of a KL-regularized credit-allocation problem), and anchors unaligned positions to the initial policy with a KL penalty. Improves best baseline by 2.45/1.32 pts cross-tokenizer (Qwen3-8B → Mistral-7B / Llama-3.1-8B) and 2.10 pts shared-tokenizer (→ Qwen3-1.7B) across math/science/code benchmarks.
- **arXiv**: https://arxiv.org/abs/2610.13257

### 14. Beyond Domain-Routed Supervision: Cross-Teacher Guarding for Multi-Teacher On-Policy Distillation
- **Authors**: Shi-Yu Tian, Yong Liu, Ximan Liu, Tianrui Zhu, Sule Bai, Xinwei Yang, Ruiqi Liu, Kun-Yang Yu, Ming Yang, Zhi Zhou, Yu-Feng Li, Yipeng Sun, Gu Simiu
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: Multi-teacher OPD (MOPD) routes domain-specific data to specialized teachers, but all updates still hit shared parameters; teachers differing strongly in style/expertise cause persistent gradient conflicts and capability degradation. Road MOPD adds non-routed teachers as auxiliary cross-domain critics on the same trajectories, coordinating supervision via token-level credit assignment and gradient updates.
- **Key innovations**: Cross-teacher-guided credit assignment (teacher-agreement strengthens jointly-supported corrections, attenuates conflicts) + preventive multi-teacher gradient projection with adaptive strength. Mitigates degradation in the disadvantaged domain, gains >5 percentage points under high conflict, improves overall performance in low-conflict and three-domain settings.
- **arXiv**: https://arxiv.org/abs/2610.13521

### 15. S$^3$R: Fast and Faithful RL Rollouts via Self-Sparse Speculative Decoding
- **Authors**: Yuhang He, Hongyu Ge, Zihan Lin, Siyi Liu, Yongqi Zhang
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG; cs.CL
- **Abstract**: In profiled RLVR workloads, attention is 72–76% of autoregressive decoding kernel time. Sparse attention cuts the reads, but sampling straight from a sparse policy changes the response groups used for learning — and for group-relative optimization, even exact response-wise reweighting does not recover the dense-policy update (each response's advantage depends on group-mate rewards).
- **Key innovations**: Self-Sparse Speculative Rollouts (S$^3$R): sparse-attention proposals + full-attention verification + exact speculative sampling, sharing one policy (no drafter training), so response groups follow the dense-policy distribution. KV-aware scheduling limits KV-cache thrashing. On long-context math with Qwen3, **1.39×** training throughput vs autoregressive rollouts at comparable performance; aggressive direct sparse sampling becomes unstable where S$^3$R stays stable.
- **arXiv**: https://arxiv.org/abs/2610.13202

### 16. A Critical Look at Power Sampling when Test Time Sharpening LLMs
- **Authors**: Abiel Malkani Talwar, Christopher Nemeth, Henry Moss
- **Institution**: not stated (Lancaster/Intel-adjacent author list, unconfirmed)
- **Subjects**: stat.ML; cs.LG
- **Abstract**: RLVR mostly sharpens distributions — concentrating mass on reasoning paths the base model already produces. Recent work seeks the same gains without reward signals by sampling $π_α ∝ π_{\rm base}^α$ via MCMC/SMC; this paper shows those samplers fail to converge to $π_α$ under realistic compute budgets and their gains are largely recreated by simple Best-of-$N$.
- **Key innovations**: Directly tests the power-distribution target by fine-tuning the base model to match $π_α$ (far more faithful than existing samplers): gains are noisy and specific to certain models/tasks. Conclusion: the value of power sampling lies not in faithfully targeting $π_α$ but in the simpler goal of extracting sequences the base model already deems likely.
- **arXiv**: https://arxiv.org/abs/2610.13653

## Efficiency / Inference / Serving / Quantization

### 17. zip2zip++: Towards Inference-Time Token Compression with Minimal Quality Loss
- **Authors**: Saibo Geng, Andrea Gentilini, Xinxian Ma, Nathan Ranchin, Yunzhen Yao, Robert West
- **Institution**: EPFL (EPFL DLAB; code: github.com/epfl-dlab/zip2zip-plus-plus)
- **Subjects**: cs.CL
- **Abstract**: On-the-fly LZW dynamic vocabularies compress text into fewer tokens but hurt reasoning and perplexity. The paper shows this gap is not inherent — it can be substantially closed by improving the compression layer and LZW codec without touching the pretrained model. Four root causes: (1) LZW conflicts input vs output embedding; (2) naive RoPE ignores that merged tokens span multiple tokens; (3) merging digits disproportionately hurts accuracy; (4) dynamic vocabularies create segmentation ambiguity in evaluation.
- **Key innovations**: Decoupled input/output dynamic embedding layer + size-aware RoPE positioning + modified LZW codec with selective merges and multi-view segmentations. Across four models, perplexity improves on every corpus and math reasoning accuracy rises, closing roughly **half the quality gap** between zip2zip and uncompressed baselines at similar compression ratio.
- **arXiv**: https://arxiv.org/abs/2610.13605

### 18. Orthros: Phase-Aware Heterogeneous Attention for Efficient Transformers
- **Authors**: Yuhong Chou, Zehao Liu, Yuqi Pan, Qian Liu, Xianwei Chen, Zhongzhu Zhou, Jibin Wu
- **Institution**: not stated (NeurIPS 2026 paper, preprint with lab template)
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Linear/window attention reduces complexity but degrades in-context recall, forcing interleaved full-attention layers that keep the quadratic bottleneck in long-context processing. Orthros shifts the paradigm from structural allocation to **phase-aware decoupling**: one unified module dynamically switches computation across sequence-processing phases — linear-complexity prefill, full attention decoding.
- **Key innovations**: Lower asymptotic complexity in heavy-prefill/light-decode long-context regimes; data-efficient Transformer→Orthros conversion that even surpasses the original; **21.9× prefill speedup** with end-to-end gains, near-perfect 128K needle-in-a-haystack, Transformer-level in-context recall. Scalable across model sizes.
- **arXiv**: https://arxiv.org/abs/2610.13735

### 19. RAMP: Recurrent Adaptive Mixed Precision for Efficient Prefill in Recurrent-Depth Language Models
- **Authors**: Ke Wan, Chen Chen
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.CL
- **Abstract**: Recurrent-depth LLMs refine internal representations by re-applying a shared network, which inflates long-context prefill cost. Quantizing weights-and-activations accelerates this, but repeated quantized computations accumulate numerical perturbations along the recurrent trajectory.
- **Key innovations**: Systematic error-propagation analysis shows errors introduced earlier are attenuated by more subsequent steps, so **early recurrent refinement in low precision + high precision for terminal refinement** gives the best fidelity at matched budget. RAMP preserves near-full-precision prefill quality up to 4K context with up to 1.16× first-prefill speedup on H100 (13.9% latency cut).
- **arXiv**: https://arxiv.org/abs/2610.13041

### 20. DuoRate: Two-Rate Per-Expert Precision Allocation for Mixture-of-Experts Serving
- **Authors**: Mengqi Guo, Zhe Wei, Yuan Yuan, Jiunn Bin Lim, Boyi Pan, Michael Bi Mi
- **Institution**: not stated (Huawei-adjacent author list, unconfirmed)
- **Subjects**: cs.LG
- **Abstract**: MoE serving pays expert precision twice: resident footprint covers every reachable expert; decode reads only selected experts — two different rate functionals over the same widths that published allocators constrain only for storage. This **store-read gap**: in the released BitsMoE checkpoint, 2.54 bits/weight of storage become 7.50 bpw of decode traffic.
- **Key innovations**: DuoRate stores one uniform prefix-readable tier, profiles a workload's own prefill, and solves a Lagrangian rate-distortion allocation under the decode functional; routing frequency cancels from every per-expert decision (one dot product + bisection). On Qwen3-30B-A3B, reading 2.3 bpw beats every 2-bit baseline by 6.3–47.0 pts; at 2.9 bpw matches 4-bit formats reading 1.4–1.6 bpw more; on GSM8K trails BF16 by only 0.25 pts.
- **arXiv**: https://arxiv.org/abs/2610.13328

### 21. DualQuant: Dual-scale Calibration-free Weight-and-Activation Quantization for LLMs
- **Authors**: Mahsa Salmani, Sayeh Sharify, Hesham Mostafa
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Native-4-bit accelerators need both weights and activations quantized, but activation quantization is hard and typically needs calibration data. DualQuant is a dual-scale, calibration-free PTQ framework that minimizes weight-reconstruction MSE and, as a by-product, derives per-channel activation rescalings.
- **Key innovations**: Solves the weight-reconstruction problem via variable splitting + block coordinate descent (closed-form subproblems); first dual-scaling method formally supporting the full **MX family and NVFP4** formats. Matches/beats calibration-based SmoothQuant across Llama/Qwen on WikiText-2, C4 and zero-shot tasks; real packed W4A4 path on RTX 4090 delivers up to 2.61× memory reduction and 2.46× throughput over BF16 at fake-quant accuracy.
- **arXiv**: https://arxiv.org/abs/2610.13767

### 22. ReplaySSM: Cache SSM Inputs, Not State
- **Authors**: Ze-Wei Li, Harris Nover, Amey Naik, Andrii Skliar, Igor Shovkun, Ido Shahaf, Tri Dao
- **Institution**: not stated (Princeton/Together-adjacent author list, unconfirmed; code: github.com/Johnny-Liou/ReplaySSM)
- **Subjects**: cs.LG; cs.AI
- **Abstract**: SSMs keep a fixed-size recurrent state, but reading/writing it every decoding step bottlenecks hybrid models: large state I/O with low arithmetic intensity, no cheap speculative rollback, and state-quantization error feeds later updates. ReplaySSM unrolls the recurrence, representing state as a checkpoint plus a buffer of recent SSM inputs.
- **Key innovations**: Periodic checkpoint updates roughly halve dominant state-memory traffic; speculative rollback becomes a buffer-pointer op; output-only verification; low-precision checkpoint for output computation while a high-precision one serves updates (so rounding error never propagates). In vLLM for Mamba-2 and Gated DeltaNet at batch 256: **1.20–1.47×** decode vs tuned baseline across four hybrid models, ~1.8× speculative throughput on 120B-class models, lower KL/downstream loss.
- **arXiv**: https://arxiv.org/abs/2610.13778

### 23. PreSTO: Predictive Subtree Prefetching for Fast LLM Power Sampling
- **Authors**: Nan Jiang, Panagiotis Theodoropoulos, Wei Deng
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.CL
- **Abstract**: Power sampling sharpens the base distribution for better test-time reasoning, but its Metropolis–Hastings kernel is sequential — every accept/reject sets the state for the next proposal. PreSTO prefetches future proposals and **provably leaves the MH transition kernel unchanged**, viewing future outcomes as a tree of accept/reject decisions.
- **Key innovations**: Batches proposals of a prefetched subtree in one model call, then follows the realized path with the original accept rule; a **predictive traversal rule** exploits that MH reaches a sparse, nearly-unarized part of each subtree. Median speedups 1.71×/1.91×/2.33× on PowerMH/EntropyCut/MultiTryMH across seven datasets and five base LLMs; with Qwen3.5-9B on LCB V6 the predictive rule is a further 1.25–1.37× faster than breadth-first.
- **arXiv**: https://arxiv.org/abs/2610.13171

## Memory / Personalization / Long-Context Agents

### 24. Test-Time Memory Construction
- **Authors**: Zijun Wang, Yifan Ji, Haidong Xin, Zhenghao Liu, Yukun Yan, Zulong Chen, Yu Gu, Ge Yu, Maosong Sun
- **Institution**: OpenBMB (Tsinghua-affiliated; code: github.com/OpenBMB/T2Mem)
- **Subjects**: cs.CL
- **Abstract**: LLMs struggle over long interaction histories where evidence scatters across distant sessions; existing memory systems build representations offline before queries arrive, incurring overhead and failing to adapt to query-specific needs. T$^2$Mem defers memory construction to inference and builds memory progressively along the reasoning process.
- **Key innovations**: Lightweight episode-level metadata offline (key events + temporal associations as retrieval cues) with links back to raw interactions; at test time the LLM adaptively retrieves and organizes metadata and interactions. Consistently outperforms strong baselines on LoCoMo and LongMemEval across backbones, with substantially lower construction overhead.
- **arXiv**: https://arxiv.org/abs/2610.13348

### 25. Temporal Evidence Forests for Long-Horizon Multi-Party Conversational Memory
- **Authors**: Junyou Guo, Chongyang Tao, Yan He, Yong Wang, Shuai Ma
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.CL
- **Abstract**: Long-term multi-party interactions accumulate dense, repeatedly-updated information, so temporal structure is critical: relevant info clusters in short intervals, and state transitions are anchored by strict temporal order. Existing temporally-aware memory frameworks store time as metadata or use it only to guide retrieval — they don't use temporal structure to both recover locally-concentrated evidence and reconstruct the full event progression.
- **Key innovations**: T-Mem uses Temporal Evidence Discovery (local message concentration to recover overlooked evidence), Temporal Memory Structuring (models state transitions/relations over time, compresses low-information spans into an evidence forest), and Evidence Forest Linearization for answer generation. Outperforms competitive memory frameworks across LLMs, parameter settings, domains, and query types on two long-term multi-party memory benchmarks.
- **arXiv**: https://arxiv.org/abs/2610.12874

### 26. Double-Take: Improving Capacity, Binding, and Selectivity In Long-Context Within Bidirectional Memory
- **Authors**: Vakul Raghavan, Utkarsh Grover, Mingyang Mao, Chengwen Wang, Xiaomin Lin
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG; q-bio.GN; q-bio.QM
- **Abstract**: Extending context length does not guarantee distant information stays usable: a fixed-size memory must store many associations, connect information across positions, and preserve relevant structure. Identifies two failure modes in large-chunk test-time training (TTT): single-step writes accumulate interference (limits capacity); self-associative writes cannot form cross-position bindings.
- **Key innovations**: Double-Take (DT) fixes these with multi-step unpinned updates and cross-position mixing, plus bidirectional change-sensitive writes for selective retention. Recall goes from the 0.10 chance floor to 0.92 when binding is added; trained on 32kb genomic contexts, DT reaches 0.927 AUROC at 131kb and 0.856 near 1Mb, transferring zero-shot from human to mouse.
- **arXiv**: https://arxiv.org/abs/2610.13073

### 27. LongHarness: Advancing Agentic Reasoning over 100M-Token Corpora via Stateful Evidence Management
- **Authors**: Songtao Huang, Zhijie Zhong, Xiaohan He, Shuaiyu Zhang, Zhiyin Yu, Li Kang, Heng Zhou, Yutao Fan, Xiangchao Yan, Bo Zhang, Shiyang Feng
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: Corpus-scale reasoning requires acquiring and integrating evidence beyond the context window; existing harnesses entangle evidence and conclusions in a growing interaction history, causing unbounded exploration and evidence-state drift. LongHarness makes the evidence/conclusion interplay explicit via **Evidence-Conclusion Coevolution** plus Evidence Lifecycle Management.
- **Key innovations**: Unresolved conclusions guide exploration toward missing information while new evidence strengthens/revises the conclusions that directed the search. On OfficeQA Pro V1/V2 and AA-LCR with GLM-5.3-Flash: exact match 15.8% → 60.2% (V1) and 4.4% → 61.1% (V2) vs direct reasoning; beats Claude Code by 12.0 pts (V1) and Codex by 18.9 pts (V2); Qwen3.8-Flash reaches 61.7% on V1, +8.3 over Claude Code.
- **arXiv**: https://arxiv.org/abs/2610.13075

### 28. RegulaTutor: A Theory-Informed Framework for Long-Term Personalized Learning
- **Authors**: Yonggang Li, Boqian Han, Rui Sheng, Yushi Sun, Zixin Chen
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: Long-term tutoring requires translating a learner's evolving history into instructional support, but the pedagogical rationale linking evidence to teaching strategy is often implicit. RegulaTutor operationalizes self-regulated-learning research into a cognitive-affective-metacognitive-motivational (CAMM) framework that derives evidence-supported learner interpretations and teaching policies, with policies retaining links to evidence and updating as observations arrive.
- **Key innovations**: PairRoute, an offline refinement procedure, uses intermediate execution records to distinguish harness/model/mixed failures, proposing targeted revisions and reviewed stage-level supervision for confirmed model failures. Improves historical-evidence accuracy, learner diagnosis, and judged teaching quality; endpoint improvement in standalone-model evidence accuracy over the refinement trajectory.
- **arXiv**: https://arxiv.org/abs/2610.13399

### 29. DP-MIND: Differentially private memory-guided Long context Inference
- **Authors**: Zhihao Liu, Yitian Cheng, Shuang Liu, Rui Wen, Yuke Hu, Zhan Qin
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: LLM-as-a-Service puts user queries at privacy risk; differential privacy protects them, but existing DP inference targets short/moderate contexts and degrades badly on million-token inputs. DP-MIND scales DP inference to million-token contexts by locally perturbing input and processing chunk-by-chunk with a compact task-relevant memory.
- **Key innovations**: Memory construction policy is optimized directly on perturbed inputs via RL (rewarded by final-answer correctness and memory consistency); a local denoising module recovers perturbation-corrupted answer spans without exposing the original context. Theoretical privacy analysis plus empirical wins over DP and long-context baselines at up to million-token scale.
- **arXiv**: https://arxiv.org/abs/2610.13132

### 30. Training User Simulators with Latent Intrinsic Feedback
- **Authors**: Tarek Naous, Craig Boutilier, Wei Xu, Ofer Meshi
- **Institution**: not stated (Google-adjacent author list, unconfirmed)
- **Subjects**: cs.CL
- **Abstract**: User simulators are emerging as environments for training assistants, but prior work focuses on generating realistic utterances rather than direct feedback on assistant responses. This work introduces simulators with **intrinsic feedback** — latent evaluation states (internal thoughts, reactions, scalar ratings) evaluating the assistant from a first-person user perspective each turn.
- **Key innovations**: Trained on real user/assistant interaction logs; improves simulation realism and critiquing vs prompted baselines, adds turn-level evaluations fine-tuned simulators lack, and correlates better with human judgments than same-size prompted simulators. Provides effective reward signals for multi-turn RL — matching external-judge-LLM reward setups while **cutting RL compute by more than half**.
- **arXiv**: https://arxiv.org/abs/2610.13617

## IR / Retrieval / Ranking

### 31. Beyond the Final Embedding: Retrieving Memories from Token-Level Evidence
- **Authors**: Han Luo, Zhan Zhuang, Xu He, Jujia Zhao, Yu Li, Suqin Yuan, Dong Li, Lei Feng
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.IR; cs.CL
- **Abstract**: Most embedding-based retrievers compare single-vector representations even when relevance hinges on a small part of content. Since the contextual token representations already exist inside embedding models, matching can happen at the token level.
- **Key innovations**: Training-free sparse token matching — each query token retrieves a small set of matching tokens across candidates; scores aggregate per memory and combine with whole-memory similarity. Optional low-rank query adapter (encoder/stored representations fixed) adds 13.3/14.3 points on average Recall@10/NDCG@10 for Qwen3-Embedding-4B. Improves retrieval on eight benchmarks, several model families, and QA accuracy on long-term memory tasks.
- **arXiv**: https://arxiv.org/abs/2610.13277

### 32. NEAR: Neighborhood-Aware Residuals for Memory Retrieval
- **Authors**: Han Luo, Zhan Zhuang, Xu He, Jujia Zhao, Yu Li, Suqin Yuan, Dong Li, Lei Feng
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.IR
- **Abstract**: Stored records that share topics/entities/events without carrying the required evidence tend to outrank the correct record. NEAR exploits that shared content to build **local references** for query–memory matching, producing residual representations that complement original embeddings.
- **Key innovations**: Each memory derives a reference direction from its neighbors; each query gets a reference from a precomputed table; projection residuals + original embeddings feed a single approximate-NN search over a fixed index. Training-free, consistent improvements on eight long-context retrieval benchmarks across nine embedding models, with downstream QA gains.
- **arXiv**: https://arxiv.org/abs/2610.13314

### 33. PRIME: Pre-Retrieval Index Modeling Enhancement for Structured Document Retrieval
- **Authors**: Cheuk Hei Chung, Li Liu
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.IR; cs.AI
- **Abstract**: High-precision retrieval for agents depends on external KBs, but IR research optimizes the query side (retrievers, generators) and reduces the corpus side to chunking — index-side quality is an underexplored lever. PRIME is an index-side optimization framework with two tracks: LLM-driven **Semantic Restructuring** (SR) of long documents into structured dense sections, and deterministic **Metadata Synthesis** (MS) + **Hierarchical Retrieval** (HR).
- **Key innovations**: Deterministic metadata matches structure-aware chunking quality while cutting embedding computation **45.8×** and index vector count **22.4×**; SR further adds 13.7% Answer-F1 in full deployment. On QASPER/BRIGHT/NFCorpus maps three quality-fidelity-cost regimes (index-side effects are neutralized under a strong reranker).
- **arXiv**: https://arxiv.org/abs/2610.13296

### 34. Locate, Judge, Read: Role-Specialized Tool Agents over a Knowledge-Point Index for Open-Domain Multimodal Document QA
- **Authors**: Wenlin Lin, Fanzhe Wei
- **Institution**: not stated (code org: metask-ai; github.com/metask-ai/knowforge-bench)
- **Subjects**: cs.AI; cs.CL; cs.IR
- **Abstract**: Open-domain QA over heterogeneous document collections needs to find then read passages; current RAG agents give one model both tools and let it self-schedule, which fails on multi-hop and multimodal corpora. KnowForge separates jobs: a hybrid-retrieval **knowledge-point index**, a Locator agent that can only search, a code-scheduled bridge judge forcing the second hop, a typed evidence pool, a Deep Reader (text/images/tables only), and a synthesizer with format checker.
- **Key innovations**: With self-hosted Qwen3.6-35B-A3B, F1 47.5 on full open-domain M3DocVQA (+11.0 over M3DocRAG, +7.1 over one-shot RAR), 53.5 with DeepSeek-V4-Flash; 73.5 accuracy on MultiHop-RAG (best published 71.2); MMLongBench-Doc 34.8 → 47.0 (level with GPT-4o reading page images). Merging the two agents loses 1.9 F1 (it keeps searching instead of reading); latency scales with model calls, not corpus size.
- **arXiv**: https://arxiv.org/abs/2610.13128

### 35. Tracing and Taming Hallucinated Terms via Subsequence-Association Filtering and Breadth-Aware Selection for LLM Query Expansion
- **Authors**: Amit Kumar Jaiswal, Sagar Uprety, Prayag Tiwari
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.IR; cs.CL
- **Abstract**: LLMs are the standard source of query-expansion terms but hallucinate — inserting non-existent entities that add ranking noise and hurt strong retrievers. Existing remedies filter by agreement heuristics without explaining why a term appears or how many to keep.
- **Key innovations**: SAFE-QE (training-free, retriever-agnostic) scores expansion terms by corpus-conditioned cross-context reproducibility, down-weighting terms that reappear under randomized query contexts yet lack pseudo-relevant support; term selection is cast as constrained coverage maximization (consistency–breadth trade-off). Introduces Hallucinated Expansion Term Rate (query-side faithfulness metric). Statistically indistinguishable from generative/corpus-steered expansion on nDCG@10 while injecting 4.3 unsupported terms/query vs 27.8 (Query2doc) and 57.5 (HyDE).
- **arXiv**: https://arxiv.org/abs/2610.13810

## Recommendation / CTR / Advertising

### 36. Beyond Semantic IDs: Finite-Beam Reachability and Continuous-Query Generation in Generative Recommendation
- **Authors**: Yu Sun, Renkai Xiang, Zuodong Xiang, Junwei Zhou, Yike Zhang, Jianxin Zhang, Zhihao Zhu, Xiaoyu Cao, Hailu Xu
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: Generative recommendation retrieves items by autoregressively decoding discrete Semantic IDs (SIDs) with finite-width beam search; this paper analyzes how that interface constrains whether held-out targets enter the returned list, distinguishing catalog-wide scoreability from empirical top-K support, and proposes continuous-query paradigms that drop the SID vocabulary entirely.
- **Key innovations**: CQG-Single (one retrieval query in a single pass) and CQG-AR (autoregressive continuous residual updates) remove the finite-beam reachability constraint and the SID-vocabulary/backbone alignment problem, making every item directly scoreable via dense or approximate-NN retrieval. CQG-Single beats the TIGER-style baseline in all seven runs with 55.3% of the trainable parameters; a depth ablation shows continuous refinement does not monotonically improve shallow accuracy — motivating decoupling output representation, autoregression, and retrieval budget in GR evaluation.
- **arXiv**: https://arxiv.org/abs/2610.12977

### 37. Evolving Creatives with Clicks: CTR-Driven Advertising Image Editing via Attribute Disentanglement and Preference Alignment
- **Authors**: Xu Zhang, Haohan Wang, Zheng Zhang, Yingjie Xia, Wei Feng, Honghe Zhu, Jingjing Lv, Changping Peng, Xuheng Qin, Zehua Zhang, Zheng Luo, Qicheng Li
- **Institution**: not stated (industry author list, unconfirmed)
- **Subjects**: cs.CV; cs.AI
- **Abstract**: E-commerce creative optimization has shifted from aesthetics to online metrics like CTR; current methods generate images from product shots with CTR-based rewards and RL prompt refinement, but equally penalize every attribute of an underperforming image — even ones that help clicks. ECC reformulates creative optimization as **fine-grained editing** rather than generation from scratch.
- **Key innovations**: Identifies 28 CTR-correlated attributes via ANOVA + Random Forest regression; instruction-tunes a prompt model on attribute contrasts between disparate-CTR images, then refines with real click preferences; **Consistent Preference Optimization (CPO)** enforces consistency across semantically-equivalent shuffled suggestions to curb DPO overfitting. Significantly improves ad-image CTR over SOTA. Data and code on acceptance.
- **arXiv**: https://arxiv.org/abs/2610.13066

### 38. FORTE: A Production Framework for Feature Evaluation and Deprecation in Industrial Recommender Systems
- **Authors**: Vishnu Arun, Adam Obeng, Tianyou Wang, Zilin Ren, Mukuntha Narayanan Sundararaman, Han Wang, Shivin Thukral, Zhixiang Wang, Saurabh Vishwas Joshi, Darren Reger
- **Institution**: not stated (industry author list, unconfirmed)
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Production recommenders have feature-lifecycle asymmetry: adding features must improve some metric, removing them must not regress any. Deprecation is hard to prioritize (interactions, daily-changing importance, drift, A/B contention, multi-model consumers). FORTE is a model-agnostic production framework for discovering, validating, and removing features.
- **Key innovations**: Efficient perturbation enables daily feature evaluation; grouped ablation over low-rank feature sets captures interactions; offline results predict online A/B outcomes well enough to deprecate with confidence; lineage tracing covers all downstream consumers. On a search-relevance model, 43.3% of features deprecated via a 48-feature set with no online regressions; on a large ranking model, 8 features removed → 29.9% fewer trainable parameters, 19.8–25.5% serving-throughput gains, hundreds of thousands of dollars in annual training costs saved.
- **arXiv**: https://arxiv.org/abs/2610.13806

### 39. Polarization Dynamics under Algorithmic Recommendations in LLM-based Online Social Networks
- **Authors**: Ali Safarpoor Dehkordi, Mohammad Shirzadi, Mehwish Nasim, Ahad N. Zehmakan
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.SI
- **Abstract**: A controlled comparison of two recommendation mechanisms in LLM-based social simulations: **Edge Recommendation** (ER; new graph connections) vs **Content-Exposure Recommendation** (CR; additional post exposure without graph changes). Users are LLM agents interacting in natural language with evolving opinion states; polarization is measured as opinion dispersion, extremization as distance from the neutral midpoint, and reinforcement as amplification of aligned opinions.
- **Key innovations**: Both recommendation conditions raise mean polarization and extremization vs no-recommendation baselines, with absolute differences up to 0.12 — isolating how the way recommendations are applied changes opinion dynamics independently of platform noise.
- **arXiv**: https://arxiv.org/abs/2610.13351

### 40. Complexity of Autobidding Equilibria in GSP Sponsored Shopping
- **Authors**: Kristoffer Arnsfelt Hansen, Yuhao Li, Xinhao Nie
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.GT; cs.CC
- **Abstract**: Revisits the autobidding equilibria of GSP sponsored-shopping auctions (Dütting et al.). Existence: autobidding equilibria under budget (ABE-B) and ROI (ABE-R) constraints **always exist**, and always admit equilibria with polynomial-size support over the allocation space.
- **Key innovations**: Complexity: exact equilibrium in **FIXP**, approximate equilibrium in **PPAD**, and approximate equilibrium is **PPAD-hard** for both ABE-B and ABE-R — a fairly complete computational-complexity picture for autobidding equilibria in GSP sponsored shopping.
- **arXiv**: https://arxiv.org/abs/2610.13716

## Sequential Modeling / Time Series

### 41. Time Delay System for Sequence Modeling
- **Authors**: Youshan Zhang, Jialu Li
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.CL
- **Abstract**: Sequence models lack an explicit, interpretable content-aware temporal recall mechanism: LSTMs compress everything into one hidden state; Transformers attend to all tokens at quadratic cost; SSMs like Mamba compress history into a fixed state without content-addressable memory. This work grounds sequence modeling in **nonlinear time-delay systems**, where the effective delay is dynamically estimated from semantic similarity between current and historical inputs.
- **Key innovations**: (i) differentiable semantic lag estimator producing content-aware soft attention weights over history; (ii) diagonal state space with closed-form cumulative-sum solution — O(1) per-step, no sequential loops; (iii) interpretable fuzzy semantic modulation learning context-dependent rules balancing instantaneous processing vs historical recall, with rule centers as prototypical contexts. Outperforms SOTA on text classification and generation.
- **arXiv**: https://arxiv.org/abs/2610.12864

### 42. HART: Hybrid Attention-RWKV Time series Foundation Model
- **Authors**: Qingwen Lin, Boyan Xu, Shifeng Xie, Zhifeng Hao, Keli Zhang, Ruichu Cai
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG
- **Abstract**: Non-autoregressive multi-step forecasting (NAF) predicts a full horizon in one forward pass, but RWKV-7 degrades at long horizons: future patches are missing inputs, so the recurrent state must evolve without new observations. Analysis of RWKV-7's generalized delta rule identifies **Placeholder Idling Decay (PID)** — repeated state transitions attenuate historical info when placeholder-driven writes under-compensate (layer-wise analysis confirms reduced state-injection norms).
- **Key innovations**: HART alternates attention and RWKV blocks, combining direct historical-token access with recurrent temporal modeling. At 36M params, improves over pure RWKV at medium/long horizons with comparable short-horizon performance — GIFT-Eval long-horizon MASE 0.752 vs Toto-2.0-1B 0.754, using ~1/28 of its parameters.
- **arXiv**: https://arxiv.org/abs/2610.12883

### 43. How Much Computation Does Every Forecast Need? Structured Block Skipping in Two Time-Series Foundation Models
- **Authors**: Max Bourgeat
- **Institution**: not stated (Amazon-adjacent author, unconfirmed)
- **Subjects**: cs.LG
- **Abstract**: TS foundation models spend the same network depth on every input though forecasting windows differ in structure and difficulty. Tests whether whole Transformer blocks can be removed at inference in Chronos-Bolt and TimesFM 2.5, with masks selected only on calibration windows and evaluated on 1,088 held-out windows.
- **Key innovations**: At moderate sparsity (7/11 and 16/20 blocks), little change in mean relative forecasting quality while median A100 batch-1 latency drops 11.2% and 13.4%; aggressive skipping harms Traffic/Weather. Retrospective oracle beats the best static mask on every dataset, but masks transfer inconsistently across datasets and Chronos representations don't support unseen-domain routing — structured redundancy and input-dependent opportunity, yet not a deployable dynamic-inference method.
- **arXiv**: https://arxiv.org/abs/2610.13208

### 44. On the Encoding of Calendar Features in Covariate-Informed Time Series Foundation Models
- **Authors**: Alexander Kreusel, Maximilian Beichter, Alexandra Nikoltchovska, Benjamin Schäfer, Ralf Mikut, Frederik Zahn, Veit Hagenmeyer
- **Institution**: not stated (KIT/Karlsruhe-adjacent author list, unconfirmed)
- **Subjects**: cs.LG
- **Abstract**: Calendar information is the most common covariate for TS foundation models (available every timestep), yet its encoding is treated as an implementation detail even though it is one of the few design choices left for pretrained models at inference. A systematic comparison of seven encodings — ordinal/one-hot/cyclic (target-agnostic) and four target encodings — across four SOTA TSFMs on nine datasets in zero-shot rolling evaluation.
- **Key innovations**: Encoding choice changes forecast accuracy in every model — MASE differences up to 9.9% (non-holidays) and 83% (holidays) within a single model; gains concentrate around holidays where target history lacks the signal. SHAP attribution localizes covariate contribution vs the autoregressive component and explains degrading combinations. Current covariate-informed benchmarks can distort model comparisons by imposing fixed encoding strategies.
- **arXiv**: https://arxiv.org/abs/2610.13676

### 45. One Thing Leads to Another: The Essentials of Time Series Causal Discovery
- **Authors**: Kurt Butler, Damian Machlanski, Michael P. J. Camilleri, Zhihua Liu, Panagiotis Dimitrakopoulos, Feng Chen, Ricardo Silva, Sotirios A. Tsaftaris
- **Institution**: not stated (IEEE Signal Processing Magazine; UCL/Edinburgh-adjacent author list, unconfirmed)
- **Subjects**: eess.SP; cs.LG; stat.ML
- **Abstract**: A tutorial on time series causal discovery — detecting causation between time series — unifying fragmented work across statistics, dynamical systems, and ML, with roots in signal processing from half a century ago. Covers key principles, limitations, assumptions, evaluation/benchmarking/fine-tuning, and downstream importance in agriculture, Earth science, healthcare, and AI.
- **Key innovations**: New unified overview as a navigation aid across communities plus a companion resource repository (github.com/CHAI-UK/Awesome-Time-Series-Causal-Discovery). 16 pages, accepted for publication in IEEE Signal Processing Magazine.
- **arXiv**: https://arxiv.org/abs/2610.13430

## Games / Multi-Agent / Bandits / Mechanism Design

### 46. OpenSocialJax: Evaluating Social Adaptation in Sequential Social Dilemmas with Open-Ended Environmental Dynamics
- **Authors**: Zihao Guo, Meng Fang, Joel Z. Leibo, Yali Du
- **Institution**: not stated (KCL/DeepMind-adjacent author list, unconfirmed)
- **Subjects**: cs.MA
- **Abstract**: Sequential social dilemma benchmarks rarely test whether agents can infer hidden environmental rules through repeated interaction while adapting to other agents. OpenSocialJax extends Clean Up and Commons Harvest across an open-ended distribution of latent configurations (spatial layouts, hidden rules for tool crafting, payoffs, resource dynamics), sampling from tens of millions of configurations held fixed across five trials.
- **Key innovations**: Evaluates eight LLMs (three closed-, five open-source). Rule discovery often improves performance but doesn't reliably sustain cooperation — cleaning burden concentrates in OpenCleanup and every team exhausts the shared resource in OpenHarvest; in a mixed arena one cooperative agent sustained the public good at its own cost but couldn't prevent depletion. Highlights the difficulty of jointly adapting to unfamiliar dynamics and changing peers.
- **arXiv**: https://arxiv.org/abs/2610.13710

### 47. DIA: A Deep Reinforcement Learning-Based Interest-Aware ABR Scheme for Cloud Gaming
- **Authors**: Zhe Zhang, Haiwei Dong, Marc St-Hilaire, Abdulmotaleb El Saddik
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.MM
- **Abstract**: Cloud gaming needs high-resolution, low-latency transmission over wireless networks. DIA is a DRL-based Interest-Aware Adaptive Bitrate (ABR) scheme that guarantees quality for perceptually key objects in each frame while allocating lower resolutions for non-key objects to conserve bandwidth.
- **Key innovations**: Object-level bitrate via off-the-shelf semantic segmentation; transformer-based feature extractor + interest-aware reward (guided by in-game movement speed, object features, network conditions) without gaze trackers or extra hardware. At least **20% higher normalized average QoE than SOTA ABR** in 5G scenarios, and beats existing ABR schemes in dynamic wireless environments.
- **arXiv**: https://arxiv.org/abs/2610.13698

### 48. Limit-sure Winning in Team Games without Shared Randomness
- **Authors**: Léonard Brice, Thomas A. Henzinger, Alipasha Montaseri, Ali Shafiee, K. S. Thejaswini
- **Institution**: not stated (ISTA-adjacent author list, unconfirmed)
- **Subjects**: cs.GT; cs.FL; cs.MA
- **Abstract**: In concurrent stochastic games where a team plays against an adversarial environment, shared randomness reduces to two-player games but doesn't model real systems. With only individual randomness and reachability/safety objectives, the limit-sure problem asks whether the team can ensure the objective with probability ≥ 1−λ for every λ>0.
- **Key innovations**: Reachability: NP-complete. Safety: limit-sure winning coincides with almost-sure winning, which lies in P. Corollary: model checking the qualitative fragment of Individually Randomised ATL is P^NP-complete.
- **arXiv**: https://arxiv.org/abs/2610.13569

### 49. A 1/2-Approximation for Pandora's Problem with Deadlines
- **Authors**: Shenyu Qin, Chihao Zhang, Yuhao Zhang, Zixuan Zhu
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.GT
- **Abstract**: Pandora's problem models sequential search with per-box opening costs; the deadlines variant gives each box a publicly known deadline for both opening and selection.
- **Key innovations**: A simple threshold strategy achieves a **1/2-approximation** to the optimal expected utility, improving the previous (e−1)/(4e) ≈ 0.158 guarantee (Berger et al., AAAI 2024).
- **arXiv**: https://arxiv.org/abs/2610.13775

### 50. Accelerating Linear Bandits with Persistent Candidate Sets
- **Authors**: Bingkui Tong, Daria Korovaitceva, Marina Sheshukova, Sergey Samsonov, Junpei Komiyama
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG
- **Abstract**: Exhaustive optimistic scoring is costly in linear bandits with a large fixed action set — O(K) score evaluations per round. Persistent Candidate LinUCB (PC-LinUCB) keeps k active actions and samples q challengers uniformly from the remaining K−k, scoring only k+q candidates per round.
- **Key innovations**: Problem-independent and problem-dependent high-probability regret bounds = standard linear-bandit learning term + additive discovery cost O((K−k)log(K−k)/q) at fixed confidence, which **does not grow with horizon**; an Ω((K−k)/q) lower bound under uniform challenger sampling shows partial candidate access is intrinsically costly. Substantially accelerates LinUCB at comparable regret; the mechanism extends beyond LinUCB.
- **arXiv**: https://arxiv.org/abs/2610.13407