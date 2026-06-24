---
keyword: AutoGJratUs
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 363
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
  - -50
  - 20000
  default: 140
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 设置用户提供的负载与电机惯量比（百分比），供自动增益整定算法使用。
---
# AutoGJratUs

**定义：**

AutoGJratUs 设置用户提供的负载与电机惯量比（以百分比表示），自动增益整定算法将以此值替代其自身估算值使用。在采用用户惯量比的自动增益模式下，增益依据总惯量（电机惯量 × (1 + AutoGJratUs / 100)）计算，用户惯量比也作为最终比值上报。用户惯量比仅在位于 AutoGMinRat 至 AutoGMaxRat 窗口范围内时才被采用；否则本周期不更新参数。有效范围为 -50 至 20000，默认值为 140。本参数为轴相关参数，保存至闪存，可随时更改。

**另请参阅：**

[AutoGJm](AutoGJm.md)、[AutoGBW](AutoGBW.md)、[AutoGOn](AutoGOn.md)
