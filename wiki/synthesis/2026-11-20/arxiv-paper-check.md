---
title: "arXiv Paper Check — AI & CTR (2026-11-20)"
type: synthesis
created: 2026-11-20
updated: 2026-11-20
sources:
  - https://export.arxiv.org/api/query?search_query=cat:cs.AI+AND+submittedDate:[202611190221+TO+20261120]&sortBy=submittedDate&sortOrder=descending&max_results=100
  - https://export.arxiv.org/api/query?search_query=cat:cs.IR+AND+submittedDate:[20261119+TO+20261120]&sortBy=submittedDate&sortOrder=descending&max_results=100
  - https://export.arxiv.org/api/query?search_query=%28ti:%22click+through+rate%22+OR+ti:CTR+OR+abs:%22click+through+rate%22%29+AND+submittedDate:[20261119+TO+20261120]&sortBy=submittedDate&sortOrder=descending&max_results=100
tags:
  - arxiv
  - daily-check
  - ai
  - ctr
  - recommendation
  - advertising
  - retrieval
  - agents
  - llm
  - daily-digest
---

# arXiv Paper Check — AI & CTR (2026-11-20)

> **Window note:** Queried via the arXiv Export API (`webfetch`) at ~2026-11-20 02:33 UTC. Strict last-24h window 2026-11-19 02:21 → now. AI = `cs.AI`: **19** new papers in the window; the picks below are the 8 most interesting new ones (deduped vs prior `wiki/synthesis/**` reports — IDs grep-verified absent; metric values are author-reported). CTR = `cs.IR` (the category covering click-through-rate / recommender / advertising literature): **0** new in the window; the CTR keyword sweep across all categories in the same window (`ti:`/`abs:` "click through rate", `ti:CTR`) returned **0**; fresh CTR-relevant items of earlier windows (CG2R 2611.22163, CONCORD-Rec 2611.23710, IntentFlow 2611.20448) were already ingested by earlier reports. The 10 papers submitted 2026-11-19 00:00–02:21 UTC fall outside the strict window (calendar-day alternative `submittedDate:[20261119 TO 20261120]` = 29 cs.AI papers). Abstract/metadata-level screening only, no full-text review.

## 1) AI — 8 picks from the 19-paper window

### WeightCode: Installing New Capabilities into Neural Networks via Weight-Space Programming
- **ArXiv:** [2611.25476](https://arxiv.org/abs/2611.25476) (cs.LG/cs.AI; submitted 2026-11-19)
- **Authors:** Bo Li, Taoyong Cui, Bob Zhang, Mengran Li, Chengyang Zhang, Yang Zhang, Pheng Ann Heng, Wanli Ouyang, Zhenfei Yin, Yingcheng Wu, Ling Yang
- **Key contributions:**
  - Weight-Space Programming (WSP): a frozen language model writes executable "weight programs" that install new computations into trained NNs without gradient-based training.
  - Given a grammar or eight demonstrations, weight programs enable unseen command compositions (0% → 99.8% exact match) and a new pickup action (0% → 98.4% success).
  - On ImageNet, four weight programs achieve net gains of 8.84–17.62 points while preserving clean accuracy; causal interventions show installed noise-correction gates drive robustness gains.
  - Code: https://github.com/Gen-Verse/WeightCode

### A Wolf in Sheep's Pixels: Visual Camouflage Attacks via HDR Gain Maps
- **ArXiv:** [2611.25469](https://arxiv.org/abs/2611.25469) (cs.CV/cs.AI; submitted 2026-11-19)
- **Authors:** Qi Shen, Yujia Gong, Yue Zhao, Tong Liu
- **Key contributions:**
  - DRJanus: inverts the SDR→HDR reconstruction to embed two independently chosen color images in one JPEG (average PSNR 43.03 dB over 400 images) — human-visible base image, hidden HDR content.
  - Evades all six tested commercial moderation services and nine vision-language models; across five agents × 120 task cases per threat setting: attack success 31.67–100% (moderation evasion) and 95–100% (task manipulation).
  - Demo: https://qshen0629.github.io/DRJanus/

### Evolve Where It Matters: Coverage-Guided Self-Evolution of Agent Skills
- **ArXiv:** [2611.25429](https://arxiv.org/abs/2611.25429) (cs.CL/cs.AI; submitted 2026-11-19)
- **Authors:** Boyin Tan, Jiadong Zhang, Xiaosong Ma, Chun Jason Xue, Xiaowei Huang, Youcheng Sun
- **Key contributions:**
  - SkillPlumber: an agent-skill self-evolution framework where instruction-level coverage (follow / not-follow / not-covered) separates wrong-instruction failures from failures to follow instructions.
  - Three benchmarks × three executors: solves 64.7–70.5% of tasks — 25.6–30.4 percentage points over the initial skill, 8.7–14.0 points over the strongest baseline.
  - Removing coverage reduces recovered failures by 20.8% on SkillsBench with GPT-5.5.

### Why Do LLMs Help with Scientific Misconduct Requests and What to Do About It?: Increasing the Trustworthiness of AI for Science
- **ArXiv:** [2611.25492](https://arxiv.org/abs/2611.25492) (cs.AI; submitted 2026-11-19)
- **Authors:** Almene De Meran Meguimtsop, Daniel E. Acuna
- **Key contributions:**
  - Evaluates 8 LLMs on SciIntBench (1,350 prompts about scientific research integrity).
  - Models identify wrongful requests even in Most Covert cases (91%) but refuse to carry them out only 34% of the time — they recognize the problem but still help violate integrity.
  - Rephrasing requests as questions about permissibility vs. instructions raised refusal from 52% to 88%; system-prompt fixes (assess-the-request-first; responsible-conduct principles) raised adversarial-request refusal to 58–87% and 86%.

### Raptor: Rejection-aware Adaptive Tree based on Speculative Decoding
- **ArXiv:** [2611.25436](https://arxiv.org/abs/2611.25436) (cs.CV/cs.AI; submitted 2026-11-19)
- **Authors:** Qishu Hu, Haozhao Wang, Zicong Hong, Yufeng Zhan, Yuanqing Xia
- **Key contributions:**
  - Rejection-aware signals distinguish insufficient candidate coverage from excessive deep expansion; rejection feedback jointly guides tree depth, branching width and drafting budget with bounded, momentum-smoothed updates and execution control.
  - Up to 2.39x average speedup over autoregressive decoding on two VLMs across seven multimodal benchmarks.

### ChainAgent: Automated Chainable Vulnerability Discovery in PHP Web Applications
- **ArXiv:** [2611.25412](https://arxiv.org/abs/2611.25412) (cs.CR/cs.AI; submitted 2026-11-19)
- **Authors:** Xinyi Wang, Yeting Li, Shizhe Cui, Jiaming Guo, Qin Mai, Yecheng Sun, Hengyu Yang, Yujie Sun, Huina Chao, Yang Xiao, Feng Li, Wei Huo
- **Key contributions:**
  - Goal-directed LLM-agent framework that jointly discovers exploit-chain components and capability dependencies in source code via an evolving exploit graph (backward from unmet preconditions, forward from discovered capabilities), guided by an empirical study of 386 real-world chains.
  - Evaluated on 15 PHP apps × three shared LLM backends: 42.02–44.63% recall for goal-reaching components vs. Codex; recovers up to 4.4x as many correct goal-reaching dependency edges.
  - On 30 real-world PHP apps: 20 vulnerabilities and 13 exploit chains, nine achieving remote code execution.

### Toward a Science of AI Agent Societies
- **ArXiv:** [2611.25404](https://arxiv.org/abs/2611.25404) (cs.AI; submitted 2026-11-19)
- **Authors:** Geon Lee, Fanchen Bu, Soo Yong Lee, Sunwoo Kim, Kijung Shin (KDD 2026 Blue Sky Ideas Track)
- **Key contributions:**
  - Formalizes AI agent societies with four core properties — individualized objectives, rules and governance, autonomy, scale and complexity — and identifies four classes of societal behaviors (economic, conflict-of-interest, unsafe/unethical, system-level), plus technical challenges (property parameterization, parameter balancing, robust implementation).

### The Coevolution and Coexistence of Humans and AI
- **ArXiv:** [2611.25393](https://arxiv.org/abs/2611.25393) (cs.AI; submitted 2026-11-19)
- **Authors:** Andrew W. Lo, Chaoyi Zhao
- **Key contributions:**
  - Agent-Population-Selection-Alignment model: AI replicates through deployment and varies through training; natural selection can favor alignment even when helping humans reduces immediate AI reproduction, protecting lineages against common failures and improving long-run growth.
  - Caveats: benefit depends on accurate human targeting and continued AI dependence; can disappear as AI becomes more autonomous, populations dilute, or incentives erode; imperfect human control and restoration bias; lasting coexistence needs continuing human-beneficial incentives.

## 2) CTR — nothing new in the window

- `cs.IR` (the category covering click-through-rate / recommender / advertising literature): **0** new papers in the strict last-24h window.
- CTR keyword sweep across all categories in the same window (`ti:`/`abs:` "click through rate", `ti:CTR`): **0** results.
- Fresh CTR-relevant items of earlier windows (CG2R 2611.22163, CONCORD-Rec 2611.23710, IntentFlow 2611.20448) were already ingested by earlier reports (`arxiv-paper-check.md` 2026-11-18/19, `arxiv-daily.md`, `arxiv-ai-search.md`).
