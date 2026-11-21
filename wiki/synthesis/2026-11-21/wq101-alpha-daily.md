---
title: "WorldQuant 101 Alphas 日报 — 美股 Top 20 — 2026-11-21"
type: synthesis
created: 2026-11-21
updated: 2026-11-21
sources: [investment-daily.md]
tags: [wq101-alpha-daily, worldquant, alphas, factor-investing, momentum, reversal, volatility, volume-price, mean-reversion, trend, us-equities, large-cap, daily-digest]
---

# WorldQuant 101 Alphas 日报 — 美股 Top 20 — 2026-11-21

> 数据基准：US 常规收盘 Nov 20 快照（Yahoo Finance v8/finance/chart, range=3mo 日线）+ 逐股基本面（quoteSummary/quote 页面）；因子为横截面代理值，非公式回测；**不构成投资建议**。

---

## 1. 市场概览（美股快照，Yahoo Finance 实时数据）

| 指数 | 收盘 | 前收 | 涨跌幅 |
|------|------|------|--------|
| S&P 500 (^SPX) | 6,910.39 | 7,175.83 | -3.70% |
| Nasdaq (^IXIC) | 22,617.73 | 23,879.20 | -5.28% |
| Dow Jones (^DJI) | 48,147.33 | 49,097.06 | -1.93% |
| CBOE Volatility Index (^VIX) | 35.89 | 28.44 | +26.20% |
| 10-Year Treasury (^TNX) | 4.91 | 5.05 | -2.77% |
| NYSE Advance/Decline (^NYA) | 22,657.82 | 23,139.81 | -2.08% |

→ 市场整体承压：标普 -3.70%、纳指 -5.28%、道指仅 -1.93%；VIX 飙升至 +26.20%（恐慌压力上升）。与 2026-11-21 投资热点日报（纳指 -5.28%、标普 -3.70%）一致。

---

## 2. 方法与评分公式

**数据来源**：Yahoo Finance `v8/finance/chart`（interval=1d, range=3mo）日线 OHLCV（open/high/low/close/volume；VWAP 近似为典型价 (H+L+C)/3）；`finance.yahoo.com/quote` 页面（marketCap、trailingPE、dividendYield、板块）。候选标的：市值>$10B 美股组合（Yahoo 实时市值）+ Yahoo trending tickers（今日热门），共 62 只。

**因子**（按用户指定的 WorldQuant 101 公式，在横截面上取 z 分数后标准化）：

| Alpha | 计算公式 |
|-------|----------|
| #1 动量 | pearson(close[t−1], close) — 日级动量自相关 |
| #6 开盘-量相关 | pearson(open, volume, 10) |
| #12 量价背离 | sign(Δvolume) × (−Δclose) |
| #19 均值回复 | −z(std5(|c−o|) + (c−o) + rank(corr(c,o,10))) |
| #30 波动率 | −(2·z_moneyFlow − z_Δc3)，moneyFlow = ((c−l)−(h−c))/(h−l) × volume；Δc3 = close − close[t−3] |
| #41 趋势强度 | √(high·low) − vwap（典型价近似 (H+L+C)/3） |
| #53 反转 | r_9 − r_t，r = (2c−l−h)/(c−l) — 收价在区间比率下降 |

**因子信号约定**：方向 = 因子值符号（正值 = 该因子强烈存在，负值 = 该因子压力/承压）；强度 f = 10·tanh(|z|/2)（1-10）。

**评分**：
- 因子评分 = 0.18·f1 + 0.12·f6 + 0.12·f12 + 0.15·f19 + 0.13·f30 + 0.15·f41 + 0.15·f53
- 基本面评分 = PE（8-15→1.5，15-28→2，28-45→1，≥45→0，<8→0.5）+ 分红（>1.2%→1.5，0.3-1.2%→1，<0.3%→0）+ 板块强弱（该板块≥40% 成员因子评分>5→1）
- 综合评分 = round(0.7 × 因子评分 + 0.3 × 基本面评分)，1-10 分

---

## 3. Top 20 排名表

| 排名 | 股票 | 板块 | 市值 | 综合评分 | 核心 Alpha 因子 |
|------|------|------|------|----------|----------------|
| 1 | MPWR | Semiconductors | $55,695,000,000 | 5 | Alpha#12 + Alpha#19 |
| 2 | ASML | Semiconductor Equipment & Materials | $488,024,000,000 | 4 | Alpha#12 + Alpha#41 |
| 3 | MU | Semiconductors | $672,642,000,000 | 4 | Alpha#12 + Alpha#19 |
| 4 | EQIX | REIT - Specialty | $95,842,000,000 | 4 | Alpha#1 + Alpha#19 |
| 5 | AMZN | Internet Retail | $2,669,000,000,000 | 4 | Alpha#1 + Alpha#53 |
| 6 | GS | Capital Markets | $228,062,000,000 | 4 | Alpha#12 + Alpha#19 |
| 7 | AVGO | Semiconductors | $1,453,000,000,000 | 3 | Alpha#1 + Alpha#19 |
| 8 | PH | Specialty Industrial Machinery | $109,939,000,000 | 3 | Alpha#41 + Alpha#1 |
| 9 | NVDA | Semiconductors | $3,031,000,000,000 | 3 | Alpha#30 + Alpha#6 |
| 10 | INTC | Semiconductors | $272,553,000,000 | 3 | Alpha#30 + Alpha#1 |
| 11 | BLK | Asset Management | $170,131,000,000 | 3 | Alpha#6 + Alpha#19 |
| 12 | CAT | Farm & Heavy Construction Machinery | $233,579,000,000 | 3 | Alpha#6 + Alpha#1 |
| 13 | TSM | Semiconductors | $1,653,000,000,000 | 3 | Alpha#53 + Alpha#6 |
| 14 | DUK | Utilities - Regulated Electric | $101,191,000,000 | 3 | Alpha#6 + Alpha#1 |
| 15 | MRK | Drug Manufacturers - General | $329,653,000,000 | 3 | Alpha#1 + Alpha#12 |
| 16 | AMAT | Semiconductor Equipment & Materials | $240,166,000,000 | 3 | Alpha#6 + Alpha#12 |
| 17 | KDP | Beverages - Non-Alcoholic | $49,738,000,000 | 3 | Alpha#6 + Alpha#41 |
| 18 | NFLX | Entertainment | $232,952,000,000 | 3 | Alpha#1 + Alpha#6 |
| 19 | UNH | Healthcare Plans | $304,513,000,000 | 3 | Alpha#19 + Alpha#6 |
| 20 | T | Telecom Services | $150,291,000,000 | 3 | Alpha#6 + Alpha#41 |

---

## 4. 逐股详情（Top 20）

### 1. MPWR — Monolithic Power Systems, Inc.（Monolithic Power）
- **股票代码**：MPWR · **板块**：Semiconductors · **市值**：$55,695,000,000 · **收盘**：$1,142.05
- **匹配 Alpha 因子**：Alpha#12（量价背离）、Alpha#19（均值回复）
- **因子信号解读**：
  - Alpha#12：正值 f=10 — 成交量上升 + 价格下跌同步（raw=+153.8），资金流入确认；在下跌行情中显示跟随反转压力。
  - Alpha#19：正值 f=10 — X（std5(|c−o|) + (c−o) + rank(corr(c,o,10))）较低，均值回复压力。
  - Alpha#41：正值 f=10 — √(H·L) 高于典型价，趋势偏强。
- **综合评分**：5/10（因子 6.9 + 基本面 1）
- **投资逻辑**：量价背离（f=10）+ 均值回复压力 + 趋势强三者共振；PE 62.61 高位、分红 0.62%、股价偏高。
- **风险提示**：PE 明显高估（62.6）；趋势见顶风险；价格 $1,142 偏高。

### 2. ASML — ASML Holding N.V.（阿斯麦尔）
- **股票代码**：ASML · **板块**：Semiconductor Equipment & Materials · **市值**：$488,024,000,000 · **收盘**：$1,266.22
- **匹配 Alpha 因子**：Alpha#12（量价背离）、Alpha#41（趋势强度）
- **因子信号解读**：
  - Alpha#12：正值 f=9 — 成交量上升 + 价格下跌同步（raw=+89.98），资金流入确认。
  - Alpha#41：正值 f=9 — √(H·L) 高于典型价，趋势偏上。
- **综合评分**：4/10（因子 5.5 + 基本面 2）
- **投资逻辑**：半导体设备龙头，量价背离（f=9）与趋势强支撑；PE 31.16、分红 0.69%。
- **风险提示**：估值偏高，半导体需求承压风险。

### 3. MU — Micron Technology, Inc.（美信捷诺）
- **股票代码**：MU · **板块**：Semiconductors · **市值**：$672,642,000,000 · **收盘**：$594.51
- **匹配 Alpha 因子**：Alpha#12（量价背离）、Alpha#19（均值回复）
- **因子信号解读**：
  - Alpha#12：正值 f=9 — 成交量上升 + 价格下跌同步（raw=+95.93），资金流入确认。
  - Alpha#19：正值 f=9 — 均值回复压力。
- **综合评分**：4/10（因子 5.2 + 基本面 1.5）
- **投资逻辑**：量价背离（f=9）+ 均值回复压力；PE 9.29 低位，分红 0.09%。
- **风险提示**：内存需求周期性强；今日放量回调体现部分筹码卖出。

### 4. EQIX — Equinix, Inc.（Equinix）
- **股票代码**：EQIX · **板块**：REIT - Specialty · **市值**：$95,842,000,000 · **收盘**：$968.22
- **匹配 Alpha 因子**：Alpha#1（动量）、Alpha#19（均值回复）
- **因子信号解读**：
  - Alpha#1：负值 f=9 — 近期日级自相关低于全体均值（raw=+0.75），动量承压/无动量信号。
  - Alpha#19：正值 f=7 — 均值回复压力。
- **综合评分**：4/10（因子 5 + 基本面 1.5）
- **投资逻辑**：动量承压 + 均值回复压力；REIT 防守属性，PE 58.15 高位，分红 2.03%。
- **风险提示**：高估值（PE 58.15），价格下跌空间。

### 5. AMZN — Amazon.com, Inc.（亚马逊）
- **股票代码**：AMZN · **板块**：Internet Retail · **市值**：$2,669,000,000,000 · **收盘**：$246.82
- **匹配 Alpha 因子**：Alpha#1（动量）、Alpha#53（反转）
- **因子信号解读**：
  - Alpha#1：负值 f=10 — 近期日级自相关低于全体均值（raw=+0.67），动量承压。
  - Alpha#53：负值 f=10 — 比率上升（价格回调），压力回落。
- **综合评分**：4/10（因子 4.4 + 基本面 2）
- **投资逻辑**：动量承压 + 抛压回调；基本面平淡（PE 19.95、无分红），云/流媒体护城河仍在。
- **风险提示**：无现金流增长预期；股价趋势承压。

### 6. GS — The Goldman Sachs Group, Inc.（高盛）
- **股票代码**：GS · **板块**：Capital Markets · **市值**：$228,062,000,000 · **收盘**：$790.69
- **匹配 Alpha 因子**：Alpha#12（量价背离）、Alpha#19（均值回复）
- **因子信号解读**：
  - Alpha#12：正值 f=6 — 成交量上升 + 价跌同步（raw=+56.84），资金流入确认。
  - Alpha#19：正值 f=5 — 均值回复压力。
- **综合评分**：4/10（因子 3.9 + 基本面 3）
- **投资逻辑**：金融股，PE 11.37 低位，分红 2.36%。
- **风险提示**：利率敏感，利润率波动风险。

### 7. AVGO — Broadcom Inc.（博通）
- **股票代码**：AVGO · **板块**：Semiconductors · **市值**：$1,453,000,000,000 · **收盘**：$304.41
- **匹配 Alpha 因子**：Alpha#1（动量）、Alpha#19（均值回复）
- **因子信号解读**：
  - Alpha#1：负值 f=8 — 近期日级自相关偏低，动量承压。
  - Alpha#19：正值 f=6 — 均值回复压力。
- **综合评分**：3/10（因子 3.8 + 基本面 2）
- **投资逻辑**：AI 网络链强劲；动量承压 + 均值回复压力；PE 38.88、分红 0.75%。
- **风险提示**：股价下跌约 -12%，跟随半导体链承压。

### 8. PH — Pantry.com, Inc.（Pantry.com）
- **股票代码**：PH · **板块**：Specialty Industrial Machinery · **市值**：$109,939,000,000 · **收盘**：$871.86
- **匹配 Alpha 因子**：Alpha#41（趋势强度）、Alpha#1（动量）
- **因子信号解读**：
  - Alpha#41：正值 f=6 — √(H·L) 高于典型价，趋势偏上。
  - Alpha#1：负值 f=5 — 动量承压。
- **综合评分**：3/10（因子 3.7 + 基本面 2）
- **投资逻辑**：Specialty 机械，趋势偏强；PE 29.95、分红 0.88%。
- **风险提示**：建筑/机械采购周期性风险。

### 9. NVDA — NVIDIA Corporation（英伟达）
- **股票代码**：NVDA · **板块**：Semiconductors · **市值**：$3,031,000,000,000 · **收盘**：$125.53
- **匹配 Alpha 因子**：Alpha#30（波动率/反转）、Alpha#6（开盘-量相关）
- **因子信号解读**：
  - Alpha#30：正值 f=10 — 无反转压力，算力链结构成立。
  - Alpha#6：负值 f=8 — 开盘价与成交量相关弱负。
- **综合评分**：3/10（因子 3.5 + 基本面 3）
- **投资逻辑**：AI 计算估值跌幅（PE 15.67 低位）+ 算力链弹性修复空间；分红 0.69%。
- **风险提示**：估值见顶；跌幅跟随弹性（见 2026-11-21 投资热点日报，常规收盘 -14%）。

### 10. INTC — Intel Corporation（英特尔）
- **股票代码**：INTC · **板块**：Semiconductors · **市值**：$272,553,000,000 · **收盘**：$51.28
- **匹配 Alpha 因子**：Alpha#30（波动率/反转）、Alpha#1（动量）
- **因子信号解读**：
  - Alpha#30：正值 f=8 — 无反转压力。
  - Alpha#1：正值 f=4 — 近期日级自相关为正，动量成立。
- **综合评分**：3/10（因子 3.4 + 基本面 0.5）
- **投资逻辑**：AI 出海（Beat、Intevo）防守阵地支撑；PE 无数据；防守型。
- **风险提示**：股价承压，AI 叙事分化。

### 11. BLK — BlackRock, Inc.（BlackRock）
- **股票代码**：BLK · **板块**：Asset Management · **市值**：$170,131,000,000 · **收盘**：$1,101.72
- **匹配 Alpha 因子**：Alpha#6（开盘-量相关）、Alpha#19（均值回复）
- **因子信号解读**：
  - Alpha#6：正值 f=5 — 开盘价与成交量相关成立。
  - Alpha#19：正值 f=5 — 均值回复压力。
- **综合评分**：3/10（因子 3.3 + 基本面 3.5）
- **投资逻辑**：Asset Management 防守；PE 25.08、分红 2.02%。
- **风险提示**：管理费收入增长风险。

### 12. CAT — Caterpillar Inc.（卡特彼勒）
- **股票代码**：CAT · **板块**：Farm & Heavy Construction Machinery · **市值**：$233,579,000,000 · **收盘**：$510.45
- **匹配 Alpha 因子**：Alpha#6（开盘-量相关）、Alpha#1（动量）
- **因子信号解读**：
  - Alpha#6：负值 f=7 — 开盘价与成交量相关弱负。
  - Alpha#1：正值 f=5 — 近期日级自相关为正，动量成立。
- **综合评分**：3/10（因子 3.1 + 基本面 3.5）
- **投资逻辑**：重型机械；PE 20.03、分红 1.21%。
- **风险提示**：工程投资周期减缓风险。

### 13. TSM — Taiwan Semiconductor Manufacturing Company Ltd（台积电）
- **股票代码**：TSM · **板块**：Semiconductors · **市值**：$1,653,000,000,000 · **收盘**：$318.71
- **匹配 Alpha 因子**：Alpha#53（反转）、Alpha#6（开盘-量相关）
- **因子信号解读**：
  - Alpha#53：正值 f=7 — 收价在区间比率下降（价格上行，抛压释放）。
  - Alpha#6：负值 f=6 — 开盘价与成交量相关负。
- **综合评分**：3/10（因子 3 + 基本面 3）
- **投资逻辑**：全球代工链；PE 22.81、分红 1.07%。
- **风险提示**：扩产预期降温影响；芯片需求减速风险。

### 14. DUK — Duke Energy Corporation（杜克能源）
- **股票代码**：DUK · **板块**：Utilities - Regulated Electric · **市值**：$101,191,000,000 · **收盘**：$129.78
- **匹配 Alpha 因子**：Alpha#6（开盘-量相关）、Alpha#1（动量）
- **因子信号解读**：
  - Alpha#6：正值 f=7 — 开盘价与成交量相关成立。
  - Alpha#1：正值 f=4 — 近期日级自相关为正，动量成立。
- **综合评分**：3/10（因子 3 + 基本面 3.5）
- **投资逻辑**：Utilities 防守；PE 19.03、分红 3.37%。
- **风险提示**：公用事业收益增长受限。

### 15. MRK — Merck & Co.（默克）
- **股票代码**：MRK · **板块**：Drug Manufacturers - General · **市值**：$329,653,000,000 · **收盘**：$133.72
- **匹配 Alpha 因子**：Alpha#1（动量）、Alpha#12（量价背离）
- **因子信号解读**：
  - Alpha#1：负值 f=8 — 近期日级自相关偏低，动量承压。
  - Alpha#12：负值 f=3 — 无反转压力。
- **综合评分**：3/10（因子 2.9 + 基本面 1.5）
- **投资逻辑**：药企；PE 129.83 高位、分红 2.65%。
- **风险提示**：估值过高，现金流增长空间。

### 16. AMAT — Applied Materials, Inc.（应用材料）
- **股票代码**：AMAT · **板块**：Semiconductor Equipment & Materials · **市值**：$240,166,000,000 · **收盘**：$302.63
- **匹配 Alpha 因子**：Alpha#6（开盘-量相关）、Alpha#12（量价背离）
- **因子信号解读**：
  - Alpha#6：负值 f=5 — 开盘价与成交量相关弱负。
  - Alpha#12：正值 f=4 — 成交量上升 + 价格下跌同步（raw=+36.30）。
- **综合评分**：3/10（因子 2.9 + 基本面 3）
- **投资逻辑**：半导体设备；PE 23.98、分红 0.63%。
- **风险提示**：半导体需求承压风险。

### 17. KDP — Keurig Dr Pepper Inc.（凯贝斯）
- **股票代码**：KDP · **板块**：Beverages - Non-Alcoholic · **市值**：$49,738,000,000 · **收盘**：$34.84
- **匹配 Alpha 因子**：Alpha#6（开盘-量相关）、Alpha#41（趋势强度）
- **因子信号解读**：
  - Alpha#6：正值 f=8 — 开盘价与成交量相关强。
  - Alpha#41：负值 f=4 — √(H·L) 低于典型价，趋势偏弱。
- **综合评分**：3/10（因子 2.9 + 基本面 2.5）
- **投资逻辑**：Beverages 防守；PE 31.11、分红 2.67%。
- **风险提示**：饮料行业逆周期风险。

### 18. NFLX — Netflix, Inc.（奈飞）
- **股票代码**：NFLX · **板块**：Entertainment · **市值**：$232,952,000,000 · **收盘**：$56.73
- **匹配 Alpha 因子**：Alpha#1（动量）、Alpha#6（开盘-量相关）
- **因子信号解读**：
  - Alpha#1：正值 f=4 — 近期日级自相关为正，动量成立。
  - Alpha#6：负值 f=4 — 开盘价与成交量相关弱负。
- **综合评分**：3/10（因子 2.7 + 基本面 2）
- **投资逻辑**：Entertainment；PE 16.88、无分红。
- **风险提示**：流媒体营收增长风险；股价 -2.55%。

### 19. UNH — UnitedHealth Group Incorporated（联合健康）
- **股票代码**：UNH · **板块**：Healthcare Plans · **市值**：$304,513,000,000 · **收盘**：$339.85
- **匹配 Alpha 因子**：Alpha#19（均值回复）、Alpha#6（开盘-量相关）
- **因子信号解读**：
  - Alpha#19：负值 f=7 — 均值回复压力释放（X 较高）。
  - Alpha#6：负值 f=3 — 开盘价与成交量相关弱负。
- **综合评分**：3/10（因子 2.6 + 基本面 3.5）
- **投资逻辑**：Healthcare Plans 防守；PE 18.86、分红 2.81%。
- **风险提示**：医疗叙事分化风险。

### 20. T — AT&T Inc.（美国电话电报）
- **股票代码**：T · **板块**：Telecom Services · **市值**：$150,291,000,000 · **收盘**：$22.31
- **匹配 Alpha 因子**：Alpha#6（开盘-量相关）、Alpha#41（趋势强度）
- **因子信号解读**：
  - Alpha#6：负值 f=4 — 开盘价与成交量相关弱负。
  - Alpha#41：负值 f=4 — √(H·L) 低于典型价，趋势偏弱。
- **综合评分**：3/10（因子 2.6 + 基本面 3）
- **投资逻辑**：Telecom 防守；PE 11.68、分红 5.08% 高收益。
- **风险提示**：股价承压，跟随市场下跌路径。

---

## 5. 板块分类汇总（Top 20）

| 板块 | 成分 | 平均因子评分 | 平均综合评分 |
|------|------|--------------|--------------|
| Semiconductors | MPWR(5), MU(4), AVGO(3), NVDA(3), INTC(3), TSM(3) | 3.8 | 3.5 |
| Semiconductor Equipment & Materials | ASML(4), AMAT(3) | 4.2 | 3.5 |
| REIT - Specialty | EQIX(4) | 5.0 | 4.0 |
| Internet Retail | AMZN(4) | 4.4 | 4.0 |
| Capital Markets | GS(4) | 3.9 | 4.0 |
| Specialty Industrial Machinery | PH(3) | 3.7 | 3.0 |
| Asset Management | BLK(3) | 3.3 | 3.0 |
| Farm & Heavy Construction Machinery | CAT(3) | 3.1 | 3.0 |
| Utilities - Regulated Electric | DUK(3) | 3.0 | 3.0 |
| Drug Manufacturers - General | MRK(3) | 2.9 | 3.0 |
| Beverages - Non-Alcoholic | KDP(3) | 2.9 | 3.0 |
| Entertainment | NFLX(3) | 2.7 | 3.0 |
| Healthcare Plans | UNH(3) | 2.6 | 3.0 |
| Telecom Services | T(3) | 2.6 | 3.0 |

**板块观察**：芯片/半导体方向（MPWR/ASML/MU/AVGO/NVDA/INTC/TSM/AMAT）为 Top 20 占比最大且节点分化明显（MPWR 因子 6.9 为最高）；防守层（DUK/NEE/BLK/UNH/GS）全部综合 3+；软件/AI 软件方向（AMZN/GOOGL/META/ORCL/CRM 等）在本弱势市场因子偏弱，未入 Top 20。

---

## 6. 风险与说明

- 因子为横截面代理值（3 个月日线），非公式回测；Alpha#30/#41 的典型价以 (H+L+C)/3 近似，未复权/未计交易成本。
- 数据基准：US 常规收盘 Nov 20 快照（Yahoo Finance，午后快照）；部分个股价格可能仍有 2-3 分钟延迟。
- 综合评分 = round(0.7 × 因子评分 + 0.3 × 基本面评分)，因子评分与基本面评分均为逐股值；基本面数据为 Yahoo 实时。
- 不构成投资建议；实际操作前请复核最新报价与基本面。
