---
keyword: AutoGJm
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 351
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
  - 2147483647
  default: 3993
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 存储用户提供给自动增益整定算法的电机转动惯量值。
---
# AutoGJm

**定义：**

AutoGJm 保存用户提供给自动增益整定算法的电机转动惯量值。它与 AutoGKt 中设置的电机转矩常数共同用于估算负载与电机的惯量比，并计算速度增益和位置增益。估算所得比值通过自动增益状态报告，而非通过 AutoGJratUs 报告（AutoGJratUs 本身是用户提供的输入值）。该参数是算法的设置输入，而非算法辨识所得的值。有效范围为 1 至 2147483647，默认值为 3993。本参数为轴相关参数，保存至闪存，可随时更改。

**另请参阅：**

[AutoGBW](AutoGBW.md)、[AutoGKt](AutoGKt.md)、[AutoGJratUs](AutoGJratUs.md)、[AutoGOn](AutoGOn.md)
