---
keyword: FWInfo
summary: 只读命令，返回固件版本与构建信息。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 312
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
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# FWInfo

只读命令，返回固件版本与构建信息。

## 概述

`FWInfo` 是一个只读命令（一个函数），用于返回控制器的固件构建信息块。上位机软件用它来识别设备当前运行的固件构建——例如在调试投运前确认某台单元已运行预期的发布版本，或为支持报告记录该构建信息。若需获取数值形式的固件/FPGA 版本，请改读 [Identity](Identity.md)；`FWInfo` 返回的是可读的构建描述。

## 工作原理

构建信息存储在闪存中一个固定的常量块内，该块在下载固件 HEX 镜像时写入。该块保存**四行自由文本，每行最多 64 个字符**，用于描述构建信息——通常是关于该发布版本变更内容的简短说明，以及该固件应配套的 FPGA 版本。`FWInfo` 将这四行回传给上位机，随后追加**固件校验和**作为最后一个文本字段，再追加一个终止符。每行存储内容均以 NUL 结尾；固件会用空格替换终止符及任何尾随字节，使上位机（Agito PCSuite）收到定宽、可打印的文本。回复使用与 `ProgInfo` 相同的字符串协议。

由于这四行是任意的构建文本，其确切内容随每次固件构建而变化；应将其视为不透明的可读描述，而非可解析的结构。

## 示例

```text
AFWInfo             ; return the firmware build-info lines and checksum
```

## 另请参阅

- [Identity](Identity.md) — 数值形式的固件/FPGA 版本与功能标志
- [About](About.md) — 完整参数转储（Agito PCSuite 内部使用）
- [UnitStat](UnitStat.md) — 标记固件/FPGA 镜像不匹配
