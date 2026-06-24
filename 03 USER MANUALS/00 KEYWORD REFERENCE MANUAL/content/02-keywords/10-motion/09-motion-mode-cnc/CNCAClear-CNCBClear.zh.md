---
summary: 清除 CNC FIFO 队列 A（或 B）中所有待处理段的指令。
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CNCAClear/CNCBClear

清除 CNC FIFO 队列 A（或 B）中所有待处理段的指令。

## 概述

`CNCAClear`（及其在第二 CNC 引擎上的对应项 `CNCBClear`）清除队列 A（或 B）的 CNC 段队列（FIFO）中的所有待处理段，并将其复位，以便从干净状态加载新段。该参数为非轴指令函数。

与 [StopCNCA](StopCNCA.md)/[StopCNCB](StopCNCB.md) 停止运动但保留队列不同，`CNCAClear` 清空由 [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) 加载的队列。

## 工作原理

- 当该队列上的 CNC 运动正在进行时，`CNCAClear` **将被拒绝并返回错误 190（"此 CNC 正在运动中，无法清除 CNC FIFO。"）**。请先停止运动（[StopCNCA](StopCNCA.md)/[StopCNCB](StopCNCB.md)），再执行清除。当队列空闲（或仅在填充但尚未启动运动时），清除操作将被接受。
- 清除操作将队列恢复为空状态：空闲空间计数恢复至最大可用容量（由 [CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md) 的元素 7 报告），队列指针和段 ID 被复位，引擎重新等待第一个段（因此下一次压入必须遵循 [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) 中描述的首段规则）。
- 段末校正计数器 [CNCAEndErrCnt/CNCBEndErrCnt](CNCAEndErrCnt-CNCBEndErrCnt.md) 及速度跳变/加速度限制计数器被复位为 0，各轴的最大速度跳变和加速度限制恢复为默认值。

## 示例

```text
ACNCAClear           ; 清空 FIFO A 中所有排队段
```

## 另请参阅

- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — 已排队的段数据
- [CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md) — 空闲空间及运动状态（必须空闲才能清除）
- [StopCNCA](StopCNCA.md) — 停止运动而不清除队列
- [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) — 向队列压入一个段
- [CNCARemove/CNCBRemove](CNCARemove-CNCBRemove.md) — 仅移除最后一个段
