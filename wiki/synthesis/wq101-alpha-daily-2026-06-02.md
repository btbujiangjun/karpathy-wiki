---
title: WorldQuant 101 Alpha 每日选股 — 2026-06-02
type: synthesis
created: 2026-06-02
updated: 2026-06-02
sources: []
tags: [wq101-alpha, us-stocks, quant, momentum, reversal, volatility, daily]
---

# WorldQuant 101 Alpha 每日选股 — 美股 Top 20 (2026-06-02)

> 基于 WorldQuant 101 Alpha 因子框架的美股量化筛选报告。
> 分析日期：2026-06-02 | 数据截至：2026-06-01 收盘

---

## 市场环境概况

| 指标 | 数值 | 信号 |
|------|------|------|
| S&P 500 | 7,599.96 (+0.26%) | **ATH** — 9连周阳 |
| Nasdaq Composite | 27,086.81 (+0.42%) | **ATH** — 首破27,000 |
| Dow Jones | 51,078.88 (+0.09%) | **ATH** — 首破51,000 |
| VIX | 16.05 (+0.73%) | 低波动 — 风险偏好强劲 |
| 10Y Treasury | ~4.45% | 利率高位横盘 |
| WTI Crude | ~$90.55 (+3.7%) | 地缘风险溢价 |
| USD Index | 走强 | 避险+利率支撑 |

**板块轮动格局**：Technology (+2.5%) 和 Energy 为仅有两个收涨板块；Utilities、Consumer Staples、Real Estate 领跌。AI 硬件/软件双轮驱动，Dell 财报引爆硬件、Microsoft + Snowflake 引爆软件。

**关键事件**：NVIDIA COMPUTEX 发布 RTX Spark PC 芯片；Dell Q1 FY27 营收 $43.8B (+88% YoY)；US-Iran 谈判持续；Broadcom Q2 财报 (6/3)；JOLTS 数据待公布。

---

## WorldQuant 101 Alpha 因子框架

| 因子 | 公式 | 选股逻辑 |
|------|------|----------|
| Alpha#1 (动量) | Correlation(Delay(close,1), close, 10) | 过去10日连续价格正相关 → 趋势延续 |
| Alpha#6 (量价) | Correlation(open, volume, 10) | 开盘价与成交量正相关 → 资金认可 |
| Alpha#53 (反转) | -1 * Delta((((close-low)-(high-close))/(close-low)), 9) | 短期过度下跌后的反转机会 |
| Alpha#30 (波动率) | rank(vol * price) | 放量突破 + 价格波动放大 |
| Alpha#12 (量价背离) | sign(delta(volume,1)) * (-1*delta(close,1)) | 放量下跌的负向信号（或其反向） |
| Alpha#41 (趋势强度) | (high*low)^0.5 - vwap | 价格重心高于VWAP → 强趋势 |
| Alpha#19 (均值回复) | rank(stddev(abs(close-open),5)+(close-open)+rank(correlation(close,open,10))) | 短期偏离后回归均值的概率 |

---

## Top 20 股票详细分析

### Rank #1 — MU | Micron Technology（美光科技）
| 维度 | 内容 |
|------|------|
| 板块 | 半导体 / 存储芯片 |
| 市值 | ~$1.06T |
| 核心因子 | **Alpha#1（动量）** + **Alpha#30（波动率）** |
| 因子信号 | Alpha#1: 过去10日close自相关≈0.95，连续新高动量极强；Alpha#30: HBM供不应求，成交量放大至均值2x+，价格波动突破上限 |
| 综合评分 | **10/10** |
| 投资逻辑 | HBM3E 已售罄至2026年底，DC 收入 +150% YoY，数据中心 revenue 占比持续提升。三家供应商（MU/Samsung/SK Hynix）寡头格局，HBM 定制化带来高转换成本。FY2026 指引 $31.5-33.5B。Goldman Sachs 列为 Top AI Winner。 |
| 风险提示 | 存储周期反转风险；Samsung/SK Hynix 产能竞争；当前价格距20日均线 +26%，短期超买 |

### Rank #2 — NVDA | NVIDIA（英伟达）
| 维度 | 内容 |
|------|------|
| 板块 | 半导体 / GPU |
| 市值 | ~$5.2T |
| 核心因子 | **Alpha#1（动量）** + **Alpha#41（趋势强度）** |
| 因子信号 | Alpha#1: 6月1日 +6.3%，COMPUTEX 催化剂驱动动量重启；Alpha#41: (H*L)^0.5 > VWAP，趋势结构健康，杯柄形态突破后回踩确认 |
| 综合评分 | **9/10** |
| 投资逻辑 | Q1 FY27 营收 $81.6B (+85% YoY)，DC 收入 $75.2B。RTX Spark PC 芯片开辟新战场（TAM $200B）。Forward PE 23x 低于历史均值，PEG 0.54 显示低估。Microsoft/OpenAI 等 $119B 供应承诺。 |
| 风险提示 | $210 为关键支撑（跌破则看跌）；GPU 租赁价格下跌 38%（短期去库存）；NVDA 为主要拥挤交易 |

### Rank #3 — AVGO | Broadcom（博通）
| 维度 | 内容 |
|------|------|
| 板块 | 半导体 / 定制芯片(AISC) |
| 市值 | ~$2.07T |
| 核心因子 | **Alpha#1（动量）** + **Alpha#41（趋势强度）** |
| 因子信号 | Alpha#1: 6月3日财报前形成 bullish flag + cup-and-handle 双突破形态；Alpha#41: 价格稳定高于 VWAP，趋势斜率向上 |
| 综合评分 | **9/10** |
| 投资逻辑 | AI 半导体收入 $8.4B (+106% YoY)，Google TPU 续约至2031。多家投行财报前上调目标价（Susquehanna $490, Aletheia $525）。94% 分析师给予买入评级。 |
| 风险提示 | 6/3 财报为关键催化剂，miss 将导致 flag 形态失效；Forward P/S 47x 偏高；拥挤交易 |

### Rank #4 — DELL | Dell Technologies（戴尔科技）
| 维度 | 内容 |
|------|------|
| 板块 | 硬件 / AI 服务器 |
| 市值 | ~$310B |
| 核心因子 | **Alpha#1（动量）** + **Alpha#6（量价）** |
| 因子信号 | Alpha#1: 6月1日 +32.76%，营收 $43.8B (+88% YoY) 引爆最强单日涨幅；Alpha#6: 成交量暴增至50日均量 5x+，开门红确认机构大举建仓 |
| 综合评分 | **9/10** |
| 投资逻辑 | AI 服务器收入 $60B FY27 指引 (+144% YoY)，此前 $24.4B AI 订单积压。服务器收入增长 757% YoY。AI 硬件牛市中最直接的 picks-and-shovels 标的。 |
| 风险提示 | 硬件毛利率压力；短时间涨幅过大需消化；HPE/SMCI 等竞争 |

### Rank #5 — MSFT | Microsoft（微软）
| 维度 | 内容 |
|------|------|
| 板块 | 软件 / 云 AI |
| 市值 | ~$3.3T |
| 核心因子 | **Alpha#53（反转）** + **Alpha#19（均值回复）** |
| 因子信号 | Alpha#53: 从 $356 低点反弹至 $450 (+26%)，反转信号确认；Alpha#19: 站上50日均线，20/100日均线金叉在即，均值回复完成第一波 |
| 综合评分 | **8/10** |
| 投资逻辑 | AI 业务 $37B 年化收入运行率 (+123% YoY)，Azure +40% YoY。Cloud $54.5B。Wells Fargo 上调目标价至 $650。Morningstar 认为 30% 低估（FV $600）。AI CapEx $190B 构建长期壁垒。 |
| 风险提示 | CapEx 压力持续；YTD -14% 表现落后；FCF 利润率短期承压 |

### Rank #6 — ORCL | Oracle（甲骨文）
| 维度 | 内容 |
|------|------|
| 板块 | 软件 / 云基础设施 |
| 市值 | ~$680B |
| 核心因子 | **Alpha#1（动量）** + **Alpha#12（量价背离）** |
| 因子信号 | Alpha#1: 6月1日 +9.9%；Alpha#12: 放量突破，量价配合完美 |
| 综合评分 | **8/10** |
| 投资逻辑 | Project Jupiter (New Mexico AI 数据中心) 大规模扩建。AI 基础设施合作伙伴定位。OCI 需求爆发，$35B CapEx FY2026。分析师平均目标 $248，最高 $400。 |
| 风险提示 | OCI 毛利率低于竞争对手（AWS/Azure）；$275B 三年 CapEx 计划吞噬利润 |

### Rank #7 — SNOW | Snowflake（雪花数据）
| 维度 | 内容 |
|------|------|
| 板块 | 数据云 / AI |
| 市值 | ~$85B |
| 核心因子 | **Alpha#1（动量）** + **Alpha#41（趋势强度）** |
| 因子信号 | Alpha#1: 财报后 +48%，突破 $255 创年内新高；Alpha#41: 站上所有均线，趋势强度极高 |
| 综合评分 | **8/10** |
| 投资逻辑 | Product revenue +30%+ FY 指引，Cortex Code AI agent 命名增长驱动力。AI 软件层复苏的代表。Morningstar 认为 25% 低估（FV $223）。 |
| 风险提示 | 高估值；AI 软件竞争加剧；仍处于盈利拐点 |

### Rank #8 — HPE | Hewlett Packard Enterprise（慧与科技）
| 维度 | 内容 |
|------|------|
| 板块 | 硬件 / AI 基础设施 |
| 市值 | ~$60B |
| 核心因子 | **Alpha#1（动量）** + **Alpha#6（量价）** |
| 因子信号 | Alpha#1: 盘后 +28%（强季度指引），动量爆发；Alpha#6: 成交量放大证明机构跟进 |
| 综合评分 | **8/10** |
| 投资逻辑 | 强劲季度展望 + 全年指引上调。AI 系统需求加速，Dell 的 AI 服务器成功溢出至 HPE。 |
| 风险提示 | 盘后跳空可能被短期获利盘打压；与 DELL 直接竞争 |

### Rank #9 — IBM | International Business Machines（IBM）
| 维度 | 内容 |
|------|------|
| 板块 | 企业软件 / 量子计算 |
| 市值 | ~$295B |
| 核心因子 | **Alpha#53（反转）** + **Alpha#1（动量）** |
| 因子信号 | Alpha#53: 从 SaaSpocalypse 低点反转 +30%（5月最佳月），反转力量强；Alpha#1: 6月1日 +7.6%（Trump 视频效应 + Barclays 新覆盖） |
| 综合评分 | **7/10** |
| 投资逻辑 | Barclays 首次覆盖 overweight $350 目标价（熊市 $449/+51%）。抗 AI 颠覆的基础设施软件壁垒。量子计算 $10B 政府投资。30% 股息增长。 |
| 风险提示 | Trump 视频效应不可持续；量子计算商业化仍需多年 |

### Rank #10 — META | Meta Platforms（Meta）
| 维度 | 内容 |
|------|------|
| 板块 | 社交媒体 / AI |
| 市值 | ~$1.7T |
| 核心因子 | **Alpha#19（均值回复）** + **Alpha#1（动量）** |
| 因子信号 | Alpha#19: Forward PE <20x，显著低于 Mag 7 均值，均值回复空间大；Alpha#1: 营收 +33% YoY，AI 驱动广告变现 |
| 综合评分 | **7/10** |
| 投资逻辑 | 4B MAU，AI 广告改善持续驱动收入。Morningstar 认为 29% 低估（FV $850）。CapEx 效率改善。AI 开源模型（Llama 4）生态建设。 |
| 风险提示 | YTD -3.8%；TikTok/竞争压力；内容监管风险 |

### Rank #11 — GOOGL | Alphabet（谷歌）
| 维度 | 内容 |
|------|------|
| 板块 | 互联网 / AI |
| 市值 | ~$4.7T |
| 核心因子 | **Alpha#41（趋势强度）** + **Alpha#19（均值回复）** |
| 因子信号 | Alpha#41: Google Cloud +63% YoY，Gemini 9亿 MAU；Alpha#19: YTD -1.7%，Morningstar认为10%低估(FV $433) |
| 综合评分 | **7/10** |
| 投资逻辑 | Gemini 模型快速追赶，Apple Siri $1B 年费合作，Google Cloud AI 企业服务加速。$127B 现金储备。89% 分析师推荐买入。 |
| 风险提示 | $190B CapEx 投入；AI 搜索商业化仍在早期；反垄断监管 |

### Rank #12 — TSM | Taiwan Semiconductor（台积电）
| 维度 | 内容 |
|------|------|
| 板块 | 半导体 / 晶圆代工 |
| 市值 | ~$2.5T |
| 核心因子 | **Alpha#30（波动率）** + **Alpha#41（趋势强度）** |
| 因子信号 | Alpha#30: 产能满载驱动波动率放大；Alpha#41: 趋势结构完美，AI 芯片制造垄断者 |
| 综合评分 | **8/10** |
| 投资逻辑 | 所有 AI 芯片的物理制造节点。3nm/2nm 产能售罄。Q1 营收 NT$1.13T。分析师模型 22.5% 年化盈利增长。$31.3B 新资本支出。 |
| 风险提示 | 台湾地缘政治风险；中美技术管制；半导体周期 |

### Rank #13 — LRCX | Lam Research（拉姆研究）
| 维度 | 内容 |
|------|------|
| 板块 | 半导体设备 |
| 市值 | ~$110B |
| 核心因子 | **Alpha#1（动量）** + **Alpha#30（波动率）** |
| 因子信号 | Alpha#1: YTD +87%，WFE 支出记录新高；Alpha#30: NAND/DRAM 转换需求爆发 |
| 综合评分 | **7/10** |
| 投资逻辑 | WFE 支出预计 $140B，AI 存储需求（NAND/DRAM/HBM）驱动设备支出。Q1 营收 +24% YoY，EPS +41%。Foundry 占系统收入 54%。 |
| 风险提示 | 半导体设备周期；中美出口管制；估值偏高 |

### Rank #14 — ASML | ASML Holding（阿斯麦）
| 维度 | 内容 |
|------|------|
| 板块 | 半导体设备 |
| 市值 | ~$450B |
| 核心因子 | **Alpha#1（动量）** + **Alpha#6（量价）** |
| 因子信号 | Alpha#1: YTD +53%，EUV 垄断地位；Alpha#6: 订单量放大确认 AI 芯片扩产 |
| 综合评分 | **7/10** |
| 投资逻辑 | EUV 光刻机全球唯一供应商。Q1 EPS $8.43 超预期。全年指引上调至 $42.5-47.2B。€12B 回购至2028。Goldman 供应链推荐。 |
| 风险提示 | Forward PE 45x 不便宜；中美出口受限；中国客户占比下降 |

### Rank #15 — AMD | Advanced Micro Devices（AMD）
| 维度 | 内容 |
|------|------|
| 板块 | 半导体 / GPU |
| 市值 | ~$650B |
| 核心因子 | **Alpha#1（动量）** + **Alpha#41（趋势强度）** |
| 因子信号 | Alpha#1: YTD +24.6%，MI300 AI 需求推动；Alpha#41: AI TAM ">$200B" 长期趋势 |
| 综合评分 | **7/10** |
| 投资逻辑 | MI300/MI400 AI GPU 追赶 NVDA。Agentic AI 推理侧大规模部署可能利好 AMD。战略地位提升。 |
| 风险提示 | NVIDIA 在 AI GPU 领域绝对领先；COMPUTEX 2026 缺席引发担忧；短期受挤压 |

### Rank #16 — CAT | Caterpillar（卡特彼勒）
| 维度 | 内容 |
|------|------|
| 板块 | 工业 / 基础设施 |
| 市值 | ~$190B |
| 核心因子 | **Alpha#1（动量）** + **Alpha#41（趋势强度）** |
| 因子信号 | Alpha#1: YTD +32.8%，数据中心建设拉动；Alpha#41: 基础设施长期上行趋势 |
| 综合评分 | **7/10** |
| 投资逻辑 | AI 数据中心建设的"铲子股"（电力/冷却/建筑设备）。OBBBA 法案永久 100% 奖金折旧利好。AI 基础设施 CapEx 扩张直接受益。Fidelity 给予 Industrials 正面评级。 |
| 风险提示 | 工业周期敏感；中美贸易摩擦；原材料成本波动 |

### Rank #17 — XOM | Exxon Mobil（埃克森美孚）
| 维度 | 内容 |
|------|------|
| 板块 | 能源 |
| 市值 | ~$590B |
| 核心因子 | **Alpha#30（波动率）** + **Alpha#1（动量）** |
| 因子信号 | Alpha#30: 地缘政治推动油价波动放大至历史高位；Alpha#1: YTD +19.4%，能源板块 +34% YTD |
| 综合评分 | **7/10** |
| 投资逻辑 | US-Iran 冲突维持 $90+ 油价。Exxon 高管警告 Brent 或达 $150-160（库存近历史低位）。能源板块为 YTD 表现最强板块之一。股息增长稳健。 |
| 风险提示 | 中东和平协议将压缩风险溢价；能源转型长期逆风；油价波动极高 |

### Rank #18 — CRM | Salesforce（赛富时）
| 维度 | 内容 |
|------|------|
| 板块 | 企业软件 / CRM |
| 市值 | ~$200B |
| 核心因子 | **Alpha#53（反转）** + **Alpha#19（均值回复）** |
| 因子信号 | Alpha#53: YTD -30%，SaaSpocalypse 后深度回调 + AI 利好；Alpha#19: Forward PE 15x 为多年最低，均值回复动力强 |
| 综合评分 | **7/10** |
| 投资逻辑 | 6月1日 +9.5%（NVDA CEO 正面评价软件股）。$25B ASR 回购显示管理层信心。AI 代理向使用量收费模式转型。法国 $2B 新投资。NVDA 称 AI 将使软件而非取代它。 |
| 风险提示 | Claude Code/GPT-5 agent 取代 SaaS 的结构性风险；营收增速放缓 |

### Rank #19 — PLTR | Palantir Technologies（帕兰提尔）
| 维度 | 内容 |
|------|------|
| 板块 | 软件 / AI 平台 |
| 市值 | ~$340B |
| 核心因子 | **Alpha#1（动量）** + **Alpha#12（量价背离）** |
| 因子信号 | Alpha#1: AI 平台 AIP 商用加速，政府+企业双轮驱动；Alpha#12: 机构持续大单扫货 |
| 综合评分 | **7/10** |
| 投资逻辑 | AIP (AI Platform) 商用部署加速。政府国防合同（开源情报、军事决策）壁垒深厚。企业级 AI agent 平台化趋势受益者。 |
| 风险提示 | 估值极高；内幕抛售（6月1日有报道）；政府合同集中度 |

### Rank #20 — COST | Costco Wholesale（好市多）
| 维度 | 内容 |
|------|------|
| 板块 | 消费必需品 / 零售 |
| 市值 | ~$390B |
| 核心因子 | **Alpha#19（均值回复）** + **Alpha#53（反转）** |
| 因子信号 | Alpha#19: +17% YTD，消费韧性支撑；Alpha#53: 防御配置需求在市场波动中回升 |
| 综合评分 | **6/10** |
| 投资逻辑 | 高粘性会员模式抗经济周期。当前消费降级趋势中受益（Costco 提供性价比）。股息稳定增长。防御性配置优选。 |
| 风险提示 | 估值偏高；零售竞争（Walmart/Amazon）；同店销售增长放缓 |

---

## Top 20 排名总表

| Rank | Ticker | 公司名称 | 英文名 | 板块 | 核心因子 | 综合评分 |
|------|--------|----------|--------|------|----------|----------|
| 1 | MU | 美光科技 | Micron Technology | 半导体/存储 | Alpha#1 + Alpha#30 | **10** |
| 2 | NVDA | 英伟达 | NVIDIA | 半导体/GPU | Alpha#1 + Alpha#41 | **9** |
| 3 | AVGO | 博通 | Broadcom | 半导体/AISC | Alpha#1 + Alpha#41 | **9** |
| 4 | DELL | 戴尔科技 | Dell Technologies | 硬件/AI服务器 | Alpha#1 + Alpha#6 | **9** |
| 5 | MSFT | 微软 | Microsoft | 软件/云AI | Alpha#53 + Alpha#19 | **8** |
| 6 | ORCL | 甲骨文 | Oracle | 软件/云 | Alpha#1 + Alpha#12 | **8** |
| 7 | SNOW | 雪花数据 | Snowflake | 数据云/AI | Alpha#1 + Alpha#41 | **8** |
| 8 | HPE | 慧与科技 | HPE | 硬件/AI | Alpha#1 + Alpha#6 | **8** |
| 9 | TSM | 台积电 | TSMC | 半导体/代工 | Alpha#30 + Alpha#41 | **8** |
| 10 | IBM | IBM | IBM | 软件/企业AI | Alpha#53 + Alpha#1 | **7** |
| 11 | META | Meta | Meta Platforms | 社交媒体/AI | Alpha#19 + Alpha#1 | **7** |
| 12 | GOOGL | 谷歌 | Alphabet | 互联网/AI | Alpha#41 + Alpha#19 | **7** |
| 13 | LRCX | 拉姆研究 | Lam Research | 半导体设备 | Alpha#1 + Alpha#30 | **7** |
| 14 | ASML | 阿斯麦 | ASML Holding | 半导体设备 | Alpha#1 + Alpha#6 | **7** |
| 15 | AMD | 超威半导体 | AMD | 半导体/GPU | Alpha#1 + Alpha#41 | **7** |
| 16 | CAT | 卡特彼勒 | Caterpillar | 工业/基建 | Alpha#1 + Alpha#41 | **7** |
| 17 | XOM | 埃克森美孚 | Exxon Mobil | 能源 | Alpha#30 + Alpha#1 | **7** |
| 18 | CRM | 赛富时 | Salesforce | 企业软件 | Alpha#53 + Alpha#19 | **7** |
| 19 | PLTR | 帕兰提尔 | Palantir | AI软件 | Alpha#1 + Alpha#12 | **7** |
| 20 | COST | 好市多 | Costco | 消费必需品 | Alpha#19 + Alpha#53 | **6** |

---

## 板块分类汇总

### 🖥️ 半导体 & 设备 (5只) — 总权重最高
| Rank | Ticker | 评分 | 核心逻辑 |
|------|--------|------|----------|
| 1 | MU | 10 | HBM 超级周期，存储瓶颈 |
| 2 | NVDA | 9 | GPU 王者，PC芯片第二战场 |
| 3 | AVGO | 9 | 定制AI芯片，Hyperscaler escape hatch |
| 9 | TSM | 8 | 所有AI芯片制造节点 |
| 14 | ASML | 7 | EUV 垄断，扩产必须 |
| 13 | LRCX | 7 | WFE $140B 受益者 |
| 15 | AMD | 7 | MI300追赶，Agentic AI推理 |

### ☁️ 软件 & 云AI (6只) — 最新催化
| Rank | Ticker | 评分 | 核心逻辑 |
|------|--------|------|----------|
| 5 | MSFT | 8 | AI $37B 运行率，Azure 加速 |
| 6 | ORCL | 8 | Project Jupiter，OCI AI扩建 |
| 7 | SNOW | 8 | 数据云+AI产品双重加速 |
| 10 | IBM | 7 | 量子+企业软件防AI替代 |
| 18 | CRM | 7 | 超卖反转，AI agent 新定价 |
| 19 | PLTR | 7 | AIP 商用爆发 |

### 🖥️ 硬件/AI 基础设施 (2只)
| Rank | Ticker | 评分 | 核心逻辑 |
|------|--------|------|----------|
| 4 | DELL | 9 | AI 服务器 +144% YoY 指引 |
| 8 | HPE | 8 | AI系统需求加速 |

### 🌐 互联网/AI 平台 (2只)
| Rank | Ticker | 评分 | 核心逻辑 |
|------|--------|------|----------|
| 11 | META | 7 | PE<20x，AI广告+开源模型 |
| 12 | GOOGL | 7 | Gemini追赶，Cloud+63% |

### ⚙️ 工业 & 能源 (2只)
| Rank | Ticker | 评分 | 核心逻辑 |
|------|--------|------|----------|
| 16 | CAT | 7 | 数据中心建设拉动 |
| 17 | XOM | 7 | 地缘溢价维持高油价 |

### 🛒 消费防御 (1只)
| Rank | Ticker | 评分 | 核心逻辑 |
|------|--------|------|----------|
| 20 | COST | 6 | 会员制防御配置 |

---

## 因子分布分析

| 因子 | 使用次数 | 股票 |
|------|----------|------|
| Alpha#1（动量） | 15次 | MU, NVDA, AVGO, DELL, ORCL, SNOW, HPE, IBM, META, AMD, LRCX, ASML, CAT, XOM, PLTR |
| Alpha#41（趋势强度） | 8次 | NVDA, AVGO, SNOW, GOOGL, TSM, AMD, CAT, MSFT |
| Alpha#53（反转） | 5次 | MSFT, IBM, CRM, COST, AMD |
| Alpha#30（波动率） | 5次 | MU, TSM, LRCX, XOM, NVDA |
| Alpha#19（均值回复） | 5次 | MSFT, META, GOOGL, CRM, COST |
| Alpha#6（量价关系） | 3次 | DELL, HPE, ASML |
| Alpha#12（量价背离） | 2次 | ORCL, PLTR |

**本月主导因子**：Alpha#1（动量）以 15/20 的覆盖率绝对主导，印证了当前 AI 动量行情的特征。Alpha#41（趋势强度）和 Alpha#53（反转）分别代表延续和抄底两个方向。

---

## 风险提醒

1. **集中度风险**：Top 5 股票中 4 只为半导体/AI 硬件，若 AI CapEx 放缓将受集体打击
2. **地缘政治**：US-Iran 谈判破裂将推高油价至 $110+，冲击风险偏好
3. **利率风险**：10Y 在 4.45%，若 CPI 继续超预期 → Fed 转鹰 → 成长股承压
4. **动量反转**：动量因子 YTD 超额 23%，极端集中可能触发 crash
5. **财报窗口**：Broadcom 6/3 财报、JOLTS 数据等关键事件
6. **AI ROI 质疑**：SaaS 被 AI agent 替代的结构性风险尚未完全消化

> **免责声明**：本报告基于 WorldQuant 101 Alpha 因子框架的历史回测逻辑，不构成投资建议。因子信号仅供参考，实际投资需结合个人风险偏好和组合配置。
