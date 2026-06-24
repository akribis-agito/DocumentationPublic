---
keyword: StallTh
summary: 只读的步进失步检测阈值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 516
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
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# StallTh

只读的步进失步检测阈值。

## 概述

`StallTh` 是只读的、由固件计算的阈值，失步度量 [StallVal](StallVal.md) 会与之比较：当 `StallVal < StallTh` 时即判定为失步。它在每个控制周期重新计算（仅当 [StallCfg](StallCfg.md) 启用检测时），是一个与速度相关的阈值，由 [StallThPcnt](StallThPcnt.md) 缩放，并由 [StallCnst](StallCnst.md) 系数整形。

## 工作原理

该阈值在每个周期由指令速度、百分比 [StallThPcnt](StallThPcnt.md) 以及两个 [StallCnst](StallCnst.md) 系数构建，然后经过低通滤波：

```text
speed = |commanded velocity| >> (StepBits - 2)   ; scaled commanded speed, shifted to avoid overflow

threshold input = (StallThPcnt * speed) * 0.01 * 0.001
                  * (StallCnst[1]*speed + StallCnst[2])
                  - 10000                          ; fixed offset

StallTh = threshold input * 0.005 + 0.995 * previous StallTh   ; same ~13 Hz LPF as StallVal
```

用文字描述：

- `StallCnst[1]·speed + StallCnst[2]` 是**预期度量随速度变化的线性拟合**（斜率和截距）——参见 [StallCnst](StallCnst.md)。这使阈值能够跟踪健康状态下 `StallVal` 随速度增长的预期趋势。
- 该拟合被 `StallThPcnt/100`（即 `× 0.01`）和固定的 `× 0.001` 缩放，因此 `StallThPcnt` 设定预期健康值的*多大比例*被视为“失步”——百分比越低，阈值越低，检测灵敏度也越低。
- 减去固定偏置 `10000` 以减少误触发。
- 结果以与 `StallVal` 相同的 0.005 平滑因子进行滤波，因此阈值与度量在相同的时间尺度上变化。

`StallTh` 为只读，当电机失能时复位为 `0`。

![Stepper stall detection sketch: a healthy StallVal stays well above the StallTh line; when the rotor loses step, StallVal collapses below StallTh and the stall outcome is taken from StallCfg](stall-detect.svg)

## 示例

```text
AStallTh[1]           ; read the live (filtered) stall threshold
```

## 另请参阅

- [StallThPcnt](StallThPcnt.md) — 缩放此阈值的百分比
- [StallCnst](StallCnst.md) — 速度相关拟合的斜率/截距系数
- [StallVal](StallVal.md) — 与此阈值比较的度量
- [StallStat](StallStat.md) — 当 `StallVal < StallTh` 时置位
