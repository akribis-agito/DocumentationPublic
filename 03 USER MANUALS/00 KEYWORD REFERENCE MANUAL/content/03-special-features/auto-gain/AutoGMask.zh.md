---
keyword: AutoGMask
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 370
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 指定自动增益算法允许更新哪些伺服增益参数的数组掩码。
---
# AutoGMask

**定义：**

AutoGMask 是一个数组，用于指定自动增益算法允许更新的伺服增益参数。该数组有四个可用元素，索引从 [1] 开始：元素 [1] 为位置增益，元素 [2] 为速度增益，元素 [3] 为速度积分增益，元素 [4] 为加速度前馈增益。每个元素设为 1 表示允许写入对应增益，设为 0 表示保持不变。该掩码在全自动模式下自动下载增益时以及在半自动模式下使用 AutoGCopy 应用计算所得增益时均会生效。每个元素的默认值为 1。本参数为轴相关数组参数，保存至闪存，可随时更改。

**另请参阅：**

[AutoGCopy](AutoGCopy.md)、[AutoGOn](AutoGOn.md)、[AutoGBW](AutoGBW.md)
