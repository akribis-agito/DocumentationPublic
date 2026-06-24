---
keyword: PDFactDen
summary: 在累积至 PDPos 之前，应用于检测到的脉冲的缩放系数的分母。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 119
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 16777215
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# PDFactDen

在累积至 PDPos 之前，应用于检测到的脉冲的缩放系数的分母。

## 概述

`PDFactDen` 是缩放系数的分母，该系数应用于检测到的脉冲数，然后进行符号修正并累积至内部计数器 [PDPos](PDPos.md)。它与分子 [PDFact](PDFact.md) 共同构成有理数比例 `PDFact / PDFactDen`，将输入脉冲计数转换为 `PDPos` 增量，使解码后的脉冲方向指令能够匹配所需的轴分辨率。最小值为 `1`（不允许除以零）。

## 工作原理

每个控制器周期内，累积至 [PDPos](PDPos.md) 的增量为：

```text
PDPos increment = (pulses this cycle) × PDFact / PDFactDen
```

在 Central-i v5 上，当 [PDEncDir](PDEncDir.md) 为 1 时，累积增量将被取反；在其他版本上，`PDEncDir` 未实现，无任何效果。

最小值为 `1`（比例在 0 时未定义），最大值为 16,777,215。由于每个周期的除法余数会被保留，即使 `PDFact/PDFactDen` 为非整数比例，累积至 `PDPos` 的结果也是精确的，不会产生漂移——详见 [PDFact](PDFact.md)。

## 示例

```text
APDFactDen=4         ; 4 input pulses per PDFact numerator
APDFactDen=1000      ; default denominator (with default PDFact=1000, ratio = 1)
APDFactDen          ; read the current denominator
```

## 另请参阅

- [PDFact](PDFact.md) — 缩放系数的分子（以及精确余数机制）
- [PDPos](PDPos.md) — 缩放结果累积至的计数器
- [PDEncDir](PDEncDir.md) — 累积方向反转（仅限 Central-i v5）
