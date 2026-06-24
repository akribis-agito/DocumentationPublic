---
keyword: InjectedValue
summary: 当前注入值的只读读数；单位随注入点而定。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 118
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# InjectedValue

当前注入值的只读读数；单位随注入点而定。

## 概述

`InjectedValue` 是当前正在施加到控制环的注入值的只读读数。其单位取决于 [InjectPoint](InjectPoint.md) 选择的活动注入位置（例如，电流指令注入时单位为 mA）。在系统辨识或阶跃响应测试期间，可用于监测或记录注入波形。

## 工作原理

控制器每个控制器周期根据活动的 [InjectType](InjectType.md) 波形重新计算注入值，并在此报告整数结果，因此反复读取 `InjectedValue` 即可描绘波形本身（正弦波在 ±幅值 之间扫动，方波在 +幅值 和 −幅值 之间交替，PRBS 在两者之间切换，脉冲保持幅值后返回 0）。限定其范围的幅值来自与所选 `InjectPoint`（电流、速度、位置或力）关联的关键字。对于电流指令注入，报告值为添加 [InjectCurrDC](InjectCurrDC.md) 偏置之前的波形值。当 [InjectType](InjectType.md) 为 0（无注入）时，该值为 0。

该值与每个周期被替换进或叠加到目标指令的注入值相同；对于速度环，该项修改 [VelRef](../10-motion/01-kinematics-status/VelRef.md)。

## 示例

```text
AInjectedValue      ; read the present injection value
```

## 另请参阅

- [InjectPoint](InjectPoint.md) — 决定该值的单位
- [InjectType](InjectType.md) — 选择正在注入的波形
- [InjectCurrDC](InjectCurrDC.md) — 电流注入时在该值之后附加的直流偏置
- [VelRef](../10-motion/01-kinematics-status/VelRef.md) — 速度注入时该值所修改的速度环参考
