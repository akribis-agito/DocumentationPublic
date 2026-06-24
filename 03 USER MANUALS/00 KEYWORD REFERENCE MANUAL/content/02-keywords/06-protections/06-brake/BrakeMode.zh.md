---
keyword: BrakeMode
summary: 选择静态（保持）制动器抱闸与松闸的方式。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 380
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 4
  default: 2
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# BrakeMode

选择外部静态（保持）制动器的抱闸策略。

## 概述

`BrakeMode` 选择如何控制静态制动器——一种故障安全型机电装置（失电 = 抱闸/保持，得电 = 松闸）。可选范围从固定的手动状态、考虑电机状态的保护方式，到与电机使能时序或某个数字量输入挂钩的全自动定时方式。

`BrakeMode` 仅在 [BrakeUsed](BrakeUsed.md) = 1 时生效。默认值为 **2**（手动松闸，无保护）。所选模式产生的抱闸请求会反映在 [StatReg](../../07-status-and-faults/StatReg.md) 的 bit 29。

## 工作原理

静态制动器状态机每个控制周期运行一次，并执行由 `BrakeMode` 选择的分支：

| 取值 | 模式 | 行为 |
|-------|------|-----------|
| 0 | 手动抱闸 | 始终抱闸（接合），无论电机状态如何。 |
| 1 | 手动松闸，带保护 | 仅在电机使能时松闸；若电机失能，则制动器重新抱闸。 |
| 2 | 手动松闸，无保护 *(默认)* | 始终松闸（释放），无论电机状态如何。 |
| 3 | 按电机使能状态自动 | 电机使能时松闸，失能时抱闸；松闸与抱闸由电机使能时序定时，使用 [BrakeRelTime](BrakeRelTime.md) 与 [BrakeLockTime](BrakeLockTime.md)。 |
| 4 | 按数字量输入自动，带保护 | 由配置为静态制动器抱闸功能的数字量输入驱动：输入有效请求抱闸（但运动中保持松闸）；输入无效请求松闸（但电机失能时保持抱闸）。 |

特定模式的说明：

- **模式 0/1/2（手动）：** 若在手动模式下将 [BrakeUsed](BrakeUsed.md) 从 1 改为 0，制动器保持其最后一次的指令状态（轴停止驱动该输出）。
- **模式 3（按电机使能自动）：** 松闸/抱闸及其延时作为电机使能/失能时序的一部分被执行——参见 [BrakeRelTime](BrakeRelTime.md) 与 [BrakeLockTime](BrakeLockTime.md)。若电机通过标准电机使能指令以外的路径被使能，制动器仍会松闸，但不会施加松闸延时。在此模式下电机失能期间，制动器保持抱闸（保护）。
- **模式 4（数字量输入）：** 在数字量输入功能处理中执行。它始终保持运动与电机失能状态安全——无论输入电平如何，轴在运动中不会抱闸，电机失能时不会松闸。
- **超出范围的取值：** 若 `BrakeMode` 以某种方式超出 0–4，轴会回退到安全默认值并保持制动器**抱闸**。

`BrakeMode` 可在电机使能时更改，但不可在轴运动中更改。

## 示例

```text
ABrakeMode=3            ; automatic, timed by the motor-on sequence
ABrakeMode             ; read back the current mode
ABrakeMode=0            ; force the brake locked
ABrakeMode=2            ; force the brake released (default)
```

## 参见

- [Static brake](Staticbrake.md) — 保持制动器控制与定时概述
- [BrakeUsed](BrakeUsed.md) — 启用静态制动器功能
- [BrakeRelTime](BrakeRelTime.md) / [BrakeLockTime](BrakeLockTime.md) — 模式 3 使用的松闸与抱闸延时
- [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) — 驱动模式 3 的松闸/抱闸定时
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 29 报告静态制动器抱闸请求
