---
title: WorldQuant 101 Alphas 日报 — 美股 Top 20 — 2026-11-21
type: synthesis
created: 2026-11-21
updated: 2026-11-21
sources: [wq101-alpha-daily.md]
tags: [wq101-alpha-daily, worldquant, alphas, factor-investing, quantitative-screening, momentum, reversal, volatility, volume-price, mean-reversion, trend, us-equities, large-cap, semiconductors, ai-infrastructure, daily-digest]
---

# WorldQuant 101 Alphas 日报 — 美股 Top 20 — 2026-11-21

基于 WorldQuant 101 Alpha 因子库（#1 动量、#6 开盘-量相关、#12 量价背离、#19 均值回复、#30 波动率、#41 趋势强度、#53 反转），对美股大市值（市值 > $10B）做公式级横截面代理计算与综合打分。**数据基准：美股常规收盘 Nov 20（Yahoo v8/finance/chart 日线 OHLCV，15 日窗口）；美股 11 月 21 日（周六）已闭合。不构成投资建议。**

---

## 1. 市场概览（美股快照）

**主要指数表现**（Nov 20 收盘）：
- S&P 500 (^GSPC): **6,910.39** (-3.70%)
- Nasdaq 100 (^IXIC): **22,617.73** (-5.28%)
- Dow Jones (^DJI): **48,147.33** (-1.93%)
- Russell 2000 (^RUT): **2,581.79** (-2.76%)
- CBOE 10-Year Treasury (^TNX): **4.9120** (-2.77%)
- CBOE Volatility Index (^VIX): **35.89** (+26.20%)

**板块轮动**（11 个 Select Sector SPDR ETF 一日涨跌，Nov 19→20）：

| 板块 | ETF | 涨跌 |
|------|-----|------|
| Technology | XLK | -7.27% |
| Communication Services | XLC | -2.66% |
| Consumer Cyclical | XLY | -2.95% |
| Industrials | XLI | -3.09% |
| Materials | XLB | -2.19% |
| Energy | XLE | -0.62% |
| Utilities | XLU | -0.74% |
| Health Care | XLV | -0.12% |
| Consumer Staples | XLP | +0.67% |
| Financials | XLF | -1.82% |
| Real Estate | VNQ | -0.97% |

→ 全线回调，仅 XLP 微正；科技板块（XLK）跌最深，与今日个股表现同步（NVDA -14.01%、AVGO -12.19%、TSM -9.48%、MU -13.89%、PLTR -6.63%）。

**放量活跃**（Day Gainers 页面，>$10B）：GPN +13.82%（$24.3B）、ZS +10.22%（$31.8B）、FICO +5.47%（$14.8B）、RKT +4.91%（$39.0B）、EC +4.49%（$27.5B）、RBLX（$33.4B）、ARM（$162.9B）、LITE（$41.8B）。

**热点事件**（参考 11-21 投资热点日报）：NVIDIA Q3 财报盘后（营收 $115.84B +103%、Q4 指引 $130B、Vera Rubin 出货，NVDA -14.01%）；AMD AI 营销强势（-13.25%）；AVGO AI networking 链（-12.19%）；TSM AI 需求（-9.48%）；PLTR AI 高弹性（-6.63%）；Anthropic IPO 招股追踪；CPO/光通信催化（LITE/ARM 强势下跌但反转压力显著）。

---

## 2. 方法与评分公式

**数据来源**：
- 个股行情：Yahoo Finance v8/finance/chart（interval=1d, range=15d）日线 OHLCV（close/high/low/open/volume；VWAP 用典型价 (H+L+C)/3）
- 市值/PE/板块/52 周区间：Yahoo Finance Equity Screener 页面 + 2026-11-20 因子日报补充（FSLR/DE/PFE/DELL/NEE/MMM/SMCI 等）
- 股息：2026-11-20 因子日报（FSLR/ASML/MSFT/MU/DE/GOOGL/DELL/PFE/CAT/NEE/ORCL/META/INTU/TSM/UNH/MMM/XOM/AMZN/NVDA/AAPL），缺失计 0
- 板块 ETF 表现：Select Sector ETF 日线（XLF/XLK/XLY/XLU/XLI/XLE/XLV/XLB/XLP/VNQ/XLC）
- 候选集合：66 只（Equity Screener 行 1-100、Day Gainers >$10B、2026-11-20 因子日报宇宙）；市值 > $10B 筛选全部进入因子打分

**因子计算**（公式级，横截面标准化，f = 5 + 5·tanh(z/2)）：

| 因子 | 计算公式（最近交易日 t） | 正向含义 |
|------|--------------------------|---------|
| Alpha#1 动量 | pearson(close[t-1], close[t], trailing 10) — 滞后动量自相关 | 正 = 近期价格能预测上一日动量 |
| Alpha#6 开盘-量相关 | pearson(open, volume, trailing 10) | 正 = 开盘价与成交量高度相关（开价反映强量） |
| Alpha#12 量价背离 | sign(Δvolume) × (−Δclose) | 正 = 成交量趋势与价格方向相反 |
| Alpha#19 均值回复 | −(std(|close−open|, 5) + (close−open) + rank(corr(close, open, 10))) | 正 = 价格开收范围稳定 + 跌/涨状态利于均值回归 |
| Alpha#30 波动率 | −rank01(2·rank(mf) − rank(Δclose(t,3))) × Σ(volume, 5)，mf = ((c−l)−(h−c))/(h−l) × v | 正 = 量越跌/越大 + 开收区间位更低 |
| Alpha#41 趋势强度 | sqrt(high·low) − vwap(典型价 (H+L+C)/3) | 正 = 开收高于典型价 |
| Alpha#53 反转 | −(r(t) − r(t−9)), r = ((c−l)−(h−c))/(c−l) | 正 = 收价比区间低端更近（反转压力） |

**评分**：
- 因子评分（0-10）= 0.18·f1 + 0.12·f6 + 0.12·f12 + 0.15·f19 + 0.13·f30 + 0.15·f41 + 0.15·f53（f_i 为各因子横截面 z 标准化后映射的 0-10 强度）
- 基本面评分（0-4.5）：PE 理性（<8：0.5；8-15：1.5；15-28：2.0；28-45：1.0；≥45：0；无数据：1.0）+ 股息收益率（>1.2%：1.5；0.3-1.2%：1.0；其他：0；缺失：0）+ 板块强弱（XLF/XLK/XLY/XLI/XLE/XLV/XLB/XLP/VNQ/XLC 一日涨跌 >0.5%：+1）
- 综合评分 = 四舍五入(0.7 × 因子评分 + 0.3 × 基本面评分)，按 综合评分 desc，因子评分 desc 排序

注：因子为横截面代理值（非公式回测）；Alpha#19 的 (close−open) 项用当日价差近似；Alpha#30 的 rank 按横截面标准化实现。

---

## 3. Top 20 排名表

| 排名 | 股票 | 板块 | 市值 | 因子评分 | 基本面评分 | 综合评分 |
|------|------|------|------|----------|-----------|----------|
| 1 | ASML — ASML Holding N.V.（阿斯麦尔） | Technology (Semiconductor Equipment & Materials) | $488.0B | 7.16 | 2.00 | 6 |
| 2 | LITE — Lumentum Holdings Inc.（光子收发器龙头） | Technology | $41.8B | 6.93 | 1.00 | 5 |
| 3 | FSLR — First Solar, Inc.（美国太阳能股份公司） | Solar | $1.27T | 6.43 | 1.50 | 5 |
| 4 | MU — Micron Technology, Inc.（美信捷诺） | Technology (Semiconductors) | $672.6B | 6.28 | 1.50 | 5 |
| 5 | TSM — Taiwan Semiconductor Manufacturing Co.（台积电） | Technology (Semiconductors) | $1.653T | 6.26 | 3.00 | 5 |
| 6 | DELL — Dell Technologies Inc.（戴尔科技） | Computer Hardware | $198.7B | 6.01 | 3.00 | 5 |
| 7 | INTU — Intuit Inc.（Intuit） | Technology (Software—Application) | $72.3B | 6.01 | 3.50 | 5 |
| 8 | CLS — Celestica Inc. | Technology (Communication Equipment) | $25.4B | 5.60 | 2.00 | 5 |
| 9 | META — Meta Platforms, Inc.（Meta 平台） | Communication Services | $1.434T | 5.50 | 3.00 | 5 |
| 10 | NVDA — NVIDIA Corporation（英伟达） | Technology (Semiconductors) | $3.031T | 5.23 | 3.00 | 5 |
| 11 | NEE — NextEra Energy, Inc.（NextEra 能源） | Utilities | $1.27T | 5.19 | 3.50 | 5 |
| 12 | MMM — 3M Company（3M 公司） | Conglomerates | $92.2B | 5.11 | 3.50 | 5 |
| 13 | AVGO — Broadcom Inc.（博通） | Technology (Semiconductors) | $1.453T | 5.97 | 1.00 | 4 |
| 14 | TMO — Thermo Fisher Scientific Inc.（Thermo Fisher） | Healthcare (Diagnostics & Research) | $248.1B | 5.74 | 1.00 | 4 |
| 15 | COST — Costco Wholesale Corporation（Costco 开市乐） | Consumer Defensive (Discount Stores) | $488.4B | 5.69 | 1.00 | 4 |
| 16 | CAT — Caterpillar Inc.（卡特彼勒） | Industrials (Farm & Heavy Construction Machinery) | $233.6B | 5.57 | 2.00 | 4 |
| 17 | DE — Deere & Company（约翰迪尔） | Industrials (Farm & Heavy Construction Machinery) | $168.5B | 5.51 | 2.00 | 4 |
| 18 | NBIS — Nebius Group N.V.（Nebius，AI 云算力） | Technology (Computer Hardware) | $23.8B | 5.41 | 0.00 | 4 |
| 19 | BE — Bloom Energy Corporation（Bloom Energy） | Utilities (Electric Utilities) | $42.1B | 5.37 | 0.00 | 4 |
| 20 | TSLA — Tesla, Inc.（特斯拉） | Consumer Cyclical (Auto Manufacturers) | $1.367T | 5.26 | 0.00 | 4 |

---

## 4. 逐股详情（Top 20）

### 1. ASML — ASML Holding N.V.（阿斯麦尔）
- **板块**：Technology (Semiconductor Equipment & Materials) · **市值**：$488.0B · **PE(TTM)**：36.84 · **股息**：0.67% · **52 周**：946.11-1999.96 · 今日收：1266.22（-6.63%）
- **匹配 Alpha**：Alpha#41（趋势强度）+ Alpha#12（量价背离）
- **因子信号解读**：
  - Alpha#41：α=+9.89（方向正，强度 f=9.76）—— sqrt(H·L)=1296.05 高于典型价 1287.17，开收高于典型价，趋势强
  - Alpha#12：α=+89.98（方向正，强度 f=9.69）—— 成交量抬升 + 价跌（Δv>0，−Δc=+89.98），资金流向与价格回调同步
- **综合评分**：6/10
- **投资逻辑**：半导体设备龙头，今日 -6.63% 放量回调，Alpha#41 与 #12 均显著正向；投机机会在半导体扩张周期调整企稳后继续，PE 36.84 略高但估值中位。
- **风险提示**：PE 偏高（36.8）；AI 光模块/芯片扩张节奏变化风险。

### 2. LITE — Lumentum Holdings Inc.（光子收发器龙头）
- **板块**：Technology · **市值**：$41.8B · **PE**：缺失 · **股息**：缺失 · **52 周**：233.72-1143.00 · 今日收：460.54（-13.93%）
- **匹配 Alpha**：Alpha#19（均值回复）+ Alpha#12（量价背离）
- **因子信号解读**：
  - Alpha#19：α=+35.85（方向正，强度 f=9.43）—— 收价占比比率走低，反转/抛压压力显著，低开
  - Alpha#12：α=+74.61（方向正，强度 f=9.40）—— 今日成交量 15.3M 放大 + 价跌，量价背离强
- **综合评分**：5/10
- **投资逻辑**：AI 光模块热潮下，光子收发器龙头今日 -13.93% 伴随巨量，Alpha#19 与 #12 均显著正向反转压力；若 AI 产能恢复预期，有回升空间。
- **风险提示**：PE 与股息数据缺失，估值不明；光模块供应链波动风险；高波动性。

### 3. FSLR — First Solar, Inc.（美国太阳能股份公司）
- **板块**：Solar · **市值**：$1.27T · **PE(TTM)**：8.79 · **股息**：0.00% · **52 周**：320.95-150.25
- **匹配 Alpha**：Alpha#6（开盘-量相关）+ Alpha#1（动量）
- **因子信号解读**：
  - Alpha#6：α=+0.52（方向正，强度 f=9.08）—— 开盘价与成交量相关度极高
  - Alpha#1：α=+0.96（方向正，强度 f=8.00）—— 近 10 日动量自相关为正，趋势持续
- **综合评分**：5/10
- **投资逻辑**：First Solar -9.45% 回落至 $137.59，PE 8.79 处于成长类低位；动量与开盘-量相关均为正；全球光伏产能紧张有望支撑行业复苏。
- **风险提示**：绿能利润率波动风险；股价跌破周期底部区间，关注反弹企稳。

### 4. MU — Micron Technology, Inc.（美信捷诺）
- **板块**：Technology (Semiconductors) · **市值**：$672.6B · **PE(TTM)**：9.29 · **股息**：0.09% · **52 周**：192.59-1255.00 · 今日收：594.51（-13.89%）
- **匹配 Alpha**：Alpha#19（均值回复）+ Alpha#12（量价背离）
- **因子信号解读**：
  - Alpha#19：α=+46.39（方向正，强度 f=9.77）—— 收价占比比率回升，反转压力中等
  - Alpha#12：α=+95.93（方向正，强度 f=9.76）—— 成交量大幅放大 + 价跌，资金流向与价格回调同步
- **综合评分**：5/10
- **投资逻辑**：Micron -13.89% 放量，体现内存购买结构的弹性调整；均值回复与量价背离均显著，短期调整空间较大。
- **风险提示**：内存需求情绪反转风险大；PE 9.29 低位但跌幅较深。

### 5. TSM — Taiwan Semiconductor Manufacturing Co.（台积电）
- **板块**：Technology (Semiconductors) · **市值**：$1.653T · **PE(TTM)**：21.55 · **股息**：1.04% · **52 周**：266.82-487.47 · 今日收：318.71（-9.48%）
- **匹配 Alpha**：Alpha#53（反转）+ Alpha#12（量价背离）
- **因子信号解读**：
  - Alpha#53：α=+108.17（方向正，强度 f=8.79）—— 收价比区间低端更近（反转压力），且与动量自相关相当（a1 f=6.86）
  - Alpha#12：α=+33.38（方向正，强度 f=7.21）—— 成交量抬升 + 价跌
- **综合评分**：5/10
- **投资逻辑**：TSM -9.48% 放量，但收价占比比率走低（反转压力）+ 开盘-成交量背离；AI 产业链需求企稳后反弹窗口，PE 21.55 中位、股息 1.04%。
- **风险提示**：AI 芯片需求减速风险。

### 6. DELL — Dell Technologies Inc.（戴尔科技）
- **板块**：Computer Hardware · **市值**：$198.7B · **PE(TTM)**：18.17 · **股息**：0.80% · **52 周**：595.51-110.22 · 今日收：278.02（-11.05%）
- **匹配 Alpha**：Alpha#19（均值回复）+ Alpha#12（量价背离）
- **因子信号解读**：
  - Alpha#19：α=+17.87（方向正，强度 f=7.62）—— 低开+均值回复压力
  - Alpha#12：α=+34.52（方向正，强度 f=7.31）—— 成交量抬升 + 价跌
- **综合评分**：5/10
- **投资逻辑**：戴尔 -11.05% 回落，AI 叙事早期，PE 18.17 低位、股息 0.80%；均值回复压力显著。
- **风险提示**：AI 叙事分化风险；利润率缩水风险。

### 7. INTU — Intuit Inc.（Intuit）
- **板块**：Technology (Software—Application) · **市值**：$72.3B · **PE(TTM)**：17.66 · **股息**：1.76% · **52 周**：252.84-682.27 · 今日收：270.44（-12.77%）
- **匹配 Alpha**：Alpha#12（量价背离）+ Alpha#41（趋势强度）
- **因子信号解读**：
  - Alpha#12：α=+39.58（方向正，强度 f=7.72）—— 今日成交量 9.83M 放大 + 价跌
  - Alpha#41：α=+4.39（方向正，强度 f=7.57）—— sqrt(H·L) 高于典型价，趋势偏强
- **综合评分**：5/10
- **投资逻辑**：Intuit 发票搜索 AI 主题下价跌 -12.77%，量价背离明显；PE 17.66 低位、股息 1.76%。
- **风险提示**：AI 叙事分化风险；高估值修复空间。

### 8. CLS — Celestica Inc.
- **板块**：Technology (Communication Equipment) · **市值**：$25.4B · **PE(TTM)**：22.69 · **股息**：-- · **52 周**：197.50-474.03 · 今日收：201.80（-15.99%）
- **匹配 Alpha**：Alpha#19（均值回复）+ Alpha#12（量价背离）
- **因子信号解读**：
  - Alpha#19：α=+18.59（方向正，强度 f=7.74）—— 收价占比比率走低，反转压力（与 -15.99% 大跌同步）
  - Alpha#12：α=+38.43（方向正，强度 f=7.63）—— 成交量抬升 + 价跌
- **综合评分**：5/10
- **投资逻辑**：Celestica -15.99%，收价比区间低端（反转压力）+ 量价背离明显；PE 22.69 中位。
- **风险提示**：成本曲线压缩下行风险；工厂投资周期波动。

### 9. META — Meta Platforms, Inc.（Meta 平台）
- **板块**：Communication Services (Internet Content & Information) · **市值**：$1.434T · **PE(TTM)**：20.33 · **股息**：0.34% · **52 周**：520.26-779.82 · 今日收：560.84（-5.94%）
- **匹配 Alpha**：Alpha#12（量价背离）+ Alpha#41（趋势强度）
- **因子信号解读**：
  - Alpha#12：α=+35.38（方向正，强度 f=7.39）—— 量价背离（价跌量升），跌幅以反转压力为主
  - Alpha#41：α=+4.09（方向正，强度 f=7.30）—— sqrt(H·L) 高于典型价，趋势偏强
- **综合评分**：5/10
- **投资逻辑**：META -5.94%，处于估值修复区间；PE 20.33 中低位，股息 0.34%，广告 AI 叙事仍可维持。
- **风险提示**：广告收入减速风险；AI 摊销预期不及预期。

### 10. NVDA — NVIDIA Corporation（英伟达）
- **板块**：Technology (Semiconductors) · **市值**：$3.031T · **PE(TTM)**：15.68 · **股息**：0.66% · **52 周**：145.71-243.37 · 今日收：125.53（-14.01%）
- **匹配 Alpha**：Alpha#1（动量）+ Alpha#19（均值回复）
- **因子信号解读**：
  - Alpha#1：α=+0.91（方向正，强度 f=7.57）—— 近 10 日动量自相关为正，趋势持续
  - Alpha#19：α=+11.35（方向正，强度 f=6.39）—— 低开+均值回复压力
- **综合评分**：5/10
- **投资逻辑**：NVDA -14.01% 放量，Q3 财报盘后调整；PE 15.68 极低，但均值回复压力显著，谨慎关注 AI 需求弹性恢复。
- **风险提示**：AI 计算需求减速风险；估值修复空间较大。

### 11. NEE — NextEra Energy, Inc.（NextEra 能源）
- **板块**：Utilities (Utilities—Regulated Electric) · **市值**：$1.27T · **PE(TTM)**：15.10 · **股息**：2.94% · **52 周**：74.41-98.75 · 今日收：83.45（-0.41%）
- **匹配 Alpha**：Alpha#1（动量）+ Alpha#6（开盘-量相关）
- **因子信号解读**：
  - Alpha#1：α=+0.91（方向正，强度 f=7.57）—— 近 10 日动量为正
  - Alpha#6：α=+0.05（方向正，强度 f=7.39）—— 开盘价与成交量相关度强
- **综合评分**：5/10
- **投资逻辑**：NEE -0.41% 弱跌；公用事业股稳健动量 + 开盘-量相关；股息 2.94%，PE 15.10 中低位。
- **风险提示**：营销限制导致增长受限风险；公用事业股防御性强但弹性有限。

### 12. MMM — 3M Company（3M 公司）
- **板块**：Conglomerates (Conglomerates) · **市值**：$92.2B · **PE(TTM)**：26.64 · **股息**：1.72% · **52 周**：139.34-196.90 · 今日收：177.99（-1.69%）
- **匹配 Alpha**：Alpha#1（动量）+ Alpha#30（波动率）
- **因子信号解读**：
  - Alpha#1：α=+0.90（方向正，强度 f=7.46）—— 近 10 日动量为正
  - Alpha#30：α=-8,249,140（方向负，强度 f=6.40）—— 放量下跌体现反转压力
- **综合评分**：5/10
- **投资逻辑**：MMM -1.69%，多元化工集团动量稳健；PE 26.64 略偏高，股息 1.72%。
- **风险提示**：多元化价值减弱风险；企业内化销售预期下行。

### 13. AVGO — Broadcom Inc.（博通）
- **板块**：Technology (Semiconductors) · **市值**：$1.453T · **PE(TTM)**：44.25 · **股息**：-- · **52 周**：289.77-495.00 · 今日收：304.41（-12.19%）
- **匹配 Alpha**：Alpha#19（均值回复）+ Alpha#41（趋势强度）
- **因子信号解读**：
  - Alpha#19：α=+24.45（方向正，强度 f=8.54）—— 均值回复压力显著，价跌到开收趋势区间下方
  - Alpha#41：α=+5.18（方向正，强度 f=8.18）—— sqrt(H·L) 高于典型价，放量强
- **综合评分**：4/10
- **投资逻辑**：AVGO -12.19% 放量，AI networking 链调整；PE 44.25 估值偏高，跌幅已触及防守区。
- **风险提示**：估值修复空间有限；AI 叙事分化风险。

### 14. TMO — Thermo Fisher Scientific Inc.（Thermo Fisher）
- **板块**：Healthcare (Diagnostics & Research) · **市值**：$248.1B · **PE(TTM)**：36.30 · **股息**：-- · **52 周**：435.27-727.56 · 今日收：669.54（-2.79%）
- **匹配 Alpha**：Alpha#19（均值回复）+ Alpha#41（趋势强度）
- **因子信号解读**：
  - Alpha#19：α=+13.87（方向正，强度 f=6.90）—— 收价占比比率回升，均值回复中性
  - Alpha#41：α=+3.37（方向正，强度 f=6.60）—— 趋势偏强
- **综合评分**：4/10
- **投资逻辑**：TMO -2.79% 小幅回调；诊断与研究类生物制药龙头，现金流强劲。
- **风险提示**：高 PE 36.30，估值偏高；生物医药研发周期风险。

### 15. COST — Costco Wholesale Corporation（Costco 开市乐）
- **板块**：Consumer Defensive (Discount Stores) · **市值**：$488.4B · **PE(TTM)**：52.69 · **股息**：0.00% · **52 周**：844.06-1123.67 · 今日收：1102.15（+0.76%）
- **匹配 Alpha**：Alpha#6（开盘-量相关）+ Alpha#1（动量）
- **因子信号解读**：
  - Alpha#6：α=+0.54（方向正，强度 f=9.12）—— 开盘价与成交量相关度极高（受利率预期影响高开）
  - Alpha#1：α=+0.87（方向正，强度 f=7.17）—— 近 10 日动量为正
- **综合评分**：4/10
- **投资逻辑**：COST +0.76% 涨跌对冲，量价正相关强；消费防御龙头，PE 52.69 高位估值。
- **风险提示**：估值偏高，股价距 52 周区间上线较近。

### 16. CAT — Caterpillar Inc.（卡特彼勒）
- **板块**：Industrials (Farm & Heavy Construction Machinery) · **市值**：$233.6B · **PE(TTM)**：21.10 · **股息**：1.17% · **52 周**：535.53-1073.46 · 今日收：510.45（-5.01%）
- **匹配 Alpha**：Alpha#41（趋势强度）+ Alpha#12（量价背离）
- **因子信号解读**：
  - Alpha#41：α=+4.21（方向正，强度 f=7.42）—— sqrt(H·L) 高于典型价，今日放量强
  - Alpha#12：α=+26.92（方向正，强度 f=6.61）—— 成交量抬升 + 价跌
- **综合评分**：4/10
- **投资逻辑**：CAT -5.01%，工程投资周期低谷；PE 21.10 低位，股息 1.17%；XLF/XLI 下行共振。
- **风险提示**：工程投资减缓风险；全球建筑市场影响。

### 17. DE — Deere & Company（约翰迪尔）
- **板块**：Industrials (Farm & Heavy Construction Machinery) · **市值**：$168.5B · **PE(TTM)**：35.83 · **股息**：1.01% · **52 周**：455.91-721.22 · 今日收：609.25（-2.50%）
- **匹配 Alpha**：Alpha#1（动量）+ Alpha#30（波动率）
- **因子信号解读**：
  - Alpha#1：α=+0.92（方向正，强度 f=7.68）—— 近 10 日动量为正
  - Alpha#30：α=-6,601,200（方向负，强度 f=6.52）—— 体现反转压力
- **综合评分**：4/10
- **投资逻辑**：DE -2.50%，动量正但仍在底部区间；PE 35.83 偏高但股息 1.01% 回撤。
- **风险提示**：农业装备需求分散风险；PE 偏高。

### 18. NBIS — Nebius Group N.V.（Nebius，AI 云算力）
- **板块**：Technology (Computer Hardware) · **市值**：$23.8B · **PE(TTM)**：230.08 · **股息**：缺失 · **52 周**：73.52-299.86 · 今日收：81.31（-16.11%）
- **匹配 Alpha**：Alpha#1（动量）+ Alpha#6（开盘-量相关）
- **因子信号解读**：
  - Alpha#1：α=+0.79（方向正，强度 f=6.30）—— 近 10 日动量为正
  - Alpha#6：α=-0.18（方向负，强度 f=6.09）—— 开盘价与成交量相关度中等负向
- **综合评分**：4/10
- **投资逻辑**：NBIS -16.11%；AI 云算力需求旺盛，但动量与开盘-量相关信号仍在收敛。
- **风险提示**：PE 230.08 极高，安全边际不足；今日跌幅体现需求预期减退。

### 19. BE — Bloom Energy Corporation（Bloom Energy）
- **板块**：Utilities (Utilities—Electric Utilities) · **市值**：$42.1B · **PE(TTM)**：97.96 · **股息**：缺失 · **52 周**：75.70-351.28 · 今日收：142.39（-15.29%）
- **匹配 Alpha**：Alpha#19（均值回复）+ Alpha#12（量价背离）
- **因子信号解读**：
  - Alpha#19：α=+12.50（方向正，强度 f=6.63）—— 均值回复压力中等，价格接近区间中低端
  - Alpha#12：α=+25.72（方向正，强度 f=6.49）—— 成交量抬升 + 价跌
- **综合评分**：4/10
- **投资逻辑**：BE -15.29%，反转压力与量价背离均显著；可逆燃料电池龙头，有潜在回升窗口。
- **风险提示**：PE 97.96 极高，估值过热；燃料电池产业周期风险。

### 20. TSLA — Tesla, Inc.（特斯拉）
- **板块**：Consumer Cyclical (Auto Manufacturers) · **市值**：$1.367T · **PE(TTM)**：411.36 · **股息**：缺失 · **52 周**：297.38-498.83 · 今日收：345.82（-7.64%）
- **匹配 Alpha**：Alpha#41（趋势强度）+ Alpha#19（均值回复）
- **因子信号解读**：
  - Alpha#41：α=+4.12（方向正，强度 f=7.34）—— sqrt(H·L) 高于典型价，今日 -7.64% 放量
  - Alpha#19：α=+15.33（方向正，强度 f=7.18）—— 低开+收价反转压力
- **综合评分**：4/10
- **投资逻辑**：TSLA -7.64% 放量下跌，但收价反转压力明显；AI 选项（Optimus 等）与 Cybercab 叙事仍在酝酿，动能可能回升。
- **风险提示**：PE 411.36 极高，估值极不安全；AI 选项空间犹豫不决。

---

## 5. 板块分类汇总

| 板块 | 成分 | 平均因子评分 | 平均综合评分 |
|------|------|--------------|--------------|
| Technology | ASML, LITE, MU, TSM, INTU, CLS, NVDA, AVGO, NBIS | 6.09 | 4.89 |
| Utilities | NEE, BE | 5.28 | 4.50 |
| Industrials | CAT, DE | 5.54 | 4.00 |
| Solar | FSLR | 6.43 | 5.00 |
| Computer Hardware | DELL | 6.01 | 5.00 |
| Communication Services | META | 5.50 | 5.00 |
| Conglomerates | MMM | 5.11 | 5.00 |
| Healthcare | TMO | 5.74 | 4.00 |
| Consumer Defensive | COST | 5.69 | 4.00 |
| Consumer Cyclical | TSLA | 5.26 | 4.00 |

*(注：因子值为横截面代理计算，非公式回测；数据截至 Nov 20 收盘；排名参考性强；不构成投资建议。)*
