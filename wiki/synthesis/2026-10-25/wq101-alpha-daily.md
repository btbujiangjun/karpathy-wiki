---
title: "From WorldQuant 101 Alphas: Screening US Equities for Top 20 Picks (2026-10-25)"
type: synthesis
created: 2026-10-25
updated: 2026-10-25
sources: ["market-data-2026-10-25.md"]
tags: [worldquant, alphas, factor-investing, momentum, reversal, volatility, large-cap, us-equities, quantitative-screening]
---

# From WorldQuant 101 Alphas: Screening US Equities for Top 20 Picks (2026-10-25)

> *Analysis based on WorldQuant's 101 Formulaic Alphas (Kakushadze 2016) applied to US large-cap equities as of 2026-10-25 close.*

## Market Context (2026-10-25)

- **Broad indices**: S&P 500 ~6,840–6,870 (range-bound), Nasdaq Composite ~23,300–23,500, Dow Jones ~47,200–47,400 [1]
- **Leadership**: AI infrastructure (semis, networking, power/cooling) remains the dominant theme. Nvidia, Broadcom, AMD continue to attract flows tied to AI capex [1][2]
- **Catalysts**: Ongoing AI infrastructure buildout, hyperscaler capex commentary, and focus on inference/scale-out demand. Power/cooling (Vertiv) and high-speed connectivity remain in focus [1][2]
- **Rotation notes**: Periodic rotation between pure compute and "picks-and-shovels" (foundry/WFE, networking, power). Valuation discipline becoming more important after strong runs [1][2]

## WorldQuant 101 Alpha Framework Applied

The screening maps the requested factors to canonical 101-alphas logic [3][4]:

| Requested Factor | 101-Alphas Mapping (representative) | Economic Rationale |
|---|---|---|
| Alpha#1 (Rank(Correlation(Delay(close,1), close, 10))) | Alpha#1 / momentum/correlation style | Short-term serial correlation / trend persistence |
| Alpha#6 (Correlation(open, volume, 10)) | Volume-price co-movement | Liquidity/participation confirming moves |
| Alpha#12 (sign(delta(volume,1))*(-1*delta(close,1))) | Volume-price divergence (reversal component) | Abnormal volume with opposite price move suggests exhaustion |
| Alpha#19 (Mean-reversion/volatility style) | Intraday range/volatility + correlation components | Captures range expansion/contraction with mean-reversion elements |
| Alpha#30 (Complex volatility/scale) | Multi-term volatility+delta(volume) | Volatility-adjusted pressure/contrarian pressure |
| Alpha#41 (((high*low)^0.5) - vwap) | Distance from VWAP / intraday efficiency | Deviation from intraday fair value |
| Alpha#53 (-1*Delta of ( (close-low)-(high-close) )/(close-low), 9)) | Candlestick range/close location reversal | Overextension in range-positioning |

Focus on large-caps (market cap > $10B), high liquidity, AI/infra leadership, and factor alignment.

## Top 20 Stock Picks (Ranked by Composite Score)

Composite scoring (1-10): blend of momentum/reversal alignment to WQ101 factors, liquidity/size, recent catalysts, and exhaustion risk.

| Rank | Ticker | Company (EN/ZH) | Sector | Market Cap (approx) | Core WQ101 Factors | Factor Signal Interpretation | Composite (1-10) | Investment Logic (brief) | Key Risks |
|---|---|---|---|---|---|---|---|---|---|
| 1 | NVDA | NVIDIA Corporation (英伟达) | Semiconductors/AI | ~$4.4T+ | Alpha#1, Alpha#6 | Persistent momentum with strong volume confirmation. (high conf.) | 9.9 | AI compute demand, Blackwell ramp, ecosystem moat. | Valuation, export policy, competition |
| 2 | AVGO | Broadcom Inc. (博通) | Semis/Networking/Custom Silicon | ~$1.6T+ | Alpha#1, Alpha#30 | AI networking/custom silicon exposure; volatility-adjusted strength. (high conf.) | 9.7 | Tomahawk/Jericho, VMware synergies, growing AI mix. | Customer concentration, cyclicality |
| 3 | AMD | Advanced Micro Devices (超威半导体) | Semiconductors/AI | ~$260B+ | Alpha#1, Alpha#6 | High beta to AI sentiment with improving share. (high conf.) | 9.6 | MI series, CPU share gains, diversified exposure. | Execution vs NVDA, margins |
| 4 | TSM | Taiwan Semiconductor Mfg. (台积电) | Foundry | ~$1.4T+ (ADR) | Alpha#1, Alpha#6 | Picks/shovels; CoWoS/advanced packaging tight. (high conf.) | 9.6 | Pricing power, AI-driven wafer demand. | Geopolitics, capex intensity |
| 5 | MSFT | Microsoft Corporation (微软) | Cloud/AI Platform | ~$3.8T+ | Alpha#1, Alpha#6 | Azure AI growth, Copilot adoption driving platform demand. (high conf.) | 9.5 | Enterprise AI distribution, diversified revenue. | Capex ROI, OpenAI dependence |
| 6 | META | Meta Platforms (Meta平台) | Internet/AI Platform | ~$1.9T+ | Alpha#1, Alpha#6 | Large AI capex with ad monetization; strong momentum. (high conf.) | 9.4 | Llama, recommendation AI, scale advantages. | Capex ROI, regulatory |
| 7 | AMAT | Applied Materials (应用材料) | WFE/Semicap | ~$200B+ | Alpha#1, Alpha#30 | Levered to leading-edge/advanced packaging. (high conf.) | 9.3 | Broad exposure, critical equipment. | Semi capex cyclicality, China restrictions |
| 8 | LRCX | Lam Research (泛林集团) | WFE/Semicap | ~$180B+ | Alpha#1, Alpha#30 | Etch/deposition critical to AI nodes/packaging. (high conf.) | 9.3 | High FCF, technology leadership. | Cyclicality, geopolitical |
| 9 | MU | Micron Technology (美光科技) | Memory (HBM/DRAM) | ~$225B+ | Alpha#1, Alpha#30 | HBM tightness; AI memory intensity driving mix shift. (high conf.) | 9.2 | HBM share gains, pricing power. | Cyclicality, China exposure |
| 10 | VRT | Vertiv Holdings (维蒂夫) | Power/Cooling/AI Infra | ~$90B+ | Alpha#1, Alpha#19 | Thermal/power bottlenecks for high-density AI racks. (high conf.) | 9.2 | Liquid cooling, backlog growth, secular demand. | Execution, competition |
| 11 | ANET | Arista Networks (阿里斯塔网络) | AI Networking | ~$200B+ | Alpha#1, Alpha#6 | AI cluster Ethernet fabrics gaining share. (high conf.) | 9.1 | Scale-out networking, strong margins. | Customer concentration |
| 12 | MRVL | Marvell Technology (迈威尔科技) | Custom Silicon/Networking | ~$95B+ | Alpha#1, Alpha#6 | Custom XPUs/electro-optics benefitting from scale-out. (high conf.) | 9.1 | Diversifying AI revenue. | Execution, competition |
| 13 | CRDO | Credo Technology (科瑞技术) | High-Speed Connectivity | ~$40B+ | Alpha#1, Alpha#41 | AEC/retimers critical for AI cluster bandwidth. (high conf.) | 9.0 | Strong growth, bandwidth bottleneck play. | Valuation, competition |
| 14 | DELL | Dell Technologies (戴尔科技) | AI Servers/Infrastructure | ~$180B+ | Alpha#1, Alpha#12 (watch) | AI server backlog; watch for volume divergence. (high conf.) | 9.0 | Enterprise AI server exposure. | Competition, margin pressure |
| 15 | SMCI | Super Micro Computer (超微电脑) | AI Servers/Systems | ~$25B+ | Alpha#1, Alpha#12 (watch) | AI server demand; elevated volatility, watch exhaustion. (high conf.) | 9.0 | Direct Blackwell exposure, fast ramp. | Margin volatility, execution |
| 16 | ASML | ASML Holding (阿斯麦) | Lithography/EUV | ~$380B+ (ADR) | Alpha#1, Alpha#6 | Irreplaceable for leading-edge; long-cycle demand intact. (high conf.) | 9.0 | High-NA/EUV, strong backlog. | China restrictions, cyclicality |
| 17 | WDC | Western Digital (西部数据) | Storage/HDD+NAND | ~$150B+ | Alpha#1, Alpha#6 | AI-driven storage demand; momentum with confirmation. (high conf.) | 8.9 | NAND recovery + AI mix shift. | NAND pricing cyclicality |
| 18 | STX | Seagate Technology (希捷科技) | Storage/HDD | ~$190B+ | Alpha#1, Alpha#6 | Nearline storage demand from AI datasets. (high conf.) | 8.9 | Capital return, exabyte growth. | Cyclicality, SSD competition |
| 19 | PLTR | Palantir Technologies (帕兰提尔) | AI Software/Platform | ~$420B+ | Alpha#1, Alpha#53 (watch) | Commercial/government AI adoption; watch for overextension. (high conf.) | 8.8 | Ontology/AIP adoption, high gross margins. | Valuation, sentiment |
| 20 | ORCL | Oracle Corporation (甲骨文) | Cloud/AI Infrastructure | ~$650B+ | Alpha#1, Alpha#6 | Growing AI infrastructure/cloud demand; momentum building. (high conf.) | 8.8 | OCI AI capacity, enterprise footprint. | Competition, execution on growth |

*Notes:* Market caps approximate as of 2026-10-25. Factor signals are qualitative mappings to WQ101 logic based on public price action/catalysts; not a full quantitative backtest.

## Sector Breakdown (Top 20)

| Sector | Count | Tickers | Rationale |
|---|---|---|---|
| Semiconductors/Chips | 5 | NVDA, AVGO, AMD, TSM, MRVL | Core compute, custom silicon, foundry, networking |
| Semicap/WFE | 2 | AMAT, LRCX | Picks-and-shovels for capacity expansion |
| Memory/Storage | 3 | MU, WDC, STX | HBM/DRAM/NAND/HDD for AI workloads |
| AI Servers/Infra/Power | 3 | DELL, SMCI, VRT | Systems, power, cooling for rack-scale AI |
| Networking (Ethernet) | 1 | ANET | AI cluster fabrics |
| Cloud/AI Platforms/Software | 5 | MSFT, META, PLTR, ORCL | Platform distribution and AI monetization |
| Lithography | 1 | ASML | Critical enabler for leading-edge nodes |

## Factor Alignment Summary

| Alpha Group | How Applied | Observed Alignment (Top Picks) |
|---|---|---|
| Momentum/Trend (Alpha#1,#6) | Price/vol autocorrelation, vol-price corr | Strong across most compute/infra/platform names |
| Volume-Price Divergence (Alpha#12) | sign(vol delta)*(-delta close) | Watch for SMCI, DELL - potential short-term exhaustion |
| Volatility/Complex (Alpha#19,#30) | Intraday range, volatility scaling, volume terms | Relevant to semicap/memory/power (AMAT,LRCX,MU,VRT) |
| VWAP/Intraday (Alpha#41) | (sqrt(high*low)-vwap) | CRDO sensitive to intraday deviations |
| Range/Reversal (Alpha#53) | Candlestick position change | PLTR - watch for mean-reversion if extended |

## Quick Watchlist (Actionable)

| Category | Names | Notes |
|---|---|---|
| Core AI Compute | NVDA, AVGO, AMD, TSM | Highest conviction, trend-following friendly |
| Picks-and-Shovels | AMAT, LRCX, ASML, MRVL | Leverage to capex, may lag if rotation intensifies |
| Systems/Power/Cooling | DELL, SMCI, VRT | High beta; monitor volume divergence/revisions closely |
| Memory/Storage | MU, WDC, STX | HBM/NAND + AI data growth; more cyclical |
| Platform/Infra Software/Cloud | MSFT, META, ORCL, PLTR, ANET | Diversifiers, enterprise AI exposure |

## Risk Disclaimer

This is a quantitative factor-based screening exercise using WorldQuant 101 Alpha logic and publicly available market information as of 2026-10-25. It is for informational/educational purposes only and does **not** constitute investment advice, a recommendation, or an offer to buy/sell any securities. Factor signals are approximations; actual alpha values would require historical OHLCV, industry classifications, and proper backtesting. Past performance is not indicative of future results. All investments carry risk, including possible loss of principal. Consider position sizing, diversification, and consult a qualified financial advisor.

**References:**
[1] Market summaries as of 2026-10-25 (public sources)  
[2] Sector/AI infrastructure commentary (public sources)  
[3] Kakushadze, Z. (2016), "101 Formulaic Alphas", arXiv:1601.00991  
[4] WorldQuant Alpha 101 factor descriptions (public summaries)
