---
keyword: CNCBCumPosRef
summary: 自运动开始以来 CNC 组 B 跨所有段的累积指令路径位置。
availability:
  standalone: []
  central-i:
  - v5
can_code: 700
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
# CNCBCumPosRef

自运动开始以来 CNC 组 B 跨所有段的累积指令路径位置。

## 概述

`CNCBCumPosRef` 是**第二** CNC 组（组 B）的只读 64 位累积路径坐标。它是独立 CNC 组 A 上 [CNCACumPosRef](CNCACumPosRef.md) 的精确对应关键字：报告自当前组 B CNC 运动开始以来沿 CNC 路径的**总指令行进距离**——所有已完成段的长度之和，加上当前正在执行段内的路径位置。

[CNCBPosRef](CNCAPosRef-CNCBPosRef.md) 在每个段开始时重置为零，而 `CNCBCumPosRef` 则跨段边界持续累加，为组 B 上的整个已编程路径提供一个连续递增的坐标。这便于进度跟踪，也便于以路径位置（而非某一个成员轴的位置）驱动下游功能（例如虚拟编码器或基于位置的事件）。

仅在 central-i（v5）上可用。

## 工作原理

CNC 模式每个控制周期推进一个标量路径位置（参见 [CNCBPosRef](CNCAPosRef-CNCBPosRef.md)）。控制器维护所有已完成组 B 段的长度累计；每个周期报告：

```text
CNCBCumPosRef = (sum of completed-segment lengths) + (current CNCBPosRef)
```

- 当组 B CNC 运动启动时，`CNCBCumPosRef` 和已完成段总计均**重置为 0**。
- 随着路径在段内推进，`CNCBCumPosRef` 与 [CNCBPosRef](CNCAPosRef-CNCBPosRef.md) 同步上升。
- 当一个段完成时，其完整长度被加入已完成段总计，而 [CNCBPosRef](CNCAPosRef-CNCBPosRef.md) 为下一段从零重新开始，因此 `CNCBCumPosRef` 在转角处平滑地持续上升，不发生跳变。

该值是指令**路径**坐标（驱动组 B 所有成员轴的主坐标），而非任何单个轴的位置。其每周期变化量即为 [CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) 报告的路径速度。

`CNCBCumPosRef` 可被选作虚拟编码器的来源。若正在以该方式使用，且 CNC 来源被重置（新运动启动），则正在仿真该坐标的虚拟编码器会自动关闭，以免跟踪刚跳回零的坐标。

## 示例

```text
ACNCBCumPosRef       ; read the total commanded path distance on group B
ACNCACumPosRef       ; read the total commanded path distance on group A
```

## 另请参阅

- [CNCACumPosRef](CNCACumPosRef.md) — 第一 CNC 组上的相同累积坐标
- [CNCAPosRef/CNCBPosRef](CNCAPosRef-CNCBPosRef.md) — 每段路径位置（每段重置）
- [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) — 路径位置的每周期变化量（路径速度）
- [CNCAAbsTrgt/CNCBAbsTrgt](CNCAAbsTrgt-CNCBAbsTrgt.md) — 段完成时加入总计的当前段长度
- [VEncSrc](../../03-encoder/06-virtual-encoder/VEncSrc.md) — 选择一个变量（例如本累积路径位置）作为虚拟编码器的来源
