---
keyword: ProgEventVal
summary: 用于事件触发检测的值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 523
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 6
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
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# ProgEventVal

用于事件触发检测的值。

## 概述

`ProgEventVal` 定义用于事件触发检测的阈值（索引 `[1]`–`[5]`，每个事件对应一个索引）。它与被监控参数进行比较——两者均经 [ProgEventMask](ProgEventMask.md) 掩码处理后——根据 [ProgEventType](ProgEventType.md) 选择的条件进行判断。它是定义事件触发器的四个参数之一，与源参数 [ProgEventPar](ProgEventPar.md) 和位掩码 [ProgEventMask](ProgEventMask.md) 共同构成触发定义。该参数为非轴数组参数，保存至闪存（默认值为 `0`）。

## 工作原理

以与 [ProgEventPar](ProgEventPar.md) 所选被监控参数**相同的用户单位**输入 `ProgEventVal`。每当该值或触发源被（重新）赋值时，控制器将该阈值一次性转换为源参数的内部（原始）单位，应用该参数的用户单位缩放或缩放因子，从而使每个周期的比较快速执行。[ProgEventMask](ProgEventMask.md) 的掩码每个周期应用于被监控源读数，而非此阈值，因此阈值以全位宽与经掩码处理的源进行比较。对于边沿条件（[ProgEventType](ProgEventType.md) `5`/`6`），阈值为源必须穿越的电平；对于"已更改"条件（`8`），阈值不使用，因为比较对象是事件置位时捕获的值。

## 示例

```text
AProgEventVal[1]=100 ; threshold of 100 (in the monitored parameter's user units) for event 1
```

## 版本间变更

在 v4（独立版和 central-i v4）中，`ProgEventVal` 为 32 位有符号整数；[ProgEventMask](ProgEventMask.md) 亦同。在 central-i v5 中，两者均扩展为 64 位有符号整数，使更宽的触发源能够以全位宽进行比较。

## 另请参阅

- [ProgEventType](ProgEventType.md) — 触发类型（边沿、等于、不等于……）
- [ProgEventPar](ProgEventPar.md) — 触发事件的参数
- [ProgEventMask](ProgEventMask.md) — 应用于触发的位掩码
