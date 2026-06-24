---
keyword: LoggerFullMod
summary: 选择记录器缓冲区填满时的行为（覆盖或停止）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 533
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# LoggerFullMod

选择记录器缓冲区填满时的行为（覆盖或停止）。

## 概述

`LoggerFullMod` 设置连续数据记录器在内部缓冲区填满时的行为，可在停止模式与覆盖（循环）模式之间切换。该设置决定长时间记录是在缓冲区首次填满时冻结，还是持续保留最新采样。该参数为非轴参数，保存至闪存，可随时更改。它与 [LoggerOn](LoggerOn.md) 和 [LoggerGap](LoggerGap.md) 配合使用，并通过 [LoggerStatus](LoggerStatus.md) 反映。

## 工作原理

该值选择当新采样到期但缓冲区无法容纳完整数据包时的处理方式：

| 值 | 模式 | 缓冲区满时的行为 |
|---|---|---|
| 0 | 停止（暂停） | 新采样被丢弃，记录器报告暂停状态（[LoggerStatus](LoggerStatus.md) 索引 3 = 2）。上位机通过调用 [LoggerUpload](LoggerUpload.md) 释放空间后，记录自动恢复。较早的采样得以保留。 |
| 1 | 覆盖（循环） | 最旧的已存储采样被丢弃以腾出空间存放新采样，因此缓冲区始终保存最新的采样。（如果最旧的采样正在上传，则丢弃该采样。） |

在两种模式下，每个被丢弃或覆盖的采样都会使 [LoggerStatus](LoggerStatus.md)（索引 5）报告的丢包计数器递增。记录器启用时，生效的模式会被捕获至会话元数据中，并由 [LoggerAbout](LoggerAbout.md)（索引 2）报告。运行中的会话保持启动时的模式；若需使新设置生效，请在启用记录器之前更改 `LoggerFullMod`（或停止后重新启动）。

## 示例

```text
ALoggerFullMod=0    ; 缓冲区填满时停止（暂停）记录
ALoggerFullMod=1    ; 覆盖最旧采样（循环缓冲区）
ALoggerFullMod      ; 查询当前的缓冲区满模式
```

## 另请参阅

- [LoggerOn](LoggerOn.md) — 启动/停止记录器
- [LoggerStatus](LoggerStatus.md) — 记录器运行状态及缓冲区填充情况
- [LoggerGap](LoggerGap.md) — 记录器采样间隔
