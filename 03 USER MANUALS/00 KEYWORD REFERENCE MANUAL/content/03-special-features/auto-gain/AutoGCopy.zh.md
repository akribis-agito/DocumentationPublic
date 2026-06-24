---
keyword: AutoGCopy
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 350
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 将自动增益整定算法计算所得的增益应用至当前伺服控制器参数。
---
# AutoGCopy

**定义：**

AutoGCopy 是一个指令，用于将自动增益整定算法计算所得的增益应用至当前有效的伺服控制器参数。计算值被写入由 AutoGNumSet 选定的增益组，且仅复制由 AutoGMask 启用的各项增益（位置增益、速度增益、速度积分增益及加速度前馈增益）。复制操作仅在存在有效整定结果时执行，且仅适用于半自动模式（AutoGMode 2 或 4）——在这些模式下，增益按请求计算但不会自动应用；AutoGCopy 即为将计算结果传送至控制器的操作步骤。本参数为轴相关指令，不保存至闪存。

**另请参阅：**

[AutoGOn](AutoGOn.md)、[AutoGStatus](AutoGStatus.md)、[AutoGBW](AutoGBW.md)
