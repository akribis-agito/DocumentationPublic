---
keyword: MaxPosErr
summary: 最大闭环位置误差；超过它将禁用轴。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 84
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
  - 80000000
  default: 20
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-30'
doc_revision: '2026.06'
language: zh-CN
---
# MaxPosErr

最大闭环位置误差；超过它将禁用轴。

## 概述

`MaxPosErr` 是闭环运行中允许的最大绝对位置误差（[PosErr](../../../10-motion/01-kinematics-status/PosErr.md)）。它是主要的“跟随误差”保护：如果 `|PosErr|` 超过当前生效阈值，轴会在同一控制采样内被禁用，并在 [ConFlt](../../../07-status-and-faults/ConFlt.md) 中记录故障。关于注入/开环期间使用的开环等效限值，参见 [MaxPosErrOL](MaxPosErrOL.md)。

## 工作原理

该检测在位置环中每个控制采样运行：

```text
if |PosErr| > active threshold
    turn the axis off and log the fault
```

![跟随误差跳闸阈值：绝对误差上升直至越过生效限值；在该采样上轴被禁用并记录一个 ConFlt 码。开环限值更高，以容忍注入或开环运行期间更大的自然误差。](following-error-trip.svg)

要点：

- 实际使用的阈值会根据环路状态在 `MaxPosErr`（闭环）和 [MaxPosErrOL](MaxPosErrOL.md)（开环 / 注入）之间切换。在正常闭环运行中应用闭环阈值，因此违例会记录 [ConFlt](../../../07-status-and-faults/ConFlt.md) ConFlt 码 1020（位置误差过大）。在开环中应用开环阈值，相同条件改为记录 ConFlt 码 1055（开环位置误差过大）。关于哪种条件选择哪个阈值的完整表格，参见 [MaxPosErrOL](MaxPosErrOL.md)。
- 对于开环步进电机，以及只要轴不处于位置控制 / force-over-PIV 模式，位置误差被强制为 `0`（因此此保护从不跳闸）。因此该保护仅在位置环实际闭合时才有效。
- 发生违例时轴会立即关闭，并应用该故障所配置的停止行为。
- **需要换相。** 承载此检测的位置环代码块仅在换相建立后才运行——[StatReg](../../../07-status-and-faults/StatReg.md) 位 0（换相完成）已置位。在尚未完成自动定相的无刷电机上，位置环未闭合，因此跟随误差跳闸无法触发。注意这与 [MaxVel](MaxVel.md) 超速跳闸不同，后者不要求换相（对于电流指令驱动器上的真实电机，它在电机使能后即运行，与换相状态无关）。

### 边界情况

- **电机失能：** 位置环与限值检测不运行；电机失能时误差被复位。
- **模式相关性：** `PosErr` 在位置控制和 force-over-PIV 运行之外，以及对于开环步进电机（[MotorType](../../../02-motor-and-amplifier/MotorType.md) = 开环步进），被强制为 `0`，因此在这些配置下检测无法跳闸。
- **开环 / 注入：** 在 [OpenLoopOn](../../../08-axis-operation/01-general-keywords/OpenLoopOn.md) ≠ 0 期间，或在电流、速度或力参考点的任何直接注入期间，生效限值变为 [MaxPosErrOL](MaxPosErrOL.md)，故障变为 ConFlt 码 1055。仅当在位置参考点直接注入时，限值才保持为 `MaxPosErr`。
- **范围溢出：** 超出 `0…80000000`（v4）的写入会以超范围错误被拒绝；存储值保持不变。生效的内部限值在下一次对 `MaxPosErr`/`MaxPosErrOL`/`OpenLoopOn`/`InjectType`/`InjectPoint` 的更改时更新。
- **清除故障：** ConFlt 码 1020 在重新使能（[MotorOn](../../../08-axis-operation/01-general-keywords/MotorOn.md) = 1）或写入 `AConFlt=0` 时清除；[ErrLog](../../../07-status-and-faults/ErrLog.md) 条目仍保留。
- **HWProtectBits / ProtectMask：** 跟随误差跳闸不可通过 [ProtectMask](../../01-general-protection/ProtectMask.md) 屏蔽（该掩码仅覆盖硬件保护位）。

## 示例

```text
AMaxPosErr[1]=5000    ; max following error (user units)
AMaxPosErr[1]         ; read back the limit
```

### 操作演练：整定并验证跟随误差跳闸

将限值设置为接近应用应当出现的最大跟踪误差，然后在部署前执行最坏情况移动并确认跳闸行为：

```text
AMaxPosErr[1]=2000    ; chosen well above the expected steady-state |PosErr|
APosErr               ; sample the live error in normal operation; should stay << MaxPosErr
```

运行最坏情况曲线（最高 `Speed`/`Accel`、最重负载），并在移动过程中的多个点重新采样 `APosErr`。如果裕量太小，可以提高位置增益（使滞后减小）或提高 `MaxPosErr`。要确认跳闸路径本身，可命令一次向机械障碍物的移动：

```text
AConFlt                       ; expect 1020 (closed-loop position error too high)
AMotionReason                 ; expect 8 (motor disabled)
APosErr                       ; last value before the trip; will be > MaxPosErr
```

轴会在越过阈值的同一控制采样内被禁用，因此没有斜坡；如果需要的是软停止，则应留出裕量并依靠软件 [FwdPLim](../position-limit-protection/FwdPLim.md)/[RevPLim](../position-limit-protection/RevPLim.md) 先行制动。

## 参见

- [PosErr](../../../10-motion/01-kinematics-status/PosErr.md) — 此限值所作用的被测位置误差
- [MaxPosErrOL](MaxPosErrOL.md) — 开环位置误差限值（备用阈值）
- [MaxVelErr](MaxVelErr.md) — 配套的速度跟随误差限值
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — 记录故障码 1020（闭环）/ 1055（开环）
- [MotionReason](../../../10-motion/05-motion-status/MotionReason.md) — 此跳闸触发时记录原因 8（电机失能）
