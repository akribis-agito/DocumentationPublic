---
keyword: InjectCurrDC
summary: 直接模式下叠加到电流指令注入的直流偏置，单位为 mA。
availability:
- controller
- ci-master
can_code: 126
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
  - -8000.0
  - 8000.0
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  ci-master:
    range:
    - -32000.0
    - 32000.0
  agc300-et:
    range:
    - -2000.0
    - 2000.0
  agc301-et:
    range:
    - -2000.0
    - 2000.0
  agc301-et-bioxtreme:
    range:
    - -2000.0
    - 2000.0
  agd200-et-2d01:
    range:
    - -2000.0
    - 2000.0
  agd200-et-2d02:
    range:
    - -4000.0
    - 4000.0
  agd301-et-2d01:
    range:
    - -2000.0
    - 2000.0
  agd301-et-2d02:
    range:
    - -4000.0
    - 4000.0
  agd301-et-2d09:
    range:
    - -12750.0
    - 12750.0
  agd155-af-2a06:
    range:
    - -12750.0
    - 12750.0
  agd155-af-2a10:
    range:
    - -14250.0
    - 14250.0
  agd155-ec:
    range:
    - -12750.0
    - 12750.0
  agd155-ec-var34:
    range:
    - -14250.0
    - 14250.0
  agd155-ec-var34-3:
    range:
    - -21250.0
    - 21250.0
  agd156-ec:
    range:
    - -6363.0
    - 6363.0
  agd101-ec-34a:
    range:
    - -14140.0
    - 14140.0
  agd101-ec-17a:
    range:
    - -7070.0
    - 7070.0
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# InjectCurrDC

直接模式下叠加到电流指令注入的直流偏置，单位为 mA。

## 概述

`InjectCurrDC` 是注入电流值的直流偏置，单位为 mA。仅当 [InjectPoint](InjectPoint.md) 选择电流指令时（`InjectPoint = 0`）生效。它将 [InjectCurrAmp](InjectCurrAmp.md) 所设定的波形偏移到非零电流水平，使注入电流在直流偏置附近而非零点附近振荡。

该偏置仅在**直接** [InjectType](InjectType.md) 模式下被添加到电流指令；在叠加模式下，波形叠加在现有指令之上，不含直流偏置。控制器仅在电机换相/定相完成后才应用直流项，以避免产生不受控的稳态电流。在 v5 中，电机未完成定相时仍会注入波形，但不含偏置；在 v4 中，电流指令注入仅在电机完成定相后运行，因此未定相期间波形和偏置均不施加。

## 示例

```text
AInjectCurrDC=500        ; 500 mA 直流偏置
AInjectCurrDC=0          ; 无偏置（默认）
AInjectCurrDC           ; 查询当前直流偏置
```

## 另请参阅

- [InjectPoint](InjectPoint.md) — 电流指令注入时必须为 0
- [InjectType](InjectType.md) — 选择波形及直接/叠加模式
- [InjectCurrAmp](InjectCurrAmp.md) — 电流注入的幅值
