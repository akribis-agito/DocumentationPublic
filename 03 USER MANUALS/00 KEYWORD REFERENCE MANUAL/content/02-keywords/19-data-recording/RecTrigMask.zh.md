---
keyword: RecTrigMask
summary: 应用于触发源和比较值的位掩码。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 251
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
  default: 4294967295
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
    default: 18446744073709551615
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# RecTrigMask

应用于触发源和比较值的位掩码。

## 概述

`RecTrigMask` 对触发比较操作中使用的值进行位掩码处理。触发源值（来自 [RecTrigSrc](RecTrigSrc.md)）以及触发比较值（[RecTrigVal](RecTrigVal.md) 和 [RecTrigValMax](RecTrigValMax.md)）在比较前均会被掩码处理。这使得触发可基于状态字中单个或多个选定位来激活。`RecTrigMask` 的每个索引对应不同示波器的不同触发。

## 工作原理

| 索引 | 示波器编号 | 触发 |
|---|---|---|
| 1 | 1（第一） | 1 |
| 2 | 1（第一） | 2 |
| 3 | 1（第一） | 3 |
| 4 | 2（第二） | 1 |
| 5 | 2（第二） | 2 |
| 6 | 2（第二） | 3 |

仅当触发源（[RecTrigSrc](RecTrigSrc.md)）为定点数据类型（32 位 int 或 64 位 long）时，掩码才适用；对于浮点触发源，掩码不会被应用。默认情况下，`RecTrigMask` 值为 -1（全部位置 1），即不屏蔽任何位，触发比较使用原始值。掩码操作通过按位与运算完成。

掩码为 0 将使所有掩码后的值归零，导致触发永远无法激活。为防止此情况，若任一有效触发（其 [RecTrigTyp](RecTrigTyp.md) 不为"none"）的 `RecTrigMask` 被设为 0，[RecStart](RecStart.md) 将拒绝请求并返回错误 35。

> **注意：** 在 v4 中，掩码为 32 位整数。在 v5（Central-i）中，掩码为 64 位整数，可对 64 位触发源的所有位进行掩码操作。

$$
\text{Masked value} = (\text{Original value})\ \&\ \left( \text{RecTrigMask}[x] \right)
$$

## 示例

假设需要在第一示波器的第二触发上，基于轴 A `MotionStat` 加速度位的上升沿激活触发，需进行以下设置：

1.  RecTrigTyp\[2\] = 5（上升沿）

2.  RecTrigSrc\[2\] = 32（以 AMotionStat 作为触发源变量）

3.  RecTrigMask\[2\] = 16（屏蔽第 4 位）

4.  RecTrigVal\[2\] = 0（在检测到超过此值的上升沿时触发）

## 另请参阅

- [RecTrigSrc](RecTrigSrc.md) — 触发源变量
- [RecTrigVal](RecTrigVal.md) — 比较值
- [RecTrigValMax](RecTrigValMax.md) — 范围上界
- [RecTrigTyp](RecTrigTyp.md) — 触发激活类型
