---
keyword: StuckTime
summary: 在轴被标记为堵转之前，堵转条件必须持续的时长。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 88
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 2147483647
  default: 4096
  scaling: 65.536
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# StuckTime

在轴被标记为堵转之前，堵转条件必须持续的时长。

## 概述

`StuckTime` 是电机堵转故障触发之前，堵转条件必须连续保持的时长。堵转条件为电流达到或高于 [StuckCurr](StuckCurr.md) **且**速度达到或低于 [StuckVel](StuckVel.md)。该关键字带有采样数到毫秒的缩放，因此你以毫秒为单位设置数值；在内部它会与一个采样计数器进行比较。当你写入该关键字时，数值（以 ms 为单位）会乘以 16.384 以得到内部采样计数；当你读回时，显示的数值等于内部采样计数除以 16.384——因此往返后仍以 ms 为单位。（在标准 16 kHz 控制速率下，1 个控制采样 ≈ 61.0 µs，故 250 ms ≈ 4096 个内部采样。）默认值 250 ms 对应 4096 个内部采样。

## 工作原理

固件维护一个内部采样计数器：

```text
increment the stuck counter
if the stuck counter has reached StuckTime
    turn the axis off and log the fault
```

- 只要经 AND 组合的 [StuckCurr](StuckCurr.md)/[StuckVel](StuckVel.md) 条件为真，计数器就在每个控制采样周期递增一。
- 任何采样一旦打破该条件，计数器立即重置为 `0`。因此故障要求 `StuckTime` 的单次不间断持续；间歇性堵转不会累积。
- 当计数器达到 `StuckTime` 时，轴被关闭，[ConFlt](../../../07-status-and-faults/ConFlt.md) 记录 ConFlt 码 1007（电机堵转）。

### 边界情况

- **电机失能：** 检测不运行；电机失能时计数器重置为 `0`。
- **模式依赖性：** 与 [StuckCurr](StuckCurr.md) 相同的绕过列表——仅在采用非步进电机的位置控制/速度控制下有效，且仅在外层门控之后（电机使能、真实——非仿真——电机、电流指令型驱动器而非脉冲方向驱动器）。
- **`StuckTime = 0`：** 计数器在条件为真的第一个采样周期即达到上限，因此保护立即跳闸（无消抖）。
- **范围溢出：** 写入超出 `0…2147483647` 的值会被钳位到关键字的 `range`。
- **清除故障：** ConFlt 码 1007 在重新使能（[MotorOn](../../../08-axis-operation/01-general-keywords/MotorOn.md) = 1）时或通过写入 `AConFlt=0` 清除；[ErrLog](../../../07-status-and-faults/ErrLog.md) 条目仍然保留。
- **HWProtectBits / ProtectMask：** 电机堵转跳闸无法通过 [ProtectMask](../../01-general-protection/ProtectMask.md) 屏蔽（该掩码仅覆盖硬件保护位）。

![Motor-stuck detection logic](stuck-logic.svg)

控制环以固定采样率运行，因此较大的 `StuckTime` 在跳闸前可容忍更长的瞬时堵转。将其设小可使保护快速响应，但会增加在合理的高负载、低速阶段误跳闸的几率。

## 示例

```text
AStuckTime[1]=250     ; require 250 ms of unbroken stuck condition (the default)
AStuckTime[1]         ; read back (returns the value in ms)
```

## 另请参阅

- [StuckCurr](StuckCurr.md) — 电流阈值；也列出了模式绕过情况
- [StuckVel](StuckVel.md) — 速度阈值
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — 记录故障码 1007（电机堵转）
