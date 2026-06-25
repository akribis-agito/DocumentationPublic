---
keyword: OfflineALog
summary: Central-i 离线邮箱 1 的预留离线（邮箱）消息日志；当前固件未予填充，因此保持为 0。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 620
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
# OfflineALog

Central-i **离线邮箱 1** 的预留离线（邮箱）消息日志；当前固件未予填充。

## 概述

`OfflineALog` 是一个非轴数组，**预留**作为 Central-i **离线邮箱 1**（优先级的、固件驱动的通道）的日志。当前固件**未予填充**，因此其所有元素均保持默认值 `0`；读取它不会返回离线消息数据。

实际被记录的离线事务记录在 [OfflineBLog](OfflineBLog.md)（离线邮箱 2）中。请使用该日志查看已交换的离线消息及其结果。

## 工作原理

该数组的维度与 [OfflineBLog](OfflineBLog.md) 相同：最多 **5 条消息，每条 9 个字段**（占用 45 个元素，索引 `[1]`…`[45]`）。由于当前没有任何内容写入它，每个元素读出均为 `0`。预期的每条消息字段布局（由 [OfflineBLog](OfflineBLog.md) 实际填充）依次为：

| 槽内偏移 | 字段 | 含义 |
|----------------|-------|---------|
| +1 | Sender | 发出该消息的来源（中断 / 上位机函数 / 后台 / 特殊） |
| +2 | Message type | `0` = 查询，`1` = 赋值 |
| +3 | Opcode | 所读取或写入的远程寄存器地址 |
| +4 | Value out | 发送的值（用于赋值） |
| +5 | Value in | 返回的值（用于查询） |
| +6 | Acknowledge / error | `0` = 正常，否则为远程单元的错误码 |
| +7 | Time | 发送消息时的控制器时间（参见 [Time](../03-timing/Time.md)） |
| +8 | Sample counter | 发送时的采样计数器 |
| +9 | Port | 该消息发往的轴/端口编号 |

消息槽 *k*（k = 0…4）将占用元素 `[9k+1]` … `[9k+9]`。[OfflineBLog](OfflineBLog.md) 填充相同的字段布局。

## 示例

```text
AOfflineALog[3]     ; reserved slot; currently reads 0 (not populated)
AOfflineALog[12]    ; reserved slot; currently reads 0 (not populated)
```

## 另请参阅

- [OfflineBLog](OfflineBLog.md) — 离线邮箱 2 日志，即固件实际填充的那个
- [CIOfflineData](CIOfflineData.md) / [CIOfflineSend](CIOfflineSend.md) — 离线事务
- [CIStatus](CIStatus.md) — 离线错误计数器与最近错误码
