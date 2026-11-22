---
title: "投资热点日报 — 美股 / 港股 / A 股 / 中榄股 / 中榄新能源 / AI（2026-11-22）"
type: synthesis
created: 2026-11-22
updated: 2026-11-22
sources: [investment-daily.md]
tags: [investment, daily, us-equities, hk-equities, a-share-equities, adr, china-concept, ai, semiconductor, nvidia, amd, tsm, avgo, smci, pltr, nvda, tencent, alibaba, meituan, xiaomi, baidu, smic, hygon, cambricon, innolight, naura, iflytek, byd, tesla, xpev, nio, li-auto, ntes, pdd, baidu-us, tcomb, tme, bili, ymm, vips, bz, rlx, catl, sungrow, daily-digest]
---

# 投资热点日报 — 美股 / 港股 / A 股 / 中榄股 / 中榄新能源 / AI（2026-11-22）

> ## ⚠️ 数据基准（撰写时点 ≈ 2026-11-22，Sunday）
>
> - **数据源**：Yahoo Finance 页面（^GSPC/^IXIC/^DJI/^VIX 指数页面；个股页面的 Summary/Stats 段），抓取时间 ≈ 11/21–11/22；美股数据基准 = 常规收盘 Nov 20 + 隔夜快照；港/A 为 11/21 常规收盘快照。`websearch` 不可用、Yahoo v7/v8 quote/chart API（401/Too Many Requests）不可用，已改用 Yahoo HTML 页面。今日事件另用 Yahoo live markets 页（休市日新闻）核对。
> - **约定**：涨跌幅 = (今日价 − 前收)/前收；"隔夜" 为隔夜快照；对 Yahoo 页面数据冲突已标注。**未取得条目**已标注。**不构成投资建议。**

---

## 0. 一页速览：核心主线

| # | 主线 | 核心股票 | 今日反应 |
|---|------|----------|----------|
| ① | 美股 AI 承压分化（SEC 调查 Nvidia，AI 交易整体转弱） | NVIDIA 125.53（-14.01%，隔夜 +3.57%）；AMD 424.39（-13.25%，隔夜 +3.53%）；TSM 318.71（-9.48%，隔夜 +3.10%）；AVGO 304.41（-12.19%）；SMCI 21.65（-9.19%） | 纳指 -5.28%、标普 -3.70%、VIX +26.20% |
| ② | 港股平台股跟随反弹，结构回调（阿里 +3.48%，腾讯/百度/小米下行） | 阿里 9988.HK 83.350（+3.48%）；腾讯 0700.HK 344.000（-1.26%）；百度 9888.HK 64.050（-4.04%）；小米 1810.HK 27.640（-3.09%） | 平台股混合：阿里反弹，腾讯/百度/小米承压 |
| ③ | A 股 AI 链条分化（海光体现强度，中际旭创光模块承压） | 海光 688041.SS 164.25（-8.75%）；寒武玎 688256.SS 920.00（-1.50%）；中际旭创 300308.SZ 393.20（-3.72%） | AI 链条跟随普跌见顶修正 |
| ④ | ADR 分化，防守阵地跟随指数表现 | 拼多多 PDD 83.40（-0.33%）；NTES 99.85（-4.85%）；XPEV 8.16（-13.86%）；NIO 2.4500（-7.89%）；LI 10.39（-7.56%） | 筹码挤出，EV 与北美平台股跟随防守指数 |
| ⑤ | AI 热点：NVIDIA SEC 调查 + Q3 财报对冲，Anthropic IPO 招股追踪，算力租赁弹性退 | NVIDIA（SEC 调查/Q3 财报/AI 资本开支）；Anthropic IPO（ANT）；CoreWeave -9.07% | AI 估值仍在打折，但相对弹性有支撑 |

---

## 1. 美股（Mag 7 / AI 链条）

### 1.1 宏观指数（常规收盘 Nov 20 + 隔夜）

| 指数 | 今日 | 涨跌幅 | 备注 |
|------|------|--------|------|
| **S&P 500 (SPX)** | 6,910.39 | **-3.70%** | At close Nov 20 (4:35:54 PM EST)；YTD +0.95% |
| **Nasdaq Composite (^IXIC)** | 22,617.73 | **-5.28%** | At close Nov 20 (5:15:59 PM EST)；YTD -2.69% |
| **Dow Jones (^DJI)** | 48,147.33 | **-1.93%** | At close Nov 20 |
| **VIX** | 35.89 | **+26.20%**（+7.45%） | 恐慌指数反弹 |

### 1.2 Mag 7 与 AI 权重股

| 公司（中英文） | 股票代码 | 板块 / 交易所 | 热点事件 | 市场反应 | 投资逻辑 |
|---|---|---|---|---|---|
| 英伟达 NVIDIA | NVDA | AI 芯片 / NASDAQ | SEC 调查（live: "Nvidia stock extends 25-trillion rout as SEC probes accounting"）；Q3 FY27 财报（实报 Nov 17：Revenue $115.84B、Earnings $65.29B、Margin 56.36%；dividend $0.25, ex 12/2） | 收 Nov 20: 125.53（-14.01%）；隔夜快照 130.01（+3.57%）。注：NVIDIA 页面 YTD 各源存在矛盾已标注 | 计算芯片估值跌幅见底（PE 13.48），AI 弹性空间待实现；Jensen Huang Nov 12 辞任治理争议仍持续（live 报告） |
| AMD Advanced Micro Devices | AMD | AI 芯片 / NASDAQ | AI 营销强势；BofA Nov 12 Maintains Buy, target 650→700 | 收 Nov 20: 424.39（-13.25%）；隔夜 439.39（+3.53%） | 落后 NVIDIA 估值，PE 90.68 偏高，关注营销弹性 |
| 博通 Broadcom | AVGO | AI networking / NASDAQ | AI networking 链强势 | 收 Nov 20: 304.41（-12.19%） | 相对 NVIDIA 的 AI 估值修复空间 |
| 超微 Super Micro | SMCI | 服务器/AI / NASDAQ | NVIDIA GPP 需求透支周期；Susquehanna target 15→18 | 收 Nov 20: 21.65（-9.19%）；隔夜 22.16（+2.36%） | AI 芯片下游周期利空 |
| 台积电 TSMC | TSM | 半导体 / NASDAQ | AI 需求跟随 NVIDIA 兑现；Bernstein target 554→600 | 收 Nov 20: 318.71（-9.48%）；隔夜 328.60（+3.10%） | AI 下游链修复引擎，PE 20.66 |
| 苹果 Apple | AAPL | 消费 / NASDAQ | China Renaissance Nov 11 Upgrade, target 425；防守+成长（YTD +26.01%） | 收 Nov 20: 342.56（-1.90%）；隔夜 344.87（+0.67%） | 防御属性 + 营收弹性，需等创新品定型 |
| 微软 Microsoft | MSFT | 云/AI / NASDAQ | RBC Capital Nov 20 Reiterates Outperform, target 640 | 收 Nov 20: 484.52（-2.77%）；隔夜 489.49（+1.03%） | 云 AI 空间实在大；PE 25.29 |
| 亚马逊 Amazon | AMZN | 电商/云 / NASDAQ | AWS 需求未明 | 收 Nov 20: 246.82（-2.48%） | 防守落后 |
| Alphabet (Google) | GOOG | 搜索/云 / NASDAQ | 搜索/云稳定 | 收 Nov 20: 264.00（-0.93%） | 防守层承压跟随 |
| Meta Platforms | META | 社交/广告 / NASDAQ | 广告 AI 推荐弹性担忧 | 收 Nov 20: 560.84（-4.82%） | 高弹性防守指数的退潮表现 |
| 特斯拉 Tesla | TSLA | EV/AI / NASDAQ | AI 选项（Optimus/Jarvis）空间 | 收 Nov 20: 345.82（-7.64%）；隔夜 351.08（+1.52%） | AI 选项空间 + 防守落后；PE 380 偏高 |
| Palantir | PLTR | AI 软件/NASDAQ | AI 软件高弹性；Barclays target 265→273 | 收 Nov 20: 143.49（-6.63%）；隔夜 145.58（+1.46%） | AI 软件需求保值 |

### 1.3 AI 软件 / 算力租赁 / 数据中心

| 公司（中英文） | 股票代码 | 板块 / 交易所 | 热点事件 | 市场反应 | 投资逻辑 |
|---|---|---|---|---|---|
| 数据中心需求（NVIDIA → Schnieder Electric） | NVIDIA | 数据中心 / NASDAQ | Simply Wall St 报告（约 41m ago） | NVDA 隔夜快照 +3.57% | 数据中心下游弹性在 NVIDIA 打压后恢复 |
| NVIDIA GPP 需求兑现 | NVIDIA / SMCI | 芯片 | SMCI 收 Nov 20: 21.65（-9.19%）；NVIDIA +3.57% | 周期见顶压抑 | 强势兑现，关注 AVGO 相对安全侧 |
| 算力租赁 | CoreWeave | 算力租赁 / NASDAQ | AI 算力租赁需求弹性退（疑关联 NVIDIA 放缓） | 收 Nov 20: 39.51（-9.07%） | 关注修复空间 |
| Anthropic IPO（招股追踪） | Anthropic | IPO tracking | 首日交易：股价以约 $86（10:55 AM ET）盘旋，定价 $83；跌 8% 至 $86–88，市值 $1.5 万亿成立 | — | 追踪中，无需过度解读 |

---

## 2. 港股（平台股 / 科技 / AI）

### 2.1 平台股 / 科技 / AI 板块（常规收盘快照 ≈ Nov 20）

| 公司（中英文） | 股票代码 | 板块/交易所 | 热点事件 | 市场反应 | 投资逻辑 |
|---|---|---|---|---|---|
| 腾讯控股 Tencent | 0700.HK | 互联网平台/游戏/AI / 港交所 | Q3 2026 财报今日可看；估值已提升（PE 12.26）；FCF 60.26B；YTD +42.10% | 收 Nov 20: 344.000（-1.26%） | 估值退税接近见顶，AI 投入稳定；均值回归 |
| 美团 Meituan | 3690.HK | 本地生活/AI / 港交所 | AI 自研强势 | 收 Nov 20: 66.500（-1.55%） | 防守类 |
| 阿里巴巴（HK） | 9988.HK | 电商/云/AI / 港交所&纳斯达克 | Q2 2027 earnings call 可见；云管理费率压力 | 收 Nov 20: 83.350（+3.48%） | 云出海+Temu 混排，管理费率修复缓慢；逆势反弹 |
| 小米集团 Xiaomi | 1810.HK | 手机/EV/AI / 港交所 | SU7 减亏与手机高端化双轮 | 收 Nov 20: 27.640（-3.09%） | 防守 + 双轮增长 |
| 百度 | 9888.HK | 搜索/AI / 港交所&纳斯达克 | 萝卜快跑+模型迭代 | 收 Nov 20: 64.050（-4.04%） | 估值折价，跟随美股 |
| 中芯国际 SMIC | 0981.HK | 半导体 / 港交所 | 替代链上游利好 | **未取得**（11/21 页无近期快照；11/20 50.050，-0.89%） | 国产替代标跟随 A 链 |
| 比亚迪（HK） | 1211.HK | Auto Manufacturers / 港交所 | 减亏与产品降价趋势 | 收 Nov 20: 62.350（-1.34%） | 跟随 A 股 BYD（A -0.87%） |
| 快手 Kuaishou | 1024.HK | 短视频/AI / 港交所 | 短视频 AI 视频预期疲软 | 11/20 20.140（-12.59%） | 高弹性，YTD -68.41% |
| 网易 NetEase | 9999.HK | 游戏/内容/AI / 港交所&纳斯达克 | AI (Confucius 大模型 for education) | 11/20 152.600（-18.35%） | 跟随美股下行 |

---

## 3. A 股（含 A 股 AI 与国产替代）

### 3.1 AI/算力/芯片/光模块/半导体设备（常规收盘快照 ≈ Nov 20）

| 公司（中英文） | 股票代码 | 板块/交易所 | 热点事件 | 市场反应 | 投资逻辑 |
|---|---|---|---|---|---|
| 海光信息 Hygon | 688041.SS | 国产 GPU/AI / 科创板 | AI 链强势，业绩见顶强化；Advanced Micro-Fabrication 688012 +1.95% | 收 Nov 20: 164.25（-8.75%） | AI 主线体现强度；估值已接近修复边界 |
| 寒武玎 Cambricon | 688256.SS | 国产 AI 芯片 / 科创板 | 国产 AI 芯片 | 收 Nov 20: 920.00（-1.50%） | AI 芯片防守阵地坐实弹性 |
| 中际旭创 Innolight | 300308.SZ | 光模块 / 深圳 | 光模块龙头，10G→1.6T, AI/数据中心应用 | 收 Nov 20: 393.20（-3.72%） | AI/DC 入场点清晰；PE 17.79 |
| 科大讯飞 iFlytek | 002230.SZ | 大模型/软件 / 深圳 | 大模型应用下行承压；PE 90.79 高位 | 收 Nov 20: 34.50（-3.90%） | 大模型应用下行，抬头等待增长；PE 偏高 |
| 北方华创 NAURA | 002371.SZ | 半导体设备 / 深圳 | 半导体设备（非晶丝）/光模块，国产替代龙头 | 收 Nov 20: 579.00（-2.20%） | 半导体设备龙头，下行但 AI 链兜底 |
| 宁德时代 CATL | 300750.SZ | 储能/动力 / 深圳 | 储能链国产龙头，AI 侧比例小 | 收 Nov 20: 227.78（-2.90%） | 储能双龙头 |
| 阳光电源 | 300274.SZ | 光伏/储能 / 深圳 | 光伏+储能，需求回暖见顶 | 11/20: 69.78（-2.31%，10:25 AM） | 光伏+储能线 |
| 中微公司 AMEC | 688012.SH | 半导体设备（刻蚀等）/ 科创板 | 国产刻蚀设备龙头；先进制程/存储扩产与国产化率提升 | **未取得**（11/21 数据缺失；10/27: -5.30%） | 与北方华创同属设备国产替代主线 |
| 未取得 | — | — | — | — | 中科曙光（603019.SH）、新易盛（最近可见 -5.60%，10/27）、隆基绿能（601012.SS 部分可见 10.89/-0.55%）、三六零（601360.SH 已退市/停牌） |

---

## 4. 中榄股（ADR，US）

| 公司（中英文） | 股票代码 | 热点事件 | 市场反应 | 投资逻辑 |
|---|---|---|---|---|
| 阿里巴巴 | BABA | Q2 2027 earnings call 可见；Citigroup Nov 20 Maintains Buy, target 193→160 | 收 Nov 20: 81.08（-2.68%） | 管理费率修复缓慢，云出海+Temu 混排仍在 |
| 拼多多 | PDD | Q3 2026 Earnings Nov 19；Macmautiff Nov 20 Upgrade, target 98→106 | 收 Nov 20: 83.40（-0.33%） | 筹码挤出，跟随指数 |
| 百度（US ADR） | BIDU | US ADR 数据未取得（11/21 页；11/20 页亦未获取，HK 9888.HK 见 3.2） | — | 落后美股，跟随美股 |
| 网易 | NTES | 语音 AI 应用（Deepting/Hi Echo）；PE 14.58；Morgan Stanley target 174→163 | 收 Nov 20: 99.85（-4.85%） | 防守侧下行 |
| 小鹏汽车 | XPEV | Profits -3.61B；HSBC Nov 20 Downgrade, target 10.1 | 收 Nov 20: 8.16（-13.86%） | 跟随国际 EV 指数；Turing AI 平台双轮仍在 |
| 蔚来 | NIO（ADR） | 自动驾驶交付，Dec 1 财报（预期 >40k/月交付） | 收 Nov 20: 2.4500（-7.89%） | 自动驾驶弹性 |
| 理想汽车 | LI | AI 平台，主力保持稳定 | 收 Nov 20: 10.39（-7.56%） | 防守 |
| 华润记得 BEKE | BEKE | 地产中介，CLSA Outperform target 23.8 | 11/20: 18.00（-1.32%） | — |
| 携程 TCOM | TCOM | 旅游/航空业务，YTD +41.57% | 11/20: 41.58（-1.84%） | — |
| 满帮 YMM | YMM | 交易所数字物流平台，Q3 2026 财报今日（7 AM EST Nov 20） | 11/20: 9.06（+8.11% O） | — |
| 唯品会 VIPS | VIPS | 吊牌会，防御消费，PE 4.25 | 11/20: 12.61（-1.79%） | — |
| BOSS 直聘 BZ | BZ | 招聘+就业温度；JP Morgan target 22→18 | 11/20: 12.88（-1.90%） | — |
| 雾芯科技 RLX | RLX | e烟，Q3 2026 财报今日（7 AM EST Nov 20） | 11/20: 1.46（+0.68% O） | — |
| 腾讯音乐 TME | TME | QQ Music/Kugou/Kuwo 音乐业务，PE 11.00 | 11/20: 9.02（-1.20%） | — |
| 哔哩哔哩 BILI | BILI | 内容平台 | 11/20: 10.99（-0.63%） | — |

---

## 5. 中榄车链（新能源/电动汽车链条）

| 公司（中英文） | 股票代码 | 热点事件 | 市场反应 | 投资逻辑 |
|---|---|---|---|---|
| 比亚迪（A） | 002594.SZ | 车载产品降价趋势 | 11/20 78.95（-1.78%，10:24 AM） | 行业分化，YTD +18.91% |
| 小米（SU7） | 1810.HK | 汽车减亏与手机高端化双轮 | 收 Nov 20: 27.640（-3.09%） | 防守 + 双轮增长 |
| 宁德时代 | 300750.SZ | 储能/动力双龙头 | 收 Nov 20: 227.78（-2.90%） | 储能双龙头 |
| 阳光电源 | 300274.SZ | 光伏+储能 | 11/20 69.78（-2.31%） | 光伏+储能线 |

---

## 6. AI 热点主题（事件 → 名称 / 代码 → 市场反应 → 投资逻辑）

| 热点事件 | 名称 / 代码 | 市场反应 | 投资逻辑 |
|---|---|---|---|
| **Nvidia SEC 调查（会计核查）**（live page: "Nvidia stock extends 25-trillion rout as SEC probes its accounting"） | NVIDIA / NVDA | 收 Nov 20 125.53（-14.01%），隔夜 +3.57%（130.01）；Live: Jensen Huang Nov 12 辞去职务，随后 NVDA 累计下跌 14% | SEC 调查加上 AI 交易整体转弱，计算芯片弹性被路径转弱吃掉，AI 仍兑现 |
| **Nvidia Q3 FY27 财报（Nov 17 实报）** | NVIDIA | Revenue $115.84B、Earnings $65.29B、Margin 56.36%；NVDA 收 Nov 20 125.53（-14.01%）；AMD 424.39（-13.25%）；TSM 318.71（-9.48%） | 估值跌幅被路径转弱吃掉，AI 资本开支/算力租赁预期放缓，跟随弹性回归；YTD -32.69%（矛盾，已标注） |
| **NVIDIA GPP 需求兑现** | NVIDIA / SMCI | SMCI 收 Nov 20 21.65（-9.19%）；NVIDIA 隔夜 +3.57% | 周期见顶压抑，关注 AVGO 相对安全侧 |
| **NVIDIA AI 资本开支/算力租赁预期** | NVIDIA / CoreWeave | CoreWeave 收 Nov 20 39.51（-9.07%）；怀疑关联 NVIDIA 放缓 | 算力链弹性在退，关注企业 AI 端的二次补洁点 |
| **数据中心需求（NVIDIA → Schnieder Electric）** | NVIDIA | Simply Wall St 报告（约 41m ago）；NVDA 隔夜快照 +3.57% | 数据中心下游弹性在 NVIDIA 打压后恢复 |
| **Anthropic IPO（招股 ANT）** | Anthropic | 首日交易：股价约 $86（10:55 AM ET）盘旋，定价 $83，跌 8%–12%；市值 $1.5 万亿 | 等待定价稳定，关注 Secondary 行情节奏（S-1 已预估：营收 $163 亿、净亏损 >$800 亿，估值 >$1.4T） |
| **AI 防守层消退（防守股下行）** | NTES | 收 Nov 20 99.85（-4.85%）；PE 13.75；Revenue 27.85B，Margin 30.17% | 防守阵地指数（Tencent、Xiaomi、Baidu）承压反映 AI 投入争清 |
| **机器人/AI 选项空间** | TSLA / LI / XPEV | 跟随 EV 指数：TSLA 收 Nov 20 345.82；LI 10.39（-7.56%）；XPEV 8.16（-13.86%） | AI 选项是 LI/TSLA 的叙事续板，但目前估值对冲大 |

---

## 7. 跨市场投资逻辑

- **美股 AI 强势**：AMD/TSM/PLTR/AVGO 构成 AI 弹性侧（隔夜 +3.53%/+3.10%，NVDA +3.57%）；NVIDIA 页面低点（-14.01%）= 计算芯片估值接近底部（PE 13.48），防守空间等待 AI 弹性到齐。
- **港股平台股跟随**：阿里 +3.48% 与 Tencent -1.26%、Baidu -4.04%、Xiaomi -3.09% 分化；平台股投资线性：估值退税已见顶，云出海+Temu 混排（Q2 2027 earnings call 可见）。
- **A 股 AI 链条分化**：海光 -8.75% 体现强度；中际旭创 -3.72%（光模块龙头）。
- **ADR 分化，筹码挤出**：PDD -0.33% 与美股此时相比跟随指数；防守 ADR（NTES -4.85%、XPEV -13.86%、NIO -7.89%、LI -7.56%）跟随 US 矿路径。
- **宏观/总线**：US 偏弱：S&P 500 -3.70%、Nasdaq -5.28%、VIX +26.20%；AI 交易继续给给解释权（Nvidia SEC 调查 + 财报分化）。

---

## 8. 风险提示

- **市场数据时点限制**：US 数据为常规收盘（Nov 20）+ 隔夜快照；港/A 为常规收盘快照（≈ Nov 20）；今日（2026-11-22）三地均休市，价格面停留在最近一次收盘，事件面来自 Yahoo live markets 页（休市日新闻，未经过收盘价格验证）。
- **Yahoo 页面展示数据存在部分不完整**：Google 搜索被登录验证拦截、部分股票页面无有效数据；**未取得条目**：中科曙光（603019.SH）、中微公司 11/21（688012.SH）、新易盛（光模块）、三六零（601360.SH 已退市/停牌）、BIDU US ADR、SMIC 11/21 数据、Kuaishou/NetEase 11/21 数据（11/20: -12.59% 20.140 / -18.35% 152.600）。
- **投资逻辑没有价值建议**：此报告基于投资者视角收集信息，不构成投资建议；实际操作前请核实最新报价与财务基本面。
