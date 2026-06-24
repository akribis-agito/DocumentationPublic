---
keyword: CanMotorOn
summary: 在运行预检查后尝试使能电机的命令。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 129
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CanMotorOn

在运行预检查后尝试使能电机的命令。

## 概述

`CanMotorOn` 是一个命令函数，用于测试轴*是否能够*被使能，并在 [CanMotorOnRes](CanMotorOnRes.md) 中报告结果。它是轴相关命令，可在任意时刻发出。

重要提示：`CanMotorOn` **不会**使电机上电。它运行与 `MotorOn = 1` 相同的预条件检查，但并不进行使能，而是将 `1`（全部检查通过——使能将成功）或第一个失败检查的错误/故障码写入 [CanMotorOnRes](CanMotorOnRes.md)。要实际使能轴，仍需写入 [MotorOn](MotorOn.md) `= 1`。当你想知道使能*为何*会被拒绝而又不想触发错误响应时，可先使用 `CanMotorOn`。

## 工作原理

`CanMotorOn` 先将 `CanMotorOnRes = 1`，然后遍历一条单趟检查链，在第一个失败处中断并存储该原因码：

1. 与**使用 [MotorOn](MotorOn.md) 使能时所检查的相同预条件**，且顺序一致：FPGA / 变体 / 满量程健康状态、Central-i 端口已激活且设备为驱动器且继电器已闭合、整体电流限制、**换相完成**、浪涌已旁路、滤波器计算成功、以及滤波器未被修改。在 v5 上，最后这两项滤波器检查不再阻止使能（滤波器会实时重新计算），并且会首先运行一项 draw-mode 设置有效性检查；若 draw-mode 配置无效，则报告该项。
2. 然后是即使在静止状态下也会使轴故障的**中断级保护**：硬件保护条件（STO1/STO2、编码器错误、过流、IPM 故障、看门狗、5 V 故障、交流电源相位）、未知编码器类型、缺失电源、母线过压/欠压、逻辑过压/欠压、控制器板 / IPM / 电机过温，以及非法的取模与输入整形组合。

如果电机已使能，或 `MotorType` = simulation，或驱动器为 PD 类型，则结果保持为 `1`。

该检查是一次**快照**：与时间相关的保护（例如需要持续存在的 `MaxVBus` 过压）以及任何只能在使能后发生的情况（位置/速度误差、堵转、高电流）*均不*在覆盖范围内，因此即使 `CanMotorOn` 返回 `1`，`MotorOn = 1` 仍可能失败，或轴在使能后不久跳闸。

## 示例

```text
ACanMotorOn          ; run the pre-checks (does not enable the motor)
ACanMotorOnRes       ; 1 = enabling would succeed, otherwise the reject/fault code
AMotorOn=1           ; actually enable the axis
```

### 边界情况

- **电机已使能** —— 仍会运行预检查，但结果无论如何都被强制为 `1`（固件假定使能成功，因为不会有任何变化）。因此在电机使能时读取 `CanMotorOnRes = 1` 并不是一项有意义的预检查。
- **仿真电机** / **PD 驱动器** —— 固件将结果短路为 `1`；不查询快照预条件。
- **与时间相关的保护** —— `1` 的结果并非保证。某些保护（例如 `MaxVBus` 过压消抖、控制器板温度爬升、运动中误差）仅在使能后才会故障。务必在 `MotorOn = 1` 后读取 [ConFlt](../../07-status-and-faults/ConFlt.md) 以确认。
- **时机语义** —— `CanMotorOn` **不**了解未来的运动或负载；它无法预测堵转、位置误差或速度误差跳闸。
- **只读** —— 该关键字是一个函数（读取它即可触发）；写入会被拒绝。
- **按轴** —— 检查是按轴进行的；龙门对必须在其主轴上测试。
- **与 MotorOn 相同的检查链** —— 该检查链精确地镜像了 [MotorOn](MotorOn.md) `= 1` 的预检查链加上中断级保护；二者被有意保持同步。

## 另请参阅

- [CanMotorOnRes](CanMotorOnRes.md) —— 本命令写入的结果码
- [MotorOn](MotorOn.md) —— 实际使能/禁用电机的关键字
- [ConFlt](../../07-status-and-faults/ConFlt.md) —— `CanMotorOnRes` 可回传的故障码
- [StatReg](../../07-status-and-faults/StatReg.md) —— 检查读取的换相 / 滤波器状态位
