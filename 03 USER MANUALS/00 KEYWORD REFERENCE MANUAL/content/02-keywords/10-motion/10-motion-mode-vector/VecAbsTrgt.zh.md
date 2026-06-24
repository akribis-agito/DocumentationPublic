---
keyword: VecAbsTrgt
summary: 只读的矢量路径总距离（始终为正），从运动起点到终点。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 642
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
# VecAbsTrgt

只读的矢量路径总距离（始终为正），从运动起点到终点。

## 概述

`VecAbsTrgt` 是一个状态参数，用于报告矢量运动沿矢量路径从运动起点到终点的目标距离。`VecAbsTrgt` 始终为正值。它是运行中的位置参考 [VecPosRef](VecPosRef.md) 随运动完成而趋近的终值。

`VecAbsTrgt` 不用于*定义*矢量运动。运动由成员轴各自的目标关键字 [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) 或 [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) 定义；`VecAbsTrgt` 是由这些目标计算得出的路径总长度。

## 工作原理

矢量运动启动时，控制器解析每个成员轴的起点和终点（来自其绝对目标或相对目标），并一次性计算路径总长度，存储为 `VecAbsTrgt`。计算方式取决于几何类型（[VecType](VecType.md)）：

- **直线**（[VecType](VecType.md) = 0）：直线距离，即各轴行程距离的均方根。例如，一个轴移动 3000、另一个轴移动 4000，则 `VecAbsTrgt = 5000`。
- **圆弧**（[VecType](VecType.md) = 1）：弧长，等于扫过角度乘以半径。扫过角度从起始角按 [VecArcDir](VecArcDir.md) 设定的方向运行到终止角，并加上 [VecNumCircles](VecNumCircles.md) 所请求的整圈数（每圈 2π）。半径由 [VecArcCenter](VecArcCenter.md) 导出。

`VecAbsTrgt` 是路径坐标 [VecPosRef](VecPosRef.md) 的终值：路径速度曲线将 `VecPosRef` 从 0 斜坡上升至 `VecAbsTrgt`，减速预判使用剩余距离（`VecAbsTrgt − VecPosRef`）来规划制动时机。该值在运动过程中固定不变——运动中修改成员轴目标不会改变它。

## 示例

```text
AVecAbsTrgt         ; read the total vector path distance for the move
```

## 另请参阅

- [VecPosRef](VecPosRef.md) — 沿路径的运行位置（终值为 `VecAbsTrgt`）
- [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) / [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) — 定义运动的各轴目标
- [VecMemberAxes](VecMemberAxes.md) — 参与矢量运动的轴
