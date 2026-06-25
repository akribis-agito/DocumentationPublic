---
keyword: UPMCalcCoeff
availability:
  standalone: []
  central-i:
  - v5
can_code: 649
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
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
summary: 重新计算 UPM 重复补偿系数，依据当前被控对象模型（PlantModel）和已配置的滤波器范围（UPMRptRange）。
---
# UPMCalcCoeff

**定义：**

UPMCalcCoeff 是一条指令，用于根据当前被控对象模型（PlantModel）和已配置的滤波器范围（UPMRptRange）（重新）计算 UPM 重复补偿系数。该指令对被控对象模型进行验证，推导逆被控对象滤波器链和范围整形（Q）滤波器，并将所得系数存储，供 UPMRptCalc 构建前馈修正时使用。在设置好被控对象模型后，以及每次更改 PlantModel 或 UPMRptRange 后，均需运行一次 UPMCalcCoeff，因为这些更改会将系数标记为需要重新计算，且在发出 UPMCalcCoeff 之前不会生效。

该指令要求使用受支持的被控对象模型：积分器类型模型（例如增益除以 s 的平方，或增益除以 s 乘以（s 加 a））——包含单一增益项且无高频极点，后面可选地跟随谐振、反谐振或二阶低通项。模型还必须恰好包含一个延迟项（系统/反馈延迟），此外还有单一增益项和积分器。延迟项数量为零或多于一个、增益项数量为零或多于一个、积分器分量数量不符，或存在任何高频极点，均导致模型不受支持。注意，延迟项的具体数值不被 UPM 重复计算所使用；仅要求模型中恰好存在一个延迟项即可被接受。

若被控对象模型缺失或不受支持，该指令将返回错误 234（至少有一个被控对象模型条目非法），系数保持无效状态，后续的 UPMRptCalc 将无法运行（此时返回错误 236，无有效被控对象模型）。UPMCalcCoeff 失败时还会设置一个独立的"计算失败"标志（与需要重新计算标志相互独立）；该标志将持续存在，直到后续成功执行 UPMCalcCoeff 后才被清除，且不阻止电机使能。该指令本身会回复 OK 或错误，可直接观察执行结果；上述两个标志反映在轴状态寄存器中（需要重新计算标志在第 26 位，计算失败标志在第 27 位）。成功后，待重新计算标志被清除。该指令不能在轴运动中或电机使能时发出。该指令为轴相关指令，不保存至闪存。

本关键字自 v5（Central-i）起可用。

**另请参阅：**

[UPMRptRange](UPMRptRange.md)、[UPMRptCalc](UPMRptCalc.md)、[UPMRptOn](UPMRptOn.md)、[UPMRptState](UPMRptState.md)
