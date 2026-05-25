---
title: arXiv Broad Survey — AI Research Landscape (May 2026)
type: synthesis
created: 2026-05-25
updated: 2026-05-25
sources: []
tags: [arxiv, survey, llm, recsys, agents, games, diffusion, sequence-modeling, benchmarks]
---

# arXiv Broad Survey — AI Research Landscape (May 2026)

> Comprehensive survey of recent arXiv papers (2025-2026) across 10 research areas: LLM training/theory, recommendation systems, CTR prediction, ad retrieval, agents/multi-agent, game AI/RL, code execution prediction, generative models/diffusion, sequence modeling, and evaluation benchmarks.

---

## 1. LLM Training & Theory

### 1.1 Scaling Laws & Optimization

| Paper | Chinese Title | Authors | Affiliation | arXiv | Route | Contribution |
|-------|-------------|---------|-------------|-------|-------|-------------|
| HyperP: Hypersphere Parameterization | 超球参数化：统一learning rate迁移框架 | - | - | 2603.28743 | MoE Scaling | First LR transfer laws across FLOPs for hypersphere optimization; SqrtGate reduces router Z-value peaks by 5× |
| Train-to-Test Scaling Laws | 训练-测试联合Scaling Law | - | - | 2604.01411 | Scaling Law | Joint optimization of model size, training tokens, and test-time samples; overtrained smaller models optimal with repeated sampling |
| FineRMoE: FineR-Grained MoE | 细粒度MoE：扩展到输出维度 | - | - | 2603.13364 | MoE Architecture | Extends fine-grained expert design from intermediate to output dimension; 6× parameter efficiency |
| Batch Size Scheduling via FSL | 基于函数Scaling Law的批大小调度 | - | - | 2602.14208 | Training Efficiency | Late-switch batch schedules consistently outperform constant/early baselines across dense and MoE up to 1.1B |
| Megatron Core for MoE | Megatron Core的MoE可扩展训练 | NVIDIA | NVIDIA | 2603.07685 | Systems | Production-ready open-source MoE training achieving 1,233 TFLOPS/GPU for DeepSeek-V3-685B |
| MOUE: Mixture of Universal Experts | 通用专家混合：深度-宽度转换 | - | - | 2603.04971 | MoE Architecture | Introduces Virtual Width as new scaling dimension; reuses layer-agnostic expert pool across layers |
| Arcee Trinity Large | Arcee Trinity Large技术报告 | Arcee AI | Arcee AI | 2602.17004 | MoE Scaling | 685B MoE trained with Muon optimizer; SMEBU load balancing; sigmoid routing |
| PACED Distillation | 自适应能力增强蒸馏 | - | - | 2603.11178 | Knowledge Distillation | Beta-kernel pass-rate weighting for distillation; minimax-robust; +9.8 on MATH-500 |
| Low-Rank KD Theory | 低秩Knowledge Distillation理论保证 | - | - | 2603.22355 | Knowledge Distillation | First rigorous theoretical framework for low-rank KD; convergence O(1/√T) and generalization bounds |
| UNICOMP Compression | 统一压缩评估框架 | - | - | 2602.09130 | Model Compression | Systematic comparison of pruning, quantization, KD across LLMs; reasoning-oriented models more compression-sensitive |
| SPINAL Alignment Diagnostic | 对齐层几何诊断 | IIIT Ranchi / Google | IIIT Ranchi, Google | 2601.06238 | Alignment Theory | DPO alignment concentrates in terminal decoder blocks; SPINAL Score quantifies calibration |
| Introspective X Training (IXT) | 内省训练：反馈调节缩放 | - | - | 2605.20285 | Training Efficiency | Conditioning on rubric feedback across all stages; up to 2.8× FLOP efficiency gain |
| Decoupled DiLoCo | 解耦DiLoCo：异步分布式训练 | Google DeepMind | Google DeepMind | 2604.21428 | Distributed Training | Fully asynchronous learners; matches data-parallel quality with 88% goodput under failures |
| Efficient Exploration for RLHF | RLHF的高效探索缩放律 | - | - | 2603.17378 | RLHF Scaling | Online uncertainty-guided exploration; systematic scaling laws for RLHF data efficiency |
| Topology-Enhanced Alignment | 拓扑增强的LLM对齐 | - | - | 2605.07172 | Alignment | Persistent homology regularization for SFT and DPO; outperforms non-topological baselines |
| Meta Flow Maps | 元流图：可扩展奖励对齐 | - | - | 2601.14430 | Diffusion Alignment | Stochastic one-step posterior sampling for efficient reward alignment; beats Best-of-1000 |

### 1.2 LLM Post-Training & Reasoning

| Paper | Chinese Title | Authors | Affiliation | arXiv | Route | Contribution |
|-------|-------------|---------|-------------|-------|-------|-------------|
| SML: Social Meta-Learning | 社会元学习：对话中学习 | Google DeepMind | Google DeepMind | 2602.16488 | RL + SML | Online RL yields greater improvement than SFT for learning from language feedback; cross-domain transfer |
| TMPC: Textual Model Predictive Control | 文本模型预测控制 | NVIDIA / NYCU | NVIDIA, NYCU | 2026 ICLR | Test-time Alignment | MPC-inspired test-time alignment; hindsight subgoal identification + subgoal-conditioned re-generation |
| Shifting the Gradient (PPS vs IP) | 梯度偏移：防御训练机制 | - | - | 2604.16423 | Safety Alignment | PPS shifts activation gradient; IP explains away trait expression; distinct mechanisms for safety |
| RubricEval | 评分标准级元评估基准 | - | - | 2603.25133 | Benchmark | First rubric-level meta-evaluation for instruction following; GPT-4o only 55.97% on Hard subset |

---

## 2. Recommendation Systems

| Paper | Chinese Title | Authors | Affiliation | arXiv | Route | Contribution |
|-------|-------------|---------|-------------|-------|-------|-------------|
| Netflix Generative Recommender Scaling | Netflix生成式推荐器缩放 | Netflix | Netflix | 2605.23312 | Generative Rec | Scaling generative recommenders to 1B params; production deployment at Netflix |
| RankElastor | 有效秩动力学推荐 | - | KDD 2026 | 2605.23191 | Rec Theory | Effective-rank dynamics for understanding and improving recommendation quality |
| LoopCTR | 循环缩放：CTR预测新范式 | - | - | 2604.19550 | Loop Scaling | Train-multi-loop, infer-zero-loop; 0.02-0.04 AUC untapped headroom |
| OneMall (Kuaishou) | OneMall：快手电商生成式推荐 | Kuaishou | Kuaishou | 2601.21770 | Generative Rec | Unified e-commerce generative framework; +14.7% GMV in Product-Card; 400M DAU |
| LONGER (ByteDance) | LONGER：长Sequence Modeling | ByteDance | ByteDance | 2505.04421 | Sequence Rec | Long-sequence optimized transformer; deployed at Douyin for ads and e-commerce |
| OneTrans (ByteDance) | OneTrans：统一Feature Interaction与Sequence Modeling | ByteDance / NTU | ByteDance, NTU | 2510.26104 | Unified Rec | Unified transformer for feature interaction + sequence modeling; 5.68% GMV lift |
| OneRec-V2 (Kuaishou) | OneRec-V2技术报告 | Kuaishou | Kuaishou | 2508.20900 | Generative Rec | Lazy decoder-only architecture; preference alignment; 0.467-0.741% stay time improvement |
| DualGR (Kuaishou) | DualGR：长短兴趣生成式检索 | Kuaishou | Kuaishou | 2511.12518 | Generative Retrieval | Dual-branch long/short-term router; exposure-aware loss; +0.527% video views |
| HAP (ByteDance/Toutiao) | HAP：异构感知自适应预排序 | ByteDance | ByteDance | 2603.03770 | Pre-ranking | Heterogeneity-aware pre-ranking; gradient-harmonized contrastive learning; deployed 9 months |
| MaRI (Kuaishou) | MaRI：矩阵重参数化推理加速 | Kuaishou | Kuaishou | 2602.23105 | Inference Acceleration | Structural re-parameterization for ranking; 1.3× speedup, 5.9% resource reduction |
| GFlowGR (Alibaba) | GFlowGR：生成流网络微调推荐 | Alibaba / CityU HK | Alibaba, CityU HK | 2506.16114 | Generative Rec | GFlowNet fine-tuning for GR; deployed on Taobao; 1% annual revenue lift |
| RecGen (Kuaishou) | GR4AD：大规模广告生成式推荐 | Kuaishou | Kuaishou | 2602.22732 | Generative Rec | UA-SID tokenization; LazyAR decoder; RSPO RL; 4.2% ad revenue improvement |

---

## 3. CTR Prediction

| Paper | Chinese Title | Authors | Affiliation | arXiv | Route | Contribution |
|-------|-------------|---------|-------------|-------|-------|-------------|
| GRAB (Baidu) | GRAB：类LLM序列优先CTR预测 | Baidu | Baidu | 2602.01865 | Generative CTR | CamA mechanism; 3.05% CPM and 3.49% CTR lift; full deployment in Baidu feed ads |
| EST (Taobao) | EST：高效可扩展CTRScaling Law | Alibaba/Taobao | Alibaba/Taobao | 2602.10811 | Scaling CTR | Power-law scaling in CTR; LCA + CSA; 3.27% RPM lift on Taobao display ads |
| IDProxy (Xiaohongshu) | IDProxy：多模态LLM冷启CTR | Xiaohongshu | Xiaohongshu | 2603.01590 | Cold-start CTR | MLLM proxy embeddings aligned with ID embeddings; deployed in feed and display ads |
| CADET (LinkedIn) | CADET：上下文条件解码器CTR | LinkedIn | LinkedIn | 2602.11410 | Decoder-only CTR | Context-conditioned decoding; self-gated attention; 11.04% CTR lift |
| PRECTR-V2 (Meituan) | PRECTR-V2：统一相关性CTR框架 | Meituan | Meituan | 2602.20676 | Unified CTR | Cross-user preference mining; exposure debias; LLM-distilled encoder |
| DAIAN (Alibaba/Xianyu) | DAIAN：深度自适应意图感知CTR | Alibaba/Xianyu | Alibaba/Xianyu | 2602.13971 | Intent-Aware CTR | Intent myopia mitigation; three-stage training; +1.59% CTR in TIR |
| HeMix (AMAP) | HeMix：可扩展CTR模型 | Alibaba/AMAP | Alibaba/AMAP | 2602.09387 | Scalable CTR | Query-mixed interest extraction; HeteroMixer block; +3.61% GMV on AMAP |
| LoopCTR | LoopCTR：循环缩放CTR范式 | - | - | 2604.19550 | Loop Scaling | Recursive loop block; process supervision; train-multi-loop infer-zero-loop |
| RankUp (Tencent) | RankUp：高秩表示广告排序 | Tencent | Tencent | 2604.17878 | Representation Learning | Mitigates embedding collapse; +3.41-4.81% GMV on Weixin scenarios |
| OneRanker (Tencent) | OneRanker：统一生成与排序 | Tencent | Tencent | 2603.02999 | Generative Ranking | Value-aware multi-task decoupling; K/V pass-through; +1.34% GMV |

---

## 4. Ad Retrieval & Sponsored Search

| Paper | Chinese Title | Authors | Affiliation | arXiv | Route | Contribution |
|-------|-------------|---------|-------------|-------|-------|-------------|
| LinkedIn LLM Ad Retrieval | LLM检索稳定广告推荐 | LinkedIn | LinkedIn | 2605.21969 | Semantic Retrieval | Semantic candidate generation via fine-tuned LLMs; 45% MAD improvement |
| Walmart Unified Supervision | Walmart赞助搜索统一监督 | Walmart | Walmart | 2604.07930 | Retrieval Supervision | Combined cross-encoder + retrieval prior + engagement for bi-encoder training |
| AdNanny (Bing Ads) | AdNanny：统一推理广告引擎 | Microsoft Bing Ads | Microsoft | 2602.01563 | Unified Ads LLM | Single 671B reasoning LLM replacing task-specific models; SFT + RL alignment |
| KP-Agent (Meituan) | KP-Agent：关键词剪枝代理 | Meituan | Meituan | 2601.05257 | Agentic Ads | LLM contextual bandit for keyword pruning; 49.28% cumulative profit improvement |
| RARE (Alibaba) | RARE：实时广告检索框架 | Alibaba | Alibaba | 2504.01304 | Generative Retrieval | LLM-generated Commercial Intentions; 5.04% consumption increase |
| LBM Auto-Bidding | LBM：分层自动竞价大模型 | Alibaba | Alibaba | 2603.05134 | Auto-bidding | LBM-Think reasoning + LBM-Act; GQPO offline RL fine-tuning |
| GR4AD (Kuaishou) | GR4AD：广告生成式推荐 | Kuaishou | Kuaishou | 2602.22732 | Generative Ad | See Section 2 for details |
| Autobidding Equilibria | 赞助购物自动竞价均衡 | - | - | 2602.21966 | Auction Theory | Universal existence of autobidding equilibrium; tight PoA of 2 |
| Position Auctions in AIGC | AIGC中的位置拍卖 | - | - | 2506.03309 | Auction Theory | Extended position auctions for AI-generated content; MNL and cascade models |

---

## 5. Agents & Multi-Agent Systems

| Paper | Chinese Title | Authors | Affiliation | arXiv | Route | Contribution |
|-------|-------------|---------|-------------|-------|-------|-------------|
| Coalition Formation in LLM Agent Networks | LLM代理网络联盟形成 | - | - | 2604.14386 | Game Theory | First hedonic game framework for LLM coalitions; Nash stability in 73.2% |
| DIG: Dynamic Interaction Graph | 动态交互图：通用代理协作 | - | - | 2603.00309 | MAS Analysis | Causal network modeling of emergent collaboration; real-time failure correction |
| Agent Q-Mix | Agent Q-Mix：RL多代理拓扑选择 | - | - | 2604.00344 | MARL Topology | QMIX value factorization for topology selection; 20.8% on HLE with Gemini |
| LLM-Derived Graph Priors for MARL | LLM图先验提升多代理协调 | - | - | 2604.17191 | GNN+LLM MARL | First quantitative evidence LLM priors enhance MARL coordination; 1.5B params sufficient |
| Cooperation in Multi-Agent LLMs | 多代理LLM协作失败分析 | - | ICLR 2026 WS | 2604.07821 | Cooperation Analysis | o3 achieves only 17% optimal collective performance; capability ≠ cooperation |
| Agentic AI Architecture Taxonomy | 代理AI架构分类法 | - | - | 2601.12560 | Survey | Unified taxonomy: Perception, Brain, Planning, Action, Tool Use, Collaboration |
| Mass: Multi-Agent System Search | Mass：多代理系统搜索优化 | - | - | 2502.02533 | MAS Optimization | Automated prompt+topology optimization; outperforms manually-designed MAS |
| AgentConductor | AgentConductor：RL优化拓扑MAS | - | - | 2602.17100 | RL Topology | RL-optimized orchestrator for dynamic DAG topology; 14.6% pass@1 improvement |
| AgentAuditor | AgentAuditor：推理树审计 | - | - | 2602.09341 | MAS Auditing | Anti-Consensus Preference Optimization; up to 5% over majority voting |
| AgentArk | AgentArk：多代理蒸馏到单代理 | - | - | 2602.03955 | Distillation | Distills multi-agent dynamics into single model; efficient and robust reasoning |
| SAMPO | SAMPO：稳定代理策略优化 | - | - | 2602.21534 | Agentic RL | Systematic ARL stability analysis; 25.2% improvement over GRPO |
| Credit Assignment Survey | 代理RL信用分配综述 | - | - | 2604.09459 | Survey | 47 CA methods surveyed; taxonomy by granularity and methodology |
| ARLArena | ARLArena：代理RL训练稳定性 | - | - | 2602.21534 | Agentic RL | Standardized testbed; SAMPO method; 25.2% improvement |
| SkillOpt | SkillOpt：自进化代理技能 | Microsoft Research Asia | Microsoft | 2605.23904 | Agent Skills | Self-evolving agent skills through structured optimization |
| Foundation Protocol | Foundation Protocol：代理社会协调 | Tencent/HKUST/UIUC | Tencent, HKUST, UIUC | 2605.23218 | Agent Protocol | Agentic society protocol for inter-agent coordination |
| AutoResearch AI | AutoResearch AI：研究自动化 | Salesforce | Salesforce | 2605.23204 | Research Agent | Multi-agent research automation with verification |
| Inductive Deductive Synthesis | 归纳演绎综合验证系统 | UC Berkeley/Microsoft | UC Berkeley, Microsoft | 2605.23109 | Verified Synthesis | Combines inductive and deductive reasoning for verified program synthesis |
| EVE-Agent | EVE-Agent：证据可验证自进化 | - | - | 2605.22905 | Self-Evolving | Evidence-verifiable self-evolving agents with formal guarantees |

---

## 6. Games & Strategic Reasoning

| Paper | Chinese Title | Authors | Affiliation | arXiv | Route | Contribution |
|-------|-------------|---------|-------------|-------|-------|-------------|
| SPIRAL | SPIRAL：零和博弈自对弈推理 | - | - | 2506.24119 | Self-Play RL | Self-play in zero-sum games; up to 10% improvement across 8 reasoning benchmarks |
| Odysseus | Odysseus：VLM长程决策游戏RL | - | - | 2605.00347 | VLM+RL | PPO with turn-level critic; 3× game progress vs frontier models |
| OpenGame | OpenGame：开源代理式游戏开发 | - | - | 2604.18394 | Agentic Game Dev | GameCoder-27B; execution-grounded RL; 150 diverse game prompts |
| Generalist Game Player Survey | 通用游戏玩家：基础模型调查 | - | - | 2605.09965 | Survey | Five-level roadmap from single-game mastery to creator stage |
| Game BC Scaling Laws | 游戏行为克隆Scaling Law | - | - | 2601.04575 | BC Scaling | Power-law in game BC; larger models improve causal reasoning |
| MARL-GPT | MARL-GPT：多智能体RL基础模型 | - | - | 2604.05943 | Foundation MARL | Single GPT model across SMACv2, GRF, POGEMA; multi-task MARL |
| Cross-Entropy Games | 交叉熵游戏 | - | - | 2603.22479 | Game Curriculum | Cross-entropy as game curriculum for general capability emergence |
| Nemobot | Nemobot：LLM游戏代理工程 | - | - | 2604.21896 | LLM Game Agents | Taxonomy-based game agent engineering; self-programming AI agents |
| HGPO | HGPO：分层组策略优化 | - | - | 2602.22817 | Multi-agent RL | Hierarchy-of-groups for scalable multi-agent policy optimization |
| Dark Souls III Lifelong | 黑暗之魂III终身学习 | - | ICLR '26 WS | 2601.17923 | Lifelong RL | Lifelong learning in complex 3D game environments |
| PCSP | PCSP：统一NPC策略 | - | - | 2605.23652 | Persona RL | One policy for infinite NPCs via persona-conditioned shared policy |
| GenStrat | GENSTRAT：LLM战略推理 | - | - | 2605.23238 | Strategic Reasoning | General strategic reasoning benchmark and method for LLMs |

---

## 7. Code Execution & Program Repair

| Paper | Chinese Title | Authors | Affiliation | arXiv | Route | Contribution |
|-------|-------------|---------|-------------|-------|-------|-------------|
| SVRepair | SVRepair：结构化视觉程序修复 | - | - | 2602.06090 | Multimodal Repair | Structured visual reasoning for APR; 36.47% on SWE-Bench M |
| SYNTHFIX | SYNTHFIX：自适应神经符号漏洞修复 | - | - | 2604.17184 | Neuro-Symbolic | Compiler-informed symbolic rewards; adaptive SFT/RFT routing; 18% CodeBLEU improvement |
| DebugRepair | DebugRepair：自导向调试修复 | - | - | 2604.19305 | Debugging | Simulated instrumentation; debugging-driven repair; 51.3% more bugs fixed |
| FailureMem | FailureMem：多模态程序修复 | - | - | 2603.17826 | Multimodal Repair | Hybrid workflow-agent; failure memory bank; +3.7% on SWE-Bench M |
| ReinFix | ReinFix：修复成分搜索 | - | - | 2506.23100 | Retrieval Repair | Static analysis + historical fix retrieval; 146 bugs fixed on Defects4J V1.2 |
| Verify Before You Fix | 执行验证的跨语言漏洞修复 | - | - | 2604.10800 | Execution-Grounded | uAST normalization; execution-grounded validation; 69.74% end-to-end resolution |
| SelfHeal + AgentDefect | SelfHeal：LLM代理缺陷修复 | - | - | 2604.17699 | Agent Bug Repair | First benchmark for LLM agent bugs (AgentDefect); dual ReAct agent framework |
| DynaFix | DynaFix：执行级动态修复 | - | - | 2512.24635 | Dynamic Repair | ByteTrace instrumentation; closed-loop execution feedback |
| ExpeRepair | ExpeRepair：双记忆修复 | - | - | 2506.10484 | Memory-Augmented | Dual-memory (episodic + semantic); 74.6% pass@1 on SWE-Bench Verified |
| Prometheus | Prometheus：意图桥接修复 | - | - | 2604.17464 | Specification Inference | BDD specification inference; 93.97% correct patch rate on Defects4J |
| Agentic Proving | Agentic Proving：程序验证 | - | - | 2605.23772 | Formal Verification | Agentic approach to interactive theorem proving |
| ImProver 2 | ImProver 2：神经符号证明优化 | CMU | CMU | 2605.22885 | Proof Optimization | Neurosymbolic proof optimization with learned heuristics |
| RMA | RMA：研究数学代理系统 | - | - | 2605.22875 | Math Agent | Agentic system for research-level mathematics |

---

## 8. Generative Models & Diffusion

| Paper | Chinese Title | Authors | Affiliation | arXiv | Route | Contribution |
|-------|-------------|---------|-------------|-------|-------|-------------|
| ViBe | ViBe：超高分辨率视频合成 | - | - | 2603.23326 | Video Diffusion | Pure image adaptation for ultra-high-res video; Relay LoRA; no video training data needed |
| GPDiT | GPDiT：autoregressive扩散Transformer | - | - | 2505.07344 | AR Diffusion | Unifies autoregressive and diffusion for long-range video; continuous latent space |
| PixelGen | PixelGen：像素空间扩散超越latent space | - | - | 2602.02493 | Pixel Diffusion | Perceptual supervision; FID 5.11 on ImageNet-256; GenEval 0.79 |
| LoL | LoL：视频生成长度延长至小时 | - | - | 2601.16914 | Long Video | Sink-collapse analysis; streaming generation to infinity |
| DyDiT++ | DyDiT++：动态扩散Transformer | Alibaba | Alibaba | 2504.06803 | Efficient Diffusion | TDW + SDT dynamic computation; 51% FLOPs reduction; 1.73× speedup |
| Bernini | Bernini：潜语义规划视频扩散 | - | - | 2605.22344 | MLLM+Diffusion | MLLM planner + DiT renderer; SOTA video generation and editing |
| LatSearch | LatSearch：潜奖励引导搜索 | - | - | 2603.14526 | Inference Scaling | Latent reward model for search in video diffusion; improved VBench-2.0 |
| Drift-AR | Drift-AR：单步视觉autoregressive | - | - | 2603.28049 | AR Acceleration | Entropy-informed speculative decoding; 3.8-5.5× speedup |
| Causal Forcing | Causal Forcing：autoregressive扩散蒸馏 | - | - | 2602.02214 | Video AR Distillation | AR teacher ODE distillation; 19.3% Dynamic Degree improvement |
| Adaptive Video Distillation | 自适应视频蒸馏 | - | - | 2603.21864 | Video Distillation | Adaptive regression loss + temporal regularization; few-step video synthesis |
| Precise (ByteDance) | Precise：SDE一致性流匹配RL | ByteDance | ByteDance | 2605.23522 | Flow-Matching RL | SDE-consistent sampling for flow-matching RL |
| DiLaDiff (NVIDIA) | DiLaDiff：蒸馏潜增强扩散LM | NVIDIA | NVIDIA | 2605.23605 | Diffusion LM | Distilled latent-augmented diffusion for language modeling |

---

## 9. Sequence Modeling & Transformers

| Paper | Chinese Title | Authors | Affiliation | arXiv | Route | Contribution |
|-------|-------------|---------|-------------|-------|-------|-------------|
| InfoMamba | InfoMamba：无注意力混合Mamba | - | - | 2603.18031 | SSM Hybrid | Concept-bottleneck linear filtering + SSM; outperforms Transformer and SSM baselines |
| Mamba-3 | Mamba-3：状态空间原理改进 | - | - | 2603.15569 | SSM | Complex-valued state update; MIMO formulation; 1.8 pp accuracy gain |
| TransMamba | TransMamba：序列级混合Transformer-Mamba | - | - | 2503.24067 | SSM Hybrid | Shared parameters between Transformer and Mamba; dynamic switching |
| Swimba (Switch Mamba) | Swimba：MoE参数化SSM | NVIDIA | NVIDIA | 2603.06938 | MoE + SSM | Routes over expert SSM streams; single-pass recurrence; 14B model |
| UniMamba | UniMamba：统一时空Mamba | - | - | 2604.16325 | Time Series | FFT-Laplace + TCN + Spatial-Temporal Attention for forecasting |
| LongMamba | LongMamba：训练免费Mambalong-context | - | - | 2504.16053 | Long Context SSM | Training-free receptive field expansion; token filtering for global channels |
| HADES | HADES：层次自适应SSM滤波器组 | - | - | 2603.22333 | SSM Theory | GSP-inspired reinterpretation of Mamba2; 58.9% parameters of baseline |
| Sessa | Sessa：选择性状态空间注意力 | - | - | 2604.18580 | SSM Theory | Attention in recurrent feedback path; power-law memory tails |
| Understanding Mamba Selectivity | Mamba输入选择性理论理解 | - | - | 2506.11891 | SSM Theory | Mamba S6 = Haar wavelet projection; analytical solutions to MQAR |
| CAB Distillation (Transformer→Mamba) | 跨架构注意力桥接蒸馏 | - | ICLR 2026 | - | Cross-Arch Distillation | Attention Bridge for Transformer→SSM distillation; data-efficient |
| Preisach Attention | Preisach注意力：迟滞序列记忆 | - | - | 2605.23603 | Novel Attention | Hysteretic sequential memory based on Preisach model |
| Dimensionality Barrier (MIT) | 维度是检索的障碍吗？ | MIT | MIT | 2605.23556 | Retrieval Theory | Theoretical analysis of dimensionality constraints in retrieval |
| Training-Free Looped Transformers | 免训练循环Transformer | Google? | Google? | 2605.23872 | Looped Models | Training-free computation scaling via looped transformer layers |

---

## 10. Evaluation Benchmarks

| Paper | Chinese Title | Authors | Affiliation | arXiv | Route | Contribution |
|-------|-------------|---------|-------------|-------|-------|-------------|
| Benchmark Saturation Study | AI基准饱和系统研究 | - | - | 2602.16763 | Benchmark Analysis | 60 benchmarks analyzed; nearly half show saturation; expert-curated resists saturation better |
| LLMEvalDB | LLMEvalDB：大规模评估数据库 | - | - | 2502.18791 | Benchmark Database | 18,127 records from 1,737 papers; replicates CoT analysis findings |
| Benchmark Redundancy (PCA) | LLM基准冗余性分析 | - | - | 2603.00394 | Benchmark Redundancy | 2 PCs explain 97.4% variance; ARC-Challenge + TruthfulQA sufficient |
| MEDLEY-BENCH | MEDLEY-BENCH：元认知评估 | - | - | 2604.16009 | Metacognition | Evaluation/control dissociation; scale buys evaluation but not control |
| Interactive Leaderboards | 谁定义"最佳"？交互式LLM排行榜 | - | - | 2604.21769 | Leaderboard Design | LMArena analysis; user-defined evaluation priorities |
| IQ Test for LLMs | LLM智商测试：因子分析评估 | - | - | 2507.20208 | Skill-Based Eval | Factor analysis on 60 models × 44 tasks; 8 latent skills identified |
| RubricEval | RubricEval：评分标准级元评估 | - | - | 2603.25133 | Meta-Evaluation | 3,486 instances; rubric-level judging far from solved |
| CLARIN-PT-LDB | 葡萄牙语LLM排行榜 | PORTULAN | PORTULAN | 2603.12872 | Multilingual Eval | Novel benchmarks for Portuguese culture and safeguards |
| GraphOmni | GraphOmni：图任务LLM基准 | - | - | 2504.12764 | Graph Reasoning | 241,726 samples; 7 graph types; GPT-4o best but far from human |
| MetaLead | MetaLead：透明排行榜数据集 | - | - | 2601.22420 | Leaderboard Data | Human-annotated dataset with all experimental results |
| Benchmark Rigging Analysis | 基准操纵难度分析 | - | - | 2605.23628 | Benchmark Security | How hard it is to rig a benchmark; security analysis |

---

## Statistics Summary

| Category | Paper Count | Key Affiliations |
|----------|------------|-----------------|
| LLM Training & Theory | 16 | Google DeepMind, NVIDIA, Arcee AI, IIIT Ranchi |
| Recommendation Systems | 12 | Netflix, Kuaishou, ByteDance, Alibaba |
| CTR Prediction | 10 | Baidu, Alibaba, LinkedIn, Tencent, Meituan, Xiaohongshu |
| Ad Retrieval & Sponsored Search | 9 | LinkedIn, Walmart, Microsoft, Meituan, Alibaba, Kuaishou |
| Agents & Multi-Agent Systems | 14 | Salesforce, Microsoft, Tencent, UC Berkeley |
| Games & Strategic Reasoning | 12 | Various (unaffiliated + ICLR workshops) |
| Code Execution & Program Repair | 12 | CMU, Various |
| Generative Models & Diffusion | 12 | Alibaba, NVIDIA, ByteDance |
| Sequence Modeling & Transformers | 13 | NVIDIA, MIT, Google |
| Evaluation Benchmarks | 11 | PORTULAN, Various |
| **Total** | **121** | Cross-institution |

---

## References

All papers indexed by arXiv ID. See individual paper pages in `wiki/papers/` for detailed analysis.
