---
title: WorldQuant 101 Alpha 美股 Top 20 精选 — 2026-11-26
type: synthesis
created: 2026-11-26
updated: 2026-11-26
sources: []
tags: [wq101-alpha-daily, worldquant, alphas, factor-investing, momentum, reversal, volatility, volume-price, mean-reversion, trend, us-equities, large-cap, daily-digest]
---

# WorldQuant 101 Alpha 美股 Top 20 精选 — 2026-11-26

> **数据基准 / As-of：** 美股最近一个完整交易日 **2026-11-25** 收盘（本报告日 2026-11-26 为美国 **感恩节（Thanksgiving）休市日**，Yahoo Finance 显示 “U.S. markets closed”；11-25 已收盘，26 日不交易，27 日为半日交易）。行情/因子数据抓取于 2026-11-26。**本报告为基于 WorldQuant 101 因子逻辑的横截面量化筛选代理，非公式化回测、非实时报价，不构成任何投资建议。**

> **偏好文件 / Preference:** 已启用仓库根目录 `EXTEND.md`（llm-wiki-bootstrap 偏好；本任务为合成页输出，不涉及 BM25）。

---

## 0. 执行摘要（TL;DR）

- **方法**：取 **美股普通股、市值 ≥ $10B** 的大中盘池（Nasdaq screener，~300 只 → 过滤后 **292 只** 参与横截面排名），用 Yahoo Finance **近 1 年日线 OHLCV** 精确计算用户指定的 **7 个 WorldQuant 101 因子**（Alpha#1/#6/#12/#19/#30/#41/#53），每因子做 **横截面百分位 rank（0–1，并列取平均）**，**等权合成**，映射为 **1–10 分**。
- **今日市场（11-25）**：三大指数小幅收跌、VIX 反弹 +7.3%，但 **休市日 + 期货回升** 指向假日后反弹预期；热点集中在 **关税/利率博弈** 与 **AI 交易回吐**。**板块**：Materials（XLB +2.07%）领涨，Technology（XLK −0.83%）偏弱，Health Care/Consumer Staples 等防御板块相对抗跌。**本模型当日选出的 Top 20 偏向“超跌均值回复 + 趋势确认 + 量价共振”而非纯动量**：市值最重的金融/医疗/能源/消费龙头多次入选，**纯科技仅 INTU/ADBE**。
- **Top 20 结构**：医疗保健 6、能源 4、金融 2、必需消费品 2、房地产 2、信息技术 2、工业 1、公用事业 1。
- **最强共振**：CBOE（#19+#41+#53 三强）、JNJ（#41+#53+#19）、CVS（#1+#53+#41）、INTU（#1+#12+#41+#53）等。
- **首要风险**：因子是**短窗口代理**，**非基本面/估值**；**超跌≠反转**；**daily VWAP 以典型价 (H+L+C)/3 代理**；**免费源 screener 与 chart 快照存在轻微口径差异**；**用户对 #1/#6/#19/#30 的改写与原版 WorldQuant 符号/公式不完全一致**；**不构成投资建议**。

---

## 1. 市场概览（今日热点 / 指数 / 板块轮动）

### 1.1 主要指数与市场状态（2026-11-25 收盘，Yahoo Finance `v8/finance/chart`）

| 指标 | 数值 | 日变动 | 备注 |
|------|------|--------|------|
| S&P 500 (^GSPC) | 7,182.78 | **−0.25%** | 三大指数中相对抗跌 |
| Nasdaq Composite (^IXIC) | 23,585.80 | **−0.62%** | AI/科技承压偏弱 |
| Dow Jones (^DJI) | 50,182.95 | **+0.33%** | 价值/工业相对强 |
| CBOE VIX (^VIX) | 28.29 | **+7.32%** | 波动率回升 |
| 10-Yr Treasury (^TNX) | 4.848 | −0.056 pt（−1.14%） | 美债收益率回落（Yahoo 首页） |
| 我们的全池个股 | — | 中位 **+0.63%**；**上涨 195 / 下跌 97**（n=292） | 等权个股强于市值加权指数 |

**假日/时段**：2026-11-26 美股 **休市（感恩节）**；期货盘面回升（S&P 期货 +0.56%、Dow 期货 +0.33%、Nasdaq 期货 +0.79%、Russell 2000 期货 +0.44%，Yahoo 首页）；黄金 +1.22%、原油 +0.50%、比特币 +2.29%。本报告因子以 **11-25 收盘** 为准。

### 1.2 今日热点（Yahoo Finance 首页头条，11-25/26 窗口，原标题引述）

- **关税与利率**：*“US unveils 20% tariffs on China, EU, others”*；*“Trump's new tariffs raise the risk of 'a more hawkish Fed response'”*；*“New tariffs put rates where they were before Supreme Court stepped in”*；*“Inflation rises, but economic growth remains strong”*。→ 宏观不确定性上升，**防御/低贝塔板块受青睐**。
- **AI 交易回吐**：*“World stocks tumble as Trump tariffs rattle markets, AI rally fades”*（^IXIC −0.62%）；*“Why Jensen Huang's return failed to stop the AI trade sell-off”*；*“How China got access to Nvidia's AI chips despite rules to stop them”*（**NVDA −2.68%**）；*“Dow erases losses, S&P 500 and Nasdaq recover ground amid AI sell-off”*；**JPMorgan 预计 2027 年 $450B AI 融资潮**。→ AI 高估值承压，但资金**并未全面退出**。
- **微软**：*“Microsoft declares a code red in the middle of a 'Patchpocalypse'”*（MSFT −0.80%）。
- **SpaceX/Starlink**：*“FCC clears SpaceX to launch up to 1 million data center satellites”*（SPCX +2.50%）；*“SpaceX, Elon Musk to give one share each to active Trump Accounts”*。
- **台积电 TSMC**：*“Trump heads to Arizona next week for a high-stakes expansion of TSMC's computer chip factories”*（TSM −0.52%）。
- **财报/公司事件**：强生 **$1.34 分红 ex-date 11-24**；好市多财报 **12-10**；Intuit 财报 **11-19**；塔吉特财报 **11-18**；安捷伦财报 **11-23**；CME 分红 **ex 12-11** 等（见各股）。
- **风险提示类**：*“Palo Alto Networks accused by ex-manager of accounting fraud”*（PANW −2.87%）；*“US airlines brace for pricier Embraer planes under a new duty”*（EMBJ −1.49%）；*“Oil holds two-day gain as Mideast tensions fuel market jitters”*。

### 1.3 板块轮动（2026-11-25，Yahoo sector ETF 日变动 + 全池聚合）

**板块 ETF（State Street Select Sector SPDR，11-25 日变动，由 Yahoo chart 计算）：**

| 排名 | 板块 | ETF | 日变动 |
|------|------|-----|--------|
| 1 | Materials 原材料 | XLB | **+2.07%** |
| 2 | Real Estate 房地产 | XLRE | +0.92% |
| 3 | Communication Services 通信服务 | XLC | +0.89% |
| 4 | Industrials 工业 | XLI | +0.83% |
| 5 | Energy 能源 | XLE | +0.74% |
| 6 | Financials 金融 | XLF | +0.71% |
| 7 | Utilities 公用事业 | XLU | +0.48% |
| 8 | Consumer Staples 必需消费品 | XLP | +0.46% |
| 9 | Consumer Discretionary 可选消费 | XLY | −0.20% |
| 10 | Health Care 医疗保健 | XLV | −0.56% |
| 11 | Technology 信息技术 | XLK | **−0.83%** |

**本报告全池（n=292，按 GICS/Nasdaq 板块，等权；日变动中位 + 综合分中位）：**

| 板块 | 家数 | 日变动中位 | 因子综合中位 |
|------|------|-----------|-------------|
| Energy 能源 | 15 | +1.02% | 0.597 |
| Consumer Staples 必需消费品 | 17 | +0.44% | 0.590 |
| Utilities 公用事业 | 17 | +0.61% | 0.578 |
| Real Estate 房地产 | 13 | +1.07% | 0.521 |
| Health Care 医疗保健 | 40 | −0.36% | 0.553 |
| Financials 金融 | 45 | +0.85% | 0.497 |
| Materials 原材料 | 9 | +1.76% | 0.387 |
| Industrials 工业 | 43 | +0.90% | 0.448 |
| Consumer Discretionary 可选消费 | 26 | +1.39% | 0.488 |
| Information Technology 信息技术 | 53 | −0.28% | 0.400 |
| Communication Services 通信服务 | 13 | −0.57% | 0.489 |

→ **轮动方向**：今日价格动量偏向 Materials/Energy/Real Estate；**本因子模型偏好防御 + 超跌反转**（Consumer Staples/Utilities/Health Care/Energy 因子综合靠前），**Information Technology 价格与因子双弱**。

---

## 2. 方法与评分公式（透明可复现）

### 2.1 候选池与过滤

1. **来源**：Nasdaq screener `api.nasdaq.com/api/screener/stocks`（全市场 ~7,365 只快照）。
2. **过滤**：国家=United States；**marketCap ≥ $10,000,000,000**；**普通股**（剔除 ETF/基金/Warrant/Right/Unit/Preferred/“ZONES”/“tracking stock”/“when issued”/“depositary” 等）；**按市值取前 300**；进一步要求 **≥60 根日线** 且 **7 个因子全部可计算**；**实际参与排名 n = 292**。
3. 已剔除明显死标的（如 `CCZ` 价格恒定、零成交、市值异常）与历史不足（如近期上市 `VYLR`，仅 ~40 根）。

### 2.2 数据

- **日线 OHLCV（近 1 年，~251 根）**：Yahoo Finance `query1.finance.yahoo.com/v8/finance/chart/{sym}?interval=1d&range=1y`；**最后一根 = 2026-11-25**（292/292）；使用 **原始价**计算因子（WorldQuant 语义；**非 adjclose**），`volume=null→0`，**丢弃 O/H/L/C 缺失日**；并列缺失日剔除。**Pearson 相关 = 总体相关**；**stddev = 总体标准差**。
- **市值/板块**：Nasdaq screener `marketCap`（字符串→数值）+ **S&P500 GICS** 映射（GitHub `datasets/s-and-p-500-companies`）+ Yahoo 个股页板块**交叉验证**（`EPD` Nasdaq 误标 Utilities，Yahoo/GICS 为 **Energy**，已修正）。**中文公司名为译，非公司官方**。
- **基本面/事件**：Yahoo 个股页（EPS(TTM)、1y Target、分红 ex-date、Earnings Date、板块）+ Yahoo 首页头条。**screener 的 `pctchange`/`lastsale` 未用于因子**（与 chart 收盘存在轻微口径/时间差，见 §6）。

### 2.3 因子定义（**严格采用用户给定公式**；符号说明 + 与原版 WorldQuant 101 的差异）

记号：`close/open/high/low/volume`；`vwap`；`returns=close/prev_close−1`；`delta(x,d)=x−delay(x,d)`；`delay(x,d)`；`correlation(x,y,d)`=d 日滚动 Pearson；`stddev(x,d)`；`rank(x)`=**横截面百分位（0,1，并列取平均）**；`scale(x)`=**重标使 Σ|x|=1**；`sign`。

| Alpha | 用户给定公式（原文） | 本报告实际计算 | 高值含义（在本模型里） | 与原版 WorldQuant 101 |
|-------|----------------------|----------------|------------------------|------------------------|
| **#1 动量** | `Rank(Correlation(Delay(close,1), close, 10))` | `pearson(close[t-10..t-1], close[t-9..t])` → `rank` | 价格自相关/持续性更强 | **原版 #1 为 `(rank(ts_argmax(signedpower((returns<0?stddev(returns,20):close),2),5))-0.5)`；用户改写** |
| **#6 开盘-量能** | `Correlation(open, volume, 10)` | `pearson(open[t-9..t], volume[t-9..t])` → `rank`（用户未写外层 rank，**为打分做横截面 rank，raw 保留**） | 开盘价与成交量同向（放量高开） | **原版 #6 为 `-1 * correlation(open, volume, 10)`；用户去掉 −1** |
| **#12 量价背离** | `sign(delta(volume, 1)) * (-1 * delta(close, 1))` | `sign(V[t]-V[t-1]) * -(close[t]-close[t-1])` → `rank` | 放量+跌价 或 缩量+涨价（量价背离） | **与原版 #12 一致** |
| **#19 均值回复** | `(-1 * rank((stddev(abs((close - open)), 5) + (close - open) + rank(correlation(close, open, 10))))`（**括号不配平**） | 重构：`-1 * rank( stddev(abs(close-open),5) + (close-open) + rank(correlation(close,open,10)) )`；**两步**：先算 `rank(correlation(close,open,10))` 再 `rank` 内层和 | 近 5 日波动小 + 收盘<开盘 + 开收低相关 → 超跌回复 | **原版 #19 为 `(-1*sign((close-delay(close,7))+delta(close,7)))*(1+rank(1+sum(returns,250)))`；用户改写** |
| **#30 波动率** | `((-1 * rank(((2 * scale(rank(((((close - low) - (high - close)) / (high - low)) * volume))) - scale(rank(delta(close, 3)))))) * sum(volume, 5)`（**括号不配平**） | 重构：`( -1 * rank( 2*scale(rank(X)) - scale(rank(delta(close,3))) ) ) * sum(volume,5)`，其中 `X=((close-low)-(high-close))/(high-low)*volume`；**两步** rank/scale | 复杂波动结构 + 高成交 | **原版 #30 为 `((1-rank(sign(close-D1)+sign(D1-D2)+sign(D2-D3)))*sum(volume,5))/sum(volume,20)`；用户改写** |
| **#41 趋势强度** | `((high * low)^0.5) - vwap` | `sqrt(high[t]*low[t]) - vwap[t]` → `rank` | 价格典型中枢 > VWAP | **与原版 #41 一致；但 `vwap` 见下** |
| **#53 反转** | `-1 * Delta((((close - low) - (high - close)) / (close - low)), 9)` | `r[t]=(close-low - (high-close))/(close-low)`；`-(r[t]-r[t-9])`；分母 `close-low==0`→缺失 → `rank` | 9 日内盘中相对位置改善 | **与原版 #53 一致** |

**⚠️ 公式诚实性说明**：
- 用户对 **#1、#6、#19、#30** 的写法与 **Kakushadze (2016)《101 Formulaic Alphas》原版** **不完全一致**（原版 #6 带 −1、#1/#19/#30 完全不同公式）；**本报告一律以用户给定公式为准**，并在上表标注差异。因此“WorldQuant 因子”此处指**借用其算子与结构的透明代理**，**不保证与 WorldQuant 商业引擎输出一致**。
- **#19/#30 括号不配平**，已重构为自然配平读法（上表），并明确**两步 rank/scale 顺序**；若用户本意不同，可据 raw 值复核。
- **`vwap` 代理**：免费日线不提供**真日内 VWAP**；Alpha#41 的 `vwap` 用 **典型价 `(high+low+close)/3`** 代理（亦为本报告 Alpha#41 raw 中的 `vwap_proxy`）。原版 WorldQuant 用真 daily VWAP。**#41 数值会因此略偏**。

### 2.4 综合评分

- 每因子 **横截面 rank**（n=292）→ 每只股 7 个百分位；**缺失因子剔除后等权平均**（本 Top 20 均 7/7）。
- **综合分（1–10）= 1 + 9 × mean(7 个百分位)**；保留 1 位小数；`composite_pct=mean`。
- **匹配因子（1–2 个核心因子）**：取该股 **百分位最高的 2 个**。
- **方向/强度标签**：百分位 ≥0.90 **极强**；0.75–0.90 **强**；0.50–0.75 **中**；<0.50 **弱**；并给 **raw 值符号**。
- **不等权、不做行业中性、不做择时/风控**；**不含基本面/估值/质量**；**不构成投资建议**。

---

## 3. 因子信号总览（Top 20 共振）

- **最常出现的匹配因子**：**#41 趋势强度**（多次）、**#53 反转**、**#19 均值回复**、**#1 动量**、**#12 量价背离**；**#6 开盘-量能**、**#30 波动率** 亦入围。
- **系统性特征（与 11-25 下跌/假日环境一致）**：当日普遍 `rank(a41)`/`rank(a53)`/`rank(a19)` 高 → **超跌反转 + 趋势确认 + 均值回复** 主导，**纯动量 #1 并非最强**；**科技股价格偏弱** 而 **防御/能源/医疗** 更易入选。
- **注意**：高 `rank` ≠ 一定上涨；#19/#53 是**短窗口反转**，#1 是**持续性**，#12 是**量价背离**，#30 含**成交量放大**，#41 是**VWAP 代理下的中枢**。**信号叠加 ≠ 基本面看多**。

---

## 4. Top 20 排名表

| 排名 | 代码 | 公司名称（中英文） | 板块 | 市值 | 综合评分(1-10) | 匹配 Alpha 因子 |
|------|------|-------------------|------|------|---------------|-----------------|
| 1 | **CBOE** | Cboe Global Markets（芝加哥期权交易所集团 / Cboe全球市场） | Financials 金融 | ~$40.5B | **8.90** | #19 均值回复、#41 趋势强度 |
| 2 | **JNJ** | Johnson & Johnson（强生） | Health Care 医疗保健 | ~$666.3B | **7.98** | #53 反转、#41 趋势强度 |
| 3 | **COST** | Costco Wholesale（好市多） | Consumer Staples 必需消费品 | ~$483.0B | **7.96** | #41 趋势强度、#53 反转 |
| 4 | **VTR** | Ventas（威塔斯/文塔斯，医疗房地产REIT） | Real Estate 房地产 | ~$46.1B | **7.95** | #19 均值回复、#53 反转 |
| 5 | **CCI** | Crown Castle（冠军城堡，通信塔REIT） | Real Estate 房地产 | ~$35.4B | **7.92** | #53 反转、#41 趋势强度 |
| 6 | **RPRX** | Royalty Pharma（皇家制药） | Health Care 医疗保健 | ~$40.9B | **7.79** | #6 开盘-量能、#19 均值回复 |
| 7 | **RSG** | Republic Services（共和服务/美国共和环境服务） | Industrials 工业 | ~$76.8B | **7.78** | #53 反转、#30 波动率 |
| 8 | **CVS** | CVS Health（CVS健康） | Health Care 医疗保健 | ~$104.3B | **7.67** | #1 动量、#53 反转 |
| 9 | **EPD** | Enterprise Products Partners（企业产品合伙人，MLP） | Energy 能源* | ~$77.5B | **7.63** | #6 开盘-量能、#19 均值回复 |
| 10 | **INTU** | Intuit（财捷） | Information Technology 信息技术 | ~$73.4B | **7.62** | #41 趋势强度、#53 反转 |
| 11 | **OXY** | Occidental Petroleum（西方石油） | Energy 能源 | ~$53.5B | **7.51** | #53 反转、#1 动量 |
| 12 | **TGT** | Target（塔吉特） | Consumer Staples 必需消费品** | ~$79.9B | **7.51** | #19 均值回复、#41 趋势强度 |
| 13 | **XEL** | Xcel Energy（Xcel能源） | Utilities 公用事业 | ~$51.9B | **7.37** | #6 开盘-量能、#19 均值回复 |
| 14 | **ABBV** | AbbVie（艾伯维） | Health Care 医疗保健 | ~$530.1B | **7.31** | #19 均值回复、#41 趋势强度 |
| 15 | **CI** | Cigna（信诺） | Health Care 医疗保健 | ~$72.5B | **7.28** | #1 动量、#41 趋势强度 |
| 16 | **CME** | CME Group（芝商所/芝加哥商品交易所集团） | Financials 金融 | ~$111.5B | **7.19** | #41 趋势强度、#30 波动率 |
| 17 | **MPC** | Marathon Petroleum（马拉松石油） | Energy 能源 | ~$96.7B | **7.19** | #1 动量、#12 量价背离 |
| 18 | **XOM** | ExxonMobil Holdings（埃克森美孚） | Energy 能源 | ~$647.3B | **7.16** | #53 反转、#41 趋势强度 |
| 19 | **ADBE** | Adobe（奥多比） | Information Technology 信息技术 | ~$90.2B | **7.15** | #53 反转、#30 波动率 |
| 20 | **A** | Agilent Technologies（安捷伦科技） | Health Care 医疗保健 | ~$51.9B | **7.14** | #6 开盘-量能、#53 反转 |

> 市值来源 Nasdaq screener（快照，略有口径差异）；Yahoo 个股页市值可略不同。\* **EPD 板块修正为 Energy**（Nasdaq 误标 Utilities；Yahoo/GICS=Energy；MLP）。\*\* 本数据集中 **TGT 板块=Consumer Staples**（见 S&P500 GICS；Yahoo 显示 Consumer Defensive；现实 GICS 多归 Consumer Discretionary，**以本环境数据为准**）。**中文译名为译，非公司官方**。

---

## 5. 逐股因子解读（Top 20 详解）

> 每只给出：**匹配因子（1–2）+ 当前因子值方向 + 强度（横截面百分位）**；并附当日涨跌、市值、基本面/近期事件、投资逻辑、风险。**raw=原始值；pct=横截面百分位(0–1)**。

### 1) CBOE — Cboe Global Markets（芝加哥期权交易所集团）｜Financials｜~$40.5B｜评分 **8.90**
- **当日**：−2.96%（11-24 362.52→11-25 351.80；**screener 口径冲突见 §6**）；**7/7 因子**。
- **匹配因子**：**Alpha#19 均值回复**（pct **1.00 极强**；raw a19=−0.002，近5日波动小+收<开+低相关）+ **Alpha#41 趋势强度**（pct **1.00 极强**；raw a41=**+2.6556**，sqrt(H·L)−vwap 全池最高）。辅助：#12 pct0.97（放量跌/背离）、#30 pct0.79、#53 pct**1.00**（raw +115.66，9日盘中相对位置大改善）、#6 pct0.77、#1 pct0.61。
- **投资逻辑**：超跌 + 中枢偏强 + 9 日反转三重共振；11-25 放量下跌后均值回复信号极强；**EPS(TTM)=14.05、1y Target≈360.27、分红 $0.86 ex-date 11-30**。Cboe 受益于交易活跃度/VIX 上行（当日 VIX +7.3%）与清算收入。
- **风险**：**公司=交易所本身**，对市场成交量/波动率高度敏感；当日下跌是否为趋势起点未定；**screener 与 chart 当日口径冲突**；高相关性结构使多因子“共振”可能是同一信号；**因子≠基本面**。**⚠️ 建议人工复核 CBOE 数据质量后再用**。

### 2) JNJ — Johnson & Johnson（强生）｜Health Care｜~$666.3B｜评分 **7.98**
- **当日**：−0.91%（276.46→273.94；**分红 $1.34 ex-date 11-24**；After-hours 274.01）；Yahoo 页市值 $659.5B、**PE(TTM)41.95、EPS 6.53、1y Target 279.85、Beta0.20**；**Earnings 1/26/2027**；JPMorgan 11/20 维持 Neutral、目标 285→300；**3Y +95%、YTD +32%**。
- **匹配因子**：**Alpha#53 反转**（pct **0.99 极强**；raw +11.11）+ **Alpha#41 趋势强度**（pct **0.99 极强**；raw +0.8897）。辅助：#19 pct0.98（raw −0.015）、#12 pct0.79、#30 pct0.66、#1 pct0.73、#6 pct0.27。
- **投资逻辑**：防御龙头 + 低贝塔 + 高分红；11-25 小跌后反转/趋势强；分红日、财报在即。
- **风险**：估值不低（PE~42）；医疗诉讼/专利/监管；**因子为短窗口代理**。

### 3) COST — Costco Wholesale（好市多）｜Consumer Staples｜~$483.0B｜评分 **7.96**
- **当日**：−0.45%；**EPS(TTM)=20.76、1y Target≈1,083.69、Earnings 12/10/2026**；YTD/防御属性。
- **匹配因子**：**Alpha#41 趋势强度**（pct **0.99 极强**；raw +1.7558）+ **Alpha#53 反转**（pct **0.99 极强**；raw +16.69）。辅助：#6 pct0.88、#12 pct0.87（放量+跌价背离）、#30 pct0.65、#19 pct0.77、#1 pct0.24。
- **投资逻辑**：必需消费 + 会员费模式 + 超跌反转 + 趋势确认；假日消费关注。
- **风险**：估值偏高；超大单一市场集中；**#12 放量跌价未必是底**；财报 12-10。

### 4) VTR — Ventas（威塔斯/文塔斯）｜Real Estate｜~$46.1B｜评分 **7.95**
- **当日**：+0.22%；**医疗房地产 REIT**；**EPS(TTM)=0.52、1y Target≈99.82、Earnings 2/3/2027**。
- **匹配因子**：**Alpha#19 均值回复**（pct **0.97 极强**；raw −0.025）+ **Alpha#53 反转**（pct **0.96 极强**；raw +0.6118）。辅助：#1 pct**0.96**（raw +0.9040 强持续）、#41 pct0.95（raw +0.1868）、#30 pct0.65、#12 pct0.56、#6 pct0.35。
- **投资逻辑**：医疗 REIT 防御 + 长租约；多因子（#1+#19+#41+#53）共振；轮动中 REIT 强。
- **风险**：利率敏感（关税→利率 hawkish 风险）；医疗租户集中；**EPS 偏低、估值看 FFO**（因子不含 FFO）。

### 5) CCI — Crown Castle（冠军城堡，通信塔REIT）｜Real Estate｜~$35.4B｜评分 **7.92**
- **当日**：+1.11%；**通信塔/小型蜂窝 REIT**；**EPS(TTM)=2.49、1y Target≈93.61、分红 $1.062 ex-date 12-15**；Earnings 10/22。
- **匹配因子**：**Alpha#53 反转**（pct **0.98 极强**；raw +1.50）+ **Alpha#41 趋势强度**（pct **0.92 强**；raw +0.0724）。辅助：#1 pct0.88（raw +0.8485）、#6 pct0.75、#30 pct0.69、#19 pct0.79、#12 pct0.37。
- **投资逻辑**：REIT 轮动 + 9日反转 + 动量持续；利率回落利好；分红。
- **风险**：利率/融资成本；5G/通信资本开支；**估值看 FFO/AFFO，因子不覆盖**。

### 6) RPRX — Royalty Pharma（皇家制药）｜Health Care｜~$40.9B｜评分 **7.79**
- **当日**：−1.04%；**royalty/版税模式**；**EPS(TTM)=1.53、1y Target≈75.25**；screener 当日 +2.49%（口径差）。
- **匹配因子**：**Alpha#6 开盘-量能**（pct **0.98 极强**；raw **+0.7754**，10日 open-volume 强正相关）+ **Alpha#19 均值回复**（pct **0.98 极强**；raw −0.022）。辅助：#41 pct0.94（raw +0.1374）、#30 pct0.72、#12 pct0.66、#1 pct0.33、#53 pct0.66。
- **投资逻辑**：轻资产版税 + 高现金流 + 量价/均值回复双强；医疗防御。
- **风险**：版税到期/专利悬崖；海外监管；现金流长周期；**screener/chart 口径差**。

### 7) RSG — Republic Services（共和服务）｜Industrials｜~$76.8B｜评分 **7.78**
- **当日**：+0.80%；**废弃物/环保服务**；**EPS(TTM)=7.22、1y Target≈257.42、Earnings 2/16/2027**。
- **匹配因子**：**Alpha#53 反转**（pct **0.96 极强**；raw +0.4658）+ **Alpha#30 波动率**（pct **0.89 强**；raw −8.79e5，含 volume5 故负大，**看 pct**）。辅助：#12 pct0.77（放量+跌价）、#19 pct0.77、#41 pct0.80、#6 pct0.70、#1 pct0.38。
- **投资逻辑**：防御型工业 + 稳定现金流 + 反转/波动结构；环保需求。
- **风险**：油价/燃料成本；监管；**#30 raw 巨负勿直读，看 pct**。

### 8) CVS — CVS Health（CVS健康）｜Health Care｜~$104.3B｜评分 **7.67**
- **当日**：+0.46%；**医疗+药房+PBM**；**EPS(TTM)=8.61、1y Target≈109.31**；screener +2.32%（口径差）。
- **匹配因子**：**Alpha#1 动量**（pct **0.98 极强**；raw +0.9227 强持续）+ **Alpha#53 反转**（pct **0.97 极强**；raw +0.9462）。辅助：#41 pct0.91（raw +0.0604）、#19 pct0.78、#6 pct0.74、#12 pct0.47、#30 pct0.35。
- **投资逻辑**：动量 + 反转 + 趋势三重；PBM/医保整合进展；防御属性。
- **风险**：PBM 利润率压力；医保政策；债务/商誉；**screener/chart 口径差**。

### 9) EPD — Enterprise Products Partners（企业产品合伙人，MLP）｜Energy*｜~$77.5B｜评分 **7.63**
- **当日**：+0.17%；**能源基础设施 MLP**；**板块修正 Energy**；**EPS(TTM)=3.02、1y Target≈41.67**。
- **匹配因子**：**Alpha#6 开盘-量能**（pct **0.92 强**；raw +0.3705）+ **Alpha#19 均值回复**（pct **0.86 强**；raw −0.143）。辅助：#1 pct0.83（raw +0.8244）、#41 pct0.85（raw −0.0123）、#12 pct0.55、#30 pct0.57、#53 pct0.58。
- **投资逻辑**：能源基础设施 + 分红 + 动量/均值回复；能源轮动偏强。
- **风险**：**MLP 税务结构（UBT）**；利率/融资；管道商品价敏感；**因子不含分派覆盖**。**板块源分歧已标注**。

### 10) INTU — Intuit（财捷）｜Information Technology｜~$73.4B｜评分 **7.62**
- **当日**：−2.76%；**会计/税务/小贷 SaaS**；**EPS(TTM)=17.57、1y Target≈358.63、Earnings 11/19**；screener +0.94%（口径差）。
- **匹配因子**：**Alpha#41 趋势强度**（pct **0.98 极强**；raw +0.6425）+ **Alpha#53 反转**（pct **0.96 极强**；raw +0.4882）。辅助：#1 pct**0.93**（raw +0.8856）、#12 pct**0.94**（放量+跌价）、#30 pct0.59、#19 pct0.56、#6 pct0.19。
- **投资逻辑**：超跌 + 动量残留 + 趋势确认；抗周期财务软件；AI 整合。
- **风险**：**11-25 放量下跌、当日 −2.76%**；AI 颠覆叙事；财报已过（11-19）后续指引；**技术强≠基本面**。

### 11) OXY — Occidental Petroleum（西方石油）｜Energy｜~$53.5B｜评分 **7.51**
- **当日**：+1.07%；**油气+化工**；**EPS(TTM)=4.49、1y Target≈70.63、分红 $0.28 ex-date 12-10**。
- **匹配因子**：**Alpha#53 反转**（pct **0.92 强**；raw −0.0143，**注 raw 为负、看 pct**）+ **Alpha#1 动量**（pct **0.89 强**；raw +0.8620）。辅助：#6 pct0.86、#41 pct0.78、#12 pct0.63、#19 pct0.77、#30 pct0.21。
- **投资逻辑**：能源轮动 + 反转 + 动量；油价/Mideast 风险溢价；低分红。
- **风险**：油价波动；地缘（Mideast）；化工周期；**#53 raw 负勿误读**。

### 12) TGT — Target（塔吉特）｜Consumer Staples**｜~$79.9B｜评分 **7.51**
- **当日**：−2.18%；**大众零售**；**EPS(TTM)=10.76、1y Target≈172.54、Earnings 11/18**；screener +4.53%（口径差）。
- **匹配因子**：**Alpha#19 均值回复**（pct **0.98 极强**；raw −0.019）+ **Alpha#41 趋势强度**（pct **0.97 极强**；raw +0.2589）。辅助：#12 pct0.84（放量+跌价）、#1 pct0.68、#6 pct0.70、#30 pct0.79、#53 pct**0.11 弱**（raw −28.2，9日反转为负）。
- **投资逻辑**：11-25 放量下跌超跌 + 趋势确认 + 均值回复；必需消费；**但 #53 弱、当日跌幅大，反转未确认**。
- **风险**：**11-25 −2.18% + #12 放量跌价 + #53 弱**；同店/促销；消费信用；板块口径分歧；**screener/chart 口径差**。

### 13) XEL — Xcel Energy（Xcel能源）｜Utilities｜~$51.9B｜评分 **7.37**
- **当日**：+0.36%；**受监管公用事业**；**EPS(TTM)=4.29、1y Target≈90.55**。
- **匹配因子**：**Alpha#6 开盘-量能**（pct **0.97 极强**；raw +0.5609）+ **Alpha#19 均值回复**（pct **0.90 强**；raw −0.103）。辅助：#41 pct0.85（raw −0.0077）、#53 pct0.78、#1 pct0.48、#12 pct0.59、#30 pct0.39。
- **投资逻辑**：防御公用事业 + 低波动 + 均值回复；利率回落 + AI 数据中心用电需求叙事。
- **风险**：利率敏感；监管回报率；资本开支；**#41 raw 微负**。

### 14) ABBV — AbbVie（艾伯维）｜Health Care｜~$530.1B｜评分 **7.31**
- **当日**：−1.93%；**制药（Immunology/Oncology 等）**；**EPS(TTM)=5.82、1y Target≈315.88、Earnings 2/3/2027**。
- **匹配因子**：**Alpha#19 均值回复**（pct **0.99 极强**；raw −0.005）+ **Alpha#41 趋势强度**（pct **0.99 极强**；raw +1.2419）。辅助：#12 pct0.90（放量+跌价）、#30 pct0.90、#6 pct0.48、#1 pct0.21、#53 pct0.42。
- **投资逻辑**：超跌 + 趋势 + 放量背离；高分红成长；专利/管线。
- **风险**：**11-25 放量下跌**；专利悬崖；管线失败；收购整合（Allergan 等）；估值。

### 15) CI — Cigna（信诺）｜Health Care｜~$72.5B｜评分 **7.28**
- **当日**：−1.30%；**医疗保险**；**EPS(TTM)=22.68、1y Target≈344.40、分红 $1.56 ex-date 12-3**；Earnings 2/4/2027。
- **匹配因子**：**Alpha#1 动量**（pct **0.97 极强**；raw +0.9137）+ **Alpha#41 趋势强度**（pct **0.94 强**；raw +0.1119）。辅助：#12 pct0.83（放量+跌价）、#19 pct0.83、#30 pct0.66、#6 pct0.22、#53 pct0.43。
- **投资逻辑**：动量残留 + 趋势 + 超跌 + 背离；医保利润率改善。
- **风险**：医保赔付/MLR；监管；会员增长；**当日 −1.3%**。

### 16) CME — CME Group（芝商所）｜Financials｜~$111.5B｜评分 **7.19**
- **当日**：+0.81%；**衍生品交易所**；**EPS(TTM)=12.20、1y Target≈318.12、分红 $1.30 ex-date 12-11**。
- **匹配因子**：**Alpha#41 趋势强度**（pct **0.92 强**；raw +0.0707）+ **Alpha#30 波动率**（pct **0.81 强**；raw −2.03e6，**看 pct**）。辅助：#12 pct0.79（放量+跌价）、#1 pct0.63、#19 pct0.71、#6 pct0.62、#53 pct0.34。
- **投资逻辑**：趋势 + 波动结构 + 放量背离；**波动率/利率上行利好交易量**；与 CBOE 同业对比。
- **风险**：对市场成交/波动率敏感；清算风险；**#30 raw 勿直读**；与 CBOE 高度相关。

### 17) MPC — Marathon Petroleum（马拉松石油）｜Energy｜~$96.7B｜评分 **7.19**
- **当日**：−2.50%；**炼油**；**EPS(TTM)=50.47、1y Target≈447.18、Earnings 2/2/2027**。
- **匹配因子**：**Alpha#1 动量**（pct **1.00 极强**；raw +0.9389 全池最高）+ **Alpha#12 量价背离**（pct **0.95 强**；raw +8.89）。辅助：#53 pct0.91、#6 pct0.61、#30 pct0.53、#19 pct0.40、#41 pct0.41。
- **投资逻辑**：强动量 + 放量背离 + 反转；能源轮动；炼油裂解价。
- **风险**：**11-25 −2.50% + #12 放量跌价**；炼油利润率；油价；能源周期；**高动量易反转**。

### 18) XOM — ExxonMobil Holdings（埃克森美孚）｜Energy｜~$647.3B｜评分 **7.16**
- **当日**：−0.09%；**综合能源**；**EPS(TTM)=9.72、1y Target≈184.18**；股息龙头。
- **匹配因子**：**Alpha#53 反转**（pct **0.97 极强**；raw +0.8288）+ **Alpha#41 趋势强度**（pct **0.90 强**；raw +0.0552）。辅助：#1 pct0.87、#19 pct0.82、#12 pct0.56、#6 pct0.39、#30 pct0.28。
- **投资逻辑**：超大盘能源龙头 + 反转 + 趋势 + 防御分红；Mideast 风险溢价。
- **风险**：油价；地缘；资本纪律；能源政策。

### 19) ADBE — Adobe（奥多比）｜Information Technology｜~$90.2B｜评分 **7.15**
- **当日**：+0.32%；**创意/文档 SaaS**；**EPS(TTM)=17.91、1y Target≈266.91、Earnings 12/9/2026**。
- **匹配因子**：**Alpha#53 反转**（pct **0.95 强**；raw +0.3599）+ **Alpha#30 波动率**（pct **0.76 强**；raw −2.79e6，**看 pct**）。辅助：#1 pct0.72、#12 pct0.66、#6 pct0.52、#41 pct0.68、#19 pct0.50。
- **投资逻辑**：反转 + 波动结构；SaaS 护城河；AI（Firefly）叙事；**但科技板块偏弱**。
- **风险**：AI 颠覆/订阅压力；估值；**科技板块轮动弱**；**#30 raw 勿直读**。

### 20) A — Agilent Technologies（安捷伦科技）｜Health Care｜~$51.9B｜评分 **7.14**
- **当日**：−2.77%；**分析/诊断/仪器**；**EPS(TTM)=5.01、1y Target≈199.34、Earnings 11/23**；screener +4.6%（口径差）。
- **匹配因子**：**Alpha#6 开盘-量能**（pct **0.99 极强**；raw **+0.7893** 近全池最高）+ **Alpha#53 反转**（pct **0.95 强**；raw +0.2706）。辅助：#19 pct0.88（raw −0.116）、#41 pct0.91（raw +0.0624）、#30 pct0.87、#12 pct0.11、#1 pct0.05 **弱**。
- **投资逻辑**：开盘-量能强 + 反转 + 超跌 + 趋势；科学仪器护城河；**但 #1 动量弱、当日 −2.77%**。
- **风险**：**11-25 放量下跌**；生命科学需求；仪器周期；**screener/chart 口径差**；#1 弱。

---

## 6. 数据质量、口径差异与诚实性说明

1. **不构成投资建议**；**非公式回测**；**短窗口代理**；**不含估值/质量/基本面排序**；**等权、无行业中性、无风控**；**昨日信号≠明日收益**。
2. **两套行情源口径差异**：**Nasdaq screener**（`lastsale`/`pctchange`/`marketCap` 快照，**部分标的略滞后/不同口径**）vs **Yahoo chart**（日线收盘，本报告因子所用）。例：**CBOE** screener +2.21% vs chart −2.96%；JNJ −0.91 vs +3.0；ABBV −1.93 vs +3.97；TGT −2.18 vs +4.53；**本报告“当日”与因子一律以 Yahoo chart 为准**，screener 仅用于**市值**与**初筛**。
3. **CBOE 特别标注**：ranked #1 纯属**因子数学**；同时存在 **screener/chart 当日冲突**、**exchange 本身高相关结构**、`a53 raw` 极大值；**强烈建议人工核验后再用**。**不因排名而背书**。
4. **#30/#12 raw 量级**：#30 因 `*sum(volume,5)` raw 可达 **数百万负值**；#12 raw=±价格变动；**应看 pct，不要直读 raw 大小**；**方向符号已如实给出**（部分 pct 高但 raw 负，如 OXY #53 raw−0.0143 pct0.92，因横截面相对）。
5. **用户改写 vs 原版 WQ101**：#1/#6/#19/#30 与原版不一致（§2.3）；**#19/#30 重构配平**；**daily VWAP 以 (H+L+C)/3 代理**；**rank/scale 实现细节**可能与 WorldQuant 商业引擎不同。
6. **板块口径**：GICS（S&P500）+ Nasdaq 交叉 + Yahoo 页；**EPD 修正 Energy**；**TGT 本环境=Consumer Staples**（现实多归 Discretionary）；**中文译名为译**。
7. **数据时点**：因子 as-of **2026-11-25**；今日 **11-26 休市**；抓取 **11-26**；**不保证实时**；screener 快照时点与 chart 收盘不同。
8. **环境说明**：本环境 **websearch 不可用**，市场热点/事件来自 **Yahoo Finance 首页 + 个股页（webfetch）**；新闻为原标题引述，**未逐篇核验**；**部分公司中文译名非官方**。

---

## 7. 板块分类汇总（Top 20）

| 板块 | 家数 | 成员 | 平均评分 | 代表因子 |
|------|------|------|----------|----------|
| **Health Care 医疗保健** | 6 | JNJ、RPRX、CVS、ABBV、CI、A | ~7.50 | #19/#41/#53 超跌反转 + 趋势；#12 放量背离 |
| **Energy 能源** | 4 | EPD、OXY、MPC、XOM | ~7.37 | #1 动量、#12、#53、#41；能源轮动 |
| **Financials 金融** | 2 | CBOE、CME | ~8.05 | 交易所：#19/#41/#53 + #30；波动率利好 |
| **Consumer Staples 必需消费品** | 2 | COST、TGT | ~7.74 | 防御 + #19/#41；#12 放量背离（TGT） |
| **Real Estate 房地产** | 2 | VTR、CCI | ~7.94 | 医疗/通信塔 REIT：#19/#53/#41 + #1；利率敏感 |
| **Information Technology 信息技术** | 2 | INTU、ADBE | ~7.39 | 超跌反转 + #41 + #30/#12；科技板块偏弱 |
| **Industrials 工业** | 1 | RSG | 7.78 | 防御工业：#53 + #30 + #12 |
| **Utilities 公用事业** | 1 | XEL | 7.37 | 低波动防御：#6 + #19 + #41 |

**合计 20。** 结构上 **偏防御 + 超跌反转 + 趋势确认**，与 11-25 市场小跌 + VIX 回升 + 关税/AI 回吐环境一致；**纯科技敞口有限**。

---

## 8. 风险提示（通用）

1. **因子失效**：短窗口动量/反转在趋势反转、黑天鹅、风格切换时失效；**超跌≠反转**；**高 pct≠看多**。
2. **口径风险**：screener vs chart 差异、**daily VWAP 代理**、**用户改写 vs 原版**、**rank/scale 实现**、**raw 量级误读**（#12/#30）。
3. **数据风险**：免费源、不保证实时、**死标的/低流动性**已过滤但非零风险、**板块/中文译名非官方**、新闻未逐篇核验。
4. **市场风险（当下）**：**关税→hawkish Fed**、**AI 交易回吐**、**油价/Mideast**、**利率敏感（REIT/Utilities/医疗）**、**休市/假日流动性**、**VIX 上行**。
5. **个股风险**：见各股；特别关注 **CBOE 数据质量**、**MPC/ABBV/TGT/INTU/A 当日放量下跌**、**TGT #53 弱**、**REIT 看 FFO 非 EPS**、**MLP(EPD) 税务**、**医疗/专利/监管**、**交易所对波动率敏感**。
6. **非投资建议**：仅为研究/教育；**不构成买卖建议**；请结合基本面、估值、风险承受、合规与独立判断；**过往/当日因子不预示未来**。

---

## 9. 数据来源

- **Yahoo Finance `v8/finance/chart`**：日线 OHLCV（range=1y, interval=1d）+ meta；指数 `^GSPC/^IXIC/^DJI/^VIX/^TNX`；sector ETF（XLK/XLF/XLE/XLV/XLI/XLY/XLP/XLU/XLRE/XLB/XLC）。
- **Nasdaq `api.nasdaq.com/api/screener/stocks`**：全市场快照（marketCap/sector/lastsale/pctchange），用于 **市值>$10B 初筛 + 市值 + 板块初筛**（口径见 §6）。
- **S&P500 GICS**：GitHub `datasets/s-and-p-500-companies` `constituents.csv`（板块映射）。
- **Yahoo Finance 首页** + **个股页**（`/quote/{sym}/`）：今日头条、EPS/1y Target/分红/Earnings Date/板块/基本面（webfetch）。
- **WorldQuant 101 因子定义**：Kakushadze (2016), *101 Formulaic Alphas*；**用户给定公式为最终依据**（§2.3）。
- 计算脚本为本仓库临时脚本（`fetch.py`/`compute.py`），**结果可复现**；**因子数值经独立手算交叉验证**（JNJ/CBOE/XOM 抽样一致）。

---

> **再次声明：本页为基于 WorldQuant 101 因子逻辑的横截面量化筛选研究，非公式回测、非实时、不构成投资建议。**
