---
keyword: ForceFiltDef
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 740
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - -2147483648
  - 2147483647
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
summary: 定义每个力环滤波器的类型及参数。
---
# ForceFiltDef

定义每个力环滤波器的类型及参数。

## 概述

`ForceFiltDef` 存储 [ForceFiltOn](ForceFiltOn.md) 所使能的两个力输出滤波器的定义。每个滤波器由最多 5 个连续数组元素描述（一个类型码加最多四个参数）：

| 滤波器（N） | 描述       | 数组元素 |
|------------|------------|----------------|
| 1          | 力滤波器 1 | `ForceFiltDef[1]` … `ForceFiltDef[5]`   |
| 2          | 力滤波器 2 | `ForceFiltDef[6]` … `ForceFiltDef[10]`  |

对于每个滤波器，第一个元素为**滤波器类型**，后续四个为**参数 1 至 4**，其含义取决于类型。

这些滤波器**仅**用于标准力控制（[ForcePIVOn](ForcePIVOn.md) = 0）；在 force-over-PIV 控制（`ForcePIVOn = 1`）中无效。

## 工作原理

每个 5 元素块的布局如下：

| 偏移 | 含义 |
|--------|---------|
| 第 1 个 | 滤波器类型（`0` = 无，`1` = 一阶低通，`2` = 二阶低通，`3` = 含一个零点的二阶低通，`4`/`5` = 一/二阶超前-滞后，`6`/`7` = 按相位的一/二阶超前-滞后，`8` = 陷波，`9` = 复合超前-滞后） |
| 第 2–5 个 | 参数 1 至 4（频率单位为 Hz/100，阻尼比单位为 %，相位单位为度，陷波深度单位为 dB——取决于类型） |

每个滤波器实现为二阶（双二次）节。力滤波器 1 和力滤波器 2 串联作用于力 PID 加前馈输出，经 [ForceFiltOn](ForceFiltOn.md) 使能后形成电流参考值。写入 `ForceFiltDef`（及对应的 [ForceFiltOn](ForceFiltOn.md)）后，需运行 [CalcFilters](../01-general-keywords/CalcFilters.md) 以重新计算系数。

写入 `ForceFiltDef`（或 `ForceFiltOn`）仅将定义标记为已修改；新系数仅在下次运行 `CalcFilters` 后才生效。在此之前，电机无法使能——`MotorOn` 请求将被拒绝并报错 `102`（"Can't enable motor if filters were modified and CalcFilters was not executed"）。若已使能滤波器的定义无效——类型码不支持，或参数超出允许范围——`CalcFilters` 将失败并报告力滤波器 1 的错误 `325` 或力滤波器 2 的错误 `326`（"Out of range filter definitions, at Force filter number N"），电机将持续被阻止，直至计算出有效定义为止。

完整的按类型分类的参数定义、传递函数及单位请参见附录：[可定制滤波器（FiltDef）](../../../06-appendix/customisable-filter-filtdef.md)。

## 示例

```text
; Force filter 1 as a second-order low-pass at 500 Hz, damping 0.71
AForceFiltDef[1]=2      ; type: second-order low-pass
AForceFiltDef[2]=50000  ; cutoff 500 Hz (Hz/100)
AForceFiltDef[3]=71     ; damping ratio 0.71 (%)
AForceFiltOn[1]=1       ; enable force filter 1
ACalcFilters            ; recompute filter coefficients
```

## 版本间变化

在 **v4** 中，`ForceFiltDef` 只能在电机关闭且不在运动中时修改。在 **v5（central-i）** 中，也可在电机使能及运动中修改。

## 另见

- [ForceFiltOn](ForceFiltOn.md) — 使能此处定义的每个力滤波器
- [ForcePIVOn](ForcePIVOn.md) — 这些滤波器仅在本参数为 0 时有效
- [CalcFilters](../01-general-keywords/CalcFilters.md) — 修改后重新计算滤波器系数
- 附录：[可定制滤波器（FiltDef）](../../../06-appendix/customisable-filter-filtdef.md)
