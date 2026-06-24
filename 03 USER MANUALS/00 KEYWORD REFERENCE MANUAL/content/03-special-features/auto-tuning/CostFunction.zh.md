---
keyword: CostFunction
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 672
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 评估自动电流环 PI 整定所用的代价函数指标。
---
# CostFunction

**定义：**

CostFunction 评估自动电流环 PI 整定所用的代价函数指标。它根据理论电流响应（TheorCurArray）与记录的电机电流响应之间的加权均方根误差加上超调惩罚，计算出一个标量分数；整定过程在搜索电流环 PI 增益时将最小化该分数。这是一个轴相关指令，不保存至闪存。

**另请参阅：**

[TheorCurArray](TheorCurArray.md)
