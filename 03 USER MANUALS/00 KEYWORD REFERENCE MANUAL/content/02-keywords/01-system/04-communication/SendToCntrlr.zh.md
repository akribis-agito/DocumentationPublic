---
keyword: SendToCntrlr
summary: 部分实现的函数，用于将参数写操作路由到另一台控制器。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 484
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 1001
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: partial
overrides:
  central-i.v5:
    array_size: 10001
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# SendToCntrlr

部分实现的函数，用于将参数写操作路由到另一台控制器。

## 概述

`SendToCntrlr` 通过串口（RJ45）将本控制器 [GenData](../../20-arrays/GenData.md) 数组中的某个值转发到另一台控制器的 `GenData` 数组。它被标记为**部分实现**，因此其行为可能取决于具体的固件版本，且该值的传输是单向的，没有解析应答。

要写入远程节点上的任意参数，[RemoteCAN](RemoteCANSend.md) 组（基于 CAN）是更通用、更直接的机制。

## 工作原理

`SendToCntrlr` 是一个接受两个参数（实参）的函数——一个目标索引和一个源索引——并在串口 B 上发出如下形式的 ASCII 命令：

```text
AGenData[<destination index>] = <value of local GenData[<source index>]>
```

换言之，它读取由源索引指定的本地 [GenData](../../20-arrays/GenData.md) 元素的值，并发送一条命令，将该值写入接在串口上的控制器的 `GenData` 数组中由目标索引指定的元素。该传输固定使用 `GenData` 数组，但目标索引与源索引相互独立——它们不必在两侧引用相同的元素号。由于它发送的是文本命令且不将应答解析回参数，因此最适合在链式配置中将一个工作值推送到下游控制器。

## 示例

```text
ASendToCntrlr[5]=5   ; send local GenData[5] to the remote controller's GenData[5] (destination 5, source 5)
```

## 另请参阅

- [RemoteCANSend](RemoteCANSend.md) — 向远程节点发送单次 CAN 写/读操作（更通用）
- [GenData](../../20-arrays/GenData.md) — 此函数所传输的通用数组
- [RSBaud](RSBaud.md) — 所用串口的波特率
- [CANAddr](CANAddr.md) — CAN 寻址
