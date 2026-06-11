---
title: "arXiv Paper Check — AI & CTR (June 11, 2026)"
type: synthesis
created: 2026-06-11
updated: 2026-06-11
sources: [arxiv.org/list/cs.AI/recent, arxiv.org/list/cs.IR/recent]
tags: [arxiv, ai, ctr, recommendation, agents, reasoning]
---

# arXiv Paper Check — AI & CTR (June 11, 2026)

Surveyed: **cs.AI** (199 new entries, Thu Jun 11) + **cs.IR** (19 new entries, Thu Jun 11).

---

## AI Highlights

### 1. The Impossibility of Eliciting Latent Knowledge
- **Authors**: Korbinian Friedl, Francis Rhys Ward, Paul Yushin Rapoport, Tom Everitt, Jonathan Richens
- **arXiv**: 2606.12268
- **Contribution**: Formal proof that no procedure can guarantee eliciting latent knowledge from an AI system without making strong assumptions about the knowledge representation. Important alignment theory result — challenges the feasibility of "brain-reading" approaches to AI safety.

### 2. Redesign Mixture-of-Experts Routers with Manifold Power Iteration
- **Authors**: Songhao Wu, Ang Lv, Ruobing Xie, Yankai Lin
- **arXiv**: 2606.12397 (cs.LG cross-list)
- **Contribution**: Novel MoE routing method based on manifold power iteration. Improves expert specialization and load balancing without auxiliary losses. Relevant to efficient scaling of large models.

### 3. Architecture-Aware Reinforcement Learning Makes Sliding-Window Attention Competitive in Math Reasoning
- **Authors**: Kai Liu, Peijie Dong, Xinchen Xie, Jianfei Gao, Qipeng Guo, Xiaowen Chu, Shaoting Zhang, Kai Chen
- **arXiv**: 2606.11634
- **Contribution**: Uses RL to optimize sliding-window attention patterns for math reasoning tasks. Shows that architecture-aware training can close the gap between efficient attention and full attention on reasoning benchmarks.

### 4. SVoT: State-aware Visualization-of-Thought for Spatial Reasoning via Reinforcement Learning
- **Authors**: Chao Lei, Yanbei Jiang, Markus Hiller, Zhijian Zhou, Xunye Tian, Krista A. Ehinger, Nir Lipovetzky
- **arXiv**: 2606.11770
- **Contribution**: Extends Visualization-of-Thought with state-awareness and RL fine-tuning. Improves spatial reasoning in LLMs by maintaining explicit world state during reasoning.

### 5. TreeSeeker: Tree-Structured Trial, Error, and Return in Deep Search
- **Authors**: Zhuofan Shi, Mingzhe Ma, Lu Wang, Fangkai Yang, Pu Zhao, Yiming Guan, Youling Huang, Wei Zhang, Qingwei Lin, Dongmei Zhang, Saravan Rajmohan
- **arXiv**: 2606.11662
- **Contribution**: Tree-structured search algorithm with backtracking for LLM reasoning. Combines tree search with learned value functions for efficient exploration of reasoning paths.

### 6. Can AI Agents Synthesize Scientific Conclusions?
- **Authors**: Hayoung Jung, Pedro Viana Diniz, José Reinaldo Corrêa Roveda, Abner Fernandes da Silva, Haeun Jung, Enoch Tsai, Aleksandra Korolova, Manoel Horta Ribeiro
- **arXiv**: 2606.11337
- **Contribution**: Large-scale evaluation (79 pages) of AI agents' ability to synthesize scientific conclusions from literature. Found significant gaps in reliability, especially for nuanced or contradictory evidence.

### 7. ATLAS: Active Theory Learning for Automated Science
- **Authors**: Noémi Éltető, Nathaniel D. Daw, Kimberly L. Stachenfeld, Kevin J. Miller
- **arXiv**: 2606.12386 (cs.LG cross-list)
- **Contribution**: Framework for active learning of scientific theories from experiments. Combines Bayesian theory learning with active experimental design. Promising direction for automated scientific discovery.

### 8. APPO: Agentic Procedural Policy Optimization
- **Authors**: Xucong Wang, Ziyu Ma, Yong Wang, Yuxiang Ji, Shidong Yang, Guanhua Chen, Pengkun Wang, Xiangxiang Chu
- **arXiv**: 2606.12384 (cs.LG cross-list)
- **Contribution**: Fine-grained agentic RL framework that learns procedural policies (step-by-step action sequences) rather than end-to-end. Better interpretability and compositionality for agent tasks.

### 9. Position: Hippocampal Explicit Memory Is the Cornerstone for AGI
- **Authors**: Sangjun Park
- **arXiv**: 2606.11245 (ICML 2026 Position Paper)
- **Contribution**: Argues that explicit memory systems (analogous to hippocampus) are necessary for AGI. Proposes architectural principles for integrating episodic memory into neural networks.

### 10. Search Discipline for Long-Horizon Research Agents
- **Authors**: Adithya Srinivasan, Devesh Paragiri
- **arXiv**: 2606.11522
- **Contribution**: Framework for structured search strategies in research agents. Introduces "search discipline" — meta-level control of when to explore vs. exploit during long-horizon research tasks.

### 11. Forecasting Future Behavior as a Learning Task
- **Authors**: Mosh Levy, Yoav Goldberg, Asa Cooper Stickland
- **arXiv**: 2606.11445
- **Contribution**: Frames forecasting of AI system behavior as a learning problem. Introduces benchmarks and methods for predicting future model capabilities from early training dynamics.

---

## CTR / Recommendation Highlights

### 1. DiffCold: A Diffusion-based Generative Model for Cold-Start Item Recommendation
- **Authors**: Kangning Zhang, Yingjie Qin, Weinan Zhang, Yong Yu, Jianghao Lin
- **arXiv**: 2606.12245 (ECML-PKDD 2026)
- **Contribution**: Diffusion model for cold-start item recommendation. Generates item representations from content features, outperforming traditional ID-based methods for new items. The first diffusion-based approach to cold-start recommendation.

### 2. LLM-Based User Personas for Recommendations at Scale
- **Authors**: Haoting Wang, Haokai Lu, Zheyun Feng, Jenny Huang, Yifat Amir, Gregory Hinkson, Ben Most, Zelong Zhao, Yixin Kelly Cui, Rein Zhang, Fabio Soldo, Yu Xia, Nihar Bhupalam, Minmin Chen, Konstantina Christakopoulou, Lichan Hong, Ed H. Chi
- **arXiv**: 2606.12198 (Google)
- **Contribution**: Uses LLMs to generate structured user personas from historical behavior for recommendation. Deployed at scale on Google's recommendation systems. Bridges the gap between LLM reasoning and traditional collaborative filtering.

### 3. Tail-Aware Adaptive-k: Query-Adaptive Context Selection for RAG
- **Authors**: Ziyu Song, Jiaming Fang, Kuangyu Li, Tuo Xia, Chuanpeng Wang
- **arXiv**: 2606.11907 (ECML-PKDD 2026)
- **Contribution**: Adaptive context window selection for RAG. Dynamically chooses number of retrieved documents per query, with emphasis on handling tail (rare) queries better. Improves both quality and efficiency.

### 4. CORE-Bench: A Comprehensive Benchmark for Code Retrieval in Agentic Coding
- **Authors**: Fuwei Zhang, Yanzhao Zhang, Mingxin Li, Dingkun Long, Lexiang Hu, Pengjun Xie, Zhao Zhang, Fuzhen Zhuang
- **arXiv**: 2606.11864
- **Contribution**: New benchmark for code retrieval in agentic coding scenarios. Evaluates retrieval systems on their ability to find relevant code across repositories given complex natural language queries.

### 5. CompRank: Efficient LLM Reranking via Token-Level Compression and Decoding-Free Scoring
- **Authors**: Xuan Lu, Haohang Huang, Yingqi Fan, Junlong Tong, Yuxuan Zhang, Ping Nie, Rui Meng, Xiaoyu Shen
- **arXiv**: 2606.11700
- **Contribution**: Uses compression techniques to enable fast LLM-based reranking without full decoding. Token-level compression reduces computation while preserving ranking quality.

### 6. What Limits Does Quantization Place on Dense Top-k Retrieval?
- **Authors**: Koki Okajima, Tsukasa Yoshida
- **arXiv**: 2606.11780
- **Contribution**: Theoretical analysis of how quantization affects dense retrieval quality. First formal characterization of the trade-off between compression rate and retrieval accuracy.

### 7. FAST-MEL: Fast, Accurate, Storage Efficient Multimodal Entity Linking
- **Authors**: Derrien Thomas, Laurent Amsaleg, Pascale Sébillot
- **arXiv**: 2606.11749 (SIGIR 2026)
- **Contribution**: Multimodal entity linking with efficient storage. Links text and image mentions to knowledge base entities with minimal storage overhead.

---

## Key Themes

1. **RL for reasoning continues to dominate** — Three papers (SVoT, Architecture-Aware RL, APPO) use RL to improve reasoning or agent behavior.
2. **Alignment theory maturing** — The impossibility result for latent knowledge elicitation is a significant theoretical contribution to AI safety.
3. **LLM + Recommendation convergence accelerates** — Google's user personas paper and DiffCold show LLMs being integrated into core recommendation pipelines.
4. **Efficient retrieval** — CompRank, quantization analysis, and adaptive RAG all tackle the efficiency-quality frontier.
5. **Agent evaluation becoming rigorous** — CORE-Bench and the scientific synthesis paper both push toward better evaluation of agent capabilities.
