---
keyword: VEncModRev
summary: 用于补偿虚拟编码器源回绕的取模范围（每转计数）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 629
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
  - 2000000000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    can_code: 830
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# VEncModRev

用于补偿虚拟编码器源回绕的取模范围（每转计数）。

## 概述

`VEncModRev` 提供补偿源（[VEncSrc](VEncSrc.md)）回绕所用的范围。虚拟编码器生成跟踪该源的正交或脉冲/方向信号；参见 [VEncOn](VEncOn.md)。

它是一个保存至闪存的轴相关参数，可在电机使能（但非运动中）时更改，默认值为 `0`，该值会**禁用**回绕处理。可用范围为 `0` 到 `2,000,000,000`。

## 工作原理

`VEncModRev` 是源在一个完整取模周期内的源计数数量——即源的每转计数。将其设置为与 [VEncSrc](VEncSrc.md) 所指向的任何变量的 [ModRev](../04-modulo-mode/ModRev.md) 范围相匹配。

每个控制周期，生成器将新的源值与前一个值进行比较：

- 如果 `VEncModRev = 0`，则不进行回绕处理；假定源永不翻转。
- 如果 `VEncModRev ≠ 0` 且源在单个周期内的变化超过 `VEncModRev` 的**一半**，生成器会将跟踪存储及 [VEncValue](VEncValue.md) 移动一个经缩放的范围，以补偿回绕。

在包含 [Firmware-Main #1103](https://github.com/akribis-agito/Firmware-Main/issues/1103) 修复的固件中，源步长的容量检查在此补偿之后进行。如果补偿后的步长超过每采样周期的容量，跟踪将从新参考值重新开始，并丢弃该步长。电机使能时，故障 **1066** 仍会触发。参见 [VEncOn](VEncOn.md)。

缩放后的范围由 `VEncModRev` 连同输出缩放 [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) 共同计算得出，因此回绕补偿以与生成输出相同的单位施加。

## 示例

```text
AVEncModRev=0            ; default: source never wraps, no roll-over handling
AVEncModRev=131072       ; compensate source wraps at 131072 counts/rev
AVEncModRev               ; read the configured modulo span
```

## 另请参阅

- [VEncSrc](VEncSrc.md) —— 此参数所描述的取模范围所对应的源变量
- [VEncOn](VEncOn.md) —— 启用虚拟编码器
- [VEncValue](VEncValue.md) —— 虚拟编码器跟踪计数
- [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) —— 源到输出的缩放比值
- [ModRev](../04-modulo-mode/ModRev.md) —— 轴反馈的取模范围（一种典型源）
