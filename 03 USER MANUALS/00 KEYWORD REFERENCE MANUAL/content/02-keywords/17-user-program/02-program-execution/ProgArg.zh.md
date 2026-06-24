---
keyword: ProgArg
summary: 传递给索引用户程序任务的参数值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 439
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 9
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 20
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range:
    - 0
    - 26
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ProgArg

传递给索引用户程序任务的参数值。

## 概述

`ProgArg` 从*外部*读取某线程当前执行函数的参数——以线程号为索引，以实参位置作为指令值。[ProgArgThis](ProgArgThis.md) 允许函数读取自身的参数，而 `ProgArg` 则允许上位机或其他上下文检查任意线程的当前参数，因此适用于监控和调试。它是非轴参数，不保存至闪存。

## 工作原理

`ProgArg[thread], position` 针对指定线程的当前调用栈帧进行解析，并返回给定实参位置处的值，编号规则与 [ProgArgThis](ProgArgThis.md) 相同：位置 `1` 是调用前最后一个通过 [ProgPushArg](ProgPushArg.md) 压入的值，位置 `2` 是其前一个，依此类推。有效位置范围为 `0`–`20`（Central-i v5 为 `0`–`26`），覆盖函数的参数与局部变量空间；位置 `1` 是第一个（最后压入的）参数，而位置 `0` 指向帧引用/返回槽，而非用户提供的参数。

由于读取的是所选线程的*当前*帧，返回值反映该线程在查询时刻正在执行的函数。若请求的位置超出线程当前帧范围，将引发"调用栈中无操作数"错误。

## 示例

```text
AProgArg[1],1       ; 读取线程 1 当前执行函数的实参位置 1
AProgArg[3],2       ; 读取线程 3 当前执行函数的实参位置 2
```

## 另请参阅

- [ProgArgThis](ProgArgThis.md) — 函数读取自身参数
- [ProgPushArg](ProgPushArg.md) — 调用前暂存参数
- [ProgCallStack](ProgCallStack.md) — 每个线程的完整调用栈内容
