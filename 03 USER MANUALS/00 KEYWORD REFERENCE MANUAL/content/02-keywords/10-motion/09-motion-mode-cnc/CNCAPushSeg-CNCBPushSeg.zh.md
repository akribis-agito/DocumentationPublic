---
summary: 通过单条以太网消息推送完整 CNC 段（类型和参数）。
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CNCAPushSeg/CNCBPushSeg

通过单条以太网消息推送完整 CNC 段（类型和参数）。

## 概述

`CNCAPushSeg`（及其在第二 CNC 引擎上的对应项 `CNCBPushSeg`）使用单条以太网消息将一个完整段——其类型、涉及轴及所有参数——推入队列 A（或 B）的 CNC 段队列（FIFO）。它将一条 [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) 加上所需数量 [CNCAPushParam/CNCBPushParam](CNCAPushParam-CNCBPushParam.md) 写操作的多消息序列合并为单次传输，从而显著提高段的加载速率——这是保持队列充足以避免在流式传输密集路径时发生[欠运行](CNCAPushType-CNCBPushType.md)的主要因素。

> **注意：** 本关键字仅支持通过以太网通信连接至控制器。通过其他连接（如 RS-232 或 CAN）使用时将返回错误；在这些链路上，请改用 `CNCAPushType` 和 `CNCAPushParam` 推送段。

## 工作原理

消息携带与 [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) 相同的类型/涉及轴字（高字节 = 段类型，低 24 位 = 最多六个涉及轴），后跟该段类型所需数量的参数值，顺序与单独的 `CNCAPushParam` 写操作相同。有关段类型和参数表，请参阅 [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md)。

控制器将该段处理为等效的一次类型推送加上每次参数推送的序列，然后关闭它，使其立即具备回放资格。队列中的行为、回放期间以及耗尽时的行为与多消息方式推送的段完全相同。

提供的参数值数量必须与段类型所需的数量完全匹配；若不匹配，消息将被预先拒绝，且不会向队列添加任何内容。在段打开之前被捕获的错误——无效或超出范围的类型、顺序违规（例如"设置初始位置"段不是第一个）或整段空间不足——同样会干净地拒绝推送。但是，仅在段关闭时才能检测到的值验证失败（例如圆弧半径不一致、段过短或速度超出范围）会在报告错误时*已经*将该段的类型条目及其早期参数写入队列，留下一个部分构建、未关闭的段。对于这种情况，请通过 [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) 刷新队列来恢复。

## 示例

```text
ACNCAPushSeg=...     ; 通过以太网推送一个完整段（类型 + 参数）
```

## 另请参阅

- [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) — 段类型编码和参数数量
- [CNCAPushParam/CNCBPushParam](CNCAPushParam-CNCBPushParam.md) — 逐个推送段参数
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — 队列段数据
- [CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md) — 空闲槽和队列状态
- [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) — 刷新所有待处理段
