---
keyword: EncAbsWRType
summary: 为下一次绝对式编码器寄存器事务选择读或写访问。
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 715
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# EncAbsWRType

为下一次绝对式编码器寄存器事务选择读或写访问。

## 概述

`EncAbsWRType` 选择由 [EncAbsSendCmd](EncAbsSendCmd.md) 执行的下一次绝对式编码器寄存器事务的方向（读或写）。在发起 `EncAbsSendCmd` 之前设置它，以定义该事务是从 [EncAbsAddr](EncAbsAddr.md) 处的编码器存储器读取还是向其写入。它是轴相关参数，不保存至闪存，且在电机使能或运动中无法更改。仅适用于 v4 固件。

## 工作原理

`EncAbsSendCmd` 根据此值进行分支：

| 值 | 访问 | 效果 |
|---|---|---|
| 0 | 读 | 发送编码器“从存储器读取”命令；返回的字节出现在 [EncAbsRData](EncAbsRData.md) 中。 |
| 1 | 写 | 发送编码器“写入存储器”命令，将 [EncAbsWData](EncAbsWData.md) 写入被寻址的寄存器。 |

该值仅为方向选择器；它本身不触发事务。完整序列请参见 [EncAbsSendCmd](EncAbsSendCmd.md)。

## 示例

```text
AEncAbsWRType=0      ; read access
AEncAbsWRType=1      ; write access
```

## 参见

- [EncAbsAddr](EncAbsAddr.md) — 事务的寄存器地址
- [EncAbsWData](EncAbsWData.md) — 写入事务中要写入的数据
- [EncAbsRData](EncAbsRData.md) — 读取事务中读回的数据
- [EncAbsSendCmd](EncAbsSendCmd.md) — 发起事务
- [EncType](../01-general-settings/EncType-AuxEncType.md) — 编码器类型；此接口适用于串行绝对式编码器
