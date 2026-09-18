---
title: "arXiv AI Research Paper Search Report"
type: synthesis
created: 2026-09-18
updated: 2026-09-18
sources: [arxiv.org]
tags: [arxiv, AI, LLM, recommendation, advertising, CTR, retrieval, RAG, diffusion-LM, RL, GRPO, reasoning, test-time-scaling, inference, KV-cache, speculative-decoding, mechanism-design, game-theory, world-models, agents, multi-agent, OPD, distillation, cross-lingual, curriculum, daily-digest]
---

# arXiv AI Research Paper Search Report — 2026-09-18

Generated: 2026-09-18 (Friday). Fresh window = the **Fri 18 Sep 2026 mailing** (Thu 17 Sep submissions). `/list/{cat}/new` announces *"Showing new listings for Friday, 18 September 2026"*; the batch covers IDs **2609.19149 → 2609.20822** observed live in the fresh listing (all strictly above the Thu-17 siblings' ceiling **2609.19145**, so structurally disjoint from all 09-16/09-17 reports). All featured IDs verified **0 hits in `wiki/`** and **0 hits in the sibling 09-18 arxiv-paper-check / arxiv-daily citation sets** at grep-verification time.

**Methodology**: The public arXiv API (`export.arxiv.org`) remained rate-limited (429 / 301 redirects), so this run used direct page fetches of `/list/{cat}/new` for **cs.AI, cs.LG, cs.IR, cs.CL, cs.GT, cs.MA, cs.NE** (fresh Fri-18 window), plus ~37 targeted `abs/{id}` fetches for the screened shortlist. Probe HTML was cached under the pre-approved temp dir `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/arxiv-search/` and cleaned up after the report landed. Every featured ID below was grep-verified **0 hits in `wiki/`** prior to writing.

**Dedup / cross-reference notice**: The same Fri-18 window (2609.19149–2609.20822) was also mined by the sibling **`arxiv-paper-check`** (rec/CTR/tabular focus, 11 featured + 6 runner-ups) and partially by **`arxiv-daily`** (Thu-17 remainder). Those sets are **not re-featured here**; they are cross-referenced in §5. The AI/LLM/RL/inference/games remainder is featured below. Institutions are author-affiliation inferred where not printed on arXiv (marked *tentative*).

## Summary Statistics

| Scope | Value |
|---|---|
| Window covered | Fri 18 Sep 2026 mailing (Thu 17 Sep submissions); IDs 2609.19149–2609.20822 observed live |
| Categories parsed | cs.AI, cs.LG, cs.IR, cs.CL, cs.GT, cs.MA, cs.NE |
| Featured in full in this report | 28 papers (7 sections) + 8 shortlisted runner-ups |
| Direct advertising / sponsored-search / CTR-ML papers | **0 new** (6th consecutive window ≈0 classic end-to-end CTR/pCVR ML on the daily arXiv; sibling arxiv-paper-check claims the window's only CTR/CVR paper = 2609.19787 KDD Cup 2026 UniRec, 340.82M records, CVR drought-breaker) |
| Dedup | All featured IDs 0 hits in `wiki/` + 0 hits in sibling 09-18 paper-check / daily citation sets |
| Notable fail-note | Institutions not printed on arXiv abs pages; author-affiliation inference is tentative for all non-DeepSeek entries |

**Theme of the window**: the Fri-18 batch is unusually **RL/post-training-heavy** — on-policy distillation length inflation (EOS-token mismatch, OPD retirement), advantage-scale calibration (Score Centering, MaxNorm-AC, EPIG-Tree), observation supervision for RLM agents (ActObs), and compositional reasoning under RL — plus a strong **diffusion-LM** cluster (dQwen3.5 hybrid adaptation, block parallelism for long-context dLLM training, diffusion parallelism separations, probe guidance for continuous dLLMs, Video DeltaNet). Games/world-models & mechanism design remain healthy (GAVEL graph world model for LLM planners; retaliation-aware collusion countermeasures; matroid-intersection prophet lower bound).

---

## 1 LLM Training, Data & Architecture

### 1.1 DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression (2609.19969)
- **Title**: DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression
- **Authors**: DeepSeek-AI (Anyi Xu, B. Li, Bangcai Lin, Bing Xue, et al.)
- **Institution**: **DeepSeek-AI** (stated)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19969
- **Abstract**: Long-horizon agent workloads are increasingly input-heavy; prefill remains expensive and large KV caches strain HBM/SSD capacity and bandwidth. V4.1-Flash is a **multimodal MoE with 552B backbone params, 1M-token context, Causal Encoder-Decoder (CED)** — activates **16B params/token at decode but only 8B during prefill**. KV compression combines **cross-layer KV reuse in Compressed Sparse Attention 2 (CSA2)** with **FP4 KV caching**, cutting the always-in-HBM global KV footprint to **890 bytes/token (~1/4 of V4-Flash)**; a dedicated deployment optimization (**SWA Bounded Replay**) cuts the persistent SSD/host KV footprint to **~1/8 of V4-Flash**. Pretrained on 45T tokens (multimodal), strong across text + multimodal agentic scenarios.
- **Key Innovations**: (1) CED asymmetric prefill/decode activation (8B vs 16B); (2) CSA2 cross-layer reuse + FP4 KV → 4× HBM / 8× SSD KV reduction with *better* performance than the baseline; (3) first-party checkpoints released. This is the window's flagship frontier-AI KV-compression paper (cross-ref: tech-report-digest 09-14 pin on V4.1-Flash 552B MoE / CED / KV details).
- **Venue**: Preprint (cs.CL cross cs.AI).

### 1.2 Why Pretraining Fails to Share Cross-Lingual Knowledge (2609.19291)
- **Title**: Why Pretraining Fails to Share Cross-Lingual Knowledge
- **Authors**: Adam Gaber, Uriel Dolev, Elisabeth Fittschen, Bobby Cheng, Yuval Marton, Leshem Choshen
- **Institution**: MIT-IBM Watson AI Lab & Hebrew University-aligned (author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19291
- **Abstract**: LLMs show surprisingly limited cross-lingual knowledge transfer. This work pretrains 360M- and 7B-parameter models and shows poor cross-lingual knowledge generalization **emerges during pretraining and persists under standard interventions**. Using a controlled bilingual setup — two copies of *the same language* (identical text + token segmentation) mapped to **disjoint token spaces** — they show *disjoint tokens alone* are enough to induce **knowledge compartmentalization**, establishing disjoint token spaces as a fundamental barrier. Mapping languages into a **shared token space by simple word-wise translation** recovers up to **12.6% of native-language learning efficiency — 14× the baseline**.
- **Key Innovations**: (1) controlled same-language two-token-space experiment isolates token-space identity as the cross-lingual transfer bottleneck; (2) simple word-wise-translation shared-token-space intervention as the fix (14× recovery); (3) 7B-scale confirmation. Important for multilingual pretraining / multilingual tokenizer design.
- **Venue**: Preprint (cs.CL).

### 1.3 QVAC Genesis III — Open Synthetic STEM Corpus for Small-Model Pretraining (2609.19513)
- **Title**: QVAC Genesis III: A Large-Scale, High-Quality Open Synthetic STEM Corpus for Efficient Language Model Pre-Training
- **Authors**: Davide Vitabile, N. Ranjan, Akshay Nambiar, Kamal K. Gupta, Amril Nazir
- **Institution**: Not stated (open-source corpus release; author-inferred academic)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19513
- **Abstract**: High-quality pretraining data is the bottleneck for STEM/edge LLMs under tight token budgets. **QVAC Genesis III = 191.43B-token STEM-focused synthetic corpus** over 19 domains and difficulty levels, built via **dual-strategy teacher distillation using a weak edge-scale student as signal**: student failures → corrective explanations; student successes → contrastive option-level reasoning over all choices. A new **LLM-as-a-parser eval protocol** extracts final answers and tracks accuracy + answer validity. From-scratch 1.7B ablations beat Cosmopedia-v2 / Cosmo-1B across ARC, GPQA Diamond, MMLU STEM — **up to +28.57% on ARC-E, +21.35% on ARC-C**, Valid Answer Rate up to 99.45%.
- **Key Innovations**: (1) leverages the *student's own errors* as training signal (corrective + contrastive); (2) open large-scale STEM corpus targeting edge/on-device budgets; (3) validity-aware evaluation protocol.
- **Venue**: Preprint (cs.AI/cs.LG).

### 1.4 ATC — Abstract Token Curriculum (Continuous CoT without supervision) (2609.19717)
- **Title**: Learn Your Own Thoughts: Abstract Token Curriculum
- **Authors**: Khashayar Gatmiry, Avrajit Ghosh, Parsa Mirtaheri, Jason D. Lee, Nika Haghtalab, Emmanuel Abbe, Peter Bartlett
- **Institution**: MIT / EPFL / UC Berkeley / Princeton-aligned (author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19717
- **Abstract**: CoT requires explicit supervision on thinking tokens (task-specific, data-hungry). **ATC** eliminates direct supervision: a **curriculum of easy→hard problem distributions** makes the model develop *internal abstract "thoughts" in the continuous representation space* as an emergent scratchpad. Theory: for parity functions with single-layer softmax attention, ATC makes attention **naturally focus on CoT tokens that provide the "easiest path" to the next token**. Experiments: graph reachability and arithmetic tasks outperform prior continuous-thought training.
- **Key Innovations**: (1) self-supervised, no-manual-scratchpad CoT training via curriculum; (2) theory (parity/attention) + practice (graph reachability, arithmetic); (3) positions continuous internal thought as learnable via instance difficulty rather than token labels.
- **Venue**: Preprint (cs.LG).

### 1.5 dQwen3.5 — Hybrid-Attention Diffusion LMs from AR Adaptation (2609.20751)
- **Title**: dQwen3.5: Hybrid-Attention Diffusion Language Models
- **Authors**: Anton Xue, Litu Rout, Aditya Akella, Adam Klivans, Sujay Sanghavi, Sanjay Shakkottai
- **Institution**: UT Austin-aligned (author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.20751
- **Abstract**: Nearly all AR→DLM (diffusion language model) adaptations start from a full-attention transformer, but modern AR backbones are hybrid (attention + RNN layers). RNNs are structurally causal and nontrivial to bidirectionalize — yet this work shows hybrid backbones can still be efficient dLLM starts: adapting **Qwen3.5 at 0.8B/2B/4B/9B** yields the **dQwen3.5 family**, reaching a given training loss in **~half the tokens** of a full-attention control. dQwen3.5 matches full-attention DLMs in any-order decoding and performs strongly under parallel decoding.
- **Key Innovations**: (1) first systematic hybrid-backbone→DLM adaptation study across scale; (2) ~2× token-efficiency vs full-attention control; (3) evidence that parallel decoding benefits survive hybrid attention. Directly adjacent to §4.4 (Video DeltaNet) and §1.6 (block parallelism) — the dLLM cluster of this window.
- **Venue**: Preprint (cs.CL/cs.LG).

### 1.6 CSBP — Block Parallelism for Long-Context dLLM Training (2609.19242)
- **Title**: Block Parallelism For Efficient Distributed Long-Context Diffusion Language Model Training
- **Authors**: Tarun Suresh, Pranshu Chaturvedi, Hangoo Kang, Parth Shroff, Ishan S. Khare, Hermann Kumbong, Azalia Mirhoseini
- **Institution**: Scaling Intelligence / Stanford / Univ. of Edinburgh-aligned (author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19242
- **Abstract**: Block diffusion LMs (BDLMs) combine AR cross-block dependencies with parallel within-block denoising, but long-context training is bottlenecked by distributed attention communication + activation memory. Because the BDLM objective **separates over target blocks**, **Block Parallelism (BP)** assigns each corrupted-block computation to one rank; **Context-Sharded BP (CSBP)** additionally shards the shared clean sequence, keeping corrupted K/V + gradients local and avoiding replicated clean prefixes. On 16×H200 @256K: **1.18–1.45×** SFT / **1.27–1.33×** AR→BDLM conversion throughput vs best baseline; **1.61×** at 512K; 2.48× (512K) / 7.59× (1M) for DFlash2 speculative decoder training; in matched 12h DiffusionGemma 26B-A4B SFT, CSBP beats the baseline, at every checkpoint, on SWE-bench Verified + Terminal-Bench Lite.
- **Key Innovations**: (1) new distributed-parallelism dimension exploiting the block-separable objective (corrupted blocks assigned to ranks); (2) CSBP removes replicated clean prefixes + keeps corrupted KV/grads local; (3) large speedups with matching/peak-lower HBM at 256K–1M context.
- **Venue**: Preprint (cs.LG).

---

## 2 Post-Training: RL Stabilization, Compositional Reasoning & OPD

### 2.1 Score Centering Stabilizes Off-policy RL (2609.20807)
- **Title**: Score Centering Stabilizes Off-policy Reinforcement Learning
- **Authors**: Martin Marek, Max Ryabinin
- **Institution**: Together AI-aligned (Ryabinin; author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.20807
- **Abstract**: RL of LLMs is notoriously sensitive to **training-inference mismatch (TIM)**. This paper shows TIM instability is primarily caused by **drift** — a persistent bias between training and inference engines accumulating per training step — and derives an **additive "score centering" correction** that cancels drift. From 0.6B to 30B params, score centering alone **matches or beats importance-sampling under quantization**, with the gap growing as mismatch worsens; being additive it **composes with IS** and beats IS-only baselines in staleness experiments.
- **Key Innovations**: (1) identifies the failure mechanism (drift rather than pure variance) for TIM; (2) one-line additive correction — IS-free, cheap, composable; (3) verified 0.6B→30B across mismatch severities. Practical value for production PPO/GRPO rollouts with different engines.
- **Venue**: Preprint (cs.LG).

### 2.2 EOS-Token Mismatch Explains OPD Length Inflation (2609.20511)
- **Title**: When EOS Tokens Disagree: Understanding Length Inflation in On-Policy Distillation
- **Authors**: Yuxiao Yang, Tianrun Yu, Shangzhe Li, Kaixiang Zhao, Xuchao Zhang, Chetan Bansal, Huaxiu Yao, Taylor W. Killian, Weitong Zhang
- **Institution**: Academic-mixed (UNC / UCSB-aligned; author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.20511
- **Abstract**: In on-policy distillation (OPD) students get excessively long responses and exhaust generation budgets. Root cause identified: **termination-token mismatch** between base students and post-trained teachers — across Qwen3/Llama/Gemma the two models can place stopping probability on *different EOS tokens* even with identical declared stopping sets, suppressing the student's preferred termination without transferring the teacher's alternative. Aligning the decoding stopping set alone is insufficient; treating **functionally equivalent EOS tokens as a shared semantic stopping action** substantially mitigates length inflation. Stage-wise analysis across K2-Horizon stages also reveals a distinct late-OPD inflation that persists beyond alignment (so mismatch is *important but not exhaustive*).
- **Key Innovations**: (1) precise mechanism (EOS-token identity, not stopping-set) for OPD length inflation; (2) simple token-semantic-grouping fix; (3) stage-wise OPD dynamics study. Complements the drift study of §2.1 and RetireOPD (runner-up) on OPD failure modes.
- **Venue**: Preprint (cs.LG).

### 2.3 MaxNorm-AC — Advantage-Scale Calibration for GRPO under low-variance rewards (2609.19164)
- **Title**: Advantage Scale Calibration Imbalance in Group-Relative Optimization under Low-Variance Rewards: Diagnosis and Bounded Recovery
- **Authors**: Fei Ding
- **Institution**: Not stated
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19164
- **Abstract**: In verifier-style RLVR, group-relative optimization often treats advantage scale as an implementation detail. This paper separates two low-variance cases — **sub-resolution jitter** (must not become a preference signal) vs **credible small cardinal gaps** (must be learned without distorting KL). A three-way calibration interface shows why **RLOO/Dr.GRPO can make credible small gaps KL-dominated**, while **GRPO's std-dev denominator can amplify tiny gaps without bound**. Result: the **Reward-Resolution Protocol** (filter sub-resolution gaps) + **MaxNorm-AC** (bounded cardinal recovery on credible gaps). Across dense/MoE and math/code reasoning, MaxNorm-AC improves over the strongest robust-scale baseline while truncating the low-variance inverse-scale tail.
- **Key Innovations**: (1) separates jitter vs credible micro-gaps explicitly; (2) unified three-way interface explaining RLOO/Dr.GRPO vs GRPO divergence; (3) bounded-recovery normalization (MaxNorm-AC) with empirical wins. Directly relevant to reward-noise-sensitive RLVR tuning.
- **Venue**: Preprint (cs.CL/cs.LG).

### 2.4 ActObs — Supervise Environment Observations to Prepare for RL (2609.20715)
- **Title**: Don't Mask the Environment: Observation Supervision Changes How Agents Explore Under RL
- **Authors**: Juzheng Zhang, Disha Makhija, Manoj Ghuhan Arivazhagan, Vinayshekhar Bannihatti Kumar, Rashmi Gangadharaiah
- **Institution**: Amazon-aligned (author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.20715
- **Abstract**: SFT applies loss only to agent-authored action tokens; observations are context, not targets. **ActObs** adds supervision on the observation tokens already present in trajectories — no extra data/params/tokens/forward passes. Methods match after SFT but diverge after GRPO: **Qwen3-4B pass@k improves at every sampling budget** on Terminal-Bench 2.0; Qwen3-8B trades some pass@1 for higher pass@k (+3.4pp at pass@16); aids cross-domain code editing (aider-polyglot +4.2pp pass@1 at 4B). ActObs keeps more entropy during RL, needs less policy movement, and stays closer to SFT init. Analysis: action+observation gradients rapidly become orthogonal; action-only training leaves a large residual observation gradient that degrades environment prediction.
- **Key Innovations**: (1) free supervision signal (already in trajectories) that reshapes exploration under RL; (2) orthogonalization explanation for why one-sided action training hurts; (3) cross-domain generalization evidence.
- **Venue**: Preprint (cs.LG/AI/CL).

### 2.5 EPIG-Tree — Compute-Optimal Branching for Policy-Gradient Estimation (2609.20004)
- **Title**: EPIG-Tree: Compute-Optimal Branching for Gradient-Efficient Reinforcement Learning
- **Authors**: Nikita Khomich, Leopold Hermansson, Ido Hakimi
- **Institution**: Not stated
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.20004
- **Abstract**: GRPO collapses a whole trajectory into one scalar reward, exploring/allocating reward inefficiently — every token inherits a trajectory-level advantage. **EPIG-Tree** treats **tree-based rollout construction as a compute-allocation problem**: branches belong where they most reduce *policy-gradient* uncertainty per unit of compute. From a law-of-total-variance decomposition of the local PG random variable come two allocation laws (new branches → decision uncertainty; repeated suffixes → continuation uncertainty) and a **suffix law** nₑ ∝ wₑ‖∇logπ‖σₑ/√cₑ. EPIG reduces gradient MSE in cloned-state control (wins 9/13 continuous-control envs, near-perfect reference direction recovery), improves frozen-LLM gradient calibration, and in online **Wordle reaches 0.850 final win rate vs flat-GRPO 0.790 saturation**.
- **Key Innovations**: (1) formalizes rollout-branch placement as gradient-estimation allocation; (2) decision vs continuation uncertainty laws; (3) word-level credit beats flat GRPO in online single-turn math + multi-turn Wordle.
- **Venue**: Preprint (cs.LG).

### 2.6 Compositional Reasoning in LMs under RL Post-Training (2609.19465)
- **Title**: Compositional Reasoning in Language Models under Reinforcement Learning Post-Training
- **Authors**: Yu He, Yingxi Li, Yifei Wang, Ellen Vitercik
- **Institution**: Stanford-aligned (Vitercik; author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19465
- **Abstract**: Do RL post-training methods improve *compositional* generalization? A **dependency-graph framework** yields three compositionality levels. On data-structure tasks (deterministic rewards, clear compositional structure), a consistent **decomposed-to-composed asymmetry**: decomposed-skill training does *not* reliably transfer to composed tasks, whereas composed-task training transfers *back* to decomposed tasks; provided a theoretical explanation. Extends to length extrapolation, structural shifts, unseen-skill transfer, with a **pilot on real tool-calling benchmarks** showing the asymmetry may persist in the real world.
- **Key Innovations**: (1) formal dependency-graph levels of composition for RL; (2) the asymmetry result (decomposed→composed fails, reverse transfers); (3) theory + tool-calling pilot. Implication: RL curricula pushing decomposed skills may not buy composed-task generalization.
- **Venue**: Preprint (cs.AI/cs.LG).

---

## 3 Reasoning & Test-Time Scaling

### 3.1 Sample Count Is Not Enough — Generation *Schedule* Shapes TTS Performance/energy (2609.19499)
- **Title**: Sample Count Is Not Enough: Candidate-Generation Strategy Shapes the Energy and Performance of LLM Test-Time Scaling
- **Authors**: Mobina Kashaniyan, Ali Jannesari
- **Institution**: Iowa State-aligned (author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19499
- **Abstract**: TTS budgets are often described by candidate count N, but N doesn't say how candidates are *executed*: one batched call (1×8) vs split into 2×4 / 4×2 / 8×1 sequential calls. On Phi-3-mini / Qwen2.5-1.5B (500 GSM8K prompts), N:1→8 lifts accuracy 8.4 / 18.4pp; but for fixed N=8, **8 serial calls use 4.64–4.86× GPU-device energy and 5.77–6.12× P95 latency vs one 8-candidate batched call**. When candidates are independent and memory allows, fewer/larger batches win.
- **Key Innovations**: (1) separates budget (N) from schedule (batches); (2) energy + latency measurements (A100) for the schedule choice; (3) cheap practical rule for multi-candidate TTS deployments.
- **Venue**: Preprint (cs.LG/DC/PF).

### 3.2 SIFT — Fast Tree-Search Self-Improvement for Coding Agents (2609.19526)
- **Title**: Self Improvement via Fast Tree-search
- **Authors**: Xinghong Fu, Aravinth Kulanthaivelu, Yutaro Yamada
- **Institution**: Toyota Research Institute-aligned (author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19526
- **Abstract**: Coding agents that recursively modify themselves exist but are compute-hungry. Bottleneck: evaluating candidate self-modifications by re-running benchmark tasks. **SIFT** augments downstream task evaluations with an **LLM-as-a-judge pairwise signal** aggregated via a **regularized Bradley-Terry model**; strength scores drive rank-based parent sampling inside a lightweight disaggregated tree search, reserving expensive evaluations for the most promising nodes. Outperforms existing tree-search self-evolution frameworks on the full **Polyglot** benchmark at far lower CPU-hours, wall-clock, and API cost.
- **Key Innovations**: (1) judge-signal as a cheap intermediate oracle (Bradley-Terry strength) to steer tree exploration; (2) disaggregated search w/ sparse expensive evaluations; (3) strict-budget wins on Polyglot.
- **Venue**: Preprint (cs.AI/LG).

### 3.3 VRR — LLM-as-an-Improver (Verify → Repair → Reselect) (2609.19515)
- **Title**: LLM-as-an-Improver: Turning Verification into Better Candidates
- **Authors**: Akiyoshi Tomihari, Yuma Ichikawa
- **Institution**: Not stated
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19515
- **Abstract**: Verifier-based selection treats verification as a ranking step and discards its feedback. **VRR** keeps the initial winner while conditionally generating three complementary alternatives — repaired winner, repaired runner-up, and a new-approach solution — filters invalid/duplicate candidates using only inference-time info, then reselects. Improves over fixed-pool verifier selection on code + reasoning benchmarks, and **recovers correct solutions even when the entire initial pool is wrong**.
- **Key Innovations**: (1) verification feedback *improves the candidate pool*, not just ranks it; (2) conditional complementary alternatives (repair + fresh approach); (3) all-inference-time filtering.
- **Venue**: Preprint (cs.AI/LG).

### 3.4 Uni-LaDiR — Latent Diffusion Unifies Multimodal Reasoning (2609.19878)
- **Title**: Uni-LaDiR: Latent Diffusion Unifies Multimodal Reasoning
- **Authors**: Haoqiang Kang, Yizhe Zhang, Nikki Lijing Kuang, Yian Ma, Lianhui Qin
- **Institution**: UCSD / Stanford-aligned (author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19878
- **Abstract**: Multimodal reasoning usually concatenates modality-specific thought tokens in one sequence, forcing the model to bridge representational gaps. **Uni-LaDiR** maps teacher reasoning steps from different modalities into a **shared latent thought space** (unified encoder preserving info for later steps/answers), and uses **diffusion to predict the next block of thought tokens** (since one context supports many valid next steps); encoder+reasoner trained jointly with shared weights. Inference needs no teacher observations. Across **11 VLM benchmarks + 2 VLA suites**: relative gains over the strongest baselines of **+7.3% visual reasoning, +6.1% robot manipulation**.
- **Key Innovations**: (1) modality-agnostic shared latent for multimodal thoughts; (2) diffusion multi-step-prediction of thought blocks; (3) VLM + VLA evidence. Bridges the window's dLLM cluster (§1) with multimodal reasoning.
- **Venue**: Preprint (cs.LG/CL).

---

## 4 Inference Efficiency & Diffusion-LM Serving

### 4.1 SwitchSD — Model-Aware Copy vs Neural Speculative Decoding (2609.20186)
- **Title**: To Copy or Not to Copy: Controlling Speculative Decoding via Intrinsic Model Signals
- **Authors**: Roy Eisenstadt, Ido Cohen, Edo Cohen-Karlik, Lior Wolf, Itamar Zimerman
- **Institution**: Tel Aviv University-aligned (author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.20186
- **Abstract**: Speculative decoding faces a draft-strategy tradeoff: neural drafts (EAGLE3) robust across settings, copy-based methods faster in copy-intensive regimes but prone to **accidental repetitions** (n-gram overlap ≠ structural copy-intent), causing false-positive triggers that degrade throughput. **SwitchSD** trains **lightweight probes on the target model's internal representations** to detect genuine copy-intent (**AUC > 0.99**) and dynamically switch between neural drafting and context-based copying. Llama/Qwen: **throughput gains up to 15% over SOTA baselines like EAGLE3**.
- **Key Innovations**: (1) copy-intent as a *latent control signal* learned from the LLM's own representations; (2) high-precision trigger (>0.99 AUC) eliminating false-positive copy bursts; (3) adaptive hybrid drafting. Adjacent to the wiki's inference/serving cluster.
- **Venue**: Preprint (cs.CL).

### 4.2 D-Quant — Driftable Entropy Coding for the KV Cache (2609.19880)
- **Title**: D-Quant: Driftable Entropy Coding for KV Cache Quantization
- **Authors**: Yi Su, Hong Liu, Guanghua Yu, Jianchen Zhu
- **Institution**: Not stated
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19880
- **Abstract**: Fixed-width KV quantization is limited to 2^b levels (severe loss at low bit width) and wastes bits on tail values. Post-rotation KV values are approximately normal — non-uniform. **Entropy coding** exploits this (short codewords for frequent values), but variable-length output breaks parallel attention kernels that need fixed-stride regular memory. **D-Quant** introduces a **drift mechanism converting entropy-coded per-token representations into fixed-size bitstreams**, restoring regular memory access + parallel dequantization in attention kernels.
- **Key Innovations**: (1) applies entropy coding to KV cache quantization with attention-friendly fixed-size outputs; (2) normal-mixture observation exploited (center vs tails); (3) kernel-compatible deployment framing.
- **Venue**: Preprint (cs.CL). Complements V4.1-Flash (§1.1) on the KV-compression theme.

### 4.3 Video DeltaNet — Video-Native Hybrid Attention for Livestream Video Gen (2609.20744)
- **Title**: Video DeltaNet: A Video-Native Hybrid Attention for Livestream Video Generation
- **Authors**: Haocheng Xi, Yiming Xie, Hexu Zhao, Yiwen Zhang, Michael Liu, Thomas Creavin, Kurt Keutzer, Xiuyu Li, Zhaoyang Lv, Chenfeng Xu, Haiwen Feng
- **Institution**: UC Berkeley-aligned, built on MiniMax H3 (author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.20744
- **Abstract**: Video diffusion models repeatedly process long spatiotemporal token sequences during denoising; attention is the bottleneck. Direct linear-attention application breaks fine-grained video interactions. **Video DeltaNet (VDN)** = local Softmax attention + **bidirectional linear memory** for long-range video context; new **Video Delta Attention (VDA)** updates memory once per frame jointly with its spatial tokens; separate output projections + learnable gates calibrate branches; a **staged teacher-alignment recipe** progressively inserts the new pathway into pretrained models. Instantiated on **MiniMax H3** (hybrid only for video↔video; softmax kept for text/audio). With 8-step distillation + an optimized SGLang stack, **VDN-H3 completes DiT denoising of a 14.3s 768p video in 6.70s on 8×B200 — a 14.5× speedup over the 50-step dense H3 baseline**.
- **Key Innovations**: (1) per-frame bidirectional linear memory adapted for video (VDA); (2) progressive teacher-alignment grafting into pretrained models; (3) 14.5× end-to-end denoising speedup with serving stack; (4) extends the window's hybrid/dLLM theme into multimodal generation.
- **Venue**: Preprint (cs.LG).

### 4.4 Probe Guidance — Free Guidance Signals for Continuous Diffusion LMs (2609.19356)
- **Title**: How to Guide Your Language Flow
- **Authors**: Rohit Dilip, Tianrong Chen, Yuyang Wang, David Van Valen, Joshua Susskind, Miguel Angel Bautista
- **Institution**: Apple / Caltech-aligned (Susskind, Bautista — Apple; Van Valen — Caltech; author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19356
- **Abstract**: **Probe guidance** uses the *frozen internal states of an existing diffusion model* to build a guidance signal — same principle as autoguidance but **no extra forward pass at inference** and a reliable way to keep weak/strong models sharing dynamics. Sets **new SOTA on unconditional generation** for continuous diffusion LMs; on a 1.7B dLLM it consistently improves multiple-choice QA. Probing the traditional autoguidance setup (strong model = weak checkpoint) shows the weak model **must come from a low-entropy region of training** — a mechanistic footnote on autoguidance.
- **Key Innovations**: (1) guidance from the model's own frozen states (parameter-free at inference); (2) SOTA unconditional dLLM generation + MCQ gains; (3) mechanistic insight into autoguidance (low-entropy-checkpoint requirement).
- **Venue**: Preprint (cs.LG/AI). Same line as the dLLM cluster (§1.5/§1.6/§4.3).

### 4.5 Parallelism Separations among Diffusion LMs (2609.20539)
- **Title**: Parallelism, critical windows, and separations among diffusion language models
- **Authors**: Sitan Chen, Liye Wang
- **Institution**: Harvard-aligned (author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.20539
- **Abstract**: A promised strength of dLLMs is parallelism vs autoregressive (1 pass/token). This paper initiates a fine-grained comparison of **masked vs uniform vs Gaussian diffusion** parallelism: (a) uniform + Gaussian can sample in a number of forward passes scaling with the **dual total correlation** of the underlying distribution (can be ≪ context length — previously only known for masked); (b) for certain random empirical measures, **Θ̃(√d) passes are necessary and sufficient for uniform/Gaussian**, yet **Ω̃(d) passes are needed for masked** — the **first provable separation** between the three dLLM paradigms. Contrary to intuition (masked "committing to token values"), the separation comes from **critical windows in masked sampling being asymptotically narrower** than in uniform/Gaussian.
- **Key Innovations**: (1) total-correlation-based parallelism bound extended to uniform/Gaussian diffusion; (2) first masked-vs-uniform-vs-Gaussian *provable* separation; (3) mechanism (asymptotic critical-window width).
- **Venue**: Preprint (cs.LG/DS).

### 4.6 LSTM-UT — Universal Transformers via Recurrent-Depth LSTM Layers (2609.19521)
- **Title**: LSTM-UT: Universal Transformer-style Weight Tying with LSTM Layers
- **Authors**: Aras Kavuncu
- **Institution**: Not stated
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19521
- **Abstract**: Universal Transformers tie weights across depth. **LSTM-UT** combines a recurrent-depth LSTM layer with a width-wise gating mechanism (`ct = ct-1 + sigmoid(x)*tanh(Ux + Wct-1)`), producing a **depth-invariant minimal-equivalent architecture** with significantly fewer parameters. Claims vs traditional transformers: comparable downstream performance with **~1/10 the parameters** and **reduced training compute** (per abstract).
- **Key Innovations**: (1) recurrent-depth LSTM as a universal-transformer-style layer; (2) width-wise gate + recurrent critical path → depth-invariant minimal equivalent; (3) order-of-magnitude parameter reduction. Relevant to the wiki's sequential-modeling / weight-tying line (treat the 1/10-parameter claim as *single-source, unverified*).
- **Venue**: Preprint (cs.CL).

---

## 5 Recommendation, Retrieval & Agent-Context (cross-reference with sibling arxiv-paper-check)

⚠️ **CTR/ads note**: this Fri-18 window contains **no new classic end-to-end CTR/pCVR ML** — 6th consecutive window. The window's only direct CTR/CVR paper is **KDD Cup 2026 UniRec (2609.19787, 340.82M records)** — **featured by the sibling arxiv-paper-check** (dense-feature stack +0.0095 AUC, orthogonalized optimizer +0.0028, all sequence-modeling components ≤0.0005; final test AUC 0.828535; shared-train/val-window warning). Also claimed by paper-check (NOT re-featured): 2609.19928 (CyberAgent bank-scale semantic profiling), 2609.20313 (EviRec), 2609.20175 (FacetCRS), 2609.19831 (UPR), 2609.19482 (Algebraic Retrieval), 2609.19656 (SELF-INDEX), 2609.19244 (agentic web-search census), 2609.20218, 2609.19511, 2609.20474 + runner-ups 2609.20131, 2609.20563, 2609.19832, 2609.20171, 2609.20530, 2609.19209. The new retrieval/agent-context content below is the **unclaimed remainder**.

### 5.1 G³RAG — Zero-Token Geometric Graphs for Multi-Hop RAG (2609.19622)
- **Title**: Beyond Similarity through Zero-Token Geometric Graphs for Multi-Hop RAG
- **Authors**: Zeliang Li, Xiaofen Xing, Kailing Guo, Xiangmin Xu
- **Institution**: SCUT (South China Univ. of Tech)-aligned (author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19622
- **Abstract**: Multi-hop RAG needs evidence that stays relevant yet is novel enough to bridge gaps; dense retrieval concentrates on similar docs, graph methods often require expensive LLM entity extraction. **G³RAG** is a **document-only framework with offline graph construction using no LLM calls or generated tokens**: each edge gets a **geometric gain score cosθ·sinθ** capturing directional consistency and orthogonality; a **density-aware topological penalty** suppresses hub nodes; single-step controlled diffusion expands from filtered query seeds. On MusiQue / 2WikiMultiHopQA / HotpotQA with Nv-embed-v2 and Qwen3-8B-embed: **best average F1 and answer-document hit rate among graph baselines** (up to +4.26 F1, +5.76 on MusiQue), with **zero graph-construction token cost**.
- **Key Innovations**: (1) LLM-free graph construction (zero token cost); (2) geometric gain (cos·sin) as a relevance/novelty balance; (3) density-aware hub suppression + controlled diffusion.
- **Venue**: Preprint (cs.IR).

### 5.2 MSS-Complement — State-Conditioned Minimal Sufficient Evidence for Coding Agents (2609.20050)
- **Title**: The Missing Complement: State-Conditioned Minimal Sufficient Evidence for Coding Agents
- **Authors**: Zhexi Feng, Ruiyi Zhang, Yongbo Yang, Pengtao Xie
- **Institution**: UCSD-aligned (author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.20050
- **Abstract**: A coding agent mid-issue has already read what a ranker ranks highest; relevance is per-passage but **sufficiency belongs to the set** — a ranker can fill its budget with variants of one fact and leave the decision unsupported. Formalizes **state-conditioned minimal sufficient evidence recovery**: given a captured agent state, return a compact evidence combination supplying what the next decision still lacks. On **SERBench** (500 held-out states, 45 repos), three semantic calls (propose jointly sufficient set → search for its gaps → return 4–8 intact units within 6144 tokens) **recover complete sets for 73.0% of states @5 items and 80.6% @8**, vs 61.4%/72.4% for Qwen3-embed+rerank (similarity-only control 66.6% → gain is in the set-level policy). Outperforms a memory agent on AMA-Bench (2.08 pts) with 76.2% smaller answer prompts.
- **Key Innovations**: (1) reframes agentic retrieval as *recovering what a decision lacks* not re-ranking what an issue resembles; (2) set-sufficiency semantics (not single-passage relevance) with a search-for-gaps cycle; (3) state-conditioned minimal evidence benchmark (SERBench).
- **Venue**: Preprint (cs.IR/AI/CL). Complements the coding-agent harness literature (sibling 09-17 Lines: Traverse+Scout, 09-18 2609.20474).

---

## 6 Games, World Models & Agents

### 6.1 GAVEL — Graph World Models for Verified LLM Task Planning (2609.19315)
- **Title**: GAVEL: Graph World Models for Verified and Efficient Long-Horizon LLM Task Planning
- **Authors**: Ruiyang Wang, Hao-Lun Hsu, Swarajh Mehta, Jiwoo Kim, Zhihao Dou, Miroslav Pajic
- **Institution**: Duke University-aligned (Pajic; author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19315
- **Abstract**: LLM long-horizon robot plans often violate embodiment constraints, fail to recover from errors, or reason poorly under partial observability. **GAVEL** wraps the LLM in an **explicit graph world model** (object-relations, action pre-conditions/effects, probabilistic beliefs over unobserved object locations) that predicts action consequences *before execution*, detects violations, and repairs those whose fixes follow directly from the graph; LLM replanning is reserved for errors needing semantic reasoning. On BEHAVIOR-1K (100 single long-horizon tasks + 500 multi-task instructions), Qwen3-8B + GAVEL: **single-task success 41.2%→91.8%, multi-task 19.9%→92.6%**; distributional belief reasoning cuts travel distance ~5.4%.
- **Key Innovations**: (1) graph world model as a *verifiable harness* for long-horizon planning; (2) semantic-reasoning-only LLM escalation (efficiency); (3) belief-distribution subtask reordering under partial observability. Strong games/embodied planning cross-over (world-model line).
- **Venue**: Preprint (cs.RO/cs.AI).

### 6.2 Silence Is Endorsement — Verification-Status Laundering in Agent Pipelines (2609.20211)
- **Title**: Silence Is Endorsement: Verification-Status Laundering in LLM Agent Pipelines
- **Authors**: Yibo Hu
- **Institution**: Not stated
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.20211
- **Abstract**: Safety monitors often judge actions from **summaries or stored handoffs, not the original evidence** — the handoff preserves "the action is authorized" while losing "the claim was never verified": **verification-status laundering**. Removing unverified provenance framing (propositions fixed) raises risky-action approval **5%→60% on Llama-3.1-8B and 9%→98% on Qwen2.5-14B** (similar on hosted models). Ordinary pipelines reproduce it: summarizers weaken status, memory compressors remove it; a full proposer→summarizer→memory→monitor pipeline raises risky approval to **57–81%** across three monitors; pattern repeats on WildGuard / ATBench. Instructing monitors to reject unverified auths isn't a reliable cross-model fix (some remain vulnerable, others over-reject). **Fix: carry authorization provenance as structured state attached to the claim.**
- **Key Innovations**: (1) identifies a new safety failure class (status laundering vs lurking-classicity); (2) quantifies the single-source-of-truth divergence (5%→98% swings); (3) structured-provenance prescription. Pairs with sibling 09-17 agent-safety line (RIR rollback memory, collective-loss-of-control).
- **Venue**: Preprint (cs.CR/cs.MA).

### 6.3 Reflective Recovery — Self-Supervised Learning from Mistakes for Reasoning (2609.19156, runner-up ▸ featured here)
- **Title**: Reflective Recovery: A Self-Supervised Method for Reasoning by Learning from Mistakes
- **Authors**: Bo Liu, Lingpeng Kong (author-inferred from digest; tentative)
- **Institution**: HKU-aligned (author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19156
- **Abstract**: (per digest) Self-supervised reasoning training that learns from the model's own mistakes — a "reflective recovery" objective producing gains across reasoning benchmarks relative to baselines on the same model family. (Abstract details partially truncated in digest; treat specifics in the abs page.)
- **Key Innovations**: (1) mistake-anchored self-supervised objective; (2) reflection as a training signal rather than only inference-time.
- **Venue**: Preprint (cs.CL). *Note: compact entry — full verification via abs page recommended for claims.*
- **arXiv**: https://arxiv.org/abs/2609.19156

### 6.4 FINSKILLOPS — Self-Evolving Multi-Agent System for SEC Filing QA (2609.19680)
- **Title**: FINSKILLOPS: A Self-Evolving Multi-Agent System for SEC Filing QA
- **Authors**: Yanzhang Ma, Zhenghan Tai, Hanwei Wu, Sizhe Guan, Jianliang Lei, Hailin He, ... Xinyu Wang (28 authors)
- **Institution**: Not stated (financial-ops team; author-inferred industry)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19680
- **Abstract**: Financial QA systems usually improve pre-deployment, fixing reliability behavior forever; new SEC-filing questions keep exposing heterogeneous errors (period, entity, evidence, calculation). **FINSKILLOPS** frames post-deployment improvement as **controlled behavioral maintenance**: recurring failures become **scoped skill patches**, each earning deployment via targeted validation, **protected-case regression checks, negative controls, and versioned replacement/retirement**. Across 6 financial QA benchmarks a frozen skill registry wins on verdict-weighted correctness + reference consistency; evolved skills raise correctness 3.70→4.55; in a 12-round operational study only **6 of 33 proposed skills are promoted** while non-correct rate drops 20.0%→12.5%.
- **Key Innovations**: (1) skill admission/regression/retirement lifecycle as reliability machinery; (2) evidence-grounded typed failure diagnoses → scoped, versioned patches; (3) conservative promotion economics (6/33). Strong multi-agent + finance + self-improvement cross-over.
- **Venue**: Preprint (cs.AI/IR/MA/SE).

### 6.5 For Your Eyes Only — Coordination between Isolated LLM Instances (2609.19504)
- **Title**: For Your Eyes Only: Evaluating Coordination Between Isolated Language Model Instances
- **Authors**: Alexander Shirnin, Aleksey Kudelya
- **Institution**: Not stated
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19504
- **Abstract**: Can a model embed a signal in natural language that an independent same-model instance detects, with only shared pretraining + task instructions (no shared memory or coordination-specific training)? A cooperative **signalling game**: a Sender writes free-form descriptions for two words (one hidden target), an isolated Receiver identifies it. Seven models, four families, 300 psycholinguistic word pairs, **Double-Pass Success Rate** controlling output biases: most models fail to maintain coordination once detectable signals are filtered; one frontier model stays near-perfect; models can direct this ability toward **deliberate misdirection**; coordination is **weaker across architectures than within**.
- **Key Innovations**: (1) rigorous isolated-instance coordination protocol (no shared memory); (2) hidden-signal robustness + misdirection direction; (3) cross-architecture consistency finding. Relevant to multi-agent watermarking / model-model communication lines.
- **Venue**: Preprint (cs.CL/AI).

---

## 7 Mechanism Design & Game Theory

### 7.1 Nearly Tight Lower Bound for Matroid Intersection Prophet Inequalities (2609.20696)
- **Title**: A Nearly Tight Lower Bound for Matroid Intersection Prophet Inequalities
- **Authors**: Dimitris Fotakis, Charalampos Platanos, Thanos Tolias
- **Institution**: NTUA Athens-aligned (Fotakis; author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.20696
- **Abstract**: Prophet inequalities under intersections of **q partition matroids** (online irrevocable selection, adversarial order). Proves an **Ω(q/log q) competitive-ratio lower bound**; with the known O(q) upper bounds this **resolves (up to log q) the optimal dependence on q** — open since Correa-Cristi-Fielbaum-Pollner-Weinberg (IPCO 2022) and Saxena-Velusamy-Weinberg (ITCS 2023). Also yields **Ω(d/log d)** for d-single-minded auctions (buyers request fixed bundles of ≤d unit-capacity items), built on the "big-decisions-first" framework of Rubinstein-Singla (STOC 2026).
- **Key Innovations**: (1) 5-year-open lower bound refined to within log; (2) transfer to single-minded auction complexity; (3) new use of big-decisions-first framework.
- **Venue**: Preprint (cs.GT).

### 7.2 CURB — Mitigating Retaliatory Algorithmic Collusion (2609.20548)
- **Title**: Mitigating Retaliatory Algorithmic Collusion in Repeated Games
- **Authors**: Karthik Sivachandran, Rohan Paleja
- **Institution**: Georgia Tech-aligned (Paleja; author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.20548
- **Abstract**: RL agents maximizing own reward can converge to supra-competitive outcomes resembling explicit collusion without communication. Existing mitigations are tied to specific settings (two-sided platforms, auctions). This paper links empirical Q-learning collusion to classical **Simple Penal Codes (SPCs)**: any non-trivial SPC induces a quantifiable **conditional dependence** in policies, detectable via the **total variation distance** between action distributions across cooperation vs defection histories. **CURB** (Collusion Unwinding via Reward shaping and Belief injection) penalizes this TV signal during Q-learning and is *guaranteed to convert any SPC fixed point into a trivial one*, precluding punishment-threat collusive equilibria. Substantially reduces collusion in Bertrand + Cournot repeated games; extends to DQN in Bertrand competition.
- **Key Innovations**: (1) general (setting-agnostic) collusion countermeasure grounded in SPC theory; (2) TV-distance detection signal; (3) guarantee of SPC fixed-point elimination + DQN generalization. Complements the wiki's algorithmic-collusion line (09-17: fictitious play, faithful-yet-collusive).
- **Venue**: Preprint (cs.LG/AI).

### 7.3 Steering Equilibrium Selection in Regularized Self-Play via the Reference Policy (2609.19820)
- **Title**: Steering Equilibrium Selection in Regularized Self-Play via the Reference Policy
- **Authors**: Luis Leal
- **Institution**: Not stated (self-contained reproducible companion notebook; companion papers 2606.28308, 2607.17543)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19820
- **Abstract**: Regularized self-play (deep in DeepNash's Stratego) drives zero-sum policies to a Nash equilibrium by best-responding to a slowly moving entropy-regularized reference ρ. When the Nash set is a polytope of value-equivalent equilibria, the regularizer silently picks (uniform ref → max-entropy member, the **I-projection of ρ onto the Nash set**). This paper uses the reference to choose the equilibrium *on purpose*: **anchoring ρ at a target member + refining** steers self-play to it — mean coordinate error 0.007 at median exploitability 5e-5, TOST-equivalent within ±0.05 across 5 exactly solvable games + a 2-D polytope; selection follows the **reach-weighted I-projection** (slope 0.969). Where it breaks: off-manifold references cost 0.08–0.25 exploitability; stiff/flat families need smaller mirror steps; boundary targets undershoot; curvature predicts boundary saturation (rank corr 0.90).
- **Key Innovations**: (1) reinterprets the RLHF KL anchor as an *equilibrium-selection knob*, not only a stability leash; (2) anchoring+refine steering with precise equivalence bounds; (3) honest failure-mode mapping + full reproducibility (single notebook).
- **Venue**: Preprint (cs.AI/GT/LG).

---

## Key Trends Across This Window

1. **The dLLM (diffusion language model) stack is maturing end-to-end this window**: adaptation from hybrid AR backbones (dQwen3.5, ~2× token-efficiency), distributed long-context training (CSBP, 1.18–7.59× across 256K–1M), inference guidance (probe guidance, SOTA unconditional + MCQ), parallelism theory (first masked-vs-uniform-vs-Gaussian separation), and video-native hybrids (Video DeltaNet 14.5× denoising). Cross-theme consistency: shared latent/parallel semantics also appear in Uni-LaDiR (§3.4).
2. **On-policy distillation is the focused pain point in post-training**: EOS-token mismatch (§2.2), drift in off-policy RL (§2.1), self-retiring OPD (runner-up 2609.20784), reflection/repair loops (§3.3), plus composition asymmetry under RL (§2.6). Gradient-monkey-patching and reward calibration (Score Centering, MaxNorm-AC, EPIG-Tree) dominate.
3. **Agent context engineering is converting to set-statutes**: sufficiency-of-set over per-passage relevance (MSS-Complement), zero-token graph construction (G³RAG), verification-provenance as structured state (Silence Is Endorsement), and self-evolving skill registries with conservative admission (FINSKILLOPS). Matches the sibling arxiv-paper-check harness-economics angle (2609.20474).
4. **CTR/ads on the daily arXiv remains quiet (6th window ≈0)**; CVR content flows through the *conference/competition* channel instead (KDD Cup 2026 UniRec featured by paper-check). Sponsored-search/rec content continues mainly as *physical-layer economics + audits*.
5. **Games/mechanism design**: one strong verified long-horizon planner harness (GAVEL) and two GE theory results (Ω(q/log q) matroid-intersection lower bound; SPC-cancellation collusion countermeasure). Equilibrium-steering via reference anchoring anticipates new RLHF-tunable knobs.

## Runner-Ups (shortlisted but not featured — details on abs pages)
- 2609.19671 **When2Think** — instance-adaptive reasoning-depth control (IDAC); AIME24 Pass@3 +10.0% with −27.9% tokens.
- 2609.20082 **MATCH** — model-aware tool-learning curriculum + hierarchically gated rewards (API-Bank 72.19%, BFCL V3 62.87%).
- 2609.20784 **RetireOPD** — self-retiring on-policy distillation for agentic RL (ZJU-aligned).
- 2609.19156 **Reflective Recovery** — learning-from-mistakes self-supervised reasoning (HKU-aligned; compact entry in §6.3).
- 2609.19657 **PrefixBench-H100** — prefix-reuse / TTFT characterization on H100 (two runtimes).
- 2609.20034 **Astronex-World 1.0** — real-time interactive world-model foundation model.
- 2609.19417 **TrioRAG** — graph-free multimodal RAG via multi-signal late fusion (+ AutoQA automotive benchmark; 1.6–2.3× speedup).
- 2609.19213 **Layer-wise Curriculum LLM Compression** — segment-level teacher→student curriculum; −50% GPU memory/training hours (EMNLP 2026).
- 2609.19530 **Agent-Mediated Résumé Screening** — two-agent screening changes who advances + how reliably (REALM@EMNLP 2026).
- 2609.19589 **Form Over Content in Gradient-Based Data Attribution** — gradient alignment tracks answer *format*, not task (KAIST/Yonsei-aligned).
- 2609.19366 **Fine-grained Harm Signals** — category-orthogonal residual analysis of safety directions (KAIST).