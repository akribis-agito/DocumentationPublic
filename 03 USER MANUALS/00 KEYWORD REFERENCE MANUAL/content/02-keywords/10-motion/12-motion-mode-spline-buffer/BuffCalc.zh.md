---
keyword: BuffCalc
summary: 命令，根据缓冲区路径点预先计算样条系数。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 547
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 1
  data_type: int32
  ok_in_motion: false
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
# BuffCalc

命令，根据缓冲区路径点预先计算样条系数。

## 概述

`BuffCalc` 通过 [BuffPos](BuffPos.md) / [BuffTime](BuffTime.md) 中的路径点拟合样条曲线，并将其展开为可立即回放的插值轨迹。该命令必须在**主轴**上发出，在路径点数组和形状设置加载完毕之后、以样条缓冲区模式发出 `Begin` 之前执行，以确保控制器已有准备就绪的轨迹可供执行。轴运动中不可发出该命令。

## 工作原理

### 命令执行内容

对于组内每个成员轴，`BuffCalc`：

1. **验证 [BuffTime](BuffTime.md)**——第一个条目非零、值严格递增、存在零终止符，且最后一个时间戳在控制器插值容量范围内。
2. **拟合曲线**，依据 [BuffSplineMod](BuffSplineMod.md) 所选类型（线性 / 抛物线 / 三次），使用 [BuffEdgeMode](BuffEdgeMode.md) 的边界条件，以及该模式所需的 [BuffSlopes](BuffSlopes.md) 斜率。主轴的形状设置和时间基准应用于所有成员；各成员使用各自的位置数据。
3. **展开曲线**——从起点到最后一个时间戳，生成每个伺服采样周期对应的一个插值位置，并内部存储以供回放。
4. **将组信息写入 [BuffStatus](BuffStatus.md)**：主轴、成员轴集合、各轴计算曲线的峰值速度和加速度，以及最后一个点的索引。随后为每个成员清除"需要重新计算"标志。

### 为何修改后必须重新运行

控制器跟踪自上次 `BuffCalc` 以来是否有任何样条参数被修改。写入 [BuffPos](BuffPos.md)、[BuffTime](BuffTime.md)、[BuffSplineMod](BuffSplineMod.md)、[BuffEdgeMode](BuffEdgeMode.md) 或 [BuffSlopes](BuffSlopes.md) 均会置位该标志。若在任意成员上该标志被置位时发出 `Begin`，命令将被**拒绝**，以防止运行过时的轨迹——请重新发出 `BuffCalc` 以清除该标志。

### 导致 BuffCalc 失败的条件

若满足以下任一条件，`BuffCalc` 将返回错误（且不计算任何内容）：

| 条件 | 原因 |
|---|---|
| 第一个时间戳为零 | `BuffTime[1]` = 0。 |
| 时间戳非严格递增 | 某个 `BuffTime` 条目等于或小于前一个值。 |
| 无终止零 | `BuffTime` 列表中未出现零条目。 |
| 轨迹过长 | 最后一个时间戳超出内部插值容量。 |
| 主轴不在成员集合中 | 发出 `BuffCalc` 的轴未包含在其自身组的成员集合中。 |
| 某成员正在执行样条缓冲区运动 | 成员运动期间不允许重新计算。 |

## 示例

```text
ABuffPos[1]=0
ABuffPos[2]=10000
ABuffTime[1]=100
ABuffTime[2]=300
ABuffTime[3]=0       ; terminator
ABuffCalc            ; fit and expand the trajectory (run before Begin)
```

## 另请参阅

- [BuffPos](BuffPos.md) — 拟合所用的路径点位置
- [BuffTime](BuffTime.md) — 在此处验证的路径点时间戳
- [BuffSplineMod](BuffSplineMod.md) — 拟合时应用的曲线类型
- [BuffEdgeMode](BuffEdgeMode.md) / [BuffSlopes](BuffSlopes.md) — 拟合时应用的边界条件
- [BuffStatus](BuffStatus.md) — 本命令写入的组信息及峰值速度/加速度
