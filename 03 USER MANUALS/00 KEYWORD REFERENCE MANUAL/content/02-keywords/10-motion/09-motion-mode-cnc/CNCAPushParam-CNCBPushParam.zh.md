---
summary: 将 CNC 段的参数值推入 CNC FIFO。
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CNCAPushParam/CNCBPushParam

将 CNC 段的参数值推入 CNC FIFO。

## 概述

`CNCAPushParam`（及其在第二 CNC 引擎上的对应项 `CNCBPushParam`）为当前正被推入队列 A（或 B）的 CNC 段队列（FIFO）中的段提供一个参数值。它始终跟随在 [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) 之后使用——后者打开段并确定该段所需的参数数量；随后所需数量的 `CNCAPushParam` 写操作将完成该段。当最后一个预期参数被推入时，该段**关闭**并成为可供回放的队列条目。

如需通过以太网在单条消息中推送完整段（类型及所有参数），请参阅 [CNCAPushSeg/CNCBPushSeg](CNCAPushSeg-CNCBPushSeg.md)。

## 工作原理

使用 `CNCAPushType` 打开段时，会记录该段所需的参数总数（参见 [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) 中的段类型表）。每次 `CNCAPushParam` 写操作执行如下操作：

- 若当前没有打开的段——即队列为空或上一个段已关闭——则操作被拒绝并返回错误。必须先执行 `CNCAPushType`。
- 该值被存入队列，仍需参数的计数减一。
- 当计数归零时，该段**关闭**：其参数作为一个整体进行验证（例如，路径速度和终止速度必须在允许的速度范围内，段的长度必须足够，圆弧或螺旋线从圆心推导出的起始和终止半径必须在允许的精度范围内一致）。验证失败将拒绝该段。（与上一段终止速度的路径连续性检查则在较早阶段进行，即使用 `CNCAPushType` 打开下一段时。）

参数必须按照段类型规定的顺序依次推入。在段关闭之前，它不具备回放资格，因此队列尾部有一个半推送状态的段并不能防止[欠运行](CNCAPushType-CNCBPushType.md)——运动引擎将"最后一个段仍在填充中"与"没有可用段"同等对待。

空闲队列槽的数量由 [CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md) 报告。整个段的空间在使用 `CNCAPushType` 打开段时预留，队列过满也在此处被拒绝；单个 `CNCAPushParam` 写操作不进行额外的空间检查，`CNCAPushParam` 写操作可能返回的唯一错误是"无打开的段"。

## 示例

```text
ACNCAPushType=value  ; 打开，例如一个双轴直线运动（需要 4 个参数）
ACNCAPushParam=1000  ; 参数 1：第一轴目标位置
ACNCAPushParam=2000  ; 参数 2：第二轴目标位置
ACNCAPushParam=50000 ; 参数 3：路径速度
ACNCAPushParam=0     ; 参数 4：终止速度 -> 段现已关闭并排入队列
```

## 另请参阅

- [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) — 打开段并选择其类型
- [CNCAPushSeg/CNCBPushSeg](CNCAPushSeg-CNCBPushSeg.md) — 通过单条以太网消息推送完整段
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — 队列段数据
- [CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md) — 空闲槽数量及已打开段仍需参数的数量
