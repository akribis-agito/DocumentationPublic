---
keyword: FIFOPosCycle
summary: 连续 FIFO 位置段之间的周期时间，以伺服采样数表示。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 660
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
  - 1
  - 1600
  default: 16
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# FIFOPosCycle

连续 FIFO 位置段之间的周期时间，以伺服采样数表示。

## 概述

`FIFOPosCycle` 设置位置跟踪轨迹的周期长度（以伺服采样数表示）：控制器每个周期取一个新的位置目标，并在两个目标之间的采样上进行插值。因此，它决定了流式目标的时间间距——即 [FIFOPosFIFOEn](FIFOPosFIFOEn.md) 使能的轨迹的回放速率。

该值以控制环采样数给出。控制环以固定采样频率运行（通常为 16384 Hz），因此 N 个采样的周期对应 N / 16384 秒。以默认值 16 个采样为例，每约 1 ms 消耗一个新目标。

范围为 1 至 1600 个采样（默认 16）。该参数保存至闪存，轴在运动中时不能修改。

## 工作原理

在每个周期的第一个采样，控制器从队列中弹出下一个目标（若队列为空则保持最后一个目标），并准备 [FIFOPosType](FIFOPosType.md) 设定的插值方式。在周期余下的采样中，位置参考平滑地向该目标推进：

- `FIFOPosCycle` 较大时，目标在时间上间隔较远，各点之间运动较慢，每点插值采样数更多。
- 较小时，目标回放更快，每点插值采样数更少。

上位机在流式传输目标时，必须以与所选周期长度相匹配的速率压入目标；否则队列耗尽，轴将保持最后一个目标。可通过 [FIFOPosStatus](FIFOPosStatus.md) 监控队列占用情况。

例如，`FIFOPosCycle = 164`（在 16 384 Hz 下约为 10 ms），上位机每秒应压入约 100 个目标以保持轨迹流畅流式传输；若速率落后导致队列耗尽，轴将简单地保持最后一个已消耗的目标，直到新目标到达。

## 示例

```text
AFIFOPosCycle=16     ; 每 16 个采样消耗一个目标（16384 Hz 下约 1 ms）
AFIFOPosCycle=164    ; 每约 10 ms 消耗一个目标
```

## 另请参阅

- [FIFOPosType](FIFOPosType.md) — 插值模式
- [FIFOPosPush](FIFOPosPush.md) — 压入位置目标
- [FIFOPosFIFOEn](FIFOPosFIFOEn.md) — 使能 FIFO 位置跟踪
- [FIFOPosStatus](FIFOPosStatus.md) — 队列状态
