---
keyword: EncAbsRData
summary: 从绝对式编码器寄存器读取事务中返回的数据。
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 718
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 255
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# EncAbsRData

从绝对式编码器寄存器读取事务中返回的数据。

## 概述

`EncAbsRData` 包含由 [EncAbsSendCmd](EncAbsSendCmd.md) 触发的绝对式编码器寄存器读取事务所返回的字节。读取成功后，由 [EncAbsAddr](EncAbsAddr.md) 寻址的编码器寄存器的值可在此处获取。该值为 8 位（0 到 255）。它是只读、轴相关参数，不保存至闪存。仅适用于 v4 固件。

## 工作原理

在读取事务中，`EncAbsSendCmd` 等待编码器响应，从编码器接口的读数据寄存器中读取返回的字节，对其进行位反转（编码器以 LSB 优先方式传输），并将结果存入 `EncAbsRData`。它仅由读取操作（[EncAbsWRType](EncAbsWRType.md) = 0）更新；写入事务不会改变它。请在 `EncAbsSendCmd` 报告完成后读取它。

## 示例

```text
AEncAbsRData        ; read the result of the last register read
```

## 另请参阅

- [EncAbsAddr](EncAbsAddr.md) — 已读取的寄存器地址
- [EncAbsWRType](EncAbsWRType.md) — 选择读或写访问
- [EncAbsWData](EncAbsWData.md) — 要写入被寻址寄存器的数据
- [EncAbsSendCmd](EncAbsSendCmd.md) — 发起事务
- [EncType](../01-general-settings/EncType-AuxEncType.md) — 编码器类型；此接口适用于串行绝对式编码器
