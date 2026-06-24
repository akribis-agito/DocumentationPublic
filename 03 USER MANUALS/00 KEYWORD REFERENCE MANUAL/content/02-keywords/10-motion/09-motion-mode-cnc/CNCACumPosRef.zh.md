---
keyword: CNCACumPosRef
summary: 自运动开始以来 CNC A 组跨所有段的累计指令路径位置。
availability:
  standalone: []
  central-i:
  - v5
can_code: 468
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2251799813685247
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CNCACumPosRef

自运动开始以来 CNC A 组跨所有段的累计指令路径位置。

## 概述

`CNCACumPosRef`（及其在第二 CNC 组上的对应项 [CNCBCumPosRef](CNCBCumPosRef.md)）报告自当前 CNC 运动开始以来沿 CNC 路径的**总指令行进距离**——即所有已完成段长度之和，加上当前正在执行段内的路径位置。该参数为只读 64 位值。

[CNCAPosRef](CNCAPosRef-CNCBPosRef.md) 在每段起点重置为零，而 `CNCACumPosRef` 则跨段边界持续递增，从而为整个编程路径提供一个单调递增的坐标。这使其便于进行进度跟踪，以及从路径位置（而非任何单个成员轴）驱动下游功能（例如虚拟编码器或基于位置的事件）。

仅适用于 Central-i（v5）。

## 工作原理

CNC 模式每个控制周期推进单一标量路径位置（参见 [CNCAPosRef](CNCAPosRef-CNCBPosRef.md)）。控制器维护所有已完成段长度的累计总和；每个周期报告：

```text
CNCACumPosRef = (已完成段长度之和) + (当前 CNCAPosRef)
```

- CNC 运动启动时，`CNCACumPosRef` 和已完成段总量**复位为 0**。
- 路径在段内推进时，`CNCACumPosRef` 与 [CNCAPosRef](CNCAPosRef-CNCBPosRef.md) 同步上升。
- 一段完成后，其完整长度被加入已完成段总量，[CNCAPosRef](CNCAPosRef-CNCBPosRef.md) 为下一段重新从零开始，因此 `CNCACumPosRef` 在转角处平滑延续，无跳变。

该值是指令**路径**坐标（驱动所有成员轴的主坐标），而非任何单个轴的位置。其每周期变化量即为 [CNCAdPosRef](CNCAdPosRef-CNCBdPosRef.md) 报告的路径速度。

`CNCACumPosRef` 可被选为虚拟编码器的来源。若以此方式使用，且 CNC 来源被复位（新运动启动），正在仿真该坐标的虚拟编码器将自动关闭，以避免跟踪一个已跳回零的坐标。

## 示例

```text
ACNCACumPosRef       ; 读取 A 组总指令路径距离
ACNCBCumPosRef       ; 读取 B 组总指令路径距离
```

## 另请参阅

- [CNCAPosRef/CNCBPosRef](CNCAPosRef-CNCBPosRef.md) — 逐段路径位置（每段重置）
- [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) — 路径位置每周期的变化量（路径速度）
- [CNCBCumPosRef](CNCBCumPosRef.md) — 第二 CNC 组上的相同累计坐标
- [CNCAAbsTrgt/CNCBAbsTrgt](CNCAAbsTrgt-CNCBAbsTrgt.md) — 段完成时加入总量的当前活动段长度
- [VEncSrc](../../03-encoder/06-virtual-encoder/VEncSrc.md) — 选择变量（例如该累计路径位置）作为虚拟编码器的来源
