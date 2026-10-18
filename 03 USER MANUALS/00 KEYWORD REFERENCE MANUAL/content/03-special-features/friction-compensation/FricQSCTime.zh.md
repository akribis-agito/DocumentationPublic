---
keyword: FricQSCTime
summary: 象限切换冲击的衰减时间常数，单位为 µs。
availability:
  standalone: []
  central-i:
  - v5
can_code: 939
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
  - 100
  - 1000000
  default: 5000
  scaling: 1.0
  implemented: final
overrides: {}
language: zh-CN
---
# FricQSCTime

象限切换冲击的衰减时间常数，单位为 µs。

## 概述

`FricQSCTime` 设定象限切换冲击衰减的快慢，单位为微秒。适用于 AGM800 和 AGM800-EC（central-i v5）。取值范围为 100 至 1 000 000 µs，默认值为 5000 µs（5 ms）。

## 工作原理

起动或换向后，冲击每经过一个 `FricQSCTime` 下降约 63%。应保持较短：冲击应在轴移动较远之前消失，否则它本身会造成超调。仅在 [FricQSCOn](FricQSCOn.md) = 1 时有效。

## 示例

```text
AFricQSCTime=3000  ; 冲击以 3 ms 时间常数衰减
```

## 另请参阅

- [FricQSCOn](FricQSCOn.md)
- [FricQSCHold](FricQSCHold.md)
