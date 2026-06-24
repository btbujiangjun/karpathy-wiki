---
title: "arXiv Paper Check 2026-06-24"
type: synthesis
created: 2026-06-24
updated: 2026-06-24
tags: [arxiv, paper-scan, ai, ctr, llm, recommendation]
---

# arXiv Paper Check — 2026-06-24

Scan of cs.LG, cs.AI, cs.IR new submissions from the last 24h (June 23–24, 2026).

---

## AI / LLM

### 1. OpenThoughts-Agent: Data Recipes for Agentic Models
- **arXiv**: 2606.24855 (cs.AI, Jun 24)
- **Authors**: Negin Raoof, Richard Zhuang, Marianna Nezhurina, Etash Guha, Atula Tejaswi, Ryan Marten, Charlie F. Ruan, Tyler Griggs, Alexander Glenn Shaw, Hritik Bansal, E. Kelly Buchanan, Artem Gazizov, Reinhard Heckel, Chinmay Hegde, Sankalp Jajee, Daanish Khazi, Emmanouil Koukoumidis, Xiangyi Li, Hange Liu, Shlok Natarajan, Harsh Raj, Nicholas Roberts, Ethan Shen, Nishad Singhi, Michael Siu, Ashima Suvarna, Hanwen Xing, Patrick Yubeaton, Robert Zhang, Leon Liangyu Chen, Xiaokun Chen, Steven Dillmann, Saadia Gabriel, Xunyi Jiang, Anurag Kashyap, Boxuan Li, Yein Park, Minh Pham, Sujay Sanghavi, Lin Shi, Ke Sun, Yixin Wang, Zhiwei Xu, Erica Zhang, Siyan Zhao, Wanjia Zhao, Jenia Jitsev, Alex Dimakis, Benjamin Feuer, Ludwig Schmidt
- **Key contribution**: Large collaboration studying data recipes for training agentic LLM models. Likely explores how data composition, mixture strategies, and curation impact agent capabilities.

### 2. Can Scale Save Us From Plasticity Loss in Large Language Models?
- **arXiv**: 2606.24752 (cs.AI, Jun 24)
- **Authors**: J. Fernando Hernandez-Garcia, Tomás Figliolia, Beren Millidge
- **Key contribution**: Investigates whether scaling (more parameters, more data) mitigates or exacerbates plasticity loss — the phenomenon where neural networks lose their ability to learn new information over time. Critical for continual learning and fine-tuning.

### 3. Scaling Laws for Task-Specific LLM Distillation
- **arXiv**: 2606.24747 (cs.AI, Jun 24)
- **Authors**: Lavinia Ghita, Dhruv Desai, Ioana Boier
- **Key contribution**: Empirically characterizes scaling laws for distilling LLMs into task-specific smaller models. Provides guidance on optimal teacher-student size ratios and distillation data budgets.

### 4. On the Smallness of the Large Language Models Scaling Exponents
- **arXiv**: 2606.24504 (cs.AI, Jun 24)
- **Authors**: Sauro Succi, Peter V. Coveney, Alex Hansen
- **Key contribution**: Theoretical analysis arguing that LLM scaling exponents are surprisingly small, with implications for the diminishing returns of scale and the potential need for architectural innovation.

### 5. Grad Detect: Gradient-Based Hallucination Detection in LLMs
- **arXiv**: 2606.24790 (cs.LG, cs.AI, Jun 24)
- **Authors**: Anand Kamat, Daniel Blake, Brent M. Werness
- **Key contribution**: Uses gradient signals from the LLM itself to detect hallucinations without external knowledge bases. Accepted at ICML 2026 Workshop on Compositional Learning.

### 6. AdversaBench: Automated LLM Red-Teaming with Multi-Judge Confirmation and Cross-Model Transferability
- **arXiv**: 2606.24589 (cs.AI, cs.CL, Jun 24)
- **Authors**: Khanak Khandelwal
- **Key contribution**: Automated red-teaming benchmark with multi-judge confirmation pipeline. Studies whether adversarial examples transfer across different LLM families.

### 7. World Models in Pieces: Structural Certification for General Agents
- **arXiv**: 2606.24842 (cs.AI, Jun 24)
- **Authors**: Yikai Lu, Yifei Wu, Xinyu Lu, Tongxin Li
- **Key contribution**: Camera-ready ICML 2026 paper. Proposes compositional world model certification — verifying agent behavior by decomposing the world model into certified pieces.

---

## Recommendation / CTR / IR

### 8. ScaleToT: Generalizing Structured LLM Reasoning for Billion-Scale Low-Activity User Modeling
- **arXiv**: 2606.24605 (cs.AI, Jun 24)
- **Authors**: Tianbao Ma, Chang Xi, Yichuan Zou, Chengen Li, Linxun Chen, Zilong Lu, Yanan Niu, Zhaojie Liu, Han Li, Kun Gai
- **Key contribution**: Applies structured LLM reasoning (Chain-of-Thought / Tree-of-Thought) to user modeling at billion-scale, specifically tackling cold-start / low-activity users. Notable given Kun Gai's involvement (prominent figure in Chinese recommendation/CTR).

### 9. Unified Multi-Task Relevance Modeling for E-Commerce: Comparing Task Routing Architectures Across LLMs and Cross-Encoders
- **arXiv**: 2606.23919 (cs.IR, Jun 24)
- **Authors**: Md Omar Faruk Rokon, Jhalak Nilesh Acharya, Shasvat Desai, Hong Yao, Kuang-chih Lee
- **Key contribution**: Accepted at SIGIR 2026 E-commerce Workshop. Compares LLM vs cross-encoder architectures for multi-task relevance scoring in e-commerce search.

### 10. LLM-as-a-Judge for Reliable and Explainable Offline Evaluation in Top-K Recommendation
- **arXiv**: 2606.22961 (cs.IR, Jun 23)
- **Authors**: Yue Que, Junyi Zhou, Xiaokun Zhang, Haiming Jin, Qiao Xiang, Chen Ma
- **Key contribution**: Accepted KDD 2026. Uses LLMs as judges for offline evaluation of recommender systems, providing both reliability scores and natural language explanations.

### 11. The Pitfall of Scaling Up: Uncovering and Mitigating Popularity Bias Amplification in Scaling Transformer-based Recommenders
- **arXiv**: 2606.21911 (cs.IR, cs.LG, Jun 23)
- **Authors**: Weiqin Yang, Yue Pan, Chongming Gao, Sheng Zhou, Xiang Wang, Can Wang, Jiawei Chen
- **Key contribution**: Accepted KDD 2026. Shows that scaling transformer-based recommenders amplifies popularity bias, and proposes mitigation strategies.

### 12. Improving Long-Context Retrieval with Multi-Prefix Embedding
- **arXiv**: 2606.23642 (cs.IR, Jun 23)
- **Authors**: Zhenglin Yu, Xueguang Ma, Shengyao Zhuang, Zhichao Xu, Luyu Gao, Crystina Zhang, Jimmy Lin
- **Key contribution**: Multi-prefix embedding approach to improve dense retrieval for long-context scenarios, addressing the information bottleneck in single-vector representations.

### 13. INSPIRE: Intent-aware Neural Sponsored Product Retrieval for E-commerce
- **arXiv**: 2606.23889 (cs.IR, Jun 24)
- **Authors**: Shasvat Desai, Hong Yao, Utkarsh Porwal, Kuang-chih Lee
- **Key contribution**: Accepted SIGIR 2026 E-commerce Workshop. Intent-aware retrieval model for sponsored products, incorporating user intent signals into the retrieval stage.

---

## ML Methods & Theory

### 14. Data Augmentation: A Fourier Analysis Perspective
- **arXiv**: 2606.24418 (cs.LG, stat.ML, Jun 24)
- **Authors**: Behrooz Tahmasebi, Melanie Weber, Stefanie Jegelka
- **Key contribution**: Published at COLT 2026. Provides a theoretical understanding of data augmentation through Fourier analysis, explaining which augmentations help and why.

### 15. Holistic Data Scheduler for LLM Pre-training via Multi-Objective Reinforcement Learning
- **arXiv**: 2606.24133 (cs.LG, cs.CL, Jun 24)
- **Authors**: Chenhao Dang, Jing Ma, Mingjie Liao
- **Key contribution**: Accepted KDD 2026. Uses multi-objective RL to schedule data mixture and ordering during LLM pre-training, optimizing for multiple downstream metrics simultaneously.

### 16. Catastrophic Compositional Generation: Why Vanilla Diffusion Models Fail to Extrapolate
- **arXiv**: 2606.23920 (cs.LG, cs.AI, Jun 24)
- **Authors**: Duncan Soiffer, Chandler Squires, Yuan Guan, Jason Hartford, Pradeep Ravikumar
- **Key contribution**: Identifies and analyzes the failure mode of diffusion models in compositional generation tasks where attribute binding exceeds training distribution support.

### 17. Reasoning as Attractor Dynamics: Latent Memory Retrieval via Gibbs-Weighted Energy Minimization
- **arXiv**: 2606.24543 (cs.LG, Jun 24)
- **Authors**: Kanishk Awadhiya
- **Key contribution**: Accepted ICLR Workshop 2026. Frames reasoning as energy minimization in a latent attractor space, connecting transformer reasoning to statistical physics and associative memory.

### 18. KLip-PPO: A per-sample KL perspective on PPO-Clip
- **arXiv**: 2606.23932 (cs.LG, Jun 24)
- **Authors**: Riccardo Colletti, Robin Holzinger
- **Key contribution**: Provides a per-sample KL divergence analysis of PPO's clipping mechanism, offering insights into why PPO works and how to better tune it.

---

## Summary

| Area | Notable Papers | Themes |
|------|---------------|--------|
| AI / LLM | OpenThoughts-Agent, Plasticity Loss, Scaling Laws for Distillation, Scaling Exponents, Grad Detect, AdversaBench | Agent data recipes, plasticity, scaling limits, hallucination, red-teaming |
| Recommendation / CTR | ScaleToT, Multi-Task Relevance, LLM-as-Judge, Popularity Bias, Multi-Prefix Embedding, INSPIRE | LLM reasoning for user modeling, LLM evaluation, bias in scaling, retrieval |
| ML Theory | Fourier Augmentation, Data Scheduler, Compositional Diffusion, Attractor Dynamics, KLip-PPO | Augmentation theory, data scheduling, diffusion failures, reasoning as energy minimization |
