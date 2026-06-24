---
keyword: MaxVelErr
summary: 最大闭环速度误差；超过该值将禁用轴。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 85
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 1300000000
  default: 32768
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# MaxVelErr

最大闭环速度误差；超过该值将禁用轴。

## 概述

`MaxVelErr` 是闭环运行中所允许的最大绝对速度误差（[VelErr](../../../10-motion/01-kinematics-status/VelErr.md)）。如果 `|VelErr|` 超过激活阈值，轴会在同一个控制周期内被禁用，并在 [ConFlt](../../../07-status-and-faults/ConFlt.md) 中记录一个故障。关于在注入/开环期间使用的开环等效项，参见 [MaxVelErrOL](MaxVelErrOL.md)。

## 工作原理

该检查在速度环中每个控制周期运行：

```text
if (mode is position-control, velocity-control, or force-over-PIV)
   and |VelErr| > active threshold
    turn the axis off and log the fault   (skipped for velocity-command amplifiers)
```

![跟随误差跳闸阈值：绝对误差持续上升直至越过激活限值；在该采样上轴被禁用并记录一个 ConFlt 故障码。开环限值更高，以容忍注入或开环运行期间天然更大的误差。](following-error-trip.svg)

要点：

- 实际使用的阈值会根据环路状态在 `MaxVelErr`（闭环）与 [MaxVelErrOL](MaxVelErrOL.md)（开环/注入）之间切换。在闭环中，违规会记录 [ConFlt](../../../07-status-and-faults/ConFlt.md) ConFlt 故障码 1021（速度误差过高）；在开环中，则记录 ConFlt 故障码 1056（开环速度误差过高）。关于哪种条件选择哪个阈值的完整表格，参见 [MaxVelErrOL](MaxVelErrOL.md)。
- 该保护**仅**在位置控制、速度控制或 force-over-PIV 运行中生效。在其他模式下，速度误差被强制为 `0`，因此该检查无法触发。
- 对于**速度指令（模拟）驱动器**会被**绕过**（[AmpType](../../../02-motor-and-amplifier/AmpType.md) = 模拟速度指令），因为外部驱动会闭合其自身的速度环。
- 一旦违规，轴会立即关闭。
- **需要换相。** 该检查与位置跟随误差跳闸位于同一个位置/速度环模块中，仅在换相已建立后才运行——[StatReg](../../../07-status-and-faults/StatReg.md) bit 0（换相完成）置位。在尚未完成自动定相的无刷电机上，环路未闭合，因此速度跟随误差跳闸无法触发。请注意，这与 [MaxVel](MaxVel.md) 超速跳闸不同，后者不需要换相（对于电流指令驱动器上的实际电机，只要电机使能它就会运行，与换相状态无关）。

### 边界情况

- **电机失能：** 速度环和限值检查均不运行；电机失能时 `VelErr` 被重置为 `0`。
- **模式依赖：** 在位置控制、速度控制和 force-over-PIV 运行之外，`VelErr` 被强制为 `0`，因此该跳闸在这些模式下无法触发——包括仅电流控制和仅力控制。
- **速度指令驱动器绕过：** 当 [AmpType](../../../02-motor-and-amplifier/AmpType.md) 为模拟速度指令（外部速度环）驱动器时，该跳闸被完全跳过——驱动不会检查其自身从动件的速度误差。
- **步进开环：** 对于 [MotorType](../../../02-motor-and-amplifier/MotorType.md) = 步进开环，`VelErr` 被强制为 `0`。
- **开环/注入：** 在 [OpenLoopOn](../../../08-axis-operation/01-general-keywords/OpenLoopOn.md) ≠ 0 期间，或在电流参考点或力参考点处的直接注入期间，激活限值变为 [MaxVelErrOL](MaxVelErrOL.md)，故障变为 ConFlt 故障码 1056。在速度参考点或位置参考点处的注入则使限值保持在 `MaxVelErr` 上。
- **范围溢出：** 超出 `0…1300000000`（v4）的写入将以越界错误被拒绝，存储值保持不变；生效的内部限值会在 `MaxVelErr`/`OpenLoopOn`/`InjectType`/`InjectPoint` 下一次发生变化时更新。
- **清除故障：** ConFlt 故障码 1021 在重新使能（[MotorOn](../../../08-axis-operation/01-general-keywords/MotorOn.md) = 1）或写入 `AConFlt=0` 时清除；[ErrLog](../../../07-status-and-faults/ErrLog.md) 条目仍然保留。
- **HWProtectBits / ProtectMask：** 跟随误差跳闸无法通过 [ProtectMask](../../01-general-protection/ProtectMask.md) 屏蔽（该掩码仅涵盖硬件保护位）。

## 示例

```text
AMaxVelErr[1]=100000   ; max velocity error (user units/s)
AMaxVelErr[1]          ; read back the limit
```

## 另请参阅

- [VelErr](../../../10-motion/01-kinematics-status/VelErr.md) — 该限值所作用的测量速度误差
- [MaxVelErrOL](MaxVelErrOL.md) — 开环速度误差限值（备选阈值）
- [MaxPosErr](MaxPosErr.md) — 配套的位置跟随误差限值（参见其详解；相同的跳闸模式）
- [VelRef](../../../10-motion/01-kinematics-status/VelRef.md) / [Vel](../../../10-motion/01-kinematics-status/Vel.md) — `VelErr` 的操作数
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — 记录故障码 1021（闭环）/ 1056（开环）
- [MotionReason](../../../10-motion/05-motion-status/MotionReason.md) — 在该跳闸触发时记录原因 8（电机已禁用）
