---
keyword: RemoteCANSend
summary: 使用 RemoteCAN* 寄存器向远程节点发送 CAN 写操作的命令。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 443
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 1
  - 3
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# RemoteCANSend

使用 RemoteCAN* 寄存器向远程节点发送 CAN 写操作的命令。

## 概述

`RemoteCANSend` 对远程节点执行单次 CAN 访问，使一台控制器可以作为 CAN 主站面向另一台控制器。它使用事先设置好的三个 RemoteCAN 寄存器：

1. [RemoteCANAdd](RemoteCANAdd.md) — 目标节点的 CAN 地址
2. [RemoteCANCCC](RemoteCANCCC.md) — 待访问的已编码参数（Complex CAN Code）
3. [RemoteCANVal](RemoteCANVal.md) — 待写入的值，或读结果返回的位置

赋给 `RemoteCANSend` 的值用于选择访问类型：

| RemoteCANSend | 访问 | 效果 |
|---|---|---|
| 1 | 赋值（写） | 将 [RemoteCANVal](RemoteCANVal.md) 写入远程参数 |
| 2 | 查询（读） | 读取远程参数；返回的值存回 [RemoteCANVal](RemoteCANVal.md) |
| 3 | 函数 | 将远程参数作为函数/命令执行 |

## 工作原理

`RemoteCANSend` 必须在**用户程序**内部执行——如果直接通过普通通信通道发出则会被拒绝，因为它在等待远程节点期间会阻塞发起的线程。执行时控制器会：

1. 配置其远程访问邮箱，以向 [RemoteCANAdd](RemoteCANAdd.md) 发送，并在 `RemoteCANAdd + 1` 处接收应答。
2. 根据 [RemoteCANCCC](RemoteCANCCC.md)（以及在写操作时的 32 位 [RemoteCANVal](RemoteCANVal.md)）构建请求帧并发送。
3. 分两个阶段等待——先等待帧被发送，再等待远程节点的应答——每个阶段约有 100 ms 的超时。
4. 解析应答：写/函数操作期望收到 "OK" 确认；查询操作期望收到一个值，该值从 32 位应答中解码并写入 [RemoteCANVal](RemoteCANVal.md)。

该事务可能报告以下错误：

| 错误 | 含义 |
|---|---|
| 111 | `RemoteCANSend` 未从用户程序发出（它必须在用户程序内部运行）。 |
| 238 | 远程访问超时——发送或应答未在其约 100 ms 的阶段内完成。 |
| 239 | 远程节点以错误作答；其 16 位错误码被写入 [RemoteCANVal](RemoteCANVal.md)。 |
| 240 | 无法解析应答。 |

它可以在运动期间执行。

> 平台说明：此事务在 standalone/控制器平台上已实现。在 central-i 平台上，远程 CAN 主站事务尚未实现。

## 示例

```text
ARemoteCANAdd=128    ; target node
ARemoteCANCCC=100    ; encoded parameter on the remote node
ARemoteCANVal=5000   ; value (used for a write)
ARemoteCANSend=1     ; perform a write

ARemoteCANSend=2     ; perform a read; afterwards ARemoteCANVal holds the returned value
```

## 另请参阅

- [RemoteCANAdd](RemoteCANAdd.md) — 目标节点地址
- [RemoteCANCCC](RemoteCANCCC.md) — 待访问的已编码参数
- [RemoteCANVal](RemoteCANVal.md) — 写入的值，或读操作返回的值
- [SendToCntrlr](SendToCntrlr.md) — 通过串口将值转发至另一台控制器
