---
keyword: AutoGVelTh
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 352
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 1300000000
  default: 5000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 设置速度阈值（用户单位/秒），低于此值的运动数据将被排除在自动增益辨识过程之外。
---
# AutoGVelTh

**定义：**

AutoGVelTh 设置速度阈值（用户单位/秒），低于此值的运动数据将被排除在自动增益辨识过程之外。当绝对速度低于 AutoGVelTh 或绝对加速度低于 AutoGAccTh 时，该采样点将被跳过；两个阈值均满足时，采样点才会被采集。默认值为 5000。该参数为轴相关参数，以用户单位表示，保存至闪存，可随时修改。

**另请参阅：**

[AutoGAccTh](AutoGAccTh.md)、[AutoGOn](AutoGOn.md)、[AutoGMinLen](AutoGMinLen.md)
