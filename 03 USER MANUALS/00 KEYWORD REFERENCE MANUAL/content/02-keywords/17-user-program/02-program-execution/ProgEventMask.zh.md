---
keyword: ProgEventMask
summary: 应用于事件触发参数与触发值的位掩码。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 521
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 6
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 4294967295
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
    default: null
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# ProgEventMask

应用于事件触发参数与触发值的位掩码。

## 概述

`ProgEventMask` 定义一个位掩码，在比较前应用于被监控的事件参数（[ProgEventPar](ProgEventPar.md)）（索引 `[1]`–`[5]`，每个事件对应一个）。只有源值中被掩码选中的位才参与 [ProgEventType](ProgEventType.md) 所选条件的比较。这使得可以针对特定状态位而非整个字来触发事件。它是一个非轴数组参数，保存至闪存。

## 工作原理

对于整数触发源，控制器计算 `(source AND mask)`，并使用所选条件与触发阈值进行比较。掩码仅应用于*源值*；阈值本身不重新进行掩码处理，因此请将 [ProgEventVal](ProgEventVal.md) 设置为掩码后的源值应匹配的数值。比较为有符号比较。只有掩码中设置为 `1` 的位才参与比较：

- 若要监视单个状态位，只需在掩码中设置该位，并将 [ProgEventVal](ProgEventVal.md) 设置为期望的掩码后值（例如，掩码 `0x0001` 配合值 `0x0001` 在使用"等于"条件时，当第 0 位置位时触发）。
- 对于沿触发条件（[ProgEventType](ProgEventType.md) `5`/`6`），源值的前一次读取在比较前同样会被掩码处理，因此边沿检测仅针对掩码选中的位。

掩码对整数触发源有意义。浮点触发源直接进行比较，不应用掩码。该值以宽位模式存储，因此支持全字宽的掩码（不同版本的位宽差异见下方版本说明）。默认值为不掩码（所有位置 1），因此除非缩窄掩码范围，否则源值的每一位都参与比较。

## 版本间变更

在 v4（独立版和 Central-i v4）上，掩码存储为 32 位有符号整数；[ProgEventVal](ProgEventVal.md) 同样如此。在 Central-i v5 上，`ProgEventMask` 和 `ProgEventVal` 均扩展为 64 位有符号整数，因此可以对 64 位状态字（例如宽位图）进行全宽掩码和比较。

## 示例

```text
AProgEventMask[1]=0x0001   ; only bit 0 of the trigger parameter is tested for event 1
AProgEventMask[1]=0xFFFFFFFF ; test the whole 32-bit word (no masking effect)
```

## 另请参阅

- [ProgEventPar](ProgEventPar.md) — 触发事件的参数
- [ProgEventVal](ProgEventVal.md) — 用于触发检测的值
- [ProgEventType](ProgEventType.md) — 触发类型（沿、等于、不等于……）
