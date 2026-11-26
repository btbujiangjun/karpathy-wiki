---
title: WorldQuant 101 Alpha 美股 Top 20 精选 — 2026-11-26
type: synthesis
created: 2026-11-26
updated: 2026-11-26
sources: []
tags: [wq101-alpha-daily, worldquant, alphas, factor-investing, quantitative-screening, momentum, reversal, volatility, volume-price, mean-reversion, trend, us-equities, large-cap, daily-digest]
---

# WorldQuant 101 Alpha 美股 Top 20 精选 — 2026-11-26

> **数据基准**：本报告生成于 2026-11-26（Thanksgiving 假期，美股休市，无当日交易）；价格/成交量/估值基准为 **2026-11-25（周三）美股常规时段收盘**。数据来源为 Yahoo Finance Chart API（`v8/finance/chart`, `interval=1d`, `period=3mo`, `auto_adjust=True`）+ `yfinance` quoteSummary（`fast_info`/`get_info`：marketCap、sector、trailingPE/forwardPE、profitMargins、dividendYield、beta 等）+ S&P 500 成分股名单（Wikipedia）。候选池 = 503 只 S&P 500 成分股，过滤后市值 **> $10B**，按下述 WorldQuant 101 因子综合分数排序取 Top 20。
>
> **诚实声明**：本文为**短期技术面因子筛选**，不是基本面投资建议，**不构成投资建议**。因子为公式级计算但含近似（见下文「方法与局限」）；本环境 `websearch` 返回 `cancelled`、Yahoo `get_news` 返回 `YAHOO FINANCE IS CURRENTLY DOWN`，**无法核实当日新闻/财报/事件**，「近期事件」以价格+成交量异动与基本面快照作代理，需自行复核。估值字段为 Yahoo 快照，可能为 TTM/forward 混合口径。

---

## 0. 一句话结论

在 2026-11-25 收盘的**risk-off 偏防御盘面**（S&P 500 −0.25%、Nasdaq −0.62%、VIX +7.3% 至 28.3、VIX 1 个月 +53.8%、科技板块 1 个月 −16.4%、消费纵深/公用事业/医疗/地产领跑）下，**纯 WorldQuant 101 因子（动量 #1/#6 + 反转 #53 + 波动结构 #30 + 量价背离 #12 + 趋势 #41 + 均值回复 #19）横截面综合排序**，倾向选出**低波动、趋势平稳、无量价背离、近期强度未衰减的大盘股**。本期 Top 20 偏向**医疗健康、消费纵深、公用事业、工业/地产防御**，**不含科技/半导体巨头**（NVDA/AAPL/MSFT 等在本公式级筛选中未进前列，原因见风险提示）。头部：**CBOE(8.8)、WST(8.4)、COST(8.2)、LH(8.0)、JNJ(8.0)、VRSK(7.9)、VTR(7.9)、SOLV(7.9)、ES(7.8)、CCI(7.7)**。

---

## 1. 市场概览（美股，2026-11-25 收盘）

| 指数 | 收盘 | 当日 | 5 日 | 1 月 | 备注 |
|------|------|------|------|------|------|
| S&P 500 (^GSPC) | 7,182.78 | −0.25% | −1.92% | −6.43% | 大盘小幅下跌，1 个月显著回调 |
| Nasdaq Composite (^IXIC) | 23,585.80 | −0.62% | −3.46% | −9.87% | 科技领跌，1 个月最弱 |
| Dow Jones (^DJI) | 50,182.95 | +0.33% | −0.03% | −4.16% | 工业/价值相对抗跌 |
| Russell 2000 (^RUT) | 2,704.06 | +0.71% | −0.38% | −2.96% | 小盘当日反弹 |
| CBOE VIX (^VIX) | 28.29 | +7.32% | +15.19% | +53.83% | **波动率显著抬升，risk-off** |

**市场解读**：2026-11-26 为 Thanksgiving 假期，美股休市；基准取 11-25 收盘。整体 **risk-off、板块轮动向防御**：风险偏好下降、VIX 快速上行；Nasdaq 弱于道指；能源/科技 1 个月大幅回调而消费纵深/公用事业/医疗/地产相对稳健。（无法联网核实当日新闻；以下为价格+量能+基本面快照，不含新闻事件。）

---

## 2. 板块轮动（11 板块 ETF，2026-11-25 收盘）

| 板块 | ETF | 当日 | 5 日 | 1 月 |
|------|-----|------|------|------|
| Consumer Staples（消费纵深） | XLP | +0.46% | +1.23% | **+4.93%** |
| Utilities（公用事业） | XLU | +0.48% | +0.14% | +2.49% |
| Real Estate（地产） | XLRE | +0.92% | +0.55% | +2.48% |
| Health Care（医疗） | XLV | −0.56% | +1.39% | +2.45% |
| Communication Services（通信） | XLC | +0.89% | −0.19% | +1.47% |
| Consumer Discretionary（消费循环） | XLY | −0.20% | −1.43% | +2.83% |
| Financials（金融） | XLF | +0.71% | +0.16% | +0.87% |
| Materials（材料） | XLB | +2.07% | +1.49% | −0.33% |
| Industrials（工业） | XLI | +0.83% | −1.04% | −2.40% |
| Energy（能源） | XLE | +0.74% | −0.64% | −12.55% |
| Technology（科技） | XLK | −0.83% | −4.90% | **−16.39%** |

**轮动方向**：资金从 **Technology / Energy**（1 月最弱，−16.4% / −12.6%）向 **Consumer Staples / Utilities / Real Estate / Health Care** 防御板块迁移；当日 Materials 领涨。这与本期 WQ101 筛选偏防御、低波动结果**同向**，但也意味着动量维度对纯科技在本快照期偏弱。

---

## 3. 方法与评分公式（WorldQuant 101 → 公式级计算）

### 3.1 因子（严格按用户给定公式实现；`rank` = 横截面分位，`scale` = 归一化 Σ|x|=1）

| 维度 | Alpha | 用户公式 | 本报告计算 |
|------|-------|----------|-----------|
| 动量 | **#1** | `Rank(Correlation(Delay(close,1), close, 10))` | 10 日滚动 Pearson `corr(close.shift(1), close)` 末值 → 横截面 pct-rank |
| 动量 | **#6** | `Correlation(open, volume, 10)` | 10 日滚动 `corr(open, volume)` 末值 |
| 反转 | **#53** | `-1 * Delta((((close-low)-(high-close))/(close-low)), 9)` | `-(ratio_t − ratio_{t-9})`，`ratio=(C-L-(H-C))/(C-L)=(2C-H-L)/(C-L)` |
| 波动率 | **#30** | `(-1 * rank((2*scale(rank(((((close-low)-(high-close))/(high-low))*volume))) - scale(rank(delta(close,3))))) * sum(volume,5)` | 按公式逐层计算（见下文局限） |
| 量价背离 | **#12** | `sign(delta(volume,1)) * (-1 * delta(close,1))` | `sign(V_t−V_{t-1}) * (C_{t-1}−C_t)` |
| 趋势强度 | **#41** | `(((high*low)^0.5) - vwap)` | `sqrt(H*L) − VWAP_d`，`VWAP_d ≈ (H+L+C)/3`（见局限） |
| 均值回复 | **#19** | `(-1 * rank((stddev(abs(close-open),5) + (close-open) + rank(correlation(close,open,10))))` | `-rank( std5(|C-O|) + (C-O) + rank(corr(C,O,10)) )` |

**与 canonical WorldQuant 101 的差异（诚实标注）**：
- 用户的 **Alpha#1** ≠ canonical WQ#1（canonical `#1 = rank(ts_argmax(signedpower((returns<0)?stddev(returns,20):close,2),5)) − 0.5`）；本文按**用户给定**的 `Rank(Correlation(Delay(close,1),close,10))` 实现。
- 用户的 **Alpha#6** 省略了 canonical 的前导 `-1`（canonical `#6 = -1 * correlation(open, volume, 10)`）；本文按**用户给定**正号实现。
- 用户的 **Alpha#19** ≠ canonical WQ#19（canonical `#19 = -sign((close−delay(close,7))+delta(close,7)) * (1+rank(sum(returns,250)))`）；本文按**用户给定**公式实现。
- **Alpha#41 VWAP**：日线 OHLCV 无法得到 intraday VWAP，用典型价 `(H+L+C)/3` 近似（与本系列既往口径一致）；canonical 用 intraday `vwap`。因此 #41 偏向度量「日内区间位置/平稳度」。
- **Alpha#30**：canonical `scale` 默认 `a=1`（`x/sum(|x|)`）；`rank` 横截面；输出恒为 `≤0`（因 `rank∈[0,1]`、`sum(volume,5)≥0`、前导 −1），「更高=更好」= 量能更小 + 无日内结构；**magnitude 会被巨量放大**，最终再横截面 pct-rank，故 scale-invariant。
- **stddev** 用样本标准差（ddof=1）；`corr` 用 Pearson；`sum(volume,5)` 滚动 5 日成交量。
- `(close−low)=0` / `(high−low)=0` / `(close−low)=0` 的退化项置 NaN；因子末值 NaN 的股票该因子跳过，composite 对可用因子取均值。

### 3.2 横截面标准化与综合评分（本报告自定义、可复现）

1. 每个因子末值在候选池内做 **percentile rank** `p_k ∈ [0,1]`（越高 = 因子越强；这些 alpha 在 canonical 下「更高=更优」，但**本文的高分=强因子信号，非已验证未来收益**）。
2. `composite = mean_k(p_k)`（可用因子等权）。
3. `score_1_10 = clip(round(1 + 9 * composite, 1), 1, 10)`。
4. **匹配因子** = `p_k` 最高的 **1–2 个**（用户要求 1–2 个核心因子）。
5. **候选池**：S&P 500；丢弃近 12 日内收盘缺失、关键窗口不足的标的；**市值 > $10B**（Yahoo `marketCap`，过滤后保留）；去重 Alphabet 双股（保留 GOOGL，剔除 GOOG）。
6. **综合评分仅由 7 个 WQ101 因子决定**；估值/质量/事件仅在「投资逻辑/风险」中披露，**未混入打分**，保持因子纯度（与用户「结合 WQ101 因子逻辑打分」一致）。

### 3.3 因子重叠性（诚实）

实测 7 因子横截面 pct-rank 相关：**F19_mean_rev ↔ F41_trend ≈ 0.92**（都奖励「平稳上行/无内区间破坏」）；其余因子两两 |ρ| ≤ ~0.22。即**有效独立维度约 5 个**，F19+F41 对「平稳趋势」的合计权重略高。这解释了本期低波动防御名的高分。

---

## 4. Top 20 排名表（市值 > $10B，按 composite 排序）

| 排名 | 股票代码 | 公司名称（中英文） | 板块 | 市值 | 综合评分 | 匹配 WorldQuant Alpha 因子 | 当日涨跌 | 收盘价 |
|------|----------|-------------------|------|------|----------|---------------------------|----------|--------|
| 1 | CBOE | Cboe Global Markets（CBOE 全球市场） | Financial Services | $36.7B | 8.8 | **Alpha#19**、**Alpha#41** | −2.96% | $351.80 |
| 2 | WST | West Pharmaceutical Services（西方制药服务） | Healthcare | $26.0B | 8.4 | **Alpha#19**、**Alpha#41** | −4.07% | $372.94 |
| 3 | COST | Costco Wholesale（好市多） | Consumer Defensive | $481.6B | 8.2 | **Alpha#41**、**Alpha#53** | −0.45% | $1,086.81 |
| 4 | LH | Labcorp Holdings（实验室考检集团） | Healthcare | $30.0B | 8.0 | **Alpha#19**、**Alpha#41** | −1.90% | $368.95 |
| 5 | JNJ | Johnson & Johnson（强生） | Healthcare | $659.5B | 8.0 | **Alpha#41**、**Alpha#53** | −0.91% | $273.94 |
| 6 | VRSK | Verisk Analytics（Verisk 分析） | Industrials | $26.3B | 7.9 | **Alpha#53**、**Alpha#41** | +0.39% | $204.76 |
| 7 | VTR | Ventas（文泰斯） | Real Estate | $46.2B | 7.9 | **Alpha#19**、**Alpha#53** | +0.22% | $87.36 |
| 8 | SOLV | Solventum（Solventum 制药） | Healthcare | $14.8B | 7.9 | **Alpha#53**、**Alpha#6** | −1.13% | $87.16 |
| 9 | ES | Eversource Energy（Eversource 能源） | Utilities | $27.3B | 7.8 | **Alpha#53**、**Alpha#41** | −0.15% | $72.55 |
| 10 | CCI | Crown Castle（皇冠城堡通信） | Real Estate | $35.6B | 7.7 | **Alpha#53**、**Alpha#41** | +1.11% | $83.63 |
| 11 | AES | The AES Corporation（AES 公司） | Utilities | $10.7B | 7.7 | **Alpha#1**、**Alpha#19** | 0.00% | $15.02 |
| 12 | RSG | Republic Services（共和服务集团） | Industrials | $77.4B | 7.7 | **Alpha#53**、**Alpha#30** | +0.80% | $254.16 |
| 13 | TGT | Target（塔吉特） | Consumer Defensive | $78.0B | 7.6 | **Alpha#19**、**Alpha#41** | −2.18% | $172.22 |
| 14 | CVS | CVS Health（CVS 健康） | Healthcare | $103.7B | 7.5 | **Alpha#1**、**Alpha#53** | +0.46% | $81.06 |
| 15 | HRL | Hormel Foods（荷美尔食品） | Consumer Defensive | $12.7B | 7.5 | **Alpha#6**、**Alpha#19** | −0.77% | $23.09 |
| 16 | XEL | Xcel Energy（伊克赛尔能源） | Utilities | $52.1B | 7.4 | **Alpha#6**、**Alpha#19** | +0.36% | $81.11 |
| 17 | VYLR | Vylor（Vylor 金融） | Financial Services | $46.4B | 7.4 | **Alpha#1**、**Alpha#53** | +1.31% | $69.47 |
| 18 | ABBV | AbbVie（艾伯维） | Healthcare | $520.5B | 7.4 | **Alpha#19**、**Alpha#41** | −1.93% | $294.48 |
| 19 | INTU | Intuit（财捷） | Technology | $71.7B | 7.4 | **Alpha#41**、**Alpha#53** | −2.76% | $271.72 |
| 20 | OXY | Occidental Petroleum（西方石油） | Energy | $53.9B | 7.4 | **Alpha#53**、**Alpha#1** | +1.07% | $53.95 |

> 中文名为译名/音译；obscure 名称无通用官方中译，以英文为准。因子「方向+强度」见逐股详情。

---

## 5. 逐股详情（Top 20）

> **因子信号解读**：给出匹配 1–2 核心因子的**原始值** + **横截面分位 p**（p≈1=最强）+ **方向**。**注意：高分=强因子信号，非已验证未来收益；Alpha#12/#30 等反转/结构因子本期非 top-2 但仍计入 composite。**「估值/质量」为 Yahoo 快照，不计入打分。**未核实近期事件。**

### 1. CBOE — Cboe Global Markets（CBOE 全球市场）
- **股票代码** CBOE · **板块** Financial Services · **市值** $36.7B · **综合评分** 8.8
- **匹配 WorldQuant 因子**：**Alpha#19 均值回复**（p=1.000，原始 F19≈−0.002，无均值回复压力）+ **Alpha#41 趋势强度**（p=1.000，原始 +2.656，√(H·L)>VWAP）
- **因子信号解读**：最平稳日内区间 + 无量价背离；Alpha#12 p=0.978、#53 p=1.000 同向；唯 Alpha#6 p=0.732。强但当日 −2.96%（量/均量 1.01，非放量）下跌，仍因区间平稳居首。**composite=0.871**
- **估值/质量**：trailingPE 25.0 / forwardPE 22.7；profitMargins 28.0%；股息率 0.95%；beta 0.36
- **投资逻辑**：交易所+数据+清算三元、监管事件型现金流；因子层面无量价背离、趋势平稳、低 beta 防御；risk-off 期可受益于波动率。**但当日 −2.96%，需看是否为独立利空而非系统性。**
- **风险提示**：依赖交易量/波动率周期；VIX 高位或抑制成交；监管与费率风险；本因子非基本面；**无法核实当日下跌原因**；未验证未来收益。

### 2. WST — West Pharmaceutical Services（西方制药服务）
- **股票代码** WST · **板块** Healthcare · **市值** $26.0B · **综合评分** 8.4
- **匹配 WorldQuant 因子**：**Alpha#19**（p=0.998，F19≈−0.004）+ **Alpha#41**（p=0.998，+1.948）
- **因子信号解读**：极度平稳日内 + 动量平滑（Alpha#1 p=0.893）+ 量价背离向优（#12 p=0.988）；**当日 −4.07%、量/均量 1.47**（放量下跌但区间仍平稳）。**composite=0.818**
- **估值/质量**：trailingPE 41.9 / forwardPE 35.9；profitMargins 18.8%；股息率 0.27%；beta 1.14
- **投资逻辑**：注射容器/服务 + 医疗耗材刚性需求 + CDMO 受益；因子层面无破位 + 趋势平稳。**但估值偏高、当日放量下跌。**
- **风险提示**：高 PE；当日 −4.07% 放量；**原因未核实**；制药资本开支/监管；非基本面筛选。

### 3. COST — Costco Wholesale（好市多）
- **股票代码** COST · **板块** Consumer Defensive · **市值** $481.6B · **综合评分** 8.2
- **匹配 WorldQuant 因子**：**Alpha#41**（p=0.996，+1.756）+ **Alpha#53 反转**（p=0.992，+16.689）
- **因子信号解读**：趋势平稳 + 日内强度近 9 日**回落→反转** + 量价背离向优（#12 p=0.903）+ 动量平滑（#6 p=0.863、#30 p=0.990）。当日 −0.45%。**composite=0.801**
- **估值/质量**：trailingPE 52.4 / forwardPE 43.4；profitMargins 3.0%（低毛利会员制）；股息率 0.54%；beta 0.85
- **投资逻辑**：会员制稳健现金流、薄利多销、防御属性 + 全球规模；risk-off 期相对抗跌；因子无破位 + 反转修复。
- **风险提示**：**高估值（PE 52）**；低利润率；消费降级/汇率；动量 #1 偏弱；非基本面。

### 4. LH — Labcorp Holdings（实验室考检集团）
- **股票代码** LH · **板块** Healthcare · **市值** $30.0B · **综合评分** 8.0
- **匹配 WorldQuant 因子**：**Alpha#19**（p=0.994，F19≈−0.008）+ **Alpha#41**（p=0.982，+0.546）
- **因子信号解读**：平稳日内 + 反转修复（#53 p=0.978）+ 量价背离向优（#12 p=0.942）；唯动量 #1 p=0.024 弱（近期整体偏弱）。当日 −1.90%。**composite=0.780**
- **估值/质量**：trailingPE 30.2 / forwardPE 18.8；profitMargins 6.9%；股息率 0.77%；beta 0.83
- **投资逻辑**：诊断/医疗考检刚性需求 + 医保支付；forwardPE 较 trailing 下移；因子平稳 + 反转 + 无背离。
- **风险提示**：近期动量弱（#1 p=0.024）；医保费率/集中度；利润率薄；非基本面；**近期事件未核实**。

### 5. JNJ — Johnson & Johnson（强生）
- **股票代码** JNJ · **板块** Healthcare · **市值** $659.5B · **综合评分** 8.0
- **匹配 WorldQuant 因子**：**Alpha#41**（p=0.992，+0.890）+ **Alpha#53**（p=0.990，+11.107）
- **因子信号解读**：平稳趋势 + 反转修复 + 无背离（#12 p=0.825、#19 p=0.986）；动量平滑 #1 p=0.688；**beta 仅 0.20**。当日 −0.91%。**composite=0.774**
- **估值/质量**：trailingPE 42.0 / forwardPE 23.6；profitMargins 16.2%；股息率 1.94%；beta 0.2
- **投资逻辑**：医疗+制药双引擎 + 高分红 + 极低 beta 防御；risk-off 期稳健；因子无破位 + 反转。
- **风险提示**：trailingPE 42（forward 更低）；制药诉讼/专利悬崖；前列腺等产品风险；非基本面。

### 6. VRSK — Verisk Analytics（Verisk 分析）
- **股票代码** VRSK · **板块** Industrials · **市值** $26.3B · **综合评分** 7.9
- **匹配 WorldQuant 因子**：**Alpha#53 反转**（p=0.996，+55.834）+ **Alpha#41**（p=0.984，+0.563）
- **因子信号解读**：近 9 日日内强度显著回落→强反转 + 平稳趋势 + 无背离（#19 p=0.942、#6 p=0.879、#30 p=0.873）；动量 #1 p=0.332。当日 +0.39%。**composite=0.767**
- **估值/质量**：trailingPE 30.9 / forwardPE 23.5；profitMargins 27.7%；股息率 0.98%；beta 0.67
- **投资逻辑**：保险/风险数据订阅、高转换成本、高利润率、经常性收入；因子反转 + 平稳 + 无背离。
- **风险提示**：PE 31；经济周期（保险/理赔）；**#53 强反转可能已修复**；非基本面。

### 7. VTR — Ventas（文泰斯）
- **股票代码** VTR · **板块** Real Estate · **市值** $46.2B · **综合评分** 7.9
- **匹配 WorldQuant 因子**：**Alpha#19**（p=0.980，F19≈−0.022）+ **Alpha#53 反转**（p=0.968，+0.612）
- **因子信号解读**：平稳日内 + 反转 + 强动量平滑（#1 p=0.960）；**高估值**。当日 +0.22%。**composite=0.764**
- **估值/质量**：trailingPE 168.0 / forwardPE 138.7；profitMargins 3.9%；股息率 2.39%；beta 0.77
- **投资逻辑**：医疗 REIT（三级护理/医院）+ 高分红 + 防御地产；risk-off 期相对稳健；因子强。
- **风险提示**：**估值极高（PE 168）**；利率敏感（REIT）；运营者风险；非基本面；REIT 分红可变。

### 8. SOLV — Solventum（Solventum 制药）
- **股票代码** SOLV · **板块** Healthcare · **市值** $14.8B · **综合评分** 7.9
- **匹配 WorldQuant 因子**：**Alpha#53 反转**（p=0.933，+0.029）+ **Alpha#6 开盘-量**（p=0.867，+0.293）
- **因子信号解读**：反转 + 开盘-量相关 + 无背离（#12 p=0.702、#19 p=0.853、#30 p=0.817）；**低毛利、高 PE(trailing)**；当日 −1.13%。**composite=0.764**
- **估值/质量**：trailingPE 97.9 / **forwardPE 11.5**；profitMargins 1.9%；股息率 0%；beta 0.75
- **投资逻辑**：从 3M 分拆的医疗耗材（敷料/粘合剂/注射器）；**forwardPE 远低于 trailing→预期盈利大幅改善**；因子反转。
- **风险提示**：近期盈利低、trailingPE 极高；forward 依赖指引兑现；无股息；非基本面；**盈利改善未核实**。

### 9. ES — Eversource Energy（Eversource 能源）
- **股票代码** ES · **板块** Utilities · **市值** $27.3B · **综合评分** 7.8
- **匹配 WorldQuant 因子**：**Alpha#53 反转**（p=0.998，+83.320）+ **Alpha#41**（p=0.956，+0.137）
- **因子信号解读**：近 9 日日内强度大幅回落→极强反转 + 平稳 + 无背离（#6 p=0.924、#19 p=0.944、#30 p=0.708）；动量 #1 p=0.209 弱。当日 −0.15%。**composite=0.750**
- **估值/质量**：trailingPE 19.1 / forwardPE 14.7；profitMargins 10.4%；**股息率 4.34%**；beta 0.66
- **投资逻辑**：受监管电力+天然气公用事业 + 高股息 + 低 beta；防御板块轮动；因子强反转。
- **风险提示**：**#53 极强反转可能已修复**；利率敏感；监管费率；动量弱；非基本面。

### 10. CCI — Crown Castle（皇冠城堡通信）
- **股票代码** CCI · **板块** Real Estate · **市值** $35.6B · **综合评分** 7.7
- **匹配 WorldQuant 因子**：**Alpha#53 反转**（p=0.982，+1.501）+ **Alpha#41**（p=0.936，+0.072）
- **因子信号解读**：反转 + 平稳 + 动量平滑（#1 p=0.877、#6 p=0.700）；**最高股息**；当日 +1.11%。**composite=0.749**
- **估值/质量**：trailingPE 33.6 / forwardPE 28.6；profitMargins 20.1%；**股息率 5.14%**；beta 0.91
- **投资逻辑**：通信塔/室内分布 REIT + 5G/小基站需求 + 高分红 + 利润率高；防御 + 收益。
- **风险提示**：利率敏感（REIT，beta 0.91）；运营商资本开支；PE 34；非基本面。

### 11. AES — The AES Corporation（AES 公司）
- **股票代码** AES · **板块** Utilities · **市值** $10.7B · **综合评分** 7.7
- **匹配 WorldQuant 因子**：**Alpha#1 动量**（p=0.982，F1=0.922）+ **Alpha#19 均值回复**（p=0.917，F19≈−0.086）
- **因子信号解读**：最强平滑趋势 + 无均值回复压力 + 开盘-量（#6 p=0.907）；**Alpha#53 退化 NaN**（不计入）；**无背离**；**最小规模入选**。当日 0.00%。**composite=0.745（6 因子）**
- **估值/质量**：trailingPE 6.0 / forwardPE 6.3；profitMargins 13.2%；股息率 1.7%；beta 0.92
- **投资逻辑**：发电/储能 + 低估值 + 因子极平滑 + 无破位；仅 6 因子可用。
- **风险提示**：**Alpha#53 无数据**；最小市值（$10.7B）；海外/汇率/监管/债务；低 PE 可能反映风险；非基本面。

### 12. RSG — Republic Services（共和服务集团）
- **股票代码** RSG · **板块** Industrials · **市值** $77.4B · **综合评分** 7.7
- **匹配 WorldQuant 因子**：**Alpha#53 反转**（p=0.962，+0.466）+ **Alpha#30 波动/量结构**（p=0.855，F30≈−8.4e5）
- **因子信号解读**：反转 + 量能结构良好 + 无背离（#12 p=0.802、#19 p=0.712、#41 p=0.791）；**beta 仅 0.32**。当日 +0.80%。**composite=0.742**
- **估值/质量**：trailingPE 35.2 / forwardPE 31.7；profitMargins 12.9%；股息率 1.06%；beta 0.32
- **投资逻辑**：固废/环保服务 + 经常性收入 + 低 beta + 防御；因子反转 + 结构良好。
- **风险提示**：PE 35；燃料/运输成本；环保监管；非基本面。

### 13. TGT — Target（塔吉特）
- **股票代码** TGT · **板块** Consumer Defensive · **市值** $78.0B · **综合评分** 7.6
- **匹配 WorldQuant 因子**：**Alpha#19**（p=0.984，F19≈−0.018）+ **Alpha#41**（p=0.972，+0.259）
- **因子信号解读**：平稳日内 + 趋势 + 无背离（#12 p=0.875、#1 p=0.684、#6 p=0.650、#30 p=0.809）；**Alpha#53 p=0.150 偏弱**。当日 −2.18%。**composite=0.732**
- **估值/质量**：trailingPE 16.0 / forwardPE 17.6；profitMargins 4.5%；股息率 2.64%；beta 0.93
- **投资逻辑**：价值零售 + 股息 + 防御消费；PE 合理；因子平稳。
- **风险提示**：**当日 −2.18%**（原因未核实）；消费降级；库存/毛利；#53 弱；非基本面。

### 14. CVS — CVS Health（CVS 健康）
- **股票代码** CVS · **板块** Healthcare · **市值** $103.7B · **综合评分** 7.5
- **匹配 WorldQuant 因子**：**Alpha#1 动量**（p=0.984，F1=0.923）+ **Alpha#53 反转**（p=0.974，+0.946）
- **因子信号解读**：强平滑动量 + 反转 + 平稳（#19 p=0.748、#41 p=0.924）；**薄利**；当日 +0.46%。**composite=0.722**
- **估值/质量**：trailingPE 9.4 / forwardPE 9.3；profitMargins 2.6%；**股息率 3.30%**；beta 0.58
- **投资逻辑**：药房+保险+PBM 三元 + 低 PE + 高股息 + 低 beta；因子动量 + 反转。
- **风险提示**：薄利润率；PBM 监管/药价压力；医保风险；非基本面。

### 15. HRL — Hormel Foods（荷美尔食品）
- **股票代码** HRL · **板块** Consumer Defensive · **市值** $12.7B · **综合评分** 7.5
- **匹配 WorldQuant 因子**：**Alpha#6 开盘-量**（p=0.988，F6=0.678）+ **Alpha#19 均值回复**（p=0.970，F19≈−0.032）
- **因子信号解读**：开盘-量强相关 + 平稳 + 无背离（#1 p=0.777、#41 p=0.903、#12 p=0.573）；**Alpha#53 p=0.366 偏弱**；**高分红**。当日 −0.77%。**composite=0.719**
- **估值/质量**：trailingPE 37.2 / forwardPE 14.7；profitMargins 2.8%；**股息率 5.07%**；beta 0.26
- **投资逻辑**：包装食品 + 高股息 + 极低 beta + 防御；forwardPE 远低于 trailing；因子平稳 + 开盘-量。
- **风险提示**：**trailingPE 37（forward 14.7）需盈利改善兑现**；薄利润率；原料/通胀；#53 弱；非基本面。

### 16. XEL — Xcel Energy（伊克赛尔能源）
- **股票代码** XEL · **板块** Utilities · **市值** $52.1B · **综合评分** 7.4
- **匹配 WorldQuant 因子**：**Alpha#6 开盘-量**（p=0.978，F6=0.561）+ **Alpha#19 均值回复**（p=0.883，F19≈−0.119）
- **因子信号解读**：开盘-量 + 平稳 + 无背离（#1 p=0.513、#41 p=0.861、#30 p=0.340、#53 p=0.832）；**低 vol**。当日 +0.36%。**composite=0.715**
- **估值/质量**：trailingPE 18.9 / forwardPE 17.8；profitMargins 17.9%；**股息率 2.93%**；beta 0.34
- **投资逻辑**：受监管电力公用事业 + 清洁能源转型 + 高分红 + 极低 beta；防御轮动。
- **风险提示**：利率敏感；监管费率；资本开支；非基本面。

### 17. VYLR — Vylor（Vylor 金融）
- **股票代码** VYLR · **板块** Financial Services · **市值** $46.4B · **综合评分** 7.4
- **匹配 WorldQuant 因子**：**Alpha#1 动量**（p=0.915，F1=0.869）+ **Alpha#53 反转**（p=0.911，F53≈−0.103）
- **因子信号解读**：强平滑动量 + 反转 + 无背离（#6 p=0.696、#12 p=0.686、#19 p=0.654、#30 p=0.392、#41 p=0.751）；**高估值**；当日 +1.31%。**composite=0.715**
- **估值/质量**：trailingPE 347.4 / **forwardPE 26.3**；profitMargins 4.3%；股息率 0.76%；beta 0.60
- **投资逻辑**：因子动量 + 反转最强；**forwardPE 远低于 trailing→盈利改善**。
- **风险提示**：**trailingPE 347 极高，forward 兑现未核实**；薄利润率；**对公司基本面了解有限（非我熟悉的公开大盘名），需独立核实**；非基本面。
- **诚实标注**：VYLR 为 S&P 500 成分股（本环境名单），但**无法联网核实其公开信息**；仅依据 Yahoo 数据。

### 18. ABBV — AbbVie（艾伯维）
- **股票代码** ABBV · **板块** Healthcare · **市值** $520.5B · **综合评分** 7.4
- **匹配 WorldQuant 因子**：**Alpha#19**（p=0.996，F19≈−0.006）+ **Alpha#41**（p=0.994，+1.242）
- **因子信号解读**：极度平稳 + 无背离（#12 p=0.918、#30 p=0.895）+ 低波动；动量 #1 p=0.282 偏弱、#53 p=0.455。当日 −1.93%。**composite=0.714**
- **估值/质量**：trailingPE 50.6 / forwardPE 18.2；profitMargins 15.7%；**股息率 2.30%**；**beta 0.19**；当日 −1.93%
- **投资逻辑**：免疫学/神经科学 + 高利润率 + 高分红 + **极低 beta 0.19**；因子平稳 + 无破位。
- **风险提示**：**trailingPE 50（forward 18）需兑现**；制药专利/诉讼；动量偏弱；非基本面。

### 19. INTU — Intuit（财捷）
- **股票代码** INTU · **板块** Technology · **市值** $71.7B · **综合评分** 7.4
- **匹配 WorldQuant 因子**：**Alpha#41**（p=0.990，+0.643）+ **Alpha#53 反转**（p=0.964，+0.488）
- **因子信号解读**：平稳趋势 + 反转 + 强平滑动量（#1 p=0.936、#12 p=0.950）+ 无背离（#19 p=0.441 中性）；**本期唯一科技**；当日 −2.76%。**composite=0.714**
- **估值/质量**：trailingPE 15.5 / forwardPE 10.5；profitMargins 22.0%；股息率 1.98%；beta 0.92
- **投资逻辑**：TurboTax+QuickBooks+Credit Karma + 高利润率 + 合理估值 + AI 生产力；因子平稳 + 反转；科技但板块轮动下相对抗跌。
- **风险提示**：**科技板块 1 月 −16%**；监管/税务软件竞争/AI 颠覆；**当日 −2.76%**（原因未核实）；非基本面。

### 20. OXY — Occidental Petroleum（西方石油）
- **股票代码** OXY · **板块** Energy · **市值** $53.9B · **综合评分** 7.4
- **匹配 WorldQuant 因子**：**Alpha#53 反转**（p=0.923，F53≈−0.014）+ **Alpha#1 动量**（p=0.905，F1=0.862）
- **因子信号解读**：反转 + 强平滑动量 + 开盘-量（#6 p=0.853、#12 p=0.641、#19 p=0.753、#41 p=0.767）；**低 vol、beta 0.15**；当日 +1.07%。**composite=0.713**
- **估值/质量**：trailingPE 12.0 / forwardPE 10.2；profitMargins 33.0%；**股息率 2.10%**；beta 0.15
- **投资逻辑**：油气+化工 + 高利润率 + 低估值 + **极低 beta 0.15** + 碳捕获/直接空气捕获(DAC) + 因子动量 + 反转。
- **风险提示**：**能源板块 1 月 −12.6%**；油价/地缘/碳政策；碳捕获投资回报；非基本面。

---

## 6. 板块汇总（Top 20）

| 板块 | 入选数 | 代表 | 备注 |
|------|--------|------|------|
| Healthcare（医疗健康） | 6 | WST、LH、JNJ、SOLV、ABBV、CVS | 防御 + 平稳趋势；部分估值偏高 |
| Consumer Defensive（消费纵深） | 3 | COST、TGT、HRL | risk-off 防御 + 低 beta；COST 高 PE |
| Utilities（公用事业） | 3 | ES、AES、XEL | 高分红 + 极低 beta + 反转；AES 最小规模/#53 缺失 |
| Real Estate（地产） | 2 | VTR、CCI | 医疗 REIT/通信塔 + 高股息；**VTR 估值极高** |
| Financial Services（金融服务） | 2 | CBOE、VYLR | CBOE 低 beta；VYLR 估值极高 + 基本面需核实 |
| Industrials（工业） | 2 | VRSK、RSG | 数据订阅/固废 + 低 beta + 反转 |
| Technology（科技） | 1 | INTU | 唯一科技；板块 1 月最弱但个股平稳 + 合理估值 |
| Energy（能源） | 1 | OXY | 低 vol + 低 beta + 高利润；板块 1 月回调 |

**板块结构**：医疗(6) + 消费纵深(3) + 公用事业(3) + 地产(2) + 金融(2) + 工业(2) + 科技(1) + 能源(1) = 20。**防御倾斜显著**，与 risk-off 盘面 + 低波动因子一致；**不含科技/半导体巨头**。

---

## 7. 方法与局限 / 风险（诚实）

1. **不是投资建议**。纯短期技术面 WQ101 筛选；**未做基本面深度分析、未验证未来收益、未回测**。历史因子强 ≠ 未来收益。
2. **数据来源/时点**：Yahoo Finance Chart API + `yfinance` quoteSummary + S&P500 名单；基准 2026-11-25 收盘；2026-11-26 假期休市；无盘前/盘后；无 intraday VWAP。价格为复权（`auto_adjust=True`）。
3. **本环境无法联网核实事件**：`websearch` = `cancelled`、`get_news` = `YAHOO FINANCE IS CURRENTLY DOWN`。**当日新闻/财报/指引/诉讼/宏观事件未核实**；「近期事件」以量价异动代理。尤其 **CBOE/WST/TGT/INTU 当日下跌原因、SOLV/VYLR/HRL forwardPE 改善、ABBV/VTR 估值**需自行核实。
4. **因子近似**：VWAP≈(H+L+C)/3（canonical 用 intraday）；样本 std ddof=1；退化项 NaN；NaN 因子跳过；用户公式与 canonical WQ101 差异见 §3.1（#1/#6/#19 用用户版本，#6 省略 −1，#19 用用户版本）；**Alpha#30 输出恒 ≤0** 且被 volume 放大，最终再 pct-rank。
5. **因子重叠**：F19↔F41 ≈0.92；有效独立维度 ~5；偏「平稳+无破位」。**F12 raw 未按价格归一**（canonical 如此）。
6. **打分自定义**：等权 percentile composite；**估值/质量/事件未混入**；非 WorldQuant 商业回测管线。高分=强因子，非买入信号。
7. **结果偏防御/低波**：本快照 risk-off + 低波因子 → 医疗/纵深/公用事业/地产；**科技/半导体虽基本面强未入前 20**。不同窗口/因子权重结果会变。
8. **市值**：Yahoo `marketCap` 快照，过滤 >$10B；**AES $10.7B 最小**；未核实股本变动。
9. **估值口径**：trailingPE/forwardPE/profitMargins/dividendYield 为 Yahoo 快照，可能混合 TTM/forward；**SOLV/VYLR/HRL/ABBV/VTR/COST trailing 极高但 forward 低**需看盈利改善；**AES PE 6 / OXY 12 / CVS 9.4 低 PE 可能反映风险**。
10. **VYLR/SOLV 等**：在本环境名单中，但**无法联网核实公开信息**，需独立核实。
11. **组合构建缺失**：未考虑相关性、行业中性、仓位、止损、流动性（均为大盘）、税费、分红再投；板块集中（医疗 6 + 防御）需分散。
12. **同系列既往**：见 [[wq101-alpha-daily]]（历史各日）；本期为**公式级计算**版本，与既往「结构性代理」口径不同，**排名不可直接横向比较**。

---

## 8. 数据核查 / Data Provenance

- **行情**：Yahoo Finance `v8/finance/chart/{symbol}?interval=1d&period=3mo&auto_adjust=true`（503 S&P500；65 交易日）；指数 `^GSPC ^IXIC ^DJI ^VIX ^RUT`；板块 11 ETF（XLK/XLF/XLE/XLV/XLY/XLP/XLI/XLB/XLU/XLRE/XLC）。
- **基本面/市值**：`yfinance.Ticker.fast_info['marketCap']` + `.get_info()`（sector、industry、longName、trailingPE、forwardPE、priceToBook、profitMargins、dividendYield、beta、fiftyTwoWeekHigh/Low、returnOnEquity、revenueGrowth、earningsGrowth、freeCashflow、debtToEquity）。
- **成分股**：Wikipedia `List_of_S%26P_500_companies`（503；symbol `.`→`-`）。
- **因子计算**：本环境 Python 3.14 + pandas + numpy + yfinance；**可复现**（相同数据窗口同结果）；逐股原始因子与 pct-rank 见 §4/§5 与临时 CSV（未入 wiki，可重跑）。
- **交叉核验**：对 COST 抽样手工复算 Alpha#1/#6/#12/#41/#53 与脚本输出一致（a1 0.4576、a6 0.2708、a12 4.8999、a41 1.7558、a53 16.6889）。
- **新闻/事件**：不可用（见 §7-3）。
- **不构成投资建议**。市场数据随时变动；请以官方来源复核。

## 9. 相关

- [[wq101-alpha-daily]] · [[investment-daily]] · [[overview]]
- WorldQuant 101 Alphas（#1, #6, #12, #19, #30, #41, #53）；本文按用户给定公式实现，与 canonical 差异见 §3.1。
