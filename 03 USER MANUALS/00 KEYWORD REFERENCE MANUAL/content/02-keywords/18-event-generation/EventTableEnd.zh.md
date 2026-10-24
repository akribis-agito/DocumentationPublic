---
keyword: EventTableEnd
summary: 事件表中活动区域的结束索引。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 185
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 100
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-10-25'
doc_revision: '2026.10'
---
# EventTableEnd

事件表中活动区域的结束索引。

## 已验证硬件事件表（EventType=3）

[EventLoad](EventLoad.zh.md) 在使能前捕获包含两端的所选范围：N=EventTableEnd−EventTableBeg+1 须为 1..2048。无效范围被拒绝，不会截断或作为单次事件运行。控制器侧大数组保留，但一次硬件会话只使用所选范围。原始坐标和修正后的远程坐标均须按同一方向严格排序，不允许重复、反向或有符号计数器回绕。应先配置再加载；更改使 Ready 失效，传输、使能或运行占用会话时拒绝冲突写入。EventOn=1 不会重新读取或上传实时表。

下文的传统行为适用于其他事件模式。

## 概述

`EventTableEnd` 设置 [EventTable](EventTable.md) 中活动区域的结束索引，定义用于事件生成的最后一个条目。它与 [EventTableBeg](EventTableBeg.md) 配合使用，后者标记第一个活动条目。索引从 1 开始（范围 1–100）。这是一个保存至闪存的轴相关参数，可随时修改。

## 工作原理

在表驱动模式（[EventType](EventType.md) = 2）下，控制器从 [EventTableBeg](EventTableBeg.md) 开始，逐条推进 [EventTable](EventTable.md)，每生成一个脉冲递进一个索引。为 `EventTableEnd` 条目产生脉冲后，下一次推进使索引超过 `EventTableEnd`，事件生成停止；控制器将 [EventOn](EventOn.md) 清零为 0。因此，完整一轮产生的脉冲数为 `EventTableEnd − EventTableBeg + 1`，可通过 [EventCntr](EventCntr.md) 确认。

## 示例

```text
AEventTableEnd=10    ; 使用最多到索引 10 的表条目
AEventTableEnd      ; 查询已配置的结束索引
```

## 另请参阅

- [EventTableBeg](EventTableBeg.md) — 第一个活动表索引
- [EventTable](EventTable.md) — 事件位置表
- [EventTableSel](EventTableSel.md) — 按条目选择
