---
keyword: VecSpeed
summary: 协调多轴运动中矢量（合成）速度的最大值，单位为用户单位/秒。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 635
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
  default: 10000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range: null
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# VecSpeed

协调多轴运动中矢量（合成）速度的最大值，单位为用户单位/秒。

## 概述

`VecSpeed` 设置协调多轴矢量运动（[MotionMode](../02-motion-configuration/MotionMode.md) = 16）的最大矢量（合成）速度，单位为用户单位每秒。各轴速度按比例缩放，使矢量幅值不超过该值，从而使多轴路径以受控的进给速率运行。加速和减速斜坡由 [VecAccel](VecAccel.md) 和 [VecDecel](VecDecel.md) 控制。该参数为轴相关参数，保存至闪存，可在任何时候修改，包括运动期间。

## 工作原理

矢量运动沿**路径**运行单一速度曲线，而非按轴分别运行。每个控制周期，控制器推进一个标量路径速度并将其加入路径位置 [VecPosRef](VecPosRef.md)；`VecSpeed` 是该路径速度的巡航上限（始终以正幅值处理——方向来自几何形状，而非符号）。

点到点（PTP）运动所用的相同规划器逻辑被应用于路径标量：

- 在梯形情况下（急动关闭，[VecJerk](VecJerk.md) = 0），路径速度每个控制周期增加 `VecAccel × Ts`，直到达到 `VecSpeed`，保持该速度，然后根据剩余路径距离和 `VecDecel` 计算减速距离前瞻，强制降速，生成梯形（或在短路径上为三角形）曲线。
- 在支持矢量急动整形的固件上，启用该功能（通过 [VecJerkMode](VecJerkMode.md)）会将同一 `VecSpeed` 作为 S 曲线规划器的路径速度峰值输入；否则矢量路径为梯形。

由于曲线是针对合成路径生成的，然后通过几何形状（[VecType](VecType.md)）分配至各成员轴，因此没有任何单个成员轴必然以 `VecSpeed` 运行——只有几何合成量才以该速度运行。例如，一个线性矢量运动在一个轴上行程为 `3000`，在第二个轴上行程为 `4000`，路径长度为 `5000`；当 `VecSpeed = 1000` 用户单位/秒时，合成进给速率巡航于 1000 用户单位/秒，而两个成员轴分别以 `1000 × 3/5 = 600` 和 `1000 × 4/5 = 800` 用户单位/秒巡航。控制器每个控制周期重新读取 `VecSpeed`，因此在运动中途提高或降低该值会在下一个控制周期重新定向路径速度目标。[VecPause](VecPause.md) 暂时将路径速度目标强制为 0；[StopVec](StopVec.md) 执行相同操作但结束运动。

报告的路径速度为 [VecdPosRef](VecdPosRef.md)；巡航值 `VecSpeed` 是其斜坡所趋向的上限。

## 示例

```text
AVecSpeed=10000      ; 最大合成速度（用户单位/秒，默认值）
AVecSpeed           ; 读取当前值
```

## 另请参阅

- [VecAccel](VecAccel.md) — 矢量加速度
- [VecDecel](VecDecel.md) — 矢量减速度
- [VecJerk](VecJerk.md) — 旧版 `0`-`9` 选择器，对矢量路径无效（请使用 [VecJerkMode](VecJerkMode.md)）
- [VecdPosRef](VecdPosRef.md) — 报告的路径速度（向 `VecSpeed` 斜坡靠近）
- [VecPosRef](VecPosRef.md) — 曲线推进的路径位置
