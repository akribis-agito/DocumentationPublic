---
keyword: PushParam
summary: 将参数的值压入当前线程的数值栈。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 200
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# PushParam

将参数的值压入当前线程的数值栈。

## 概述

`PushParam` 是一个底层用户程序关键字，用于将参数的值压入当前用户程序线程的数值栈。参数由一个编码引用标识，该引用指定了要读取的关键字、轴及数组索引。它是 [PushConstant](PushConstant.md) 的参数值对应指令，也是 [PopParam](PopParam.md) 的逆操作；压入的值通常由 [Math](../02-program-execution/Math.md) 操作消费。通常用户无需手动生成该引用——PC Suite 用户程序 IDE 在编译时自动产生。该关键字为非轴指令，不保存至闪存。

## 工作原理

每个线程拥有独立的数值（表达式）栈。`PushParam` 读取指定参数并将其值放置到该线程栈顶，使栈深度增加一项。在 Central-I v5 上，栈是带类型的，因此压入的值保留参数的数据类型（32 位整数、64 位整数、32 位浮点或 64 位 double）。在 v4 上，栈存储 32 位整数，值以 32 位整数形式放置。

以下几点行为值得注意：

- **轴解析。** 当引用未指定特定轴时，轴取自线程的 [ChooseAxis](../02-program-execution/ChooseAxis.md) 条目，因此同一指令可跟随线程当前操作的轴。
- **间接（计算）数组索引。** 若引用指向数组但未指定索引，`PushParam` 会先从栈中弹出一个值并将其用作数组索引。这允许程序计算索引（例如通过 [Math](../02-program-execution/Math.md)）后读取对应数组元素。
- **单位缩放。** 以用户单位表示的参数在压栈时将转换为用户单位，与通过通信读取该参数的结果一致。
- **限制。** 向已满的栈压入值将报告栈满错误；函数类型的关键字（而非值类型）不可压栈。

## 示例

```text
; Push a parameter's value onto the stack (encoded reference emitted by the compiler)
APushParam=<encoded reference to source parameter>
```

## 另请参阅

- [PushConstant](PushConstant.md) — 将常量压入数值栈
- [PopParam](PopParam.md) — 将栈顶值弹出至参数
- [Math](../02-program-execution/Math.md) — 对数值栈上的值执行运算
