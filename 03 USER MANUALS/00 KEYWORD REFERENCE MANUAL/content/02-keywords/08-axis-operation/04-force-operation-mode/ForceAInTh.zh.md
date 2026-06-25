---
keyword: ForceAInTh
summary: 用于进入力模式的模拟量力反馈阈值（条件 B）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 584
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
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ForceAInTh

用于进入力模式的模拟量力反馈阈值（条件 B）。

## 概述

`ForceAInTh` 是在第二个条件检查（条件 B）中用于进入力运行模式的模拟量力反馈阈值。它仅在轴处于速度或位置运行模式（[OperationMode](../01-general-keywords/OperationMode.md) = 2 或 3）时使用。

## 工作原理

每个周期，在未处于力模式时，控制器会针对经过滤波的模拟量力反馈通道评估该阈值：

| 值 | 描述 |
|----|----|
| \< 0 | 若模拟量力反馈 < `ForceAInTh`，则满足第二个条件。 |
| 0 | 不满足第二个条件。 |
| \> 0 | 若模拟量力反馈 > `ForceAInTh`，则满足第二个条件。 |

**如果没有任何模拟量输入被分配力反馈功能，则该检查会被完全跳过** —— 请先用 [AInMode](../../../02-keywords/05-inputs-outputs/02-analog-inputs/AInMode.md) 分配它。

进入力运行模式仍需要第一个条件检查（[CurrPosTh](../03-current-operation-mode/CurrPosTh.md) / [CurrPosThDir](../03-current-operation-mode/CurrPosThDir.md)，针对位置参考进行评估）。当两个条件都满足时，轴会通过与 [GoToForceMode](GoToForceMode.md) 相同的平稳交接方式进入力模式，并且 `ForceAInTh` 被清零为 0，以避免将来发生非预期的切换；用户必须为下一次切换重新配置其值。`ForceAInTh` 和 [ForcePosErrTh](ForcePosErrTh.md) 作为并列的 B 条件 —— 任一触发即足够。概述请参见 [Force operation mode](00-overview.md)。

## 示例

```text
AForceAInTh=5000     ; enter force mode when force feedback > 5000
AForceAInTh=0        ; disable this condition
```

### 边界情况

- **错误模式**（[OperationMode](../01-general-keywords/OperationMode.md) ∉ {2, 3}）— 不评估。
- **零值** — 停用此条件。
- **未配置模拟量力反馈** — 当没有任何 [AInMode](../../05-inputs-outputs/02-analog-inputs/AInMode.md) 映射功能 3（力反馈）时，静默跳过。
- **触发后** — 进入力模式时 `ForceAInTh` 被清零为 `0` 以避免重复触发；通过再次写入来重新置位。
- **超出范围** — 超出 ±100000 的值会被拒绝。
- **电机失能** — 阈值引擎不运行。
- **保存** — 不可保存至闪存。

## 另请参阅

- [Force operation mode](00-overview.md) — 完整的模式切换条件
- [ForcePosErrTh](ForcePosErrTh.md) — 备选的第二个条件（位置误差）
- [Force](Force.md) — 被比较的力反馈
