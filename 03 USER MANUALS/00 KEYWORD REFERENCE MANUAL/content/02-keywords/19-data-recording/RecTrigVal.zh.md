---
keyword: RecTrigVal
summary: 每个触发器的触发激活逻辑中使用的比较值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 246
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
# RecTrigVal

每个触发器的触发激活逻辑中使用的比较值。

## 概述

`RecTrigVal` 存储 [RecTrigTyp](RecTrigTyp.md) 所选触发激活逻辑中使用的比较值。对于范围类型，该值为下界，与 [RecTrigValMax](RecTrigValMax.md) 的上界配对使用。比较值与经掩码处理后的触发源值进行比较。每个索引对应不同的触发器。

| 索引 | 示波器编号 | 触发器 |
|---|---|---|
| 1 | 1（第一） | 1 |
| 2 | 1（第一） | 2 |
| 3 | 1（第一） | 3 |
| 4 | 2（第二） | 1 |
| 5 | 2（第二） | 2 |
| 6 | 2（第二） | 3 |

有关比较值的使用方式，请参阅 [RecTrigTyp](RecTrigTyp.md)。

当触发源（[RecTrigSrc](RecTrigSrc.md)）是以用户单位表示的变量时，比较值以相同的用户单位进行解释：在 [RecStart](RecStart.md) 时，阈值从用户单位转换为控制器内部单位后再与触发源进行比较。[RecTrigValMax](RecTrigValMax.md) 也适用同样的转换。对于无用户单位缩放的触发源，比较值直接进行比较。

> **注意：** 在 v4 中，比较值为 32 位整数。在 v5（Central-i）中，比较值为 64 位浮点数，因此可以直接指定非整数阈值。

## 示例

```text
ARecTrigVal[1]=1000  ; 第一示波器触发器 1 的比较值
ARecTrigVal[1]      ; 查询触发器 1（第一示波器）的比较值
```

## 另请参阅

- [RecTrigTyp](RecTrigTyp.md) — 触发激活类型
- [RecTrigValMax](RecTrigValMax.md) — 范围上界
- [RecTrigSrc](RecTrigSrc.md) — 触发源变量
- [RecTrigMask](RecTrigMask.md) — 对值进行位掩码运算
