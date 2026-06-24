---
keyword: Begin
summary: 根据当前运动模式和目标设置在该轴上启动运动。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 131
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# Begin

根据当前运动模式和目标设置在该轴上启动运动。

## 概述

`Begin` 使用当前选定的 [MotionMode](../02-motion-configuration/MotionMode.md)、已配置的目标（[AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) / [RelTrgt](../13-motion-mode-ptp/RelTrgt.md)）以及运动学参数（[Speed](../03-kinematics-configuration/Speed.md)、[Accel](../03-kinematics-configuration/Accel.md)、[Decel](../03-kinematics-configuration/Decel.md)、[Jerk](../03-kinematics-configuration/Jerk.md)）在该轴上启动运动。它是一个轴相关的命令函数，不携带任何值。

处理程序依次完成三件事：首先运行一连串**前置条件**检查，若该轴未就绪则拒绝该命令；然后运行**特定于模式的校验与初始化**；最后通过设置 [MotionStat](../05-motion-status/MotionStat.md) 中的位来**武装该次运动**。运动通过 [Stop](Stop.md)（受控）或 [Abort](Abort.md)（立即）结束。运动也可以通过 [BeginDInOn](BeginDInOn.md) 推迟到某个数字量输入边沿后再启动。

当该轴已处于运动中时，`Begin` 会被拒绝（该关键字带有 `ok_in_motion: false` 属性，由解释器强制执行）。无限模式——摇杆位置模式以及带 [PTPKeepMoving](../02-motion-configuration/PTPKeepMoving.md) `= 1` 的 PTP——则会保持该次运动持续有效，并跟踪新的位置指令而不结束。

## 工作原理

### 前置条件检查（所有模式）

在任何运动模式处理之前，`Begin` 会校验该轴的状态。第一个失败的检查会设置一个错误码，命令被拒绝且不启动任何运动：

| 拒绝 `Begin` 的条件 | 错误码 |
|---|---|
| 电机失能（[MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) ≠ on） | 39 |
| [ModRev](../../03-encoder/04-modulo-mode/ModRev.md) ≠ 0 但超出 [RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md)/[FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md) | 267 |
| 回零进行中 | 109 |
| 不处于位置运行模式 | 156 |
| 静态制动器已抱闸且正在使用 | 114 |
| 参考值已超出软件限位，且模式不是点动/PTP/速度摇杆 | 164 |
| 在间接模式下（jog/PTP/PTP-rep/PD-indirect/gear-indirect/eCam-indirect/joystick-pos-indirect）[Speed](../03-kinematics-configuration/Speed.md) 超过 [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md) | 271 |
| （central-i v5）在点动或 PTP 系列模式下（PTP、PTP-rep 以及 v5 正弦 PTP 模式 20/21），指令的 [Accel](../03-kinematics-configuration/Accel.md) 或 [Decel](../03-kinematics-configuration/Decel.md) 超过 [MaxAcc](../../06-protections/03-motion/general-maximum-limits/MaxAcc.md) | 324 |
| 龙门过渡进行中（该轴尚未为平滑过渡做好准备） | 292 |
| [MotionMode](../02-motion-configuration/MotionMode.md) 不是有效的运动模式 | 48 |

### 特定于模式的校验与初始化

随后 `Begin` 根据 [MotionMode](../02-motion-configuration/MotionMode.md) 进行分支。常见的点到点和点动路径如下：

- **PTP**（[MotionMode](../02-motion-configuration/MotionMode.md) `= 1`）：若 [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) ≠ 0，则绝对目标按 `PosRef + RelTrgt` 重新计算；该目标会针对 [RevPLim](../../06-protections/03-motion/position-limit-protection/RevPLim.md)/[FwdPLim](../../06-protections/03-motion/position-limit-protection/FwdPLim.md) 进行范围检查（错误码 161），并针对运动方向上的限位开关进行检查（错误码 162）。随后用当前 [PosRef](../01-kinematics-status/PosRef.md)、零初始速度、目标、[Speed](../03-kinematics-configuration/Speed.md)、[Accel](../03-kinematics-configuration/Accel.md)、[Decel](../03-kinematics-configuration/Decel.md) 以及 [JerkInAcc](../03-kinematics-configuration/JerkInAcc.md)/[JerkInDec](../03-kinematics-configuration/JerkInDec.md) 为加加速度规划器装填初值。
- **PTP-repetitive**（[MotionMode](../02-motion-configuration/MotionMode.md) `= 2`）：此外还根据 [RptMode](../02-motion-configuration/RptMode.md)（往复 vs 单向）计算返回目标，对**两个**目标都进行范围检查，并将重复计数器 [RptCounter](../05-motion-status/RptCounter.md) 重置为 0。
- **点动 / 速度摇杆**：若某次点动的 [Speed](../03-kinematics-configuration/Speed.md) 符号会将该轴驱入已激活的 RLS/FLS，则拒绝该次点动。

### 武装该次运动

对每种模式，最后一步（在关中断状态下）会设置运动状态位并重置每次运动的状态：

| `Begin` 设置的字段 | 值 | 含义 |
|---|---|---|
| [MotionStat](../05-motion-status/MotionStat.md) bit 0（运动中位） | 1 | 该轴处于运动中——规划器现已接管 [PosRef](../01-kinematics-status/PosRef.md) |
| [MotionStat](../05-motion-status/MotionStat.md) bit 9（等待输入位） | 1（仅当 [BeginDInOn](BeginDInOn.md) `= 1`） | 运动已武装但暂停，直到某个数字量输入上升沿到来 |
| [MotionReason](../05-motion-status/MotionReason.md) | 0 | 清除任何先前的停止原因 |
| [InTargetStat](../05-motion-status/InTargetStat.md) | 2 | 整定状态设为“运动中” |
| 运动采样计数器 | 0 | 重启 [MotionSamples](../05-motion-status/MotionSamples.md) 计时 |
| 摩擦补偿标志 | 1 | 在首个运动采样时重新装填速度积分 |

设置运动中位（bit 0）才是真正将 [PosRef](../01-kinematics-status/PosRef.md) 的控制权交给规划器的动作：在下一个控制周期，规划器使用 `Accel × AccelFact` 朝 [Speed](../03-kinematics-configuration/Speed.md) 加速，并用 [Decel](../03-kinematics-configuration/Decel.md) 规划其停止（减速距离前瞻参见 [Decel](../03-kinematics-configuration/Decel.md)）。当设置了 [BeginDInOn](BeginDInOn.md) 时，等待输入位（bit 9）将该轴保持静止，且在所配置的输入上升之前不递增运动时间计数器。

## 示例

```text
ABegin               ; start motion with the current mode and targets
APTPKeepMoving=1     ; allow retargeting on the fly (AbsTrgt can be updated without re-issuing Begin)
```

要在 A 轴上运行一次 100000 单位的绝对点到点运动：选择 PTP，设置目标和运动学参数，然后启动。

```text
AMotionMode=1        ; PTP
AAbsTrgt=100000      ; absolute target
ASpeed=50000         ; cruise speed
ABegin               ; start the move
```

### 演练：完整的 PTP 设置、命令与整定校验

一个完整的周期——设置运动学参数、命令运动、轮询直到稳定到位，然后检查停止原因：

```text
AMotorOn=1            ; enable the axis (precondition for Begin)
AMotionMode=1         ; PTP
ASpeed=500000         ; cruise velocity (must be <= MaxVel in indirect modes)
AAccel=1000000        ; leading slope
ADecel=1000000        ; trailing slope
AJerk=0               ; trapezoid; set non-zero for S-curve smoothing
AInTargetTol=50       ; settling window (user units)
AInTargetTime=20      ; minimum dwell (ms)
AAbsTrgt=100000       ; absolute target
ABegin                ; start the move
```

在运动期间和之后进行轮询：

```text
AMotionStat                   ; bit 0 = in motion; bit 4 accel, bit 5 decel, bit 6 smoothing tail
AInTargetStat                 ; 2 in motion -> 3 settling -> 4 reached
AInTargetStat                 ; once 4, the move is fully settled
AMotionReason                 ; expect 0 (normal end); see MotionReason for non-zero codes
APosErr                       ; final tracking error in user units
```

如果 `Begin` 被*拒绝*，则不会设置任何运动位——检查 [ErrLog](../../07-status-and-faults/ErrLog.md) 以获取拒绝码（例如 39 电机失能、161 目标超出软件限位、271 `Speed` 超过 `MaxVel`）。

### 边界情况

- **电机失能：** 以错误 39 拒绝（运动要求电机使能）。
- **超范围“写入”：** `Begin` 是一个无值函数；该关键字不携带需要校验的负载。
- **仿真模式（`MotorType` = 5）：** 允许；仿真路径仍会运行规划器并更新合成反馈。
- **ModRev 环绕：** 允许；运动期间环绕仍会继续应用于参考值。
- **存在激活故障：** 因电机失能而被拒绝。
- **已处于运动中（`ok_in_motion: false`）：** 解释器在命令到达处理程序之前以错误 21（运动中不允许）拒绝它。运动中门控检查的是**整个** [MotionStat](../05-motion-status/MotionStat.md) 字是否非零，而不仅仅是运动中位（bit 0）。因此，残留或过期的状态位——例如重复停止位（bit 2）或多轴组成员位（CNCA bit 10、CNCB bit 13、vector bit 19）——会使门控读为“运动中”，即使该轴在物理上处于静止也会拒绝 `Begin`。
- **使用 `PTPKeepMoving = 1` 的 PTP 重新设定目标：** 原始运动永远不会报告“完成”——当 `PTPKeepMoving = 1` 时规划器会跳过其运动结束检查，因此该轴保持运动中。可通过实时写入新的 [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md)（或 [RelTrgt](../13-motion-mode-ptp/RelTrgt.md)）来重新设定目标（两者均为 `ok_in_motion: true`）；规划器会在不先停止的情况下斜坡过渡到新目标。**不要**再次发出 `Begin` 来重新设定目标——`Begin` 为 `ok_in_motion: false`，运动期间第二次发出 `Begin` 会在到达处理程序之前以错误 21（运动中不允许）被拒绝。
- **`BeginDInOn = 1`：** `Begin` 被接受且 [MotionStat](../05-motion-status/MotionStat.md) 的 bit 9（等待输入）被置位；规划器在所配置的数字量输入上升之前不会启动。
- **龙门：** 在龙门平滑过渡进行期间该轴尚未就绪，`Begin` 会以错误 292 被拒绝，直到龙门就绪。
- **多轴模式（CNCA、CNCB、vector、spline-buffer）：** 在成员轴上发出 `Begin` 会武装主轴；其特定于模式的校验与 PTP 不同。

## 版本间的差异

在 **v5（central-i）** 中，`Begin` 增加了两项前置条件检查并支持更多运动模式：

| | v4（standalone &amp; central-i） | v5（central-i） |
|---|---|---|
| MaxAcc 检查 | 无 | 若 [Accel](../03-kinematics-configuration/Accel.md) 或 [Decel](../03-kinematics-configuration/Decel.md) 超过 [MaxAcc](../../06-protections/03-motion/general-maximum-limits/MaxAcc.md)，则拒绝（错误 324）（点动 / PTP / PTP-rep / 正弦 PTP / 正弦 PTP-rep 模式） |
| 换相检查 | 无 | 若电机尚未定相（[StatReg](../../07-status-and-faults/StatReg.md) 换相位 bit 0 为清零），则拒绝（错误 31）。在龙门模式下，主轴及其配对轴都必须已定相 |
| 正弦 PTP 模式 | 不存在 | 识别正弦 PTP 和正弦 PTP-repetitive 模式 |
| 位置限位 / 速度 | 32 位 | 64 位 |

成功的 `Begin` 所设置的位（[MotionStat](../05-motion-status/MotionStat.md) bit 0/9、[MotionReason](../05-motion-status/MotionReason.md) `= 0`）保持不变。**v5 仅适用于 central-i。**

## 另请参阅

- [MotionMode](../02-motion-configuration/MotionMode.md) — 选择要启动的运动类型
- [Stop](Stop.md) — 受控停止（使用 `Decel`）
- [Abort](Abort.md) — 立即停止
- [BeginDInOn](BeginDInOn.md) — 将 `Begin` 推迟到某个数字量输入边沿
- [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) / [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) — 由 `Begin` 校验的点到点目标
- [MotionStat](../05-motion-status/MotionStat.md) — 由 `Begin` 设置的 bit 0/9
- [MotionReason](../05-motion-status/MotionReason.md) — 由 `Begin` 重置为 0
- [PosRef](../01-kinematics-status/PosRef.md) — 一旦运动中位被置位，规划器所驱动的参考值
- [PTPKeepMoving](../02-motion-configuration/PTPKeepMoving.md) — 保持 PTP 运动持续有效以便实时重新设定目标
