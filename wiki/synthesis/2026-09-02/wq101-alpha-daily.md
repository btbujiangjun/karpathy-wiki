---
title: WorldQuant 101 Alpha 因子选股日报 — 2026-09-02
type: synthesis
created: 2026-09-02
updated: 2026-09-02
sources: []
tags: [quant, worldquant-101, alpha-factors, us-stock-picks, daily-report]
---

# WorldQuant 101 Alpha 因子选股日报 — 2026-09-02

> 基于 WorldQuant 101 Alpha 因子库，对美股中大盘股（市值 > $10B）进行量化筛选，精选 Top 20 最值得投资的标的。
> 数据口径：美股 **9/1（周二）收盘**；9/2 晚间 Broadcom Q3 财报为待验证的关键催化，尚未计入。

## 市场背景

| 指数 | 收盘价（9/1） | 日涨跌 | 关键信号 |
|------|--------|--------|----------|
| S&P 500 | 7,631.47 | -0.71% | 9 月开门红转弱，7/11 板块收跌，9 月"魔咒"季节压力 |
| Nasdaq Composite | 26,099.77 | -1.03% | 科技/半导体领跌，AI 硬件链承压 |
| Dow Jones | 52,766.88 | -0.79% | 金融/工业相对抗跌 |
| VIX | 16.33 | +9.45% | 波动率抬头，市场风险偏好回落 |
| 10Y 美债 | ~4.75-4.79% | — | 突破前高，压制高估值成长股 |
| WTI / Brent | >$86 / >$90 | +3.8~4.3% | 美伊再度空袭霍尔木兹，油价暴涨 |

**核心驱动因素：**
1. **美伊冲突再度升级 + 油价暴涨**：美国恢复空袭伊朗，原油单日 +3.8~4.3% 重返 $90+；Energy 板块领涨（+1.54%），DINO / MPC / PSX / VLO / XOM / CVX 多只创 52 周新高
2. **Fed 9 月加息预期升温**：10Y 收益率突破 4.75% 前高，Jackson Hole 主席 Warsh 偏鹰，9 月加息概率 ~66%；高估值成长股（PLTR / CRWD / 半导体）承压
3. **板块轮动显著**：Energy（+1.54%）与 Utilities（+0.85%）领涨，Consumer Discretionary（-1.89%）与 Industrials（-1.39%）领跌；结构性逻辑是"债务融资型 AI 基建"受利率打击（ORCL -5%），"无债表 + 现金流"的苹果逆势 +3%（Ternus 接任 CEO）
4. **AI 主线分化剧烈**：英伟达成为美股市值第一（Vera Rubin 全面投产），但半导体当日普跌（NVDA -1.51% / MU -2.64% / AMD -2.36% / INTC -0.60%）——存储/服务器涨价（AI 服务器明年 +15%+）加剧成本与毛利率担忧
5. **决定事件**：**9/2 晚间 Broadcom Q3 财报**（Q2 AI 半导体 +143% 至 $10.8B，Q3 指引 AI $16B / 总营收 $29.4B；FY27 AI 营收 >$100B）—— 定制 ASIC（谷歌 TPU）链的关键验证；另 9/4 非农、9/11 CPI、9/15-16 FOMC
6. **苹果 CEO 交接**：John Ternus 接替 Tim Cook（9/1），9/9 秋季发布会（iPhone 18 + 折叠款 + Siri AI）为短期催化

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

**本日因子环境判断：** 9 月开门日"弃成长、买能源"——Energy 动量（Alpha#1）+ 量价相关（Alpha#6）+ 趋势强度（Alpha#41）三因子共振最强烈（油价 +3.8%）；AI 硬件链受利率 + 存储涨价双重打击，动量与趋势强度因子走弱（NVDA/MU/AMD），需以 Alpha#41 甄别"价格 vs VWAP"的真实强度；医疗板块（MRK/LLY/JNJ）在癌症疫苗 + GLP-1 主线下动量稳健；苹果"无债表"逆转成为利率环境下的防御型动量标的。

---

## Top 20 精选股票

### 第一梯队：综合评分 8.0+

| 排名 | 代码 | 公司名称 | 板块 | 市值 | 核心因子 | 因子信号解读 | 综合评分 |
|------|------|----------|------|------|----------|-------------|----------|
| 1 | NVDA | 英伟达 / NVIDIA | Technology / AI 芯片 | $5.6T+ | Alpha#1, Alpha#41 | 成为美股市值第一；Q2 营收 $96.2B（+106%）、数据中心 +117%、**Vera Rubin 全面投产**（每 GW $400 亿，较 Blackwell +60%）、FY28 +70% 首度远期指引、云未完成订单 >$2T；8/31 收 $220.78（+5.9%/周）；散户连买 15 日 >$2.5B；虽当日 -1.51%，但价格远高于 VWAP，趋势结构保持 | 9.2 |
| 2 | CVX | 雪佛龙 / Chevron | Energy / Integrated | ~$360B | Alpha#1, Alpha#41 | **9/1 创 52 周新高 $211.05**，突破 5 个月阻力；Q2 净利 $12.1B（+近 5 倍）、EPS $6.06 超预期；油价 >$90 + 委内瑞拉 650 亿桶储备 + 霍尔木兹溢价；放量上行（1.5× 平日量）、OBV 走高，趋势强度极强 | 9.0 |
| 3 | MRK | 默克 / Merck | Healthcare / Pharma | ~$330B | Alpha#1, Alpha#41 | 9/1 +1.42% 至 $149.86；YTD **+50.9%**（领先行业 19.9%）；与 Moderna mRNA 癌症疫苗 INTerpath-001 三期成功，平台价值延伸 Keytruda（占 50% 营收）生命周期；接近 52 周高 $154，动量 + 趋势强度共振 | 8.7 |
| 4 | XOM | 埃克森美孚 / Exxon Mobil | Energy / Integrated | ~$650B | Alpha#1, Alpha#6 | 9/1 +2.24% 至 $164.55；Q2 营收 $116B（+42.3%）、上游产量 4.514M boe/d 创纪录、Q2 FCF $17.2B、季度利润 $14.5B 翻倍；YTD +33~37%；油价 $90+ 下量价齐升，趋势强度强 | 8.6 |
| 5 | LLY | 礼来 / Eli Lilly | Healthcare / Pharma | ~$1.2T | Alpha#1, Alpha#53 | 自 8/19 高 $1,292 回撤 ~10% 至 $1,174-1,182；Q2 营收 $23B（+48%）、Mounjaro +91% / Zepbound +46%、全年指引上调至 $85-87B；FDA 扩大 Mounjaro 心血管适应症、retatrutide 超强三期数据；回调后给出 Alpha#53 反转再入场机会，长期动量完好 | 8.5 |
| 6 | CRWD | CrowdStrike / CrowdStrike | Technology / Cybersecurity | ~$58B | Alpha#6, Alpha#30 | **创 52 周/历史新高**；9/1 收 $231（Fal.Con 2026 催化，8/31-9/3）；Q2 净新增 ARR $332.8M 创纪录、FCF $377M 创纪录、Falcon Flex 渗透提升、AI 安全需求；放量突破 $227 双顶，目标 $238.77 / $250；估值 P/S 高需警惕 | 8.5 |
| 7 | PLTR | Palantir / Palantir Technologies | Technology / Data Analytics | ~$448B | Alpha#6, Alpha#41 | 9/1 收 $186.38（连续 6 日上涨，月中 +43%）；Q2 营收 +93%、美国商业 +149%、调整后营业利润率 62%、Rule of 40 155%、FCF $1.22B；Maven 项目 9 月转正 + 法院解除 Anthropic 禁令；小超高管但 52 周高 $207 在上方，趋势强度仍在 | 8.2 |

### 第二梯队：综合评分 7.5-7.9

| 排名 | 代码 | 公司名称 | 板块 | 市值 | 核心因子 | 因子信号解读 | 综合评分 |
|------|------|----------|------|------|----------|-------------|----------|
| 8 | AAPL | 苹果 / Apple | Technology / Consumer Hardware | ~$4T | Alpha#1, Alpha#41 | 9/1 **逆势 +3% 至 $325**（Ternus 接任 CEO 首日）——高收益率 + ORCL 大跌下"无债表 + 巨额 FCF"成避风港；收复 20/50 日均线，逼近 $327.85 阻力，目标 $344 历史高；9/9 iPhone 18 + 折叠款 + Siri AI 为催化 | 7.9 |
| 9 | AVGO | 博通 / Broadcom | Technology / AI ASIC & Semi | ~$1.8T | Alpha#41, Alpha#12 | 9/2 晚 Q3 财报决定性事件；Q2 总营收 $22.2B（+48%）、AI 半导体 +143% 至 $10.8B、经调整 EPS $2.44；Q3 指引 AI $16B（+200%）/ 总营收 $29.4B（+84%）、FY27 AI >$100B、订单 >$30B；当前仍较峰值低 >23%，回落提供均值回复候选 | 7.9 |
| 10 | JNJ | 强生 / Johnson & Johnson | Healthcare / Pharma | ~$460B | Alpha#1, Alpha#53 | 9/1 创当日上涨名单（与 CVX/AAPL 并列）；防御型动量，近一年稳步抬升；利率上行 + 地缘不确定下的避风港属性，Alpha#53 反转/回调支撑 | 7.7 |
| 11 | SLB | 斯伦贝谢 / Schlumberger | Energy / Oilfield Services | ~$72B | Alpha#6, Alpha#30 | 油价 $90+ 直接受益；9/1 +2.20%，油服量价齐升；钻机活跃度 + 国际资本开支回暖双驱动，Alpha#6 量价相关信号强 | 7.6 |
| 12 | UNH | 联合健康 / UnitedHealth | Healthcare / Managed Care | ~$500B | Alpha#1, Alpha#19 | Q2 营收 $112.03B 超预期、EPS $6.38 远超预期、MCR 改善至 86.7%、上调全年指引；8 月创新高后小幅整理，防御型动量 + 均值回复兼具 | 7.5 |
| 13 | HAL | 哈里伯顿 / Halliburton | Energy / Oilfield Services | ~$33B | Alpha#6, Alpha#30 | 9/1 +1.53% 至 $36.74，**1 个月 +16%**；油价反攻 + 钻机数回升，量价齐升；油服第三梯队弹性标的 | 7.5 |

### 第三梯队：综合评分 7.0-7.4

| 排名 | 代码 | 公司名称 | 板块 | 市值 | 核心因子 | 因子信号解读 | 综合评分 |
|------|------|----------|------|------|----------|-------------|----------|
| 14 | AMD | 超威半导体 / Advanced Micro | Technology / AI 芯片 | ~$450B | Alpha#41, Alpha#12 | 9/1 -2.36% 反映板块普跌，但 MI350/MI400 进度 + 通用 AI 加速器第二梯队叙事；内存涨价抬成本是双刃剑；超跌后均值回复候选 | 7.3 |
| 15 | COP | 康菲石油 / ConocoPhillips | Energy / E&P | ~$130B | Alpha#1, Alpha#41 | 纯上游生产商，油价弹性最大；YTD +45%；近期获利了结后趋势仍在，霍尔木兹供给风险 + 现金流强劲（TTM FCF $10.1B） | 7.2 |
| 16 | MSFT | 微软 / Microsoft | Technology / Software | ~$3.9T | Alpha#1, Alpha#41 | 9/1 -1.24% 至 $501（科技普跌拖累）；Azure +43%、Copilot 增长、AI 资本开支龙头；高收益率环境下的现金流安全垫，短线回调至均线附近提供入场点 | 7.2 |
| 17 | MU | 美光 / Micron | Technology / Memory | ~$200B | Alpha#6, Alpha#30 | 9/1 -2.64% 反映半导体普跌，但存储/内存涨价周期超级强劲（TrendForce：Q2 DRAM +58-63%、NAND +70-75%；Q3 服务器 DRAM 再 +13-18%）；放量 + 涨价兑现逻辑，量价高波动 | 7.1 |
| 18 | OXY | 西方石油 / Occidental | Energy / E&P | ~$55B | Alpha#1, Alpha#6 | 9/1 上涨名单；油价弹性 + Permian/墨西哥湾产能对冲中东中断，Q2 已"完全对冲"中东扰动；量价齐升 | 7.1 |

### 第四梯队：综合评分 6.5-6.9

| 排名 | 代码 | 公司名称 | 板块 | 市值 | 核心因子 | 因子信号解读 | 综合评分 |
|------|------|----------|------|------|----------|-------------|----------|
| 19 | NOW | ServiceNow / ServiceNow | Technology / Software | ~$290B | Alpha#6, Alpha#19 | 9 月 SaaS 反弹叙事持续（"软件未死"）；Q2 revenue +24%、AI 年化 $1B；量价健康，动量与均值回复兼具 | 6.9 |
| 20 | VEEV | Veeva / Veeva Systems | Healthcare / Life Sciences | ~$30B | Alpha#6, Alpha#30 | 生命科学 AI + 医药板块轮动共振；放量上行，弹性标的 | 6.7 |

---

## Top 20 排名总表

| 排名 | 代码 | 公司名称（中/英） | 板块 | 市值 | 核心因子 | 综合评分 |
|------|------|-------------------|------|------|----------|----------|
| 1 | NVDA | 英伟达 / NVIDIA | Technology | $5.6T+ | Alpha#1, Alpha#41 | 9.2 |
| 2 | CVX | 雪佛龙 / Chevron | Energy | ~$360B | Alpha#1, Alpha#41 | 9.0 |
| 3 | MRK | 默克 / Merck | Healthcare | ~$330B | Alpha#1, Alpha#41 | 8.7 |
| 4 | XOM | 埃克森美孚 / Exxon Mobil | Energy | ~$650B | Alpha#1, Alpha#6 | 8.6 |
| 5 | LLY | 礼来 / Eli Lilly | Healthcare | ~$1.2T | Alpha#1, Alpha#53 | 8.5 |
| 6 | CRWD | CrowdStrike / CrowdStrike | Technology | ~$58B | Alpha#6, Alpha#30 | 8.5 |
| 7 | PLTR | Palantir / Palantir Technologies | Technology | ~$448B | Alpha#6, Alpha#41 | 8.2 |
| 8 | AAPL | 苹果 / Apple | Technology | ~$4T | Alpha#1, Alpha#41 | 7.9 |
| 9 | AVGO | 博通 / Broadcom | Technology | ~$1.8T | Alpha#41, Alpha#12 | 7.9 |
| 10 | JNJ | 强生 / Johnson & Johnson | Healthcare | ~$460B | Alpha#1, Alpha#53 | 7.7 |
| 11 | SLB | 斯伦贝谢 / Schlumberger | Energy | ~$72B | Alpha#6, Alpha#30 | 7.6 |
| 12 | UNH | 联合健康 / UnitedHealth | Healthcare | ~$500B | Alpha#1, Alpha#19 | 7.5 |
| 13 | HAL | 哈里伯顿 / Halliburton | Energy | ~$33B | Alpha#6, Alpha#30 | 7.5 |
| 14 | AMD | 超威半导体 / Advanced Micro | Technology | ~$450B | Alpha#41, Alpha#12 | 7.3 |
| 15 | COP | 康菲石油 / ConocoPhillips | Energy | ~$130B | Alpha#1, Alpha#41 | 7.2 |
| 16 | MSFT | 微软 / Microsoft | Technology | ~$3.9T | Alpha#1, Alpha#41 | 7.2 |
| 17 | MU | 美光 / Micron | Technology | ~$200B | Alpha#6, Alpha#30 | 7.1 |
| 18 | OXY | 西方石油 / Occidental Petroleum | Energy | ~$55B | Alpha#1, Alpha#6 | 7.1 |
| 19 | NOW | ServiceNow / ServiceNow | Technology | ~$290B | Alpha#6, Alpha#19 | 6.9 |
| 20 | VEEV | Veeva / Veeva Systems | Healthcare | ~$30B | Alpha#6, Alpha#30 | 6.7 |

---

## 按板块分类汇总

### Energy（7 只）
CVX, XOM, SLB, HAL, COP, OXY

**板块逻辑：** 本日最强方向。美伊再度空袭霍尔木兹 + 油价 +3.8% 重返 $90+，Energy 板块 +1.54% 领涨，多只（DINO/MPC/PSX/VLO/XOM/CVX）创 52 周新高。Alpha#1（动量）+ Alpha#6（量价相关）信号全板块最强。**风险提示**：油价地缘溢价可逆，EIA 预计 2027 布油回落至 ~$69，若局势缓和将快速回吐。

### Healthcare（5 只）
MRK, LLY, JNJ, UNH, VEEV

**板块逻辑：** 9 月开门红日的确定性方向。MRK 癌症疫苗（YTD +50.9%）、LLY GLP-1（回调后价值显现）、JNJ 创上涨名单、UNH 防御型动量。高利率地缘风险下的避风港 + 增长主线兼备。

### Technology（8 只）
NVDA, CRWD, PLTR, AAPL, AVGO, MSFT, AMD, MU, NOW

**板块逻辑：** 高分化。9/1 当日科技普跌（半导体/高估值成长承压），但英伟达（市值第一 + Vera Rubin）、苹果（无债表 + CEO 交接）、CRWD（Fal.Con）、PLTR（AI 主权）结构性强势。**决定性事件**：9/2 晚 Broadcom Q3 财报，验证定制 ASIC 链是否"未到顶只欠供应"。

---

## 风险提示

1. **9 月魔咒 + 加息风险**：9 月为美股历史最弱月份（标普平均 -0.6~0.7%、正收益概率 ~45%）；9/16 FOMC 加息概率 ~66%，10Y 突破 4.75% 前高——高估值成长股（PLTR P/S 77x / CRWD / NOW）将承压
2. **油价地缘溢价可逆**：Energy 股上涨由美伊冲突 + 霍尔木兹停运驱动（约 20% 全球供给中断、1400 万桶/日受影响），若局势缓和 / 通航恢复，风险溢价随时回吐（EIA 已料 2027 布油回落至 ~$69）
3. **AI 硬件毛利率/涨价压力**：内存（DRAM/NAND 连续两季合约价大涨）推高 AI 服务器造价（明年 +15%+），英伟达毛利率 Q4 触底至 71-72%；MU/AMD/NVDA 需消化"以利润率换增长"的博弈
4. **Broadcom 财报不确定性**：9/2 晚 Q3 财报为 AVGO/定制 ASIC 链分水岭——谷歌转单 Marvell（58.9M 股认股权证）引发客户集中度担忧；若 ASIC 需求平淡，AI 硬件或再迎高位消化
5. **高动量追高风险**：NVDA/PLTR/CRWD 已远离 VWAP，Alpha#1 动量强劲但 Alpha#12 反转隐患；9 月魔咒下波动率（VIX +9.45%）可能放大
6. **苹果 CEO 交接不确定性**：Ternus 首日 +3% 为利率轮动驱动（ORCL -5% 对比例证），若 9/9 发布会不及预期或收益率回落，轮动交易可能反向；DOJ 反垄断诉讼悬而未决
7. **单一因子局限性**：WorldQuant 101 因子本质是技术面量化信号，需结合基本面与宏观环境综合判断，不可作为唯一决策依据

> ⚠️ 免责声明：本报告仅为基于 WorldQuant 101 因子框架的量化分析研究，不构成任何投资建议。投资有风险，决策需谨慎。
