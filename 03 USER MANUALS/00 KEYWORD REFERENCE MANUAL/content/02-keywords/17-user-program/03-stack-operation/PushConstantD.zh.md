---
keyword: PushConstantD
summary: 将 64 位浮点（double）常量压入当前线程的数值栈。
availability:
  standalone: []
  central-i:
  - v5
can_code: 782
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: float64
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range: null
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# PushConstantD

将 64 位浮点（double）常量压入当前线程的数值栈。

## 概述

`PushConstantD` 是 [PushConstant](PushConstant.md) 的双精度浮点形式。它将 64 位浮点（double）常量值压入当前用户程序线程的数值栈。与基础关键字类似，它是 [PushParam](PushParam.md)（将参数值压栈）的常量字面量对应指令，压入的值通常由 [Math](../02-program-execution/Math.md) 操作、[Compare](../02-program-execution/Compare.md) 或 [PopParam](PopParam.md) 消费。通常用户无需手动生成此代码——PC Suite 用户程序 IDE 在编译时自动产生。该关键字为非轴指令，不保存至闪存。

该关键字从 v5（central-i）起可用。

## 工作原理

`PushConstantD` 将指令所携带的字面值放置到当前线程数值栈的栈顶，使栈深度增加一项。不涉及参数查找、轴解析或单位缩放——值按原样使用。向已满的栈压入值将报告栈满错误。

与 [PushConstant](PushConstant.md) 的唯一区别在于压入的数据类型：`PushConstantD` 压入的是 64 位浮点（double）字面量，而非 32 位整数常量。栈槽相同；各类型形式仅控制值的存储方式，以便在消费时正确解释。64 位值与 32 位值一样，仍占用线程 50 个栈槽中的一个，即计为一项栈满限制。

## 示例

```text
APushConstantD=3.14159  ; push the double constant 3.14159 onto the numeric stack
```

## 另请参阅

- [PushConstant](PushConstant.md) — 基础形式（32 位整数）
- [PushConstantF](PushConstantF.md) — 32 位浮点形式
- [PushConstLL](PushConstLL.md) — 64 位整数形式
- [PushParam](PushParam.md) — 将参数值压入数值栈
- [PopParam](PopParam.md) — 将栈顶值弹出至参数
