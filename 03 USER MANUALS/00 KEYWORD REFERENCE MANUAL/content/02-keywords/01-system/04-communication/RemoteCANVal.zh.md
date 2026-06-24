---
keyword: RemoteCANVal
summary: 在 RemoteCANSend 时写入远程控制器参数的值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 442
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# RemoteCANVal

在 RemoteCANSend 时写入远程控制器参数的值。

## 概述

`RemoteCANVal` 是远程 CAN 访问的数据寄存器。其作用取决于 [RemoteCANSend](RemoteCANSend.md) 所请求的访问类型：

- 在**写**（赋值）操作中，它提供写入由 [RemoteCANCCC](RemoteCANCCC.md) 标识的远程参数的值。
- 在**读**（查询）操作中，固件用远程节点返回的值将其覆盖，因此访问完成后可从 `RemoteCANVal` 读回结果。

它是一个瞬态寄存器，**不会**保存至闪存。默认值为 -1。

## 工作原理

对于写操作，请在调用 `RemoteCANSend` 之前设置 `RemoteCANVal`；固件会将其打包进发出的 CAN 帧。对于读操作，其先前的内容无关紧要——当应答到达时，固件会解码返回的值并存放于此。如果远程节点返回的是错误而非正常应答，则 `RemoteCANVal` 收到的是返回的错误码，而非参数值。

## 示例

```text
ARemoteCANVal=5000   ; value to send on a write access
ARemoteCANVal        ; after a read access, holds the value returned by the remote node
```

## 另请参阅

- [RemoteCANAdd](RemoteCANAdd.md) — 目标节点地址
- [RemoteCANCCC](RemoteCANCCC.md) — 待访问的已编码参数
- [RemoteCANSend](RemoteCANSend.md) — 执行远程访问（写 / 读 / 函数）
