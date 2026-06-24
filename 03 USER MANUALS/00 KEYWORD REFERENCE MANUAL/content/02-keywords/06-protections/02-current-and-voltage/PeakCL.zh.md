---
keyword: PeakCL
summary: 峰值电流限值，同时用于电流指令饱和与 I²t 保护。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 52
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
  - 20
  - 64000
  default: 64000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# PeakCL

峰值电流限值，同时用于电流指令饱和与 I²t 保护。

## 概述

`PeakCL` 是峰值电流限值（单位 mA）。它承担两种作用：

1. **电流指令饱和。** 当电流限制模式 [CurrLimMode](CurrLimMode.md) 为 `0` 时，`PeakCL` 对电流指令（`CurrRef`）进行对称限幅，使指令的绝对值永远不超过 `PeakCL`。（在 `CurrLimMode` 的其他取值下，先施加方向性限值，然后仍将此 `PeakCL` 边界作为最终的绝对钳位施加。）
2. **I²t 上限。** 它与 [ContCL](ContCL.md) 和 [PeakTime](PeakTime.md) 一起构成 I²t 方案中的峰值。

## 工作原理

每个控制周期，驱动器形成有效的绝对电流指令限值，并将其作为电流指令饱和边界施加。通常该限值等于 `PeakCL`；当 [I²t](ContCL.md) 限制启用时，它会降至有效连续值。当指令被钳位时，[StatReg](../../07-status-and-faults/StatReg.md) 位 21（电流饱和）被置位。

`PeakCL` 还为 `StatReg` 中报告的多级电流告警提供基准：驱动器预先计算 0.88·`PeakCL`、0.92·`PeakCL` 和 0.96·`PeakCL` 作为低 / 中 / 高告警阈值。

`PeakCL` 必须大于 [ContCL](ContCL.md)；如果 `ContCL` ≥ `PeakCL`，固件使用 `PeakCL / 2` 作为有效连续限值（参见 [ContCL](ContCL.md)）。

### 边界情况

- **电机失能：** 饱和不会主动钳位（未生成 `CurrRef`），但预先计算的限值和告警阈值在下次电机使能时仍然有效。
- **模式依赖：** 只要电流环处于活动状态（或向外部电流模式驱动器驱出 `CurrRef`），绝对钳位即生效。
- **饱和指示：** 钳位会将 [StatReg](../../07-status-and-faults/StatReg.md) 位 21（电流饱和）置位。
- **与 I²t 的交互：** 当 [ContCL](ContCL.md) 的 I²t 限制启用时，有效绝对钳位会从 `PeakCL` 降至连续电流值。
- **告警阈值：** 预先计算的 `0.88·PeakCL`、`0.92·PeakCL`、`0.96·PeakCL` 分段边界为 [StatReg](../../07-status-and-faults/StatReg.md) 电流告警字段（位 9–10）提供输入。
- **范围溢出：** 超出 `20…64000`（v4）的写入会被钳位到关键字 `range`。
- **HWProtectBits / ProtectMask：** 电流饱和不是跳闸，也不可被掩码屏蔽。

## 版本间差异

在 **v4** 中 `PeakCL` 是 32 位整数；在 **v5**（仅 central-i）中它是 32 位浮点数（`float32`）。饱和和 I²t 作用保持不变。

## 示例

```text
APeakCL=64000        ; peak current limit (mA)
```

## 另请参阅

- [ContCL](ContCL.md) — 连续电流限值（必须低于 `PeakCL`）；I²t 详解见该页
- [PeakTime](PeakTime.md) — 允许处于峰值电流的时间
- [CurrLimMode](CurrLimMode.md) — 选择电流指令的限制方式
- [MaxMotorCurr](MaxMotorCurr.md) — 瞬时过流跳闸（与基于 `PeakCL` 的限制不同）
- [StatReg](../../07-status-and-faults/StatReg.md) — 位 21 标志电流指令饱和；位 25 标志 I²t 功率限制处于活动状态
