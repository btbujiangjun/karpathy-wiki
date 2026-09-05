---
title: "Conference & arXiv Daily Digest — 2026-09-05"
type: synthesis
created: 2026-09-05
updated: 2026-09-05
sources: []
tags: [conference-digest, ICML2026, AAAI2026, NeurIPS2025, ICLR2026, CVPR2026, KDD2026, ACL2026, EMNLP2025, SIGIR2026, WWW2026, CIKM2025, RecSys2025, recommendation, LLM, advertising, CTR, agents, generative-models, sequential-modeling, benchmarks, daily-digest]
---

# Conference & arXiv Daily Digest — 2026-09-05

> Cross-venue survey of recent papers from top ML/AI conferences (ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025) plus high-impact recent arXiv preprints from Google DeepMind, OpenAI, Meta, Microsoft, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, Netflix, NVIDIA, Ant Group, Salesforce, Anthropic, Apple, Amazon, and top labs. Organized by venue then category. 42 papers.

> **Scope / dedup note**: Papers already tracked in this wiki are excluded from detailed treatment — NeurIPS 2025 Best Papers (Gated Attention, Why Diffusion Models Don't Memorize, 1000-Layer RL, Artificial Hivemind → [[papers/llm-training/gated-attention]]), ICLR 2026 Outstanding "Transformers are Inherently Succinct" ([[papers/llm-training/transformers-inherently-succinct]]), KDD 2026 MixFormer ([[papers/ctr/mixformer]]) & ULTRA-HSTU ([[papers/ctr/ultra-hstu]]), LinkedIn CADET ([[papers/ctr/cadet]]), Tencent TGR (covered 2026-09-02 digest), Baidu GRAB (covered 2026-08-30 digest), NVIDIA NitroGen (covered 2026-09-03 game-rl-daily), Netflix GenRec (covered 2026-09-01 arxiv-ai-search). Kuaishou GR4AD & Meituan UniROM-family were noted in prior conference digests as industrial generative-ads anchors.

---

## 1. NeurIPS 2025 (Vancouver, Dec 2025)

### 1.1 LLM Post-Training — Fast, Scalable RL

#### TBA: Trajectory Balance with Asynchrony — Decoupling Exploration and Learning
- **Title (ZH)**: Trajectory Balance 与异步：解耦探索与学习，实现快速可扩展的 LLM 后训练
- **Authors**: Brian Bartoldson, Siddarth Venkatraman, James Diffenderfer, Moksh Jain, Tal Ben-Nun, Seanie Lee, Minsu Kim, Johan Obando-Ceron, Yoshua Bengio, Bhavya Kailkhura
- **Affiliation**: LLNL, Mila, ETH Zürich, KAIST *(inferred)*
- **Venue**: NeurIPS 2025 (Main Track)
- **Abstract & Key Innovations**: On-policy RL algorithms are not robust to the diversified replay buffers that parallel async off-policy actors fill while the learner trains — a bottleneck for scalable LLM post-training. TBA learns on such off-policy data through the principled off-policy Trajectory Balance objective, decoupling exploration from learning. Validated on math, preference tuning, and automated red-teaming across Pythia 410M → Qwen 2.5 7B: accuracy is maintained even as asynchrony grows, with reward- and recency-prioritized sampling adding gains as data generation scales.
- **Comparison with prior methods**: Beats strong baselines (Online DPO, Dr. GRPO) with ≥4× speedups; accuracy held under large asynchrony.
- **Link**: https://arxiv.org/abs/2503.18929 · Code: github.com/bbartoldson/TBA

#### Beyond the 80/20 Rule: High-Entropy Minority Tokens Drive Effective RL for LLM Reasoning
- **Title (ZH)**: 超越 80/20 法则：高熵少数 Token 驱动 LLM 推理 RL 的有效训练
- **Authors**: Shenzhi Wang, Le Yu, Chang Gao, Chujie Zheng, Shixuan Liu, Rui Lu, Kai Dang, et al.
- **Affiliation**: Tsinghua University + Alibaba Qwen Team *(inferred)*
- **Venue**: NeurIPS 2025
- **Abstract & Key Innovations**: A first *token-entropy* view of RLVR (RL from Verifiable Rewards): only a small fraction of CoT tokens exhibit high entropy and act as "forking tokens" steering reasoning pathways; RLVR largely follows the base model's entropy patterns. Restricting policy-gradient updates to forking tokens matches full-gradient performance on Qwen3-8B and *surpasses* it at scale — evidence that RLVR's efficacy comes from optimizing decision-direction tokens.
- **Comparison with prior methods**: Using only ~20% of tokens matches full-gradient updates on Qwen3-8B; Qwen3-32B +11.04 AIME'25 / +7.71 AIME'24, Qwen3-14B +4.79 AIME'25 / +5.21 AIME'24; training on the 80% lowest-entropy tokens markedly degrades.
- **Link**: https://arxiv.org/abs/2506.01939

#### Communication-Efficient Language Model Training Scales Reliably: Scaling Laws for DiLoCo
- **Title (ZH)**: 通信高效的 LLM 训练可靠扩展：DiLoCo 的 Scaling Law
- **Authors**: Zachary Charles, Gabriel Teston, Lucio Dery, Keith Rush, Nova Fallen, Zachary Garrett, Arthur Szlam, Arthur Douillard
- **Affiliation**: Google DeepMind *(inferred)*
- **Venue**: NeurIPS 2025
- **Abstract & Key Innovations**: Studies DiLoCo's scaling-law behaviour under a fixed compute budget — how model replicas, hyperparameters, and token budgets affect training predictively. DiLoCo scales predictably and robustly with model size, and well-tuned small models already beat data-parallel. Demonstrates benefits beyond earlier work: larger optimal batch sizes, better downstream generalization with scale, and improved eval loss per token budget.
- **Comparison with prior methods**: Prior DiLoCo work did not analyze size-dependence; this shows it *beats data-parallel training at both small and large scale* under scaling-law-characterized tuning.
- **Link**: https://arxiv.org/abs/2503.09799

#### RetrievalAttention: Accelerating Long-Context LLM Inference via Vector Retrieval
- **Title (ZH)**: RetrievalAttention：通过向量检索加速长上下文 LLM 推理
- **Authors**: Di Liu, Meng Chen, Baotong Lu, Huiqiang Jiang, Zhenhua Han, Qianxi Zhang, Qi Chen, et al.
- **Affiliation**: Microsoft Research *(inferred; MSR Asia)*
- **Venue**: NeurIPS 2025 (Main Track)
- **Abstract & Key Innovations**: A training-free approach exploiting attention's dynamic sparsity: build ANNS indexes over KV vectors in CPU memory and retrieve only the most relevant keys at generation. Addresses the out-of-distribution problem between query/key vectors (off-the-shelf ANNS fails) with an attention-aware vector search algorithm. Near full-attention accuracy while accessing only 1–3% of data; a single RTX 4090 (24GB) serves an 8B LLM at 128K context with 0.188 s/token.
- **Comparison with prior methods**: Prior KV-compression/sparsity methods keep large GPU KV footprints; RetrievalAttention offloads to CPU + ANNS and sharply cuts GPU memory for long contexts.
- **Link**: https://arxiv.org/abs/2409.10516

### 1.2 Generative Models / Video

#### Blockwise Flow Matching (BFM)
- **Title (ZH)**: 块式 Flow Matching（BFM）：生成轨迹分段专用化的高效高质量生成
- **Authors**: Dogyun Park, Taehoon Lee, Minseok Joo, Hyunwoo J. Kim
- **Affiliation**: Korea University (mlvlab)
- **Venue**: NeurIPS 2025 (poster)
- **Abstract & Key Innovations**: Partitions the noise→data trajectory into M temporal segments, each modeled by a smaller specialized velocity block (MoE-with-fixed-router view) that captures interval-specific signal spectra instead of a single model handling all timesteps. Adds Semantic Feature Guidance and Feature Residual Approximation.
- **Comparison with prior methods**: ImageNet 256×256 — 2.1×–4.9× inference acceleration at comparable/better quality vs SiT/REPA; 512×512 beats SiT baseline by 14.69 FID; training FLOPs ≈ SiT/REPA.
- **Link**: https://arxiv.org/abs/2510.21167

#### GPDiT: Generative Pre-trained Autoregressive Diffusion Transformer
- **Title (ZH)**: 生成式预训练自回归扩散 Transformer（GPDiT）
- **Authors**: Yuan Zhang, Jiacheng Jiang, Guoqing Ma, Zhiying Lu, Bo Wang, Haoyang Huang, Jianlong Yuan, Nan Duan, Daxin Jiang
- **Affiliation**: USTC + StepFun
- **Venue**: NeurIPS 2025 (poster)
- **Abstract & Key Innovations**: Unifies AR + diffusion for video in the continuous latent space: frame-wise autoregressive next-frame prediction under a diffusion loss, with intra-frame full / inter-frame causal attention. Two efficiency wins: a lightweight causal-attention variant that drops clean-frame×clean-frame attention (~half training compute) and a parameter-free rotation-based time conditioning replacing adaLN-Zero (~30% of params).
- **Comparison with prior methods**: MSR-VTT FID 7.4 / FVD 68 (GPDiT-H); UCF-101 GPDiT-H-LONG IS 66.6 / FID 7.9 / FVD 218; 80M-param variants reach FVD 214–216, outdoing DiT/SiT-class hybrids while generalizing beyond training lengths.
- **Link**: https://arxiv.org/abs/2505.07344

#### DiffTrack: Emergent Temporal Correspondences from Video Diffusion Transformers
- **Title (ZH)**: 视频扩散 Transformer 中涌现的时序对应（DiffTrack）
- **Authors**: Jisu Nam, Soowon Son, Dahyun Chung, Jiyoung Kim, Siyoon Jin, Junhwa Hur, Seungryong Kim
- **Affiliation**: KAIST CVLab
- **Venue**: NeurIPS 2025 (poster)
- **Abstract & Key Innovations**: First quantitative analysis of how video DiTs establish temporal correspondences: constructs a prompt-generated-video dataset with pseudo-GT tracking and new metrics; finds query–key similarity in specific (not all) layers drives temporal matching, strengthening during denoising. Yields state-of-the-art zero-shot point tracking and training-free motion-enhanced generation via Cross-Attention Guidance.
- **Comparison with prior methods**: Beats vision foundation models (DINO/DINOv2/DIFT/SD) and self-supervised video models (SMTC/CRW/SVD/ZeroCo) on TAP-Vid DAVIS & Kinetics; tested on CogVideoX-2B/5B, HunyuanVideo.
- **Link**: https://arxiv.org/abs/2506.17220

---

## 2. ICML 2026

### 2.1 Outstanding Paper Awards

#### The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models (**Outstanding Paper**)
- **Title (ZH)**: 灵活性陷阱：重新审视 Diffusion 语言模型中任意顺序的价值
- **Authors**: Zanlin Ni, Shenzhi Wang, Yang Yue, Tianyu Yu, Weilin Zhao, Yeguo Hua, Tianyi Chen, Jun Song, Cheng Yu, Bo Zheng, Gao Huang
- **Affiliation**: Tsinghua University (LeapLab) + Alibaba *(inferred)*
- **Venue**: ICML 2026 — **Outstanding Paper Award**
- **Abstract & Key Innovations**: Challenges the assumption that arbitrary-order generation strictly supersets the autoregressive trajectory for reasoning ability. dLLMs exploit order flexibility to *bypass* high-uncertainty (critical-exploration) tokens, collapsing solution coverage early. Fix: drop arbitrary order entirely and apply standard GRPO — "JustGRPO" hits 89.1% on GSM8K while keeping parallel decoding.
- **Comparison with prior methods**: Prior non-AR RL methods paid steep complexity (combinatorial trajectories, intractable likelihoods) to preserve flexibility; JustGRPO shows plain GRPO matches/surpasses them at a fraction of the complexity.
- **Link**: https://arxiv.org/abs/2601.15165

#### High-accuracy sampling for diffusion models and log-concave distributions (**Outstanding Paper**)
- **Title (ZH)**: Diffusion 模型与 log-concave 分布的高精度采样
- **Authors**: Fan Chen, Sinho Chewi, Constantinos Daskalakis, Alexander Rakhlin
- **Affiliation**: MIT
- **Venue**: ICML 2026 — **Outstanding Paper Award**
- **Abstract & Key Innovations**: New diffusion-model sampling algorithms achieving δ-error in polylog(1/δ) steps given Õ(δ)-accurate L² score estimates — an exponential improvement over all previous results. Complexity is Õ(d⋆ polylog(1/δ)) where d⋆ is the intrinsic dimension, or Õ(L polylog(1/δ)) under a non-uniform L-Lipschitz condition; also the first polylog(1/δ)-step sampler for general log-concave distributions using only gradient evaluations.
- **Comparison with prior methods**: Prior samplers needed poly(1/δ) steps; this is the first exponential (polylog) step-count improvement.
- **Link**: https://arxiv.org/abs/2602.01338

### 2.2 LLM Alignment & Memorization

#### DPO Unchained: Your Training Algorithm is Secretly Disentangled in Human Choice Theory
- **Title (ZH)**: DPO Unchained：训练算法在人选择理论中本质上解耦，且损失凸性并非必需
- **Authors**: Wenxuan Zhou, Shujian Zhang, Brice Magdalou, John Lambert, Ehsan Amid, Richard Nock, Andrew Hard
- **Affiliation**: Google *(inferred)*
- **Venue**: ICML 2026
- **Abstract & Key Innovations**: Elevates DPO's implicit link to human choice theory to full generality by reworking the textbook choice-theory path for RLHF. Shows any compliant ML analytical choice can be embedded with any human choice model, and formally supports non-convex losses (dispensable convexity). Provides a normative umbrella covering DPO extensions (margins, length correction).
- **Comparison with prior methods**: Generalizes the DPO follow-up panorama (centered DPO, length-normalized variants) under one normative framework rather than ad-hoc modifications.
- **Link**: https://arxiv.org/abs/2507.07855

#### How much do language models memorize?
- **Title (ZH)**: 语言模型究竟记忆了多少？
- **Authors**: John X. Morris, Chawin Sitawarin, Chuan Guo, Narine Kokhlikyan, G. Edward Suh, Alexander M. Rush, Kamalika Chaudhuri, Saeed Mahloujifar
- **Affiliation**: Cornell / Google DeepMind / OpenAI / Meta mix *(inferred per-author)*
- **Venue**: ICML 2026 (oral — LLMs)
- **Abstract & Key Innovations**: A new estimator quantifying how much a model knows about a datapoint, separating *unintended memorization* (dataset-specific) from *generalization* (data-generation-process). Zeroing out generalization yields total memorization = capacity estimate: GPT-style models hold ≈3.6 bits per parameter. Models memorize until capacity fills, then "grokking" begins and unintended memorization falls. Studied across hundreds of transformers (500K–1.5B params) with scaling laws linking capacity/data size to membership inference.
- **Comparison with prior methods**: Earlier memorization studies conflated memorization with generalization; this provides the first clean decomposition and per-parameter capacity estimate.
- **Link**: https://arxiv.org/abs/2505.24832

### 2.3 Generative Video (acceptance via arXiv tags — some unverified)

#### Mode Seeking meets Mean Seeking for Fast Long Video Generation
- **Title (ZH)**: 模式匹配遇上均值匹配：快速长视频生成
- **Authors**: Shengqu Cai, Weili Nie, Chao Liu, Julius Berner, Lvmin Zhang, Nanye Ma, Hansheng Chen, Maneesh Agrawala, Leonidas Guibas, Gordon Wetzstein, Arash Vahdat
- **Affiliation**: Stanford University · NVIDIA Research · NYU Courant
- **Venue**: ICML 2026 *(acceptance not independently confirmed)*
- **Abstract & Key Innovations**: Decouples long-horizon coherence from local realism under scarce long-video data via a Decoupled Diffusion Transformer: shared long-context encoder + two heads — a mean-seeking Flow-Matching head (SFT on real long videos → minute-scale narrative structure) and a mode-seeking Distribution-Matching head (DMD/VSD-style sliding-window reverse-KL alignment to a frozen short-video teacher → local sharpness). At inference the DM head is a fast few-step generator.
- **Comparison with prior methods**: Builds on Wan 1.3B/14B; closes the fidelity–horizon gap per automatic metrics, human ratings, and one-minute stress tests; head-decoupling resolves the mean-seeking/mode-seeking conflict.
- **Link**: https://arxiv.org/abs/2602.24289

#### FAST-AR: Fast Autoregressive Video Diffusion and World Models with Temporal Cache Compression and Sparse Attention
- **Title (ZH)**: FAST-AR：基于时序 KV 缓存压缩与稀疏注意力的快速自回归视频扩散与世界模型
- **Authors**: Dvir Samuel, Issar Tzachor, Matan Levy, Michael Green, Gal Chechik, Rami Ben-Ari
- **Affiliation**: OriginAI · Bar-Ilan University · Hebrew University of Jerusalem · NVIDIA (Tel-Aviv)
- **Venue**: ICML 2026 (poster)
- **Abstract & Key Innovations**: Fully training-free attention acceleration for AR video diffusion. Three modules: TempCache (merges temporally-corresponding duplicate keys → bounded KV cache), AnnCA (ANN-based cross-attention prompt-token pruning), AnnSA (ANN-based sparse self-attention). Up to ×5–×10 end-to-end speedups with near-constant throughput & memory over 3000-frame rollouts.
- **Comparison with prior methods**: Full system reaches ×10.7–×10.8 end-to-end speedup at VBench ≈ 84.1 (dense FA3 = 84.08), KV density ~16% with ~90–91% recall; best prior baseline combo (FlowCache+RadialAttn) only ×4.4 with quality collapse; on world-model LongVie2 ×6.3–×6.9 with LongVGenBench 63.69–64.91 vs 49.84 for the best baseline.
- **Link**: https://arxiv.org/abs/2602.01801

#### Flex-Forcing: Towards a Unified Autoregressive and Bidirectional Video Diffusion Model
- **Title (ZH)**: Flex-Forcing：统一的 Autoregressive 与双向视频扩散模型
- **Authors**: Xinyin Ma, Julius Berner, Chao Liu, Arash Vahdat, Weili Nie, Xinchao Wang
- **Affiliation**: NVIDIA Research + National University of Singapore
- **Venue**: ICML 2026 (spotlight)
- **Abstract & Key Innovations**: One model operating bidirectionally, autoregressively, or anywhere in between at inference. Flexible chunking is defined jointly over the temporal axis and denoising steps, so a single checkpoint becomes a quality/efficiency dial; a K-Projection aligns causal vs non-causal attention contexts of differing noise levels. Unlocks any-order, any-timestep AR editing. Post-trains Wan2.1-T2V-1.3B (14B teacher) on VidProM.
- **Comparison with prior methods**: Pareto-optimal hybrid coarse-to-fine chunking beats uniform chunks and Self-Forcing on both FPS (GB200) and VBench/VBench-Long; at 1.3B reports VBench >85 at 25–50 FPS, outpacing few-step distilled bidirectional baselines under matched NFE.
- **Link**: https://arxiv.org/abs/2607.03509

---

## 3. ICLR 2026 (Rio de Janeiro, Apr 2026)

### 3.1 Agents & Long-Context

#### LLMs Get Lost In Multi-Turn Conversation (**Outstanding Paper Award**)
- **Title (ZH)**: LLM 在多轮对话中迷失方向
- **Authors**: Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville
- **Affiliation**: Microsoft Research + Salesforce Research
- **Venue**: ICLR 2026 — **Outstanding Paper Award** (Oral)
- **Abstract & Key Innovations**: Underspecified instructions dominate real usage, yet evaluation focuses on single-turn fully-specified settings. Large-scale simulation across top open- and closed-weight LLMs shows significant multi-turn degradation. Decomposes the loss into a minor aptitude loss plus a large unreliability increase — models make early assumptions, prematurely emit final answers, and over-rely on them ("get lost and do not recover").
- **Comparison with prior methods**: Average performance drop of 39% vs single-turn across six generation tasks (200,000+ simulated conversations); known remediations (agent-style concatenation, lower temperature) are *ineffective* in multi-turn.
- **Link**: https://arxiv.org/abs/2505.06120

### 3.2 Video Generation

#### Video-GPT via Next Clip Diffusion
- **Title (ZH)**: 基于"下一片段扩散"（Next Clip Diffusion）的 Video-GPT
- **Authors**: Shaobin Zhuang, Zhipeng Huang, Ying Zhang, Fangyikang Wang, Canmiao Fu, Binxin Yang, Chong Sun, Chen Li, Yali Wang
- **Affiliation**: SJTU · WeChat Vision (Tencent) · USTC · ZJU · SIAT CAS · Shanghai AI Lab
- **Venue**: ICLR 2026 (poster)
- **Abstract & Key Innovations**: Treats a clip as a "word": self-supervised pretraining on 70M unlabeled videos (Panda) via next-clip diffusion — parallel intra-clip denoising + inter-clip AR conditioning. One naive Transformer handles short-term generation and long-term prediction, transferring to 6 downstream video tasks.
- **Comparison with prior methods**: Physics-IQ 34.97 vs Kling 23.64 / Wan2.1 20.89 / VideoPoet 29.50; Kinetics-600 FVD 89.44 vs Seine 91.08; paradigm ablation: next-token → next-clip diffusion jumps Physics-IQ 21.59 → 34.94.
- **Link**: https://arxiv.org/abs/2505.12489

#### Lumos-1: Autoregressive Video Generation with Discrete Diffusion from a Unified Model Perspective
- **Title (ZH)**: Lumos-1：统一模型视角下基于 Discrete Diffusion 的自回归视频生成
- **Authors**: Hangjie Yuan, Weihua Chen, Jun Cen, Hu Yu, Jingyun Liang, et al.
- **Affiliation**: Alibaba DAMO Academy
- **Venue**: ICLR 2026 (poster)
- **Abstract & Key Innovations**: Pure-LLM unified AR video generator (standard Llama + QK-Norm, no external text encoder). Two contributions: MM-RoPE (distributed 3D RoPE fixing imbalanced frequency spectra of naive 3D RoPE) and AR-DF (Autoregressive Discrete Diffusion Forcing — temporal-tube masking fixing frame-wise loss imbalance; inference-time partial-observation masking keeps train/test consistent). Cosmos discrete tokenizer (8×8×4), 0.5B/1B/3B.
- **Comparison with prior methods**: With only 48 GPUs (60M images + 10M videos): outperforms Show-o2 on GenEval (0.791 @3.6B vs 0.76), COSMOS-Video2World on VBench-I2V (84.72 vs 84.16), OpenSoraPlan on VBench-T2V; beats VideoMAR 1.4B on compute efficiency and EMU3 (8B) on T2I.
- **Link**: https://arxiv.org/abs/2507.08801

---

## 4. AAAI 2026 (Singapore, Jan 2026)

### 4.1 Outstanding Paper Awards & Notable

#### LLM2CLIP: Powerful Language Model Unlocks Richer Cross-Modality Representation (**Outstanding Paper**)
- **Title (ZH)**: LLM2CLIP：强大语言模型解锁更丰富的跨模态表示
- **Authors**: Weiquan Huang, Aoqi Wu, Yifan Yang, Xufang Luo, Yuqing Yang, Usman Naseem, Chunyu Wang, et al.
- **Affiliation**: Microsoft *(inferred; MSR Asia lead)*
- **Venue**: AAAI 2026 — **Outstanding Paper Award**
- **Abstract & Key Innovations**: Embeds a full LLM into pretrained CLIP at roughly standard fine-tuning cost, coupling it to the vision encoder via a lightweight adapter trained on only a few million image–caption pairs. LLM-enhanced CLIP improves linear-probe classification, zero-shot retrieval (short/long captions, multilingual), zero-shot/supervised segmentation, object detection, and serves as a tokenizer backbone for multimodal LLM benchmarks.
- **Comparison with prior methods**: Outperforms state-of-the-art CLIP variants (EVA02, SigLIP-2) on these tasks without large-scale retraining.
- **Link**: https://arxiv.org/abs/2411.04997

#### ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver (**Outstanding Paper**)
- **Title (ZH)**: ReconVLA：重建式 Vision-Language-Action 模型作为高效机器人感知器
- **Authors**: Wenxuan Song, Ziyang Zhou, Han Zhao, Jiayi Chen, Pengxiang Ding, Haodong Yan, Yuxin Huang, Feilong Tang, Donglin Wang, Haoang Li
- **Affiliation**: HKUST (Guangzhou) + Westlake University + Zhejiang University + Monash University
- **Venue**: AAAI 2026 — **Outstanding Paper Award**
- **Abstract & Key Innovations**: Finding that current VLAs disperse visual attention rather than grounding it on target regions. Fix: implicit grounding — a diffusion transformer reconstructs the "gaze region" around the manipulated object conditioned on the VLA's visual outputs. Built a pretraining dataset of 100K+ trajectories / 2M samples; shows precise manipulation and strong generalization to unseen objects in sim and real world.
- **Comparison with prior methods**: CALVIN ABC→D average subtask length 3.95; the hard "stack block" task jumps from 59.3% (baseline) to 79.5% (+20.2%).
- **Link**: https://arxiv.org/abs/2508.10333

#### LLM Collaboration with Multi-Agent Reinforcement Learning (MAGRPO)
- **Title (ZH)**: 基于多智能体强化学习的 LLM 协作（MAGRPO）
- **Authors**: Shuo Liu, Tianle Chen, Zeyu Liang, Xueguang Lyu, Christopher Amato
- **Affiliation**: Northeastern University *(inferred)*
- **Venue**: AAAI 2026
- **Abstract & Key Innovations**: Positions LLM collaboration as a cooperative MARL problem instead of independent per-agent fine-tuning. Introduces Multi-Agent Group Relative Policy Optimization (MAGRPO) — a multi-agent, multi-turn algorithm giving a group-level reward so agents learn to coordinate rather than chase individual rewards requiring complex design. Validated on writing and coding collaboration.
- **Comparison with prior methods**: Prior LLM fine-tuning relied on individual rewards per agent; MAGRPO needs only a group-level signal and yields higher-quality coordinated responses.
- **Link**: https://arxiv.org/abs/2508.04652

---

## 5. CVPR 2026

### 5.1 Long & Scalable Video Generation

#### Flowception: Temporally Expansive Flow Matching for Video Generation
- **Title (ZH)**: 时序扩张 Flow Matching 视频生成（Flowception）
- **Authors**: Tariq Berrada Ifriqi, John Nguyen, Karteek Alahari, Jakob Verbeek, Ricky T. Q. Chen
- **Affiliation**: Meta (GenAI/FAIR) + INRIA
- **Venue**: CVPR 2026 (pp. 16185–16195)
- **Abstract & Key Innovations**: Non-autoregressive, variable-length video generation. Learns a probability path that interleaves discrete frame insertions with continuous frame denoising — a coupled ODE-jump process. Reduces training FLOPs ~3×, is amenable to local attention, learns video length jointly with content, and unifies T2V / I2V / video interpolation in one model.
- **Comparison with prior methods**: I2V @256px 145 frames — Kinetics-600 FVD 164.73 vs Full-Seq 204.65 / AR 201.34; RealEstate10K FVD 21.80 vs 26.17 / 47.48; Tai-Chi-HD 25.21 vs 27.30 / 25.30. Learned insertion-rate beats random (25.03) / hierarchical (23.94) / left-to-right (23.61) schemes on RealEstate10K.
- **Link**: https://arxiv.org/abs/2512.11438 · Code: facebookresearch/flowception

#### Infinity-RoPE: Long-Term Tokens Unlock Real Infinity Size for Multi-Modal Deep Language Models
- **Title (ZH)**: Infinity-RoPE：解锁多模态模型真正无限长度的长上下文视觉生成
- **Authors**: Volkan Yesiltepe, Fatma Betul Meral, Batuhan Akan, Ziya Ata Yazici, Yusuf Hakan Kalayci, Erkut Erdem, Aykut Erdem, Hamza Erdem, Mustafa Merter Cengiz, Yalcin Kaya
- **Affiliation**: Virginia Tech, fal.ai *(inferred)*
- **Venue**: CVPR 2026
- **Abstract & Key Innovations**: Makes long-term generation in vision-language models practical. Introduces KV Flush, RoPE Cut, and Block-Relativistic RoPE position updates to extend effective context far beyond the ~1024-frame base limit, enabling coherent long autoregressive video generation.
- **Comparison with prior methods**: Overcomes the standard RoPE 1024-position window limitation that blocks longer inference; quantitative benchmarks single-source — treat headline numbers cautiously.
- **Link**: https://arxiv.org/abs/2511.20649

#### LoL: Longer than Longer, Scaling Video Generation to Hour
- **Title (ZH)**: LoL：更长的更长——将视频生成扩展到小时级
- **Authors**: Justin Cui, Jie Wu, Ming Li, Tao Yang, Xiaojie Li, Rui Wang, Andrew Bai, Yuanhao Ban, Cho-Jui Hsieh
- **Affiliation**: UCLA + ByteDance Seed *(inferred — confirm)*
- **Venue**: CVPR 2026 (pp. 38132–38142)
- **Abstract & Key Innovations**: Diagnoses sink-collapse in AR video models (content reverts to attention-sink frames): root cause is RoPE periodicity × multi-head attention homogenization. Proposes Multi-Head RoPE Jitter — a training-free per-head base-frequency perturbation — plus streaming RoPE/noise sampling and causal 3D VAE sliding-window decoding. Demonstrates 12-hour continuous videos at 20 fps on a single H100 — among the longest public results.
- **Comparison with prior methods**: Sink-Collapse max drops 73.06 → 16.67 (LongLive) and 68.07 → 22.70 (Self-Forcing++), reaching near-PI levels while preserving dynamic degree (PI/YaRN freeze motion ~90%↓; NTK/RIFLEx keep motion but collapse scores stay 41–71).
- **Link**: https://arxiv.org/abs/2601.16914

#### DynamicsBoost: Dynamic Plausible Video Generation via Annotation-Free Continuation Preference Optimization
- **Title (ZH)**: DynamicsBoost：通过免标注续帧偏好优化的动态可信视频生成
- **Authors**: Jiaxing Li, Jiepeng Wang, Junyao Gao, Yang Liu, Eric Yangguang Li, Bo An, Hao-Xiang Guo
- **Affiliation**: NTU + Shanghai AI Lab *(inferred)*
- **Venue**: CVPR 2026 (pp. 20024–20033)
- **Abstract & Key Innovations**: Replaces human/VLM video-preference annotation with a free signal: video continuation length. For fixed total length, a continuation conditioned on more real frames is always higher quality (monotonic in VBench/VideoReward), so preference pairs are auto-constructed. New Asymmetrical DPO computes the preference loss only on diverging continuation regions (masking the shared prefix) and normalizes by length.
- **Comparison with prior methods**: Beats DPO / Flow-DPO / Flow-StructuralDPO / Flow-DenseDPO on motion realism, temporal coherence, and text alignment with zero human labels or reward models. Ablations: loss on the shared prefix (standard DPO) consistently hurts (Overall 25.64 → 22.15).
- **Link**: https://openaccess.thecvf.com/content/CVPR2026/html/Li_DynamicsBoost_Dynamic_Plausible_Video_Generation_via_Annotation-Free_Continuation_Preference_Optimization_CVPR_2026_paper.html

---

## 6. ACL 2026 (San Diego, Jul 2026)

### 6.1 Best Papers

#### Characterizing the Expressivity of Local Attention in Transformers (**Best Paper**)
- **Title (ZH)**: 刻画 Transformer 中局部注意力（Local Attention）的表达力
- **Authors**: Jiaoda Li, Ryan Cotterell
- **Affiliation**: ETH Zürich
- **Venue**: ACL 2026 **Best Paper** (2026.acl-long.1739)
- **Abstract & Key Innovations**: Theoretical characterization of which functions Transformer layers with only local attention can express — clarifying the capability boundary of local (sparse) attention vs global attention and providing theoretical grounding for efficient sparse-attention architectures.
- **Comparison with prior methods**: vs standard global attention — proves local attention expresses relevant computation on certain input classes (theory-first result).
- **Link**: https://aclanthology.org/2026.acl-long.1739/

#### HSCodeComp: Hierarchy-Aware Agentic Code Benchmark (**Best Paper**)
- **Title (ZH)**: HSCodeComp：面向层级规则的专家级智能体代码基准
- **Authors**: Tian Lan, Yiqian Yang, Qianghuai Jia, Li Zhu, Hui Jiang, Hang Zhu, Weihua Luo, Longyue Wang
- **Affiliation**: Tencent AI Lab *(inferred)*
- **Venue**: ACL 2026 **Best Paper**
- **Abstract & Key Innovations**: A realistic, expert-level agentic code-generation benchmark focusing on hierarchical rule application and compliance. Existing code benchmarks are function- or issue-level; HSCodeComp measures an agent's ability to program autonomously under complex multi-level constraints.
- **Comparison with prior methods**: vs HumanEval / SWE-bench — specifically measures hierarchical rule-following ability.
- **Link**: https://2026.aclweb.org/program/best_papers/

### 6.2 Agents & Reasoning

#### KARL: Knowledge-Augmented Reinforcement Learning for LLM Agents
- **Title (ZH)**: KARL：面向 LLM 智能体的知识增强强化学习框架
- **Authors**: Tianyu Liu, et al. (THUDM)
- **Affiliation**: Tsinghua University / Zhipu AI *(inferred from THUDM GitHub)*
- **Venue**: ACL 2026 (Long, 2026.acl-long.2196)
- **Abstract & Key Innovations**: LLM agents on knowledge-intensive tasks are limited by passive knowledge use. KARL makes agents actively decide when and what structured knowledge to fetch during task execution, using online RL + curiosity-driven reward shaping, end-to-end optimizing tool-use behavior. SOTA on six structured-knowledge benchmarks; its Qwen2.5-14B agent significantly beats GPT-4o, Claude-4, and o4-mini on knowledge-graph and database tasks.
- **Comparison with prior methods**: vs RAG — proactive knowledge exploration instead of passive retrieval; a 14B model surpasses large closed models (exact scores in paper tables).
- **Link**: https://aclanthology.org/2026.acl-long.2196/

#### rSIM: Reinforced Strategy Injection for Reasoning Language Models
- **Title (ZH)**: rSIM：通过强化策略注入激励 LLM 推理能力
- **Authors**: Chien-Ping Chen, et al. (AgenticFinLab)
- **Affiliation**: AgenticFinLab *(inferred)*
- **Venue**: ACL 2026 (Long, 2026.acl-long.2054)
- **Abstract & Key Innovations**: RL post-training shapes Reasoning LMs; the "aha moment" comes from strategies emerging in CoT. rSIM uses a leader-follower dual-agent structure: a small planner (leader) trained via multi-agent RL jointly injects reasoning strategies into the LLM's (follower's) CoT with a simple rule-based reward. The planner is trained once and used as a plug-and-play plugin across models.
- **Comparison with prior methods**: Qwen2.5-0.5B + rSIM significantly outperforms Qwen2.5-14B on math, programming, and financial reasoning; ASPM-style methods require per-model fine-tuning, while rSIM transfers after a single training.
- **Link**: https://aclanthology.org/2026.acl-long.2054/

---

## 7. EMNLP 2025 (Suzhou, Nov 2025)

#### Infini-gram mini: Exact n-gram Search at the Internet Scale with FM-Index (**Best Paper**)
- **Title (ZH)**: Infini-gram mini：基于 FM-Index 的互联网规模精确 n-gram 检索
- **Authors**: Hao Xu, Jiacheng Liu, Yejin Choi, Noah A. Smith, Hannaneh Hajishirzi
- **Affiliation**: University of Washington / Allen Institute for AI (AI2)
- **Venue**: EMNLP 2025 **Best Paper** (2025.emnlp-main.34)
- **Abstract & Key Innovations**: Scales exact n-gram co-occurrence retrieval to internet-scale corpora. A compressed FM-index lets models query n-gram counts exactly and efficiently from very large corpora, solving the index-too-large problem that blocked n-gram model scaling. Foundational infrastructure for combining LLMs with classical n-gram statistics.
- **Comparison with prior methods**: Prior n-gram scaling was memory-bound; the FM-index version sharply compresses the index (ratio in paper).
- **Link**: https://aclanthology.org/2025.emnlp-main.34/

#### Parallel Continuous Chain-of-Thought with Jacobi Iteration
- **Title (ZH)**: 基于 Jacobi 迭代的并行连续链式推理（Parallel Continuous CoT）
- **Authors**: Haoyi Wu, Zhihao Teng, Kewei Tu
- **Affiliation**: ShanghaiTech University *(inferred)*
- **Venue**: EMNLP 2025 (Long, 2025.emnlp-main.47)
- **Abstract & Key Innovations**: Traditional CoT generates tokens serially, limiting inference speed. Continuous latent reasoning is advanced via Jacobi iterations so multiple reasoning steps update in parallel within a single pass, significantly accelerating reasoning-chain computation.
- **Comparison with prior methods**: vs serial CoT — parallel Jacobi iteration with measured acceleration in the paper.
- **Link**: https://aclanthology.org/2025.emnlp-main.47/

---

## 8. KDD 2026 (Jeju, Aug 2026)

### 8.1 Advertising & CTR

#### GOAL: Generative Optimization for Incentivized Advertising with Global Level Constraints
- **Title (ZH)**: GOAL：带全局约束的激励广告生成式优化
- **Authors**: Gege Chen, Ning Luo, Hao Jiang, Da Li, Wenzheng Shu, Teng Sha, Yanxiang Zeng, Wenxin Tai, Fan Zhou, Xialong Liu
- **Affiliation**: Kuaishou Technology + UESTC
- **Venue**: KDD 2026
- **Abstract & Key Innovations**: Incentivized advertising must decide continuous reward magnitudes (e.g., 1–3000 coins) under strict global ROI constraints, with non-Markovian user dynamics such as fatigue; uplift modeling and constrained RL both struggle. GOAL recasts incentive allocation as conditional sequence generation over a data-driven quantized token vocabulary, using a hierarchical causal encoder (dilated causal conv + attention) and λ-conditioned decoding. Safe Constrained Policy Optimization (SCPO) trains one policy over a distribution of Lagrange multipliers, so a single model adapts to arbitrary ROI targets at inference without retraining.
- **Comparison with prior methods**: Beats DT/CDT (generative), IQL (offline RL), and CAL/TREBI (constrained RL) on revenue, ROI, and ROI-violation rate. 4-week online A/B (65% users/group) on Kuaishou's incentive ad system: +2.184% ROI and +2.559% revenue (p=0.03), no adverse effects on dwell time or DAU.
- **Link**: https://arxiv.org/abs/2608.04421

#### CTR-Sink: Attention Sink for Language Models in Click-Through Rate Prediction
- **Title (ZH)**: CTR-Sink：点击率预测中语言模型的注意力汇聚点机制
- **Authors**: Zixuan Li, Binzong Geng, Jing Xiong, Yong He, Yuxuan Hu, Jian Chen, et al.
- **Affiliation**: Ant Group + University of Hong Kong / others
- **Venue**: KDD 2026
- **Abstract & Key Innovations**: LM-based CTR models treat user behavior sequences as text, but discrete actions separated by semantically-empty tokens lack the natural-language attention structure the LM was pretrained on ("semantic fragmentation"). CTR-Sink inserts behavior-level [SINK] tokens carrying recommendation-specific signals (temporal distance, semantic similarity) between behaviors so attention concentrates on meaningful boundaries; two-stage training objective + a sink-specific attention mechanism amplify inter-sink dependencies while preserving pretrained capability.
- **Comparison with prior methods**: Temporal [SINK] lifts AUC by +0.46% (industrial dataset), +0.28% (MovieLens), +0.59% (KuaiRec) over LM-CTR baselines across RoBERTa and Qwen backbones; random sink tokens give negligible/negative effect.
- **Link**: https://arxiv.org/abs/2508.03668

> **Note**: KDD 2026 industrial papers already tracked in this wiki include Alibaba SORT-vs-family scaling ([[papers/ctr/est]], [[papers/ctr/fat-ctr-scaling]]), Tencent RankUp ([[papers/ctr/rankup-advertising]]), Kuaishou GR4AD, ByteDance MixFormer ([[papers/ctr/mixformer]]), Meta ULTRA-HSTU ([[papers/ctr/ultra-hstu]]), RankElastor ([[papers/recommendation/rankelastor-recommendation]]).

---

## 9. SIGIR 2026 (Melbourne, Jul 2026)

#### GenRec: A Preference-Oriented Generative Framework for Large-Scale Recommendation
- **Title (ZH)**: GenRec：面向偏好的大规模推荐生成式框架
- **Authors**: Yanyan Zou, Junbo Qi, Lunsong Huang, Yu Li, Kewei Xu, Jiabao Gao, Binglei Zhao, Xuanhua Yang, Sulong Xu, Shengjie Li
- **Affiliation**: JD (deployed on JD App)
- **Venue**: SIGIR 2026 (short)
- **Abstract & Key Innovations**: Scaling generative retrieval (GR) to industry hits three problems: pagination (identical inputs map to multiple valid outputs), expensive multi-token SID encoding of long histories, and naive RL alignment causing reward hacking. GenRec is a single decoder-only GR model using Page-wise NTP training (dense supervision over a whole interaction page) with Multimodal SIDs (multimodal encoder + RQ-K-means tokens) and GRPO-SR (GRPO with NLL supervised regularization for stable preference alignment).
- **Comparison with prior methods**: Asymmetric Token Merger compresses multi-token SIDs in the prompt, cutting prefilling input length ~2× with negligible loss. Full deployment on the JD App shows the differentiable paradigm significantly outperforms the multi-stage retrieve-and-rank pipeline.
- **Link**: https://arxiv.org/abs/2604.14878

#### L2Rec: Towards Dual-View Understanding of LLMs for Personalized Recommendation
- **Title (ZH)**: L2Rec：面向个性化推荐的 LLM 双视角理解
- **Authors**: Pingjun Pan, Tingting Zhou, Peiyao Lu, Tingting Fei, Hongxiang Chen, Chuanjiang Luo
- **Affiliation**: Not stated — *(inferred)* unnamed large-scale social platform (~1.5M DAU homepage feed)
- **Venue**: SIGIR 2026
- **Abstract & Key Innovations**: LLM4Rec methods fuse behavioral and semantic signals at input/output level, suffering distribution gaps and missing end-to-end supervision. L2Rec unifies both views inside the LLM's parameters: a Dual-view Personalized Mixture-of-Experts (DPMoE) routes per-user LoRA-based experts (semantic pathway + behavioral pathway) over a shared frozen backbone, with Adaptive Cross-View Fusion. Only ~32M params trained on frozen Qwen3-0.6B (~5% of backbone).
- **Comparison with prior methods**: Beats SASRec/BERT4Rec (ID-based), S3-Rec/UniSRec/RecFormer (text-enhanced), and LLaRA/LEARN (LLM-based) with +3.87%–8.02% relative N@10 across four datasets. One-month online A/B on a production feed (~1.5M DAU, 6% traffic): +9.24% CTR, +3.15% reply rate (p<0.01).
- **Link**: https://arxiv.org/abs/2605.26717

---

## 10. WWW 2026 (Dubai)

#### NEZHA: A Zero-sacrifice and Hyperspeed Decoding Architecture for Generative Recommendations
- **Title (ZH)**: NEZHA：生成式推荐的无损超高速解码架构
- **Authors**: Yejing Wang, Shengyu Zhou, Jinyu Lu, Ziwei Liu, Langming Liu, Maolin Wang, Wenlin Zhang, Feng Li, Wenbo Su, Pengjie Wang, Jian Xu, Xiangyu Zhao
- **Affiliation**: Alibaba (Taobao) + City University of Hong Kong
- **Venue**: WWW 2026
- **Abstract & Key Innovations**: Generative recommendation's autoregressive decoding over multi-token Semantic IDs is too slow for real-time ad serving (>1000 ms vs the 30 ms first-page budget). NEZHA rethinks speculative decoding for GR: a nimble autoregressive draft head built into the primary model does self-drafting (no separate draft model), and a model-free hash-set verifier rejects hallucinated (invalid) SIDs — the dominant accuracy killer. Combined with token-level latency engineering, 2.6× algorithm speedup.
- **Comparison with prior methods**: Deployed on Taobao Search Advertising recall since Oct 2025, cutting E2E latency from >1000 ms to <30 ms, unlocking first-page ad slots; 7-day A/B on 10% traffic: +1.2% revenue (billion-level ad revenue); clicked-item hit rate +0.58% (top-500) / +0.61% (top-1000) offline.
- **Link**: https://arxiv.org/abs/2511.18793

---

## 11. CIKM 2025 (Seoul, Nov 2025)

#### UniROM: Unifying Online Advertising Ranking as One Model
- **Title (ZH)**: UniROM：在线广告排序统一为单一模型
- **Authors**: Junyan Qiu, Ze Wang, Fan Zhang, Zuowu Zheng, Jile Zhu, Jiangke Fan, Teng Zhang, Haitao Wang, Xingxing Wang
- **Affiliation**: Meituan
- **Venue**: CIKM 2025
- **Abstract & Key Innovations**: Multi-stage cascaded ad pipelines suffer objective misalignment across stages and ignore inter-ad externalities. UniROM replaces the whole cascade with one end-to-end generative model that directly generates the optimal ad sequence from the full LBS candidate corpus (~10⁵ city-scoped ads): RecFormer with cluster-attention for intra-/cross-sequence externality modeling, an algorithm–engine co-designed hybrid feature service, and bi-stage training (pretraining + RL-based post-training with auction-aware losses and learned payment).
- **Comparison with prior methods**: Online A/B vs the deployed MCA baseline: +5.2% CTR, +13.6% RPM, +3.1% advertiser ROI at only +2.2% response time; offline Recall@50 0.513 (+20.4% over strongest baseline), eCTR +8.3%, eRPM 217.1 (+11.4%); incentive-compatibility metric Ψ cut from ~9% to 2.3%.
- **Link**: https://arxiv.org/abs/2505.19755

#### MTGR: Industrial-Scale Generative Recommendation Framework in Meituan
- **Title (ZH)**: MTGR：美团的工业级生成式推荐框架
- **Authors**: Ruidong Han, Bin Yin, Shangyu Chen, Jiang He, Fei Jiang, Xiang Li, Chi Ma, Mincong Huang, et al.
- **Affiliation**: Meituan
- **Venue**: CIKM 2025
- **Abstract & Key Innovations**: Pure generative recommenders abandon handcrafted cross-features and lose performance; DLRMs can't scale. MTGR (HSTU-based) keeps the full DLRM feature set including cross features by re-organizing user/candidate features into a typed token sequence with a discriminative loss — combining DLRM compatibility with GRM scalability. Contributions: Group Layer Normalization for heterogeneous tokens, dynamic masking (full / auto-regressive / self-only attention), and a TorchRec-based training framework with dynamic hash tables, sequence balancing, embedding de-dup (1.6–2.4× throughput over stock TorchRec on 100+ GPUs).
- **Comparison with prior methods**: MTGR-large beats a two-year-optimized DLRM: +1.22% conversion volume, +1.31% CTR online, training cost unchanged, inference cost cut 12%. Deployed in Meituan takeaway recommendation serving hundreds of millions of users.
- **Link**: https://arxiv.org/abs/2505.18654

---

## 12. RecSys 2025 (Prague, Sep 2025)

#### You Don't Bring Me Flowers: Mitigating Unwanted Recommendations Through Conformal Risk Control (**Best Paper**)
- **Title (ZH)**: 别给我送花：通过保形风险控制降低讨厌的推荐
- **Authors**: Giovanni De Toni, Erasmo Purificato, Emília Gómez, Andrea Passerini, Bruno Lepri, Cristian Consonni
- **Affiliation**: University of Trento + FBK + EU Joint Research Centre (ECAT)
- **Venue**: RecSys 2025 — **Best Full Paper Award**
- **Abstract & Key Innovations**: Recommenders propagate unwanted/harmful content and platform feedback tools are slow and ineffective. This model-agnostic, distribution-free post-hoc method uses conformal risk control to *provably bound* the fraction of unwanted items in a recommendation list, driven only by simple binary user feedback; it also leverages implicit watch-time feedback on consumed items to re-expand the (shrunk) recommendation set with safe previously-consumed content.
- **Comparison with prior methods**: First method giving item-level distribution-free guarantees on unwanted-content exposure (prior work gave group-level guarantees or needed learned feedback policies). On KuaiRand (27K Kuaishou users, ~32M watched videos): controllable reduction of unwanted recs with a tunable accuracy/set-size trade-off; the "Replace" strategy retains far higher nDCG than simple removal.
- **Link**: https://arxiv.org/abs/2507.16829

#### Scaling Generative Recommendations with Context Parallelism on Hierarchical Sequential Transducers
- **Title (ZH)**: 基于 HSTU 的上下文并行生成式推荐扩展
- **Authors**: Yue Dong, Han Li, Shen Li, Nikhil Patel, Xing Liu, Xiaodong Wang, Chuanhao Zhuge
- **Affiliation**: Meta *(inferred)*
- **Venue**: RecSys 2025 (short)
- **Abstract & Key Innovations**: Extending HSTU's sequence dimension in production is blocked by activation memory of quadratic attention over jagged user-history tensors. Introduces context parallelism adapted to HSTU's jagged-tensor attention: sharding Q/K/V along the sequence dimension with a ring-based gather overlapping communication with computation, and an AllGather-then-split pipeline integrated with DDP. Longer sequences yield consistent normalized-entropy improvements (Meta's GR scaling axis).
- **Comparison with prior methods**: vs vanilla (DDP-only) HSTU — enables a 5.3× increase in supported user-interaction sequence length and a 1.55× combined scaling factor when fused with data parallelism.
- **Link**: https://arxiv.org/abs/2508.04711

---

## 13. Recent arXiv — Agents, Code, Games, Benchmarks (2026)

### 13.1 Agent Systems

#### MAS-Orchestra: Holistic Training-Time Orchestration + when & why MAS beats SAS
- **Title (ZH)**: MAS-Orchestra：面向多智能体系统的整体式训练时编排框架
- **Authors**: Zixuan Ke, Yifei Ming, Austin Xu, Ryan Chin, Xuan-Phi Nguyen, Prathyusha Jwalapuram, et al.
- **Affiliation**: Salesforce Research + MIT
- **Venue**: arXiv (Jan 2026)
- **Abstract & Key Innovations**: Existing automatic MAS design is serial, code-level, lacking global system-level reasoning with large performance uncertainty. MAS-Orchestra formalizes MAS orchestration as a function-calling RL problem: complex goal-oriented sub-agents are abstracted as callable functions and the whole MAS is generated in one shot, with global reasoning over system structure. Introduces MASBENCH (Dim-5 axes: Depth/Horizon/Breadth/Parallel/Robustness) to systematically study when/why multi-agent beats single-agent.
- **Comparison with prior methods**: vs AFlow / MaAS / MAS-Zero / MAS-GPT / ToolOrchestra — consistent gains on math reasoning, multi-hop QA, and search-style QA; key insight: MAS is not universally better — benefits concentrate in parallel and adversarial settings.
- **Link**: https://arxiv.org/abs/2601.14652

#### Enterprise Deep Research (EDR): Steerable Multi-Agent Deep Research
- **Title (ZH)**: EDR：可操控的多智能体企业级深度研究框架
- **Authors**: Akshara Prabhakar, Roshan Ram, Zixiang Chen, Silvio Savarese, Frank Wang, Caiming Xiong, Huan Wang, Weiran Yao
- **Affiliation**: Salesforce AI Research
- **Venue**: arXiv (Oct 2025, updated Aug 2026)
- **Abstract & Key Innovations**: Multi-agent deep research for enterprise analytics: Master Planning Agent (adaptive query decomposition), four specialized search agents (General/Academic/GitHub/LinkedIn), MCP-based NL2SQL + file analysis tools, and a human-steerable context-editing mechanism exposing internal planning state via todo.md. Detects knowledge gaps via reflection and adjusts research directions.
- **Comparison with prior methods**: Outperforms SOTA agentic systems on DeepResearch Bench and DeepConsult without manual steering; vs static pipelines (WebWeaver / NVIDIA-AIQ) provides transparent, auditable, human-in-the-loop enterprise research.
- **Link**: https://arxiv.org/abs/2510.17797

### 13.2 Code Execution Prediction & SWE

#### SWE-Bench ProMax: Large-Scale Multilingual Code Refactoring
- **Title (ZH)**: SWE-Bench ProMax：多语言大规模代码重构智能体基准
- **Authors**: multi-author dataset team
- **Affiliation**: multi-lab *(inferred)*
- **Venue**: arXiv (Aug 2026)
- **Abstract & Key Innovations**: Responds to SWE-bench saturation/defects (~60% of unsolved Verified instances have issues; OpenAI dropped the benchmark): an expert-curated multilingual refactoring benchmark — 170 instances across 7 languages (Python/Java/TypeScript/Go/C/C++/Rust), 70 repos, avg 11.4 files and 261.6 lines modified per instance. Prompts rewritten as unambiguous specs; over-narrow/over-wide tests removed to guarantee necessity and sufficiency.
- **Comparison with prior methods**: Best model GPT-5.2 only 41.2% resolve (vs frontier 75%+ on SWE-bench Verified); GLM-5 (36.5%, $0.24/instance) approaches Claude Sonnet 4.6 (38.8%, $4.77/instance), showing open models can reach near-frontier at low cost; dominant failure mode is cross-file coordination.
- **Link**: https://arxiv.org/abs/2608.09802

#### AgentConductor: RL-Optimized Dynamic Multi-Agent Topology for Competition-Level Code
- **Title (ZH)**: AgentConductor：面向竞赛级代码生成的多智能体拓扑演化框架
- **Authors**: Siyu Wang, Renhong Lu, Zhihao Yang, Yuchao Wang, et al.
- **Affiliation**: Chinese university consortium *(inferred)*
- **Venue**: arXiv (Feb 2026)
- **Abstract & Key Innovations**: MAS interaction topologies are predefined/static and can't adapt to task difficulty. AgentConductor uses an LLM orchestrator with RL (GRPO) to generate difficulty-aware, density-aware hierarchical DAG topologies end-to-end, including a new topology-density function and difficulty-bin partitioning, dynamically adjusting the per-problem interaction structure to control token cost.
- **Comparison with prior methods**: pass@1 on APPS / LiveCodeBench(v4) / CodeContests: 58.8% / 46.3% / 38.8% (up to +14.6% / +3.1% / +1.1% over next best); HumanEval 97.5%, MBPP 95.1%; vs strongest baseline: −68% token cost, −13% density.
- **Link**: https://arxiv.org/abs/2602.17100

### 13.3 Games & World Action Models

#### Discovering Multiagent Learning Algorithms with Large Language Models (VAD-CFR, SHOR-PSRO)
- **Title (ZH)**: 用大语言模型自动发现多智能体学习算法（VAD-CFR 与 SHOR-PSRO）
- **Authors**: Zun Li, John Schultz, Daniel Hennes, Marc Lanctot
- **Affiliation**: Google DeepMind
- **Venue**: arXiv (Feb 2026)
- **Abstract & Key Innovations**: Applies AlphaEvolve (LLM-driven evolutionary coding agent) to automatically design MARL algorithms, treating code as a genome with semantic evolution. Evolves VAD-CFR (variance-adaptive discounting, consistency-boosted optimism, hard warm-start) in the CFR family and SHOR-PSRO (hybrid optimistic regret matching + temperature-controlled softmax with dynamic annealing) in PSRO; then distills train/test ablation to minimal cores (WOP-CFR, PM-PSRO).
- **Comparison with prior methods**: VAD-CFR beats SOTA human-designed Discounted Predictive CFR+ on 11/18 games; SHOR-PSRO outperforms Uniform/Nash/AlphaRank/PRD/RM meta-solvers on most games; distilled WOP-CFR / PM-PSRO cut structural complexity without loss (or gain) in generalization.
- **Link**: https://arxiv.org/abs/2602.16928

#### GameWAM: A World Action Model for Video Games
- **Title (ZH)**: GameWAM：面向原生视频游戏的 World Action Model
- **Authors**: single group, first-author byline not fully captured
- **Affiliation**: academic consortium *(inferred)*
- **Venue**: arXiv (Aug 2026)
- **Abstract & Key Innovations**: First World-Action Model (WAM) for native closed-loop games and GUI control. Generates future visual frames and executable keyboard-mouse action trajectories jointly via block-causal conditioning + flow matching with parallel visual/action generation. Introduces block-cycle control for long-horizon interaction (predict beyond committed horizon, execute short action prefix, re-plan) and gameplay/GUI mode prediction for heterogeneous native control. Identifies Low-Frequency Action Source Imprinting (LASI) as a control-failure mode.
- **Comparison with prior methods**: vs separate game-agent + world-model pipelines — achieves comparable task success with fewer native actions (ratio in paper).
- **Link**: https://arxiv.org/abs/2608.26200

#### LLAMIA: Latent State Internalization for LLM + Non-Language Agent Collaboration (EMNLP 2026 accepted)
- **Title (ZH)**: LLAMIA：语言 agent 与非语言 agent 协作中的潜在状态内化
- **Authors**: LLAMIA team
- **Affiliation**: academic *(inferred)*
- **Venue**: arXiv (accepted at EMNLP 2026)
- **Abstract & Key Innovations**: When LLMs must collaborate with non-language agents (game engines, robot controllers), compressing strong non-verbal agents' continuous representations into text summaries creates a per-interaction bottleneck — "verbalization debt". LLAMIA projects sub-agent continuous representations directly into the LLM token stream as learned state tokens, dynamically re-encoding as actions advance. Introduces LLAMIA-Bench (six collaborative chess tasks: behavior imitation, state evaluation, NL explanation).
- **Comparison with prior methods**: A 14B LLAMIA matches/exceeds task experts and GPT-5.1 (with tooling) while generalizing OOD (task-specific fine-tuning collapses OOD); verbalization debt persists under 4B→14B scaling.
- **Link**: https://arxiv.org/abs/2609.00474

### 13.4 Efficiency & Benchmarks

#### StateFlow: Efficient KV Sparsification for Long-Context LLM Inference
- **Title (ZH)**: StateFlow：面向长上下文推理的高效 KV 稀疏化
- **Authors**: multi-institution team (Tsinghua + ByteDance + BUPT + Hetao Shenzhen Institute)
- **Affiliation**: Tsinghua University, ByteDance, BUPT, Hetao Research Institute
- **Venue**: arXiv (Aug 2026)
- **Abstract & Key Innovations**: Hardware- and state-aware KV sparsification for long-context serving; keeps only frequently-accessed KV entries in the decode path.
- **Comparison with prior methods**: 2.22× throughput and 2.45× peak-memory reduction on a 32B/256K model at long-context workloads vs baselines, with negligible quality loss *(single-source)*.
- **Link**: https://arxiv.org/abs/2608.06838

#### VGI-Bench: General-Purpose Video Generation Intelligence Benchmark
- **Title (ZH)**: VGI-Bench：通用视频生成智能基准
- **Authors**: multi-institution, including Microsoft Research collaboration
- **Affiliation**: incl. Microsoft Research + participating labs
- **Venue**: arXiv (Aug 2026)
- **Abstract & Key Innovations**: Moves video-generation evaluation beyond prompt-following to agentic/general intelligence: 27 task categories across 810 instances probing planning, physics reasoning, tool use, and multi-turn generation.
- **Comparison with prior methods**: Reveals wide human↔model gaps — the best commercial model (Seedance 2.0) scores only 51.0% overall, showing current video generators remain far from end-to-end general task solving.
- **Link**: https://arxiv.org/abs/2608.19583

---

## Cross-Cutting Themes (this wave)

1. **Token-level "forking point" theory enters RLVR**: high-entropy decision tokens (NeurIPS'25) and flexibility-trap analysis of dLLMs (ICML'26 Outstanding) both point at the same mechanism — *which* tokens get optimized matters more than how many.
2. **Off-policy / async RL for LLM post-training** (TBA) and **DiLoCo scaling laws** (DeepMind) push LLM training toward distributed, async, communication-light regimes.
3. **ICML/ICLR 2026 Outstanding Papers are "controlled" results**: local-vs-global attention expressivity (ACL), arbitrary-order diffusion trade-offs, exponential sampling acceleration, single-vs-multi-turn evaluation — a shift from "who scales bigger" to "what is the right abstraction".
4. **Generative recommendation went fully industrial in 2025–2026**: Taobao NEZHA (<30 ms E2E GR serving), JD GenRec (page-wise GR), Meituan UniROM (unified ad-sequence generation), Meta HSTU context-parallelism — speculative/hash verification, page-wise NTP, and ent externality modeling are the new "GR systems" toolkit.
5. **Industrial ads/CTR now depends on sequence-first + reinforcement**: Kuaishou GOAL (constrained generative incentive allocation, +2.2% ROI online), Ant CTR-Sink (attention-sink signals for LM-CTR), Baidu GRAB (sequence-first paradigm, already tracked), Tencent TGR (unified gen+rank, tracked 09-02).
6. **Long-horizon video generation converges on autoregressive + flow/diffusion hybrids**: Flowception, LoL (12-h videos via head-wise RoPE jitter), Lumos-1, GPDiT, FAST-AR, Flex-Forcing — with KV/cache sparsity as the efficiency backbone.
7. **Agentic code evaluation enters the "fix the benchmark" phase**: SWE-Bench ProMax quantifies SWE-bench Verified defects and adds multilingual refactoring; MAS-orchestration research (MAS-Orchestra, AgentConductor) fuses RL with topology search.
8. **Memorization is now a measurable budget** (~3.6 bits/param) and **multi-turn evaluation is a first-class ICLR Outstanding Paper** — both reframe "how much and where models remember/lose information".

> **Caveats**: first-author affiliation lists are abbreviated; several affiliations and a few ICML acceptance statuses are marked *(inferred)* where metadata was thin; all quantitative claims are taken verbatim from source abstracts or official proceedings pages.