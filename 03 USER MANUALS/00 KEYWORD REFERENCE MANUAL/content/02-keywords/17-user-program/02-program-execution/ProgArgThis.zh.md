---
keyword: ProgArgThis
summary: 读回当前正在执行的任务所接收到的参数值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 433
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 21
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    array_size: 27
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ProgArgThis

读回当前正在执行的任务所接收到的参数值。

## 概述

`ProgArgThis` 是一个数组参数，供当前正在执行的函数访问其自身的参数和局部变量。它是调用前通过 [ProgPushArg](ProgPushArg.md) 暂存的值的函数内部视图。`ProgArgThis` 可读可写，因此同一数组也充当函数的局部变量存储。该参数为非轴参数，不保存至闪存。

## 工作原理

函数的参数存储在相对于当前帧的调用栈上。`ProgArgThis[k]` 寻址帧参考位置下方第 `k` 个槽，具体如下：

- `ProgArgThis[1]` 是调用前最后一次通过 [ProgPushArg](ProgPushArg.md) 压入的值。
- `ProgArgThis[2]` 是在其之前压入的值，依此类推，按逆压入顺序向前追溯已暂存的参数。

读取索引返回该槽的值；写入索引则存入该槽，这即是函数保存局部变量以及在 [Return](Return.md) 前准备输出值的方式。索引针对*当前*帧进行解析，因此即使函数嵌套，值也会自动对应正确的函数。

`ProgArgThis` 仅在运行中的用户程序内部有效（它寻址当前调用帧）；从普通通信指令发出此命令将被拒绝并返回运行时错误。

数组覆盖函数的参数与局部变量的组合空间：在 v4 上最多 20 个条目，在 central-i v5 上最多 26 个（为一个函数的输入参数、输出参数与局部变量之和）。读取超出当前帧范围的索引将引发"调用栈中无操作数"错误。

此处展示的整数形式是最常用的；相应的变体关键字以浮点数、64 位整数或双精度浮点数形式读写相同的槽。

## 示例

```text
AProgArgThis[1]     ; read the most-recently-pushed argument of this function
AProgArgThis[2]     ; read the argument pushed before it
AProgArgThis[3]=0   ; use the third slot as a local variable
```

## 另请参阅

- [ProgPushArg](ProgPushArg.md) — 调用前暂存参数
- [ProgFuncCall](ProgFuncCall.md) — 调用函数
- [ProgArg](ProgArg.md) — 从函数外部读取其他线程的参数槽
- [Return](Return.md) — 向调用方返回输出值
