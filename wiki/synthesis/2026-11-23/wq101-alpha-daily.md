---
title: WorldQuant 101 Alpha 美股 Top 20 精选 — 2026-11-23
type: synthesis
created: 2026-11-23
updated: 2026-11-23
sources: [investment-daily.md, yahoo-finance]
tags: [wq101-alpha-daily, worldquant, alphas, factor-investing, momentum, reversal, volatility, volume-price, mean-reversion, trend, us-equities, large-cap, daily-digest]
---

# WorldQuant 101 Alpha 美股 Top 20 精选 — 2026-11-23

> 数据基准：Yahoo Finance `v8/finance/chart`（interval=1d, range=1mo）日线 OHLCV；市值为 Yahoo 报价页 Market Cap（intraday）；个股常规收盘基准 Nov 20；本报告生成于 Nov 23（Yahoo 显示当前为 U.S. markets closed 休市快照）。因子为横截面代理值，非公式回测；**不构成投资建议**。

---

## 1. 市场概览（美股实时快照，截至 Nov 20 常规收盘 + 隔夜/盘后）

| 指数 | 收盘/快照 | 涨跌幅 |
|------|-----------|--------|
| S&P 500 (^GSPC) | 6,910.39（常规收盘 Nov 20） | −3.70% |
| S&P Futures | 7,093.00 | +2.28% |
| Dow Futures | 49,000.00 | +1.63% |
| Nasdaq Futures | 25,890.50 | +3.04% |
| Russell 2000 Futures | 2,637.50 | +1.94% |
| VIX (^VIX) | 35.89 | +26.20% |
| 10-Year Treasury (^TNX) | 4.9120 | −2.77% |
| Gold | 3,606.30 | +2.59% |
| Bitcoin USD | 61,188.43 | +3.31% |

→ Yahoo 显示当前为 U.S. markets closed（休市快照）；futures 快照显示后市温和反弹（S&P +2.28%、Nasdaq +3.04%）；AI/半导体链条整体承压，VIX 波动加剧，贵金属与比特币明显强于股指。

---

## 2. 方法与评分公式

**候选池**：市值 > $10B 美股（本窗口挑出 22 只候选：Most Active 活跃榜 + 财经报价页筛选；最小值 FSLR $14.788B，全部满足 > $10B 门槛）。

**因子定义**（横截面代理，Pearson 相关系数记 r；X = ((C−L)−(H−C))/(C−L)）：

| Alpha | 公式 | 正 = |
|-------|------|------|
| #1 动量 | pearson(C[t−1], C[t], 10) | 近 10 日价格环比正相关（r > 0，动量存在） |
| #6 开盘-量 | pearson(open, volume, 10) | 开盘价与成交量正相关 |
| #53 反转 | X[t−9] − X[t] | 比率上升（价格向高端移动，回升/反转压力） |
| #30 波动结构 | X[n−1]（当日值） | 收价在区间高端（强势结构）；负 = 收价贴近区间低端 |
| #12 量价背离 | sign(dV[t,1]) × (−dC[t,1]) | 成交量上升 + 价跌同步（资金流入确认） |
| #41 趋势强度 | √(H·L) − (H+L+C)/3（以典型价近似 VWAP） | 价格在典型价上方（趋势强） |
| #19 均值回复 | σ(|C−O|,5) + (C−O) + ρ(C,O,10) | 开盘上方 + 正相关（开盘后回归压力） |

**综合评分**：s = 5 + [+2（a1>0, \|a1\|≥0.3）/ +1（0<a1<0.3）/ −2（a1<0）] + [a6>0: +1 / a6<0: −1] + [a53>0: +2 / −2] + [a12>0: +2 / −2] + [a41>0: +1 / −1] + [a19>0: +1 / −1]；clamp ∈ [1, 10]。

**排名**：综合评分降序；同分（10 分）按信号强度（正因子值之和）排序；Top 20 中最弱两名（诺基亚 NOK、百事可口 PEP）次于 AMD 被排除。

---

## 3. Top 20 排名表

| 排名 | 股票代码 | 公司名称（中英文） | 板块 | 市值 | 综合评分 | 匹配 Alpha 因子 |
|------|----------|-------------------|------|------|----------|-----------------|
| 1 | TSM | Taiwan Semiconductor Manufactur（台积电） | Technology | $1,653,000,000,000 | 10 | Alpha#53、Alpha#12 |
| 2 | MU | Micron Technology, Inc.（美信捷诺） | Technology | $672,642,000,000 | 10 | Alpha#53、Alpha#12、Alpha#41 |
| 3 | AVGO | Broadcom Inc.（博通） | Technology | $1,453,000,000,000 | 10 | Alpha#53、Alpha#12、Alpha#41 |
| 4 | TSLA | Tesla, Inc.（特斯拉） | Consumer Cyclical | $1,367,000,000,000 | 10 | Alpha#53、Alpha#12、Alpha#41 |
| 5 | NVDA | NVIDIA Corporation（英伟达） | Technology | $3,031,000,000,000 | 10 | Alpha#1、Alpha#53 |
| 6 | FSLR | First Solar, Inc.（First Solar） | Technology | $14,788,000,000 | 10 | Alpha#1、Alpha#53 |
| 7 | INTC | Intel Corporation（英特尔） | Technology | $272,553,000,000 | 10 | Alpha#1、Alpha#53、Alpha#30 |
| 8 | UNH | UnitedHealth Group Incorporated（UnitedHealth） | Healthcare | $304,513,000,000 | 10 | Alpha#1、Alpha#53、Alpha#12、Alpha#19、Alpha#41 |
| 9 | SNDK | Sandisk Corporation（Sandisk） | Technology | $90,200,000,000 | 10 | Alpha#1、Alpha#53、Alpha#12、Alpha#41 |
| 10 | MSFT | Microsoft Corporation（微软） | Technology | $3,598,000,000,000 | 10 | Alpha#1、Alpha#53、Alpha#12 |
| 11 | NU | Nu Holdings Ltd.（Nu） | Financial Services | $54,530,000,000 | 10 | Alpha#53、Alpha#12、Alpha#30 |
| 12 | NFLX | Netflix, Inc.（Netflix） | Communication Services | $232,952,000,000 | 10 | Alpha#1、Alpha#53、Alpha#12 |
| 13 | SOFI | SoFi Technologies, Inc.（SoFi） | Financial Services | $16,197,000,000 | 10 | Alpha#1、Alpha#53、Alpha#12 |
| 14 | AMD | Advanced Micro Devices, Inc.（超威） | Technology | $702,393,000,000 | 8 | Alpha#53、Alpha#41 |
| 15 | AAPL | Apple Inc.（苹果） | Technology | $4,978,000,000,000 | 10 | Alpha#53、Alpha#12 |
| 16 | GRAB | Grab Holdings Limited（Grab） | Industrials | $11,102,000,000 | 10 | Alpha#1、Alpha#53、Alpha#12 |
| 17 | V | Visa Inc.（Visa） | Financial Services | $749,809,000,000 | 10 | Alpha#1、Alpha#53、Alpha#41、Alpha#19 |
| 18 | COST | Costco Wholesale Corporation（Costco） | Consumer Defensive | $1,102,150,000,000 | 10 | Alpha#1、Alpha#53、Alpha#41、Alpha#19 |
| 19 | F | Ford Motor Company（福特） | Consumer Cyclical | $44,604,000,000 | 10 | Alpha#1、Alpha#53、Alpha#30、Alpha#19 |
| 20 | MA | Mastercard Incorporated（Mastercard） | Financial Services | $544,999,000,000 | 10 | Alpha#1、Alpha#53、Alpha#41、Alpha#19 |

---

## 4. 逐股详情（Top 20）

### 1. TSM — Taiwan Semiconductor Manufactur（台积电）
- **股票代码**：TSM · **板块**：Technology · **市值**：$1,653,000,000,000 · **最新**：$318.71（Nov 20）
- **匹配 Alpha 因子**：Alpha#53（反转）、Alpha#12（量价背离）、Alpha#41（趋势强度）
- **因子信号解读**：Alpha#53：正，ΔX≈+108.18（价格向高端移动，回升压力）；Alpha#12：正，≈+33.38（成交量上升 + 价跌同步，资金流入确认）；Alpha#41：正，≈+3.89（趋势强）；Alpha#1：正，r≈0.84（动量强）；Alpha#30：负，X≈−107.88（收价贴近区间低端）。
- **综合评分**：10
- **投资逻辑**：半导体龙头；反转压力 + 量价背离 + 趋势强三项共振，放量跌破本周低后显示筹码流动。
- **风险提示**：AI 需求疑虑与周期顶；今日 −9.48% 放量承压。

### 2. MU — Micron Technology, Inc.（美信捷诺）
- **股票代码**：MU · **板块**：Technology · **市值**：$672,642,000,000 · **最新**：$594.51（Nov 20）
- **匹配 Alpha 因子**：Alpha#53（反转）、Alpha#12（量价背离）、Alpha#41（趋势强度）
- **因子信号解读**：Alpha#12：正强，≈+95.93（成交量大幅上升 + 价跌同步，资金流入确认）；Alpha#41：正，≈+9.47（趋势强）；Alpha#1：正，r≈0.61（动量强）；Alpha#53：正，ΔX≈+7.78；Alpha#19：负，≈−43.59（开盘上方压力）。
- **综合评分**：10
- **投资逻辑**：内存龙头；近期放量跌势中显示强势结构与资金流入，周期低点下的回归压力明显。
- **风险提示**：内存周期顶，缺财报催化；今日 −13.89% 放量。

### 3. AVGO — Broadcom Inc.（博通）
- **股票代码**：AVGO · **板块**：Technology · **市值**：$1,453,000,000,000 · **最新**：$304.41（Nov 20）
- **匹配 Alpha 因子**：Alpha#53（反转）、Alpha#12（量价背离）、Alpha#41（趋势强度）
- **因子信号解读**：Alpha#53：正，ΔX≈+11.15（价格向高端移动）；Alpha#12：正，≈+42.24（资金流入确认）；Alpha#41：正，≈+5.18（趋势强）；Alpha#30：负，X≈−10.39（收价贴近区间低端）。
- **综合评分**：10
- **投资逻辑**：AI/云网络龙头；反转 + 量价 + 趋势共振，NVIDIA 财报传导相对相对安全侧。
- **风险提示**：今日 −12.19%；NVIDIA 利空链传导。

### 4. TSLA — Tesla, Inc.（特斯拉）
- **股票代码**：TSLA · **板块**：Consumer Cyclical · **市值**：$1,367,000,000,000 · **最新**：$345.82（Nov 20）
- **匹配 Alpha 因子**：Alpha#53（反转）、Alpha#12（量价背离）、Alpha#41（趋势强度）
- **因子信号解读**：Alpha#53：正，ΔX≈+18.60（价格向高端移动）；Alpha#12：正，≈+28.59（资金流入确认）；Alpha#41：正，≈+4.12（趋势强）；Alpha#1：正，r≈0.43（动量转弱）；Alpha#30：负，X≈−17.83（结构极弱）。
- **综合评分**：10
- **投资逻辑**：AI 选项空间（Optimus/Jarvis）+ 防守落后；反转压力 + 量价 + 趋势共振。
- **风险提示**：前景分化（SpaceX）+ 结构极弱（X≈−17.8）；估值偏高。

### 5. NVDA — NVIDIA Corporation（英伟达）
- **股票代码**：NVDA · **板块**：Technology · **市值**：$3,031,000,000,000 · **最新**：$125.53（Nov 20）
- **匹配 Alpha 因子**：Alpha#1（动量）、Alpha#53（反转）
- **因子信号解读**：Alpha#1：正，r≈0.91（动量强）；Alpha#53：正，ΔX≈+17.52（价格向高端移动）；Alpha#12：正，≈+20.45（成交量上升 + 价跌同步，资金流入确认）；Alpha#41：正，≈+2.52（趋势强）；Alpha#30：负，X≈−16.67（收价贴近区间低端）。
- **综合评分**：10
- **投资逻辑**：AI 芯片龙头；动量强 + 反转压力 + 量价背离共振，价格从高端回落显示筹码流动。
- **风险提示**：今日 −14.01% 放量承压；AI 需求疑虑与供应链分歧。

### 6. FSLR — First Solar, Inc.（First Solar）
- **股票代码**：FSLR · **板块**：Technology · **市值**：$14,788,000,000 · **最新**：$137.59（Nov 20）
- **匹配 Alpha 因子**：Alpha#1（动量）、Alpha#53（反转）
- **因子信号解读**：Alpha#1：正，r≈0.96（动量强）；Alpha#53：正，ΔX≈+16.36（价格向高端移动）；Alpha#12：正，≈+14.36（资金流入确认）；Alpha#41：正，≈+2.22（趋势强）；Alpha#30：负，X≈−16.77（收价贴近区间低端）。
- **综合评分**：10
- **投资逻辑**：绿能登陆技术龙头；动量强 + 回升压力 + 量价共振。
- **风险提示**：今日 −9.45% 放量；能源行业低谷 + 原材料波动；52Wk Range 136.71–320.95。

### 7. INTC — Intel Corporation（英特尔）
- **股票代码**：INTC · **板块**：Technology · **市值**：$272,553,000,000 · **最新**：$51.28（Nov 20）
- **匹配 Alpha 因子**：Alpha#1（动量）、Alpha#53（反转）、Alpha#30（波动结构）
- **因子信号解读**：Alpha#1：正，r≈0.61（动量强）；Alpha#53：正，ΔX≈+28.70（价格向高端移动）；Alpha#12：正，≈+4.44（资金流入确认）；Alpha#30：负，X≈−27.89（收价贴近区间低端）；Alpha#41：正弱，≈+0.77。
- **综合评分**：10
- **投资逻辑**：AI 芯片补缺角色；动量 + 反转 + 量价配合。
- **风险提示**：结构极弱（X≈−27.9），波动大。

### 8. UNH — UnitedHealth Group Incorporated（UnitedHealth）
- **股票代码**：UNH · **板块**：Healthcare · **市值**：$304,513,000,000 · **最新**：$339.85（Nov 20）
- **匹配 Alpha 因子**：Alpha#1（动量）、Alpha#53（反转）、Alpha#12（量价背离）、Alpha#19（均值回复）、Alpha#41（趋势强度）
- **因子信号解读**：Alpha#1：正，r≈0.86（动量强）；Alpha#53：正，ΔX≈+4.34；Alpha#12：正，≈+9.37（资金流入确认）；Alpha#19：正，≈+16.57（开盘上方压力）；Alpha#41：正弱，≈+0.97；Alpha#30：负，X≈−3.72（收价在区间低端偏下）。
- **综合评分**：10
- **投资逻辑**：医疗保险/健康服务龙头；动量 + 量价 + 均值回复 + 轻度趋势共振。
- **风险提示**：医疗政策 + 防御属性；X 负值显示结构仍在低位。

### 9. SNDK — Sandisk Corporation（Sandisk）
- **股票代码**：SNDK · **板块**：Technology · **市值**：$90,200,000,000 · **最新**：$79.24（Nov 20）
- **匹配 Alpha 因子**：Alpha#1（动量）、Alpha#53（反转）、Alpha#12（量价背离）、Alpha#41（趋势强度）
- **因子信号解读**：Alpha#1：正，r≈0.75（动量强）；Alpha#53：正，ΔX≈+11.23（价格向高端移动）；Alpha#12：正，≈+15.16（资金流入确认）；Alpha#41：正，≈+1.51（趋势强）；Alpha#30：负，X≈−10.55（收价贴近区间低端）。
- **综合评分**：10
- **投资逻辑**：存储龙头（NVMe/SSD）；动量 + 反转 + 量价 + 趋势共振。
- **风险提示**：今日 −16.06% 放量；存储周期波动。

### 10. MSFT — Microsoft Corporation（微软）
- **股票代码**：MSFT · **板块**：Technology · **市值**：$3,598,000,000,000 · **最新**：$484.52（Nov 20）
- **匹配 Alpha 因子**：Alpha#1（动量）、Alpha#53（反转）、Alpha#12（量价背离）
- **因子信号解读**：Alpha#1：正，r≈0.85（动量强）；Alpha#53：正，ΔX≈+5.05（价格向高端移动）；Alpha#12：正，≈+13.78（资金流入确认）；Alpha#41：正，≈+2.50（趋势强）；Alpha#30：负，X≈−4.52（收价在区间低端偏下）。
- **综合评分**：10
- **投资逻辑**：Azure/AI 基建龙头，确定性最高，动量 + 量价 + 趋势共振。
- **风险提示**：NVIDIA 利空链传导；估值 PE 25.29 偏高。

### 11. NU — Nu Holdings Ltd.（Nu）
- **股票代码**：NU · **板块**：Financial Services · **市值**：$54,530,000,000 · **最新**：$11.27（Nov 20）
- **匹配 Alpha 因子**：Alpha#53（反转）、Alpha#12（量价背离）、Alpha#30（波动结构）
- **因子信号解读**：Alpha#53：正，ΔX≈+18.17（价格向高端移动）；Alpha#12：正，≈+0.55（资金流入确认）；Alpha#19：正弱，≈+0.29；Alpha#30：负，X≈−17.29（收价贴近区间低端）；Alpha#1：弱正，r≈0.23。
- **综合评分**：10
- **投资逻辑**：金融科技，回升压力 + 轻度量价；结构弱。
- **风险提示**：今日 −4.65% 承压；金融环境决定性。

### 12. NFLX — Netflix, Inc.（Netflix）
- **股票代码**：NFLX · **板块**：Communication Services · **市值**：$232,952,000,000 · **最新**：$56.73（Nov 20）
- **匹配 Alpha 因子**：Alpha#1（动量）、Alpha#53（反转）、Alpha#12（量价背离）
- **因子信号解读**：Alpha#1：正，r≈0.92（动量强）；Alpha#53：正，ΔX≈+15.23（价格向高端移动）；Alpha#12：正，≈+1.73（资金流入确认）；Alpha#30：负，X≈−14.41（收价贴近区间低端）；Alpha#41：正弱，≈+0.39。
- **综合评分**：10
- **投资逻辑**：流媒体基础设施；动量强 + 反转压力，结构轻。
- **风险提示**：防守阵地指数（Tencent、Xiaomi、Baidu）下行阶段；今日 −2.96% 承压。

### 13. SOFI — SoFi Technologies, Inc.（SoFi）
- **股票代码**：SOFI · **板块**：Financial Services · **市值**：$16,197,000,000 · **最新**：$12.48（Nov 20）
- **匹配 Alpha 因子**：Alpha#1（动量）、Alpha#53（反转）、Alpha#12（量价背离）
- **因子信号解读**：Alpha#1：正，r≈0.97（动量强）；Alpha#53：正，ΔX≈+15.38（价格向高端移动）；Alpha#12：正，≈+1.05（资金流入确认）；Alpha#19：正弱，≈+0.50；Alpha#30：负，X≈−14.86（收价贴近区间低端）。
- **综合评分**：10
- **投资逻辑**：金融生态/算力租赁；动量强 + 回升压力共振，结构弱。
- **风险提示**：算力/AI 交易萎缩风险；市值小但 ≥ $10B。

### 14. AMD — Advanced Micro Devices, Inc.（超威）
- **股票代码**：AMD · **板块**：Technology · **市值**：$702,393,000,000 · **最新**：$424.39（Nov 20）
- **匹配 Alpha 因子**：Alpha#53（反转）、Alpha#41（趋势强度）
- **因子信号解读**：Alpha#53：正，ΔX≈+8.79（价格向高端移动）；Alpha#41：正，≈+6.58（趋势强）；Alpha#1：正，r≈0.44（动量转弱）；Alpha#12：负，≈−64.8（价跌伴成交量下降，流出压力）；Alpha#19：负，≈−23.45；Alpha#30：负，X≈−7.95（收价贴近区间低端）。
- **综合评分**：8
- **投资逻辑**：AI 芯片增长股；回升压力 + 趋势强，但近 1 日价跌量缩与结构弱。
- **风险提示**：PE 90.73 极高（估值分化，仅次 NVDA）；今日 −13.25% 放量承压。

### 15. AAPL — Apple Inc.（苹果）
- **股票代码**：AAPL · **板块**：Technology · **市值**：$4,978,000,000,000 · **最新**：$342.56（Nov 20）
- **匹配 Alpha 因子**：Alpha#53（反转）、Alpha#12（量价背离）
- **因子信号解读**：Alpha#53：正，ΔX≈+5.61（价格向高端移动）；Alpha#12：正，≈+6.65（资金流入确认）；Alpha#41：正，≈+1.56（趋势强）；Alpha#30：负，X≈−4.89（收价在区间低端偏下）；Alpha#1：正弱，r≈0.35。
- **综合评分**：10
- **投资逻辑**：防守 + 成长双轮，回升压力与量价背离共振，结构相对温和。
- **风险提示**：AI 链条承压 + 防御属性；今日 −1.90%。

### 16. GRAB — Grab Holdings Limited（Grab）
- **股票代码**：GRAB · **板块**：Industrials · **市值**：$11,102,000,000 · **最新**：$2.75（Nov 20）
- **匹配 Alpha 因子**：Alpha#1（动量）、Alpha#53（反转）、Alpha#12（量价背离）
- **因子信号解读**：Alpha#1：正，r≈0.95（动量强）；Alpha#53：正，ΔX≈+13.0（价格向高端移动）；Alpha#12：正，≈+0.18（资金流入确认）；Alpha#30：负，X≈−13.0（收价贴近区间低端）。
- **综合评分**：10
- **投资逻辑**：平台/物流（区域）；动量强 + 回升压力共振。
- **风险提示**：区域/监管风险；结构弱。

### 17. V — Visa Inc.（Visa）
- **股票代码**：V · **板块**：Financial Services · **市值**：$749,809,000,000 · **最新**：$401.87（Nov 20）
- **匹配 Alpha 因子**：Alpha#1（动量）、Alpha#53（反转）、Alpha#41（趋势强度）、Alpha#19（均值回复）
- **因子信号解读**：Alpha#1：正，r≈0.79（动量强）；Alpha#53：正，ΔX≈+9.14（价格向高端移动）；Alpha#41：正，≈+1.01（趋势强）；Alpha#19：正，≈+2.50（开盘上方压力）；Alpha#30：负，X≈−9.10（收价贴近区间低端）。
- **综合评分**：10
- **投资逻辑**：支付基础设施；动量 + 回升 + 趋势，结构相对温和。
- **风险提示**：卡网络需求温和；防守属性；X 小值。

### 18. COST — Costco Wholesale Corporation（Costco）
- **股票代码**：COST · **板块**：Consumer Defensive · **市值**：$1,102,150,000,000 · **最新**：$1,102.15（Nov 20）
- **匹配 Alpha 因子**：Alpha#1（动量）、Alpha#53（反转）、Alpha#41（趋势强度）、Alpha#19（均值回复）
- **因子信号解读**：Alpha#1：正，r≈0.87（动量强）；Alpha#53：正，ΔX≈+5.61（价格向高端移动）；Alpha#41：正，≈+2.77（趋势强）；Alpha#19：正，≈+4.06（开盘上方压力）；Alpha#12：负，≈−8.32（价涨伴成交量上升，流出压力）；Alpha#30：负，X≈−4.68（收价在区间低端偏下）。
- **综合评分**：10
- **投资逻辑**：零售巨头；动量强 + 回升 + 趋势 + 均值回复共振。
- **风险提示**：估值（P/E）高；季度财报数据波动；非自动化交易建议。

### 19. F — Ford Motor Company（福特）
- **股票代码**：F · **板块**：Consumer Cyclical · **市值**：$44,604,000,000 · **最新**：$11.17（Nov 20）
- **匹配 Alpha 因子**：Alpha#1（动量）、Alpha#53（反转）、Alpha#30（波动结构）、Alpha#19（均值回复）
- **因子信号解读**：Alpha#1：正，r≈0.95（动量强）；Alpha#53：正，ΔX≈+9.79（价格向高端移动）；Alpha#19：正，≈+0.99（开盘上方压力）；Alpha#30：负，X≈−11.50（收价贴近区间低端）。
- **综合评分**：10
- **投资逻辑**：美国 OEM 龙头；动量 + 回升，均值回复压力。
- **风险提示**：经济周期 + 大宗商品/汽车业贸易；结构弱。

### 20. MA — Mastercard Incorporated（Mastercard）
- **股票代码**：MA · **板块**：Financial Services · **市值**：$544,999,000,000 · **最新**：$625.59（Nov 20）
- **匹配 Alpha 因子**：Alpha#1（动量）、Alpha#53（反转）、Alpha#41（趋势强度）、Alpha#19（均值回复）
- **因子信号解读**：Alpha#1：正，r≈0.79（动量强）；Alpha#53：正，ΔX≈+7.07（价格向高端移动）；Alpha#41：正，≈+1.63（趋势强）；Alpha#19：正，≈+1.68（开盘上方压力）；Alpha#30：负，X≈−6.73（收价贴近区间低端）。
- **综合评分**：10
- **投资逻辑**：支付网络（V 兄弟）；动量 + 回升 + 趋势 + 均值回复共振。
- **风险提示**：相对安全但缺 AI 弹性（V 强于此）；X 小值。

---

## 5. 板块分类汇总（Top 20）

### Technology（技术/科技）— 10 只
TSM、MU、AVGO、NVDA、FSLR、INTC、SNDK、MSFT、AMD、AAPL

### Consumer Cyclical（可选消费）— 2 只
TSLA、F

### Healthcare（医疗保健）— 1 只
UNH

### Communication Services（通信服务）— 1 只
NFLX

### Financial Services（金融服务）— 4 只
NU、SOFI、V、MA

### Industrials（工业/工业制品）— 1 只
GRAB

### Consumer Defensive（必需消费/防御）— 1 只
COST

板块分布：Technology 50%、Financial Services 20%、Consumer Cyclical 10%、Communication Services 5%、Consumer Defensive 5%、Industrials 5%、Healthcare 5%。

---

## 6. 免责声明

因子为横截面代理值（非公式回测）；数据基准为 Yahoo Finance 快照；市值为 Yahoo 报价页 Market Cap；整体不构成投资建议；非自动化交易建议；实际交易前请核实最新报价与财务基本面。
