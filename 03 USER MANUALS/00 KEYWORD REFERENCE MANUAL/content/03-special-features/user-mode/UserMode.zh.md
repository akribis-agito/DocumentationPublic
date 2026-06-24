---
keyword: UserMode
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 77
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
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-25'
doc_revision: '2026.06'
language: zh-CN
summary: 用于激活控制器内特殊算法的参数；保持为 0 可避免意外启用未记录的专用功能。
---
# UserMode

UserMode 是用于激活控制器内特殊算法的参数。这些算法大多为专用目的而定制开发。
通过为 UserMode 赋予特定值，用户可以激活控制器软件中为其需求预置的特定算法。
相关客户将被告知可用且适用的 UserMode 值，以激活其特殊算法。
建议其他所有客户将此参数保持为 0，以避免意外启用未记录的特殊应用专用功能。
