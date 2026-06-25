---
keyword: InjectForceA
summary: 力指令注入的幅值，以内部力单位表示。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 590
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# InjectForceA

力指令注入的幅值，以内部力单位表示。

## 概述

`InjectForceA` 是在力指令处注入波形时的幅值，以内部力单位表示。仅当 [InjectPoint](InjectPoint.md) 选择力指令时（`InjectPoint = 3`）生效。波形形状由 [InjectType](InjectType.md) 选择。

## 工作原理

该值设定波形在力指令处所能达到的峰值幅度：正弦波在 +`InjectForceA` 与 −`InjectForceA` 之间摆动，方波和 PRBS 在这两个电平之间切换。在力指令处，v4 支持的波形为**正弦、方波和 PRBS**；v5（仅限 central-i）还在力指令处额外支持 **chirp**（[InjectType](InjectType.md) = 8 或 9）。脉冲仅适用于电流指令，不在此处使用。在**直接**模式下，波形叠加在注入开始时捕获的力参考值之上，使指令以该固定基准加上波形的形式运行。在**叠加**模式下，仅当力指令来自模拟源时，波形才叠加在实时力指令之上；否则叠加模式表现与直接模式相同，将波形叠加在注入开始时捕获的基准之上。当前电平可通过 [InjectedValue](InjectedValue.md) 读回。

## 示例

```text
AInjectForceA=10000      ; 力注入幅值（内部力单位）
AInjectForceA           ; 查询当前力注入幅值
```

## 另请参阅

- [InjectPoint](InjectPoint.md) — 力指令注入时必须为 3
- [InjectType](InjectType.md) — 选择波形形状及直接/叠加模式
- [InjectedValue](InjectedValue.md) — 读回当前注入值
