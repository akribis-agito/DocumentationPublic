---
keyword: ProgClrExp
summary: 清空当前线程的数值（表达式）栈。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 203
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 10
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# ProgClrExp

清空当前线程的数值（表达式）栈。

## 概述

`ProgClrExp` 是一个以线程为索引的底层用户程序关键字，用于清空数值（表达式）栈。建议在新程序开始时执行 `ProgClrExp`，以确保 [PushParam](../03-stack-operation/PushParam.md)、[PushConstant](../03-stack-operation/PushConstant.md) 或 [Math](Math.md) 操作遗留在栈上的过期值被清除。它是 [ProgClrCall](ProgClrCall.md) 的表达式栈对应版本——后者清空程序调用栈。它是一个非轴指令，不保存至闪存。

## 工作原理

数值栈是求值表达式的场所：[PushParam](../03-stack-operation/PushParam.md) 和 [PushConstant](../03-stack-operation/PushConstant.md) 等关键字将操作数压栈，[Math](Math.md) 弹出操作数并将结果压栈，[PopParam](../03-stack-operation/PopParam.md) 将最终值从栈中弹出至参数。每个线程有一个此类栈，最多可容纳 50 个值。

`ProgClrExp[thread]` 一步清空该栈，将其标记为无已占用位置。它不会改变已弹出至参数的任何值；仅丢弃仍在栈上的操作数。这是在程序开始时执行的干净初始化操作，可防止上次运行遗留的操作数污染第一个表达式——例如，某个表达式结束时未匹配 `PopParam`，或序列执行到一半被中断。

## 示例

```text
AProgClrExp[1]      ; clear the numeric stack of thread 1 at program start
```

## 另请参阅

- [ProgExpStack](ProgExpStack.md) — 读取数值栈上的值而不弹出
- [ProgExpDepth](ProgExpDepth.md) — 数值栈中剩余的空闲空间
- [PopParam](../03-stack-operation/PopParam.md) — 将栈顶值弹出至参数
- [ProgClrCall](ProgClrCall.md) — 清空程序调用栈
