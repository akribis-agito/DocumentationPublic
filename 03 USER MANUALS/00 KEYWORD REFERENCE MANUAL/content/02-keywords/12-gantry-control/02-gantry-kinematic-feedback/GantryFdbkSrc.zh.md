---
summary: 选择用于龙门偏摆测量的编码器/反馈源。
keyword: GantryFdbkSrc
availability:
  standalone: []
  central-i:
  - v5
can_code: 673
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
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
# GantryFdbkSrc

选择双环龙门模式下用于龙门共模（线性）位置的反馈源。

## 概述

`GantryFdbkSrc` 是一个指针，用于在**双环龙门控制**（[GantryDLoopOn](../01-general-variables/GantryDLoopOn.md) = 1）激活时，选择哪个反馈变量提供龙门共模（线性）位置。写入的值为源变量的数字代码（与其他源指针关键字（如电子齿轮主轴或虚拟编码器）使用的编号相同）；默认值 `0` 表示未选择外部源。所引用的变量必须为 64 位参数；若代码超出范围（错误 `77`）、轴无效（错误 `78`）、数组索引错误（错误 `79`）、指向函数而非参数（错误 `80`）或引用非 64 位参数（错误 `305`），则写入将被验证并拒绝。该参数为轴作用域，保存至闪存，只能在电机关闭且不处于运动中时设置。

在普通（单环）龙门控制中，位置环由两个主编码器合并为共模反馈驱动（参阅 [GantryFdbk](GantryFdbk.md)）。在**双环**龙门控制中，控制器改为将线性位置环闭合于 `GantryFdbkSrc` 所指向的反馈——通常是运动台的直接负载端测量——同时仍使用两个电机编码器用于内部速度环和偏摆（差值）环。此处选择的源通常称为龙门的负载反馈；两个主电机编码器则成为辅助反馈，由 [GantryAuxFdbk](GantryAuxFdbk.md) 报告，其导数为 [GantryAuxVel](GantryAuxVel.md)。关于三种模式下各反馈和速度项的来源，请参阅[双环龙门控制概述](../04-dual-loop-gantry-control/00-overview.md)。

## 工作原理

双环龙门模式启用后，控制器每个控制周期将 `GantryFdbkSrc` 解析为所选变量的实时值，并将其（经偏移以避免线性位置在接入瞬间跳变）用作主轴的共模位置反馈。两个电机编码器继续提供差值（偏摆）反馈和速度环反馈。由于指针在写入时解析，请仅在电机关闭时修改。

## 示例

```text
AGantryFdbkSrc=<code> ; 将线性环指向所选负载端反馈源（使用该源的 CAN 代码）
AGantryFdbkSrc       ; 读取已配置的源代码
```

### 边界情况

- **写入时电机使能/处于运动中**——被拒绝（电机使能时错误 `22`，运动中时错误 `21`）。
- **单环模式**（[GantryDLoopOn](../01-general-variables/GantryDLoopOn.md) = 0）——**不查询** `GantryFdbkSrc`；线性环闭合于电机编码器共模，源指针闲置。
- **源 = 0（默认）**——未绑定负载源；若启用双环，负载反馈指针读取为零，线性环无有效反馈。请在启用龙门前配置有效源。
- **无效源代码**——写入被拒绝并返回具体错误（超出范围代码 `77`、轴无效 `78`、数组索引错误 `79`、函数而非参数 `80`，或非 64 位引用 `305`），并保留之前存储的源。
- **在错误轴上设置**——仅在主轴上查询；在其他轴上的写入被存储但被忽略。
- **接入偏移**——龙门接入时，控制器计算负载源与当前 [PosRef](../../10-motion/01-kinematics-status/PosRef.md) 之间的偏移，使报告的线性位置不发生跳变。
- **保存**——可保存至闪存；指针在启动时重新解析。
- **平台**——仅限 v5 central-i。

## 另请参阅

- [GantryDLoopOn](../01-general-variables/GantryDLoopOn.md) — 启用使用本源的双环模式
- [GantryAuxFdbk](GantryAuxFdbk.md) — 双环模式下的电机编码器反馈（与本源并行导出）
- [GantryAuxVel](GantryAuxVel.md) — 由辅助反馈导出的速度
- [GantryFdbk](GantryFdbk.md) — 龙门共模/差模反馈
- [GantryOn](../01-general-variables/GantryOn.md) — 启用龙门 MIMO 控制
