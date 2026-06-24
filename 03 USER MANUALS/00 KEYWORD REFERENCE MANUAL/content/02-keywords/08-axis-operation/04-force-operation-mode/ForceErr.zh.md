---
keyword: ForceErr
summary: 力参考与力反馈之间的差值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 583
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
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
    data_type: float32
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# ForceErr

力参考与力反馈之间的差值。

## 概述

`ForceErr` 是（已滤波的）力参考 [ForceRef](ForceRef.md) 与力反馈 [Force](Force.md) 之间的差值。它是力控制环要驱动趋近于零的误差信号。

## 工作原理

`ForceErr` 在每个控制周期重新计算，为已滤波参考减去反馈：

$$
\text{ForceErr}\ [\text{unit}] = \text{ForceRef}\ [\text{unit}] - \text{Force}\ [\text{unit}]
$$

除闭合控制环外，`ForceErr` 还承担两项作用：

- **到位检测。** 力到位检查将 `|ForceErr|` 与 [ForceInTTol](ForceInTTol.md) 比较；一旦力在该窗口内持续 [ForceInTTime](ForceInTTime.md)，轴即稳定到位（[ForceInTStat](ForceInTStat.md) = 4）。
- **高误差保护。** 若 `|ForceErr|` 超过内部最大力误差限值，则关闭电机，且在闭环运行时 [ConFlt](../../07-status-and-faults/ConFlt.md) 显示故障码 1045（力误差超出限值），在开环运行时显示故障码 1057（开环下力误差超出限值）。

当轴不处于力模式时，`ForceErr` 被强制为 `0`。

## 示例

```text
AForceErr           ; read the current force error
```

### 边界情况

- **模式错误**（[OperationMode](../01-general-keywords/OperationMode.md) ≠ 4）——强制为 `0`；无论 `ForceRef − Force` 会计算出何值，读取它都返回 `0`。
- **电机失能**——保持为 `0`（控制环未运行）。
- **高误差跳闸**——超过内部最大力误差限值会禁用电机并触发 `ConFlt = 1045`（闭环）或 `ConFlt = 1057`（开环）；此保护仅在力模式下运行。
- **只读**——写入被拒绝。

## 另请参阅

- [ForceRef](ForceRef.md) —— 已滤波力参考（被减数）
- [Force](Force.md) —— 力反馈（减数）
- [ForceInTTol](ForceInTTol.md) —— 应用于该误差的稳定到位窗口
- [ForceInTStat](ForceInTStat.md) —— 由该误差驱动的到位状态
