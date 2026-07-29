---
keyword: ExtCurrCmdVal
summary: 只读数组，报告实际发送给数字 SPI 外部驱动器的每相 DAC 代码。
availability:
  standalone: []
  central-i:
  - v5
can_code: 868
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -1
  - 65536
  default: 32768
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-07-30'
doc_revision: '2026.07'
language: zh-CN
---
# ExtCurrCmdVal

只读数组，报告实际发送给数字 SPI 外部驱动器的每相 DAC 代码。

## 概述

`ExtCurrCmdVal` 仅在轴由**数字 SPI 外部驱动器**（[AmpType](../../02-motor-and-amplifier/AmpType.md) `= 8`）驱动时才带有实时值——在其他任何 `AmpType` 下均不使用。它是只读的每相数组，以原始计数报告控制器实际发送给驱动器的 DAC 代码。数组按 1 起始索引：`[1]` = Ia，`[2]` = Ib；索引 `0` 保留、不使用。

它是一个诊断量，而非控制量：由于是只读且不保存至闪存，可在任意时刻读取，其存在纯粹是为了让集成方确认控制器实际发送了什么——例如当驱动器自身的微调存疑时。对其写入会被以只读错误拒绝。

## 工作原理

每个控制周期，对相索引 `i`，控制器计算

```
codeBeforeMidCode = round( gain × (PhaseCurr[i] + ExtCurrCmdOfs[i]) )
ExtCurrCmdVal[i]  = codeBeforeMidCode + 32768                          ; saturated to 0…65535
```

其中 `gain = 32768 / AAmpFullScale`（counts/mA），`32768` 为 DAC 的中间码（相电流和偏置均为零时对应 0 mA）。完整的"先偏置、后增益"推导及算例见 [ExtCurrCmdOfs](ExtCurrCmdOfs.md)。

`ExtCurrCmdVal` 会饱和：若计算出的代码超出 DAC 的 0–65535 范围，会被钳位到最近的一端，而不会回绕。该值就是实际写入驱动器 SPI/DAC 寄存器的值，因此即使未钳位的计算结果本可以更大，它也如实反映了发生的钳位。

> 仅适用于 Central-i v5，且仅当轴配置为数字 SPI 驱动器（[AmpType](../../02-motor-and-amplifier/AmpType.md) `= 8`）时。

## 示例

```text
AExtCurrCmdVal[1]       ; read the DAC code currently sent for Ia
AExtCurrCmdVal[2]       ; read the DAC code currently sent for Ib
AExtCurrCmdVal[1]=100   ; rejected: ExtCurrCmdVal is read-only
```

## 另请参阅

- [ExtCurrCmdOfs](ExtCurrCmdOfs.md) —— 进入该代码的每相 mA 偏置，含完整指令链与算例
- [AAmpFullScale](../../02-motor-and-amplifier/AAmpFullScale.md) —— 在偏置与该代码之间施加的增益
- [AmpType](../../02-motor-and-amplifier/AmpType.md) —— 选择本关键字所适用的数字 SPI 驱动器模式（8）
- [ComtStatus](../../15-commutation/ComtStatus.md) —— 状态 `-17`，轴配置为外部驱动器时的定相拒绝
