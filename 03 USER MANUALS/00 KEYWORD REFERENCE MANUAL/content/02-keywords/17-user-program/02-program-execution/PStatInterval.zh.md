---
keyword: PStatInterval
summary: 相邻两次参数统计传输之间的时间间隔，单位为毫秒。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 482
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
  - 2
  - 10000
  default: 1000
  scaling: 1.0
  implemented: partial
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# PStatInterval

相邻两次参数统计传输之间的时间间隔，单位为毫秒。

## 概述

`PStatInterval` 设置在 [PStatOn](PStatOn.md) 启用流式传输时，相邻两次程序状态传输之间的时间间隔（单位：毫秒）。有效范围为 `2`–`10000` ms（默认 `1000`）。它控制 [PStatParams](PStatParams.md) 中列出的参数采样并通过 [PStatPort](PStatPort.md) 所选端口发送的频率。这是一个非轴参数，保存至闪存。

## 工作原理

流式传输开启时，控制器在距上次传输的已用时间超过 `PStatInterval` 后发送下一批数据。较小的值提供更频繁的更新，但会在所选 [PStatPort](PStatPort.md) 上产生更多流量；请选择端口带宽和 [PStatParams](PStatParams.md) 条目数量能够承受的间隔。由于该值保存至闪存，所配置的速率在重新上电后仍保留。

## 示例

```text
APStatInterval=500   ; transmit parameter statistics every 500 ms
```

## 参见

- [PStatOn](PStatOn.md) — 启用/禁用周期性统计流式传输
- [PStatPort](PStatPort.md) — 用于流式传输的通信端口
- [PStatParams](PStatParams.md) — 每次传输中包含的参数
