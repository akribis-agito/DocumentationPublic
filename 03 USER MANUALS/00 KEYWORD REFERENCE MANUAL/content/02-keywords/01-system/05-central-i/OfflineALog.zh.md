---
keyword: OfflineALog
summary: 启用队列的 AGM800 和 AGM800-EC 固件中的优先级离线邮箱 1 事务日志。
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
last_updated: '2026-10-17'
doc_revision: '2026.10'
language: zh-CN
---
# OfflineALog

**启用队列的 AGM800 和 AGM800-EC 固件**中的优先级离线邮箱 1 事务日志。

## 概述

中断工作器在事务完成时记录锁存位置查询以及事件目标位置/选择器写入。此环形日志由所有端口共享，最多保留五条消息。较旧固件及其他产品可能仍将此预留数组保持为零。

每条记录在事务终结时完整发布，包括失败和取消的事务。队列接收前被拒绝的请求不产生记录。确认/错误字段为零表示成功，非零表示远端错误或本地通信错误。时间和采样计数器字段表示完成时刻。

## 字段布局

槽 *k*（k = 0…4）占用 `[9k+1]` … `[9k+9]`。

| 偏移 | 字段 | 含义 |
|---|---|---|
| +1 | Sender | `1` = 中断 |
| +2 | Message type | `0` = 查询，`1` = 赋值 |
| +3 | Opcode | 远端寄存器地址 |
| +4 | Value out | 已复制的赋值数据 |
| +5 | Value in | 成功查询的结果；否则为零 |
| +6 | Acknowledge / error | 成功为零，失败为非零 |
| +7 | Time | 完成时的控制器时间 |
| +8 | Sample counter | 完成时的采样计数器 |
| +9 | Port | 从零开始的轴/端口编号 |

## 示例

```text
AOfflineALog[3]     ; 槽 0 的操作码
AOfflineALog[6]     ; 槽 0 的终结确认/错误
```

## 另请参阅

- [OfflineBLog](OfflineBLog.md) —— 邮箱 2 事务，包括 CNC 中断提交
- [CIStatus](CIStatus.md) —— 邮箱错误计数器及最近错误
