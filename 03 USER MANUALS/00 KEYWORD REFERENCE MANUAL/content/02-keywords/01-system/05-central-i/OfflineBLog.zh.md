---
keyword: OfflineBLog
summary: 在离线邮箱 2 上记录的所有 Central-i 离线（邮箱）事务的滚动日志。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 621
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 46
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
# OfflineBLog

在离线邮箱 2 上记录的所有 Central-i 离线（邮箱）事务的滚动日志。

## 概述

`OfflineBLog` 是一个非轴数组，用于在**离线邮箱 2** 上记录最近的 Central-i **离线**（邮箱）事务。这是固件实际填充的日志，它捕获来自多个来源的离线流量，而不仅仅是 [CIOfflineSend](CIOfflineSend.md)。所记录的事务（请求及其回复）来自：

- 用户程序调用 [CIOfflineSend](CIOfflineSend.md)（一个主机函数），
- 后台离线流量，以及
- 连接/事件状态机（“特殊”离线处理，例如在 [CIConnect](CIConnect.md) 与事件处理期间）。

每条已记录消息的 [Sender](#sender-字段取值) 字段标识其中哪一个发起了该消息，因此上位机可以查看发送了什么以及远端返回了什么。配套数组 [OfflineALog](OfflineALog.md)（离线邮箱 1）已预留，但当前未被填充。

## 工作原理

该缓冲区与 [OfflineALog](OfflineALog.md) 形状相同：最多 **5 条消息，每条 9 个字段**（使用 45 个元素，索引 `[1]`…`[45]`）。每条消息使写入索引前进一格，覆盖最旧的条目。每个消息槽的九个字段为：

| 槽内偏移 | 字段 | 含义 |
|----------------|-------|---------|
| +1 | Sender | 发起该消息的来源（见下表） |
| +2 | Message type | `0` = 查询，`1` = 赋值 |
| +3 | Opcode | 读取或写入的远端寄存器地址 |
| +4 | Value out | 发送的值（针对赋值） |
| +5 | Value in | 返回的值（针对查询） |
| +6 | Acknowledge / error | `0` = 正常，否则为远端的错误码 |
| +7 | Time | 发送消息时的控制器时间（参见 [Time](../03-timing/Time.md)） |
| +8 | Sample counter | 发送时的采样计数器 |
| +9 | Port | 消息所发往的轴/端口号 |

消息槽 *k*（k = 0…4）占用元素 `[9k+1]` … `[9k+9]`。

### Sender 字段取值

**Sender** 字段（每个槽中偏移 `+1`）标识发起该已记录消息的来源：

| 取值 | 含义 |
|-------|---------|
| 2 | 主机函数 —— 用户程序调用 [CIOfflineSend](CIOfflineSend.md) |
| 3 | 后台离线流量 |
| 4 | 连接/事件状态机（“特殊”离线处理） |

取值 `1`（中断）已预留，当前不会发出。

## 示例

```text
AOfflineBLog[1]     ; sender of the first logged message (2 = CIOfflineSend, 3 = background, 4 = special)
AOfflineBLog[3]     ; opcode of the first logged message
AOfflineBLog[5]     ; value returned by the remote for that message
AOfflineBLog[6]     ; its acknowledge/error code (0 = ok)
```

## 参见

- [OfflineALog](OfflineALog.md) —— 离线邮箱 1 日志（已预留；当前未被填充）
- [CIOfflineSend](CIOfflineSend.md) —— 在此处记录其事务的来源之一
- [CIOfflineData](CIOfflineData.md) —— 每个事务的请求/响应缓冲区
