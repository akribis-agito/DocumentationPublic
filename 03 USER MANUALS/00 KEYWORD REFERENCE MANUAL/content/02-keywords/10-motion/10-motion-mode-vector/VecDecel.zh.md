---
keyword: VecDecel
summary: 矢量减速度（用户单位/s^2），将合成速度斜坡减速至静止。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 637
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# VecDecel

矢量减速度（用户单位/s^2），将合成速度斜坡减速至静止。

## 概述

`VecDecel` 设置协调多轴矢量运动（[MotionMode](../02-motion-configuration/MotionMode.md) = 16）的减速度，单位为用户单位每秒平方。它定义合成（矢量）速度在受控停止结束时从 [VecSpeed](VecSpeed.md) 斜坡减速至静止的快慢，作用于整条路径。该参数为轴相关参数，保存至闪存，可在任何时候（包括运动中）修改。

`VecDecel` 为受控（正常）减速；[VecEmrgDec](VecEmrgDec.md) 为停止或故障时使用的更快紧急减速率。

## 工作原理

矢量运动沿几何路径运行单一速度曲线（参见 [VecSpeed](VecSpeed.md)）。`VecDecel` 以两种方式设定该曲线的后沿斜率：

- **路径末端制动。** 每个控制周期，规划器根据到 [VecAbsTrgt](VecAbsTrgt.md) 的剩余路径距离，计算仍能使用 `VecDecel` 恰好在终点制动至静止的最高路径速度，并将路径速度钳位至该值。这使巡航阶段在运动结束时平滑减速至停止：

$$
v_{dec} = -\text{VecDecel} \cdot T_s + \sqrt{\text{VecDecel}^{2} \cdot T_s^{2} + 2 \cdot \text{VecDecel} \cdot (\text{VecAbsTrgt} - \text{VecPosRef})}
$$

- **速度降低。** 当 [VecSpeed](VecSpeed.md) 在运动中途降低，或请求 [VecPause](VecPause.md) 时，路径速度以 `VecDecel` 斜坡减速。

减速作用于**合成**路径速度；任一成员轴上的减速率为 `VecDecel` 乘以该轴在路径中的分量。`VecDecel` 为正常速率，也是 [StopVec](StopVec.md) 制动路径时所使用的速率；只有成员轴到达软件位置限位或输入信号请求受控停止时，才会改用更快的 [VecEmrgDec](VecEmrgDec.md)。启用急动平滑（[VecJerk](VecJerk.md) ≠ 0）时，`VecDecel` 作为减速度约束传递给 S 曲线路径规划器。

## 示例

```text
AVecDecel=100000     ; vector deceleration (user units/s^2, default)
AVecDecel           ; read the current value
```

## 另请参阅

- [VecAccel](VecAccel.md) — 矢量加速度
- [VecSpeed](VecSpeed.md) — 目标合成速度
- [VecEmrgDec](VecEmrgDec.md) — 紧急减速率
