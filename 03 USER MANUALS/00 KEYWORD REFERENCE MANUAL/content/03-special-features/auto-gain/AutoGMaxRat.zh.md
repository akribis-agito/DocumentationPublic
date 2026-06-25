---
keyword: AutoGMaxRat
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 365
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
  - 100
  - 20000
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 设置自整定算法验证辨识结果时可接受的负载与电机惯量比上限（百分比）。
---
# AutoGMaxRat

**定义：**

AutoGMaxRat 设置自整定算法验证辨识结果时可接受的负载与电机惯量比上限（以百分比表示）。每次计算周期中，估算得到的比值须满足 AutoGMinRat <= 比值 <= AutoGMaxRat，增益才会被更新；估算值超过 AutoGMaxRat 时，该周期的结果将被拒绝，不进行增益更新。在接受用户提供惯量比的模式下，所提供的比值同样会与此上下限进行校验。范围 100 至 20000；默认值 1000。该参数为轴相关参数，保存至闪存，可随时修改。

**另请参阅：**

[AutoGMinRat](AutoGMinRat.md)、[AutoGJm](AutoGJm.md)、[AutoGQualTh](AutoGQualTh.md)
