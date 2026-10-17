---
title: "WorldQuant 101 Alpha 选股日报 — 2026-10-17（美股）"
type: synthesis
created: 2026-10-17
updated: 2026-10-17
sources:
  - synthesis/2026-10-17/wq101-alpha-daily.md
tags:
  - worldquant
  - 101-alpha
  - quant
  - stock-selection
  - us-equities
  - momentum
  - reversal
  - volatility
  - volume-price
  - mean-reversion
  - daily-digest
  - synthesis-date-organized
---

## 市场概览（今日美股，2026-10-17）

根据实时市场观察（Fri, Oct 16, 2026 收盘，媒体综合）：
- S&P 500：7,659.44（-1.09%，周跌 -1.95%）
- Nasdaq Composite：26,140.03（-2.14%，周跌 -4.48%）
- Dow Jones：52,002.41（-0.34%，周涨 +0.67%）
- VIX：>22（四个月新高）
- 油价：WTI $101.41（+3.51%），Brent $109.86（+3.72%）

市场特征：
- AI/半导体板块持续承压（NVDA -1.43%，AMD -5.95%，AVGO -4.52%，MU -5.63%，SMH 周跌 -9.70%），市场对 AI 基建杠杆和回报时点担忧加剧。
- 资金出现轮动，防御/能源/公用事业表现相对抗跌（Energy +2.47%，Utilities +1.4%）。
- 三季报季开端，市场对财报和“AI 回报兑现”更为敏感。
- 中东局势及油价上行进一步强化通胀粘性预期，限制了 Fed 近期降息预期（市场预期本月维持利率的概率约 82%）。

选股思路：在科技回调中，结合 WorldQuant 101 Alpha 因子逻辑，优先筛选：动量衰减但未崩、成交量确认、波动率收敛、以及在轮动中受益或估值/基本面相对稳健的大盘股（市值>$10B）。

## WorldQuant 101 Alpha 因子（本次选股所用核心因子）

| 因子 | 公式（WorldQuant 101 概念） | 信号逻辑 |
|---|---|---|
| Alpha#1 | Rank(Correlation(Delay(close,1), close, 10)) | 近10日收盘价与昨日收盘的相关性排序；相关性较高反映延续性动量。 |
| Alpha#6 | Correlation(open, volume, 10) | 近10日开盘价与成交量的相关性；量价联动强弱。 |
| Alpha#12 | sign(delta(volume,1)) * (-1 * delta(close,1)) | 昨日成交量变动方向×（-1×收盘价变动）；关注量增价跌/量减价升等背离信号。 |
| Alpha#19 | (-1 * rank((stddev(abs(close-open),5) + (close-open) + rank(correlation(close,open,10))))) | 综合日内波动、收盘-开盘、收盘与开盘相关性；偏向均值回复倾向（数值越高越有利）。 |
| Alpha#30 | (-1 * rank(...))*sum(volume,5)（概念化表述） | 高频波动/结构信号与短期成交量叠加，强调波动率调整后的强度。 |
| Alpha#41 | ((high*low)^0.5 - vwap) | 几何均价（高低均值）相对 VWAP 偏离；价格相对成交均价的位置。 |
| Alpha#53 | -1 * Delta((((close-low)-(high-close))/(close-low)), 9) | 9日变动：计算内盘强度（close-low vs high-close）相对区间，负变动可能意味着反转信号。 |

> 注：上述为 WorldQuant 101 Alpha 的公开表述思路，用于日常选股逻辑解读，不等同精确因子值（需平台计算）。

