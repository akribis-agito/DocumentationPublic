---
keyword: UPMRptOn
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 559
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range: null
    default: null
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 为下一次运动请求 UPM 重复（周期性）运动补偿。
---
# UPMRptOn

**定义：**

UPMRptOn 为下一次运动请求 UPM 重复（周期性）运动补偿。激活后，控制器自适应一个前馈修正以消除随每次运动周期重复出现的位置误差。该请求有三个取值：0 = 无，1 = 首次（捕获单次学习过程），2 = 重复（应用重复补偿）。该请求在下一次运动开始时被消耗：控制器设置对应的重复状态，然后将 UPMRptOn 清零，因此每次需要使用该功能的运动前都必须重新设置。轴在运动中时不可更改；电机使能时可更改。该参数为轴相关参数，不保存至闪存。

**另请参阅：**

[UPMRptCalc](UPMRptCalc.md)、[UPMRptLevel](UPMRptLevel.md)、[UPMRptState](UPMRptState.md)、[UPMRptTime](UPMRptTime.md)
