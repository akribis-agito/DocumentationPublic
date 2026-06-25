---
keyword: ForcePosErrTh
summary: 进入力模式的位置误差阈值（条件 B）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 576
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
# ForcePosErrTh

进入力模式的位置误差阈值（条件 B）。

## 概述

`ForcePosErrTh` 是进入力运行模式的第二个条件检查（条件 B）中所使用的阈值位置误差（`PosErr`）值。每当轴既不处于电流运行模式也不处于力运行模式时，即评估该条件——也就是处于位置运行模式（[OperationMode](../01-general-keywords/OperationMode.md) = 3）**或**速度运行模式（[OperationMode](../01-general-keywords/OperationMode.md) = 2）时。

## 工作原理

当轴既不处于电流模式也不处于力模式时，控制器每个周期将位置误差与该阈值进行比较：

| 值    | 说明                                                      |
|-------|-----------------------------------------------------------|
| \< 0  | 若 `PosErr` < `ForcePosErrTh` 则满足第二个条件。 |
| 0     | 第二个条件不满足。                        |
| \> 0  | 若 `PosErr` > `ForcePosErrTh` 则满足第二个条件。 |

进入力运行模式仍需要第一个条件检查（[CurrPosTh](../03-current-operation-mode/CurrPosTh.md) / [CurrPosThDir](../03-current-operation-mode/CurrPosThDir.md)，针对位置参考进行评估）。当两个条件均满足时，轴通过与 [GoToForceMode](GoToForceMode.md) 相同的平滑交接进入力模式，且 `ForcePosErrTh` 被清零为 0 以避免日后非预期的切换；用户必须为下一次切换重新配置其值。`ForcePosErrTh` 与 [ForceAInTh](ForceAInTh.md) 作为并行的 B 条件——任一触发即足够。概述请参见[力运行模式](00-overview.md)。

## 示例

```text
AForcePosErrTh=5000  ; enter force mode when PosErr > 5000
AForcePosErrTh=0     ; disable this condition
```

### 边界情况

- **电流模式或力模式** — 当轴已处于电流运行模式（[OperationMode](../01-general-keywords/OperationMode.md) = 1）或力运行模式（[OperationMode](../01-general-keywords/OperationMode.md) = 4）时不评估。在位置模式（= 3）和速度模式（= 2）下均评估。
- **零值** — 禁用该条件。
- **触发后** — 进入力模式时清零为 `0` 以避免重复触发。
- **超出范围** — 超出 ±327680 的值将被拒绝。
- **电机失能** — 阈值引擎不运行。
- **保存** — 不可保存至闪存。

## 另请参阅

- [力运行模式](00-overview.md) — 完整的模式切换条件
- [ForceAInTh](ForceAInTh.md) — 替代的第二个条件（模拟力反馈）
