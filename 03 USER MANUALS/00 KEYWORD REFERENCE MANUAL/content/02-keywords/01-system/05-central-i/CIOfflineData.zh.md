---
keyword: CIOfflineData
summary: 保存 Central-i 离线（仿真）事务期间所发送有效载荷的轴级数组。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 501
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
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
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# CIOfflineData

保存 Central-i 离线（仿真）事务期间所发送有效载荷的轴级数组。

## 概述

`CIOfflineData` 是用于单次 Central-i **离线**事务的轴级请求/响应缓冲区——即对所连接远程单元内某个寄存器进行的非周期“信箱”读写。与同步通道（每个周期交换控制数据）不同，离线通道承载的是偶发的、带地址的消息：查询某个远程寄存器的值，或为其赋值。你先设置该缓冲区，调用 [CIOfflineSend](CIOfflineSend.md)，然后从同一数组中读回回复。它会保存至闪存。索引 `[0]` 未使用；字段为 `[1]`–`[5]`。

## 工作原理

| 索引 | 字段 | 含义 |
|-------|-------|---------|
| [1] | 消息类型 | `0` = 查询（读取远程寄存器），`1` = 赋值（写入远程寄存器） |
| [2] | Opcode | 要读取或写入的远程寄存器地址 |
| [3] | 待赋值的值 | 要写入的值（仅当消息类型为 `1` 时使用） |
| [4] | 查询所得值 | 远程返回的值（查询成功时填入） |
| [5] | 确认 / 错误 | `0` = 已确认；任何其他值为远程返回的错误码 |

[CIOfflineSend](CIOfflineSend.md) 由元素 [1]–[3] 构建外发的离线消息，在端口的离线信箱上发送，等待回复，并将结果写入 [4]（用于查询）和 [5]（确认/错误）。该交换过程也记录在离线日志缓冲区（[OfflineALog](OfflineALog.md) / [OfflineBLog](OfflineBLog.md)）中。

这是一个直接读取或设置远程单元单个寄存器的专家级机制；在正常运行中，固件本身会在 [CIConnect](CIConnect.md) 期间使用离线通道来读取远程单元的标识。

## 示例

```text
ACIOfflineData[1]=0   ; message type: query (read)
ACIOfflineData[2]=...  ; opcode: the remote register address to read
ACIOfflineSend         ; perform the transaction
ACIOfflineData[4]      ; read back the value returned by the remote
ACIOfflineData[5]      ; 0 = ok, non-zero = error code
```

## 另请参阅

- [CIOfflineDef](CIOfflineDef.md) — 离线通道定义（频率 / 滤波器）
- [CIOfflineSend](CIOfflineSend.md) — 发送此事务并捕获回复
- [OfflineALog](OfflineALog.md) / [OfflineBLog](OfflineBLog.md) — 离线消息日志
- [CISyncDef](CISyncDef.md) — 与之相对的同步（每周期）通道
