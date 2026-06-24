---
keyword: CurrAInTh
summary: 进入电流模式的模拟力反馈阈值（条件 B）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 338
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
  - -100000
  - 100000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CurrAInTh

进入电流模式的模拟力反馈阈值（条件 B）。

## 概述

`CurrAInTh` 是用于进入电流运行模式的第二个条件检查（条件 B）的模拟力反馈阈值。它仅在轴处于速度或位置运行模式（[OperationMode](../01-general-keywords/OperationMode.md) = 2 或 3）时使用。模拟力反馈通过 [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md) 配置，并从 `AInPort` 读取。

## 工作原理

| 值 | 说明 |
|----|----|
| \< 0 | 若模拟力反馈 < `CurrAInTh`，则满足第二个条件。 |
| 0 | 不满足第二个条件。 |
| \> 0 | 若模拟力反馈 > `CurrAInTh`，则满足第二个条件。 |

仅当**确实有一路模拟量输入被配置为力反馈**时才会评估此检查：控制器首先验证是否有一路模拟量输入被分配了力反馈功能（通过 [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md)），并读取该输入的滤波值。如果没有任何输入被分配该功能，则 `CurrAInTh` 无论取何值都不起作用。

`CurrAInTh` 是三个可互换的条件 B 检查之一（另外两个为 [CurrPosErrTh](CurrPosErrTh.md) 和 [CurrCurrTh](CurrCurrTh.md)）；只要其中任一项满足其比较条件（且条件 A 已通过），即可触发切换。

进入电流运行模式仍需要第一个条件检查（[CurrPosTh](CurrPosTh.md) / [CurrPosThDir](CurrPosThDir.md)）。当第一个和第二个条件均满足时，轴进入电流运行模式，固件将 `CurrAInTh` 清零为 0（并清除 [CurrPosThDir](CurrPosThDir.md)）以避免今后发生不期望的切换；用户必须为下一次切换重新配置其值。完整切换逻辑参见[电流运行模式](00-overview.md)。

## 示例

```text
ACurrAInTh=5000      ; enter current mode when force feedback > 5000
ACurrAInTh=0         ; disable this condition
```

### 边界情况

- **模式错误**（[OperationMode](../01-general-keywords/OperationMode.md) ∉ {2, 3}）—— 不评估。
- **零值** —— 禁用此条件。
- **未配置模拟力反馈** —— 如果没有任何 [AInMode](../../05-inputs-outputs/02-analog-inputs/AInMode.md) 被设置为功能 3（力反馈），则该条件被**静默跳过**；永远不会触发。
- **触发后** —— `CurrAInTh` 和 [CurrPosThDir](CurrPosThDir.md) 均被清零为 `0`，以防止重复触发。
- **符号敏感性** —— 正阈值在 `value > threshold` 时触发；负阈值在 `value < threshold` 时触发。
- **电机失能** —— 阈值引擎不运行。
- **保存** —— 可保存至闪存。

## 另请参阅

- [Current operation mode](00-overview.md) —— 完整的模式切换条件
- [CurrPosTh](CurrPosTh.md) —— 第一个条件（位置参考阈值）
- [CurrPosErrTh](CurrPosErrTh.md) —— 备选的第二个条件（位置误差）
- [CurrCurrTh](CurrCurrTh.md) —— 备选的第二个条件（电流参考）
