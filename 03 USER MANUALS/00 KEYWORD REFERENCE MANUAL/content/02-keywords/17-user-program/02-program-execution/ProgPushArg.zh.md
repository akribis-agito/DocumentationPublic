---
keyword: ProgPushArg
summary: 将一个值压入目标用户程序任务的参数栈。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 431
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
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
---
# ProgPushArg

将一个值压入目标用户程序任务的参数栈。

## 概述

`ProgPushArg` 将一个值压入运行中线程的调用栈，以便将其作为即将发生的函数调用的参数进行暂存。在 [ProgFuncCall](ProgFuncCall.md) 之前每发出一次 `ProgPushArg`，都会成为被调用函数通过 [ProgArgThis](ProgArgThis.md) 读取的一个输入参数。这是一个非轴指令，不保存至闪存。

## 工作原理

参数通过调用栈传递，而非专用寄存器。要携参数调用函数，需先压入参数，再进行调用：

1. 每次 `ProgPushArg` 将一个值压入当前线程的调用栈，并将该槽位标记为参数或局部变量。栈必须有空闲槽位，否则指令将因栈满错误而失败。
2. 后续的 [ProgFuncCall](ProgFuncCall.md) 将返回地址和帧位置压入已暂存参数的*上方*，因此参数最终位于新帧的正下方。
3. 在函数内部，[ProgArgThis](ProgArgThis.md) 相对于帧读取这些槽位：最后压入的值变为 `ProgArgThis[1]`，之前压入的值变为 `ProgArgThis[2]`，以此类推。

`ProgPushArg` 暂存一个整数。浮点数、64 位整数和双精度值使用相应的变体关键字以相同方式暂存；无论类型如何，值均作为函数的参数存储。每个线程的调用栈最多可容纳 100 个条目；通过 [ProgCallDepth](ProgCallDepth.md) 监控剩余空闲空间。

## 示例

```text
AProgPushArg=10     ; stage 10 — becomes ProgArgThis[2] in the callee
AProgPushArg=20     ; stage 20 — becomes ProgArgThis[1] in the callee
AProgFuncCall,1     ; call function 1 with the two staged arguments
```

## 另请参阅

- [ProgFuncCall](ProgFuncCall.md) — 使用已暂存的参数调用函数
- [ProgArgThis](ProgArgThis.md) — 在被调用函数内读取参数
- [ProgArg](ProgArg.md) — 从函数外部读取线程的参数槽位
- [ProgCallDepth](ProgCallDepth.md) — 调用栈中剩余的空闲空间
