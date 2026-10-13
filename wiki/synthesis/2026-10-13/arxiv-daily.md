---
title: arXiv Daily AI/LLM/RecSys/CTR/Games (2026-10-13)
type: synthesis
created: 2026-10-13
updated: 2026-10-13
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

# arXiv Daily Report (2026-10-13)

Search scope: the arXiv export API's latest indexed announcement is still the **2026-10-09 (Fri) block** — `submittedDate:[20261009 TO 20261010]` returns **1,129 papers**, the identical block mined by the 2026-10-12 digest, and `[20261010 TO 20261013]` → 0 (no 2026-10-10/11/12 mailing is indexed as of this run). 2026-10-13 is a Tuesday; the Sat/Sun/Mon submissions are not yet in the export, and directly sorting `cs.AI` by `submittedDate` descending still bottoms out at `2026-10-09T17:59Z`. Because the block is unchanged, this run re-mines its **not-yet-reported tail**: the full 1,129-paper block was downloaded and parsed, then filtered to the relevant primary categories (`cs.AI`, `cs.LG`, `cs.CL`, `cs.IR`, `cs.GT`, `cs.MA`, `cs.MM`, `cs.CY`, `cs.NE`, `cs.SI`, `cs.SE`, `cs.CR`, `cs.SD`, `cs.RO`, `stat.ML`, `eess.SP`, `eess.AS`, `q-bio.NC/QM/GN`) → **429 papers**, of which **322 are new to the wiki** (grep-verified 0-hit against the 8,856-ID repo-wide baseline). The **50 featured papers below are all new to the wiki** and were not claimed by the 2026-10-09 → 2026-10-12 digests; all carry a 2026-10-09 submission date.

> ⚠️ Metadata note: the arXiv Atom API does **not** expose author affiliations. **Institution/company** is stated only where the abstract, comments, or a code/project link name one; otherwise it is marked `not stated (arXiv metadata omits affiliations)`, with an author-list hint flagged `unconfirmed` where relevant.

> ℹ️ Lane note: the classical **CTR / ad-auction / recommender-serving** lanes are again effectively empty in this block — its only directly topical papers (ECC ad-image editing, FORTE feature deprecation, GSP autobidding complexity, continuous-query generative recommendation, PC-LinUCB, and LLM-social polarization) were already claimed by the 2026-10-12 digest. The closest *new* material sits in §6 (word-of-mouth diffusion and network targeting, dynamic matching with abandonment, latent user-bias identification) and §2/§4 (delayed-outcome credit assignment for sequential decision-making). §2 RL/post-training remains the most crowded lane, and this run surfaces a strong **diffusion-LM / parallel-generation** cluster in §3.

## Core AI / LLM / Agents

### 1. A Baseline Assessment for the Agentic Web Technology Stack
- **Authors**: Vagner Figueredo de Santana, Diogo Cortiz
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI; cs.ET; cs.SE
- **Abstract**: The rapid pace of protocols, frameworks, and libraries proposed for LLM-based agents makes it hard to know how the pieces fit together, creating governance, skilling, and infrastructure burdens before organizations even join the Agentic Web. The paper introduces **MASTIF** (Multi-Agent System TestIng Framework) and a baseline evaluation of Agentic Web technologies — 3 LLMs, 3 protocols, and 4 agent-implementation frameworks — on 300 Mind2Web tasks.
- **Key innovations**: A system for assessing how different protocols/frameworks compose into a working Agentic Web solution; results show that picking a task-specific stack can improve task-completion rate, efficiency, and social-value stability while cutting verbosity and time-to-complete, establishing baseline metrics for a fast-moving design space.
- **arXiv**: https://arxiv.org/abs/2610.13703

### 2. Scaling Empowered Agents
- **Authors**: Catherine Ji, Vivek Myers, Joshua Lin, Alexandra Wingate, Sergey Levine, Benjamin Eysenbach
- **Institution**: not stated (Berkeley/Princeton-adjacent author list, unconfirmed; project: empowerment-geometry.github.io)
- **Subjects**: cs.AI; cs.LG
- **Abstract**: Empowerment measures an agent's capacity to actively control its environment. The paper explains the connection between skill learning and empowerment and introduces a scalable recipe for empowerment maximization: empowerment corresponds to the number of executable skills from a state, so maximizing it means reaching states that are good starting points for many skills — applicable to any underlying skill-learning method. Prior empowerment work is mostly tabular; this scales far enough to observe theoretically predicted but empirically elusive properties.
- **Key innovations**: A recipe that unlocks emergent behaviors at scale (e.g., building a house in Crafter), including resource gathering, environment modification, and survival, and that generalizes across skill-learning methods. 30 pages, 13 figures.
- **arXiv**: https://arxiv.org/abs/2610.13002

### 3. Scaling Agentic Data for Long-Horizon Terminal Intelligence
- **Authors**: Shun Zou, Ziyu Ma, Yi Zou, Yong Wang, Lin Chen, Zehui Chen, Guanhua Chen, Xiangxiang Chu, Feng Zhao
- **Institution**: not stated (project: zs1314.github.io/TerminalHorizon; Alibaba-adjacent author list, unconfirmed)
- **Subjects**: cs.CL
- **Abstract**: Terminal agents are moving toward real-world professional tasks. Short trajectories show commands and tool calls but not how agents accumulate evidence through exploration, adjust strategy under feedback, and turn intermediate results into deliverables. Synthesizing such environments risks completing or simplifying the very work the agent is meant to do. **TerminalHorizon** is a fully automated data-synthesis engine that starts from real professional work, uses independent execution to identify omitted key work, and reconstructs the environment from that evidence.
- **Key innovations**: Progressively expands tasks under the same goal to extend agentic patterns across stages; builds 1.5K task environments and SFTs Qwen3.5-27B into **TerminalHorizon-27B**, with gains on all 12 benchmarks (coding agents, production agentic tasks, general reasoning). Multiple RSI case studies (12-hour budgets) show continued experimentation and retention of improvements.
- **arXiv**: https://arxiv.org/abs/2610.13166

### 4. Collaborative Theory of Mind: Learning to Self-Revise by Anticipating User Responses
- **Authors**: Fanzhi Zeng, Anubrata Das, Maytal Saar-Tsechansky, Liu Leqi
- **Institution**: not stated (UT Austin-adjacent author list, unconfirmed)
- **Subjects**: cs.AI
- **Abstract**: LLMs perform well on individual tasks but still struggle to collaborate with users over extended multi-turn interactions — solving before understanding needs, or failing to revise mistaken assumptions after feedback. **CToM** explicitly trains LLMs to anticipate user responses and use those predictions to improve their own behavior: it drafts a response, predicts the user reply, and uses that prediction to guide internal revision before responding.
- **Key innovations**: Trains on the user's actual reply as the next-turn prediction target and combines that objective with GRPO. On collaborative math reasoning it raises final accuracy from 74.1% to 79.6% over naive GRPO; prediction supervision cuts user replies by 8% (coding) and 17% (writing) at equal reward, and more accurate predictions correlate with larger self-revision gains.
- **arXiv**: https://arxiv.org/abs/2610.12872

### 5. Travel Back To Move Forward: Retrospective Exploration and Evolving for Long Horizon Agents
- **Authors**: Ziang Ye, Wentao Shi, Lei Chen, Zhengzhou Cai, Yu Wang, Zhiyuan Yao, Zihan Wang, Xierui Song, Fuli Feng, Yixin Cao
- **Institution**: not stated (code: github.com/whi497/ReTRAIL)
- **Subjects**: cs.AI; cs.CL
- **Abstract**: Long-horizon LLM agents face cascading failures from early mistakes. Agents must proactively recover from dead-end states and convert exploratory experience into guidance. **ReTRAIL** rewinds the environment to earlier states while preserving valid progress and carrying forward knowledge learned from abandoned exploration — the environment state moves backward while the agent's knowledge moves forward.
- **Key innovations**: Trains a shared policy with two signals — State-Anchored GRPO comparing alternative continuations from revisited states, and a branch-advancement reward guiding reflection by subsequent progress. Across MineSweeper, Sokoban, ALFWorld, ScienceWorld: a bare rewind primitive offers little (sometimes harms), whereas coupling rewinding with experience reuse lets agents escape unproductive states and improve later exploration.
- **arXiv**: https://arxiv.org/abs/2610.13058

### 6. Work2Skill: Capturing Human GUI Experience for Reusable Agent Skill Induction
- **Authors**: Yuqi Huang, Hui Li, Yifei Cao, Zikun Cai, Tianci Xie, Yangfan Gao, Pinxue Guo, Chaoyun Zhang, Bingxuan Li, Rui Zheng, Hang Yan, Ning Liao
- **Institution**: not stated (code: github.com/china-qijizhifeng/Work2Skill)
- **Subjects**: cs.AI; cs.HC
- **Abstract**: Computer-use agents handle increasingly complex GUI tasks but struggle with unfamiliar software requiring human domain knowledge. Human demonstrations convey procedural knowledge through the same GUI interaction space, but reuse requires interpreting actions in context and separating workflow rules from task-specific detail. **Work2Skill** captures human GUI experience for reusable agent skill induction.
- **Key innovations**: **WorkRecorder** collects synchronized screen recordings, mouse/keyboard events, and accessibility-tree info; **WorkDemo-350** is the first synchronized multimodal dataset of human desktop GUI demonstrations (350 screened tasks). An agentic skill-induction method produces reusable skills capturing workflow rules, step dependencies, and completion checks. Mean score gains of 4.67–10.54 pts (MyPCBench Bounded Action) and 3.11–7.50 pts (286-task OSWorld-Verified subset) over the no-skill baseline across four execution models.
- **arXiv**: https://arxiv.org/abs/2610.12984

### 7. Quality, Not Just Outcome: A Structural Scoring Framework for Selecting Coding-Agent Trajectories for Supervised Fine-Tuning
- **Authors**: Sida Li, Yuanxin Liu, Shicheng Li, Linli Yao, Xu Sun, Haoli Bai, Xiaohui Li
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: Open coding agents are typically trained by SFT on trajectories whose final patch passes the test suite, but outcome-level filtering ignores process quality: successful trajectories may still contain repetitive file inspection, unstable tool use, or delayed modification, all of which become part of the imitation target. **TQS** (Trajectory Quality Score) scores coding-agent trajectories directly on trajectory structure — no LLM judge, linear time.
- **Key innovations**: Characterizes quality via structured convergence, information focus, intent–action alignment, and policy dynamics. On 155,144 successful trajectories from a public open-license corpus, models fine-tuned on top-TQS subsets consistently beat those trained on random or bottom-ranked subsets on SWE-Bench-Verified — a scalable alternative to LLM-based data selection.
- **arXiv**: https://arxiv.org/abs/2610.13152

## Reasoning / RL / Post-Training / Test-Time

### 8. A Step Harder, Not a Step Too Far: The Benefits and Limits of Curriculum Difficulty Progression in GRPO
- **Authors**: Ronghan Li, Fei Chen, Mingyu Lu
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: Curriculum learning typically orders samples easy-to-hard. In GRPO, medium-difficulty samples are attractive for online selection because they yield informative group-relative signals, but it is unclear whether persistently selecting them gives the strongest final model, and sample difficulty shifts as the policy evolves. This work re-estimates difficulty under the current policy and evaluates a staged curriculum that progressively shifts the active difficulty band harder.
- **Key innovations**: On GSM8K, persistent medium-difficulty selection is *not* strongest; progressing to a moderately harder band improves test accuracy to 0.6591 ± 0.0077 (vs 0.6449 ± 0.0024 fixed-medium), while progressing further drops it to 0.6405 ± 0.0053. Staged progression can beat fixed-medium, but the benefit is **non-monotonic**. 30 pages, 8 figures, 19 tables.
- **arXiv**: https://arxiv.org/abs/2610.13669

### 9. BoundaryEvo: Data-Model Co-Evolution at the Capability Boundary for Long-Chain Reasoning Distillation
- **Authors**: Jiaming Su, Suorong Yang, Xudong Li, Tengchao Yang, Peng Ye
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI; cs.CL
- **Abstract**: Distilling long-chain reasoning from large teachers helps small models, but existing methods fix the training set before distillation, ignoring that an example's usefulness changes as the student evolves — mastered examples add little supervision, and far-beyond-capability examples are hard to learn from. Reliable selection is hard when the student is initially weak. **BoundaryEvo** first primes basic reasoning capability, then adapts data to the evolving capability boundary.
- **Key innovations**: Two-stage co-evolution: Capability Priming distills a small trajectory set with no separate judge; then it repeatedly selects questions the current student has not mastered but the expert reliably solves. With only **1,000** training examples it beats static and dynamic selection baselines on 11 benchmarks, raising Qwen3.5-4B from 62.9→75.3 on IMO-AnswerBench and 26.8→46.0 on AMO-Bench.
- **arXiv**: https://arxiv.org/abs/2610.13285

### 10. Learning More by Training Less: Uncertainty-Guided Progressive Contraction for Efficient Reasoning Post-Training
- **Authors**: Suorong Yang, Jiaxin Wang, Jiaming Su, Chentao Yue, Furao Shen, Peng Ye, Soujanya Poria
- **Institution**: not stated (SUTD-adjacent author list, unconfirmed)
- **Subjects**: cs.AI
- **Abstract**: Scaling reasoning post-training with ever-larger corpora raises cost without proportional gains. This paper asks how far reasoning supervision can be compressed. The proposed framework builds Monte Carlo reasoning trees around intermediate states to expose process-level uncertainty, then contracts the corpus to a compact teacher-informed pool and, second, online-routes optimization according to the student's evolving learning state.
- **Key innovations**: Two-stage progressive contraction of both supervision and optimization. Across reasoning benchmarks and LLM families it uses as little as **0.22%** of the full-data-SFT optimization budget (450× less training exposure) while matching or improving reasoning performance, and generalizes to heterogeneous student families, black-box teachers, and weak-to-strong transfer.
- **arXiv**: https://arxiv.org/abs/2610.12933

### 11. What Should SFT Learn? Conditional Information Gain for Generalizable Post-Training
- **Authors**: Yuxuan Gu, Kequan Niu, Xiaocheng Feng, Yun Li, Yiqiao Yang, Bing Qin
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.CL; cs.AI; cs.LG
- **Abstract**: SFT forces a model to imitate external trajectories, which can interfere with pretraining behavior and hurt generalization. Recent dynamic SFT methods reweight tokens by model-side signals like predictive probability, but model compatibility is not learning value: a weakly supported token may be an undesirable mismatch or exactly the task-specific decision intended. **CIG-SFT** estimates the task-conditioned information carried by each demonstrated token.
- **Key innovations**: Under teacher forcing, it compares token likelihood from a frozen reference model with and without the task input, with the gold prefix fixed; the resulting conditional information gain is converted into a KL-regularized projection of the policy, yielding an equivalent scalar-weighted SFT objective whose gradient exactly matches the projected target. Beats standard SFT and adaptive baselines on math/code, with strong gains on tough evaluation distributions, needing no extra data or rollouts.
- **arXiv**: https://arxiv.org/abs/2610.12995

### 12. Rethinking Relative Policy Differences Transfer of On-Policy Distillation
- **Authors**: Rong Wu, Daocheng Fu, Yu Yang, Xuemeng Yang, Siqi Li, Shu Zou, Yao Zhu, Botian Shi, Bo Zhang, Cong Zhang, Pinlong Cai, Jianbiao Mei
- **Institution**: not stated (Shanghai AI Lab-adjacent author list, unconfirmed)
- **Subjects**: cs.LG
- **Abstract**: On-policy distillation (OPD) usually assumes the teacher is much stronger than the target; recent work instead transfers the *relative* policy difference between an expert and a reference. This paper develops a unified view in which the log-probability ratio between a proxy expert and proxy reference defines an implicit reward for KL-regularized policy optimization, inducing an on-policy update and recovering conventional OPD as a special case.
- **Key innovations**: Three findings: (1) a stronger expert is not necessarily better — differences from task-specific training (RL/SFT) transfer, while scale-only differences transfer weakly or not at all; (2) expert and reference are complementary (expert supplies capability, reference isolates the residual); (3) useful differences do not transfer to every target. Raw policy distance does not predict transferability, but a good reference can rescue otherwise failed transfer.
- **arXiv**: https://arxiv.org/abs/2610.13205

### 13. Hindsight Structured Advice Distillation: Steering Executor Agents with Advisors Trained on Their Failures and Task Characteristics
- **Authors**: O. Ozan Koyluoglu
- **Institution**: Samaya AI (the paper evaluates on Samaya's proprietary research agent)
- **Subjects**: cs.AI
- **Abstract**: Agents for specialized work (finance, healthcare, law) are often capable enough but miss task details — which filing reports a figure, how a company discloses a metric. Retraining is expensive or impossible for closed/shared agents; writing know-how into the prompt makes it long and identical for every input. The paper instead learns to *generate* guidance: a small advisor reads each input and writes structured advice appended to a frozen executor's prompt.
- **Key innovations**: **HSAD** trains the advisor with hindsight (privileged information): analyze the executor's failures, run it under several strategies to see which worked, and have a grade-and-trace-aware teacher write the advice that would have helped. On FrontierFinance an 8B advisor lifts the qualification rate of Samaya's leaderboard-topping agent from 52.9%→56.6%, above its own high-effort config at 37% lower cost per query; also improves WebShop, BIRD text-to-SQL, and ExpertLongBench.
- **arXiv**: https://arxiv.org/abs/2610.13000

### 14. SWE-Critix: Post-Training Generalist Verifiers for Assessing Coding-Agent Trajectories
- **Authors**: Jiajun Hu, Chun Yong Chong
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: Coding agents handle end-to-end software engineering where no oracle evaluator defines success, motivating verifiers that can judge and explain their behavior — but trajectories can be hundreds of iterative interactions long. Existing verifiers either rely on general-purpose LLMs or train critics that mostly emit scalar rewards, leaving training-based *generalist* verification underexplored. **SWE-Critix** learns to predict a completion label and generate a natural-language analysis.
- **Key innovations**: Combines SFT with RL and trains a series of 30B models on CodeForge-Preview trajectories. On a held-out test set, classification accuracy rises from 57% (base Qwen3-30B-A3B reasoning) to 66% after SFT and **78%** after RL; models, datasets, and training code are released.
- **arXiv**: https://arxiv.org/abs/2610.13356

### 15. TreeHCA: Hindsight-Guided Exploration and Credit Assignment for Multi-Turn LLM Agents
- **Authors**: Debajoy Mukherjee, Jeremy Carleton, Sushil Vemuri, Srinivas Shakkottai, Dileep Kalathil
- **Institution**: not stated (UT Austin-adjacent author list, unconfirmed; code: github.com/TheBlackCat22/TreeHCA)
- **Subjects**: cs.LG
- **Abstract**: Group-relative policy optimization assigns the same advantage to every token in an agent trajectory, leaving useful and unhelpful decisions undifferentiated. Hindsight credit assignment (HCA) can refine this, but its estimates rely on trajectories containing informative alternatives at consequential histories. **TreeHCA** couples hindsight-guided exploration with hindsight credit assignment, using changes in reference-answer likelihood to revisit intermediate histories and sample alternative continuations, forming a tree of reasoning and tool interactions.
- **Key innovations**: Derives the inverse-hindsight importance correction (including an exact finite-pool identity) for the changed sampling distribution, and uses a normalized tree backup to propagate terminal outcomes into turn-level advantages. Across seven QA benchmarks and three Qwen backbones, TreeHCA leads in aggregate exact match.
- **arXiv**: https://arxiv.org/abs/2610.12828

### 16. Variance-Reduced Policy Gradient is Nearly Minimax-Optimal
- **Authors**: Leonardo Cesani, Matteo Papini, Marcello Restelli
- **Institution**: not stated (Politecnico di Milano-adjacent author list, unconfirmed)
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Standard policy gradient suffers high estimation variance from Monte Carlo updates; off-policy variance reduction helps, but optimal sample complexity previously required restrictive assumptions (uniformly bounded importance weights) or impractical second-order operations. **LVR-PG** is a unified theoretical framework abstracting a class of first-order estimators that integrate recursive updates with defensive importance sampling (including PAGE-PG and STORM-PG).
- **Key innovations**: Proves the class achieves Õ(ε⁻²) last-iterate global convergence under weak gradient domination for general parametric policies using purely first-order updates and minimal assumptions; extends state-of-the-art lower bounds to continuous parametric policies to establish an Ω(ε⁻²) sample-complexity limit — confirming minimax-optimality up to logarithmic and horizon factors.
- **arXiv**: https://arxiv.org/abs/2610.13692

## Efficiency / Inference / Serving / Generation

### 17. On the Design Space of Continuous Diffusion Language Models
- **Authors**: Oscar Davis, Daan Roos, Alice Bizeul, Amitis Shidani, Victor Turrisi, Louis Béthune, Pierre Ablin, Marco Cuturi
- **Institution**: not stated (Apple/ENSAE-CREST-adjacent author list, unconfirmed)
- **Subjects**: cs.LG
- **Abstract**: Continuous diffusion language models (CDLMs) increasingly rival discrete diffusion, yet the training levers that matter for continuous modalities remain poorly understood. This paper studies two levers — self-conditioning and embedding geometry — and the mechanisms behind them, suggesting cheaper and more effective designs.
- **Key innovations**: Shows self-conditioning corrects a train/inference mismatch by exposing inference-like states, and that its gains can be recovered without an extra forward pass via a two-level interpolant **DoubleCat** (improves TinyGSM accuracy >3×). Adds discrete reveals to get **SemiCat**, reaching 49.94% on TinyGSM and beating discrete diffusion on four of six likelihood-based evaluations at 1.7B scale; finds cross-entropy drives embeddings toward a geometry whose decoding error matches one-hot.
- **arXiv**: https://arxiv.org/abs/2610.13834

### 18. Rethinking the Roles of Diffusion and Decoding: Predictive-State Flows for Parallel Language Generation
- **Authors**: Jinjin He, Xinsong Feng, Lucheng Fu, Sinan Wang, Bo Zhu, Jiayun Wang
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.CL; cs.LG
- **Abstract**: In continuous diffusion LMs, latents are mapped almost deterministically to tokens, which forces the prior to capture fine-grained discrete choices in continuous space. The paper argues generative roles should be divided: the diffusion prior generates high-level predictive information, while the decoder resolves remaining token-level choices. **Predictive-State Flows (PSF)** partitions a sequence into blocks, each with a predictive state computed only from preceding context.
- **Key innovations**: A rectified-flow prior generates the sequence of predictive states; a block-causal decoder then generates all blocks in parallel (autoregressive only within a block), reducing diffusion from L token-level states to K ≪ L states and token sequential depth to L/K. A 197M model with K=8 reaches generative perplexity 22.8 at 0.31 TFLOPs/1K tokens (vs 24.0 at 7.2 TFLOPs for ELF-B), with MAUVE@512 0.93 vs 0.73.
- **arXiv**: https://arxiv.org/abs/2610.12898

### 19. KV-Repurpose: A Testbed for Evaluating Non-Prefix KV-Cache Reuse
- **Authors**: Taiga Ikeda, Daisuke Miyashita, Jun Deguchi
- **Institution**: not stated (University of Tokyo-adjacent author list, unconfirmed; code: github.com/taiga333/eval-kv-repurpose)
- **Subjects**: cs.CL
- **Abstract**: KV-cache reuse in LLM serving is usually limited to exact prompt prefixes, blocking reuse when the same retrieved document appears after different system prompts, histories, or metadata. **KV-Repurpose** is an open-source, vLLM-based system for developing and evaluating segment-wise KV-cache reuse beyond exact prefixes, combining cache-aware segment scheduling, prompt construction, capacity management, workload generation, and runtime monitoring.
- **Key innovations**: On long-context benchmarks, naive segment reuse largely preserves quality for single-document QA/summarization but shows clear limits in cross-document reasoning. Under a Zipfian RAG workload (20% of requests share a fixed prefix), it reaches **63.9%** token-level cache-hit rate vs 3.3% for prefix caching at 30 GB cache (prefix caching only 17.9% even at 1 TB), lowering TTFT. Apache-2.0.
- **arXiv**: https://arxiv.org/abs/2610.13060

### 20. Surfing the Activation Wave: Analyzing the Information and Geometry of LLM Hidden States for Speculative Decoding
- **Authors**: Raghavv Goel, Sudhanshu Agrawal, Mukul Gagrani, Risheek Garrepalli, Mingu Lee
- **Institution**: not stated (accepted at NeurIPS workshops Axiom, GDDL, PriGM)
- **Subjects**: cs.CL; cs.AI
- **Abstract**: Decoder hidden states from different LLM layers encode complementary information, but speculative decoding picks target layers by fixed positional heuristics; optimal subset selection is combinatorial. This work presents a principled multi-layer hidden-state selection framework based on two criteria — informativeness (matrix-entropy analysis) and diversity (centered kernel alignment, CKA).
- **Key innovations**: Examines layer-wise Shannon entropy, aggregate entropy under concatenation, and pairwise CKA across depth, revealing distinct geometric/informational compartments; proposes entropy- and CKA-based layer-selection algorithms favoring informative, minimally redundant sets, plus token-entropy filtering. In EAGLE3-style speculative decoding, selected sets beat fixed baselines including the default [2, N//2, N−3] rule.
- **arXiv**: https://arxiv.org/abs/2610.12939

### 21. Monarch-MoE: Structured Experts for Multimodal Continual Instruction Tuning
- **Authors**: Xi Zhang, Boyu Diao, Zesen Chen, Ruiqi Liu, Hangda Liu, Yongjun Xu
- **Institution**: not stated (Chinese Academy of Sciences-adjacent author list, unconfirmed)
- **Subjects**: cs.LG
- **Abstract**: Continual multimodal instruction tuning causes catastrophic forgetting. Multi-expert LoRA distributes learning across experts, but updates to a dense low-rank expert still affect many output features. **Monarch-MoE** replaces the dense factors in LoRA experts with block-diagonal factors connected by a fixed permutation, giving blockwise gradient isolation: each block-pair update affects only one output block while all input→output block connections are maintained.
- **Key innovations**: Batched computation, fused forward operators, and an optimized backward pass make compact experts practical on limited hardware. Across three continual-learning methods on MLLM-DCL and UCIT with LLaVA-1.5-7B, first-task retention improves while adapter parameters drop ~75% and ~50%; forgetting as low as 0.52 pts (MLLM-DCL) and 0.10 (UCIT), fine-tuning and inference on a single 24 GB RTX 4090.
- **arXiv**: https://arxiv.org/abs/2610.13215

### 22. Returning to Development States: When Full Sandbox Snapshots Help Coding Agents
- **Authors**: Daniel Thi Graviet, Tanmay Shah
- **Institution**: not stated (uses Daytona sandbox snapshots)
- **Subjects**: cs.LG; cs.SE
- **Abstract**: Coding agents often make useful progress before they fail, yet retry-from-scratch discards the machine state created along the way. This makes failure recovery a search problem: if intermediate environment states preserve meaningful progress, restoring and branching from them could beat repeated restarts. The paper implements Go-Explore-style search over full Daytona snapshots.
- **Key innovations**: Finds that higher and more efficient solve rates depend mainly on progress *outside* the repository — databases, services, and other runtime state. Full-snapshot search is most effective when long-horizon coding work spans multiple services whose state cannot be reconstructed from a single diff. 7 pages, 6 figures, preprint.
- **arXiv**: https://arxiv.org/abs/2610.13841

## Memory / Personalization / Robust Training

### 23. L₀ Feature Selection via Monte Carlo Tree Search in High-Dimensional Financial Regression
- **Authors**: Cameron Mouangue, Tristan Cazenave
- **Institution**: not stated (Université Paris-Dauphine-adjacent author list, unconfirmed; ICAIF '26)
- **Subjects**: cs.LG; q-fin.CP; q-fin.ST
- **Abstract**: Feature selection is central in high-dimensional financial regression, where correlated predictors hurt stability and interpretability. Lasso shrinks coefficients, which is restrictive when informative signals are spread across correlated variables; exact sparse regression avoids shrinkage but is combinatorial and typically minimizes in-sample rather than out-of-sample error.
- **Key innovations**: A feature-selection framework based on Monte Carlo Tree Search with Generalized Nested Rollout Policy Adaptation (GNRPA), casting selection as a sequential decision process and scoring candidate subsets by out-of-sample validation performance, with a lexicographic objective on subset size and multicollinearity. On explaining NASDAQ-100 weekly returns from 1,072 engineered features it reaches out-of-sample R² 0.6961 vs 0.6313 for optimized Lasso.
- **arXiv**: https://arxiv.org/abs/2610.13574

### 24. Personalized Federated Direct Preference Optimization via LoRA Adapters
- **Authors**: Zhanhong Jiang, Soumik Sarkar
- **Institution**: not stated (AAAI Fall Symposium Series 2026)
- **Subjects**: cs.LG
- **Abstract**: Federated DPO aligns language models across distributed agents without centralizing preference data, but existing analysis assumes all clients converge to one shared policy — at odds with heterogeneous preferences. **pFedDPO** has each client keep a small private LoRA adapter atop a shared global base model: the base is synchronized via FedAvg each round, while adapters stay local to capture client-specific preferences.
- **Key innovations**: Proves this decomposition replaces the gradient diversity κ² in the FedDPO bound with a residual heterogeneity κ²_eff (no larger than κ² when adapters absorb client-specific directions) at the cost of an additive adapter-bias term that vanishes as adapters converge. Experiments show lower gradient norms than vanilla FedDPO at competitive training loss and per-client reward accuracy.
- **arXiv**: https://arxiv.org/abs/2610.12885

### 25. GIST: Generator-state-Informed Supervision for Tabular Foundation Models
- **Authors**: Zhangyang Peng, Jingze Shi, Tongyi Zhang, Yuyu Luo
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG
- **Abstract**: Tabular foundation models based on prior-data fitted networks use sampled hard query labels, leaving avoidable sampling variability in pretraining. A key observation is that intermediate generator states reveal label uncertainty beyond a sampled outcome. **GIST** uses these states to average query losses over conditional label distributions.
- **Key innovations**: Jointly designs task generation and query supervision, using entropy-calibrated encodings for tractable, input-consistent targets on supported label-dependent branches; shows the averaging preserves the population objective and yields no larger gradient covariance at fixed parameters. Under matched schedules, improves mean rank across three architectures on TabArena and TALENT, winning 62.1% of paired dataset-level comparisons vs hard-label controls.
- **arXiv**: https://arxiv.org/abs/2610.12904

### 26. Specialists Learn Faster: Knowledge Organization in Pre-training Shapes Knowledge Update Efficiency
- **Authors**: Sheng Zhao, Yuhao Zhu
- **Institution**: not stated (University of Rochester-adjacent author list, unconfirmed; project: horizon-lab.org/specialist)
- **Subjects**: cs.LG
- **Abstract**: An ideal model must continually update knowledge; most work focuses on post-training update efficiency. This paper studies how knowledge organization *during pre-training* shapes later update efficiency. Models trained on chronologically ordered knowledge specialize in recent knowledge ("specialists"); models trained on the same knowledge shuffled perform well across periods ("generalists").
- **Key innovations**: Surprisingly, specialists need far fewer update steps to acquire new knowledge. Derives a first-principles law relating update cost to optimization dynamics that closely predicts results, then designs a pre-training data-ordering strategy that preserves stable historical knowledge while enabling efficient updates to current knowledge; benefits transfer to real pre-trained models and existing knowledge-update tools. 25 pages, 12 figures, 11 tables.
- **arXiv**: https://arxiv.org/abs/2610.13835

### 27. Robust Langevin Sampling under State-Dependent Heavy-Tailed Noise with Applications to LLM Fine-Tuning
- **Authors**: M. Berk Sahin, Ege C. Kaya, Arda Fazla, Behzad Sharif, Abolfazl Hashemi
- **Institution**: not stated (Purdue-adjacent author list, unconfirmed)
- **Subjects**: cs.LG
- **Abstract**: Convergence guarantees for non-log-concave sampling with stochastic gradient Langevin Monte Carlo assume globally Lipschitz gradients and uniformly bounded noise variance — assumptions that can fail even in elementary problems and that do not reflect Bayesian fine-tuning of LLMs. This work relaxes both via generalized smoothness and a state-dependent heavy-tailed oracle with finite p-th moments (1 < p ≤ 2).
- **Key innovations**: Three methods — R-LMC (geometric-median centering + residual clipping under Lipschitz gradients), A-LMC (exact gradients, generalized smoothness), and RA-LMC (both, via robust estimation and a noise-aware step size) — with non-asymptotic Fisher-information convergence guarantees that assume neither dissipativity nor a functional inequality. Bayesian fine-tuning of LLMs and VLMs matches or beats SOTA baselines in accuracy and uncertainty quantification.
- **arXiv**: https://arxiv.org/abs/2610.12865

## IR / Retrieval / Ranking

### 28. SPARQL-LLM in the TEXT2SPARQL 2026 Challenge
- **Authors**: Panayiotis Smeros, Vincent Emonet, Ruijie Wang, Ana-Claudia Sima, Tarcisio Mendes de Farias
- **Institution**: not stated (SIB Swiss Institute of Bioinformatics; deployed at expasy.org, unconfirmed)
- **Subjects**: cs.IR
- **Abstract**: Querying distributed knowledge graphs via SPARQL is hard, requiring fluency in syntax, endpoints, and schema. KGQA systems translate natural language into SPARQL, and LLMs make this increasingly feasible. This paper describes **SPARQL-LLM**, an open-source KGQA system, in the TEXT2SPARQL 2026 challenge.
- **Key innovations**: Ranks first overall among eight competing approaches across all datasets, achieving up to **59%** higher accuracy than the second-best system, with multilingual answering (English, German, Spanish). Publicly released (github.com/sib-swiss/sparql-llm) and deployed over decentralized bioinformatics KGs. 6 pages.
- **arXiv**: https://arxiv.org/abs/2610.13648

### 29. SOAR: Source-Aware Reinforcement Learning with Precise Credit Assignment for Search Agents
- **Authors**: Shengze Huang, Zihao Tang, Jinluan Yang, Xin Yu, Zhenghao Lin, Xiao Liu, Zengxuan Wen, Yeyun Gong, Haizhen Huang, Weiwei Deng, Feng Sun, Qi Zhang, Fei Wu, Kun Kuang
- **Institution**: not stated (Microsoft-adjacent author list, unconfirmed)
- **Subjects**: cs.CL
- **Abstract**: RL for search agents suffers from *evidence fabrication*, where agents bypass external information and fabricate an incorrect answer, over-relying on unreliable internal knowledge as shortcuts. **SOAR** transforms monolithic reasoning into source-explicit trajectories by disentangling external (E_ext) and internal (E_int) evidence into parallel observable streams via a source-aware workflow.
- **Key innovations**: A Source-Consistent Reward guides policy evolution, and making source attribution explicit enables precise credit assignment between knowledge streams. SOAR improves 3B/7B backbones by 7.3%/5.4% while cutting evidence fabrication by **74.8%**, improving knowledge-intensive benchmarks and grounded reasoning. 17 pages, 16 tables.
- **arXiv**: https://arxiv.org/abs/2610.13157

### 30. Verifiable Retrieval for Legal Reasoning through Structure-driven Knowledge Graph
- **Authors**: Ibrahim Siddig, Sviatoslav Tugeev, Munir Georges
- **Institution**: not stated (RAGE-KG 2026 Workshop @ ISWC 2026)
- **Subjects**: cs.CL
- **Abstract**: Automation in reliability-critical contexts like law must be transparent and verifiable, but LLM systems are black boxes. RAG grounds generation in interpretable documents, yet as sources grow, naive retrieval degrades by ignoring critical context elements. This paper targets the German Legal Code: structure-driven parsing builds a knowledge graph for source-document navigation and retrieval.
- **Key innovations**: Compares several KG-informed chunking and retrieval strategies and evaluates their effect on the accuracy of retrieved citations, providing a verifiable-retrieval recipe for legal reasoning. 7 pages.
- **arXiv**: https://arxiv.org/abs/2610.13695

## Recommendation / Advertising / Marketing / User Modeling

### 31. How Social Reinforcement Shapes Word-of-Mouth: A Conviction-Based Model for Marketing Diffusion and Network Targeting
- **Authors**: Abhishek K. Umrawal, Curt Stutsman, Camille Woods, Eliot W. Robson
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.SI
- **Abstract**: Organizations rely on social networks to drive adoption and word-of-mouth, but consumers differ not only in whether they adopt but in how strongly they advocate — individuals who adopt under strong social reinforcement develop greater conviction and become more persuasive. Existing diffusion models abstract this away by treating influence strength as static. The **Pressure Threshold (PT)** model captures how social reinforcement shapes both adoption and subsequent advocacy.
- **Key innovations**: An individual's influence rises with cumulative social pressure at adoption, giving a tractable, interpretable representation of conviction formation. Accounting for reinforcement shifts optimal targeting toward consumers in cohesive regions with repeated exposure, and scalable heuristics retain data-dependent performance guarantees; on synthetic and real networks reinforcement boosts seeding effectiveness, and on time-stamped cascades the PT model improves predictive accuracy over standard diffusion models. 44 pages.
- **arXiv**: https://arxiv.org/abs/2610.13890

### 32. Dynamic Matching with Abandonment: Optimal Guarantees via Static Priority Policies
- **Authors**: Nick Arnosti, Rad Niazadeh, Pranav Nuti, Felipe Simon
- **Institution**: not stated (Cornell/Chicago-adjacent author list, unconfirmed)
- **Subjects**: cs.DS; cs.CC; cs.GT; econ.TH; math.OC
- **Abstract**: Stochastic dynamic matching with abandonment: agents of different types arrive over time, may abandon while waiting, and are matched in pairs for type-dependent rewards. No online policy can guarantee more than 0.5 of the omniscient benchmark (which knows all arrival/departure times), and whether 0.5 is achievable was a central open problem, even in special cases.
- **Key innovations**: Resolves it — on every instance a simple static priority policy, computable in polynomial time, earns at least **0.5** of the omniscient benchmark, proving the optimal competitive ratio is exactly 0.5 (up from the previous best 0.192). The analysis rests on a new lower bound on the probability that some agent from a given type set is available, with primal (LP-based priorities) and dual (type "values" from an LP-duality fixed point) constructions.
- **arXiv**: https://arxiv.org/abs/2610.12991

### 33. From Observation to Intervention: Identifiability of Latent User Bias in Human-AI Interaction
- **Authors**: Lucas Biechy, Yuxiao Li, Zhonghao He, Tianyi Qiu
- **Institution**: not stated (BiAlign Workshop @ NeurIPS 2026)
- **Subjects**: cs.HC
- **Abstract**: Alignment methods treat user behavior as a reliable proxy for preferences, but this breaks when users hold belief-dependent cognitive biases, risking irreversible "confirmation traps" and harmful feedback loops. This paper formalizes when an AI system can distinguish true preferences from behavior shaped by bias, modeling the interaction as a multi-armed bandit.
- **Key innovations**: Proves a **non-identifiability** theorem: under passive observation, a static binary biased user produces action-trajectory distributions strictly identical to an unbiased user in a transformed environment, so any action-only estimator is no better than random. Then proves active preference elicitation breaks this equivalence — a finite sequence of adversarial zero-reward interventions makes post-intervention action distributions arbitrarily separable, suggesting robust alignment requires active intervention.
- **arXiv**: https://arxiv.org/abs/2610.13185

## Sequential Modeling / Time Series / Trajectory

### 34. Target-Constrained Pooling for Trajectory Extrapolation
- **Authors**: Ning Wang, Claire Cardie, Sainyam Galhotra
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG
- **Abstract**: Trajectory extrapolation from a partial target trajectory is underdetermined, but completed related trajectories carry information about the unresolved continuation. **Target-constrained pooling (TCP)** separates the finite-horizon endpoint from continuation shape and estimates the endpoint from two complementary source signals.
- **Key innovations**: Uniform pooling captures final response levels; matched-increment pooling captures remaining change after aligning source and target states. TCP selects representative sources, projects both endpoint estimates onto a target-consistent region, converts them into corrections of the free forecast, and controls influence via strength calibration and degradation-aware weighting. Across 25,245 targets from five domains it reduces mean RMSE by 35.8%–42.1% for all ten target-only forecasters and improves all 100 comparisons, using 12.7× fewer donor inputs.
- **arXiv**: https://arxiv.org/abs/2610.13034

### 35. Looking Ahead and Back: Anticipatory Generative Modeling for Road-Network Trajectories
- **Authors**: Zhenhao Huang, Li Sun, Philip S. Yu
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI; cs.LG
- **Abstract**: Within road networks, vehicle movement along segments is largely deterministic, whereas intersection transitions are critical — multiple outgoing paths may be equally plausible yet lead to very different downstream routes. Existing generative methods simulate location sequences and fail at next-transition selection, even producing off-network trajectories. This paper shifts from location simulation toward behavior modeling: generative route planning.
- **Key innovations**: **Foresight** is a graph-constrained generative paradigm that resolves next-transition selection by *anticipating* how the future route may unfold toward the destination, forming an "anticipate–select–update–re-anticipate" loop that enables longer-term foresight while continuing sequential generation along the history. Beats state-of-the-art baselines.
- **arXiv**: https://arxiv.org/abs/2610.13131

### 36. In-Context Learning for System Identification: Probabilistic Formulation, Long-Sequence Handling, and Benchmark Validation
- **Authors**: Matteo Rufolo, Dario Piga, Filippo Pura, Marco Forgione
- **Institution**: not stated (SUPSI-adjacent author list, unconfirmed)
- **Subjects**: cs.LG; cs.AI; eess.SY
- **Abstract**: Traditional system identification trains a model from data, then predicts outputs for new queries; recent in-context approaches learn a meta-model mapping training data and query inputs directly to outputs zero-shot, bypassing explicit model estimation. This paper advances the meta-learning framework for system identification in three directions.
- **Key innovations**: (1) a unified probabilistic meta-identification architecture combining a Transformer encoder-decoder with long-sequence mechanisms for calibrated long-horizon predictions; (2) shows a pre-trained meta-model can act as an uncertainty-aware synthetic data generator regularizing parametric models when real data are scarce; (3) systematic evaluation on nonlinear system-identification benchmarks and an out-of-distribution scenario, with competitive accuracy and strong generalization (input-only adaptation suffices for significant distribution shifts).
- **arXiv**: https://arxiv.org/abs/2610.13411

### 37. Probabilistic Ship Trajectory Forecasting using Transformer Models on AIS Data
- **Authors**: Frederik E. T. Schöller
- **Institution**: not stated (manuscript written in 2021)
- **Subjects**: cs.LG; cs.RO
- **Abstract**: Anticipating vessel trajectories matters for human navigators and autonomous surface vessels, enabling sub-routines such as collision avoidance. This paper investigates Transformer and Performer models for trajectory prediction of surface vessels in confined waters using Automatic Identification System (AIS) position data.
- **Key innovations**: Conveys historical movement of nearby vessels via positional heat maps generated with Kernel Density Estimation and encoded by a CNN before entering the Transformer; trains with quantile loss for a model-aware prediction interval. The proposed architectures greatly outperform prior work, and the local heat maps enable predicting vessel movement not otherwise indicated by prior positions. 16 pages.
- **arXiv**: https://arxiv.org/abs/2610.13557

### 38. SeoulMMOD: A Large-Scale Multimodal Origin-Destination Flow Benchmark
- **Authors**: Taeyoung Yu, Seonbin Jo, Jiwon Kim, Junyoung Byun
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG
- **Abstract**: Origin-destination (OD) flow forecasting supports urban mobility decisions, but most public OD benchmarks give only a partial view of citywide mobility (one service or at most two modes), making it hard to separate mode shifts from changes in total travel. **SeoulMMOD** is a large-scale public benchmark for citywide multimodal mobility in Seoul.
- **Key innovations**: Three years of hourly OD flows across 6 urban travel modes, 25 districts and 426 sub-districts, with travel-time/distance, calendar, rainfall, and POI signals; benchmarks 14 baselines under a common protocol and analyzes spatial scaling, joint vs mode-separate training, and cross-year generalization. Finds several district-level spatio-temporal models do not scale to sub-district OD forecasting and that naive joint multi-mode training does not consistently help.
- **arXiv**: https://arxiv.org/abs/2610.13730

## Games / Multi-Agent / Bandits / Mechanism Design

### 39. The Distortion of Threshold Approval Multiwinner Voting
- **Authors**: Mohamad Latifian, Marzieh Nilipour, Alexandros A. Voudouris
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.GT
- **Abstract**: Multiwinner voting with n voters and m candidates selects a committee of size k. Voters have unit-sum cardinal utilities but report only coarse information induced by t utility thresholds, partitioning candidates into approval sets. Each voter's utility for a committee is a normalized monotone symmetric norm, capturing additive welfare, best-representative utility, top-r welfare, ℓ_p welfare, and normalized non-increasing OWAs.
- **Key innovations**: A deterministic rule with distortion at most 2(2m)^{1/t} and a randomized rule with distortion at most 2·min{m^{1/(t+1)}, m/k}, holding for every committee size and every norm in the framework. A single threshold gives O(m) (deterministic) and O(√m) (randomized) distortion, while O(log m) thresholds suffice for constant distortion; norm-dependent lower bounds asymptotically match for constant committee sizes.
- **arXiv**: https://arxiv.org/abs/2610.13725

### 40. The False Allure of "Security by Obscurity": A Game-Theoretic Approach
- **Authors**: In-Uck Park, Sunoo Park
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.GT; cs.CR; cs.CY; econ.TH
- **Abstract**: "Security by obscurity" — hiding how a system works to protect it — is poorly regarded yet has persistent intuitive appeal. The debate is about how attackers and good-faith researchers respond to openness, but the field lacks empirical or theoretical foundations for its long-standing beliefs. This paper provides the first rigorous modeling of security by obscurity.
- **Key innovations**: Captures how rational actors respond to openness or obscurity in fallible systems and proves that, in equilibrium under realistic conditions, "obscured" systems are **more** likely to suffer successful attacks than "open" systems — theoretical support for the received wisdom.
- **arXiv**: https://arxiv.org/abs/2610.12858

### 41. Gaussian-Width Bounds for Offline-to-Online Linear Bandits
- **Authors**: Kushagra Chandak, Volodymyr Tkachuk, Xiaoqi Tan, Csaba Szepesvári
- **Institution**: not stated (DeepMind/Alberta-adjacent author list, unconfirmed)
- **Subjects**: cs.LG
- **Abstract**: Studies how offline data helps online learning in stochastic linear bandits under partial coverage, where only k of d feature directions are poorly covered. Existing phased-elimination/optimism analyses give regret Õ(√(dkT)); the paper shows this dependence arises from loose control of reward-prediction error.
- **Key innovations**: Obtains tighter bounds via concentration of Lipschitz functions of Gaussian vectors, developing a phased-elimination algorithm with regret Õ(k√T). For the unit Euclidean ball it proves a matching lower bound under partial coverage and matching upper/lower bounds under uniform coverage; also studies pure exploration with offline data, giving matching bounds for fixed-design and adaptive algorithms.
- **arXiv**: https://arxiv.org/abs/2610.12990

### 42. CB-Orchestrator: Adaptive Workflow Optimization for LLM Agents via Contextual Bandits
- **Authors**: Jiahang Sun, Zhiwei Shang, Zhipiao Liu, Hongwei Yang, Guoqing Xie, Shuang Qiu, Zhongxiang Dai
- **Institution**: not stated (ICML 2026 Workshop on Compositional Learning)
- **Subjects**: cs.LG
- **Abstract**: LLM agents tackle complex tasks through agentic workflows, but hand-designing them is labor-intensive and inflexible; automated workflow optimization often incurs expensive API costs during training-phase feedback collection and fails to adaptively reuse high-quality workflows. **CB-Orchestrator** decouples workflow generation from selection.
- **Key innovations**: Stage 1 builds a diverse candidate-workflow pool via evolutionary search; stage 2 formulates workflow selection as a **contextual bandit**, enabling sample-efficient learning with far less feedback, and at inference adaptively selects the optimal workflow per query. Across five benchmarks it beats all baselines, and on MATH reduces training-phase API token overhead by ≥40.55% (total end-to-end ≥29.73%).
- **arXiv**: https://arxiv.org/abs/2610.13064

### 43. When AI Advisors Agree: Distinguishing Forecast Risk from Forecast Reliability
- **Authors**: Russlan Ramdowar
- **Institution**: iPulse AI (the study analyzes four production batches of iPulse AI forecasts)
- **Subjects**: cs.MA
- **Abstract**: If several AI advisors give similar forecasts, should we trust them more? Agreement can reflect shared useful evidence, but it can also reflect an asset that was easier to forecast. The paper examines this using 928 completed first-quarter forecasts for 232 assets across four production batches of iPulse AI, comparing archived Gemini-config forecasts with later market outcomes.
- **Key innovations**: Mean absolute return error rises from 10.31 pp (lowest-disagreement quartile) to 21.05 pp (highest) — but a "no price change" forecast shows almost the same increase (9.89→21.15), and the disagreement–error relationship is not resolved after accounting for visible asset risk. Retaining the lowest-historical-volatility quarter yields lower error than least-disagreement selection (7.97 vs 10.31 pp). Direction agreement raises directional accuracy but also return-magnitude error — distinguishing asset risk, directional agreement, and return precision.
- **arXiv**: https://arxiv.org/abs/2610.13431

### 44. Collective Autonomous Vehicle Routing Needs Social Awareness for Coexistence with Human Drivers
- **Authors**: Anastasia Psarou, Mikolaj Rams, Blazej Torbus, Rafal Kucharski
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.MA; cs.AI
- **Abstract**: Collective AV route choices can create externalities for human-driven vehicles (HDVs), since routes that benefit AVs may increase travel times for others. The authors add a social component — the *marginal cost*, an AV's impact on others' travel times vs a counterfactual simulation with the AV removed — to the selfish travel-time AV reward, and study mixed-autonomy routing via MARL.
- **Key innovations**: On the real networks of Ingolstadt and Provins, incorporating marginal cost into the AV reward limits HDV travel-time increases, shortens AV travel times, and improves overall system performance (Ingolstadt: 40% AVs raise others' travel times by 1.7% under selfish routing, 1.1% with the social reward). Computing marginal cost only for the most influential AVs achieves similar performance at much lower cost; over-weighting the social term degrades the system.
- **arXiv**: https://arxiv.org/abs/2610.13439

### 45. Tight asymptotic competitive ratio for the Canadian Traveller Problem on unit-weighted grids
- **Authors**: Pierre Bergé, Vsevolod Chernyshev, Malory Marin, Alexey Pyrko, Lou Salaün
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.DS
- **Abstract**: The k-Canadian Traveller Problem (k-ctp) is an online navigation problem: on an undirected weighted graph, a traveller goes from s to t minimizing distance, but up to k edges may be blocked and are discovered only upon reaching an endpoint. Performance is measured by competitive ratio vs an omniscient traveller. A general lower bound 2k+1 holds even for series-parallel graphs, while constant ratios are achievable on restricted classes.
- **Key innovations**: Establishes the first **intermediate** competitive ratio between constant and linear: on unit-weighted solid grid graphs there is an online algorithm with competitive ratio O(√k), asymptotically tight even on unit-weighted square grids. Shows both the unit-weight and solidity assumptions are essential — arbitrary edge weights or non-solid unit-weighted grid structures yield an Ω(k) linear lower bound.
- **arXiv**: https://arxiv.org/abs/2610.13712

## Benchmarks / Evaluation / Interpretability

### 46. Mind the Spatial Gap: A Benchmark for Geospatial Reasoning and Constrained Spatial Editing
- **Authors**: Zheng Ren, Yanning Wang, Ziheng Huang, Fei Huang, Shiqi Wang, Ziqian Ye, Yang Yue
- **Institution**: not stated (under review at ICLR 2027)
- **Subjects**: cs.AI
- **Abstract**: Understanding and manipulating spatial relations is fundamental to AI reasoning about physical environments, but existing evaluations of MLLMs rely on static QA over small or synthetic scenes and rarely probe whether models can modify spatial configurations under explicit geometric constraints. **GeoSpatialBench** evaluates an escalating progression from spatial-relation understanding and geometric reasoning to constrained spatial editing.
- **Key innovations**: Grounded in real urban data across six cities, with a taxonomy of 28 topological/directional/metric/ordering relations in structured GeoJSON and map-image modalities, ground-truth constraints verified via GIS operations. Reveals a stark spatial gap: GeoJSON consistently beats map images; multimodal combinations give no reliable gain; editing on ordering relations declines vs QA and most failed edits violate a specified constraint. 15 pages.
- **arXiv**: https://arxiv.org/abs/2610.12881

### 47. MAGMA-Bench: Evaluating Long-Horizon Embodied Agents under Dynamic Tasks and Execution Failures
- **Authors**: Loan Bernat, Matthieu Grard, Ariane Herbulot, Florent Lamiraux
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI; cs.RO
- **Abstract**: Long-horizon embodied agents must maintain task-relevant information, coordinate heterogeneous robots, and adapt as execution unfolds; existing benchmarks study dynamic execution and embodied multi-agent coordination but rarely their intersection. **MAGMA-Bench** is an architecture-agnostic benchmark for persistent task reasoning in dynamic multi-robot environments.
- **Key innovations**: Evaluates agents across increasing task horizons and controlled online perturbations (execution failures, task interruptions, mission updates) with scenarios requiring coordination across robots of heterogeneous capability, using a structured skill-level interface separating task reasoning from perception/control. Even the strongest evaluated models fail on a substantial fraction of clean episodes and degrade under perturbations; supervised adaptation helps a small model but remains far behind on longer multi-robot missions. Releases the benchmark, 261,646 task-level training examples, and an expert-trace pipeline.
- **arXiv**: https://arxiv.org/abs/2610.13534

### 48. Language Models Have Interpretable Narrative Mechanisms
- **Authors**: David Yiyang Liu, Aditya Joshi, Paul Dawson, Andrew Piper
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.CL
- **Abstract**: Investigates whether language models contain internal components that represent *narrativity*, the degree to which a text exhibits narrative properties. Across GPT-2-Small, Gemma-2-2B, and Llama-3.1-8B, the authors identify attention heads, MLP neurons, and sparse-autoencoder features whose activations correlate with narrativity.
- **Key innovations**: Ablating selected neuron/feature sets increases next-token prediction loss more for high- than low-narrativity texts and reduces the narrativity of open-ended generations; on downstream benchmarks the largest effects are in story completion and narrative QA, though they vary across models and languages and are mixed on confabulation/hallucination. Provides causal evidence that selected components contribute to model behavior. 24 pages.
- **arXiv**: https://arxiv.org/abs/2610.12989

### 49. Task Context Shapes Component Roles in Language Models
- **Authors**: Sovesh Mohapatra, Dani S. Bassett
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.CL; cs.AI
- **Abstract**: LLMs reuse the same attention heads across tasks, but identifying shared heads does not explain what they do differently per task — a natural analogy is task-dependent interactions among shared brain regions. The paper compares fixed model components across tasks using identical graph facts, measuring how interventions affect attention heads and later-layer activations (influence) and the answer (importance).
- **Key innovations**: Task changes redistribute influence in five open-weight models (four families, 1.5–14B). In Gemma-2-9B and Qwen3-14B, an activation edit changes an early activation vector and switches which fact the model reads while the written instruction stays fixed; per-prompt linear response maps predict a later head's response from an earlier head's change, reducing MS prediction error by 53.6% (Gemma) and 5.0% (Qwen) for a factual intervention. Suggests a network account of task-dependent computation and guides targeted interventions.
- **arXiv**: https://arxiv.org/abs/2610.13895

### 50. Evaluating LLM Creativity through Long-Tail Performance
- **Authors**: Yichen Wang, Tenghao Huang, Vishakh Padmakumar, Mina Lee
- **Institution**: not stated (code: github.com/YichenZW/longtail-creativity)
- **Subjects**: cs.CL
- **Abstract**: Creativity benchmarks for LLMs vary widely in task and metric design, raising the question of whether they capture a common notion of creativity. The paper proposes that the shared target is task-specific performance in the *long tail* of a reference input–output distribution, grounding this in the novelty-quality product formulation and evaluating it across 15 benchmarks and 26 open-weight models (n-gram absence as a novelty proxy).
- **Key innovations**: Creativity benchmarks lie further in the tail than standard benchmarks, and higher-tail subsets of each benchmark rank models more consistently with human creativity judgments in LM-Arena. Introduces **q@Tail(α)**, a lower-cost creativity diagnostic measuring mean task quality on the tail fraction of an existing benchmark; applying it to creativity-promoting methods shows substantial room to improve LLM creativity via stronger tail performance. 26 pages.
- **arXiv**: https://arxiv.org/abs/2610.12998
