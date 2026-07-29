---
keyword: ExtCurrCmdOfs
summary: 每相偏置（mA），在缩放为数字 SPI 驱动器的 DAC 代码之前加到相电流指令上。
availability:
  standalone: []
  central-i:
  - v5
can_code: 867
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -4000.0
  - 4000.0
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-07-30'
doc_revision: '2026.07'
language: zh-CN
---
# ExtCurrCmdOfs

每相偏置（mA），在缩放为数字 SPI 驱动器的 DAC 代码之前加到相电流指令上。

## 概述

`ExtCurrCmdOfs` 仅在轴由**数字 SPI 外部驱动器**（[AmpType](../../02-motor-and-amplifier/AmpType.md) `= 8`）驱动时才有意义——在其他任何 `AmpType` 下（包括内置 PWM 级）均无效。它是加到该外部驱动器相电流指令上的每相偏置，单位为毫安。数组按 1 起始索引：`[1]` = Ia，`[2]` = Ib；索引 `0` 保留、不使用。

它是保存至闪存的轴相关参数。该值为浮点偏置，可用范围为 -4000.0 至 4000.0 mA，默认值为 0。使用它来抵消外部驱动器自身模拟/DAC 级中每通道的零电流偏差——即原本需要在驱动器本身上手动调整的那个微调量。

## 工作原理

该偏置在数字 SPI 增益**之前**被加到相电流指令上，而不是之后加到最终的 DAC 代码上。该增益由 [AAmpFullScale](../../02-motor-and-amplifier/AAmpFullScale.md) 设定（`增益 = 32768 / AAmpFullScale`，单位为 counts/mA；该数字 SPI 模式下的推导见该页）。每个控制周期，对相索引 `i`：

```
codeBeforeMidCode = round( gain × (PhaseCurr[i] + ExtCurrCmdOfs[i]) )
ExtCurrCmdVal[i]  = codeBeforeMidCode + 32768                          ; saturated to 0…65535
```

其中 `32768` 为 DAC 的中间码，代表 0 mA。所得代码由 [ExtCurrCmdVal](ExtCurrCmdVal.md) 报告，即实际发送给驱动器的值。

![External-amplifier DAC command chain, per phase: the phase current command in mA has ExtCurrCmdOfs added to it in mA, then the sum is multiplied by the gain 32768 over AAmpFullScale in counts per mA, then 32768 (the DAC mid-code for zero current) is added, then the result is saturated to 0 through 65535. The final value is ExtCurrCmdVal, the DAC code sent to the amplifier. The offset is applied before the gain, in the same mA domain as the phase current, not after the gain as a raw count.](extcurrcmd-dac-chain.svg)

由于偏置是在 mA 域中施加的，它对 DAC 代码的影响会随该轴的增益而变化。例如，当 `AAmpFullScale` 给出的增益为 8.0 counts/mA、相电流指令为 1000 mA 时：

- `ExtCurrCmdOfs[1] = 0`：代码 = round(8.0 × 1000) + 32768 = 40768
- `ExtCurrCmdOfs[1] = 250`：代码 = round(8.0 × (1000 + 250)) + 32768 = 42768

250 mA 的偏置恰好使 DAC 代码移动 2000 个计数（250 × 8.0）。这正是它与"增益之后施加的原始计数偏置"的关键区别：同一个 `ExtCurrCmdOfs` 值在不同轴上会按该轴的 `AAmpFullScale` 比例产生不同的代码偏移，这也正是它能够以物理电流单位（而非取决于增益设置的计数）来调整的原因。

> 仅适用于 Central-i v5，且仅当轴配置为数字 SPI 驱动器（[AmpType](../../02-motor-and-amplifier/AmpType.md) `= 8`）时。

## 示例

```text
AExtCurrCmdOfs[1]=250     ; add 250 mA to the Ia command before the gain
AExtCurrCmdOfs[2]=-100    ; add -100 mA to the Ib command before the gain
AExtCurrCmdOfs[1]         ; read the configured Ia offset
```

## 另请参阅

- [ExtCurrCmdVal](ExtCurrCmdVal.md) —— 该偏置最终进入的 DAC 代码
- [AAmpFullScale](../../02-motor-and-amplifier/AAmpFullScale.md) —— 在该偏置之后施加的增益
- [AmpType](../../02-motor-and-amplifier/AmpType.md) —— 选择本关键字所适用的数字 SPI 驱动器模式（8）
- [ExtCurrFBSca](ExtCurrFBSca.md) —— 对应外部电流反馈路径的缩放
- [ComtStatus](../../15-commutation/ComtStatus.md) —— 状态 `-17`，轴配置为外部驱动器时的定相拒绝
