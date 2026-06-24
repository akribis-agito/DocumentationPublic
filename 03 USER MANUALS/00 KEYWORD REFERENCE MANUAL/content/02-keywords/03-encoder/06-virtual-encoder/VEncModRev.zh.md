---
keyword: VEncModRev
summary: 虚拟编码器源的取模范围（每转计数），使生成器在源回绕时保持连续。
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

虚拟编码器源的取模范围（每转计数），使生成器在源回绕时保持连续。

## 概述

`VEncModRev` 告知虚拟编码器源信号的取模范围有多大，从而当源（[VEncSrc](VEncSrc.md)）从其范围顶部回绕至零（或反之）时，所生成的输出不会跳变。虚拟编码器是一个编码器**信号生成器**（它发出跟踪某个源变量的正交或脉冲/方向信号），而不是反馈输入；参见 [VEncOn](VEncOn.md)。`VEncModRev` 的存在纯粹是为了在所选源本身以取模方式运行时，保持该生成信号的连续性。

它是一个保存至闪存的轴相关参数，可在电机使能（但非运动中）时更改，默认值为 `0`，该值会**禁用**回绕处理。可用范围为 `0` 到 `2,000,000,000`。

## 工作原理

`VEncModRev` 是源在一个完整取模周期内的源计数数量——即源的每转计数。将其设置为与 [VEncSrc](VEncSrc.md) 所指向的任何变量的 [ModRev](../04-modulo-mode/ModRev.md) 范围相匹配。

每个控制周期，生成器将新的源值与前一个值进行比较：

- 如果 `VEncModRev = 0`，则不进行回绕处理；假定源永不翻转。
- 如果 `VEncModRev ≠ 0` 且源在单个周期内的变化超过 `VEncModRev` 的**一半**，则将该变化视为翻转（而非真实跳变）。生成器将其内部跟踪移动一个完整范围，并将生成的计数 [VEncValue](VEncValue.md) 步进一个范围的缩放等效值，使发出的信号平滑延续，而不会产生大量边沿的突发。

缩放后的范围由 `VEncModRev` 连同输出缩放 [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) 共同计算得出，因此回绕补偿以与生成输出相同的单位施加。

## 示例

```text
AVEncModRev=0            ; default: source never wraps, no roll-over handling
AVEncModRev=131072       ; source runs modulo 131072 counts/rev; keep output continuous on wrap
AVEncModRev               ; read the configured modulo span
```

## 另请参见

- [VEncSrc](VEncSrc.md) — 此参数所描述的取模范围所对应的源变量
- [VEncOn](VEncOn.md) — 使能虚拟编码器
- [VEncValue](VEncValue.md) — 在回绕时保持连续的生成输出计数
- [VEncFact](VEncFact.md) / [VEncFactDen](VEncFactDen.md) — 源到输出的缩放比例
- [ModRev](../04-modulo-mode/ModRev.md) — 轴反馈的取模范围（一种典型源）
