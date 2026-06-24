---
keyword: VEncDelay
summary: 脉冲/方向建立延迟（us），即方向变化与第一个虚拟编码器脉冲之间的延迟。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 616
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
  - 25
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# VEncDelay

脉冲/方向建立延迟（以微秒为单位），即方向变化与第一个脉冲之间的延迟。

## 概述

当输出为脉冲/方向格式（[VEncType](VEncType.md) = 0）时，`VEncDelay` 设置虚拟编码器在改变方向线后、发出第一个脉冲之前所等待的建立时间，**单位为微秒**。这可保证接收设备在前导脉冲边沿之前看到稳定的方向电平。取值范围为 0 至 25（µs），默认值为 0。它是轴相关参数，保存至闪存，并可在电机使能或运动中更改。

它**不是**反馈路径延迟，也不会延迟被跟踪的值本身 —— 它只是将一个控制周期内方向反转之后的第一个脉冲向后移位。

## 工作原理

写入 `VEncDelay` 时，控制器将其从微秒转换为硬件时钟数（微秒 × 每微秒时钟数），并将其存储为“到第一个脉冲的时钟数”值。每个控制周期，当发出的方向符号发生变化时，控制器在新方向的第一个脉冲之前加载 `2 × VEncDelay` 个时钟数；当方向未变化时，不插入额外延迟。

对于 A-quad-B 输出（`VEncType = 1`），该延迟被强制为 **0** —— 正交通道从不同时切换，因此无需方向建立时间。

## 示例

```text
AVEncDelay=0         ; no setup delay (default)
AVEncDelay=5         ; 5 us between a direction change and the first pulse
```

## 另请参阅

- [VEncOn](VEncOn.md) —— 启用虚拟编码器
- [VEncType](VEncType.md) —— 输出格式；该延迟仅适用于脉冲/方向（`VEncType=0`）
- [VEncSrc](VEncSrc.md) —— 被跟踪的源变量
