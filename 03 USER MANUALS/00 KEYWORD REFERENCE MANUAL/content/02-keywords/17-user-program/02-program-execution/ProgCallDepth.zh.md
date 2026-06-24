---
keyword: ProgCallDepth
summary: 报告线程程序调用栈中剩余的空闲空间。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 277
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 9
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# ProgCallDepth

报告线程程序调用栈中剩余的空闲空间。

## 概述

`ProgCallDepth` 是一个以线程为索引的只读数组参数，报告指定线程的程序调用栈中剩余的空槽（空闲槽）数量。它与 [ProgCallStack](ProgCallStack.md) 互补——后者暴露调用栈内容——适用于诊断深度嵌套的函数调用（参见 [ProgFuncCall](ProgFuncCall.md)）。它是一个非轴状态变量，不保存至闪存。

## 工作原理

每个线程的调用栈固定容量为 100 个槽。`ProgCallDepth` 返回*空闲*槽数——即容量减去当前已使用的槽数——因此刚清空的调用栈（参见 [ProgClrCall](ProgClrCall.md)）报告值为 100，随着调用嵌套加深，该值逐渐减小。

每次 [ProgFuncCall](ProgFuncCall.md) 至少消耗两个槽（返回地址加帧引用），通过 [ProgPushArg](ProgPushArg.md) 暂存的每个参数额外消耗一个槽；匹配的 [Return](Return.md) 释放这些槽。监视此值是确认递归或深度嵌套调用序列是否接近上限的方法——超出上限将导致栈溢出错误。

## 示例

```text
AProgCallDepth[1]   ; free call-stack slots for thread 1 (100 when empty)
```

## 另请参阅

- [ProgCallStack](ProgCallStack.md) — 每个线程的程序调用栈内容
- [ProgFuncCall](ProgFuncCall.md) — 调用用户程序函数
- [ProgPushArg](ProgPushArg.md) — 暂存参数（消耗一个调用栈槽）
- [ProgClrCall](ProgClrCall.md) — 清空程序调用栈
