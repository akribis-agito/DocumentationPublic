---
keyword: InjectCurrAmp
summary: 电流指令注入的幅值，单位为 mA。
availability:
- controller
- ci-master
can_code: 114
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 16000
  default: 533.3333333333334
  scaling: 1.0
  implemented: final
overrides:
  ci-master:
    range:
    - 0
    - 64000
    default: 2133.3333333333335
  agc300-et:
    range:
    - 0
    - 4000
    default: 133.33333333333334
  agc301-et:
    range:
    - 0
    - 4000
    default: 133.33333333333334
  agc301-et-bioxtreme:
    range:
    - 0
    - 4000
    default: 133.33333333333334
  agd200-et-2d01:
    range:
    - 0
    - 4000
    default: 133.33333333333334
  agd200-et-2d02:
    range:
    - 0
    - 8000
    default: 266.6666666666667
  agd301-et-2d01:
    range:
    - 0
    - 4000
    default: 133.33333333333334
  agd301-et-2d02:
    range:
    - 0
    - 8000
    default: 266.6666666666667
  agd301-et-2d09:
    range:
    - 0
    - 25500
    default: 850.0
  agd155-af-2a06:
    range:
    - 0
    - 25500
    default: 850.0
  agd155-af-2a10:
    range:
    - 0
    - 28500
    default: 950.0
  agd155-ec:
    range:
    - 0
    - 25500
    default: 850.0
  agd155-ec-var34:
    range:
    - 0
    - 28500
    default: 950.0
  agd155-ec-var34-3:
    range:
    - 0
    - 42500
    default: 1416.6666666666667
  agd156-ec:
    range:
    - 0
    - 12726
    default: 424.2
  agd101-ec-34a:
    range:
    - 0
    - 28280
    default: 942.6666666666666
  agd101-ec-17a:
    range:
    - 0
    - 14140
    default: 471.3333333333333
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# InjectCurrAmp

电流指令注入的幅值，单位为 mA。

## 概述

`InjectCurrAmp` 是在电流指令处注入波形时的幅值，单位为 mA。仅当 [InjectPoint](InjectPoint.md) 选择电流指令时（`InjectPoint = 0`）生效。波形形状由 [InjectType](InjectType.md) 选择；可通过 [InjectCurrDC](InjectCurrDC.md) 叠加直流偏置。

## 工作原理

该值设定波形在电流指令处所能达到的峰值幅度：正弦波在 +`InjectCurrAmp` 与 −`InjectCurrAmp` 之间摆动，方波和 PRBS 在这两个电平之间切换，脉冲在脉冲接通时间内保持 +`InjectCurrAmp`。在**直接**模式（[InjectType](InjectType.md) = 1、3、5、6 或 8）下，该波形（加上 [InjectCurrDC](InjectCurrDC.md) 偏置）成为电流指令，替代速度环输出；在**叠加**模式下，它叠加在现有电流指令之上。当前电平可通过 [InjectedValue](InjectedValue.md) 读回。幅值在下一个注入采样点生效，因此可在注入过程中更改。

## 示例

```text
AInjectCurrAmp=2133      ; 2133 mA 注入幅值（默认）
AInjectCurrAmp          ; 查询当前注入幅值
```

## 另请参阅

- [InjectPoint](InjectPoint.md) — 电流指令注入时必须为 0
- [InjectType](InjectType.md) — 选择波形形状及直接/叠加模式
- [InjectCurrDC](InjectCurrDC.md) — 电流注入的直流偏置
- [InjectedValue](InjectedValue.md) — 读回当前注入值
