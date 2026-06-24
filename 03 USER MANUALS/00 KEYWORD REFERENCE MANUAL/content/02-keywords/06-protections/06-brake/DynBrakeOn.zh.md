---
keyword: DynBrakeOn
summary: 在电机失能时启用电气动态制动。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 405
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# DynBrakeOn

启用或禁用电气动态制动，使电机在失能时快速减速。

## 概述

动态制动是一种纯电气制动：它（通过下桥器件）将电机相短接并耗散反电动势电流，使刚刚失能的电机快速减速。与[静态制动器](Staticbrake.md)不同，它不需要外部硬件，用于在电机失能时泄放运动能量。

`DynBrakeOn` 是使能开关。默认值为 **0**（禁用），因此动态制动需要主动开启。

| 取值 | 含义 |
|-------|---------|
| 0 | 禁用动态制动 *(默认)* |
| 1 | 启用动态制动 |

## 工作原理

当 `DynBrakeOn ≠ 0` 时，只要满足以下条件，轴会在每个控制周期接合动态制动：

1. `DynBrakeOn ≠ 0`；且
2. 电机**失能**（[MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) = 0）。

在副控制器轴上（轴 B，以及三轴产品上的轴 C），当某个活动故障禁止动态制动时（某些 [ConFlt](../../07-status-and-faults/ConFlt.md) 状况，例如接地短路或功率级故障），还会额外抑制接合。在主轴（轴 A）和 Central-i 驱动器轴上，接合仅取决于上述两个条件——禁止性故障在此处**不会**阻止接合。

接合期间，轴会置位 [StatReg](../../07-status-and-faults/StatReg.md) 的 bit 28（动态制动激活），并调制短接占空比，使制动电流保持在 [PeakCL](../02-current-and-voltage/PeakCL.md)/[ContCL](../02-current-and-voltage/ContCL.md) 限值之内；[DynBrkRef](DynBrkRef.md) 设定最强制动上限。若电机被重新使能，动态制动脱开且 bit 28 清除。若母线电压过高，则过压保护强制制动占空比为 0，使制动器停止施加转矩，但 bit 28 保持置位（制动器仍“激活”，只是不驱动电流），直到电机被重新使能。在副轴上（轴 B，以及三轴产品上的轴 C），禁止性故障也会脱开制动并清除 bit 28；在主轴（轴 A）和 Central-i 轴上，禁止性故障不会清除 bit 28。

说明：

- 动态制动绝不会与活动的电流环对抗——它仅在电机失能时接合。
- 接合不取决于 [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md)；它取决于 `DynBrakeOn` 与电机失能状态，外加副轴上（轴 B，以及三轴产品上的轴 C）的逐故障许可。主轴（轴 A）和 Central-i 驱动器轴忽略逐故障许可，仅凭 `DynBrakeOn` 与电机失能即接合。
- 当 `DynBrakeOn = 0` 时，制动绝不接合，且 [StatReg](../../07-status-and-faults/StatReg.md) 的 bit 28 绝不置位。
- 在 PWM 驱动器上，动态制动在轴 A 和 B（以及三轴产品上的轴 C）上受支持。

`DynBrakeOn` 可在任何时候更改，包括电机使能时和运动中（在电机失能之前它根本不起作用）。

## 示例

```text
ADynBrakeOn=1           ; enable dynamic braking on the axis
ADynBrakeOn            ; read back the setting
ADynBrakeOn=0           ; disable (default)
```

要同时配置使能与制动强度：

```text
ADynBrakeOn=1
ADynBrkRef=1000         ; brake at full strength (100%) when engaged
```

## 参见

- [Dynamic brake](Dynamicbrake.md) — 动态制动机制概述
- [DynBrkRef](DynBrkRef.md) — 最大制动强度
- [Static brake](Staticbrake.md) — 独立的机械保持制动器
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 28 报告动态制动激活
- [PeakCL](../02-current-and-voltage/PeakCL.md) / [ContCL](../02-current-and-voltage/ContCL.md) — 限定制动的电流限值
