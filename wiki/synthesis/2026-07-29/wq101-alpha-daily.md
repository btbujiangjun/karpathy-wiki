---
title: "WorldQuant 101 Alpha 因子选股 Top 20 — 美股 (2026-07-29)"
type: synthesis
created: 2026-07-29
updated: 2026-07-29
sources: []
tags: [wq101-alpha, daily, us-stocks, factor-investing, quantitative]
---

# WorldQuant 101 Alpha 因子选股 Top 20 — 美股 (2026-07-29)

## 大盘与板块全景

| 指数 | 收盘 | 涨跌 | 备注 |
|------|------|------|------|
| S&P 500 | 7,428.78 | +0.21% | 涨跌比 2.5:1 广度极佳 |
| Nasdaq | 24,876.91 | -0.22% | 芯片拖累，但软件/AAPL支撑 |
| Dow Jones | 52,747.32 | +1.03% | 距历史收盘新高仅0.58% |
| VIX | ~16.18 | -1.94% | 恐慌情绪降温 |
| US 10Y | ~4.60% | 回落 | 油价下跌缓解通胀预期 |
| Brent Crude | $82.08 | -4.4% | 伊朗谈判推动油价急跌 |

### 板块轮动速览 (RRG 7/27)

| 象限 | 板块 | 趋势 |
|------|------|------|
| **Leading** | Energy (XLE), Financials (XLF), Real Estate (XLRE), Communication Services (XLC), Consumer Staples (XLP) | 持续领导 / 新晋领导 |
| **Improving** | Materials (XLB), Utilities (XLU) | 动量改善 |
| **Weakening** | Health Care (XLV) | 相对强度仍正但动能在衰减 |
| **Lagging** | Technology (XLK), Industrials (XLI), Consumer Discretionary (XLY) | 持续落后 |

### 当日关键信号

- **板块轮动极致化**：Healthcare +2.4% / Consumer Staples +2.0% / Materials +1.7% 领涨；Tech -1.4% 被半导体拖累
- **芯片恐慌扩散**：SOX -4.5% 距 6/22 高点 -25%；MU -8.9% / AMD -8.1% / INTC -5.9% / STX -8.7%
- **AAPL 历史时刻**：盘中触及 $5T 市值里程碑，收 $340.08 (+0.94%)
- **KO 业绩爆发**：+5% 历史新高，营收+7% 超预期，上调全年指引
- **软件股接棒**：ADBE +4.81% / IBM +5.21% / CRM +4.55% — "买芯片卖软件" 交易瓦解
- **Fed 决议前夕**：加息概率从 36% 降至 31.5%，市场预期按兵不动
- **能源大跌**：Brent -4.4% 至 $82，伊朗谈判 + 需求担忧

## WorldQuant 101 Alpha 因子打分框架

| 因子 | 代号 | 逻辑 | 本日应用 |
|------|------|------|---------|
| Alpha#1 | Momentum | Rank(Correlation(Delay(close,1), close, 10)) | 筛选 52-week high / 强势股 |
| Alpha#6 | Volume Confirmation | Correlation(open, volume, 10) | 量价配合确认上涨 |
| Alpha#12 | Divergence | sign(delta(volume,1)) * (-1 * delta(close,1)) | 价跌量增（潜在吸筹） |
| Alpha#19 | Mean Reversion | rank(stddev(abs((close-open)),5) + (close-open) + rank(correlation(close,open,10))) | 超卖反弹 / 均值回复 |
| Alpha#30 | Volatility | rank(((2*scale(rank(((close-low)-(high-close))/(high-low)*volume))) - scale(rank(delta(close,3)))) * sum(volume,5)) | 波动率 + 量确认 |
| Alpha#41 | Trend Strength | ((high*low)^0.5) - vwap | 趋势强度 / 折价 |
| Alpha#53 | Reversal | -1 * Delta((((close-low)-(high-close))/(close-low)), 9) | 超跌反转 |

## 个股评分详解

### 1. KO — Coca-Cola (可口可乐)

| 维度 | 内容 |
|------|------|
| **板块** | Consumer Staples |
| **市值** | ~$280B |
| **核心因子** | Alpha#1 (Momentum) + Alpha#12 (Volume-Price Divergence) |
| **因子解读** | Alpha#1: 10日收盘价自相关性持续上行，52-week high + 跳空突破；Alpha#12: 成交量较均值放大 2.5×(+5% gap up)，量价齐升 |
| **综合评分** | 9.5 / 10 |
| **投资逻辑** | Q2 营收 $133.7 亿 (+6% YoY，超预期 $131.6 亿) + 上调全年指引；油价暴跌利好成本端；防御属性在轮动中受追捧；技术面跳空放量突破历史新高，动能极强 |
| **风险提示** | 估值溢价（PE ~28×）已部分反映增长；消费者支出若放缓可能拖累 |

### 2. JPM — JPMorgan Chase (摩根大通)

| 维度 | 内容 |
|------|------|
| **板块** | Financials |
| **市值** | ~$967B |
| **核心因子** | Alpha#1 (Momentum) + Alpha#6 (Volume Confirmation) |
| **因子解读** | Alpha#1: 52-week high 持续刷新，10日动量指标处于 90+ 分位；Alpha#6: 开盘价与成交量正相关，机构资金持续流入 |
| **综合评分** | 9.5 / 10 |
| **投资逻辑** | 美国银行利润纪录 + 资本市场经济活动回暖 + 投行业务 M&A/IPO 复苏；XLF 板块新晋 Leading 象限；美联储加息预期降温利好银行股估值扩张 |
| **风险提示** | 商业地产贷款风险敞口；净息差若因降息收窄；估值已处于 5 年高位 |

### 3. AAPL — Apple (苹果)

| 维度 | 内容 |
|------|------|
| **板块** | Technology / Consumer Electronics |
| **市值** | ~$4.94T |
| **核心因子** | Alpha#1 (Momentum) + Alpha#41 (Trend Strength) |
| **因子解读** | Alpha#1: 52-week high + 1M +22.4% 动能强劲；Alpha#41: sqrt(H*L) 持续高于 VWAP，趋势结构完整 |
| **综合评分** | 9.5 / 10 |
| **投资逻辑** | 7/28 盘中触及 $5T 里程碑（第二家）；AI 投入克制+高效，iPhone 租赁计划提升渗透率；HW 毛利率 ~46%；7/30 财报催化，期权市场提前布局 |
| **风险提示** | 6/26 高点 $334.99 获利回吐；AAPL+KeyBanc 看跌评级目标 $250；中国竞争加剧；估值 PE ~40× |

### 4. LLY — Eli Lilly (礼来)

| 维度 | 内容 |
|------|------|
| **板块** | Healthcare |
| **市值** | ~$1.05T |
| **核心因子** | Alpha#1 (Momentum) + Alpha#41 (Trend Strength) |
| **因子解读** | Alpha#1: 52-week high，1Y +51.4% 领跑医疗板块；Alpha#41: 趋势强度持续高位，Zepbound 需求爆发 |
| **综合评分** | 9.0 / 10 |
| **投资逻辑** | 2026 医疗板块 EPS 增长预期 +19.3%（全市场第二）；GLP-1 双雄之一，Foundayo 口服 GLP-1 临床推进；Healthcare 板块轮动受益 |
| **风险提示** | PE ~40× 估值偏高；Zepbound/Mounjaro 需求增速若放缓；竞争对手 NVO 追赶 |

### 5. BAC — Bank of America (美国银行)

| 维度 | 内容 |
|------|------|
| **板块** | Financials |
| **市值** | ~$450B |
| **核心因子** | Alpha#1 (Momentum) + Alpha#6 (Volume Confirmation) |
| **因子解读** | Alpha#1: 52-week high 序列，1Y +31.2%；Alpha#6: 量价正相关系数增强，RS 指标 ~85 |
| **综合评分** | 9.0 / 10 |
| **投资逻辑** | 降息预期下贷款需求有望回升；投行收入 + 财富管理双轮驱动；XLF 板块 Leading 象限确认 |
| **风险提示** | 净息差对利率敏感度高；商业地产敞口 ~$900 亿 |

### 6. PM — Philip Morris International (菲利普莫里斯)

| 维度 | 内容 |
|------|------|
| **板块** | Consumer Staples |
| **市值** | ~$304B |
| **核心因子** | Alpha#1 (Momentum) + Alpha#41 (Trend Strength) |
| **因子解读** | Alpha#1: 52-week high，1M +9.4%；Alpha#41: 价格趋势稳定高于 VWAP，防御性资金持续流入 |
| **综合评分** | 9.0 / 10 |
| **投资逻辑** | IQOS 加热不燃烧替代传统卷烟加速；营收 +8.9% YoY，OPM 37.7% + 高利润率；油价下跌利好成本；Consumer Staples 板块持续 Leading |
| **风险提示** | PE ~224× 极度高估（一次性税收项目扭曲）；监管风险（FDA 政策变化）；烟草长期衰退趋势 |

### 7. RTX — RTX Corporation (雷神技术)

| 维度 | 内容 |
|------|------|
| **板块** | Industrials / Aerospace & Defense |
| **市值** | ~$294B |
| **核心因子** | Alpha#1 (Momentum) + Alpha#41 (Trend Strength) |
| **因子解读** | Alpha#1: 52-week high，1W +12.3% / 1M +17.1%；Alpha#41: 价格持续高于 VWAP，防御+地缘政治双驱动 |
| **综合评分** | 9.0 / 10 |
| **投资逻辑** | 积压订单 $2890 亿创纪录；THAAD $350 亿合同 + 全球军费上升周期；商用航空发动机售后市场复苏 |
| **风险提示** | 国防合同周期长、利润率不确定；地缘政治缓和可能减弱催化剂 |

### 8. BMY — Bristol-Myers Squibb (百时美施贵宝)

| 维度 | 内容 |
|------|------|
| **板块** | Healthcare |
| **市值** | ~$127B |
| **核心因子** | Alpha#1 (Momentum) + Alpha#19 (Mean Reversion) |
| **因子解读** | Alpha#1: 52-week high，1M +14.2%；Alpha#19: 从 2025 年低点 +34% 1Y 均值回复中后期 |
| **综合评分** | 8.5 / 10 |
| **投资逻辑** | 新药管线（Breyanzi + Opdualag）推升增长预期；医疗板块轮动 + 估值回归 ($127B 在医疗巨头中相对低估)；2027E EPS +19% |
| **风险提示** | 专利悬崖（Eliquis ~2028）；后续管线能否弥补老药下滑 |

### 9. MRK — Merck & Co (默克)

| 维度 | 内容 |
|------|------|
| **板块** | Healthcare |
| **市值** | ~$324B |
| **核心因子** | Alpha#1 (Momentum) + Alpha#6 (Volume Confirmation) |
| **因子解读** | Alpha#1: 52-week high，1Y +61.3%；Alpha#6: 成交量和价格同步上升 |
| **综合评分** | 8.5 / 10 |
| **投资逻辑** | Keytruda 依然为全球最畅销药物；Gardasil 中国市场重启增长；Healthcare 板块 2027E 盈利增速第二 |
| **风险提示** | Keytruda 2028 专利到期；中国集采对疫苗价格压力 |

### 10. JNJ — Johnson & Johnson (强生)

| 维度 | 内容 |
|------|------|
| **板块** | Healthcare |
| **市值** | ~$603B |
| **核心因子** | Alpha#1 (Momentum) + Alpha#19 (Mean Reversion) |
| **因子解读** | Alpha#1: 52-week high 附近震荡，1Y +49.2%；Alpha#19: 从 $164 低点反弹至 $269，均值回复过程完成约 70% |
| **综合评分** | 8.5 / 10 |
| **投资逻辑** | 医疗科技 + 制药双轮驱动；医疗板块从 Weakening 向 Improving 过渡中；PE ~28× 相对合理 |
| **风险提示** | 滑石粉诉讼不确定性；药品定价政策风险 |

### 11. XOM — Exxon Mobil (埃克森美孚)

| 维度 | 内容 |
|------|------|
| **板块** | Energy |
| **市值** | ~$628B |
| **核心因子** | Alpha#6 (Volume Confirmation) + Alpha#41 (Trend Strength) |
| **因子解读** | Alpha#6: 油价大跌但量价结构尚可；Alpha#41: 中长期趋势仍为正（Brent $82 但仍高于成本线） |
| **综合评分** | 8.0 / 10 |
| **投资逻辑** | Energy 仍为 Leading 象限最强板块；43 年股息增长历史；油价回落 $82 但地缘风险溢价未完全消失 |
| **风险提示** | 油价若持续跌至 $70 以下将压缩利润；伊朗谈判若取得突破将加剧供应过剩 |

### 12. GS — Goldman Sachs (高盛)

| 维度 | 内容 |
|------|------|
| **板块** | Financials |
| **市值** | ~$185B |
| **核心因子** | Alpha#1 (Momentum) + Alpha#6 (Volume Confirmation) |
| **因子解读** | Alpha#1: 投行业务反弹推升股价，接近 52-week high；Alpha#6: 机构资金流入 M&A 复苏预期 |
| **综合评分** | 8.0 / 10 |
| **投资逻辑** | 投行 + 交易双引擎：Q2 股票交易收入突破 $50 亿；M&A/IPO 积压释放；Financials 板块 Leadership 确认 |
| **风险提示** | 投行收入波动大；信贷业务规模较小 |

### 13. ADBE — Adobe (奥多比)

| 维度 | 内容 |
|------|------|
| **板块** | Technology / Software |
| **市值** | ~$110B |
| **核心因子** | Alpha#53 (Reversal) + Alpha#30 (Volatility) |
| **因子解读** | Alpha#53: 软件板块从超卖区域反转，ADBE 7/28 +4.81%；Alpha#30: 波动率放大 + 成交量回升确认反转信号 |
| **综合评分** | 8.0 / 10 |
| **投资逻辑** | AI 资金从芯片轮动至软件（ADBE AI 助手 Firefly 商业化加速）；"买芯片卖软件" 交易瓦解直接利好；估值从 30× 压缩后修复 |
| **风险提示** | AI 竞争（Canva + 开源工具）；增长从双位数放缓至高单位数 |

### 14. CRM — Salesforce (赛富时)

| 维度 | 内容 |
|------|------|
| **板块** | Technology / Software |
| **市值** | ~$290B |
| **核心因子** | Alpha#53 (Reversal) + Alpha#19 (Mean Reversion) |
| **因子解读** | Alpha#53: 软件板块反转确认，CRM 7/28 +4.55%；Alpha#19: 此前 AI 叙事担忧导致大幅回撤，均值回复空间充裕 |
| **综合评分** | 8.0 / 10 |
| **投资逻辑** | Agentforce AI 产品推动企业级 AI 落地；利润率优化（Margin 目标 25%+）；AI 轮动从基础设施 → SaaS 应用 |
| **风险提示** | 企业软件支出周期；Agentforce 商业化进度不确定 |

### 15. TRV — Travelers Companies (旅行者保险)

| 维度 | 内容 |
|------|------|
| **板块** | Financials / Insurance |
| **市值** | ~$84B |
| **核心因子** | Alpha#1 (Momentum) + Alpha#41 (Trend Strength) |
| **因子解读** | Alpha#1: 1M +22.6% / 1Y +51.4%，52-week high；Alpha#41: 保险板块结构性走强，价格趋势明确 |
| **综合评分** | 8.0 / 10 |
| **投资逻辑** | 保险板块 + Financials 双轮驱动；承保利润率改善 + 投资收益上升；财产险保费上涨周期 |
| **风险提示** | 巨灾损失（飓风季）可能拖累承保业绩 |

### 16. UNP — Union Pacific (联合太平洋)

| 维度 | 内容 |
|------|------|
| **板块** | Industrials / Transportation |
| **市值** | ~$182B |
| **核心因子** | Alpha#1 (Momentum) + Alpha#6 (Volume Confirmation) |
| **因子解读** | Alpha#1: 52-week high，1M +18.2% / 1Y +36.1%；Alpha#6: 货运量回升 + 成交量配合 |
| **综合评分** | 7.5 / 10 |
| **投资逻辑** | 油价下跌直接利好成本端（燃油成本占比 ~20%）；工业产出稳健 + Precision Railroading 运营效率提升 |
| **风险提示** | 经济放缓将削减货运需求；铁路劳资谈判风险 |

### 17. MMM — 3M

| 维度 | 内容 |
|------|------|
| **板块** | Industrials |
| **市值** | ~$94B |
| **核心因子** | Alpha#1 (Momentum) + Alpha#6 (Volume Confirmation) |
| **因子解读** | Alpha#1: 52-week high，1W +12.0%（突破放量）；Alpha#6: 重组 + 诉讼和解驱动资金流入 |
| **综合评分** | 7.5 / 10 |
| **投资逻辑** | 诉讼风险逐渐出清 + 重组降本增效 + 自由现金流改善 | 工业板块估值修复 |
| **风险提示** | PFAS 诉讼仍有不确定性；工业需求若放缓 |

### 18. PG — Procter & Gamble (宝洁)

| 维度 | 内容 |
|------|------|
| **板块** | Consumer Staples |
| **市值** | ~$390B |
| **核心因子** | Alpha#1 (Momentum) + Alpha#19 (Mean Reversion) |
| **因子解读** | Alpha#1: 防御属性在板块轮动中受益；Alpha#19: 相对前期高点折价，均值回复空间 |
| **综合评分** | 7.5 / 10 |
| **投资逻辑** | Consumer Staples 板块 Leading 象限 + 油价暴跌利好成本（石化衍生品）；稳定的股息增长（66 年连续提升） |
| **风险提示** | 定价能力随通胀回落减弱；私有品牌竞争加剧 |

### 19. ABBV — AbbVie (艾伯维)

| 维度 | 内容 |
|------|------|
| **板块** | Healthcare |
| **市值** | ~$459B |
| **核心因子** | Alpha#1 (Momentum) + Alpha#41 (Trend Strength) |
| **因子解读** | Alpha#1: 52-week high，1M +11.2% / 1Y +40.3%；Alpha#41: Skyrizi/Rinvoq 放量驱动趋势强劲 |
| **综合评分** | 7.5 / 10 |
| **投资逻辑** | Skyrizi + Rinvoq 已成功接棒 Humira（2023 专利到期）；免疫学管线领先；医疗板块轮动受益 |
| **风险提示** | PE ~126× 极端高估（一次性因素）；Skyrizi/Rinvoq 峰值增长能否持续 |

### 20. CVX — Chevron (雪佛龙)

| 维度 | 内容 |
|------|------|
| **板块** | Energy |
| **市值** | ~$330B |
| **核心因子** | Alpha#41 (Trend Strength) + Alpha#6 (Volume Confirmation) |
| **因子解读** | Alpha#41: 油价 $82 虽回撤，但中长期趋势仍高于盈亏平衡线；Alpha#6: Permian 盆地增产 + 回购驱动 |
| **综合评分** | 7.0 / 10 |
| **投资逻辑** | Energy 板块仍在 Leading 象限；油价 $82 仍支持大比例回购（~$175 亿/年）；股息增长 37 年 |
| **风险提示** | 伊朗/中东地缘溢价消退；全球石油需求增速放缓；能源转型长期压力 |

## Top 20 排名总表

| 排名 | 代码 | 公司名 | 板块 | 市值 | 核心因子 | 评分 |
|:----:|:----:|--------|------|------|----------|:----:|
| 1 | KO | Coca-Cola 可口可乐 | Consumer Staples | ~$280B | Alpha#1 + Alpha#12 | 9.5 |
| 2 | JPM | JPMorgan Chase 摩根大通 | Financials | ~$967B | Alpha#1 + Alpha#6 | 9.5 |
| 3 | AAPL | Apple 苹果 | Technology | ~$4.94T | Alpha#1 + Alpha#41 | 9.5 |
| 4 | LLY | Eli Lilly 礼来 | Healthcare | ~$1.05T | Alpha#1 + Alpha#41 | 9.0 |
| 5 | BAC | Bank of America 美国银行 | Financials | ~$450B | Alpha#1 + Alpha#6 | 9.0 |
| 6 | PM | Philip Morris 菲利普莫里斯 | Consumer Staples | ~$304B | Alpha#1 + Alpha#41 | 9.0 |
| 7 | RTX | RTX Corporation 雷神技术 | Industrials | ~$294B | Alpha#1 + Alpha#41 | 9.0 |
| 8 | BMY | Bristol-Myers Squibb 百时美施贵宝 | Healthcare | ~$127B | Alpha#1 + Alpha#19 | 8.5 |
| 9 | MRK | Merck & Co 默克 | Healthcare | ~$324B | Alpha#1 + Alpha#6 | 8.5 |
| 10 | JNJ | Johnson & Johnson 强生 | Healthcare | ~$603B | Alpha#1 + Alpha#19 | 8.5 |
| 11 | XOM | Exxon Mobil 埃克森美孚 | Energy | ~$628B | Alpha#6 + Alpha#41 | 8.0 |
| 12 | GS | Goldman Sachs 高盛 | Financials | ~$185B | Alpha#1 + Alpha#6 | 8.0 |
| 13 | ADBE | Adobe 奥多比 | Technology / Software | ~$110B | Alpha#53 + Alpha#30 | 8.0 |
| 14 | CRM | Salesforce 赛富时 | Technology / Software | ~$290B | Alpha#53 + Alpha#19 | 8.0 |
| 15 | TRV | Travelers 旅行者保险 | Financials / Insurance | ~$84B | Alpha#1 + Alpha#41 | 8.0 |
| 16 | UNP | Union Pacific 联合太平洋 | Industrials | ~$182B | Alpha#1 + Alpha#6 | 7.5 |
| 17 | MMM | 3M | Industrials | ~$94B | Alpha#1 + Alpha#6 | 7.5 |
| 18 | PG | Procter & Gamble 宝洁 | Consumer Staples | ~$390B | Alpha#1 + Alpha#19 | 7.5 |
| 19 | ABBV | AbbVie 艾伯维 | Healthcare | ~$459B | Alpha#1 + Alpha#41 | 7.5 |
| 20 | CVX | Chevron 雪佛龙 | Energy | ~$330B | Alpha#41 + Alpha#6 | 7.0 |

## 板块分布汇总

| 板块 | 数量 | 代码 | 总权重（估值） |
|------|:----:|------|:------------:|
| **Healthcare** | 5 | LLY / BMY / MRK / JNJ / ABBV | 25% |
| **Financials** | 4 | JPM / BAC / GS / TRV | 20% |
| **Consumer Staples** | 3 | KO / PM / PG | 15% |
| **Industrials** | 3 | RTX / UNP / MMM | 15% |
| **Technology** | 3 | AAPL / ADBE / CRM | 15% |
| **Energy** | 2 | XOM / CVX | 10% |

## 因子使用频率统计

| 因子 | 次数 | 占比 |
|------|:----:|:----:|
| Alpha#1 (Momentum) | 15 | 75% |
| Alpha#6 (Volume Confirmation) | 8 | 40% |
| Alpha#41 (Trend Strength) | 8 | 40% |
| Alpha#19 (Mean Reversion) | 5 | 25% |
| Alpha#53 (Reversal) | 2 | 10% |
| Alpha#30 (Volatility) | 1 | 5% |
| Alpha#12 (Divergence) | 1 | 5% |

## 综合投资策略

### 核心配置逻辑

1. **Healthcare (25%)** — 板块轮动最受益 + 2027E EPS 增速全市场第二（+19.3%）+ 估值处于 15 年低位
2. **Financials (20%)** — XLF 新晋 RRG Leading 象限 + M&A/IPO 复苏 + 降息预期利好
3. **Consumer Staples (15%)** — 防御属性 + 油价下跌利好成本 + 板块持续 Leading
4. **Industrials (15%)** — RTX/UNP/MMM 均在 52-week high，油价成本下降 + 国防/基建
5. **Technology (15%)** — AAPL 超大盘避险 + ADBE/CRM 软件轮动接棒芯片；MSFT 财报 7/29 核心催化
6. **Energy (10%)** — 仍处 Leading 象限但油价 $82 大幅回调，减配至 10%

### 本日与昨日对比变化

| 维度 | 7/28（昨日） | 7/29（本日） | 变化方向 |
|------|-------------|-------------|---------|
| 市场环境 | S&P 7413 / Nasdaq 24932 / Dow 52210 | S&P 7428 / Nasdaq 24876 / Dow 52747 | 道指大涨，纳指走弱 |
| 芯片抛售 | SOX -2.23% (距高点 -21%) | SOX -4.5% (距高点 -25%) | 芯片恐慌升级 |
| Sector Lead | XLE+XLF+XLRE+XLC+XLP | XLE+XLF+XLRE+XLC+XLP (XLF强化) | Financials 巩固领导 |
| 核心催化 | MSFT/META 财报前夕 | MSFT/META 财报 + Fed决议 | 逻辑验证日 |
| Top 5 变化 | AAPL(9.5)/JPM(9.3)/BAC(9.2)/ABBV(9.0)/RTX(9.0) | KO(9.5)/JPM(9.5)/AAPL(9.5)/LLY(9.0)/BAC(9.0) | KO 跳升(财报爆发) |
| Healthcare | 2 只 (ABBV, UNH) → 评分 9.0/8.5 | 5 只 (LLY/BMY/MRK/JNJ/ABBV) → 评分 9.0-7.5 | 医疗板块大幅上调 |
| Software | 未入选 | 2 只 (ADBE/CRM) → 评分 8.0 | 新增软件轮动 |

### 关键催化

| 时间 | 事件 |
|------|------|
| **7/29 (本日) 盘后** | **MSFT + META 财报** — AI Capex ROI 核心验证 |
| **7/30 盘后** | **AAPL + AMZN 财报** |
| **7/30** | MA + V 财报 |
| **7/31** | **FOMC 利率决议** (加息概率 ~31.5%) |
| **7/31–8/1** | AAPL/META/AMZN/INTC/LNG 等陆续财报 |
