---
keyword: ProgArgLL
summary: 从函数外部以 64 位有符号整数形式读取线程当前函数的参数槽。
availability:
  standalone: []
  central-i:
  - v5
can_code: 787
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 9
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 26
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ProgArgLL

从函数外部以 64 位有符号整数形式读取线程当前函数的参数槽。

## 概述

`ProgArgLL` 是 [ProgArg](ProgArg.md) 的 64 位有符号整数形式。它从*外部*读取某线程当前正在执行的函数的参数，将所请求的槽解释为 64 位有符号整数返回。与基础关键字相同，它以线程号为索引，参数位置通过指令值指定，适用于在该槽存储 64 位整数时进行监测和调试。该参数为非轴参数，不保存至闪存。

本关键字从 v5（central-i）起可用。

## 工作原理

`ProgArgLL[thread], position` 对指定线程的当前调用栈帧进行解析，并以与 [ProgArgThis](ProgArgThis.md) 相同的编号方式返回指定参数位置的值：位置 `1` 是调用前最后压入的值，位置 `2` 是在其之前压入的值，依此类推，按逆压入顺序向前追溯已暂存的参数。

与 [ProgArg](ProgArg.md) 的唯一区别在于数据类型：`ProgArgLL` 以 64 位有符号整数而非 32 位整数形式返回槽的值。底层调用栈槽相同；有类型的形式只是让上位机以存储时的类型读回数据。当该槽使用 [ProgPushArgLL](ProgPushArgLL.md) 暂存（或以其他方式存储 64 位整数）时，使用此关键字。

由于它读取所选线程的*当前*帧，返回值反映该线程查询时正在执行的函数的状态。若请求的位置超出线程当前帧的范围，将引发"调用栈中无操作数"错误。

## 示例

```text
AProgArgLL[1],1     ; read argument position 1 of the function running on thread 1 as a 64-bit integer
AProgArgLL[3],2     ; read argument position 2 of the function running on thread 3 as a 64-bit integer
```

## 另请参阅

- [ProgArg](ProgArg.md) — 基础（32 位整数）形式
- [ProgArgF](ProgArgF.md) — 32 位浮点数形式
- [ProgArgD](ProgArgD.md) — 64 位浮点数（double）形式
- [ProgArgThisLL](ProgArgThisLL.md) — 函数内部以 64 位整数形式读取自身参数
- [ProgPushArgLL](ProgPushArgLL.md) — 调用前暂存 64 位整数参数
