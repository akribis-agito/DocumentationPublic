---
keyword: VecArcDir
summary: 矢量圆弧运动的扫描方向（0 = 逆时针，1 = 顺时针）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 634
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
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# VecArcDir

矢量圆弧运动的扫描方向（0 = 逆时针，1 = 顺时针）。

## 概述

对于圆弧矢量（[VecType](VecType.md) = 1），`VecArcDir` 定义圆弧方向：`0` 为逆时针（CCW），`1` 为顺时针（CW）。与所有矢量运动关键字一样，它是按轴设置的，但只有发出 [Begin](../04-motion-command/Begin.md) 命令的轴的 `VecArcDir` 生效。它与 [VecArcCenter](VecArcCenter.md) 配合使用，后者固定圆心和半径。

该参数保存至闪存，运动中不可修改。

## 工作原理

圆弧运动定义了两个轴。圆弧在这两个轴构成的平面内执行，第三轴不运动。两个轴的顺序有意义；例如，`B, C` 与 `C, B` 不同：

- 第一个轴为 **X** 轴。
- 第二个轴为 **Y** 轴。
- 逆时针运动围绕"Z"轴进行，X 轴向 Y 轴方向运动。

`VecArcDir` 决定扫过角度从起点到终点的移动方向，从而决定覆盖圆的多大部分：

- **逆时针（`0`）** — 角度从起始角增大至终止角。路径长度为递增的角度差（加上 [VecNumCircles](VecNumCircles.md) 的整圈数）乘以半径。
- **顺时针（`1`）** — 角度减小。路径长度为互补角度差（整圈减去逆时针角度差，加上额外整圈数）乘以半径。

因此，对于相同的起点、终点和圆心，切换 `VecArcDir` 可选择"短弧"或"长弧"方向。当起点与终点重合（整圆）时，逆时针和顺时针各自恰好扫过一整圈（2π）；可使用 [VecNumCircles](VecNumCircles.md) 在任意方向添加额外圈数。所得弧长存储为 [VecAbsTrgt](VecAbsTrgt.md)。

## 示例

```text
AVecArcDir=0         ; counter-clockwise arc (default)
AVecArcDir=1         ; clockwise arc
```

## 另请参阅

- [VecType](VecType.md) — 选择直线或圆弧矢量
- [VecArcCenter](VecArcCenter.md) — 圆弧圆心 / 半径定义
- [Begin](../04-motion-command/Begin.md) — 命令，其轴决定有效的 `VecArcDir`
