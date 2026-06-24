---
summary: 在龙门运动前初始化龙门映射校正功能。
keyword: GantryMapInit
availability:
  standalone: []
  central-i:
  - v5
can_code: 752
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int64
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - -2251799813685248
  - 2251799813685247
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# GantryMapInit

对应龙门解耦映射表第一个条目的位置。

## 概述

`GantryMapInit` 设置 [GantryMap](GantryMap.md) 表中**第一个**条目适用的位置（以 [GantryMapSrc](GantryMapSrc.md) 所选源的单位表示）。结合映射间距，它确定每个表条目在横梁上的位置：条目 1 位于 `GantryMapInit`，条目 2 在此基础上再向前一个间距，以此类推。该参数为 64 位轴范围值，可保存至闪存，可在电机使能时设置但不能在运动中设置。默认值为 `0`。仅适用于 central-i（v5）。

在构建映射表之前，将 `GantryMapInit` 设置为表起始位置所对应的源位置；结合映射间距，它确定了映射表覆盖的位置窗口。

## 工作原理

当位置相关映射表激活时（[GantryMapType](GantryMapType.md) = 1），控制器将实时源位置减去 `GantryMapInit` 并除以映射间距，将其转换为表索引，然后在两个相邻的 [GantryMap](GantryMap.md) 条目之间进行线性插值（实时结果为 [GantryMapVal](GantryMapVal.md)）。等于 `GantryMapInit` 的源位置落在条目 1 上；低于该值的位置钳位至条目 1，超过最后一个条目的位置钳位至最后一个条目。

## 示例

```text
AGantryMapInit=0     ; 第一个映射条目对应源位置 0
AGantryMapInit       ; 读取已配置的起始位置
```

### 边界情况

- **运动中写入**——被拒绝（`NOMOTN`）。可在电机使能时更改。
- **映射类型关闭**（[GantryMapType](GantryMapType.md) = 0）——已存储但**不被查询**。
- **位置低于初始值**——索引低于条目 1 时钳位至条目 1；控制器不向起始位置左侧进行外推。
- **位置超过最后一个条目**——钳位至最后一个已填写的条目；若工作范围超过表格，请考虑增加 [GantryMap](GantryMap.md) 条目或移动 `GantryMapInit`。
- **设置在错误轴上**——仅在主轴上读取；其他轴的写入虽被存储，但将被忽略。
- **保存**——可保存至闪存；启动时重新加载。
- **平台**——仅限 v5 central-i。

## 另请参阅

- [GantryMap](GantryMap.md) — 此参数确定第一个条目位置的解耦比值表
- [GantryMapSrc](GantryMapSrc.md) — 此起始位置所对应单位的源
- [GantryMapType](GantryMapType.md) — 启用映射表的使用
- [GantryMapVal](GantryMapVal.md) — 实时插值比值
