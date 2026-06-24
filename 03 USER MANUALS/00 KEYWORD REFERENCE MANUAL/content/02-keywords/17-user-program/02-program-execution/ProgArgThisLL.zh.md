---
keyword: ProgArgThisLL
summary: 以 64 位有符号整数形式读写当前函数的参数槽和局部变量槽。
availability:
  standalone: []
  central-i:
  - v5
can_code: 785
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 27
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2251799813685248
  - 2251799813685247
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ProgArgThisLL

以 64 位有符号整数形式读写当前函数的参数槽和局部变量槽。

## 概述

`ProgArgThisLL` 是 [ProgArgThis](ProgArgThis.md) 的 64 位有符号整数形式。它供当前正在执行的函数以 64 位有符号整数形式读写其自身的参数和局部变量。它是调用前通过 [ProgPushArgLL](ProgPushArgLL.md) 暂存的值的函数内部视图。与基础关键字相同，它可读可写，因此同一槽也充当函数的局部变量存储。该参数为非轴参数，不保存至闪存。

本关键字从 v5（central-i）起可用。

## 工作原理

函数的参数存储在相对于当前帧的调用栈上。`ProgArgThisLL[k]` 与 [ProgArgThis](ProgArgThis.md) 相同，寻址帧参考位置下方第 `k` 个槽：

- `ProgArgThisLL[1]` 是调用前最后一次通过 [ProgPushArgLL](ProgPushArgLL.md) 压入的值。
- `ProgArgThisLL[2]` 是在其之前压入的值，依此类推，按逆压入顺序向前追溯已暂存的参数。

与 [ProgArgThis](ProgArgThis.md) 的唯一区别在于数据类型：`ProgArgThisLL` 以 64 位有符号整数而非 32 位整数形式读写槽的值。底层调用栈槽相同——有类型的形式选择对槽中位的解释方式——因此函数应选择与其存储类型匹配的变体。读取索引返回该槽的值；写入索引则存入该槽，这即是函数保存局部变量以及在 [Return](Return.md) 前准备输出值的方式。索引针对*当前*帧进行解析，因此即使函数嵌套，值也会自动对应正确的函数。

与基础关键字一样，`ProgArgThisLL` 仅在运行中的用户程序内部有效（它寻址当前调用帧）；从普通通信指令发出此命令将被拒绝并返回运行时错误。

数组覆盖函数的参数与局部变量的组合空间（为一个函数的输入参数、输出参数与局部变量之和）。读取超出当前帧范围的索引将引发"调用栈中无操作数"错误。

## 示例

```text
AProgArgThisLL[1]   ; read the most-recently-pushed argument of this function as a 64-bit integer
AProgArgThisLL[2]   ; read the argument pushed before it as a 64-bit integer
AProgArgThisLL[3]=0 ; use the third slot as a 64-bit integer local variable
```

## 另请参阅

- [ProgArgThis](ProgArgThis.md) — 基础（32 位整数）形式
- [ProgArgThisF](ProgArgThisF.md) — 32 位浮点数形式
- [ProgArgThisD](ProgArgThisD.md) — 64 位浮点数（double）形式
- [ProgPushArgLL](ProgPushArgLL.md) — 调用前暂存 64 位整数参数
- [ProgArgLL](ProgArgLL.md) — 从函数外部以 64 位整数形式读取其他线程的参数槽
