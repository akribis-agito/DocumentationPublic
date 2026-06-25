---
keyword: AutoGMinLen
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 355
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
  - 10
  - 100
  default: 15
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 设置自动增益整定算法在某区域内数据充足可进行惯量辨识前必须采集的最少运动样本数。
---
# AutoGMinLen

**定义：**

AutoGMinLen 设置自整定算法在某运动方向/指令区域内被认为数据充足、可进行惯量辨识之前，必须采集的最少运动样本数。样本按运动方向与指令方向分成四个区域；当其中至少两个区域各自累计的样本数均达到 AutoGMinLen 时，算法即认为数据充足，可计算惯量比估算值并更新增益。AutoGMaxLen 设置各区域采集样本数量的上限。范围 10 至 100；默认值 15。该参数为轴相关参数，保存至闪存，可随时修改。

**另请参阅：**

[AutoGMaxLen](AutoGMaxLen.md)、[AutoGAccTh](AutoGAccTh.md)、[AutoGVelTh](AutoGVelTh.md)
