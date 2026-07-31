---
title: "arXiv AI Research Scan — July 2026"
type: synthesis
created: 2026-07-30
updated: 2026-07-30
tags: [arxiv, survey, llm, recommendation, ctr, sequential-modeling, games, reinforcement-learning]
---

# arXiv AI Research Scan — July 2026

Curated papers submitted Jul 29–30, 2026 (plus notable earlier July submissions) across LLMs/agents/RL, recommendation/CTR/advertising, and sequential modeling/memory.

---

## Large Language Models, Agents & Multi-Agent Systems

### 1. SVR: Self-Verifying Refinement via Joint Verdict-Confidence Reinforcement Learning for Adaptive Test-Time Compute
- **Authors**: Hongyu Chen, Liang Lin, Guangrun Wang
- **Institution**: N/A
- **Abstract**: Oracle-free multi-turn RL framework that learns to use self-verification as a compute-control policy. At each turn the model emits a solution, a correctness verdict, and a confidence score; it stops when verdict=Correct and confidence exceeds threshold, otherwise refines using its own self-verification. Ground truth is used only in training rewards, never at inference.
- **Key Innovations**: Learned internal control signal for answer retention and adaptive test-time compute; on seven math benchmarks with Qwen3.5-2B achieves 0.563 macro accuracy in only 2.99 inference turns, beating fixed-budget oracle-guided baselines.
- **Link**: https://arxiv.org/abs/2607.28457

### 2. MANTA: Multi-Agent Network Topology Adaptation for Self-Evolving Multi-Agent Systems
- **Authors**: Mao-xun Huang, Jerry Wang, Yi-Cheng Lai, Zhengxin Zhang, Claire Cardie, Hen-Hsen Huang
- **Institution**: Cornell University et al.
- **Abstract**: Treats communication topology as an inference-time asset rather than a fixed design. MANTA initializes a task-conditioned topology from prior structural experience, monitors collaboration traces at deployment, and applies bounded structural updates (roles, links, order, visibility, validation pathways) when the current organization is insufficient.
- **Key Innovations**: First framework for inference-time self-evolution of multi-agent topology; highest average score 74.0 across five benchmarks (information seeking, tool use, planning, workflow, math), +5.8pp over strongest baseline, best on PlanCraft.
- **Link**: https://arxiv.org/abs/2607.28527

### 3. MemHarness: Memory Is Reconstructed, Not Replayed
- **Authors**: Rong Wu, Daocheng Fu, Licheng Wen, Xuemeng Yang, Shu Zou, Jianbiao Mei, Yuxin Wang, Hairong Zhang, Yu Yang, Tao Hu, Cong Zhang, Botian Shi, Pinlong Cai
- **Institution**: Shanghai AI Laboratory et al.
- **Abstract**: Argues that replaying retrieved experiences verbatim causes negative transfer because stored experience is abstract while decision states are concrete. MemHarness has a unified policy model critique and reconstruct retrieved memory conditioned on the current state, trained end-to-end with GRPO.
- **Key Innovations**: Reconstructive (not replay) memory paradigm; outperforms pure RL and static-memory baselines on ALFWorld/WebShop with strong OOD robustness; reconstruction objective also improves intrinsic reasoning as latent guidance.
- **Link**: https://arxiv.org/abs/2607.28272

### 4. Beyond Rephrasing: Book-Level Organization Improves Synthetic Textbook Data for Mid-Training
- **Authors**: Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan
- **Institution**: N/A
- **Abstract**: Studies whether organizing related synthetic content into coherent book-level documents matters (vs. content or local rewriting style). Pipeline: retrieve from pre-training corpus, cluster into topical units, plan hierarchical TOCs, assemble source-grounded sections into 686K books (32B tokens) across 15,000+ disciplines.
- **Key Innovations**: Isolates document packaging as a design axis via controlled ablations (Full vs Split vs RandomConcat vs Rephrase); +1.09 average downstream gain replacing natural books in mid-training mix; works on Llama3-8B.
- **Link**: https://arxiv.org/abs/2607.28109

### 5. Group-Reflective Self-Distillation for Agentic Reinforcement Learning (GRSD)
- **Authors**: Binbin Zheng, Zijun Xie, Guanqun Zhao, Enlei Gong, Xing Ma, Xiaoliang Fu, Zeyu Chen
- **Institution**: N/A
- **Abstract**: Derives capability-aligned, outcome-discriminative guidance from the policy's own verified rollouts. For each prompt, the policy reflects on verified trajectories in an on-policy group; a stop-gradient snapshot contrasts reflections from successful vs failed rollouts to build group-level privileged guidance for turn-level credit assignment.
- **Key Innovations**: Self-generated (not externally retrieved) skill guidance for agentic RL; consistently outperforms RLVR and existing self-distillation baselines and generalizes better to unseen tasks.
- **Link**: https://arxiv.org/abs/2607.28076

### 6. Echoverse: Deep, Evolving Environments for Training Computer-Use Agents at Scale
- **Authors**: Yash Pandya, Sahil Gupta, Sarthak Harne, Archana Yadav, Kavyansh Chourasia, Hussein Mozannar, Vibhav Vineet, Sara Abdali, Corby Rosset, Yash Lara, Ahmed Awadallah, Ece Kamar, Akshay Nambi
- **Institution**: Microsoft Research
- **Abstract**: Compiles specifications into stateful applications whose tasks are graded against the application's own database, plus a co-evolution loop reading every graded rollout twice: as environment/task/verifier repairs and as model training signal.
- **Key Innovations**: Identifies three properties that drive returns — behavioral depth, failure-targeted interaction, and co-evolution; 9B model improves 36.5%→67.1% across 14 splits, within 14 points of the frontier model that taught it; releases four environments as a benchmark.
- **Link**: https://arxiv.org/abs/2607.28074

### 7. SKILL-KD: Contrastive Skill Distillation for LLM Agents
- **Authors**: Qiming Shi, Yibo Dou, Jiawen Zhu, Yulong Tao, Linbo Jin, Zhaolu Kang, Yunfan Zhou, Di Weng
- **Institution**: N/A
- **Abstract**: Treats skills as an explicit distillation medium between teacher and weaker student. Given a student failure and the teacher trajectory on the same task, SKILL-KD distills their actionable discrepancy into a textual skill patch, re-runs the student to evaluate, and iteratively refines. Drift-Aware Skill Consolidation prevents local-update skill drift.
- **Key Innovations**: Contrastive skill patches as reusable guidance; improves frozen student agents across five agent benchmarks over fixed-model adaptation baselines.
- **Link**: https://arxiv.org/abs/2607.28048

### 8. Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World Centric Foundation GUI Agents
- **Authors**: Hanzhang Zhou, Panrong Tong, Xu Zhang, Quyu Kong, Chenglin Cai, Tianyu Xia, Gongjie Zhang, Jianan Zhang, Long Li, Long Chen, Lei Wang, Gaole Dai, Pengxiang Li, Liangyu Chen, Yue Wang, Steven Hoi
- **Institution**: Alibaba Qwen Team
- **Abstract**: Real-world-centric foundation GUI agent spanning mobile, computer-use, web, and DeepSearch. Unified action space interleaves GUI operations with CLI execution and generates batched actions per turn; AutoResearch-style data flywheel and online RL over 100-turn trajectories with 10,000+ concurrent environments.
- **Key Innovations**: State of the art on mobile use (82.1% MobileWorld, 92.2% MobileWorld-Real, 97.5% AndroidDaily); competitive computer-use (79.5% OSWorld-Verified) and browser use (73.6% WebArena, 81.5% ScreenSpot-Pro) against frontier models incl. Opus 4.8, Gemini 3.1 Pro, GPT-5.6 Sol.
- **Link**: https://arxiv.org/abs/2607.28227

### 9. AISPA: User-Centric System Prompt Auditing for Large Language Model Applications
- **Authors**: Xiangning Lin, Shenzhe Zhu, Shu Yang, Zhenyu Zhang, Haoqian Zhang, Yipeng Zhao, Chengxuan Qian, Tianwei Wang, Ziheng Zhang, Zhenlong Yuan, Dingcheng Wang, Juncheng Wu, Yuan Si, Jiaxin Liu, Baolong Bi, Robert Mahari, Tobin South, Dazza Greenwood, Zexue He, Rishi Bommasani, Sophia Kazinnik, Andreas Haupt, Samuele Marro, Erik Brynjolfsson, Alex Pentland, Jiaxin Pei
- **Institution**: MIT et al.
- **Abstract**: User-centric framework for auditing system prompts across eight user-relevant dimensions. Reviews 3,249 instructions from 88 commercial AI products, classifying each as protective or problematic.
- **Key Innovations**: First systematic commercial system-prompt audit; finds 98.9% of products contain protective instructions but only 24% cover all eight dimensions, while ~40% contain at least one instruction working against user interests — protective and problematic instructions coexist.
- **Link**: https://arxiv.org/abs/2607.28617

### 10. OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models
- **Authors**: Qiushi Sun, Kanzhi Cheng, Yian Wang, Bowen Yang, Hang Yan, Liheng Chen, Fangzhi Xu, Zichen Ding, Nuo Chen, Jialin Cao, Xingdong Gong, Zehao Li, Kaiming Jin, Xinfeng Yuan, Zhoumianze Liu, Jingyang Gong, Zhangyue Yin, Jiahui Gao, Zhiyong Wu, Tianbao Xie, Jianbing Zhang, Ben Kao, Lingpeng Kong
- **Institution**: HKU et al.
- **Abstract**: Benchmark for evaluating VLM judges on computer-use agent trajectories. Trajectories come from diverse agent backbones executing human-verified instructions, rigorously labeled via multi-stage human annotation; derives OSReward-Hard (hard cases) and OSReward-Multi (efficiency/alignment scoring).
- **Key Innovations**: Finds SOTA VLMs share a systematic leniency bias (failed runs mislabeled as successes); releases OS-Shepherd-100K corpus and OS-Shepherd (9B/35B) open reward models matching commercial judges at 30–60% lower cost.
- **Link**: https://arxiv.org/abs/2607.28609

### 11. WIDE: Boosting Adaptive LLM Inference via Token-level Dynamic Width Pruning
- **Authors**: Haozhe Hu, Hao Wu, Peiran Yin, Chao Han, Yunpu Ma, Xiaoyu Shen
- **Institution**: N/A
- **Abstract**: First end-to-end differentiable token-level dynamic width pruning framework for both prefill and decode. Each token dynamically selects attention-head groups and FFN-channel groups; two-stage training learns token-wise sparse execution patterns; pruning-kernel co-design decomposes dynamic sparsity acceleration into mask reordering, block-level and intra-block skipping.
- **Key Innovations**: Neuron-block-level dynamic pruning granularity; at 50% sparsity, 55.1% boost over SOTA dynamic depth pruning; close-to-theoretical kernel speedups up to 1.98x (prefill) and 4.95x (decode), 1.68x/1.55x end-to-end.
- **Link**: https://arxiv.org/abs/2607.28418

### 12. Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning (SAO)
- **Authors**: Zhenyu Hou, Yujiang Li, Jie Tang, Yuxiao Dong
- **Institution**: Tsinghua University / Zhipu AI
- **Abstract**: Addresses stability and off-policy challenges in asynchronous RL. Replaces GRPO group-wise sampling with single-rollout sampling (one rollout per prompt), adds practical value-model training and strict double-side token-level clipping.
- **Key Innovations**: Trains stably for 1000 steps and consistently outperforms GRPO variants on SWE-Bench Verified, BeyondAIME, IMOAnswerBench; deployed in agentic RL pipeline for GLM-5.2 (750B-A40B). (Submitted Jul 8.)
- **Link**: https://arxiv.org/abs/2607.07508

### 13. Reinforcement Learning: From Algorithms To Foundation Models
- **Authors**: Zihan Ding
- **Institution**: Princeton University
- **Abstract**: PhD thesis studying RL from two perspectives: multi-agent RL in games (two-player zero-sum, large-scale video games, general-sum multi-player settings) and RL with generative/foundation models (diffusion world models, RL for video generation, generative policy classes, interactive video world models, long-horizon memory architectures).
- **Key Innovations**: Unifies RL as objective-driven adaptation from strategic games to foundation-model capabilities. (Submitted Jul 20.)
- **Link**: https://arxiv.org/abs/2607.17560

---

## Recommendation, CTR & Advertising

### 14. CCFormer: Efficient Cross-Field Interaction and Hierarchical Sequence Compression for Industrial Recommendation at Tencent
- **Authors**: Yunlong Wang, Huizhe Zhang, Haonan Hu, Yudong Li, Bing Wen, Jianchao Tu, Chengxiang Zhuo, Zang Li
- **Institution**: Tencent
- **Abstract**: Transformer backbone unifying cross-field feature interaction and compressed long-sequence modeling: feature-field separated cross attention + long-sequence subspace token mixing, with hierarchical sequence compression using progressively expanded receptive fields.
- **Key Innovations**: Fully deployed on Tencent production recommendation (video + ads); +3.57% CTR and +1.71% ad revenue in A/B tests; 2.21x training acceleration over HSTU.
- **Link**: https://arxiv.org/abs/2607.28070

### 15. Hierarchical Latent Reasoning for LLM-based Recommendation (HiLaR)
- **Authors**: Peiyu Hu, Siying Gu, Weihai Lu, Zhuodong Liu, Yuntian Tang, Jiahao Liang, Yiying Xie, Jiang Rong, Zhaokai Luo, Zhiyong Wang, Jia Wang
- **Institution**: N/A
- **Abstract**: Builds temporal-guided hierarchical user preference representations aligned with multiple LLM latent reasoning states, organizing reasoning from broad preferences to fine-grained current intents. Combines final recommendation feedback with layer-aware process rewards from marginal target-likelihood gain of each state.
- **Key Innovations**: Layer-wise characterization of latent reasoning roles; outperforms sequential, generative, and LLM-based baselines on four Amazon benchmarks; code released.
- **Link**: https://arxiv.org/abs/2607.27760

### 16. LoopMemGR: From Behavior Logs to Evolving Memory for Generative Recommendation
- **Authors**: Hui Qian, Changfa Wu, Chang Liu, Binbin Cao, Jian Wu, Yuliang Yan, Han Zhu, Bo Zheng
- **Institution**: Alibaba (Taobao)
- **Abstract**: Identifies "asymmetric memory" in generative recommendation — systems remember user behavior but not their own prior recommendations and resulting feedback. Maintains a recommendation experience log with recency/frequency/global views compressed into a fixed number of experience tokens conditioning the generative backbone.
- **Key Innovations**: Closed-loop recommendation experience memory; multi-view experience extraction validated on industrial Taobao dataset.
- **Link**: https://arxiv.org/abs/2607.27647

### 17. ROCS: Request-Oriented Compute Sharing for Efficient Large-Scale Recommendation
- **Authors**: Yuxin Chen et al. (47 authors)
- **Institution**: Meta
- **Abstract**: Exploits a unique property of recommendation inference — one request evaluated against many candidates with shared request-side features. ROCS defers request-candidate interactions as late as possible and evaluates model portions once per request instead of once per candidate. Components: Generalized Layer Masking (GLM), Deep Cross Attention (DCA), In-Kernel Broadcast Optimization (IKBO).
- **Key Innovations**: Up to 3x QPS gain on retrieval without quality loss; +0.5% LogLoss with 50% QPS gain on short-form video ranking; deployed across ads and organic surfaces spanning >2 orders of magnitude inference complexity.
- **Link**: https://arxiv.org/abs/2607.27744

### 18. From Understanding to Action: Feedback-Grounded Policy Discovery for Generative Recommendation
- **Authors**: Zhi Chen, Minmao Wang, Xingchen Liu, Haoqiang Liang, Huihuang Lin, Likang Wu, Hongke Zhao, Yulong Wang, Shijie Yi, Fei Pan, Peng Jiang
- **Institution**: N/A
- **Abstract**: Introduces the Understanding-Action Gap: LLMs reason over interaction histories but aren't trained on recommendation outcome feedback. Distinguishes intent knowledge (current demand) from policy knowledge (recommendation direction and rejection boundary); policies are discovered by incremental utility over an intent-only baseline using outcome-derived feedback, then distilled into two latent tokens of a Semantic-ID generator.
- **Key Innovations**: Feedback-driven policy discovery replacing linguistic plausibility; LLM-free online inference via dual-space relational distillation; +4.506% Revenue and +4.621% ADVV in large-scale A/B tests.
- **Link**: https://arxiv.org/abs/2607.27789

### 19. Restoring Collaborative Signals in Semantic-ID Generative Recommendation via Personalized Natural Language
- **Authors**: Changjiang Han, Qingyang Li, Yaqiang Zang, Jikun Kang, Pinghua Gong, Xue Liu, Bowei He
- **Institution**: N/A
- **Abstract**: Shows that a compact Semantic-ID cannot hold content and collaborative signal at once — collaboration loses, capping recommendation accuracy. Uses personalized natural language to attach analyzable links between collaborative patterns and their audiences at generation time, without retraining SIDs or altering the backbone.
- **Key Innovations**: Inference-time channel carrying collaborative signal into SID generation; consistent accuracy gains without explicit reasoning or retraining; diagnoses why "thinking" gives no gain or hurts in SID models.
- **Link**: https://arxiv.org/abs/2607.27682

### 20. Learning from the Future: Privileged Self-Distillation for Sequential Recommendation (PSD)
- **Authors**: Jiakai Tang, Yang Zhang, See-Kiong Ng, Xu Chen, Wen Chen, Jian Wu, Han Zhu
- **Institution**: NUS et al.
- **Abstract**: Uses future interactions (which reveal how user intent evolves) as training-only privileged information. Two attention masks on the same backbone: future-aware teacher vs prefix-only student. Advantage-reachability gate and momentum-averaged teacher stabilize the one-stage, end-to-end distillation.
- **Key Innovations**: Teacher's advantage is purely informational (shared backbone, no pretrained teacher); deployed model and inference cost unchanged; consistent gains across benchmarks and backbones.
- **Link**: https://arxiv.org/abs/2607.27055

### 21. IMFuse: Instance-Aware Multi-Layer Fusion for LLM-Enhanced Sequential Recommendation
- **Authors**: Yuheng Zheng, Yu Cui, Bin Wu, Jian Zhang, Ye Feng, Can Wang, Jiawei Chen
- **Institution**: Zhejiang University / Zhengzhou University / USTC
- **Abstract**: Shows final-layer LLM hidden states suffer dimensional collapse while intermediate layers preserve complementary coarse-to-fine semantics, and different items evolve representations heterogeneously. IMFuse learns global dimension-wise layer preferences plus instance-aware expert modulation for item-specific representations.
- **Key Innovations**: Adaptive multi-layer fusion replacing single-layer reliance; +6.72% average relative improvement over SOTA across four datasets with limited overhead.
- **Link**: https://arxiv.org/abs/2607.27002

### 22. DASH: Beyond Action Imitation — Decision-Aware User Simulator for Online Advertising
- **Authors**: Zipeng Chen, Jiaer Zheng, Xiangyang Xu, Xinyu Lin, Zhaobin Wang, Zhaohui Liu, Qianjin Xiang, Xiaoyu Zhao, Zhuozhen Yu, Guangshuo Wang, Daxing Chen, Junwei Pan, Zhangbin Zhu, Chengguo Yin, Hao Chen, Tat-Seng Chua, Haijie Gu, Jie Jiang
- **Institution**: Tencent / NUS
- **Abstract**: User simulator that jointly generates thinking traces and predicts actions from heterogeneous cross-domain histories. Context Engineering folds cross-domain histories into decision-relevant context; thinking trajectories distilled from strong LLMs as SFT data plus a rubric-based reward model (form, content, logic) for RL training.
- **Key Innovations**: Models cognitive decision process rather than action imitation; validated on real-world Tencent advertising data across five domains; improved fidelity and diagnostic value.
- **Link**: https://arxiv.org/abs/2607.26893

### 23. WhisperRec: Latent Reasoning for Efficient Foundation Recommendation Models
- **Authors**: Hao Jiang, Peiru Du, Pengfei Yao, Mengting Li, Siyuan Lou, Kuo Cai, Sheng Yu, Qiang Luo, Jian Liang, Ruiming Tang, Fei Pan, Peng Jiang, Wenwu Ou
- **Institution**: Kuaishou
- **Abstract**: Compresses teacher-generated Chain-of-Thought into learnable latent reasoning tokens (Latent-Reason-then-Answer), avoiding verbose rationale generation. Multi-View Adaptive CoT adapts reasoning complexity per instance; three-stage Latent Reasoning Alignment internalizes teacher CoT into latent space.
- **Key Innovations**: +17.44% SID@64 over explicit-CoT Think variants with >10x online inference throughput; curriculum-based post-training preserves standard recommendation capability; industrial-scale Kuaishou dataset.
- **Link**: https://arxiv.org/abs/2607.26621

### 24. Multi-Decoder OneRec: Controllable Generative Retrieval for Multi-Objective Industrial Recommendation
- **Authors**: You Wang, Zhao Liu, Guoping Tang, Yiqing Yang, Shuo Su, Jing Liu, Naifu Zhou, Xiaoyou Zhou, Wei Jiang, Jian Liang, Xiao Lv, Ruiming Tang, Liyin Hong, Wenwu Ou
- **Institution**: Kuaishou
- **Abstract**: Shared user-context module and General Decoder with per-objective LoRA experts, trained via exposure-sample NTP, target-filtered NTP, and KL-regularized policy optimization with gradient routing. At inference, route quotas + Multi-Decoder Constrained Beam Search reduce cross-route overlap.
- **Key Innovations**: Releases Kwai26, a 1.31B-record multi-objective benchmark; +1.69–5.62% across four Recall@512 metrics vs single-decoder OneRec; production A/B gains incl. +2.09% new-content Cold-Start.
- **Link**: https://arxiv.org/abs/2607.26500

### 25. Guess Where You Go: Generative Next Point-of-Interest Recommendation in Amap (Gwhere)
- **Authors**: Penglong Zhai, Bowen Zheng, Jie Li, Yifang Yuan, Yue Liu, Sicong Wang, Mingyang Yin, Tingting Hu, Shuaijun Guo, Fanyi Di, Xin Li
- **Institution**: Alibaba (Amap)
- **Abstract**: End-to-end framework integrating Semantic-ID generation with LLM-based next-POI recommendation: contrastive residual-quantization tokenizer aligning textual/visual/spatial/collaborative signals, continued pretraining on enriched spatio-temporal corpora, SFT, and Exposure-Aware Kahneman-Tversky Optimization (EAKTO) RL for behavioral preference alignment.
- **Key Innovations**: Deployed in Amap homepage under high-concurrency/low-latency; long-term A/B gains of +5.83% P-CTR and +6.20% U-CTR. (Submitted Jul 13.)
- **Link**: https://arxiv.org/abs/2607.26073

### 26. LGRID: Interpretable Representation via LLM-Driven Generative Disentanglement for Local-Life Service Recommendation
- **Authors**: Long Zhang, Hao Jiang, Sheng Yu, Fei Pan, Peng Jiang, Kun Gai
- **Institution**: Kuaishou
- **Abstract**: Generative disentanglement paradigm (Encode→Disentangle→Align→Quantize): joint LLM encoding preserves cross-attribute geographic-semantic dependencies, Structured Disentangled Block routes hidden states into attribute-aligned slots, Synergistic Alignment Learning makes slots generatively decodable and discriminative, Dual-Stream Residual Quantization produces interpretable SIDs.
- **Key Innovations**: Interpretable SIDs with attribute-grounded positions; up to +5.44% relative AUC on Kuaishou/Foursquare; >99% attribute-decoding accuracy for coarse geography; full-SID collision rate cut to 39.9% vs 97.0% for LGSID.
- **Link**: https://arxiv.org/abs/2607.27944

### 27. Heterogeneous Ranking in Industrial-Scale Recommender Systems: A Case Study (HA-MoE)
- **Authors**: Di Bai, Jintao Liu, Zhenwei Tang, Peifan Wu, Nada Al-Thawr, Luoshu Wang
- **Institution**: Google (Discover)
- **Abstract**: Case study on multi-task ranking of heterogeneous feeds in Google Discover (web articles, long/short-form video, UGC). HA-MoE is a heterogeneity-adaptive multi-gated mixture-of-experts with explicit heterogeneity context in gating and expert representations; LENS observability framework tracks expert specialization across retraining; evaluated with Dual-Level AUC (DL-AUC).
- **Key Innovations**: Avoids negative transfer and majority bias in heterogeneous ranking; accepted at ACM RecSys 2026 Industry Track; online A/B confirms feed activity and exploration gains.
- **Link**: https://arxiv.org/abs/2607.27577

---

## Sequential Modeling & Memory

### 28. Memory for Large Language Models
- **Authors**: Sining Zhoubian, Dan Zhang, Evgeny Kharlamov, Jie Tang
- **Institution**: Tsinghua University
- **Abstract**: Systematic, architecture-centric survey of memory in LLMs, characterizing memory along three orthogonal axes — representation (implicit vs explicit), update dynamics (offline vs online), persistence (short-term vs long-term) — and formalizing memory writing, routing, state transitions, and consolidation.
- **Key Innovations**: Unified framework bridging computation-coupled vs independently addressable memory; critically analyzes hybrid architectures, efficiency trade-offs, and multi-dimensional evaluation. (Submitted Jul 28.)
- **Link**: https://arxiv.org/abs/2607.25380

### 29. Naju: A Native Discrete State-Space Model with Independent Retention and Writing for Long-Sequence Memory
- **Authors**: Hyuk Lim, Seunghyun Yoon
- **Institution**: N/A
- **Abstract**: Parameterizes the discrete SSM transition directly (bypassing continuous-time zero-order-hold discretization), factorizing the recurrence into an explicit learned forget gate (Schur-stable by construction), an independent write gain, and input-dependent write/read maps. Formalizes why coupled single-gate designs tie retention and write gain (|r|+w≤1).
- **Key Innovations**: Only evaluated model staying strong on both retention and overwriting at 4x training length; outperforms Mamba baselines on WikiText-103, Long Range Arena, multi-query associative recall with linear-time/linear-memory scaling. (Submitted Jul 23.)
- **Link**: https://arxiv.org/abs/2607.21000

### 30. HOLA: A Hippocampus for Linear Attention — An Exact Memory for What the Recurrent State Forgets
- **Authors**: Wanyun Cui
- **Institution**: N/A
- **Abstract**: Gives linear-attention/SSM models a hippocampal complement: keeps the delta-rule state as compressive memory and adds a bounded exact KV cache (semiparametric test-time memory). Cache writes tokens with large beta·‖e‖ (prediction residual committed to state); decoupled RMSNorm-gamma cache read turns exact KV pairs into sharp retrieval.
- **Key Innovations**: At 340M params / 15B tokens, Wikitext ppl 27.32→22.92 (-16.1%), below full-attention Transformer++; robust RULER needle recall out to 32k tokens (16x training length). (Submitted Jul 2.)
- **Link**: https://arxiv.org/abs/2607.02303

---

## Key Themes

| Theme | Papers | Trend |
|-------|--------|-------|
| **Latent reasoning** | WhisperRec, HiLaR | CoT compressed into latent tokens to avoid verbose rationale overhead; layer-aware process rewards emerging |
| **Memory for LLMs/agents** | MemHarness, Memory survey, HOLA, Naju, LoopMemGR | Shift from replay to reconstruction; architecture-centric memory taxonomies; SSMs decoupling retention/writing |
| **Inference-time adaptation** | SVR, MANTA, WIDE, GRSD | Self-evolution at inference: adaptive test-time compute, adaptive multi-agent topology, token-level dynamic pruning |
| **Computer-use agents** | Qwen-UI-Agent, Echoverse, OSReward | Foundation GUI agents, evolving training environments, standardized reward-model evaluation; frontier gap closing |
| **Generative recommendation** | CCFormer, ROCS, LoopMemGR, Feedback-Grounded, OneRec, Gwhere, LGRID, WhisperRec | Industrial adoption of Semantic-ID generative retrieval; shared-compute inference; closed-loop experience memory |
| **System prompt governance** | AISPA | Commercial system prompts largely unaudited; protective and problematic instructions coexist |
| **Synthetic data** | Synthetic Textbook | Book-level organization is a distinct axis for synthetic pre-training data quality |

(End of file)
