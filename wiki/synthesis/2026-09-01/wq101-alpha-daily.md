---
title: WorldQuant 101 Alpha 因子选股日报 — 2026-09-01
type: synthesis
created: 2026-09-01
updated: 2026-09-01
sources: []
tags: [quant, worldquant-101, alpha-factors, us-stock-picks, daily-report]
---

# WorldQuant 101 Alpha 因子选股日报 — 2026-09-01

> 基于 WorldQuant 101 Alpha 因子库，对美股中大盘股（市值 > $10B）进行量化筛选，精选 Top 20 最值得投资的标的。

## 市场背景

| 指数 | 收盘价（8/31） | 日涨跌 | 8月涨跌 | 关键信号 |
|------|--------|--------|--------|----------|
| S&P 500 | 7,686.14 | -0.33% | +2.62% | 8月收涨，9月"魔咒"季节压力 |
| Nasdaq Composite | 26,370.89 | -0.12% | +3.93% | AI 交易主线仍在，8月表现最佳 |
| Dow Jones | 53,185.90 | -0.70% | +1.34% | 连续5个月收涨（16个月中15个月收红） |
| Russell 2000 | 2,956.45 | -0.54% | — | 小盘/高贝塔资金撤退 |
| Brent / WTI | ~$90.49 / ~$85.76 | +2.7% / +2.8% | +1.3% | 美伊冲突升级，油价重返90+ |

**核心驱动因素：**
1. **美伊冲突再度升级**：美方攻击霍尔木兹海峡的伊朗火箭发射装置，伊方反击阿联酋/约旦，布伦特原油单日 +2.7% 突破 $90，10年期美债收益率升至 4.75%（2025年1月来最高）
2. **Fed 鹰派 + 9月加息预期**：主席 Warsh Jackson Hole 讲话偏鹰，CME FedWatch 显示 9/16 加息 25bp 概率 ~66%；若 9 月未加息可能引发剧烈反应
3. **板块轮动显著**：Energy 独领涨（SLB +4.83% / XOM +2.71% / CVX +2.12%），Healthcare"Heating-Up"，Communication Services / Consumer Discretionary 走强，Technology / Utilities 走弱（XLK -1.55% / XLU -1.04%）
4. **AI 主线分化**：五大平台股集体守住（AMZN +3.97% / MSFT +1.68% / AAPL +1.63% / GOOGL +1.53% / META +1.21%），但 AI 硬件链承压（MRVL -10.28% / ARM -6.33%），NVDA 财报后回撤至 ~$217
5. **关键事件**：周五（9/4）非农就业、9/11 CPI、9/16 FOMC 利率决议

## 因子框架与评分方法

基于 WorldQuant 101 Alpha 因子库中的 6 类核心因子，对每只股票进行定性因子信号评估：

| 因子编号 | 因子名称 | 计算逻辑（简化） | 信号方向 |
|----------|----------|------------------|----------|
| Alpha#1 | 动量 | Rank(Correlation(Delay(close,1), close, 10)) | 正 = 上涨趋势延续 |
| Alpha#6 | 量价相关 | Correlation(open, volume, 10) | 正 = 量价齐升 |
| Alpha#12 | 量价背离 | sign(delta(volume,1)) × (-1 × delta(close,1)) | 正 = 缩量下跌（反转信号） |
| Alpha#19 | 均值回复 | -1 × rank(stddev(abs(close-open),5) + (close-open) + rank(correlation(close,open,10))) | 正 = 波动收敛 + 回归均值 |
| Alpha#30 | 波动率 | (-1 × rank(...delta(close,3)...)) × sum(volume,5) | 正 = 低波动 + 放量 |
| Alpha#41 | 趋势强度 | ((high × low)^0.5) - vwap | 正 = 价格高于 VWAP |
| Alpha#53 | 反转 | -1 × Delta(((close-low)-(high-close))/(close-low), 9) | 正 = 近期超跌后反转 |

**综合评分方法：** 对每只股票评估其在上述因子维度的信号强度，加权计算综合得分（1-10分），权重为：动量 25%、量价相关 20%、趋势强度 20%、波动率 15%、均值回复 10%、量价背离/反转 10%。

**本日因子环境判断：** 地缘风险推高油价 → Energy 动量 + 量价相关共振；Fed 鹰派 + 高收益率 → Technology 高估值股承压（动量/趋势强度走弱），资金转向 Healthcare（Heating-Up）与 Financial / Staples（Improving）；9月魔咒下对高动量股需结合"反转"因子（Alpha#12/#53）审慎评估追高风险。

---

## Top 20 精选股票

### 第一梯队：综合评分 8.5+

| 排名 | 代码 | 公司名称 | 板块 | 市值 | 核心因子 | 因子信号解读 | 综合评分 |
|------|------|----------|------|------|----------|-------------|----------|
| 1 | LLY | 礼来 / Eli Lilly | Healthcare / Pharma | ~$1.2T | Alpha#1, Alpha#41 | 近一年 +74~78%，8/24 收 $1,246.93 逼近 52 周新高 $1,292.65；Q2 营收 +48%($22.97B) 超预期，全年指引上调至 $85-87B；趋势强度极高，量价齐升 | 9.2 |
| 2 | XOM | 埃克森美孚 / Exxon Mobil | Energy / Integrated | $640B+ | Alpha#1, Alpha#6, Alpha#41 | 8/31 +2.71% 至 $160.95；年内 +33~36%，YTD 领先板块；油价重返 $90 + 霍尔木兹溢价，量价共振，趋势强度显著优于 VWAP | 9.0 |
| 3 | MRK | 默克 / Merck | Healthcare / Pharma | $330B+ | Alpha#1, Alpha#41 | 近一年 +89.5%（B 股板块最高）；与 Moderna mRNA 癌症疫苗 Phase 3 成功，8/19 单日 +12%；9 只 Big Pharma 创新高，动量强 | 8.8 |
| 4 | CVX | 雪佛龙 / Chevron | Energy / Integrated | $360B+ | Alpha#1, Alpha#30 | 8/31 +2.12% 至 $206.14；年内 +36%；Hess 整合扩储 + 委内瑞拉布局，油价敏感度高，放量上行波动率稳定 | 8.5 |
| 5 | CRWD | CrowdStrike / CrowdStrike | Technology / Cybersecurity | $58B+ | Alpha#6, Alpha#30 | 8/31 +5.77% 至 $231（Fal.Con 2026 催化）；2026 年内 +94%，创收盘新高；Q2 ARR +25%($5.84B)、Falcon Flex ARR +101%，连续四季加速，量价齐升（估值 P/S 43.5x 极高需警惕） | 8.5 |

### 第二梯队：综合评分 7.5-8.4

| 排名 | 代码 | 公司名称 | 板块 | 市值 | 核心因子 | 因子信号解读 | 综合评分 |
|------|------|----------|------|------|----------|-------------|----------|
| 6 | JNJ | 强生 / Johnson & Johnson | Healthcare / Pharma | $460B+ | Alpha#1, Alpha#53 | 近一年 +54%，8/25 报 $272.91 贴近纪录；FDA 获批 + 上调指引；冲高后小幅回踩为 Alpha#53 反转/均值回复提供了再入场机会 | 8.3 |
| 7 | SLB | 斯伦贝谢 / Schlumberger | Energy / Oilfield Services | $72B+ | Alpha#6, Alpha#30 | 8/31 +4.83% 至 $60.10（板块最强），成交量 35.21M 显著放大；年内 +56%；油服在油价上涨 + 钻机活跃度回升双驱动下量价齐升 | 8.2 |
| 8 | PLTR | Palantir / Palantir Technologies | Technology / Data Analytics | $450B+ | Alpha#6, Alpha#41 | 8月 +48%（Q2 美国商业收入 +150%）；8/31 $186.38，日成交 25.59M 高企；AI 主权需求叙事 + 动量延续，但已远离 VWAP、追高风险上升 | 8.0 |
| 9 | UNH | 联合健康 / UnitedHealth | Healthcare / Managed Care | $500B+ | Alpha#1, Alpha#19 | Q2 营收 $112.03B 超预期，EPS $6.38 远超预期（$4.90）；MCR 改善至 86.7%，上调全年指引 $19.50-20.00；8月创新高，防御型动量 | 7.9 |
| 10 | AMZN | 亚马逊 / Amazon | Consumer Discretionary / Internet | ~$3T | Alpha#6, Alpha#41 | 8/28 +3.97% 至 $266.43（AWS +37%、$220B AI capex）；突破下降趋势线 + 38.2% Fib；8/31 -2.5%（FTC 起诉广告操纵）回踩，量价仍属健康（支撑 $263-264） | 7.7 |

### 第三梯队：综合评分 7.0-7.4

| 排名 | 代码 | 公司名称 | 板块 | 市值 | 核心因子 | 因子信号解读 | 综合评分 |
|------|------|----------|------|------|----------|-------------|----------|
| 11 | MSFT | 微软 / Microsoft | Technology / Software | $3.9T | Alpha#1, Alpha#41 | 8/31 逆势 +1.68%（平台股避风港）；$513 上方，Azure +43%、Copilot 3,000万付费座席；趋势强度高，高收益率环境下的现金流安全垫 | 7.6 |
| 12 | V | Visa / Visa | Financial / Payments | $690B+ | Alpha#1, Alpha#12 | 金融板块 Improvising，支付双寡头之一；降息不确定 + 消费韧性，8月创新高并回踩，Alpha#12/均值回复信号 | 7.3 |
| 13 | NOW | ServiceNow / ServiceNow | Technology / Software | $290B+ | Alpha#1, Alpha#6 | 8/31 +2.27%（$147.99）；8月 +33%，AI 整合进现有 stack 印证"软件未死"；量价齐升，反弹最坚决 | 7.2 |
| 14 | VEEV | Veeva / Veeva Systems | Healthcare / Life Sciences | $30B+ | Alpha#6, Alpha#30 | 8/31 +4.9%（大医疗逆势）；8月 +40%，生命科学 AI 叙事 + 医药板块轮动共振；放量上行 | 7.1 |
| 15 | TEAM | Atlassian / Atlassian | Technology / Software | $48B | Alpha#1, Alpha#19 | 8月 +83.6%（月度大反弹）；软件被过度抛售后均值回复猛烈，动量与反转因子共振 | 7.0 |

### 第四梯队：综合评分 6.5-7.0

| 排名 | 代码 | 公司名称 | 板块 | 市值 | 核心因子 | 因子信号解读 | 综合评分 |
|------|------|----------|------|------|----------|-------------|----------|
| 16 | HAL | 哈里伯顿 / Halliburton | Energy / Oilfield Services | $33B+ | Alpha#6, Alpha#30 | 8/31 +1.85% 至 $36.85；油服量价齐升，钻机数回升迹象，油价反攻第三梯队受益 | 6.9 |
| 17 | TSLA | 特斯拉 / Tesla | Consumer Discretionary / Auto | $1.3T+ | Alpha#1, Alpha#12 | 8/31 +5.51% 创逾一个月新高（港澳/澳门 Model 3）；能源业务 Megapack 受益"外国电力设备禁令"，5/10/20均线多头，量价配合 | 6.8 |
| 18 | MRNA | 莫德纳 / Moderna | Healthcare / Biotech | $55B | Alpha#53, Alpha#19 | 8月 +150%（与 Merck mRNA 癌症疫苗 Phase 3 成功），短期涨幅极端、严重超买；作为反转/动量混合标的仅作高风险观察 | 6.7 |
| 19 | SNDK | 闪迪 / SanDisk | Technology / Memory | $30B+ | Alpha#6, Alpha#30 | 8/31 尾盘急升 +5.50%（$1,566.7）；SK海力士拟日本建厂 + AI 数据中心存储需求；高波动量价，但 7 月曾单月 -46%（均值回复中） | 6.6 |
| 20 | COIN | Coinbase / Coinbase Global | Financial / Crypto | $70B+ | Alpha#6, Alpha#12 | 8/31 +5%（加密概念走强）；8月 +29%，财政/债务担忧下的稀缺资产对冲；高波动率 + 量价背离信号（年内仍 -17%，均值回复空间） | 6.5 |

---

## Top 20 排名总表

| 排名 | 代码 | 公司名称（中/英） | 板块 | 市值 | 核心因子 | 综合评分 |
|------|------|-------------------|------|------|----------|----------|
| 1 | LLY | 礼来 / Eli Lilly | Healthcare | ~$1.2T | Alpha#1, Alpha#41 | 9.2 |
| 2 | XOM | 埃克森美孚 / Exxon Mobil | Energy | $640B+ | Alpha#1, Alpha#6, Alpha#41 | 9.0 |
| 3 | MRK | 默克 / Merck | Healthcare | $330B+ | Alpha#1, Alpha#41 | 8.8 |
| 4 | CVX | 雪佛龙 / Chevron | Energy | $360B+ | Alpha#1, Alpha#30 | 8.5 |
| 5 | CRWD | CrowdStrike / CrowdStrike | Technology | $58B+ | Alpha#6, Alpha#30 | 8.5 |
| 6 | JNJ | 强生 / Johnson & Johnson | Healthcare | $460B+ | Alpha#1, Alpha#53 | 8.3 |
| 7 | SLB | 斯伦贝谢 / Schlumberger | Energy | $72B+ | Alpha#6, Alpha#30 | 8.2 |
| 8 | PLTR | Palantir / Palantir | Technology | $450B+ | Alpha#6, Alpha#41 | 8.0 |
| 9 | UNH | 联合健康 / UnitedHealth | Healthcare | $500B+ | Alpha#1, Alpha#19 | 7.9 |
| 10 | AMZN | 亚马逊 / Amazon | Consumer Discretionary | ~$3T | Alpha#6, Alpha#41 | 7.7 |
| 11 | MSFT | 微软 / Microsoft | Technology | $3.9T | Alpha#1, Alpha#41 | 7.6 |
| 12 | V | Visa / Visa | Financial | $690B+ | Alpha#1, Alpha#12 | 7.3 |
| 13 | NOW | ServiceNow / ServiceNow | Technology | $290B+ | Alpha#1, Alpha#6 | 7.2 |
| 14 | VEEV | Veeva / Veeva Systems | Healthcare | $30B+ | Alpha#6, Alpha#30 | 7.1 |
| 15 | TEAM | Atlassian / Atlassian | Technology | $48B | Alpha#1, Alpha#19 | 7.0 |
| 16 | HAL | 哈里伯顿 / Halliburton | Energy | $33B+ | Alpha#6, Alpha#30 | 6.9 |
| 17 | TSLA | 特斯拉 / Tesla | Consumer Discretionary | $1.3T+ | Alpha#1, Alpha#12 | 6.8 |
| 18 | MRNA | 莫德纳 / Moderna | Healthcare | $55B | Alpha#53, Alpha#19 | 6.7 |
| 19 | SNDK | 闪迪 / SanDisk | Technology | $30B+ | Alpha#6, Alpha#30 | 6.6 |
| 20 | COIN | Coinbase / Coinbase Global | Financial | $70B+ | Alpha#6, Alpha#12 | 6.5 |

---

## 按板块分类汇总

### Healthcare（6 只）
LLY, MRK, JNJ, UNH, VEEV, MRNA

**板块逻辑：** 本日最强"确定性"方向。板块"Heating-Up"，9 只 Big Pharma 创 8 月 52 周新高（MRK 一年 +89.5% / LLY +74% / JNJ +54%）。GLP-1（LLY）+ 个性化癌症疫苗（MRK/MRNA）+ AI 保险效率（UNH）等多重主线，防御性成长兼备，且在高利率地缘风险下成为避风港。

### Energy（4 只）
XOM, CVX, SLB, HAL

**板块逻辑：** 年内最佳板块，油价重返 $90+ 催化。美伊冲突 + 霍尔木兹海峡航运受阻推高供给风险溢价，YTD XLE +44%，SLB +56% / XOM +36% / CVX +36%。油服（SLB/HAL）兼具油价与钻机活跃度双驱动，量价相关因子（Alpha#6）信号最强。

### Technology（6 只）
CRWD, PLTR, MSFT, NOW, TEAM, SNDK

**板块逻辑：** 高领涨但分化。平台/软件（MSFT/PLTR/CRWD/NOW/TEAM）在"软件未死"叙事下强势反弹（PLTR 8月 +48%、TEAM +83%、NOW +33%），网络安全受 AI 安全需求驱动（CRWD 年内 +94% 创高）；AI 硬件链（NVDA/MRVL/ARM）则因估值和高利率承压。存储（SNDK）波动大，仅作均值回复标的。

### Consumer Discretionary（2 只）
AMZN, TSLA

**板块逻辑：** 板块 8/28 领涨（XLY +1.15%）。AMZN AWS +37%、$220B AI capex 突破趋势线但遭 FTC 起诉回踩；TSLA 港澳 Model 3 + 能源业务受益电力设备禁令。

### Financial（2 只）
V, COIN

**板块逻辑：** 金融板块 Improvising。支付双寡头（V）趋势稳健；COIN 加密/稀缺资产对冲高度投机。

---

## 风险提示

1. **9月魔咒 + 加息风险**：9 月为美股历史最弱月份（标普平均 -1.1%、正收益概率 44.5%）；9/16 FOMC 加息 25bp 概率 ~66%，若超预期鹰派，高估值成长股（CRWD/LY PLTR/TEAM）将承压——这些 P/S、P/E 均处极端
2. **油价地缘溢价可逆**：XOM/CVX/SLB/HAL 的上涨由美伊冲突驱动，若局势缓和 / 霍尔木兹通航恢复，风险溢价随时可能快速回吐
3. **Healthcare 短期过热**：MRNA 8月 +150%、MRK/LLY/JNJ 大涨后需警惕获利了结，尤其 LLY 交易 ~62x 远期 P/E、产品定价下行风险
4. **高动量追高风险**：PLTR/TEAM/CRWD 已大幅远离 VWAP，Alpha#1 动量虽强但有 Alpha#12 反转隐患，9月魔咒下波动率可能放大
5. **NVDA 财报后"抛售"与 AI 硬件链分化**：NVDA 回撤至 $217（支撑 $200/$190），MRVL/ARM/AMAT 重挫揭示 AI 硬件板块内部风险
6. **FTC 监管风险**：AMZN 被 FTC+22 州起诉（广告价格操纵），反垄断/监管不确定性
7. **单一因子局限性**：WorldQuant 101 因子本质是技术面量化信号，需结合基本面与宏观环境综合判断，不可作为唯一决策依据

> ⚠️ 免责声明：本报告仅为基于 WorldQuant 101 因子框架的量化分析研究，不构成任何投资建议。投资有风险，决策需谨慎。
