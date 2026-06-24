---
keyword: PStatPort
summary: 选择用于参数统计流式传输的通信端口。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 481
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
  - 1
  - 3
  default: 1
  scaling: 1.0
  implemented: partial
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# PStatPort

选择用于参数统计流式传输的通信端口。

## 概述

`PStatPort` 选择在 [PStatOn](PStatOn.md) 启用流式传输时，程序状态数据通过哪个通信端口发送。它与 [PStatParams](PStatParams.md)（发送内容）和 [PStatInterval](PStatInterval.md)（发送频率）配合使用。它是非轴参数，保存至闪存（默认值 `1`，即 CAN）。

## 工作原理

该值选择后台流式传输器使用的物理链路：

| 值 | 端口 |
|---|---|
| 1 | CAN |
| 2 | 串口（mini 连接器） |
| 3 | 串口（RJ45 连接器） |

在串口上，状态流式传输会让步于输出的指令回复，因此不会干扰正常的请求/响应通信；在 CAN 上（默认），批量数据以状态消息形式发送。请根据所选 [PStatInterval](PStatInterval.md) 和 [PStatParams](PStatParams.md) 条目数量，选择带宽满足需求的端口。

## 示例

```text
APStatPort=1         ; 通过 CAN 流式传输（默认）
APStatPort=2         ; 通过串口（mini 连接器）流式传输
```

## 另请参阅

- [PStatOn](PStatOn.md) — 启用/禁用周期性统计流式传输
- [PStatParams](PStatParams.md) — 每次发送所包含的参数
- [PStatInterval](PStatInterval.md) — 发送间隔
