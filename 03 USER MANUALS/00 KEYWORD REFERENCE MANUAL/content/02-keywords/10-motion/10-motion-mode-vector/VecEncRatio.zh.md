---
keyword: VecEncRatio
summary: 每轴编码器分辨率补偿比，以 1/256 为缩放单位（256 表示比值为 1）。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 632
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 256
  - 25600
  default: 256
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# VecEncRatio

每轴编码器分辨率补偿比，以 1/256 为缩放单位（256 表示比值为 1）。

## 概述

`VecEncRatio` 用于补偿参与协调矢量运动（[MotionMode](../02-motion-configuration/MotionMode.md) = 16）的各轴之间的编码器分辨率差异，即使成员轴的每单位计数数不同，也能保持合成路径的几何精度。它是分子/分母对 [VecEncFactNu](VecEncFactNu.md) / [VecEncFactDn](VecEncFactDn.md) 所提供的同一补偿的单值形式。该参数保存至闪存，运动中不可修改。

## 工作原理

该值以 1/256 为比例因子解释：`256` 表示比值为 1（默认值，无缩放），较大的值给出按比例放大的比——例如 `260` 表示比值为 260/256。范围为 `256`（比值为 1）到 `25600`（比值为 100）。

> 在当前固件版本中，此比值按轴存储，但不应用于矢量路径：矢量运动纯粹根据路径几何计算各成员轴的运动，因此 `VecEncRatio` 目前不影响合成运动。后续固件以有理对 [VecEncFactNu](VecEncFactNu.md) / [VecEncFactDn](VecEncFactDn.md) 替代它，以分子/分母形式表达同一比值；该对参数同样被存储（并由此计算内部乘数），但也尚未应用于路径。在依赖矢量编码器分辨率补偿之前，请针对您的固件版本验证实际行为。

## 示例

```text
AVecEncRatio=256       ; ratio of 1 on axis A (default, no scaling)
AVecEncRatio=260       ; ratio of 260/256
```

## 另请参阅

- [VecEncFactNu](VecEncFactNu.md) / [VecEncFactDn](VecEncFactDn.md) — 同一比值的分子/分母形式
- [VecMemberAxes](VecMemberAxes.md) — 构成矢量组的各轴
- [VecSpeed](VecSpeed.md) — 指令合成速度
