---
keyword: CurrCurrTh
summary: 进入电流模式的电流参考阈值（条件 B）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 339
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -64000
  - 64000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CurrCurrTh

进入电流模式的电流参考阈值（条件 B）。

## 概述

`CurrCurrTh` 是在第二个条件检查（条件 B）中与电流*参考*值 `CurrRef`（即指令电流，而非测量电流）比较的阈值，用于进入电流运行模式。仅当轴处于速度或位置运行模式（[OperationMode](../01-general-keywords/OperationMode.md) = 2 或 3）时使用。若该值为 0，则该检查被解除武装，轴不会因此切换；否则比较方向由 [CurrCurrThDir](CurrCurrThDir.md) 设定。

## 工作原理

| CurrCurrThDir | 说明                                                    |
|---------------|---------------------------------------------------------|
| 0             | 若 `CurrRef` > `CurrCurrTh`，则满足第二个条件。 |
| 1             | 若 `CurrRef` < `CurrCurrTh`，则满足第二个条件。 |

`CurrCurrTh` 是三个可互换的条件 B 检查之一（另两个为 [CurrPosErrTh](CurrPosErrTh.md) 和 [CurrAInTh](CurrAInTh.md)）；只要任一已武装的检查得到满足，且条件 A 已经通过，固件即进行切换。

进入电流运行模式仍需通过第一个条件检查（[CurrPosTh](CurrPosTh.md) / [CurrPosThDir](CurrPosThDir.md)）。当两个条件均满足时，轴进入电流模式，固件将 `CurrCurrTh` 清为 0（并清除 [CurrPosThDir](CurrPosThDir.md)），以避免日后发生不期望的切换；用户必须为下一次切换重新配置其值。概述请参见 [Current operation mode](00-overview.md)。

## 示例

```text
ACurrCurrThDir=0     ; trigger when CurrRef rises above threshold
ACurrCurrTh=2000     ; enter current mode when CurrRef > 2000 mA
```

### 边界情况

- **模式错误**（[OperationMode](../01-general-keywords/OperationMode.md) ∉ {2, 3}）—— 不评估。
- **值为零** —— 禁用此条件。
- **触发后** —— `CurrCurrTh` 和 [CurrPosThDir](CurrPosThDir.md) 都被清为 `0`；用户必须为下一次切换重新武装两者。
- **方向** —— 比较意义由 [CurrCurrThDir](CurrCurrThDir.md) 设定；`0` 默认为上升沿穿越。
- **电机失能** —— 阈值引擎不运行。
- **保存** —— 不可保存至闪存；该值在重新上电时丢失，必须重新武装。

## 另请参阅

- [CurrCurrThDir](CurrCurrThDir.md) — 选择比较方向
- [Current operation mode](00-overview.md) — 完整的模式切换条件
- [CurrPosTh](CurrPosTh.md) — 第一个条件（位置参考阈值）
