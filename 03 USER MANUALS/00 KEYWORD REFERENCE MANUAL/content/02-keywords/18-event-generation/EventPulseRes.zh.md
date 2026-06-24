---
keyword: EventPulseRes
summary: 选择解释事件脉冲宽度所用的时间单位：微秒或纳秒。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 517
attributes:
  access: rw
  scope: axis
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# EventPulseRes

选择解释事件脉冲宽度所用的时间单位：微秒或纳秒。

## 概述

`EventPulseRes` 选择事件输出脉冲宽度的时间单位。[EventPulseWid](EventPulseWid.md) 和每项 [EventTableWid](EventTableWid.md) 中的值将根据此设置解释为微秒或纳秒，从而可以指定普通毫秒级脉冲或极短的纳秒级脉冲。该参数是轴相关参数，保存至闪存，可随时更改。

## 工作原理

| 值 | EventPulseWid / EventTableWid 的宽度单位 |
|-------|----------------------------------------------|
| 0（默认） | 微秒。 |
| 1 | 纳秒。 |

控制器在使能事件时将请求的宽度转换为脉冲生成器的内部时基。为保持全范围精度，它根据请求的时长自动选择粗精或细精内部时间步长，使极短脉冲和较长脉冲均能精确计时。更改 `EventPulseRes` 会改变给定数值宽度的解释方式，因此更改后请检查 [EventPulseWid](EventPulseWid.md) 和所有 [EventTableWid](EventTableWid.md) 项。

确切的分辨率和最大值取决于硬件。在使用增量式或 SIN-COS 反馈的 Central-i 远程驱动器上，脉冲由硬件计数器计时：对于约 **163.8 us** 以内的宽度，分辨率约为 **20 ns**；对于更长的宽度，步长为较粗的 **5.12 us**，最长可产生的脉冲约为 **1.34 秒**。独立产品的分辨率和最大值有所不同（最大值更短）。在所有情况下，控制器根据请求的时长自动选择细精或粗精内部步长，因此 `EventPulseRes` 仅选择输入宽度的*单位*（微秒或纳秒），不改变可实现的分辨率（分辨率取决于脉冲的长度）。请求的宽度将量化到可实现的步长（截断至最接近的较低步长），因此低于最细步长的值可能截断为零；宽度为 0 时选择切换模式而非零长度脉冲。

## 示例

```text
AEventPulseRes=0     ; 宽度单位为微秒（默认）
AEventPulseRes=1     ; 宽度单位为纳秒
AEventPulseRes       ; 查询当前设置
```

## 另请参阅

- [EventPulseWid](EventPulseWid.md) — 每个事件脉冲的持续时间
- [EventSelect](EventSelect.md) — 选择事件脉冲驱动的输出线路
- [EventTableWid](EventTableWid.md) — 每项脉冲宽度覆盖值
