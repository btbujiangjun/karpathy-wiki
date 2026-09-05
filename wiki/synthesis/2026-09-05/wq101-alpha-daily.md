---
title: WorldQuant 101 Alpha 因子选股日报 — 2026-09-05
type: synthesis
created: 2026-09-05
updated: 2026-09-05
sources: []
tags: [quant, worldquant-101, alpha-factors, us-stock-picks, daily-report, memory, semiconductors, refining, gold, financials]
---

# WorldQuant 101 Alpha 因子选股日报 — 2026-09-05

> 基于 WorldQuant 101 Alpha 因子库，对美股中大盘股（市值 > $10B）进行量化筛选，精选 Top 20 标的。
> 数据基准：2026-09-04（周五）收盘。同年 9/6-9/7 周末，9/7 为 Labor Day 休市。

## 市场背景（9/4 周五收盘）

| 指数 | 收盘价 | 日涨跌 | 关键信号 |
|------|--------|--------|----------|
| S&P 500 | 7,718.60 | -0.4% | 周涨 +0.1%，冲高回落 |
| Nasdaq Composite | 26,506.99 | -0.3% | 周涨 +0.4%；硬件强、软件弱 |
| Dow Jones | 53,414.25 | -0.5% | 周跌 -0.3%，防御品种领跌 |
| Nasdaq 100 | 29,544.16 | +0.21% | 大盘科技相对强 |
| Russell 2000 | 2,975.65 | +0.25% | 中小盘相对抗跌 |

**核心驱动因素：**
1. **8 月非农大超预期**：新增就业 +162k（预期 +53k），9 月加息概率升至 57%~60.2%，2Y 收益率升至 4.37%（2025 年 1 月以来新高），10Y 约 4.8%
2. **存储/半导体板块爆发**：DRAM ETF（Roundhill Memory）单日 **+6.6%**，SOX 芯片指数 +2.1%；MU +6.1%、SNDK +8%~12%、WDC +4~6%、STX +5%、ALAB +9.75%、KLA +7% —— "硬件强于软件" 成为当日最大结构特征
3. **软件板块普跌**：Asana -11.8%、Workday -5.4%、Snowflake -5.2%、Palantir -3~4%（7 个月最差单日）、MSFT -2.04%；TSLA -5.92%（NHTSA 就 Cybercab 发调查函，吐回 9/3 涨幅）
4. **炼油/黄金双主线延续**：MPC/PSX/VLO 齐创新高（WTI 3-2-1 crack spread ~$9/bbl，约为 1 月的 3 倍）；金价 ~$4,400-4,509/oz 高位，Citi 目标 $5,000（2027 底）
5. **AI 主题从基建走向部署与变现**：GPT-6 Astra 分阶段开放定价（$10/$50 per M）；MSFT 发布 Project Zenith（64GB+ 本地跑 30B+ 模型）；Goldman Sachs 强调"谁在 AI 支出上真正赚到回报"成为新焦点

> 对比上一期（2026-09-04 报告，基于 9/3 收盘）：当时 Energy（CVX/XOM）+ 防御（JNJ）领跑；本日轮动信号明确——**资金回流存储/半导体 + 金融 + 炼油 + 黄金**。Top 20 中 9 只更替。

## 因子框架与评分方法

基于本任务给定的 7 类核心因子，对每只股票进行定性因子信号评估：

| 因子编号 | 因子逻辑（简化） | 信号方向 |
|----------|------------------|----------|
| Alpha#1 | Rank(Correlation(Delay(close,1), close, 10)) | 正 = 10 日收盘序列自相关高 → 趋势延续 |
| Alpha#6 | -1 × Rank(Correlation(open, volume, 10)) | 正 = 开盘价与成交量 10 日负相关（无追高量） |
| Alpha#12 | sign(delta(volume,1)) × (-1 × delta(close,1)) | 正 = 放量下跌后反转做多 / 缩量回调确认 |
| Alpha#19 | -1 × rank(stddev(abs(close-open),5) + (close-open) + rank(corr(close,open,10))) | 正 = 波动收敛 + 回归均值 |
| Alpha#30 | -1 × rank(2×scale(rank(日内位置×volume)) - scale(rank(delta(close,3)))) × sum(volume,5) | 正 = 5 日放量 + 日内位置与 3 日价格变化背离 |
| Alpha#41 | ((high × low)^0.5) - vwap | 正 = 典型价高于 VWAP → 买方控制 |
| Alpha#53 | -1 × Delta(((close-low)-(high-close))/(close-low), 9) | 正 = 9 日内收盘位置从低位转向高位（吸筹） |

**综合评分：** 动量 (Alpha#1) 25%、趋势强度 (Alpha#41) 20%、量价背离 (Alpha#12) 15%、反转/收盘位置 (Alpha#53) 15%、波动率/量能 (Alpha#30) 10%、量价相关 (Alpha#6) 10%、均值回复 (Alpha#19) 5%，加权后给出 1-10 分。

> ⚠️ 方法说明：本报告为每日研究型选股，因子值为基于公开行情快照（价格/成交量/板块 ETF/新闻事件的代理信号）的**定性重构**，并非在完整 OHLCV 面板上计算的原生意值。市值部分为近似估算（标注"估"）；跨数据源分歧处取多数来源或区间披露。不构成投资建议。

---

## Top 20 精选股票

### 第一梯队：综合评分 9.0

| 排名 | 代码 | 公司名称 | 板块 | 市值(估) | 核心因子 | 因子信号解读 | 综合评分 |
|------|------|----------|------|----------|----------|-------------|----------|
| 1 | NVDA | 英伟达 / NVIDIA | Technology / Semiconductors | $4.56T | Alpha#1, Alpha#41 | 8/27 财报跳空后于 $224-225 高位缩量整理（距 ATH $236.54 一步之遥），10 日收盘序列自相关强、典型价持续高于 VWAP；Q2 营收 $96.2B (+106%)、数据中心 $89B (+117%)、FY28 指引 +70%；RVOL ~0.8-1.0 无人气崩塌迹象 | 9.2 |
| 2 | MU | 美光 / Micron | Technology / Memory | ~$236B | Alpha#1, Alpha#12 | 周五 $1,016.59 放 +6.10% 创新高（35.25M 量、新高日），Alpha#1 动量 + Alpha#12 量价背离双确认；DRAM/NAND 合约价 QoQ +50%/+60%，先进制程 2026 底前售罄，Q4 指引 $50B±1、毛利 ~86%；分析师目标 $1,325-1,555 | 9.1 |
| 3 | MPC | 马拉松石油 / Marathon Petroleum | Energy / Refining | ~$132B | Alpha#41, Alpha#1 | $387.71 连续创新高，WTI crack spread ~$9/bbl（3 倍于 1 月）→ 典型价持续高于 VWAP + 动量延续；Q2 净利润 + 回购（TD Cowen 估年回购约 20% 市值），MPLX 中游稳定现金流；月涨 +24%、年涨 +120% | 9.0 |
| 4 | NEM | 纽蒙特 / Newmont | Basic Materials / Gold | ~$145B | Alpha#53, Alpha#1 | 8 月 +34.5%、金价 ~$4,400+，9 日内收盘位置持续抬升（吸筹确认）；EV/EBITDA ~9x、FCF yield >6%、AISC $1,621 vs 实际售价 $4,414；Citi 头号选股（金色矿商折价 ~$500/oz），央行年购金 ~1,000 吨/连续 4 年，美债破 $40T 的 "debasement trade" 主线 | 9.0 |

### 第二梯队：综合评分 8.0-8.9

| 排名 | 代码 | 公司名称 | 板块 | 市值(估) | 核心因子 | 因子信号解读 | 综合评分 |
|------|------|----------|------|----------|----------|-------------|----------|
| 5 | SNDK | 闪迪 / SanDisk | Technology / NAND Storage | ~$190B | Alpha#1, Alpha#30 | 周五 +8%~12% 至 ~$1,686 新高，5 日放量 + 日内强势（Alpha#30 量能确认）；Q4 营收 $8.96B (+371.6%)、GM 84.6%，Q1 指引 $10.3-10.8B（环比续涨）；YTD +555% 存储超级周期最强 Beta | 8.9 |
| 6 | MS | 摩根士丹利 / Morgan Stanley | Financials / Investment Bank | ~$330B | Alpha#1, Alpha#41 | YTD +19% 为六大行第一；Q2 创纪录营收 $21.35B、权益交易 +69%、财富+资管 $10T 客户资产；9/3 +2.52%，逼近 $231 前高（突破则上看 $250）；典型价高于 VWAP | 8.7 |
| 7 | GS | 高盛 / Goldman Sachs | Financials / Investment Bank | ~$350B | Alpha#1, Alpha#53 | 连续第 5 次盈利 beat（Q2 EPS $20.98 vs $14.54），IB 管道持续扩张（权益承销 +130%）；9/3 +3.34%、9 日收盘位置抬升（Alpha#53）；股息 +11%；YTD +14% | 8.6 |
| 8 | STX | 希捷 / Seagate | Technology / Data Storage (HDD) | ~$113B | Alpha#1, Alpha#41 | $837.23 放量 +5% 创高，+204% YTD；FQ1 指引 $4.1B 超预期，"80% 的 hyperscale 数据存于 HDD"（AI 推理/agentic AI 海量存储需求）；典型价高于 VWAP | 8.5 |
| 9 | JPM | 摩根大通 / JPMorgan | Financials / Diversified Bank | ~$1.0T | Alpha#1, Alpha#53 | 最新季 EPS $6.14 超预期、营收 $58.02B (+27.7%)，离 12 个月新高 $366.50 仅 ~3%（$356）；$50B 回购 + 股息 +10%；金融板块资金流入 45 周连胜中的主力 | 8.4 |
| 10 | ALAB | Astera Labs / Astera Labs | Technology / AI Connectivity | ~$49B | Alpha#1, Alpha#12 | 周五 $310.40 放 +9.75%（盘中高 $321.65），AI 集群互联（PCIe/CXL）需求受大厂 capex 直接驱动；Alpha#12 确认放量突破 | 8.3 |
| 11 | CRWD | CrowdStrike / CrowdStrike | Technology / Cybersecurity | ~$160B | Alpha#1, Alpha#19 | +83.4% YTD，8 月从 $227→$189 回撤后强力反弹（均值回复确认）；网络安全 = AI 基建的经常性收入层；Navellier 最高因子评分队列；注意 9/4 软件板块普跌的短期外溢 | 8.2 |
| 12 | HOOD | 罗宾汉 / Robinhood Markets | Financials / Fintech-Brokerage | ~$185B | Alpha#1, Alpha#12 | 9/3 +16.6%、1 月 +34.4%，零售交易 + 加密热度共振；Alpha#1 动量 + Alpha#12 放量确认；YTD +10.3% 且处于资金流入拐点 | 8.1 |
| 13 | AEM | 阿格尼克鹰矿 / Agnico Eagle | Basic Materials / Gold | ~$95B | Alpha#53, Alpha#41 | 记录季 FCF $1.34B，实际售价 $4,483 vs AISC $1,459（创纪录价差）；9/3 +5.04%；9 日收盘位置抬升、典型价高于 VWAP；EV/EBITDA ~10x，矿区集中于加拿大/澳洲/芬兰等稳定法域 | 8.0 |
| 14 | PSX | 菲利普斯 66 / Phillips 66 | Energy / Refining | $100.6B | Alpha#41, Alpha#1 | $254.66 创新高，+80% YTD；炼油利用率行业领先 + 中游 NGL 分馏量创纪录 + 重质原油（委内瑞拉）加工期权；债务快速下降，净化平衡表 | 8.0 |
| 15 | CEG | 星座能源 / Constellation Energy | Utilities / Nuclear Power | ~$110B | Alpha#1, Alpha#41 | AI 数据中心电力瓶颈受益方，GS 点名 "谁从 AI capex 赚到回报" 的首批 Infra 标的；Utility 板块 RRG 由 Improving 向 Leading 过渡，资金轮入；典型价高于 VWAP | 8.0 |
| 16 | WDC | 西部数据 / Western Digital | Technology / Data Storage (HDD) | ~$90B | Alpha#1, Alpha#41 | 周五 +4~6% 至 ~$460，+168% YTD 创新高；HDD 平均售价环比高双位数上行，agentic AI 驱动高容量存储需求（管理层定性）；分析师上行空间 ~+45% | 8.0 |

### 第三梯队：综合评分 7.0-7.9

| 排名 | 代码 | 公司名称 | 板块 | 市值(估) | 核心因子 | 因子信号解读 | 综合评分 |
|------|------|----------|------|----------|----------|-------------|----------|
| 17 | ORCL | 甲骨文 / Oracle | Technology / Cloud & AI | ~$500B | Alpha#19, Alpha#41 | YTD -20.2% 深度回撤后 9/3 放量反弹 +5.7% → 均值回复启动；AI 云/RSC 大单管线为 9/10 财报催化剂（Q1 财报临近）；典型价首度回到 VWAP 上方 | 7.8 |
| 18 | CRM | 赛富时 / Salesforce | Technology / Software | ~$380B | Alpha#1, Alpha#12 | 1 月 +37%、Agentforce ARR $1.5B（9/3 +3.07%）——企业软件 "SaaSpocalypse" 反转；接近新高处量价配合；但 9/4 软件板块普跌带来短期波动 | 7.6 |
| 19 | COIN | Coinbase / Coinbase（美国加密货币交易所） | Financials / Crypto Exchange | ~$90B | Alpha#1, Alpha#12 | 9/3 +10.1%、1 月 +28.6%（BTC 9/3 破 $81K、9/4 回落至 ~$79.7K）；量价共振但 YTD -14.8% 仍处前高下方 → Alpha#12 确认、Alpha#19 未完成，仓位需留冲高回落余地 | 7.5 |
| 20 | MRNA | 莫德纳 / Moderna | Healthcare / Biotech | ~$60B | Alpha#1, Alpha#19(反向) | 1 月 +164.6%、YTD +404.8%，Alpha#1 动量极强，但距均值回归压力极大（Alpha#19 给出反向警告）——典型"高动量 + 高反转风险"矛盾标的，仅适合小仓位趋势跟踪 | 7.2 |

---

## Top 20 排名总表

| 排名 | 代码 | 公司名称（中/英） | 板块 | 市值(估) | 核心因子 | 综合评分 |
|------|------|-------------------|------|----------|----------|----------|
| 1 | NVDA | 英伟达 / NVIDIA | Technology | $4.56T | Alpha#1, Alpha#41 | 9.2 |
| 2 | MU | 美光 / Micron | Technology | ~$236B | Alpha#1, Alpha#12 | 9.1 |
| 3 | MPC | 马拉松石油 / Marathon Petroleum | Energy | ~$132B | Alpha#41, Alpha#1 | 9.0 |
| 4 | NEM | 纽蒙特 / Newmont | Materials | ~$145B | Alpha#53, Alpha#1 | 9.0 |
| 5 | SNDK | 闪迪 / SanDisk | Technology | ~$190B | Alpha#1, Alpha#30 | 8.9 |
| 6 | MS | 摩根士丹利 / Morgan Stanley | Financials | ~$330B | Alpha#1, Alpha#41 | 8.7 |
| 7 | GS | 高盛 / Goldman Sachs | Financials | ~$350B | Alpha#1, Alpha#53 | 8.6 |
| 8 | STX | 希捷 / Seagate | Technology | ~$113B | Alpha#1, Alpha#41 | 8.5 |
| 9 | JPM | 摩根大通 / JPMorgan | Financials | ~$1.0T | Alpha#1, Alpha#53 | 8.4 |
| 10 | ALAB | Astera Labs / Astera Labs | Technology | ~$49B | Alpha#1, Alpha#12 | 8.3 |
| 11 | CRWD | CrowdStrike / CrowdStrike | Technology | ~$160B | Alpha#1, Alpha#19 | 8.2 |
| 12 | HOOD | 罗宾汉 / Robinhood | Financials | ~$185B | Alpha#1, Alpha#12 | 8.1 |
| 13 | AEM | 阿格尼克鹰矿 / Agnico Eagle | Materials | ~$95B | Alpha#53, Alpha#41 | 8.0 |
| 14 | PSX | 菲利普斯 66 / Phillips 66 | Energy | $100.6B | Alpha#41, Alpha#1 | 8.0 |
| 15 | CEG | 星座能源 / Constellation Energy | Utilities | ~$110B | Alpha#1, Alpha#41 | 8.0 |
| 16 | WDC | 西部数据 / Western Digital | Technology | ~$90B | Alpha#1, Alpha#41 | 8.0 |
| 17 | ORCL | 甲骨文 / Oracle | Technology | ~$500B | Alpha#19, Alpha#41 | 7.8 |
| 18 | CRM | 赛富时 / Salesforce | Technology | ~$380B | Alpha#1, Alpha#12 | 7.6 |
| 19 | COIN | Coinbase / Coinbase | Financials | ~$90B | Alpha#1, Alpha#12 | 7.5 |
| 20 | MRNA | 莫德纳 / Moderna | Healthcare | ~$60B | Alpha#1, Alpha#19 | 7.2 |

---

## 按板块分类汇总

### Technology（9 只）
NVDA, MU, SNDK, STX, ALAB, WDC, CRWD, ORCL, CRM

**板块逻辑：** 本日最强主线为**存储/内存超级周期**（MU/SNDK/STX/WDC/ALAB 全线上涨，DRAM ETF +6.6%）——NAND/DRAM 合约价 QoQ +50~60%、先进制程售罄到 2026 底、HDD 承载 ~80% hyperscale 数据，AI capex 从"建算力"转向"存数据"。Alpha#1 动量 + Alpha#12 量价确认集中在这条链。软件端（CRWD/ORCL/CRM）分化明显：网络安全与总账软件维持动量，但 9/4 软件板块普跌（PLTR -3~4%、ASAN/WDAY/SNOW 领跌）提示"硬件 > 软件"结构仍在延续，软件仓位应低于硬件。

### Financials（5 只）
MS, GS, JPM, HOOD, COIN

**板块逻辑：** 金融是 RRG 核心 Leading 象限（XLF 9/3 +1.56% 全板块最强），投行（MS/GS）受益于资本市场的重新开放（权益承销 +130%、IB 管道扩张）+ 创纪录交易收入；JPM 基本面全美最强（EPS 连续 beat + $50B 回购）；HOOD/COIN 为资金流 + 加密热度的镜像敞口。风险：10Y ~4.8% 的利率上冲会在单日反向冲击（9/4 已演示）。

### Basic Materials - Gold（2 只）
NEM, AEM

**板块逻辑：** "Debasement Trade" 主线——美国国债破 $40T、财政赤字 ~$2T、央行年购金 ~1,000 吨（4 年连购），金价 $4,400-4,509/oz 逼近纪录，Citi 看 $5,000（2027 底）。矿商经营杠杆：NEM 实际售价 $4,414 vs AISC $1,621、AEM $4,483 vs $1,459，价差仍处历史极宽。Alpha#53（收盘位置抬升）在两只标的上均确认。风险：金价 -13% 级别的回撤（4-6 月已发生一次）将快速压缩利润。

### Energy - Refining（2 只）
MPC, PSX

**板块逻辑：** WTI 3-2-1 crack spread ~$9/bbl（1 月的 3 倍），全球炼能结构性紧张（2020-23 关停潮）+ 霍尔木兹地缘扰动 + 出口需求，三大独立炼厂 Q2 合计利润 $12.6B（2022 年以来最高）。MPC/PSX/VLO 全线创纪录新高，YTD >80%。Alpha#41（价格持续高于 VWAP）+ Alpha#1 动量双重确认。风险：crack spread 压缩（需求衰退或新产能）、估值（MPC 高于分析师 fair value）。

### Utilities（1 只）
CEG

**板块逻辑：** AI 电力瓶颈的最直接受益方；Utility 板块 RRG 位于 Improving 区间、资金轮入中。属于"AI capex 变现"第二阶段标的（GS 框架），替代上一期防御型 JNJ/LLY 的仓位。

### Healthcare（1 只）
MRNA

**板块逻辑：** 动量旗舰但风险提示最重——1 月 +164.6%/YTD +404.8% 背后是疫苗/肿瘤管线叙事，Alpha#1 极强同时 Alpha#19 均值回复风险极高，与板块内 UNH/LLY 的防御定位完全不同。仅适合趋势跟踪小仓位。

---

## 与上期报告对比（轮动信号）

| 维度 | 2026-09-04 报告（9/3 收盘） | 2026-09-05 报告（9/4 收盘） |
|------|----------------------------|----------------------------|
| 主导板块 | 能源（CVX/XOM）+ 防御（JNJ/LLY） | 存储/半导体 + 金融 + 炼油 + 黄金 |
| Top 定调 | NVDA(9.5) 独大，价值轮动 | NVDA(9.2) 领跑但 MU(9.1) 逼近，硬件链共振 |
| 行业配置 | 科技/AI×7、能源×4、医疗×3、金融×4 | 科技×9、金融×5、能源×2、黄金×2、其他×2 |
| 更替 | — | 移出 CVX/XOM/JNJ/UNH/LLY/AVGO/META/MSFT/AAPL/DELL；新入 MU(↑至一级)/SNDK/STX/ALAB/WDC/AEM/CEG/COIN/MRNA/HOOD |

---

## 风险提示

1. **利率风险是本日最大逆风**：8 月非农 +162k → 9 月加息概率 57~60%，2Y 4.37% 创新高。高估值成长股（尤其软件/长久期）对利率上冲高度敏感，9/4 已有演示
2. **存储周期拥挤度**：SNDK +555%/STX +204%/WDC +168% YTD，正处历史性拥挤交易；周期拐点（NAND 合约价见顶、内存 ETF 跌破 $58）将触发同级别反向回撤（8 月初已出现一次 -6~7% 单日）
3. **"Hardware > Software" 持续性**：SOXX YTD +70% vs IGV +4% 的剪刀差不会永远扩大；9/4 软件普跌可视为 AI 交易内部再平衡的开始，软件侧仅保留高质量经常性收入标的
4. **9 月季节性（September Effect）**：1928 年以来 S&P 9 月平均 -1.1%；Mag7 占标普 ~34% 的集中度放大去杠杆时点的回撤幅度
5. **金矿经营杠杆双刃剑**：金价 -13% 级别的回撤即可压缩矿商利润（4-6 月已发生）；AEM capex 指引上调至 $2.6-2.8B
6. **炼化估值风险**：MPC 已高于分析师 fair value（$324 vs $387），crack spread 一旦压缩回撤剧烈
7. **单因子与数据局限**：本报告因子值为行情快照的定性重构（非全量 OHLCV 计算），市值部分为估算；应结合基本面与宏观独立判断，不可作为唯一决策依据

> ⚠️ 免责声明：本报告仅为基于 WorldQuant 101 因子框架的量化分析研究，不构成任何投资建议。投资有风险，决策需谨慎。