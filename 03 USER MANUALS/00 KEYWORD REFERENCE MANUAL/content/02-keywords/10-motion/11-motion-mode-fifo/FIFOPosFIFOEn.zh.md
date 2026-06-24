---
keyword: FIFOPosFIFOEn
summary: 使能或禁用 FIFO 位置跟踪模式。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 665
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# FIFOPosFIFOEn

使能或禁用 FIFO 位置跟踪模式。

## 概述

`FIFOPosFIFOEn` 控制向位置跟踪轨迹供给数据的队列的开启或关闭。当轴以位置跟踪模式运行时，工作目标（[FIFOPosTrgt](FIFOPosTrgt.md)）是控制器每个周期进行插值的目标值。此关键字控制工作目标的来源：

- `1` — 队列激活。在每个周期开始时，控制器从位置队列中弹出最旧的目标并将其作为新的工作目标。这是正常的流式传输模式：上位机通过 [FIFOPosPush](FIFOPosPush.md) 压入一系列目标，控制器依次回放。
- `0` — 队列旁路。控制器不从队列中弹出数据，直接使用 [FIFOPosTrgt](FIFOPosTrgt.md) 中当前的值。上位机可在每个周期直接写入 `FIFOPosTrgt` 来驱动轴。

该参数保存至闪存，轴在运动中时不能修改。

## 工作原理

位置跟踪始终以固定周期运行，周期长度（以伺服采样数表示）由 [FIFOPosCycle](FIFOPosCycle.md) 设定。在每个周期的第一个采样：

1. 若 `FIFOPosFIFOEn` 为 `1` 且队列非空，则移除并复制最旧的已排队目标至工作目标。若队列为空，则保持前一个工作目标（轴保持最后一个指令位置，而非结束运动）。
2. 为新周期设置 [FIFOPosType](FIFOPosType.md) 选定的插值规则。

在周期余下的采样中，位置参考向工作目标插值，并叠加位置偏置 [FIFOPosPosOf](FIFOPosPosOf.md)；速度偏置 [FIFOPosVelOf](FIFOPosVelOf.md) 叠加至速度参考，电流偏置 [FIFOPosCurrOf](FIFOPosCurrOf.md) 叠加至电流参考。结果始终受软件位置限位钳位，且轴在触及正向或反向限位开关时仍会减速等待。

与主 FIFO 模式（参见 [FIFOType](FIFOType.md)）在队列耗尽时自动结束运动不同，位置跟踪在队列为空时不会自动终止——它保持最后一个目标。使用 [Stop](../04-motion-command/Stop.md) 使轴减速停止。

## 示例

```text
AFIFOPosFIFOEn=1     ; 从队列流式传输目标
AFIFOPosFIFOEn=0     ; 跟随每个周期直接写入的 FIFOPosTrgt
```

## 另请参阅

- [FIFOPosType](FIFOPosType.md) — 插值模式
- [FIFOPosPush](FIFOPosPush.md) — 压入位置目标
- [FIFOPosTrgt](FIFOPosTrgt.md) — 工作目标
- [FIFOPosCycle](FIFOPosCycle.md) — 每目标采样数（周期长度）
- [FIFOPosStatus](FIFOPosStatus.md) — 队列状态
