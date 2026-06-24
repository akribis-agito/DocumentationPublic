---
keyword: AnomDtctOn
summary: 使能或禁用轴上的异常（碰撞）检测。
availability:
  standalone: []
  central-i:
  - v5
can_code: 778
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
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# AnomDtctOn

使能或禁用轴上的异常（碰撞）检测。

## 概述

`AnomDtctOn` 是异常检测功能的总开关。将其设为 `1` 以使能检测器，设为 `0` 以关闭它。在使能状态下，控制器在每个控制周期对配置的被监测信号进行滤波，并将其与 [AnomDtctUL](AnomDtctUL.md) / [AnomDtctLL](AnomDtctLL.md) 中保存的预期分段进行校验。当信号离开分段时，轴被停止或触发保护（参见 [AnomDtctCnfg](AnomDtctCnfg.md)）。

在使能检测器之前，请先配置检测器——监测源、滤波器、限值表。完整流程参见[类别概述](00-overview.md)。

该关键字自 v5（central-i）起可用。

## 工作原理

| 取值 | 含义 |
| --- | --- |
| 0 | 检测关闭。检测器返回空闲状态。 |
| 1 | 检测已使能。在下一次运动开始后，检测器变为活动并开始将滤波信号与分段进行比较。 |

使能并不会立即开始校验。检测器首先等待运动开始；只有当运动正在进行时，它才变为活动并沿限值表跟踪。进展由 [AnomDtctSt](AnomDtctSt.md) 元素 1（状态）报告。检测仅在电机使能时运行。

如果检测器触发，则视 [AnomDtctCnfg](AnomDtctCnfg.md) 中的停止模式而定，轴要么被带至受控停止，要么被禁用并在 [ConFlt](../../07-status-and-faults/ConFlt.md) 上置故障码 1067（检测到异常/碰撞）。

## 示例

```text
AAnomDtctOn[1]=1     ; arm anomaly detection on axis A
AAnomDtctOn[1]=0     ; disable it
AAnomDtctOn[1]       ; read the current enable state
```

## 另请参阅

- [AnomDtctCnfg](AnomDtctCnfg.md) — 监测源、滤波器极点和停止行为
- [AnomDtctSt](AnomDtctSt.md) — 实时检测器状态和滤波后的值
- [AnomDtctUL](AnomDtctUL.md) / [AnomDtctLL](AnomDtctLL.md) — 预期分段
- [ConFlt](../../07-status-and-faults/ConFlt.md) — 触发时引发的故障码 1067
