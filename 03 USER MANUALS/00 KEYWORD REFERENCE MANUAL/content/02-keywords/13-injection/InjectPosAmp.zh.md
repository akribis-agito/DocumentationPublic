---
keyword: InjectPosAmp
summary: 位置指令注入的幅值，以主用户单位表示。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 116
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
  - 2147483647
  default: 100
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# InjectPosAmp

位置指令注入的幅值，以主用户单位表示。

## 概述

`InjectPosAmp` 是在位置指令处注入波形时的幅值，以主用户单位（可由 [UsrUnits](../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) 配置）表示。仅当 [InjectPoint](InjectPoint.md) 选择位置指令时（`InjectPoint = 2`）生效。波形形状由 [InjectType](InjectType.md) 选择。

## 工作原理

该值设定波形在位置参考处所能达到的峰值幅度：正弦波在 +`InjectPosAmp` 与 −`InjectPosAmp` 之间摆动，方波和 PRBS 在这两个电平之间切换。在位置指令处，v4 支持的波形为**正弦、方波和 PRBS**；v5（仅限 central-i）还在位置指令处额外支持 **chirp**（[InjectType](InjectType.md) = 8 或 9）。脉冲波形仅适用于电流指令，不在此处使用。在**直接**模式下，波形叠加在注入开始时捕获的位置参考值之上，从该点起替代运动规划器输出；在**叠加**模式下，波形叠加在运动规划器的实时输出之上。当前电平可通过 [InjectedValue](InjectedValue.md) 读回。

## 示例

```text
AInjectPosAmp=100        ; 位置注入幅值（默认）
AInjectPosAmp           ; 查询当前位置注入幅值
```

## 另请参见

- [InjectPoint](InjectPoint.md) — 位置指令注入时必须为 2
- [InjectType](InjectType.md) — 选择波形形状及直接/叠加模式
- [InjectedValue](InjectedValue.md) — 读回当前注入值
