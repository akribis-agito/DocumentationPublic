---
keyword: AutoGStatus
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 357
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 51
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
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
summary: 只读数组（索引 1 至 50），报告该轴自动增益整定过程的工作值。
---
# AutoGStatus

**定义：**

AutoGStatus 是一个只读数组（索引 1 至 50），报告该轴自动增益整定过程的工作值。其各位置公开最新结果及中间量，包括：估计的惯量比、估计质量指标、计算所得增益（位置增益、速度增益、速度积分增益及加速度前馈增益）、最近一次计算的时间、距下次定期更新的剩余时间（以分钟为单位）、有效整定结果标志，以及算法所用的内部采样计数器。该参数为轴相关状态变量，不保存至闪存。

**另请参阅：**

[AutoGOn](AutoGOn.md)、[AutoGMode](AutoGMode.md)、[AutoGCopy](AutoGCopy.md)
