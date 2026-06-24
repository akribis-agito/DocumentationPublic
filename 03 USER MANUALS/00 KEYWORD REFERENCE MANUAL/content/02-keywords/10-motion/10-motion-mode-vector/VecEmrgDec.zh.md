---
keyword: VecEmrgDec
summary: 停止或故障时对所有成员轴施加的紧急矢量减速度。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 638
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
  - 100
  - 2000000000
  default: 100000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range:
    - 100.0
    - 686700000000.0
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# VecEmrgDec

停止或故障时对所有成员轴施加的紧急矢量减速度。

## 概述

`VecEmrgDec` 设置紧急减速率，单位为用户单位每秒平方，当成员轴在运动中到达软件位置限位，或输入信号请求受控停止时，对所有参与矢量运动的轴施加此减速率。通常将其设置为高于正常 [VecDecel](VecDecel.md)，以便在保持路径协调的同时尽快停止矢量运动。用户发出的 [StopVec](StopVec.md) 命令本身以正常 [VecDecel](VecDecel.md) 制动路径；`VecEmrgDec` 专用于限位触发的故障路径。该参数为轴相关参数，保存至闪存，可在任何时候（包括运动中）修改。

## 工作原理

矢量运动通常以 [VecDecel](VecDecel.md) 对路径速度进行减速。当限位触发的紧急停止被触发时，控制器设置一个内部标志，将路径规划器中的减速项从 `VecDecel` 切换为 `VecEmrgDec`，用于运动的剩余部分，使合成路径速度以此更快的速率斜坡减速至静止，同时保持成员轴沿路径协调运动。制动仍作用于单一路径速度，因此每个成员轴的减速率为 `VecEmrgDec` 乘以其在路径中的分量。

当成员轴在运动中到达软件位置限位时（其他成员轴的 [MotionReason](../05-motion-status/MotionReason.md) = 34，触发轴为 6 / 7），或输入信号请求受控停止时（[MotionReason](../05-motion-status/MotionReason.md) = 28），选用紧急减速率。用户发出的 [StopVec](StopVec.md) **不会**触发此标志——停止仍以 [VecDecel](VecDecel.md) 制动（[MotionReason](../05-motion-status/MotionReason.md) = 29，以及矢量停止位 [MotionStat](../05-motion-status/MotionStat.md) 第 18 位 / 掩码 `0x00040000`）。硬件反向/正向限位开关不通过此路径处理。

任一成员轴发生电机关闭或故障时，运动立即终止，而非以上述任一速率斜坡减速。

## 示例

```text
AVecEmrgDec=100000   ; emergency vector deceleration (user units/s^2, default)
AVecEmrgDec         ; read the current value
```

## 另请参阅

- [VecDecel](VecDecel.md) — 正常（受控）矢量减速
- [StopVec](StopVec.md) — 使用此速率制动的命令
- [MotionStat](../05-motion-status/MotionStat.md) — 矢量停止位（第 18 位）
- [MotionReason](../05-motion-status/MotionReason.md) — 停止原因代码 28 / 29 / 34
