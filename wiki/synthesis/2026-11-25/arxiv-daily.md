---
title: "arXiv Daily — AI / LLM / Recommendation / Advertising / Sequential Modeling / CTR / Games (2026-11-25)"
type: synthesis
created: 2026-11-25
updated: 2026-11-25
sources: []
tags: [arxiv-daily, ai, llm, llm-agents, recommendation, advertising, ctr, sequential-modeling, sequential, games, agents, post-training, auto-bidding, rta, e-commerce]
---

# arXiv Daily — 2026-11-25

> **Window**: arXiv Atom API (`export.arxiv.org/api/query`, `sortBy=submittedDate`, `max_results=10`) — query sets: `all:"large language model"` (LLM), `cat:cs.AI` (AI), `all:recommendation`, `all:advertising`, `all:adtech`, `all:"sequential modeling"`, `all:CTR`, `all:games`; newest submissions 2026-11-23 (small tail 2026-11-24).
> **Method**: Atom API abstract-level screening; deduped vs all wiki IDs (`grep wiki/synthesis/**`) — selected 15 papers new to the wiki except 2611.25659v1 / 2611.24283v1 which also appeared in the 2026-11-23 batch (`wiki/synthesis/2026-11-23/arxiv-daily.md`); re-included here as central to the requested domains.
> **Affiliation discipline**: arXiv API/abs pages list almost no author affiliations; **Institution / Company = "Not stated on arXiv metadata (best effort)"** unless an affiliation line was visible in paper comments (e.g., Taobao context for DNA 2611.25659v1, MARS Technical Report 2611.24006v1). Institutional context quoted from paper text/comments only; otherwise marked tentative or absent.
> **Flags**: Metrics/results are author-reported; no full-text review; papers screened at abstract level.

---

## 1. AI / LLMs

### 1.1 TipSweep: Precision-Aware Learning Rate Transfer Across Block Count in LLM Post-Training
- **Authors**: Nan Chen, Soledad Villar, Soufiane Hayou
- **Institution / Company**: Not stated on arXiv metadata (best effort)
- **Published**: 2026-11-23 · cs.LG/cs.CL · [arXiv:2611.31166](https://arxiv.org/abs/2611.31166)
- **Abstract**: The post-training of pretrained large language models, including supervised finetuning (SFT), direct preference optimization (DPO), and reinforcement learning with verifiable reward (RLVR), is very sensitive to the learning rate, and tuning it through grid search is costly in both computation and memory. In this work, we propose TipSweep, a method to transfer the learning rate across the number of trainable transformer blocks. To do so efficiently, we search for the best learning rate by training only the last k₀ blocks (in our experiments, typically k₀=1), and provide scaling rules that predict the optimal learning rate when training any set of k blocks, including when k=L (the full transformer). Across experiments with models ranging from 1 to 7 billion parameters, we observe that the optimal learning rate follows precision-dependent scaling rules: the optimal rate scales approximately as k⁻¹ with float32 (FP32) master weights, but as k⁻¹/² when updates are applied directly to bfloat16 (BF16) weights without a master copy. We explain both rules using an analytical model that accounts for update rounding, under assumptions supported by profiling experiments. Finally, we develop two prototypes of the learning rate search for a 6.7-billion-parameter model: one fits the search on a single consumer GPU with 16 GiB of memory; the second speeds up the search on a high-end GPU by evaluating all candidate learning rates in a single pass over the data, so that a five-candidate search takes about half the GPU hours of one full-depth (k=L) run.
- **Key innovations**:
  - TipSweep: LR transfer across block counts by training only the last k₀=1 blocks; scaling rules predict optimal LR for any k (incl. k=L).
  - Precision-dependent scaling: LR ∝ k⁻¹ with FP32 master weights vs k⁻¹/² without master copy under BF16 — both explained by an analytical update-rounding model.
  - Single-GPU prototype (16 GiB) + fast single-pass multi-candidate evaluation prototype for 6.7B models.

### 1.2 CO-GRAFT: Attributing Reinforcement Learning Gains in Search Agents via Role-Level Policy Grafting
- **Authors**: Ramraj Chandradevan, Sayontan Ghosh, Vinoth Selvendran
- **Institution / Company**: Not stated on arXiv metadata (best effort)
- **Published**: 2026-11-23 · cs.IR/cs.AI/cs.CL · [arXiv:2611.31185](https://arxiv.org/abs/2611.31185)
- **Abstract**: Reinforcement learning (RL) improves large language model search agents by up to 32 exact-match (EM) points over their pre-RL initializations, yet overall accuracy gains do not identify which underlying functional capabilities improve or interact during training. We introduce CO-GRAFT, a reward-agnostic interventional attribution framework in which an RL-trained agent and its pre-RL initialization jointly generate a single trajectory under closed-loop execution with live retrieval. Each policy controls a mutually exclusive subset of four functional roles: intermediate reasoning, search-or-answer decision, search query generation, and final answer extraction. Evaluating all 2⁴=16 role assignments without modifying weights or retraining defines a cooperative game whose Shapley values decompose the total RL gain across roles, while Möbius interaction terms distinguish standalone role improvements from multi-role coupling. Applying CO-GRAFT to Search-R1 agents across Qwen2.5 and Llama-3.2 models (spanning two sizes, base and instruction-tuned initializations, GRPO and PPO optimizers, and NQ and HotpotQA datasets), we show that query generation never exceeds 15% of the total gain; instead, gains are governed by pre-RL answer validity, search retention, model scale, and fixed task-level search budgets, shifting credit from reasoning toward answer extraction in larger or well-formatted answer response checkpoints while smaller base models rely on reasoning–decision coupling.
- **Key innovations**:
  - Reward-agnostic causal attribution: jointly generate one trajectory with RL-trained and pre-RL policies; evaluate all 2⁴=16 role assignments without retraining.
  - Cooperative-game decomposition: Shapley values decompose RL gains across the four roles; Möbius interaction terms separate standalone role effects from coupling.
  - Finding: search query generation never exceeds 15% of total gain; gains follow pre-RL answer validity, search retention, and scale — shifts credit toward answer extraction in larger models.

### 1.3 Reducing RSA-2048 Factoring Resources Below One Billion Toffolis via LLM-Driven Verifiable Quantum Compilation
- **Authors**: Xiaodi Li, Yuqing Wang, Xue Chen, Yang-Yang Tang, Linghui Chen, Tao Zhang
- **Institution / Company**: Not stated on arXiv metadata (best effort)
- **Published**: 2026-11-23 · quant-ph · [arXiv:2611.31158](https://arxiv.org/abs/2611.31158)
- **Abstract**: Modular exponentiation dominates the logical cost of factoring 2048-bit RSA integers (RSA-2048) with Shor's algorithm. Recent approaches based on approximate residue number systems (RNS) sharply reduce the required logical qubits, yet still demand billions of Toffoli gates. Optimizing these circuits is difficult because shared ancilla qubits and measurement-based uncomputation tightly couple the arithmetic stages, while rare overflows in compressed registers occur too infrequently for random simulation to detect. Here we use large language model (LLM)-driven search to redesign the RNS pipeline across stages and build a deterministic compiler that produces a Pareto frontier of RSA-2048 circuits. We bound rare overflow probabilities analytically and verify the resulting elementary gate sequences across all constituent RNS primes on representative circuits. Relative to Gidney's 2025 baseline under matched adder accounting, our frontier cuts the minimum qubit-Toffoli product by 70.1% and lowers expected factoring Toffolis by up to 78.6% at matched accumulator precision, bringing RSA-2048 factoring below one billion Toffolis for the first time.
- **Key innovations**:
  - LLM-driven redesign of the RNS pipeline + deterministic compiler emitting a Pareto frontier of RSA-2048 circuits.
  - Analytic bounding of rare register overflows; verification of gate sequences across all RNS primes.
  - First RSA-2048 factoring below 1B Toffolis: min qubit-Toffoli product down 70.1%.

---

## 2. Recommendation

### 2.1 Needwise: Generation-Free Conversational Recommendation from Need-Level Typed Decisions
- **Authors**: Sungchul Kim, Weixiao Huang, Mekala Raja Sekhar Reddy, Amrutha Srinivasan
- **Institution / Company**: Not stated on arXiv metadata (best effort)
- **Published**: 2026-11-23 · cs.AI · [arXiv:2611.31175](https://arxiv.org/abs/2611.31175)
- **Abstract**: Conversational recommenders must rank items against needs that catalogs record only in part, while users add, withdraw and reverse needs and switch between requests. LLM rankers re-read the dialogue at every turn: they are slow, and their ordering does not show which needs an item meets. We show that a conversational recommender can be built from typed decisions instead: named questions over fixed options, answered with option probabilities rather than generated text. On each turn, one typed request maps the message onto the catalog's fields, keeps what no field expresses in the user's words, and decides how the turn changes each earlier need. Needwise then ranks candidates must-first: the needs on the kind of item, its place and its price form a tier, and within it one holistic decision and need-level verdicts (supported, contradicted or unknown) are combined with equal weight (Needwise-HF). With the graded attributes withheld from the records, so that needs must be inferred from names, descriptions and reviews, Needwise-HF ranks Google Local requests significantly better than GPT-6 Sol (0.383 against 0.343 nDCG@10) and is not significantly different from the strongest LLM ranker on Google Local and Yelp; these comparisons keep their sign under every treatment of unrecorded attributes we test. It costs a fraction of GPT-6 Sol's API price and answers in 2.5 s at the median on Google Local, against 5.6 s for GPT-6 Sol. In conversations, the typed state keeps the ranking across switches and returns, but it recognizes only 19–27% of withdrawn needs.
- **Key innovations**:
  - Generation-free conversational recsys: typed named questions over fixed options; per-turn typed request maps message → catalog fields and updates needs.
  - Must-first tier ranking + equal-weight need-level verdicts (supported/contradicted/unknown) (Needwise-HF).
  - Results: nDCG@10 0.383 vs GPT-6 Sol 0.343 on Google Local (significant), parity on Yelp; ~2.3× faster and ~free vs LLM rankers.

### 2.2 From Head to Tail: LLM-Augmented Sequential Recommendation and Trade-off Optimization
- **Authors**: Adeep Hande, Shaghayegh Agah, Neeraj Sharma, Karina Halevy, Sardar Hamidian
- **Institution / Company**: Not stated on arXiv metadata (best effort)
- **Published**: 2026-11-23 · cs.IR/cs.AI · Accepted at GRAIL 2026 (held at CIKM 2026) · [arXiv:2611.31052](https://arxiv.org/abs/2611.31052)
- **Abstract**: Recommender systems exhibit popularity bias, often under-serving long-tail and cold-start items with sparse interaction data. We propose a group-specific data augmentation approach that leverages LLMs to generate synthetic interactions, formulated as a constrained optimization problem, maximizing group-specific NDCG@20 and coverage while bounding overall NDCG@20 degradation within an acceptable threshold. Items are partitioned by interaction frequency to find the optimal augmentation strategy for each group. We further study combining the augmentation across groups simultaneously and find that while individual optimal strategies navigate the multi-group augmentation design, they are not simply additive. We further ablate on the LLM-based augmentation itself, comparing LLM scales, augmentation configuration under token constraints, finding that augmentation quality scales with contextual richness, albeit at a proportionally higher cost. Experiments with SASRec demonstrate the effectiveness of the proposed approach, achieving over 100% and 60% improvement in group-specific NDCG@20 for extreme and regular long-tail items, respectively, on our industrial dataset, and 40%, 25% for MovieLens-32M, while increasing their coverage without significant overall degradation.
- **Key innovations**:
  - Group-specific LLM-generated synthetic interactions as a constrained optimization (max group NDCG@20 + coverage, bound on global NDCG@20 degradation).
  - SASRec gains: +100%/+60% (extreme/regular long-tail) on industrial dataset, +40%/+25% on MovieLens-32M, with increased coverage.
  - Study of additive vs non-additive multi-group augmentation; LLM-scale/token-budget ablation for augmentation quality.

### 2.3 MARS Technical Report
- **Authors**: Tong Liu, Chaoqun Hou, Longxiang Xiong, Junhong Lou, Jiaqi Zheng, Qixin Li, Zixin Zhao, Yong Duan, Xiannian Hu, Fengze Jiang, Yu Zhu, Cheng Guo, Xinyuan Qi, Zi Zhuang, Ping Liu, Lv Shao, Zongwei Wang
- **Institution / Company**: Not stated on arXiv metadata (best effort — best context: Taobao production context per paper text)
- **Published**: 2026-11-18 · cs.IR · [arXiv:2611.24006](https://arxiv.org/abs/2611.24006)
- **Abstract**: Modern industrial recommender systems use multi-stage cascades--retrieval, pre-ranking, ranking, and re-ranking--to narrow millions of candidates to a personalized list. While each stage deploys sophisticated models, pipeline-level decisions on channel activation, quotas, model selection, and score fusion remain engineer-tuned and user-agnostic within each scenario. This report presents MARS (Multi-stage Agentic Recommendation System), extending personalization from individual-stage predictions to full pipeline orchestration. A near-line agent built on fine-tuned Qwen3-0.6B generates per-user configurations--a seven-dimensional action covering pipeline mode, retrieval quotas, model selection, fusion weights, and reranker settings--from a constrained action space. Configurations are validated, cached, and consumed asynchronously; the cascade never waits for LLM inference. Schema checks, fallbacks, and a kill switch ensure serving safety. The policy is trained in three stages: Confidence-aware SFT distills schema-valid generation from a teacher model; Format-Anchored Preference Optimization (FAPO) learns action preferences via ActionMask with posterior weighting; Group Relative Policy Optimization (GRPO) refines the policy through Sandbox replay with a frozen reward model, without exposing exploratory actions to live traffic. Two-week A/B tests across five Taobao scenarios with over ten million daily users show positive gains on all key metrics. The largest reach +5.22% V2P and +7.34% GMV, with positive CTR lifts on both click surfaces. About 20% of requests use a lightweight Minimal mode, and deployment shows 12 ms lower mean serving latency versus production.
- **Key innovations**:
  - MARS: full-pipeline personalization via a near-line Qwen3-0.6B agent emitting 7-dim per-user pipeline configs; validated/cached asynchronously; kill switch + schema checks.
  - Training stack: SFT distillation → FAPO (ActionMask + posterior weighting) → GRPO via Sandbox replay without live-traffic exploration.
  - A/B (5 Taobao scenarios, >10M dau, 2 weeks): reach +5.22%, GMV +7.34%.

---

## 3. Advertising

### 3.1 Ads for Agents: Measuring Ad-Serving MCP Servers
- **Authors**: Shahrooz Pouryousef, Sohini Chakraborty, Ali Montazer, Muoi Tran
- **Institution / Company**: Not stated on arXiv metadata (best effort)
- **Published**: 2026-11-21 · cs.CR · [arXiv:2611.28911](https://arxiv.org/abs/2611.28911)
- **Abstract**: AI agents call external tools through protocols such as the Model Context Protocol (MCP). Some MCP servers return paid advertisements (ads) into the model's context. The model then decides whether these ads and their disclosures reach the user. We trace these ads from their sources to the agent's tool results across public MCP servers and packages. We find the servers through their public traces in ad networks, package registries, certificate logs, hostnames, MCP directories, and GitHub configurations. We then query the ad-serving servers with read-only requests and inspect their ad links. Ads appear on only 0.57% of 101,363 open MCP endpoints and 0.04% of 122,656 local MCP packages. Although 173 ad networks target agents, operators insert the ads themselves on about half of the 226 ad-returning servers. Nearly all ad-serving packages likewise carry the operator's own affiliate identifier. While ads adapt to the topic and intent of the query, their disclosure stays fixed within each tool. Only 9.3% of the ads carry an explicit sponsored label. Most ad links also hide their destinations. Since operators insert most ads themselves and label them inconsistently, we propose a per-item ad annotation in MCP results. Clients can show this annotation to the user independently of the model's answer.
- **Key innovations**:
  - End-to-end trace of agent-served ads: 101k public MCP endpoints / 122k local packages audited.
  - Finding: only 0.57% (endpoints) and 0.04% (local packages) return ads; operators insert ads on ~half of ad-serving servers; affiliate identifiers leaked in nearly all.
  - Proposal: per-item ad annotation in MCP tool results, client-displayable independently of the model's answer.

### 3.2 Iterative Scarcity-Guided Exploration: Bootstrapping Generative Auto-bidding from Narrow Support
- **Authors**: Qingmao Yao, Guangzheng Hu, Yusen Huo, Zhilin Zhang, Chuan Yu, Jian Xu, Xu Chu, Bo Zheng, Xiaotie Deng
- **Institution / Company**: Not stated on arXiv metadata (best effort — code linked: github.com/alimama-tech/ISGE)
- **Published**: 2026-11-19 · cs.LG · Accepted at NeurIPS 2026 (poster) · [arXiv:2611.26060](https://arxiv.org/abs/2611.26060)
- **Abstract**: Auto-bidding is a core algorithmic component in online advertising auctions. In practical cold-start settings, iterative training is commonly used to compensate for low-quality, narrowly supported historical data. Unfortunately, in iterative training, representative diffusion-based AI-Generated Bidding (AIGB) methods fail to sustain extrapolation beyond the narrow data support and stagnate at a suboptimal level. In this paper, we theoretically attribute this stagnation to Signal-to-Noise Ratio (SNR) collapse: the weak radial return signal is overwhelmed by a curvature-induced penalty. To break this stagnation, we propose Iterative Scarcity-Guided Exploration (ISGE), which introduces a guidance handoff: as the return signal collapses, scarcity subsequently takes over as an exploratory signal to elevate the SNR above a critical threshold. Specifically, ISGE iteratively alternates between a Judger that assigns scarcity scores to trajectories and an Explorer that performs guided generation of high-scarcity and high-return trajectories, thereby bootstrapping from the narrow support with such self-generated trajectories. Extensive experiments on the industrial AuctionNet benchmark demonstrate that ISGE, starting from cold-start datasets, effectively surpasses the performance of the Full-Dataset baseline within three iterations. Code is available at https://github.com/alimama-tech/ISGE
- **Key innovations**:
  - ISGE: Judger/Explorer alternation; scarcity becomes an exploratory signal as SNR collapses; bootstraps beyond narrow support.
  - Empirical: ISGE reaches Full-Dataset performance within 3 iterations on AuctionNet (cold start).

---

## 4. Sequential Modeling

### 4.1 Adaptive Residual Modeling for Scenario Learning in Probabilistic Load Forecasting
- **Authors**: Jinbao Wang, Jun Liu, Shiliang Zhang, Xuehui Ma, Yushuai Li, Lin Yan
- **Institution / Company**: Not stated on arXiv metadata (best effort)
- **Published**: 2026-11-02 · eess.SY · [arXiv:2611.03049](https://arxiv.org/abs/2611.03049)
- **Abstract**: Uncertainties in weather, user behavior, and distributed energy production introduce significant variability into feeder power. Effective power system operations require both multi-horizon load forecasts and well-calibrated extreme quantiles for the forecast. Nevertheless, standard objectives that fit the full forecast distribution often underemphasize rare observations and extremes. Conversely, applying heavy tail-weighting in the distribution to capture these extremes can distort the underlying probability distribution. To address this issue, this paper proposes adaptive residual modeling for scenario learning (ARMSL), a two-stage framework. Particularly, Stage I in our framework sequentially models environmental response, history-dependent load patterns, persistent residual deviations, and the remaining innovations. Upon the modeling, we then generate joint active- and reactive-power scenarios with state-dependent dispersion. Stage II keeps the scenario model fixed and calibrates extreme marginal quantiles using a simple, channel-specific reference forecast (an anchor). Only outward deviations from this anchor are admitted, with their contribution determined by local calibration history and the current operating state. From our numerical simulations on FeederBW dataset, Stage I outperforms diffusion baselines in energy and variogram scores. Our complete framework achieves an active-power 0.99-quantile pinball loss of 0.1932 (a 30.08% to 85.33% reduction relative to three baselines) with 1.054% exceedance rate against a nominal 1%. From simulations on the Rolle dataset, we observe decreased losses by 5.39%--14.40% compared to the active-power-only anchor. Furthermore, the unchanged Stage I scenarios in the simulation yield a correlation of 0.953 between predicted and observed feeder event rates, with 90.0% of feeder errors falling within two percentage points.
- **Key innovations**:
  - ARMSL two-stage framework: Stage I sequentially models env response → history patterns → residuals → innovations; Stage II calibrates extreme quantiles against an anchor.
  - 0.99-quantile pinball loss down 30–85% vs baselines; event-rate correlation 0.953.

### 4.2 Query- and Candidate-Aware Long User Sequence Modeling for Sponsored Product Ranking in Search
- **Authors**: Dongyue Xie, Sergey Kolbin, Manavender Malgireddy, Iurii Shcherbak, Weixing Tang, Arushi Jain, Wanchen Shao, Kurt Zimmer, Raja Hafiz Affandi, Matt Lindsay
- **Institution / Company**: Not stated on arXiv metadata (best effort)
- **Published**: 2026-11-08 · stat.ML/cs.LG · Accepted to ACM RecSys 2026 Workshop on Context-Aware Recommender Systems (CARS) · [arXiv:2611.11675](https://arxiv.org/abs/2611.11675)
- **Abstract**: User sequence modeling is widely used in recommendation and advertising. Search ranking presents an additional challenge: the current query expresses immediate intent, while a candidate product determines which parts of a user's long-term history are relevant. We present a production sequence framework for sponsored-product ranking that augments recent behavior with two retrieval channels over long-term history: candidate-nearest-neighbor retrieval and query-nearest-neighbor retrieval. The selected actions are encoded together with dedicated query and candidate context tokens, while candidate-aware early fusion injects the candidate into every history token. Offline ablations show that dual retrieval improves major ranking metrics relative to the production baseline. In an online A/B test on sponsored-product search traffic, the model increased CTR, attributed conversion rate, and orders per impression.
- **Key innovations**:
  - Two retrieval channels (candidate-NN, query-NN) over long-term history + dedicated query/candidate context tokens + candidate-aware early fusion.
  - Online A/B on sponsored search: CTR, attributed conversion rate and orders/impression improved.

---

## 5. CTR

### 5.1 DNA: Unlocking Depth Scaling in CTR Models
- **Authors**: Caiyuan Li, Wenjie Wu, Yuheng Huang, Xiao Zhou, Silu Zhou, Ke Chen, Zinan Zhao, Xinrui Zeng, Hanmo Xu, Chaoqun Song, Hua Zong, Zongyuan Wu, Hongbin Zhou, Huimin Yi, Zhixuan Zhang, Dan Ou, Haihong Tang
- **Institution / Company**: Not stated on arXiv metadata (best effort — paper context: deployed on Taobao search)
- **Published**: 2026-11-19 · cs.IR · [arXiv:2611.25659](https://arxiv.org/abs/2611.25659)
- **Abstract**: Long user behavior sequences are among the strongest signals for click-through rate (CTR) prediction. Cross-attention makes these sequences practical for industrial ranking by keeping compute linear in sequence length. Yet the gains from stacking cross-attention layers taper off: on Taobao search, growing a cross-attention stack from 16 to 28 layers adds only 0.02 percentage points (pt) of AUC. We argue that the key-value side is the bottleneck. Each layer projects the same behavior sequence into keys and values, so adding depth gives the model more reads of a fixed sequence. We propose DNA (Dual-stream Nexus Attention), which lets the sequence itself evolve with depth. At each layer, the request representation (the search query, user features and scene) first reads the sequence. Each behavior token then attends to the updated request representation and uses what it reads to update itself, so the next layer reads a sequence shaped by the current request. The update runs once per request, all candidates share the resulting sequence, and both the reads and the update keep linear complexity in sequence length. At comparable forward FLOPs, DNA improves AUC over cross-attention stacks by 0.08 to 0.26 pt and keeps improving in the depth range where those stacks level off. DNA-4 is deployed in Taobao search. In an online A/B test against the production model, it improves CTR by 0.8% and GMV by 0.5%.
- **Key innovations**:
  - DNA (Dual-stream Nexus Attention): behavior sequence itself evolves with depth — request reads sequence, tokens update themselves, next layer reads the updated sequence.
  - Fix: removes the KV-side bottleneck; gains where cross-attention stacks saturate; linear complexity preserved.
  - DNA-4 deployed in Taobao search: A/B vs production: CTR +0.8%, GMV +0.5%.

### 5.2 X-split Argus: Learning Reusable History Tokens for Efficient CTR Prediction
- **Authors**: Alexander Ploshkin, Nikita Stepanov, Alexey Pismenny, Viacheslav Ovchinnikov, Nikolay Savushkin
- **Institution / Company**: Not stated on arXiv metadata (best effort)
- **Published**: 2026-11-18 · cs.IR · [arXiv:2611.24283](https://arxiv.org/abs/2611.24283)
- **Abstract**: Accurate click-through rate (CTR) prediction depends on user representations that capture both persistent preferences and recent intent, yet processing extensive behavioral histories for every ranking request is costly under production compute and latency constraints. We present X-split ARGUS, a framework for ad ranking whose history compressor and online ranker are trained end to end. The compressor encodes past interactions into a compact set of tokens that are computed offline and reused across candidates, while the online ranker scores ads through cross-attention to these tokens and representations of recent events. Training combines an autoregressive loss for click feedback with distillation of candidate-specific click logits from a larger teacher that scores each candidate using the uncompressed history. The number of compressed history tokens and the length of recent history can be adjusted to fit serving compute and latency budgets. Offline evaluation shows a 0.81% relative reduction in normalized entropy (NE) compared with the production baseline. Deployment in a large-scale real-time bidding system increases online inference cost by 15% relative to the production baseline. An online A/B test against this baseline yields relative gains of 4.65% in a business metric reflecting the monetary value of conversions generated for advertisers and 2.96% in clicks.
- **Key innovations**:
  - X-split ARGUS: offline-computed reusable history tokens + cross-attending ranker; end-to-end training with autoregressive click loss + teacher distillation.
  - Offline NE −0.81% vs production baseline; +2.96% clicks online (+4.65% advertiser-value metric).

---

## 6. Games

### 6.1 AlphaDefect: Expert-Level AI for Slay the Spire 2
- **Authors**: Qiyue Chen, Taian Yu, Junpei Komiyama, Haobo Huang
- **Institution / Company**: Not stated on arXiv metadata (best effort)
- **Published**: 2026-11-23 · cs.AI/stat.ML · [arXiv:2611.31076](https://arxiv.org/abs/2611.31076)
- **Abstract**: Slay the Spire 2 (STS2) is a single-player deck-building game that requires long-term planning under heavy randomness. We present AlphaDefect, an expert-level AI system for STS2: for each character, one network trained with proximal policy optimization (PPO) makes every decision of a run, in combat and outside it. At the highest difficulty, Ascension 10, on two versions of the game current in November 2026 and on test seeds not played in training, AlphaDefect wins 62–77% of runs across six characters with greedy play and 68–80% with test-time search, after 1.3 to 6.7 billion decisions of training per character; runs uploaded by human players of all levels are won 11–20% of the time at the same difficulty. The networks read the game as entity records that identify each card, relic and enemy through a learned embedding and attributes from the game data, together with consequences of public information computed by the engine. Ablations show how much the agent depends on this encoding: without these identities, the network did not win a single run, and without the computed consequences it won 8.3 points fewer. To our knowledge, AlphaDefect is the strongest publicly reported STS2 agent as of November 2026.
- **Key innovations**:
  - Per-character PPO networks for every STS2 decision (combat and outside); wins 62–77% of runs at Ascension 10 (greedy, 6 chars), 68–80% with test-time search.
  - Entity records + engine-computed public consequences encoding; ablations show identity info essential (0 wins w/o it).

### 6.2 GameDojo: Benchmarking Real-Time Interactive Agents in Video Games
- **Authors**: Kuan Zhang, Zhihao Yang, Yukun Chen, Xingyilang Yin, Mingyu Ouyang, Yue Su, Xiangnan Wu, Jiaming Li, Longze Chen, Run Luo, Zirong Chen, Lu Wang, Yiming Li
- **Institution / Company**: Not stated on arXiv metadata (best effort)
- **Published**: 2026-11-23 · cs.AI · [arXiv:2611.30771](https://arxiv.org/abs/2611.30771)
- **Abstract**: Interactive intelligence requires agents to act on observations and adapt to the consequences of actions. Studying these abilities calls for diverse, challenging tasks under controlled conditions. We introduce GameDojo, a controllable interactive gameplay benchmark of 120 boss encounters across 20 games for evaluating model capabilities, learning algorithms, and agent harnesses. Coding agents reconstruct the environments and write gameplay scripts, producing GameDojo-Data with 600 hours of gameplay trajectories. Experiments reveal substantial challenges for frontier models, especially in real-time interaction. Training on GameDojo-Data brings GameDojo-4B to frontier performance, with the strongest real-time performance. We also find joint training improves individual tasks, and learned policies transfer across bosses. Together, these findings establish GameDojo as a challenging and valuable interactive gameplay benchmark for the community. Project page: https://gamedojo-benchmark.github.io/ ; code: https://github.com/THUSI-Lab/GameDojo
- **Key innovations**:
  - GameDojo: benchmark of 120 boss encounters across 20 games; GameDojo-Data (600h of gameplay trajectories) produced by coding agents.
  - Frontier models lag significantly in real-time interactive play; GameDojo-4B reaches frontier performance after training (strongest real-time).

---

## Quick Takeaways

- **LLMs/post-training**: TipSweep transfers LR across block counts with precision-dependent scaling (k⁻¹ FP32 vs k⁻¹/² BF16); CO-GRAFT decomposes RL gains across search-agent roles (query-gen ≤ 15%); RSA-2048 factoring first brought below 1B Toffolis via LLM-driven circuit redesign.
- **Recommendation**: Needwise builds generation-free conversational recsys from typed decisions (0.383 nDCG@10 on Google Local); MARS personalizes whole pipelines via a near-line agent; "From Head to Tail" uses LLM-generated group-specific synthetic interactions for long-tail coverage (+40–100% on industrial and MovieLens-32M).
- **Advertising**: Ads-for-Agents maps agent ad flow on MCP endpoints/packages (0.57% return rate, affiliate leaks found); ISGE (Alibaba) bootstraps AIGB auto-bidding out of narrow cold-start support via a Judger/Explorer game.
- **Sequential modeling**: ARMSL (Nankai/CEIT) does sequential residual modeling + anchor-calibrated extreme quantiles for probabilistic load forecasting; Query- & Candidate-Aware long-sequence retrieval improves sponsored search ranking (A/B: CTR, orders/impression).
- **CTR/ad ranking**: DNA unlocks depth scaling (KV-side bottleneck fix; Taobao A/B: +0.8% CTR, +0.5% GMV); X-split Argus reuses compressed offline tokens (+2.96% clicks online).
- **Games**: AlphaDefect (pupu) wins 62–77% of STS2 runs at Ascension 10 on 6 characters; GameDojo (Tsinghua/ByteDance) establishes the real-time interactive gameplay benchmark.
