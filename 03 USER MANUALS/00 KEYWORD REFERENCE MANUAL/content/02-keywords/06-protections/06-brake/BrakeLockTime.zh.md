---
keyword: BrakeLockTime
summary: 接入静态制动器后、电机被禁用前的延时（BrakeMode 3）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 381
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: scaling
  range:
  - 655
  - 13107
  default: 1638
  scaling: 65.536
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# BrakeLockTime

设置静态制动器的**抱闸**延时——即轴在接入制动器后、禁用电机之前，使电机保持励磁的持续时间。

## 概述

保持制动器在断电后需要一定时间才能实际机械接入。`BrakeLockTime` 是轴在命令制动器抱闸后、实际禁用电机之前，使电机保持励磁（仍能够保持位置/力矩）的时间。它保护禁用切换过程：负载由电机保持，直到制动器有足够时间夹紧，从而不会在“命令制动”与“制动接入”之间的间隙中下坠。

`BrakeLockTime` **仅**在 [BrakeMode](BrakeMode.md) = 3（按电机使能状态自动）时有效。在其他模式下，该值会被存储但不起作用。

该值为以**毫秒**为单位的时间，可设置范围约为 **10 ms 至 800 ms**，默认值为 **100 ms**。（内部以控制周期采样数保存该时间；控制器会将您的毫秒值转换为采样数。）

## 工作原理

在 [BrakeMode](BrakeMode.md) = 3 时，当电机被禁用（且轴当前处于使能状态）时，序列为：

1. 命令静态制动器抱闸（断电），并启动一个 `BrakeLockTime` 计时器，同时电机保持励磁；
2. 在计时器到时之前保持电机励磁——在此窗口内电机继续保持负载；
3. 当计时器到时，置位 [StatReg](../../07-status-and-faults/StatReg.md) 第 29 位的抱闸请求，并禁用电机。

第 29 位的置位与电机禁用在抱闸计时器到时时一起发生，而不是在命令抱闸的那一刻。

`BrakeLockTime` 保护**停止 → 禁用**切换过程；与之互补的 [BrakeRelTime](BrakeRelTime.md) 保护**使能 → 运动**切换过程。在模式 3 下，请勿将 `BrakeLockTime` 设为 0——定时逻辑依赖一个非零延时；请至少保持几毫秒（最小值约为 10 ms）。

## 示例

```text
ABrakeUsed=1
ABrakeMode=3            ; automatic by motor-on state
ABrakeLockTime=350      ; hold the motor 350 ms after engaging the brake, then disable
ABrakeLockTime         ; read back the configured lock delay
```

如果在轴被禁用时负载下坠或下沉，请增大 `BrakeLockTime`，使制动器在移除电机力矩之前完全接入。

## 另请参阅

- [Static brake](Staticbrake.md) — 概述，包含模式 3 的定时时序图
- [BrakeRelTime](BrakeRelTime.md) — 与之互补的松开延时
- [BrakeMode](BrakeMode.md) — 必须为 3 才能使该延时生效
- [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) — 应用该延时的禁用序列
