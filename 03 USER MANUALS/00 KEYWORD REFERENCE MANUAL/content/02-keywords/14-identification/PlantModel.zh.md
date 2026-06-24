---
keyword: PlantModel
summary: 已辨识的被控对象模型系数数组，供自整定和速度滤波器设计使用。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 558
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 81
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-27'
doc_revision: '2026.06'
language: zh-CN
---
# PlantModel

已辨识的被控对象模型系数数组，供自整定和速度滤波器设计使用。

## 概述

`PlantModel` 存储供自整定和速度滤波器设计算法使用的已辨识被控对象模型系数。这些系数描述了通过辨识过程确定的轴的机械传递函数（参见 [CalcIden](CalcIden.md) 和 [IdenResults](IdenResults.md)）。该关键字为轴相关数组，保存至闪存，可随时更改。

## 示例

```text
APlantModel         ; read all identified plant-model coefficients
APlantModel[1]      ; read the first coefficient
```

## 另请参阅

- [CalcIden](CalcIden.md) — 运行正弦扫频计算
- [IdenResults](IdenResults.md) — 输入模型的原始输入/输出关系
