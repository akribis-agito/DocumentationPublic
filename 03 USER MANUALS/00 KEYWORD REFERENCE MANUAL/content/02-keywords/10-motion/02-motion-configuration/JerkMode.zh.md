---
keyword: JerkMode
summary: 选择点到点运动规划器阶数（二阶或三阶）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 722
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    units: user
    can_code: 567
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# JerkMode

选择点到点运动规划器阶数（二阶或三阶）。

## 概述

`JerkMode` 定义点到点运动规划器的阶数，它决定是否对移动施加加加速度（及 snap）限制。它仅在 [MotionMode](MotionMode.md) = 1 或 2（点到点运动）时使用。二阶曲线使用 [Speed](../03-kinematics-configuration/Speed.md)、[Accel](../03-kinematics-configuration/Accel.md)、[Decel](../03-kinematics-configuration/Decel.md) 和 [Jerk](../03-kinematics-configuration/Jerk.md)；三阶曲线另外使用 [JerkInAcc](../03-kinematics-configuration/JerkInAcc.md) 和 [JerkInDec](../03-kinematics-configuration/JerkInDec.md)。在轴运动中不可更改。

## 工作原理

`JerkMode` 用于定义点到点运动规划器的阶数，如下所示。

| JerkMode | 运动规划器阶数 | 相关关键字 |
|----|----|----|
| 0 | 2 (Infinite jerk) | Speed, Accel, Decel, Jerk |
| 1 | 3 (Infinite snap) | Speed, Accel, Decel, Jerk, JerkInAcc, JerkInDec |

每个控制周期，规划器读取 `JerkMode` 并据此选择其轨迹规律：当 `JerkMode = 0` 时使用二阶平方根减速规律，当 `JerkMode = 1` 时运行完整的加加速度规划器。控制器还会在限位/受控停止期间将阶数**覆盖**为二阶，因此无论 `JerkMode` 如何，紧急减速停止都不施加加加速度限制。

与规划器阶数无关，[Jerk](../03-kinematics-configuration/Jerk.md) 关键字设置一个 `2^Jerk` 周期的移动平均平滑尾段，规划器会在每次移动结束时将其排出（即 [MotionStat](../05-motion-status/MotionStat.md) bit 6 报告的曲线平滑尾段）。

### 减速触发（模式 1）

与二阶平方根减速规律不同，三阶规划器（`JerkMode = 1`）通过预测在加加速度限制的减速斜坡下使轴停止所需的**距离**来决定何时开始制动。每周期它计算梯形子曲线的减速距离（加加速度上升至 `Decel`、恒定 `Decel`、加加速度下降至零，使用 [JerkInDec](../03-kinematics-configuration/JerkInDec.md)）；对于无法达到完整 `Decel` 的短移动，它回退到三角形子曲线（加加速度上升然后加加速度下降，无恒定减速阶段）。当该预测距离仍小于到目标的剩余距离时，规划器保持在加速/巡航阶段；在首个达到或超过剩余距离的周期切换进入减速。

由于该切换通常落在某个控制周期的中途，规划器通过对加速阶段与减速阶段候选值之间的位置-目标误差进行线性插值来细化周期内确切的切换时刻，迭代几次直至预测落点位于目标约 0.1 计数以内。这正是加加速度限制的移动尽管更新速率离散仍能在目标上停止的原因。

### 边界情况

- **电机失能：** 该值被保持；在下次 `Begin` 时读取。
- **超出范围写入：** 参数系统拒绝 `0`–`1` 范围之外的值。
- **仿真模式（`MotorType` = 5）：** 规划器在仿真中以相同方式运行。
- **ModRev 回绕：** 与 `JerkMode` 无关；两种规划器阶数以相同方式处理回绕。
- **活动故障：** 轴被禁用；在重新使能并下次 `Begin` 时，再次读取当前 `JerkMode`。
- **硬件/软件限位停止或由输入触发的受控停止：** 在停止斜坡期间，`JerkMode` 被内部强制为 `0`（二阶），无论用户设置如何——这些紧急减速始终使用平方根规律。普通的 [Stop](../04-motion-command/Stop.md) 命令**不**属于此类：普通 `Stop` 按配置的 `JerkMode` 和正常的 [Decel](../03-kinematics-configuration/Decel.md) 减速。
- **回零期间：** 在整个回零序列期间，`JerkMode` 被强制为 `0`（二阶），无论用户设置如何；用户值在回零进入时保存，并在回零结束时恢复。
- **其他运动模式：** `JerkMode` 在 PTP（1）和重复 PTP（2）之外被忽略；点动、齿轮、ECAM、PD、CNC、矢量、操纵杆、FIFO、样条缓冲区和从轴各自使用其自身的轨迹规律。
- **运动中不可更改：** 当 [MotionStat](../05-motion-status/MotionStat.md) 非零时，写入被拒绝。

## 示例

```text
AJerkMode=0          ; second-order profile
AJerkMode=1          ; third-order profile
AJerkMode           ; query current value
```

## 另请参阅

- [MotionMode](MotionMode.md) — 必须为 1 或 2，`JerkMode` 才适用
- [Jerk](../03-kinematics-configuration/Jerk.md) — 二阶加加速度设置
- [JerkInAcc](../03-kinematics-configuration/JerkInAcc.md) — 加速期间的加加速度（三阶）
- [JerkInDec](../03-kinematics-configuration/JerkInDec.md) — 减速期间的加加速度（三阶）
