---
keyword: ProgArgD
summary: 从函数外部以 64 位浮点数（double）形式读取线程当前函数的参数槽。
availability:
  standalone: []
  central-i:
  - v5
can_code: 788
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 9
  data_type: float64
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
# ProgArgD

从函数外部以 64 位浮点数（double）形式读取线程当前函数的参数槽。

## 概述

`ProgArgD` 是 [ProgArg](ProgArg.md) 的双精度浮点数形式。它从*外部*读取某线程当前执行函数的参数，将请求的槽位以 64 位浮点数（double）形式返回。与基础关键字相同，以线程号为索引，以实参位置作为指令值，适用于当该槽位值为 double 时的监控和调试场景。它是非轴参数，不保存至闪存。

本关键字从 v5（Central-i）起可用。

## 工作原理

`ProgArgD[thread], position` 针对指定线程的当前调用栈帧进行解析，并返回给定实参位置处的值，编号规则与 [ProgArgThis](ProgArgThis.md) 相同：位置 `1` 是调用前最后一个压入的值，位置 `2` 是其前一个，依此类推，按压入顺序的逆序计数。

与 [ProgArg](ProgArg.md) 的唯一区别在于数据类型：`ProgArgD` 以 64 位浮点数（double）形式返回槽位值，而非 32 位整数。底层调用栈槽位相同；带类型的形式仅允许上位机以存储时的类型读回数据。当槽位通过 [ProgPushArgD](ProgPushArgD.md) 暂存（或以其他方式保存 double 值）时，使用本关键字。

由于读取的是所选线程的*当前*帧，返回值反映该线程在查询时刻正在执行的函数。若请求的位置超出线程当前帧范围，将引发"调用栈中无操作数"错误。

## 示例

```text
AProgArgD[1],1      ; 以 double 形式读取线程 1 当前执行函数的实参位置 1
AProgArgD[3],2      ; 以 double 形式读取线程 3 当前执行函数的实参位置 2
```

## 另请参阅

- [ProgArg](ProgArg.md) — 基础（32 位整数）形式
- [ProgArgF](ProgArgF.md) — 32 位浮点数形式
- [ProgArgLL](ProgArgLL.md) — 64 位整数形式
- [ProgArgThisD](ProgArgThisD.md) — 函数以 double 形式读取自身参数
- [ProgPushArgD](ProgPushArgD.md) — 调用前暂存 double 参数
