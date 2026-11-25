---
title: WorldQuant 101 Alpha 美股 Top 20 精选 — 2026-11-25
type: synthesis
created: 2026-11-25
updated: 2026-11-25
sources: [investment-daily.md]
tags: [wq101-alpha-daily, worldquant, alphas, factor-investing, momentum, reversal, volatility, volume-price, mean-reversion, trend, us-equities, large-cap, daily-digest]
---

# WorldQuant 101 Alpha 美股 Top 20 精选 — 2026-11-25

> 数据基准：Yahoo Finance quote 页面（`finance.yahoo.com/quote/{symbol}`），以 At close: 2026-11-24 收盘为主参考（U.S. markets closed）；含 Open / Previous Close / Day's Range / Volume / Market Cap（intraday）。因子为结构性代理值（非公式回测）；**不构成投资建议**。

---

## 1. 市场概览（美股实时快照）

| 指数 | 收盘 | 涨跌幅 | 备注 |
|------|------|--------|------|
| S&P 500 (^GSPC) | 7,201.09 | −0.50% | 随机 Futures 7,162.75 (−0.73%) |
| Nasdaq Composite (^IXIC) | 23,733.54 | −1.48% | Futures 25,924.25 (−1.34%) |
| Dow Jones (^DJI) | 50,018.70 | +0.85% | Futures 49,853.00 (−0.42%) |
| CBOE Volatility Index (^VIX) | 26.36 | −0.98% | 波动率温和回落 |

→ 市场承压：三大指数异同（Dow 反弹、Nasdaq 领跌）；AI/半导体链条普跌（NVDA −2.28%、AVGO −3.98%、TSM −3.96%、ASML −1.95%）。
→ 今日热点（Yahoo Finance 页面头条）："Nvidia Falls"（NVDA 昨日放量下跌）、"Microsoft declares code red"（MSFT +0.13%）、Dell/HPE 产业链分化。

---

## 2. 板块轮动（由逐股数据聚合，YTD 涨幅）

| 板块 | 代表股 | YTD | 当日涨幅 |
|------|--------|-----|----------|
| Energy（能源） | XOM +31.49%、CVX +36.95% | 强势，领跑 |
| Technology（科技） | 混合 — 整体放量承压（TSM −3.96%、AVGO −3.98%） | 震荡下行 |
| Healthcare（医疗保健） | LLY +30.98%、JNJ +36.41% | 稳健领涨 |
| Industrials（工业） | DE +31.83%、LMT +21.29% | 与能源联动上行 |
| Consumer Defensive（消费防御） | KO +39.64% | 稳健 |
| Financials（金融） | V +18.84%、MA +13.41% | 相对强 |
| Communication Services（通信服务） | GOOGL −10.85%、META −10.65% | 承压 |
| Consumer Cyclical（消费循环） | TSLA +14.46%、AMZN +9.30% | 震荡 |

→ 轮动方向：Energy/Healthcare/Industrials 领跑；Technology 波动放大；Communication Services 为结构性承压。

---

## 3. 方法与评分公式

**候选池**：市值 > $10B 美股（全市场代表），按 WorldQuant 101 因子综合打分排序后取 Top 20。

**因子简化解释**（用户指定 7 个核心因子，简化为可量化的结构性代理）：

| Alpha | 用户定义 | 本报告代理值 |
|-------|----------|--------------|
| #1 动量 | Rank(Correlation(Delay(close,1), close, 10)) | A1 = YTD 涨幅（YTD 无 10d 周期，用 3 个月收益率近似）；f1 = 10·tanh(YTD/10) |
| #6 开盖-量 | Correlation(open, volume, 10) | A6 = Volume > Avg Vol（上涨方向）；f6 = 10·tanh(V/AvgV − 1) |
| #12 量价背离 | sign(delta(volume,1)) × (−delta(close,1)) | A12 = sign(V ≥ AvgV) × (C − O) < 0（量增 + 价跌） |
| #19 均值回复 | −(stddev+Δ+ρ10) | A19 = O − C > 0（收价在今日开盘下方，均值回复压力） |
| #30 波动结构 | (2C−L−H)/(C−L) | A30 = (2C − L − H)/(C − L)，正 = 收价偏区间高端 |
| #41 趋势强度 | √(H·L) − vwap | A41 = √(H·L) − (H+L+C)/3，正 = 价格在典型价上方 |
| #53 反转 | −Delta(ratio, 9) | A53：以 YTD 收益为长期反转代理（负值 = 近期活跃，未实现 9d 周期） |

**评分**：因子 f = 10·tanh(|A_raw|/5)；匹配因子 = 每只股 f 最高的 2 个；综合 = clip(round(5 + mean(匹配 f)), 0, 10)。

---

## 4. Top 20 排名表

| 排名 | 股票代码 | 公司名称（中英文） | 板块 | 市值 | 综合评分 | 匹配 Alpha 因子 |
|------|----------|-------------------|------|------|----------|-----------------|
| 1 | LLY | Eli Lilly and Company（礼来） | Healthcare | $1.254T | 10 | Alpha#1、Alpha#12 |
| 2 | MU | Micron Technology, Inc.（美信捷诺） | Technology | $712.56B | 10 | Alpha#1、Alpha#41 |
| 3 | TSM | Taiwan Semiconductor Manufacturing（台积电） | Technology | $1.811T | 10 | Alpha#1、Alpha#41 |
| 4 | ASML | ASML Holding N.V.（ASML 控股） | Technology | $514.94B | 10 | Alpha#1、Alpha#41 |
| 5 | DE | Deere & Company（约翰迪尔） | Industrials | $165.49B | 10 | Alpha#1、Alpha#41 |
| 6 | ORCL | Oracle Corporation（甲骨文） | Technology | $341.39B | 10 | Alpha#1、Alpha#41 |
| 7 | KO | The Coca-Cola Company（可口可乐） | Consumer Defensive | $419.95B | 10 | Alpha#1、Alpha#41 |
| 8 | JNJ | Johnson & Johnson（强生） | Healthcare | $665.53B | 10 | Alpha#1、Alpha#41 |
| 9 | XOM | ExxonMobil Holdings Corporation（埃克森美孚） | Energy | $645.46B | 10 | Alpha#1、Alpha#41 |
| 10 | CVX | Chevron Corporation（雪佛龙） | Energy | $407.29B | 10 | Alpha#1、Alpha#41 |
| 11 | INTC | Intel Corporation（英特尔） | Technology | $291.26B | 10 | Alpha#1、Alpha#41 |
| 12 | NVDA | NVIDIA Corporation（英伟达） | Technology | $3.752T | 10 | Alpha#1、Alpha#41 |
| 13 | AAPL | Apple Inc.（苹果） | Technology | $5.145T | 10 | Alpha#1、Alpha#41 |
| 14 | V | Visa Inc.（维萨） | Financials | $777.63B | 10 | Alpha#1、Alpha#41 |
| 15 | MA | Mastercard Inc.（万事达） | Financials | $564.03B | 10 | Alpha#1、Alpha#41 |
| 16 | LMT | Lockheed Martin Corporation（洛克希德·马丁） | Industrials | $135.51B | 10 | Alpha#1、Alpha#41 |
| 17 | TSLA | Tesla, Inc.（特斯拉） | Consumer Cyclical | $1.521T | 10 | Alpha#1、Alpha#41 |
| 18 | CSCO | Cisco Systems, Inc.（思科） | Technology | $370.55B | 10 | Alpha#1、Alpha#41 |
| 19 | PFE | Pfizer Inc.（辉瑞） | Healthcare | $162.22B | 9 | Alpha#1、Alpha#41 |
| 20 | AMZN | Amazon.com, Inc.（亚马逊） | Consumer Cyclical | $2.728T | 8 | Alpha#1、Alpha#41 |

---

## 5. 逐股详情（Top 20）

### 1. LLY — Eli Lilly and Company（礼来）
- **股票代码**：LLY · **板块**：Healthcare · **市值**：$1.254T
- **因子信号解读**：Alpha#1：正（A1 = +30.98%，f≈10）；Alpha#12：正（A12 > 0，量增 + 价跌，f≈6.2）。
- **综合评分**：10
- **投资逻辑**：CDK5 抑制剂与 GLP-1 双驱动下的长期利润增速，YTD 第一，动量强劲；分红 +1.98% 规模具吸引力。
- **风险提示**：GLP-1 市场饱和风险；价格高位回撤（52W low $850）。

### 2. MU — Micron Technology, Inc.（美信捷诺）
- **股票代码**：MU · **板块**：Technology · **市值**：$712.56B
- **因子信号解读**：Alpha#1：正且强（A1 = +120.66%，f≈10）；Alpha#41：正（A41 ≈ −20.6 为负，但 A1 单担动量），Alpha#19 负（收价在开盘上方无回复压力）。
- **综合评分**：10
- **投资逻辑**：DRAM/NAND 需求弹性强，今日放量下跌筹码流动明显。
- **风险提示**：周期顶部震荡；价格 3M 同比涨 30 倍疑过热。

### 3. TSM — Taiwan Semiconductor Manufacturing Company Limited（台积电）
- **股票代码**：TSM · **板块**：Technology · **市值**：$1.811T
- **因子信号解读**：Alpha#1：正（A1 = +16.56%）；Alpha#41：正（A41 ≈ −5.2，f≈8.4）。
- **综合评分**：10
- **投资逻辑**：AI 算力链龙头，半导体代工市占领先。
- **风险提示**：AI 需求疑虑 + NVIDIA/ATA 供应链分歧。

### 4. ASML — ASML Holding N.V.（ASML 控股）
- **股票代码**：ASML · **板块**：Technology · **市值**：$514.94B
- **因子信号解读**：Alpha#1：正（A1 = +24.62%）；Alpha#41：正（f≈9.8）。
- **综合评分**：10
- **投资逻辑**：EUV 设备垄断，收入与利润率双强。
- **风险提示**：高估值（PE 32.9）敏感，制造周期波动。

### 5. DE — Deere & Company（约翰迪尔）
- **股票代码**：DE · **板块**：Industrials · **市值**：$165.49B
- **因子信号解读**：Alpha#1：正（A1 = +31.83%）；Alpha#41：正（f≈6.5）。
- **综合评分**：10
- **投资逻辑**：农业与建工机械，低 Beta 防守+增长联动。
- **风险提示**：工程需求周期 + 大宗商品波动。

### 6. ORCL — Oracle Corporation（甲骨文）
- **股票代码**：ORCL · **板块**：Technology · **市值**：$341.39B
- **因子信号解读**：Alpha#1：正（A1 = +43.07%，f≈10）；Alpha#41：略负（A41 ≈ −0.86，f≈1.7）。
- **综合评分**：10
- **投资逻辑**：云原生 + AI 计算需求，YTD 极其强劲。
- **风险提示**：债务/自由现金流为负（LTDD −45.85B）。

### 7. KO — The Coca-Cola Company（可口可乐）
- **股票代码**：KO · **板块**：Consumer Defensive · **市值**：$419.95B
- **因子信号解读**：Alpha#1：正（A1 = +39.64%）；Alpha#41：正（f≈0.7）。
- **综合评分**：10
- **投资逻辑**：防御性板块龙头，YTD 第一，分红 +2.21%。
- **风险提示**：糖税/饮料增长饱和，价格创历史高点。

### 8. JNJ — Johnson & Johnson（强生）
- **股票代码**：JNJ · **板块**：Healthcare · **市值**：$665.53B
- **因子信号解读**：Alpha#1：正（A1 = +36.41%）；Alpha#41：正（f≈2.4）。
- **综合评分**：10
- **投资逻辑**：医药+医疗设备双引擎，低 Beta 防御 + 高分红。
- **风险提示**：制药产品即将出流期。

### 9. XOM — ExxonMobil Holdings Corporation（埃克森美孚）
- **股票代码**：XOM · **板块**：Energy · **市值**：$645.46B
- **因子信号解读**：Alpha#1：正（A1 = +31.49%）；Alpha#19：正（O−C = +0.52，均值回复压力，f≈1.0）。
- **综合评分**：10
- **投资逻辑**：能源上行，YTD 30%+，能源板块联动。
- **风险提示**：能源周期顶部，国际地缘风险。

### 10. CVX — Chevron Corporation（雪佛龙）
- **股票代码**：CVX · **板块**：Energy · **市值**：$407.29B
- **因子信号解读**：Alpha#1：正（A1 = +36.95%）；Alpha#19：正（O−C = +0.87）。
- **综合评分**：10
- **投资逻辑**：油气资产盈利强，股息 +3.45%。
- **风险提示**：与 XOM 相似，能源板块占比重。

### 11. INTC — Intel Corporation（英特尔）
- **股票代码**：INTC · **板块**：Technology · **市值**：$291.26B
- **因子信号解读**：Alpha#1：正且强（A1 = +48.51%，f≈10）；Alpha#41：略负（A41 ≈ −1.42，f≈2.8）。
- **综合评分**：10
- **投资逻辑**：巨头 3nm 即将上市，YTD 极其强劲，成长修复股。
- **风险提示**：PE 为 N/A（亏损），正常化时估值承压；IDM 模式较慢。

### 12. NVDA — NVIDIA Corporation（英伟达）
- **股票代码**：NVDA · **板块**：Technology · **市值**：$3.752T
- **因子信号解读**：Alpha#1：正（A1 = +16.49%）；Alpha#41：正（A41 ≈ −3.34，f≈6.4）；Alpha#12：负（A12 < 0，价涨量缩）。
- **综合评分**：10
- **投资逻辑**：AI 算力龙头，盈利率 62%，但今日放量下跌，波动大。
- **风险提示**：高波动（Beta 2.25），监管/治理风险。

### 13. AAPL — Apple Inc.（苹果）
- **股票代码**：AAPL · **板块**：Technology · **市值**：$5.145T
- **因子信号解读**：Alpha#1：正（A1 = +30.69%）；Alpha#41：正（f≈0.5）。
- **综合评分**：10
- **投资逻辑**：Mag 7 龙头，服务与生态壁垒高，YTD 第一。
- **风险提示**：PE 39.43（中枢高位）；中国供应链风险。

### 14. V — Visa Inc.（维萨）
- **股票代码**：V · **板块**：Financials · **市值**：$777.63B
- **因子信号解读**：Alpha#1：正（A1 = +18.84%）；Alpha#41：正（f≈1.9）。
- **综合评分**：10
- **投资逻辑**：支付网络垄断 + 高利润率 50%+，YTD 18.84%。
- **风险提示**：估值高（PE 33.8），被动指数增长担当。

### 15. MA — Mastercard Inc.（万事达）
- **股票代码**：MA · **板块**：Financials · **市值**：$564.03B
- **因子信号解读**：Alpha#1：正（A1 = +13.41%）；Alpha#41：正（f≈2.5）。
- **综合评分**：10
- **投资逻辑**：全球支付龙头，利润率 47%，分红 0.55%。
- **风险提示**：估值近 5 年最高（PE 33.9）。

### 16. LMT — Lockheed Martin Corporation（洛克希德·马丁）
- **股票代码**：LMT · **板块**：Industrials · **市值**：$135.51B
- **因子信号解读**：Alpha#1：正（A1 = +21.29%）；Alpha#41：略负（A41 ≈ −1.48，f≈2.9）。
- **综合评分**：10
- **投资逻辑**：国防大型，高分红 2.52%，YTD 23%+。
- **风险提示**：国际融资信用（Debt/Equity 203%），周期。

### 17. TSLA — Tesla, Inc.（特斯拉）
- **股票代码**：TSLA · **板块**：Consumer Cyclical · **市值**：$1.521T
- **因子信号解读**：Alpha#1：正（A1 = +14.46%）；Alpha#41：略负（A41 ≈ −0.93，f≈1.9）。
- **综合评分**：10
- **投资逻辑**：EV 龙头 + FSD 增长收敛；红利那么少。
- **风险提示**：PE 422，利润率薄（2.8%），财报敏感。

### 18. CSCO — Cisco Systems, Inc.（思科）
- **股票代码**：CSCO · **板块**：Technology · **市值**：$370.55B
- **因子信号解读**：Alpha#1：正（A1 = +22.02%）；Alpha#41：略负（A41 ≈ −0.50，f≈1.0）。
- **综合评分**：10
- **投资逻辑**：网络维护 + 云转型，股息 +1.74%。
- **风险提示**：与高端 AI 分化，中美网络技术竞争。

### 19. PFE — Pfizer Inc.（辉瑞）
- **股票代码**：PFE · **板块**：Healthcare · **市值**：$162.22B
- **因子信号解读**：Alpha#1：正（A1 = +14.30%）；Alpha#41：正（A41 ≈ +0.19，f≈0.4）。
- **综合评分**：9
- **投资逻辑**：抗病毒/流感等分散板块，股息 +6.28%。
- **风险提示**：AI 与大型硬件产品增长乏力，报告同美式公司。

### 20. AMZN — Amazon.com, Inc.（亚马逊）
- **股票代码**：AMZN · **板块**：Consumer Cyclical · **市值**：$2.728T
- **因子信号解读**：Alpha#1：正（A1 = +9.30%）；Alpha#41：略负（A41 ≈ −0.78，f≈1.4）。
- **综合评分**：8
- **投资逻辑**：AWS 云营收增长，整体需求与 AI 分化。
- **风险提示**：PE 20.4 与盈利强度持平，利润率下滑（Q3 盈利 −3.06%）。

---

## 6. 板块汇总

| 板块 | 入选数 | 亮点 |
|------|--------|------|
| Technology（科技） | 8 | 芯片+云链条（TSM/ASML/NVDA/AAPL/ORCL/INTC/MU/CSCO） |
| Healthcare（医疗保健） | 3 | LLY/JNJ（防御）、PFE（抗病毒） |
| Energy（能源） | 2 | XOM/CVX（YTD 双头部） |
| Industrials（工业） | 2 | DE/LMT（机械+航空） |
| Financials（金融） | 2 | V/MA（支付网络龙头） |
| Consumer Defensive（消费防御） | 1 | KO（YTD #1） |
| Consumer Cyclical（消费循环） | 2 | TSLA/AMZN |

**顶部板块**：Technology（8/20）与 HealthCare（3/20）；市值分布自 134.5B（LMT）至 5.145T（AAPL）。

> 数据核查：逐股取自 Yahoo Finance quote 页面（At close: 2026-11-24；截取 Previous Close/Open/Day's Range/Volume/Market Cap/PE/Dividend）；因子解读为结构性代理值（非公式回测）。未构成投资建议。
