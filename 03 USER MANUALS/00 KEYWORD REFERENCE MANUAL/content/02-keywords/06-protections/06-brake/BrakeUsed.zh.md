---
keyword: BrakeUsed
summary: 启用或禁用对外部静态（保持）制动器的控制。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 379
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 1
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# BrakeUsed

声明是否存在外部静态（保持）制动器并应由轴驱动。

## 概述

`BrakeUsed` 是静态制动器功能的总开关。静态制动器是一种外部的、故障安全型机电装置（失电 = 抱闸/保持，得电 = 松闸），用于在轴关闭时保持负载。当此类制动器接线到轴上时，设置 `BrakeUsed = 1`；当未安装制动器时，设置 `BrakeUsed = 0`。

当 `BrakeUsed = 0` 时，轴绝不会向（不存在的）装置施加松闸电压，因此所有静态制动器处理——包括 [BrakeMode](BrakeMode.md) 策略与 [BrakeRelTime](BrakeRelTime.md)/[BrakeLockTime](BrakeLockTime.md) 定时——都不会产生电气作用。

此关键字仅适用于静态制动器。电气[动态制动](Dynamicbrake.md)由 [DynBrakeOn](DynBrakeOn.md) 单独控制。

| 取值 | 含义 |
|-------|---------|
| 0 | 无静态制动器（轴不施加松闸电压） |
| 1 | 存在静态制动器并由轴控制 *(默认)* |

## 工作原理

每个控制周期，轴运行由 [BrakeMode](BrakeMode.md) 选择的静态制动器状态机。其所有分支仅在 `BrakeUsed ≠ 0` 时起作用；当 `BrakeUsed = 0` 时，在手动模式下制动器输出保持不变（见下文）。

- **在手动模式下禁用已存在的制动器（`1 → 0`）**（[BrakeMode](BrakeMode.md) 0/1/2）：轴只是停止驱动制动器输出，并使其保持最后一次的指令状态。随后制动器硬件保持其当前状态，直到断电。
- **在按电机自动模式下禁用已存在的制动器（`1 → 0`）**（[BrakeMode](BrakeMode.md) 3）：轴无法等待下一次电机使能/失能时序，因此立即抱闸并在 [StatReg](../../07-status-and-faults/StatReg.md) 的 bit 29 置位抱闸请求。
- 当 `BrakeUsed = 1` 时，抱闸请求会反映在 [StatReg](../../07-status-and-faults/StatReg.md) 的 bit 29，且在制动器抱闸期间发出的运动指令会被拒绝（轴报告 “can't start motion while the static brake is locked” 错误）。

`BrakeUsed` 不可在电机使能时更改；请先禁用轴。

## 示例

```text
ABrakeUsed=1            ; declare a static brake on the axis
ABrakeUsed             ; read back the setting
ABrakeUsed=0            ; no static brake fitted
```

典型的垂直轴设置，启用制动器并选择自动定时：

```text
ABrakeUsed=1
ABrakeMode=3            ; automatic by motor-on state
```

## 参见

- [Static brake](Staticbrake.md) — 保持制动器控制与定时概述
- [BrakeMode](BrakeMode.md) — 制动器如何抱闸/松闸
- [BrakeRelTime](BrakeRelTime.md) / [BrakeLockTime](BrakeLockTime.md) — 松闸与抱闸延时（模式 3）
- [DynBrakeOn](DynBrakeOn.md) — 独立的电气动态制动
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 29 报告静态制动器抱闸请求
