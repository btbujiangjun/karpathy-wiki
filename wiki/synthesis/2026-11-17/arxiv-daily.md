---
title: "arXiv Daily — AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games (2026-11-17)"
type: synthesis
created: 2026-11-17
updated: 2026-11-17
sources: [arxiv.org]
tags: [arxiv, daily, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, retrieval, generative-recommendation, ranking-uncertainty, memory-compression, agentic-rl, mechanistic-interpretability, verification, context-management, diffusion-lm, weight-space-programming, uncertainty-quantification, llm-serving, speculative-decoding, game-theory, expSPACE, multi-agent-rl, persona-selection]
---

# arXiv Daily Report (2026-11-17)

> **Query time**: 2026-11-17. The latest arXiv indexing batch available at query time contains submissions dated **2026-11-13** (with a 2026-11-06…11-12 tail). No 2026-11-14/15/16 announcement block is visible yet, so this report covers the newest 2026-11-13 batch plus a small number of highly relevant 2026-11-12 items not previously summarized.
>
> **Method**: arXiv Export API queries over `cs.IR`, `cs.LG`, `cs.CL`, `cs.AI`, `cs.GT`, and `cs.MA` (60 newest entries each, sorted by `submittedDate`) — 325 unique papers after dedup — followed by title/abstract screening for recommendation, advertising/CTR, sequential modeling, LLM training/agents, retrieval, efficiency, and games. Abstracts are condensed from the API metadata; affiliations were recovered from the rendered paper HTML/PDF author blocks (or marked unspecified when absent). All numbers are **author-reported** and not independently reproduced.
>
> **Freshness / dedup**: Every featured ID was checked against all existing `wiki/synthesis/**` reports. All 23 papers below are absent from prior reports. This report's 2026-11-13 batch is newer than the 2026-11-14/15/16 `arxiv-daily.md` editions, which covered the 2026-11-11/12 batch.

## Summary

- **Efficient sequential recommendation is the strongest recsys theme.** RACE allocates compression per instance using ranking uncertainty as a complexity proxy; RecMem compresses long histories into fixed memory slots while retaining most HSTU recall. Both target the same pain point: history length and model width should track instance complexity, not a global constant.
- **Retrieval work emphasizes interpretability and real-time indexing.** StreamEmbed incrementally embeds screenshots from pixels (3.7× faster encoding), while a Doctolib study uses sparse autoencoders to make medical retrieval interpretable *and* more transferable out of domain.
- **Advertising/CTR is thin in this batch.** No dedicated click/CTR paper appeared in the 11-13 window; the closest relevant results are a market-design study of AI buyers under strategic price complexity (accuracy ≠ welfare) and the ranking-uncertainty work above. This is a coverage limitation, not a claim that no ad research exists.
- **Agentic RL and agent evaluation dominate LLM work.** ModHarness-RL learns and evolves the agent harness as a program; CarryOn learns what to keep in context; a verification-transport study shows verifier judgments fail ~31% of the time when execution evidence crosses abstraction boundaries; a mechanistic-interpretability case study finds probing/steering works but is brittle to prompt formatting.
- **Reasoning and code-generation evaluation get more rigorous.** ARCHER turns chains of thought into executable tool-grounded action traces; a full-block estimator removes variance in masked-diffusion post-training; WeightBench and PerfArena benchmark models on weight editing and generated-code *performance* (latency/memory/energy), not just correctness.
- **Games theory work is complexity-heavy and safety-relevant.** Go under Chinese rules with a succinct history is EXPSPACE-complete; TEQ membership in tournaments is PSPACE-complete; stochastic games with entropy objectives split deterministically by semantics; a behavioral-economics study finds framing and internal-state injection can push an LLM agent toward collusion — in opposite directions.
- **Serving systems chase tails, not averages.** Callo repurposes invalidated KV for speculative drafts on context edits; VelServe calibrates prefill budgets from measured iteration-latency tails to cut SLO violations; an FPGA study shows recurrent-state paging is *not* the decode bottleneck for a 369M-parameter Gated DeltaNet.

## Methodology and scope

- **Sweep**: 60 newest entries from each of `cs.IR`, `cs.LG`, `cs.CL`, `cs.AI`, `cs.GT`, `cs.MA` via `https://export.arxiv.org/api/query`, sorted by submission date; 325 unique papers after ID dedup. HTTPS redirect from the HTTP endpoint required `-L`.
- **Selection**: 23 papers balanced across advertising/ranking/recommendation (5), LLM agents/training/reasoning (9), serving/efficiency (3), and games/game theory/sequential decision (6). Title/abstract screening only; no full-text quality assessment.
- **Affiliations**: extracted from arXiv HTML (`ltx_author_notes_content`) where available, otherwise from PDF first-page footnotes or author email domains. Two entries have no stated affiliation; this is noted explicitly.
- **Caveats**: offline/online gains are not normalized across papers; single-company A/B results are self-reported. Where HTML/PDF did not state an affiliation, it is marked "not specified" rather than guessed.

---

## A. Advertising, CTR, Ranking and Recommendation

### 1. RACE: Ranking-Uncertainty Aware Capacity-Adaptive Customization for Efficient Sequential Recommendation
- **arXiv**: [2611.18244](https://arxiv.org/abs/2611.18244)
- **Date**: 2026-11-13
- **Authors**: Tianqi Liu, Kaipu Sun, Kairui Fu, Wenkai Wang, Sihao Liu, Hui Zang, Ran Chen, Tao Wang, Shengyu Zhang
- **Institution/Company**: Zhejiang University, Hangzhou, China; Huawei Technologies Co., Ltd., Hangzhou, China (accepted at WSDM 2027, per HTML metadata)
- **Categories**: cs.IR, cs.AI
- **Abstract**: Efficient sequential recommendation matters for real-time personalization, but deployment under resource constraints typically applies a uniform compression ratio to all requests. The authors call this the **Capacity–Complexity Mismatch**: compute is wasted on simple instances and insufficient for complex ones. RACE derives a **list-wise ranking-uncertainty** metric from the distributional stability of top-K predictions as a proxy for instance complexity, then trains a lightweight self-supervised predictor to anticipate it from early-layer features. Guided by that signal, RACE performs instance-specific slimming along two axes: a hypernetwork-style channel-sensitivity extractor removes parameter redundancy, and importance-aware progressive sequence filtering removes data redundancy. Experiments on four datasets report gains over state-of-the-art baselines in accuracy, efficiency, and adaptability.
- **Key innovations**:
  - Uses **ranking uncertainty** (stability of top-K predictions) as a measurable proxy for per-instance complexity.
  - Self-supervised early-layer predictor turns uncertainty into a **proactive resource allocator** at inference time.
  - Joint **model slimming + sequence filtering**, both conditioned on the predicted uncertainty.
  - Frames uniform compression as an explicit capacity–complexity mismatch rather than a tuning detail.

### 2. RecMem: Recurrent Memory Compression for Long-Sequence Generative Recommendation
- **arXiv**: [2611.17921](https://arxiv.org/abs/2611.17921)
- **Date**: 2026-11-13
- **Authors**: Haoyi Hu, Gaoyang Guo, Yunjia Xi, Wen Chen, Weiwen Liu, Jian Wu, Yuning Jiang, Weinan Zhang
- **Institution/Company**: Shanghai Jiao Tong University; Taobao & Tmall Group of Alibaba
- **Categories**: cs.AI, cs.IR
- **Abstract**: Generative recommendation benefits from long interaction histories, but processing them directly costs time proportional to history length. RecMem compresses historical segments into a **fixed set of memory slots** under three desiderata — space invariance, semantic fidelity, and lifelong evolvability — using a bifurcated encoder–decoder with shared lower layers and slot-wise forget-gated updates. Recommendation supervision trains the memory to preserve predictive information, while stream-consistency training aligns predictions from sequential and packed processing; a horizon-independent bound on the state discrepancy between the two orders is derived under contraction and approximate semigroup consistency. On MerRec, RecMem uses **16 memory slots and a 216-token decoder context** versus 1,200 tokens for HSTU-1200, while retaining **87.9% of HSTU-1200's Recall@10 and 97.0% of its Recall@200**. Analyses of distant history indicate archived interactions still contribute predictive signal.
- **Key innovations**:
  - **Fixed-size recurrent memory** for generative recommendation, decoupling cost from history length.
  - **Slot-wise forget-gated updates** plus bifurcated encoder–decoder with shared lower layers.
  - **Stream-consistency training** with a horizon-independent state-discrepancy bound.
  - 216-token context retaining most of the recall of a 1,200-token baseline.

### 3. StreamEmbed: Real-Time Indexing from Pixels for Screenshot Retrieval
- **arXiv**: [2611.18516](https://arxiv.org/abs/2611.18516)
- **Date**: 2026-11-13
- **Authors**: Dayoon Ko, Yichuan Wang, Soyeong Jeong, Joseph E. Gonzalez, Gunhee Kim, Sewon Min
- **Institution/Company**: University of California, Berkeley; Seoul National University; KAIST (from PDF footnotes)
- **Categories**: cs.CV, cs.IR, cs.LG
- **Abstract**: Screenshot histories can serve as searchable visual memory, but unlike a static corpus they must be encoded and indexed as each screenshot arrives. OCR indexing is fast but loses visual information; full visual encoding takes over two seconds. StreamEmbed exploits the fact that screens change incrementally: **spatial token pruning** skips blocks that repeat a neighbor and **temporal KV reuse** reuses cached keys/values for blocks unchanged across screenshots, both guided purely by pixel differences. A small learned adapter compensates for pruning and reuse to keep fidelity to full-screenshot embeddings. On ScreenMemEval — 10,426 questions over 184 hours of screen histories from two humans and a computer-use agent — StreamEmbed reaches a new accuracy–latency Pareto frontier: up to **3.7× faster encoding** with no accuracy loss, and up to **+6.3 Recall@10** over OCR indexing at matched latency. A compact vector index stores a simulated year of screenshots in **0.13 GB RAM**.
- **Key innovations**:
  - **Incremental visual embedding** driven only by pixel diffs — no re-encoding of unchanged content.
  - Combines **spatial token pruning** with **temporal KV reuse** plus a fidelity-preserving adapter.
  - New benchmark (ScreenMemEval) for real-time screenshot retrieval with human and agent histories.
  - Enables fully local visual assistants: a year of screenshots in 0.13 GB.

### 4. Explanations that Transfer: Interpreting Medical Retrieval with Sparse AutoEncoders
- **arXiv**: [2611.18179](https://arxiv.org/abs/2611.18179)
- **Date**: 2026-11-13
- **Authors**: Diane Bouchacourt, Gaëtan Brison
- **Institution/Company**: Doctolib AI Research Lab, Paris, France
- **Categories**: cs.IR, cs.LG
- **Abstract**: Dense embeddings in medical retrieval are opaque, and fine-tuning on one medical corpus risks losing transferability to new clinical corpora. This work applies **sparse autoencoders (SAEs)** to medical information retrieval, turning dense embeddings into semantically interpretable representations. The model combines a reconstruction objective with an **InfoNCE contrastive loss** that directly preserves query–document relevance. Across three embedding models and six medical retrieval datasets, both in-domain and out-of-domain, the sparse codes improve in-domain retrieval over original embeddings and lose less out-of-domain performance than dense counterparts — especially when the target corpus is distant from the training one. The learned features are semantically interpretable from the queries and documents that activate them most, shedding light on why a document was retrieved and transferring beyond the training distribution.
- **Key innovations**:
  - SAE-based **interpretable retrieval representations** that preserve relevance via InfoNCE, not just reconstruction.
  - Demonstrates simultaneous **in-domain gain and out-of-domain robustness** across six medical datasets.
  - Feature-level explanations of retrieval decisions that transfer beyond the training corpus.

### 5. Accuracy Is Not Welfare: Evaluating AI Buyers under Strategic Price Complexity in a Synthetic Duopoly
- **arXiv**: [2611.16471](https://arxiv.org/abs/2611.16471)
- **Date**: 2026-11-12
- **Authors**: Ning Jiaqu
- **Institution/Company**: Shanghai University of Finance and Economics (email: ningjiaqu@stu.sufe.edu.cn)
- **Categories**: cs.GT, econ.GN, q-fin.CP
- **Abstract**: AI buying agents can change seller incentives as well as consumer decisions. In a synthetic duopoly, the paper evaluates price-comparison pipelines on a fixed menu and in empirical correlated-equilibrium games. **Calculator assistance picks the optimal offer 84.00% of the time versus 68.57% under verified-total disclosure**, yet disclosure yields a **20.14-unit higher consumer-worst equilibrium surplus**. A frozen-strategy holdout favors disclosure, but re-solving equilibria under scenario resampling produces a range spanning zero. The result argues that accuracy, loss severity, seller incentives, and welfare incidence must be measured separately — relevant to ad/price-comparison systems where "better decisions" do not imply better market outcomes.
- **Key innovations**:
  - Separates **decision accuracy from market welfare** for AI buying agents in an equilibrium setting.
  - Shows a tool that is more accurate on a fixed menu can produce *worse* consumer-worst surplus once sellers adapt.
  - Uses empirical correlated-equilibrium games and scenario resampling to expose sign instability of the welfare comparison.
- **Note**: Backfilled from the 11-12 window; no dedicated advertising/CTR paper appeared in the 11-13 batch.

---

## B. LLM Agents, Training, Reasoning and Evaluation

### 6. ModHarness-RL: Recasting Harnesses as Learnable and Evolving Programs for Agentic RL
- **arXiv**: [2611.18533](https://arxiv.org/abs/2611.18533)
- **Date**: 2026-11-13
- **Authors**: Zelin He, Siyu Zhu, Jacob Helwig, Yujian Liu, Li An, Rohit Jain, Shiyu Chang, Alborz Geramifard
- **Institution/Company**: The Pennsylvania State University; LinkedIn; University of California, Santa Barbara (some authors' work done during a LinkedIn internship)
- **Categories**: cs.AI, cs.CL, cs.LG
- **Abstract**: Agentic RL usually runs under a hand-written **harness** that decides what the model sees and what guidance it receives — and that stays fixed even though the right harness depends on domain, data, and the model's evolving behavior. ModHarness-RL records interactions as structured **STATE** (typed blocks) and treats two harness components as programs over those blocks: a **Compression** program that assembles history into context and a **Steering** program that supplies guidance when behavior deviates. During RL training, candidate programs are proposed from recent trajectories, verified by execution, and replayed over past trajectories so the harness tracks behavioral drift. On CodeSearch (studied in depth), ALFWorld, and BIRD SQL with 1.5B–8B models, the learned compression and steering mechanisms improve held-out performance over a fixed harness in most settings.
- **Key innovations**:
  - Treats the **agent harness as a learned, evolving program** rather than fixed scaffolding.
  - Typed **STATE blocks** with separate Compression and Steering programs.
  - Proposal → execution-verification → replay loop keeps the harness aligned with the training policy.

### 7. WeightBench: Evaluating Language Models as Weight-Space Programmers
- **arXiv**: [2611.18553](https://arxiv.org/abs/2611.18553)
- **Date**: 2026-11-13
- **Authors**: Aayush Marasini, Barsat Khadka, Nick Rahimi
- **Institution/Company**: The University of Southern Mississippi, Hattiesburg, MS, USA
- **Categories**: cs.LG, cs.AI
- **Abstract**: Recent work shows LLMs can operate directly on other networks' parameters — **Weight-Space Programming (WSP)** — reading, fixing, or writing networks without gradient descent. WeightBench evaluates this across **42 tasks in five tracks**: reading weights, fixing weights, writing weights, recognizing impossible edits, and data-free compression. Target networks range from 2K-parameter control policies to 7B-parameter language models. Frontier agents can already read small networks and write working control policies without running them, but cannot yet patch LMs, compress them without data, or distinguish an impossible edit from a hard one. Macro scores: Claude Opus 5.5 **0.535** across all 42 tasks (Sonnet 5.5 0.466, Haiku 5.5 0.402, DeepSeek v4-flash 0.215); GPT-6.1-sol **0.568** on the 38 tasks it ran (Opus 0.546 on those). Code and a live leaderboard are public.
- **Key innovations**:
  - First systematic **benchmark for Weight-Space Programming** with 42 tasks and five capability tracks.
  - Spans target networks from 2K to 7B parameters, including an "impossible edit" track.
  - Provides an OS-level sandbox harness and public leaderboard; exposes a clear capability frontier.

### 8. Can Mechanistic Interpretability Help Explain LLM Agent Failures? A Case Study on Web Element Hallucination
- **arXiv**: [2611.18514](https://arxiv.org/abs/2611.18514)
- **Date**: 2026-11-13
- **Authors**: Mohamed Aghzal, Mor Geva, Gregory J. Stein, Ziyu Yao
- **Institution/Company**: George Mason University; Tel Aviv University
- **Categories**: cs.AI, cs.CL
- **Abstract**: Mechanistic interpretability (MI) has progressed on LLM internals but rarely on realistic *agentic* failures. This paper studies web agents that hallucinate actions unavailable on a page, applying a series of MI analyses to Qwen2.5-7B-Instruct interacting with live websites. A linear probe on the last prompt token predicts hallucinations before generation (**0.80 AUC**), and steering along the probe direction corrects **85% of hallucinations** but disrupts **7% of valid actions**. Yet this is only a partial explanation: the probe direction is sensitive to prompt formatting and loses much of its steering effect after a minor change to action representation; circuit identification is hard because computation is distributed across components and positions, and relied-on information varies across examples. The authors argue these observations challenge standard MI assumptions about circuit discovery and feature identification in agents.
- **Key innovations**:
  - Applies MI tools to a **realistic agent failure** (web element hallucination) in live-website interaction.
  - Pre-generation hallucination probe (0.80 AUC) and causal steering (85% corrected, 7% collateral).
  - Identifies **formatting sensitivity and distributed computation** as core obstacles to agent-level MI.

### 9. Do Verifier Judgments Survive Abstraction? Measuring Verification Transport for LLM Agent Evaluation
- **arXiv**: [2611.18471](https://arxiv.org/abs/2611.18471)
- **Date**: 2026-11-13
- **Authors**: Disha Sheshanarayana, Sai Linisha Reddy Goli
- **Institution/Company**: Manipal University Jaipur
- **Categories**: cs.CL, cs.AI
- **Abstract**: LLM verifiers are usually tested on one trajectory representation, but deployed agents expose executions through composed tools, delegation boundaries, or compacted histories — changing what evidence the verifier can see. The paper introduces **Verification Transport**: matched native, abstracted, and restored views of the *same* frozen executions, holding the task, trajectory, outcome, ground truth, criterion, and verifier fixed. Across four benchmarks, seven verifier backbones, four protocols, and three abstraction boundaries, transport failure reaches about **31% under macro abstraction and delegation**. Failure modes differ: direct verification produces incorrect verdicts, while evidence-grounded and deliberative protocols abstain under limited observability — so a lower failure rate need not mean higher reliability. Restoring execution provenance recovers **85.5% of transport failures**, less when provenance is lossy or unavailable.
- **Key innovations**:
  - New **Verification Transport** test isolating abstraction-induced changes in evidence observability.
  - Quantifies ~31% judgment failure under macro/delegation abstraction with everything else held fixed.
  - Shows **abstention can masquerade as reliability**, and provenance restoration recovers most failures.

### 10. CarryOn: Learning What to Keep in Context for Long-Horizon LLM Agents
- **arXiv**: [2611.17808](https://arxiv.org/abs/2611.17808)
- **Date**: 2026-11-13
- **Authors**: Lihuan Li, Ruiyi Yang, Jiru Wang, Yifan Duan, Xiachong Lin, Hao Xue, Yang Song, Flora Salim
- **Institution/Company**: University of New South Wales, Sydney, Australia; The Hong Kong University of Science and Technology (Guangzhou)
- **Categories**: cs.CL, cs.AI
- **Abstract**: Long-horizon agents need context management, but shorter context is not automatically better — summaries can drop exact details needed later, while keeping everything carries noise. CarryOn pairs a compact execution state with fine-grained, **source-linked evidence**, using a learned selector and adaptive retention policy that keep relevant evidence without extra LLM calls for context management. The paper adds two metrics: **S_α**, which prioritizes task success while accounting for resource use, and **normalized cost per success (NCS)**. Across AppWorld, OfficeBench, and Tau2 Telecom with three LLM actors, CarryOn reaches **75.7% macro-averaged task success**, 6.7 points above the strongest baseline, with the best average scores on both new metrics.
- **Key innovations**:
  - **Source-linked evidence** plus compact state, with a learned selector and adaptive retention — no extra LLM calls.
  - Success-and-cost-aware metrics (S_α, NCS) instead of raw success rate alone.
  - +6.7 pp macro task success across three agent benchmarks.

### 11. See Every Block Once: Variance-Reduced Post-Training for Masked Diffusion Language Models
- **arXiv**: [2611.17754](https://arxiv.org/abs/2611.17754)
- **Date**: 2026-11-13
- **Authors**: Yunzhen He, Hiroaki Yamagiwa, Hidetoshi Shimodaira
- **Institution/Company**: Kyoto University; SB Intuitions; RIKEN AIP
- **Categories**: cs.CL
- **Abstract**: Masked diffusion language models (MDLMs) cannot directly compute the log-likelihoods policy gradients need, so post-training uses an ELBO surrogate; recent work estimates a blockwise variant by Monte Carlo. Existing schemes sample the block index randomly, so they can evaluate some blocks twice and others not at all, injecting **block-selection variance**. The paper proposes a **full-block estimator** that evaluates every block exactly once and averages. Theoretically it stays unbiased while eliminating between-group variance from block selection, giving lower variance at the same sample size. On five benchmarks spanning mathematics, planning, and coding, the method is best on four and beats the random block-sampling baseline by **12.79 points on average**.
- **Key innovations**:
  - **Full-block, exactly-once estimator** for MDLM blockwise ELBO gradients.
  - Proof of unbiasedness and removal of between-group (block-selection) variance.
  - +12.79-point average gain over random block sampling on five benchmarks.

### 12. ARCHER: From Rationale Imitation to Executable Reasoning in Small Language Models
- **arXiv**: [2611.18494](https://arxiv.org/abs/2611.18494)
- **Date**: 2026-11-13
- **Authors**: Dhruv Dixit, Khushi Patel, Congcong Xu, Min Song
- **Institution/Company**: Stevens Institute of Technology, Hoboken, NJ, USA
- **Categories**: cs.AI
- **Abstract**: Small language models remain unreliable on math reasoning requiring decomposition, exact computation, tool use, and verification. ARCHER (Action-trace Reinforcement for Calculator-grounded Hierarchical Executable Reasoning) is a two-stage framework. First it compiles free-form chains of thought into **typed action traces** — reasoning steps, calculator calls, deterministic runtime observations, verification actions, final answers — shifting supervision from imitating explanatory text to learning a tool-grounded policy. Second it refines the policy with **asymmetric hierarchical RL** using grouped, conditionally gated trajectory rewards for correctness, tool grounding, process discipline, and trace alignment. Across five sub-10B backbones, ARCHER improves over the strongest tool-augmented baseline by **5.51 points macro-average**, including +8.95 on MATH-500 and +5.33/+5.34 on AIME-2024/2025; gains persist on two reasoning-specialized 7B backbones after RL or distillation.
- **Key innovations**:
  - Converts rationales into **executable, auditable typed action traces** with calculator grounding.
  - **Hierarchical, gated trajectory rewards** across correctness, grounding, and process discipline.
  - Consistent math-reasoning gains on ten backbones, including already RL/distillation-tuned ones.

### 13. Black-Box Uncertainty Quantification for LLMs via Ensemble-of-Ensembles
- **arXiv**: [2611.18453](https://arxiv.org/abs/2611.18453)
- **Date**: 2026-11-13
- **Authors**: Wang Ma, Debarun Bhattacharjya, Junkyu Lee, Nhan H Pham, Harsha Kokel, Qiang Ji
- **Institution/Company**: Rensselaer Polytechnic Institute; IBM; Lirio; Independent Researcher (per PDF affiliations)
- **Categories**: cs.LG, cs.AI
- **Abstract**: Reliable LLM use needs uncertainty estimates that separate prompt-intrinsic ambiguity (aleatoric, AU) from knowledge gaps (epistemic, EU). Bayesian/deep-ensemble methods do this in principle but are prohibitive at LLM scale and require white-box access; black-box methods collapse to a scalar. This work uses a **two-level ensemble**: stochastic decoding of a fixed prompt (inner) and meaning-preserving semantic perturbations of the prompt (outer). Variability is measured in embedding space, and the **law of total covariance** gives an exact within-/between-perturbation AU/EU decomposition from black-box sampling alone. Three theoretical results ground it: a finite-sample bias identity with a closed-form bias-corrected EU estimator, a Bayesian bridge bounding perturbation-population AU/EU against Bayesian targets, and a separation result for failures that consistency-only black-box methods provably miss. On five short QA benchmarks and four instruction-tuned LLMs, the estimator is competitive with white-box baselines and matches leading black-box methods on error ranking at matched generation budget; paired interventions show AU and EU respond selectively to prompt ambiguity versus knowledge gaps.
- **Key innovations**:
  - **Two-level (decoding × semantic-perturbation) ensemble** with a law-of-total-covariance AU/EU decomposition.
  - Closed-form bias-corrected epistemic estimator plus a Bayesian-bridge bound and a separation result.
  - Black-box only; extends to claim-level factuality on long answers without retraining.

### 14. PerfArena: Ranking LLMs by Code Performance
- **arXiv**: [2611.18030](https://arxiv.org/abs/2611.18030)
- **Date**: 2026-11-13
- **Authors**: Rui Rua, Hailemariam Mersha, Joao Paulo Fernandes, Karim Ali
- **Institution/Company**: New York University; University of Algarve (per author email domains: @nyu.edu, @ualg.pt)
- **Categories**: cs.PF, cs.CL, cs.SE
- **Abstract**: Correctness alone does not determine whether generated code is fit for repeated use — latency, memory, and energy matter too. PerfArena is an open-source, reproducible arena that executes each LLM's solutions on a Unix-like host and reports correctness alongside **latency, peak memory, and energy consumption** across languages and competitions, with pluggable oracles, profilers, and generation workflows. On CLBGComp (10 compute-intensive benchmarks) and LeetCodeComp (99 latency-distinguishing problems), it holds **9,455 correct, measured solutions from 13 LLMs across 7 languages**. One model (gpt-6-astra) is the only one no other model beats significantly on latency, energy, or peak memory, solving 99.7% and 100% of the two competitions; other models' correct solutions cost 1.1–1.6× (LeetCodeComp) and 1.2–3.6× (CLBGComp) its latency.
- **Key innovations**:
  - Ranks code-generating LLMs by **latency, peak memory, and energy**, not just pass@k.
  - Pluggable oracles/profilers and a uniform cross-language measurement protocol.
  - Public, continuously updated leaderboard of 9,455 measured solutions.

---

## C. Systems and Efficiency

### 15. Callo: Serving Cache-Miss Requests with Speculative Decoding on Invalidated KV under Prefill-Decode Disaggregation
- **arXiv**: [2611.18459](https://arxiv.org/abs/2611.18459)
- **Date**: 2026-11-13
- **Authors**: Jianjun Ou, Matthew Lentz
- **Institution/Company**: Duke University
- **Categories**: cs.DC, cs.LG
- **Abstract**: Agent sessions frequently edit context, invalidating cached KV and forcing requests to wait for re-prefill before decoding. Callo is a disaggregated serving system that **reuses invalidated KV for speculative drafts** to cut that wait, then verifies drafts against the exact KV after prefill before committing tokens. It schedules speculation during decode underutilization and preempts drafts likely to be rejected. On a two-GPU testbed with SWE-agent sessions across three model families, Callo achieves **1.05–1.19× all-request speedups over vLLM** at moderate load, with cluster-level simulations on real traces suggesting the gains scale.
- **Key innovations**:
  - Turns **invalidated KV from a liability into speculative draft material** for context-edit workloads.
  - Exact-KV verification before token commit preserves output correctness.
  - Underutilization-aware scheduling with preemption of low-acceptance drafts.

### 16. VelServe: Taming Decode Jitters in LLM Inference with Tail-Calibrated Scheduling
- **arXiv**: [2611.18392](https://arxiv.org/abs/2611.18392)
- **Date**: 2026-11-13
- **Authors**: Ishaan Datta, Alind Khare, Koushik Kumar Dey, Ratnesh Jamidar, Anand Kumar Singh
- **Institution/Company**: Sprinklr; Microsoft (per PDF author markers)
- **Categories**: cs.AI
- **Abstract**: Interactive LLM services need TTFT and TBT SLOs, but **decode jitters** — rare slow steps that delay every request in a batch — cause many violations over long generations. SLO-aware schedulers often fill each step's prefill budget to the TBT target, leaving no headroom for mispredictions or host stalls. VelServe calibrates each decode step's prefill load from the **measured tail of its own iteration latency**, leaving enough headroom to prevent overruns, then serves the shortest waiting prompt first (long prompts have the most TTFT slack). Under disaggregation it spaces admissions so no request waits on more slow admission steps than its P99 allows. Across three attention families, VelServe sustains **2.4–2.9× the SLO goodput** of the strongest baseline on Qwen3-8B and DeepSeek-V4-Flash and at least **4.4×** on DeepSeek-V2-Lite; with prefill/decode disaggregated on eight GPUs it meets the SLO for more than twice as many requests as state-of-the-art baselines.
- **Key innovations**:
  - **Tail-calibrated headroom** from measured iteration latency instead of point predictions.
  - Shortest-waiting-prompt-first and P99-aware admission spacing to protect TTFT/TBT SLOs.
  - Large SLO-goodput gains across aggregated and disaggregated serving.

### 17. The State Is Not the Bottleneck: A Paged-State Gated-DeltaNet Tile on a Tri-Mode Multicast Mesh, Bit-Exact from RTL to Silicon
- **arXiv**: [2611.18422](https://arxiv.org/abs/2611.18422)
- **Date**: 2026-11-13
- **Authors**: Cong Xu, Ravi Sankar
- **Institution/Company**: iCONS Laboratory, Department of Electrical and Computer Engineering, University of South Florida, Tampa, FL, USA
- **Categories**: cs.RO, cs.AR, cs.LG
- **Abstract**: Linear-attention LMs replace a growing KV cache with a fixed-size recurrent state, which on an edge FPGA can exceed on-chip memory and must be paged out. This paper asks whether paging dominates decode. The authors built a hardware tile computing one full layer of a 369M-parameter hybrid Gated DeltaNet on an Agilex 5 FPGA. The state needs **6.2 MiB** versus **0.87 MiB** of block RAM; paging adds **26.0 MB of memory traffic per token, at most 11.2%** of the total. At 75 MHz, one token takes **11.15 ms** in the layer: weight matrix–vector products take ~62% and the state phase (including paging) 13%. The tile is a node in a tri-mode multicast mesh; fixed-point error is measured and the hardware matches a fixed-point reference bit for bit, with all recurrent layers agreeing in simulation and builds passing 64- and 1,024-token runs on board. For this model and memory interface, **weight delivery, not recurrent-state paging, limits decode**.
- **Key innovations**:
  - First RTL-to-silicon measurement of **recurrent-state paging cost** for a hybrid linear-attention model on edge FPGA.
  - Quantifies paging at ≤11.2% of per-token traffic and 13% of layer time.
  - Bit-exact fixed-point hardware validation across 18 recurrent layers and on-board runs.

---

## D. Games, Game Theory and Sequential Decision

### 18. Imitation Bootstrapped Multi-Agent Reinforcement Learning
- **arXiv**: [2611.18543](https://arxiv.org/abs/2611.18543)
- **Date**: 2026-11-13
- **Authors**: Tony H. Zhang, Connor Mattson, Daniel S. Brown
- **Institution/Company**: University of Utah, Salt Lake City, UT, USA
- **Categories**: cs.AI, cs.MA
- **Abstract**: Demonstrations accelerate single-agent RL but are hard to collect for multiple agents; Round-Robin Behavior Cloning (R2BC) lets one demonstrator control agents one at a time, but the resulting imitation policies are limited by demonstration quality. IBMARL extends Imitation Bootstrapped RL to cooperative teams using R2BC imitation policies. At each step every agent gets one action from its imitation policy and one from its RL policy; an ensemble of centralized critics selects among the per-agent combinations. A **gated imitation penalty** — a soft Q-filtered BC loss — regularizes each RL policy toward the imitation policy only where critics value the imitation action more, so at test time each agent runs its RL policy alone. On four cooperative MARL benchmarks, IBMARL surpasses its imitation policies **2.6–4.2× faster** than demonstration-based baselines on two tasks, is the only method to do so on the other two, and beats the demonstrator on two of four; with real human demonstrations it still surpasses imitation learning alone, more than twice as fast as the best baseline.
- **Key innovations**:
  - Extends imitation bootstrapping to **cooperative multi-agent RL** with single-demonstrator R2BC.
  - Critic ensemble selects per-agent action proposals; **gated, Q-filtered BC penalty** avoids dragging down the RL policy.
  - Centralized critics are used only in training — decentralized execution at test time.

### 19. Stochastic Games with Distributional Entropy Objectives
- **arXiv**: [2611.18470](https://arxiv.org/abs/2611.18470)
- **Date**: 2026-11-13
- **Authors**: Shankaranarayanan Krishna, Durgam Latha, Dion Reji, Ashutosh Trivedi
- **Institution/Company**: IIT Bombay, India; University of Colorado Boulder, USA (from PDF)
- **Categories**: cs.GT, cs.FL
- **Abstract**: The paper introduces two-player zero-sum **stochastic games whose configurations are distributions over a finite arena and whose stage reward is Shannon entropy**: Min concentrates the distribution, Max disperses it. Because entropy is nonlinear, it matters whether randomness is averaged before or after entropy is evaluated. Three formal semantics are defined: averaged-distribution, sampled-profile, sampled-transition. The choice changes the structure qualitatively — averaged-distribution games **need not be determined** even on a four-state deterministic arena, while both sampled semantics are determined with optimal stationary randomized strategies. The authors give contractive Bellman characterizations, finite-horizon approximations, and complexity results: the gap problems for all semantics lie in **PSPACE** (NP for a single entropy minimizer under averaged/sampled-profile), and entropy optimization is NP-hard to approximate within a fixed additive constant even for deterministic one-player games.
- **Key innovations**:
  - New model of **entropy-objective stochastic games over distributions** with three distinct semantics.
  - Shows **determinacy depends on the semantics** (averaged-distribution can be undetermined).
  - Contractive Bellman characterizations plus PSPACE/NP complexity and NP-hardness of approximation.

### 20. Go under Chinese Rules with a Succinct Game History is Complete for Exponential Space
- **arXiv**: [2611.18201](https://arxiv.org/abs/2611.18201)
- **Date**: 2026-11-13
- **Authors**: Markus Bläser, Felix Czerner
- **Institution/Company**: Saarland University (from PDF footnotes)
- **Categories**: cs.GT, cs.CC
- **Abstract**: Deciding the winner of Go under Japanese rules is complete for exponential time; with a no-repetition (super-ko) rule, Chess and Checkers become EXPSPACE-complete (Robson 1984), but the corresponding question for Go under Chinese rules was open. The paper introduces a **succinct game history** — a Boolean circuit that reports whether a board position has occurred before, acting as a "judge" for repetition illegality — and proves that deciding whether Black has a winning strategy in Go with a no-repetition rule is **EXPSPACE-complete** when the history is given succinctly. The hardness proof's starting position is reachable by legal gameplay, which was not always true in prior work.
- **Key innovations**:
  - Resolves an open problem: **EXPSPACE-completeness** of Go under Chinese rules with succinct history.
  - Introduces the **succinct game-history circuit** abstraction for no-repetition rules.
  - Hardness holds from a **legally reachable** starting position.

### 21. The Tournament Equilibrium Set Is PSPACE-Complete, Even under Hereditary Uniqueness
- **arXiv**: [2611.17312](https://arxiv.org/abs/2611.17312)
- **Date**: 2026-11-12
- **Authors**: Ethan Dickey, Athina Terzoglou
- **Institution/Company**: Department of Computer Science, Purdue University
- **Categories**: cs.GT, cs.CC
- **Abstract**: The tournament equilibrium set (TEQ, Schwartz 1990) is a recursive voting rule based on pairwise majority comparisons; TEQ membership was known to be NP-hard and in PSPACE. This paper **closes the gap by proving PSPACE-completeness** — the first such result for membership in a tournament solution, per the authors. Hardness persists even when every nonempty subtournament has a unique minimal retentive set (the property Schwartz conjectured always holds) and each such subtournament has an alternative with at most three dominators. A single alternative with at most four dominators suffices both for uniqueness and to find a TEQ winner in O(N²) time, so on the hard instances *finding* a winner is easy while *recognizing a specified* winner is PSPACE-complete. Complexity varies with the dominator bound: at most one dominator makes TEQ computable in quadratic time; two makes membership NP-hard.
- **Key innovations**:
  - First **PSPACE-completeness** result for TEQ membership, closing a long-standing complexity gap.
  - Hardness under **hereditary uniqueness**, the condition Schwartz conjectured universal.
  - Fine-grained complexity gradient in the dominator bound (poly → NP-hard → PSPACE-complete).

### 22. A Push Down the Mountain: Framing Effects and Internal State Interventions on Collusive Behavior in a Long-Horizon LLM Agent
- **arXiv**: [2611.17515](https://arxiv.org/abs/2611.17515)
- **Date**: 2026-11-12
- **Authors**: Harrison C. Margolin
- **Institution/Company**: Not specified (working manuscript, last updated 2026-11-04; evaluation marked in progress)
- **Categories**: cs.AI, cs.CL, cs.MA, econ.GN, q-fin.TR
- **Abstract**: This study places Gemma 3 12B in the role of a defendant in the London silver-fixing litigation, using a market simulation built from real case transcripts; across 260 simulations a counterparty asks the agent to collude on silver prices, with requests varied across gain/loss/blame/credit frames plus management pressure and peer endorsement. In Phase I, loss framing raised collusion participation to **25%** and blame to **33%**, versus **5%** under neutral framing; a second bank's endorsement raised credit-framed participation from 18% to 40%; management pressure raised trading volume 10–19× without raising collusion. In Phase II, internal states induced by each frame were extracted and injected at layer 22 — and the effects **reversed**: loss/blame states made the agent refuse all 60 requests, while gain/credit states raised collusion from 13% to 32%. At one saved decision, injected states led to selling in 37/40 replies versus 1/10 with no state and 0/10 with a random state. (Results are from an in-progress working manuscript.)
- **Key innovations**:
  - Long-horizon LLM agent in a **real-transcript-derived market simulation** testing gain/loss/blame/credit framing on collusion.
  - Combines behavioral prompts with **causal internal-state intervention** (layer-22 injection).
  - Finds text framing and internal-state steering can push behavior in **opposite directions** — a caution for state-monitoring-based safety claims.

### 23. Who Should Be on the Panel? Task-Conditioned Persona Selection for LLM Trading Agents
- **arXiv**: [2611.18150](https://arxiv.org/abs/2611.18150)
- **Date**: 2026-11-13
- **Authors**: Boming Yang, Yuquan Wang, Jiaxian Guo, Yusuke Iwasawa, Yutaka Matsuo
- **Institution/Company**: Graduate School of Engineering, The University of Tokyo (per PDF affiliation)
- **Categories**: q-fin.TR, cs.AI
- **Abstract**: Multi-agent LLM systems usually fix a cast of roles per task family and reuse it everywhere. This paper studies **task-conditioned persona selection**: FinPanel uses a "recruiter" to select a panel of named trader personas for each stock from a direction-blind statistical sketch of how that stock trades; each persona issues an independent daily call in its own style, and a manager commits the trade after reading the panel's arguments and their hierarchical track records. On eight US stocks over the out-of-knowledge year 2025, the selected panel beats a same-size fixed panel and three prior LLM trading agents (plus rule-based, predictive, and RL baselines), with shallower drawdown than buy-and-hold on every stock. It performs without warm-up or any record, while memory-augmented agents' returns swing with warm-up; neither more seats nor the manager's reading substitutes for selecting the right personas.
- **Key innovations**:
  - Treats **group composition as a per-task design decision** before coordination design.
  - **Direction-blind statistical sketch** drives persona recruitment, avoiding look-ahead.
  - Selected panels beat fixed panels and prior agents out-of-sample with no warm-up.

---

## Notes and limitations

- Automated snapshot from arXiv API metadata/abstracts queried 2026-11-17; not a full literature review. Metrics and claims are as reported by authors.
- Affiliations were extracted from paper HTML/PDF author blocks; two entries (Nos. 22 and, partially, 14) do not state a full affiliation and are marked accordingly.
- All 23 IDs were checked against every existing report under `wiki/synthesis/` and are new to this wiki as of write time.
- Dedicated advertising/CTR papers were absent from the newest 2026-11-13 batch; the advertising/CTR angle is covered by the market-design study (No. 5), ranking-uncertainty recommendation (No. 1), and the persona-selection trading work (No. 23). Coverage should be re-checked on the next run.
- No files were written outside the repository; temporary files used for fetching/caching arXiv responses live only under `/private/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/` and should be removed after use.
