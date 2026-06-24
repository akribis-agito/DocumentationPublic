---
keyword: PushConstant
summary: 将常量值压入当前线程的数值栈。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 201
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
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# PushConstant

将常量值压入当前线程的数值栈。

## 概述

`PushConstant` 是一个底层用户程序关键字，用于将常量值压入当前用户程序线程的数值栈。它是 [PushParam](PushParam.md)（将参数值压栈）的常量字面量对应指令。压入的值通常由 [Math](../02-program-execution/Math.md) 操作、[Compare](../02-program-execution/Compare.md) 或 [PopParam](PopParam.md) 消费。通常用户无需手动生成此代码——PC Suite 用户程序 IDE 在编译时自动产生。该关键字为非轴指令，不保存至闪存。

## 工作原理

`PushConstant` 将指令所携带的字面值放置到当前线程数值栈的栈顶，使栈深度增加一项。不涉及参数查找、轴解析或单位缩放——值按原样使用。每个线程的数值栈最多可容纳 50 个值；向已满的栈压入值将报告栈满错误。可通过 [ProgExpDepth](../02-program-execution/ProgExpDepth.md) 读取剩余空闲空间。此系列中还有一个用于浮点字面量的配套操作；此处记录的整数形式压入的是 32 位整数常量。

## 示例

```text
APushConstant=5      ; push the constant 5 onto the numeric stack
```

## 另请参阅

- [PushParam](PushParam.md) — 将参数值压入数值栈
- [PopParam](PopParam.md) — 将栈顶值弹出至参数
- [Math](../02-program-execution/Math.md) — 对数值栈上的值执行运算
