---
keyword: EventPulseRes
summary: 选择解释事件脉冲宽度所用的时间单位：微秒或纳秒。
availability:
- controller
- ci-master
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

控制器在使能事件时将请求的宽度转换为脉冲生成器的内部时基。为保持全范围精度，它根据请求的时长自动选择粗步长或细步长内部时间步，使极短脉冲和较长脉冲均能精确计时。更改 `EventPulseRes` 会改变给定数值宽度的解释方式，因此更改后请检查 [EventPulseWid](EventPulseWid.md) 和所有 [EventTableWid](EventTableWid.md) 项。

`EventPulseRes` 用于选择输入单位。对于使用 100 MHz 时钟和增量式或硬件 SIN-COS 反馈的 Central-i 远程驱动器，约 163.8 µs 以内的脉宽由主控按最接近的 20 ns 步长舍入，更长的脉宽采用 5.12 µs 步长。最大值取决于事件模式和固件版本。在包含软件表脉宽修复的 AGM800 和 AGM800-EC 固件中，逐点加载的 `EventType=2` 表中每一行的脉宽上限均为 **41.93792 ms**。5.3.0-rc7 的行为、切换模式及硬件表的独立规则见脉宽说明。独立产品使用自己的定时器，并按其步长向下取整。[EventPulseWid](EventPulseWid.md)

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
