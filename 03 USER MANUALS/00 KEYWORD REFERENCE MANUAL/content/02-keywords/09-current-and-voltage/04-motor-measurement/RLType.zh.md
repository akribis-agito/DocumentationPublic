---
keyword: RLType
summary: 选择 PCSuite 的 R/L 测量结果以相数据（0）还是线间（线对线）数据（1）报告。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 375
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
  - 0
  - 1
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# RLType

选择 PCSuite 的 R/L 测量结果以相数据（0）还是线间（线对线）数据（1）报告。

## 概述

`RLType` 定义 PCSuite 的电阻与电感测量工具所进行测量的类型。它决定如何解释所测得的 [Rm](Rm.md) 和 [Lm](Lm.md) 值（相数据还是线间数据）。

## 工作原理

`RLType` 是一个存储的、闪存存储的轴相关参数，用于标记如何读取所记录的 [Rm](Rm.md) 和 [Lm](Lm.md) 值。它是一个二值选择器，默认值为 1（线间）：

| RLType | 测量类型  |
|--------|-------------------|
| 0      | 相数据        |
| 1      | 线间数据（默认） |

`RLType` 是对所存储的 [Rm](Rm.md) 和 [Lm](Lm.md) 值如何测得的记录；控制器并不查阅它。特别地，对于三相无刷电机，v5 电压前馈始终将所存储的 `Rm`/`Lm` 视为线间值（在内部将其减半以得到每相值），无论 `RLType` 设置如何。

## 示例

```text
ARLType=1            ; report line-to-line data (default)
ARLType=0            ; report phase data
```

## 参见

- [Rm](Rm.md) — 测得的电机电阻
- [Lm](Lm.md) — 测得的电机电感
