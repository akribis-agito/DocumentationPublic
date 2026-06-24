---
keyword: InjectTimeOn
summary: 脉冲注入的脉冲持续时间，单位为毫秒。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 125
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 65536
  default: 0
  scaling: 65.536
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# InjectTimeOn

脉冲注入的脉冲持续时间，单位为毫秒。

## 概述

`InjectTimeOn` 定义脉冲注入的导通时间（持续时间），单位为毫秒。仅当 [InjectType](InjectType.md) 选择脉冲波形（`InjectType = 5`）时有效，该波形仅用于电流指令注入（`InjectPoint = 0`）。脉冲幅值来自 [InjectCurrAmp](InjectCurrAmp.md)。

## 工作原理

脉冲为单次、不重复的矩形脉冲。脉冲注入开始时，输出保持在配置的幅值；控制器累计已过去的控制器周期数，一旦经过时间达到 `InjectTimeOn`，输出降为零并保持不变（脉冲不重复）。该值以毫秒为单位输入，控制器在内部将其转换为完整控制器周期数，因此实际持续时间四舍五入到最近的周期。值为 0 时不产生脉冲。脉冲高电平期间的注入电平可通过 [InjectedValue](InjectedValue.md) 读回。

## 示例

```text
AInjectTimeOn=10     ; 10 ms pulse
AInjectTimeOn       ; query the current pulse duration
```

## 另请参阅

- [InjectType](InjectType.md) — 选择脉冲波形（InjectType = 5）
- [InjectCurrAmp](InjectCurrAmp.md) — 电流脉冲的幅值
- [InjectPoint](InjectPoint.md) — 选择注入位置（脉冲时必须为 0）
- [InjectedValue](InjectedValue.md) — 在脉冲高电平期间读回脉冲电平
