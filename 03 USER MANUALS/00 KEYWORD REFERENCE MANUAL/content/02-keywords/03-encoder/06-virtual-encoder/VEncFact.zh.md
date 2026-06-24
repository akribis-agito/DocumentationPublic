---
keyword: VEncFact
summary: 应用于虚拟编码器源信号的缩放比值的分子。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 617
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
  - -16777215
  - 16777215
  default: 65536
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# VEncFact

应用于虚拟编码器源信号的缩放比值的分子。

## 概述

`VEncFact` 是应用于虚拟编码器源的缩放比值的分子。有效缩放因子为 `VEncFact / VEncFactDen`，它将源变量的单位映射到所发出的编码器计数上，因此输出分辨率可独立于源分辨率进行设置。当虚拟编码器启用（[VEncOn](VEncOn.md) = 1）时，它与 [VEncFactDen](VEncFactDen.md)（分母）配合使用。它是轴相关参数，保存至闪存，并可在电机使能或运动中更改。`VEncFact` 可为**负值**（范围 −16,777,215 至 16,777,215），以使输出方向相对于源反向。

## 工作原理

所发出的编码器计数按此有理因子缩放后跟踪源值：

$$\text{Output count} = \text{Source} \cdot \frac{\text{VEncFact}}{\text{VEncFactDen}}$$

在内部，固件首先将源乘以 `VEncFact` 进入 64 位“输出平面”，然后由一个跟踪控制器驱动所发出的计数，使得 `count × VEncFactDen` 跟随 `source × VEncFact`。默认值 `VEncFact = VEncFactDen = 65536` 给出单位缩放，并与使用固定 `/65536` 因子的较旧固件保持向后兼容。

选择过于激进的缩放（相对于源的移动速度而言 `VEncFact / VEncFactDen` 过大）会使虚拟编码器在一个控制周期内必须发出的脉冲数超过硬件所能产生的数量。若在电机使能时超出该限制，控制器将关闭电机并记录故障 **1066**（虚拟编码器超过每周期最大脉冲数）。

## 示例

```text
AVEncFact=65536          ; unity scale when VEncFactDen=65536
AVEncFact=-65536         ; unity scale, inverted output direction
```

## 另请参阅

- [VEncFactDen](VEncFactDen.md) —— 缩放比值的分母
- [VEncOn](VEncOn.md) —— 启用虚拟编码器
- [VEncSrc](VEncSrc.md) —— 被缩放的源变量
