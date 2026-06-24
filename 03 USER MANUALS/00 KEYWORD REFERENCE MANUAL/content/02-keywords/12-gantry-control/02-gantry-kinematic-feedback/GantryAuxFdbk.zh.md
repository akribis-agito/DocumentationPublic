---
summary: 只读辅助编码器反馈，用于测量龙门偏摆。
keyword: GantryAuxFdbk
availability:
  standalone: []
  central-i:
  - v5
can_code: 674
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
# GantryAuxFdbk

只读辅助编码器反馈，用于测量龙门偏摆。

## 概述

`GantryAuxFdbk` 是一个只读反馈，用于**双环龙门控制**（[GantryDLoopOn](../01-general-variables/GantryDLoopOn.md) = 1）模式。在该模式下，共模（线性）位置环闭合于由 [GantryFdbkSrc](GantryFdbkSrc.md) 选择的负载反馈，两个电机编码器降级为*辅助*角色：其共模（均值）位置在此报告为 `GantryAuxFdbk`。它是 [GantryFdbk](GantryFdbk.md)（负载端）的电机端对应量，内部速度环闭合于其导数 [GantryAuxVel](GantryAuxVel.md)，并按双环系数缩放。该参数为轴作用域，不保存至闪存，以用户单位报告。

在单环龙门模式下，该值不被使用（电机编码器通过 [GantryFdbk](GantryFdbk.md) 直接构成线性反馈）。

## 工作原理

当双环龙门模式启用时，控制器计算与单环龙门反馈相同的共模量——两个电机编码器位置（含已捕获的 [GantryOffset](GantryOffset.md)）的均值——但将其路由至 `GantryAuxFdbk` 而非位置环。位置环随后跟随来自 [GantryFdbkSrc](GantryFdbkSrc.md) 的负载反馈。环路所使用的速度是该辅助反馈的时间导数，并按双环系数缩放；完整的信号来源表请参阅[双环龙门控制概述](../04-dual-loop-gantry-control/00-overview.md)。

## 示例

```text
AGantryAuxFdbk     ; 读取双环模式下的电机编码器（辅助）龙门反馈
```

### 边界情况

- **单环龙门**（[GantryDLoopOn](../01-general-variables/GantryDLoopOn.md) = 0）——不更新。电机编码器均值直接作为主轴的 [GantryFdbk](GantryFdbk.md) 报告。
- **龙门关闭**（[GantryOn](../01-general-variables/GantryOn.md) = 0）——不更新。保持最后一次龙门开启周期的值，直至下次龙门开启。
- **电机失能**——该对轴的龙门计算停止；若 A 轴和 B 轴的电机状态不一致，控制器将强制仍处于使能状态的轴断电，并记录 [ConFlt](../../07-status-and-faults/ConFlt.md) 代码 `1061`（另一龙门成员轴电机关闭）。
- **非主轴**——在龙门主轴以外的任何轴上读取返回 `0`。
- **平台**——仅限 v5 central-i；v4 或独立模式不可用。

## 另请参阅

- [GantryDLoopOn](../01-general-variables/GantryDLoopOn.md) — 使用本反馈的双环模式
- [GantryFdbkSrc](GantryFdbkSrc.md) — 线性环的负载反馈源
- [GantryAuxVel](GantryAuxVel.md) — 由本反馈导出的速度
- [GantryFdbk](GantryFdbk.md) — 负载端共模/差模龙门反馈
- [GantryOffset](GantryOffset.md) — 折叠入共模计算的 A/B 偏置
