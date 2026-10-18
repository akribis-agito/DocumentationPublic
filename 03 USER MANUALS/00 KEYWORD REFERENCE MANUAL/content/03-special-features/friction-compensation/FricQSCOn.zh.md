---
keyword: FricQSCOn
summary: 使能象限切换补偿（在换向和起动时施加起动冲击）。
availability:
  standalone: []
  central-i:
  - v5
can_code: 938
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
language: zh-CN
---
# FricQSCOn

使能象限切换补偿（在换向和起动时施加起动冲击）。

## 概述

`FricQSCOn` = 1 时，轴每次起动或换向都会叠加一个短暂的起动冲击。适用于 AGM800 和 AGM800-EC（central-i v5）。默认值为 0（关闭）。

## 工作原理

当速度反馈朝新的方向离开死区带（[FricVBandPos](FricVBandPos.md) / [FricVBandNeg](FricVBandNeg.md)），并经过保持时间 [FricQSCHold](FricQSCHold.md) 后，环节叠加一个约为 |[FricIStatPos](FricIStatPos.md)| − |[FricIPos](FricIPos.md)|（或负方向对应值）的冲击，并按时间常数 [FricQSCTime](FricQSCTime.md) 衰减。冲击只包含起动超出量；滑动电平由所选的 [FricMethod](FricMethod.md) 提供。

冲击叠加在方法 0 至 3 上。方法 4 和 5 已包含起动电平，因此不叠加。冲击属于该环节的输出，因此同样受 [FricLim](FricLim.md) 钳位。

## 示例

```text
AFricQSCOn=1       ; 叠加起动冲击
```

## 另请参阅

- [FricQSCTime](FricQSCTime.md)
- [FricQSCHold](FricQSCHold.md)
- [摩擦前馈](00-overview.md)
