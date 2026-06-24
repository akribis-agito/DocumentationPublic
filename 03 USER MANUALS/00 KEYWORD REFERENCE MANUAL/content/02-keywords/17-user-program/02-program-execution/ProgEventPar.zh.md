---
keyword: ProgEventPar
summary: 通过复合 CAN 代码选择触发事件的控制器参数。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 520
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
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# ProgEventPar

通过复合 CAN 代码选择触发事件的控制器参数。

## 概述

`ProgEventPar` 使用复合 CAN 代码定义被监控的控制器参数，以触发指定事件（索引 `[1]`–`[5]`，每个事件对应一个索引）。若 `ProgEventPar[EventNumber]` 设置为 `0`，或设置为无法解析为有效可读参数的复合代码，则该事件不会被感测，也不会被处理。它与 [ProgEventType](ProgEventType.md)、[ProgEventVal](ProgEventVal.md) 和 [ProgEventMask](ProgEventMask.md) 共同构成事件的四部分触发定义，其结构与数据记录触发器非常相似。该参数为非轴数组参数，保存至闪存（默认值为 `0`）。

## 工作原理

每个元素持有一个[复合 CAN 代码](../../../01-keyword-usage-and-syntax/complex-can-code.md)，用于指定被监控的确切参数，而非仅是裸 CAN 代码。复合值包含三个字段：

| 位 | 字段 |
|---|---|
| 0–9 | 参数的 CAN 代码 |
| 10–14 | 轴编号（0 = A；对非轴参数忽略） |
| 16–31 | 数组索引（用于数组参数；标量使用 0） |

对于轴 A 上的标量参数，复合代码即为普通 CAN 代码。写入 `ProgEventPar` 时，控制器将验证所选内容：CAN 代码必须存在，必须是参数（而非指令），且轴和数组索引必须在有效范围内。验证失败时，该事件的触发器将指向一个始终为零的内部源，使其永远无法触发（在更正选择之前，该事件实际上处于禁用状态）。

选择有效后，控制器将解析触发源，同时将触发阈值 [ProgEventVal](ProgEventVal.md) 转换为源参数的内部（原始）单位——应用该参数的用户单位缩放或缩放因子——使触发时的比较快速且单位正确。因此，请以与被监控参数相同的用户单位设置 [ProgEventVal](ProgEventVal.md)。

## 示例

```text
AProgEventPar[1]=<complex CAN code of monitored parameter>   ; choose the trigger source for event 1
AProgEventPar[1]=0   ; disable the trigger source for event 1
```

## 另请参阅

- [ProgEventType](ProgEventType.md) — 触发类型（边沿、等于、不等于……）
- [ProgEventVal](ProgEventVal.md) — 用于触发检测的值
- [ProgEventMask](ProgEventMask.md) — 应用于触发的位掩码
