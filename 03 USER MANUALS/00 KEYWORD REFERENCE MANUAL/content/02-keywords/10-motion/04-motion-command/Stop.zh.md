---
keyword: Stop
summary: 受控停止；使用正常的 Decel 速率将该轴减速至静止。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 132
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
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# Stop

受控停止；使用正常的 `Decel` 速率将该轴减速至静止。

## 概述

`Stop` 使用正常的 [Decel](../03-kinematics-configuration/Decel.md) 速率以**受控减速**将该轴带至静止。与立即清除运动的 [Abort](Abort.md) 不同，`Stop` 本身并不停止运动——它设置一个*请求*位，由轨迹规划器在下一个控制周期拾取，然后将规划器速度斜坡降至零。它是一个轴相关的命令函数，可在运动期间随时发出。

## 工作原理

### 单轴运动

对于一次正常的单轴运动，`Stop`（在关中断状态下）设置停止请求位并记录原因——但仅当该轴确实处于运动中时：

| `Stop` 设置的字段 | 值 | 含义 |
|---|---|---|
| [MotionStat](../05-motion-status/MotionStat.md) bit 3（停止请求） | 1 | 已请求一次减速至停止 |
| [MotionReason](../05-motion-status/MotionReason.md) | 1 | 记录本次运动因 `Stop` 而结束 |

在下一个周期，规划器看到停止请求位并将其**目标速度强制为零**。随后速度以 `Decel × AccelFact` 斜坡下降，并由 [Jerk](../03-kinematics-configuration/Jerk.md)/[JerkInDec](../03-kinematics-configuration/JerkInDec.md) 平滑，与正常运动的尾部斜坡完全一致。由于原因码是受控停止原因（1，而非限位/故障原因），规划器继续使用 [Decel](../03-kinematics-configuration/Decel.md)——它**不会**替换为 [EmrgDec](../03-kinematics-configuration/EmrgDec.md)。

规划器仅对以下五个 [MotionReason](../05-motion-status/MotionReason.md) 码用 `EmrgDec × AccelFact` 计算其最终减速度——到达 RLS（4）、到达 FLS（5）、到达反向位置限位（6）、到达正向位置限位（7），以及由输入触发的受控停止（28）——而对其他所有原因（包括 `Stop` 命令（1））用 `Decel × AccelFact`。这两个停止来源在 [MotionStat](../05-motion-status/MotionStat.md) 中也是不同的：`Stop` 设置停止请求位（bit 3），而受控停止数字量输入设置受控停止请求位（bit 16）。规划器将任一请求位都视为“已请求停止”，但只有受控停止输入原因（28）才选择 `EmrgDec` 斜坡。

当规划器速度在停止请求待处理的情况下到达零时，运动进入平滑结束尾部，并最终清除所有运动位。[MotionReason](../05-motion-status/MotionReason.md) 在该轴静止后保持值 `1`。

### 组运动

如果该轴是某个组的成员，`Stop` 会沿整个组请求停止，而不是单个轴：

- **CNCA / CNCB 成员**：在每个成员轴和 CNC 路径上请求停止；发出命令的轴得到 [MotionReason](../05-motion-status/MotionReason.md) = 1（Stop 命令），其他成员得到 [MotionReason](../05-motion-status/MotionReason.md) = 19（一个 CNC 成员已停止）。CNC 步进模式被禁用以便停止能够进行。
- **Vector 成员**：在所有成员上请求停止并将主 vector 状态设为正在停止；发出命令的轴得到 [MotionReason](../05-motion-status/MotionReason.md) = 1（Stop 命令），其他成员得到 [MotionReason](../05-motion-status/MotionReason.md) = 31（一个 vector 成员已停止）。
- **Spline-buffer 成员**：在所有缓冲区成员上请求停止；发出命令的轴得到 [MotionReason](../05-motion-status/MotionReason.md) = 1（Stop 命令），其他成员得到 [MotionReason](../05-motion-status/MotionReason.md) = 37（一个 spline-buffer 成员已停止）。（若要在缓冲区运动当前周期结束时停止而非立即减速，请使用 [StopBuff](StopBuff.md)。）

## 示例

```text
AStop                ; controlled stop using the normal Decel rate
```

### 边界情况

- **电机失能：** `Stop` 被接受但无效果（没有正在运行的规划器）。
- **不处于运动中：** `Stop` 不更新任何状态——该函数在设置停止请求位之前会检查运动中位。
- **超范围“写入”：** 函数无值。
- **仿真模式（`MotorType` = 5）：** 允许；仿真规划器斜坡下降。
- **ModRev 环绕：** 斜坡下降会穿过环绕工作；规划器在零速度处停止，无论环绕将其留在何处。
- **存在激活故障：** 该轴被禁用——`Stop` 是空操作（电机失能路径覆盖斜坡）。
- **在重复 PTP（`MotionMode = 2`）的停留期间：** 停止请求被执行并结束重复；停留的等待计数器被放弃。
- **PTPKeepMoving = 1：** `Stop` 仍会结束运动；keep-moving 标志被停止请求位覆盖。
- **CNCA / CNCB / vector / spline-buffer 成员：** 整个组被请求停止；每轴原因如上所列。

## 另请参阅

- [Abort](Abort.md) — 立即停止（一次性清除运动；不是 `Decel` 斜坡）
- [Begin](Begin.md) — 本 `Stop` 所结束的命令
- [Decel](../03-kinematics-configuration/Decel.md) — `Stop` 使用的减速度速率
- [Jerk](../03-kinematics-configuration/Jerk.md) / [JerkInDec](../03-kinematics-configuration/JerkInDec.md) — 平滑 `Stop` 的尾部斜坡
- [EmrgDec](../03-kinematics-configuration/EmrgDec.md) — 紧急速率（用于限位/故障停止，而非 `Stop`）
- [MotionStat](../05-motion-status/MotionStat.md) — 由 `Stop` 设置的 bit 3（停止请求）
- [MotionReason](../05-motion-status/MotionReason.md) — 由 `Stop` 设置的原因码 1
- [StopBuff](StopBuff.md) / [StopRep](StopRep.md) — 特定于模式的停止变体
