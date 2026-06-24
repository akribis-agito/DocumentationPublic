---
keyword: AutoGQualTh
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 368
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
  - 1
  - 1000
  default: 100
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 设置辨识质量指标的最大允许值（以百分比表示的估计误差，越小越好）。
---
# AutoGQualTh

**定义：**

AutoGQualTh 设置辨识质量指标的最大允许值（该指标为以百分比表示的估计误差，数值越小越好）。仅当某次计算的质量指标不超过此阈值，且估计的惯量比也在 AutoGMinRat 至 AutoGMaxRat 范围内时，该结果才被接受并纳入估计；质量指标超过阈值的结果将被丢弃。范围为 1 至 1000，默认值为 100。该参数为轴相关参数，保存至闪存，可随时修改。

**另请参阅：**

[AutoGNumSet](AutoGNumSet.md)、[AutoGMinRat](AutoGMinRat.md)、[AutoGMaxRat](AutoGMaxRat.md)
