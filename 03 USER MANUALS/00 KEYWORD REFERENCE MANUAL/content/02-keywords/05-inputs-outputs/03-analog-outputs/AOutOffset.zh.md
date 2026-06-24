---
keyword: AOutOffset
summary: 加到模拟量输出上的偏置（mV），用于校准/置零。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 227
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -500
  - 500
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
    data_type: float32
    range:
    - -700
    - 700
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# AOutOffset

加到模拟量输出上的偏置（mV），用于校准/置零。

## 概述

`AOutOffset` 向模拟量输出加上一个固定偏置，单位为毫伏——在[模拟量输出信号路径](00-overview.md)中于缩放之后、毫伏到 DAC 码转换之前应用。数组索引即模拟量输出编号（从 1 开始：`AOutOffset[1]` 为模拟量输出 1）。用它来校准或置零某个通道的输出。

## 工作原理

`AOutOffset` 在两种输出模式下均会应用，于值被转换为 DAC 码并钳位之前：

- **直接模式：** `DAC code = (AOutPort + AOutOffset) × (mV-to-DAC factor)`。
- **监视模式：** `DAC code = ((parameter << AOutShifts) + AOutOffset) × (mV-to-DAC factor)`。

由于偏置以与（缩放后的）值相同的毫伏单位加上，之后才由 mV 到 DAC 的因子（−2.752457 LSB/mV）缩放，因此 `AOutOffset` 每一个单位使输出移动 1 mV。该窄范围（v4 上为 ±500 mV）足以用于校准/置零，而不适用于大信号偏置。

## 示例

```text
AAOutOffset[1]=-12   ; trim analog output 1 by -12 mV to zero it
AAOutOffset[1]        ; read back the offset
```

### 边界情况

- **索引 0** — 无效；有效索引为 `AOutOffset[1]`–`AOutOffset[4]`。`AOutOffset[0]` 不存在。
- **超出范围** — 超出 ±500 mV（v4）或 ±700 mV（v5）的值会被参数表拒绝。
- **模式独立性** — 在直接（`AOutMode = 0`）和监视（`AOutMode ≠ 0`）两种模式下均应用。
- **饱和** — 加偏置后的 DAC 码被钳位至 ±11905 mV 的输出范围；较大的偏置可能将本来在范围内的值削顶。
- **电机使能/失能** — 无论 `MotorOn` 状态如何，每个周期均运行。
- **保存** — 可保存至闪存；启动时重新加载。
- **平台** — v4 以 `int32` 存储，范围 ±500 mV；v5 以 `float32` 存储，范围 ±700 mV。

## 版本间差异

在 Central-i v5 上，`AOutOffset` 为 `float32`，范围扩大至 ±700 mV（v4 / standalone：`int32`，±500 mV）。其作用与信号路径中的位置保持不变。

## 另请参阅

- [AOutPort](AOutPort.md) — 指令值（直接模式）；偏置加到其上
- [AOutShifts](AOutShifts.md) — 在偏置之前应用的缩放（监视模式）
- [analog-output overview](00-overview.md) — 完整信号路径
