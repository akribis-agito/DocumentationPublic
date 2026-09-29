---
keyword: ForceInTTol
summary: 用于到位状态判定的目标力周围的稳定窗口。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 734
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 2147483647
  default: 10
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ForceInTTol

用于到位状态判定的目标力周围的稳定窗口。

## 概述

`ForceInTTol` 是目标值（[ForceCmdVal](ForceCmdVal.md)）周围的稳定窗口（单位：用户单位），用于判定力控制的到位状态。在力模式下当 [ForceCmdSrc](ForceCmdSrc.md) = 1 或 2 时适用；在电流模式（[OperationMode](../01-general-keywords/OperationMode.md) = 1）下当 [CurrCmdSrc](../03-current-operation-mode/CurrCmdSrc.md) = 1 或 2 时也适用，此时它以 mA 与 `CurrRef − MotorCurr` 比较；与所有 USER_UNITS 关键字一样，读写的值按 [UsrUnits](../../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) 缩放。它与驻留时间 [ForceInTTime](ForceInTTime.md) 共同决定 [ForceInTStat](ForceInTStat.md) 何时报告到位。

## 工作原理

该窗口是**对称的**：每个周期（当 [ForceInTStat](ForceInTStat.md) = 3 时）控制器将力误差与 ±`ForceInTTol` 进行比较，即 `ForceErr <= ForceInTTol && ForceErr >= -ForceInTTol`。由于目标力由（已滤波的）[ForceRef](ForceRef.md) 保持，`ForceErr` 是 [Force](Force.md) 反馈相对于指令值的偏差，因此该窗口实际上为 `|measured force − target force| <= ForceInTTol`。在窗口内时，[ForceInTTime](ForceInTTime.md) 驻留计数器累计；离开窗口则将其复位。

## 示例

```text
AForceInTTol=10      ; settled when force error stays within ±10 units
```

### 边界情况

- **错误模式 / 错误源**——仅当 [OperationMode](../01-general-keywords/OperationMode.md) = 4 且 [ForceCmdSrc](ForceCmdSrc.md) ∈ {1, 2}，或 OperationMode = 1 且 [CurrCmdSrc](../03-current-operation-mode/CurrCmdSrc.md) ∈ {1, 2} 时使用；其他情况下忽略。两种模式共用同一个值，因此在力模式与电流模式之间切换时，需要按所用模式设置 ForceInTTol。
- **零值**——实际上要求误差为零；几乎从不锁存到位。
- **超出范围**——负值将被拒绝；最大值为 `2 147 483 647`。
- **已达到状态 4**——增大 `ForceInTTol` 不会重新置位到位；状态机仅在达到状态 4 之前评估该窗口。
- **保存**——可保存至闪存。

## 另请参阅

- [ForceInTTime](ForceInTTime.md) —— 在该窗口内所需的驻留时间
- [ForceInTStat](ForceInTStat.md) —— 使用该窗口的到位状态
- [ForceErr](ForceErr.md) —— 与该窗口比较的误差
