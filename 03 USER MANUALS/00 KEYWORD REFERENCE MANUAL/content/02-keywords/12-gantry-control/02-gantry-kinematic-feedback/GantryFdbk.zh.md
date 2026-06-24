---
keyword: GantryFdbk
summary: 只读 MIMO 龙门反馈；A 轴报告均值位置，B 轴报告差值。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 652
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# GantryFdbk

只读 MIMO 龙门反馈；A 轴报告均值位置，B 轴报告差值。

## 概述

`GantryFdbk` 是一个只读参数，提供两个 MIMO 龙门反馈——即 [GantryOn](../01-general-variables/GantryOn.md) 中所描述的共模环和差模环的输入。主轴值报告龙门共模（均值）位置，线性位置环跟随该值；偏摆轴值报告两个梁端之间的差值位置（偏摆），偏摆环将其保持在 [GantryYawRef](../01-general-variables/GantryYawRef.md) 目标。反馈仅在主轴 `GantryOn` 为 1 时每周期重新计算；龙门关闭时，报告值为旧值（上次龙门开启周期锁存的值，若龙门在上电后从未启用则为 `0`）。以用户单位报告；在 central-i v5 上为 64 位值。

## 工作原理

反馈将两个电机位置合并，并折入 [GantryOffset](GantryOffset.md) 中捕获的初始偏置：

```text
AGantryFdbk = (APos + BPos + AGantryOffset) / 2     ; 共模（均值）- 线性位置
BGantryFdbk = (APos - BPos - AGantryOffset)         ; 差值 - 偏摆
```

（简化形式 `AGantryFdbk = (APos + BPos) / 2` 和 `BGantryFdbk = (APos - BPos)` 省略了偏置项以便阅读。）

差值**故意不**除以二：保留完整的 `APos - BPos` 差值可为偏摆环保留测量分辨率，该环只需将差值驱动至目标，而无需报告真实的中间缩放角度。

当位置相关解耦映射表启用时（[GantryMapType](../01-general-variables/GantryMapType.md) = 1，仅 v5），共模反馈不再是简单的 50/50 均值：两个电机位置使用映射比（[GantryMapVal](../01-general-variables/GantryMapVal.md)）混合，以便沿梁移动有效线性测量点。在双环龙门模式下（[GantryDLoopOn](../01-general-variables/GantryDLoopOn.md) = 1），主轴值改为反映由 [GantryFdbkSrc](GantryFdbkSrc.md) 选择的负载反馈，电机编码器均值则单独报告为 [GantryAuxFdbk](GantryAuxFdbk.md)。

## 示例

```text
AGantryFdbk        ; 读取龙门均值（共模）位置
BGantryFdbk        ; 读取龙门差值（偏摆）位置
```

### 边界情况

- **龙门关闭**——`GantryFdbk` 不更新。值反映上次龙门开启周期的状态，若龙门从未启用则为 `0`。龙门关闭时请直接使用 [Pos](../../10-motion/01-kinematics-status/Pos.md)。
- **电机失能**——任一成员轴电机关闭均会强制该对轴的 `GantryOn` 回到 `0` 并停止反馈更新；若 A 轴和 B 轴的电机状态不一致，则在仍处于使能状态的轴上记录 [ConFlt](../../07-status-and-faults/ConFlt.md) 代码 `1061`（另一龙门成员轴电机关闭）。
- **非龙门轴**——在既非主轴也非偏摆轴的轴上读取返回 `0`。
- **双环**（[GantryDLoopOn](../01-general-variables/GantryDLoopOn.md) = 1）——主轴值反映由 [GantryFdbkSrc](GantryFdbkSrc.md) 选择的负载反馈；电机编码器均值显示在 [GantryAuxFdbk](GantryAuxFdbk.md) 上。
- **解耦映射表**（[GantryMapType](../01-general-variables/GantryMapType.md) = 1，仅 v5）——共模值为基于位置混合的均值，而非简单的 50/50 均值。
- **仿真**——若仿真电机正在运行且龙门已开启，值正常更新。

## 另请参阅

- [GantryOffset](GantryOffset.md) — 折叠入本反馈的初始 A/B 偏置
- [GantryOn](../01-general-variables/GantryOn.md) — 启用龙门 MIMO 控制；说明共模与差模模式
- [GantryYawRef](../01-general-variables/GantryYawRef.md) — 由差值反馈指令的偏摆校正
- [GantryMapType](../01-general-variables/GantryMapType.md) — 对共模反馈重新加权的解耦映射表
- [GantryAuxFdbk](GantryAuxFdbk.md) — 使用双环龙门时的电机编码器反馈
