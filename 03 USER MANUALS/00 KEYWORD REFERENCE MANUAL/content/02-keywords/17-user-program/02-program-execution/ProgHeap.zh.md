---
keyword: ProgHeap
summary: 控制器级易失性读写 int32 数组，为用户程序与通信提供共享存储。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 1021
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 51
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
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# ProgHeap

控制器级易失性读写 `int32` 数组，为用户程序与通信提供共享存储。

## 概述

`ProgHeap` 是一个控制器级读写 `int32` 数组，提供可供用户程序和通信双方访问的共享存储。可在任意时刻通过通信访问，便于与运行中的用户程序交换数值。该参数为非轴参数，不保存至闪存，因此为易失性：其内容在重新上电后不保留（默认值为 `0`）。

## 工作原理

`ProgHeap` 是整个控制器的单一共享存储区域，而非每线程结构——不同于每线程调用栈（[ProgCallStack](ProgCallStack.md)）和数值栈（[ProgExpStack](ProgExpStack.md)）。用户程序与通信双方访问相同的元素，因此可用于在两者之间传递数值。

该数组为 1-indexed：第一个可用元素为 `ProgHeap[1]`，共 50 个可用元素（索引 0 为保留，以便通信索引从 1 开始）。每个元素为 32 位有符号整数，取值范围为 -2147483648 至 2147483647。由于不保存至闪存，该数组为易失性，每次上电后从 `0` 开始。如需在重新上电后保留数据，请改用通用数据数组（参见 [GenData](../../20-arrays/GenData.md)）。

## 示例

```text
AProgHeap[1]        ; read the first element
AProgHeap[1]=0      ; write the first element
```

## 另请参阅

- [GenData](../../20-arrays/GenData.md) — 保存至闪存的通用共享存储
- [ProgResetAll](ProgResetAll.md) — 停止所有线程并重置指针和调用栈
- [ProgStatAll](ProgStatAll.md) — 所有线程的综合状态
