---
keyword: BEMFConst
summary: 电机反电动势常数，用于计算与速度成比例的电压前馈项。
availability:
  standalone: []
  central-i:
  - v5
can_code: 847
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
  - 10000.0
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# BEMFConst

电机反电动势常数，用于计算与速度成比例的电压前馈项。

> 从 central-i v5 起可用。

## 概述

`BEMFConst` 是电机的反电动势（BEMF）常数。运动中的电机会产生与速度成比例的电压；`BEMFConst` 是该感应电压与速度之间的比例系数，取自电机数据手册。控制器使用该常数计算电压前馈中的反电动势项——即需要提供的与速度成比例的电压，使电流环无需自行克服反电动势。反电动势项作用于交轴，并作为 [VqFFW](VqFFW.md) 的一部分输出。

`BEMFConst` 仅在 [VoltageFFWOn](VoltageFFWOn.md) 启用电压前馈且其级别 [BEMFFFWLevel](BEMFFFWLevel.md) 不为零时才起作用。默认值为 0，表示无反电动势前馈。

## 工作原理

每个控制周期，反电动势前馈电压为 `BEMFConst` 乘以 [BEMFFFWLevel](BEMFFFWLevel.md)（百分比），再乘以实际电机速度（[Vel](../../../02-keywords/10-motion/01-kinematics-status/Vel.md)）。控制器将速度从内部计数/秒换算为常数所指定的单位，并将结果转换为电流环内部电压（PWM）单位，因此输入的值即为数据手册中以物理单位表示的电机常数。

`BEMFConst` 的预期单位取决于电机类型（[MotorType](../../../02-keywords/02-motor-and-amplifier/MotorType.md)）：

| 电机类型 | BEMFConst 单位 |
|---------|--------------|
| 旋转无刷及直流有刷电机 | 伏特/RPM |
| 线性无刷电机 | 伏特/(m/s) |
| 音圈（电机） | 伏特/(m/s) |

对于三相（旋转和线性无刷）电机，数据手册中的反电动势常数通常为线间值；控制器内部将其除以 √3 得到每相值，因此输入时应填写数据手册公布的线间常数。

有效范围为 0 至 10000（上述单位），默认值为 0。`BEMFConst` 为闪存存储参数，可在电机使能或运动中设置。

## 示例

```text
ABEMFConst=0.05      ; 设置反电动势常数（例如旋转电机的 V/RPM）
ABEMFConst           ; 读取已配置的常数
```

## 另请参阅

- [BEMFFFWLevel](BEMFFFWLevel.md) — 应用于反电动势前馈项的百分比级别
- [VqFFW](VqFFW.md) — 承载反电动势项的 q 轴前馈输出
- [VoltageFFWOn](VoltageFFWOn.md) — 电压前馈的主使能开关
- [MotorType](../../../02-keywords/02-motor-and-amplifier/MotorType.md) — 选择电机类型，决定 BEMFConst 的单位
- [Vel](../../../02-keywords/10-motion/01-kinematics-status/Vel.md) — 反电动势项所正比于的实际电机速度
