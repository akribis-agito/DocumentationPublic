---
keyword: UPMRptRange
availability:
  standalone: []
  central-i:
  - v5
can_code: 554
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 30
  - 500
  default: 124
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 设置 UPM 重复补偿滤波器的频率范围（Hz）。
---
# UPMRptRange

**定义：**

UPMRptRange 设置 UPM 重复补偿滤波器的频率范围，单位为 Hz。它定义了已学习修正值的整形带宽：范围内的误差分量得到修正，范围以上的分量被衰减；因此较高的取值使补偿作用于更快的误差特征，较低的取值则使修正更平滑、更保守。该值为计算修正时所应用的整形（Q）滤波器的截止频率，可用范围为 30 Hz 至 500 Hz，默认值为 124 Hz。UPMRptRange 是旧参数 UPMRptLevel（以百分比表示相同设置）的重命名继承者；现在直接以 Hz 为单位指定频率。该参数为轴相关参数，保存至闪存，可在运动中及电机使能时更改。

更改 UPMRptRange（与更改被控对象模型类似）不会立即生效：它通过置位 [StatReg] 第 26 位（滤波器/被控对象模型已修改指示）将 UPM 重复补偿系数标记为需要重新计算。之后需运行 UPMCalcCoeff 以根据新范围重新计算系数，再进行下一次 UPMRptCalc；UPMCalcCoeff 成功后会清除 [StatReg] 第 26 位。该待处理状态仅作为指示呈现，不会阻止电机使能。

该关键字名称自 v5（central-i）起使用；在 v4 上，相同设置对应 UPMRptLevel（以百分比表示）。

**另请参阅：**

[UPMCalcCoeff](UPMCalcCoeff.md)、[UPMRptOn](UPMRptOn.md)、[UPMRptCalc](UPMRptCalc.md)、[UPMRptLevel](UPMRptLevel.md)、[UPMRptState](UPMRptState.md)
