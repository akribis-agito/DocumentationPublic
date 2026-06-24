---
keyword: PIVNoiseDtct
summary: 在轴保持静止时，启用对位置/速度环中过度噪声或抖动的运行时检测。
availability:
  standalone: []
  central-i:
  - v5
can_code: 797
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
# PIVNoiseDtct

在轴保持静止时，启用对位置/速度环中过度噪声或抖动的运行时检测。

## 概述

`PIVNoiseDtct` 用于开启或关闭 PIV（位置/速度）噪声检测器。启用后，控制器会监测在轴被指令保持静止期间，位置/速度环产生的电流参考的摆动幅度。在真正静止的情况下，该参考值应当平稳，因此大幅摆动表明存在噪声或抖动经由控制环传入（例如来自噪声较大的反馈信号或过于激进的增益）。若摆动幅度过大，控制器将关闭电机并记录故障。

| 值 | 含义 |
|---|---|
| 0 | 检测器禁用（默认）。 |
| 1 | 检测器启用。 |

此关键字仅在 v5（central-i）中可用。

## 工作原理

在检测器启用且电机使能期间，控制器计算电流参考在滑动窗口内的方差，窗口长度由 [PIVNoiseWSize](PIVNoiseWSize.md) 设置。测量仅在轴处于指令静止状态时进行：位置参考必须保持不变，且不得有信号注入激活。检测器会等待轴持续静止时间超过一个窗口长度（约一个半窗口长度）后，再对统计量采取动作，从而确保窗口内仅包含静止数据，正常运动不会引发误触发。

当方差超过 [PIVNoiseSTD](PIVNoiseSTD.md) 设定的阈值（峰值电流限值 [PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md) 的百分比）时，控制器将关闭电机并记录故障码 1072（检测到高噪声/抖动），该故障码在 [ConFlt](../../07-status-and-faults/ConFlt.md) 中上报。

启用检测器在电机使能时生效，此时统计窗口和静止计数器将被清零。将关键字写回 0 将立即禁用检测。由于检测器可随时开启或关闭，此关键字可在轴运动中及电机使能时写入。实时统计量和当前阈值可从 [PIVNoiseStat](PIVNoiseStat.md) 读取。

## 示例

```text
APIVNoiseWSize=30     ; 30 ms statistics window
APIVNoiseSTD=2        ; threshold 2% of peak current limit
APIVNoiseDtct=1       ; enable the PIV noise detector
APIVNoiseDtct[1]      ; read back the enable state
```

## 另请参阅

- [PIVNoiseSTD](PIVNoiseSTD.md) — PIV 噪声方差阈值
- [PIVNoiseWSize](PIVNoiseWSize.md) — 统计窗口大小
- [PIVNoiseStat](PIVNoiseStat.md) — PIV 噪声检测器状态数组
- [ConFlt](../../07-status-and-faults/ConFlt.md) — 控制器故障码（检测到时为 1072）
- [PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md) — 阈值所基准的峰值电流限值
