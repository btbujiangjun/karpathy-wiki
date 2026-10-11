---
title: WorldQuant 101 Alphas 每日精选 - 美股 Top 20 (2026-10-11)
type: synthesis
created: 2026-10-11
updated: 2026-10-11
sources:
  - https://www.portfolio-terminal.com/blog/stock-market-week-in-review-october-9-2026
  - https://seekingalpha.com/news/4651869-s-and-p-500-advances-for-week-amid-ai-jitters-and-sector-rotation
  - https://www.cmegroup.com/videos/2026/10/09/e-mini-s-p-500-futures-near-all-time-highs-as-sector-rotation-su.html
  - https://www.reuters.com/business/wall-st-week-ahead-bank-earnings-cpi-headline-busy-markets-week-sp-500-hovers-2026-10-09/
  - https://www.cnbc.com/2026/10/09/jim-cramer-week-ahead-bank-earnings-ai-chips.html
  - https://www.jpmorganchase.com/ir/news/2026/jpmc-to-host-third-quarter-2026-earnings-call
  - https://www.investmenthouse.com/2026/09/15/goldman-sachs-near-1t-in-ma-this-year-q3-earnings-oct-13
  - https://investor.asml.com/quarterly-results
  - https://investor.tsmc.com/english/quarterly-results/2026/q3
  - https://fiscal.ai/company/NYSE-SNOW
  - https://www.benzinga.com/trading-ideas/movers/26/10/62279712/why-is-newmont-stock-surging-on-friday
  - https://www.investing.com/equities/palantir-technologies-inc-consensus-estimates
  - https://www.sec.gov/Archives/edgar/data/1318605/000162828026064366/exhibit991111111.htm
tags: [wq101, alpha-factors, quantitative, stock-selection, us-equities, earnings-season, week-ahead, semiconductors, software, banks, gold, towers, 2026-10-11]
---

# WorldQuant 101 Alphas 每日精选 — 美股 Top 20（2026-10-11，周日/下周前瞻版）

> 基于 WorldQuant 101 Alphas 因子框架，对美股市场进行量化筛选，精选出最值得投资的 Top 20 只股票。
> 本期为**周日版**：分析基准 = **2026-10-09（周五）收盘信号**，重点为**下周 Q3 财报季开启（10/13 银行 → 10/14 ASML+CPI → 10/15 TSMC）的前瞻性因子布局**。今日休市。

## 市场概况（2026-10-09 收盘）

| 指数 | 收盘 | 单日 | 全周 |
|------|------|------|------|
| 标普 500 | 7,811.54（纪录收盘） | +0.59% | +1.15% |
| 纳斯达克综指 | 27,366.17 | +0.64% | +0.64% |
| 纳斯达克 100 | 30,883.15 | +0.51% | — |
| 道琼斯 | 51,654.95 | +0.83%（+423.31） | +0.93% |
| 罗素 2000 | 2,806.98 | +0.46% | −0.9% |
| VIX | ~14.8 | 回落 | 持平 |
| 10Y 美债 | ~5.24%（跨源 5.17%–5.31%） | 高位 | 2002 年来高位区 |
| WTI / Brent | ~$92 / ~$104 | — | 高位 |
| 现货金 | ~$4,195（盘中破 $4,200 纪录） | +1.8% | 破纪录 |

**核心叙事 = "OpenAI 营收惊吓次日，市场以『轮动修复』收官，焦点转向下周财报季"**：

1. **10/8 AI 惊吓 → 10/9 轮动修复**——10/8 FT 报道 OpenAI 年化营收约 $500 亿（vs 市场 $680~700 亿预期）触发 AI 硬件杀估值（SOX 单日 −3.39%）；10/9 三大指数集体收红创周内高点。但修复靠**板块切换**而非 AI 硬件回归：SOX 全周 −4.3%，等权重标普跑赢市值加权 = 集中度松动。
2. **软件/数据云/网安爆发**——SNOW +7.42%、DDOG +7.11%、PLTR +5.17%（**历史新高**）、CRWD +4.57%、PANW +5.09%——资金从"对 OpenAI 直接收入敞口大的硬件"切向"AI 应用/软件变现第二落点"。
3. **SpaceX ~$8B 收购 800MHz 频谱 → 电信闪崩、铁塔暴涨**——TMUS −13.27%（33 个月新低）、T −10.82%、VZ −10.14%；CCI +15.6%、AMT +9.3%——"卫星+地面基建"双受益的创造性破坏。
4. **黄金破 $4,200 → 金矿股走强**；**特斯拉 Q3 交付 486,532 超预期 +5.3%** 续燃 EV 反转叙事。
5. **下周定调事件密集**：10/13 银行财报季开启（JPM/GS/WFC/C）→ 10/14 ASML Q3 + 美国 9 月 CPI → 10/15 TSMC Q3 → 10/28 FOMC（市场定价"可能再度加息"，2Y 逼近 5%）。

**跨源口径提示**：10Y 美债收盘跨源在 **5.17%–5.31%** 区间（个别财经来源误报 3.92%，未采信）；股价/市值为 exa/fiscal.ai/交易平台口径估算，部分为盘中快照。

## WorldQuant 101 Alphas 核心因子说明

| 因子维度 | 选定 Alpha | 公式逻辑（简述） | 因子解读 |
|---|---|---|---|
| 动量 | Alpha#1 | `rank(ts_argmax(signed_power(returns<0 ? stddev(returns,20) : close, 2), 5)) - 0.5` | 以近 5 日极值位置衡量动量强弱，捕捉趋势延续；历史新高/5 日极值标的最强。 |
| 动量/量价 | Alpha#6 | `Correlation(open, volume, 10)` | 开盘价与成交量的相关性，衡量量价同步性；放量上涨时正向强化。 |
| 反转 | Alpha#53 | `-1 * Delta((((close-low)-(high-close))/(close-low)), 9)` | 价位内部结构的 9 日变化；事件性暴跌（极端 range）后的均值修复信号。 |
| 波动率/反转 | Alpha#30 | `(-1 * rank(((2*scale(rank(((close-low)-(high-close))/(high-low))*volume)) - scale(rank(delta(close,3)))))) * sum(volume,5)` | 日内价差×成交量的波动结构；机构放量 + 洗盘结构 = 优质入场。 |
| 量价背离 | Alpha#12 | `sign(delta(volume,1)) * (-1 * delta(close,1))` | 量增价跌 / 量缩价涨的背离信号；暴跌后放量企稳为修复标志。 |
| 趋势强度 | Alpha#41 | `((high*low)^0.5) - vwap` | 区间几何均值 vs VWAP 的偏离，衡量趋势强度；资源/贵金属趋势延续的核心因子。 |
| 均值回复 | Alpha#19 | `-1 * rank((stddev(abs(close-open),5) + (close-open) + rank(correlation(close,open,10))))` | 基于开盘-收盘波动与相关性的短期均值回复；防御/价值梯队风险控制因子。 |

> 注：以上因子基于 WorldQuant 101 Formulaic Alphas（Kakushadze, 2016）理论逻辑，结合 10/9 收盘市场信号进行定性解读与选股匹配。

## Top 20 股票筛选结果（分析基准：2026-10-09 收盘 + 下周催化剂）

| 排名 | 代码 | 公司（中/英） | 板块 | 市值（估算） | 核心 Alpha | 因子信号解读（方向+强度） | 综合评分 | 投资逻辑简述 | 风险提示 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | TSM | 台积电 / Taiwan Semiconductor | Semiconductors（代工） | ~$1.2T | Alpha#41 + Alpha#6 | 趋势：强（高强度，价运行于均线/VWAP 上方）；量价：同步（中-高强度） | 9.5 | **10/15 Q3 财报为全周最硬催化**（3Q26 指引营收 $44.6–45.8B、毛利率 65–67%），Q3 营收同比约 +50%；ASML/TSMC 开启半导体财报周，CoWoS/先进制程为 AI 算力瓶颈。ADR 随板块回调提供入场。Alpha#41 趋势 + Alpha#6 量价。 | 地缘（两岸）、客户集中、AI capex 验证、汇率、先进制程溢价已计价。 |
| 2 | PLTR | 帕兰提尔 / Palantir Technologies | Software（AI 应用） | ~$420B | Alpha#1 + Alpha#6 | 动量：极值动量（高强度，历史新高）；量价：放量同步（高强度） | 9.3 | 10/9 **+5.17% 收 $209.05 创历史新高**；AI agent 软件变现龙头，Open Agent Safety 生态外溢；52 周低点 $106.37 翻倍。Alpha#1 极值动量 + Alpha#6 量价双共振，全榜动量信号最强。 | 估值极端（P/E ~150x+）、国防收入集中、拥挤交易、叙事降温易高波动。 |
| 3 | JPM | 摩根大通 / JPMorgan Chase | Financials（银行） | ~$850B | Alpha#41 + Alpha#6 | 趋势：稳（中-高强度，均线上方）；量价：同步（中强度） | 9.1 | **10/13 银行财报季开启**（Q3 共识 EPS ~$5.82–5.84，投资银行/交易收入指引中高双位数增长）；10Y 高位利好净息差。Alpha#41 趋势 + Alpha#6 量价，事件驱动确定性最高。 | 信贷成本、利率路径、资本监管、财报不及预期、银行板块拥挤。 |
| 4 | SNOW | 雪花 / Snowflake | Software（数据云） | ~$116B | Alpha#6 + Alpha#53 | 量价：放量 V 型修复（高强度，8.0M 股）；反转：极端内部结构修复（高强度） | 9.0 | 10/9 **+7.42% 收 $368.89**，单日吞没 10/8 跌幅；对 OpenAI 直接收入敞口小 = "轮动免疫"标的。Alpha#6 量价同步 + Alpha#53 内部结构修复共振。 | 高估值软件（尚未盈利口径）、营收增速换挡、机构持仓拥挤。 |
| 5 | NVDA | 英伟达 / NVIDIA | Semiconductors | ~$5.6T | Alpha#53 + Alpha#30 | 反转：深跌后风险收益改善（中-高强度，距 ATH ~5%）；波动结构：机构放量介入（高强度，~3.2× 均量） | 8.9 | 基本面未被 OpenAI 事件破坏：Q3 指引 $1,080 亿±2%、回购累计 $2,350 亿、Rubin 需求超供给；**10/9 放量（3.2× 均量）为机构确认信号**。Alpha#53/#30 识别"有基本面支撑的洗盘"入场。11/18 财报为关键验证。 | 单一客户收入传导脆弱、公开融资窗口收紧、出口/地缘约束、高利率压制高估值。 |
| 6 | GS | 高盛 / Goldman Sachs | Financials（投行） | ~$220B | Alpha#41 + Alpha#6 | 趋势：强（中-高强度，突破结构）；量价：放量（中强度） | 8.8 | **10/13 Q3 财报**（共识 EPS ~$16），全年 M&A 顾问规模 >$1 万亿、SpaceX IPO lead-left；Polymarket 隐含约 **74% 超预期概率**。Alpha#41 趋势 + Alpha#6 量价，事件前动能配合。 | 交易收入波动、资本市场监管、财报预期已高、宏观 alpha 依赖。 |
| 7 | NEM | 纽蒙特 / Newmont | Materials（黄金） | ~$130B | Alpha#41 + Alpha#6 | 趋势：强（高强度，金价破纪录）；量价：同步（中-高强度） | 8.7 | 现货金 ~$4,195 创纪录区域，10/9 NEM +2.06% 收 $117.93；Q1/Q2 连续 FCF 创纪录（Q2 ~$22 亿）、$60 亿回购计划，**10/22 Q3 财报**。Alpha#41 趋势强度 + Alpha#6 量价同步。 | 金价高位回调、AISC 成本通胀（$1,400–1,550/oz）、产量下滑、美元/实际利率反弹。 |
| 8 | MSFT | 微软 / Microsoft | Software / IT | ~$3.9T | Alpha#6 + Alpha#19 | 量价：温和同步（中-高强度）；均值回复：波动可控（中强度） | 8.6 | 10/9 +1.89%，云+AI 现金流韧性最强，回撤幅度小于纯硬件标的；"软件修复轮动"中的压舱石。Alpha#6 量价配合 + Alpha#19 波动结构稳定。 | AI capex 回报节奏、云增长放缓、监管（DOJ）、10Y 高位对高估值压制。 |
| 9 | LITE | 卢孟特 / Lumentum | Optical（光模块） | ~$70B | Alpha#1 + Alpha#41 | 动量：板块领涨（高强度）；趋势：产能售罄至 2029（高强度） | 8.4 | **+5.22% 收 $1,103**——数据中心 DCI 物理需求仍在的最硬证据，已在 OpenAI 惊吓日逆势走强。Alpha#1 动能 + Alpha#41 趋势强度，为算力链中"消息免疫"最佳候选。 | 高估值、需求周期见顶疑虑、客户集中（超大规模厂）、光模块价格战。 |
| 10 | GOOGL | 谷歌 / Alphabet | Communication Services | ~$4.2T | Alpha#19 + Alpha#41 | 均值回复：波动可控（中强度）；趋势：稳（中-高强度） | 8.4 | 核电-算力核心买方（CEG 20 年 PPA）+ Gemini 生态/云推进，前瞻 P/E ~16.6x 相对 Mag 7 有吸引力。Alpha#19 防御 + Alpha#41 趋势稳健。 | AI 搜索竞争（ChatGPT/Perplexity）、云盈利节奏、DOJ/监管、capex 强度。 |
| 11 | MU | 美光 / Micron | Semiconductors（存储） | ~$1.2T | Alpha#53 + Alpha#30 | 反转：企稳确认（中-高强度）；波动结构：回调后缩量收敛（中强度） | 8.3 | 存储超级周期延续（DRAM 合约价上行、三星 HBM4、S&P 100 成分），9/30 财报后随 OpenAI 惊吓回撤、10/9 盘前企稳。Alpha#53/#30 显示高位洗盘而非破位。 | 存储价格拐点、供给释放、AI capex 节奏、周期股在高利率下的估值。 |
| 12 | ASML | 阿斯麦 / ASML | Semiconductors（设备） | ~$680B | Alpha#41 + Alpha#6 | 趋势：强（中-高强度）；量价：同步（中强度） | 8.2 | **10/14 Q3 财报**（共识 EPS ~$12.54，同比 +96%，期权隐含波动 **±8.5%**）；Q3 指引 €11–12bn / 毛利率 55–57%；EUV 垄断 + TSMC 2027 capex 上看 $850 亿的上游受益人。Alpha#41 + Alpha#6。 | 客户延迟交付、订单波动、估值已高（P/E ~55x）、出口管制、财报后波动剧烈。 |
| 13 | AVGO | 博通 / Broadcom | Semiconductors（ASIC/网络） | ~$1.7T | Alpha#53 + Alpha#30 | 反转：超卖反弹结构（中-高强度）；波动结构：回撤后改善（中强度） | 8.1 | 10/8 −4.35% 后，定制 ASIC + 网络业务基本面未变，OpenAI 定制芯片融资（>$500 亿）为长逻辑。Alpha#53/Alpha#30 识别超卖反弹结构。 | 客户融资/债务风险、AI 订单节奏、估值、消息面扰动。 |
| 14 | DDOG | 达特多格 / Datadog | Software（可观测性） | ~$130B | Alpha#1 + Alpha#6 | 动量：放量爆发（高强度）；量价：板块同步（高强度） | 8.0 | +7.11%，软件风险偏好回升日最大受益者之一；可观测性 = AI 基建"数字后院"刚需，对 OpenAI 收入敞口小。Alpha#1/#6 双动量结构。 | 高估值成长股、云优化节奏、竞争（微软/新进入者）、高利率估值压缩。 |
| 15 | TSLA | 特斯拉 / Tesla | Consumer Discr（EV） | ~$1.26T | Alpha#53 + Alpha#30 | 反转：交付兑现后反弹（高强度）；波动结构：RSI 修复、MACD 转正（中-高强度） | 8.0 | Q3 交付 **486,532（超共识 +5.3%）**、储能 13.7GWh；10/9 +2.05% 收 $382.70；**10/21 Q3 财报**（共识 EPS $0.41 / 营收 $27.6B）为验证点。Alpha#53 反转 + Alpha#30 波动结构。 | 利润率（Q2 接近运营亏损）、YTD 跑输 mega-cap、高利率、储能不及预期。 |
| 16 | CCI | 皇冠城堡 / Crown Castle | Telecom REIT（铁塔） | ~$35B | Alpha#6 + Alpha#41 | 量价：放量突破（高强度）；趋势：新升浪（高强度） | 7.9 | SpaceX 收购 800MHz 频谱 → 若自建地面网将新增租户（Bernstein：自建成本 $50–130B）。**+15.6% 收 $79.64**，量价同步极强（Alpha#6）+ 突破趋势完整（Alpha#41）。"卫星替代 vs 铁塔受益"分歧中的反直觉赢家。 | 单日 +15.6% 已相当延伸、FCC 批准不确定、涨幅过于乐观、高杠杆 REIT 对利率敏感。 |
| 17 | AMT | 美国铁塔 / American Tower | Telecom REIT（铁塔） | ~$85B | Alpha#6 + Alpha#41 | 量价：放量上行（高强度）；趋势：修复性新高（中-高强度） | 7.8 | +9.3% 收 $182.24，铁塔板块受益 SpaceX 地面网租户预期；相对 CCI 单日涨幅更温和（+9.3% vs +15.6%）= 动量未过度，趋势完整度更高。Alpha#6/#41 结构稳健。 | 利率敏感（10Y 高位）、租户集中、估计偏乐观修正风险、全球业务汇率。 |
| 18 | BABA | 阿里巴巴 / Alibaba | Communication Services（ADR） | ~$260B | Alpha#6 + Alpha#1 | 量价：放量领涨（中-高强度）；动量：ADR 领袖（中强度） | 7.7 | **+5.36% 收 $111.37** 领涨金龙指数（+2.69%），恒生科技指数改编（12/7 生效，AI/硬科技增量买盘预期）+ AI 云叙事 + 沽空回补（约 24.7%）。Alpha#6 量价 + Alpha#1 动量修复。 | 沽空/筹码结构、外资情绪持续性、地缘与政策扰动、估值分歧。 |
| 19 | CRWD | 克劳德斯瑞克 / CrowdStrike | Software（网安） | ~$271B | Alpha#1 + Alpha#6 | 动量：修复阳线（高强度）；量价：板块共振（中-高强度） | 7.6 | +4.57%，网安防御属性 + AI agent 安全叙事（NVDA Open Agent Safety 平台、100+ 合作伙伴）；FY26 营收 $4.8B +21.7%。Alpha#1/#6 显示健康修复。 | 2024 更新事故余波、依赖公有云基础设施、估值溢价、订阅放缓。 |
| 20 | XOM | 埃克森美孚 / Exxon Mobil | Energy | ~$660B | Alpha#41 + Alpha#6 | 趋势：油价高位下的强趋势（中-高强度）；量价：温和同步（中强度） | 7.5 | 2026 年最热标的之一（YTD ~+18%），Q2 盈利 $14.5B + FCF $17.2B；WTI ~$92 / Brent ~$104 高位支撑。Alpha#41 趋势完整，但 10/9 能源板块回落、动量边际减弱，降档配置。 | 油价回落风险（Hormuz 缓和/需求走弱）、上游高基数、地缘溢价回吐、分红政策。 |

## 按板块分类汇总

| 板块 | 入选股票（代码） | 特征分析 |
|---|---|---|
| **Semiconductors / 设备 / 光通信（6）** | TSM、NVDA、MU、ASML、AVGO、LITE | **下周 ASML（10/14）+ TSMC（10/15）开启半导体财报周**，是全周最硬的因子催化。两条线：Alpha#41/A#6 趋势型（TSM/ASML/LITE，产能售罄/EUV/代工瓶颈）与 Alpha#53/A#30 洗盘反转型（NVDA/MU/AVGO，OpenAI 惊吓后"有基本面支撑的回撤"）。 |
| **Software / 数据云 / 网安 / AI 应用（5）** | PLTR、SNOW、MSFT、DDOG、CRWD | 本期最大赢家群体。资金从"算力硬件"推向"AI 变现/软件第二落点"，Alpha#1（动量）+ Alpha#6（量价同步）信号最密；PLTR（历史新高）与 SNOW（V 型修复）为双因子最强标的。 |
| **Financials（2）** | JPM、GS | **10/13 银行财报季开启**的事件驱动标的。Alpha#41（趋势）+ Alpha#6（量价）配合；JPM 共识 EPS ~$5.82、GS ~$16 且隐含 ~74% 超预期。利率高位利好净息差。 |
| **Telecom REIT / 铁塔（2）** | CCI、AMT | SpaceX 频谱事件的"反直觉赢家"——800MHz 低频穿透力强、室内覆盖需地面铁塔。Alpha#6 放量突破 + Alpha#41 趋势，但单日涨幅已大，需防喧嚣顶部。 |
| **Comm Svcs / 中概（2）** | GOOGL、BABA | GOOGL 为电力战略买方 + Gemini 生态（Alpha#19 防御）；BABA 为中国资产共振修复的 ADR 领涨（Alpha#6 量价同步）。 |
| **Materials / 黄金（1）** | NEM | 金价破 $4,200 历史新高，宏观/地缘对冲，Alpha#41 趋势强度核心因子；10/22 Q3 财报。 |
| **Consumer Discr / EV（1）** | TSLA | Q3 交付 486,532 超预期，Alpha#53 反转 + Alpha#30 波动结构；10/21 财报为验证点。 |
| **Energy（1）** | XOM | 油价高位（WTI ~$92 / Brent ~$104）支撑趋势，但 10/9 能源回落，动量边际减弱，降档配置。 |

## 下周催化剂日历（2026-10-13 → 10-28）

| 日期 | 事件 | 影响标的 |
|---|---|---|
| 10/13（一）BMO | **JPM、WFC、GS、C Q3 财报**（JPM 通话 8:30 ET） | JPM（#3）、GS（#6）、银行板块 |
| 10/14（二）BMO / 8:30 ET | **ASML Q3 财报**（07:00 CET，隐含波动 ±8.5%）+ **美国 9 月 CPI** + BAC/MS 财报 | ASML（#12）、BAC/MS、利率敏感资产 |
| 10/15（三）14:00 ET | **TSMC Q3 财报** + 美国 9 月零售销售 + 英国 GDP | TSM（#1）、全半导体链 |
| 10/16（五） | 月度期权到期 | 高成交/高持仓个股 |
| 10/20（二）盘后 | Netflix Q3 | 流媒体/科技 |
| 10/21（三）盘后 | **Tesla Q3**（共识 EPS $0.41 / 营收 $27.6B） | TSLA（#15） |
| 10/22 | Newmont Q3 | NEM（#7） |
| 10/27–28 | **FOMC 议息（决议 10/28 14:00 ET）** | 全市场；市场定价"可能再度加息" |

## 投资逻辑总结

1. **财报周定调**：10/13 银行（JPM/GS）→ 10/14 ASML+CPI → 10/15 TSMC，本周由"软件/AI 应用动量"与"半导体财报验证"双主线主导。因子框架下 **TSM（Alpha#41 趋势）** 与 **PLTR/SNOW（Alpha#1+#6 放量动量）** 信号最强；**JPM/GS** 为事件驱动确定性最高的组合。
2. **Alpha#53 反转群体**：NVDA/MU/AVGO/TSLA 经历事件性回撤后，以 **Alpha#53（反转）+ Alpha#30（波动结构）** 识别"有基本面支撑的洗盘"，而非破位；需以成交量与波动结构确认企稳。
3. **事件驱动四条独立线**：① 半导体财报周（ASML/TSMC）；② 黄金破纪录（NEM）；③ SpaceX 频谱（CCI/AMT 铁塔）；④ 特斯拉交付超预期（TSLA）。
4. **宏观悬顶**：10/14 9 月 CPI + 10/28 FOMC（2Y 逼近 5%，市场定价"可能再度加息"）+ 10Y ~5.2% 高位——"利率压估值"与"财报验证"并存，成长/高估值资产弹性与脆弱性同源。
5. **组合结构**：核心 ~55% = 半导体 + 软件/AI 应用（11 席），事件驱动 ~20% = 银行 + 黄金（JPM/GS/NEM），反直觉/防御 ~25% = 铁塔 + EV + 能源 + 中概（CCI/AMT/TSLA/XOM/BABA/GOOGL/CRWD）。整体对"OpenAI 单一客户收入"的直接暴露低于纯算力组合。

## 风险提示

- **利率/CPI 风险**：10Y 约 5.2% 高位 + 10/14 CPI + 10/28 FOMC；若 CPI 超预期或加息预期升温，高估值软件/半导体首当其冲。
- **财报验证风险**：ASML（隐含 ±8.5%）、TSMC、JPM/GS 的指引将决定"AI capex 可持续性"与"银行资本市场需求"能否兑现；OpenAI 会计口径事件提醒"单一大客户收入"传导脆弱。
- **事件逆反风险**：铁塔暴涨建立在 SpaceX 自建地面网假设上（FCC 未批、分析师提示过度乐观）；电信三巨头暴跌后可能反向超卖反弹。
- **拥挤度/动量衰减风险**：软件/网安单日放量普涨后短期易分化；WQ101 因子在公开传播后可能衰减，本报告为公开数据的定量框架应用，**不构成投资建议**。
- **数据口径风险**：部分价格/市值为网络检索估算值（10Y 跨源 5.17%–5.31%、个别来源误报 3.92% 未采信），可能与行情终端存在差异；下周事件日期以公司 IR 为准。

---
报告日期：2026-10-11（周日/下周前瞻版）
分析基准：2026-10-09 美股收盘
因子框架：WorldQuant 101 Formulaic Alphas（Kakushadze, 2016）
声明：本报告仅供研究参考，不构成投资建议。
