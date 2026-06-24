---
keyword: StuckCurr
summary: 电机堵转检测的电流阈值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 86
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
  default: 4000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# StuckCurr

电机堵转检测的电流阈值。

## 概述

`StuckCurr` 是电机堵转检测的电机电流阈值。当驱动器推得很用力（电流达到或高于 `StuckCurr`）但电机几乎不动（速度达到或低于 [StuckVel](StuckVel.md)），并且该组合持续 [StuckTime](StuckTime.md) 时，电机即处于"堵转"。默认值为电机的 4 A 电流水平。最大值被钳位至驱动器的最大电流指令。

## 工作原理

每个控制采样周期，固件都会评估堵转条件：

```text
if |Vel[3]| <= StuckVel  and  |MotorCurr| >= StuckCurr  and mode is eligible
    increment the stuck counter
    if the stuck counter has reached StuckTime
        turn the axis off and log the fault
else
    reset the stuck counter to 0
```

![Motor-stuck detection logic](stuck-logic.svg)

- 这两个条件通过 **AND** 组合：滤波后速度的绝对值 `Vel[3]` 必须 `<= StuckVel`，**且**电机电流的绝对值必须 `>= StuckCurr`。
- 在两者同时成立期间，内部计数器每个采样周期递增一次；任何打破该条件的采样都会将其重置为 `0`。因此故障仅在连续 *持续* [StuckTime](StuckTime.md) 个采样周期时才会触发。
- 跳闸时，轴被关闭，[ConFlt](../../../07-status-and-faults/ConFlt.md) 记录 ConFlt 码 1007（电机堵转）。
- 对于步进电机，以及仅电流控制（[OperationMode](../../../08-axis-operation/01-general-keywords/OperationMode.md) = current-only）、力控制、正在进行的换相/自动定相和电机学习模式——这些预期会出现低速大电流的情形——检测被**绕过**。
- 整个堵转检查（连同双堵转检查和超速检查）位于一个外层驱动器/电机门控之后：仅当电机使能（[MotorOn](../../../08-axis-operation/01-general-keywords/MotorOn.md) = 1）、电机为真实电机（而非[仿真](../../../02-motor-and-amplifier/MotorType.md)电机）且驱动器为电流指令型驱动器时才运行——在脉冲方向（步进/方向）驱动器（[AmpType](../../../02-motor-and-amplifier/AmpType.md)）上**不**运行。在 central-i v5 上，该门控还额外排除带反馈的脉冲方向驱动器。在该门控之外，内部计数器保持重置。

### 边界情况

- **电机失能：** 检测不运行；电机失能时内部计数器重置为 `0`，因此下一次电机使能将从干净状态开始。
- **模式依赖性：** 绕过列表（仅电流、力控制、自动定相、电机学习、任何步进电机）意味着堵转保护仅在采用非步进电机的位置控制模式和速度控制模式下有效。
- **基于 PIV 的力控制：** 力控制绕过是针对 [OperationMode](../../../08-axis-operation/01-general-keywords/OperationMode.md)（力控制模式）检查的；在位置控制模式下运行的基于 PIV 的力控制配置仍然激活堵转检测。
- **范围溢出：** 写入 `StuckCurr` 超出 `0…64000` 的值会被钳位到关键字的 `range`；在 Central-i 上，最大值还会额外被钳位至远程驱动器的最大电流指令。
- **清除故障：** ConFlt 码 1007 在重新使能（[MotorOn](../../../08-axis-operation/01-general-keywords/MotorOn.md) = 1）时或通过写入 `AConFlt=0` 清除；[ErrLog](../../../07-status-and-faults/ErrLog.md) 条目仍然保留。
- **HWProtectBits / ProtectMask：** 电机堵转跳闸无法通过 [ProtectMask](../../01-general-protection/ProtectMask.md) 屏蔽（该掩码仅覆盖硬件保护位）。

> **示例演练：** 设 `StuckCurr = 4000`（4 A）、`StuckVel = 40000`（user units/s）且 `StuckTime` 为几千个采样周期，假设电机在以 6 A 点动时撞上机械硬限位。电流升至 4 A 以上，滤波后速度跌至 40 000 以下；两个 AND 条件均成立。内部采样计数器递增，当达到 `StuckTime` 时，轴被禁用并置 `ConFlt = 1007`。如果障碍在计数器达到 `StuckTime` 之前解除（使速度升至 `StuckVel` 以上），则计数器重置，不会引发故障。

## 示例

```text
AStuckCurr[1]=4000    ; current above which a non-moving motor counts as stuck
AStuckCurr[1]         ; read back the threshold
```

## 参见

- [StuckVel](StuckVel.md) — 速度阈值（AND 条件的另一半）
- [StuckTime](StuckTime.md) — 该条件必须持续多长时间
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — 记录故障码 1007（电机堵转）
