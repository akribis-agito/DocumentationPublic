---
keyword: LoggerStatus
summary: 报告连续数据记录器的当前状态。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 534
attributes:
  access: ro
  scope: non-axis
  flash: false
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# LoggerStatus

报告连续数据记录器的当前状态。

## 概述

`LoggerStatus` 是一个只读数组，用于报告连续数据记录器的实时状态：运行状态、剩余缓冲区空间、当前数据包大小、运行中的数据包标识符，以及丢包计数。上位机可通过轮询此关键字来确定何时调用 [LoggerUpload](LoggerUpload.md)，以读取由 [LoggerOn](LoggerOn.md) 启动的记录器数据。该关键字为非轴变量，不保存至闪存。缓冲区满时的行为由 [LoggerFullMod](LoggerFullMod.md) 控制。

## 工作原理

该数组以 1 为起始索引，每个元素报告记录器的一个方面：

| 索引 | 报告内容 | 含义 |
|---|---|---|
| 1 | 数据包大小 | 一个已记录采样所占用的缓冲区槽数（一个时间戳加上每个已配置参数各一个槽）。值为 0 或 1 表示未配置参数，即未进行任何记录。 |
| 2 | 剩余空间 | 内部缓冲区中剩余的空闲槽数。只有当此值至少等于数据包大小（索引 1）时，才能存储一个完整数据包。 |
| 3 | 运行状态 | `0` 未记录；`1` 正在记录；`2` 因缓冲区满而暂停。当 [LoggerFullMod](LoggerFullMod.md) = 0（满时停止）时通常会出现此情况；在覆盖模式下，若 [LoggerUpload](LoggerUpload.md) 正在读取最旧的数据包导致无法丢弃时，也可能短暂出现此状态。 |
| 4 | 数据包标识符 | 每次应生成采样时递增 1 的计数器，无论采样是否能够被存储。可用于检测数据缺口。 |
| 5 | 丢包计数器 | 因缓冲区满而未能正常存储的应采样次数：在停止模式下（索引 3 = 2），这些采样被丢弃；在覆盖模式下，最旧的采样被删除以腾出空间。 |

上位机的典型流程为：使用 [LoggerOn](LoggerOn.md) 启动记录器，然后轮询索引 3 获取运行状态，轮询索引 2 获取累积数据量，再调用 [LoggerUpload](LoggerUpload.md) 读取已完成的数据包。若索引 5 不为零且持续增长，说明缓冲区的上传速度不足。

## 示例

```text
ALoggerStatus[3]    ; query the logger run state (0/1/2)
ALoggerStatus[5]    ; query the lost-packets counter
```

## 另请参阅

- [LoggerOn](LoggerOn.md) — 启动/停止记录器
- [LoggerFullMod](LoggerFullMod.md) — 缓冲区满时的行为
- [LoggerAbout](LoggerAbout.md) — 会话元数据
- [LoggerUpload](LoggerUpload.md) — 读取已记录数据
