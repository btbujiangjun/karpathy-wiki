---
title: Learning more about Claude's mathematical capabilities (Riemann zeta)
type: source-summary
created: 2026-08-11
updated: 2026-08-11
sources: [anthropic-riemann-zeta.md]
tags: [anthropic, claude, riemann-hypothesis, math-ai, lean, agents, claude-code, research-automation]
---

# Anthropic — Learning more about Claude's mathematical capabilities

> 来源：Anthropic 研究博客，2026-08-10 发布。原文：https://anthropic.com/research/riemann-zeta

## 核心声明（按原文忠实记录）

- Claude（未发布的 research 版）尝试证明 Riemann 假设未成功，但**意外改进了临界线上零点比例的下界：41.6% → 67.2%**。
- 结果建立在 Bombieri（2000）与 Baluyot / Goldston / Suriajaya / Turnage-Butterbaugh 系列（arXiv:2306.04799, 2501.14545）之上；后者使 Montgomery（1973）pair correlation 技术无需假设 Riemann 假设成立。
- 技术核心：带 Weil 诱导二次型的函数空间 + 正/负定子空间 + 二次型秩不等式（first/second-moment）；关键勇气是**同时处理全空间、正负定并纳、允许非对角二次型**。
- 验证：Anthropic 数学家 Levent Alpöge、Ralph Furman 验证；外部专家 Brian Conrey、Dan Goldston 审阅；Lean 形式化证明（github.com/anthropics/zeta-23-lean）通过 comparator。

## 方法论（Claude Code 中的 agent 研究）

- **31M output tokens**，两次会话；**约 60 个 Claude subagents**；**2,400 个 shell 命令**；数百个 Python 脚本。
- subagent 分工：2 个核心数学思想、13 个贡献想法、30 个未成功、13 个 validator、2 个撰写论文。
- 自验证流程：数千次已知零点数值检验、互相评审、下载 **54 篇 arXiv** 查重、独立重证。
- 人的角色主要是鼓励性 prompt（"keep going" / "believe in yourself"）；该模式曾用于协助反驳 **Jacobian 猜想**。

## 定位

- Anthropic 明言**不指望该技术证明 Riemann 假设**；价值在于 AI 数学能力进步速率的最新例证，以及「未成功探索的意外副产品」范式。
- 与 [2026-08-11 Conference Digest](../synthesis/2026-08-11/conference-digest.md) 的 ICLR 2026 RSI（自进化 Agent 研究）主线互相印证。

## 置信度

- 数字（41.6% → 67.2%、31M tokens、60 subagents、2,400 commands、54 papers）均来自 Anthropic 官方页面（high confidence，single-source 为 Anthropic 自身）。
- 数学结果的正确性由外部专家 Conrey/Goldston 审阅 + Lean comparator 背书（high confidence），但截至收录时尚未见独立第三方复现或同行评议期刊发表（tentative）。

## 相关页面

- [2026-08-11 Conference Digest](../synthesis/2026-08-11/conference-digest.md)
- [2026-08-11 arXiv Paper Check](../synthesis/2026-08-11/arxiv-paper-check.md)
