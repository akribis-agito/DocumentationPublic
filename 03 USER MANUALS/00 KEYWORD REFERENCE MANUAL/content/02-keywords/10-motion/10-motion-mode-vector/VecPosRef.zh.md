---
keyword: VecPosRef
summary: 只读的沿矢量路径当前运行位置（0 至 VecAbsTrgt），始终为正值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 643
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
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# VecPosRef

只读的沿矢量路径当前运行位置（0 至 VecAbsTrgt），始终为正值。

## 概述

`VecPosRef` 是一个状态参数，报告矢量运动曲线沿矢量路径的当前位置参考。它从 0 开始，运动结束时达到 [VecAbsTrgt](VecAbsTrgt.md) 的值。`VecPosRef` 始终为正值，其时间导数由 [VecdPosRef](VecdPosRef.md) 报告。

## 工作原理

`VecPosRef` 是整个矢量运动的主坐标。矢量运动沿路径运行单一速度曲线；每个控制周期，控制器推进路径速度（由 [VecSpeed](VecSpeed.md)、[VecAccel](VecAccel.md)、[VecDecel](VecDecel.md) 和 [VecJerk](VecJerk.md) 整形），并将其累积到 `VecPosRef` 中，使该值从 0 单调递增至 [VecAbsTrgt](VecAbsTrgt.md)。

累积过程在内部以更高精度进行，以确保分数路径运动不产生漂移；`VecPosRef` 通过将该值四舍五入回用户单位来报告。可选地，可对路径位置应用滤波器，在将参考分配至各轴之前对其进行平滑处理。

每个控制周期，控制器根据几何形状（[VecType](VecType.md)）将 `VecPosRef` 转换为各轴位置参考：

- **线性** — 每个成员轴被设置为其起始点加上路径分数（`VecPosRef ÷ VecAbsTrgt`）乘以该轴的总行程，使各轴共同沿直线运行。
- **圆弧** — `VecPosRef ÷ radius` 给出从起始角度（沿 [VecArcDir](VecArcDir.md) 设定的方向）扫过的角度；两轴位置则为圆心坐标加上 radius × 该角度的余弦值/正弦值。

由于所有轴均由此单一坐标派生，无论各轴的单独速度如何，它们始终在路径上保持精确协调。当 `VecPosRef` 达到 `VecAbsTrgt` 且路径速度降至（接近）零时，运动被宣告完成，此时各成员轴将被捕捉到其精确终点。

## 示例

```text
AVecPosRef          ; 读取沿矢量路径的当前位置
```

## 另请参阅

- [VecAbsTrgt](VecAbsTrgt.md) — 总路径距离（`VecPosRef` 的终值）
- [VecdPosRef](VecdPosRef.md) — `VecPosRef` 的导数（路径速度）
