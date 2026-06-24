---
summary: 由龙门辅助编码器导出的只读速度。
keyword: GantryAuxVel
availability:
  standalone: []
  central-i:
  - v5
can_code: 677
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2251799813685248
  - 2251799813685247
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# GantryAuxVel

由龙门辅助编码器导出的只读速度。

## 概述

`GantryAuxVel` 是一个只读速度，用于**双环龙门控制**（[GantryDLoopOn](../01-general-variables/GantryDLoopOn.md) = 1）模式。它是 [GantryAuxFdbk](GantryAuxFdbk.md) 的时间导数——两个电机编码器的共模（均值）速度。该参数为轴作用域，不保存至闪存，以用户单位报告。

在双环龙门模式下，线性位置环跟随负载反馈，但内部速度环仍闭合于电机端速度以保证稳定性；`GantryAuxVel` 即为该电机端速度。速度环实际使用的值是该读数乘以双环系数（参阅[双环龙门控制概述](../04-dual-loop-gantry-control/00-overview.md)）。在单环龙门模式下，速度环直接使用共模速度，本读数不被使用。

## 工作原理

每个控制周期，控制器对 [GantryAuxFdbk](GantryAuxFdbk.md)（两个电机编码器位置（含已捕获偏置）的均值）求时间导数，得到 `GantryAuxVel`。这使内部速度环在外部位置环参考负载时，仍保持对电机的参考，从而使双环结构保持稳定。概述表中给出了各控制结构的精确单位和缩放方式。

## 示例

```text
AGantryAuxVel      ; 读取双环模式下的电机编码器（辅助）龙门速度
```

### 边界情况

- **单环龙门**（[GantryDLoopOn](../01-general-variables/GantryDLoopOn.md) = 0）——不更新。速度环直接使用 [GantryVel](../03-gantry-tuning/GantryVel.md)。
- **龙门关闭**（[GantryOn](../01-general-variables/GantryOn.md) = 0）——不更新；保持最后一次龙门开启周期的值。
- **龙门开启瞬间**——进入时强制置为 `0`，待反馈历史预热完成；第一个可用导数在一个周期后出现。
- **电机失能**——龙门对轴计算停止；若 A 轴和 B 轴的电机状态不一致，控制器将强制仍处于使能状态的轴断电，并记录 [ConFlt](../../07-status-and-faults/ConFlt.md) 代码 `1061`（另一龙门成员轴电机关闭）。
- **非主轴**——在龙门主轴以外的任何轴上读取返回 `0`。
- **平台**——仅限 v5 central-i。

## 另请参阅

- [GantryDLoopOn](../01-general-variables/GantryDLoopOn.md) — 使用本速度的双环模式
- [GantryAuxFdbk](GantryAuxFdbk.md) — 本速度导出自的辅助反馈
- [GantryFdbkSrc](GantryFdbkSrc.md) — 为线性环选择负载反馈源
