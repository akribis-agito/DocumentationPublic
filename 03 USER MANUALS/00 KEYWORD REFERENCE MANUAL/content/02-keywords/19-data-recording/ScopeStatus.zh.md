---
keyword: ScopeStatus
summary: 报告 Central-i 示波器的当前状态。
language: zh-CN
availability:
  standalone: []
  central-i:
  - v5
can_code: 745
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
---
# ScopeStatus

报告 Central-i 示波器的当前状态。

## 概述

`ScopeStatus` 是一个只读数组，报告 Central-i 示波器的实时状态：运行状态、剩余缓冲空间、当前数据包大小、运行数据包标识符以及丢包计数。它使上位机能够轮询 [ScopeOn](ScopeOn.md) 启动的示波器，以决定何时调用 [ScopeUpload](ScopeUpload.md)。该变量为非轴状态变量，不保存至闪存。

## 工作原理

该数组为 1 索引。每个元素报告示波器的一个方面：

| 索引 | 报告内容 | 含义 |
|---|---|---|
| 1 | 数据包大小 | 一个已捕获采样占用的缓冲槽数（一个时间戳加每个已配置信号各一个槽）。为 0 或 1 表示未配置任何信号，即无内容被捕获。 |
| 2 | 剩余空间 | 捕获缓冲区中剩余的空闲槽数。仅当该值至少等于数据包大小（索引 1）时，才能存储一个完整数据包。 |
| 3 | 运行状态 | `0` 未捕获；`1` 正在捕获；`2` 因缓冲区满而暂停。[ScopeUpload](ScopeUpload.md) 释放空间后，示波器将自动从暂停状态恢复。 |
| 4 | 数据包标识符 | 每次到达采样时刻时递增一次的计数器，无论是否能够存储——可用于检测数据间隙。 |
| 5 | 丢包计数器 | 因缓冲区满而无法存储的到期采样数量。 |

上位机通常先用 [ScopeOn](ScopeOn.md) 启动示波器，然后轮询索引 3 获取运行状态、轮询索引 2 获取已积累数据，并调用 [ScopeUpload](ScopeUpload.md) 获取已完成的数据包。索引 5 非零且持续增长表明上传速度不足——请通过 [ScopeGap](ScopeGap.md) 降低速率，或提高上传频率。

## 示例

```text
AScopeStatus[3]      ; 查询示波器运行状态（0 空闲，1 正在捕获，2 因满而暂停）
AScopeStatus[2]      ; 查询剩余缓冲空间
AScopeStatus[5]      ; 查询丢包计数器
```

## 另请参阅

- [ScopeOn](ScopeOn.md) — 启动/停止示波器
- [ScopeUpload](ScopeUpload.md) — 获取已捕获数据
- [ScopeAbout](ScopeAbout.md) — 已捕获信号集的快照
