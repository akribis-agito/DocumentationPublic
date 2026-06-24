---
keyword: BrakeRelTime
summary: 松开静态制动器后、允许运动之前的延时（BrakeMode 3）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 382
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
# BrakeRelTime

设置静态制动器的**松闸**延时——轴在松开制动器后、允许运动之前的等待时间。

## 概述

保持制动器在得电后需要一定时间才能物理打开。`BrakeRelTime` 是轴在指令制动器松闸后、允许运动之前的等待时间。它保护运动的起始阶段：在制动器有足够时间打开之前，不允许规划器运行，从而使电机不必与尚未完全松开的制动器对抗。

`BrakeRelTime` **仅**在 [BrakeMode](BrakeMode.md) = 3（按电机使能状态自动）时有效。在其他模式下，该值被保存但不起作用。

该值为**毫秒**计的时间，可设置范围约为 **10 ms 至 800 ms**，默认值为 **100 ms**。（内部以控制采样为单位保存该时间；控制器会将你的毫秒值转换为采样数。）

## 工作原理

在 [BrakeMode](BrakeMode.md) = 3 时，标准电机使能时序会：

1. 使能电机；
2. 指令静态制动器松闸（得电）并为 `BrakeRelTime` 启动一个定时器；
3. 当该定时器到时，清除 [StatReg](../../07-status-and-faults/StatReg.md) 的 bit 29 抱闸请求，并允许运动。

bit 29 的清除在松闸定时器到时执行，而非在指令松闸的那一刻。在此之前，你在使能轴后立即排队的运动不会开始——它会等待松闸时间窗结束。

`BrakeRelTime` 保护**使能 → 运动**的转换；与之互补的 [BrakeLockTime](BrakeLockTime.md) 保护**停止 → 失能**的转换。在模式 3 下不要将 `BrakeRelTime` 设为 0——定时逻辑依赖于一个非零延时；请至少保持几毫秒（最小值约为 10 ms）。

## 示例

```text
ABrakeUsed=1
ABrakeMode=3            ; automatic by motor-on state
ABrakeRelTime=200       ; wait 200 ms after release before allowing motion
ABrakeRelTime          ; read back the configured release delay
```

若运动起始处出现卡顿或轴在运动开始时猛冲，请增大 `BrakeRelTime`，使制动器在规划器启动前完全打开。

## 参见

- [Static brake](Staticbrake.md) — 概述，含模式 3 的定时图
- [BrakeLockTime](BrakeLockTime.md) — 互补的抱闸（接合）延时
- [BrakeMode](BrakeMode.md) — 必须为 3 此延时才生效
- [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) — 施加该延时的使能时序
