---
keyword: TheorCurArray
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 671
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 309
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range: null
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 存储自动电流环 PI 整定所用理论电流环响应的数组参数，用作计算代价函数的参考。
---
# TheorCurArray

**定义：**

TheorCurArray 是一个数组参数，用于存储自动电流环 PI 整定所用的理论电流环响应，作为代价函数计算的参考。它保存预期的电流阶跃响应波形，并与记录的电机电流响应进行比较；固件仅读取该数组，因此参考点必须由上位机提供。该数组最多容纳 308 个条目（索引 [1] 至 [308]）。这是一个轴相关数组参数，保存至闪存，可在任何时刻修改，包括轴运动中及电机使能时。

**另请参阅：**

[CostFunction](CostFunction.md)
