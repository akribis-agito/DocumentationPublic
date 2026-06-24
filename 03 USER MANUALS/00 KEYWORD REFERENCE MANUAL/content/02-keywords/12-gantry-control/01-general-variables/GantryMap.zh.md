---
summary: 应用于龙门偏摆轴的有效误差映射校正值。
keyword: GantryMap
availability:
  standalone: []
  central-i:
  - v5
can_code: 748
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 1025
  data_type: float64
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0.0
  - 1.0
  default: 0.5
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# GantryMap

龙门位置相关解耦比值表。

## 概述

`GantryMap` 保存当位置相关龙门映射表启用时（[GantryMapType](GantryMapType.md) = 1）所使用的解耦比值表。每个条目为 **0.0 至 1.0** 范围内的比值（默认 **0.5**），描述在横梁上某给定位置处龙门如何在两个电机之间进行分配。0.5 表示对称分配；偏离 0.5 的值将受控中点移向一侧，从而可对非均匀机构在整个行程中进行线性化。该参数为主轴上可保存至闪存的数组。

该表**从 1 开始索引**，最多提供 **1024 个可用条目**。选择条目的位置来自 [GantryMapSrc](GantryMapSrc.md) 所选的源；第一个条目对应位置 [GantryMapInit](GantryMapInit.md)，相邻条目之间相距一个映射间距（间距由相关关键字 `GantryMapGap` 设置）。控制器在条目之间进行线性插值，并将实时结果报告为 [GantryMapVal](GantryMapVal.md)。仅适用于 central-i（v5）。

## 工作原理

当映射表激活时，每个控制周期控制器从 [GantryMapSrc](GantryMapSrc.md) 获取当前位置，相对于 [GantryMapInit](GantryMapInit.md) 和映射间距将其转换为分数表索引，并在两个相邻的 `GantryMap` 条目之间进行线性插值以获得有效比值。低于第一个条目的位置钳位至条目 1；超过最后一个可用条目的位置钳位至最后一个条目。插值比值随后以两种方式应用：

- **反馈合并**——加权两个电机编码器位置合并为龙门线性反馈的方式（而非简单的 50/50 均值）。
- **电流分配**——加权合并后的线性和偏摆电流指令分配给两个电机的方式。

即使在机构不对称的位置，这也能保持线性轴与偏摆轴的解耦。构建表格时，使每个条目保存其所代表横梁位置处正确的局部分配比值；各处均为特殊值 0.5 则等效于固定对称龙门。

## 示例

```text
AGantryMap[1]        ; 读取表中第一个解耦比值
AGantryMap[1]=0.5    ; 将第一个条目设为对称分配
AGantryMapVal        ; 读取当前位置的实时插值比值
```

### 边界情况

- **索引 0**——无效；有效索引为 `GantryMap[1]`–`GantryMap[1024]`。`GantryMap[0]` 不存在。
- **运动中写入**——被拒绝（`NOMOTN`）。可在电机使能时编辑映射表，但不能在运动中操作。
- **映射类型关闭**（[GantryMapType](GantryMapType.md) = 0）——表格已存储但**不被查询**；龙门使用固定的 50/50 对称分配。
- **超出表范围**——低于 [GantryMapInit](GantryMapInit.md) 的位置钳位至条目 1；超过条目 1024 的位置钳位至最后一个已填写的条目。
- **超出范围的值**——写入时，`[0.0, 1.0]` 之外的条目将被拒绝；有效比值为 0.0–1.0，默认对称值为 0.5。
- **设置在错误轴上**——引擎在**主轴**上读取 `GantryMap`。其他轴的写入虽被接受，但不会被查询。
- **保存**——可保存至闪存；大型表格在重启后保持不变。
- **平台**——仅限 v5 central-i。

## 另请参阅

- [GantryMapType](GantryMapType.md) — 启用此表的使用
- [GantryMapSrc](GantryMapSrc.md) — 用于索引此表的位置源
- [GantryMapInit](GantryMapInit.md) — 对应第一个表条目的位置
- [GantryMapVal](GantryMapVal.md) — 从表中读取的实时插值比值
