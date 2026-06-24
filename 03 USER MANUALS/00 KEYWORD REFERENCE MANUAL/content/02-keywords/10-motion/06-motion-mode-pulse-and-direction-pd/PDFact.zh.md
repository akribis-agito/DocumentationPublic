---
keyword: PDFact
summary: 在累积至 PDPos 之前，应用于检测到的脉冲的缩放系数的分子。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 110
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
  - -16777215
  - 16777215
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# PDFact

在累积至 PDPos 之前，应用于检测到的脉冲的缩放系数的分子。

## 概述

`PDFact` 是缩放系数的分子，该系数应用于检测到的脉冲数，然后进行符号修正并累积至内部计数器 [PDPos](PDPos.md)。它与分母 [PDFactDen](PDFactDen.md) 共同构成有理数比例 `PDFact / PDFactDen`，将输入脉冲计数转换为 `PDPos` 增量。这样，解码后的脉冲方向指令便可匹配所需的轴分辨率。

`PDFact` 为负值时，会反转累积方向。在 Central-i v5 上，方向也可以通过 [PDEncDir](PDEncDir.md) 单独反转；在独立控制器和 Central-i v4 上，`PDEncDir` 无效，因此累积符号仅由脉冲计数器方向和 `PDFact` 的符号决定。

## 工作原理

每个控制器周期内，累积至 [PDPos](PDPos.md) 的增量为：

```text
PDPos increment = (pulses this cycle) × PDFact / PDFactDen
```

在 Central-i v5 上，当 [PDEncDir](PDEncDir.md) 为 1 时，累积增量将被取反（为 0 时保持不变）；在其他版本上，`PDEncDir` 未实现，无任何效果。

**计数不会因舍入而丢失。** 由于 `PDFact/PDFactDen` 通常为小数，缩放后会产生余数；控制器将该余数带入下一个周期。因此随时间推移，累积的 `PDPos` 将精确匹配有理数缩放比例而不产生漂移——正是为了能精确跟踪该余数，`PDFact` 和 `PDFactDen` 才以独立整数的形式分别保存（而非合并为一个值）。

取值范围为 ±16,777,215。`PDFact` 为**负值**时，会反转累积方向。在 Central-i v5 上，这与 [PDEncDir](PDEncDir.md) 的反转相互独立，因此两者可叠加（两者均为负时恢复为正常方向）；在其他版本上，`PDEncDir` 无效。

### 计算示例

步进主站发送每转 10 000 个脉冲；从轴配置为每转 4 000 个 PDPos 计数。所需缩放比例为 `4000 / 10000 = 2 / 5`。设 `PDFact = 2`，`PDFactDen = 5`。若主站以 50 kHz 的速率发送脉冲，则 `PDPos` 以 `50000 × 2/5 = 20000` 计数/秒的速率推进，恰好等于从轴的标称进给速率，且由于每个脉冲的 `2/5` 小数余数在每个周期都会被保留，因此不存在长期漂移。

## 示例

将缩放设置为每 4 个输入脉冲使 `PDPos` 前进 1 个计数，设 `PDFact = 1`，`PDFactDen = 4`：

```text
APDFact=1            ; numerator: 1 PDPos count
APDFactDen=4         ; denominator: per 4 input pulses
APDFact=1000         ; default numerator (with default PDFactDen=1000, ratio = 1)
APDFact             ; read the current numerator
```

## 另请参阅

- [PDFactDen](PDFactDen.md) — 缩放系数的分母
- [PDPos](PDPos.md) — 缩放结果累积至的计数器
- [PDEncDir](PDEncDir.md) — 累积方向反转（仅限 Central-i v5），与 `PDFact` 符号共同作用
