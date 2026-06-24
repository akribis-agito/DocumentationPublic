---
keyword: LoggerOn
summary: 启用或禁用连续数据记录器。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 530
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# LoggerOn

启用或禁用连续数据记录器。

## 概述

`LoggerOn` 启动或停止连续数据记录器。设为 `1` 时，记录器开始按 [LoggerGap](LoggerGap.md) 设定的速率采样 [LoggerParams](LoggerParams.md) 中配置的参数；设为 `0` 时停止记录。该参数为非轴参数，不保存至闪存，因此记录器在上电后始终处于禁用状态。

## 工作原理

将 `LoggerOn` 从 `0` 设为 `1` 将在一步内准备好全新会话：

1. 分析 [LoggerParams](LoggerParams.md) 中的参数列表，计算数据包大小（时间戳加每个已配置参数一个缓冲槽），并将结果发布至 [LoggerStatus](LoggerStatus.md)（索引 1）。
2. 重置缓冲区（空闲空间置为满，清除数据包标识符和丢包计数器），并将第一个采样的时间戳置零。
3. 将当前的 [LoggerFullMod](LoggerFullMod.md)、启动时间和参数列表快照至 [LoggerAbout](LoggerAbout.md)。

此后，记录器在后台每 [LoggerGap](LoggerGap.md) 个节拍评估一次采样，并将其追加至循环缓冲区。缓冲区满时，按 [LoggerFullMod](LoggerFullMod.md) 选定的行为处理。将 `LoggerOn` 设回 `0` 立即停止采样；缓冲区中已有的数据仍可上传。

与记录示波器（`Rec*` 关键字）——捕获固定长度、触发对齐的窗口并一次性回读——不同，连续记录器在后台无限期运行，并以增量方式排空：使用 [LoggerStatus](LoggerStatus.md) 监控其状态，使用 [LoggerUpload](LoggerUpload.md) 在数据包积累时逐步取回。记录器没有触发配置。

## 示例

```text
ALoggerOn=1          ; 启动连续记录器
ALoggerOn=0          ; 停止连续记录器
ALoggerOn           ; 查询记录器是否正在运行
```

## 另请参见

- [LoggerParams](LoggerParams.md) — 记录器记录的参数
- [LoggerGap](LoggerGap.md) — 记录器采样间隔
- [LoggerStatus](LoggerStatus.md) — 记录器运行状态
- [LoggerUpload](LoggerUpload.md) — 取回已记录数据
