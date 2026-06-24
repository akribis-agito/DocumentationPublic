---
keyword: RemoteCANCCC
summary: 由 RemoteCANSend 发起的远程写操作所使用的 CAN 命令码（参数标识符）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 441
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 2
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# RemoteCANCCC

由 RemoteCANSend 发起的远程写操作所使用的 CAN 命令码（参数标识符）。

## 概述

`RemoteCANCCC` 保存的是 **Complex CAN Code**（CCC，复合 CAN 码），用于标识 [RemoteCANSend](RemoteCANSend.md) 事务作用于远程控制器上的*哪一个*参数。它不只是一个单纯的 CAN 码：它将目标关键字的 CAN 码与其所适用的轴一并编码，对于数组关键字还包含数组索引。它与 [RemoteCANAdd](RemoteCANAdd.md)（节点）和 [RemoteCANVal](RemoteCANVal.md)（值）共同构成一次完整的远程访问。它会保存至闪存。

## 工作原理

当 `RemoteCANSend` 运行时，控制器将 `RemoteCANCCC` 分解为各组成部分——参数的 CAN 码、所寻址的轴以及数组索引——并将它们打包进发出的 CAN 帧中。这正是为什么单个整数即可寻址远程节点上的任意参数，包括某个数组关键字的特定元素以及特定的轴。

该 32 位值被拆分为三个字段（bit 15 未使用）：

| Bits | 字段 | 范围 | 含义 |
|---|---|---|---|
| 0–9 | CAN code | 0–1023 | 远程关键字的 CAN 码 |
| 10–14 | Axis | 0–31 | 轴号，基于 0（axis A = 0，axis B = 1，……） |
| 16–31 | Array index | 0–65535 | 数组关键字基于 1 的元素；标量关键字为 0 |

因此该值为：

$$\texttt{RemoteCANCCC} = (\text{index} \times 65536) + (\text{axis} \times 1024) + \text{CAN code}$$

数组索引字段遵循控制器自身的校验规则：数组关键字必须以 1 或更大的索引寻址（索引 0 会被拒绝），标量关键字必须使用索引 0（任何大于 0 的索引都会被拒绝）。默认值为 2。

例如，要寻址 axis A（axis = 0）上某个数组关键字的第 3 个元素，且其 CAN 码为 100：

$$(3 \times 65536) + (0 \times 1024) + 100 = 196708$$

## 示例

```text
ARemoteCANCCC=100    ; encoded identifier of the remote parameter to access
```

## 参见

- [RemoteCANAdd](RemoteCANAdd.md) — 目标节点地址
- [RemoteCANVal](RemoteCANVal.md) — 写入的值，或读操作返回的值
- [RemoteCANSend](RemoteCANSend.md) — 执行远程访问
