---
keyword: Return
summary: 从用户程序函数调用返回，继续执行调用之后的行。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 432
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 7
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 10
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range:
    - 0
    - 16
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# Return

从用户程序函数调用返回，继续执行调用之后的行。

## 概述

`Return` 使用户程序从通过 [ProgFuncCall](ProgFuncCall.md) 发起的函数调用中返回，继续执行调用之后的下一行。它从程序调用栈（[ProgCallStack](ProgCallStack.md)）中弹出最近的一帧，也用于完成事件处理函数——执行后该事件可再次被触发（参见 [ProgEventStat](ProgEventStat.md)）。

`Return` 还可以返回值。其写法为 `AReturn[N], M`，其中**值** `M` 是函数接收的*输入*参数数量，**数组索引** `N` 以 `N − 1` 编码*输出*参数数量（即 `AReturn[1]` 无输出，`AReturn[2]` 返回 1 个输出，`AReturn[3]` 返回 2 个输出，依此类推）。输出值本身不在此处给出——函数在此行之前已通过 [ProgArgThis](ProgArgThis.md) 将输出值写入对应的输出参数槽；`Return` 随后将这些槽推入调用方的数值栈。输入参数数量的支持范围为 `0`–`10`，在 central-i v5 上扩展至 `0`–`16`。

> **注意：** 若程序不是无限循环，应在程序末尾使用 [ProgHalt](ProgHalt.md)。否则执行将延续至第一个函数，`Return` 关键字将导致错误。

## 工作原理

`Return` 执行时作用于当前线程的调用栈。指令值为函数接收的*输入*参数数量；数组索引减一为要返回的*输出*参数数量（输出值应已提前通过 [ProgArgThis](ProgArgThis.md) 写入函数的输出参数槽）。引擎随后执行以下步骤：

1. 检查调用栈非空——若无可返回目标则 `Return` 报错。同时检查栈中确实包含所声明数量的输入参数、输出参数、返回地址和帧位置，并确认数值（表达式）栈有足够空间存放输出值。
2. 弹出*返回地址*，从发起 [ProgFuncCall](ProgFuncCall.md) 的行的下一行继续执行。
3. 将函数的输出参数推入数值（表达式）栈，调用方可通过栈操作关键字读取。每个输出值占用一个数值栈位置。
4. 恢复调用方的帧位置，并从调用栈中丢弃整个帧（输入参数、输出参数、返回地址和帧位置）。

若正在弹出的帧是作为程序事件处理程序进入的（而非普通调用），`Return` 将重新置位该事件，使其可再次触发（参见 [ProgEventStat](ProgEventStat.md)）；事件处理程序的 `Return` 必须声明无输入或输出参数。

两种常见错误：调用栈为空时调用 `Return`（例如执行流进入函数时——参见 [ProgFunc](ProgFunc.md)），以及声明的输出参数数量超出数值栈可用空间。

## 示例

```text
AProgFuncCall,1     ; 调用函数 1
...
AProgFunc[1]        ; 标签：函数 1 的起始位置
; 函数主体
AReturn[1],0        ; 返回调用之后的行（无输入或输出参数）

; 接收 2 个输入参数并返回 2 个输出值的函数末尾
; （输出值在此行之前已通过 ProgArgThis 写入函数的输出参数槽）：
AReturn[3],2        ; 数组索引 3 => 2 个输出参数；值 2 => 2 个输入参数
```

## 另请参阅

- [ProgFuncCall](ProgFuncCall.md) — 调用函数
- [ProgFunc](ProgFunc.md) — 标记函数起始位置的标签
- [ProgArgThis](ProgArgThis.md) — 在函数内部读取参数
- [ProgCallStack](ProgCallStack.md) — 程序调用栈内容
- [ProgHalt](ProgHalt.md) — 停止线程（置于函数定义之前）
