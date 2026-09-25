---
keyword: EncAbsAddr
summary: 绝对式编码器内部的寄存器地址，供下一次事务访问。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 716
attributes:
  access: rw
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
overrides:
  central-i.v5:
    can_code: 899
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# EncAbsAddr

绝对式编码器内部的寄存器地址，供下一次事务访问。

## 概述

`EncAbsAddr` 指定绝对式编码器内部、供下一次 [EncAbsSendCmd](EncAbsSendCmd.md) 事务访问的存储地址。它与 [EncAbsWRType](EncAbsWRType.md)（读或写）配合使用，以指向正确的编码器寄存器。有效范围为 0 到 255（8 位）。它是轴相关参数，不保存至闪存，且不能在电机使能或运动中更改。适用于 v4（独立式与 central-i）和 v5（central-i）；两个版本的 CAN 代码不同（参见[版本间的变化](#版本间的变化)）。

## 工作原理

当 [EncAbsSendCmd](EncAbsSendCmd.md) 运行时，它会在发出读或写命令之前，将 `EncAbsAddr` 写入编码器接口的存储地址寄存器。因此该地址选择后续事务所针对的编码器寄存器；它自身不产生任何作用。请将其与 [EncAbsWRType](EncAbsWRType.md)（对于写入，还需 [EncAbsWData](EncAbsWData.md)）一同设置，然后发出 `EncAbsSendCmd`。

## 版本间的变化

| | v4（独立式与 central-i） | v5（central-i） |
|---|---|---|
| CAN 代码 | 716 | 899 |

取值范围、默认值以及电机使能/运动中的限制在两个版本中相同。**v5 仅适用于 central-i。** 使用该值的事务仅在独立式控制器上执行：在 central-i 主控上，v5 会拒绝 [EncAbsSendCmd](EncAbsSendCmd.md)，v4 的事务则无法到达编码器。

## 示例

```text
AEncAbsAddr=16       ; target register address 16
AEncAbsAddr          ; query the configured address
```

## 另请参阅

- [EncAbsWRType](EncAbsWRType.md) — 选择读或写访问
- [EncAbsWData](EncAbsWData.md) — 要写入所寻址寄存器的数据
- [EncAbsRData](EncAbsRData.md) — 从所寻址寄存器读回的数据
- [EncAbsSendCmd](EncAbsSendCmd.md) — 发出事务
- [EncType](../01-general-settings/EncType-AuxEncType.md) — 编码器类型；此接口适用于串行绝对式编码器
