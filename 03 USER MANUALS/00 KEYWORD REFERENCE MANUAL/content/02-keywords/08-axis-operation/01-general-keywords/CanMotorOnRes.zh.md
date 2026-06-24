---
keyword: CanMotorOnRes
summary: 最近一次 CanMotorOn 使能尝试的结果码。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 413
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CanMotorOnRes

最近一次 CanMotorOn 使能尝试的结果码。

## 概述

`CanMotorOnRes` 是一个只读状态变量，保存最近一次 [CanMotorOn](CanMotorOn.md) 命令的结果。它是轴相关变量，且不保存至闪存。

值 `1` 表示**全部预检查通过**——此时使能轴（通过 `MotorOn = 1`）将被接受。任何**其他**值都是第一个失败检查的代码。这些代码来自两个来源：控制器的解释器错误编号（下方较小的“not allowed…”/硬件代码）以及当某项持续性保护会阻止使能时的控制器[故障码](../../07-status-and-faults/ConFlt.md)（基于 1000 的[控制器错误代码](../../../04-error-codes/controller-error-codes.md)）。

> 注意：尽管参数表将范围列为 `0…1`，但实时值可保存为下方任意一个原因码。`1` 是唯一的“全部正常”值——不要把 `0` 当作成功。

## 工作原理

非故障拒绝码是控制器错误编号；其余为控制器故障码。代表性取值：

| 值 | 含义 |
|---|---|
| 1 | **全部检查通过** —— 当前使能将成功。 |
| 31 | 换相 / 自动定相尚未完成。 |
| 86 | 浪涌充电继电器尚未闭合。 |
| 87 | 最近一次 [CalcFilters](../../11-control-tuning/01-general-keywords/CalcFilters.md) 失败。 |
| 102 | 环路滤波器已更改但未重新运行 [CalcFilters](../../11-control-tuning/01-general-keywords/CalcFilters.md)。 |
| 159 | Central-i 端口未激活/未连接。 |
| 175 | Central-i 设备不是驱动器。 |
| 186 | 远程驱动器继电器仍处于断开状态。 |
| 241 | 各轴 [ContCL](../../06-protections/02-current-and-voltage/ContCL.md) 之和超过硬件限制。 |
| 244 | 检测到故障的 FPGA。 |
| 245 / 250 / 268 | FPGA 版本与固件不匹配。 |
| ≥ 1000 | 某项持续性控制器故障会阻止使能（STO、编码器错误、过流、母线电压、过温……）。参见[控制器错误代码](../../../04-error-codes/controller-error-codes.md)。 |

该列表并不详尽——某些保护可能不被 `CanMotorOn` 分析，并且由于检查以固定顺序运行，只会报告**第一个**失败项。在 v5（central-i）上，环路滤波器检查不再阻止使能，因此不会产生代码 `87` 和 `102`；此时已修改/失败的滤波器状态只影响是否需要重新计算，而不影响电机使能决策。

## 示例

```text
ACanMotorOn         ; run the checks
ACanMotorOnRes      ; 1 = would enable; 31 = needs commutation; >=1000 = standing fault
```

### 边界情况

- **未运行 CanMotorOn** —— 上电时 `CanMotorOnRes = 0`。**`0` 并非“成功”**——只有 `1` 表示全部检查会通过；在调用 `CanMotorOn` 之前，应将 `0` 视为“未知”。
- **结果过期** —— 该值反映**最近一次** `CanMotorOn` 调用；检查与 `MotorOn = 1` 之间条件可能发生变化。
- **电机使能 / 仿真 / PD 驱动器** —— 在这些情况下固件会短路为 `1` 而不运行完整检查链；电机使能时不要将其作为真正的检查依据。
- **仅报告第一个失败** —— 只报告第一个失败的检查；清除一个原因可能会在下一次 `CanMotorOn` 调用时暴露另一个。
- **只读** —— 写入会被拒绝。
- **保存** —— 不可保存至闪存。

## 另请参阅

- [CanMotorOn](CanMotorOn.md) —— 产生此结果的命令
- [MotorOn](MotorOn.md) —— 实际使能电机的关键字
- [ConFlt](../../07-status-and-faults/ConFlt.md) —— 在此回传的故障码（≥ 1000）
- [控制器错误代码](../../../04-error-codes/controller-error-codes.md) —— 完整代码列表
