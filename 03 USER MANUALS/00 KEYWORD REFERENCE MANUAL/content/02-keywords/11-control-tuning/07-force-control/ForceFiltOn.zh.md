---
keyword: ForceFiltOn
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 741
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    ok_in_motion: true
    ok_motor_on: true
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 使能两个力环输出滤波器中的各个滤波器。
---
# ForceFiltOn

使能两个力环输出滤波器中的各个滤波器。

## 概述

`ForceFiltOn` 使能或旁路两个力输出滤波器。每个元素控制一个滤波器：`ForceFiltOn[Index] = 1` 使能该滤波器，`ForceFiltOn[Index] = 0` 旁路该滤波器。默认值均为 `0`（均旁路）。

| 索引 | 描述       |
|-------|----------------|
| 1     | 力滤波器 1 |
| 2     | 力滤波器 2 |

这些滤波器**仅**用于标准力控制（[ForcePIVOn](ForcePIVOn.md) = 0）；在 force-over-PIV 控制（`ForcePIVOn = 1`）中无效。

## 工作原理

在标准力控制中，力 PID 输出与前馈项（[ForceFFW](ForceFFW.md) 和速度补偿 [ForceVelFFW](ForceVelFFW.md)）之和依次经过力滤波器 1 和力滤波器 2；第二个滤波器的输出即为电流参考值。被旁路的滤波器信号直接通过，不作处理。

每个滤波器实现为二阶（双二次）节，其类型和参数由 [ForceFiltDef](ForceFiltDef.md) 定义。修改 `ForceFiltOn`（或 `ForceFiltDef`）后，需运行 [CalcFilters](../01-general-keywords/CalcFilters.md) 以重新计算系数。

修改 `ForceFiltOn` 仅将滤波器标记为已修改；变更仅在下次运行 `CalcFilters` 后才生效。在此之前，电机无法使能——`MotorOn` 请求将被拒绝并报错 `102`（"Can't enable motor if filters were modified and CalcFilters was not executed"）。若使能了 [ForceFiltDef](ForceFiltDef.md) 定义无效的滤波器（类型码不支持或参数超出允许范围），`CalcFilters` 将失败并报告力滤波器 1 的错误 `325` 或力滤波器 2 的错误 `326`，电机将持续被阻止，直至计算出有效定义为止。

## 示例

```text
AForceFiltOn[1]=1       ; enable force filter 1
AForceFiltOn[2]=0       ; bypass force filter 2
ACalcFilters            ; recompute filter coefficients
```

## 版本间变化

在 **v4** 中，`ForceFiltOn` 只能在电机关闭且不在运动中时修改。在 **v5（central-i）** 中，也可在电机使能及运动中修改。

## 另请参阅

- [ForceFiltDef](ForceFiltDef.md) — 定义每个力滤波器的类型及参数
- [ForcePIVOn](ForcePIVOn.md) — 这些滤波器仅在本参数为 0 时有效
- [CalcFilters](../01-general-keywords/CalcFilters.md) — 修改后重新计算滤波器系数
- [Force control](00-overview.md) — 力环结构概述
