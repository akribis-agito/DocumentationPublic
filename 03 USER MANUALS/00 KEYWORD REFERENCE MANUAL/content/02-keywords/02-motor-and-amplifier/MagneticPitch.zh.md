---
keyword: MagneticPitch
summary: 直线电机的磁极距，单位毫米，用于将速度从 counts/s 转换为 m/s 以供反电动势前馈使用。
availability:
  standalone: []
  central-i:
  - v5
can_code: 849
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
  - 1000.0
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# MagneticPitch

直线电机的磁极距，单位毫米，用于将速度从 counts/s 转换为 m/s 以供反电动势前馈使用。

## 概述

`MagneticPitch` 是**直线**电机的磁极距——电机磁轨一个磁周期的物理距离，单位为毫米。控制器仅用它将电机的机械速度与编码器计数率相关联，这在启用反电动势前馈时是必需的。它对旋转电机无影响。

它是保存至闪存的轴相关参数。该值以毫米为单位，可用范围为 0 到 1000 mm，默认值为 0。值为 0 表示该转换实际上未配置，因此在使用带反电动势前馈的直线电机时，应将其设置为电机的实际磁极距。

> 仅自 v5（Central-i）起可用。

## 工作原理

反电动势前馈预测克服电机产生电压所需的电压，该电压与机械速度成正比。对于直线电机，反电动势常数（[BEMFConst](../11-control-tuning/05-feedforwards/BEMFConst.md)）按每米每秒指定，但控制器以每秒编码器计数测量速度。`MagneticPitch` 与编码器分辨率 [EncRes](../03-encoder/01-general-settings/EncRes.md) 一起提供转换：

$$\text{speed in m/s} = \text{speed in counts/s} \cdot \frac{\text{MagneticPitch}\,[\text{mm}] \cdot 10^{-3}}{\text{EncRes}}$$

其中 [EncRes](../03-encoder/01-general-settings/EncRes.md) 为每个磁周期的计数数。其结果输入到反电动势电压项。由于它仅缩放该项，因此 `MagneticPitch` 仅在直线电机上使用反电动势前馈时才有意义；对于其他 [MotorType](MotorType.md) 设置它会被忽略（旋转电机和音圈电机使用各自的转换）。

## 示例

```text
AMagneticPitch=24       ; linear motor with a 24 mm magnetic pitch
AMagneticPitch          ; read the configured magnetic pitch (mm)
```

## 另请参阅

- [MotorType](MotorType.md) — `MagneticPitch` 仅适用于直线电机
- [EncRes](../03-encoder/01-general-settings/EncRes.md) — 每个磁周期的计数数，在转换中与 `MagneticPitch` 配对
- [BEMFConst](../11-control-tuning/05-feedforwards/BEMFConst.md) — 转换后的速度所乘的反电动势常数
