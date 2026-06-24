---
keyword: ScopeOn
summary: 启用或禁用 Central-i 信号示波器。
language: zh-CN
availability:
  standalone: []
  central-i:
  - v5
can_code: 742
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# ScopeOn

启用或禁用 Central-i 信号示波器。

## 概述

`ScopeOn` 启动或停止 Central-i 信号示波器——一种流式捕获机制，按 [ScopeGap](ScopeGap.md) 设定的间隔对 [ScopeParams](ScopeParams.md) 中配置的信号进行采样，并通过 [ScopeUpload](ScopeUpload.md) 提供增量读取。设为 `1` 时示波器开始捕获；设为 `0` 时停止捕获。该参数为非轴参数，不保存至闪存，因此示波器在上电后始终处于禁用状态。仅适用于 Central-i（v5）。

## 工作原理

将 `ScopeOn` 从 `0` 设为 `1` 可一步完成新会话的准备：

1. 分析 [ScopeParams](ScopeParams.md) 中的信号列表，计算数据包大小（一个时间戳加每个已配置信号各一个缓冲槽），并发布至 [ScopeStatus](ScopeStatus.md)（索引 1）。
2. 循环捕获缓冲区复位（空闲空间设为全满，数据包标识符和丢包计数器清零）。
3. 配置快照至 [ScopeAbout](ScopeAbout.md)，以便后续上传时能够解析数据。

此后，示波器在后台每隔 [ScopeGap](ScopeGap.md) 个节拍评估一次采样并追加至缓冲区。若缓冲区在数据读出前已满，示波器将**暂停**——[ScopeStatus](ScopeStatus.md) 索引 3 读取为 `2`（因缓冲区满而暂停），丢包计数器递增——并在 [ScopeUpload](ScopeUpload.md) 释放空间后自动恢复。将 `ScopeOn` 设回 `0` 立即停止采样；已缓冲的数据仍可上传。

示波器是三种独立捕获机制之一：触发对齐记录示波器（`Rec*` 关键字）一次性捕获固定长度窗口；连续记录器（[LoggerOn](LoggerOn.md)）可无限期运行，最多支持 40 个参数；而此 Central-i 示波器最多流式传输六路信号用于实时监控。

## 示例

```text
AScopeOn=1           ; 启动 Central-i 示波器
AScopeOn=0           ; 停止 Central-i 示波器
AScopeOn            ; 查询示波器是否正在运行
```

## 另请参阅

- [ScopeParams](ScopeParams.md) — 示波器捕获的信号
- [ScopeGap](ScopeGap.md) — 示波器采样间隔
- [ScopeStatus](ScopeStatus.md) — 示波器运行状态及缓冲区填充情况
- [ScopeUpload](ScopeUpload.md) — 获取已捕获数据
- [LoggerOn](LoggerOn.md) — 连续数据记录器
