---
keyword: EncAbsWData
summary: 在写入事务中要写入绝对式编码器寄存器的数据值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 717
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
    can_code: 900
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# EncAbsWData

在写入事务中要写入绝对式编码器寄存器的数据值。

## 概述

`EncAbsWData` 保存在通过 [EncAbsSendCmd](EncAbsSendCmd.md) 发起的写入事务中要写入绝对式编码器寄存器的字节。在调用 `EncAbsSendCmd`（[EncAbsWRType](EncAbsWRType.md) 设为 1，即写入）之前载入它。有效范围为 0 到 255（8 位）。它是轴相关参数，不保存至闪存，且在电机使能或运动中无法更改。适用于 v4（独立式与 central-i）和 v5（central-i）；两个版本的 CAN 代码不同（参见[版本间的变化](#版本间的变化)）。

## 工作原理

在写入事务中，`EncAbsSendCmd` 在设置 [EncAbsAddr](EncAbsAddr.md) 后，将 `EncAbsWData` 写入编码器接口的写数据寄存器，然后发出编码器“写入存储器”命令。在读取事务（[EncAbsWRType](EncAbsWRType.md) = 0）中它被忽略。该值是发送至被寻址编码器寄存器的数据字节。

## 版本间的变化

| | v4（独立式与 central-i） | v5（central-i） |
|---|---|---|
| CAN 代码 | 717 | 900 |

取值范围、默认值以及电机使能/运动中的限制在两个版本中相同。**v5 仅适用于 central-i。** 使用该值的事务仅在独立式控制器上执行：在 central-i 主控上，v5 会拒绝 [EncAbsSendCmd](EncAbsSendCmd.md)；v4 的事务无法到达编码器，并且会更改远程驱动器中无关的设置（参见 [EncAbsSendCmd](EncAbsSendCmd.md)）。

## 示例

```text
AEncAbsWData=200     ; value to write to the addressed register
AEncAbsWData         ; query the staged write value
```

## 另请参阅

- [EncAbsAddr](EncAbsAddr.md) — 写入的寄存器地址
- [EncAbsWRType](EncAbsWRType.md) — 选择读或写访问
- [EncAbsRData](EncAbsRData.md) — 读取事务中读回的数据
- [EncAbsSendCmd](EncAbsSendCmd.md) — 发起事务
- [EncType](../01-general-settings/EncType-AuxEncType.md) — 编码器类型；此接口适用于串行绝对式编码器
