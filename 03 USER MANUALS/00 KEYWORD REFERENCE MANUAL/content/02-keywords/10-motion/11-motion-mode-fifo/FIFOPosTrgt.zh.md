---
keyword: FIFOPosTrgt
summary: 下一个 FIFO 位置段所携带的目标位置。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 661
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
# FIFOPosTrgt

下一个 FIFO 位置段所携带的目标位置。

## 概述

`FIFOPosTrgt` 是位置跟踪子系统的工作位置目标——控制器当前插值朝向的绝对位置，以位置计数表示，不保存至闪存，可在任意时刻更改，包括运动过程中。

`FIFOPosTrgt` 的作用取决于队列是否处于活动状态（参见 [FIFOPosFIFOEn](FIFOPosFIFOEn.md)）：

- **队列活动**（`AFIFOPosFIFOEn=1`）：每个周期开始时，控制器以从队列弹出的最旧目标覆盖 `FIFOPosTrgt`。读取时显示轴当前正在跟踪的目标。
- **队列旁路**（`AFIFOPosFIFOEn=0`）：控制器不覆盖该值。上位机通过每个周期直接写入 `FIFOPosTrgt` 来驱动轴，控制器对每个新值进行插值跟踪。

当轴进入位置跟踪模式时，`FIFOPosTrgt` 初始化为当前位置参考，使跟踪从当前位置平滑开始，同时三个位置跟踪偏置 [FIFOPosPosOf](FIFOPosPosOf.md)、[FIFOPosVelOf](FIFOPosVelOf.md) 和 [FIFOPosCurrOf](FIFOPosCurrOf.md) 均复位为 0。

## 工作原理

目标值被解释为绝对位置。在作为运动参考应用之前，会叠加 [FIFOPosPosOf](FIFOPosPosOf.md)，因此实际指令位置为目标值加上该偏置。相邻目标之间的插值方式由 [FIFOPosType](FIFOPosType.md) 控制，生成的参考值受软件位置限位的钳位。

## 示例

```text
AFIFOPosTrgt=100000  ; set the working target (used by the next push, or tracked directly)
```

## 另请参阅

- [FIFOPosPush](FIFOPosPush.md) — 将目标压入队列
- [FIFOPosFIFOEn](FIFOPosFIFOEn.md) — 使能队列流式传输
- [FIFOPosPosOf](FIFOPosPosOf.md) — 全局位置偏置
- [FIFOPosStatus](FIFOPosStatus.md) — 队列状态
