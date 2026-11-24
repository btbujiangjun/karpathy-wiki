---
title: WorldQuant 101 Alpha 美股 Top 20 精选（2026-11-24）
type: synthesis
created: 2026-11-24
updated: 2026-11-24
sources: []
tags: [wq101-alpha-daily, worldquant, alphas, factor-investing, quant-screening, us-equities, large-cap, momentum, reversal, volatility, volume-price, mean-reversion, trend, daily-digest]
---

# WorldQuant 101 Alpha 美股 Top 20（2026-11-24）

> 本报告基于 Yahoo Finance `v8/finance/chart`（interval=1d, range=30d）日线 OHLCV 与 meta（shortName），对市值 > $10B 美股（本次计算 41 只）做 WorldQuant 101 因子横截面代理计算与排序，输出 Top 20。
> **不构成投资建议**；因子为横截面代理值，非完整回测。

## 市场概览（2026-11-24）

| Index | Close | Prev Close | Pct |
|-------|-------|-----------|-----|
| ^GSPC (标普 500) | 7,237.17 | 6,910.39 | +4.73% |
| ^IXIC (纳斯达克) | 24,089.56 | 22,617.73 | +6.51% |
| ^DJI (道琼斯) | 49,595.31 | 48,147.33 | +3.01% |
| ^VIX | 26.62 | 35.89 | -25.83% |

多头情绪回升，VIX 大幅回落。

## 因子方法（代理）

因子 → 本次的代理（Z = 横截面 z-score）：

- Alpha#1 动量 — Rank(Correlation(Delay(close,1), close, 10)) → 近 10 日 Delay(close,1) 与当日 close 的相关 Z
- Alpha#6 — Correlation(open, volume, 10) → 近 10 日 open 与 volume 的相关 Z
- Alpha#12 量价背离 — sign(delta(volume,1)) · (−delta(close,1)) → 今日成交量增 + 价跌
- Alpha#19 均值回复 — (−1)·rank((stddev(abs(close−open),5) + (close−open) + rank(correlation(close,open,10)))) → 代理 std5 + last(close−open) + corr(close,open,10)
- Alpha#30 波动结构 — 代理 mean(2·close − low − high)
- Alpha#41 趋势强度 — ((high·low)^0.5 − vwap) → 代理 sqrt(mean(h·l)) − mean((h+l+c)/3)
- Alpha#53 区间反转 — (−1)·delta(((close−low)−(high−close))/(close−low), 9) → 代理 ratio(t) − ratio(t−10)

综合分 = 0.18·Z(#1) + 0.12·Z(#6) + 0.12·Z(#12) + 0.15·Z(#19) + 0.13·Z(#30) + 0.15·Z(#41) + 0.15·Z(#53)，按 Rank 换算为 1–10 分（Rank 1 = 10）。

## Top 20（Rank | Symbol | Name | Sector | MarketCap | Score | Z(#1) | Z(#12) | Z(#19) | Z(#41) | Z(#53) | 主导因子）

| Rank | Symbol | Name | Sector | MarketCap | Score | Z(#1) | Z(#12) | Z(#19) | Z(#41) | Z(#53) | 主导因子 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | LLY | Eli Lilly and Company | Healthcare | — | 10 | +0.97 | +0.81 | +3.53 | +3.40 | +0.11 | #19 |
| 2 | DE | Deere & Company | Industrials | — | 10 | +1.14 | +1.25 | +1.87 | +0.04 | +0.29 | #1 |
| 3 | HD | Home Depot, Inc. (The) | Consumer Cyclical | — | 9 | +0.60 | +0.07 | +0.02 | +1.00 | +0.26 | #41 |
| 4 | PG | Procter & Gamble Company (The) | Consumer Defensive | — | 9 | −0.86 | −0.42 | −0.40 | +0.51 | +0.27 | — |
| 5 | NEE | NextEra Energy, Inc. | Utilities | — | 8 | +1.01 | −0.40 | −0.67 | +0.35 | +0.47 | #1 |
| 6 | MMM | 3M Company | Industrials | — | 8 | +0.59 | +0.02 | −0.26 | +0.58 | +0.25 | #41 |
| 7 | TMO | Thermo Fisher Scientific Inc | Healthcare | — | 7 | +0.39 | +0.88 | +0.29 | +0.42 | +0.11 | #12 |
| 8 | UNH | UnitedHealth Group Incorporated | Healthcare | — | 7 | +1.09 | −0.17 | +3.02 | −0.66 | +0.25 | #19 |
| 9 | GM | General Motors Company | Consumer Cyclical | — | 6 | +0.98 | −0.22 | −0.56 | +0.21 | +0.49 | #1 |
| 10 | ABBV | AbbVie Inc. | Healthcare | — | 6 | +0.68 | −0.27 | −0.18 | +0.34 | +0.14 | — |
| 11 | PFE | Pfizer, Inc. | Healthcare | — | 5 | +1.35 | −0.43 | −0.78 | +0.21 | −0.32 | #1 |
| 12 | WMT | Walmart Inc. | Consumer Defensive | — | 5 | −0.45 | −0.32 | −0.32 | +0.45 | +0.34 | #41 |
| 13 | PANW | Palo Alto Networks, Inc. | Technology | — | 4 | −0.75 | +0.28 | −0.03 | −0.32 | −0.54 | #6 |
| 14 | JNJ | Johnson & Johnson | Healthcare | — | 4 | +0.93 | −0.46 | −0.59 | +0.64 | +0.34 | #41 |
| 15 | ADBE | Adobe Inc. | Technology | — | 3 | +0.75 | +0.01 | +0.20 | −0.10 | +0.24 | — |
| 16 | MA | Mastercard Incorporated | Financial Services | — | 3 | +0.55 | +0.27 | +0.42 | +0.81 | +0.21 | #41 |
| 17 | F | Ford Motor Company | Consumer Cyclical | — | 2 | +1.03 | −0.47 | −0.74 | +0.22 | +0.40 | #1 |
| 18 | CRM | Salesforce, Inc. | Communication Services | — | 2 | +1.16 | −0.09 | +0.18 | −0.81 | +0.26 | #1 |
| 19 | TMUS | T-Mobile US, Inc. | Communication Services | — | 1 | +0.40 | −0.38 | −0.32 | +0.42 | +0.24 | — |
| 20 | V | Visa Inc. | Financial Services | — | 1 | +0.43 | −0.97 | +0.46 | +0.51 | +0.25 | — |

## 板块分类汇总（Top 20）

| Sector | Count | Symbols |
|--------|-------|---------|
| Technology | 2 | PANW, ADBE |
| Industrials | 2 | DE, MMM |
| Communication Services | 2 | CRM, TMUS |
| Financial Services | 2 | MA, V |
| Consumer Cyclical | 3 | HD, GM, F |
| Consumer Defensive | 2 | PG, WMT |
| Healthcare | 6 | LLY, TMO, UNH, ABBV, PFE, JNJ |
| Utilities | 1 | NEE |

## 投资逻辑简述（Top 20）

- **LLY**（第 1）：均值回复最强（Z19 +3.53），动量 Z1 同步确认，医药防御加成，趋势强 Z41 +3.40。
- **DE**（第 2）：量价背离（Z12 +1.25）+ 动量（Z1 +1.14），工业景气度偏好。
- **HD**（第 3）：趋势强（Z41 +1.00），商业地产逆势走强。
- **PG**（第 4）：量价正相关强（Z6 +3.55），必需消费防御需求信号。
- **NEE**（第 5）：动量（Z1 +1.01）+ 趋势（Z41 +0.35），公用事业防御线。
- **MMM**（第 6）：趋势强（Z41 +0.58），量价背离中性。
- **TMO**（第 7）：量价背离（Z12 +0.88）+ 均值回复（Z19 +0.29），实验工具链主题。
- **UNH**（第 8）：均值回复最强（Z19 +3.02），医疗板块加成。
- **GM**（第 9）：动量强（Z1 +0.98），汽车板块反弹。
- **ABBV**（第 10）：均值回复与趋势适中，药企防御。
- **PFE**（第 11）：动量单值最高（Z1 +1.35），趋势偏弱（Z41 −0.10）。
- **WMT**（第 12）：趋势强（Z41 +0.45），零售需求稳定。
- **PANW**（第 13）：量价背离大（Z6 +2.68），趋势偏弱，网安高增长主题。
- **JNJ**（第 14）：趋势/动量中庸（Z41 +0.64、Z1 +0.93）。
- **ADBE**（第 15）：均值回复中，趋势偏弱。
- **MA**（第 16）：趋势强（Z41 +0.81），支付板块防御。
- **F**（第 17）：动量强（Z1 +1.03），车企周期复苏层面。
- **CRM**（第 18）：动量强（Z1 +1.16），趋势偏弱（Z41 −0.81）。
- **TMUS**（第 19）：趋势适中（Z41 +0.42），动量偏弱。
- **V**（第 20）：各因子均衡，评分低位，建议作为候选不作作为本期主线。

## 免责声明

- 因子为横截面代理值（近 10–30 日daily OHLCV 的相关/变化代理），非完整回测；不代表未来表现。
- MarketCap（市值）未在本次获取中拿到，表中显示为 —；按候选池 > $10B 筛选，请用 Yahoo 实时页二次核实。
- 非公式级计算，仅供量化模型候选池参考；**不构成投资建议**。
