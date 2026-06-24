---
keyword: VecdPosRef
summary: 只读的矢量位置参考导数（矢量速度），始终为正值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 644
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# VecdPosRef

只读的矢量位置参考导数（矢量速度），始终为正值。

## 概述

`VecdPosRef` 是一个状态参数，报告矢量运动位置参考的导数，即 [VecPosRef](VecPosRef.md) 的时间导数。它表示沿矢量路径的瞬时速度，并遵循由 [VecAccel](VecAccel.md)、[VecDecel](VecDecel.md) 和 [VecSpeed](VecSpeed.md) 整形的曲线。`VecdPosRef` 始终为正值。

## 工作原理

`VecdPosRef` 在每个控制周期计算为（经过滤波、高精度）路径位置 [VecPosRef](VecPosRef.md) 在该周期内的变化量，以计数/秒表示。因此，它是运动的实时路径速度：

- 加速期间，以 [VecAccel](VecAccel.md) 的速率上升，趋向巡航上限 [VecSpeed](VecSpeed.md)；
- 运动处于巡航速度时保持巡航值；
- 路径终点临近时，以 [VecDecel](VecDecel.md)（或在停止或故障时以 [VecEmrgDec](VecEmrgDec.md)）下降。

它是沿路径的合成速度，而非任何单个成员轴的速度；各成员轴以 `VecdPosRef` 乘以其路径份额（线性运动中为方向余弦，圆弧上为切向分量）的速度运行。控制器在运动结束时将其强制精确置零，使报告值干净地归零。[VecPause](VecPause.md) 将其斜坡降至 0，恢复时再斜坡升回。

## 示例

```text
AVecdPosRef         ; 读取沿矢量路径的当前速度
```

## 另请参阅

- [VecPosRef](VecPosRef.md) — 本参数报告其导数的位置参考
- [VecSpeed](VecSpeed.md) — 指令最大合成速度
