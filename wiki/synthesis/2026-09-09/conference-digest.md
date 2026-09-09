---
title: "Conference Digest: 2025-2026 Top ML/AI Venues (Sep Update)"
type: synthesis
created: 2026-09-09
updated: 2026-09-09
sources: []
tags: [conference-digest, ICML2026, AAAI2026, NeurIPS2025, ICLR2026, KDD2026, CVPR2026, ACL2026, EMNLP2025, SIGIR2026, WWW2026, CIKM2025, RecSys2025, recommendation, LLM, advertising, CTR, agent, generative-model, sequential-modeling, benchmark]
---

# Conference Digest: 2025-2026 Top ML/AI Venues

> Compiled 2026-09-09. Covers ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025, plus recent arXiv highlights in agents/code-execution/generative-models/benchmarks. Focus areas: recommendation, LLM-based recommendation, advertising & auto-bidding, CTR, games & RL, generative / sequential modeling, agent & benchmark research.
>
> This is the September follow-up to the [2026-07-27 digest](../2026-07-27/conference-digest.md). Papers featured in today's arXiv daily files (arxiv-daily / arxiv-ai-search / arxiv-paper-check, all 2609.xx) are intentionally excluded.

---

## 1. ICML 2026 (Seoul, July 6-11)

**Scale**: 6,634 accepted papers — largest ICML to date (new submissions + NeurIPS/ICLR carryovers). Seoul, South Korea, July 6-11.

### 1.1 Pretraining & Optimizer Advances

#### Stabilizing Native Low-Rank LLM Pretraining (Spectron)
- **Translation (CN)**: 稳定原生低秩 LLM 预训练（Spectron）
- **Authors**: Paul Janson, Edouard Oyallon, Eugene Belilovsky
- **Affiliation**: MILA / Université de Montréal
- **Venue**: ICML 2026
- **arXiv**: <https://arxiv.org/abs/2602.12429>
- **Abstract & Innovations**: Native low-rank pretraining (training the weight matrices directly in factorized form) is unstable for deep LLMs. Spectron introduces a spectral normalization scheme on the factors that bounds the effective operator norm and stabilizes training, letting a low-rank LLM match full-rank quality at a fraction of the parameter count. Demonstration across decoder-only LMs at multiple scales.
- **Comparison**: Contrasts with the common LoRA-style "pretrain full-rank, then compress" approach; Spectron goes the other direction (train low-rank from scratch) and shows it is viable once spectral stability is imposed.

#### Direct Low-Rank Diffusion Pretraining
- **Venue**: ICML 2026
- **Abstract & Innovations**: Applies native low-rank training to diffusion backbones (not just autoregressive LLMs), showing the same spectral-stability recipe transfers to U-Net and DiT-style architectures, with measured training-time FLOP and memory savings.
- **Comparison**: Suggests the low-rank paradigm is architecture-agnostic, not LLM-specific.

### 1.2 LLM-Based Recommendation

#### Principled Synthetic Data Enables the First Scaling Laws for LLMs in Recommendation (Meta AI)
- **Venue**: ICML 2026
- **arXiv**: <https://arxiv.org/abs/2602.07298>
- **Abstract & Innovations**: Attributes the absence of scaling laws in LLM4Rec to noise/bias/incompleteness in raw interaction logs. Proposes a hierarchical synthetic-data curriculum (long-tail → multi-preference → reasoning-heavy) and empirically recovers stable power-law scaling of recommendation quality with model size and data quality.
- **Comparison**: Prior LLM4Rec scaling work treated raw logs as the scaling axis; this paper shows curated synthetic data is the enabling axis.

#### Mitigating Reward Hacking in LLM-based Recommendation
- **Affiliation**: USTC (University of Science and Technology of China)
- **Venue**: ICML 2026
- **Link**: <https://icml.cc/virtual/2026/poster/66384>
- **Abstract & Innovations**: Shows DPO-style pairwise objectives in LLM4Rec can improve the training metric while leaving ranking quality unchanged. Identifies "epsilon-insensitive regions" in the gradient space where pairwise updates do not change the ordering between positive and unsampled negatives, and offers diagnostic procedures to detect reward hacking before deployment.
- **Comparison**: Directly challenges the default assumption that pairwise preference loss correlates with ranking improvement — the same failure mode documented in RLHF reward hacking, now characterized for the ranking setting.

#### T-POP: Test-Time Personalization with Online Preference Feedback
- **Venue**: ICML 2026
- **Link**: <https://icml.cc/virtual/2026/poster/66384>
- **Abstract & Innovations**: Keeps the LLM frozen and learns a personalized per-user reward function on the fly from pairwise preference feedback, tackling cold-start personalization without any parameter updates.
- **Comparison**: Separates personalization from model training — orthogonal to DPO/SFT approaches that bake preferences into weights.

### 1.3 Advertising, Auctions & Auto-Bidding

#### Autobidding Auctions with LLM-Powered Creatives
- **Venue**: ICML 2026
- **Link**: <https://icml.cc/virtual/2026/poster/60993>
- **Abstract & Innovations**: Models the ad platform as a Stackelberg leader and budget-constrained autobidders as followers. The platform's decision variable expands from pCTR/pCVR to whether to invoke on-the-fly LLM creative generation, explicitly budgeting LLM inference cost into the mechanism. Characterizes when generative creatives improve welfare vs. merely shifting spend.
- **Comparison**: Earlier auction theory treated creatives as static; this integrates GenAI inference cost into mechanism design.

#### Model Monotonicity in Autobidding Auctions (Uber)
- **Venue**: ICML 2026
- **Link**: <https://icml.cc/virtual/2026/poster/60993>
- **Abstract & Innovations**: Proves that improved pCTR/pCVR predictions do not monotonically improve revenue, welfare, or liquid welfare under autobidding. Introduces a cluster-refinement notion of model improvement and analyzes non-monotonicity across auction rules and autobidder types.
- **Comparison**: Formalizes a suspicion long held by practitioners (a better CTR model can lose money in auctions) and gives the theory for when it happens.

#### Generative Auto-Bidding Meets Hierarchical Reasoning (LBM)
- **Cross-reference**: See full entry under WWW 2026 (§9) — the Kuaishou/NTU hierarchical LLM auto-bidding model; the ICML community published the companion sequence-modeling analysis of generative bid policies.

### 1.4 CTR & Sequential Modeling

#### From Scaling to Structured Expressivity: Rethinking Transformers for CTR Prediction (FAT)
- **Cross-reference**: Detailed under KDD 2026 (§6). The ICML 2026 version frames the same Field-Aware Transformer w.r.t. long-context budget allocation in lifelong user sequences.

---

## 2. AAAI 2026

### 2.1 LLM-Based Recommendation

#### TWiCE-Rec: Rationale-Aware LLM-based Recommender with RL from Collaborative Signals
- **Translation (CN)**: TWiCE-Rec：基于协作信号强化学习的理由感知 LLM 推荐器
- **Venue**: AAAI 2026
- **Link**: <https://ojs.aaai.org/index.php/AAAI/article/view/38590>
- **Abstract & Innovations**: Adds a rationale (reasoning) head to an LLM recommender and trains it with reinforcement learning using ranks derived from collaborative signals as the reward — not just next-item likelihood. The model must both recommend and justify; RL from collaborative ranks closes the gap between language-model optimization and ranking goal.
- **Comparison**: Steps beyond "generate-then-rank" pipelines (like Align³GR-style SFT+DPO) by putting rationale quality under the same RL objective as ranking quality. Relevance: it is another datapoint in the "LLM4Rec + RL" surge seen at ICML/AAAI 2026.

#### BEAT: Behavior Tokens Speak Louder than Words
- **Cross-reference**: Covered in the July digest (§2.1). Re-confirmed as a strong AAAI 2026 paper — behavior-aware tokenization for LLM4Rec (Kuaishou lineage).

---

## 3. NeurIPS 2025 (San Diego, Dec 2-7)

### 3.1 Best Paper Awards (7 winners incl. 1 D&B track)

#### Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)
- **Translation (CN)**: 人工蜂群思维：语言模型的开放式同质化（及其延伸）
- **Venue**: NeurIPS 2025 Best Paper
- **Abstract & Innovations**: Shows that models tuned on the same corpus converge to the same effective "homogenized" behavior regardless of architecture — an open-ended but convergent process they dub the "artificial hivemind." Analyzes the phenomenon mathematically and empirically across pretraining runs.
- **Comparison**: Contrasts with the common assumption that architecture diversity guarantees behavioral diversity; the paper argues homogenization dominates across scales.

#### Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free
- **Translation (CN)**: 门控注意力：非线性、稀疏性与免 Attention Sink
- **Authors**: Zihan Qiu et al. (incl. Junyang Lin, Alibaba)
- **Venue**: NeurIPS 2025 Best Paper
- **Abstract & Innovations**: Inserting a learned sigmoid gate after softmax(QKᵀ) — the "gated attention" trick — provides non-linearity and implicit sparsity, eliminates attention sinks, and stabilizes long-context training. Now the basis of the Qwen3-Next attention design.
- **Comparison**: A tiny architectural change fixing a family of known pathologies (attention sink, over-smoothing); shown to improve long-context retention over plain softmax attention. In production in Qwen3-Next.

#### 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities
- **Translation (CN)**: 一千层网络用于自监督强化学习：深度规模带来新目标达成能力
- **Venue**: NeurIPS 2025 Best Paper
- **Abstract & Innovations**: Trains 1000+ layer residual networks for self-supervised RL (successor-style via contrastive/self-prediction). Scaling depth alone unlocks temporally distant goal-reaching that shallow networks cannot reach, offering an alternative axis to compute scaling.
- **Comparison**: Reframes the "shallow RL nets suffice" folk theorem; depth, not just width, is a scaling degree of freedom for planning/reaching.

#### Why Diffusion Models Don't Memorize
- **Translation (CN)**: 为什么扩散模型不记忆
- **Venue**: NeurIPS 2025 Best Paper
- **Abstract & Innovations**: Gives a rigorous account of why diffusion models memorize far less than GANs/likelihood models at equal capacity — memorization is controlled by the score-matching objective's noise floor, not merely capacity. Provides bounds relating noise level schedules to near-duplicate generation.
- **Comparison**: Explains a widely observed but unexplained phenomenon; has direct privacy implications for generative media pipelines.

### 3.2 Runner-Up / Honorable Mentions
- **Long-Context Training Dynamics**: multiple accepted works on next-token-prediction curriculum vs. compute-optimal long-context budgets (relevant to the "contexting vs pretraining" debate).
- **Self-Play RL for Agents**: the emergent "self-play + verifiable rewards" family of papers pre-dating DeepSeek-R1-style recipes formalized in 2026.

---

## 4. ICLR 2026 (Rio de Janeiro, April 23-27)

**Scale**: 5,355 accepted papers (27.4% acceptance). Rio de Janeiro, Brazil, Apr 23-27.

**Review-Crisis data point (context)**: community audits found ~45% of reviews leaked reviewer identities and ~21% contained AI-generated text; the PC responded with strengthened anonymity and attribution pre-checks. Flagged as a reliability concern for 2026 venue metrics.

### 4.1 Oral Papers / Highlights

#### Common Corpus
- **Type**: Open pretraining-data release (2.5T+ tokens public-domain corpus).
- **Significance**: The largest fully open pretraining corpus; used by multiple 2026 "fully open LLMs" as the data backbone. Established the "data openness" tiered benchmark (data → code → weights → logs).

#### Q-RAG: Query-based Retrieval-Augmented Generation
- **Significance**: Replaces chunk-level retrieval with query-level generation of target structures, improving recall on multi-hop and tabular questions over standard RAG pipelines. Bridge topic to recommendation-style "query → structured item" retrieval.

#### MedAgentGym
- **Type**: Medical multi-agent benchmark/environment.
- **Significance**: Gym for training/evaluating medical agent teams with an RL verifier for tool-grounded claims; a reference setup for safety-critical agent RL in 2026.

#### DIVA-GRPO
- **Significance**: Distributional/robust variant of the group-relative policy-optimization recipe; targets reward variance collapse in verifier-driven RL for reasoning models.

#### R-Horizon
- **Significance**: Extends GRPO-style RL over longer horizons (reasoning + acting across many turns), addressing credit assignment across tool-call chains — a key stepping stone for agentic RL.

#### Kimi-Dev
- **Type**: Agentic coding dataset/benchmark from Moonshot AI, in the "real-repo software engineering" meta (SWE-bench lineage) but over full feature-development cycles rather than single issues.

#### CLAUSE
- **Significance**: Clause-level / decompositional supervision method, revisited in 2026 as a strong SFT alternative to over-long "CoT dump" tuning.

#### FingerTip 20K
- **Type**: Large-scale fine-grained fingertip-tracking dataset/benchmark; notable for pushing 3D hand interaction (games/interfaces) scale.

### 4.2 Trend Notes
- **Open-science constellation**: Common Corpus + fully-open LLM releases make the "open data → open weights" pipeline the dominant ICLR 2026 narrative.
- **RL in the loop**: DIVA-GRPO, R-Horizon and MedAgentGym all place RL (not just SFT) at the center of reasoning/agent training, mirroring the industrial DeepSeek-R1 lineage.

---

## 5. CVPR 2026

**Scale**: 4,090 accepted papers.

### 5.1 Highlights
- **Storyboard Generation**: a new theme — turning scripts/plots into consistent multi-shot storyboards; several best-paper-nominated works tackle cross-shot character consistency.
- **Scone: Subject-Driven Image Generation** (Wang et al.) — single/few reference images drive new-scene subject rendering, pushing beyond StyleGAN-era "subject fidelity" to text-driven, layout-aware generation.
- **SconeEval** — the associated evaluation benchmark for subject-driven generation (identity preservation × prompt alignment), indicating benchmarked evaluation is catching up to the task.
- **FoleyDirector: Video-to-Audio (V2A)** — generates synchronized Foley audio from silent video with per-affordance control; relevant to multimodal generative modeling (also connected to EMNLP/ACL multimodal papers).

---

## 6. KDD 2026 (Jeju Island, August 9-13)

### 6.1 CTR & Transformers

#### From Scaling to Structured Expressivity: Rethinking Transformers for CTR Prediction (FAT / Field-Aware Transformer)
- **Translation (CN)**: 从扩展到结构化表达力：重思用于 CTR 预测的 Transformer
- **Affiliation**: Alibaba-affiliated group
- **Venue**: KDD 2026
- **arXiv**: <https://arxiv.org/abs/2511.12081>
- **Abstract & Innovations**: Argues that naive Transformer scaling for CTR (billions of raw feature tokens) is compute-inefficient; proposes the Field-Aware Transformer (FAT) that 
  (a) compresses feature fields into fixed slots so attention cost stops scaling with sequence length, and 
  (b) restores structured expressivity with explicit field-level interactions rather than unconstrained token mixing. Reports outperformance over HSTU-class industrial baselines on click prediction under the same compute budget, with analysis of attention-sink-like token-massing issues in long user sequences.
- **Comparison**: Positions FAT as the "structured" middle ground between DLRM-era field aggregation and fully flexible HSTU/transformer tokenization; challenges the "just scale tokens longer" doctrine on CTR.

### 6.2 Recommendation & Generative
- **SIGIR/KDD overlap**: multiple 2026 CTR papers converge on lifelong-sequence compression (C-Former lineage, see CIKM §12) — the "compress behavior, not scale tokens" theme is now the KDD 2026 CTR consensus.

---

## 7. ACL 2026 (San Diego, July 2-7)

**Scale**: 2,296 main-conference papers + 2,163 Findings.

### 7.1 Best Paper / Outstanding
#### From Form to Function: Default Knowledge as a Resource-Rational Encoding
- **Translation (CN)**: 从形式到功能：作为资源理性编码的默认知识
- **Authors**: Weijie Xu, Brian Dillon, Richard Futrell
- **Affiliation**: MIT Linguistics (Futrell lab)
- **Venue**: ACL 2026 Best Paper
- **Abstract & Innovations**: Explains memory-efficient linguistic encoding via a resource-rational (rate-distortion) model: the grammar "defaults" to compressed/heuristic forms when the communicative channel is under pressure. Links NLP/LLM token-efficiency results to psycholinguistics, giving a theoretical account of why language regularization happens at scale.
- **Comparison**: Bridges optimal-transport/rate-distortion theory and grammatical regularity; relevant to tokenizer/representation design discussions in LLM work.

### 7.2 Agents & Reasoning Dominance
- The accepted-paper distribution confirms LLM reasoning + LLM agents as the largest ACL 2026 track, consistent with EMNLP 2025 and the 2026 arXiv waves. Representative agentic lines:
  - **OctoTools**-style octagonal tool orchestration for multi-tool planning.
  - **Discover-and-Prove**: models generate their own lemma/corollary structure during math reasoning ("prove as you go, then exploit"), cutting error propagation vs. flat CoT.
  - **MARCH** and **KARL**: dialogue-state / recall-aware persona consistency; typical memory-augmented agent stacks now standard in ACL findings.
  - **Memory-R1**: applies GRPO-style RL to memory-augmented conversations — evidence that RL recipes (NeurIPS/ICLR 2026) reached the conversational-agent track.

---

## 8. EMNLP 2025 (Suzhou, China)

### 8.1 Awards (from Dec 2025 ceremony)
- **Best Resource Paper**: *Autoformalization in the Wild* — a large, noisy web-scale dataset of informal→formal mathematically-flavored text pairs, plus a benchmark to measure autoformalization progress; important substrate for proof-adjacent LLM training.
- **Outstanding Papers** (selection):
  - **LingGym**: a linguistically-grounded reasoning gym (type-logical/formal semantics tasks) for testing LLM reasoning beyond math/code.
  - **Mind the Value-Action Gap**: diagnosis of LLM alignment where stated values and actual behavior diverge; measurable gap metric for RLAIF-style pipelines.
  - **DiscoSG**: discourse-aware scene graph generation, demonstrating that discourse structure (not just local grounding) improves SG quality.
  - **Generative or Discriminative?**: a careful study flipping between generative and discriminative objectives for the same NLP tasks, with cost/benefit analysis now widely cited in the 2026 generative-recommendation debates (see §13 trend notes).
  - **Measuring Chain-of-Thought Faithfulness by Unlearning Reasoning Steps**: intervenes on CoT traces (unlearning single reasoning steps) to check whether final answers actually depend on them; large fraction of "unfaithful" CoT turns — a widely cited operationalization of CoT faithfulness.
  - **MiCRo**: incremental cognitive-readiness modeling for LLM test-taking.

### 8.2 Code-Execution Surrogates (relevant to code-execution focus)
#### SURGE: Surrogate Benchmark for Code Execution
- **Venue**: EMNLP 2025 (main)
- **Abstract & Innovations**: Introduces a cheap *surrogate* benchmark that approximates true code-execution outcomes without running arbitrary sandboxes — measuring execution-faithfulness (does the model's claimed execution trace match a real interpreter?) with controllable difficulty.
- **Comparison**: Connects to the live-code-execution debate: sandboxed runtimes give ground truth but at heavy cost; SURGE gives a fast proxy useful for comparing executor-specialized models at scale.

---

## 9. SIGIR 2026 (Melbourne, July 20-24)

### 9.1 Accepted-Papers Standouts
#### NeurPIU
- **Area**: Pre-training and Injected-User (PIU) modeling — injecting user states into pretrained recommender backbones, layered on generative/LLM pipelines.
#### MLLM with Adaptive Preference Optimization for Sequential Recommendation
- **Translation (CN)**: 面向序列推荐的自适应偏好优化多模态 LLM
- **Authors**: Yu Wang et al.
- **Translation note**: adaptive PO replaces static single-step preference optimization; adjusts optimization strength per session difficulty/user type.
#### DCGL / NeuCon-ICE / BEAR
- **Areas**: DCGL (diffusion-based collaborative graph learning); NeuCon-ICE (neural network + item co-embeddings for cold/long-tail); BEAR (balanced/expressive alignment regularizer for LLM-rec embeddings). These pick up the "behavioral alignment" subfield (LLM embeddings ↔ collaborative embeddings) mainstreamed by RLMRec/SAID/LLM-ESR.
#### Fusion & Alignment for Tail-Item Sequential Recommendation
- **Addresses**: long-tail items where pure behavior signals are too sparse; fuses LLM semantics with behavior signals via adaptive gating.
#### LLM-EDT: Cross-Domain Sequential Recommendation
- **Authors**: Ziwei Liu et al.
- **Abstract & Innovations**: EDT = evidence-decoupled training; separates cross-domain evidence into transferable vs. domain-specific, addressing the "which knowledge should transfer?" question in cross-domain sequential rec.
#### TM-Bench
- **Type**: benchmark for tail-item / long-tail recommendation, standardizing tail metrics in addition to head-dominated NDCG/Recall.

**Scale**: 113 full papers + 45 short papers.

---

## 10. WWW 2026 (Dubai, April 13-17)

### 10.1 Thinking-Based & Agentic Recommendation
#### ThinkRec: Thinking-based Recommendation via LLM
- **Translation (CN)**: ThinkRec：基于"思考"的 LLM 推荐
- **Venue**: WWW 2026
- **Link**: <https://dl.acm.org/doi/10.1145/3774904.3792070> | Code: <https://github.com/Yu-Qi-hang/ThinkRec>
- **Abstract & Innovations**: Moves LLM4Rec from the System-1 (intuition, superficial feature matching) to System-2 (rational) regime: (1) a *thinking activation* mechanism injects synthetic reasoning traces so recommendations resemble CoT; (2) an *instance-wise expert fusion* mechanism assigns per-user weights to expert models, adapting the reasoning path to the user. Reports significant accuracy + interpretability gains over baselines on web user-behavior datasets. Code released.
- **Comparison**: Positions itself against the "System 1-style" LLM4Rec family (ReLLa, R²ec, Reinforced Latent Reasoning all cited as prior). Pairs naturally with Kuaishou's Align³GR (RL-aligned reasoning) — thinking + RL is the 2026 intersection point.

#### MATRAG: Multi-Agent Transparent RAG for Explainable Recommendations
- **Venue**: WWW 2026 (Companion)
- **arXiv**: <https://doi.org/10.48550/arxiv.2604.20848>
- **Abstract & Innovations**: Four specialized agents (User Modeling, Item Analysis, Reasoning, Explanation) over item knowledge graphs, plus a transparency-scoring module quantifying faithfulness/coherence/personalization of explanations. Reports +12.8% Hit Rate, +15.3% NDCG vs. leading baselines, and 87.4% human-rated helpful/trustworthy explanations.
- **Comparison**: A representative of the "explainable agentic recommender" theme that emerges at WWW 2026; complements ThinkRec (thinking) with explicit evidence-tracing (RAG over KG).

#### When Ads Become Profiles: Uncovering the Invisible Risk of Web Advertising at Scale with LLMs
- **Translation (CN)**: 当广告成为画像：用 LLM 揭示大规模网络广告的隐形风险
- **Venue**: WWW 2026
- **arXiv**: <https://arxiv.org/html/2509.18874v3>
- **Abstract & Innovations**: Uses off-the-shelf multimodal LLMs as adversarial inference engines to reconstruct private attributes purely from ad exposure streams — on a longitudinal dataset of 435,000+ Facebook ad impressions from 891 users. LLMs reconstruct party preference, employment status, education level; outperforming census-based priors and matching/exceeding human social perception at 223× lower cost and 52× faster pace. Shows actionable profiling within short observation windows — a systemic privacy vulnerability of the ad ecosystem.
- **Comparison**: Inverts the usual recsys direction: instead of using ads to serve users, it shows adversaries can use ad signals to profile users — the counter-side of every LLM4Rec paper in this digest.

### 10.2 Item-Aware & Generative Representations
#### IAM: From Token to Item — Enhancing LLMs for Recommendation via Item-aware Attention
- **Translation (CN)**: 从 Token 到 Item：面向推荐的 Item-Aware 注意力
- **Venue**: WWW 2026
- **arXiv**: <https://arxiv.org/html/2603.19693v1>
- **Abstract & Innovations**: Criticizes LLM-based recommenders for modeling token–token relations while missing item-level collaborative structure. IAM adds dedicated attention layers distinguishing intra- vs inter-item token relations, consolidating items as independent units. Gains vs. strong baselines: +25.81% Prec@10 / +10.04% NDCG@10 on Grocery, +6.80%/+3.74% on Arts, +71.00%/+74.86% on Cellphones.
- **Comparison**: Where FAT (KDD 2026) restructures Transformers for CTR, IAM restructures attention inside LLMs for sequential recommendation — a symmetry worth tracking.

#### GenAIR: Generative Archetype-Grounded Item Representations for Sequential Recommendation
- **Translation (CN)**: GenAIR：原型的生成式 Item 表示用于序列推荐
- **Venue**: WWW 2026 (DOI 10.1145/3774904.3792587)
- **arXiv**: <https://arxiv.org/html/2606.11023v1>
- **Abstract & Innovations**: Uses LLMs to *generate archetypes* (target-audience-style profiles) from item metadata instead of relying on behavior bootstrap or frozen LLM embeddings; adds a *behavioral calibration* objective that grounds the generative representations in real interactions. Model-agnostic — works with GRU4Rec, BERT4Rec, SASRec.
- **Comparison**: Addresses the known weaknesses flagged for the LLM-embedding family (RLMRec weak w/o careful projection; LLM-Init/LLMEmb/AlphaFuse rely on static LLM semantic space). GenAIR is the "generate semantics, calibrate behavior" middle path.

### 10.3 Auto-Bidding
#### LBM: Hierarchical Large Auto-Bidding Model via Reasoning and Acting
- **Translation (CN)**: LBM：推理 + 执行的分层大规模自动出价模型
- **Authors**: Yewen Li, Zhiyi Lyu (Kuaishou / NTU), Peng Jiang, Qingpeng Cai, Fei Pan (Kuaishou), Bo An (NTU)
- **Venue**: WWW 2026 (DOI 10.1145/3774904.3792202)
- **arXiv**: <https://arxiv.org/abs/2603.05134> | Code: <https://github.com/yewen99/LBM-WWW26>
- **Abstract & Innovations**: Two-level design — high-level **LBM-Think** (LLM reasoning about auction state) + low-level **LBM-Act** (precise action generation). Contribution: (1) dual embedding mechanism fusing language + numerical modalities for language-guided training of LBM-Act; (2) **GQPO**, an offline reinforcement-fine-tuning method that suppresses LLM hallucination and improves decisions *without* simulation/online rollouts (unlike prior multi-turn LLM methods). Reports stronger generalization vs. generative/offline-RL baselines with a cheaper training loop.
- **Comparison**: This is the "generative backbone as bidder" industrial line (Generative Auto-Bidding GAEB, Value-Guided Explorations 2025 → LBM 2026); GQPO extends GRPO-style recipes to the bidding domain offline — a concrete bridge between LLM RL (ICLR/NeurIPS 2026 §4) and computational advertising.

---

## 11. RecSys 2025

### 11.1 Notable Papers
#### Non-parametric Graph Convolution for Re-ranking in Recommendation Systems
- **Translation (CN)**: 推荐系统中用于重排的非参数图卷积
- **Authors**: Zhongyu Ouyang et al.
- **DOI**: <https://doi.org/10.1145/3705328.3748058>
- **Abstract & Innovations**: Applies non-parametric graph convolution at the re-ranking stage — propagating scores across a user/item graph built on the candidate beam without training extra parameters; empirically robust to re-ranking feedback loops.
- **Comparison**: A low-cost complement to the parametric re-ranking (permutation/autoregressive) literature; supports the "graph-informed second pass" pattern now common in 2026 CTR stacks.

### 11.2 Looking Ahead
- **RecSys 2026**: Minneapolis, MN, Sep 27 – Oct 1, 2026. CfP emphasizes multimodal/LLM integration and safety/fairness evaluations — consistent with the trends in this digest.

---

## 12. CIKM 2025 (Seoul, November 10-14)

### 12.1 Industrial-Scale Generative Recommendation
#### Industrial-Scale Generative Recommendation Framework in Meituan (Meituan GR / HSTU)
- **Translation (CN)**: 美团工业级生成式推荐框架
- **Authors**: Ruidong Han, Bin Yin, Shangyu Chen, He Jiang, Fei Jiang, Xiang Li, Chi Ma, Mincong Huang, Xiaoguang Li, Chunzhen Jing, Yueming Han, MengLei Zhou, Lei Yu, Chuan Liu, Wei Lin (Meituan)
- **Venue**: CIKM 2025 (Applied Research)
- **Abstract & Innovations**: A production generative recommender built on the HSTU architecture that *retains traditional DLRM features (incl. cross features)* — the exact thing naive generative rec (Semantic-ID tokenization) threw away. Shows that keeping engineered features + adding generative next-item decoding recovers the accuracy loss observed in first-gen generative rec at Meituan scale.
- **Comparison**: Directly answers the trade-off surfaced in earlier digests (generative rec accuracy dip vs. DLRM features). Together with Kuaishou GR4AD/OneRec, it cements "HSTU-class + DLRM features" as the industrial Gen-Rec template.

### 12.2 Lifelong Sequence Modeling (CTR)
#### C-Former: Transformers Are Good Clusterers for Lifelong User Behavior Sequence Modeling
- **Translation (CN)**: C-Former：Transformer 作为终身行为序列建模的聚类器
- **Authors**: Xingmei Wang, Shiyao Wang, Wuchao Li, Jiaxin Deng, Song Lu, Defu Lian, Guorui Zhou
- **Affiliation**: Alibaba / USTC lineage
- **Venue**: CIKM 2025
- **Abstract & Innovations**: Frames lifelong user sequences as a clustering problem: learns trainable "cluster queries" (attention queries as centroids) and shifts clustering from Euclidean distance to meaningful *semantic* distance in an end-to-end CTR objective. Compresses arbitrarily long histories into a bounded query set.
- **Comparison**: Core member of the lifelong-sequence compression family — the same theme as FAT (KDD 2026) and the "fixed-slot" designs now consensus at CTR tracks. (Note: "Transformers as Clusterers" also appears as a 2025 ICLR/NeurIPS meta-theme across NLP.)

### 12.3 Datasets & LLM-Rec Ecosystems
- **MicroLens** (Ni, Zhao, Xiangnan He, Yongfeng Zhang, Fajie Yuan et al.): large-scale content-driven micro-video recommendation dataset — fills the scarcity of public micro-video rec data.
- **LangPTune** (Gao, Zhou, Dai, Thorsten Joachims): first end-to-end framework to directly optimize LLM-generated *user profiles* as differentiable objects for recommendation — profile-as-parameter instead of profile-as-output.
- **DeepRec** (Zheng, Xiaolei Wang, Wayne Xin Zhao, Ji-Rong Wen et al.): autonomous multi-turn LLM↔TRM interaction for deep item-space exploration — LLMs *call* the recommender model repeatedly, not just score once.
- **Scenario-Wise Rec** (Xiaopeng Li, Xiangyu Zhao, Ruiming Tang et al.): multi-scenario recommendation benchmark — 6 public datasets + 12 baselines + training/evaluation pipeline.
- **SELF** (Pengyue Jia, Xiangyu Zhao, Huifeng Guo, Ruiming Tang et al.): surrogate-light feature selection with LLMs for deep rec.
- **Personalized Multi-Modal Alignment Encoding for CTR in WeChat** (Zheng, Gu, Yi, Wen, Chuan Chen): multimodal alignment encoding applied to WeChat CTR production data.
- **Twin-Flow Generative Ranking Network** (Hao Guo et al., Meituan): dual-flow generative ranking — a generative-rank output alongside the traditional listwise score at serving time.

---

## 13. Cross-Conference Trends

### Trend 1: LLM4Rec is Moving from Generation to "Thinking + RL"
ThinkRec (WWW), TWiCE-Rec (AAAI), Memory-R1 (ACL): the 2026 story is not "can LLMs recommend" but "can LLMs reason-then-recommend with RL-trained reasoning." EXCEPT the R2ce/Align3 families, every new entry adds a reasoning/rationale head + a collaboration/RL supervision signal. The plain SFT+DPO era is over.

### Trend 2: "Compress Sequences, Don't Scale Tokens" Wins CTR
FAT (KDD), C-Former (CIKM), item-aware attention (IAM, WWW), fixed-slot lifetime-sequence designs: the consensus is that naive tokenization of long user histories into attention is wrong. Structured compression + field/item-granular attention is the 2026 CTR architecture pattern.

### Trend 3: Generative Recommendation Is Now Industrialized With Features
Meituan GR (HSTU + DLRM features), plus Kuaishou GR4AD/OneRec: model families now prove you can keep traditional features, add generative decoding, and win online A/B. Purely tokenized generative rec has been revised.

### Trend 4: LLM RL Recipes Are Flowing Into Every Vertical
GQPO (WWW LBM), DIVA-GRPO / R-Horizon (ICLR), Memory-R1 (ACL), Align3-style progressive DPO (AAAI): GRPO-family + offline variants are the shared substrate of 2026 agentic/bidding/recommendation RL. NeurIPS reward-hacking analysis (ranking version) is the cautionary pair.

### Trend 5: Privacy as the Inverse of Personalization
"When Ads Become Profiles" (WWW) inverts the modeling axis: signals that make recsys good can make profiling attacks cheap (223× cheaper, 52× faster than human). Expect safety/fairness tracks (RecSys 2026 CfP already signals this) to pick this up.

### Trend 6: CoT Faithfulness Is Being Measured, Not Assumed
EMNLP 2025 "Unlearning Reasoning Steps" + ACL/ICLR 2026 reasoning papers: "thinking" (Trend 1) is only worth it if CoT traces are causally faithful; measurement methods are catching up to generation methods.

---

## Key Industrial Deployments at a Glance

| Paper | Company | Stage | Reported Gain |
|-------|---------|-------|---------------|
| Meituan GR (HSTU+features) | Meituan | Production (referenced at scale) | Accuracy recovery vs. feature-less Gen-Rec |
| LBM (GQPO) auto-bidder | Kuaishou / NTU | Online-adjacent validated | Generalization gain vs. generative/ORL baselines |
| ThinkRec | (academic, code released) | Paper + code | SOTA vs. System-1 LLM4Rec on web datasets |
| C-Former | Alibaba lineage | CTR stack | Lifelong sequence compression in production family |
| When Ads Become Profiles | (adversarial study) | Study | 223× cost / 52× time reduction for profiling |