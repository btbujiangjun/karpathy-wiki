---
title: arXiv Daily AI/LLM/RecSys/CTR/Games (2026-10-15)
type: synthesis
created: 2026-10-15
updated: 2026-10-15
sources: [arxiv-export-api, arxiv-html]
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

# arXiv Daily Report (2026-10-15)

Search scope: the arXiv export API has caught up on the recent submission backlog. A single `submittedDate:[20261013 TO 20261015]` sweep across the relevant primary categories (`cs.AI`, `cs.LG`, `cs.CL`, `cs.IR`, `cs.GT`, `cs.MA`, `cs.MM`, `cs.CY`, `cs.NE`, `cs.SI`, `cs.SE`, `cs.CR`, `cs.SD`, `cs.RO`, `stat.ML`, `eess.SP`, `eess.AS`, `q-bio.NC`) returns **1,330 unique records**, split across the **2026-10-13 (754)** and **2026-10-14 (576)** submission blocks. The newest indexed submission is `2026-10-14T17:49Z` (2610.20563); the `[20261015 TO 20261016]` block is still empty at run time. This run is therefore the first `arxiv-daily` to mine the 10-13 / 10-14 blocks — the previous digest (2026-10-13) was still pinned to the 2026-10-09 block.

Dedup: a repo-wide regex extract of every `\d{4}\.\d{4,5}` across `wiki/**` and `raw/**` yields a **9,123-ID baseline**; of the 1,330 harvested records **1,323 are new to the wiki**. The **52 featured papers below are all new-to-wiki** (verified by grep against the live wiki immediately before writing; 0 collisions). Note the run is collision-managed against today's sibling `game-rl-daily` (same-scope filter, so its 2610.17xxx/2610.18xxx game IDs are excluded).

> ℹ️ Affiliation note: the arXiv Atom **metadata** API omits affiliations, so for this run **Institution/company** was recovered from each paper's own **arXiv full-text HTML author block** (`arxiv.org/html/{id}`). Where the block was unavailable the entry is marked `not stated (arXiv metadata omits affiliations)` with an author-list hint flagged `unconfirmed`. Recovered affiliations reflect what the author block literally lists (not disambiguated corporate entities).

> ℹ️ Lane note: the classical **industrial CTR / ad-serving architecture** lane is again effectively empty — the only directly topical advertising work is **AdCoEvo** (§4, advertising delivery) and **CASI** (§1, sponsored-search auction credit assignment with a 10% production A/B test). The broader recommendation lane yields a healthy 9 papers (§4) plus 4 IR/ranking papers (§5). §2 self-distillation / RLVR is the most crowded lane this block, and a visible **KV-cache / serving-efficiency** cluster appears in §3.

## Core AI / LLM / Agents

### 1. Scaling Discovery Requires Forgetting
- **Authors**: Shangyin Tan, Ben Zhou, Lakshya A Agrawal, Jialin Zhang, Yilin Chen, Qiuyang Mang, Donghyun Lee, Dennis Jacob, Koushik Sen, Alex Dimakis, Matei Zaharia
- **Institution**: not stated (UC Berkeley-adjacent author list, unconfirmed)
- **Subjects**: cs.AI; cs.CL
- **Abstract**: Automated research with LLM agents improves through iterative refinement and scored verifiers, but the paper finds that all three scaling strategies — iterate longer, run agents in parallel, or let parallel agents communicate — eventually plateau as each agent becomes **anchored to its own past attempts**, making fewer and smaller edits. The key to scaling further is to **forget**: periodically discard the search state (every agent's session and the candidate history) and restart from the best candidate found so far.
- **Key innovations**: Implements "forgetting" in a communicating agent team and evaluates it on four tasks (heuristic programming, kernel optimization, model training): up to **15%** improvement over parallel agents and up to **39%** over a single agent at equal budget. Argues that for open-ended discovery, *what an agent is allowed to remember matters as much as how much compute it is given*.
- **arXiv**: https://arxiv.org/abs/2610.20563

### 2. The Wealth of Agents: Scaling Agentic AI Across Developers
- **Authors**: Austin W. Hanjie, Carlos E. Jimenez, Zirui Wang, Karthik Narasimhan
- **Institution**: Princeton University; UC Berkeley
- **Subjects**: cs.AI; cs.MA
- **Abstract**: Agentic systems are usually built by a single developer with full control. The paper studies **multi-developer agentic systems (MDAs)**, where developers collaboratively build systems beyond what any one could achieve, and compares them with single-developer systems (SDAs) empirically and theoretically.
- **Key innovations**: On GAIA, a population of specialized developers whose individual agents each stay below **35%** accuracy reaches **70%** when combined in an MDA — **12 points** above the median general-purpose SDA built with several times each specialist's budget. Theoretical models show MDAs incentivize specialization and more efficient use of aggregated resources, making MDAs a "new scaling axis."
- **arXiv**: https://arxiv.org/abs/2610.20518

### 3. LAGO: Language Agents with Reusable Growing Options
- **Authors**: Yuran Wu, Mengkang Hu, Qionglin Qiu, Fanqing Meng, Qiguang Chen, Yuhang Zhou, Qiudan Zhang, Xu Wang
- **Institution**: Shenzhen University; The University of Hong Kong; Hunan University; National University of Singapore
- **Subjects**: cs.AI; cs.MA
- **Abstract**: Long-horizon tasks expose a weakness of monolithic tool-use loops: one agent must decompose, execute, and verify within a single trajectory. **LAGO** treats specialized language agents as **reusable temporally extended options**: a meta-agent retrieves options from a persistent library (or spawns new ones), dispatches sub-tasks, verifies results, and admits successful novel options. The library grows across tasks **without updating model weights**.
- **Key innovations**: Frozen Qwen3.5-35B-A3B in both roles resolves **58.6%** of 500 SWE-bench Verified tasks (single attempt, official Docker evaluator). On a fixed 150-task subset under identical policy/temperature/evaluator, LAGO (60.3%) beats mini-SWE-agent (49.3%) and Terminus 2 (57.3%); ablations show 4/2/6 fewer resolved tasks without decomposition / with shuffled reuse / without the library.
- **arXiv**: https://arxiv.org/abs/2610.19843

### 4. CASI: Credit Assignment via Set Intervention for Agentic Retrieval
- **Authors**: Xinyi Cheng, Tianfu Zhang, Jiwen Li, Xuesen Zhang, Shihao Yu, Pengfei Zhu, Renhuan, Heda Wang
- **Institution**: Xiaohongshu Inc. (plus academic co-authors)
- **Subjects**: cs.AI; cs.IR; cs.LG
- **Abstract**: LLMs increasingly generate multiple retrieval actions jointly while downstream systems give only one reward for the resulting set. Broadcasting the reward is a valid score-function estimator for the expected set objective but does not determine a coalition-dependent **within-set** attribution. **CASI** constructs the missing counterfactual via **snapshot-grounded set intervention**: generate/retrieve once, hold replayable snapshot components fixed, and evaluate alternative subsets under common conditions; **Shapley aggregation** converts marginals into within-set credit.
- **Key innovations**: Shows that for m ≥ 4, singleton/leave-one-out/full-set endpoints do not determine the Shapley allocation. In a five-action **sponsored-search** setting, exhaustive auction replay over 1,200 requests exposes large coalition dependence; across five training runs CASI-trained policies achieve higher held-out auction-replay set value, and a randomized seven-day production A/B test on 10% of traffic yields a **3.51%** lift in the primary advertiser-value metric over control.
- **arXiv**: https://arxiv.org/abs/2610.20293

### 5. The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery
- **Authors**: Robert Tjarko Lange, Luca Grillotti, Yutaro Yamada, Rujikorn Charakorn, David Ha
- **Institution**: Sakana AI
- **Subjects**: cs.AI; cs.CL; cs.LG
- **Abstract**: Fully autonomous research agents suffer from a limited ideation radius and myopic hill-climbing. **The Agentic Scientist** is an end-to-end distributed pipeline for computational research alongside modern coding agents: it decomposes research into task drafting, idea generation, planning, sandboxed experimentation, result aggregation, baseline/ablation construction, post-hoc analysis, and report writing, with a meta-controller managing parallel research agents and enforcing **rubric verification** at each stage.
- **Key innovations**: The same orchestration layer works across heterogeneous domains, execution environments, coding harnesses, and metrics, and supports a spectrum of autonomy (co-scientist → end-to-end). In co-scientist mode a development version produced a single paper **accepted at ALIFE 2026**; ablations show reliable autonomy depends on the cross-agent orchestration layer, not just base-model capability. 88 pages.
- **arXiv**: https://arxiv.org/abs/2610.18933

### 6. Explorer-Zero: Improving Self-Play for Long-Horizon Tasks with Decomposable Verifiable Rewards
- **Authors**: Tianyu Liu, Davide Belli, Bence Major, Arash Behboodi, Tribhuvanesh Orekondy
- **Institution**: ETH Zurich; Qualcomm AI Research
- **Subjects**: cs.AI; cs.LG
- **Abstract**: RL training of LLM agents on long-horizon interactive tasks relies on human-annotated tasks and reliable verification, both expensive. **Explorer-Zero** is a self-play framework that jointly generates tasks and fine-grained verifiable rewards through environment interaction: a learned **proposer** explores the environment, constructs tasks, and records intermediate/final states as verification targets; checkpoints reward partial completion, and alternating proposer–solver training adapts the curriculum.
- **Key innovations**: Theory shows subtask rewards reduce collapse among unsuccessful rollouts completing different numbers of subtasks. Without human-annotated training tasks, Explorer-Zero beats evaluated self-play baselines across ALFWorld, ScienceWorld, and AppWorld; on AppWorld a 30B agent reaches **59.67%** success, approaching **62.65%** for RL on human-annotated tasks, and self-play initialization improves subsequent human-data RL on all three benchmarks.
- **arXiv**: https://arxiv.org/abs/2610.19868

### 7. From Relevance to Validity: Zero-Shot Tool Selection via Functional and Contextual Validation
- **Authors**: Xiaoxuan Dong, Jin Zhang, Zichen Yuan, Yue Zhou, Zihao Rao, Dexu Yu, Tingyong Wu, Wenhao Deng, Junchen Fu, Pengwei Sun, Yang Ran, Bo Lan, Yongxin Ni, Youhua Li
- **Institution**: UESTC; Lanzhou University; City University of Hong Kong; Northwestern Polytechnical University
- **Subjects**: cs.AI
- **Abstract**: LLM agents face tasks from unseen domains, making zero-shot tool selection essential. Existing methods rely on **relevance ranking**, but semantic matching cannot ensure a tool is functionally compatible or remains applicable in a new context. The paper identifies a **transfer-validity gap** — semantically relevant tools may still fail after transfer — and proposes a progressive validation framework complementing semantic relevance with **endpoint-grounded functional compatibility** and **task-conditioned contextual evidence**.
- **Key innovations**: Across cross-domain and cross-dataset transfer it consistently improves capability ranking, with larger gains under functional or contextual ambiguity; ablations confirm the complementary contributions of functional and contextual validation.
- **arXiv**: https://arxiv.org/abs/2610.20388

### 8. Memorizing Who, Knowing How: Benchmarking Personal and Procedural Memory for Persistent Assistants
- **Authors**: Maosheng Qin, Qi Zhang, Mingxuan Xia, Jinglei Chen, Jiexiang Wang, Sheng Guo, Cheng Peng, Haobo Wang
- **Institution**: Zhejiang University
- **Subjects**: cs.AI
- **Abstract**: Persistent personal agents must maintain both **personal memory** (whom they serve) and **procedural memory** (how to act), and in harness-based assistance procedures are **user-conditioned**. **PraxisMemBench** is a harness-based benchmark across daily-life and work trajectories where the two memory types evolve together and later tasks depend on both. Experiments show maintaining the two separately is insufficient: completion drops from 84.6% to 77.9% as interdependence increases, and relation-related failures grow from 59.8% to 72.9% across sessions.
- **Key innovations**: Proposes **PraxisMem**, using privileged joint-state supervision to internalize maintenance of memory content *and* organization (location-aware GRPO + dynamic residual-routed OPSD), reaching **40.78%** overall Session Success Rate vs **20.60%** for Claude Code's native memory.
- **arXiv**: https://arxiv.org/abs/2610.20022

## Reasoning / RL / Post-Training / Test-Time

### 9. Long-Horizon RL Needs Muon
- **Authors**: Kai Ruan, Jinghao Lin, Tao Chen, Ziqi Zhou, Qianshan Wei, Zihe Huang
- **Institution**: Renmin University of China (Gaoling School of AI); Duke University
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Long-horizon agents must coordinate reasoning, tool use, and environment feedback, learning from sparse outcome rewards while updating the policy as rollouts are still collected. The paper examines a **single-rollout asynchronous recipe** combining **Muon**, token-averaged loss, truncated importance sampling, and auxiliary length and tool-error penalties; single-rollout sampling allows asynchronous learning without waiting for multiple trajectories per issue.
- **Key innovations**: Studies optimizer choices and recipe components for repository-level issue resolution across two model families; reports higher training success with the full recipe than with baselines. (7 pages, work in progress.)
- **arXiv**: https://arxiv.org/abs/2610.20256

### 10. C3: Rethinking Process Supervision via Confidence-Guided Credit Correction in Multi-Turn RL
- **Authors**: Ai Jian, Haoran Pan, Eryu Guo, Haojin Yang, Jinghan He, Xiaoyun Zhang, Jiangbo Pei, Peiyu Liu
- **Institution**: Beijing University of Posts and Telecommunications; Peking University; Institute of Automation, Chinese Academy of Sciences
- **Subjects**: cs.AI
- **Abstract**: Outcome-only RL for multi-turn tool agents can produce **misguided reinforcement**: even on successful trajectories, undesirable local behaviors may receive positive token-level advantages. **C³** is a plug-in local credit-correction method: it identifies spans corresponding to undesirable behaviors and selectively corrects positive credit after advantage estimation, with correction strength adaptively controlled by the behavior policy's confidence — leaving the task reward and original credit estimation unchanged.
- **Key innovations**: Improves performance across multiple multi-turn benchmarks under both critic-based and critic-free RL; injecting the same behavioral signals as turn-level or outcome rewards does *not* consistently help, showing local credit correction is an effective form of process supervision. (Gradient-equivalent projection-style correction without an auxiliary critic.)
- **arXiv**: https://arxiv.org/abs/2610.19695

### 11. Function-Space Temporal Self-Distillation for Policy Optimization
- **Authors**: Aryan Das, Arnab Bhattacharya, Vinay Kumar Verma
- **Institution**: Indian Institute of Technology Kanpur
- **Subjects**: cs.LG; cs.AI; cs.CL; stat.ML
- **Abstract**: RLVR improves reasoning but scalar outcomes give coarse trajectory supervision; self-distillation adds dense token-level guidance by comparing an unassisted policy with a feedback-informed self-teacher, but the evolving teacher creates unstable targets. **FSPO** is a single-policy framework combining current privileged adaptation with **function-space temporal consolidation**: it stores sparse historical next-token distributions as fixed temporal targets, providing temporal separation without a persistent teacher model.
- **Key innovations**: Adds privileged disagreement correction (suppress locally overvalued actions), reliability-adaptive grounding, and quality/coverage-aware temporal memory. Achieves the highest average accuracy under a **5-hour** budget (≈+4 pts over the strongest baseline) while reducing peak memory from ~70 GB to **56 GB** on Olmo3-7B-Instruct.
- **arXiv**: https://arxiv.org/abs/2610.19687

### 12. Teach Me After You Learn It: Lookahead Self-Distillation for RLVR
- **Authors**: Zepeng Zhai, Meilin Chen
- **Institution**: Xiaohongshu Inc.
- **Subjects**: cs.LG
- **Abstract**: On-policy self-distillation (OPSD) provides dense token-level supervision by aligning a model with the distribution induced by privileged information, but derives supervision only from the **same** instance, leaving inter-instance supervision unexplored. **LEAD** introduces inter-instance distillation: the teacher first learns from other on-policy rollouts via **virtual RL updates on disjoint subsets**, then cross-group token-level supervision is exchanged between subsets.
- **Key innovations**: Introduces **harmonious modulation**, adaptively modulating the GRPO advantage based on agreement between the OPSD and RLVR signals. Best in-domain average across model scales on scientific reasoning and interactive-agent benchmarks while maintaining out-of-domain generalization comparable to GRPO. (18 pages.)
- **arXiv**: https://arxiv.org/abs/2610.18256

### 13. Does self-distillation improve reasoning?
- **Authors**: Jason Ken Adhinarta, Raina Wu, Ashutosh Sharma, Avinash Balakrishnan, Rameswar Panda, Polina Golland, Yoon Kim, Zhang-Wei Hong
- **Institution**: Massachusetts Institute of Technology
- **Subjects**: cs.LG; cs.AI; cs.CL
- **Abstract**: Self-distillation trains a model to imitate its own predictions conditioned on privileged information, and recent methods report better sample efficiency and generalization than RL. This paper revisits two representative methods — **SDPO** and **OPSD** — across code, science, tool use, and math reasoning, testing whether the gains hold out of distribution and whether they actually stem from privileged distillation.
- **Key innovations**: A largely negative result: reported gains **do not consistently generalize** to unseen problems and are largely explained by **overfitting or transferring existing reasoning behavior** rather than using privileged information; self-distillation gradients show weak alignment with reward-optimizing policy gradients. Across Qwen3 (1.7B–14B) and OLMo-3-7B, effectively leveraging privileged information to improve reasoning remains open. (33 pages.)
- **arXiv**: https://arxiv.org/abs/2610.18613

### 14. Contextual Credit Policy Optimization
- **Authors**: Huiwen Han, Ziyao Zeng, Zihao Zhu, Sisong Bei, Hao Wang, Hongyu Xu, Yan Han, Degui Zhi, Zhiwen Fan
- **Institution**: Stanford University; Texas A&M University; Yale University
- **Subjects**: cs.LG
- **Abstract**: Group-based RL derives step-level credit by comparing observation-matched experiences across trajectories, but identical observations occur in different **contexts** and matched peers are not equally informative; moreover, favorable terminal outcomes can obscure redundant actions within successful trajectories. **CCPO** weights observation-matched peers by **contextual similarity** (frozen LLM representations + accumulated trajectory statistics) and pairs **historical credit** with **future credit** (change in contextual outcome value over a short realized continuation).
- **Key innovations**: Both credits are computed in hindsight from already-collected rollouts, avoiding an auxiliary value critic. Across Qwen2.5-Instruct 1.5B/7B it reaches up to **97.4%** on ALFWorld and **79.4%** on WebShop, beating GRPO by up to 21.6 and 18.5 points; ablations show contextual weighting beats uniform weighting and the two credits are complementary.
- **arXiv**: https://arxiv.org/abs/2610.19103

### 15. DoubtLess: Training-Free Contrastive Decoding for Efficient Reasoning
- **Authors**: Minghao Luo, Liang Chen
- **Institution**: The Chinese University of Hong Kong; EPFL
- **Subjects**: cs.CL; cs.AI; cs.LG
- **Abstract**: Reasoning models spend more tokens than needed; prior shortening methods require per-model training, add fixed steering vectors, or use harmful heuristics (early stopping, banning "wait"). **DoubtLess** is a training-free decoding method where a **smaller reasoning model steers the large one toward brevity**: the small model reads the large model's CoT twice — once prompted brief, once verbose — and the difference between its two logit vectors (scaled) is added to the large model's logits at every step.
- **Key innovations**: On seven competition-math / graduate-science / competitive-programming benchmarks it shortens Qwen3-32B's CoT by **31%** with unchanged accuracy, beating five inference-time baselines; in a self-debugging coding agent it cuts thinking tokens per turn by **20%** at unchanged task performance, and generalizes to two other model families. Analysis shows it reduces repeated checking, with most savings after the correct answer first appears.
- **arXiv**: https://arxiv.org/abs/2610.18862

### 16. DTDD: Divergence-Triggered Dynamic Distillation for Reliable On-Policy Supervision
- **Authors**: Qijia He, Zequn Li, Spencer Luo, Tianle Chen, Pradyumna Narayana, Zixian Ma, Ranjay Krishna, Lan Nie, Sugato Basu
- **Institution**: Google; University of Washington; Boston University
- **Subjects**: cs.LG; cs.AI
- **Abstract**: On-policy distillation (OPD) gives dense token-level supervision but becomes unreliable when student and teacher diverge (large initial gap, or compounding errors in long-horizon reasoning/tool use). **DTDD** uses **segment-level student–teacher divergence** to trigger **teacher takeover**: the student prefix keeps standard OPD supervision, the teacher generates a recovery suffix, and the student learns it by behavior cloning.
- **Key innovations**: Reduces post-warmup peak gradient norm by **8.6×**; from a base initialization reaches **21.3%** held-out math accuracy in **2.6× fewer** optimizer updates (both finish near 22%). Improves best-observed ALFWorld / agentic-code performance by 4.8 / 4.1 points. Segment-averaged triggers beat token-spike triggers; BC beats the tested OPD surrogate for recoveries. (23 experimental arms.)
- **arXiv**: https://arxiv.org/abs/2610.19302

### 17. Where to Start, How to Move: Analyzing Curricula under GRPO for Long-Horizon LLM Agents
- **Authors**: Minchan Kim, Sungho Bae, Youngjin Kim, Hyunwoo Park
- **Institution**: Seoul National University (Graduate School of Data Science)
- **Subjects**: cs.LG; cs.CL
- **Abstract**: GRPO provides no reward-relative signal when all rollouts get identical rewards; in long-horizon tasks rewards arrive only on completion, making all-fail groups common early. **Guide Assisted GRPO** replays a successful reference prefix before the learner continues. This paper studies how **initial positions, handoff units, and movement rules** affect unassisted task completion.
- **Key innovations**: Across three model sizes on BFCL, **starting near completion** is more effective under a fixed turn-level threshold; finer handoffs alone do not consistently help, but outcome-informed tool-call selection beats GRPO on trained and untrained categories; guided starts also improve AppWorld success on both splits. Highlights "where learning starts and how starting positions move" as key curriculum choices.
- **arXiv**: https://arxiv.org/abs/2610.19349

## Efficiency / Inference / Serving / Generation

### 18. LatentRemedy: Efficient Remedy For Non-Prefix KV Cache Reuse in Multi-Agent Systems
- **Authors**: Zhiwei Chen, Zhongtao Rao, Waikit Xiu, Yuxiang Zhang, Shuting Cui, Jian Chen, Tianxiang Zhao
- **Institution**: The Hong Kong University of Science and Technology (Guangzhou); Microsoft
- **Subjects**: cs.CL; cs.AI
- **Abstract**: Non-prefix KV-cache reuse can boost multi-agent serving efficiency (agents share context blocks), but under **conflicting tasks** directly reusing non-prefix KV caches can degrade performance by up to **90%**. Existing remedies (selective recomputation, offset-based calibration) recover only a fraction. The paper argues the issue is not only contaminated KV representations but the agent's **difficulty interpreting reused context under its own instructions**.
- **Key innovations**: **LatentRemedy** maps the target prefix's last hidden state through an MLP into a few **task-conditioned latent tokens** placed after the reused KV block to interact with the shared context, trained via full-prefill distillation. Consistently beats reuse baselines on conflicting tasks while keeping TTFT close to direct reuse as cache size grows. (Code released.)
- **arXiv**: https://arxiv.org/abs/2610.18014

### 19. AlignPred: Error-Controlled KV Cache Compression via Alignment and Predictive Coding
- **Authors**: Xu Yang, Jiapeng Zhang, Zhiwei Zuo, Yuxin Chen, Feiqiang Sun, Chengguang Xu, Feng Jin, Zhuo Tang
- **Institution**: Hunan University; Tencent; Central China Normal University
- **Subjects**: cs.PF; cs.LG
- **Abstract**: Long-running agents retain KV caches for hours or days; compressing persistent caches requires reducing storage while controlling reconstruction error. **AlignPred** is a codec combining **local alignment** with **predictive coding** under a configurable KV reconstruction-error budget: local orthogonal transforms align related heads/layers into a common frame, enabling token-wise and same-token cross-head/layer prediction; residuals are quantized on an error-bounded lattice and entropy-coded, **without learned predictors or encoder-side mode search**.
- **Key innovations**: Across three attention mechanisms it uses less storage than evaluated baselines at comparable reconstruction error and decodes ≥**1.6×** faster than evaluated CPU codecs. Near-native task scores on LongBench-Pro at 128K; its SGLang HiCache integration cuts persistent target-KV storage by **42–72%** vs native HiCache with comparable latency.
- **arXiv**: https://arxiv.org/abs/2610.17970

### 20. JointServe: Serving Multi-Model Agents on Memory-Constrained GPUs
- **Authors**: Daijin Hu
- **Institution**: Beihang University
- **Subjects**: cs.DC; cs.LG
- **Abstract**: Agents are evolving from single-model tool users to **planners orchestrating multiple expert models**, breaking the assumption that the working set of models fits in GPU memory. On memory-constrained GPUs, naive whole-model swapping serializes weight transfer with computation and discards session state at a switch. **JointServe** treats weight shards and KV blocks as **residency objects competing for one unified memory budget**.
- **Key innovations**: Exploits three structural properties of agent workloads (directed calls, gapped execution, dual-state residency): intent-signal **prefetch** during generation, **partial k\* residency** reducing switching to incremental layers, and a preemptive transfer scheduler guaranteeing bandwidth share to live-session KV, plus a carve-out control step. Cuts session completion time **21.7%** over the strongest whole-model-swap baseline and stays usable in a crash regime where all swap baselines fail (46× gap); on SWE-bench/tau-bench/OSWorld traces cuts time up to **49%** and lifts SLO attainment to **76.8–100%**. (18 pages.)
- **arXiv**: https://arxiv.org/abs/2610.19822

### 21. Full-duplex Spoken Language Modeling with Discrete Diffusion
- **Authors**: Chen Chen, Pin-Jui Ku, Ankita Pasad, Ante Jukić, Zhehuai Chen, Boris Ginsburg
- **Institution**: NVIDIA
- **Subjects**: cs.CL
- **Abstract**: **Diffuplex** is a full-duplex spoken language model based on **discrete diffusion** that balances linguistic intelligence and response efficiency. With thinking mode it delivers **13.0 tokens per forward pass**, reaching ~**1,872 tokens/s** and substantially surpassing frontier autoregressive models in decoding speed; without thinking it matches the first-audio latency of existing full-duplex models with markedly stronger linguistic intelligence.
- **Key innovations**: Separates **when to say** from **what to say** at the training level rather than compressing both into one autoregressive timeline: at inference it tracks user speech through an **AR interaction policy** while independently generating/refining response content via **parallel diffusion**, so semantic computation is no longer bounded by the perception audio frame rate. Training code and checkpoints to be released.
- **arXiv**: https://arxiv.org/abs/2610.17780

### 22. Delta Tokenizer: Reference-Identical Tokenization of Session Deltas and Segment-Parallelism for Long Prompts on Multicore CPUs
- **Authors**: Zhenyu Zhang, Zhichao Cao
- **Institution**: Arizona State University
- **Subjects**: cs.CL; cs.DC; cs.PF
- **Abstract**: An agent resends the conversation every turn and inference engines reuse the shared-prefix KV cache — but **tokenization has no such shortcut**: the CPU front end converts every request back to token IDs from its first character, inflating TTFT. **Delta Tokenizer** tokenizes only the **delta** between a request and the previous request of the same session, retaining the earlier token sequence, re-encoding only the appended text and the short tail the append could affect, and joining only at a split boundary the tokenizer's rules cannot move, keeping the result **exact**.
- **Key innovations**: For long stateless requests it cuts text at tokenizer-independent boundaries and encodes chunks on several cores in parallel, concatenating to the exact reference encoding, with a shared CPU pool scheduling chunks and short incremental updates. The incremental path shortens a session turn ~**40×** vs the HF reference tokenizer; on 16 cores the chunk-parallel path encodes a 4M-character request **8.2×** faster than serial and 1.6–2.1× faster than LoPT. In SGLang it reduces median chat TTFT by **59%** at 100K tokens and P99 agent-session TTFT by up to **23×**. (42 pages; code in `toktier`.)
- **arXiv**: https://arxiv.org/abs/2610.19801

## Recommendation / Advertising / CTR / User Modeling

### 23. AdCoEvo: A Co-Evolving Multi-Agent Advertising Delivery System
- **Authors**: Tianzhu Hu, Hang Yu, Zeyuan Zhao, Zeyu Pan, Huan Luo, Chun Gan, Mingzhe Cao, Liubin Wang, Mingming Li, Jiao Dai, Jizhong Han, Songlin Hu
- **Institution**: not stated (Chinese Academy of Sciences–adjacent author list, unconfirmed)
- **Subjects**: cs.AI; cs.IR; cs.MA
- **Abstract**: Advertising delivery is the core link between marketing objectives and returns. Existing methods automate individual tasks (bidding, budget allocation) but rely on humans for overall coordination and cannot adapt quickly to market change. **AdCoEvo** is a **co-evolving multi-agent advertising delivery system**: role specialization connects delivery decisions across timescales/granularities; diagnostic results guide account planning and strategy adjustment for the next period; the system updates model parameters from real delivery outcomes and improves via mutual feedback among planning/adjustment/diagnosis.
- **Key innovations**: vs a rule-based operational baseline, increases **advertiser value by 14.02%** and reduces **CPA by 7.07%**; vs a fixed-parameter multi-agent system, +3.96% advertiser value and −1.24% CPA — evidence that co-evolution yields greater delivery returns.
- **arXiv**: https://arxiv.org/abs/2610.19454

### 24. Bridging the Topological Divide: Dual-Branch Graph Distillation with Semantic Priors for Robust Cold-Start Recommendation
- **Authors**: Yuanfeng Qiu
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.IR; cs.LG
- **Abstract**: Graph Collaborative Filtering suffers **catastrophic representation collapse** in strict cold-start scenarios due to topological isolation of unobserved items; directly mapping isolated semantic attributes into a topology-driven collaborative space precipitates degradation and optimization conflicts. **DualGCN** is a **dual-branch graph knowledge-distillation** framework under a decoupled two-stage paradigm.
- **Key innovations**: A collaborative **teacher** anchors item representations with a topology-smoothed semantic prior (reshaping the latent manifold); a semantic **student** branch uses residual mapping and a magnitude-agnostic cosine distillation objective for high-fidelity cross-modal alignment without disrupting collaborative signals; a dynamic norm reconstruction mechanism calibrates scales of novel and warm items during global retrieval. Outperforms SOTA baselines in strict cold-start while preserving accuracy for active items across three datasets.
- **arXiv**: https://arxiv.org/abs/2610.19578

### 25. xLightGCN: Explainable Graph Neural Network Based Recommendation Systems with Most Influential Peers
- **Authors**: Calder Johnson, Robin Cohen
- **Institution**: not stated (University of Waterloo–adjacent author list, unconfirmed)
- **Subjects**: cs.AI
- **Abstract**: Recommendation systems are ubiquitous yet many modern approaches are opaque black boxes, making them hard to audit and assess. In the risk-sensitive sociotechnical context of user-facing AI, the paper argues **explainability is a key pillar** for trustworthiness. **xLightGCN** is an exact, graph-based approach for generating explanations for recommendations built on **LightGCN-like** architectures.
- **Key innovations**: Provides **interpretable explanations** with a **theoretically guaranteed measure of explanation fidelity** (exact graph-based attribution via "most influential peers"), positioned as an assurance mechanism for recommender systems; discusses limitations and future directions.
- **arXiv**: https://arxiv.org/abs/2610.19446

### 26. AdaFrame: Hierarchical Multimodal Deduplication with Adaptive Information Budgeting for Cost-Efficient Video Advertisement Analysis
- **Authors**: Abdul Basit Tonmoy, Arman Luthra, Guang Lin, Qixin Deng
- **Institution**: Wabash College (Crawfordsville, Indiana, USA)
- **Subjects**: cs.MM
- **Abstract**: Uniform frame sampling for VLM-based video analysis floods backbones with redundant content, while keyframe selection is often optimized for human viewing rather than extraction accuracy. **AdaFrame** is a content-adaptive preprocessing cascade with three progressively finer filters — **perceptual hashing, LPIPS, and CLIP-based semantic clustering** — to eliminate redundant frames before costly cross-modal inference. Per-video budgets come from **Intrinsic Semantic Dimensionality (ISD)**, estimated via SVD of frame embeddings.
- **Key innovations**: On 500 **video advertisements** from the Pitt Ads Dataset, reduces frame count by **48%** and VLM inference cost by **75%** vs uniform sampling, while *improving* topic accuracy to **86.0%** (+1.6 pts) and sentiment accuracy to **79.4%** (+7.5 pts).
- **arXiv**: https://arxiv.org/abs/2610.19127

### 27. Prompt or Policy? Optimizing Physician Slate Presentations with LLM User Simulators
- **Authors**: Andrei Niculae, Adrian Cosma, Emilian Radoi
- **Institution**: National University of Science and Technology POLITEHNICA Bucharest; IDSIA (Dalle Molle Institute for Artificial Intelligence, Lugano)
- **Subjects**: cs.CL
- **Abstract**: Choosing a physician is hard; recommendation systems identify relevant doctors but patients struggle to compare profiles. The paper formulates **slate presentation optimization**: given a patient's case and a fixed ranked list of physicians, generate short case-specific summaries that make doctors comparable while staying grounded in their profiles. It optimizes presentations **without real patient interactions** using **persona-conditioned LLM patient simulators**.
- **Key innovations**: Compares prompt-level optimization (**GEPA**), parameter-level optimization (**GRPO**), and their combination across two model sizes. GRPO substantially outperforms GEPA on the full constraint set and its simulated-conversion gains persist under a held-out unseen **LLM judge**; GEPA alone brings smaller gains, but initializing GRPO with its optimized prompt speeds training and achieves the highest simulated conversion.
- **arXiv**: https://arxiv.org/abs/2610.18309

### 28. Mitigating Popularity Bias in Sequential Recommendations with Sparse Prior-Regularized Objective
- **Authors**: Anton Pembek, Anton Klenitskiy, Alexander Savchenko, Alexey Vasilev
- **Institution**: Sber AI Lab; Lomonosov Moscow State University
- **Subjects**: cs.IR
- **Abstract**: Popularity bias causes over-exposure of popular items and reduced catalog coverage. The paper proposes **PR-entmax**, a **sparse prior-regularized objective** making popularity correction context-dependent. Derived from a generalized variational principle where an item-popularity prior is incorporated into a sparse probability mapping, it yields a **popularity-aware active support**: the set of items with non-zero probabilities (and hence non-zero gradients) is jointly determined by contextual relevance and item popularity.
- **Key innovations**: The prior affects not only item probabilities but **which items participate in gradient updates** during training; requires no architectural changes (loss-only modification). At inference the prior is removed and items are ranked by learned contextual relevance alone. Across multiple benchmarks and sequential architectures it consistently reduces popularity bias while preserving/improving relevance.
- **arXiv**: https://arxiv.org/abs/2610.17823

### 29. Many Right Answers, One Training Example: Removing Responder Noise from GRPO for LLM Recommenders
- **Authors**: Xin Li, Hao Jiang, Jinghao Guo, Weisi Lin, Chau Yuen
- **Institution**: Nanyang Technological University, Singapore
- **Subjects**: cs.CL
- **Abstract**: A recommendation request on Reddit draws several replies, each naming different titles — so which replies should a generated list be rewarded against? The SOTA recipe **Rank-GRPO** picks one reply per example, so the advantage mostly records **which reply was drawn** (~85% of its variance) rather than how good the list is. **ReMaRk** scores every list once against the **union** of all replies' titles and samples each request equally.
- **Key innovations**: Makes RL cheaper: on seven backbones and three datasets it reaches the validation recall of 2,000 per-reply RL steps in **25–53%** of the steps and leads at that budget; trained to convergence it is never significantly behind Rank-GRPO and in four of seven pairs reaches Rank-GRPO's best with fewer GPU-hours. The same joint reward helps on ProtoQA (≈100 answers/question) — a simple rule: **reward multiple valid human answers jointly**.
- **arXiv**: https://arxiv.org/abs/2610.17771

### 30. SMI: Ontology-Grounded Semantic IDs for Hierarchy-Aware Medical Concept Representation
- **Authors**: Ziyang Song, Lia Shen, Yixuan Li, Qincheng Lu, Weihao Li, Haoran Xu, He Zhu, Xinyu Wang, Yue Li
- **Institution**: Ohio University (plus co-authors)
- **Subjects**: cs.CL; cs.AI
- **Abstract**: Biomedical LMs give strong clinical-task representations but fail to capture the **hierarchical structure** among medical concepts, especially for rare/fine-grained codes in long-tailed vocabularies. **SMI** (Semantic Medical Identifier) is a **training-free** framework constructing **ontology-grounded Semantic IDs**: each diagnosis/procedure/medication concept gets a coarse-to-fine path through an expert medical ontology, and frozen biomedical LM embeddings are aggregated across ontology levels.
- **Key innovations**: Theoretical analysis shows SMI yields more informative representations than hierarchy-agnostic embeddings, particularly for rare/fine-grained concepts; a level-weighted variant selects global level weights on validation data. On MIMIC-IV it improves mortality, readmission, **drug recommendation**, and **rare drug prediction**; on eICU it yields more robust representations under cross-hospital distribution shift. (Accepted to NeurIPS 2026 Main Track.)
- **arXiv**: https://arxiv.org/abs/2610.18672

### 31. SimInter: Evidence-Grounded User Simulation with Interview-Based Profile Enrichment for Conversational Recommender Systems
- **Authors**: Erfan Shahabi, Amirhossein Roshandel, Mohammad Sadegh Sadeghi, Azadeh Shakery
- **Institution**: University of Tehran (School of Electrical and Computer Engineering)
- **Subjects**: cs.CL; cs.AI; cs.IR
- **Abstract**: Conversational Recommender Systems need reliable user simulators; LLM-based simulators condition on profiles from explicit ratings/demographics/static sources, capturing surface preferences while omitting **implicit behavioral characteristics** (decision-making style, aspect-level preferences, domain expertise). **SimInter** elicits these via **synthetic interviews between two LLM agents**, grounded in the user's statistical profile and historical conversational evidence, with an audit agent flagging fabrication/stereotyping at the turn level.
- **Key innovations**: On movie recommendation, simulating 300 ReDial users, SimInter significantly increases diversity of expressed preference aspects (filtered aspect entropy **1.619 vs 0.859**, paired d = 0.96, Holm-adjusted p < 0.001), a gain that persists against two trained recommenders (KBRD, UniCRS) under two independent judges. Human evaluation: **94.3%** of enriched-attribute claims supported/partially supported, and human judgments agree with **95.2%** of the auditor's binary decisions. (25 pages.)
- **arXiv**: https://arxiv.org/abs/2610.18308

## IR / Retrieval / Ranking

### 32. Revisiting Generative vs. Dense Retrieval: A Static Value Prior Reverses the Gap
- **Authors**: Renbo Tu, Yang Liu, Shuying Sun
- **Institution**: Shopify; University of Toronto
- **Subjects**: cs.IR; cs.AI; cs.LG
- **Abstract**: Generative retrieval (GR) is a strong candidate generator for sequential recommendation as language models and semantic-item identifiers improve, but it is **not uniformly stronger** than dense retrieval (DR) in online retail candidate generation. On two Amazon Toys datasets, GR leads on *best relevant item value* for covered users, while DR leads on **exact-target recall** and relevant value across the ranked list.
- **Key innovations**: Deep analysis finds **popularity contributes the most** to GR's measured value lead; adding the same static item value to DR in one reranking step **reverses** the lead while keeping recall above GR. On an industrial-scale internal e-commerce dataset with LLM-judged relevance, a **14B SID-LLM still underperforms a 47× smaller dense encoder**.
- **arXiv**: https://arxiv.org/abs/2610.19065

### 33. Web Scale on a Budget: Tail-Aware Retrieval Evaluation
- **Authors**: Boaz Meivar, Shai Avidan
- **Institution**: Tel Aviv University
- **Subjects**: cs.CV; cs.IR
- **Abstract**: Instance retrieval benchmarks grow galleries to improve discrimination (e.g., ILIAS with up to 100M distractors), assuming faithful evaluation demands web scale — a steep price (~200 GB of descriptors per model, hundreds of GPU-hours). The paper shows **evaluation itself obeys a scaling law**: the number of distractors outranking a positive is **Binomial** in gallery size. It defines a **per-query retrieval hardness** (gallery-scale agnostic) derivable from a small random sample.
- **Key innovations**: Adapts long-established sampled-rank machinery from recommender/biometric evaluation to visual retrieval. On ILIAS/INSTRE (100M) and GLDv2 (759k), a **5% sample (20× less indexing)** gives an EVT-based estimate converging onto the large-scale mAP within ~**0.01** (MAE 0.005) across five backbones/three benchmarks/two pools — an order of magnitude better than naively reporting the subset metric. Releases code + per-query hardness.
- **arXiv**: https://arxiv.org/abs/2610.17986

### 34. FASHION-RQ: Mining Hierarchical Semantic Structure for Automated Evaluation of Fashion Retrieval
- **Authors**: Tripti Shukla, Shwetha Somasundaram, Akshat Gupta, Rohit Garg, Paul Duff, Ian Anderson
- **Institution**: Glance (Bengaluru, India)
- **Subjects**: cs.IR; cs.AI; cs.CV; cs.LG
- **Abstract**: Fashion-retrieval evaluation is hard due to limited benchmarks capturing fine-grained open-ended queries; existing benchmarks rely on manual curation, predefined taxonomies, or synthetic prompts. **FASHION-RQ** derives user-type queries and relevance sets directly from **catalog structure**: hierarchical discrete representations learned by **RQ-VAE** organize products into semantically coherent clusters at progressively finer granularities.
- **Key innovations**: Builds **FASHION-RQBENCH**, a scalable benchmark *without manual query annotation or predefined taxonomies*, with four tasks (ranking, relevance classification, fine-grained sibling discrimination, paraphrase robustness) plus query- and attribute-level metrics. A human study shows the queries achieve comparable naturalness and **higher intent clarity** than real user queries.
- **arXiv**: https://arxiv.org/abs/2610.17841

### 35. RALI@iKAT 2026: Retrieval-aware User Profile Denoising via Personalized Conversational Dense Retrieval
- **Authors**: Yuchen Hui, Fengran Mo, Jia Ao Sun, Yuxing Tian, Wenhao Xu, Jian-Yun Nie
- **Institution**: RALI, Université de Montréal
- **Subjects**: cs.IR; cs.CL
- **Abstract**: Conversational systems build user profiles over time, which become noisy; existing personalized reformulation methods expand the query with profile phrases (rewrite-then-retrieve), reducing denoising to explicit phrase selection in sparse token space and separating personalization from relevance modeling. **PCDR** (Personalized Conversational Dense Retrieval) **jointly projects conversation history and user profile into a latent embedding space dedicated to retrieval**, inheriting context-denoising from conversational dense retrievers and needing only a few personalized relevance annotations.
- **Key innovations**: Evaluated on iKAT 2026, where it serves as the core retrieval component of a conversational AI agent; **ranked 1st in both retrieval performance and response quality** at iKAT 2026. (Presented at the SCAI Workshop @ SIGIR 2026.)
- **arXiv**: https://arxiv.org/abs/2610.17673

## Sequential Modeling / Time Series / Trajectory

### 36. Historical-Feature Residual Adaptation for Sequential Screening
- **Authors**: Yixiang Hong, Yuchen Zhang
- **Institution**: The University of Texas Health Science Center at Houston
- **Subjects**: cs.LG
- **Abstract**: Sequential screening policies must use acquired feedback under a fixed experiment budget. The paper studies **acquisition-time residual adaptation**: a small ranking correction built from **fixed historical features** and anchored to base scores recorded before feedback is revealed. Its primary instantiation augments **AssayFormer's** ten-dimensional representation with **64 historical directions** while retaining the pretrained model.
- **Key innovations**: Retrospective evaluation on 20 official-test screens from 15 recorded sources increased source-macro fraction of hits recovered from **22.58% → 28.61%**, exceeding all six prespecified comparators (same-feature ordinary ranking head: 25.73%). A separate model-independent pilot reconstructs features without AssayFormer assets (random-forest hit recovery 28.87% → 31.27% across three seeds). Gains depend on the base model. (NeurIPS 2026 Agentic AI for Biological Discovery Workshop.)
- **arXiv**: https://arxiv.org/abs/2610.19315

### 37. GIFT-Eval-CTX: A Benchmark For Contextual Forecasting Model Evaluation
- **Authors**: Xu Liu, Hanshu Yan, Taha Aksu, Quang Pham, Zhongzheng Qiao, Jun Hao Liew, Silvio Savarese, Doyen Sahoo, Junnan Li
- **Institution**: Salesforce AI Research (Moirai Team)
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Contextual forecasting uses forward-looking information (planned events, external conditions, expert expectations) to improve time-series forecasting, but reliable evaluation is hard: existing benchmarks have limited domain coverage, lack standardized history–future splits, or provide text not guaranteed to inform the future. **GIFT-Eval-CTX** isolates whether methods can translate **verified future information** into accurate numerical trajectories.
- **Key innovations**: Built on GIFT-Eval, **10,000 instances across 20 datasets**; each instance provides structured effects from the realized future — **Macro** (horizon-wide) and **Micro** (localized) — constructed with an agentic pipeline combining LLM discovery and deterministic code validation. Structured effects reduce aggregate relative MASE by **40.7%** for GPT-5.6 Sol and **29.6%** for Claude Opus 4.8 vs history-only prompting; the **MoiraiAgent** system achieves the best overall result.
- **arXiv**: https://arxiv.org/abs/2610.17794

### 38. Learning Across Temporal Graph Representation Silos
- **Authors**: Minwoo Yu, Young-guk Ha
- **Institution**: Konkuk University, Seoul (Smart Computing Laboratory)
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Temporal graph data are recorded in different representations, but whether these differences also determine the scope of learned-knowledge reuse is unclear. This study asks whether predictive structure learned from relational histories can be **reused between continuous-time dynamic graphs (CTDGs) and temporal knowledge graphs (TKGs)**, retaining distinct input/prediction interfaces and independent vocabularies.
- **Key innovations**: Demonstrates **bidirectional reuse** of learned **Relational Dynamics** across conventional representation boundaries; sources with the same representation are not always more useful, and the organization contributing to reuse varies across source–target conditions. Independently pretrained TKG and CTDG learners can be **fused at the score level** to improve prediction on a third dataset without entity/relation-semantic alignment; two proofs of concept in recommendation and security detection.
- **arXiv**: https://arxiv.org/abs/2610.19576

### 39. MMTA: Benchmarking Multimodal Temporal Analysis with Time Series, Text, and Vision
- **Authors**: Ziyang Zhang, Shenyi Li, Yilin Wang, Ziyun Cui, Bowen Zhou, Wen Wu, Chao Zhang
- **Institution**: Tsinghua University; Shanghai Artificial Intelligence Laboratory
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Most temporal benchmarks pair signals with text or with visualizations derived from the same signal, leaving open whether MLLMs integrate time series with **real-world visual evidence**. **MMTA** is a **tri-modal** benchmark (time series + text + vision) with diverse cross-modal complementarity patterns across nine domains (robotics, autonomous driving, human action, manufacturing, AR, healthcare, recommendation, finance, climate) under video+TS and image+TS layouts, with a **3,524-sample** test split.
- **Key innovations**: Standardizes heterogeneous real-world sources into a shared schema with domain prompts, provenance, and success-weighted metrics. Evaluating eight open/proprietary MLLMs exposes a shared bottleneck: representing time series as text creates very long token sequences and weak fine-grained alignment (especially long video). Introduces **TimeOmni-v** (dedicated time-series encoder, temporal positional alignment, modality-aware token layout, forecasting head). (NeurIPS 2026 Evaluations & Datasets.)
- **arXiv**: https://arxiv.org/abs/2610.17856

### 40. Retrieval Over Training: Similarity search-based Model Selection for Time Series Anomaly Detection
- **Authors**: Christos Panourgias, Roberto Stanzione, Adrien Petralia, Themis Palpanas, Paul Boniol
- **Institution**: Université Paris Cité (LIPADE); École Normale Supérieure / Inria
- **Subjects**: cs.LG; cs.AI
- **Abstract**: No single anomaly detector performs best across heterogeneous series, so a practical solution is **model selection**. Existing selectors drop accuracy in **out-of-distribution (OOD)** settings. **RAMSAD** is a **retrieval-based** framework: given a new series it queries a knowledge base of previously observed instances, retrieves the top-k most similar series, and transfers detector recommendations from their performance profiles.
- **Key innovations**: Works with standard similarity measures and embedding-based representations. Outperforms existing baselines **in-distribution** and is the **most robust selector in OOD**, where — when selecting a small subset of detectors — it matches or exceeds ensembles that run the entire detector pool at a fraction of their cost.
- **arXiv**: https://arxiv.org/abs/2610.20243

## Games / Multi-Agent / Bandits / Mechanism Design

### 41. Player-1: Learning to Play from Synthetic Experience
- **Authors**: Mingyu Ouyang, Yiran Wang, Siyuan Hu, Xingyilang Yin, Huiqiang Sun, Guangzhi Wang, Junfu Pu, Cheng Cheng, Honghao Chen, Ying Shan, Mike Zheng Shou, Hwee Tou Ng
- **Institution**: National University of Singapore; ARC Lab, Tencent IEG; Nanyang Technological University
- **Subjects**: cs.CV; cs.AI; cs.HC
- **Abstract**: Computer-use agents handle screens and keyboard/mouse actions, but **games** — visually rich with diverse mechanics — remain a demanding next step. Current game-agent pipelines rely on large demonstrations with limited coverage. **Player-1** is a post-training framework for learning game control **beyond demonstrations** through **synthetic experience**: it extends the computer-use action space with relative pointer motion, sustained inputs, and composite actions, and fine-tunes on **6,044** curated gameplay trajectories.
- **Key innovations**: **Player-1-Gym** provides sixteen synthetic 2D/3D environments with programmatically verifiable rewards, randomized observations, and control dynamics for multi-environment **PPO** RL. Player-1-9B and Player-1-35B-A3B improve MineDojo-300 success over their SFT policies by **27.8** and **17.7** points; Player-1-9B reaches **38.33%** vs **12.63%** for the strongest evaluated baseline, with further gains on ViZDoom-10 and GameWorld. (Code/project page released.)
- **arXiv**: https://arxiv.org/abs/2610.20584

### 42. SafeAdapt-Poker: Counterfactual Risk Calibration for Budgeted Adaptation under Opponent Shift
- **Authors**: Miaobo Hu, Shuhao Hu, Xiaobo Guo, Xin Wang, Bokun Wang, Rui Chen, Daren Zha, Jun Xiao
- **Institution**: University of Chinese Academy of Sciences (School of Artificial Intelligence); (co-authors)
- **Subjects**: cs.AI; cs.GT; cs.LG
- **Abstract**: Opponent histories can mislead after behavioral shifts. **SafeAdapt-Poker** formulates budgeted adaptation under opponent shift as a **dual-counterfactual sequential-control** problem using only pre-decision information: at each decision it asks (1) what local downside a deviation from the frozen anchor would induce under matched legal continuations, and (2) what future adaptation value would be lost by consuming deviation budget now.
- **Key innovations**: A monotone strategic-risk model answers (1); a paired budget-state continuation model prices (2). A **pathwise cumulative-KL ledger** bounds total anchor-relative deviation, and a finite family of frozen controllers is screened on complete paired calibration sessions. On exact **Leduc** the full controller attains matched weak-pool gain **+0.0718** with worst-opponent delta **−0.0126**, raises delayed-opportunity capture from 0.6318 → **0.7841** at the same budget, and reaches **+42.7 mbb/hand** in abstract-HUNL cross-play. (16 pages.)
- **arXiv**: https://arxiv.org/abs/2610.20473

### 43. Auction-based allocation of routes in capacity-constrained networks
- **Authors**: Gergely Csáji, Dávid Csercsik
- **Institution**: HUN-REN Institute for Computer Science and Control; Budapest University of Technology and Economics
- **Subjects**: econ.TH; cs.GT; econ.GN
- **Abstract**: The paper studies route-set allocation between end nodes in capacity-constrained **flow networks** with transfer costs. It introduces an **origin–destination (OD) bidding language** in which participants bid for bounded conic combinations of inlet–outlet–quantity licences, with winner determination solved as a network-flow optimization.
- **Key innovations**: Under a restricted model (open, uniformly priced sources; source-indifferent bidders), the **VCG payment is core-stable** — the key structural fact is that some optimal aggregate flows never use a physical pipe in both directions, reducing winner determination to a **single-commodity network flow** whose value is **submodular** in active bidders. If source access depends on the consumer (e.g., political gas deals), the reduction fails and VCG may fall outside the core; the paper proposes a **dual (nodal) pricing rule** from flow-conservation shadow prices that is always core-stable (at the cost of dominant-strategy IC).
- **arXiv**: https://arxiv.org/abs/2610.20125

### 44. No-Regret Learning in Stackelberg Security Games with an Unknown, Bounded Set of Attacker Types
- **Authors**: Sabil Ahmad, Ishita, Aditi Singh, Swaprava Nath
- **Institution**: Indian Institute of Technology Bombay
- **Subjects**: cs.GT
- **Abstract**: In repeated **Stackelberg security games**, a defender commits each round to a randomized resource allocation and a drawn attacker type best-responds. Existing no-regret guarantees assume the defender **knows the type set**. This paper drops that assumption: the type set is unknown and its size is at most K_max (itself unknown to the defender), and what can be learned depends on **what the defender observes**.
- **Key innovations**: If the defender observes each attacker's type, an algorithm that adds types as they appear achieves regret **Õ(n·K_max·√T)** — the same √T rate as with known types, at an extra factor of only √K_max and without ever using K_max. If it observes only the attacked target and types come from an infinite universe, **no algorithm has sublinear regret** (a fixed three-target game forces ≥ T−2); if told every B rounds which types have appeared, sublinear regret returns at Õ(n·K_max^{4/3}·T^{2/3} + K_max·B), and the additive delay cost is unavoidable. (39 pages.)
- **arXiv**: https://arxiv.org/abs/2610.20066

### 45. Euler: Towards Human-Centered Multi-Agent Mathematical Discovery
- **Authors**: Qiuyu Chen, Qi Wang, Liang Xu, Xin Jin, Baao Xie, Wenjun Zeng
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: AI-for-mathematics work centers on obtaining a **final answer**, leaving the exploration behind a result hard for researchers to understand, while long-running investigations face fragmented context and unsupported claims propagating across reasoning steps. **Euler** is a human-centered mathematical research system built around a **shared, structured representation** of the research process.
- **Key innovations**: Organizes statements, assumptions, proof dependencies, alternative approaches, failed attempts, and verification evidence into connected **research graphs**, letting researchers **trace how results developed** and supplying agents with persistent task-relevant knowledge for planning/collaboration/verification across sessions. Researchers can select a graph node linked to a saved team state, revisit earlier reasoning, and explore alternatives through continued interaction. Illustrated via three mathematical research case studies. (Code released.)
- **arXiv**: https://arxiv.org/abs/2610.19864

### 46. Exact Cut Complexity of Equal-Length Proportional Cake Cutting
- **Authors**: Yasushi Kawase, Bodhayan Roy, Mohammad Azharuddin Sanpui
- **Institution**: Chuo University (Tokyo); Indian Institute of Technology Kharagpur
- **Subjects**: cs.MA; cs.AI; cs.DS; cs.GT
- **Abstract**: Proportional **cake cutting** under an equal-length constraint requires each of n agents to receive a bundle of length exactly 1/n worth at least 1/n. The paper determines the **exact worst-case number of cuts** needed to guarantee such an allocation.
- **Key innovations**: Proves the exact bound is **2n−2** for every n (improving the prior quadratic upper bound) via the constrained necklace-splitting theorem and a recursive Hall's-theorem assignment argument; the bound extends to **envy-freeness when n is a prime power** (with an O(n^1.525) bound for general n). Also shows **no deterministic Robertson–Webb protocol** terminates finitely on every instance and returns an exact equal-length proportional allocation (even for two identical-valuation agents); for every ε>0, O(n²/ε) queries suffice to get value ≥ 1/n−ε with ≤ 2n−2 cuts; augmenting with two-knife queries attains the optimal 2n−2 cuts when n is a power of two. (MFCS 2026.)
- **arXiv**: https://arxiv.org/abs/2610.19733

### 47. CyberArena: Benchmarking AI Agents in Live Symmetric Attack-and-Defense Combat
- **Authors**: Bangya Liu, Jianhong Tu, Yueyang Pan, Hanhong Zhao, Zhe Ye, Hongwei Li, Saastha Vasan, Katherine Lambert, Junmin Zhu, Hao Wang, Jienan Chen, Yunze Xiao, Minglai Yang, Zihan Wang, Hairong Yin, Hao Wang, Zhiwen Fan, Tianneng Shi, Zhun Wang, Chenguang Wang, Dawn Song
- **Institution**: not stated (UC Berkeley-adjacent author list, unconfirmed)
- **Subjects**: cs.CR; cs.AI; cs.MA
- **Abstract**: Existing security-agent benchmarks evaluate agents in isolation against static targets, but real cyber operations are **dynamic and coupled**. **CyberArena** is a dynamic, **symmetric adversarial** benchmark built around multi-round attack-and-defense combat: in isolated sandboxes two agents compete under identical rules, acting concurrently as both attackers and defenders over continuously changing services, directly testing speed and precision in discovering, exploiting, and patching vulnerabilities.
- **Key innovations**: An automated agentic pipeline continuously generates/reviews/validates new environments for longevity, and a **dynamical model** maps match dynamics into unified multidimensional scores (offensive, defensive, domain-specific). Evaluating 12 frontier LLM agents across 40 challenges in 466 matches separates capabilities where single-agent baselines hit a ceiling (trajectories "read like a fight rather than an exam" — planting backdoors, writing a packet sniffer).
- **arXiv**: https://arxiv.org/abs/2610.19005

## Benchmarks / Evaluation / Interpretability

### 48. How GUI Agents Fail: GraceBench for Execution Stability Diagnosis
- **Authors**: Ridong Zhang, Shuxian Liang, Chaoqun Wan, Zhen Huang, Xian-Sheng Hua
- **Institution**: Institute of AI for Engineering, Tongji University
- **Subjects**: cs.AI
- **Abstract**: GUI agents' reliability depends not only on final outcomes but on whether they reach them through **stable interaction trajectories** — unnecessary actions, detours, and execution errors add noise or irreversible side effects even on successes. Existing benchmarks assess final success or a few milestones, leaving step-level behavior unclear. **GraceBench** represents each app's reachable interaction space as **UI Transition Graphs (UTGs)** and uses **video-grounded** trajectory evaluation over a graph-aligned representation.
- **Key innovations**: Metrics beyond success — **deviation rate, loop burden rate, recovery ability**. Contains **169 tasks** across 10 applications, **10 UTGs** with 2,909 canonical GUI states and 3,116 observed transitions, and **3,718 trajectories**. Findings: outcome scores hide instability — GPT-5.6 Sol has the highest success rate but the **lowest recovery ability**; **51.24%** of successful runs still contain a deviation or loop; equal SR/CR trajectories differ substantially in recovery.
- **arXiv**: https://arxiv.org/abs/2610.19900

### 49. Can Agents Forget When Asked? A Benchmark for Memory Unlearning in LLM Agents
- **Authors**: Bofan Xie, Chaokun Wang, Guanchen Ge, Songyao Wang, Fang Niu, Hang Zhang, Wei Wang
- **Institution**: Tsinghua University
- **Subjects**: cs.AI
- **Abstract**: As agents accumulate personal information, users increasingly ask them to **delete** sensitive/outdated facts; a memory system should remove exactly what was requested and keep the rest intact. Existing benchmarks evaluate only memory writing, retrieval, and organization. **Bemula** is the first benchmark dedicated to **memory unlearning**: 50 multi-session dialogues, **135 forget requests** of six types, **1,742 test questions**, with a control version per dialogue so only systems that stored the target can earn credit for forgetting.
- **Key innovations**: Five paired test suites measure storage, removal of requested info, preservation of unrelated memories, relearning of similar facts, and resistance to extraction attacks. Results are **negative**: across six mainstream memory systems under three backbones (plus Full-Context LLM), **no system passes more than 1.5%** of forget requests end to end and most pass none — they either leave the info extractable or delete far more than requested.
- **arXiv**: https://arxiv.org/abs/2610.18052

### 50. On the Monitorability of Natural Language Autoencoders: Identification vs Discrimination
- **Authors**: Kevin Yandoka Denamganaï
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG; cs.CL
- **Abstract**: **Natural Language Autoencoders (NLAs)** are proposed as oversight tools: an **Activation Verbaliser (AV)** writes an English explanation of an activation vector and an **Activation Reconstructor (AR)** maps the explanation back to a vector. Their oversight value depends on a human monitor distinguishing a **true** account of an activation from a **false** one. The paper formalises NLA training and NLA oversight deployment as two different referential games from Emergent Communication: training is a **generative** game, oversight a **discriminative, multi-modal, partially-observable** game.
- **Key innovations**: The gap between the two games predicts AV explanations will *identify* which activation they describe without *discriminating* its true account from closely matched false ones (training never asks explanations to rule anything out). Using the NLA's own AR as a maximally-sympathetic surrogate monitor, experiments confirm this on one released checkpoint: true accounts beat accounts of other activations in **all 320** comparisons, but beat fluent rivals differing in a single claim only **60.2%** of the time (std.err 6.7%, chance 50%). A meaning-preserving rewrite costs only **2.1%** of the distance to another activation's account, so the failure isn't from private conventions.
- **arXiv**: https://arxiv.org/abs/2610.18727

### 51. JockeyBench: Evaluating LLM Agents on Horse-Racing Decision-Making
- **Authors**: Zhongwei Xie, Xingsu Li, Jingqiao Yu, Zihao Wang, Hong ChiTat, Zhaowei Wang, Weizhi Du, Yuxuan Liu, Huihao Jing, Jiaxin Bai, Yangqiu Song
- **Institution**: The Hong Kong University of Science and Technology
- **Subjects**: cs.AI
- **Abstract**: Repeated event forecasting requires extracting predictive signals from noisy evidence and evaluating their value across successive decisions. **JockeyBench** studies this through historical Japanese horse racing, combining **time-gated evidence, priced tools, paired frozen-program controls**, and two workflows: executing an LLM-written predictor, or acquiring evidence for a fresh per-race LLM forecast. Evaluation separates forecast quality, benchmark-specific net utility, and retrospective betting returns/risk under fixed decision rules.
- **Key innovations**: Across **28 model–scaffold configurations on 324 races**, paired tests identify seven revision gains and two declines after multiple-testing correction — **yet every configuration has negative mean profit** under capped-Kelly settlement. The reusable-program workflow has higher mean betting profit and lower research fees, though both workflows lose on average; diagnostics show mean probability bias reverses on selected bets and profitable runs can depend on concentrated returns. Motivates evaluating predictive competence, adaptation, resource use, and decision value **separately**.
- **arXiv**: https://arxiv.org/abs/2610.19589

### 52. RuleTrek: Benchmarking Agentic Rule Reasoning in Complex Scenarios
- **Authors**: Chenhao Yuan, Bohan Yu, Yinhao Xu, Chao Yin, Chenxi Zhou, Zhaoxuan Wang, Shuwen Xu, Shaoping Huang, Haolin Ren, Jiaxiang Liu, Yao Xu, Jun Zhao, Kang Liu
- **Institution**: The Key Laboratory of Cognition and Decision Intelligence for Complex Systems, Institute of Automation, Chinese Academy of Sciences, Beijing
- **Subjects**: cs.AI
- **Abstract**: LLMs increasingly tackle specialized real-world tasks, but identifying and applying **domain-specific rules** remains hard when scenario information is distributed across multiple files; existing rule-reasoning benchmarks represent scenarios with only a few factual statements. **RuleTrek** is a multi-domain benchmark for agentic rule reasoning in complex scenarios, with a **rule-grounded construction pipeline** that extracts structured rule graphs and generates/incrementally composes rule-specific sub-scenarios while ensuring consistency and solvability.
- **Key innovations**: Assesses three capabilities in interactive workspaces — **Rule Identification (RI), Rule Deduction (RD), and End-to-End (E2E)** reasoning. Across 11 frontier LLMs the highest RI and RD scores are only **62.47%** and **60.43%**, while E2E ranges **26.97–55.29%** — showing current agents face substantial challenges in rule reasoning over complex scenarios. (Code/dataset released.)
- **arXiv**: https://arxiv.org/abs/2610.19698

---

## Coverage & Method Notes

- **Window**: arXiv export API, single `submittedDate:[20261013 TO 20261015]` sweep over 18 relevant primary categories → **1,330 unique records** (2026-10-13 block: 754; 2026-10-14 block: 576). Newest indexed submission `2026-10-14T17:49Z`; the 2026-10-15 block is not yet indexed. This is the **first** `arxiv-daily` run to mine the 10-13/10-14 blocks (the 2026-10-13 digest was still pinned to the 10-09 block).
- **Dedup**: repo-wide `\d{4}\.\d{4,5}` baseline = **9,123 IDs**; **1,323 / 1,330** harvested records are new-to-wiki; all **52 featured** re-verified grep 0-hit against the live wiki before writing (0 collisions), collision-managed against today's sibling `game-rl-daily`.
- **Sections (52 featured)**: Core AI/LLM/Agents (8), Reasoning/RL/Post-Training (9), Efficiency/Inference/Serving/Generation (5), Recommendation/Advertising/CTR/User Modeling (9), IR/Retrieval/Ranking (4), Sequential/Time Series/Trajectory (5), Games/Multi-Agent/Bandits/Mechanism Design (7), Benchmarks/Evaluation/Interpretability (5).
- **Affiliation provenance**: recovered from each paper's arXiv full-text HTML author block where available (`arxiv.org/html/{id}`); otherwise `not stated`. Notably recovered: **Sakana AI** (2610.18933), **Xiaohongshu Inc.** (2610.20293, 2610.18256), **Qualcomm AI Research + ETH Zurich** (2610.19868), **Google** (2610.19302), **NVIDIA** (2610.17780), **Salesforce AI Research** (2610.17794), **Tencent IEG ARC Lab + NUS** (2610.20584), **Shopify + U. Toronto** (2610.19065), **Glance** (2610.17841), **Sber AI Lab** (2610.17823), **Microsoft + HKUST(GZ)** (2610.18014).
- **CTR lane**: explicit industrial-CTR-prediction architecture work remains **absent** this block; the closest advertising material is **AdCoEvo** (ad delivery, §4) and **CASI** (sponsored-search auction, §1). Rec/ranking lanes are well-populated (13 papers across §4–§5).
