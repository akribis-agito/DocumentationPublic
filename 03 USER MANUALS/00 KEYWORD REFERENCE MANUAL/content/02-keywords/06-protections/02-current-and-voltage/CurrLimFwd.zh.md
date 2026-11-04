---
keyword: CurrLimFwd
summary: 正向电流指令限值（当 CurrLimMode = 3 时使用）。
availability:
- controller
- ci-master
can_code: 393
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 16000
  default: 16000
  scaling: 1.0
  implemented: final
overrides:
  ci-master:
    range:
    - 0
    - 64000
    default: 64000
  agc300-et:
    range:
    - 0
    - 4000
    default: 4000
  agc301-et:
    range:
    - 0
    - 4000
    default: 4000
  agc301-et-bioxtreme:
    range:
    - 0
    - 4000
    default: 4000
  agd200-et-2d01:
    range:
    - 0
    - 4000
    default: 4000
  agd200-et-2d02:
    range:
    - 0
    - 8000
    default: 8000
  agd301-et-2d01:
    range:
    - 0
    - 4000
    default: 4000
  agd301-et-2d02:
    range:
    - 0
    - 8000
    default: 8000
  agd301-et-2d09:
    range:
    - 0
    - 25500
    default: 25500
  agd155-af-2a06:
    range:
    - 0
    - 25500
    default: 25500
  agd155-af-2a10:
    range:
    - 0
    - 28500
    default: 28500
  agd155-ec:
    range:
    - 0
    - 25500
    default: 25500
  agd155-ec-var34:
    range:
    - 0
    - 28500
    default: 28500
  agd155-ec-var34-3:
    range:
    - 0
    - 42500
    default: 42500
  agd156-ec:
    range:
    - 0
    - 12726
    default: 12726
  agd101-ec-34a:
    range:
    - 0
    - 28280
    default: 28280
  agd101-ec-17a:
    range:
    - 0
    - 14140
    default: 14140
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

## 版本间变更

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
