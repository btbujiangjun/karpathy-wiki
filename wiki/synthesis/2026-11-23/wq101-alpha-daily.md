---
title: WorldQuant 101 Alpha 美股 Top 20 精选 — 2026-11-23
type: synthesis
created: 2026-11-23
updated: 2026-11-23
sources: [investment-daily.md]
tags: [wq101-alpha-daily, worldquant, alphas, factor-investing, momentum, reversal, volatility, volume-price, mean-reversion, trend, us-equities, large-cap, daily-digest]
---

# WorldQuant 101 Alpha 美股 Top 20 精选 — 2026-11-23

> 数据基准：Yahoo Finance `v8/finance/chart`（interval=1d, range=20d）日线 OHLCV；因子为横截面代理值（简化定义，非公式回测）；**不构成投资建议**。

---

## 1. 市场概览（美股实时快照）

| 指数 | 收盘 | 涨跌幅 |
|------|------|--------|
| S&P 500 (^GSPC) | 6,910.39 | −3.70% |
| Nasdaq (^IXIC) | 22,617.73 | −5.28% |
| Dow Jones (^DJI) | 48,147.33 | −1.93% |
| VIX (^VIX) | 35.89 | +26.20% |
| 10-Year Treasury (^TNX) | 4.912 | −2.77% |

→ 市场承压：AI/半导体链整体放量回调（AMD −13.25%、AVGO −12.19%、TSM −9.48%、MU −13.89%、ASML −6.63%、MPWR −11.87%）；能源较强（XOM +0.67%）；VIX 反弹 +26.20%（恐慌情绪）。
→ 今日热点（按 WQ101 因子得分排序）：MPWR、T、MU、ASML、ABT（因子共振最强 5 只）。

---

## 2. 方法与评分公式

**候选池**：市值 > $10B 美股组合（43 只，取近 3 期报告（2026-11-15→22）的 Top 20 并集）。

**因子定义**（用户指定的 7 个核心因子；简化说明）：

| Alpha | 用户定义 | 本报告简化解释 |
|-------|----------|----------------|
| #1 动量 | Rank(Correlation(Delay(close,1), close, 10)) | A1 = pearson(C[i−1], C[i]) 近 10 对收盘滞后相关；正 = 动量 |
| #6 开盖-量 | Correlation(open, volume, 10) | A6 = pearson(open, volume) 近 10 日 |
| #12 量价背离 | sign(delta(volume,1)) × (−delta(close,1)) | A12 = sign(ΔV)×(−ΔC)（最近一个计量）；正 = 成交量上升 + 价跌同步 |
| #19 均值回复 | (−1×rank((stddev(|C−O|,5) + (C−O) + rank(corr(C,O,10))))) | A19 = −(σ5 + Δ(C−O) + ρ10)；正 = 均值回复压力 |
| #30 波动结构 | 用户公式 | A30 = (2C−L−H)/(H−L)；正 = 收价在区间高端（强势结构） |
| #41 趋势强度 | ((H·L)^0.5 − vwap) | A41 = √(H·L) − (H+L+C)/3（vwap 取典型价）；正 = 价格在典型价上方 |
| #53 反转 | −Delta((((C−L)−(H−C))/(C−L)), 9) | X = (2C−L−H)/(C−L)，A53 = X[t−9]−X[t]；正 = 比率下降（价格下行/反转压力） |

**评分**：
- 横截面 z：每个因子对全样本计算 z，f = 10·tanh(|z|/2)（0–10，符号为方向）；匹配核心因子 = 每只股 f 最高的 2 个因子。
- 综合评分 = clip(round(5 + mean(匹配因子 f)), 0, 10)；Top 20 按 (综合评分 desc, 匹配因子分和 desc) 排序。

---

## 3. Top 20 排名表

| 排名 | 股票代码 | 公司名称（中英文） | 板块 | 市值 | 综合评分 | 匹配 Alpha 因子 |
|------|----------|-------------------|------|------|----------|-----------------|
| 1 | MPWR | Monolithic Power Systems, Inc.（美国高压系统） | Technology | $55,695,000,000 | 10 | Alpha#41、Alpha#19 |
| 2 | T | AT&T Inc.（AT&T） | Communication Services | $150,291,000,000 | 10 | Alpha#6、Alpha#30 |
| 3 | MU | Micron Technology, Inc.（美信捷诺） | Technology | $672,642,000,000 | 10 | Alpha#19、Alpha#12 |
| 4 | ASML | ASML Holding N.V.（ASML 控股） | Technology | $488,024,000,000 | 10 | Alpha#12、Alpha#41 |
| 5 | ABT | Abbott Laboratories（雅培） | Healthcare | $178,390,000,000 | 10 | Alpha#6、Alpha#1 |
| 6 | AMD | Advanced Micro Devices, Inc.（超威） | Technology | $702,393,000,000 | 10 | Alpha#6、Alpha#41 |
| 7 | DE | Deere & Company（约翰迪尔） | Industrials | $164,269,000,000 | 10 | Alpha#30、Alpha#1 |
| 8 | AVGO | Broadcom Inc.（博通） | Technology | $1,453,000,000,000 | 10 | Alpha#6、Alpha#19 |
| 9 | TSM | Taiwan Semiconductor Manufacturing Company Limited（台积电） | Technology | $1,653,000,000,000 | 10 | Alpha#53、Alpha#1 |
| 10 | EQIX | Equinix, Inc.（思存） | Real Estate | $95,842,000,000 | 10 | Alpha#19、Alpha#41 |
| 11 | XOM | ExxonMobil Holdings Corporation（埃克森美孚） | Energy | ~$720B | 10 | Alpha#30、Alpha#6 |
| 12 | JNJ | Johnson & Johnson（强生） | Healthcare | ~$680B | 10 | Alpha#30、Alpha#1 |
| 13 | KDP | Keurig Dr Pepper, Inc. | Consumer Staples | $49,738,000,000 | 9 | Alpha#6、Alpha#30 |
| 14 | GS | The Goldman Sachs Group, Inc.（摩根斯坦利） | Financials | $228,062,000,000 | 9 | Alpha#12、Alpha#19 |
| 15 | ABBV | AbbVie Inc. | Healthcare | ~$520B | 9 | Alpha#30、Alpha#1 |
| 16 | BLK | BlackRock, Inc.（美国黑石） | Financials | $170,131,000,000 | 9 | Alpha#1、Alpha#19 |
| 17 | PH | Parker-Hannifin Corporation（派克-汉尼芬） | Industrials | $109,939,000,000 | 9 | Alpha#41、Alpha#19 |
| 18 | DUK | Duke Energy Corporation（杜克能源） | Utilities | $101,191,000,000 | 9 | Alpha#6、Alpha#30 |
| 19 | AAPL | Apple Inc.（苹果） | Technology | ~$5.25T | 8 | Alpha#6、Alpha#30 |
| 20 | UNH | UnitedHealth Group Incorporated（美国联合健康） | Healthcare | $304,513,000,000 | 8 | Alpha#1、Alpha#30 |

---

## 4. 逐股详情（Top 20）

### 1. MPWR — Monolithic Power Systems, Inc.（美国高压系统）
- **股票代码**：MPWR · **板块**：Technology · **市值**：$55,695,000,000 · **今日价**：$1,142.05 · **涨跌幅**：−11.87%
- **匹配 Alpha 因子**：Alpha#41、Alpha#19
- **因子信号解读**：Alpha#41：方向正，f=9.77 — A41 = √(H·L)−vwap = +17.98（价格在典型价上方，趋势强）；Alpha#19：方向正，f=9.71 — A19 = −(σ5+Δ+ρ10) = +74.79（收价在开盖下方，均值回复压力）。
- **综合评分**：10
- **投资逻辑**：半导体功率器件龙头，A41 趋势强 + A19 均值回复压力共振，AI 基建链传导明确，今日放量回调筹码流动。
- **风险提示**：AI 需求疑虑；高估值敏感；周期波动。

### 2. T — AT&T Inc.（AT&T）
- **股票代码**：T · **板块**：Communication Services · **市值**：$150,291,000,000 · **今日价**：$22.31 · **涨跌幅**：+2.11%
- **匹配 Alpha 因子**：Alpha#6、Alpha#30
- **因子信号解读**：Alpha#6：方向正，f=8.72 — A6 = pearson(open,volume,10) = +0.372（开盖-量同向）；Alpha#30：方向正，f=8.44 — A30 = (2C−L−H)/(H−L) = −0.313（价格略偏区间中点）。
- **综合评分**：10
- **投资逻辑**：电信垂直龙头，开盖-量共振，今日 +2.11% 规律上行，分红防御。
- **风险提示**：电信业务收益率下行、分红政策；5G 投资推迟；债务信用。

### 3. MU — Micron Technology, Inc.（美信捷诺）
- **股票代码**：MU · **板块**：Technology · **市值**：$672,642,000,000 · **今日价**：$594.51 · **涨跌幅**：−13.89%
- **匹配 Alpha 因子**：Alpha#19、Alpha#12
- **因子信号解读**：Alpha#19：方向正，f=8.29 — A19 = −(σ5+Δ+ρ10) = +46.39（收价在开盖下方，均值回复压力）；Alpha#12：方向正，f=8.23 — A12 = sign(ΔV)×(−ΔC) = +95.93（放量价跌，资金流入确认）。
- **综合评分**：10
- **投资逻辑**：内存龙头，A19/A12 同向共振，AI 需求驱动基本面反弹预期，放量回调结构承接。
- **风险提示**：放量 −13.9% 为周期顶部区间，反弹未确认；缺乏新增增长引擎；高波动。

### 4. ASML — ASML Holding N.V.（ASML 控股）
- **股票代码**：ASML · **板块**：Technology · **市值**：$488,024,000,000 · **今日价**：$1,266.22 · **涨跌幅**：−6.63%
- **匹配 Alpha 因子**：Alpha#12、Alpha#41
- **因子信号解读**：Alpha#12：方向正，f=7.91 — A12 = +89.98（放量下跌，资金流入）；Alpha#41：方向正，f=7.71 — A41 = √(H·L)−vwap = +9.89（价格在典型价上方）。
- **综合评分**：10
- **投资逻辑**：EUV 垄断龙头，趋势+量价共振，逆势放量可能是均值回复，先进制程扩产周期。
- **风险提示**：地缘出口管制；结构压力仍存；高估值。

### 5. ABT — Abbott Laboratories（雅培）
- **股票代码**：ABT · **板块**：Healthcare · **市值**：$178,390,000,000 · **今日价**：$103.00 · **涨跌幅**：−0.84%
- **匹配 Alpha 因子**：Alpha#6、Alpha#1
- **因子信号解读**：Alpha#6：方向正，f=9.06 — A6 = pearson(open,volume,10) = +0.469（开盖-量同向）；Alpha#1：方向正，f=5.17 — A1 = pearson(C[t−1],C[t],10) = +0.906（近 10 日动量强）。
- **综合评分**：10
- **投资逻辑**：医药巨头，价量共振+动量共振，防御+增长双属性。
- **风险提示**：药物研发与专利风险；获利能力平稳。

### 6. AMD — Advanced Micro Devices, Inc.（超威）
- **股票代码**：AMD · **板块**：Technology · **市值**：$702,393,000,000 · **今日价**：$424.39 · **涨跌幅**：−13.25%
- **匹配 Alpha 因子**：Alpha#6、Alpha#41
- **因子信号解读**：Alpha#6：方向正，f=6.53 — A6 = pearson(open,volume,10) = +0.032（开盖-量弱正）；Alpha#41：方向正，f=4.85 — A41 = √(H·L)−vwap = +6.58。
- **综合评分**：10
- **投资逻辑**：AI 芯片代理龙头，量价同向、开盖放量回调，低位筹码流动，AI 增长确定性高。
- **风险提示**：AI 需求疑虑；估值分化；低位止跌支撑不确定。

### 7. DE — Deere & Company（约翰迪尔）
- **股票代码**：DE · **板块**：Industrials · **市值**：$164,269,000,000 · **今日价**：$609.25 · **涨跌幅**：−2.5%
- **匹配 Alpha 因子**：Alpha#30、Alpha#1
- **因子信号解读**：Alpha#30：方向正，f=5.68 — A30 = (2C−L−H)/(H−L) = −0.522（价格偏低端）；Alpha#1：方向正，f=5.48 — A1 = pearson(C[t−1],C[t],10) = +0.920（趋势持续）。
- **综合评分**：10
- **投资逻辑**：农机龙头，动量+趋势共振，AI 基建传导优。
- **风险提示**：农产品期货波动+荷兰一波段干旱；周期。

### 8. AVGO — Broadcom Inc.（博通）
- **股票代码**：AVGO · **板块**：Technology · **市值**：$1,453,000,000,000 · **今日价**：$304.41 · **涨跌幅**：−12.19%
- **匹配 Alpha 因子**：Alpha#6、Alpha#19
- **因子信号解读**：Alpha#6：方向正，f=6.61 — A6 = pearson(open,volume,10) = +0.040（开盖-量弱）；Alpha#19：方向正，f=4.43 — A19 = −(σ5+Δ+ρ10) = +24.46（收价在开盖下方，均值回复压力）。
- **综合评分**：10
- **投资逻辑**：云网络龙头，均值回复+开盖放量，低位止跌筹码。
- **风险提示**：NVIDIA 供应链分歧；估值高位。

### 9. TSM — Taiwan Semiconductor Manufacturing Company Limited（台积电）
- **股票代码**：TSM · **板块**：Technology · **市值**：$1,653,000,000,000 · **今日价**：$318.71 · **涨跌幅**：−9.48%
- **匹配 Alpha 因子**：Alpha#53、Alpha#1
- **因子信号解读**：Alpha#53：方向正，f=6.71 — A53 = X[t−9]−X[t] = +108.18（9 日收盘位置反转压力显著）；Alpha#1：方向正，f=3.65 — A1 = pearson(C[t−1],C[t],10) = +0.840。
- **综合评分**：10
- **投资逻辑**：先进制程代工龙头，反转压力+动量共振，低位承接，CoWoS 封装瓶颈。
- **风险提示**：资本开支周期；客户集中；地缘供应链。

### 10. EQIX — Equinix, Inc.（思存）
- **股票代码**：EQIX · **板块**：Real Estate · **市值**：$95,842,000,000 · **今日价**：$968.22 · **涨跌幅**：−4.89%
- **匹配 Alpha 因子**：Alpha#19、Alpha#41
- **因子信号解读**：Alpha#19：方向正，f=5.49 — A19 = −(σ5+Δ+ρ10) = +28.82（收价在开盖下方，均值回复压力）；Alpha#41：方向正，f=4.84 — A41 = √(H·L)−vwap = +6.57。
- **综合评分**：10
- **投资逻辑**：数据中心 REIT 龙头，均值回复+趋势共振，AI 基建租赁强劲。
- **风险提示**：市场租金变化；宏观投资意愿。

### 11. XOM — ExxonMobil Holdings Corporation（埃克森美孚）
- **股票代码**：XOM · **板块**：Energy · **市值**：~$720B · **今日价**：$159.99 · **涨跌幅**：+0.67%
- **匹配 Alpha 因子**：Alpha#30、Alpha#6
- **因子信号解读**：Alpha#30：方向正，f=9.62 — A30 = (2C−L−H)/(H−L) = −0.051（价格略低于区间中点，结构弱）；Alpha#6：方向正，f=0.63 — A6 = pearson(open,volume,10) = −0.403（弱负）。
- **综合评分**：10
- **投资逻辑**：能源巨头，量能结构承接，石油/炼油价格弹性与现金流。
- **风险提示**：油价与炼油价差；能源转型政策；地缘政治。

### 12. JNJ — Johnson & Johnson（强生）
- **股票代码**：JNJ · **板块**：Healthcare · **市值**：~$680B · **今日价**：$270.47 · **涨跌幅**：+1.25%
- **匹配 Alpha 因子**：Alpha#30、Alpha#1
- **因子信号解读**：Alpha#30：方向正，f=8.21 — A30 = (2C−L−H)/(H−L) = −0.340（价格偏低端）；Alpha#1：方向正，f=1.56 — A1 = pearson(C[t−1],C[t],10) = +0.762。
- **综合评分**：10
- **投资逻辑**：医药多元化巨头，结构承接+动量，防御稳健。
- **风险提示**：药物研发；诉讼；政策。

### 13. KDP — Keurig Dr Pepper, Inc.
- **股票代码**：KDP · **板块**：Consumer Staples · **市值**：$49,738,000,000 · **今日价**：$34.84 · **涨跌幅**：+1.25%
- **匹配 Alpha 因子**：Alpha#6、Alpha#30
- **因子信号解读**：Alpha#6：方向正，f=6.74 — A6 = pearson(open,volume,10) = +0.054；Alpha#30：方向正，f=2.22 — A30 = (2C−L−H)/(H−L) = −0.671（价格偏低端）。
- **综合评分**：9
- **投资逻辑**：美国饮料龙头，开盖-量同向，防御+分红。
- **风险提示**：市场份额竞争；渠道政策。

### 14. GS — The Goldman Sachs Group, Inc.（摩根斯坦利）
- **股票代码**：GS · **板块**：Financials · **市值**：$228,062,000,000 · **今日价**：$790.69 · **涨跌幅**：−6.71%
- **匹配 Alpha 因子**：Alpha#12、Alpha#19
- **因子信号解读**：Alpha#12：方向正，f=5.15 — A12 = +56.84（放量下跌）；Alpha#19：方向正，f=3.71 — A19 = −(σ5+Δ+ρ10) = +21.79（收价在开盖下方，均值回复压力）。
- **综合评分**：9
- **投资逻辑**：投行龙头，资本市场增长期间的债券/承销收入，资本结构健康。
- **风险提示**：信贷周期；利率；受法规环境；估值。

### 15. ABBV — AbbVie Inc.
- **股票代码**：ABBV · **板块**：Healthcare · **市值**：~$520B · **今日价**：$286.20 · **涨跌幅**：+0.94%
- **匹配 Alpha 因子**：Alpha#30、Alpha#1
- **因子信号解读**：Alpha#30：方向正，f=6.12 — A30 = (2C−L−H)/(H−L) = −0.498；Alpha#1：方向正，f=2.50 — A1 = pearson(C[t−1],C[t],10) = +0.796。
- **综合评分**：9
- **投资逻辑**：免疫与肿瘤管线现金流强、分红稳定，结构承接+动量共振。
- **风险提示**：专利到期与管线接续；药价政策；并购整合。

### 16. BLK — BlackRock, Inc.（美国黑石）
- **股票代码**：BLK · **板块**：Financials · **市值**：$170,131,000,000 · **今日价**：$1,101.72 · **涨跌幅**：−3%
- **匹配 Alpha 因子**：Alpha#1、Alpha#19
- **因子信号解读**：Alpha#1：方向正，f=4.50 — A1 = pearson(C[t−1],C[t],10) = +0.875；Alpha#19：方向正，f=3.83 — A19 = −(σ5+Δ+ρ10) = +22.22（收价在开盖下方，均值回复压力）。
- **综合评分**：9
- **投资逻辑**：资产管理龙头，动量+均值回复共振。
- **风险提示**：管理费与资本流失；市场调整。

### 17. PH — Parker-Hannifin Corporation（派克-汉尼芬）
- **股票代码**：PH · **板块**：Industrials · **市值**：$109,939,000,000 · **今日价**：$871.86 · **涨跌幅**：−3.78%
- **匹配 Alpha 因子**：Alpha#41、Alpha#19
- **因子信号解读**：Alpha#41：方向正，f=4.38 — A41 = √(H·L)−vwap = +6.18；Alpha#19：方向正，f=3.84 — A19 = −(σ5+Δ+ρ10) = +22.26（收价在开盖下方，均值回复压力）。
- **综合评分**：9
- **投资逻辑**：高压器件龙头，趋势+均值回复共振，工业自动化分散增长。
- **风险提示**：行业周期性；自动化支出推迟。

### 18. DUK — Duke Energy Corporation（杜克能源）
- **股票代码**：DUK · **板块**：Utilities · **市值**：$101,191,000,000 · **今日价**：$129.78 · **涨跌幅**：+0.71%
- **匹配 Alpha 因子**：Alpha#6、Alpha#30
- **因子信号解读**：Alpha#6：方向正，f=5.93 — A6 = pearson(open,volume,10) = −0.028（弱）；Alpha#30：方向正，f=1.61 — A30 = (2C−L−H)/(H−L) = −0.693（价格偏低端）。
- **综合评分**：9
- **投资逻辑**：公用事业龙头，高分红防御，开盖-量弱。
- **风险提示**：监管比例；利率敏感；负债率。

### 19. AAPL — Apple Inc.（苹果）
- **股票代码**：AAPL · **板块**：Technology · **市值**：~$5.25T · **今日价**：$342.56 · **涨跌幅**：−1.9%
- **匹配 Alpha 因子**：Alpha#6、Alpha#30
- **因子信号解读**：Alpha#6：方向正，f=5.68 — A6 = pearson(open,volume,10) = −0.051（非常弱）；Alpha#30：方向正，f=1.15 — A30 = (2C−L−H)/(H−L) = −0.71（价格偏低端）。
- **综合评分**：8
- **投资逻辑**：消费电子+服务双引擎，回购缓冲，趋势弱但结构承接。
- **风险提示**：换机周期；中国供应链；AI 端侧兑现步伐。

### 20. UNH — UnitedHealth Group Incorporated（美国联合健康）
- **股票代码**：UNH · **板块**：Healthcare · **市值**：$304,513,000,000 · **今日价**：$339.85 · **涨跌幅**：+2.84%
- **匹配 Alpha 因子**：Alpha#1、Alpha#30
- **因子信号解读**：Alpha#1：方向正，f=4.03 — A1 = pearson(C[t−1],C[t],10) = +0.856；Alpha#30：方向正，f=2.76 — A30 = (2C−L−H)/(H−L) = −0.65（价格偏低端，强度为全样本正向）。
- **综合评分**：8
- **投资逻辑**：医疗保险巨头，动量+结构共振，防御+成长双属性。
- **风险提示**：监管比例；利润率；大病需求波动。

---

## 5. 板块分类汇总（Top 20）

### Technology（科技）— 7 只
MPWR、MU、ASML、AMD、AVGO、TSM、AAPL
### Communication Services（通信服务）— 1 只
T
### Real Estate（房地产）— 1 只
EQIX
### Industrials（工业）— 2 只
DE、PH
### Healthcare（医疗保健）— 4 只
ABT、JNJ、ABBV、UNH
### Energy（能源）— 1 只
XOM
### Utilities（公用事业）— 1 只
DUK
### Financials（金融）— 2 只
GS、BLK
### Consumer Staples（消费品）— 1 只
KDP

板块分布：Technology 35%、Healthcare 20%、Financials 10%、Industrials 10%、Communication Services 5%、Real Estate 5%、Energy 5%、Utilities 5%、Consumer Staples 5%。

---

## 6. 免责声明

因子为横截面代理值（非公式回测）；数据基准为 Yahoo Finance 实时数据；市值数据取自近期 wq101 报告（2026-11-15→22），可能缺少新入池股的最新值；**不构成投资建议**。
