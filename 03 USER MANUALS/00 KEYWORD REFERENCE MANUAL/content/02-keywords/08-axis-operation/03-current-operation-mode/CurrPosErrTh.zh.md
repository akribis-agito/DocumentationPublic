---
keyword: CurrPosErrTh
summary: 进入电流模式的位置误差阈值（条件 B）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 337
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -327680
  - 327680
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CurrPosErrTh

进入电流模式的位置误差阈值（条件 B）。

## 概述

`CurrPosErrTh` 是用于进入电流运行模式第二个条件检查（条件 B）的阈值位置误差（`PosErr`）值。它仅在轴处于位置运行模式（[OperationMode](../01-general-keywords/OperationMode.md) = 3）时使用。

## 工作原理

| 值    | 说明                                                       |
|-------|----------------------------------------------------------|
| \< 0  | 若 `PosErr` < `CurrPosErrTh`，则满足第二个条件。            |
| 0     | 第二个条件不满足。                                          |
| \> 0  | 若 `PosErr` > `CurrPosErrTh`，则满足第二个条件。            |

`CurrPosErrTh` 是三个可互换的条件 B 检查之一；另外两个是 [CurrAInTh](CurrAInTh.md)（模拟力反馈）和 [CurrCurrTh](CurrCurrTh.md)（电流参考）。固件每个周期都会评估所有已置位的条件 B 检查，只要其中**任意一个**满足即切换（条件 B 之间为逻辑或），前提是条件 A 的位置门已经通过。

进入电流运行模式仍要求第一个条件检查（[CurrPosTh](CurrPosTh.md) / [CurrPosThDir](CurrPosThDir.md)）在同一周期内通过。当两个条件都满足时，轴进入电流模式，固件将 `CurrPosErrTh` 清零为 0（并清除 [CurrPosThDir](CurrPosThDir.md)），以避免后续不期望的切换；用户必须重新配置其值以进行下一次切换。概述请参见[电流运行模式](00-overview.md)。

## 示例

```text
ACurrPosErrTh=5000   ; enter current mode when PosErr > 5000
ACurrPosErrTh=0      ; disable this condition
```

### 边界情况

- **模式相关性** —— 尽管条件 B 阈值引擎在速度模式（[OperationMode](../01-general-keywords/OperationMode.md) = 2）和位置模式（`OperationMode` = 3）运行模式下都会运行，但 `CurrPosErrTh` 只能在位置模式下触发。位置误差（`PosErr`）在速度模式下（以及通常在位置模式之外）保持为 `0`，因此 `PosErr > value` 和 `PosErr < value` 比较在那里都无法满足。
- **零值** —— 禁用此条件（仅条件 A 和其他条件 B 关键字起作用）。
- **触发后** —— `CurrPosErrTh` 和 [CurrPosThDir](CurrPosThDir.md) 都被清零为 `0`，以防止重复触发。通过再次写入两者来重新置位。
- **符号敏感性** —— 正阈值在 `PosErr > value` 时触发；负阈值在 `PosErr < value` 时触发。
- **电机失能** —— 阈值引擎不运行。
- **保存** —— 不可保存至闪存；启动时复位为 `0`。

## 另请参阅

- [电流运行模式](00-overview.md) —— 完整的模式切换条件
- [CurrAInTh](CurrAInTh.md) —— 可选的第二个条件（模拟力反馈）
- [CurrCurrTh](CurrCurrTh.md) —— 可选的第二个条件（电流参考）
