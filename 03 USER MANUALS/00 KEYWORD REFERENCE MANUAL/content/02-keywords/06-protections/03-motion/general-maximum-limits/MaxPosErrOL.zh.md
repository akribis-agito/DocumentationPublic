---
keyword: MaxPosErrOL
summary: 最大开环（注入）位置误差；超过该值将禁用轴。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 388
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
  - 1500000000
  default: 1000000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
last_updated: '2026-05-30'
doc_revision: '2026.06'
language: zh-CN
---
# MaxPosErrOL

最大开环（注入）位置误差；超过该值将禁用轴。

## 概述

`MaxPosErrOL` 是轴处于**开环**运行（开环模式或直接[注入](../../../13-injection/00-overview.md)期间）时所允许的最大绝对位置误差（[PosErr](../../../10-motion/01-kinematics-status/PosErr.md)）。它是 [MaxPosErr](MaxPosErr.md) 的开环对应项；开环位置误差天然大得多，因此存在一个独立的（且默认大得多的）限值。

## 工作原理

`MaxPosErrOL` 与 [MaxPosErr](MaxPosErr.md) 馈入控制环中**同一个**位置误差检查。在任一时刻哪一个生效由环路状态选择，该状态会切换当前激活的阈值并记录开环限值是否生效（固件使用一个内部标志位，bit 0 = 位置开环，bit 1 = 速度开环，bit 2 = 力开环）：

| 条件 | 激活阈值 | 开环限值 |
|-----------|------------------|--------------------|
| 开环模式开启（[OpenLoopOn](../../../08-axis-operation/01-general-keywords/OpenLoopOn.md) ≠ 0） | `MaxPosErrOL` | 是 |
| 在电流参考点、速度参考点或力参考点处的直接注入（[InjectType](../../../13-injection/InjectType.md) 为直接类型；[InjectPoint](../../../13-injection/InjectPoint.md) = `0`/`1`/`3`） | `MaxPosErrOL` | 是 |
| 在位置参考点处的直接注入（[InjectPoint](../../../13-injection/InjectPoint.md) = `2`） | [MaxPosErr](MaxPosErr.md) | 否 |
| 正常闭环 | [MaxPosErr](MaxPosErr.md) | 否 |

重要提示：即使是速度参考注入也将位置视为开环，因为闭合的位置环不再驱动 `VelRef`。因此，只要注入运行在电流参考点、速度参考点**或**力参考点处，位置限值便会切换到 `MaxPosErrOL`——只有位置参考注入（以及纯闭环）才使位置限值保持在 `MaxPosErr` 上。

当环路随后发现位置误差超过激活阈值时，开环标志决定记录哪种故障：开环 → [ConFlt](../../../07-status-and-faults/ConFlt.md) ConFlt 故障码 1055（开环位置误差过高）；闭环 → ConFlt 故障码 1020（位置误差过高）。无论哪种情况，轴都会立即关闭。在返回正常运行时（或注入期间电机失能时），激活阈值会恢复为 [MaxPosErr](MaxPosErr.md)，并清除开环标志。

### 边界情况

- **电机失能：** 位置环和限值检查均不运行；电机失能时误差被强制为 `0`。
- **模式依赖：** 对于开环步进电机，以及在任何非位置控制或非 force-over-PIV 的模式下，底层 `PosErr` 被强制为 `0`。在这些情况下，无论激活阈值如何，该检查都无法触发。
- **需要换相：** 与闭环检查一样（参见 [MaxPosErr](MaxPosErr.md)），位置误差跳闸仅在换相已建立（[StatReg](../../../07-status-and-faults/StatReg.md) bit 0 置位）后才运行，因此在尚未完成自动定相的无刷电机上不会触发。
- **范围溢出：** 超出关键字 `range` 的写入将以越界错误被拒绝；存储值保持不变。每当 `MaxPosErrOL`/`MaxPosErr`/`OpenLoopOn`/`InjectType`/`InjectPoint` 发生变化时，都会重新计算生效的内部限值。
- **清除故障：** ConFlt 故障码 1055 在重新使能（[MotorOn](../../../08-axis-operation/01-general-keywords/MotorOn.md) = 1）或写入 `AConFlt=0` 时清除；[ErrLog](../../../07-status-and-faults/ErrLog.md) 条目仍然保留。
- **HWProtectBits / ProtectMask：** 开环跟随误差跳闸无法通过 [ProtectMask](../../01-general-protection/ProtectMask.md) 屏蔽（该掩码仅涵盖硬件保护位）。

![跟随误差跳闸阈值：绝对误差持续上升直至越过激活限值；在该采样上轴被禁用并记录一个 ConFlt 故障码。开环限值更高，以容忍注入或开环运行期间天然更大的误差。](following-error-trip.svg)

## 示例

```text
AMaxPosErrOL[1]=1000000   ; max open-loop position error (user units)
AMaxPosErrOL[1]           ; read back the limit
```

## 另请参阅

- [MaxPosErr](MaxPosErr.md) — 闭环位置误差限值（备选阈值）
- [MaxVelErrOL](MaxVelErrOL.md) — 开环速度误差限值
- [PosErr](../../../10-motion/01-kinematics-status/PosErr.md) — 该限值所作用的测量误差
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — 记录故障码 1055（开环位置误差过高）
