---
keyword: RmFFWLevel
summary: 应用于阻性（R i）电压前馈贡献量的百分比级别。
availability:
  standalone: []
  central-i:
  - v5
can_code: 845
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0.0
  - 200.0
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# RmFFWLevel

应用于阻性（R i）电压前馈贡献量的百分比级别。

> 从 central-i v5 起可用。

## 概述

`RmFFWLevel` 对电压前馈中的阻性项进行缩放。要在电机绕组中维持稳定电流，控制器必须施加等于电流乘以绕组电阻的电压（即 R·i 项）。控制器根据测量得到的电机电阻 [Rm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Rm.md) 和指令电流计算该电压；`RmFFWLevel` 是一个百分比，设定该计算电压中实际施加的比例。该项提供维持电流所需的稳态电压，使电流环无需通过积分器逐步建立。

阻性项同时贡献于交轴和直轴前馈输出 [VqFFW](VqFFW.md) 和 [VdFFW](VdFFW.md)，仅在 [VoltageFFWOn](VoltageFFWOn.md) 启用电压前馈时才生效。

## 工作原理

`RmFFWLevel` 的单位为百分比（%）。阻性前馈电压为建模 R·i 电压（由 [Rm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Rm.md) 和参考电流计算）乘以 `RmFFWLevel`/100：

- `0` — 无阻性前馈（默认）；
- `100` — 施加全部建模阻性电压；
- 最大值以内的其他值允许对建模项进行过补偿或欠补偿。

对于三相电机，控制器使用每相电阻：若存储的 [Rm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Rm.md) 为线间值，则在计算前内部将其折半得到每相值。

有效范围为 0 至 200（%），默认值为 0。`RmFFWLevel` 为闪存存储参数，可在电机使能或运动中设置；更改在下一个控制周期生效。仅当 `RmFFWLevel` 为 0（其最小值及默认值）时，阻性项为零。测量得到的 [Rm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Rm.md) 具有非零最小值，因此应将 `RmFFWLevel` 降至 0 来去除阻性贡献。

## 示例

```text
ARmFFWLevel=100      ; 施加全部建模阻性电压
ARmFFWLevel          ; 读取已配置的级别
ARmFFWLevel=0        ; 禁用阻性前馈项
```

## 另请参阅

- [Rm](../../../02-keywords/09-current-and-voltage/04-motor-measurement/Rm.md) — 该级别所缩放的测量电机电阻
- [LmFFWLevel](LmFFWLevel.md) — 感性（L di/dt）前馈项的级别
- [BEMFFFWLevel](BEMFFFWLevel.md) — 反电动势前馈项的级别
- [VqFFW](VqFFW.md) / [VdFFW](VdFFW.md) — 承载阻性项的前馈输出
- [VoltageFFWOn](VoltageFFWOn.md) — 电压前馈的主使能开关
