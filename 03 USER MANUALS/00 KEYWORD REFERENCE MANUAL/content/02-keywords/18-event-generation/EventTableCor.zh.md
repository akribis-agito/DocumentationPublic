---
keyword: EventTableCor
summary: 由 EventCorrect 生成的已校正事件位置的只读数组。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 315
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 101
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-10-25'
doc_revision: '2026.10'
---
# EventTableCor

由 EventCorrect 生成的已校正事件位置的只读数组。

## 已验证硬件事件表（EventType=3，且由 EventLoad 会话占用）

[EventLoad](EventLoad.zh.md) 在使能前捕获包含两端的所选范围：N=EventTableEnd−EventTableBeg+1 须为 1..2048。无效范围被拒绝，不会截断或作为单次事件运行。控制器侧大数组保留，但一次硬件会话只使用所选范围。原始坐标和修正后的远程坐标均须按同一方向严格排序，不允许重复、反向或有符号计数器回绕。应先配置再加载；更改使 Ready 失效，传输、使能或运行占用会话时拒绝冲突写入。EventOn=1 不会重新读取或上传实时表。

下文的传统行为也适用于没有已验证表会话占用轴时的 EventType=3。已验证表能力仅限制 EventLoad，不限制传统硬件表使能。

## 概述

`EventTableCor` 是一个只读数组，存储由 [EventCorrect](EventCorrect.md) 计算的位置校正应用后得到的已校正事件位置。它与 [EventTable](EventTable.md) 逐条对应，但已施加编码器误差映射校正，以用户单位表示。这是一个轴相关的数组状态变量，不保存至闪存。

## 工作原理

当轴在活动的编码器误差映射下运行时，[EventTable](EventTable.md) 中的指令表位置与比较器实际看到的*真实*位置并不一致，因为误差映射会对反馈进行偏移。运行 [EventCorrect](EventCorrect.md) 时，系统会遍历每个活动条目，在该位置处查找映射校正值（根据误差映射类型进行 1D、2D 或 3D 插值），并将调整后的值写入对应的 `EventTableCor` 元素。该结果是已校正反馈实际到达预期指令点时的位置。

仅当 [EventTableSrc](EventTableSrc.md) = 1 时，`EventTableCor` 才作为比较器来源使用。当 `EventTableSrc` = 0 时，使用原始 [EventTable](EventTable.md)，`EventTableCor` 被忽略。若使用纯软件比较，反馈已经过校正，因此原始表即已足够，无需使用已校正表。

## 示例

```text
AEventTableCor[1]   ; 读取第一个已校正事件位置
AEventTableCor[2]   ; 读取第二个已校正事件位置
```

## 另请参阅

- [EventTable](EventTable.md) — 未校正的源位置
- [EventCorrect](EventCorrect.md) — 用于计算校正值的指令
- [EventTableSel](EventTableSel.md) — 按条目选择
