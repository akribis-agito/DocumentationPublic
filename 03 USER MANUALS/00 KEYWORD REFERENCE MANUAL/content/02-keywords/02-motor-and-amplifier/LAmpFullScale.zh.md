---
keyword: LAmpFullScale
summary: 为特定内置线性驱动器产品保留的满量程电流范围选择。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 229
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# LAmpFullScale

为特定内置线性驱动器产品保留的满量程电流范围选择。

## 概述

`LAmpFullScale` 选择特定内置**线性驱动器**产品的满量程电流参考范围，以对应 10 V 输出的电流表示。它仅在 [AmpType](AmpType.md) = 4 时适用，而该设置本身就是一个保留（线性驱动器）设置——因此在标准产品上此关键字无效。

由于它是轴相关且保存至闪存，因此在配置期间设置，且无法在电机使能或运动中更改。

> [!note]
> `AmpType = 4` 是为特定线性驱动器产品保留的设置。仅在支持该设置的硬件上使用此关键字；如有疑问请联系 Agito。

## 工作原理

选择一个范围在固件中会做两件事：设置模拟缩放系数 `10000 / FullScale[mA]`（每 mA 对应的 mV，因此电流参考等于满量程时给出 10 V），并对线性驱动器硬件增益位进行编程，使驱动器的电流采样与所选范围匹配。较低的满量程范围给出更精细的电流分辨率；较高的范围允许更大的电流。

| LAmpFullScale | 10 V 对应的满量程电流 | 缩放系数 |
|---------------|--------------------|----------------|
| 0             | 0.4 A over 10 V    | 10000 / 400 = 25 mV/mA |
| 1             | 1.2 A over 10 V    | 10000 / 1200 ≈ 8.33 mV/mA |
| 2             | 3.0 A over 10 V    | 10000 / 3000 ≈ 3.33 mV/mA |

写入 `LAmpFullScale`（在 `AmpType = 4` 时）会重新计算缩放系数并重新对增益位编程。将 [AmpType](AmpType.md) 更改为 4 时，仅根据当前选择重新计算缩放系数——增益位是在 `LAmpFullScale` 本身被写入时设置的。该线性驱动器服务于两个轴；其他轴的设置不会影响它。

## 示例

```text
ALAmpFullScale=1     ; 1.2 A corresponds to full-scale (10 V) output
ALAmpFullScale      ; query the current selection
```

## 另请参阅

- [AmpType](AmpType.md) — 必须为 4（保留的线性驱动器）此关键字才适用
- [AAmpFullScale](AAmpFullScale.md) — 外部驱动器模式的满量程缩放
