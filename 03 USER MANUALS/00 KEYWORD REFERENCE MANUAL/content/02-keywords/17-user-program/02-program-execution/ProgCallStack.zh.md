---
keyword: ProgCallStack
summary: 用户程序线程的程序调用栈内容。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 276
attributes:
  access: rw
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
  - 99
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# ProgCallStack

用户程序线程的程序调用栈内容。

## 概述

`ProgCallStack` 是一个以线程为索引的数组参数，暴露线程程序调用栈的原始内容——该结构在通过 [ProgFuncCall](ProgFuncCall.md) 调用函数时建立，并由 [Return](Return.md) 展开。每次调用会添加一个帧，其中保存暂存的参数、返回地址和调用方的帧引用。使用 [ProgCallDepth](ProgCallDepth.md) 检查剩余空闲空间，使用 [ProgClrCall](ProgClrCall.md) 清空调用栈。它主要用于调试，是一个非轴参数，不保存至闪存。

## 工作原理

`ProgCallStack[thread], location` 通过绝对位置（从栈底开始计数，非相对于当前帧的相对位置）读取所选线程的一个栈槽。位置从 `0` 到最高已占用槽；每个线程的调用栈最多可容纳 100 个槽。读取操作是非破坏性的——不会改变调用栈。

返回值取决于该槽保存的内容：

- **返回地址** — 以偏移量表示，单位与 [ProgPointer](ProgPointer.md) 相同，从程序起始处计算。这是匹配的 [Return](Return.md) 运行后执行将恢复的行。
- **参数、局部变量或帧引用** — 按原始存储值返回。保存浮点参数的槽以原始位模式返回，由上位机将其解释为浮点数。

读取超出最高已占用槽或超出 `0`–99 范围的位置将引发栈范围错误。

## 示例

```text
AProgCallStack[1],0     ; read the base slot (location 0) of thread 1's call stack
AProgCallStack[1],1     ; read the next slot up
```

## 另请参阅

- [ProgCallDepth](ProgCallDepth.md) — 调用栈中剩余的空闲空间
- [ProgClrCall](ProgClrCall.md) — 清空程序调用栈
- [ProgFuncCall](ProgFuncCall.md) — 调用用户程序函数
- [Return](Return.md) — 从函数调用中返回
- [ProgPointer](ProgPointer.md) — 程序内当前执行偏移量
