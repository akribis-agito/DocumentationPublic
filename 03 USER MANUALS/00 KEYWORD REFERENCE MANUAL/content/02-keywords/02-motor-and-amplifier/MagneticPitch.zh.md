---
keyword: MagneticPitch
summary: 直线无刷电机每个电气周期的行程，单位为毫米。
availability:
- controller
- ci-master
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

直线无刷电机每个电气周期的行程，单位为毫米。

## 概述

CAN 849 是保存在闪存中的单轴参数，范围为 0 至 1000 mm。新版独立驱动器和 Central-i 均提供此参数。旧版独立驱动器的参数文件可能没有这一项。默认值 0 表示未配置磁极距。

对于直线无刷电机，每毫米计数 = EncRes / MagneticPitch。例如，3250 计数和 32.5 mm 对应 100 计数/mm。此换算需要正磁极距。旋转电机和音圈电机沿用原有编码器单位。

## 工作原理

反电动势前馈预测克服电机产生电压所需的电压，该电压与机械速度成正比。对于直线电机，反电动势常数（[BEMFConst](../11-control-tuning/05-feedforwards/BEMFConst.md)）按每米每秒指定，但控制器以每秒编码器计数测量速度。`MagneticPitch` 与编码器分辨率 [EncRes](../03-encoder/01-general-settings/EncRes.md) 一起提供转换：

$$\text{speed in m/s} = \text{speed in counts/s} \cdot \frac{\text{MagneticPitch}\,[\text{mm}] \cdot 10^{-3}}{\text{EncRes}}$$

其中 [EncRes](../03-encoder/01-general-settings/EncRes.md) 为每个磁周期的计数数。其结果输入到反电动势电压项。

## 示例

```text
AMagneticPitch=24       ; linear motor with a 24 mm magnetic pitch
AMagneticPitch          ; read the configured magnetic pitch (mm)
```

## 另请参阅

- [MotorType](MotorType.md) — `MagneticPitch` 仅适用于直线电机
- [EncRes](../03-encoder/01-general-settings/EncRes.md) — 每个磁周期的计数数，在转换中与 `MagneticPitch` 配对
- [BEMFConst](../11-control-tuning/05-feedforwards/BEMFConst.md) — 转换后的速度所乘的反电动势常数
