---
keyword: CurrBw
summary: 电流环带宽（Hz），用于归一化磁场削弱增益。
language: zh-CN
availability:
  standalone: []
  central-i:
  - v5
can_code: 877
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range: [500, 8000]
  default: 1000
  scaling: 1
  implemented: final
last_updated: '2026-07-30'
doc_revision: '2026.07'
---

# CurrBw

电流环带宽（Hz），用于归一化磁场削弱增益。

## 概述

`CurrBw` 告知驱动器电流环有多快。它并不*设定*电流环带宽——带宽由 [CurrGain](../../11-control-tuning/06-current-control/CurrGain.md) 与 [CurrKi](../../11-control-tuning/06-current-control/CurrKi.md) 决定——而是*声明*带宽，以便磁场削弱增益能够被归一化，从而在电气时间常数差异很大的不同电机之间表现相当。

## 工作原理

驱动器按由 `CurrBw` 导出的因子对磁场削弱环路增益作除法，使得同一 [FieldWeakKi](FieldWeakKi.md) 无论电流环运行在 500 Hz 还是 2 kHz，都能产生相近的闭环响应。

> **重要：** 请将 `CurrBw` 设为电流环**实际达到**的带宽，而非期望值。若声明值有误，磁场削弱增益将相对一个并不存在的环路被归一化，其表现将与所设定的数值不符。

### 确定实际带宽

对于按抵消绕组极点原则调好的 PI 电流环，闭环带宽由增益以及电机的每相电阻与电感决定。可通过指令一个电流阶跃并测量上升时间来确认：以 Hz 为单位的带宽约为 `1 / (2π × 上升时间)`。

> **注意：** 数据表的电阻与电感通常以**线间**值给出。每相值为其一半。直接使用线间数值会使带宽估算相差一倍。

### 边界情况

- **范围：** 超出 `500…8000` Hz 的写入将被钳位。
- **电压限制：** 随转速上升，反电动势耗用母线电压，可达到的电流环带宽会下降。`CurrBw` 是单一声明值，并不描述这一变化。

## 示例

```text
ACurrBw=1000          ; 电流环实际约 1 kHz
```

## 另请参阅

- [FieldWeakKp](FieldWeakKp.md)、[FieldWeakKi](FieldWeakKi.md) — 由本参数归一化的增益
