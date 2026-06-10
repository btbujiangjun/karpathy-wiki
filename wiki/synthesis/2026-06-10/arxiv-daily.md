---
title: "arXiv Daily — 2026-06-10"
type: synthesis
created: 2026-06-10
updated: 2026-06-10
sources: []
tags: [arxiv, daily, llm, recommendation, ctr, games, sequential-modeling, diffusion, agents]
---

# arXiv Daily Report — June 10, 2026

Curated recent papers from arXiv spanning AI, LLMs, recommendation systems, CTR prediction, sequential modeling, games, advertising, and diffusion language models.

---

## 1. LLM Reasoning & Efficiency

### Agentic Chain-of-Thought Steering for Efficient and Controllable LLM Reasoning (ACTS)

- **Authors**: Yu Xia, Zhouhang Xie, Xin Xu, Byungkyu Kang, Prarit Lamba, Xiang Gao, Julian McAuley
- **Institution**: Not specified (multi-affiliation)
- **Link**: [arXiv:2606.03965](https://arxiv.org/abs/2606.03965)
- **Abstract**: Formulates reasoning steering as a Markov decision process where a controller agent adaptively steers a frozen reasoner during inference. Issues budget-aware steering actions (reasoning strategy + steering phrase). Initialized from synthetic trajectories and optimized via RL with budget-conditioned reward shaping. Matches full-thinking performance with substantial token savings.
- **Key Innovations**: MDP-based reasoning steering; budget-aware strategy control; RL-optimized controller agent.
- **Tags**: `LLM`, `reasoning`, `chain-of-thought`, `efficiency`

### SIRI: Self-Internalizing Reinforcement Learning with Intrinsic Skills for LLM Agent Training

- **Authors**: Zhongyu He, Yuanfan Li, Fei Huang, Tianyu Chen, Siyuan Chen, Xingyang Li, Meng Hsuan Yu, Xiangrong Liu, Leyi Wei, Lu Pan, Ke Zeng, Xunliang Cai
- **Institution**: Not specified
- **Link**: [arXiv:2606.02355](https://arxiv.org/abs/2606.02355)
- **Abstract**: Three-phase framework enabling agents to discover, validate, and internalize skills without external skill generators or inference-time skill banks. Uses GiGPO warmup, self-skill mining, then distillation of beneficial skill-guided action tokens. On ALFWorld and WebShop with Qwen2.5-7B-Instruct, improves GiGPO from 0.908→0.930 and 0.728→0.813.
- **Key Innovations**: Self-skill mining without external generators; trajectory-level utility + action-level advantage distillation; inference-time skill-free.
- **Tags**: `LLM`, `agents`, `reinforcement-learning`, `skill-discovery`

---

## 2. Diffusion Language Models

### FLARE: Diffusion for Hybrid Language Model

- **Authors**: Yuchen Zhu, Jing Shi, Chongjian Ge, Hao Tan, Yiran Xu, Wanrong Zhu, Jason Kuen, Koustava Goswami, Rajiv Jain, Yongxin Chen, Molei Tao, Jiuxiang Gu
- **Institution**: Not specified
- **Link**: [arXiv:2606.01774](https://arxiv.org/abs/2606.01774)
- **Abstract**: Systematic conversion framework for hybrid-attention LLMs enabling one checkpoint to support both AR-style verified decoding and diffusion-style parallel denoising. Identifies transfer data quality as primary determinant of capability preservation. Competitive with leading open-source dLLMs with limited post-training data.
- **Key Innovations**: Hybrid AR+diffusion objective; token-equal training; hardware-aware kernels for unified inference.
- **Tags**: `diffusion`, `language-model`, `hybrid-architecture`, `efficient-inference`

### SAID: Accelerating Diffusion-Based Language Models via Scaffold-Aware Iterative Decoding

- **Authors**: Na Li, Chengda Wang, Mingju Gao, Hao Tang
- **Institution**: Peking University (TH-AI-Lab-PKU)
- **Link**: [arXiv:2606.04974](https://arxiv.org/abs/2606.04974)
- **Abstract**: Reallocates denoising computation across tokens — first establishes coarse semantic structure via scaffold tokens, then completes predictable detail tokens with fewer steps. Introduces Confidence-Hierarchical Layered Generation (CHLG). Up to 9.1x speedup on LLaDA-8B/1.5 while maintaining quality.
- **Key Innovations**: Scaffold-aware computation reallocation; CHLG for confidence-based step allocation; block-wise diffusion adaptation.
- **Tags**: `diffusion`, `language-model`, `inference-acceleration`, `LLaDA`

### Diffusion Models for Adaptive Sequential Data Generation

- **Authors**: Haoyang Cao, Minshuo Chen, Yinbin Han, Renyuan Xu
- **Institution**: Not specified
- **Link**: [arXiv:2606.06007](https://arxiv.org/abs/2606.06007)
- **Abstract**: Sequential forward-backward diffusion framework for adapted time series generation. Progressively injects/removes noise along the sequence conditioning on history. Novel score-matching objective for parallel training. Statistical guarantees with ReLU networks. Validated on ARMA, GPs, and portfolio optimization.
- **Key Innovations**: Adapted (non-anticipating) sequential diffusion; rigorous statistical guarantees; score approximation/estimation results.
- **Tags**: `diffusion`, `sequential-modeling`, `time-series`, `generation`

---

## 3. Recommendation Systems & Advertising

### Bridging Short Videos and Live Streams: Reasoning-Guided Multimodal LLMs for Cross-Domain Representation Learning (RGCD-Rep)

- **Authors**: Le Zhang, Xiaolan Zhu, Yuchen Wang, Shilong Kang, Jiaqi Xue, Xiaoyu Zhang, Xiang Chen, Yalong Guan, Xiangyu Wu, Shijun Wang, Lantao Hu, Kun Gai
- **Institution**: Kuaishou
- **Link**: [arXiv:2606.04448](https://arxiv.org/abs/2606.04448)
- **Abstract**: Reasoning-guided framework for cross-domain recommendation from short videos to live streams. Uses MLLM teacher-student distillation for structured reasoning knowledge, then decomposes item representations into transferable and domain residual components. Deployed at Kuaishou serving 400M+ daily users.
- **Key Innovations**: MLLM reasoning distillation for recommendation; transferable vs domain-specific representation decomposition; large-scale industrial deployment.
- **Tags**: `recommendation`, `cross-domain`, `multimodal`, `LLM`, `live-streaming`

### Fine-Tuned LLM as a Complementary Predictor Improving Ads System

- **Authors**: Hui Yang, Daiwei He, Kevin Jiang, Taejin Park, Kungang Li, Jiajun Luo, Yuying Chen, Xinyi Zhang, Sihan Wang, Haoyu He, Yu Liu, Lakshmi Manoharan, David Xue, Shubham Barhate, Runze Su, Duna Zhan, Ling Leng, Siping Ji, Jinfeng Zhuang, Alice Wu, Leo Lu, Han Sun, Zhifang Liu
- **Institution**: Large-scale production advertising system (likely Meta/LinkedIn-scale)
- **Link**: [arXiv:2605.27856](https://arxiv.org/abs/2605.27856)
- **Abstract**: Fine-tuned open-source LLM used as an ads-specific ancillary predictor forecasting likely advertisers from user profiles/histories. Augments conventional candidate generation and provides informative priors to downstream ranking. Demonstrated offline improvements and measurable online business impact.
- **Key Innovations**: LLM as ancillary predictor (not ranker) for ads; advertiser prediction for candidate generation augmentation; end-to-end gains across retrieval and ranking.
- **Tags**: `advertising`, `LLM`, `recommendation`, `candidate-generation`

### The Injection Paradox: Brand-Level Suppression in Safety-Trained LLM Recommendations via RAG Context Injection

- **Authors**: Hyunseok Paeng
- **Institution**: Not specified
- **Link**: [arXiv:2606.09204](https://arxiv.org/abs/2606.09204)
- **Abstract**: Reveals that prompt injections in RAG contexts suppress brand recommendations in safety-trained LLMs (Claude). In Claude Opus 4.6, target brand drops from 54% baseline to zero top-2 across 50 trials with only 1/4 documents injected. GPT models instead increase recommendations — model-family differences.
- **Key Innovations**: Discovery of "Injection Paradox"; brand-level propagation of suppression; reverse-attack scenario for competitors.
- **Tags**: `RAG`, `safety`, `LLM`, `recommendation`, `adversarial`

### EviProp: Seeded Relevance Diffusion on Chunk-Page Graphs for Long Multimodal Document Retrieval

- **Authors**: Hongwei Zhang, Xiaoman Wang, Zehui Ling, Ruicheng Zhu, Yue Zhang, Pinlong Cai, Fuke Shen, Botian Shi, Tongquan Wei, Guohang Yan
- **Institution**: Not specified
- **Link**: [arXiv:2606.08979](https://arxiv.org/abs/2606.08979)
- **Abstract**: Models documents as multimodal Chunk-Page graphs with hierarchical/sequential/similarity links. Combines dense visual page priors with sparse chunk seeds, runs Personalized PageRank for relevance diffusion. Consistent gains on MMLongBench-Doc and LongDocURL.
- **Key Innovations**: Chunk-Page graph for document modeling; seeded relevance diffusion via PageRank; multimodal retrieval.
- **Tags**: `retrieval`, `document-QA`, `multimodal`, `RAG`

---

## 4. CTR Prediction

### CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer

- **Authors**: Not specified
- **Institution**: LinkedIn
- **Link**: [arXiv:2602.11410](https://arxiv.org/abs/2602.11410)
- **Abstract**: End-to-end decoder-only transformer for ads CTR deployed at LinkedIn. Introduces context-conditioned decoding with multi-tower prediction heads, self-gated attention, timestamp-based RoPE, session masking, and production engineering (tensor packing, Flash Attention). 11%+ online gains.
- **Key Innovations**: Decoder-only architecture for CTR; self-gated attention; temporal RoPE for multi-timescale patterns; train-serve skew mitigation via session masking.
- **Tags**: `CTR`, `advertising`, `transformer`, `production`

---

## 5. Games & Reinforcement Learning

### Game-RL: Synthesizing Multimodal Verifiable Game Data to Boost VLMs' General Reasoning

- **Authors**: Jingqi Tong, Jixin Tang, Hangcheng Li, Yurong Mou, Ming Zhang, Jun Zhao, Yanbo Wen, Fan Song, Jiahao Zhan, Yuyang Lu, Chaoran Tao, Zhiyuan Guo, Jizhou Yu, Tianhao Cheng, Zhiheng Xi, Changhao Jiang, Zhangyue Yin, Yining Zheng, Weifeng Ge, Guanhua Chen, Tao Gui, Xipeng Qiu, Qi Zhang, Xuanjing Huang
- **Institution**: Fudan University / multi-affiliation
- **Link**: [ICLR 2026](https://openreview.net/forum?id=e4FqU4SyHL)
- **Abstract**: Proposes Code2Logic to adapt game code for synthesizing verifiable reasoning data (GameQA: 30 games, 158 tasks). RL training on GameQA enables VLMs to generalize across 7 diverse out-of-domain vision-language benchmarks. Scaling game diversity/volume consistently improves reasoning.
- **Key Innovations**: Code2Logic for game-based synthetic data; verifiable multimodal rewards; RL training for generalizable VLM reasoning.
- **Tags**: `games`, `RL`, `VLM`, `reasoning`, `synthetic-data`

### GARL: Game-Theoretic Reinforcement Learning for Multi-Agent Strategic Prioritisation

- **Authors**: Yuxiao Ye, Yiwen Zhang, Huiyuan Xie, Yuqin Huang, Zhiyuan Liu
- **Institution**: Not specified
- **Link**: [arXiv:2606.05002](https://arxiv.org/abs/2606.05002)
- **Abstract**: Formalises strategic prioritisation as a two-stage game: competing agents allocate strategic resources over a shared candidate set, then a higher-level arbiter produces final ranking. Game-theoretic utilities converted into role-specific RL signals. Applied to legal issue ranking.
- **Key Innovations**: Game-theoretic formalization for multi-agent prioritization; role-specific reward design; small open LLMs competitive with closed-source.
- **Tags**: `game-theory`, `reinforcement-learning`, `multi-agent`, `strategic-decision`

---

## 6. Agent Systems & Memory

### Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents (MRAgent)

- **Authors**: Shuo Ji, Yibo Li, Bryan Hooi
- **Institution**: Not specified
- **Link**: [arXiv:2606.06036](https://arxiv.org/abs/2606.06036)
- **Abstract**: Combines associative memory graph (Cue-Tag-Content) with active reconstruction mechanism. LLM reasoning integrated into memory access — iteratively explores/prunes retrieval paths based on accumulated evidence. Up to 23% improvement on LoCoMo and LongMemEval benchmarks. Accepted at ICML 2026.
- **Key Innovations**: Active memory reconstruction (not static retrieval); Cue-Tag-Content graph; dynamic evidence-based retrieval path pruning.
- **Tags**: `agents`, `memory`, `graph`, `ICML-2026`

### TRACE: Trajectory Reasoning through Adaptive Cross-Step Evidence Aggregation for LLM Agents

- **Authors**: Vijitha Mittapalli, Shreyaa Jayant Dani, Satya Srujana Pilli, Snigdha Ansu, Mohammadreza Teymoorianfard, Franck Dernoncourt, Hongjie Chen, Yu Wang, Ryan A. Rossi, Nesreen K. Ahmed
- **Institution**: Adobe Research / multi-affiliation
- **Link**: [arXiv:2606.07054](https://arxiv.org/abs/2606.07054)
- **Abstract**: Monitoring framework for long-horizon LLM agent trajectories operating through a Triage-Inspect-Judge (TIJ) loop. Identifies high-signal regions, performs targeted inspection with accumulated evidence, synthesizes trajectory-level verdict. Aggregate F1 of 0.713, recall of 0.844 on SHADE-Arena.
- **Key Innovations**: TIJ loop for trajectory monitoring; cross-step evidence aggregation; detection of hidden malicious objectives.
- **Tags**: `agents`, `safety`, `monitoring`, `trajectory-analysis`

---

## 7. Benchmarks & Evaluation

### SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks

- **Authors**: Hongcheng Gao, Hailong Qu, Jingyi Tang, Jiahao Wang, Zihao Huang, Hengkang Qiao, Shihong Huang, Junming Yang, Yi Li, Hongyixuan Yuan, Wenjie Li, Bohan Zeng, Wenbo Li, Bo Wang, Jianhui Liu, Olive Huang, Haoyang Huang, Wentao Zhang, Guoqing Huang, Nan Duan, Yinpeng Dong
- **Institution**: Multi-affiliation
- **Link**: [arXiv:2606.09669](https://arxiv.org/abs/2606.09669)
- **Abstract**: Unified benchmark for interactive spatial understanding with 8 heterogeneous simulation backends, 760 human-annotated tasks. Vision-only partial observability with text-based action interface. Best model (GPT-5) achieves only 17.4% TSR; Qwen-3.5 reaches 14.1%.
- **Key Innovations**: Simulator-agnostic spatial benchmark; vision-only partial observability; terminal-state verifier for reliable evaluation.
- **Tags**: `benchmark`, `spatial-reasoning`, `multimodal`, `agents`

### Hedge-Bench: Benchmarking Agents on Hard, Realistic Tasks Pertaining to Financial Reasoning

- **Authors**: Eric Cho, Shawn Huang, Alice Lu, Andy Lyu
- **Institution**: Trata Inc.
- **Link**: [arXiv:2606.03918](https://arxiv.org/abs/2606.03918)
- **Abstract**: 102 actual on-the-job financial reasoning tasks grounded in explicit reasoning traces of professional hedge fund analysts. Deterministic grading against verified expert steps. Frontier models score below 16%.
- **Key Innovations**: Real financial analyst tasks; deterministic grading (no model-judged); open-ended reasoning evaluation.
- **Tags**: `benchmark`, `finance`, `agents`, `reasoning`

---

## Summary Table

| Category | Paper | Venue/Date | Key Contribution |
|----------|-------|-----------|------------------|
| LLM Reasoning | ACTS | Jun 2 | MDP-based CoT steering with budget control |
| RL for Agents | SIRI | Jun 1 | Self-internalizing skills without external generators |
| Diffusion LM | FLARE | Jun 1 | Hybrid AR+diffusion from pretrained checkpoints |
| Diffusion LM | SAID | Jun 3 | 9.1x speedup via scaffold-aware decoding |
| Sequential Diffusion | Diff-Seq | Jun 4 | Adapted (non-anticipating) time series generation |
| Cross-Domain Rec | RGCD-Rep | Jun 3 | MLLM reasoning distillation, Kuaishou deployment |
| Ads/LLM | LLM-Ads-Predictor | May 27 | LLM as ancillary advertiser predictor |
| RAG Safety | Injection Paradox | Jun 8 | Brand suppression via prompt injection |
| Document Retrieval | EviProp | Jun 8 | PageRank relevance diffusion on chunk-page graphs |
| CTR | CADET | Feb 11 | Decoder-only transformer for ads CTR (LinkedIn) |
| Games/RL | Game-RL | ICLR 2026 | Game-synthesized data for VLM reasoning |
| Game Theory/RL | GARL | Jun 3 | Game-theoretic RL for multi-agent prioritization |
| Agent Memory | MRAgent | ICML 2026 | Active reconstruction graph memory |
| Agent Safety | TRACE | Jun 5 | Cross-step evidence aggregation for trajectory monitoring |
| Benchmark | SpatialWorld | Jun 8 | Interactive spatial reasoning benchmark |
| Benchmark | Hedge-Bench | Jun 2 | Financial reasoning benchmark (frontier < 16%) |
