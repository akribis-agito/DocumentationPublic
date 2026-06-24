---
keyword: UserDynParam
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 371
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 51
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 供特殊用户自定义处理模式使用的通用数据数组，提供 50 个元素（索引 [1] 至 [50]），运行时由活动用户模式算法读写。
---
# UserDynParam

**定义：**

UserDynParam 是供特殊用户自定义处理模式使用的通用数据数组。每个元素保存一个值，活动用户模式算法在运行时对其进行读取或写入（例如捕获的位置或传感器数据）。该数组提供 50 个元素，索引为 [1] 至 [50]。轴在运动中或电机使能时不可更改。该参数为非轴数组参数，不保存至闪存。

**另请参阅：**

[GenData](../../02-keywords/20-arrays/GenData.md)、[UserParam](../../02-keywords/20-arrays/UserParam.md)
