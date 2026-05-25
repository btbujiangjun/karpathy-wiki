---
title: "Foundation Protocol: A Coordination Layer for Agentic Society"
title-zh: "Foundation Protocol：面向智能体社会的协调层协议"
type: paper
created: 2026-05-25
updated: 2026-05-25
authors: [Bang Liu, Yongfeng Gu, Jiayi Zhang, Zhaoyang Yu, Sirui Hong, Maojia Song, Xiaoqiang Wang, Mingyi Deng, Zijie Zhuang, Ronghao Wang, Mingzhe Cao, Yutong Zhu, Xingjian Li, Yifan Wu, Jianhao Ruan, Yiran Peng, Shuangrui Chen, Jinlin Wang, Yizhang Lin, Dongjie Zhang, Dekun Wu, Chen Ma, Lizi Liao, Han Yu, Jian Pei, Heng Ji, Qiang Yang, Yuyu Luo, Chenglin Wu]
year: 2026
arxiv: 2605.23218
affiliation: Multiple (Tencent, HKUST, UIUC)
tags: [agents, multi-agent, protocol, coordination]
category: agents
---

## 问题背景

随着 AI Agent 的广泛应用，多 Agent 系统（Multi-Agent System）已从实验室走向生产环境。但不同团队开发的 Agent 使用不同的通信协议、任务描述格式和执行规范，导致 Agent 之间无法协作——相当于早期的计算机网络缺少 TCP/IP 协议栈。Foundation Protocol 旨在为"Agent 社会"提供一个标准化的协调层。

## 方法详述

Foundation Protocol 定义了 Agent 间通信和协作的标准接口，包括：

**核心层：**
1. **消息层**：标准化的 Agent 间消息格式（类 HTTP/gRPC 但专门为 Agent 设计）
2. **发现层**：Agent 如何注册、广播和发现其他 Agent 的能力
3. **任务层**：任务描述、分解、分配和结果报告的标准格式
4. **信任层**：Agent 身份验证、执行证明、结果签名

**关键设计原则：**
- 去中心化：无中心协调节点，Agent 之间点对点通信
- 可扩展性：新类型的 Agent 可以即插即用，无需全局注册
- 安全优先：内置身份验证和结果证明机制

## 主要创新点

- **Agent 社会的基础设施协议**：类比互联网的 TCP/IP，为多 Agent 系统提供标准化通信范式
- **产学研联合提案**：腾讯、HKUST、UIUC 等多家机构的联合工作，增大了被广泛采用的可能性
- **end-to-end设计**：从消息格式到信任机制，覆盖多 Agent 协作的全栈需求

## 实验结果与对比

| 能力 | 无协议（直接调用） | 私有协议 | Foundation Protocol |
|------|------------------|---------|-------------------|
| 跨组织 Agent 通信 | ❌ 不支持 | ⚠️ 有限 | ✅ 原生支持 |
| Agent 发现 | ❌ 需硬编码地址 | ⚠️ 部分支持 | ✅ 自动发现 |
| 任务分解与分配 | ❌ 手动 | ⚠️ 固定流程 | ✅ 标准化 |
| 结果验证 | ❌ 无 | ⚠️ 有限 | ✅ 签名证明 |
| 安全/身份验证 | ❌ 无 | ⚠️ 实现依赖 | ✅ 内置 |

**核心结论：** 目前处于标准提案阶段，尚未有大规模部署验证。但从设计完整性来看，它是当前最接近"Agent 社会 TCP/IP"的方案。如果被广泛采纳，将根本上改变多 Agent 系统的构建方式。

## 局限性

- 目前是协议提案阶段，尚无大规模实际部署验证
- 协议设计的完整性需要在真实复杂场景中验证，可能存在未预见的边界情况
- 去中心化设计在性能上可能不如中心化调度，尤其是在高吞吐场景中
- 需要生态系统的共同采纳，单个组织的采纳价值有限
