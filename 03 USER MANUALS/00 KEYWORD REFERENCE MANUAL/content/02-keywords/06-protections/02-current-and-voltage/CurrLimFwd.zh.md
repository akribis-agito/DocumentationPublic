---
keyword: CurrLimFwd
summary: 正向电流指令限值（当 CurrLimMode = 3 时使用）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 393
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
  - 0
  - 64000
  default: 64000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
last_updated: '2026-05-27'
doc_revision: '2026.06'
language: zh-CN
---
# CurrLimFwd

正向电流指令限值（当 CurrLimMode = 3 时使用）。

## 概述

`CurrLimFwd` 定义**正向**电流指令限值（单位为 mA），用于替代默认的 [PeakCL](PeakCL.md) 钳位。它仅在 [CurrLimMode](CurrLimMode.md) 为 `3` 时适用。请将其设为正值。

## 工作原理

当 `CurrLimMode = 3` 时，固件在每个控制周期将电流指令钳位至非对称范围 `[−CurrLimRev, +CurrLimFwd]`（`CurrLimFwd` 限定正向侧）。随后仍会施加绝对的 [PeakCL](PeakCL.md) 钳位，因此任一方向限值都不能超过 `PeakCL`。当指令被钳位时，会设置 [StatReg](../../07-status-and-faults/StatReg.md) 位 21（电流饱和）。

方向限值可通过配置为转矩限制禁用功能的数字量输入临时取消，此时指令将退回至仅 `PeakCL` 钳位。

## 版本间变化

在 **v4** 中 `CurrLimFwd` 是 32 位整数；在 **v5**（仅 central-i）中它是 32 位浮点数（`float32`）。钳位机制保持不变。

## 示例

```text
ACurrLimMode=3
ACurrLimFwd=40000    ; positive current limit (mA)
```

## 另请参阅

- [CurrLimRev](CurrLimRev.md) —— 负向电流指令限值
- [CurrLimMode](CurrLimMode.md) —— 必须为 3 才能使其生效
- [PeakCL](PeakCL.md) —— 仍会在其之上施加绝对钳位
- [StatReg](../../07-status-and-faults/StatReg.md) —— 位 21 标志电流饱和
