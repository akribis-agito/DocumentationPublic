---
keyword: ScopeUpload
summary: 将 Central-i 示波器缓冲区传输至上位机的指令。
language: zh-CN
availability:
  standalone: []
  central-i:
  - v5
can_code: 747
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# ScopeUpload

将 Central-i 示波器缓冲区传输至上位机的指令。

## 概述

`ScopeUpload` 是一条指令，用于将示波器缓冲区中已捕获的采样流式传输至上位机。可在 [ScopeOn](ScopeOn.md) 启动的示波器运行期间或停止后调用。它是 [LoggerUpload](LoggerUpload.md) 和 [RecUpload](RecUpload.md) 在 Central-i 示波器中的对应项。该指令为非轴指令，不保存至闪存。使用 [ScopeAbout](ScopeAbout.md) 解析已上传的内容。

## 工作原理

每次调用将流式传输缓冲区中当前等待的所有完整采样（数据包），并释放其占用的空间以便捕获继续：

1. 根据 [ScopeStatus](ScopeStatus.md) 报告的空闲空间和数据包大小，确定可用的完整数据包数量。若不足一个完整数据包，则不发送任何内容。
2. 单次调用传输有限量的数据；若排队的数据包超过单次传输容量，则需多次调用 `ScopeUpload` 才能完全清空。
3. 数据包发送后，其缓冲空间随即释放，体现为 [ScopeStatus](ScopeStatus.md)（索引 2）中空闲空间的增加。

由于示波器在后台运行，上位机通常定期调用 `ScopeUpload` 以防止缓冲区填满。上传也是使因缓冲区满而暂停（[ScopeStatus](ScopeStatus.md) 索引 3 = `2`）的示波器恢复捕获的方式，因为上传释放了示波器等待的空间。

## 示例

```text
AScopeUpload         ; 将可用的已捕获数据包流式传输至上位机
```

## 另请参阅

- [ScopeOn](ScopeOn.md) — 启动/停止示波器
- [ScopeStatus](ScopeStatus.md) — 示波器运行状态及缓冲区填充情况
- [ScopeAbout](ScopeAbout.md) — 会话元数据
- [LoggerUpload](LoggerUpload.md) — 连续记录器的等效上传指令
