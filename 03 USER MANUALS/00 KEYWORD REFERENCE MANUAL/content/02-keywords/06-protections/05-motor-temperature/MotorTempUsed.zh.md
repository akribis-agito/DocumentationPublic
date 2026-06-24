---
keyword: MotorTempUsed
summary: 选择电机温度传感器类型。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 398
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
# MotorTempUsed

选择电机温度传感器类型。

## 概述

`MotorTempUsed` 选择是否使用电机温度传感器。它作为所有电机温度逻辑的主控开关：当其为 `0` 时，固件完全跳过温度的读取/比较；当其为非零时，[MaxMotorTemp](MaxMotorTemp.md) 故障和 [StatReg](../../07-status-and-faults/StatReg.md) 告警分段将被激活。它为轴相关，且保存至闪存。

| 值 | 传感器 |
|-------|--------|
| 0 | 无——电机温度读取与保护被禁用 |
| 1 | 温度传感器输入上的 PT100 / RTD 传感器 |

> **范围说明：** 在本固件中，该关键字的范围为 `0…1`（仅 PT100/RTD）；该关键字中没有单独的“thermostat”选项。

## 工作原理

电机温度检查均受 `MotorTempUsed != 0` 测试的保护：

- **故障**——针对 [MaxMotorTemp](MaxMotorTemp.md) 的过温跳闸仅在 `MotorTempUsed ≠ 0` 时运行。
- **告警**——[StatReg](../../07-status-and-faults/StatReg.md) 第 15–16 位的告警分段仅在 `MotorTempUsed ≠ 0` 时评估；否则告警字段被清除。

该比较使用 `≠ 0` 而非 `== 1`，因此该开关纯粹为开/关。

## 示例

```text
AMotorTempUsed[1]=1    ; enable the PT100/RTD sensor on axis A
AMotorTempUsed=0       ; disable motor-temperature reading and protection
```

## 另请参阅

- [MotorTemp](MotorTemp.md) — 实测温度
- [MaxMotorTemp](MaxMotorTemp.md) — 过温故障限值
- [StatReg](../../07-status-and-faults/StatReg.md) — 电机温度告警位（15–16）
