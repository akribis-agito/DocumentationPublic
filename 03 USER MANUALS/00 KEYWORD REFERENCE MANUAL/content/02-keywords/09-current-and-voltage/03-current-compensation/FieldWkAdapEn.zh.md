---
keyword: FieldWkAdapEn
summary: 随转速上升，按定子磁链比例缩放磁场削弱增益。
language: zh-CN
availability:
  standalone: []
  central-i:
  - v5
can_code: 876
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
  range: [0, 1]
  default: 0
  scaling: 1
  implemented: final
last_updated: '2026-07-30'
doc_revision: '2026.07'
---

# FieldWkAdapEn

随转速上升，按定子磁链比例缩放磁场削弱增益。

## 概述

磁场削弱环路的理想增益在整个速度范围内并非恒定——随着磁场被削弱，电压误差与纠正它所需 d 轴电流之间的关系会发生变化。`FieldWkAdapEn` 使驱动器按当前定子磁链与未削弱值之比来缩放两个环路增益。

## 工作原理

当 `FieldWkAdapEn=1` 时，驱动器由 d 轴与 q 轴电流及实际电感计算定子磁链，并按其与未削弱磁链之比的平方缩放 [FieldWeakKp](FieldWeakKp.md) 与 [FieldWeakKi](FieldWeakKi.md)。该比值以 1 为上界，因此自适应项只会降低增益。

在区域 2 中，则改为对 q 轴限值施加单独的线性递减。

> **注意：** 这是该功能设计的工作模式。若关闭自适应缩放，在磁场削弱范围内某一点调好的增益，在该范围的其他位置可能过于激进或过于迟缓。

### 边界情况

- **禁用时无效：** 除非 [FieldWeakEn](FieldWeakEn.md) 为 1，否则被忽略。
- **依赖电感：** 磁链计算使用驱动器推导出的 d 轴与 q 轴电感，因此 [Lm](../04-motor-measurement/Lm.md) 必须设置正确，缩放才有意义。

## 示例

```text
AFieldWkAdapEn=1
```

## 另请参阅

- [FieldWeakEn](FieldWeakEn.md)、[FieldWeakKp](FieldWeakKp.md)、[FieldWeakKi](FieldWeakKi.md)
