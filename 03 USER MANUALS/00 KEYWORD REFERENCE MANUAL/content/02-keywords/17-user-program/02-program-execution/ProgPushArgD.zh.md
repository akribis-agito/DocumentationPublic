---
keyword: ProgPushArgD
summary: 将一个 64 位浮点（双精度）值压入运行中线程的参数栈，以备函数调用使用。
language: zh-CN
availability:
  standalone: []
  central-i:
  - v5
can_code: 784
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
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# ProgPushArgD

将一个 64 位浮点（双精度）值压入运行中线程的参数栈，以备函数调用使用。

## 概述

`ProgPushArgD` 是 [ProgPushArg](ProgPushArg.md) 的双精度浮点形式。它将一个 64 位浮点（双精度）值压入运行中线程的调用栈，以便将其作为即将发生的函数调用的参数进行暂存。在 [ProgFuncCall](ProgFuncCall.md) 之前每发出一次 `ProgPushArgD`，都会成为被调用函数通过 [ProgArgThisD](ProgArgThisD.md) 读取的一个输入参数。这是一个非轴指令，不保存至闪存。

此关键字从 v5（central-i）起可用。

## 工作原理

参数通过调用栈传递，而非专用寄存器。要携参数调用函数，需先压入参数，再进行调用：

1. 每次 `ProgPushArgD` 将一个值压入当前线程的调用栈，并将该槽位标记为参数或局部变量。栈必须有空闲槽位，否则指令将因栈满错误而失败。
2. 后续的 [ProgFuncCall](ProgFuncCall.md) 将返回地址和帧位置压入已暂存参数的*上方*，因此参数最终位于新帧的正下方。
3. 在函数内部，[ProgArgThisD](ProgArgThisD.md) 相对于帧读取这些槽位：最后压入的值变为 `ProgArgThisD[1]`，之前压入的值变为 `ProgArgThisD[2]`，以此类推。

与 [ProgPushArg](ProgPushArg.md) 的唯一区别在于压入的数据类型：`ProgPushArgD` 暂存一个 64 位浮点（双精度）值，而非 32 位整数。调用栈槽位相同；类型化形式仅控制值的存储方式，以便被调用方可通过匹配的变体以全精度读取。与基础关键字一样，`ProgPushArgD` 仅在运行中的用户程序内有效；从普通通信指令发出将被拒绝。每个线程的调用栈最多可容纳 100 个条目；通过 [ProgCallDepth](ProgCallDepth.md) 监控剩余空闲空间。

## 示例

```text
AProgPushArgD=1.5   ; stage 1.5 — becomes ProgArgThisD[2] in the callee
AProgPushArgD=2.5   ; stage 2.5 — becomes ProgArgThisD[1] in the callee
AProgFuncCall,1     ; call function 1 with the two staged arguments
```

## 另请参阅

- [ProgPushArg](ProgPushArg.md) — 基础（32 位整数）形式
- [ProgPushArgF](ProgPushArgF.md) — 32 位浮点形式
- [ProgPushArgLL](ProgPushArgLL.md) — 64 位整数形式
- [ProgArgThisD](ProgArgThisD.md) — 在被调用函数内读取双精度参数
- [ProgFuncCall](ProgFuncCall.md) — 使用已暂存的参数调用函数
