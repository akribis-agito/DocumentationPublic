---
keyword: PushConstLL
summary: 将 64 位有符号整数常量压入当前线程的数值栈。
availability:
  standalone: []
  central-i:
  - v5
can_code: 781
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - -2251799813685248
  - 2251799813685247
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# PushConstLL

将 64 位有符号整数常量压入当前线程的数值栈。

## 概述

`PushConstLL` 是 [PushConstant](PushConstant.md) 的 64 位有符号整数形式。它将一个 64 位有符号整数常量的值压入当前用户程序线程的数值栈。与基础关键字相同，它是 [PushParam](PushParam.md)（压入参数值）的常量字面量对应项，压入的值通常由 [Math](../02-program-execution/Math.md) 运算、[Compare](../02-program-execution/Compare.md) 或 [PopParam](PopParam.md) 消耗。通常用户无需手动生成代码——PC Suite 用户程序 IDE 在编译时会自动生成。该命令属于非轴域命令，不保存至闪存。

该关键字从 v5（central-i）起可用。

## 工作原理

`PushConstLL` 将指令携带的字面值放置于当前线程数值栈的栈顶，使栈增加一个条目。不涉及参数查找、轴解析或单位换算——值按原样使用。向已满的栈压入数据将报告栈满错误。

与 [PushConstant](PushConstant.md) 的唯一区别在于压入的数据类型：`PushConstLL` 压入的是 64 位有符号整数字面量，而非 32 位整数常量。栈槽相同；不同类型的形式仅控制值的存储方式，以便在被消耗时能正确解释。64 位值与 32 位值一样占用一个栈槽，因此同样计为一个条目，受栈满限制约束。

## 示例

```text
APushConstLL=5000000000 ; 将 64 位整数常量 5000000000 压入数值栈
```

## 另请参阅

- [PushConstant](PushConstant.md) — 基础（32 位整数）形式
- [PushConstantF](PushConstantF.md) — 32 位浮点形式
- [PushConstantD](PushConstantD.md) — 64 位浮点（双精度）形式
- [PushParam](PushParam.md) — 将参数值压入数值栈
- [PopParam](PopParam.md) — 将栈顶值弹出并写入参数
