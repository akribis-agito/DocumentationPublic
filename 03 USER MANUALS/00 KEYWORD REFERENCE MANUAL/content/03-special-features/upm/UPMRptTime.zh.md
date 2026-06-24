---
keyword: UPMRptTime
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 561
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 65536
  default: 0
  scaling: 65.536
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 设置 UPM 重复补偿算法的记录"尾部"时间（毫秒）。
---
# UPMRptTime

**定义：**

UPMRptTime 设置 UPM 重复补偿算法的记录"尾部"时间，单位为毫秒：即运动本身结束后，控制器继续记录学习周期位置误差和电流参考的额外时间。当重复运动开始时，该尾部值被加载为倒计时；倒计时仅在轴不再运动时递减，倒计时结束后首次学习周期停止，已记录的周期长度固定为截至该点所采集的采样数量。因此较长的尾部可将更多的运动后整定过程纳入已学习修正中。默认值为 0（无尾部），取值范围为 0 ms 至 1000 ms，并受重复补偿存储数组可用空间进一步限制。该值在内部以控制采样数保存，并与您设置的毫秒值进行相互转换。轴在运动中时不可更改；电机使能时可更改。该参数为轴相关参数，保存至闪存。

**另请参阅：**

[UPMRptOn](UPMRptOn.md)、[UPMRptCalc](UPMRptCalc.md)、[UPMRptMotion](UPMRptMotion.md)
