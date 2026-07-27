---
title: "Conference Digest: 2025-2026 Top ML/AI Venues"
type: synthesis
created: 2026-07-27
updated: 2026-07-27
sources: []
tags: [conference-digest, ICML2026, AAAI2026, NeurIPS2025, ICLR2026, CVPR2026, KDD2026, ACL2026, recommendation, LLM, advertising, CTR, agent, generative-model]
---

# Conference Digest: 2025-2026 Top ML/AI Venues

> Compiled 2026-07-27. Covers ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, CVPR 2026, KDD 2026, ACL 2026, SIGIR 2026, WWW 2026, EMNLP 2025, RecSys 2025. Focus areas: recommendation systems, LLM-based recommendation, advertising/auction, generative models, agent systems, benchmarks.

---

## 1. ICML 2026 (Seoul, July 6-11)

**Scale**: 6,634 accepted papers. Largest ICML to date.

### 1.1 LLM-Based Recommendation

#### Align³GR: Unified Multi-Level Alignment for LLM-based Generative Recommendation
- **Authors**: Wencai Ye, Mingjie Sun, Shuhang Chen, Wenjin Wu, Peng Jiang
- **Affiliation**: Kuaishou Technology
- **Venue**: AAAI 2026 Oral (also relevant to ICML community)
- **arXiv**: <https://arxiv.org/abs/2511.11255>
- **Abstract & Innovations**: Proposes a unified three-level alignment framework bridging LLMs and recommender systems. (1) Token-level: dual-side SCID fusion of semantic and collaborative signals. (2) Behavior modeling level: multi-task SFT with bidirectional semantic alignment. (3) Preference level: progressive DPO combining self-play (SP-DPO) and real-world feedback (RF-DPO). Outperforms SOTA by +17.8% Recall@10 and +20.2% NDCG@10 on public benchmarks, with confirmed gains in online A/B tests on Kuaishou's industrial platform.
- **Comparison**: Prior LLM4Rec methods typically align at only one level (tokenization, SFT, or RLHF). Align³GR is the first to unify all three in a single framework with industrial deployment evidence.

#### Principled Synthetic Data Enables the First Scaling Laws for LLMs in Recommendation
- **Authors**: Meta AI
- **Venue**: ICML 2026
- **arXiv**: <https://arxiv.org/abs/2602.07298>
- **Abstract & Innovations**: Attributes the difficulty of scaling laws in LLM4Rec to noise, bias, and incompleteness of raw interaction data. Proposes a hierarchical synthetic data curriculum to enable predictable scaling. Demonstrates stable power-law relationships between model size, data quality, and recommendation performance.
- **Comparison**: Prior work treated LLM4Rec scaling as analogous to NLP scaling; this paper shows clean synthetic data is the key enabler, not more raw logs.

#### Mitigating Reward Hacking in LLM-based Recommendation
- **Authors**: University of Science and Technology of China
- **Venue**: ICML 2026
- **Link**: <https://icml.cc/virtual/2026/poster/66384>
- **Abstract & Innovations**: Identifies reward hacking in LLM recommendation: training metrics improve but actual ranking quality stagnates. Defines epsilon-insensitive regions in gradient space showing pairwise updates fail to change ordering between positive and unsampled negatives. Analyzes failures under the Bradley-Terry framework.
- **Comparison**: Standard DPO-based LLM4Rec methods assume pairwise loss下降 correlates with ranking improvement; this paper proves it does not and provides diagnostic tools.

#### CCLRec: Consensus-driven Contrastive Learning for LLM-enhanced Graph Recommendation
- **Authors**: North University of China / Harbin Institute of Technology / Penn State
- **Venue**: ICML 2026
- **Link**: <https://icml.cc/virtual/2026/poster/65594>
- **Abstract & Innovations**: Addresses the disconnect between structural proximity (GNN) and semantic relevance (LLM) in graph-based recommendation. Uses consensus-driven contrastive learning to align structural and semantic representations.
- **Comparison**: Prior GNN+LLM methods process the two signals independently, causing representation drift. CCLRec enforces cross-signal consensus.

#### UniRec: Unified Multimodal Encoding for LLM-Based Recommendations
- **Authors**: Zijie Lei, Tao Feng, Zhigang Hua, Yan Xie, Guanyu Lin, Shuang Yang, Ge Liu, Jiaxuan You
- **Affiliation**: UIUC
- **Venue**: TMLR 2026 (also ICML-adjacent)
- **arXiv**: <https://arxiv.org/abs/2601.19423>
- **Abstract & Innovations**: Formalizes recommendation into 4 modalities (text, image, categorical, numerical). Each attribute encoded as (name, type, value) triplet. Uses modality-specific encoders and two-stage hierarchical Q-Former to preserve schema and history structure. Achieves up to 15% improvement over SOTA multimodal and LLM-based recommenders.
- **Comparison**: Prior multimodal LLM recommenders focus only on text+image; UniRec extends to categorical and numerical features with disentangled schema representation.

#### T-POP: Test-Time Personalization with Online Preference Feedback
- **Authors**: ICML 2026
- **Link**: <https://icml.cc/virtual/2026/poster/66384>
- **Abstract & Innovations**: Without modifying LLM parameters, learns a personalized reward function online using pairwise preference feedback per round. Addresses cold-start personalization for new users.

### 1.2 Advertising & Auction Mechanism Design

#### Autobidding Auctions with LLM-Powered Creatives
- **Authors**: ICML 2026
- **Link**: <https://icml.cc/virtual/2026/poster/60993>
- **Abstract & Innovations**: Models the platform as Stackelberg leader and advertisers as budget-constrained followers in an autobidding auction. Explicitly considers LLM inference cost for real-time creative generation/enhancement. Core variable shifts from pCTR/pCVR to whether the platform should invoke LLM creative generation for specific ads.
- **Comparison**: Prior auction theory assumed static creatives; this paper integrates GenAI cost into the mechanism design.

#### Model Monotonicity in Autobidding Auctions
- **Authors**: Uber
- **Venue**: ICML 2026
- **Link**: <https://icml.cc/virtual/2026/poster/60993>
- **Abstract & Innovations**: Proves that improved pCTR/pCVR predictions do NOT necessarily lead to better auction outcomes (revenue, welfare, liquid welfare). Uses cluster refinement to define model improvement and analyzes non-monotonicity across auction formats and autobidder behaviors.
- **Comparison**: Industry assumption that "better model → better outcomes" is formally disproven under budget-constrained autobidding.

#### Risk-Averse and Optimistic Advertiser Incentive Compatibility in Auto-bidding
- **Authors**: Google
- **arXiv**: <https://arxiv.org/abs/2508.16823>
- **Abstract & Innovations**: Relaxes the traditional AIC definition (worst-case comparison) by introducing risk-averse and optimistic perspectives for comparing truthful reporting vs. deviation when multiple equilibria exist.
- **Comparison**: Standard AIC is overly strict; this paper provides more practical incentive compatibility guarantees.

#### Incentivized Exploration with Stochastic Covariates
- **Authors**: UCLA / Meta
- **Link**: <https://icml.cc/virtual/2026/poster/64632>
- **Abstract & Innovations**: Designs a two-stage mechanism for recommender system exploration where user covariates arrive online stochastically. Uses Bayesian Incentive Compatibility to ensure users voluntarily accept exploration, achieving sublinear regret.

### 1.3 Generative Recommendation & Semantic IDs

#### Hyperbolic RQ-VAE enhanced Generative Recommendation (HG-Rec)
- **Authors**: ICML 2026
- **Link**: <https://icml.cc/virtual/2026/poster/61457>
- **Abstract & Innovations**: Uses hyperbolic RQ-VAE with differential-length codebook strategy for item tokenization in generative recommendation. Hyperbolic geometry naturally captures long-tail and hierarchical structure of item semantics.
- **Comparison**: Prior Semantic ID methods (TIGER, COINS) use Euclidean RQ-VAE; HG-Rec shows hyperbolic space provides lower-distortion discrete representations for hierarchical item taxonomies.

#### UniRec (Generative): Bridging the Expressive Gap between Generative and Discriminative Recommendation
- **Authors**: Ziliang Wang, Gaoyun Lin, Xuesi Wang, Shaoqiang Liang, Liam Huang, Jason Bian
- **arXiv**: <https://arxiv.org/abs/2604.12234>
- **Abstract & Innovations**: Addresses the fundamental expressive gap: discriminative models score items with direct feature crossing, while generative models decode over compact SID tokens without item-side signal. Introduces Capacity-constrained SID (exposure-weighted capacity penalties) and Conditional Decoding Context (CDC) with task-conditioned BOS and hash-based content summaries. Joint RFT+DPO alignment. Achieves +22.6% HR@50 overall and +15.5% on high-value orders. Deployed in Kuaishou e-commerce.
- **Comparison**: Prior GR methods (TIGER, OneRec) lack explicit mechanism to bridge the feature-access gap; UniRec injects scenario-conditioned signals at each decoding step.

#### RSIR: Can Recommender Systems Teach Themselves?
- **Authors**: USTC / Huawei
- **arXiv**: <https://arxiv.org/abs/2602.15659>
- **Abstract & Innovations**: Recursive self-improving framework: current model generates synthetic interaction sequences, fidelity control filters samples near the user preference manifold, successor model trains on filtered data. Achieves 4-11% NDCG/Recall improvement across 4 datasets and 3 backbones. Theoretically proves equivalence to implicit regularization along the preference manifold tangent space.

### 1.4 Graph & Multi-Behavior Recommendation

#### GCIB: Graph Contrastive Information Bottleneck for Multi-Behavior Recommendation
- **Authors**: Tianjin University / Anhui University
- **Link**: <https://icml.cc/virtual/2026/poster/62097>
- **Abstract & Innovations**: Uses dual "Graph Information Bottleneck + Cross-behavior Contrastive Learning" to prune auxiliary behavior edges irrelevant to the target task. Maximizes mutual information with target behavior while minimizing MI with original auxiliary graph via HSIC surrogates.

#### HVAE: Hyperbolic Variational Autoencoder for Cross-Domain Knowledge Transfer
- **Authors**: Alibaba / Ant Group / Ocean University of China
- **Link**: <https://icml.cc/virtual/2026/poster/61457>
- **Abstract & Innovations**: Uses hyperbolic VAE to address geometric mismatch in cross-domain recommendation. Disentangles domain-invariant preferences from domain-specific interests in hyperbolic space, enabling flexible knowledge transfer.

### 1.5 Reliable & Calibrated Recommendation

#### CARE: Adaptive Calibration for Reliable Recommendations
- **Authors**: University of Technology Sydney
- **Link**: <https://icml.cc/virtual/2026/poster/62132>
- **Abstract & Innovations**: Wraps any backbone recommender with adaptive calibration. Outputs variable-sized recommendation sets with finite-sample performance guarantees. Loss-based behavior change detection + online aggregation threshold recalibration.

#### CORAL: Uncertainty-Aware Regulation of Exposure Concentration
- **Authors**: University of Technology Sydney
- **Link**: <https://icml.cc/virtual/2026/poster/63919>
- **Abstract & Innovations**: Models exposure regulation as constrained sequential decision-making with UCB-style risk estimation. Prevents engagement optimization from collapsing exposure to少数 categories.

### 1.6 Controllable & Editable Recommendation

#### CRAMER: Control via Request-Aware Masking for Editing Recommenders
- **Authors**: Renmin University / Dalhousie
- **Link**: <https://icml.cc/virtual/2026/poster/62968>
- **Abstract & Innovations**: Enables sequential recommenders to respond to real-time natural language requests (e.g., "cheaper", "lighter") without retraining. Uses request-aware masking to edit recommendation output while preserving serving efficiency.

### 1.7 Efficient Model Architecture

#### Sparse by Design: Relevance-Driven Scaling for Recommender Systems
- **Authors**: Meta
- **Link**: <https://icml.cc/virtual/2026/poster/66202>
- **Abstract & Innovations**: Shows Sparse MoE does not transfer naturally from LLMs to recommendation because token-level routing misaligns with user-item relevance prediction. Proposes relevance-driven scaling where sparse computation is designed around relevance signals rather than token routing.
- **Comparison**: Direct MoE transfer from LLMs fails; this paper provides the first principled adaptation of sparsity to recommendation architectures.

### 1.8 Privacy & Unlearning

#### Obliviate: Efficient Unlearning in Recommender Systems
- **Authors**: Sony Research India / IIT Roorkee
- **Link**: <https://icml.cc/virtual/2026/poster/64974>
- **Abstract & Innovations**: Two-stage machine unlearning framework for recommendation that deletes specified interactions without full retraining while preserving recommendation quality. High compliance value for GDPR/CCPA.

#### Federated Cross-Silo Recommendation with Differential Privacy
- **Authors**: ICML 2026
- **Abstract & Innovations**: Trains collaborative models across parties without data centralization, providing DP guarantees. Addresses the conflict between implicit negative samples, missing-not-at-random data, and DP noise.

### 1.9 Security

#### VENOMREC: Cross-Modal Interactive Poisoning for Multimodal LLM Recommenders
- **Authors**: NTU / Beihang / Alibaba
- **arXiv**: <https://arxiv.org/abs/2602.06409>
- **Abstract & Innovations**: Demonstrates that cross-modal consensus in multimodal LLM recommenders can be exploited via synchronized multi-modal poisoning. Proposes Exposure Alignment to find high-exposure regions and Cross-modal Interactive Perturbation for targeted promotion. Critical for understanding attack surfaces in multimodal recommendation deployments.

### 1.10 Reinforcement Learning for Recommendation

#### ProRL: Rectified Policy Gradient for Proactive Recommendation
- **Authors**: Fudan University
- **Link**: <https://icml.cc/virtual/2026/poster/61903>
- **Abstract & Innovations**: Addresses proactive recommendation (guiding user preference toward target items via intermediate paths). Fixes length-dependent bias and high variance in naive policy gradient via rectified gradient estimation.

### 1.11 Cold-Start & Preference Elicitation

#### PEP: Cold-Start Personalization via Training-Free Priors from Structured World Models
- **Authors**: University of Washington / Meta FAIR / AI2
- **arXiv**: <https://arxiv.org/abs/2602.15012>
- **Abstract & Innovations**: Leverages cross-population preference structure (e.g., people who value detailed explanations also value worked examples) from structured world models. Training-free decomposition for preference elicitation with minimal interaction.

---

## 2. AAAI 2026

**Scale**: 27 recommender system papers catalogued. Vol. 40, No. 19.

### 2.1 LLM-Based Generative Recommendation

#### Align³GR (see ICML section above)
- **Affiliation**: Kuaishou Technology
- **Status**: AAAI 2026 Oral
- **Key Result**: +17.8% Recall@10, +20.2% NDCG@10; deployed on Kuaishou industrial platform.

#### BEAT: Behavior Tokens Speak Louder than Words
- **Authors**: AAAI 2026
- **DOI**: <https://doi.org/10.1609/aaai.v40i25.39252>
- **Abstract & Innovations**: Designs semantic alignment regularization to embed behavior tokens directly into the input space of frozen language models. Improves zero-shot recommendation while generating coherent explanations. Tested on 3 public datasets.

### 2.2 Additional AAAI 2026 RecSys Papers (from en.papernotes.org)
- **BidSeesaw**: Bidirectional seesaw mechanism for CTR prediction
- **DMLP**: Deep MLP-based interaction modeling
- 27 papers total across Data Mining & Knowledge Management tracks

---

## 3. NeurIPS 2025 (San Diego, Dec 2-7)

**Scale**: 5,290 accepted papers. 77 Orals (top 1.5%).

### 3.1 Best Paper Awards

#### Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)
- **Authors**: Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Yejin Choi
- **Affiliation**: University of Washington / Carnegie Mellon / Allen Institute for AI
- **arXiv**: <https://arxiv.org/abs/2510.22954>
- **Track**: Datasets & Benchmarks (Best Paper)
- **Abstract & Innovations**: Introduces INFINITY-CHAT dataset (26K+ open-ended queries from WildChat, 31K+ human annotations) with a taxonomy of 6 top-level / 17 subcategories of open-ended prompts. Evaluates 70+ LLMs and finds pervasive "artificial hivemind" — extreme mode collapse both intra-model (repeatedly generating same outputs) and inter-model (different model families converging on strikingly similar responses). Shows RLHF and instruction tuning homogenize creative latent space. Current reward models are poorly calibrated to diverse human preferences.
- **Comparison**: Prior benchmarks focus on tasks with ground-truth answers; INFINITY-CHAT is the first large-scale resource for studying open-endedness. Reveals that temperature scaling and model ensembles do NOT guarantee diversity.

#### Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free
- **Authors**: Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, Junyang Lin
- **Affiliation**: Alibaba Qwen Team
- **arXiv**: <https://arxiv.org/abs/2505.06708>
- **Track**: Best Paper + Oral
- **Abstract & Innovations**: Adds a learnable, input-dependent sigmoid gate immediately after Scaled Dot-Product Attention (SDPA). Systematically explored 5 gating positions (G1-G5) and 30+ variants on 15B MoE and 1.7B dense models trained on 3.5T tokens. G1 position (sigmoid gate after SDPA) eliminates attention sink phenomenon, improves training stability (no loss spikes), and enhances long-context extrapolation. Already integrated into Qwen3-Next production architecture.
- **Comparison**: Prior attention sink fixes are heuristic (sink tokens); gated attention provides a principled architectural solution. Open-source implementation at <https://github.com/qiuzh20/gated_attention>.

#### 1000 Layer Networks for Self-Supervised RL
- **Authors**: Kevin Wang, Ishaan Javali, Michał Bortkiewicz, Tomasz Trzciński, Benjamin Eysenbach
- **Track**: Best Paper
- **Abstract & Innovations**: Scales RL networks to 1,024 layers, achieving 2x-50x improvements in goal-conditioned self-supervised RL. Shatters the conventional wisdom that RL networks should be shallow (2-5 layers).

#### Why Diffusion Models Don't Memorize
- **Authors**: Tony Bonnaire, Raphaël Urfin, Giulio Biroli, Marc Mézard
- **arXiv**: <https://arxiv.org/abs/2505.17638>
- **Track**: Best Paper
- **Abstract & Innovations**: Identifies two distinct timescales in diffusion model training: τ_gen (learning to generate valid samples) and τ_mem (beginning to memorize training instances). Provides theoretical and empirical analysis of implicit dynamical regularization.

### 3.2 Runner-Up Papers
- Test of Time Award: Faster R-CNN
- Additional runner-up papers in oral/poster tracks

---

## 4. ICLR 2026

**Scale**: 223 oral papers (selected from thousands of submissions).

### 4.1 Stanford SAIL at ICLR 2026
- Featured papers include GritLM, STARK, and other works (details at <https://ai.stanford.edu/blog/iclr-2026/>)

### 4.2 ICLR 2026 Oral Papers
- Full list with Chinese translations maintained at <https://github.com/XinyuLiuCs/iclr2026-oral-papers>
- 223 oral papers across all tracks

---

## 5. CVPR 2026

**Scale**: 4,000+ papers accepted.

### 5.1 Highlights
- **Llama for Image Generation**: Meta's Llama model adapted for image generation
- **ProSpect**: Progressive spectral methods
- **S4D Video Understanding**: State-space models for video
- **Gemini-CLIP**: Google's Gemini adapted for CLIP-style tasks
- Full highlights at <https://resources.paperdigest.org/2026/04/cvpr-2026-papers-highlights/>

---

## 6. KDD 2026 (Jeju Island, Aug 9-13)

**Status**: Proceedings published on ACM Digital Library.

### 6.1 Notable Papers
- **GR4AD: Generative Recommendation for Large-Scale Advertising** (Kuaishou, arXiv: 2602.22732)
  - VSL (Value-Aware Supervised Learning) + RSPO (Ranking-Guided Softmax Preference Optimization)
  - Dynamic beam serving with adaptive beam width
  - **4.2% ad revenue improvement** over DLRM-based stack in online A/B tests
  - Fully deployed in Kuaishou advertising system (400M+ users)
  - Demonstrates both model scaling and inference-time scaling gains

---

## 7. ACL 2026 (San Diego, Jul 2-7)

**Scale**: 2,296 main + 2,163 findings = 4,459 total papers. Record year.

### 7.1 Highlights
- Full highlights at <https://www.paperdigest.org/2026/06/acl-2026-papers-highlights/>
- Largest ACL to date with 4,459 papers

---

## 8. SIGIR 2026 (Melbourne, Jul 20-24)

**Scale**: 113 full papers + 45 short papers.

---

## 9. WWW 2026 (Sydney, Apr 28 - May 2)

### 9.1 Notable Recommendation Papers
- **Talos**: Optimizing Top-K Accuracy in Recommender Systems
- **Improving Multi Task Recommendations via Cross User Learning** with Hybrid Pointwise and Pairwise Ranking Loss
- **ONeRec**: Openness-Aware and Adaptive Proactive News Recommendation
- **Bridging Time and Domains**: Time-aware Framework for Cross-Domain Sequential Recommendation
- **PRISM**: Personalized Recommendation via Information Synergy Module

---

## 10. EMNLP 2025 (Suzhou, China)

**Format**: Hybrid (in-person + virtual)

---

## 11. RecSys 2025

**Status**: Accepted contributions page live. Meta AI confirmed as gold supporter.

---

## Cross-Conference Trends

### Trend 1: LLM-based Generative Recommendation Goes Industrial
Multiple papers from Kuaishou (Align³GR, UniRec, GR4AD) demonstrate full deployment of generative recommendation at scale. The progression: TIGER → OneRec → UniRec/GR4AD shows rapid industrialization of Semantic ID + autoregressive decoding paradigm.

### Trend 2: Alignment Taxonomy Expands
Align³GR establishes three-level alignment (token/behavior/preference). Reward hacking analysis reveals DPO-style objectives can decouple training metrics from actual ranking quality. Progressive DPO with self-play and real-world feedback becomes the new standard.

### Trend 3: Non-Euclidean Geometry for Recommendation
HG-Rec (hyperbolic RQ-VAE) and HVAE (hyperbolic VAE) both demonstrate that hyperbolic geometry better captures long-tail and hierarchical item structures than Euclidean embeddings.

### Trend 4: Auction Theory Meets LLM Creatives
ICML 2026 papers integrate LLM inference cost into auction mechanism design, challenging the assumption that "better predictions → better outcomes" and introducing Stackelberg game formulations.

### Trend 5: Safety & Robustness in Multimodal Rec
VENOMREC demonstrates cross-modal poisoning attacks. Reward hacking analysis provides diagnostic tools for LLM-based recommendation failures.

### Trend 6: MoE Must Be Redesigned for Rec
Meta's "Sparse by Design" shows direct MoE transfer from LLMs fails; relevance-driven scaling is needed.

### Trend 7: Attention Mechanism Revolution
Gated Attention (NeurIPS 2025 Best Paper) is already in production (Qwen3-Next). Simple sigmoid gating after SDPA eliminates attention sinks and improves long-context performance.

### Trend 8: RL Depth Scaling
1000-layer networks for RL shatter the shallow-network assumption, opening new possibilities for robotic manipulation and multi-agent coordination.

---

## Key Industrial Deployments

| Paper | Company | Scale | Metric |
|-------|---------|-------|--------|
| Align³GR | Kuaishou | Full platform | +17.8% Recall@10 |
| GR4AD | Kuaishou | 400M+ users | +4.2% ad revenue |
| UniRec (Gen) | Kuaishou E-commerce | Online A/B | +22.6% HR@50 |
| Gated Attention | Alibaba Qwen | Qwen3-Next | Production deployed |
