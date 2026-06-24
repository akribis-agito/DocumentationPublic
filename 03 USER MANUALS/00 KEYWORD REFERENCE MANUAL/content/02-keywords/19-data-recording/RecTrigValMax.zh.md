---
keyword: RecTrigValMax
summary: 基于范围的触发激活逻辑（RecTrigTyp 9–12）的上界值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 293
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 4
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float64
    range: null
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# RecTrigValMax

基于范围的触发激活逻辑（RecTrigTyp 9–12）的上界值。

## 概述

`RecTrigValMax` 存储基于范围的触发激活逻辑中的最大值（上界）。仅当对应的 [RecTrigTyp](RecTrigTyp.md) 为范围相关类型（`9`、`10`、`11` 或 `12`）时适用，与 [RecTrigVal](RecTrigVal.md) 的下界配对使用。每个索引对应不同的触发器。

| 索引 | 示波器编号 | 触发器 |
|---|---|---|
| 1 | 1（第一） | 1 |
| 2 | 1（第一） | 2 |
| 3 | 1（第一） | 3 |
| 4 | 2（第二） | 1 |
| 5 | 2（第二） | 2 |
| 6 | 2（第二） | 3 |

有关最大值的使用方式，请参阅 [RecTrigTyp](RecTrigTyp.md)。

当触发源（[RecTrigSrc](RecTrigSrc.md)）是以用户单位表示的变量时，上界以相同的用户单位进行解释：在 [RecStart](RecStart.md) 时，上界从用户单位转换为控制器内部单位后再与触发源进行比较，处理方式与 [RecTrigVal](RecTrigVal.md) 完全一致。对于无用户单位缩放的触发源，比较值直接进行比较。在 v4 中，若转换后的上界超出 32 位整数范围，`RecStart` 将返回错误并被拒绝。

> **注意：** 在 v4 中，上界值为 32 位整数。在 v5（Central-i）中，上界值为 64 位浮点数，因此可以直接指定非整数范围边界。

## 示例

```text
ARecTrigValMax[1]=2000   ; 第一示波器触发器 1 的范围上界
ARecTrigValMax[1]       ; 查询触发器 1（第一示波器）的上界
```

## 另请参阅

- [RecTrigTyp](RecTrigTyp.md) — 触发激活类型（范围类型 9–12）
- [RecTrigVal](RecTrigVal.md) — 范围下界
- [RecTrigSrc](RecTrigSrc.md) — 触发源变量
