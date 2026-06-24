---
keyword: ForceRef
summary: 力控制环中使用的已滤波力参考。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 581
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
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ForceRef

力控制环中使用的已滤波力参考。

## 概述

`ForceRef` 是力控制环中使用的**已滤波**力参考。它跟随由 [ForceCmdSrc](ForceCmdSrc.md) 定义的源（模拟量输入或 [ForceCmdVal](ForceCmdVal.md) 表）。力环驱动反馈 [Force](Force.md) 趋向该参考，两者之差报告为 [ForceErr](ForceErr.md)。

## 工作原理

力指令生成器首先每个周期从所选源构建一个*原始*力参考——模拟量输入，或 [ForceCmdVal](ForceCmdVal.md) 表值（在应用 [ForceCmdSlope](ForceCmdSlope.md) 斜坡之后）。该原始参考随后通过一阶参考滤波器以产生 `ForceRef`，即环路和 [ForceErr](ForceErr.md) 所使用的值。

这种滤波正是力模式下的到位 / 时序定时以**未滤波**（滤波前）参考为基准的原因：保持定时器以及运动/稳定测量在原始参考到达目标 [ForceCmdVal](ForceCmdVal.md) 的那一刻开始，而非在已滤波的 `ForceRef` 追上时开始。当力模式未激活时，`ForceRef` 保持等于 [Force](Force.md) 反馈，从而使进入力模式的切换无冲击。

有关该滤波器的更多信息，请参见[控制整定 – 力控制](../../11-control-tuning/07-force-control/00-overview.md)。

## 示例

```text
AForceRef           ; read the filtered force reference
```

### 边界情况

- **错误模式**（[OperationMode](../01-general-keywords/OperationMode.md) ≠ 4）— `ForceRef` 保持等于 [Force](Force.md)，以使下一次进入力模式无冲击。
- **电机失能** — `ForceRef` 跟踪 `Force`；环路未运行。
- **时序定时与滤波器** — 到位 / 时序定时以**未滤波**参考为基准；不要为序列步骤决策直接将 `ForceRef` 与 [ForceCmdVal](ForceCmdVal.md) 比较。
- **只读** — 写入将被拒绝。

## 参见

- [ForceCmdSrc](ForceCmdSrc.md) — 选择参考源
- [ForceCmdSlope](ForceCmdSlope.md) — 原始参考趋向每个表值的斜坡速率
- [Force](Force.md) — 环路跟踪的力反馈
- [ForceErr](ForceErr.md) — ForceRef 减 Force
