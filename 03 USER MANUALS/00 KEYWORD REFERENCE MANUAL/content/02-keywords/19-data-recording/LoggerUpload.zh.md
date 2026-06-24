---
keyword: LoggerUpload
summary: 将已记录的数据缓冲区传输至上位机的指令。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 536
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# LoggerUpload

将已记录的数据缓冲区传输至上位机的指令。

## 概述

`LoggerUpload` 是一条指令，用于将控制器中累积的已记录采样流式传输至上位机。可在由 [LoggerOn](LoggerOn.md) 启动的记录器运行期间或停止后调用。它是连续记录器对应 [RecUpload](RecUpload.md) 的等效指令，适用于记录示波器。该指令为非轴指令，不保存至闪存。使用 [LoggerAbout](LoggerAbout.md) 解析已上传的内容。

## 工作原理

每次调用仅流式传输缓冲区中已完成并等待上传的采样（数据包），然后释放其占用的空间以便记录继续进行：

1. 根据 [LoggerStatus](LoggerStatus.md) 报告的剩余空间和数据包大小，确定缓冲区中当前完整数据包的数量。若可用数据包不足一个，则不发送任何数据。
2. 单次调用最多传输约 800 字节的数据包（取决于固件：传统 32 位固件约为 200 个缓冲槽，较新的 64 位固件约为 100 个缓冲槽）；若队列中还有更多数据，则需多次调用 `LoggerUpload` 将其全部读取。
3. 数据包发送后，其占用的缓冲区空间被释放，体现为 [LoggerStatus](LoggerStatus.md)（索引 2）中剩余空间增加。

由于记录器持续运行，上位机通常需定期调用 `LoggerUpload` 以防止缓冲区填满。在停止模式下（[LoggerFullMod](LoggerFullMod.md) = 0），上传操作同时也是使已暂停的记录器恢复运行的方式，因为上传释放了记录器等待的空间。

## 示例

```text
ALoggerUpload        ; stream the available logged packets to the host
```

## 另请参阅

- [LoggerOn](LoggerOn.md) — 启动/停止记录器
- [LoggerStatus](LoggerStatus.md) — 记录器运行状态与缓冲区填充情况
- [LoggerAbout](LoggerAbout.md) — 会话元数据
- [RecUpload](RecUpload.md) — 记录示波器的等效上传指令
