---
keyword: GantrySwapSrc
summary: 选择用于决定龙门双环与单环控制在线切换的位置源。
availability:
  standalone: []
  central-i:
  - v5
can_code: 754
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# GantrySwapSrc

选择用于决定龙门双环与单环控制在线切换的位置源。

## 概述

`GantrySwapSrc` 是一个指针，用于选择控制器在**双环龙门**中在线切换双环（负载反馈）和单环（电机编码器）控制时所监视的位置。写入的值为源变量的数字代码，与其他龙门源指针关键字（[GantryFdbkSrc](../02-gantry-kinematic-feedback/GantryFdbkSrc.md)、[GantryMapSrc](GantryMapSrc.md)）使用相同的编号方案；默认值 `0` 表示不选择任何源。

当龙门配置为双环控制（[GantryDLoopOn](GantryDLoopOn.md) = 1）且启用了在线切换时，控制器每个周期读取该源的实时值，并用其决定线性位置环应闭合哪个反馈：在配置的位置窗口内使用负载（双环）反馈；超出该窗口则回退至电机编码器（单环）反馈。这使龙门能够仅在负载测量有效的行程范围内使用高精度负载测量，在其他位置回退到电机编码器——且无位置跳变。

该参数为轴范围（在龙门主轴上配置），保存至闪存，可在电机使能时修改，但不可在运动中修改。适用于 central-i（v5）。

## 工作原理

写入时 `GantrySwapSrc` 被解析为目标变量的指针，使控制器能够在每个控制周期以低成本读取实时源值。当龙门以双环控制和在线切换运行时，每个周期控制器将源值与位置窗口进行比较：

- **源值在窗口内** — 线性位置环使用 [GantryFdbkSrc](../02-gantry-kinematic-feedback/GantryFdbkSrc.md) 选择的负载（双环）反馈；电机编码器保持为辅助/速度反馈（[GantryAuxFdbk](../02-gantry-kinematic-feedback/GantryAuxFdbk.md) / [GantryAuxVel](../02-gantry-kinematic-feedback/GantryAuxVel.md)）。
- **源值在窗口外** — 线性环回退到电机编码器反馈（单环行为）。

从单环切换到双环时，控制器捕获两个反馈之间的偏置，使报告的线性位置在切换时刻不发生阶跃。位置窗口本身及切换的主使能由独立的双编码器切换关键字配置；`GantrySwapSrc` 仅选择*哪个位置*被与该窗口进行比较。

## 示例

```text
AGantrySwapSrc=<code>  ; 监视选定的位置源以进行双环/单环切换（使用该源的 CAN 代码）
AGantrySwapSrc        ; 读取已配置的源代码
```

### 边界情况

- **运动中写入** — 被拒绝（`NOMOTN`）；可在电机使能时修改。
- **源 = 0（默认）** — 未绑定任何源；在线切换无法测试，龙门保持在已配置的环路模式。
- **无效或类型错误的源** — 若代码不是有效的关键字 CAN 代码、指向的是指令而非可读变量、轴或数组索引有误，或不是 64 位（int64）源，则写入经验证后被拒绝并返回错误。仅在写入通过验证后才更新指针，因此被拒绝的写入将保留原有源。
- **切换未启用** — `GantrySwapSrc` 被存储，但除非同时启用双环龙门控制和在线切换，否则无效果。
- **写入错误轴** — 仅在龙门主轴上查询；写入其他轴时虽被存储但被忽略。
- **保存** — 可保存至闪存；指针在启动时重新解析。
- **平台** — 仅适用于 v5 central-i。

## 另请参阅

- [GantryDLoopOn](GantryDLoopOn.md) — 启用此切换所在的双环龙门模式
- [GantryFdbkSrc](../02-gantry-kinematic-feedback/GantryFdbkSrc.md) — 切换窗口内使用的负载反馈
- [GantryAuxFdbk](../02-gantry-kinematic-feedback/GantryAuxFdbk.md) / [GantryAuxVel](../02-gantry-kinematic-feedback/GantryAuxVel.md) — 窗口外使用的电机编码器反馈
- [GantryOn](GantryOn.md) — 启用龙门 MIMO 控制
