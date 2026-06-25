---
summary: 启用双环（位置 + 偏摆）龙门控制模式。
keyword: GantryDLoopOn
availability:
  standalone: []
  central-i:
  - v5
can_code: 675
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# GantryDLoopOn

启用双环（位置 + 偏摆）龙门控制模式。

## 概述

`GantryDLoopOn` 选择龙门共模（线性）位置环是基于两个电机编码器还是独立的负载端反馈来闭环：

| 值 | 模式 | 线性位置环闭合于 |
|:-----:|------|-------------------------------|
| 0 | 单环龙门（默认） | 两个电机编码器的共模（均值）。 |
| 1 | 双环龙门 | 由 [GantryFdbkSrc](../02-gantry-kinematic-feedback/GantryFdbkSrc.md) 选择的反馈（通常为直接负载测量），两个电机编码器作为辅助/速度反馈。 |

该参数按轴设置，保存至闪存，且只能在电机关闭且不在运动中时更改（在开启电机并启用 [GantryOn](GantryOn.md) 之前进行配置）。在两种模式下，**偏摆**（差模）环路仍从两个电机编码器运行，因此控制器仍向两个电机注入偏摆校正电流以保持横梁对正；双环设置仅改变*线性*位置的测量方式。

这是单轴双环功能在龙门场景的对应实现：线性环路在负载端闭环，而电机编码器稳定内环并测量偏摆。负载单位与电机单位之间的双环缩放因子与单轴双环相同。

## 工作原理

在单环模式下，控制器由两个电机编码器（均值）形成共模位置，因此主轴上的 [GantryFdbk](../02-gantry-kinematic-feedback/GantryFdbk.md) 是线性环路的跟随位置。在双环模式下，控制器改为使用 [GantryFdbkSrc](../02-gantry-kinematic-feedback/GantryFdbkSrc.md) 选择的负载反馈作为线性环路，并将电机编码器均值报告为辅助反馈 [GantryAuxFdbk](../02-gantry-kinematic-feedback/GantryAuxFdbk.md)；速度环在经双环因子缩放后的辅助（电机编码器）速度 [GantryAuxVel](../02-gantry-kinematic-feedback/GantryAuxVel.md) 上运行。控制器还根据双环因子调整内部位置限制和跟随误差边界，并在接入时捕获偏置，使报告的线性位置不发生跳变。完整的各模式反馈和速度源表，请参见[双环龙门控制概述](../04-dual-loop-gantry-control/00-overview.md)。

## 示例

```text
AGantryDLoopOn=1     ; 将线性龙门环路闭合至负载反馈（双环）
AGantryDLoopOn=0     ; 将线性环路闭合至电机编码器（单环）
AGantryDLoopOn       ; 读取已配置的模式
```

### 边界情况

- **电机使能或运动中写入**——被拒绝（`NOMOTN`、`NOMTRON`）。请在启用任一龙门成员之前配置双环模式。
- **超出范围**——`0`–`1` 之外的值将被拒绝。
- **设置在错误轴上**——引擎在**主轴**（与 [GantryOn](GantryOn.md) 设置在同一轴）上读取 `GantryDLoopOn`。在偏摆轴或非龙门轴上的写入虽被接受，但不会被查询。
- **`GantryDLoopOn = 1` 而无有效的 [GantryFdbkSrc](../02-gantry-kinematic-feedback/GantryFdbkSrc.md)**——负载反馈指针回落至零，线性环路无实时参考；请在启用龙门之前配置 `GantryFdbkSrc`。
- **偏摆环路不变**——在两种模式下，差模（偏摆）环路仍在电机编码器上运行；仅线性测量源发生改变。
- **保存**——可保存至闪存；启动时重新加载。
- **平台**——仅限 v5 central-i。v4 不支持双环龙门。

## 另请参阅

- [GantryOn](GantryOn.md) — 启用龙门 MIMO 控制
- [GantryFdbkSrc](../02-gantry-kinematic-feedback/GantryFdbkSrc.md) — 当本参数为 1 时使用的负载反馈源
- [GantryAuxFdbk](../02-gantry-kinematic-feedback/GantryAuxFdbk.md) / [GantryAuxVel](../02-gantry-kinematic-feedback/GantryAuxVel.md) — 双环模式下的辅助（电机编码器）反馈和速度
- [GantryYawRef](GantryYawRef.md) — 偏摆校正参考值
- [GantryPosGain](../03-gantry-tuning/GantryPosGain.md) — 偏摆位置环增益
