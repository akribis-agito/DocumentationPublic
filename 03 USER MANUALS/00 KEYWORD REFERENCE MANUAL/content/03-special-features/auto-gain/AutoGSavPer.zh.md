---
keyword: AutoGSavPer
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 366
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 1000
  default: 300
  scaling: 60.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 设置自动增益更新周期的重复间隔（以分钟为单位）。
---
# AutoGSavPer

**定义：**

AutoGSavPer 设置自动增益更新周期的重复间隔（以分钟为单位输入和显示）：算法运行期间，增益的重新计算和 AutoGStatus 结果的刷新频率不超过每隔该间隔一次。在全自动模式（AutoGMode 1 和 3）下，每次更新时新计算的增益将直接写入当前有效的控制组；在半自动模式（AutoGMode 2 和 4）下，增益按此间隔重新计算，但仅在之后通过 AutoGCopy 手动应用。默认值为 5 分钟。该参数为轴相关参数，保存至闪存，可随时修改。

**另请参阅：**

[AutoGOn](AutoGOn.md)、[AutoGStatus](AutoGStatus.md)、[AutoGCopy](AutoGCopy.md)
