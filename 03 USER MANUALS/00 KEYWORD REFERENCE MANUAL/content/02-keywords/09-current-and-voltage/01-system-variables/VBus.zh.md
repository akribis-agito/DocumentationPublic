---
keyword: VBus
summary: 驱动器直流母线电压测量值的只读量，单位为毫伏。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 36
attributes:
  access: ro
  scope: non-axis
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
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# VBus

驱动器直流母线电压测量值的只读量，单位为毫伏。

## 概述

`VBus` 报告驱动器直流母线电压测量值，单位为毫伏。它是一个只读状态量，反映功率级可用的供电电压。固件中每一项与母线电压相关的判定都由这同一个测量值驱动：保护限值 [MinVBus](../../06-protections/02-current-and-voltage/MinVBus.md) / [MaxVBus](../../06-protections/02-current-and-voltage/MaxVBus.md) / [MaxVBusAbs](../../06-protections/02-current-and-voltage/MaxVBusAbs.md)、再生阈值 [RegenOn](../05-regeneration/RegenOn.md) / [RegenOff](../05-regeneration/RegenOff.md)，以及在 [StatReg](../../07-status-and-faults/StatReg.md) 中报告的多级 VBus 告警。

## 工作原理

在内置（PWM）驱动器上，母线电压每 16 个控制周期为一组采样一次，原始 ADC 读数通过固定的比例因子换算为毫伏，然后施加低通滤波以抑制测量尖峰。该滤波器为一阶 IIR，时间常数约为 8 个采样点（≈8 ms）：

$$
\text{VBus}_{new} = \frac{\text{VBus}_{raw} + 7 \cdot \text{VBus}_{old}}{8}
$$

原始值到毫伏的比例因子取决于驱动器型号（每种型号具有不同的检测电阻分压器和 ADC 参考），因此同一原始计数在不同硬件上对应不同电压；正确的乘数会按产品施加。滤波后的结果即为你读取的 `VBus` 值。

在 **central-i** 远程轴上，驱动器并不拥有 ADC：母线电压通过周期性的驱动器同步报文到达，并在存储为 `VBus` 之前按逐轴校准系数和偏置进行换算。

`VBus` 更新后，控制器用它来驱动再生开关，并在 `StatReg` 中设置过压/欠压状态位；实际的禁用故障随后在保护步骤中触发。

## 示例

```text
AVBus               ; read the present bus voltage (mV)
```

## 另请参阅

- [MaxVBus](../../06-protections/02-current-and-voltage/MaxVBus.md) — 母线电压最大保护限值（使用该测量值）
- [MinVBus](../../06-protections/02-current-and-voltage/MinVBus.md) — 母线电压最小保护限值（使用该测量值）
- [RegenOn](../05-regeneration/RegenOn.md), [RegenOff](../05-regeneration/RegenOff.md) — 与 `VBus` 比较的再生阈值
- [StatReg](../../07-status-and-faults/StatReg.md) — 位 3/4/6（VBus 过压/欠压）和位 7–8（VBus 告警等级）
- [VLogic](VLogic.md) — 逻辑电源电压读数
- [DCDC](DCDC.md) — 内部逻辑电源轨测量值
