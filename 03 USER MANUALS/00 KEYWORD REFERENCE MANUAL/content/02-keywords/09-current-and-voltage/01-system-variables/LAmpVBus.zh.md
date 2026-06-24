---
keyword: LAmpVBus
summary: 内置线性驱动器（AmpType = 4）母线电压测量值的只读量。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 253
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 3
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
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# LAmpVBus

内置线性驱动器（AmpType = 4）母线电压测量值的只读量。

## 概述

`LAmpVBus` 以只读数组形式报告内置线性驱动器的两条母线电压轨，单位为毫伏。它仅在 [AmpType](../../02-motor-and-amplifier/AmpType.md) = 4（内置线性驱动器）时适用。标准开关（PWM）驱动器的母线电压请参见 [VBus](VBus.md)。

## 工作原理

线性驱动器采用分裂（双极性）电源供电，因此具有正、负两条电机轨。当 `AmpType` = 4 时，两条轨都在电流读取步骤中采样，每个原始读数都换算为毫伏：

| Index | Rail | Description                              |
|-------|------|------------------------------------------|
| 1     | +Vm  | Positive linear-amplifier bus voltage    |
| 2     | −Vm  | Negative linear-amplifier bus voltage (reported as a negative value) |

该数组的大小为两条轨加上一个未使用的索引 0（使通信索引从 1 开始）。负轨单独读取并取反，因此正常的 −Vm 读数为负的毫伏值。

> **注意：** 在内置线性驱动器（`AmpType` = 4）上，母线电压保护限值（[MinVBus](../../06-protections/02-current-and-voltage/MinVBus.md) / [MaxVBus](../../06-protections/02-current-and-voltage/MaxVBus.md)）仍然运行，且 [VBus](VBus.md) 仍会被采样。仅当 central-i 系统上使用线性适配器（`AmpType` = 7）时，标准 VBus 路径才会被旁路，此时母线电压读数及其保护均不可用。

## 示例

```text
ALAmpVBus[1]        ; read the +Vm linear-amplifier bus voltage (mV)
ALAmpVBus[2]        ; read the -Vm linear-amplifier bus voltage (mV, negative)
```

## 另请参阅

- [VBus](VBus.md) — 开关驱动器直流母线电压读数
- [AmpType](../../02-motor-and-amplifier/AmpType.md) — 驱动器类型选择（= 4 选择线性驱动器）
