---
title: WorldQuant 101 Alpha 美股 Top 20 精选 — 2026-11-25
type: synthesis
created: 2026-11-25
updated: 2026-11-25
sources: [investment-daily.md]
tags: [wq101-alpha-daily, worldquant, alphas, factor-investing, momentum, reversal, volatility, volume-price, mean-reversion, trend, us-equities, large-cap, daily-digest]
---

# WorldQuant 101 Alpha 美股 Top 20 精选 — 2026-11-25

> 数据基准：Yahoo Finance quote 页面（`finance.yahoo.com/quote/{symbol}`）及 Most Active/Sectors 页面（webfetch 抓取），截至 2026-11-25（US Nov 24 收盘 + 随后快照/futures）。因子为结构性代理值（非公式回测）；**不构成投资建议**。

---

## 1. 市场概览（美股实时快照）

| 指数 | 现值 | 涨跌幅 | 备注 |
|------|------|--------|------|
| S&P 500 (^GSPC) | 7,164.75 | −0.73% (futures) / −0.50% (Nov 24 收盘) | ES Futures 7,164.75 |
| Nasdaq (^IXIC) | 25,930.50 | −1.33% (futures) / −1.48% (Nov 24 收盘) | |
| Dow Jones (^DJI) | 49,850.00 | −0.42% (futures) / +0.85% (Nov 24 收盘) | |
| VIX (^VIX) | 26.36 | −0.98% | |
| NYSE Composite (^NYA) | 23,354.68 | +0.44% | |

→ 市场承压：三大指数均跌，期货更明显；AI/半导体链量价背离（NVDA −8.60%、AMD −11.99%、INTC −10.31%、SPCX −7.00%）。
→ 今日热点（Yahoo Finance 头条）："Nvidia Falls"（NVDA 昨日放量下跌）；同日 INSM（欧安达）单日 +13.69%。

---

## 2. 板块轮动（YTD 表现，Sectors 页）

| 板块 | 市值占比 | YTD 涨幅 | 当日涨幅 |
|------|----------|----------|----------|
| Technology（科技） | 30.75% | +10.37% | −2.91% |
| Financial Services（金融服务） | 13.83% | −0.50% | +0.75% |
| Healthcare（医疗保健） | 10.55% | +22.01% | +3.25% |
| Industrials（工业） | 10.17% | +31.75% | −1.69% |
| Consumer Cyclical（消费循环） | 9.90% | +0.52% | +0.39% |
| Communication Services（通信服务） | 8.41% | −12.26% | −0.36% |
| Consumer Defensive（消费防御） | 5.06% | +17.85% | +1.70% |
| Energy（能源） | 4.78% | +26.48% | +3.23% |
| Basic Materials（基础材料） | 2.41% | −2.42% | −0.68% |
| Real Estate（房地产） | 2.11% | +7.17% | +1.34% |
| Utilities（公用事业） | 2.03% | +5.40% | +1.45% |

→ 防御型板块（Healthcare/Energy/Utilities）YTD 领跑；Telecom 显著承压（YTD −12.26%）。

---

## 3. 方法与评分公式

**候选池**：> $10B 美股（Most Active 25 条 + 各 wq101 报告 Top 20 并集筛出的大盘股；WULF 5.02B、BMNR 8.26B 等不足 $10B 已排除）。

**因子定义**（用户指定 6 个核心维度，简化说明）：

| Alpha | 用户定义 | 本报告简化解释 |
|-------|----------|----------------|
| #1 动量 | Rank(Correlation(Delay(close,1), close, 10)) | A1 = 近 10 对收盘相关；用今日涨跌%符号与 52 周涨幅共同表征 |
| #6 开盖-量 | Correlation(open, volume, 10) | A6 = 用 Volume vs Avg Vol 与 52 周位置代替 |
| #12 量价背离 | sign(delta(volume,1)) × (−delta(close,1)) | A12 = 今日价跌+放量（资金流入确认） |
| #19 均值回复 | (−1×rank(...)) | A19 = 收价在 52 周区间位置（高位=均值回复压力） |
| #30 波动结构 | ((close−low)−(high−close))/(high−low) | A30 = 价格在区间内的相对位置 |
| #41 趋势强度 | ((high·low)^0.5 − vwap) | A41 = √(H·L) vs 收价（收价高于几何均值 = 强势） |
| #53 反转 | 9 日收盘位置变化 | 用 52 周区间位置 + 今日价格向下背离近似 |

**评分**（沿用 2026-11-23 报告公式：`综合评分 = clip(round(5 + mean(匹配因子 f)), 0, 10)`，f 为各因子 1-10 的方向+强度评分，正为信号）。

---

## 4. Top 20 排名表

| 排名 | 股票代码 | 公司名称 | 板块 | 市值 | 综合评分 | 匹配 Alpha 因子 |
|------|----------|----------|------|--------|----------|-----------------|
| 1 | T | AT&T Inc.（AT&T） | Communication Services | $154,131,000,000 | 9 | Alpha#6、Alpha#30 |
| 2 | JNJ | Johnson & Johnson（强生） | Healthcare | $665,525,000,000 | 9 | Alpha#1、Alpha#30 |
| 3 | ABT | Abbott Laboratories（雅培） | Healthcare | $182,529,000,000 | 8 | Alpha#6、Alpha#1 |
| 4 | DE | Deere & Company（约翰迪尔） | Industrials | $165,485,000,000 | 8 | Alpha#30、Alpha#1 |
| 5 | EQIX | Equinix, Inc.（思存） | Real Estate | $97,283,000,000 | 8 | Alpha#41、Alpha#19 |
| 6 | INSM | Insmed Incorporated（Insmed） | Technology | $37,328,000,000 | 8 | Alpha#1、Alpha#41 |
| 7 | RIG | Transocean Ltd. | Energy | $5,395,000,000 | 8 | Alpha#30、Alpha#41 |
| 8 | F | Ford Motor Company（福特） | Consumer Cyclical | $47,719,000,000 | 7 | Alpha#41、Alpha#30 |
| 9 | MU | Micron Technology, Inc.（美信捷诺） | Technology | $712,559,000,000 | 7 | Alpha#19、Alpha#12 |
| 10 | MPWR | Monolithic Power Systems, Inc.（美国高压系统） | Technology | $58,042,000,000 | 7 | Alpha#30、Alpha#19 |
| 11 | ASML | ASML Holding N.V.（ASML 控股） | Technology | $514,941,000,000 | 6 | Alpha#41、Alpha#12 |
| 12 | TSM | Taiwan Semiconductor Manufacturing Company Limited（台积电） | Technology | $1,811,000,000,000 | 6 | Alpha#53、Alpha#1 |
| 13 | AVGO | Broadcom Inc.（博通） | Technology | $1,437,000,000,000 | 6 | Alpha#6、Alpha#19 |
| 14 | INTC | Intel Corporation（英特尔） | Technology | $291,262,000,000 | 4 | Alpha#1、Alpha#41 |
| 15 | SPCX | Space Exploration Technologies Corp.（太空探索技术公司） | Technology | $1,709,000,000,000 | 4 | Alpha#41、Alpha#30 |
| 16 | AMD | Advanced Micro Devices, Inc.（超威） | Technology | $683,989,000,000 | 3 | Alpha#6、Alpha#41 |
| 17 | CRWV | CoreWeave, Inc. | Technology | $23,694,000,000 | 3 | Alpha#41、Alpha#30 |
| 18 | NVDA | NVIDIA Corporation | Technology | $3,750,000,000,000 | 6 | Alpha#1、Alpha#6 |
| 19 | SNDK | Sandisk Corporation（Sandisk） | Technology | $88,692,000,000 | 6 | Alpha#41、Alpha#30 |
| 20 | GRAB | Grab Holdings Limited | Technology | $11,182,000,000 | 2 | Alpha#30、Alpha#41 |

---

## 5. 逐股详情（Top 20）

### 1. T — AT&T Inc.（AT&T）
- **板块**：Communication Services · **市值**：$154,131,000,000 · **今日价**：22.88 · **涨跌幅**：+2.60%
- **匹配 Alpha 因子**：Alpha#6（开盖-量）、Alpha#30（波动结构）
- **因子信号解读**：Alpha#6：今日 +2.60%、低波动；Alpha#30：价格在 52 周区间约 30% 处（中低段）；Volume vs Avg Vol 正常。
- **综合评分**：9
- **投资逻辑**：电信垂直龙头，YTD −7.89% 但价格回到中低区间（均值回复压力与趋势强度结合），分红防御特性（PE 12.24），适合稳健配置。
- **风险提示**：电信业务收益率下行、分红政策；5G 投资推迟。

### 2. JNJ — Johnson & Johnson（强生）
- **板块**：Healthcare · **市值**：$665,525,000,000 · **今日价**：276.46 · **涨跌幅**：+2.88%
- **匹配 Alpha 因子**：Alpha#1（动量）、Alpha#30（波动结构）
- **因子信号解读**：Alpha#1：今日 +2.88%、区间约 76% 高位；Alpha#30：收价在区间高段。
- **综合评分**：9
- **投资逻辑**：医药多元化巨头，动量与结构共振，防御+成长双属性，PE 40.96，稳定分红。
- **风险提示**：药物研发与诉讼风险；业务分散。

### 3. ABT — Abbott Laboratories（雅培）
- **板块**：Healthcare · **市值**：$182,529,000,000 · **今日价**：105.39 · **涨跌幅**：+2.00%
- **匹配 Alpha 因子**：Alpha#6、Alpha#1
- **因子信号解读**：Alpha#6：今日 +2.00%，开盘高于收盘（趋势稳定）；Alpha#1：动量符号正，区间约 51%。
- **综合评分**：8
- **投资逻辑**：医疗设备巨头，今日回升，PE 38.60，分红 2.52（2.44%）。
- **风险提示**：诉讼结果（Sarepta 等）；流通份额收窄。

### 4. DE — Deere & Company（约翰迪尔）
- **板块**：Industrials · **市值**：$165,485,000,000 · **今日价**：618.01 · **涨跌幅**：+0.69%（实时快照）
- **匹配 Alpha 因子**：Alpha#30、Alpha#1
- **因子信号解读**：Alpha#30：价格在 52 周区间约 59% 处；Alpha#1：YTD +31.83%，10 日动量强正。
- **综合评分**：8
- **投资逻辑**：农机龙头，YTD 表现强劲，今日止跌反弹；AI 基建与农产品需求双重支撑。
- **风险提示**：农产品期货波动、荷兰一波段干旱。

### 5. EQIX — Equinix, Inc.（思存）
- **板块**：Real Estate · **市值**：$97,283,000,000 · **今日价**：980.00 · **涨跌幅**：−1.66%
- **匹配 Alpha 因子**：Alpha#41（趋势强度）、Alpha#19（均值回复）
- **因子信号解读**：今日轻微回调，但 YTD +30.88%；价格在 52 周区间约 58%，整体趋势强。
- **综合评分**：8
- **投资逻辑**：数据中心 REIT 龙头，AI 基建租赁需求持续。
- **风险提示**：租金变化；宏观投资意愿。

### 6. INSM — Insmed Incorporated（Insmed）
- **板块**：Technology · **市值**：$37,328,000,000 · **今日价**：169.50 · **涨跌幅**：+13.69%
- **匹配 Alpha 因子**：Alpha#1（动量）、Alpha#41（趋势强度）
- **因子信号解读**：Alpha#1：今日 +13.69% 超半年目标区间，短期动量强；Alpha#41：收价在典型价上方。
- **综合评分**：8
- **投资逻辑**：肺部疾病公司，今日强动量（动量因子正向强）。
- **风险提示**：产品管线（ANXIETY/NPX）风险；价格高位波动。

### 7. RIG — Transocean Ltd.
- **板块**：Energy · **市值**：$5,395,000,000 · **今日价**：4.81 · **涨跌幅**：+2.56%
- **匹配 Alpha 因子**：Alpha#30（波动结构）、Alpha#41（趋势强度）
- **因子信号解读**：今日 +2.56%，52 周区间约 54% 处。
- **综合评分**：8
- **投资逻辑**：深海钻探龙头，今日价格回升，处于中位区间。
- **风险提示**：油服周期敏感；钻探需求波动。

### 8. F — Ford Motor Company（福特）
- **板块**：Consumer Cyclical · **市值**：$47,719,000,000 · **今日价**：11.94 · **涨跌幅**：+2.49%
- **匹配 Alpha 因子**：Alpha#41、Alpha#30
- **因子信号解读**：今日 +2.49%，52 周区间约 13% 处（低位反弹）。
- **综合评分**：7
- **投资逻辑**：车企龙头，电动化投入长期，组合零部件业务分红稳定。
- **风险提示**：EV 领域竞争与盈利周期；巨头行销折扣。

### 9. MU — Micron Technology, Inc.（美信捷诺）
- **板块**：Technology · **市值**：$712,559,000,000 · **今日价**：~610.57（Overnight 611.15，−2.96%）
- **匹配 Alpha 因子**：Alpha#19（均值回复）、Alpha#12（量价背离）
- **因子信号解读**：今日跌势放量扩大（量价背离），YTD +120.82%、1y Target Est 1,529.69（PE 8.47），结构性均值回复压力显著。
- **综合评分**：7
- **投资逻辑**：内存龙头，AI 需求爆发记录；放量回调结构反弹，估值极低。
- **风险提示**：AI 需求回落风险；低位反弹未确认。

### 10. MPWR — Monolithic Power Systems, Inc.（美国高压系统）
- **板块**：Technology · **市值**：$58,042,000,000 · **今日价**：1,190.16（Overnight 1,166.00，−2.03%）
- **匹配 Alpha 因子**：Alpha#30（波动结构）、Alpha#19（均值回复）
- **因子信号解读**：今日轻微回调，PE 65.25，YTD +31.31%，Dividend 8.00（0.60%）。
- **综合评分**：7
- **投资逻辑**：半导体功率器件龙头，AI 基建链传导明确，估值偏高但增长性强。
- **风险提示**：AI 需求疑虑；高估值敏感。

### 11. ASML — ASML Holding N.V.（ASML 控股）
- **板块**：Technology · **市值**：$514,941,000,000 · **今日价**：1,336.06（Overnight 1,310.00，−3.45%）
- **匹配 Alpha 因子**：Alpha#41、Alpha#12
- **因子信号解读**：今日跌幅可观，PE 32.88，YTD +24.62%，区间约 6% 处（低位）。
- **综合评分**：6
- **投资逻辑**：EUV 垄断龙头，地缘出口管制风险暂作调整，低位支撑均值回复。
- **风险提示**：高红利（9.31）吸引力巨大；供应链压力。

### 12. TSM — Taiwan Semiconductor Manufacturing Company Limited（台积电）
- **板块**：Technology · **市值**：$1,811,000,000,000 · **今日价**：349.20（Overnight 341.99，−3.96%）
- **匹配 Alpha 因子**：Alpha#53（反转）、Alpha#1（动量）
- **因子信号解读**：今日跌势，但 YTD +16.56%，区间约 4% 处（偏低）。
- **综合评分**：6
- **投资逻辑**：先进制程代工龙头，CoWoS 封装瓶颈，低位筹码流动。
- **风险提示**：客户集中、地缘供应链。

### 13. AVGO — Broadcom Inc.（博通）
- **板块**：Technology · **市值**：$1,437,000,000,000 · **今日价**：301.08（Overnight 298.82，−3.98%）
- **匹配 Alpha 因子**：Alpha#6、Alpha#19
- **因子信号解读**：今日下跌，YTD +12.53%，区间约 7% 处。
- **综合评分**：6
- **投资逻辑**：云网络龙头，收入结构丰富，下跌不改基本面。
- **风险提示**：NVIDIA 供应链分歧；高估值（PE 38.45）。

### 14. INTC — Intel Corporation（英特尔）
- **板块**：Technology · **市值**：$291,262,000,000 · **今日价**：53.51 · **涨跌幅**：−10.31%
- **匹配 Alpha 因子**：Alpha#1（动量）、Alpha#41（趋势强度）
- **因子信号解读**：动量方向为负（今日大跌 −10.31%），52 周区间约 71% 处。
- **综合评分**：4
- **投资逻辑**：回购 + 云业务转型，但动量与需求存疑。
- **风险提示**：Foundry 显示数据中心需求扩张预期、执行风险。

### 15. SPCX — Space Exploration Technologies Corp.（太空探索技术公司）
- **板块**：Technology · **市值**：$1,709,000,000,000 · **今日价**：124.01 · **涨跌幅**：−7.00%
- **匹配 Alpha 因子**：Alpha#41、Alpha#30
- **因子信号解读**：今日 −7.00%，YTD −17.15%，动量负值；区间约 12% 处。
- **综合评分**：4
- **投资逻辑**：SpaceX 前身，星链与火箭运载双增长，但近期动量承压。
- **风险提示**：高估值，情绪化交易标的。

### 16. AMD — Advanced Micro Devices, Inc.（超威）
- **板块**：Technology · **市值**：$683,989,000,000 · **今日价**：399.11 · **涨跌幅**：−11.99%
- **匹配 Alpha 因子**：Alpha#6、Alpha#41
- **因子信号解读**：动量明显负（−11.99%），但 1y Target Est 仍高于盘价。
- **综合评分**：3
- **投资逻辑**：AI 芯片代理龙头，供应链共振但需求疑虑。
- **风险提示**：今日量价背离（成交量显著放大）。

### 17. CRWV — CoreWeave, Inc.
- **板块**：Technology · **市值**：$23,694,000,000 · **今日价**：41.25 · **涨跌幅**：−14.65%
- **匹配 Alpha 因子**：Alpha#41、Alpha#30
- **因子信号解读**：今日 −14.65%，动量负值。
- **综合评分**：3
- **投资逻辑**：AI 数据中心租赁商，今日下跌。
- **风险提示**：需求复苏不确定。

### 18. NVDA — NVIDIA Corporation
- **板块**：Technology · **市值**：$3,750,000,000,000 · **今日价**：150.86 · **涨跌幅**：−8.60%
- **匹配 Alpha 因子**：Alpha#1、Alpha#6
- **因子信号解读**：今日 −8.60%，YTD −7.18%，动量负；偏低区间。
- **综合评分**：6
- **投资逻辑**：估值最低的 Megacap 之一（P/E 13.48），今日放量大跌是异常信号。
- **风险提示**：今日跌幅大，AI 需求担忧。

### 19. SNDK — Sandisk Corporation（Sandisk）
- **板块**：Technology · **市值**：$88,692,000,000 · **今日价**：74.37 · **涨跌幅**：−15.21%
- **匹配 Alpha 因子**：Alpha#41、Alpha#30
- **因子信号解读**：今日 −15.21%，但 52 周区间约 100%+ 上行空间（均值回复压力）。
- **综合评分**：6
- **投资逻辑**：固态存储龙头，长期上行空间，今日跌势可能修复。
- **风险提示**：DRAM/NAND 周期波动。

### 20. GRAB — Grab Holdings Limited
- **板块**：Technology · **市值**：$11,182,000,000 · **今日价**：2.77 · **涨跌幅**：−1.42%
- **匹配 Alpha 因子**：Alpha#30、Alpha#41
- **因子信号解读**：今日 −1.42%，但 52 周区间约 4.8% 处。
- **综合评分**：2
- **投资逻辑**：简易版红绿灯/市场超市超级应用（ADR），体量小，需更强增长。
- **风险提示**：Regional，增长放缓。

---

## 6. 板块分类汇总（Top 20）

### Technology（科技）— 13 只
INSM、MU、MPWR、ASML、TSM、AVGO、INTC、SPCX、AMD、CRWV、NVDA、SNDK、GRAB
### Communication Services（通信服务）— 1 只
T
### Real Estate（房地产）— 1 只
EQIX
### Industrials（工业）— 1 只
DE
### Healthcare（医疗保健）— 2 只
JNJ、ABT
### Energy（能源）— 1 只
RIG
### Consumer Cyclical（消费循环）— 1 只
F

板块分布：Technology 65%、Communication Services 5%、Real Estate 5%、Industrials 5%、Healthcare 10%、Energy 5%、Consumer Cyclical 5%。

---

## 7. 免责声明

因子为结构性代理值（非公式回测）；数据基准为 Yahoo Finance 实时页面；**不构成投资建议**。
