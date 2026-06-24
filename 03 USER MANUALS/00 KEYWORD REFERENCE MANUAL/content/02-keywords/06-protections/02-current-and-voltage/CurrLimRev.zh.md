---
keyword: CurrLimRev
summary: 负向电流指令限值（在 CurrLimMode = 3 时使用）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 394
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
# CurrLimRev

负向电流指令限值（在 CurrLimMode = 3 时使用）。

## 概述

`CurrLimRev` 定义**负向**电流指令限值（单位 mA），用于替代默认的 [PeakCL](PeakCL.md) 钳位。仅当 [CurrLimMode](CurrLimMode.md) 为 `3` 时生效。请以正数给出——它限定的是负侧，因此指令被限制为 −`CurrLimRev`。

## 工作原理

当 `CurrLimMode = 3` 时，固件在每个控制周期将电流指令钳位到非对称范围 `[−CurrLimRev, +CurrLimFwd]`。此后仍会施加绝对 [PeakCL](PeakCL.md) 钳位，因此负向限值的幅值不能超过 `PeakCL`。当指令被钳位时，会置位 [StatReg](../../07-status-and-faults/StatReg.md) 第 21 位（电流饱和）。

方向性限值可由配置为转矩限制禁用功能的数字量输入临时取消，此时指令将退回到仅使用 `PeakCL` 钳位。

## 版本间变更

在 **v4** 中 `CurrLimRev` 为 32 位整数；在 **v5**（仅 central-i）中为 32 位浮点数（`float32`）。钳位机制保持不变。

## 示例

```text
ACurrLimMode=3
ACurrLimRev=40000    ; magnitude of the negative current limit (mA)
```

## 参见

- [CurrLimFwd](CurrLimFwd.md) — 正向电流指令限值
- [CurrLimMode](CurrLimMode.md) — 必须为 3 本限值才生效
- [PeakCL](PeakCL.md) — 仍在其上施加的绝对钳位
- [StatReg](../../07-status-and-faults/StatReg.md) — 第 21 位标记电流饱和
