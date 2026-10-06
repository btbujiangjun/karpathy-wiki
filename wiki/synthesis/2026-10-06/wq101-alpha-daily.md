---
title: WorldQuant 101 Alphas - 美股 Top 20 股票精选 (2026-10-06)
type: synthesis
created: 2026-10-06
updated: 2026-10-06
sources: []
tags: [quant, worldquant-101-alphas, stock-screening, us-equities, large-cap]
---
# WorldQuant 101 Alphas - 美股 Top 20 股票精选 (2026-10-06)

> 基于 WorldQuant 101 Alpha 因子库对美股大盘股（市值 > $10B）进行量化筛选，结合动量、反转、波动率、量价关系等多维度因子进行综合打分。

## 分析框架说明

本次筛选基于以下 7 个经典 WorldQuant 101 Alpha 因子：

| Alpha | 公式（核心逻辑） | 因子类型 | 投资逻辑 |
|---|---|---|---|
| Alpha#1 | `Rank(Ts_ArgMax(SignedPower(((returns<0)?stddev(returns,20):close), 2), 5)) - 0.5` | 动量/趋势 | 捕捉近期价格波动结构，偏好具有持续动量特征的股票 |
| Alpha#6 | `-1 * Correlation(open, volume, 10)` | 动量/量价 | 量价背离信号，负相关可能预示资金流入变化 |
| Alpha#12 | `sign(delta(volume,1)) * (-1 * delta(close,1))` | 量价背离 | 成交量上升伴随价格回调时发出信号，捕捉短期量价关系 |
| Alpha#19 | `(-1 * sign((close - delay(close,7)) + delta(close,7))) * (1 + rank(1 + sum(returns,250)))` | 均值回复/趋势 | 综合短期价格变化与长期收益，识别趋势延续或反转 |
| Alpha#30 | `(-1 * rank(2*scale(rank(IV*volume)) - scale(rank(delta(close,3)))))*sum(volume,5)` | 波动率/价量 | 基于日内波动幅度（IV = (close-low-high+close)/(high-low)）与成交量的复合信号 |
| Alpha#41 | `(high*low)^0.5 - vwap` | 趋势强度 | 代表交易日内价格中枢偏移，正值表明价格运行在 VWAP 之上，趋势偏强 |
| Alpha#53 | `-1 * delta((((close-low)-(high-close))/(close-low)), 9)` | 反转 | 9日变化的蜡烛内在强度（body/price range），负delta可能预示形态变化 |
