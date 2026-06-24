---
keyword: PDVel
summary: 只读，经缩放的 P/D 计数器 PDPos 的变化率，单位为 P/D 用户单位每秒。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 7
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: pd_user_units
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
# PDVel

只读，经缩放的 P/D 计数器 PDPos 的变化率，单位为 P/D 用户单位每秒。

## 概述

`PDVel` 是经缩放的脉冲方向计数器 [PDPos](PDPos.md) 的变化率，以脉冲方向用户单位每秒表示。它反映了解码后的 P/D 指令的运动速度，可用于在直接（[MotionMode](../02-motion-configuration/MotionMode.md) = 3）或间接（`MotionMode` = 4）P/D 运动期间监测输入脉冲方向流的速度。

## 工作原理

`PDVel` 并非在事后对 `PDPos` 求导得到，而是直接取自 P/D 解码过程中计算的**每周期经缩放变化量**。该变化量已包含 [PDFact](PDFact.md)/[PDFactDen](PDFactDen.md) 的缩放（包括 `PDFact` 的符号）、输入脉冲/方向流的自然方向以及进位小数余量，因此 `PDVel` 在缩放和流方向上与 `PDPos` 保持一致。但它**不**反映 [PDEncDir](PDEncDir.md) 的反向，该反向仅作用于 `PDPos` 累加器。`PDVel` 是每控制器周期的变化量以速度形式表示的结果。

在直接模式下，该速度还会影响与方向相关的决策（例如限位开关处理和摩擦补偿符号），因此 `PDVel` 反映了瞬时 P/D 指令速率。

从数值上看，`PDVel` 是 `PDPos` 的每周期变化量乘以固定采样率 **16,384 Hz**（经缩放的变化量在约 61 us 的一个周期内取得并换算为每秒值）。因此，当输入脉冲频率较低时，`PDVel` 可能会从一个周期到下一个周期在离散值之间跳变——例如，稳定的每周期一个脉冲（`PDFact/PDFactDen = 1`）读数约为 16,384 单位/s——而非平滑变化。控制器会在周期间保留缩放变化量的小数部分，因此随时间推移，`PDVel` 能分辨出比单周期步长更细的精度，并跟踪真实平均速率。

与 `PDPos` 类似，`PDVel` 是一个内部计数值，通过通信通道查询时会转换为脉冲方向用户单位——参见 [PDUsrUnits](PDUsrUnits.md)。

## 示例

```text
APDVel              ; 读取当前 P/D 指令速度（脉冲方向单位/s）
```

## 参见

- [PDPos](PDPos.md) — `PDVel` 报告其每周期增量的计数器
- [PDUsrUnits](PDUsrUnits.md) — 查询单位转换
- [PDEncDir](PDEncDir.md) — 仅反转 `PDPos` 累加方向，不影响 `PDVel`
