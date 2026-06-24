---
keyword: AutoGMaxLen
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 356
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
  range: null
  default: 30
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 设置自整定算法每个区域采集运动样本数量的上限。
---
# AutoGMaxLen

**定义：**

AutoGMaxLen 设置自整定算法在惯量辨识过程中每个区域采集运动样本数量的上限。样本按运动方向与指令方向分成四个区域；某区域累计样本数达到 AutoGMaxLen 后，该区域停止继续采集，其他区域继续采集。AutoGMinLen 设置各区域被认为数据充足时的样本数下限。范围 20 至 100；默认值 30。该参数为轴相关参数，保存至闪存，可随时修改。

**另请参阅：**

[AutoGMinLen](AutoGMinLen.md)、[AutoGAccTh](AutoGAccTh.md)、[AutoGOn](AutoGOn.md)
