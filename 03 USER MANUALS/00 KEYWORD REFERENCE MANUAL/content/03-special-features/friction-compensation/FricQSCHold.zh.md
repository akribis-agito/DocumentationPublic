---
keyword: FricQSCHold
summary: 象限切换冲击前的保持时间，单位为 µs（由 FricQSCDelay 更名，原单位为采样周期）。
availability:
  standalone: []
  central-i:
  - v5
can_code: 940
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
  - 250000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
language: zh-CN
---
# FricQSCHold

象限切换冲击前的保持时间，单位为 µs（由 FricQSCDelay 更名，原单位为采样周期）。

## 概述

`FricQSCHold` 在速度离开死区带后延迟施加象限切换冲击，单位为微秒。适用于 AGM800 和 AGM800-EC（central-i v5）。取值范围为 0 至 250 000 µs，默认值为 0（不延迟）。它取代 5.3.0-rc4 中的 `FricQSCDelay`（CAN 代码不变）。

## 工作原理

过零后紧接着的速度是整个运动中最不可靠的部分；短暂的保持时间可避免朝一个即将再次改变的方向施加冲击。该值按整数个控制周期取整。

**单位已变更。** `FricQSCDelay` 以控制周期计数；`FricQSCHold` 以微秒为单位，因此在所有产品上表示相同的时间。在 rc4 下保存的值会被当作微秒读取，对应的延迟不同（短得多）：请重新输入。仅在 [FricQSCOn](FricQSCOn.md) = 1 时有效。

## 示例

```text
AFricQSCHold=500   ; 离开死区带后等待 0.5 ms 再施加冲击
```

## 另请参阅

- [FricQSCOn](FricQSCOn.md)
- [FricQSCTime](FricQSCTime.md)
