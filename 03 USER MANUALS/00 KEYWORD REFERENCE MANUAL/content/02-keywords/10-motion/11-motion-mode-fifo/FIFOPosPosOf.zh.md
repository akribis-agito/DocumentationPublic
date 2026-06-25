---
keyword: FIFOPosPosOf
summary: 叠加到每个 FIFO 位置段上的位置偏置。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 662
attributes:
  access: rw
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
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# FIFOPosPosOf

叠加到每个 FIFO 位置段上的位置偏置。

## 概述

`FIFOPosPosOf` 是一个以位置计数为单位的常量位置偏置，在每个流式目标成为轴位置参考之前叠加其上。它在不改变已排队目标或 [FIFOPosTrgt](FIFOPosTrgt.md) 的情况下，整体平移整条位置跟踪轨迹。它是三个位置跟踪偏置中的位置分量，另外两个分别是速度偏置 [FIFOPosVelOf](FIFOPosVelOf.md) 和电流偏置 [FIFOPosCurrOf](FIFOPosCurrOf.md)。该参数不保存至闪存，可在任意时刻更改，包括运动过程中。

## 工作原理

在每个采样周期，插值目标（当前工作目标与下一目标之间的插值结果）与 `FIFOPosPosOf` 相加，形成指令位置参考：

```text
position reference = interpolated target + FIFOPosPosOf
```

求和结果随后受软件位置限位的钳位。由于偏置在插值之后施加，修改它会均匀地平移整条路径；阶跃变化会在参考值上产生阶跃，因此若轴正在跟踪，请逐渐调整。该偏置仅影响位置参考，与速度前馈偏置和电流前馈偏置相互独立。

常见用途是在固定的流式曲线基础上叠加实时修正量（例如来自外部传感器或主轴的修正）。

当轴进入位置跟踪模式时，`FIFOPosPosOf` 将被复位为 0（与 [FIFOPosVelOf](FIFOPosVelOf.md) 和 [FIFOPosCurrOf](FIFOPosCurrOf.md) 一同复位），因此每次运行均从无位置偏置开始。若需要非零偏移，请在模式进入后重新设置。

## 示例

```text
AFIFOPosPosOf=5000   ; shift the whole position trajectory by 5000 counts
AFIFOPosPosOf=0      ; remove the offset
```

## 另请参阅

- [FIFOPosTrgt](FIFOPosTrgt.md) — 工作目标位置
- [FIFOPosVelOf](FIFOPosVelOf.md) — 速度前馈偏置
- [FIFOPosCurrOf](FIFOPosCurrOf.md) — 电流前馈偏置
- [PosRef](../01-kinematics-status/PosRef.md) — 输出的位置参考
