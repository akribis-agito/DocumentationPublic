---
keyword: RemoteCANAdd
summary: RemoteCANSend 发起的远程写入所针对的目标 CAN 节点地址。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 440
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
  - 0
  - 2047
  default: 128
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# RemoteCANAdd

RemoteCANSend 发起的远程写入所针对的目标 CAN 节点地址。

## 概述

`RemoteCANAdd` 指定 [RemoteCANSend](RemoteCANSend.md) 事务所针对的远程控制器的 CAN 节点地址。它是描述一次远程访问的三个寄存器之一：`RemoteCANAdd`（哪个节点）、[RemoteCANCCC](RemoteCANCCC.md)（哪个参数）以及 [RemoteCANVal](RemoteCANVal.md)（值）。它会保存至闪存。有效范围为完整的 11 位 CAN 标识符空间（0–2047）；默认值为 128。

## 工作原理

当 `RemoteCANSend` 运行时，控制器会根据 `RemoteCANAdd` 配置其远程访问 CAN 邮箱：

- 它向 `RemoteCANAdd` 中的地址**发送**请求，并且
- 它在 `RemoteCANAdd + 1` 处**接收**远程节点的应答。

这种 +0 / +1 的请求/应答配对，与控制器自身用于其 [CANAddr](CANAddr.md) 的接收/应答布局一致，因此 `RemoteCANAdd` 应设为远程节点的*基准*接收地址。

## 示例

```text
ARemoteCANAdd=128    ; address of the remote node to access
```

## 另请参阅

- [RemoteCANCCC](RemoteCANCCC.md) — 要访问的编码参数（CAN 命令码）
- [RemoteCANVal](RemoteCANVal.md) — 写入的值，或读取时返回的值
- [RemoteCANSend](RemoteCANSend.md) — 执行远程访问
- [CANAddr](CANAddr.md) — 本控制器自身的 CAN 地址
