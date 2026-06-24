---
keyword: FIFOPosType
summary: 选择 FIFO 位置跟踪功能的工作模式。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 659
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
# FIFOPosType

选择 FIFO 位置跟踪功能的工作模式。

## 概述

`FIFOPosType` 选择通过 FIFO 位置跟踪队列流式传输的位置点在相邻周期之间的插值方式。它是位置跟踪子系统的插值模式设置，该子系统由 [FIFOPosFIFOEn](FIFOPosFIFOEn.md) 使能，由 [FIFOPosPush](FIFOPosPush.md) 填充。

与主 FIFO 运动模式（参见 [FIFOType](FIFOType.md)）不同——后者从速度型和加速度型*段*构建轨迹——位置跟踪流式传输一系列绝对**位置目标**。控制器每个周期取一个新目标，并通过在相邻目标之间插值来产生运动参考。`FIFOPosType` 选择用于该填充过程的插值规则。

该参数保存至闪存，在轴运动过程中不可更改。

## 工作原理

每个周期第一个采样时从队列取出一个新的位置目标（周期长度以伺服采样数计，由 [FIFOPosCycle](FIFOPosCycle.md) 设定）。周期之间，位置参考根据选定模式由周围目标计算得出：

| 值 | 模式 | 行为 |
|-------|------|----------|
| 0 | 线性插值（默认） | 参考值在当前周期起始目标与终止目标之间沿直线变化。需要两个目标。 |
| 1 | 三次样条插值 | 参考值沿经过四个连续目标（上一周期起始、当前周期起始、当前周期终止、下一周期终止）拟合的平滑三次曲线变化。这在周期边界处产生连续速度，代价是一个额外周期的前瞻延迟。 |

在两种模式下，插值参考在使用前均叠加 [FIFOPosPosOf](FIFOPosPosOf.md)，最终参考值仍受软件位置限位的钳位。

当轴进入位置跟踪模式时，工作目标和所有内部控制点均初始化为当前位置参考，使跟踪从轴当前所在位置平滑开始。同时，三个位置跟踪偏置 [FIFOPosPosOf](FIFOPosPosOf.md)、[FIFOPosVelOf](FIFOPosVelOf.md) 和 [FIFOPosCurrOf](FIFOPosCurrOf.md) 均复位为 0，每次运行均从无偏置的参考开始。

### 插值数学

参考值在每个采样点由周期内采样计数器重新计算，该计数器从 0 运行至 [FIFOPosCycle](FIFOPosCycle.md) − 1，并在下一周期第一个采样时回绕至 0（该计数器由 `FIFOPosStatus[6]` 报告）。记该计数器为 `k`，`FIFOPosCycle` 为 `N`，周期内插值因子为 `k / N`，取值范围为 `0, 1/N, 2/N, …, (N−1)/N`，最大值为 `(N − 1) / N`——始终严格小于 1。

**线性模式（`FIFOPosType=0`）。** 记 `T_start` 为当前周期起始目标，`T_end` 为当前周期终止目标（`FIFOPosStatus[2]` 和 `FIFOPosStatus[3]`），采样 `k` 处的参考值为

$$\text{PosRef}(k) = T_\text{start} + (T_\text{end} - T_\text{start})\,\frac{k}{N} + \text{FIFOPosPosOf}$$

**三次模式（`FIFOPosType=1`）。** 三次模式使用 Catmull-Rom 三次样条。以四个控制点 `P1` = 上一周期起始、`P2` = 当前周期起始、`P3` = 当前周期终止、`P4` = 下一周期终止（分别由 `FIFOPosStatus[1]` 至 `FIFOPosStatus[4]` 报告），当前周期的参考值为

$$\text{PosRef}(t) = P_2 + c_1 t + c_2 t^2 + c_3 t^3 + \text{FIFOPosPosOf}, \qquad t = \frac{k}{N} \in [0, 1)$$

$$c_1 = \frac{P_3 - P_1}{2}$$
$$c_2 = (P_1 - P_2) + 2(P_3 - P_2) - 0.5\,(P_4 - P_2)$$
$$c_3 = -0.5\,(P_1 - P_2) - 1.5\,(P_3 - P_2) + 0.5\,(P_4 - P_2)$$

（系数由相对于 `P2` 的目标值构成，`k` 为 `FIFOPosStatus[6]` 报告的周期内采样索引。）曲线在 `t = 0` 处精确经过 `P2`，在下一周期起始处精确经过 `P3`；`P1` 和 `P4` 仅设定切线，正是这一特性使速度在周期边界处连续。`P4` 是最近弹出的目标，因此三次模式渲染落后队列头一个周期——即一个周期的前瞻延迟。

**到达每个目标。** 由于周期内因子 `k / N` 永远不会达到 1，周期终止目标不会在其所在周期的最后一个采样产生。取而代之，在下一周期第一个采样时，周期起始控制点被推进至上一周期终止控制点，参考值被精确设置为该值加 `FIFOPosPosOf`。因此，在线性模式和三次模式下，轨迹均在目标被消耗后的一个周期精确经过每个压入的目标。

## 示例

```text
AFIFOPosType=0       ; linear interpolation between targets
AFIFOPosType=1       ; smooth cubic-spline interpolation
```

## 另请参阅

- [FIFOPosFIFOEn](FIFOPosFIFOEn.md) — 使能 FIFO 位置跟踪
- [FIFOPosPush](FIFOPosPush.md) — 压入位置目标
- [FIFOPosCycle](FIFOPosCycle.md) — 每目标采样数（周期长度）
- [FIFOPosStatus](FIFOPosStatus.md) — 位置跟踪队列状态
- [FIFOType](FIFOType.md) — 主（基于段的）FIFO 运动模式
