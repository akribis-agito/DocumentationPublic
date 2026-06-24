---
keyword: InjectVelAmp
summary: 速度指令注入的幅值；单位取决于双环设置。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 115
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 1300000000
  default: 10000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# InjectVelAmp

速度指令注入的幅值；单位取决于双环设置。

## 概述

`InjectVelAmp` 是在速度指令处注入波形的幅值。仅当 [InjectPoint](InjectPoint.md) 选择速度指令（`InjectPoint = 1`）时有效。波形形状由 [InjectType](InjectType.md) 选择。幅值单位取决于双环设置；详见[控制整定 – 双环控制](../11-control-tuning/02-dual-loop-control/00-overview.md)。

## 工作原理

该值设定波形在速度环参考 [VelRef](../10-motion/01-kinematics-status/VelRef.md) 处达到的峰值幅值：正弦波在 +`InjectVelAmp` 和 −`InjectVelAmp` 之间摆动，方波和 PRBS 在这两个电平之间切换。v4 中可用的速度指令波形为正弦、方波和 PRBS；**扫频（Chirp）**在 v5（仅限 central-i）中新增。在**直接**模式（[InjectType](InjectType.md) = 1、3 或 6，v5 中还有 8）下，该波形成为 `VelRef`，替代位置环输出；在**叠加**模式下，它叠加到 `VelRef` 上。两个版本中，合成参考值仍按常规钳位至速度限值（[MaxVel](../06-protections/03-motion/general-maximum-limits/MaxVel.md)）。当前电平可通过 [InjectedValue](InjectedValue.md) 读回。

**仅在 v4 中**，速度指令处的 PRBS 波形还会在速度参考上附加 [InjectCurrDC](InjectCurrDC.md) 偏置（直接和叠加 PRBS 模式均如此）；v5 仅施加 PRBS 值，不含直流项。

## 示例

```text
AInjectVelAmp=10000      ; velocity injection amplitude (default)
AInjectVelAmp           ; query the current velocity injection amplitude
```

## 另请参阅

- [InjectPoint](InjectPoint.md) — 速度指令注入时必须为 1
- [InjectType](InjectType.md) — 选择波形形状和直接/叠加模式
- [VelRef](../10-motion/01-kinematics-status/VelRef.md) — 本注入所修改的速度环参考
- [InjectedValue](InjectedValue.md) — 读回当前注入值
- [控制整定 – 双环控制](../11-control-tuning/02-dual-loop-control/00-overview.md) — 确定幅值单位
