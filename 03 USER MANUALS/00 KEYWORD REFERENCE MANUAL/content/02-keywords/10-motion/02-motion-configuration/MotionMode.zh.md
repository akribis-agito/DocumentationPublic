---
keyword: MotionMode
summary: 选择发出 Begin 时所执行的运动类型。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 141
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - -1
  - 19
  default: -1
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range:
    - -1
    - 21
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# MotionMode

选择发出 `Begin` 时所执行的运动类型。

## 概述

`MotionMode` 决定发出 [Begin](../04-motion-command/Begin.md) 命令时将执行的运动类型。它是轴运动引擎的主选择器，可在点动、点到点、重复、脉冲方向、电子齿轮、ECAM 等模式之间进行选择。该模式还决定了哪些运动学参数和目标关键字相关（例如，重复模式使用 [RptMode](RptMode.md)、[RptCycles](RptCycles.md) 和 [RptWait](RptWait.md)）。在当前运动结束之前，它无法被更改。

## 工作原理

`Begin` 读取 `MotionMode` 并根据其值进行分支。值 `-1`（无效选择）会被拒绝并返回错误，每个有效值在置位 [MotionStat](../05-motion-status/MotionStat.md) 的运动中位（位 0）之前都会运行各自的初始化设置。这些模式分为两大类：

- **间接**模式 —— 由控制器自身的规划器在 [Speed](../03-kinematics-configuration/Speed.md)/[Accel](../03-kinematics-configuration/Accel.md)/[Decel](../03-kinematics-configuration/Decel.md) 约束下生成轨迹：点动、PTP、PTP 重复、PD 间接、电子齿轮间接、eCam 间接、摇杆位置间接。若 `|Speed|` 超过 [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md)，`Begin` 会以错误码 271 拒绝这些模式。在 central-i v5 上，若 `Accel` 或 `Decel` 超过 [MaxAcc](../../06-protections/03-motion/general-maximum-limits/MaxAcc.md)，`Begin` 还会以错误码 324 额外拒绝点动以及 PTP 系列模式（PTP、PTP 重复，以及 v5 正弦 PTP 模式 20/21）。MaxAcc 闸门**不**适用于 PD/电子齿轮/eCam/摇杆间接模式。
- **直接**模式 —— 参考值由用户的位置/速度指令直接驱动（脉冲方向直接、电子齿轮直接、ECAM 直接、FIFO、从轴、CNCA/CNCB、矢量、样条缓冲区、摇杆速度）。

下表列出了 `MotionMode` 所描述的运动类型。

| MotionMode | Descriptions |
|---|---|
| -1 | **无效选择。** 这是 MotionMode 的默认值。 |
| 0 | **点动运动** 电机将加速至 Speed 指定的恒定速度，并保持该速度直至收到 Stop 命令。点动方向由 Speed 关键字的符号决定。**相关关键字：** Speed, Accel, Decel, JerkMode, JerkInAcc, JerkInDec |
| 1 | **点到点运动** 若 RelTrgt = 0，轴移动到由 AbsTrgt 定义的位置。否则，轴根据 RelTrgt 相对于初始位置移动。生成的运动曲线将保持在 Speed、Accel、Decel 以及可选的 JerkInAcc 和 JerkInDec 的最大运动学限值之内。**相关关键字：** RelTrgt, AbsTrgt, Speed, Accel, Decel, JerkMode, JerkInAcc, JerkInDec |
| 2 | **点到点重复运动** 若 RelTrgt = 0，轴移动到由 AbsTrgt 定义的位置，然后返回初始位置。否则，轴根据 RelTrgt 相对于初始位置移动，然后返回初始位置。重复运动将无限期持续，直至发出 StopRep 或 RptCounter 等于用户定义的 RptCycles。轴在每次运动之间会停留 RptWait。生成的运动曲线将保持在 Speed、Accel、Decel 以及可选的 JerkInAcc 和 JerkInDec 的最大运动学限值之内。**相关关键字：** RelTrgt, AbsTrgt, Speed, Accel, Decel, JerkMode, JerkInAcc, JerkInDec |
| 3 | **脉冲方向（PD）运动 – 直接模式** 轴将跟随由脉冲方向输入生成的曲线。更多信息请参阅 Motion mode – Pulse and direction。 |
| 4 | **脉冲方向（PD）运动 - 间接模式** 轴将跟随由脉冲方向输入生成的二阶曲线，受指定的加速度和速度值限制。更多信息请参阅 Motion mode – Pulse and direction。 |
| 5 | **电子齿轮运动 – 直接模式** 轴将跟随按比例跟踪主变量的曲线。更多信息请参阅 Motion mode – Gear motion。 |
| 6 | **电子齿轮运动 – 间接模式** 轴将跟随二阶运动曲线（受指定的加速度和速度值限制），其中生成的曲线按比例跟踪主变量的变化。更多信息请参阅 Motion mode – Gear motion。 |
| 7 | **电子凸轮（ECAM）运动 - 直接模式** 轴将进行永久性的相对运动，其中相对位置参考（相对于 Begin 命令时的初始位置）取决于主变量。相对位置参考在每个控制器周期从一个可定制的数组中获得，该数组映射到用户定义且均匀间隔的主位置范围。这类似于机械凸轮-从动件运动。更多信息请参阅 Motion mode – ECAM motion。 |
| 8 | **电子凸轮（ECAM）运动 - 间接模式** 该运动模式保留供内部使用。 |
| 9 | FIFO 运动 |
| 10 | **直接从轴运动** 轴 A 的位置参考在每个控制周期由轴 B 位置参考的变化直接驱动，并按 [MasterFact](../07-motion-mode-gear-motion/MasterFact.md) 缩放。这是一个独立的、范围更窄的机制，区别于电子齿轮运动（它不使用 `GearMaster`、`MasterPos` 或 `MasterFilt`）。仅在多轴版本上可用。更多信息请参阅 [MotionMode10](../07-motion-mode-gear-motion/MotionMode10.md)。 |
| 11 | CNCA 运动 |
| 12 | 摇杆位置直接模式 |
| 13 | 摇杆位置间接模式 |
| 14 | 摇杆速度直接模式 |
| 15 | 摇杆速度间接模式 |
| 16 | 矢量运动 |
| 17 | CNCB 运动 |
| 18 | 样条缓冲区 |
| 19 | FIFO 位置跟踪 |

## 版本间的变化

| | v4 (standalone &amp; central-i) | v5 (central-i) |
|---|---|---|
| Range | −1 … 19 | −1 … **21** |
| Mode 20 | 未定义 | **正弦点到点曲线** |
| Mode 21 | 未定义 | **正弦点到点曲线（重复）** |

v5 新增了两种正弦曲线点到点模式。与其他 PTP 系列模式一样，正弦模式（20/21）受 `Begin` 在 [MaxVel](../../06-protections/03-motion/general-maximum-limits/MaxVel.md)（错误 271）和 [MaxAcc](../../06-protections/03-motion/general-maximum-limits/MaxAcc.md)（错误 324）上的双重闸门约束。**v5 仅适用于 central-i。**

## 示例

```text
AMotionMode=1        ; point-to-point motion
AMotionMode=2        ; repetitive point-to-point motion
AMotionMode         ; query current mode
```

## 参见

- [Begin](../04-motion-command/Begin.md) —— 在所选模式下启动运动
- [JerkMode](JerkMode.md) —— 规划器阶数（模式 1 和 2）
- [RptMode](RptMode.md) —— 重复方向（模式 2）
- [RptCycles](RptCycles.md) —— 重复次数（模式 2）
- [RptWait](RptWait.md) —— 重复之间的停留（模式 2）
- [MotionStat](../05-motion-status/MotionStat.md) —— 每种模式置位哪些状态位（参见其中的模式位映射）
- [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) / [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) —— PTP 模式的目标（1 和 2）
