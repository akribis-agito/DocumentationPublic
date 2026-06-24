---
keyword: CurrFBFact
summary: 比例因子（微单位），将远程模拟电流检测输入映射为电机电流，用于直线适配器远程驱动器。
availability:
  standalone: []
  central-i:
  - v4
can_code: 649
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: -1907500
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CurrFBFact

比例因子（微单位），将远程模拟电流检测输入映射为电机电流，用于直线适配器远程驱动器。

## 概述

`CurrFBFact` 设置当 Central-i 主站驱动通过模拟电流检测输入报告电机电流的远程**直线适配器**驱动器时所使用的电流反馈比例。它将来自该远程设备的原始模拟电流反馈读数转换为控制环所使用的电机电流，并包含符号以保证反馈极性正确。

它是保存至闪存的轴相关参数。该值以固定的 10⁻⁶（六位小数）比例进行解释，因此存储的整数是所施加因子的百万分之一；例如默认值 `-1907500` 施加约为 `-1.9075` 的因子。负号反映了所支持硬件的反馈极性。

> 这是外部电流反馈比例的 v4 形式。在 v5 上等效设置为浮点形式的 [ExtCurrFBSca](ExtCurrFBSca.md)。

## 工作原理

当 Central-i 主站识别到连接的直线适配器远程驱动器（[AmpType](../../02-motor-and-amplifier/AmpType.md) 设置为直线适配器类型）时，它会将 `CurrFBFact × 10⁻⁶` 加载为该设备的电流检测因子。此后该远程设备的原始模拟电流读数将乘以此因子，以产生电流环使用并由 [MotorCurr](../02-motor-variables/MotorCurr.md) 报告的电机电流反馈。

该设置在远程设备被识别/连接时生效，因此请在连接远程设备前更改它（或重新连接以使新值生效）。它仅用于直线适配器远程驱动器；其他远程驱动器类型通过各自的路径报告电流并忽略此设置。

## 示例

```text
ACurrFBFact=-1907500     ; default scaling for the supported linear-adapter remote
ACurrFBFact              ; read the configured current-feedback factor
```

## 参见

- [ExtCurrFBSca](ExtCurrFBSca.md) — 此比例的 v5 浮点等效形式
- [AmpType](../../02-motor-and-amplifier/AmpType.md) — 驱动器类型；本设置适用于直线适配器远程设备
- [MotorCurr](../02-motor-variables/MotorCurr.md) — 由缩放后的反馈产生的电机电流
